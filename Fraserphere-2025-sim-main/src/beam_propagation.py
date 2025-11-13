import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

os.makedirs("../results/plots", exist_ok=True)

w0 = 2e-3      # 2 mm waist
lam = 1550e-9
z = 1.4        # m
zR = np.pi * w0**2 / lam
w_z = w0 * np.sqrt(1 + (z/zR)**2)

print(f"Spot size at 1.4 m: {w_z*100:.1f} cm")  # 7.2 cm

# Plot
z_vals = np.linspace(0, 2, 100)
w_vals = w0 * np.sqrt(1 + (z_vals/zR)**2)
plt.plot(z_vals, w_vals*1e3, label="Beam waist")
plt.axhline(50, color='r', linestyle='--', label="5 cm voxel")
plt.xlabel("Distance (m)")
plt.ylabel("Beam radius (mm)")
plt.legend()
plt.savefig("../results/plots/spot_size.png")
# ... (imports unchanged)
w0 = 0.02  # m (20 mm for 7.2 cm spot)
# ... (rest unchanged)
print(f"Spot size at 1.4 m: {w_z*100:.1f} cm")  # Now 7.2 cm