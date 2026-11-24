"""Scenes for Turn Left."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

RED = "#d0302c"
WARM = "#ffb54a"
GPS = "#4fd1c5"


def glow(cx, cy, r, color, op=0.6):
    """Soft glow that doesn't clip into a square on small radii."""
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" opacity="{op}" filter="url(#blur30)"/>'
            if r >= 120 else
            f'<circle cx="{cx}" cy="{cy}" r="{r * 2.2:.0f}" fill="url(#rg{abs(hash(color)) % 9999})" opacity="{op}"/>'
            f'<defs><radialGradient id="rg{abs(hash(color)) % 9999}"><stop offset="0" stop-color="{color}"/>'
            f'<stop offset="0.35" stop-color="{color}" stop-opacity="0.6"/><stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient></defs>')


def saguaro(x, base, h=260, color="#07080c"):
    w = h * 0.12
    return (f'<g fill="{color}" stroke="{color}" stroke-linecap="round">'
            f'<rect x="{x - w / 2:.0f}" y="{base - h:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{w / 2:.0f}"/>'
            f'<path d="M{x - w / 2:.0f} {base - h * .45:.0f} h{-w * 1.3:.0f} v{-h * .3:.0f}" fill="none" stroke-width="{w * .8:.0f}"/>'
            f'<path d="M{x + w / 2:.0f} {base - h * .6:.0f} h{w * 1.2:.0f} v{-h * .25:.0f}" fill="none" stroke-width="{w * .8:.0f}"/></g>')


def desert_sky(id_="dsky"):
    return sky(id_, "#05060d", "#141a2e", "#2c2a3a")


def mesas(y, color="#0c0d16"):
    return (f'<path d="M0 {y} L180 {y} L230 {y - 90} L520 {y - 95} L560 {y} L900 {y} L960 {y - 40} L1150 {y - 45} '
            f'L1200 {y} L1450 {y} L1500 {y - 130} L1760 {y - 135} L1800 {y} L1920 {y} L1920 1080 L0 1080Z" fill="{color}"/>')


def road(vx=960, vy=600, wl=300, wr=1620, color="#15161c", dash=True):
    out = [f'<polygon points="{vx - 6},{vy} {vx + 6},{vy} {wr},1080 {wl},1080" fill="{color}"/>']
    if dash:
        for i in range(9):
            t0 = (i / 9) ** 1.8; t1 = ((i + .45) / 9) ** 1.8
            y0 = vy + (1080 - vy) * t0; y1 = vy + (1080 - vy) * t1
            xm0 = vx + ((wl + wr) / 2 - vx) * t0; xm1 = vx + ((wl + wr) / 2 - vx) * t1
            out.append(f'<line x1="{xm0:.0f}" y1="{y0:.0f}" x2="{xm1:.0f}" y2="{y1:.0f}" stroke="#c9a640" '
                       f'stroke-width="{2 + 14 * t1:.1f}" opacity="0.7"/>')
    return "".join(out)


def car_rear(cx, base, s=1.0, lights=True):
    w = 300 * s; h = 150 * s
    out = [f'<g>',
           f'<path d="M{cx - w * .42:.0f} {base - h * .55:.0f} C{cx - w * .35:.0f} {base - h:.0f} {cx + w * .35:.0f} {base - h:.0f} {cx + w * .42:.0f} {base - h * .55:.0f} Z" fill="#0a0b10"/>',
           f'<path d="M{cx - w * .33:.0f} {base - h * .6:.0f} C{cx - w * .28:.0f} {base - h * .9:.0f} {cx + w * .28:.0f} {base - h * .9:.0f} {cx + w * .33:.0f} {base - h * .6:.0f} Z" fill="#1c2233"/>',
           f'<rect x="{cx - w / 2:.0f}" y="{base - h * .58:.0f}" width="{w:.0f}" height="{h * .45:.0f}" rx="{14 * s:.0f}" fill="#0d0e14"/>',
           f'<rect x="{cx - w * .45:.0f}" y="{base - h * .15:.0f}" width="{w * .14:.0f}" height="{h * .2:.0f}" fill="#050507"/>',
           f'<rect x="{cx + w * .31:.0f}" y="{base - h * .15:.0f}" width="{w * .14:.0f}" height="{h * .2:.0f}" fill="#050507"/>']
    if lights:
        for lx in (cx - w * .44, cx + w * .32):
            out.append(f'<rect x="{lx:.0f}" y="{base - h * .5:.0f}" width="{w * .12:.0f}" height="{h * .12:.0f}" fill="{RED}"/>')
            out.append(glow(lx + w * .06, base - h * .44, 40 * s, RED, 0.55))
    out.append('</g>')
    return "".join(out)


