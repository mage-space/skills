# Cherry (`cherry`)

Mage's flagship video line: cinematic motion with native sound, saved characters with their own voices, scenes built from many references, and edits of a source video. Cherry 2 Pro (`cherry-2-pro`) is the default.

## Variants

| `model_id` | Name | Length | Resolution | Images | Prompt dialect |
|---|---|---|---|---|---|
| `cherry-2-pro` | Cherry 2 Pro | 4–30 s | 480p–1080p | 29 | Cherry 2 Pro rules below |
| `cherry-pro` | Cherry Pro | 4–15 s | 480p–4K | 8 | Classic rules below |
| `cherry` | Cherry | 4–15 s | 480p, 720p | 8 | Classic rules |
| `cherry-mini` | Cherry Mini | 4–15 s | 480p, 720p | 8 | Classic rules |

Where the two dialects differ:

| | Cherry 2 Pro | Cherry, Cherry Pro, Cherry Mini |
|---|---|---|
| Timing within a clip | Whole-second timestamps or `Shot N` | `Shot N` only; second ranges are ignored |
| Closing quality line | Leave it out: no quality or negative words the user did not ask for | Add one short quality and stability line |
| Character images | Multi-view sheets fine for up to 5 subjects | One view per image: a headshot plus a full-body shot. Turnaround sheets make twins |
| Cast size | 1–8 subject references work best; up to 12 is less stable | More than 4 people: group them into images of 4 or fewer on Mango first |
| Naming a character | Bind the name once, then use the name | Repeat the mention with the name in every shot where they act |
| Dialogue | 11 languages natively: English, Chinese, Spanish, Portuguese, Arabic, Indonesian, Malay, Thai, Vietnamese, Japanese, Korean | Name the language for anything but English or Chinese |
| A source video | The output keeps the source's length and aspect ratio | Your `duration` and `aspect_ratio` apply |
| Drafts | Its look differs from the others | A Cherry Mini draft previews motion, blocking and timing, not Cherry 2 Pro's look |

## How Mage sends your prompt

- Fields: `prompt`, `model_id`, `duration`, `resolution`, `aspect_ratio` (16:9, 9:16, 1:1), `image`, `additional_images`, `videos` (one source video), `use_character_voices`. Cherry has no first- or last-frame field: for an exact start and end frame, use Lemon.
- Never write duration, resolution, aspect ratio, frame rate or "with sound" into the prompt. They are fields, and the model reads such words as content.
- Images reach the model as one numbered list: `image`, `additional_images`, then each mentioned character in order of first mention, then each mentioned reference in order of first mention. Mage rewrites the mentions:

| You write | The model reads |
|---|---|
| `@image1` | `image 1` (your own inputs, in order) |
| `@mara` (a character) | `character from image N` |
| `@mara` (a character with a saved voice) | `character from image N with voice from [Audio M]` |
| `@harbor` (a saved location) | `location from image N`; likewise `outfit`, `pose`, `object` |
| `@narrator` (a saved audio clip) | `[Audio M]` |

- Numbered assets are this model's convention: name each by its number and give it one role.
- Audio slots: 3 in all, audio references first (in mention order), then character voices. `use_character_voices: false` leaves the voices out. A request with audio references needs at least one image.
- Audio clips share a fixed time budget, cut from each clip's start: 30 s in total on Cherry 2 Pro, 15 s on the others (5 s each with three clips). A voice clip must start speaking at once.
- There is no `@` handle for video. The source video is `video 1`: write those words plainly. `@video1` is refused.
- Cherry makes sound by default. For a silent clip send `generate_audio: false` (fields `get_model` does not list pass through to the model).
- `keep_original_audio: true` (also passed through) edits a silent copy of the source video and puts the source's own audio back on the result. Use it for visual edits that must keep the original sound; it also avoids moderation false flags caused by the source's audio. With it, no new sound is generated and audio references are dropped.
- There is no negative-prompt field.

## Prompt structure

Write it as a production instruction, not ad copy: which asset is what, what happens in order, how it is shot, what we hear.

### Cherry 2 Pro

A simple clip, four lines:

