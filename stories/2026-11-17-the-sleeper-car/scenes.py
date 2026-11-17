"""Scenes for The Sleeper Car. Run inside this folder: python3 scenes.py"""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

_save = save


def save(name, markup):
    for b in ("blur8", "blur30", "blur60"):
        markup = markup.replace(f'<filter id="{b}">', f'<filter id="{b}" x="-200%" y="-200%" width="500%" height="500%">')
    _save(name, markup)


DEFS = (sky("night", "#03040a", "#101a2e", "#28324a") +
        sky("dawn", "#1a2236", "#3a4258", "#5a5a68") +
        sky("cab", "#120d0b", "#1e1510", "#0c0806") +
        '<linearGradient id="curt" x1="0" x2="1"><stop offset="0" stop-color="#3a0e12"/><stop offset="0.5" stop-color="#5a161b"/>'
        '<stop offset="1" stop-color="#2a090c"/></linearGradient>'
        '<linearGradient id="curtlit" x1="0" x2="1"><stop offset="0" stop-color="#5a1a16"/><stop offset="0.5" stop-color="#8a2a22"/>'
        '<stop offset="1" stop-color="#4a120e"/></linearGradient>'
        '<linearGradient id="floor" x1="0" y1="0" y2="1"><stop offset="0" stop-color="#1a1210"/><stop offset="1" stop-color="#2e1f18"/></linearGradient>'
        '<linearGradient id="blanket" x1="0" y1="0" y2="1"><stop offset="0" stop-color="#3a3f5a"/><stop offset="1" stop-color="#1c1f30"/></linearGradient>')


def pine(x, base, h, color="#05070c"):
    pts = []
    tiers = 6
    for i in range(tiers):
        y = base - h * (i / tiers)
        w = h * 0.32 * (1 - i / tiers) + 18
        pts.append(f'<polygon points="{x - w},{y} {x},{y - h / tiers * 1.7} {x + w},{y}" fill="{color}"/>')
    return f'<rect x="{x - 8}" y="{base - 20}" width="16" height="30" fill="{color}"/>' + "".join(pts)


def forest(base, n, hrange, color, x0=0, x1=W):
    return "".join(pine(rnd.randint(x0, x1), base + rnd.randint(-10, 10), rnd.randint(*hrange), color) for _ in range(n))


def snowfall(n, op=0.7, ymax=H):
    return "".join(f'<circle cx="{rnd.randint(0, W)}" cy="{rnd.randint(0, ymax)}" r="{rnd.choice([1.5, 2.2, 3, 4])}" '
                   f'fill="#e8eef8" opacity="{rnd.uniform(0.25, op):.2f}"/>' for _ in range(n))


def curtain(x, y, w, h, fill="url(#curt)", folds=7, open_frac=0.0):
    """Heavy berth curtain on a rail; open_frac bunches it to the left."""
    cw = w * (1 - open_frac * 0.8)
    out = f'<rect x="{x - 10}" y="{y - 14}" width="{w + 20}" height="12" rx="6" fill="#8a7a58"/>'
    out += f'<rect x="{x}" y="{y}" width="{cw}" height="{h}" fill="{fill}"/>'
    for i in range(1, folds):
        fx = x + cw * i / folds
        out += f'<path d="M{fx} {y} q{8} {h / 2} {-4} {h}" stroke="#1a0507" stroke-width="{cw / folds * .35:.0f}" fill="none" opacity="0.55"/>'
    out += "".join(f'<circle cx="{x + cw * i / folds + 4}" cy="{y + 4}" r="7" fill="#b0a070"/>' for i in range(folds + 1))
    return out


