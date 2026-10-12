---
title: "Proposte — Fisco"
tags:
  - l-italia-che-vorrei
  - proposte
  - fisco
status: "GENERATO"
sorgente: "dati/proposte.json"
---

# Proposte — Fisco

> [!warning] File generato
> Prodotto da `strumenti/genera.py` da `dati/proposte.json`. Non modificare a mano: le modifiche vanno fatte sul dataset e rigenerate.

7 proposte nell'ambito `fisco`. Ogni scheda riporta problema, leva, evidenza, oppositori, KPI, fase e vincolo giuridico.
Il formato editoriale di riferimento resta [la scheda proposta](../00_SCHEDA_PROPOSTA.md): le voci qui assenti (costi dettagliati, effetti distributivi, compatibilita' UE) sono lavoro ancora da fare, non voci omesse.

### P-FISC-06 — Divieto di condono per legge rinforzata per un decennio

- **Problema**: I condoni ricorrenti distruggono la tax morale
- **Leva (meccanismo di incentivo)**: Divieto di condono per legge rinforzata per un decennio
- **Fase**: 0 — credibilita' (primi 12 mesi)
- **Vincolo giuridico**: legge ordinaria (non vincola il legislatore futuro: limite noto)
- **Costo**: nullo
- **KPI**: Zero condoni per 5 anni e propensione all'adempimento spontaneo aumentata di almeno 5 punti
- **Chi si oppone**: Chi usa il condono come valvola politica
- **Rischio / obiezione piu' forte**: Nessuna legge ordinaria puo' vincolare la successiva
- **Evidenza**:
    - `F-PSICO-01` Tax morale condizionata: La tax morale e la compliance spontanea sono correlate positivamente alla percezione che anche gli altri contribuenti paghino (equita' orizzontale) e che le risorse siano impiegate in servizi pubblici visibili (OECD, 'Tax Morale II: Building Trust between Tax Administrations and Large Businesses and Individuals'; Banca d'Italia, QEF n. 531, 2023) **[NON VERIFICATO — vietato in pubblicazione]**
- **Origine del record**: claude · confidenza media · stato `proposta`

### P-FISC-08-GEM — Rafforzare la valutazione periodica indipendente dei programmi di spesa e dei sussidi, con dati pubblici, analisi distributiva e decisione parlamentare su conferma, modifica o chiusura

- **Problema**: Programmi di spesa e sussidi possono continuare senza una valutazione comparabile degli effetti
- **Leva (meccanismo di incentivo)**: Rafforzare la valutazione periodica indipendente dei programmi di spesa e dei sussidi, con dati pubblici, analisi distributiva e decisione parlamentare su conferma, modifica o chiusura
- **Benchmark**: Paesi Bassi / Canada (Program Review con criteri stringenti di addizionalita')
- **Fase**: 0 — credibilita' (primi 12 mesi)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: medio
- **KPI**: Quota dei programmi valutati con dati pubblici e decisione motivata; baseline e target da definire
- **Chi si oppone**: Imprese e settori sussidiati senza obbligo di rendicontazione o innovazione
- **Gate di attivazione**: Mandato e risorse per valutatori indipendenti; confronto con Ragioneria, UPB e Parlamento senza attribuire all UPB poteri decisionali automatici
- **Evidenza**:
    - `F-ECO-01` Debito pubblico / PIL: ~138,6% previsto 2026 (sopra la Grecia) (DFP 2026; FMI Fiscal Monitor apr. 2026, 2026)
    - `F-ECO-02` Debito nominale: oltre 3.200 mld EUR (giu. 2026) (Banca d'Italia, 2026)
- **Nota**: Nessun risparmio di 8 miliardi e dimostrato. Stimare per singola misura effetti fiscali, ambientali, sociali e costi di transizione.
- **Origine del record**: gemini · confidenza bassa · stato `proposta`

### P-FISC-05 — Compliance by design: precompilazione totale, incroci in tempo reale, algoritmi di rischio pubblicati

- **Problema**: Tax gap ~100 mld/anno; 60% sul reddito da lavoro autonomo
- **Leva (meccanismo di incentivo)**: Compliance by design: precompilazione totale, incroci in tempo reale, algoritmi di rischio pubblicati
- **Benchmark**: Estonia, Danimarca
- **Fase**: 1 — capacita' (1-3 anni)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: medio
- **KPI**: Tax gap < 60 mld in 8 anni
- **Chi si oppone**: Categorie a alta evasione; garantisti sulla privacy fiscale
- **Evidenza**:
    - `F-FISC-01` Tax gap: ~100 mld EUR/anno; propensione all'evasione 17% (MEF, Relazione su economia non osservata ed evasione, 2025)
    - `F-FISC-02` Tax gap lavoro autonomo: ~60% del reddito (Commissione UE / UPB, 2025)
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-FISC-01 — Riduzione strutturale del cuneo, finanziata non a debito

- **Problema**: Cuneo fiscale alto su redditi da lavoro medio-bassi
- **Leva (meccanismo di incentivo)**: Riduzione strutturale del cuneo, finanziata non a debito
- **Benchmark**: Media OCSE
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: legge di bilancio
- **Costo**: alto
- **KPI**: Cuneo fiscale medio sceso sotto il 40% (allineato alla media OCSE) entro il 2028
- **Chi si oppone**: Chi perde agevolazioni usate come copertura
- **Prerequisiti bloccanti**: P-FISC-02, P-FISC-03, P-FISC-05
- **Evidenza**:
    - `F-ECO-03` Salari reali medi: nel 2024 sotto il livello 1990 (-1,6%); media OCSE +35% (UPB su dati OCSE, 2024)
    - `F-FISC-01` Tax gap: ~100 mld EUR/anno; propensione all'evasione 17% (MEF, Relazione su economia non osservata ed evasione, 2025)
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-FISC-02 — Revisione sistematica con soppressione automatica delle inefficaci

- **Problema**: Circa 600 tax expenditures mai valutate
- **Leva (meccanismo di incentivo)**: Revisione sistematica con soppressione automatica delle inefficaci
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: legge delega
- **Costo**: nullo (genera gettito)
- **KPI**: Almeno 50 micro-agevolazioni soppresse e 8 miliardi di euro di gettito recuperati entro 24 mesi
- **Chi si oppone**: Ogni categoria beneficiaria
- **Evidenza**:
    - `F-FISC-03` Spese fiscali censite nel Rapporto MEF 2023: 625 misure censite nel Rapporto 2023; 555 ancora vigenti nel 2024; effetti finanziari stimati per 411 misure quantificabili pari a circa 96,3 miliardi di euro nel 2024 (MEF, Rapporto annuale sulle spese fiscali 2023, p. 15, https://www.mef.gov.it/export/sites/MEF/documenti-allegati/2023/Rapporto-spese-fiscali-2023.pdf, 2024)
    - `F-FISC-01` Tax gap: ~100 mld EUR/anno; propensione all'evasione 17% (MEF, Relazione su economia non osservata ed evasione, 2025)
    - `F-ECO-03` Salari reali medi: nel 2024 sotto il livello 1990 (-1,6%); media OCSE +35% (UPB su dati OCSE, 2024)
- **Nota**: Contributo Gemini integrato da P-FISC-07-GEM; soglie, costi e compatibilita da valutare prima dell approvazione.
- **Origine del record**: claude; gemini (contributo integrato) · confidenza media · stato `proposta`

### P-FISC-03 — Riordino catastale a invarianza di gettito, contestuale al taglio del cuneo

- **Problema**: Rendite catastali scollegate dai valori reali; tassazione sul lavoro anziche' sullo stock
- **Leva (meccanismo di incentivo)**: Riordino catastale a invarianza di gettito, contestuale al taglio del cuneo
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: legge delega
- **Costo**: nullo (neutro)
- **KPI**: Scostamento medio tra valori catastali e valori OMI ridotto sotto il 15% a parita' di gettito
- **Chi si oppone**: Proprietari immobiliari, ceto medio anziano
- **Rischio / obiezione piu' forte**: Politicamente il punto piu' esplosivo del piano
- **Evidenza**:
    - `F-PARAD-01` Ricchezza privata vs debito pubblico: ricchezza netta delle famiglie tra le piu' alte d'Europa in rapporto al reddito, a fronte di debito pubblico tra i piu' alti al mondo (Banca d'Italia, Relazione annuale, 2026)
- **Origine del record**: claude · confidenza media · stato `proposta`

### P-FISC-04 — Sostituzione degli scalini con transizione continua degli oneri

- **Problema**: Soglie dimensionali fiscali e lavoristiche che disincentivano la crescita
- **Leva (meccanismo di incentivo)**: Sostituzione degli scalini con transizione continua degli oneri
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: medio
- **KPI**: Quota imprese >50 addetti +30%
- **Chi si oppone**: Nessun oppositore organizzato; ostacolo tecnico
- **Evidenza**:
    - `F-PARAD-02` Nanismo d'impresa: soglie dimensionali fiscali e lavoristiche a 5/15/50 addetti disincentivano la crescita (OCSE; Banca d'Italia, 2026)
- **Origine del record**: claude · confidenza alta · stato `proposta`
