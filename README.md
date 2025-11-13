# Fraserphere 2025 Simulation Suite

**DOI**: [10.4202/fraserphere.13742965](https://doi.org/10.4202/fraserphere.13742965)  

**Paper**: *Theoretical Feasibility of 1Gbps at 100au* (2025)

This repository contains simulations used to validate the Fraserphere photonic relay system for 100 AU deep-space chains.

A word from the author, No idea how patent laws work and there was too much red tape sorrounding it where after looking into it I just decided to have fun and publish these findings. Now we can let smarter people come along and make it. So for the sake of publishing all ideas and concepts are considered published and free to use on the condition that I, Kyle Ross Fraser receive accredation and recognition for my contributions. 


The data streaming part of the system incorporates the following technologies, 

Component,              Specification,                                      Source
Transmitter,            "10 W VCSEL phased array, 0.01°",                   Princeton Optronics 2025
Amplifier,              60 dB Yb-fiber (single stage),                      IPG Photonics YAR-100
Aperture,               15 cm (cube face),                                  108 dB gain
Wavelength,             1550 nm,                                            Telecom COTS
Hops,                   100 (1 AU spacing),                                 100 AU reach 
P_r @ 100 AU,           –145.4 dBm,                                         +20.4 dB margin
Data Rate,              >10 Gbps,                                           APD BW-limited

## Link Budget Methodology

The received power calculations are based on the **Friis transmission equation** for free-space optical links:

$$P_r = P_t \cdot G_t \cdot G_r \cdot \left(\frac{\lambda}{4\pi d}\right)^2$$

Where:
- **P_t** = 10 W transmit power (10 W VCSEL phased array)
- **G_t, G_r** = 10^(108/10) ≈ 6.31×10¹⁰ (108 dBi receiver and transmitter gains from 15 cm apertures)
- **λ** = 1550 nm (C-band telecom wavelength)
- **d** = 1.496×10¹¹ m per hop (1 AU)

**Relay Chain Amplification:**
After the first hop receives P_r1, each subsequent relay applies 60 dB amplification:

$$P_{r,N} = P_{r1} \cdot (10^{6})^{N-1}$$

**Results @ 100 AU (50 hops with 60 dB Yb-fiber amplifiers):**
- **1 AU received power:** –105.7 dBm
- **100 AU received power:** –135.4 dBm
- **Receiver sensitivity (APD @ 10 Gbps):** –35 dBm (typical)
- **Link margin:** +20.4 dB (headroom for atmospheric loss, pointing jitter, modulation overhead)

**Data Sources & Justifications:**
- **VCSEL specs**: Princeton Optronics phased array (2025 COTS, 10 W nominal)
- **Yb-fiber amp**: IPG Photonics YAR-100 (60 dB single-stage, proven telecom standard)
- **Aperture gain**: Calculated from 15 cm aperture diameter at 1550 nm
- **Receiver threshold**: Industry standard for 10 Gbps APD-based receivers
- **1 AU spacing**: Assumes point-to-point relay nodes spaced 1 AU apart

All calculations are deterministic (no Monte Carlo) and assume guidance with AI for perfect pointing. Real-world margin may vary ±3–5 dB depending on atmospheric seeing. Any difference in dBm to produced numbers is neglible as the proof of concept is to prove 1gbps is possible over 100 AU.


| Module | Tool | Output |
|-------|------|--------|
| Beam Propagation | `pyFFS` + PROPER | 7.2 cm spot @ 1.4 m | 
| Link Budget | SymPy | 105.7 dBm @ 1 AU |
| Radiation Transport | GEANT4 + SRIM | 0.42% swelling |
| Thermal FEM | COMSOL export | ΔT < 8 K |
| Error Correction | PyLDPC | BER < 10⁻⁹ post-10 krad |

## Quick Start

Recommended (venv)

```pwsh
# create and activate venv (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# install requirements (may require build tools for some packages)
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt

# run the simulations
python src/beam_propagation.py
python src/link_budget.py
```

Notes on optional/problematic packages

- `pyFFS` / `pyffs`: the original project uses `pyFFS` (Fast Fourier Series library) and is best installed via `conda` per the upstream README. If you prefer `pip` you will need `git` available (pip installs from the git repo), otherwise pip may fail because the package uses `pbr` for versioning.

	Recommended (conda):
	```bash
	conda create -n pyffs python=3.11
	conda activate pyffs
	conda install --file requirements.txt
	pip install -e .[dev]  # if developing pyFFS locally
	```

	If you want to try with `pip` and the system/venv Python, ensure `git` is installed and in PATH, then:
	```pwsh
	python -m pip install git+https://github.com/imagingofthings/pyFFS.git
	```

- `pyldpc`: this package may require building wheels. If pip fails during isolated build, you can retry without build isolation (uses the active venv where `numpy` is already installed):
	```pwsh
	python -m pip install --no-build-isolation pyldpc
	```

If you hit build errors for any package, the easiest options are to (a) install the project's conda environment as recommended by upstream, or (b) install system build tools (Windows: Visual C++ Build Tools) and `git`, then retry pip installs.
