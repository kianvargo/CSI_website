#!/usr/bin/env python3
"""
Split the single-file Country Explorer into a small index.html plus separate files.

Before: every Word/PDF document, preview page and cover photo was embedded inside index.html,
which pushed it to ~26 MB, against Cloudflare's 25 MiB per-file limit.
After:  documents   -> files/<name>.docx|.pdf     (plain links, downloaded on click)
        previews    -> files/previews/<name>-<n>.jpg  (loaded only when shown)
        cover photos-> files/images/<Country>.jpg
        index.html keeps the map, code and a small DATA object that points at those files.

It also removes each profile's internal `resolution_log`, which the page never displays and
which should not be publicly served.

Usage (from the repository root):  python3 tools/split_site.py
Run it once on the old single-file page; it refuses to run on a page that is already split.
"""
import base64
import json
import re
import sys
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "index.html"
FILES = ROOT / "files"
MAGIC = {".pdf": b"%PDF", ".docx": b"PK\x03\x04"}

NEW_DOWNLOAD_FN = """  async function downloadDocument(id){
    const file=DATA.downloads[id];if(!file)return;
    const status=$('#atlas-download-status');
    const link=document.createElement('a');link.href=file.url;link.download=id;link.hidden=true;document.body.appendChild(link);link.click();link.remove();
    if(status)status.textContent=`Download requested: ${id}`;
  }
"""


def data_uri_to_file(uri, path):
    head, b64 = uri.split(",", 1)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(base64.b64decode(b64))
    return path.relative_to(ROOT).as_posix()


def main():
    html = PAGE.read_text(encoding="utf-8")
    start = html.index("const DATA=") + len("const DATA=")
    data, length = json.JSONDecoder().raw_decode(html[start:])
    if not any("b85" in f for f in data["downloads"].values()):
        sys.exit("index.html is already split (no embedded documents found).")

    # 1. Documents: base85 + zlib -> real files
    for name, f in data["downloads"].items():
        raw = base64.b85decode(f["b85"])
        if f.get("compressed"):
            raw = zlib.decompress(raw)
        ext = Path(name).suffix.lower()
        if ext in MAGIC and not raw.startswith(MAGIC[ext]):
            sys.exit(f"{name}: decoded bytes do not look like a {ext} file")
        out = FILES / name
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(raw)
        data["downloads"][name] = {"mime": f["mime"], "url": f"files/{name}", "bytes": len(raw)}

    # 2. Preview page images
    for name, p in data["previews"].items():
        p["pages"] = [data_uri_to_file(uri, FILES / "previews" / f"{name}-{i + 1}.jpg")
                      if uri.startswith("data:") else uri for i, uri in enumerate(p["pages"])]

    # 3. Cover photos; drop internal resolution logs
    for country, prof in data["profiles"].items():
        if prof.get("image", "").startswith("data:"):
            prof["image"] = data_uri_to_file(prof["image"], FILES / "images" / f"{country}.jpg")
        prof.pop("resolution_log", None)

    # 4. Rewrite the page: new DATA, and a download function that follows plain links
    html = html[:start] + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + html[start + length:]
    html, n = re.subn(r"  function decodeB85\(payload\)\{.*?\n  \}\n", "", html, flags=re.S)
    html, m = re.subn(r"  async function downloadDocument\(id\)\{.*?\n  \}\n", NEW_DOWNLOAD_FN, html, flags=re.S)
    if n != 1 or m != 1:
        sys.exit(f"Could not patch the download code (decodeB85: {n}, downloadDocument: {m}); page left unchanged.")
    PAGE.write_text(html, encoding="utf-8")

    sizes = sorted(((p.stat().st_size, p) for p in FILES.rglob("*") if p.is_file()), reverse=True)
    print(f"index.html: {PAGE.stat().st_size:,} bytes")
    print(f"files/: {len(sizes)} files, {sum(s for s, _ in sizes):,} bytes; largest {sizes[0][1].name} {sizes[0][0]:,} bytes")


if __name__ == "__main__":
    main()
