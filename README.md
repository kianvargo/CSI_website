# CSI Country Intelligence: User Guide

The **Country Explorer** is Cedars-Sinai International's interactive world map of country research.
Click a country to read a short overview and download its documents, or browse Cedars-Sinai's
international partnerships.

This page explains how to **add a new country**, **update an existing one**, and **put the results on
the website**. You don't need to know how to code: an AI assistant called **Claude** does the
technical work, and you review and approve it.

> **⚠️ Important: this page and everything stored here is public.** Anyone on the internet can see it.
> **Never** include internal CSI information: patient numbers, revenue, referral sources, contacts,
> contract terms, or a filled-in "CSI Assessment" section. Keep that only in your own private copy of a
> document.

---

## Quick start

**To add or update a country:**

1. **Ask Claude** using one of the ready-made requests in [Requests you can copy](#requests-you-can-copy).
   Claude researches the country, has its work independently fact-checked, and creates the documents.
2. **Read Claude's summary** of what it found and what it corrected, and open the documents to look them
   over.
3. **Ask Claude to put it on the website.** It prepares the change and sends you a link to review.
4. **Approve it** by clicking **Merge** on GitHub (see [How to approve a change](#how-to-approve-a-change)).
   The website updates by itself within a couple of minutes.

That's it. The rest of this page explains each step in more detail.

---

## What each country includes

Every country has **six documents**: three documents, each as a Word file and a PDF.

| Document | What's in it |
|---|---|
| **Executive summary** | About 4 pages: 8 key figures, the main takeaways, three charts, and the main risks and recent news |
| **Country profile** | About 10 pages: population, government, economy, disease patterns, the health system (public and private hospitals, spending, doctors and nurses, medical training), which foreign hospitals already work there, and recent health news |
| **Sources** | The numbered list of every source. The small numbers in the other two documents point here. |

Sections marked **[MANUAL INPUT REQUIRED]** are left empty on purpose. They are for CSI's own
information and judgment, such as patient volumes, relationships and opportunities, which the research
never fills in.

## How we make sure the research is accurate

1. **Research:** Claude gathers facts only from trustworthy public sources: governments, national
   statistics offices, the World Health Organization, the World Bank, the IMF, the institutions
   themselves and established news outlets. It never uses Wikipedia.
2. **Three independent fact-checks:** three separate fact-checkers re-check every sentence, number and
   chart. They work separately and can't see each other's notes.
3. **Corrections:** anything any of them questions is corrected to match the source, or removed, before
   the documents are made.
4. **Every fact is cited**, so a reader can check where it came from.

A few rules to know:
- **Partnerships:** the documents only list partnerships with **evidence of activity in the last two
  years**. They describe the kind of work (for example research, training or clinical affiliation)
  rather than naming every partner hospital.
- **Drafts:** everything is a **draft for review**. Someone at CSI should read it before it is relied on
  or shared outside CSI.

---

## Working with Claude

### Getting set up (once)

> 💡 **Tip:** setup is easiest with help from someone technical, done once for the team.

1. **Get a Claude account** that includes **Claude Code** (the Pro plan or higher).
2. **Connect GitHub to Claude** at https://claude.ai/connect-github. When asked which repositories Claude
   may use, choose **both** of these:
   - `kianvargo/CedarsSinaiInternational` (where the research and documents are made)
   - `kianvargo/CSI_website` (the website)
3. **Open Claude Code** at https://claude.ai/code and start a new session with
   **CedarsSinaiInternational** selected.
4. **Turn on full internet access** in the session's environment settings, so the fact-checkers can
   reach government and hospital websites.

### Requests you can copy

Copy one, replace the **bold** parts, and paste it into Claude.

**➕ Add a new country**
> Using the country-profile skill, build a full country profile for **Malaysia** with a research cutoff
> of today. Run the full process: research, three independent fact-checkers and corrections. Create the
> profile, summary and sources documents, the partnerships list and map, and a properly licensed cover
> photo. Leave every CSI section blank. Save the work, then tell me in plain language what the
> fact-checkers corrected and anything I should double-check.

**🔄 Update an existing country**
> Update the **Egypt** profile with information through today. Re-check every number, leader, policy,
> link, chart and partnership against current sources with three independent fact-checkers. Rebuild the
> documents and tell me in plain language what changed since the last version.

**🌐 Put a country on the website**
> Add **Malaysia** to the Country Explorer website (kianvargo/CSI_website) using its new documents,
> following the "For maintainers" section of the README. Test it, then send me a link to review the
> change. Don't publish it until I approve.

**🛠️ Fix how a document looks**
> In the **Indonesia** summary, **the chart on page 3 is cut off and there's a blank half page before
> Recent Developments**. Fix it so it doesn't happen in other countries either, rebuild Indonesia, and
> show me the result.

**📍 Add a Cedars-Sinai partnership to the map**
> Add Cedars-Sinai's partnership with **[hospital or university]** in **[city, country]** to the
> website's partnership map. Confirm it on Cedars-Sinai's or the partner's own website first, include the
> source, and send me a link to review the change.

**📏 Change a rule for all future countries**
> From now on, every country profile should **[describe the change, e.g. include a short paragraph on
> medical tourism]**. Write the new rule into the instructions and the README so it's never lost, try it
> on one existing country, and send me links to review.

**❓ Check what's on the site**
> What's currently on the Country Explorer? List each country, its date, whether all six documents are
> available, and any known problems.

### What to expect

- **Time:** a new country takes about **45 to 90 minutes**. Updates and website changes are quicker.
- **Plan usage:** a new country uses a large share of a Pro plan's usage, roughly a third or more of a
  5-hour window. If you run out partway through, wait for it to reset and ask Claude to continue. Its
  work is saved as it goes.
- **Don't interrupt** while Claude says its fact-checkers are running, because sending a new message can
  stop them.

### Tips

- **Ask for one country or one change at a time.**
- **Always ask Claude to "send me a link to review"** rather than publishing directly.
- **Ask what Claude couldn't verify.** It will tell you about weak or missing sources.
- **Never paste internal CSI information into Claude for this project.** It could end up in public files.
- **Changing how things should work?** Ask Claude to write the new rule into the instructions and this
  README. Anything agreed only in a chat is forgotten when the chat ends.

---

## How to approve a change

When Claude finishes a website change, it sends you a link to a **pull request**, which is a proposed
change waiting for approval.

1. **Open the link.** You'll see a description of what changed.
2. **Check the "Files changed" tab** if you want to see exactly what was changed.
3. **Approve it:** click the green **Merge pull request** button, then **Confirm merge**.
4. **Wait about two minutes**, then open the website and check your country. If you don't see the
   change, press **Ctrl+Shift+R** (Windows) or **Cmd+Shift+R** (Mac) to refresh.

> **You may see a red ✗ next to "Workers Builds" on the link.** That's a known setup issue with test
> previews and doesn't mean anything is wrong with the change.

**Made a mistake?** Open the same link and click **Revert**, then merge the revert. The website goes back
to how it was within minutes.

---

## What's on the site now (October 2026)

| Country | Updated | Documents |
|---|---|---|
| China | Sep 2026 | Profile and sources (no summary yet) |
| Egypt | Oct 2026 | All six |
| India | Sep 2026 | All six |
| Indonesia | Oct 2026 | All six |
| Singapore | Oct 2026 | All six |
| Vietnam | Sep 2026 | Profile and sources (no summary yet) |

**Partnership map:** 20 Cedars-Sinai partnerships in 11 countries, last checked 1 October 2026.

**Known issues:**
- **Images to replace:** Singapore's cover image is AI-generated, and India's photo rights are still
  being checked. Replace both before formal distribution.
- **China and Vietnam:** they were made with an older process and need a full update.
- **New-country style:** new countries made today use a slightly older document style than Singapore
  and Indonesia, until the newer styling tools are added. See "For maintainers".

---

## Words you might see

| Word | Meaning |
|---|---|
| **Repository (repo)** | A shared project folder on GitHub. There are two: one makes the documents, one is the website. |
| **GitHub** | The website where these project folders are stored. |
| **Pull request** | A proposed change, waiting for someone to review and approve it. |
| **Merge** | Approving a pull request, so the change takes effect. |
| **Revert** | Undoing a change that was merged. |
| **Branch** | A separate working copy where changes are prepared before they're approved. |
| **Cloudflare** | The service that runs the website. It updates by itself when a change is merged. |
| **Claude Code** | The version of Claude that can work directly on these project folders. |

---

## For maintainers (technical details)

*Most people can skip this section. It's for whoever maintains the tools, and for Claude.*

### The two repositories

| Repository | Holds |
|---|---|
| [`kianvargo/CedarsSinaiInternational`](https://github.com/kianvargo/CedarsSinaiInternational) (pipeline) | Research process (`.claude/skills/country-profile/SKILL.md`), scripts, data and generated documents |
| [`kianvargo/CSI_website`](https://github.com/kianvargo/CSI_website) (website) | `index.html`, `files/` (documents), `files/previews/`, `files/images/`, `tools/` |

### Making a country manually (pipeline)

Requires Python 3.11+.

```
git clone https://github.com/kianvargo/CedarsSinaiInternational && cd CedarsSinaiInternational
pip install python-docx matplotlib openpyxl Pillow
python3 scripts/tracker.py brief <Country> work/<country>/<country>_tracker_brief.json
python3 scripts/fetch_cover_photo.py <Country>            # licensed photos only; saves the credit
# Research, three independent checks and resolution are run by Claude Code per SKILL.md,
# producing output/<country>_profile.json and work/<country>/tracker_final.json.
python3 scripts/tracker.py import <Country> work/<country>/tracker_final.json YYYY-MM-DD
python3 scripts/tracker.py export
python3 scripts/make_partner_map.py <Country> output/<Country>_partnerships_map.png   # needs data/<country>_partner_locations.json
python3 scripts/generate_profile.py output/<country>_profile.json output/<Country>_Profile_DRAFT.docx
python3 scripts/generate_summary.py output/<country>_profile.json output/<country>_summary.json output/<Country>_Summary_DRAFT.docx
python3 scripts/package.py <Country>
```

To make the PDFs, open each .docx in Word, click **Yes** to update fields (this fills in the table of
contents page numbers), then **Save As → PDF** with the same name.

**Rules** (full list in SKILL.md):
- **Sources:** every factual sentence is cited from a source actually read, and no Wikipedia.
- **Partnerships:** Active means dated evidence within 24 months; only Active partnerships appear in the
  documents, by nature of work.
- **Charts:** line charts need at least 6 points and bar charts at least 5.
- **Style:** no em or en dashes, American spelling.
- **CSI fields** stay blank.

**Gap:** the branded layout and PDF export used for the current site documents
(`build_country_publication.py`, `publication_layout.py`, `validate_publication.py`) are not yet in
the pipeline repo, so new countries currently get the earlier layout.

### Adding a country to the website

1. **Files:**
   - Put the six documents in `files/` (`<Country>_Summary_DRAFT`, `<Country>_Profile_DRAFT` and
     `<Country>_Profile_DRAFT_SOURCES`, each as `.docx` and `.pdf`).
   - Put the cover photo in `files/images/<Country>.jpg`.
2. **Data:** in `index.html`, inside `const DATA=`, copy an existing country (Egypt or Indonesia) and edit:
   - `profiles["<Country>"]`: `country`, `code`, `region`, `generated_date`, `dateLabel`, short `facts`,
     `research` (from the pipeline's profile JSON **without** `resolution_log`), `image`, `imageAlt`,
     `credit`, `documents` (with file sizes in bytes).
   - `downloads["<file>"]`: `{"mime", "url": "files/<file>", "bytes"}` for each of the six.
   - `previews["<Country>_<Doc>_DRAFT"]`: `pages` (image paths), `count` (PDF page count).
   - `partners` / `sites` (Cedars-Sinai pins only): `lat`/`lon` plus map `x`/`y` consistent with the
     existing pins.
   - The country name must match the map's name exactly.
3. **Previews:** `pip install pymupdf pillow && python3 tools/render_previews.py`
4. **Test:** `python3 -m http.server 8000`, open http://localhost:8000, and check:
   - the new country, all six downloads and the preview;
   - one other country.
5. **Safety check, then a pull request to `main`.** Check for filled CSI fields, internal data,
   `resolution_log` and unlicensed photos. Cloudflare deploys `main` on merge, with a 25 MiB limit per
   file.

**Known issue:** Cloudflare builds of branches other than `main` fail, so pull-request previews don't
work. Fix this in the Cloudflare dashboard (csi-website → Settings → Build).

**Tools:**
- `tools/render_previews.py` re-renders previews from the PDFs.
- `tools/split_site.py` is the one-time script that moved the documents out of `index.html`. It doesn't
  need to be run again.
