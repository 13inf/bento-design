"""Validate this repository's structure and self-contained release assets.

Standard library only; this does not validate visual quality or arbitrary YAML.
"""

from pathlib import Path
import re
import struct
import sys
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    '.gitignore', 'LICENSE', 'NOTICE.md', 'README.md', 'SKILL.md',
    'agents/openai.yaml', 'assets/tokens.css',
    'references/typography-color.md', 'references/layout-recipes.md',
    'references/reference-measurements.md',
    'references/image-direction.md', 'docs/preview.svg', 'docs/preview.png',
    'docs/showcases/01-typography.png', 'docs/showcases/02-product-study.png',
    'docs/showcases/03-information-grid.png', 'docs/showcases/prompts.md',
    'docs/showcases/04-energy-dispatch.png',
    'scripts/install.ps1', 'scripts/validate.py',
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    files = {
        path.relative_to(ROOT).as_posix(): path
        for path in ROOT.rglob('*')
        if path.is_file()
        and '.git' not in path.relative_to(ROOT).parts
        and '__pycache__' not in path.relative_to(ROOT).parts
    }
    require(set(files) == EXPECTED,
            f'Unexpected/missing files: extra={sorted(set(files) - EXPECTED)}, '
            f'missing={sorted(EXPECTED - set(files))}')
    link_count = 0
    for name, path in files.items():
        require(path.resolve().is_relative_to(ROOT), f'External file: {name}')
        if path.suffix != '.png':
            content = path.read_text(encoding='utf-8')
            require(not content.startswith('\ufeff'), f'UTF-8 BOM: {name}')
        if path.suffix == '.md':
            targets = re.findall(r'\[[^\]]*\]\(([^)]+)\)', content)
            targets.extend(re.findall(r'(?:src|href)="([^"]+)"', content))
            for target in targets:
                if '://' in target or target.startswith('#'):
                    continue
                local = (path.parent / target.split('#')[0]).resolve()
                require(local.is_relative_to(ROOT), f'External link: {name}: {target}')
                require(local.is_file(), f'Broken link: {name}: {target}')
                link_count += 1

    entry = files['SKILL.md'].read_text(encoding='utf-8')
    frontmatter = entry.split('---', 2)
    require(len(frontmatter) == 3 and not frontmatter[0].strip(), 'Missing frontmatter')
    require(re.search(r'(?m)^name:\s*bento-design\s*$', frontmatter[1]), 'Wrong skill name')
    require(re.search(r'(?m)^description:\s*\S.+$', frontmatter[1]), 'Missing description')
    require('$bento-design' in entry, 'Missing invocation example')
    metadata = files['agents/openai.yaml'].read_text(encoding='utf-8')
    prompt = re.search(r'(?m)^  default_prompt: "(.+)"$', metadata)
    require(prompt and '$bento-design' in prompt.group(1), 'Wrong UI invocation')
    short = re.search(r'(?m)^  short_description: "(.+)"$', metadata)
    require(short and 25 <= len(short.group(1)) <= 64, 'Wrong UI description length')

    svg = ET.parse(files['docs/preview.svg']).getroot()
    for element in svg.iter():
        tag = element.tag.split('}')[-1]
        require(tag not in {'image', 'script', 'foreignObject'}, f'Unexpected SVG node: {tag}')
        for attr in element.attrib:
            require(attr.split('}')[-1] != 'href', 'SVG must not load external resources')
    for name, path in files.items():
        if path.suffix != '.png':
            continue
        png = path.read_bytes()
        require(len(png) >= 24 and png[:8] == b'\x89PNG\r\n\x1a\n'
                and png[12:16] == b'IHDR', f'Invalid PNG header: {name}')
        width, height = struct.unpack('>II', png[16:24])
        if name == 'docs/preview.png':
            require((width, height) == (1280, 1560), f'Unexpected preview size: {width}x{height}')
        elif name == 'docs/showcases/04-energy-dispatch.png':
            require(width >= 600 and height > width,
                    f'Invalid poster dimensions: {name}: {width}x{height}')
        else:
            require(width >= 800 and height >= 450 and width > height,
                    f'Invalid showcase dimensions: {name}: {width}x{height}')
    require('MIT License' in files['LICENSE'].read_text(encoding='utf-8'), 'Missing MIT license')
    print(f'PASS: {len(files)} release files; {link_count} local links; '
          'skill identity, metadata, original SVG and preview/showcase headers verified.')
    print('Visual quality and external asset rights require separate review.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, ET.ParseError, UnicodeError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        sys.exit(1)
