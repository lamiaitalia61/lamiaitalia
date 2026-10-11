#!/usr/bin/env python3
"""
Genera i documenti derivati dal dataset L'Italia che vorrei.

    python strumenti/genera.py

Tutti i file prodotti hanno l'intestazione GENERATO: non si modificano a mano.
Per cambiarne il contenuto si modifica il dataset in dati/ e si rigenera.
Regola del progetto (PROTOCOLLO_MERGE): il testo e' un artefatto, la fonte di verita' e' il record.
"""
import json
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATI = ROOT / "dati"
OGGI = date.today().isoformat()

FASE_NOME = {
    0: "Fase 0 — credibilita' (primi 12 mesi)",
    1: "Fase 1 — capacita' (1-3 anni)",
    2: "Fase 2 — scambio (3-6 anni)",
    3: "Fase 3 — struttura (4-8 anni)",
}
AMBITO_TITOLO = {
    "stato-leggibile": "Stato leggibile",
    "fisco": "Fisco",
    "produttivita": "Produttivita' e dimensione d'impresa",
    "lavoro-capitale-umano": "Lavoro e capitale umano",
    "demografia": "Demografia",
    "istituzioni": "Istituzioni",
    "sicurezza": "Sicurezza",
    "immigrazione": "Immigrazione",
    "costi-politica": "Costi della politica",
    "presidenza-repubblica": "Presidenza della Repubblica",
    "accountability-eletti": "Accountability degli eletti",
    "limiti-di-mandato": "Limiti di mandato",
    "senatori-a-vita": "Senatori a vita",
    "democrazia-diretta": "Democrazia diretta",
    "trasparenza-parlamentare": "Trasparenza parlamentare",
    "giustizia": "Giustizia",
    "sanita": "Sanità",
    "capitale-civico": "Capitale civico",
    "macro": "Quadro macroeconomico",
    "energia": "Energia",
    "pnrr": "PNRR",
    "paradossi": "Paradossi strutturali",
}


def intestazione(titolo, descrizione, tags, sorgente):
    return (
        "---\n"
        f'title: "{titolo}"\n'
        "tags:\n" + "".join(f"  - {t}\n" for t in tags) +
        'status: "GENERATO"\n'
        f'generato: "{OGGI}"\n'
        f'sorgente: "{sorgente}"\n'
        "---\n\n"
        f"# {titolo}\n\n"
        "> [!warning] File generato\n"
        f"> Prodotto da `strumenti/genera.py` da `{sorgente}`. Non modificare a mano: le modifiche vanno fatte sul dataset e rigenerate.\n\n"
        f"{descrizione}\n\n"
    )


def carica():
    p = json.load(open(DATI / "proposte.json", encoding="utf-8"))["proposals"]
    f = json.load(open(DATI / "fatti.json", encoding="utf-8"))["facts"]
    return p, {x["id"]: x for x in f}, f


def scrivi(path, testo):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(testo.rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"  scritto  {path.relative_to(ROOT)}")


