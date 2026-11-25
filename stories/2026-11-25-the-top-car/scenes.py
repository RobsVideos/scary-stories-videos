"""Scenes for The Top Car."""
import sys, math; sys.path.insert(0, "../../toolkit")
from scenekit import *

RED = "#ff2a22"
WARM = "#ffb54a"
JACKET = "#b0291f"
DARK = "#07060c"


def gondola(x, y, s=1.0, tilt=0, fill="#101018", trim="#2a2a3a", lit=False, rider=None, bar=True):
    """Car hanging from pivot (x, y). s=1 -> about 80 wide."""
    o = [f'<g transform="translate({x} {y}) rotate({tilt}) scale({s})">']
    o.append(f'<line x1="0" y1="0" x2="0" y2="38" stroke="{fill}" stroke-width="6"/>')
    o.append(f'<path d="M-44 38 L44 38 L38 46 L-38 46Z" fill="{trim}"/>')  # canopy
    o.append(f'<line x1="-34" y1="46" x2="-34" y2="72" stroke="{fill}" stroke-width="4"/><line x1="34" y1="46" x2="34" y2="72" stroke="{fill}" stroke-width="4"/>')
    if rider:
        o.append(rider)
    o.append(f'<path d="M-42 72 L42 72 L36 112 Q0 126 -36 112Z" fill="{fill}"/>')  # tub
    o.append(f'<path d="M-42 72 L42 72 L41 78 L-41 78Z" fill="{trim}"/>')
    if bar:
        o.append(f'<line x1="-40" y1="66" x2="40" y2="66" stroke="{trim}" stroke-width="4"/>')
    if lit:
        o.append(f'<circle cx="0" cy="44" r="4" fill="{WARM}"/>')
    o.append('</g>')
    return "".join(o)


