#!/usr/bin/env python3
"""Complete rational RK4 reference for the four original local A arrays saved in actual47.

Scientific execution is restricted to this public repository's GitHub Actions.
This program calls no RHS, root, Jacobian producer, ODE integrator, native solver,
or nonlinear trial.  The finite input words define the reference object.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import resource
import struct
import sys
import time
import traceback

PUBLIC_REPOSITORY = "Rogerhu12/math-research-public"
M, K, SIZE = 112, 224, 226
CAPTURE_SHA = "da9715ef1685c04210d5c3d8bbfb40629fd4bf810455b497e5e25630ac0aa403"
PRIOR_EXACT_SHA = "f145cf0efea702964413abf5490df5f2ef584b373afb9b8213f001774e9ea33b"
READER_NAME = "exact_20261114_single_step_rational_action.py"
READER_SHA = "9c42982291bd1a7b7cf21c472d8aae877136fb884708a8310ca6bb882c1d103e"
CANDIDATE_NAME = "geometry_20261114_saved_stage_rk_covariance.py"
CANDIDATE_SCHEMA = "saved-four-local-A-R271-frequency-balanced-RK4-candidates-v1"
CANDIDATE_ARRAY_SCHEMA = "saved-four-local-A-R271-working-arrays-v1"
CANDIDATE_KEYS = ("r271-frequency-balanced-longdouble",
                  "direct-original-coordinates-longdouble")
LABELS = ("highest-mode-Q112", "highest-mode-Pi112", "actual43-best-node520")
E = None


def actions_only():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != PUBLIC_REPOSITORY):
        raise RuntimeError("Scientific execution is restricted to this public repository's Actions")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def load_reader():
    global E
    path = Path(__file__).resolve().parent / READER_NAME
    raw = path.read_bytes()
    if digest(raw) != READER_SHA:
        raise ValueError("The frozen actual47 exact reader does not match its source SHA256")
    spec = importlib.util.spec_from_file_location("_visible_actual47_exact_reader", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    E = module
    return dict(file=READER_NAME, bytes=len(raw), sha256=READER_SHA)


def fraction_record(record):
    if not isinstance(record, dict):
        raise ValueError("An exact fraction record is required")
    p, q = record.get("numerator_hex"), record.get("denominator_hex")
    if not isinstance(p, str) or not isinstance(q, str):
        raise ValueError("Exact fraction numerators and denominators must be hexadecimal strings")
    numerator, denominator = int(p, 16), int(q, 16)
    if denominator <= 0 or hex(numerator) != p or hex(denominator) != q:
        raise ValueError("Noncanonical exact fraction record")
    return Fraction(numerator, denominator)


def receipts_file(directory, relative):
    path = E.safe_file(directory, relative)
    raw = path.read_bytes()
    return dict(file=relative, bytes=len(raw), sha256=digest(raw))


def load_prior_actions(directory, expected_sha, current_binding, output):
    """Bind the three saved actual47 inputs without downloading actual43 again."""
    E.same(expected_sha, PRIOR_EXACT_SHA, "fixed actual47 three-action result")
    report, receipt = E.read_json(Path(directory) / "result.json.gz", expected_sha)
    E.same(report.get("schema"), "saved-four-local-J-exact-rational-RK4-action-v1",
           "prior action result schema")
    E.same(report.get("source_sha256"), READER_SHA, "prior action producer")
    E.same(report.get("completed"), True, "all three actual47 actions completed")
    E.same(report.get("native_accepted"), False, "prior actions remain diagnostics")
    binding = E.object_file(directory, report["input_binding"])
    E.same(binding, current_binding, "the prior action and current capture operand identity")
    items = report.get("cases")
    if not isinstance(items, list) or len(items) != 3:
        raise ValueError("Exactly the three actual47 cases are required")
    vectors = []
    receipts = []
    for index, item in enumerate(items):
        E.same(item.get("label"), LABELS[index], "prior exact action order")
        case = E.object_file(directory, item["exact_action"])
        E.same(case.get("schema"), "saved-four-local-J-exact-rational-case-v1",
               "prior exact case schema")
        E.same(case.get("source_sha256"), READER_SHA, "prior exact case producer")
        E.same(case.get("label"), LABELS[index], "prior exact case label")
        E.same(case.get("input_binding"), report["input_binding"], "prior exact case binding")
        E.same(case.get("input_vector"), item["input_vector"], "prior input descriptor alias")
        raw = E.descriptor_bytes(directory, item["input_vector"], (K,))
        if index < 2:
            basis_raw = bytearray(K * 8)
            column = M - 1 if index == 0 else K - 1
            basis_raw[column * 8:(column + 1) * 8] = struct.pack("<Q", 0x3ff0000000000000)
            E.same(raw, bytes(basis_raw), "actual47 exact unit input bytes")
        else:
            provenance = case.get("provenance", {})
            E.same(provenance.get("kind"),
                   "actual43-best-original-Q-Pi-direction-at-incoming-node520",
                   "actual43 original-coordinate direction identity")
            E.same(provenance.get("step_expanded_input_node"), 520, "actual43 input node")
            E.same(provenance.get("original_matrix_sha256"), E.ORIGINAL_MATRIX_SHA,
                   "actual43 original1372 matrix")
            E.same(provenance.get("source_sha256"), E.GAUGE_PRODUCER_SHA,
                   "actual43 direction producer")
            E.same(provenance.get("row_float64le_sha256"), digest(raw),
                   "actual43 row bytes retained by actual47")
        saved_outputs = {}
        for name in ("exact_RK_output", "exact_original41_short_J_output",
                     "exact_same_call_observed_short_J_output"):
            rows = case.get(name)
            if not isinstance(rows, list) or len(rows) != SIZE:
                raise ValueError("Every previous exact action must retain 226 outputs")
            saved_outputs[name] = [fraction_record(value) for value in rows]
        copied = E.write_raw(output, f"large-arrays/input-{index:02d}.f64le", raw, (K,))
        vectors.append(dict(
            label=LABELS[index], raw=raw, dyadic=E.decode(raw),
            rational=[E.rational(v) for v in E.decode(raw)],
            input_vector=copied, provenance=case["provenance"], prior_outputs=saved_outputs))
        receipts.append(dict(label=LABELS[index], prior_case=item["exact_action"],
                             prior_input=item["input_vector"], copied_input=copied,
                             provenance=case["provenance"]))
    return vectors, dict(
        result=receipt, input_binding=report["input_binding"], cases=receipts,
        no_actual43_redownload=True,
        actual43_input_is_bound_through_completed_actual47_case=True)


def checked_any_raw(directory, descriptor):
    """Hash all candidate work arrays, preserving their explicitly different dtypes."""
    if not isinstance(descriptor, dict):
        raise ValueError("A complete candidate work-array descriptor is required")
    relative = descriptor.get("file")
    path = E.safe_file(directory, relative)
    raw = path.read_bytes()
    E.same(len(raw), descriptor["bytes"], "candidate complete work-array bytes")
    E.same(digest(raw), E.require_sha(descriptor["sha256"], relative),
           "candidate complete work-array SHA")
    if not isinstance(descriptor.get("dtype"), str):
        raise ValueError("Every candidate work array must declare its dtype")
    if not isinstance(descriptor.get("shape"), list):
        raise ValueError("Every candidate work array must declare its full shape")
    return raw


def load_candidate(directory, result_sha, expected_source_sha, capture_binding, output):
    """Only the final original-coordinate <f8 maps are mathematical operands."""
    E.require_sha(expected_source_sha, "candidate source")
    source_path = Path(__file__).resolve().parent / CANDIDATE_NAME
    source_raw = source_path.read_bytes()
    E.same(digest(source_raw), expected_source_sha, "candidate source bytes")
    result, receipt = E.read_json(Path(directory) / "result.json", result_sha)
    E.same(result.get("schema"), CANDIDATE_SCHEMA, "candidate result schema")
    E.same(result.get("completed"), True, "complete candidate matrix formation")
    E.same(result.get("source_sha256"), expected_source_sha, "candidate producer")
    E.same(result.get("capture_result_sha256"), CAPTURE_SHA, "candidate actual47 capture")
    E.same(result.get("original_h"), capture_binding["original_h"], "candidate original h bits")
    E.same(result.get("original_port_ratio"), capture_binding["original_port_ratio"],
           "candidate original exit port bits")
    bound = E.object_file(directory, result["input_binding"])
    for key, expected in capture_binding.items():
        E.same(bound.get(key), expected, "candidate shared capture binding " + key)
    manifest = E.object_file(directory, result["array_manifest"])
    E.same(manifest.get("schema"), CANDIDATE_ARRAY_SCHEMA, "candidate work-array manifest")
    E.same(manifest.get("source_sha256"), expected_source_sha, "candidate manifest producer")
    E.same(manifest.get("capture_result_sha256"), CAPTURE_SHA, "candidate manifest capture")
    E.same(manifest.get("completed"), True, "candidate manifest complete")
    entries = manifest.get("arrays")
    if not isinstance(entries, list):
        raise ValueError("The candidate manifest must contain a descriptor list")
    by_name = {}
    checked = []
    for descriptor in entries:
        name = descriptor.get("name")
        if not isinstance(name, str) or name in by_name:
            raise ValueError("Candidate array names must be unique")
        by_name[name] = descriptor
        checked_any_raw(directory, descriptor)
        checked.append(descriptor)
    outputs = result.get("candidate_maps")
    if not isinstance(outputs, dict) or set(outputs) != set(CANDIDATE_KEYS):
        raise ValueError("Both explicitly named full original-coordinate candidate maps are required")
    maps = {}
    copied = {}
    for index, name in enumerate(CANDIDATE_KEYS):
        descriptor = outputs[name]
        E.same(by_name.get(descriptor.get("name")), descriptor, "candidate map manifest alias")
        raw = E.descriptor_bytes(directory, descriptor, (SIZE, K))
        maps[name] = raw
        copied[name] = E.write_raw(
            output, f"large-arrays/candidate-{index:02d}-full-original.f64le", raw, (SIZE, K))
    E.same(result.get("full_original_output"), outputs[CANDIDATE_KEYS[0]],
           "main full-output candidate alias")
    # Validate the explicitly published main shape/mean split against the same raw map.
    for key, shape, section in (
            ("shape_J", (K, K), maps[CANDIDATE_KEYS[0]][:K * K * 8]),
            ("mean_rows", (2, K), maps[CANDIDATE_KEYS[0]][K * K * 8:])):
        descriptor = result.get(key)
        E.same(by_name.get(descriptor.get("name")), descriptor, "main split descriptor alias")
        E.same(E.descriptor_bytes(directory, descriptor, shape), section,
               "main candidate shape/mean slices are the exact full-map bytes")
    return maps, dict(
        result=receipt, input_binding=result["input_binding"],
        array_manifest=result["array_manifest"],
        source=dict(file=CANDIDATE_NAME, bytes=len(source_raw), sha256=expected_source_sha),
        candidate_maps=outputs, copied_candidate_maps=copied,
        all_work_arrays_hash_checked=checked,
        longdouble_work_arrays_not_reinterpreted_as_binary64=True,
        mathematical_operands_are_final_original_coordinate_binary64_maps=True)


def exact_rk_column(local, h, port, column):
    """The same finite four-A recursion as 9c429, with a complete unit input."""
    vector = [(0, 0) for _ in range(K)]
    vector[column] = (1, 0)
    current = vector
    derivatives = []
    product_counts = []
    half_h = E.compact((h[0], h[1] - 1))
    for index in range(4):
        image, products = E.exact_matvec(local[index], current, SIZE)
        derivatives.append(image)
        product_counts.append(products)
        if index in (0, 1):
            current = E.intermediate(vector, image, half_h)
        elif index == 2:
            current = E.intermediate(vector, image, h)
    output = []
    port_fraction = E.rational(port)
    for row in range(SIZE):
        weighted = E.add(
            E.add(derivatives[0][row], E.multiply((2, 0), derivatives[1][row])),
            E.add(E.multiply((2, 0), derivatives[2][row]), derivatives[3][row]))
        initial = Fraction(1 if row == column else 0)
        value = initial + E.rational(E.multiply(h, weighted)) / 6
        if M <= row < K:
            value /= port_fraction
        output.append(value)
    return output, product_counts


def nearest_even_integer(numerator, denominator):
    quotient, remainder = divmod(numerator, denominator)
    doubled = remainder << 1
    tie = doubled == denominator
    increment = doubled > denominator or (tie and quotient & 1)
    return quotient + int(bool(increment)), tie


def rational_to_binary64_word(value):
    """Exact round-to-nearest, ties-to-even, by integer quotient/remainder.

    No float conversion, Decimal approximation, or longdouble cast participates.
    Exact zero is +0; a nonzero negative input rounded to zero yields -0.
    """
    if value == 0:
        return 0, dict(classification="positive-zero", exact_zero=True,
                       tie=False, unit_power=-1074)
    sign = (1 << 63) if value < 0 else 0
    numerator, denominator = abs(value.numerator), value.denominator
    exponent = numerator.bit_length() - denominator.bit_length()
    if exponent >= 0:
        if numerator < (denominator << exponent):
            exponent -= 1
    elif (numerator << -exponent) < denominator:
        exponent -= 1
    if exponent > 1023:
        return sign | (2047 << 52), dict(
            classification="infinity", exact_zero=False, tie=False,
            unit_power=exponent - 52, overflow=True)
    if exponent < -1022:
        mantissa, tie = nearest_even_integer(numerator << 1074, denominator)
        if mantissa > (1 << 52):
            raise ArithmeticError("Subnormal quantization exceeded its possible carry")
        if mantissa == (1 << 52):
            word = sign | (1 << 52)
            classification = "normal"
        else:
            word = sign | mantissa
            classification = ("negative-zero" if sign else "positive-zero") if mantissa == 0 else "subnormal"
        return word, dict(classification=classification, exact_zero=False,
                          tie=tie, unit_power=-1074, overflow=False)
    unit_power = exponent - 52
    if unit_power <= 0:
        mantissa, tie = nearest_even_integer(numerator << -unit_power, denominator)
    else:
        mantissa, tie = nearest_even_integer(numerator, denominator << unit_power)
    if not ((1 << 52) <= mantissa <= (1 << 53)):
        raise ArithmeticError("Normal quantization produced an impossible significand")
    if mantissa == (1 << 53):
        mantissa >>= 1
        exponent += 1
    if exponent > 1023:
        return sign | (2047 << 52), dict(
            classification="infinity", exact_zero=False, tie=tie,
            unit_power=unit_power, overflow=True)
    word = sign | ((exponent + 1023) << 52) | (mantissa - (1 << 52))
    return word, dict(classification="normal", exact_zero=False, tie=tie,
                      unit_power=unit_power, overflow=False)


def word_fraction(word):
    return E.rational(E.from_word(word))


def word_is_finite(word):
    return ((word >> 52) & 2047) != 2047


def matrix_coordinate(row, column):
    return dict(output=E.coordinate(row), input=E.coordinate(column))


class MatrixStatistics:
    """Exact element, squared Frobenius, and induced infinity norms."""
    def __init__(self):
        self.max_abs = Fraction(0)
        self.max_value = Fraction(0)
        self.max_index = (0, 0)
        self.row_sums = [Fraction(0) for _ in range(SIZE)]
        self.squared = {"Q": Fraction(0), "Pi": Fraction(0), "means": Fraction(0)}
        self.nonzero = 0
        self.entries = 0

    def add(self, value, row, column):
        absolute = abs(value)
        if absolute > self.max_abs:
            self.max_abs, self.max_value, self.max_index = absolute, value, (row, column)
        self.row_sums[row] += absolute
        block = "Q" if row < M else ("Pi" if row < K else "means")
        self.squared[block] += value * value
        self.nonzero += int(value != 0)
        self.entries += 1

    def report(self):
        row = max(range(SIZE), key=self.row_sums.__getitem__)
        shape_row = max(range(K), key=self.row_sums.__getitem__)
        mean_row = max(range(K, SIZE), key=self.row_sums.__getitem__)
        return dict(
            full_shape=[SIZE, K], entries=self.entries, nonzero_entries=self.nonzero,
            all_zero=(self.nonzero == 0),
            maximum_absolute_entry=E.rational_json(self.max_abs, True),
            signed_entry_at_maximum=E.rational_json(self.max_value, True),
            maximum_entry_coordinate=matrix_coordinate(*self.max_index),
            squared_Frobenius_norm=E.rational_json(sum(self.squared.values(), Fraction(0)), True),
            squared_Frobenius_by_output_block={
                name: E.rational_json(value, True) for name, value in self.squared.items()},
            induced_infinity_norm=E.rational_json(self.row_sums[row], True),
            induced_infinity_row=E.coordinate(row),
            shape_induced_infinity_norm=E.rational_json(self.row_sums[shape_row], True),
            shape_induced_infinity_row=E.coordinate(shape_row),
            mean_induced_infinity_norm=E.rational_json(self.row_sums[mean_row], True),
            mean_induced_infinity_row=E.coordinate(mean_row))


def file_receipt(directory, relative):
    path = Path(directory) / relative
    hashed = hashlib.sha256()
    length = 0
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            hashed.update(block)
            length += len(block)
    return dict(file=relative, bytes=length, sha256=hashed.hexdigest())


def write_rational_matrix(directory, relative, rows, role):
    """One complete 226x224 matrix per gzip; no API-driven chunking."""
    path = Path(directory) / relative
    header = dict(schema="complete-rational-matrix-hex-v1", shape=[SIZE, K], order="C",
                  scalar_representation="reduced numerator_hex / positive denominator_hex",
                  role=role)
    prefix = json.dumps(header, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    with path.open("xb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as zipped:
            zipped.write(prefix[:-1] + b',"rows":[')
            count = 0
            for index, values in enumerate(rows):
                if len(values) != K:
                    raise ValueError("A full rational matrix row must have all 224 columns")
                if index:
                    zipped.write(b",")
                record = [E.rational_json(value) for value in values]
                zipped.write(json.dumps(record, sort_keys=True, separators=(",", ":"),
                                        allow_nan=False).encode())
                count += 1
            if count != SIZE:
                raise ValueError("A full rational matrix must retain all 226 output rows")
            zipped.write(b"]}\n")
    return dict(**file_receipt(directory, relative), shape=[SIZE, K], order="C",
                representation="complete-rational-matrix-hex-v1", role=role)


def matrix_action(matrix, vector):
    """Exact action of an already formed rational matrix; no new A calls."""
    return [sum((a * b for a, b in zip(row, vector)), Fraction(0)) for row in matrix]


def raw_to_matrix(raw):
    values = [E.rational(value) for value in E.decode(raw)]
    if len(values) != SIZE * K:
        raise ValueError("A complete original-coordinate map must have 226x224 entries")
    return [values[row * K:(row + 1) * K] for row in range(SIZE)]


def stats_and_difference(output, name, matrix, reference, reference_statistics, rn_raw=None):
    stats = MatrixStatistics()

    def rows():
        for row in range(SIZE):
            current = []
            for column in range(K):
                difference = matrix[row][column] - reference[row][column]
                stats.add(difference, row, column)
                current.append(difference)
            yield current
    safe_name = name.replace("_", "-")
    descriptor = write_rational_matrix(
        output, "large-arrays/" + safe_name + "-minus-exact.json.gz", rows(),
        name + " minus the same exact four-A RK4 reference, original coordinates")
    result = dict(exact_difference_matrix=descriptor, **stats.report())
    denominator = fraction_record(reference_statistics["induced_infinity_norm"])
    result["relative_induced_infinity_difference"] = (
        E.rational_json(max(stats.row_sums) / denominator, True) if denominator else None)
    if rn_raw is not None:
        result["comparison_with_correctly_rounded_reference_is_separate"] = True
    return result


def reduced_summary(value):
    """Keep public summary small; complete exact rational operands stay in result.gz."""
    if isinstance(value, dict):
        if "numerator_hex" in value and "denominator_hex" in value:
            return {"decimal_40_significant_digits_approximation":
                    value.get("decimal_40_significant_digits_approximation"),
                    "complete_exact_fraction_is_in_result_or_matrix_file": True}
        return {key: reduced_summary(item) for key, item in value.items()
                if key not in ("all_work_arrays_hash_checked", "all_array_descriptors",
                               "provenance", "exact_source_bindings", "per_column_products")}
    if isinstance(value, list):
        return [reduced_summary(item) for item in value]
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture-directory", type=Path, required=True)
    parser.add_argument("--capture-result-sha256", required=True)
    parser.add_argument("--prior-exact-directory", type=Path, required=True)
    parser.add_argument("--prior-exact-result-sha256", required=True)
    parser.add_argument("--candidate-directory", type=Path)
    parser.add_argument("--candidate-result-sha256")
    parser.add_argument("--expected-candidate-source-sha256")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    actions_only()
    candidate_arguments = (args.candidate_directory, args.candidate_result_sha256,
                           args.expected_candidate_source_sha256)
    if any(value is None for value in candidate_arguments) and not all(
            value is None for value in candidate_arguments):
        parser.error("Candidate directory, result SHA, and expected producer SHA must be supplied together")
    args.out.mkdir(parents=True, exist_ok=False)
    (args.out / "large-arrays").mkdir()
    started = time.monotonic()
    source_raw = Path(__file__).read_bytes()
    report = dict(
        schema="saved-actual47-full-rational-RK4-reference-and-candidate-comparison-v1",
        source_sha256=digest(source_raw), completed=False,
        repository=os.environ.get("GITHUB_REPOSITORY"),
        run_id=os.environ.get("GITHUB_RUN_ID"), run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        python=sys.version, input_columns=K, output_rows=SIZE, shape_rows=K, mean_rows=2,
        new_root_calls=0, new_RHS_calls=0, new_local_J_calls=0, new_ODE_steps=0,
        native_solves=0, nonlinear_trials=0, omitted_modes=0, thresholded_components=0,
        means_feedback_to_local_A=False, final_port_applies_only_to_Pi_rows=True,
        exact_zero_rounds_to_positive_zero=True,
        nonzero_negative_underflow_retains_negative_zero=True,
        correct_RN_is_a_new_explicit_matrix_identity=True,
        no_new_acceptance_gate=True, native_accepted=False, task_completed=False,
        true_DF_or_original_local_J_accuracy_certified=False,
        current_actual43_direction_effectiveness_claimed=False,
        scientific_scope="The complete finite four-saved-A RK4 linear map, not a new ODE flow",
        cases=[], map_comparisons={}, completed_reference_columns=0)
    try:
        report["exact_reader_source"] = load_reader()
        E.same(args.capture_result_sha256, CAPTURE_SHA, "fixed actual47 capture result")
        E.same(args.prior_exact_result_sha256, PRIOR_EXACT_SHA, "fixed actual47 action result")
        (local, old_shape, old_mean, obs_shape, obs_mean,
         h, port, sigma, capture_binding) = E.validate_capture(
            args.capture_directory, args.capture_result_sha256)
        capture, _ = E.read_json(Path(args.capture_directory) / "result.json", CAPTURE_SHA)
        vectors, prior_binding = load_prior_actions(
            args.prior_exact_directory, args.prior_exact_result_sha256, capture_binding, args.out)
        refs = capture["reference_arrays"]
        obs = capture["observed_step_arrays"]
        maps_raw = {
            "original41": E.descriptor_bytes(args.capture_directory, refs["short-J"], (K, K))
                + E.descriptor_bytes(args.capture_directory, refs["mean-tangent-rows"], (2, K)),
            "same-call-observed": E.descriptor_bytes(args.capture_directory, obs["shape_J"], (K, K))
                + E.descriptor_bytes(args.capture_directory, obs["mean_tangent_rows"], (2, K))}
        map_descriptors = {}
        for name, raw in maps_raw.items():
            map_descriptors[name] = E.write_raw(
                args.out, "large-arrays/" + name + "-full-original.f64le", raw, (SIZE, K))
        candidate_binding = None
        if args.candidate_directory is not None:
            candidates, candidate_binding = load_candidate(
                args.candidate_directory, args.candidate_result_sha256,
                args.expected_candidate_source_sha256, capture_binding, args.out)
            maps_raw.update(candidates)
            map_descriptors.update(candidate_binding["copied_candidate_maps"])
        full_binding = dict(
            capture=capture_binding, prior_actions=prior_binding, candidate=candidate_binding,
            exact_reader_source=report["exact_reader_source"], producer_sha256=report["source_sha256"],
            all_original_modes_and_mean_rows_retained=True,
            candidate_longdouble_work_only_byte_checked=True)
        report["input_binding"] = E.write_json(args.out, "input-binding.json", full_binding)
        report["original_h"] = capture_binding["original_h"]
        report["original_port_ratio"] = capture_binding["original_port_ratio"]
        report["original_sigma"] = capture_binding["original_sigma"]
        report["input_maps"] = map_descriptors
        report["old_and_observed_full_matrix_bytes_equal"] = (
            maps_raw["original41"] == maps_raw["same-call-observed"])
        reference = [[Fraction(0) for _ in range(K)] for _ in range(SIZE)]
        rn_raw = bytearray(SIZE * K * 8)
        rounding_counts = dict(elements=0, exact_values=0, inexact_values=0,
                               ties=0, normal=0, subnormal=0,
                               positive_zero=0, negative_zero=0, infinity=0)
        report["per_column_products"] = []
        reference_stats = MatrixStatistics()
        for column in range(K):
            column_started = time.monotonic()
            values, products = exact_rk_column(local, h, port, column)
            for row, value in enumerate(values):
                reference[row][column] = value
                reference_stats.add(value, row, column)
                word, metadata = rational_to_binary64_word(value)
                struct.pack_into("<Q", rn_raw, 8 * (row * K + column), word)
                rounding_counts["elements"] += 1
                rounding_counts["ties"] += int(metadata["tie"])
                rounding_counts[metadata["classification"].replace("-", "_")] += 1
                if word_is_finite(word) and word_fraction(word) == value:
                    rounding_counts["exact_values"] += 1
                else:
                    rounding_counts["inexact_values"] += 1
            report["completed_reference_columns"] = column + 1
            report["per_column_products"].append(dict(column=column, local_stages=products))
            if column == 0 or (column + 1) % 16 == 0 or column + 1 == K:
                print(json.dumps(dict(event="complete_rational_reference_progress",
                                      completed_columns=column + 1, total_columns=K,
                                      elapsed_seconds=time.monotonic() - started,
                                      current_column_seconds=time.monotonic() - column_started)),
                      flush=True)
        report["reference_statistics"] = reference_stats.report()
        report["exact_reference"] = write_rational_matrix(
            args.out, "large-arrays/complete-exact-reference.json.gz", reference,
            "All 226x224 exact rational elements of the same saved four-A RK4 map")
        rn_raw = bytes(rn_raw)
        report["correctly_rounded_reference"] = E.write_raw(
            args.out, "large-arrays/complete-reference-RN.f64le", rn_raw, (SIZE, K))
        report["correct_rounding"] = dict(
            algorithm="Exact integer quotient/remainder; round nearest, ties even; gradual underflow",
            decimal_or_float_conversion_used=False, counts=rounding_counts,
            full_exact_elements_and_binary64_words_allow_independent_rounding_verification=True,
            finite=(rounding_counts["infinity"] == 0),
            rounding_loss_recorded_separately_from_original_propagation_difference=True)
        matrices = {name: raw_to_matrix(raw) for name, raw in maps_raw.items()}
        if rounding_counts["infinity"] == 0:
            matrices["correct-RN-reference"] = raw_to_matrix(rn_raw)
            report["map_comparisons"]["correct-RN-reference"] = stats_and_difference(
                args.out, "correct-RN-reference", matrices["correct-RN-reference"],
                reference, report["reference_statistics"])
        else:
            report["correct_rounding"]["nonfinite_RN_actions_not_formed"] = True
        for name in maps_raw:
            result = stats_and_difference(
                args.out, name, matrices[name], reference, report["reference_statistics"], rn_raw)
            result["bitwise_elements_different_from_correct_RN"] = sum(
                a != b for (a,), (b,) in zip(struct.iter_unpack("<Q", maps_raw[name]),
                                           struct.iter_unpack("<Q", rn_raw)))
            result["bitwise_count_includes_the_sign_of_zero"] = True
            report["map_comparisons"][name] = result
        sigma_fraction = E.rational(sigma)
        for index, vector in enumerate(vectors):
            exact_action = matrix_action(reference, vector["rational"])
            old_prior = vector["prior_outputs"]
            case = dict(
                schema="complete-saved-four-A-reference-direction-v1", label=vector["label"],
                input_vector=vector["input_vector"], provenance=vector["provenance"],
                input_binding=report["input_binding"],
                exact_reference_action=[E.rational_json(value) for value in exact_action],
                reference_action_matches_actual47_exact_case=(
                    exact_action == old_prior["exact_RK_output"]),
                input_vector_unchanged=True, maps={}, scope="Linear action; not a nonlinear trial")
            short_maps = {}
            reference_norm = max(map(abs, exact_action))
            for name, matrix in matrices.items():
                output = matrix_action(matrix, vector["rational"])
                difference = [a - b for a, b in zip(output, exact_action)]
                item = dict(
                    exact_action=[E.rational_json(value) for value in output],
                    exact_minus_rational_reference=[E.rational_json(value) for value in difference],
                    complete226_difference=E.norm(difference, range(SIZE)),
                    shape_difference=E.norm(difference, range(K)),
                    mean_difference=E.norm(difference, range(K, SIZE)),
                    shape_difference_over_original_sigma=E.norm(
                        [value / sigma_fraction for value in difference[:K]], range(K)),
                    relative_to_exact_reference_norm=(
                        E.rational_json(max(map(abs, difference)) / reference_norm, True)
                        if reference_norm else None))
                if name == "original41":
                    item["matches_actual47_old_exact_action"] = (
                        output == old_prior["exact_original41_short_J_output"])
                if name == "same-call-observed":
                    item["matches_actual47_observed_exact_action"] = (
                        output == old_prior["exact_same_call_observed_short_J_output"])
                case["maps"][name] = item
                short_maps[name] = {key: value for key, value in item.items()
                                    if key not in ("exact_action", "exact_minus_rational_reference")}
            case_file = E.write_json(
                args.out, f"large-arrays/direction-{index:02d}-comparison.json.gz",
                case, compressed=True)
            report["cases"].append(dict(
                label=vector["label"], input_vector=vector["input_vector"],
                exact_comparison=case_file,
                reference_action_matches_actual47_exact_case=case[
                    "reference_action_matches_actual47_exact_case"], maps=short_maps))
        report["all_prior_exact_action_consistency_flags"] = all(
            item["reference_action_matches_actual47_exact_case"] for item in report["cases"])
        report["no_comparison_error_threshold_applied"] = True
        report["replacement_matrix_does_not_reuse_an_old_solve_as_new_acceptance"] = True
        manifest = dict(
            schema="complete-saved-four-A-reference-output-arrays-v1",
            shape=[SIZE, K], exact_reference=report["exact_reference"],
            correctly_rounded_reference=report["correctly_rounded_reference"],
            input_maps=map_descriptors,
            complete_difference_matrices={
                name: item["exact_difference_matrix"] for name, item in report["map_comparisons"].items()},
            direction_comparisons=[item["exact_comparison"] for item in report["cases"]],
            inputs=[item["input_vector"] for item in report["cases"]])
        report["array_manifest"] = E.write_json(args.out, "array-manifest.json", manifest)
        report["completed"] = True
    except Exception as error:
        report["actual_error"] = repr(error)
        trace_raw = traceback.format_exc().encode()
        with (args.out / "failure-traceback.txt").open("xb") as stream:
            stream.write(trace_raw)
        report["failure_traceback"] = dict(
            file="failure-traceback.txt", bytes=len(trace_raw), sha256=digest(trace_raw))
    finally:
        report["elapsed_seconds"] = time.monotonic() - started
        report["maximum_RSS_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if E is not None:
            full_result = E.write_json(args.out, "result.json.gz", report, compressed=True)
            summary = reduced_summary(dict(report, full_result=full_result))
            # Full vectors/matrices always remain in the same complete files.
            encoded = json.dumps(summary, allow_nan=False).encode()
            if len(encoded) >= 90000:
                summary["cases"] = [
                    {key: item[key] for key in (
                        "label", "input_vector", "exact_comparison",
                        "reference_action_matches_actual47_exact_case")}
                    for item in report["cases"]]
                summary["complete_comparison_reports_are_in_result_gz"] = True
            summary_file = E.write_json(args.out, "summary.json", summary)
            print(json.dumps(dict(event="complete_rational_reference_finished",
                                  completed=report["completed"], summary=summary_file,
                                  original_RHS_J_calls=0, native_accepted=False)), flush=True)
        else:
            raw = (json.dumps(report, sort_keys=True, allow_nan=False) + "\n").encode()
            with (args.out / "summary.json").open("xb") as stream:
                stream.write(raw)
    return 0 if report["completed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())

