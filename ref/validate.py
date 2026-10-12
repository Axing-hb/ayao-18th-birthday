# -*- coding: utf-8 -*-
"""校验 manifest.json：路径存在性、文件可读性、图片可解析性、统计。"""
import json
import sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
MANIFEST = json.loads((ASSETS / "manifest.json").read_text(encoding="utf-8"))

errors = []
warns = []

# 1. 路径存在 + 可解析
checked = 0
for it in MANIFEST["images"]:
    p = ROOT / "assets" / it["rel"]
    if not p.exists():
        errors.append(f"missing image: {it['rel']}")
        continue
    checked += 1
    try:
        with Image.open(p) as im:
            w, h = im.size
        if (w, h) != (it["w"], it["h"]):
            warns.append(f"size mismatch {it['rel']}: manifest {it['w']}x{it['h']} vs actual {w}x{h}")
    except Exception as e:
        errors.append(f"unreadable image {it['rel']}: {e}")

for d in MANIFEST["deco"]:
    p = ROOT / "assets" / d["rel"]
    if not p.exists():
        errors.append(f"missing deco: {d['rel']}")
    else:
        checked += 1

for f in MANIFEST["fonts"]["files"]:
    p = ROOT / "assets" / f["rel"]
    if not p.exists():
        errors.append(f"missing font: {f['rel']}")
    else:
        checked += 1

# 2. counts 一致性
if MANIFEST["counts"]["images"] != len(MANIFEST["images"]):
    errors.append("counts.images mismatch")
if MANIFEST["counts"]["deco_svg"] != len(MANIFEST["deco"]):
    errors.append("counts.deco_svg mismatch")
if MANIFEST["counts"]["fonts"] != len(MANIFEST["fonts"]["files"]):
    errors.append("counts.fonts mismatch")

# 3. 迪拉熊约束（S1 只能出现两只）
DILLA_MAX = 2
dilla_personal = [i for i in MANIFEST["images"]
                  if i["group"] == "personal" and "dilla_plush" in i["rel"]
                  and i["rel"] not in ("personal/dilla_plush_pair.webp",)]
if not dilla_personal:
    errors.append("no personal dilla plush assets found")
constraint = MANIFEST["constraints"]
for key in ("dilla_bears_files", "dilla_bears_fallback"):
    for c in constraint.get(key, []):
        if not (ROOT / "assets" / c.replace("../assets/", "")).exists():
            errors.append(f"constraint {key} file missing: {c}")
if constraint.get("dilla_bears_max") != DILLA_MAX:
    errors.append(f"dilla_bears_max should be {DILLA_MAX}")

# 3b. 私人照片必须齐全且被 S1/S7 引用
PERSONAL_REQUIRED = {
    "personal/us_switch.webp": "S7",
    "personal/us_switch_square.webp": "S2",
    "personal/dilla_plush_pair.webp": "S1",
    "personal/dilla_plush_big.webp": "S1",
    "personal/dilla_plush_small.webp": "S1",
    "personal/hamster_avatar.webp": "S6",
    "personal/hamster_face.webp": "S5",
    "personal/hamster_ball.webp": "S3",
    "personal/hamster_cage.webp": "S6",
}
sec_assets = {s["id"]: set(s["assets"]) for s in MANIFEST["sections"]}
for rel, sid in PERSONAL_REQUIRED.items():
    if not (ASSETS / rel).exists():
        errors.append(f"missing personal photo: {rel}")
    if f"../assets/{rel}" not in sec_assets.get(sid, set()):
        errors.append(f"personal photo {rel} not referenced by section {sid}")

# 4. MARETU 10 首齐备
tracks = sorted([i for i in MANIFEST["images"] if i["group"] == "marettu"], key=lambda x: x.get("track_no", 99))
if len(tracks) != 10:
    errors.append(f"marettu track count = {len(tracks)}, expected 10")
for n, t in enumerate(tracks, 1):
    if t.get("track_no") != n:
        errors.append(f"marettu track order broken at #{n}: {t['rel']}")
    if not t.get("title_romaji"):
        errors.append(f"marettu missing romaji: {t['rel']}")
    if not t.get("title"):
        errors.append(f"marettu missing japanese title: {t['rel']}")

# 4b. 部署就绪：文件名必须纯 ASCII（GitHub Pages 会对非 ASCII 做 URL 编码，有 404 风险）
non_ascii = [p for p in ASSETS.rglob("*")
             if p.is_file() and any(ord(ch) > 127 for ch in p.name)]
if non_ascii:
    errors.append(f"{len(non_ascii)} files with non-ASCII names (breaks GitHub Pages):")
    for p in non_ascii[:10]:
        errors.append(f"    {p.relative_to(ASSETS)}")

# 4c. 部署就绪：文件名不得含大写（GitHub Pages 大小写敏感，易踩坑）
upper = [p for p in ASSETS.rglob("*")
         if p.is_file() and p.name != p.name.lower() and p.name not in ("README.md",)]
if upper:
    warns.append(f"{len(upper)} files with uppercase in name (case-sensitive on GitHub Pages)")
    for p in upper[:5]:
        warns.append(f"    {p.relative_to(ASSETS)}")

# 4d. 部署就绪：_raw 备份不应上传（由 .gitignore 排除）
gi = ROOT / ".gitignore"
if not gi.exists():
    errors.append("missing .gitignore (should exclude assets/_raw/)")
else:
    txt = gi.read_text(encoding="utf-8")
    if "_raw" not in txt:
        errors.append(".gitignore does not exclude assets/_raw/")

# 4e. 部署就绪：3D 蛋糕允许用 Three.js，但 manifest 要标明
dep = MANIFEST["constraints"].get("deploy", {})
if not dep.get("three_js"):
    warns.append("deploy.three_js is false — 3D cake is expected to use Three.js on github.io")
