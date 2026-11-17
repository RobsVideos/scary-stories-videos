"""Scenes for The Attic Box. Run inside this folder: python3 scenes.py"""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

_save = save


def save(name, markup):
    for b in ("blur8", "blur30", "blur60"):
        markup = markup.replace(f'<filter id="{b}">', f'<filter id="{b}" x="-200%" y="-200%" width="500%" height="500%">')
    _save(name, markup)


CARD = '''<linearGradient id="card" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8a6a44"/><stop offset="1" stop-color="#4a3420"/></linearGradient>
<linearGradient id="cardD" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#3a2817"/><stop offset="1" stop-color="#5a4128"/></linearGradient>
<linearGradient id="beam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c9d6f2" stop-opacity="0.35"/><stop offset="1" stop-color="#c9d6f2" stop-opacity="0"/></linearGradient>'''


def dust(n, x0, x1, y0, y1, op=0.5):
    return "".join(f'<circle cx="{rnd.randint(x0, x1)}" cy="{rnd.randint(y0, y1)}" r="{rnd.choice([1.5, 2, 2.6])}" '
                   f'fill="#e8e4d8" opacity="{rnd.uniform(0.15, op):.2f}"/>' for _ in range(n))


def attic_room(window_x=960, light="#c9d6f2"):
    """Sloped attic interior: rafters, floorboards, a small round window high in the gable."""
    rafters = "".join(f'<line x1="{960 + k * 130}" y1="80" x2="{960 + k * 420}" y2="760" stroke="#120c08" stroke-width="22"/>'
                      for k in range(-6, 7) if k != 0)
    boards = "".join(f'<line x1="{960 + k * 40}" y1="760" x2="{960 + k * 260}" y2="1080" stroke="#140d09" stroke-width="3"/>' for k in range(-9, 10))
    return f'''
<rect width="{W}" height="{H}" fill="#0c0806"/>
<polygon points="960,60 -400,760 2320,760" fill="url(#atticWall)"/>
{rafters}
<line x1="960" y1="60" x2="-400" y2="760" stroke="#0a0604" stroke-width="40"/>
<line x1="960" y1="60" x2="2320" y2="760" stroke="#0a0604" stroke-width="40"/>
<rect x="0" y="740" width="{W}" height="26" fill="#0a0604"/>
<polygon points="0,766 1920,766 1920,1080 0,1080" fill="#22160e"/>
<g clip-path="url(#floorClip)">{boards}</g>
<circle cx="{window_x}" cy="300" r="78" fill="#0a0604"/>
<circle cx="{window_x}" cy="300" r="62" fill="#1d2640"/>
<circle cx="{window_x}" cy="300" r="62" fill="{light}" opacity="0.55"/>
<line x1="{window_x - 62}" y1="300" x2="{window_x + 62}" y2="300" stroke="#0a0604" stroke-width="7"/>
<line x1="{window_x}" y1="238" x2="{window_x}" y2="362" stroke="#0a0604" stroke-width="7"/>
{glow(window_x, 300, 120, light, 0.25)}
'''


ATTIC_DEFS = CARD + '''<linearGradient id="atticWall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a120c"/><stop offset="1" stop-color="#2b1c12"/></linearGradient>
<clipPath id="floorClip"><rect x="0" y="766" width="1920" height="314"/></clipPath>'''


