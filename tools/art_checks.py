"""Pictures for the 16 Check cards: each shows the move a reader makes (same kit and style rules as tools/art.py).
Keep the drawing inside y = 18..132 of the 200 x 150 box."""
from art import (ACC, COOL, DIM, FAINT, HOT, INK, arrow, check, circle, crowd, doc, line, magnifier, node, path, person,
                 rect, scatter, text, lcg)

DARK = "#0f172a"
OK = "#86EFAC"


def denominator():
    out = text(100, 66, "12", 34, INK, weight=800, family="'Bricolage Grotesque', 'Arial Narrow', sans-serif")
    out += line([(56, 80), (144, 80)], INK, 4)
    return out + text(100, 120, "OUT OF ?", 26, ACC, weight=800, family="'Bricolage Grotesque', 'Arial Narrow', sans-serif")


def comparison():
    out = crowd(28, 72, 3, 2, dx=18, dy=30, s=0.8, color=lambda i, j: ACC)
    out += crowd(136, 72, 3, 2, dx=18, dy=30, s=0.8, color=lambda i, j: DIM.replace(".38", ".75"))
    return out + text(100, 92, "VS", 22, INK) + text(46, 130, "GOT IT", 10, ACC) + text(154, 130, "DIDN'T", 10, DIM)


def causal_diagram():
    out = node(100, 36, "Z", 14, DARK + "aa", INK) + node(40, 106, "X", 14, DARK + "aa", INK) + node(160, 106, "Y", 14, DARK + "aa", INK)
    out += arrow(90, 48, 52, 94, INK, 2.5, head=7) + arrow(110, 48, 148, 94, INK, 2.5, head=7) + arrow(56, 106, 144, 106, ACC, 3, head=8)
    return out


def timeline():
    out = line([(20, 84), (180, 84)], INK, 3)
    for x, lab, c in [(40, "1", ACC), (100, "2", COOL), (160, "3", HOT)]:
        out += circle(x, 84, 9, c) + text(x, 88, lab, 11, DARK)
    out += arrow(30, 108, 170, 108, DIM, 2.5) + text(100, 128, "WHAT CAME FIRST?", 11, INK)
    return out + circle(100, 44, 16, DARK + "aa", INK, 2.5) + line([(100, 44), (100, 34)], INK, 2.5) + line([(100, 44), (108, 48)], INK, 2.5)


def over_time():
    pts = [(24 + k * 8, 92 + 14 * ((k * 7) % 5 - 2) / 2 - k * 1.2) for k in range(20)]
    out = line([(20, 28), (20, 120), (180, 120)], DIM, 2) + line(pts, ACC, 2.5)
    out += rect(130, 60, 34, 46, "none", INK, 2, dash="4 3") + text(147, 54, "THEN", 10, DIM)
    return out + text(60, 34, "WHOLE SERIES", 11, INK)


def split():
    out = rect(26, 46, 36, 72, INK, "none", 0, rx=2, o=.85) + arrow(70, 82, 98, 82, ACC, 3)
    for k, (h, c) in enumerate([(30, ACC), (24, COOL), (18, HOT)]):
        out += rect(110 + k * 24, 118 - h * 2.2, 18, h * 2.2, c, "none", 0, rx=2)
    return out + text(100, 134, "WITHIN EACH GROUP", 11, INK)


def individuals():
    out = circle(78, 78, 46, DARK + "66", DIM, 2)
    out += crowd(52, 66, 4, 2, dx=17, dy=28, s=0.7, color=lambda i, j: DIM)
    out += magnifier(120, 66, 20, INK) + person(120, 68, 0.9, ACC)
    return out