if "by Axing" not in MANIFEST["constraints"].get("footer_credit", ""):
    errors.append("footer_credit should be 'by Axing'")
if MANIFEST["constraints"].get("age") != 18:
    errors.append("constraints.age should be 18")

# 5. sections 引用的素材都存在
for s in MANIFEST["sections"]:
    for a in s["assets"]:
        rel = a.replace("../assets/", "")
        if not (ASSETS / rel).exists():
            errors.append(f"section {s['id']} references missing asset: {a}")

# 5b. 音频
if not MANIFEST.get("audio"):
    errors.append("no audio registered")
for a in MANIFEST.get("audio", []):
    p = ROOT / "assets" / a["rel"]
    if not p.exists():
        errors.append(f"missing audio: {a['rel']}")
    elif p.stat().st_size != a["bytes"]:
        errors.append(f"audio size mismatch: {a['rel']}")

# 5c. 18 岁生日必须写进配置
if MANIFEST["recipient"].get("age") != 18:
    errors.append("recipient.age should be 18")

# 5d. 她喜欢的村民 / 宝可梦必须在册且被引用
FAVORITES_REQUIRED = {
    "acnh/sasha_mixueer.webp": "S4",
    "acnh/fang_shipeiya.webp": "S4",
    "pokemon/sylveon_700.webp": "S5",
    "pokemon/lycanroc_745_midday.webp": "S5",
    "pokemon/lycanroc_10126_midnight.webp": "S5",
    "pokemon/lycanroc_10152_dusk.webp": "S5",
    "pokemon/zacian_888.webp": "S5",
    "pokemon/zamazenta_889.webp": "S5",
    "pokemon/eternatus_890.webp": "S5",
    "pokemon/vaporeon_134.webp": "S5",
    "pokemon/jolteon_135.webp": "S5",
    "pokemon/flareon_136.webp": "S5",
    "pokemon/espeon_196.webp": "S5",
    "pokemon/umbreon_197.webp": "S5",
    "pokemon/leafeon_470.webp": "S5",
    "pokemon/glaceon_471.webp": "S5",
}
for rel, sid in FAVORITES_REQUIRED.items():
    if not (ASSETS / rel).exists():
        errors.append(f"missing favorite asset: {rel}")
    if f"../assets/{rel}" not in sec_assets.get(sid, set()):
        errors.append(f"favorite asset {rel} not referenced by section {sid}")

# 5e. 伊布家族必须 9 只齐全
EEVEE_FAMILY = ["eevee_133", "vaporeon_134", "jolteon_135", "flareon_136",
                "espeon_196", "umbreon_197", "leafeon_470", "glaceon_471", "sylveon_700"]
for e in EEVEE_FAMILY:
    if not (ASSETS / "pokemon" / f"{e}.webp").exists():
        errors.append(f"missing eevee family member: {e}")

# 5g. Three.js vendor
if not MANIFEST.get("vendor"):
    errors.append("no vendor library registered (Three.js expected for 3D cake)")
for v in MANIFEST.get("vendor", []):
    p = ROOT / "assets" / v["rel"]
    if not p.exists():
        errors.append(f"missing vendor file: {v['rel']}")
    elif p.stat().st_size < 100_000:
        errors.append(f"vendor file suspiciously small: {v['rel']} ({p.stat().st_size} B)")

# 5h. 部署入口页
root_index = ROOT / "index.html"
if not root_index.exists():
    errors.append("missing root index.html (GitHub Pages entry / redirect)")
else:
    c = root_index.read_text(encoding="utf-8")
    if "web/index.html" not in c:
        errors.append("root index.html does not redirect to web/index.html")

# 5i. web/index.html 存在（GPT 产出或占位页）
if not (ROOT / "web" / "index.html").exists():
    errors.append("missing web/index.html (GPT output target)")

# 5f. 剑盾宝可梦至少 10 只
SWORD_SHIELD = ["grookey_810", "scorbunny_813", "sobble_816", "rillaboom_812",
                "cinderace_815", "inteleon_818", "zacian_888", "zamazenta_889",
                "eternatus_890", "corviknight_823", "dragapult_887", "toxtricity_849",
                "grimmsnarl_861", "wooloo_831", "alcremie_869", "snom_872",
                "morpeko_877", "kubfu_891", "urshifu_892", "sirfetchd_865",
                "falinks_870", "yamper_835"]
present = [s for s in SWORD_SHIELD if (ASSETS / "pokemon" / f"{s}.webp").exists()]
if len(present) < 10:
    errors.append(f"sword/shield pokemon only {len(present)}, expected >= 10")

# 6. 目录体积
def dir_size(p):
    return sum(f.stat().st_size for f in p.rglob("*") if f.is_file())

total = dir_size(ASSETS)
web_assets = total - dir_size(ASSETS / "_raw")

print(f"checked {checked} files")
print(f"images={len(MANIFEST['images'])} deco={len(MANIFEST['deco'])} fonts={len(MANIFEST['fonts']['files'])}")
print(f"assets total = {total/1024/1024:.2f} MB  (excluding _raw = {web_assets/1024/1024:.2f} MB)")
print(f"deploy target = {MANIFEST['constraints'].get('deploy', {}).get('target', '?')}"
      f"  three.js = {MANIFEST['constraints'].get('deploy', {}).get('three_js')}")
print()
if warns:
    print(f"--- {len(warns)} warnings ---")
    for w in warns[:20]:
        print(" WARN", w)
if errors:
    print(f"--- {len(errors)} ERRORS ---")
    for e in errors:
        print(" ERR ", e)
    sys.exit(1)
print("OK: manifest validated, no errors")