def box(cx, base, w=380, h=280, flaps="open", tape=None, inner="#050302"):
    """Cardboard box in 3/4 view. flaps: open | closed. tape: None | 'x' | 'split'."""
    x = cx - w / 2; top = base - h; d = 70
    out = [f'<ellipse cx="{cx}" cy="{base + 6}" rx="{w * 0.75}" ry="26" fill="#000" opacity="0.55" filter="url(#blur8)"/>',
           f'<rect x="{x}" y="{top}" width="{w}" height="{h}" fill="url(#card)"/>',
           f'<polygon points="{x + w},{top} {x + w + d},{top - d * 0.6} {x + w + d},{base - d * 0.6} {x + w},{base}" fill="url(#cardD)"/>',
           f'<line x1="{x}" y1="{top + 40}" x2="{x + w}" y2="{top + 40}" stroke="#3a2817" stroke-width="2" opacity="0.6"/>']
    if flaps == "open":
        out += [f'<polygon points="{x},{top} {x + w},{top} {x + w + d},{top - d * 0.6} {x + d},{top - d * 0.6}" fill="{inner}"/>',
                f'<polygon points="{x},{top} {x + d},{top - d * 0.6} {x - 70},{top - 150} {x - 120},{top - 40}" fill="#6e5234"/>',
                f'<polygon points="{x + w},{top} {x + w + d},{top - d * 0.6} {x + w + 170},{top - 120} {x + w + 120},{top + 10}" fill="#5c4329"/>',
                f'<polygon points="{x + d},{top - d * 0.6} {x + w + d},{top - d * 0.6} {x + w + 40},{top - 190} {x + 50},{top - 190}" fill="#4a3420"/>',
                f'<polygon points="{x},{top} {x + w},{top} {x + w - 20},{top + 70} {x + 20},{top + 70}" fill="#7d5f3d"/>']
    else:
        out += [f'<polygon points="{x},{top} {x + w},{top} {x + w + d},{top - d * 0.6} {x + d},{top - d * 0.6}" fill="#7d5f3d"/>',
                f'<line x1="{x + d / 2}" y1="{top - d * 0.3}" x2="{x + w + d / 2}" y2="{top - d * 0.3}" stroke="#3a2817" stroke-width="3"/>']
    if tape == "x":
        out += [f'<polygon points="{x + d / 2 - 10},{top - d * 0.3 - 14} {x + w + d / 2 + 10},{top - d * 0.3 - 14} {x + w + d / 2 + 10},{top - d * 0.3 + 14} {x + d / 2 - 10},{top - d * 0.3 + 14}" fill="#c9b98f" opacity="0.85"/>',
                f'<rect x="{cx - 22}" y="{top}" width="44" height="{h * 0.55}" fill="#c9b98f" opacity="0.85"/>',
                f'<rect x="{x + 40}" y="{top + 10}" width="{w - 80}" height="40" fill="#c9b98f" opacity="0.8" transform="rotate(18 {cx} {top + 90})"/>',
                f'<rect x="{x + 40}" y="{top + 10}" width="{w - 80}" height="40" fill="#c9b98f" opacity="0.8" transform="rotate(-18 {cx} {top + 90})"/>']
    if tape == "split":
        out += [f'<polygon points="{x + 10},{top - 20} {x + w + d},{top - 20} {x + w + d - 6},{top + 4} {x + 14},{top + 4}" fill="#000"/>',
                glow(cx + 30, top - 10, 90, "#c42b22", 0.55),
                f'<path d="M{x + d / 2} {top - d * 0.3} L{cx - 40} {top - d * 0.3} q-10 -50 -50 -70 l-8 22 q30 14 30 48" fill="#c9b98f" opacity="0.9"/>',
                f'<path d="M{x + w + d / 2} {top - d * 0.3} L{cx + 60} {top - d * 0.3} q16 -60 60 -78 l6 24 q-34 12 -36 54" fill="#c9b98f" opacity="0.9"/>',
                f'<path d="M{cx - 40} {top - 18} l-20 -60 l14 4 l12 40 M{cx + 60} {top - 18} l26 -64 l12 8 l-24 52" fill="#c9b98f" opacity="0.9"/>',
                f'<rect x="{cx - 22}" y="{top}" width="44" height="{h * 0.55}" fill="#c9b98f" opacity="0.85"/>',
                f'<path d="M{cx - 22} {top + h * 0.55} l10 -14 l8 14 l10 -16 l8 16 l10 -14 v-0z" fill="#c9b98f"/>']
    return "".join(out)


scenes = {}

