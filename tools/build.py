#!/usr/bin/env python3
"""Validate the Red Flag card data and generate, for every language in i18n/languages.json,
the printable deck, the answer-key booklet and the web app (plus the English ANSWER_KEY.md).

Usage:  python tools/build.py                     (from anywhere)
        python tools/build.py --artifact <file>   also write a single-page copy for hosting
Only the Python standard library is needed. Run tools/check_cards.py afterwards to confirm no card overflows.
"""
import html
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
sys.path.insert(0, str(Path(__file__).resolve().parent))

import art  # noqa: E402  (needs the tools/ folder on sys.path)
import art_claims  # noqa: E402
import cards  # noqa: E402
import i18n  # noqa: E402

SOUND = "sound"          # the answer id of the "This claim is sound" card
SOUND_COPIES = 6         # one Sound card per player in table play


def load(name):
    return json.loads((DATA / f"{name}.json").read_text(encoding="utf-8"))


meta = load("meta")
claims = load("claims")
flags = load("flags")
checks = load("checks")

F = {f["id"]: f for f in flags}
K = {k["id"]: k for k in checks}
FAM = {f["id"]: f for f in meta["families"]}


# --------------------------------------------------------------------------- validation
errors, warnings = [], []

for coll, name in [(claims, "claim"), (flags, "flag"), (checks, "check")]:
    dupes = [i for i, n in Counter(x["id"] for x in coll).items() if n > 1]
    if dupes:
        errors.append(f"duplicate {name} ids: {dupes}")
if SOUND in F:
    errors.append(f"'{SOUND}' is reserved for the Sound card; rename that flag")

for f in flags:
    w = f"flag {f['id']}"
    if f["family"] not in FAM:
        errors.append(f"{w}: unknown family {f['family']}")
    for k in f["checks"]:
        if k not in K:
            errors.append(f"{w}: unknown check '{k}'")
    if not f["checks"]:
        errors.append(f"{w}: no check exposes it")
    if not (f.get("ref") or {}).get("url", "").startswith("https://"):
        errors.append(f"{w}: no key reference (ref.url, https)")
    if not f.get("example_url", "").startswith("https://"):
        errors.append(f"{w}: the example has no source link (example_url, https)")
    if len(f["short"]) > 95:
        warnings.append(f"{w}: short text is {len(f['short'])} chars (may overflow card)")
    if len(f["example"]) > 135:
        warnings.append(f"{w}: example is {len(f['example'])} chars")

for k in checks:
    if not any(k["id"] in f["checks"] for f in flags):
        warnings.append(f"check {k['id']} exposes no flag")
    if len(k["short"]) > 95:
        warnings.append(f"check {k['id']}: short text is {len(k['short'])} chars (may overflow card)")

ANSWERS = set(F) | {SOUND}
best_count = Counter()
for c in claims:
    w = f"claim {c['id']}"
    for i in c["best"] + c["ok"] + list(c["traps"]):
        if i not in ANSWERS:
            errors.append(f"{w}: unknown answer '{i}'")
    tiers = [set(c["best"]), set(c["ok"]), set(c["traps"])]
    if (tiers[0] & tiers[1]) or (tiers[0] & tiers[2]) or (tiers[1] & tiers[2]):
        errors.append(f"{w}: an answer appears in two tiers")
    if not c["best"]:
        errors.append(f"{w}: no best answer")
    sound = c["best"] == [SOUND]
    if SOUND in c["best"] and not sound:
        errors.append(f"{w}: a sound claim has only 'sound' as its best answer")
    if sound and c["ok"]:
        errors.append(f"{w}: a sound claim can't have defensible flags (any flag on it is a false alarm)")
    if SOUND in c["ok"] or SOUND in c["traps"]:
        errors.append(f"{w}: 'sound' is scored automatically on a flawed claim; don't list it")
    if not c["traps"]:
        warnings.append(f"{w}: no traps listed")
    if c["check"] not in K:
        errors.append(f"{w}: unknown check '{c['check']}'")
    elif not sound and c["check"] not in F.get(c["best"][0], {}).get("checks", []):
        warnings.append(f"{w}: key check '{c['check']}' is not listed on its best flag '{c['best'][0]}'")
    if c["picture"]["type"] not in art_claims.DRAW:
        errors.append(f"{w}: unknown picture type {c['picture']['type']}")
    if c["difficulty"] not in (1, 2, 3):
        errors.append(f"{w}: difficulty must be 1, 2 or 3")
    if len(c["text"]) > 215:
        warnings.append(f"{w}: text is {len(c['text'])} chars (may overflow card)")
    for b in c["best"]:
        best_count[b] += 1

