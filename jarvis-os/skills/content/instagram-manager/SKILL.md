---
name: instagram-manager
branch: content
description: >
  Instagram management za Kore kliente: content calendar, copywriting
  (captioni, hooki, CTA), ideje za objave/reels/stories. Sproži se ob:
  "instagram plan za [klient]", "napiši caption", "content calendar",
  "ideje za objave", "story za [klient]". NE uporabljaj za odgovarjanje
  na komentarje/DM-je (to je community branch) ali za blog/web copy
  (to gre v klientski agency skill).
---

# SKILL: Instagram Manager — calendar + copywriting

## KONTEKST
- Klient / projekt: več Kore klientov (vsak ima svoj glas in pravila)
- Deliverable: mesečni content calendar + posamezni captioni/scenariji
- Stack / orodja: vault/clients/<klient>/instagram.md za profil klienta,
  vault/reports/ za mesečne povzetke
- Status: aktiven — ponavljajoča storitev agencije

## PRAVILA
- PREDEN pišeš za klienta, preberi njegov profil v
  `vault/clients/<klient>/instagram.md` (ton, prepovedane teme, hashtagi).
  Če datoteka ne obstaja, jo najprej ustvari z vprašanji za Gregorja —
  NE ugibaj klientovega glasu.
- Medicinski klienti (Dolinar, Méra Care): brez zdravstvenih trditev,
  brez obljub rezultatov, brez diagnoz — enaka pravila kot chatbot.
- Vedno slovenščina, razen če klientov profil določa drugače.
- Objav NIKOLI ne objavljaš sam — deliverable je vedno osnutek za potrditev.
- Vsak calendar ima za vsako objavo: datum, format (post/reel/story),
  hook, caption, CTA, predlog vizuala.

## POGOSTE NALOGE

| Naloga | Kaj narediti |
|---|---|
| Mesečni calendar | Preberi klientov profil + pretekle objave → predlagaj 8–12 objav z datumi → zapiši v `vault/clients/<klient>/instagram-calendar-YYYY-MM.md` |
| Caption za objavo | Hook (1. vrstica) → vrednost/zgodba → CTA → hashtagi po klientovem profilu |
| Ideje za reels | 5 idej s scenarijem (hook v prvih 2 s, struktura, CTA) prilagojenih klientovi niši |
| Mesečno poročilo | Povzemi objavljeno + metrike (če jih Gregor poda) v `vault/reports/YYYY-MM-<klient>-instagram.md` |
| Nov klient | Ustvari `vault/clients/<klient>/instagram.md` profil: ciljna publika, ton, teme, tabuji, hashtag seti |

## POVEZAVE (vault)
- `vault/clients/<klient>/instagram.md` — profil glasu po klientu
- `vault/reports/` — mesečni content povzetki
- `vault/reference/jarvis-os-arhitektura.md` — [[jarvis-os-arhitektura]]

## TODO / NASLEDNJI KORAKI
- [ ] Ustvariti instagram.md profile za obstoječe kliente (rabim podatke od Gregorja)
- [ ] Standardizirati hashtag strategijo (velikost setov, rotacija)
