import numpy as np
import pandas as pd
import os

# Parameters
k_range = [0.0015, 0.0025]  # krad^{-1}
doses_krad = np.array([0, 10, 50, 100])

# Retention
retention_min = np.exp(-k_range[1] * doses_krad)
retention_max = np.exp(-k_range[0] * doses_krad)
loss_min_pct = (1 - retention_max) * 100
loss_max_pct = (1 - retention_min) * 100

print(f"Capacity loss at 100 krad: {loss_min_pct[-1]:.1f}% to {loss_max_pct[-1]:.1f}%")

# Save CSV
os.makedirs("../results/tables", exist_ok=True)
data = {"Dose_krad": doses_krad, "Loss_min_pct": loss_min_pct, "Loss_max_pct": loss_max_pct}
pd.DataFrame(data).to_csv("../results/tables/li_s_radiation.csv", index=False)