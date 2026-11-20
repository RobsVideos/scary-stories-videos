"""Scenes for 'The Quiet Kennels' — a night shift at a county animal shelter, forty dogs that suddenly go silent."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

r = random.Random(1120)

WARM = "#ffb04a"
FLUO = "#cfe6dc"
RED = "#ff3b2f"
CAM = "#9fd6b8"


def dog(cx, base, s=1.0, pose="sit", color="#06070a", eye=None, flip=False):
    """Dog silhouette, base = ground y. pose: sit | bark | cower."""
    g = []
    if pose == "bark":
        g.append('<ellipse cx="0" cy="-70" rx="95" ry="48"/>')                       # body
        g.append('<path d="M-80 -60 L-92 0 L-74 0 L-58 -50 Z"/><path d="M-40 -50 L-46 0 L-28 0 L-20 -50 Z"/>')
        g.append('<path d="M50 -60 L60 0 L78 0 L76 -60 Z"/><path d="M20 -50 L22 0 L40 0 L44 -50 Z"/>')
        g.append('<path d="M-90 -90 Q-130 -120 -140 -160" stroke-width="16" fill="none" stroke-linecap="round"/>')  # tail
        g.append('<path d="M60 -100 Q90 -140 100 -170 L130 -165 Q120 -120 92 -70 Z"/>')  # neck
        g.append('<ellipse cx="118" cy="-182" rx="40" ry="32"/>')                       # head
        g.append('<path d="M140 -200 L196 -214 L196 -200 L150 -186 Z"/>')                # upper jaw
        g.append('<path d="M145 -178 L188 -160 L186 -150 L140 -165 Z"/>')                # lower jaw (open)
        g.append('<path d="M100 -205 L92 -250 L122 -212 Z"/>')                           # ear
    elif pose == "cower":
        g.append('<ellipse cx="0" cy="-48" rx="100" ry="44"/>')
        g.append('<path d="M-70 -30 L-90 0 L-60 0 Z"/><path d="M60 -30 L90 0 L60 0 Z"/>')
        g.append('<ellipse cx="96" cy="-40" rx="42" ry="30"/>')
        g.append('<path d="M120 -40 L168 -26 L160 -14 L118 -22 Z"/>')
        g.append('<path d="M84 -58 L70 -40 L100 -50 Z"/>')
    else:  # sit
        g.append('<path d="M-60 0 C-80 -40 -70 -110 -30 -140 C-10 -160 30 -170 46 -150 C60 -120 60 -60 50 0 Z"/>')
        g.append('<ellipse cx="-40" cy="-30" rx="58" ry="40"/>')                         # haunch
        g.append('<path d="M20 -120 L22 0 L40 0 L44 -110 Z"/>')                           # front leg
        g.append('<ellipse cx="34" cy="-182" rx="36" ry="32"/>')                          # head
        g.append('<path d="M50 -190 L98 -178 L96 -162 L54 -166 Z"/>')                     # snout
        g.append('<path d="M14 -200 L4 -248 L36 -208 Z"/><path d="M40 -206 L44 -250 L58 -204 Z"/>')  # ears
        g.append('<path d="M-90 0 Q-120 -10 -110 -40" stroke-width="14" fill="none" stroke-linecap="round"/>')
    eyes_svg = ""
    if eye:
        ex, ey = (40, -190) if pose == "sit" else (120, -190)
        eyes_svg = (f'<circle cx="{ex}" cy="{ey}" r="5" fill="{eye}"/><circle cx="{ex + 18}" cy="{ey - 2}" r="5" fill="{eye}"/>'
                    f'<circle cx="{ex + 9}" cy="{ey}" r="16" fill="{eye}" opacity="0.55" filter="url(#blur8)"/>')
    sx = -s if flip else s
    return (f'<g transform="translate({cx} {base}) scale({sx} {s})" fill="{color}" stroke="{color}" stroke-width="0">'
            f'{"".join(g)}{eyes_svg}</g>')


def chainlink(id_, color="#8a978f", op=0.55, size=26):
    return (f'<pattern id="{id_}" width="{size}" height="{size}" patternUnits="userSpaceOnUse">'
            f'<path d="M0 0 L{size} {size} M{size} 0 L0 {size}" stroke="{color}" stroke-width="2" opacity="{op}"/></pattern>')


# ---------- kennel corridor (perspective) ----------
VX, VY = 960, 470          # vanishing point


def lerp(a, b, t): return a + (b - a) * t


def corridor(dogs_mode="bark", tint="#0d1714", last_open=False, feet=False, light_op=1.0):
    """Long kennel row seen from the office end. dogs_mode: bark | silent | cower | none."""
    out = []
    # walls / ceiling / floor
    out.append(f'<rect width="{W}" height="{H}" fill="{tint}"/>')
    out.append(f'<polygon points="0,0 {W},0 1080,400 840,400" fill="#0a100e"/>')
    out.append(f'<polygon points="0,1080 840,560 1080,560 {W},1080" fill="url(#floorG)"/>')
    # floor drain line + wet reflections
    out.append(f'<line x1="960" y1="560" x2="960" y2="1080" stroke="#050807" stroke-width="10" opacity="0.7"/>')
    out.append(f'<polygon points="900,560 1020,560 1200,1080 720,1080" fill="{FLUO}" opacity="{0.06 * light_op:.2f}"/>')
    out.append('<polygon points="0,0 440,120 440,1080 0,1080" fill="#060a09"/><polygon points="1920,0 1480,120 1480,1080 1920,1080" fill="#060a09"/>')
    # far end wall + door
    out.append('<rect x="840" y="400" width="240" height="160" fill="#101816"/>')
    out.append('<rect x="920" y="430" width="80" height="130" fill="#050707"/>')
    # kennels each side
    depths = [0.0, 0.42, 0.64, 0.78, 0.87, 0.93, 0.97]
    for side in (-1, 1):
        for i in range(len(depths) - 1):
            a, b = depths[i], depths[i + 1]
            xa = lerp(440 if side < 0 else 1480, 840 if side < 0 else 1080, a)
            xb = lerp(440 if side < 0 else 1480, 840 if side < 0 else 1080, b)
            ta, tb = lerp(0, 400, a), lerp(0, 400, b)
            ba, bb = lerp(1080, 560, a), lerp(1080, 560, b)
            ta, tb = ta + lerp(120, 30, a), tb + lerp(120, 30, b)
            quad = f"{xa:.0f},{ta:.0f} {xb:.0f},{tb:.0f} {xb:.0f},{bb:.0f} {xa:.0f},{ba:.0f}"
            out.append(f'<polygon points="{quad}" fill="#070b0a"/>')
            is_last = (i == len(depths) - 2 and side > 0)
            if is_last and last_open:
                out.append(f'<polygon points="{quad}" fill="#000"/>')
                # gate swung out into the aisle
                gx = xb - 60
                out.append(f'<polygon points="{xa:.0f},{ta:.0f} {gx:.0f},{ta + 4:.0f} {gx:.0f},{ba - 4:.0f} {xa:.0f},{ba:.0f}" fill="url(#link)" stroke="#9aa79f" stroke-width="3"/>')
            else:
                out.append(f'<polygon points="{quad}" fill="url(#link)"/>')
            out.append(f'<line x1="{xa:.0f}" y1="{ta:.0f}" x2="{xa:.0f}" y2="{ba:.0f}" stroke="#9aa79f" stroke-width="{lerp(14, 3, a):.0f}"/>')
            # dogs in the nearer kennels
            if i < 4 and dogs_mode != "none":
                sc = lerp(1.2, 0.25, (a + b) / 2)
                dx = (xa + xb) / 2 + (-10 if side < 0 else 10) * sc
                base = (ba + bb) / 2 - 20 * sc
                if dogs_mode == "bark":
                    out.append(dog(dx, base, sc * 0.85, "bark", "#030404", flip=(side > 0)))
                elif dogs_mode == "silent":
                    out.append(dog(dx, base, sc * 0.85, "sit", "#030404", eye="#d9f2a8", flip=(side > 0)))
                elif dogs_mode == "cower":
                    # pressed against the BACK of the kennel: smaller, higher, dimmer, eyes on the viewer
                    out.append(dog(dx + (-60 if side < 0 else 60) * sc, base - 60 * sc, sc * 0.75, "sit", "#020303",
                                   eye=RED, flip=(side < 0)))
    # fluorescent tubes
    for t in (0.18, 0.45, 0.68, 0.84):
        y = lerp(0, 400, t) + 20; w = lerp(300, 50, t)
        out.append(f'<rect x="{960 - w / 2:.0f}" y="{y:.0f}" width="{w:.0f}" height="{lerp(18, 4, t):.0f}" rx="4" fill="{FLUO}" opacity="{light_op:.2f}"/>')
        out.append(f'<ellipse cx="960" cy="{y + 10:.0f}" rx="{w:.0f}" ry="{lerp(80, 20, t):.0f}" fill="{FLUO}" opacity="{0.25 * light_op:.2f}" filter="url(#blur30)"/>')
    if feet:
        # wet bare footprints on the concrete, coming out of the last kennel toward us
        prints = [(1030, 600, 0.3), (995, 650, 0.4), (1035, 710, 0.52), (990, 790, 0.66), (1040, 890, 0.85)]
        for x, y, s in prints:
            out.append(f'<g transform="translate({x} {y}) scale({s})" fill="#c4dcd2" opacity="0.5">'
                       f'<ellipse cx="0" cy="0" rx="22" ry="44"/>'
                       + "".join(f'<circle cx="{-18 + k * 9}" cy="{-56 + abs(k - 2) * 4}" r="6"/>' for k in range(5)) + '</g>')
        # pale figure deep in the dark doorway
        out.append(glow(1040, 500, 90, "#b9c7c1", 0.22))
        out.append(f'<g opacity="0.85">{figure(1040, 600, 230, "#000")}</g>')
    out.append(fog(1000, "#9fb7ad", 0.08, 120))
    return "".join(out)


DEFS_CORR = (chainlink("link") +
             '<linearGradient id="floorG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1b2522"/>'
             '<stop offset="1" stop-color="#0c1311"/></linearGradient>')


# ---------- office ----------
def office(note=True, clock_time=(11, 50), screen=None, person=True):
    hx, mx = clock_time
    ha = (hx % 12 + mx / 60) * 30 - 90
    ma = mx * 6 - 90
    import math
    def hand(a, l, w): return (f'<line x1="0" y1="0" x2="{l * math.cos(math.radians(a)):.0f}" '
                               f'y2="{l * math.sin(math.radians(a)):.0f}" stroke="#15110c" stroke-width="{w}" stroke-linecap="round"/>')
    o = [f'<rect width="{W}" height="{H}" fill="#1a130d"/>',
         '<rect x="0" y="0" width="1920" height="700" fill="url(#wallO)"/>',
         # interior window into the kennel row (dark glass)
         '<rect x="560" y="150" width="520" height="330" fill="#0a1110"/>',
         f'<rect x="560" y="150" width="520" height="330" fill="url(#link)" opacity="0.35"/>',
         '<rect x="560" y="150" width="520" height="330" fill="none" stroke="#0b0805" stroke-width="16"/>',
         '<line x1="820" y1="150" x2="820" y2="480" stroke="#0b0805" stroke-width="10"/>',
         f'<rect x="600" y="180" width="140" height="8" fill="{FLUO}" opacity="0.4"/><rect x="880" y="190" width="100" height="6" fill="{FLUO}" opacity="0.3"/>',
         # leashes hanging on hooks
         ''.join(f'<path d="M{x} 300 q-6 120 10 200" stroke="{c}" stroke-width="7" fill="none"/><circle cx="{x}" cy="298" r="7" fill="#3a2f24"/>'
                 for x, c in ((1130, "#7a2a22"), (1160, "#2c4a5c"), (1190, "#6b5a2a"))),
         # clock
         f'<g transform="translate(1290 230)"><circle r="70" fill="#d9cfb7"/><circle r="70" fill="none" stroke="#3a2f24" stroke-width="8"/>'
         + "".join(f'<rect x="-2" y="-62" width="4" height="12" fill="#3a2f24" transform="rotate({k * 30})"/>' for k in range(12))
         + hand(ha, 36, 8) + hand(ma, 54, 5) + '<circle r="6" fill="#15110c"/></g>',
         # desk
         '<rect x="380" y="700" width="1180" height="40" fill="#2b1d12"/>',
         '<rect x="380" y="740" width="1180" height="340" fill="#140d08"/>',
         '<rect x="420" y="760" width="300" height="300" fill="#0f0a06"/><rect x="1220" y="760" width="300" height="300" fill="#0f0a06"/>',
         # papers, mug, clipboard
         '<rect x="1000" y="680" width="150" height="22" fill="#cfc6b2" transform="rotate(-4 1075 690)"/>',
         '<rect x="880" y="640" width="60" height="62" rx="8" fill="#5a2a22"/><path d="M940 655 q26 4 0 34" stroke="#5a2a22" stroke-width="8" fill="none"/>',
         # lamp
         '<path d="M1300 700 l-30 -10 l-20 -130 l50 -50" stroke="#0d0a07" stroke-width="10" fill="none"/><rect x="1250" y="690" width="90" height="14" rx="6" fill="#0d0a07"/>',
         '<path d="M1270 520 L1350 480 L1380 560 Z" fill="#1d1710"/>',
         glow(1330, 600, 150, WARM, 0.4),
         f'<polygon points="1340,540 1380,560 1420,700 1180,700" fill="{WARM}" opacity="0.2"/>',
         ]
    if note:
        o.append('<g transform="translate(220 280) rotate(-3 470 300)"><rect x="380" y="230" width="150" height="150" fill="#e8dfa4"/>'
                 f'<text x="455" y="282" text-anchor="middle" font-family="{SANS}" font-size="22" font-weight="bold" fill="#2a2418">IF THEY</text>'
                 f'<text x="455" y="312" text-anchor="middle" font-family="{SANS}" font-size="22" font-weight="bold" fill="#2a2418">GO QUIET</text>'
                 f'<text x="455" y="348" text-anchor="middle" font-family="{SANS}" font-size="18" fill="#8a1c14">STAY HERE</text></g>'
                 '<circle cx="675" cy="512" r="6" fill="#b3261e"/>')
    if screen is not None:
        o.append(screen)
    if person:
        # me, from behind, in the chair
        o.append('<g fill="#050403"><rect x="820" y="640" width="260" height="440" rx="40"/>'
                 '<ellipse cx="950" cy="600" rx="70" ry="82"/><path d="M820 720 Q950 650 1080 720 L1100 1080 L800 1080 Z"/></g>')
    o.append(f'<ellipse cx="960" cy="1040" rx="1100" ry="80" fill="#000" opacity="0.5" filter="url(#blur60)"/>')
    return "".join(o)


DEFS_OFF = (chainlink("link") +
            '<linearGradient id="wallO" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c1712"/>'
            '<stop offset="1" stop-color="#2b2117"/></linearGradient>')


# ---------- S1: shelter exterior ----------
fence = "".join(f'<line x1="{x}" y1="640" x2="{x}" y2="820" stroke="#121820" stroke-width="6"/>' for x in range(1180, 1760, 64))
s1 = f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(170, 520)}
{moon(560, 200, 70)}
<path d="M0 760 C400 720 900 740 1300 730 C1600 722 1800 740 1920 735 L1920 1080 L0 1080Z" fill="#11141c"/>
{dead_tree(300, 760, 380)}{dead_tree(1690, 740, 300, s=0.8)}
<g fill="#090b10">
<rect x="620" y="520" width="600" height="250"/>
<rect x="600" y="500" width="640" height="26"/>
<rect x="760" y="440" width="320" height="64"/>
</g>
<rect x="780" y="455" width="280" height="34" fill="#1b2230"/>
<text x="920" y="481" text-anchor="middle" font-family="{SANS}" font-size="22" font-weight="bold" fill="#8e9ab0" letter-spacing="3">ANIMAL SHELTER</text>
{lit_window(680, 590, 110, 80, WARM)}
<rect x="900" y="620" width="70" height="150" fill="#05060a"/>
<rect x="1060" y="600" width="90" height="60" fill="#151a24"/>
<rect x="1180" y="640" width="580" height="180" fill="url(#link)" opacity="0.8"/>
{fence}
<line x1="1180" y1="640" x2="1760" y2="640" stroke="#1a222c" stroke-width="6"/>
<g fill="#06070a">
<rect x="460" y="420" width="10" height="360"/><path d="M465 425 q40 -14 70 0" stroke="#06070a" stroke-width="8" fill="none"/>
</g>
{glow(535, 440, 90, "#ffd9a0", 0.35)}
<polygon points="520,440 550,440 640,800 430,800" fill="#ffd9a0" opacity="0.07"/>
<path d="M0 900 C600 860 1300 870 1920 880 L1920 1080 L0 1080Z" fill="#191b20"/>
<g stroke="#c9b25a" stroke-width="6" opacity="0.45" stroke-dasharray="80 70"><path d="M0 975 C600 950 1300 955 1920 965" fill="none"/></g>
{grass(880, 200, "#0b0d12")}
{fog(800, "#a9b6c8", 0.12)}
'''
save("s1", svg(s1, sky("sky1", "#04060c", "#141a2c", "#2a2a3a") + chainlink("link", "#2a3440", 0.9, 22)))

# ---------- S2: kennel row, barking ----------
save("s2", svg(corridor("bark"), DEFS_CORR))

# ---------- S3: office with the rule note ----------
save("s3", svg(office(note=True, clock_time=(11, 50), person=False), DEFS_OFF))

# ---------- S4: outdoor run at sunrise, dogs barking ----------
run_fence = "".join(f'<line x1="{x}" y1="560" x2="{x}" y2="900" stroke="#0a0a0f" stroke-width="10"/>' for x in range(300, 1700, 120))
s4 = f'''
<rect width="{W}" height="{H}" fill="url(#sky4)"/>
{stars(30, 250, 0.35)}
<circle cx="960" cy="700" r="320" fill="#ff9a5a" opacity="0.25" filter="url(#blur60)"/>
<circle cx="960" cy="730" r="90" fill="#ffc07a" opacity="0.85"/>
<path d="M0 720 C300 690 700 700 960 712 C1300 728 1600 690 1920 705 L1920 1080 L0 1080Z" fill="#170f16"/>
{dead_tree(1500, 720, 260, "#120b10", 0.8)}
<rect x="300" y="560" width="1400" height="340" fill="url(#link)"/>
{run_fence}
<line x1="300" y1="560" x2="1700" y2="560" stroke="#0a0a0f" stroke-width="10"/>
{dog(700, 900, 1.0, "bark", "#070508")}
{dog(1120, 900, 0.9, "bark", "#070508", flip=True)}
{dog(1380, 900, 0.75, "sit", "#070508")}
<rect x="0" y="895" width="{W}" height="185" fill="#0c080c"/>
{grass(900, 220, "#0c080c")}
{fog(880, "#d7a08a", 0.10)}
'''
save("s4", svg(s4, sky("sky4", "#0b0b1e", "#3a2140", "#b4584a") + chainlink("link", "#2a1c24", 0.9, 30)))

# ---------- S5: 3 a.m., all of them silent ----------
s5 = corridor("silent", tint="#0b1210", light_op=0.75) + \
    '<g transform="translate(960 150)"><circle r="62" fill="#d9cfb7"/><circle r="62" fill="none" stroke="#3a2f24" stroke-width="8"/>' + \
    "".join(f'<rect x="-2" y="-55" width="4" height="10" fill="#3a2f24" transform="rotate({k * 30})"/>' for k in range(12)) + \
    '<line x1="0" y1="0" x2="34" y2="0" stroke="#15110c" stroke-width="8" stroke-linecap="round"/>' \
    '<line x1="0" y1="0" x2="0" y2="-48" stroke="#15110c" stroke-width="5" stroke-linecap="round"/>' \
    f'<line x1="0" y1="0" x2="4" y2="-50" stroke="{RED}" stroke-width="2"/><circle r="6" fill="#15110c"/></g>'
save("s5", svg(s5, DEFS_CORR))

# ---------- S6: me at the desk, listening ----------
save("s6", svg(office(note=True, clock_time=(3, 2), person=True), DEFS_OFF))

# ---------- S7: last gate open, wet footprints ----------
save("s7", svg(corridor("silent", tint="#091010", last_open=True, feet=True, light_op=0.55), DEFS_CORR))


# ---------- S8 / S8b: the security monitor ----------
def cam_view(with_it=False):
    """Grainy overhead CCTV image of the office, drawn into a 760x440 box."""
    v = ['<rect width="760" height="440" fill="#0d1a14"/>',
         '<rect x="0" y="0" width="760" height="440" fill="url(#scan)"/>',
         # desk from above-behind
         '<polygon points="140,300 620,300 700,440 60,440" fill="#24382d"/>',
         '<rect x="250" y="240" width="260" height="60" fill="#162a20"/>',      # monitor on desk
         '<rect x="262" y="250" width="236" height="40" fill="#5aa47c" opacity="0.6"/>',
         # me in chair
         '<g fill="#07100b"><rect x="300" y="300" width="160" height="140" rx="20"/><ellipse cx="380" cy="300" rx="44" ry="50"/>'
         '<path d="M300 360 Q380 320 460 360 L470 440 L290 440 Z"/></g>',
         # wall + door
         '<rect x="0" y="0" width="760" height="230" fill="#13241b"/>',
         '<rect x="560" y="40" width="110" height="190" fill="#06100a"/>',
         ]
    if with_it:
        v.append('<g fill="#000">'
                 # tall thin body behind the chair, head bent above mine
                 '<path d="M410 440 L420 200 C418 150 440 120 470 118 C500 120 516 150 512 200 L520 440 Z"/>'
                 '<ellipse cx="470" cy="80" rx="34" ry="46"/>'
                 # long arm folding up, one finger to its lips
                 '<path d="M500 160 C560 180 560 120 500 96" stroke="#000" stroke-width="16" fill="none" stroke-linecap="round"/>'
                 '<path d="M496 100 L486 64" stroke="#000" stroke-width="7" stroke-linecap="round"/>'
                 # other arm hanging long to the floor
                 '<path d="M428 170 C400 260 396 340 400 420" stroke="#000" stroke-width="14" fill="none" stroke-linecap="round"/>'
                 '</g>'
                 f'<circle cx="459" cy="76" r="4" fill="{RED}"/><circle cx="481" cy="76" r="4" fill="{RED}"/>'
                 f'<circle cx="470" cy="76" r="16" fill="{RED}" opacity="0.5" filter="url(#blur8)"/>')
    v.append(f'<text x="18" y="34" font-family="{MONO}" font-size="24" fill="{CAM}">CAM 4  OFFICE</text>')
    v.append(f'<text x="742" y="34" text-anchor="end" font-family="{MONO}" font-size="24" fill="{CAM}">03:07</text>')
    v.append(f'<circle cx="24" cy="416" r="8" fill="{RED}"/><text x="40" y="424" font-family="{MONO}" font-size="20" fill="{RED}">REC</text>')
    return "".join(v)


def monitor_scene(with_it):
    return f'''
<rect width="{W}" height="{H}" fill="#070806"/>
<rect x="0" y="760" width="{W}" height="320" fill="#120c07"/>
<rect x="0" y="750" width="{W}" height="20" fill="#24180e"/>
<g transform="translate(540 190)">
<rect x="-40" y="-40" width="920" height="560" rx="26" fill="#121412"/>
<rect x="0" y="0" width="840" height="480" rx="10" fill="#020403"/>
<g transform="translate(40 20)">{cam_view(with_it)}</g>
<rect x="0" y="0" width="840" height="480" rx="10" fill="#9fd6b8" opacity="0.05"/>
<rect x="380" y="520" width="80" height="60" fill="#121412"/><rect x="300" y="575" width="240" height="18" rx="8" fill="#121412"/>
</g>
{glow(960, 430, 420, "#7fd6a8", 0.12)}
<polygon points="580,710 1340,710 1500,1080 420,1080" fill="#7fd6a8" opacity="0.05"/>
<g fill="#030302"><rect x="300" y="700" width="160" height="60" rx="6"/><rect x="1450" y="640" width="70" height="120" rx="10"/></g>
'''


SCAN = ('<pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">'
        '<rect width="4" height="2" fill="#000" opacity="0.25"/></pattern>')
save("s8", svg(monitor_scene(False), SCAN))
save("s8b", svg(monitor_scene(True), SCAN))

# ---------- S9: every dog pressed to the back of its kennel ----------
save("s9", svg(corridor("cower", tint="#0e0a0a", light_op=0.45) + glow(960, 560, 300, "#b3261e", 0.12), DEFS_CORR))
print("ok")
