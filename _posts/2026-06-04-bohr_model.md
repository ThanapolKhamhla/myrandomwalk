---
title: "Bohr Atomic Model"
categories:
  - blog
tags:
  - physics
classes: wide
mathjax: true
---



– It was almost as incredible as if you fired a 15 inch shell at a peice of tissue paper and it came pack and hit you- 


## Rutherford’s model of the atom

Total energy of atom 

$$
E = \frac{1}{2}mv^2 - \frac{1}{4\pi\epsilon_0}\frac{e^2}{r}
$$

from Newton's second law of angular force and electrostatic force

$$
\begin{align*}
  m\frac{v^2}{r} &= \frac{1}{4\pi\epsilon_0}\frac{e^2}{r^2} \\

  v^2 &= \frac{1}{4\pi\epsilon_0m}\frac{e^2}{r}
\end{align*}
$$

Thus

$$
\begin{align*}
  E &= \frac{1}{2}m \left(\frac{1}{4\pi\epsilon_0m}\frac{e^2}{r}\right) - \frac{1}{4\pi\epsilon_0}\frac{e^2}{r} \\
  
  &= -\frac{1}{8\pi\epsilon_0}\frac{e^2}{r}
\end{align*}
$$

the energy loss deu to radiation from charge $e$ with accelleration $a$ was descibed by Larmor's equation;

$$
\frac{dE}{dt} = - \frac{e^2a^2}{6\pi\epsilon_0c^3}
$$

again, from Newton's second law of angular force

$$
a = \frac{v^2}{r} = \frac{1}{4\pi\epsilon_0m}\frac{e^2}{r^2}
$$

energy loss become

$$
\begin{align*}
  \frac{dE}{dt} &= - \frac{e^2}{6\pi\epsilon_0c^3}\left(\frac{1}{4\pi\epsilon_0m}\frac{e^2}{r^2}\right) \\

  &= \frac{e^6}{96\pi^3\epsilon_0^3c^3m^2r^4}
\end{align*}
$$

So energy of the electron will gradually radiated away and finally combine with nucleus.  

But maybe it take billion of years so our measurement cannot observe the decay.

To find the time untill energy is deplete, let plug in derivative of total energy from above;

$$
\frac{dE}{dt} = \frac{1}{8\pi\epsilon_0}\frac{e^2}{r^2} \frac{dr}{dt} = \frac{e^6}{96\pi^3\epsilon_0^3c^3m^2r^4}
$$

$$
dt = \frac{12\pi^2\epsilon^2c^3m^2}{e^4}r^2dr
$$

integrate both side from $t = 0 \rightarrow t_0$ (time untill electron reach the nucleus) and $ = 0 r_0 \rightarrow 0$ (from atomic radius to 0)

$$
\begin{align*}
  \int_0^{t_0} dt &= \frac{12\pi^2\epsilon^2c^3m^2}{e^4} \int_{r_0}^{0} r^2dr \\

 t_0 &= \frac{4\pi^2\epsilon^2c^3m^2}{e^4} r_0^3
\end{align*}
$$

after inserting every constant and atomic radius of around 5 $nm$, the result is $t_0 \approx 100 \,ns$!!


## Bohr model

Bohr's quatisation:

$$
J = \oint_0^T p_\phi d\phi = nh \quad n = 1, 2, 3, ...
$$

where $p_\phi$ is the radial momentum canonically conjugate to the coordinate $q$, which is the radial position, and $T$ is one full orbital period.







## Hydrogen spectrum

Gustav Kirchhoff

Robert Bunsen

### Balmer

$$
\lambda = B \left(\frac{n^2}{n^2-4} \right) \quad B = 3.65 \times 10^{-7} m
$$

### Rydberg

$$
\frac{1}{\lambda} = R_H\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)
$$

no physical interpretation

### Bohr