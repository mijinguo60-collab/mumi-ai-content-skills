# vendored upstream: gzh-design-skill

来源：<https://github.com/isjiamu/gzh-design-skill>

本目录保留微信公众号排版实际运行所需的上游流程、主题组件、通用组件、格式归一化规则、校验脚本和预览脚本。当前同步基准为 2026-10-04 从上游 `main` 读取的版本；上游 `SKILL.md` blob：`cd1d70dd3427c5821bfde7589832ed0ba8a01322`。

许可证：上游仓库随附 `LICENSE`，为 GNU Affero General Public License v3。该许可证文件与本目录中的派生/搬运文件一并保留。Mumi 自己的编排、企鹅 IP、Punk 风格门槛和自动化规则写在仓库外层的 `mumi-gzh-design/SKILL.md`，不声称属于上游。

使用边界：这里只纳入排版运行所需文件，不复制上游画廊和示例主题预览；实际执行时先读 `references/theme-index.md`，再读选定主题文件和 `references/common-components.md`，最后运行 `scripts/validate_gzh_html.py` 与 `scripts/wrap_preview.py`。
