# Attributes

The app's fourteen attributes, in the order they enter the prompt. The values are the exact words the prompt uses; don't paraphrase them.

| Attribute | Pick | Prompt words |
|---|---|---|
| Gender | one | `female`, `male` |
| Ethnicity | one | `Asian ethnicity`, `European ethnicity`, `African ethnicity`, `Indian ethnicity`, `Middle Eastern ethnicity`, `mixed ethnicity` |
| Hair color | one | `black hair`, `brown hair`, `blonde hair`, `red hair`, `white hair`, `pink hair`, `blue hair` |
| Hair length | one | `short hair`, `medium-length hair`, `long hair` |
| Hair style | one | `straight hair`, `wavy hair`, `curly hair`, `braided hair`, `ponytail hairstyle`, `hair in a bun` |
| Skin tone | one | `fair skin`, `light skin`, `medium skin tone`, `olive skin`, `tan skin`, `brown skin`, `dark skin` |
| Body type | one | `slim build`, `athletic build`, `average build`, `curvy build`, `muscular build` |
| Eye color | one | `brown eyes`, `blue eyes`, `green eyes`, `hazel eyes`, `gray eyes`, `amber eyes` |
| Face shape | one | `oval face`, `round face`, `square jawline`, `heart-shaped face`, `diamond-shaped face`, `oblong face` |
| Eye shape | one | `almond-shaped eyes`, `round eyes`, `hooded eyes`, `monolid eyes`, `upturned eyes`, `downturned eyes` |
| Nose shape | one | `straight nose`, `button nose`, `aquiline nose`, `wide nose`, `snub nose`, `pointed nose` |
| Facial features | any number | `freckles`, `dimples`, `beauty mark`, `facial scar`, `wearing glasses`, `facial piercing`, `beard`, `stubble` |
| Age | one | `young adult`, `adult`, `middle-aged`, `elderly` |
| Clothing | one | `casual clothing`, `formal attire`, `streetwear outfit`, `fantasy costume`, `sci-fi outfit`, `athletic wear`, `swimwear` |

## Rules

- **Gender is required** and becomes the subject: "a female" or "a male". Every other attribute is optional.
- An attribute the user didn't set is left out of the prompt, and the model chooses. Don't fill it in yourself.
- Selected values are joined with `, ` in the table's order, top to bottom. Within facial features, keep the order the user named them ("a beard and glasses" is `beard, wearing glasses`).
- The lists are fixed. If the user wants something outside them (silver hair, a tattoo, a specific outfit), say this skill can't set it and offer `mage-character-muse`, which works from an image and free-text changes.
- Map the user's words to the nearest value only when it is the same thing ("ginger" → `red hair`, "40s" → `middle-aged`). When it isn't, ask.

## Example

Female, European, red hair, long, wavy, fair skin, green eyes, freckles and glasses, young adult, casual:

```
A full-body standing portrait shot of a female with European ethnicity, red hair, long hair, wavy hair, fair skin, green eyes, freckles, wearing glasses, young adult, casual clothing. High quality, detailed, studio lighting, wide shot.
```
