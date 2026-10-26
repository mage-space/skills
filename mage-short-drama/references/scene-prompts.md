# Scene prompts: Cherry 2 Pro and Lemon

What a drama scene needs from each video model's prompt syntax. `get_model` has the current fields, options and limits.

## How Mage numbers what you send

Images reach the model as one numbered list: your own `image` and `additional_images` first, then each mentioned character in order of first mention, then each mentioned reference (location, outfit, pose, object) in order of first mention. Mage rewrites each mention before the model reads it:

| You write | The model reads |
|---|---|
| `@image1` | `image 1` (your own inputs, in order) |
| `@nora` (a character) | `character from image N` |
| `@nora` (a character with a saved voice) | `character from image N with voice from [Audio M]` |
| `@diner` (a saved location) | `location from image N` |
| `@narrator` (a saved audio clip) | `[Audio M]` |

- A mention is replaced wherever it appears, with the long phrase each time. Mention each handle once, bound to the character's name (`NORA is @nora`), and use the name afterwards.
- Mention characters in the order they first appear on screen: a mismatched order is the usual cause of swapped faces and voices.
- Any `@` followed by letters is read as a handle; one that matches nothing is refused before anything is charged. Never write an email address or a social handle with its `@` in a line.
- Never write duration, resolution, aspect ratio or "with sound" in the prompt: they are fields.

## Cherry 2 Pro (`cherry`, `cherry-2-pro`)

- **Length and size:** 4, 5, 8, 10, 15, 20, 25 or 30 seconds; 480p, 720p or 1080p; 16:9, 9:16 or 1:1. Up to 29 images (your images, characters and references together).
- **Voices:** 3 audio slots per clip, audio references first, then the voices of mentioned characters. So at most three speaking characters in one Cherry scene. The clips share a 30-second audio budget, cut from each clip's start: a voice clip must start speaking at once.
- **Shots:** `Shot N:` paragraphs, one camera move each; budget one shot per 3 to 6 seconds. In a drama, leave the seconds in your shot list and out of the prompt.
- **Each shot:** shot size, camera position and move; the action as a chain with hand states; the speaker, delivery and exact line; and an end state ("End with the envelope back under ELI's hand").
- **Dialogue:** lines in `{}`, with the language and delivery before them: `NORA says flatly, in English: {He had twenty years to give me something.}` One spoken language per clip apart from names. Never repeat or annotate the words after a line: it summons subtitles.
- **Listeners** "keep their mouths naturally closed". A shot without speech: "No dialogue."
- **Sound:** sound effects follow the actions; for no score, write "No music or score; only ambient and action sounds." If music still appears, name it every way (music, background music, BGM, score, melody) at the start and the end.
- **Emotion as visible behavior:** sad = head lowered, shoulders trembling, tears welling; anxious = checking a watch, darting eyes; angry = fists clenched, jaw tight; relieved = long exhale, shoulders dropping, faint smile. Two or three cues, in plain words: extreme words ("utterly shocked") can give glowing eyes; if they appear, add "normal human eyes, no glowing eyes".
- **Space:** place people against fixed things (the counter, the door, the window) and keep the camera on one side of a conversation.
- **No quality or negative packs** the user did not ask for; an Avoid line names only what must not appear (extra people, an unscripted line, a second prop).
- **A storyboard grid** guides the plot loosely: give its reading order, say it is for shot order and rough framing only, and still write every shot in text.
- **From an approved still:** pass it as `image` and write `Use @image1 as the first frame.` as its own sentence, then one sentence on what that frame shows.
- **Editing a finished scene** (a look-only fix): the clip in `videos`, called `video 1` in the prompt (never `@video1`). The output keeps its length and ratio. Name only what changes and say everything else in `video 1` stays. Send `keep_original_audio: true` so the dialogue and room sound survive; it also avoids moderation false flags caused by the clip's audio.
- **Avoid:** two camera moves in one shot; `image 2 runs…` (a number followed by a verb reads as a count; write the name); names written as text on a reference image; high-resolution references on grass and foliage (they leave a fingerprint texture: downscale them to the output size); burned-in subtitles in any reference.

## Lemon (`lemon`)

- **Length and size:** 2 to 30 seconds; 480p, 720p or 1080p; 16:9, 4:3, 1:1, 3:4 or 9:16. Up to 10 images and 5 audio slots (voice clips first, then characters' voices).
- **Two modes, never mixed:** references (`image`, `additional_images`, `@handles`, voices) or frames (`first_image`, `last_image`, no handles at all: a mention in frame mode is refused). In frame mode, describe people by what the frame shows.
- **Asset lines**, one per asset, saying what it lends: `NORA is @nora, adopting her face, hairstyle and voice.` `The scene follows @diner, adopting its layout and light; ignore any people in it.`
- **Several people:** a `Subject locking:` line mapping every name to its asset, then "NORA and ELI are two different people and must not look alike; each look stays locked to its own reference."
- **Shots** tile the duration end to end with time ranges, 2 to 5 seconds each: `Shot 1 [0-4s]: …`, `Shot 2 [4-7s]: …`. Pick one format and keep it.
- **One take:** start with `Generate single shot.`, or Lemon may cut on its own.
- **Dialogue:** `NORA says: "..."`, one line per speaker, named every time; add `Lip sync` after a line for a tight mouth match. About 2.5 spoken words a second.
- **Silence is explicit:** without `No dialogue.` Lemon may add speech; without "No background music" it may add a score.
- **A negative list** at the end, only of what must not appear: `Negative prompt list: No subtitles, no watermark, no extra characters, no face distortion, no costume changes.`
- `prompt_extend` stays off (the default) when you wrote the prompt.
- If a result comes back as a still image instead of a clip, Lemon's own filter stopped the prompt or an input: reword plainly or replace the input.
