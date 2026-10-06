# Mage Skills

> **Beta.** These skills are at 0.x: names and behavior may change until 1.0.

[Agent skills](https://agentskills.io) that teach Claude, Codex, Cursor, and other agents to do real creative jobs with [Mage](https://www.mage.space)'s image, video, and audio models: product photoshoots, marketplace listings, ad variants, UGC and faceless videos, YouTube thumbnails, and the Mage apps (swaps, inpaint, relight, lip sync, video edits, and more). The skills drive the [Mage connector](https://www.mage.space/mcp) (an MCP server), and every generation is paid in Gems from your Mage account.

Browse every skill with examples at [mage.space/skills](https://www.mage.space/skills).

## Install

Two steps: connect Mage, then add the skills.

### Plugin connection

The plugin manifest includes all 27 skills and the production Mage MCP server. Compatible plugin hosts, including Claude Code and Grok Build, discover the connection automatically and ask you to sign in to Mage through OAuth. Installing this source does not mean it is listed or approved in a platform’s public directory.

The connector calls `https://mcp.mage.space/mcp`, with sign-in and OAuth token handling at `https://www.mage.space`. It accesses the connected account’s balance, media history, saved creations, characters, and references; it can generate media, manage characters and references, upload files, and cancel requests. Generations spend Gems. It requests no local shell server, lifecycle hooks, or stored API keys. Disconnect it in [Mage’s connected apps](https://www.mage.space/mcp?tab=connected).

Publisher: Ollano Inc. Support: [mage@mage.space](mailto:mage@mage.space). [Privacy policy](https://www.mage.space/privacy-policy) · [Terms](https://www.mage.space/terms-and-conditions).

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

### Mage apps as skills

Each of these is one of the [apps on mage.space](https://www.mage.space/apps) as a skill: the same prompt, models, and defaults, run through the connector.

| Skill | Invoke | What it does |
|---|---|---|
| [`mage-face-swap`](./mage-face-swap) | `/mage-face-swap` | Put a face from one image onto the person in another, keeping the pose, clothes, and scene. |
| [`mage-character-swap`](./mage-character-swap) | `/mage-character-swap` | Replace the whole person in an image with another character, keeping the scene and pose. |
| [`mage-outfit-swap`](./mage-outfit-swap) | `/mage-outfit-swap` | Dress the person in one image in the outfit from another, keeping the person and scene. |
| [`mage-inpaint`](./mage-inpaint) | `/mage-inpaint` | Mark one region of an image and change only that: remove, replace, fix, or add. |
| [`mage-refine`](./mage-refine) | `/mage-refine` | One focused improvement to an image: fix eyes, fix hands, add detail, or your own instruction. |
| [`mage-relight`](./mage-relight) | `/mage-relight` | Relight a photo: direction, soft or hard, brightness, and color, with the content unchanged. |
| [`mage-angles`](./mage-angles) | `/mage-angles` | The same image from a new camera angle: side, three-quarter, behind, high, low, or overhead. |
| [`mage-character-builder`](./mage-character-builder) | `/mage-character-builder` | Design a new character from traits (hair, eyes, build, age, style) and save it with an `@handle`. |
| [`mage-character-muse`](./mage-character-muse) | `/mage-character-muse` | Refine a character from a starter image with nine face presets or plain words, then save it. |
| [`mage-character-sheet`](./mage-character-sheet) | `/mage-character-sheet` | One character image into a full reference sheet: face close-up, four body views, details. |
| [`mage-recreate`](./mage-recreate) | `/mage-recreate` | Read a reference image into a detailed prompt, then generate new images in that look. |
| [`mage-video-editor`](./mage-video-editor) | `/mage-video-editor` | Edit a video with a prompt and optional reference images, keeping its motion and framing. |
| [`mage-video-face-swap`](./mage-video-face-swap) | `/mage-video-face-swap` | Swap a face into a video, keeping the pose, motion, expressions, and lip movements. |
| [`mage-video-character-swap`](./mage-video-character-swap) | `/mage-video-character-swap` | Replace the whole person in a video, body and outfit included, keeping the motion and scene. |
| [`mage-lipsync`](./mage-lipsync) | `/mage-lipsync` | Make the subject of one image speak an audio clip of up to 15 seconds. |
| [`mage-music-video`](./mage-music-video) | `/mage-music-video` | One to three saved characters singing and dancing to a track of up to 15 seconds. |
| [`mage-scene-builder`](./mage-scene-builder) | `/mage-scene-builder` | A video scene with two characters, from nine multi-shot presets or your own prompt. |

In Claude Code with the plugin, skills are namespaced: `/mage:mage-generate`.

The skills chain: save a character with `mage-characters` and use its `@handle` everywhere; shoot a product with `mage-product-photoshoot`, then turn the winner into a listing (`mage-marketplace-cards`) or a video (`mage-ugc-video`); make an ad, then multiply, resize, and localize it; build a character with `mage-character-builder`, give it a sheet with `mage-character-sheet`, then put it in a scene (`mage-scene-builder`) or make it talk (`mage-lipsync`). Recipes: [COOKBOOK.md](./COOKBOOK.md).

## How they work

Each skill is a folder with a `SKILL.md` (when to use it, the workflow, the UX rules) and `references/` the agent reads only when it needs them (prompt recipes, platform rules). Skills never talk to Mage directly: they call the connector's tools (`list_models`, `get_model`, `estimate_cost`, `generate`, `get_request`, `create_upload`, the character and reference tools), so pricing, moderation, and billing are the same as in the Mage app and the [API](https://docs.mage.space/api/overview).

- **You approve the spend.** Skills quote the price in Gems and wait for a yes before a batch or a video.
- **Your files:** skills take https links to images and video. Agents that run commands can upload local files. Files attached to a chat can't reach Mage.
- **Results** are links that last 30 days. Download what you want to keep, or save it in Mage.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

MIT. See [LICENSE](./LICENSE). Some skills are adapted from [higgsfield-ai/skills](https://github.com/higgsfield-ai/skills) (MIT).