def scheda(p, fatti):
    out = [f"### {p['id']} — {p['leva']}\n"]
    out.append(f"- **Problema**: {p['problema']}")
    out.append(f"- **Leva (meccanismo di incentivo)**: {p['leva']}")
    if p.get("benchmark") and p["benchmark"] != "-":
        out.append(f"- **Benchmark**: {p['benchmark']}")
    out.append(f"- **Fase**: {p['fase']} — {FASE_NOME[p['fase']].split('—')[1].strip()}")
    out.append(f"- **Vincolo giuridico**: {p.get('vincolo_giuridico', 'da definire')}")
    out.append(f"- **Costo**: {p.get('costo', 'da stimare')}")
    out.append(f"- **KPI**: {p.get('kpi') or 'ASSENTE — da definire'}")
    out.append(f"- **Chi si oppone**: {p.get('oppositori') or 'NON IDENTIFICATO — da compilare'}")
    if p.get("gate"):
        out.append(f"- **Gate di attivazione**: {p['gate']}")
    if p.get("dipende_da"):
        out.append(f"- **Prerequisiti bloccanti**: {', '.join(p['dipende_da'])}")
    if p.get("rafforzata_da"):
        out.append(f"- **Rafforzata da (non bloccante)**: {', '.join(p['rafforzata_da'])}")
    if p.get("variante"):
        out.append(f"- **Variante**: {p['variante']} (alternativa incompatibile nello stesso ambito: non si sceglie in sede di dataset)")
    if p.get("rischio"):
        out.append(f"- **Rischio / obiezione piu' forte**: {p['rischio']}")
    if p.get("evidenza"):
        righe = []
        for e in p["evidenza"]:
            f = fatti.get(e)
            if not f:
                righe.append(f"`{e}` (assente)")
            else:
                marchio = "" if f["verificato"] else " **[NON VERIFICATO — vietato in pubblicazione]**"
                righe.append(f"`{e}` {f['indicatore']}: {f['valore']} ({f['fonte']}, {f['anno']}){marchio}")
        out.append("- **Evidenza**:\n" + "\n".join(f"    - {r}" for r in righe))
    else:
        out.append("- **Evidenza**: nessuna collegata — priorita' minore finche' non ne ha")
    if p.get("nota"):
        out.append(f"- **Nota**: {p['nota']}")
    out.append(f"- **Origine del record**: {p.get('fonte', '?')} · confidenza {p.get('confidenza', 'non dichiarata')} · stato `{p.get('stato', 'proposta')}`")
    return "\n".join(out) + "\n"


def genera_schede(props, fatti):
    per_ambito = defaultdict(list)
    for p in props:
        per_ambito[p["ambito"]].append(p)
    for amb, lista in sorted(per_ambito.items()):
        titolo = AMBITO_TITOLO.get(amb, amb)
        testo = intestazione(
            f"Proposte — {titolo}",
            f"{len(lista)} proposte nell'ambito `{amb}`. Ogni scheda riporta problema, leva, evidenza, oppositori, KPI, fase e vincolo giuridico.\n"
            f"Il formato editoriale di riferimento resta [la scheda proposta](../00_SCHEDA_PROPOSTA.md): le voci qui assenti "
            f"(costi dettagliati, effetti distributivi, compatibilita' UE) sono lavoro ancora da fare, non voci omesse.",
            ["l-italia-che-vorrei", "proposte", amb],
            "dati/proposte.json",
        )
        for p in sorted(lista, key=lambda x: (x["fase"], x["id"])):
            testo += scheda(p, fatti) + "\n"
        scrivi(ROOT / "02_PROPOSTE" / "SCHEDE" / f"{amb}.md", testo)


def genera_indice(props, fatti):
    testo = intestazione(
        "Indice delle proposte",
        f"{len(props)} proposte. Colonne: fase, vincolo giuridico, costo, evidenza collegata, KPI quantificato.",
        ["l-italia-che-vorrei", "proposte", "moc"],
        "dati/proposte.json",
    )
    per_ambito = defaultdict(list)
    for p in props:
        per_ambito[p["ambito"]].append(p)
    testo += "| Ambito | Proposte | Fasi | Con evidenza | Con KPI quantificato | Scheda |\n|---|---|---|---|---|---|\n"
    import re as _re
    for amb, lista in sorted(per_ambito.items()):
        fasi = ", ".join(str(x) for x in sorted({p["fase"] for p in lista}))
        con_ev = sum(1 for p in lista if p.get("evidenza"))
        con_kpi = sum(1 for p in lista if p.get("kpi") and p["kpi"] != "-" and _re.search(r"\d", p["kpi"]))
        testo += (f"| {AMBITO_TITOLO.get(amb, amb)} | {len(lista)} | {fasi} | {con_ev}/{len(lista)} | "
                  f"{con_kpi}/{len(lista)} | [Apri](SCHEDE/{amb}.md) |\n")
    testo += "\n## Varianti aperte (alternative incompatibili, non risolte per scelta)\n\n"
    var = defaultdict(list)
    for p in props:
        if p.get("variante"):
            var[p["ambito"]].append(p)
    for amb, lista in sorted(var.items()):
        testo += f"\n**{AMBITO_TITOLO.get(amb, amb)}**\n\n"
        for p in sorted(lista, key=lambda x: (x["variante"], x["id"])):
            testo += f"- `{p['variante']}` {p['id']} — {p['leva']}\n"
    testo += ("\nLe varianti restano aperte per regola: il dataset preferisce due alternative esplicite "
              "a una media indistinta che nessuno sosterrebbe.\n")
    scrivi(ROOT / "02_PROPOSTE" / "02_INDICE_PROPOSTE.md", testo)


