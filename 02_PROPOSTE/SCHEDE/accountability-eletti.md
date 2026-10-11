---
title: "Proposte — Accountability degli eletti"
tags:
  - l-italia-che-vorrei
  - proposte
  - accountability-eletti
status: "GENERATO"
generato: "2026-10-11"
sorgente: "dati/proposte.json"
---

# Proposte — Accountability degli eletti

> [!warning] File generato
> Prodotto da `strumenti/genera.py` da `dati/proposte.json`. Non modificare a mano: le modifiche vanno fatte sul dataset e rigenerate.

6 proposte nell'ambito `accountability-eletti`. Ogni scheda riporta problema, leva, evidenza, oppositori, KPI, fase e vincolo giuridico.
Il formato editoriale di riferimento resta [la scheda proposta](../00_SCHEDA_PROPOSTA.md): le voci qui assenti (costi dettagliati, effetti distributivi, compatibilita' UE) sono lavoro ancora da fare, non voci omesse.

### P-ACC-03 — Scheda di valutazione istituzionale pubblica e standardizzata per ogni carica: presenze in aula e commissione, voti, atti, incarichi, patrimonio, finanziamenti

- **Problema**: I dati sugli eletti esistono ma li produce un soggetto privato e non incidono sulla selezione
- **Leva (meccanismo di incentivo)**: Scheda di valutazione istituzionale pubblica e standardizzata per ogni carica: presenze in aula e commissione, voti, atti, incarichi, patrimonio, finanziamenti
- **Fase**: 0 — credibilita' (primi 12 mesi)
- **Vincolo giuridico**: legge ordinaria / regolamenti
- **Costo**: basso
- **KPI**: 100% degli eletti con scheda di rendicontazione delle attivita' istituzionali aggiornata trimestralmente
- **Chi si oppone**: Eletti meno attivi
- **Evidenza**:
    - `F-ACC-02` Composizione del Parlamento: laureati ~70% (in linea con Germania, Francia, Spagna); eta' media 51,5 anni e in aumento; under 40 al 10,7% degli eletti contro ~23% della popolazione; nessun under 30; permanenza media oltre due legislature (Openpolis; Il Sole 24 Ore; ricerca Bocconi, 2022)
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-ACC-05 — Automazione e trasparenza dei criteri: togliere la merce di scambio invece di punire lo scambio

- **Problema**: Il voto di scambio funziona perche' l'eletto puo' consegnare pratiche, posti, licenze
- **Leva (meccanismo di incentivo)**: Automazione e trasparenza dei criteri: togliere la merce di scambio invece di punire lo scambio
- **Benchmark**: Estonia
- **Fase**: 1 — capacita' (1-3 anni)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: medio
- **KPI**: 100% dei procedimenti per assenteismo oltre il 30% conclusi con decadenza automatica o decurtazione
- **Chi si oppone**: Reti di intermediazione politica
- **Prerequisiti bloccanti**: P-STATO-01, P-STATO-04
- **Evidenza**:
    - `F-ACC-03` Legge Severino: incandidabilita' per condanne definitive sopra soglie di pena per determinati reati; sospensione degli amministratori locali dopo condanna non definitiva (d.lgs. 235/2012, 2012)
    - `F-ACC-01` Mandato imperativo: vietato dall'art. 67 Cost.: esclude il recall senza revisione costituzionale (Costituzione italiana, 2026)
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-ACC-02 — Primarie regolate per legge con albo degli elettori e controlli

- **Problema**: Selezione delle candidature senza regole pubbliche
- **Leva (meccanismo di incentivo)**: Primarie regolate per legge con albo degli elettori e controlli
- **Benchmark**: USA (regolate per legge statale)
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: legge ordinaria (delicata su art. 49 Cost.)
- **Costo**: basso
- **KPI**: 100% delle candidature parlamentari vagliate da procedure selettive trasparenti con criteri pubblici
- **Chi si oppone**: Partiti
- **Evidenza**:
    - `F-ACC-02` Composizione del Parlamento: laureati ~70% (in linea con Germania, Francia, Spagna); eta' media 51,5 anni e in aumento; under 40 al 10,7% degli eletti contro ~23% della popolazione; nessun under 30; permanenza media oltre due legislature (Openpolis; Il Sole 24 Ore; ricerca Bocconi, 2022)
- **Origine del record**: claude · confidenza bassa · stato `proposta`

### P-ACC-04 — Decurtazioni progressive automatiche e decadenza oltre soglia di assenze ingiustificate

- **Problema**: Assenteismo sanzionato solo con decurtazioni marginali
- **Leva (meccanismo di incentivo)**: Decurtazioni progressive automatiche e decadenza oltre soglia di assenze ingiustificate
- **Benchmark**: Consigli comunali e regionali italiani (gia' prevista)
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: regolamenti parlamentari / legge costituzionale
- **Costo**: nullo
- **KPI**: Tasso di presenza alle votazioni in aula e commissione superiore all'85% per oltre il 90% degli eletti
- **Chi si oppone**: Eletti; rischio di conflitto con art. 67
- **Evidenza**:
    - `F-ACC-02` Composizione del Parlamento: laureati ~70% (in linea con Germania, Francia, Spagna); eta' media 51,5 anni e in aumento; under 40 al 10,7% degli eletti contro ~23% della popolazione; nessun under 30; permanenza media oltre due legislature (Openpolis; Il Sole 24 Ore; ricerca Bocconi, 2022)
- **Origine del record**: claude · confidenza media · stato `proposta`

### P-ACC-06 — Mantenere l'incandidabilita' alla condanna definitiva (legge Severino) e agire sui tempi del processo

- **Problema**: Richiesta di escludere i condannati; tensione con la presunzione di innocenza
- **Leva (meccanismo di incentivo)**: Mantenere l'incandidabilita' alla condanna definitiva (legge Severino) e agire sui tempi del processo
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: nullo
- **KPI**: Durata media dei procedimenti giudiziari a carico di titolari di cariche pubbliche inferiore a 2 anni
- **Chi si oppone**: Chi chiede esclusione gia' in primo grado
- **Evidenza**:
    - `F-ACC-03` Legge Severino: incandidabilita' per condanne definitive sopra soglie di pena per determinati reati; sospensione degli amministratori locali dopo condanna non definitiva (d.lgs. 235/2012, 2012)
- **Nota**: Estendere alle condanne non definitive darebbe a un giudice di primo grado il potere di escludere un avversario politico
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-ACC-01 — Collegi uninominali o liste molto corte in collegi piccoli

- **Problema**: Voto personale organizzato (reti clientelari) in collegi ampi con preferenze
- **Leva (meccanismo di incentivo)**: Collegi uninominali o liste molto corte in collegi piccoli
- **Benchmark**: UK, Germania (quota uninominale)
- **Fase**: 3 — struttura (4-8 anni)
- **Vincolo giuridico**: legge elettorale
- **Costo**: nullo
- **KPI**: Indice di concentrazione elettorale ridotto; quota eletti con voti territorialmente diffusi >75%
- **Chi si oppone**: Partiti che perdono controllo sulle liste
- **Evidenza**:
    - `F-PSICO-02` Fiducia istituzionale: La fiducia nelle istituzioni nazionali (governo e parlamento) e' attestata al 27% (media UE 36%), a fronte di una fiducia nella cerchia familiare ristretta superiore all'88% (Commissione Europea, Standard Eurobarometer 101; Istat, Rapporto BES, 2024) **[NON VERIFICATO — vietato in pubblicazione]**
- **Nota**: Le liste bloccate sono la soluzione opposta e peggiorativa: spostano il potere ai capipartito
- **Origine del record**: claude · confidenza media · stato `proposta`
