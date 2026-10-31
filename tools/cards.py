"""Trading-card renderer for Red Flag.

The card frame, fonts and CSS are the SMART-Lab Science Game Kit's, copied from Methodical (its tools/cards.py) so
every kit game looks alike; only the card types and colours below are Red Flag's own.

Each card is plain HTML + inline SVG art. Every size is a multiple of the CSS variable --u, which is 1mm in
print (cards are 63 x 88 u, standard poker size) and can be set to any pixel size on screen.
"""
import html

import art
import art_claims
from art_checks import CHECK_ART
from art_flags import FLAG_ART, FAMILY_ICONS, sound_art
from i18n import Strings

e = html.escape

# Card labels by key, set by the build for each language (see tools/i18n.py and i18n/<code>/ui.json).
S = Strings({})


def L(key, **kw):
    return e(S(key, **kw))


# Every claim card shares one neutral colour (the kit's prompt-card colour), so the colour never hints at the answer.
CLAIM_COLOR = "#40402C"
FLAG_COLOR = "#B42318"
CHECK_COLOR = "#0C4A6E"
SOUND_COLOR = "#047857"
BACK_COLOR = "#0F172A"
# Red Flag's own accent on the card back (Methodical uses amber); the kit mark sits under the game name.
BACK_ACCENT = "#F87171"

FONTS_URL = ("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800"
             "&family=Barlow+Condensed:wght@600;700&family=IBM+Plex+Sans+Condensed:ital,wght@0,400;0,600;1,400&display=swap")

# Translations can run longer than English. After cards are on the page, shrink a card's main text a little at a time
# until its text box fits (down to 72%). A card that still overflows is marked, so the build check can find it.
FIT_JS = """
function fitCards(root) {
  (root || document).querySelectorAll(".tcg .tb").forEach(tb => {
    let k = 1;
    tb.style.removeProperty("--fit");
    while (tb.scrollHeight > tb.clientHeight + 1 && k > 0.72) { k -= 0.04; tb.style.setProperty("--fit", k.toFixed(2)); }
    tb.closest(".tcg").toggleAttribute("data-overflow", tb.scrollHeight > tb.clientHeight + 1);
  });
  // A name too long for its bar would be cut off; mark it too.
  (root || document).querySelectorAll(".tcg .nm b").forEach(b => b.closest(".tcg").toggleAttribute("data-name-overflow",
    b.scrollWidth > b.clientWidth + 1 || b.offsetHeight > b.parentElement.clientHeight));
  if (document.body) document.body.dataset.fitted = "1";
}
if (document.readyState === "loading") addEventListener("DOMContentLoaded", () => fitCards()); else fitCards();
if (document.fonts) document.fonts.ready.then(() => fitCards());
"""

