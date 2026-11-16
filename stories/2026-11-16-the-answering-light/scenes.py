"""Scenes for The Answering Light. Run inside this folder: python3 scenes.py"""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

HAND = "DejaVu Serif, serif"
_save = save


def save(name, markup):
    """Widen blur filter regions so small glows don't clip into squares."""
    for b in ("blur8", "blur30", "blur60"):
        markup = markup.replace(f'<filter id="{b}">', f'<filter id="{b}" x="-200%" y="-200%" width="500%" height="500%">')
    _save(name, markup)


def sea(y0, top="#0c1424", bottom="#04070d", n=60, seed_off=0):
    """Dark sea from y0 down with thin wave glints."""
    waves = "".join(
        f'<path d="M{x} {y} q{w / 4} -5 {w / 2} 0 t{w / 2} 0" stroke="#5a6f92" stroke-width="{1.5 + (y - y0) / 160:.1f}" '
        f'fill="none" opacity="{0.12 + (y - y0) / 2400:.2f}"/>'
        for x, y, w in ((rnd.randint(-100, W), rnd.randint(y0 + 8, H), rnd.randint(40, 180)) for _ in range(n)))
    return (f'<rect x="0" y="{y0}" width="{W}" height="{H - y0}" fill="url(#seaG)"/>{waves}',
            f'<linearGradient id="seaG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/>'
            f'<stop offset="1" stop-color="{bottom}"/></linearGradient>')


def lighthouse(cx, base, top, lamp="#ffcf7a", beam_dir=-1, beam=True):
    bw, tw = 95, 62
    out = []
    if beam:
        tip = 0 if beam_dir < 0 else W
        out.append(f'<polygon points="{cx},{top - 45} {tip},{top - 260} {tip},{top + 170}" fill="url(#beamG)" opacity="0.55"/>')
    out.append(f'<polygon points="{cx - bw},{base} {cx - tw},{top} {cx + tw},{top} {cx + bw},{base}" fill="#0a0c14"/>')
    # faint red bands
    for f in (0.25, 0.55):
        y1 = top + (base - top) * f; y2 = y1 + 60
        w1 = tw + (bw - tw) * f; w2 = tw + (bw - tw) * (f + 60 / (base - top))
        out.append(f'<polygon points="{cx - w1:.0f},{y1:.0f} {cx + w1:.0f},{y1:.0f} {cx + w2:.0f},{y2:.0f} {cx - w2:.0f},{y2:.0f}" fill="#3a1216" opacity="0.8"/>')
    out.append(f'<rect x="{cx - 14}" y="{top + 120}" width="28" height="40" rx="12" fill="{lamp}" opacity="0.55"/>')
    out.append(f'<rect x="{cx - 88}" y="{top - 8}" width="176" height="16" fill="#07080e"/>')
    out.append("".join(f'<line x1="{x}" y1="{top - 8}" x2="{x}" y2="{top - 36}" stroke="#07080e" stroke-width="4"/>' for x in range(cx - 84, cx + 90, 21)))
    out.append(f'<rect x="{cx - 88}" y="{top - 40}" width="176" height="6" fill="#07080e"/>')
    out.append(f'<rect x="{cx - 50}" y="{top - 100}" width="100" height="92" fill="{lamp}"/>')
    out.append(glow(cx, top - 55, 90, lamp, 0.7))
    out.append("".join(f'<line x1="{x}" y1="{top - 100}" x2="{x}" y2="{top - 8}" stroke="#07080e" stroke-width="5"/>' for x in (cx - 25, cx, cx + 25)))
    out.append(f'<path d="M{cx - 60} {top - 98} Q{cx} {top - 175} {cx + 60} {top - 98}Z" fill="#07080e"/>')
    out.append(f'<line x1="{cx}" y1="{top - 150}" x2="{cx}" y2="{top - 185}" stroke="#07080e" stroke-width="5"/>')
    return "".join(out)


BEAM = ('<linearGradient id="beamG" x1="1" y1="0" x2="0" y2="0"><stop offset="0" stop-color="#ffe2a0" stop-opacity="0.9"/>'
        '<stop offset="1" stop-color="#ffe2a0" stop-opacity="0"/></linearGradient>')

