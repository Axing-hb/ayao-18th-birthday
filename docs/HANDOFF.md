# HANDOFF · 交给 gpt6astra 的拼装说明

> 详细版见同目录 `PLAN.md`。
> **给 GPT 的完整提示词见 `PROMPT_FOR_GPT.md`** —— 那份可以直接整段复制给 GPT。

---

## 你的任务

输出一个单文件网页：`web/index.html`

- 纯静态，无框架，无 CDN，无外链（**包括不用 Three.js**）
- 素材路径全部走相对路径 `../assets/...`
- CSS 内联 `<style>`，JS 内联 `<script>`
- 断网打开也要完全正常（字体、图片、图标、音乐全部已本地化）
- 不要修改 `assets/` 下任何文件

---

## 本次追加的四个要求（重点）

1. **18 岁生日**（成年礼）—— S2 要 **18 根蜡烛**，S7 要有 **18 岁蜡烛的 3D 蛋糕动画**，信里要提 18 岁
2. **背景音乐** `../assets/audio/acnh_bgm.mp4`（动森 BGM）—— **单曲循环**，**左上角透明音符按钮**控制开关
3. **她喜欢的角色** —— 动森：**西施惠、蜜雪儿、史培亚**；宝可梦：**仙子伊布、鬃岩狼人**；
   **伊布家族合影**；**剑盾（她最喜欢的世代）**知名宝可梦
4. **S7 底部 3D 生日蛋糕 + 18 岁蜡烛动画**；**网页最下端写 `by Axing`**

> ~~术曲封面加超链接跳 B 站~~ —— **已取消，不要做**。

---

## 人物与背景

- 寿星：**阿药**（B 站昵称 `Anria_01017`），生日 **10 月 17 日**，**18 岁**
- 她签名：**「你好，我叫阿药。一个成分复杂的 intp」**
- 她是二次元，爱听**术曲（Vocaloid）**，尤其 **MARETU**
- 也玩/喜欢：**舞萌 DX（maimai）、动物森友会、宝可梦、人森（朋友收集：梦想生活）**
- **养仓鼠** —— 你们一起养的宠物，多张私人照片里都有它
- 语气：**克制、温柔、有一点理科生式幽默**。她是 INTP，**不要写肉麻长抒情**。

**她明确喜欢的角色（重点照顾）：**

| 类别 | 角色 |
| --- | --- |
| 动森 | **西施惠** `acnh/isabelle.webp` |
| 动森 | **蜜雪儿** Sasha（兔）`acnh/sasha_mixueer.webp` |
| 动森 | **史培亚** Fang（狼）`acnh/fang_shipeiya.webp` |
| 宝可梦 | **仙子伊布** `pokemon/sylveon_700.webp` |
| 宝可梦 | **鬃岩狼人** 三形态 `pokemon/lycanroc_*.webp` |
| 宝可梦 | **伊布家族** 9 只全 `pokemon/{eevee,...}_*.webp` |
| 宝可梦 | **剑盾（第八世代）**是她最喜欢的世代 |

> ⚠️ **注意**：她的 B 站头像是**表情包动物**，不是仓鼠。仓鼠是现实中的宠物（见 `assets/personal/`）。

---

## 背景音乐（`assets/audio/acnh_bgm.mp4`）

- **单曲循环**：`audio.loop = true`
- **默认不自动播放**（浏览器会拦），首次交互后开始
- **左上角透明音符按钮**控制播放/暂停，`position:fixed`，手机上避开刘海
- 按钮图标用 `../assets/deco/note.svg`
- 用户手动暂停后不要再自动播放

完整 CSS/JS 见 `PLAN.md` 第 2.3b 节。

---

## ★ 最重要：私人照片（`assets/personal/`）

这些是**用户本人提供的真实照片**，情感权重高于一切网上素材。整页的核心就是它们。

| 文件 | 内容 | 用在哪 |
| --- | --- | --- |
| `us_switch.webp` | **你们俩躺床上一起玩 Switch** | **S7 结尾，大幅居中，先出图再出字** |
| `us_switch_square.webp` | 同上方形版 | S2 拍立得相框 |
| `dilla_plush_pair.webp` | **两只迪拉熊实物玩偶**（带官方吊牌） | S1 主视觉（整张） |
| `dilla_plush_big.webp` | 大只玩偶特写 | **S1 左侧** / S0 加载动画 |
| `dilla_plush_small.webp` | 小只挂件特写 | **S1 右侧** |
| `hamster_avatar.webp` | 仓鼠正脸（圆形） | **S6 居民卡头像** |
| `hamster_face.webp` | 仓鼠特写 | S5 图鉴「仓鼠条目」 |
| `hamster_ball.webp` | 仓鼠缩成球 + 漫画「!?」 | **S3 第 6 张卡片彩蛋** |
| `hamster_cage.webp` | 仓鼠趴笼顶（竖图） | S6 竖版配图 |