CARD_CSS = """
.tcg { --u: var(--card-u, 1mm); --hi: color-mix(in srgb, var(--c) 72%, #fff); --lo: color-mix(in srgb, var(--c) 55%, #000);
  box-sizing: border-box; width: calc(var(--u) * 63); height: calc(var(--u) * 88); flex: none;
  border-radius: calc(var(--u) * 3.2); padding: calc(var(--u) * 2.3); position: relative; overflow: hidden;
  display: flex; flex-direction: column; gap: calc(var(--u) * 1.2); color: #16181d; text-align: start;
  background: linear-gradient(160deg, var(--hi), var(--c) 42%, var(--lo));
  box-shadow: inset 0 0 0 calc(var(--u) * .45) rgba(0,0,0,.45), inset 0 0 0 calc(var(--u) * 1) rgba(255,255,255,.14);
  font-family: "IBM Plex Sans Condensed", "Arial Narrow", sans-serif; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.tcg *, .tcg *::before { box-sizing: border-box; }
.tcg::before { content: ""; position: absolute; inset: 0; pointer-events: none; opacity: .5;
  background: repeating-linear-gradient(135deg, rgba(255,255,255,.07) 0 calc(var(--u) * .5), transparent calc(var(--u) * .5) calc(var(--u) * 1.6)); }
.tcg > * { position: relative; }
.tcg .nm { height: calc(var(--u) * 8.4); flex: none; display: flex; align-items: center; justify-content: space-between; gap: calc(var(--u) * 1.4);
  padding: 0 calc(var(--u) * 1.4) 0 calc(var(--u) * 2.2); border-radius: calc(var(--u) * 1.4);
  background: linear-gradient(#ffffff, #e4e8ee); box-shadow: inset 0 calc(var(--u) * -.45) 0 rgba(0,0,0,.14), 0 calc(var(--u) * .35) calc(var(--u) * .8) rgba(0,0,0,.35); }
.tcg .nm b { font: 800 calc(var(--u) * 4.4)/1 "Bricolage Grotesque", "Arial Narrow", sans-serif; letter-spacing: -.02em; overflow: hidden; }
.tcg .nm b.s1 { font-size: calc(var(--u) * 3.95); } .tcg .nm b.s2 { font-size: calc(var(--u) * 3.45); } .tcg .nm b.s3 { font-size: calc(var(--u) * 3.0); line-height: 1.05; } .tcg .nm b.s4 { font-size: calc(var(--u) * 2.6); line-height: 1.05; }
.tcg .attr { flex: none; width: calc(var(--u) * 5.8); height: calc(var(--u) * 5.8); border-radius: 50%; display: grid; place-items: center;
  background: radial-gradient(circle at 35% 30%, var(--hi), var(--lo)); color: #fff; box-shadow: 0 0 0 calc(var(--u) * .4) #fff, 0 0 0 calc(var(--u) * .7) rgba(0,0,0,.35); }
.tcg .attr .ic, .tcg .sb .ic { width: 62%; height: 62%; }
.tcg .lv { height: calc(var(--u) * 4.6); flex: none; display: flex; align-items: center; justify-content: space-between; gap: calc(var(--u) * 1); color: #fff;
  font: 700 calc(var(--u) * 2.5)/1 "Barlow Condensed", "Arial Narrow", sans-serif; letter-spacing: .08em; text-transform: uppercase; }
.tcg .lv > span { display: flex; align-items: center; gap: calc(var(--u) * .8); }
.tcg .sb { width: calc(var(--u) * 4.4); height: calc(var(--u) * 4.4); border-radius: 50%; display: grid; place-items: center; color: #fff;
  background: var(--s); box-shadow: 0 0 0 calc(var(--u) * .35) #fff; }
.tcg .off { opacity: .28; }
.tcg .star { color: #fde047; font-size: calc(var(--u) * 3.6); line-height: 1; text-shadow: 0 0 calc(var(--u) * .5) rgba(0,0,0,.6); }
.tcg .art { flex: none; height: calc(var(--u) * 37.5); border-radius: calc(var(--u) * .7); overflow: hidden; background: #0f172a;
  box-shadow: 0 0 0 calc(var(--u) * .55) rgba(255,255,255,.9), 0 0 0 calc(var(--u) * .9) rgba(0,0,0,.45); margin: calc(var(--u) * .5) calc(var(--u) * .9); }
.tcg .art svg { width: 100%; height: 100%; display: block; }
/* Pictures keep left-to-right coordinates in right-to-left languages, so labels stay anchored where they were drawn. */
.tcg .art svg, .tcg.back svg { direction: ltr; }
.tcg.tcg-c .art { height: calc(var(--u) * 33); }
.tcg.tcg-f .art { height: calc(var(--u) * 40); }
.tcg.tcg-k .art { height: calc(var(--u) * 40.5); }
.tcg.tcg-s .art { height: calc(var(--u) * 40.5); }
.tcg .tb { flex: 1; min-height: 0; display: flex; flex-direction: column; gap: calc(var(--u) * .7); padding: calc(var(--u) * 1.1) calc(var(--u) * 1.7) calc(var(--u) * 1);
  border-radius: calc(var(--u) * 1); background: linear-gradient(#f8f9f6, #eceee8); box-shadow: inset 0 0 0 calc(var(--u) * .3) rgba(0,0,0,.28); }
.tcg .ty { font: 700 calc(var(--u) * 2.45)/1.1 "Barlow Condensed", "Arial Narrow", sans-serif; letter-spacing: .05em; text-transform: uppercase; color: #3b3f47; }
.tcg .fx { margin: 0; font-size: calc(var(--u) * 2.95 * var(--fit, 1)); line-height: 1.24; }
.tcg.tcg-c .fx { font-size: calc(var(--u) * 3.05 * var(--fit, 1)); line-height: 1.25; }
.tcg .row { display: flex; flex-wrap: wrap; align-items: center; gap: calc(var(--u) * .6) calc(var(--u) * 1.2);
  font: 700 calc(var(--u) * 2.3 * (0.4 + 0.6 * var(--fit, 1)))/1.15 "Barlow Condensed", "Arial Narrow", sans-serif; letter-spacing: .04em; text-transform: uppercase; color: #4b5059; }
.tcg .row .k { color: #8a8f98; }
/* label then plain text: the text starts on the label's line instead of dropping below it */
.tcg .row.flow { display: block; } .tcg .row.flow .k { margin-inline-end: calc(var(--u) * .9); }
.tcg .ft { margin-top: auto; display: flex; justify-content: space-between; gap: calc(var(--u) * 1); padding-top: calc(var(--u) * .5);
  border-top: calc(var(--u) * .25) solid rgba(0,0,0,.18); font: 600 calc(var(--u) * 2.1)/1 "Barlow Condensed", "Arial Narrow", sans-serif; letter-spacing: .06em; color: #6b7079; text-transform: uppercase; }
.tcg .ref { margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: calc(var(--u) * 1.1); font-size: calc(var(--u) * 2.9); line-height: 1.22; }
.tcg .ref li { display: flex; gap: calc(var(--u) * 1); align-items: flex-start; }
.tcg .ref .sb { flex: none; width: calc(var(--u) * 3.8); height: calc(var(--u) * 3.8); }
/* card back */
.tcg.back { padding: calc(var(--u) * 3); background: radial-gradient(circle at 50% 42%, #3a1d24, #0f172a 70%); }
.tcg.back .bk { flex: 1; border-radius: calc(var(--u) * 2); border: calc(var(--u) * .5) solid rgba(248,113,113,.75); display: grid; place-items: center; overflow: hidden;
  background: repeating-conic-gradient(from 0deg at 50% 45%, rgba(255,255,255,.035) 0 10deg, transparent 10deg 20deg); }
.tcg.back svg { width: 86%; }
"""


