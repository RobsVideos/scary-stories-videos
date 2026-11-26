"""Scenes for The Low Tide (a winter beach rental and footprints on the night flats)."""
import sys, math; sys.path.insert(0, "../../toolkit")
from scenekit import *

RED = "#e0261d"
WARM = "#ffb54a"
DARK = "#06070c"
HAND = "Comic Relief, DejaVu Sans, sans-serif"
HZ = 560  # horizon line


def foot(x, y, s, rot=0, col="#0a0d16", op=0.85, sheen=True, crooked=True):
    """A bare footprint pointing 'up' (-y) before rotation; drawn on a squashed ground plane."""
    toes = [(-13, -46, 7.5), (-1, -50, 5.5), (9, -48, 5), (17, -43, 4.5), (23, -36, 4)]
    if crooked:
        toes[1] = (-4, -55, 5.5)  # the crooked second toe
    t = "".join(f'<ellipse cx="{a}" cy="{b}" rx="{r}" ry="{r * 1.25:.1f}"/>' for a, b, r in toes)
    body = ('<path d="M-4 40 C-18 38 -20 20 -16 8 C-12 -4 -22 -14 -20 -26 C-18 -38 -4 -42 8 -38 '
            'C22 -34 26 -22 20 -8 C14 6 16 22 12 32 C8 40 4 41 -4 40Z"/>')
    sh = (f'<path d="M-14 6 C-10 -6 -18 -16 -14 -26" stroke="#9fb3d8" stroke-width="2.5" fill="none" opacity="0.45"/>'
          if sheen else "")
    return (f'<g transform="translate({x:.0f} {y:.0f}) scale({s:.3f} {s * 0.45:.3f}) rotate({rot})">'
            f'<g fill="{col}" opacity="{op}">{body}{t}</g>{sh}</g>')


def trail(x0, y0, x1, y1, n=16, s0=1.0, s1=0.12, col="#0a0d16", away=True, sway=0.0, op=0.85):
    """A walking line of prints from near (x0,y0) to far (x1,y1), shrinking with distance."""
    o = []
    for i in range(n):
        t = i / (n - 1)
        u = 1 - (1 - t) ** 1.8
        x = x0 + (x1 - x0) * u + math.sin(t * 5) * sway
        y = y0 + (y1 - y0) * u
        s = s0 + (s1 - s0) * u
        side = -1 if i % 2 == 0 else 1
        x += side * 22 * s
        rot = 0 if away else 180
        o.append(foot(x, y, s, rot + side * 6, col=col, op=op * (0.55 + 0.45 * (1 - u))))
    return "".join(o)


def flats(top="#141a2c", bot="#1f2740", reflect=True, mx=1400):
    """Wet sand from horizon to bottom with a moon streak."""
    o = [f'<rect x="0" y="{HZ}" width="{W}" height="{H - HZ}" fill="url(#sand)"/>']
    if reflect:
        o.append(f'<path d="M{mx - 30} {HZ} L{mx + 30} {HZ} L{mx + 260} {H} L{mx - 260} {H}Z" fill="#c9d4ee" opacity="0.10" filter="url(#blur30)"/>')
        for k in range(14):
            yy = HZ + 12 + k * k * 2.6
            ww = 30 + k * 18
            o.append(f'<rect x="{mx - ww / 2 + rnd.randint(-30, 30):.0f}" y="{yy:.0f}" width="{ww}" height="{2 + k * 0.4:.1f}" fill="#e6ecfa" opacity="{0.35 - k * 0.018:.2f}"/>')
    # ripples / puddles
    for _ in range(40):
        yy = rnd.randint(HZ + 20, H)
        d = (yy - HZ) / (H - HZ)
        o.append(f'<ellipse cx="{rnd.randint(0, W)}" cy="{yy}" rx="{20 + 160 * d:.0f}" ry="{2 + 8 * d:.0f}" fill="#2f3b5c" opacity="0.35"/>')
    return "".join(o)


