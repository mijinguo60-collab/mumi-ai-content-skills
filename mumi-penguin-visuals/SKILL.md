---
name: mumi-penguin-visuals
description: 为 Mumi聊Ai 选择 Punk v1 视觉风格，并调用三只同款企鹅的三视图、表情和动作参考库，生成统一的 3:4 图文卡片及公众号插图、提示卡和分隔图。
---

# Mumi 企鹅 IP 与生图

这是一个带门槛的视觉编排 skill，不是普通的“生成一张可爱企鹅图”。任何图片生成前都必须先完成内容、风格、动作和站位决策。

## 1. 参考资产

- 单只企鹅三视图：`assets/penguin/reference-library/three-view/single-penguin-three-view.jpg`
- 三只企鹅组合三视图：`assets/penguin/reference-library/three-view/penguin-trio-three-view.jpg`
- 单只企鹅动作/表情库：`assets/penguin/reference-library/single-expression/`，15 张独立的 16:9 横图，每张 5 行×8 格。
- 三只企鹅组合动作库：`assets/penguin/reference-library/group-expression/`，15 张独立的 16:9 横图，每张 5 行×8 格。
- 原始主体参考：`assets/penguin/penguin-stack-base.jpg`。

30 张动作/表情图必须一张一张作为独立参考文件使用和上传，不能拼成总览图；拼图会显著降低每个动作格子的可读性。

先用三视图锁定主体，再从单只库或组合库选择动作参考。不要只依赖文字描述猜动作。

## 2. IP 硬约束

- 三只企鹅完全同款：黑色圆润身体、白色脸/腹部、白色大眼、橙色嘴和橙色脚、手绘不规则轮廓。
- 不固定角色身份，不把顶部/中部/底部永久设定成讲解者或执行者。
- 三只可以左右并排、左中右、三角、对角、前后景、分散站位、横向站位或根据内容形成其他可读构图；不能默认所有画面都是叠罗汉。
- 表情、动作、姿势、衣服和道具可以变化，但不能改变基础脸型、物种和黑白橙识别点。
- 黄色外套图只是参考变体，不是固定服装规则。
- 需要三只时必须正好三只；单只参考图只在明确选择单只库时使用。

## 3. Punk 风格门槛

从 `references/style-atoms.md` 选择一个真实 Punk v1 style id。选择依据必须写清：选题隐喻、内容类型、材料/线条/构图和为什么适合企鹅。一个内容包只锁定一个主风格。

同一个 style lock 必须贯穿：

- 小红书/抖音 3:4 封面、内容卡和感谢卡；
- 公众号正文插图、提示卡、分隔图和结尾装饰；
- 同一选题的所有视觉变体。

不得把封面用拼贴、内页用像素、公众号分隔图用摄影。可以改变画幅、主体大小和留白，不能换主视觉语法。

## 4. 生图前决策卡

```yaml
content_type: tutorial | test | comparison | troubleshooting | opinion | result
platform_branch: social_cards | wechat_article
style_id:
style_reason:
visual_metaphor:
reference_set: single | trio | both
expressions:
actions:
positions:
clothing_and_props:
exact_text:
aspect_ratio: 3:4 | 16:9 | component-specific
```

小红书/抖音图文必须是 3:4 竖图：第1张封面，第2张到第X张内容卡，最后一张感谢/互动卡。每张都要把本页信息和企鹅动作组合成完整卡片，不得只放纯插图。

微信公众号不做多页卡片和封面卡。它使用独立长文，图片只作为文章里的插图、提示卡、分隔图和结尾装饰。提示卡和分隔图要按公众号组件的实际比例生成。

## 5. 文字准确性

用户要求图片文字由生图模型直接生成。将要出现的文字放进 prompt 的 `exact_text` 字段，要求逐字生成。生成后必须读取图片文字并与 `exact_text` 对比：

1. 发现乱码、错别字、漏字、错序或无意义字，重新生成；
2. 重新生成仍失败，标记为待修复，不发布；
3. 不把错误图片交给 Muse 的发布步骤。

## 6. Prompt 结构

每张图的 prompt 至少包含：主体参考图、单只/三只数量、表情、动作、站位、一个内容隐喻、锁定的 Punk 风格、画幅、确切文字和禁止漂移项。禁止使用“随便摆放”“可爱一点”“自由发挥”代替构图决策。