# S1 — lighthouse on a rocky island, beam sweeping left
sea1, seadef1 = sea(700, n=90)
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(170, 640)}
{moon(1290, 190, 62)}
{sea1}
<ellipse cx="1290" cy="760" rx="40" ry="220" fill="#f1e9d3" opacity="0.07" filter="url(#blur30)"/>
{lighthouse(930, 760, 330)}
<path d="M600 800 C640 740 700 720 760 735 C820 700 900 710 960 730 C1040 700 1120 720 1180 745 C1250 735 1320 770 1360 810 Z" fill="#080a10"/>
<path d="M560 830 C650 790 760 800 860 790 C980 785 1120 795 1240 790 C1330 800 1400 815 1440 840 L1440 860 L560 860Z" fill="#0b0e16"/>
<g fill="#07090f"><polygon points="1050,745 1050,680 1110,640 1170,680 1170,745"/><rect x="1140" y="645" width="14" height="40"/></g>
{lit_window(1075, 690, 34, 34)}
{fog(820, op=0.12, ry=80)}
<g fill="#06080d"><path d="M0 1080 L0 930 C80 900 160 910 230 940 C300 960 330 1000 360 1080Z"/>
<path d="M1920 1080 L1920 900 C1820 880 1730 920 1660 960 C1600 990 1580 1040 1560 1080Z"/></g>
''', sky("sky1", "#04060e", "#141a33", "#2a2a46") + seadef1 + BEAM))

# S2 — inside the lamp room: the great lens, windows onto black sea
panes = "".join(f'<rect x="{x}" y="160" width="330" height="560" fill="url(#night2)"/>' for x in (130, 495, 1095, 1460))
waves2 = "".join(f'<path d="M{rnd.randint(130, 1790)} {rnd.randint(520, 715)} q20 -4 40 0" stroke="#4a5d80" stroke-width="2" fill="none" opacity="0.35"/>' for _ in range(60))
rings = "".join(f'<ellipse cx="960" cy="440" rx="{r}" ry="{r * 1.25:.0f}" fill="none" stroke="#ffe7b0" stroke-width="{3 + r / 60:.0f}" opacity="{0.25 + (220 - r) / 400:.2f}"/>' for r in range(40, 230, 26))
prisms = "".join(f'<rect x="{960 - 210}" y="{y}" width="420" height="10" rx="5" fill="#fff1c9" opacity="0.35"/>' for y in (180, 215, 250, 630, 665, 700))
save("s2", svg(f'''
<rect width="{W}" height="{H}" fill="#07080d"/>
{panes}
<g>{waves2}</g>
<line x1="130" y1="510" x2="1790" y2="510" stroke="#2a3552" stroke-width="2" opacity="0.6"/>
<g fill="#0b0c12">{''.join(f'<rect x="{x}" y="140" width="35" height="600"/>' for x in (95, 460, 825, 1060, 1425, 1790))}
<rect x="0" y="120" width="{W}" height="40"/><rect x="0" y="720" width="{W}" height="40"/></g>
<circle cx="960" cy="440" r="420" fill="#ffb54a" opacity="0.18" filter="url(#blur60)"/>
<path d="M740 160 L1180 160 L1230 720 L690 720Z" fill="#3a2a14" opacity="0.6"/>
<ellipse cx="960" cy="440" rx="240" ry="300" fill="url(#lensG)"/>
{rings}{prisms}
<circle cx="960" cy="440" r="46" fill="#fff6dc"/>
{glow(960, 440, 120, "#ffd890", 0.9)}
<rect x="900" y="740" width="120" height="340" fill="#0a0b10"/>
<rect x="760" y="760" width="400" height="30" fill="#0e0f16"/>
<path d="M0 860 L1920 860" stroke="#0d0e14" stroke-width="10"/>
<g stroke="#0d0e14" stroke-width="6">{''.join(f'<line x1="{x}" y1="860" x2="{x}" y2="1080"/>' for x in range(60, 1920, 110))}</g>
<rect x="0" y="1000" width="{W}" height="80" fill="#08090d"/>
<polygon points="960,440 1920,220 1920,700" fill="#ffe2a0" opacity="0.05"/>
''', '<linearGradient id="night2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05070f"/><stop offset="0.62" stop-color="#151b33"/><stop offset="0.63" stop-color="#0a1120"/><stop offset="1" stop-color="#04060c"/></linearGradient>'
   '<radialGradient id="lensG"><stop offset="0" stop-color="#fff3d0" stop-opacity="0.9"/><stop offset="0.6" stop-color="#e2a54e" stop-opacity="0.55"/><stop offset="1" stop-color="#6b4316" stop-opacity="0.4"/></radialGradient>'))

# S3 — from the gallery rail: a tiny light blinking far out past the rocks
sea3, seadef3 = sea(560, top="#0b1222", n=120)
rail = "".join(f'<rect x="{x}" y="820" width="12" height="260" fill="#05060a"/>' for x in range(0, 1920, 96))
save("s3", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky3)"/>
{stars(220, 520, 0.8)}
{sea3}
<polygon points="1920,250 0,120 0,330 1920,330" fill="#ffe2a0" opacity="0.05"/>
<g fill="#06080d"><path d="M640 640 C700 610 760 615 800 640 L820 660 L620 660Z"/>
<path d="M1180 630 C1230 600 1300 605 1340 640 L1360 655 L1170 655Z"/>
<path d="M880 610 C900 598 930 600 945 612 L950 620 L875 620Z"/></g>
<circle cx="1040" cy="588" r="9" fill="#fff3d6"/>
{glow(1040, 588, 34, "#ffeec8", 0.95)}
{glow(1040, 588, 60, "#ff9e6a", 0.35)}
<line x1="1040" y1="600" x2="1040" y2="760" stroke="#ffeec8" stroke-width="6" opacity="0.18" filter="url(#blur8)"/>
{fog(640, op=0.10, ry=60)}
<rect x="0" y="790" width="{W}" height="34" rx="6" fill="#06070b"/>
{rail}
<rect x="0" y="960" width="{W}" height="18" fill="#05060a"/>
<rect x="0" y="1040" width="{W}" height="40" fill="#030305"/>
''', sky("sky3", "#03050c", "#0f1428", "#1d2340") + seadef3))