# S1 — the night train crossing a snowy pine forest, lit sleeper windows
cars = ""
for c, (x0, x1) in enumerate(((180, 760), (780, 1360), (1380, 1960))):
    cars += f'<rect x="{x0}" y="560" width="{x1 - x0}" height="230" rx="18" fill="#0c0f18"/>'
    cars += f'<rect x="{x0}" y="560" width="{x1 - x0}" height="16" rx="8" fill="#1a1f2c"/>'
    cars += f'<rect x="{x0}" y="740" width="{x1 - x0}" height="10" fill="#5a161b"/>'
    for k in range(5):
        wx = x0 + 40 + k * ((x1 - x0 - 80) / 5)
        lit = not (c == 1 and k == 2)
        cars += lit_window(wx, 610, 70, 70, "#ffb54a" if lit else "#1c1e2c", "#0c0f18") if lit else f'<rect x="{wx}" y="610" width="70" height="70" fill="#151826"/>'
    for wx in (x0 + 60, x1 - 120):
        cars += f'<circle cx="{wx}" cy="800" r="34" fill="#06070b"/><circle cx="{wx + 70}" cy="800" r="34" fill="#06070b"/>'
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>{stars(160, 450)}{moon(1180, 190, 70)}
{forest(560, 40, (180, 320), "#0a0e18")}
{fog(560, op=0.16)}
<path d="M0 820 L1920 820 L1920 1080 L0 1080Z" fill="#c8d0e0" opacity="0.18"/>
<rect x="0" y="815" width="1920" height="14" fill="#1a1a22"/>
{"".join(f'<rect x="{x}" y="826" width="34" height="10" fill="#14141a"/>' for x in range(0, 1920, 52))}
{cars}
{glow(960, 650, 420, "#ffb54a", 0.12)}
<path d="M0 860 C500 840 1300 850 1920 845 L1920 1080 L0 1080Z" fill="#dfe5ef" opacity="0.32"/>
{forest(1080, 4, (160, 240), "#04060a", 0, 520)}{forest(1080, 4, (160, 240), "#04060a", 1400, 1920)}
{snowfall(260)}
''', DEFS))

# S2 — inside the berth: window with snow, curtain open, the rule card
card = (f'<g transform="translate(0 -150) rotate(-4 900 760)"><rect x="750" y="690" width="320" height="170" fill="#e8dcc0"/>'
        f'<rect x="762" y="702" width="296" height="146" fill="none" stroke="#8a1c1c" stroke-width="3"/>'
        f'<text x="910" y="752" text-anchor="middle" font-family="{SERIF}" font-size="26" fill="#2a1a12">AFTER MIDNIGHT</text>'
        f'<text x="910" y="796" text-anchor="middle" font-family="{SERIF}" font-size="26" fill="#2a1a12">KEEP YOUR</text>'
        f'<text x="910" y="834" text-anchor="middle" font-family="{SERIF}" font-size="26" fill="#8a1c1c" font-weight="bold">CURTAIN CLOSED</text></g>')
save("s2", svg(f'''
<rect width="{W}" height="{H}" fill="url(#cab)"/>
<rect x="560" y="140" width="800" height="440" rx="40" fill="#2a1d14"/>
<rect x="600" y="175" width="720" height="370" rx="30" fill="url(#night)"/>
<clipPath id="win2"><rect x="600" y="175" width="720" height="370" rx="30"/></clipPath>
<g clip-path="url(#win2)">{moon(1150, 260, 40)}{forest(545, 26, (120, 260), "#060910", 560, 1360)}{snowfall(120, 0.9, 560)}</g>
<rect x="600" y="175" width="720" height="370" rx="30" fill="none" stroke="#4a3624" stroke-width="10"/>
{curtain(470, 120, 980, 560, folds=9, open_frac=0.92)}
{curtain(1300, 120, 180, 560, folds=3)}
<rect x="440" y="640" width="1040" height="440" fill="#1e140e"/>
<path d="M440 660 L1480 660 L1480 1080 L440 1080Z" fill="url(#blanket)"/>
<path d="M480 700 q240 -60 480 0 q240 50 480 -10" stroke="#11131e" stroke-width="12" fill="none"/>
<ellipse cx="620" cy="690" rx="150" ry="60" fill="#d8d4c8"/>
<rect x="1140" y="800" width="160" height="210" fill="#3a1410" transform="rotate(8 1220 900)"/>
{card}
{glow(1400, 300, 120, "#ffb54a", 0.5)}<circle cx="1400" cy="300" r="20" fill="#ffd38a"/>
<rect x="1385" y="300" width="30" height="40" fill="#5a4630"/>
''', DEFS))

# S3 — the stopped train, out the window: snow, black pines (and something between the trees)
save("s3", svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>{stars(90, 400, 0.5)}
{forest(700, 30, (300, 520), "#0b1018")}
{fog(700, op=0.2)}
<path d="M0 720 L1920 720 L1920 1080 L0 1080Z" fill="#c8d2e2" opacity="0.28"/>
{forest(760, 24, (380, 600), "#04060a")}
{figure(1080, 760, 300, "#020204")}
{eyes(1080, 494, gap=12, r=3)}
{snowfall(200, 0.8)}
<g fill="#1e140e"><rect x="0" y="0" width="1920" height="90"/><rect x="0" y="990" width="1920" height="90"/>
<rect x="0" y="0" width="560" height="1080"/><rect x="1360" y="0" width="560" height="1080"/></g>
<rect x="560" y="90" width="800" height="900" rx="50" fill="none" stroke="#3a2a1c" stroke-width="40"/>
<rect x="560" y="90" width="800" height="900" rx="50" fill="#dfe8f5" opacity="0.04"/>
<path d="M600 140 L760 140 L620 400Z" fill="#ffffff" opacity="0.05"/>
''', DEFS))


