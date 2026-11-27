"""Scenes for The Peephole (apartment 4C, a strip of black tape over the peephole, and a knock at 2:01 AM)."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

RED = "#ff2a18"
WARM = "#ffb54a"
BRASS = '<linearGradient id="brass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e3c37a"/><stop offset="0.5" stop-color="#a7853f"/><stop offset="1" stop-color="#4e3712"/></linearGradient>'
BIG = ('<filter id="bb30" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="30"/></filter>'
       '<filter id="bb60" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="60"/></filter>'
       '<filter id="bb12" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="12"/></filter>')


def glow(cx, cy, r, color, op=0.6):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" opacity="{op}" filter="url(#bb30)"/>'


def door_front(x, y, w, h, wood="url(#doorw)", number="4C", tape=True, hole=False, peep_r=22):
    """Apartment door seen straight on from inside/outside. Peephole at upper centre."""
    cx = x + w / 2; py = y + h * 0.3
    o = [f'<rect x="{x - 26}" y="{y - 26}" width="{w + 52}" height="{h + 26}" fill="#0c0807"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{wood}"/>']
    for (px, pyy, pw, ph) in [(x + 40, y + 40, w / 2 - 60, h * .42), (x + w / 2 + 20, y + 40, w / 2 - 60, h * .42),
                              (x + 40, y + h * .5, w / 2 - 60, h * .45), (x + w / 2 + 20, y + h * .5, w / 2 - 60, h * .45)]:
        o.append(f'<rect x="{px:.0f}" y="{pyy:.0f}" width="{pw:.0f}" height="{ph:.0f}" fill="none" stroke="#120a07" stroke-width="8" opacity="0.8"/>')
        o.append(f'<rect x="{px + 6:.0f}" y="{pyy + 6:.0f}" width="{pw - 12:.0f}" height="{ph - 12:.0f}" fill="none" stroke="#4a3120" stroke-width="2" opacity="0.5"/>')
    if number:
        o.append(f'<rect x="{cx - 46:.0f}" y="{py - 110:.0f}" width="92" height="52" rx="6" fill="url(#brass)"/>'
                 f'<text x="{cx:.0f}" y="{py - 71:.0f}" text-anchor="middle" font-family="{SERIF}" font-size="38" font-weight="bold" fill="#2a1c0a">{number}</text>')
    if hole:
        o.append(f'<circle cx="{cx:.0f}" cy="{py:.0f}" r="{peep_r * .7:.0f}" fill="#000"/>')
    else:
        o.append(f'<circle cx="{cx:.0f}" cy="{py:.0f}" r="{peep_r}" fill="url(#brass)"/><circle cx="{cx:.0f}" cy="{py:.0f}" r="{peep_r * .55:.0f}" fill="#0b0d14"/>')
    if tape:
        tw = peep_r * 4.4; th = peep_r * 1.5
        o.append(f'<rect x="{cx - tw / 2:.0f}" y="{py - th / 2:.0f}" width="{tw:.0f}" height="{th:.0f}" fill="#0a0a0c" transform="rotate(-8 {cx:.0f} {py:.0f})"/>'
                 f'<rect x="{cx - tw / 2:.0f}" y="{py - th / 2:.0f}" width="{tw:.0f}" height="6" fill="#2b2b33" opacity="0.7" transform="rotate(-8 {cx:.0f} {py:.0f})"/>')
    # deadbolt, chain, knob
    o.append(f'<circle cx="{x + w - 70:.0f}" cy="{y + h * .48:.0f}" r="20" fill="url(#brass)"/>'
             f'<rect x="{x + w - 78:.0f}" y="{y + h * .48 - 14:.0f}" width="16" height="28" rx="4" fill="#5e4318"/>'
             f'<circle cx="{x + w - 70:.0f}" cy="{y + h * .58:.0f}" r="30" fill="url(#brass)"/>'
             f'<rect x="{x + w - 150:.0f}" y="{y + h * .4:.0f}" width="40" height="14" rx="4" fill="url(#brass)"/>'
             f'<path d="M{x + w - 130:.0f} {y + h * .4 + 14:.0f} q-40 70 -90 40" stroke="#b08c3e" stroke-width="6" fill="none" stroke-dasharray="14 6"/>')
    return "".join(o)


def hand(x, y, s=1.0, col="#0a0606", rot=0):
    """Silhouette hand reaching right, fingertips around (x, y)."""
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" fill="{col}">'
            f'<rect x="-230" y="-60" width="200" height="30" rx="15"/>'
            f'<rect x="-220" y="-24" width="215" height="32" rx="16"/>'
            f'<rect x="-230" y="14" width="200" height="30" rx="15"/>'
            f'<rect x="-250" y="50" width="160" height="28" rx="14"/>'
            f'<rect x="-300" y="-80" width="150" height="40" rx="20" transform="rotate(-28 -230 -60)"/>'
            f'<ellipse cx="-310" cy="0" rx="120" ry="95"/>'
            f'<rect x="-760" y="-70" width="470" height="150" rx="70"/></g>')


scenes = {}

# S1 — the apartment building at night, one lit window on the fourth floor
bricks = "".join(f'<line x1="560" y1="{y}" x2="1360" y2="{y}" stroke="#1c1218" stroke-width="2" opacity="0.6"/>' for y in range(160, 940, 22))
wins = []
for fl, wy in enumerate((200, 360, 520, 680)):
    for wx in (640, 830, 1020, 1210):
        if fl == 0 and wx == 1020:
            continue
        wins.append(f'<rect x="{wx}" y="{wy}" width="80" height="110" fill="#0d0f1a"/><rect x="{wx}" y="{wy}" width="80" height="110" fill="none" stroke="#2a1e24" stroke-width="6"/>'
                    f'<line x1="{wx + 40}" y1="{wy}" x2="{wx + 40}" y2="{wy + 110}" stroke="#2a1e24" stroke-width="4"/>'
                    f'<rect x="{wx - 8}" y="{wy + 110}" width="96" height="10" fill="#2e2228"/>')
lit = lit_window(1020, 200, 80, 110, WARM, "#2a1e24")
fire_esc = "".join(f'<rect x="1180" y="{wy + 118}" width="140" height="8" fill="#07060a"/>'
                   f'<g stroke="#07060a" stroke-width="3">{"".join(f"<line x1=\"{xx}\" y1=\"{wy + 90}\" x2=\"{xx}\" y2=\"{wy + 120}\"/>" for xx in range(1182, 1322, 14))}</g>'
                   f'<line x1="1185" y1="{wy + 90}" x2="1320" y2="{wy + 90}" stroke="#07060a" stroke-width="4"/>'
                   f'<line x1="1200" y1="{wy + 125}" x2="1300" y2="{wy + 280}" stroke="#07060a" stroke-width="6"/>' for wy in (200, 360, 520))
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(120, 500, 0.6)}
{moon(1520, 190, 80)}
<rect x="0" y="420" width="420" height="660" fill="#0a0a14"/><rect x="1500" y="360" width="420" height="720" fill="#0a0a14"/>
{"".join(f'<rect x="{x}" y="{y}" width="40" height="50" fill="#1a1c2a"/>' for x, y in ((80, 500), (200, 620), (300, 480), (1580, 450), (1700, 600), (1800, 480)))}
<rect x="1600" y="560" width="40" height="50" fill="#5a4a30" opacity="0.6"/>
<rect x="540" y="140" width="840" height="800" fill="url(#brick)"/>
{bricks}
<rect x="520" y="120" width="880" height="30" fill="#1a1016"/>
<rect x="600" y="80" width="60" height="50" fill="#120c10"/><rect x="1240" y="90" width="70" height="40" fill="#120c10"/>
{"".join(wins)}
{lit}
{glow(1060, 255, 160, WARM, 0.25)}
<rect x="1040" y="230" width="22" height="80" fill="#3a1e10" opacity="0.6"/>
{fire_esc}
<rect x="880" y="800" width="160" height="140" fill="#0a0708"/><rect x="890" y="810" width="140" height="70" fill="#3a3020" opacity="0.7"/>
<rect x="860" y="780" width="200" height="20" fill="#24181c"/>
<rect x="880" y="940" width="160" height="14" fill="#1e1a22"/><rect x="860" y="954" width="200" height="14" fill="#1a161e"/>
<rect x="0" y="940" width="{W}" height="140" fill="#101018"/>
<rect x="0" y="1000" width="{W}" height="6" fill="#1c1c28"/>
<rect x="470" y="560" width="10" height="440" fill="#050508"/><path d="M475 560 q0 -30 40 -30 h20" stroke="#050508" stroke-width="10" fill="none"/>
<rect x="520" y="524" width="40" height="16" rx="4" fill="#ffe2a8"/>
<polygon points="525,540 555,540 650,1000 430,1000" fill="#ffd890" opacity="0.07"/>
{glow(540, 540, 70, "#ffd890", 0.5)}
{fog(960, op=0.12)}
''', sky("sky1", "#04050c", "#141530", "#2a1e34") + BRASS + BIG +
    '<linearGradient id="brick" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2c1a1e"/><stop offset="1" stop-color="#1a1014"/></linearGradient>')

# S2 — the door of 4C from inside, black tape over the peephole
DOORW = '<linearGradient id="doorw" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a2618"/><stop offset="1" stop-color="#22160e"/></linearGradient>'
paper = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="1000" stroke="#2c2418" stroke-width="10" opacity="0.35"/>' for x in range(0, W, 60))
scenes["s2"] = svg(f'''
<rect width="{W}" height="{H}" fill="#1a150f"/>
{paper}
<rect x="0" y="0" width="{W}" height="{H}" fill="url(#lamp2)"/>
{door_front(720, 110, 480, 890, peep_r=32)}
{glow(960, 377, 110, "#ffd28a", 0.12)}
<rect x="0" y="1000" width="{W}" height="80" fill="#140d08"/>
<rect x="0" y="990" width="{W}" height="14" fill="#2a1c12"/>
<rect x="700" y="1000" width="520" height="26" fill="#3a2a1c" opacity="0.6"/>
<rect x="360" y="380" width="200" height="16" fill="#2a1c12"/><rect x="380" y="396" width="10" height="40" fill="#2a1c12"/>
<g fill="#0d0907"><rect x="400" y="320" width="14" height="60"/><circle cx="430" cy="340" r="10"/><rect x="460" y="350" width="70" height="30"/></g>
{glow(470, 330, 120, WARM, 0.18)}
{glow(960, 380, 90, "#ffffff", 0.05)}
''', DOORW + BRASS + BIG +
    '<radialGradient id="lamp2" cx="300" cy="300" r="1300" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#ffb54a" stop-opacity="0.18"/><stop offset="1" stop-color="#000" stop-opacity="0.55"/></radialGradient>')

# S3 — the dark apartment at 2:01, light under the door
scenes["s3"] = svg(f'''
<rect width="{W}" height="{H}" fill="#07080d"/>
<rect x="0" y="0" width="{W}" height="780" fill="#0c0e16"/>
<rect x="0" y="780" width="{W}" height="300" fill="#0a0809"/>
<g stroke="#120f12" stroke-width="3">{"".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in (840, 920, 1020))}</g>
<rect x="300" y="160" width="220" height="320" fill="#141a2c"/><rect x="300" y="160" width="220" height="320" fill="#5a70a8" opacity="0.18"/>
<line x1="410" y1="160" x2="410" y2="480" stroke="#07080d" stroke-width="8"/><line x1="300" y1="320" x2="520" y2="320" stroke="#07080d" stroke-width="8"/>
<polygon points="300,480 520,480 640,780 240,780" fill="#5a70a8" opacity="0.05"/>
<path d="M380 760 v-170 q0 -50 60 -50 h300 q60 0 60 50 v170 z" fill="#050508"/>
<rect x="350" y="640" width="480" height="140" rx="30" fill="#060609"/>
<rect x="640" y="660" width="140" height="110" fill="#08080c"/>
<rect x="860" y="620" width="150" height="160" fill="#0a090c"/><rect x="852" y="610" width="166" height="14" fill="#0c0b10"/>
<rect x="872" y="560" width="126" height="54" rx="8" fill="#030303"/>
<text x="935" y="601" text-anchor="middle" font-family="{MONO}" font-size="40" font-weight="bold" fill="{RED}">2:01</text>
{glow(935, 588, 70, RED, 0.35)}
<rect x="1100" y="200" width="300" height="580" fill="#0b0906"/>
<rect x="1080" y="180" width="340" height="20" fill="#060506"/>
<circle cx="1250" cy="370" r="10" fill="#2a2418"/>
<circle cx="1360" cy="500" r="16" fill="#3a3020"/>
<rect x="1100" y="772" width="300" height="10" fill="#ffd08a"/>
<polygon points="1100,782 1400,782 1560,960 940,960" fill="url(#spill3)"/>
<rect x="1100" y="772" width="300" height="10" fill="#ffd08a" filter="url(#blur8)"/>
<rect x="1170" y="772" width="60" height="10" fill="#000"/><rect x="1270" y="772" width="60" height="10" fill="#000"/>
<polygon points="1170,782 1230,782 1250,960 1140,960" fill="#000" opacity="0.6"/><polygon points="1270,782 1330,782 1370,960 1270,960" fill="#000" opacity="0.6"/>
''', BIG + '<linearGradient id="spill3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffd08a" stop-opacity="0.35"/><stop offset="1" stop-color="#ffd08a" stop-opacity="0"/></linearGradient>')

# S4 — the hallway outside: a tall figure pressed against door 4C
hall_doors = []
for i, t in enumerate((0.0, 0.35, 0.6, 0.78)):
    # left and right doors receding toward vanishing point (960, 470)
    def lerp(a, b): return a + (b - a) * t
    xl = lerp(140, 800); xr = lerp(1780, 1120); top = lerp(200, 400); bot = lerp(1000, 640); dw = lerp(170, 40)
    hall_doors.append(f'<polygon points="{xl:.0f},{top:.0f} {xl + dw:.0f},{top + dw * .25:.0f} {xl + dw:.0f},{bot - dw * .3:.0f} {xl:.0f},{bot:.0f}" fill="#1a0e0c"/>')
    hall_doors.append(f'<polygon points="{xr:.0f},{top:.0f} {xr - dw:.0f},{top + dw * .25:.0f} {xr - dw:.0f},{bot - dw * .3:.0f} {xr:.0f},{bot:.0f}" fill="#1a0e0c"/>')
lights = "".join(f'<rect x="{960 - w / 2:.0f}" y="{y:.0f}" width="{w:.0f}" height="{w * .12:.0f}" fill="#e8dcb8" opacity="{op}"/>' for w, y, op in ((300, 60, 0.15), (170, 230, 0.8), (100, 320, 0.7), (60, 372, 0.6)))
scenes["s4"] = svg(f'''
<rect width="{W}" height="{H}" fill="#100b0b"/>
<polygon points="0,0 800,400 800,640 0,1080" fill="url(#wl4)"/>
<polygon points="1920,0 1120,400 1120,640 1920,1080" fill="url(#wr4)"/>
<polygon points="0,0 1920,0 1120,400 800,400" fill="#0b0808"/>
<polygon points="0,1080 800,640 1120,640 1920,1080" fill="url(#carpet)"/>
<g stroke="#2a0f10" stroke-width="3" opacity="0.6">{"".join(f'<line x1="960" y1="640" x2="{x}" y2="1080"/>' for x in range(-400, 2400, 240))}</g>
{"".join(hall_doors)}
{lights}
{glow(960, 250, 140, "#e8dcb8", 0.18)}
<rect x="800" y="400" width="320" height="240" fill="#1c1210"/>
<rect x="880" y="430" width="160" height="210" fill="url(#doorw)"/>
<rect x="944" y="462" width="32" height="18" rx="3" fill="url(#brass)"/>
<circle cx="960" cy="498" r="6" fill="url(#brass)"/>
<rect x="912" y="402" width="96" height="24" rx="3" fill="#5a0a08"/>
<text x="960" y="421" text-anchor="middle" font-family="{SANS}" font-size="19" font-weight="bold" fill="#ff4a38">EXIT</text>
{glow(960, 412, 70, RED, 0.45)}
<g transform="translate(960 650) scale(1.75) translate(-960 -650)">
<ellipse cx="960" cy="458" rx="26" ry="34" fill="#030203"/>
<path d="M920 640 L924 560 C914 520 922 500 960 494 C998 500 1006 520 996 560 L1000 640 Z" fill="#030203"/>
<path d="M926 506 C900 540 900 580 906 620" stroke="#030203" stroke-width="12" fill="none" stroke-linecap="round"/>
<path d="M994 506 C1022 520 1024 500 1000 470" stroke="#030203" stroke-width="12" fill="none" stroke-linecap="round"/>
</g>
<ellipse cx="960" cy="652" rx="150" ry="14" fill="#000" opacity="0.7"/>
{fog(700, "#7a6a6a", 0.08, 80)}
''', BRASS + DOORW + BIG +
    '<linearGradient id="wl4" x1="0" x2="1"><stop offset="0" stop-color="#2c1c16"/><stop offset="1" stop-color="#140c0b"/></linearGradient>'
    '<linearGradient id="wr4" x1="1" x2="0"><stop offset="0" stop-color="#2c1c16"/><stop offset="1" stop-color="#140c0b"/></linearGradient>'
    '<linearGradient id="carpet" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#3a1414"/><stop offset="1" stop-color="#160808"/></linearGradient>')

# S5 — close-up: fingers peeling back the tape from the peephole
grain = "".join(f'<path d="M{x} 0 C{x + 30} 300 {x - 30} 700 {x + 14} 1080" stroke="#120b07" stroke-width="3" fill="none" opacity="0.55"/>' for x in range(40, W, 120))
scenes["s5"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#door5)"/>
{grain}
{glow(960, 520, 300, "#ffd28a", 0.10)}
<circle cx="960" cy="520" r="120" fill="url(#brass)"/>
<circle cx="960" cy="520" r="120" fill="none" stroke="#3a2810" stroke-width="6"/>
<circle cx="960" cy="520" r="78" fill="#5e4318"/>
<circle cx="960" cy="520" r="62" fill="#05060a"/>
<ellipse cx="940" cy="500" rx="20" ry="12" fill="#8aa0c8" opacity="0.35"/>
<path d="M800 470 L1010 440 L1010 590 L800 620 Z" fill="#0a0a0c"/>
<path d="M800 470 L1010 440 L1010 455 L800 485 Z" fill="#2b2b33" opacity="0.7"/>
<path d="M1010 440 C1090 420 1140 470 1120 540 C1110 580 1060 600 1010 590 Z" fill="#141418"/>
<path d="M1010 440 C1070 432 1100 470 1090 520" stroke="#3a3a44" stroke-width="4" fill="none" opacity="0.7"/>
<g transform="translate(1180 520) scale(-1 1)">{hand(0, 0, 1.0, "#0a0606", 8)}</g>
{glow(1150, 520, 120, "#000", 0.0)}
''', BRASS + BIG + '<linearGradient id="door5" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1e130c"/><stop offset="1" stop-color="#3a2419"/></linearGradient>')


# S6 / S6b — the view through the peephole: a dark blurry circle... that blinks
def peep_view(inner):
    return svg(f'''
<rect width="{W}" height="{H}" fill="#000"/>
<defs><clipPath id="lens"><circle cx="960" cy="540" r="360"/></clipPath></defs>
<g clip-path="url(#lens)">
<rect width="{W}" height="{H}" fill="#0b0a0c"/>
{inner}
<circle cx="960" cy="540" r="360" fill="url(#fish)"/>
</g>
<circle cx="960" cy="540" r="362" fill="none" stroke="#000" stroke-width="30" filter="url(#bb12)"/>
<ellipse cx="860" cy="400" rx="90" ry="40" fill="#ffffff" opacity="0.05" transform="rotate(-30 860 400)"/>
''', BIG + '<radialGradient id="fish" cx="960" cy="540" r="360" gradientUnits="userSpaceOnUse"><stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.95"/></radialGradient>')


blur_dark = f'''<g filter="url(#bb30)"><ellipse cx="960" cy="540" rx="300" ry="280" fill="#16131a"/>
<path d="M700 300 Q960 220 1220 300" stroke="#2a2420" stroke-width="30" fill="none"/>
<ellipse cx="960" cy="560" rx="180" ry="190" fill="#0a080b"/></g>{glow(1150, 330, 60, RED, 0.25)}'''
scenes["s6"] = peep_view(blur_dark)

eye = f'''<ellipse cx="960" cy="540" rx="560" ry="420" fill="#2a1c1a" filter="url(#bb30)"/>
<path d="M560 560 Q960 230 1360 560 Q960 820 560 560 Z" fill="#d8ccc0"/>
<path d="M560 560 Q960 230 1360 560 Q960 820 560 560 Z" fill="url(#eyeShade)"/>
<g stroke="#a04848" stroke-width="2" opacity="0.5" fill="none"><path d="M600 560 q80 -20 140 10"/><path d="M1320 560 q-80 30 -150 0"/><path d="M640 520 q60 0 110 30"/></g>
<circle cx="960" cy="545" r="170" fill="#4a0e0c"/>
<circle cx="960" cy="545" r="170" fill="url(#iris)"/>
<circle cx="960" cy="545" r="78" fill="#030102"/>
<ellipse cx="910" cy="495" rx="30" ry="20" fill="#fff" opacity="0.65"/>
<path d="M540 560 Q960 180 1380 560 Q960 300 540 560 Z" fill="#1a100e"/>
<path d="M540 560 Q960 860 1380 560 Q960 760 540 560 Z" fill="#1a100e"/>
{glow(960, 545, 200, RED, 0.18)}'''
scenes["s6b"] = peep_view(eye).replace('</defs>', '<radialGradient id="iris" cx="960" cy="545" r="170" gradientUnits="userSpaceOnUse"><stop offset="0.4" stop-color="#ff3b2f" stop-opacity="0.2"/><stop offset="0.85" stop-color="#7a1410" stop-opacity="0.9"/><stop offset="1" stop-color="#1a0402"/></radialGradient>'
                                                         '<radialGradient id="eyeShade" cx="960" cy="545" r="420" gradientUnits="userSpaceOnUse"><stop offset="0.4" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.75"/></radialGradient></defs>', 1)

# S7 — morning: the super holds the removed peephole, turned the wrong way round
scenes["s7"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#morning)"/>
{paper.replace("#2c2418", "#3a4252")}
<rect x="660" y="0" width="600" height="1000" fill="url(#doorm)"/>
<rect x="636" y="0" width="24" height="1000" fill="#101418"/><rect x="1260" y="0" width="24" height="1000" fill="#101418"/>
<rect x="700" y="420" width="240" height="520" fill="none" stroke="#141a22" stroke-width="8" opacity="0.7"/><rect x="980" y="420" width="240" height="520" fill="none" stroke="#141a22" stroke-width="8" opacity="0.7"/>
<circle cx="960" cy="300" r="16" fill="#000"/>
<circle cx="960" cy="300" r="40" fill="#000" opacity="0.15" filter="url(#blur8)"/>
<rect x="930" y="250" width="70" height="20" fill="#0a0a0c" opacity="0.9" transform="rotate(30 960 260)"/>
<rect x="0" y="1000" width="{W}" height="80" fill="#14181e"/>
<g transform="translate(1000 1000) rotate(-12)"><rect x="-110" y="-12" width="140" height="18" rx="6" fill="#7a1a14"/><rect x="30" y="-6" width="120" height="6" fill="#9aa4b0"/></g>
<g transform="translate(960 640) rotate(-18)">
<rect x="-160" y="-38" width="320" height="76" rx="14" fill="url(#brass)"/>
<rect x="-160" y="-38" width="40" height="76" rx="10" fill="#5e4318"/>
<ellipse cx="160" cy="0" rx="22" ry="40" fill="#c8d4e8"/>
<ellipse cx="160" cy="0" rx="13" ry="26" fill="#3a4a64"/>
<g stroke="#4e3712" stroke-width="3">{"".join(f'<line x1="{x}" y1="-38" x2="{x}" y2="38"/>' for x in range(-100, 140, 18))}</g>
</g>
<g fill="#07090c">
<ellipse cx="820" cy="760" rx="120" ry="90"/>
<rect x="760" y="600" width="66" height="160" rx="30" transform="rotate(-18 790 680)"/>
<rect x="840" y="700" width="200" height="40" rx="20" transform="rotate(-18 940 720)"/>
<rect x="860" y="740" width="180" height="40" rx="20" transform="rotate(-18 950 760)"/>
<rect x="420" y="740" width="420" height="190" rx="80" transform="rotate(10 630 830)"/>
</g>
{glow(1400, 200, 260, "#c8d4f0", 0.12)}
''', BRASS + BIG +
    '<linearGradient id="morning" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3a4558"/><stop offset="1" stop-color="#141a24"/></linearGradient>'
    '<linearGradient id="doorm" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a2c34"/><stop offset="1" stop-color="#181a20"/></linearGradient>')

# S8 — night again: the empty hole in the door, and a red eye looking in
scenes["s8"] = svg(f'''
<rect width="{W}" height="{H}" fill="#060406"/>
{paper.replace("#2c2418", "#1a1014")}
{door_front(720, 110, 480, 890, tape=False, hole=True, peep_r=26)}
<rect x="0" y="0" width="{W}" height="{H}" fill="#000" opacity="0.3"/>
<polygon points="955,377 965,377 1500,1080 420,1080" fill="{RED}" opacity="0.05"/>
<circle cx="960" cy="377" r="9" fill="{RED}"/>
<circle cx="960" cy="377" r="4" fill="#ffd0c0"/>
{glow(960, 377, 60, RED, 0.7)}
{glow(960, 377, 180, RED, 0.18)}
<rect x="0" y="1000" width="{W}" height="80" fill="#0a0507"/>
<path d="M880 1040 l70 -12 l6 16 l-70 12 z" fill="#0a0a0c"/>
''', DOORW.replace("#3a2618", "#1e120c").replace("#22160e", "#120a07") + BRASS + BIG)

for name, s in scenes.items():
    save(name, s)
print("drew", ", ".join(scenes))
