# CSI Website: Country Intelligence

A single-page web atlas for **Cedars-Sinai International (CSI)**. It brings together CSI's draft country
profiles and Cedars-Sinai's international partnerships on one interactive world map. Everything,
including the downloadable documents, is built into one file, `index.html`.

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

- **Locally:** download `index.html` and open it in a recent version of Chrome, Edge, Firefox or Safari.
- **Online:** turn on GitHub Pages for this repository (Settings → Pages → deploy from the `main` branch,
  root folder). The site will then be at `https://kianvargo.github.io/CSI_website/`.

The page makes no network requests. The map, data, images and documents are all embedded, so it also
works offline. Downloads are stored compressed inside the page and unpacked by the browser when you
click them, which needs a modern browser that supports `DecompressionStream`.

## How it is built

- One HTML file (~45 MB) with inline CSS and JavaScript, and no external libraries.
- All content lives in a single `DATA` object inside the page:
  - `profiles`: one entry per country (facts, research sections, document list, image, credit)
  - `partners` / `sites`: partnership records and their map positions
  - `countries`: names for search
  - `downloads`: the Word/PDF files, compressed and base85-encoded
  - `previews`: page images for the document viewer
- **Content source:** the profiles, partnership data and documents come from the CSI research pipeline in
  [`kianvargo/CedarsSinaiInternational`](https://github.com/kianvargo/CedarsSinaiInternational).
  That pipeline drafts each profile from public sources and checks it with independent verifier agents.
  To update the site, regenerate the content there and rebuild this page. There is no build script in
  this repository yet.

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
- **File size:** `index.html` is about 45 MB. GitHub shows a warning for files over 50 MB and rejects
  files over 100 MB, so adding more countries may require moving the documents out of the page.
- **Public repository:** keep CSI-internal material (patient volumes, revenue, internal contacts or the
  completed CSI assessments) out of this repo.
