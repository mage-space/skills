# Eleven Speech (`eleven_speech`)

ElevenLabs' expressive text to speech, in 90+ languages. Use it for the most natural narration, voiceover and character lines. Audio tags in square brackets direct the delivery: `[whispers]`, `[laughs]`, `[sarcastic]`. The result is an MP3 as long as the text.

## Variants

There is one variant, `eleven-v4`, with three settings:

- **`voice`:** one of the 16 below.
- **`stability`:** from 0 to 1, default 0.5. Lower is more expressive and varied; higher stays closer to the voice's steady baseline.
- **`seed`:** best-effort repeatability.

**Price:** charged per started block of 250 characters, tags included; `estimate_cost` has the figure. The prompt is at most 5,000 characters.

| `voice` | Voice | `voice` | Voice |
|---|---|---|---|
| `darian` | Warm, grounded storyteller (male) | `alicia` | Polished British anchor (female) |
| `talia` | Warm, soft guide (female) | `maisie` | Friendly, casual neighbor (female) |
| `elara` | Crisp narrator (female) | `warren` | Effortless and cool (male) |
| `baxter` | Dry, calm Australian (male) | `jade` | Upbeat and natural (female) |
| `eldrin` | Crisp British baritone (male) | `caleb` | Trusted guide (male) |
| `elowen` | Upbeat modern narrator (female) | `sawyer` | Midnight storyteller (male) |
| `kaelen` | Amateur warrior (male) | `florence` | Atmospheric British storyteller (female) |
| `lawrence` | Bright and informative (male) | `wyatt` | Seasoned mentor (male) |

## How Mage sends your prompt

- **The prompt is the script.** It goes unchanged to one `voice`, which speaks every word outside square brackets and treats each bracketed tag as direction. No separate style prompt exists.
- **One voice per generation.** A speaker label such as `Speaker 1:` would be spoken. For a conversation, generate each speaker's lines in their own voice (see Audio and dialogue).
- **No SSML.** Use the pause methods below.
- **Stray `@`.** Any `@word` is read as a saved handle and refused. Write "at" for an email address or a social handle ("mage dot space", "at mage space").

## Prompt structure

Tag a script in one pass, following ElevenLabs' own "Enhance" method. When the user hands you a script:

1. **Keep every word.** Do not add, cut or reword anything, and never move the script's own words into brackets. Your job is to add tags, not to edit the speech.
2. **Read each line** for its mood, its context and its subtext.
3. **Add audio tags** in square brackets, directly before the words they color (`[annoyed] This is hard.`) or directly after them for a reaction (`This is hard. [sighs]`). A tag can also sit at a natural pause.
4. **Tag only the voice.** Every tag must describe something you hear in the voice: an emotion, a delivery, or a non-verbal sound. Never `[standing]`, `[grinning]`, `[pacing]` or `[music]`.
5. **Leave narration alone.** If the text says "He laughed loudly", keep it as written; you may add `[chuckles]` after it, but never turn it into `[laughing loudly]`.
6. **Emphasize with punctuation only:** CAPITALS for a stressed word, plus question marks, exclamation marks and ellipses.
7. **Vary the delivery** across lines (energetic, relaxed, surprised, thoughtful), and never choose a tag that contradicts what the line means.
8. **Send only the tagged text.**

When you write the script yourself, write it for the ear first: natural spoken sentences, full punctuation, and a line break between beats. Then run the pass.

For long narration, open each paragraph with one direction tag for the whole passage, such as `[Quiet, reflective narration]` or `[Building tension, measured pace]`.

**Write everything as it is spoken.** The voice can misread symbols and digits:

| Write | Not |
|---|---|
| forty-five dollars | $45 |
| January second | 01/02 |
| two thirty PM | 14:30 |
| one hundred percent | 100% |
| Doctor | Dr. |
| mage dot space slash pricing | mage.space/pricing |

**Pronunciation.** For a name or a term the voice gets wrong, write standard IPA with stress marks, between forward slashes and in double quotes: `The term "/ˌbaɪoʊˈkemɪstri/" covers it.` Wrap only the words that need it. A plain respelling ("Shiv-awn") also works. Results vary by voice, so listen before relying on one.

**Pauses.** Use an ellipsis for hesitation and weight, a dash for a short break, a line break between beats, or a tag: `[short pause]`, `[long pause]`, `[pause]`.

## Vocabulary