for f in flags:
    if best_count[f["id"]] == 0:
        warnings.append(f"flag {f['id']} is never the best answer to any claim")
share = best_count[SOUND] / max(len(claims), 1)
if not 0.2 <= share <= 0.3:
    warnings.append(f"{best_count[SOUND]} of {len(claims)} claims are sound ({share:.0%}); the design aims for about one in four")


# --------------------------------------------------------------------------- languages
e = html.escape
DATA_ALL = {"meta": meta, "claims": claims, "flags": flags, "checks": checks}


def tier_of(c, answer):
    """Scoring tier of an answer to a claim. Flagging a sound claim, or calling a flawed one sound, is a trap."""
    if answer in c["best"]:
        return "best"
    if answer in c["ok"]:
        return "ok"
    if answer in c["traps"] or c["best"] == [SOUND] or answer == SOUND:
        return "trap"
    return "unlisted"


class Lang:
    """Everything one language's outputs need: translated data, its strings, and where its files go."""

    def __init__(self, info):
        self.code, self.info = info["code"], info
        self.rtl = info.get("dir") == "rtl"
        self.d = i18n.translated(DATA_ALL, self.code)
        self.F = {x["id"]: x for x in self.d["flags"]}
        self.K = {x["id"]: x for x in self.d["checks"]}
        table = i18n.ui_strings(self.code)
        self.ui, self.art = table["ui"], table["art"]
        self.S = i18n.Strings(self.ui)
        sub = "" if self.code == "en" else self.code
        self.print_dir = ROOT / "print" / sub
        self.app_dir = ROOT / "app" / sub

    def activate(self):
        """Point the card renderer at this language and return its rendering context."""
        cards.S = self.S
        art.TR = self.art
        return cards.Ctx(self.d["meta"], self.d["flags"], self.d["checks"])

    def answer_name(self, i):
        return self.S("card.sound_name") if i == SOUND else self.F[i]["name"]

    def html_attrs(self):
        return f'lang="{self.code}" dir="{"rtl" if self.rtl else "ltr"}"'

    def fonts(self):
        extra = self.info.get("font")
        return cards.FONTS_URL + (f"&family={extra.replace(' ', '+')}:wght@400;600;700" if extra else "")

    def extra_font_link(self):
        extra = self.info.get("font")
        return f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={extra.replace(" ", "+")}:wght@400;600;700&display=swap">' if extra else ""

    def lang_css(self):
        extra = self.info.get("font")
        if not extra:
            return ""
        # Scripts such as Arabic need their own font everywhere, and letter-spacing would break the joined letters.
        return (f'html[lang="{self.code}"] body, html[lang="{self.code}"] body * {{ font-family: "{extra}", "IBM Plex Sans", system-ui, sans-serif !important;'
                " letter-spacing: 0 !important; }"
                f' html[lang="{self.code}"] .tcg .nm b {{ line-height: 1.45; padding-block: .1em; }}'
                f' html[lang="{self.code}"] .tcg .nm b.s3 {{ font-size: calc(var(--u) * 2.7); line-height: 1.25; }}'
                f' html[lang="{self.code}"] .tcg .nm b.s4 {{ font-size: calc(var(--u) * 2.35); line-height: 1.25; }}')


