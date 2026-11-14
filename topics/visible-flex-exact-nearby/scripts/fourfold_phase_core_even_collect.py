#!/usr/bin/env python3
"""Compose the whole-eta angular-even core and its waist-even finite DN.

Only existing completed local arrays are used. Their exact algebraic cosine
compressions cost no new selected-coefficient error. This entry does not
assume the infinite core Dirichlet problem or full high feedback invertible.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
import time
import traceback

import numpy as np
from flint import arb, acb, acb_mat, ctx

from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_core_cell_flow import exact_matrix, real_midpoint, ball_record
from fourfold_phase_core_flow_collect import (
    sha, read, write, norm, sub, product_bound, validate)
from fourfold_phase_low_feedback_paid_inputs import adjoint


def cosine_basis(N):
    n = 2*N+1
    Q = acb_mat(n, N+1)
    Q[N, 0] = 1
    s = 1/arb(2).sqrt()
    for k in range(1, N+1):
        Q[N+k, k] = s
        Q[N-k, k] = s
    return Q


def two_cauchy_slots(Q):
    n, m = Q.nrows(), Q.ncols()
    result = acb_mat(2*n, 2*m)
    for i in range(n):
        for j in range(m):
            result[i, j] = Q[i, j]
            result[n+i, m+j] = Q[i, j]
    return result


def paired_cut_heights(Q):
    n, m = Q.nrows(), Q.ncols()
    result = acb_mat(2*n, m)
    s = 1/arb(2).sqrt()
    for i in range(n):
        for j in range(m):
            result[i, j] = s*Q[i, j]
            result[n+i, j] = s*Q[i, j]
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--cover-root", type=Path, required=True)
    ap.add_argument("--bits", type=int, default=256)
    ap.add_argument("--old-core", type=Path,
        default=Path("notes/2026-11-12-actual-core-low-block-M4.json"))
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    ctx.prec = args.bits
    wall, cpu = time.monotonic(), time.process_time()
    report = dict(
        kind="complete_uniform_angular_even_waist_even_finite_core_DN",
        complete=False, source_sha256=sha(__file__), bits=args.bits,
        rigorous_infinite_core_DN_inverse=False, rigorous_full_Schur_inverse=False)
    trace = []
    try:
        manifests = sorted(args.cover_root.glob("block_*/manifest.json"))
        if not manifests:
            raise ValueError("no complete original local cover")
        ident, original, inputs, leaves = validate(manifests)
        N = int(ident["modes"])
        n, m = 2*N+1, N+1
        Q = cosine_basis(N)
        U = two_cauchy_slots(Q)
        positive = []
        for center, error, metadata in original:
            # This is the exact algebraic Q* T Q expression enclosed by Acb.
            # The true local T preserves this subspace; its error is <= error.
            compressed = adjoint(U)*center*U
            positive.append((compressed, error, metadata))
        report.update(
            identity=ident, input_manifests=inputs,
            accepted_real_leaves=len(positive),
            original_common_spans=sum(len(read(p)["original_spans"]) for p in manifests),
            exact_physical_cuts=["-1/4", "1/4"],
            angular_cos_modes=list(range(m)), angular_Cauchy_dimension=2*m,
            physical_momentum_scale=ident["momentum_scale"],
            complete_original_leaf_identities=leaves,
            exact_local_compression="diag(Qcos,Qcos)^* T_j diag(Qcos,Qcos), with Qcos columns e0 and (ek+e-k)/sqrt(2); no newly chosen floating local centers.",
            local_compression_error_rule="The actual angular invariant transfer is compressed by isometries, so its complete local error is no greater than the already paid original error.")
        P, error, half, trace = product_bound(positive, 2*m, "positive angular-even half")
        report["positive_half"] = half
        A = sub(P, 0, m, 0, m)
        C = sub(P, m, 2*m, 0, m)
        Ai = A.inv()
        qa, cn = norm(Ai), norm(C)
        if not qa*error < 1:
            raise ValueError("waist-even five-height inverse perturbation is not below one")
        qtrue = (qa/(1-qa*error)).upper()
        dq = (qa*qa*error/(1-qa*error)).upper()
        scale = exact_arb(Fraction(ident["momentum_scale"]))
        DN = scale*C*Ai
        dn_error = (scale*(error*qtrue+cn*dq)).upper()
        symmetric = (DN+adjoint(DN))/2
        chosen = real_midpoint(symmetric)
        chosen = (chosen+chosen.T)/2
        selection = norm(symmetric-exact_matrix(chosen))
        total = (dn_error+selection).upper()
        report.update(
            finite_waist_even_DN_certified=True,
            true_positive_cos_transfer_error=ball_record(error),
            reference_height_A_inverse_norm=ball_record(qa),
            height_A_inverse_perturbation_product=ball_record(qa*error),
            true_height_A_inverse_bound=ball_record(qtrue),
            actual_finite_even_core_DN_error=ball_record(total),
            DN_before_selected_center_error=ball_record(dn_error),
            exact_Hermitian_projection_selection_error=ball_record(selection),
            reference_DN_antisymmetric_norm=ball_record(norm(DN-adjoint(DN))/2),
            exact_DN_formula="scale*C*A^-1, A=Pww, C=Ppw; the waist-even initial flux is exactly zero.",
            normalized_boundary_coordinates="(w_left,w_right)=(Qcos*v,Qcos*v)/sqrt(2); the two outward fluxes have the same sign. This normalization gives scale*C*A^-1 without an extra factor two.",
            angular_mean_retained=True, two_regular_ports_not_deleted="The paired complete-cap regular coordinate is still required when assembling the desired finite low block.",
            whole_eta_interval=ident["exact_parameter_interval"])
        arrays = args.out.with_suffix(".npz")
        arrays.parent.mkdir(parents=True, exist_ok=True)
        Pchosen = real_midpoint(P)
        np.savez_compressed(
            arrays, core_DN_even_waist=chosen,
            diagnostic_positive_cos_transfer_center=Pchosen)
        report["arrays"] = dict(
            path=str(arrays), sha256=sha(arrays), bytes=arrays.stat().st_size,
            definition="core_DN_even_waist is an exact dyadic Hermitian center with the complete radius stated above. The positive transfer is a diagnostic selected center with its separate selection fee.")
        report["diagnostic_positive_transfer_selection_error"] = ball_record(
            norm(P-exact_matrix(Pchosen)))
        if args.old_core.exists():
            old = read(args.old_core)
            old_arrays = old["arrays"]
            if old["object_sha256"] != ident["object_sha256"]:
                raise ValueError("old diagnostic belongs to another object")
            if old["exact_physical_cuts"] != ["-1/4", "1/4"]:
                raise ValueError("old diagnostic has different physical ports")
            if sha(old_arrays["path"]) != old_arrays["sha256"]:
                raise ValueError("old diagnostic arrays changed")
            with np.load(old_arrays["path"], allow_pickle=False) as data:
                old_center = exact_matrix(np.array(data["core_DN"], copy=True))
            V = paired_cut_heights(Q)
            old_even = adjoint(V)*old_center*V
            difference = norm(exact_matrix(chosen)-old_even)
            report["old_floating_core_even_comparison"] = dict(
                path=str(args.old_core), sha256=sha(args.old_core),
                old_scope="Only a previously saved floating diagnostic.",
                selected_center_difference=ball_record(difference),
                true_uniform_even_DN_minus_old_center_upper=ball_record(
                    (difference+total).upper()))
        report["complete"] = True
        report["scope"] = [
            "All original accepted positive leaves and the entire same eta interval are required and checked.",
            "Actual angular and waist symmetry determine the complete desired finite problem, retaining the angular mean.",
            "No full finite P inverse, reflected whole transfer or odd-waist Dirichlet inverse is required.",
            "The six-dimensional complete low block still needs the true cap, uniform quarter-cut multipliers and full symmetric high feedback.",
            "No full infinite-core DN inverse is assumed or certified."]
    except Exception as exc:
        report.update(failure=repr(exc), traceback=traceback.format_exc())
    report.update(
        CPU_seconds=time.process_time()-cpu, wall_seconds=time.monotonic()-wall,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            "fourfold_phase_core_flow_collect.py", "fourfold_phase_core_cell_flow.py",
            "fourfold_phase_core_flow_cover.py", "fourfold_phase_low_feedback_paid_inputs.py",
            "fourfold_phase_cap_energy_collect.py", "fourfold_phase_beta_bulk_interval.py")})
    if trace:
        tp = args.out.with_suffix(".prefix-trace.json.gz")
        tp.parent.mkdir(parents=True, exist_ok=True)
        with gzip.GzipFile(filename=str(tp), mode="wb", mtime=0) as f:
            f.write((json.dumps(trace, sort_keys=True, allow_nan=False)+"\n").encode())
        report["complete_ordered_prefix_trace"] = dict(
            path=str(tp), sha256=sha(tp), bytes=tp.stat().st_size)
    write(args.out, report)
    print(json.dumps({key:report.get(key) for key in (
        "complete", "accepted_real_leaves", "angular_Cauchy_dimension",
        "true_positive_cos_transfer_error", "actual_finite_even_core_DN_error",
        "height_A_inverse_perturbation_product", "failure", "CPU_seconds")},
        indent=2, allow_nan=False), flush=True)
    if not report["complete"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
