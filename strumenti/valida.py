#!/usr/bin/env python3
"""
Validatore del dataset L'Italia che vorrei.

    python strumenti/valida.py                      valida ed esporta i CSV in build/
    python strumenti/valida.py --merge contrib.json valida un contributo esterno e produce build/merge-report.json
    python strumenti/valida.py --strict             esce con errore anche in presenza di soli avvisi
    python strumenti/valida.py --pubblicazione      verifica che 06_PUBBLICAZIONE non citi fatti non verificati

Esce con codice 1 se ci sono errori bloccanti (o avvisi, con --strict).

Differenze rispetto al validatore del pacchetto di lavoro originario (non pubblicato):
  - controlla gli ambiti contro il vocabolario dello schema;
  - controlla che 'costo' sia nell'enum e che 'variante' sia una sola lettera;
  - verifica che un prerequisito bloccante non stia in una fase successiva;
  - distingue 'dipende_da' (bloccante) da 'rafforzata_da' (non bloccante);
  - verifica che le varianti di uno stesso ambito siano almeno due e distinte;
  - segnala i KPI privi di soglia numerica (falsificabilita');
  - segnala i temi contestati privi del campo 'rischio';
  - verifica che i documenti pubblici non citino fatti con verificato=false.
"""
import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATI = ROOT / "dati"
SCHEMA = DATI / "schema" / "l-italia-che-vorrei.schema.json"
BUILD = ROOT / "build"
PUBBL = ROOT / "06_PUBBLICAZIONE"

ID_PROP = re.compile(r"^P-[A-Z]+-[0-9]{2}(-[A-Z]{2,4})?$")
ID_FACT = re.compile(r"^F-[A-Z]+-[0-9]{2}(-[A-Z]{2,4})?$")
FASI = {0, 1, 2, 3}
REQ_PROP = ["id", "ambito", "problema", "leva", "fase", "fonte"]
REQ_FACT = ["id", "indicatore", "valore", "anno", "fonte", "verificato"]
FASE_NOME = {0: "credibilita'", 1: "capacita'", 2: "scambio", 3: "struttura"}


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def schema_bits():
    s = load(SCHEMA)
    return (
        set(s["vocabulary"]["ambiti"]),
        set(s["vocabulary"]["temi_contestati"]),
        set(s["$defs"]["proposal"]["properties"]["costo"]["enum"]),
    )


