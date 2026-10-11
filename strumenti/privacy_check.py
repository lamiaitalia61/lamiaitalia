#!/usr/bin/env python3
"""Audit prudente di identificatori nei file e nei metadati Git.

Non stampa i valori trovati. Non può certificare l'anonimato: nomi liberi,
copie esterne, allegati e titolarità dell'account richiedono una revisione umana.
"""

import argparse
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EMAIL = re.compile(r"(?<![\w])(?:[\w.+-]+)@(?:[\w-]+\.)+[A-Za-z]{2,}")
IPV4 = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
WIN_USER = re.compile(r"(?i)[A-Z]:[\\/]Users[\\/][^\\/\s]+")
UNIX_USER = re.compile(r"/" + r"home/[^/\s]+")
HOST_FIELD = re.compile(r"(?im)^\s*(?:username|computername|hostname)\s*[:=]\s*\S+")
URL = re.compile(r"https?://\S+")
SHARED_CHAT = re.compile(r"https?://(?:chatgpt\.com/share/|share\.gemini\.google/)")


def git(*args):
    return subprocess.check_output(
        ["git", *args], cwd=ROOT, encoding="utf-8", errors="replace"
    )


def content_issues():
    names = git("ls-files", "--cached", "--others", "--exclude-standard").splitlines()
    issues = []
    for name in names:
        path = ROOT / name
        if not path.is_file():
            continue
        try:
            source = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            issues.append((name, "non-text file; inspect embedded metadata"))
            continue
        without_urls = URL.sub("", source)
        for label, pattern, text in (
            ("email", EMAIL, source),
            ("IPv4", IPV4, source),
            ("Windows user path", WIN_USER, source),
            ("Unix user path", UNIX_USER, without_urls),
            ("host/user field", HOST_FIELD, source),
            ("shared chat link", SHARED_CHAT, source),
        ):
            if pattern.search(text) or pattern.search(name):
                issues.append((name, label))
    return issues


def history_issues():
    rows = git("log", "--all", "--format=%h%x09%an%x09%ae%x09%cn%x09%ce").splitlines()
    issues = []
    for row in rows:
        fields = row.split("\t")
        if len(fields) != 5:
            continue
        commit, author_name, author, committer_name, committer = fields
        for label, name, address in (("author", author_name, author), ("committer", committer_name, committer)):
            if name != "Redazione civica" or address != "anonimo":
                issues.append((commit, label + " identity metadata"))
    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--history", action="store_true", help="check all reachable Git commit metadata")
    args = parser.parse_args()
    issues = content_issues()
    if args.history:
        issues += history_issues()
    for location, category in issues:
        print(f"CHECK {location}: {category}")
    print(f"Privacy scan: {len(issues)} item(s) needing review")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
