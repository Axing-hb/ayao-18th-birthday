# 给 GPT 的提示词 · 阿药 18 岁生日网页

> **用法**：把本文件**整份**复制给 gpt6astra（或任何负责拼装的模型），它就会产出 `web/index.html`。
> 配套素材在 `ayao-birthday/assets/`，规划详情见 `docs/PLAN.md`。

---

## ⬇️ 以下内容整段复制给 GPT ⬇️

---

你是一个前端工程师。请写一个**单文件网页**：`web/index.html`。

这个网页会**部署到 GitHub Pages**（`https://<用户名>.github.io/<仓库名>/`），所以：

- **可以用 Three.js 做 3D 生日蛋糕**（联网访问，不要求断网可用）
- Three.js **请用本地 vendor 版本**：`../assets/vendor/three.min.js`
  （如果该文件不存在，就用 CDN `https://unpkg.com/three@0.149.0/build/three.min.js` 并在注释里标明）
- 其余部分用**纯 HTML + CSS + 原生 JS**，不要引入其他框架（不要 React/Vue/jQuery）
- 所有素材路径用**相对路径** `../assets/...`（项目站点带子路径，绝对路径会 404）

这是一个生日惊喜网页，送给我女朋友 **阿药**。她 **18 岁生日**，生日 10 月 17 日。那天我可能在学校，所以用网页远程送祝福。

---

### 一、人物设定（决定了文案语气，务必读懂）

- 她叫 **阿药**，B 站昵称 `Anria_01017`，签名是 **「你好，我叫阿药。一个成分复杂的 intp」**
- 她是 **INTP**：理性、爱思考、脑内小剧场丰富、**讨厌被强行煽情**
- 她是二次元，爱听**术曲（Vocaloid）**，尤其 **MARETU**
- 她喜欢：**舞萌 DX（maimai）、动物森友会、宝可梦、人森（朋友收集：梦想生活）**
- 她最喜欢的宝可梦世代是 **剑盾（第八世代）**
- 你们一起养了一只**仓鼠**

**文案纪律（最重要）：**
- 要**克制**，不要写肉麻的长篇抒情。INTP 吃「克制的浪漫 + 一个只有她懂的梗」
- 可以用「正经的自我介绍句式 + 突然的偏心」这种反差
- 可以有一点点理科生式浪漫（编号、进度条、坐标、数据）
- **让照片说话，文字只做点睛**。不要用文字去描述照片里已经能看到的东西
- **18 岁要提，但不要长辈式说教**。可以调侃：「从今天起你要为自己的每一个决定负责了。—— 不过今天先不用。」
- ⚠️ 她的 B 站头像是**表情包动物**，**不是仓鼠**。仓鼠是现实中的宠物，别搞混

---

### 二、素材（全部已在本地，用相对路径引用，**禁止改成外链**）

网页放在 `web/` 目录下，所以素材路径是 `../assets/...`。

#### ★ 私人照片 `../assets/personal/`（情感权重最高）

| 文件 | 内容 | 用在哪 |
| --- | --- | --- |
| `us_switch.webp` | **我们俩躺床上一起玩 Switch**（穿宝可梦睡衣） | **S7 结尾，大幅居中** |
| `us_switch_square.webp` | 同上方形版 | S2 拍立得相框 |
| `dilla_plush_pair.webp` | **两只迪拉熊实物玩偶**（带舞萌DX吊牌） | S1 主视觉（整张） |
| `dilla_plush_big.webp` | 大只迪拉熊玩偶特写 | **S1 左侧** / S0 加载 |
| `dilla_plush_small.webp` | 小只迪拉熊挂件特写 | **S1 右侧** |
| `hamster_avatar.webp` | 仓鼠正脸（圆形） | **S6 居民卡头像** |
| `hamster_face.webp` | 仓鼠特写 | S5 图鉴「仓鼠条目」 |
| `hamster_ball.webp` | 仓鼠缩成球 + 漫画「!?」 | **S3 第 6 张卡片彩蛋** |
| `hamster_cage.webp` | 仓鼠趴笼顶（竖图） | S6 竖版配图 |

