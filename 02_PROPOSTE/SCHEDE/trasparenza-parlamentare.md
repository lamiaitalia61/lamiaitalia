---
title: "Proposte — Trasparenza parlamentare"
tags:
  - l-italia-che-vorrei
  - proposte
  - trasparenza-parlamentare
status: "GENERATO"
generato: "2026-10-11"
sorgente: "dati/proposte.json"
---

# Proposte — Trasparenza parlamentare

> [!warning] File generato
> Prodotto da `strumenti/genera.py` da `dati/proposte.json`. Non modificare a mano: le modifiche vanno fatte sul dataset e rigenerate.

6 proposte nell'ambito `trasparenza-parlamentare`. Ogni scheda riporta problema, leva, evidenza, oppositori, KPI, fase e vincolo giuridico.
Il formato editoriale di riferimento resta [la scheda proposta](../00_SCHEDA_PROPOSTA.md): le voci qui assenti (costi dettagliati, effetti distributivi, compatibilita' UE) sono lavoro ancora da fare, non voci omesse.

### P-TRASP-04 — Obbligo di legge: ogni voto, presenza, emendamento e incarico in formato aperto con API pubblica istituzionale

- **Problema**: I dati parlamentari aperti li produce una fondazione privata
- **Leva (meccanismo di incentivo)**: Obbligo di legge: ogni voto, presenza, emendamento e incarico in formato aperto con API pubblica istituzionale
- **Benchmark**: UK, USA (govtrack, istituzionalizzati)
- **Fase**: 0 — credibilita' (primi 12 mesi)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: basso
- **KPI**: Uptime delle API degli atti parlamentari al 99,9% con latenza di aggiornamento inferiore a 10 minuti
- **Chi si oppone**: -
- **Evidenza**:
    - `F-ACC-02` Composizione del Parlamento: laureati ~70% (in linea con Germania, Francia, Spagna); eta' media 51,5 anni e in aumento; under 40 al 10,7% degli eletti contro ~23% della popolazione; nessun under 30; permanenza media oltre due legislature (Openpolis; Il Sole 24 Ore; ricerca Bocconi, 2022)
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-TRASP-01 — Divieto di emendamenti sostitutivi dell'intero articolato; tempi minimi tra deposito e voto

- **Problema**: Maxiemendamento e fiducia: un solo voto su centinaia di commi, responsabilita' individuale non tracciabile
- **Leva (meccanismo di incentivo)**: Divieto di emendamenti sostitutivi dell'intero articolato; tempi minimi tra deposito e voto
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: regolamenti parlamentari
- **Costo**: nullo
- **KPI**: Numero di maxiemendamenti governativi ridotto a zero; 100% commi di spesa votati singolarmente entro il 2026
- **Chi si oppone**: Governo di turno
- **Evidenza**:
    - `F-IST-02` Decretazione d'urgenza: uso sistematico di decreti-legge, maxiemendamenti e voti di fiducia; requisito di omogeneita' (art. 15 l. 400/1988) disatteso (Servizi studi parlamentari; Openpolis, 2026)
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-TRASP-02 — Stralcio automatico delle disposizioni estranee, con rilievo formale in sede di emanazione

- **Problema**: Decreti omnibus: obbligo di omogeneita' gia' vigente e sistematicamente ignorato
- **Leva (meccanismo di incentivo)**: Stralcio automatico delle disposizioni estranee, con rilievo formale in sede di emanazione
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: legge ordinaria (art. 15 l. 400/1988 da rendere cogente)
- **Costo**: nullo
- **KPI**: Materie per singolo decreto ridotte a una sola; 100% disposizioni eterogenee espunte dalla presidenza
- **Chi si oppone**: Governo di turno
- **Rafforzata da (non bloccante)**: P-QUIR-01
- **Evidenza**:
    - `F-IST-02` Decretazione d'urgenza: uso sistematico di decreti-legge, maxiemendamenti e voti di fiducia; requisito di omogeneita' (art. 15 l. 400/1988) disatteso (Servizi studi parlamentari; Openpolis, 2026)
- **Nota**: Lo stralcio automatico e' ottenibile rendendo cogente l'art. 15 l. 400/1988 con legge ordinaria. Il rilievo formale del Presidente in sede di emanazione (P-QUIR-01) lo rende piu' efficace ma non e' prerequisito.
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-TRASP-03 — Limitazione ai casi su persone e diritti della persona; tracciatura di tutto il resto

- **Problema**: Voto segreto usato oltre i casi di coscienza
- **Leva (meccanismo di incentivo)**: Limitazione ai casi su persone e diritti della persona; tracciatura di tutto il resto
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: regolamenti parlamentari
- **Costo**: nullo
- **KPI**: Quota votazioni a scrutinio segreto ridotta a meno del 2% delle deliberazioni complessive dell'aula
- **Chi si oppone**: Gruppi parlamentari
- **Evidenza**:
    - `F-IST-02` Decretazione d'urgenza: uso sistematico di decreti-legge, maxiemendamenti e voti di fiducia; requisito di omogeneita' (art. 15 l. 400/1988) disatteso (Servizi studi parlamentari; Openpolis, 2026)
- **Origine del record**: claude · confidenza media · stato `proposta`

### P-TRASP-06 — Quote garantite di calendario per l'iniziativa parlamentare e per l'opposizione, con obbligo di voto finale

- **Problema**: Circa il 75% delle leggi e' di iniziativa governativa: il Parlamento ratifica piu' di quanto legiferi
- **Leva (meccanismo di incentivo)**: Quote garantite di calendario per l'iniziativa parlamentare e per l'opposizione, con obbligo di voto finale
- **Benchmark**: UK (opposition days)
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: regolamenti parlamentari
- **Costo**: nullo
- **KPI**: Quota leggi ordinarie di iniziativa parlamentare aumentata ad almeno il 35% del totale delle leggi promulgate
- **Chi si oppone**: Governo di turno
- **Evidenza**:
    - `F-IST-06` Iniziativa legislativa: circa 75% delle leggi della legislatura di iniziativa governativa, ~25% parlamentare (Openparlamento (Openpolis), 2026)
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-TRASP-05 — Sindacabilita' dei regolamenti parlamentari come ogni altra fonte

- **Problema**: Autodichia: regolamenti parlamentari sottratti al controllo di costituzionalita'
- **Leva (meccanismo di incentivo)**: Sindacabilita' dei regolamenti parlamentari come ogni altra fonte
- **Fase**: 3 — struttura (4-8 anni)
- **Vincolo giuridico**: legge costituzionale
- **Costo**: nullo
- **KPI**: -
- **Chi si oppone**: Camere
- **Evidenza**:
    - `F-POL-01` Autodichia: Camera e Senato deliberano su se stessi in materia di trattamento economico e previdenziale; i ricorsi sono decisi da organi interni (Regolamenti parlamentari; Corte cost. sent. 262/2017, 2026)
- **Origine del record**: claude · confidenza media · stato `proposta`
