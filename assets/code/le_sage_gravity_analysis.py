from __future__ import annotations

from dataclasses import dataclass
from math import exp, pi
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


G = 6.67430e-11
C = 2.99792458e8
AU = 1.495978707e11
EARTH_ORBITAL_SPEED = 2.978e4
PROTON_MASS = 1.67262192369e-27
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "images"


@dataclass(frozen=True)
class Body:
    name: str
    mass: float
    radius: float


SUN = Body("Sun", 1.98847e30, 6.9634e8)
EARTH = Body("Earth", 5.9722e24, 6.371e6)

SAMPLE_KAPPAS = [1.0e-14, 1.0e-13, 3.0e-13, 5.0e-13, 7.6e-13]


def geometric_area(body: Body) -> float:
    return pi * body.radius * body.radius


def optical_depth(body: Body, kappa: float) -> float:
    return kappa * body.mass / geometric_area(body)


def suppression_factor(body: Body, kappa: float) -> float:
    tau = optical_depth(body, kappa)
    if tau == 0.0:
        return 1.0
    return (1.0 - exp(-tau)) / tau


def force_ratio_to_newton(body_a: Body, body_b: Body, kappa: float) -> float:
    return suppression_factor(body_a, kappa) * suppression_factor(body_b, kappa)


def required_pressure(kappa: float) -> float:
    return 4.0 * pi * G / (kappa * kappa)


def minimum_corpuscle_speed(source_mass: float, separation: float, kappa: float) -> float:
    anisotropy = kappa * source_mass / (4.0 * pi * separation * separation)
    return EARTH_ORBITAL_SPEED / anisotropy


def heating_power_per_mass(kappa: float, corpuscle_speed: float = C) -> float:
    pressure = required_pressure(kappa)
    energy_density = 3.0 * pressure
    return 0.25 * energy_density * corpuscle_speed * kappa


def required_number_density(
    kappa: float,
    corpuscle_mass: float = PROTON_MASS,
    corpuscle_speed: float = C,
) -> float:
    pressure = required_pressure(kappa)
    return 3.0 * pressure / (corpuscle_mass * corpuscle_speed * corpuscle_speed)


def exact_shadow_fraction(target_radius: float, separation: np.ndarray | float) -> np.ndarray:
    separation_array = np.asarray(separation, dtype=float)
    ratio = np.clip(target_radius / separation_array, 0.0, 1.0)
    return 0.5 * (1.0 - np.sqrt(1.0 - ratio * ratio))


def far_field_shadow_fraction(target_radius: float, separation: np.ndarray | float) -> np.ndarray:
    separation_array = np.asarray(separation, dtype=float)
    return (target_radius * target_radius) / (4.0 * separation_array * separation_array)


def random_unit_vectors(sample_count: int, rng: np.random.Generator) -> np.ndarray:
    mu = rng.uniform(-1.0, 1.0, sample_count)
    phi = rng.uniform(0.0, 2.0 * np.pi, sample_count)
    radial = np.sqrt(1.0 - mu * mu)
    return np.column_stack((radial * np.cos(phi), radial * np.sin(phi), mu))


def ray_hits_sphere(directions: np.ndarray, center: np.ndarray, radius: float) -> np.ndarray:
    projection = directions @ center
    center_norm_squared = float(center @ center)
    discriminant = projection * projection - (center_norm_squared - radius * radius)
    return (projection > 0.0) & (discriminant >= 0.0)


def monte_carlo_shadow_fraction(
    target_radius: float,
    separation: float,
    sample_count: int = 120_000,
    seed: int = 7,
) -> float:
    rng = np.random.default_rng(seed)
    directions = random_unit_vectors(sample_count, rng)
    center = np.array([separation, 0.0, 0.0])
    return float(np.mean(ray_hits_sphere(directions, center, target_radius)))


def monte_carlo_shadow_curve(
    target_radius: float,
    separations: np.ndarray,
    sample_count: int = 120_000,
    seed: int = 7,
) -> np.ndarray:
    fractions = []
    for index, separation in enumerate(separations):
        fractions.append(
            monte_carlo_shadow_fraction(
                target_radius,
                float(separation),
                sample_count=sample_count,
                seed=seed + index,
            )
        )
    return np.asarray(fractions)


