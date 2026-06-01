---
title: "Quantum mechanics before the wavefunction"
date: 2025-11-18
categories:
  - blog
tags:
  - physics
mathjax: true
---

Disclaimer: 

Below infomation is not meant to be used in any serious manner as it is just personal research.
only quantum physics I can remember is 'particles in the box' from university level general physics course.




As far as I know, one of the most precise sets of experimental data in physics came from a very simple object: a cavity heated until it glowed. The radiation escaping through a small hole in the cavity wall was found to have a very specific intensity as a function of wavelength. This curve is now known as the blackbody spectrum. Classical physics seemed perfectly capable of handling the problem, but the resulting formulas failed in a dramatic way.The resolution proposed by Max Planck in 1900 introduced a single modification in the energy of radiation and, with it, the first appearance of the quantum.

Consider a large cavity at a temperature $T$. A small aperture allows observation of the radiation inside without significantly disturbing it. The radiation field in the cavity can be described by standing electromagnetic waves satisfying the boundary conditions at the walls.
A standard idealisation is a cube of side $L$, volume $V=L^3$, with perfectly conducting walls. The electromagnetic field inside can be decomposed into normal modes labelled by an integer triplet $(n_x,n_y,n_z)$ and a polarisation index. Each mode has a frequency

$$\omega = c\,|\vec{k}|,\qquad\vec{k} = \frac{\pi}{L}(n_x, n_y, n_z),$$

where $c$ is the speed of light. Each allowed mode behaves, classically, like a harmonic oscillator with frequency $\omega$.

The aim is to find the spectral energy density $u(\nu,T)$, defined such that $u(\nu,T)\, d\nu$ is the energy per unit volume in modes with frequencies between $\nu$ and $\nu + d\nu$, where $\nu = \omega/2\pi$.

To compute the energy in the radiation field, one first counts how many modes lie in a given frequency interval. The allowed wavevectors $\vec{k}$ form a cubic lattice in $k$-space with spacing $\pi/L$ in each direction. For large L, the lattice can be approximated as continuous, and the number of modes with wavevectors in a spherical shell between $k$ and $k+dk$ is proportional to the volume of the shell. Number of lattice points in shell can be obtained as

$$dN_{\text{modes}} = \frac{V}{(2\pi)^3}\, 4\pi k^2\,dk \times g_{\text{pol}} = \frac{V}{\pi^2}\,k^2\,dk$$

where $g_{\text{pol}} = 2$ counts the two possible polarisations of light. Using $\omega = c k$ and $\nu = \omega / 2\pi = c k / 2\pi$;

$$k = \frac{2\pi\nu}{c},\qquad dk = \frac{2\pi}{c}\, d\nu.$$

$$dN_{\text{modes}}
= \frac{V}{\pi^2}\left(\frac{2\pi\nu}{c}\right)^2 \frac{2\pi}{c}\, d\nu
= \frac{8\pi V \nu^2}{c^3}\, d\nu.$$

Thus, the number density of modes per unit frequency is

$$g(\nu)\equiv \frac{1}{V}\frac{dN_{\text{modes}}}{d\nu}
= \frac{8\pi \nu^2}{c^3}.$$

