# Eleven Music (`eleven_music`)

ElevenLabs' music model. It writes full songs with vocals, or instrumentals, as an MP3 at the requested `duration`. It also handles loops, stems, ad beds with a voiceover, and musical sound design.

## Variants

There is one variant, `eleven-music-v2.5`, with two settings:

- **`duration`:** `10`, `30`, `60`, `120`, `180` or `300` seconds. The price follows the duration; `estimate_cost` has it.
- **`instrumental`:** default `false`. Set it to `true` for no vocals.

The prompt is at most 2,000 characters. A `seed` has no effect.

## How Mage sends your prompt

- **What goes up:** `prompt` is sent unchanged as the description of the song, `duration` as its length, and `instrumental` as a switch that forces no vocals. The model composes close to the length, but not to the exact fraction of a second.
- **What is not available:** no audio reference, no seed, and no section-by-section plan. Everything goes into the one prompt.
- **Refusals.** ElevenLabs refuses a prompt that names an artist, a band or a song, or that quotes copyrighted lyrics. The request fails and is refunded, and no suggested rewrite comes back. Describe the sound instead.
- **Stray `@`.** Any `@word` is read as a saved handle and refused.

## Prompt structure

Every prompt answers five questions, whether you mean it to or not:

1. **Genre**
2. **Mood**
3. **Instrumentation**
4. **Tempo**, as a BPM, plus a key when it matters
5. **Production era**

Whatever you leave open, the model fills with its most average choice, so decide all five. Then add production words and the arrangement:

```text
<genre>, <BPM>, <key> — <instruments>, <production and space>, <mood>. <arrangement in time order>. <vocals: who, delivery, language; or "instrumental only">
```

- **Intent prompts:** a high-level purpose also works ("track for a sneaker ad", "peaceful meditation with voiceover"). The model infers the tone, structure and content from it.
- **Length of the prompt:** short, evocative prompts give freer, more surprising results; detailed prompts give control. Constrain what matters and leave room everywhere else.
- **Arrangement:** narrate it in time order, the way you would brief a band: "start with just a shuffled drum loop, add a warm sub bass after four bars, then bring in chopped vocal stabs". The small words carry the structure: start with, just, then, bring in. Without "just", the model fills the silence.

## Vocabulary

- **Production:** sidechained, close-mic'd, bone-dry, tape saturation, plate reverb, tape echo throws, wow and flutter, dusty vinyl crackle, dead room, gospel room, warm analog glue. Without the words, describe the space: "sounds like it was recorded in a stairwell".
- **Era:** a named era sets the whole production character ("1950s rock and roll with slapback echo", "1990s jungle"). An era can also change over the course of one track, and the transitions stay coherent.
- **Tempo and key:** "128 BPM", "in F minor". The model holds them closely enough to layer the result with other material.
- **Vocal delivery:** whispered, belted, breathy, raw, live, conversational, deadpan, aggressive, glitching, stacked harmonies. For several singers, write "two singers harmonizing in C".
- **Mood:** abstract words ("eerie", "foreboding") and precise musical language ("dissonant violin screeches over a pulsing sub-bass") both work.
- **Stems:** put "solo" before an instrument ("solo piano in C minor") and "a cappella" before a voice ("a cappella male chorus"), with the key, BPM and tone.

## References, characters, and frames

The model takes no references. To keep several tracks consistent, reuse the same genre, BPM, key and instrument line word for word in each prompt _(general advice)_.

## Audio and dialogue

- **Vocals:**
  - By default, a prompt gets vocals, with lyrics the model writes to fit the length. For none, set `instrumental: true` or write "instrumental only".
  - Never send lyrics with `instrumental: true`.
- **Your own lyrics:**
  - Put them in the prompt after the description; the model places them using the length.
  - The lyrics must be original.
  - _(General advice)_ Put each line on its own line, and label sections in plain words such as `[Verse]` and `[Chorus]`.
  - _(General advice)_ Size them to `duration`: a 30 s clip fits a verse or a chorus, not a whole song.
- **Vocal timing:** "lyrics begin at 15 seconds", "instrumental only after 1:45".
- **Language:** name it ("sung in Japanese"). Lyrics work in many languages.
- **Voiceover in a track:** write "Voiceover only", give the exact opening line in quotes, and say where the brand name lands.
- **Loops:** a loop prompt is about exclusion. Give the bars, the BPM and the key, and say what is banned: "four bars, no melody — just drums".
- **Sound design:** sounds that are not music work too. Take a real sound, give it one property it should not have, and describe the result plainly.
- **Under a video _(general advice)_:** choose a `duration` at least as long as the edit and trim the track to fit. End the arrangement on something you can cut on, such as "ends on a clean final hit".

## Avoid

- Naming an artist, a band or a song, or writing "in the style of" someone. Describe the genre, era, instruments and production instead.
- Lyrics taken from existing songs.
- An open prompt such as "upbeat electronic track", where all five decisions are left to the model.
- Lyrics sent alongside `instrumental: true`, or both "instrumental" and a vocal description.
- More lyrics than the duration can hold.
- Any `@` in the prompt.

## Examples

All five decisions made (`duration: 30`, `instrumental: true`):

```text
French house, 122 BPM — filtered disco sample chops, sidechained bass, tight four-on-the-floor kick, rooftop-at-sunset mood, warm analog glue
```

Narrated arrangement (`duration: 60`):

```text
UK garage, 132 BPM — start with just a shuffled drum loop, add a warm sub bassline after four bars, then bring in chopped vocal stabs for the drop. Breathy female vocal, conversational verses, the hook sung twice.
```

Loop (`duration: 10`, `instrumental: true`):

```text
boom bap drum break, 90 BPM, dusty and swung, four bars, no melody — just drums
```

Ad bed with a voiceover (`duration: 30`):

```text
Track for a premium running-shoe commercial. Bright, driving and polished, 118 BPM, synth bass and crisp claps. Voiceover only. The script begins: "Every mile starts lighter." End on the brand name "Stride", spoken over a final chord.
```

Original lyrics (`duration: 60`):

```text
Bedroom pop about a city at 5am, 96 BPM, A minor — muted guitar chops, soft breakbeat, tape-warm bass. Verse close and conversational, chorus opens wide with stacked harmonies.

[Verse]
Streetlights blinking out one by one
Bakery windows catching the sun
[Chorus]
We stayed up, we stayed up
Long enough to see it start again
```

Sound design (`duration: 30`, `instrumental: true`):

```text
a thunderstorm in 6/8 — thunder lands on the downbeat, rain fills the offbeats, distant lightning as crash cymbals
```
