# Short drama templates

One worked example runs through every stage: a 30-second, five-shot scene with two characters, NORA (`@nora`) and ELI (`@eli`), in a diner (`@diner`). Replace it with the user's story; keep the structure.

## Bible

```markdown
# <Title>

Logline: <who wants what, against what, in one sentence>
Format: 9:16, <n> episodes of <s> seconds, dialogue in <language>
Look: <setting and period, materials, palette, light by time of day, lens feel>. Avoid: <what does not belong in this world>.

## Characters

### NORA (@nora)

- Role: <protagonist>. Wants <...>; fears <...>; hides <...>.
- Fixed look: <age, build, skin, hair, eyes>; <costume, colours by name>. Never changes: <...>.
- Voice: <register, accent, pace, texture>. Clip: <how it was made>.
- Knows: <what she knows at the end of the latest episode>.

## Places

### Diner (@diner)

- Layout: <fixed landmarks and where they sit>. Light: <source and direction, by time of day>.
```

## Outline (series)

| Ep | What happens | What is revealed | Ends on (the hook) | Who knows what afterwards |
|---|---|---|---|---|

Each episode opens on the previous one's hook, and its own hook is a question the next episode answers.

## Script

Action first, then the speaker, the delivery in parentheses, and the exact line.

```text
EP 1, SCENE 1. INT. DINER - NIGHT

NORA wipes the counter in slow circles. ELI, on the stool across from her, slides a sealed white envelope over the counter. Her hand stops on it.

ELI (quietly, eyes on the envelope)
Dad wanted you to have this.

At the word "Dad", NORA's jaw sets. She pushes the envelope back to him without opening it.

NORA (flat)
He had twenty years to give me something.

ELI tips the envelope. A small brass key slides out onto the counter between them.

ELI (gently)
It's the house key. It's yours now.

NORA looks at the key. Her hand hovers over it and does not touch it.
```

## Shot list

Blocking, once per scene:

```text
Scene 1, diner, night. NORA stands behind the counter, facing the door; ELI sits on the stool opposite, an arm's reach away. The register is at NORA's right; the window with a red neon sign is behind ELI. Cameras stay at the counter's left end, so NORA is screen left and ELI screen right in every two-shot. Warm overhead light on the counter; red neon on ELI's back. Envelope: ELI's hand → counter → NORA's hand → pushed back to ELI. Key: inside the envelope → on the counter, untouched.
```

| Shot | s | Framing and camera | Start → action → end | Line (speaker, delivery) | Sound | Hook |
|---|---|---|---|---|---|---|
| 1 | 6 | Close-up on NORA, eye level, locked | Wiping → the envelope slides into frame → her hand stops flat on it | — | Cloth on steel, paper | Question |
| 2 | 5 | Medium close-up on ELI past NORA's shoulder | Eyes on the envelope → speaks → looks up at her | ELI, quietly: "Dad wanted you to have this." | Fridge hum | — |
| 3 | 7 | Close-up on NORA, slow push in | Listening → jaw sets at "Dad" → pushes the envelope back → speaks | NORA, flat: "He had twenty years to give me something." | Paper on steel | Reversal |
| 4 | 5 | Extreme close-up, top-down on the counter | Envelope under ELI's hand → he tips it → the key slides out and stops between them | — | Metal on steel | Reveal |
| 5 | 7 | Medium two-shot in profile, locked | Both look at the key → ELI speaks → NORA's hand hovers over it, not touching | ELI, gently: "It's the house key. It's yours now." | Fridge hum | Cliffhanger |

## Self-check, before pricing

1. **Coverage**: the shots add up to the clip's length; each line fits its shot (about 2.5 English words a second, then a beat); at most two lines a shot.
2. **Chain**: each shot starts in the state the previous one ended in (positions, hands, props, light, eyelines); a jump in time or place is written as a cut.
3. **Everyone tracked**: a character out of frame still has a place; every prop has one holder at a time.
4. **Space**: one camera side per conversation; each character keeps their screen side in every two-shot.
5. **Hooks**: shot 1 opens on conflict or a question; a reveal, reversal or callback at least every third shot; the last shot ends on a turn.
6. **Voices**: at most three speakers in a Cherry scene (five on Lemon); every speaker who appears in more than one clip has a voice clip.
7. **Three-way read**: script → shot list → prompt. Every trigger, reaction, handoff and line survives word for word.

## Prompts

### Identity still: Mango 3, 2:3

