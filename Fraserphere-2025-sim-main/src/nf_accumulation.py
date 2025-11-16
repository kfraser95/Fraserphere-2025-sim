import numpy as np
import pandas as pd
import os

# Parameters
NF_dB = 4.0
G_dB = 30.0
num_hops = 100

NF_lin = 10**(NF_dB / 10)
G_lin = 10**(G_dB / 10)

# Cumulative NF
nf_total_lin = NF_lin
for i in range(1, num_hops):
    nf_total_lin += (NF_lin - 1) / np.prod([G_lin] * i)

nf_total_dB = 10 * np.log10(nf_total_lin)
degradation_dB = nf_total_dB - NF_dB
print(f"Total NF degradation over {num_hops} hops: {degradation_dB:.4f} dB")

# Save CSV
os.makedirs("../results/tables", exist_ok=True)
data = {"Hops": [num_hops], "Degradation_dB": [degradation_dB]}
pd.DataFrame(data).to_csv("../results/tables/nf_degradation.csv", index=False)