#!/usr/bin/env python3
"""Convert a colorful tangram image into a black-and-white challenge silhouette."""

import sys
from pathlib import Path
from PIL import Image, ImageFilter
import numpy as np


def convert(src: Path, dst: Path) -> None:
    img = Image.open(src).convert("RGB")
    img = img.filter(ImageFilter.MedianFilter(size=3))   # kill JPEG artifacts
    arr = np.array(img)

    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    is_white = (r > 210) & (g > 210) & (b > 210)

    mask = np.where(is_white, np.uint8(255), np.uint8(0))
    m = Image.fromarray(mask, mode="L")
    m = m.filter(ImageFilter.GaussianBlur(radius=1))     # smooth staircase edges
    final = np.where(np.array(m) > 128, np.uint8(255), np.uint8(0))

    rgb = np.stack([final, final, final], axis=-1)
    Image.fromarray(rgb).save(dst, quality=95)


def challenge_path(src: Path) -> Path:
    return src.with_stem(src.stem + "-challenge")


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <image> [output]")
        sys.exit(1)

    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else challenge_path(src)

    if not src.exists():
        print(f"File not found: {src}", file=sys.stderr)
        sys.exit(1)

    convert(src, dst)
    print(dst)


if __name__ == "__main__":
    main()
