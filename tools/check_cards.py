#!/usr/bin/env python3
"""Check that no printed card overflows: render every print sheet at print size in headless Chrome or Edge and
look for cards the page itself marked (fitCards in tools/cards.py sets data-overflow when a card's text box still
overflows after shrinking to 72%, and data-name-overflow when a name doesn't fit its bar).

Usage:  python tools/build.py && python tools/check_cards.py
Needs Chrome, Chromium or Edge installed; fonts load from Google Fonts, so run it online for a faithful check.
Exit status 1 if any card overflows.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "google-chrome", "chromium", "chromium-browser", "microsoft-edge",
]


def browser():
    for c in CANDIDATES:
        path = c if os.path.isabs(c) else shutil.which(c)
        if path and os.path.exists(path):
            return path
    sys.exit("No Chrome, Chromium or Edge found. Install one, or open print/cards.html and check the cards by eye.")


def dump(exe, page):
    with tempfile.TemporaryDirectory() as profile:
        out = subprocess.run([exe, "--headless=new", "--disable-gpu", "--no-first-run", f"--user-data-dir={profile}",
                              "--virtual-time-budget=20000", "--dump-dom", page.as_uri()],
                             capture_output=True, text=True, encoding="utf-8", timeout=180)
    return out.stdout


def main():
    exe = browser()
    pages = sorted((ROOT / "print").rglob("cards.html"))
    if not pages:
        sys.exit("No print sheets found: run python tools/build.py first.")
    bad = 0
    for page in pages:
        dom = dump(exe, page)
        if 'data-fitted="1"' not in dom:
            print(f"FAIL {page.relative_to(ROOT)}: the page did not finish fitting its cards (no data-fitted mark)")
            bad += 1
            continue
        cards = re.findall(r'<div class="tcg[^"]*"[^>]*>', dom)
        over = [c for c in cards if "data-overflow" in c or "data-name-overflow" in c]
        # Name each overflowing card by the code in its footer.
        codes = re.findall(r'<div class="tcg[^"]*"[^>]*data-(?:name-)?overflow[^>]*>.*?<span>(RF-[^<]+)</span>', dom, re.S)
        print(f"{'ok  ' if not over else 'FAIL'} {page.relative_to(ROOT)}: {len(cards)} cards, {len(over)} overflowing"
              + (f": {', '.join(codes)}" if codes else ""))
        bad += len(over)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
