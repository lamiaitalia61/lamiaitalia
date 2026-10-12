---
title: "Sequenza di attuazione per fasi"
tags:
  - l-italia-che-vorrei
  - attuazione
  - sequenza
status: "GENERATO"
sorgente: "dati/proposte.json"
---

# Sequenza di attuazione per fasi

> [!warning] File generato
> Prodotto da `strumenti/genera.py` da `dati/proposte.json`. Non modificare a mano: le modifiche vanno fatte sul dataset e rigenerate.

La sequenza e' la variabile piu' importante del piano: le riforme che chiedono sacrifici vengono dopo quelle che producono risultati visibili, altrimenti il consenso finisce prima del beneficio. Ogni fase si chiude con un gate: se il gate non passa, non si procede alla fase successiva.


## Fase 0 — credibilita' (primi 12 mesi) — 11 proposte

| ID | Ambito | Leva | Costo | Prerequisiti | Gate |
|---|---|---|---|---|---|
| `P-ACC-03` | accountability-eletti | Scheda di valutazione istituzionale pubblica e standardizzata per ogni carica: presenze in aula e commissione, voti, atti, incarichi, patrimonio, finanziamenti | basso | — | — |
| `P-FISC-06` | fisco | Divieto di condono per legge rinforzata per un decennio | nullo | — | — |
| `P-FISC-08-GEM` | fisco | Rafforzare la valutazione periodica indipendente dei programmi di spesa e dei sussidi, con dati pubblici, analisi distributiva e decisione parlamentare su conferma, modifica o chiusura | medio | — | Mandato e risorse per valutatori indipendenti; confronto con Ragioneria, UPB e Parlamento senza attribuire all UPB poteri decisionali automatici |
| `P-GIU-01-CLA` | giustizia | Pubblicare per ufficio durata, arretrato, clearance rate e risorse con definizioni omogenee; sperimentare miglioramenti organizzativi e valutarli. | basso | — | Definizioni statistiche condivise, tutela dei dati dei procedimenti e confronto dei carichi per complessita. |
| `P-PROD-02` | produttivita | Sportello unico nazionale investimenti con potere sostitutivo e termine certo | basso | — | — |
| `P-SIC-05` | sicurezza | Militari solo su obiettivi fissi e in emergenza dichiarata a termine, con obiettivo esplicito di liberare agenti per l'investigazione | nullo (risparmio) | — | — |
| `P-STATO-01` | stato-leggibile | Principio once-only reso obbligo giuridico, atto annullabile se violato | trascurabile | — | — |
| `P-STATO-02` | stato-leggibile | Sunset clause a 5 anni su norme amministrative, salvo riconferma motivata con dati | nullo | — | — |
| `P-STATO-04` | stato-leggibile | Certificazione automatica rilasciata dal sistema allo scadere del termine | basso | — | — |
| `P-STATO-05` | stato-leggibile | Riforma responsabilita' erariale: distinzione netta dolo / colpa lieve | nullo | — | — |
| `P-TRASP-04` | trasparenza-parlamentare | Obbligo di legge: ogni voto, presenza, emendamento e incarico in formato aperto con API pubblica istituzionale | basso | — | — |

## Fase 1 — capacita' (1-3 anni) — 28 proposte

