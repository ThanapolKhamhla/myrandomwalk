---
title: "Tiny worker"
excerpt: "Le Sage tried to replace gravitational attraction with an invisible rain of fast corpuscles. The idea is clever, intuitive, and analytically disastrous."
categories:
  - blog
tags:
  - physics
classes: wide
mathjax: true
---

Sometimes failed theories are more revealing than successful ones. A successful theory usually reaches me when they are already compressed into textbook form, polished until all the anxiety that produced it has been hidden. A failed theory still shows its seams. I can still see what problem its creator was trying to solve, what kind of explanation felt satisfying at the time, and exactly where nature refused to cooperate. That is why Le Sage's theory of gravitation is still worth reading now. It is wrong, and wrong in a very instructive way, but it begins from a discomfort that is hard not to feel even today.

Newton's law of gravitation,

$$
F = G \frac{m_1 m_2}{r^2},
$$

is one of the great compressions in physics. With it we can organize falling bodies, tides, the Moon's motion, planetary orbits, and much of the visible order of the solar system. But the law leaves a wound behind. It tells us what happens with extraordinary precision, yet it does not tell us what local process, if any, is doing the work. "Action at a distance" is both triumph and irritation: a powerful rule, and an invitation to ask for a deeper mechanism.

Le Sage's answer is almost irresistibly concrete. Instead of one body mysteriously pulling another across empty space, we imagine the universe filled with tiny invisible corpuscles racing in from all directions at enormous speed. A single isolated body feels no net force because the impacts balance. Two nearby bodies, however, screen one another. Each removes a tiny part of the incoming flux that would otherwise strike the inward-facing side of the other. The outer sides still receive the full bombardment. The inner sides receive slightly less. The two bodies therefore drift together, not because they pull, but because they are pushed.

We might see immediately why this picture had appeal. It turns attraction into pressure imbalance. It replaces a remote influence with local collisions. It has the flavor of kinetic theory, the same style of explanation that later made gas pressure and heat feel intelligible. Nicolas Fatio de Duillier had already explored related corpuscular ideas before Georges-Louis Le Sage developed the picture more fully in the eighteenth century, and the broader philosophical urge behind the theory was perfectly understandable. If gravity is real, should it not come from some medium, some traffic of causes, some mechanism that operates locally rather than mysteriously? That instinct was not foolish at all.

The difficulty is that a vivid mechanism is not yet a viable theory. A viable theory must survive its own arithmetic. It must give the right dependence on distance, the right dependence on mass, the right behavior for moving bodies, and tolerable side effects. Le Sage's theory begins with one genuinely promising feature, and it is worth being fair about that before we start dismantling it. The geometry of shadowing really can produce something very close to an inverse-square law.

Suppose one spherical body of radius $R$ is seen from the center of another at separation $r$. The body blocks a circular patch of the sky. If its angular radius is $\alpha$, then the blocked fraction of the full sky is just the solid angle of a spherical cap divided by $4\pi$:

$$
f_{\mathrm{shadow}}(r) = \frac{1 - \cos\alpha}{2},
\qquad
\sin\alpha = \frac{R}{r}.
$$

Eliminating $\alpha$ gives the exact shadow fraction,

$$
f_{\mathrm{shadow}}(r) = \frac{1 - \sqrt{1 - (R/r)^2}}{2}.
$$

And in the far-field limit $r \gg R$, this becomes

$$
f_{\mathrm{shadow}}(r) \approx \frac{R^2}{4r^2}.
$$

So the geometry itself is not the embarrassing part of the theory. The angular size of the shadow really does want to produce a $1/r^2$ behavior. That is important, because it means Le Sage's idea is not defeated at the very first line of the calculation.

It is useful to see this numerically rather than only in symbols. All the code needed to reproduce the figures and printed results in this post is included inline in self-contained blocks. The next snippet computes the exact shadow fraction, compares it with the far-field approximation, then checks the same geometry with a Monte Carlo ray count. The plot it produces is the one shown immediately below.