def corridor(dawn=False, figure_at=None, opened=(), porter=False):
    """Sleeper car aisle seen from one end: curtains on both sides converging to the far door."""
    vx, vy = 960, 470
    base = "url(#dawn)" if dawn else "#0a0708"
    out = f'<rect width="{W}" height="{H}" fill="{base}"/>'
    out += f'<polygon points="0,0 1920,0 {vx + 120},{vy - 170} {vx - 120},{vy - 170}" fill="#140e0c"/>'
    out += f'<polygon points="0,1080 1920,1080 {vx + 120},{vy + 170} {vx - 120},{vy + 170}" fill="url(#floor)"/>'
    out += f'<polygon points="{vx - 380},1080 {vx + 380},1080 {vx + 60},{vy + 170} {vx - 60},{vy + 170}" fill="#4a1418" opacity="0.8"/>'
    # ceiling lamps
    for t in (0.25, 0.5, 0.72, 0.88):
        lx = vx; ly = vy - 170 - (1 - t) * 430 * 0.0 - (1 - t) * 300
        r = 40 * (1 - t) + 8
        col = "#cfd6e0" if dawn else "#ffb54a"
        out += f'<ellipse cx="{lx}" cy="{ly}" rx="{r * 2}" ry="{r * .5}" fill="{col}" opacity="0.9"/>' + glow(lx, ly + r, r * 4, col, 0.35)
    # side curtains (left & right) in perspective
    for side in (-1, 1):
        for i in range(5):
            t0 = i / 5; t1 = (i + 0.85) / 5
            def px(t): return vx + side * (960 - (960 - 120) * t) * 1.0
            def ty(t): return 0 + (vy - 170) * t
            def by(t): return 1080 - (1080 - (vy + 170)) * t
            x0, x1 = px(t0 * 0.92), px(t1 * 0.92)
            top0, top1, bot0, bot1 = ty(t0 * .92) + 60 * (1 - t0), ty(t1 * .92) + 60 * (1 - t1), by(t0 * .92) - 120 * (1 - t0), by(t1 * .92) - 120 * (1 - t1)
            is_open = (side, i) in opened
            fill = "#0e0a0a" if is_open else ("url(#curtlit)" if not dawn else "#6a2a28")
            out += f'<polygon points="{x0},{top0} {x1},{top1} {x1},{bot1} {x0},{bot0}" fill="{fill}"/>'
            if is_open:
                out += f'<polygon points="{x0},{top0} {x0 + (x1 - x0) * .2},{top0 + (top1 - top0) * .2} {x0 + (x1 - x0) * .2},{bot0 + (bot1 - bot0) * .2} {x0},{bot0}" fill="#5a161b"/>'
            else:
                for f in range(1, 5):
                    fx = x0 + (x1 - x0) * f / 5
                    fy0 = top0 + (top1 - top0) * f / 5; fy1 = bot0 + (bot1 - bot0) * f / 5
                    out += f'<line x1="{fx}" y1="{fy0}" x2="{fx}" y2="{fy1}" stroke="#1a0406" stroke-width="{max(2, 10 * (1 - t0))}" opacity="0.5"/>'
            out += f'<line x1="{x0}" y1="{top0}" x2="{x1}" y2="{top1}" stroke="#8a7a58" stroke-width="{max(2, 10 * (1 - t0))}"/>'
    # far door
    dcol = "#0a0c14" if not dawn else "#3a4256"
    out += f'<rect x="{vx - 70}" y="{vy - 150}" width="140" height="310" fill="#2a1d14"/>'
    out += f'<rect x="{vx - 55}" y="{vy - 135}" width="110" height="290" fill="{dcol}"/>'
    if figure_at:
        out += glow(vx, vy, 160, "#6a7aa0", 0.25)
        out += figure(vx, vy + 160, figure_at, "#010102")
        out += eyes(vx, vy + 160 - figure_at * .9, gap=10, r=2.6)
    if porter:
        # porter in cap and coat standing mid-aisle
        px_, base_ = 1020, 900
        out += (f'<g fill="#121624"><path d="M{px_ - 70} {base_} L{px_ - 60} {base_ - 300} Q{px_} {base_ - 340} {px_ + 60} {base_ - 300} L{px_ + 70} {base_} Z"/>'
                f'<rect x="{px_ - 90}" y="{base_ - 300}" width="40" height="200" rx="18"/><rect x="{px_ + 50}" y="{base_ - 300}" width="40" height="200" rx="18"/></g>'
                f'<g fill="#b8955c">{"".join(f"<circle cx=\"{px_}\" cy=\"{base_ - 270 + k * 50}\" r=\"6\"/>" for k in range(4))}</g>'
                f'<ellipse cx="{px_}" cy="{base_ - 365}" rx="40" ry="48" fill="#c7b29a"/>'
                f'<rect x="{px_ - 46}" y="{base_ - 425}" width="92" height="34" rx="6" fill="#121624"/>'
                f'<rect x="{px_ - 58}" y="{base_ - 395}" width="116" height="10" rx="4" fill="#121624"/>'
                f'<rect x="{px_ - 40}" y="{base_ - 415}" width="80" height="6" fill="#b8955c"/>'
                f'<path d="M{px_ - 16} {base_ - 345} q16 12 32 0" stroke="#3a2418" stroke-width="5" fill="none"/>'
                f'<circle cx="{px_ - 14}" cy="{base_ - 370}" r="4" fill="#1a1010"/><circle cx="{px_ + 14}" cy="{base_ - 370}" r="4" fill="#1a1010"/>')
    return out


