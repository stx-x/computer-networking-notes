# 计算机网络 · 全章中文译注（网页版）

《Computer Networking: A Top-Down Approach》（第 9 版）八章中文译注的 VitePress 站点。
内容与仓库根目录下的 8 个 `ch0x-*` Typst 工程同源，由脚本自动转换。

## 结构

```
site/
├─ docs/
│  ├─ .vitepress/
│  │  ├─ config.ts          站点配置（导航 / 侧边栏 / 搜索）
│  │  ├─ chapters.json      由转换脚本生成：章节目录与页码
│  │  └─ theme/             自定义主题（排版 / 组件 / 配色）
│  ├─ ch01 … ch08/          每节一个 .md
│  ├─ public/figs/ch0x/     插图（从各章 figs/ 复制）
│  ├─ index.md              首页
│  └─ about.md
├─ tools/
│  ├─ convert.py            Typst → Markdown 转换器（主入口）
│  └─ mathconv.py           Typst 数学 → LaTeX
└─ .github/workflows/deploy.yml
```

## 本地开发

```bash
cd site
npm install
npm run dev        # http://localhost:5173
npm run build      # 产物在 docs/.vitepress/dist
npm run preview
```

## 重新生成正文

改动任意 `ch0x-*/sec/*.typ` 之后：

```bash
python3 site/tools/convert.py
```

脚本会重写 `docs/ch0x/*.md`、复制插图、并刷新 `docs/.vitepress/chapters.json`（侧边栏依赖它）。
依赖只有 Python 3 标准库。

转换器支持的构造：`==` 标题、`-`/`+` 列表、`*粗*`/`_斜_`、`$数学$`、`#fig()`、`#figure(…table(…))`、
`#eq($…$, n)`、`#example`/`#key`/`#remark`/`#warn`、`#aside()`/`#focus()`、`#bin()`/`#listing()`。

## 部署到 GitHub Pages

1. 仓库根目录执行 `git subtree push --prefix site origin gh-pages`，或直接把 `site/` 作为仓库根。
2. 若把 `site/` 作为仓库根，workflow 里 `working-directory: site` 要删掉。
3. 仓库 Settings → Pages → Build and deployment 选择 **GitHub Actions**。
4. 推送到 `main` 即自动构建发布。

> 项目站点（`username.github.io/repo/`）必须设置 `DOCS_BASE=/repo/`，workflow 已按仓库名自动处理。
> 用户站点（`username.github.io`）或绑定自定义域名时，把 workflow 里的 `DOCS_BASE` env 删掉即可。

## 设计说明

- 字体：Inter（拉丁）+ 苹方 / HarmonyOS Sans（中文），等宽用 JetBrains Mono。
- 正文 17px / 1.88 行高 / 716px 栏宽，接近书籍的单栏阅读宽度。
- 配色：靛蓝 `#4f46e5` → 青 `#06b6d4` 渐变作为强调色，深浅色双主题。
- 图片统一白底圆角，保证深色模式下插图仍可读。
- 表格超过栏宽时横向滚动，不挤压列宽。
