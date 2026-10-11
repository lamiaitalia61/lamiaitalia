---
title: "Proposte — Costi della politica"
tags:
  - l-italia-che-vorrei
  - proposte
  - costi-politica
status: "GENERATO"
generato: "2026-10-11"
sorgente: "dati/proposte.json"
---

# Proposte — Costi della politica

> [!warning] File generato
> Prodotto da `strumenti/genera.py` da `dati/proposte.json`. Non modificare a mano: le modifiche vanno fatte sul dataset e rigenerate.

6 proposte nell'ambito `costi-politica`. Ogni scheda riporta problema, leva, evidenza, oppositori, KPI, fase e vincolo giuridico.
Il formato editoriale di riferimento resta [la scheda proposta](../00_SCHEDA_PROPOSTA.md): le voci qui assenti (costi dettagliati, effetti distributivi, compatibilita' UE) sono lavoro ancora da fare, non voci omesse.

### P-POL-03 — Obbligo di tracciamento per chiunque finanzi attivita' politica sopra soglia bassa; registro unico nazionale in formato aperto e in tempo reale

- **Problema**: Trasparenza limitata ai partiti: fondazioni e comitati restano fuori
- **Leva (meccanismo di incentivo)**: Obbligo di tracciamento per chiunque finanzi attivita' politica sopra soglia bassa; registro unico nazionale in formato aperto e in tempo reale
- **Benchmark**: Germania, UK (Electoral Commission)
- **Fase**: 1 — capacita' (1-3 anni)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: basso
- **KPI**: 100% dei contributi ai partiti e fondazioni collegati tracciati online con ritardo massimo di 30 giorni
- **Chi si oppone**: Fondazioni collegate ai leader
- **Evidenza**:
    - `F-POL-04` Finanziamento ai partiti: finanziamento pubblico diretto abolito nel 2013 (uscita entro il 2017), sostituito da 2x1000 e donazioni; obblighi di trasparenza l. 13/2014 che non coprono pienamente fondazioni e comitati (d.l. 149/2013; l. 13/2014, 2017)
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-POL-04 — Registro obbligatorio dei rappresentanti di interessi + agenda pubblica degli incontri dei decisori

- **Problema**: Italia senza una vera legge sul lobbying
- **Leva (meccanismo di incentivo)**: Registro obbligatorio dei rappresentanti di interessi + agenda pubblica degli incontri dei decisori
- **Benchmark**: UE (registro trasparenza), Irlanda, Germania
- **Fase**: 1 — capacita' (1-3 anni)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: basso
- **KPI**: Oltre 95% degli incontri tra decisori pubblici e portatori di interessi registrati sull'agenda pubblica
- **Chi si oppone**: Lobby e decisori
- **Evidenza**:
    - `F-POL-05` Lobbying: assenza di una legge nazionale organica sulla rappresentanza di interessi (Ricognizione comparata (OCSE, GRECO), 2026)
- **Nota**: Contributo Gemini integrato da P-POL-06-GEM; soglie, costi e compatibilita da valutare prima dell approvazione.
- **Origine del record**: claude; gemini (contributo integrato) · confidenza media · stato `proposta`

### P-POL-07-GEM — Definire obblighi proporzionati di dichiarazione, astensione e gestione indipendente delle partecipazioni rilevanti per titolari di cariche esecutive, con vigilanza e sanzioni soggette a ricorso

- **Problema**: I conflitti di interesse nelle cariche esecutive possono compromettere imparzialita e fiducia
- **Leva (meccanismo di incentivo)**: Definire obblighi proporzionati di dichiarazione, astensione e gestione indipendente delle partecipazioni rilevanti per titolari di cariche esecutive, con vigilanza e sanzioni soggette a ricorso
- **Benchmark**: USA (Ethics in Government Act) / Francia (Haute Autorité pour la transparence de la vie publique)
- **Fase**: 1 — capacita' (1-3 anni)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: basso
- **KPI**: Quota di dichiarazioni complete e controllate nei termini, decisioni di astensione pubblicate; baseline e target da definire
- **Chi si oppone**: Grandi proprietari patrimoniali o imprenditori che intendono assumere cariche esecutive senza separare i propri interessi privati
- **Gate di attivazione**: Valutazione costituzionale, tutela dei dati personali e dell impresa; soglie di rilevanza e autorita competente da definire
- **Evidenza**:
    - `F-POL-01` Autodichia: Camera e Senato deliberano su se stessi in materia di trattamento economico e previdenziale; i ricorsi sono decisi da organi interni (Regolamenti parlamentari; Corte cost. sent. 262/2017, 2026)
    - `F-POL-04` Finanziamento ai partiti: finanziamento pubblico diretto abolito nel 2013 (uscita entro il 2017), sostituito da 2x1000 e donazioni; obblighi di trasparenza l. 13/2014 che non coprono pienamente fondazioni e comitati (d.l. 149/2013; l. 13/2014, 2017)
- **Nota**: Blind trust o alienazione solo se il conflitto non puo essere gestito con misure meno intrusive; non pubblicare dati patrimoniali non necessari.
- **Origine del record**: gemini · confidenza media · stato `proposta`

### P-POL-01 — Autorita' indipendente esterna che fissa indennita' di tutte le cariche elettive su parametro oggettivo automatico

- **Problema**: Camere che deliberano su se stesse (autodichia) sui propri trattamenti
- **Leva (meccanismo di incentivo)**: Autorita' indipendente esterna che fissa indennita' di tutte le cariche elettive su parametro oggettivo automatico
- **Benchmark**: UK (IPSA)
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: legge costituzionale (autodichia)
- **Costo**: nullo
- **KPI**: Indennita' parlamentare parametrata rigidamente al trattamento dei magistrati di cassazione entro 6 mesi
- **Chi si oppone**: Camere (perdita di autonomia)
- **Evidenza**:
    - `F-POL-01` Autodichia: Camera e Senato deliberano su se stessi in materia di trattamento economico e previdenziale; i ricorsi sono decisi da organi interni (Regolamenti parlamentari; Corte cost. sent. 262/2017, 2026)
    - `F-POL-02` Indennita' parlamentare: ~10.400 EUR lordi/mese alla Camera (~5.000 netti); con diaria e rimborsi ordine di 13.900-14.600 EUR mensili complessivi (Camera dei deputati; Senato, 2024)
- **Origine del record**: claude · confidenza media · stato `proposta`

### P-POL-02 — Indennita' unica uguale per tutti + rimborsi a pie' di lista documentati e pubblicati + continuita' contributiva per il periodo di mandato

- **Problema**: Vitalizi aboliti nel 2012 ma percezione pubblica ferma; extra opachi persistono
- **Leva (meccanismo di incentivo)**: Indennita' unica uguale per tutti + rimborsi a pie' di lista documentati e pubblicati + continuita' contributiva per il periodo di mandato
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: regolamenti parlamentari / legge
- **Costo**: nullo
- **KPI**: 100% delle spese per assistenti e trasferte parlamentari documentate con fattura elettronica pubblica
- **Chi si oppone**: Beneficiari delle voci accessorie
- **Evidenza**:
    - `F-POL-02` Indennita' parlamentare: ~10.400 EUR lordi/mese alla Camera (~5.000 netti); con diaria e rimborsi ordine di 13.900-14.600 EUR mensili complessivi (Camera dei deputati; Senato, 2024)
    - `F-POL-03` Vitalizi: aboliti dal 1/1/2012: sistema contributivo, pensione a 65 anni con almeno 5 anni di mandato (fino a 60 con piu' mandati); pro rata per il pregresso; ricalcolo contributivo 2018 con contenzioso interno (Delibere Ufficio di Presidenza Camera 2011-2012; Senato, 2012)
- **Nota**: Evitare l'aggancio al reddito precedente: renderebbe l'accesso alla politica proporzionale al reddito
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-POL-05 — Cooling-off period obbligatorio tra incarico pubblico e assunzione nel settore regolato

- **Problema**: Porte girevoli tra regolatore e regolato
- **Leva (meccanismo di incentivo)**: Cooling-off period obbligatorio tra incarico pubblico e assunzione nel settore regolato
- **Benchmark**: UE, USA
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: nullo
- **KPI**: Zero casi di passaggio al settore privato regolato prima di 24 mesi dalla cessazione dell'incarico pubblico
- **Chi si oppone**: Categorie interessate
- **Evidenza**:
    - `F-POL-05` Lobbying: assenza di una legge nazionale organica sulla rappresentanza di interessi (Ricognizione comparata (OCSE, GRECO), 2026)
- **Origine del record**: claude · confidenza alta · stato `proposta`