# S4 — the far door opens, a tall shape in the dark doorway
save("s4", svg(corridor(figure_at=270), DEFS))
# S5 — curtains scraped open one by one, the shape closer
save("s5", svg(corridor(figure_at=None, opened={(-1, 4), (1, 4), (-1, 3), (1, 3), (1, 2)})
               + figure(800, 880, 600, "#010102") + eyes(800, 350, gap=20, r=4.5)
               + glow(800, 600, 260, "#000", 0.4), DEFS))

# S6 — inside my berth: hands gripping the curtain shut, the shadow standing right outside
hands = ""
for hx, hy in ((860, 560), (1060, 600)):
    hands += (f'<ellipse cx="{hx}" cy="{hy}" rx="48" ry="62" fill="#c49c80"/>'
              + "".join(f'<rect x="{hx - 44 + k * 22}" y="{hy - 70}" width="20" height="46" rx="10" fill="#b48c70"/>' for k in range(4))
              + f'<path d="M{hx - 30} {hy + 60} L{hx - 50} 1080 L{hx + 50} 1080 L{hx + 30} {hy + 60}Z" fill="#2a2440"/>')
save("s6", svg(f'''
<rect width="{W}" height="{H}" fill="#080506"/>
<rect x="460" y="60" width="1000" height="1020" fill="url(#curtlit)"/>
{"".join(f'<path d="M{460 + i * 90} 60 q14 500 -6 1020" stroke="#1a0406" stroke-width="30" fill="none" opacity="0.5"/>' for i in range(1, 12))}
<rect x="440" y="44" width="1040" height="16" rx="8" fill="#8a7a58"/>
{glow(960, 420, 420, "#ffb54a", 0.35)}
<g opacity="0.85" filter="url(#blur8)">{figure(960, 1100, 1100, "#120204")}</g>
{eyes(960, 120, gap=40, r=7)}
<path d="M955 60 L955 1080" stroke="#0a0204" stroke-width="10"/>
{hands}
''', DEFS))

