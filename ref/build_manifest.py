# -*- coding: utf-8 -*-
"""生成 assets/manifest.json —— 供 gpt6astra 拼装时查询素材路径、尺寸、用途。"""
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

# 用途/角色备注表（key = 相对 assets/ 的路径）
NOTES = {
    # maimai
    "maimai/dilla_01_base.webp":   ("迪拉熊（原版蓝·DX无印启程区域）", "S1 主视觉左 / S0 加载动画", True),
    "maimai/dilla_02_ietek.webp":  ("雪人熊熊", "备用", False),
    "maimai/dilla_03_risuk.webp":  ("栗子熊熊", "备用", False),
    "maimai/dilla_04_panda.webp":  ("熊猫熊熊", "备用", False),
    "maimai/dilla_05_mitsuyoshi.webp": ("光吉熊熊", "备用", False),
    "maimai/dilla_06_aoharu.webp": ("青春熊熊", "备用", False),
    "maimai/dilla_07_lime.webp":   ("酸橙熊熊（青绿·咻哇咻哇区域）", "S1 主视觉右", True),
    "maimai/dilla_08_lemon.webp":  ("柠檬熊熊", "备用", False),
    "maimai/dilla_09_splash.webp": ("Splash 版迪拉熊", "备用", False),
    "maimai/dilla_10_universe3.webp": ("UNiVERSE 版迪拉熊", "备用", False),
    "maimai/dilla_11_universe4.webp": ("UNiVERSE 版柠檬熊", "备用", False),
    "maimai/dilla_12_universe5.webp": ("UNiVERSE 版酸橙熊", "备用", False),
    "maimai/dilla_13_tanuki.webp": ("狸子熊熊", "备用", False),
    "maimai/dilla_14_ninja.webp":  ("忍者熊熊", "备用", False),
    "maimai/dilla_15_dragon.webp": ("恶龙熊熊", "备用", False),
    "maimai/dilla_16_blackrose.webp": ("黑蔷薇熊熊", "备用", False),
    "maimai/maimai_favicon.webp":   ("maimai 官网 favicon", "站点 favicon", True),
    "maimai/maimai_touchicon.webp": ("maimai 官网 touch icon", "PWA / Apple Touch Icon", False),
    # acnh
    "acnh/isabelle.webp":   ("西施惠 Isabelle", "S4 左侧主装饰", True),
    "acnh/tom_nook.webp":   ("狸克 Tom Nook", "S4 备用", False),
    "acnh/kk_slider.webp":  ("K.K. Slider", "S4 中下装饰", True),
    "acnh/celeste.webp":    ("傅珂 Celeste", "S4 右上装饰", True),
    "acnh/blathers.webp":   ("傅达 Blathers", "S4 备用", False),
    "acnh/redd.webp":       ("狐利 Redd", "备用（神秘商人彩蛋）", False),
    "acnh/zucker.webp":     ("章丸丸 Zucker", "备用", False),
    "acnh/marshal.webp":    ("小润 Marshal", "备用", False),
    "acnh/diana.webp":      ("艳后 Diana", "备用", False),
    "acnh/leaf_icon.webp":  ("动森叶子图标", "全站飘落叶子 / S2 点缀", True),
    # acnh —— 她喜欢的村民（新增）
    "acnh/sasha_mixueer.webp": ("★ 蜜雪儿 Sasha（兔，懒散性格）", "S4 主装饰（她喜欢的村民）", True),
    "acnh/fang_shipeiya.webp": ("★ 史培亚 Fang（狼，暴躁性格）", "S4 主装饰（她喜欢的村民）", True),
    "acnh/skye.webp":       ("史凯 Skye（狼）", "S4 备用（狼村民同好）", False),
    "acnh/chief.webp":      ("阿猪 Chief（狼）", "S4 备用", False),
    "acnh/whitney.webp":    ("白女士 Whitney（狼）", "S4 备用", False),
    "acnh/merengue.webp":   ("蜜糖 Merengue（犀牛）", "S4 备用", False),
    # pokemon
    "pokemon/pikachu_025.webp":   ("皮卡丘 No.025", "S2 蛋糕后探头", True),
    "pokemon/eevee_133.webp":     ("伊布 No.133", "S2 探头 / S5 主视觉 / 伊布家族合影", True),
    "pokemon/jigglypuff_039.webp":("胖丁 No.039", "S2 探头", True),
    "pokemon/snorlax_143.webp":   ("卡比兽 No.143", "S5 图鉴装饰", True),
    "pokemon/mew_151.webp":       ("梦幻 No.151", "备用", False),
    "pokemon/slowpoke_079.webp":  ("呆呆兽 No.079", "S5 图鉴装饰", True),
    "pokemon/psyduck_054.webp":   ("可达鸭 No.054", "S5 小装饰", True),
    "pokemon/gengar_094.webp":    ("耿鬼 No.094", "备用", False),
    "pokemon/bulbasaur_001.webp": ("妙蛙种子 No.001", "备用", False),
    "pokemon/charmander_004.webp":("小火龙 No.004", "备用", False),
    "pokemon/squirtle_007.webp":  ("杰尼龟 No.007", "备用", False),
    "pokemon/togepi_175.webp":    ("波克比 No.175", "S5 小装饰", True),
    "pokemon/mareep_179.webp":    ("咩利羊 No.179", "S5 小装饰", True),
    "pokemon/piplup_393.webp":    ("波加曼 No.393", "备用", False),
    "pokemon/rowlet_722.webp":    ("木木枭 No.722", "备用", False),
    "pokemon/mimikyu_778.webp":   ("谜拟丘 No.778", "S5 主视觉（INTP 认同感强）", True),
    "pokemon/magikarp_129.webp":  ("鲤鱼王 No.129", "备用", False),
    "pokemon/ditto_132.webp":     ("百变怪 No.132", "备用", False),
    # pokemon —— 伊布家族（合影用，新增）
    "pokemon/vaporeon_134.webp":  ("水伊布 No.134", "S5 伊布家族合影", True),
    "pokemon/jolteon_135.webp":   ("雷伊布 No.135", "S5 伊布家族合影", True),
    "pokemon/flareon_136.webp":   ("火伊布 No.136", "S5 伊布家族合影", True),
    "pokemon/espeon_196.webp":    ("太阳伊布 No.196", "S5 伊布家族合影", True),
    "pokemon/umbreon_197.webp":   ("月亮伊布 No.197", "S5 伊布家族合影", True),
    "pokemon/leafeon_470.webp":   ("叶伊布 No.470", "S5 伊布家族合影", True),
    "pokemon/glaceon_471.webp":   ("冰伊布 No.471", "S5 伊布家族合影", True),
    "pokemon/sylveon_700.webp":   ("★ 仙子伊布 No.700", "S5 伊布家族合影 C 位（她最喜欢）", True),
    # pokemon —— 鬃岩狼人（她喜欢，新增）
    # 注意：PokeAPI 里 745=白昼, 10126=黑夜, 10152=黄昏（10153 是波士可多拉Mega，勿用）
    "pokemon/lycanroc_745_midday.webp":     ("★ 鬃岩狼人·白昼形态 No.745", "S5 狼系展示", True),
    "pokemon/lycanroc_10126_midnight.webp": ("★ 鬃岩狼人·黑夜形态", "S5 狼系展示", True),
    "pokemon/lycanroc_10152_dusk.webp":     ("★ 鬃岩狼人·黄昏形态", "S5 狼系展示", True),
    # pokemon —— 剑盾（她最喜欢的世代，新增）
    "pokemon/grookey_810.webp":    ("敲音猴 No.810", "S5 剑盾区", True),
    "pokemon/scorbunny_813.webp":  ("炎兔儿 No.813", "S5 剑盾区", True),
    "pokemon/sobble_816.webp":     ("泪眼蜥 No.816", "S5 剑盾区", True),
    "pokemon/rillaboom_812.webp":  ("轰擂金刚猩 No.812", "S5 剑盾御三家最终进化", True),
    "pokemon/cinderace_815.webp":  ("闪焰王牌 No.815", "S5 剑盾御三家最终进化", True),
    "pokemon/inteleon_818.webp":   ("千面避役 No.818", "S5 剑盾御三家最终进化", True),
    "pokemon/zacian_888.webp":     ("苍响 No.888", "S5 剑盾传说（剑版封面）", True),
    "pokemon/zacian_10188_crowned.webp": ("苍响·剑之王", "S5 剑盾传说·强化形态", True),
    "pokemon/zamazenta_889.webp":  ("藏玛然特 No.889", "S5 剑盾传说（盾版封面）", True),
    "pokemon/zamazenta_10189_crowned.webp": ("藏玛然特·盾之王", "S5 剑盾传说·强化形态", True),
    "pokemon/eternatus_890.webp":  ("无极汰那 No.890", "S5 剑盾传说", True),
    "pokemon/corviknight_823.webp":("钢铠鸦 No.823", "S5 剑盾知名宝可梦", True),
    "pokemon/dragapult_887.webp":  ("多龙巴鲁托 No.887", "S5 剑盾知名宝可梦", True),
    "pokemon/toxtricity_849.webp": ("颤弦蝾螈 No.849", "S5 剑盾知名宝可梦", True),
    "pokemon/grimmsnarl_861.webp": ("长毛巨魔 No.861", "S5 剑盾知名宝可梦", True),
    "pokemon/wooloo_831.webp":     ("毛辫羊 No.831", "S5 剑盾可爱系", True),
    "pokemon/alcremie_869.webp":   ("霜奶仙 No.869", "S5 剑盾可爱系", True),
    "pokemon/snom_872.webp":       ("雪吞虫 No.872", "S5 剑盾可爱系", True),
    "pokemon/morpeko_877.webp":    ("莫鲁贝可 No.877", "S5 剑盾可爱系", True),
    "pokemon/kubfu_891.webp":      ("熊徒弟 No.891", "S5 剑盾 DLC", True),
    "pokemon/urshifu_892.webp":    ("武道熊师 No.892", "S5 剑盾 DLC", True),
    "pokemon/sirfetchd_865.webp":  ("葱游兵 No.865", "S5 剑盾知名宝可梦", True),
    "pokemon/falinks_870.webp":    ("列阵兵 No.870", "S5 剑盾知名宝可梦", True),
    "pokemon/yamper_835.webp":     ("来电汪 No.835", "S5 剑盾可爱系", True),
    # ui
    "ui/aya_avatar.webp":    ("阿药 B 站头像", "S6 居民卡头像（圆形裁切+描边）", True),
    "ui/aya_space_l.webp":   ("阿药主页大图", "S1 背景纹理（低透明度）", True),
    "ui/aya_space_s.webp":   ("阿药主页小图", "备用", False),
    "ui/aya_nameplate.webp": ("「有爱楷模」名牌", "S5 徽章区 / S7 装饰", True),
    # personal —— 用户本人提供的私人照片（优先级最高，最能打动人）
    "personal/us_switch.webp":        ("★ 我们俩：两人躺床上一起玩 Switch（穿宝可梦睡衣）",
                                       "S7 结尾信核心照片 + S2 蛋糕区回忆卡", True),
    "personal/us_switch_square.webp": ("★ 我们俩（方形裁切版）",
                                       "S6 居民卡配图 / 任意方形卡位", True),
    "personal/dilla_plush_pair.webp": ("★ 两只迪拉熊实物玩偶（舞萌 DX 官方周边，带吊牌）",
                                       "S1 主视觉（真实版，优先于官方立绘）", True),
    "personal/dilla_plush_big.webp":  ("★ 大只迪拉熊玩偶（单只特写）",
                                       "S1 左侧 / S0 加载动画", True),
    "personal/dilla_plush_small.webp":("★ 小只迪拉熊挂件（单只特写）",
                                       "S1 右侧", True),
    "personal/hamster_avatar.webp":   ("★ 仓鼠正脸（宠物）",
                                       "S6 居民卡头像 / 圆形头像位", True),
    "personal/hamster_face.webp":     ("★ 仓鼠特写（宠物）",
                                       "S5 图鉴卡 / 装饰", True),
    "personal/hamster_ball.webp":     ("★ 仓鼠缩成球睡觉 + 漫画「!?」特效",
                                       "S3 彩蛋（翻到某张卡时弹出）/ S5 表情包位", True),
    "personal/hamster_cage.webp":     ("★ 仓鼠趴笼顶（竖图，已裁掉手机状态栏）",
                                       "S6 竖版卡位 / 移动端装饰", True),
    # tomodachi
    "tomodachi/tomo_logo.webp":        ("人森 logo", "S6 标题装饰", True),
    "tomodachi/tomo_kv_1.webp":        ("人森主视觉 1", "S6 背景（低透明度）", True),
    "tomodachi/tomo_kv_2.webp":        ("人森主视觉 2", "S6 备用背景", False),
    "tomodachi/tomo_pickup.webp":      ("人森精选大图", "S6 备用背景", False),
    "tomodachi/tomo_obj_resident.webp":("居民相关物件", "S6 装饰", True),
    "tomodachi/tomo_obj_island_1.webp":("岛屿物件 1", "S6 装饰", True),
    "tomodachi/tomo_obj_island_2.webp":("岛屿物件 2", "S6 装饰", True),
    "tomodachi/tomo_obj_daily_1.webp": ("日常物件 1", "S6 装饰", True),
    "tomodachi/tomo_obj_daily_2.webp": ("日常物件 2", "S6 装饰", True),
    "tomodachi/tomo_obj_daily_3.webp": ("日常物件 3", "S6 装饰", True),
    "tomodachi/tomo_sticker_1.webp":   ("贴纸 1", "S6 贴纸点缀", True),
    "tomodachi/tomo_sticker_2.webp":   ("贴纸 2", "S6 贴纸点缀", True),
    "tomodachi/tomo_sticker_3.webp":   ("贴纸 3", "S6 贴纸点缀", True),
    "tomodachi/tomo_sticker_4.webp":   ("贴纸 4", "S6 贴纸点缀", True),
    "tomodachi/tomo_ic_make.webp":     ("菜单图标·制作", "S6 图标", True),
    "tomodachi/tomo_ic_enjoy.webp":    ("菜单图标·享受", "S6 图标", True),
    "tomodachi/tomo_ic_rel.webp":      ("菜单图标·关系", "S6 图标", True),
    "tomodachi/tomo_ic_create.webp":   ("菜单图标·创造", "S6 图标", True),
    "tomodachi/tomo_ic_item.webp":     ("菜单图标·道具", "S6 图标", True),
    "tomodachi/tomo_bird.webp":        ("小鸟装饰", "S6 装饰", True),
    "tomodachi/tomo_bowling.webp":     ("保龄球小游戏", "S6 彩蛋", False),
    "tomodachi/tomo_resident_1.webp":  ("居民截图 1", "S6 内容示意", False),
    "tomodachi/tomo_resident_2.webp":  ("居民截图 2", "S6 内容示意", False),
    "tomodachi/tomo_resident_3.webp":  ("居民截图 3", "S6 内容示意", False),
    "tomodachi/tomo_resident_4.webp":  ("居民截图 4", "S6 内容示意", False),
    "tomodachi/tomo_island_1.webp":    ("岛屿截图 1", "S6 背景纹理", False),
    "tomodachi/tomo_island_2.webp":    ("岛屿截图 2", "S6 背景纹理", False),
    "tomodachi/tomo_island_3.webp":    ("岛屿截图 3", "S6 背景纹理", False),
    "tomodachi/tomo_island_4.webp":    ("岛屿截图 4", "S6 背景纹理", False),
    "tomodachi/tomo_about_1.webp":     ("介绍图 1", "S6 备用", False),
    "tomodachi/tomo_about_2.webp":     ("介绍图 2", "S6 备用", False),
    "tomodachi/tomo_about_4.webp":     ("介绍图 4", "S6 备用", False),
    "tomodachi/tomo_about_6.webp":     ("介绍图 6", "S6 备用", False),
    "tomodachi/tomo_daily_1.webp":     ("日常截图 1", "S6 备用", False),
    "tomodachi/tomo_daily_2.webp":     ("日常截图 2", "S6 备用", False),
    "tomodachi/tomo_daily_3.webp":     ("日常截图 3", "S6 备用", False),
    "tomodachi/tomo_product.webp":     ("商品图", "备用", False),
}

