---
title: "Registro delle correzioni al dataset"
tags:
  - l-italia-che-vorrei
  - verifica
  - decisioni
status: "ATTIVO"
---

# Registro delle correzioni al dataset

Ogni modifica al dataset che non sia l'aggiunta di un record nuovo viene registrata qui: cosa è cambiato, perché, su quale base, e chi l'ha proposta. Le versioni di lavoro originarie non sono pubblicate per ragioni di riservatezza; le correzioni vanno quindi controllate sulle fonti qui citate.

Le correzioni qui elencate sono **strutturali**: riguardano la coerenza interna del dataset e il rispetto dello schema. Nessuna di esse cambia una cifra, una fonte o il merito di una proposta. Le correzioni di merito richiedono una fonte primaria e vanno registrate con la stessa struttura.

---

## C-01 — Tre fatti con ambito fuori vocabolario

**Record**: `F-DEMO-05`, `F-DEMO-07`, `F-LAV-01`
**Cosa**: `ambito: "lavoro"` → `ambito: "lavoro-capitale-umano"`
**Perché**: `lavoro` non esiste nel vocabolario dello schema. L'ambito è la chiave di join primaria del merge: un valore fuori vocabolario rende quei fatti invisibili al confronto con i contributi di altri modelli, che useranno la chiave corretta.
**Impatto sul merito**: nessuno.
**Proposto da**: claude · **Stato**: APPLICATO

## C-02 — Due valori di costo fuori enum

**Record**: `P-PROD-04` (`medio (indennizzi)` → `medio`), `P-IST-04` (`alto (LEP)` → `alto`)
**Cosa**: classe di costo normalizzata all'enum, qualificazione spostata in `nota`.
**Perché**: l'enum serve ad aggregare il costo del piano per fase. Una stringa libera rompe l'aggregazione e l'informazione va comunque persa nel conteggio. La qualificazione è sostanziale e va conservata, ma in un campo di testo.
**Impatto sul merito**: nessuno. In entrambi i casi la nota precisa che il costo è quasi interamente una voce specifica — indennizzi transitori nel primo caso, finanziamento dei livelli essenziali delle prestazioni nel secondo — e non il costo della riforma ordinamentale in sé.
**Proposto da**: claude · **Stato**: APPLICATO

## C-03 — Tre dipendenze con inversione di fase

Tre proposte dichiaravano come prerequisito bloccante una proposta collocata in una fase successiva. Letteralmente, non sarebbero mai state attivabili. È l'errore che rende un piano inattuabile senza che nessuno l'abbia deciso, e ora il validatore lo blocca.

### C-03a — `P-PROD-02` (sportello unico investimenti, fase 0)

Dichiarava `dipende_da: P-IST-04` (clausola di supremazia e riordino del Titolo V, fase 3).
**Correzione**: declassata a `rafforzata_da`. La proposta resta in fase 0.
**Motivo**: lo sportello unico con potere sostitutivo è attivabile con legge ordinaria nel quadro costituzionale vigente — il potere sostitutivo statale è già previsto dall'art. 120 Cost. La clausola di supremazia su infrastrutture ed energia ne amplierebbe il perimetro, ma non ne è condizione di esistenza. Tenerla come prerequisito bloccante avrebbe spostato in fase 3 una delle poche misure a costo trascurabile della fase 0.

### C-03b — `P-DEMDIR-06` e `P-DEMDIR-02`: relazione invertita

`P-DEMDIR-06` (tetti di spesa e trasparenza sulle campagne referendarie, fase 2) dichiarava `dipende_da: P-DEMDIR-02` (referendum propositivo, fase 3).
**Correzione**: la dipendenza è stata **invertita**. Ora è `P-DEMDIR-02` a dipendere da `P-DEMDIR-06`.
**Motivo**: è la correzione più sostanziale delle quattro, e discende dall'analisi stessa. Dove il finanziamento delle campagne referendarie non è regolato, l'iniziativa popolare diventa lo strumento di chi può pagarla. I tetti di spesa non sono una conseguenza del referendum propositivo: ne sono la precondizione. Con la firma digitale, che dal 2021 ha azzerato il costo di raccolta, la questione non è teorica.
**Nota**: questa correzione cambia la sequenza del piano ed è quindi di merito, non solo strutturale. È registrata come tale e resta contestabile.