**私人照片使用纪律：**
1. **不裁掉主体**（玩偶吊牌、仓鼠爪子都是细节）
2. **不加滤镜**（不要黑白、不要复古、不要高对比）
3. **不拉伸**（用 `object-fit: contain` 或按原比例）
4. **不缩小到看不清**（`us_switch` 在 S7 要占足够大面积）
5. **不做背景底图**（会被文字盖住，失去意义），要**单独成块展示**
6. 给**有意义的 `alt`**（描述内容，不要写「图片」）

#### 背景音乐 `../assets/audio/acnh_bgm.mp4`

动森背景音乐（AAC / 48kHz 立体声，约 90 秒）。**浏览器原生可播，不用转码。**

#### 舞萌 / 迪拉熊 `../assets/maimai/`（18 个）

`dilla_01_base` `dilla_02_ietek` `dilla_03_risuk` `dilla_04_panda` `dilla_05_mitsuyoshi` `dilla_06_aoharu` `dilla_07_lime` `dilla_08_lemon` `dilla_09_splash` `dilla_10_universe3` `dilla_11_universe4` `dilla_12_universe5` `dilla_13_tanuki` `dilla_14_ninja` `dilla_15_dragon` `dilla_16_blackrose` `maimai_favicon` `maimai_touchicon`

#### 动物森友会 `../assets/acnh/`（16 个）

`isabelle`（**西施惠 ★她喜欢**）`sasha_mixueer`（**蜜雪儿 ★她喜欢**）`fang_shipeiya`（**史培亚 ★她喜欢**）`kk_slider` `celeste` `tom_nook` `blathers` `redd` `zucker` `marshal` `diana` `skye` `chief` `whitney` `merengue` `leaf_icon`

#### 宝可梦 `../assets/pokemon/`（54 个）

**基础 18 只**：`pikachu_025` `eevee_133` `jigglypuff_039` `snorlax_143` `mew_151` `slowpoke_079` `psyduck_054` `gengar_094` `bulbasaur_001` `charmander_004` `squirtle_007` `togepi_175` `mareep_179` `piplup_393` `rowlet_722` `mimikyu_778` `magikarp_129` `ditto_132`

**★ 伊布家族 9 只**：`eevee_133` `vaporeon_134` `jolteon_135` `flareon_136` `espeon_196` `umbreon_197` `leafeon_470` `glaceon_471` **`sylveon_700`（仙子伊布 ★她最喜欢）**

**★ 鬃岩狼人 3 形态**（★她喜欢）：`lycanroc_745_midday`（白昼）`lycanroc_10126_midnight`（黑夜）`lycanroc_10152_dusk`（黄昏）

**★ 剑盾 / 第八世代 22 只**（她最喜欢的世代）：`grookey_810` `scorbunny_813` `sobble_816` `rillaboom_812` `cinderace_815` `inteleon_818` `zacian_888` `zacian_10188_crowned` `zamazenta_889` `zamazenta_10189_crowned` `eternatus_890` `corviknight_823` `dragapult_887` `toxtricity_849` `grimmsnarl_861` `wooloo_831` `alcremie_869` `snom_872` `morpeko_877` `kubfu_891` `urshifu_892` `sirfetchd_865` `falinks_870` `yamper_835`

#### 人森 / 朋友收集 `../assets/tomodachi/`（37 个）

`tomo_logo` `tomo_kv_1` `tomo_kv_2` `tomo_pickup` `tomo_obj_resident` `tomo_obj_island_1` `tomo_obj_island_2` `tomo_obj_daily_1` `tomo_obj_daily_2` `tomo_obj_daily_3` `tomo_sticker_1~4` `tomo_ic_make` `tomo_ic_enjoy` `tomo_ic_rel` `tomo_ic_create` `tomo_ic_item` `tomo_bird` `tomo_bowling` `tomo_resident_1~4` `tomo_island_1~4` `tomo_about_1/2/4/6` `tomo_daily_1~3` `tomo_product`

#### MARETU 术曲封面 `../assets/marettu/`（10 个）

| 文件 | 日文标题（网页上显示这个） | 罗马音（副标题） |
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

