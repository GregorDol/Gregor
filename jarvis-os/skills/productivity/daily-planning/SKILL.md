---
name: daily-planning
branch: productivity
description: >
  Jutranji planning ritual za Kore agencijo. Sproži se ob: "dobro jutro",
  "plan dneva", "kaj imam danes", "začniva dan", ali ob prvem pogovoru
  dneva, ko še ne obstaja današnji zapisek v vault/daily/. NE uporabljaj
  za planiranje posameznega projekta (to gre v klientski skill v agency/)
  ali za tedenski/mesečni pregled — ta skill pokriva SAMO dnevni ritual.
---

# SKILL: Daily Planning — jutranji ritual

## KONTEKST
- Klient / projekt: interno — Kore agencija (Gregor)
- Deliverable: današnji daily zapisek s prioritiziranim planom dneva
- Stack / orodja: vault/daily/, Obsidian markdown, [[wikilinki]]
- Status: aktiven — teče vsako jutro

## PRAVILA
- Preberi zapiske zadnjih 3 dni iz `vault/daily/` PREDEN predlagaš karkoli —
  plan mora izhajati iz odprtih TODO-jev, ne iz domišljije.
- Nikoli ne izbriši ali prepiši obstoječega daily zapiska — samo dopolnjuj.
- Predlagaj največ 3 prioritete za dan (Kore realnost: WordPress dev,
  Instagram management, RAG/chatbot projekti + pre-sales).
- Nedokončane TODO-je iz prejšnjih dni eksplicitno prenesi naprej ali
  označi kot opuščene — nikoli jih tiho ne izgubi.
- Plan je PREDLOG — Gregor ga potrdi ali premeša; ne izvajaj taskov sam
  od sebe v tem skillu.

## POGOSTE NALOGE

| Naloga | Kaj narediti |
|---|---|
| Jutranji plan | Preberi `vault/daily/` zadnje 3 dni → zberi odprte TODO → predlagaj top 3 prioritete → zapiši v današnji `vault/daily/YYYY-MM-DD.md` |
| Današnji zapisek ne obstaja | Ustvari ga po formatu: `# YYYY-MM-DD`, sekcije `## Danes`, `## Odločitve`, `## Odprto / TODO jutri` |
| Prenos TODO-jev | Odprte alineje iz prejšnjih dni prekopiraj v današnji zapisek pod `## Danes`, z virom npr. `(prenos iz [[2026-07-02]])` |
| Konec dneva / "zaključiva" | Povzemi kaj je bilo narejeno, zapiši odločitve in odprte stvari za jutri |
| Klientski task se pojavi v planu | Poveži z ustreznim skillom: [[../../agency/ambulanta-dolinar/SKILL|ambulanta-dolinar]] ali [[../../agency/mera-care/SKILL|mera-care]] |

## POVEZAVE (vault)
- `vault/daily/` — dnevni zapiski (vir in cilj tega skilla)
- `vault/reference/jarvis-os-arhitektura.md` — [[jarvis-os-arhitektura]], kako sistem deluje
- `skills/memory/vault-sync/SKILL.md` — pravila KAM se kaj zapiše

## TODO / NASLEDNJI KORAKI
- [ ] Dodati tedenski pregled (petek popoldne) kot ločen skill ali razširitev
- [ ] Povezati z voice pipeline: "dobro jutro" prek mikrofona sproži ta ritual