def genera_registro_fatti(props, fatti, lista_fatti):
    usati = defaultdict(list)
    for p in props:
        for e in p.get("evidenza", []):
            usati[e].append(p["id"])
    testo = intestazione(
        "Registro dei fatti",
        f"{len(lista_fatti)} record. Un numero senza fonte e anno non entra nel dataset. "
        "I record marcati NON VERIFICATO non possono comparire in 06_PUBBLICAZIONE.",
        ["l-italia-che-vorrei", "verifica", "fatti"],
        "dati/fatti.json",
    )
    per_ambito = defaultdict(list)
    for f in lista_fatti:
        per_ambito[f.get("ambito", "senza-ambito")].append(f)
    for amb, lista in sorted(per_ambito.items()):
        testo += f"\n## {AMBITO_TITOLO.get(amb, amb)}\n\n"
        testo += "| ID | Indicatore | Valore | Fonte | Anno | Tipo | Stato | Citato da |\n|---|---|---|---|---|---|---|---|\n"
        for f in sorted(lista, key=lambda x: x["id"]):
            stato = "VERIFICATO" if f["verificato"] else "**DA VERIFICARE**"
            cit = ", ".join(usati.get(f["id"], [])) or "—"
            val = f["valore"].replace("|", "/")
            testo += (f"| `{f['id']}` | {f['indicatore']} | {val} | {f['fonte']} | {f['anno']} | "
                      f"{f.get('tipo', '?')} | {stato} | {cit} |\n")
    scrivi(ROOT / "03_VERIFICA" / "03_REGISTRO_FATTI.md", testo)


def genera_da_verificare(props, lista_fatti):
    nv = [f for f in lista_fatti if not f["verificato"]]
    testo = intestazione(
        "Fatti da verificare su fonte primaria",
        f"{len(nv)} record aperti. Finche' restano qui, le proposte che li citano come unica evidenza "
        "non possono essere presentate come documentate. Questa e' la coda di lavoro prioritaria della sezione VERIFICA.",
        ["l-italia-che-vorrei", "verifica", "blocco"],
        "dati/fatti.json",
    )
    for f in sorted(nv, key=lambda x: x["id"]):
        citanti = [p["id"] for p in props if f["id"] in p.get("evidenza", [])]
        testo += f"\n### `{f['id']}` — {f['indicatore']}\n\n"
        testo += f"- **Valore attuale nel dataset**: {f['valore']}\n"
        testo += f"- **Fonte dichiarata**: {f['fonte']} ({f['anno']}, {f.get('tipo', '?')})\n"
        testo += f"- **Proposte che lo citano**: {', '.join(citanti) if citanti else 'nessuna'}\n"
        if f.get("nota"):
            testo += f"- **Nota**: {f['nota']}\n"
        testo += "- **Cosa serve**: riferimento puntuale a documento istituzionale (titolo, data, pagina o tabella) oppure rimozione del record.\n"
    scrivi(ROOT / "03_VERIFICA" / "04_FATTI_DA_VERIFICARE.md", testo)