```
<Subject> <main action or event> in <scene>.
The visuals present <style or mood>.
The camera uses <shot size, position, movement or cuts>.
The sound includes <dialogue, ambience, effects or music>.
```

With references or several beats, use these section labels in the prompt:

```
Goal: Generate <kind of video>. The core subject is <subject>; the principal event is <one-line summary>.
Inputs: One line per asset: <Name> is @handle; use only the face, hairstyle and clothing. @image2 is the café; use only its layout and light, not the people in it.
Positions: Fixed features, who stands where relative to doors and tables, who holds what.
Script: At the start: <state>. Then Shot 1 / Shot 2… or 0-4 seconds / 4-9 seconds… At the end: <final positions, who holds what>.
Keep the same: Identities and count, clothing, prop ownership, directions, which voice belongs to whom.
```

Several shots in one clip:

- Mark beats with `Shot N:` or with continuous whole-second ranges that cover the clip with no gaps ("0-3 seconds… 3-7 seconds… 7-10 seconds…"). Moments work too: "At the 5-second mark…", "After 3 seconds…".
- Budget one beat or shot per 3–5 seconds. Too little content and the model improvises; too much and it adds cuts or skips beats. Never time rapid repeated actions.
- Use second ranges when a beat must land at a moment (an entrance, a handoff, a line on an action); otherwise `Shot N` or stages, and let the `duration` field set the length.
- Each shot: `[shot size, camera position, angle, move]`, the action as a chain with hand states, the exact line in `{}`, and an end state ("End with the dagger flat on the rug, no hand on it").
- One camera move per shot. Name a cut by its trigger: "cut on the word guest", "at the 6-second mark, a whip pan right into the next room".

### Cherry, Cherry Pro, Cherry Mini

Three paragraphs, then one closing line:

1. Setup: each character, the setting and every image's role. Every mention carries a name or noun right next to it (`Mara (@mara)`), never a bare `image 2 walks`.
2. `Shot 1: … Shot 2: … Shot 3: …`, one camera move each, anchoring each acting character with `Name (@handle)` again. No second ranges.
3. Edits only: what changes, where in frame and in which shot.
4. Closing line: "High definition, rich detail, cinematic texture. Faces stay stable without distortion; movement is natural and smooth, with no flicker." With several people add "No two characters share an identical face and outfit."

## Vocabulary

- Shot sizes, moves, angles and named techniques (one-take, dolly zoom, aerial, FPV, bullet time, handheld, speed ramp) work as written. For anything niche, give the term and its visible result: "Rack focus: the foreground leaves blur while the woman behind them comes into sharp focus."
- A move needs its subject and path: move + who it centers on + where it starts + direction + where it arrives.
- Motion, classic variants: body part, range, speed and force ("slowly raises her right hand to shoulder height"); slow, continuous movement beats sprints and flips; say how one action flows into the next. Cherry 2 Pro: describe most action briefly ("they trade blows across the deck") and detail only the one or two moments that matter; never repeat an action.
- Emotion as visible behavior: sad = head lowered, shoulders trembling, tears welling; anxious = checking a watch, tapping, darting eyes; angry = fists clenched, jaw tight, chest heaving; relieved = long exhale, shoulders dropping, faint smile. Pick two or three cues.
- Cherry 2 Pro overreacts to extreme words ("fanatical", "utterly shocked") with glowing eyes: use plain words ("amazed") and, if it happens, add "normal human eyes, no glowing eyes".
- Space: place people against fixed things (door, counter, table, window) and keep the camera on one side of a conversation.
- Style: name it outright ("2D Japanese anime style"). Realistic references drift a stylized clip toward live action; restyle the still on Mango first.
- Products: start state → one operation → a visible result, one per stage.

## References, characters, and frames

