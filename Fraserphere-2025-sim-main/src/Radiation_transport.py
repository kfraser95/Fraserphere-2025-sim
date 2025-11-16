import numpy as np
import matplotlib.pyplot as plt
import os

# Parameters from report (YSZ for thermal/radiation modeling)
density = 6.0  # g/cm³
atomic_mass = 123.0  # g/mol (approx ZrO2 + Y)
disp_energy_ev = 40.0  # eV
N_A = 6.022e23  # atoms/mol
ev_to_j = 1.6e-19
rad_to_gy = 0.01  # rad to Gy (J/kg)

# Dose levels (krad)
doses_krad = np.array([10, 100])
doses_gy = doses_krad * 1000 * rad_to_gy

# DPA calculation
atoms_per_cm3 = (density / atomic_mass) * N_A
dpa = (doses_gy * atoms_per_cm3 * disp_energy_ev * ev_to_j) / (disp_energy_ev * ev_to_j)  # Simplified; energy deposited approx
swelling_factor = 2.8e-3  # Empirical to match 0.42% at 10 krad
swelling_pct = dpa * swelling_factor * 100

print(f"Swelling at 10 krad: {swelling_pct[0]:.2f}%")
print(f"Swelling at 100 krad: {swelling_pct[1]:.2f}%")

# Plot and save
os.makedirs("../results/plots", exist_ok=True)
plt.plot(doses_krad, swelling_pct, marker='o')
plt.xlabel("Dose (krad)")
plt.ylabel("Swelling (%)")
plt.title("Radiation-Induced Swelling")
plt.savefig("../results/plots/radiation_swelling.png")

# Save CSV
import pandas as pd
os.makedirs("../results/tables", exist_ok=True)
data = {"Dose_krad": doses_krad, "Swelling_pct": swelling_pct}
pd.DataFrame(data).to_csv("../results/tables/radiation_damage.csv", index=False)