def missing():
    out = ""
    for k in range(6):
        x = 28 + k * 29
        out += (person(x, 76, 1.1, INK) if k % 2 == 0 else
                f'<g opacity=".9">{circle(x, 66, 4.8, "none", HOT, 2, dash="2 2")}'
                + path(f"M{x - 8},{86} V{78} Q{x - 8},{72} {x},{72} Q{x + 8},{72} {x + 8},{78} V{86}", HOT, 2, dash="3 3") + "</g>")
    return out + text(100, 120, "WHO ISN'T HERE?", 13, HOT)


def range_():
    rnd = lcg(4)
    pts = [(60 + 80 * rnd(), 60 + 40 * rnd()) for _ in range(14)]
    out = line([(20, 120), (180, 120)], DIM, 2) + scatter(pts, 3, ACC)
    out += path("M58,128 V132 H142 V128", INK, 2.5) + line([(56, 40), (56, 124)], INK, 2, dash="4 3") + line([(144, 40), (144, 124)], INK, 2, dash="4 3")
    return out + text(30, 80, "?", 22, HOT) + text(170, 80, "?", 22, HOT)


def prereg():
    out = doc(46, 26, 66, 92, INK, 4)
    out += rect(104, 74, 50, 32, DARK + "aa", ACC, 3, rx=4) + path("M114,74 V64 A15,15 0 0 1 144,64 V74", ACC, 3)
    return out + text(129, 96, "DATED", 10, ACC)


def replicate():
    out = ""
    for k in range(4):
        out += doc(30 + k * 34, 40 + (k % 2) * 8, 30, 40, INK, 2, fill=DARK + "88")
        out += check(45 + k * 34, 98, 10, OK if k != 2 else HOT, 3.5) if k != 2 else text(45 + k * 34, 104, "✗", 16, HOT)
    return out + text(100, 130, "AGAIN?", 12, INK)


def interval():
    out = line([(20, 100), (180, 100)], DIM, 2) + line([(80, 40), (80, 110)], INK, 2, dash="4 4")
    out += arrow(110, 70, 34, 70, ACC, 3) + arrow(110, 70, 176, 70, ACC, 3) + circle(110, 70, 7, ACC)
    return out + text(100, 128, "HOW WIDE?", 13, INK)


def effect_size():
    out = line([(30, 118), (170, 118)], DIM, 2)
    out += rect(50, 56, 34, 62, INK, "none", 0, rx=2, o=.85) + rect(116, 36, 34, 82, ACC, "none", 0, rx=2)
    out += arrow(100, 58, 100, 38, HOT, 2.5, head=6) + arrow(100, 36, 100, 56, HOT, 2.5, head=6)
    return out + text(100, 134, "HOW BIG?", 12, INK)


def outcome():
    out = circle(100, 74, 44, "none", INK, 3) + circle(100, 74, 28, "none", INK, 3) + circle(100, 74, 12, HOT)
    return out + arrow(170, 24, 108, 68, ACC, 3.5)


def new_data():
    out = rect(26, 54, 56, 44, DARK + "aa", INK, 2.5, rx=4) + text(54, 81, "MODEL", 12, INK)
    out += arrow(88, 76, 116, 76, ACC, 3)
    out += scatter([(130, 52), (146, 70), (160, 58), (138, 96), (168, 90)], 4, COOL)
    return out + text(148, 126, "UNSEEN", 11, COOL)


def axis():
    out = line([(40, 28), (40, 118), (176, 118)], INK, 3) + text(32, 122, "0", 13, ACC, anchor="end")
    out += rect(64, 82, 30, 36, DIM, "none", 0, rx=2) + rect(112, 68, 30, 50, DIM, "none", 0, rx=2)
    return out + magnifier(40, 112, 14, ACC, 3)


CHECK_ART = {"denominator": denominator, "comparison": comparison, "causal-diagram": causal_diagram, "timeline": timeline,
             "over-time": over_time, "split": split, "individuals": individuals, "missing": missing, "range": range_,
             "prereg": prereg, "replicate": replicate, "interval": interval, "effect-size": effect_size, "outcome": outcome,
             "new-data": new_data, "axis": axis}