def validate(proposals, facts, ambiti, contestati, costi):
    errors, warnings = [], []
    fact_ids = {f.get("id") for f in facts}
    prop_ids = {p.get("id") for p in proposals}
    byid = {p.get("id"): p for p in proposals}

    seen = set()
    for p in proposals:
        pid = p.get("id", "<senza id>")
        for field in REQ_PROP:
            if not p.get(field) and p.get(field) != 0:
                errors.append(f"[{pid}] campo obbligatorio mancante: {field}")
        if pid in seen:
            errors.append(f"[{pid}] ID duplicato")
        seen.add(pid)
        if not ID_PROP.match(pid):
            errors.append(f"[{pid}] formato ID non valido")
        if p.get("fase") not in FASI:
            errors.append(f"[{pid}] fase non valida: {p.get('fase')}")
        if p.get("ambito") not in ambiti:
            errors.append(f"[{pid}] ambito fuori vocabolario: {p.get('ambito')}")
        if p.get("costo") and p["costo"] not in costi:
            errors.append(f"[{pid}] costo fuori enum: {p['costo']}")
        if p.get("variante") and not re.fullmatch(r"[A-Z]", p["variante"]):
            errors.append(f"[{pid}] variante deve essere una sola lettera, trovato: {p['variante']!r}")

        for ev in p.get("evidenza", []):
            if ev not in fact_ids:
                errors.append(f"[{pid}] evidenza orfana: {ev}")
        for dep in p.get("dipende_da", []):
            if dep not in prop_ids:
                errors.append(f"[{pid}] dipendenza inesistente: {dep}")
            elif byid[dep].get("fase", 0) > p.get("fase", 0):
                errors.append(
                    f"[{pid}] sequenza incoerente: fase {p.get('fase')} ({FASE_NOME.get(p.get('fase'))}) "
                    f"ma dipende da {dep} in fase {byid[dep].get('fase')} ({FASE_NOME.get(byid[dep].get('fase'))}). "
                    f"Se non e' un prerequisito bloccante, usare 'rafforzata_da'."
                )
        for r in p.get("rafforzata_da", []):
            if r not in prop_ids:
                errors.append(f"[{pid}] rafforzata_da inesistente: {r}")
            if r in p.get("dipende_da", []):
                errors.append(f"[{pid}] {r} e' insieme dipendenza bloccante e rafforzativo: scegliere")

        kpi = (p.get("kpi") or "").strip()
        if not kpi:
            warnings.append(f"[{pid}] nessun KPI: verificare se e' una proposta o un'opinione")
        elif kpi == "-":
            if p.get("vincolo_giuridico", "").startswith("legge costituzionale") is False:
                warnings.append(f"[{pid}] KPI assente ('-'): ammesso solo per interventi puramente ordinamentali")
        elif not re.search(r"\d", kpi):
            warnings.append(f"[{pid}] KPI-DEBOLE senza soglia numerica: {kpi!r}")
        if not p.get("oppositori"):
            warnings.append(f"[{pid}] nessun oppositore identificato")
        if not p.get("evidenza"):
            warnings.append(f"[{pid}] nessuna evidenza collegata")
        if p.get("ambito") in contestati and not p.get("rischio"):
            warnings.append(f"[{pid}] tema contestato ({p.get('ambito')}) senza campo 'rischio'")

    # varianti: in un ambito con varianti devono esserci almeno due lettere distinte
    lettere = defaultdict(set)
    for p in proposals:
        if p.get("variante"):
            lettere[p["ambito"]].add(p["variante"])
    for amb, lett in lettere.items():
        if len(lett) < 2:
            errors.append(
                f"[{amb}] varianti incomplete: presente solo '{sorted(lett)[0]}'. "
                f"Una variante senza alternativa non e' una variante."
            )

    seen_f = set()
    for f in facts:
        fid = f.get("id", "<senza id>")
        for field in REQ_FACT:
            if f.get(field) is None:
                errors.append(f"[{fid}] campo obbligatorio mancante: {field}")
        if fid in seen_f:
            errors.append(f"[{fid}] ID duplicato")
        seen_f.add(fid)
        if not ID_FACT.match(fid):
            errors.append(f"[{fid}] formato ID non valido")
        if f.get("ambito") and f["ambito"] not in ambiti:
            errors.append(f"[{fid}] ambito fuori vocabolario: {f['ambito']}")
        if not f.get("verificato"):
            warnings.append(f"[{fid}] NON verificato: vietato in 06_PUBBLICAZIONE finche' non e' confermato su fonte primaria")

    usati = {e for p in proposals for e in p.get("evidenza", [])}
    for fid in sorted(fact_ids - usati):
        warnings.append(f"[{fid}] fatto mai citato come evidenza: verificare se serve al dataset")

    return errors, warnings


def check_pubblicazione(facts):
    """Nessun fatto verificato=false puo' essere citato nei documenti pubblici."""
    problemi = []
    non_verificati = {f["id"] for f in facts if not f.get("verificato")}
    if not PUBBL.exists():
        return problemi
    for md in sorted(PUBBL.glob("*.md")):
        testo = md.read_text(encoding="utf-8")
        for fid in sorted(non_verificati):
            if fid in testo:
                problemi.append(f"[{md.name}] cita il fatto NON verificato {fid}")
    return problemi


