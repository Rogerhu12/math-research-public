#!/usr/bin/env python3
"""Exact shared-R quintic stage 127 and continuous metric/curvature bounds.

The nodal data are explicit finite choices from the existing accepted .25
response. This proves properties of the newly defined C2 map over the same
true R58 background, not exactness of its original PDE, JS oracle, or FD.
"""
import argparse
from fractions import Fraction as Q
import json
import math
from pathlib import Path
import time

from q060_true_background_oracle import Q060TrueBackgroundOracle, file_sha256, mpf_fraction


def trim(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(a, b):
    out = [Q(0)] * max(len(a), len(b))
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[i] += v
    return trim(out)


def scale(a, value):
    return trim([v * value for v in a])


def radius_product(poly, r0, span):
    return add(scale(poly, r0), [Q(0)] + scale(poly, span))


def derivative(poly, span, order):
    p = list(poly)
    for _ in range(order):
        p = [i * p[i] / span for i in range(1, len(p))] or [Q(0)]
    return trim(p)


def bernstein_abs(poly):
    n = len(poly) - 1
    values = [sum((poly[j] * Q(math.comb(k, j), math.comb(n, j))
                   for j in range(k + 1)), Q(0)) for k in range(n + 1)]
    return max(map(abs, values))


def evaluate(poly, t):
    value = Q(0)
    for c in reversed(poly):
        value = value * t + c
    return value


def hermite(y0, d0, dd0, y1, d1, dd1, h):
    delta = y1 - y0
    u0, u1, v0, v1 = h * d0, h * d1, h * h * dd0, h * h * dd1
    return [y0, u0, v0 / 2,
            10 * delta - 6 * u0 - 4 * u1 - Q(3, 2) * v0 + v1 / 2,
            -15 * delta + 8 * u0 + 7 * u1 + Q(3, 2) * v0 - v1,
            6 * delta - 3 * u0 - 3 * u1 - v0 / 2 + v1 / 2]


def harmonic_add(destination, frequency, poly, sine=False):
    if sine and frequency == 0:
        return
    if frequency < 0:
        frequency = -frequency
        if sine:
            poly = scale(poly, -1)
    destination[frequency] = add(destination.get(frequency, [Q(0)]), poly)


def physical_background_box(oracle, data):
    """Enclose the entire literal-R stage, allowing its inner source join."""
    rlo = Q.from_float(data["nodes"][0]["radiusJS"])
    rhi = Q.from_float(data["nodes"][-1]["radiusJS"])
    anchor = oracle.primitives(0, 1, 0)["r"]
    delta = Q(1, 10**6)
    for _ in range(16):
        inner = oracle.integrate(0, 0, 1 - delta, 1)
        outer = oracle.integrate(0, 1, 0, Q(1, 16) + delta)
        left = anchor - inner[0] - oracle.alpha * inner[1]
        right = anchor + outer[0] + oracle.alpha * outer[1]
        if oracle.hi(left) < oracle.lo(oracle.qi(rlo)) and oracle.lo(right) > oracle.hi(oracle.qi(rhi)):
            break
        delta *= 2
    else:
        raise ArithmeticError("Could not enclose the literal radius stage in the true chart")
    if delta >= Q(1, 100):
        raise ArithmeticError("Unexpectedly large chart displacement")
    a = oracle.local_jets(0, 0, 1 - delta, 1)
    b = oracle.local_jets(0, 1, 0, Q(1, 16) + delta)
    w = oracle.k.hull([a["w"], b["w"]])
    w0 = Q.from_float(float((oracle.lo(w) + oracle.hi(w)) / 2))
    dw = max(abs(mpf_fraction(oracle.lo(w)) - w0), abs(mpf_fraction(oracle.hi(w)) - w0))
    return {"literal_radius_bounds": [str(rlo), str(rhi)],
            "source_cover": [[0, 0, str(1 - delta), "1"], [0, 1, "0", str(Q(1, 16) + delta)]],
            "left_radius": oracle.bounds(left), "right_radius": oracle.bounds(right),
            "w_range": oracle.bounds(w), "auxiliary_w0_exact": str(w0),
            "maximum_abs_w_minus_w0_exact": str(dw),
            "strict_monotone_cover_verified": True,
            "w0_scope": "Auxiliary constant in an exact error decomposition, not a new background or an alpha choice."}, w0, dw


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data", type=Path, required=True)
    ap.add_argument("--constants", type=Path, required=True)
    ap.add_argument("--normalization-certificate", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    started = time.monotonic()
    data = json.loads(a.data.read_text())
    if (data["stage"], data["rawCell"], data["rawSegment"], data["rawLeft"], data["rawRight"]) != (127, 0, 1, 0, 1 / 16):
        raise ValueError("This first continuous component certificate is for the actual cusp stage 127.")
    if data["finiteScope"]["M"] != 24 or data["finiteScope"]["quadrature"] != 512:
        raise ValueError("Finite field scope changed")
    oracle = Q060TrueBackgroundOracle(a.constants, a.normalization_certificate)
    background, w0, dw = physical_background_box(oracle, data)
    print(json.dumps({"stage": "true_background_R_cover", "seconds": time.monotonic() - started,
                      "w": background["w_range"], "cover": background["source_cover"]}), flush=True)
    planar, heights = data["planarModes"], data["heightModes"]
    P, C = len(planar), len(planar) + len(heights)
    nodes, mids = data["nodes"], data["midpoints"]
    if len(mids) != len(nodes) - 1:
        raise ValueError("Missing original midpoint data")
    rows = []
    total_shared_identities = 0
    maximum_metric = Q(0)
    maximum_eta_sq = Q(0)
    maximum_beta_sq = Q(0)
    maximum_position = Q(0)
    maximum_midpoint_differences = [Q(0)] * 3
    all_radii = [Q.from_float(row["radiusJS"]) for row in nodes]
    if any(y <= x for x, y in zip(all_radii, all_radii[1:])):
        raise ValueError("The explicit literal R mesh is not increasing")

    for index, (left, right, middle) in enumerate(zip(nodes, nodes[1:], mids)):
        r0, r1 = all_radii[index:index + 2]
        span = r1 - r0
        polynomials, derivs, norms = [], [[], [], []], [[], [], []]
        for component in range(C):
            l = [Q.from_float(row[component]) for row in left["coefficients"]]
            r = [Q.from_float(row[component]) for row in right["coefficients"]]
            poly = hermite(l[0], l[1], l[2], r[0], r[1], r[2], span)
            polynomials.append(poly)
            for order in range(3):
                d = derivative(poly, span, order)
                if evaluate(d, Q(0)) != l[order] or evaluate(d, Q(1)) != r[order]:
                    raise ArithmeticError("Exact common two-jet identity failed")
                total_shared_identities += 2
                derivs[order].append(d)
                norms[order].append(bernstein_abs(d))

        # Combine linearized metric terms at equal true angular frequencies
        # before taking absolute values. All polynomial operations are exact.
        Alinear, Blinear, Clinear = {}, {}, {}
        for i, frequency in enumerate(planar):
            value, first = derivs[0][i], derivs[1][i]
            harmonic_add(Alinear, frequency - 1, scale(first, 2))
            harmonic_add(Blinear, frequency - 1,
                         add(radius_product(first, r0, span), scale(value, -frequency)), sine=True)
            harmonic_add(Clinear, frequency - 1, scale(radius_product(value, r0, span), 2 * frequency))
        for j, frequency in enumerate(heights):
            harmonic_add(Alinear, frequency, scale(derivs[1][P + j], 2 * w0))
            harmonic_add(Blinear, frequency, scale(derivs[0][P + j], -w0 * frequency), sine=True)
        la = sum((bernstein_abs(v) for v in Alinear.values()), Q(0))
        lb = sum((bernstein_abs(v) for v in Blinear.values()), Q(0))
        lc = sum((bernstein_abs(v) for v in Clinear.values()), Q(0))

        frequencies = planar + heights
        v0 = sum(norms[0], Q(0))
        vr = sum(norms[1], Q(0))
        vt = sum((abs(m) * b for m, b in zip(frequencies, norms[0])), Q(0))
        vrr = sum(norms[2], Q(0))
        vrt = sum((abs(m) * b for m, b in zip(frequencies, norms[1])), Q(0))
        vtt = sum((m * m * b for m, b in zip(frequencies, norms[0])), Q(0))
        hz_r = sum(norms[1][P:], Q(0))
        hz_t = sum((abs(m) * b for m, b in zip(heights, norms[0][P:])), Q(0))
        eta_sq = vr * vr + (vt / r0) ** 2
        A = la + 2 * dw * hz_r + vr * vr
        B = (lb + dw * hz_t) / r0 + eta_sq / 2
        Cbound = (lc + vt * vt) / (r0 * r0)
        metric = max(A, Cbound) + B

        # R58: |w| <= 41/100, |k_i(background)| <= 8. For the reference
        # orthonormal frame the connection coefficients give these bounds.
        h11 = vrr + Q(82, 25) * vr
        h12 = (vrt + vt / r0) / r0
        h22 = vtt / (r0 * r0) + vr / r0
        beta_sq = h11 * h11 + 2 * h12 * h12 + h22 * h22

        # All-angle differences from the finite original midpoint data are
        # exact rational Fourier l1 bounds at these 17 radial planes only.
        t = (Q.from_float(middle["radiusJS"]) - r0) / span
        if not 0 < t < 1:
            raise ValueError("Original midpoint is outside the chosen literal R span")
        differences = []
        for order in range(3):
            d = sum((abs(evaluate(derivs[order][i], t) - Q.from_float(middle["coefficients"][order][i]))
                     for i in range(len(frequencies))), Q(0))
            differences.append(d)
            maximum_midpoint_differences[order] = max(maximum_midpoint_differences[order], d)
        maximum_metric = max(maximum_metric, metric)
        maximum_eta_sq = max(maximum_eta_sq, eta_sq)
        maximum_beta_sq = max(maximum_beta_sq, beta_sq)
        maximum_position = max(maximum_position, v0)
        rows.append({"span": index, "radius_left_exact": str(r0), "radius_right_exact": str(r1),
                     "metric_upper_exact": str(metric), "eta_squared_upper_exact": str(eta_sq),
                     "covariant_hessian_squared_upper_exact": str(beta_sq),
                     "position_upper_exact": str(v0),
                     "linear_numerator_upper_exact": [str(v) for v in (la, lb, lc)],
                     "metric_component_abs_upper_exact": [str(v) for v in (A, B, Cbound)],
                     "midpoint_literal_reference_jet_difference_upper_exact": [str(v) for v in differences]})
        print(json.dumps({"span": index, "continuous_metric_upper": float(metric),
                          "midpoint_jet_difference": [float(v) for v in differences],
                          "seconds": time.monotonic() - started}), flush=True)

    eta = oracle.iv.sqrt(oracle.qi(maximum_eta_sq))
    beta = oracle.iv.sqrt(oracle.qi(maximum_beta_sq))
    if oracle.hi(eta) >= 1:
        raise ArithmeticError("Immersion was not proved by the perturbation bound")
    curvature = (8 + beta) / (1 - eta) ** 2
    passed = maximum_metric < Q(1, 10**6)
    result = {"status": "explicit_C2_stage_true_metric_gate_passed" if passed else "explicit_C2_stage_metric_gate_not_proved",
              "scope": __doc__, "source_sha256": file_sha256(__file__),
              "data_sha256": file_sha256(a.data), "oracle_provenance": oracle.provenance,
              "background_cover": background, "source_stage": 127,
              "radius_mesh_definition": "Exact binary64 radiusJS knot values, explicitly selected; no true-R interval midpoint is used as a breakpoint.",
              "map_definition": "The original true R58 rotational background plus Fourier coefficients interpolated by the unique exact quintic in physical R matching each pair of shared literal value/first/second jets.",
              "mean_definition": data["meanDefinition"],
              "literal_shared_two_jet_identities_checked": total_shared_identities,
              "spans": len(rows), "all_angle_and_continuous_radius": True,
              "continuous_metric_operator_upper": oracle.bounds(oracle.qi(maximum_metric)),
              "continuous_metric_gate": "1e-6", "metric_gate_passed": passed,
              "position_perturbation_upper": oracle.bounds(oracle.qi(maximum_position)),
              "normalized_first_jet_upper": oracle.bounds(eta),
              "normalized_covariant_hessian_upper": oracle.bounds(beta),
              "principal_curvature_absolute_upper": oracle.bounds(curvature),
              "reference_geometric_bounds": {"maximum_slope_exact": "41/100", "maximum_absolute_principal_curvature_exact": "8", "source": "R58 true 4.625 background, with the tight normalization proof. These are not old 3.125 bounds."},
              "midpoint_literal_reference_jet_difference_upper": [oracle.bounds(oracle.qi(v)) for v in maximum_midpoint_differences],
              "midpoint_difference_scope": "Exact all-angle Fourier l1 bounds at the 17 saved midpoint radii; reference arrays are finite literal data, not a continuous PDE solution.",
              "planar_second_jet_selection": "Recorded fourth-order finite differences used only as explicit finite common node parameters.",
              "source_fd_step_comparison": data["secondStepComparison"],
              "global_tail_completed": False, "full_H_response": False,
              "bvp_solves_executed": 0, "shooting_iterations_executed": 0,
              "rows": rows, "seconds": time.monotonic() - started}
    a.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "metric": result["continuous_metric_operator_upper"],
                      "curvature": result["principal_curvature_absolute_upper"],
                      "seconds": result["seconds"], "output_sha256": file_sha256(a.out)}))


if __name__ == "__main__":
    main()
