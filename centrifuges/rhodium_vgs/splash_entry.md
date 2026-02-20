# Rhodium Variable Gravity Simulator (RhVGS-01) — SPLASH Entry

## General
- **Operations:** GROUND-CONTROLLED + ON-ORBIT SAMPLE EXCHANGE
- **Category:** Experiment Hosting Facilities with Centrifuges
- **Operator/Vendor:** Rhodium Scientific / NASA (ISS National Lab)
- **Status:** Active
- **Flight Heritage:** ISS internal; DARPA Biomanufacturing missions (e.g., Summer 2024); 2024
- **Year of First Launch:** 2024

## Specifications
- **Mass:** Per Rhodium Scientific / ISS National Lab documentation
- **Size:** ISS internal facility
- **Power:** Per ISS allocation
- **Centrifuge Performance:** Low-speed, high-throughput; Lunar, Martian, and Earth gravity simulation
- **Temperature Range:** Ambient ISS (mission-dependent configuration)
- **Payload Volume Required:** Up to 36 samples per operational period
- **Interface Definitions:** Proprietary QuIC Space Process™; industry-compatible quality assurances
- **Radiation Sensitivity:** Standard ISS
- **Heat Sink Required:** As per facility design

## Research
- **Supported Specimen Types:** Biological systems; biomanufacturing
- **Specimen Size/Quantity:** Up to 36 samples; load/unload on orbit per operational period
- **Temperature Range at Sample:** Mission-dependent
- **Experiment Duration:** Mission-dependent; multiple gravity forces and time points supported
- **Centrifuge:** Yes (Lunar, Martian, Earth g)
- **Imaging:** As per mission
- **Key Applications:** Partial-g accuracy in µg; on-orbit sample exchange; high-throughput partial-g

## Logistics
- **Crew Handling Required:** Yes (sample exchange on orbit)
- **Crew Time:** Required for sample exchange
- **Autonomy:** Yes (ground control)
- **Sample Return Required:** As per mission
- **Compatibility with On-Orbit Sample Processing:** Yes (only ISS centrifuge with on-orbit load/unload for high-throughput partial-g; 6–9 months to launch from kickoff)

## Structural Models
See [stress_analysis.py](./stress_analysis.py) for centrifugal force and hoop stress calculations (max g-load, etc.).
