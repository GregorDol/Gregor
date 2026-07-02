---
name: ambulanta-dolinar
branch: agency
description: >
  Uporabi ta skill za VSE naloge povezane z Ambulanta Dolinar projektom -
  WordPress AI chatbot za ortopedsko ambulanto prof. dr. Draga Dolinarja.
  Sproži se ob: vprašanjih o chatbot arhitekturi, popravkih/nadgradnjah
  chatbota, RAG/knowledge base posodobitvah, klientskih poročilih,
  Anthropic/Gemini API integraciji, ali kakršnikoli komunikaciji s klientom
  Dolinar. NE uporabljaj za druge WordPress projekte (Méra Care ima svoj
  skill) ali splošna Kore vprašanja.
---

# SKILL: Ambulanta Dolinar — AI Chatbot

## KONTEKST PROJEKTA
- Klient: Prof. dr. Drago Dolinar, ortopedska ambulanta
- Deliverable: WordPress AI chatbot za odgovarjanje na vprašanja pacientov
- Stack: Anthropic API (Claude) + Gemini API, four-layer arhitektura
- Status: Referenčni primer za Kore — uporabi kot template za druge medicinske/SMB kliente

## ARHITEKTURA (4 sloji)
1. Vhodni sloj — WordPress widget/vmesnik, sprejme uporabnikovo vprašanje
2. Routing sloj — odloči, ali gre za enostavno (FAQ/regex) ali kompleksno vprašanje, ki rabi LLM
3. Knowledge/RAG sloj — poišče relevantne informacije iz baze znanja (ordinacijski čas, storitve, postopki, kontakt…)
4. Generacijski sloj — Claude/Gemini sestavi odgovor v naravnem jeziku, v slovenščini, s primernim medicinskim tonom (previdno, brez diagnoz)

## KLJUČNA PRAVILA
- Chatbot NIKOLI ne daje medicinskih diagnoz ali nasvetov o zdravljenju — samo informacije o ambulanti, terminih, splošnih postopkih
- Pri negotovosti chatbot preusmeri na klic/email ambulante
- Ves tekst v slovenščini, formalen nagovor (vikanje), primeren za starejšo/mešano populacijo pacientov
- Odgovori naj bodo kratki in jasni — pacienti niso tehnično podkovani

## POGOSTE NALOGE V TEM SKILLU

| Naloga | Kaj narediti |
|---|---|
| Dodaj novo FAQ | Posodobi knowledge base, testiraj routing |
| Popravi ton odgovora | Prilagodi system prompt v generacijskem sloju |
| Nov API endpoint | Preveri kompatibilnost Anthropic/Gemini slojev |
| Klientsko poročilo | Povzemi uporabo, pogosta vprašanja, predlogi izboljšav |
| Bug v chatbotu | Preveri routing sloj najprej (najpogostejši vzrok napak) |

## POVEZAVE (vault)
- `vault/clients/dolinar/arhitektura.md` — polna tehnična dokumentacija
- `vault/clients/dolinar/knowledge-base.md` — vsa vsebina za RAG
- `vault/clients/dolinar/porocila/` — mesečna poročila klientu
- `vault/reference/rag-stack-supabase-n8n.md` — splošna RAG arhitektura, ki se ponovno uporabi za druge kliente

## NASLEDNJI KORAKI / TODO
- Prenesti arhitekturo na Supabase + n8n stack (trenutno v razvoju)
- Pripraviti reskin verzijo za naslednjega medicinskega klienta
- Dodati analytics sloj (koliko vprašanj, katera najpogostejša)

## OPOMBE
Ta skill služi kot referenčni template — ko boš delal SKILL.md za naslednjega
klienta (npr. zobozdravstvo, avto servis), kopiraj to strukturo in prilagodi
kontekst, pravila in pogoste naloge.
