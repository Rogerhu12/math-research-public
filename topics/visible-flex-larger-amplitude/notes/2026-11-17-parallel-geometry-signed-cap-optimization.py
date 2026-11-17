#!/usr/bin/env python3
"""Exact budgets and reproducible numerical exploration for the signed C2 cap.

No files are written. The rational candidate is proved feasible by the checks
below and the companion mathematical note. The scalar optimization is numerical
evidence only. --samples evaluates the defining convolution by polar quadrature.
"""

import argparse
from fractions import Fraction as Q
import json
import math


def moment_polynomial(radius, height_over_slope):
    r, s = radius, height_over_slope
    return r**4 * s - 2 * r**3 * s**2 + Q(2, 3) * r**2 * s**3 + r * s**4 + s**5 / 5


def exact_candidate():
    tau0, tau, isolation, support = Q(39, 1250), Q(301, 10000), Q(3, 40), Q(1, 8)
    amplitude, slope = Q(3, 10000), Q(2, 125)
    smoothing = Q(3, 2) * slope * tau
    inner_radius = support - smoothing
    s = amplitude / slope
    lhs = 1 / tau0 + 2 * slope / isolation + 4 * amplitude / isolation**2
    rhs = (1 - 2 * amplitude / isolation)**2 / tau
    moment = 2 * slope * moment_polynomial(inner_radius, s)
    baseline_over_pi = Q(27, 6400000000)
    gain_lower = moment / (baseline_over_pi * Q(22, 7))
    # pi > 3 and the exact kernel integral give K*tau < 1600/1617.
    hessian_ratio_upper = Q(1600, 1617)
    assert lhs < rhs
    assert 2 * amplitude < isolation
    assert hessian_ratio_upper < 1
    assert s < Q(2, 5) * inner_radius  # sqrt(2)-1 > 2/5.
    assert gain_lower > Q(77, 10)
    assert tau / (1 + 2 * amplitude) > Q(3, 100)
    return {
        "status": "exact rational feasible cap component; no new closed isometric surface",
        "source_reach": tau0,
        "target_reach": tau,
        "cap_radius": Q(1, 5),
        "required_global_support_isolation": isolation,
        "outer_support_radius": support,
        "height_bound": amplitude,
        "gradient_bound": slope,
        "smoothing_radius": smoothing,
        "inner_support_radius": inner_radius,
        "height_over_slope": s,
        "reach_lhs": lhs,
        "reach_rhs": rhs,
        "reach_margin": rhs - lhs,
        "hessian_times_target_reach_strict_upper": hessian_ratio_upper,
        "full_diameter_upper": 1 + 2 * amplitude,
        "new_reach_over_full_diameter_lower": tau / (1 + 2 * amplitude),
        "required_old_hold_ratio": Q(1, 5) * (1 + 2 * amplitude) + 2 * amplitude,
        "fixed_signed_B2": moment,
        "fixed_signed_B2_decimal": float(moment),
        "B2_gain_lower_using_pi_lt_22_over_7": gain_lower,
        "area_increment_over_pi_upper": slope**2 * support**2,
        "volume_increment": Q(0),
        "centroid_increment": [Q(0), Q(0), Q(0)],
    }


def numerical_boundary(height):
    tau0, tau, isolation, support = 0.0312, 0.0301, 0.075, 0.125
    slope = isolation / 2 * ((1 - 2 * height / isolation)**2 / tau
                            - 1 / tau0 - 4 * height / isolation**2)
    if slope <= 0:
        return 0.0, slope, 0.0, 0.0
    inner_radius = support - 1.5 * slope * tau
    s = min(height / slope, (math.sqrt(2) - 1) * inner_radius)
    value = 2 * slope * float(moment_polynomial(inner_radius, s))
    return value, slope, inner_radius, s


def numerical_search():
    tau0, tau, d = 0.0312, 0.0301, 0.075
    aa = 4 / (tau * d * d)
    bb = 4 / (tau * d) + 4 / (d * d)
    cc = 1 / tau - 1 / tau0
    max_height = 2 * cc / (bb + math.sqrt(bb * bb - 4 * aa * cc))
    grid_n = 4096
    values = [numerical_boundary(max_height * i / grid_n)[0]
              for i in range(grid_n + 1)]
    index = max(range(grid_n + 1), key=values.__getitem__)
    lo = max_height * max(0, index - 1) / grid_n
    hi = max_height * min(grid_n, index + 1) / grid_n
    ratio = (math.sqrt(5) - 1) / 2
    left, right = hi - ratio * (hi - lo), lo + ratio * (hi - lo)
    vl, vr = numerical_boundary(left)[0], numerical_boundary(right)[0]
    for _ in range(90):
        if vl < vr:
            lo, left, vl = left, right, vr
            right = lo + ratio * (hi - lo)
            vr = numerical_boundary(right)[0]
        else:
            hi, right, vr = right, left, vl
            left = hi - ratio * (hi - lo)
            vl = numerical_boundary(left)[0]
    height = (lo + hi) / 2
    value, slope, radius, s = numerical_boundary(height)
    feasible = float(exact_candidate()["fixed_signed_B2"])
    return {
        "status": "4097-point boundary scan and local golden search; not a certified global optimum",
        "height": height,
        "gradient": slope,
        "inner_radius": radius,
        "height_over_gradient": s,
        "B2": value,
        "rational_candidate_fraction_of_numerical_value": feasible / value,
    }


