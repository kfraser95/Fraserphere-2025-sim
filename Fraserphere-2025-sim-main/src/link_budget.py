import numpy as np
import pandas as pd
import os
from sympy import symbols, pi, log

# Core Params (Corrected for Optical)
lam = 1550e-9  # m
d_1AU = 1.496e11  # m
P_t_W = 10.0  # W per node
P_t_dBm = 10 * np.log10(P_t_W * 1000)  # 40 dBm
D = 0.15  # m aperture diameter
A = np.pi * (D / 2)**2
G_linear = 4 * np.pi * A / lam**2
G_dB = 10 * np.log10(G_linear)
total_G_dB = 2 * G_dB  # Tx + Rx
FSPL_dB = 20 * np.log10(4 * np.pi * d_1AU / lam)

# P_r per hop (constant)
P_r_dBm = P_t_dBm + total_G_dB - FSPL_dB
P_r_W = 10**((P_r_dBm - 30) / 10) / 1000  # W from dBm

# Required G_amp
req_G_amp_dB = P_t_dBm - P_r_dBm + 3  # 3 dB margin

# Margin (APD sens -90 dBm for 10 Gbps w/ FEC)
P_sens_dBm = -90
margin_dB = P_r_dBm - P_sens_dBm

# Outputs
num_hops = 100
print(f"P_r per hop: {P_r_dBm:.1f} dBm")
print(f"Required G_amp: {req_G_amp_dB:.1f} dB")
print(f"Margin per hop: {margin_dB:.1f} dB")

# Symbolic Req Gain
P_t_sym, P_r_sym = symbols('P_t P_r')
req_gain_sym = 10 * log(P_t_sym / P_r_sym, 10)
print(f"Symbolic req gain: {req_gain_sym.subs({P_t_sym: P_t_W, P_r_sym: P_r_W}).evalf():.1f} dB")

# Save CSV
os.makedirs("results/tables", exist_ok=True)
data = [
    {"Hops": 1, "P_r_dBm": round(P_r_dBm, 1), "P_r_W": P_r_W, "Margin_dB": round(margin_dB, 1), "Req_G_amp_dB": round(req_G_amp_dB, 1)},
    {"Hops": num_hops, "P_r_dBm": round(P_r_dBm, 1), "P_r_W": P_r_W, "Margin_dB": round(margin_dB, 1), "Req_G_amp_dB": round(req_G_amp_dB, 1)}
]
pd.DataFrame(data).to_csv("results/tables/link_budget.csv", index=False)