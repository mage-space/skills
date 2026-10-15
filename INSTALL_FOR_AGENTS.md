# Install for agents

You are an AI agent. The user asked you to install the Mage skills. Follow these steps exactly.

## Step 1: install the skills

**Claude Code:** install the plugin. It includes every skill and the Mage connector:

```bash
claude plugin marketplace add mage-space/skills
claude plugin install mage@mage
```

Then ask the user to run `/reload-plugins` (or restart Claude Code) and tell you when it's done, and continue with step 2.

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

## Step 2: connect Mage and sign in

- **Claude Code with the plugin:** the plugin already added the Mage server. Ask the user to run `/mcp`, select the Mage server, and sign in with their Mage account. If they added `mage` by hand before, Claude Code keeps that entry instead of the plugin's; sign in there. Wait for them to confirm.
- **Other agents:** if the Mage tools (`list_models`, `generate`, `get_request`) aren't available, ask the user to add the MCP server `https://mcp.mage.space/mcp` in your settings and sign in, following https://www.mage.space/mcp. In Claude Code without the plugin, run `claude mcp add --transport http mage https://mcp.mage.space/mcp` and have them sign in through `/mcp`. Wait for them to confirm.

## Step 3: verify

Call `list_models` once. It should list Mango, Cherry, and Seed Audio. Don't generate anything: generations cost Gems.

Seeing the Mage tools doesn't mean the user is signed in: they stay listed after a sign-in expires. If `list_models` fails with 401 or asks to sign in, ask the user to run `/mcp` (or open your MCP settings), select the Mage server, and sign in again, then call `list_models` again. Don't reinstall anything.

## Step 4: done

Tell the user: "Mage skills installed. Try a product photoshoot, marketplace listing images, ad variants, a UGC or faceless video, or a YouTube thumbnail." Don't explain skill paths or internals.