def wheel(cx, cy, R, rot=0, n=12, col="#0b0b14", lights=False, car_fill="#0d0d16", car_trim="#262636",
          skip_top=False, base=900, legs=True):
    o = []
    if legs:
        for d in (-1, 1):
            o.append(f'<path d="M{cx} {cy} L{cx + d * R * .62:.0f} {base}" stroke="{col}" stroke-width="22"/>')
            o.append(f'<path d="M{cx} {cy} L{cx + d * R * .40:.0f} {base}" stroke="{col}" stroke-width="12"/>')
        o.append(f'<line x1="{cx - R * .55:.0f}" y1="{cy + (base - cy) * .75:.0f}" x2="{cx + R * .55:.0f}" y2="{cy + (base - cy) * .75:.0f}" stroke="{col}" stroke-width="8"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{col}" stroke-width="12"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{R * .9:.0f}" fill="none" stroke="{col}" stroke-width="6"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{R * .25:.0f}" fill="none" stroke="{col}" stroke-width="5"/>')
    for i in range(n * 2):
        a = math.radians(rot + i * 180 / n)
        o.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + R * math.cos(a):.0f}" y2="{cy + R * math.sin(a):.0f}" stroke="{col}" stroke-width="4"/>')
    if lights:
        for i in range(n * 4):
            a = math.radians(rot + i * 90 / n)
            px, py = cx + R * math.cos(a), cy + R * math.sin(a)
            o.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="5" fill="#ffd27a"/>')
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{R + 20}" fill="none" stroke="{WARM}" stroke-width="30" opacity="0.25" filter="url(#blur30)"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="22" fill="{col}"/>')
    cars = []
    for i in range(n):
        a = math.radians(rot + i * 360 / n - 90)
        px, py = cx + R * math.cos(a), cy + R * math.sin(a)
        if skip_top and abs(py - (cy - R)) < 2:
            continue
        cars.append(gondola(px, py, R / 380, fill=car_fill, trim=car_trim, lit=lights))
    return "".join(o) + "".join(cars)


def tent(x, base, w, h, c1, c2):
    stripes = "".join(f'<polygon points="{x},{base - h} {x - w / 2 + k * w / 6:.0f},{base} {x - w / 2 + (k + .5) * w / 6:.0f},{base}" fill="{c2}"/>' for k in range(6))
    return (f'<polygon points="{x},{base - h} {x - w / 2},{base} {x + w / 2},{base}" fill="{c1}"/>{stripes}'
            f'<line x1="{x}" y1="{base - h}" x2="{x}" y2="{base - h - 30}" stroke="{c1}" stroke-width="4"/>'
            f'<polygon points="{x},{base - h - 30} {x + 24},{base - h - 22} {x},{base - h - 14}" fill="{c2}"/>')


def bulbs(x1, y1, x2, y2, sag, n, color="#ffcf70", op=1):
    o = [f'<path d="M{x1} {y1} Q{(x1 + x2) / 2} {max(y1, y2) + sag} {x2} {y2}" stroke="#05050a" stroke-width="2" fill="none"/>']
    for k in range(1, n):
        t = k / n
        bx = (1 - t) ** 2 * x1 + 2 * (1 - t) * t * (x1 + x2) / 2 + t * t * x2
        by = (1 - t) ** 2 * y1 + 2 * (1 - t) * t * (max(y1, y2) + sag) + t * t * y2
        o.append(f'<circle cx="{bx:.0f}" cy="{by + 6:.0f}" r="5" fill="{color}" opacity="{op}"/>')
    return "".join(o)


def person(cx, base, h=300, color="#050407", jacket=None, cap=True, arm_up=None):
    """Teen in a work jacket, seen from behind."""
    sh = h * .13
    o = [f'<g>']
    o.append(f'<rect x="{cx - sh * .55:.0f}" y="{base - h * .48:.0f}" width="{sh * .45:.0f}" height="{h * .48:.0f}" fill="{color}"/>')
    o.append(f'<rect x="{cx + sh * .1:.0f}" y="{base - h * .48:.0f}" width="{sh * .45:.0f}" height="{h * .48:.0f}" fill="{color}"/>')
    jc = jacket or color
    o.append(f'<path d="M{cx - sh:.0f} {base - h * .45:.0f} L{cx - sh * 1.05:.0f} {base - h * .78:.0f} Q{cx:.0f} {base - h * .86:.0f} {cx + sh * 1.05:.0f} {base - h * .78:.0f} L{cx + sh:.0f} {base - h * .45:.0f}Z" fill="{jc}"/>')
    # arms
    o.append(f'<path d="M{cx - sh * 1.02:.0f} {base - h * .76:.0f} L{cx - sh * 1.2:.0f} {base - h * .48:.0f}" stroke="{jc}" stroke-width="{h * .07:.0f}" stroke-linecap="round"/>')
    if arm_up:
        o.append(f'<path d="M{cx + sh * 1.02:.0f} {base - h * .76:.0f} L{cx + sh * 1.6:.0f} {base - h * 1.0:.0f}" stroke="{jc}" stroke-width="{h * .07:.0f}" stroke-linecap="round"/>')
        o.append(f'<circle cx="{cx + sh * 1.65:.0f}" cy="{base - h * 1.04:.0f}" r="{h * .04:.0f}" fill="{color}"/>')
    else:
        o.append(f'<path d="M{cx + sh * 1.02:.0f} {base - h * .76:.0f} L{cx + sh * 1.2:.0f} {base - h * .48:.0f}" stroke="{jc}" stroke-width="{h * .07:.0f}" stroke-linecap="round"/>')
    o.append(f'<circle cx="{cx}" cy="{base - h * .9:.0f}" r="{h * .075:.0f}" fill="{color}"/>')
    if cap:
        o.append(f'<path d="M{cx - h * .08:.0f} {base - h * .92:.0f} Q{cx} {base - h * 1.0:.0f} {cx + h * .08:.0f} {base - h * .92:.0f}Z" fill="{color}"/>')
    o.append('</g>')
    return "".join(o)


def moon2(cx, cy, r, color="#f1e9d3"):
    return ("".join(f'<circle cx="{cx}" cy="{cy}" r="{r * (1 + k * 0.1):.0f}" fill="{color}" opacity="0.012"/>' for k in range(22, 0, -1)) +
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>'
            f'<g fill="#000" opacity="0.07"><circle cx="{cx - r * .27:.0f}" cy="{cy - r * .23:.0f}" r="{r * .24:.0f}"/>'
            f'<circle cx="{cx + r * .27:.0f}" cy="{cy + r * .27:.0f}" r="{r * .16:.0f}"/></g>')

BIG = '<radialGradient id="softglow"><stop offset="0" stop-color="#f1e9d3"/><stop offset="0.35" stop-color="#f1e9d3" stop-opacity="0.45"/><stop offset="1" stop-color="#f1e9d3" stop-opacity="0"/></radialGradient><radialGradient id="warmglow"><stop offset="0" stop-color="#ffb54a" stop-opacity="1"/><stop offset="1" stop-color="#ffb54a" stop-opacity="0"/></radialGradient><filter id="bigblur" x="-1" y="-1" width="3" height="3"><feGaussianBlur stdDeviation="50"/></filter>'
SKY_DUSK = BIG + sky("dusk", "#0b0a1c", "#2a1a3c", "#5a2e3a")
SKY_NIGHT = BIG + sky("night", "#03040a", "#0c1022", "#1a1d30")

# ---------------------------------------------------------------- s1: lit wheel, old operator
s1 = f'''
<rect width="{W}" height="{H}" fill="url(#dusk)"/>
{stars(120, 500, 0.6)}
{moon2(1500, 180, 60)}
<path d="M0 820 C400 790 1500 800 1920 810 L1920 1080 L0 1080Z" fill="#120e1c"/>
{tent(520, 900, 300, 220, "#2a0e14", "#3d1820")}{tent(1420, 900, 340, 240, "#1c0e1e", "#2c1430")}
{wheel(960, 440, 340, rot=8, lights=True, car_fill="#14121e", car_trim="#5a1e22")}
{bulbs(200, 640, 700, 700, 60, 10)}{bulbs(1220, 700, 1720, 640, 60, 10)}
<rect x="1080" y="790" width="130" height="110" fill="#0a0910"/>
<polygon points="1070,790 1220,790 1200,770 1090,770" fill="#16131f"/>
{lit_window(1110, 810, 70, 44)}
{figure(1270, 902, 210, "#040306")}
<path d="M1235 735 q30 -14 70 0 l-8 -8 q-27 -10 -54 0Z" fill="#040306"/>
<rect x="0" y="900" width="{W}" height="180" fill="#0a0812"/>
{grass(1080, 240, "#06050a", (14, 40))}
{fog(880, "#d0a8a0", 0.10)}
'''
save("s1", svg(s1, SKY_DUSK))

# ---------------------------------------------------------------- s2: empty car at the platform, flashlight
s2 = f'''
<rect width="{W}" height="{H}" fill="url(#dusk)"/>
{stars(60, 300, 0.4)}
<circle cx="960" cy="-260" r="900" fill="none" stroke="#0a0912" stroke-width="40"/>
<g stroke="#0a0912" stroke-width="10">{''.join(f'<line x1="960" y1="-260" x2="{960 + 900 * math.cos(math.radians(a)):.0f}" y2="{-260 + 900 * math.sin(math.radians(a)):.0f}"/>' for a in range(40, 150, 18))}</g>
<rect x="0" y="830" width="{W}" height="250" fill="#120f18"/>
<rect x="0" y="830" width="{W}" height="12" fill="#2a2430"/>
<g stroke="#1e1a24" stroke-width="3">{''.join(f'<line x1="{x}" y1="842" x2="{x - 80}" y2="1080"/>' for x in range(0, 2000, 120))}</g>
<g transform="translate(960 260) scale(4.6)">
<line x1="0" y1="0" x2="0" y2="38" stroke="#0e0d16" stroke-width="5"/>
<path d="M-44 38 L44 38 L38 46 L-38 46Z" fill="#6a1e22"/>
<line x1="-34" y1="46" x2="-34" y2="72" stroke="#0e0d16" stroke-width="3"/><line x1="34" y1="46" x2="34" y2="72" stroke="#0e0d16" stroke-width="3"/>
<rect x="-30" y="60" width="60" height="14" rx="3" fill="#2a2030"/>
<path d="M-42 72 L42 72 L36 112 Q0 126 -36 112Z" fill="#1c1824"/>
<path d="M-42 72 L42 72 L41 78 L-41 78Z" fill="#6a1e22"/>
<line x1="-40" y1="66" x2="40" y2="66" stroke="#8a8a96" stroke-width="2.5"/>
<text x="0" y="100" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="11" fill="#d9cfc0" opacity="0.8">7</text>
</g>
<polygon points="560,1080 760,1080 1020,560 940,540" fill="#fff2c8" opacity="0.10"/>
<ellipse cx="985" cy="560" rx="160" ry="110" fill="#fff2c8" opacity="0.16" filter="url(#blur30)"/>
<g transform="translate(640 1000) rotate(-28)">
<rect x="-30" y="-10" width="60" height="140" rx="12" fill="{JACKET}"/>
<rect x="-18" y="-80" width="36" height="90" rx="6" fill="#1a1a20"/>
<rect x="-24" y="-96" width="48" height="22" rx="4" fill="#2a2a30"/>
<ellipse cx="0" cy="-98" rx="20" ry="6" fill="#fff6d8"/>
</g>
{fog(900, "#c0a0a8", 0.08)}
'''
save("s2", svg(s2, SKY_DUSK))

# ---------------------------------------------------------------- s3: the big switch, fair goes dark
s3 = f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(160, 600, 0.7)}
{moon2(1700, 150, 50)}
{wheel(1300, 470, 300, rot=0, car_fill="#090910", car_trim="#141420", legs=True, base=860)}
{tent(560, 860, 300, 200, "#0b0a12", "#100e18")}
{bulbs(0, 600, 800, 660, 50, 14, "#2a2420")}
<rect x="0" y="860" width="{W}" height="220" fill="#08070c"/>
<rect x="640" y="380" width="380" height="540" rx="10" fill="#3a3c44"/>
<rect x="660" y="400" width="340" height="500" rx="6" fill="#2a2c33"/>
<rect x="700" y="430" width="260" height="46" fill="#d6c340"/>
<text x="830" y="465" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="30" fill="#141414">MAIN POWER</text>
<rect x="790" y="560" width="80" height="260" rx="10" fill="#18191e"/>
<g transform="rotate(28 830 790)">
<rect x="818" y="560" width="24" height="230" fill="#9a9ca4"/>
<rect x="790" y="530" width="80" height="50" rx="12" fill="{RED}"/>
</g>
<circle cx="830" cy="790" r="26" fill="#55575e"/>
<text x="900" y="600" font-family="{SANS}" font-size="24" fill="#8a8c90">ON</text>
<text x="900" y="820" font-family="{SANS}" font-size="24" fill="#8a8c90">OFF</text>
<circle cx="720" cy="860" r="10" fill="#3a1010"/>
<circle cx="700" cy="1080" r="0"/>
<g transform="translate(980 540) rotate(30)">
<path d="M0 0 C40 -10 90 -10 110 10 L120 60 C80 70 30 70 0 50Z" fill="{JACKET}"/>
<ellipse cx="-6" cy="24" rx="32" ry="24" fill="#c89878"/>
</g>
{fog(900, "#7a84a0", 0.12)}
'''
save("s3", svg(s3, SKY_NIGHT))

# ---------------------------------------------------------------- s4: dark wheel, one car rocking at the top
def top_wheel(tilt, rider=None, red=False):
    return f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(200, 700, 0.8)}
{moon2(960, 230, 120, "#e8e2d0")}
{wheel(960, 520, 360, rot=0, car_fill="#08080e", car_trim="#121220", skip_top=True, base=1000)}
{gondola(960, 160, 1.5, tilt=tilt, fill="#06060b", trim="#3a1a22", rider=rider)}
<path d="M870 360 q90 40 180 0" stroke="#c8ccdc" stroke-width="4" fill="none" opacity="0.45"/>
<path d="M840 385 q120 50 240 0" stroke="#c8ccdc" stroke-width="2" fill="none" opacity="0.22"/>
{glow(960, 250, 110, "#ff2a22", 0.10 if red else 0.0)}
<rect x="0" y="960" width="{W}" height="120" fill="#06050a"/>
{fog(980, "#7a84a0", 0.14)}
'''
save("s4", svg(top_wheel(14), SKY_NIGHT))

