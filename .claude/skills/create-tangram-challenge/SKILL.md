---
name: create-tangram-challenge
description: Converts a colorful tangram image into a black-and-white silhouette challenge — solid black pieces with no internal edges visible, making the shape recognizable but the piece boundaries hidden. Use whenever the user has a colorful tangram figure and wants to create a printable challenge version, mentions "tangram challenge", asks to remove colors from tangram pieces, or wants to make a black-and-white version of a tangram image.
---

# Create Tangram Challenge

Convert a colorful tangram image to a solid black silhouette suitable for a puzzle challenge.

## What it does

- All colored tangram pieces → solid black (internal piece boundaries disappear)
- White background and interior holes → stay white
- Edges are crisp (JPEG artifacts suppressed before thresholding)

## How to run

Use the bundled script. The script path is relative to this skill file:

```bash
python3 <skill-dir>/scripts/convert.py <input-image> [output-image]
```

- If no output path is given, the script appends `-challenge` before the extension:
  `page02-animals.jpg` → `page02-animals-challenge.jpg` in the same directory.
- The script prints the output path on success.

## Step-by-step

1. **Resolve the input file** — confirm the path exists; if the user gave a relative path, resolve it against the current working directory.

2. **Run the script** for each input file:
   ```bash
   python3 ~/.claude/skills/create-tangram-challenge/scripts/convert.py <input> [output]
   ```

3. **Show the result** — read the output file so the user can see the generated image.

4. **Batch mode** — if the user provides multiple files or a glob pattern, loop over them and run the script once per file.

## Dependencies

`Pillow` and `numpy` must be installed. If the script fails with `ModuleNotFoundError`, install them:

```bash
pip3 install --break-system-packages Pillow numpy
```

## Example

User: "make a challenge version of page04-alphabet.jpg"

```bash
python3 ~/.claude/skills/create-tangram-challenge/scripts/convert.py \
  /path/to/page04-alphabet.jpg
# prints: /path/to/page04-alphabet-challenge.jpg
```

Then show the output image to the user.
