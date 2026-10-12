# 阿药生日网页 · 制作规划书

> 交付对象：**gpt6astra**（网页主体拼装）
> 素材整理与规划：本仓库 `ayao-birthday/`
> 生成时间：2026-10-12

---

## 0. 一句话需求

给女朋友 **阿药** 做一个生日惊喜网页。她 **18 岁生日**，生日是 **10 月 17 日**，那天我可能在学校，所以要用网页远程送祝福。
她是二次元，没有特定喜欢的角色，喜欢听歌（**术曲 / Vocaloid，尤其 MARETU**）。
风格二次元。装饰元素：**舞萌（maimai DX）迪拉熊 ×2 只**（主要是我喜欢，不要放太多）、**动物森友会**、**宝可梦**、**人森（朋友收集：梦想生活）**，其余元素自由发挥。

> **重要**：除了网上素材，我还提供了 **6 张私人照片**（我们俩的合照、迪拉熊玩偶实拍、养的仓鼠）和 **1 段背景音乐**。
> 这些照片的情感权重最高，是整页的核心，见第 4.0 节。

### 本次追加的四个要求（已全部落实）

1. **18 岁生日** —— 这是成年礼，不是普通生日。文案、蜡烛数量（18 根）、S7 的 3D 蛋糕动画都要体现。
2. **背景音乐** —— `assets/audio/acnh_bgm.mp4`（动森 BGM），**单曲循环**，左上角一个**透明音符按钮**控制开关。
3. **她喜欢的角色** —— 动森：**西施惠、蜜雪儿、史培亚**；宝可梦：**仙子伊布、鬃岩狼人**；
   要摆一张**伊布家族合影**；她最喜欢**剑盾**，要加剑盾知名宝可梦。
4. **S7 底部 3D 生日蛋糕 + 18 岁蜡烛动画**，网页最下端写 **by Axing**。

> ~~术曲封面加超链接跳 B 站~~ —— **此需求已取消**，不要做。

---

## 1. 目标用户画像（阿药）

从她的 B 站主页 `space.bilibili.com/614351218` 抓取到的公开信息：

| 项目 | 内容 |
| --- | --- |
| 昵称 | **Anria_01017**（她本人叫**阿药**） |
| 签名 | 「你好，我叫阿药。一个成分复杂的 intp」 |
| 性别 / 等级 | 女 / LV6 |
| 关注 / 粉丝 | 836 / 131 |
| 获赞 | 10,416 |
| 投稿 | 视频 14、追番 7、收藏夹 27、频道 1、专栏 0、音频 0、合辑 1 |
| 会员 | 年度大会员 |
| 勋章 | 「有爱楷模」名牌 |
| **年龄** | **18 岁（本次是 18 岁生日，成年礼）** |
| 头像 | 已下载 `assets/ui/aya_avatar.webp` |
| 主页头图 | 已下载 `assets/ui/aya_space_l.webp` |
| 主页小图 | 已下载 `assets/ui/aya_space_s.webp` |

**她明确喜欢的角色（本次追加，重点照顾）：**

| 类别 | 角色 | 素材 |
| --- | --- | --- |
| 动森 | **西施惠** Isabelle | `assets/acnh/isabelle.webp` |
| 动森 | **蜜雪儿** Sasha（兔，懒散性格） | `assets/acnh/sasha_mixueer.webp` |
| 动森 | **史培亚** Fang（狼，暴躁性格） | `assets/acnh/fang_shipeiya.webp` |
| 宝可梦 | **仙子伊布** Sylveon No.700 | `assets/pokemon/sylveon_700.webp` |
| 宝可梦 | **鬃岩狼人** Lycanroc（三形态齐全） | `assets/pokemon/lycanroc_*.webp` |
| 宝可梦 | **伊布家族**（9 只全） | `assets/pokemon/{eevee,vaporeon,...}_*.webp` |
| 宝可梦 | **剑盾（第八世代）是她最喜欢的世代** | `assets/pokemon/` 里 22 只剑盾宝可梦 |

**画像提炼（供文案与配色使用）：**
- **INTP**：理性、爱思考、脑内小剧场丰富、对「有趣的结构」敏感、不喜欢被强行煽情。
- **成分复杂**：涉猎广 —— 音游、术曲、动森、宝可梦、人森都玩/听，审美偏「杂食但挑」。
- **自称「你好，我叫阿药」**：句式自带一种正经又可爱的自我介绍感，网页文案可以呼应这个句式。
- **签名 + 昵称双重身份**：昵称 `Anria_01017` 中的 `01017` 与 **10 月 17 日**生日吻合（`0101`+`7`），这是很自然的隐藏彩蛋点。
- **养仓鼠**：从私人照片看，你们一起养了一只**米色仓鼠**（多张照片里出现，还有一张趴在笼顶、一张缩成球睡觉）。这是比任何网上素材都好的情感切入点。
- ⚠️ **注意区分**：她的 B 站头像是**表情包动物**（一只白色毛绒小动物），**不是仓鼠**。仓鼠是现实中的宠物。别把两者混为一谈。

**文案语气建议（重要）：**
- 用「**正经的自我介绍句式 + 突然的偏心**」这种反差。
- 不要写肉麻长抒情。INTP 更吃**克制的浪漫 + 一个只有她懂的梗**。
- 允许一点点「理科生式浪漫」（例如用数据、编号、坐标、进度条来承载情绪）。
- **私人照片是最大的武器**：一张你们俩躺在一起玩 Switch 的照片，比一千字抒情有用。
  文案要「轻」，照片要「重」——让照片说话，文字只做一句点睛。
- **18 岁要「正经地提一下」**：可以调侃成年礼（「从今天起你要为自己的每一个决定负责了……不过今天先不用」），
  但不要写成长辈式的说教。用她的语气去说，不要用「你长大了」这种空话。

---

## 2. 视觉设计规范

### 2.1 配色方案

主色调来自 **舞萌 DX 的机台蓝紫** + **动森/人森的暖木色与奶油白** + **MARETU 封面的高饱和冲击色（点缀）**。

| 角色 | 色值 | 用途 |
| --- | --- | --- |
| `--c-bg-deep` | `#12102A` | 深色背景基底（夜空/机房感） |
| `--c-bg-soft` | `#1E1B3A` | 次级背景块 |
| `--c-card` | `#FFFDF7` | 卡片奶油白（动森纸张感） |
| `--c-wood` | `#D9A45B` | 动森木色（边框、木牌） |
| `--c-wood-dark` | `#A9762F` | 木色阴影 |
| `--c-maimai-blue` | `#2BB3E8` | 舞萌机台蓝（主强调色） |
| `--c-maimai-pink` | `#F5539E` | 舞萌按键粉（次强调色） |
| `--c-maimai-yellow` | `#FFD23F` | 舞萌黄（高亮/分数） |
| `--c-maretu-red` | `#E8202A` | MARETU 冲击红（危险/高潮点缀，慎用） |
| `--c-leaf` | `#7BC96F` | 动森叶子绿 |
| `--c-text` | `#2B2740` | 正文深紫灰 |
| `--c-text-dim` | `#6E6A8A` | 次要文字 |

**用色纪律：**
- 深色底 + 奶油白卡片 = 主结构。
- 舞萌蓝/粉只用于**交互反馈和强调**，不铺大面积。
- MARETU 红**只在最后一个 section 或某一瞬间出现**，用来做情绪爆点，全页出现不超过 2 次。

