"""Scenes for The Trail Camera. Run inside this folder: python3 scenes.py"""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

_save = save


def save(name, markup):
    for b in ("blur8", "blur30", "blur60"):
        markup = markup.replace(f'<filter id="{b}">', f'<filter id="{b}" x="-200%" y="-200%" width="500%" height="500%">')
    _save(name, markup)


DEFS = (sky("night", "#04050c", "#141a30", "#2a2a40") +
        sky("ir", "#141a17", "#2c3530", "#3e4842") +
        '<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="4"/>'
        '<feColorMatrix values="0 0 0 0 0.8  0 0 0 0 0.9  0 0 0 0 0.85  0 0 0 0.16 0"/></filter>'
        '<radialGradient id="flash" cx="0.5" cy="0.55" r="0.6"><stop offset="0" stop-color="#d7e3dc" stop-opacity="0.22"/>'
        '<stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>'
        '<linearGradient id="wood" x1="0" x2="1"><stop offset="0" stop-color="#1a120c"/><stop offset="1" stop-color="#2b1d13"/></linearGradient>')

STAMP = "CAM 01   11-17   03:12 AM   41°F"


def oak(x, base, h=620, color="#07080e"):
    """Big oak: thick trunk, heavy branches and a dark leafy crown."""
    t = base - h
    crown = "".join(f'<circle cx="{x + rnd.randint(-330, 330)}" cy="{t + rnd.randint(-60, 200)}" r="{rnd.randint(70, 140)}"/>' for _ in range(28))
    return (f'<g fill="{color}">{crown}'
            f'<path d="M{x - 55} {base} C{x - 40} {base - 200} {x - 50} {base - 360} {x - 20} {t + 150} L{x + 30} {t + 150} '
            f'C{x + 50} {base - 360} {x + 45} {base - 200} {x + 65} {base} Z"/>'
            f'<path d="M{x - 30} {base - 330} C{x - 140} {base - 400} {x - 220} {base - 430} {x - 300} {base - 520}" stroke="{color}" stroke-width="34" fill="none"/>'
            f'<path d="M{x + 30} {base - 380} C{x + 140} {base - 440} {x + 230} {base - 470} {x + 310} {base - 560}" stroke="{color}" stroke-width="30" fill="none"/>'
            f'<path d="M{x - 60} {base} q-50 10 -90 8 M{x + 60} {base} q50 10 90 6" stroke="{color}" stroke-width="18" fill="none"/></g>')


def trailcam(x, y, s=1.0, led=True):
    """Camo trail camera strapped to a trunk, lens and red LED."""
    w, h = 70 * s, 100 * s
    out = (f'<rect x="{x - w / 2 - 22 * s}" y="{y + h * .35}" width="{w + 44 * s}" height="{10 * s}" fill="#151510"/>'
           f'<rect x="{x - w / 2}" y="{y}" width="{w}" height="{h}" rx="{10 * s}" fill="#2a3020"/>'
           f'<path d="M{x - w / 2 + 6 * s} {y + 20 * s} q{20 * s} {-10 * s} {30 * s} {8 * s} q{10 * s} {14 * s} {28 * s} {4 * s}" stroke="#1a1e12" stroke-width="{9 * s}" fill="none"/>'
           f'<circle cx="{x}" cy="{y + h * .58}" r="{15 * s}" fill="#08090a" stroke="#3c4430" stroke-width="{4 * s}"/>'
           f'<circle cx="{x - 4 * s}" cy="{y + h * .55}" r="{4 * s}" fill="#6a7a8a" opacity="0.7"/>'
           f'<rect x="{x - 24 * s}" y="{y + 10 * s}" width="{48 * s}" height="{14 * s}" rx="{3 * s}" fill="#14160f"/>')
    if led:
        out += (f'<circle cx="{x + 20 * s}" cy="{y + h * .85}" r="{5 * s}" fill="#ff3b2f"/>' + glow(x + 20 * s, y + h * .85, 26 * s, "#ff3b2f", 0.8))
    return out


