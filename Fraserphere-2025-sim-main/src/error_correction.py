import numpy as np
from pyldpc import make_ldpc, encode, decode, get_message
import matplotlib.pyplot as plt
import os

# LDPC parameters (small for sim; n must be divisible by d_c for regular codes)
n = 102  # Adjusted: 102 / 6 = 17 (integer)
d_v = 3  # Variable degree
d_c = 6  # Check degree
H, G = make_ldpc(n, d_v, d_c, systematic=True, sparse=True)

# Simulate BER vs SNR (post-10 krad degradation: +3 dB noise)
snr_db = np.linspace(0, 10, 5)
ber = []
for snr in snr_db:
    k = G.shape[1]
    v = np.random.randint(0, 2, k)
    y = encode(G, v, snr, seed=42)
    d = decode(H, y, snr)
    decoded_v = get_message(G, d)
    errors = np.sum(v != decoded_v)
    ber.append(errors / k)

print(f"BER at 10 dB SNR: {ber[-1]:.2e}")

# Plot and save
os.makedirs("../results/plots", exist_ok=True)
plt.semilogy(snr_db, ber, marker='o')
plt.xlabel("SNR (dB)")
plt.ylabel("BER")
plt.title("LDPC BER Curve")
plt.savefig("../results/plots/ber_vs_snr.png")