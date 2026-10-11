---
title: "Documento completo"
tags:
  - l-italia-che-vorrei
  - pubblicazione
status: "BOZZA INTEGRATA"
versione: "v0.2"
data: "2026-10-11"
---

# L'Italia che vorrei — Documento completo

**Versione 0.3 — bozza integrata in revisione.** Struttura conforme a [00_REGOLA_PUBBLICAZIONE](00_REGOLA_PUBBLICAZIONE.md). Le sezioni economica e territoriale espongono dati verificati, ipotesi e lavoro mancante; non costituiscono una copertura finanziaria approvata.

Versione divulgativa: [Manifesto](01_MANIFESTO.md).
Dossier storico-causale: [Perché siamo arrivati qui](../01_RICERCA/03_PERCHE_SIAMO_ARRIVATI_QUI.md).

---

## 1. Executive summary

L'Italia presenta un insieme di problemi strutturali che si tengono l'uno con l'altro: produttività ferma dalla metà degli anni Novanta, salari reali nel 2024 sotto il livello del 1990, natalità al minimo dal dopoguerra, emigrazione netta di laureati, debito pubblico intorno al 138,6% del PIL. Nessuno di questi è isolabile: ciascuno è insieme causa ed effetto di un altro, e un intervento su un punto solo viene riassorbito dal sistema.

La diagnosi non è controversa e non è nuova. È condivisa da Banca d'Italia, Istat, Ufficio parlamentare di bilancio, OCSE e Corte dei conti, ed è nota da decenni. Il vincolo non è la conoscenza: è l'economia politica delle riforme, in cui i costi sono concentrati e immediati e i benefici diffusi e lontani, mentre l'orizzonte del decisore — circa 70 governi in 80 anni — è più corto del tempo di maturazione di qualunque riforma seria.

Da questa constatazione discende l'impostazione dell'intero documento. Il contenuto delle riforme proposte è largamente noto. La parte non ovvia, e l'unica su cui questo lavoro rivendica un contributo, è **la sequenza**: quali misure vengono prima perché producono risultati visibili a costo quasi nullo, quali condizioni misurate devono essere soddisfatte prima di passare alla fase successiva, e quali compensazioni rendono politicamente sostenibili le misure che hanno perdenti identificabili.

L'archivio contiene 83 proposte e 66 fatti con fonte e anno; 10 fatti restano da verificare su fonte puntuale. La parte maggioritaria del piano è attivabile con legge ordinaria o con la semplice attuazione di norme già vigenti; la parte che richiede legge costituzionale è minoritaria ed è collocata in fondo alla sequenza, non per prudenza ma per una lettura precisa dell'esito referendario del marzo 2026.

**Stato**: 83 proposte nel dataset `dati/proposte.json`, 66 fatti in `dati/fatti.json` (10 da verificare), 22 avvisi aperti al controllo del 2026-10-11. Una revisione umana qualificata non è ancora stata effettuata.

---

## 2. Problemi documentati

Diagnosi sintetica nel [Manifesto §2](01_MANIFESTO.md). Registro completo dei record con fonte, anno, tipo e proposte che li citano: [03_REGISTRO_FATTI](../03_VERIFICA/03_REGISTRO_FATTI.md).

I problemi documentati si raggruppano in cinque insiemi, ordinati per grado di consenso nella letteratura istituzionale.

**Insieme A — stagnazione della produttività e dei salari.** Produttività sostanzialmente ferma dalla metà degli anni Novanta (`F-ECO-05`); salari reali medi nel 2024 sotto il livello 1990 di 1,6 punti, a fronte di un +35% medio OCSE (`F-ECO-03`); nanismo d'impresa alimentato da soglie dimensionali fiscali e lavoristiche a 5, 15 e 50 addetti (`F-PARAD-02`); prezzo dell'energia industriale fra i più alti dell'Unione, indicato dall'OCSE come freno diretto alla competitività (`F-ECO-04`).

**Insieme B — demografia.** 355.000 nascite nel 2025, minimo dal dopoguerra (`F-DEMO-01`); saldo naturale a −296.000 ed età media a 49,1 anni contro 44,9 della media UE (`F-DEMO-02`); divario fra 760.000 figli desiderati e 355.000 nati, con il 62% che ha rinunciato per ostacoli economici e sociali e il 5,5% per scelta (`F-DEMO-03`); donne in età fertile scese da 14,3 a 11,5 milioni e in proiezione verso i 9 milioni al 2050 (`F-DEMO-06`); saldo dei laureati fra 25 e 34 anni a −21.000 in un anno (`F-DEMO-04`).

