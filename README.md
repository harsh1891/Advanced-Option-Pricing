\# 📈 Advanced Option Pricing Engine



A modular quantitative finance framework for pricing derivative securities using both analytical and Monte Carlo methods.



This project demonstrates numerical methods, stochastic simulation, variance reduction techniques, and sensitivity analysis commonly used in quantitative finance and derivatives trading.



---



\## 🧠 Project Overview



The objective of this project is to build a flexible pricing engine capable of handling:



\- Closed-form analytical solutions

\- Simulation-based pricing

\- Path-dependent derivatives

\- Variance reduction techniques

\- Numerical Greeks estimation



The framework is designed in a modular structure to allow future extensions such as stochastic volatility models, calibration to market data, and performance optimization.



---



\## ⚙️ Implemented Models \& Methods



\### 🔹 Black–Scholes Analytical Model

\- European Call Option pricing

\- Closed-form benchmark solution

\- Used for validating Monte Carlo estimators



\### 🔹 Monte Carlo Simulation Framework

\- Geometric Brownian Motion (GBM) path simulation

\- Risk-neutral pricing approach

\- Configurable simulation size

\- Convergence analysis



\### 🔹 Variance Reduction Techniques

To improve estimator efficiency:

\- Antithetic Variates

\- Control Variates

\- Absolute error comparison against analytical benchmark

\- Convergence visualization



\### 🔹 Path-Dependent Options

Monte Carlo pricing implementation for:

\- Asian Options (Arithmetic Average)

\- Up-and-Out Barrier Call Options



These demonstrate pricing of exotic derivatives where closed-form solutions may not exist.



\### 🔹 Greeks Estimation (Sensitivity Analysis)



Numerical estimation using finite-difference Monte Carlo:



\- Delta

\- Gamma

\- Vega



This showcases sensitivity computation when analytical Greeks are unavailable.



---



\## 📊 Example Outputs



\- Black–Scholes European Call Price

\- Asian Option Price (Monte Carlo)

\- Barrier Option Price

\- Monte Carlo Delta, Gamma, Vega

\- Variance Reduction Convergence Graph



---



\## 🏗 Project Structure



The project is organized as follows:



\- models/

&nbsp; - black\_scholes.py



\- monte\_carlo/

&nbsp; - variance\_reduction.py

&nbsp; - asian.py

&nbsp; - barrier.py



\- greeks/

&nbsp; - finite\_difference.py



\- main.py  

\- requirements.txt  

\- README.md  



---



\## 🛠 Technologies Used



\- Python

\- NumPy

\- Matplotlib



---



\## 🚀 Potential Future Enhancements



\- Heston Stochastic Volatility Model

\- Implied Volatility Solver

\- Pathwise Monte Carlo Greeks

\- Parallelization / Performance Optimization

\- Calibration to Market Data



---



\## 👨‍💻 Author



\*\*HARSH AMBADE\*\*



Aspiring Quantitative Developer | Financial Engineering Enthusiast