```python
import matplotlib.pyplot as plt
import numpy as np


def exact_shadow_fraction(target_radius, separation):
    ratio = np.clip(target_radius / separation, 0.0, 1.0)
    return 0.5 * (1.0 - np.sqrt(1.0 - ratio * ratio))


def far_field_shadow_fraction(target_radius, separation):
    return target_radius**2 / (4.0 * separation**2)


def random_unit_vectors(sample_count, rng):
    mu = rng.uniform(-1.0, 1.0, sample_count)
    phi = rng.uniform(0.0, 2.0 * np.pi, sample_count)
    radial = np.sqrt(1.0 - mu * mu)
    return np.column_stack((radial * np.cos(phi), radial * np.sin(phi), mu))


def ray_hits_sphere(directions, center, radius):
    projection = directions @ center
    discriminant = projection * projection - (center @ center - radius * radius)
    return (projection > 0.0) & (discriminant >= 0.0)


def monte_carlo_shadow_fraction(target_radius, separation, sample_count=120_000, seed=7):
    rng = np.random.default_rng(seed)
    directions = random_unit_vectors(sample_count, rng)
    center = np.array([separation, 0.0, 0.0])
    return float(np.mean(ray_hits_sphere(directions, center, target_radius)))


separations = np.geomspace(1.15, 20.0, 300)
exact = exact_shadow_fraction(1.0, separations)
far_field = far_field_shadow_fraction(1.0, separations)
mc_r = np.array([1.2, 1.4, 1.8, 2.5, 3.5, 5.0, 8.0, 12.0, 18.0])
mc = np.array([monte_carlo_shadow_fraction(1.0, r, seed=7 + i) for i, r in enumerate(mc_r)])

fig, ax = plt.subplots(figsize=(8.6, 5.0), constrained_layout=True)
ax.loglog(separations, exact, linewidth=2.8, label="exact solid-angle shadow")
ax.loglog(separations, far_field, "--", linewidth=2.2, label=r"far-field $R^2/(4r^2)$")
ax.scatter(mc_r, mc, s=42, zorder=3, label="Monte Carlo rays")
ax.set_xlabel(r"separation / target radius, $r/R$")
ax.set_ylabel("fraction of sky shadowed")
ax.legend(frameon=False)
ax.grid(True, which="both", alpha=0.28)
plt.show()
```

![Monte Carlo ray-tracing check for Le Sage shielding geometry. The red points are Monte Carlo estimates, the dark curve is the exact solid-angle shadow fraction, and the dashed curve is the far-field inverse-square approximation.](/assets/images/le-sage-monte-carlo.svg)

*This is the fairest thing we can say for Le Sage's idea. The geometry cooperates. A shielding mechanism really can imitate inverse-square behavior once the bodies are well separated.*

That matters because it sharpens where the theory really fails. If all we asked was whether a small shadow in an isotropic flux can produce something proportional to $1/r^2$, the answer would be yes. The geometry does that willingly. But gravity is not only a distance law. It also scales with mass, it acts nearly universally on different kinds of matter, and it does not noticeably slow the planets down or roast them with absorbed flux. The moment we ask for all of that at once, Le Sage's theory starts to tighten around its own throat.

The standard analytic step is to write the force in the most generous possible form. Let the corpuscle bath carry an effective momentum flux, or pressure, $P$. Let body $i$ intercept the flux with effective cross-section $\sigma_i$. If body 2 blocks a fraction $\sigma_2/(4\pi r^2)$ of the sky seen by body 1, then the force scale is

$$
F_{\mathrm{Le\,Sage}} \approx P\,\sigma_1\,\frac{\sigma_2}{4\pi r^2}.
$$

If we now assume the interception cross-section is proportional to mass,

$$
\sigma_i = \kappa m_i,
$$

then the force becomes

$$
F_{\mathrm{Le\,Sage}} \approx \frac{P\kappa^2}{4\pi} \frac{m_1 m_2}{r^2},
$$

so matching Newton requires

$$
P = \frac{4\pi G}{\kappa^2}.
$$

This is the bargain the theory makes with nature. If $\kappa$ is small, the required background pressure becomes enormous. If $\kappa$ is large, bodies stop being optically thin and the effective interaction stops scaling cleanly with mass. The model then begins to saturate toward geometric area, exactly where gravity is supposed to keep looking universal.

We can capture that self-shielding with a simple saturation model,

$$
\sigma_{\mathrm{eff}} = A\left(1 - e^{-τ}\right),
\qquad
τ = \frac{\kappa m}{A},
\qquad
A = \pi R^2,
$$

where $τ$ is an optical depth and $A$ is the geometric cross-section. In the thin limit $τ \ll 1$, we recover $\sigma_{\mathrm{eff}} \approx \kappa m$. But once $τ$ is not small, bodies behave more like opaque screens than transparent mass-proportional absorbers.

At that point the code needs to do more than define helper functions. It should actually produce the figure that carries the argument. The next snippet computes the force suppression from opacity, estimates the minimum corpuscle speed needed to keep drag smaller than the Sun-induced anisotropy at Earth's orbit, and plots both constraints on the same parameter scan.