class Ctx:
    """Lookup tables the renderers need (built once from the card data)."""

    def __init__(self, meta, flags, checks):
        self.meta = meta
        self.F = {f["id"]: f for f in flags}
        self.K = {k["id"]: k for k in checks}
        self.FAM = {f["id"]: f for f in meta["families"]}
        self.fnum = {f["id"]: i + 1 for i, f in enumerate(flags)}
        self.knum = {k["id"]: i + 1 for i, k in enumerate(checks)}
        # Check -> flags it exposes is derived from flags.checks (single source of truth).
        self.exposes = {k["id"]: [f["id"] for f in flags if k["id"] in f["checks"]] for k in checks}


def _name(s):
    n = len(s)
    cls = "s4" if n > 38 else "s3" if n > 30 else "s2" if n > 24 else "s1" if n > 18 else ""
    return f'<b class="{cls}">{e(s)}</b>'


def _art(inner, uid, color):
    return f'<div class="art">{art.frame(inner, uid, art.shade(color, .12), art.shade(color, -.45))}</div>'


def _fam_badge(cx, fid):
    f = cx.FAM[fid]
    return f'<span class="sb" style="--s:{f["color"]}" title="{e(f["name"])}">{FAMILY_ICONS[fid]}</span>'


def claim_card(cx, c):
    stars = "".join(f'<span class="star{"" if k < c["difficulty"] else " off"}">★</span>' for k in range(3))
    return f'''<div class="tcg tcg-c" style="--c:{CLAIM_COLOR}">
  <div class="nm">{_name(c["title"])}<span class="attr">{_claim_icon()}</span></div>
  <div class="lv"><span>{L("card.claim")}</span><span>{stars}</span></div>
  {_art(art_claims.draw(c), "c-" + c["id"], CLAIM_COLOR)}
  <div class="tb">
    <div class="ty">[ {e(c["field"])} ]</div>
    <p class="fx">{e(c["text"])}</p>
    <div class="ft"><span>RF-{c["id"]}</span><span>{L("card.flag_or_sound")}</span></div>
  </div>
</div>'''


def flag_card(cx, f):
    fam = cx.FAM[f["family"]]
    checks = " · ".join(e(cx.K[k]["name"]) for k in f["checks"][:2])
    return f'''<div class="tcg tcg-f" style="--c:{FLAG_COLOR}">
  <div class="nm">{_name(f["name"])}<span class="attr">{_flag_icon()}</span></div>
  <div class="lv"><span>{_fam_badge(cx, f["family"])}{e(fam["name"])}</span><span>{L("card.play_on_claim")}</span></div>
  {_art(FLAG_ART[f["id"]](), "f-" + f["id"], FLAG_COLOR)}
  <div class="tb">
    <div class="ty">[ {L("card.flag")} / {e(fam["name"])} ]</div>
    <p class="fx">{e(f["short"])}</p>
    <div class="row flow"><span class="k">{L("card.exposed_by")}</span> {checks}</div>
    <div class="ft"><span>RF-F{cx.fnum[f["id"]]:02d}</span><span>{L("card.reasoning_error")}</span></div>
  </div>
</div>'''