**使用纪律（必须遵守）：**
1. **不裁主体** —— 玩偶吊牌、仓鼠爪子都是细节。
2. **不加滤镜** —— 不要黑白、不要复古、不要高对比。
3. **不拉伸** —— `object-fit: contain` 或按原比例。
4. **不缩小到看不清** —— `us_switch` 在 S7 要占足够大面积。
5. **不做背景底图** —— 单独成块展示，不要被文字盖住。
6. **给有意义的 `alt`** —— 描述内容，不要写「图片」。

---

## 配色（直接抄进 `:root`）

```css
:root{
  --c-bg-deep:#12102A; --c-bg-soft:#1E1B3A;
  --c-card:#FFFDF7; --c-wood:#D9A45B; --c-wood-dark:#A9762F;
  --c-maimai-blue:#2BB3E8; --c-maimai-pink:#F5539E; --c-maimai-yellow:#FFD23F;
  --c-maretu-red:#E8202A; --c-leaf:#7BC96F;
  --c-text:#2B2740; --c-text-dim:#6E6A8A;
}
```
深色底 + 奶油白卡片做主结构。舞萌蓝/粉只做强调。MARETU 红**全页只出现 1 次**（S3 第 4 张卡片）。

---

## 字体（本地，禁止改成 Google Fonts 外链）

```css
@font-face{font-family:'ZCOOL KuaiLe';src:url('../assets/fonts/zcool-kuaile-400.woff2') format('woff2');font-display:swap}
@font-face{font-family:'Hachi Maru Pop';src:url('../assets/fonts/hachi-maru-pop-400.woff2') format('woff2');font-display:swap}
@font-face{font-family:'Mochiy Pop One';src:url('../assets/fonts/mochiy-pop-one-400.woff2') format('woff2');font-display:swap}
@font-face{font-family:'Zen Maru Gothic';src:url('../assets/fonts/zen-maru-gothic-400.woff2') format('woff2');font-weight:400;font-display:swap}
@font-face{font-family:'Zen Maru Gothic';src:url('../assets/fonts/zen-maru-gothic-700.woff2') format('woff2');font-weight:700;font-display:swap}
@font-face{font-family:'Noto Sans SC';src:url('../assets/fonts/noto-sans-sc-400.woff2') format('woff2');font-weight:400;font-display:swap}
@font-face{font-family:'Noto Sans SC';src:url('../assets/fonts/noto-sans-sc-700.woff2') format('woff2');font-weight:700;font-display:swap}

:root{
  --font-title:'ZCOOL KuaiLe','Hachi Maru Pop',system-ui,sans-serif;
  --font-jp:'Zen Maru Gothic','Hachi Maru Pop',sans-serif;
  --font-body:'Noto Sans SC','Zen Maru Gothic',system-ui,sans-serif;
}
```

---

## 页面结构（7 段，按顺序）

### S0 加载
- 全屏深色，中央迪拉熊跳动 + 判定圈 `TAP → PERFECT` 扩散
- 小字：`LOADING ... 为阿药准备的第 01017 号惊喜`
- 素材：`../assets/personal/dilla_plush_big.webp`（首选）；`../assets/maimai/dilla_01_base.webp` 备选
- **进入按钮点击时同时启动 BGM**

### S1 Hero
- 大标题：**生日快乐，阿药。**
- 副标题：**你好，我叫阿药。一个成分复杂的 intp。—— 今天这一页，是专门为你一个人开的服务器。**
- 背景：深蓝夜空渐变 + 缓慢飘落音符/叶子/星星
- **只放两只迪拉熊**（用户硬性要求），优先用真实玩偶照：
  - 左：`../assets/personal/dilla_plush_big.webp`
  - 右：`../assets/personal/dilla_plush_small.webp`
  - 或整张合影 `../assets/personal/dilla_plush_pair.webp` 做主视觉
  - 备选（官方立绘，两套**不要混用**）：`../assets/maimai/dilla_01_base.webp` + `dilla_07_lime.webp`
- 上下浮动，相位错开；底部 SCROLL 箭头

