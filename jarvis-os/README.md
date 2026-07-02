# Jarvis OS — Osebni AI Command Center

Voice-driven AI operacijski sistem. Skill-based arhitektura + Obsidian vault
za trajen spomin + (opcijsko) lokalen glas. Zasnovan tako, da ga je mogoče
forkati/reskinati za vsakega Kore klienta posebej.

## Struktura

```
jarvis-os/
├── skills/              KORAK 1 — možgani sistema
│   ├── memory/
│   ├── productivity/
│   ├── research/
│   ├── content/
│   ├── community/
│   ├── agency/          ← Kore klientski projekti (en podfolder na klienta)
│   ├── sales/
│   ├── finance/
│   └── ops-custom/
├── vault/                KORAK 2 — dolgoročni spomin (Obsidian)
│   ├── daily/            dnevni zapiski (2026-07-03.md)
│   ├── clients/          en folder na klienta
│   ├── reports/          avto-generirana poročila
│   └── reference/        trajne opombe, odločitve, arhitektura
├── voice/                KORAK 3 — lokalni glas (mic → STT → Claude → TTS)
│   ├── pipeline.py       glavna zanka (push-to-talk)
│   ├── test.py           testi po členih, brez mikrofona
│   ├── config.yaml       model, jezik, glas, sample rate
│   └── README.md         zagon, menjava glasu/modela, znani problemi
└── SKILL_TEMPLATE.md     kopiraj to za vsak nov skill
```

## Kako deluje

- Claude Code prebere SAMO tisti `SKILL.md`, ki je relevanten za trenutni
  task — ne celotne mape. To drži kontekst majhen.
- Vsak `SKILL.md` ima `description` polje na vrhu (YAML-style), ki pove
  KDAJ naj se skill sproži — to je edini del, ki ga Claude vidno "skenira"
  vnaprej, zato mora biti oster in specifičen (glej primer spodaj).
- Vault je čisti markdown + `[[wikilinki]]` — brez baze. Supabase (če/ko ga
  uporabljaš prek n8n) ostane za strukturirane podatke (klienti, produkti,
  metrike); vault je za nestrukturiran spomin — odločitve, konteksti,
  poročila v naravnem jeziku.

## Stanje (2026-07-03, po nočni gradnji)

1. **Skills** ✅: pravi skilli v `productivity/daily-planning`,
   `content/instagram-manager`, `research/client-research`,
   `agency/ambulanta-dolinar` (referenčni), `agency/mera-care` (skelet s
   TODO — čaka podatke o klientu) in `memory/vault-sync`. Branchi
   `community`, `sales`, `finance`, `ops-custom` so stub-i, vsak s 3
   konkretnimi idejami v `_START_HERE.md`.
2. **Vault** ✅: `vault/reference/jarvis-os-arhitektura.md` opisuje celoten
   sistem. `vault/clients/dolinar/` ostaja skelet — vsebino je treba
   preliti iz obstoječega dela (ročno).
3. **Glas (Korak 3)** ✅ koda / ⏳ ročni test: `voice/` vsebuje delujoč
   pipeline (faster-whisper STT + Piper/espeak TTS + `claude -p`).
   `voice/test.py` je v sandboxu potrdil TTS in Claude CLI; prenos whisper
   modela, mikrofon in zvočnik rabijo **ročni test na tvojem stroju** —
   glej `voice/README.md` in "Za pregled zjutraj" v
   `vault/daily/2026-07-03.md`. Slovenskega Piper glasu ni (angleški
   privzet, espeak-ng za silo govori slovensko).

## Kako dodam nov skill

1. Skopiraj `SKILL_TEMPLATE.md` v ustrezno branch mapo, npr.
   `skills/agency/mera-care/SKILL.md`
2. Izpolni `name`, `description` (trigger — bodi specifičen, da se skill
   ne sproži po nepotrebnem), in telo (kontekst, pravila, pogoste naloge).
3. Poveži skill z vault mapo klienta, če obstaja (`vault/clients/...`).
