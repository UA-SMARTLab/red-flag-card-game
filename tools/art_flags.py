"""Pictures for the 30 Flag cards, the Sound card and the four flag-family icons.

Same drawing kit and style rules as tools/art.py: light line art on the card colour, INK for the main idea, ACC for
highlights, HOT for the error, DIM for background. Each picture is a diagram of the reasoning error itself.
Flag cards show about y = 6..144 of the 200 x 150 box; keep the drawing inside y = 18..132.
"""
import math

from art import (ACC, COOL, DIM, FAINT, HOT, INK, _icon, arrow, carrow, check, circle, cross, crowd, doc, globe, lcg,
                 line, magnifier, node, path, person, rect, scatter, star, text)

DARK = "#0f172a"
OK = "#86EFAC"
# The kit's rose HOT disappears on the red Flag card, so the error mark is drawn in pale pink here.
HOT = "#FFD1DC"


def _dag(x, y, label, r=15, c=INK, fill=DARK + "aa", size=15):
    return node(x, y, label, r, fill, c, size=size)


def correlation_causation():
    rnd = lcg(11)
    pts = [(24 + k * 5.2, 112 - k * 3.6 + (rnd() - .5) * 22) for k in range(14)]
    out = line([(18, 30), (18, 122), (100, 122)], DIM, 2) + scatter(pts, 3, ACC)
    out += _dag(128, 76, "X") + _dag(178, 76, "Y") + arrow(145, 76, 160, 76, INK, 3, head=7)
    out += cross(153, 76, 11, HOT, 4) + text(153, 112, "≠ CAUSE", 13, HOT)
    return out


def confounding():
    out = circle(100, 38, 17, DARK + "88", HOT, 2.5, dash="4 3") + text(100, 44, "Z", 17, HOT)
    out += arrow(86, 50, 54, 92, HOT, 3) + arrow(114, 50, 146, 92, HOT, 3)
    out += _dag(44, 106, "X") + _dag(156, 106, "Y")
    out += line([(62, 106), (138, 106)], ACC, 2.5, dash="5 5") + text(100, 128, "SAME CAUSE", 11, DIM)
    return out


def reverse_causation():
    out = _dag(46, 78, "X", 18) + _dag(154, 78, "Y", 18)
    out += arrow(68, 62, 130, 62, DIM, 2.5, dash="5 5") + text(100, 52, "CLAIMED", 10, DIM)
    out += arrow(132, 96, 70, 96, HOT, 3.5) + text(100, 118, "ACTUAL?", 12, HOT)
    return out


def shared_trend():
    out = line([(24, 30), (24, 118), (176, 118)], DIM, 2)
    out += line([(30, 104), (60, 96), (90, 84), (120, 74), (150, 60), (172, 52)], ACC, 3.5)
    out += line([(30, 112), (60, 100), (90, 92), (120, 78), (150, 70), (172, 58)], COOL, 3.5)
    out += circle(60, 50, 15, DARK + "aa", INK, 2.5) + line([(60, 50), (60, 41)], INK, 2.5) + line([(60, 50), (67, 54)], INK, 2.5)
    return out + text(118, 132, "TIME", 11, DIM)


def collider():
    out = _dag(40, 46, "X") + _dag(160, 46, "Y")
    out += arrow(52, 58, 88, 92, INK, 3) + arrow(148, 58, 112, 92, INK, 3)
    out += path("M74,96 H126 L110,116 V128 H90 V116 Z", ACC, 3, fill=DARK + "88") + text(100, 110, "C", 14, ACC)
    out += line([(58, 46), (142, 46)], HOT, 3, dash="5 5") + text(100, 36, "FAKE LINK", 11, HOT)
    return out


def immortal_time():
    out = line([(20, 92), (180, 92)], INK, 3)
    out += rect(22, 80, 66, 24, HOT, "none", 0, rx=2, o=.45) + text(55, 72, "MUST SURVIVE", 11, HOT)
    out += line([(88, 70), (88, 112)], ACC, 3.5) + text(88, 126, "TREATED", 11, ACC)
    out += circle(22, 92, 5, INK) + text(22, 126, "START", 10, DIM)
    return out + person(150, 62, 1.0, INK)


