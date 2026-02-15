# SPLASH adopt-an-instrument: rover wheel load under 1/6g (SymPy)
import sympy as sp

g_lunar, m_wheel, F_gravity = sp.symbols('g_lunar m_wheel F_gravity')
F_gravity = m_wheel * g_lunar / 6

E, I, L, w, t = sp.symbols('E I L w t')
sigma_beam = E * I * L * F_gravity / (w * t**3)

# Example: m_wheel=10kg, g=9.81 m/s²
g_val = 9.81
m_val = 10
load_val = F_gravity.subs({m_wheel: m_val, g_lunar: g_val})
print(f"Lunar load: {load_val:.2f} N")

# Wire dia ~0.0005m for tensile stress.
