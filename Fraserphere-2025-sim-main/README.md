# Fraserphere 2025 Simulation Suite

**DOI**: [10.5281/zenodo.13742965](https://doi.org/10.5281/zenodo.13742965)  

**Paper**: *Theoretical Feasibility of the Fraserphere* (2025)

This repository contains simulations used to validate the Fraserphere photonic relay system for 100 AU deep-space chains.
A word from the auther, No idea how patent laws work and there was too much red tape sorruding it when I looked into it. So for the sake of publishing all ideas and concepts are considered published and free use on the condition that I, Kyle Ross Fraser receive accredation and recognition for my contributions. 

The system incorporates the following technologies, 
Component,              Specification,                                      Source
Transmitter,            "10 W VCSEL phased array, 0.01°",                   Princeton Optronics 2025
Amplifier,              60 dB Yb-fiber (single stage),                      IPG Photonics YAR-100
Aperture,               15 cm (cube face),                                  108 dB gain
Wavelength,             1550 nm,                                            Telecom COTS
Hops,                   100 (1 AU spacing),                                 100 AU reach 
P_r @ 100 AU,           –135.4 dBm,                                         +20.4 dB margin
Data Rate,              >10 Gbps,                                           APD BW-limited

## Modules
| Module | Tool | Output |
|-------|------|--------|
| Beam Propagation | `pyFFS` + PROPER | 7.2 cm spot @ 1.4 m | 
| Link Budget | SymPy | –136.2 dBm @ 1 AU |
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
