"""Scenes for 'The Last Order' — a night food-delivery driver, a forbidden address, a house full of still people."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

r = random.Random(18)


def pines(y, n, color, hmin=60, hmax=150, x0=0, x1=W):
    out = []
    for _ in range(n):
        x = r.randint(x0, x1); h = r.randint(hmin, hmax); w = h * 0.32
        out.append(f'<polygon points="{x},{y - h} {x - w:.0f},{y} {x + w:.0f},{y}" fill="{color}"/>'
                   f'<polygon points="{x},{y - h * 1.15:.0f} {x - w * .7:.0f},{y - h * .45:.0f} {x + w * .7:.0f},{y - h * .45:.0f}" fill="{color}"/>')
    return "".join(out)


def phone(cx, cy, screen, w=420, h=800, glowc="#8fb6ff"):
    """A phone held upright, centred at (cx, cy). `screen` is markup drawn in local coords (0,0)-(w-40,h-80)."""
    x, y = cx - w / 2, cy - h / 2
    sw, sh = w - 40, h - 80
    return (f'{glow(cx, cy, w * .9, glowc, 0.18)}'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="54" fill="#0a0a0f" stroke="#2a2a33" stroke-width="5"/>'
            f'<g transform="translate({x + 20} {y + 40})"><clipPath id="scr{cx}{cy}"><rect width="{sw}" height="{sh}" rx="30"/></clipPath>'
            f'<g clip-path="url(#scr{cx}{cy})">{screen}</g></g>'
            f'<rect x="{cx - 50}" y="{y + 14}" width="100" height="14" rx="7" fill="#1c1c24"/>')


def hand(cx, cy, side=1, color="#050407", h=820, w=420):
    """A dark hand cupping the bottom of a phone: palm below, thumb and fingers only over the frame edges."""
    b = cy + h / 2; L = cx - w / 2; R = cx + w / 2
    return (f'<path d="M{cx - 300} 1080 C{cx - 280} {b + 40} {L - 30} {b - 120} {L - 10} {b - 160} '
            f'C{L + 6} {b - 180} {L + 22} {b - 150} {L + 22} {b - 110} L{L + 30} {b - 30} '
            f'C{cx - 100} {b - 10} {cx + 100} {b - 10} {R - 30} {b - 30} '
            f'L{R - 18} {b - 90} C{R - 14} {b - 120} {R + 20} {b - 120} {R + 24} {b - 80} '
            f'C{R + 40} {b - 20} {cx + 300} {b + 60} {cx + 300} 1080Z" fill="{color}"/>'
            f'<path d="M{R - 6} {b - 230} C{R + 20} {b - 232} {R + 30} {b - 200} {R + 10} {b - 180}" stroke="{color}" stroke-width="26" stroke-linecap="round" fill="none"/>'
            f'<path d="M{R - 6} {b - 160} C{R + 20} {b - 162} {R + 30} {b - 130} {R + 10} {b - 110}" stroke="{color}" stroke-width="26" stroke-linecap="round" fill="none"/>')


def map_screen(sw=380, sh=720, pin=True):
    roads = (f'<rect width="{sw}" height="{sh}" fill="#0f1726"/>'
             + "".join(f'<path d="M{-20} {y} C{sw * .3} {y + 30} {sw * .6} {y - 40} {sw + 20} {y + 10}" stroke="#22324d" stroke-width="10" fill="none"/>' for y in (120, 300, 470, 640))
             + "".join(f'<path d="M{x} -20 L{x + 30} {sh + 20}" stroke="#22324d" stroke-width="8"/>' for x in (60, 170, 300))
             + f'<path d="M190 690 C200 560 120 480 160 380 C200 280 300 260 290 170" stroke="#4f8cff" stroke-width="12" fill="none" stroke-linecap="round"/>')
    if pin:
        roads += (f'<path d="M290 170 C290 120 250 100 250 70 A40 40 0 1 1 330 70 C330 100 290 120 290 170Z" fill="#e0262a"/>'
                  f'<circle cx="290" cy="68" r="14" fill="#2a0508"/>{glow(290, 90, 60, "#ff3030", 0.35)}')
    return roads


def figure_row(xs, base, hs, color="#030203"):
    return "".join(figure(x, base, h, color) for x, h in zip(xs, hs))


# S1 — a lonely small-town main street at night, my little car with the phone glowing on the dash
shops = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{900 - y}" fill="#0b0b14"/>' for x, y, w in
                ((180, 420, 200), (380, 380, 170), (550, 450, 160), (1240, 400, 190), (1430, 360, 180), (1610, 440, 200)))
s1 = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk1)"/>
{stars(120, 420, 0.6)}
{moon(1250, 200, 60)}
{shops}
<g fill="#16131f">{''.join(f'<rect x="{x}" y="{y}" width="40" height="50"/>' for x, y in ((220, 480), (300, 480), (420, 440), (600, 520), (1280, 470), (1350, 470), (1480, 430), (1660, 500)))}</g>
{lit_window(1480, 520, 56, 70, "#ff9a3a")}
<path d="M0 900 L1920 900 L1920 1080 L0 1080Z" fill="#0d0c14"/>
<path d="M0 880 L1920 880 L1920 900 L0 900Z" fill="#1a1824"/>
<g stroke="#3a3540" stroke-width="6" stroke-dasharray="50 50"><line x1="0" y1="1000" x2="1920" y2="1000"/></g>
<rect x="760" y="400" width="12" height="490" fill="#0a0a10"/>
<path d="M766 404 C800 380 860 380 880 400" stroke="#0a0a10" stroke-width="10" fill="none"/>
<polygon points="860,410 900,410 980,900 780,900" fill="#ffc46b" opacity="0.07"/>
{glow(880, 410, 60, "#ffc46b", 0.5)}
<g transform="translate(960 0)">
<path d="M-300 960 L-290 860 C-280 830 -250 820 -220 818 L-150 740 C-130 720 -100 712 -60 712 L120 712 C160 712 190 724 210 744 L280 818 C300 822 320 836 324 860 L330 960Z" fill="#14121c"/>
<path d="M-140 810 L-80 740 L40 740 L40 810Z" fill="#202a40"/>
<path d="M60 810 L60 740 L120 740 C140 740 160 748 176 762 L216 810Z" fill="#202a40"/>
<rect x="-2" y="776" width="22" height="30" rx="4" fill="#dfe8ff"/>
{glow(9, 790, 40, "#cfe0ff", 0.45)}
<ellipse cx="-40" cy="770" rx="22" ry="26" fill="#07060a"/><path d="M-70 810 C-70 790 -60 784 -40 784 C-20 784 -10 790 -10 810Z" fill="#07060a"/>
<circle cx="-180" cy="960" r="52" fill="#050407"/><circle cx="-180" cy="960" r="22" fill="#24222c"/>
<circle cx="210" cy="960" r="52" fill="#050407"/><circle cx="210" cy="960" r="22" fill="#24222c"/>
<rect x="300" y="860" width="30" height="18" rx="4" fill="#ff2a2a"/>
{glow(315, 870, 40, "#ff2a2a", 0.6)}
<rect x="-310" y="866" width="26" height="16" rx="4" fill="#ffe9b0"/>
<polygon points="-300,866 -700,830 -700,940 -300,882" fill="#ffe9b0" opacity="0.12"/>
</g>
{fog(900, "#8a8fb0", 0.12, 90)}
''', sky("sk1", "#04050c", "#141530", "#2c2140"))
save("s1", s1)

# S2 — the warning: phone in a hand, map with a red pin far outside town
s2 = svg(f'''
<rect width="{W}" height="{H}" fill="#06060a"/>
{glow(960, 500, 420, "#1d2a55", 0.35)}
<rect x="300" y="620" width="1320" height="460" fill="#0b0a10"/>
<circle cx="1500" cy="560" r="70" fill="#ff7a2a" opacity="0.08" filter="url(#blur60)"/>
{phone(960, 470, map_screen() + f'<rect x="20" y="560" width="340" height="130" rx="20" fill="#0a0f1a" opacity="0.92"/>'
      f'<text x="190" y="616" text-anchor="middle" font-family="{SANS}" font-size="40" font-weight="bold" fill="#f2f2f2">14 LARKIN RD</text>'
      f'<text x="190" y="664" text-anchor="middle" font-family="{SANS}" font-size="28" fill="#ff5a5a">after midnight</text>', 420, 820)}
{hand(960, 470)}
''')
save("s2", s2)

# S3 — 2:40 a.m., new order, the cancel button gone gray
order = (f'<rect width="380" height="740" fill="#0d1220"/>'
         f'<text x="190" y="110" text-anchor="middle" font-family="{SANS}" font-size="74" font-weight="bold" fill="#e9eef7">2:40</text>'
         f'<rect x="20" y="170" width="340" height="250" rx="24" fill="#18213a"/>'
         f'<text x="190" y="235" text-anchor="middle" font-family="{SANS}" font-size="34" fill="#9fb3d9">NEW ORDER</text>'
         f'<text x="190" y="300" text-anchor="middle" font-family="{SANS}" font-size="42" font-weight="bold" fill="#ffffff">14 LARKIN RD</text>'
         f'<text x="190" y="360" text-anchor="middle" font-family="{SANS}" font-size="28" fill="#ff6060">1 bag  ·  leave at door</text>'
         f'<rect x="40" y="480" width="300" height="90" rx="45" fill="#3a3d46"/>'
         f'<text x="190" y="538" text-anchor="middle" font-family="{SANS}" font-size="36" fill="#6b6f7a">CANCEL</text>'
         f'<rect x="40" y="600" width="300" height="90" rx="45" fill="#2fbf6a"/>'
         f'<text x="190" y="658" text-anchor="middle" font-family="{SANS}" font-size="36" font-weight="bold" fill="#06210f">ACCEPT</text>')
s3 = svg(f'''
<rect width="{W}" height="{H}" fill="#05050a"/>
<path d="M0 0 L1920 0 L1920 520 L0 520Z" fill="#0b0e1a"/>
{stars(40, 300, 0.4)}
<path d="M0 560 C600 520 1300 520 1920 560 L1920 1080 L0 1080Z" fill="#09080d"/>
<ellipse cx="960" cy="1050" rx="700" ry="200" fill="none" stroke="#040306" stroke-width="60"/>
{phone(960, 500, order, 420, 820, "#6f9cff")}
<path d="M760 1080 C790 960 830 880 860 860 C880 850 900 860 905 880 L920 960 L1000 960 L1010 880 C1015 860 1040 850 1060 860 C1090 880 1130 960 1160 1080Z" fill="#050407"/>
''')
save("s3", s3)

# S4 — the lone house at the end of a dirt road; one porch light, every window dark; my headlights
s4 = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk4)"/>
{stars(160, 520, 0.7)}
{moon(1240, 170, 50, "#e4dcc6")}
{pines(640, 40, "#07080e", 80, 200, 0, 640)}{pines(640, 40, "#07080e", 80, 200, 1280, 1920)}
{dead_tree(1300, 660, 360)}
<path d="M0 640 C500 610 1400 610 1920 640 L1920 1080 L0 1080Z" fill="#100e17"/>
<g fill="#07060b">
<polygon points="700,650 700,430 960,300 1220,430 1220,650"/>
<rect x="1110" y="300" width="40" height="110"/>
<polygon points="680,650 680,540 1240,540 1240,650"/>
<polygon points="660,550 960,500 1260,550"/>
{''.join(f'<rect x="{x}" y="550" width="12" height="100"/>' for x in (700, 820, 1100, 1210))}
</g>
<g fill="#13121c">{''.join(f'<rect x="{x}" y="{y}" width="70" height="80"/>' for x, y in ((760, 410), (1090, 410), (880, 580), (1060, 580)))}</g>
<rect x="935" y="570" width="50" height="80" fill="#1a1520"/>
<circle cx="1000" cy="560" r="9" fill="#ffd27a"/>
{glow(1000, 570, 90, "#ffc060", 0.55)}
<polygon points="930,650 1050,650 1110,700 880,700" fill="#ffc060" opacity="0.10" filter="url(#blur8)"/>
<path d="M880 660 C860 760 760 880 560 1080 L1360 1080 C1160 880 1060 760 1040 660Z" fill="#2a2420"/>
<path d="M960 660 C950 760 900 900 840 1080" stroke="#1b1714" stroke-width="10" fill="none"/>
<polygon points="600,1080 930,700 990,700 1320,1080" fill="#fff1c4" opacity="0.09" filter="url(#blur30)"/>
{grass(1080, 160, "#09080e", (20, 50))}
{fog(700, "#9aa0c0", 0.12, 80)}
''', sky("sk4", "#03040a", "#121428", "#262036"))
save("s4", s4)

# S5 — on the porch step: the paper bag, the dark front window right beside it
s5 = svg(f'''
<rect width="{W}" height="{H}" fill="#0a0910"/>
<rect x="400" y="0" width="1120" height="820" fill="#16131b"/>
{''.join(f'<line x1="400" y1="{y}" x2="1520" y2="{y}" stroke="#0e0c12" stroke-width="4"/>' for y in range(40, 820, 60))}
<rect x="560" y="160" width="420" height="440" fill="#0c0d14" stroke="#24202a" stroke-width="18"/>
<rect x="560" y="160" width="420" height="440" fill="#3a4466" opacity="0.10"/>
<line x1="770" y1="160" x2="770" y2="600" stroke="#24202a" stroke-width="10"/>
<line x1="560" y1="380" x2="980" y2="380" stroke="#24202a" stroke-width="10"/>
<path d="M590 190 L700 190 L590 300Z" fill="#aab4d8" opacity="0.06"/>
<rect x="1100" y="140" width="300" height="680" fill="#1e1820"/>
<rect x="1130" y="170" width="240" height="280" fill="none" stroke="#120f16" stroke-width="6"/>
<rect x="1130" y="480" width="240" height="300" fill="none" stroke="#120f16" stroke-width="6"/>
<circle cx="1140" cy="480" r="10" fill="#a7853f"/>
<circle cx="1470" cy="120" r="12" fill="#ffd27a"/>{glow(1470, 140, 160, "#ffc060", 0.4)}
<polygon points="1470,130 1900,1080 600,1080" fill="#ffc060" opacity="0.06"/>
<rect x="300" y="820" width="1320" height="40" fill="#221d24"/>
<rect x="260" y="860" width="1400" height="220" fill="#17141b"/>
<rect x="260" y="940" width="1400" height="12" fill="#0d0b10"/>
<g transform="translate(860 700)">
<path d="M0 0 L200 0 L210 160 L-10 160Z" fill="#8a6a44"/>
<path d="M0 0 L20 -20 L40 0 L60 -20 L80 0 L100 -20 L120 0 L140 -20 L160 0 L180 -20 L200 0Z" fill="#7a5c3a"/>
<path d="M0 0 L-10 160" stroke="#5e4630" stroke-width="4"/>
<rect x="60" y="50" width="80" height="50" rx="6" fill="#c22a2e"/>
</g>
{glow(960, 780, 140, "#ffc060", 0.12)}
''')
save("s5", s5)

# S6 — the look: through the window, a living room full of still people all facing the door
s6 = svg(f'''
<rect width="{W}" height="{H}" fill="#07060a"/>
<rect x="420" y="80" width="1080" height="880" fill="url(#room6)"/>
<rect x="1320" y="300" width="140" height="560" fill="#1a1418"/>
<circle cx="1340" cy="590" r="8" fill="#a7853f"/>
<rect x="1310" y="290" width="160" height="10" fill="#0c0a0e"/>
{glow(1390, 580, 200, "#6a7aa8", 0.12)}
{figure_row((520, 640, 760, 880, 1000, 1120, 1230), 900, (430, 470, 410, 480, 440, 460, 420), "#030203")}
{figure_row((580, 820, 940, 1060, 1180), 960, (480, 500, 470, 520, 490), "#000000")}
<rect x="420" y="80" width="1080" height="880" fill="#2a3456" opacity="0.08"/>
<rect x="400" y="60" width="1120" height="920" fill="none" stroke="#1a161e" stroke-width="40"/>
<line x1="960" y1="60" x2="960" y2="980" stroke="#1a161e" stroke-width="22"/>
<line x1="400" y1="520" x2="1520" y2="520" stroke="#1a161e" stroke-width="22"/>
<path d="M440 100 L620 100 L440 300Z" fill="#c8d0f0" opacity="0.05"/>
<path d="M0 0 L400 0 L400 1080 L0 1080Z M1520 0 L1920 0 L1920 1080 L1520 1080Z" fill="#100d13"/>
<rect x="0" y="980" width="1920" height="100" fill="#100d13"/>
''', '<linearGradient id="room6" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0d0e16"/><stop offset="1" stop-color="#1e2236"/></linearGradient>')
save("s6", s6)

# S7 — driving home on the empty highway, radio off, house shrinking in the mirror
s7 = svg(f'''
<rect width="{W}" height="{H}" fill="#06060a"/>
<path d="M260 120 C700 80 1220 80 1660 120 L1740 600 L180 600Z" fill="url(#ws7)"/>
{stars(70, 380, 0.45)}
{pines(600, 50, "#05070c", 60, 170, 180, 800)}{pines(600, 50, "#05070c", 60, 170, 1120, 1740)}
<path d="M560 600 L930 420 L990 420 L1360 600Z" fill="#17171d"/>
<polygon points="620,600 960,430 1300,600" fill="#f4e7c2" opacity="0.13" filter="url(#blur30)"/>
<g stroke="#cfc8a8" stroke-width="5" opacity="0.6">{''.join(f'<line x1="960" y1="{y}" x2="960" y2="{y + 14}"/>' for y in (450, 490, 540))}</g>
<rect x="860" y="140" width="200" height="66" rx="18" fill="#0b0b0e"/>
<rect x="872" y="150" width="176" height="46" rx="12" fill="#151824"/>
<circle cx="1010" cy="176" r="4" fill="#ffc060"/>{glow(1010, 176, 16, "#ffc060", 0.6)}
<rect x="950" y="100" width="16" height="44" fill="#0b0b0e"/>
<path d="M0 600 L1920 600 L1920 1080 L0 1080Z" fill="#0b0a0e"/>
<path d="M0 640 C500 600 1400 600 1920 640 L1920 700 L0 700Z" fill="#141218"/>
<rect x="880" y="720" width="160" height="60" rx="8" fill="#08080b"/>
<rect x="892" y="732" width="136" height="36" rx="4" fill="#111318"/>
<circle cx="910" cy="810" r="16" fill="#08080b" stroke="#1d1d24" stroke-width="3"/><circle cx="1010" cy="810" r="16" fill="#08080b" stroke="#1d1d24" stroke-width="3"/>
<ellipse cx="620" cy="880" rx="230" ry="230" fill="none" stroke="#050407" stroke-width="42"/>
<path d="M390 880 L850 880" stroke="#050407" stroke-width="30"/>
<path d="M420 1080 C440 980 480 900 520 860 L560 870 C530 920 510 1000 500 1080Z" fill="#050407"/>
<path d="M820 1080 C800 980 760 900 720 860 L690 870 C720 920 740 1000 750 1080Z" fill="#050407"/>
''', '<linearGradient id="ws7" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#04050b"/><stop offset="1" stop-color="#1c2032"/></linearGradient>')
save("s7", s7)

# S8 — back home in the dark bedroom, the phone lights up: an order on its way to me
incoming = (f'<rect width="380" height="740" fill="#120a0e"/>'
            f'<text x="190" y="110" text-anchor="middle" font-family="{SANS}" font-size="74" font-weight="bold" fill="#f2e6e6">3:00</text>'
            f'<rect x="20" y="170" width="340" height="300" rx="24" fill="#2a1016"/>'
            f'<text x="190" y="232" text-anchor="middle" font-family="{SANS}" font-size="30" fill="#e0a0a0">YOUR ORDER IS</text>'
            f'<text x="190" y="274" text-anchor="middle" font-family="{SANS}" font-size="30" fill="#e0a0a0">ON ITS WAY</text>'
            f'<line x1="60" y1="304" x2="320" y2="304" stroke="#4a1c24" stroke-width="3"/>'
            f'<text x="190" y="350" text-anchor="middle" font-family="{SANS}" font-size="26" fill="#a08088">DRIVER</text>'
            f'<text x="190" y="400" text-anchor="middle" font-family="{SANS}" font-size="38" font-weight="bold" fill="#ffffff">14 LARKIN RD</text>'
            f'<text x="190" y="446" text-anchor="middle" font-family="{SANS}" font-size="28" fill="#ff4a4a">arriving now</text>'
            f'<path d="M60 640 C120 600 160 560 190 520" stroke="#ff3a3a" stroke-width="10" fill="none" stroke-dasharray="20 14"/>'
            f'<circle cx="190" cy="520" r="20" fill="#ff3a3a"/>{glow(190, 520, 40, "#ff3a3a", 0.5)}'
            f'<path d="M60 640 l-20 30 h40z" fill="#e9eef7"/>')
s8 = svg(f'''
<rect width="{W}" height="{H}" fill="#050407"/>
<rect x="1300" y="120" width="260" height="360" fill="#0d1020"/>
<rect x="1300" y="120" width="260" height="360" fill="#3a4a7a" opacity="0.15"/>
<line x1="1430" y1="120" x2="1430" y2="480" stroke="#050407" stroke-width="10"/>
<path d="M0 760 C400 720 1500 720 1920 760 L1920 1080 L0 1080Z" fill="#0d0b12"/>
<path d="M0 760 C300 740 600 760 900 770" stroke="#16131c" stroke-width="20" fill="none"/>
{phone(960, 470, incoming, 420, 820, "#ff4a4a")}
{hand(960, 470)}
''')
save("s8", s8)

# S9 — my front door from inside: the doorbell lit, and in the narrow side window... shapes, waiting
s9 = svg(f'''
<rect width="{W}" height="{H}" fill="#08070b"/>
<rect x="0" y="0" width="1920" height="1080" fill="url(#wall9)"/>
<rect x="680" y="140" width="420" height="860" fill="#1c1517"/>
<rect x="700" y="160" width="380" height="840" fill="#251b1c"/>
<rect x="740" y="200" width="300" height="330" fill="none" stroke="#150f10" stroke-width="8"/>
<rect x="740" y="580" width="300" height="380" fill="none" stroke="#150f10" stroke-width="8"/>
<circle cx="1040" cy="580" r="13" fill="#a7853f"/>
<rect x="1010" y="520" width="16" height="30" rx="4" fill="#3a3030"/>
<rect x="1150" y="200" width="150" height="760" fill="#0c0e18"/>
<rect x="1150" y="200" width="150" height="760" fill="#5a6a9a" opacity="0.12"/>
{glow(1225, 560, 120, "#ff3a2a", 0.18)}
<g clip-path="url(#side9)">
{figure(1190, 960, 640, "#000")}
{figure(1270, 990, 600, "#020102")}
</g>
<rect x="1150" y="200" width="150" height="760" fill="none" stroke="#1c1517" stroke-width="16"/>
<line x1="1225" y1="200" x2="1225" y2="960" stroke="#1c1517" stroke-width="8"/>
<rect x="580" y="480" width="40" height="60" rx="8" fill="#141016"/>
<circle cx="600" cy="510" r="10" fill="#ff4a3a"/>{glow(600, 510, 40, "#ff4a3a", 0.6)}
<polygon points="680,1000 1100,1000 1240,1080 540,1080" fill="#ff8a6a" opacity="0.05"/>
<rect x="0" y="1000" width="1920" height="80" fill="#0a080b"/>
<rect x="760" y="1010" width="260" height="40" rx="6" fill="#2a1418"/>
''', '<linearGradient id="wall9" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0a090d"/><stop offset="0.5" stop-color="#17131a"/><stop offset="1" stop-color="#0a090d"/></linearGradient>'
   '<clipPath id="side9"><rect x="1150" y="200" width="150" height="760"/></clipPath>')
save("s9", s9)
