"""Scenes for 'The Dusk Count' — a lake, a lifeguard chair, and one swimmer too many."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

HZ = 560  # lake horizon
_save = save


def save(name, markup):
    """Widen the blur filter regions so glows fade out softly instead of showing square edges."""
    for n in ("blur8", "blur30", "blur60"):
        markup = markup.replace(f'<filter id="{n}">', f'<filter id="{n}" x="-150%" y="-150%" width="400%" height="400%">')
    _save(name, markup)


def pines(y, n, hmin, hmax, color, x0=-40, x1=1960):
    out = []
    for _ in range(n):
        x = rnd.randint(x0, x1); h = rnd.randint(hmin, hmax); w = h * rnd.uniform(.28, .38)
        out.append(f'<polygon points="{x},{y - h} {x - w / 2:.0f},{y} {x + w / 2:.0f},{y}" fill="{color}"/>')
    return "".join(out)


def ripples(y0, y1, n, color, op=(0.15, 0.5), xr=(0, 1920)):
    out = []
    for _ in range(n):
        y = rnd.randint(y0, y1); x = rnd.randint(*xr); w = rnd.randint(20, 40) + (y - y0) * 0.25
        out.append(f'<line x1="{x}" y1="{y}" x2="{x + w:.0f}" y2="{y}" stroke="{color}" stroke-width="{1.5 + (y - y0) / 200:.1f}" opacity="{rnd.uniform(*op):.2f}" stroke-linecap="round"/>')
    return "".join(out)


def head_in_water(x, y, r, rim="#c9d3e8", color="#05060a", ring=True):
    ringm = (f'<ellipse cx="{x}" cy="{y + r * .15:.0f}" rx="{r * 2.0:.0f}" ry="{r * .35:.0f}" fill="none" stroke="{rim}" stroke-width="{max(1.5, r / 10):.1f}" opacity="0.35"/>'
             if ring else "")
    return (f'{ringm}<path d="M{x - r} {y} A{r} {r * 1.1:.0f} 0 0 1 {x + r} {y} Z" fill="{color}"/>'
            f'<path d="M{x - r * .55:.0f} {y - r * .82:.0f} A{r} {r * 1.1:.0f} 0 0 1 {x + r * .7:.0f} {y - r * .7:.0f}" fill="none" stroke="{rim}" stroke-width="{max(1.2, r / 9):.1f}" opacity="0.55"/>')


def person(x, base, h, color="#06050a", lean=0, arms_in=False):
    """Simple standing swimmer silhouette (shoulders, head, legs)."""
    hw = h * .13; hr = h * .075
    arms = (f'<path d="M{x - hw:.0f} {base - h * .78:.0f} L{x - hw * 1.25:.0f} {base - h * .45:.0f}" stroke="{color}" stroke-width="{h * .055:.0f}" stroke-linecap="round"/>'
            f'<path d="M{x + hw:.0f} {base - h * .78:.0f} L{x + hw * 1.25:.0f} {base - h * .45:.0f}" stroke="{color}" stroke-width="{h * .055:.0f}" stroke-linecap="round"/>')
    if arms_in:
        arms = (f'<path d="M{x - hw:.0f} {base - h * .78:.0f} L{x - hw * .4:.0f} {base - h * .62:.0f}" stroke="{color}" stroke-width="{h * .06:.0f}" stroke-linecap="round"/>'
                f'<path d="M{x + hw:.0f} {base - h * .78:.0f} L{x + hw * .4:.0f} {base - h * .62:.0f}" stroke="{color}" stroke-width="{h * .06:.0f}" stroke-linecap="round"/>')
    return (f'<g fill="{color}" transform="rotate({lean} {x} {base})">'
            f'<circle cx="{x}" cy="{base - h * .88:.0f}" r="{hr:.0f}"/>'
            f'<path d="M{x - hw:.0f} {base - h * .8:.0f} Q{x} {base - h * .84:.0f} {x + hw:.0f} {base - h * .8:.0f} L{x + hw * .75:.0f} {base - h * .47:.0f} L{x + hw * .55:.0f} {base} L{x + hw * .1:.0f} {base} L{x:.0f} {base - h * .42:.0f} L{x - hw * .1:.0f} {base} L{x - hw * .55:.0f} {base} L{x - hw * .75:.0f} {base - h * .47:.0f} Z"/>'
            f'{arms}</g>')


DUSK = sky("dusk", "#0b0d22", "#3a2340", "#a2413a")
NIGHT = sky("night", "#04050c", "#0f1530", "#26304f")
WATER_D = '<linearGradient id="wd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a2b35"/><stop offset="1" stop-color="#090a16"/></linearGradient>'
WATER_N = '<linearGradient id="wn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1b2440"/><stop offset="1" stop-color="#04050b"/></linearGradient>'
SAND = '<linearGradient id="sand" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a2230"/><stop offset="1" stop-color="#0d0a10"/></linearGradient>'


def buoys(y, color="#c2362b", x0=0, x1=1920, step=95, r=9):
    rope = f'<path d="M{x0} {y} ' + " ".join(f"Q{x + step / 2} {y + 6} {x + step} {y}" for x in range(x0, x1, step)) + '" stroke="#1a1a24" stroke-width="3" fill="none"/>'
    return rope + "".join(f'<ellipse cx="{x}" cy="{y}" rx="{r * 1.3:.0f}" ry="{r}" fill="{color if i % 2 else "#d8d2c4"}" opacity="0.85"/>' for i, x in enumerate(range(x0, x1, step)))


def moonpath(x, y0, y1, color="#e9e4d4"):
    out = []
    for i in range(40):
        y = y0 + (y1 - y0) * i / 40; w = 30 + i * 6 + rnd.randint(-10, 10)
        out.append(f'<rect x="{x - w / 2 + rnd.randint(-20, 20):.0f}" y="{y:.0f}" width="{w}" height="{2 + i // 10}" fill="{color}" opacity="{rnd.uniform(.15, .45):.2f}"/>')
    return "".join(out)


# ---------- S1: the lifeguard chair at dusk
chair = f'''<g fill="#09070c" stroke="#09070c">
<line x1="1010" y1="930" x2="1060" y2="560" stroke-width="16"/><line x1="1230" y1="930" x2="1180" y2="560" stroke-width="16"/>
<line x1="1035" y1="930" x2="1080" y2="600" stroke-width="10"/><line x1="1205" y1="930" x2="1160" y2="600" stroke-width="10"/>
<line x1="1030" y1="760" x2="1210" y2="760" stroke-width="10"/><line x1="1040" y1="680" x2="1200" y2="680" stroke-width="10"/>
<line x1="1018" y1="860" x2="1222" y2="860" stroke-width="10"/>
<rect x="1040" y="540" width="160" height="22" stroke="none"/>
<rect x="1060" y="380" width="120" height="165" rx="6" stroke="none"/>
<line x1="1050" y1="470" x2="1050" y2="545" stroke-width="10"/><line x1="1190" y1="470" x2="1190" y2="545" stroke-width="10"/>
<line x1="1050" y1="470" x2="1080" y2="470" stroke-width="10"/><line x1="1160" y1="470" x2="1190" y2="470" stroke-width="10"/>
<line x1="1120" y1="380" x2="1120" y2="260" stroke-width="7"/>
</g>
<path d="M1120 262 L1220 285 L1120 308 Z" fill="#7d1c1c"/>
<rect x="1068" y="392" width="104" height="140" rx="4" fill="#1d1820"/>
<text x="1120" y="440" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="22" fill="#c9bfa8" letter-spacing="2">COUNT</text>
<text x="1120" y="470" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="22" fill="#c9bfa8" letter-spacing="2">AT</text>
<text x="1120" y="500" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="20" fill="#c9bfa8" letter-spacing="1">SUNSET</text>
<line x1="1080" y1="514" x2="1160" y2="514" stroke="#8c2a22" stroke-width="3"/>
<circle cx="1000" cy="720" r="44" fill="none" stroke="#d8d2c4" stroke-width="22"/>
<circle cx="1000" cy="720" r="44" fill="none" stroke="#b3261e" stroke-width="22" stroke-dasharray="34.5 34.5"/>
<line x1="1000" y1="676" x2="1045" y2="640" stroke="#09070c" stroke-width="5"/>'''
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#dusk)"/>
{stars(40, 260, 0.5)}
<ellipse cx="760" cy="{HZ}" rx="520" ry="120" fill="#ff7a4a" opacity="0.35" filter="url(#blur60)"/>
<circle cx="760" cy="{HZ + 4}" r="70" fill="#e86a3e" opacity="0.8"/>
<rect x="0" y="{HZ}" width="{W}" height="{H - HZ}" fill="url(#wd)"/>
{pines(HZ + 4, 140, 40, 120, "#0b0912")}
<rect x="0" y="{HZ}" width="{W}" height="6" fill="#0b0912"/>
<rect x="640" y="{HZ + 8}" width="240" height="160" fill="#e86a3e" opacity="0.25" filter="url(#blur30)"/>
{ripples(HZ + 10, 820, 160, "#f0a07a", (0.1, 0.45))}
{buoys(700, x0=0, x1=1940)}
<path d="M0 860 C400 830 900 850 1300 835 C1600 826 1800 840 1920 830 L1920 1080 L0 1080Z" fill="url(#sand)"/>
<path d="M0 870 C400 845 900 862 1300 848 C1600 840 1800 852 1920 845" stroke="#d6a48f" stroke-width="3" fill="none" opacity="0.35"/>
{chair}
{grass(1080, 80, "#07060b", (14, 30))}
{fog(800, "#d48a7a", 0.10, 90)}
''', DUSK + WATER_D + SAND))

# ---------- S2: eleven heads in the dark water (and S2b: twelve)
def water_scene(extra_head):
    heads = [(700, 760, 22), (820, 720, 18), (930, 790, 26), (1060, 740, 20), (1190, 770, 24), (620, 830, 30), (1270, 840, 30),
             (880, 880, 36), (1080, 900, 38), (760, 680, 14), (1140, 690, 15)]
    hm = "".join(head_in_water(x, y, r) for x, y, r in heads)
    if extra_head:
        hm += glow(965, 610, 70, "#cfdcff", 0.35) + head_in_water(965, 618, 18, rim="#ffffff", ring=False) + eyes(965, 608, gap=14, r=2.5, color="#e4ecff")
    return svg(f'''
<rect width="{W}" height="{H}" fill="url(#dusk2)"/>
{stars(120, 400, 0.6)}
<rect x="0" y="{HZ - 40}" width="{W}" height="{H}" fill="url(#wn)"/>
{pines(HZ - 36, 160, 50, 140, "#06070d")}
<rect x="0" y="{HZ - 40}" width="{W}" height="8" fill="#06070d"/>
{moon(1500, 220, 60)}
{moonpath(965, HZ - 30, 1080, "#c9d3e8")}
{ripples(HZ - 20, 1060, 220, "#9fb0d8", (0.08, 0.35))}
{buoys(660, x0=0, x1=1940, step=80, r=7)}
{hm}
<path d="M0 1010 C500 990 1400 1000 1920 990 L1920 1080 L0 1080Z" fill="#0a0b12"/>
{fog(HZ, "#aab3c8", 0.12, 80)}
''', sky("dusk2", "#04050c", "#141a35", "#3b2a44") + WATER_N)

save("s2", water_scene(False))
save("s2b", water_scene(True))

# ---------- S3: the whistle
save("s3", svg(f'''
<rect width="{W}" height="{H}" fill="url(#bg3)"/>
{glow(960, 520, 360, "#7a1d22", 0.35)}
<path d="M660 0 C700 220 780 360 880 430" stroke="#c9bfa8" stroke-width="10" fill="none"/>
<path d="M1260 0 C1220 220 1140 360 1040 430" stroke="#c9bfa8" stroke-width="10" fill="none"/>
<circle cx="960" cy="450" r="34" fill="none" stroke="#a7853f" stroke-width="10"/>
<g transform="rotate(-12 960 600)">
<rect x="770" y="500" width="300" height="120" rx="34" fill="url(#red3)"/>
<circle cx="1040" cy="620" r="105" fill="url(#red3)"/>
<rect x="640" y="525" width="170" height="70" rx="14" fill="url(#red3)"/>
<rect x="640" y="545" width="18" height="30" fill="#2a0607"/>
<rect x="880" y="515" width="60" height="30" rx="6" fill="#2a0607"/>
<path d="M790 512 L1050 512" stroke="#ff8b7a" stroke-width="6" opacity="0.6" stroke-linecap="round"/>
<circle cx="1040" cy="620" r="60" fill="#5a0d10" opacity="0.6"/>
</g>
<g fill="#050306">
<path d="M1060 1080 C1060 900 1100 780 1180 720 C1260 660 1330 700 1360 760 L1460 1080 Z"/>
<rect x="1010" y="690" width="230" height="56" rx="28" transform="rotate(-20 1120 720)"/>
<rect x="1030" y="745" width="240" height="56" rx="28" transform="rotate(-14 1150 770)"/>
<rect x="1050" y="805" width="220" height="56" rx="28" transform="rotate(-8 1160 830)"/>
</g>
{glow(1060, 560, 160, "#ff4a3a", 0.25)}
{fog(950, "#6a5a6a", 0.12)}
''', '<radialGradient id="bg3" cx="0.5" cy="0.45" r="0.7"><stop offset="0" stop-color="#2a1a26"/><stop offset="1" stop-color="#05040a"/></radialGradient>'
     '<linearGradient id="red3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e2453a"/><stop offset="0.6" stop-color="#a51f1f"/><stop offset="1" stop-color="#4a0a0c"/></linearGradient>'))

# ---------- S4: eleven on the sand, one head out past the rope
crowd = [(570, 960, 200), (650, 985, 215), (730, 955, 190), (810, 990, 225), (890, 965, 200),
         (1035, 970, 205), (1115, 990, 225), (1195, 958, 190), (1275, 980, 215), (1355, 962, 200), (960, 1010, 235)]
crowd_m = "".join(person(x, b, h, "#050409", lean=rnd.uniform(-3, 3), arms_in=(i % 3 == 0)) for i, (x, b, h) in enumerate(crowd))
towels = "".join(f'<rect x="{x}" y="{y}" width="140" height="22" rx="4" fill="{c}" transform="skewX(-20)" opacity="0.7"/>'
                 for x, y, c in ((900, 980, "#5a1b22"), (1450, 1000, "#2a3550"), (1180, 1030, "#3b2f2a")))
save("s4", svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(160, 420, 0.75)}
{moon(960, 230, 58)}
<rect x="0" y="{HZ}" width="{W}" height="{H - HZ}" fill="url(#wn)"/>
{pines(HZ + 4, 150, 40, 130, "#05060b")}
<rect x="0" y="{HZ}" width="{W}" height="6" fill="#05060b"/>
{moonpath(960, HZ + 8, 800)}
{ripples(HZ + 10, 790, 150, "#9fb0d8", (0.08, 0.3))}
{buoys(700, x0=0, x1=1940)}
{glow(960, 615, 70, "#dfe6ff", 0.35)}
{head_in_water(960, 625, 18, rim="#ffffff", ring=False)}
<path d="M0 790 C400 780 900 795 1300 785 C1600 778 1800 790 1920 784 L1920 1080 L0 1080Z" fill="url(#sand)"/>
<path d="M0 800 C400 790 900 806 1300 795 C1600 788 1800 800 1920 794" stroke="#c9d3e8" stroke-width="3" fill="none" opacity="0.3"/>
{towels}
{crowd_m}
{grass(1080, 60, "#050409", (14, 30))}
{fog(780, "#aab3c8", 0.10, 70)}
''', NIGHT + WATER_N + SAND))

# ---------- S5: the head that watches (and S5b: gone, no ripple)
def close_head(present):
    hm = ""
    if present:
        hm = (f'<path d="M820 640 C820 520 880 460 960 460 C1040 460 1100 520 1100 640 Z" fill="#030307"/>'
              f'<path d="M842 560 C860 500 905 474 960 472" stroke="#dfe6ff" stroke-width="5" fill="none" opacity="0.5"/>'
              f'<path d="M830 640 C860 625 900 620 960 620 C1020 620 1060 625 1090 640" stroke="#030307" stroke-width="10" fill="none"/>'
              f'{eyes(960, 590, gap=70, r=7, color="#d9e4ff")}'
              f'<path d="M820 640 L1100 640 L1110 700 L810 700 Z" fill="#030307" opacity="0.55" filter="url(#blur8)"/>')
    return svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(120, 300, 0.6)}
{moon(1240, 150, 50)}
<rect x="0" y="380" width="{W}" height="700" fill="url(#wn)"/>
{pines(384, 160, 30, 90, "#05060b")}
<rect x="0" y="380" width="{W}" height="6" fill="#05060b"/>
{moonpath(1150, 390, 1080)}
{ripples(400, 600, 60, "#9fb0d8", (0.06, 0.2))}
<path d="M0 640 L1920 640" stroke="#c9d3e8" stroke-width="2" opacity="0.35"/>
<rect x="0" y="640" width="{W}" height="440" fill="#02030a" opacity="0.45"/>
{ripples(660, 1060, 90, "#9fb0d8", (0.05, 0.22))}
{hm}
{fog(640, "#aab3c8", 0.14, 60)}
''', NIGHT + WATER_N)

save("s5", close_head(True))
save("s5b", close_head(False))

# ---------- S6: twelve on the beach, facing me, empty lake behind
back_row = [(600, 900, 200), (720, 905, 210), (840, 895, 195), (1080, 900, 205), (1200, 908, 212), (1320, 896, 198)]
front_row = [(560, 1040, 290), (700, 1050, 300), (840, 1035, 285), (1080, 1045, 295), (1220, 1050, 305), (1360, 1038, 288)]
row_m = ("".join(person(x, b, h, "#0b0a14", lean=rnd.uniform(-2, 2), arms_in=True) for x, b, h in back_row)
         + "".join(person(x, b, h, "#040308", lean=rnd.uniform(-2, 2), arms_in=True) for x, b, h in front_row))
save("s6", svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(160, 420, 0.75)}
{moon(1250, 200, 52)}
<rect x="0" y="{HZ}" width="{W}" height="{H - HZ}" fill="url(#wn)"/>
{pines(HZ + 4, 150, 40, 130, "#05060b")}
<rect x="0" y="{HZ}" width="{W}" height="6" fill="#05060b"/>
{moonpath(1250, HZ + 8, 790)}
<rect x="0" y="{HZ + 8}" width="{W}" height="240" fill="#0a0e20" opacity="0.25"/>
{buoys(690, x0=0, x1=1940)}
<path d="M0 790 C400 780 900 795 1300 785 C1600 778 1800 790 1920 784 L1920 1080 L0 1080Z" fill="url(#sand)"/>
{glow(960, 900, 380, "#7a1d22", 0.22)}
{row_m}
{grass(1080, 60, "#050409", (14, 30))}
{fog(800, "#aab3c8", 0.12, 80)}
''', NIGHT + WATER_N + SAND))

# ---------- S7: eleven breaths in the cold air... and one without
def bust(x, base, s, breath=True, color="#050409"):
    hr = 70 * s
    out = (f'<g fill="{color}"><path d="M{x - 170 * s:.0f} {base} C{x - 165 * s:.0f} {base - 150 * s:.0f} {x - 110 * s:.0f} {base - 190 * s:.0f} {x - 40 * s:.0f} {base - 200 * s:.0f} '
           f'L{x + 40 * s:.0f} {base - 200 * s:.0f} C{x + 110 * s:.0f} {base - 190 * s:.0f} {x + 165 * s:.0f} {base - 150 * s:.0f} {x + 170 * s:.0f} {base} Z"/>'
           f'<rect x="{x - 32 * s:.0f}" y="{base - 250 * s:.0f}" width="{64 * s:.0f}" height="{70 * s:.0f}"/>'
           f'<ellipse cx="{x}" cy="{base - 300 * s:.0f}" rx="{hr * .9:.0f}" ry="{hr * 1.12:.0f}"/></g>'
           f'<path d="M{x - hr * .8:.0f} {base - 330 * s:.0f} C{x - hr * .6:.0f} {base - 375 * s:.0f} {x - hr * .1:.0f} {base - 385 * s:.0f} {x + hr * .2:.0f} {base - 383 * s:.0f}" stroke="#8a93ad" stroke-width="{3 * s:.1f}" fill="none" opacity="0.45"/>')
    if breath:
        bx = x + 90 * s; by = base - 285 * s
        out += (f'<g filter="url(#blur8)" fill="#dfe6f2"><ellipse cx="{bx:.0f}" cy="{by:.0f}" rx="{45 * s:.0f}" ry="{24 * s:.0f}" opacity="0.35"/>'
                f'<ellipse cx="{bx + 55 * s:.0f}" cy="{by - 18 * s:.0f}" rx="{60 * s:.0f}" ry="{32 * s:.0f}" opacity="0.22"/>'
                f'<ellipse cx="{bx + 120 * s:.0f}" cy="{by - 40 * s:.0f}" rx="{70 * s:.0f}" ry="{36 * s:.0f}" opacity="0.12"/></g>')
    return out

back = "".join(bust(x, 760, 0.55, True, "#0a0912") for x in (520, 640, 1300, 1420, 760))
front_l = bust(660, 1100, 1.0, True); front_r = bust(1270, 1100, 1.0, True)
it = (bust(960, 1130, 1.12, False, "#020205")
      + f'<g stroke="#bfd0ea" stroke-width="3" fill="none" opacity="0.55">'
        f'<path d="M905 820 C902 850 900 880 903 905"/><path d="M1010 812 C1014 845 1012 870 1016 900"/><path d="M955 790 C952 800 950 815 952 825"/></g>'
      + '<g fill="#bfd0ea" opacity="0.7"><circle cx="903" cy="912" r="4"/><circle cx="1016" cy="907" r="4"/><circle cx="952" cy="832" r="3"/></g>'
      + eyes(960, 770, gap=56, r=6, color="#e4ecff")
      + '<path d="M915 830 Q960 852 1005 830" stroke="#e4ecff" stroke-width="4" fill="none" opacity="0.8" stroke-linecap="round"/>')
save("s7", svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(100, 300, 0.6)}
{moon(1380, 170, 44)}
<rect x="0" y="470" width="{W}" height="610" fill="url(#wn)"/>
{pines(474, 160, 30, 90, "#05060b")}
<rect x="0" y="470" width="{W}" height="6" fill="#05060b"/>
{moonpath(1380, 480, 760)}
{back}
{glow(960, 700, 260, "#3a4a7a", 0.35)}
{front_l}{front_r}
{it}
{fog(1000, "#aab3c8", 0.10, 80)}
''', NIGHT + WATER_N))
print("ok")