### S2 18 岁生日蛋糕
- 蛋糕用 CSS + twemoji 拼：`cake.svg` `cupcake.svg` `candy.svg` `cherry.svg`
- **18 根蜡烛**（成年礼，必须 18 根）
- **吹蜡烛交互**：点击 → 蜡烛依次熄灭 + 烟雾 → 礼花（`party.svg` + CSS 粒子）
- 熄灭后文案：**「18 根都吹灭了。愿望已经收到，剩下的交给时间。」**
- 副标题：**「从今天起，你要为自己的每一个决定负责了。—— 不过今天先不用。」**
- 宝可梦探头：`pikachu_025.webp` `eevee_133.webp` `jigglypuff_039.webp`
- 动森叶子飘落：`leaf_icon.webp`
- **方形合照** `../assets/personal/us_switch_square.webp` 做成拍立得相框，配字：「上一次一起过生日，也是这样躺着的。」

### S3 MARETU 电台（重头戏）
- 做成**音乐播放器 / CD 机**，带旋转唱片
- 标题：**MARETU 电台 · 深夜档**，副标题 `for 阿药 · 成分复杂频道`
- 10 张曲目卡片，封面在 `../assets/marettu/`，**日文原名做标题、罗马音做副标题**：

| 封面文件 | 日文标题 | 罗马音 |
| --- | --- | --- |
| `mind_brand.webp` | マインドブランド | Mind Brand |
| `umi_naoshi.webp` | うみなおし | Uminaoshi |
| `white_happy.webp` | ホワイトハッピー | White Happy |
| `coin_locker_baby.webp` | コインロッカーベイビー | Coin Locker Baby |
| `maegamist.webp` | マエガミスト | Maegamist |
| `umitagari.webp` | うみたがり | Umitagari |
| `shiu.webp` | しう | Shiu |
| `dokuhaku.webp` | ドクハク | Dokuhaku |
| `binomiuri.webp` | ビノミウリ | Binomiuri |
| `sunusumumuriku.webp` | スヌスムムリク | Sunusumumuriku |

> 文件名是纯 ASCII（为 GitHub Pages 部署），**日文标题照上表写死在网页里**。

- 卡片可翻转，背面写一句短话（自己写，风格克制）
- **彩蛋 1**：翻到第 4 张（コインロッカーベイビー）时，整页闪一下 `--c-maretu-red`，0.6s 恢复，**只触发一次**
- **彩蛋 2**：翻到第 6 张（うみたがり）时，弹出仓鼠表情包 `../assets/personal/hamster_ball.webp`，
  配字：「这张图是它睡成这样的样子。我当时也这个表情。」
- 底部放假的播放进度条，hover 出现 `PERFECT` 判定字样
- ⚠️ **不要给卡片加跳转 B 站的链接**（该需求已取消）

### S4 动森 · 岛上公告（含她喜欢的村民）
- 木牌样式（木色边框 + 奶油白底）
- 标题：**岛上公告**
- 三条公告：
  1. 今日天气：晴。风力：刚好能吹灭 18 根蜡烛。
  2. 岛上来了新居民，名字叫阿药。生日：10 月 17 日。年龄：18。
  3. 狸克说，今天所有商品免费。……骗你的，但蛋糕是真的。
- **★ 她喜欢的三只村民必须都出现**：
  - `../assets/acnh/isabelle.webp`（**西施惠**）—— 主位
  - `../assets/acnh/sasha_mixueer.webp`（**蜜雪儿**，兔）—— 右侧
  - `../assets/acnh/fang_shipeiya.webp`（**史培亚**，狼）—— 左侧
  - `kk_slider.webp` 中下氛围，`celeste.webp` 右上小装饰
- **给这三只各写一句台词**：
  - 西施惠：「今天的公告板我特意擦干净了。生日快乐呀！」
  - 蜜雪儿：「唔……我本来想给你烤个蛋糕，结果自己吃掉了。抱歉。」
  - 史培亚：「这倒是……挺不错的。生日快乐，小子。」

### S5 宝可梦 · 图鉴 + 伊布家族合影 + 剑盾专区

**5a 图鉴卡片**
- 卡片头 `No.01017  阿药`；属性 `思考系 / 音乐系`；特性 `成分复杂`、`深夜术曲专精`
- 写 4–6 条可爱的图鉴说明
- **加一条仓鼠条目**（`../assets/personal/hamster_face.webp`）：
  `No.00001  仓鼠` · 属性 `毛绒系 / 半夜跑轮系` · 特性 `缩成球`
  说明：「两人共同持有。攻击力 0，可爱度溢出。」

