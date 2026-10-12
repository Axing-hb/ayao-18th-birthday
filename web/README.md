# web/ · 网页主体输出目录

这个目录是留给 **gpt6astra** 的。

## 要产出什么

```
web/index.html      ← 单文件网页（CSS 内联 <style>，JS 内联 <script>）
```

如果要拆分：

```
web/index.html
web/style.css
web/main.js
```

## 开工前必读

1. [`../docs/HANDOFF.md`](../docs/HANDOFF.md) —— 精简执行说明（照着做就行）
2. [`../docs/PLAN.md`](../docs/PLAN.md) —— 完整规划（配色 / 字体 / 结构 / 交互 / 文案 / 验收清单）
3. [`../assets/manifest.json`](../assets/manifest.json) —— 素材路径、尺寸、用途、推荐标记
4. [`../assets/_preview.html`](../assets/_preview.html) —— 素材总览页，可以肉眼先看一遍

## 三条最容易踩的坑

1. **迪拉熊只放两只** —— 只用 `../assets/maimai/dilla_01_base.webp` 和 `../assets/maimai/dilla_07_lime.webp`，只在 S1 出现。
2. **路径是 `../assets/...`** —— 因为网页在 `web/` 子目录里，素材在上一级。
3. **不许改成外链** —— 字体和图片全部已本地化，改成 Google Fonts / CDN 会让断网打开时挂掉。

## 自检

写完后直接双击 `web/index.html` 用浏览器打开（`file://` 协议），确认：

- [ ] 断网状态下字体、图片、图标全部正常
- [ ] 375px 宽（手机）无横向滚动
- [ ] 迪拉熊只有两只
- [ ] 控制台无报错

再跑一次素材校验，确认没有误改素材：

```powershell
& "C:\Users\29631\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe" ..\ref\validate.py
```
