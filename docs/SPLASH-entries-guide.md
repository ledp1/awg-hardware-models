# Creating and updating SPLASH entries for centrifuges

This repo contains **all data needed** to create or update SPLASH entries for the four ISS centrifuges (BioServe MiniSpin, BioLab, CBEF, Rhodium VGS). Use this guide to know where everything lives and how to add or edit entries.

## What’s in the repo

| Asset | Purpose |
|-------|--------|
| **centrifuges/{name}/SPLASH_entry.md** | **Canonical SPLASH entry** — full structured text (General, Specifications, Research, Logistics, Structural Models). Use this as the main source when submitting or updating an entry in SPLASH. |
| **splash_data.json** | Machine-readable list of all four centrifuges with the same SPLASH-oriented fields. Use for scripts, bulk import, or form-fill. |
| **splash_data/*.md** | One Markdown table per centrifuge (Field \| Value). Same content as the canonical entries in table form. |
| **splash_entries/*.md** | Alternate SPLASH-formatted templates; useful as copy-paste starting points. |
| **centrifuges/{name}/splash_summary.md** | Short summary per centrifuge; points to `stress_analysis.py` in that folder. |
| **centrifuges/{name}/stress_analysis.py** | Structural models (e.g. hoop stress, max g-load); linked from SPLASH_entry.md. |

## Updating an existing centrifuge entry

1. **Edit the canonical entry**  
   - Open **centrifuges/{name}/SPLASH_entry.md** (e.g. `centrifuges/bio_serve_minispin/SPLASH_entry.md`).
   - Update the sections (General, Specifications, Research, Logistics) with the new or corrected data.

2. **Optional: keep other assets in sync**  
   - **splash_data.json** — update the object for that instrument so JSON stays accurate for tools/import.  
   - **splash_data/{name}.md** — update the table if you use it for reference or export.  
   - **splash_entries/*.md** — update the matching template if you want it to stay aligned.

3. **Structural models**  
   - If you change centrifuge parameters (e.g. max g, radius), consider updating **centrifuges/{name}/stress_analysis.py** and ensure **SPLASH_entry.md** still links to it under “Structural Models”.

## Adding a new centrifuge

1. **Create a folder**  
   - `centrifuges/{short_name}/` (e.g. `centrifuges/new_centrifuge/`).

2. **Add the canonical SPLASH entry**  
   - Create **centrifuges/{short_name}/SPLASH_entry.md** using the same structure as the existing entries (General, Specifications, Research, Logistics, Structural Models).  
   - You can copy **centrifuges/bio_serve_minispin/SPLASH_entry.md** and replace the content with the new centrifuge’s data.

3. **Add structural model (if applicable)**  
   - Add **centrifuges/{short_name}/stress_analysis.py** (e.g. copy from another centrifuge and adapt).  
   - In **SPLASH_entry.md**, under “Structural Models”, link to `stress_analysis.py` in the same folder (e.g. `[stress_analysis.py](./stress_analysis.py)`).

4. **Add summary and metadata**  
   - Create **centrifuges/{short_name}/splash_summary.md** (see existing `splash_summary.md` files for format).  
   - Add **splash_data/{short_name}.md** with the same Field \| Value table as other centrifuges.  
   - Add **splash_entries/Display_Name.md** if you want a top-level template.

5. **Update repo-wide files**  
   - **README.md** — add a row to the “Ready for SPLASH Import” table and, if you use it, to the “SPLASH entry templates” table.  
   - **splash_data.json** — add a new object to the `instruments` array with the same field names as the existing entries. Use `"TBD"` for unknown values.

## Field names and “TBD”

- **splash_data.json** uses snake_case keys (e.g. `centrifuge_performance`, `crew_handling_required`).  
- **SPLASH_entry.md** and **splash_data/*.md** use the same concepts with human-readable labels.  
- Where official specs are missing, use **TBD** in the JSON and “TBD” or “Per [agency] documentation” in the Markdown so submitters know what still needs to be filled from primary sources.

## Quick reference: centrifuge ↔ paths

| Centrifuge | Folder | SPLASH_entry.md |
|------------|--------|------------------|
| BioServe MiniSpin | centrifuges/bio_serve_minispin | centrifuges/bio_serve_minispin/SPLASH_entry.md |
| BioLab (ESA) | centrifuges/biolab | centrifuges/biolab/SPLASH_entry.md |
| CBEF (JAXA) | centrifuges/cbef | centrifuges/cbef/SPLASH_entry.md |
| Rhodium VGS | centrifuges/rhodium_vgs | centrifuges/rhodium_vgs/SPLASH_entry.md |

For more on session history and repo layout, see [session-context.md](session-context.md).
