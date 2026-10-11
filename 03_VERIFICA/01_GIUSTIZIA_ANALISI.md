---
title: "L'Italia che vorrei — Revisione indipendente GIUSTIZIA"
aliases:
  - "Giustizia — revisione"
tags:
  - l-italia-che-vorrei
  - giustizia
  - verifica
  - costituzione
status: "INCOMPLETO — INPUT ACQUISITO, PROPOSTA NON STRUTTURATA"
reviewer: "CODEX"
version: "v1.0-CODEX"
source_branch: "codex"
date: "2026-09-20"
---

# L'Italia che vorrei — Revisione indipendente GIUSTIZIA

> [!critical] Verdetto
> La precedente analisi non è pubblicabile. L'input originario è ora conservato in materiale di lavoro non pubblicato e contiene indicazioni GIUSTIZIA ad alto livello, ma non un articolato completo. La vecchia nota aveva sostituito l'input con «proposte standard», aggiungendo conclusioni causali non dimostrate, riferimenti normativi incompleti e uno stato istituzionale superato. Questa revisione torna alle affermazioni effettivamente presenti nell'input e ne segnala i limiti.

> [!info] Tracciabilità
> Le fonti, i dati comparati e le verifiche estese sono in [01_GIUSTIZIA_FONTI](../01_RICERCA/01_GIUSTIZIA_FONTI.md). Le opzioni non ancora approvate sono in [01_GIUSTIZIA_OPZIONI](../02_PROPOSTE/01_GIUSTIZIA_OPZIONI.md). Il confronto multi-modello è registrato in [02_GIUSTIZIA_CONFRONTO_MODELLI](02_GIUSTIZIA_CONFRONTO_MODELLI.md).

## Perimetro e metodo

- verifica su fonti primarie o istituzionali, con data e definizione degli indicatori;
- separazione tra fatto, inferenza e scelta normativa;
- controevidenze cercate anche quando indeboliscono la tesi iniziale;
- confronto con Francia, Germania e Spagna senza trasformarlo in classifica;
- controllo di Costituzione, Carta UE, CEDU, diritto UE e fattibilità amministrativa;
- nessun consenso dedotto dal conteggio dei modelli; la revisione Gemini è acquisita, mentre manca ancora una revisione Claude specifica sulla GIUSTIZIA.

## Correzioni e modifiche proposte

### G-00 — Strutturare l'input originario prima di approvare una riforma

- **Problema:** l'input originario contiene proposte di termini certi di decadenza, depenalizzazione e responsabilità per colpa grave, ma non specifica reati, soglie, destinatari, procedura, transizione o coperture.
- **Evidenza:** la conversazione originaria è stata acquisita nel repository dal branch Gemini e archiviata senza riscrittura; non risulta ancora una scheda GIUSTIZIA strutturata nel dataset `dati/proposte.json`.
- **Fonte:** materiale di lavoro non pubblicato; materiale di lavoro non pubblicato; `dati/proposte.json`.
- **Modifica suggerita:** conservare l'input originale, estrarre ogni misura in una scheda con ID stabile e sottoporre lo stesso testo ai revisori prima di redigere un articolato.
- **Incertezza:** l'input è un riassunto conversazionale e potrebbe omettere versioni o precisazioni elaborate altrove.

### G-01 — Sostituire la diagnosi monocausale sugli organici

