---
name: client-research
branch: research
description: >
  Pre-sales raziskava novega potencialnega klienta za Kore. Sproži se ob:
  "razišči [podjetje]", "nov lead", "pripravi se na sestanek s [klient]",
  "kaj vemo o [podjetje]". NE uporabljaj za obstoječe kliente (njihov
  kontekst je v agency/ skillih in vault/clients/) niti za splošno
  tržno/tehnološko raziskavo — ta skill je vezan na konkreten lead.
---

# SKILL: Client Research — pre-sales raziskava

## KONTEKST
- Klient / projekt: potencialni Kore klienti (leadi)
- Deliverable: research brief pred prvim sestankom / ponudbo
- Stack / orodja: web search, vault/clients/<lead>/research.md
- Status: aktiven — pred vsakim pre-sales sestankom

## PRAVILA
- Loči DEJSTVA (z virom/URL) od SKLEPOV (moja interpretacija) — vedno
  označi, kaj je kaj. Nikoli ne predstavi ugibanja kot dejstvo.
- Fokus na Kore storitve: ali lead rabi WordPress prenovo, Instagram
  management, ali RAG/chatbot? Oceni za vsako od treh.
- Brief mora biti prebavljiv v 5 minutah pred sestankom: max 1 stran,
  na vrhu 3 ključne ugotovitve.
- Rezultat vedno zapiši v vault (ne samo v chat), da se ob podpisu
  klienta preseli v pravi klientski folder.

## POGOSTE NALOGE

| Naloga | Kaj narediti |
|---|---|
| Nov lead brief | Preglej spletno stran, Instagram/FB, Google recenzije → povzemi: kdo so, kaj prodajajo, digitalna prisotnost, šibke točke → zapiši v `vault/clients/<lead>/research.md` |
| Ocena priložnosti | Za vsako Kore storitev (WP / IG / RAG-chatbot) oceni: potreba (1–5), dokaz za oceno, predlog pristopa |
| Priprava na sestanek | Iz research.md izlušči 3 vprašanja za klienta + 1 konkreten "quick win" predlog |
| Konkurenčna slika | 2–3 podobna podjetja v regiji: kaj delajo bolje/slabše na webu in IG |
| Lead postane klient | Preseli research.md v stalni `vault/clients/<klient>/` folder in ustvari `skills/agency/<klient>/SKILL.md` po vzoru [[../../agency/ambulanta-dolinar/SKILL|ambulanta-dolinar]] |

## POVEZAVE (vault)
- `vault/clients/<lead>/research.md` — izhod tega skilla
- `skills/agency/ambulanta-dolinar/SKILL.md` — vzorec, ko lead postane klient
- `vault/reference/rag-stack-supabase-n8n.md` — [[rag-stack-supabase-n8n]], kaj Kore ponudi pri chatbot leadu

## TODO / NASLEDNJI KORAKI
- [ ] Definirati standardno predlogo research.md (da so briefi primerljivi med leadi)
- [ ] Dodati checklist za GDPR/omejitve pri scrapanju podatkov o podjetjih
