#!/usr/bin/env python3
"""Certify the exact four dihedral blocks of a saved finite low candidate.

The actual geometry preserves angular reflection. This program changes only
the finite candidate and computes directed inverses of its four joint parity blocks.
It does not certify the unpaid core propagation or infinite high feedback.
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
from fourfold_phase_low_feedback_paid_inputs import (
    adjoint, eye, hermitian_enclosure, matrix, midpoint, norm)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    def reject(value):
        raise ValueError("nonfinite JSON constant "+value)
    return json.loads(Path(path).read_text(), parse_constant=reject)


def order_weight(k, order):
    x = arb(max(1, 4*abs(k)))
    if order == 0:
        return arb(1)
    if order == Fraction(1, 2):
        return x.sqrt()
    if order == 1:
        return x
    if order == Fraction(3, 2):
        return x*x.sqrt()
    if order == 2:
        return x*x
    raise ValueError("unsupported explicitly normalized height order")


def involutions(N):
    n, dimension = 2*N+1, 4*N+5
    angular, radial = list(range(dimension)), list(range(dimension))
    signs = [1]*dimension
    for offset in (0, n):
        for k in range(-N, N+1):
            angular[offset+N+k] = offset+N-k
    for j in range(n):
        radial[j], radial[n+j] = n+j, j
    radial[2*n], radial[2*n+1] = 2*n+1, 2*n
    signs[-1] = -1
    S, J = acb_mat(dimension, dimension), acb_mat(dimension, dimension)
    for i in range(dimension):
        S[i, angular[i]] = 1
        J[i, radial[i]] = signs[i]
    return S, J, angular, radial, signs


def joint_basis(N, angular_sign, waist_sign):
    n, dimension = 2*N+1, 4*N+5
    count = N+(2 if angular_sign == 1 else 0)
    if angular_sign == 1 and waist_sign == -1:
        count += 1
    result = acb_mat(dimension, count)
    labels, column = [], 0
    s = 1/arb(2).sqrt()
    if angular_sign == 1:
        result[N, column] = s
        result[n+N, column] = waist_sign*s
        labels.append("paired angular mean")
        column += 1
    for k in range(1, N+1):
        if angular_sign == 1:
            zplus, zminus = acb(arb(1)/2), acb(arb(1)/2)
            label = "cos("+str(4*k)+"theta)"
        else:
            zplus, zminus = acb(0, -arb(1)/2), acb(0, arb(1)/2)
            label = "sin("+str(4*k)+"theta)"
        result[N+k, column], result[N-k, column] = zplus, zminus
        result[n+N+k, column] = waist_sign*zplus
        result[n+N-k, column] = waist_sign*zminus
        labels.append("paired "+label)
        column += 1
    if angular_sign == 1:
        result[2*n, column] = s
        result[2*n+1, column] = waist_sign*s
        labels.append("paired regular mean")
        column += 1
        if waist_sign == -1:
            result[dimension-1, column] = 1
            labels.append("translation border")
            column += 1
    if column != count:
        raise ValueError("incorrect joint parity dimension")
    return result, labels


def inverse_certificate(A):
    chosen = midpoint(A)
    if np.any(~np.isfinite(chosen)):
        raise ValueError("nonfinite finite parity center")
    row = dict(dimension=A.nrows(), inverse_certified=False)
    selection = norm(A-matrix(chosen))
    row["saved_center_selection_error"] = ball_record(selection)
    try:
        candidate = np.linalg.inv(chosen)
    except np.linalg.LinAlgError as exc:
        row["failure"] = "floating preconditioner unavailable: "+str(exc)
        return row, chosen, None
    if np.any(~np.isfinite(candidate)):
        row["failure"] = "floating preconditioner is nonfinite"
        return row, chosen, None
    R = matrix(candidate)
    residual = norm(eye(A.nrows())-R*A)
    candidate_norm = norm(R)
    row.update(inverse_candidate_residual=ball_record(residual),
               inverse_candidate_norm=ball_record(candidate_norm))
    if residual < 1:
        bound = (candidate_norm/(1-residual)).upper()
        row.update(inverse_certified=True,
                   exact_parity_block_inverse_norm_upper=ball_record(bound))
    else:
        row["failure"] = "directed inverse residual is not below one"
    return row, chosen, candidate


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--paid-low", type=Path,
        default=Path("notes/2026-11-12-actual-low-feedback-paid-cap-interface-M4.json"))
    ap.add_argument("--height-order", type=Fraction, default=Fraction(0))
    ap.add_argument("--bits", type=int, default=256)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    ctx.prec = args.bits
    if args.height_order not in (0, Fraction(1, 2), 1, Fraction(3, 2), 2):
        raise ValueError("height order must be 0, 1/2, 1, 3/2 or 2")
    src = read(args.paid_low)
    if not src.get("complete") or src.get("kind") != (
        "paid_cap_and_interface_fees_for_exact_finite_low_feedback_candidate"):
        raise ValueError("unexpected or incomplete finite candidate report")
    record = src["arrays"]
    arrays_path = Path(record["path"])
    if sha(arrays_path) != record["sha256"]:
        raise ValueError("saved finite candidate arrays changed")
    with np.load(arrays_path, allow_pickle=False) as data:
        values = np.array(data["finite_bordered_center"], copy=True)
        translation = np.array(data["translation"], copy=True)
    N = int(src["modes"])
    n, dimension = 2*N+1, 4*N+5
    if N < 1 or values.shape != (dimension, dimension):
        raise ValueError("unexpected full bordered dimension")
    if translation.shape != (dimension-1,) or np.any(~np.isfinite(values)):
        raise ValueError("invalid complete finite input")
    S, J, angular, radial, signs = involutions(N)
    t = np.concatenate((translation, [0]))
    if not np.array_equal(t, t[angular]):
        raise ValueError("the saved translation border is not angular even")
    if not np.array_equal(-t, np.asarray(signs)*t[radial]):
        raise ValueError("the saved translation vector is not waist odd")

    A = matrix(values)
    H = hermitian_enclosure(A)
    angular_average = (H+S*H*S)/2
    symmetric = (angular_average+J*angular_average*J)/2
    weights = []
    for _ in (0, n):
        weights.extend(order_weight(k, args.height_order) for k in range(-N, N+1))
    weights.extend((arb(1), arb(1), arb(1)))
    weighted = acb_mat(dimension, dimension)
    for i in range(dimension):
        for j in range(dimension):
            weighted[i, j] = symmetric[i, j]/(weights[i]*weights[j])
    known_fee = (
        arb(src["total_paid_finite_matrix_fee"]["ball"]).upper()
        +arb(src["saved_binary_center_selection_error"]["ball"]).upper()).upper()
    sectors, saved, bases = {}, {}, {}
    for key, alpha, rho in (
        ("angular_even_waist_even", 1, 1),
        ("angular_even_waist_odd", 1, -1),
        ("angular_odd_waist_even", -1, 1),
        ("angular_odd_waist_odd", -1, -1)):
        Q, labels = joint_basis(N, alpha, rho)
        block = hermitian_enclosure(adjoint(Q)*weighted*Q)
        row, chosen, candidate = inverse_certificate(block)
        row.update(angular_sign=alpha, waist_sign=rho, coordinates=labels)
        if row["inverse_certified"]:
            bound = arb(row["exact_parity_block_inverse_norm_upper"]["ball"]).upper()
            row["known_partial_fee_product"] = ball_record((bound*known_fee).upper())
            row["remaining_unpaid_error_allowance"] = ball_record(
                (1/bound-known_fee).lower())
        sectors[key], bases[key] = row, Q
        saved[key+"_center"] = chosen
        if candidate is not None:
            saved[key+"_dyadic_inverse_candidate"] = candidate
    cross = []
    keys = list(sectors)
    for i, ki in enumerate(keys):
        for kj in keys[i+1:]:
            cross.append(dict(sectors=[ki, kj], exact_zero=True,
                arithmetic_enclosure=ball_record(norm(adjoint(bases[ki])*weighted*bases[kj]))))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    array_out = args.out.with_suffix(".npz")
    saved["angular_reflection_permutation"] = np.asarray(angular, dtype=np.int64)
    saved["waist_permutation"] = np.asarray(radial, dtype=np.int64)
    saved["waist_signs"] = np.asarray(signs, dtype=np.int64)
    np.savez_compressed(array_out, **saved)
    report = dict(
        kind="exact_dihedral_compressions_of_saved_finite_low_candidate",
        complete=True, source_sha256=sha(__file__), bits=args.bits,
        input_report=dict(path=str(args.paid_low), sha256=sha(args.paid_low)),
        input_arrays=record, object_sha256=src["object_sha256"],
        exact_delta_fraction=src["exact_delta_fraction"], modes=N,
        physical_cut="1/4", height_order=str(args.height_order),
        full_dimension=dimension, angular_even_dimension=2*N+5,
        angular_odd_dimension=2*N,
        desired_sector="angular_even_waist_even",
        desired_sector_dimension=N+2,
        full_port_order="left -N..N, right -N..N, left regular, right regular, translation border",
        Hilbert_normalization="W diagonal: height Fourier k has max(1,4|k|)^s, both regular slots and border have weight one; the Hermitian form matrix is W^-1 A W^-1.",
        exact_candidate_definition="Take the Hermitian part of the saved exact dyadic bordered matrix, then average over both commuting exact involutions S and J. Restrict by the exactly normalized joint parity bases defined in the source.",
        hermitian_projection_change=ball_record(norm(A-H)),
        angular_projection_change=ball_record(norm(H-angular_average)),
        waist_projection_change=ball_record(norm(angular_average-symmetric)),
        complete_cross_block_rounding_enclosures=cross,
        exact_cross_blocks_zero=True,
        known_partial_finite_fee=ball_record(known_fee),
        known_fee_scope="Original paid cap/interface/symmetrization fees plus saved-center selection. Unpaid actual core and high-feedback errors remain excluded. Both group averages and the isometries contract errors relative to the actual symmetric target; W^-1 has norm <=1 for the allowed orders.",
        sectors=sectors,
        desired_angular_mean_retained=True,
        desired_symmetric_regular_mean_retained=True,
        translation_border_retained_in_angular_even_waist_odd_sector=True,
        actual_core_radial_error_paid=src.get("actual_core_radial_error_paid", False),
        entire_eta_family_certified=False,
        rigorous_full_Schur_inverse=False,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in
            ("fourfold_phase_low_feedback_paid_inputs.py",
             "fourfold_phase_cap_energy_collect.py", "fourfold_phase_beta_interval.py")},
        arrays=dict(path=str(array_out), sha256=sha(array_out), bytes=array_out.stat().st_size),
        scope=[
            "Only the saved finite candidate is decomposed and inverted here.",
            "R105 proves the exact actual involutions, including the positive left groundstate -Yz and right groundstate +Yz.",
            "The desired invariant Newton problem may use the (N+2)-dimensional block only when its source, geometry, realization and nonlinear reconstruction retain the full stated symmetry.",
            "The paired regular trace/flux and angular mean remain genuine ports; translation compatibility follows from symmetry and is not replaced by deleting a nonzero source.",
            "The actual finite core and complete symmetric high problem remain necessary; no new numerical inverse is inferred before execution."])
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps({key:report[key] for key in
        ("complete", "full_dimension", "desired_sector_dimension", "sectors",
         "entire_eta_family_certified", "rigorous_full_Schur_inverse")},
         indent=2, allow_nan=False), flush=True)


if __name__ == "__main__":
    main()
