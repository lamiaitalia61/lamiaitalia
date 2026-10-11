---
title: "Proposte — Democrazia diretta"
tags:
  - l-italia-che-vorrei
  - proposte
  - democrazia-diretta
status: "GENERATO"
generato: "2026-10-11"
sorgente: "dati/proposte.json"
---

# Proposte — Democrazia diretta

> [!warning] File generato
> Prodotto da `strumenti/genera.py` da `dati/proposte.json`. Non modificare a mano: le modifiche vanno fatte sul dataset e rigenerate.

6 proposte nell'ambito `democrazia-diretta`. Ogni scheda riporta problema, leva, evidenza, oppositori, KPI, fase e vincolo giuridico.
Il formato editoriale di riferimento resta [la scheda proposta](../00_SCHEDA_PROPOSTA.md): le voci qui assenti (costi dettagliati, effetti distributivi, compatibilita' UE) sono lavoro ancora da fare, non voci omesse.

### P-DEMDIR-04 — Obbligo di linguaggio piano + libretto informativo a ogni elettore con testo, effetti e argomenti pro/contro verificati da organismo terzo

- **Problema**: Quesiti incomprensibili e informazione di parte
- **Leva (meccanismo di incentivo)**: Obbligo di linguaggio piano + libretto informativo a ogni elettore con testo, effetti e argomenti pro/contro verificati da organismo terzo
- **Benchmark**: Svizzera (libretto di voto), Oregon (Citizens' Initiative Review)
- **Fase**: 1 — capacita' (1-3 anni)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: basso
- **KPI**: Indice di leggibilita' (Gulpease) dei quesiti referendari superiore a 70 punti; 100% elettori con libretto
- **Chi si oppone**: Comitati che traggono vantaggio dalla confusione
- **Rischio / obiezione piu' forte**: La redazione del libretto informativo neutrale puo' diventare essa stessa terreno di feroce scontro politico sulla scelta degli esperti e delle argomentazioni.
- **Evidenza**:
    - `F-REF-06` Referendum costituzionale 2026: 22-23 mar. 2026, separazione delle carriere e riassetto CSM: prevale il No, riforma non entrata in vigore; per circa il 31% degli elettori del No fu un voto contro il governo (Ministero dell'Interno; YouTrend, 2026)
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-DEMDIR-03 — Election day referendario fisso per legge, una data annuale prestabilita

- **Problema**: La data del voto viene usata come arma contro i promotori
- **Leva (meccanismo di incentivo)**: Election day referendario fisso per legge, una data annuale prestabilita
- **Benchmark**: Svizzera (4 date/anno fissate in anticipo)
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: nullo (risparmio)
- **KPI**: Costo per consultazione referendaria ridotto di oltre il 60% grazie all'accorpamento in data fissa annuale
- **Chi si oppone**: Governo di turno
- **Rischio / obiezione piu' forte**: Fissare una data annuale unica (election day) rischia di ammassare troppi quesiti eterogenei nella stessa tornata, disorientando gli elettori.
- **Evidenza**:
    - `F-REF-05` Scelta della data: nel 2025 il voto fu fissato in coincidenza con i ballottaggi, contro la richiesta dei promotori (Cronaca; Wikipedia referendum 2025, 2025)
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-DEMDIR-05 — Giuria di cittadini estratti a sorte che audisce esperti e pubblica un documento sintetico neutrale prima del voto

- **Problema**: Temi divisivi decisi senza fase deliberativa
- **Leva (meccanismo di incentivo)**: Giuria di cittadini estratti a sorte che audisce esperti e pubblica un documento sintetico neutrale prima del voto
- **Benchmark**: Irlanda (Citizens' Assembly)
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: basso
- **KPI**: Sperimentazione di almeno 3 giurie civiche per consultazioni su temi complessi entro il primo triennio
- **Chi si oppone**: Chi teme la delega a organismi non eletti
- **Rischio / obiezione piu' forte**: La giuria di cittadini estratti a sorte puo' essere manipolata nella selezione degli esperti o subire polarizzazione di gruppo.
- **Evidenza**:
    - `F-REF-03` Affluenza e polarizzazione: correlazione 0,77 tra affluenza regionale ai referendum 2025 e voto ai partiti di sinistra alle europee 2024 (Studi Elettorali, 2025)
- **Origine del record**: claude · confidenza media · stato `proposta`

### P-DEMDIR-06 — Tetti di spesa e trasparenza totale sui finanziamenti delle campagne referendarie

- **Problema**: Con la firma digitale il costo di promozione crolla: rischio di cattura da parte di chi paga
- **Leva (meccanismo di incentivo)**: Tetti di spesa e trasparenza totale sui finanziamenti delle campagne referendarie
- **Benchmark**: California come contro-esempio
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: basso
- **KPI**: Tetto massimo di spesa per comitato promotore rispettato dal 100% dei comitati con bilanci certificati
- **Chi si oppone**: Promotori ben finanziati
- **Rischio / obiezione piu' forte**: Tetti di spesa troppo bassi possono penalizzare i comitati civici spontanei rispetto a movimenti sostenuti da grandi organizzazioni o media.
- **Evidenza**:
    - `F-REF-07` Firma digitale: dal 2021 firma digitale con piattaforma pubblica: costo di raccolta crollato (d.l. 77/2021 e successive, 2021)
- **Nota**: Precondizione, non conseguenza: senza tetti di spesa e trasparenza il referendum propositivo (P-DEMDIR-02) diventa lo strumento di chi puo' pagarne la promozione.
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-DEMDIR-01 — Sostituzione con quorum di approvazione (Si' sopra il 25-33% dell'elettorato), indipendente dall'affluenza

- **Problema**: Il quorum di partecipazione trasforma l'astensione in arma di voto; quorum raggiunto 2 volte su 10 in trent'anni
- **Leva (meccanismo di incentivo)**: Sostituzione con quorum di approvazione (Si' sopra il 25-33% dell'elettorato), indipendente dall'affluenza
- **Benchmark**: Ordinamenti con quorum di approvazione
- **Fase**: 3 — struttura (4-8 anni)
- **Vincolo giuridico**: legge costituzionale (art. 75)
- **Costo**: nullo
- **KPI**: Partecipazione referendaria con voto favorevole di almeno il 25% degli aventi diritto per l'approvazione
- **Chi si oppone**: Chi usa l'astensione come strategia difensiva
- **Rischio / obiezione piu' forte**: Un quorum di approvazione troppo basso rischia di consentire a minoranze agguerrite e organizzate di approvare norme respinte dalla maggioranza silenziosa.
- **Evidenza**:
    - `F-REF-01` Quorum raggiunto: negli ultimi 30 anni, su 10 referendum non costituzionali il quorum e' stato raggiunto 2 volte (Ipsos / Corriere della Sera, 2025)
    - `F-REF-02` Referendum 8-9 giugno 2025: affluenza 30,58%; quorum mancato; Si' all'88-89% sui quesiti lavoro e 65% su cittadinanza (Ministero dell'Interno; Pagella Politica, 2025)
    - `F-REF-03` Affluenza e polarizzazione: correlazione 0,77 tra affluenza regionale ai referendum 2025 e voto ai partiti di sinistra alle europee 2024 (Studi Elettorali, 2025)
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-DEMDIR-02 — Referendum propositivo: firme rafforzate, termine al Parlamento, controllo preventivo di costituzionalita' e obbligo di copertura

- **Problema**: Il popolo puo' solo abrogare, mai proporre
- **Leva (meccanismo di incentivo)**: Referendum propositivo: firme rafforzate, termine al Parlamento, controllo preventivo di costituzionalita' e obbligo di copertura
- **Benchmark**: Svizzera (iniziativa popolare); California come contro-esempio
- **Fase**: 3 — struttura (4-8 anni)
- **Vincolo giuridico**: legge costituzionale
- **Costo**: basso
- **KPI**: 100% delle proposte di legge d'iniziativa popolare con 50.000 firme calendarizzate ed esaminate entro 6 mesi
- **Chi si oppone**: Parlamento; chi teme la cattura da parte di chi finanzia
- **Prerequisiti bloccanti**: P-DEMDIR-06
- **Rischio / obiezione piu' forte**: Senza controllo preventivo e vincolo di copertura si replica il dissesto californiano
- **Evidenza**:
    - `F-REF-04` Tipologia referendum: art. 75: solo abrogativo, 500k firme o 5 consigli regionali, escluse materie tributarie, di bilancio, amnistia e trattati; art. 138: costituzionale senza quorum (Costituzione italiana, 2026)
- **Nota**: Non attivabile prima di P-DEMDIR-06 (tetti di spesa e trasparenza sulle campagne): e' la lezione californiana citata nell'analisi.
- **Origine del record**: claude · confidenza media · stato `proposta`