**Insieme C — fiscalità e capacità amministrativa.** Tax gap intorno ai 100 miliardi annui, con propensione all'evasione al 17% (`F-FISC-01`) e con un divario del 60% sul reddito da lavoro autonomo (`F-FISC-02`); complessità amministrativa e lentezza dei procedimenti indicate fra i freni diretti alla crescita e agli investimenti (`F-STATO-01`); asimmetria fra ricchezza netta delle famiglie fra le più alte d'Europa e debito pubblico fra i più alti al mondo (`F-PARAD-01`).

**Insieme D — architettura istituzionale.** Circa 70 governi in 80 anni con durata media poco superiore all'anno (`F-IST-01`); uso sistematico di decreti-legge, maxiemendamenti e voti di fiducia, con il requisito di omogeneità dell'art. 15 l. 400/1988 sistematicamente disatteso (`F-IST-02`); quattro sistemi elettorali dal 1993, due dichiarati incostituzionali (`F-IST-03`); competenze concorrenti del Titolo V, conflittualità Stato-Regioni e ventuno sistemi sanitari con esiti diseguali (`F-IST-04`); circa 7.900 comuni, molti sotto i 5.000 abitanti (`F-IST-05`); circa il 75% delle leggi della legislatura di iniziativa governativa (`F-IST-06`).

**Insieme E — regole della politica e partecipazione.** Autodichia delle Camere sul proprio trattamento economico e previdenziale (`F-POL-01`); obblighi di trasparenza che non coprono pienamente fondazioni e comitati (`F-POL-04`); assenza di una legge nazionale organica sulla rappresentanza di interessi (`F-POL-05`); quorum referendario raggiunto due volte su dieci consultazioni non costituzionali negli ultimi trent'anni (`F-REF-01`), con il caso del giugno 2025 in cui quattordici milioni di votanti non hanno prodotto effetti (`F-REF-02`).

**Controevidenze registrate.** Un documento che elenca solo ciò che peggiora non è un'analisi. NEET fra 15 e 29 anni al 13,3%, contro il 25,7% di dieci anni prima; abbandono scolastico all'8,2%, sotto la media UE del 9,1% (`F-LAV-01`). I target PNRR sul *disposition time* civile sono stati centrati, in parte grazie allo sprint della Cassazione che ha compensato i ritardi di primo e secondo grado: risultato reale, ma fragile perché ottenuto con misure straordinarie (`F-PNRR-02`). Le variabili di flusso si muovono; quelle di stock no.

---

## 3. Principi guida

Quattro principi di metodo, esposti per esteso nel [Manifesto §5](01_MANIFESTO.md): la sequenza conta più del contenuto; ogni fase si apre solo superando un gate misurato; ogni misura ha un rollback dichiarato in anticipo; ogni proposta dichiara chi ci perde.

A questi si aggiungono tre principi editoriali, che vincolano il documento e non il paese:

1. **Fatto, interpretazione, ipotesi e proposta restano distinti.** La diagnosi è verificabile, la proposta è opinabile. Confonderle è il modo più efficace di rendere entrambe inattaccabili e inutili.
2. **Le alternative incompatibili restano alternative.** Dove due leve non possono coesistere, l'archivio le tiene come varianti A e B con i rispettivi tradeoff e non sceglie. Una media fra due posizioni che nessuno sosterrebbe non è un compromesso: è un documento che ha smesso di dire qualcosa.
3. **Un numero senza fonte e anno non entra.** Il rischio specifico di un lavoro costruito con il contributo di più modelli di intelligenza artificiale è la statistica plausibile ma inventata, che sopravvive perché suona giusta e perché dopo un paio di passaggi nessuno sa più da dove venisse. Il flag di verifica e il controllo automatico sui documenti pubblici esistono per questo.

---

## 4. Proposte

