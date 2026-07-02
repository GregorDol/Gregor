# Jarvis Voice — lokalni glasovni pipeline

```
mikrofon → faster-whisper (STT) → claude -p → Piper/espeak (TTS) → zvočnik
```

## Zagon

```bash
# enkratna namestitev
pip install faster-whisper piper-tts sounddevice PyYAML
sudo apt install libportaudio2 espeak-ng   # Linux; na macOS: brew install portaudio espeak-ng

# zagon (iz jarvis-os/voice/)
python3 pipeline.py
```

Način: **push-to-talk** — Enter za začetek snemanja, Enter za konec,
Jarvis transkribira, vpraša Claude in odgovor prebere na glas. Ctrl+C za izhod.

Ob **prvem zagonu** se sama preneseta whisper model (~460 MB za "small")
in piper glas (~60 MB) — rabi internet (huggingface.co); potem vse teče lokalno,
razen `claude` CLI, ki gre v Anthropic API.

## Testiranje brez mikrofona

```bash
python3 test.py
```

Testira vsak člen posebej: TTS → testni wav → STT nad njim → `claude -p` ping →
pregled avdio naprav. Mikrofonskega dela se avtomatsko NE da testirati —
to preveriš ročno z `pipeline.py`.

## Menjava modela / glasu (config.yaml)

| Kaj | Kje | Opombe |
|---|---|---|
| STT model | `stt.model` | `tiny`/`base` hitrejši, `medium` natančnejši; prenese se sam |
| Jezik govora | `stt.language` | privzeto `sl` |
| TTS engine | `tts.engine` | `auto` (privzeto), `piper`, `espeak` |
| Piper glas | `tts.piper_voice` | ime iz kataloga, npr. `en_US-ryan-high`; prenese se sam. Ročno: `python3 -m piper.download_voices --download-dir voices <ime>` |
| espeak glas | `tts.espeak_voice` | `sl` = slovenski (robotski) |
| Mikrofon/zvočnik | `audio.input_device` / `output_device` | seznam naprav: `python3 -m sounddevice` |

## Znani problemi

- **Slovenskega Piper glasu ni** v uradnem katalogu (stanje 2026-07).
  Opciji: (a) angleški piper glas — naravno zveni, a odgovori so prebrani
  po angleško izgovorjeno; (b) `tts.engine: espeak` — slovenska izgovorjava,
  a robotski zvok. Dolgoročno: XTTS/Coqui ali treniran piper glas za sl.
- **`PortAudio library not found`** → `sudo apt install libportaudio2`.
- **Prvi odgovor je počasen** — nalaganje whisper modela; pipeline ga zato
  naloži že ob zagonu.
- **`claude` CLI timeout** pri dolgih vprašanjih → povečaj `claude.timeout`.
- **Piper prenos glasu ne uspe** (offline/blokiran huggingface) → pipeline
  sam pade nazaj na espeak-ng in to izpiše.
- V oblaku/sandboxu ni avdio naprav — `test.py` to označi kot SKIP; snemanje
  in predvajanje delata samo na pravem stroju.

Arhitektura celotnega sistema: `../vault/reference/jarvis-os-arhitektura.md`.
