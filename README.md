# 📈 Advanced Option Pricing Engine

A **modular quantitative finance framework** for pricing derivative securities using **analytical methods** and **Monte Carlo simulations**.  

This project demonstrates **numerical methods**, **stochastic simulations**, **variance reduction techniques**, and **sensitivity analysis** used in quantitative finance and derivatives trading.

---

## 🧠 Project Overview

The goal of this project is to build a **flexible pricing engine** capable of handling:

- ⚡ **Closed-form analytical solutions**  
- 🎲 **Simulation-based pricing**  
- 🔗 **Path-dependent derivatives**  
- 📉 **Variance reduction techniques**  
- 📊 **Numerical Greeks estimation**

The framework is **modular**, allowing future extensions like **stochastic volatility models**, **market data calibration**, and **performance optimization**.

---

## ⚙️ Implemented Models & Methods

### 🔹 Black–Scholes Analytical Model
- 💰 European Call Option pricing  
- 📏 Closed-form benchmark solution  
- ✅ Used to validate Monte Carlo estimators  

### 🔹 Monte Carlo Simulation Framework
- 📈 Geometric Brownian Motion (GBM) path simulation  
- 🏦 Risk-neutral pricing  
- ⚙️ Configurable simulation size  
- 📉 Convergence analysis  

### 🔹 Variance Reduction Techniques
Improve estimator efficiency using:

- 🔄 **Antithetic Variates**  
- 🎯 **Control Variates**  
- 📊 Absolute error comparison vs analytical benchmark  
- 📈 Convergence visualization  

### 🔹 Path-Dependent Options
Monte Carlo pricing for exotic derivatives:

- 🍚 **Asian Options** (Arithmetic Average)  
- 🚧 **Up-and-Out Barrier Call Options**  

### 🔹 Greeks Estimation (Sensitivity Analysis)
Numerical estimation using finite-difference Monte Carlo:

- 🔹 **Delta**  
- 🔹 **Gamma**  
- 🔹 **Vega**  

---

## 📊 Example Outputs

| Model | Example Output |
|-------|----------------|
| 💹 Black–Scholes | Black–Scholes European Call Price plot |
| 🎲 Asian Option | Monte Carlo Asian Option Price plot |
| 🚧 Barrier Option | Up-and-Out Barrier Option Price plot |
| 🔄 Greeks (Delta/Gamma/Vega) | Monte Carlo Greeks Sensitivity plots |
| 📈 Variance Reduction | Variance Reduction Convergence plot |

---

## 🏗 Project Structure

```text
Advanced-Option-Pricing/
├─ models/
│  └─ black_scholes.py
├─ monte_carlo/
│  ├─ variance_reduction.py
│  ├─ asian.py
│  └─ barrier.py
├─ greeks/
│  └─ finite_difference.py
├─ main.py
├─ requirements.txt
└─ README.md

