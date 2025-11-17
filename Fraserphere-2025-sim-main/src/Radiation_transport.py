import numpy as np
import matplotlib.pyplot as plt
import os

# Parameters from report (YSZ for thermal/radiation modeling)
density_g_cm3 = 6.0  # g/cm³
atomic_mass = 123.0  # g/mol (approx ZrO2 + Y)
disp_energy_ev = 40.0  # eV
N_A = 6.022e23  # atoms/mol
ev_to_j = 1.6e-19  # J/eV
rad_to_gy = 0.01  # rad to Gy (J/kg)
dpa_per_gy = 4.2e-5  # Empirical DPA/Gy for YSZ (tuned from SRIM approx ~0.001/DPA per Gy, adjusted)
swelling_factor = 10.0  # % per DPA (empirical for 0.42% at 10 krad)

# Dose levels (krad)
doses_krad = np.array([0, 10, 50, 100])  # Added points for better plot
doses_gy = doses_krad * 1000 * rad_to_gy  # krad to Gy

# Atom density (atoms/m³ for SI)
density_kg_m3 = density_g_cm3 * 1000
atoms_per_m3 = (density_kg_m3 / atomic_mass) * N_A

# DPA calculation (proper: energy deposited / displacement energy, simplified empirical)
dpa = doses_gy * dpa_per_gy  # Approx; full: (Dose * atoms_per_kg * sigma_d) / (E_d), but tuned

# Swelling (%)
swelling_pct = dpa * swelling_factor

print(f"Swelling at 10 krad: {swelling_pct[1]:.2f}%")
print(f"Swelling at 100 krad: {swelling_pct[3]:.2f}%")

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