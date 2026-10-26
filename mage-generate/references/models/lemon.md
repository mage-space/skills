# Lemon (`lemon`)

Mage's all-round video model: first and last frames, up to 10 reference images and 5 reference videos, saved voices, generated audio, and clips from 2 to 30 seconds. It follows long, structured prompts well: multi-shot scripts with timestamps, quoted dialogue, sound direction and a negative list.

## Variants

One variant, `lemon`.

- `resolution` 480p (default), 720p, 1080p. `duration` 2 to 30 seconds (default 3). `aspect_ratio` 16:9, 4:3, 1:1, 3:4, 9:16; with a frame the output follows the frame instead.
- `audio` (default true): the generated soundtrack. `false` drops it at the same price.
- The price climbs with seconds and resolution, and every second of reference video bills like a second of output.

Lemon has three modes, chosen by what you send. Frames and references never mix: send one kind or the other, or the request is refused.

| Mode | You send | The prompt carries |
|---|---|---|
| Text to video | `prompt` only | Everything: look, action, camera, sound |
| Frames | `first_image`, `last_image`, or both | Motion, plot, dialogue, camera; not the look |
| References | `image`, `additional_images`, `videos`, `@handle` mentions | Each asset's job, then the plot |

## How Mage sends your prompt

Mage rewrites mentions before Lemon sees them:

| You write | Lemon reads |
|---|---|
| `@mara` (character with a voice) | `character from image 2 with voice from [Audio 1]` |
| `@mara` (character, no voice) | `character from image 2` |
| `@redcoat` (saved reference) | `outfit from image 3` (or `pose`, `location`, `object`) |
| `@gravelvoice` (voice clip) | `[Audio 1]` |
| `@image1` | `image 1` |

- **Image numbers**: your own `image` and `additional_images` first, then mentioned characters, then mentioned references, each in the order first mentioned. With one `image` and `@mara`, Mara is image 2. All share the 10-image budget.
- **Video numbers**: `videos` in order, as `Video 1`, `Video 2`. Videos have no handles; write `Video 1` yourself.
- **Audio numbers**: voice-clip mentions first, then the voices of mentioned characters, 5 slots in all. `use_character_voices: false` leaves the character voices out.
- In reference mode, citing each asset by its number is the syntax, and Mage writes those numbers itself. In frame mode, describe what the frame shows instead of pointing at it.
- Frame mode takes no mentions at all: a character, reference or voice-clip mention adds reference media and the request is refused. Describe the person by what the frame shows.
- `prompt_extend` is off by default. Leave it off when you wrote the prompt: it rewrites your text with an extra model. Turn it on only for a one-line idea you want the model to expand.
- There is no negative-prompt field. Write the exclusions inside the prompt (see **Prompt structure**).
- Duration, resolution and aspect ratio are settings, not prompt text. Plan how many events fit the duration you set.
- If a result comes back as a still placeholder image instead of a clip, Lemon's own filter stopped the prompt or an input. Reword plainly (describe what is visible, drop words that read as risky out of context) or replace the input, then try again.

## Prompt structure

A simple clip is one paragraph: who, the action beats in order, the camera, the sound, the look. For anything longer than about 6 seconds, or with several people, use this layout, dropping the parts you do not need:

```
<One overall sentence: genre, point of view, narrative style, mood, pacing.>
<Reference lines, one per asset, reference mode only.>
Shot 1 [0-3s]: <shot size, lens, camera move>. <Subject action, expression>. <Dialogue>.
Shot 2 [3-6s]: ...
Sound: <dialogue language and texture, ambience, sound effects, music or none>.
Style: <art style, colour tone, mood>.
Negative prompt list: <only what must not appear>.
```

- **Pacing goes in the overall sentence**: "pacing shifts from steady restraint to explosive release", "brisk build, sudden conflict, short climax, warm ending".
- **Shots tile the duration** end to end, with no gaps or overlaps, 2 to 5 seconds each: 2 or 3 shots for 8 seconds, 3 to 5 for 15, 6 to 10 for 30. Pick one timestamp format (`Shot 1 [0-3s]` or `Shot 1 (00:00-00:03)`) and keep it.
- **Force one continuous shot** by starting the prompt with `Generate single shot.` Without it, Lemon may cut on its own, especially on longer clips. Use it for bridges, loops, frame work and any "no cut" request.
- **Transitions**: end a shot with "hard cut" or "dissolve", or open the next with "continues seamlessly from the end of the previous shot".
- Write each shot like a single-shot prompt: the subject's action, expression, line and the scene details that move.
- Stay inside the user's story: their characters, counts, props, events, ending and lines, verbatim. Add camera, light and sound craft, not plot.
- Bracketed section headers also work (`[Shot structure]`, `[Visual style]`, `[Overall sound]`, `[Negative limits]`), and long prompts often read better with them.