# MARETU 曲目表（顺序即 S3 卡片顺序）
# 文件名已全部改为纯 ASCII（GitHub Pages 部署要求），日文原名保留在 title 字段
MARETU = [
    ("marettu/mind_brand.webp",       "マインドブランド", "Mind Brand", 1),
    ("marettu/umi_naoshi.webp",       "うみなおし",       "Uminaoshi", 2),
    ("marettu/white_happy.webp",      "ホワイトハッピー", "White Happy", 3),
    ("marettu/coin_locker_baby.webp", "コインロッカーベイビー", "Coin Locker Baby", 4),
    ("marettu/maegamist.webp",        "マエガミスト",     "Maegamist", 5),
    ("marettu/umitagari.webp",        "うみたがり",       "Umitagari", 6),
    ("marettu/shiu.webp",             "しう",             "Shiu", 7),
    ("marettu/dokuhaku.webp",         "ドクハク",         "Dokuhaku", 8),
    ("marettu/binomiuri.webp",        "ビノミウリ",       "Binomiuri", 9),
    ("marettu/sunusumumuriku.webp",   "スヌスムムリク",   "Sunusumumuriku", 10),
]

# 装饰 emoji 分组
DECO_GROUPS = {
    "music":  ["note.svg", "notes.svg", "music_mic.svg", "headphone.svg", "cd.svg", "tape.svg",
               "video.svg", "tv.svg", "phone.svg"],
    "party":  ["cake.svg", "cupcake.svg", "balloon.svg", "gift.svg", "party.svg", "ribbon.svg",
               "crown.svg", "candy.svg", "cookie.svg", "bubbletea.svg", "ice.svg", "cherry.svg",
               "strawberry.svg", "peach.svg", "apple.svg"],
    "sparkle":["star.svg", "star2.svg", "sparkle.svg", "sparkles2.svg", "comet.svg", "dizzy.svg",
               "fire.svg", "rainbow.svg", "diamond.svg", "clover.svg"],
    "nature": ["bear.svg", "cat.svg", "paw.svg", "bird.svg", "chick.svg", "fish.svg", "shell.svg",
               "mushroom.svg", "leaf.svg", "flower.svg", "blossom.svg"],
    "misc":   ["heart_pink.svg", "heart_blue.svg", "bubble.svg", "letter.svg", "envelope.svg",
               "clock.svg", "calendar.svg", "pin.svg", "bulb.svg", "check.svg", "zzz.svg",
               "game.svg", "dice.svg", "trophy.svg", "medal.svg", "camera.svg", "cloud.svg",
               "sun.svg", "moon.svg"],
}