SHEET_CSS = """
@page { size: A4; margin: 0; }
body { margin: 0; background: #d7dbe0; font-family: "IBM Plex Sans Condensed", "Arial Narrow", sans-serif; }
.sheet { width: 210mm; height: 297mm; margin: 0 auto 8mm; background: #fff; position: relative; break-after: page; display: grid; place-items: center; }
.grid { display: grid; grid-template-columns: repeat(3, 63mm); grid-auto-rows: 88mm; gap: 1mm; }
.label { position: absolute; top: 6mm; inset-inline-start: 10mm; font-size: 8pt; color: #888; }
.cover, .key { width: 210mm; min-height: 297mm; margin: 0 auto 8mm; background: #fff; padding: 16mm; box-sizing: border-box; break-after: page; font-size: 10pt; line-height: 1.45; }
.cover h1, .key h1 { font: 800 26pt/1.1 "Bricolage Grotesque", sans-serif; margin: 0 0 4mm; }
.cover table { border-collapse: collapse; margin: 4mm 0; } .cover td { padding: 1mm 6mm 1mm 0; border-bottom: .2mm solid #ddd; }
.key table { border-collapse: collapse; width: 100%; font-size: 8.4pt; }
.key th, .key td { text-align: start; vertical-align: top; padding: 1.2mm 2mm; border-bottom: .2mm solid #ddd; }
.key th { font: 700 8pt "Barlow Condensed", sans-serif; letter-spacing: .06em; text-transform: uppercase; color: #555; }
.key td.id { font-weight: 600; white-space: nowrap; } .key .trap { color: #b42318; }
.key h2 { font: 700 13pt "Barlow Condensed", sans-serif; letter-spacing: .04em; text-transform: uppercase; margin: 5mm 0 1mm; }
.langs { float: inline-end; font-size: 9pt; } .langs a { margin-inline-start: 2mm; color: #B42318; }
@media print { body { background: #fff; } .sheet, .cover, .key { margin: 0; } .label, .langs { display: none; } }
"""


def lang_links(g, langs, page_name):
    """Links to the same print page in every other language."""
    up = "" if g.code == "en" else "../"
    return '<span class="langs">' + "".join(
        f'<a href="{up}{"" if x["code"] == "en" else x["code"] + "/"}{page_name}" hreflang="{x["code"]}">{e(x["name"])}</a>'
        for x in langs if x["code"] != g.code) + "</span>"


def sheets(g, cards_html, title, per=9):
    out = []
    for k in range(0, len(cards_html), per):
        out.append(f'<section class="sheet"><div class="label">{e(g.S("print.page", deck=title, n=k // per + 1))}</div>'
                   f'<div class="grid">{"".join(cards_html[k:k + per])}</div></section>')
    return "".join(out)


def page(g, title, body):
    return f"""<!doctype html>
<html {g.html_attrs()}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title><link rel="stylesheet" href="{g.fonts()}">
<style>{cards.CARD_CSS}{SHEET_CSS}{g.lang_css()}</style></head><body>{body}<script>{cards.FIT_JS}</script></body></html>"""


def build_print(g, langs):
    cx = g.activate()
    d, S = g.d, g.S
    decks = [
        (S("print.reference"), cards.reference_cards(cx)),
        (S("deck.claims"), [cards.claim_card(cx, c) for c in d["claims"]]),
        (S("deck.flags"), [cards.flag_card(cx, f) for f in d["flags"]]),
        (S("deck.checks"), [cards.check_card(cx, k) for k in d["checks"]]),
        (S("deck.sound"), [cards.sound_card(cx)] * SOUND_COPIES),
    ]
    total = sum(len(c) for _, c in decks)
    rows = "".join(f'<tr><td>{e(n)}</td><td>{e(S("print.cards", n=len(c)))}</td><td>{e(S("print.pages", n=-(-len(c) // 9)))}</td></tr>' for n, c in decks)
    title = d["meta"]["title"]
    cover = f"""<div class="cover">{lang_links(g, langs, "cards.html")}<h1>{e(S("print.title", game=title))}</h1>
<p>{e(S("print.intro", tagline=d["meta"]["tagline"], version=d["meta"]["version"], total=total))}</p>
<table>{rows}</table>
<p>{S("print.printing_html")}</p>
<p>{S("print.answers_html")}</p></div>"""
    body = cover + "".join(sheets(g, c, n) for n, c in decks)
    g.print_dir.mkdir(parents=True, exist_ok=True)
    out = g.print_dir / "cards.html"
    out.write_text(page(g, f"{title}: print sheets", body), encoding="utf-8")
    (g.print_dir / "backs.html").write_text(page(g, f"{title}: card backs", sheets(g, [cards.card_back()] * 9, S("print.backs"))), encoding="utf-8")
    build_answer_booklet(g, langs)
    return out, total


