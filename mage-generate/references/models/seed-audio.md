# Seed Audio (`seed_audio`)

Mage's audio model and the default for any sound: voices, multi-speaker dialogue, music beds and sound effects generated together from one prompt, as an MP3 of exactly the requested duration. It is a scene model, not text-to-speech: write the scene and the performance, not only the words.

## Variants

One variant, `seed-audio-1.0`.

- `duration`: 5, 10, 30, 60 or 120 seconds. A longer piece is several calls, joined afterwards (with ffmpeg when you can run commands, or in an editor).
- Prompt: at most 2,986 characters.
- Dialogue in 20 languages: English, Chinese, Japanese, Korean, Mexican Spanish, Castilian Spanish, Indonesian, German, Brazilian Portuguese, French, Thai, Vietnamese, Malay, Filipino, Italian, Russian, Dutch, Polish, Turkish, Swedish. One voice can carry across languages.
- `seed` does nothing: every run is a new take.

## How Mage sends your prompt

- Fields: `prompt`, `duration`, `image` (one picture), `speech_rate` (−50 to 100; 100 is double speed), `pitch_rate` (−12 to 12), `loudness_rate` (−50 to 100), `sample_rate`. Audio references come only from `@handle` mentions.
- Timing: Mage marks the whole clip as one time span in front of your prompt, and the model reads your prompt as content for that window. Afterwards the audio is trimmed or padded to exactly `duration`, with a short fade at the end.
  - Don't write a whole-clip span yourself; Mage adds it.
  - Content that runs long is cut off at the end, mid-word. Content that runs short leaves silence at the tail. Write to the duration.
  - Per-line timestamps (below) work inside that span. Keep every one within 0 and the duration.
- Saved audio clips: Mage rewrites each `@handle` to `@Audio1`, `@Audio2`, `@Audio3` in the order you first mention them, up to three. Write the handle, never `@Audio1` yourself: any `@word` that isn't a saved handle is refused. Characters (image handles) can't be mentioned here.
- `image`: one picture of a person or creature; the model designs a voice that fits it. With a picture, the prompt can be just the delivery and the words. A picture and audio clips can't go in the same request.
- The rate fields change the whole clip. Set pace and pitch per speaker in words; use the fields only for a global nudge, such as a slightly faster read of a finished script.

## Prompt structure

A good prompt has five parts, in this order: (1) the environment: place, weather, context; (2) background music and sound effects; (3) what the characters do and look like; (4) each voice: gender, age band, accent, timbre, emotion, pace; (5) the exact words.

Write it as one scene in time order, like a radio-drama script:

```
<Place and ambience>. Background music: <instruments, mood, how it moves>.
<Name> (<gender, age band, accent, timbre, emotion, pace>) <delivery>: "<line>"
<A sound where it happens>. <Name>, <short delivery note>: "<line>"
<How it ends: the music swells, fades or cuts; the ambience continues to the end>.
```

- Describe a voice fully the first time; after that, the name and a short delivery note.
- Write the whole prompt in the language of the lines: a Spanish scene gets a Spanish prompt.
- Only the quoted words are spoken. Names, voice notes and scene description are direction.

A music and effects bed with no voice:

```
Generate pure background music and sound effects only. No voice, no dialogue, no narration, no lyrics.
Style: <genre and mood>. Create original music only; do not imitate any existing melody.
Background music: <instruments and how the piece develops>.
Sound effects: <list>. Keep effects clear but balanced under the music.
Duration: about <the duration field> seconds.
Structure:
[0:00-0:08] <section: instruments, effects, mood>
[0:08-0:18] <section>
…
Final mix: No vocals or spoken words. <Overall character of the mix>.
```

Section times are approximate: timing control is precise for dialogue only. Make the sections add up to the `duration` field.

## Vocabulary

- Voice: gender and age band ("young adult female", "middle-aged male"), accent ("British accent", "soft Southern US accent"), timbre ("raspy, low, gravelly", "clear, bright, crystalline", "deep and resonant"), emotion and pace ("rapid, soaring, full-throated", "softly, forcing herself to stay composed", "words speeding up as he panics").
- Voice treatments: "as if from a television, with slight reverberation", "as if over a walkie-talkie", "a mechanical quality", "whispered close to the microphone".
- Music: instruments, mood and change over time ("deep war drums, low brass and a mournful choir"; "the drums quicken and the choir brightens"; "it shifts to a lone clarinet that fades into silence").
- Effects: a concrete source plus the sound ("arrows hiss through the rain", "a sword slides back into its sheath with a crisp shhhk", "chains drop into the dust with a heavy clatter"). Give an onomatopoeia its source noun so it reads as sound, not speech.
- Ambience and space: "inside a huge stadium, the roar of tens of thousands of fans throughout", "footsteps echo in a stone hall", "a small tiled bathroom".

## References, characters, and frames

