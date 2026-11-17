"""Scenes for 'The Empty Swing'. Run inside this folder: python3 scenes.py"""
import sys, math, random
sys.path.insert(0, "../../toolkit")
from scenekit import *

R = random.Random(11)
_save = save


def save(name, markup):
    """Widen blur filter regions so glows don't clip into squares."""
    for f in ("blur8", "blur30", "blur60"):
        markup = markup.replace(f'<filter id="{f}">', f'<filter id="{f}" x="-1.5" y="-1.5" width="4" height="4">')
    _save(name, markup)


# ------------------------------------------------------------------ helpers
def swing_set(x0, x1, top, base, swings, color="#07080e", chain="#3a3f52", seat="#0a0b12", cw=4, sw=92):
    """Side-on swing set. swings = [(x, angle_deg, opacity), ...]"""
    out = [f'<g fill="none" stroke="{color}" stroke-linecap="round">']
    for x in (x0, x1):
        out.append(f'<path d="M{x - 85} {base} L{x} {top} L{x + 85} {base}" stroke-width="16"/>')
        out.append(f'<line x1="{x - 50}" y1="{base - 90}" x2="{x + 50}" y2="{base - 90}" stroke-width="8"/>')
    out.append(f'<line x1="{x0 - 20}" y1="{top}" x2="{x1 + 20}" y2="{top}" stroke-width="18"/></g>')
    L = base - top - 95
    for sx, ang, op in swings:
        a = math.radians(ang)
        cx, cy = sx + L * math.sin(a), top + L * math.cos(a)
        dx, dy = 34 * math.cos(a), -34 * math.sin(a)
        out.append(f'<g opacity="{op}">'
                   f'<line x1="{sx}" y1="{top}" x2="{cx - dx:.0f}" y2="{cy - dy:.0f}" stroke="{chain}" stroke-width="{cw}" stroke-dasharray="{cw*2} {cw}"/>'
                   f'<line x1="{sx}" y1="{top}" x2="{cx + dx:.0f}" y2="{cy + dy:.0f}" stroke="{chain}" stroke-width="{cw}" stroke-dasharray="{cw*2} {cw}"/>'
                   f'<rect x="{cx - sw/2:.0f}" y="{cy - sw/12:.0f}" width="{sw}" height="{sw/6:.0f}" rx="6" fill="{seat}" stroke="{chain}" stroke-width="2" '
                   f'transform="rotate({-ang:.1f} {cx:.0f} {cy:.0f})"/></g>')
    return "".join(out)


def seat_pos(sx, top, base, ang):
    L = base - top - 95; a = math.radians(ang)
    return sx + L * math.sin(a), top + L * math.cos(a)


def streetlight(x, base, h=520, color="#ffc46b", on=True, flip=False):
    d = -1 if flip else 1
    tip = x + d * 90
    s = (f'<g fill="#06070c"><rect x="{x - 7}" y="{base - h}" width="14" height="{h}"/>'
         f'<path d="M{x} {base - h} q{d * 10} -30 {d * 90} -20" stroke="#06070c" stroke-width="10" fill="none"/>'
         f'<path d="M{tip - 32} {base - h - 14} h64 l-12 22 h-40z"/></g>')
    if on:
        s += (f'<polygon points="{tip - 22},{base - h + 8} {tip + 22},{base - h + 8} {tip + 260},{base} {tip - 260},{base}" fill="{color}" opacity="0.10"/>'
              f'<ellipse cx="{tip}" cy="{base}" rx="260" ry="34" fill="{color}" opacity="0.18" filter="url(#blur30)"/>'
              f'{glow(tip, base - h + 6, 70, color, 0.75)}<ellipse cx="{tip}" cy="{base - h + 9}" rx="20" ry="6" fill="#fff2cf"/>')
    return s