def extrapolation():
    out = line([(20, 30), (20, 118), (180, 118)], DIM, 2)
    pts = [(30 + k * 9, 108 - k * 6.2) for k in range(7)]
    out += scatter(pts, 3.5, ACC) + line([pts[0], pts[-1]], INK, 2.5)
    out += line([pts[-1], (176, 18 + 6)], HOT, 3, dash="5 5") + text(160, 50, "?", 30, HOT)
    out += rect(24, 34, 70, 88, "none", DIM, 1.5, dash="3 4") + text(58, 132, "DATA", 10, DIM)
    return out


def _mouse(x, y, c=INK):
    return (path(f"M{x - 26},{y + 8} Q{x - 24},{y - 14} {x},{y - 14} Q{x + 22},{y - 14} {x + 26},{y + 6} Z", c, 2.5, fill=DARK + "88")
            + circle(x + 12, y - 16, 6, "none", c, 2.5) + circle(x + 22, y + 1, 1.8, c)
            + path(f"M{x - 26},{y + 6} Q{x - 42},{y + 4} {x - 40},{y - 10}", c, 2.5))


def model_to_human():
    out = _mouse(56, 82) + arrow(92, 80, 124, 80, HOT, 3.5) + person(152, 80, 1.9, INK)
    out += text(108, 62, "?", 26, HOT)
    return out


def ecological():
    out = ""
    for k, (cx, cy) in enumerate([(52, 100), (100, 74), (148, 48)]):
        out += circle(cx, cy, 24, DARK + "66", DIM, 2)
        for j in range(4):
            out += circle(cx - 12 + j * 8, cy - 9 + j * 6, 2.8, ACC)
    out += line([(30, 118), (172, 30)], INK, 2.5, dash="6 5")
    out += text(160, 122, "GROUPS ↑", 11, INK) + text(160, 134, "PEOPLE ↓", 11, ACC)
    return out


def survivorship():
    plane = ("M100,30 L106,58 L176,78 L176,86 L106,78 L104,108 L122,120 L122,126 L100,120 L78,126 L78,120 L96,108 "
             "L94,78 L24,86 L24,78 L94,58 Z")
    out = path(plane, INK, 2.5, fill=DARK + "88")
    rnd = lcg(5)
    for _ in range(12):
        side = -1 if rnd() < .5 else 1
        out += circle(100 + side * (30 + 50 * rnd()), 76 + 6 * rnd(), 2.6, HOT)
    out += circle(100, 64, 9, "none", OK, 2.5, dash="3 3") + circle(100, 112, 7, "none", OK, 2.5, dash="3 3")
    return out


def unrepresentative():
    out = crowd(24, 62, 9, 2, dx=19, dy=34, s=0.82, color=lambda i, j: ACC if (i + 2 * j) % 4 == 0 else DIM)
    out += magnifier(150, 54, 18, INK)
    return out + text(60, 132, "WHO ANSWERED?", 11, HOT)


def weird():
    out = globe(100, 76, 46, DIM)
    out += circle(84, 58, 11, HOT, o=.85) + crowd(80, 60, 2, 1, dx=8, s=0.4, color=lambda i, j: INK)
    return out + text(160, 34, "ALL?", 14, HOT)


def simpsons():
    out = line([(20, 30), (20, 120), (180, 120)], DIM, 2)
    out += scatter([(36 + k * 10, 64 + k * 6) for k in range(5)], 3.4, ACC) + line([(32, 60), (82, 92)], ACC, 3)
    out += scatter([(110 + k * 10, 34 + k * 6) for k in range(5)], 3.4, COOL) + line([(106, 30), (156, 62)], COOL, 3)
    out += line([(30, 106), (172, 40)], HOT, 3, dash="6 5") + text(160, 108, "POOLED", 11, HOT)
    return out


def regression_mean():
    out = line([(20, 76), (180, 76)], DIM, 2, dash="5 5") + text(176, 70, "MEAN", 10, DIM, anchor="end")
    for x, y0, y1 in [(46, 28, 60), (82, 34, 66), (118, 122, 90), (154, 116, 86)]:
        out += circle(x, y0, 6, HOT) + arrow(x, y0 + (8 if y0 < 76 else -8), x, y1, INK, 2.5, head=7) + circle(x, y1, 4, INK)
    return out


def small_sample():
    out = line([(24, 28), (24, 118), (178, 118)], DIM, 2) + line([(24, 74), (178, 74)], DIM, 1.5, dash="4 4")
    rnd = lcg(9)
    for k in range(26):
        x = 30 + 146 * (k / 25)
        spread = 44 * (1 - k / 28) ** 2
        out += circle(x, 74 + (rnd() * 2 - 1) * spread, 3, ACC if k > 6 else HOT)
    return out + text(100, 133, "SIZE →", 11, DIM)