| ID | Ambito | Leva | Costo | Prerequisiti | Gate |
|---|---|---|---|---|---|
| `P-ACC-05` | accountability-eletti | Automazione e trasparenza dei criteri: togliere la merce di scambio invece di punire lo scambio | medio | P-STATO-01, P-STATO-04 | — |
| `P-DEMDIR-04` | democrazia-diretta | Obbligo di linguaggio piano + libretto informativo a ogni elettore con testo, effetti e argomenti pro/contro verificati da organismo terzo | basso | — | — |
| `P-DEMO-01` | demografia | Nidi 0-3 a copertura universale, costo marginale vicino a zero dal secondo figlio | alto | — | — |
| `P-DEMO-02` | demografia | Tempo pieno reale su tutto il territorio | alto | — | — |
| `P-DEMO-03` | demografia | Piano nazionale affitto accessibile under 35 e riuso del patrimonio pubblico inutilizzato | alto | — | — |
| `P-DEMO-04` | demografia | Assegno unico stabilizzato e indicizzato per legge pluriennale | medio | — | — |
| `P-FISC-05` | fisco | Compliance by design: precompilazione totale, incroci in tempo reale, algoritmi di rischio pubblicati | medio | — | — |
| `P-IMM-01` | immigrazione | Accordi di riammissione come priorita' di politica estera, con condizionalita' su visti, aiuti e commercio, negoziati a livello UE | medio | — | — |
| `P-IMM-02` | immigrazione | Ufficio dedicato che segue il caso dalla sentenza all'esecuzione materiale | basso | — | — |
| `P-IMM-04` | immigrazione | Identificazione biometrica all'ingresso e termini certi per la decisione | medio | — | — |
| `P-IST-05` | istituzioni | Gestioni associate obbligatorie sotto soglia per appalti, progettazione, digitale (non fusioni forzate) | basso | — | — |
| `P-IST-06` | istituzioni | Reclutamento rapido per competenze + valutazione con conseguenze reali + retribuzione competitiva su poche centinaia di ruoli tecnici strategici | medio | — | — |
| `P-LAV-01` | lavoro-capitale-umano | Sistema duale su scala tedesca: ITS a 200.000 studenti, imprese coinvolte per obbligo o contributo | alto | — | — |
| `P-LAV-03` | lavoro-capitale-umano | Presa in carico entro 30 giorni, budget formativo trasferibile alla persona, valutazione sui tassi di ricollocazione | alto | — | — |
| `P-LAV-06-GEM` | lavoro-capitale-umano | Collegare i percorsi di riqualificazione alla NASpI con offerta formativa verificata e tutoraggio; applicare eventuale condizionalita solo dopo una offerta effettivamente accessibile e congrua | medio | — | Disponibilita territoriale dei corsi, accomodamenti per disabilita e cura, ricorso contro le sanzioni e valutazione degli effetti |
| `P-POL-03` | costi-politica | Obbligo di tracciamento per chiunque finanzi attivita' politica sopra soglia bassa; registro unico nazionale in formato aperto e in tempo reale | basso | — | — |
| `P-POL-04` | costi-politica | Registro obbligatorio dei rappresentanti di interessi + agenda pubblica degli incontri dei decisori | basso | — | — |
| `P-POL-07-GEM` | costi-politica | Definire obblighi proporzionati di dichiarazione, astensione e gestione indipendente delle partecipazioni rilevanti per titolari di cariche esecutive, con vigilanza e sanzioni soggette a ricorso | basso | — | Valutazione costituzionale, tutela dei dati personali e dell impresa; soglie di rilevanza e autorita competente da definire |
| `P-PROD-03` | produttivita | Semplificazione autorizzativa rinnovabili + accumuli + scelta esplicita e documentata sul nucleare di nuova generazione | alto | — | — |
| `P-SAN-01-CLA` | sanita | Integrare in un agenda verificabile l offerta pubblica e convenzionata; pubblicare tempi per prestazione e area, e pianificare organici per le strutture territoriali. | alto | — | Misurazione omogenea delle liste, piano del personale, accordi regionali e copertura pluriennale verificata. |
| `P-SIC-01` | sicurezza | Una specialita' = una forza, per legge, con termine di attuazione vincolante e compensazione tra corpi | nullo | — | — |
| `P-SIC-02` | sicurezza | Piano nazionale di gravitazione territoriale con scadenza a 5 anni; risorse liberate alla polizia giudiziaria | nullo | — | — |
| `P-SIC-03` | sicurezza | Banca dati unica interoperabile con accesso profilato alla polizia locale | medio | — | — |
| `P-STATO-03` | stato-leggibile | Codice unico per materia con testo consolidato digitale a valore legale | basso | — | — |
| `P-STATO-06` | stato-leggibile | AIR obbligatoria e pubblica + regola one-in-two-out sugli oneri | basso | — | — |
| `P-STATO-07-GEM` | stato-leggibile | Sperimentare la riduzione dei soli visti amministrativi duplicativi, con tracciabilita degli atti e audit successivi basati sul rischio; conservare il controllo preventivo della Corte dei conti previsto dall art. 100 Cost. | basso | — | Mappatura dei visti modificabili con legge ordinaria, parere della Corte dei conti e baseline dei procedimenti |
| `P-STATO-10-CLA` | stato-leggibile | Progettare i servizi essenziali end-to-end e garantire un canale assistito equivalente; pubblicare prove di usabilita e tempi per canale. | medio | — | Test con utenti vulnerabili, accessibilita, costi del canale assistito e tutela dati personali verificati. |
| `P-STATO-11-CLA` | stato-leggibile | Creare uno sportello interoperabile che mostri i benefici potenzialmente spettanti e precompili, previo controllo della persona, le domande; garantire verifica umana e ricorso. | medio | — | Mappatura dei benefici, basi giuridiche degli scambi dati, valutazione privacy e prova pilota con ricorso accessibile. |

