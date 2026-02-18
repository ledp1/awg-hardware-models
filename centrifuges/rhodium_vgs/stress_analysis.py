# SPLASH adopt-an-instrument: centrifuge hoop stress (SymPy)
import sympy as sp

m, r, omega = sp.symbols('m r omega')
F_centrifugal = m * omega**2 * r

rho = sp.symbols('rho')
sigma_hoop = rho * r * omega**2

# Example: omega = 1403 rad/s (13,400 RPM), r=0.05m, rho=2700 kg/m³ (aluminum)
omega_val = 1403
r_val = 0.05
rho_val = 2700
stress_val = sigma_hoop.subs({r: r_val, omega: omega_val, rho: rho_val})
print(f"Hoop stress: {stress_val} Pa (~{stress_val/1e6:.2f} MPa)")

# Rhodium VGS (current ISS, variable 0-1g)
