---
name: vault-sync
branch: memory
description: >
  Pravila, kdaj in kam Claude zapisuje v vault. Sproži se ob: koncu
  vsakega delovnega bloka, ob sprejeti odločitvi, ob "zapiši to",
  "zabeleži", "shrani v vault", ali ko drug skill proizvede vsebino,
  ki mora preživeti sejo. NE uporabljaj za branje vaulta (to delajo
  drugi skilli sami) — ta skill določa SAMO pravila pisanja.
---

# SKILL: Vault Sync — kam se kaj zapiše

## KONTEKST
- Klient / projekt: interno — spomin Jarvis OS
- Deliverable: konsistenten, povezan vault brez izgubljenih informacij
- Stack / orodja: vault/ (čisti markdown + [[wikilinki]], Obsidian-kompatibilno)
- Status: aktiven — velja za vse skille

## PRAVILA — ODLOČITVENO DREVO (kam gre zapis)

| Vsebina | Cilj | Primer |
|---|---|---|
| Kaj se je danes delalo, odločitve dneva, TODO za jutri | `vault/daily/YYYY-MM-DD.md` | "Izbral piper glas X, ker Y" |
| Dejstvo/kontekst o ENEM klientu | `vault/clients/<klient>/...` | ordinacijski čas, IG ton, arhitektura projekta |
| Znanje, ki velja za VEČ klientov/projektov | `vault/reference/...` | RAG stack, jarvis arhitektura, standardi |
| Generirano poročilo (mesečno, avtomatsko) | `vault/reports/YYYY-MM-....md` | mesečno IG poročilo |

- Daily je append-only dnevnik: nikoli ne prepisuj starih dni; današnjega
  samo dopolnjuj v obstoječe sekcije (`## Danes`, `## Odločitve`,
  `## Odprto / TODO jutri`).
- Vsaka avtonomna odločitev (sprejeta brez Gregorja) MORA v današnji
  daily pod `## Odločitve`, z razlogom v enem stavku.
- Ista informacija živi na ENEM mestu; povsod drugod se nanjo kaže z
  wikilinkom — ne kopiraj vsebine med datotekami.
- Nikoli ne briši vault datotek brez izrecnega naročila.

## FORMAT WIKILINKOV
- Znotraj vaulta: `[[ime-datoteke]]` brez končnice `.md`
  (npr. `[[rag-stack-supabase-n8n]]`, `[[2026-07-03]]`).
- Ob dvoumnem imenu uporabi pot znotraj vaulta: `[[dolinar/arhitektura]]`.
- Prikazno ime po potrebi: `[[dolinar/arhitektura|arhitektura chatbota]]`.
- Iz skillov proti vaultu (izven Obsidiana) navedi tudi polno pot v
  backtickih, da povezava dela v obeh svetovih.

## POGOSTE NALOGE

| Naloga | Kaj narediti |
|---|---|
| Konec delovnega bloka | Odločitve + narejeno + odprto → današnji daily |
| Nova trajna ugotovitev | Ustrezna datoteka v reference/ ali clients/, wikilink iz daily zapiska nanjo |
| Nov klient | Ustvari `vault/clients/<klient>/` in povezavo iz skilla v agency/ |
| Konflikt (podatek že obstaja drugače) | Ne prepiši tiho — zabeleži oba v daily pod `## Odločitve` in označi za Gregorja |

## POVEZAVE (vault)
- `vault/daily/` — dnevnik
- `vault/reference/jarvis-os-arhitektura.md` — [[jarvis-os-arhitektura]]

## TODO / NASLEDNJI KORAKI
- [ ] Dogovoriti retencijo: ali se stari daily zapiski mesečno povzamejo v reference?
