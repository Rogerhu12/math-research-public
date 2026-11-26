#!/usr/bin/env python3
"""Compare two accepted warm-phase fields at one identical complete fixed problem.

This reports finite sampled C2 differences, not a continuous certificate or
a proven Cauchy sequence.  The vertical mean rule is identical in both maps.
Position uses the same declared finite mean's true primitive, numerically
evaluated with positive per-cell Gauss rules; the difference of two rules is
a diagnostic, not an integration error bound.  Derivatives use the analytic
integrand jets, not derivatives of the quadrature algorithm.

Physical phase-control l1_0/l1_2/l1_4 differences are evaluated as exact
rationals of the literal binary d vectors, after zero extension. They are
not support-coefficient distances and do not bound any uncomputed tail.
"""
import os
for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[name] = "1"

import argparse
import copy
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent
JETS = ("F", "Fs", "Fp", "Fss", "Fsp", "Fpp")


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require_same_problem(left, right):
    keys = ("frozen_profile", "physical_tail_parameters", "physical_tail_cut",
            "angular_chart", "warm_definition", "warm_provider_sha256", "model_kind",
            "gauge_q", "warp_reference", "mean_nodes", "bc_normalization",
            "terminal_kind", "parameter_zero_meaning", "frozen_source_signature",
            "origin_design_sha256")
    for key in keys:
        if left.get(key) != right.get(key):
            raise ValueError("Different complete warm problems: "+key)
    if left.get("model_kind") != "warm-supported-material-phase-fixed-metric":
        raise ValueError("Use the declared warm supported-phase family")
    if any(not r.get("fixed_metric") or r.get("fixed_core") is not False for r in (left, right)):
        raise ValueError("Use fixed-metric, unknown-phase-core records")
    if any(not r.get("finite_linear_candidate_pass") or not r.get("physical_sha256")
           or not r.get("raw_return", {}).get("success") or r.get("error") for r in (left, right)):
        raise ValueError("Both actual fields must have passed their finite gates")
    if left["terminal_kind"] != "original_linear_dn":
        raise ValueError("This comparison has no attached actual nonlinear DN")
    if left["parameter_zero_meaning"] != "log(q_aux/gauge_q)":
        raise ValueError("Auxiliary coordinate semantics are missing")
    # warm_definition includes the same lambda, frozen full baseline support,
    # phase scale, circle/window parameters and actual source identity.
    return {key: left[key] for key in keys}


def complete_jets(obj, flow, physical, s, N, mean_N, heights):
    Y, Ys, Yss = (physical.sol(s, order) for order in (0, 1, 2))
    B, B1, B2 = flow.basis(N)
    _, Dmean, DDmean = flow.basis(mean_N)
    frame, _, dW = flow.velocity_s(s, Y, Ys, Dmean, DDmean)
    mean = np.mean(frame["V"][:, :, 2], axis=1)
    mean_s = np.mean(dW[:, :, 2], axis=1)
    g = flow.geo(s, N)
    result = {
        "F": g["pos"]+obj.q*flow.values(Y, B),
        "Fs": g["s1"]+obj.q*flow.values(Ys, B),
        "Fp": g["p1"]+obj.q*flow.values(Y, B1),
        "Fss": g["s2"]+obj.q*flow.values(Yss, B),
        "Fsp": g["sp"]+obj.q*flow.values(Ys, B1),
        "Fpp": g["p2"]+obj.q*flow.values(Y, B2),
    }
    for key, values in (("F", heights), ("Fs", mean), ("Fss", mean_s)):
        result[key] = np.asarray(result[key], float).copy()
        result[key][:, :, 2] += values[:, None]
    return result


