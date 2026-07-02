Ta mapa je še prazna.

Ko boš pripravljen dodati prvi skill v "ops-custom" branch:
1. Skopiraj /jarvis-os/SKILL_TEMPLATE.md v ops-custom/ime-skilla/SKILL.md
2. Izpolni trigger (description), kontekst, pravila, pogoste naloge
3. Izbriši to datoteko, ko ops-custom/ ni več prazna

Ideja za "ops-custom": vse kar ne sodi drugam: enkratni skripti, interna orodja

## 3 konkretne ideje za skille

1. **wp-maintenance** — mesečno vzdrževanje WordPress strani klientov:
   checklist (backup, update jedra/pluginov/tem, varnostni pregled,
   hitrostni test), rezultat v `vault/reports/YYYY-MM-wp-maintenance.md`;
   seznam strani in dostopov v `vault/reference/wp-portfolio.md`.
2. **voice-ops** — upravljanje glasovnega pipeline-a iz `voice/`:
   menjava STT/TTS modela, diagnostika ("zakaj me ne sliši"), dodajanje
   novih glasov; glej [[jarvis-os-arhitektura]] in `voice/README.md`.
3. **n8n-workflows** — katalog n8n avtomatizacij agencije: kaj vsak
   workflow dela, kje teče, kako se ga restarta/debugira; povezano z
   [[rag-stack-supabase-n8n]] (ingestion in poročila).
