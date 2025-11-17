import numpy as np
import pandas as pd
import os

# Parameters
lam_v = 0.55e-6  # m
lam = 1.55e-6  # m
exponent = 1.61
mag_to_db = 4  # Approx factor

# A_V levels (mag/pc) - convert to NumPy array for element-wise operations
a_v_levels = np.array([0.002, 0.1, 1, 10, 100, 1000])  # Diffuse to ultra
labels = ["Diffuse", "Dense", "Extreme", "Worst-case", "Hyper-extreme", "Ultra-pockets"]

a_lambda = a_v_levels * (lam_v / lam)**exponent
alpha_db_pc = mag_to_db * a_lambda

# Coherence reduction at 10 pc (% loss ≈ 1 - 10^{-alpha/10 * dist})
dist_pc = 10
loss_db = alpha_db_pc * dist_pc
coherence_loss_pct = (1 - 10**(-loss_db / 10)) * 100

print("ISM Attenuation Summary:")
for label, alpha, loss in zip(labels, alpha_db_pc, coherence_loss_pct):
    print(f"{label}: {alpha:.4f} dB/pc, {loss:.2f}% loss at 10 pc")

# Save CSV
os.makedirs("../results/tables", exist_ok=True)
data = {"Type": labels, "A_V_mag_pc": a_v_levels, "Alpha_dB_pc": alpha_db_pc, "Loss_pct_10pc": coherence_loss_pct}
pd.DataFrame(data).to_csv("../results/tables/ism_attenuation.csv", index=False)