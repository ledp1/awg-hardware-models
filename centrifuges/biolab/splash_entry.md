# BioLab (ESA Columbus) — SPLASH Entry

## General
- **Operations:** CREW TIME FOR LOADING + GROUND TELESCIENCE
- **Category:** Experiment Hosting Facilities with Centrifuges
- **Operator/Vendor:** ESA / DLR (MUSC, Cologne)
- **Status:** Active
- **Flight Heritage:** Columbus module, ISS; launched 7 February 2008 (Space Shuttle Atlantis)
- **Year of First Launch:** 2008

## Specifications
- **Mass:** Per ESA/Columbus payload documentation
- **Size:** Rack-mounted in Columbus; two rotor platforms in incubator
- **Power:** Per Columbus rack allocation
- **Centrifuge Performance:** Two rotor platforms; 1 g simulated for gravity comparison with weightlessness
- **Temperature Range:** Incubator-controlled (facility life support)
- **Payload Volume Required:** Columbus rack; experiment containers / vials (ATV, Progress, commercial cargo)
- **Interface Definitions:** Experiment containers; standard vials; MELFI storage interface
- **Radiation Sensitivity:** Standard ISS
- **Heat Sink Required:** Facility thermal control

## Research
- **Supported Specimen Types:** Micro-organisms, cells, tissue cultures, small plants, small invertebrates
- **Specimen Size/Quantity:** Standard experiment containers and vials; capacity per rotor platform
- **Temperature Range at Sample:** Incubator-controlled
- **Experiment Duration:** 1 day–3 months
- **Centrifuge:** Yes (1 g on rotor platforms)
- **Imaging:** Yes (video on rotor platforms; microscope; teleoperations)
- **Key Applications:** Life science µg vs 1 g; video/microscope teleoperations

## Logistics
- **Crew Handling Required:** Yes (insert containers, BioGlovebox loading, initiate automatic processing)
- **Crew Time:** Required for loading and initiation
- **Autonomy:** Yes (automatic processing after crew initiation; ground teleoperations)
- **Sample Return Required:** As per mission (cargo return)
- **Compatibility with On-Orbit Sample Processing:** Yes (BioGlovebox, Experiment Preparation Unit, MELFI)

## Structural Models
See [stress_analysis.py](./stress_analysis.py) for centrifugal force and hoop stress calculations (max g-load, etc.).