> 文件名是纯 ASCII（为了 GitHub Pages 部署），**日文标题照上表写死在网页文字里**。
> 顺序就是表格顺序（`coin_locker_baby` 是第 4 张，触发红色闪屏彩蛋；`umitagari` 是第 6 张，触发仓鼠彩蛋）。

#### 阿药 B 站元素 `../assets/ui/`（4 个）

`aya_avatar`（她的 B 站头像，**表情包动物**）`aya_space_l` `aya_space_s` `aya_nameplate`（「有爱楷模」名牌）

#### 装饰 Emoji `../assets/deco/`（64 个 SVG）

- **音乐**：`note` `notes` `music_mic` `headphone` `cd` `tape` `video` `tv` `phone`
- **庆祝**：`cake` `cupcake` `balloon` `gift` `party` `ribbon` `crown` `candy` `cookie` `bubbletea` `ice` `cherry` `strawberry` `peach` `apple`
- **闪光**：`star` `star2` `sparkle` `sparkles2` `comet` `dizzy` `fire` `rainbow` `diamond` `clover`
- **自然**：`bear` `cat` `paw` `bird` `chick` `fish` `shell` `mushroom` `leaf` `flower` `blossom`
- **其他**：`heart_pink` `heart_blue` `bubble` `letter` `envelope` `clock` `calendar` `pin` `bulb` `check` `zzz` `game` `dice` `trophy` `medal` `camera` `cloud` `sun` `moon`

#### 字体 `../assets/fonts/`（7 个 woff2）

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

### 三、配色（直接抄进 `:root`）

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

### 四、页面结构（8 段，按顺序）

#### S0 · 加载入场
- 全屏深色遮罩，中央迪拉熊跳动 + 音游判定圈 `TAP → PERFECT` 扩散动画
- 小字：`LOADING ... 为阿药准备的第 01017 号惊喜`
- 图：`../assets/personal/dilla_plush_big.webp`
- **进入按钮**（`▶ 进入` 或 `TAP TO START`）—— **点击时同时启动 BGM**

#### S1 · Hero 主视觉
- 大标题：**生日快乐，阿药。**
- 副标题：**你好，我叫阿药。一个成分复杂的 intp。—— 今天这一页，是专门为你一个人开的服务器。**
- 背景：深蓝夜空渐变 + 缓慢飘落音符/叶子/星星
- **只放两只迪拉熊**（硬性要求）：
  - 左：`../assets/personal/dilla_plush_big.webp`
  - 右：`../assets/personal/dilla_plush_small.webp`
  - 或整张合影 `../assets/personal/dilla_plush_pair.webp`
  - 备选（官方立绘，**两套不要混用**）：`dilla_01_base.webp` + `dilla_07_lime.webp`
- 上下浮动，相位错开；底部 SCROLL 箭头

#### S2 · 18 岁生日蛋糕 / 吹蜡烛
- 蛋糕用 CSS + twemoji 拼（`cake` `cupcake` `candy` `cherry`）
- **18 根蜡烛**（2 排各 9 根，或围成一圈）—— 这是成年礼，必须是 18 根
- **吹蜡烛交互**：点击按钮 → 蜡烛依次熄灭 + 烟雾 → 礼花（`party.svg` + CSS 粒子）
- 熄灭后文案：**「18 根都吹灭了。愿望已经收到，剩下的交给时间。」**
- 副标题：**「从今天起，你要为自己的每一个决定负责了。—— 不过今天先不用。」**
- 宝可梦探头：`pikachu_025` `eevee_133` `jigglypuff_039`
- 动森叶子飘落：`leaf_icon`
- 方形合照 `../assets/personal/us_switch_square.webp` 做成拍立得相框，配字：「上一次一起过生日，也是这样躺着的。」

