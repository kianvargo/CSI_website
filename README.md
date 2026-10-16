# CSI Country Intelligence: User Guide

This repository is the **Cedars-Sinai International (CSI) Country Explorer**: an interactive world map
with CSI's country profiles, document downloads and Cedars-Sinai's international partnerships. It is
hosted on Cloudflare, and every change merged into `main` goes live automatically.

This README is the single guide for the whole process:

| Part | Use it to |
|---|---|
| [Part 1: Create or update a country profile](#part-1-create-or-update-a-country-profile) | Research and build a new country's documents, or refresh an existing country |
| [Part 2: Publish to the website](#part-2-publish-new-or-updated-files-to-the-website) | Put new or updated documents on the live site |
| [Part 3: Working with Claude](#part-3-working-with-claude) | Have Claude do Parts 1 and 2 for you, change the process, or fix problems |

> **Before you start: this repository is public.** Anyone on the internet can read everything in it,
> including old versions. Never put CSI-internal information here: patient volumes, revenue, referral
> sources, contacts, contract terms, or filled-in "CSI Assessment" sections. Those belong only in your
> private copy of a document, never on GitHub or the website.

---

## The two repositories

| Repository | What it holds |
|---|---|
| [`kianvargo/CedarsSinaiInternational`](https://github.com/kianvargo/CedarsSinaiInternational) (the **pipeline**) | The research process, scripts and data that **produce** country documents. Part 1 happens here. |
| [`kianvargo/CSI_website`](https://github.com/kianvargo/CSI_website) (this repository, the **website**) | The finished documents and the page that **displays** them. Part 2 happens here. |

Each country package has six files: an **executive summary**, a **full profile** and a **sources list**,
each as Word (`.docx`) and PDF.

---

## Part 1: Create or update a country profile

### What you get

For each country, the pipeline produces:
- **`<Country>_Profile_DRAFT.docx`:** a full profile of about 2,400 to 2,700 words. It has a cover with a
  landmark photo and table of contents; then country overview, health system (public, private,
  financing, workforce, education, outlook), competitive landscape and recent developments; and finally
  blank CSI Assessment fields.
- **`<Country>_Summary_DRAFT.docx`:** a 4-page executive summary with 8 key figures, takeaways and three
  charts, plus blank CSI-partnership and opportunity prompts.
- **`<Country>_Profile_DRAFT_SOURCES.docx`:** numbered sources. The superscript numbers in both
  documents point here.
- **An entry in the partnerships tracker:** foreign health systems working in the country, and a map of
  where they work.

### How the research is checked

Every profile goes through the same quality process. It is described in full in the pipeline's
[`.claude/skills/country-profile/SKILL.md`](https://github.com/kianvargo/CedarsSinaiInternational/blob/main/.claude/skills/country-profile/SKILL.md).

1. **Research:** AI research agents gather public facts. Each one is tied to a source the agent actually
   read: governments, national statistics offices, WHO, World Bank, IMF, the institutions themselves and
   established news. No Wikipedia.
2. **Three independent checks:** three separate checker agents verify every sentence, number, chart
   value and partnership against the sources. They cannot see each other's work.
3. **Resolution:** anything flagged is corrected to what the source says, or deleted, before the
   documents are built. The fixes are made in the text itself, with no "verification notes" page.
4. **Build:** scripts turn the checked research into the Word documents, charts and map.

**House rules every profile follows:**
- **Citations:** every factual sentence is cited, and nothing is invented.
- **Style:** American spelling, no em or en dashes, short quick-fact values.
- **Partnerships:** only **confirmed-active** partnerships appear in the documents, meaning dated evidence
  from the last 24 months. They are shown by the *kind* of work (research, training, clinical
  affiliation, and so on), not the partner hospital's name.
- **Charts:** a line chart needs at least 6 data points and a bar chart at least 5.
- **CSI sections:** CSI Assessment, CSI partnerships and opportunities are always left blank as
  `[MANUAL INPUT REQUIRED]`.

### Steps

The easiest way is to ask Claude to do all of this (see [Part 3](#part-3-working-with-claude)). The manual
steps, for reference:

1. **Get the pipeline**
   ```
   git clone https://github.com/kianvargo/CedarsSinaiInternational
   cd CedarsSinaiInternational
   pip install python-docx matplotlib openpyxl Pillow
   ```
   You need Python 3.11 or later and an internet connection.
2. **Start a work folder and briefs**
   ```
   python3 scripts/tracker.py brief <Country> work/<country>/<country>_tracker_brief.json
   python3 scripts/fetch_cover_photo.py <Country>          # or --landmark "Petronas Towers"
   ```
   `fetch_cover_photo.py` only accepts photos that are licensed for reuse, and it saves the credit line.
3. **Research, check and resolve**
   This is done by AI agents (Claude Code), following `SKILL.md`. It produces
   `output/<country>_profile.json` and the country's partnership records.
4. **Record the partnerships and draw the map**
   ```
   python3 scripts/tracker.py import <Country> work/<country>/tracker_final.json YYYY-MM-DD
   python3 scripts/tracker.py export
   python3 scripts/make_partner_map.py <Country> output/<Country>_partnerships_map.png
   ```
   The map needs a small city file, `data/<country>_partner_locations.json`. See
   `data/egypt_partner_locations.json` for an example.
5. **Build the documents**
   ```
   python3 scripts/generate_profile.py output/<country>_profile.json output/<Country>_Profile_DRAFT.docx
   python3 scripts/generate_summary.py output/<country>_profile.json output/<country>_summary.json output/<Country>_Summary_DRAFT.docx
   python3 scripts/package.py <Country>
   ```
   The documents land in `output/`, and a zip package in `deliverables/<Country>/`.
6. **Make the PDFs**
   Open each of the three Word documents. When Word asks to update fields, click **Yes**; this fills in
   the page numbers in the table of contents. Then **File → Save As → PDF**, keeping the same file name.
   Check every page.

### Updating an existing country

Use the same steps, starting from the country's existing `output/<country>_profile.json`. Re-check
**every** dated figure, leader, policy, link, chart value, photo credit and partnership status.
Changing only the date on the cover is not an update.

### Known gaps in the pipeline (October 2026)

- **Branded layout:** the documents currently on this website use a newer branded layout (Cedars-Sinai
  International logo header, Arial, red `#DC1E34`) and were exported to PDF with scripts that are **not
  yet in the pipeline repository**. Those scripts include `build_country_publication.py`,
  `publication_layout.py` and `validate_publication.py`. The pipeline on GitHub produces the earlier
  layout. Until those scripts are added, new countries will not exactly match Singapore and Indonesia.
- **China and Vietnam:** these predate the full checking process and have no executive summary.
- **Images to replace:** Singapore's cover image is AI-generated, and India's image licensing is still
  under review. Replace both before formal distribution.

---

## Part 2: Publish new or updated files to the website

### How the website is put together

```
index.html             the page: map, code and the DATA object that lists every country
files/                 all documents (.docx and .pdf)
files/previews/        page images shown in the document viewer
files/images/          country cover photos
tools/                 helper scripts (see below)
```

Cloudflare builds the site from `main`. **Merging a change into `main` makes it live within a couple of
minutes.** Each file may be at most 25 MiB, which is not a concern for normal documents (the largest is
about 2.7 MB).

### Steps to add or update a country

1. **Create a branch.** On GitHub use the branch menu, or on your computer:
   ```
   git clone https://github.com/kianvargo/CSI_website && cd CSI_website
   git checkout -b add-<country>
   ```
2. **Add the files**
   - Six documents in `files/`, named exactly like the existing ones:
     `<Country>_Summary_DRAFT.docx` and `.pdf`, `<Country>_Profile_DRAFT.docx` and `.pdf`,
     `<Country>_Profile_DRAFT_SOURCES.docx` and `.pdf`.
   - The cover photo as `files/images/<Country>.jpg`.
   - For an update, replace the old files with the same names.
3. **Add or update the country in `index.html`.** Inside `const DATA=` there are entries to add or edit.
   Copy an existing country (Egypt or Indonesia are good models) and change its contents:

   | Part of `DATA` | What to put there |
   |---|---|
   | `profiles["<Country>"]` | `country`, `code` (two-letter, e.g. `MY`), `region`, `generated_date`, `dateLabel` (e.g. `Nov 2026`), short `facts`, the `research` section from `output/<country>_profile.json` **without** `resolution_log`, `image` (`files/images/<Country>.jpg`), `imageAlt`, `credit`, and `documents` (the six files with their sizes in bytes) |
   | `downloads["<file name>"]` | One entry per document: `{"mime": ..., "url": "files/<file name>", "bytes": ...}` |
   | `previews["<Country>_Profile_DRAFT"]` (and Summary, Sources) | `pages`: the preview image paths; `count`: total pages in the PDF |
   | `partners` / `sites` | Only if Cedars-Sinai itself has a new or changed partnership there. Pins need `lat`/`lon` and map `x`/`y` positions consistent with the existing pins. |

   The country's name must match the map's country name exactly (for example `"United Arab Emirates"`).
4. **Make the preview images** from the PDFs:
   ```
   pip install pymupdf pillow
   python3 tools/render_previews.py
   ```
5. **Test on your computer**
   ```
   python3 -m http.server 8000
   ```
   Open http://localhost:8000. Check that the new country is highlighted, its card and photo show, all
   **six downloads** work, the preview opens, and at least one other country still works.
6. **Safety check before committing:** no filled-in CSI fields, no internal data, no `resolution_log`,
   and photos with usable rights and a credit line.
7. **Commit, push and open a pull request** to `main`. Describe what changed and what you tested.
8. **Review and merge.** Once a reviewer approves, click **Merge**, and Cloudflare deploys it. Then open
   the live site and test the new country again.

**If something goes wrong after merging:** open the merged pull request on GitHub and click **Revert**,
then merge the revert. The previous version comes back within minutes.

> **Known issue:** Cloudflare's automatic *preview* build fails for every branch except `main`, so pull
> requests show a failed "Workers Builds" check. That is a setup problem, not a sign your change is
> broken. Test locally (step 5) instead. The fix is in the Cloudflare dashboard (csi-website → Settings →
> Build); the build log behind the "View logs" link on any pull request shows the error.

### Tools in this repository

| Script | What it does |
|---|---|
| `tools/render_previews.py` | Renders the preview images from the PDFs at a readable resolution. Run it after adding or replacing PDFs. |
| `tools/split_site.py` | One-time script that moved the documents out of `index.html` into `files/`. Kept for the record; it does not need to be run again. |

---

## Part 3: Working with Claude

Claude Code can do Parts 1 and 2 for you: research, checking, building the documents, updating the
website and opening the pull request. You review the result and merge.

### One-time setup

1. **Claude account:** use a Claude plan that includes Claude Code (Pro or higher).
2. **Connect GitHub:** at https://claude.ai/connect-github, connect your GitHub account and make sure the
   Claude GitHub App has access to **both** repositories. Claude can read public repositories without
   it, but it **cannot push changes** unless the app is installed on that repository.
3. **Start a session:** open Claude Code (https://claude.ai/code) and start a session with
   `CedarsSinaiInternational` selected. Mention `CSI_website` in your request, and Claude can attach it.
4. **Network access:** in the environment settings, give the session **full network access**. The research
   checkers must be able to open government and institutional websites.

### Costs and timing

- **Usage:** a full new country (research, three checkers, resolution, documents) uses a large share of a
  Pro plan's usage limit, roughly a third or more of a 5-hour window. Updates and website changes cost
  far less.
- **Time:** expect about 45 to 90 minutes for a new country.
- **Interruptions:** don't send new messages while the research and checking agents are running, because
  interrupting can stop them. If usage runs out mid-run, ask Claude to resume. The work in progress is
  saved in files.

### Prompts you can copy

**Create a new country**
> Using the country-profile skill in CedarsSinaiInternational, build a full country profile for
> **Malaysia** with a research cutoff of today. Run the full process: research, three independent
> checkers and resolution. Then build the profile, summary and sources documents, the partnerships
> tracker entry and the map, and fetch a licensed cover photo. Leave every CSI field blank. Commit and
> push the pipeline changes, then tell me what the checkers changed and anything I should spot-check.

**Update an existing country**
> Refresh the **Egypt** profile through today using the country-profile skill. Re-check every dated
> statistic, leader, policy, link, chart value and partnership status against current sources with three
> independent checkers. Rebuild the documents and tell me exactly what changed since the last version.

**Publish to the website**
> In kianvargo/CSI_website, add **Malaysia** to the Country Explorer using the new documents from
> CedarsSinaiInternational. Follow Part 2 of the README: add the six files and cover photo, add the
> country to DATA (without resolution_log), render the previews, and test locally. Open a pull request
> to main, and don't merge until I say so.

**Fix layout or formatting**
> In the **Indonesia** summary, the chart on page 3 is cut off and there's a blank half page before
> Recent Developments. Fix it in the generator so it doesn't happen for other countries either, rebuild
> Indonesia, and show me the result.

**Add or correct a Cedars-Sinai partnership pin**
> Add Cedars-Sinai's partnership with **[institution]** in **[city, country]** to the website's partner
> list and map. Verify it on Cedars-Sinai's or the partner's own website first, include the source and
> date, and place the pin consistently with the existing pins. Open a pull request.

**Change a rule for all future profiles**
> From now on, profiles should **[new rule, e.g. include a one-paragraph medical tourism section]**.
> Update SKILL.md, the generators and this README so the rule is written down, test it on one existing
> country, and open pull requests in both repositories.

**Check status or ask questions**
> What is the current state of the Country Explorer? List every country with its date, whether all six
> documents are on the site, and any known problems.

### Tips for good results

- **Ask for one country or one change at a time.**
- **Ask for pull requests** rather than direct pushes to `main`, and **review before merging**. Claude can
  merge for you once you say so.
- **Ask Claude what it changed and what it couldn't verify.** It will list the checkers' corrections and
  any weak sources.
- **Never paste internal CSI data into a prompt for these repositories.** Claude may write it into files
  that become public.
- **Keep the rules written down:** if you change a rule in conversation, ask Claude to add it to
  `SKILL.md` and this README. Rules that exist only in a chat are lost when the session ends.
- **Use this README as Claude's map:** if a session seems confused, tell Claude to read this README and
  `SKILL.md` first.

---

## What's on the site now (October 2026)

| Country | Date | Documents on site |
|---|---|---|
| China | Sep 2026 | Profile, sources (older process, no summary) |
| Egypt | Oct 2026 | All six |
| India | Sep 2026 | All six |
| Indonesia | Oct 2026 | All six |
| Singapore | Oct 2026 | All six |
| Vietnam | Sep 2026 | Profile, sources (older process, no summary) |

Partnerships: 20 Cedars-Sinai records (18 Active, 2 Unclear) across 11 countries, last checked
1 October 2026. All profiles are **drafts that need analyst review** before they are relied on or shared
outside CSI.