def cone_cap(x, y, radius, height, slope):
    distance = min(radius - math.hypot(x, y), abs(abs(x) - abs(y)) / math.sqrt(2))
    if distance <= 0:
        return 0.0
    sign = 1 if x*x >= y*y else -1
    return sign * min(height, slope * distance)


def convolution_samples():
    import numpy as np
    candidate = exact_candidate()
    h = float(candidate["height_bound"])
    g = float(candidate["gradient_bound"])
    eta = float(candidate["smoothing_radius"])
    radius = float(candidate["inner_support_radius"])
    points = [(0.0, 0.0), (0.08, 0.0), (0.0, 0.08), (0.04, 0.04),
              (0.02, 0.0), (0.12, 0.0), (0.126, 0.0)]
    results = []
    for ntheta in [128, 256, 512, 1024]:
        nodes, weights = np.polynomial.legendre.leggauss(32)
        radii, weights = (nodes + 1) / 2, weights / 2
        angles = 2 * np.pi * np.arange(ntheta) / ntheta
        dx, dy = eta * radii[:, None] * np.cos(angles), eta * radii[:, None] * np.sin(angles)
        weighted_kernel = weights[:, None] * radii[:, None]
        weighted_kernel *= (1275 / (1024 * np.pi)) * (1 - radii[:, None]**16)**3
        out = []
        for x, y in points:
            xx, yy = x - dx, y - dy
            distances = np.minimum(radius - np.hypot(xx, yy),
                                   np.abs(np.abs(xx) - np.abs(yy)) / np.sqrt(2))
            f = np.sign(xx*xx - yy*yy) * np.minimum(h, g * np.maximum(distances, 0))
            out.append(float(np.sum(f * weighted_kernel) * 2 * np.pi / ntheta))
        results.append({"radial_gauss_order": 32, "angular_order": ntheta, "values": out})
    expected_abs_component = 2720 / (2261 * math.pi)
    ridge_exact = g / math.sqrt(2) * (0.02 - eta * expected_abs_component)
    return {
        "status": "numerical evaluations of the exact convolution definition; no full flex evaluated",
        "points": points,
        "refinements": results,
        "known_exact_values": {"point_0": 0, "point_1": h, "point_2": -h,
                               "point_3": 0, "point_4_formula_value": ridge_exact, "point_6": 0},
    }


def direct_integral_check():
    from scipy.integrate import quad
    data = exact_candidate()
    r = float(data["inner_support_radius"])
    s = float(data["height_over_slope"])
    g = float(data["gradient_bound"])
    def angular_integral(u):
        if u == 0:
            return 0.0
        splits = sorted(set([0.0, r, min(r, s / u), max(0.0, r-s), r/(1+u)]))
        total = 0.0
        for a, b in zip(splits, splits[1:]):
            if b > a:
                v, _ = quad(lambda radius: radius**3 * min(s, r-radius, radius*u),
                            a, b, epsabs=1e-20, epsrel=1e-12)
                total += v
        return u * total
    integral, error = quad(angular_integral, 0, 1/math.sqrt(2),
                           points=[s/(r-s)], epsabs=1e-20, epsrel=1e-11)
    value = 32 * g * integral
    exact = float(data["fixed_signed_B2"])
    return {"status": "independent numerical quadrature check of the exact moment formula",
            "quadrature_B2": value, "exact_formula_B2": exact,
            "absolute_difference": abs(value-exact),
            "quadrature_error_estimate_not_certified": 32*g*error}


def as_json(value):
    if isinstance(value, Q):
        return str(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--samples", action="store_true")
    parser.add_argument("--check-integral", action="store_true")
    args = parser.parse_args()
    output = {"strict_candidate": exact_candidate(), "numerical_search": numerical_search()}
    if args.samples:
        output["convolution_samples"] = convolution_samples()
    if args.check_integral:
        output["independent_integral_check"] = direct_integral_check()
    print(json.dumps(output, default=as_json, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