| Kind | Tags |
|---|---|
| Emotion and delivery | `[happy]` `[sad]` `[excited]` `[angry]` `[annoyed]` `[appalled]` `[thoughtful]` `[surprised]` `[curious]` `[sarcastic]` `[mischievously]` `[crying]` `[whispers]` `[shouting]` |
| Non-verbal | `[laughs]` `[laughs harder]` `[starts laughing]` `[chuckles]` `[giggles]` `[wheezing]` `[sighs]` `[exhales sharply]` `[inhales deeply]` `[clears throat]` `[snorts]` `[gulps]` |
| Descriptive | `[Low, steady voice, restrained urgency]` `[Quietly, with controlled fear]` `[Warm, conversational tone, faint amusement]` `[Gentle laugh, then sincere]` `[under his breath]` |
| Experimental | `[strong French accent]` (any accent), `[sings]`, `[woo]`: these vary more between voices |
| Sound effects | `[applause]` `[clapping]` `[gunshot]` `[explosion]` `[door slams]` |

- You can combine tags, and you can invent descriptive ones; plain words for a voice quality work.
- This model makes both deliveries and sound effects, so it can read a delivery tag as a sound or the reverse. Phrase delivery tags as voice qualities (`[low, gravelly voice]`) so they cannot read as a sound cue.
- Use sound-effect tags only when the user wants a sound inside the speech. For a sound bed or music, generate it on another model (Seed Audio, Eleven Music) and mix it underneath.

## References, characters, and frames

There are no references, frames, or cloned voices: the `voice` is the character.

- **Match tags to the voice.** A delivery the voice already has lands most reliably. A soft guide will not shout convincingly, and a polished anchor may ignore `[giggles]` or `[mischievously]`. If a tag does not land, rephrase it as a voice quality or choose a voice that fits.
- **Other languages.** Write the text in the target language. Every voice speaks it fluently, without carrying its own accent over. To force an accent, try `[strong Italian accent]`; results vary.
- **Stability _(general advice)_.** Try about 0.3 for acted, tag-heavy lines and about 0.7 for steady narration that must sound the same across takes.
- **A saved character's voice.** A clean line here can become a character's voice: pass its `result.url` as `voice` to `create_character` (trimmed to 10 seconds), and Cherry and Lemon then speak that character's lines in it.

## Audio and dialogue

- **Emotion as a tag, not narration.** "She asked, her voice trembling" is spoken aloud; `[trembling] Are you leaving?` is not.
- **Conversations:**
  - Plan the speakers' voices, then generate each speaker's lines separately: one generation per line, or per run of lines by the same speaker.
  - Deliver the clips in order with a short cue list, or, when you can run commands, join them with ffmpeg with short silences for the gaps.
  - Each generation pays for at least one 250-character block, so group consecutive lines from the same speaker.
  - For interruptions, end the cut-off line with a dash (`So I was thinking we could—`), and start the reply with `[jumping in]` or `[interrupting]`.
- **Fit to a video _(general advice)_:** speech at a normal pace runs about 2.5 words a second. Check the MP3's length, then trim or rewrite the script to match the shot.

## Avoid

- Changing the user's words while tagging.
- Tags for things you cannot hear (`[smiling]`, `[walks away]`), and `[music]`.
- SSML `<break>` tags; they are not supported.
- Raw digits, symbols, URLs and abbreviations.
- Speaker labels in a single generation.
- Any `@` in the text.
- Tags that fight the voice or the meaning of the line.

## Examples

A plain line, tagged:

```text
[appalled] Are you serious? [sighs] I can't believe you did that!
```

A product voiceover (`voice: elowen`):

```text
[excited] Meet the lightest trail shoe we've EVER made. [short pause] Two hundred grams... [impressed] and it still grips wet rock. [warm, confident] Go further. Feel less.
```

Character acting (`voice: sawyer`, `stability: 0.3`):

```text
[Low, steady voice, restrained urgency] Keep the lantern covered. If they see the light, they'll know we crossed the river.

[Quietly, with controlled fear] I heard them at the bridge... not soldiers. Something else.

[Voice rising into firm resolve] Then we don't stop. We reach the tower before sunrise.
```

Long narration (`voice: florence`):

```text
The rain had stopped before dawn, leaving the old road silver beneath the moon.

[Quiet, reflective narration] She had promised herself she would not return. Yet there she was, at the gate, with the key cold against her palm.

[Building tension, measured pace] The lock turned easily. Too easily. [Softly, with wonder] On the table sat a single lantern... already lit.
```

One line of a two-voice scene (`voice: maisie`; the reply is a separate generation in another voice):

```text
[nervously] So... I may have tried to fix the boiler myself. [sheepish laugh] It's making a NEW noise now.
```