def detect_conflicts(base_p, base_f, new_p, new_f):
    """Rileva sovrapposizioni tra dataset diversi. Non decide: segnala."""
    report = {"duplicati_probabili": [], "conflitti_fattuali": [], "nuovi": []}

    def norm(s):
        return re.sub(r"[^a-z ]", "", (s or "").lower())

    for np_ in new_p:
        match = None
        for bp in base_p:
            if np_.get("ambito") != bp.get("ambito"):
                continue
            a, b = set(norm(np_.get("leva")).split()), set(norm(bp.get("leva")).split())
            if a and b and len(a & b) / len(a | b) > 0.25:
                match = bp
                break
        if match:
            report["duplicati_probabili"].append({
                "nuovo": np_.get("id"), "esistente": match.get("id"),
                "ambito": np_.get("ambito"),
                "azione": "unire in una sola scheda, oppure marcare come variante A/B se incompatibili",
            })
        else:
            report["nuovi"].append(np_.get("id"))

    for nf in new_f:
        for bf in base_f:
            if nf.get("indicatore", "").lower() == bf.get("indicatore", "").lower() \
               and nf.get("valore") != bf.get("valore"):
                report["conflitti_fattuali"].append({
                    "indicatore": nf.get("indicatore"),
                    "valore_a": f"{bf.get('valore')} ({bf.get('fonte')}, {bf.get('anno')})",
                    "valore_b": f"{nf.get('valore')} ({nf.get('fonte')}, {nf.get('anno')})",
                    "azione": "vince la fonte primaria piu' recente; se una delle due non ha fonte primaria, si elimina",
                })
    return report


def export_csv(proposals, facts):
    BUILD.mkdir(exist_ok=True)
    pcols = ["id", "ambito", "problema", "leva", "evidenza", "benchmark", "oppositori",
             "kpi", "fase", "vincolo_giuridico", "costo", "fonte", "confidenza",
             "variante", "dipende_da", "rafforzata_da", "gate", "rischio", "stato", "nota"]
    with open(BUILD / "proposte.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=pcols, extrasaction="ignore")
        w.writeheader()
        for p in proposals:
            row = dict(p)
            row["evidenza"] = ";".join(p.get("evidenza", []))
            row["dipende_da"] = ";".join(p.get("dipende_da", []))
            row["rafforzata_da"] = ";".join(p.get("rafforzata_da", []))
            w.writerow(row)
    fcols = ["id", "ambito", "indicatore", "valore", "anno", "fonte", "tipo", "verificato", "nota"]
    with open(BUILD / "fatti.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fcols, extrasaction="ignore")
        w.writeheader()
        w.writerows(facts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--merge", help="file JSON di un altro modello, conforme allo schema")
    ap.add_argument("--strict", action="store_true", help="fallisce anche con soli avvisi")
    ap.add_argument("--pubblicazione", action="store_true", help="controlla 06_PUBBLICAZIONE")
    args = ap.parse_args()

    ambiti, contestati, costi = schema_bits()
    proposals = load(DATI / "proposte.json")["proposals"]
    facts = load(DATI / "fatti.json")["facts"]

    errors, warnings = validate(proposals, facts, ambiti, contestati, costi)
    print(f"Dataset: {len(proposals)} proposte, {len(facts)} fatti")
    print(f"Errori: {len(errors)} | Avvisi: {len(warnings)}")
    for e in errors:
        print("  ERRORE  " + e)
    for w in warnings:
        print("  avviso  " + w)

    pub_problemi = []
    if args.pubblicazione:
        pub_problemi = check_pubblicazione(facts)
        print(f"\nControllo 06_PUBBLICAZIONE: {len(pub_problemi)} problemi")
        for p in pub_problemi:
            print("  BLOCCANTE  " + p)

    if args.merge:
        contrib = load(args.merge)
        new_p, new_f = contrib.get("proposals", []), contrib.get("facts", [])
        e2, _ = validate(new_p, facts + new_f, ambiti, contestati, costi)
        print(f"\nContributo '{contrib.get('source_model', '?')}': "
              f"{len(new_p)} proposte, {len(new_f)} fatti, {len(e2)} errori")
        for e in e2:
            print("  ERRORE  " + e)
        rep = detect_conflicts(proposals, facts, new_p, new_f)
        BUILD.mkdir(exist_ok=True)
        with open(BUILD / "merge-report.json", "w", encoding="utf-8") as f:
            json.dump(rep, f, ensure_ascii=False, indent=2)
        print(f"  duplicati probabili: {len(rep['duplicati_probabili'])}")
        print(f"  conflitti fattuali:  {len(rep['conflitti_fattuali'])}")
        print(f"  proposte nuove:      {len(rep['nuovi'])}")
        print("  report in build/merge-report.json")
        errors += e2

    export_csv(proposals, facts)
    print("\nCSV esportati in build/")
    fallisci = bool(errors) or bool(pub_problemi) or (args.strict and bool(warnings))
    sys.exit(1 if fallisci else 0)


if __name__ == "__main__":
    main()
