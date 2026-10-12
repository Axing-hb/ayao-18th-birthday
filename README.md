# 阿药生日网页 · 项目总览

给女朋友 **阿药** 做的 **18 岁**生日惊喜网页。她生日 **10 月 17 日**，那天我可能在学校，所以用网页远程送祝福。

**这个仓库做的是「规划 + 素材 + 提示词」三件事，网页主体交给 gpt6astra 拼装。**

---

## 快速上手

| 我想…… | 打开 |
| --- | --- |
| **给 GPT 派活**（最重要） | [`docs/PROMPT_FOR_GPT.md`](docs/PROMPT_FOR_GPT.md) ← 整段复制给 GPT |
| **部署到 GitHub Pages** | [`docs/DEPLOY.md`](docs/DEPLOY.md) ← 操作手册 |
| 看素材下载了什么 | [`assets/_preview.html`](assets/_preview.html) |
| 看完整制作规划 | [`docs/PLAN.md`](docs/PLAN.md) |
| 看精简执行说明 | [`docs/HANDOFF.md`](docs/HANDOFF.md) |
| 查素材路径 / 尺寸 | [`assets/manifest.json`](assets/manifest.json) |

**本地预览**（用 http 服务，比双击 `file://` 更接近线上）：

```powershell
cd ayao-birthday
& "C:\Users\29631\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe" -e "const h=require('http'),f=require('fs'),p=require('path');h.createServer((q,s)=>{let u=decodeURIComponent(q.url.split('?')[0]);if(u.endsWith('/'))u+='index.html';f.readFile(p.join(process.cwd(),u),(e,d)=>{if(e){s.writeHead(404);return s.end('404 '+u)}s.writeHead(200);s.end(d)})}).listen(8080,()=>console.log('http://127.0.0.1:8080'))"
```

然后打开 <http://127.0.0.1:8080/>

---

## 部署状态

已为 **GitHub Pages** 做好准备：

| 项目 | 状态 |
| --- | --- |
| 部署目标 | `https://<用户名>.github.io/<仓库名>/` |
| Three.js | ✅ **已本地 vendor**（`assets/vendor/three.min.js`，r149 UMD，实测可用） |
| 3D 蛋糕 | ✅ 允许用 Three.js（联网访问，不再要求断网可用） |
| 非 ASCII 文件名 | ✅ 30 个术曲封面已改为 ASCII，日文标题保留在 manifest 里 |
| `.gitignore` | ✅ 排除 `assets/_raw/`（34 MB）+ 字体参考 CSS + 原始 jpg |
| 根目录入口 | ✅ `index.html` 跳转页已就位 |
| `web/index.html` | ⚠️ **目前是占位页**，等 GPT 产出正式网页后替换 |
| 上传体积 | **239 个文件 / 17.27 MB** |
| 隐私 | ⚠️ 含私人照片，Public 仓库任何人可见（详见 DEPLOY.md 第七节） |

---

## 本次的四个重点需求

1. **18 岁生日**（成年礼）—— S2 要 18 根蜡烛，S7 要有 18 岁蜡烛的 3D 蛋糕动画
2. **背景音乐** `assets/audio/acnh_bgm.mp4`（动森 BGM）—— 单曲循环，左上角透明音符按钮控制
3. **她喜欢的角色** —— 动森：西施惠、蜜雪儿、史培亚；宝可梦：仙子伊布、鬃岩狼人、
   伊布家族合影、剑盾（她最喜欢的世代）
4. **S7 底部 3D 生日蛋糕动画**；**网页最下端写 `by Axing`**

> ~~术曲封面加超链接跳 B 站~~ —— **已取消**。

---

## 关于阿药（从她 B 站主页抓的公开信息）

| 项目 | 内容 |
| --- | --- |
| 昵称 | **Anria_01017**（本人叫**阿药**） |
| 签名 | 「你好，我叫阿药。一个成分复杂的 intp」 |
| B 站 | <https://space.bilibili.com/614351218> |
| 等级 / 粉丝 | LV6 / 131 粉 · 836 关注 · 获赞 10,416 |
| 投稿 | 视频 14 · 追番 7 · 收藏夹 27 |
| **年龄** | **18 岁（本次生日是成年礼）** |

**她喜欢**：二次元 · 术曲（Vocaloid，尤其 **MARETU**）· 舞萌 DX · 动物森友会 · 宝可梦 · 人森（朋友收集：梦想生活）

**她明确喜欢的角色**：

| 类别 | 角色 |
| --- | --- |
| 动森 | **西施惠**、**蜜雪儿**（兔）、**史培亚**（狼） |
| 宝可梦 | **仙子伊布**、**鬃岩狼人**、**伊布家族** |
| 宝可梦世代 | **剑盾（第八世代）是她最喜欢的** |

**养仓鼠**：你们一起养的宠物，出现在多张私人照片里。

