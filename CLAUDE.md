# Mage Skills

Agent skills that drive the Mage connector (the MCP server at `https://mcp.mage.space/mcp`) to make images, video, and audio for real jobs. Public, MIT, and installed with `npx skills add mage-space/skills`.

## Layout

```
mage-<name>/SKILL.md          # one skill: frontmatter, workflow, UX rules
mage-<name>/references/*.md   # read on demand: recipes, rules, prompt templates
.claude-plugin/               # Claude Code marketplace and plugin manifests
.codex-plugin/, .cursor-plugin/
scripts/validate.py           # CI: frontmatter, versions, references, self-containment
setup                         # links skills into ~/.claude, ~/.codex, ~/.cursor
evals/scenarios.md            # prompts that should (and should not) trigger each skill
COOKBOOK.md                   # recipes that chain skills
```

## Rules

- **Tools, not HTTP.** Skills call the connector's tools (`list_models`, `get_model`, `estimate_cost`, `generate`, `get_request`, `create_upload`, the character and reference tools, `list_history`, `search_creations`). Never tell an agent to call `api.mage.space` directly from a skill.
- **Real names only.** Model ids, fields, and options must match what `get_model` returns today. Use Mage's model names; never name the lab or upstream model behind one.
- **Money is explicit.** Every skill quotes Gems with `estimate_cost` and waits for a yes before a batch or a video.
- **Inputs are links.** Chat attachments never reach Mage. Skills ask for https links, or upload from disk with `create_upload` when the agent has a shell.
- **Truthful output.** No invented product facts, claims, reviews, quotes, or research.
- **Self-contained skills.** No `../` paths; each skill installs alone. Duplicate small shared sections (connector setup, tool loop) instead of sharing files.
- **Frontmatter per spec.** `name`, `description` (with `Use when:` and `NOT for:`), `license`, `compatibility`, `metadata.version`. A top-level `version` breaks claude.ai uploads.
- **Small SKILL.md.** Under 300 lines; move recipes and tables to `references/`, and mention every reference file in its `SKILL.md`.

## Versions

`VERSION` is the source of truth; `metadata.version` in every `SKILL.md` and the four plugin manifests must match. release-please bumps them all; don't edit versions by hand. `python3 scripts/validate.py` checks everything CI checks.

## Where skills show up

Each skill has a page at `https://www.mage.space/skills/<slug>` and a card on `https://www.mage.space/mcp`, built from the Mage web app's skills catalog. When you add, rename, or remove a skill, that catalog needs the same change.
