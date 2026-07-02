#!/usr/bin/env python3
"""Jarvis OS — test vsakega člena voice pipeline-a BREZ mikrofona.

    1. TTS  : sintetizira testni stavek v test_output/tts_test.wav
    2. STT  : faster-whisper transkribira ta wav in primerja besede
    3. Claude CLI : `claude -p` ping
    4. Avdio naprave : informativno (mikrofon/zvočnik ni testiran!)

Izhodna koda 0 = noben test ni FAIL (SKIP je dovoljen in izpisan).
"""

import shutil
import subprocess
import sys
import wave
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pipeline  # noqa: E402

OUT_DIR = pipeline.VOICE_DIR / "test_output"

# Testna stavka — izbere se glede na TTS engine, da se STT ujema z jezikom.
SENTENCES = {
    "piper": ("en", "Good morning Gregor, the Jarvis voice system is ready."),
    "espeak": ("sl", "Dobro jutro Gregor, glasovni sistem Jarvis je pripravljen."),
}

results: list[tuple[str, str, str]] = []  # (test, PASS/SKIP/FAIL, detajl)


def report(name: str, status: str, detail: str = "") -> None:
    results.append((name, status, detail))
    icon = {"PASS": "✅", "SKIP": "⏭ ", "FAIL": "❌"}[status]
    print(f"{icon} {name}: {status}" + (f" — {detail}" if detail else ""))


def wav_duration(path: Path) -> float:
    with wave.open(str(path), "rb") as wf:
        return wf.getnframes() / wf.getframerate()


def test_tts(cfg: dict) -> tuple[str, Path | None]:
    """Vrne (engine, pot do wav) ali ('', None) ob neuspehu."""
    try:
        engine = pipeline.resolve_tts_engine(cfg)
    except Exception as e:
        report("TTS", "FAIL", str(e))
        return "", None
    _lang, sentence = SENTENCES[engine]
    out = OUT_DIR / "tts_test.wav"
    try:
        pipeline.synthesize_to_wav(cfg, sentence, out, engine)
        dur = wav_duration(out)
        if dur < 0.5:
            report("TTS", "FAIL", f"wav prekratek ({dur:.2f}s)")
            return "", None
        report("TTS", "PASS", f"engine={engine}, {dur:.1f}s → {out.name}")
        return engine, out
    except Exception as e:
        report("TTS", "FAIL", f"engine={engine}: {e}")
        return "", None


def test_stt(cfg: dict, engine: str, wav: Path | None) -> None:
    if wav is None:
        report("STT", "SKIP", "ni TTS wav-a za transkripcijo")
        return
    lang, sentence = SENTENCES[engine]
    try:
        text = pipeline.transcribe_wav(cfg, wav, language=lang)
    except Exception as e:
        msg = str(e)
        if any(k in msg.lower() for k in ("huggingface", "connection", "proxy",
                                          "network", "403", "name resolution")):
            report("STT", "SKIP",
                   f"whisper modela ni bilo mogoče prenesti (mreža): {msg[:120]}")
        else:
            report("STT", "FAIL", msg[:200])
        return
    want = {w.strip(".,!?").lower() for w in sentence.split()}
    got = {w.strip(".,!?").lower() for w in text.split()}
    overlap = len(want & got) / max(len(want), 1)
    if overlap >= 0.5 and text:
        report("STT", "PASS", f'"{text}" (ujemanje {overlap:.0%})')
    else:
        report("STT", "FAIL", f'transkript "{text}" (ujemanje {overlap:.0%})')


def test_claude(cfg: dict) -> None:
    if shutil.which(cfg["claude"]["command"]) is None:
        report("Claude CLI", "FAIL", "'claude' ni v PATH")
        return
    try:
        reply = pipeline.ask_claude(cfg, "Odgovori samo z besedo: DELUJE")
        if reply:
            report("Claude CLI", "PASS", f'odgovor: "{reply[:60]}"')
        else:
            report("Claude CLI", "FAIL", "prazen odgovor")
    except Exception as e:
        report("Claude CLI", "FAIL", str(e)[:200])


def test_audio_devices() -> None:
    """Informativno — mikrofona/zvočnika se BREZ človeka ne da zares testirati."""
    try:
        import sounddevice as sd

        devs = sd.query_devices()
        n_in = sum(1 for d in devs if d["max_input_channels"] > 0)
        n_out = sum(1 for d in devs if d["max_output_channels"] > 0)
        if n_in and n_out:
            report("Avdio naprave", "PASS",
                   f"{n_in} vhod / {n_out} izhod — ročno preizkusi pipeline.py")
        else:
            report("Avdio naprave", "SKIP",
                   f"vhod={n_in}, izhod={n_out} — na tem stroju ni mikrofona/zvočnika")
    except Exception as e:
        report("Avdio naprave", "SKIP", f"sounddevice ni uporaben tukaj: {str(e)[:100]}")


def main() -> int:
    cfg = pipeline.load_config()
    OUT_DIR.mkdir(exist_ok=True)
    print("=== Jarvis voice — testi po členih (brez mikrofona) ===\n")
    engine, wav = test_tts(cfg)
    test_stt(cfg, engine or "espeak", wav)
    test_claude(cfg)
    test_audio_devices()

    print("\n=== Povzetek ===")
    for name, status, _ in results:
        print(f"  {status:4}  {name}")
    fails = [r for r in results if r[1] == "FAIL"]
    if fails:
        print("\nNekateri testi so FAIL — glej zgoraj.")
        return 1
    print("\nVsi izvedljivi testi OK. Mikrofon/zvočnik = ročni test (pipeline.py).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