def build_answer_booklet(g, langs):
    d, S = g.d, g.S
    body = (f'<div class="key">{lang_links(g, langs, "answer-key.html")}<h1>{e(S("print.key_title", game=d["meta"]["title"]))}</h1>'
            f'<p>{e(S("print.key_intro"))}</p>')
    head_row = "".join(f"<th>{e(S(k))}</th>" for k in ("print.key_card", "print.key_best", "print.key_ok", "print.key_traps", "print.key_why"))
    body += f'<table><tr>{head_row}</tr>'
    for c in d["claims"]:
        traps = "<br>".join(f'<span class="trap">{e(g.answer_name(i))}</span>' for i in c["traps"])
        body += (f'<tr><td class="id">{c["id"]} {e(c["title"])}</td><td>{e(", ".join(g.answer_name(i) for i in c["best"]))}</td>'
                 f'<td>{e(", ".join(g.answer_name(i) for i in c["ok"])) or "–"}</td><td>{traps}</td>'
                 f'<td>{e(c["why"])} <i>{e(S("print.key_check", check=g.K[c["check"]]["name"]))}</i></td></tr>')
    body += "</table></div>"
    (g.print_dir / "answer-key.html").write_text(page(g, S("print.key_title", game=d["meta"]["title"]), body), encoding="utf-8")


# --------------------------------------------------------------------------- answer key (markdown)
def aname(i):
    return "Sound claim" if i == SOUND else F[i]["name"]


