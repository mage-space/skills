# Contributing

Thanks for helping improve the Mage skills. Bug reports, new recipes, and pull requests are welcome.

## Development

Skills are Markdown. The only tooling is the validator, which needs Python 3 and PyYAML:

```bash
pip install pyyaml
python3 scripts/validate.py
```

CI runs it on every pull request. Test a changed skill by installing your checkout (`./setup`) and running a real request through an agent with the Mage connector; generations cost Gems, so use cheap models (Mango 3 Turbo, GPT Image 2.5 Flare, Cherry Mini) while iterating.

Use [Conventional Commits](https://www.conventionalcommits.org/) for commit messages and pull request titles (`feat(product-photoshoot): add a seasonal mode`, `fix(generate): …`, `docs: …`); releases and the changelog are built from them. Pull requests are squash-merged.

## Pull request checklist

1. **Frontmatter is valid.** Only the [spec's](https://agentskills.io/specification) fields (`name`, `description`, `license`, `compatibility`, `metadata`); `name` matches the folder; the description says what the skill does, has `Use when:` triggers and a `NOT for:` boundary naming the skill to use instead, and stays under 1024 characters. Don't add a top-level `version`: claude.ai rejects unknown fields. The version lives in `metadata.version` and is set by releases.
2. **References resolve.** Every `references/*.md` a `SKILL.md` mentions exists, every reference file is mentioned, and nothing points outside the skill's folder (`../`). Each skill installs on its own.
3. **Tools are real.** Every tool, field, model id, and option is one the Mage connector has today (`list_models`, `get_model`). Use Mage's model names (Mango, Cherry, Guava, Lemon, Seed Audio, GPT Image 2.5 Flare) and never name the lab or upstream model behind one.
4. **UX rules stay as strict.** Quote the price before a batch or a video, never invent product facts or claims, never pass chat attachments as if Mage could read them, no raw ids or JSON in replies.
5. **Behavior change, docs change.** An agent reading only `SKILL.md` must be able to do the job; recipes and tables live in `references/`.

## Adding a skill

Create `mage-<name>/SKILL.md` following the existing ones:

```yaml
---
name: mage-<name>
description: |
  <What it does and which Mage models it uses.>
  Use when: "<trigger>", "<trigger>", ...
  NOT for: <case> (use <skill>), <case> (use <skill>).
license: MIT
compatibility: Requires the Mage connector (https://mcp.mage.space/mcp) and a Mage account with Gems.
metadata:
  author: mage-space
  version: "<current VERSION>" # x-release-please-version
---
```

Then add the folder to `.claude-plugin/marketplace.json`, `release-please-config.json` (`extra-files`), and the tables in `README.md`, and run the validator. Keep `SKILL.md` under 300 lines: if removing a section wouldn't stop the agent deciding what to do next, it belongs in `references/`.

## Releases

[release-please](https://github.com/googleapis/release-please) keeps a release pull request open with the next version and changelog. Merging it tags the release and bumps `VERSION`, every plugin manifest, and every skill's `metadata.version` together. Before 1.0, a breaking change bumps the minor version and anything else the patch version.

## Maintainer setup

- **GitHub App** installed on this repository with read and write access to contents and pull requests. Its id goes in the `MAGE_BOT_APP_ID` variable and its private key in the `MAGE_BOT_PRIVATE_KEY` secret; the release workflow uses its token so CI runs on the release pull request. The workflow stays idle until the variable is set.
- **Repository settings:** squash merging only; protect `main` with the `Validate skills` check required.

## License

By contributing, you agree your contribution is licensed under MIT.
