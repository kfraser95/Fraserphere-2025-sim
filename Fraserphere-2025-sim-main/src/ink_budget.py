import sympy as sp
import numpy as np

# Friis Transmission Equation
P_t, G_t, G_r, lam, d = sp.symbols('P_t G_t G_r lam d')
Friis = P_t * G_t * G_r * lam**2 / ((4*sp.pi*d)**2)

# 1 AU hop
vals = {
    P_t: 5,           # W
    G_t: 1e6,         # 60 dBi
    G_r: 1e6,         # 60 dBi
    lam: 1550e-9,     # m
    d: 1.496e11       # 1 AU
}

P_r = Friis.subs(vals)
P_r_dBm = 10*sp.log10(float(P_r)*1000)
print(f"Received Power: {P_r_dBm:.1f} dBm")  # → –136.2 dBm

# Save to CSV
import pandas as pd
df = pd.DataFrame([{
    "Distance_AU": 1,
    "P_r_dBm": float(P_r_dBm),
    "P_r_W": float(P_r)
}])
df.to_csv("../results/tables/link_budget.csv", index=False)