# S7 — morning: pale dawn in the aisle, the porter smiling
save("s7", svg(corridor(dawn=True, porter=True), DEFS))

# S8 — my berth with the curtain closed, blanket, two pairs of shoes ... (memory: I never closed it)
save("s8", svg(f'''
<rect width="{W}" height="{H}" fill="#0a0708"/>
<rect x="470" y="120" width="980" height="560" fill="url(#curtlit)"/>
{"".join(f'<path d="M{470 + i * 98} 120 q12 280 -4 560" stroke="#1a0406" stroke-width="26" fill="none" opacity="0.5"/>' for i in range(1, 10))}
<rect x="450" y="104" width="1020" height="14" rx="7" fill="#8a7a58"/>
{"".join(f'<circle cx="{470 + i * 98}" cy="112" r="8" fill="#b0a070"/>' for i in range(11))}
<rect x="440" y="680" width="1040" height="60" fill="#2a1d14"/>
<path d="M440 1080 L1480 1080 L1480 740 L440 740Z" fill="url(#floor)"/>
<g fill="#1a1414"><path d="M640 960 q0 -60 60 -60 l60 0 q40 0 60 40 l30 30 q10 30 -30 30 l-180 0 z"/>
<path d="M800 990 q0 -60 60 -60 l60 0 q40 0 60 40 l30 30 q10 30 -30 30 l-180 0 z"/></g>
<g fill="#cfd4dc" opacity="0.9"><path d="M1060 950 q0 -50 50 -50 l50 0 q36 0 54 34 l26 26 q8 26 -26 26 l-154 0 z"/>
<path d="M1210 985 q0 -50 50 -50 l50 0 q36 0 54 34 l26 26 q8 26 -26 26 l-154 0 z"/></g>
<g fill="#6a6e78"><rect x="1060" y="986" width="200" height="10"/><rect x="1210" y="1021" width="200" height="10"/></g>
{glow(1240, 960, 220, "#9fb8d8", 0.18)}
{glow(960, 380, 380, "#ffb54a", 0.18)}
''', DEFS))

# S9 — the berth, the blanket behind me ... and something cold underneath it
save("s9", svg(f'''
<rect width="{W}" height="{H}" fill="#06040a"/>
<rect x="560" y="140" width="800" height="300" rx="40" fill="#1a120c"/>
<rect x="600" y="170" width="720" height="240" rx="30" fill="url(#night)"/>
<clipPath id="win9"><rect x="600" y="170" width="720" height="240" rx="30"/></clipPath>
<g clip-path="url(#win9)">{forest(410, 24, (100, 200), "#060910", 560, 1360)}{snowfall(80, 0.9, 420)}</g>
<rect x="420" y="460" width="1080" height="620" fill="#140d0a"/>
<path d="M420 560 C600 470 800 520 980 500 C1160 480 1300 430 1500 520 L1500 1080 L420 1080Z" fill="url(#blanket)"/>
<path d="M620 560 C760 470 1000 460 1140 520" stroke="#0e1018" stroke-width="16" fill="none"/>
<path d="M560 520 C700 420 1000 410 1200 480 C1260 500 1300 540 1320 560 L560 560Z" fill="#141626"/>
<ellipse cx="900" cy="555" rx="220" ry="34" fill="#020203"/>
{eyes(860, 548, gap=70, r=8, color="#e8eef8")}
<g fill="#d8dde6"><path d="M1060 600 q40 -20 90 -6 l70 20 q20 8 6 20 l-70 -6 q-30 30 -80 20 q-30 -20 -16 -48z"/>
{"".join(f'<rect x="{1150 + k * 18}" y="{604 + k * 7}" width="70" height="13" rx="6" transform="rotate({10 + k * 4} {1150 + k * 18} {604 + k * 7})"/>' for k in range(4))}</g>
{glow(1120, 620, 140, "#9fb8d8", 0.35)}
{glow(900, 540, 260, "#3a4a7a", 0.25)}
''', DEFS))