# S4 — hand on the signal lamp, aimed out the window
save("s4", svg(f'''
<rect width="{W}" height="{H}" fill="#06070b"/>
<rect x="140" y="140" width="760" height="640" fill="url(#night4)"/>
{stars(40, 0)}
<g>{''.join(f'<circle cx="{rnd.randint(150, 890)}" cy="{rnd.randint(150, 470)}" r="1.6" fill="#dfe3f5" opacity="{rnd.uniform(.3, .8):.2f}"/>' for _ in range(50))}</g>
<g fill="#0b0c12"><rect x="120" y="120" width="800" height="30"/><rect x="120" y="770" width="800" height="30"/>
<rect x="120" y="120" width="30" height="680"/><rect x="890" y="120" width="30" height="680"/><rect x="505" y="120" width="26" height="680"/></g>
{glow(380, 540, 10, "#fff1d0", 0.95)}
<rect x="0" y="800" width="{W}" height="280" fill="#0d0b0b"/>
<rect x="0" y="800" width="{W}" height="14" fill="#1a1512"/>
<g transform="translate(0 0)">
<rect x="880" y="420" width="560" height="300" rx="40" fill="url(#metal)"/>
<rect x="840" y="400" width="90" height="340" rx="24" fill="#2b2f36"/>
<ellipse cx="850" cy="570" rx="40" ry="150" fill="#9fb0c8"/>
<ellipse cx="850" cy="570" rx="30" ry="125" fill="#d9e3f0" opacity="0.4"/>
{''.join(f'<line x1="{x}" y1="440" x2="{x}" y2="700" stroke="#1a1d22" stroke-width="3" opacity="0.7"/>' for x in range(980, 1420, 60))}
<rect x="1110" y="380" width="200" height="44" rx="12" fill="#22262c"/>
<rect x="1300" y="560" width="230" height="60" rx="20" fill="#1c1f24"/>
<rect x="1520" y="540" width="120" height="260" rx="30" fill="#17191d"/>
<rect x="1140" y="358" width="70" height="26" rx="8" fill="#b02a22"/>
</g>
<g fill="#241915" stroke="#7a5442" stroke-width="3">
<path d="M1330 300 L1960 250 L1960 420 L1340 420Z"/>
<ellipse cx="1260" cy="355" rx="115" ry="58"/>
<rect x="1180" y="352" width="38" height="96" rx="19"/>
<rect x="1222" y="358" width="38" height="104" rx="19"/>
<rect x="1264" y="360" width="38" height="100" rx="19"/>
<rect x="1306" y="356" width="34" height="86" rx="17"/>
<path d="M1200 330 C1170 330 1150 345 1160 362 C1170 376 1200 370 1215 362Z"/>
</g>
<path d="M1150 320 C1220 290 1330 290 1380 305" stroke="#c98a5a" stroke-width="4" fill="none" opacity="0.6"/>
<circle cx="900" cy="570" r="380" fill="#9fb4e8" opacity="0.05" filter="url(#blur60)"/>
<circle cx="1250" cy="480" r="260" fill="#ffb54a" opacity="0.06" filter="url(#blur60)"/>
''', '<linearGradient id="night4" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05070f"/><stop offset="0.6" stop-color="#141a33"/><stop offset="0.61" stop-color="#0a1120"/><stop offset="1" stop-color="#04060c"/></linearGradient>'
   '<linearGradient id="metal" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a505a"/><stop offset="0.5" stop-color="#2c3038"/><stop offset="1" stop-color="#15171b"/></linearGradient>'))