# ---------------------------------------------------------------- s5: looking up at the car; a small hand on the bar
s5 = f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(220, 1080, 0.8)}
{moon2(1250, 220, 55)}
<circle cx="960" cy="1500" r="1150" fill="none" stroke="#0a0a12" stroke-width="40"/>
<g stroke="#0a0a12" stroke-width="12">{''.join(f'<line x1="960" y1="1500" x2="{960 + 1150 * math.cos(math.radians(a)):.0f}" y2="{1500 + 1150 * math.sin(math.radians(a)):.0f}"/>' for a in range(210, 340, 15))}</g>
<g transform="translate(960 340) rotate(-8) scale(5.2)">
<line x1="0" y1="-30" x2="0" y2="38" stroke="#0a0a12" stroke-width="6"/>
<path d="M-44 38 L44 38 L38 46 L-38 46Z" fill="#1c1218"/>
<line x1="-34" y1="46" x2="-34" y2="72" stroke="#0a0a12" stroke-width="4"/><line x1="34" y1="46" x2="34" y2="72" stroke="#0a0a12" stroke-width="4"/>
<path d="M-42 72 L42 72 L36 112 Q0 126 -36 112Z" fill="#0b0a12"/>
<path d="M-42 72 L42 72 L41 78 L-41 78Z" fill="#24161c"/>
<line x1="-40" y1="68" x2="40" y2="68" stroke="#3a3440" stroke-width="3"/>
<g fill="#c9ccd6"><ellipse cx="8" cy="67" rx="6" ry="3.2"/>
<rect x="3" y="63.5" width="2.2" height="5" rx="1"/><rect x="6" y="62.5" width="2.2" height="5.5" rx="1"/><rect x="9" y="62.8" width="2.2" height="5.3" rx="1"/><rect x="12" y="64" width="2" height="4.5" rx="1"/></g>
</g>
<ellipse cx="1000" cy="690" rx="70" ry="40" fill="#c9ccd6" opacity="0.14" filter="url(#blur30)"/>
{fog(760, "#8a94b0", 0.10)}
'''
save("s5", svg(s5, SKY_NIGHT))

# ---------------------------------------------------------------- s6: small me at the base, huge dark wheel
s6 = f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(220, 800, 0.8)}
{moon2(960, 70, 70)}
{wheel(960, 340, 290, rot=0, car_fill="#07070d", car_trim="#101018", skip_top=True, base=780)}
{gondola(960, 50, 290 / 380, tilt=-6, fill="#08080e", trim="#24161c")}
<rect x="0" y="780" width="{W}" height="300" fill="#07060b"/>
<rect x="740" y="770" width="440" height="18" fill="#141320"/>
{person(1060, 790, 230, jacket=JACKET)}
<ellipse cx="1060" cy="792" rx="70" ry="10" fill="#000" opacity="0.6"/>
{fog(820, "#8a94b0", 0.16, 120)}
{fog(600, "#8a94b0", 0.05)}
'''
save("s6", svg(s6, SKY_NIGHT))