**5b ★ 伊布家族合影**
- 9 只：`eevee_133` `vaporeon_134` `jolteon_135` `flareon_136` `espeon_196` `umbreon_197` `leafeon_470` `glaceon_471` `sylveon_700`
- **仙子伊布放 C 位**（她最喜欢）—— 中间、放大、`--c-maimai-pink` 柔光
- 标题：**「伊布家族，全员到齐。」** 副标题：`No.133 – No.700`

**5c ★ 鬃岩狼人三形态**
- `lycanroc_745_midday`（白昼）`lycanroc_10126_midnight`（黑夜）`lycanroc_10152_dusk`（黄昏）
- 横向三格，中间稍大
- 标题：**「同一只狼，三个时间段。」** 副标题：`昼 / 夜 / 黄昏`
- 小字：`它随你什么时候遇见它而改变样子。`

**5d ★ 剑盾专区（她最喜欢的世代）**
- 标题：**「第八世代 · 伽勒尔地区」**
- **御三家**：`grookey_810` `scorbunny_813` `sobble_816` + `rillaboom_812` `cinderace_815` `inteleon_818`
- **传说**：`zacian_888` + `zacian_10188_crowned`、`zamazenta_889` + `zamazenta_10189_crowned`、`eternatus_890`
- **人气**：`corviknight_823` `dragapult_887` `toxtricity_849` `grimmsnarl_861` `sirfetchd_865` `falinks_870`
- **可爱系**：`wooloo_831` `alcremie_869` `snom_872` `morpeko_877` `yamper_835`
- **DLC**：`kubfu_891` `urshifu_892`
- 苍响/藏玛然特建议**双形态并排**

**5e 徽章**：twemoji `medal` `trophy` `diamond` `star2` 做 8 枚假道馆徽章

### S6 人森 · 居民卡
- 标题：**我的岛上，已经给你留好位置了。**
- 居民卡字段：
  - 居民名 `阿药`
  - 性格 `INTP（自我诊断 100% 准确）`
  - 口头禅 `「成分复杂」`
  - 喜欢 `术曲、舞萌、动森、宝可梦、仓鼠`
  - 讨厌 `（留白，让她自己填）`
- **头像用 `../assets/personal/hamster_avatar.webp`**（你们养的仓鼠，圆形裁切 + 描边）；
  她的 B 站头像 `../assets/ui/aya_avatar.webp` 放旁边做小徽章，两个并列
- 配图 `../assets/personal/hamster_cage.webp`（竖图）放右侧，手机端移到下方
- 装饰：`tomo_logo.webp`、`tomo_obj_resident.webp`、`tomo_sticker_1~4.webp`、`tomo_ic_*.webp`
- 背景：`tomo_kv_1.webp` 或 `tomo_island_*.webp`，低透明度当纹理

### S7 结尾信 + 3D 生日蛋糕动画
- 深色星空 + 缓慢旋转唱片
- **先放核心照片**：`../assets/personal/us_switch.webp`（你们俩玩 Switch 的合照）
  - 大幅、居中、圆角、轻微投影
  - 图下方小字（`--c-text-dim`）：`某个普通的晚上 · 谁也没赢`
  - **不要缩小、不要做背景、不要加滤镜**
- 标题：**最后一句，不绕圈子了。**
- 正文（照抄，`[你的名字]` 处留占位注释）：

> 阿药：
>
> 今天是你 18 岁生日。我可能在教室，可能在路上，可能隔着几百公里。
> 但这一页会一直开着 —— 你什么时候点进来，它就在那儿等着。
>
> 18 岁听起来是个挺大的数字，可我没什么大道理要讲。
> 我只想说：以后每年这天，我都想在这儿留点什么。
>
> 我不太会说话，所以我把想说的都放进了这些图里：
> 两只迪拉熊是替我陪着你的，
> 那些 MARETU 的歌是我猜你会喜欢的，
> 伊布家族全员到齐了，仙子伊布在中间，
> 岛上的位置我早就留好了，一直空着。
> 还有那只仓鼠 —— 它今天也在等你回来。
>
> 你不用回什么，看完笑一下就行。
> 生日快乐。
>
> —— 一个成分没那么复杂、但成分里全是你的人