## Fase 2 — scambio (3-6 anni) — 26 proposte

| ID | Ambito | Leva | Costo | Prerequisiti | Gate |
|---|---|---|---|---|---|
| `P-ACC-02` | accountability-eletti | Primarie regolate per legge con albo degli elettori e controlli | basso | — | — |
| `P-ACC-04` | accountability-eletti | Decurtazioni progressive automatiche e decadenza oltre soglia di assenze ingiustificate | nullo | — | — |
| `P-ACC-06` | accountability-eletti | Mantenere l'incandidabilita' alla condanna definitiva (legge Severino) e agire sui tempi del processo | nullo | — | — |
| `P-DEMDIR-03` | democrazia-diretta | Election day referendario fisso per legge, una data annuale prestabilita | nullo (risparmio) | — | — |
| `P-DEMDIR-05` | democrazia-diretta | Giuria di cittadini estratti a sorte che audisce esperti e pubblica un documento sintetico neutrale prima del voto | basso | — | — |
| `P-DEMDIR-06` | democrazia-diretta | Tetti di spesa e trasparenza totale sui finanziamenti delle campagne referendarie | basso | — | — |
| `P-DEMO-08-GEM` | demografia | Rafforzare e coordinare il Fondo per le non autosufficienze gia esistente con ADI e servizi sociali comunali, definendo criteri di accesso e continuita assistenziale | alto | — | Ricognizione delle risorse attuali, fabbisogni territoriali e valutazione degli effetti sulle famiglie e sul personale di cura |
| `P-FISC-01` | fisco | Riduzione strutturale del cuneo, finanziata non a debito | alto | P-FISC-02, P-FISC-03, P-FISC-05 | — |
| `P-FISC-02` | fisco | Revisione sistematica con soppressione automatica delle inefficaci | nullo (genera gettito) | — | — |
| `P-FISC-03` | fisco | Riordino catastale a invarianza di gettito, contestuale al taglio del cuneo | nullo (neutro) | — | — |
| `P-FISC-04` | fisco | Sostituzione degli scalini con transizione continua degli oneri | medio | — | — |
| `P-IMM-03` | immigrazione | Ingressi legali per lavoro dimensionati sul fabbisogno certificato | basso | — | — |
| `P-LAV-02` | lavoro-capitale-umano | Contratto unico a tutele crescenti con costo di uscita crescente e prevedibile | medio | P-LAV-03 | Attivabile solo dopo verifica dei tassi di ricollocazione dei CPI |
| `P-LAV-04` | lavoro-capitale-umano | Soglia minima agganciata ai CCNL piu' rappresentativi + detassazione premi di produttivita' | medio | — | — |
| `P-LAV-05` | lavoro-capitale-umano | Leve non fiscali: carriere per merito, laboratori finanziati, casa accessibile nelle citta' universitarie | alto | — | — |
| `P-POL-01` | costi-politica | Autorita' indipendente esterna che fissa indennita' di tutte le cariche elettive su parametro oggettivo automatico | nullo | — | — |
| `P-POL-02` | costi-politica | Indennita' unica uguale per tutti + rimborsi a pie' di lista documentati e pubblicati + continuita' contributiva per il periodo di mandato | nullo | — | — |
| `P-POL-05` | costi-politica | Cooling-off period obbligatorio tra incarico pubblico e assunzione nel settore regolato | nullo | — | — |
| `P-PROD-01` | produttivita | Condizionalita' a crescita misurata + valutazione d'impatto pubblica + soppressione automatica | nullo | — | — |
| `P-PROD-04` | produttivita | Apertura concorrenziale con transizione lunga e indennizzi | medio | — | — |
| `P-SENV-01` | senatori-a-vita | Esclusione dei senatori a vita dal voto di fiducia, mantenendo parola, iniziativa e voto sulle leggi | nullo | — | — |
| `P-SIC-04` | sicurezza | Comparto sicurezza unico con mobilita' tra forze, mantenendo il dualismo democratico PS/CC | medio | — | — |
| `P-TRASP-01` | trasparenza-parlamentare | Divieto di emendamenti sostitutivi dell'intero articolato; tempi minimi tra deposito e voto | nullo | — | — |
| `P-TRASP-02` | trasparenza-parlamentare | Stralcio automatico delle disposizioni estranee, con rilievo formale in sede di emanazione | nullo | — | — |
| `P-TRASP-03` | trasparenza-parlamentare | Limitazione ai casi su persone e diritti della persona; tracciatura di tutto il resto | nullo | — | — |
| `P-TRASP-06` | trasparenza-parlamentare | Quote garantite di calendario per l'iniziativa parlamentare e per l'opposizione, con obbligo di voto finale | nullo | — | — |

