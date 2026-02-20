# AWG Hardware Models for SPLASH (BioServe MiniSpin + BioLab + CBEF + Rhodium VGS + lunar rover wheels)

## Ready for SPLASH Import

| Centrifuge | SPLASH entry |
|------------|--------------|
| BioServe MiniSpin | [centrifuges/bio_serve_minispin/SPLASH_entry.md](centrifuges/bio_serve_minispin/SPLASH_entry.md) |
| BioLab (ESA) | [centrifuges/biolab/SPLASH_entry.md](centrifuges/biolab/SPLASH_entry.md) |
| CBEF (JAXA) | [centrifuges/cbef/SPLASH_entry.md](centrifuges/cbef/SPLASH_entry.md) |
| Rhodium VGS | [centrifuges/rhodium_vgs/SPLASH_entry.md](centrifuges/rhodium_vgs/SPLASH_entry.md) |

## SPLASH entry templates (ISS centrifuges)

| Centrifuge | Template |
|------------|----------|
| BioServe MiniSpin | [splash_entries/BioServe_MiniSpin.md](splash_entries/BioServe_MiniSpin.md) |
| BioLab (ESA) | [splash_entries/BioLab.md](splash_entries/BioLab.md) |
| CBEF (JAXA) | [splash_entries/CBEF.md](splash_entries/CBEF.md) |
| Rhodium VGS | [splash_entries/Rhodium_VGS.md](splash_entries/Rhodium_VGS.md) |

Structural integrity models for **Hardware AWG adopt-an-instrument**. Includes full SPLASH-compatible metadata tables + structural models. This repo contains complete SPLASH-ready entry templates + structural models for all 4 active ISS centrifuges.

- **Centrifuges**
  - **Active ISS centrifuges:** BioServe MiniSpin, Rhodium VGS
  - BioServe MiniSpin (current ISS)
  - BioLab (ESA) on ISS Columbus
  - JAXA CBEF on ISS Kibo
  - Rhodium VGS (current ISS, variable 0-1g)
- **Rover wheels**

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

- **`.waylog/`** — Session context and history; **included in the repo on purpose** (not local-only). If a tool says ".waylog does not exist (404)", it may be skipping dot-paths: the folder is at [tree/main/.waylog](https://github.com/ledp1/awg-hardware-models/tree/main/.waylog). See **[docs/session-context.md](docs/session-context.md)** for working URLs and a short summary.

## Contact

- **Email:** depombo2@gmail.com  
- **X:** @luisdepombo
