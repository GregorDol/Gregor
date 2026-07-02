---
name: mera-care
branch: agency
description: >
  Uporabi ta skill za VSE naloge povezane s klientom Méra Care.
  Sproži se ob: vprašanjih o Méra Care projektu, spremembah na njihovi
  strani/chatbotu, klientskih poročilih ali komunikaciji s tem klientom.
  NE uporabljaj za Ambulanto Dolinar (ima svoj skill) ali splošna Kore
  vprašanja. TODO: ko so znani detajli projekta, zaostri ta trigger.
---

# SKILL: Méra Care

> Skelet po vzoru [[../ambulanta-dolinar/SKILL|ambulanta-dolinar]].
> TODO oznake pomenijo: podatka NIMAM — vprašaj Gregorja, ne izmišljuj si.

## KONTEKST PROJEKTA
- Klient: Méra Care — TODO: panoga, kontaktna oseba, lokacija
- Deliverable: TODO (WordPress stran? AI chatbot? Instagram? kombinacija?)
- Stack: TODO (če chatbot: predvidoma po vzoru [[../../../vault/reference/rag-stack-supabase-n8n|rag-stack-supabase-n8n]])
- Status: TODO (pre-sales / v razvoju / live?)

## ARHITEKTURA
- TODO: dopolni, ko je deliverable potrjen. Če gre za chatbot, kopiraj
  4-slojno strukturo iz ambulanta-dolinar in prilagodi.

## KLJUČNA PRAVILA
- Dokler KONTEKST vsebuje TODO oznake, pred vsako klientsko nalogo
  preveri manjkajoče podatke pri Gregorju — nikoli ne ugibaj dejstev
  o klientu (cene, storitve, ton, obljube).
- Če je Méra Care zdravstveni/wellness klient: veljajo ista varnostna
  pravila kot pri Dolinarju — brez diagnoz, brez obljub rezultatov,
  ob negotovosti preusmeritev na osebni kontakt. TODO: potrdi panogo.
- TODO: jezik in ton komunikacije (predvidoma slovenščina, vikanje).

## POGOSTE NALOGE

| Naloga | Kaj narediti |
|---|---|
| TODO | Dopolni, ko so znani deliverable in ponavljajoče naloge |
| Klientsko poročilo | Po vzoru dolinar: povzemi delo/uporabo v `vault/clients/mera-care/porocila/` |

## POVEZAVE (vault)
- `vault/clients/mera-care/` — klientski folder (trenutno prazen skelet)
- `vault/clients/dolinar/` — referenčni vzor strukture
- `vault/reference/rag-stack-supabase-n8n.md` — če projekt vključuje RAG/chatbot

## TODO / NASLEDNJI KORAKI
- [ ] Gregor: izpolni KONTEKST (panoga, deliverable, stack, status)
- [ ] Ustvariti `vault/clients/mera-care/arhitektura.md` in `knowledge-base.md` po vzoru dolinar
- [ ] Zaostriti description/trigger, ko je jasen obseg projekta
