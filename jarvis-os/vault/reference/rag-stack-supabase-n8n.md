# RAG Stack — Supabase + n8n (splošna arhitektura)

Status: skelet — dopolni z detajli iz obstoječega dela na [[dolinar/arhitektura]]

## Namen
Ponovno uporabna RAG arhitektura za vse Kore kliente, ki rabijo AI chatbot
ali knowledge-base search. Prvi implementiran primer: [[dolinar/arhitektura]].

## Sloji
1. Vhod — widget/API endpoint sprejme vprašanje
2. Routing — FAQ/regex vs. LLM
3. Retrieval — Supabase (pgvector) hrani embeddinge knowledge base
4. Generacija — Claude/Gemini sestavi odgovor

## n8n vloga
- Orkestrira ingestion pipeline (dokument → chunk → embed → Supabase)
- Sproža avtomatska poročila (glej [[reports]])

## TODO
- [ ] Prenesti dolinar chatbot na ta stack (trenutno v razvoju, glej skill)
- [ ] Definirati standarden chunking/embedding pristop za vse kliente
- [ ] Reskin checklist za nov klient (kaj se spremeni, kaj ostane isto)

## Povezano
- [[dolinar/arhitektura]]
- [[dolinar/knowledge-base]]