def build_answer_key():
    sc = meta["scoring"]
    L = [f"# {meta['title']}: answer key", "",
         "Generated from `data/` by `tools/build.py`. Don't edit by hand.", "",
         f"Scoring: 🥇 best +{sc['best']} · 🥈 defensible +{sc['ok']} · ⚠️ trap {sc['trap']} · unlisted {sc['unlisted']} "
         f"(or +{sc['appeal_win']} on a successful appeal) · matching Check card +{sc['check']}. "
         "On a sound claim every flag is a trap; on a flawed claim, calling it sound is a trap.", ""]
    for c in claims:
        L += [f"## {c['id']} · {c['title']} ({c['field']}, {'★' * c['difficulty']})", "",
              f"> {c['text']}", "",
              f"- 🥇 **Best:** {', '.join(aname(i) for i in c['best'])}",
              f"- 🥈 **Defensible:** {', '.join(aname(i) for i in c['ok']) or 'none'}"]
        for i, r in c["traps"].items():
            L.append(f"- ⚠️ **Trap, {aname(i)}:** {r}")
        if c["best"] != [SOUND]:
            L.append("- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).")
        L += ["", c["why"], "", f"*Check:* **{K[c['check']]['name']}**", ""]
    L += ["## Flags", "", "| Flag | Family | Exposed by | Best answer to | Example | Key reference |", "|---|---|---|---|---|---|"]
    for f in flags:
        cs = [c["id"] for c in claims if f["id"] in c["best"]]
        L.append(f"| {f['name']} | {FAM[f['family']]['name']} | {', '.join(K[k]['name'] for k in f['checks'])} | {', '.join(cs) or '–'} "
                 f"| [{f['example']}]({f['example_url']}) | [{f['ref']['cite']}]({f['ref']['url']}) |")
    L += ["", f"Sound claims: {', '.join(c['id'] for c in claims if c['best'] == [SOUND])} ({best_count[SOUND]} of {len(claims)})."]
    (ROOT / "ANSWER_KEY.md").write_text("\n".join(L) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- web app
def fill_template(tpl, g):
    """Replace {{key}} in the page template with this language's string (escaped, unless the key ends in _html)."""
    def sub(m):
        key = m.group(1)
        if key not in g.ui:
            raise KeyError(f"app/template.html uses unknown string key {key!r}; add it to i18n/en/ui.json")
        return g.ui[key] if key.endswith("_html") else e(g.ui[key])
    return re.sub(r"\{\{([\w.]+)\}\}", sub, tpl)


def build_app(g, langs, artifact=None):
    cx = g.activate()
    d = g.d
    tpl = fill_template((ROOT / "app" / "template.html").read_text(encoding="utf-8"), g)
    rendered = {
        "claims": {c["id"]: cards.claim_card(cx, c) for c in d["claims"]},
        "flags": {f["id"]: cards.flag_card(cx, f) for f in d["flags"]},
        "checks": {k["id"]: cards.check_card(cx, k) for k in d["checks"]},
        "sound": cards.sound_card(cx),
        "back": cards.card_back(),
    }
    bundle = {**d, "cards": rendered, "exposes": cx.exposes}

    def href(x):
        return ("" if g.code == "en" else "../") + ("" if x["code"] == "en" else x["code"] + "/")

    def js(v):
        return json.dumps(v, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

    lang = {"code": g.code, "dir": "rtl" if g.rtl else "ltr",
            "langs": [{"code": x["code"], "name": x["name"], "href": href(x), "current": x["code"] == g.code} for x in langs]}
    body = (tpl.replace("/*__DATA__*/null", js(bundle))
            .replace("/*__CARD_CSS__*/", cards.CARD_CSS + g.lang_css())
            .replace("/*__UI__*/{}", js(g.ui))
            .replace("/*__LANG__*/{}", js(lang))
            .replace("/*__FIT__*/", cards.FIT_JS)
            .replace("<!--__EXTRA_FONTS__-->", g.extra_font_link()))
    # The template is page content only (a hosted copy wraps it); the local copy gets its own skeleton.
    g.app_dir.mkdir(parents=True, exist_ok=True)
    out = g.app_dir / "index.html"
    out.write_text(f'<!doctype html>\n<html {g.html_attrs()}><head><meta charset="utf-8">'
                   '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
                   '<style>[hidden]{display:none!important}body{margin:0}</style></head><body>\n'
                   + body + "\n</body></html>\n", encoding="utf-8")
    if artifact:
        Path(artifact).write_text(body, encoding="utf-8")
    return out


if __name__ == "__main__":
    for w in warnings:
        print("warning:", w)
    for err in errors:
        print("ERROR:", err)
    if errors:
        sys.exit(1)
    i18n.write_source(DATA_ALL)
    langs = i18n.languages()
    bad = [msg for info in langs if info["code"] != "en" for msg in i18n.problems(info["code"])]
    for msg in bad:
        print("ERROR:", msg)
    if bad:
        sys.exit(1)
    artifact = sys.argv[sys.argv.index("--artifact") + 1] if "--artifact" in sys.argv else None
    build_answer_key()
    for info in langs:
        g = Lang(info)
        _, n = build_print(g, langs)
        build_app(g, langs, artifact if info["code"] == "en" else None)
        if info["code"] == "en":
            print(f"ok: {len(claims)} claims ({best_count[SOUND]} sound), {len(flags)} flags, {len(checks)} checks "
                  f"({n} printable cards)")
            print("  en: source language")
        else:
            total, done = i18n.coverage(info["code"])
            print(f"  {info['code']}: {100 * done // max(total, 1)}% translated ({done}/{total} strings)")
