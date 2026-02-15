# AWG hardware models for SPLASH
_Exported on 02/15/2026 at 11:11:40 GMT-5 from Cursor via WayLog_


**User**

Generate README.md for this repo: Title "AWG Hardware Models for SPLASH". Content: Structural integrity models for Hardware AWG adopt-an-instrument (centrifuges: BioServe/NanoRacks; lunar rover wheels). Bullet points: Centrifuges stress at 12,100g (NanoRacks). Rover wheels load under 1/6g lunar gravity. Aligns with SPLASH V1 (Kylee Brahma Sep 2025 presentation) and subgroup sheet. Contact: depombo2@gmail.com | @luisdepombo. See /centrifuges and /rover_wheels for Python (sympy) models.

---


**Cursor**

Checking the repo structure so the README accurately references the project.

Creating README.md with the provided content. Repo is minimal; README will reference `/centrifuges` and `/rover_wheels` as specified.

Summary of what’s in the new **README.md**:

- **Title:** AWG Hardware Models for SPLASH  
- **Intro:** Structural integrity models for Hardware AWG adopt-an-instrument (centrifuges: BioServe/NanoRacks; lunar rover wheels).  
- **Bullets:**  
  - Centrifuges stress at 12,100g (NanoRacks).  
  - Rover wheels load under 1/6g lunar gravity.  
  - Aligns with SPLASH V1 (Kylee Brahma Sep 2025 presentation) and subgroup sheet.  
- **Contact:** depombo2@gmail.com | @luisdepombo  
- **Model locations:** Table linking to `/centrifuges` and `/rover_wheels` with a short note that they contain Python (SymPy) models.

The file is at `/Users/myhomefolder/my-development/awg-hardware-models/README.md`. You can tweak wording or add sections (e.g. setup, usage) if you want.

---


**User**

Create folder 'centrifuges' with file 'stress_analysis.py' inside. Add this code to stress_analysis.py: import sympy as sp; m, r, omega = sp.symbols('m r omega'); F_centrifugal = m * omega**2 * r; sigma_hoop = sp.symbols('rho') * r * omega**2; # Example: omega = 1403 rad/s (13,400 RPM), r=0.05m, rho=2700 kg/m³ (aluminum); omega_val=1403; r_val=0.05; rho_val=2700; stress_val=sigma_hoop.subs({r:r_val, omega:omega_val, rho:rho_val}); print(f"Hoop stress: {stress_val} Pa (~{stress_val/1e6:.2f} MPa)"); # For BioServe: Lower RPM (105 rad/s), adjust omega_val.

---


**Cursor**

Creating the `centrifuges` folder and adding `stress_analysis.py` with the provided code. Defining `rho` as a symbol so `sigma_hoop.subs(...)` works.

Summary of what’s in place:

**Created**
- `centrifuges/`
- `centrifuges/stress_analysis.py` with your SymPy stress analysis

**In the script**
- Symbols `m`, `r`, `omega` and centrifugal force \(F = m \omega^2 r\)
- Hoop stress \(\sigma = \rho r \omega^2\) (with `rho` defined as a symbol so `.subs({..., rho: rho_val})` works)
- Example: 1403 rad/s (13,400 RPM), \(r = 0.05\) m, \(\rho = 2700\) kg/m³ (aluminum)
- Comment for BioServe case (e.g. 105 rad/s)

**Change made**
- Replaced `sigma_hoop = sp.symbols('rho') * r * omega**2` with `rho = sp.symbols('rho')` and `sigma_hoop = rho * r * omega**2` so the symbol `rho` is defined and can be used in `.subs({r: r_val, omega: omega_val, rho: rho_val})`.

Run it with:
`python centrifuges/stress_analysis.py`  
(from the repo root, with `sympy` installed).

---


**User**

Create folder 'rover_wheels' with file 'stress_analysis.py' inside. Add this code: import sympy as sp; g_lunar, m_wheel, F_gravity = sp.symbols('g_lunar m_wheel F_gravity'); F_gravity = m_wheel * g_lunar / 6; sigma_beam = sp.symbols('E I L') * F_gravity / (sp.symbols('w t')**3); # Example: m_wheel=10kg, g=9.81 m/s²; g_val=9.81; m_val=10; load_val=F_gravity.subs({m_wheel:m_val, g_lunar:g_val}); print(f"Lunar load: {load_val:.2f} N"); # Wire dia ~0.0005m for tensile stress.

---


**Cursor**

Creating the `rover_wheels` folder and adding `stress_analysis.py`. Defining symbols so expressions are valid (e.g. `E`, `I`, `L`, `w`, `t` for `sigma_beam`).

---