# S1 - the house, a lit attic window
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(150, 560)}
{moon(1420, 200, 80)}
<path d="M0 820 C400 790 900 800 1300 810 C1600 818 1800 800 1920 805 L1920 1080 L0 1080Z" fill="#12101e"/>
<g fill="#07060c">
<polygon points="640,830 640,520 960,250 1280,520 1280,830"/>
<polygon points="600,540 960,220 1320,540 1300,556 960,256 620,556"/>
<rect x="1140" y="300" width="50" height="140"/>
<polygon points="560,840 560,700 1360,700 1360,840"/>
<polygon points="530,712 960,640 1390,712"/>
</g>
<polygon points="960,330 900,390 900,440 1020,440 1020,390" fill="#e8a24a"/>
<polygon points="960,330 900,390 900,440 1020,440 1020,390" fill="#ffb54a" filter="url(#blur30)" opacity="0.8"/>
<line x1="960" y1="330" x2="960" y2="440" stroke="#07060c" stroke-width="6"/>
<line x1="900" y1="400" x2="1020" y2="400" stroke="#07060c" stroke-width="6"/>
{lit_window(720, 560, 70, 90, "#3a3550")}{lit_window(1130, 560, 70, 90, "#3a3550")}
<rect x="920" y="740" width="80" height="100" fill="#0b0912"/>
{dead_tree(400, 840, 420)}{dead_tree(1560, 850, 360, s=0.8)}
<path d="M0 900 C500 870 1300 890 1920 880 L1920 1080 L0 1080Z" fill="#0b0a14"/>
{grass(1080, 260, "#06050b", (20, 46))}
{fog(860)}
''', sky("sky1", "#04050d", "#17142f", "#33203a"))

# S2 - attic, open box under moonlight, a note on the lid
scenes["s2"] = svg(attic_room() + f'''
<polygon points="905,330 1015,330 1180,960 740,960" fill="url(#beam)"/>
{box(960, 920)}
<g transform="rotate(-8 790 760)"><rect x="740" y="720" width="110" height="80" fill="#e6dcc0"/>
<g stroke="#4a3a2a" stroke-width="3">{''.join(f'<line x1="752" y1="{y}" x2="{835 - (y % 3) * 6}" y2="{y}"/>' for y in (738, 752, 766, 780))}</g></g>
{dust(70, 760, 1160, 340, 900)}
{fog(960, "#9a8a70", 0.10)}
''', ATTIC_DEFS)

# S3 - inside the box: glasses, watch, keys, ring
glint = lambda x, y, r=20: (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff4d0" opacity="0.6" filter="url(#blur8)"/>'
                            f'<path d="M{x - r} {y} L{x + r} {y} M{x} {y - r} L{x} {y + r}" stroke="#fff8e6" stroke-width="2"/>')
scenes["s3"] = svg(f'''
<rect width="{W}" height="{H}" fill="#1a120b"/>
<polygon points="420,0 1500,0 1400,1080 520,1080" fill="#5a4128"/>
<polygon points="520,80 1400,80 1330,1000 590,1000" fill="#0a0604"/>
<polygon points="520,80 590,1000 640,1000 580,80" fill="#2a1d12"/>
<polygon points="1400,80 1330,1000 1290,1000 1350,80" fill="#1e140c"/>
{glow(960, 520, 300, "#c9d6f2", 0.12)}
<g fill="none" stroke="#b8b0a0" stroke-width="7">
<circle cx="760" cy="330" r="62"/><circle cx="910" cy="330" r="62"/><path d="M822 325 q14 -16 26 0"/>
<path d="M698 320 l-80 -40"/><path d="M972 320 l70 -50"/></g>
<circle cx="760" cy="330" r="56" fill="#9fb4e8" opacity="0.12"/><circle cx="910" cy="330" r="56" fill="#9fb4e8" opacity="0.12"/>
<g transform="translate(1150 460) rotate(20)">
<rect x="-34" y="-170" width="68" height="340" rx="14" fill="#3a2a1e"/>
<circle r="70" fill="#a7853f"/><circle r="58" fill="#e6dcc0"/>
<line x1="0" y1="0" x2="0" y2="-40" stroke="#1a100d" stroke-width="5"/><line x1="0" y1="0" x2="28" y2="10" stroke="#1a100d" stroke-width="4"/></g>
<g transform="translate(780 700) rotate(-25)" fill="#8f8a80">
<circle r="46" fill="none" stroke="#8f8a80" stroke-width="10"/>
<rect x="40" y="-14" width="150" height="28" rx="6"/><rect x="160" y="14" width="14" height="22"/><rect x="130" y="14" width="12" height="16"/>
<rect x="-30" y="40" width="22" height="130" rx="4" transform="rotate(30)"/></g>
<circle cx="1050" cy="780" r="34" fill="none" stroke="#e3c37a" stroke-width="12"/>
{glint(1072, 752, 26)}{glint(730, 300)}{glint(1180, 410, 16)}
{dust(40, 600, 1320, 100, 980, 0.35)}
''')

# S4 - bedroom, the attic hatch above the bed
scenes["s4"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0b0e18"/>
<polygon points="0,0 1920,0 1600,220 320,220" fill="#080a12"/>
<rect x="820" y="70" width="280" height="110" fill="#05060b" stroke="#1c2133" stroke-width="10"/>
<rect x="820" y="174" width="280" height="6" fill="#ffb54a" opacity="0.7"/>
{glow(960, 180, 60, "#ffb54a", 0.25)}
<line x1="1060" y1="180" x2="1060" y2="230" stroke="#2a2f45" stroke-width="3"/><circle cx="1060" cy="236" r="7" fill="#2a2f45"/>
<rect x="320" y="220" width="1280" height="560" fill="#121626"/>
{lit_window(1380, 360, 140, 200, "#2c3a62")}
<polygon points="1380,560 1520,560 1640,1080 1260,1080" fill="#9fb4e8" opacity="0.05"/>
<rect x="0" y="780" width="{W}" height="300" fill="#0d0f1a"/>
<rect x="560" y="430" width="800" height="190" rx="20" fill="#191428"/>
<rect x="520" y="620" width="880" height="200" rx="16" fill="#2a2440"/>
<ellipse cx="720" cy="575" rx="110" ry="50" fill="#4a4566"/><ellipse cx="1060" cy="575" rx="110" ry="50" fill="#4a4566"/>
<path d="M660 640 C660 560 780 560 780 640Z" fill="#0a0812"/><path d="M1000 640 C1000 555 1125 555 1125 640 C1110 600 1060 600 1040 640Z" fill="#0a0812"/>
<path d="M560 640 C640 600 760 600 840 640 C920 600 1040 600 1120 640 C1200 610 1300 610 1380 640 L1380 760 L560 760Z" fill="#3a3358"/>
<rect x="520" y="810" width="20" height="60" fill="#0a0812"/><rect x="1380" y="810" width="20" height="60" fill="#0a0812"/>
{fog(900, "#6b6f90", 0.08)}
''')

