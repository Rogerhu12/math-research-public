#!/usr/bin/env python3
"""Certify R126 continuation with a separate affine barrier on every true box.

This consumes the entire unprojected, closed-cell residual report.  A failed
single global barrier is permitted; an incomplete residual cover is not.
No coefficient or residual is inferred from samples or interpolated reports.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

from flint import arb, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_two_jet_newton_source import record, save


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_json(path):
    raw = Path(path).read_bytes()
    if str(path).endswith(".gz"):
        raw = gzip.decompress(raw)
    return json.loads(raw)


def up(item):
    # Saved decimal records enclose the original binary directed endpoint.
    # Taking the outer endpoint again covers decimal serialization as well.
    return arb(item["upper"]).upper()


def down(item):
    return arb(item["lower"]).lower()


def propagate(data, tube):
    inflation = arb(1)+arb(2)**-40
    tiny = arb(2)**-180
    start0 = (2*up(data["initial_error"]["epsilon0"])+tiny).upper()
    start1 = (2*up(data["initial_error"]["epsilon1"])+tiny).upper()
    initial = [record(start0), record(start1)]
    endpoint = Fraction(0)
    rows = []
    min_gap = None
    min_k = None
    max_actual_C1 = arb(0)
    for number, native in enumerate(data["rows"]):
        left, right = map(Fraction, native["interval"])
        gl, gr = map(Fraction, native["actual_scalar_germ"])
        if left != endpoint or not gl <= left < right <= gr:
            raise ValueError("noncontiguous cover or box outside its actual germ")
        bounds = native["bounds"]
        u = {key: up(bounds[key]) for key in
             ("Mhat", "D1", "D2", "rho0", "rho1", "gamma", "beta", "kappa")}
        if not all(value >= 0 for value in u.values()):
            raise ValueError("negative comparison coefficient")
        gap = down(bounds["candidate_gap"])
        k = down(bounds["k_lower"])
        h = exact_arb(right-left)
        M = (u["Mhat"]+tube).upper()
        J = (u["beta"]*(1+3*M*M)+2*u["kappa"]).upper()
        A0 = (u["gamma"]*u["D1"]+J).upper()
        A1 = (2*u["gamma"]*u["D1"]+J).upper()
        A10 = (u["gamma"]*u["D2"]+6*u["beta"]*M*u["D1"]).upper()
        denominator = (1-h*A0).lower()
        if not denominator > 0:
            raise ValueError(f"box {number}: C0 affine denominator failed")
        end0 = ((start0+h*u["rho0"])/denominator*inflation+tiny).upper()
        aa = (h*u["gamma"]).upper()
        bb = (1-h*A1).lower()
        cc = (start1+h*(A10*end0+u["rho1"])).upper()
        disc = (bb*bb-4*aa*cc).lower()
        if not bb > 0 or not disc > 0:
            raise ValueError(f"box {number}: C1 affine quadratic failed")
        # Stable evaluation of the smaller quadratic root; the outward
        # inflation puts Y strictly inside the two-root admissible interval.
        end1 = (2*cc/(bb+disc.sqrt())*inflation+tiny).upper()
        margin0 = (end0-start0-h*(A0*end0+u["rho0"])).lower()
        margin1 = (end1-start1-h*(A1*end1+u["gamma"]*end1*end1
                                    +A10*end0+u["rho1"])).lower()
        actual_gap = (gap-2*end0).lower()
        gates = dict(
            positive_target_k=bool(k > 0),
            C0_in_tube=bool(end0 < tube),
            strict_actual_Riemann_gap=bool(actual_gap > 0),
            C0_barrier_increases=bool(end0 > start0),
            C1_barrier_increases=bool(end1 > start1),
            strict_C0_affine_differential_margin=bool(margin0 > 0),
            strict_C1_affine_differential_margin=bool(margin1 > 0),
        )
        row = dict(
            native_row=number, piece=native["piece"], part=native["part"],
            interval=[str(left), str(right)],
            initial=[record(start0), record(start1)],
            final=[record(end0), record(end1)],
            coefficients={name: record(value) for name, value in
                          dict(M=M, J=J, A0=A0, A1=A1, A10=A10).items()},
            quadratic={name: record(value) for name, value in
                       dict(a=aa, b=bb, c=cc, discriminant=disc).items()},
            strict_margins=[record(margin0), record(margin1)],
            actual_gap_lower=record(actual_gap), gates=gates,
        )
        rows.append(row)
        if not all(gates.values()):
            return dict(passed=False, failed_row=number, rows=rows,
                        covered_interval=["0", str(endpoint)], initial=initial)
        endpoint = right
        min_gap = actual_gap if min_gap is None else min(min_gap, actual_gap).lower()
        min_k = k if min_k is None else min(min_k, k).lower()
        max_actual_C1 = max(max_actual_C1, u["D1"]+end1).upper()
        start0, start1 = end0, end1
    if not rows:
        raise ValueError("empty true radial cover")
    return dict(passed=True, rows=rows, covered_interval=["0", str(endpoint)],
                initial=initial, final=[record(start0), record(start1)],
                actual_Riemann_gap_lower=record(min_gap), target_k_lower=record(min_k),
                actual_first_angular_derivative_upper=record(max_actual_C1))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--native", type=Path, required=True)
    parser.add_argument("--producer", type=Path, default=Path(
        "scripts/fourfold_phase_codazzi_continuation_validate.py"))
    parser.add_argument("--provider", type=Path, default=Path(
        "scripts/fourfold_phase_codazzi_coefficients.py"))
    parser.add_argument("--candidate", type=Path, default=Path(
        "notes/2026-11-13-codazzi-dense-r0005-n1024-candidate.npz.gz"))
    parser.add_argument("--object", type=Path, default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    parser.add_argument("--tube", type=Fraction, default=Fraction(1, 16))
    parser.add_argument("--bits", type=int, default=256)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    if args.out.exists():
        raise FileExistsError("refusing to overwrite an existing certificate")
    native = read_json(args.native)
    if (native.get("kind") != "actual_R126_continuous_Codazzi_Cauchy_validation"
            or not native.get("complete") or native.get("failure") is not None
            or not native.get("whole_affine_parameter_interval")
            or not native.get("whole_real_angular_circle")):
        raise ValueError("input is not a complete true continuous residual report")
    if native["covered_interval"] != native["exact_requested_interval"]:
        raise ValueError("native radial coverage identity failed")
    for path, key in ((args.producer, "source_sha256"),
                      (args.provider, "coefficient_provider_sha256"),
                      (args.candidate, "candidate_sha256"),
                      (args.object, "object_sha256")):
        if sha(path) != native[key]:
            raise ValueError(f"native dependency hash mismatch: {path}")
    if not args.tube > 0:
        raise ValueError("nonpositive tube")
    barrier = propagate(native, exact_arb(args.tube))
    result = dict(
        kind="R126_true_continuous_piecewise_affine_C0_C1_barrier",
        source_sha256=sha(__file__), bits=args.bits,
        native_path=str(args.native), native_sha256=sha(args.native),
        native_producer_sha256=native["source_sha256"],
        native_provider_sha256=native["coefficient_provider_sha256"],
        candidate_sha256=native["candidate_sha256"], object_sha256=native["object_sha256"],
        exact_center_parameter=native["exact_center_parameter"],
        parameter_half_width=native["parameter_half_width"],
        whole_affine_parameter_interval=True, whole_real_angular_circle=True,
        complete=True, tube=str(args.tube),
        native_single_global_barrier_passed=native["continuation_certified"],
        exact_requested_interval=native["exact_requested_interval"],
        piecewise_barrier=barrier, continuation_certified=barrier["passed"],
        closed_surface_complete=False,
    )
    if barrier["passed"] and barrier["covered_interval"] != native["exact_requested_interval"]:
        raise ValueError("barrier did not cover the complete native interval")
    save(args.out, result)
    print(json.dumps({key: result[key] for key in
                      ("continuation_certified", "native_single_global_barrier_passed",
                       "exact_requested_interval", "source_sha256")}, indent=2))
    if barrier["passed"]:
        print("final", [x["upper"] for x in barrier["final"]])
        print("gap", barrier["actual_Riemann_gap_lower"]["lower"])


if __name__ == "__main__":
    main()
