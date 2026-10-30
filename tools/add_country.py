#!/usr/bin/env python3
"""
Add (or refresh) a country on the site from the profile pipeline's finished files.

Usage (from the repository root, with kianvargo/CedarsSinaiInternational cloned next to it or
at --pipeline):
  python3 tools/add_country.py "New Zealand" NZ Oceania "Mitre Peak, Milford Sound" [--pipeline PATH]

Reads   <pipeline>/output/<country>_profile.json, <pipeline>/output/<Country>_{Summary,Profile,
        Profile_SOURCES}_DRAFT.{docx,pdf} and <pipeline>/assets/covers/<Country>.{jpg,json}.
Writes  files/<Web_Name>_*.{docx,pdf}, files/images/<Web_Name>.jpg (600 px wide) and the
        DATA entry in index.html (profiles, downloads, previews). File names use underscores
        for spaces. Then run tools/render_previews.py to draw the preview images.
DATA stays a single-line JSON literal after `const DATA=`.
"""
import json
import re
import shutil
import sys
from pathlib import Path

import pymupdf
from PIL import Image

SITE = Path(__file__).resolve().parent.parent
args = [a for a in sys.argv[1:]]
pipeline = SITE.parent / 'CedarsSinaiInternational'
if '--pipeline' in args:
    i = args.index('--pipeline'); pipeline = Path(args[i + 1]); del args[i:i + 2]
if len(args) != 4:
    sys.exit(__doc__)
C, CODE, REGION, ALT = args
W = C.replace(' ', '_')
key = C.lower().replace(' ', '_')
DOCX = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'

html = (SITE / 'index.html').read_text(encoding='utf-8')
start = html.index('const DATA=') + len('const DATA=')
D, end = json.JSONDecoder().raw_decode(html[start:])

prof = json.loads((pipeline / f'output/{key}_profile.json').read_text())
strip = lambda s: re.sub(r'\{\{[^}]+\}\}', '', s).strip()
facts = [{'label': f['label'], 'value': strip(f['value'])} for f in prof['research']['country_overview']['demographics']['facts']]
credit = json.loads((pipeline / f'assets/covers/{C}.json').read_text())['credit']

im = Image.open(pipeline / f'assets/covers/{C}.jpg').convert('RGB')
im = im.resize((600, round(600 * im.height / im.width)), Image.LANCZOS)
im.save(SITE / f'files/images/{W}.jpg', 'JPEG', quality=85, optimize=True, progressive=True)

docs = []
for kind, label, suffix in [('summary', 'Executive summary', 'Summary_DRAFT'),
                            ('profile', 'Country profile', 'Profile_DRAFT'),
                            ('sources', 'Sources', 'Profile_DRAFT_SOURCES')]:
    base, files = f'{W}_{suffix}', []
    for ext, fmt, mime in [('docx', 'Word', DOCX), ('pdf', 'PDF', 'application/pdf')]:
        name = f'{base}.{ext}'
        shutil.copy(pipeline / 'output' / f'{C}_{suffix}.{ext}', SITE / 'files' / name)
        size = (SITE / 'files' / name).stat().st_size
        files.append({'id': name, 'format': fmt, 'bytes': size})
        D['downloads'][name] = {'mime': mime, 'url': f'files/{name}', 'bytes': size}
    docs.append({'kind': kind, 'label': label, 'files': files})
    pages = pymupdf.open(SITE / 'files' / f'{base}.pdf').page_count
    D['previews'][base] = {'pages': [f'files/previews/{base}-{i}.jpg' for i in (1, 2)], 'count': pages}

D['profiles'][C] = {
    'country': C, 'code': CODE, 'region': REGION, 'generated_date': prof['generated_date'],
    'dateLabel': __import__('datetime').date.fromisoformat(prof['generated_date']).strftime('%b %Y'),
    'facts': facts, 'research': prof['research'], 'image': f'files/images/{W}.jpg',
    'credit': credit, 'imageAlt': ALT, 'documents': docs}
if C not in D['countries']:
    print(f'Note: "{C}" is not a map country name; the profile card works but the map cannot highlight it.')
html = html[:start] + json.dumps(D, ensure_ascii=False, separators=(',', ':')) + html[start + end:]
(SITE / 'index.html').write_text(html, encoding='utf-8')
print(f'{C}: {len(facts)} facts, documents', [(d['kind'], [f['bytes'] for f in d['files']]) for d in docs])
