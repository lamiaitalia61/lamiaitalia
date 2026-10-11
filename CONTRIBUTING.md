# Contribuire a L'Italia che vorrei

**Nell'Italia che vorrei ogni proposta si può controllare e migliorare.** Porta una fonte, una controprova, una stima di costo, un rischio o una soluzione alternativa.

## Prima di aprire una proposta

1. Cerca nell'[indice](02_PROPOSTE/02_INDICE_PROPOSTE.md) se la leva esiste già.
2. Indica problema, persone interessate, meccanismo della riforma, fonte primaria, costo o motivo per cui è ancora ignoto, indicatore misurabile e possibile effetto indesiderato.
3. Distingui dato, interpretazione e scelta politica. Una fonte non verificata resta esplicitamente in verifica.
4. Non pubblicare nomi privati, recapiti, indirizzi di rete, percorsi del computer, esportazioni di chat o metadati personali. Per parlare di persone pubbliche usa solo informazioni pertinenti e fonti affidabili.
5. Per i documenti generati modifica `dati/` e lancia `python strumenti/genera.py`.

## Verifiche

```bash
python strumenti/valida.py --pubblicazione
python strumenti/genera.py
python strumenti/privacy_check.py --history
```

La cronologia del repository principale ha solo `main`. Usa una pull request da un tuo fork; la revisione segue il [protocollo](PROTOCOLLO_MERGE.md). Contribuire non equivale ad approvazione automatica e non richiede di rivelare un'identità personale nella proposta. I metadati del tuo account GitHub o del tuo fork sono gestiti da GitHub e restano sotto il tuo controllo.

Per riuso e attribuzione vedi [LICENSE](LICENSE) e [LICENSE-CODE](LICENSE-CODE).
