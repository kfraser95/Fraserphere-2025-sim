import numpy as np

w0 = 0.075  # m (half aperture for effective waist)
lam = 1550e-9
z = 1.4  # m
zR = np.pi * w0**2 / lam  # Rayleigh range
w_z = w0 * np.sqrt(1 + (z / zR)**2)  # Beam radius
spot_diameter_cm = 2 * w_z * 100  # cm

print(f"Spot diameter at 1.4 m: {spot_diameter_cm:.1f} cm")  # 15.0 cm (aperture match)