# S5 - the box taped shut
scenes["s5"] = svg(attic_room() + f'''
<polygon points="905,330 1015,330 1180,960 740,960" fill="url(#beam)"/>
{box(960, 920, flaps="closed", tape="x")}
<g transform="translate(1260 900) rotate(-10)"><circle r="44" fill="#c9b98f"/><circle r="20" fill="#5a4128"/>
<path d="M0 44 l120 30 l0 20 l-120 -24z" fill="#c9b98f"/></g>
{dust(50, 760, 1160, 340, 900, 0.35)}
{fog(960, "#9a8a70", 0.08)}
''', ATTIC_DEFS)

# S6 - pull-down ladder, warm light above; then the split tape
scenes["s6"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0a0810"/>
<rect x="0" y="0" width="{W}" height="240" fill="#07060a"/>
<rect x="760" y="120" width="400" height="130" fill="#d07a3a"/>
<rect x="760" y="120" width="400" height="130" fill="#ff9a4a" filter="url(#blur30)" opacity="0.6"/>
<rect x="760" y="120" width="400" height="130" fill="none" stroke="#050407" stroke-width="16"/>
{glow(960, 180, 220, "#ff9a4a", 0.25)}
<polygon points="880,250 1040,250 1180,1000 740,1000" fill="#ff9a4a" opacity="0.06"/>
<g stroke="#1a120c" stroke-width="26" stroke-linecap="round">
<line x1="860" y1="250" x2="740" y2="1010"/><line x1="1060" y1="250" x2="1180" y2="1010"/></g>
<g stroke="#2a1d12" stroke-width="18">{''.join(f'<line x1="{860 - (y - 250) * 120 / 760:.0f}" y1="{y}" x2="{1060 + (y - 250) * 120 / 760:.0f}" y2="{y}"/>' for y in range(340, 1000, 110))}</g>
<rect x="0" y="1000" width="{W}" height="80" fill="#060509"/>
<g fill="#05040a"><rect x="180" y="300" width="20" height="700"/><rect x="1720" y="300" width="20" height="700"/></g>
{figure(1520, 1000, 330, "#030204")}
''')

scenes["s6b"] = svg(attic_room(light="#d06a50") + f'''
{box(960, 920, flaps="closed", tape="split")}
{dust(50, 760, 1160, 340, 900, 0.3)}
{fog(960, "#7a3a30", 0.10)}
''', ATTIC_DEFS)

# S7 - the box is full: shoes, coat, photos with faces scratched out
def photo(x, y, rot, s=1.0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
            f'<rect x="-90" y="-110" width="180" height="220" fill="#e6dcc0"/><rect x="-74" y="-94" width="148" height="150" fill="#4a5466"/>'
            f'<rect x="-74" y="20" width="148" height="36" fill="#3a4250"/>'
            f'<path d="M-30 56 L-30 0 Q0 -16 30 0 L30 56Z" fill="#1a1e28"/><circle cx="0" cy="-30" r="26" fill="#c8b8a0"/>'
            f'<g stroke="#120c08" stroke-width="5" stroke-linecap="round"><path d="M-26 -52 l52 40 M-24 -10 l48 -38 M-30 -36 l60 6 M-14 -56 l24 50"/></g>'
            f'</g>')

scenes["s7"] = svg(attic_room() + f'''
<polygon points="905,330 1015,330 1180,960 740,960" fill="url(#beam)"/>
{box(960, 940, w=420, h=250, inner="#0a0604")}
<path d="M770 700 C760 560 800 470 880 450 C980 430 1040 470 1100 520 L1180 700Z" fill="#2c3248"/>
<path d="M860 460 L940 600 L1000 470" fill="none" stroke="#1a1e2c" stroke-width="8"/>
<path d="M1100 520 C1180 560 1240 620 1250 700" stroke="#2c3248" stroke-width="60" fill="none" stroke-linecap="round"/>
<path d="M790 690 c-10 -50 30 -70 80 -60 l90 20 c20 10 10 40 -10 44 l-150 10z" fill="#141018"/>
<path d="M980 700 c0 -40 40 -56 80 -46 l100 26 c20 8 14 34 -8 38 l-160 6z" fill="#1c1622"/>
{photo(860, 600, -14)}{photo(1060, 590, 10)}{photo(960, 640, -2, 1.05)}
{photo(720, 900, -30, 0.7)}{photo(1250, 910, 24, 0.7)}
{dust(40, 760, 1160, 340, 900, 0.3)}
''', ATTIC_DEFS)

# S8 - from the dark hall: the kitchen, my wife, and someone wearing me
scenes["s8"] = svg(f'''
<rect width="{W}" height="{H}" fill="#07060a"/>
<rect x="640" y="160" width="640" height="840" fill="url(#kit)"/>
{glow(960, 300, 200, "#ffcf7a", 0.45)}
<path d="M900 160 L900 220 M870 220 L1020 220 L990 260 L930 260Z" stroke="#2a1a0c" stroke-width="5" fill="#2a1a0c"/>
<ellipse cx="960" cy="262" rx="30" ry="10" fill="#fff0c0"/>
<rect x="640" y="160" width="640" height="840" fill="none" stroke="#120c08" stroke-width="40"/>
<rect x="700" y="700" width="520" height="30" fill="#3a2414"/>
<rect x="720" y="730" width="18" height="270" fill="#2a1a0e"/><rect x="1180" y="730" width="18" height="270" fill="#2a1a0e"/>
<g fill="#0b0708">
<ellipse cx="820" cy="470" rx="46" ry="56"/><path d="M780 440 C760 520 770 600 790 640 L780 560Z"/>
<path d="M750 700 L760 560 C770 520 870 520 880 560 L890 700Z"/>
<ellipse cx="1110" cy="450" rx="48" ry="58"/>
<path d="M1040 700 L1050 540 C1060 500 1160 500 1170 540 L1180 700Z"/>
</g>
<path d="M1080 470 q30 18 60 0" stroke="#f2e8d8" stroke-width="5" fill="none"/>
<path d="M1077 473 q33 24 66 -3" stroke="#f2e8d8" stroke-width="3" fill="none" opacity="0.8"/>
{eyes(1110, 438, 34, 5, "#f2e8d8")}
<rect x="900" y="660" width="60" height="40" rx="6" fill="#d8ccb0"/><rect x="1000" y="664" width="50" height="36" rx="6" fill="#d8ccb0"/>
<polygon points="640,1000 1280,1000 1500,1080 420,1080" fill="#ffcf7a" opacity="0.10"/>
<rect x="0" y="0" width="640" height="{H}" fill="#06050a"/><rect x="1280" y="0" width="640" height="{H}" fill="#06050a"/>
<g stroke="#0e0c14" stroke-width="2">{''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}"/>' for x in range(40, 640, 80))}</g>
''', '''<linearGradient id="kit" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7a4a22"/><stop offset="1" stop-color="#3a2212"/></linearGradient>''')

# S9 - still up here; the box is open, and something in it says there's room
scenes["s9"] = svg(attic_room(light="#8090c0") + f'''
<polygon points="905,330 1015,330 1180,960 740,960" fill="url(#beam)" opacity="0.6"/>
{box(1010, 940, w=440, h=300, inner="#000")}
{glow(1070, 620, 130, "#000", 0.8)}
{eyes(1080, 616, 40, 6)}
<g fill="#050304">
<ellipse cx="660" cy="720" rx="44" ry="52"/>
<path d="M590 950 C580 860 590 790 640 770 C700 750 740 790 750 860 L770 950Z"/>
<path d="M620 950 L560 950 L570 900 Z"/>
</g>
<path d="M740 860 C780 850 800 830 810 800" stroke="#050304" stroke-width="22" stroke-linecap="round" fill="none"/>
{dust(40, 760, 1160, 340, 900, 0.25)}
{fog(980, "#6070a0", 0.10)}
''', ATTIC_DEFS)

for name, s in scenes.items():
    save(name, s)
print("drew", ", ".join(scenes))