SAND_DEFS = '''<linearGradient id="sand" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#2a3352"/><stop offset="0.25" stop-color="#1a2036"/><stop offset="1" stop-color="#12141f"/></linearGradient>'''


def beach_house(x, y, col="#07080e", lit=True):
    """Stilt beach house; (x,y) = left edge of floor deck."""
    o = [f'<g fill="{col}">',
         f'<rect x="{x}" y="{y - 230}" width="420" height="230"/>',
         f'<polygon points="{x - 30},{y - 225} {x + 210},{y - 370} {x + 450},{y - 225}"/>',
         f'<rect x="{x + 300}" y="{y - 360}" width="30" height="80"/>',
         ''.join(f'<rect x="{x + px}" y="{y}" width="16" height="170"/>' for px in (10, 140, 270, 400)),
         f'<rect x="{x + 420}" y="{y - 10}" width="200" height="16"/>',
         ''.join(f'<rect x="{x + 430 + k * 38}" y="{y - 70}" width="6" height="62"/>' for k in range(5)),
         f'<rect x="{x + 420}" y="{y - 74}" width="200" height="8"/>',
         f'<rect x="{x + 600}" y="{y}" width="14" height="170"/>',
         '</g>']
    # stairs down to sand
    for k in range(9):
        o.append(f'<rect x="{x + 600 + k * 22}" y="{y + 8 + k * 19}" width="40" height="7" fill="{col}"/>')
    o.append(f'<line x1="{x + 610}" y1="{y - 60}" x2="{x + 800}" y2="{y + 120}" stroke="{col}" stroke-width="7"/>')
    if lit:
        o.append(lit_window(x + 60, y - 170, 90, 100))
        o.append(lit_window(x + 250, y - 170, 90, 100, color="#3a3f58"))
    # back door with tiny note
    o.append(f'<rect x="{x + 360}" y="{y - 190}" width="56" height="182" fill="#141623"/>')
    o.append(f'<rect x="{x + 372}" y="{y - 150}" width="26" height="30" fill="#d9d2bd" opacity="0.8"/>')
    return "".join(o)


def sea(y=HZ, op=1.0):
    o = [f'<rect x="0" y="{y - 30}" width="{W}" height="34" fill="#0c1222" opacity="{op}"/>']
    for k in range(6):
        o.append(f'<path d="M0 {y - 28 + k * 5} Q480 {y - 34 + k * 5} 960 {y - 28 + k * 5} T1920 {y - 28 + k * 5}" stroke="#4a5a85" stroke-width="1.5" fill="none" opacity="{0.4 * op:.2f}"/>')
    return "".join(o)


def dune_grass(y0, n, color):
    return grass(y0, n, color, (30, 70))