#### S3 · MARETU 电台（重头戏）
- 做成**音乐播放器 / CD 机**，带旋转唱片
- 标题：**MARETU 电台 · 深夜档**，副标题 `for 阿药 · 成分复杂频道`
- **10 张曲目卡片**，封面在 `../assets/marettu/`，**日文原名做标题、罗马音做副标题**（清单见上方表格）
- 卡片可翻转，背面写一句短话（自己写，风格克制）
- **彩蛋 1**：翻到第 4 张（コインロッカーベイビー）时，整页闪一下 `--c-maretu-red`，0.6s 恢复，**只触发一次**
- **彩蛋 2**：翻到第 6 张（うみたがり）时，弹出仓鼠表情包 `../assets/personal/hamster_ball.webp`，
  配字：「这张图是它睡成这样的样子。我当时也这个表情。」
- 底部假播放进度条，hover 出现 `PERFECT` 判定字样
- ⚠️ **不要给卡片加跳转 B 站的链接**（这个需求已取消）

#### S4 · 动森 · 岛上公告（含她喜欢的村民）
- 木牌样式（木色边框 + 奶油白底）
- 标题：**岛上公告**
- 三条公告：
  1. 今日天气：晴。风力：刚好能吹灭 18 根蜡烛。
  2. 岛上来了新居民，名字叫阿药。生日：10 月 17 日。年龄：18。
  3. 狸克说，今天所有商品免费。……骗你的，但蛋糕是真的。
- **★ 她喜欢的三只村民必须都出现**：
  - `../assets/acnh/isabelle.webp`（**西施惠**）—— 主位，居中或左侧
  - `../assets/acnh/sasha_mixueer.webp`（**蜜雪儿**，兔）—— 右侧
  - `../assets/acnh/fang_shipeiya.webp`（**史培亚**，狼）—— 左侧
  - `kk_slider.webp`（K.K.）中下氛围，`celeste.webp` 右上小装饰
- **给这三只各写一句台词**：
  - 西施惠：「今天的公告板我特意擦干净了。生日快乐呀！」
  - 蜜雪儿：「唔……我本来想给你烤个蛋糕，结果自己吃掉了。抱歉。」
  - 史培亚：「这倒是……挺不错的。生日快乐，小子。」

#### S5 · 宝可梦 · 图鉴 + 伊布家族合影 + 剑盾专区

**5a 图鉴卡片**
- 卡片头 `No.01017  阿药`；属性 `思考系 / 音乐系`；特性 `成分复杂`、`深夜术曲专精`
- 写 4–6 条可爱的图鉴说明
- **加一条仓鼠条目**（`../assets/personal/hamster_face.webp`）：
  `No.00001  仓鼠` · 属性 `毛绒系 / 半夜跑轮系` · 特性 `缩成球`
  说明：「两人共同持有。攻击力 0，可爱度溢出。」

**5b ★ 伊布家族合影（重点）**
- 9 只排成家族全家福：
  `eevee_133` `vaporeon_134` `jolteon_135` `flareon_136` `espeon_196` `umbreon_197` `leafeon_470` `glaceon_471` **`sylveon_700`**
- **仙子伊布放 C 位**（她最喜欢）—— 中间、放大、加一点 `--c-maimai-pink` 柔光
- 标题：**「伊布家族，全员到齐。」** 副标题：`No.133 – No.700`
- 每只下面标一行小字（名字 + 属性）

**5c ★ 鬃岩狼人三形态（重点）**
- 横向三格，中间稍大：
  - `lycanroc_745_midday.webp` —— 白昼形态
  - `lycanroc_10126_midnight.webp` —— 黑夜形态
  - `lycanroc_10152_dusk.webp` —— 黄昏形态
- 标题：**「同一只狼，三个时间段。」** 副标题：`昼 / 夜 / 黄昏`
- 小字：`它随你什么时候遇见它而改变样子。`

**5d ★ 剑盾专区（她最喜欢的世代）**
- 标题：**「第八世代 · 伽勒尔地区」** 副标题：`她最喜欢的世代`
- 分类展示：
  - **御三家**：`grookey_810` `scorbunny_813` `sobble_816` + 最终进化 `rillaboom_812` `cinderace_815` `inteleon_818`
  - **传说**：`zacian_888` + `zacian_10188_crowned`（剑之王）、`zamazenta_889` + `zamazenta_10189_crowned`（盾之王）、`eternatus_890`
  - **人气对战**：`corviknight_823` `dragapult_887` `toxtricity_849` `grimmsnarl_861` `sirfetchd_865` `falinks_870`
  - **可爱系**：`wooloo_831` `alcremie_869` `snom_872` `morpeko_877` `yamper_835`
  - **DLC**：`kubfu_891` `urshifu_892`
