# Cell Biology Experiment Facility (CBEF) — SPLASH Entry

## General
- **Operations:** GROUND TELEMETRY + CREW INSTALLATION
- **Category:** Experiment Hosting Facilities with Centrifuges
- **Operator/Vendor:** JAXA / MHI (Mitsubishi Heavy Industries)
- **Status:** Active
- **Flight Heritage:** JEM Pressurized Module (Kibo), ISS; launched 2008 (Space Shuttle)

## Specifications
- **Mass:** TBD (per JAXA/Kibo payload documentation)
- **Size:** Rack-mounted; incubator with µG and 1G compartments
- **Power:** TBD (per JEM rack); canister: DC +5 V, +12 V, ±15 V
- **Centrifuge Performance:** 0.1–2.0 G at 112.5 mm radius; 20–140 rpm (1 rpm steps)
- **Temperature Range:** 15°C–40°C (±1°C distribution, 0.1°C steps)
- **Payload Volume Required:** 6 medium canisters (µG) + 4 medium canisters (1G)
- **Interface Definitions:** Standard medium canister (power, analog, video, command per JEM spec)
- **Radiation Sensitivity:** Standard ISS
- **Heat Sink Required:** Facility thermal control

## Research
- **Supported Specimen Types:** Cells, plants, small animals (life science cultivation)
- **Specimen Size/Quantity:** 6 medium canisters (µG) + 4 (1G); BEU-compatible
- **Temperature Range at Sample:** 15°C–40°C (±1°C, 0.1°C steps)
- **Experiment Duration:** User-defined; long-term cultivation supported
- **Centrifuge:** Yes (0.1–2.0 G at 112.5 mm; 20–140 rpm)
- **Imaging:** Video interface per standard JEM video specification
- **Key Applications:** Gravity contrast (µG vs 0.1–2 G); BEU standard canister

## Logistics
- **Crew Handling Required:** Yes (install/remove canisters)
- **Crew Time:** Required for canister install/removal
- **Autonomy:** Yes (parameters set from ground by telemetry; user-program automatic control)
- **Sample Return Required:** As per mission
- **Compatibility with On-Orbit Sample Processing:** Yes (Kibo PM, BEU standard canister interface)

## Structural Models
- [stress_analysis.py](./stress_analysis.py)