## Vocabulary

- **Lens and depth**: "85mm telephoto, shallow depth of field", "24mm wide-angle, deep focus", "anamorphic widescreen", "extreme low angle".
- **Moves**: push in, pull out, orbit (give degrees: "orbits 120 degrees around him"), handheld follow, whip pan, snap zoom, crane descending, FPV drone, Steadicam lateral tracking. Lock the frame with "Fixed shot, camera static, position unchanged."
- **Speed**: "high-speed photography, 1000fps slow motion"; cadence "fast, then slow, then fast".
- **Style trio** at the start or end: an art style (35mm film, line illustration, clay animation, motion graphics, ink wash, "minimalist keynote business style"), a colour tone (high-saturation warm yellow, cyan-blue against gilded gold, low-key high contrast), and a mood (tragic and unyielding, light and healing, oppressive and tense).
- **Physical detail sells realism**: cloth sway, dust, sparks, puddle reflections, steam, light from practical sources in the scene, "no strobing".
- **Finish**: "cinematic, film grain, high dynamic range", "IMAX-scale spectacle".

## References, characters, and frames

**Give every asset one job and say what it lends.** One line per asset:

- `Mara is @mara, adopting her face, hairstyle and clothing.`
- `The scene follows Image 1, adopting its layout, architecture and lighting; ignore the person in it.`
- `Take only the camera movement from Video 1; nothing in it appears on screen.`
- `Take only the colour grade and lighting from Image 2, not its people.`
- Several images of one person: say they together define one person and that only one appears.

**Several people**: add a `Subject locking:` line mapping every name to its asset, then "Mara and Jun are two different people and must not look alike; each look stays locked to its own reference, with no mixing or swapping." Use the same name for a person in every shot.

**Motion from a video**: "Replace the skateboarder in Video 1 with Mara, keeping the skateboarding action, path and scene unchanged." When a video lends only motion, say its look is not inherited.

**Storyboard sheet as a reference**: "Use Image 1 only as shot guidance; do not animate the storyboard as a single image." Then restate the panels left to right, top to bottom; shots need not match panels one to one.

**Editing a clip** (the clip goes in `videos`): one change per run, with add, remove, replace or change to, and a keep clause: "...; her movement and the rest of the frame stay unchanged." Point at a moment with times: "From 4s to 6s in Video 1, ...". Set `duration` to the source's length in whole seconds.

**Extending a clip**: "Using Video 1 as the opening, continue: ..." (or "as the closing", or "as the middle segment, extend forward by two seconds ... and backward by three seconds ..."). Restate the person's look, clothes and setting so they hold. Set `duration` to the source plus the new seconds; the reference seconds plus `duration` cannot pass 30.

**Limits**: 10 images (your images, characters and references together), 5 videos of 1 to 15 seconds each and 15 seconds combined, 5 audio slots.

**Frame mode**:

- A first frame already fixes the subject, scene and style. Spend the prompt on what happens: motion, plot, dialogue, camera.
- First and last frames: describe the path between them. When they differ a lot, name how it gets there, by a camera move ("the camera rises and swings left") or by the subject ("she runs toward the door").
- Timestamped shots still work with frames, for clips of 20 or 30 seconds.
- For continuity across clips, use clip n's last frame as clip n+1's first frame. Extracting a last frame needs a shell (`ffmpeg -sseof -0.1 -i clip.mp4 -frames:v 1 last.png`, then `create_upload`); without one, make the next frame as a still on Mango instead.
- Lock first and last frames to land an exact ending: a payoff pose, the next shot's opening, or a loop (the same image as both).

## Audio and dialogue

- **Lines**: speaker, speaking verb, colon, the quoted line: `Mara says: "..."`, `she whispers: "..."`, `Voiceover: "..."`. One line per speaker, named every time. Write each line in the language it should be spoken.
- **Voices**: a voiced character's mention already carries the voice, so just name her as the speaker. A saved voice clip: `Jun speaks in the voice of @gravelvoice: "..."`. Add `Lip sync` after the dialogue for a tight mouth match.
- **Timing**: put a line inside its shot, or time it: "From the 8th second, a woman's voice chants: '...'". Budget about 2.5 spoken words per second: a 4-second shot holds about 10 words.
- **Silence is explicit**: without `No dialogue.` Lemon may add speech. Control music the same way: name it ("a slow piano score that swells at the climax"), or write "No background music, only ambient and action sounds."
- **Sound effects**: well-described physical events get matching sound on their own; add standalone sound sentences for the rest ("a whoosh as each colour block slides in, a soft keyboard click on every number change").
- **Music as the driver**: with a voice-clip or music mention, "Choreograph the dance to the rhythm, speed and swells of @beat."

