#!/usr/bin/env python3
"""Exact original new519 row-block attribution for the actual43 direction.

Consume the completed three-action comparison and byte-bound original
residual/scales. No root, RHS, J, ODE, solve, trial, or repeat A-matvec runs.
All rational arithmetic belongs only to this public repository's Actions.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import resource
import struct
import sys
import time
import traceback

EXACT_NAME = "exact_20261114_single_step_rational_action.py"
EXACT_SHA = "9c42982291bd1a7b7cf21c472d8aae877136fb884708a8310ca6bb882c1d103e"
DIRECTION_RESULT_SHA = "cf6e00345697ed8bd4a114c2d79f8625e49626d2263e83f42e7dc60e3020013e"
STEP_SYSTEM_SOURCE_SHA = "fde0e03918814c9400a37eeb7719ecd0894c204490ee830fa128a3a49797cc81"
STAGE, INPUT_NODE, ORIGINAL_STAGE, ORIGINAL_STEP = 519, 520, 43, 11
M, K, SIZE = 112, 224, 226
HEX_INTEGER = re.compile(r"-?0x[0-9a-f]+\Z")


def load_exact_reader():
    path = Path(__file__).resolve().parent / EXACT_NAME
    if hashlib.sha256(path.read_bytes()).hexdigest() != EXACT_SHA:
        raise ValueError("The frozen exact-action source bytes changed")
    spec = importlib.util.spec_from_file_location("_pinned_original_new519_exact_reader", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    # The imported file has no numerical execution at module scope. Only
    # byte/metadata helpers and exact encoders are used below; never compare_action.
    return module


def parse_rational(value):
    if not isinstance(value, dict):
        raise ValueError("A complete exact rational record is required")
    n, d = value.get("numerator_hex"), value.get("denominator_hex")
    if (not isinstance(n, str) or HEX_INTEGER.fullmatch(n) is None
            or not isinstance(d, str) or HEX_INTEGER.fullmatch(d) is None):
        raise ValueError("Exact rational integers must retain their hexadecimal representation")
    numerator, denominator = int(n, 16), int(d, 16)
    if denominator <= 0:
        raise ValueError("An exact rational denominator must be positive")
    return Fraction(numerator, denominator)


def vector(value, length):
    if not isinstance(value, list) or len(value) != length:
        raise ValueError("The complete exact action vector has the wrong dimensions")
    return [parse_rational(entry) for entry in value]


def dot(left, right):
    if len(left) != len(right):
        raise ValueError("Complete rational dot-product dimensions differ")
    return sum((a*b for a, b in zip(left, right)), Fraction(0))


def norm_squared(value):
    return dot(value, value)


def write_ratio(E, numerator, denominator):
    return E.rational_json(numerator/denominator, True) if denominator != 0 else None


def load_inputs(E, args):
    E.same(args.direction_result_sha256, DIRECTION_RESULT_SHA, "actual43 complete result pin")
    source_row, provenance = E.direction_vector(
        args.direction_result, args.direction_result_sha256)
    direction_directory = args.direction_result.resolve().parent
    result, result_receipt = E.read_json(args.direction_result, args.direction_result_sha256)
    direction_raw = E.descriptor_bytes(direction_directory, result["step_delta"], (1373, K))
    checkpoint = E.object_file(direction_directory, result["step_direction_checkpoint"])
    system_binding = checkpoint["original_input_binding"]
    E.same(system_binding.get("adapter_source_sha256"), STEP_SYSTEM_SOURCE_SHA, "original step-system definition")
    E.same(system_binding.get("new_matrix_identity_sha256"), E.ORIGINAL_MATRIX_SHA, "same original1372 finite matrix")
    old_to_new = system_binding.get("old_to_new")
    if not isinstance(old_to_new, list) or len(old_to_new) != 577:
        raise ValueError("The complete original-to-expanded node mapping is required")
    E.same(old_to_new[ORIGINAL_STAGE], STAGE, "original43 outgoing node maps to new519")
    cells = system_binding.get("cells")
    blocks = system_binding.get("complete_block_manifest")
    if not isinstance(cells, list) or len(cells) != 1372 or not isinstance(blocks, list) or len(blocks) != 1372:
        raise ValueError("The complete original expanded-cell/block mapping is required")
    cell = cells[STAGE]
    for key, expected in (("newStage", STAGE), ("originalStage", ORIGINAL_STAGE),
                          ("stepIndex", ORIGINAL_STEP), ("originalStepCount", 12),
                          ("kind", "actual-original-RK-step"), ("port", "original-exit")):
        E.same(cell.get(key), expected, "selected original step " + key)
    block = blocks[STAGE]
    for key, expected in (("new_stage", STAGE), ("original_stage", ORIGINAL_STAGE),
                          ("step_index", ORIGINAL_STEP)):
        E.same(block.get(key), expected, "selected saved short-J block " + key)

    arrays = result["original_bound_system_arrays"]
    residual_desc, scale_desc = arrays["stage-residuals"], arrays["original-scales"]
    residual_raw = E.descriptor_bytes(direction_directory, residual_desc, (1372, K))
    scale_raw = E.descriptor_bytes(direction_directory, scale_desc, (1, 1373))
    original_hashes = system_binding["raw_array_sha256"]
    for name, desc in (("stage-residuals", residual_desc), ("original-scales", scale_desc)):
        E.same(desc["sha256"], original_hashes.get(name), "complete original matrix array " + name)
    r_raw = residual_raw[STAGE*K*8:(STAGE+1)*K*8]
    out_delta_raw = direction_raw[STAGE*K*8:(STAGE+1)*K*8]
    in_delta_raw = direction_raw[INPUT_NODE*K*8:(INPUT_NODE+1)*K*8]
    E.same(in_delta_raw, source_row, "same actual43 incoming direction bytes")
    sigma_raw = scale_raw[STAGE*8:(STAGE+1)*8]
    sigma = E.rational(E.decode(sigma_raw)[0])
    if sigma <= 0:
        raise ValueError("The original stored sigma must be positive")

    exact_dir = args.exact_directory.resolve()
    exact, exact_receipt = E.read_json(exact_dir/"result.json.gz", args.exact_result_sha256)
    E.same(exact.get("schema"), "saved-four-local-J-exact-rational-RK4-action-v1", "completed action schema")
    E.same(exact.get("source_sha256"), EXACT_SHA, "completed action producer")
    E.same(exact.get("completed"), True, "completed exact comparison")
    for key in ("new_root_calls", "new_local_J_calls", "new_ODE_steps", "native_solves", "nonlinear_trials"):
        E.same(exact.get(key), 0, "exact comparison introduces no " + key)
    selected = [row for row in exact.get("cases", []) if row.get("label") == "actual43-best-node520"]
    if len(selected) != 1:
        raise ValueError("Exactly one completed actual43 incoming-direction action is required")
    selected = selected[0]
    case = E.object_file(exact_dir, selected["exact_action"])
    E.same(case.get("schema"), "saved-four-local-J-exact-rational-case-v1", "complete exact case schema")
    E.same(case.get("source_sha256"), EXACT_SHA, "complete exact case producer")
    E.same(case.get("label"), "actual43-best-node520", "actual43 case label")
    E.same(case.get("provenance"), provenance, "complete same-direction provenance")
    E.same(case.get("input_binding"), exact.get("input_binding"), "same exact input binding file")
    E.same(case.get("input_vector"), selected.get("input_vector"), "same case input descriptor")
    E.same(E.descriptor_bytes(exact_dir, case["input_vector"], (K,)), in_delta_raw,
           "exact action uses the identical incoming vector, without scaling")
    E.same(case.get("shape_columns"), K, "full original shape columns")
    E.same(case.get("full_output_rows"), SIZE, "complete original output rows")
    E.same(case.get("port_is_applied_only_to_final_Pi_shape_rows"), True, "original exit-port placement")
    E.same(case.get("means_are_not_scaled_by_exit_port"), True, "original mean convention")
    E.same(case.get("exact_difference_decomposition_for_all226"), True, "completed three-object exact decomposition")

    action_binding = E.object_file(exact_dir, exact["input_binding"])
    for key, expected in (("original_stage", ORIGINAL_STAGE), ("original_flow_step", ORIGINAL_STEP),
                          ("new_shooting_stage", STAGE), ("new_input_node", INPUT_NODE),
                          ("actual41_result_sha256", E.ACTUAL41_RESULT_SHA),
                          ("original1372_matrix_identity_sha256", E.ORIGINAL_MATRIX_SHA)):
        E.same(action_binding.get(key), expected, "exact capture binding " + key)
    E.same(bytes.fromhex(action_binding["original_sigma"]["float64le_hex"]), sigma_raw,
           "the exact comparison and original row use identical sigma words")
    E.same(action_binding["original_h"], cell["schedule"]["h"], "the original saved h is unchanged")
    descriptors = action_binding.get("all_array_descriptors")
    if not isinstance(descriptors, list):
        raise ValueError("The complete exact-action operand descriptor list is required")
    reference = [entry for entry in descriptors if entry.get("name") == "reference-short-J"]
    if len(reference) != 1:
        raise ValueError("The original actual41 short-J reference must be unique")
    E.same(reference[0]["shape"], [K, K], "complete original short-J shape")
    E.same(reference[0]["bytes"], K*K*8, "complete original short-J byte count")
    E.same(reference[0]["sha256"], block["raw_sha256"], "same actual41 short-J as original1372 stage519")

    actions = {
        "original41_short_J": vector(case["exact_original41_short_J_output"], SIZE)[:K],
        "same_call_observed_short_J": vector(case["exact_same_call_observed_short_J_output"], SIZE)[:K],
        "four_local_A_rational_RK4": vector(case["exact_RK_output"], SIZE)[:K],
    }
    # Re-read every saved action-difference component, rather than trusting a
    # norm or a summary label. This checks exact arithmetic identities only.
    for name, left, right in (
            ("exact_original41_minus_RK", "original41_short_J", "four_local_A_rational_RK4"),
            ("exact_same_call_observed_minus_RK", "same_call_observed_short_J", "four_local_A_rational_RK4"),
            ("exact_original41_minus_same_call_observed", "original41_short_J", "same_call_observed_short_J")):
        difference = vector(case[name], SIZE)
        E.same([actions[left][j]-actions[right][j] for j in range(K)], difference[:K],
               "same saved exact action difference " + name)
    binding = dict(
        actual43_result=result_receipt, actual43_direction=result["step_delta"],
        actual43_complete_checkpoint=result["step_direction_checkpoint"],
        original_stage_residuals=residual_desc, original_scales=scale_desc,
        exact_result=exact_receipt, exact_action=selected["exact_action"],
        exact_case_input=case["input_vector"], exact_input_binding=exact["input_binding"],
        original1372_matrix_identity_sha256=E.ORIGINAL_MATRIX_SHA,
        original_step_system_source_sha256=STEP_SYSTEM_SOURCE_SHA,
        original41_result_sha256=E.ACTUAL41_RESULT_SHA,
        fixed_expanded_stage=STAGE, incoming_node=INPUT_NODE, outgoing_node=STAGE,
        original_stage=ORIGINAL_STAGE, original_flow_step=ORIGINAL_STEP,
        original_sigma_float64le_hex=sigma_raw.hex(),
        original_h=action_binding["original_h"], original_port_ratio=action_binding["original_port_ratio"],
        original_short_J=reference[0], original_cell=cell, original_block_identity=block,
        original_residual_definition=system_binding.get("expanded_residual_rule"),
        residual_row_is_actual_saved_binary64_not_reconstructed=True,
        no_port_applied_again_to_saved_shape_actions=True,
        mean_outputs_not_original_native_stage_equations=True,
        complete_actual43_direction_checkpoint_raw_bits_previously_rechecked=True)
    raw_rows = dict(
        original_residual=r_raw, outgoing_delta=out_delta_raw,
        incoming_delta=in_delta_raw, original_sigma=sigma_raw)
    return E, actions, [E.rational(v) for v in E.decode(r_raw)], \
        [E.rational(v) for v in E.decode(out_delta_raw)], sigma, binding, raw_rows


def build_attribution(E, actions, residual, outgoing_delta, sigma):
    common = [r-d for r, d in zip(residual, outgoing_delta)]
    unscaled = {name:[values[j]+common[j] for j in range(K)] for name, values in actions.items()}
    scaled = {name:[v/sigma for v in values] for name, values in unscaled.items()}
    norms = {name:norm_squared(values) for name, values in scaled.items()}
    pair_definitions = (
        ("original41_minus_observed", "original41_short_J", "same_call_observed_short_J"),
        ("observed_minus_rational", "same_call_observed_short_J", "four_local_A_rational_RK4"),
        ("original41_minus_rational", "original41_short_J", "four_local_A_rational_RK4"))
    pairs = {}
    differences = {}
    for label, left, right in pair_definitions:
        difference = [a-b for a, b in zip(scaled[left], scaled[right])]
        square = norm_squared(difference)
        cross = 2*dot(scaled[right], difference)
        change = norms[left]-norms[right]
        if change != cross+square:
            raise ArithmeticError("An exact row-block square-norm decomposition failed")
        differences[label] = difference
        pairs[label] = dict(
            left=left, right=right,
            squared_norm_difference=E.rational_json(change, True),
            twice_reference_cross_term=E.rational_json(cross, True),
            squared_action_difference=E.rational_json(square, True),
            exact_identity_verified=True,
            signed_norm_difference_over_reference_norm_squared=write_ratio(E, change, norms[right]),
            relative_difference_not_defined_when_reference_zero=(norms[right] == 0))
    d1, d2 = differences["original41_minus_observed"], differences["observed_minus_rational"]
    reference = scaled["four_local_A_rational_RK4"]
    terms = dict(
        rational_residual_squared_norm=norms["four_local_A_rational_RK4"],
        twice_rational_residual_dot_recapture_difference=2*dot(reference, d1),
        twice_rational_residual_dot_same_call_propagation_difference=2*dot(reference, d2),
        recapture_difference_squared_norm=norm_squared(d1),
        same_call_propagation_difference_squared_norm=norm_squared(d2),
        twice_difference_cross_term=2*dot(d1, d2))
    exact_sum = sum(terms.values(), Fraction(0))
    if exact_sum != norms["original41_short_J"]:
        raise ArithmeticError("The complete three-object square-norm decomposition failed")
    rows = []
    for j in range(K):
        rows.append(dict(
            coordinate=E.coordinate(j),
            original_saved_residual=E.rational_json(residual[j]),
            outgoing_delta=E.rational_json(outgoing_delta[j]),
            common_residual_minus_outgoing_delta=E.rational_json(common[j]),
            exact_linear_actions={name:E.rational_json(values[j]) for name, values in actions.items()},
            unscaled_row_residual={name:E.rational_json(values[j]) for name, values in unscaled.items()},
            original_sigma_scaled_row_residual={name:E.rational_json(values[j]) for name, values in scaled.items()},
            original_sigma_scaled_row_square={name:E.rational_json(values[j]*values[j]) for name, values in scaled.items()},
            pairwise_scaled_row_difference={name:E.rational_json(values[j]) for name, values in differences.items()},
            pairwise_row_square_difference={
                label:E.rational_json(scaled[left][j]**2-scaled[right][j]**2)
                for label,left,right in pair_definitions}))
    maxima = {name:E.norm(values, range(K)) for name, values in scaled.items()}
    return dict(
        exact_squared_L2_norms={name:E.rational_json(value, True) for name, value in norms.items()},
        pairwise_square_norm_decompositions=pairs,
        three_object_square_norm_decomposition={name:E.rational_json(value, True) for name,value in terms.items()},
        three_object_sum_equals_original41_squared_norm=True,
        original_sigma_scaled_maxima_for_location_only=maxima,
        no_difference_of_two_maxima_used_for_attribution=True,
        rows=rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exact-directory", type=Path, required=True)
    parser.add_argument("--exact-result-sha256", required=True)
    parser.add_argument("--direction-result", type=Path, required=True)
    parser.add_argument("--direction-result-sha256", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    E = load_exact_reader()
    E.actions_only()
    E.require_sha(args.exact_result_sha256, "completed exact comparison result")
    E.require_sha(args.direction_result_sha256, "actual43 result")
    args.out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    source_sha = E.digest(Path(__file__).read_bytes())
    report = dict(
        schema="actual43-original-new519-exact-rational-residual-attribution-v1",
        source_sha256=source_sha, frozen_exact_action_source_sha256=EXACT_SHA,
        completed=False, original_stage_rows=K, fixed_stage=STAGE,
        equation="(J519 delta520 - delta519 + original_saved_r519) / original_sigma519",
        three_maps_share_identical_delta_r_sigma_and_original_port_convention=True,
        square_norms_are_exact_and_do_not_take_irrational_square_roots=True,
        new_root_calls=0, new_J_calls=0, new_ODE_steps=0, new_solves=0, new_trials=0,
        repeated_four_A_matvecs=0, no_new_scientific_gate=True,
        original_J_accuracy_or_true_DF_error_certified=False,
        one_block_does_not_establish_global_system_or_nonlinear_improvement=True,
        native_accepted=False, task_completed=False)
    try:
        unused_E, actions, residual, out_delta, sigma, binding, rows = load_inputs(E, args)
        report["input_binding"] = E.write_json(args.out, "input-binding.json", binding)
        report["actual_row_input_bytes"] = {
            name:E.write_raw(args.out, name+".f64le", raw, (1,) if name=="original_sigma" else (K,))
            for name,raw in rows.items()}
        computation = build_attribution(E, actions, residual, out_delta, sigma)
        detail = dict(
            schema="actual43-new519-complete-exact-row-attribution-v1",
            source_sha256=source_sha, input_binding=report["input_binding"],
            actual_row_input_bytes=report["actual_row_input_bytes"], **computation)
        report["all224_exact_rows"] = E.write_json(
            args.out, "all224-exact-rows.json.gz", detail, compressed=True)
        for key,value in computation.items():
            if key != "rows":
                report[key] = value
        report["completed"] = True
    except Exception as error:
        report["actual_error"] = repr(error)
        raw = traceback.format_exc().encode()
        with (args.out/"failure-traceback.txt").open("xb") as stream:
            stream.write(raw)
        report["failure_traceback"] = dict(file="failure-traceback.txt",bytes=len(raw),sha256=E.digest(raw))
    finally:
        report["elapsed_seconds"] = time.monotonic()-started
        report["maximum_RSS_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        full = E.write_json(args.out,"result.json.gz",report,compressed=True)
        summary = dict(report,full_result=full)
        if len(json.dumps(summary,allow_nan=False).encode()) >= 90000:
            summary = {key:report[key] for key in (
                "schema","source_sha256","frozen_exact_action_source_sha256","completed",
                "fixed_stage","equation","native_accepted","task_completed","elapsed_seconds","maximum_RSS_kib")}
            summary["full_result"] = full
            summary["exact_rational_details_in_full_result"] = True
            if "all224_exact_rows" in report:
                summary["all224_exact_rows"] = report["all224_exact_rows"]
            if "actual_error" in report:
                summary["actual_error"] = report["actual_error"]
        summary_file = E.write_json(args.out,"summary.json",summary)
        print(json.dumps(dict(
            event="original_new519_exact_attribution_finished",completed=report["completed"],
            summary=summary_file,native_accepted=False,task_completed=False)),flush=True)
    return 0 if report["completed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
