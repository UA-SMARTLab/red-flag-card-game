"""Pictures for Claim cards, drawn from the numbers in data/claims.json ("picture").

Each claim names a picture type and its data; the drawing is generic, so a new claim needs no new code. The art box
is 200 x 150, but a Claim card shows only about y = 18..132 of it (the box is wider than 4:3), so everything stays
inside that band. Labels go through `t()`, which uses the claim's translated labels when a language has them.
"""
import math

from art import ACC, COOL, DIM, FAINT, HOT, INK, circle, doc, lcg, line, path, rect, text

# The plotting area of every chart.
X0, X1, Y0, Y1 = 34, 184, 34, 110
SERIES = [ACC, COOL]


def _seed(s):
    return sum((i + 1) * ord(ch) for i, ch in enumerate(s))


def _labels(c):
    tr = c.get("labels") or {}
    return lambda s: tr.get(s, s)


def _frame(t, ylab="", xlab=""):
    out = line([(X0, Y0 - 4), (X0, Y1), (X1 + 4, Y1)], INK, 2.5)
    if ylab:
        out += text(X0 - 6, 27, t(ylab), 10, DIM.replace(".38", ".8"), anchor="start")
    if xlab:
        out += text((X0 + X1) / 2, 125, t(xlab), 10, DIM.replace(".38", ".8"))
    return out


def _fmt(v):
    return f"{v:g}" if abs(v) >= 0.1 or v == 0 else f"{v:.2f}"


def bars(c, p, t):
    data = p["bars"]
    base = p.get("base", 0)
    top = max(v for _, v in data)
    span = (top - base) or 1
    n = len(data)
    slot = (X1 - X0 - 8) / n
    w = min(34, slot * 0.62)
    # Show every bar with the same number of decimals as the most precise one (3.00 vs 3.02, not 3 vs 3.02).
    dec = max((len(f"{v:g}".split(".")[1]) if "." in f"{v:g}" else 0) for _, v in data)
    out = _frame(t, p.get("y", ""))
    for i, (lab, v) in enumerate(data):
        cx = X0 + 8 + slot * (i + 0.5)
        h = (Y1 - Y0 - 8) * (v - base) / span
        out += rect(cx - w / 2, Y1 - h, w, h, ACC if i == 0 else INK, "none", 0, rx=1.5, o=0.95 if i == 0 else 0.8)
        out += text(cx, Y1 - h - 4, f"{v:.{dec}f}", 11, INK)
        out += text(cx, 123, t(lab), 9 if n > 2 else 10, INK)
    if base:
        # A cut axis is drawn the way it appears in the wild: starting at the base value, with no break mark.
        out += text(X0 - 4, Y1 + 3, _fmt(base), 9, DIM, anchor="end")
    return out


def series(c, p, t):
    ss = p["series"]
    allv = [v for s in ss for v in s]
    dual = p.get("dual", False)
    base = p.get("base")
    out = _frame(t, p.get("y", ""), p.get("x", ""))

    def scale(s, v):
        lo, hi = (min(s), max(s)) if dual else (base if base is not None else min(allv), max(allv))
        if hi == lo:
            hi = lo + 1
        return Y1 - 6 - (Y1 - Y0 - 14) * (v - lo) / (hi - lo)
    for k, s in enumerate(ss):
        n = len(s)
        pts = [(X0 + 6 + (X1 - X0 - 12) * i / max(n - 1, 1), scale(s, v)) for i, v in enumerate(s)]
        out += line(pts, SERIES[k % 2], 3.2)
        out += "".join(circle(x, y, 2.6, SERIES[k % 2]) for x, y in pts)
    names = p.get("names", [])
    if len(names) > 1:
        x = X1
        for k, nm in reversed(list(enumerate(names))):
            out += text(x, 27, t(nm), 10, SERIES[k % 2], anchor="end")
            x -= 7 + 5.2 * len(t(nm))
    return out


def scatter(c, p, t):
    rnd = lcg(_seed(c["id"]))
    r = p["r"]
    n = p.get("n", 22)
    xs, ys = [], []
    for _ in range(n):
        x = rnd() * 2 - 1
        noise = (rnd() + rnd() + rnd() - 1.5) * 1.2
        xs.append(x)
        ys.append(r * x + math.sqrt(max(0, 1 - r * r)) * noise)
    lo, hi = min(ys), max(ys)
    out = _frame(t, p.get("y", ""), p.get("x", ""))
    for x, y in zip(xs, ys):
        px = X0 + 10 + (X1 - X0 - 20) * (x + 1) / 2
        py = Y1 - 8 - (Y1 - Y0 - 16) * (y - lo) / ((hi - lo) or 1)
        out += circle(px, py, 3.2, ACC, o=0.9)
    return out


def headline(c, p, t):
    out = rect(36, 22, 128, 106, "rgba(248,250,252,.1)", INK, 2.5, rx=3)
    out += text(100, 36, "THE DAILY CLAIM", 10, DIM, family="Georgia, serif")
    out += line([(44, 41), (156, 41)], INK, 1.5)
    words = p["words"]
    y = 60
    for w in words:
        s = t(w)
        out += text(100, y, s, min(20, 180 / max(len(s), 1)), ACC if w is words[-1] else INK, weight=800,
                    family="'Bricolage Grotesque', 'Arial Narrow', sans-serif")
        y += 21
    return out + line([(46, 119), (154, 119)], FAINT, 2)