- With saved clips, say three things: what to generate, which clip, and what it is for (timbre, accent, emotion). Still describe the voice in words beside the handle: `Marcus (smooth, confident male broadcaster voice; the voice of @marcus-voice), upbeat:`.
- A good voice clip: one speaker, no music or noise, 5–30 seconds, speaking from the first second.
- The same voice across takes and scenes comes from reusing the same saved clip. A description alone drifts between runs.
- A voice for a video character: generate a clean line here, then pass its `result.url` as `voice` to `create_character` (trimmed to 10 seconds) or save it with `create_reference` as `kind: "audio"` (trimmed to 15 seconds). Cherry splits a fixed audio budget across its clips and may keep only the first 5 seconds of one, so make the clip speak from its first moment.
- No frames: this is an audio model.

## Audio and dialogue

- Timing a line: put the span at the start of the quoted words, in seconds with one decimal: `"[5.5s:8.0s] Maya! Wait — you're really leaving tonight?"`. Time each line of dialogue; music and effects follow the scene order.
- Size each window to its words. A natural English pace is about 2.5 words a second, so a 10-word line needs about 4 seconds; excited delivery runs faster, grave delivery slower.
- Leave 0.3–0.6 s between speakers for natural turn-taking, and end the last line at least 0.5 s before the clip ends so the trim and fade fall on silence or ambience.
- To fit picture: measure the cut, request the next duration up, time the lines to the picture, and trim the result to the cut.
- Long scenes: one call per scene of up to 120 seconds, the same saved voices in each, joined afterwards.

## Avoid

- Only the words to say, for a scene: add the place, the sound and the voice description. Conversely, for a clean voice clip, say so: "Clean, close-miked studio voice recording. No music, no background sound, no effects."
- A whole-clip timestamp or a script longer than the duration.
- Writing `@Audio1`, or a voice handle with no description beside it.
- Speakers without labels in a multi-voice scene: voices swap.
- A prompt in one language with lines in another.
- Asking for a known song or theme: ask for original music in that genre and mood.

## Examples

Two voices, timed (`duration`: 10):

```
A quiet train platform at night in light drizzle, a station announcement echoing faintly under the roof. Ryan (young adult male, warm voice, slightly out of breath) calls out anxiously: "[0.4s:3.0s] Maya! Wait — you're really leaving tonight?" Maya (young adult female, soft voice) answers, forcing herself to stay composed: "[3.5s:8.5s] I have to. I've spent years chasing this. I can't walk away now." A train door chimes and slides shut; the drizzle continues to the end.
```

Commentary over a crowd (`duration`: 10):

```
Inside a huge football stadium, the deafening roar of tens of thousands of fans throughout. The commentator (middle-aged male, British accent, rich penetrating voice, wildly excited) shouts in a rapid, soaring, full-throated tone: "[0.5s:8.0s] OH, HE SCORES! WHAT A GOAL! He beats two men and buries it in the top corner — UNBELIEVABLE!" He draws out the word "GOAL", his voice cracking, and the crowd's cheer erupts at the goal and carries to the end.
```

Music bed for a product clip (`duration`: 30):

```
Generate pure background music and sound effects only. No voice, no dialogue, no narration, no lyrics.
Style: bright, modern, confident tech commercial. Create original music only.
Background music: clean electric piano, plucked synth arpeggios, a tight kick and claps, warm sub bass.
Sound effects: soft UI clicks, a glassy whoosh, a gentle chime on the reveal. Keep effects clear but balanced under the music.
Duration: about 30 seconds.
Structure:
[0:00-0:08] Electric piano alone, light and curious, one soft click.
[0:08-0:20] Drums and bass enter, arpeggios rise, a whoosh at 0:19.
[0:20-0:27] Full groove, brighter, the chime lands on the reveal.
[0:27-0:30] The groove stops on one sustained piano chord that rings out.
Final mix: No vocals or spoken words. Polished, upbeat, ready for a 30-second ad.
```

Two saved voices (`duration`: 30):

```
Ambient street sounds: passing cars, distant chatter, a light breeze. Marcus (smooth, confident male broadcaster voice, warm and playful; the voice of @marcus-voice), upbeat, says: "[0.5s:4.5s] Quick question — what's the most embarrassing thing that's ever happened to you?" Tyler (younger male, a little nervous, expressive; the voice of @tyler-voice) groans, then laughs: "[5.2s:13.5s] Oh, you do NOT want to know. My first day at a new job, I walked into a meeting and completely missed the chair." Marcus bursts out laughing: "[14.2s:16.5s] No! In front of everyone?" Tyler, defeated, half-laughing: "[17.2s:25.0s] Everyone. And I grabbed the tablecloth on the way down. They still call me Splash." Both laugh; the street ambience swells and fades out.
```

A voice from a picture (`image`: the character portrait; `duration`: 5):

```
The man in the picture says warmly, a little amused, unhurried: "[0.3s:3.8s] Well, look who finally showed up."
```

A clean voice clip for a character (`duration`: 10):

```
Clean, close-miked studio voice recording. No music, no background sound, no effects. Mara (woman in her early thirties, low, warm, slightly husky voice, standard American accent, calm and assured) says at an even pace: "[0.2s:9.3s] I've walked this coast every morning for ten years. The tide always tells you something, if you're patient enough to listen."
```
