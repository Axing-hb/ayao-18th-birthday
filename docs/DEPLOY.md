# 部署到 GitHub Pages · 操作手册

> 目标：把 `ayao-birthday/` 部署成 `https://<你的用户名>.github.io/<仓库名>/`
> 做完之后，把这个链接发给阿药就行。

---

## 一、部署前已处理好的事（不用你操心）

| 项目 | 状态 |
| --- | --- |
| 非 ASCII 文件名 | ✅ 已全部改为 ASCII（30 个术曲封面 `日文.webp` → `罗马音.webp`） |
| 日文标题会不会丢 | ✅ 不会。日文原名保留在 `assets/manifest.json` 的 `title` 字段，网页文字照常显示日文 |
| 大写字母文件名 | ✅ 无。GitHub Pages 区分大小写，全小写最安全 |
| `_raw/` 备份（34 MB） | ✅ 已在 `.gitignore` 里排除，不会上传 |
| 单文件超限 | ✅ 最大 2.95 MB，远低于 GitHub 的 100 MB 上限 |
| 素材路径 | ✅ 全用相对路径 `../assets/...`，项目站点子路径下也能正常加载 |

**上传后仓库体积约 17 MB**（不含 `_raw/`）。

---

## 二、Three.js 相关（重要变化）

**之前**：要求纯 CSS 3D、禁止 Three.js，理由是「断网也要能看」。

**现在**：部署到 github.io，本来就是联网访问，**这个顾虑消失了。3D 生日蛋糕允许用 Three.js。**

给 GPT 的提示词里已经改成允许，且**已经帮你本地 vendor 好了**：

```
assets/vendor/three.min.js     ← Three.js r149 UMD，608 KB，已下载并实测可用
```

**为什么是 r149 而不是最新版**：Three.js 从 **r150 起弃用了 UMD 构建**（`build/three.min.js`），
r160 直接移除。r149 是最后一个能直接 `<script>` 引入、暴露全局 `THREE` 的版本。

```
r149  → UMD 干净，无弃用警告  ✅ 用这个
r150+ → 会打印 "deprecated with r150+" 警告
r160+ → UMD 构建已删除
```

已用 Node 实测过 r149：

```
OK: 全局 THREE 已暴露
  REVISION     = 149
  有 Scene / Camera / Renderer / Geometry / Material / Light  = true
  蜡烛数       = 18 (18 根 ✓)
```

**网页里这样引：**

```html
<!-- 优先本地（推荐，抗 CDN 挂掉 / 被墙） -->
<script src="../assets/vendor/three.min.js"></script>

<!-- 兜底：本地文件缺失时才用 CDN -->
<script src="https://unpkg.com/three@0.149.0/build/three.min.js"></script>
```

> ⚠️ 不要用 ES module 版本（`three.module.js` + `import`）。
> 一是本地 `file://` 调试会被 CORS 拦，二是没必要——r149 的 UMD 已经够用。

---

## 三、部署步骤

### 1. 建仓库

在 GitHub 新建一个仓库，例如 `ayao-18th-birthday`。

**关键**：如果仓库名是 `<你的用户名>.github.io`，访问地址就是根路径；
否则是项目站点，地址带子路径 `https://<用户名>.github.io/<仓库名>/`。

两种都可以，**推荐项目站点**（名字随意、以后能建别的）。

### 2. 把 `ayao-birthday/` 的内容推到仓库根

```powershell
cd ayao-birthday

git init
git add .
git commit -m "阿药 18 岁生日网页"

# 把 <用户名> 和 <仓库名> 换成你的
git remote add origin https://github.com/<用户名>/<仓库名>.git
git branch -M main
git push -u origin main
```

推之前先确认 `_raw/` 没被带上：

```powershell
git status --short | Select-String "_raw"
# 应该没有任何输出
```

如果有输出，说明 `.gitignore` 没生效，检查 `.gitignore` 是否在 `ayao-birthday/` 目录里。

### 3. 开启 Pages

仓库页面 → **Settings** → 左侧 **Pages**：

- **Source**：`Deploy from a branch`
- **Branch**：`main`，目录选 **`/ (root)`**
- 点 **Save**

等 1–3 分钟，刷新页面会显示访问地址：

```
https://<用户名>.github.io/<仓库名>/
```

---

## 四、入口文件问题（必须处理）

现在网页主体在 `web/index.html`，但 GitHub Pages 默认找**根目录**的 `index.html`。