## Text in the image

- Short titles and numbers render in motion-graphics and logo pieces. Quote the exact text and give its place and treatment: `The title "Q3 RESULTS" slides in at top center in bold white sans-serif.`
- For a product, ask that its label "stays sharp and legible, without deformation".
- Anywhere else, rule text out: "No subtitles, no watermark, no on-screen text." Dialogue scenes especially can grow burned-in subtitles.

## Avoid

| Problem | Write instead |
|---|---|
| Unwanted cuts in a clip meant to be one take | `Generate single shot.` as the first line |
| Two characters merge or look like twins | A `Subject locking:` line and "two different people, must not look alike" |
| The wrong asset used for a role | Recount the numbers: your images, then characters, then references |
| Invented speech or music | `No dialogue.` and "No background music" |
| Too much happening, smeared motion | 2 to 5 seconds per shot; no rapid repeated actions ("shakes his head three times a second") |
| A negative list full of quality words | Only list what must not appear; never repeat positives as negatives |
| Faces or outfits drifting in long clips | Restate the look in later shots; "no costume changes, no face distortion" |

Useful negative items by kind: faces and bodies (no face distortion, no face swapping, no extra fingers, no twisted limbs), text (no subtitles, no watermark), style (no game-CG look, no childish cartoon), camera (no sustained shake, no frequent cuts), space (no axis errors, no clipping through objects), consistency (no costume changes, no scale drift).

## Examples

**First and last frame, one take** (`first_image`, `last_image`, 5 s):

```
Generate single shot. The barista lifts the steaming cup from the counter, turns, and carries it to the window table as steam trails behind her and the pendant lights sway slightly. The camera tracks left with her at waist height, then settles as she sets the cup down. Café chatter, a ceramic clink as the cup lands. No dialogue. No background music.
```

**Multi-shot drama from text** (12 s, 16:9):

```
A third-person short drama about a missed train and a kind stranger; restrained at first, warm at the end.
Shot 1 [0-3s]: Wide shot, 24mm, camera static. A young man in a grey overcoat sprints onto an empty night platform as the last train's doors close; his breath fogs in the cold.
Shot 2 [3-6s]: Hard cut. Close-up, 85mm telephoto, shallow depth of field. He bends forward, hands on his knees, and laughs once at himself.
Shot 3 [6-9s]: Medium shot, slow push in. An older woman on the bench beside him holds out half of her sandwich and says: "Next one's in forty minutes. Sit."
Shot 4 [9-12s]: Medium two-shot, camera static. He sits, takes it, and replies: "Thank you. I'm Daniel." The station lights hum.
Sound: quiet platform ambience, a train fading into the distance, soft piano entering in Shot 4.
Style: 35mm film look, cool blue platform light against warm sodium lamps, fine grain.
Negative prompt list: No subtitles, no watermark, no extra characters, no face distortion.
```

**References: a voiced character, an outfit and a location** (10 s, 9:16):

```
An upbeat vertical ad for a rain jacket.
Mara is @mara, adopting her face, hairstyle and voice. She wears @yellowshell. The setting is @harbourwalk, adopting its layout and light; ignore any people in it.
Shot 1 [0-4s]: Medium shot, handheld follow. Mara jogs along the harbour wall as rain starts; drops bead and roll off the jacket's sleeve.
Shot 2 [4-7s]: Close-up, slow push in. She pulls up the hood, grins at the camera and says: "Let it pour." Lip sync.
Shot 3 [7-10s]: Wide shot, crane rising. She runs on as the sun breaks through behind the moored boats.
Sound: rain on fabric, footsteps on wet stone, a light acoustic guitar track.
Negative prompt list: No subtitles, no watermark, no changes to the jacket's logo.
```

**Editing a clip** (the clip in `videos`, `duration` = its length):

```
Edit the video: in Video 1, change the man's white T-shirt to a black leather jacket that creases with his shoulders as he turns. His face, hair and movement, the background, the lighting and the camera path stay unchanged.
```

**Motion graphics with text** (6 s, 16:9):

```
Generate single shot. A minimalist motion-graphics chart on a deep navy background: three teal bars grow upward from left to right while the numbers "12%", "18%" and "27%" count up above them in white sans-serif, and the title "Growth in 2026" fades in at top center. A whoosh as each bar rises, a soft click on each number change. No dialogue. Negative prompt list: no other text, no watermark.
```
