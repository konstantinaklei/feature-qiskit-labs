# Quantum State Simulation & Hardware Error Analysis

## Summary
This project demonstrates the execution of quantum algorithm workflows, state preparation, and noise modeling using **IBM Qiskit V2 Primitives**. 

By running simulations against realistic noise profiles derived from actual IBM Quantum Processors (`ibm_fez`), this repository showcases **data-driven error analysis**, comparing theoretical expected values against statistical measurement distributions

---

## Experiment & Data Insights

### 1. Entanglement & Bell State Execution (`firstcircuit.py`)
A 2-qubit Bell State ($|\Psi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}$) was generated using Hadamard (`H`) and Controlled-NOT (`CX`) gates. 
* **Sample Size:** 1,000 shots.
* **Results Distribution:** Yielded near 50/50 probability distribution between states `|01>` and `|10>` (with gate noise perturbation evaluated).

### 2. Transverse-Field Ising Model & Noise Deviation (`firstquantumexperiment.ipynb`)
Evaluated the expectation value of a 2-qubit Ising Hamiltonian:
$$H = J \cdot (Z \otimes Z) + h_x \cdot (X \otimes I) + h_x \cdot (I \otimes X)$$ 
*(where $J = 1.0$ and $h_x = -0.5$)*.

---

##  Tech Stack
* **Language:** Python 3.14
* **Quantum SDK:** Qiskit, Qiskit Aer (`AerSimulator`), Qiskit IBM Runtime (`EstimatorV2`, `SamplerV2`)
* **Analytics & Visualization:** Matplotlib, Python `dotenv`

---

## Security Note
* API Credentials are loaded dynamically via standard environment variables (`.env`) and are strictly ignored via `.gitignore` to prevent credential leakage.

---