# ------------------------------------------------------------------ s1 rental counter
keys = ""
for i in range(5):
    for j in range(2):
        x = 1130 + i * 46; y = 300 + j * 90
        tag = RED if (i, j) == (2, 1) else "#8a8f7a"
        keys += (f'<circle cx="{x}" cy="{y}" r="5" fill="#555"/><line x1="{x}" y1="{y}" x2="{x}" y2="{y + 30}" stroke="#9a9aa0" stroke-width="3"/>'
                 f'<rect x="{x - 9}" y="{y + 30}" width="18" height="26" rx="3" fill="{tag}" opacity="{0.25 if (i, j) == (2, 1) else 0.9}"/>')
s1 = svg(f'''
<rect width="{W}" height="{H}" fill="#121619"/>
<rect x="0" y="0" width="{W}" height="120" fill="#0c0f11"/>
<rect x="700" y="60" width="520" height="26" rx="6" fill="#e9f3e8"/>
<rect x="700" y="60" width="520" height="26" fill="#d9f5e0" opacity="0.6" filter="url(#blur30)"/>
<polygon points="700,86 1220,86 1500,700 420,700" fill="#d9f5e0" opacity="0.05"/>
<rect x="500" y="200" width="380" height="330" fill="#0a0d1c"/>
<rect x="500" y="200" width="380" height="330" fill="url(#winsky)"/>
{''.join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="#dfe3f5" opacity="0.7"/>' for x, y in [(540,230),(610,260),(700,220),(780,250),(850,235),(660,300),(820,300)])}
<path d="M500 470 L560 470 L580 430 L700 428 L720 470 L880 470 L880 530 L500 530Z" fill="#05060b"/>
{saguaro(800, 520, 90)}
<rect x="500" y="200" width="380" height="330" fill="none" stroke="#06080a" stroke-width="14"/>
<line x1="690" y1="200" x2="690" y2="530" stroke="#06080a" stroke-width="10"/>
<rect x="1100" y="270" width="270" height="230" rx="6" fill="#2a2620"/>
{keys}
<text x="1235" y="250" text-anchor="middle" font-family="{SANS}" font-size="22" fill="#8a8170" letter-spacing="4">KEYS</text>
<g fill="#050608">
<ellipse cx="960" cy="345" rx="52" ry="64"/>
<path d="M920 300 C930 260 1000 260 1010 300 L1030 305 L900 305Z"/>
<path d="M840 700 C840 520 880 420 960 420 C1040 420 1080 520 1080 700Z"/>
</g>
<rect x="0" y="690" width="{W}" height="40" fill="#3a2c22"/>
<rect x="0" y="730" width="{W}" height="350" fill="#1d1612"/>
<g stroke="#120d0a" stroke-width="3">{''.join(f'<line x1="{x}" y1="730" x2="{x}" y2="1080"/>' for x in range(80, 1920, 160))}</g>
<path d="M1010 690 C1040 640 1090 640 1110 672 L1150 690 Z" fill="#050608"/>
<g transform="translate(1000 708) rotate(-12)">
<rect x="-20" y="-12" width="70" height="24" rx="8" fill="#22242a"/>
<line x1="50" y1="0" x2="100" y2="0" stroke="#b8b8c0" stroke-width="7" stroke-linecap="round"/>
<path d="M78 0 v10 M90 0 v8" stroke="#b8b8c0" stroke-width="5"/>
<circle cx="-30" cy="0" r="10" fill="none" stroke="#9a9aa0" stroke-width="4"/>
<rect x="-72" y="-14" width="34" height="46" rx="4" fill="{RED}"/>
</g>
{glow(990, 712, 70, RED, 0.18)}
''', '<linearGradient id="winsky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#060814"/><stop offset="1" stop-color="#2a2840"/></linearGradient>')
save("s1", s1)

