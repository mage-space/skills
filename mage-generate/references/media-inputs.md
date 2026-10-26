# Media inputs

## Where inputs come from

| Source | How to pass it |
|---|---|
| A public link to the file itself | The https URL, as is. Mage downloads it (60 s, 3 redirects, 100 MB). |
| A small local image (under about 3 MB) | A data URL: `data:image/png;base64,...`. |
| A larger local file, on a machine where you can run commands | `create_upload` with the file's `content_type`, then PUT the file to `upload_url` with exactly the returned `headers`, then pass the returned `url`. |
| An earlier Mage result | Its `result.url`. |
| A saved character or reference | `@handle` in the prompt, not a field. |
| A file attached to the chat | Not possible: it never reaches Mage. Ask for a direct link, or use a shell and `create_upload`. |

Formats: images JPEG or PNG; video MP4, MOV, or WebM; audio MP3 or WAV. Inputs and results are deleted after 30 days.

Upload example:

```bash
curl -X PUT -T clip.mp4 \
  -H 'Content-Type: video/mp4' \
  -H 'x-goog-content-length-range: 0,104857600' \
  '<upload_url>'
```

## Fields by model

| Model | Reference images | Frames | Source video |
|---|---|---|---|
| Mango, Guava, GPT Image 2.5 Flare | `image`, `additional_images` | none | none |
| Cherry (all variants) | `image`, `additional_images` | none | `videos` |
| Lemon | `image`, `additional_images` | `first_image`, `last_image` | `videos` |
| Seed Audio | `image` (one picture of a person or creature) | none | none |
| Eleven Speech, Eleven Music | none | none | none |

Opt-in models differ (Berry and Grok Video take one source `video`, not `videos`); their files in `references/models/` list their inputs. `get_model` returns the exact fields (`image_inputs`, `video_inputs`) and the image budget (`max_images`), which characters and references mentioned in the prompt share.

## Patterns

- **Edit an image:** pass it in `image` with Mango 3 and describe only the change. Mango 3 keeps everything else in place.
- **Combine images:** put each in `image` / `additional_images` and name them in the prompt with `@image1`, `@image2`: "The model from @image1 holding the bag from @image2 on the street from @image3."
- **Image to video, exact first frame:** Lemon with `first_image`, and optionally `last_image` for where it ends.
- **Image to video, highest quality:** Cherry 2 Pro with the image in `image` and `Use @image1 as the first frame.` as the prompt's first sentence, `aspect_ratio` set to the image's. It is a reference, not a frame field, so the clip may not match it pixel for pixel; for that, use Lemon's `first_image`.
- **Edit a video:** Cherry 2 Pro or Lemon with the clip in `videos`, and a prompt describing the change ("Change her jacket to red leather. Keep the motion, framing, and timing."). Call the clip `video 1` in the prompt; `@video1` is refused. The price depends on the clip's length: `estimate_cost` measures a `create_upload` URL or an earlier result, and answers `requires_media_measurement` for a video on another host. On Cherry, `keep_original_audio: true` keeps the source's sound for a visual edit and avoids moderation false flags caused by it.
- **A voice for a face:** Seed Audio with a picture of the person or creature in `image`: the model designs a voice that fits it, and the prompt can be just the delivery and the words.
