#!/usr/bin/env python3
"""Smoke test of the built app (app/index.html) in headless Chrome or Edge, and screenshots for a visual check.

  python tools/test_app.py                      play every claim through the real interface and check the scoring
  python tools/test_app.py --shots <folder>     also save screenshots: desktop and phone width, light and dark,
                                                home, a claim being chosen, a result and the decks

The test page loads the app in a frame and drives it like a player: deal a claim, tap a card, press the green
"Pick this card" button, answer the bonus check. Expected results come from the key in data/claims.json, scored
by the rule in tools/build.py (tier_of). Exit status 1 on any failure.
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_cards import browser  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

DRIVER = r"""
const sleep = ms => new Promise(r => setTimeout(r, ms));
const out = { errors: [], fails: [], played: 0, sound: 0 };
const fr = document.getElementById("app");
async function run() {
  const w = fr.contentWindow, d = fr.contentDocument;
  w.addEventListener("error", e => out.errors.push(String(e.message)));
  const $ = s => d.querySelector(s), $$ = s => [...d.querySelectorAll(s)];
  const fail = m => out.fails.push(m);
  // Home
  if ($$("#hero-fan .tcg").length !== 5) fail("home: the fan should show 5 cards");
  if ($$("#home-counts .count").length !== 3) fail("home: 3 deck counts expected");
  $("#quick-card").click(); await sleep(50);
  if ($$("#quick-panel .opt").length !== 4) fail("home: quick claim should offer 4 choices");
  $("#quick-panel .opt").click(); await sleep(50);
  if (!$("#quick-verdict p")) fail("home: quick claim gave no verdict");
  // Play: every claim once, always choosing the best card through the full-screen viewer and its green button
  $('[data-go="play"]').click(); await sleep(50);
  const claims = w.eval("claims"), SC = w.eval("SC");
  const seen = new Set();
  w.eval("queue = []; stats = { score: 0, answered: 0, bestHits: 0, streak: 0, seen: {} }; nextClaim()");
  for (let n = 0; n < claims.length; n++) {
    const q = w.eval("q"); seen.add(q.id);
    const picks = $$("#panel [data-pick]").map(b => b.dataset.pick);
    if (picks.length !== 4) fail(`${q.id}: ${picks.length} choices instead of 4`);
    if (!picks.includes("sound")) fail(`${q.id}: the Sound card is missing from the choices`);
    if (!picks.includes(q.best[0])) fail(`${q.id}: the best answer is not among the choices`);
    if (new Set(picks).size !== 4) fail(`${q.id}: a choice is repeated`);
    // Score a wrong answer on every other claim, the best answer on the rest.
    const wrong = picks.find(p => p !== q.best[0]);
    const choice = n % 2 ? wrong : q.best[0];
    const expect = w.eval(`tierOf(q, ${JSON.stringify(choice)})`);
    const ref = window.EXPECT[q.id][choice] || "unlisted";
    if (expect !== ref) fail(`${q.id}: app scores ${choice} as ${expect}, the key says ${ref}`);
    const before = w.eval("stats.score");
    $$("#panel [data-pick]")[picks.indexOf(choice)].click(); await sleep(60);
    if (!$(".viewer.choosing")) { fail(`${q.id}: tapping a card did not open the viewer`); break; }
    await sleep(380);
    $(".viewer .v-pick").click(); await sleep(60);
    const head = $("#panel .result-head");
    if (!head || !head.classList.contains("r-" + ref)) fail(`${q.id}: result shows ${head && head.className}, expected r-${ref}`);
    if (w.eval("stats.score") - before !== SC[ref]) fail(`${q.id}: score changed by ${w.eval("stats.score") - before}, expected ${SC[ref]}`);
    if ($$("#panel .pick.res").length !== 4 || !$("#panel .pick.chosen")) fail(`${q.id}: the four cards don't show the result`);
    if (q.best[0] !== "sound" && !$("#panel .case a[href^='https://']")) fail(`${q.id}: no real case with a source link`);
    // bonus check: pick the key check
    const opt = $(`#review [data-k="${q.check}"]`);
    if (!opt) fail(`${q.id}: the key check is not offered`); else {
      const b2 = w.eval("stats.score"); opt.click(); await sleep(20);
      if (w.eval("stats.score") - b2 !== SC.check) fail(`${q.id}: the right check did not score +${SC.check}`);
    }
    out.played++; if (q.best[0] === "sound") out.sound++;
    if (n < claims.length - 1) { $("#b-next").click(); await sleep(30); }
  }
  if (seen.size !== claims.length) fail(`dealt ${seen.size} different claims in ${claims.length} deals; the queue should not repeat`);
  // Keyboard: Escape closes the viewer
  w.eval("nextClaim()"); await sleep(30);
  $("#panel [data-pick]").click(); await sleep(60);
  d.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape" })); w.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape" })); await sleep(300);
  if ($(".viewer")) fail("Escape did not close the viewer");
  // Decks
  $("#tab-decks").click(); await sleep(50);
  const counts = {};
  for (const k of ["claims", "flags", "checks", "sound"]) {
    $(`#deck-tabs [data-deck="${k}"]`).click(); await sleep(30);
    counts[k] = $$("#cards figure").length;
  }
  out.counts = counts;
  const exp = { claims: claims.length, flags: w.eval("flags.length"), checks: w.eval("checks.length"), sound: 1 };
  for (const k in exp) if (counts[k] !== exp[k]) fail(`decks: ${k} shows ${counts[k]} cards, expected ${exp[k]}`);
  $(`#deck-tabs [data-deck="flags"]`).click(); await sleep(30);
  if ($$("#cards a.ref").length !== exp.flags) fail("decks: every flag needs its ? link");
  w.fitCards(d); out.overflow = $$("[data-overflow],[data-name-overflow]").length;
  if (out.overflow) fail(`${out.overflow} cards overflow in the app`);
}
run().catch(e => out.fails.push("driver crashed: " + e)).finally(() => { document.body.dataset.result = JSON.stringify(out); });
"""

SHOT = r"""
const sleep = ms => new Promise(r => setTimeout(r, ms));
const fr = document.getElementById("app");
(async () => {
  const w = fr.contentWindow, d = fr.contentDocument;
  d.documentElement.dataset.theme = THEME;
  w.eval("matchMedia = () => ({ matches: true, addEventListener() {} })");   // reduced motion: no mid-animation frames
  const step = STEP;
  if (step === "home") { d.querySelector("#quick-card").click(); }
  if (step !== "home" && step !== "decks") { d.querySelector('[data-go="play"]').click(); w.eval("queue = ['C17']; nextClaim()"); }
  if (step === "viewer") { d.querySelector("#panel [data-pick]").click(); }
  if (step === "result") { const b = [...d.querySelectorAll("#panel [data-pick]")]; const best = w.eval("q.best[0]");
    b.find(x => x.dataset.pick !== best).click(); await sleep(400); d.querySelector(".v-pick").click(); await sleep(50); w.scrollTo(0, 0); }
  if (step === "decks") { d.querySelector("#tab-decks").click(); }
  await sleep(300);
})();
"""


def harness(tmp, script, width="100%", height="100%"):
    app = (ROOT / "app" / "index.html").as_uri()
    page = Path(tmp) / "harness.html"
    page.write_text(f"""<!doctype html><html><head><meta charset="utf-8"><style>html,body{{margin:0;height:100%}}
