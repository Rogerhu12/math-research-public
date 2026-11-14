#!/usr/bin/env python3
"""Saved-four-A RK4 formation in explicit R271 frequency-balanced coordinates.

Scientific execution is restricted to the public repository's GitHub Actions.
No native/root/RHS/local-J call, ODE step, nonlinear solve or trial is made.
All four saved 226 by 224 matrices and the original h/port remain fixed.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import resource
import sys
import time
import traceback

PUBLIC_REPOSITORY = "Rogerhu12/math-research-public"
M, K, SIZE = 112, 224, 226
EXACT_READER = "exact_20261114_single_step_rational_action.py"
EXACT_READER_SHA = "9c42982291bd1a7b7cf21c472d8aae877136fb884708a8310ca6bb882c1d103e"
ACTUAL47_RESULT_SHA = "da9715ef1685c04210d5c3d8bbfb40629fd4bf810455b497e5e25630ac0aa403"
ACTUAL47_WINDOW_SHA = "2608bb3b27cfd16020fcdbaf2bae6c8c9b63cb85146d6c5198d1905b4f64e450"
ACTUAL47_SPEC_SHA = "f813683b76caf4ede4b73bdc2085880b669736c2cf967be981869f7f34de1d05"
SCHEMA = "saved-four-local-A-R271-frequency-balanced-RK4-candidates-v1"
ARRAY_SCHEMA = "saved-four-local-A-R271-working-arrays-v1"
PRIMARY = "r271-frequency-balanced-longdouble"
DIRECT = "direct-original-coordinates-longdouble"


def actions_only():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != PUBLIC_REPOSITORY):
        raise RuntimeError("Execute scientific algebra only in the designated public Actions")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def need(value, message):
    if not value:
        raise ValueError(message)


def load_exact_reader():
    path = Path(__file__).resolve().parent / EXACT_READER
    raw = path.read_bytes()
    need(digest(raw) == EXACT_READER_SHA, "The frozen input reader changed")
    spec = importlib.util.spec_from_file_location("_saved_stage_r271_exact_input_reader", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write_json(directory, name, value):
    raw = (json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n").encode()
    path = directory / name
    with path.open("xb") as stream:
        stream.write(raw)
    return dict(file=name, bytes=len(raw), sha256=digest(raw))


def complete_metadata(E, directory, result, name, fixed_sha=None):
    candidates = [d for d in result["small_output_files"] if d.get("file") == name]
    need(len(candidates) == 1, "Unique completed metadata descriptor required: " + name)
    descriptor = candidates[0]
    if fixed_sha is not None:
        E.same(descriptor["sha256"], fixed_sha, "fixed original metadata " + name)
    obj = E.object_file(directory, descriptor)
    return obj, descriptor


def bind_inputs(E, args, np):
    E.same(args.capture_result_sha256, ACTUAL47_RESULT_SHA, "the actual47 complete capture")
    decoded, old_shape, old_mean, obs_shape, obs_mean, h, port, sigma, binding = E.validate_capture(
        args.capture_directory, args.capture_result_sha256)
    # E performed full byte/shape/finite/source binding, not a new scientific action.
    del decoded, old_shape, old_mean, obs_shape, obs_mean, h, port, sigma
    directory = args.capture_directory.resolve()
    result, receipt = E.read_json(directory / "result.json", ACTUAL47_RESULT_SHA)
    summary, summary_receipt = E.read_json(
        directory / "stage43-local-j-summary.json", result["capture_summary_sha256"])
    window, window_desc = complete_metadata(
        E, directory, result, "stage43-local-j-window-identity.json", ACTUAL47_WINDOW_SHA)
    spec, spec_desc = complete_metadata(
        E, directory, result, "stage43-local-j-spec.json", ACTUAL47_SPEC_SHA)
    E.same(result["spec_sha256"], ACTUAL47_SPEC_SHA, "same complete capture spec")
    E.same(spec["numerical_parameters"]["orientation"], 1, "original orientation")
    E.same(spec["numerical_parameters"]["spacing"], 2, "original Fourier frequency spacing")
    E.same(spec["numerical_parameters"]["modes"], M, "all original modes")
    E.same(window["selected_original_stage"], 43, "original selected stage")
    E.same(window["selected_flow_step"], 11, "original selected flow step")
    E.same(window["complete_mean_state_not_reset"], True, "carried original means")
    E.same(window["additional_ODE_steps"], 0, "no additional original ODE steps")
    fields = summary["field_reports"]
    arrays = []
    for index, field in enumerate(fields):
        E.same(field["field_index"], index, "all four independent field matrices")
        raw = E.descriptor_bytes(directory, field["arrays"]["local_jacobian"], (SIZE, K))
        arrays.append(np.frombuffer(raw, dtype="<f8").reshape(SIZE, K).astype(np.longdouble))
    enriched = dict(binding)
    enriched.update(
        capture_result=receipt, capture_summary=summary_receipt,
        actual47_window=window_desc, actual47_capture_spec=spec_desc,
        original_four_field_records=fields,
        selected_window_identity=window,
        original_orientation=spec["numerical_parameters"]["orientation"],
        original_spacing=spec["numerical_parameters"]["spacing"],
        original_mode_count=M, fixed_stage=43, fixed_step=11,
        fixed_new_stage=519, fixed_input_node=520,
        saved_A_are_actual_binary64_operands=True,
        no_claim_that_saved_A_are_exact_true_DF=True)
    return arrays, summary, window, enriched


def number_ld(E, np, record, label):
    E.number_record(record, label)
    return np.longdouble(np.frombuffer(bytes.fromhex(record["float64le_hex"]), dtype="<f8")[0])


def finite(np, array, label):
    need(bool(np.all(np.isfinite(array))), "Nonfinite formed array: " + label)


def working_format(np):
    dtype = np.dtype(np.longdouble)
    info = np.finfo(dtype)
    # The frozen implementation names and canonicalizes the actual storage.
    # This is a representation requirement, not a geometric acceptance test.
    need(sys.byteorder == "little", "This saved-byte implementation uses little endian storage")
    if info.nmant == 63 and dtype.itemsize in (12, 16) and info.maxexp == 16384:
        active = 10
        representation = "x87-binary80-little-endian-with-zeroed-storage-padding"
    elif info.nmant == 112 and dtype.itemsize == 16 and info.maxexp == 16384:
        active = 16
        representation = "IEEE754-binary128-little-endian"
    elif info.nmant == 52 and dtype.itemsize == 8:
        active = 8
        representation = "IEEE754-binary64-little-endian-longdouble-alias"
    else:
        raise ValueError("Unsupported longdouble storage; do not guess its padding or precision")
    return dict(
        numpy_dtype=dtype.str, itemsize=dtype.itemsize,
        numpy_finfo_nmant=int(info.nmant), explicit_fraction_bits=int(info.nmant),
        significand_bits=int(info.nmant)+1, max_exponent=int(info.maxexp),
        machine_epsilon_decimal=str(info.eps), representation=representation,
        active_bytes=active, storage_padding_bytes=dtype.itemsize-active,
        padding_is_canonicalized_without_changing_the_numeric_value=True,
        actual_precision_is_recorded_not_assumed=True)


class Arrays:
    def __init__(self, np, directory, format_record):
        self.np = np
        self.directory = directory
        self.large = directory / "large-arrays"
        self.large.mkdir()
        self.format = format_record
        self.rows = []
        self.names = set()

    def save(self, name, values, role, binary64=False):
        np = self.np
        need(name not in self.names and all(c.isalnum() or c == "-" for c in name),
             "Use a unique safe array name")
        self.names.add(name)
        dtype = np.dtype("<f8") if binary64 else np.dtype(np.longdouble)
        arr = np.ascontiguousarray(values, dtype=dtype)
        shape = list(arr.shape)
        if binary64:
            raw = arr.tobytes(order="C")
            suffix, stored_dtype = ".f64le", "<f8"
            encoding = dict(representation="IEEE754-binary64-little-endian",
                            itemsize=8, active_bytes=8, storage_padding_bytes=0)
        else:
            words = arr.view(np.uint8).reshape(-1, dtype.itemsize).copy()
            active = self.format["active_bytes"]
            if active < dtype.itemsize:
                words[:, active:] = 0
            raw = words.tobytes(order="C")
            suffix, stored_dtype = ".longdouble-le", dtype.str
            encoding = dict(self.format)
        relative = "large-arrays/" + name + suffix
        with (self.directory / relative).open("xb") as stream:
            stream.write(raw)
        row = dict(
            name=name, file=relative, bytes=len(raw), sha256=digest(raw),
            dtype=stored_dtype, order="C", shape=shape, role=role,
            encoding=encoding, entries=int(arr.size),
            finite_entries=int(np.count_nonzero(np.isfinite(arr))),
            negative_zero_entries=int(np.count_nonzero((arr == 0) & np.signbit(arr))))
        self.rows.append(row)
        return row

    def manifest(self, source_sha, complete, capture_sha):
        return write_json(self.directory, "array-manifest.json", dict(
            schema=ARRAY_SCHEMA, source_sha256=source_sha, completed=complete,
            capture_result_sha256=capture_sha, arrays=self.rows,
            complete_array_bytes_retained=True, arrays_are_artifact_only=True,
            longdouble_encoding_is_explicit=True))


def left_triangular(np, X, coefficients):
    """diag(H,Imean) X; Q/Pi are the first/second contiguous M rows."""
    alpha, beta, eta = (coefficients[:, j, None] for j in range(3))
    Y = np.array(X, dtype=np.longdouble, copy=True, order="C")
    Y[:M] = alpha * X[:M]
    Y[M:K] = beta * X[:M] + eta * X[M:K]
    return Y


def inverse_left_triangular(np, X, coefficients):
    alpha, beta, eta = (coefficients[:, j, None] for j in range(3))
    Y = np.array(X, dtype=np.longdouble, copy=True, order="C")
    Y[:M] = X[:M] / alpha
    Y[M:K] = (X[M:K] - beta * Y[:M]) / eta
    return Y


def right_triangular(np, X, coefficients):
    """X H on its full 224 input columns, including both output mean rows."""
    alpha, beta, eta = (coefficients[None, :, j] for j in range(3))
    Y = np.empty_like(X, dtype=np.longdouble, order="C")
    Y[:, :M] = X[:, :M] * alpha + X[:, M:K] * beta
    Y[:, M:K] = X[:, M:K] * eta
    return Y


def inverse_right_triangular(np, X, coefficients):
    """X H^-1 by its two triangular formulas; no dropped coupling."""
    alpha, beta, eta = (coefficients[None, :, j] for j in range(3))
    Y = np.empty_like(X, dtype=np.longdouble, order="C")
    Y[:, :M] = (X[:, :M] - X[:, M:K] * (beta / eta)) / alpha
    Y[:, M:K] = X[:, M:K] / eta
    return Y


def transport_coefficients(np, destination, source):
    """Form H_destination H_source^-1; equal saved frames give exact I."""
    if bool(np.array_equal(destination, source)):
        out = np.zeros((M, 3), dtype=np.longdouble)
        out[:, 0] = 1
        out[:, 2] = 1
        return out, True
    da, db, de = (destination[:, j] for j in range(3))
    sa, sb, se = (source[:, j] for j in range(3))
    out = np.empty((M, 3), dtype=np.longdouble)
    out[:, 0] = da / sa
    out[:, 2] = de / se
    out[:, 1] = (db - out[:, 2] * sb) / sa
    return out, False


def frames(E, np, summary, window, writer):
    mu = number_ld(E, np, window["mu"], "original saved mu")
    need(bool(mu > 0), "The actual saved positive mu is required")
    sqrt7 = np.sqrt(np.longdouble(7))
    sqrt12 = np.sqrt(np.longdouble(12))
    frequency = np.arange(1, M+1, dtype=np.longdouble) * np.longdouble(2)
    outputs = {}
    records = []
    for index, field in enumerate(summary["field_reports"]):
        geom = field["geometry_number_fields"]
        r = number_ld(E, np, geom["r"], "field r")
        w = number_ld(E, np, geom["w"], "field w")
        need(bool(r > 0) and bool(w > 0), "Positive saved r and w are required")
        alpha = r**4
        b = sqrt12 * mu / (r**7 * w)
        H = np.empty((M, 3), dtype=np.longdouble)
        H[:, 0] = alpha
        H[:, 1] = alpha * frequency / sqrt7
        H[:, 2] = alpha * b / (sqrt7 * frequency)
        descriptor = writer.save(
            "frame-field-"+str(index), H,
            "Per-mode rows [alpha,beta,eta] of H=[[alpha,0],[beta,eta]]")
        finite(np, H, "frame field "+str(index))
        need(bool(np.all(H[:, 0] != 0)) and bool(np.all(H[:, 2] != 0)),
             "A finite invertible saved triangular frame is required")
        outputs["abcd"[index]] = H
        records.append(dict(
            label="abcd"[index], field_index=index, coefficients=descriptor,
            input_r=geom["r"], input_w=geom["w"], input_mu=window["mu"],
            original_x=field["x"], original_h=field["h"],
            complete_original_geometry=geom,
            frozen_at_saved_stage_geometry=True,
            H_definition="r^4 * [[1,0],[m/sqrt(7), b/(sqrt(7)*m)]], b=sqrt(12)*mu/(r^7*w)",
            original_w2_retained_as_input_metadata_not_replaced_by_w_squared=True))
    outputs["input"] = outputs["a"]
    outputs["output"] = outputs["d"]
    constants = writer.save(
        "frame-frequency-and-square-roots",
        np.concatenate((frequency, np.array([sqrt7, sqrt12], dtype=np.longdouble))),
        "112 exact even frequencies followed by the two actual working-precision square roots")
    return outputs, records, constants


def balanced_rk(np, A, H, h, port, writer):
    E0 = np.zeros((SIZE, K), dtype=np.longdouble)
    E0[:K] = np.eye(K, dtype=np.longdouble)
    transports = {}
    transport_records = []
    required = (
        ("a","input"), ("b","input"), ("b","a"), ("c","input"), ("c","b"),
        ("d","input"), ("d","c"), ("output","input"), ("output","a"),
        ("output","b"), ("output","c"), ("output","d"))
    for to, fr in required:
        values, identical = transport_coefficients(np, H[to], H[fr])
        name = "transport-"+to+"-from-"+fr
        descriptor = writer.save(name, values, "H_destination H_source^-1 triangular coefficients")
        finite(np, values, name)
        transports[(to,fr)] = values
        transport_records.append(dict(
            destination=to, source=fr, coefficients=descriptor,
            exact_same_saved_frame_identity_used=identical,
            distinct_field_A_not_merged=True))
    similarities = []
    similarities_desc = []
    for label, original in zip("abcd", A):
        transformed = inverse_right_triangular(
            np, left_triangular(np, original, H[label]), H[label])
        descriptor = writer.save(
            "similarity-"+label, transformed,
            "diag(H_stage,I2) saved_A H_stage^-1, full 226 by 224")
        finite(np, transformed, "local similarity "+label)
        similarities.append(transformed)
        similarities_desc.append(descriptor)

    stage_inputs, stage_derivatives = [], []
    input_desc, derivative_desc = [], []
    for index, label in enumerate("abcd"):
        initial = left_triangular(np, E0, transports[(label,"input")])
        if index == 0:
            eta = initial
        else:
            previous = "abcd"[index-1]
            transferred = left_triangular(
                np, stage_derivatives[index-1], transports[(label,previous)])
            coefficient = h if index == 3 else h / np.longdouble(2)
            eta = initial + coefficient * transferred
        input_desc.append(writer.save(
            "balanced-stage-"+label+"-input", eta,
            "Full 226 by 224 stage tangent; mean rows retained but never fed into A"))
        finite(np, eta, "balanced stage input "+label)
        derivative = similarities[index] @ eta[:K, :]
        derivative_desc.append(writer.save(
            "balanced-stage-"+label+"-derivative", derivative,
            "Full transformed stage derivative C_i eta_i, all mode couplings retained"))
        finite(np, derivative, "balanced stage derivative "+label)
        stage_inputs.append(eta); stage_derivatives.append(derivative)

    shifted = [left_triangular(np, derivative, transports[("output",label)])
               for label, derivative in zip("abcd", stage_derivatives)]
    weighted = shifted[0] + np.longdouble(2)*shifted[1]
    weighted = weighted + np.longdouble(2)*shifted[2]
    weighted = weighted + shifted[3]
    output = left_triangular(np, E0, transports[("output","input")])
    output = output + h*weighted/np.longdouble(6)
    transformed_desc = writer.save(
        "balanced-output-before-recovery", output,
        "Engine output in field-d frame and input field-a coordinates, full mean rows")
    finite(np, output, "balanced output before original-coordinate recovery")

    # R271: diag(H_out^-1,I2) T_transformed H_in. The original exit port
    # has not been applied to this engine-coordinate map.
    left_recovered = inverse_left_triangular(np, output, H["output"])
    left_desc = writer.save(
        "balanced-output-after-left-recovery", left_recovered,
        "Output restored to original engine Q/Pi; input still in H_input coordinates")
    finite(np, left_recovered, "balanced left recovery")
    engine_original = right_triangular(np, left_recovered, H["input"])
    engine_desc = writer.save(
        "balanced-original-engine-output", engine_original,
        "Complete original-coordinate engine map before the single original exit port")
    finite(np, engine_original, "balanced original engine map")
    stored_original = np.array(engine_original, copy=True, dtype=np.longdouble)
    stored_original[M:K, :] /= port
    stored_desc = writer.save(
        "balanced-original-stored-output", stored_original,
        "Complete original-coordinate map with final Pi port applied exactly once")
    finite(np, stored_original, "balanced original stored output")
    return stored_original, dict(
        transports=transport_records, local_similarities=similarities_desc,
        stage_inputs=input_desc, stage_derivatives=derivative_desc,
        transformed_output=transformed_desc,
        after_left_recovery=left_desc, original_engine_output=engine_desc,
        original_stored_output=stored_desc,
        mean_stage_rows_preserved_and_not_used_as_feedback=True,
        recovery_order="inverse_left_output_frame_then_right_input_frame_then_original_Pi_port",
        continuous_G_derivative_equation_not_used=True)


def direct_rk(np, A, h, port, writer):
    E0 = np.zeros((SIZE, K), dtype=np.longdouble)
    E0[:K] = np.eye(K, dtype=np.longdouble)
    derivatives = []
    records = []
    for index, original in enumerate(A):
        if index == 0:
            stage = E0.copy()
        else:
            coefficient = h if index == 3 else h/np.longdouble(2)
            stage = E0 + coefficient*derivatives[index-1]
        stage_desc = writer.save(
            "direct-stage-"+str(index)+"-input", stage,
            "Same-precision ordinary original-coordinate RK4 full stage tangent")
        derivative = original @ stage[:K, :]
        derivative_desc = writer.save(
            "direct-stage-"+str(index)+"-derivative", derivative,
            "Original saved A_i times the complete shape tangent, two means retained")
        finite(np, stage, "direct stage input "+str(index))
        finite(np, derivative, "direct stage derivative "+str(index))
        derivatives.append(derivative)
        records.append(dict(field_index=index, input=stage_desc, derivative=derivative_desc))
    weighted = derivatives[0] + np.longdouble(2)*derivatives[1]
    weighted = weighted + np.longdouble(2)*derivatives[2]
    weighted = weighted + derivatives[3]
    engine = E0 + h*weighted/np.longdouble(6)
    engine_desc = writer.save(
        "direct-original-engine-output", engine,
        "Working-precision original-coordinate RK4 map before the exit port")
    finite(np, engine, "direct engine output")
    stored = np.array(engine, copy=True, dtype=np.longdouble)
    stored[M:K, :] /= port
    stored_desc = writer.save(
        "direct-original-stored-output", stored,
        "Working-precision original-coordinate RK4 map after the single Pi port")
    finite(np, stored, "direct stored output")
    return stored, dict(stages=records, original_engine_output=engine_desc,
                        original_stored_output=stored_desc)


def save_candidate(np, writer, name, working, role):
    # The independent exact consumer measures this actual cast matrix against
    # the fixed four-A rational reference; no producer-side tolerance is used.
    output = np.asarray(working, dtype="<f8", order="C")
    full = writer.save(name+"-full", output, role, binary64=True)
    shape = writer.save(name+"-shape", output[:K, :],
                        "Complete original-coordinate shape block; all columns", binary64=True)
    mean = writer.save(name+"-mean", output[K:, :],
                       "Both original-coordinate mean rows, no final port scaling", binary64=True)
    finite(np, output, "candidate binary64 output "+name)
    return full, dict(
        shape_J=shape, mean_rows=mean,
        working_nonzero_to_binary64_zero_entries=int(np.count_nonzero((working != 0) & (output == 0))),
        binary64_negative_zero_entries=int(np.count_nonzero((output == 0) & np.signbit(output))),
        all_224_original_input_columns_retained=True,
        complete_original_output_rows=SIZE,
        original_Pi_exit_port_already_applied=True,
        mean_rows_not_port_scaled=True,
        candidate_is_new_array_not_actual41_frozen_J=True)


def main():
    actions_only()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture-directory", type=Path, required=True)
    parser.add_argument("--capture-result-sha256", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.capture_directory = args.capture_directory.resolve()
    args.out = args.out.resolve()
    need(not args.out.exists() and not args.out.is_relative_to(args.capture_directory),
         "Use a new independent candidate output directory")
    args.out.mkdir(parents=True)
    started = time.monotonic()
    source_sha = digest(Path(__file__).read_bytes())
    report = dict(
        schema=SCHEMA, completed=False, source_sha256=source_sha,
        frozen_input_reader_sha256=EXACT_READER_SHA,
        capture_result_sha256=args.capture_result_sha256,
        fixed_stage=43, fixed_step=11, fixed_new_stage=519, fixed_input_node=520,
        rows=SIZE, columns=K, modes=M,
        new_root_calls=0, new_RHS_calls=0, new_local_J_calls=0,
        new_ODE_steps=0, new_native_solves=0, new_nonlinear_trials=0,
        full_actual_couplings_retained=True, omitted_modes=0,
        native_accepted=False, task_completed=False,
        exact_reference_comparison_is_a_separate_consumer=True,
        no_actual43_direction_used_as_an_acceptance_gate=True,
        no_claim_of_true_DF_or_global_system_accuracy=True,
        changed_arithmetic_representation_not_changed_nonlinear_equations=True)
    writer = None
    phase = "loading-bound-inputs"
    try:
        E = load_exact_reader()
        E.require_sha(args.capture_result_sha256, "actual47 capture result")
        import numpy as np
        np.seterr(over="raise", invalid="raise", divide="raise", under="ignore")
        report["runtime"] = dict(
            python=sys.version, numpy=np.__version__, platform=platform.platform(),
            machine=platform.machine(), byteorder=sys.byteorder,
            public_run=os.environ.get("GITHUB_RUN_ID"),
            public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
            working_precision=working_format(np))
        writer = Arrays(np, args.out, report["runtime"]["working_precision"])
        A, summary, window, binding = bind_inputs(E, args, np)
        report["input_binding"] = write_json(args.out, "input-binding.json", binding)
        report["original_h"] = summary["original_h"]
        report["original_port_ratio"] = summary["original_port_ratio"]
        report["original_sigma"] = summary["original_sigma"]
        h = number_ld(E, np, summary["original_h"], "same original h")
        port = number_ld(E, np, summary["original_port_ratio"], "same original exit port")
        need(bool(h > 0) and bool(port != 0), "Positive h and a nonzero original port are required")

        phase = "forming-frozen-frequency-frames"
        H, frame_records, constants = frames(E, np, summary, window, writer)
        report["frames"] = frame_records
        report["working_frequency_and_constants"] = constants
        report["frame_aliases"] = dict(input="a", output="d")
        report["frame_mean_extension"] = "diag(H_shape,I2)"
        report["frame_parameters_are_frozen_at_saved_field_geometry"] = True
        report["frame_coefficients_are_saved_finite_working_precision_constants"] = True
        report["all_distinct_stage_interfaces_explicit"] = True

        phase = "forming-R271-complete-transferred-RK"
        balanced, balanced_work = balanced_rk(np, A, H, h, port, writer)
        report["balanced_work"] = balanced_work
        balanced_full, balanced_components = save_candidate(
            np, writer, PRIMARY, balanced,
            "Full226x224 R271 candidate restored to original Q/Pi/mean coordinates and original port")

        phase = "forming-same-precision-direct-control"
        direct, direct_work = direct_rk(np, A, h, port, writer)
        report["direct_work"] = direct_work
        direct_full, direct_components = save_candidate(
            np, writer, DIRECT, direct,
            "Same-working-precision direct RK4 control in original coordinates and original port")
        report["candidate_maps"] = {PRIMARY:balanced_full, DIRECT:direct_full}
        report["candidate_components"] = {
            PRIMARY:balanced_components, DIRECT:direct_components}
        report["full_original_output"] = balanced_full
        report["shape_J"] = balanced_components["shape_J"]
        report["mean_rows"] = balanced_components["mean_rows"]
        report["complete_mean_rows_retained"] = True
        report["formed_complete_linear_maps"] = 2
        report["completed"] = True
        phase = "complete"
    except Exception as error:
        report["actual_failure"] = dict(phase=phase, error=repr(error))
        raw = traceback.format_exc().encode()
        with (args.out/"failure-traceback.txt").open("xb") as stream:
            stream.write(raw)
        report["failure_traceback"] = dict(
            file="failure-traceback.txt", bytes=len(raw), sha256=digest(raw))
    finally:
        if writer is not None:
            report["array_manifest"] = writer.manifest(
                source_sha, report["completed"], args.capture_result_sha256)
        report["elapsed_seconds"] = time.monotonic()-started
        report["maximum_RSS_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        result = write_json(args.out, "result.json", report)
        summary = dict(
            schema=SCHEMA, completed=report["completed"],
            source_sha256=source_sha, capture_result_sha256=args.capture_result_sha256,
            full_result=result, elapsed_seconds=report["elapsed_seconds"],
            maximum_RSS_kib=report["maximum_RSS_kib"],
            native_accepted=False, task_completed=False)
        for name in ("candidate_maps","original_h","original_port_ratio","array_manifest","actual_failure"):
            if name in report:
                summary[name] = report[name]
        summary_desc = write_json(args.out,"summary.json",summary)
        print(json.dumps(dict(event="saved_stage_R271_candidates_finished",
                              completed=report["completed"], summary=summary_desc,
                              native_accepted=False, task_completed=False)),flush=True)
    return 0 if report["completed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
