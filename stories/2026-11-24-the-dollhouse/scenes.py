"""Scenes for The Dollhouse."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

RED = "#c4262b"
WARM = "#ffb54a"


# ------------------------------------------------------------------ dolls
def peg_doll(x, base, h=120, dress="#5a6a8a", hair="#2a1a10", face="#e8d6bf", ponytail=False, facing=0, op=1.0):
    """Small wooden doll standing at (x, base). facing: 0 front, 1 = looking right (side, back-ish)."""
    hr = h * 0.17
    hy = base - h + hr
    out = [f'<g opacity="{op}">']
    # dress / body
    out.append(f'<path d="M{x - h * .1:.0f} {hy + hr * .9:.0f} L{x - h * .22:.0f} {base - h * .06:.0f} '
               f'L{x + h * .22:.0f} {base - h * .06:.0f} L{x + h * .1:.0f} {hy + hr * .9:.0f}Z" fill="{dress}"/>')
    out.append(f'<rect x="{x - h * .12:.0f}" y="{base - h * .07:.0f}" width="{h * .08:.0f}" height="{h * .07:.0f}" fill="#120c0a"/>')
    out.append(f'<rect x="{x + h * .04:.0f}" y="{base - h * .07:.0f}" width="{h * .08:.0f}" height="{h * .07:.0f}" fill="#120c0a"/>')
    # arms
    out.append(f'<path d="M{x - h * .1:.0f} {hy + hr * 1.2:.0f} L{x - h * .17:.0f} {hy + hr * 2.6:.0f}" stroke="{dress}" stroke-width="{h * .06:.0f}" stroke-linecap="round"/>')
    out.append(f'<path d="M{x + h * .1:.0f} {hy + hr * 1.2:.0f} L{x + h * .17:.0f} {hy + hr * 2.6:.0f}" stroke="{dress}" stroke-width="{h * .06:.0f}" stroke-linecap="round"/>')
    # head
    if facing == 0:
        out.append(f'<circle cx="{x}" cy="{hy:.0f}" r="{hr:.0f}" fill="{face}"/>')
        out.append(f'<path d="M{x - hr:.0f} {hy:.0f} C{x - hr:.0f} {hy - hr * 1.3:.0f} {x + hr:.0f} {hy - hr * 1.3:.0f} {x + hr:.0f} {hy:.0f} '
                   f'C{x + hr * .6:.0f} {hy - hr * .6:.0f} {x - hr * .6:.0f} {hy - hr * .6:.0f} {x - hr:.0f} {hy:.0f}Z" fill="{hair}"/>')
        out.append(f'<circle cx="{x - hr * .35:.0f}" cy="{hy + hr * .1:.0f}" r="{max(2, hr * .11):.1f}" fill="#120c0a"/>')
        out.append(f'<circle cx="{x + hr * .35:.0f}" cy="{hy + hr * .1:.0f}" r="{max(2, hr * .11):.1f}" fill="#120c0a"/>')
        out.append(f'<path d="M{x - hr * .25:.0f} {hy + hr * .5:.0f} q{hr * .25:.0f} {hr * .15:.0f} {hr * .5:.0f} 0" stroke="#7a2a2a" stroke-width="{max(1.5, hr * .08):.1f}" fill="none"/>')
    else:
        # seen from behind-left, looking right: mostly hair
        out.append(f'<circle cx="{x}" cy="{hy:.0f}" r="{hr:.0f}" fill="{face}"/>')
        out.append(f'<path d="M{x + hr * .55:.0f} {hy - hr * .9:.0f} C{x - hr * 1.3:.0f} {hy - hr * 1.2:.0f} {x - hr * 1.3:.0f} {hy + hr * 1.1:.0f} {x + hr * .2:.0f} {hy + hr:.0f} '
                   f'C{x + hr * .1:.0f} {hy + hr * .3:.0f} {x + hr * .2:.0f} {hy - hr * .3:.0f} {x + hr * .55:.0f} {hy - hr * .9:.0f}Z" fill="{hair}"/>')
    if ponytail:
        px = x - hr * 0.9 if facing == 0 else x - hr * 1.1
        out.append(f'<path d="M{px + hr * .3:.0f} {hy - hr * .5:.0f} C{px - hr * .8:.0f} {hy - hr * .2:.0f} {px - hr * .7:.0f} {hy + hr * 1.4:.0f} {px - hr * .2:.0f} {hy + hr * 2.1:.0f}" '
                   f'stroke="{hair}" stroke-width="{hr * .55:.0f}" fill="none" stroke-linecap="round"/>')
        out.append(f'<circle cx="{px + hr * .15:.0f}" cy="{hy - hr * .4:.0f}" r="{hr * .2:.0f}" fill="{RED}"/>')
    out.append('</g>')
    return "".join(out)


def sleeping_girl(x, y, w=120, blanket="#7a4a5a", hair="#3a2414"):
    return (f'<rect x="{x - w / 2:.0f}" y="{y - 6:.0f}" width="{w:.0f}" height="34" rx="4" fill="#3a2418"/>'
            f'<rect x="{x - w / 2:.0f}" y="{y - 40:.0f}" width="10" height="68" fill="#2a1810"/>'
            f'<rect x="{x - w / 2 + 6:.0f}" y="{y - 22:.0f}" width="30" height="16" rx="6" fill="#d8ccb8"/>'
            f'<circle cx="{x - w / 2 + 24:.0f}" cy="{y - 22:.0f}" r="12" fill="#e8d6bf"/>'
            f'<path d="M{x - w / 2 + 12:.0f} {y - 22:.0f} a12 12 0 0 1 24 -4 Z" fill="{hair}"/>'
            f'<rect x="{x - w / 2 + 30:.0f}" y="{y - 20:.0f}" width="{w - 34:.0f}" height="18" rx="7" fill="{blanket}"/>')


def chair(x, y, s=1.0, c="#4a2c1a"):
    return (f'<g fill="{c}"><rect x="{x}" y="{y - 70 * s:.0f}" width="{6 * s:.0f}" height="{70 * s:.0f}"/>'
            f'<rect x="{x}" y="{y - 34 * s:.0f}" width="{34 * s:.0f}" height="{6 * s:.0f}"/>'
            f'<rect x="{x + 28 * s:.0f}" y="{y - 34 * s:.0f}" width="{6 * s:.0f}" height="{34 * s:.0f}"/>'
            f'<rect x="{x}" y="{y - 70 * s:.0f}" width="{6 * s:.0f}" height="{6 * s:.0f}"/></g>')


# ------------------------------------------------------------------ dollhouse
# Cutaway, three storeys. Ground floor y 600..900, upper floor 320..600, attic above.
L, M1, M2, R = 560, 830, 1090, 1360
G0, G1, A1 = 900, 600, 320


def dollhouse(dolls="", lamps=True, twin_light=True, extra="", dim=0.0):
    p = []
    # outer shell + roof
    p.append(f'<polygon points="{L - 40},{A1 + 10} 960,90 {R + 40},{A1 + 10}" fill="#2a1a18"/>')
    p.append(f'<polygon points="{L - 10},{A1} 960,120 {R + 10},{A1}" fill="#1a1012"/>')
    p.append(f'<rect x="{L - 30}" y="{A1}" width="{R - L + 60}" height="{G0 - A1 + 20}" fill="#2a1a18"/>')
    # attic
    p.append(f'<polygon points="{L + 30},{A1 - 4} 960,150 {R - 30},{A1 - 4}" fill="#120c10"/>')
    p.append(f'<circle cx="960" cy="240" r="34" fill="#1c2236"/><circle cx="960" cy="240" r="34" fill="none" stroke="#2a1a18" stroke-width="8"/>'
             f'<line x1="926" y1="240" x2="994" y2="240" stroke="#2a1a18" stroke-width="5"/><line x1="960" y1="206" x2="960" y2="274" stroke="#2a1a18" stroke-width="5"/>')
    p.append(f'<rect x="{L + 90}" y="{A1 - 50}" width="60" height="46" fill="#24170f"/><rect x="{R - 170}" y="{A1 - 40}" width="80" height="36" fill="#1f140d"/>')
    # rooms
    rooms = [
        (L, A1, M1 - L, G1 - A1, "#3a2638", "#4a3248"),   # parents' room
        (M1, A1, M2 - M1, G1 - A1, "#2c2620", "#3a3228"),  # upstairs hall / landing
        (M2, A1, R - M2, G1 - A1, "#2c3448", "#38425a"),   # twins' room
        (L, G1, M1 - L, G0 - G1, "#3a2a22", "#4a362a"),    # living room
        (M1, G1, M2 - M1, G0 - G1, "#2a221c", "#362c22"),  # stair hall
        (M2, G1, R - M2, G0 - G1, "#2e3a30", "#3c4a3c"),   # kitchen
    ]
    for x, y, w, h, c1, c2 in rooms:
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c1}"/>')
        # wallpaper stripes
        p.append("".join(f'<rect x="{xx}" y="{y}" width="8" height="{h - 40}" fill="{c2}" opacity="0.6"/>' for xx in range(x + 14, x + w - 8, 34)))
        p.append(f'<rect x="{x}" y="{y + h - 40}" width="{w}" height="40" fill="#1d120c"/>')  # floor board
        p.append(f'<rect x="{x}" y="{y + h - 46}" width="{w}" height="6" fill="#4a2e1c"/>')  # skirting
    # walls / floors between rooms
    for x in (M1, M2):
        p.append(f'<rect x="{x - 8}" y="{A1}" width="16" height="{G0 - A1}" fill="#2a1a18"/>')
    p.append(f'<rect x="{L - 30}" y="{G1 - 8}" width="{R - L + 60}" height="16" fill="#2a1a18"/>')
    p.append(f'<rect x="{L - 30}" y="{A1 - 8}" width="{R - L + 60}" height="16" fill="#2a1a18"/>')
    # stair opening in the landing floor: stairs rise left->right through stair hall
    steps = 9
    for i in range(steps):
        sx = M1 + 12 + i * 26
        sy = G0 - 40 - (i + 1) * 30
        p.append(f'<rect x="{sx}" y="{sy}" width="{M2 - 8 - sx}" height="30" fill="#4a2e1c"/>')
        p.append(f'<rect x="{sx}" y="{sy}" width="{M2 - 8 - sx}" height="6" fill="#6a4228"/>')
    # banister
    p.append(f'<line x1="{M1 + 20}" y1="{G0 - 110}" x2="{M2 - 20}" y2="{G1 - 70}" stroke="#1a0f0a" stroke-width="8"/>')
    p.append("".join(f'<line x1="{M1 + 30 + i * 26}" y1="{G0 - 104 - i * 30.5:.0f}" x2="{M1 + 30 + i * 26}" y2="{G0 - 40 - (i + 1) * 30 + 2:.0f}" stroke="#1a0f0a" stroke-width="4"/>' for i in range(0, 8)))
    # landing: twins' door on the right of the hallway (back wall)
    p.append(f'<rect x="{M2 - 80}" y="{G1 - 160}" width="62" height="120" fill="#1a1210"/>')
    p.append(f'<rect x="{M2 - 74}" y="{G1 - 154}" width="50" height="114" fill="#3a2418"/>')
    p.append(f'<circle cx="{M2 - 32}" cy="{G1 - 96}" r="4" fill="#b08a40"/>')
    # parents' room furniture: bed, wardrobe
    p.append(f'<rect x="{L + 40}" y="{G1 - 100}" width="170" height="54" rx="6" fill="#5a3a4a"/>'
             f'<rect x="{L + 30}" y="{G1 - 140}" width="14" height="96" fill="#2a1810"/><rect x="{L + 46}" y="{G1 - 112}" width="44" height="20" rx="8" fill="#d8ccb8"/>'
             f'<rect x="{L + 220}" y="{A1 + 60}" width="40" height="180" fill="#2a1810"/>')
    # picture frames
    p.append(f'<rect x="{L + 100}" y="{A1 + 50}" width="60" height="70" fill="#1a1010" stroke="#8a6a3a" stroke-width="5"/>')
    p.append(f'<rect x="{L + 150}" y="{G1 + 50}" width="80" height="56" fill="#1a1010" stroke="#8a6a3a" stroke-width="5"/>')
    # twins' room: two beds
    p.append(sleeping_girl(M2 + 80, G1 - 70, 110, "#7a4a5a"))
    p.append(sleeping_girl(M2 + 205, G1 - 70, 110, "#4a5a7a"))
    p.append(f'<rect x="{M2 + 110}" y="{A1 + 50}" width="70" height="80" fill="#0e1424"/><rect x="{M2 + 110}" y="{A1 + 50}" width="70" height="80" fill="none" stroke="#2a1a18" stroke-width="6"/>')
    # living room: couch + lamp
    p.append(f'<rect x="{L + 30}" y="{G0 - 120}" width="190" height="70" rx="14" fill="#6a2c2c"/>'
             f'<rect x="{L + 20}" y="{G0 - 100}" width="28" height="60" rx="10" fill="#5a2424"/><rect x="{L + 202}" y="{G0 - 100}" width="28" height="60" rx="10" fill="#5a2424"/>'
             f'<rect x="{L + 40}" y="{G0 - 80}" width="170" height="30" rx="8" fill="#7a3636"/>')
    p.append(f'<line x1="{M1 - 40}" y1="{G0 - 40}" x2="{M1 - 40}" y2="{G0 - 170}" stroke="#1a0f0a" stroke-width="5"/>'
             f'<polygon points="{M1 - 62},{G0 - 170} {M1 - 18},{G0 - 170} {M1 - 28},{G0 - 205} {M1 - 52},{G0 - 205}" fill="#d8a060"/>')
    # kitchen: table + chairs
    p.append(f'<rect x="{M2 + 70}" y="{G0 - 110}" width="140" height="12" fill="#5a3620"/>'
             f'<rect x="{M2 + 80}" y="{G0 - 100}" width="8" height="60" fill="#4a2c1a"/><rect x="{M2 + 192}" y="{G0 - 100}" width="8" height="60" fill="#4a2c1a"/>')
    p.append(chair(M2 + 30, G0 - 40, 1.0) + chair(M2 + 222, G0 - 40, 1.0))
    p.append(f'<rect x="{M2 + 40}" y="{G1 + 40}" width="200" height="60" fill="#24301f"/><rect x="{M2 + 40}" y="{G1 + 40}" width="200" height="60" fill="none" stroke="#1a1210" stroke-width="4"/>')
    if lamps:
        p.append(glow(M1 - 40, G0 - 190, 90, WARM, 0.45))
        p.append(glow(M2 + 140, G0 - 160, 120, WARM, 0.18))
    if twin_light:
        p.append(glow(M2 + 140, G1 - 80, 110, "#9fb4e8", 0.18))
    p.append(dolls)
    p.append(extra)
    # foundation + base
    p.append(f'<rect x="{L - 50}" y="{G0}" width="{R - L + 100}" height="30" fill="#1a1010"/>')
    if dim:
        p.append(f'<rect x="{L - 60}" y="80" width="{R - L + 120}" height="{G0 - 50}" fill="#05040a" opacity="{dim}"/>')
    return "".join(p)


def playroom_bg():
    return (f'<rect width="{W}" height="{H}" fill="#120c10"/>'
            f'<rect width="{W}" height="930" fill="url(#wallp)"/>'
            + "".join(f'<rect x="{x}" y="0" width="6" height="930" fill="#22161e" opacity="0.7"/>' for x in range(20, W, 60))
            + f'<rect x="0" y="930" width="{W}" height="150" fill="#1a110c"/>'
            + "".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#120b08" stroke-width="3"/>' for y in (960, 1000, 1045))
            + f'<rect x="420" y="930" width="1080" height="24" fill="#2a1a12"/>')


PLAY_DEFS = '<linearGradient id="wallp" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0c080c"/><stop offset="1" stop-color="#2a1a22"/></linearGradient>'

# the four dolls of the family
PARENTS = peg_doll(M2 + 110, G0 - 40, 125, "#3a4a6a", "#2a1a10") + peg_doll(M2 + 175, G0 - 40, 115, "#7a3a4a", "#5a3a1a")
PONY = dict(dress="#2a2a34", hair="#6a4022", ponytail=True)

# ---------------------------------------------------------------- S1 house exterior
win = lambda x, y, c=WARM: lit_window(x, y, 56, 80, c)
s1 = f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(150, 560)}
{moon(1330, 210, 80)}
<path d="M0 820 C400 790 800 800 1200 810 C1500 815 1700 800 1920 805 L1920 1080 L0 1080Z" fill="#120f20"/>
{dead_tree(470, 840, 380)}
{dead_tree(1460, 840, 300, s=0.8)}
<g fill="#07060c">
<polygon points="680,840 680,470 960,250 1240,470 1240,840"/>
<polygon points="650,480 960,225 1270,480 1250,490 960,255 670,490"/>
<rect x="1110" y="300" width="44" height="120"/>
<polygon points="640,840 640,690 1280,690 1280,840"/>
<polygon points="620,700 960,640 1300,700"/>
</g>
{win(760, 520)}{win(1104, 520, "#9fb4e8")}{win(932, 390, "#6a5a4a")}
{win(760, 720)}{win(1104, 720)}
<rect x="925" y="720" width="70" height="120" fill="#1c120c"/>
<circle cx="1060" cy="680" r="40" fill="{WARM}" opacity="0.35" filter="url(#blur30)"/>
{fog(860, op=0.12)}
{grass(1080, 260, "#06050b", (20, 46))}
'''
save("s1", svg(s1, sky("sky1", "#04050d", "#16163a", "#33284a")))

# ---------------------------------------------------------------- S2 playroom with mom at doorway
s2 = f'''
{playroom_bg()}
<rect x="1240" y="300" width="230" height="630" fill="#ffcf8a"/>
<rect x="1240" y="300" width="230" height="630" fill="#ffb54a" filter="url(#blur30)" opacity="0.7"/>
<polygon points="1240,930 1470,930 1700,1080 1060,1080" fill="#ffb54a" opacity="0.18"/>
{figure(1355, 930, 520, "#0a0608")}
<g transform="translate(960 600) scale(0.5) translate(-960 -500)">{dollhouse(PARENTS)}</g>
<rect x="600" y="815" width="720" height="20" fill="#2a1a12"/>
<rect x="620" y="835" width="16" height="100" fill="#1a100a"/><rect x="1284" y="835" width="16" height="100" fill="#1a100a"/>
<circle cx="960" cy="600" r="420" fill="{WARM}" opacity="0.05" filter="url(#blur60)"/>
'''
save("s2", svg(s2, PLAY_DEFS))

# ---------------------------------------------------------------- S3 close: four dolls
CLOSE_BG = f'<rect width="{W}" height="{H}" fill="#0c080c"/><rect x="0" y="930" width="{W}" height="150" fill="#1a110c"/>'
s3 = CLOSE_BG + dollhouse(PARENTS)
save("s3", svg(s3))

# ---------------------------------------------------------------- S4 fifth doll on the couch
s4 = CLOSE_BG + dollhouse(PARENTS + peg_doll(L + 130, G0 - 74, 105, **PONY)) + glow(L + 130, G0 - 140, 70, RED, 0.25)
save("s4", svg(s4))

# S4b: fifth doll at the bottom of the stairs (cut)
s4b = CLOSE_BG + dollhouse(PARENTS + peg_doll(M1 + 40, G0 - 40, 105, **PONY), lamps=False) + glow(M1 + 40, G0 - 110, 80, RED, 0.3)
save("s4b", svg(s4b))

# ---------------------------------------------------------------- S5 zoom: doll at top of the stairs facing the door
LAND = G1 - 40
s5_house = dollhouse(PARENTS + peg_doll(M2 - 130, LAND, 110, facing=1, **PONY), lamps=False)
s5 = (CLOSE_BG + f'<g transform="translate(960 560) scale(2.2) translate({-(M2 - 110)} {-(G1 - 110)})">{s5_house}</g>'
      + glow(1000, 420, 160, RED, 0.18))
save("s5", svg(s5))

# ---------------------------------------------------------------- S6 empty landing, a hand pulling the doll away
hand = (f'<g fill="#140c0c">'
        f'<path d="M1920 760 C1700 740 1560 700 1430 640 L1380 600 C1360 580 1380 560 1400 570 L1470 600 L1440 520 C1430 495 1460 485 1475 505 L1510 580 '
        f'L1505 495 C1505 470 1540 470 1542 495 L1550 585 L1570 510 C1578 488 1608 495 1602 518 L1590 610 C1640 640 1760 660 1920 660Z"/></g>')
held = f'<g transform="translate(1470 470) rotate(-28)">{peg_doll(0, 140, 150, **PONY)}</g>'
s6_house = dollhouse(PARENTS, lamps=False, twin_light=False, dim=0.25)
s6 = (CLOSE_BG + f'<g transform="translate(860 560) scale(2.2) translate({-(M2 - 110)} {-(G1 - 110)})">{s6_house}</g>'
      + glow(860, 600, 90, RED, 0.2))
save("s6", svg(s6))


# ---------------------------------------------------------------- S7 / S9 real staircase from below
def real_stairs(extra="", door_glow=0.35):
    p = [f'<rect width="{W}" height="{H}" fill="#0b0809"/>']
    p.append('<polygon points="0,0 700,0 700,1080 0,1080" fill="url(#wl7)"/>')
    p.append('<polygon points="1920,0 1220,0 1220,1080 1920,1080" fill="url(#wr7)"/>')
    # upper landing and door
    p.append('<rect x="700" y="80" width="520" height="260" fill="#1a1214"/>')
    p.append('<rect x="860" y="110" width="150" height="230" fill="#0a0708"/>')
    p.append(f'<rect x="872" y="122" width="40" height="218" fill="#9fb4e8" opacity="{door_glow}"/>')
    p.append(f'<rect x="872" y="122" width="40" height="218" fill="#9fb4e8" opacity="{door_glow}" filter="url(#blur30)"/>')
    p.append('<polygon points="912,122 1000,108 1000,352 912,340" fill="#2a1a14"/>')
    # steps: from bottom (wide) to top (narrow)
    n = 12
    for i in range(n):
        t0 = i / n; t1 = (i + 1) / n
        y0 = 1080 - t0 * 740; y1 = 1080 - t1 * 740
        xl0 = 300 + t0 * 400; xr0 = 1620 - t0 * 400
        xl1 = 300 + t1 * 400; xr1 = 1620 - t1 * 400
        riser = f'#{0x22 - i:02x}{0x16 - i // 2:02x}{0x12 - i // 2:02x}'
        p.append(f'<polygon points="{xl0:.0f},{y0:.0f} {xr0:.0f},{y0:.0f} {xr1:.0f},{y0 - (y0 - y1) * .55:.0f} {xl1:.0f},{y0 - (y0 - y1) * .55:.0f}" fill="{riser}"/>')
        p.append(f'<polygon points="{xl1:.0f},{y0 - (y0 - y1) * .55:.0f} {xr1:.0f},{y0 - (y0 - y1) * .55:.0f} {xr1:.0f},{y1:.0f} {xl1:.0f},{y1:.0f}" fill="#3a2418"/>')
        p.append(f'<line x1="{xl1:.0f}" y1="{y1:.0f}" x2="{xr1:.0f}" y2="{y1:.0f}" stroke="#5a3822" stroke-width="3"/>')
    # banister on the right with balusters
    p.append('<line x1="1700" y1="980" x2="1240" y2="300" stroke="#140a06" stroke-width="18"/>')
    for i in range(14):
        t = i / 14
        x = 1700 - t * 460; y = 980 - t * 680
        p.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x - 20 * (1 - t):.0f}" y2="{y + 150 * (1 - t * .6):.0f}" stroke="#140a06" stroke-width="{8 - t * 4:.0f}"/>')
    p.append('<rect x="1680" y="960" width="44" height="120" fill="#140a06"/>')
    # night light on the landing
    p.append(glow(1150, 300, 60, WARM, 0.35))
    p.append(f'<circle cx="1150" cy="300" r="8" fill="{WARM}"/>')
    p.append(extra)
    p.append(fog(1000, op=0.06))
    return "".join(p)


STAIR_DEFS = ('<linearGradient id="wl7" x1="0" x2="1"><stop offset="0" stop-color="#140c0e"/><stop offset="1" stop-color="#2a1c1e"/></linearGradient>'
              '<linearGradient id="wr7" x1="1" x2="0"><stop offset="0" stop-color="#140c0e"/><stop offset="1" stop-color="#2a1c1e"/></linearGradient>')

# a long shadow climbing the left wall
shadow = (f'<g opacity="0.75" transform="translate(690 400) skewX(-12)">{figure(0, 440, 560, "#030203")}</g>')
s7 = real_stairs(shadow + f'<path d="M820 640 l20 -8" stroke="#000" stroke-width="2"/>')
save("s7", svg(s7, STAIR_DEFS))

s9 = real_stairs(f'{figure(960, 342, 250, "#030203")}{eyes(960, 120, 14, 4)}', door_glow=0.55)
save("s9", svg(s9, STAIR_DEFS))

# ---------------------------------------------------------------- S8 Mrs. Marlowe at the front door
s8 = f'''
<rect width="{W}" height="{H}" fill="#120c0c"/>
<rect x="0" y="0" width="{W}" height="920" fill="url(#hall8)"/>
<rect x="0" y="920" width="{W}" height="160" fill="#1f140e"/>
<rect x="700" y="180" width="520" height="740" fill="#24160e"/>
<rect x="730" y="210" width="460" height="710" fill="url(#night8)"/>
{stars(30, 200, 0.4)}
<g transform="translate(0 0)">
<rect x="730" y="210" width="460" height="710" fill="none"/>
</g>
<circle cx="1260" cy="260" r="16" fill="{WARM}"/>
{glow(1260, 260, 90, WARM, 0.5)}
<polygon points="730,920 1190,920 1400,1080 520,1080" fill="{WARM}" opacity="0.1"/>
{figure(960, 900, 560, "#050304")}
<path d="M900 560 C880 620 880 720 900 860 L1020 860 C1040 720 1040 620 1020 560Z" fill="#0a0607"/>
<ellipse cx="960" cy="402" rx="40" ry="50" fill="#d9d4cc" opacity="0.8"/>
<ellipse cx="960" cy="402" rx="44" ry="52" fill="#000" opacity="0.15"/>
<circle cx="946" cy="400" r="4" fill="#0a0607"/><circle cx="974" cy="400" r="4" fill="#0a0607"/>
<path d="M952 428 h16" stroke="#0a0607" stroke-width="3"/>
<path d="M914 400 C910 340 1010 330 1006 400 C1000 370 920 370 914 400Z" fill="#1a1010"/>
<g transform="translate(1340 920)">
<rect x="-40" y="-120" width="80" height="120" fill="#2a1a18"/>
<polygon points="-50,-120 0,-170 50,-120" fill="#1a1012"/>
<rect x="-28" y="-104" width="22" height="30" fill="#ffb54a" opacity="0.5"/>
</g>
{fog(900, op=0.07)}
'''
save("s8", svg(s8, '<linearGradient id="hall8" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#140c0c"/><stop offset="1" stop-color="#2e1e1a"/></linearGradient>'
                   '<linearGradient id="night8" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a0c1a"/><stop offset="1" stop-color="#1e2034"/></linearGradient>'))
