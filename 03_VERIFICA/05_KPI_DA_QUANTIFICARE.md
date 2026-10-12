---
title: "KPI da quantificare"
tags:
  - l-italia-che-vorrei
  - verifica
  - kpi
status: "GENERATO"
sorgente: "dati/proposte.json"
---

# KPI da quantificare

> [!warning] File generato
> Prodotto da `strumenti/genera.py` da `dati/proposte.json`. Non modificare a mano: le modifiche vanno fatte sul dataset e rigenerate.

Regola del progetto: un giudizio si tiene solo se e' falsificabile, cioe' se ha una soglia e una data. 8 proposte hanno un indicatore senza soglia e 6 non hanno KPI. Finche' restano cosi', sono direzioni di marcia, non impegni verificabili: e' la differenza fra un piano e un programma elettorale.


## Indicatore presente ma senza soglia numerica

| ID | Ambito | KPI attuale | Cosa manca |
|---|---|---|---|
| `P-DEMO-08-GEM` | demografia | Quota delle persone non autosufficienti prese in carico con piano integrato, per regione e classe di bisogno; baseline e target da definire | soglia e data |
| `P-FISC-08-GEM` | fisco | Quota dei programmi valutati con dati pubblici e decisione motivata; baseline e target da definire | soglia e data |
| `P-GIU-01-CLA` | giustizia | Copertura e aggiornamento degli indicatori per ufficio; andamento dei tempi su casi comparabili, con baseline e target da definire. | soglia e data |
| `P-POL-07-GEM` | costi-politica | Quota di dichiarazioni complete e controllate nei termini, decisioni di astensione pubblicate; baseline e target da definire | soglia e data |
| `P-SAN-01-CLA` | sanita | Quota di prestazioni entro la classe di priorita, per regione e struttura; baseline e target da definire. | soglia e data |
| `P-STATO-07-GEM` | stato-leggibile | Tempo mediano dei procedimenti campione e rilievi di irregolarita: baseline e soglie da fissare prima della sperimentazione | soglia e data |
| `P-STATO-10-CLA` | stato-leggibile | Quota di pratiche concluse per canale, abbandoni e tempi per gruppi di utenti; baseline e target da definire. | soglia e data |
| `P-STATO-11-CLA` | stato-leggibile | Quota di aventi diritto che presenta domanda, errori di eleggibilita e ricorsi accolti; baseline e target da definire. | soglia e data |

## Nessun KPI

| ID | Ambito | Vincolo giuridico | Ammissibile senza KPI? |
|---|---|---|---|
| `P-QUIR-02` | presidenza-repubblica | legge costituzionale | si', intervento ordinamentale |
| `P-QUIR-03` | presidenza-repubblica | legge costituzionale + referendum | si', intervento ordinamentale |
| `P-SENV-01` | senatori-a-vita | legge costituzionale | si', intervento ordinamentale |
| `P-SENV-02` | senatori-a-vita | legge costituzionale | si', intervento ordinamentale |
| `P-SENV-03` | senatori-a-vita | legge costituzionale | si', intervento ordinamentale |
| `P-TRASP-05` | trasparenza-parlamentare | legge costituzionale | si', intervento ordinamentale |

> Nessuna soglia va inventata per far tornare la tabella. Una soglia senza baseline documentata e' peggio di una casella vuota: sembra una misura e non lo e'.
