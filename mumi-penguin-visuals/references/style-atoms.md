# Punk 风格选择索引

本文件把 Punk-Skill v1 的风格模块作为内容生产的选择层。每次内容只选择一个真实 `style_id`，然后把它和企鹅 IP、主题隐喻、平台比例合并成 `style_lock`。不复制第三方源码、原始提示词或示例图片。

## 选择门槛

1. 先根据选题决定一个视觉隐喻：工具、步骤、失败、结果、系统或观点，只选一个。
2. 再从下面的真实 style id 中选择最适合的一个，并写出选择理由。
3. 该 style id 必须贯穿小红书/抖音3:4封面、内容卡、感谢卡，以及公众号插图、提示卡和分隔图。
4. 不能封面用拼贴、内页用像素、公众号分隔图用摄影；换风格必须视为新的内容系列。

## Punk v1 风格 ID

| Style ID | 适合内容方向 |
| --- | --- |
| `black-white-minimal-concept` | 抽象观点、战略、哲学、批判 |
| `black-white-etching-editorial-cover` | 机制解释、深度教程、古典科学感 |
| `semantic-minimal-translation` | 单词、短句、概念转译 |
| `retro-torn-collage` | 社交传播、文化观察、复盘 |
| `block-world` | 工具、教程、系统搭建、工作流 |
| `giant-perspective-chinese-title` | 中文标题主导、强冲击社媒封面 |
| `interleaved-title-editorial-poster` | 主结论、清单、编辑海报 |
| `layered-paper-cut-concept-poster` | 单一隐喻、教程总览、纸雕空间 |
| `paper-emboss-deboss-cover` | 高级方法论、资料包、工艺感封面 |
| `godot-2d-pixel-metaphor-poster` | 升级、失败点、流程闯关 |
| `osb-industrial-blue-line-metaphor` | 系统、效率、工程流程 |
| `brick-world` | 计划、教育、团队、自动化 |
| `consulting-report-visual` | 商业、策略、产品分析 |
| `research-journal-concept` | AI机制、实测、研究、材料 |
| `retro-diffuse-gradient` | 艺术、设计、情绪化文章 |
| `midcentury-surreal-editorial-cover` | AI工具、数字工作、时代错位隐喻 |
| `retro-futurism` | 自动化、系统、复古未来设施 |
| `minimal-public-space-photography` | 观点长文、文化观察、空间秩序 |
| `business-magazine-front-page` | AI、创业、趋势、商业科技 |
| `black-white-gray-avant-geometry` | 实验性观点、现代主义、几何构成 |
| `black-red-silhouette` | 工具教程、风险、效率、速度 |
| `avant-retro-architecture-poster` | 城市、空间、展览、建筑隐喻 |
| `retro-ink-dot-matrix-metaphor` | AI、科技、系统、研究 |
| `black-midcentury-modernist-cover` | 服务场景、产品人物、建筑概念 |
| `silver-foil-blue-minimal` | 成长路径、方法论、AI工具 |
| `color-neo-constructivist-megastructure-poster` | 发布、热点、强冲击主题 |
| `retro-japanese-sci-fi-anime-cover` | AI、代码、心理、社会冲突 |
| `french-minimal-ink-poster` | 关系、制度、选择、抽象观点 |
| `brand-collaboration-connection` | 工具集成、品牌联动、自动化 |
| `anthropic-research-style` | AI、研究、知识、系统 |
| `kimi-stlye` | AI、产品、材料、创意项目 |
| `minimal-light-tech` | 科技产品、工具教程、轻科技 |
| `minimal-visual-metaphor` | AI、商业科技、组织和系统变化 |
| `pixel-avatar` | 单只企鹅头像、栏目图标、像素化角色 |
| `grotesque-soul-sketch` | 情绪反应、失败、吐槽 |
| `messy-crayon-pet-portrait` | 生活化教程、轻松栏目 |
| `fashion-sketch-observation` | 人设、栏目视觉、趋势观察 |
| `polaroid-keepsake` | 实测结果、里程碑、系列卡片 |
| `minimal-paper-acrylic-block-illustration` | 头像、概念卡、留白插图 |
| `surreal-pop-up-paper-landscape` | 超现实封面、栏目视觉、品牌记忆 |

## style_lock 模板

```yaml
style_lock:
  style_id: <真实 Punk style id>
  reason: <选题和风格的匹配理由>
  material: <纸张/版画/拼贴/像素/空间等>
  line_or_shape: <线条、几何、构图语言>
  palette: <主色和企鹅黑白橙如何共存>
  lighting: <光影或印刷质感>
  typography: <图片内文字的层级和安全区>
  forbidden_mixing: <本系列禁止混入的主风格>
```
