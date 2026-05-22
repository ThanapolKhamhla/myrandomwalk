import numpy as np
import matplotlib.pyplot as plt

h = 6.62607015e-34   # Planck constant [J s]
kB = 1.380649e-23    # Boltzmann constant [J/K]
c = 2.99792458e8     # speed of light [m/s]

def u_rayleigh_jeans(nu, T):
    return 8 * np.pi * nu**2 * kB * T / c**3

def u_planck(nu, T):
    x = h * nu / (kB * T)
    return 8 * np.pi * h * nu**3 / (c**3 * (np.exp(x) - 1))

T = 3000.0  # temperature in K
nu = np.linspace(1e12, 1e15, 100)  # frequency range

u_RJ = u_rayleigh_jeans(nu, T)
u_P  = u_planck(nu, T)

plt.figure(figsize=(5, 4))
plt.plot(nu, u_RJ, label="Rayleigh–Jeans", color = 'red', linestyle='--')
plt.plot(nu, u_P, label="Blackbody", color = 'black')
plt.xlabel("Frequency ν [Hz]")
plt.ylabel("Spectral energy density u(ν, T) [J m⁻³ Hz⁻¹]")
plt.legend()
plt.tick_params(axis='both', which='both', direction='in', top=True, right=True)
# tick minors
plt.minorticks_on()
plt.grid()
plt.ylim(0, np.nanmax(u_P)*1.2)
plt.savefig("2025-11-18-quantum_before_wavefunction.png", dpi=300)
plt.show()
