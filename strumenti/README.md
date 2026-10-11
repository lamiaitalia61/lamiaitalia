# Strumenti

```bash
python strumenti/valida.py                      # valida il dataset ed esporta i CSV in build/
python strumenti/valida.py --pubblicazione      # + verifica che 06_PUBBLICAZIONE non citi fatti non verificati
python strumenti/valida.py --strict             # fallisce anche in presenza di soli avvisi
python strumenti/valida.py --merge contrib.json # valida un contributo esterno e produce build/merge-report.json
python strumenti/genera.py                      # rigenera i documenti derivati dal dataset
```

Nessuna dipendenza esterna: solo libreria standard, Python 3.9+.

## Cosa blocca il validatore

ID duplicati o malformati, campi obbligatori mancanti, ambiti fuori vocabolario, valori di `costo` fuori enum, `variante` diversa da una singola lettera, evidenze orfane, dipendenze inesistenti, **prerequisiti bloccanti collocati in una fase successiva**, varianti presenti in un solo ramo, un record che è insieme dipendenza e rafforzativo, e — con `--pubblicazione` — qualunque fatto `verificato: false` citato nei documenti pubblici.

## Cosa segnala senza bloccare

Proposte senza KPI, senza oppositori o senza evidenza collegata — che quasi sempre sono opinioni travestite da proposte; KPI privi di soglia numerica, quindi non falsificabili; temi contestati privi del campo `rischio`; fatti non verificati; fatti mai citati da nessuna proposta.

Gli avvisi sono la coda di lavoro del progetto, non rumore da silenziare. `--strict` li rende bloccanti: va usato prima di una pubblicazione, non durante la stesura.

## Documenti generati

`genera.py` riscrive per intero, ogni volta:

| File | Contenuto |
|---|---|
| `02_PROPOSTE/02_INDICE_PROPOSTE.md` | indice per ambito, copertura di evidenza e KPI, varianti aperte |
| `02_PROPOSTE/SCHEDE/<ambito>.md` | una scheda per proposta, con evidenza espansa |
| `03_VERIFICA/03_REGISTRO_FATTI.md` | tutti i fatti con fonte, anno, stato e proposte che li citano |
| `03_VERIFICA/04_FATTI_DA_VERIFICARE.md` | coda dei record da confermare su fonte primaria |
| `03_VERIFICA/05_KPI_DA_QUANTIFICARE.md` | proposte con indicatore senza soglia |
| `04_COSTITUZIONE/02_MATRICE_VINCOLI.md` | proposte per fonte del diritto necessaria |
| `05_PIANO_ATTUAZIONE/02_SEQUENZA_FASI.md` | fasi, catene di dipendenza, gate |

Non vanno modificati a mano: si modifica `dati/` e si rigenera.
