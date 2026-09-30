# Mage Skills

> **Beta.** These skills are at 0.x: names and behavior may change until 1.0.

[Agent skills](https://agentskills.io) that teach Claude, Codex, Cursor, and other agents to do real creative jobs with [Mage](https://www.mage.space)'s image, video, and audio models: product photoshoots, marketplace listings, ad variants, UGC and faceless videos, YouTube thumbnails, and more. The skills drive the [Mage connector](https://www.mage.space/mcp) (an MCP server), and every generation is paid in Gems from your Mage account.

Browse every skill with examples at [mage.space/skills](https://www.mage.space/skills).

## Install

Two steps: connect Mage, then add the skills.

### 1. Connect Mage

| Agent | How |
|---|---|
| Claude | Customize → Connectors → Add custom connector, URL `https://mcp.mage.space/mcp`, then sign in to Mage |
| Claude Code | `claude mcp add --transport http mage https://mcp.mage.space/mcp`, then `/mcp` to sign in |
| ChatGPT, Grok, Cursor, and others | [mage.space/mcp](https://www.mage.space/mcp) |

### 2. Add the skills

```bash
npx skills add mage-space/skills
```

Works with Claude Code, Codex, Cursor, and any agent that loads `SKILL.md` skills. Other ways, including the Claude Code plugin and claude.ai uploads, are in [INSTALL.md](./INSTALL.md). Agents can install themselves with [INSTALL_FOR_AGENTS.md](./INSTALL_FOR_AGENTS.md).

## Skills

| Skill | Invoke | What it does |
|---|---|---|
| [`mage-generate`](./mage-generate) | `/mage-generate` | Images, video, and audio on the right Mage model, priced before it runs. Defaults: Mango 3, Cherry 2 Pro, Seed Audio. |
| [`mage-characters`](./mage-characters) | `/mage-characters` | Save a person, mascot, outfit, place, or voice once and keep it consistent everywhere with `@handle`. |
| [`mage-product-photoshoot`](./mage-product-photoshoot) | `/mage-product-photoshoot` | Ten photography modes from one product photo: studio, lifestyle, hands, Pinterest, hero, carousel, ads, try-on, concept, restyle. |
| [`mage-marketplace-cards`](./mage-marketplace-cards) | `/mage-marketplace-cards` | A compliant white-background main image, secondary images, and A+ modules for Amazon and other marketplaces. |
| [`mage-ad-multiplier`](./mage-ad-multiplier) | `/mage-ad-multiplier` | One ad into many test variants: talent, wardrobe, setting, color, season, or headline, everything else locked. |
| [`mage-ad-resizer`](./mage-ad-resizer) | `/mage-ad-resizer` | Recompose a static ad for feed, Stories, Reels, banners, and Pinterest without losing a word. |
| [`mage-ad-localizer`](./mage-ad-localizer) | `/mage-ad-localizer` | Native-sounding versions of a static ad in other languages, same layout and offer. |
| [`mage-ugc-video`](./mage-ugc-video) | `/mage-ugc-video` | Creator-style product videos: review, unboxing, how-to, try-on, routine, problem–solution. |
| [`mage-faceless-video`](./mage-faceless-video) | `/mage-faceless-video` | Narrated videos with no one on camera, in ten illustrated styles, researched and scripted. |
| [`mage-youtube-thumbnail`](./mage-youtube-thumbnail) | `/mage-youtube-thumbnail` | Truthful, high-click thumbnails and covers with faces kept exact, variants, and surgical edits. |

In Claude Code with the plugin, skills are namespaced: `/mage:mage-generate`.

The skills chain: save a character with `mage-characters` and use its `@handle` everywhere; shoot a product with `mage-product-photoshoot`, then turn the winner into a listing (`mage-marketplace-cards`) or a video (`mage-ugc-video`); make an ad, then multiply, resize, and localize it. Recipes: [COOKBOOK.md](./COOKBOOK.md).

## How they work

Each skill is a folder with a `SKILL.md` (when to use it, the workflow, the UX rules) and `references/` the agent reads only when it needs them (prompt recipes, platform rules). Skills never talk to Mage directly: they call the connector's tools (`list_models`, `get_model`, `estimate_cost`, `generate`, `get_request`, `create_upload`, the character and reference tools), so pricing, moderation, and billing are the same as in the Mage app and the [API](https://docs.mage.space/api/overview).

- **You approve the spend.** Skills quote the price in Gems and wait for a yes before a batch or a video.
- **Your files:** skills take https links to images and video. Agents that run commands can upload local files. Files attached to a chat can't reach Mage.
- **Results** are links that last 30 days. Download what you want to keep, or save it in Mage.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

MIT. See [LICENSE](./LICENSE). Some skills are adapted from [higgsfield-ai/skills](https://github.com/higgsfield-ai/skills) (MIT).