def genera_kpi_deboli(props):
    import re as _re
    deboli = [p for p in props if p.get("kpi") and p["kpi"] != "-" and not _re.search(r"\d", p["kpi"])]
    assenti = [p for p in props if not p.get("kpi") or p["kpi"] == "-"]
    testo = intestazione(
        "KPI da quantificare",
        "Regola del progetto: un giudizio si tiene solo se e' falsificabile, cioe' se ha una soglia e una data. "
        f"{len(deboli)} proposte hanno un indicatore senza soglia e {len(assenti)} non hanno KPI. "
        "Finche' restano cosi', sono direzioni di marcia, non impegni verificabili: e' la differenza fra un piano e un programma elettorale.",
        ["l-italia-che-vorrei", "verifica", "kpi"],
        "dati/proposte.json",
    )
    testo += "\n## Indicatore presente ma senza soglia numerica\n\n| ID | Ambito | KPI attuale | Cosa manca |\n|---|---|---|---|\n"
    for p in sorted(deboli, key=lambda x: x["id"]):
        testo += f"| `{p['id']}` | {p['ambito']} | {p['kpi']} | soglia e data |\n"
    testo += "\n## Nessun KPI\n\n| ID | Ambito | Vincolo giuridico | Ammissibile senza KPI? |\n|---|---|---|---|\n"
    for p in sorted(assenti, key=lambda x: x["id"]):
        ammissibile = "si', intervento ordinamentale" if "costituzionale" in (p.get("vincolo_giuridico") or "") else "da motivare"
        testo += f"| `{p['id']}` | {p['ambito']} | {p.get('vincolo_giuridico', '?')} | {ammissibile} |\n"
    testo += ("\n> Nessuna soglia va inventata per far tornare la tabella. Una soglia senza baseline documentata "
              "e' peggio di una casella vuota: sembra una misura e non lo e'.\n")
    scrivi(ROOT / "03_VERIFICA" / "05_KPI_DA_QUANTIFICARE.md", testo)


def genera_matrice_vincoli(props):
    testo = intestazione(
        "Matrice dei vincoli giuridici",
        "Ogni proposta classificata per fonte del diritto necessaria. La colonna che conta e' la terza: "
        "cio' che richiede legge costituzionale ha un percorso lungo, un referendum possibile e un rischio politico "
        "che non dipende dal merito della misura.",
        ["l-italia-che-vorrei", "costituzione", "vincoli"],
        "dati/proposte.json",
    )
    gruppi = defaultdict(list)
    for p in props:
        v = (p.get("vincolo_giuridico") or "non dichiarato").lower()
        if "costituzionale" in v:
            k = "Legge costituzionale (art. 138: doppia deliberazione, referendum eventuale)"
        elif "regolament" in v:
            k = "Regolamenti parlamentari (autonomia delle Camere: nessun governo puo' imporli)"
        elif "delega" in v:
            k = "Legge delega (rischio noto: i decreti attuativi che non arrivano)"
        elif "ue" in v or "internazional" in v:
            k = "Fonte UE o internazionale (non decidibile dal solo legislatore nazionale)"
        elif "vigente" in v:
            k = "Norma gia' vigente (serve attuazione, non legislazione)"
        else:
            k = "Legge ordinaria"
        gruppi[k].append(p)
    ordine = [
        "Norma gia' vigente (serve attuazione, non legislazione)",
        "Legge ordinaria",
        "Legge delega (rischio noto: i decreti attuativi che non arrivano)",
        "Regolamenti parlamentari (autonomia delle Camere: nessun governo puo' imporli)",
        "Fonte UE o internazionale (non decidibile dal solo legislatore nazionale)",
        "Legge costituzionale (art. 138: doppia deliberazione, referendum eventuale)",
    ]
    for k in ordine:
        lista = gruppi.get(k, [])
        if not lista:
            continue
        testo += f"\n## {k} — {len(lista)} proposte\n\n| ID | Ambito | Fase | Leva | Vincolo dichiarato |\n|---|---|---|---|---|\n"
        for p in sorted(lista, key=lambda x: (x["fase"], x["id"])):
            testo += f"| `{p['id']}` | {p['ambito']} | {p['fase']} | {p['leva']} | {p.get('vincolo_giuridico', '—')} |\n"
    testo += ("\n> [!note] Lettura\n> Il grosso del piano e' attivabile con legge ordinaria o con la semplice attuazione "
              "di norme gia' in vigore. La parte costituzionale e' minoritaria e concentrata in fase 3, per costruzione: "
              "e' la conseguenza operativa della regola secondo cui una riforma istituzionale votata in un clima di sfiducia "
              "viene letta come giudizio sul governo e non sul merito.\n")
    scrivi(ROOT / "04_COSTITUZIONE" / "02_MATRICE_VINCOLI.md", testo)


