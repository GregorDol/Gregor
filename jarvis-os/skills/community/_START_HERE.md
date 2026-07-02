Ta mapa je še prazna.

Ko boš pripravljen dodati prvi skill v "community" branch:
1. Skopiraj /jarvis-os/SKILL_TEMPLATE.md v community/ime-skilla/SKILL.md
2. Izpolni trigger (description), kontekst, pravila, pogoste naloge
3. Izbriši to datoteko, ko community/ ni več prazna

Ideja za "community": community management, odgovarjanje na komentarje/DM-je za kliente

## 3 konkretne ideje za skille

1. **comment-responder** — odgovarjanje na Instagram komentarje/DM-je po
   klientovem glasu: prebere `vault/clients/<klient>/instagram.md` profil,
   pripravi osnutke odgovorov (nikoli ne objavlja sam), eskalira občutljive
   primere (pritožbe, zdravstvena vprašanja) Gregorju.
2. **review-manager** — Google/FB recenzije za kliente: osnutki odgovorov
   na pozitivne in negativne recenzije, mesečni povzetek sentimenta v
   `vault/reports/`, opozorilo pri recenziji pod 3 zvezdicami.
3. **faq-harvester** — iz komentarjev, DM-jev in chatbot logov izlušči
   ponavljajoča se vprašanja in jih predlaga za vnos v klientovo knowledge
   base (npr. [[dolinar/knowledge-base]]) — most med community in RAG projekti.