def check_card(cx, k):
    flags = " · ".join(e(cx.F[f]["name"]) for f in cx.exposes[k["id"]])
    return f'''<div class="tcg tcg-k" style="--c:{CHECK_COLOR}">
  <div class="nm">{_name(k["name"])}<span class="attr">{_check_icon()}</span></div>
  <div class="lv"><span>{L("card.check")}</span><span>{L("card.play_with_flag")}</span></div>
  {_art(CHECK_ART[k["id"]](), "k-" + k["id"], CHECK_COLOR)}
  <div class="tb">
    <div class="ty">[ {L("card.check")} / {L("card.move")} ]</div>
    <p class="fx">{e(k["short"])}</p>
    <div class="row flow"><span class="k">{L("card.exposes")}</span> {flags}</div>
    <div class="ft"><span>RF-K{cx.knum[k["id"]]:02d}</span><span>{L("card.the_move")}</span></div>
  </div>
</div>'''


def sound_card(cx):
    sc = cx.meta["scoring"]
    return f'''<div class="tcg tcg-s" style="--c:{SOUND_COLOR}">
  <div class="nm">{_name(S("card.sound_name"))}<span class="attr">{_sound_icon()}</span></div>
  <div class="lv"><span>{L("card.verdict")}</span><span>{L("card.play_on_claim")}</span></div>
  {_art(sound_art(), "s-sound", SOUND_COLOR)}
  <div class="tb">
    <div class="ty">[ {L("card.verdict")} / {L("card.no_flag")} ]</div>
    <p class="fx">{L("card.sound_text")}</p>
    <div class="row flow"><span class="k">{L("card.wrong_call")}</span> {L("card.sound_penalty", trap=sc["trap"])}</div>
    <div class="ft"><span>RF-S</span><span>{L("card.calibrated")}</span></div>
  </div>
</div>'''


def reference_cards(cx):
    m = cx.meta
    fams = "".join(f'<li>{_fam_badge(cx, f["id"])}<span><b>{e(f["name"])}</b> {e(f["text"])}</span></li>' for f in m["families"])
    sc = m["scoring"]

    def card(title, body, color="#334155"):
        return f'''<div class="tcg tcg-r" style="--c:{color}"><div class="nm"><b class="s1">{e(title)}</b></div>
  <div class="tb">{body}</div></div>'''
    score = (f'<ul class="ref"><li>🥇 <span><b>{L("card.best")}</b> +{sc["best"]}</span></li><li>🥈 <span><b>{L("card.defensible")}</b> +{sc["ok"]}</span></li>'
             f'<li>⚠️ <span><b>{L("card.trap")}</b> {sc["trap"]}. {L("card.trap_note")}</span></li>'
             f'<li>⚖️ <span><b>{L("card.unlisted")}</b> {L("card.appeal", unlisted=sc["unlisted"], appeal=sc["appeal_win"])}</span></li>'
             f'<li>🔍 <span><b>{L("card.check")}</b> {L("card.check_bonus", check=sc["check"])}</span></li></ul>')
    rnd = "".join(f'<li><b>{i}</b><span>{L("card.round" + str(i))}</span></li>' for i in range(1, 5))
    return [card(S("card.ref_round"), f'<ul class="ref">{rnd}</ul>'), card(S("card.ref_fams"), f'<ul class="ref">{fams}</ul>'),
            card(S("card.ref_scoring"), score)]


def card_back():
    flag = ('<path d="M38 24 V112" stroke="#F8FAFC" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M40 26 C58 18 70 34 86 28 L86 66 C70 72 58 56 40 64 Z" fill="{BACK_ACCENT}"/>')
    logo = ('<svg viewBox="0 0 120 150" xmlns="http://www.w3.org/2000/svg">' + flag
            + '<text x="60" y="96" font-size="9" fill="#94A3B8" text-anchor="middle" font-family="Barlow Condensed, sans-serif" font-weight="700" letter-spacing="2">' + L("card.back_claim") + '</text>'
            '<text x="60" y="130" font-size="19" fill="#F8FAFC" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="800" letter-spacing="1">RED FLAG</text>'
            f'<text x="60" y="143" font-size="6.4" fill="{BACK_ACCENT}" text-anchor="middle" font-family="Barlow Condensed, sans-serif" font-weight="700" letter-spacing="1.2">' + L("card.back_kit") + '</text></svg>')
    return f'<div class="tcg back" style="--c:{BACK_COLOR}"><div class="bk">{logo}</div></div>'


def _flag_icon():
    return art._icon('<path d="M5 21V4"/><path d="M5 4h11l-2 4 2 4H5" fill="currentColor"/>')


def _check_icon():
    return art._icon('<circle cx="10" cy="10" r="6"/><path d="m15 15 6 6"/><path d="M7.5 10.5 9.5 12.5 13 8"/>')


def _sound_icon():
    return art._icon('<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/>')


def _claim_icon():
    return art._icon('<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>')
