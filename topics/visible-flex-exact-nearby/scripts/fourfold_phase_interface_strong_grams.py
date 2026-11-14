#!/usr/bin/env python3
"""Complete strong high-output Gram bounds at the same whole-eta quarter cut.

Consumes an actually completed family multiplier package. No geometry or
Fourier coefficient is reconstructed from a point-only or summary report.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import numpy as np
from flint import arb, acb, acb_mat, ctx

from fourfold_phase_beta_interval import ball_record
from fourfold_phase_cap_energy_collect import hermitian_norm_bound
from fourfold_phase_low_feedback_paid_inputs import (
    adjoint, hermitian_enclosure, matrix, midpoint, norm)
from fourfold_phase_core_even_collect import cosine_basis


ORDERS = {
    "height_Y": (("H1", 1), ("Hthreehalf", Fraction(3, 2))),
    "inverse_height": (("H1", 1), ("Hthreehalf", Fraction(3, 2))),
    "conormal_pY": (("H0", 0), ("Hhalf", Fraction(1, 2))),
    "energy_shear_YpY": (("H0", 0), ("Hhalf", Fraction(1, 2))),
    "conormal_ratio_pY_over_Y": (("H0", 0), ("Hhalf", Fraction(1, 2))),
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    def reject(value):
        raise ValueError("nonfinite JSON constant "+value)
    return json.loads(Path(path).read_text(), parse_constant=reject)


def input_weight(N, order):
    x = arb(max(1, 4*N))
    if order == 0:
        return arb(1)
    if order == Fraction(1, 2):
        return x.sqrt()
    if order == 1:
        return x
    if order == Fraction(3, 2):
        return x*x.sqrt()
    raise ValueError("unsupported physical Sobolev order")


def complete_finite_high_gram(positive, N, cutoff, twice_order):
    K, n = len(positive)-1, 2*N+1
    coefficients = [arb(float(x)) for x in positive]
    result = acb_mat(n, n)
    for k in range(-K-N, K+N+1):
        if abs(k) <= cutoff:
            continue
        weight = arb(4*abs(k))**twice_order
        row = [coefficients[abs(k-j)] if abs(k-j) <= K else arb(0)
               for j in range(-N, N+1)]
        for i in range(n):
            for j in range(i, n):
                result[i, j] += weight*row[i]*row[j]
    for i in range(n):
        for j in range(i+1, n):
            result[j, i] = result[i, j].conjugate()
    return result


def selected_gram_record(G, operator_error):
    G = hermitian_enclosure(G)
    upper, _ = hermitian_norm_bound(G)
    if not upper.is_finite() or upper < 0:
        raise ValueError("invalid finite positive Gram norm")
    finite_norm = upper.sqrt().upper()
    chosen = midpoint(G)
    chosen = (chosen+chosen.conjugate().T)/2
    selection = norm(G-matrix(chosen))
    radius = (selection+2*finite_norm*operator_error+operator_error**2).upper()
    record = dict(
        finite_operator_norm_upper=ball_record(finite_norm),
        complete_actual_minus_finite_operator_error=ball_record(operator_error),
        selected_finite_Gram_error=ball_record(selection),
        actual_Gram_operator_radius=ball_record(radius),
        true_high_output_operator_norm_upper=ball_record(
            (finite_norm+operator_error).upper()),
        complete_Gram_contract="For every parameter in the input eta interval, ||T_true^*T_true-G_selected|| <= radius; equivalently both Hermitian Loewner inequalities hold.")
    return record, chosen


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--interface", type=Path, required=True)
    ap.add_argument("--object", type=Path,
        default=Path("data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    ap.add_argument("--modes", type=int, default=4)
    ap.add_argument("--output-cutoffs", default="4,16,64,256")
    ap.add_argument("--bits", type=int, default=256)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    ctx.prec = args.bits
    N = args.modes
    if N < 1:
        raise ValueError("positive input cutoff required")
    cutoffs = sorted(set(int(x) for x in args.output_cutoffs.split(",")))
    if not cutoffs or min(cutoffs) < N:
        raise ValueError("high-output cutoffs must be at least the input cutoff")
    doc = read(args.interface)
    if not doc.get("complete") or doc.get("kind") != (
        "uniform_eta_complete_physical_quarter_cut_interface_multipliers"):
        raise ValueError("an actually completed whole-family interface is required")
    if not doc.get("uniform_in_the_entire_real_parameter_interval"):
        raise ValueError("a point-only multiplier package is not accepted")
    if sha(args.object) != doc["object_sha256"]:
        raise ValueError("the exact graph object differs from the requested input")
    if doc["exact_physical_radius"] != "1/4":
        raise ValueError("wrong physical cut")
    center = Fraction(doc["exact_center_parameter"])
    expected_center = Fraction(-7789843107295549, 4611686018427387904)
    if center != expected_center:
        raise ValueError("the actual affine center differs from delta5")
    lo, hi = map(Fraction, doc["exact_parameter_interval"])
    eta = Fraction(1, 10**9)
    if lo > center-eta or hi < center+eta:
        raise ValueError("the declared family misses the required eta interval")
    producer = Path(__file__).with_name("fourfold_phase_family_interface_fourier.py")
    if sha(producer) != doc["source_sha256"]:
        raise ValueError("the actual family producer source identity differs")
    apath = Path(doc["arrays"]["path"])
    if sha(apath) != doc["arrays"]["sha256"]:
        raise ValueError("the complete family coefficient package changed")
    with np.load(apath, allow_pickle=False) as data:
        positive = np.array(data["positive_fourier_coefficients"], copy=True)
    names = doc["exact_function_names"]
    if positive.shape != (len(names), doc["retained_positive_indices"]+1):
        raise ValueError("coefficient dimensions differ")
    if np.any(~np.isfinite(positive)) or np.any(positive.imag != 0):
        raise ValueError("the finite multiplier must be exactly real and finite")
    positive = positive.real
    Qc = cosine_basis(N)
    arrays, rows = {}, []
    for name, choices in ORDERS.items():
        index = names.index(name)
        for label, order in choices:
            error = arb(doc["functions"][name]["complete_multiplier_errors"][label]["ball"]).upper()
            operator_error = (input_weight(N, order)*error).upper()
            for cutoff in cutoffs:
                G = complete_finite_high_gram(positive[index], N, cutoff, int(2*order))
                full, selected_full = selected_gram_record(G, operator_error)
                cosine, selected_cosine = selected_gram_record(
                    adjoint(Qc)*G*Qc, operator_error)
                key = name+"_"+label+"_above_"+str(cutoff)
                arrays[key+"_full"] = selected_full
                arrays[key+"_cosine"] = selected_cosine
                rows.append(dict(
                    function=name, output_space=label, physical_output_cutoff=cutoff,
                    retained_finite_output_indices=[-len(positive[index])+1-N,
                                                     len(positive[index])-1+N],
                    full_input_dimension=2*N+1, cosine_input_dimension=N+1,
                    full=full, cosine=cosine,
                    selected_Gram_array_keys=[key+"_full", key+"_cosine"]))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    out_arrays = args.out.with_suffix(".npz")
    np.savez_compressed(out_arrays, **arrays)
    report = dict(
        kind="whole_eta_complete_strong_quarter_cut_high_output_Grams",
        complete=True, source_sha256=sha(__file__), bits=args.bits,
        input_report=dict(path=str(args.interface), sha256=sha(args.interface)),
        input_arrays=doc["arrays"], object_sha256=doc["object_sha256"],
        exact_center_parameter=doc["exact_center_parameter"],
        exact_parameter_interval=doc["exact_parameter_interval"],
        uniform_in_the_entire_real_parameter_interval=True,
        exact_physical_radius="1/4", input_physical_modes=N,
        input_norm="Euclidean full physical Fourier coefficients, or the exactly isometric cosine subspace; the angular mean is retained.",
        output_norm="H^s has weight (4|k|)^s on each retained nonzero high output. Every finite output through |k|=K+N and the complete actual-minus-finite infinite remainder are included.",
        rows=rows,
        paired_regular_port_scope="These are height/coefficient multiplication outputs. The complete cap regular trace and regular flux are separate genuine ports and are not set to zero.",
        strong_cap_flux_error_certified=False,
        complete_core_radial_propagation_certified=False,
        rigorous_full_Schur_inverse=False,
        arrays=dict(path=str(out_arrays), sha256=sha(out_arrays), bytes=out_arrays.stat().st_size),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            "fourfold_phase_family_interface_fourier.py",
            "fourfold_phase_core_even_collect.py",
            "fourfold_phase_low_feedback_paid_inputs.py",
            "fourfold_phase_cap_energy_collect.py", "fourfold_phase_beta_interval.py")},
        scope=[
            "Actual full-frequency parameter-uniform multiplier outputs only.",
            "The existing negative-order complete cap flux bound is not upgraded by this calculation.",
            "No missing high solver or regular port is removed by a finite Gram projection."])
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps(dict(complete=True, whole_eta=True, rows=len(rows),
        modes=N, arrays=report["arrays"]), indent=2), flush=True)


if __name__ == "__main__":
    main()
