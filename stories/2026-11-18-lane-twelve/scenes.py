"""Lane Twelve: scenes drawn with scenekit + custom SVG."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

def pin(x, base, h, fill="#efe9dc", stripe="#b3261e"):
    w = h * 0.36
    return (f'<path d="M{x} {base - h} C{x + w*0.45} {base - h} {x + w*0.42} {base - h*0.78} {x + w*0.22} {base - h*0.66} '
            f'C{x + w*0.6} {base - h*0.5} {x + w*0.62} {base - h*0.2} {x + w*0.35} {base} L{x - w*0.35} {base} '
            f'C{x - w*0.62} {base - h*0.2} {x - w*0.6} {base - h*0.5} {x - w*0.22} {base - h*0.66} '
            f'C{x - w*0.42} {base - h*0.78} {x - w*0.45} {base - h} {x} {base - h}Z" fill="{fill}"/>'
            f'<rect x="{x - w*0.24:.1f}" y="{base - h*0.74:.1f}" width="{w*0.48:.1f}" height="{h*0.04:.1f}" fill="{stripe}"/>'
            f'<rect x="{x - w*0.24:.1f}" y="{base - h*0.68:.1f}" width="{w*0.48:.1f}" height="{h*0.04:.1f}" fill="{stripe}"/>')

def rack(cx, base, h, gap):
    out = []
    rows = [(3, 4), (2, 3), (1, 2), (0, 1)]  # back row first
    for r, n in rows:
        y = base - r * h * 0.08
        for i in range(n):
            x = cx + (i - (n - 1) / 2) * gap
            out.append(pin(x, y, h * (1 - r * 0.04)))
    return "".join(out)

VP = (960, 430)
def lanes(lit=True, pins=True):
    """Perspective of an alley from the approach; lane twelve centred."""
    out = [f'<rect width="{W}" height="{H}" fill="#07060b"/>',
           f'<rect x="0" y="0" width="{W}" height="430" fill="#0b0a12"/>']
    # ceiling masking units
    out.append('<rect x="0" y="250" width="1920" height="70" fill="#100e18"/><rect x="0" y="318" width="1920" height="6" fill="#1d1a2a"/>')
    # lane numbers above
    for k, x in [(10, 520), (11, 740), (12, 960), (13, 1180), (14, 1400)]:
        col = "#e8d9b0" if k == 12 else "#4a4558"
        out.append(f'<rect x="{x-48}" y="262" width="96" height="48" rx="6" fill="#16131f" stroke="{col}" stroke-width="2"/>'
                   f'<text x="{x}" y="298" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="34" fill="{col}">{k}</text>')
    # far wall / pin deck strip
    out.append('<rect x="0" y="380" width="1920" height="60" fill="#0e0c15"/>')
    # lanes: boundaries at bottom
    xs = list(range(-1120, 3300, 320))
    for i in range(len(xs) - 1):
        a, b = xs[i], xs[i + 1]
        def top(x): return VP[0] + (x - VP[0]) * 0.34
        ga, gb = a + 34, b - 34
        out.append(f'<polygon points="{top(a):.0f},440 {top(b):.0f},440 {b},1080 {a},1080" fill="#050408"/>')  # gutter base
        out.append(f'<polygon points="{top(ga):.0f},440 {top(gb):.0f},440 {gb},1080 {ga},1080" fill="url(#wood)"/>')
        for j in range(1, 8):
            x = ga + (gb - ga) * j / 8
            out.append(f'<line x1="{top(x):.0f}" y1="440" x2="{x:.0f}" y2="1080" stroke="#1b0f08" stroke-width="1.5" opacity="0.5"/>')
        # arrows
        m = (ga + gb) / 2
        ax = VP[0] + (m - VP[0]) * 0.55
        out.append(f'<polygon points="{ax-8:.0f},770 {ax+8:.0f},770 {ax:.0f},752" fill="#120a06" opacity="0.7"/>')
    # pin decks: dark for all but 12
    for k in [-2, -1, 1, 2]:
        px = 960 + k * 109
        out.append(f'<rect x="{px-44:.0f}" y="380" width="88" height="60" fill="#08070c"/>')
    if lit:
        out.append(glow(960, 410, 150, "#ffe2a8", 0.55))
        out.append('<rect x="890" y="330" width="140" height="110" fill="#3a2c1a"/><rect x="890" y="330" width="140" height="22" fill="#14111a"/>')
        if pins:
            out.append(rack(960, 438, 84, 30))
        out.append('<polygon points="916,440 1004,440 1160,1080 760,1080" fill="#ffd9a0" opacity="0.07"/>')
    # foreground approach / foul line + ball return silhouettes
    out.append('<rect x="0" y="1040" width="1920" height="40" fill="#050408"/>')
    out.append(fog(470, "#8a7fa0", 0.08, 60))
    return "".join(out)

WOOD = '''<linearGradient id="wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a1a0e"/><stop offset="1" stop-color="#5a3a1f"/></linearGradient>'''

def screen(rows, red_row=None, extra=""):
    """A CRT score monitor hanging in the dark."""
    body = [f'<rect width="{W}" height="{H}" fill="#06050a"/>', lanes(lit=False).replace(f'<rect width="{W}" height="{H}" fill="#07060b"/>', '') ]
    body.append('<rect width="1920" height="1080" fill="#000" opacity="0.55"/>')
    body.append('<rect x="930" y="0" width="16" height="200" fill="#14121c"/><rect x="975" y="0" width="16" height="200" fill="#14121c"/>')
    body.append('<rect x="540" y="180" width="840" height="560" rx="34" fill="#1a1822"/><rect x="560" y="200" width="800" height="520" rx="26" fill="#0c0b12"/>')
    body.append('<rect x="600" y="235" width="720" height="450" rx="30" fill="#04160f"/>')
    body.append('<rect x="600" y="235" width="720" height="450" rx="30" fill="#2bd67f" opacity="0.05"/>')
    # frame grid
    body.append(''.join(f'<line x1="{x}" y1="300" x2="{x}" y2="{300 + 90*max(1,len(rows))}" stroke="#1f6e48" stroke-width="2"/>' for x in range(880, 1300, 70)))
    body.append(f'<text x="640" y="280" font-family="{MONO}" font-size="30" fill="#2bd67f" opacity="0.8">LANE 12        FRAME 1</text>')
    for i, name in enumerate(rows):
        y = 300 + i * 90
        col = "#ff4d3d" if red_row == i else "#2bd67f"
        body.append(f'<rect x="630" y="{y}" width="660" height="80" fill="none" stroke="#1f6e48" stroke-width="2"/>')
        body.append(f'<text x="650" y="{y+56}" font-family="{MONO}" font-weight="bold" font-size="48" fill="{col}">{name}</text>')
        body.append(f'<text x="650" y="{y+56}" font-family="{MONO}" font-weight="bold" font-size="48" fill="{col}" filter="url(#blur8)" opacity="0.8">{name}</text>')
    body.append(''.join(f'<rect x="600" y="{y}" width="720" height="3" fill="#000" opacity="0.35"/>' for y in range(240, 685, 9)))
    body.append(extra)
    body.append('<rect x="520" y="160" width="880" height="600" fill="#2bd67f" opacity="0.07" filter="url(#blur60)"/>')
    return svg("".join(body), WOOD)

# S1 — the alley from the parking lot
def exterior(lights=True, walker=False):
    sign_col = "#ff3b2f" if lights else "#3a1512"
    win = "#ffcf7a" if lights else "#15121c"
    b = [f'<rect width="{W}" height="{H}" fill="url(#sky1)"/>', stars(140, 520), moon(1560, 190, 70),
         '<path d="M0 700 L1920 700 L1920 1080 L0 1080Z" fill="#100e17"/>',
         '<rect x="420" y="470" width="1100" height="250" fill="#0a0910"/>',
         '<polygon points="400,470 960,410 1540,470" fill="#0c0b13"/>']
    for x in range(520, 1440, 140):
        b.append(f'<rect x="{x}" y="560" width="90" height="70" fill="{win}" opacity="{0.85 if lights else 1}"/>')
        if lights: b.append(f'<rect x="{x}" y="560" width="90" height="70" fill="{win}" filter="url(#blur30)" opacity="0.5"/>')
    b.append(f'<rect x="900" y="590" width="120" height="130" fill="{"#e6b15e" if lights else "#120f18"}"/>')
    # sign pole and giant pin
    b.append('<rect x="1180" y="180" width="18" height="300" fill="#0a0910"/>')
    b.append(f'<g transform="translate(1189 290)">{pin(0, 110, 230, fill="none", stripe=sign_col).replace("fill=\"none\"", f"fill=\"none\" stroke=\"{sign_col}\" stroke-width=\"8\"")}</g>')
    if lights:
        b.append(glow(1189, 290, 140, "#ff3b2f", 0.35))
    b.append(f'<text x="960" y="520" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="58" letter-spacing="14" fill="{sign_col}">BOWL</text>')
    if lights: b.append(f'<text x="960" y="520" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="58" letter-spacing="14" fill="{sign_col}" filter="url(#blur8)">BOWL</text>')
    # lot lines, lamp, car
    b.append(''.join(f'<line x1="{x}" y1="1080" x2="{x*0.6+380:.0f}" y2="760" stroke="#2a2836" stroke-width="5"/>' for x in range(0, 1920, 260)))
    b.append('<rect x="560" y="300" width="10" height="460" fill="#08070c"/><rect x="560" y="300" width="70" height="10" fill="#08070c"/>')
    b.append(glow(620, 318, 60, "#f4e4b0", 0.6) + '<polygon points="600,318 640,318 760,780 480,780" fill="#f4e4b0" opacity="0.06"/>')
    b.append('<path d="M660 860 L700 800 L860 790 L900 850 L940 860 L940 900 L640 900Z" fill="#06050a"/><circle cx="700" cy="905" r="26" fill="#020203"/><circle cx="880" cy="905" r="26" fill="#020203"/>')
    if walker:
        b.append(figure(790, 900, 240, "#030204").replace('', ''))
    b.append(fog(760, "#9a90b0", 0.12, 90))
    return svg("".join(b), sky("sky1", "#04040b", "#171330", "#3a1f33"))

save("s1", exterior())

# S2 — lane twelve, empty, nothing on the deck
s2 = svg(lanes(lit=False), WOOD)
save("s2", s2)

# S3 — machine on twelve hums, pins set; mop bucket in foreground
s3 = svg(lanes(lit=True) +
         '<g transform="translate(1310 760)"><path d="M0 0 L160 0 L145 200 L15 200Z" fill="#c9a226" opacity="0.85"/><path d="M0 0 L160 0 L145 200 L15 200Z" fill="#000" opacity="0.55"/>'
         '<rect x="70" y="-420" width="12" height="440" fill="#0a090f" transform="rotate(12 76 0)"/><circle cx="25" cy="205" r="14" fill="#050408"/><circle cx="135" cy="205" r="14" fill="#050408"/></g>',
         WOOD)
save("s3", s3)

# S4 — score screen: NEXT
save("s4", screen(["NEXT"]))

# S5 — leaving: lights out, figure heading to car
save("s5", exterior(lights=False, walker=True))

# S6 — two players
save("s6", screen(["NEXT", "BRIGGS"], red_row=1))

# S7 — through the glass doors: pins already standing
s7 = svg(lanes(lit=True) +
         '<rect width="1920" height="1080" fill="#0a1220" opacity="0.35"/>'
         # door frames
         '<rect x="0" y="0" width="560" height="1080" fill="#050408"/><rect x="1360" y="0" width="560" height="1080" fill="#050408"/>'
         '<rect x="0" y="0" width="1920" height="200" fill="#050408"/><rect x="560" y="600" width="800" height="40" fill="#050408"/>'
         '<rect x="560" y="200" width="800" height="880" fill="#9fb4e8" opacity="0.05"/>'
         '<polygon points="620,200 720,200 600,1080 560,1080 560,600" fill="#cfd9ff" opacity="0.06"/>'
         '<rect x="1250" y="540" width="40" height="180" rx="10" fill="#1a1822"/>'
         # key in the lock, ring hanging
         '<rect x="1150" y="750" width="32" height="40" rx="6" fill="#2a2632"/>'
         '<rect x="1160" y="764" width="70" height="12" fill="#a7853f"/><circle cx="1245" cy="770" r="18" fill="none" stroke="#a7853f" stroke-width="7"/>'
         '<circle cx="1255" cy="820" r="34" fill="none" stroke="#8a6c30" stroke-width="5"/><rect x="1265" y="850" width="12" height="54" fill="#8a6c30" transform="rotate(-15 1271 850)"/>'
         + glow(1200, 770, 60, "#ffd28a", 0.25),
         WOOD)
save("s7", s7)

# S8 — one player: YOU
save("s8", screen(["YOU"], red_row=0, extra='<rect x="900" y="310" width="16" height="56" fill="#ff4d3d"/>'))

# S9 — ball return pushes a ball toward a hand
s9 = svg(f'''
<rect width="{W}" height="{H}" fill="#07060b"/>
{glow(960, 520, 300, "#7a1a14", 0.35)}
<rect x="0" y="760" width="1920" height="320" fill="#0d0b12"/>
<path d="M560 760 L560 520 C560 380 1360 380 1360 520 L1360 760Z" fill="#1b1824"/>
<path d="M620 760 L620 540 C620 430 1300 430 1300 540 L1300 760Z" fill="#0b0a10"/>
<rect x="520" y="740" width="880" height="60" rx="18" fill="#22202c"/>
<path d="M640 700 L1300 700 L1300 760 L640 760Z" fill="#141220"/>
<circle cx="900" cy="640" r="120" fill="url(#ball)"/>
<circle cx="870" cy="590" r="12" fill="#050408"/><circle cx="910" cy="585" r="12" fill="#050408"/><circle cx="890" cy="625" r="14" fill="#050408"/>
<circle cx="900" cy="640" r="150" fill="#ff3b2f" opacity="0.12" filter="url(#blur30)"/>
<path d="M900 760 C900 760 1000 800 1100 790" stroke="#ffd9a0" stroke-width="3" fill="none" opacity="0.15"/>
<g fill="#030204">
<path d="M1560 1080 C1500 960 1400 900 1260 880 C1210 872 1150 860 1100 840 C1080 832 1080 812 1100 808 C1150 800 1200 812 1250 820 L1240 790 C1236 770 1256 764 1266 780 L1300 830 L1310 780 C1314 760 1336 760 1336 782 L1336 840 L1360 790 C1370 772 1392 778 1386 798 L1370 860 C1440 880 1600 960 1680 1080Z"/>
</g>
{fog(820, "#8a7fa0", 0.08, 70)}
''', '<radialGradient id="ball" cx="0.35" cy="0.3" r="0.8"><stop offset="0" stop-color="#5a1e2a"/><stop offset="0.6" stop-color="#2a0c14"/><stop offset="1" stop-color="#0a0306"/></radialGradient>')
save("s9", s9)
print("ok")
