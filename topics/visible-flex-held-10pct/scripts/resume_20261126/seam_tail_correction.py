#!/usr/bin/env python3
"""Bound an explicit tail-side C2 correction from two actual bound inputs.

Uses the new accepted bridge trace and stage 0 of one canonical common-R
tail map. Never substitutes interval midpoints into the exact map. Optional
baseline numbers produce explicitly conditional metric/curvature budgets.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
from math import comb, isqrt
from pathlib import Path
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
H = [
    [F(1), 0, 0, -F(10), F(15), -F(6)],
    [0, F(1), 0, -F(6), F(8), -F(3)],
    [0, 0, F(1, 2), -F(3, 2), F(3, 2), -F(1, 2)],
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    return json.loads(gzip.decompress(path.read_bytes()) if path.suffix == ".gz" else path.read_text())


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def fq(value):
    value = float(value)
    if not np.isfinite(value):
        raise ValueError("Nonfinite saved coefficient")
    return F.from_float(value)


def declared(value):
    return F(value) if isinstance(value, str) else fq(value)


def derivative(poly):
    return [(j + 1) * poly[j + 1] for j in range(len(poly) - 1)]


def value(poly, x):
    total = F(0)
    for coefficient in reversed(poly):
        total = total * x + coefficient
    return total


def bernstein_sup(poly, left, right):
    """Exact power-to-Bernstein bound after mapping [left,right] to [0,1]."""
    n = len(poly) - 1
    width = right - left
    shifted = [
        width ** j * sum((poly[k] * comb(k, j) * left ** (k - j)
                          for k in range(j, n + 1)), F(0))
        for j in range(n + 1)
    ]
    return max(
        abs(sum((shifted[j] * F(comb(k, j), comb(n, j))
                 for j in range(k + 1)), F(0)))
        for k in range(n + 1)
    )


def sqrt_upper(x):
    if x < 0:
        raise ArithmeticError("Negative squared bound")
    scale = 10 ** 80
    k = isqrt(x.numerator * scale * scale // x.denominator)
    if F(k, scale) ** 2 == x:
        return F(k, scale)
    upper = F(k + 1, scale)
    assert upper * upper > x
    return upper


def interval_rows(modes, array):
    if array.shape != (3, 2, len(modes)) or not np.all(np.isfinite(array)):
        raise ValueError("Invalid bridge trace tensor")
    result = {}
    for k, m in enumerate(modes):
        rows = []
        for j in range(3):
            lo, hi = fq(array[j, 0, k]), fq(array[j, 1, k])
            if lo > hi:
                raise ValueError("Reversed bridge interval")
            rows.append((lo, hi))
        result[int(m)] = rows
    return result


def difference(bridge, tail):
    result = {}
    for m in sorted(set(bridge) | set(tail)):
        left = bridge.get(m, [(F(0), F(0))] * 3)
        right = tail.get(m, [F(0)] * 3)
        result[m] = [(lo - b, hi - b) for (lo, hi), b in zip(left, right)]
    return result


def coefficient_polynomial(rows, length, order):
    centers = [(lo + hi) / 2 for lo, hi in rows]
    radii = [(hi - lo) / 2 for lo, hi in rows]
    poly = [F(0)] * 6
    basis = []
    for j in range(3):
        q = [F(v) * (-length) ** j for v in H[j]]
        for _ in range(order):
            q = derivative(q)
        q = [v * (-1 / length) ** order for v in q]
        basis.append(q)
        for k, v in enumerate(q):
            poly[k] += centers[j] * v
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly, basis, radii


def patch_bounds(planar, height, length, blocks):
    result = {}
    component = {}
    prepared = {}
    for name, group in (("planar", planar), ("height", height)):
        prepared[name] = {
            order: {m: coefficient_polynomial(rows, length, order)
                    for m, rows in group.items()}
            for order in range(3)
        }
    for radial, angular in ((0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)):
        best, best_p, best_h = F(0), F(0), F(0)
        for block in range(blocks):
            left, right = F(block, blocks), F(block + 1, blocks)
            bounds = []
            for name in ("planar", "height"):
                total = F(0)
                for mode, (center, basis, radii) in prepared[name][radial].items():
                    weight = F(abs(mode) ** angular)
                    if not weight:
                        continue
                    bound = bernstein_sup(center, left, right)
                    bound += sum((radius * bernstein_sup(q, left, right)
                                  for radius, q in zip(radii, basis)), F(0))
                    total += weight * bound
                bounds.append(total)
            squared = bounds[0] ** 2 + bounds[1] ** 2
            best = max(best, squared)
            best_p, best_h = max(best_p, bounds[0]), max(best_h, bounds[1])
        result[(radial, angular)] = sqrt_upper(best)
        component[(radial, angular)] = (best_p, best_h)
    return result, component


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ("bridge-trace", "bridge-certificate", "tail-stage", "tail-manifest",
                 "source-port", "out"):
        ap.add_argument("--" + name, type=Path, required=True)
    ap.add_argument("--lengths", default="1/10000,1/5000,1/2000,1/1000,1/500,1/200,1/100,1/50")
    ap.add_argument("--blocks", type=int, default=16)
    ap.add_argument("--conditional-baseline", type=Path)
    a = ap.parse_args()
    if a.blocks < 1:
        raise ValueError("Positive Bernstein subdivision count required")
    started = time.monotonic()
    audit = module("_seam_correction_input_gate", HERE / "seam_cut_height_compatibility.py")
    outward = audit.outward
    bridge_report, stage, manifest = map(read, (a.bridge_certificate, a.tail_stage, a.tail_manifest))
    if bridge_report["status"] != "accepted_prefix_true_cut_R_trace_enclosed":
        raise ValueError("Require the new bound accepted-prefix trace")
    if sha(a.bridge_trace) != bridge_report["npz_sha256"]:
        raise ValueError("Bridge trace bytes changed")
    if manifest["status"] != "selected_stages_share_one_literal_R_C2_definition":
        raise ValueError("Require an actually exported canonical shared-R tail map")
    if stage["status"] != "literal_R_stage_with_exact_common_boundary_two_jets" or stage["stage"] != 0:
        raise ValueError("Require stage 0 of the common-R tail")
    entry = next((v for v in manifest["files"] if v["stage"] == 0), None)
    if entry is None or entry["sha256"] != sha(a.tail_stage):
        raise ValueError("Tail stage is not bound to this manifest")
    if stage["sharing"]["mapHash"] != entry["mapHash"] or stage["boundInput"] != manifest["input"]:
        raise ValueError("Tail canonical map identity differs")
    chain_path = Path(manifest["input"]["path"])
    if sha(chain_path) != manifest["input"]["sha256"]:
        raise ValueError("Original saved mean-chain input changed")
    chain = read(chain_path)
    if chain["status"] != "all_saved_initial_states_matched_single_mean_chain":
        raise ValueError("Require the original common cumulative mean chain")
    if chain["all_stage_input_maximum_difference"] != 0:
        raise ValueError("Saved native stages do not match the accepted states")
    if chain["checkpoint"] != manifest["existingCheckpoint"]:
        raise ValueError("Tail checkpoint binding differs")
    raw_path = Path(chain["checkpoint"]["path"])
    if sha(raw_path) != chain["checkpoint"]["sha256"]:
        raise ValueError("Accepted tail packet changed")
    reference = HERE.parents[1] / "notes/2026-11-20-m3-m24-warm050-execution.json"
    packet, response, jets, spacing, count, arrays = audit.load_packet(raw_path, a.source_port, reference)
    if sha(a.source_port) != bridge_report["source_port_sha256"]:
        raise ValueError("Bridge and tail have different original physical ports")
    if spacing != 3:
        raise ValueError("This correction preserves the specified m3 symmetry")
    Rc, w = fq(.3), fq(.08)
    wR = -7 * w / Rc
    radii = [fq(v["radiusJS"]) for v in stage["nodes"]]
    if not radii or radii[-1] != Rc or any(v >= u for v, u in zip(radii, radii[1:])):
        raise ValueError("Invalid actual stage-0 R domain")
    cut = stage["nodes"][-1]
    if cut.get("canonicalNode") != 0:
        raise ValueError("Tail cut is not the common map's original node 0")
    pm, hm = list(map(int, stage["planarModes"])), list(map(int, stage["heightModes"]))
    if stage["finiteScope"]["M"] != count or stage["finiteScope"]["spacing"] != spacing:
        raise ValueError("Stage finite scope differs from its accepted response")
    if hm != list(range(0, 3 * count + 1, 3)):
        raise ValueError("Tail height modes are not the full accepted Fourier family")
    if pm != manifest["planarModes"] or hm != manifest["heightModes"]:
        raise ValueError("Stage Fourier definition differs from the common map")
    if len(set(pm)) != len(pm) or len(set(hm)) != len(hm) or 0 not in hm:
        raise ValueError("Invalid tail Fourier indices")
    if any((m - 1) % 3 for m in pm) or any(m < 0 or m % 3 for m in hm):
        raise ValueError("Tail does not retain the actual m3 Fourier definition")
    coefficients = cut["coefficients"]
    if len(coefficients) != 3 or any(len(row) != len(pm) + len(hm) for row in coefficients):
        raise ValueError("Tail cut lacks complete nodal R two-jets")
    tp = {m: [fq(row[k]) for row in coefficients] for k, m in enumerate(pm)}
    for j, value_ in enumerate((Rc, F(1), F(0))):
        tp.setdefault(1, [F(0)] * 3)[j] += value_
    th = {m: [-fq(row[len(pm) + k]) for row in coefficients] for k, m in enumerate(hm)}
    if fq(coefficients[0][len(pm) + hm.index(0)]) != fq(chain["mean_chain"][0][0]):
        raise ValueError("The saved perturbation mean was replaced")
    mu_cut = fq(coefficients[0][len(pm) + hm.index(0)])
    th[0] = [F(0), th[0][1] - w, th[0][2] - wR]
    with np.load(a.bridge_trace) as z:
        bp = interval_rows(z["planar_modes"], z["planar_R_jets"])
        bh = interval_rows(z["height_modes"], z["height_R_jets_relative_Zc"])
    if bh.get(0, [None])[0] != (F(0), F(0)):
        raise ValueError("Require the exact same formal Z_cut height convention")
    dp, dh = difference(bp, tp), difference(bh, th)
    if dh[0][0] != (F(0), F(0)):
        raise AssertionError("Mean position must cancel symbolically before interval arithmetic")
    for j, h in enumerate(H):
        q = h
        for k in range(3):
            assert value(q, F(0)) == int(j == k) and value(q, F(1)) == 0
            q = derivative(q)
    baseline = read(a.conditional_baseline) if a.conditional_baseline else None
    lengths = sorted(set(F(v) for v in a.lengths.split(",")) | {(Rc - radii[0]) / 2})
    report = {
        "status": "actual_cut_tail_side_C2_correction_budget_enclosed",
        "scope": "Explicit correction of this finite shared-R tail; no full-H identity, unchanged metric, or global completion is inferred.",
        "source_sha256": sha(__file__),
        "input_sha256": {name: sha(getattr(a, name)) for name in
                         ("bridge_trace", "bridge_certificate", "tail_stage", "tail_manifest", "source_port")},
        "accepted_packet_sha256": sha(raw_path),
        "bridge_source_run_sha256": bridge_report["source_run_sha256"],
        "tail_map_hash": stage["sharing"]["mapHash"],
        "patch_domain_allowed_exact": [str(radii[0]), str(Rc)],
        "mu_cut_exact": str(mu_cut),
        "height_constant_contract": "z_b=the same exact Z_cut+the original saved mu_cut",
        "correction_definition": "P=sum_{j=0}^2 (-L)^j H_j((R_c-R)/L) Delta_j(theta), Delta=actual bridge minus actual upper tail two-jet.",
        "coefficient_meaning": "The same computable-real bridge trace expressions minus original literal tail coefficients. Interval midpoints are used only to bound polynomials; never to define the correction.",
        "shared_C2_endpoint_identities_exact": 18,
        "background_contract": "The same R58 true background: |w|<=.41 and principal curvature<=8, with fixed original configuration verified through the accepted packet.",
        "mean_definition": "The original saved mean remains the fixed baseline; an explicit zero-mode correction is added when required. Total mean then changes on the patch.",
        "total_mean_correction_needed": any(lo != 0 or hi != 0 for lo, hi in dh[0][1:]),
        "baseline_replaced": False, "target_metric_modified": False,
        "full_H_certified_here": False, "global_metric_certified_here": False,
        "fixed_g_refinement_certified_here": False,
        "patches": [],
    }
    for length in lengths:
        if length <= 0 or Rc - length < radii[0]:
            report["patches"].append({"length_exact": str(length), "status": "outside_supplied_stage_0"})
            continue
        bounds, components = patch_bounds(dp, dh, length, a.blocks)
        rmin = Rc - length
        eta = sqrt_upper(bounds[1, 0] ** 2 + (bounds[0, 1] / rmin) ** 2)
        H00 = bounds[2, 0] + F(82, 25) * bounds[1, 0]
        H01 = bounds[1, 1] / rmin + bounds[0, 1] / rmin ** 2
        H11 = bounds[0, 2] / rmin ** 2 + bounds[1, 0] / rmin
        beta = sqrt_upper(H00 * H00 + 2 * H01 * H01 + H11 * H11)
        row = {
            "length_exact": str(length), "status": "correction_enclosed",
            "R_exact": [str(rmin), str(Rc)],
            "Cartesian_derivative_upper": {f"{r},{t}": outward(v, 1) for (r, t), v in bounds.items()},
            "normalized_first_jet_upper": outward(eta, 1),
            "normalized_covariant_Hessian_upper": outward(beta, 1),
            "conditional_baseline_budget": None,
        }
        if baseline is not None:
            eps0, eta0, beta0 = (declared(baseline[k]) for k in ("metric", "eta", "beta"))
            if not 0 <= eps0 < 1 or not 0 <= eta0 < 1 or beta0 < 0:
                raise ValueError("Invalid conditional baseline bounds")
            metric = eps0 + 2 * sqrt_upper(1 + eps0) * eta + eta * eta
            curvature = (8 + beta0 + beta) / (1 - eta0 - eta) ** 2 if eta0 + eta < 1 else None
            conditional = {
                "scope": "Only conditional on these baseline numbers being certified for this same stage/map; this script does not certify them.",
                "baseline_sha256": sha(a.conditional_baseline),
                "metric_upper": outward(metric, 1),
                "metric_below_1e_6_conditionally": metric < F(1, 10**6),
                "principal_curvature_upper": outward(curvature, 1) if curvature is not None else None,
            }
            if "radius" in baseline and "support" in baseline:
                radius0, support0 = declared(baseline["radius"]), declared(baseline["support"])
                if radius0 < 0:
                    raise ValueError("Negative conditional radius")
                cross_gap = 2 * sqrt_upper(1 + eps0) * eta + eta * eta
                normal_gap = 2 * cross_gap / (1 - eps0)
                regular = cross_gap < 1 - eps0
                conditional.update({
                    "radius_upper": outward(radius0 + bounds[0, 0], 1),
                    "support_lower": (
                        outward(support0 - bounds[0, 0] - radius0 * normal_gap, -1)
                        if regular else None
                    ),
                    "normal_difference_upper": outward(normal_gap, 1) if regular else None,
                    "normal_orientation_preserved_by_cross_bound": regular,
                })
            row["conditional_baseline_budget"] = conditional
        report["patches"].append(row)
    report["seconds"] = time.monotonic() - started
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "status": report["status"], "patches": report["patches"],
        "global_metric_certified_here": False, "full_H_certified_here": False,
        "seconds": report["seconds"],
    }))


if __name__ == "__main__":
    main()
