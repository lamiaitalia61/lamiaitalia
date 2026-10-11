---
title: "Manifesto"
tags:
  - l-italia-che-vorrei
  - pubblicazione
  - manifesto
status: "BOZZA"
versione: "v0.3"
data: "2026-10-11"
---

# L'Italia che vorrei — Manifesto

**Versione 0.3 — bozza editoriale in revisione.** Il testo non indica l'autore; ciò non garantisce l'anonimato della cronologia Git o dell'account che lo pubblica. Le affermazioni di fatto vanno valutate sulle fonti e le proposte sui loro effetti e costi.

---

## 1. Che cosa è questo documento, e cosa non è

Non è un programma politico. Non chiede voti, non nomina partiti, non indica colpevoli.

È l'estratto leggibile di un archivio di ricerca: 83 proposte e 66 fatti con fonte e anno, di cui 10 ancora da verificare, tenuti in un dataset versionato con regole esplicite su quando un'affermazione entra e quando esce. Il testo che state leggendo è un artefatto generato da quell'archivio, non il contrario. Se una frase qui contraddice un record del dataset, è questa frase a essere sbagliata.

Tre livelli, tenuti separati apposta perché confonderli è il modo più rapido di rendere un documento del genere inservibile:

| Livello | Cosa contiene | Come si contesta |
|---|---|---|
| **Diagnosi** (§2–§4) | Dati verificabili su cui esiste larghissima convergenza fra Banca d'Italia, Istat, UPB, OCSE, Corte dei conti, indipendentemente dal colore politico | Con una fonte primaria più recente o più pertinente |
| **Metodo** (§5) | Come è costruito il piano | Con un controesempio di riforma riuscita costruita diversamente |
| **Proposta** (§6–§9) | Scelte politiche, dove persone ragionevoli dissentono | Con una leva alternativa, non con un'obiezione generica |

Il paese di riferimento è l'Italia. Il metodo può essere riutilizzato, ma i dati, le norme e le istituzioni qui citati sono italiani.

**Stato di questa versione**: bozza dopo revisione dei contributi Gemini e Claude. Il dataset contiene 83 proposte e 66 fatti; 10 fatti richiedono conferma puntuale, 10 proposte hanno un gate e diverse soglie KPI richiedono una baseline. Il dossier [Perché siamo arrivati qui](../01_RICERCA/03_PERCHE_SIAMO_ARRIVATI_QUI.md) separa fatti e interpretazioni. L'integrazione tecnica non costituisce approvazione editoriale.

---

## 2. La diagnosi, in dodici numeri

Ogni riga porta il codice del record nell'archivio, così che chiunque possa risalire a fonte e anno senza fidarsi di questo documento.

| Indicatore | Valore | Fonte, anno | Record |
|---|---|---|---|
| Debito pubblico / PIL | ~138,6% previsto 2026 | DFP 2026; FMI, 2026 | `F-ECO-01` |
| Debito nominale | oltre 3.200 miliardi € | Banca d'Italia, giu. 2026 | `F-ECO-02` |
| Salari reali medi | nel 2024 **sotto** il livello 1990 (−1,6%), contro +35% di media OCSE | UPB su dati OCSE, 2024 | `F-ECO-03` |
| Produttività | sostanzialmente ferma dalla metà degli anni '90 | OCSE; Banca d'Italia, 2026 | `F-ECO-05` |
| Nascite | 355.000 nel 2025, minimo dal dopoguerra | Istat, 2025 | `F-DEMO-01` |
| Saldo naturale ed età media | −296.000 in un anno; età media 49,1 anni contro 44,9 della media UE | Istat, 1/1/2026 | `F-DEMO-02` |
| Divario fra figli desiderati e nati | con le intenzioni dichiarate sarebbero nati ~760.000 bambini; il 62% ha rinunciato per ostacoli economici e sociali, il 5,5% per scelta | Istat, 2025 | `F-DEMO-03` |
| Donne in età fertile | 11,5 milioni oggi contro 14,3 nel 1995; proiezione ~9 milioni al 2050 | Istat, 2026 | `F-DEMO-06` |
| Saldo laureati 25–34 | −21.000 in un anno | Istat, 2026 | `F-DEMO-04` |
| Occupati entro 3 anni dal titolo | 67,6%, contro 81% dell'Eurozona e oltre 90% della Germania | CSC su Istat/Eurostat, 2026 | `F-DEMO-05` |
| Tax gap | ~100 miliardi €/anno; propensione all'evasione 17% | MEF, 2025 | `F-FISC-01` |
| Tax gap sul lavoro autonomo | ~60% del reddito | Commissione UE / UPB, 2025 | `F-FISC-02` |