## Fase 3 — struttura (4-8 anni) — 18 proposte

| ID | Ambito | Leva | Costo | Prerequisiti | Gate |
|---|---|---|---|---|---|
| `P-ACC-01` | accountability-eletti | Collegi uninominali o liste molto corte in collegi piccoli | nullo | — | — |
| `P-DEMDIR-01` | democrazia-diretta | Sostituzione con quorum di approvazione (Si' sopra il 25-33% dell'elettorato), indipendente dall'affluenza | nullo | — | — |
| `P-DEMDIR-02` | democrazia-diretta | Referendum propositivo: firme rafforzate, termine al Parlamento, controllo preventivo di costituzionalita' e obbligo di copertura | basso | P-DEMDIR-06 | — |
| `P-DEMO-05` | demografia | Ripristino pieno di eta' e coefficienti automatici, con eccezioni documentate per lavori gravosi e vincolo di destinazione dei risparmi a scuola/natalita'/ricerca | nullo (genera risparmi) | — | — |
| `P-DEMO-06` | demografia | Programmazione pluriennale dell'immigrazione per fabbisogno, con corridoi legali e riconoscimento rapido dei titoli | medio | — | — |
| `P-IST-01` | istituzioni | Una sola camera legislativa; seconda camera di rappresentanza territoriale senza rapporto fiduciario | nullo | — | — |
| `P-IST-02` | istituzioni | Limiti stringenti alla decretazione d'urgenza in cambio di corsie preferenziali garantite per i ddl del governo | nullo | — | — |
| `P-IST-03` | istituzioni | Costituzionalizzazione dei principi (soglia, premio, preferenze) | nullo | — | — |
| `P-IST-04` | istituzioni | Clausola di supremazia su infrastrutture ed energia; LEP finanziati prima di ogni ulteriore differenziazione | alto | — | — |
| `P-MAND-01` | limiti-di-mandato | Estensione dei limiti: 3 legislature per i parlamentari, 2 mandati pieni per il Presidente del Consiglio | nullo | — | — |
| `P-MAND-02` | limiti-di-mandato | Tetto cumulativo 12-15 anni per carica, con conteggio che segue la persona | nullo | — | — |
| `P-MAND-03` | limiti-di-mandato | Contrappeso obbligatorio: uffici legislativi professionalizzati, dirigenza valutata, registro lobby | medio | P-POL-04 | — |
| `P-QUIR-01` | presidenza-repubblica | Obbligo di motivazione pubblica per il rifiuto di emanazione e per il rinvio; termini certi | nullo | — | — |
| `P-QUIR-02` | presidenza-repubblica | Divieto costituzionale esplicito di secondo mandato | nullo | — | — |
| `P-QUIR-03` | presidenza-repubblica | Elezione diretta in quadro semipresidenziale organico | nullo | — | — |
| `P-SENV-02` | senatori-a-vita | Mandato a termine non rinnovabile (7-9 anni) al posto del seggio a vita | nullo | — | — |
| `P-SENV-03` | senatori-a-vita | Assorbimento nella seconda camera senza rapporto fiduciario: il problema democratico si scioglie da se' | nullo | P-IST-01 | — |
| `P-TRASP-05` | trasparenza-parlamentare | Sindacabilita' dei regolamenti parlamentari come ogni altra fonte | nullo | — | — |