### 2.2 字体（已全部本地化，不依赖外网）

| 用途 | 字体 | 本地文件 |
| --- | --- | --- |
| 标题 / 大字号可爱体 | **ZCOOL KuaiLe（站酷快乐体）** | `assets/fonts/zcool-kuaile-400.woff2` |
| 日文/术曲标题 | **Hachi Maru Pop** | `assets/fonts/hachi-maru-pop-400.woff2` |
| 圆润装饰标题 | **Mochiy Pop One** | `assets/fonts/mochiy-pop-one-400.woff2` |
| 日文正文 | **Zen Maru Gothic 400/700** | `assets/fonts/zen-maru-gothic-400.woff2` / `-700.woff2` |
| 中文正文 | **Noto Sans SC 400/700** | `assets/fonts/noto-sans-sc-400.woff2` / `-700.woff2` |

```css
/* gpt6astra 直接使用：字体已本地化，禁止改成 Google Fonts 外链 */
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

### 2.3 整体风格关键词

`深蓝夜空` + `奶油白卡片` + `动森木牌` + `音游判定特效` + `像素/贴纸感` + `克制的温柔`

### 2.3b 背景音乐（BGM）

**文件**：`assets/audio/acnh_bgm.mp4`（动森背景音乐，AAC / 48kHz 立体声，约 90 秒）

**播放要求：**
- **单曲循环** —— `<audio loop>`
- **默认不自动播放** —— 浏览器会拦截自动播放，而且突然出声会吓到人
- 首次用户交互（点击/滚动/触摸）后尝试播放
- **左上角一个透明音符按钮**控制播放/暂停，见下方规格

**音符按钮规格：**

```html
<!-- 固定在左上角，z-index 要高于内容 -->
<button id="bgm-toggle" aria-label="背景音乐开关" aria-pressed="false">
  <img src="../assets/deco/note.svg" alt="" aria-hidden="true">
