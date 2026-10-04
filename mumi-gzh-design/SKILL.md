---
name: mumi-gzh-design
description: 把 Mumi 同题但独立的微信公众号长文排成可预览、可复制的内联 HTML；使用 gzh-design-skill 的主题和组件方法，并在插图、提示卡、分隔图中加入同一 Punk 风格的企鹅 IP。
---

# Mumi 微信公众号排版

公众号是长文加插图，不是小红书/抖音多页图文卡片，也不制作公众号封面卡。输入是独立的公众号 Markdown，输出是正文 HTML 和可观看的 `preview.html`。

## 排版流程

本 skill 已把上游 `gzh-design-skill` 的运行时资料放在 `vendor/gzh-design-skill/`。它不是一个“参考链接”，而是本仓库实际使用的主题索引、通用组件、主题组件、归一化规则、校验脚本和预览脚本。

1. 先读 `vendor/gzh-design-skill/references/theme-index.md`，根据题材自动选择一个主题并记录理由；教程、测评、清单、工具工作流默认优先摸鱼绿，工具对比可选摸鱼票据风。
2. 同时读选定主题文件和 `vendor/gzh-design-skill/references/common-components.md`，按主题的“文章类型 → 组件配方”和“完整文章模板骨架”装配，不凭记忆手写一套普通 HTML。
3. 按上游规则解析文章：引言、章节、步骤、提示、代码/Prompt、结果、失败记录、结尾和图片说明都要分别映射；关键词下划线、章节编号、全角标点和签名区也按上游规则处理。
4. 插入与当前 Punk `style_lock` 一致的企鹅插图、提示卡和分隔图。图片是正文的视觉辅助，不替代正文；提示卡和分隔图必须使用为该比例单独生成的横图，禁止把竖图 `object-fit:cover` 裁成窄条。
5. 生成干净的 `<section>...</section>` 片段，再用上游 `vendor/gzh-design-skill/scripts/wrap_preview.py` 生成带复制按钮的 `preview.html`。
6. 用上游 `vendor/gzh-design-skill/scripts/validate_gzh_html.py` 校验，ERROR 和 WARNING 都清零后才交付。现有 `scripts/validate_gzh_structure.py` 仅作为旧兼容检查，不能替代上游校验器。

## 硬约束

- 不输出 `<html>`、`<head>`、`<body>`、`<style>`、`<script>`、`<div>` 外壳。
- 样式内联；文字叶节点使用 `<span leaf="">` 包裹。
- 图片使用占位符或本地相对路径，不能编造远程 URL。
- 普通图片遵循 `max-width:100%;height:auto;display:block;margin:0 auto`；分隔图和提示卡按它们的实际宽高比自然显示，不能强行使用正文比例，也不能从竖图裁出一条企鹅脚。
- 公众号文章和小红书/抖音图文共享选题，但文案、章节和图片用途必须独立。
- 当前测试只需要可观看预览；正式发布由 Muse 自己执行。

## 上游资料与归属

`vendor/gzh-design-skill/UPSTREAM.md` 记录了来源、版本和许可证。只搬运排版运行所需资料，不把上游仓库当作本账号内容；Mumi 的企鹅视觉规则和自动化门槛由本仓库补充。
