---
title: "Proposte — Presidenza della Repubblica"
tags:
  - l-italia-che-vorrei
  - proposte
  - presidenza-repubblica
status: "GENERATO"
sorgente: "dati/proposte.json"
---

# Proposte — Presidenza della Repubblica

> [!warning] File generato
> Prodotto da `strumenti/genera.py` da `dati/proposte.json`. Non modificare a mano: le modifiche vanno fatte sul dataset e rigenerate.

3 proposte nell'ambito `presidenza-repubblica`. Ogni scheda riporta problema, leva, evidenza, oppositori, KPI, fase e vincolo giuridico.
Il formato editoriale di riferimento resta [la scheda proposta](../00_SCHEDA_PROPOSTA.md): le voci qui assenti (costi dettagliati, effetti distributivi, compatibilita' UE) sono lavoro ancora da fare, non voci omesse.

### P-QUIR-01 — Obbligo di motivazione pubblica per il rifiuto di emanazione e per il rinvio; termini certi

- **Problema**: Poteri presidenziali reali ma esercitati in forma informale e non tracciabile (moral suasion)
- **Leva (meccanismo di incentivo)**: Obbligo di motivazione pubblica per il rifiuto di emanazione e per il rinvio; termini certi
- **Fase**: 3 — struttura (4-8 anni)
- **Vincolo giuridico**: legge costituzionale
- **Costo**: nullo
- **KPI**: 100% dei rilievi presidenziali su decreti o leggi accompagnati da motivazione scritta pubblica entro 12 mesi
- **Chi si oppone**: Prassi consolidata del Quirinale
- **Variante**: A (alternativa incompatibile nello stesso ambito: non si sceglie in sede di dataset)
- **Rischio / obiezione piu' forte**: Pubblicare le motivazioni del rifiuto di firma puo' trasformare il Quirinale in un attore politico antagonistico aperto del Governo in carica.
- **Evidenza**:
    - `F-QUIR-01` Poteri effettivi: nomina PdC e ministri, rinvio delle leggi (art. 74), emanazione dei decreti-legge, scioglimento delle Camere, presidenza CSM e Consiglio supremo di difesa, nomina di 5 giudici costituzionali e 5 senatori a vita, grazia, comando forze armate (Costituzione italiana, 2026)
- **Nota**: Percorso A: rafforzare la garanzia mantenendo l'elezione parlamentare. Incompatibile con P-QUIR-03.
- **Origine del record**: claude · confidenza media · stato `proposta`

### P-QUIR-02 — Divieto costituzionale esplicito di secondo mandato

- **Problema**: La non rielezione era convenzione, violata nel 2013 e nel 2022
- **Leva (meccanismo di incentivo)**: Divieto costituzionale esplicito di secondo mandato
- **Fase**: 3 — struttura (4-8 anni)
- **Vincolo giuridico**: legge costituzionale
- **Costo**: nullo
- **KPI**: -
- **Chi si oppone**: Chi valorizza la continuita' in crisi
- **Variante**: A (alternativa incompatibile nello stesso ambito: non si sceglie in sede di dataset)
- **Rischio / obiezione piu' forte**: Il divieto assoluto di secondo mandato priva la Repubblica di una figura di equilibrio collaudata durante gravissime crisi geopolitiche o di sistema.
- **Evidenza**:
    - `F-QUIR-02` Secondo mandato: la non rielezione era una convenzione, derogata nel 2013 (Napolitano) e nel 2022 (Mattarella) (Cronaca istituzionale, 2022)
- **Nota**: Misura interna al percorso A. Incompatibile con P-QUIR-03, che ridisegna la carica.
- **Origine del record**: claude · confidenza alta · stato `proposta`

### P-QUIR-03 — Elezione diretta in quadro semipresidenziale organico

- **Problema**: Legittimazione indiretta del Capo dello Stato
- **Leva (meccanismo di incentivo)**: Elezione diretta in quadro semipresidenziale organico
- **Benchmark**: Francia
- **Fase**: 3 — struttura (4-8 anni)
- **Vincolo giuridico**: legge costituzionale + referendum
- **Costo**: nullo
- **KPI**: -
- **Chi si oppone**: Chi teme due legittimita' concorrenti
- **Variante**: B (alternativa incompatibile nello stesso ambito: non si sceglie in sede di dataset)
- **Rischio / obiezione piu' forte**: L'elezione diretta del Capo dello Stato crea una diarchia conflittuale permanente tra Presidente e Primo Ministro con rischio di paralisi (coabitazione).
- **Evidenza**:
    - `F-QUIR-01` Poteri effettivi: nomina PdC e ministri, rinvio delle leggi (art. 74), emanazione dei decreti-legge, scioglimento delle Camere, presidenza CSM e Consiglio supremo di difesa, nomina di 5 giudici costituzionali e 5 senatori a vita, grazia, comando forze armate (Costituzione italiana, 2026)
- **Nota**: Percorso B: elezione diretta in quadro semipresidenziale organico. Incompatibile con A e con il premierato.
- **Origine del record**: claude · confidenza bassa · stato `proposta`
