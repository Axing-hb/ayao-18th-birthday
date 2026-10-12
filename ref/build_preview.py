# -*- coding: utf-8 -*-
"""生成 assets/_preview.html —— 素材总览页，用于肉眼核对下载结果。"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
MANIFEST = json.loads((ASSETS / "manifest.json").read_text(encoding="utf-8"))

GROUP_LABEL = {
    "personal": "★ 你提供的私人照片（情感权重最高）",
    "maimai": "舞萌 / 迪拉熊（maimai DX）",
    "acnh": "动物森友会（Animal Crossing: New Horizons）",
    "pokemon": "宝可梦（Pokémon）",
    "tomodachi": "人森 / 朋友收集：梦想生活（Tomodachi Life）",
    "marettu": "MARETU / 术曲封面",
    "ui": "阿药 B 站元素",
}
GROUP_NOTE = {
    "personal": "⚠️ 这些是真实照片，不是网上素材。S1 迪拉熊优先用玩偶实拍，S7 结尾用合照。"
                "不要过度裁切主体、不要加滤镜、不要做黑白处理。",
    "maimai": "⚠️ 用户要求：迪拉熊只放两只做装饰。S1 优先用 personal/dilla_plush_* 真实玩偶；"
              "官方立绘 dilla_01_base + dilla_07_lime 作为备选，两套不要同时出现。",
    "acnh": "建议用 isabelle / kk_slider / celeste 三个，不要全放",
    "pokemon": "18 只，按 section 挑，不要全放",
    "tomodachi": "任天堂日本官网官方素材，贴纸 sticker_* 和图标 ic_* 最好用",
    "marettu": "顺序即 S3 卡片顺序；第 4 张（コインロッカーベイビー）触发红色闪屏彩蛋",
    "ui": "aya_avatar 是她的 B 站头像（表情包动物，不是仓鼠）；仓鼠是现实宠物，见 personal/",
}


def card(it):
    rec = " recommended" if it.get("recommended") else ""
    badge = '<span class="badge">推荐</span>' if it.get("recommended") else ""
    egg = f'<div class="egg">🥚 {html.escape(it["easter_egg"])}</div>' if it.get("easter_egg") else ""
    track = f'<span class="track">#{it["track_no"]:02d}</span>' if it.get("track_no") else ""
    romaji = f'<div class="romaji">{html.escape(it["title_romaji"])}</div>' if it.get("title_romaji") else ""
    return f'''<figure class="card{rec}">
  <div class="thumb"><img src="{html.escape(it["rel"])}" alt="{html.escape(it.get("title") or it["rel"])}" loading="lazy"></div>
  <figcaption>
    <div class="name">{track}{html.escape(it["rel"])}</div>
    <div class="title">{html.escape(it.get("title") or "")}</div>
    {romaji}
    <div class="use">{html.escape(it.get("use") or "")}</div>
    <div class="meta">{it.get("w")}×{it.get("h")} · {it["bytes"]/1024:.1f} KB {badge}</div>
    {egg}
  </figcaption>
</figure>'''


def personal_card(it):
    """私人照片单独一种卡片样式：大图、不裁切。"""
    return f'''<figure class="pcard">
  <div class="pthumb"><img src="{html.escape(it["rel"])}" alt="{html.escape(it.get("title") or "")}" loading="lazy"></div>
  <figcaption>
    <div class="name">{html.escape(it["rel"])}</div>
    <div class="title">{html.escape(it.get("title") or "")}</div>
    <div class="use">{html.escape(it.get("use") or "")}</div>
    <div class="meta">{it.get("w")}×{it.get("h")} · {it["bytes"]/1024:.1f} KB</div>
  </figcaption>
</figure>'''


def section(gid):
    items = [i for i in MANIFEST["images"] if i["group"] == gid]
    if not items:
        return ""
    if gid == "personal":
        cards = "\n".join(personal_card(i) for i in items)
        return f'''<section id="{gid}" class="personal-sec">
  <h2>{html.escape(GROUP_LABEL[gid])} <small>{len(items)} 个文件</small></h2>
  <p class="note">{html.escape(GROUP_NOTE.get(gid, ""))}</p>
  <div class="pgrid">{cards}</div>
</section>'''
    cards = "\n".join(card(i) for i in items)
    return f'''<section id="{gid}">
  <h2>{html.escape(GROUP_LABEL[gid])} <small>{len(items)} 个文件</small></h2>
  <p class="note">{html.escape(GROUP_NOTE.get(gid, ""))}</p>
  <div class="grid">{cards}</div>
</section>'''


def deco_section():
    groups = {}
    for d in MANIFEST["deco"]:
        groups.setdefault(d["group"], []).append(d)
    label = {"music": "音乐", "party": "庆祝 / 甜点", "sparkle": "星星 / 闪光",
             "nature": "动物 / 自然", "misc": "心情 / 其他"}
    out = []
    for g, items in groups.items():
        imgs = "\n".join(
            f'<figure class="mini"><img src="{html.escape(d["rel"])}" alt="" loading="lazy">'
            f'<figcaption>{html.escape(Path(d["rel"]).name)}</figcaption></figure>' for d in items)
        out.append(f'<h3>{html.escape(label.get(g, g))} <small>{len(items)}</small></h3><div class="grid mini-grid">{imgs}</div>')
    total = len(MANIFEST["deco"])
    return f'''<section id="deco">
  <h2>装饰 Emoji（Twemoji SVG） <small>{total} 个文件</small></h2>
  <p class="note">MIT / CC-BY 授权，可自由使用。用于飘落粒子、图标、按钮装饰。</p>
  {"".join(out)}
</section>'''


def font_section():
    rows = "\n".join(
        f'<tr><td><code>{html.escape(Path(f["rel"]).name)}</code></td><td>{f["bytes"]/1024/1024:.2f} MB</td></tr>'
        for f in MANIFEST["fonts"]["files"])
    return f'''<section id="fonts">
  <h2>本地字体 <small>{len(MANIFEST["fonts"])} 个 woff2</small></h2>
  <p class="note">全部已本地化，断网可用。<b>禁止改成 Google Fonts 外链。</b></p>
  <table><thead><tr><th>文件</th><th>大小</th></tr></thead><tbody>{rows}</tbody></table>
</section>'''


def main():
    counts = MANIFEST["counts"]
    total_bytes = sum(i["bytes"] for i in MANIFEST["images"]) + sum(f["bytes"] for f in MANIFEST["fonts"]["files"])
    body = "\n".join(section(g) for g in
                     ["personal", "maimai", "acnh", "pokemon", "tomodachi", "marettu", "ui"])
    rec = MANIFEST["recipient"]
    nav = " · ".join(
        f'<a href="#{g}">{html.escape(GROUP_LABEL[g].split("（")[0].replace("★ ", ""))}</a>'
        for g in ["personal", "maimai", "acnh", "pokemon", "tomodachi", "marettu", "ui"])

    doc = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>素材总览 · 阿药生日网页</title>
<style>
  :root{{
    --bg:#12102A; --soft:#1E1B3A; --card:#FFFDF7; --wood:#D9A45B;
    --blue:#2BB3E8; --pink:#F5539E; --yellow:#FFD23F; --red:#E8202A;
    --text:#2B2740; --dim:#6E6A8A;
  }}
  *{{box-sizing:border-box}}
  body{{margin:0;padding:0 20px 80px;background:var(--bg);color:#EDEBF5;
    font-family:system-ui,"Noto Sans SC","Microsoft YaHei",sans-serif;line-height:1.65}}
  header{{max-width:1200px;margin:0 auto;padding:48px 0 24px}}
  h1{{font-size:clamp(24px,4vw,38px);margin:0 0 8px;
    background:linear-gradient(90deg,var(--blue),var(--pink),var(--yellow));
    -webkit-background-clip:text;background-clip:text;color:transparent}}
  .sub{{color:#B9B4D6;margin:0 0 20px}}
  .stats{{display:flex;flex-wrap:wrap;gap:10px;margin:16px 0 24px}}
  .stat{{background:var(--soft);border:2px solid #35305C;border-radius:14px;padding:10px 16px;font-size:14px}}
  .stat b{{color:var(--yellow);font-size:18px}}
  .who{{background:var(--soft);border-left:4px solid var(--pink);border-radius:0 14px 14px 0;
    padding:14px 18px;font-size:14px;color:#D5D1EA;margin-bottom:20px}}
  .who code{{color:var(--yellow)}}
  nav{{position:sticky;top:0;z-index:9;background:rgba(18,16,42,.92);backdrop-filter:blur(8px);
    padding:12px 0;margin:0 -20px 20px;padding-left:20px;padding-right:20px;border-bottom:1px solid #2C2750}}
  nav a{{color:var(--blue);text-decoration:none;font-size:14px;margin-right:6px}}
  nav a:hover{{color:var(--yellow)}}
  section{{max-width:1200px;margin:0 auto 56px;scroll-margin-top:70px}}
  h2{{font-size:clamp(18px,2.6vw,26px);margin:0 0 6px;color:#fff;
    border-left:5px solid var(--blue);padding-left:12px}}
  h2 small,h3 small{{font-size:13px;color:var(--dim);font-weight:400;margin-left:6px}}
  h3{{font-size:16px;color:#CFC9EA;margin:24px 0 8px}}
  .note{{color:#9C97BC;font-size:13px;margin:0 0 16px;padding-left:17px}}
  .grid{{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(180px,1fr))}}
  .card{{margin:0;background:var(--card);border-radius:16px;overflow:hidden;
    border:2px solid #3A3468;display:flex;flex-direction:column;transition:.18s}}
  .card:hover{{transform:translateY(-4px);border-color:var(--blue)}}
  .card.recommended{{border-color:var(--pink);box-shadow:0 0 0 2px rgba(245,83,158,.25)}}
  .thumb{{height:150px;display:flex;align-items:center;justify-content:center;
    background:linear-gradient(160deg,#EFEAF8,#DFD8F0);padding:8px}}
  .thumb img{{max-width:100%;max-height:100%;object-fit:contain;
    image-rendering:-webkit-optimize-contrast}}
  figcaption{{padding:10px 12px 12px;color:var(--text);font-size:12px}}
  .name{{font-family:ui-monospace,Consolas,monospace;font-size:11px;color:#5B5580;
    word-break:break-all;margin-bottom:4px}}
  .track{{display:inline-block;background:var(--blue);color:#fff;border-radius:6px;
    padding:0 5px;margin-right:4px;font-weight:700}}
  .title{{font-weight:700;font-size:13px;color:#231F3A;line-height:1.35}}
  .romaji{{color:var(--dim);font-size:11px;font-style:italic}}
  .use{{color:#4A4568;font-size:11.5px;margin-top:4px;line-height:1.4}}
  .meta{{color:var(--dim);font-size:10.5px;margin-top:6px;
    border-top:1px dashed #D6D0E8;padding-top:5px}}
  .badge{{background:var(--pink);color:#fff;border-radius:6px;padding:1px 6px;margin-left:4px}}
  .egg{{margin-top:6px;background:#FFF0F5;border:1px dashed var(--pink);color:#B0295E;
    border-radius:8px;padding:4px 7px;font-size:10.5px;line-height:1.4}}
  .mini-grid{{grid-template-columns:repeat(auto-fill,minmax(86px,1fr));gap:8px}}
  .mini{{margin:0;background:var(--soft);border:1px solid #35305C;border-radius:10px;
    padding:6px;text-align:center}}
  .mini img{{width:100%;height:38px;object-fit:contain}}
  .mini figcaption{{padding:4px 0 0;font-size:9px;color:#9C97BC;
    word-break:break-all;font-family:ui-monospace,monospace}}
  /* 私人照片：大图、完整不裁切、金色描边 */
  .personal-sec h2{{border-left-color:var(--yellow)}}
  .pgrid{{display:grid;gap:18px;grid-template-columns:repeat(auto-fill,minmax(280px,1fr))}}
  .pcard{{margin:0;background:var(--card);border-radius:18px;overflow:hidden;
    border:3px solid var(--yellow);display:flex;flex-direction:column;transition:.18s;
    box-shadow:0 0 0 1px rgba(255,210,63,.25)}}
  .pcard:hover{{transform:translateY(-4px)}}
  .pthumb{{background:#EFEAF8;padding:10px;display:flex;align-items:center;justify-content:center;
    min-height:200px}}
  .pthumb img{{max-width:100%;max-height:260px;object-fit:contain;border-radius:10px}}
  .pcard figcaption{{padding:12px 14px 14px;color:var(--text);font-size:12px}}
  .pcard .title{{font-weight:700;font-size:13.5px;color:#231F3A;line-height:1.4}}
  table{{width:100%;border-collapse:collapse;background:var(--soft);
    border-radius:12px;overflow:hidden;font-size:13px}}
  th,td{{padding:9px 14px;text-align:left;border-bottom:1px solid #2C2750}}
  th{{background:#262150;color:var(--yellow);font-size:12px}}
  td code{{color:#A8E6FF}}
  footer{{max-width:1200px;margin:0 auto;color:var(--dim);font-size:12px;
    border-top:1px solid #2C2750;padding-top:16px}}
</style>
</head>
<body>
<header>
  <h1>素材总览 · 阿药生日网页</h1>
  <p class="sub">这份页面只用于<b>核对下载结果</b>，不是最终生日网页。最终网页由 gpt6astra 拼装。</p>
  <div class="who">
    寿星：<b>{html.escape(rec["name"])}</b> ·
    B 站：<a href="{html.escape(rec["space"])}" target="_blank" rel="noopener" style="color:#F5539E">{html.escape(rec["bilibili"])}</a> ·
    生日：<b>{html.escape(rec["birthday"])}</b><br>
    签名：<code>{html.escape(rec["signature"])}</code><br>
    关键词：{html.escape(" / ".join(rec["traits"]))}
  </div>
  <div class="stats">
    <div class="stat"><b>{counts["images"]}</b> 张图片</div>
    <div class="stat"><b>{counts["deco_svg"]}</b> 个装饰 SVG</div>
    <div class="stat"><b>{counts["fonts"]}</b> 个字体</div>
    <div class="stat"><b>{total_bytes/1024/1024:.1f}</b> MB 合计</div>
  </div>
</header>
<nav>{nav} · <a href="#deco">装饰</a> · <a href="#fonts">字体</a></nav>
{body}
{deco_section()}
{font_section()}
<footer>
  素材来源：舞萌 DX 官网（SEGA）· Nookipedia / 动森 · PokeAPI sprites · 任天堂日本官网 · YouTube PV 封面 · B 站公开头像 ·
  Twemoji (MIT/CC-BY) · Google Fonts / fontsource<br>
  原始未优化素材备份在 <code>assets/_raw/</code>。
</footer>
</body>
</html>
'''
    out = ASSETS / "_preview.html"
    out.write_text(doc, encoding="utf-8")
    print(f"wrote {out} ({len(doc)} chars)")


if __name__ == "__main__":
    main()