def base_rate():
    out = ""
    for i in range(5):
        for j in range(10):
            k = i * 10 + j
            c = HOT if k == 23 else ACC if k in (3, 17, 31, 38, 46) else FAINT
            out += circle(28 + j * 16, 36 + i * 18, 5.5, c)
    return out + text(100, 134, "1 TRUE · 5 FALSE ALARMS", 11, INK)


def inverse_probability():
    out = text(100, 62, "P(D | H)", 26, ACC, weight=700) + text(100, 112, "P(H | D)", 26, COOL, weight=700)
    out += carrow(160, 54, 186, 78, 162, 104, INK, 2.5) + text(28, 90, "≠", 30, HOT)
    return out


def not_significant():
    out = line([(20, 100), (180, 100)], DIM, 2) + line([(64, 40), (64, 110)], INK, 2, dash="4 4") + text(64, 124, "0", 12, INK)
    out += line([(44, 70), (170, 70)], ACC, 4) + circle(110, 70, 7, ACC)
    out += text(110, 50, "p = 0.09", 14, INK) + text(140, 124, "≠ NO EFFECT", 12, HOT)
    return out


def trivial_effect():
    out = line([(30, 118), (170, 118)], DIM, 2)
    out += rect(54, 50, 36, 68, INK, "none", 0, rx=2, o=.85) + rect(110, 48, 36, 70, ACC, "none", 0, rx=2)
    return out + text(100, 36, "p < 0.001", 16, HOT) + text(100, 134, "SO WHAT?", 12, INK)


def relative_risk():
    out = text(100, 52, "+100%", 34, HOT, weight=800, family="'Bricolage Grotesque', 'Arial Narrow', sans-serif")
    for i in range(2):
        for j in range(20):
            # top row: 1 case before; bottom row: 2 cases after, out of the same many people
            out += rect(22 + j * 8, 76 + i * 22, 6, 18, HOT if j <= i else FAINT, "none", 0, rx=1)
    return out + text(100, 134, "1 → 2 IN 7,000", 11, INK)


def chart_distortion():
    out = line([(36, 28), (36, 118), (176, 118)], INK, 2.5)
    out += path("M30,104 L42,100 L30,96 L42,92", HOT, 2.5)
    out += rect(60, 96, 34, 22, DIM, "none", 0, rx=2) + rect(114, 34, 34, 84, ACC, "none", 0, rx=2)
    return out + text(77, 90, "49", 12, INK) + text(131, 28, "52", 12, INK)


def overfitting():
    rnd = lcg(3)
    pts = [(28 + k * 13, 80 - k * 2 + (rnd() - .5) * 46) for k in range(12)]
    out = line([(24, 72), (176, 54)], DIM, 2.5, dash="6 5")
    d = f"M{pts[0][0]},{pts[0][1]}" + "".join(f" Q{(a[0] + b[0]) / 2},{a[1] + (b[1] - a[1]) * 2.2} {b[0]},{b[1]}" for a, b in zip(pts, pts[1:]))
    out += path(d, HOT, 2.5) + scatter(pts, 3.4, ACC)
    return out + text(100, 132, "FITS NOISE", 11, HOT)


def p_hacking():
    out = circle(26, 76, 6, INK)
    ends = [(170, 30), (170, 58), (170, 86), (170, 114)]
    for k, (x, y) in enumerate(ends):
        mid = (96, 46 if k < 2 else 106)
        out += path(f"M26,76 Q{mid[0] - 40},{mid[1]} {mid[0]},{mid[1]} T{x},{y}", ACC if k == 2 else DIM, 3 if k == 2 else 2)
        out += (star(x + 6, y, 9, ACC) if k == 2 else cross(x + 6, y, 5, DIM, 2.5))
    return out + text(150, 134, "p < .05", 12, ACC)


def multiple_tests():
    out = ""
    for i in range(4):
        for j in range(8):
            hit = (i, j) == (2, 5)
            out += rect(30 + j * 18, 30 + i * 21, 13, 13, HOT if hit else FAINT, INK if hit else "none", 2 if hit else 0, rx=2)
    return out + text(100, 132, "32 TESTS, 1 HIT", 12, INK)