# ---------------------------------------------------------------- s7: pushing the lever, wheel groans
s7 = f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(100, 400, 0.6)}
<g opacity="0.85">{wheel(960, 160, 420, rot=10, car_fill="#08080e", car_trim="#121220", legs=False)}</g>
<g opacity="0.25">{wheel(960, 160, 420, rot=18, car_fill="#08080e", car_trim="#121220", legs=False)}</g>
<rect x="500" y="620" width="920" height="460" fill="#1d1e24"/>
<rect x="500" y="620" width="920" height="16" fill="#34353d"/>
<rect x="560" y="690" width="300" height="150" rx="6" fill="#101116"/>
<g>{''.join(f'<circle cx="{600 + k * 55}" cy="740" r="14" fill="{c}"/>' for k, c in enumerate(["#2a3a20", "#3a3420", "#3a1414", "#1e2a3a", "#2a2a2a"]))}</g>
<circle cx="710" cy="800" r="18" fill="{RED}"/>{glow(710, 800, 50, RED, 0.5)}
<rect x="1060" y="660" width="40" height="220" rx="8" fill="#0a0a0e"/>
<g transform="rotate(-30 1080 860)">
<rect x="1070" y="560" width="20" height="300" fill="#8a8c94"/>
<circle cx="1080" cy="560" r="34" fill="#141418"/>
</g>
<g transform="translate(860 520) rotate(-12)">
<path d="M-60 120 C-20 40 40 10 90 0 L110 40 C60 60 10 100 -20 160Z" fill="{JACKET}"/>
<ellipse cx="110" cy="16" rx="34" ry="28" fill="#c89878"/>
</g>
{glow(960, 640, 300, WARM, 0.08)}
'''
save("s7", svg(s7, SKY_NIGHT))

# ---------------------------------------------------------------- s8: car at the bottom, empty, bar locked, seat warm
s8 = f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(80, 300, 0.4)}
<circle cx="960" cy="-280" r="880" fill="none" stroke="#0a0912" stroke-width="40"/>
<g stroke="#0a0912" stroke-width="10">{''.join(f'<line x1="960" y1="-280" x2="{960 + 880 * math.cos(math.radians(a)):.0f}" y2="{-280 + 880 * math.sin(math.radians(a)):.0f}"/>' for a in range(40, 150, 18))}</g>
<rect x="0" y="830" width="{W}" height="250" fill="#0f0d15"/>
<rect x="0" y="830" width="{W}" height="12" fill="#22202c"/>
<circle cx="960" cy="480" r="420" fill="url(#warmglow)" opacity="0.28"/><rect x="1300" y="300" width="12" height="530" fill="#0a0910"/><circle cx="1306" cy="300" r="18" fill="#ffd890"/><circle cx="1306" cy="300" r="120" fill="url(#warmglow)" opacity="0.5"/>
<g transform="translate(960 240) scale(4.8)">
<line x1="0" y1="0" x2="0" y2="38" stroke="#0e0d16" stroke-width="5"/>
<path d="M-44 38 L44 38 L38 46 L-38 46Z" fill="#3a1418"/>
<line x1="-34" y1="46" x2="-34" y2="72" stroke="#0e0d16" stroke-width="3"/><line x1="34" y1="46" x2="34" y2="72" stroke="#0e0d16" stroke-width="3"/>
<rect x="-30" y="60" width="60" height="14" rx="3" fill="#3a2028"/>
<path d="M-42 72 L42 72 L36 112 Q0 126 -36 112Z" fill="#14121c"/>
<path d="M-42 72 L42 72 L41 78 L-41 78Z" fill="#3a1418"/>
<line x1="-40" y1="66" x2="40" y2="66" stroke="#b0b0bc" stroke-width="2.5"/>
<rect x="-6" y="63" width="12" height="7" rx="1.5" fill="#d0a040"/>
</g>
<g fill="none" stroke="#e8e4f0" stroke-linecap="round" opacity="0.5" stroke-width="6" filter="url(#blur8)">
<path d="M900 500 c-20 -40 20 -60 0 -110"/><path d="M970 505 c-20 -40 20 -70 0 -130"/><path d="M1040 500 c-20 -40 20 -60 0 -100"/></g>
{glow(960, 540, 120, "#ff6a40", 0.12)}
{fog(880, "#8a94b0", 0.12)}
'''
save("s8", svg(s8, SKY_NIGHT))