def house(x, base, color="#08070d", lit=True, w=520):
    out = (f'<g fill="{color}"><rect x="{x - w / 2}" y="{base - 300}" width="{w}" height="300"/>'
           f'<polygon points="{x - w / 2 - 30},{base - 295} {x},{base - 470} {x + w / 2 + 30},{base - 295}"/>'
           f'<rect x="{x + w / 4}" y="{base - 450}" width="36" height="110"/></g>')
    if lit:
        out += lit_window(x - w / 4 - 40, base - 240, 80, 100, "#ffb54a")
        out += lit_window(x + 60, base - 240, 80, 100, "#2a2a3e", color)
    out += f'<rect x="{x - 30}" y="{base - 150}" width="60" height="150" fill="#14121c"/>'
    return out


def person(cx, base, h=560, body="#c9d4cc", shade="#7d8a82", eye="#ffffff", smile=0, wave=False):
    """A pale IR-lit person in pajamas, barefoot, arms at sides (or one raised to wave)."""
    hr = h * 0.075
    hy = base - h + hr
    sw = h * 0.13
    torso_top = hy + hr + h * 0.03
    hip = base - h * 0.47
    out = f'<g>'
    # legs (pajama pants), bare feet
    out += (f'<path d="M{cx - sw * .9} {hip} L{cx - sw * .75} {base - 18} L{cx - sw * .05} {base - 18} L{cx} {hip + 40} '
            f'L{cx + sw * .05} {base - 18} L{cx + sw * .75} {base - 18} L{cx + sw * .9} {hip} Z" fill="{shade}"/>')
    out += (f'<ellipse cx="{cx - sw * .45}" cy="{base - 8}" rx="{sw * .42}" ry="12" fill="{body}"/>'
            f'<ellipse cx="{cx + sw * .45}" cy="{base - 8}" rx="{sw * .42}" ry="12" fill="{body}"/>')
    # torso (pajama shirt)
    out += (f'<path d="M{cx - sw} {torso_top + 20} Q{cx} {torso_top - 10} {cx + sw} {torso_top + 20} L{cx + sw * .95} {hip + 10} '
            f'L{cx - sw * .95} {hip + 10} Z" fill="{body}"/>')
    out += "".join(f'<circle cx="{cx}" cy="{torso_top + 50 + k * 45}" r="5" fill="{shade}"/>' for k in range(4))
    # arms
    arm = f'stroke="{body}" stroke-width="{sw * .42}" stroke-linecap="round" fill="none"'
    out += f'<path d="M{cx - sw} {torso_top + 30} Q{cx - sw * 1.3} {hip - 40} {cx - sw * 1.15} {hip + 50}" {arm}/>'
    if wave:
        out += f'<path d="M{cx + sw} {torso_top + 30} Q{cx + sw * 1.9} {torso_top - 10} {cx + sw * 1.7} {torso_top - h * .2}" {arm}/>'
        out += f'<ellipse cx="{cx + sw * 1.7}" cy="{torso_top - h * .24}" rx="{sw * .28}" ry="{sw * .38}" fill="{body}"/>'
    else:
        out += f'<path d="M{cx + sw} {torso_top + 30} Q{cx + sw * 1.3} {hip - 40} {cx + sw * 1.15} {hip + 50}" {arm}/>'
    # neck, head, hair
    out += f'<rect x="{cx - hr * .35}" y="{hy + hr * .7}" width="{hr * .7}" height="{hr * .6}" fill="{body}"/>'
    out += f'<ellipse cx="{cx}" cy="{hy}" rx="{hr * .85}" ry="{hr}" fill="{body}"/>'
    out += f'<path d="M{cx - hr * .9} {hy - hr * .1} Q{cx - hr * .7} {hy - hr * 1.25} {cx} {hy - hr * 1.05} Q{cx + hr * .8} {hy - hr * 1.2} {cx + hr * .9} {hy - hr * .1} Q{cx} {hy - hr * .7} {cx - hr * .9} {hy - hr * .1}Z" fill="{shade}"/>'
    # eyes (IR eyeshine) and mouth
    out += eyes(cx, hy - hr * .05, gap=hr * .7, r=hr * .12, color=eye)
    if smile:
        out += f'<path d="M{cx - hr * .45 * smile} {hy + hr * .4} Q{cx} {hy + hr * (.4 + .45 * smile)} {cx + hr * .45 * smile} {hy + hr * .4}" stroke="#1a201c" stroke-width="{hr * .1}" fill="none" stroke-linecap="round"/>'
    else:
        out += f'<line x1="{cx - hr * .25}" y1="{hy + hr * .5}" x2="{cx + hr * .25}" y2="{hy + hr * .5}" stroke="#3a443e" stroke-width="{hr * .07}"/>'
    return out + '</g>'