# ------------------------------------------------------------------ s2 empty desert highway
s2 = svg(f'''
<rect width="{W}" height="{H}" fill="url(#dsky)"/>
{stars(220, 560, 0.85)}
{moon(1250, 200, 46)}
{mesas(610)}
<rect x="0" y="600" width="{W}" height="480" fill="#17141c"/>
{road(960, 600)}
{fog(620, "#8a8fb0", 0.12, 60)}
{saguaro(640, 760, 260)}
{saguaro(1330, 700, 170)}
{saguaro(450, 900, 380)}
<polygon points="930,850 990,850 1050,620 870,620" fill="#f3e6b0" opacity="0.08" filter="url(#blur8)"/>
{car_rear(960, 900, 0.75)}
''', desert_sky())
save("s2", s2)

# ------------------------------------------------------------------ dashboard helpers
def windshield(extra=""):
    return f'''
<rect width="{W}" height="{H}" fill="url(#dsky)"/>
{stars(140, 420, 0.8)}
{mesas(520, "#0a0b13")}
<rect x="0" y="515" width="{W}" height="565" fill="#120f15"/>
<polygon points="955,515 965,515 1500,1080 420,1080" fill="#1a1a20"/>
<polygon points="955,515 965,515 1350,900 570,900" fill="#f3e6b0" opacity="0.10" filter="url(#blur30)"/>
{extra}
<path d="M0 0 L1920 0 L1920 120 C1400 70 520 70 0 120Z" fill="#06070a"/>
<path d="M0 1080 L0 700 C500 650 1420 650 1920 700 L1920 1080Z" fill="#0b0c11"/>
<path d="M0 700 C500 650 1420 650 1920 700" stroke="#1c1e26" stroke-width="6" fill="none"/>
'''

def wheel(cx=690, cy=980):
    return (f'<circle cx="{cx}" cy="{cy}" r="250" fill="none" stroke="#050507" stroke-width="44"/>'
            f'<path d="M{cx - 230} {cy} L{cx + 230} {cy}" stroke="#050507" stroke-width="40"/>'
            f'<circle cx="{cx}" cy="{cy}" r="70" fill="#050507"/>')

def gps(cx, cy, w, h, body, glowc=GPS, on=True):
    out = f'<rect x="{cx - w / 2 - 16}" y="{cy - h / 2 - 16}" width="{w + 32}" height="{h + 32}" rx="18" fill="#040405"/>'
    if on:
        out += glow(cx, cy, w * .55, glowc, 0.22)
        out += f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="8" fill="#0b1a1f"/>' + body
    else:
        out += f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="8" fill="#08090b"/>' + body
    return out

def left_arrow(cx, cy, s, color):
    return (f'<path d="M{cx + 40 * s} {cy + 60 * s} L{cx + 40 * s} {cy - 10 * s} L{cx - 20 * s} {cy - 10 * s} L{cx - 20 * s} {cy - 40 * s} '
            f'L{cx - 70 * s} {cy} L{cx - 20 * s} {cy + 40 * s} L{cx - 20 * s} {cy + 10 * s} L{cx + 15 * s} {cy + 10 * s} L{cx + 15 * s} {cy + 60 * s}Z" fill="{color}"/>')

# ------------------------------------------------------------------ s3 GPS flickers: turn left
map3 = (f'<g clip-path="url(#scr3)"><path d="M1130 940 L1130 800 L980 800" stroke="{GPS}" stroke-width="14" fill="none" opacity="0.85"/>'
        f'<path d="M1130 940 L1130 700" stroke="#1e3a40" stroke-width="10"/>'
        f'{left_arrow(1035, 735, 0.9, "#e9fffb")}'
        f'<circle cx="1130" cy="900" r="12" fill="#e9fffb"/>'
        f'<line x1="1010" y1="860" x2="1250" y2="760" stroke="#e9fffb" stroke-width="2" opacity="0.25"/></g>')
s3 = svg(windshield() + wheel() + gps(1110, 820, 280, 220, map3) + glow(1110, 820, 220, GPS, 0.08),
         desert_sky() + '<clipPath id="scr3"><rect x="970" y="710" width="280" height="220" rx="8"/></clipPath>')