**★★★ 3D 生日蛋糕 + 18 岁蜡烛动画（本页最重要的特效）**
- **触发**：滚动到网页最下端时自动播放（`IntersectionObserver`）
- **必须是真 3D**，用 **Three.js 实现**
  - 优先 `../assets/vendor/three.min.js`，缺失则退化为 CDN `https://unpkg.com/three@0.149.0/build/three.min.js`
  - 不要用 ES module 版本
- 结构：三层圆柱蛋糕 + **18 根蜡烛**（内圈 6 + 外圈 12）+ 摇曳火焰
- 动画序列：
  1. `0.0s` 蛋糕升起 + 缓慢自转
  2. `0.4s` 18 根蜡烛**依次点亮**（间隔 60ms）
  3. `1.6s` 浮现金色数字 `18`
  4. `2.0s` 粒子升起
  5. `2.4s` 底部浮现 **「18 · 生日快乐」**
- **交互**：`mousemove` 时相机跟随轻微旋转
- **性能**：离开视口暂停渲染；`setPixelRatio` 上限 2
- **`prefers-reduced-motion`**：不启动动画循环，只渲染一帧静态蛋糕
- **降级**：Three.js 没加载成功时显示纯 CSS 静态蛋糕，不要留空白

**页脚（硬性要求）**
- `MADE WITH ♥ · 01017`
- **网页最下端必须出现 `by Axing`**
- 隐藏「再看一遍」按钮回顶部
- **收尾彩蛋**：默认收起的折叠按钮「**DX 熊熊全家福**」，点开显示 `../assets/maimai/` 里另外 14 只迪拉熊

---

## 硬性约束

1. **迪拉熊只有两只**，只在 S1（S7 的折叠彩蛋默认收起）。优先真实玩偶照，两套素材不要混用
2. **18 岁**必须体现：S2 的 18 根蜡烛、S7 的 3D 蛋糕、S7 的信
3. **`by Axing` 必须出现在网页最下端**
4. **背景音乐单曲循环**，左上角透明音符按钮，默认不自动播放
5. **私人照片规则**：不裁主体、不加滤镜、不拉伸、不缩小、不做背景、给有意义的 `alt`
6. **部署目标是 GitHub Pages** —— 联网访问，**允许用 Three.js**
7. **素材路径必须用相对路径 `../assets/...`**（项目站点带子路径，绝对路径会 404）
8. **文件名大小写要完全一致**（GitHub Pages 区分大小写）
9. 不要引入其他框架（React / Vue / jQuery 都不要）
10. 响应式：375 / 768 / 1440 三个宽度都要正常，375px 下无横向滚动
11. CSS 动效只用 `transform` / `opacity`（Three.js 部分不受此限）
12. 必须处理 `@media (prefers-reduced-motion: reduce)`
13. 装饰图 `alt="" aria-hidden="true"`；有意义的图给 `alt`
14. 按钮用 `<button>`，不要 `<div onclick>`
15. 不写 `<iframe>`
16. 首屏关键图预加载：`dilla_plush_big.webp`、`dilla_plush_small.webp`
17. Three.js 渲染循环**离开视口要暂停**，`setPixelRatio` 上限 2

---

## 部署

完整步骤见 [`DEPLOY.md`](DEPLOY.md)。要点：

- 素材文件名已全部改为**纯 ASCII**（避免 GitHub Pages 的 URL 编码问题）
- `.gitignore` 已排除 `assets/_raw/`（34 MB 备份，不上传）
- 仓库根需要放一个 `index.html` 跳转页指向 `web/index.html`
- 上传后仓库约 17 MB

---

## 目录参考

```
ayao-birthday/
├── docs/PLAN.md            详细规划
├── docs/HANDOFF.md         本文件
├── docs/PROMPT_FOR_GPT.md  ★ 给 GPT 的完整提示词（可直接整段复制）
├── assets/manifest.json    素材清单（含尺寸）
├── assets/personal/        ★ 私人照片（9）—— 最重要
├── assets/audio/           ★ 背景音乐 acnh_bgm.mp4
├── assets/maimai/          舞萌 / 迪拉熊（18）
├── assets/acnh/            动物森友会（16，含她喜欢的三只）
├── assets/pokemon/         宝可梦（54，含伊布家族/鬃岩狼人/剑盾）
├── assets/tomodachi/       人森 / 朋友收集（37）
├── assets/marettu/         MARETU 术曲封面（10）
├── assets/ui/              阿药 B 站元素（4）
├── assets/deco/            Twemoji 装饰 SVG（64）
├── assets/fonts/           本地字体（7 woff2）
└── web/index.html          ← 你的产出
```