def woman(cx, base, h=420, color="#040408", bag=True, stride=0, face=1):
    """Woman in a coat with long hair. face=1 right, -1 left (only hair/bag side changes)."""
    hy = base - h * .89; hr = h * .065
    sh_y = base - h * .78; hip = base - h * .42
    s = [f'<g fill="{color}">']
    # hair behind
    s.append(f'<path d="M{cx - hr * 1.1:.0f} {hy - hr * .2:.0f} C{cx - hr * 1.4:.0f} {hy + hr * 2:.0f} {cx - hr * 1.6:.0f} {sh_y + h * .06:.0f} {cx - hr * 1.2:.0f} {sh_y + h * .1:.0f} '
             f'L{cx + hr * 1.2:.0f} {sh_y + h * .1:.0f} C{cx + hr * 1.6:.0f} {sh_y + h * .06:.0f} {cx + hr * 1.4:.0f} {hy + hr * 2:.0f} {cx + hr * 1.1:.0f} {hy - hr * .2:.0f}Z"/>')
    s.append(f'<circle cx="{cx}" cy="{hy:.0f}" r="{hr:.0f}"/>')
    s.append(f'<rect x="{cx - hr * .4:.0f}" y="{hy + hr * .8:.0f}" width="{hr * .8:.0f}" height="{hr * 1.2:.0f}"/>')
    # coat
    s.append(f'<path d="M{cx - h * .1:.0f} {sh_y:.0f} Q{cx:.0f} {sh_y - h * .03:.0f} {cx + h * .1:.0f} {sh_y:.0f} L{cx + h * .135:.0f} {hip + h * .12:.0f} L{cx - h * .135:.0f} {hip + h * .12:.0f}Z"/>')
    # legs
    for sgn in (-1, 1):
        lx = cx + sgn * h * .04
        fx = lx + sgn * stride * h * .12
        s.append(f'<path d="M{lx:.0f} {hip + h * .1:.0f} L{fx:.0f} {base - 4:.0f}" stroke="{color}" stroke-width="{h * .045:.0f}" stroke-linecap="round"/>')
        s.append(f'<ellipse cx="{fx + face * h * .02:.0f}" cy="{base - 4:.0f}" rx="{h * .035:.0f}" ry="{h * .015:.0f}"/>')
    # arms
    s.append(f'<path d="M{cx - h * .1:.0f} {sh_y + h * .02:.0f} L{cx - h * .14:.0f} {hip + h * .02:.0f}" stroke="{color}" stroke-width="{h * .04:.0f}" stroke-linecap="round"/>')
    s.append(f'<path d="M{cx + h * .1:.0f} {sh_y + h * .02:.0f} L{cx + h * .14:.0f} {hip + h * .02:.0f}" stroke="{color}" stroke-width="{h * .04:.0f}" stroke-linecap="round"/>')
    if bag:
        bx = cx + face * h * .17
        s.append(f'<path d="M{bx - h * .07:.0f} {hip - h * .02:.0f} h{h * .14:.0f} l{-h * .01:.0f} {h * .17:.0f} h{-h * .12:.0f}Z" fill="#1d1a22"/>')
        s.append(f'<path d="M{bx - h * .03:.0f} {hip - h * .02:.0f} l{-h * .02:.0f} {-h * .07:.0f} M{bx + h * .02:.0f} {hip - h * .02:.0f} l{h * .03:.0f} {-h * .05:.0f}" stroke="#1d1a22" stroke-width="{h * .02:.0f}" stroke-linecap="round"/>')
    s.append('</g>')
    return "".join(s)


def grandma(cx, base, h=330, color="#140c0a"):
    hy = base - h * .86
    return (f'<g fill="{color}"><circle cx="{cx + 14}" cy="{hy:.0f}" r="{h * .07:.0f}"/>'
            f'<circle cx="{cx + 4}" cy="{hy - h * .07:.0f}" r="{h * .04:.0f}"/>'
            f'<path d="M{cx - h * .12:.0f} {base - h * .74:.0f} Q{cx + h * .02:.0f} {base - h * .86:.0f} {cx + h * .14:.0f} {base - h * .74:.0f} '
            f'L{cx + h * .18:.0f} {base - h * .05:.0f} L{cx - h * .17:.0f} {base - h * .05:.0f}Z"/>'
            f'<rect x="{cx - h * .1:.0f}" y="{base - h * .06:.0f}" width="{h * .07:.0f}" height="{h * .06:.0f}"/>'
            f'<rect x="{cx + h * .03:.0f}" y="{base - h * .06:.0f}" width="{h * .07:.0f}" height="{h * .06:.0f}"/>'
            f'<path d="M{cx + h * .16:.0f} {base - h * .5:.0f} L{cx + h * .26:.0f} {base:.0f}" stroke="{color}" stroke-width="7"/></g>')