iframe{{border:0;width:{width};height:{height};display:block}}</style></head><body>
<iframe id="app" src="{app}"></iframe>
<script>window.EXPECT = EXPECT_JSON;
document.getElementById("app").addEventListener("load", () => setTimeout(() => {{ {script} }}, 400));</script></body></html>""", encoding="utf-8")
    return page


def expectations():
    """For every claim, the tier of each answer by the key in data/ (tools/build.py: tier_of)."""
    import build
    out = {}
    for c in build.claims:
        out[c["id"]] = {a: build.tier_of(c, a) for a in [f["id"] for f in build.flags] + [build.SOUND]}
    return out


def run_test(exe):
    with tempfile.TemporaryDirectory() as tmp:
        page = harness(tmp, DRIVER)
        page.write_text(page.read_text(encoding="utf-8").replace("EXPECT_JSON", json.dumps(expectations())), encoding="utf-8")
        dom = subprocess.run([exe, "--headless=new", "--disable-gpu", "--no-first-run", "--allow-file-access-from-files",
                              f"--user-data-dir={Path(tmp) / 'profile'}", "--window-size=1280,900",
                              "--virtual-time-budget=120000", "--dump-dom", page.as_uri()],
                             capture_output=True, text=True, encoding="utf-8", timeout=600).stdout
    m = re.search(r'data-result="([^"]*)"', dom)
    if not m:
        print("FAIL: the test page produced no result (the app did not load, or the driver did not finish)")
        return False
    res = json.loads(m.group(1).replace("&quot;", '"').replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">"))
    for f in res["fails"] + [f"page error: {e}" for e in res["errors"]]:
        print("FAIL", f)
    ok = not res["fails"] and not res["errors"]
    print(f"{'ok  ' if ok else 'FAIL'} played {res['played']} claims ({res['sound']} sound) through the viewer and its green button; "
          f"decks show {res.get('counts')}; {res.get('overflow')} cards overflow")
    return ok


def shots(exe, folder):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    sizes = {"desktop": (1280, 900), "phone": (390, 844), "narrow": (320, 640)}
    with tempfile.TemporaryDirectory() as tmp:
        for size, (w, h) in sizes.items():
            for theme in ("light", "dark"):
                for step in ("home", "viewer", "result", "decks"):
                    # Headless Chrome won't make a window narrower than about 500 px, so the app's frame gets the exact size.
                    page = harness(tmp, SHOT.replace("THEME", json.dumps(theme)).replace("STEP", json.dumps(step)), f"{w}px", f"{h}px")
                    page.write_text(page.read_text(encoding="utf-8").replace("EXPECT_JSON", "{}"), encoding="utf-8")
                    png = folder / f"{size}-{theme}-{step}.png"
                    subprocess.run([exe, "--headless=new", "--disable-gpu", "--no-first-run", "--hide-scrollbars",
                                    "--allow-file-access-from-files", f"--user-data-dir={Path(tmp) / 'profile'}",
                                    f"--window-size={max(w, 520)},{h + 120}", "--virtual-time-budget=15000", f"--screenshot={png}", page.as_uri()],
                                   capture_output=True, timeout=180)
                    print("saved", png)


if __name__ == "__main__":
    exe = browser()
    ok = run_test(exe)
    if "--shots" in sys.argv:
        shots(exe, sys.argv[sys.argv.index("--shots") + 1])
    sys.exit(0 if ok else 1)