def ir_frame(body, stamp=STAMP):
    """Wrap content as a grainy grey-green night-vision trail-cam photo with a timestamp bar."""
    return (f'<rect width="{W}" height="{H}" fill="url(#ir)"/>{body}'
            f'<rect width="{W}" height="{H}" fill="url(#flash)"/>'
            f'<rect width="{W}" height="{H}" filter="url(#grain)"/>'
            f'<rect x="0" y="980" width="{W}" height="100" fill="#000" opacity="0.75"/>'
            f'<text x="960" y="1045" text-anchor="middle" font-family="{MONO}" font-size="40" fill="#e8efe8" letter-spacing="2">{stamp}</text>')


def ir_grass(y0, n):
    return grass(y0, n, "#2c3631", (18, 46)) + grass(y0 - 40, n // 2, "#3a4640", (12, 30))


def phone_hand(cx, cy, screen, w=330, h=600):
    """A hand holding a glowing phone; `screen` is SVG drawn in a 1920x1080 space, scaled into the screen."""
    sx, sy = cx - w / 2 + 16, cy - h / 2 + 40
    sw, sh = w - 32, h - 80
    scale = sh / 1080
    off = sx + sw / 2 - 960 * scale
    return (glow(cx, cy, 340, "#9fb8c8", 0.35) +
            f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="40" fill="#0b0b0f" stroke="#2a2a33" stroke-width="5"/>'
            f'<clipPath id="scr{cx}"><rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="10"/></clipPath>'
            f'<g clip-path="url(#scr{cx})"><rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" fill="#3d4842"/>'
            f'<g transform="translate({off} {sy}) scale({scale})">{screen}</g></g>'
            f'<path d="M{cx - w / 2 - 30} {cy + h / 2 - 160} q-20 160 60 260 l200 60 q120 -10 140 -120 l10 -200 '
            f'q-30 60 -80 70 l-210 0 q-70 -10 -120 -70 z" fill="#2a1e1a"/>'
            f'<path d="M{cx - w / 2 - 6} {cy + 40} q-28 60 -10 140" stroke="#2a1e1a" stroke-width="36" fill="none" stroke-linecap="round"/>')


# S1 — backyard, oak tree with the trail camera, dug-up garden
dug = "".join(f'<ellipse cx="{x}" cy="{y}" rx="{rnd.randint(30, 60)}" ry="{rnd.randint(10, 18)}" fill="#1c140e"/>'
              f'<path d="M{x - 40} {y - 6} q40 -30 80 0" fill="#2a1c12"/>' for x, y in ((620, 900), (760, 940), (900, 880), (1180, 930), (1320, 895), (980, 980)))
rows = "".join(f'<path d="M{540 + k * 60} 1080 L{760 + k * 24} 820" stroke="#140f0a" stroke-width="10"/>' for k in range(12))
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>{stars(140, 520)}{moon(1240, 200, 70)}
<path d="M0 760 C500 730 1300 740 1920 750 L1920 1080 L0 1080Z" fill="#12121c"/>
{house(560, 770)}
<g fill="#0a0a12">{''.join(f'<rect x="{x}" y="700" width="12" height="80"/>' for x in range(0, 1920, 46))}<rect x="0" y="716" width="1920" height="8"/></g>
{fog(760, op=0.12)}
{oak(1110, 860)}
{trailcam(1110, 600, 1.0)}
<path d="M0 820 C600 800 1300 810 1920 815 L1920 1080 L0 1080Z" fill="#191a14"/>
{rows}{dug}
{grass(1080, 260, "#0b0c08", (16, 44))}
{fog(900, op=0.08, ry=80)}
''', DEFS))

# S2 — the neighbour on his porch
rail = "".join(f'<rect x="{x}" y="720" width="12" height="130" fill="#0a0806"/>' for x in range(520, 1420, 50))
save("s2", svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>{stars(80, 300, 0.5)}
<rect x="380" y="260" width="1160" height="700" fill="#17110d"/>
{''.join(f'<line x1="380" y1="{y}" x2="1540" y2="{y}" stroke="#0e0a07" stroke-width="4"/>' for y in range(290, 960, 38))}
<polygon points="300,280 960,150 1620,280" fill="#0b0806"/>
<rect x="300" y="270" width="1320" height="30" fill="#0b0806"/>
<rect x="400" y="300" width="34" height="660" fill="#0d0907"/><rect x="1480" y="300" width="34" height="660" fill="#0d0907"/>
{lit_window(1180, 420, 170, 220, "#ffae4a")}
<rect x="610" y="380" width="170" height="440" fill="#0c0806"/>
<circle cx="830" cy="350" r="18" fill="#ffd38a"/>{glow(830, 350, 160, "#ffb54a", 0.45)}
<polygon points="830,350 600,960 1140,960" fill="#ffb54a" opacity="0.06"/>
<rect x="0" y="850" width="{W}" height="230" fill="url(#wood)"/>
{rail}<rect x="500" y="710" width="920" height="16" fill="#0a0806"/>
<g fill="#050405">
<path d="M920 860 l-20 -250 l170 0 l-10 250 z" opacity="0.7"/>
<ellipse cx="985" cy="560" rx="46" ry="56"/>
<path d="M930 605 q55 -20 110 0 l25 160 l-160 0 z"/>
<rect x="900" y="740" width="200" height="22" rx="8"/>
<path d="M915 760 l-25 110 M1085 760 l25 110" stroke="#050405" stroke-width="12"/>
<path d="M880 880 q120 30 240 0" stroke="#050405" stroke-width="10" fill="none"/>
<path d="M1040 640 q60 60 30 120" stroke="#050405" stroke-width="26" fill="none" stroke-linecap="round"/>
<path d="M940 520 q45 -40 90 0 l10 -10 l-110 0z"/>
<rect x="925" y="505" width="120" height="14" rx="6"/>
</g>
<circle cx="1072" cy="770" r="8" fill="#ff6a2a"/>{glow(1072, 770, 22, "#ff6a2a", 0.8)}
<path d="M1072 760 q-10 -40 10 -80 q20 -40 0 -80" stroke="#8890a0" stroke-width="3" fill="none" opacity="0.35"/>
{fog(980, op=0.1)}
''', DEFS))