def child(cx, base, h=200, color="#140c0a"):
    hy = base - h * .85
    return (f'<g fill="{color}"><circle cx="{cx}" cy="{hy:.0f}" r="{h * .1:.0f}"/>'
            f'<path d="M{cx - h * .13:.0f} {base - h * .7:.0f} Q{cx:.0f} {base - h * .78:.0f} {cx + h * .13:.0f} {base - h * .7:.0f} L{cx + h * .17:.0f} {base - h * .32:.0f} L{cx - h * .17:.0f} {base - h * .32:.0f}Z"/>'
            f'<rect x="{cx - h * .09:.0f}" y="{base - h * .34:.0f}" width="{h * .07:.0f}" height="{h * .34:.0f}"/>'
            f'<rect x="{cx + h * .02:.0f}" y="{base - h * .34:.0f}" width="{h * .07:.0f}" height="{h * .34:.0f}"/>'
            f'<path d="M{cx - h * .13:.0f} {base - h * .66:.0f} L{cx - h * .24:.0f} {base - h * .52:.0f}" stroke="{color}" stroke-width="{h * .06:.0f}" stroke-linecap="round"/></g>')


def porch_swing(cx, top, y, color="#0c0a10", chain="#3a3348", w=230, ang=0):
    return (f'<g transform="rotate({-ang} {cx} {top})">'
            f'<line x1="{cx - w / 2 + 10}" y1="{top}" x2="{cx - w / 2 + 10}" y2="{y}" stroke="{chain}" stroke-width="4" stroke-dasharray="7 4"/>'
            f'<line x1="{cx + w / 2 - 10}" y1="{top}" x2="{cx + w / 2 - 10}" y2="{y}" stroke="{chain}" stroke-width="4" stroke-dasharray="7 4"/>'
            f'<rect x="{cx - w / 2}" y="{y}" width="{w}" height="18" rx="4" fill="{color}"/>'
            f'<rect x="{cx - w / 2}" y="{y - 70}" width="{w}" height="12" rx="4" fill="{color}"/>'
            + "".join(f'<rect x="{x}" y="{y - 70}" width="9" height="72" fill="{color}"/>' for x in range(int(cx - w / 2) + 6, int(cx + w / 2), 28))
            + f'<rect x="{cx - w / 2 - 8}" y="{y - 50}" width="12" height="70" fill="{color}"/><rect x="{cx + w / 2 - 4}" y="{y - 50}" width="12" height="70" fill="{color}"/></g>')


def house(cx, base, body="#0a0910", lit=True, win="#ffb54a", swing_ang=0, swing_chain="#2e2a3a", extra=""):
    """Two-storey house with a front porch and a porch swing on the right."""
    L, Rr = cx - 380, cx + 380
    s = [f'<g fill="{body}">',
         f'<polygon points="{L},{base - 120} {L},{base - 470} {cx},{base - 700} {Rr},{base - 470} {Rr},{base - 120}"/>',
         f'<rect x="{cx + 190}" y="{base - 690}" width="50" height="130"/>',
         f'<rect x="{L - 30}" y="{base - 130}" width="{Rr - L + 60}" height="130"/>',
         f'<polygon points="{L - 60},{base - 330} {Rr + 60},{base - 330} {Rr + 30},{base - 380} {L - 30},{base - 380}"/>',
         ''.join(f'<rect x="{x - 9}" y="{base - 330}" width="18" height="210"/>' for x in (L - 20, L + 230, Rr - 230, Rr + 20)),
         f'<rect x="{cx - 120}" y="{base - 60}" width="240" height="20" fill="#14121c"/><rect x="{cx - 140}" y="{base - 30}" width="280" height="30" fill="#14121c"/>',
         '</g>']
    wc = win if lit else "#141826"
    for x, y in ((cx - 250, base - 560), (cx + 150, base - 560)):
        if lit: s.append(lit_window(x, y, 100, 120, wc))
        else: s.append(f'<rect x="{x}" y="{y}" width="100" height="120" fill="{wc}"/><line x1="{x + 50}" y1="{y}" x2="{x + 50}" y2="{y + 120}" stroke="{body}" stroke-width="5"/><line x1="{x}" y1="{y + 60}" x2="{x + 100}" y2="{y + 60}" stroke="{body}" stroke-width="5"/>')
    s.append(f'<rect x="{cx - 60}" y="{base - 300}" width="120" height="180" fill="#05040a"/>')
    s.append(f'<rect x="{cx - 290}" y="{base - 280}" width="130" height="110" fill="{"#7a4a20" if lit else "#121522"}" opacity="{0.9 if lit else 1}"/>')
    s.append(porch_swing(cx + 260, base - 330, base - 190, color=body, chain=swing_chain, ang=swing_ang))
    s.append(extra)
    return "".join(s)