# ---------------------------------------------------------------- s9: POV inside the car, bar across lap, ground dropping
s9 = f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(200, 500, 0.8)}
<path d="M0 560 L1920 560 L1920 1080 L0 1080Z" fill="#0a0910"/>
<g opacity="0.8">{tent(700, 760, 200, 120, "#100e18", "#14121e")}{tent(1250, 740, 160, 100, "#100e18", "#14121e")}</g>
{bulbs(300, 700, 1600, 680, 40, 20, "#1e1a16")}
<rect x="1050" y="790" width="40" height="28" fill="#0c0b12"/>
<circle cx="1080" cy="796" r="4" fill="{RED}"/>
<line x1="380" y1="0" x2="380" y2="1080" stroke="#0a0a10" stroke-width="40"/>
<line x1="1540" y1="0" x2="1540" y2="1080" stroke="#0a0a10" stroke-width="40"/>
<path d="M300 0 L1620 0 L1580 70 L340 70Z" fill="#3a1418"/>
<path d="M300 820 L1620 820 L1620 1080 L300 1080Z" fill="#14121c"/>
<path d="M300 820 L1620 820 L1620 850 L300 850Z" fill="#3a1418"/>
<rect x="300" y="760" width="1320" height="34" rx="12" fill="#a8a8b4"/>
<rect x="300" y="760" width="1320" height="10" rx="5" fill="#d8d8e0" opacity="0.6"/>
<rect x="920" y="752" width="80" height="50" rx="8" fill="#c09030"/>
<g fill="{JACKET}"><path d="M540 1080 C560 900 640 820 700 800 L760 830 C700 870 660 960 650 1080Z"/>
<path d="M1380 1080 C1360 900 1280 820 1220 800 L1160 830 C1220 870 1260 960 1270 1080Z"/></g>
<g fill="#c89878"><ellipse cx="720" cy="780" rx="46" ry="30"/><ellipse cx="1200" cy="780" rx="46" ry="30"/></g>
{fog(700, "#8a94b0", 0.10)}
'''
save("s9", svg(s9, SKY_NIGHT))

# ---------------------------------------------------------------- s10: looking down: a boy in my jacket waving at the controls
s10 = f'''
<rect width="{W}" height="{H}" fill="#08070d"/>
<rect width="{W}" height="{H}" fill="url(#ground)"/>
<g stroke="#14121c" stroke-width="4">{''.join(f'<line x1="{x}" y1="0" x2="{x + 300}" y2="1080"/>' for x in range(-400, 2000, 160))}</g>
<g stroke="#0a0a12" stroke-width="34" stroke-linecap="round"><line x1="960" y1="-200" x2="640" y2="1200"/><line x1="960" y1="-200" x2="1280" y2="1200"/></g>
<rect x="800" y="400" width="260" height="170" fill="#16151e"/>
<rect x="800" y="400" width="260" height="20" fill="#2a2834"/>
<circle cx="890" cy="490" r="110" fill="url(#redglow)" opacity="0.6"/><circle cx="890" cy="490" r="10" fill="{RED}"/>
<ellipse cx="1000" cy="690" rx="100" ry="26" fill="#000" opacity="0.6"/>
<g transform="translate(1000 600) scale(1.7)">
<ellipse cx="0" cy="-10" rx="44" ry="40" fill="{JACKET}"/>
<path d="M-44 -10 Q0 30 44 -10" fill="#7a1a14"/>
<circle cx="0" cy="-20" r="26" fill="#0a0808"/>
<path d="M-26 -22 Q0 -54 26 -22Z" fill="#0a0808"/>
<path d="M36 -20 L90 -90" stroke="{JACKET}" stroke-width="22" stroke-linecap="round"/>
<circle cx="94" cy="-96" r="14" fill="#c9ccd6"/>
<g fill="#ffffff"><circle cx="-8" cy="-14" r="4"/><circle cx="8" cy="-14" r="4"/></g>
<path d="M-10 -2 Q0 6 10 -2" stroke="#ffffff" stroke-width="2.5" fill="none"/>
</g>
<path d="M1190 400 q24 -24 12 -48 M1214 424 q40 -36 20 -80" stroke="#c9ccd6" stroke-width="3" fill="none" opacity="0.5"/>
<polygon points="300,0 1620,0 1620,140 300,140" fill="#14121c"/>
<rect x="300" y="120" width="1320" height="26" rx="10" fill="#8a8a96"/>
{fog(560, "#8a94b0", 0.10, 200)}
'''
save("s10", svg(s10, '<radialGradient id="redglow"><stop offset="0" stop-color="#ff2a22"/><stop offset="1" stop-color="#ff2a22" stop-opacity="0"/></radialGradient><radialGradient id="ground" cx="960" cy="680" r="700" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#2a2232"/><stop offset="1" stop-color="#08070d"/></radialGradient>'))