# S3 — phone in bed showing a deer photo
deer = (f'<g fill="#a9b8ae"><ellipse cx="960" cy="560" rx="220" ry="110"/><path d="M1140 520 l90 -150 l60 10 l-40 170 z"/>'
        f'<ellipse cx="1260" cy="370" rx="70" ry="42"/><path d="M1240 340 l-30 -120 M1260 330 l20 -130 M1222 290 l-40 -30 M1270 260 l40 -30" stroke="#a9b8ae" stroke-width="12"/>'
        f'<path d="M800 600 l-20 240 M860 620 l0 230 M1060 620 l10 230 M1110 600 l30 240" stroke="#a9b8ae" stroke-width="28" stroke-linecap="round"/></g>'
        + eyes(1270, 362, gap=50, r=14, color="#ffffff"))
s3_screen = ir_frame(dead_tree(400, 900, 500, "#2a332e") + dead_tree(1600, 900, 560, "#2a332e") + ir_grass(1000, 200) + deer)
save("s3", svg(f'''
<rect width="{W}" height="{H}" fill="#07080c"/>
<path d="M0 820 C400 760 800 790 1100 800 C1500 810 1700 760 1920 780 L1920 1080 L0 1080Z" fill="#141826"/>
<path d="M0 900 C500 860 1200 880 1920 870" stroke="#1d2233" stroke-width="20" fill="none"/>
<rect x="420" y="160" width="300" height="200" fill="#0b0e18"/>{lit_window(440, 180, 260, 160, "#2c3550", "#07080c")}
{phone_hand(960, 540, s3_screen)}
''', DEFS))

