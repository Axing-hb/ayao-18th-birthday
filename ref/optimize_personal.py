# -*- coding: utf-8 -*-
"""
处理用户自己提供的私人照片 -> 网页素材。

原图备份在 assets/_raw/personal/，输出到 assets/personal/。

处理规则：
- us_switch       两人玩 Switch 的合照，S7 结尾信的核心照片
- dilla_plush_pair 两只迪拉熊实物玩偶，S1 主视觉（真实版，替代官方立绘）
- hamster_avatar  仓鼠正脸，圆形头像用
- hamster_face    仓鼠特写
- hamster_ball    仓鼠缩成球 + 漫画「!?」特效，S3 彩蛋用
- hamster_cage    手机截图，裁掉状态栏与底部手势条
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "assets" / "_raw" / "personal"
OUT = ROOT / "assets" / "personal"
OUT.mkdir(parents=True, exist_ok=True)


def save(im, name, long_edge, quality=88):
    w, h = im.size
    scale = min(1.0, long_edge / max(w, h))
    if scale < 1.0:
        im = im.resize((max(1, round(w * scale)), max(1, round(h * scale))), Image.LANCZOS)
    if im.mode in ("P", "LA"):
        im = im.convert("RGBA")
    elif im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGB")
    p = OUT / name
    im.save(p, "WEBP", quality=quality, method=6)
    print(f"  {name:28s} {im.size[0]:5d}x{im.size[1]:<5d} {p.stat().st_size/1024:7.1f} KB")
    return p


def square_crop(im):
    """居中裁成正方形"""
    w, h = im.size
    s = min(w, h)
    return im.crop(((w - s) // 2, (h - s) // 2, (w - s) // 2 + s, (h - s) // 2 + s))


print("=== 处理私人照片 ===")

# --- 1. 两人玩 Switch 的合照 ---
im = Image.open(RAW / "us_switch.jpg").convert("RGB")
W, H = im.size
# 裁掉底部边缘一点点（床单杂物），保留主体
im2 = im.crop((0, 0, W, int(H * 0.97)))
save(im2, "us_switch.webp", 1200)
# 额外出一个方形版本，给「贴纸 / 头像卡」用
save(square_crop(im2), "us_switch_square.webp", 640)

# --- 2. 两只迪拉熊实物玩偶 ---
im = Image.open(RAW / "dilla_plush_pair.jpg").convert("RGB")
W, H = im.size
# 裁掉顶部盘子与底部桌面，聚焦两只玩偶
im2 = im.crop((0, int(H * 0.03), W, int(H * 0.95)))
save(im2, "dilla_plush_pair.webp", 1200)
# 单独裁出左侧大只
save(im.crop((0, int(H * 0.05), int(W * 0.55), H)), "dilla_plush_big.webp", 700)
# 单独裁出右侧小只（挂件）
save(im.crop((int(W * 0.56), int(H * 0.15), W, int(H * 0.95))), "dilla_plush_small.webp", 700)

# --- 3. 仓鼠正脸（圆形头像用）---
im = Image.open(RAW / "hamster_avatar.jpg").convert("RGB")
save(square_crop(im), "hamster_avatar.webp", 600)

# --- 4. 仓鼠特写 ---
im = Image.open(RAW / "hamster_face.jpg").convert("RGB")
save(square_crop(im), "hamster_face.webp", 600)

# --- 5. 仓鼠缩成球 + 漫画「!?」特效 ---
im = Image.open(RAW / "hamster_ball.jpg").convert("RGB")
save(square_crop(im), "hamster_ball.webp", 720)

# --- 6. 手机截图：裁掉顶部状态栏 + 底部手势条 ---
im = Image.open(RAW / "hamster_cage.jpg").convert("RGB")
W, H = im.size
im2 = im.crop((0, int(H * 0.028), W, int(H * 0.985)))
save(im2, "hamster_cage.webp", 900)

print("\n完成。")
