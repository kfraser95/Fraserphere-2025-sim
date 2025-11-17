import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

os.makedirs("../results/plots", exist_ok=True)

# Initial parameters (updated for report: w0 = 0.075 m radius for 15 cm diameter)
w0 = 0.075  # m (half of 15 cm aperture)
lam = 1550e-9  # m
z = 1.4  # m

# Rayleigh range and beam radius
zR = np.pi * w0**2 / lam
w_z = w0 * np.sqrt(1 + (z / zR)**2)
print(f"Spot diameter at 1.4 m: {2 * w_z * 100:.1f} cm")  # 15.0 cm

# Plot over distance
z_vals = np.linspace(0, 2, 100)
w_vals = w0 * np.sqrt(1 + (z_vals / zR)**2)
plt.plot(z_vals, w_vals * 1e3, label="Beam waist")  # In mm
plt.axhline(50, color='r', linestyle='--', label="5 cm voxel")  # Reference line
plt.xlabel("Distance (m)")
plt.ylabel("Beam radius (mm)")
plt.legend()
plt.savefig("../results/plots/spot_size.png")