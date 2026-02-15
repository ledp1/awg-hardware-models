# Session context (waylog)

Session and chat history for this project is stored in **`.waylog/history/`** in this repo.

Some tools (e.g. Supergrok) may report "404" or "does not exist" for paths starting with `.` even though the folder is present. On GitHub it is at:

- **Directory:** [.waylog](https://github.com/ledp1/awg-hardware-models/tree/main/.waylog)
- **History folder:** [.waylog/history](https://github.com/ledp1/awg-hardware-models/tree/main/.waylog/history)

Use **`tree/main/.waylog`** (not `blob`). The markdown file(s) under `.waylog/history/` contain the full session export (WayLog from Cursor).

## Summary for indexers

- **AWG Hardware Models for SPLASH:** Structural integrity models for adopt-an-instrument (centrifuges: BioServe/NanoRacks; lunar rover wheels). Centrifuges stress at 12,100g; rover wheels under 1/6g. Aligns with SPLASH V1 (Kylee Brahma Sep 2025). Python (SymPy) in `centrifuges/` and `rover_wheels/`.