**文案基调**：她是 **INTP**，吃「克制的浪漫 + 只属于她的梗」，不吃肉麻长抒情。

**关键彩蛋**：她的昵称 `Anria_01017` 里藏着 **01017** —— 和 10 月 17 日生日吻合。整个网页的编号系统（`No.01017`、`第 01017 号惊喜`）都建立在这上面。

> ⚠️ **别搞混**：她的 B 站头像是**表情包动物**，不是仓鼠。仓鼠是现实中的宠物（在 `assets/personal/`）。

---

## ★ 私人照片（`assets/personal/`）—— 整页的核心

你自己提供的 6 张真实照片，情感权重高于一切网上素材。

| 文件 | 内容 | 用在哪 |
| --- | --- | --- |
| `us_switch.webp` | **你们俩躺床上一起玩 Switch** | **S7 结尾核心照片** |
| `us_switch_square.webp` | 同上方形版 | S2 拍立得相框 |
| `dilla_plush_pair.webp` | **两只迪拉熊实物玩偶**（带官方吊牌） | S1 主视觉 |
| `dilla_plush_big.webp` / `dilla_plush_small.webp` | 玩偶单只特写 | **S1 左 / 右** |
| `hamster_avatar.webp` | 仓鼠正脸 | **S6 居民卡头像** |
| `hamster_face.webp` | 仓鼠特写 | S5 图鉴「仓鼠条目」 |
| `hamster_ball.webp` | 仓鼠缩成球 + 漫画「!?」 | **S3 第 6 张卡片彩蛋** |
| `hamster_cage.webp` | 仓鼠趴笼顶（竖图） | S6 竖版配图 |

**使用纪律**：不裁主体 · 不加滤镜 · 不拉伸 · 不缩小到看不清 · 不做背景底图 · 给有意义的 `alt`。

---

## 素材清单（全部已下载到本地）

| 目录 | 内容 | 数量 | 体积 |
| --- | --- | ---: | ---: |
| `assets/personal/` | ★ **私人照片**（你提供的） | 9 | 0.6 MB |
| `assets/audio/` | ★ **动森背景音乐** | 1 | 1.4 MB |
| `assets/vendor/` | ★ **Three.js r149**（3D 蛋糕用） | 1 | 0.6 MB |
| `assets/maimai/` | 舞萌 DX · 迪拉熊一族（SEGA 官网） | 18 | 0.2 MB |
| `assets/acnh/` | 动物森友会（**含她喜欢的三只**） | 16 | 0.7 MB |
| `assets/pokemon/` | 宝可梦（**伊布家族 / 鬃岩狼人 / 剑盾 22 只**） | 53 | 1.2 MB |
| `assets/tomodachi/` | 人森 · 任天堂日本官网官方素材 | 37 | 3.1 MB |
| `assets/marettu/` | MARETU 术曲 PV 封面 ×10 首 | 10 | 0.7 MB |
| `assets/ui/` | 阿药 B 站头像 / 头图 / 名牌 | 4 | 0.1 MB |
| `assets/deco/` | Twemoji 装饰 SVG（MIT/CC-BY） | 64 | 0.08 MB |
| `assets/fonts/` | 本地中/日文字体 woff2 | 7 | 9.5 MB |

**网页实际用量约 17.8 MB**（不含 `_raw/` 备份）。
**上传到 GitHub 约 17.3 MB / 239 个文件**（`_raw/` 和字体参考 CSS 已被 `.gitignore` 排除）。

### 硬约束

1. **迪拉熊只放两只** —— S1 优先用**真实玩偶照**（`personal/dilla_plush_big` + `dilla_plush_small`），
   官方立绘 `dilla_01_base` + `dilla_07_lime` 作备选，**两套不要混用**
2. **18 岁**必须体现在 S2 蜡烛数量、S7 的 3D 蛋糕、S7 的信
3. **`by Axing` 必须出现在网页最下端**
4. **背景音乐单曲循环**，左上角透明音符按钮，默认不自动播放
5. **部署到 GitHub Pages** —— 素材路径必须用相对路径 `../assets/...`，且大小写要与文件名一致
6. **允许用 Three.js**（已本地 vendor r149），但**不要引入其他框架**
7. **字体和图片全部本地** —— 禁止改成 Google Fonts / 外链 CDN

---

## 页面结构（8 段）

