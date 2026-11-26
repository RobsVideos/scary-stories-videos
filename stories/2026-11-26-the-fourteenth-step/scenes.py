"""Scenes for The Fourteenth Step."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

# ---------- S1: the little rental house at night ----------
clap = "".join(f'<line x1="640" y1="{y}" x2="1280" y2="{y}" stroke="#0d0c14" stroke-width="3"/>' for y in range(520, 820, 22))
logs = "".join(f'<circle cx="{x}" cy="{y}" r="17" fill="#2a1c14"/><circle cx="{x}" cy="{y}" r="9" fill="#3d2a1c"/>'
               for y in (790, 760, 730) for x in range(1340, 1500 - (790 - y), 36))
s1 = f'''
<rect width="{W}" height="{H}" fill="url(#sk1)"/>
{stars(150, 560)}
{moon(1500, 220, 95)}
<path d="M0 780 C400 740 800 760 1200 750 C1500 744 1700 760 1920 750 L1920 1080 L0 1080Z" fill="#161327"/>
{dead_tree(380, 800, 440)}{dead_tree(1660, 790, 360, s=0.8)}
<g fill="#0b0a12">
<polygon points="620,820 620,520 960,330 1300,520 1300,820"/>
<rect x="1110" y="360" width="46" height="110"/>
</g>
<g fill="#13111c" opacity="0.9"><polygon points="640,820 640,525 960,352 1280,525 1280,820"/></g>
{clap}
<polygon points="600,530 960,322 1320,530 1300,540 960,346 620,540" fill="#06050a"/>
{lit_window(700, 580, 100, 120)}
{lit_window(1120, 580, 100, 120, "#e9a24a")}
<rect x="900" y="620" width="120" height="200" fill="#0a090f"/>
<circle cx="1000" cy="725" r="5" fill="#a7853f"/>
<circle cx="960" cy="600" r="8" fill="#ffd28a"/>{glow(960, 605, 60, "#ffcf7a", 0.5)}
<polygon points="880,820 1040,820 1080,850 840,850" fill="#1f1a26"/>
<g transform="translate(470 820)">
<polygon points="0,0 150,0 150,-70 0,-40" fill="#1e1712"/>
<line x1="75" y1="0" x2="75" y2="-55" stroke="#0c0806" stroke-width="4"/>
<circle cx="60" cy="-28" r="4" fill="#6a5430"/><circle cx="90" cy="-30" r="4" fill="#6a5430"/>
</g>
{logs}
<path d="M0 900 C500 870 1300 890 1920 875 L1920 1080 L0 1080Z" fill="#0f0c1c"/>
{grass(900, 220, "#0d0b18")}{grass(1080, 260, "#07060d", (20, 50))}
{fog(840, op=0.12)}
'''
save("s1", svg(s1, sky("sk1", "#05060f", "#1b1638", "#3b2343")))

# ---------- S2: the cellar door with the taped rule ----------
s2 = f'''
<rect width="{W}" height="{H}" fill="#1a1210"/>
<g stroke="#140d0b" stroke-width="3" opacity="0.7">{"".join(f'<line x1="{x}" y1="0" x2="{x}" y2="860"/>' for x in range(0, 1920, 64))}</g>
<rect x="0" y="860" width="{W}" height="220" fill="#24170f"/>
<g stroke="#140c08" stroke-width="3">{"".join(f'<line x1="0" y1="{y}" x2="1920" y2="{y}"/>' for y in (900, 950, 1010))}</g>
<rect x="0" y="600" width="520" height="40" fill="#2e2018"/><rect x="0" y="640" width="500" height="220" fill="#1b120d"/>
<rect x="30" y="670" width="200" height="160" fill="none" stroke="#120b08" stroke-width="6"/><rect x="260" y="670" width="200" height="160" fill="none" stroke="#120b08" stroke-width="6"/>
<path d="M120 600 v-60 h60 v60" fill="#3a3530"/><rect x="300" y="520" width="90" height="80" rx="10" fill="#2a2420"/>
<rect x="1460" y="250" width="300" height="300" fill="#0d1022"/>
<rect x="1460" y="250" width="300" height="300" fill="#9fb4e8" opacity="0.15"/>
{moon(1560, 330, 30)}
<line x1="1610" y1="250" x2="1610" y2="550" stroke="#1a1210" stroke-width="10"/><line x1="1460" y1="400" x2="1760" y2="400" stroke="#1a1210" stroke-width="10"/>
<rect x="1450" y="240" width="320" height="320" fill="none" stroke="#2a1d16" stroke-width="16"/>
<rect x="770" y="190" width="380" height="670" fill="#2b1b13"/>
<rect x="750" y="175" width="420" height="20" fill="#1c120d"/><rect x="750" y="175" width="20" height="685" fill="#1c120d"/><rect x="1150" y="175" width="20" height="685" fill="#1c120d"/>
<rect x="820" y="240" width="280" height="250" fill="none" stroke="#1d120d" stroke-width="8"/>
<rect x="820" y="540" width="280" height="270" fill="none" stroke="#1d120d" stroke-width="8"/>
<circle cx="1110" cy="525" r="14" fill="#a7853f"/><rect x="1095" y="560" width="30" height="40" rx="4" fill="#5e4318"/>
<g transform="rotate(-3 960 380)">
<rect x="860" y="290" width="200" height="180" fill="#d9cfb4"/>
<rect x="900" y="280" width="60" height="22" fill="#cfc39a" opacity="0.8" transform="rotate(-8 930 290)"/>
<text x="960" y="345" text-anchor="middle" font-family="{SERIF}" font-size="30" font-weight="bold" fill="#2a1d14">COUNT</text>
<text x="960" y="385" text-anchor="middle" font-family="{SERIF}" font-size="30" font-weight="bold" fill="#2a1d14">THE STEPS</text>
<text x="960" y="440" text-anchor="middle" font-family="{SERIF}" font-size="34" font-weight="bold" fill="#8c1c1c">NEVER 14</text>
</g>
<rect x="770" y="850" width="380" height="10" fill="#0a0604"/>
{glow(400, 120, 200, "#ffae4a", 0.12)}
<polygon points="770,860 1150,860 1250,1080 670,1080" fill="#000" opacity="0.25"/>
'''
save("s2", svg(s2))

# ---------- S3 / S4: looking down the thirteen steps ----------
def stairs(lit=True):
    out = []
    n = 13
    for i in range(n):
        t0, t1 = i / n, (i + 1) / n
        y0 = 1080 - t0 * 640; y1 = 1080 - t1 * 640
        hw0 = 520 - t0 * 330; hw1 = 520 - t1 * 330
        col = f"#{int(0x4a - i * 2.4):02x}{int(0x32 - i * 1.7):02x}{int(0x22 - i * 1.2):02x}" if lit else f"#{int(0x22 - i):02x}{int(0x18 - i * .7):02x}{int(0x14 - i * .6):02x}"
        out.append(f'<polygon points="{960 - hw0:.0f},{y0:.0f} {960 + hw0:.0f},{y0:.0f} {960 + hw1:.0f},{y1:.0f} {960 - hw1:.0f},{y1:.0f}" fill="{col}"/>')
        out.append(f'<rect x="{960 - hw0:.0f}" y="{y0 - 9:.0f}" width="{2 * hw0:.0f}" height="9" fill="#0d0806" opacity="0.8"/>')
    return "".join(out)

base_stairs = f'''
<rect width="{W}" height="{H}" fill="#0a0706"/>
<polygon points="0,0 770,440 770,1080 0,1080" fill="#1c1310"/>
<polygon points="1920,0 1150,440 1150,1080 1920,1080" fill="#1a110e"/>
<g stroke="#120c0a" stroke-width="3" opacity="0.6">{"".join(f'<line x1="{x}" y1="{x * 440 / 770:.0f}" x2="{x}" y2="1080"/>' for x in range(60, 770, 80))}</g>
<rect x="770" y="440" width="380" height="0" fill="#000"/>
<rect x="790" y="300" width="340" height="150" fill="#050303"/>
'''
woodpile = "".join(f'<circle cx="{x}" cy="{y}" r="13" fill="#4a3220"/><circle cx="{x}" cy="{y}" r="6" fill="#6a4a30"/>' for y in (420, 398) for x in range(850, 1080, 28))
s3 = base_stairs + f'''
<g>{woodpile}</g>
{glow(960, 380, 150, "#ffb54a", 0.25)}
{stairs(True)}
<line x1="960" y1="0" x2="960" y2="150" stroke="#0a0706" stroke-width="4"/>
<path d="M948 150 h24 v18 h-24z" fill="#2a2420"/>
<circle cx="960" cy="185" r="22" fill="#ffd28a"/>{glow(960, 185, 120, "#ffc56a", 0.55)}
<polygon points="960,190 1480,1080 440,1080" fill="#ffc56a" opacity="0.08"/>
<rect x="430" y="440" width="14" height="640" fill="#2e1f16" transform="skewX(-28) translate(240 0)"/>
'''
save("s3", svg(s3))

s4 = base_stairs + f'''
<rect width="{W}" height="{H}" fill="#000" opacity="0.3"/>
{stairs(False)}
<line x1="960" y1="0" x2="960" y2="150" stroke="#050303" stroke-width="4"/>
<path d="M948 150 h24 v18 h-24z" fill="#1a1612"/><circle cx="960" cy="185" r="22" fill="#2a2420"/>
<polygon points="900,1080 1040,1080 1110,520 830,520" fill="#e8ecff" opacity="0.13"/>
<ellipse cx="970" cy="540" rx="150" ry="40" fill="#e8ecff" opacity="0.18" filter="url(#blur30)"/>
<ellipse cx="960" cy="420" rx="160" ry="60" fill="#000" opacity="0.9" filter="url(#blur30)"/>
<g fill="#06040a">
<path d="M700 1080 C700 990 760 960 820 960 L900 960 C940 960 950 1000 930 1030 L900 1080Z"/>
<path d="M1220 1080 C1220 990 1160 960 1100 960 L1020 960 C980 960 970 1000 990 1030 L1020 1080Z"/>
</g>
{glow(960, 300, 260, "#5a1010", 0.25)}
'''
save("s4", svg(s4))

# ---------- S5: the soft step ----------
st = []
for i in range(8):
    x0 = 300 + i * 190; y = 900 - i * 105
    st.append(f'<rect x="{x0}" y="{y}" width="{1920 - x0}" height="22" fill="#4a3220"/>'
              f'<rect x="{x0}" y="{y + 22}" width="{1920 - x0}" height="{1080 - y}" fill="#21150e"/>'
              f'<line x1="{x0}" y1="{y + 22}" x2="{x0}" y2="1080" stroke="#0d0806" stroke-width="4"/>')
s5 = f'''
<rect width="{W}" height="{H}" fill="#070405"/>
<rect x="0" y="900" width="{W}" height="180" fill="#120b09"/>
{"".join(st)}
<polygon points="1500,0 1900,0 1100,1080 500,1080" fill="#e8ecff" opacity="0.05"/>
<ellipse cx="620" cy="905" rx="420" ry="70" fill="#8a1a14" opacity="0.35" filter="url(#blur30)"/>
<path d="M260 905 C280 800 400 740 560 735 C720 730 860 770 940 830 C990 870 1000 905 980 908 Z" fill="#140c10"/>
<path d="M300 900 C330 830 430 790 560 788 C700 786 820 820 900 870" fill="none" stroke="#5a2a30" stroke-width="5" opacity="0.7"/>
<path d="M350 902 C380 860 460 835 570 834 C680 833 780 855 850 890" fill="none" stroke="#5a2a30" stroke-width="4" opacity="0.5"/>
<path d="M300 790 C380 740 520 728 640 736" fill="none" stroke="#c24a3a" stroke-width="3" opacity="0.5"/>
<g fill="#b9aeb8" opacity="0.45">
<path d="M262 905 c-14 -26 -8 -50 10 -58 c6 18 8 40 -2 58z"/>
<path d="M290 906 c-12 -30 -2 -56 16 -62 c4 22 4 42 -6 62z"/>
<path d="M322 906 c-8 -30 2 -52 18 -56 c2 20 0 40 -8 56z"/>
</g>
<g fill="#181c2c">
<path d="M560 0 L520 560 C515 640 530 700 545 730 L700 730 C700 700 690 650 690 560 L720 0Z"/></g>
<path d="M720 0 L690 560 C690 650 700 700 700 730" fill="none" stroke="#5a6690" stroke-width="5" opacity="0.5"/>
<g fill="#100a08">
<path d="M520 700 C500 700 470 720 470 750 L470 775 L760 775 C780 775 790 760 780 745 C770 730 720 720 690 715 Z"/>
</g>
<path d="M520 700 C500 700 470 720 470 750" fill="none" stroke="#8a5a3a" stroke-width="4" opacity="0.6"/>
{eyes(250, 790, 30, 5)}
{glow(620, 820, 260, "#7a1010", 0.18)}
'''
save("s5", svg(s5))

# ---------- S6: door slammed, chair under the knob ----------
s6 = s2.replace('fill="#9fb4e8" opacity="0.15"', 'fill="#9fb4e8" opacity="0.08"').replace(glow(400, 120, 200, "#ffae4a", 0.12), "") + f'''
<rect width="{W}" height="{H}" fill="#000" opacity="0.35"/>
<rect x="770" y="852" width="380" height="8" fill="#ff3b2f" opacity="0.8"/>
<rect x="760" y="846" width="400" height="20" fill="#ff3b2f" opacity="0.5" filter="url(#blur8)"/>
<polygon points="770,860 1150,860 1260,1080 660,1080" fill="#ff3b2f" opacity="0.08"/>
<g fill="#08050a" stroke="#08050a" stroke-linecap="round">
<polygon points="1000,700 1260,700 1290,730 1030,730"/>
<line x1="1035" y1="725" x2="1010" y2="900" stroke-width="22"/><line x1="1280" y1="725" x2="1300" y2="900" stroke-width="22"/>
<line x1="1100" y1="730" x2="1090" y2="870" stroke-width="16"/>
<line x1="1240" y1="710" x2="1130" y2="540" stroke-width="22"/><line x1="1020" y1="705" x2="1110" y2="540" stroke-width="18"/>
<line x1="1120" y1="540" x2="1112" y2="530" stroke-width="26"/>
</g>
'''
save("s6", svg(s6))

# ---------- S7: the phone call ----------
s7 = f'''
<rect width="{W}" height="{H}" fill="#07070b"/>
<rect x="0" y="700" width="{W}" height="380" fill="#1c130e"/>
<g stroke="#120b07" stroke-width="3">{"".join(f'<line x1="{x}" y1="700" x2="{x * 1.3 - 288:.0f}" y2="1080"/>' for x in range(0, 1920, 120))}</g>
<rect x="0" y="690" width="{W}" height="14" fill="#2c1e15"/>
<g transform="translate(560 560)"><path d="M0 0 h110 v120 c0 30 -110 30 -110 0z" fill="#2a2a32"/><path d="M110 30 c40 0 40 60 0 60" fill="none" stroke="#2a2a32" stroke-width="12"/></g>
<ellipse cx="620" cy="700" rx="90" ry="10" fill="#000" opacity="0.5"/>
{glow(980, 450, 330, "#7fa0ff", 0.22)}
<g transform="rotate(8 980 470)">
<rect x="850" y="170" width="260" height="520" rx="34" fill="#0c0c10"/>
<rect x="866" y="200" width="228" height="460" rx="18" fill="#101a2e"/>
<rect x="866" y="200" width="228" height="460" rx="18" fill="#3a5aa0" opacity="0.4"/>
<circle cx="980" cy="320" r="48" fill="#5d6f96"/><circle cx="980" cy="305" r="18" fill="#2a3550"/><path d="M948 350 c10 -30 54 -30 64 0" fill="#2a3550"/>
<text x="980" y="410" text-anchor="middle" font-family="{SANS}" font-size="30" fill="#e6ecff">Landlord</text>
<text x="980" y="450" text-anchor="middle" font-family="{MONO}" font-size="24" fill="#b8c4e6">03:12</text>
<circle cx="980" cy="590" r="34" fill="#d23a30"/>
</g>
<g fill="#0a0708">
<path d="M760 1080 C770 900 820 760 880 640 C900 600 950 600 960 640 L1000 760 C1060 700 1120 690 1140 720 C1160 760 1120 860 1060 960 L1040 1080Z"/>
<rect x="870" y="560" width="50" height="160" rx="25" transform="rotate(-18 895 640)"/>
<rect x="1060" y="420" width="44" height="120" rx="22" transform="rotate(20 1080 480)"/>
<rect x="1080" y="520" width="44" height="120" rx="22" transform="rotate(15 1100 580)"/>
</g>
{fog(1000, "#6a7aa0", 0.08)}
'''
save("s7", svg(s7))

# ---------- S8: the kitchen floor breathes ----------
boards = []
for i in range(14):
    y0 = 560 + i * 40 + i * i * 2.2
    boards.append(f'<line x1="0" y1="{y0:.0f}" x2="{W}" y2="{y0:.0f}" stroke="#0e0805" stroke-width="{2 + i * 0.4:.1f}"/>')
s8 = f'''
<rect width="{W}" height="{H}" fill="#08060a"/>
<rect x="0" y="0" width="{W}" height="560" fill="#140e10"/>
<rect x="760" y="120" width="400" height="440" fill="#1a1012"/>
<rect x="770" y="552" width="380" height="8" fill="#ff3b2f" opacity="0.5"/>
<rect x="0" y="560" width="{W}" height="520" fill="url(#fl8)"/>
{"".join(boards)}
<path d="M560 865 C700 820 1220 820 1360 865 L1360 905 C1220 885 700 885 560 905 Z" fill="#3a2418"/>
<path d="M560 905 C700 885 1220 885 1360 905" fill="none" stroke="#050303" stroke-width="10"/>
<path d="M600 900 C760 890 1160 890 1320 900" fill="none" stroke="#ff3b2f" stroke-width="4" opacity="0.6"/>
{glow(960, 900, 160, "#b01a12", 0.35)}
{eyes(930, 905, 44, 6)}
<g fill="#050304" stroke="#050304" stroke-linecap="round">
<rect x="820" y="420" width="300" height="30" rx="8"/>
<line x1="840" y1="440" x2="800" y2="880" stroke-width="22"/><line x1="1100" y1="440" x2="1140" y2="880" stroke-width="22"/>
<line x1="880" y1="440" x2="870" y2="760" stroke-width="16"/><line x1="1060" y1="440" x2="1070" y2="760" stroke-width="16"/>
<line x1="830" y1="430" x2="820" y2="80" stroke-width="20"/><line x1="1110" y1="430" x2="1120" y2="80" stroke-width="20"/>
<line x1="825" y1="180" x2="1115" y2="180" stroke-width="16"/><line x1="825" y1="300" x2="1115" y2="300" stroke-width="16"/>
<path d="M880 420 C870 340 900 300 960 300 C1030 300 1060 340 1050 420Z" opacity="0.0"/>
</g>
{fog(1040, "#5a1010", 0.15, 90)}
'''
save("s8", svg(s8, '<linearGradient id="fl8" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a110c"/><stop offset="1" stop-color="#2e1d12"/></linearGradient>'))
print("ok")
