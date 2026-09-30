# Troubleshooting

## Errors from tools

| Code | Meaning | Fix |
|---|---|---|
| `invalid_config` | A field has the wrong type or value, an input could not be fetched, an `@handle` did not resolve, or a model rule was broken. The message names it. | Read `get_model` again and fix the field. Submit with a new idempotency key. |
| `insufficient_gems` | The balance is below the price (`gems_required`). | Tell the user; Gems are added at https://www.mage.space/api?tab=billing. |
| `content_blocked` | Blocked by Mage's content policy, or by the model's lab. | Don't retry the same prompt. Rephrase only if the request is legitimate. |
| `too_many_requests` | The account already has 20 generations in flight. | Wait for some to finish, then submit again. |
| `architecture_retired` | The model was retired. | Pick another from `list_models`. |
| `generation_failed` | The run produced no output; the Gems are refunded. | Retry once with a new key. If it fails again, change the prompt or model. |
| `internal_error` | Mage failed. | Retry with backoff, same key if no response arrived. |

A code you don't know: treat it by what the message says, and don't loop.

## Requests

- **Still `queued` or `in_progress`:** keep calling `get_request` with `wait_seconds: 120`. Long 1080p videos can take several minutes.
- **The response to `generate` never arrived:** call it again with the same `idempotency_key`. It returns the original request and charges nothing twice.
- **Stop a run:** `cancel_request`. Gems are not refunded.
- **Find an earlier generation:** `list_history` (last 30 days, including ones made in the Mage app). Saved creations are in `search_creations`.

## Inputs

- **"input could not be fetched":** the link is a web page, private, or needs a login. Ask for a direct link to the file (it should end in `.jpg`, `.png`, `.mp4`, …) or upload it.
- **A file the user attached in the chat:** Mage cannot see it. Ask for a link, or upload it from disk with `create_upload` if you can run commands.
- **Too many images:** characters, references, and images share `max_images`. Drop one.

## Results

- **Wrong text in an image:** switch to GPT Image 2.5 Flare, quote the text exactly, and keep each line short.
- **The subject changed during an edit:** say what must stay the same ("keep the face, pose, and clothing unchanged") and describe only the change.
- **A character doesn't look like the reference:** save them with `mage-characters` and mention `@handle`, or pass the portrait in `image` and say "the person from @image1".
- **Video too static:** describe camera movement and one clear action. **Too chaotic:** fewer actions, a static camera.