**E due numeri che vanno nella direzione opposta**, riportati perché un documento che elenca solo ciò che va male sta facendo propaganda, non analisi: i NEET fra i 15 e i 29 anni sono al 13,3%, erano il 25,7% dieci anni fa; l'abbandono scolastico è all'8,2%, sotto la media UE del 9,1% (`F-LAV-01`). Alcune cose si sono mosse davvero.

Il punto è **quali** si sono mosse. Migliorano le variabili di flusso — occupazione, arretrato giudiziario, dispersione scolastica. Restano ferme quelle di stock e di struttura: produttività, salari, demografia, debito.

---

## 3. Il nucleo del problema, in una frase

La bassa crescita della produttività, i salari deboli, il costo dell'abitare, la disponibilità dei servizi, il cambiamento demografico e il debito si influenzano a vicenda. Le relazioni causali esatte non sono state isolate da questo archivio: per scegliere quali leve usare servono valutazioni comparabili per territorio e gruppo sociale.

**È un'ipotesi di sistema.** Le interazioni proposte aiutano a formulare domande di ricerca, ma non provano che ogni intervento isolato fallisca. Le priorità vanno scelte con evidenze, costi, diritti e possibilità di attuazione.

---

## 4. Otto incongruenze

Non sono difetti di esecuzione: sono configurazioni stabili, in cui il comportamento di ciascun attore è individualmente razionale e l'esito collettivo è pessimo. Per questo durano.

**① Stato povero, famiglie ricche.** La ricchezza netta delle famiglie è fra le più alte d'Europa in rapporto al reddito; il debito pubblico è fra i più alti al mondo (`F-PARAD-01`). Il debito è stato socializzato, il patrimonio è rimasto privato. La fiscalità colpisce pesantemente il flusso — il lavoro — e leggermente lo stock.

**② Pressione fiscale alta, servizi percepiti scarsi.** Non è solo quantità di spesa, è composizione: una quota enorme va a pensioni e interessi, cioè a trasferimenti verso il passato, non a investimenti verso il futuro.

**③ Vogliamo figli e non li facciamo.** Il divario fra 760.000 desiderati e 355.000 nati non è culturale: il 5,5% non vuole figli per scelta, il 62% ha rinunciato per ostacoli (`F-DEMO-03`). Questo cambia radicalmente quali politiche funzionano — servizi, casa, stabilità del reddito — e quali no: bonus una tantum e campagne valoriali.

**④ Molte leggi, poca legalità.** Norme ambigue e procedimenti lunghi aumentano la discrezionalità del funzionario; la discrezionalità aumenta il rischio corruttivo; si risponde con nuovi controlli e nuove norme. L'anticorruzione per accumulo produce burocrazia difensiva: il dirigente che non firma non rischia nulla, quello che firma rischia in proprio. I controlli non fermano i disonesti, che conoscono le scorciatoie: paralizzano gli onesti.

**⑤ Formiamo capitale umano e lo regaliamo.** Quindici o vent'anni di istruzione pubblica per un laureato che produce valore aggiunto altrove, con un saldo di −21.000 laureati fra 25 e 34 anni in un solo anno (`F-DEMO-04`). Il problema non è solo attrarre: è trattenere e valorizzare.