## Catene di dipendenza bloccanti

- `P-STATO-01` (fase 0) deve precedere `P-ACC-05` (fase 1) — Automazione e trasparenza dei criteri: togliere la merce di scambio invece di punire lo scambio
- `P-STATO-04` (fase 0) deve precedere `P-ACC-05` (fase 1) — Automazione e trasparenza dei criteri: togliere la merce di scambio invece di punire lo scambio
- `P-FISC-02` (fase 2) deve precedere `P-FISC-01` (fase 2) — Riduzione strutturale del cuneo, finanziata non a debito
- `P-FISC-03` (fase 2) deve precedere `P-FISC-01` (fase 2) — Riduzione strutturale del cuneo, finanziata non a debito
- `P-FISC-05` (fase 1) deve precedere `P-FISC-01` (fase 2) — Riduzione strutturale del cuneo, finanziata non a debito
- `P-LAV-03` (fase 1) deve precedere `P-LAV-02` (fase 2) — Contratto unico a tutele crescenti con costo di uscita crescente e prevedibile
- `P-DEMDIR-06` (fase 2) deve precedere `P-DEMDIR-02` (fase 3) — Referendum propositivo: firme rafforzate, termine al Parlamento, controllo preventivo di costituzionalita' e obbligo di copertura
- `P-POL-04` (fase 1) deve precedere `P-MAND-03` (fase 3) — Contrappeso obbligatorio: uffici legislativi professionalizzati, dirigenza valutata, registro lobby
- `P-IST-01` (fase 3) deve precedere `P-SENV-03` (fase 3) — Assorbimento nella seconda camera senza rapporto fiduciario: il problema democratico si scioglie da se'

## Relazioni non bloccanti

- `P-PROD-02` e' rafforzata da P-IST-04, ma e' attivabile da sola
- `P-TRASP-02` e' rafforzata da P-QUIR-01, ma e' attivabile da sola

> [!warning] Distinzione che il validatore fa rispettare
> `dipende_da` e' un prerequisito bloccante e non puo' puntare a una fase successiva. `rafforzata_da` e' un rafforzativo e non vincola la sequenza. Confondere i due produce piani in cui tutto dipende da una riforma costituzionale che non arriva mai.
