import numpy as np
import matplotlib.pyplot as plt
import os

# Parameters (15 cm cube, Al structure)
L = 0.15  # m
kappa = 200  # W/m·K
P_heat = 1.0  # W (10% inefficiency from 10 W tx)
nx = 50  # Grid points
dx = L / (nx - 1)
x = np.linspace(0, L, nx)

# Source term Q = P_heat / volume
vol = L**3
Q = P_heat / vol  # W/m³

# FEM-like: Solve -kappa d²T/dx² = Q (boundaries T=0 K ambient)
A = np.diag(-2 * np.ones(nx)) + np.diag(np.ones(nx-1), 1) + np.diag(np.ones(nx-1), -1)
A[0, 0] = 1; A[0, 1] = 0; A[-1, -1] = 1; A[-1, -2] = 0  # Dirichlet BC
b = - (dx**2 / kappa) * Q * np.ones(nx)
b[0] = 0; b[-1] = 0
T = np.linalg.solve(A, b)

delta_T = np.max(T)
print(f"Max ΔT: {delta_T:.1f} K")

# Plot and save
os.makedirs("../results/plots", exist_ok=True)
plt.plot(x, T)
plt.xlabel("Position (m)")
plt.ylabel("ΔT (K)")
plt.title("Thermal Profile")
plt.savefig("../results/plots/thermal_profile.png")