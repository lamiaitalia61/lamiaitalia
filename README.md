# L'Italia che vorrei — rinnoviamola noi dal basso

![L'Italia che vorrei: idee aperte, dati verificabili, scelte pubbliche](assets/cover.svg)

> **Non ditelo ai politici.**

**Nell'Italia che vorrei** la Costituzione si rispetta, la burocrazia aiuta invece di bloccare, i servizi funzionano ovunque e ogni spesa pubblica si può spiegare. **Rinnoviamo l'Italia** con proposte controllabili e discussioni aperte.

**L'Italia ripensata dall'AI, verificata dalle persone.** I modelli aiutano a generare e contestare idee; la decisione resta pubblica e umana.

## Da dove partire

| Se vuoi… | Leggi |
|---|---|
| capire perché siamo arrivati qui | [Diagnosi con fonti e limiti](01_RICERCA/03_PERCHE_SIAMO_ARRIVATI_QUI.md) |
| leggere la visione breve | [Manifesto](06_PUBBLICAZIONE/01_MANIFESTO.md) |
| confrontare le riforme | [Indice delle 83 proposte](02_PROPOSTE/02_INDICE_PROPOSTE.md) |
| entrare nel merito | [Documento completo](06_PUBBLICAZIONE/02_DOCUMENTO_COMPLETO.md) |
| vedere ciò che resta da verificare | [Registro dei fatti](03_VERIFICA/03_REGISTRO_FATTI.md) e [KPI da quantificare](03_VERIFICA/05_KPI_DA_QUANTIFICARE.md) |
| proporre una correzione | [Come contribuire](CONTRIBUTING.md) |
| condividere il progetto | [Messaggi pronti e attribuzione](CONDIVIDI.md) |
| preparare post, immagini e video brevi | [Prompt per i contenuti social](PROMPT_SOCIAL.md) |

## I temi

**Riforme costituzionali e istituzioni · pubblica amministrazione e burocrazia · sanità e liste d'attesa · giustizia · scuola e lavoro · famiglie e welfare · fisco e spesa pubblica · trasparenza politica e partecipazione.**

Il dataset contiene **83 proposte** e **66 fatti** con fonte e anno. Dieci fatti attendono ancora conferma puntuale; 22 avvisi del validatore segnalano lavoro aperto, tra cui soglie e fonti mancanti. Una proposta presente nel repository **non è una posizione approvata**. Le coperture e gli effetti territoriali di molte misure sono ancora da stimare.

## Come funziona

Il punto di partenza è [`dati/`](dati/): ogni proposta ha un identificativo, una leva, un ambito, una fase e, quando disponibile, evidenze e condizioni di attivazione. I documenti marcati `GENERATO` derivano da quei record. [`proposte/`](proposte/README.it.md) conserva un contributo editoriale di nove capitoli, [mappato al dataset](proposte/MAPPATURA_DATASET.md), senza trasformarlo automaticamente in programma politico.

```bash
python strumenti/valida.py --pubblicazione
python strumenti/genera.py
python strumenti/privacy_check.py --history
```

Il validatore controlla struttura, riferimenti e divieto di citare fatti non verificati nei testi pubblici; **non certifica** la verità di ogni affermazione né la fattibilità economica o giuridica di una riforma. Il controllo privacy cerca identificatori strutturati nei file e nei commit; non può garantire anonimato assoluto.

## Partecipa

1. Scegli una proposta nell'[indice](02_PROPOSTE/02_INDICE_PROPOSTE.md).
2. Porta una fonte primaria, un costo, un effetto indesiderato o un'alternativa concreta.
3. Apri una issue o una pull request, seguendo il [protocollo di revisione](PROTOCOLLO_MERGE.md) e le [regole per contribuire](CONTRIBUTING.md).
4. Se il lavoro ti convince, condividi il link e invita altre persone a verificarlo. Le visualizzazioni non sostituiscono le prove.

Questa repository pubblica un solo branch, **`main`**. L'integrazione tecnica di un contributo non equivale alla sua approvazione editoriale.

## Riutilizzo e citazione

Testi e dataset originali: **[Creative Commons Attribution 4.0 International](LICENSE)**. Puoi copiare, adattare e ricondividere anche commercialmente, indicando **“L'Italia che vorrei”**, il link al repository, la licenza e le modifiche apportate. Gli strumenti software in [`strumenti/`](strumenti/) usano la [licenza MIT](LICENSE-CODE). Le fonti esterne conservano le proprie condizioni di riuso; citarle qui non significa concedere diritti sui loro contenuti.

Citazione pronta: *L'Italia che vorrei, “Proposte per rinnovare l'Italia dal basso”, versione consultata, repository `lamiaitalia61/lamiaitalia`, CC BY 4.0.* Vedi anche [`CITATION.cff`](CITATION.cff).

## English summary

**L'Italia che vorrei** is an open, evidence-led collection of ideas for reforming Italy's institutions, public administration, healthcare, justice, welfare, taxation and public spending. AI helps draft and challenge proposals; people check sources and make choices. The project currently tracks 83 proposals and 66 dated facts, with unresolved evidence and cost estimates clearly marked. Read the [diagnosis](01_RICERCA/03_PERCHE_SIAMO_ARRIVATI_QUI.md), [proposal index](02_PROPOSTE/02_INDICE_PROPOSTE.md), [social content prompts](PROMPT_SOCIAL.md), [contribution guide](CONTRIBUTING.md) and [license](LICENSE). Reuse is welcome with attribution.