```text
Character identity reference for a photoreal vertical drama. One original adult woman, NORA: late twenties, slim, light olive skin with faint freckles, dark brown hair in a low messy bun with loose strands, tired brown eyes. A pale grey diner uniform dress with a white collar, a navy cardigan with the sleeves pushed up, a plain silver watch.
One person only, from the top of her head to her knees, standing in a slight three-quarter turn with her face nearly frontal, both empty hands relaxed and visible. Plain warm-grey studio backdrop. Her face large and sharp.
Photoreal, natural unretouched skin texture, soft even studio light that shows both eyes and the clothes, neutral closed-mouth expression. No text, labels, logos, props or furniture, no second view, no resemblance to a real person.
```

The still fixes appearance only: the scenes set the pose, expression and light.

### Place still: Mango 3, 9:16

```text
An empty roadside diner at night, seen from the left end of the counter. The steel counter runs across the middle of the frame with four red stools in front of it; the register sits at the counter's right end; behind the stools, a window with a red neon sign whose letters cannot be read; the door at the far right. Warm overhead pendant lights pool on the counter; red neon spills across the stools. Photoreal, lived-in, no people, no readable text.
```

### Keyframe: Mango 3 Turbo, 9:16

One per shot, at the shot's key moment:

```text
Vertical film still from a photoreal drama: a close-up of @nora behind the counter of @diner, seen at eye level from the counter's left end. Her jaw is set and her two fingers push a sealed white envelope away across the steel counter. Warm overhead light on her face, red neon glow soft in the background. Natural skin, shallow depth of field, no text.
```

### Voice clip: Seed Audio, `duration` 10

With the character's identity still as `image`, the prompt can be just the line and how it is said:

```text
NORA says, tired and guarded, low and even, close to the microphone: "We close at midnight. If you're not eating, you're leaving. I've had a long enough night already." One voice only, a quiet dry room, no music, no other sounds.
```

Without an image, describe the voice: `NORA (woman in her late twenties, low slightly husky voice, American English, tired and guarded) says: "..."`. On Eleven Speech, choose the preset `voice` that fits and give it the same line, with a tag for the delivery (`[tired, guarded] We close at midnight...`). Then `create_character` with the face and this clip's `result.url` as `voice`.

### Scene: Cherry 2 Pro

`image` is the storyboard grid; `@nora`, `@eli` and `@diner` are saved; `use_character_voices` is on. Lines are in `{}`. Without a grid, drop the first line.

```text
@image1 is the storyboard: five panels read left to right, top to bottom, one per shot, for shot order and rough framing only; do not copy its drawing style or layout.
Cast: NORA is @nora and ELI is @eli: face, hair and build only. NORA wears a pale grey diner uniform and a navy cardigan; ELI wears a worn brown canvas jacket over a grey T-shirt.
Place: @diner, its layout, materials and light only.
Photoreal vertical drama at night, natural skin, readable eyes and hands. NORA stands behind the steel counter facing the door; ELI sits on the stool opposite her, an arm's reach away. The register is at NORA's right; the window with red neon is behind ELI. Cameras stay at the counter's left end: NORA is screen left and ELI screen right in two-shots. Warm overhead light on the counter, red neon on ELI's back. Clothes, positions and the counter's layout persist.
Dialogue: each character in their own voice; only the named speaker talks and the other keeps their mouth closed. No narrator, no music or score; a quiet fridge hum, cloth, paper and metal sounds with the actions. No subtitles, captions or on-screen text.
Avoid: extra people, any line not written below, a second envelope or key.
Shot 1: Close-up on NORA at eye level from the counter's left end, camera locked. She wipes the counter in slow circles without looking up. ELI's hand slides a sealed white envelope into frame across the counter; her hand stops flat on it. End with her hand resting on the envelope.
Shot 2: Cut to a medium close-up on ELI past NORA's shoulder. His eyes stay on the envelope. ELI says quietly, in English: {Dad wanted you to have this.} End with him looking up at her.
Shot 3: Cut to a close-up on NORA; the camera pushes in slowly. At the word "Dad" her jaw sets. She slides the envelope back to ELI with two fingers without opening it. NORA says flatly, in English: {He had twenty years to give me something.} End with the envelope back under ELI's hand.
Shot 4: Cut to a top-down extreme close-up of the counter between them. ELI tips the envelope; a small brass key slides out and stops between their hands. No dialogue. End with the key alone on the steel.
Shot 5: Cut to a medium two-shot in profile, camera locked. Both look down at the key. ELI says gently, in English: {It's the house key. It's yours now.} NORA's hand rises and hovers above the key and does not touch it. End with her hand still in the air.
```

