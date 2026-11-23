"""Scenes for Echo Point."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

ROCK1 = "#2a1626"
ROCK2 = "#1b0f1c"
ROCK3 = "#0d0810"
NEON = "#ff3b45"
WARM = "#ffb54a"


def canyon_layers(y=620):
    """Layered mesa / canyon wall silhouettes receding into the night."""
    return (f'<path d="M0 {y} L180 {y} L220 {y-120} L420 {y-120} L450 {y-40} L640 {y-40} L700 {y-170} L900 {y-170} '
            f'L940 {y-60} L1180 {y-60} L1220 {y-150} L1460 {y-150} L1500 {y-30} L1700 {y-30} L1740 {y-110} L1920 {y-110} L1920 1080 L0 1080Z" fill="{ROCK1}"/>'
            f'<path d="M0 {y+80} L120 {y+80} L160 {y+10} L380 {y+10} L420 {y+100} L760 {y+100} L800 {y+20} L1060 {y+20} '
            f'L1100 {y+110} L1400 {y+110} L1440 {y+30} L1640 {y+30} L1680 {y+120} L1920 {y+120} L1920 1080 L0 1080Z" fill="{ROCK2}"/>')


def kid(cx, base, h=300, color="#050305", cupped=True):
    """Small child silhouette; optionally hands cupped at the mouth (facing right)."""
    hr = h * 0.12
    hx, hy = cx, base - h + hr
    body = (f'<circle cx="{hx}" cy="{hy:.0f}" r="{hr:.0f}"/>'
            f'<path d="M{cx - h*.14:.0f} {base - h*.18:.0f} L{cx - h*.12:.0f} {base - h*.62:.0f} C{cx - h*.1:.0f} {base - h*.72:.0f} '
            f'{cx + h*.1:.0f} {base - h*.72:.0f} {cx + h*.12:.0f} {base - h*.62:.0f} L{cx + h*.14:.0f} {base - h*.18:.0f}Z"/>'
            f'<rect x="{cx - h*.11:.0f}" y="{base - h*.2:.0f}" width="{h*.09:.0f}" height="{h*.2:.0f}"/>'
            f'<rect x="{cx + h*.02:.0f}" y="{base - h*.2:.0f}" width="{h*.09:.0f}" height="{h*.2:.0f}"/>')
    if cupped:
        arms = (f'<path d="M{cx + h*.08:.0f} {base - h*.62:.0f} L{cx + h*.2:.0f} {base - h*.7:.0f} L{hx + hr*1.1:.0f} {hy + hr*.3:.0f}" '
                f'stroke="{color}" stroke-width="{h*.06:.0f}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
                f'<path d="M{cx - h*.08:.0f} {base - h*.62:.0f} L{cx + h*.1:.0f} {base - h*.58:.0f} L{hx + hr*1.2:.0f} {hy + hr*.7:.0f}" '
                f'stroke="{color}" stroke-width="{h*.06:.0f}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
                f'<ellipse cx="{hx + hr*1.35:.0f}" cy="{hy + hr*.45:.0f}" rx="{hr*.45:.0f}" ry="{hr*.6:.0f}"/>')
    else:
        arms = (f'<path d="M{cx - h*.12:.0f} {base - h*.62:.0f} L{cx - h*.17:.0f} {base - h*.32:.0f}" stroke="{color}" stroke-width="{h*.06:.0f}" stroke-linecap="round"/>'
                f'<path d="M{cx + h*.12:.0f} {base - h*.62:.0f} L{cx + h*.17:.0f} {base - h*.32:.0f}" stroke="{color}" stroke-width="{h*.06:.0f}" stroke-linecap="round"/>')
    return f'<g fill="{color}">{body}{arms}</g>'


def railing(y, x0=0, x1=W, color="#0a070c"):
    posts = "".join(f'<rect x="{x}" y="{y}" width="14" height="140" fill="{color}"/>' for x in range(x0 + 20, x1, 160))
    return (f'{posts}<rect x="{x0}" y="{y}" width="{x1 - x0}" height="12" fill="{color}"/>'
            f'<rect x="{x0}" y="{y + 60}" width="{x1 - x0}" height="8" fill="{color}"/>')


CANYON_SKY = sky("csky", "#05060f", "#1d1335", "#4a2338")

# S1 — station wagon parked at the overlook at dusk
car = '''<g fill="#07050a">
<path d="M640 860 L650 790 C660 770 690 760 720 758 L780 700 C795 688 815 684 840 684 L1080 684 C1105 684 1120 692 1135 706 L1185 758 L1260 766 C1290 770 1305 790 1305 815 L1305 860 Z"/>
<circle cx="740" cy="866" r="44"/><circle cx="1190" cy="866" r="44"/></g>
<g fill="#2b3350" opacity="0.8"><path d="M800 752 L845 704 L950 704 L950 752Z"/><path d="M965 752 L965 704 L1090 704 L1140 752Z"/></g>
<rect x="1290" y="790" width="16" height="12" fill="#ffd27a"/>
<ellipse cx="1380" cy="800" rx="160" ry="30" fill="#ffd27a" opacity="0.25" filter="url(#blur30)"/>
<rect x="640" y="796" width="12" height="14" fill="#ff3b2f"/><circle cx="646" cy="803" r="24" fill="#ff3b2f" opacity="0.4" filter="url(#blur8)"/>
<rect x="700" y="664" width="400" height="20" rx="6" fill="#07050a"/>
<g fill="#07050a"><rect x="760" y="646" width="120" height="20" rx="4"/><rect x="900" y="650" width="90" height="16" rx="4"/></g>'''
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#csky)"/>{stars(170, 520)}{moon(1340, 210, 80)}
{canyon_layers(600)}{fog(700, "#c58a8a", 0.12, 90)}
<path d="M0 820 L1920 800 L1920 1080 L0 1080Z" fill="{ROCK3}"/>
<path d="M300 1080 L760 830 L1160 828 L1700 1080Z" fill="#141018"/>
{car}
{railing(780, 1360, 1920)}
<rect x="440" y="760" width="16" height="120" fill="#0a070c"/><rect x="380" y="730" width="140" height="44" fill="#100b12"/>
{grass(1080, 140, "#08060a", (20, 46))}
''', CANYON_SKY))

# S2 — the rusted sign on the railing
rust = "".join(f'<circle cx="{rnd.randint(720, 1200)}" cy="{rnd.randint(390, 610)}" r="{rnd.choice([3, 5, 8, 12])}" fill="#5a2a14" opacity="{rnd.uniform(.35, .8):.2f}"/>' for _ in range(40))
save("s2", svg(f'''
<rect width="{W}" height="{H}" fill="url(#csky)"/>{stars(90, 380, 0.5)}
{canyon_layers(560)}{fog(640, "#c58a8a", 0.14, 110)}
<rect x="940" y="600" width="26" height="420" fill="#0b080c"/>
<g transform="rotate(-2 960 500)">
<rect x="700" y="370" width="520" height="260" rx="10" fill="#8f7a5c"/>
<rect x="700" y="370" width="520" height="260" rx="10" fill="#000" opacity="0.35"/>
{rust}
<rect x="722" y="392" width="476" height="216" rx="6" fill="none" stroke="#2a1a12" stroke-width="6"/>
<text x="960" y="452" text-anchor="middle" font-family="{SANS}" font-weight="700" font-size="40" fill="#1e120c" letter-spacing="4">ECHO POINT</text>
<line x1="790" y1="476" x2="1130" y2="476" stroke="#1e120c" stroke-width="4"/>
<text x="960" y="532" text-anchor="middle" font-family="{SANS}" font-weight="700" font-size="40" fill="#5a0d0d">NEVER SHOUT</text>
<text x="960" y="584" text-anchor="middle" font-family="{SANS}" font-weight="700" font-size="40" fill="#5a0d0d">YOUR OWN NAME</text>
<circle cx="724" cy="394" r="6" fill="#2a1a12"/><circle cx="1196" cy="394" r="6" fill="#2a1a12"/>
</g>
{glow(960, 500, 300, "#ffcf8a", 0.10)}
{railing(820)}
<path d="M0 960 L1920 940 L1920 1080 L0 1080Z" fill="{ROCK3}"/>{grass(1080, 160, "#08060a", (18, 40))}
''', CANYON_SKY))

# S3 — Danny shouting into the canyon, rings of sound going out
rings = "".join(f'<path d="M{900 + i*90} {470 - i*55} Q{970 + i*120} 540 {900 + i*90} {610 + i*55}" stroke="#e9d3c0" stroke-width="{6 - i}" fill="none" opacity="{0.55 - i*0.09:.2f}"/>' for i in range(5))
save("s3", svg(f'''
<rect width="{W}" height="{H}" fill="url(#csky)"/>{stars(150, 500)}{moon(1500, 180, 60)}
<path d="M600 560 L760 560 L790 470 L1000 470 L1030 590 L1300 590 L1330 450 L1600 450 L1640 600 L1920 600 L1920 1080 L600 1080Z" fill="{ROCK1}"/>
<path d="M600 700 L900 700 L930 640 L1240 640 L1270 720 L1920 720 L1920 1080 L600 1080Z" fill="{ROCK2}"/>
<ellipse cx="1300" cy="900" rx="600" ry="160" fill="#000" opacity="0.7" filter="url(#blur60)"/>
{fog(760, "#d39a9a", 0.12, 80)}
<path d="M0 640 L820 640 L880 700 L860 1080 L0 1080Z" fill="{ROCK3}"/>
{railing(560, 0, 860)}
{kid(760, 640, 330)}
{rings}
''', CANYON_SKY))

# S3b — the echo keeps going: rings fill the canyon, faint shapes in the depths
rings2 = "".join(f'<path d="M{900 + i*80} {470 - i*40} Q{980 + i*110} 560 {900 + i*80} {650 + i*40}" stroke="#e9c0c0" stroke-width="4" fill="none" opacity="{0.5 - i*0.035:.2f}"/>' for i in range(11))
pale = "".join(eyes(x, y, 18, 4, "#ffd8c8") for x, y in [(1180, 870), (1330, 930), (1050, 960), (1450, 880)])
save("s3b", svg(f'''
<rect width="{W}" height="{H}" fill="url(#csky)"/>{stars(150, 500)}{moon(1500, 180, 60)}
<path d="M600 560 L760 560 L790 470 L1000 470 L1030 590 L1300 590 L1330 450 L1600 450 L1640 600 L1920 600 L1920 1080 L600 1080Z" fill="{ROCK1}"/>
<path d="M600 700 L900 700 L930 640 L1240 640 L1270 720 L1920 720 L1920 1080 L600 1080Z" fill="{ROCK2}"/>
<ellipse cx="1300" cy="900" rx="600" ry="160" fill="#000" opacity="0.8" filter="url(#blur60)"/>
{pale}
{fog(760, "#d39a9a", 0.14, 80)}
<path d="M0 640 L820 640 L880 700 L860 1080 L0 1080Z" fill="{ROCK3}"/>
{railing(560, 0, 860)}
{kid(760, 640, 330, cupped=False)}
{rings2}
''', CANYON_SKY))

# S4 — roadside motel at night, red neon
doors = "".join(f'<rect x="{x}" y="640" width="80" height="170" fill="#120c14"/><rect x="{x+64}" y="720" width="6" height="10" fill="#c9a86a"/>'
                f'<text x="{x+40}" y="630" text-anchor="middle" font-family="{SANS}" font-size="20" fill="#6b5a66">{n}</text>' for n, x in zip(range(1, 7), range(520, 1500, 165)))
lamps = "".join(f'{glow(x, 600, 60, WARM, 0.35)}<circle cx="{x}" cy="600" r="8" fill="#ffd27a"/>' for x in range(600, 1500, 330))
save("s4", svg(f'''
<rect width="{W}" height="{H}" fill="url(#msky)"/>{stars(140, 420)}
<path d="M0 560 L300 520 L600 540 L900 500 L1300 530 L1600 510 L1920 540 L1920 820 L0 820Z" fill="#160d18"/>
<rect x="460" y="560" width="1100" height="260" fill="#0d0a10"/>
<rect x="440" y="540" width="1140" height="30" fill="#07050a"/>
{doors}
<rect x="1040" y="808" width="80" height="6" fill="{WARM}" opacity="0.9"/>
{''.join(lit_window(x + 95, 680, 50, 60, "#d99a3e") for x in (520, 850))}
{lamps}
<rect x="1640" y="300" width="18" height="520" fill="#07050a"/>
<rect x="1560" y="300" width="180" height="200" rx="10" fill="#0b070b" stroke="{NEON}" stroke-width="5"/>
{glow(1650, 400, 160, NEON, 0.4)}
<text x="1650" y="380" text-anchor="middle" font-family="{SANS}" font-weight="700" font-size="40" fill="{NEON}">MOTEL</text>
<text x="1650" y="440" text-anchor="middle" font-family="{SANS}" font-size="26" fill="#ff8a8f">VACANCY</text>
<path d="M0 820 L1920 820 L1920 1080 L0 1080Z" fill="#0a080d"/>
<g fill="#06040a"><path d="M700 900 L710 860 C720 845 740 840 760 840 L800 810 L960 810 L1000 840 L1060 846 C1080 850 1090 862 1090 880 L1090 900Z"/>
<circle cx="760" cy="904" r="28"/><circle cx="1030" cy="904" r="28"/></g>
{fog(860, "#8a87a8", 0.10, 60)}
''', sky("msky", "#04050c", "#140f26", "#2b1630")))

# Motel room interior: two beds, door on the left with light under it
def room(sitting=False, shadow=False):
    under = f'<rect x="250" y="846" width="250" height="10" fill="{WARM}"/><rect x="230" y="836" width="290" height="40" fill="{WARM}" opacity="0.45" filter="url(#blur8)"/>'
    shade = ''
    if shadow:
        shade = '<g fill="#050305"><rect x="300" y="846" width="40" height="10"/><rect x="390" y="846" width="44" height="10"/></g>'
    bed1 = '''<g><rect x="760" y="760" width="460" height="130" rx="10" fill="#1d1622"/>
<rect x="760" y="740" width="460" height="60" rx="18" fill="#2a2032"/><rect x="740" y="620" width="30" height="270" fill="#0e0a12"/>
<ellipse cx="840" cy="745" rx="60" ry="22" fill="#3a3044"/></g>'''
    bed2 = '''<g><rect x="1340" y="760" width="460" height="130" rx="10" fill="#1d1622"/>
<rect x="1340" y="740" width="460" height="60" rx="18" fill="#2a2032"/><rect x="1320" y="620" width="30" height="270" fill="#0e0a12"/>
<ellipse cx="1420" cy="745" rx="60" ry="22" fill="#3a3044"/></g>'''
    if sitting:
        boy = (kid(880, 770, 280, "#040205", cupped=False) + eyes(890, 770 - 280 + 34, 20, 5, "#ffe9d0") +
               '<rect x="860" y="770" width="360" height="40" rx="14" fill="#2a2032"/>')
    else:
        boy = '<path d="M820 742 C900 712 1060 716 1160 740 L1160 760 L820 760Z" fill="#33283c"/><circle cx="830" cy="728" r="26" fill="#120c14"/>'
    return svg(f'''
<rect width="{W}" height="{H}" fill="#0b0810"/>
<rect x="0" y="0" width="{W}" height="860" fill="#120d18"/>
<g opacity="0.25">{''.join(f'<rect x="{x}" y="0" width="4" height="860" fill="#2b2238"/>' for x in range(0, W, 60))}</g>
<rect x="0" y="856" width="{W}" height="224" fill="#0a070d"/>
<rect x="230" y="420" width="290" height="436" fill="#09060b"/>
<rect x="250" y="440" width="250" height="406" fill="#150f19"/>
<circle cx="470" cy="650" r="10" fill="#6b5a3a"/><rect x="370" y="480" width="18" height="10" rx="5" fill="#3a2f2a"/>
<rect x="485" y="600" width="12" height="30" fill="#3a2f2a"/>
{under}{shade}
<rect x="1100" y="280" width="200" height="240" fill="#1a1c2c"/><rect x="1100" y="280" width="200" height="240" fill="#2a3352" opacity="0.6"/>
<line x1="1200" y1="280" x2="1200" y2="520" stroke="#09060b" stroke-width="6"/>
<rect x="1080" y="270" width="240" height="20" fill="#09060b"/>
{glow(1200, 400, 140, "#6c7bb0", 0.15)}
{bed1}{bed2}{boy}
<path d="M1440 742 C1520 712 1680 716 1780 740 L1780 760 L1440 760Z" fill="#33283c"/><circle cx="1450" cy="728" r="26" fill="#120c14"/>
<rect x="1240" y="700" width="70" height="110" fill="#0e0a12"/><circle cx="1275" cy="690" r="14" fill="#c98a3a" opacity="0.4"/>
<path d="M250 860 L120 1080 L640 1080 L500 860Z" fill="{WARM}" opacity="0.05"/>
''')

save("s5", room())

# S6 — close on the gap under the door, something standing just outside
save("s6", svg(f'''
<rect width="{W}" height="{H}" fill="#08060b"/>
<rect x="0" y="0" width="{W}" height="700" fill="#120d18"/>
<rect x="560" y="0" width="800" height="700" fill="#150f19"/>
<rect x="540" y="0" width="20" height="700" fill="#09060b"/><rect x="1360" y="0" width="20" height="700" fill="#09060b"/>
<rect x="600" y="80" width="720" height="260" fill="none" stroke="#0d0911" stroke-width="10"/>
<rect x="600" y="380" width="720" height="260" fill="none" stroke="#0d0911" stroke-width="10"/>
<rect x="560" y="700" width="800" height="28" fill="{WARM}"/>
<rect x="520" y="680" width="880" height="70" fill="{WARM}" opacity="0.5" filter="url(#blur30)"/>
<g fill="#040205"><rect x="720" y="700" width="120" height="28"/><rect x="1060" y="700" width="120" height="28"/>
<path d="M880 700 L900 728 L920 700 L940 728 L960 700 L980 728 L1000 700Z" opacity="0.8"/></g>
<rect x="0" y="728" width="{W}" height="352" fill="#0a070d"/>
<path d="M560 728 L380 1080 L1540 1080 L1360 728Z" fill="{WARM}" opacity="0.08"/>
<g fill="#040205" opacity="0.85"><path d="M720 728 L640 1080 L780 1080 L840 728Z"/><path d="M1060 728 L1140 1080 L1280 1080 L1180 728Z"/></g>
'''))

# S7 — Danny sitting up in the dark, answering
save("s7", room(sitting=True, shadow=True))

# S8 — morning at a roadside diner booth, Danny smiling across the table
save("s8", svg(f'''
<rect width="{W}" height="{H}" fill="#1a1420"/>
<rect x="0" y="0" width="{W}" height="520" fill="url(#dawn)"/>
<g fill="#0c0910"><rect x="0" y="0" width="{W}" height="60"/>{''.join(f'<rect x="{x}" y="60" width="24" height="460"/>' for x in range(0, W, 420))}<rect x="0" y="500" width="{W}" height="30"/></g>
<path d="M0 470 L400 430 L800 450 L1300 420 L1920 450 L1920 500 L0 500Z" fill="#2a1626" opacity="0.8"/>
<rect x="560" y="520" width="800" height="560" rx="40" fill="#5a1a22"/>
<rect x="600" y="560" width="720" height="300" rx="30" fill="#6a2028"/>
{kid(960, 840, 360, "#0a070c", cupped=False)}
<path d="M936 546 Q960 560 984 546" stroke="#d9c8b8" stroke-width="4" fill="none"/>
<rect x="300" y="800" width="1320" height="280" fill="#2d2630"/><rect x="300" y="800" width="1320" height="16" fill="#8a7f86"/>
<ellipse cx="760" cy="880" rx="110" ry="30" fill="#e8e1d6"/><ellipse cx="760" cy="876" rx="60" ry="14" fill="#d9a44a"/>
<rect x="1110" y="830" width="70" height="80" rx="8" fill="#e8e1d6"/><path d="M1180 850 q30 10 0 40" stroke="#e8e1d6" stroke-width="10" fill="none"/>
{glow(1600, 260, 300, "#ffb88a", 0.18)}
''', sky("dawn", "#3a3550", "#7a5a6a", "#c8866a")))

# S8b — the last line: same picture, his eyes catch the light
save("s8b", svg(f'''
<rect width="{W}" height="{H}" fill="#120d16"/>
<rect x="0" y="0" width="{W}" height="520" fill="url(#dawn2)"/>
<g fill="#0a070d"><rect x="0" y="0" width="{W}" height="60"/>{''.join(f'<rect x="{x}" y="60" width="24" height="460"/>' for x in range(0, W, 420))}<rect x="0" y="500" width="{W}" height="30"/></g>
<rect x="560" y="520" width="800" height="560" rx="40" fill="#3a0f16"/>
<rect x="600" y="560" width="720" height="300" rx="30" fill="#45121a"/>
{kid(960, 840, 360, "#050305", cupped=False)}
{eyes(960, 518, 30, 7, "#ffe9d0")}
<path d="M930 544 Q960 566 990 544" stroke="#f0ddd0" stroke-width="5" fill="none"/>
<rect x="300" y="800" width="1320" height="280" fill="#1d181f"/><rect x="300" y="800" width="1320" height="16" fill="#5a5056"/>
<ellipse cx="760" cy="880" rx="110" ry="30" fill="#9a948a"/>
<rect x="1110" y="830" width="70" height="80" rx="8" fill="#9a948a"/>
{glow(960, 560, 260, NEON, 0.12)}
''', sky("dawn2", "#1a1626", "#3a2a3a", "#5a3a3a")))