def town_skyline(base, color="#0c0d18", lights=True):
    out = [f'<g fill="{color}">']; x = -20; win = []
    while x < W:
        w = R.randint(110, 200); h = R.randint(70, 160)
        out.append(f'<rect x="{x}" y="{base - h}" width="{w}" height="{h}"/><polygon points="{x - 10},{base - h} {x + w / 2},{base - h - 60} {x + w + 10},{base - h}"/>')
        if lights and R.random() < .35:
            win.append(f'<rect x="{x + w / 2 - 10}" y="{base - h + 30}" width="20" height="24" fill="#ffb54a" opacity="0.8"/>')
        x += w + R.randint(10, 60)
    out.append('</g>'); return "".join(out + win)


def ground(y, c1, c2):
    return (f'<path d="M0 {y} C500 {y - 20} 1300 {y + 10} {W} {y - 10} L{W} {H} L0 {H}Z" fill="{c1}"/>'
            f'{grass(y + 6, 220, c2)}')


NIGHT = sky("night", "#04050c", "#141a33", "#2a2f4a")

# ------------------------------------------------------------------ S1  the swing set in the park
TOP, BASE = 430, 860
s1 = f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>{stars(160, 520)}{moon(560, 190, 70)}
{town_skyline(760)}
{dead_tree(470, 860, 420)}{dead_tree(1560, 860, 380)}
{ground(840, "#121628", "#0b0e1c")}
<path d="M560 1080 C700 950 820 900 960 880 C1100 870 1250 900 1400 1080Z" fill="#1b2038" opacity="0.8"/>
{streetlight(1330, 860, 560)}
{swing_set(720, 1180, TOP, BASE, [(800, 0, 1), (950, 0, 1), (1100, 0, 1)])}
{fog(880, op=0.16)}
{grass(1080, 260, "#06070e", (20, 50))}
'''
save("s1", svg(s1, NIGHT))

# ------------------------------------------------------------------ S2  grandmother and child, long ago (warm dusk)
s2 = f'''
<rect width="{W}" height="{H}" fill="url(#dusk)"/>
{glow(1450, 760, 260, "#ff9a4a", 0.45)}
<circle cx="1450" cy="760" r="120" fill="#ffb066" opacity="0.6"/>
{ground(860, "#2a1712", "#1e100c")}
{swing_set(1230, 1610, 560, 870, [(1310, 0, 1), (1530, 8, 1)], color="#1b0f0c", chain="#4a2e24", seat="#1b0f0c")}
{grandma(860, 900, 360)}
{child(1000, 900, 200)}
<path d="M1000 720 Q950 690 905 705" stroke="#140c0a" stroke-width="12" fill="none" stroke-linecap="round"/>
{dead_tree(380, 880, 460, color="#1a0e0b")}
{fog(880, color="#e0a070", op=0.12)}
{grass(1080, 260, "#120907", (20, 50))}
'''
save("s2", svg(s2, sky("dusk", "#2a1420", "#7a3a2a", "#c4703a")))

# ------------------------------------------------------------------ S3  her empty house, years later
boxes = ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#3a2a1c" stroke="#1a1209" stroke-width="3"/><line x1="{x}" y1="{y + 10}" x2="{x + w}" y2="{y + 10}" stroke="#6a5030" stroke-width="5"/>'
                for x, y, w, h in ((640, 880, 110, 80), (760, 900, 90, 60), (690, 820, 80, 60)))
sign = ('<g><rect x="1340" y="850" width="10" height="170" fill="#0a0910"/><rect x="1260" y="820" width="180" height="100" fill="#d9d2c0"/>'
        f'<text x="1350" y="860" text-anchor="middle" font-family="{SANS}" font-size="30" font-weight="bold" fill="#8c1c1c">FOR</text>'
        f'<text x="1350" y="900" text-anchor="middle" font-family="{SANS}" font-size="30" font-weight="bold" fill="#8c1c1c">SALE</text></g>')
s3 = f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>{stars(140, 450)}{moon(560, 180, 55)}
{dead_tree(1580, 990, 520)}
{house(960, 990, lit=False)}
{ground(990, "#121628", "#0b0e1c")}
{boxes}
<polygon points="0,1080 0,960 300,1000 380,1080" fill="#f4e6b0" opacity="0.10"/>
{sign}
{fog(1000, op=0.14)}
'''
save("s3", svg(s3, NIGHT))

