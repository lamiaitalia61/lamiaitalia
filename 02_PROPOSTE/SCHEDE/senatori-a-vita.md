---
title: "Proposte — Senatori a vita"
tags:
  - l-italia-che-vorrei
  - proposte
  - senatori-a-vita
status: "GENERATO"
generato: "2026-10-11"
sorgente: "dati/proposte.json"
---

# Proposte — Senatori a vita

> [!warning] File generato
> Prodotto da `strumenti/genera.py` da `dati/proposte.json`. Non modificare a mano: le modifiche vanno fatte sul dataset e rigenerate.

3 proposte nell'ambito `senatori-a-vita`. Ogni scheda riporta problema, leva, evidenza, oppositori, KPI, fase e vincolo giuridico.
Il formato editoriale di riferimento resta [la scheda proposta](../00_SCHEDA_PROPOSTA.md): le voci qui assenti (costi dettagliati, effetti distributivi, compatibilita' UE) sono lavoro ancora da fare, non voci omesse.

### P-SENV-01 — Esclusione dei senatori a vita dal voto di fiducia, mantenendo parola, iniziativa e voto sulle leggi

- **Problema**: Con il Senato a 200 elettivi il peso dei non eletti e' cresciuto di circa il 50% e puo' decidere la fiducia
- **Leva (meccanismo di incentivo)**: Esclusione dei senatori a vita dal voto di fiducia, mantenendo parola, iniziativa e voto sulle leggi
- **Fase**: 2 — scambio (3-6 anni)
- **Vincolo giuridico**: legge costituzionale
- **Costo**: nullo
- **KPI**: -
- **Chi si oppone**: Chi vede una menomazione della carica
- **Variante**: A (alternativa incompatibile nello stesso ambito: non si sceglie in sede di dataset)
- **Rischio / obiezione piu' forte**: Escludere i senatori a vita dal voto di fiducia riduce lo status di senatore a un ruolo dimezzato, creando una diseguaglianza tra componenti della stessa Camera.
- **Evidenza**:
    - `F-SENV-01` Senatori a vita: art. 59: ex Presidenti della Repubblica di diritto + max 5 nominati contemporaneamente; votano anche la fiducia. Con il Senato ridotto a 200 elettivi il loro peso relativo e' cresciuto di circa il 50% (Costituzione; l. cost. 1/2020, 2020)
- **Nota**: Opzione minima: legge ordinaria o regolamenti parlamentari.
- **Origine del record**: claude · confidenza media · stato `proposta`

### P-SENV-02 — Mandato a termine non rinnovabile (7-9 anni) al posto del seggio a vita

- **Problema**: Idem
- **Leva (meccanismo di incentivo)**: Mandato a termine non rinnovabile (7-9 anni) al posto del seggio a vita
- **Fase**: 3 — struttura (4-8 anni)
- **Vincolo giuridico**: legge costituzionale
- **Costo**: nullo
- **KPI**: -
- **Chi si oppone**: -
- **Variante**: B (alternativa incompatibile nello stesso ambito: non si sceglie in sede di dataset)
- **Rischio / obiezione piu' forte**: La nomina a termine (7-9 anni) puo' indurre il senatore a calcolare posizionamenti politici in vista del proprio futuro post-mandato.
- **Evidenza**:
    - `F-SENV-01` Senatori a vita: art. 59: ex Presidenti della Repubblica di diritto + max 5 nominati contemporaneamente; votano anche la fiducia. Con il Senato ridotto a 200 elettivi il loro peso relativo e' cresciuto di circa il 50% (Costituzione; l. cost. 1/2020, 2020)
- **Nota**: Opzione intermedia: revisione costituzionale, mandato a termine non rinnovabile.
- **Origine del record**: claude · confidenza media · stato `proposta`

### P-SENV-03 — Assorbimento nella seconda camera senza rapporto fiduciario: il problema democratico si scioglie da se'

- **Problema**: Idem
- **Leva (meccanismo di incentivo)**: Assorbimento nella seconda camera senza rapporto fiduciario: il problema democratico si scioglie da se'
- **Fase**: 3 — struttura (4-8 anni)
- **Vincolo giuridico**: legge costituzionale
- **Costo**: nullo
- **KPI**: -
- **Chi si oppone**: -
- **Prerequisiti bloccanti**: P-IST-01
- **Variante**: C (alternativa incompatibile nello stesso ambito: non si sceglie in sede di dataset)
- **Rischio / obiezione piu' forte**: Se la seconda camera mantiene poteri legislativi su materie chiave, il voto dei senatori a vita continua a pesare sull'indirizzo politico generale.
- **Evidenza**:
    - `F-SENV-01` Senatori a vita: art. 59: ex Presidenti della Repubblica di diritto + max 5 nominati contemporaneamente; votano anche la fiducia. Con il Senato ridotto a 200 elettivi il loro peso relativo e' cresciuto di circa il 50% (Costituzione; l. cost. 1/2020, 2020)
- **Nota**: Opzione massima: la questione si scioglie nel superamento del bicameralismo paritario (dipende da P-IST-01).
- **Origine del record**: claude · confidenza alta · stato `proposta`
