"""Scenes for 'The Request Line'. Run inside this folder: python3 scenes.py"""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *
import random

r = random.Random(1114)

RED = "#ff2f2a"
AMBER = "#ffb54a"


def snow(n, op=0.6, x0=0, x1=W, y0=0, y1=H, rr=(1.5, 4)):
    return "".join(f'<circle cx="{r.randint(x0, x1)}" cy="{r.randint(y0, y1)}" r="{r.uniform(*rr):.1f}" fill="#e6ecf7" '
                   f'opacity="{r.uniform(.2, op):.2f}"/>' for _ in range(n))


def tower(x, base, h, color="#07080e"):
    """Lattice radio mast with a red beacon on top."""
    top = base - h
    out = [f'<g stroke="{color}" fill="none" stroke-linecap="round">',
           f'<line x1="{x - 34}" y1="{base}" x2="{x - 6}" y2="{top}" stroke-width="7"/>',
           f'<line x1="{x + 34}" y1="{base}" x2="{x + 6}" y2="{top}" stroke-width="7"/>']
    steps = 16
    for i in range(steps):
        y1 = base - h * i / steps; y2 = base - h * (i + 1) / steps
        w1 = 34 - 28 * i / steps; w2 = 34 - 28 * (i + 1) / steps
        out.append(f'<line x1="{x - w1:.0f}" y1="{y1:.0f}" x2="{x + w2:.0f}" y2="{y2:.0f}" stroke-width="3"/>')
        out.append(f'<line x1="{x + w1:.0f}" y1="{y1:.0f}" x2="{x - w2:.0f}" y2="{y2:.0f}" stroke-width="3"/>')
    # guy wires
    for dx in (-420, 420):
        out.append(f'<line x1="{x}" y1="{top + 60}" x2="{x + dx}" y2="{base + 10}" stroke-width="1.5" opacity="0.6"/>')
    out.append('</g>')
    out.append(glow(x, top - 10, 60, RED, 0.7))
    out.append(f'<circle cx="{x}" cy="{top - 10}" r="11" fill="{RED}"/>')
    mid = base - h * .5
    out.append(glow(x, mid, 34, RED, 0.45) + f'<circle cx="{x}" cy="{mid}" r="7" fill="{RED}"/>')
    return "".join(out)


def console(y, x0=300, x1=1620, lit=True):
    """Radio mixing board: slanted top with faders, knobs and two VU meters."""
    out = [f'<polygon points="{x0},{y} {x1},{y} {x1 + 80},{y + 170} {x0 - 80},{y + 170}" fill="#1c1d26"/>',
           f'<rect x="{x0 - 80}" y="{y + 170}" width="{x1 - x0 + 160}" height="{H - y - 170}" fill="#101118"/>',
           f'<line x1="{x0 - 80}" y1="{y + 170}" x2="{x1 + 80}" y2="{y + 170}" stroke="#2c2e3b" stroke-width="4"/>']
    for i in range(14):
        fx = x0 + 70 + i * (x1 - x0 - 140) / 13
        out.append(f'<line x1="{fx:.0f}" y1="{y + 60}" x2="{fx + (fx - 960) * .04:.0f}" y2="{y + 150}" stroke="#07070b" stroke-width="6"/>')
        fy = y + 70 + r.randint(0, 60)
        out.append(f'<rect x="{fx - 13:.0f}" y="{fy}" width="26" height="14" rx="3" fill="#8b8f9e"/>')
        for k in range(2):
            out.append(f'<circle cx="{fx:.0f}" cy="{y + 18 + k * 24}" r="8" fill="#3a3c4a"/>')
        if lit and i % 3 == 0:
            out.append(f'<circle cx="{fx + 16:.0f}" cy="{y + 30}" r="3.5" fill="#7dff8a" opacity="0.8"/>')
    return "".join(out)