- Give every asset exactly one role in words: "use only the face and clothing", "use only the layout and light; do not use the people in it", "use only the camera movement".
- Bind each character by name: `Mara (@mara) …` reads as `Mara (character from image 2 with voice from [Audio 1]) …`. On Cherry 2 Pro bind once and use "Mara" after that; on the classic variants repeat `Mara (@mara)` in each shot she acts in. Give each subject two or three fixed visible features.
- Mention characters in the order they first appear on screen. A mismatched order is the usual cause of swapped faces and voices.
- Send only the images the clip uses. Four or five assets is a strong mix: one or two character images, one scene image, an audio clip. Never write names as text on an image; bind names in the prompt.
- Start from an approved still: pass it as `image` and write `Use @image1 as the first frame.` as its own sentence, then one sentence on what that frame shows. Set `aspect_ratio` to the still's. Never weaken it to "a first-frame composition reference".
- Keyframes (Cherry 2 Pro): first sentence "Use images 1 to 5 in order as keyframes.", then describe the path between them.
- A storyboard sheet (Cherry 2 Pro): one clean line-art image of 15 panels or fewer with little text. It guides the plot loosely: state the reading order and write every shot in text.

### Editing a source video

Cherry 2 Pro takes a 4–30 s source (under 20 s works best) and returns the same length and ratio. The others take 2–15 s. Use an edit verb (edit, add, insert, remove, replace, change to) and write `video 1` itself, never "reference video 1", which turns the edit into a new generation.

```
Edit: Edit video 1, changing only <object or region> to <target>.
Source video: video 1 is the sole editing master and governs the scene, camera, action paths, occlusion and event order.
New material: @image1 is used only for <the target's appearance>; do not use its background.
Scope: Modify only <…>. There is exactly one <target> throughout. Except for the objects explicitly modified above, all other visible characters, props, and background elements in video 1 remain unchanged and are not to be replaced or removed.
Timing: <Target> takes the exact appearance timing, path, speed and occlusion of <original>, which no longer appears. Everything else stays as in video 1.
```

- Partial edits by time (Cherry 2 Pro): "from 4-6 seconds in video 1, change the man's action from drinking coffee to mopping the floor; leave the rest unchanged."
- Audio-only edits keep every visual, the lip sync and the other sounds: "Remove the background music from video 1; keep the dialogue, lip sync, ambience, action sounds and all visuals." "Translate the spoken dialogue in video 1 into Spanish, with no subtitles. Match the lip movements to the new speech and keep everything else unchanged."
- A new length, a new aspect ratio or a continuation is not an edit on Cherry 2 Pro: edits keep the source's length and ratio. Continue from the source's last frame instead (`Use @image1 as the first frame.`) or use Lemon. On the other variants, "Extend video 1 forward: …" continues a clip; chained extensions wear faces down.
- The source's own audio often trips moderation. For a visual edit, send `keep_original_audio: true`; or, when you can run commands, strip the audio with ffmpeg (`ffmpeg -i in.mp4 -an -c:v copy silent.mp4`), upload the silent copy with `create_upload`, and put the sound back afterwards.

## Audio and dialogue

- Symbols: dialogue `{…}`, sound effects `<…>`, music `(…)`. Don't also put names in angle brackets.
- Each line: language, accent only if asked, delivery, speaker, words: `Mara's line (in English, low and steady): {Then we hold the ridge.}` Label every line's speaker. One spoken language per clip apart from names. Add "Use English" when English might come out in another language.
- Don't repeat or annotate words after a line; it summons subtitles. One delivery note per line, in the parentheses.
- Listeners "keep their mouths naturally closed". A shot without speech: "Characters keep their mouths naturally closed; there is no narration; no subtitles or signs appear on screen."
- A voice from an audio clip: describe it in words too ("in the deep, slightly gravelly voice of Audio 1"). The text decides the words; the clip gives timbre, accent, pace and emotion.
- Sound beds (Cherry 2 Pro): "No BGM; only ambient and action sounds." or "No audio." If music still appears, list its names (music, background music, BGM, score, melody) at the start and the end. Water, wave and echo words add ripple or echo artifacts.

## Text in the image

- Short on-screen text: words, time, position, entrance, look: `At the 2-second mark the word "OPEN" fades in at the bottom center in white bold sans-serif.` Subtitles: "Display subtitles at the bottom center, synchronized with the speech."
- Exact logos and labels come from an image of them ("the label exactly as in @image3"). Cherry 2 Pro misspells long words: spell the word letter by letter, appearing in sequence, or supply it as an image.
- With dialogue and no subtitles wanted, write "No subtitles." Exact captions are better added afterwards in an editor.

## Avoid