- 苍响/藏玛然特建议**双形态并排**（普通 + 王形态）

**5e 徽章**
- twemoji `medal` `trophy` `diamond` `star2` 做成 8 枚假道馆徽章

#### S6 · 人森 · 居民卡
- 标题：**我的岛上，已经给你留好位置了。**
- 居民卡字段：
  - 居民名 `阿药`
  - 性格 `INTP（自我诊断 100% 准确）`
  - 口头禅 `「成分复杂」`
  - 喜欢 `术曲、舞萌、动森、宝可梦、仓鼠`
  - 讨厌 `（留白，让她自己填）`
- **头像用 `../assets/personal/hamster_avatar.webp`**（仓鼠，圆形裁切 + 描边）
- 她的 B 站头像 `../assets/ui/aya_avatar.webp` 放旁边做小徽章，两个并列
- 配图 `../assets/personal/hamster_cage.webp`（竖图）放右侧，手机端移到下方
- 装饰：`tomo_logo` `tomo_obj_resident` `tomo_sticker_1~4` `tomo_ic_*`
- 背景：`tomo_kv_1` 或 `tomo_island_*`，低透明度当纹理

#### S7 · 结尾信 + 3D 生日蛋糕动画

**7a 核心照片（先出图）**
- `../assets/personal/us_switch.webp` 大幅、居中、圆角、轻微投影
- 图下方小字（`--c-text-dim`）：`某个普通的晚上 · 谁也没赢`
- **不要缩小、不要做背景、不要加滤镜**

**7b 信**
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

**7c ★★★ 3D 生日蛋糕 + 18 岁蜡烛动画（本页最重要的特效）**

**触发**：用户**滚动到网页最下端**时自动播放（用 `IntersectionObserver`）。

**技术要求：**
- **必须是真的 3D**，不是平面图。**用 Three.js 实现**（本页最重要的视觉特效）
  - 引入方式：`<script src="../assets/vendor/three.min.js"></script>`
  - 如果该文件不存在，退化为 CDN：`<script src="https://unpkg.com/three@0.149.0/build/three.min.js"></script>`
  - **不要用 ES module 版本**（避免 `type="module"` 与本地 `file://` 调试冲突）
- 场景结构（Three.js）：
  - 相机 + 环境光 + 一个带阴影的方向光（立体感更强）
  - 蛋糕：三层圆柱体（`CylinderGeometry`），从下到上依次变小
  - 顶层奶油 + 若干小球体（樱桃）点缀
  - **18 根蜡烛**：细圆柱，内圈 6 根 + 外圈 12 根均匀分布
  - **火焰**：每根蜡烛顶部一个小球，`--c-maimai-yellow` 自发光材质 + 缩放摇曳
- **动画序列**（进入视口后依次触发）：
  1. `0.0s` 蛋糕从下方升起 + 缓慢自转（`rotation.y` 持续增加）
  2. `0.4s` 18 根蜡烛**依次点亮**（每根间隔 60ms，火焰 `scale` 从 0 → 1）
  3. `1.6s` 浮现金色数字 `18`（Canvas 贴图或 HTML 叠加层都行）
  4. `2.0s` 粒子升起（`Points` 或若干小 Sprite）
  5. `2.4s` 底部浮现 **「18 · 生日快乐」**（HTML 叠加层即可）
- **交互**：`mousemove` 时相机跟随轻微旋转，增强 3D 感
- **性能**：
  - `requestAnimationFrame` 驱动，**离开视口时暂停渲染**（省电，尤其手机上）
  - `renderer.setPixelRatio(Math.min(devicePixelRatio, 2))`
  - `resize` 时更新相机宽高比
- **`prefers-reduced-motion`**：检测到时**不启动动画循环**，只渲染一帧静态蛋糕（蜡烛全部点亮）
- **降级**：如果 Three.js 没加载成功（`typeof THREE === 'undefined'`），
  显示一个纯 CSS 的静态蛋糕兜底，**不要留空白**