- **Problema:** «il problema primario è la carenza di personale amministrativo» non è sostenuto da un'analisi causale.
- **Evidenza:** risultano carenze sia tra magistrati sia tra personale amministrativo; il confronto CEPEJ mostra inoltre che il numero grezzo degli addetti non spiega da solo i tempi. La Francia aveva meno personale non giudice per abitante ma tempi inferiori, mentre la Spagna ne aveva molto di più senza avvicinarsi alla Germania.
- **Fonte:** [Commissione europea, Rule of Law Report — capitolo nazionale](https://commission.europa.eu/document/download/019229a1-8c23-4f90-bfe4-f842cd59c6a9_it?filename=16_2_coun_chap_italy_it.pdf); [CEPEJ, Evaluation Report](https://rm.coe.int/cepej-evaluation-report-2024-country-profiles/1680b1e7d0).
- **Modifica suggerita:** usare una diagnosi multifattoriale per ufficio, materia e grado: vacanze effettive, competenze, età e complessità dello stock, flussi, organizzazione, strumenti digitali e tassi di impugnazione.
- **Incertezza:** vacanze e headcount non misurano produttività, qualità o composizione professionale.

### G-02 — Correggere indicatori e stato del miglioramento

- **Problema:** la vecchia analisi citava genericamente dati «2022/2024» e suggeriva differenze di clearance rate non confermate dai dati comparabili più recenti.
- **Evidenza:** nel civile e commerciale contenzioso di primo grado, nel 2024 il clearance rate era circa 95,0% nell'ordinamento di riferimento e 95,4% in Francia: quasi uguale. Il divario maggiore riguarda disposition time e pendenze. Il monitoraggio nazionale 2025 segnala progressi, ma il disposition time civile aggregato era 1.789 giorni, ancora distante dal target PNRR di riduzione del 40% rispetto al 2019; il penale aveva superato il proprio target aggregato, con criticità in Cassazione.
- **Fonte:** [EU Justice Scoreboard 2026](https://commission.europa.eu/document/download/d1367f58-9eed-4ebd-8eb3-68646b7c7ddc_en?filename=2026_eu_justice_scoreboard.PDF); [Ministero, monitoraggio PNRR 2025](https://datiestatistiche.giustizia.it/cmsresources/cms/documents/2025_Continuous_Monitoring_PNRR.pdf).
- **Modifica suggerita:** indicare sempre anno osservato, materia, grado, denominatore e formula; affiancare al disposition time durata effettiva mediana e percentili, età dello stock e qualità.
- **Incertezza:** il disposition time è una durata teorica (`pendenti/definiti × 365`), non la durata media della stessa coorte di fascicoli.

### G-03 — Allineare le priorità penali alla normativa vigente

- **Problema:** proporre semplicemente priorità annuali del Parlamento come novità ignora la disciplina già introdotta e confonde priorità organizzative con rinuncia generalizzata all'azione penale.
- **Evidenza:** la legge delega n. 134/2021 e l'art. 3-bis disp. att. c.p.p., introdotto dal d.lgs. n. 150/2022, prevedono criteri generali indicati dalla legge e criteri trasparenti e predeterminati nei progetti organizzativi. La Corte costituzionale n. 58/2026 ha chiarito che l'art. 112 non impone un indiscriminato *favor actionis*: l'azione è esercitata quando gli elementi sostengono una ragionevole previsione di condanna oltre ogni ragionevole dubbio.
- **Fonte:** [Normattiva, legge n. 134/2021](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=21G00146&atto.dataPubblicazioneGazzetta=2021-10-04); [Normattiva, d.lgs. n. 150/2022, art. 41](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.articolo.numero=41&atto.articolo.sottoArticolo=1&atto.articolo.tipoArticolo=0&atto.codiceRedazionale=22G00159&atto.dataPubblicazioneGazzetta=2022-10-17); [Corte costituzionale n. 58/2026](https://www.cortecostituzionale.it/scheda-pronuncia/2026/58).
- **Modifica suggerita:** descrivere prima il regime vigente; se si vuole cambiarlo, specificare quali priorità, chi le approva, controlli, pubblicità, rimedi e tutela dell'eguaglianza. Una rinuncia politica generalizzata richiederebbe una verifica costituzionale distinta.
- **Incertezza:** il confine tra ordine temporale, selezione organizzativa e non perseguibilità sostanziale dipende dalla formulazione concreta.

### G-04 — Aggiornare la separazione delle carriere

- **Problema:** il testo trattava una riforma costituzionale come se fosse ancora in corso e lasciava intendere che la separazione produca necessariamente dipendenza del PM dall'esecutivo.
- **Evidenza:** la riforma approvata dal Parlamento è stata respinta nel referendum del 22-23 marzo 2026; la Costituzione vigente non è cambiata. Francia, Germania e Spagna mostrano che appartenenza al corpo, separazione delle funzioni, gerarchia e poteri ministeriali possono combinarsi in modi diversi.
- **Fonte:** [Ministero dell'interno, referendum](https://www.interno.gov.it/it/speciali/referendum-22-e-23-marzo-2026); [Gazzetta Ufficiale, esito](https://www.gazzettaufficiale.it/atto/vediMenuHTML?atto.codiceRedazionale=26A02490&atto.dataPubblicazioneGazzetta=2026-05-18&tipoSerie=serie_generale&tipoVigenza=originario); fonti comparate in [01_GIUSTIZIA_FONTI](../01_RICERCA/01_GIUSTIZIA_FONTI.md).
- **Modifica suggerita:** archiviare la descrizione precedente. Un'eventuale nuova proposta deve essere riscritta da zero e specificare status del PM, nomine, disciplina, istruzioni, irremovibilità, organi di autogoverno e regime transitorio.
- **Incertezza:** efficienza e indipendenza non sono effetti automatici dell'etichetta «carriere separate»; dipendono dal disegno complessivo.

### G-05 — Trattare digitalizzazione e AI come programmi ad alto rischio operativo

- **Problema:** chiedere una stima generica dei costi IT non basta e non considera interoperabilità, sistemi legacy, sicurezza, continuità operativa e garanzie processuali.
- **Evidenza:** il processo civile risulta ampiamente digitalizzato, ma permangono lacune nel penale, nei gradi successivi, negli uffici del giudice di pace e nell'interoperabilità. L'AI Act qualifica ad alto rischio gli strumenti che assistono l'autorità giudiziaria nell'interpretazione di fatti e diritto; la decisione finale deve restare umana.
- **Fonte:** [Commissione europea, Rule of Law Report](https://commission.europa.eu/document/download/019229a1-8c23-4f90-bfe4-f842cd59c6a9_it?filename=16_2_coun_chap_italy_it.pdf); [Regolamento (UE) 2024/1689](https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:32024R1689); [Regolamento (UE) 2023/2844](https://eur-lex.europa.eu/eli/reg/2023/2844/oj?locale=it).
- **Modifica suggerita:** per ogni sistema indicare funzione, dati, base giuridica, rischio, CAPEX, OPEX, formazione, log, audit, contestabilità, fallback e responsabile. Partire da automazione ausiliaria verificabile, non da decisioni opache.
- **Incertezza:** costi e perimetro dipendono dall'architettura tecnica e dal riuso delle piattaforme esistenti.

### G-06 — Riformulare il rischio dell'ADR obbligatoria

- **Problema:** «l'ADR obbligatoria limita l'accesso» è troppo assoluto; il rischio dipende dal disegno.
- **Evidenza:** la CGUE ammette condizioni obbligatorie purché non impediscano l'accesso effettivo al giudice e siano rispettate garanzie su costi, termini, tutela cautelare e recesso. I dati nazionali mostrano segnali di maggiore successo della mediazione, ma non provano da soli causalità, risparmio netto o assenza di effetti distributivi.
- **Fonte:** [CGUE, C-75/16, Menini e Rampanelli](https://curia.europa.eu/jcms/upload/docs/application/pdf/2017-06/cp170062it.pdf); [d.lgs. n. 28/2010](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2010-03-04;28); [Corte costituzionale n. 10/2022](https://www.cortecostituzionale.it/scheda-pronuncia/2022/10).
- **Modifica suggerita:** sperimentare per materia, con patrocinio effettivo, tutela urgente, sospensione della prescrizione, termini brevi, monitoraggio di abbandoni, esecuzione degli accordi e impatti sulle parti vulnerabili.
- **Incertezza:** mancano nel progetto costi unitari, denominatori dei tassi di successo e risultati per gruppi sociali.

### G-07 — Non introdurre un court manager già presente nell'ordinamento

- **Problema:** la proposta duplica la dirigenza amministrativa già prevista.
- **Evidenza:** il d.lgs. n. 240/2006 disciplina il dirigente amministrativo e la ripartizione con il magistrato capo dell'ufficio. Il problema verificabile è la copertura, la capacità e la chiarezza delle responsabilità, non l'assenza assoluta della funzione.
- **Fonte:** [Normattiva, d.lgs. n. 240/2006](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=006G0259&atto.dataPubblicazioneGazzetta=2006-07-29); [Ministero, riparto delle competenze](https://www.giustizia.it/giustizia/it/mg_1_8_1.wp?contentId=SDC854829).
- **Modifica suggerita:** rafforzare e coprire la dirigenza esistente, dotarla di analisi dei flussi, budget e procurement digitale, mantenendo i KPI gestionali separati dal contenuto delle decisioni giudiziarie.
- **Incertezza:** serve una mappa aggiornata dei posti coperti, delle deleghe effettive e delle competenze disponibili per sede.

### G-08 — Migliorare gli open data senza creare classifiche distorsive

- **Problema:** «rendere pubbliche le performance» ignora che esistono già dataset e dashboard e che una granularità eccessiva può produrre reidentificazione, gaming e incentivi alla selezione dei casi.
- **Evidenza:** il Ministero pubblica dati su disposition time, clearance rate, pendenze e performance. Dati pseudonimizzati possono restare dati personali; la pubblicazione deve rispettare minimizzazione e proporzionalità.
- **Fonte:** [Ministero, open data](https://datiestatistiche.giustizia.it/it/open_data.page); [Ministero, indicatori di performance](https://datiestatistiche.giustizia.it/it/indicatori_di_performance.page); [CGUE, C-268/21](https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:62021CJ0268); [Garante, diffusione di dati giudiziari](https://www.garanteprivacy.it/home/docweb/-/docweb-display/print/1774813).
- **Modifica suggerita:** proporre standard, dizionario dati, versioni, API, case-mix adjustment, soglie minime e audit; evitare ranking individuali e pubblicazione di celle piccole.
- **Incertezza:** il livello di aggregazione sicuro dipende dai volumi e dalla collegabilità con fascicoli pubblici.

### G-09 — Ridurre la forza del nesso con crescita e investimenti

- **Problema:** la formula «correlazione ampiamente dimostrata» può essere letta come prova che una specifica misura causerà più investimenti esteri.
- **Evidenza:** Commissione e OCSE associano sistemi giudiziari efficaci a migliori condizioni per investimenti e produttività, ma confronti nazionali e studi trasversali non stimano automaticamente il beneficio marginale di una singola assunzione o piattaforma.
- **Fonte:** [EU Justice Scoreboard 2026](https://commission.europa.eu/document/download/d1367f58-9eed-4ebd-8eb3-68646b7c7ddc_en?filename=2026_eu_justice_scoreboard.PDF); [OCSE, Judicial performance and its determinants](https://www.oecd.org/en/publications/judicial-performance-and-its-determinants_5k44x00md5g8-en.html).
- **Modifica suggerita:** scrivere «associata a migliori condizioni» e richiedere un'analisi costi-benefici con controfattuale e sensibilità per ogni misura.
- **Incertezza:** qualità istituzionale generale, composizione economica e selezione degli investimenti sono confondenti.

### G-10 — Documentare i divari territoriali senza schema Nord/Sud

- **Problema:** l'affermazione «a parità di risorse» non aveva dataset né controllo per materia, arretrato o complessità.
- **Evidenza:** il monitoraggio 2025 mostra forti differenze tra uffici, ma anche peggioramenti in alcuni distretti settentrionali e centrali; le risorse non sono necessariamente comparabili. Una dicotomia geografica semplice non regge.
- **Fonte:** [Ministero, monitoraggio PNRR 2025](https://datiestatistiche.giustizia.it/cmsresources/cms/documents/2025_Continuous_Monitoring_PNRR.pdf); [Ministero, dati per ufficio](https://datiestatistiche.giustizia.it/it/dettaglio_CR_e_DT_open_data.page).
- **Modifica suggerita:** confrontare uffici omogenei con data di estrazione, case mix, stock storico, vacanze, sopravvenienze e qualità; pubblicare il metodo prima dei risultati.
- **Incertezza:** i dati pubblici potrebbero non contenere tutte le variabili necessarie a un'inferenza causale.

### G-11 — Riconciliare costi PNRR e spesa strutturale

- **Problema:** la vecchia analisi dichiarava assente una copertura strutturale, ma la stabilizzazione è in corso; al tempo stesso non esiste nel progetto un costo a regime riconciliato.
- **Evidenza:** il programma capitale umano/UPP ha un'allocazione superiore a 2,2 miliardi di euro e la documentazione 2026 registra migliaia di unità in servizio e un percorso di stabilizzazione. Perimetri e stime di costo ricorrente differiscono tra documenti.
- **Fonte:** [Ministero, capitale umano e UPP](https://www.giustizia.it/giustizia/it/contentview.page?contentId=ART421883); [Ministero, relazione PNRR](https://www.giustizia.it/cmsresources/cms/documents/pnrr_relazione_su_attuazione_interventi_mag2026.pdf).
- **Modifica suggerita:** indicare per profilo e sede numero effettivo, norma di copertura, costo lordo annuo, spazi, IT, formazione, turnover evitato e risultato marginale; non sommare stanziamenti con perimetri sovrapposti.
- **Incertezza:** il costo finale dipende da assunzioni effettive, inquadramenti, sedi e provvedimenti definitivamente vigenti.

## Confronto minimo tra Paesi comparabili

| Profilo | Francia | Germania | Spagna | Controevidenza utile |
|---|---|---|---|---|
| Pubblico ministero | Corpo giudiziario; direttive generali del Ministro, non individuali | Carriera distinta; soggezione alle istruzioni gerarchiche | Unità d'azione e dipendenza gerarchica; Procuratore generale proposto dal Governo | Separazione formale e indipendenza non sono sinonimi. |
| DT civile/commerciale di 1° grado, 2024 | 433,7 giorni | 232,2 giorni | 422,8 giorni | Nessun assetto di carriera spiega da solo l'efficienza. |
| CR di 1° grado, 2024 | 95,41% | 99,88% | 81,53% | DT, flusso e stock possono muoversi diversamente. |
| Problema recente | Arretrato e misure ADR/accesso contestate | Carichi penali e risorse; finanziamento di nuovi posti | Pendenze elevate e attuazione ADR disomogenea | Ogni modello ha costi e criticità; non esiste una copia pronta. |

Fonti: [Code de procédure pénale, art. 30](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000027753870); [GVG, §§ 146-147](https://www.gesetze-im-internet.de/englisch_gvg/englisch_gvg.html); [Constitución Española, art. 124](https://boe.es/buscar/act.php?id=BOE-A-1978-31229&p=20240217&tn=0); rapporti nazionali 2026 della [Commissione europea](https://commission.europa.eu/publications/2026-rule-law-report-communication-and-country-chapters_en); [01_GIUSTIZIA_FONTI](../01_RICERCA/01_GIUSTIZIA_FONTI.md).

## Effetti indesiderati da testare

| Misura | Possibile effetto indesiderato | Contromisura minima |
|---|---|---|
| Obiettivi quantitativi | chiusure facili, rinvii o spostamento dei casi complessi | indicatori bilanciati, audit del case mix e qualità |
| Priorità penali | diseguaglianza territoriale o pressione politica indiretta | criteri legali, pubblicità, motivazione, controllo e rimedi |
| Separazione delle carriere | dipendenza gerarchica del PM se le garanzie sono deboli | autonomia costituzionale, disciplina e nomine indipendenti |
| ADR obbligatoria | costi, ritardi e pressione sulle parti vulnerabili | patrocinio, recesso, cautelare, tempi e valutazione distributiva |
| Digitalizzazione | esclusione digitale, indisponibilità e vendor lock-in | assistenza, canale alternativo, interoperabilità e piano di uscita |
| AI giudiziaria | automazione del pregiudizio e opacità | uso limitato, supervisione reale, log, audit e contestazione |
| Open data | reidentificazione, ranking e gaming | aggregazione, soglie, minimizzazione e audit |
| Stabilizzazioni uniformi | personale dove serve meno, rigidità futura | fabbisogno per sede/profilo e revisione periodica |

## Costi e fattibilità

Il progetto non consente ancora una stima totale. Prima dell'approvazione, ogni misura deve indicare:

| Voce | Minimo richiesto |
|---|---|
| Personale | FTE per profilo e sede, retribuzione lorda, selezione, formazione, spazi e IT |
| Digitale | sviluppo/migrazione, licenze, interoperabilità, cybersecurity, assistenza, OPEX e dismissione legacy |
| ADR | tariffe, patrocinio, costo per accordo eseguito, abbandoni e contenzioso successivo |
| Dati/AI | protezione dati, audit, logging, monitoraggio, incident response e contenzioso |
| Governance | responsabile, dipendenze normative, tempi, procurement, baseline e clausola stop/go |

La fattibilità deve essere valutata per fasi e piloti; vedi [01_GIUSTIZIA](../05_PIANO_ATTUAZIONE/01_GIUSTIZIA.md). L'art. 81 Cost. richiede copertura delle nuove spese; gli artt. 101, 104 e 110 impongono di non trasformare la gestione in pressione sul contenuto delle decisioni.

## Registro delle affermazioni da eliminare o riscrivere

| Affermazione precedente | Azione | Nuova formulazione |
|---|---|---|
| «Il problema primario è il personale amministrativo» | **ELIMINARE** | Carenze multiple e cause da stimare per ufficio e materia. |
| «Tassi di smaltimento peggiori della Francia» | **RISCRIVERE** | Nel 2024 il CR di primo grado è quasi uguale; differiscono soprattutto DT e stock. |
| «Criteri annuali definiti dal Parlamento» come novità | **RISCRIVERE** | Descrivere prima legge n. 134/2021 e art. 3-bis disp. att. c.p.p. |
| «La separazione comporta assoggettamento all'esecutivo» | **RISCRIVERE** | È un rischio dipendente da status, nomine, disciplina e istruzioni. |
| «Mancanza di coperture strutturali» | **RISCRIVERE** | Stabilizzazione in corso; perimetro e costo a regime da riconciliare. |
| «A parità di risorse, Nord e Sud» | **ELIMINARE** | Nessuna parità dimostrata; usare uffici omogenei e dataset allegato. |
| «Introdurre il manager di tribunale» | **ELIMINARE** | Rafforzare la dirigenza amministrativa già esistente. |
| «Rendere pubbliche le performance» | **RISCRIVERE** | Migliorare dati già pubblici con standard, privacy, case mix e audit. |
| «L'ADR obbligatoria limita l'accesso» | **RISCRIVERE** | Il rischio dipende da costi, tempi e garanzie. |
| «Correlazione ampiamente dimostrata con gli investimenti» | **RISCRIVERE** | Associazione plausibile; effetto causale della misura non stimato. |

# CRITICITÀ BLOCCANTI

1. L'input-base è disponibile, ma non costituisce una proposta normativa completa: non è possibile certificare misure non specificate.
2. La precedente disciplina delle priorità penali è incompleta e deve essere allineata alla normativa vigente e alla Corte costituzionale n. 58/2026.
3. La parte sulla separazione delle carriere usa uno stato istituzionale superato dall'esito referendario del 2026.
4. La diagnosi causale centrata sul solo personale amministrativo non è provata.
5. Costi strutturali, unità stabilizzate e coperture non sono riconciliati.
6. Il confronto multi-modello è parziale: sono disponibili CODEX e GEMINI; manca una revisione Claude specifica sullo stesso input e l'arbitraggio umano.

# CRITICITÀ IMPORTANTI

1. Indicatori e anni erano imprecisi; il trend civile recente è meno lineare di quanto suggerito.
2. Court manager e open data erano presentati come novità pur esistendo già funzioni e dataset.
3. ADR, digitalizzazione e AI non consideravano adeguatamente accesso, privacy, resilienza e costi ricorrenti.
4. Il confronto internazionale non controllava per funzioni del personale, carichi, case mix e poteri ministeriali.
5. Mancavano metriche di qualità, equità e indipendenza accanto alla velocità.

# CORREZIONI MINORI

1. Definire sempre DT e CR e indicare anno, grado e materia.
2. Usare «tra i valori più elevati» invece di primati non verificati.
3. Non chiamare la somma dei DT «durata media».
4. Separare risorse assegnate, impegnate e pagate.
5. Conservare nomi ufficiali e anni nelle fonti anche se il branding è name-agnostic.

# PROPOSTE AGGIUNTIVE

1. Unità indipendente di valutazione con protocolli pubblicati prima dei risultati.
2. Rafforzamento della dirigenza amministrativa esistente con analisti di flusso e competenze digitali.
3. Cruscotto di resilienza digitale: incidenti, deroghe, uptime, ripristino e fallback.
4. Piloti ADR mirati con valutazione causale e distribuzionale.
5. Criteri organizzativi delle procure pubblici e motivati entro i limiti del segreto investigativo.
6. Clausole di revisione biennale e stop/go per software e riorganizzazioni.

# FONTI DA VERIFICARE

1. Dataset definitivo e attestazione finale dei target PNRR.
2. Numero effettivo di stabilizzazioni per profilo e sede, norma di copertura e costo a regime.
3. Costo medio, denominatore, abbandoni ed esecuzione degli accordi di mediazione.
4. Serie per ufficio normalizzata per case mix, arretrato storico e vacanze.
5. Stato completo della digitalizzazione penale, deroghe e incidenti.
6. Durata effettiva per coorti di fascicoli, non soltanto disposition time.
7. Costo totale di proprietà per AI, open data, audit e cybersecurity.

# PARTI CHE NON MODIFICHERESTI

1. L'idea che la durata dei processi sia un problema serio, purché non sia l'unico indicatore.
2. L'avvertenza che digitalizzazione e cybersecurity hanno costi ricorrenti.
3. La conclusione prudente che la separazione delle carriere non garantisce da sola efficienza o indipendenza.
4. La necessità di aggiornare periodicamente i dati e rendere trasparenti i criteri organizzativi.
5. L'attenzione alla continuità dell'Ufficio per il processo, subordinata a valutazione e copertura.
6. L'uso della comparazione internazionale come controllo delle ipotesi, non come prova causale o modello da copiare.
