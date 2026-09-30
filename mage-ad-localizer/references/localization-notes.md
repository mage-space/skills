# Localization notes

## Text length

Translations change length. Plan line breaks so the text fits the same area without shrinking below legibility.

| Language | Length vs English | Notes |
|---|---|---|
| German, Dutch, Finnish | +20–35% | Long compounds; prefer shorter synonyms over hyphenating a headline. |
| French, Spanish, Italian, Portuguese | +15–30% | Spanish for Spain vs Latin America differ in vocabulary and "tú"/"usted"; ask which. |
| Polish, Russian, Czech | +10–25% | Cyrillic for Russian; check the font renders it. |
| Japanese, Chinese, Korean | −10–50% characters | Needs a CJK-capable font style; don't break a word across lines. Simplified (mainland China) vs Traditional (Taiwan, Hong Kong) Chinese. |
| Arabic, Hebrew, Persian, Urdu | varies | Right-to-left: mirror the text alignment and reading order. Arabic letters join; never space them out. |
| Hindi, Thai | varies | Scripts with stacked marks need extra line height. |

For a short CTA, pick the idiomatic button text the market uses ("Jetzt kaufen", "Comprar ahora", "今すぐ購入") rather than a literal translation.

## Formats

- **Prices and currency:** keep the amount unless the user gives the local price. Format it locally: `€19,99` (most of the eurozone), `19,99 €` (France), `¥1,980`, `R$ 99,90`. Never convert currency yourself.
- **Numbers:** decimal comma in much of Europe and Latin America (`1.000,50`), decimal point in the US, UK, and Asia (`1,000.50`).
- **Dates:** `DD/MM` in most of the world, `MM/DD` in the US, `YYYY年MM月DD日` in Japan.
- **Units:** metric everywhere except the US; convert only when the user asks, and round sensibly.
- **Percentages:** `20 %` with a space in French and German, `20%` in English.

## Tone

- Formal vs informal address differs by market and brand: German "du" vs "Sie", French "tu" vs "vous", Japanese politeness. Match the brand's voice in that market; ask when unsure.
- Wordplay and idioms rarely survive. Replace them with a local idiom that carries the same idea, and tell the user you did.

## Cultural checks

Flag, don't silently change:

- Gestures, colors, or symbols with different meanings (a thumbs-up, white for mourning in parts of East Asia).
- Offers or claims that local advertising law may restrict (health, finance, alcohol, comparative claims).
- Seasonal references that don't match the hemisphere or calendar.

## Proofreading checklist

- Every approved line appears exactly once, spelled exactly, with accents and diacritics.
- No leftover source-language words except the ones kept on purpose.
- Line breaks fall between words (or characters, for CJK) at natural points.
- Right-to-left text is aligned right and reads in the correct order.
