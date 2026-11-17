#!/usr/bin/env python3
"""Exact design budgets for nonnegative graphs on two supporting plane caps.

The source surface's supporting planes and complete separation are hypotheses,
not certified by this script. No files are written. Optional checks integrate
the explicit radial component and sample its fixed C2 convolution.
"""

import argparse
from fractions import Fraction as F
import json
import math


TAU = F(39, 1250)
A = F(7, 100)
B = F(13, 200)
D0 = F(13, 200)
RC = F(1, 5)
ETA = F(1, 10000)
ELL = F(1, 40)


def common_budget(height, hessian_bound, b2_over_pi, volume_over_pi,
                  area_increment_over_pi):
    assert A + B + D0 == RC
    assert 2 * A > 2 * B
    assert D0 > 2 * TAU
    assert hessian_bound < 1 / TAU
    assert TAU / (1 + 2 * height) >= F(3, 100)
    return {
        "source_assumptions": "closed embedded family, reach >= tau, fixed supporting plane caps, true support-to-complement distance >= d0",
        "additional_quotient_upper_assumption": "unmarked image family consists of rotations about the cap axis",
        "source_reach_and_preserved_reach": TAU,
        "plane_cap_radius": RC,
        "bump_center_offset": A,
        "bump_support_radius": B,
        "required_actual_distance": D0,
        "cross_piece_distance_margin": D0 - 2 * TAU,
        "height": height,
        "hessian_bound": hessian_bound,
        "hessian_margin": 1 / TAU - hessian_bound,
        "full_diameter_upper": 1 + 2 * height,
        "reach_over_full_diameter_lower": TAU / (1 + 2 * height),
        "required_source_hold_ratio_using_monotonicity": F(1, 5) * (1 + 2 * height),
        "B2_over_pi": b2_over_pi,
        "B2_decimal": float(b2_over_pi) * math.pi,
        "B2_ratio_to_R625_weak_cap": b2_over_pi / F(27, 6400000000),
        "added_volume_over_pi": volume_over_pi,
        "area_increment_over_pi_upper": area_increment_over_pi,
        "quotient_distance_upper_from_phase_alignment": height,
    }


def cubic_candidate():
    h = F(19, 1000)
    k = 6 * h / (B * B)
    b2 = A * A * B * B * h
    return common_budget(h, k, b2, B * B * h, F(12, 5) * h * h)


def broad_candidate(k):
    r = B - ETA
    h = k * ELL * ELL
    plateau_radius = r - 2 * ELL
    assert plateau_radius > ETA > 0
    one_mass_over_pi = h * (r*r - 2*r*ELL + F(7, 6)*ELL*ELL)
    one_gradient_energy_over_pi = F(4, 3) * k*k * (r-ELL) * ELL**3
    answer = common_budget(h, k, 4*A*A*one_mass_over_pi,
                           4*one_mass_over_pi, 2*one_gradient_energy_over_pi)
    answer.update({
        "design": "fixed radial C1,1 quadratic profile convolved with the nonnegative radial C2 kernel",
        "smoothing_radius": ETA,
        "pre_smoothing_support_radius": r,
        "quadratic_ramp_length": ELL,
        "pre_smoothing_plateau_radius": plateau_radius,
        "single_bump_mass_over_pi": one_mass_over_pi,
        "single_bump_gradient_energy_over_pi": one_gradient_energy_over_pi,
    })
    return answer


def radial_profile(radius, k=30.0):
    r = float(B - ETA)
    ell = float(ELL)
    plateau = r - 2 * ell
    height = k * ell * ell
    if radius <= plateau:
        return height
    if radius <= plateau + ell:
        return height - k * (radius-plateau)**2 / 2
    if radius < r:
        return k * (r-radius)**2 / 2
    return 0.0


def numerical_checks():
    import numpy as np
    from scipy.integrate import quad
    r, ell, eta = float(B-ETA), float(ELL), float(ETA)
    k = 30.0
    plateau = r - 2 * ell
    integral = 0.0
    for left, right in [(0, plateau), (plateau, plateau+ell), (plateau+ell, r)]:
        value, _ = quad(lambda radius: 2*radius*radial_profile(radius, k),
                        left, right, epsabs=1e-16, epsrel=1e-12)
        integral += value
    exact = float(broad_candidate(F(30))["single_bump_mass_over_pi"])
    points = [0.0, plateau, plateau+ell, r, float(B), 0.07]
    nodes, weights = np.polynomial.legendre.leggauss(32)
    radial_nodes, weights = (nodes+1)/2, weights/2
    result = []
    for ntheta in [128, 256, 512]:
        angles = 2*np.pi*np.arange(ntheta)/ntheta
        dx = eta * radial_nodes[:, None] * np.cos(angles)
        dy = eta * radial_nodes[:, None] * np.sin(angles)
        kernel = (1275/(1024*np.pi)) * (1-radial_nodes[:, None]**16)**3
        coefficients = weights[:, None] * radial_nodes[:, None] * kernel
        values = []
        for x in points:
            rr = np.hypot(x-dx, dy)
            height = k*ell*ell
            sampled = np.where(rr <= plateau, height,
                      np.where(rr <= plateau+ell, height-k*(rr-plateau)**2/2,
                      np.where(rr < r, k*(r-rr)**2/2, 0.0)))
            values.append(float(np.sum(sampled*coefficients) * 2*np.pi/ntheta))
        result.append({"angular_order": ntheta, "radial_gauss_order": 32, "values": values})
    return {
        "scope": "component integral and convolution evaluation only; no source closed flex certified",
        "single_mass_over_pi_quadrature": integral,
        "single_mass_over_pi_exact_formula": exact,
        "absolute_difference": abs(integral-exact),
        "radial_sample_points": points,
        "convolution_refinements": result,
    }


def encode(value):
    if isinstance(value, F):
        return str(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    output = {"cubic_strict": cubic_candidate(),
              "wide_K30_strict": broad_candidate(F(30)),
              "wide_K32_normalized_boundary": broad_candidate(F(32)),
              "optimality_scope": "K=32 maximizes B2 only in this fixed l,eta,a,b family under the stated diameter bound; no global cap optimum claimed"}
    if args.check:
        output["numerical_checks"] = numerical_checks()
    print(json.dumps(output, default=encode, sort_keys=True, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