- Two camera moves in one shot; a whole script pasted in; every asset slot filled.
- Second ranges on Cherry, Cherry Pro or Cherry Mini; quality packs or negatives on Cherry 2 Pro the user did not ask for.
- `image 2 runs toward…`: a number followed by a verb gets read as a count. Write `Mara (@mara) runs toward…`.
- High-resolution AI images as references on Cherry 2 Pro leave fingerprint-like texture on grass and foliage: downscale them to the output resolution. A source or reference video with burned-in subtitles brings them back.

## Examples

Cherry 2 Pro, text only, timed beats (8 s):

```
Realistic nature documentary, natural light. On a warm afternoon on a mossy riverbank, a young otter slides down a muddy chute into the water.
The otter has sleek wet brown fur and quick, playful movements. Ferns and smooth river stones line the bank; tall trees blur softly behind.
0-3 seconds: The otter scrambles to the top of the bank, shakes its head, and flops onto its belly at the start of the chute.
3-8 seconds: It slides down fast, splashes into the river, then surfaces facing the camera and rolls onto its back, paws on its chest.
Low camera at water level with a slight handheld feel, following the otter. Natural sound only: rushing water, the wet slap of the slide, the splash, birdsong.
```

Cherry 2 Pro, two saved characters with voices, three shots (10 s):

```
Goal: Generate a tense dialogue scene in a candlelit tent at night. Hatim offers bread to a guest who hides a dagger.
Inputs: Hatim is @hatim; use only his face, head wrap and cloak. The guest is @guest; use only his face, head wrap and travel cloak.
Positions: Hatim sits on the west side of a low rug, the guest on the east side, a clay plate of bread between them. The camera stays south of them.
Script:
Shot 1: [Medium two-shot from the south, locked off] The guest's right hand rests on a sheathed dagger under his cloak. Hatim tears bread and holds out a piece. Hatim's line (in English, warm): {Eat. You are my guest.}
Shot 2: [Close-up on the guest, slow push in] His eyes move from Hatim's face to the bread. He lets go of the hilt and takes the bread with that same hand. Hatim keeps his mouth naturally closed.
Shot 3: [Medium two-shot from the south, locked off] Both men eat in silence. End with the bread in the guest's hand and the dagger still sheathed.
Keep the same: Two men only, seats unchanged, the dagger stays sheathed. No subtitles. Sound: candle crackle, cloth rustle, wind against the tent.
```

Cherry 2 Pro, replace a moving subject, original sound kept (`videos`: the park clip; `keep_original_audio: true`):

```
Edit: Edit video 1, replacing only the red bicycle and its rider with the dark-gray electric patrol cart from @image1.
Source video: video 1 is the sole editing master and governs the park path, the two people on the bench, the camera, the rider's motion and the event order.
New material: @image1 is used only for the cart's body, color and clear windshield; do not use its background or driver.
Scope: There is exactly one cart throughout. Except for the objects explicitly modified above, all other visible characters, props, and background elements in video 1 remain unchanged and are not to be replaced or removed.
Timing: The cart takes the rider's exact timing, path, speed and occlusion in front of the bench. The bicycle and rider no longer appear.
```

Cherry 2 Pro, from an approved still (`image`: the still; 9:16, 8 s):

```
Use @image1 as the first frame.
It shows Ana (@ana) at a rain-streaked café window at night, cupping a mug in both hands, neon reflections on the glass.
She lifts the mug, blows across it, and sips, then glances at her phone as it lights up on the table and breaks into a surprised half-laugh.
Slow push in from a medium shot to a close-up. Sound: rain on the glass, low café chatter, the phone's short buzz.
```

Cherry Mini draft, classic dialect (5 s):

```
Mara (@mara) is a young woman in a yellow raincoat; the street is a narrow cobbled lane at dusk.
Shot 1: Mara (@mara) walks toward the camera along the lane, slowly lowering her hood with her right hand as the rain eases. The camera tracks backward in front of her at walking pace.
Shot 2: She stops under a lit shop sign, looks up at the clearing sky, and lets out a long breath, shoulders dropping. Static medium close-up.
High definition, rich detail, cinematic texture. Her face stays stable without distortion; movement is natural and smooth, with no flicker.
```