# S4 — the photo: me, barefoot, staring into the lens
save("s4", svg(ir_frame(f'''
<path d="M0 640 C500 620 1400 630 1920 640 L1920 1080 L0 1080Z" fill="#28302c"/>
{house(1500, 620, "#2a332e", lit=False)}
<g fill="#2e3833">{''.join(f'<rect x="{x}" y="560" width="12" height="80"/>' for x in range(0, 1920, 46))}<rect x="0" y="576" width="1920" height="8"/></g>
{person(960, 960, 640, smile=0)}
{ir_grass(1000, 260)}
'''), DEFS))

# S5 — back door locked from the inside
save("s5", svg(f'''
<rect width="{W}" height="{H}" fill="#0a0a10"/>
<rect x="600" y="100" width="720" height="980" fill="#1b1714"/>
<rect x="660" y="140" width="600" height="940" fill="#2a211a"/>
<rect x="720" y="190" width="480" height="300" fill="#0d1222"/>
<rect x="720" y="190" width="480" height="300" fill="#7f97c8" opacity="0.18"/>
<clipPath id="dw"><rect x="720" y="190" width="480" height="300"/></clipPath><g clip-path="url(#dw)">{oak(1080, 560, 300, "#06070c")}</g>
<line x1="960" y1="190" x2="960" y2="490" stroke="#2a211a" stroke-width="12"/><line x1="720" y1="340" x2="1200" y2="340" stroke="#2a211a" stroke-width="12"/>
<rect x="730" y="560" width="200" height="440" fill="none" stroke="#1e1712" stroke-width="8"/>
<rect x="990" y="560" width="200" height="440" fill="none" stroke="#1e1712" stroke-width="8"/>
<polygon points="720,490 1200,490 1360,1080 560,1080" fill="#9fb4e8" opacity="0.05"/>
<rect x="1150" y="600" width="80" height="60" rx="8" fill="#5a4a2e"/><rect x="1172" y="620" width="56" height="18" rx="9" fill="#b89a5a"/>
<rect x="1240" y="610" width="60" height="44" fill="#3a3024"/>
<circle cx="1190" cy="760" r="30" fill="#b89a5a"/><circle cx="1190" cy="760" r="30" fill="none" stroke="#5a4a2e" stroke-width="6"/>
<path d="M1220 500 q-40 40 -20 80 q15 30 -10 60" stroke="#a88c50" stroke-width="7" fill="none" stroke-dasharray="14 6"/>
<rect x="1205" y="480" width="40" height="22" fill="#5a4a2e"/>
{glow(1190, 700, 120, "#d9b46a", 0.15)}
''', DEFS))

# S6 — closer: me, smiling
save("s6", svg(ir_frame(f'''
<path d="M0 700 C500 680 1400 690 1920 700 L1920 1080 L0 1080Z" fill="#28302c"/>
{dead_tree(500, 720, 400, "#2a332e")}
<g transform="translate(960 1760) scale(2.4) translate(-960 -960)">{person(960, 960, 640, smile=1.6)}</g>
'''), DEFS))

# S7 — sitting up in bed in the dark with the phone
save("s7", svg(f'''
<rect width="{W}" height="{H}" fill="#06070b"/>
<rect x="560" y="140" width="380" height="460" fill="#0b0d18"/>
<rect x="580" y="160" width="340" height="420" fill="url(#night)"/>{moon(820, 230, 26)}
{oak(760, 640, 300, "#05060a")}
<circle cx="770" cy="470" r="6" fill="#ff3b2f"/>{glow(770, 470, 22, "#ff3b2f", 0.9)}
<line x1="750" y1="160" x2="750" y2="580" stroke="#0b0d18" stroke-width="14"/><line x1="580" y1="370" x2="920" y2="370" stroke="#0b0d18" stroke-width="14"/>
<polygon points="580,580 920,580 1020,1080 420,1080" fill="#7f97c8" opacity="0.05"/>
<rect x="1100" y="380" width="380" height="320" rx="20" fill="#0d0e14"/>
<path d="M500 760 C700 700 1300 700 1600 740 L1700 1080 L400 1080Z" fill="#1a1d2c"/>
<path d="M560 820 C800 780 1100 790 1400 800" stroke="#24283a" stroke-width="16" fill="none"/>
<g fill="#040406">
<ellipse cx="1230" cy="470" rx="62" ry="74"/>
<path d="M1150 540 q80 -30 160 0 l40 260 l-240 0 z"/>
<path d="M1170 600 q-60 80 -20 160 q40 30 90 -10" stroke="#040406" stroke-width="40" fill="none" stroke-linecap="round"/>
</g>
<rect x="1110" y="690" width="60" height="100" rx="10" fill="#cfe0ea"/>{glow(1140, 700, 120, "#9fc0d8", 0.6)}
<path d="M1180 470 q40 -10 70 30" stroke="#9fc0d8" stroke-width="10" fill="none" opacity="0.5"/>
<ellipse cx="1210" cy="500" rx="40" ry="50" fill="#9fc0d8" opacity="0.18" filter="url(#blur8)"/>
''', DEFS))

