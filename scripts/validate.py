#!/usr/bin/env python3
"""Validate every skill in this repository.

Checks, per the Agent Skills specification (https://agentskills.io/specification)
and this repository's conventions:

- SKILL.md frontmatter uses only the allowed fields; `name` matches its folder and
  the naming rules; `description` is at most 1024 characters and names its
  "Use when" triggers and its "NOT for" boundary; `metadata.version` matches VERSION.
- SKILL.md stays under 500 lines.
- Every plugin manifest carries the VERSION, and the Claude Code marketplace and
  plugin manifest list every skill folder.
- Every `references/*.md` a SKILL.md mentions exists, every reference file is
  mentioned by its SKILL.md, and no skill reaches outside its own folder.

Run it from the repository root: `python3 scripts/validate.py`. Needs PyYAML.
"""

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ALLOWED_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MANIFESTS = {
    ".claude-plugin/plugin.json": ["version"],
    ".claude-plugin/marketplace.json": ["plugins", 0, "version"],
    ".codex-plugin/plugin.json": ["version"],
    ".cursor-plugin/plugin.json": ["version"],
}
# Claude Code reads the marketplace entry; hosts that load the plugin directly read plugin.json.
SKILL_LISTS = {
    ".claude-plugin/marketplace.json": ["plugins", 0, "skills"],
    ".claude-plugin/plugin.json": ["skills"],
}


def dig(value, path):
    for key in path:
        value = value[key]
    return value


def check_skill(folder: Path, version: str) -> list[str]:
    errors = []
    skill_md = folder / "SKILL.md"
    if not skill_md.is_file():
        return [f"{folder.name}: SKILL.md is missing"]
    text = skill_md.read_text()
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return [f"{skill_md}: no YAML frontmatter"]
    front = yaml.safe_load(match.group(1))

    unknown = set(front) - ALLOWED_FIELDS
    if unknown:
        errors.append(f"{skill_md}: fields not in the spec: {', '.join(sorted(unknown))}")
    name = front.get("name", "")
    if name != folder.name:
        errors.append(f"{skill_md}: name {name!r} does not match its folder")
    if not NAME_PATTERN.match(name) or len(name) > 64:
        errors.append(f"{skill_md}: name {name!r} breaks the naming rules")
    description = front.get("description", "")
    if not description or len(description) > 1024:
        errors.append(f"{skill_md}: description is empty or over 1024 characters ({len(description)})")
    for phrase in ("Use when", "NOT for"):
        if phrase not in description:
            errors.append(f"{skill_md}: description lacks '{phrase}'")
    if len(front.get("compatibility", "")) > 500:
        errors.append(f"{skill_md}: compatibility is over 500 characters")
    skill_version = (front.get("metadata") or {}).get("version")
    if skill_version != version:
        errors.append(f"{skill_md}: metadata.version {skill_version!r} != VERSION {version!r}")
    lines = text.count("\n")
    if lines > 500:
        errors.append(f"{skill_md}: {lines} lines; move detail into references/")

    mentioned = set(re.findall(r"references/([A-Za-z0-9_.-]+\.md)", text))
    for ref in sorted(mentioned):
        if not (folder / "references" / ref).is_file():
            errors.append(f"{skill_md}: mentions references/{ref}, which does not exist")
    for path in sorted((folder / "references").glob("*.md")):
        if path.name not in mentioned:
            errors.append(f"{path}: not mentioned in {skill_md}, so no agent will read it")

    for path in [skill_md, *sorted(folder.rglob("*.md"))]:
        if re.search(r"(^|[^./])\.\./", path.read_text()):
            errors.append(f"{path}: points outside its skill folder (../)")
    return errors


def main() -> int:
    version = (ROOT / "VERSION").read_text().strip()
    folders = sorted(p for p in ROOT.glob("mage-*") if p.is_dir())
    errors = []
    for folder in folders:
        errors += check_skill(folder, version)

    for manifest, path in MANIFESTS.items():
        found = dig(json.loads((ROOT / manifest).read_text()), path)
        if found != version:
            errors.append(f"{manifest}: version {found!r} != VERSION {version!r}")

    # Cursor scans the named folder's subfolders for SKILL.md; without the field it
    # scans skills/, which this repository doesn't have.
    cursor = json.loads((ROOT / ".cursor-plugin/plugin.json").read_text())
    if cursor.get("skills") != "./":
        errors.append('.cursor-plugin/plugin.json: "skills" must be "./" so Cursor finds every skill')

    for manifest, path in SKILL_LISTS.items():
        listed = {s.removeprefix("./").rstrip("/") for s in dig(json.loads((ROOT / manifest).read_text()), path)}
        for folder in folders:
            if folder.name not in listed:
                errors.append(f"{manifest}: {folder.name} is not listed")
        for name in sorted(listed - {f.name for f in folders}):
            errors.append(f"{manifest}: lists {name}, which does not exist")

    for error in errors:
        print(f"::error::{error}")
    if errors:
        return 1
    print(f"✓ {len(folders)} skills valid at version {version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
