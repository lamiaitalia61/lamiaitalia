# Prompt per post, immagini e video brevi

## Analisi delle visualizzazioni esistenti

Al momento il repository contiene una sola grafica: [`assets/cover.svg`](assets/cover.svg), una copertina orizzontale 1200 × 440 px. Il blu scuro, il verde e le due strisce laterali danno una riconoscibilità utile; titolo e invito all'azione sono leggibili nella pagina GitHub. Il riquadro verde è stato allargato perché il testo ne usciva. Questa copertina non è un formato pronto per un post verticale o un video 9:16: per quei canali serve una composizione nuova, con meno testo e margini di sicurezza. Il segno di spunta è un elemento grafico, non una certificazione delle 83 proposte o dei 66 fatti.

## Schede di partenza

Usare **un intervento per contenuto**, leggendo il record e la scheda prima di produrre il testo. Questi tre interventi sono spunti iniziali, non misure approvate:

| Tema | Proposta da leggere | Punto da spiegare | Limite da mantenere visibile |
|---|---|---|---|
| Burocrazia | [`P-STATO-10-CLA`](02_PROPOSTE/SCHEDE/stato-leggibile.md) | Servizi essenziali completi online e canale assistito equivalente | Costi, test di accessibilità e obiettivi ancora da definire |
| Sanità | [`P-SAN-01-CLA`](02_PROPOSTE/SCHEDE/sanita.md) | Agenda verificabile per offerta pubblica e convenzionata e tempi per area | Un'agenda unica non aumenta da sola la capacità di cura; copertura da stimare |
| Giustizia | [`P-GIU-01-CLA`](02_PROPOSTE/SCHEDE/giustizia.md) | Indicatori comparabili per ufficio e sperimentazione organizzativa | Nessuna evidenza collegata nel record; evitare classifiche semplicistiche |

## Prompt 1 — post per X e immagine esplicativa

```text
Sei un editor del progetto “L'Italia che vorrei”. Prepara un post in italiano per X e la specifica di una singola immagine che spieghi UN intervento. Ti fornisco il record della proposta, la scheda generata e gli eventuali fatti collegati: [INCOLLA QUI]. Usa solo questi materiali. Se manca un dato, scrivi “da verificare” o “da stimare”; non cercare di riempire i vuoti.

Produci:
1. Un post entro 280 caratteri, link compreso: [URL DELLA SCHEDA]. Apri con una frase diretta. Distingui proposta da risultato ottenuto. Chiudi con una domanda concreta o un invito a leggere la scheda. Niente hashtag obbligatori, accuse personali o slogan spiegati dopo lo slogan.
2. Testo dell'immagine: titolo di massimo 7 parole, poi tre blocchi brevi “Problema / Proposta / Da verificare”. Scrivi la fonte e l'ID del record in un piccolo piè di pagina leggibile. Se una fonte primaria non è presente nel materiale, non inventarla.
3. Istruzioni visive per 4:5 (1080 × 1350) e variante 1:1 (1080 × 1080): blu scuro #101f2d, verde #24966d, testo chiaro; gerarchia tipografica forte, margini ampi, contrasto accessibile. Nessun logo istituzionale, grafico quantitativo, foto di persone reali o segno di approvazione se non supportati da prove. Riserva spazio al link o al codice della proposta.
4. Controllo finale: conta i caratteri del post; elenca ogni numero o affermazione di fatto e il relativo record/fonte; segnala le affermazioni non supportate da eliminare.
```

## Prompt 2 — short YouTube e TikTok

```text
Sei un autore video del progetto “L'Italia che vorrei”. Scrivi lo storyboard di un video verticale 9:16 di 30–45 secondi, riutilizzabile come YouTube Short e su TikTok, che spieghi UN intervento. Materiali vincolanti: [INCOLLA RECORD, SCHEDA, FATTI COLLEGATI E URL]. Non presentare la proposta come legge vigente, scelta approvata o effetto già misurato.

Fornisci una tabella con tempo, voce narrante, testo a schermo e scena. Sequenza: apertura diretta (0–3 s), problema, meccanismo della proposta, principale condizione o rischio, invito a leggere e contestare la scheda. Usa frasi pronunciabili, sottotitoli completi e testo a schermo molto breve. Prevedi inquadrature che si possano creare con tipografia e forme semplici, senza filmati di repertorio non autorizzati. Mantieni gli elementi essenziali lontani dai bordi e dalle zone occupate dai comandi delle piattaforme.

Consegna anche: titolo YouTube, didascalia TikTok, testo alternativo della copertina, elenco dei file o schermate da produrre, link della scheda e controllo delle fonti. Per ogni numero o promessa di effetto, indica fonte e stato di verifica; elimina ciò che non è documentato. Chiudi con una frase netta, senza aggiunte che spieghino lo slogan.
```

## English note and reusable prompts

The repository currently has one horizontal visual, [`assets/cover.svg`](assets/cover.svg), at 1200 × 440 px. Its call-to-action box has been widened to contain the label. Create new 4:5 or 1:1 artwork for X and 9:16 compositions for Shorts and TikTok. The checkmark is decorative and must not be presented as validation of every proposal or fact.

**X and image prompt:** Using only the supplied proposal record, generated sheet, linked fact records and URL, write one Italian X post of at most 280 characters including the link. Make clear that the intervention is a proposal. Provide a 4:5 image brief with a seven-word headline, short “Problem / Proposal / Still to verify” blocks, record ID and source. Use the cover's navy and green palette; keep text readable and avoid invented figures, institutional logos and unsupported claims. Count characters and list evidence for each factual claim.

**Short video prompt:** Using only the supplied records, sheet, sources and URL, draft a 30–45 second Italian vertical storyboard for YouTube Shorts and TikTok. Include a direct opening, the problem, how the proposal would work, its main risk or condition, and an invitation to inspect the sheet. Return timestamps, voiceover, on-screen text, visual directions, subtitles, platform titles/captions and a source check. Keep text within safe areas. Never imply enactment, approval or measured results without evidence.
