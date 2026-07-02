#!/usr/bin/env python3
"""Jarvis OS — lokalni glasovni pipeline.

    mikrofon → faster-whisper (STT) → claude -p → Piper/espeak (TTS) → zvočnik

Način: push-to-talk (Enter za start, Enter za stop). Ctrl+C za izhod.
Nastavitve: config.yaml v isti mapi. Testiranje brez mikrofona: test.py.
"""

import shutil
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np
import yaml

VOICE_DIR = Path(__file__).resolve().parent


def load_config() -> dict:
    with open(VOICE_DIR / "config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


# ---------------------------------------------------------------- snemanje

def record_push_to_talk(cfg: dict) -> np.ndarray:
    """Posname mikrofon med dvema pritiskoma Enter. Vrne float32 mono signal."""
    import sounddevice as sd  # import tu, da test.py dela tudi brez zvočne kartice

    audio_cfg = cfg["audio"]
    rate = int(audio_cfg["sample_rate"])
    chunks: list[np.ndarray] = []

    def callback(indata, _frames, _time, status):
        if status:
            print(f"  [avdio opozorilo] {status}", file=sys.stderr)
        chunks.append(indata.copy())

    input("🎙  Pritisni Enter za ZAČETEK snemanja...")
    stream = sd.InputStream(
        samplerate=rate,
        channels=int(audio_cfg["channels"]),
        dtype="float32",
        device=audio_cfg.get("input_device"),
        callback=callback,
    )
    with stream:
        input("⏺  Snemam — pritisni Enter za KONEC...")

    if not chunks:
        return np.zeros(0, dtype=np.float32)
    audio = np.concatenate(chunks, axis=0)
    return audio.mean(axis=1) if audio.ndim > 1 else audio


# ---------------------------------------------------------------- STT

_whisper_model = None


def get_whisper(cfg: dict):
    """Naloži faster-whisper model (ob prvem klicu; model se prenese sam)."""
    global _whisper_model
    if _whisper_model is None:
        from faster_whisper import WhisperModel

        stt = cfg["stt"]
        print(f"⏳ Nalagam whisper model '{stt['model']}' (prvič se prenese)...")
        _whisper_model = WhisperModel(
            stt["model"], device=stt["device"], compute_type=stt["compute_type"]
        )
    return _whisper_model


def transcribe(cfg: dict, audio: np.ndarray, language: str | None = None) -> str:
    model = get_whisper(cfg)
    lang = language or cfg["stt"].get("language")
    segments, _info = model.transcribe(audio, language=lang, vad_filter=True)
    return " ".join(seg.text.strip() for seg in segments).strip()


def transcribe_wav(cfg: dict, wav_path: Path, language: str | None = None) -> str:
    """Transkribira WAV datoteko (uporablja test.py)."""
    model = get_whisper(cfg)
    lang = language or cfg["stt"].get("language")
    segments, _info = model.transcribe(str(wav_path), language=lang, vad_filter=True)
    return " ".join(seg.text.strip() for seg in segments).strip()


# ---------------------------------------------------------------- Claude

def ask_claude(cfg: dict, text: str) -> str:
    c = cfg["claude"]
    cmd = [c["command"], "-p", text, *c.get("extra_args", [])]
    result = subprocess.run(
        cmd, capture_output=True, text=True, timeout=int(c["timeout"])
    )
    if result.returncode != 0:
        raise RuntimeError(f"claude CLI napaka: {result.stderr.strip()[:500]}")
    return result.stdout.strip()


# ---------------------------------------------------------------- TTS

def piper_voice_paths(cfg: dict) -> tuple[Path, Path]:
    tts = cfg["tts"]
    vdir = VOICE_DIR / tts["piper_voices_dir"]
    onnx = vdir / f"{tts['piper_voice']}.onnx"
    return onnx, onnx.with_suffix(".onnx.json")


def ensure_piper_voice(cfg: dict) -> bool:
    """Vrne True, če je piper glas na voljo (po potrebi ga poskusi prenesti)."""
    onnx, cfg_json = piper_voice_paths(cfg)
    if onnx.exists() and cfg_json.exists():
        return True
    vdir = onnx.parent
    vdir.mkdir(parents=True, exist_ok=True)
    voice = cfg["tts"]["piper_voice"]
    print(f"⏳ Piper glas '{voice}' manjka — poskušam prenesti (huggingface)...")
    try:
        subprocess.run(
            [sys.executable, "-m", "piper.download_voices",
             "--download-dir", str(vdir), voice],
            check=True, capture_output=True, text=True, timeout=600,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        print(f"  prenos ni uspel ({e}); uporabim espeak-ng fallback.")
        return False
    return onnx.exists() and cfg_json.exists()


def resolve_tts_engine(cfg: dict) -> str:
    """Vrne 'piper' ali 'espeak' glede na config in dostopnost glasu."""
    engine = cfg["tts"].get("engine", "auto")
    if engine == "espeak":
        return "espeak"
    if ensure_piper_voice(cfg):
        return "piper"
    if engine == "piper":
        raise RuntimeError(
            "tts.engine=piper, a glas ni na voljo (glej voices/ in README)."
        )
    return "espeak"


def synthesize_to_wav(cfg: dict, text: str, out_path: Path, engine: str) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if engine == "piper":
        from piper import PiperVoice

        onnx, _ = piper_voice_paths(cfg)
        voice = PiperVoice.load(onnx)
        with wave.open(str(out_path), "wb") as wf:
            voice.synthesize_wav(text, wf)
    else:  # espeak-ng
        tts = cfg["tts"]
        subprocess.run(
            ["espeak-ng", "-v", str(tts["espeak_voice"]),
             "-s", str(tts["espeak_speed"]), "-w", str(out_path), text],
            check=True, capture_output=True, timeout=120,
        )


def play_wav(cfg: dict, wav_path: Path) -> None:
    import sounddevice as sd

    with wave.open(str(wav_path), "rb") as wf:
        rate = wf.getframerate()
        frames = wf.readframes(wf.getnframes())
        audio = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0
        if wf.getnchannels() > 1:
            audio = audio.reshape(-1, wf.getnchannels())
    sd.play(audio, samplerate=rate, device=cfg["audio"].get("output_device"))
    sd.wait()


def speak(cfg: dict, text: str, engine: str) -> None:
    tmp = VOICE_DIR / ".last_reply.wav"
    synthesize_to_wav(cfg, text, tmp, engine)
    play_wav(cfg, tmp)


# ---------------------------------------------------------------- glavna zanka

def main() -> None:
    cfg = load_config()
    if shutil.which(cfg["claude"]["command"]) is None:
        sys.exit("Napaka: 'claude' CLI ni v PATH — namesti Claude Code.")

    engine = resolve_tts_engine(cfg)
    print(f"Jarvis pripravljen. STT={cfg['stt']['model']}  TTS={engine}  "
          f"(Ctrl+C za izhod)\n")
    get_whisper(cfg)  # naloži model vnaprej, da prvi ukaz ni počasen

    while True:
        try:
            audio = record_push_to_talk(cfg)
            if len(audio) < cfg["audio"]["sample_rate"] * 0.3:
                print("  (prekratek posnetek, poskusi znova)\n")
                continue
            text = transcribe(cfg, audio)
            if not text:
                print("  (nisem razumel, poskusi znova)\n")
                continue
            print(f"\n🗣  Ti: {text}")
            print("⏳ Claude razmišlja...")
            reply = ask_claude(cfg, text)
            print(f"🤖 Jarvis: {reply}\n")
            speak(cfg, reply, engine)
        except KeyboardInterrupt:
            print("\nAdijo. 👋")
            break
        except Exception as e:  # ena napaka naj ne ubije cele seje
            print(f"⚠️  Napaka: {e}\n", file=sys.stderr)


if __name__ == "__main__":
    main()
