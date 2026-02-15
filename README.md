# AWG Hardware Models for SPLASH

Structural integrity models for **Hardware AWG adopt-an-instrument**:

- **Centrifuges** — BioServe / NanoRacks
- **Lunar rover wheels**

## Highlights

- **Centrifuges** — stress analysis at **12,100g** (NanoRacks).
- **Rover wheels** — load and structural response under **1/6g** lunar gravity.
- Aligns with **SPLASH V1** (Kylee Brahma, Sep 2025 presentation) and subgroup sheet.
- Updated per Kylee Brahma's Sep 2025 SPLASH presentation—models support 120+ instruments with TRL 8-9 focus.

## Models

| Topic        | Path            | Description                          |
|-------------|-----------------|--------------------------------------|
| Centrifuges | [/centrifuges](/centrifuges)   | Python (SymPy) structural/stress models |
| Rover wheels| [/rover_wheels](/rover_wheels) | Python (SymPy) load/gravity models     |

## Repo structure

- **`.waylog/`** — Session context and history for this project; **included in the repo on purpose** (not local-only). Safe for tools and humans to read for background.

## Contact

- **Email:** depombo2@gmail.com  
- **Handle:** @luisdepombo
