---
title: "Proposte — Produttivita' e dimensione d'impresa"
tags:
  - l-italia-che-vorrei
  - proposte
  - produttivita
status: "GENERATO"
generato: "2026-10-11"
sorgente: "dati/proposte.json"
---

# Proposte — Produttivita' e dimensione d'impresa

> [!warning] File generato
> Prodotto da `strumenti/genera.py` da `dati/proposte.json`. Non modificare a mano: le modifiche vanno fatte sul dataset e rigenerate.

4 proposte nell'ambito `produttivita`. Ogni scheda riporta problema, leva, evidenza, oppositori, KPI, fase e vincolo giuridico.
Il formato editoriale di riferimento resta [la scheda proposta](../00_SCHEDA_PROPOSTA.md): le voci qui assenti (costi dettagliati, effetti distributivi, compatibilita' UE) sono lavoro ancora da fare, non voci omesse.

### P-PROD-02 — Sportello unico nazionale investimenti con potere sostitutivo e termine certo

- **Problema**: L'investitore affronta decine di interlocutori e tempi incerti
- **Leva (meccanismo di incentivo)**: Sportello unico nazionale investimenti con potere sostitutivo e termine certo
- **Benchmark**: Irlanda (IDA)
- **Fase**: 0 — credibilita' (primi 12 mesi)
- **Vincolo giuridico**: legge ordinaria + questione Titolo V
- **Costo**: basso
- **KPI**: Tempo mediano per rilascio autorizzazioni industriali ridotto a meno di 60 giorni; +20% FDI entro 3 anni
- **Chi si oppone**: Enti locali (perdita di potere di veto)
- **Rafforzata da (non bloccante)**: P-IST-04
- **Evidenza**:
    - `F-STATO-01` Oneri amministrativi: la complessita' amministrativa e la lentezza dei procedimenti sono indicate tra i freni diretti alla crescita e agli investimenti (OCSE Economic Survey Italy 2026, 2026)
- **Nota**: Lo sportello unico e' attivabile con legge ordinaria nel quadro vigente (potere sostitutivo ex art. 120 Cost.). La clausola di supremazia su infrastrutture ed energia (P-IST-04) ne amplia il perimetro ma non ne e' prerequisito: la dipendenza bloccante originaria invertiva la sequenza fase 0 -> fase 3.
- **Origine del record**: claude · confidenza media · stato `proposta`

### P-PROD-03 — Semplificazione autorizzativa rinnovabili + accumuli + scelta esplicita e documentata sul nucleare di nuova generazione

- **Problema**: Prezzo dell'energia industriale tra i piu' alti UE
- **Leva (meccanismo di incentivo)**: Semplificazione autorizzativa rinnovabili + accumuli + scelta esplicita e documentata sul nucleare di nuova generazione
- **Benchmark**: Spagna (rinnovabili a basso costo), Francia (base nucleare)
- **Fase**: 1 — capacita' (1-3 anni)
- **Vincolo giuridico**: legge ordinaria + Titolo V
- **Costo**: alto
- **KPI**: Differenziale di prezzo dell'energia elettrica industriale rispetto alla media UE azzerato entro il 2028
- **Chi si oppone**: Comitati locali, settori incumbent
- **Rischio / obiezione piu' forte**: Tema politicamente contestato: il nucleare va trattato come variante A/B, non come dato
- **Evidenza**:
    - `F-ECO-04` Prezzo energia industriale: tra i piu' alti UE; indicato come freno alla competitivita' (OCSE Economic Survey Italy 2026, 2026)
- **Origine del record**: claude · confidenza media · stato `proposta`

### P-PROD-01 — Condizionalita' a crescita misurata + valutazione d'impatto pubblica + soppressione automatica

- **Problema**: Incentivi erogati su acquisto di beni, non su risultati
- **Leva (meccanismo di incentivo)**: Condizionalita' a crescita misurata + valutazione d'impatto pubblica + soppressione automatica
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: legge ordinaria
- **Costo**: nullo
- **KPI**: Oltre l'80% degli incentivi pubblici erogati accompagnati da valutazione positiva di addizionalita'
- **Chi si oppone**: Beneficiari attuali
- **Evidenza**:
    - `F-ECO-05` Produttivita': sostanzialmente ferma dalla meta' degli anni '90 (OCSE; Banca d'Italia, 2026)
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-PROD-04 — Apertura concorrenziale con transizione lunga e indennizzi

- **Problema**: Servizi protetti a bassa produttivita' (professioni, concessioni, distribuzione, balneari)
- **Leva (meccanismo di incentivo)**: Apertura concorrenziale con transizione lunga e indennizzi
- **Benchmark**: UE (direttiva servizi), raccomandazioni OCSE
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: legge annuale concorrenza
- **Costo**: medio
- **KPI**: Produttivita' oraria del lavoro nei servizi aumentata di almeno 1 punto percentuale all'anno
- **Chi si oppone**: Ordini e categorie concessionarie
- **Evidenza**:
    - `F-ECO-05` Produttivita': sostanzialmente ferma dalla meta' degli anni '90 (OCSE; Banca d'Italia, 2026)
- **Nota**: Il costo e' prevalentemente di indennizzo transitorio ai titolari di rendite legittimamente acquisite.
- **Origine del record**: claude · confidenza alta · stato `proposta`