| # | 段落 | 核心内容 |
| --- | --- | --- |
| S0 | 加载入场 | 迪拉熊跳动（**真实玩偶照**）+ 音游判定圈 `TAP → PERFECT` + **点击启动 BGM** |
| S1 | Hero 主视觉 | 「生日快乐，阿药。」+ **两只迪拉熊玩偶** + 飘落音符 |
| S2 | **18 岁**生日蛋糕 | **18 根蜡烛** + 吹蜡烛交互 → 礼花 + 宝可梦探头 + **方形合照**拍立得 |
| S3 | **MARETU 电台** | 10 首曲目卡片 + 旋转唱片 + 红色闪屏彩蛋 + **仓鼠表情包彩蛋** |
| S4 | 动森 · 岛上公告 | 木牌样式 + 三条公告 + **西施惠/蜜雪儿/史培亚**三只村民 + 台词 |
| S5 | 宝可梦专区 | 图鉴 + **伊布家族 9 只合影**（仙子伊布 C 位）+ **鬃岩狼人三形态** + **剑盾专区** |
| S6 | 人森 · 居民卡 | 「我的岛上，已经给你留好位置了。」+ **仓鼠头像** |
| S7 | 结尾信 + **3D 蛋糕** | **你们俩的合照** + 克制的告白 + **滚动触发 3D 生日蛋糕 + 18 根蜡烛动画** + `by Axing` |

完整设计规范（配色、字体、动效、响应式）见 [`docs/PLAN.md`](docs/PLAN.md)。

---

## 目录结构

```
ayao-birthday/
├── README.md                ← 本文件
├── docs/
│   ├── PLAN.md              完整制作规划书（配色/字体/结构/交互/文案/验收）
│   ├── HANDOFF.md           给 gpt6astra 的精简执行说明
│   └── PROMPT_FOR_GPT.md    ★ 给 GPT 的完整提示词（可直接整段复制）
├── assets/
│   ├── _preview.html        素材总览页（肉眼核对用）
│   ├── manifest.json        机器可读素材清单（路径/尺寸/用途/推荐标记）
│   ├── _raw/                原始未优化素材备份（含 _raw/personal/、_raw/audio/）
│   ├── personal/            ★ 私人照片（优先级最高）
│   ├── audio/               ★ 背景音乐 acnh_bgm.mp4
│   ├── maimai/ acnh/ pokemon/ tomodachi/ marettu/ ui/
│   ├── deco/                Twemoji SVG
│   └── fonts/               本地字体
├── ref/
│   ├── optimize_assets.py    网络素材优化（降采样 + 转 webp）
│   ├── optimize_personal.py  私人照片处理（裁切 + 转 webp）
│   ├── fetch_pokemon.py      批量下载伊布家族/鬃岩狼人/剑盾
│   ├── build_manifest.py     生成 manifest.json
│   ├── build_preview.py      生成素材总览页
│   └── validate.py           校验：路径 / 尺寸 / 约束 / 私人照片 / 音频 / 她喜欢的角色
└── web/                     ← gpt6astra 产出 index.html 放这里
```

---

## 复现 / 重新生成

```powershell
$py = "C:\Users\29631\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe"

& $py ref\fetch_pokemon.py      # 下载伊布家族 / 鬃岩狼人 / 剑盾宝可梦
& $py ref\optimize_assets.py    # 优化网络素材（原始文件已备份到 _raw/，可重复跑）
& $py ref\optimize_personal.py  # 处理私人照片
& $py ref\build_manifest.py     # 重建 manifest.json
& $py ref\build_preview.py      # 重建素材总览页
& $py ref\validate.py           # 校验，出错会 exit 1
```

`validate.py` 会检查：素材路径是否存在、manifest 记录尺寸与实际是否一致、迪拉熊约束、
**9 张私人照片是否齐全且被正确的 section 引用**、**音频是否登记**、
**18 岁是否写进配置**、**她喜欢的角色是否在册且被引用**、
**伊布家族是否 9 只齐全**、**剑盾宝可梦是否 ≥10 只**、
MARETU 10 首是否齐备且顺序正确、各 section 引用的素材是否都在。

当前状态：**218 个文件全部校验通过，0 错误。**

---

## 素材来源

- **私人照片** —— 用户本人提供（`我们俩.jpg`、`她的头像.jpg`、`老鼠.jpg`、`老鼠1.jpg`、`老鼠2.jpg`、`迪拉熊玩偶.jpg`）
- **背景音乐** —— 用户本人提供的 `动森背景.mp4`
- 舞萌 DX 迪拉熊图标 —— SEGA 官方 <https://maimai.sega.jp/>
- 动物森友会角色立绘 —— [Nookipedia](https://nookipedia.com/)
- 宝可梦官方 artwork —— [PokeAPI/sprites](https://github.com/PokeAPI/sprites)
- 人森（朋友收集：梦想生活）素材 —— [任天堂日本官网](https://www.nintendo.com/jp/switch/blfga/)
- MARETU 曲目封面 —— 各曲官方 PV 缩略图
- 装饰 emoji —— [Twemoji](https://github.com/twitter/twemoji)（MIT / CC-BY 4.0）
- 字体 —— Google Fonts / [fontsource](https://fontsource.org/)

仅供个人非商业用途（生日惊喜网页）。