83 proposte normalizzate. Ogni record porta: problema, leva (il meccanismo di incentivo, non l'etichetta), eventuale evidenza collegata, benchmark internazionale, oppositori identificati, KPI, fase, vincolo giuridico, classe di costo e — dove compilato — rischio e gate.

- Indice per ambito, con copertura di evidenza e KPI: [02_INDICE_PROPOSTE](../02_PROPOSTE/02_INDICE_PROPOSTE.md)
- Schede complete per ambito: [stato leggibile](../02_PROPOSTE/SCHEDE/stato-leggibile.md) · [fisco](../02_PROPOSTE/SCHEDE/fisco.md) · [produttività](../02_PROPOSTE/SCHEDE/produttivita.md) · [lavoro e capitale umano](../02_PROPOSTE/SCHEDE/lavoro-capitale-umano.md) · [demografia](../02_PROPOSTE/SCHEDE/demografia.md) · [istituzioni](../02_PROPOSTE/SCHEDE/istituzioni.md) · [sicurezza](../02_PROPOSTE/SCHEDE/sicurezza.md) · [immigrazione](../02_PROPOSTE/SCHEDE/immigrazione.md) · [costi della politica](../02_PROPOSTE/SCHEDE/costi-politica.md) · [presidenza della Repubblica](../02_PROPOSTE/SCHEDE/presidenza-repubblica.md) · [accountability degli eletti](../02_PROPOSTE/SCHEDE/accountability-eletti.md) · [limiti di mandato](../02_PROPOSTE/SCHEDE/limiti-di-mandato.md) · [senatori a vita](../02_PROPOSTE/SCHEDE/senatori-a-vita.md) · [democrazia diretta](../02_PROPOSTE/SCHEDE/democrazia-diretta.md) · [trasparenza parlamentare](../02_PROPOSTE/SCHEDE/trasparenza-parlamentare.md)

I sei pilastri in cui le proposte si organizzano sono descritti nel [Manifesto §6](01_MANIFESTO.md).

### Varianti aperte

Non risolte per scelta, non per indecisione.

| Ambito | Variante A | Variante B | Variante C |
|---|---|---|---|
| Presidenza della Repubblica | `P-QUIR-01`, `P-QUIR-02` — rafforzare la garanzia mantenendo l'elezione parlamentare: obbligo di motivazione pubblica degli atti, termini certi, divieto esplicito di secondo mandato | `P-QUIR-03` — elezione diretta in un quadro semipresidenziale organico | — |
| Senatori a vita | `P-SENV-01` — esclusione dal voto di fiducia, per legge o regolamento | `P-SENV-02` — mandato a termine non rinnovabile, per revisione costituzionale | `P-SENV-03` — la questione si scioglie nel superamento del bicameralismo paritario |

Scegliere fra queste è una posizione politica. Questo documento non la prende: espone i tradeoff e lascia la scelta a chi lo leggerà.

### Proposte che questo archivio considera fragili

Dichiarate perché l'autocritica non può essere delegata al lettore.

- Le proposte su **limiti di mandato**, **democrazia diretta** e **senatori a vita** sono complessivamente le più deboli sul piano dell'evidenza: quattordici proposte su temi contestati non hanno il campo `rischio` compilato, cioè non dichiarano l'obiezione più forte a sé stesse.
- Le proposte su **sicurezza** e **immigrazione** poggiano su un quadro normativo europeo entrato in vigore nel giugno 2026, quindi senza alcun dato di esito disponibile. Qualunque affermazione sulla loro efficacia oggi è una previsione, non una valutazione.
- Le proposte su **trasparenza parlamentare** incidono su materia coperta dall'autonomia regolamentare delle Camere: nessun governo può imporle. È un vincolo di fattibilità politica che nessun disegno tecnico aggira.

---

## 5. Analisi costituzionale

Classificazione completa per fonte del diritto necessaria: [02_MATRICE_VINCOLI](../04_COSTITUZIONE/02_MATRICE_VINCOLI.md). Schema di analisi per singola proposta: [00_SCHEMA_ANALISI_COSTITUZIONALE](../04_COSTITUZIONE/00_SCHEMA_ANALISI_COSTITUZIONALE.md).

**Il dato di struttura**: la larga maggioranza delle proposte è attivabile con legge ordinaria o con la sola attuazione di norme già vigenti. Le proposte che richiedono legge costituzionale sono una minoranza e sono concentrate in fase 3.

**Vincoli costituzionali espliciti già registrati nell'archivio.**

- **Art. 67 — divieto di mandato imperativo** (`F-ACC-01`). Esclude il *recall* dell'eletto senza revisione costituzionale. Qualunque proposta di revoca popolare a livello parlamentare deve passare da lì, e con essa il rischio di rendere l'eletto ricattabile da gruppi organizzati.
- **Art. 27 — presunzione di innocenza.** Estendere l'incandidabilità alle condanne non definitive attribuirebbe di fatto a un giudice di primo grado il potere di escludere un avversario politico dalla competizione. L'archivio sceglie la via opposta: processi rapidi più incandidabilità automatica su condanna definitiva, senza sconti (`F-ACC-03`).
- **Art. 75 — perimetro del referendum abrogativo** (`F-REF-04`). Materie tributarie e di bilancio, amnistia e ratifica dei trattati restano escluse. L'archivio non propone di toccarle, e aggiunge un limite di merito: i diritti fondamentali delle minoranze non vanno sottoposti a voto diretto. Una maggioranza del 51% non può decidere quali diritti spettino al 49%.
- **Art. 138 — procedura di revisione.** Doppia deliberazione e referendum eventuale senza quorum. È la ragione per cui la parte costituzionale del piano è collocata in fondo alla sequenza: nel marzo 2026 il referendum confermativo sulla giustizia è stato respinto e per circa il 31% degli elettori del No fu un voto contro il governo (`F-REF-06`). Una riforma istituzionale sottoposta al voto in un clima di sfiducia viene giudicata per il contesto, non per il merito.
- **Autodichia delle Camere** (`F-POL-01`). Materia coperta da autonomia costituzionale degli organi parlamentari: la modifica richiede l'intervento delle Camere stesse. È il nodo che rende reversibile qualunque riforma dei costi della politica.
- **Art. 120 — potere sostitutivo statale.** Fondamento del funzionamento dello sportello unico per gli investimenti nel quadro vigente, senza necessità di riforma del Titolo V (cfr. correzione C-03a in [06_REGISTRO_CORREZIONI](../03_VERIFICA/06_REGISTRO_CORREZIONI.md)).

**Vincolo europeo.** Le proposte su rimpatri e procedure di asilo si collocano all'interno del Patto europeo su migrazione e asilo, operativo dal 12 giugno 2026, e del regolamento rimpatri approvato dal Parlamento europeo il 17 giugno 2026 (`F-IMM-04`). Parte di quel quadro è contestata in sede giurisdizionale: un disegno che non metta in conto una revisione giudiziaria di alcune sue parti è un disegno inefficace, prima ancora che discutibile nel merito.

> [!warning] Limite di questa sezione
> È un'analisi di compatibilità formale condotta sui record dell'archivio, non un parere costituzionale. Le proposte che incidono su materia costituzionale richiedono la revisione di un costituzionalista prima di qualunque uso pubblico. Non è stata effettuata.

---

## 6. Analisi economica e coperture finanziarie

> [!warning] Stato della sezione: da quantificare
> Non esiste ancora un quadro pluriennale di costi, gettito netto e coperture per il pacchetto. I risparmi indicati nel contributo Gemini erano ipotesi senza un calcolo riproducibile, non risorse disponibili.

Il debito e la crescita economica limitano le scelte di bilancio, ma le cifre su interessi, pensioni e istruzione devono essere ricostruite con anno e perimetro omogenei prima di un confronto (stime su pensioni e interessi ancora da verificare). Anche una misura a costo amministrativo basso può avere costi di attuazione per gli enti locali.

Il [Rapporto MEF 2023](https://www.mef.gov.it/export/sites/MEF/documenti-allegati/2023/Rapporto-spese-fiscali-2023.pdf) censisce 625 spese fiscali, 555 vigenti nel 2024, e stima circa 96,3 miliardi di effetti per le 411 quantificabili nel 2024 (`F-FISC-03`). Questa è una stima di mancato gettito, non la somma che si recupererebbe abolendole. `P-FISC-02` chiede una revisione misura per misura, con beneficiari, effetti e costo della transizione; `P-FISC-01` può essere finanziata solo dopo una stima netta certificata e l'effettiva decisione di bilancio.

`P-FISC-08-GEM` propone valutazioni periodiche dei programmi di spesa, con decisione parlamentare motivata. Non assume 8 miliardi di risparmio né una soppressione automatica dei sussidi. Il recupero di gettito da contrasto all'evasione va contato soltanto a consuntivo, distinguendo entrate una tantum da entrate ricorrenti.

**Lavoro necessario:** quantificare spesa iniziale e ricorrente per nidi, assistenza domiciliare, formazione e capacità amministrativa; produrre tre scenari e il loro impatto su redditi, territori, debito e servizi; ottenere una verifica indipendente prima di dichiarare una copertura.

---

## 7. Impatti sociali e territoriali

> [!warning] Stato della sezione: parziale
> Due indicatori territoriali sono stati corretti su fonti primarie; manca una valutazione distributiva completa delle proposte.

Nel [monitoraggio LEA 2024](https://www.salute.gov.it/new/it/news-e-media/notizie/livelli-essenziali-di-assistenza-sintesi-dei-risultati-del-nuovo-sistema-di-0/) Calabria, Sicilia e Provincia autonoma di Bolzano non raggiungono la soglia in almeno una delle tre macro-aree (`F-SAN-01`). Il dato non misura da solo le cause dei divari. La stima del precedente testo di un saldo netto sanitario di 4,2 miliardi dal Sud al Nord non è confermata e resta fuori dalla diagnosi pubblica.

Per i servizi educativi 0-2 anni, [Istat](https://www.istat.it/comunicato-stampa/offerta-di-nidi-e-servizi-integrativi-per-la-prima-infanzia-anno-educativo-2023-2024/) registra 31,6 posti autorizzati ogni 100 bambini residenti nel 2023/24, con 19,0 nel Sud e 19,5 nelle Isole (`F-DEMO-08`). Il LEP vigente è 33 posti ogni 100 bambini entro il 2027 a livello locale. La proposta sui nidi (`P-DEMO-01`) deve indicare quanto costerebbe ampliarlo, dove e con quali risorse per personale e gestione.

La proposta istituzionale `P-IST-04` richiederebbe revisione costituzionale per la nuova clausola di supremazia; l'art. 120 già offre poteri sostitutivi in alcuni casi. Rafforzare assistenza domiciliare e coordinamento del Fondo per le non autosufficienze esistente (`P-DEMO-08-GEM`) richiede una ricognizione dei bisogni, degli operatori e dei bilanci. Per ogni misura vanno pubblicati esiti disaggregati per regione, reddito, età, disabilità e accesso ai servizi, nel rispetto della privacy.

---

## 8. Piano di attuazione

Sequenza completa con fasi, catene di dipendenza e gate: [02_SEQUENZA_FASI](../05_PIANO_ATTUAZIONE/02_SEQUENZA_FASI.md). Quadro sintetico nel [Manifesto §7](01_MANIFESTO.md).

**Distribuzione delle proposte:** consultare [la sequenza generata](../05_PIANO_ATTUAZIONE/02_SEQUENZA_FASI.md) per i conteggi aggiornati; l'integrazione ha accorpato proposte duplicate.

**Tre gate strutturali** separano le fasi:

| Da | A | Condizione di passaggio | Cosa si fa se non passa |
|---|---|---|---|
| 0 | 1 | Tempi mediani dei tre permessi più richiesti dimezzati | Il vincolo non è normativo ma di capacità: si rinforza la fase 1 e non si procede |
| 1 | 2 | Tasso di ricollocazione dei centri per l'impiego sopra soglia | **Il pacchetto lavoro non si apre.** Flessibilità in uscita senza politiche attive funzionanti produce precarietà, non flexicurity |
| 2 | 3 | Gettito da recupero evasione sopra target | Il taglio del cuneo non si estende: la copertura dev'essere reale, non stimata |

> [!warning] Il gate è oggi un'affermazione narrativa, non un dato
> Il numero di gate formalizzati è riportato nel dataset e va verificato a ogni aggiornamento. Le tre condizioni della tabella sopra derivano dai documenti di analisi, non da record strutturati, e nessuna ha una soglia numerica associata. Finché restano così, i gate non sono verificabili — e un gate non verificabile non è un gate, è un'intenzione. È la lacuna prioritaria dichiarata in [06_REGISTRO_CORREZIONI](../03_VERIFICA/06_REGISTRO_CORREZIONI.md) (N-05).

**Vincolo temporale esogeno.** La chiusura del PNRR è fissata al 31 agosto 2026 per milestone e rendicontazione e al 31 dicembre 2026 per i pagamenti finali, con circa l'85% delle risorse erogate ma una spesa effettiva molto più indietro (`F-PNRR-01`). Il 2027 è il primo anno senza stimolo e senza vincolo esterno. Qualunque piano che assuma implicitamente la persistenza della condizionalità europea come motore del ritmo riformatore sta assumendo una cosa che sta per finire.

---

## 9. KPI e meccanismi di revisione

**Stato degli indicatori**: 69 proposte su 83 contengono un numero nel campo KPI, ma molte soglie non hanno una baseline documentata; 10 proposte hanno un gate. La quantificazione resta aperta. Elenco completo e analisi: [05_KPI_DA_QUANTIFICARE](../03_VERIFICA/05_KPI_DA_QUANTIFICARE.md).

La regola del progetto è che un giudizio si tiene solo se è falsificabile, cioè se ha una soglia e una data. Allo stato, la maggior parte delle proposte non lo è: sono direzioni di marcia, non impegni verificabili. La differenza non è formale — è esattamente ciò che separa un piano da un programma elettorale.

**Nessuna soglia è stata inventata per far tornare le tabelle.** Una soglia senza baseline documentata è peggio di una casella vuota: ha l'aspetto di una misura e non lo è, e sopravvive nei documenti derivati molto più a lungo di un vuoto dichiarato.

**Meccanismi di revisione previsti.**

1. **Clausola di valutazione a 24 mesi** su ogni misura, con soglia di fallimento scritta prima dell'attivazione.
2. **Rollback automatico**: se un intervento peggiora l'indicatore che doveva migliorare, si ritira. La difficoltà non è tecnica, è politica: ritirare una misura è un'ammissione pubblica di errore, e per questo in Italia le misure fallite vengono quasi sempre stratificate invece che rimosse.
3. **Cruscotto pubblico** con baseline, responsabile nominativo e data per ogni misura. È il lascito più utile del monitoraggio PNRR, e la domanda operativa è se sopravviva alla fine del programma.
4. **Revisione del dataset**: ogni contributo esterno passa dal [protocollo di merge](../PROTOCOLLO_MERGE.md); ogni correzione è registrata in [06_REGISTRO_CORREZIONI](../03_VERIFICA/06_REGISTRO_CORREZIONI.md); `strumenti/valida.py` è eseguito a ogni modifica e blocca gli errori strutturali.

---

## 10. Fonti e metodologia

**Fonti primarie.** Istat (bilancio demografico 2025; report su giovani e migrazioni, maggio 2026); Banca d'Italia (Relazione annuale, maggio 2026; statistiche di finanza pubblica); MEF (Documento di finanza pubblica 2026; Relazione sull'economia non osservata e sull'evasione); Ufficio parlamentare di bilancio; Corte costituzionale; Camera dei deputati e Senato; Ministero della Giustizia; Ministero dell'Interno; Parlamento europeo e Commissione europea; Gazzetta Ufficiale e Normattiva.

**Fonti internazionali.** OCSE (*Economic Survey: Italy 2026*); FMI (*World Economic Outlook* e *Fiscal Monitor*, aprile 2026); Eurostat.

**Fonti secondarie**, usate solo dove citano esplicitamente una primaria: Centro Studi Confindustria, Osservatorio sui Conti Pubblici Italiani, Openpolis/Openparlamento, YouTrend, Pagella Politica.

**Metodologia.** Il contenuto è normalizzato in unità atomiche — `proposta` e `fatto` — con identificativi stabili, così che il confronto fra contributi di autori diversi sia un'operazione su record verificabile da uno script, invece di un lavoro di editing a sensibilità. Tre tipi di contenuto, tre regole di conflitto:

| Tipo | Dove vive | Regola in caso di conflitto |
|---|---|---|
| Fatti | `dati/fatti.json` | Vince la fonte primaria più recente. Un numero senza fonte verificabile esce dal dataset |
| Proposte | `dati/proposte.json` | Raramente in vero conflitto. Se lo sono, si conservano come varianti A/B: non si sceglie |
| Narrativa | `06_PUBBLICAZIONE/` | Generata a valle. Non è mai la fonte di verità |

Il protocollo completo è in [PROTOCOLLO_MERGE](../PROTOCOLLO_MERGE.md). Lo schema di interscambio è in `dati/schema/l-italia-che-vorrei.schema.json`.

**Limiti dichiarati del metodo.**

- Il dataset è stato costruito in larga parte con il contributo di modelli di intelligenza artificiale. Il rischio specifico è la statistica plausibile ma inventata. Le contromisure sono il flag `verificato`, il divieto automatico di citare fatti non verificati nei documenti pubblici e la tracciabilità dei contributi nel registro editoriale. Sono contromisure parziali: non sostituiscono la verifica umana.
- **Il consenso fra modelli non è una prova.** Tre modelli che concordano possono condividere la stessa fonte errata o lo stesso bias di addestramento. L'arbitraggio previsto dal materiale di lavoro non pubblicato non è per maggioranza: una modifica entra perché è meglio documentata, non perché è più votata.
- Il benchmark internazionale non importa risultati, importa **meccanismi di incentivo**. Un meccanismo trapiantato senza la sua infrastruttura amministrativa produce spesso l'effetto opposto a quello voluto.

---

## 11. Registro delle principali obiezioni

Obiezioni serie, riportate con la loro forza reale e non in versione indebolita. Le prime cinque riguardano il merito, le ultime tre il documento stesso.

**O-1 — "Tutto questo è già stato scritto."** Vero, e dichiarato. La diagnosi è nota da trent'anni e ogni governo ne ha promesso pezzi. Se il vincolo fosse la conoscenza, sarebbe già risolto. La risposta di questo lavoro è che il vincolo è l'economia politica, e che la parte non ovvia sono sequenza e compensazioni. Resta vero che un documento in più non cambia quel vincolo.

**O-2 — Il rischio di austerità autolesionista.** Consolidare tagliando investimenti con un debito a quel livello deprime la crescita e può peggiorare il rapporto. Obiezione forte, sostenuta da una parte non piccola degli economisti. La risposta sulla composizione della spesa è parziale e non chiude la questione.

**O-3 — Il rischio opposto: senza vincolo esterno non si fa nulla.** Con la fine del PNRR scompare la condizionalità che ha prodotto i risultati migliori. Questo piano non contiene uno strumento per sostituirla.

**O-4 — La demografia potrebbe essere irreversibile.** Il numero di madri potenziali è già determinato (`F-DEMO-06`). Nessuna politica per la natalità può da sola evitare il calo della forza lavoro nei prossimi venticinque anni. Le tre uscite possibili — economia più piccola, maggiore produttività per persona, immigrazione — non si escludono e realisticamente servono tutte.

**O-5 — Il rischio tecnocratico.** Un piano così articolato presuppone che chi lo scrive sappia. La storia delle riforme insegna il contrario. Da qui la sperimentazione locale e le clausole di rollback, che però sono anch'esse una risposta di disegno a un problema di disegno.

**O-6 — Più democrazia diretta non equivale a più potere ai cittadini.** Dove il finanziamento delle campagne referendarie non è regolato, l'iniziativa popolare diventa lo strumento di chi può pagarla. È la ragione per cui l'archivio colloca i tetti di spesa come precondizione del referendum propositivo e non come suo complemento (correzione C-03b).

**O-7 — I limiti di mandato possono spostare il potere invece di redistribuirlo.** Se si limitano gli eletti senza professionalizzare e rendere trasparente ciò che resta — uffici legislativi, dirigenza pubblica, rappresentanza di interessi — il potere passa a chi non è mai sulla scheda elettorale. È il modo in cui i sistemi con *term limits* falliscono più spesso.

**O-8 — Questo documento è sbilanciato.** Possibile, ed è una domanda che non può essere risolta da chi lo ha scritto. Gli elementi per giudicare: la sezione sui settori protetti e sul catasto è sfavorevole a rendite e patrimonio immobiliare; quella su pensioni e automatismi demografici è sfavorevole alle coorti prossime alla pensione; quella su immigrazione tiene insieme espulsione effettiva dei condannati e ampliamento dei canali legali di ingresso, posizione che scontenta entrambi i fronti del dibattito; sulle riforme istituzionali il documento preferisce il superamento del bicameralismo al premierato, che è una scelta politica dichiarata. Chi ritiene che vi sia uno sbilanciamento sistematico è invitato a indicarlo sul record, con il codice della proposta.

---

### Chiusura

Questo documento è anonimo, non affiliato, non finanziato e non conclusivo. Nessuna proposta è approvata; l'approvazione è una decisione editoriale umana e non coincide con il consenso fra modelli.

Modalità di contestazione: [Manifesto §10](01_MANIFESTO.md).

**L'Italia che vorrei** · versione 0.1 · 20 settembre 2026
