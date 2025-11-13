import numpy as np
import pandas as pd
import os

# === LINK BUDGET ===
P_t = 10.0              # W
G_t_dB = G_r_dB = 108.0 # dB
G_amp_dB = 60.0         # dB/hop (Optimized Design)
lam = 1550e-9           # m
d = 1.496e11            # 1 AU

# Convert gains from dB to linear
G_t = 10**(G_t_dB/10)
G_r = 10**(G_r_dB/10)

# === 1 AU: First Hop ===
P_r1 = P_t * G_t * G_r * (lam / (4*np.pi*d))**2
P_r_1AU_dBm = 10 * np.log10(P_r1 * 1000)

print(f"1 AU: {P_r_1AU_dBm:.1f} dBm")

# === 50 AU: After 49 Amplified Hops ===
N_hops = 50
P_rN = P_r1 * (10**(G_amp_dB / 10))**(N_hops - 1)
P_r_50AU_dBm = 10 * np.log10(P_rN * 1000)

print(f"50 AU: {P_r_50AU_dBm:.1f} dBm")

# === SAVE TO CSV ===
os.makedirs("../results/tables", exist_ok=True)
data = [
    {
        "Distance_AU": 1,
        "P_r_1AU_dBm": round(P_r_1AU_dBm, 1),
        "P_r_1AU_W": P_r1,
        "P_r_50AU_dBm": None,
        "P_r_50AU_W": None
    },
    {
        "Distance_AU": 50,
        "P_r_1AU_dBm": None,
        "P_r_1AU_W": None,
        "P_r_50AU_dBm": round(P_r_50AU_dBm, 1),
        "P_r_50AU_W": P_rN
    }
]
df = pd.DataFrame(data)
df.to_csv("../results/tables/link_budget.csv", index=False)
print("Saved: ../results/tables/link_budget.csv")