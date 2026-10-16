# CSI Website: Country Intelligence

A single-page web atlas for **Cedars-Sinai International (CSI)**. It brings together CSI's draft country
profiles and Cedars-Sinai's international partnerships on one interactive world map. The page is
`index.html`; its documents, preview pages and photos are separate files in `files/`.

> **Status:** research workspace, October 2026 snapshot. All profiles are **drafts that need analyst
> review** before anyone relies on them or shares them outside CSI.

## What's inside

| | |
|---|---|
| **Country profiles (6)** | China, Egypt, India, Indonesia, Singapore, Vietnam |
| **Partnership records (20)** | Cedars-Sinai's relationships with institutions outside the US (18 Active, 2 Unclear), across 11 countries, last checked 1 October 2026 |
| **Documents (32)** | For each country: executive summary, full profile and sources list, as Word (.docx) and PDF (China and Vietnam have no executive summary) |
| **Previews** | Page images of each document, viewable in the browser without downloading |

## Features

- **World map:** drag to pan, scroll or use the + and − buttons to zoom, and "Back to world" to reset.
  Countries with a profile are highlighted.
- **Country search:** jump straight to any of 177 countries.
- **Country detail panel:** key facts, profile summary, image (with credit) and document downloads.
- **Profile library:** cards for every drafted country ("View all profiles").
- **International network:** a filterable list and map pins of Cedars-Sinai partnerships. You can search
  institutions or filter by country, relationship type and status.
- **Document preview:** a pop-up viewer for summaries, profiles and sources.
- Light and dark mode follow the device setting, and the layout adapts to phone screens.

## How to use it

No installation, build step or server is needed.

- **Locally:** download the repository (keep `index.html` and the `files/` folder together) and open
  `index.html` in a recent version of Chrome, Edge, Firefox or Safari.
- **Online:** the site is hosted on Cloudflare, which is connected to this repository. Every push to
  `main` triggers a Cloudflare build and deploy. Make changes on a branch and open a pull request so the
  Cloudflare preview can be checked before merging.

The page loads nothing from other websites. Documents, preview pages and photos are fetched from the
`files/` folder only when needed, so the map opens quickly and downloads are ordinary file links.

## How it is built

```
index.html            the page: map, code and a small DATA object (about 0.5 MB)
files/*.docx, *.pdf   the 32 documents, downloaded when a visitor clicks
files/previews/       page images for the document viewer
files/images/         country cover photos
tools/split_site.py   one-time script that moved the embedded files out of index.html
```

- All page content lives in the `DATA` object inside `index.html`:
  - `profiles`: one entry per country (facts, research sections, document list, image path, credit)
  - `partners` / `sites`: partnership records and their map positions
  - `countries`: names for search
  - `downloads`: each document's file path, type and size
  - `previews`: page-image paths for the document viewer
- **Adding a country:**
  1. Put its six documents in `files/`, its preview pages in `files/previews/` and its photo in
     `files/images/`.
  2. Add its entries to `DATA`.
  3. Open a pull request and check the Cloudflare preview.
- **Size limit:** Cloudflare's limit is 25 MiB **per file**, and the largest document is about 2.7 MB,
  so the library can keep growing.
- **Content source:** the profiles, partnership data and documents come from the CSI research pipeline in
  [`kianvargo/CedarsSinaiInternational`](https://github.com/kianvargo/CedarsSinaiInternational), which
  drafts each profile from public sources and checks it with independent verifier agents.

## Notes and caveats

- **Drafts:** every profile is a draft. The CSI assessment sections are left for CSI staff to complete.
- **Partnership statuses:**
  - **Active** means dated public evidence from the last 24 months.
  - **Unclear** means older evidence within five years.
  - Partnerships unconfirmed in public sources may be missing.
- **Images:**
  - China, Egypt, Vietnam and Indonesia photos come from Wikimedia Commons, with credits shown on the page.
  - The **Singapore image is AI-generated** (not a photograph).
  - The **India image's licensing is still under review**.
- **Public files:** every file in `files/` can be opened by anyone with the site address (unless the
  site is protected with Cloudflare Access) and is visible in this public repository.
- **Public repository:** keep CSI-internal material (patient volumes, revenue, internal contacts or the
  completed CSI assessments) out of this repo.
