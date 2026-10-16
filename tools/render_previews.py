#!/usr/bin/env python3
"""
Re-render the document preview images from the PDFs in files/ at a readable resolution.

The previews originally embedded in the page were 417 x 539 px (shrunk to keep the single-file
page small), which looks fuzzy. This renders each PDF's preview pages at 150 dpi
(1275 x 1650 px for US Letter) into files/previews/<name>-<n>.jpg, keeping the same file names
and page count that index.html already references.

Usage (from the repository root):  python3 tools/render_previews.py
Requires: pip install pymupdf pillow
"""
import json
import sys
from io import BytesIO
from pathlib import Path

import pymupdf
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
DPI = 150
QUALITY = 85


def main():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    start = html.index("const DATA=") + len("const DATA=")
    data, _ = json.JSONDecoder().raw_decode(html[start:])
    total = 0
    for name, preview in data["previews"].items():
        pdf = ROOT / "files" / f"{name}.pdf"
        if not pdf.exists():
            sys.exit(f"Missing {pdf}")
        doc = pymupdf.open(pdf)
        for i, rel in enumerate(preview["pages"]):
            pix = doc[i].get_pixmap(dpi=DPI)
            img = Image.open(BytesIO(pix.tobytes("png"))).convert("RGB")
            out = ROOT / rel
            img.save(out, "JPEG", quality=QUALITY, optimize=True, progressive=True)
            total += out.stat().st_size
        print(f"{name}: {len(preview['pages'])} page(s) at {pix.width} x {pix.height}")
    print(f"Preview images total: {total:,} bytes")


if __name__ == "__main__":
    main()
