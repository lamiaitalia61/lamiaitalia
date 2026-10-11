---
title: "Protocollo di merge"
tags:
  - l-italia-che-vorrei
  - metodo
status: "ATTIVO"
versione: "1.1"
---

# Protocollo di merge

Regole per fondere contributi di autori diversi — persone o modelli — senza che il risultato diventi più lungo e meno affidabile della somma delle parti.

Adattato dal protocollo del pacchetto originario, conservato in materiale di lavoro non pubblicato.

## Principio

**Non si fondono i testi, si fondono i record.** Il testo narrativo è un artefatto generato; la fonte di verità è il dataset in `dati/`. Se due documenti dicono cose diverse, la discussione si sposta sul record, dove è decidibile.

Un merge fatto bene normalmente **riduce** il volume complessivo.

## Chiave di join

`ambito` + `leva`. Mai il titolo, mai l'ID, mai la formulazione.

La stessa idea arriva con nomi diversi — "sportello unico", "one-stop-shop", "punto di contatto unico" sono lo stesso meccanismo. Il confronto va fatto sul **meccanismo di incentivo**: chi cambia comportamento, e perché.

## Le tre sole mosse ammesse

| Mossa | Quando | Effetto |
|---|---|---|
| **Unisci** | Stessa leva, stesso ambito | Una scheda sola. Si tengono le evidenze di entrambe, il KPI più misurabile, la formulazione più precisa. `fonte` diventa multipla. |
| **Marca variante** | Stessa leva ma soluzioni incompatibili | Due record con `variante: A` e `variante: B` e i rispettivi tradeoff. **Non si sceglie.** |
| **Scarta** | Nessuna evidenza, nessun KPI, nessun oppositore identificabile | Fuori dal dataset, con `stato: scartata` e la motivazione in `nota`. |

Non è ammesso: riscrivere per "armonizzare lo stile", creare una terza proposta di compromesso non sostenuta da nessuno dei due contributi, o mediare fra due numeri discordi.

## Conflitti fattuali

Ordine di precedenza, rigido:

1. Fonte primaria istituzionale (Istat, Banca d'Italia, MEF, UPB, Corte costituzionale, Commissione UE, Eurostat, Gazzetta Ufficiale).
2. Organismo internazionale (OCSE, FMI).
3. Fonte secondaria che cita esplicitamente una primaria.
4. Tutto il resto: **non entra**.

A parità di livello vince il dato più recente. Se i due dati misurano cose diverse (debito previsto contro debito osservato), non sono in conflitto: sono due fatti distinti, con l'indicatore disambiguato.

**Il rischio principale nel fondere output di modelli diversi è la statistica plausibile ma inventata**, che sopravvive perché suona giusta e perché dopo il merge nessuno sa più da dove veniva. Il flag `verificato` esiste per questo, e `valida.py --pubblicazione` lo fa rispettare in automatico sui documenti di [06_PUBBLICAZIONE](06_PUBBLICAZIONE/00_REGOLA_PUBBLICAZIONE.md).

## Conflitti di proposta

Prima di dichiarare un conflitto, escludere i tre falsi conflitti:

- **Diverso livello di astrazione**: "riformare la PA" contro "valutare la dirigenza sui risultati". La seconda è una leva, la prima è un ambito. Si assorbe.
- **Diversa fase**: la stessa leva in fase 0 e in fase 3 è la stessa proposta con una sequenza contestata. Si discute la fase, non la leva.
- **Diverso perimetro**: nazionale contro locale. Sono due proposte, entrambe valide.

Un conflitto vero esiste solo quando le due leve **non possono coesistere**: se applichi A, B diventa impossibile. In quel caso, variante.

## Dipendenze: bloccanti e non

Introdotto nello schema 1.1 perché la confusione fra i due casi è un errore ricorrente e costoso:

- `dipende_da` — **prerequisito bloccante**: senza quello, la proposta non è attivabile. Il validatore rifiuta un prerequisito collocato in una fase successiva.
- `rafforzata_da` — **relazione non bloccante**: la proposta funziona meglio se l'altra è in vigore, ma sta in piedi da sola.

Trattare un rafforzativo come prerequisito produce piani in cui tutto dipende da una riforma costituzionale che non arriva mai. È il modo più comune in cui un piano di riforma diventa inattuabile senza che nessuno lo abbia deciso.

## Giudizi e previsioni

Si tengono solo se **falsificabili**: hanno una soglia e una data. "La produttività crescerà" esce. "Produttività oraria +1% medio annuo entro il 2035" resta, come KPI.

Una soglia non va inventata per riempire la casella. Un KPI senza baseline documentata è peggio di un KPI assente: sembra una misura e non lo è. Le proposte con indicatore senza soglia sono elencate in [05_KPI_DA_QUANTIFICARE](03_VERIFICA/05_KPI_DA_QUANTIFICARE.md) e sono lavoro aperto, non un difetto nascosto.

## Checklist di chiusura del merge

- [ ] `python strumenti/valida.py` esce con 0 errori
- [ ] `python strumenti/valida.py --pubblicazione` non segnala fatti non verificati nei documenti pubblici
- [ ] Ogni duplicato del merge report è stato risolto con una delle tre mosse
- [ ] Ogni conflitto fattuale ha una fonte vincente documentata in [06_REGISTRO_CORREZIONI](03_VERIFICA/06_REGISTRO_CORREZIONI.md)
- [ ] Le varianti A/B sono esplicite e hanno entrambe i loro tradeoff
- [ ] Il numero totale di proposte dopo il merge è stato confrontato con la somma dei due dataset: se è cresciuto della somma esatta, il merge non è stato fatto
- [ ] I documenti generati sono stati rigenerati con `python strumenti/genera.py`, non modificati a mano