所以需要在仓库根放一个跳转页，或者把网页挪到根目录。

### 推荐做法：根目录放跳转页

在 `ayao-birthday/index.html`（仓库根）放：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="0; url=./web/index.html">
<title>生日快乐 · 阿药</title>
<style>
  html,body{margin:0;height:100%;background:#12102A;color:#FFFDF7;
    display:flex;align-items:center;justify-content:center;
    font-family:system-ui,sans-serif}
</style>
</head>
<body>
  <p>正在打开… <a href="./web/index.html" style="color:#2BB3E8">点这里</a></p>
</body>
</html>
```

> 更干净的做法：让 GPT 直接把网页输出到仓库根的 `index.html`，
> 素材路径从 `../assets/...` 改成 `assets/...`。
> 但那样所有路径都要改，**建议就用跳转页**，省事且不易出错。

---

## 五、上线前自查

```powershell
# 1. 素材校验（路径 / 尺寸 / 约束 / 部署就绪）
& "C:\Users\29631\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe" `
  ayao-birthday\ref\validate.py
```

应该看到：

```
OK: manifest validated, no errors
deploy target = GitHub Pages (github.io)  three.js = True
```

然后本地用**起一个 http 服务**测试（比 `file://` 更接近线上环境）：

```powershell
cd ayao-birthday
& "C:\Users\29631\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe" `
  -e "const h=require('http'),f=require('fs'),p=require('path');h.createServer((q,s)=>{let u=decodeURIComponent(q.url.split('?')[0]);if(u==='/')u='/index.html';const fp=p.join(process.cwd(),u);f.readFile(fp,(e,d)=>{if(e){s.writeHead(404);return s.end('404 '+u)}s.writeHead(200);s.end(d)})}).listen(8080,()=>console.log('http://127.0.0.1:8080'))"
```

浏览器打开 `http://127.0.0.1:8080/`，逐项确认：

- [ ] 页面正常打开，样式生效
- [ ] 字体是可爱体（不是系统默认宋体/黑体）
- [ ] **背景音乐能播**，左上角音符按钮可开关
- [ ] 图片全部显示（**重点看术曲封面 10 张**，因为改过文件名）
- [ ] 3D 蛋糕动画正常（滚动到底部触发）
- [ ] 网页最下端有 `by Axing`
- [ ] F12 控制台**没有 404 报错**

### 部署后再查一遍

线上打开后按 F12 → Network 面板，刷新，筛选 `404`：

- 如果术曲封面 404 → 文件名大小写或路径不对
- 如果字体 404 → `assets/fonts/` 没上传
- 如果音乐 404 → `assets/audio/` 没上传

---

## 六、常见坑

| 现象 | 原因 | 解决 |
| --- | --- | --- |
| 页面 404 | 根目录没有 `index.html` | 加跳转页，或把网页挪到根目录 |
| 样式全丢、图片全裂 | 用了绝对路径 `/assets/...` | 改成相对路径 `../assets/...` 或 `assets/...` |
| 部分图片 404 | 文件名大小写不匹配 | GitHub Pages 区分大小写，路径要和文件名完全一致 |
| 推送被拒（文件过大） | `_raw/` 被带上了 | 确认 `.gitignore` 生效，`git rm -r --cached assets/_raw` |
| 改了没生效 | 浏览器缓存 / Pages 构建中 | 等 1–3 分钟，强制刷新 `Ctrl+F5` |
| 音乐不播 | 浏览器拦截自动播放 | 这是设计如此，需要用户先点一下页面 |

---

## 七、隐私提醒

这个仓库包含**你们的私人照片**（合照、仓鼠、家里环境）。

- 如果仓库设为 **Public**，任何人都能看到这些照片
- 建议设为 **Private**（GitHub Pages 免费版对 Private 仓库也支持，但需要 GitHub Pro；
  免费账号的 Private 仓库 Pages 需要把仓库设为 Public，或用 Cloudflare Pages 等替代）

**如果不想公开**，几个选择：

1. 升级 GitHub Pro，Private 仓库也能开 Pages
2. 用 **Cloudflare Pages** / **Vercel** / **Netlify**（都支持私有仓库 + 免费）
3. 只把网页发给阿药，不部署（本地双击 `web/index.html` 也能看，只是断网时字体和音乐仍在）

**这个你自己决定**，我不替你选。