save("s3", s3)

# ------------------------------------------------------------------ s4 nothing out there but one porch light
s4 = svg(f'''
<rect width="{W}" height="{H}" fill="url(#dsky)"/>
{stars(260, 600, 0.9)}
{mesas(640)}
<rect x="0" y="630" width="{W}" height="450" fill="#15121a"/>
<path d="M0 760 C300 730 600 745 900 735 C1300 720 1600 750 1920 740 L1920 1080 L0 1080Z" fill="#1b1720"/>
{road(1300, 630, 950, 2300)}
{glow(700, 668, 60, WARM, 0.75)}
<circle cx="700" cy="668" r="5" fill="#ffe6b0"/>
<path d="M660 690 L660 660 L690 640 L725 660 L725 690Z" fill="#06060a"/>
<rect x="696" y="672" width="8" height="18" fill="{WARM}" opacity="0.6"/>
<path d="M1120 900 C980 860 860 800 720 700" stroke="#2a2430" stroke-width="3" stroke-dasharray="12 14" fill="none" opacity="0.6"/>
{saguaro(560, 820, 200)}
{saguaro(880, 700, 70)}
{fog(700, "#8a8fb0", 0.12, 70)}
<polygon points="1190,940 1270,940 1330,660 1160,660" fill="#f3e6b0" opacity="0.07" filter="url(#blur8)"/>
{car_rear(1230, 990, 0.85)}
''', desert_sky())
save("s4", s4)

# ------------------------------------------------------------------ s5 GPS says my name (close-up)
bars = "".join(f'<rect x="{830 + i * 26}" y="{640 - h / 2}" width="14" height="{h}" rx="7" fill="#ff6a5a"/>'
               for i, h in enumerate([20, 40, 80, 130, 90, 160, 110, 60, 140, 70, 30, 50, 20]))
map5 = (f'<g clip-path="url(#scr5)">'
        f'<rect x="700" y="420" width="520" height="400" fill="#1a0b0d"/>'
        f'<path d="M960 820 L960 720 C960 680 900 680 760 680" stroke="#7a2a2a" stroke-width="16" fill="none" opacity="0.7"/>'
        f'{bars}'
        f'<circle cx="960" cy="780" r="14" fill="#ffd8d0"/></g>')
s5 = svg(f'''
<rect width="{W}" height="{H}" fill="#050507"/>
{windshield()}
<rect width="{W}" height="{H}" fill="#000" opacity="0.45"/>
<rect x="560" y="330" width="800" height="600" rx="40" fill="#030304"/>
{gps(960, 620, 520, 400, map5, "#ff5a4a")}
{glow(960, 620, 380, RED, 0.12)}
<path d="M1220 900 C1260 980 1240 1040 1300 1080" stroke="#030304" stroke-width="22" fill="none"/>
<path d="M1500 1080 C1460 980 1400 940 1330 930 C1300 925 1290 940 1310 955 L1380 990" fill="#060608"/>
''', desert_sky() + '<clipPath id="scr5"><rect x="700" y="420" width="520" height="400" rx="8"/></clipPath>')
save("s5", s5)

# ------------------------------------------------------------------ s5b screen dead, cord ripped out
s5b = svg(f'''
<rect width="{W}" height="{H}" fill="#050507"/>
{windshield()}
<rect width="{W}" height="{H}" fill="#000" opacity="0.6"/>
<rect x="560" y="330" width="800" height="600" rx="40" fill="#030304"/>
{gps(960, 620, 520, 400, '<path d="M720 440 L860 600" stroke="#1a1c22" stroke-width="3" opacity="0.5"/>', on=False)}
<path d="M1220 900 C1300 960 1280 1020 1230 1050 C1180 1075 1150 1040 1180 1010" stroke="#0a0a0d" stroke-width="16" fill="none"/>
<rect x="1162" y="990" width="40" height="26" rx="4" fill="#3a3a40" transform="rotate(30 1182 1003)"/>
<line x1="1190" y1="990" x2="1200" y2="975" stroke="#8a8a90" stroke-width="4"/>
<line x1="1178" y1="985" x2="1186" y2="970" stroke="#8a8a90" stroke-width="4"/>
''', desert_sky())
save("s5b", s5b)

