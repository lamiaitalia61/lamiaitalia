# Pubblicazione e versioni

Il repository pubblico usa un solo branch, `main`. Le proposte esterne arrivano tramite issue o pull request da fork personali; nessun branch di contributo viene mantenuto nel repository principale.

Ogni modifica sostanziale aggiorna dataset, documenti generati e [changelog](CHANGELOG.md), passa `python strumenti/valida.py --pubblicazione` e `python strumenti/privacy_check.py --history`, e viene esaminata prima del merge. Un merge Git non equivale all'approvazione politica o scientifica della proposta.

La pubblicazione iniziale parte da una cronologia nuova, senza importare commit di lavoro precedenti.

I messaggi dei commit descrivono in poche parole il cambiamento concreto, in linguaggio comune: `Prima pubblicazione`, `Rivede le proposte sulla burocrazia`, `Corregge la copertina`. Evitare formule tecniche o promesse di anonimato nel titolo.

**English:** Keep commit titles short and human-readable. Name the actual change, such as `First publication`, `Reviews bureaucracy proposals`, or `Fixes the cover`. Do not use the title to promise anonymity.