**Three.js 参考骨架（可自由发挥，但结构要照这个来）：**

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

**7d 页脚（硬性要求）**
- `MADE WITH ♥ · 01017`
- **网页最下端必须出现 `by Axing`** —— 这是明确要求，不能漏

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

- 隐藏按钮「**再看一遍**」滚动回顶部
- **收尾彩蛋**：默认收起的折叠按钮「**DX 熊熊全家福**」，点开显示 `../assets/maimai/` 里另外 14 只迪拉熊

---

### 五、背景音乐（左上角透明音符按钮）

```html
<button id="bgm-toggle" aria-label="背景音乐开关" aria-pressed="false">
  <img src="../assets/deco/note.svg" alt="" aria-hidden="true">
</button>
```

```css
#bgm-toggle{
  position:fixed; top:16px; left:16px; z-index:9999;
  width:44px; height:44px; padding:0;
  display:flex; align-items:center; justify-content:center;
  background:rgba(255,253,247,.10);
  border:2px solid rgba(255,253,247,.28);
  border-radius:50%;
  backdrop-filter:blur(6px);
  cursor:pointer;
  transition:transform .2s, background .2s, border-color .2s;
  margin:env(safe-area-inset-top) 0 0 env(safe-area-inset-left);
}
#bgm-toggle img{ width:22px; height:22px; opacity:.85; }
#bgm-toggle:hover{ background:rgba(255,253,247,.20); border-color:var(--c-maimai-yellow); transform:scale(1.08); }
#bgm-toggle[aria-pressed="true"]{ border-color:var(--c-maimai-yellow); background:rgba(255,210,63,.18); }
#bgm-toggle[aria-pressed="true"] img{ opacity:1; }
#bgm-toggle[aria-pressed="true"]{ animation:bgm-pulse 2s ease-in-out infinite; }
@keyframes bgm-pulse{
  0%,100%{ box-shadow:0 0 0 0 rgba(255,210,63,.35); }
  50%    { box-shadow:0 0 0 8px rgba(255,210,63,0); }
}
@media (prefers-reduced-motion: reduce){ #bgm-toggle{ animation:none !important; } }
```

```js
const audio = new Audio('../assets/audio/acnh_bgm.mp4');
audio.loop = true;        // 单曲循环
audio.volume = 0.35;      // 别太吵

const btn = document.getElementById('bgm-toggle');
let started = false;

function tryPlay(){
  audio.play().then(() => {
    btn.setAttribute('aria-pressed', 'true');
    started = true;
  }).catch(() => {});
}

// 首次交互后自动开始（点击 S0 的进入按钮时也应调用 tryPlay）
['click','touchstart','keydown'].forEach(ev =>
  document.addEventListener(ev, function once(){
    if(!started) tryPlay();
    document.removeEventListener(ev, once);
  }, {passive:true})
);

btn.addEventListener('click', e => {
  e.stopPropagation();
  if(audio.paused){ tryPlay(); }
  else { audio.pause(); btn.setAttribute('aria-pressed','false'); }
});
```

**要求：**
- **单曲循环**（`loop = true`）
- **默认不自动播放**（浏览器会拦，突然出声也吓人），首次交互后开始
- 按钮**固定在左上角**，滚动时不消失，手机上避开刘海（`env(safe-area-inset-*)`）
- 用户手动暂停后，**不要再自动播放**

---

### 六、硬性约束

