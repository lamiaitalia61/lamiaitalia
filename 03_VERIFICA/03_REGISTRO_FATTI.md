---
title: "Registro dei fatti"
tags:
  - l-italia-che-vorrei
  - verifica
  - fatti
status: "GENERATO"
generato: "2026-10-11"
sorgente: "dati/fatti.json"
---

# Registro dei fatti

> [!warning] File generato
> Prodotto da `strumenti/genera.py` da `dati/fatti.json`. Non modificare a mano: le modifiche vanno fatte sul dataset e rigenerate.

66 record. Un numero senza fonte e anno non entra nel dataset. I record marcati NON VERIFICATO non possono comparire in 06_PUBBLICAZIONE.


## Accountability degli eletti

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-ACC-01` | Mandato imperativo | vietato dall'art. 67 Cost.: esclude il recall senza revisione costituzionale | Costituzione italiana | 2026 | primaria | VERIFICATO | P-ACC-05 |
| `F-ACC-02` | Composizione del Parlamento | laureati ~70% (in linea con Germania, Francia, Spagna); eta' media 51,5 anni e in aumento; under 40 al 10,7% degli eletti contro ~23% della popolazione; nessun under 30; permanenza media oltre due legislature | Openpolis; Il Sole 24 Ore; ricerca Bocconi | 2022 | secondaria | VERIFICATO | P-ACC-02, P-ACC-03, P-ACC-04, P-TRASP-04 |
| `F-ACC-03` | Legge Severino | incandidabilita' per condanne definitive sopra soglie di pena per determinati reati; sospensione degli amministratori locali dopo condanna non definitiva | d.lgs. 235/2012 | 2012 | primaria | VERIFICATO | P-ACC-05, P-ACC-06 |

## Capitale civico

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-PSICO-01` | Tax morale condizionata | La tax morale e la compliance spontanea sono correlate positivamente alla percezione che anche gli altri contribuenti paghino (equita' orizzontale) e che le risorse siano impiegate in servizi pubblici visibili | OECD, 'Tax Morale II: Building Trust between Tax Administrations and Large Businesses and Individuals'; Banca d'Italia, QEF n. 531 | 2023 | primaria | **DA VERIFICARE** | P-FISC-06 |
| `F-PSICO-02` | Fiducia istituzionale | La fiducia nelle istituzioni nazionali (governo e parlamento) e' attestata al 27% (media UE 36%), a fronte di una fiducia nella cerchia familiare ristretta superiore all'88% | Commissione Europea, Standard Eurobarometer 101; Istat, Rapporto BES | 2024 | primaria | **DA VERIFICARE** | P-ACC-01 |

## Costi della politica

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-POL-01` | Autodichia | Camera e Senato deliberano su se stessi in materia di trattamento economico e previdenziale; i ricorsi sono decisi da organi interni | Regolamenti parlamentari; Corte cost. sent. 262/2017 | 2026 | primaria | VERIFICATO | P-POL-01, P-TRASP-05, P-POL-07-GEM |
| `F-POL-02` | Indennita' parlamentare | ~10.400 EUR lordi/mese alla Camera (~5.000 netti); con diaria e rimborsi ordine di 13.900-14.600 EUR mensili complessivi | Camera dei deputati; Senato | 2024 | primaria | VERIFICATO | P-POL-01, P-POL-02 |
| `F-POL-03` | Vitalizi | aboliti dal 1/1/2012: sistema contributivo, pensione a 65 anni con almeno 5 anni di mandato (fino a 60 con piu' mandati); pro rata per il pregresso; ricalcolo contributivo 2018 con contenzioso interno | Delibere Ufficio di Presidenza Camera 2011-2012; Senato | 2012 | primaria | VERIFICATO | P-POL-02 |
| `F-POL-04` | Finanziamento ai partiti | finanziamento pubblico diretto abolito nel 2013 (uscita entro il 2017), sostituito da 2x1000 e donazioni; obblighi di trasparenza l. 13/2014 che non coprono pienamente fondazioni e comitati | d.l. 149/2013; l. 13/2014 | 2017 | primaria | VERIFICATO | P-POL-03, P-POL-07-GEM |
| `F-POL-05` | Lobbying | assenza di una legge nazionale organica sulla rappresentanza di interessi | Ricognizione comparata (OCSE, GRECO) | 2026 | secondaria | VERIFICATO | P-POL-04, P-POL-05 |

## Democrazia diretta

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-REF-01` | Quorum raggiunto | negli ultimi 30 anni, su 10 referendum non costituzionali il quorum e' stato raggiunto 2 volte | Ipsos / Corriere della Sera | 2025 | secondaria | VERIFICATO | P-DEMDIR-01 |
| `F-REF-02` | Referendum 8-9 giugno 2025 | affluenza 30,58%; quorum mancato; Si' all'88-89% sui quesiti lavoro e 65% su cittadinanza | Ministero dell'Interno; Pagella Politica | 2025 | primaria | VERIFICATO | P-DEMDIR-01 |
| `F-REF-03` | Affluenza e polarizzazione | correlazione 0,77 tra affluenza regionale ai referendum 2025 e voto ai partiti di sinistra alle europee 2024 | Studi Elettorali | 2025 | secondaria | VERIFICATO | P-DEMDIR-01, P-DEMDIR-05 |
| `F-REF-04` | Tipologia referendum | art. 75: solo abrogativo, 500k firme o 5 consigli regionali, escluse materie tributarie, di bilancio, amnistia e trattati; art. 138: costituzionale senza quorum | Costituzione italiana | 2026 | primaria | VERIFICATO | P-DEMDIR-02 |
| `F-REF-05` | Scelta della data | nel 2025 il voto fu fissato in coincidenza con i ballottaggi, contro la richiesta dei promotori | Cronaca; Wikipedia referendum 2025 | 2025 | secondaria | VERIFICATO | P-DEMDIR-03 |
| `F-REF-06` | Referendum costituzionale 2026 | 22-23 mar. 2026, separazione delle carriere e riassetto CSM: prevale il No, riforma non entrata in vigore; per circa il 31% degli elettori del No fu un voto contro il governo | Ministero dell'Interno; YouTrend | 2026 | primaria | VERIFICATO | P-DEMDIR-04 |
| `F-REF-07` | Firma digitale | dal 2021 firma digitale con piattaforma pubblica: costo di raccolta crollato | d.l. 77/2021 e successive | 2021 | primaria | VERIFICATO | P-DEMDIR-06 |

## Demografia

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-DEMO-01` | Nascite | 355.000 nel 2025, minimo dal dopoguerra (-3,9% sul 2024) | Istat | 2025 | primaria | VERIFICATO | P-DEMO-01 |
| `F-DEMO-02` | Saldo naturale / eta' media | -296.000 in un anno; eta' media 49,1 anni (UE 44,9) | Istat, 1/1/2026 | 2026 | primaria | VERIFICATO | P-DEMO-05, P-DEMO-08-GEM |
| `F-DEMO-03` | Divario desiderio/realta' | con le intenzioni dichiarate sarebbero nati ~760.000 bambini; 62% ha rinunciato per ostacoli economici e sociali, 5,5% per scelta | Istat | 2025 | primaria | VERIFICATO | P-DEMO-01, P-DEMO-03, P-DEMO-04 |
| `F-DEMO-04` | Saldo laureati 25-34 | -21.000 in un anno (25k espatri, 4k rientri) | Istat, report giovani e migrazioni mag. 2026 | 2026 | primaria | VERIFICATO | P-LAV-05 |
| `F-DEMO-06` | Donne in eta' fertile | 11,5 mln oggi contro 14,3 mln nel 1995; proiezione ~9 mln al 2050 | Istat | 2026 | primaria | VERIFICATO | P-DEMO-06, P-IMM-03 |
| `F-DEMO-08` | Copertura asili nido e divario territoriale | 31,6 posti autorizzati nei servizi educativi 0-2 anni ogni 100 residenti; 19,0 nel Sud e 19,5 nelle Isole | Istat, Offerta di nidi e servizi integrativi per la prima infanzia, anno educativo 2023/2024, https://www.istat.it/comunicato-stampa/offerta-di-nidi-e-servizi-integrativi-per-la-prima-infanzia-anno-educativo-2023-2024/ | 2024 | primaria | VERIFICATO | P-DEMO-01, P-DEMO-02 |

## Energia

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-ECO-04` | Prezzo energia industriale | tra i piu' alti UE; indicato come freno alla competitivita' | OCSE Economic Survey Italy 2026 | 2026 | primaria | VERIFICATO | P-PROD-03 |

## Fisco

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-FISC-01` | Tax gap | ~100 mld EUR/anno; propensione all'evasione 17% | MEF, Relazione su economia non osservata ed evasione | 2025 | primaria | VERIFICATO | P-FISC-01, P-FISC-02, P-FISC-05 |
| `F-FISC-02` | Tax gap lavoro autonomo | ~60% del reddito | Commissione UE / UPB | 2025 | primaria | VERIFICATO | P-FISC-05 |
| `F-FISC-03` | Spese fiscali censite nel Rapporto MEF 2023 | 625 misure censite nel Rapporto 2023; 555 ancora vigenti nel 2024; effetti finanziari stimati per 411 misure quantificabili pari a circa 96,3 miliardi di euro nel 2024 | MEF, Rapporto annuale sulle spese fiscali 2023, p. 15, https://www.mef.gov.it/export/sites/MEF/documenti-allegati/2023/Rapporto-spese-fiscali-2023.pdf | 2024 | primaria | VERIFICATO | P-FISC-02 |

## Giustizia

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-PNRR-02` | Disposition time civile | target PNRR centrati, in parte grazie allo sprint della Cassazione che ha compensato i ritardi di primo e secondo grado | Ministero della Giustizia, monitoraggio PNRR | 2026 | primaria | VERIFICATO | P-STATO-05 |

## Immigrazione

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-IMM-01` | Rimpatri UE | I trim. 2026: 108.475 ordini di allontanamento, 34.550 rimpatri effettivi (~32%) | Eurostat / Commissione UE (via stampa parlamentare) | 2026 | secondaria | VERIFICATO | P-IMM-01 |
| `F-IMM-02` | Centri in Albania | La gestione dei centri di trattenimento extra-territoriali (Albania) ha registrato ritardi procedurali derivanti dalla necessaria applicazione delle tutele giurisdizionali (art. 5 CEDU e Direttiva Procedure UE) | Ministero dell'Interno, Dipartimento Liberta' Civili e Immigrazione; Relazione Garante Nazionale Persone Private della Liberta' | 2025 | primaria | **DA VERIFICARE** | P-IMM-01 |
| `F-IMM-03` | Espulsione del condannato | gia' prevista dall'art. 16 TU immigrazione come misura alternativa; applicazione scarsa | d.lgs. 286/1998 | 2026 | primaria | VERIFICATO | P-IMM-02 |
| `F-IMM-04` | Quadro UE 2026 | Patto migrazione e asilo operativo dal 12/06/2026; Regolamento rimpatri approvato dal PE il 17/06/2026 (418-218-30): ordine europeo di rimpatrio, trattenimento fino a 24 mesi prorogabili a 30, return hubs in Paesi terzi | Parlamento europeo; Centro Astalli; Open Migration | 2026 | primaria | VERIFICATO | P-IMM-04 |

## Istituzioni

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-IST-01` | Instabilita' di governo | circa 70 governi in 80 anni; durata media poco piu' di un anno | Camera dei deputati, serie storiche | 2026 | primaria | VERIFICATO | P-IST-01 |
| `F-IST-02` | Decretazione d'urgenza | uso sistematico di decreti-legge, maxiemendamenti e voti di fiducia; requisito di omogeneita' (art. 15 l. 400/1988) disatteso | Servizi studi parlamentari; Openpolis | 2026 | secondaria | VERIFICATO | P-IST-02, P-TRASP-01, P-TRASP-02, P-TRASP-03 |
| `F-IST-03` | Leggi elettorali | 4 sistemi dal 1993, 2 dichiarati incostituzionali; nel 2026 nuovo sistema in discussione con premio di seggi sopra il 42% | Corte costituzionale sent. 1/2014 e 35/2017; cronaca parlamentare 2026 | 2026 | primaria | VERIFICATO | P-IST-03 |
| `F-IST-04` | Titolo V | competenze concorrenti dal 2001; conflittualita' Stato-Regioni; 21 sistemi sanitari con esiti diseguali | Corte costituzionale; Agenas | 2026 | secondaria | VERIFICATO | P-IST-04 |
| `F-IST-05` | Comuni | ~7.900 comuni, molti sotto 5.000 abitanti | Istat | 2026 | primaria | VERIFICATO | P-IST-05 |
| `F-IST-06` | Iniziativa legislativa | circa 75% delle leggi della legislatura di iniziativa governativa, ~25% parlamentare | Openparlamento (Openpolis) | 2026 | secondaria | VERIFICATO | P-IST-02, P-TRASP-06 |
| `F-IST-07` | Pronunce della Corte costituzionale in via principale | 59 pronunce in via principale nel 2024 su 212 pronunce complessive (circa 28%); il dato non misura quante vertano specificamente sul riparto delle competenze del Titolo V | Corte costituzionale, Annuario 2024, Un anno in cifre, https://www.cortecostituzionale.it/annuario2024/un-anno-in-cifre.html | 2024 | primaria | VERIFICATO | P-IST-04 |
| `F-SAN-01` | Divario territoriale nei Livelli Essenziali di Assistenza (LEA) | Nel monitoraggio NSG 2024 Calabria, Sicilia e Provincia autonoma di Bolzano non raggiungono 60 punti in tutte e tre le macro-aree; le altre Regioni e Province autonome si collocano sopra la soglia in ciascuna macro-area | Ministero della Salute, sintesi NSG 2024, 10 luglio 2026, https://www.salute.gov.it/new/it/news-e-media/notizie/livelli-essenziali-di-assistenza-sintesi-dei-risultati-del-nuovo-sistema-di-0/ | 2024 | primaria | VERIFICATO | P-IST-04, P-SAN-01-CLA |
| `F-SAN-02` | Mobilita' sanitaria interregionale passiva | Saldo netto della mobilita sanitaria tra regioni da quantificare su matrice di flussi dell anno 2024 | Fondazione GIMBE su dati Ministero della Salute, Rapporto Mobilita' Sanitaria 2024 | 2024 | secondaria | **DA VERIFICARE** | P-IST-04 |

## Lavoro e capitale umano

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-DEMO-05` | Occupati entro 3 anni dal titolo | 67,6% (Eurozona 81%, Germania >90%) | CSC su Istat/Eurostat | 2026 | primaria | VERIFICATO | P-LAV-05 |
| `F-DEMO-07` | Assunzioni di stranieri per settore | La quota di ingressi extra-UE programmati copre il 38,4% della domanda in agricoltura, il 29,8% nelle costruzioni e il 51,2% nei servizi di cura e assistenza domiciliare | Ministero del Lavoro e delle Politiche Sociali / Unioncamere, Rapporto Annuale Excelsior | 2025 | primaria | **DA VERIFICARE** | P-DEMO-06 |
| `F-LAV-01` | NEET 15-29 e abbandono scolastico | NEET 13,3% (era 25,7% dieci anni fa); abbandono 8,2%, sotto media UE 9,1% | Istat | 2025 | primaria | VERIFICATO | P-LAV-01, P-LAV-03, P-LAV-06-GEM |

## Limiti di mandato

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-MAND-01` | Limiti vigenti | sindaci 2 mandati consecutivi (3 sotto i 5.000 abitanti); presidenti di regione 2 mandati consecutivi; nessun limite per parlamentari, ministri e Presidente del Consiglio | TUEL; l. 165/2004 | 2026 | primaria | VERIFICATO | P-MAND-01, P-MAND-02 |
| `F-MAND-02` | Giurisprudenza costituzionale | divieto di terzo mandato confermato per la Campania (apr. 2025) ed esteso alle autonomie speciali (nov. 2025, caso Trento) come principio generale dell'ordinamento; ulteriore pronuncia con sent. 16/2026 | Corte costituzionale | 2026 | primaria | VERIFICATO | P-MAND-01 |
| `F-MAND-03` | Evidenza sui term limits | Negli Stati USA con limiti di mandato (15 Stati) l'evidenza empirica dimostra un sensibile spostamento di potere dai parlamentari novizi verso staff burocratici permanenti, agenzie esecutive e lobby di settore | National Conference of State Legislatures (NCSL); Carey, Niemi & Powell (University of Michigan Press) | 2024 | primaria | **DA VERIFICARE** | P-MAND-03 |

## Quadro macroeconomico

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-ECO-01` | Debito pubblico / PIL | ~138,6% previsto 2026 (sopra la Grecia) | DFP 2026; FMI Fiscal Monitor apr. 2026 | 2026 | primaria | VERIFICATO | P-DEMO-05, P-FISC-08-GEM |
| `F-ECO-02` | Debito nominale | oltre 3.200 mld EUR (giu. 2026) | Banca d'Italia | 2026 | primaria | VERIFICATO | P-FISC-08-GEM |
| `F-ECO-03` | Salari reali medi | nel 2024 sotto il livello 1990 (-1,6%); media OCSE +35% | UPB su dati OCSE | 2024 | primaria | VERIFICATO | P-FISC-01, P-FISC-02, P-LAV-02, P-LAV-04, P-LAV-06-GEM |
| `F-ECO-05` | Produttivita' | sostanzialmente ferma dalla meta' degli anni '90 | OCSE; Banca d'Italia | 2026 | primaria | VERIFICATO | P-PROD-01, P-PROD-04 |
| `F-ECO-06` | Spesa pensionistica vs famiglia e istruzione | Quote comparabili di spesa per pensioni, famiglia e istruzione da ricostruire per lo stesso anno e con lo stesso perimetro | Eurostat, Social Protection Statistics 2024; Istat | 2024 | primaria | **DA VERIFICARE** | P-DEMO-01 |
| `F-ECO-07` | Spesa per servizio del debito pubblico | Spesa per interessi del 2025 da accertare con conto consuntivo e definizione omogenea | MEF, Documento di Finanza Pubblica (DFP) 2025-2026 | 2025 | primaria | **DA VERIFICARE** | — |

## Paradossi strutturali

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-PARAD-01` | Ricchezza privata vs debito pubblico | ricchezza netta delle famiglie tra le piu' alte d'Europa in rapporto al reddito, a fronte di debito pubblico tra i piu' alti al mondo | Banca d'Italia, Relazione annuale | 2026 | primaria | VERIFICATO | P-FISC-03 |
| `F-PARAD-02` | Nanismo d'impresa | soglie dimensionali fiscali e lavoristiche a 5/15/50 addetti disincentivano la crescita | OCSE; Banca d'Italia | 2026 | primaria | VERIFICATO | P-FISC-04 |

## PNRR

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-PNRR-01` | Chiusura PNRR | 31 ago. 2026 per milestone e rendicontazione; 31 dic. 2026 per i pagamenti finali; ~85% risorse erogate ma spesa effettiva molto indietro | Commissione europea; monitoraggio nazionale | 2026 | primaria | VERIFICATO | P-IST-05 |

## Presidenza della Repubblica

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-QUIR-01` | Poteri effettivi | nomina PdC e ministri, rinvio delle leggi (art. 74), emanazione dei decreti-legge, scioglimento delle Camere, presidenza CSM e Consiglio supremo di difesa, nomina di 5 giudici costituzionali e 5 senatori a vita, grazia, comando forze armate | Costituzione italiana | 2026 | primaria | VERIFICATO | P-QUIR-01, P-QUIR-03 |
| `F-QUIR-02` | Secondo mandato | la non rielezione era una convenzione, derogata nel 2013 (Napolitano) e nel 2022 (Mattarella) | Cronaca istituzionale | 2022 | primaria | VERIFICATO | P-QUIR-02 |

## Senatori a vita

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-SENV-01` | Senatori a vita | art. 59: ex Presidenti della Repubblica di diritto + max 5 nominati contemporaneamente; votano anche la fiducia. Con il Senato ridotto a 200 elettivi il loro peso relativo e' cresciuto di circa il 50% | Costituzione; l. cost. 1/2020 | 2020 | primaria | VERIFICATO | P-SENV-01, P-SENV-02, P-SENV-03 |

## Sicurezza

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-SIC-01` | Numero di forze di polizia | quattro nazionali (PS, CC, GdF, Penitenziaria); il Corpo Forestale e' stato assorbito dai Carabinieri nel 2016 | l. 124/2015 e d.lgs. attuativi | 2016 | primaria | VERIFICATO | P-SIC-01, P-SIC-03, P-SIC-04 |
| `F-SIC-02` | Agenti per abitante | tra i rapporti piu' alti d'Europa | Osservatorio CPI su dati Eurostat | 2019 | secondaria | VERIFICATO | P-SIC-02 |
| `F-SIC-03` | Risparmi dell'accorpamento | riforma 2015: meno di 60 mln a regime su una spesa di ~22,6 mld | Osservatorio CPI | 2019 | secondaria | VERIFICATO | P-SIC-01 |
| `F-SIC-04` | Operazione Strade Sicure | attiva dal 2008 con impiego permanente di militari in funzione di presidio | Ministero della Difesa | 2026 | primaria | VERIFICATO | P-SIC-05 |

## Stato leggibile

| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |
|---|---|---|---|---|---|---|---|
| `F-STATO-01` | Oneri amministrativi | la complessita' amministrativa e la lentezza dei procedimenti sono indicate tra i freni diretti alla crescita e agli investimenti | OCSE Economic Survey Italy 2026 | 2026 | primaria | VERIFICATO | P-STATO-01, P-STATO-04, P-STATO-06, P-PROD-02, P-STATO-07-GEM |
| `F-STATO-02` | Stock normativo | 11.192 leggi primarie statali vigenti (inclusi decreti legislativi e decreti legge convertiti); il computo delle 'oltre 100.000 leggi' deriva da atti secondari e regolamentari storici non abrogati espressamente | Normattiva / Dipartimento per gli Affari Giuridici e Legislativi (DAGL), Presidenza del Consiglio dei Ministri | 2026 | primaria | **DA VERIFICARE** | P-STATO-02, P-STATO-03 |
| `F-STATO-03` | Controlli formali preventivi vs controlli di rendimento | Ripartizione dei controlli amministrativi preventivi e successivi da misurare con definizioni e fonte puntuale | Corte dei Conti, Relazione sul coordinamento della finanza pubblica 2024 | 2024 | primaria | **DA VERIFICARE** | P-IST-06 |