# ------------------------------------------------------------------ S4  walking home through the park, middle swing moving
s4 = f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>{stars(150, 480)}{moon(560, 170, 60)}
{town_skyline(700)}
{ground(760, "#121628", "#0b0e1c")}
{dead_tree(1680, 790, 360)}
{streetlight(1440, 800, 470, flip=True)}
{swing_set(1060, 1380, 470, 790, [(1120, 0, 1), (1220, 32, 1), (1320, 0, 1)])}
<path d="M300 1080 C500 950 700 880 900 850 C1100 830 1400 830 1700 830 L1700 860 C1400 870 1100 880 950 905 C800 940 700 1000 640 1080Z" fill="#232a48"/>
{fog(820, op=0.17)}
{woman(800, 1000, 430, stride=0.6, face=1)}
{grass(1080, 260, "#06070e", (20, 50))}
'''
save("s4", svg(s4, NIGHT))

# ------------------------------------------------------------------ S5  close: the middle swing, swinging high
TOP5, BASE5 = 300, 980
ghosts = "".join(swing_set(0, 0, TOP5, BASE5, [(960, a, op)], color="none", chain="#5a6080", cw=6, sw=150) for a, op in ((-20, .12), (5, .18), (25, .3)))
sx5, sy5 = seat_pos(960, TOP5, BASE5, 42)
s5 = f'''
<rect width="{W}" height="{H}" fill="url(#night5)"/>{stars(90, 350, .5)}
{glow(1000, 520, 320, "#6a1420", 0.35)}
{ground(930, "#0f1324", "#090b16")}
{ghosts}
{swing_set(560, 1360, TOP5, BASE5, [(700, 0, 1), (960, 42, 1), (1220, 0, 1)], chain="#5a6080", cw=6, sw=150)}
{glow(sx5, sy5, 90, "#c6d4ff", 0.22)}
{fog(950, op=0.18)}
{grass(1080, 260, "#05060c", (20, 50))}
'''
save("s5", svg(s5, sky("night5", "#030409", "#101530", "#241a33")))

# S5b — the same, a voice from the empty seat: faint pale eyes just above it
s5b = s5.replace(f'{glow(sx5, sy5, 90, "#c6d4ff", 0.22)}',
                 f'{glow(sx5, sy5 - 90, 110, "#c6d4ff", 0.20)}'
                 f'<ellipse cx="{sx5:.0f}" cy="{sy5 - 90:.0f}" rx="44" ry="54" fill="#c6d4ff" opacity="0.08" filter="url(#blur8)"/>'
                 f'{eyes(sx5, sy5 - 95, gap=26, r=5, color="#e8eeff")}')
save("s5b", svg(s5b, sky("night5", "#030409", "#101530", "#241a33")))

# ------------------------------------------------------------------ S6  hurrying home down the street
houses = "".join(f'<g fill="#090a12"><rect x="{x}" y="{620 - h}" width="{w}" height="{h + 80}"/><polygon points="{x - 15},{620 - h} {x + w / 2},{560 - h} {x + w + 15},{620 - h}"/></g>'
                 + (lit_window(x + w / 2 - 25, 640 - h, 50, 60) if lit else "")
                 for x, w, h, lit in ((40, 260, 120, True), (340, 220, 90, False), (1360, 240, 110, False), (1640, 260, 130, True)))
tiny_set = swing_set(760, 880, 590, 680, [(790, 0, 1), (820, 30, 1), (850, 0, 1)], color="#0c0f1c", chain="#2f3448")
s6 = f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>{stars(150, 450)}{moon(1460, 170, 55)}
{houses}
<polygon points="860,700 1060,700 1500,1080 420,1080" fill="#1b2036"/>
<polygon points="0,700 860,700 420,1080 0,1080" fill="#0f1222"/><polygon points="1060,700 1920,700 1920,1080 1500,1080" fill="#0f1222"/>
<g stroke="#5a5a6a" stroke-width="6" stroke-dasharray="40 40" opacity="0.5"><line x1="960" y1="700" x2="960" y2="1080"/></g>
{tiny_set}
{glow(820, 630, 80, "#6a1420", 0.5)}
{streetlight(560, 760, 520)}{streetlight(1360, 760, 520, flip=True)}
{fog(700, op=0.18)}
{woman(1090, 1040, 470, stride=0.8, face=1, bag=True)}
'''
save("s6", svg(s6, NIGHT))