**⑥ Le soglie che puniscono la crescita.** Il sistema fiscale e lavoristico è pieno di scalini dimensionali a 5, 15 e 50 addetti (`F-PARAD-02`). Un imprenditore razionale si ferma sotto la soglia. Da qui il nanismo d'impresa, che è la causa prossima della bassa produttività: le imprese piccole investono meno, esportano meno, formano meno, pagano meno.

**⑦ Instabilità politica, immobilismo normativo.** Circa 70 governi in 80 anni, durata media poco più di un anno (`F-IST-01`). L'effetto non è il caos: è che **l'orizzonte del decisore è più corto del tempo di maturazione delle riforme**. Una riforma della scuola dà risultati in dieci o quindici anni; chi governa diciotto mesi non ha alcun incentivo a pagarne il costo politico. Da qui la preferenza sistematica per misure visibili e reversibili.

**⑧ Tutti vogliono riformare le istituzioni, nessuna riforma passa.** Nel marzo 2026 il referendum confermativo sulla giustizia è stato respinto e la riforma non è entrata in vigore; per circa il 31% degli elettori del No fu esplicitamente un voto contro il governo (`F-REF-06`). È il pattern dal 1993: si cambiano le regole del gioco elettorale e non l'architettura che produce lentezza.

**Una nota sul "carattere nazionale".** Non esiste un tratto psicologico che spieghi tutto questo, e le spiegazioni culturaliste sono spesso usate per giustificare l'immobilismo: *siamo fatti così*. La lettura che questo archivio adotta è l'opposta e ha una conseguenza operativa precisa: i comportamenti sono **risposte razionali a incentivi istituzionali**, e diventano cultura solo dopo, per stratificazione. Se sono risposte a incentivi, cambiando gli incentivi cambiano — ma i tempi sono quelli di una generazione, non di una legislatura. Le regolarità comportamentali rilevanti (familismo come sostituto di istituzioni assenti, disponibilità a pagare le tasse condizionata alla percezione che paghino anche gli altri, avversione all'incertezza) sono documentate in letteratura ma non ancora verificate su fonte primaria in questo archivio: restano **ipotesi di lavoro**, non fatti, e sono trattate come tali.

---

## 5. Quattro regole di metodo

Sono la parte meno appariscente del documento e quella che lo distingue da un programma elettorale.

**La sequenza conta più del contenuto.** La diagnosi dei paragrafi precedenti è nota da trent'anni e ogni governo ha promesso pezzi di quello che segue. Se il vincolo fosse la conoscenza, il problema sarebbe risolto. Il vincolo è l'economia politica: i costi sono concentrati e immediati, i benefici sono diffusi e lontani. Le riforme che chiedono sacrifici vanno **dopo** quelle che producono risultati visibili — altrimenti il consenso finisce prima del beneficio.

**Ogni misura dovrebbe avere un gate.** Una fase non si apre perché è passato il tempo previsto, ma perché la precedente ha prodotto un risultato misurato. Se il gate non passa, si rivede la sequenza. Questa è, oggi, una lacuna dell'archivio: solo 10 proposte su 83 hanno un gate formalizzato.

**Rollback dichiarato in anticipo.** Ogni misura ha una clausola di valutazione a ventiquattro mesi e una soglia sotto la quale viene ritirata. Il punto non è la valutazione: è che la soglia sia scritta **prima**, quando non si sa ancora come andrà. Le misure fallite, in Italia, non vengono quasi mai ritirate: vengono stratificate.

**Chi si oppone ha un nome.** Ogni proposta dell'archivio dichiara chi perde qualcosa. Una proposta senza oppositori identificabili o è banale o è stata capita male. Questa colonna non è un esercizio di trasparenza: è la colonna in cui le riforme muoiono, e un piano che non la compila non è un piano.

---

## 6. Sei pilastri

**I — Stato leggibile.** La complessità normativa è una tassa regressiva: la paga chi non può permettersi consulenti. Principio *once-only* reso obbligo giuridico — se un dato è già in una banca dati pubblica, richiederlo è illegittimo; clausole di scadenza sulle norme amministrative, che decadono se non riconfermate con dati di impatto; codice unico per materia con testo consolidato a valore legale; silenzio-assenso con certificato rilasciato dal sistema, non con contenzioso. È la precondizione di tutto il resto, costa quasi nulla e non richiede riforme costituzionali.

**II — Fisco che sposta il peso dal lavoro.** Tassare meno ciò che vogliamo di più, in modo coerente ciò che non produce. Riduzione strutturale del cuneo sui redditi medio-bassi, finanziata — non a debito — da recupero di tax gap, revisione delle agevolazioni e riordino catastale a invarianza di gettito. Abolizione delle soglie dimensionali punitive, sostituite da una transizione continua. Adempimenti semplificati per chi è in regola, incrocio dati in tempo reale per chi non lo è. Nessun condono: ogni condono distrugge dieci anni di credibilità della lotta all'evasione.

**III — Produttività e dimensione d'impresa.** Incentivi condizionati a risultati misurati e non all'acquisto di beni, con soppressione automatica di quelli inefficaci. Sportello unico nazionale per gli investimenti, con potere sostitutivo e termine certo. Energia: il prezzo industriale è fra i più alti dell'Unione ed è indicato come freno diretto alla competitività (`F-ECO-04`). Concorrenza reale nei servizi protetti, dove si annida gran parte della bassa produttività.

**IV — Giovani, lavoro, capitale umano.** Sistema duale su scala tedesca: è il singolo intervento con il miglior rapporto fra costo ed effetto, perché agisce contemporaneamente su produttività, salari giovanili, emigrazione e disallineamento fra studi e impiego. Politiche attive con presa in carico entro trenta giorni e centri per l'impiego valutati sui tassi di ricollocazione. Contratto unico a tutele crescenti, con costo del licenziamento prevedibile, in cambio dell'eliminazione della giungla dei contratti a termine — e solo dopo che le politiche attive funzionino davvero.

**V — Demografia e patto fra generazioni.** Non si tratta di convincere: si tratta di rimuovere ostacoli, e il divario fra desiderato e reale è il mandato. Servizi prima dei bonus: nidi a copertura universale, tempo pieno reale, casa accessibile per gli under 35. Assegno unico stabilizzato e indicizzato, perché la prevedibilità pluriennale vale più dell'importo. Automatismi demografici sulle pensioni ripristinati, con eccezioni documentate per i lavori gravosi e risparmi vincolati per legge a scuola, natalità e ricerca — il vincolo di destinazione visibile è ciò che rende accettabile il sacrificio. Programmazione pluriennale dell'immigrazione sul fabbisogno.

**VI — Istituzioni che decidono ed eseguono.** Superamento del bicameralismo paritario: una sola camera legislativa, la seconda di rappresentanza territoriale e controllo. Riduce i tempi senza concentrare potere nell'esecutivo, ed è l'alternativa al premierato, che concentra potere senza ridurre i passaggi. Fine dell'abuso della decretazione d'urgenza in cambio di corsie garantite per i disegni di legge del governo. Gestioni associate obbligatorie per le funzioni tecniche dei comuni sotto soglia — sono circa 7.900, molti sotto i 5.000 abitanti (`F-IST-05`), e la mancanza di capacità di progettazione è il vero collo di bottiglia. Soprattutto: **riforma della responsabilità erariale**, per distinguere il dolo dalla colpa lieve di chi decide in buona fede. Finché firmare è più rischioso di non firmare, nessuna riforma verrà eseguita.

### Sulle regole della politica

Quattro punti, perché su questi il dibattito pubblico discute quasi sempre la cifra sbagliata.

- **Autodichia.** Camera e Senato deliberano su se stessi in materia di trattamento economico e previdenziale, e i ricorsi sono decisi da organi interni (`F-POL-01`). È il motivo per cui ogni riforma dei costi della politica è reversibile: chi decide è chi ne beneficia. La leva non è tagliare l'indennità, è toglierne la determinazione a chi la riceve e affidarla a un parametro esterno automatico.
- **Perimetro della trasparenza.** Gli obblighi coprono i partiti, non pienamente fondazioni, associazioni e comitati. Trasparenza per soggetto, non per etichetta: chiunque finanzi attività politica sopra una soglia bassa è tracciato, in formato aperto e in tempo reale. Manca inoltre una legge organica sulla rappresentanza di interessi: è la lacuna più grave dell'intero capitolo.
- **Clientelismo.** Non serve punirlo, serve renderlo inutile. Il voto di scambio funziona quando l'eletto può consegnare qualcosa: una pratica, un posto in graduatoria, una licenza. L'automatismo delle procedure e la trasparenza dei criteri tolgono la merce di scambio. È una riforma amministrativa, non elettorale.
- **Referendum.** Il quorum di partecipazione è un difetto di progettazione: trasforma l'astensione in un'arma di voto, perché a chi è contrario conviene che la gente non vada a votare. Negli ultimi trent'anni, su dieci referendum non costituzionali il quorum è stato raggiunto due volte (`F-REF-01`); nel giugno 2025 hanno votato quattordici milioni di persone senza alcun effetto (`F-REF-02`). Sostituirlo con un quorum di approvazione — valido se i Sì superano una soglia dell'elettorato complessivo — obbliga chi è contrario a votare No e riporta la campagna sul merito.

Le alternative incompatibili restano aperte e non risolte: elezione parlamentare rafforzata **oppure** elezione diretta del Capo dello Stato; tre diverse soluzioni per i senatori a vita. L'archivio le tiene entrambe con i rispettivi tradeoff. Scegliere sarebbe una posizione politica, e questo non è il documento che la prende.

---

## 7. La sequenza

**Fase 0 — primi 12 mesi: credibilità.** Costo di bilancio quasi nullo, effetto percepito alto. Once-only per legge e silenzio-assenso con certificato automatico; clausole di scadenza e taglio degli adempimenti già mappati; riforma della responsabilità erariale, per sbloccare le firme; sportello unico investimenti; divieto decennale di condoni fiscali.
*Gate di uscita*: tempi mediani dei tre permessi più richiesti dimezzati. Se non accade, il vincolo non è normativo ma di capacità amministrativa, e si rinforza la fase 1 prima di proseguire.

**Fase 1 — anni 1-3: capacità.** Si costruiscono le infrastrutture che le riforme successive danno per scontate. Reclutamento tecnico della pubblica amministrazione; gestioni associate per i piccoli comuni; centri per l'impiego rifondati e valutati; scale-up del sistema duale; piano nidi e tempo pieno; autorizzazioni e accumuli sull'energia.
*Gate*: tasso di ricollocazione dei centri per l'impiego sopra soglia. **Senza questo non si procede al pacchetto lavoro.** Flessibilità in uscita senza politiche attive funzionanti non produce flexicurity: produce precarietà.

**Fase 2 — anni 3-6: scambio.** Le riforme che chiedono e danno insieme. Contratto unico e flexicurity. Riforma fiscale a due gambe **contestuali**: taglio del cuneo e riordino catastale a invarianza di gettito. Separarle è ciò che le ha sempre fatte fallire — da sole, ognuna ha solo perdenti visibili. Riordino degli incentivi con valutazione d'impatto. Apertura dei settori protetti, con compensazioni a chi perde una rendita legittimamente acquisita.
*Gate*: gettito da recupero evasione sopra target. Il taglio del cuneo si estende solo se la copertura è reale, non stimata.

**Fase 3 — anni 4-8: struttura.** Le riforme lente e quelle costituzionali. Automatismi pensionistici con vincolo di destinazione dei risparmi, comunicati come patto generazionale esplicito e non come taglio. Riforma monocamerale e riordino del Titolo V, sottoposti a referendum **dopo** che i risultati delle fasi precedenti siano visibili. Programmazione pluriennale dell'immigrazione.

La collocazione della parte costituzionale in fondo non è prudenza: è la lettura del marzo 2026. Una riforma istituzionale votata in un clima di sfiducia viene giudicata come referendum sul governo, non nel merito.

**Un vincolo temporale che non dipende da questo piano**: la chiusura del PNRR è fissata al 31 agosto 2026 per milestone e rendicontazione e al 31 dicembre 2026 per i pagamenti finali (`F-PNRR-01`). Il 2027 sarà il primo anno senza lo stimolo esterno e, soprattutto, senza il vincolo esterno che ha tenuto il ritmo. La domanda del 2027 non è *cosa faremo*: è **cosa regge senza qualcuno che tenga il cronometro**.

---

## 8. Se si potessero fare solo cinque cose

In ordine di rapporto fra impatto e fattibilità:

1. **Once-only, clausole di scadenza, riforma della responsabilità erariale.** Costo quasi nullo. Sbloccano la capacità di esecuzione di tutto il resto: senza, ogni altra riforma resta sulla carta.
2. **Sistema duale su scala tedesca.** L'unico intervento che agisce insieme su produttività, salari giovanili, emigrazione e disallineamento.
3. **Nidi e tempo pieno universali.** Un solo strumento che agisce su natalità, occupazione femminile, povertà educativa e prodotto potenziale.
4. **Riforma fiscale a due gambe contestuali**, più contrasto permanente al tax gap senza condoni.
5. **Abolizione delle soglie dimensionali** che puniscono la crescita d'impresa.

Se anche solo queste cinque venissero eseguite in dieci anni con costanza, gran parte del resto diventerebbe possibile — perché produrrebbero la cosa di cui il paese è più povero: **la prova che riformare funziona.**

---

## 9. Cosa questo documento non promette

Questa sezione non è una excusatio: è la parte in cui si verifica se un documento di questo tipo è onesto.

**Non promette che la demografia si aggiusti.** Anche con una fecondità in risalita a 1,85 — scenario ottimistico — le nascite annue non supererebbero le 500.000, perché le donne in età fertile sono già oggi 11,5 milioni contro 14,3 del 1995 e scenderanno verso i 9 milioni entro il 2050 (`F-DEMO-06`). Il numero di madri potenziali è già determinato e nessuna politica può cambiarlo. Ne segue una conclusione scomoda: **nessuna politica per la natalità può, da sola, evitare il calo della forza lavoro nei prossimi venticinque anni.** O si accetta un'economia più piccola, o si aumenta la produttività per persona, o si ricorre all'immigrazione. Realisticamente, tutte e tre.

**Non promette che il consolidamento sia indolore.** Consolidare con un debito al 138,6% tagliando investimenti deprime la crescita e peggiora il rapporto stesso. È un'obiezione keynesiana forte, sostenuta da una parte non piccola degli economisti. La risposta parziale di questo piano è la composizione — comprimere spesa corrente e agevolazioni inefficaci, proteggere la spesa in conto capitale — ma chi sostiene che serva più investimento pubblico anche a debito, con debito comune europeo, ha un argomento serio che qui non viene liquidato.

**Non promette che senza vincolo esterno si faccia qualcosa.** Con la fine del PNRR scompare la condizionalità che ha prodotto i risultati migliori. Se il prossimo quadro europeo non fornisce un vincolo analogo, la probabilità di deriva aumenta, e questo piano non ha uno strumento per impedirlo.

**Non promette di avere ragione.** Un piano così articolato presuppone che chi lo scrive sappia, e la storia delle riforme insegna il contrario. Servono sperimentazione locale, valutazione indipendente e la disponibilità a dire *questa non ha funzionato*. Da qui le clausole di rollback, che sono l'unica parte del documento che si applica al documento stesso.

**Non promette che tutto questo sia nuovo.** Non lo è, ed è dichiarato al §5. La diagnosi è condivisa da decenni. La parte non ovvia sono la sequenza e le compensazioni, non l'elenco.

---

## 10. Come si contesta questo documento

Si contesta sul record, non sulla frase.

- **Un fatto sbagliato**: si indica il codice (`F-…`), il valore che si ritiene corretto e la fonte primaria puntuale. Senza fonte primaria la correzione non entra. Vince la fonte primaria più recente; a parità di livello, il dato più recente.
- **Una proposta sbagliata**: si indica il codice (`P-…`) e si propone una **leva alternativa** — il meccanismo di incentivo, non l'etichetta. Se le due leve non possono coesistere, il dataset le tiene entrambe come varianti A e B con i rispettivi tradeoff, e non sceglie. Due alternative esplicite valgono più di una media indistinta che nessuno sosterrebbe.
- **Una sequenza sbagliata**: si discute la fase o il gate, non la leva. Sono due discussioni diverse e confonderle le rende entrambe inconcludenti.
- **Una lacuna**: si propone un record nuovo. Deve avere problema, leva, KPI con soglia e data, almeno un oppositore identificato, fase e vincolo giuridico. Se questi campi non si riescono a compilare, non è ancora una proposta.

Un contributo che non si può tradurre in una di queste quattro mosse è un'opinione. Le opinioni sono legittime e non entrano nell'archivio.

---

## 11. Stato del lavoro

| Voce | Stato |
|---|---|
| Proposte nell'archivio | 83, dopo l'accorpamento di 7 duplicati |
| Fatti con fonte e anno | 66, di cui 10 ancora da verificare |
| KPI con una soglia numerica | La presenza di un numero non documenta la baseline né la fattibilità; vedi [coda KPI](../03_VERIFICA/05_KPI_DA_QUANTIFICARE.md) |
| Gate di attivazione formalizzati | 10 su 83 |
| Coperture economiche e impatti territoriali | Da quantificare con metodo comparabile |
| Revisione Claude dei nove capitoli aggiuntivi | In attesa del materiale indicato dal contributore |
| Revisione umana qualificata | Non effettuata |

Nessuna proposta è approvata. Le fonti primarie e i limiti interpretativi sono in [04_FONTI_RIFORME_2026](../01_RICERCA/04_FONTI_RIFORME_2026.md).

---

## 12. Firma

Questo documento è anonimo per scelta e non per cautela: rende più difficile discuterlo come questione di persone e più facile discuterlo come questione di record.

Non è affiliato ad alcun partito, movimento, associazione o soggetto economico. Non raccoglie fondi. Non chiede adesioni. Chiunque può contestarlo, correggerlo o riusarlo secondo le regole del §10.

**L'Italia che vorrei** — archivio di ricerca e progettazione istituzionale
Versione 0.1 · bozza editoriale · 20 settembre 2026

---

### Nota sulle fonti

I dati citati provengono da: Istat (bilancio demografico 2025; report su giovani e migrazioni, maggio 2026); Banca d'Italia (Relazione annuale, maggio 2026; statistiche di finanza pubblica); MEF (Documento di finanza pubblica 2026; Relazione sull'economia non osservata e sull'evasione); Ufficio parlamentare di bilancio; OCSE (*Economic Survey: Italy 2026*); FMI (*Fiscal Monitor*, aprile 2026); Commissione europea; Centro Studi Confindustria; Ministero dell'Interno; Camera dei deputati. Il dettaglio per singolo record è in [03_REGISTRO_FATTI](../03_VERIFICA/03_REGISTRO_FATTI.md).
