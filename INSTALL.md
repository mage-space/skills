# Install Mage Skills

Ten skills ship in this repository: `mage-generate`, `mage-characters`, `mage-product-photoshoot`, `mage-marketplace-cards`, `mage-ad-multiplier`, `mage-ad-resizer`, `mage-ad-localizer`, `mage-ugc-video`, `mage-faceless-video`, and `mage-youtube-thumbnail`.

Every skill needs two things: the **Mage connector** in your agent, and the **skill files**.

## Step 1: connect Mage

The connector is Mage's MCP server at `https://mcp.mage.space/mcp`. You sign in with your Mage account; generations are paid from its Gems.

| Agent | How |
|---|---|
| Claude (web, desktop) | Customize → Connectors → Add custom connector. Name it Mage, URL `https://mcp.mage.space/mcp`, then sign in. In a chat, turn Mage on from the **+** menu. |
| Claude Code | `claude mcp add --transport http mage https://mcp.mage.space/mcp`, then run `/mcp`, select mage, and sign in. |
| Codex | Add `https://mcp.mage.space/mcp` as a streamable HTTP MCP server and sign in when prompted. |
| Cursor, ChatGPT, Grok | Follow [mage.space/mcp](https://www.mage.space/mcp). |

## Step 2: add the skills

### Option 1: `npx skills` (recommended, any agent)

```bash
npx skills add mage-space/skills
```

Detects your agent and installs every skill to the right folder. Requires Node.js.

### Option 2: `gh skill install`

GitHub CLI 2.90 or later:

```bash
gh skill install mage-space/skills
```

### Option 3: Claude Code plugin

Inside Claude Code:

```
/plugin marketplace add mage-space/skills
/plugin install mage@mage
```

Skills are then namespaced, for example `/mage:mage-product-photoshoot`.

### Option 4: claude.ai

Zip a skill folder (for example `mage-product-photoshoot/`, with the folder at the zip's root), then upload it in Claude under **Customize → Skills**. Repeat for each skill you want. Skills need code execution turned on, and the Mage connector must be on in the chat.

### Option 5: setup script

Clones the repository and links each skill into your agent's skills folder:

```bash
git clone --depth 1 https://github.com/mage-space/skills.git mage-skills
cd mage-skills
./setup
```

`./setup --host claude|codex|cursor` picks the agent; it detects one otherwise. Safe to run again.

## Verify

Ask your agent:

> Use Mage to make a small test image of a paper boat.

It should quote the price, generate with Mango 3, and give you a link.

## Update

| Method | Update |
|---|---|
| `npx skills` | Run `npx skills add mage-space/skills` again |
| `gh skill install` | `gh skill update mage-space/skills` |
| Claude Code plugin | `/plugin update mage@mage` |
| Setup script | `git pull && ./setup` |
