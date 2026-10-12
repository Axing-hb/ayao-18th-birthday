# -*- coding: utf-8 -*-
"""
把非 ASCII 文件名改成纯 ASCII（为 GitHub Pages 部署做准备）。

GitHub Pages 对非 ASCII 文件名会做 URL 编码，有概率 404。
日文原名不丢 —— 它保留在 manifest.json 的 title 字段里，网页文字照常显示日文。

改名规则：`罗马音__日文.webp`  ->  `罗马音.webp`
"""
from pathlib import Path

A = Path(__file__).resolve().parent.parent / "assets"

# 显式映射，避免猜错
RENAME = {
    "mind_brand__マインドブランド":            "mind_brand",
    "umi_naoshi__うみなおし":                  "umi_naoshi",
    "white_happy__ホワイトハッピー":           "white_happy",
    "coin_locker_baby__コインロッカーベイビー": "coin_locker_baby",
    "maegamist__マエガミスト":                 "maegamist",
    "umitagari__うみたがり":                   "umitagari",
    "shiu__しう":                              "shiu",
    "dokuhaku__ドクハク":                      "dokuhaku",
    "binomiuri__ビノミウリ":                   "binomiuri",
    "sunusumumuriku__スヌスムムリク":          "sunusumumuriku",
}

changed = 0
for d in (A / "marettu", A / "_raw" / "marettu"):
    if not d.exists():
        continue
    for f in sorted(d.iterdir()):
        if not f.is_file():
            continue
        stem, suffix = f.stem, f.suffix
        if stem in RENAME:
            new = d / f"{RENAME[stem]}{suffix}"
            if new.exists():
                print(f"  SKIP (已存在) {f.name}")
                continue
            f.rename(new)
            print(f"  {d.relative_to(A)}: {f.name}")
            print(f"      -> {new.name}")
            changed += 1

print(f"\n重命名 {changed} 个文件")

# 复查
left = [p for p in A.rglob("*")
        if p.is_file() and any(ord(ch) > 127 for ch in p.name)]
print(f"剩余非 ASCII 文件名: {len(left)}")
for p in left:
    print("  ", p.relative_to(A))
