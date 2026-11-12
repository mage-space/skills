# Frame rate

Deliver the frame rate the model makes. Writing "60 fps" in a prompt changes nothing, and raising the rate means interpolating: inventing frames between real ones, which can warp eyes, mouths, hands, hair, and thin objects. Do it only when the user asks, only on the final clip (never on a turntable, a draft, or anything you will pass back to Mage), and say it was interpolated. Everything here needs a shell with ffmpeg; keep the unmodified clip.

## 1. Measure the clip

```bash
ffprobe -v error -count_frames -show_entries stream=codec_type,width,height,r_frame_rate,avg_frame_rate,nb_read_frames,duration -of compact clip.mp4
```

A video model's file can be padded to a higher rate than it was made at: 24 frames a second stored as 30 repeats one frame in five. Count the near-duplicates:

```bash
ffmpeg -i clip.mp4 -vf mpdecimate -loglevel debug -f null - 2>&1 | grep -E " drop pts" | grep -oE "pts_time:[0-9.]+"
```

Repeats at a steady interval (every fifth frame, every 25th) are padding. Repeats that bunch together are a pause or a still moment: leave those alone, and don't call every low-motion pair a duplicate.

## 2. Remove padding (only a verified, regular pattern)

For 24 padded to 30 (one repeat in five), drop the repeats and keep the clip's length:

```bash
ffmpeg -i clip.mp4 -vf "decimate=cycle=5,setpts=N/24/TB" -r 24 -c:v libx264 -crf 16 -pix_fmt yuv420p -c:a copy clip_24.mp4
```

Check the result: the same duration as the source, and `nb_read_frames` equal to 24 × the duration. For any other pattern, use the retained frame count over the measured duration as the rate; never force 24 when the numbers don't say 24, which changes the length and the audio sync.

## 3. 60 fps, when the user asks

Motion-compensated interpolation from the clip with no padding:

```bash
ffmpeg -i clip_24.mp4 -map 0:v:0 -map '0:a:0?' \
  -vf "tpad=stop_mode=clone:stop_duration=0.15,minterpolate=fps=60:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1:scd=fdiff,trim=duration=DURATION,setpts=PTS-STARTPTS" \
  -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -c:a copy -fps_mode cfr -movflags +faststart clip_60.mp4
```

Replace `DURATION` with the measured duration in seconds. The short cloned tail and the trim keep the last frames, which `minterpolate` otherwise drops. `scd=fdiff` holds hard cuts instead of morphing across them. Plain frame duplication (`fps=60` alone) only relabels the clip; it is not smoother.

## 4. Verify and check again

```bash
ffprobe -v error -count_frames -select_streams v -show_entries stream=r_frame_rate,avg_frame_rate,nb_read_frames,duration -of compact clip_60.mp4
ffmpeg -v error -i clip_60.mp4 -f null -
```

- `r_frame_rate` and `avg_frame_rate` are both `60/1` (not 59.94), the frame count is 60 × the duration within a frame, and the decode prints no errors.
- Check the new file like a new render (`checks.md`): the strongest turn, the back view, every contact, every cut, and the last close-up, frame by frame. Eyes, mouth, hands, and the hairline are where interpolation breaks first. If it added a defect the native clip doesn't have, deliver the native clip and say why.
- The audio is copied unchanged; play the start and the end to confirm it still sits on the picture.
- Deliver both files: the native one and the 60 fps one, labelled as interpolated.