# ---------- S1: the beach house at night ----------
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk1)"/>
{stars(150, 480)}
{moon(1330, 220, 80)}
<rect x="0" y="600" width="{W}" height="60" fill="#0c1222"/>
{''.join(f'<path d="M0 {610 + k * 9} Q480 {604 + k * 9} 960 {610 + k * 9} T1920 {610 + k * 9}" stroke="#4a5a85" stroke-width="1.5" fill="none" opacity="0.35"/>' for k in range(5))}
<path d="M1270 605 L1390 605 L1460 660 L1200 660Z" fill="#dfe6f8" opacity="0.18" filter="url(#blur8)"/>
<path d="M0 700 C300 640 600 650 900 690 C1200 720 1500 660 1920 690 L1920 1080 L0 1080Z" fill="#1a2034"/>
{beach_house(560, 690)}
<path d="M0 860 C400 820 900 850 1300 860 C1600 870 1800 850 1920 860 L1920 1080 L0 1080Z" fill="#11141f"/>
{dune_grass(880, 180, "#0a0c14")}{dune_grass(1000, 240, "#07080e")}
<g stroke="#0a0c14" stroke-width="6">{''.join(f'<line x1="{200 + k * 70}" y1="{900 - k * 4}" x2="{205 + k * 70}" y2="{980 - k * 4}"/>' for k in range(8))}</g>
<path d="M200 930 {''.join(f'L{200 + k * 70} {935 - k * 4 + (k % 2) * 10}' for k in range(8))}" stroke="#0a0c14" stroke-width="3" fill="none"/>
{fog(820, op=0.12)}
''', SAND_DEFS + sky("sk1", "#04060e", "#141b33", "#2c3555")))

# ---------- S2: watching the tide pull back from the deck ----------
rail = "".join(f'<rect x="{x}" y="820" width="22" height="260" fill="#05060b"/>' for x in range(520, 1440, 115))
save("s2", svg(f'''
<rect width="{W}" height="{HZ}" fill="url(#sk2)"/>
{stars(170, 460)}
{moon(1180, 200, 70)}
{flats(mx=1180)}
{sea(HZ + 4)}
<path d="M0 {HZ + 120} C400 {HZ + 100} 800 {HZ + 130} 1200 {HZ + 115} C1500 {HZ + 105} 1700 {HZ + 120} 1920 {HZ + 110}" stroke="#9fb3d8" stroke-width="2" fill="none" opacity="0.35"/>
<path d="M0 {HZ + 230} C500 {HZ + 210} 1000 {HZ + 245} 1920 {HZ + 220}" stroke="#9fb3d8" stroke-width="2" fill="none" opacity="0.22"/>
{fog(HZ + 30, op=0.14, ry=70)}
<rect x="440" y="800" width="1040" height="26" fill="#05060b"/>
{rail}
<rect x="440" y="1030" width="1040" height="50" fill="#05060b"/>
<g fill="#05060b"><rect x="1330" y="760" width="70" height="44" rx="6"/><path d="M1340 760 q30 -40 50 0" stroke="#05060b" stroke-width="6" fill="none"/></g>
<ellipse cx="1365" cy="755" rx="22" ry="8" fill="#ffb54a" opacity="0.3" filter="url(#blur8)"/>
''', SAND_DEFS + sky("sk2", "#03050c", "#111832", "#2d3a60")))

# ---------- S3: footprints from the bottom of the steps out into the dark ----------
steps = "".join(f'<rect x="{300 + k * 26}" y="{620 + k * 50}" width="230" height="16" fill="#08090f"/>' for k in range(9))
save("s3", svg(f'''
<rect width="{W}" height="{HZ}" fill="url(#sk3)"/>
{stars(120, 440, 0.5)}
{moon(1500, 160, 55)}
{flats(mx=1500)}
{sea(HZ + 4, op=0.7)}
{fog(HZ + 10, op=0.22, ry=90)}
<rect x="290" y="560" width="16" height="520" fill="#08090f"/><rect x="510" y="560" width="16" height="520" fill="#08090f"/>
{steps}
<line x1="300" y1="560" x2="560" y2="1080" stroke="#08090f" stroke-width="10"/>
<path d="M640 1080 C700 900 900 700 1010 {HZ + 30}" stroke="#8fa3cf" stroke-width="120" fill="none" opacity="0.10" filter="url(#blur30)"/>
{trail(700, 1040, 1010, HZ + 30, n=18, s0=1.5, s1=0.14, sway=60, col="#03040a", op=1.0)}
<ellipse cx="1010" cy="{HZ + 30}" rx="220" ry="40" fill="#000" opacity="0.5" filter="url(#blur30)"/>
''', SAND_DEFS + sky("sk3", "#03040a", "#0d1328", "#26304f")))

# ---------- S4: my bare foot beside the print (top-down) ----------
grain = "".join(f'<circle cx="{rnd.randint(0, W)}" cy="{rnd.randint(0, H)}" r="{rnd.choice([1, 1.5, 2])}" fill="#4a5470" opacity="{rnd.uniform(.1, .4):.2f}"/>' for _ in range(900))
real_foot = ('<g transform="translate(1110 600) scale(5.2) rotate(-4)">'
             '<path d="M-4 40 C-18 38 -20 20 -16 8 C-12 -4 -22 -14 -20 -26 C-18 -38 -4 -42 8 -38 C22 -34 26 -22 20 -8 C14 6 16 22 12 32 C8 40 4 41 -4 40Z" fill="#5a6077"/>'
             '<path d="M-4 40 C-18 38 -20 20 -16 8 C-12 -4 -22 -14 -20 -26" stroke="#7b8299" stroke-width="1.5" fill="none" opacity="0.7"/>'
             '<g fill="#5a6077"><ellipse cx="-13" cy="-46" rx="7.5" ry="9"/><ellipse cx="-4" cy="-55" rx="5.5" ry="7"/>'
             '<ellipse cx="9" cy="-48" rx="5" ry="6.3"/><ellipse cx="17" cy="-43" rx="4.5" ry="5.6"/><ellipse cx="23" cy="-36" rx="4" ry="5"/></g>'
             '<g fill="#7b8299" opacity="0.6"><ellipse cx="-14" cy="-48" rx="3" ry="2.5"/><ellipse cx="-4.5" cy="-57" rx="2.2" ry="2"/></g>'
             '</g>')
print_ = ('<g transform="translate(800 590) scale(5.2) rotate(3)">'
          '<path d="M-4 40 C-18 38 -20 20 -16 8 C-12 -4 -22 -14 -20 -26 C-18 -38 -4 -42 8 -38 C22 -34 26 -22 20 -8 C14 6 16 22 12 32 C8 40 4 41 -4 40Z" fill="#090b12"/>'
          '<g fill="#090b12"><ellipse cx="-13" cy="-46" rx="7.5" ry="9"/><ellipse cx="-4" cy="-55" rx="5.5" ry="7"/>'
          '<ellipse cx="9" cy="-48" rx="5" ry="6.3"/><ellipse cx="17" cy="-43" rx="4.5" ry="5.6"/><ellipse cx="23" cy="-36" rx="4" ry="5"/></g>'
          '<path d="M-16 -10 C-12 -20 -20 -26 -16 -32" stroke="#a8bce4" stroke-width="1.4" fill="none" opacity="0.55"/>'
          '<path d="M10 20 C14 8 18 0 18 -10" stroke="#a8bce4" stroke-width="1" fill="none" opacity="0.35"/></g>')
save("s4", svg(f'''
<rect width="{W}" height="{H}" fill="#1a1f30"/>
<rect width="{W}" height="{H}" fill="url(#mlight)"/>
{grain}
{''.join(f'<path d="M0 {y} Q480 {y - 14} 960 {y} T1920 {y}" stroke="#262c42" stroke-width="10" fill="none" opacity="0.6"/>' for y in range(60, 1080, 120))}
<ellipse cx="800" cy="600" rx="190" ry="270" fill="#05060a" opacity="0.4" filter="url(#blur30)"/>
{print_}
<ellipse cx="1110" cy="620" rx="190" ry="260" fill="#000" opacity="0.35" filter="url(#blur30)" transform="translate(30 30)"/>
{real_foot}
<ellipse cx="770" cy="335" rx="30" ry="40" fill="none" stroke="{RED}" stroke-width="4" opacity="0.75"/>
<ellipse cx="1090" cy="335" rx="30" ry="40" fill="none" stroke="{RED}" stroke-width="4" opacity="0.75"/>
''', '<radialGradient id="mlight" cx="0.55" cy="0.4" r="0.6"><stop offset="0" stop-color="#3b4566" stop-opacity="0.8"/><stop offset="1" stop-color="#0a0c14" stop-opacity="0"/></radialGradient>'))

# ---------- S5: someone far out on the flats calls my name ----------
save("s5", svg(f'''
<rect width="{W}" height="{HZ}" fill="url(#sk5)"/>
{stars(90, 420, 0.45)}
{moon(960, 230, 95, "#e6e2d6")}
{flats(mx=960)}
{sea(HZ + 4)}
{trail(900, 1060, 960, HZ + 22, n=20, s0=1.1, s1=0.1, sway=30, op=0.8)}
{fog(HZ + 20, op=0.25, ry=80)}
{figure(960, HZ + 22, 150, "#020204")}
<ellipse cx="960" cy="{HZ + 24}" rx="40" ry="5" fill="#000" opacity="0.7"/>
{glow(960, HZ - 70, 80, "#9fb3d8", 0.12)}
{fog(900, op=0.10, ry=140)}
''', SAND_DEFS + sky("sk5", "#02030a", "#0f1430", "#33406a")))

# ---------- S6: back inside, door locked ----------
boards = "".join(f'<rect x="0" y="{y}" width="{W}" height="4" fill="#0c0806"/>' for y in range(860, 1080, 44))
save("s6", svg(f'''
<rect width="{W}" height="{H}" fill="#140f0e"/>
{''.join(f'<rect x="{x}" y="0" width="3" height="860" fill="#0d0908"/>' for x in range(0, W, 70))}
<rect x="0" y="860" width="{W}" height="220" fill="#1e1510"/>{boards}
<rect x="700" y="170" width="520" height="700" fill="#0b0808"/>
<rect x="730" y="200" width="460" height="670" fill="#2a1c15"/>
<rect x="790" y="250" width="340" height="250" fill="#0d1530"/>
<rect x="790" y="250" width="340" height="250" fill="#7f95c8" opacity="0.18"/>
<circle cx="1060" cy="300" r="22" fill="#e6e2d6" opacity="0.9"/>
<rect x="790" y="430" width="340" height="70" fill="#1a2036"/>
<line x1="960" y1="250" x2="960" y2="500" stroke="#2a1c15" stroke-width="10"/>
<line x1="790" y1="375" x2="1130" y2="375" stroke="#2a1c15" stroke-width="10"/>
<rect x="830" y="560" width="110" height="80" fill="#d9d2bd"/>
<g stroke="#2b2b34" stroke-width="3">{''.join(f'<line x1="842" y1="{578 + k * 14}" x2="{926 - k * 9}" y2="{578 + k * 14}"/>' for k in range(4))}</g>
<rect x="1110" y="560" width="40" height="70" rx="6" fill="#a7853f"/>
<rect x="1100" y="590" width="60" height="12" fill="#c9a35a"/>
<circle cx="1140" cy="680" r="16" fill="#a7853f"/>
<polygon points="790,500 1130,500 1260,860 700,860" fill="#7f95c8" opacity="0.05"/>
<g fill="#050304"><path d="M420 1080 L440 620 C440 540 480 500 540 500 C600 500 640 540 640 620 L660 1080Z"/><ellipse cx="540" cy="440" rx="62" ry="74"/></g>
{glow(1520, 520, 160, WARM, 0.18)}
<g fill="#0b0808"><rect x="1500" y="560" width="40" height="300"/><path d="M1450 470 L1590 470 L1560 560 L1480 560Z" fill="#3a2414"/></g>
<path d="M1460 480 L1580 480 L1556 550 L1484 550Z" fill="{WARM}" opacity="0.55"/>
'''))

# ---------- S7: sunrise, tide back in, one new set of prints coming out of the water ----------
steps7 = "".join(f'<rect x="{1180 + k * 24}" y="{430 + k * 46}" width="210" height="14" fill="#151320"/>' for k in range(9))
save("s7", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk7)"/>
{glow(560, 470, 180, "#e58a7a", 0.35)}
<circle cx="560" cy="500" r="60" fill="#f2b8a0" opacity="0.8"/>
<rect x="0" y="470" width="{W}" height="150" fill="#3e4866"/>
{''.join(f'<path d="M0 {480 + k * 14} Q480 {474 + k * 14} 960 {480 + k * 14} T1920 {480 + k * 14}" stroke="#8a97bd" stroke-width="2" fill="none" opacity="0.4"/>' for k in range(10))}
<path d="M360 480 L760 480 L860 620 L260 620Z" fill="#f2b8a0" opacity="0.18" filter="url(#blur8)"/>
<path d="M0 620 C400 600 800 640 1200 615 C1500 600 1700 625 1920 610" stroke="#dfe6f8" stroke-width="5" fill="none" opacity="0.6"/>
<path d="M0 622 C400 602 800 642 1200 617 C1500 602 1700 627 1920 612 L1920 1080 L0 1080Z" fill="url(#sand7)"/>
{''.join(foot(600 + i * 52 + (14 if i % 2 else -14), 650 + i * i * 1.9 + i * 10, 0.35 + i * 0.07, 120 + (8 if i % 2 else -8), col="#1a1824", op=1.0) for i in range(11))}
<rect x="1170" y="380" width="16" height="700" fill="#151320"/><rect x="1380" y="380" width="16" height="700" fill="#151320"/>
{steps7}
<line x1="1180" y1="380" x2="1420" y2="840" stroke="#151320" stroke-width="10"/>
{fog(560, "#e8c3c0", 0.12, 90)}
''', sky("sk7", "#2a2a46", "#7b6b86", "#d99a8e") +
     '<linearGradient id="sand7" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6a6378"/><stop offset="1" stop-color="#2a2636"/></linearGradient>'))