A scene that continues another adds, after the cast line: `@image2 is the last frame of the previous scene: positions and light only.` (when you could extract and upload it) and opens its first shot with `Continuing from the previous scene: <positions, hands, props, light>.`

### Scene: Lemon

Reference mode, same handles and voices; time ranges tile the clip:

```text
NORA is @nora and ELI is @eli: face, hair and build only. The place is @diner.
<Look, blocking, camera side and light, as for Cherry.> Each character speaks in their own voice; the listener keeps their mouth closed. No music, no subtitles or on-screen text.
Shot 1 [0-6s]: <framing>. <action>. End with <state>.
Shot 2 [6-11s]: <framing>. ELI says quietly: "Dad wanted you to have this." End with <state>.
```

Frame mode (`first_image`, optionally `last_image`) takes no handles or voices: name people by what they look like and keep it to one movement.

```text
Generate single shot. The woman in the grey diner uniform reaches across the steel counter, closes her hand around the small brass key and pulls it toward her. The camera holds still. Quiet fridge hum, metal sliding on steel. No dialogue. No background music. No subtitles or on-screen text.
```

### Voice-over: Eleven Speech

The same `voice` for the narrator in every episode; tags direct the delivery:

```text
[quietly] Twenty years without a word. [pause] And now he sends me a key.
```

### Music: Eleven Music (`instrumental: true`) or Seed Audio

Eleven Music, `duration` at or above the episode's length:

```text
Restrained late-night drama underscore, 70 BPM, D minor — soft felt piano, low sustained strings, a faint pulse, close and intimate. Start with just the piano, let the strings creep in through the middle, and end on one unresolved chord for the cliffhanger. Instrumental only.
```

Seed Audio, `duration` 30, 60 or 120:

```text
Generate pure background music only. No voice, no dialogue, no narration, no lyrics.
Style: a restrained, tense drama underscore, intimate and late-night. Instruments: soft felt piano, low sustained strings, a faint pulse.
Structure: the first ten seconds sparse and quiet; it tightens slowly through the middle; the last seconds hold one unresolved chord for the cliffhanger.
Original music only. No vocals or spoken words.
```

## Shell steps (ffmpeg)

Only when you can run commands. Upload anything Mage needs to read with `create_upload` (PUT the file with the returned headers, then pass the returned `url`).

Storyboard grid, keyframes downloaded as `kf/01.png`, `kf/02.png`, … (`tile=2x2` for four shots, `3x2` for five or six):

```sh
ffmpeg -i kf/%02d.png -vf "scale=540:960,tile=3x2:padding=16:margin=16:color=white" -frames:v 1 storyboard.png
```

Last frame of a scene, for the next one:

```sh
ffmpeg -sseof -0.1 -i s1.mp4 -frames:v 1 s1_last.png
```

Join the scenes in order (they share size and frame rate when made with the same settings):

```sh
printf "file '%s'\n" s1.mp4 s2.mp4 > scenes.txt
ffmpeg -f concat -safe 0 -i scenes.txt -c:v libx264 -crf 18 -c:a aac -movflags +faststart cut.mp4
```

Music under the cut, ducked about 10 dB below the dialogue, faded over the last 1.5 s (set `st` to the cut's length minus 1.5):

```sh
ffmpeg -i cut.mp4 -i music.mp3 -filter_complex "[1:a]volume=-10dB,afade=t=out:st=58.5:d=1.5[m];[0:a][m]amix=inputs=2:duration=first:normalize=0[a]" -map 0:v -map "[a]" -c:v copy -c:a aac episode.mp4
```

A voice-over starting at 2.0 s:

```sh
ffmpeg -i episode.mp4 -i vo_1.mp3 -filter_complex "[1:a]adelay=2000:all=1[v];[0:a][v]amix=inputs=2:duration=first:normalize=0[a]" -map 0:v -map "[a]" -c:v copy -c:a aac episode_vo.mp4
```

## Edit list (no shell)

Deliver the links in this shape so any editor can assemble the episode:

```text
Episode 1, "The Key" — 9:16, 30 s
Video track
  1. Scene 1, the diner (0:00–0:30): <link>
Music
  Underscore (<link>): from 0:00, about 10 dB under the dialogue, fade out over the last 1.5 s, trim to 0:30
Voice-over
  "Twenty years without a word…" (<link>): starts at 0:02
Links expire in 30 days: download them now.
```