def plot_shadow_geometry(output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    separations = np.geomspace(1.15, 20.0, 300)
    exact = exact_shadow_fraction(1.0, separations)
    far_field = far_field_shadow_fraction(1.0, separations)
    monte_carlo_separations = np.array([1.2, 1.4, 1.8, 2.5, 3.5, 5.0, 8.0, 12.0, 18.0])
    monte_carlo = monte_carlo_shadow_curve(1.0, monte_carlo_separations)

    fig, axis = plt.subplots(figsize=(8.6, 5.0), constrained_layout=True)
    axis.loglog(
        separations,
        exact,
        color="#203864",
        linewidth=2.8,
        label="exact solid-angle shadow",
    )
    axis.loglog(
        separations,
        far_field,
        color="#2b7a78",
        linewidth=2.4,
        linestyle="--",
        label=r"far-field $R^2/(4r^2)$",
    )
    axis.scatter(
        monte_carlo_separations,
        monte_carlo,
        color="#c44536",
        s=42,
        zorder=3,
        label="Monte Carlo rays",
    )
    axis.set_xlabel(r"separation / target radius, $r/R$")
    axis.set_ylabel("fraction of sky shadowed")
    axis.set_title("Pure shielding geometry really does want an inverse-square law")
    axis.grid(True, which="both", alpha=0.28)
    axis.legend(frameon=False)
    fig.savefig(output_path, format="svg")
    plt.close(fig)


def plot_constraint_scan(output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    kappas = np.geomspace(1.0e-14, 1.0e-12, 240)
    force_ratios = np.array([force_ratio_to_newton(SUN, EARTH, kappa) for kappa in kappas])
    minimum_speeds = np.array([minimum_corpuscle_speed(SUN.mass, AU, kappa) for kappa in kappas]) / C

    fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.8), constrained_layout=True)

    axes[0].semilogx(kappas, force_ratios, color="#2b6f77", linewidth=2.8)
    axes[0].axvline(7.6e-13, color="#9c7a18", linestyle="--", linewidth=1.6)
    axes[0].set_xlabel(r"coupling per unit mass, $\kappa$ (m$^2$/kg)")
    axes[0].set_ylabel(r"toy force / Newton")
    axes[0].set_title("Opacity ruins the mass law")
    axes[0].grid(True, alpha=0.28)

    axes[1].loglog(kappas, minimum_speeds, color="#c45c3b", linewidth=2.8)
    axes[1].axhline(1.0, color="#444444", linestyle=":", linewidth=1.6)
    axes[1].axvline(7.6e-13, color="#9c7a18", linestyle="--", linewidth=1.6)
    axes[1].set_xlabel(r"coupling per unit mass, $\kappa$ (m$^2$/kg)")
    axes[1].set_ylabel(r"minimum corpuscle speed / $c$")
    axes[1].set_title("Drag pushes the theory past relativity")
    axes[1].grid(True, which="both", alpha=0.28)

    fig.savefig(output_path, format="svg")
    plt.close(fig)


def format_row(kappa: float) -> str:
    tau_sun = optical_depth(SUN, kappa)
    ratio = force_ratio_to_newton(SUN, EARTH, kappa)
    pressure = required_pressure(kappa)
    min_speed_over_c = minimum_corpuscle_speed(SUN.mass, AU, kappa) / C
    heating = heating_power_per_mass(kappa)
    proton_density = required_number_density(kappa)
    return (
        f"{kappa:>9.2e}  "
        f"{tau_sun:>7.3f}  "
        f"{ratio:>7.3f}  "
        f"{pressure:>11.2e}  "
        f"{min_speed_over_c:>9.2f}  "
        f"{heating:>11.2e}  "
        f"{proton_density:>11.2e}"
    )


def main() -> None:
    plot_shadow_geometry(OUTPUT_DIR / "le-sage-monte-carlo.svg")
    plot_constraint_scan(OUTPUT_DIR / "le-sage-constraints.svg")

    print("Le Sage gravity toy model for the Sun-Earth system")
    print()
    print("kappa      tau_sun  F/F_Newt    P_required      v_min/c      qdot(v=c)    n_p(v=c)")
    print("(m^2/kg)                        (Pa)                         (W/kg)       (1/m^3)")
    for kappa in SAMPLE_KAPPAS:
        print(format_row(kappa))


if __name__ == "__main__":
    main()