</button>
```

```css
#bgm-toggle{
  position:fixed; top:16px; left:16px; z-index:9999;
  width:44px; height:44px; padding:0;
  display:flex; align-items:center; justify-content:center;
  background:rgba(255,253,247,.10);          /* 透明底 */
  border:2px solid rgba(255,253,247,.28);
  border-radius:50%;
  backdrop-filter:blur(6px);
  cursor:pointer;
  transition:transform .2s, background .2s, border-color .2s;
  /* 移动端别被状态栏挡到 */
  margin:env(safe-area-inset-top) 0 0 env(safe-area-inset-left);
}
#bgm-toggle img{ width:22px; height:22px; opacity:.85; }
#bgm-toggle:hover{ background:rgba(255,253,247,.20); border-color:var(--c-maimai-yellow); transform:scale(1.08); }
#bgm-toggle[aria-pressed="true"]{ border-color:var(--c-maimai-yellow); background:rgba(255,210,63,.18); }
#bgm-toggle[aria-pressed="true"] img{ opacity:1; }
/* 播放时轻微脉动，提示「正在响」 */
#bgm-toggle[aria-pressed="true"]{ animation:bgm-pulse 2s ease-in-out infinite; }
@keyframes bgm-pulse{
  0%,100%{ box-shadow:0 0 0 0 rgba(255,210,63,.35); }
  50%    { box-shadow:0 0 0 8px rgba(255,210,63,0); }
}
@media (prefers-reduced-motion: reduce){ #bgm-toggle{ animation:none !important; } }
```

**JS 逻辑（要点）：**

```js
const audio = new Audio('../assets/audio/acnh_bgm.mp4');
audio.loop = true;                 // 单曲循环
audio.volume = 0.35;               // 别太吵，做背景

const btn = document.getElementById('bgm-toggle');
let started = false;

function tryPlay(){
  audio.play().then(() => {
    btn.setAttribute('aria-pressed', 'true');
    started = true;
  }).catch(() => { /* 被拦了，等下次交互 */ });
}

// 首次交互后自动开始
['click','touchstart','keydown'].forEach(ev =>
  document.addEventListener(ev, function once(){
    if(!started) tryPlay();
    document.removeEventListener(ev, once);
  }, {once:false, passive:true})
);

// 按钮切换
btn.addEventListener('click', e => {
  e.stopPropagation();             // 别触发上面那个 once
  if(audio.paused){ tryPlay(); }
  else { audio.pause(); btn.setAttribute('aria-pressed','false'); }
});
```

**注意事项：**
- 按钮要在**所有 section 之上**，滚动时不消失（`position:fixed`）。
- 手机端要避开刘海/状态栏，用 `env(safe-area-inset-*)`。
- 用户手动暂停后，**不要再自动播放**（记住 `started` 状态）。
- 提供 `prefers-reduced-motion` 时去掉脉动动画（但不影响音频本身）。

### 2.4 布局与响应式

- 单页纵向滚动，**7 个 section**（见第 3 节）。
- 断点：`≥1024px` 桌面 / `768–1023px` 平板 / `<768px` 手机。
- 手机优先：所有关键内容在 375px 宽下可读，字号不低于 14px。
- 最大内容宽度 `1080px`，居中。
- 卡片圆角 `20–28px`，配 `2–3px` 实线深色描边（贴纸/徽章感），阴影用「硬阴影」`4px 4px 0 rgba(0,0,0,.35)` 而不是柔和模糊。

---

## 3. 页面结构（7 个 Section）

### S0 · 加载 / 入场
- 全屏深色遮罩，中央是一只**迪拉熊**在跳，脚下是音游判定圈 `TAP → PERFECT` 的扩散动画。
- 进度条伪装成 **maimai 判定条**，加载完成弹出「**PERFECT!**」再淡出。
- 顶部小字：`LOADING ... 为阿药准备的第 01017 号惊喜`
- 素材：**首选真实玩偶照** `assets/personal/dilla_plush_big.webp`；官方立绘 `assets/maimai/dilla_01_base.webp` 作备选。
- **这里也是启动 BGM 的最好时机** —— 加载页必然需要点击「进入」，顺势在点击时 `audio.play()`。
  进入按钮文案可以是 `▶ 进入` 或 `TAP TO START`（音游梗）。

### S1 · Hero 主视觉
- 大标题：**「生日快乐，阿药。」**
- 副标题（呼应她的自我介绍句式）：**「你好，我叫阿药。一个成分复杂的 intp。—— 今天这一页，是专门为你一个人开的服务器。」**
- 背景：夜空渐变 + 缓慢飘落的**音符/叶子/星星**（twemoji SVG，`assets/deco/note.svg` `leaf.svg` `star.svg`）。
- 中央放**两只迪拉熊**——这是明确要求，**只放这两只，不要再多**。

  **方案 A（推荐）· 真实玩偶照**：
  - 左：`assets/personal/dilla_plush_big.webp`（大只玩偶，实拍）
  - 右：`assets/personal/dilla_plush_small.webp`（小只挂件，实拍）
  - 或者直接用整张合影 `assets/personal/dilla_plush_pair.webp` 当主视觉，两张小图做点缀。
  - **为什么优先**：这是你真的拥有的玩偶，比官方立绘多了「我们」的意味。

  **方案 B（备选）· 官方立绘**：
  - 左：`assets/maimai/dilla_01_base.webp`（原版蓝）
  - 右：`assets/maimai/dilla_07_lime.webp`（青绿）
  - 两套**不要同时出现**，会显得杂乱。

- 两只都做轻微上下浮动，相位错开；底部一个向下箭头 + `SCROLL` 提示。
- **彩蛋**：标题的「生日」二字 hover 时轻微变形成 `01017` 的样式。

### S2 · 18 岁生日蛋糕 / 蜡烛交互
- 中间一个大蛋糕（**用 CSS + twemoji 的 `cake.svg` / `cupcake.svg` / `candy.svg` / `cherry.svg` 拼**，不依赖外部插画）。
- **18 根蜡烛** —— 这是成年礼，蜡烛必须是 18 根（排成 2 排各 9 根，或围成一圈）。
- **交互：吹蜡烛** —— 点击「吹蜡烛」按钮或麦克风吹气（可选），蜡烛依次熄灭 → 弹出礼花（`party.svg` + CSS 粒子）。
- 熄灭后文案：**「18 根都吹灭了。愿望已经收到，剩下的交给时间。」**
- 副标题点一下成年：**「从今天起，你要为自己的每一个决定负责了。—— 不过今天先不用。」**
- 背景点缀：宝可梦 `assets/pokemon/pikachu_025.webp`、`eevee_133.webp`、`jigglypuff_039.webp` 从蛋糕后探头。
- 动森元素：`assets/acnh/leaf_icon.webp` 做叶子飘落。
- **新增**：蛋糕旁边放一张**方形合照** `assets/personal/us_switch_square.webp`，做成「拍立得 / 相框」样式，
  配一行小字：「上一次一起过生日，也是这样躺着的。」—— 把回忆接到当下。
- **18 的数字要显眼**：可以把「18」做成蛋糕上的数字蜡烛，或者用 `--c-maimai-yellow` 高亮标出。

### S3 · 歌单 · 给阿药的术曲电台
**这是最贴合她爱好的 section，要做足。**

- 外壳做成**音乐播放器 / 磁带机 / CD 机**的样式，带转动的唱片。
- 标题：**「MARETU 电台 · 深夜档」** 副标题：`for 阿药 · 成分复杂频道`
- 展示 10 首 MARETU 曲目卡片（素材已全部下载，见第 4 节 `marettu/`）：
  1. マインドブランド / Mind Brand
  2. うみなおし / 海直し
  3. ホワイトハッピー / White Happy
  4. コインロッカーベイビー / Coin Locker Baby
  5. マエガミスト / Maegamist
  6. うみたがり / Umitagari
  7. しう / Shiu
  8. ドクハク / Dokuhaku
  9. ビノミウリ / Binomiuri
  10. スヌスムムリク / Sunusumumuriku
- 每张卡片：封面图（`assets/marettu/*.webp`）+ 曲名（日文用 Hachi Maru Pop）+ 罗马音/中文小字。
- 点击卡片 → 卡片翻转，背面写一句**你（我）对阿药的话**，或者一句和曲子气质呼应的短句。
  - 例：マインドブランド → 「这首的鼓点，我第一个想到的是你打字的速度。」
- **转场彩蛋**：翻到第 4 张（コインロッカーベイビー）时，整页色调瞬间切到 `--c-maretu-red`，0.6s 后恢复。全页仅此一次。
- **第二彩蛋（新增）**：翻到第 6 张（うみたがり）时，从卡片背面弹出一张**仓鼠缩成球的照片** `assets/personal/hamster_ball.webp`
  —— 因为这张照片本身就带漫画「!?」特效，直接当表情包用，配合一句：「这张图是它睡成这样的样子。我当时也这个表情。」
- 底部放一条假「播放进度条」，拖不动，但 hover 会出现 `PERFECT` 判定字样。

### S4 · 动森 · 小岛留言板（含她喜欢的村民）

> **她明确喜欢的三只村民必须都出现：西施惠、蜜雪儿、史培亚。**

- 做成**动物森友会里那种木牌 / 公告板**（木色边框 + 奶油白底）。
- 标题：**「岛上公告」** —— 用动森的语气写几条「公告」：
  - 「今日天气：晴。风力：刚好能吹灭 18 根蜡烛。」
  - 「岛上来了新居民，名字叫阿药。生日：10 月 17 日。年龄：18。」
  - 「狸克说，今天所有商品免费。……骗你的，但蛋糕是真的。」
- **村民展示（按她的喜好排优先级）：**
  - `assets/acnh/isabelle.webp`（**西施惠**）—— 主位，居中或左侧，她的最爱
  - `assets/acnh/sasha_mixueer.webp`（**蜜雪儿**，兔，懒散性格）—— 右侧
  - `assets/acnh/fang_shipeiya.webp`（**史培亚**，狼，暴躁性格）—— 左侧
  - `assets/acnh/kk_slider.webp`（K.K.）—— 中下，做氛围
  - `assets/acnh/celeste.webp`（傅珂）—— 右上，小装饰
  - 备用（狼村民同好，可放在「岛上其他居民」小头像排）：`skye.webp` `chief.webp` `whitney.webp`
- **给这三只各写一句「它们的台词」**（动森村民说话有种可爱的笨拙感）：
  - 西施惠：「今天的公告板我特意擦干净了。生日快乐呀！」
  - 蜜雪儿：「唔……我本来想给你烤个蛋糕，结果自己吃掉了。抱歉。」
  - 史培亚：「这倒是……挺不错的。生日快乐，小子。」

### S5 · 宝可梦 · 图鉴 + 伊布家族合影 + 剑盾专区

> **她明确喜欢的：仙子伊布、鬃岩狼人、伊布家族合影、剑盾世代。这一节要重点做。**

**5a. 图鉴卡片**
- 做成**宝可梦图鉴的卡片网格**，每张卡片是一个「阿药观察记录」：
  - 卡片头：`No.01017  阿药`（编号用她昵称里的 01017）
  - 属性：`思考系 / 音乐系`
  - 特性：`成分复杂`、`深夜术曲专精`
  - 描述文字：写 4–6 条可爱的「图鉴说明」。
- 加一条**仓鼠条目**，配图 `assets/personal/hamster_face.webp`：
  - `No.00001  仓鼠` · 属性 `毛绒系 / 半夜跑轮系` · 特性 `缩成球`
  - 说明：「两人共同持有。攻击力 0，可爱度溢出。」

**5b. 伊布家族合影（本次新增，重点）**
- 用 **9 只伊布家族**排成一张合影，做成「家族全家福」的感觉：
  ```
  伊布 eevee_133          水伊布 vaporeon_134    雷伊布 jolteon_135
  火伊布 flareon_136      太阳伊布 espeon_196    月亮伊布 umbreon_197
  叶伊布 leafeon_470      冰伊布 glaceon_471     仙子伊布 sylveon_700 ★
  ```
- **仙子伊布要 C 位**（她最喜欢）—— 放中间、放大一点、加一点 `--c-maimai-pink` 的柔光。
- 排版建议：中间一只大的（仙子伊布），周围 8 只小的围成半圆或网格。
- 标题：**「伊布家族，全员到齐。」** 副标题：`No.133 – No.700`
- 如果空间允许，每只下面标一行小字（名字 + 属性）。

**5c. 鬃岩狼人 · 三形态（本次新增）**
- 鬃岩狼人有**三个形态**，全部已下载，**建议三个一起展示**（对比感很有意思）：
  - `lycanroc_745_midday.webp` —— **白昼形态**（橙色，白天进化）
  - `lycanroc_10126_midnight.webp` —— **黑夜形态**（灰红，夜晚进化）
  - `lycanroc_10152_dusk.webp` —— **黄昏形态**（橙白，黄昏进化，最稀有）
- 排版：横向三格，中间那格稍大。
- 标题：**「同一只狼，三个时间段。」** 副标题：`昼 / 夜 / 黄昏`
- 小字可写：`它随你什么时候遇见它而改变样子。`（这种句子很 INTP）

**5d. 剑盾专区（她最喜欢的世代，本次新增）**
- 标题：**「第八世代 · 伽勒尔地区」** 副标题：`她最喜欢的世代`
- 从已下载的 22 只里挑，按类别分：
  - **御三家**：敲音猴 `grookey_810`、炎兔儿 `scorbunny_813`、泪眼蜥 `sobble_816`
    + 最终进化：轰擂金刚猩 `rillaboom_812`、闪焰王牌 `cinderace_815`、千面避役 `inteleon_818`
  - **传说**：苍响 `zacian_888`（+ 剑之王 `zacian_10188_crowned`）、
    藏玛然特 `zamazenta_889`（+ 盾之王 `zamazenta_10189_crowned`）、无极汰那 `eternatus_890`
  - **知名对战/人气**：钢铠鸦 `corviknight_823`、多龙巴鲁托 `dragapult_887`、
    颤弦蝾螈 `toxtricity_849`、长毛巨魔 `grimmsnarl_861`、葱游兵 `sirfetchd_865`、列阵兵 `falinks_870`
  - **可爱系**：毛辫羊 `wooloo_831`、霜奶仙 `alcremie_869`、雪吞虫 `snom_872`、
    莫鲁贝可 `morpeko_877`、来电汪 `yamper_835`
  - **DLC**：熊徒弟 `kubfu_891`、武道熊师 `urshifu_892`
- 苍响/藏玛然特建议用**双形态并排**（普通 + 王形态），视觉冲击最强。

**5e. 徽章**
- 用 twemoji `medal.svg` `trophy.svg` `diamond.svg` `star2.svg` 做成 8 枚假道馆徽章（伽勒尔道馆梗）。

**5f. 其他装饰宝可梦**
- `eevee_133`、`mimikyu_778`、`snorlax_143`、`slowpoke_079`、`psyduck_054`、`togepi_175`、`mareep_179` 按需点缀。

### S6 · 人森（朋友收集：梦想生活）· 居民卡
- 用 Nintendo 官方素材做**居民卡 / Mii 风格卡片**。
- 标题：**「我的岛上，已经给你留好位置了。」**
- 卡片内容：
  - 居民名：`阿药`
  - 性格：`INTP（自我诊断 100% 准确）`
  - 口头禅：`「成分复杂」`
  - 喜欢的东西：`术曲、舞萌、动森、宝可梦、仓鼠`
  - 讨厌的东西：`（留白，让她自己填）`
- **头像**：优先用 `assets/personal/hamster_avatar.webp`（你们养的仓鼠，圆形裁切）作为「岛上的化身」；
  她的 B 站头像 `assets/ui/aya_avatar.webp` 放旁边做小徽章，两个并列，一个代表「现实里的我们」，一个代表「网上的你」。
- **配图**：`assets/personal/hamster_cage.webp`（竖图，仓鼠趴笼顶）放在卡片右侧，手机端自动移到下方。
- 装饰：`assets/tomodachi/tomo_logo.webp`、`tomo_obj_resident.webp`、`tomo_sticker_*.webp`（做贴纸）、`tomo_ic_*.webp`（做图标）。
- 用 `tomo_island_*.webp` 或 `tomo_kv_*.webp` 做这一节的背景（调低透明度当纹理）。

### S7 · 结尾 · 只属于 01017 的一封信 + 3D 生日蛋糕动画

**7a. 核心照片**
- 深色收尾，背景是星空 + 缓慢旋转的唱片。
- **核心照片**：`assets/personal/us_switch.webp`（你们俩躺在一起玩 Switch）。
  - 建议做成**大幅、居中、圆角、带轻微投影**的样子，先出图，再出字。
  - 图片下方一行小字（用 `--c-text-dim`）：`某个普通的晚上 · 谁也没赢`
  - 这张图是整页的情感落点，**不要缩小、不要做背景、不要加滤镜**。

**7b. 信**
- 标题：**「最后一句，不绕圈子了。」**
- 正文（**这是核心文案，gpt6astra 可直接用，也可微调**）：

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

- 落款下方放一个 **签名区**，留一个 `[ 你的名字 ]` 占位符给 gpt6astra 替换。

**7c. ★ 3D 生日蛋糕 + 18 岁蜡烛动画（本次新增，重点）**

**触发时机**：用户**滚动到网页最下端**时自动播放（`IntersectionObserver` 监听 S7 底部）。

**技术要求：**
- **必须是真的 3D**，不是平面图。**用 Three.js 实现**（部署到 github.io 后本来就联网访问，
  不再要求「断网可用」，所以 Three.js 是允许的）。
- **引入方式**：
  - 优先本地 vendor：`<script src="../assets/vendor/three.min.js"></script>`
  - 缺失时退化为 CDN：`<script src="https://unpkg.com/three@0.149.0/build/three.min.js"></script>`
  - **不要用 ES module 版本**（避免 `type="module"` 与本地 `file://` 调试冲突）
- 蛋糕结构（Three.js）：
  - 相机 + 环境光 + 一个带阴影的方向光
  - 三层圆柱体（`CylinderGeometry`），从下到上依次变小
  - 顶层奶油 + 若干小球体（樱桃）
  - **18 根蜡烛**：细圆柱，内圈 6 根 + 外圈 12 根均匀分布
  - **火焰**：每根蜡烛顶部一个小球，`--c-maimai-yellow` 自发光材质 + 缩放摇曳
- **动画序列**（滚动进入视口后依次触发）：
  1. `0.0s` 蛋糕从下方升起 + 缓慢自转（`rotation.y` 持续增加）
  2. `0.4s` 18 根蜡烛**依次点亮**（每根间隔 60ms，火焰 `scale` 0 → 1）
  3. `1.6s` 浮现金色数字 `18`（Canvas 贴图或 HTML 叠加层）
  4. `2.0s` 粒子升起（`Points` 或若干小 Sprite）
  5. `2.4s` 底部浮现 **「18 · 生日快乐」**（HTML 叠加层即可）
- **交互**：`mousemove` 时相机跟随轻微旋转，增强 3D 感。
- **性能**：
  - `requestAnimationFrame` 驱动，**离开视口时暂停渲染**（省电，尤其手机上）
  - `renderer.setPixelRatio(Math.min(devicePixelRatio, 2))`
  - `resize` 时更新相机宽高比
- **`prefers-reduced-motion`**：**不启动动画循环**，只渲染一帧静态蛋糕（蜡烛全部点亮）。
- **降级**：Three.js 没加载成功时（`typeof THREE === 'undefined'`），
  显示一个纯 CSS 静态蛋糕兜底，**不要留空白**。

**参考骨架（Three.js）：**

```js
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45, w / h, 0.1, 100);
camera.position.set(0, 3, 9);

const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(w, h);

scene.add(new THREE.AmbientLight(0xffffff, 0.6));
const dir = new THREE.DirectionalLight(0xffd23f, 1.1);
dir.position.set(5, 8, 6);
scene.add(dir);

// 蛋糕：三层圆柱
function layer(rTop, rBottom, height, y, color) {
  const m = new THREE.Mesh(
    new THREE.CylinderGeometry(rTop, rBottom, height, 48),
    new THREE.MeshStandardMaterial({ color, roughness: 0.7 })
  );
  m.position.y = y;
  return m;
}

const cake = new THREE.Group();
cake.add(layer(1.5, 1.5, 0.6, 0.3, 0xfffdf7));   // 底层（奶油白）
cake.add(layer(1.2, 1.2, 0.55, 0.87, 0xd9a45b));  // 中层（动森木色）
cake.add(layer(0.95, 0.95, 0.5, 1.4, 0xfffdf7));  // 顶层
scene.add(cake);

// 18 根蜡烛：内圈 6 + 外圈 12
const candles = [];
function addCandles(count, r) {
  for (let i = 0; i < count; i++) {
    const a = (i / count) * Math.PI * 2;
    const c = new THREE.Mesh(
      new THREE.CylinderGeometry(0.045, 0.045, 0.5, 12),
      new THREE.MeshStandardMaterial({ color: 0xfffdf7 })
    );
    c.position.set(Math.cos(a) * r, 1.75, Math.sin(a) * r);

    const f = new THREE.Mesh(          // 火焰
      new THREE.SphereGeometry(0.07, 12, 12),
      new THREE.MeshBasicMaterial({ color: 0xffd23f })
    );
    f.position.y = 0.32;
    f.scale.setScalar(0);              // 初始不亮
    c.add(f);

    candles.push({ mesh: c, flame: f });
    cake.add(c);
  }
}
addCandles(6, 0.45);    // 内圈
addCandles(12, 0.85);   // 外圈  -> 共 18 根

function animate(t) {
  requestAnimationFrame(animate);
  cake.rotation.y += 0.003;
  // 蜡烛依次点亮，每根间隔 60ms
  candles.forEach((c, i) => {
    const start = 400 + i * 60;
    const p = Math.min(1, Math.max(0, (t - start) / 300));
    c.flame.scale.setScalar(p * (1 + Math.sin(t / 200 + i) * 0.12));
  });
  renderer.render(scene, camera);
}
```

**7d. 页脚**
- 最底部：`MADE WITH ♥ · 01017`
- **网页最下端写 `by Axing`** —— 这是明确要求，**必须出现**。
  建议样式：小字号、`--c-text-dim` 颜色，居中，和 `MADE WITH ♥` 在同一行或下一行。
  ```html
  <footer class="site-footer">
    <p>MADE WITH ♥ · 01017</p>
    <p class="by">by Axing</p>
  </footer>
  ```
  ```css
  .site-footer{ text-align:center; color:var(--c-text-dim); font-size:13px; padding:40px 0 32px; }
  .site-footer .by{ font-family:var(--font-title); font-size:15px; letter-spacing:.08em;
                    color:var(--c-maimai-yellow); margin-top:6px; }
  ```
- 以及一个隐藏按钮「**再看一遍**」滚动回顶部。
- **收尾彩蛋**：页面最底部放一个默认收起的折叠按钮「**DX 熊熊全家福**」，
  点开才显示 `assets/maimai/` 里另外 14 只迪拉熊 —— 既满足了「不要放太多」，又留了给懂的人看的彩蛋。

---

## 4. 素材清单（已全部下载并本地化）

> 所有素材已从网络下载到本地，**不要改成外链**。
> 原始文件备份在 `assets/_raw/<分类>/`，网页用优化后的 `.webp`。
> 完整清单见 `assets/manifest.json`。

### 4.0 ★ 私人照片 — `assets/personal/`（9 个文件）· 最重要

**这些是你自己提供的真实照片，情感权重高于一切网上素材。**
原始文件备份在 `assets/_raw/personal/`。

| 文件 | 内容 | 尺寸 | 用途 |
| --- | --- | --- | --- |
| `us_switch.webp` | **你们俩躺床上一起玩 Switch**（穿宝可梦睡衣） | 1200×872 | **S7 结尾核心照片** |
| `us_switch_square.webp` | 同上，方形裁切版 | 640×640 | S2 拍立得相框 / 任意方形卡位 |
| `dilla_plush_pair.webp` | **两只迪拉熊实物玩偶**（舞萌 DX 官方周边，带吊牌） | 1200×828 | S1 主视觉（整张） |
| `dilla_plush_big.webp` | 大只迪拉熊玩偶特写 | 540×700 | **S1 左侧** / S0 加载动画 |
| `dilla_plush_small.webp` | 小只迪拉熊挂件特写 | 514×700 | **S1 右侧** |
| `hamster_avatar.webp` | 仓鼠正脸（圆形裁切版） | 600×600 | **S6 居民卡头像** |
| `hamster_face.webp` | 仓鼠特写 | 600×600 | S5 图鉴「仓鼠条目」 |
| `hamster_ball.webp` | 仓鼠缩成球睡觉 + 漫画「!?」特效 | 720×720 | **S3 彩蛋** / S5 表情包位 |
| `hamster_cage.webp` | 仓鼠趴笼顶（竖图，已裁掉手机状态栏） | 423×900 | S6 竖版配图 |

**使用纪律（重要）：**
1. **不要裁掉主体** —— 玩偶的吊牌、仓鼠的爪子都是有信息量的细节。
2. **不要加滤镜** —— 不要黑白、不要复古、不要高对比。原图本身就够好。
3. **不要拉伸** —— 用 `object-fit: contain` 或按原比例缩放。
4. **不要缩小到看不清** —— `us_switch` 在 S7 要占据足够大的面积。
5. 私人照片**不要做背景底图**（会被文字盖住、失去意义），要**单独成块展示**。

**素材来源说明**：这 6 张原图由用户本人提供（`我们俩.jpg`、`她的头像.jpg`、`老鼠.jpg`、`老鼠1.jpg`、`老鼠2.jpg`、以及一张迪拉熊玩偶照）。
原图里 `她的头像.jpg` 这个名字有歧义 —— 它其实是**仓鼠照片**，不是她的 B 站头像（B 站头像是表情包动物，见 4.6 节）。

### 4.1b 音频 — `assets/audio/`（1 个文件）

| 文件 | 说明 | 用途 |
| --- | --- | --- |
| `acnh_bgm.mp4` | **动森背景音乐**（AAC / 48kHz 立体声，约 90 秒，1.46 MB） | 全站 BGM，**单曲循环**，左上角透明音符按钮控制 |

- 浏览器原生可播（`<audio>` 直接吃 mp4 里的 AAC 音轨），**不需要转码**。
- 默认不自动播放，首次交互后开始。
- 详见 2.3b 节的按钮规格与 JS 逻辑。

### 4.1c 舞萌 / 迪拉熊 — `assets/maimai/`（18 个文件）

| 文件 | 说明 | 用途 |
| --- | --- | --- |
| `dilla_01_base.webp` | 迪拉熊（原版蓝，DX 无印启程区域） | **S1 主视觉左**、S0 加载动画 |
| `dilla_02_ietek.webp` | 雪人熊熊（いえてぃっくま） | 备用 |
| `dilla_03_risuk.webp` | 栗子熊熊（りすっくま） | 备用 |
| `dilla_04_panda.webp` | 熊猫熊熊（ぱんだっくま） | 备用 |
| `dilla_05_mitsuyoshi.webp` | 光吉熊熊 | 备用 |
| `dilla_06_aoharu.webp` | 青春熊熊（あおはるっくま） | 备用 |
| `dilla_07_lime.webp` | 酸橙熊熊（らいむっくま，青绿） | **S1 主视觉右** |
| `dilla_08_lemon.webp` | 柠檬熊熊 | 备用 |
| `dilla_09_splash.webp` | Splash 版迪拉熊 | 备用 |
| `dilla_10_universe3.webp` | UNiVERSE 版迪拉熊 | 备用 |
| `dilla_11_universe4.webp` | UNiVERSE 版柠檬熊 | 备用 |
| `dilla_12_universe5.webp` | UNiVERSE 版酸橙熊 | 备用 |
| `dilla_13_tanuki.webp` | 狸子熊熊 | 备用 |
| `dilla_14_ninja.webp` | 忍者熊熊 | 备用 |
| `dilla_15_dragon.webp` | 恶龙熊熊 | 备用 |
| `dilla_16_blackrose.webp` | 黑蔷薇熊熊 | 备用 |
| `maimai_favicon.webp` | maimai 官网 favicon | 网站 favicon |
| `maimai_touchicon.webp` | maimai 官网 touch icon | PWA / 苹果图标 |

> ⚠️ **用户明确要求：迪拉熊只放两只做装饰。**
> **优先用真实玩偶照**（`assets/personal/dilla_plush_big` + `dilla_plush_small`，或整张 `dilla_plush_pair`），
> 因为那是你真的拥有的玩偶。官方立绘 `dilla_01_base` / `dilla_07_lime` 作为备选，**两套不要同时出现**。
> 其余 14 只全部作为「DX 熊熊全家福」彩蛋，放在 S7 结尾的默认收起折叠区里。

### 4.2 动物森友会 — `assets/acnh/`（16 个文件）

| 文件 | 角色 | 建议用途 |
| --- | --- | --- |
| `isabelle.webp` | **西施惠 Isabelle** | **S4 主位（她的最爱）** |
| `sasha_mixueer.webp` | **蜜雪儿 Sasha**（兔，懒散性格） | **S4 右侧（她喜欢）** |
| `fang_shipeiya.webp` | **史培亚 Fang**（狼，暴躁性格） | **S4 左侧（她喜欢）** |
| `kk_slider.webp` | K.K. Slider | S4 中下氛围 |
| `celeste.webp` | 傅珂 Celeste | S4 右上小装饰 |
| `tom_nook.webp` | 狸克 Tom Nook | S4 备用 |
| `blathers.webp` | 傅达 Blathers | S4 备用 |
| `redd.webp` | 狐利 Redd | 备用（神秘商人彩蛋） |
| `zucker.webp` | 章丸丸 Zucker | 备用 |
| `marshal.webp` | 小润 Marshal | 备用 |
| `diana.webp` | 艳后 Diana | 备用 |
| `skye.webp` | 史凯 Skye（狼） | 「岛上其他居民」小头像排 |
| `chief.webp` | 阿猪 Chief（狼） | 同上 |
| `whitney.webp` | 白女士 Whitney（狼） | 同上 |
| `merengue.webp` | 蜜糖 Merengue（犀牛） | 备用 |
| `leaf_icon.webp` | 动森叶子图标 | **全站飘落叶子、S2 点缀** |

### 4.3 宝可梦 — `assets/pokemon/`（54 个文件）

全部为官方 artwork（PokeAPI sprites 仓库），600px 长边，透明背景。

**基础 18 只：**
`pikachu_025` `eevee_133` `jigglypuff_039` `snorlax_143` `mew_151` `slowpoke_079` `psyduck_054` `gengar_094` `bulbasaur_001` `charmander_004` `squirtle_007` `togepi_175` `mareep_179` `piplup_393` `rowlet_722` `mimikyu_778` `magikarp_129` `ditto_132`

**★ 伊布家族（9 只全，做合影）** — `eevee_133` `vaporeon_134` `jolteon_135` `flareon_136` `espeon_196` `umbreon_197` `leafeon_470` `glaceon_471` `sylveon_700`

**★ 鬃岩狼人（3 形态）** — `lycanroc_745_midday`（白昼）`lycanroc_10126_midnight`（黑夜）`lycanroc_10152_dusk`（黄昏）
> ⚠️ 编号坑：PokeAPI 里 **745=白昼、10126=黑夜、10152=黄昏**。`10153` 是波士可多拉Mega，不是狼，别用错。

**★ 剑盾 / 第八世代（22 只）** — `grookey_810` `scorbunny_813` `sobble_816` `rillaboom_812` `cinderace_815` `inteleon_818` `zacian_888` `zacian_10188_crowned` `zamazenta_889` `zamazenta_10189_crowned` `eternatus_890` `corviknight_823` `dragapult_887` `toxtricity_849` `grimmsnarl_861` `wooloo_831` `alcremie_869` `snom_872` `morpeko_877` `kubfu_891` `urshifu_892` `sirfetchd_865` `falinks_870` `yamper_835`

### 4.4 人森 / 朋友收集：梦想生活 — `assets/tomodachi/`（37 个文件）

来自任天堂日本官网 `nintendo.com/jp/switch/blfga/` 官方素材。

| 文件 | 说明 | 用途 |
| --- | --- | --- |
| `tomo_logo.webp` | 游戏 logo | **S6 标题装饰** |
| `tomo_kv_1.webp` / `tomo_kv_2.webp` | 主视觉大图 | S6 背景（降低透明度） |
| `tomo_pickup.webp` | 精选大图 | S6 备用背景 |
| `tomo_obj_resident.webp` | 居民相关物件 | **S6 装饰** |
| `tomo_obj_island_1/2.webp` | 岛屿物件 | S6 装饰 |
| `tomo_obj_daily_1/2/3.webp` | 日常物件 | S6 装饰 |
| `tomo_sticker_1/2/3/4.webp` | 贴纸 | **S6 贴纸点缀（很好用）** |
| `tomo_ic_make/enjoy/rel/create/item.webp` | 菜单图标 | **S6 图标** |
| `tomo_resident_1/2/3/4.webp` | 居民截图 | S6 内容示意 |
| `tomo_island_1/2/3/4.webp` | 岛屿截图 | S6 背景纹理 |
| `tomo_about_1/2/4/6.webp` | 介绍图 | S6 备用 |
| `tomo_daily_1/2/3.webp` | 日常截图 | S6 备用 |
| `tomo_bird.webp` | 小鸟装饰 | S6 装饰 |
| `tomo_bowling.webp` | 保龄球小游戏 | S6 彩蛋 |
| `tomo_product.webp` | 商品图 | 备用 |

### 4.5 MARETU / 术曲 — `assets/marettu/`（10 个文件）

均为对应曲目官方 PV 封面（YouTube 缩略图，1280×720）。

| 文件 | 曲名 |
| --- | --- |
| `mind_brand.webp` | マインドブランド / Mind Brand |
| `umi_naoshi.webp` | うみなおし |
| `white_happy.webp` | ホワイトハッピー / White Happy |
| `coin_locker_baby.webp` | コインロッカーベイビー |
| `maegamist.webp` | マエガミスト / Maegamist |
| `umitagari.webp` | うみたがり |
| `shiu.webp` | しう |
| `dokuhaku.webp` | ドクハク |
| `binomiuri.webp` | ビノミウリ |
| `sunusumumuriku.webp` | スヌスムムリク |

> 注：文件名里 `__` 前面是罗马音，后面是日文原名。gpt6astra 生成卡片时**用日文原名做标题**，罗马音做副标题。

### 4.6 阿药 B 站元素 — `assets/ui/`（4 个文件）

| 文件 | 说明 | 用途 |
| --- | --- | --- |
| `aya_avatar.webp` | 她的 B 站头像 | S6 居民卡头像 / S1 角落小头像 |
| `aya_space_l.webp` | 主页大图 | S1 背景纹理（低透明度） |
| `aya_space_s.webp` | 主页小图 | 备用 |
| `aya_nameplate.webp` | 「有爱楷模」名牌 | S5 徽章区 / S7 装饰 |

> **注意**：`aya_avatar` 是她的真实头像，使用时建议做**圆形裁切 + 描边**，不要拉伸。

### 4.7 装饰 Emoji（Twemoji，本地 SVG）— `assets/deco/`（64 个文件）

全部为 MIT/CC-BY 授权的 Twitter Twemoji SVG，可自由使用。

- **音乐类**：`note.svg` `notes.svg` `music_mic.svg` `headphone.svg` `cd.svg` `tape.svg` `video.svg` `tv.svg` `phone.svg`
- **庆祝类**：`cake.svg` `cupcake.svg` `balloon.svg` `gift.svg` `party.svg` `ribbon.svg` `crown.svg` `candy.svg` `cookie.svg` `bubbletea.svg` `ice.svg` `cherry.svg` `strawberry.svg` `peach.svg` `apple.svg`
- **星星/闪光**：`star.svg` `star2.svg` `sparkle.svg` `sparkles2.svg` `comet.svg` `dizzy.svg` `fire.svg` `rainbow.svg` `diamond.svg` `clover.svg`
- **动物/自然**：`bear.svg` `cat.svg` `paw.svg` `bird.svg` `chick.svg` `fish.svg` `shell.svg` `mushroom.svg` `leaf.svg` `flower.svg` `blossom.svg`
- **心情/其他**：`heart_pink.svg` `heart_blue.svg` `bubble.svg` `letter.svg` `envelope.svg` `clock.svg` `calendar.svg` `pin.svg` `bulb.svg` `check.svg` `zzz.svg` `game.svg` `dice.svg` `trophy.svg` `medal.svg` `camera.svg` `cloud.svg` `sun.svg` `moon.svg`

### 4.8 字体 — `assets/fonts/`

见 2.2 节。共 7 个 woff2 + 5 个 CSS 参考文件。

---

## 5. 交互与动效清单

| # | 位置 | 交互 | 实现要点 |
| --- | --- | --- | --- |
| 1 | S0 加载 | 判定圈扩散 + PERFECT 弹出 | CSS `@keyframes` 缩放 + 透明度；`animation-delay` 错开 |
| 2 | S0 → S1 | 遮罩淡出 | 加载完成后加 class，`opacity` 过渡 600ms |
| 3 | 全局 | 飘落粒子（音符/叶子/星星） | 绝对定位 + 随机 `left` / `animation-duration`，JS 生成 20–30 个 |
| 4 | S1 | 迪拉熊上下浮动 | `transform: translateY()` 无限交替，两只相位错开 |
| 5 | S1 | 标题「生日」hover 变形 | `::after` 伪元素覆盖 `01017`，`opacity` 切换 |
| 6 | S2 | 吹蜡烛 | 点击按钮 → 蜡烛 `opacity:0` + 烟雾粒子 → 触发礼花 |
| 7 | S2 | 礼花 | CSS 粒子（20–40 个），随机角度/距离，`transform` 飞出后消失 |
| 8 | S3 | 唱片旋转 | 无限 `rotate`，`animation-play-state` 随 hover 暂停 |
| 9 | S3 | 卡片翻转 | `transform-style: preserve-3d` + `rotateY(180deg)` |
| 10 | S3 | 第 4 张触发全屏红色闪 | 给 `body` 加 class，CSS 变量覆盖，`setTimeout` 600ms 后移除 |
| 11 | S4 | 木牌 hover 微倾 | `rotate(-1deg)` + 硬阴影位移 |
| 12 | S5 | 图鉴卡片 hover 抬升 | `translateY(-6px)` + 阴影加大 |
| 13 | S5 | 徽章依次点亮 | `IntersectionObserver` 进入视口后依次加 class |
| 14 | S6 | 居民卡贴纸散落 | 随机 `rotate` + `translate`，hover 时回正 |
| 15 | S7 | 信纸逐行淡入 | `IntersectionObserver` + `animation-delay` 递增 |
| 16 | 全局 | 滚动进场 | `IntersectionObserver` 统一加 `.in-view` class |
| 17 | 全局 | 回到顶部 | 隐藏按钮，滚动超过 1 屏后淡入 |

**性能要求：**
- 动效一律用 `transform` / `opacity`，不要动 `width`/`height`/`top`/`left`。
- 尊重 `@media (prefers-reduced-motion: reduce)`，关闭飘落粒子和旋转。
- 所有图片加 `loading="lazy"`（S0/S1 的关键图除外）。
- 首屏关键素材预加载：`dilla_01_base.webp`、`dilla_07_lime.webp`。

---

## 6. 技术约束（交给 gpt6astra 的硬性要求）

1. **单文件优先**：输出 `web/index.html`，CSS 内联在 `<style>`，JS 内联在 `<script>`。
   - 如必须拆分，用 `web/style.css` + `web/main.js`，路径相对 `web/` 目录。
2. **部署目标是 GitHub Pages**：`https://<用户名>.github.io/<仓库名>/`，联网访问。
3. **允许使用 Three.js** 做 3D 生日蛋糕：
   - 优先本地 vendor `../assets/vendor/three.min.js`
   - 缺失时退化为 CDN `https://unpkg.com/three@0.149.0/build/three.min.js`
   - 不要用 ES module 版本
4. **不引入其他框架**（React / Vue / jQuery / Bootstrap 都不要）。
5. **素材路径必须用相对路径 `../assets/...`**：
   - GitHub Pages 项目站点带子路径，用 `/assets/...` 这种根路径会 404。
6. **文件名大小写要完全一致** —— GitHub Pages 区分大小写。
   （素材文件名已全部改为纯 ASCII 且全小写，见 `docs/DEPLOY.md`。）
7. **响应式**：375px / 768px / 1440px 三个宽度都要正常。
8. **无障碍**：
   - 装饰性图片 `alt=""` + `aria-hidden="true"`。
   - 有意义的图片给 `alt`（尤其私人照片，要描述内容）。
   - 按钮用 `<button>`，不要用 `<div onclick>`。
   - 颜色对比度正文 ≥ 4.5:1。
9. **不要修改 `assets/` 目录下的任何文件**，只读取。
10. **`prefers-reduced-motion`** 必须处理（Three.js 部分：不启动动画循环，只渲染一帧）。
11. **不写 `<iframe>`**。
12. **BGM 默认不自动播放**（浏览器会拦），给左上角明显的音符按钮。
13. **Three.js 性能**：渲染循环离开视口要暂停；`setPixelRatio` 上限 2。
14. **彩蛋占位符**：文案中所有 `[你的名字]`、`[我]` 之类，用注释标出来方便替换。

---

## 6b. 部署到 GitHub Pages

完整操作手册见 [`DEPLOY.md`](DEPLOY.md)。已处理的事项：

| 项目 | 状态 |
| --- | --- |
| 非 ASCII 文件名 | ✅ 30 个术曲封面已改为 ASCII（`日文.webp` → `罗马音.webp`） |
| 日文标题 | ✅ 保留在 `assets/manifest.json` 的 `title` 字段，网页照常显示日文 |
| 大写文件名 | ✅ 无，全小写 |
| `_raw/` 备份（34 MB） | ✅ `.gitignore` 已排除 |
| 仓库根 `index.html` | ⚠️ **需手动添加跳转页**（网页主体在 `web/`），做法见 DEPLOY.md 第四节 |
| 隐私 | ⚠️ 仓库含私人照片，Public 仓库任何人可见，建议 Private（详见 DEPLOY.md 第七节） |

---

## 7. 交付物与目录

```
ayao-birthday/                       ← GitHub Pages 仓库根
├── .gitignore                       ← 排除 assets/_raw/（34 MB 备份）
├── index.html                       ← ⚠️ 需手动加的跳转页，指向 web/index.html
├── docs/
│   ├── PLAN.md                      ← 本文件（制作规划书）
│   ├── HANDOFF.md                   ← 给 gpt6astra 的拼装说明（精简版）
│   ├── PROMPT_FOR_GPT.md            ← ★ 给 GPT 的完整提示词（整段复制）
│   └── DEPLOY.md                    ← 部署到 GitHub Pages 的操作手册
├── assets/
│   ├── manifest.json                ← 素材清单（机器可读）
│   ├── _preview.html                ← 素材总览页（肉眼核对用）
│   ├── _raw/                        ← 原始未优化素材（备份，**不上传**）
│   ├── personal/                    ← ★ 私人照片（优先级最高）
│   ├── audio/                       ← ★ 背景音乐 acnh_bgm.mp4
│   ├── vendor/                      ← Three.js（建议本地 vendor 一份）
│   ├── maimai/                      ← 舞萌 / 迪拉熊
│   ├── acnh/                        ← 动物森友会
│   ├── pokemon/                     ← 宝可梦（伊布家族 / 鬃岩狼人 / 剑盾）
│   ├── tomodachi/                   ← 人森 / 朋友收集
│   ├── marettu/                     ← MARETU 术曲封面
│   ├── ui/                          ← 阿药 B 站元素
│   ├── deco/                        ← Twemoji 装饰 SVG
│   └── fonts/                       ← 本地字体
├── web/
│   └── index.html                   ← 【gpt6astra 产出】网页主体
└── ref/
    ├── optimize_assets.py           ← 网络素材优化脚本
    ├── optimize_personal.py         ← 私人照片处理脚本
    ├── fetch_pokemon.py             ← 批量下载宝可梦
    ├── rename_ascii.py              ← 文件名转 ASCII（部署准备）
    ├── build_manifest.py            ← 生成 manifest.json
    ├── build_preview.py             ← 生成素材总览页
    ├── validate.py                  ← 校验脚本
    └── optimize_report.json         ← 优化报告
```

---

## 8. 验收清单

- [ ] **用 http 服务打开**（`http://127.0.0.1:8080/`），不是 `file://`
- [ ] 375px 宽下无横向滚动，文字不溢出
- [ ] 字体是可爱体（不是系统默认宋体/黑体）
- [ ] **背景音乐单曲循环**，左上角透明音符按钮可播放/暂停
- [ ] **默认不自动播放**，首次交互后才开始
- [ ] 按钮在滚动时始终固定在左上角
- [ ] **18 岁**：S2 有 18 根蜡烛；S7 有 18 岁蜡烛的 3D 动画
- [ ] **S7 滚动到底部触发 Three.js 的 3D 蛋糕动画**
- [ ] Three.js 加载失败时有纯 CSS 蛋糕兜底
- [ ] **网页最下端有 `by Axing`**
- [ ] **S4 出现西施惠 + 蜜雪儿 + 史培亚**三只
- [ ] **S5 有伊布家族 9 只合影，仙子伊布在 C 位**
- [ ] **S5 有鬃岩狼人三形态**（白昼/黑夜/黄昏）
- [ ] **S5 有剑盾专区**，含苍响、藏玛然特、无极汰那
- [ ] 迪拉熊**只有两只**出现在 S1（用真实玩偶照，或官方立绘，不要两套混用）
- [ ] **S7 的合照 `us_switch.webp` 足够大、没有被裁掉主体、没有加滤镜**
- [ ] **S6 用的是仓鼠头像 `hamster_avatar.webp`**，不是她的 B 站头像（两者并列也可以，但仓鼠是主体）
- [ ] **S5 图鉴里有「仓鼠」条目**
- [ ] MARETU 曲目卡片 10 张全部有封面图
- [ ] 吹蜡烛交互可用，礼花正常
- [ ] 第 4 张 MARETU 卡片的红色闪屏只触发一次
- [ ] 第 6 张卡片弹出仓鼠表情包
- [ ] 「DX 熊熊全家福」折叠区默认收起
- [ ] `prefers-reduced-motion` 开启时无飘落粒子、无旋转、无蛋糕动画
- [ ] 所有装饰图有 `alt=""` 或 `aria-hidden`
- [ ] 私人照片有**有意义的 `alt`**（描述照片内容，不要写「图片」）
- [ ] 页面总大小（含素材）在 30MB 以内
- [ ] 素材路径全是 `../assets/...` 相对路径，**没有 `/assets/...` 绝对路径**
- [ ] 文件名大小写与引用完全一致（GitHub Pages 区分大小写）
- [ ] 控制台无 404、无报错

---

## 9. 给 gpt6astra 的话

这份规划已经把**素材、配色、字体、结构、交互、文案**全部定好了。

你要做的：
1. 读 `docs/HANDOFF.md`（精简版说明）
2. 读 `assets/manifest.json`（确认素材路径与尺寸）
3. 输出 `web/index.html`

**重点记住四条：**
- **迪拉熊只放两只**（用户明确要求），优先用 `assets/personal/dilla_plush_*` 真实玩偶照。
- **部署到 GitHub Pages**，所以素材路径必须是相对路径 `../assets/...`，且大小写要与文件名完全一致。
- **允许用 Three.js** 做 3D 蛋糕（本地 vendor 优先，缺失退化 CDN），但**不要引入其他框架**。
- **文案克制**，她是 INTP，不要写肉麻长抒情。

**外加一条最重要的：**
- **`assets/personal/` 里的私人照片是整页的核心**。尤其 S7 的合照 `us_switch.webp` 和 S6 的仓鼠头像。
  文案要为照片让路 —— 图先出，字只做一句点睛。不要给这些照片加滤镜或裁掉主体。

**别忘了：**
- **18 岁**要体现（18 根蜡烛 + 3D 蛋糕 + 信里提）
- **网页最下端必须有 `by Axing`**
- **背景音乐单曲循环** + 左上角透明音符按钮
- **她喜欢的角色都要出现**：西施惠、蜜雪儿、史培亚、仙子伊布、鬃岩狼人、伊布家族合影、剑盾专区