### C-03c — `P-TRASP-02` (stralcio automatico dai decreti omnibus, fase 2)

Dichiarava `dipende_da: P-QUIR-01` (obbligo di motivazione pubblica degli atti presidenziali, fase 3).
**Correzione**: declassata a `rafforzata_da`. La proposta resta in fase 2.
**Motivo**: l'obbligo di omogeneità del decreto-legge esiste già (art. 15 l. 400/1988) ed è disatteso; renderlo cogente con stralcio automatico richiede legge ordinaria. Il rilievo formale del Presidente in sede di emanazione lo rende più efficace, ma non è prerequisito.

**Proposto da**: claude · **Stato**: APPLICATO, con C-03b marcata come correzione di merito

## C-04 — Sei varianti con etichetta non normalizzata

**Record**: `P-QUIR-01`, `P-QUIR-02`, `P-QUIR-03`, `P-SENV-01`, `P-SENV-02`, `P-SENV-03`
**Cosa**: il campo `variante` conteneva frasi intere ("A — rafforzare la garanzia mantenendo l'elezione parlamentare"). Ora contiene una sola lettera; la descrizione del percorso è in `nota`.
**Perché**: con la descrizione dentro l'etichetta, due proposte dello stesso percorso risultavano varianti diverse e il controllo di completezza A/B non poteva funzionare. Nel caso della Presidenza della Repubblica, `P-QUIR-01` e `P-QUIR-02` appartengono entrambe al percorso A (rafforzare la garanzia mantenendo l'elezione parlamentare) e sono entrambe incompatibili con `P-QUIR-03` (elezione diretta): ora il dataset lo dice.
**Impatto sul merito**: nessuno. Le alternative restano aperte e non risolte, come previsto dal protocollo.
**Proposto da**: claude · **Stato**: APPLICATO

---

## Correzioni segnalate e NON applicate

Elencate perché la scelta di non intervenire è una decisione, e va motivata.

| # | Rilievo | Perché non è stato corretto |
|---|---|---|
| N-01 | 58 proposte su 74 hanno un KPI senza soglia numerica | Inventare una soglia per far tornare la tabella produrrebbe un dato falso con l'aspetto di una misura. Sono elencate in [05_KPI_DA_QUANTIFICARE](05_KPI_DA_QUANTIFICARE.md) come lavoro aperto. |
| N-02 | 18 proposte non hanno evidenza collegata | Collegare un fatto qualsiasi per far sparire l'avviso è peggio del vuoto. Restano a priorità minore, come previsto dallo schema. |
| N-03 | 6 fatti hanno `verificato: false` | Vanno confermati su fonte primaria o rimossi, non ripuliti con un flag. Fino ad allora sono esclusi dai documenti pubblici, e il divieto è ora verificato in automatico. |
| N-04 | 14 proposte su temi contestati non hanno il campo `rischio` | Il rischio va scritto da chi sostiene la proposta, non dedotto a posteriori da chi passa i dati. Segnalato dal validatore a ogni esecuzione. |
| N-05 | Un solo `gate` su 74 proposte | Il piano si regge sull'idea che una fase non si apra prima che la precedente abbia dato risultati misurati, ma i gate non sono nel dataset: sono solo nella narrativa. È la lacuna più seria fra quelle aperte. |
| N-06 | `F-ECO-05` e `F-PSICO-02` non sono citati da nessuna proposta | Un fatto può essere di contesto e non di supporto. Da decidere caso per caso, non in blocco. |