# Logbook pages
def book(left_entries, right_entries, extra=""):
    def entries(x, items):
        out = []
        for i, (txt, ink, size, rot) in enumerate(items):
            y = 330 + i * 78
            out.append(f'<text x="{x}" y="{y}" font-family="{HAND}" font-style="italic" font-size="{size}" fill="{ink}" '
                       f'transform="rotate({rot} {x} {y})">{txt}</text>')
        return "".join(out)
    lines = "".join(f'<line x1="{x0}" y1="{y}" x2="{x0 + 360}" y2="{y}" stroke="#8a7656" stroke-width="1.5" opacity="0.45"/>'
                    for x0 in (595, 990) for y in range(300, 880, 39))
    return svg(f'''
<rect width="{W}" height="{H}" fill="#0b0705"/>
<rect x="0" y="0" width="{W}" height="{H}" fill="url(#desk)"/>
<g stroke="#000" stroke-width="3" opacity="0.35">{''.join(f'<path d="M0 {y} C600 {y + 20} 1300 {y - 20} 1920 {y}" fill="none"/>' for y in range(60, 1080, 120))}</g>
<path d="M545 195 L960 230 L1375 195 L1395 935 L960 960 L525 935Z" fill="#000" opacity="0.6" filter="url(#blur30)"/>
<path d="M560 180 L960 215 L960 940 L545 915Z" fill="url(#pageL)"/>
<path d="M960 215 L1360 180 L1375 915 L960 940Z" fill="url(#pageR)"/>
<line x1="960" y1="215" x2="960" y2="940" stroke="#4a3a24" stroke-width="5"/>
<g clip-path="url(#pages)">{lines}</g>
<g clip-path="url(#pages)">{entries(600, left_entries)}{entries(995, right_entries)}</g>
<circle cx="1640" cy="380" r="300" fill="#ffaa44" opacity="0.18" filter="url(#blur60)"/>
<g transform="translate(1640 300)">
<ellipse cx="0" cy="330" rx="110" ry="26" fill="#000" opacity="0.6" filter="url(#blur8)"/>
<path d="M-80 320 C-80 260 80 260 80 320Z" fill="#2c1e12"/>
<path d="M-40 270 C-70 180 -60 80 0 40 C60 80 70 180 40 270Z" fill="#e8d6b0" opacity="0.35"/>
<path d="M-12 200 C-20 160 0 120 0 110 C0 120 20 160 12 200Z" fill="#ffd27a"/>
{glow(0, 170, 60, "#ffb54a", 0.8)}
</g>
{extra}
''', '<linearGradient id="desk" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1c120b"/><stop offset="1" stop-color="#0a0604"/></linearGradient>'
     '<linearGradient id="pageL" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#b7a07a"/><stop offset="1" stop-color="#8a7655"/></linearGradient>'
     '<linearGradient id="pageR" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8f7b59"/><stop offset="1" stop-color="#c4ad86"/></linearGradient>'
     '<clipPath id="pages"><path d="M560 180 L960 215 L1360 180 L1375 915 L960 940 L545 915Z"/></clipPath>')


