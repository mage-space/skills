# Checking results and fixing drift

Check each result before anything builds on it: the master before the sheet, the sheet before the turntable, the turntable before any scene, the pilot before the batch. A completed request, a thumbnail, or one flattering frame is not a pass.

## How to look

- **Stills:** open the file at full size. Look at the whole composition, then the face and hair close up, then hands and contacts.
- **Sheets:** every panel against the master and against each other: same person, same scale, sides correct in each view.
- **Video, with a shell:** download the clip, then pull the frames that matter:

  ```bash
  ffprobe -v error -show_entries stream=width,height,r_frame_rate,avg_frame_rate,nb_frames,duration -of json clip.mp4
  ffmpeg -i clip.mp4 -vf "fps=1,scale=480:-1,tile=5x2" -frames:v 1 contact.png   # one frame a second
  ffmpeg -ss 6.2 -i clip.mp4 -frames:v 1 turn.png                                 # one moment, full size
  ffmpeg -ss 6.0 -t 0.5 -i clip.mp4 -fps_mode passthrough turn_%03d.png           # consecutive frames around it
  ```

  Pick the moments the shot actually has: the strongest turn, the back view, each contact, an occlusion, the last close-up. Look at a few consecutive frames around each, not one still.
- **Video, without a shell:** you can't watch it. Tell the user what to check, at which moment.
- **Watching at normal speed** is the only check of smoothness, flicker, and natural facial motion. Frames alone leave those unchecked; say so.

Note a pass, a fail, or unsure for each point below that applies. Any fail holds the result: fix that feature and check the new one the same way. A strong face match doesn't excuse wrong proportions, sides, or clothes.

## What to check

| Point | Fails when |
|---|---|
| Identity and proportions | The face, head size, or build changes from the master; a feature drifts during the clip |
| Locked details and sides | A locked detail is missing or on the wrong side |
| Hair and hairline | The style or length changes; roots slide or crawl; a dark painted band, dotted or scalloped edge appears near a highlight; a clipped highlight erases the strands |
| Clothes | Construction changes (neckline, sleeves, buttons, hem, pattern scale); fabric ignores the motion or sticks to a limb |
| Light and angle | The face is lit from another direction than the body or the scene; exposure or colour jumps with no cause |
| Shadows and contact | Shadows under the brow, nose, and chin disagree with the light; feet, hands, or props float or slide; a shadow moves on its own |
| Skin | The face's tone or sharpness differs from the neck and body beyond what the light explains; texture swims or looks pasted on |
| Eyes | Gaze or pupils jump; eyelids melt; blinks break; catchlights change with no change in light |
| Mouth and jaw | Lips double or slide; teeth change shape; the jaw moves apart from the face; talking appears in a silent shot, or lips miss the words in a spoken one |
| Expression and head | The face freezes while the body acts; expressions snap; the head slides against the neck |
| Body and hands | Feet slide, joints bend wrongly, fingers change, a hand passes through an object, weight looks wrong |
| Scene and camera | The background drifts apart from the camera move; the subject and the scene have different blur or sharpness |
| Motion artifacts | Flicker, crawling texture, warping, tearing at edges, doubled eyes, lips, or hair, jerks around a turn or a cut |

Don't over-constrain: shadows and catchlights should move when the subject or light moves, skin changes under different light, a mid-blink frame or motion blur is normal, and a still character can be intentionally still. Judge the frames around a moment, not one frame.

## Fixes by cause

Diagnose first: things that look alike can need different fixes.

| What's wrong | Likely cause | Fix |
|---|---|---|
| Face changes between images | The face is described in words instead of referenced | Mention the `@handle` in every prompt; keep the locked string word for word |
| Face right, body or outfit drifts | The character holds only the face | Add the sheet (`@kai-look`); keep the master as an image on hard shots |
| Back view or profile invents details | Only front references | The sheet for stills; the turntable on Lemon for video |
| A scar, tattoo, or part swaps sides | The side was never stated, or the master has it wrong | Write the side in capitals from the character's point of view; regenerate the master until it's right, then rebuild the sheet and turntable |
| A blend of several people | Too many or redundant references | Remove references one at a time; keep the master, the sheet, and the `@handle` |
| The grey studio or split layout appears in a scene | The prompt didn't say to ignore them | Add the ignore line, naming the studio and the layout |
| Consistent in stills, drifts in video | The video ran from a single photo | Lemon with the turntable and master; Cherry 2 Pro with the master and `@kai-look` |
| Prompt and reference disagree (long hair, short-haired master) | The model compromises between them | Make the prompt agree, or edit the master first |
| Lemon refuses a first frame with a mention | Frames and references never mix on Lemon | First frame with no mentions; mentions only in reference mode |
| Cherry refuses or ignores a reference video | Cherry's `videos` is a clip to edit, not a reference | Move the scene to Lemon, or use the sheet on Cherry 2 Pro |
| Two characters merge | The descriptions are too alike, or the action is too busy | Restate each locked string, say they must not look alike, one simple beat per shot |
| The face's colour differs from the body, but its shape and motion are right | A colour mismatch, not identity | A tracked colour correction in an editor, feathered into the neck; no new generation needed |
| Face flat or lit apart from the body | The scene still wasn't built under the scene's light | Rebuild the still (A still matched to real footage) and animate again |
| Dark spots or a scalloped hairline appear late in a clip | A generated edge defect near a highlight, or real dark roots | Compare matched frames of the still and the clip; if it's generated, describe the hairline and roots in the still and the clip's prompt and redo the hardest close-up |
| Eyes, mouth, or expressions move unnaturally | The action or references, or interpolation | Check whether the native clip has it; if so, simplify the action and render that shot again; if interpolation added it, deliver the native clip |
| Feet slide, contact fails | An action too complex for one shot | Simplify the action or split it across shots; check the whole interaction again |
| Another take looks cleaner | Unknown: its settings may differ | Compare matched frames, clothes, motion, and audio; use it if it fits the brief and say you did |

Each retry changes something real: a corrected still, a reference, a role line, the route, or the model. An unchanged reroll costs the same and fixes nothing reliably. Quote the retry before running it.