def dims(p: Path):
    try:
        with Image.open(p) as im:
            return im.size
    except Exception:
        return (None, None)


def main():
    items = []
    for sub in ("maimai", "acnh", "pokemon", "tomodachi", "marettu", "ui", "personal"):
        d = ASSETS / sub
        for f in sorted(d.glob("*.webp")):
            rel = f"{sub}/{f.name}"
            note = NOTES.get(rel)
            title, use, rec = note if note else ("", "", False)
            w, h = dims(f)
            items.append({
                "path": f"../assets/{rel}",
                "rel": rel,
                "group": sub,
                "title": title,
                "use": use,
                "recommended": rec,
                "w": w, "h": h,
                "bytes": f.stat().st_size,
            })

    # maimai 的 favicon / touchicon 已由上面的 *.webp 通配符收进来，
    # NOTES 表里已给出 title/use，这里不再重复追加。

    # MARETU 曲目（补上标题/罗马音/序号）
    by_rel = {i["rel"]: i for i in items}
    for rel, jp, romaji, idx in MARETU:
        it = by_rel.get(rel)
        if it:
            it["title"] = jp
            it["title_romaji"] = romaji
            it["track_no"] = idx
            it["use"] = "S3 MARETU 电台曲目卡片封面"
            it["recommended"] = True
            if idx == 4:
                it["easter_egg"] = "翻到这张时全页闪一次 --c-maretu-red，0.6s 后恢复，仅一次"

    deco = []
    for g, names in DECO_GROUPS.items():
        for n in names:
            p = ASSETS / "deco" / n
            if p.exists():
                deco.append({"path": f"../assets/deco/{n}", "rel": f"deco/{n}", "group": g})

    fonts = []
    for f in sorted((ASSETS / "fonts").glob("*.woff2")):
        fonts.append({"path": f"../assets/fonts/{f.name}", "rel": f"fonts/{f.name}",
                      "bytes": f.stat().st_size})

    # 音频
    audio = []
    for f in sorted((ASSETS / "audio").glob("*")):
        if f.suffix.lower() in (".mp4", ".m4a", ".mp3", ".ogg", ".wav", ".aac"):
            audio.append({
                "path": f"../assets/audio/{f.name}",
                "rel": f"audio/{f.name}",
                "bytes": f.stat().st_size,
                "title": "动森背景音乐（ACNH BGM）",
                "use": "全站 BGM，单曲循环。左上角透明音符按钮控制播放/暂停。",
                "codec": "AAC / mp4a，48000 Hz 立体声，约 90 秒",
                "note": "浏览器原生可播，无需转码。默认不自动播放（浏览器会拦截），"
                        "首次用户交互后开始播放。",
            })

    # 第三方库（vendor）
    vendor = []
    for f in sorted((ASSETS / "vendor").glob("*.js")):
        vendor.append({
            "path": f"../assets/vendor/{f.name}",
            "rel": f"vendor/{f.name}",
            "bytes": f.stat().st_size,
            "title": "Three.js r149（UMD 构建）",
            "use": "S7 的 3D 生日蛋糕动画。用 <script src=\"../assets/vendor/three.min.js\"></script> 引入，"
                   "会暴露全局 THREE。",
            "note": "r149 是最后一个干净的 UMD 版本（r150+ 弃用、r160 移除）。"
                    "已实测：全局 THREE 可用，Scene/Camera/Renderer/Geometry 齐全。",
            "cdn_fallback": "https://unpkg.com/three@0.149.0/build/three.min.js",
        })

    manifest = {
        "project": "阿药生日网页",
        "recipient": {
            "name": "阿药",
            "bilibili": "Anria_01017",
            "space": "https://space.bilibili.com/614351218",
            "birthday": "10-17",
            "age": 18,
            "age_note": "这是她的 18 岁生日（成年礼），文案与蜡烛数量都要体现「18」。",
            "signature": "你好，我叫阿药。一个成分复杂的intp",
            "traits": ["二次元", "INTP", "术曲/Vocaloid", "MARETU", "舞萌DX", "动物森友会", "宝可梦",
                       "人森/朋友收集", "养仓鼠（宠物）"],
            "favorites": {
                "acnh_villagers": ["西施惠 Isabelle", "蜜雪儿 Sasha", "史培亚 Fang"],
                "pokemon": ["仙子伊布 Sylveon", "鬃岩狼人 Lycanroc", "伊布家族 Eevee 家族"],
                "pokemon_generation": "剑盾（第八世代）是她最喜欢的世代",
            },
            "pets": {
                "hamster": "两人一起养的仓鼠，出现在多张私人照片里，是很好的情感切入点",
            },
            "personal_note": "B 站头像是表情包动物，不是仓鼠；仓鼠是现实中的宠物，别混淆。",
        },
        "constraints": {
            "dilla_bears_max": 2,
            "dilla_bears_note": "S1 只出现两只迪拉熊。优先用真实玩偶照片（personal/dilla_plush_big + dilla_plush_small，"
                                "或直接整张 dilla_plush_pair），官方立绘 dilla_01_base / dilla_07_lime 作为备选，"
                                "两套不要同时出现。",
            "dilla_bears_files": ["../assets/personal/dilla_plush_big.webp",
                                  "../assets/personal/dilla_plush_small.webp"],
            "dilla_bears_fallback": ["../assets/maimai/dilla_01_base.webp",
                                     "../assets/maimai/dilla_07_lime.webp"],
            "dilla_bears_pair_photo": "../assets/personal/dilla_plush_pair.webp",
            "personal_photos": {
                "note": "用户本人提供的私人照片，情感权重最高，不要裁掉主体、不要加过度滤镜。",
                "us_switch": "../assets/personal/us_switch.webp",
                "dilla_plush_pair": "../assets/personal/dilla_plush_pair.webp",
                "hamster_avatar": "../assets/personal/hamster_avatar.webp",
            },
            "age": 18,
            "age_note": "18 岁生日（成年礼）：S2 要 18 根蜡烛，S7 要有 18 岁蜡烛的 3D 蛋糕动画。",
            "footer_credit": "by Axing",
            "footer_note": "网页最下端必须出现 by Axing。",
            "deploy": {
                "target": "GitHub Pages (github.io)",
                "three_js": True,
                "three_js_note": "部署到 github.io 后本来就是联网访问，"
                                 "因此允许使用 Three.js 做 3D 生日蛋糕。"
                                 "推荐用 CDN 引入（如 unpkg / jsdelivr），或本地 vendor 一份。",
                "base_path_note": "GitHub Pages 项目站点路径形如 "
                                  "https://<user>.github.io/<repo>/，"
                                  "所以 assets 引用要用相对路径 ../assets/...，"
                                  "不要用 /assets/... 这种根路径（会 404）。",
                "ascii_filenames": True,
                "ascii_note": "所有素材文件名已改为纯 ASCII，避免 GitHub Pages 的 URL 编码问题。"
                              "日文原名保留在 manifest 的 title 字段。",
                "case_sensitive": "GitHub Pages 区分大小写，引用路径必须与文件名大小写完全一致。",
            },
            "no_external_network": False,
            "offline_capable": False,
            "output": "web/index.html",
        },
        "palette": {
            "--c-bg-deep": "#12102A", "--c-bg-soft": "#1E1B3A",
            "--c-card": "#FFFDF7", "--c-wood": "#D9A45B", "--c-wood-dark": "#A9762F",
            "--c-maimai-blue": "#2BB3E8", "--c-maimai-pink": "#F5539E", "--c-maimai-yellow": "#FFD23F",
            "--c-maretu-red": "#E8202A", "--c-leaf": "#7BC96F",
            "--c-text": "#2B2740", "--c-text-dim": "#6E6A8A",
        },
        "fonts": {
            "files": fonts,
            "families": {
                "title": "'ZCOOL KuaiLe','Hachi Maru Pop',system-ui,sans-serif",
                "jp": "'Zen Maru Gothic','Hachi Maru Pop',sans-serif",
                "body": "'Noto Sans SC','Zen Maru Gothic',system-ui,sans-serif",
            },
        },
        "sections": [
            {"id": "S0", "name": "加载入场", "assets": ["../assets/personal/dilla_plush_big.webp",
                                                       "../assets/maimai/dilla_01_base.webp"]},
            {"id": "S1", "name": "Hero 主视觉", "assets": ["../assets/personal/dilla_plush_big.webp",
                                                           "../assets/personal/dilla_plush_small.webp",
                                                           "../assets/personal/dilla_plush_pair.webp",
                                                           "../assets/maimai/dilla_01_base.webp",
                                                           "../assets/maimai/dilla_07_lime.webp",
                                                           "../assets/ui/aya_space_l.webp"]},
            {"id": "S2", "name": "18 岁生日蛋糕 / 吹蜡烛", "assets": ["../assets/pokemon/pikachu_025.webp",
                                                              "../assets/pokemon/eevee_133.webp",
                                                              "../assets/pokemon/jigglypuff_039.webp",
                                                              "../assets/acnh/leaf_icon.webp",
                                                              "../assets/personal/us_switch_square.webp"]},
            {"id": "S3", "name": "MARETU 电台", "assets": [m[0].replace("marettu/", "../assets/marettu/") for m in MARETU]
                                                         + ["../assets/personal/hamster_ball.webp"]},
            {"id": "S4", "name": "动森 · 岛上公告（含她喜欢的村民）",
             "assets": ["../assets/acnh/isabelle.webp",
                        "../assets/acnh/sasha_mixueer.webp",
                        "../assets/acnh/fang_shipeiya.webp",
                        "../assets/acnh/kk_slider.webp",
                        "../assets/acnh/celeste.webp"]},
            {"id": "S5", "name": "宝可梦 · 图鉴 + 伊布家族合影 + 剑盾专区",
             "assets": ["../assets/pokemon/eevee_133.webp",
                        "../assets/pokemon/vaporeon_134.webp",
                        "../assets/pokemon/jolteon_135.webp",
                        "../assets/pokemon/flareon_136.webp",
                        "../assets/pokemon/espeon_196.webp",
                        "../assets/pokemon/umbreon_197.webp",
                        "../assets/pokemon/leafeon_470.webp",
                        "../assets/pokemon/glaceon_471.webp",
                        "../assets/pokemon/sylveon_700.webp",
                        "../assets/pokemon/lycanroc_745_midday.webp",
                        "../assets/pokemon/lycanroc_10126_midnight.webp",
                        "../assets/pokemon/lycanroc_10152_dusk.webp",
                        "../assets/pokemon/zacian_888.webp",
                        "../assets/pokemon/zamazenta_889.webp",
                        "../assets/pokemon/eternatus_890.webp",
                        "../assets/pokemon/corviknight_823.webp",
                        "../assets/pokemon/dragapult_887.webp",
                        "../assets/pokemon/alcremie_869.webp",
                        "../assets/pokemon/morpeko_877.webp",
                        "../assets/personal/hamster_face.webp",
                        "../assets/ui/aya_nameplate.webp"]},
            {"id": "S6", "name": "人森 · 居民卡", "assets": ["../assets/personal/hamster_avatar.webp",
                                                          "../assets/ui/aya_avatar.webp",
                                                          "../assets/personal/hamster_cage.webp",
                                                          "../assets/tomodachi/tomo_logo.webp",
                                                          "../assets/tomodachi/tomo_kv_1.webp"]},
            {"id": "S7", "name": "结尾信 + 3D 生日蛋糕动画",
             "assets": ["../assets/personal/us_switch.webp",
                        "../assets/personal/us_switch_square.webp",
                        "../assets/ui/aya_nameplate.webp"]},
        ],
        "audio": audio,
        "vendor": vendor,
        "images": items,
        "deco": deco,
        "counts": {
            "images": len(items),
            "deco_svg": len(deco),
            "fonts": len(fonts),
            "audio": len(audio),
            "vendor": len(vendor),
        },
    }

    out = ASSETS / "manifest.json"
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {out}")
    print(f"images={len(items)} deco={len(deco)} fonts={len(fonts)}")


if __name__ == "__main__":
    main()