INK = ["#2a1d10", "#1d2433", "#33201a", "#202a1c", "#2b2230"]
na_left = [("Night 9.", INK[0], 30, -2), ("Light on the water.", INK[0], 32, -2), ("Not answered.", INK[0], 34, -2),
           ("", INK[0], 30, 0), ("Night 9.", INK[1], 30, 1), ("Light on the water.", INK[1], 32, 1), ("Not answered.", INK[1], 34, 1)]
na_right = [("Night 9.", INK[2], 30, -1), ("Light on the water.", INK[2], 32, -1), ("Not answered.", INK[2], 34, -1),
            ("", INK[0], 30, 0), ("Night 9.", INK[3], 28, 2), ("Light on the water.", INK[3], 30, 2), ("Not answered.", INK[3], 32, 2)]

# S5 — every keeper wrote the same thing
save("s5", book(na_left, na_right))

# S5b — the last keeper's entry
save("s5b", book(na_left, [("Night 9.", INK[4], 30, 0), ("", INK[4], 30, 0), ("ANSWERED.", "#7a120e", 54, -3)],
                 extra='<ellipse cx="1150" cy="489" rx="190" ry="50" fill="#b3261e" opacity="0.12" filter="url(#blur30)"/>'))

# S6 — a rowboat with a lantern coming out of the fog toward the rocks
sea6, seadef6 = sea(600, top="#0e1626", n=110)
save("s6", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky6)"/>
{stars(60, 400, 0.4)}
{sea6}
{fog(560, op=0.22, ry=160)}
<g fill="#080a10"><path d="M0 1080 L0 760 C120 730 260 760 360 820 C430 870 470 960 500 1080Z"/>
<path d="M1920 1080 L1920 700 C1800 690 1660 740 1560 820 C1500 880 1470 980 1460 1080Z"/></g>
<g transform="translate(960 720)">
<ellipse cx="0" cy="40" rx="260" ry="26" fill="#ffcf7a" opacity="0.12" filter="url(#blur30)"/>
<path d="M-220 0 L220 0 C200 40 140 60 0 62 C-140 60 -200 40 -220 0Z" fill="#06070b"/>
<path d="M-40 0 L-40 -110 C-40 -150 -10 -170 20 -170 C50 -170 70 -150 70 -110 L70 0Z" fill="#040406"/>
<ellipse cx="15" cy="-195" rx="36" ry="42" fill="#040406"/>
<path d="M-40 -90 L-260 60" stroke="#040406" stroke-width="12" stroke-linecap="round"/>
<path d="M70 -90 L260 60" stroke="#040406" stroke-width="12" stroke-linecap="round"/>
<line x1="-150" y1="0" x2="-150" y2="-80" stroke="#06070b" stroke-width="5"/>
<rect x="-166" y="-112" width="32" height="40" rx="6" fill="#ffcf7a"/>
{glow(-150, -92, 60, "#ffb54a", 0.8)}
</g>
<path d="M940 790 L800 1080 L1120 1080 Z" fill="#ffcf7a" opacity="0.05"/>
{fog(880, op=0.10, ry=90)}
''', sky("sky6", "#05070d", "#141b2c", "#26304a") + seadef6))

# fresh handwriting too small to read yet: loops of ink across the right page
SCRIBBLE = "".join(
    f'<path d="M{x0} {y} ' + " ".join(f"q6 -{rnd.randint(10, 22)} 12 0 q6 {rnd.randint(4, 12)} {rnd.randint(8, 16)} 0" for _ in range(n)) +
    f'" stroke="#14234a" stroke-width="3" fill="none" stroke-linecap="round" transform="rotate(-1 {x0} {y})"/>'
    for x0, y, n in ((1000, 410, 13), (1000, 488, 15), (1000, 566, 10), (1000, 644, 14), (1000, 722, 8)))

# S7 — tonight's page, already written, pen beside it
ME = "#14234a"
save("s7", book([("Night 1.  Wind.", INK[0], 30, 0), ("Night 4.  Fog all day.", ME, 30, 0), ("Night 8.  Quiet.", ME, 30, 0)],
                [("Night 10.", ME, 34, 0)],
                extra=SCRIBBLE + f'''<g transform="rotate(-28 1240 860)"><rect x="1100" y="850" width="300" height="18" rx="9" fill="#0d0d12"/>
