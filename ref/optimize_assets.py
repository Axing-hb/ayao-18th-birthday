# -*- coding: utf-8 -*-
"""
阿药生日网页素材优化脚本
- 大图降采样到网页可用尺寸
- 统一输出 webp（现代浏览器全支持），保留原始文件在 assets/_raw/
- 生成 manifest.json 供 gpt6astra 拼装使用
"""
import json
import shutil
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
RAW = ASSETS / "_raw"

# 每个目录的降采样上限（长边像素）
LIMITS = {
    "acnh": 900,
    "pokemon": 600,
    "tomodachi": 1400,
    "maimai": 512,
    "marettu": 800,
    "ui": 900,
    "deco": 256,
}

# 不做转换的目录
SKIP_DIRS = {"fonts", "_raw"}


def optimize():
    RAW.mkdir(exist_ok=True)
    report = []
    for sub in sorted(ASSETS.iterdir()):
        if not sub.is_dir() or sub.name in SKIP_DIRS:
            continue
        limit = LIMITS.get(sub.name, 1000)
        raw_dir = RAW / sub.name
        raw_dir.mkdir(parents=True, exist_ok=True)
        for src in sorted(sub.iterdir()):
            if not src.is_file() or src.suffix.lower() not in (".png", ".jpg", ".jpeg", ".webp"):
                continue
            # 备份原图
            shutil.copy2(src, raw_dir / src.name)
            try:
                im = Image.open(src)
            except Exception as e:
                report.append({"file": str(src.relative_to(ROOT)), "error": str(e)})
                continue
            orig_size = src.stat().st_size
            w, h = im.size
            # SVG 之外的位图统一处理
            scale = min(1.0, limit / max(w, h))
            if scale < 1.0:
                im = im.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
            # 统一转 RGBA/RGB 并输出 webp
            out = src.with_suffix(".webp")
            if im.mode in ("P", "LA"):
                im = im.convert("RGBA")
            elif im.mode == "CMYK":
                im = im.convert("RGB")
            try:
                im.save(out, "WEBP", quality=88, method=6)
            except Exception:
                im.convert("RGB").save(out, "WEBP", quality=88, method=6)
            # 删除原文件（已备份），保留 .webp
            if out != src:
                src.unlink()
            new_size = out.stat().st_size
            report.append({
                "file": str(out.relative_to(ROOT)).replace("\\", "/"),
                "w": im.size[0], "h": im.size[1],
                "bytes_before": orig_size, "bytes_after": new_size,
            })
    return report


if __name__ == "__main__":
    rep = optimize()
    total_before = sum(r.get("bytes_before", 0) for r in rep)
    total_after = sum(r.get("bytes_after", 0) for r in rep)
    print(f"processed {len(rep)} images")
    print(f"before: {total_before/1024/1024:.2f} MB  ->  after: {total_after/1024/1024:.2f} MB")
    (ROOT / "ref" / "optimize_report.json").write_text(
        json.dumps(rep, ensure_ascii=False, indent=2), encoding="utf-8")
