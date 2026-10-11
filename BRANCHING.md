# Pubblicazione e versioni

Il repository pubblico usa un solo branch, `main`. Le proposte esterne arrivano tramite issue o pull request da fork personali; nessun branch di contributo viene mantenuto nel repository principale.

Ogni modifica sostanziale aggiorna dataset, documenti generati e [changelog](CHANGELOG.md), passa `python strumenti/valida.py --pubblicazione` e `python strumenti/privacy_check.py --history`, e viene esaminata prima del merge. Un merge Git non equivale all'approvazione politica o scientifica della proposta.

La pubblicazione iniziale parte da una cronologia nuova, senza importare commit di lavoro precedenti.
