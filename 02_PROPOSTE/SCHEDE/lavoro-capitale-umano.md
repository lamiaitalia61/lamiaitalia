---
title: "Proposte — Lavoro e capitale umano"
tags:
  - l-italia-che-vorrei
  - proposte
  - lavoro-capitale-umano
status: "GENERATO"
generato: "2026-10-11"
sorgente: "dati/proposte.json"
---

# Proposte — Lavoro e capitale umano

> [!warning] File generato
> Prodotto da `strumenti/genera.py` da `dati/proposte.json`. Non modificare a mano: le modifiche vanno fatte sul dataset e rigenerate.

6 proposte nell'ambito `lavoro-capitale-umano`. Ogni scheda riporta problema, leva, evidenza, oppositori, KPI, fase e vincolo giuridico.
Il formato editoriale di riferimento resta [la scheda proposta](../00_SCHEDA_PROPOSTA.md): le voci qui assenti (costi dettagliati, effetti distributivi, compatibilita' UE) sono lavoro ancora da fare, non voci omesse.

### P-LAV-01 — Sistema duale su scala tedesca: ITS a 200.000 studenti, imprese coinvolte per obbligo o contributo

- **Problema**: Transizione scuola-lavoro tra le peggiori d'Europa
- **Leva (meccanismo di incentivo)**: Sistema duale su scala tedesca: ITS a 200.000 studenti, imprese coinvolte per obbligo o contributo
- **Benchmark**: Germania, Svizzera
- **Fase**: 1 — capacita' (1-3 anni)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: alto
- **KPI**: Occupati entro 3 anni dal titolo dal 67,6% all'80%
- **Chi si oppone**: Parte del mondo scolastico (rischio subordinazione all'impresa)
- **Evidenza**:
    - `F-LAV-01` NEET 15-29 e abbandono scolastico: NEET 13,3% (era 25,7% dieci anni fa); abbandono 8,2%, sotto media UE 9,1% (Istat, 2025)
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-LAV-03 — Presa in carico entro 30 giorni, budget formativo trasferibile alla persona, valutazione sui tassi di ricollocazione

- **Problema**: Centri per l'impiego inefficaci: precondizione mancante di ogni riforma del lavoro
- **Leva (meccanismo di incentivo)**: Presa in carico entro 30 giorni, budget formativo trasferibile alla persona, valutazione sui tassi di ricollocazione
- **Benchmark**: Danimarca, Germania (Bundesagentur)
- **Fase**: 1 — capacita' (1-3 anni)
- **Vincolo giuridico**: legge ordinaria + intesa Stato-Regioni
- **Costo**: alto
- **KPI**: Tasso di ricollocazione a 6 mesi
- **Chi si oppone**: Regioni titolari delle politiche attive
- **Evidenza**:
    - `F-LAV-01` NEET 15-29 e abbandono scolastico: NEET 13,3% (era 25,7% dieci anni fa); abbandono 8,2%, sotto media UE 9,1% (Istat, 2025)
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-LAV-06-GEM — Collegare i percorsi di riqualificazione alla NASpI con offerta formativa verificata e tutoraggio; applicare eventuale condizionalita solo dopo una offerta effettivamente accessibile e congrua

- **Problema**: La transizione dalla disoccupazione al lavoro richiede servizi formativi efficaci e accessibili
- **Leva (meccanismo di incentivo)**: Collegare i percorsi di riqualificazione alla NASpI con offerta formativa verificata e tutoraggio; applicare eventuale condizionalita solo dopo una offerta effettivamente accessibile e congrua
- **Benchmark**: Danimarca (Flexicurity e politiche attive vincolanti)
- **Fase**: 1 — capacita' (1-3 anni)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: medio
- **KPI**: Ricollocazione a 6 e 12 mesi per partecipanti comparabili; baseline e target da definire
- **Chi si oppone**: Percettori di sussidi passivi privi di controlli ed enti di formazione fittizi
- **Gate di attivazione**: Disponibilita territoriale dei corsi, accomodamenti per disabilita e cura, ricorso contro le sanzioni e valutazione degli effetti
- **Evidenza**:
    - `F-ECO-03` Salari reali medi: nel 2024 sotto il livello 1990 (-1,6%); media OCSE +35% (UPB su dati OCSE, 2024)
    - `F-LAV-01` NEET 15-29 e abbandono scolastico: NEET 13,3% (era 25,7% dieci anni fa); abbandono 8,2%, sotto media UE 9,1% (Istat, 2025)
- **Nota**: Coordinare con P-LAV-03; costi di formazione e servizi da stimare, rischio di sanzionare chi non riceve una offerta utile.
- **Origine del record**: gemini · confidenza bassa · stato `proposta`

### P-LAV-02 — Contratto unico a tutele crescenti con costo di uscita crescente e prevedibile

- **Problema**: Dualismo insider/outsider e giungla dei contratti a termine
- **Leva (meccanismo di incentivo)**: Contratto unico a tutele crescenti con costo di uscita crescente e prevedibile
- **Benchmark**: Danimarca (flexicurity)
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: legge delega
- **Costo**: medio
- **KPI**: Quota contratti a termine non stagionali scesa sotto il 12%; durata media aumentata di oltre 6 mesi
- **Chi si oppone**: Sindacati (perdita tutele insider)
- **Gate di attivazione**: Attivabile solo dopo verifica dei tassi di ricollocazione dei CPI
- **Prerequisiti bloccanti**: P-LAV-03
- **Evidenza**:
    - `F-ECO-03` Salari reali medi: nel 2024 sotto il livello 1990 (-1,6%); media OCSE +35% (UPB su dati OCSE, 2024)
- **Origine del record**: claude · confidenza media · stato `proposta`

### P-LAV-04 — Soglia minima agganciata ai CCNL piu' rappresentativi + detassazione premi di produttivita'

- **Problema**: Dumping contrattuale e salari reali sotto il livello 1990
- **Leva (meccanismo di incentivo)**: Soglia minima agganciata ai CCNL piu' rappresentativi + detassazione premi di produttivita'
- **Benchmark**: Germania (Mindestlohn), modelli nordici
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: medio
- **KPI**: Salario reale mediano in aumento di almeno l'1,5% annuo; lavoratori sotto soglia poverta' <5%
- **Chi si oppone**: Chi teme effetti occupazionali; parte del sindacato teme svuotamento della contrattazione
- **Rischio / obiezione piu' forte**: Tema contestato: esiste letteratura discorde sugli effetti occupazionali
- **Evidenza**:
    - `F-ECO-03` Salari reali medi: nel 2024 sotto il livello 1990 (-1,6%); media OCSE +35% (UPB su dati OCSE, 2024)
- **Origine del record**: claude · confidenza media · stato `proposta`

### P-LAV-05 — Leve non fiscali: carriere per merito, laboratori finanziati, casa accessibile nelle citta' universitarie

- **Problema**: Saldo laureati 25-34 negativo; sgravi fiscali per i rientri poco efficaci
- **Leva (meccanismo di incentivo)**: Leve non fiscali: carriere per merito, laboratori finanziati, casa accessibile nelle citta' universitarie
- **Benchmark**: Germania, Paesi Bassi (attrattivita' ricerca)
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: alto
- **KPI**: Saldo migratorio laureati in pareggio in 10 anni
- **Chi si oppone**: Sistema accademico a reclutamento locale
- **Evidenza**:
    - `F-DEMO-04` Saldo laureati 25-34: -21.000 in un anno (25k espatri, 4k rientri) (Istat, report giovani e migrazioni mag. 2026, 2026)
    - `F-DEMO-05` Occupati entro 3 anni dal titolo: 67,6% (Eurozona 81%, Germania >90%) (CSC su Istat/Eurostat, 2026)
- **Origine del record**: claude · confidenza media · stato `proposta`