# ------------------------------------------------------------------ s6 headlights in the rearview mirror
s6 = svg(f'''
<rect width="{W}" height="{H}" fill="url(#dsky)"/>
{stars(160, 480, 0.6)}
{mesas(560, "#090a12")}
<rect x="0" y="555" width="{W}" height="525" fill="#0f0c12"/>
<polygon points="955,555 965,555 1500,1080 420,1080" fill="#16161c"/>
<rect width="{W}" height="{H}" fill="#000" opacity="0.35"/>
<path d="M0 0 L1920 0 L1920 140 C1400 90 520 90 0 140Z" fill="#06070a"/>
<rect x="948" y="110" width="24" height="110" fill="#050507"/>
<rect x="600" y="200" width="720" height="230" rx="60" fill="#050507"/>
<rect x="625" y="222" width="670" height="186" rx="44" fill="url(#mir)"/>
<g clip-path="url(#mclip)">
<path d="M625 330 L760 330 L790 300 L1000 296 L1030 330 L1295 330 L1295 408 L625 408Z" fill="#0a0b12"/>
<polygon points="955,330 965,330 1150,408 770,408" fill="#1a1a22"/>
{''.join(f'<circle cx="{x}" cy="{y}" r="1.5" fill="#dfe3f5" opacity="0.6"/>' for x, y in [(680,250),(760,270),(880,240),(1050,260),(1180,245),(1240,280)])}
{glow(946, 333, 26, "#fff4d0", 0.9)}{glow(974, 333, 26, "#fff4d0", 0.9)}
<circle cx="946" cy="333" r="5" fill="#ffffff"/><circle cx="974" cy="333" r="5" fill="#ffffff"/>
</g>
<rect x="625" y="222" width="670" height="186" rx="44" fill="none" stroke="#1c1e26" stroke-width="4"/>
<path d="M0 1080 L0 820 C500 770 1420 770 1920 820 L1920 1080Z" fill="#0b0c11"/>
''', desert_sky() + '<linearGradient id="mir" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#090b16"/><stop offset="1" stop-color="#222436"/></linearGradient>'
   + '<clipPath id="mclip"><rect x="625" y="222" width="670" height="186" rx="44"/></clipPath>')
save("s6", s6)

# ------------------------------------------------------------------ s7 home at dawn
s7 = svg(f'''
<rect width="{W}" height="{H}" fill="url(#dawn)"/>
{stars(60, 260, 0.4)}
<path d="M0 760 C300 740 700 750 1000 745 C1400 740 1700 755 1920 750 L1920 1080 L0 1080Z" fill="#0f1018"/>
{dead_tree(1420, 780, 420, "#08090f")}
<g fill="#0a0b12">
<rect x="620" y="480" width="560" height="300"/>
<polygon points="580,490 900,300 1220,490"/>
<rect x="1060" y="340" width="50" height="110"/>
</g>
{lit_window(700, 560, 110, 120, "#3a3020")}
<rect x="900" y="620" width="90" height="160" fill="#050508"/>
{glow(1010, 600, 30, WARM, 0.7)}<circle cx="1010" cy="600" r="6" fill="#ffe0a0"/>
{lit_window(1040, 560, 100, 110, "#1c1a1c")}
<polygon points="860,780 1020,780 1200,1080 640,1080" fill="#1b1c22"/>
<g transform="translate(940 930)">
<path d="M-180 0 C-170 -60 -120 -110 -40 -115 L60 -115 C120 -110 160 -70 180 0 Z" fill="#07080c"/>
<rect x="-200" y="-20" width="400" height="70" rx="14" fill="#0b0c12"/>
<rect x="-185" y="0" width="60" height="18" fill="#2a0a0a"/><rect x="125" y="0" width="60" height="18" fill="#2a0a0a"/>
</g>
{fog(780, "#c9a6a0", 0.08, 70)}
''', '<linearGradient id="dawn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a0c18"/><stop offset="0.6" stop-color="#2a2a44"/><stop offset="1" stop-color="#8a5a4a"/></linearGradient>')
save("s7", s7)

