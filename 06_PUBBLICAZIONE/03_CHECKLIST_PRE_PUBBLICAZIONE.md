---
title: "Checklist pre-pubblicazione"
tags:
  - l-italia-che-vorrei
  - pubblicazione
  - controllo
status: "ATTIVO"
---

# Checklist pre-pubblicazione

Da eseguire per intero prima di rendere pubblico qualunque documento di `06_PUBBLICAZIONE`. Una casella non spuntata è un blocco, non un avviso.

## A. Controlli automatici

- [ ] `python strumenti/valida.py --pubblicazione` esce con codice 0
- [ ] `python strumenti/genera.py` non produce differenze rispetto a quanto committato (i documenti generati sono allineati al dataset)
- [ ] `python strumenti/valida.py --strict` eseguito: il numero di avvisi è noto e dichiarato nel documento

## B. Contenuto

- [ ] Nessun fatto `verificato: false` compare nei testi pubblici — verificato automaticamente, ma ricontrollare le parafrasi: il controllo automatico cerca gli ID, non le affermazioni riformulate
- [ ] Ogni cifra ha fonte e anno
- [ ] Nessuna proposta è presentata come fatto
- [ ] Le sezioni incomplete sono marcate come tali, non omesse
- [ ] Lo stato del lavoro è dichiarato con numeri, non con formule generiche
- [ ] Le controevidenze rilevanti sono riportate
- [ ] Le varianti A/B sono esposte entrambe, senza scelta implicita nel testo
- [ ] Il registro delle obiezioni riporta le obiezioni nella loro versione forte

## C. Revisioni esterne richieste dal progetto

- [ ] Fact-check finale su fonte primaria
- [ ] Revisione costituzionale (costituzionalista)
- [ ] Revisione economica (economista)
- [ ] Revisione amministrativa (dirigente pubblico)
- [ ] Controllo dei riferimenti e dei link interni

Nessuna di queste è surrogabile con una revisione prodotta da un modello di intelligenza artificiale. Il materiale di lavoro non pubblicato lo dice esplicitamente: se manca una revisione indipendente, lo stato è `INCOMPLETO` e il consenso multi-modello non va simulato.

## D. Privacy, anonimato e metadati

- [ ] Nessun nome reale, indirizzo, email o account personale nel testo
- [ ] Nessun riferimento che permetta di ricostruire l'identità di chi scrive (luoghi, ruoli, vicende personali, dettagli biografici indiretti)
- [ ] Metadati dei file di esportazione ripuliti — autore, organizzazione, percorsi locali, cronologia delle revisioni. Vale in particolare per PDF, DOCX e immagini: il controllo sul testo non basta, i metadati sopravvivono all'esportazione
- [ ] Cronologia git controllata: nome e email dell'autore dei commit, percorsi locali nei messaggi
- [ ] Nessun percorso di file locale nei testi pubblicati
- [ ] Se la pubblicazione avviene su un servizio online, l'account usato non è collegabile all'identità personale

> [!warning] Limite dell'anonimato
> L'uso di un'identità editoriale separata non garantisce anonimato giuridico, fiscale o tecnico. Forma giuridica, eventuale raccolta fondi, obblighi antiriciclaggio, fiscalità e sicurezza operativa richiedono una verifica professionale separata prima di qualunque attivazione.

## E. Versionamento

- [ ] Versione incrementata secondo la convenzione del progetto
- [ ] [CHANGELOG](../CHANGELOG.md) aggiornato con cosa è cambiato, perché, fonti, modello o persona che ha proposto la modifica, stato
- [ ] Eventuali correzioni al dataset registrate in [06_REGISTRO_CORREZIONI](../03_VERIFICA/06_REGISTRO_CORREZIONI.md)
- [ ] La versione sostituita è archiviata e collegata, non cancellata
