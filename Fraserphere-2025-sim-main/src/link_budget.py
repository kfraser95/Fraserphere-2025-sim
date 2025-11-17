import numpy as np
import pandas as pd
import os

# Report parameters
c = 3e8  # m/s
lam = 1550e-9  # m
d_AU = 1.495978707e11  # m
P_t_W = 10.0  # W
P_t_dBm = 10 * np.log10(P_t_W * 1000)  # 40 dBm
D = 0.15  # m
eta = 0.8
G_linear = eta * (np.pi * D / lam)**2
G_dB = 10 * np.log10(G_linear)  # 108.69 dBi
total_G_dB = 2 * G_dB  # 217.38 dB
FSPL_dB = 20 * np.log10(4 * np.pi * d_AU / lam)  # 361.68 dB

# Received power
P_r_dBm = P_t_dBm + total_G_dB - FSPL_dB  # -104.30 dBm

# Sensitivity
P_sens_dBm = -50

# Margin without amp
margin_no_amp_dB = P_r_dBm - P_sens_dBm  # -54.30 dB

# Margins with preamp gains (60, 80, 100 dB)
G_amp = [60, 80, 100]
margins_with_amp = [P_r_dBm + g - P_sens_dBm for g in G_amp]  # [5.7, 25.7, 45.7] dB

# NF accumulation (Friis formula approximation for 100 hops)
NF_dB = 4.0
NF_lin = 10**(NF_dB / 10)  # 2.5119
G_stage_dB = 30.0  # Example per stage (linear 1000)
G_lin = 10**(G_stage_dB / 10)
degrad_lin = (NF_lin - 1) / (G_lin - 1)  # Geometric sum ≈ 0.00151
NF_total_lin = NF_lin + degrad_lin  # 2.5134 (ignores finite hops, but <0.00001 error)
NF_total_dB = 10 * np.log10(NF_total_lin)  # 4.002 dB
degradation_dB = NF_total_dB - NF_dB  # 0.002 dB

# Print results
print(f"P_r_dBm: {P_r_dBm:.2f}")
print(f"Margin without amp: {margin_no_amp_dB:.2f} dB")
print(f"Margins with amps [60,80,100 dB]: {[round(m, 2) for m in margins_with_amp]} dB")
print(f"NF degradation over 100 hops: {degradation_dB:.4f} dB")

# Save to CSV
os.makedirs("../results/tables", exist_ok=True)
data = {
    "Parameter": ["P_r_dBm (1 AU)", "Margin_no_amp_dB", "Margin_60dB_amp", "Margin_80dB_amp", "Margin_100dB_amp", "NF_degradation_dB"],
    "Value": [P_r_dBm, margin_no_amp_dB] + margins_with_amp + [degradation_dB]
}
pd.DataFrame(data).to_csv("../results/tables/link_budget.csv", index=False)
print("Results saved to ../results/tables/link_budget.csv")