Classical statistical mechanics assigns energy to each mode according to the [equipartition theorem](https://en.wikipedia.org/wiki/Equipartition_theorem). Each mode is a harmonic oscillator with quadratic kinetic and potential energy. Equipartition states that each degree of freedom with quadratic term contributes $\tfrac{1}{2}k_B T$ to the average energy. The harmonic oscillator has two quadratic degrees of freedom (kinetic + potential), so the average energy per mode is $\langle E \rangle_{\text{classical}} = k_B T$.

The spectral energy density is then

$$u_{\text{RJ}}(\nu,T) = g(\nu) \times \langle E \rangle_{\text{classical}}
= \frac{8\pi \nu^2}{c^3}\,k_B T$$

This is the [Rayleigh–Jeans law](https://en.wikipedia.org/wiki/Rayleigh–Jeans_law). The formula is simple, elegant, and obviously diverges as $\nu \to \infty$ or $\lambda \to 0$. This divergence is the ultraviolet catastrophe.

The total energy density predicted by classical physics is

$$U_{\text{classical}}(T) = \int_0^\infty u_{\text{RJ}}(\nu,T)\, d\nu
= \int_0^\infty \frac{8\pi \nu^2}{c^3} k_B T\, d\nu$$

which diverges. The classical cavity would contain infinite energy. The measured spectrum of a blackbody at temperature $T$ is finite and peaked at a particular frequency $\nu_{\text{peak}}(T)$. For fixed $T$, the intensity rises with $\nu$, reaches a maximum, and then falls at higher frequency. The Rayleigh–Jeans law reproduces the low-frequency part but fails completely in the ultraviolet region. This mismatch can be illustrated numerically. Suppose a cavity is at $T = 3000\,\text{K}$. The Rayleigh–Jeans law predicts that the intensity keeps growing as $\nu^2$, while the measured spectrum displays a peak in the visible or near-infrared region.

![RJ vs Planks]({{ "/assets/images/2025-11-18-quantum_before_wavefunction_1.png" | relative_url }})

Planck approached the problem by modelling the cavity walls as a collection of charged oscillators. Each oscillator of frequency $\nu$ exchanges energy with the radiation field at the same frequency. The key assumption is that the distribution of energy among these oscillators controls the spectrum of the emitted radiation. Initially, Planck tried to derive the correct distribution using purely classical arguments, but the attempt failed. He then introduced a assumption: the energy of each oscillator is quantised in discrete steps,

$$E_n = n h \nu,\qquad n = 0,1,2,\dots$$

where $h$ is a new constant (Planck’s constant). This assumption implies that the oscillator cannot have arbitrary energy; it can only occupy levels spaced by $h\nu$. The oscillators are assumed to be in thermal equilibrium at temperature T. Their probability to occupy the level E_n follows the Boltzmann distribution,

$$ P_n = \frac{e^{-E_n/k_B T}}{Z},$$

with partition function

$$Z = \sum_{n=0}^{\infty} e^{-E_n/k_B T}
= \sum_{n=0}^{\infty} e^{-n h \nu / k_B T}$$

This is a geometric series with ratio $q = e^{-h\nu/k_B T}$, so

$$Z = \frac{1}{1 - e^{-h\nu/k_B T}}$$

The average energy is

$$\langle E \rangle = \sum_{n=0}^{\infty} E_n P_n = \frac{1}{Z} \sum_{n=0}^{\infty} (n h \nu) e^{-n h \nu / k_B T}$$

Use the identity for $\|q\|<1$

$$\sum_{n=0}^{\infty} n q^n = \frac{q}{(1-q)^2}$$

Set $q = e^{-h\nu/k_B T}$ to obtain

$$\sum_{n=0}^{\infty} n e^{-n h \nu / k_B T}
= \frac{e^{-h\nu/k_B T}}{\left(1 - e^{-h\nu/k_B T}\right)^2}$$

Thus:

$$\langle E \rangle
= h\nu\, \frac{e^{-h\nu/k_B T}}{\left(1 - e^{-h\nu/k_B T}\right)^2} \cdot \left(1 - e^{-h\nu/k_B T}\right)
= \frac{h\nu}{e^{h\nu/k_B T}-1}$$

The average energy of a Planck oscillator is therefore

$$\langle E \rangle_{\text{Planck}} = \frac{h\nu}{e^{h\nu/k_B T}-1}$$

Using the same density of states $g(\nu) = 8\pi\nu^2/c^3$, the spectral energy density becomes

$$u_{\text{Planck}}(\nu,T)
= g(\nu)\, \langle E \rangle_{\text{Planck}}
= \frac{8\pi\nu^2}{c^3} \frac{h\nu}{e^{h\nu/k_B T}-1}$$

Thus Planck’s law is

$$u_{\text{Planck}}(\nu,T)
= \frac{8\pi h \nu^3}{c^3} \frac{1}{e^{h\nu/k_B T}-1}
$$

This expression agrees with experimental measurements across the entire range of wavelengths. Planck’s formula contains classical physics as a limiting case. At low frequencies $h\nu \ll k_B T$ (or long wavelengths), exponential term can be expanded as $e^{h\nu/k_B T} \approx 1 + \frac{h\nu}{k_B T}$, so

$$\langle E \rangle_{\text{Planck}}
= \frac{h\nu}{e^{h\nu/k_B T}-1}
\approx k_B T$$

Therefore

$$u_{\text{Planck}}(\nu,T)
\approx \frac{8\pi\nu^2}{c^3} k_B T
= u_{\text{RJ}}(\nu,T)$$

and the Rayleigh–Jeans law is recovered. At high frequencies $h\nu \gg k_B T$, $\langle E \rangle_{\text{Planck}} \approx h\nu\, e^{-h\nu/k_B T}$, so

$$u_{\text{Planck}}(\nu,T)
\approx \frac{8\pi h \nu^3}{c^3}\, e^{-h\nu/k_B T}$$

which is Wien’s law. The spectrum falls exponentially in the ultraviolet, avoiding the catastrophe.

Einstein noticed that in this Wien limit, the distribution behaves like a dilute gas of particles. If this expression is divided by the energy $h\nu$, the number of quanta per unit volume per unit frequency becomes 

$$n(\nu,T)
= \frac{u(\nu,T)}{h\nu}
\approx \frac{8\pi \nu^2}{c^3} e^{-h\nu/k_B T}$$

This is exactly the form of the Maxwell–Boltzmann distribution for a classical gas:

$$n \propto e^{-E/k_B T}$$

Thus the high-frequency part of blackbody radiation behaves as if light itself consists of independent energy packets of size $h\nu$. From this formal observation, Einstein proposed the quantum of light.

This assumption made possible the explanation of the [photoelectric effect](https://en.wikipedia.org/wiki/Photoelectric_effect). In experiments where light illuminates a metal surface, the emitted electrons display a maximum kinetic energy $K_{\max}$ related to the frequency $\nu$ of the incident radiation. Classical electromagnetic theory predicted that the energy transferred to the electron should depend on the intensity of the light, not its frequency, but experiments showed otherwise. Einstein’s law states:

$$K_{\max} = h\nu - \phi$$

where \phi is the work function of the metal.
This formula implies:
- Increasing the light intensity increases the number of emitted electrons, not their energy.
- Increasing the frequency increases the energy of each electron.
- No electrons are emitted if $h\nu < \phi$, no matter the intensity.

These features follow directly if light energy arrives in discrete quanta $h\nu$. Einstein next applied quantisation to the internal vibrations of solids. Classical theory predicts the internal energy of a solid should grow indefinitely with temperature, and the heat capacity $C_V$ should approach the [Dulong–Petit value](https://en.wikipedia.org/wiki/Dulong–Petit_law)

$$C_V \approx 3 N k_B$$

where $N$ is the number of atoms. This value is accurate at high temperatures but fails dramatically at low temperatures, where measured heat capacities fall to zero rather than remain constant.

Einstein modelled a solid as $3N$ independent harmonic oscillators, each with frequency $\nu_0$. He then used the average quantum oscillator energy,

$$\langle E \rangle(\nu_0, T)
= \frac{h\nu_0}{e^{h\nu_0/k_B T} - 1}$$

The internal energy becomes

$$U(T) = 3N \langle E \rangle(\nu_0, T)
= \frac{3N h\nu_0}{e^{h\nu_0/k_B T}-1}$$

The heat capacity is

$$C_V = \left(\frac{\partial U}{\partial T}\right)_V
= 3N k_B
\left(
\frac{h\nu_0}{k_B T}
\right)^2
\frac{e^{h\nu_0/k_B T}}{(e^{h\nu_0/k_B T}-1)^2}$$

Introduce the dimensionless variable $x = \frac{h\nu_0}{k_B T}$, then

$$C_V = 3N k_B \frac{x^2 e^x}{(e^x - 1)^2}$$

At high temperature $x\ll 1$,

$$C_V \to 3Nk_B$$

consistent with the Dulong–Petit law.

At low temperature $x\gg 1$,

$$C_V \approx 3N k_B x^2 e^{-x} \sim e^{-h\nu_0/k_B T}$$

which falls exponentially, matching qualitative experimental behaviour. This model reproduced the qualitative variation of heat capacities in solids, particularly the exponential decrease at low temperature. Yet the model contained a simplification that was too restrictive: all $3N$ oscillators of the solid were assumed to vibrate at the same frequency $\nu_0$. Real crystalline solids do not vibrate in this way. Their atoms form a coupled system that supports a spectrum of vibrational modes, much like a three-dimensional elastic medium. In 1912, Peter Debye refined Einstein’s model by assigning continuous vibrational frequencies to the solid. This change altered the low-temperature behaviour from an exponential to a $T^3$ law, matching experimental measurements.

In a real crystal, atoms interact with their neighbours and vibrate collectively. The normal modes of vibration are standing waves with wavevector $\vec{k}$. In the long-wavelength limit these vibrations behave like classical sound waves with

- longitudinal waves with velocity $v_L$,
- transverse waves with velocity $v_T$.

Debye simplified the full elastic theory by assuming a single effective sound velocity v_s, producing an approximate relation:

$$\omega = v_s \, k$$

This is the acoustic phonon approximation: the lowest-energy modes behave as sound waves. Hw applied the same counting method used for electromagnetic modes in a cavity. Each vibrational mode corresponds to a lattice wavevector $\vec{k}$. The number of modes with wavenumbers between k$ and $k+dk$ is

$$dN = \frac{V}{2\pi^2} k^2\, dk \times 3$$

where the factor of 3 counts the three possible polarisations (1 longitudinal + 2 transverse). Convert $k$ to frequency via $\omega = v_s k$, so

$$k = \frac{\omega}{v_s}, \qquad dk = \frac{d\omega}{v_s}.$$

Thus;

$$
g(\omega)d\omega
= \frac{3V}{2\pi^2}\left( \frac{\omega}{v_s} \right)^2 \frac{d\omega}{v_s}
= \frac{3V\omega^2}{2\pi^2 v_s^3}\, d\omega.
$$

Debye’s density of states is therefore

$$
g(\omega) = \frac{3V\omega^2}{2\pi^2 v_s^3}.
$$

The harmonic approximation predicts infinitely many modes as $\omega \to \infty$, which is unphysical. A real crystal has only $3N$ degrees of freedom. Debye therefore chose a maximum frequency $\omega_D$ (the Debye cutoff) so that the total number of modes is exactly $3N$:

$$
\int_0^{\omega_D} g(\omega)\, d\omega = 3N.
$$

Insert the expression for $g(\omega)$:

$$
\int_0^{\omega_D} \frac{3V\omega^2}{2\pi^2 v_s^3}\, d\omega
= \frac{3V}{2\pi^2 v_s^3}\, \frac{\omega_D^3}{3}
= 3N.
$$

Solve for the cutoff frequency:

$$
\omega_D^3 = \frac{6\pi^2 v_s^3 N}{V}.
$$

Or in terms of the Debye temperature

$$
\Theta_D = \frac{\hbar\omega_D}{k_B}.
$$

The Debye temperature sets the energy scale of all phononic excitations. Each mode of frequency $\omega$ behaves as a quantum oscillator with energy

$$
\varepsilon(\omega,T) = \frac{\hbar\omega}{e^{\hbar\omega/k_B T}-1}
$$

The total internal energy is a sum (integral) over all modes

$$
U(T) = \int_0^{\omega_D} g(\omega)\, \varepsilon(\omega,T)\, d\omega.
$$

Substitute $g(\omega)$ and $\varepsilon$

$$
U(T) =
\int_0^{\omega_D}
\frac{3V\omega^2}{2\pi^2 v_s^3}
\frac{\hbar\omega}{e^{\hbar\omega/k_B T}-1} \, d\omega.
$$

Introduce the dimensionless variable

$$
x = \frac{\hbar\omega}{k_B T}, \qquad
x_D = \frac{\hbar\omega_D}{k_B T} = \frac{\Theta_D}{T}.
$$

Then,
$$
U(T) =
\frac{3V}{2\pi^2 v_s^3}
\frac{(k_B T)^4}{\hbar^3}
\int_{0}^{x_D} \frac{x^3}{e^x - 1}\, dx.
$$

Instead of volume $V$ and velocity $v_s$, we may rewrite the constant prefactor using the number of atoms $N$. Using the earlier cutoff condition, the final standard form (Debye internal energy) can be written as

$$
U(T) = 9N k_B T \left( \frac{T}{\Theta_D} \right)^3
\int_0^{\Theta_D/T} \frac{x^3}{e^x - 1}\, dx.
$$

to obtain heat capacity at constant volume, 

$$
C_V = \left( \frac{\partial U}{\partial T} \right)_V.
$$

The result is:
$$
C_V = 9 N k_B \left( \frac{T}{\Theta_D} \right)^3
\int_0^{\Theta_D/T}
\frac{x^4 e^x}{(e^x - 1)^2}\, dx.
$$

The integral is known as the Debye function:

$$
D_3(y) = \frac{3}{y^3}\int_0^{y}\frac{x^3}{e^x - 1}\, dx.
$$

Thus:

$$
C_V = 3 N k_B\, D_3(\Theta_D/T).
$$

For $T \ll \Theta_D$, the upper limit $x_D = \Theta_D/T$ is large, so:

$$
\int_0^{\infty} \frac{x^3}{e^x - 1}\, dx = \frac{\pi^4}{15}.
$$

Thus:

$$
C_V \approx 9N k_B \left( \frac{T}{\Theta_D} \right)^3
\frac{\pi^4}{15}.
$$

$$
C_V \propto T^3 \qquad (T \ll \Theta_D).
$$

This $T^3$ law matches precise low-temperature heat-capacity data for insulators, solving a major discrepancy unresolved by Einstein’s model.

Numerous clues pointed toward the discreteness of energy in both radiation and matter. Yet the behaviour of electrons inside atoms remained unexplained. Classical electrodynamics predicted that an accelerating electron in orbit would continuously radiate energy and spiral into the nucleus within a tiny fraction of a second. The existence of stable atoms contradicted this prediction in the most direct way.

Niels Bohr resolved this contradiction by proposing a model in which electrons occupy quantised stationary orbits, each with a definite energy. Radiation is not emitted by orbital motion, but only when the electron makes a discrete jump between these orbits. The model introduced an entirely new structure: energy levels and transition frequencies. These ideas provided a critical bridge to Heisenberg’s matrix mechanics more than a decade later.

# Bohr’s Atom: Quantised Orbits and Discrete Spectra

Bohr’s model was based on three postulates:

- Stationary orbits exist: Electrons move in certain allowed orbits in which they do not radiate.
- Angular momentum is quantised: $L = m v r = n\hbar,\qquad n = 1,2,3,\dots$
- Radiation is emitted or absorbed only in transitions: $h\nu_{nm} = E_n - E_m.$


For an electron of mass m and charge -e orbiting a nucleus of charge +e, the Coulomb force balances centripetal force:

$$
\frac{m v^2}{r} = \frac{e^2}{4\pi\varepsilon_0 r^2}\
$$

Solve for the velocity

$$
v^2 = \frac{e^2}{4\pi\varepsilon_0 m r}
$$

The total energy of the orbit is

$$
E = K + V
= \frac12 m v^2 - \frac{e^2}{4\pi\varepsilon_0 r}
$$

Using the force-balance expression:

$$
K = \frac12\frac{e^2}{4\pi\varepsilon_0 r}
$$

so

$$
E = -\frac{1}{2}\frac{e^2}{4\pi\varepsilon_0 r}
$$

Thus:

$$
E(r) = -\frac{e^2}{8\pi\varepsilon_0 r}
$$

Use Bohr’s angular momentum quantisation

$$
L = m v r = n\hbar
$$

Use the earlier expression for $v^2$

$$
v = \sqrt{\frac{e^2}{4\pi\varepsilon_0 m r}}.
$$

Insert into $L = mvr$

$$
m r \sqrt{\frac{e^2}{4\pi\varepsilon_0 m r}} = n\hbar.
$$

or
\sqrt{m r \frac{e^2}{4\pi\varepsilon_0}} = n\hbar.

$$
m r \frac{e^2}{4\pi\varepsilon_0} = n^2\hbar^2.
$$

Solve for r to obtain

$$
r_n = \frac{4\pi\varepsilon_0 n^2\hbar^2}{m e^2}.
$$


Define the Bohr radius:
$$
a_0 = \frac{4\pi\varepsilon_0\hbar^2}{m e^2} = 5.29177\times 10^{-11}\ \text{m}.
$$

Thus:

$$
r_n = n^2 a_0.
$$

Insert $r_n$ into the classical energy formula

$$
E_n = -\frac{e^2}{8\pi\varepsilon_0 r_n}
= -\frac{e^2}{8\pi\varepsilon_0 n^2 a_0}.
$$

Using the definition of $a_0$:

$$
E_n = -\frac{m e^4}{8\varepsilon_0^2 h^2}\frac{1}{n^2}.
$$

In standard units:

$$
E_n = -\frac{13.6\ \text{eV}}{n^2}.
$$

This matches the observed hydrogen spectrum, decades before Schrödinger’s equation. When an electron transitions from $n \to m$, the emitted radiation has frequency:

$
\nu_{nm} = \frac{E_n-E_m}{h}.
$$

With

$$
E_n = -\frac{13.6\ \text{eV}}{n^2}
$$

the formula becomes:

$$
\nu_{nm}
= \frac{13.6\ \text{eV}}{h}\left(\frac{1}{m^2}-\frac{1}{n^2}\right).
$$

Using $1/\lambda = \nu/c$, this yields the Rydberg formula:

$$
\frac{1}{\lambda_{nm}}
= R_\infty \left( \frac{1}{m^2} - \frac{1}{n^2} \right).
$$

The Rydberg constant predicted by Bohr is:

$$
R_\infty = \frac{m e^4}{8\varepsilon_0^2 h^3 c}
= 1.097\times 10^7\ \text{m}^{-1}
$$

matching experiment. Examples:
- $n=3\to 2: 656.3\ \text{nm}$ (H-α line)
- $n=4\to 2: 486.1\ \text{nm}$ (H-β line)
- $n=5\to 2: 434.0\ \text{nm}$ (H-γ line)

These spectral lines constitute the empirical backbone of early quantum theory.

Bohr’s model reproduced hydrogen spectra but still invoked classical orbits. To reconcile the two, Bohr introduced the correspondence principle, asserting that ''For large quantum numbers n, quantum results must merge smoothly with classical periodic motion.''

Classically, the electron in orbit with frequency \omega(n) produces harmonics

$$
x(t) = \sum_{\alpha=-\infty}^{\infty} X_\alpha(n) e^{i\alpha\omega(n)t}
$$

Quantum mechanically, transitions n\to m produce frequencies:

$$
\omega_{nm} = \frac{E_n - E_m}{\hbar}
$$


In the limit $n,m\to\infty$ with $n-m=\alpha$ fixed

$$
\omega_{nm} \approx \alpha\omega(n)
$$

Thus, quantum transition frequencies approach the classical harmonic frequencies. This is the conceptual seed of Heisenberg’s idea: atomic behaviour should be expressed in terms of transition frequencies and intensities, not unobservable orbits.


Bohr’s model had structural problems:
- The electron should radiate even in a stationary orbit (classical electrodynamics violated).
- Multi-electron atoms could not be handled in any consistent way.
- Elliptical orbits (Sommerfeld’s extension) created complex patterns of frequencies requiring new quantisation rules.
- The mechanism by which radiation frequencies were produced from orbit motion was internally inconsistent.

Most importantly, the intensities of spectral lines did not follow from Bohr’s model. One could compute the frequencies $\nu_{nm}$, but not the strengths of lines. Experiments yield both. Classical motion predicted intensities proportional to $|X_\alpha(n)|^2$, the Fourier coefficients of the orbit, but these did not match observed atomic spectra. Between 1916 and 1925, Arnold Sommerfeld, Paul Epstein, Wilson, and Einstein refined Bohr’s ideas into a theory of multiperiodic classical motion. This framework keeps the classical trajectory of an electron but imposes new quantisation rules on the action variables of the motion. The goal was to compute not only frequencies but also intensities of spectral lines. 

An integrable mechanical system with $f$ degrees of freedom has action–angle coordinates $(J_i, \theta_i)$, with $i = 1,\dots,f$

In these coordinates, the angles increase linearly in time, $\dot{\theta_i} = \omega_i$, and the actions $J_i$ are constants of motion.

This motion is multiperiodic. Any observable $x(t)$ can be expanded in a Fourier series over the integer lattice:

$$
x(t) = \sum_{\vec{\alpha} \in \mathbb{Z}^f} X_{\vec{\alpha}}(J)\,
e^{i(\vec{\alpha}\cdot\vec{\omega}) t}.
$$

Here:
- $\vec{\alpha} = (\alpha_1,\dots,\alpha_f) \in \mathbb{Z}^f$
- $\vec{\omega} = (\omega_1,\dots,\omega_f)$ is the vector of fundamental frequencies.

In hydrogen (Kepler motion), the orbit is doubly periodic, so $f=2$.
This produces harmonics labelled by $\vec{\alpha} = (\alpha_r, \alpha_\theta)$, where each index corresponds to radial and angular oscillations.

Sommerfeld, Wilson, and Epstein introduced the quantisation conditions

$$
J_i = n_i h,\qquad n_i = 0,1,2,\dots
$$

where the action integrals are

$$
J_i = \oint p_i\, dq_i.
$$

For hydrogen:
- $J_r = n_r h$ (radial action),
- $J_\theta = n_\theta h = L$ (angular momentum).

This leads to elliptical orbits of different eccentricities. The semi-major axis remains:

$$
a = \frac{J_r + J_\theta}{2\pi} \frac{1}{m e^2/(4\pi \varepsilon_0)}.
$$

Energy depends only on the total action:

$$
n = n_r + n_\theta
$$

so the energy-level formula still reduces to:

$$
E_n = -\frac{13.6\ \text{eV}}{n^2},
$$

matching Bohr's theory, but it still could not produce the intensities of spectral lines.

The mismatch between classical and observed spectra

Classical prediction

Frequencies of emitted radiation:
\omega_{\vec{\alpha}} = \vec{\alpha}\cdot\vec{\omega}(n_r,n_\theta).

Quantum observation

Atomic lines have frequencies:
\omega_{nm} = \frac{E_n - E_m}{\hbar}.

Key mismatch:
	•	Classical frequencies depend on one orbit labelled by (n_r,n_\theta).
	•	Spectral lines correspond to differences between two energy levels n\to m.

Thus:
	•	Classical: one index \vec{\alpha}.
	•	Quantum: two indices (n,m).

Even worse:
	•	Classical intensities |X_{\vec{\alpha}}|^2 do not match experimental intensities.





- Quantised Orbits (Bohr)
  - Bohr atomic postulates
  - Classical motion in the Coulomb potential
  - Quantisation -> Bohr radius
  - Hydrogen atom
  - Clue for Matrix mechanic
    - discrte E
    - Transition frequency $\omega_{nm}$

- Multiperiodic Motion -> Fourier 
  - Basic of Multiperiodic Motion
  - Sommerified's action
  - Classical radiation -> mismatch
  - BKS / virsual oscillator -> n,m indeces
  - Matrix

-  Umdeutung paper
  - principle ->  use only observable quantities
  - Reinterprtet Fourier -> multiplication table rule -> Born: "oh wow this is matrix multiplication!!" -> BJ commutator
  - MATRICES MECHANICS !!!


References

History
-  The Genesis of Quantum Theory

BB
- http://hyperphysics.phy-astr.gsu.edu/hbase/mod6.html

Debye
- http://hyperphysics.phy-astr.gsu.edu/hbase/Solids/phonon.html