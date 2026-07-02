# Jarvis OS — Arhitektura

Kako sistem deluje, kako se dodaja skille in kako teče voice pipeline.
Zadnja posodobitev: [[2026-07-03]] (nočna avtonomna gradnja).

## Trije stebri

```
glas (voice/)  →  možgani (skills/ + Claude Code)  →  spomin (vault/)
```

1. **skills/** — možgani. Vsak skill je ena mapa z `SKILL.md`. Claude Code
   ob tasku prebere SAMO relevanten skill (izbor prek `description`
   trigger polja v YAML glavi), ne celotne mape — kontekst ostane majhen.
2. **vault/** — dolgoročni spomin. Čisti markdown + `[[wikilinki]]`,
   Obsidian-kompatibilno, brez baze. Pravila pisanja določa skill
   `skills/memory/vault-sync/SKILL.md`.
3. **voice/** — lokalen glasovni vmesnik (mic → STT → Claude → TTS).
   Podrobnosti spodaj in v `voice/README.md`.

## Kako se doda nov skill

1. Kopiraj `SKILL_TEMPLATE.md` v `skills/<branch>/<ime-skilla>/SKILL.md`.
2. Napiši oster `description` trigger: KDAJ se sproži + KDAJ se NE
   (meja do sosednjih skillov). To je edini del, ki se "skenira" vnaprej.
3. Izpolni: KONTEKST, PRAVILA (trde omejitve), POGOSTE NALOGE (tabela),
   POVEZAVE na vault, TODO.
4. Poveži s klientsko mapo `vault/clients/<klient>/`, če gre za klienta.
5. Če je bila branch mapa prazna, izbriši njen `_START_HERE.md`.

Referenčni primer dobro izpolnjenega skilla: `skills/agency/ambulanta-dolinar/SKILL.md`.
Skelet z TODO oznakami (klient brez potrjenih podatkov): `skills/agency/mera-care/SKILL.md`.

## Stanje skillov (2026-07-03)

| Branch | Stanje |
|---|---|
| productivity | ✅ daily-planning (jutranji ritual) |
| content | ✅ instagram-manager (calendar + copywriting) |
| research | ✅ client-research (pre-sales brief) |
| agency | ✅ ambulanta-dolinar (referenčni), mera-care (skelet s TODO) |
| memory | ✅ vault-sync (pravila pisanja v vault) |
| community, sales, finance, ops-custom | stub — `_START_HERE.md` s 3 konkretnimi idejami |

## Voice pipeline (voice/)

```
mikrofon ──sounddevice──▶ WAV v RAM
              │  push-to-talk: Enter = start, Enter = stop
              ▼
     faster-whisper (STT, model "small", jezik sl)
              ▼  tekst
     claude -p "<tekst>"   (Claude Code CLI — isti možgani kot skills/)
              ▼  odgovor
     Piper (TTS, ONNX glas)
              ▼
     zvočnik (sounddevice playback)
```

- Vse nastavitve v `voice/config.yaml` (STT model, jezik, TTS glas,
  sample rate, claude ukaz).
- STT: `faster-whisper` (pip), privzet model `small`, CPU/int8 —
  menjava modela = ena vrstica v configu, prenese se sam ob prvem zagonu.
- TTS: Piper (`piper-tts` pip paket). **Slovenskega glasu v uradnem piper
  katalogu ni** (preverjeno 2026-07-03) → privzet je angleški
  `en-us-lessac-medium`; slovenski vnos vprašanja prek STT vseeno dela
  (whisper podpira slovenščino), samo odgovor je prebran z angleškim glasom.
- Testiranje brez mikrofona: `voice/test.py` preveri vsak člen posebej
  (TTS → generira test WAV → STT ga transkribira → claude CLI ping).
- Mikrofonski del se ne da testirati v oblaku — ročni test na Gregorjevem
  stroju (glej [[2026-07-03]] "Za pregled zjutraj").

## Omejitve okolja, v katerem je bilo to zgrajeno

Nočna gradnja je tekla v Claude Code remote sandboxu z omejeno mrežo
(dovoljena samo PyPI in GitHub; huggingface.co blokiran) — zato:
- piper glas je prenesen z GitHub release-a namesto s HuggingFace,
- faster-whisper modela ni bilo mogoče prenesti v sandboxu; na
  Gregorjevem stroju se prenese sam ob prvem zagonu (HF dostop).

## Povezano
- [[rag-stack-supabase-n8n]] — klientska RAG arhitektura (ločeno od Jarvisa)
- [[2026-07-03]] — dnevnik nočne gradnje z vsemi odločitvami
- `voice/README.md` — zagon, menjava glasu/modela, znani problemi
