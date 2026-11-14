#!/usr/bin/env python3
"""Finite circle Newton using one complete exact-affine actual-ray grid.

State residual, state Jacobian and parameter column all come from the same
fresh ODE grid. The input H is the defined dyadic polynomial, not a circle-map
interpolant. Every predicted parameter/H requires a new dyadic H budget, tight
root and fresh actual rays before nonlinear acceptance. This is floating only.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_circle_actual_newton import real_basis
from fourfold_circle_conjugacy import TWOPI, target_value


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--actual-nodes", type=Path, required=True)
    parser.add_argument("--base-object", type=Path, required=True)
    parser.add_argument("--dyadic-conjugacy", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--new-object", type=Path, required=True)
    parser.add_argument("--damping", type=float, default=1.)
    args = parser.parse_args()
    if not 0 < args.damping <= 1:
        raise ValueError("damping must lie in (0,1]")
    data = json.loads(args.actual_nodes.read_text())
    definition = json.loads(args.base_object.read_text())
    polynomial = json.loads(args.dyadic_conjugacy.read_text())
    if data["status"] != "complete" or data["source_sha256"] != digest(args.base_object):
        raise ValueError("a complete actual grid of exactly the base object is required")
    if data["dyadic_conjugacy_sha256"] != digest(args.dyadic_conjugacy):
        raise ValueError("actual grid uses another H")
    base_delta = float.fromhex(definition["delta_hex"])
    if Fraction(data["exact_delta_fraction"]) != Fraction.from_float(base_delta):
        raise ValueError("actual grid parameter coordinate differs")
    keys = ("x", "input_physical_angles", "returned_physical_angles", "angular_derivative",
            "parameter_column_physical")
    arrays = [np.concatenate([block[key] for block in data["completed_blocks"]]) for key in keys]
    order = np.argsort(arrays[0])
    x, theta, returned, jacobian, column = [array[order] for array in arrays]
    count = len(x)
    if count != data["rays"]:
        raise ValueError("incomplete actual grid")
    ideal = np.arange(count)*TWOPI/count
    grid_error = float(np.max(abs(x-ideal)))
    if grid_error > 2e-14:
        raise ValueError("actual nodes do not form one complete uniform circle grid")
    x = ideal
    basis, labels = real_basis(x, count)
    target = data["target"]
    alpha = TWOPI*target_value(target)
    shifted, _ = real_basis(x+alpha, count)
    degree = int(polynomial["H_degree"])
    if degree >= count//2:
        raise ValueError("use an actual grid resolving the input H below Nyquist")
    denominator = 2**int(polynomial["denominator_power_of_two"])
    coefficients = polynomial["h_nonnegative_integer_coefficients"]
    constant = int(coefficients[0][0])/denominator
    if int(coefficients[0][1]) != 0:
        raise ValueError("H must be real")
    initial = np.zeros(len(labels))
    for index, (k, kind) in enumerate(labels):
        if k <= degree:
            real, imag = map(int, coefficients[k])
            initial[index] = 2*(real if kind == "cos" else -imag)/denominator
    input_error = float(np.max(abs(x+constant+basis@initial-4*theta)))
    if input_error > 2e-13:
        raise ValueError("actual input angles are not evaluations of this H")
    error = 4*returned-x-alpha-constant-shifted@initial
    parameter_column = 4*column
    matrix = np.column_stack((jacobian[:, None]*basis-shifted, parameter_column))
    correction = np.linalg.solve(matrix, -error)
    proposed = initial+args.damping*correction[:-1]
    dp = float(args.damping*correction[-1])
    new_delta = float(base_delta+dp)
    if abs(new_delta) > .01:
        raise ValueError("predicted exact affine parameter leaves the certified R57 tube")
    dense = np.arange(16*count)*TWOPI/(16*count)
    derivative_basis, _ = real_basis(dense, count, 1)
    hprime = 1+derivative_basis@proposed
    if hprime.min() <= 0:
        raise ValueError("predicted H derivative loses positivity at diagnostic nodes")
    new_degree = count//2
    export_x = np.arange(2*new_degree+1)*TWOPI/(2*new_degree+1)
    export_basis, _ = real_basis(export_x-constant, count)
    h_values = export_basis@proposed
    exact_delta = Fraction.from_float(new_delta)
    metadata = dict(kind="floating_exact_affine_actual_value_J_parameter_circle_Newton_prediction",
                    source_sha256=data["source_sha256"], source_H_sha256=data["dyadic_conjugacy_sha256"],
                    target=target, rotation_number=target_value(target), angular_scale=4.,
                    base_parameter_delta=base_delta, parameter_correction=dp,
                    proposed_parameter_delta=new_delta, exact_delta_fraction=str(exact_delta),
                    degree=new_degree, precomposition_angle=-constant,
                    curve_direction_sha256=data["curve_direction_sha256"])
    np.savez_compressed(args.checkpoint, h_values=h_values, metadata=np.array(json.dumps(metadata)))
    new_definition = {key:value for key,value in definition.items() if key not in
                      ("recovery_note", "legacy_labels", "delta", "delta_hex", "delta_fraction")}
    new_definition.update(delta=new_delta, delta_hex=new_delta.hex(),
                          delta_fraction=dict(numerator=str(exact_delta.numerator),denominator=str(exact_delta.denominator)),
                          construction_note="New exact affine parameter; no control-vector rounding. Its H and rays still require fresh validation.",
                          predecessor_object_sha256=digest(args.base_object),
                          prediction_actual_nodes_sha256=digest(args.actual_nodes))
    args.new_object.write_text(json.dumps(new_definition, indent=2, ensure_ascii=False)+"\n")
    exact_step = exact_delta-Fraction.from_float(base_delta)
    report = dict(**metadata, actual_samples=count, parameter_samples=count,
                  all_parameter_values_from_same_actual_grid=True,
                  run_source_sha256=digest(Path(__file__)),
                  actual_nodes_sha256=digest(args.actual_nodes),
                  checkpoint_sha256=digest(args.checkpoint), new_object_sha256=digest(args.new_object),
                  complete_grid_error=grid_error, initial_dyadic_H_evaluation_difference=input_error,
                  initial_actual_collocation_residual=float(np.max(abs(error))),
                  linear_residual=float(np.max(abs(matrix@correction+error))),
                  damping=args.damping,
                  predicted_damped_linear_residual=float(np.max(abs(matrix@(args.damping*correction)+error))),
                  proposed_Hprime_sample_range=[float(hprime.min()),float(hprime.max())],
                  proposed_H_correction_sample_max=float(np.max(abs(basis@(args.damping*correction[:-1])))),
                  proposed_Hprime_correction_sample_max=float(np.max(abs(derivative_basis@(args.damping*correction[:-1])))),
                  matrix_condition_number=float(np.linalg.cond(matrix)),
                  exact_parameter_step=str(exact_step),
                  parameter_addition_rounding_error=str(exact_step-Fraction.from_float(dp)),
                  basis_labels=labels, initial_coefficients=initial.tolist(),
                  coefficient_correction=(args.damping*correction[:-1]).tolist(),
                  limitations=["actual ODE values/J/parameter columns remain floating with unvalidated primitive and arithmetic errors",
                    "finite Newton prediction; no nonlinear acceptance without fresh actual rays",
                    "new H needs its own exact dyadic and inverse-derivative certificate",
                    "new exact affine object needs a tight-root reference at its own parameter",
                    "no full R31 complex/Wiener E/P/Q/T/B estimate or exact PDE/closed-surface result"])
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps({key:report[key] for key in ("proposed_parameter_delta", "parameter_correction",
        "initial_actual_collocation_residual", "linear_residual", "proposed_Hprime_sample_range",
        "proposed_H_correction_sample_max", "proposed_Hprime_correction_sample_max",
        "matrix_condition_number")}), flush=True)


if __name__ == "__main__":
    main()