# ---------- S8: the note, now in my handwriting ----------
lines8 = ["When the tide goes out", "at night, you'll see", "footprints in the sand.", "DON'T FOLLOW THEM."]
txt = "".join(f'<text x="0" y="{k * 78}" font-family="{HAND}" font-size="{48 if k < 3 else 48}" fill="{"#1c2a5a" if k < 3 else "#7a1414"}" '
              f'font-weight="{"normal" if k < 3 else "bold"}" transform="rotate({-1.5 + k * 0.8})">{s}</text>' for k, s in enumerate(lines8))
save("s8", svg(f'''
<rect width="{W}" height="{H}" fill="#24170f"/>
{''.join(f'<rect x="{x}" y="0" width="{rnd.randint(2, 5)}" height="{H}" fill="#1a100a" opacity="0.7"/>' for x in range(0, W, 37))}
<rect x="1360" y="430" width="70" height="140" rx="10" fill="#8a6c34"/><circle cx="1395" cy="520" r="16" fill="#3a2a12"/>
<g transform="translate(960 540) rotate(-2)">
<rect x="-330" y="-250" width="660" height="500" fill="#000" opacity="0.45" filter="url(#blur30)" transform="translate(16 20)"/>
<rect x="-330" y="-250" width="660" height="500" fill="#e2dac3"/>
<rect x="-330" y="-250" width="660" height="500" fill="url(#paper)"/>
<rect x="-90" y="-272" width="180" height="44" fill="#d9d4bf" opacity="0.75" transform="rotate(3)"/>
<path d="M-200 180 q30 -30 80 -10 q40 20 90 -6" stroke="#6b5a3a" stroke-width="3" fill="none" opacity="0.4"/>
<ellipse cx="190" cy="170" rx="70" ry="44" fill="#8a7650" opacity="0.18" filter="url(#blur8)"/>
<g transform="translate(-290 -140)">{txt}</g>
</g>
{glow(1300, 200, 200, WARM, 0.12)}
''', '<radialGradient id="paper" cx="0.5" cy="0.5" r="0.7"><stop offset="0.6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#3a2a10" stop-opacity="0.35"/></radialGradient>'))
