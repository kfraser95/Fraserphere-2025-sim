import numpy as np
import matplotlib.pyplot as plt
import os

# Parameters (simplified 1D wave)
num_sources = 100  # Hops/swarm
phase_jitter = 0.01  # rad (PLL error)
t = np.linspace(0, 10, 1000)
E_total = np.zeros_like(t, dtype=complex)

for i in range(num_sources):
    phase = np.random.normal(0, phase_jitter)
    E_total += np.exp(1j * (2 * np.pi * t + phase))

I = np.abs(E_total)**2
I_avg = np.mean(I)
I_incoh = num_sources  # Normalized
coherence = I_avg / I_incoh
print(f"Coherence: {coherence * 100:.1f}%")

# Plot and save
os.makedirs("../results/plots", exist_ok=True)
plt.plot(t, np.real(E_total))
plt.xlabel("Time")
plt.ylabel("Field")
plt.title("Coherent Field")
plt.savefig("../results/plots/em_coherence.png")