# S8 — the photo is of MY window, taken from the tree
s8 = f'''
<rect x="300" y="160" width="1320" height="900" fill="#36423c"/>
{''.join(f'<line x1="300" y1="{y}" x2="1620" y2="{y}" stroke="#2c3631" stroke-width="5"/>' for y in range(190, 1060, 44))}
<polygon points="200,190 960,0 1720,190" fill="#26302b"/>
<rect x="600" y="300" width="720" height="560" fill="#1a201d"/>
<rect x="630" y="330" width="660" height="500" fill="#8e9c94"/>
<rect x="630" y="330" width="660" height="500" fill="#c6d4cc" opacity="0.25"/>
<rect x="720" y="620" width="520" height="210" fill="#59665f"/>
<rect x="1040" y="500" width="200" height="140" rx="16" fill="#6a776f"/>
<g fill="#151a17">
<ellipse cx="900" cy="500" rx="46" ry="56"/>
<path d="M840 550 q60 -24 120 0 l30 200 l-180 0 z"/>
<path d="M850 600 q-40 70 -10 130 q30 20 70 -10" stroke="#151a17" stroke-width="30" fill="none" stroke-linecap="round"/>
</g>
<rect x="866" y="690" width="40" height="66" rx="6" fill="#ffffff"/>{glow(886, 700, 70, "#ffffff", 0.8)}
<rect x="930" y="330" width="16" height="500" fill="#1a201d"/><rect x="630" y="570" width="660" height="16" fill="#1a201d"/>
<path d="M0 1080 L0 0 L140 0 Q90 400 220 1080Z" fill="#141a17"/>
<path d="M1920 0 L1780 0 Q1840 300 1700 520 Q1800 600 1920 560Z" fill="#141a17"/>
'''
save("s8", svg(ir_frame(s8), DEFS))

# S9 — out the window: the camera's red light, and me beside it, waving
save("s9", svg(f'''
<rect width="{W}" height="{H}" fill="#050508"/>
<rect x="520" y="80" width="880" height="860" fill="#0e101a"/>
<g><clipPath id="win"><rect x="560" y="120" width="800" height="780"/></clipPath>
<g clip-path="url(#win)">
<rect width="{W}" height="{H}" fill="url(#night)"/>{stars(90, 420)}{moon(1240, 220, 46)}
<path d="M0 720 C500 700 1400 710 1920 720 L1920 1080 L0 1080Z" fill="#141620"/>
{fog(740, op=0.14)}
{oak(840, 860, 520)}
{trailcam(840, 640, 0.8)}
<g opacity="0.95">{person(1090, 870, 360, body="#b9c2c8", shade="#5f6870", eye="#ff3b2f", smile=1.6, wave=True)}</g>
{glow(1080, 760, 160, "#c9d6f2", 0.12)}
{grass(900, 220, "#0a0b10", (14, 34))}
{fog(880, op=0.1, ry=70)}
</g></g>
<rect x="944" y="120" width="32" height="780" fill="#0e101a"/><rect x="560" y="490" width="800" height="28" fill="#0e101a"/>
<rect x="480" y="930" width="960" height="40" fill="#14121a"/>
<polygon points="560,940 1360,940 1500,1080 420,1080" fill="#7f97c8" opacity="0.05"/>
''', DEFS))
