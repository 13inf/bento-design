# Bento Design

[English](README.en.md)

一个用于海报、发布会信息页、演示文稿和网页展示区的 Bento 视觉设计 Skill。它从内容主张、语义断行、字重与字图关系开始，再选择合适的网格。

## 效果展示

以下为四张由本 Skill 指导生成的概念图：文字主导、产品特写、信息网格与家庭储能方案海报。前三张是通用虚构概念；第四张已移除原图中的身份、队伍、公司、品牌与赛事信息。展示图不代表真实产品参数、实际应用截图或实测效果。

![文字主导概念海报](docs/showcases/01-typography.png)

| 产品特写 | 信息网格 |
| --- | --- |
| ![产品特写概念图](docs/showcases/02-product-study.png) | ![信息网格概念图](docs/showcases/03-information-grid.png) |

**家庭储能方案概念海报**

<p align="center">
  <img src="docs/showcases/04-energy-dispatch.png" width="560" alt="已移除身份和品牌信息的家庭储能调度概念海报">
</p>

[查看生成提示词](docs/showcases/prompts.md)

## 安装

下载或克隆本仓库，在仓库根目录打开 PowerShell 7：

```powershell
pwsh -File .\scripts\install.ps1
```

脚本将 `SKILL.md`、`agents`、`assets`、`references`、`LICENSE` 和 `NOTICE.md` 安装到本机 Skills 目录。它优先使用 `CODEX_HOME`，否则使用用户目录下的 `.codex/skills`。如果目标已有同名目录，脚本会停止，不覆盖现有内容。开始新对话后使用 `$bento-design`；客户端尚未刷新技能列表时，重新打开客户端。

需要指定 Skills 目录时：

```powershell
pwsh -File .\scripts\install.ps1 -SkillsDirectory 'D:\MySkills'
```

升级前先把旧版本移到 Skills 搜索目录之外备份，再运行安装脚本；不要在 Skills 搜索目录中同时放置两个同名版本。

## 使用

```text
使用 $bento-design，把这六条产品卖点做成一张 3:4 中文海报。
先确定一个主张，再安排字重、语义断行、卡片角色和渐变范围。
保留原始参数，缺少素材的位置明确标出。
```

```text
使用 $bento-design，重做当前页面的功能展示区。
采用文字主卡与一处深色卡，保留现有文案和交互，适配手机布局。
```

```text
使用 $bento-design，先给我一份 16:9 发布会页面布局方案，不写代码。
说明主张、文字层级、图片位置和素材缺口。
```

## 文件说明

- [SKILL.md](SKILL.md)：工作流与验收规则。
- [字重、比例与色彩](references/typography-color.md)：字体角色、中文断行与渐变范围。
- [参考图参数台账](references/reference-measurements.md)：19 张学习图中的字号、字距与段距、色号、卡片间距和圆角比例，并区分原图标注、计算换算与实施建议。
- [布局配方](references/layout-recipes.md)：布局方向与网页示例。
- [图像方向](references/image-direction.md)：生成提示词骨架与针对性修订方法。
- [tokens.css](assets/tokens.css)：可选择使用的局部网页样式。

说明以中文撰写；实际设计的语言、品牌、技术栈与载体由用户需求决定。Skill 不包含图像模型、设计软件或自动导出工具。原图参数是教程示例，不是品牌官方规范；生成式图像不保证精确执行字号、字距或圆角。

## 检查

```powershell
python -X utf8 .\scripts\validate.py
```

脚本检查文件结构、UTF-8、内部引用与示意图结构，不能替代最终画面的视觉检查。安装脚本需要 PowerShell 7；校验脚本使用 Python 3.10+ 标准库。正常调用 Skill 不需要运行这些脚本。

## 许可与素材

[MIT License](LICENSE)。素材范围与许可说明见 [NOTICE.md](NOTICE.md)。本项目独立开发，不声称获得任何品牌的官方背书。