```python
from math import exp, pi

import matplotlib.pyplot as plt
import numpy as np


G = 6.67430e-11
C = 2.99792458e8
AU = 1.495978707e11
EARTH_ORBITAL_SPEED = 2.978e4

SUN_MASS = 1.98847e30
SUN_RADIUS = 6.9634e8
EARTH_MASS = 5.9722e24
EARTH_RADIUS = 6.371e6


def optical_depth(mass, radius, kappa):
    area = pi * radius * radius
    return kappa * mass / area


def suppression_factor(mass, radius, kappa):
    tau = optical_depth(mass, radius, kappa)
    return 1.0 if tau == 0.0 else (1.0 - exp(-tau)) / tau


def force_ratio_to_newton(kappa):
    return suppression_factor(SUN_MASS, SUN_RADIUS, kappa) * suppression_factor(EARTH_MASS, EARTH_RADIUS, kappa)


def minimum_corpuscle_speed(kappa):
    anisotropy = kappa * SUN_MASS / (4.0 * pi * AU * AU)
    return EARTH_ORBITAL_SPEED / anisotropy


kappas = np.geomspace(1.0e-14, 1.0e-12, 240)
force_ratios = np.array([force_ratio_to_newton(k) for k in kappas])
minimum_speeds_over_c = np.array([minimum_corpuscle_speed(k) for k in kappas]) / C

fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.8), constrained_layout=True)
axes[0].semilogx(kappas, force_ratios, linewidth=2.8)
axes[0].axvline(7.6e-13, linestyle="--", linewidth=1.6)
axes[0].set_xlabel(r"coupling per unit mass, $\kappa$ (m$^2$/kg)")
axes[0].set_ylabel("toy force / Newton")
axes[0].grid(True, alpha=0.28)

axes[1].loglog(kappas, minimum_speeds_over_c, linewidth=2.8)
axes[1].axhline(1.0, linestyle=":", linewidth=1.6)
axes[1].axvline(7.6e-13, linestyle="--", linewidth=1.6)
axes[1].set_xlabel(r"coupling per unit mass, $\kappa$ (m$^2$/kg)")
axes[1].set_ylabel(r"minimum corpuscle speed / $c$")
axes[1].grid(True, which="both", alpha=0.28)
plt.show()
```

![Two toy-model constraints for Le Sage gravity. Left: the predicted force law falls below Newton once the Sun ceases to be very optically thin. Right: the minimum corpuscle speed required to keep drag below gravity rapidly exceeds the speed of light.](/assets/images/le-sage-constraints.svg)

*The left panel is the price of opacity. The right panel is the price of motion through the bath. We do not find a comfortable parameter window in which both prices can be paid.*

The trap becomes especially sharp when we ask for the Sun to remain optically thin. That condition reads

$$
τ_\odot = \frac{\kappa M_\odot}{\pi R_\odot^2} \ll 1,
$$

and because

$$
\frac{\pi R_\odot^2}{M_\odot} \approx 7.6 \times 10^{-13}\,\mathrm{m^2/kg},
$$

we are pushed toward

$$
\kappa \ll 7.6 \times 10^{-13}\,\mathrm{m^2/kg}.
$$

But smaller $\kappa$ means larger required pressure because $P = 4\pi G/\kappa^2$. Even at the forgiving edge of this range, the pressure is already of order $1.5 \times 10^{15}\,\mathrm{Pa}$, corresponding to an energy density $u \sim 3P \sim 4 \times 10^{15}\,\mathrm{J/m^3}$. That is not a gentle hidden medium. It is a violent one.

The drag problem deepens the crisis because it is not an external criticism glued onto the model afterward. It comes from the model's own logic. A Le Sage force is produced by anisotropy in a flux, but a body moving through the same flux also creates anisotropy. If the body's speed is $u$ and the corpuscle speed is $v$, then the motion-induced anisotropy is of order $u/v$. To keep that smaller than the Sun-induced anisotropy, we need roughly

$$
\frac{u}{v} \lesssim \frac{\kappa M_\odot}{4\pi r^2}.
$$

At Earth's orbit, even the marginally transparent choice $\kappa = 7.6 \times 10^{-13}\,\mathrm{m^2/kg}$ gives

$$
v \gtrsim 5.5 \times 10^9\,\mathrm{m/s} \approx 18c.
$$

So the corpuscles already need to move faster than light simply to keep drag from competing with what the theory is trying to call gravity.

The question about particle mass leads to the same kind of trap. The force law does not fix one preferred corpuscle mass by itself. It fixes a momentum flux. If a corpuscle has mass $m_c$ and speed $v$, then the required number density is approximately

$$
P \sim \frac{1}{3} n m_c v^2,
\qquad
n \sim \frac{3P}{m_c v^2}.
$$

So a heavier corpuscle means fewer particles, while a lighter corpuscle means more of them. But this freedom does not rescue the theory. If we choose proton-mass corpuscles and the impossible generosity $v=c$, the required number density is still gigantic. And once momentum transfer is large enough to matter, energy transfer becomes destructive too.

Again, the code should show the result rather than merely define symbols. The next snippet prints representative numbers for the Sun-Earth system: optical depth, force suppression, required pressure, minimum corpuscle speed, heating rate at $v=c$, and the number density needed if the corpuscles are proton-mass.