1. **单文件** `web/index.html`，CSS 内联 `<style>`，JS 内联 `<script>`
2. **部署目标是 GitHub Pages**（`https://<用户名>.github.io/<仓库名>/`），会联网访问
3. **允许用 Three.js** 做 3D 蛋糕：优先 `../assets/vendor/three.min.js`，缺失则退化为 CDN
4. **不要引入其他框架**（不要 React / Vue / jQuery / Bootstrap）
5. **素材路径必须用相对路径 `../assets/...`** —— 项目站点带子路径，`/assets/...` 会 404
6. **文件名大小写要完全一致** —— GitHub Pages 区分大小写
7. 不要用 `fetch()` 读本地文件（部署后虽然能用，但本地调试会失败），所有数据写在 JS 里
8. **迪拉熊只有两只**，只在 S1（S7 的折叠彩蛋默认收起）
9. **18 岁**必须体现在：S2 的 18 根蜡烛、S7 的 3D 蛋糕动画、S7 的信
10. **`by Axing` 必须出现在网页最下端**
11. **私人照片**：不裁主体、不加滤镜、不拉伸、不缩小、不做背景、给有意义的 `alt`
12. **响应式**：375 / 768 / 1440 三个宽度都正常，375px 下无横向滚动
13. CSS 动效只用 `transform` / `opacity`（Three.js 部分不受此限）
14. 必须处理 `@media (prefers-reduced-motion: reduce)`
15. 装饰图 `alt="" aria-hidden="true"`；有意义的图给 `alt`
16. 按钮用 `<button>`，不要 `<div onclick>`
17. 不写 `<iframe>`
18. 首屏关键图预加载：`dilla_plush_big.webp`、`dilla_plush_small.webp`
19. Three.js 渲染循环**离开视口要暂停**，`setPixelRatio` 上限设 2（手机上省电）

---

### 七、交付

输出**完整可运行的** `web/index.html`，不要省略、不要写 `// ... 此处省略`。
写完后自查这份清单：

- [ ] 页面在 http 服务下打开正常（不是 file://）
- [ ] 375px 宽无横向滚动
- [ ] 字体是可爱体（不是系统默认宋体/黑体）
- [ ] 背景音乐单曲循环，左上角透明音符按钮可控制
- [ ] 默认不自动播放，首次交互后才响
- [ ] S2 有 18 根蜡烛
- [ ] S7 滚动到底部触发 **Three.js 的 3D 蛋糕动画**
- [ ] Three.js 加载失败时有纯 CSS 蛋糕兜底
- [ ] 网页最下端有 `by Axing`
- [ ] S4 有西施惠 + 蜜雪儿 + 史培亚
- [ ] S5 有伊布家族 9 只合影，仙子伊布 C 位
- [ ] S5 有鬃岩狼人三形态
- [ ] S5 有剑盾专区
- [ ] 迪拉熊只有两只
- [ ] S7 合照够大、没裁主体、没加滤镜
- [ ] S6 用仓鼠头像
- [ ] `prefers-reduced-motion` 生效
- [ ] 素材路径全是 `../assets/...` 相对路径，没有 `/assets/...` 绝对路径
- [ ] 控制台无 404、无报错

---

## ⬆️ 复制到此结束 ⬆️

---

## 使用说明（这部分**不要**复制给 GPT）

1. 把上面「⬇️ 以下内容整段复制给 GPT ⬇️」到「⬆️ 复制到此结束 ⬆️」之间的内容整份发给 gpt6astra
2. GPT 产出的 `index.html` 放到 `ayao-birthday/web/`
3. **本地用 http 服务测试**（比 `file://` 更接近线上环境，见 `docs/DEPLOY.md` 第五节）
4. 跑校验确认没误改素材：

```powershell
& "C:\Users\29631\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe" ayao-birthday\ref\validate.py
```

**如果 GPT 输出被截断**：让它「继续」，或要求分块输出（先 HTML 骨架，再 CSS，再 JS），最后拼起来。

**关于 Three.js**：已经放开限制，允许用了（因为部署到 github.io 本来就联网）。
建议让 GPT 用本地 vendor 版本，抗 CDN 挂掉。下载命令见 `docs/DEPLOY.md` 第二节。

**部署到 GitHub Pages**：完整步骤见 [`DEPLOY.md`](DEPLOY.md)。

**配套文件：**
- `docs/DEPLOY.md` —— **部署到 GitHub Pages 的操作手册**
- `docs/PLAN.md` —— 完整规划（配色/字体/结构/交互/文案/验收）
- `docs/HANDOFF.md` —— 精简执行说明
- `assets/manifest.json` —— 素材清单（路径/尺寸/用途）
- `assets/_preview.html` —— 素材总览页（可以先肉眼核对一遍素材）