def subgroup():
    out = ""
    cx, cy, r = 92, 76, 44
    for k in range(8):
        a0, a1 = k * math.pi / 4, (k + 1) * math.pi / 4
        off = 10 if k == 1 else 0
        mx, my = math.cos((a0 + a1) / 2) * off, math.sin((a0 + a1) / 2) * off
        p0 = (cx + mx + r * math.cos(a0), cy + my + r * math.sin(a0))
        p1 = (cx + mx + r * math.cos(a1), cy + my + r * math.sin(a1))
        out += path(f"M{cx + mx},{cy + my} L{p0[0]:.1f},{p0[1]:.1f} A{r},{r} 0 0 1 {p1[0]:.1f},{p1[1]:.1f} Z",
                    INK, 2, fill=HOT if k == 1 else DARK + "66")
    return out + star(168, 108, 10, ACC) + text(168, 132, "ONLY HERE?", 10, ACC)


def publication_bias():
    out = rect(40, 52, 120, 70, DARK + "88", INK, 2.5, rx=3) + line([(40, 86), (160, 86)], INK, 2)
    out += rect(88, 64, 24, 8, "none", INK, 2, rx=2) + rect(88, 98, 24, 8, "none", INK, 2, rx=2)
    out += doc(60, 20, 26, 34, ACC, 2) + star(73, 46, 6, ACC)
    out += text(150, 42, "NULLS", 11, DIM) + arrow(140, 46, 124, 64, DIM, 2)
    return out


def single_study():
    out = rect(70, 96, 60, 26, DARK + "88", INK, 2.5, rx=2) + doc(84, 46, 32, 44, ACC, 3)
    out += star(100, 34, 9, ACC) + text(40, 72, "?", 26, HOT) + text(160, 72, "?", 26, HOT)
    return out + text(100, 134, "N = 1 STUDY", 11, INK)


def surrogate():
    out = path("M30,98 A46,46 0 0 1 122,98", INK, 3) + line([(76, 98), (110, 64)], ACC, 4) + circle(76, 98, 5, ACC)
    out += text(76, 116, "MARKER ✓", 11, OK)
    heart = "M152,70 C152,58 136,56 136,68 C136,80 152,88 152,96 C152,88 168,80 168,68 C168,56 152,58 152,70 Z"
    return out + path(heart, HOT, 3, fill=DARK + "88") + text(152, 116, "PATIENT ✗", 11, HOT)


def lead_time():
    out = ""
    for k, (y, dx, lab) in enumerate([(56, 112, "NO SCREEN"), (100, 54, "SCREENED")]):
        out += line([(30, y), (170, y)], DIM, 2)
        out += circle(dx, y, 6, ACC) + cross(170, y, 6, HOT, 3)
        out += line([(dx, y - 12), (170, y - 12)], INK, 2.5) + text(30, y + 18, lab, 10, DIM, anchor="start")
    return out + text(140, 132, "SAME DEATH", 11, HOT)


def changed_yardstick():
    out = line([(20, 118), (180, 118)], DIM, 2)
    for k, h in enumerate([22, 24, 23, 25, 50, 54, 56]):
        out += rect(26 + k * 22, 118 - h, 15, h, ACC if k > 3 else INK, "none", 0, rx=1.5, o=.9)
    out += line([(108, 30), (108, 120)], HOT, 2.5, dash="5 4") + text(108, 26, "NEW DEFINITION", 11, HOT)
    return out


FLAG_ART = {k.replace("_", "-"): v for k, v in dict(globals()).items()
            if callable(v) and not k.startswith("_") and k not in {"sound_art"} and v.__module__ == __name__}


def sound_art():
    out = doc(56, 26, 62, 84, INK, 0, fill=DARK + "66")
    for i in range(5):
        out += line([(64, 52 + i * 10), (108 - (i % 2) * 12, 52 + i * 10)], DIM, 2.5)
    out += circle(128, 92, 26, "#065f46", OK, 3) + check(128, 93, 16, OK, 5)
    return out


FAMILY_ICONS = {
    "cause": _icon('<circle cx="6" cy="12" r="3"/><circle cx="18" cy="12" r="3"/><path d="M9 12h6M13 9.5l2.5 2.5-2.5 2.5"/>'),
    "sample": _icon('<circle cx="8" cy="8" r="3"/><circle cx="16" cy="8" r="3"/><path d="M2.5 20v-1.5a5 5 0 0 1 10 0V20M11.5 20v-1.5a5 5 0 0 1 10 0V20"/>'),
    "numbers": _icon('<path d="M5 19 19 5"/><circle cx="7" cy="7" r="2.5"/><circle cx="17" cy="17" r="2.5"/>'),
    "practice": _icon('<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3"/><path d="M7.5 15h9"/>'),
}