```python
from math import exp, pi


G = 6.67430e-11
C = 2.99792458e8
AU = 1.495978707e11
EARTH_ORBITAL_SPEED = 2.978e4
PROTON_MASS = 1.67262192369e-27

SUN_MASS = 1.98847e30
SUN_RADIUS = 6.9634e8
EARTH_MASS = 5.9722e24
EARTH_RADIUS = 6.371e6


def optical_depth(mass, radius, kappa):
    return kappa * mass / (pi * radius * radius)


def suppression_factor(mass, radius, kappa):
    tau = optical_depth(mass, radius, kappa)
    return 1.0 if tau == 0.0 else (1.0 - exp(-tau)) / tau


def required_pressure(kappa):
    return 4.0 * pi * G / (kappa * kappa)


def minimum_corpuscle_speed(kappa):
    anisotropy = kappa * SUN_MASS / (4.0 * pi * AU * AU)
    return EARTH_ORBITAL_SPEED / anisotropy


def heating_power_per_mass(kappa, corpuscle_speed=C):
    energy_density = 3.0 * required_pressure(kappa)
    return 0.25 * energy_density * corpuscle_speed * kappa


def required_number_density(kappa, corpuscle_mass=PROTON_MASS, corpuscle_speed=C):
    return 3.0 * required_pressure(kappa) / (corpuscle_mass * corpuscle_speed * corpuscle_speed)


sample_kappas = [1.0e-14, 1.0e-13, 3.0e-13, 5.0e-13, 7.6e-13]
print("kappa      tau_sun  F/F_Newt    P_required      v_min/c      qdot(v=c)    n_p(v=c)")
for kappa in sample_kappas:
    ratio = suppression_factor(SUN_MASS, SUN_RADIUS, kappa) * suppression_factor(EARTH_MASS, EARTH_RADIUS, kappa)
    print(
        f"{kappa:>9.2e}  "
        f"{optical_depth(SUN_MASS, SUN_RADIUS, kappa):>7.3f}  "
        f"{ratio:>7.3f}  "
        f"{required_pressure(kappa):>11.2e}  "
        f"{minimum_corpuscle_speed(kappa) / C:>9.2f}  "
        f"{heating_power_per_mass(kappa):>11.2e}  "
        f"{required_number_density(kappa):>11.2e}"
    )
```

Running that block prints values of the following kind:

```text
kappa      tau_sun  F/F_Newt    P_required      v_min/c      qdot(v=c)    n_p(v=c)
 1.00e-14    0.013    0.993     8.39e+18    1410.53     1.89e+13     1.68e+29
 1.00e-13    0.131    0.937     8.39e+16     141.05     1.89e+12     1.68e+27
 3.00e-13    0.392    0.821     9.32e+15      47.02     6.31e+11     1.86e+26
 5.00e-13    0.654    0.726     3.36e+15      28.21     3.79e+11     6.71e+25
 7.60e-13    0.994    0.622     1.45e+15      18.56     2.49e+11     2.89e+25
```

For representative values, the theory corners itself almost immediately. When $\kappa = 1.0 \times 10^{-14}\,\mathrm{m^2/kg}$, the Sun is comfortably thin and the force law is still close to Newton, but the required pressure is about $8.4 \times 10^{18}\,\mathrm{Pa}$ and the drag constraint pushes the corpuscle speed to roughly $1.4 \times 10^3 c$. When $\kappa = 7.6 \times 10^{-13}\,\mathrm{m^2/kg}$, chosen only because it makes the Sun barely thin, the force ratio has already fallen to about $0.62$, the required pressure is still $1.5 \times 10^{15}\,\mathrm{Pa}$, the minimum speed is still about $18c$, and the heating rate at $v=c$ is around $2.5 \times 10^{11}\,\mathrm{W/kg}$. These are not small corrections. They are structural failures.

The geometry is not the villain here. The first sketch is clever. The inverse-square behavior can emerge from shadowing. The real problem appears only when we ask the same mechanism to do everything else gravity does: scale properly with mass, stay nearly universal across different bodies, avoid severe drag, avoid catastrophic heating, and remain dynamically gentle on astronomical scales. The very same feature that makes the theory appealing, a force built from an anisotropic flux, is also what makes the side effects unavoidable.

**Further reading.** 

- Max Jammer, *Concepts of Force*. very good historical guide to the long struggle over action at a distance, mechanism, and what it even means to explain a force.
- Stephen G. Brush, *The Kind of Motion We Call Heat*. This is broader than Le Sage alone, but it helps situate the whole mechanical imagination that made impact-based explanations feel so compelling.
- Sean Carroll, *Spacetime and Geometry*. Once we have seen why mechanical push-gravity struggles, it is clarifying to compare that failure with a modern theory in which gravity is not a flux of particles pushing through space but part of spacetime structure itself.