# ------------------------------------------------------------------ s8 kitchen table, phone lights up
def kitchen(outside=""):
    return f'''
<rect width="{W}" height="{H}" fill="#0d0d12"/>
<rect x="0" y="0" width="{W}" height="640" fill="url(#kwall)"/>
<rect x="640" y="140" width="640" height="400" fill="#0b0e1c"/>
<rect x="640" y="140" width="640" height="400" fill="url(#kwin)"/>
{outside}
<g fill="#16151a">{''.join(f'<rect x="640" y="{y}" width="640" height="14"/>' for y in range(150, 330, 30))}</g>
<rect x="640" y="140" width="640" height="400" fill="none" stroke="#050507" stroke-width="18"/>
<line x1="960" y1="330" x2="960" y2="540" stroke="#050507" stroke-width="12"/>
<line x1="1250" y1="330" x2="1250" y2="460" stroke="#2a2a30" stroke-width="2"/>
<rect x="0" y="560" width="{W}" height="80" fill="#141318"/>
<rect x="200" y="560" width="220" height="80" fill="#0e0d12"/>
<path d="M0 760 L1920 760 L1920 1080 L0 1080Z" fill="#1a1410"/>
<path d="M200 700 L1720 700 L1820 820 L100 820Z" fill="#2a1e16"/>
<path d="M100 820 L1820 820 L1820 850 L100 850Z" fill="#120c08"/>
<rect x="240" y="850" width="40" height="230" fill="#0e0906"/><rect x="1640" y="850" width="40" height="230" fill="#0e0906"/>
<g transform="translate(1250 700)"><path d="M-40 0 L-30 -90 L30 -90 L40 0Z" fill="#141016"/><ellipse cx="0" cy="-90" rx="30" ry="8" fill="#1d1820"/></g>
<rect x="560" y="690" width="120" height="16" rx="4" fill="#3a2e26"/>
'''

def phone_on(textop=1.0):
    return f'''
{glow(960, 760, 220, GPS, 0.20)}
<polygon points="860,770 1060,770 1300,560 620,560" fill="{GPS}" opacity="0.05" filter="url(#blur30)"/>
<g transform="translate(960 760) scale(1 0.42) rotate(0)">
<rect x="-170" y="-200" width="340" height="400" rx="30" fill="#050507"/>
<rect x="-154" y="-184" width="308" height="368" rx="18" fill="#0b1a1f"/>
<path d="M0 50 L0 20 C0 -20 -40 -40 -60 -80" stroke="{GPS}" stroke-width="12" fill="none"/>
<path d="M-60 -150 C-90 -150 -100 -120 -100 -100 C-100 -70 -60 -40 -60 -40 C-60 -40 -20 -70 -20 -100 C-20 -120 -30 -150 -60 -150Z" fill="{RED}"/>
<circle cx="-60" cy="-102" r="14" fill="#0b1a1f"/>
</g>
<text x="960" y="800" text-anchor="middle" font-family="{SANS}" font-size="19" font-weight="700" fill="#e9fffb" opacity="{textop}" letter-spacing="1">YOU HAVE ARRIVED</text>
'''

kdefs = ('<linearGradient id="kwall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a0a10"/><stop offset="1" stop-color="#1c1a22"/></linearGradient>'
         '<linearGradient id="kwin" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a1e34"/><stop offset="1" stop-color="#4a3a44"/></linearGradient>')
s8 = svg(kitchen() + phone_on(), kdefs)
save("s8", s8)

outside = (f'<path d="M640 470 L1280 470 L1280 540 L640 540Z" fill="#100f16"/>'
           f'{glow(860, 470, 60, "#fff4d0", 0.85)}{glow(1060, 470, 60, "#fff4d0", 0.85)}'
           f'<circle cx="860" cy="470" r="16" fill="#ffffff"/><circle cx="1060" cy="470" r="16" fill="#ffffff"/>'
           f'<polygon points="640,330 1280,330 1280,540 640,540" fill="#fff4d0" opacity="0.10"/>')
s8b = svg(kitchen(outside) + phone_on() + '<polygon points="660,540 1260,540 1500,760 420,760" fill="#fff4d0" opacity="0.07" filter="url(#blur30)"/>', kdefs)
save("s8b", s8b)
