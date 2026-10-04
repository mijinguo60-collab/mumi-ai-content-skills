# 参考来源与使用边界

本仓库把公开项目的方法重新编排为 Mumi 的工作流。除明确标注为 vendored、并随原许可证保留的 `gzh-design-skill` 运行资料外，不复制第三方仓库的原始提示词、示例图片或品牌表达。

| 来源 | 使用方式 | 边界 |
| --- | --- | --- |
| [Punk-Skill](https://github.com/adrianpunk/Punk-Skill) | 参考 v1.0.0-mit 的风格模块、风格选择和系列一致性方法 | 每篇内容必须选择一个真实 style id；不混用主风格，不复制源码和原提示词 |
| [gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) | `mumi-gzh-design/vendor/gzh-design-skill/` 搬运主题索引、主题组件、通用组件、格式规则、校验和预览脚本，实际按其方法排版 | 公众号是长文加插图，不制作小红书式多页卡片；vendor 内保留上游 LICENSE 和来源说明，Mumi 的企鹅与自动化规则在外层 skill 中实现 |
| [khazix-skills](https://github.com/KKKKhazix/khazix-skills) | 参考写作流程和中文禁用词检查 | 不使用其人物口吻，不复制品牌表达 |
| [stop-slop](https://github.com/hardikpandya/stop-slop) | 参考具体化、删套话、主动语态和节奏检查 | 只保留通用编辑原则 |
| [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 参考选题研究的任务拆分和来源意识，落地为 `mumi-topic-research` 的独立证据记录 | 不把其仓库内容当作 Mumi 的现成技能直接执行 |

企鹅参考图和本次确认的动作库属于 Mumi 个人 IP 资产，统一放在 `assets/penguin/`。