def genera_sequenza(props):
    testo = intestazione(
        "Sequenza di attuazione per fasi",
        "La sequenza e' la variabile piu' importante del piano: le riforme che chiedono sacrifici vengono dopo "
        "quelle che producono risultati visibili, altrimenti il consenso finisce prima del beneficio. "
        "Ogni fase si chiude con un gate: se il gate non passa, non si procede alla fase successiva.",
        ["l-italia-che-vorrei", "attuazione", "sequenza"],
        "dati/proposte.json",
    )
    byid = {p["id"]: p for p in props}
    for fase in (0, 1, 2, 3):
        lista = [p for p in props if p["fase"] == fase]
        testo += f"\n## {FASE_NOME[fase]} — {len(lista)} proposte\n\n"
        testo += "| ID | Ambito | Leva | Costo | Prerequisiti | Gate |\n|---|---|---|---|---|---|\n"
        for p in sorted(lista, key=lambda x: x["id"]):
            dep = ", ".join(p.get("dipende_da", [])) or "—"
            gate = p.get("gate", "—")
            testo += f"| `{p['id']}` | {p['ambito']} | {p['leva']} | {p.get('costo', '?')} | {dep} | {gate} |\n"
    testo += "\n## Catene di dipendenza bloccanti\n\n"
    catene = [p for p in props if p.get("dipende_da")]
    if not catene:
        testo += "Nessuna.\n"
    else:
        for p in sorted(catene, key=lambda x: (x["fase"], x["id"])):
            for d in p["dipende_da"]:
                dp = byid.get(d)
                fd = dp["fase"] if dp else "?"
                testo += f"- `{d}` (fase {fd}) deve precedere `{p['id']}` (fase {p['fase']}) — {p['leva']}\n"
    testo += "\n## Relazioni non bloccanti\n\n"
    raff = [p for p in props if p.get("rafforzata_da")]
    if not raff:
        testo += "Nessuna.\n"
    else:
        for p in sorted(raff, key=lambda x: x["id"]):
            testo += f"- `{p['id']}` e' rafforzata da {', '.join(p['rafforzata_da'])}, ma e' attivabile da sola\n"
    testo += ("\n> [!warning] Distinzione che il validatore fa rispettare\n"
              "> `dipende_da` e' un prerequisito bloccante e non puo' puntare a una fase successiva. "
              "`rafforzata_da` e' un rafforzativo e non vincola la sequenza. Confondere i due produce piani "
              "in cui tutto dipende da una riforma costituzionale che non arriva mai.\n")
    scrivi(ROOT / "05_PIANO_ATTUAZIONE" / "02_SEQUENZA_FASI.md", testo)


def main():
    props, fatti, lista_fatti = carica()
    print(f"Generazione da {len(props)} proposte e {len(lista_fatti)} fatti:")
    genera_indice(props, fatti)
    genera_schede(props, fatti)
    genera_registro_fatti(props, fatti, lista_fatti)
    genera_da_verificare(props, lista_fatti)
    genera_kpi_deboli(props)
    genera_matrice_vincoli(props)
    genera_sequenza(props)
    print("Fatto.")


if __name__ == "__main__":
    main()
