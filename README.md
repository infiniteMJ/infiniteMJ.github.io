# Math Blog

基于 Jekyll 的数学博客，支持 LaTeX 公式。

## 本地运行

```bash
bundle install
bundle exec jekyll serve
```

浏览器打开 http://localhost:4000

## 写新文章

在 `_posts/` 下新建文件，格式：`YYYY-MM-DD-标题.md`

```yaml
---
layout: post
title: "你的标题"
date: 2025-03-14 12:00:00 +0800
---

正文内容...
```

## 数学公式写法

- 行内：`$E = mc^2$`
- 块级：`$$\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}$$`

## 部署到 GitHub Pages

将此仓库推送到你的 `mj.github.io` 仓库，GitHub 会自动构建并发布。
