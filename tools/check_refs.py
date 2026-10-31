#!/usr/bin/env python3
"""Check every key reference and example link in data/flags.json against Crossref (needs internet).

For a DOI link, it fetches the Crossref record and checks that the first author's surname and the year in the
card's citation match the record. Other links only have to answer (HTTP status below 400).

Usage:  python tools/check_refs.py           print one line per link, then a summary
Exit status 1 if any link fails, so it can gate a release. Not part of the normal build, which works offline.
"""
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "red-flag-card-game/0.1 (reference check; mailto:abdulhamid.baghdadi@gmail.com)"}


def fold(s):
    """Lower case without accents, so 'Hernández' matches 'Hernandez'."""
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c)).lower()


def crossref(doi):
    req = urllib.request.Request("https://api.crossref.org/works/" + doi, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["message"]


def status(url):
    req = urllib.request.Request(url, headers={**UA, "User-Agent": "Mozilla/5.0 (reference check)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code


def check(url, cite=None):
    m = re.match(r"https://doi\.org/(.+)$", url)
    if not m:
        code = status(url)
        return code < 400, f"HTTP {code}"
    try:
        w = crossref(m.group(1))
    except Exception as e:  # noqa: BLE001  (report any network or lookup failure as a failed check)
        return False, f"Crossref lookup failed: {e}"
    title = re.sub(r"<[^>]+>", "", (w.get("title") or ["?"])[0])
    authors = [a.get("family") or a.get("name") or "" for a in w.get("author", [])]
    year = str(((w.get("issued") or {}).get("date-parts") or [[None]])[0][0])
    found = f"{authors[0] if authors else '(no author)'} {year}: {title} [{(w.get('container-title') or ['?'])[0]}]"
    if cite is None:
        return True, found
    ok_author = not authors or fold(authors[0].split()[-1]) in fold(cite) or fold(authors[0]) in fold(cite)
    # Journals often publish online a year before the printed issue; either year is a correct citation.
    years = {year} | {str(((w.get(k) or {}).get("date-parts") or [[None]])[0][0]) for k in ("published-print", "published-online")}
    ok_year = any(f"({y})" in cite for y in years)
    problems = ([] if ok_author else ["first author differs"]) + ([] if ok_year else ["year differs"])
    return not problems, found + ("" if not problems else "  <-- " + ", ".join(problems))


def main():
    flags = json.loads((ROOT / "data" / "flags.json").read_text(encoding="utf-8"))
    bad = 0
    for f in flags:
        for kind, url, cite in (("ref", f["ref"]["url"], f["ref"]["cite"]), ("example", f["example_url"], None)):
            ok, msg = check(url, cite)
            bad += not ok
            print(f"{'ok  ' if ok else 'FAIL'} {f['id']:<22} {kind:<7} {msg}")
            time.sleep(0.3)
    print(f"\n{bad} problem(s) in {2 * len(flags)} links")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
