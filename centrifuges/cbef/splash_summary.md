# SPLASH Summary - Cell Biology Experiment Facility (CBEF)

**Operations**: Ground telemetry + crew installation  
**Category**: Experiment Hosting Facilities with Centrifuges  
**Operator/Vendor**: JAXA / MHI (Mitsubishi Heavy Industries)  
**Status**: Active  
**Flight Heritage**: JEM Pressurized Module (Kibo), ISS  
**Year of First Launch**: 2008 (Space Shuttle)  

**Mass**: Per JAXA/Kibo payload documentation  
**Size**: Rack-mounted; incubator with µG and 1G compartments  
**Payload Volume Required**: 6 medium canisters (µG) + 4 medium canisters (1G)  
**Power (Average)**: Per JEM rack; canister: DC +5 V, +12 V, ±15 V  
**Temperature Range**: 15°C–40°C (±1°C distribution, 0.1°C steps)  
**Interface Definitions**: Standard medium canister (power, analog, video, command per JEM spec)  
**Radiation Sensitivity**: Standard ISS  
**Heat Sync Required**: Facility thermal control  

**Specimen Types Supported**: Cells, plants, small animals (life science cultivation)  
**Temperature Range at Sample**: 15°C–40°C (±1°C, 0.1°C steps)  
**Gas Control**: CO₂ 0–10% vol (0.1% steps); humidity 20–80% RH  
**Experiment Duration**: User-defined; long-term cultivation supported  
**Measurements**: Video interface per standard JEM video specification  

**Crew Handling Required**: Yes (install/remove canisters)  
**Crewtime Needed**: Yes (canister install/removal)  
**Autonomy**: Yes (ground telemetry; user-program automatic control)  
**Sample Return Required**: As per mission  

**Notes / Structural Models**: See [stress_analysis.py](./stress_analysis.py) for centrifugal force and hoop stress calculations (max g-load, etc.).
