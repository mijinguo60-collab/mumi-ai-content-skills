---
name: mumi-gzh-design
description: 把 Mumi 同题但独立的微信公众号长文排成可预览、可复制的内联 HTML；使用 gzh-design-skill 的主题和组件方法，并在插图、提示卡、分隔图中加入同一 Punk 风格的企鹅 IP。
---

# Mumi 微信公众号排版

公众号是长文加插图，不是小红书/抖音多页图文卡片，也不制作公众号封面卡。输入是独立的公众号 Markdown，输出是正文 HTML 和可观看的 `preview.html`。

## 排版流程

1. 读取 `references/theme-index.md`，根据题材自动选择一个主题并记录理由。
2. 读取 `references/common-components.md`，使用对应组件，不凭记忆手写普通 HTML。
3. 从文章结构识别引言、章节、步骤、提示、代码/提示词、结果、失败记录和结尾。
4. 插入与当前 Punk `style_lock` 一致的企鹅插图、提示卡和分隔图。它们是文章视觉辅助，不替代正文。
5. 生成干净的 `<section>...</section>` 片段，以及带预览和复制按钮的 `preview.html`。
6. 运行 `scripts/validate_gzh_structure.py`；失败就修复，禁止交付未验证的 HTML。

## 硬约束

- 不输出 `<html>`、`<head>`、`<body>`、`<style>`、`<script>`、`<div>` 外壳。
- 样式内联；文字叶节点使用 `<span leaf="">` 包裹。
- 图片使用占位符或本地相对路径，不能编造远程 URL。
- 图片最大宽度100%，高度自动，分隔图和提示卡不能强行使用正文比例。
- 公众号文章和小红书/抖音图文共享选题，但文案、章节和图片用途必须独立。
- 当前测试只需要可观看预览；正式发布由 Muse 自己执行。