def exact_core_differences(c0, c1):
    M = max(len(c0), len(c1))
    x, y = np.zeros(M), np.zeros(M)
    x[:len(c0)], y[:len(c1)] = c0, c1
    result = {}
    for exponent in (0, 2, 4):
        total = Fraction(0)
        for j, (a, b) in enumerate(zip(x, y), start=1):
            weight = 1 if exponent == 0 else 1+(3*j)**exponent
            total += weight*abs(Fraction.from_float(float(b))-Fraction.from_float(float(a)))
        result["l1_"+str(exponent)] = dict(
            numerator=str(total.numerator), denominator=str(total.denominator),
            decimal=float(total),
            float_upper=float(np.nextafter(float(total), np.inf)) if total else 0.)
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--first-run", type=Path, required=True)
    p.add_argument("--second-run", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--angular", type=int, nargs="+", default=[512, 1024])
    p.add_argument("--mean-nodes", type=int, default=1168)
    p.add_argument("--radial-count", type=int, default=151)
    p.add_argument("--height-orders", type=int, nargs=2, default=[6, 12])
    p.add_argument("--batch", type=int, default=8)
    a = p.parse_args()
    begin = time.monotonic()
    records = [json.loads(path.read_text()) for path in (a.first_run, a.second_run)]
    contract = require_same_problem(*records)
    if contract["mean_nodes"] != a.mean_nodes:
        raise ValueError("Use the maps' original common mean rule")
    loader = module("_c2_common_fixed_branch_loader", HERE/"warm_fixed_m3_model.py")
    audit = module("_c2_common_physical_loader", SCRIPTS/"resume_m3/audit_full_relative_metric.py")
    obj0 = loader.load_model(dict(source_run=str(a.first_run.resolve())))
    # Reuse a single class construction.  The original geometry loader is
    # intended for a fresh process; importing/installing it twice would stack
    # global numerical patches and is unnecessary for the same fixed problem.
    port1 = copy.deepcopy(obj0.port)
    if records[1].get("linear_port_path"):
        file = Path(records[1]["linear_port_path"])
        port1 = json.loads(file.read_text())
        port1["cut"]["_prefix_bridge"] = contract["frozen_profile"]["prefix_bridge"]
        port1["_sha256"] = sha(file)
        if port1["_sha256"] != records[1]["linear_port_sha256"]:
            raise ValueError("The second numerical port bytes changed")
    if port1["parameters"] != contract["physical_tail_parameters"] or port1["cut"] != contract["physical_tail_cut"]:
        raise ValueError("The second numerical port changes the declared physical metric")
    obj1 = type(obj0)(contract["frozen_profile"], port1, contract["gauge_q"],
                      records[1]["modes"], records[1]["angular"], True,
                      contract["warp_reference"])
    obj1.bcweights = np.full(obj1.M, contract["bc_normalization"])
    objects = [obj0, obj1]
    physicals = [audit.load_physical(path.parent/"physical.npz")
                 for path in (a.first_run, a.second_run)]
    for obj, physical, record, run in zip(objects, physicals, records, (a.first_run, a.second_run)):
        if physical.source_sha256 != record["physical_sha256"]:
            raise ValueError("Physical field differs from its actual run record")
        raw_path = run.parent/record["raw_return"]["file"]
        if sha(raw_path) != record["raw_return"]["sha256"]:
            raise ValueError("The actual raw return changed")
        with np.load(raw_path, allow_pickle=False) as raw:
            if not np.array_equal(raw["p"], physical.p):
                raise ValueError("Physical and raw parameter vectors differ")
        obj.initial(physical.p)
    flows = [obj.flow(physical.p[0]) for obj, physical in zip(objects, physicals)]
    if physicals[0].x[0] != physicals[1].x[0] or physicals[0].x[-1] != physicals[1].x[-1]:
        raise ValueError("The two physical meridian domains differ")
    lo, hi = physicals[0].x[[0, -1]]
    radial = [np.linspace(lo, hi, a.radial_count)]
    for physical in physicals:
        radial += [physical.x, (physical.x[:-1]+physical.x[1:])/2.]
        radial += [np.nextafter(physical.x[1:-1], lo)]
    s = np.unique(np.concatenate(radial))
    positions = []
    primitive_differences = []
    for flow, physical in zip(flows, physicals):
        q0 = flow.height_integral(physical, s, a.mean_nodes, a.height_orders[0])
        q1 = flow.height_integral(physical, s, a.mean_nodes, a.height_orders[1])
        primitive_differences.append(float(np.max(np.abs(q1-q0))))
        positions.append(q1)
    results = []
    for N in sorted(set(a.angular)):
        maxima = {key: 0. for key in JETS}
        peaks = {key: None for key in JETS}
        core = {key: 0. for key in ("position", "first", "second")}
        theta = 2*np.pi*np.arange(N)/N
        gc = [obj._core.evaluate(theta) for obj in objects]
        for name, field in (("position", "F"), ("first", "Ft"), ("second", "Ftt")):
            core[name] = float(np.max(np.linalg.norm(gc[1][field]-gc[0][field], axis=-1)))
        for start in range(0, len(s), a.batch):
            sl = slice(start, start+a.batch)
            jets = [complete_jets(obj, flow, physical, s[sl], N, a.mean_nodes, height[sl])
                    for obj, flow, physical, height in zip(objects, flows, physicals, positions)]
            for key in JETS:
                distance = np.linalg.norm(jets[1][key]-jets[0][key], axis=-1)
                if not np.all(np.isfinite(distance)):
                    raise FloatingPointError("A complete-map comparison was nonfinite")
                ir, ia = np.unravel_index(np.argmax(distance), distance.shape)
                if distance[ir, ia] > maxima[key]:
                    maxima[key] = float(distance[ir, ia])
                    peaks[key] = dict(s=float(s[start+ir]), psi=float(2*np.pi*ia/N))
        results.append(dict(angular=N, sampled_complete_C2_jet_difference=maxima,
                            peaks=peaks, sampled_core_C2_difference=core))
        print(json.dumps(dict(angular=N, jet_difference=maxima), allow_nan=False), flush=True)
    coefficients = [obj._core.controls.copy() for obj in objects]
    result = dict(scope=__doc__, command=[sys.executable, *sys.argv], status="evaluated",
        source_sha256=sha(__file__), source_runs=[str(a.first_run.resolve()), str(a.second_run.resolve())],
        source_run_sha256=[sha(a.first_run), sha(a.second_run)],
        physical_sha256=[p.source_sha256 for p in physicals], fixed_problem=contract,
        finite_candidate_pass=[bool(r.get("finite_linear_candidate_pass")) for r in records],
        modes=[o.M for o in objects], q_aux=[float(o.support_amplitude) for o in objects],
        phase_control_literal_distances=exact_core_differences(*coefficients),
        phase_control_scope="d vectors in one fixed supported basis; q_aux is only a coordinate carrier",
        homotopy=contract["warm_definition"]["homotopy"],
        radial_samples=len(s), radial_range=[float(lo), float(hi)],
        coordinate="common fixed computational (s,psi) chart; identical material Theta",
        mean_nodes=a.mean_nodes, mean_primitive_origin=0.,
        mean_primitive_scope="true primitive of the same fixed finite mean rule; numerical positive-cell Gauss evaluation",
        height_orders=a.height_orders, observed_height_quadrature_change=primitive_differences,
        height_quadrature_error_certified=False, rows=results,
        continuous_C2_bound_certified=False, same_limit_core_proven=False,
        full_closed_surface=False, elapsed=time.monotonic()-begin)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")


if __name__ == "__main__":
    main()
