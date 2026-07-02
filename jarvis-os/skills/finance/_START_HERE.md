Ta mapa je še prazna.

Ko boš pripravljen dodati prvi skill v "finance" branch:
1. Skopiraj /jarvis-os/SKILL_TEMPLATE.md v finance/ime-skilla/SKILL.md
2. Izpolni trigger (description), kontekst, pravila, pogoste naloge
3. Izbriši to datoteko, ko finance/ ni več prazna

Ideja za "finance": fakturiranje, mesečni pregled stroškov/prihodkov agencije

## 3 konkretne ideje za skille

1. **fakturiranje** — mesečni checklist: za vsakega aktivnega klienta iz
   `vault/clients/` preveri, ali je bila storitev opravljena (poročila v
   `vault/reports/`), pripravi postavke za račun (opis, količina, cena)
   kot osnutek — samega izdajanja računov NE avtomatiziraj.
2. **mesecni-pregled** — prihodki/stroški agencije po mesecu v
   `vault/reference/finance-YYYY.md`: naročnine (hosting, API-ji, orodja),
   prihodek po klientu, marža po storitvi (WP / IG / RAG) — pokaže,
   katera storitev se najbolj splača.
3. **api-cost-tracker** — spremljanje stroškov Anthropic/Gemini/Supabase
   po klientskem projektu (pomembno za chatbot kliente kot ambulanta-dolinar):
   mesečni zapis porabe, opozorilo če strošek preseže dogovorjen prag.