def vu(x, y, w=170, h=110, needle=0.3, lit=True, color="#f2c46a"):
    face = color if lit else "#3a3426"
    ang = -60 + 120 * needle
    import math
    nx = x + w / 2 + math.sin(math.radians(ang)) * h * .75
    ny = y + h * .92 - math.cos(math.radians(ang)) * h * .75
    out = [f'<rect x="{x - 8}" y="{y - 8}" width="{w + 16}" height="{h + 16}" rx="8" fill="#0a0a0f"/>',
           f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{face}"/>']
    if lit:
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{face}" opacity="0.5" filter="url(#blur30)"/>')
    out.append(f'<path d="M{x + 25} {y + 45} Q{x + w / 2} {y + 15} {x + w - 25} {y + 45}" stroke="#2a2010" stroke-width="3" fill="none"/>')
    out.append(f'<path d="M{x + w * .7:.0f} {y + 27} Q{x + w * .8:.0f} {y + 32} {x + w - 25} {y + 45}" stroke="#b3241d" stroke-width="5" fill="none"/>')
    out.append(f'<line x1="{x + w / 2}" y1="{y + h * .92:.0f}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#111" stroke-width="3"/>')
    return "".join(out)


def mic(x, y, s=1.0, color="#16171f"):
    """Broadcast mic on a boom arm, capsule centred at (x, y)."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M60 -10 L320 -260 L620 -330" stroke="{color}" stroke-width="16" fill="none" stroke-linejoin="round"/>'
            f'<path d="M80 0 L330 -240" stroke="#2a2c38" stroke-width="4" fill="none"/>'
            f'<circle cx="320" cy="-260" r="16" fill="#2a2c38"/>'
            f'<rect x="-70" y="-150" width="140" height="300" rx="70" fill="#22242f"/>'
            f'<rect x="-70" y="-150" width="140" height="300" rx="70" fill="url(#micgrill)"/>'
            f'<rect x="-80" y="-30" width="160" height="34" rx="6" fill="#0e0f15"/>'
            f'<rect x="-30" y="150" width="60" height="60" fill="#0e0f15"/>'
            f'<path d="M-90 -40 C-90 120 90 120 90 -40" stroke="#0e0f15" stroke-width="14" fill="none"/>'
            f'</g>')


MIC_DEFS = '''<pattern id="mesh" width="14" height="14" patternUnits="userSpaceOnUse">
<circle cx="7" cy="7" r="3" fill="#0b0c11"/></pattern>
<linearGradient id="micgrill" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity="0.5"/>
<stop offset="0.45" stop-color="#9aa0b8" stop-opacity="0.18"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></linearGradient>'''


def studio_back(lamp=True, onair=True, door_open=0.0, figure_in=False, window=True, wx=380):
    """Wide studio wall: snowy window left, studio door with ON AIR sign right."""
    out = [f'<rect width="{W}" height="{H}" fill="#14131c"/>',
           # acoustic panels
           "".join(f'<rect x="{x}" y="{y}" width="150" height="150" fill="#191823" stroke="#0f0e15" stroke-width="6"/>'
                   for x in range(0, W, 160) for y in (60, 220, 380))]
    if window:
        out.append(f'<g transform="translate({wx - 380} 0)">')
        out.append(f'<rect x="380" y="200" width="420" height="320" fill="#0a0c16"/>')
        out.append(f'<rect x="390" y="210" width="400" height="300" fill="url(#winsky)"/>')
        out.append(f'<g clip-path="url(#winclip)">{snow(140, .7, 390, 790, 210, 510)}'
                   f'<path d="M390 470 C500 450 650 480 790 455 L790 510 L390 510Z" fill="#c6d0e4" opacity="0.35"/>'
                   f'{tower(690, 500, 230, "#050609")}</g>')
        out.append(f'<rect x="380" y="200" width="420" height="320" fill="none" stroke="#08080c" stroke-width="18"/>'
                   f'<line x1="590" y1="200" x2="590" y2="520" stroke="#08080c" stroke-width="10"/></g>')
    # door
    dx, dy, dw, dh = 1180, 170, 300, 560
    out.append(f'<rect x="{dx - 20}" y="{dy - 20}" width="{dw + 40}" height="{dh + 20}" fill="#08080c"/>')
    if door_open > 0:
        out.append(f'<rect x="{dx}" y="{dy}" width="{dw}" height="{dh}" fill="#030305"/>')
        out.append(f'<g clip-path="url(#doorclip)">'
                   + f'<rect x="{dx}" y="{dy}" width="{dw}" height="{dh}" fill="url(#stairlight)"/>'
                   + "".join(f'<rect x="{dx}" y="{dy + dh - 60 - i * 70}" width="{dw}" height="8" fill="#15141c" opacity="{.7 - i * .1:.2f}"/>' for i in range(6))
                   + (figure(dx + 120, dy + dh + 30, 560, "#000") + eyes(dx + 120, dy + 85, 22, 5) if figure_in else "")
                   + '</g>')
        ow = dw * (1 - door_open)
        out.append(f'<polygon points="{dx + dw},{dy} {dx + dw - ow:.0f},{dy + 30} {dx + dw - ow:.0f},{dy + dh - 20} {dx + dw},{dy + dh}" fill="#2a2630"/>')
        out.append(f'<circle cx="{dx + dw - ow + 26:.0f}" cy="{dy + dh * .55:.0f}" r="11" fill="#8d8a96"/>')
    else:
        out.append(f'<rect x="{dx}" y="{dy}" width="{dw}" height="{dh}" fill="#2a2630"/>'
                   f'<rect x="{dx + 70}" y="{dy + 60}" width="160" height="110" fill="#06070c" stroke="#15141a" stroke-width="8"/>'
                   f'<circle cx="{dx + 40}" cy="{dy + dh * .55:.0f}" r="11" fill="#8d8a96"/>')
    # ON AIR sign
    sx, sy = dx + dw / 2, 90
    if onair:
        out.append(glow(sx, sy, 130, RED, .55))
    out.append(f'<rect x="{sx - 110}" y="{sy - 34}" width="220" height="68" rx="8" fill="{"#d81f1a" if onair else "#3a1514"}" stroke="#08080c" stroke-width="6"/>'
               f'<text x="{sx}" y="{sy + 15}" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="42" letter-spacing="6" fill="{"#ffe9e0" if onair else "#5b2a28"}">ON AIR</text>')
    if lamp:
        out.append(glow(240, 640, 260, AMBER, .35))
    return "".join(out)


STUDIO_DEFS = MIC_DEFS + '''<linearGradient id="winsky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b1022"/>
<stop offset="1" stop-color="#2c3550"/></linearGradient>
<clipPath id="winclip"><rect x="390" y="210" width="400" height="300"/></clipPath>
<radialGradient id="stairlight" cx="0.4" cy="0.35" r="0.7"><stop offset="0" stop-color="#3b4766"/><stop offset="1" stop-color="#05060a"/></radialGradient>
<clipPath id="doorclip"><rect x="1180" y="170" width="300" height="560"/></clipPath>'''

# S1 - the little station in the snow
skyd = sky("sky1", "#04060e", "#141c33", "#2c3552")
s1 = f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(120, 520, .6)}
{moon(420, 210, 70, "#dfe4f0")}
<path d="M0 760 C300 730 700 745 1000 750 C1300 755 1600 730 1920 745 L1920 1080 L0 1080Z" fill="#9aa6c0"/>
<path d="M0 760 C300 730 700 745 1000 750 C1300 755 1600 730 1920 745 L1920 1080 L0 1080Z" fill="#0c1020" opacity="0.55"/>
{tower(1220, 760, 640)}
<g fill="#080a12">
<rect x="620" y="560" width="480" height="210"/>
<polygon points="600,566 1120,566 1100,540 620,540"/>
<rect x="1050" y="480" width="22" height="70"/>
<rect x="680" y="610" width="70" height="140" fill="#05060b"/>
</g>
<path d="M600 542 C700 528 900 530 1120 538 L1120 548 L600 548Z" fill="#c9d3e6" opacity="0.8"/>
{lit_window(860, 615, 120, 76)}
<polygon points="860,770 980,770 1040,900 800,900" fill="{AMBER}" opacity="0.10" filter="url(#blur8)"/>
<rect x="640" y="585" width="220" height="34" fill="#16192a"/>
<text x="750" y="610" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="24" letter-spacing="4" fill="#8e98b4">KVLR 1290</text>
{dead_tree(250, 790, 300, "#06070d", .9)}
{dead_tree(1660, 780, 260, "#06070d", .8)}
<path d="M0 860 C500 830 1300 860 1920 840 L1920 1080 L0 1080Z" fill="#7d89a6" opacity="0.35"/>
{fog(780, "#c8d1e6", .14)}
{snow(320, .75)}
'''
save("s1", svg(s1, skyd))

# S2 - the sticky note on the microphone
s2 = f'''
<rect width="{W}" height="{H}" fill="#121119"/>
{"".join(f'<rect x="{x}" y="{y}" width="190" height="190" fill="#17161f" stroke="#0e0d14" stroke-width="8"/>' for x in range(0, W, 200) for y in (-40, 160, 360))}
{glow(1000, 420, 380, AMBER, .14)}
{console(720, 200, 1720)}
{mic(780, 450, 1.25)}
<g transform="rotate(-5 1080 520)">
<rect x="935" y="410" width="330" height="270" fill="#000" opacity="0.4" filter="url(#blur8)"/>
<rect x="915" y="395" width="330" height="270" fill="#f2d65c"/>
<rect x="915" y="395" width="330" height="34" fill="#e6c54a"/>
<text x="1080" y="510" text-anchor="middle" font-family="DejaVu Sans, sans-serif" font-style="oblique" font-size="34" fill="#2b2210">AFTER 3 AM</text>
<text x="1080" y="560" text-anchor="middle" font-family="DejaVu Sans, sans-serif" font-style="oblique" font-weight="bold" font-size="34" fill="#2b2210">DON'T ANSWER</text>
<line x1="955" y1="575" x2="1205" y2="572" stroke="#8c1c1c" stroke-width="4"/>
<text x="1080" y="625" text-anchor="middle" font-family="DejaVu Sans, sans-serif" font-style="oblique" font-size="26" fill="#2b2210">never on air</text>
</g>
'''
save("s2", svg(s2, MIC_DEFS))

# S3 - me, alone at the board, snow outside
s3 = f'''
{studio_back(lamp=False, onair=False, wx=560)}
{glow(960, 560, 200, "#6f86c0", .22)}
{console(760, 260, 1660)}
<g fill="#050508">
<path d="M760 1080 C760 900 800 820 900 790 C930 760 990 760 1020 790 C1120 820 1160 900 1160 1080Z"/>
<ellipse cx="960" cy="700" rx="78" ry="92"/>
<path d="M870 700 C870 600 1050 600 1050 700" stroke="#050508" stroke-width="22" fill="none"/>
<rect x="852" y="672" width="40" height="70" rx="16"/><rect x="1028" y="672" width="40" height="70" rx="16"/>
</g>
<path d="M880 640 C900 600 1020 600 1040 640" stroke="#6f86c0" stroke-width="4" opacity="0.6" fill="none"/>
<path d="M800 830 C840 795 880 785 900 790" stroke="#6f86c0" stroke-width="4" opacity="0.4" fill="none"/>
<path d="M1120 830 C1080 795 1040 785 1020 790" stroke="#6f86c0" stroke-width="4" opacity="0.4" fill="none"/>
{glow(960, 790, 220, "#7dff8a", .05)}
<rect x="1150" y="690" width="160" height="70" fill="#0a0a10"/>
<text x="1230" y="740" text-anchor="middle" font-family="{MONO}" font-size="44" fill="#ff5a3c">2:51</text>
'''
save("s3", svg(s3, STUDIO_DEFS))


# S4 - the request line blinking
def phone(blink=True):
    out = [f'<rect x="560" y="430" width="800" height="440" rx="40" fill="#1b1c25"/>',
           f'<rect x="560" y="430" width="800" height="440" rx="40" fill="none" stroke="#0a0a0f" stroke-width="10"/>',
           # handset
           f'<path d="M600 470 C600 400 1320 400 1320 470 L1320 540 C1320 570 1240 570 1240 540 L1240 510 L680 510 L680 540 C680 570 600 570 600 540Z" fill="#101118"/>']
    for i in range(4):
        y = 600 + i * 60
        on = blink and i == 0
        out.append(f'<rect x="640" y="{y}" width="90" height="40" rx="6" fill="{"#ff3d2e" if on else "#3a1b1c"}"/>')
        out.append(f'<text x="760" y="{y + 30}" font-family="{SANS}" font-size="26" fill="#6d7085" letter-spacing="2">'
                   f'{["REQUEST", "LINE 2", "LINE 3", "HOTLINE"][i]}</text>')
    if blink:
        out.append(glow(685, 620, 120, RED, .8))
    for k in range(12):
        bx = 1000 + (k % 3) * 90; by = 600 + (k // 3) * 60
        out.append(f'<rect x="{bx}" y="{by}" width="70" height="44" rx="8" fill="#2a2c38"/>'
                   f'<text x="{bx + 35}" y="{by + 32}" text-anchor="middle" font-family="{SANS}" font-size="26" fill="#9aa0b8">{"123456789*0#"[k]}</text>')
    return "".join(out)


s4 = f'''
<rect width="{W}" height="{H}" fill="#0d0d13"/>
<rect x="0" y="760" width="{W}" height="320" fill="#191a22"/>
{glow(960, 650, 420, "#3a4060", .25)}
<path d="M560 860 C400 900 300 980 200 1080" stroke="#0a0a0e" stroke-width="10" fill="none"/>
{phone(True)}
<rect x="1080" y="250" width="230" height="110" rx="10" fill="#08080c"/>
<text x="1195" y="330" text-anchor="middle" font-family="{MONO}" font-size="64" fill="#ff5a3c">3:06</text>
{glow(1195, 305, 90, "#ff5a3c", .25)}
<rect x="240" y="640" width="200" height="160" rx="12" fill="#2a2420" opacity="0.9"/>
<ellipse cx="340" cy="645" rx="100" ry="18" fill="#110c09"/>
<path d="M440 680 C490 680 490 760 440 760" stroke="#2a2420" stroke-width="14" fill="none"/>
'''
save("s4", svg(s4, ""))

# S5 - ON AIR lights up by itself
s5 = f'''
{studio_back(lamp=False, onair=True, window=False)}
{glow(1330, 300, 420, RED, .18)}
{console(800, 260, 1660)}
<g transform="translate(860 700)">
<path d="M-110 40 C-110 -120 110 -120 110 40" stroke="#08080c" stroke-width="22" fill="none"/>
<rect x="-140" y="10" width="60" height="96" rx="24" fill="#0b0b10"/><rect x="80" y="10" width="60" height="96" rx="24" fill="#0b0b10"/>
<path d="M110 80 C200 160 120 220 260 240" stroke="#08080c" stroke-width="8" fill="none"/>
</g>
'''
save("s5", svg(s5, STUDIO_DEFS))

# S6 - mic live, meters jumping, nobody speaking
s6 = f'''
<rect width="{W}" height="{H}" fill="#0f0e15"/>
{"".join(f'<rect x="{x}" y="{y}" width="190" height="190" fill="#15141d" stroke="#0c0b11" stroke-width="8"/>' for x in range(0, W, 200) for y in (-40, 160, 360))}
{glow(960, 420, 360, RED, .18)}
{console(720, 200, 1720)}
{vu(560, 560, needle=0.92)}{vu(1190, 560, needle=0.85)}
{mic(960, 440, 1.1)}
<g opacity="0.9">{"".join(f'<path d="M{1070 + i * 28} {420 - i * 4} q18 {40 + i * 6} 0 {80 + i * 12}" stroke="{RED}" stroke-width="4" fill="none" opacity="{.7 - i * .15:.2f}"/>' for i in range(4))}</g>
<rect x="760" y="700" width="400" height="16" fill="#08080c"/>
'''
save("s6", svg(s6, MIC_DEFS))

# S7 - through the studio glass: the stairwell
steps = "".join(f'<polygon points="{620 + i * 70},{860 - i * 60} {1300 + i * 40},{860 - i * 60} {1300 + i * 40},{880 - i * 60} {620 + i * 70},{880 - i * 60}" fill="#1d1f2c"/>'
                f'<rect x="{620 + i * 70}" y="{880 - i * 60}" width="{680 - i * 30}" height="40" fill="#11121b"/>' for i in range(8))
s7 = f'''
<rect width="{W}" height="{H}" fill="#0c0c12"/>
<rect x="380" y="140" width="1160" height="760" fill="#06060a"/>
<g clip-path="url(#glass)">
<rect x="380" y="140" width="1160" height="760" fill="#0f1019"/>
{steps}
<rect x="1180" y="160" width="12" height="720" fill="#252736"/>
<path d="M600 900 L1240 380" stroke="#2c2f40" stroke-width="10"/>
{glow(1300, 220, 120, "#9fb4e8", .25)}
<circle cx="1300" cy="200" r="16" fill="#cfd8ee" opacity="0.8"/>
<path d="M880 700 C860 560 880 420 920 330 C940 290 980 290 990 330 C1020 420 1030 560 1010 700 Z" fill="#000" opacity="0.85" filter="url(#blur8)"/>
{figure(950, 720, 420, "#000")}
</g>
<rect x="380" y="140" width="1160" height="760" fill="url(#glare)"/>
<rect x="380" y="140" width="1160" height="760" fill="none" stroke="#1a1924" stroke-width="30"/>
<rect x="0" y="900" width="{W}" height="180" fill="#14141c"/>
{glow(1720, 120, 160, RED, .35)}
'''
save("s7", svg(s7, '''<clipPath id="glass"><rect x="380" y="140" width="1160" height="760"/></clipPath>
<linearGradient id="glare" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0.06"/>
<stop offset="0.4" stop-color="#fff" stop-opacity="0"/><stop offset="0.6" stop-color="#fff" stop-opacity="0.04"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'''))

# S8 - cables torn out, dead air
cables = "".join(f'<path d="M{x} 760 C{x + r.randint(-120, 120)} {900 + r.randint(0, 60)} {x + r.randint(-260, 260)} {980} {x + r.randint(-300, 300)} 1080" '
                 f'stroke="{r.choice(["#2b2d3a", "#3a2222", "#22303a"])}" stroke-width="{r.choice([8, 10, 12])}" fill="none" stroke-linecap="round"/>'
                 for x in range(560, 1400, 55))
plugs = "".join(f'<rect x="{x - 9}" y="{1000 + r.randint(-60, 40)}" width="18" height="40" rx="3" fill="#8b8f9e"/>' for x in range(600, 1400, 110))
s8 = f'''
<rect width="{W}" height="{H}" fill="#08080c"/>
{"".join(f'<rect x="{x}" y="{y}" width="190" height="190" fill="#0e0d14" stroke="#08070c" stroke-width="8"/>' for x in range(0, W, 200) for y in (-40, 160, 360))}
{console(620, 260, 1660, lit=False)}
{vu(560, 470, needle=0.0, lit=False)}{vu(1190, 470, needle=0.0, lit=False)}
<rect x="520" y="740" width="880" height="40" fill="#050508"/>
{"".join(f'<circle cx="{x}" cy="760" r="9" fill="#000"/>' for x in range(560, 1400, 55))}
{cables}{plugs}
{glow(980, 980, 40, "#ffd27a", .8)}<circle cx="980" cy="980" r="5" fill="#fff4d0"/>
<path d="M980 980 l-30 -26 m30 26 l34 -20 m-34 20 l8 -40" stroke="#ffd27a" stroke-width="3"/>
'''
save("s8", svg(s8, ""))

# S9 - the stairwell door opens behind me
s9 = f'''
{studio_back(lamp=False, onair=True, door_open=0.75, figure_in=True, window=True)}
{glow(1330, 120, 300, RED, .2)}
{console(800, 260, 1660, lit=False)}
<polygon points="1180,730 1480,730 1560,1080 1100,1080" fill="#000" opacity="0.6" filter="url(#blur8)"/>
'''
save("s9", svg(s9, STUDIO_DEFS))
