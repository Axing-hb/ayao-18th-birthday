# -*- coding: utf-8 -*-
"""下载 伊布家族 / 鬃岩狼人各形态 / 剑盾知名宝可梦（PokeAPI official artwork）。"""
import urllib.request
from pathlib import Path

PROXY = "http://127.0.0.1:7897"
OUT = Path(__file__).resolve().parent.parent / "assets" / "pokemon"
OUT.mkdir(parents=True, exist_ok=True)

opener = urllib.request.build_opener(
    urllib.request.ProxyHandler({"http": PROXY, "https": PROXY})
)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36"
BASE = ("https://raw.githubusercontent.com/PokeAPI/sprites/master/"
        "sprites/pokemon/other/official-artwork/{}.png")

# (文件名, 全国图鉴号)
WANT = [
    # ---- 伊布家族（9 只，做合影用）----
    ("eevee_133",           "133"),
    ("vaporeon_134",        "134"),
    ("jolteon_135",         "135"),
    ("flareon_136",         "136"),
    ("espeon_196",          "196"),
    ("umbreon_197",         "197"),
    ("leafeon_470",         "470"),
    ("glaceon_471",         "471"),
    ("sylveon_700",         "700"),   # 仙子伊布 ★她喜欢
    # ---- 鬃岩狼人（3 形态）★她喜欢 ----
    ("lycanroc_745_midday",   "745"),
    ("lycanroc_10152_midnight", "10152"),
    ("lycanroc_10153_dusk",     "10153"),
    # ---- 剑盾（她最喜欢的世代）----
    ("grookey_810",     "810"),   # 敲音猴
    ("scorbunny_813",   "813"),   # 炎兔儿
    ("sobble_816",      "816"),   # 泪眼蜥
    ("rillaboom_812",   "812"),   # 轰擂金刚猩
    ("cinderace_815",   "815"),   # 闪焰王牌
    ("inteleon_818",    "818"),   # 千面避役
    ("zacian_888",      "888"),   # 苍响
    ("zacian_10188_crowned", "10188"),  # 苍响·剑之王
    ("zamazenta_889",   "889"),   # 藏玛然特
    ("zamazenta_10189_crowned", "10189"),  # 藏玛然特·盾之王
    ("eternatus_890",   "890"),   # 无极汰那
    ("corviknight_823", "823"),   # 钢铠鸦
    ("dragapult_887",   "887"),   # 多龙巴鲁托
    ("toxtricity_849",  "849"),   # 颤弦蝾螈
    ("grimmsnarl_861",  "861"),   # 长毛巨魔
    ("wooloo_831",      "831"),   # 毛辫羊
    ("alcremie_869",    "869"),   # 霜奶仙
    ("snom_872",        "872"),   # 雪吞虫
    ("morpeko_877",     "877"),   # 莫鲁贝可
    ("kubfu_891",       "891"),   # 熊徒弟
    ("urshifu_892",     "892"),   # 武道熊师
    ("sirfetchd_865",   "865"),   # 葱游兵
    ("falinks_870",     "870"),   # 列阵兵
    ("yamper_835",      "835"),   # 来电汪
]

ok = fail = 0
for name, pid in WANT:
    dest = OUT / f"{name}.png"
    try:
        req = urllib.request.Request(BASE.format(pid), headers={"User-Agent": UA})
        with opener.open(req, timeout=30) as r:
            data = r.read()
        if len(data) < 1000:
            print(f"  FAIL(小文件) {name}  ({len(data)} B)")
            fail += 1
            continue
        dest.write_bytes(data)
        print(f"  OK  {name:28s} {len(data)/1024:8.1f} KB")
        ok += 1
    except Exception as e:
        print(f"  FAIL {name}: {e}")
        fail += 1

print(f"\n完成：{ok} 成功 / {fail} 失败")