def abstract(c, p, t):
    out = doc(52, 24, 96, 104, INK, 0, fill="rgba(248,250,252,.08)")
    for i in range(7):
        out += line([(62, 52 + i * 10), (138 - (i % 3) * 14, 52 + i * 10)], DIM, 2.5)
    out += text(100, 42, "ABSTRACT", 10, DIM)
    s = t(p["stat"])
    size = min(24, 170 / max(len(s), 1) * 1.1)
    out += (f'<g transform="rotate(-8 100 92)">' + rect(100 - len(s) * size * 0.3 - 8, 92 - size * 0.8, len(s) * size * 0.6 + 16, size * 1.25,
                                                       "rgba(15,23,42,.75)", HOT, 3, rx=4)
            + text(100, 92 + size * 0.22, s, size, HOT, weight=800, family="'Bricolage Grotesque', 'Arial Narrow', sans-serif") + "</g>")
    return out


def ci(c, p, t):
    lo, hi, est = p["lo"], p["hi"], p["est"]
    a, b = min(lo, 0) - (hi - lo) * 0.25, max(hi, 0) + (hi - lo) * 0.25

    def X(v):
        return 30 + 140 * (v - a) / (b - a)
    out = line([(26, 96), (174, 96)], INK, 2.5)
    out += line([(X(0), 40), (X(0), 104)], DIM, 2, dash="4 4") + text(X(0), 116, "0", 11, DIM)
    out += line([(X(lo), 70), (X(hi), 70)], ACC, 4) + line([(X(lo), 62), (X(lo), 78)], ACC, 3) + line([(X(hi), 62), (X(hi), 78)], ACC, 3)
    out += circle(X(est), 70, 6, ACC)
    out += text(X(lo), 54, _fmt(lo), 11, INK) + text(X(hi), 54, _fmt(hi), 11, INK)
    out += text(100, 128, t(p.get("y", "")), 10, DIM.replace(".38", ".8"))
    return out


def grid(c, p, t):
    rows, cols, hit = p["rows"], p["cols"], tuple(p["hit"])
    size, gap = 11, 4
    w = cols * (size + gap) - gap
    x0, y0 = 100 - w / 2, 30
    out = ""
    for i in range(rows):
        for j in range(cols):
            on = (i, j) == hit
            out += rect(x0 + j * (size + gap), y0 + i * (size + gap), size, size, HOT if on else FAINT, "none" if not on else INK, 1.5 if on else 0, rx=2)
    out += text(100, 126, t(p.get("label", "ONE HIT IN MANY TESTS")), 10, DIM.replace(".38", ".8"))
    return out


def forest(c, p, t):
    rows = p["rows"]
    allv = [v for r in rows for v in r] + [0]
    a, b = min(allv) - 0.15, max(allv) + 0.15

    def X(v):
        return 36 + 128 * (v - a) / (b - a)
    out = line([(X(0), 28), (X(0), 116)], DIM, 2, dash="4 4")
    step = 80 / max(len(rows), 1)
    for i, (est, lo, hi) in enumerate(rows):
        y = 36 + step * (i + 0.5)
        out += line([(X(lo), y), (X(hi), y)], INK, 2.5) + rect(X(est) - 4, y - 4, 8, 8, ACC, "none", 0, rx=1)
    out += text(X(0), 127, t("NO EFFECT"), 9, DIM.replace(".38", ".8"))
    if p.get("label"):
        out += text(36, 25, t(p["label"]), 10, DIM.replace(".38", ".8"), anchor="start")
    return out


def funnel(c, p, t):
    out = path("M100,28 L40,112 M100,28 L160,112", DIM, 2, dash="4 4") + line([(100, 28), (100, 112)], DIM, 1.5)
    rnd = lcg(_seed(c["id"]))
    for k in range(16):
        y = 36 + 72 * rnd()
        spread = (y - 28) / 84 * 55
        x = 100 + 6 + spread * rnd()
        out += circle(x, y, 3.2, ACC)
    out += text(68, 92, "?", 26, HOT)
    out += text(100, 126, t("EFFECT SIZE"), 10, DIM.replace(".38", ".8"))
    out += text(36, 27, t("PRECISION"), 10, DIM.replace(".38", ".8"), anchor="start")
    return out


DRAW = {"bars": bars, "line": series, "scatter": scatter, "headline": headline, "abstract": abstract,
        "ci": ci, "grid": grid, "forest": forest, "funnel": funnel}

# Fixed labels some picture types draw, listed so translators find them next to the claims' own labels.
FIXED_LABELS = ["THE DAILY CLAIM", "ABSTRACT", "ONE HIT IN MANY TESTS", "NO EFFECT", "EFFECT SIZE", "PRECISION"]


def labels_of(p):
    """Every label a picture draws (for translation)."""
    out = [p.get(k) for k in ("x", "y", "stat", "label") if p.get(k)]
    out += [lab for lab, _ in p.get("bars", [])] + p.get("names", []) + p.get("words", [])
    return out


def draw(c):
    p = c["picture"]
    return DRAW[p["type"]](c, p, _labels(c))
