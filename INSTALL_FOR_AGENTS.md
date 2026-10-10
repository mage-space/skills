# Install for agents

You are an AI agent. The user asked you to install the Mage skills. Follow these steps exactly.

## Step 1: check the Mage connector

Look for the Mage tools (`list_models`, `generate`, `get_request`). If they're available, go to step 2.

Otherwise connect Mage:

- **Claude Code:** skip this; the plugin in step 2 connects Mage. Once it's installed and Claude Code has restarted, ask the user to run `/mcp`, select the Mage server, and sign in. Without the plugin, run `claude mcp add --transport http mage https://mcp.mage.space/mcp`, then ask the user to run `/mcp`, select mage, and sign in with their Mage account. Wait for them to confirm.
- **Other agents:** ask the user to add the MCP server `https://mcp.mage.space/mcp` in your settings and sign in, following https://www.mage.space/mcp. Wait for them to confirm.

## Step 2: install the skills

**Claude Code:** install the plugin, then ask the user to restart Claude Code:

```bash
claude plugin marketplace add mage-space/skills
claude plugin install mage@mage
```

**Any other agent with Node.js:**

```bash
npx skills add mage-space/skills
```

**No Node.js:** clone the repository anywhere and run the setup script:

```bash
git clone --depth 1 https://github.com/mage-space/skills.git mage-skills
cd mage-skills && ./setup
```

Do not clone the repository into a skills folder directly (for example `~/.claude/skills/mage-skills`): agents look for each skill one level down and would find none.

## Step 3: verify

Call `list_models` once. It should list Mango, Cherry, and Seed Audio. Don't generate anything: generations cost Gems.

If a tool call fails with 401 or asks to sign in, repeat step 1.

## Step 4: done

Tell the user: "Mage skills installed. Try a product photoshoot, marketplace listing images, ad variants, a UGC or faceless video, or a YouTube thumbnail." Don't explain skill paths or internals.