# ------------------------------------------------------------------ S7  looking out the open front door at the porch swing
floor = "".join(f'<line x1="960" y1="700" x2="{x}" y2="1080" stroke="#0a0806" stroke-width="3"/>' for x in range(-600, 2600, 170))
s7 = f'''
<rect width="{W}" height="{H}" fill="#07060a"/>
<rect x="0" y="0" width="{W}" height="760" fill="#0c0a10"/>
<polygon points="0,1080 0,760 1920,760 1920,1080" fill="#130e0b"/>
<g clip-path="url(#fl)">{floor}</g>
<rect x="640" y="140" width="640" height="640" fill="url(#out7)"/>
<g clip-path="url(#doorclip)">
  {stars(60, 760, .6)}
  <circle cx="1150" cy="260" r="40" fill="#e9e3d0"/>{glow(1150, 260, 90, "#e9e3d0", .25)}
  <rect x="640" y="200" width="640" height="26" fill="#0b0a12"/>
  <rect x="640" y="660" width="640" height="120" fill="#141522"/>
  <rect x="640" y="600" width="640" height="16" fill="#0b0a12"/>
  {''.join(f'<rect x="{x}" y="600" width="10" height="70" fill="#0b0a12"/>' for x in range(650, 1280, 40))}
  <rect x="1240" y="200" width="22" height="470" fill="#0b0a12"/>
  {porch_swing(960, 226, 520, color="#0b0a12", chain="#565a72", w=300)}
  {dead_tree(780, 640, 330, color="#0c0d18", s=.7)}
</g>
<polygon points="640,780 1280,780 1500,1080 420,1080" fill="#9fb4e8" opacity="0.07"/>
<rect x="600" y="110" width="40" height="680" fill="#1c130e"/><rect x="1280" y="110" width="40" height="680" fill="#1c130e"/>
<rect x="600" y="100" width="720" height="40" fill="#1c130e"/>
<polygon points="640,140 640,780 470,840 470,90" fill="#26180f"/>
<rect x="490" y="440" width="20" height="40" rx="6" fill="#a7853f"/>
{fog(760, color="#9fb4e8", op=.05)}
'''
defs7 = f'''<linearGradient id="out7" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a0e20"/><stop offset="1" stop-color="#2c3352"/></linearGradient>
<clipPath id="doorclip"><rect x="640" y="140" width="640" height="640"/></clipPath>
<clipPath id="fl"><rect x="0" y="760" width="{W}" height="320"/></clipPath>'''
save("s7", svg(s7, defs7))

# ------------------------------------------------------------------ S8  standing in the doorway... two small hands on her back
hand = lambda x, y, rot: (f'<g transform="translate({x} {y}) rotate({rot})" fill="#c9cdda" opacity="0.92">'
                          f'<ellipse cx="0" cy="0" rx="26" ry="30"/>'
                          + "".join(f'<rect x="{fx}" y="{-62 + abs(fx) * .4:.0f}" width="11" height="{40 - abs(fx) * .3:.0f}" rx="5.5"/>' for fx in (-24, -11, 2, 15))
                          + '<rect x="22" y="-14" width="11" height="28" rx="5.5" transform="rotate(35 27 0)"/></g>')
s8 = f'''
<rect width="{W}" height="{H}" fill="#060406"/>
<rect x="0" y="0" width="{W}" height="780" fill="#0b0709"/>
<rect x="560" y="80" width="800" height="760" fill="url(#out8)"/>
<g clip-path="url(#dc8)">{stars(50, 600, .5)}{porch_swing(960, 150, 470, color="#0a0810", chain="#4a3a50", w=320)}</g>
<rect x="520" y="60" width="40" height="790" fill="#1a0f0c"/><rect x="1360" y="60" width="40" height="790" fill="#1a0f0c"/><rect x="520" y="40" width="880" height="44" fill="#1a0f0c"/>
<polygon points="0,1080 0,840 1920,840 1920,1080" fill="#100a09"/>
<polygon points="560,840 1360,840 1600,1080 320,1080" fill="#c2362b" opacity="0.10"/>
{glow(960, 560, 380, "#8c1c1c", 0.35)}
{woman(960, 1100, 980, color="#030203", bag=False, stride=0.05)}
{hand(895, 700, -8)}{hand(1030, 712, 10)}
{glow(895, 690, 60, "#e8ecff", 0.18)}{glow(1030, 700, 60, "#e8ecff", 0.18)}
'''
defs8 = '''<linearGradient id="out8" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#14070a"/><stop offset="1" stop-color="#4a1418"/></linearGradient>
<clipPath id="dc8"><rect x="560" y="80" width="800" height="760"/></clipPath>'''
save("s8", svg(s8, defs8))
print("ok")
