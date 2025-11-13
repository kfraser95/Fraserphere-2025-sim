# Fraserphere 2025 Simulation Suite

**DOI**: [10.5281/zenodo.13742965](https://doi.org/10.5281/zenodo.13742965)  
**Paper**: *Theoretical Feasibility of the Fraserphere* (2025)

This repository contains all simulations used to validate the Fraserphere photonic relay system for 50 AU deep-space chains.

## Modules
| Module | Tool | Output |
|-------|------|--------|
| Beam Propagation | `pyFFS` + PROPER | 7.2 cm spot @ 1.4 m |
| Link Budget | SymPy | –136.2 dBm @ 1 AU |
| Radiation Transport | GEANT4 + SRIM | 0.42% swelling |
| Thermal FEM | COMSOL export | ΔT < 8 K |
| Error Correction | PyLDPC | BER < 10⁻⁹ post-10 krad |

## Quick Start
```bash
pip install -r requirements.txt
python src/link_budget.py