<polygon points="1100,850 1060,859 1100,868" fill="#b8a46a"/></g>
<circle cx="1180" cy="560" r="230" fill="#4a6ad0" opacity="0.07" filter="url(#blur60)"/>'''))

# S8 — looking down the spiral stairs: wet footprints, something coming up
steps = []
for i in range(14):
    a0 = i * 26
    steps.append(f'<path d="M960 540 L{960 + 470 * __import__("math").cos(__import__("math").radians(a0)):.0f} '
                 f'{540 + 470 * __import__("math").sin(__import__("math").radians(a0)):.0f} A470 470 0 0 1 '
                 f'{960 + 470 * __import__("math").cos(__import__("math").radians(a0 + 24)):.0f} '
                 f'{540 + 470 * __import__("math").sin(__import__("math").radians(a0 + 24)):.0f}Z" '
                 f'fill="{"#1c1a22" if i % 2 else "#16141b"}" stroke="#08070b" stroke-width="5"/>')
inner = []
for i in range(14):
    a0 = i * 26 + 180
    inner.append(f'<path d="M960 540 L{960 + 260 * __import__("math").cos(__import__("math").radians(a0)):.0f} '
                 f'{540 + 260 * __import__("math").sin(__import__("math").radians(a0)):.0f} A260 260 0 0 1 '
                 f'{960 + 260 * __import__("math").cos(__import__("math").radians(a0 + 24)):.0f} '
                 f'{540 + 260 * __import__("math").sin(__import__("math").radians(a0 + 24)):.0f}Z" '
                 f'fill="{"#121017" if i % 2 else "#0e0c12"}" stroke="#060508" stroke-width="4"/>')
prints = "".join(f'<ellipse cx="{x}" cy="{y}" rx="16" ry="26" fill="#5a7aa0" opacity="0.35" transform="rotate({r} {x} {y})"/>'
                 for x, y, r in ((1320, 700, 50), (1250, 820, 70), (1130, 900, 90), (990, 930, 100), (860, 905, 120)))
save("s8", svg(f'''
<rect width="{W}" height="{H}" fill="#060509"/>
<circle cx="960" cy="540" r="560" fill="#0d0c14"/>
{''.join(steps)}
<circle cx="960" cy="540" r="270" fill="#08070c"/>
{''.join(inner)}
<circle cx="960" cy="540" r="200" fill="#030204"/>
<circle cx="960" cy="540" r="60" fill="#000"/>

{prints}
<g transform="translate(960 520) scale(1.7)">
<ellipse cx="0" cy="0" rx="62" ry="54" fill="#020203"/>
<path d="M-70 10 C-120 60 -110 130 -60 150 L60 150 C110 130 120 60 70 10Z" fill="#020203"/>
<path d="M-60 40 L-170 -20" stroke="#020203" stroke-width="18" stroke-linecap="round"/>
<path d="M-170 -20 l-26 -20 m26 20 l-30 -2 m30 2 l-22 -30" stroke="#020203" stroke-width="7" stroke-linecap="round"/>
</g>
{eyes(960, 506, gap=50, r=9)}
{glow(960, 540, 120, "#3a5a8a", 0.25)}
<rect x="1330" y="480" width="16" height="160" fill="#0a0910"/>

''', ""))
print("ok")
