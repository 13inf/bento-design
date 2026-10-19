# Bento Design

[简体中文](README.zh-CN.md)

A reusable design skill for posters, presentation pages, slide decks, and web feature sections. It starts with the message, semantic line breaks, type hierarchy, and the relationship between text and imagery, then chooses a fitting grid.

## Showcases

Four concept images guided by this skill: typography, a product close-up, an information grid, and an energy-dispatch poster. The first three are generic fictional concepts. The fourth has been anonymized to remove personal, team, company, brand, and event names. Images do not represent real product specifications, application screenshots, or measured results.

![Typography-led concept poster](docs/showcases/01-typography.png)

| Product study | Information grid |
| --- | --- |
| ![Product close-up concept](docs/showcases/02-product-study.png) | ![Information grid concept](docs/showcases/03-information-grid.png) |

**Energy-dispatch concept poster**

<p align="center">
  <img src="docs/showcases/04-energy-dispatch.png" width="560" alt="Anonymized energy-dispatch concept poster">
</p>

[View the generation prompts](docs/showcases/prompts.md)

## Install

Download or clone this repository, then run PowerShell 7 from its root:

```powershell
pwsh -File .\scripts\install.ps1
```

The installer copies `SKILL.md`, `agents`, `assets`, `references`, `LICENSE`, and `NOTICE.md` into your local skills directory. It uses `CODEX_HOME` when set, otherwise `.codex/skills` under your user profile. It stops if a directory named `bento-design` already exists and will not overwrite it. Start a new conversation and invoke `$bento-design`; reopen the client if its skill list has not refreshed.

Choose a custom skills directory with:

```powershell
pwsh -File .\scripts\install.ps1 -SkillsDirectory 'D:\MySkills'
```

Before upgrading, move the old version outside your skills search directory as a backup. Do not keep two copies with the same skill name in a skills search directory.

## Use

```text
Use $bento-design to create a 3:4 poster from these six product features.
Choose one core message, then define type hierarchy, semantic line breaks, card roles, and gradient scope.
Preserve the supplied facts and clearly mark missing assets.
```

```text
Use $bento-design to redesign this page's feature section.
Use a typography-led main card and one dark card. Preserve existing copy and interactions, and adapt the layout for mobile.
```

```text
Use $bento-design to propose a 16:9 presentation page layout without writing code.
Explain the core message, type hierarchy, image placement, and missing assets.
```

## Files

- [SKILL.md](SKILL.md): workflow and review criteria.
- [Typography, proportions, and color](references/typography-color.md): type roles, line breaks, and gradients.
- [Reference measurement register](references/reference-measurements.md): type sizes, tracking and paragraph spacing, color values, card gaps, and corner ratios from 19 study screenshots. Source annotations, calculations, and implementation suggestions are distinguished.
- [Layout recipes](references/layout-recipes.md): layout directions and web examples.
- [Image direction](references/image-direction.md): prompt structure and targeted revisions.
- [tokens.css](assets/tokens.css): optional, locally scoped web styles.

The instructions are written in Chinese; the requested design language, brand, stack, and medium remain up to the user. This skill does not include an image model, design application, or export engine. The screenshot values are tutorial examples, not official brand specifications. Generative images cannot guarantee exact type sizes, tracking, or corner radii.

## Check

```powershell
python -X utf8 .\scripts\validate.py
```

The script checks file structure, UTF-8, local links, and diagram structure; it does not replace visual review. The installer requires PowerShell 7. The validator uses the Python 3.10+ standard library. Normal skill use does not require running these scripts.

## License and assets

[MIT License](LICENSE). See [NOTICE.md](NOTICE.md) for asset notes. This is an independent project with no claimed official brand affiliation.
