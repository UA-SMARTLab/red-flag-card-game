"""Translations for Red Flag (the SMART-Lab Science Game Kit system, copied from Methodical).

English is the source language. Card text lives in data/*.json; interface and card-label strings live in
i18n/en/ui.json under stable keys. Each other language has a folder i18n/<code>/ with:

  ui.json     the same keys as i18n/en/ui.json, translated (the "art" section translates labels drawn inside pictures)
  cards.json  card text keyed by card id, in the shape of the generated i18n/en/cards.json

Anything missing falls back to English, so a language can be added a little at a time.
To add a language: add it to i18n/languages.json, copy i18n/en/ui.json and i18n/en/cards.json into i18n/<code>/,
translate the values (never the keys or ids), and run python3 tools/build.py.
"""
import copy
import json
import re
from pathlib import Path

import art_claims

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# Which fields of each deck are text to translate. Everything else (ids, links, scores) stays as it is.
TEXT_FIELDS = {
    "claims": ["title", "field", "text", "why"],
    "flags": ["name", "short", "text", "example"],
    "checks": ["name", "short", "text"],
}


def load_json(path, default=None):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def languages():
    return load_json(I18N / "languages.json")


def source_cards(data):
    """The English card text in the shape every cards.json uses: {deck: {id: {field: text}}}."""
    out = {"meta": {"tagline": data["meta"]["tagline"],
                    "families": {f["id"]: {"name": f["name"], "text": f["text"]} for f in data["meta"]["families"]}}}
    for deck, fields in TEXT_FIELDS.items():
        out[deck] = {}
        for x in data[deck]:
            entry = {f: x[f] for f in fields}
            if deck == "claims":
                entry["traps"] = dict(x["traps"])
                # Labels drawn in the claim's picture, keyed by their English text.
                entry["labels"] = {lab: lab for lab in art_claims.labels_of(x["picture"])}
            out[deck][x["id"]] = entry
    return out


def write_source(data):
    """Regenerate i18n/en/cards.json from data/. It is the reference translators work from; don't edit it by hand."""
    path = I18N / "en" / "cards.json"
    path.write_text(json.dumps(source_cards(data), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def translated(data, code):
    """A deep copy of the card data with language `code` laid over it."""
    data = copy.deepcopy(data)
    if code == "en":
        return data
    tr = load_json(I18N / code / "cards.json", {})
    m = tr.get("meta", {})
    data["meta"]["tagline"] = m.get("tagline") or data["meta"]["tagline"]
    for key, items in (("families", data["meta"]["families"]),):
        for x in items:
            for f, v in m.get(key, {}).get(x["id"], {}).items():
                if v:
                    x[f] = v
    for deck, fields in TEXT_FIELDS.items():
        for x in data[deck]:
            t = tr.get(deck, {}).get(x["id"], {})
            for f in fields:
                if t.get(f):
                    x[f] = t[f]
            if deck == "claims":
                for d, reason in t.get("traps", {}).items():
                    if d in x["traps"] and reason:
                        x["traps"][d] = reason
                x["labels"] = {k: v for k, v in t.get("labels", {}).items() if v}
    return data


def ui_strings(code):
    """English strings with language `code` laid over them: {"ui": {...}, "art": {...}}."""
    base = load_json(I18N / "en" / "ui.json")
    if code == "en":
        return base
    tr = load_json(I18N / code / "ui.json", {})
    return {sec: {**base.get(sec, {}), **{k: v for k, v in tr.get(sec, {}).items() if v}} for sec in base}


def coverage(code):
    """Share of English strings that have a translation, for the build report."""
    def leaves(x):
        if isinstance(x, dict):
            for v in x.values():
                yield from leaves(v)
        elif isinstance(x, list):
            for v in x:
                yield from leaves(v)
        elif isinstance(x, str) and x:
            yield x
    src_cards = load_json(I18N / "en" / "cards.json")
    src_ui = load_json(I18N / "en" / "ui.json")
    tr_cards = load_json(I18N / code / "cards.json", {})
    tr_ui = load_json(I18N / code / "ui.json", {})

    def count(src, tr):
        total = done = 0
        if isinstance(src, dict):
            for k, v in src.items():
                t, d = count(v, (tr or {}).get(k) if isinstance(tr, dict) else None)
                total += t; done += d
        elif isinstance(src, list):
            for i, v in enumerate(src):
                t, d = count(v, tr[i] if isinstance(tr, list) and i < len(tr) else None)
                total += t; done += d
        else:
            total, done = 1, 1 if tr else 0
        return total, done
    a = count(src_cards, tr_cards)
    b = count(src_ui, tr_ui)
    return (a[0] + b[0], a[1] + b[1])


class Strings:
    """Look up an interface string by key and fill in {placeholders}: S("play.verdict_on", card=name)."""

    def __init__(self, table):
        self.table = table

    def __call__(self, key, **kw):
        s = self.table.get(key, key)
        return re.sub(r"\{(\w+)\}", lambda m: str(kw.get(m.group(1), m.group(0))), s)


CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
PLACEHOLDER = re.compile(r"\{\w+\}")


def problems(code):
    """Mistakes a translation must not contain: control characters, and {placeholders} that differ from English."""
    out = []
    for name in ("ui.json", "cards.json"):
        src = load_json(I18N / "en" / name, {})
        tr = load_json(I18N / code / name, {})

        def walk(en, t, path):
            if isinstance(t, dict):
                for k, v in t.items():
                    yield from walk(en.get(k) if isinstance(en, dict) else None, v, f"{path}/{k}")
            elif isinstance(t, list):
                for i, v in enumerate(t):
                    yield from walk(en[i] if isinstance(en, list) and i < len(en) else None, v, f"{path}/{i}")
            elif isinstance(t, str):
                yield path, en if isinstance(en, str) else None, t
        for path, en, t in walk(src, tr, name):
            if CONTROL.search(t):
                out.append(f"{code}/{path}: contains a control character")
            if en is not None and not path.endswith("_comment") and set(PLACEHOLDER.findall(en)) != set(PLACEHOLDER.findall(t)):
                out.append(f"{code}/{path}: placeholders differ from English")
    return out
