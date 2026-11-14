#!/usr/bin/env python3
"""Exact rational actions of four saved original RK4 local Jacobians.

Only the public repository's GitHub Actions may execute the calculations.
The input matrices are finite binary64 arrays interpreted as exact dyadics.
No native engine, root, ODE, local Jacobian, solver, or trial is called here.
The old saved short-J is compared as an exact binary-array linear map.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import re
import resource
import struct
import sys
import time
import traceback

PUBLIC_REPOSITORY = "Rogerhu12/math-research-public"
M, K, SIZE = 112, 224, 226
STAGE, STEP, NEW_STAGE, INPUT_NODE = 43, 11, 519, 520
ACTUAL41_RESULT_SHA = "6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf"
ORIGINAL_MATRIX_SHA = "e929e642a9738c98d97dc06129c396b8fdff09aac32430892a412701d5dd4521"
ORIGINAL_FLOW_SHA = "717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f"
GAUGE_PRODUCER_SHA = "16fca40ec0ff21a119ce1563241692248005ec6587af000efb968c5158ad9a00"
GAUGE_SOURCE_SHA = "24a51a4e804859bcdbed78b133599a073c6a0a890039e5fe5500281ef7e90b92"
CAPTURE_RESULT_SCHEMA = "original-native-stage43-local-j-capture-result-v1"
CAPTURE_ARRAY_SCHEMA = "original-native-stage43-local-j-arrays-v1"
CAPTURE_SOURCE_PINS = {
    "geometry_20261114_native_stage43_local_j_probe.py":
        "1185bbda5390c7ef3a9043ac59139b9359fececc802146f4be64aa7639730b21",
    "geometry_20261114_native_stage43_local_j_probe_hook.mjs":
        "8992f3920729b0f6eabf7a1e15520290fc47942c72c0c4d6433d8ac6cb291059",
    "geometry_20261114_native_stage43_local_j_window.mjs":
        "966ddc4946cc63f69260dd1871c2ac31ad0383eb5593f6c3a0b45b0cfcdef5ec",
}
CAPTURE_RECORD_SOURCE_FIELDS = {
    "source_sha256": "geometry_20261114_native_stage43_local_j_probe.py",
    "hook_sha256": "geometry_20261114_native_stage43_local_j_probe_hook.mjs",
    "window_module_sha256": "geometry_20261114_native_stage43_local_j_window.mjs",
}
ACTUAL44_FIELD_RECEIPT_SHA = "d7d00de365b2118e1346e8f8630d5bad408957da91fdf51f38496f73b0e0c5f2"

HEX64 = re.compile(r"[0-9a-f]{16}\Z")
SHA256 = re.compile(r"[0-9a-f]{64}\Z")


def actions_only():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != PUBLIC_REPOSITORY):
        raise RuntimeError("Scientific evaluation is restricted to this public repository's Actions")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def require_sha(value, label):
    if not isinstance(value, str) or SHA256.fullmatch(value) is None:
        raise ValueError("An explicit complete SHA256 is required: " + label)
    return value


def same(actual, expected, label):
    if actual != expected:
        raise ValueError("Input identity mismatch: " + label)


def safe_file(directory, relative):
    if not isinstance(relative, str):
        raise ValueError("A relative input file name is required")
    rel = Path(relative)
    if rel.is_absolute() or not rel.parts or any(p in (".", "..") for p in rel.parts):
        raise ValueError("Unsafe relative input path")
    base = Path(directory).resolve()
    path = base.joinpath(rel)
    if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(base):
        raise ValueError("A contained regular input file is required: " + relative)
    return path


def json_bytes(raw, compressed=False):
    return json.loads(gzip.decompress(raw) if compressed else raw)


def read_json(path, expected_sha=None):
    path = Path(path)
    raw = path.read_bytes()
    if expected_sha is not None:
        same(digest(raw), require_sha(expected_sha, str(path)), "complete JSON file")
    return json_bytes(raw, path.name.endswith(".gz")), dict(
        file=path.name, bytes=len(raw), sha256=digest(raw))


def descriptor_bytes(directory, descriptor, shape=None):
    if not isinstance(descriptor, dict):
        raise ValueError("A complete raw-array descriptor is required")
    path = safe_file(directory, descriptor["file"])
    raw = path.read_bytes()
    same(len(raw), descriptor["bytes"], "raw byte count")
    same(digest(raw), require_sha(descriptor["sha256"], descriptor["file"]), "raw SHA256")
    same(descriptor.get("dtype"), "<f8", "raw binary64 dtype")
    same(descriptor.get("order"), "C", "raw array order")
    dims = descriptor.get("shape")
    if not isinstance(dims, list) or not dims or any(type(n) is not int or n < 0 for n in dims):
        raise ValueError("Explicit nonnegative integer array dimensions are required")
    if shape is not None:
        same(dims, list(shape), "raw array shape")
    count = 1
    for n in dims:
        count *= n
    same(len(raw), 8 * count, "raw dimensions and byte count")
    # This is a complete finite-word check. Signed zero remains in the raw hash.
    for (word,) in struct.iter_unpack("<Q", raw):
        if ((word >> 52) & 2047) == 2047:
            raise ValueError("Nonfinite input word in " + descriptor["file"])
    return raw


def object_file(directory, descriptor):
    if not isinstance(descriptor, dict):
        raise ValueError("A complete JSON descriptor is required")
    path = safe_file(directory, descriptor["file"])
    raw = path.read_bytes()
    same(len(raw), descriptor["bytes"], "JSON descriptor byte count")
    same(digest(raw), require_sha(descriptor["sha256"], descriptor["file"]), "JSON descriptor SHA")
    return json_bytes(raw, path.name.endswith(".gz"))


def compact(value):
    """Normalize an exact dyadic pair (integer, binary exponent)."""
    integer, exponent = value
    if integer == 0:
        return (0, 0)
    shift = (abs(integer) & -abs(integer)).bit_length() - 1
    return (integer >> shift, exponent + shift)


def from_word(word):
    """Decode the finite IEEE754 word directly, without decimal or float casts."""
    exponent = (word >> 52) & 2047
    fraction = word & ((1 << 52) - 1)
    if exponent == 2047:
        raise ValueError("The exact action requires finite binary64 words")
    sign = -1 if word >> 63 else 1
    if exponent == 0:
        return compact((sign * fraction, -1074))
    return compact((sign * ((1 << 52) | fraction), exponent - 1075))


def decode(raw):
    if len(raw) % 8:
        raise ValueError("A complete little-endian binary64 stream is required")
    return [from_word(word) for (word,) in struct.iter_unpack("<Q", raw)]


def number_record(record, label):
    if not isinstance(record, dict) or HEX64.fullmatch(record.get("float64le_hex", "")) is None:
        raise ValueError("A complete original bit record is required: " + label)
    raw = bytes.fromhex(record["float64le_hex"])
    word = struct.unpack("<Q", raw)[0]
    pair = from_word(word)
    value = struct.unpack("<d", raw)[0]
    expected_class = "negative-zero" if word == (1 << 63) else "finite"
    same(record.get("classification"), expected_class, label + " finite classification")
    printed = record.get("value")
    if type(printed) not in (int, float) or not math.isfinite(printed) or float(printed) != value:
        raise ValueError("The bit record and JSON numeric value disagree: " + label)
    return pair


def add(left, right):
    a, e = left
    b, f = right
    if a == 0:
        return right
    if b == 0:
        return left
    common = min(e, f)
    return compact(((a << (e - common)) + (b << (f - common)), common))


def multiply(left, right):
    if left[0] == 0 or right[0] == 0:
        return (0, 0)
    return compact((left[0] * right[0], left[1] + right[1]))


def rational(value):
    a, e = value
    return Fraction(a << e, 1) if e >= 0 else Fraction(a, 1 << -e)


def pair_json(value):
    a, e = compact(value)
    return {"integer_hex": hex(a), "binary_exponent": e}


def rational_json(value, decimal=False):
    result = {"numerator_hex": hex(value.numerator), "denominator_hex": hex(value.denominator)}
    if decimal:
        with localcontext() as context:
            context.prec = 40
            result["decimal_40_significant_digits_approximation"] = format(
                Decimal(value.numerator) / Decimal(value.denominator), ".39E")
    return result


def exact_matvec(matrix, vector, rows, columns=K):
    """Integer dyadic products and additions; no rounded dot product."""
    if len(matrix) != rows * columns or len(vector) != columns:
        raise ValueError("Exact matrix/vector dimensions do not agree")
    support = [(j, a, e) for j, (a, e) in enumerate(vector) if a != 0]
    result = []
    products = 0
    for i in range(rows):
        total, common = 0, 0
        offset = i * columns
        for j, va, ve in support:
            ma, me = matrix[offset + j]
            if ma == 0:
                continue
            integer = ma * va
            exponent = me + ve
            if total == 0:
                total, common = integer, exponent
            elif exponent >= common:
                total += integer << (exponent - common)
            else:
                total = (total << (common - exponent)) + integer
                common = exponent
            products += 1
        result.append(compact((total, common)))
    return result, products


def intermediate(base, derivative, scale):
    return [add(v, multiply(scale, derivative[j])) for j, v in enumerate(base)]


def coordinate(row):
    if row < M:
        return dict(row=row, component="Q", mode=row + 1, frequency=2 * (row + 1))
    if row < K:
        return dict(row=row, component="Pi", mode=row - M + 1, frequency=2 * (row - M + 1))
    return dict(row=row, component="mean", mean_index=row - K)


def norm(values, indices):
    indices = list(indices)
    if not indices:
        return dict(max_abs=rational_json(Fraction(0), True), coordinate=None, all_zero=True)
    row = max(indices, key=lambda i: abs(values[i]))
    return dict(max_abs=rational_json(abs(values[row]), True),
                signed_value=rational_json(values[row], True),
                coordinate=coordinate(row), all_zero=all(values[i] == 0 for i in indices))


def compare_action(local, saved_shape, saved_mean, observed_shape, observed_mean,
                   h, port, sigma, vector):
    """Classical RK4 over the exact saved A_i, including both nonfeedback means."""
    started = time.monotonic()
    stage_inputs = [list(vector)]
    stage_derivatives = []
    product_counts = []
    half_h = compact((h[0], h[1] - 1))
    for index in range(4):
        current = stage_inputs[index]
        image, products = exact_matvec(local[index], current, SIZE)
        stage_derivatives.append(image)
        product_counts.append(products)
        if index == 0:
            stage_inputs.append(intermediate(vector, image, half_h))
        elif index == 1:
            stage_inputs.append(intermediate(vector, image, half_h))
        elif index == 2:
            stage_inputs.append(intermediate(vector, image, h))
    exact_rk = []
    for row in range(SIZE):
        weighted = add(
            add(stage_derivatives[0][row], multiply((2, 0), stage_derivatives[1][row])),
            add(multiply((2, 0), stage_derivatives[2][row]), stage_derivatives[3][row]))
        initial = rational(vector[row]) if row < K else Fraction(0)
        value = initial + rational(multiply(h, weighted)) / 6
        if M <= row < K:
            value /= rational(port)
        exact_rk.append(value)
    old_shape, old_count = exact_matvec(saved_shape, vector, K)
    old_mean, mean_count = exact_matvec(saved_mean, vector, 2)
    current_shape, current_count = exact_matvec(observed_shape, vector, K)
    current_mean, current_mean_count = exact_matvec(observed_mean, vector, 2)
    old_action = [rational(v) for v in old_shape + old_mean]
    current_action = [rational(v) for v in current_shape + current_mean]
    difference = [a - b for a, b in zip(old_action, exact_rk)]
    same_call_difference = [a - b for a, b in zip(current_action, exact_rk)]
    old_minus_current = [a - b for a, b in zip(old_action, current_action)]
    sigma_fraction = rational(sigma)
    sigma_scaled = [v / sigma_fraction for v in difference[:K]]
    sigma_scaled_same_call = [v / sigma_fraction for v in same_call_difference[:K]]
    reference_norm = max(map(abs, exact_rk))
    saved_norm = max(map(abs, old_action))
    diff_norm = max(map(abs, difference))
    shape_reference_norm = max(map(abs, exact_rk[:K]))
    blocks = {}
    for label, indices in (("Q", range(M)), ("Pi", range(M, K)),
                           ("means", range(K, SIZE)), ("complete226", range(SIZE))):
        blocks[label] = dict(
            old_saved_minus_exact_RK=norm(difference, indices),
            same_call_observed_minus_exact_RK=norm(same_call_difference, indices),
            old_saved_minus_same_call_observed=norm(old_minus_current, indices),
            exact_RK=norm(exact_rk, indices),
            old_saved_short_J_and_mean=norm(old_action, indices),
            same_call_observed_short_J_and_mean=norm(current_action, indices))
    return dict(
        stage_input_dyadics=[[pair_json(v) for v in item] for item in stage_inputs],
        stage_derivative_dyadics=[[pair_json(v) for v in item] for item in stage_derivatives],
        exact_RK_output=[rational_json(v) for v in exact_rk],
        exact_original41_short_J_output=[rational_json(v) for v in old_action],
        exact_same_call_observed_short_J_output=[rational_json(v) for v in current_action],
        exact_original41_minus_RK=[rational_json(v) for v in difference],
        exact_same_call_observed_minus_RK=[rational_json(v) for v in same_call_difference],
        exact_original41_minus_same_call_observed=[rational_json(v) for v in old_minus_current],
        exact_difference_decomposition_for_all226=all(
            difference[j] == old_minus_current[j] + same_call_difference[j] for j in range(SIZE)),
        exact_block_norms=blocks,
        global_difference=norm(difference, range(SIZE)),
        same_call_propagation_difference=norm(same_call_difference, range(SIZE)),
        original41_minus_same_call_difference=norm(old_minus_current, range(SIZE)),
        relative_to_exact_RK_norm=(rational_json(diff_norm / reference_norm, True)
                                   if reference_norm != 0 else None),
        relative_to_saved_map_norm=(rational_json(diff_norm / saved_norm, True)
                                    if saved_norm != 0 else None),
        zero_reference_norm=(reference_norm == 0),
        zero_saved_map_norm=(saved_norm == 0),
        exact_equality_on_this_vector=(diff_norm == 0),
        shape_difference=norm(difference, range(K)),
        shape_same_call_propagation_difference=norm(same_call_difference, range(K)),
        shape_difference_over_original_sigma=norm(sigma_scaled, range(K)),
        shape_same_call_propagation_difference_over_original_sigma=norm(
            sigma_scaled_same_call, range(K)),
        shape_relative_to_exact_RK_norm=(
            rational_json(max(map(abs, difference[:K])) / shape_reference_norm, True)
            if shape_reference_norm != 0 else None),
        sigma_applies_to_shape_native_stage_rows_only=True,
        sigma_scaling_is_diagnostic_not_a_new_gate=True,
        executed_scalar_dyadic_products=dict(
            local_stage=product_counts, original41_shape=old_count, original41_mean=mean_count,
            observed_shape=current_count, observed_mean=current_mean_count,
            total=sum(product_counts) + old_count + mean_count + current_count + current_mean_count),
        elapsed_seconds=time.monotonic() - started)


def write_json(directory, name, value, compressed=False):
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                      allow_nan=False) + "\n").encode()
    if compressed:
        raw = gzip.compress(raw, mtime=0)
    path = Path(directory) / name
    with path.open("xb") as stream:
        stream.write(raw)
    return dict(file=name, bytes=len(raw), sha256=digest(raw))


def write_raw(directory, name, raw, shape):
    path = Path(directory) / name
    with path.open("xb") as stream:
        stream.write(raw)
    return dict(file=name, bytes=len(raw), sha256=digest(raw),
                dtype="<f8", order="C", shape=list(shape))


def validate_capture(directory, result_sha):
    directory = Path(directory).resolve()
    result, receipt = read_json(directory / "result.json", result_sha)
    same(result.get("schema"), CAPTURE_RESULT_SCHEMA, "capture result schema")
    same(result.get("capture_completed"), True, "all four original local Jacobians captured")
    same(result.get("actual41_result_sha256"), ACTUAL41_RESULT_SHA, "actual41 source capture")
    same(result.get("actual44_field_receipt_sha256"), ACTUAL44_FIELD_RECEIPT_SHA,
         "actual44 source field receipt")
    summary, summary_receipt = read_json(
        directory / "stage43-local-j-summary.json", result["capture_summary_sha256"])
    for record, label in ((result, "result"), (summary, "summary")):
        for key, expected in (("original_stage", STAGE), ("original_flow_step", STEP),
                              ("new_shooting_stage", NEW_STAGE), ("new_input_node", INPUT_NODE)):
            same(record.get(key), expected, label + " " + key)
        same(record.get("capture_completed"), True, label + " complete capture")
        same(record.get("same_state_path_as_actual41"), True, label + " original field state bytes")
        same(record.get("all_four_geometry_records_equal"), True, label + " original field geometry bits")
    for key in ("original_h", "original_port_ratio", "original_sigma", "reference_arrays",
                "field_reports", "local_J_arrays", "observed_step_arrays", "array_manifest"):
        same(summary.get(key), result.get(key), "summary/result " + key)
    manifest_receipt = result["array_manifest"]
    same(manifest_receipt.get("file"), "stage43-local-j-array-manifest.json", "array manifest file")
    manifest = object_file(directory, manifest_receipt)
    for record, label in ((result, "result"), (summary, "summary"), (manifest, "manifest")):
        for key, name in CAPTURE_RECORD_SOURCE_FIELDS.items():
            same(record.get(key), CAPTURE_SOURCE_PINS[name], label + " source " + key)
        same(record.get("actual41_result_sha256"), ACTUAL41_RESULT_SHA, label + " actual41")
        same(record.get("actual44_field_receipt_sha256"), ACTUAL44_FIELD_RECEIPT_SHA, label + " actual44")
    same(manifest.get("completed"), True, "all local arrays completed")
    same(manifest.get("schema"), CAPTURE_ARRAY_SCHEMA, "local-J array manifest schema")
    entries = manifest.get("arrays")
    if not isinstance(entries, list):
        raise ValueError("The local-J manifest must contain a complete descriptor list")
    by_name = {}
    for entry in entries:
        name = entry.get("name")
        if not isinstance(name, str) or name in by_name:
            raise ValueError("Every captured array must have a unique name")
        by_name[name] = entry
    if not CAPTURE_SOURCE_PINS:
        raise ValueError("The consumer has no frozen capture source pins")
    source_receipts = {}
    for name, expected in CAPTURE_SOURCE_PINS.items():
        path = Path(__file__).resolve().parent / name
        raw = path.read_bytes()
        same(digest(raw), expected, "frozen capture source " + name)
        source_receipts[name] = dict(bytes=len(raw), sha256=expected)
    checked = {}

    def take(descriptor, shape):
        same(by_name.get(descriptor.get("name")), descriptor, "manifest/selected descriptor")
        raw = descriptor_bytes(directory, descriptor, shape)
        checked[descriptor["name"]] = descriptor
        return raw

    fields = summary["field_reports"]
    locals_ = summary["local_J_arrays"]
    if not isinstance(fields, list) or len(fields) != 4 or not isinstance(locals_, list) or len(locals_) != 4:
        raise ValueError("Exactly four original stage-field Jacobians are required")
    matrices = []
    field_state_raw = []
    for index, field in enumerate(fields):
        same(field.get("field_index"), index, "original RK4 field order")
        arrays = field.get("arrays", {})
        same(arrays.get("local_jacobian"), locals_[index], "field/local-J alias")
        state = take(arrays["state"], (SIZE,))
        same(digest(state), field.get("state_float64le_sha256"), "field full state raw SHA")
        take(arrays["derivative"], (SIZE,))
        matrices.append(decode(take(arrays["local_jacobian"], (SIZE, K))))
        field_state_raw.append(state)
    references = summary["reference_arrays"]
    full_input = take(references["full-input"], (SIZE,))
    take(references["full-output"], (SIZE,))
    take(references["shape-output"], (K,))
    shape_raw = take(references["short-J"], (K, K))
    mean_raw = take(references["mean-tangent-rows"], (2, K))
    observed = summary["observed_step_arrays"]
    observed_shape_raw = take(observed["shape_J"], (K, K))
    observed_mean_raw = take(observed["mean_tangent_rows"], (2, K))
    take(observed["full_output"], (SIZE,))
    take(observed["shape_output"], (K,))
    same(take(observed["full_input"], (SIZE,)), full_input, "observed complete initial state")
    same(field_state_raw[0], full_input, "RK field0 and original full input bytes")
    # All remaining manifest entries are hash/finite checked, even when they
    # are not scientific operands of the exact comparison.
    for name, entry in by_name.items():
        if name not in checked:
            descriptor_bytes(directory, entry)
            checked[name] = entry
    h = number_record(summary["original_h"], "original h")
    port = number_record(summary["original_port_ratio"], "original exit port")
    sigma = number_record(summary["original_sigma"], "original old43/new519 residual sigma")
    if rational(h) <= 0 or port[0] == 0 or rational(sigma) <= 0:
        raise ValueError("The recorded step requires positive h/sigma and a nonzero exit port")
    binding = dict(
        capture_result=receipt, capture_summary=summary_receipt,
        array_manifest=manifest_receipt, all_array_descriptors=entries,
        frozen_capture_sources=source_receipts,
        original_h=summary["original_h"], original_port_ratio=summary["original_port_ratio"],
        original_sigma=summary["original_sigma"],
        observed_short_J_matches_original41_bytes=(observed_shape_raw == shape_raw),
        observed_mean_rows_match_original41_bytes=(observed_mean_raw == mean_raw),
        original_stage=STAGE, original_flow_step=STEP,
        new_shooting_stage=NEW_STAGE, new_input_node=INPUT_NODE,
        original_flow_source_sha256=ORIGINAL_FLOW_SHA,
        actual41_result_sha256=ACTUAL41_RESULT_SHA,
        original1372_matrix_identity_sha256=ORIGINAL_MATRIX_SHA,
        exact_operands_are_the_saved_binary64_words=True,
        capture_root_and_J_accuracy_not_certified=True,
        original41_local_A_were_not_independently_saved=True,
        no_native_or_scientific_source_module_imported=True)
    return (matrices, decode(shape_raw), decode(mean_raw),
            decode(observed_shape_raw), decode(observed_mean_raw), h, port, sigma, binding)


def direction_vector(result_path, expected_sha):
    """Read one actual43 best direction by its complete result/raw/checkpoint identity."""
    result_path = Path(result_path).resolve()
    directory = result_path.parent
    report, receipt = read_json(result_path, expected_sha)
    same(report.get("schema"), "native-gauge-original1372-equilibrated-band-correction-v1",
         "actual43 direction result schema")
    same(report.get("source_sha256"), GAUGE_PRODUCER_SHA, "actual43 direction producer")
    same(report.get("gauge_source_sha256"), GAUGE_SOURCE_SHA, "actual43 saved-G source")
    same(report.get("actual_step_result_sha256"), ACTUAL41_RESULT_SHA, "actual43 parent step capture")
    same(report.get("original1372_matrix_identity_sha256"), ORIGINAL_MATRIX_SHA,
         "actual43 original complete finite matrix")
    same(report.get("diagnostic_completed"), True, "actual43 completed diagnostic")
    same(report.get("linear_direction_computed"), True, "actual43 complete direction")
    same(report.get("native_accepted"), False, "the diagnostic is not a native acceptance")
    descriptor = report["step_delta"]
    raw = descriptor_bytes(directory, descriptor, (1373, K))
    selected = report.get("best_iteration")
    history = report.get("refinement_history", [])
    candidates = [item for item in history if item.get("iteration") == selected]
    if len(candidates) != 1:
        raise ValueError("The selected actual direction iteration is ambiguous")
    same(candidates[0]["delta"]["sha256"], descriptor["sha256"], "selected iteration/raw best delta")
    checkpoint_desc = report["step_direction_checkpoint"]
    checkpoint = object_file(directory, checkpoint_desc)
    same(checkpoint.get("schema"), "complete-original1372-direction-from-saved-node-gauge-v1",
         "original-coordinate complete direction checkpoint")
    for key, expected in (("source_sha256", GAUGE_PRODUCER_SHA), ("M", M), ("K", K),
                          ("depth", 1372), ("step_depth", 1372), ("original_depth", 576),
                          ("actual_coordinates_are_original_Q_Pi", True),
                          ("restricted_to_original_nodes", False),
                          ("original1372_matrix_identity_sha256", ORIGINAL_MATRIX_SHA)):
        same(checkpoint.get(key), expected, "complete direction " + key)
    same(checkpoint.get("delta_float64le_sha256"), digest(raw), "checkpoint/full raw direction")
    binding = checkpoint.get("original_input_binding", {})
    same(binding.get("new_matrix_identity_sha256"), ORIGINAL_MATRIX_SHA, "complete original binding")
    same(checkpoint.get("gauge_matrix_identity_sha256"), report.get("formed_gauge_matrix_identity_sha256"),
         "same actual gauge matrix producer")
    same(checkpoint.get("coordinate_identity_sha256"), report.get("coordinate_identity_sha256"),
         "same saved original-coordinate recovery")
    rows = checkpoint.get("rows")
    if not isinstance(rows, list) or len(rows) != 1373:
        raise ValueError("The complete checkpoint must retain all 1373 direction nodes")
    for node, row in enumerate(rows):
        same(row.get("node"), node, "complete checkpoint node order")
        values = row.get("state")
        if not isinstance(values, list) or len(values) != K:
            raise ValueError("Every original-coordinate direction row has 224 components")
        negative_zero = row.get("negative_zero_columns")
        if (not isinstance(negative_zero, list)
                or any(type(j) is not int or j < 0 or j >= K for j in negative_zero)
                or len(set(negative_zero)) != len(negative_zero)):
            raise ValueError("Complete signed-zero column indices are required")
        negative_zero = set(negative_zero)
        reconstructed = bytearray()
        for j, value in enumerate(values):
            if type(value) not in (int, float) or not math.isfinite(value):
                raise ValueError("Nonfinite checkpoint component")
            if j in negative_zero:
                if value != 0:
                    raise ValueError("A negative-zero index points to a nonzero component")
                word = struct.pack("<Q", 1 << 63)
            else:
                word = struct.pack("<d", value)
                if word == struct.pack("<Q", 1 << 63):
                    raise ValueError("An unlisted negative-zero component")
            reconstructed.extend(word)
        same(bytes(reconstructed), raw[node * K * 8:(node + 1) * K * 8],
             "complete checkpoint/raw row bits")
    row_raw = raw[INPUT_NODE * K * 8:(INPUT_NODE + 1) * K * 8]
    provenance = dict(
        kind="actual43-best-original-Q-Pi-direction-at-incoming-node520",
        complete_result=receipt, raw_delta=descriptor, checkpoint=checkpoint_desc,
        selected_iteration=selected, step_expanded_input_node=INPUT_NODE,
        coordinate_system="original Q/Pi, in the 1373-node step-expanded indexing",
        original_matrix_sha256=ORIGINAL_MATRIX_SHA,
        actual41_result_sha256=ACTUAL41_RESULT_SHA,
        source_sha256=GAUGE_PRODUCER_SHA,
        full_checkpoint_rows_checked=1373,
        row_float64le_sha256=digest(row_raw),
        no_direction_rescaling_or_thresholding=True,
        no_claim_that_the_direction_solves_the_original_system=True)
    return row_raw, provenance


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture-directory", type=Path, required=True)
    parser.add_argument("--capture-result-sha256", required=True)
    parser.add_argument("--direction-result", type=Path)
    parser.add_argument("--direction-result-sha256")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    actions_only()
    require_sha(args.capture_result_sha256, "actual local-J capture result")
    if (args.direction_result is None) != (args.direction_result_sha256 is None):
        parser.error("The actual direction result and its complete SHA256 must be supplied together")
    if args.direction_result_sha256 is not None:
        require_sha(args.direction_result_sha256, "actual43 direction result")
    args.out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    source_raw = Path(__file__).read_bytes()
    report = dict(
        schema="saved-four-local-J-exact-rational-RK4-action-v1",
        source_sha256=digest(source_raw), completed=False,
        repository=os.environ.get("GITHUB_REPOSITORY"),
        run_id=os.environ.get("GITHUB_RUN_ID"), run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        python=sys.version, arithmetic="Exact decoded dyadic integer products; Fraction only for /6, exit port, and reporting",
        cases=[], new_root_calls=0, new_local_J_calls=0, new_ODE_steps=0,
        native_solves=0, nonlinear_trials=0, native_accepted=False, task_completed=False,
        thresholded_input_components=0, omitted_modes=0,
        original_J_accuracy_or_true_DF_error_certified=False,
        no_new_acceptance_gate=True)
    try:
        (local, saved_shape, saved_mean, observed_shape, observed_mean,
         h, port, sigma, binding) = validate_capture(
            args.capture_directory, args.capture_result_sha256)
        report["input_binding"] = write_json(args.out, "input-binding.json", binding)
        vectors = []
        for label, column in (("highest-mode-Q112", M - 1), ("highest-mode-Pi112", K - 1)):
            raw = bytearray(K * 8)
            raw[column * 8:(column + 1) * 8] = struct.pack("<d", 1.0)
            vectors.append((label, bytes(raw), dict(
                kind="exact-unit-basis", column=column, mode=M, frequency=2 * M,
                mean_input=(0, 0), all_224_shape_components_retained=True)))
        if args.direction_result is not None:
            raw, provenance = direction_vector(args.direction_result, args.direction_result_sha256)
            vectors.append(("actual43-best-node520", raw, provenance))
        for index, (label, raw, provenance) in enumerate(vectors):
            print(json.dumps(dict(event="exact_single_step_action_started", case=label)), flush=True)
            input_file = write_raw(args.out, f"case-{index:02d}-input.f64le", raw, (K,))
            result = compare_action(local, saved_shape, saved_mean, observed_shape, observed_mean,
                                    h, port, sigma, decode(raw))
            payload = dict(
                schema="saved-four-local-J-exact-rational-case-v1",
                label=label, provenance=provenance, input_vector=input_file,
                source_sha256=report["source_sha256"], input_binding=report["input_binding"],
                sign_convention="original41 or same-call observed short-J action minus rational RK4 action",
                original41_vs_same_call_and_given_local_A_rounding_are_separate=True,
                shape_columns=K, full_output_rows=SIZE, nonfeedback_mean_input_zero=True,
                means_are_not_scaled_by_exit_port=True,
                port_is_applied_only_to_final_Pi_shape_rows=True, **result)
            case_file = write_json(args.out, f"case-{index:02d}-exact-action.json.gz",
                                   payload, compressed=True)
            item = dict(
                label=label, exact_action=case_file, input_vector=input_file,
                global_difference=result["global_difference"],
                same_call_propagation_difference=result["same_call_propagation_difference"],
                original41_minus_same_call_difference=result["original41_minus_same_call_difference"],
                shape_difference_over_original_sigma=result["shape_difference_over_original_sigma"],
                shape_same_call_propagation_difference_over_original_sigma=
                    result["shape_same_call_propagation_difference_over_original_sigma"],
                shape_difference=result["shape_difference"],
                shape_relative_to_exact_RK_norm=result["shape_relative_to_exact_RK_norm"],
                relative_to_exact_RK_norm=result["relative_to_exact_RK_norm"],
                relative_to_saved_map_norm=result["relative_to_saved_map_norm"],
                exact_equality_on_this_vector=result["exact_equality_on_this_vector"],
                executed_scalar_dyadic_products=result["executed_scalar_dyadic_products"],
                elapsed_seconds=result["elapsed_seconds"])
            report["cases"].append(item)
            print(json.dumps(dict(
                event="exact_single_step_action_finished", case=label,
                exact_equality=item["exact_equality_on_this_vector"],
                difference=item["global_difference"], case_file=case_file)), flush=True)
        report["completed"] = True
    except Exception as error:
        report["actual_error"] = repr(error)
        trace = traceback.format_exc()
        raw = trace.encode()
        with (args.out / "failure-traceback.txt").open("xb") as stream:
            stream.write(raw)
        report["failure_traceback"] = dict(file="failure-traceback.txt", bytes=len(raw), sha256=digest(raw))
    finally:
        report["elapsed_seconds"] = time.monotonic() - started
        report["maximum_RSS_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        full_result = write_json(args.out, "result.json.gz", report, compressed=True)
        summary = dict(report, full_result=full_result)
        encoded = json.dumps(summary, allow_nan=False).encode()
        if len(encoded) >= 90000:
            summary["cases"] = [{key: item[key] for key in (
                "label", "exact_action", "input_vector", "exact_equality_on_this_vector",
                "executed_scalar_dyadic_products", "elapsed_seconds")} for item in report["cases"]]
            summary["full_exact_rationals_in_case_files"] = True
        summary_file = write_json(args.out, "summary.json", summary)
        print(json.dumps(dict(event="exact_single_step_action_complete",
                              completed=report["completed"], summary=summary_file,
                              native_accepted=False, task_completed=False)), flush=True)
    return 0 if report["completed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
