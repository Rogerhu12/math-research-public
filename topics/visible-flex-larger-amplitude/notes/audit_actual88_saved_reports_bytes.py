#!/usr/bin/env python3
"""Read/hash actual88 reports; never recompute SVD or scientific arithmetic.

Allowed operations are JSON/gzip transport, exact recursive comparisons,
binary64 serialization/classification, structural counts, SHA256 and read-only
Git blob extraction. No NumPy/scientific module is imported or executed.
"""
from __future__ import annotations

import argparse
import ast
import gzip
import hashlib
import json
from pathlib import Path
import struct
import subprocess


ACTUAL88 = {
    "run_id": 43671452656,
    "source_commit": "facffded7fdc069cbd91473d845c2e8377a7bd8f",
    "job_id": 132682194531,
    "artifact_id": 14144800598,
    "artifact_name": "visible-mainline-modelresponse-43671452656-1",
    "artifact_zip_bytes": 70747,
    "artifact_zip_sha256": "c62887dc85bb2f551a283fb35f7c98dce048ae32a5c5b95b3b4f806990587a63",
    "job_conclusion": "success",
}
FILES = {
    "numpy-install.log": (448, "19b6e6311729ebb28107f5823f8c6297aed0ac4c9f56726c02516e8f60624276"),
    "request88-input-and-source-identity.json": (11166, "23ae230b64f205cc140803be82de51fe724d97bc0bf0f76b6fe4766a7e21b417"),
    "saved85-direction-spectrum/actual85-original-status.json": (54251, "72397df159924d54bfcf7892b0f22d0a6b9e796238b5d29f8802e22120fb1a0a"),
    "saved85-direction-spectrum/large-arrays/saved-direction-analysis.json": (174419, "0098d7c09244e6a8deae9508883399227bb59d5a9de0b97e11e4811acb7f3798"),
    "saved85-direction-spectrum/saved-direction-summary.json": (60931, "eb2ad618b74eed227aec2d224ae7553ad08774ad45ff1e910f17998e4dd38fcc"),
    "saved85-direction-spectrum-command.json": (825, "a7d44c0140768dbe2d63a9234db2894249ed0d41b6a70555d3dbefa9912abf2c"),
    "saved85-direction-spectrum-readback.json": (1462, "d2ec661f07b25fd09197874fb8b45dc32998a42592eacc980403a4553b2ab0d3"),
    "saved85-direction-spectrum.log": (243, "6e075576a8210847bb58f215b1a0cd1fe5e4a93dd83fea38ac708a78470b46b3"),
}
CONSUMER = "geometry_20261115_saved85_direction_spectrum.py"
CONSUMER_SHA = "20fcaa266aa1716be9ab910d2ab988d2259dc56e013b13d3cedccd69be9a9d20"
PUBLISHER = "root_20261114_publish_actions.py"
PUBLISHER_SHA = "22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca"
SCHEMA = "R259-saved-actual85-three-by-three-direction-spectrum-v1"
ORIGINAL_ARRAYS = {
    "r": ("unscaled_equation", (3,)),
    "J": ("unscaled_jacobian", (3, 3)),
    "D": ("coordinate_scale", (3,)),
    "A": ("scaled_jacobian", (3, 3)),
    "z": ("scaled_direction", (3,)),
    "parameter_direction": ("recovered_original_parameter_direction", (3,)),
    "Jd": ("original_jacobian_times_recovered_direction", (3,)),
    "augmented_matrix": ("augmented_matrix", (6, 3)),
    "augmented_rhs": ("augmented_rhs", (6,)),
}
PREDICTION_SUMMARY_KEYS = (
    "damping_cli_text", "residual_removed_filter", "residual_retained_filter",
    "singular_residual_coordinates_after", "original_linear_residual",
    "original_merit_directional_slope", "original_linear_merit_decrease",
    "stored_A_linear_merit_decrease", "scaled_damping_penalty",
    "damped_quadratic_decrease", "stationary_readback",
    "actual_nonlinear_trial_performed", "nonlinear_acceptance_claimed",
)
PREDICTION_VECTOR_KEYS = (
    "residual_removed_filter", "residual_retained_filter", "direction_filter",
    "singular_residual_coordinates_before", "singular_residual_coordinates_after",
    "predicted_half_squared_residual_by_singular_direction", "scaled_direction",
    "parameter_direction", "original_J_times_direction", "original_linear_residual",
    "original_merit_directional_slope_by_equation",
    "original_linear_merit_decrease_by_equation",
)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def equal_bits(a, b):
    if isinstance(a, bool) or isinstance(b, bool):
        return type(a) is bool and type(b) is bool and a is b
    if isinstance(a, dict) or isinstance(b, dict):
        return (isinstance(a, dict) and isinstance(b, dict) and a.keys() == b.keys()
                and all(equal_bits(a[k], b[k]) for k in a))
    if isinstance(a, list) or isinstance(b, list):
        return (isinstance(a, list) and isinstance(b, list) and len(a) == len(b)
                and all(equal_bits(x, y) for x, y in zip(a, b)))
    if isinstance(a, int) and isinstance(b, int):
        return a == b
    if isinstance(a, (int, float)) or isinstance(b, (int, float)):
        return (isinstance(a, (int, float)) and isinstance(b, (int, float))
                and struct.pack("<d", a) == struct.pack("<d", b))
    return type(a) is type(b) and a == b


def packed_array(value, shape):
    if not shape:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("Expected a JSON numeric leaf")
        raw = struct.pack("<d", value)
        word = struct.unpack("<Q", raw)[0]
        if ((word >> 52) & 0x7ff) == 0x7ff:
            raise ValueError("The recorded finite array contains a nonfinite word")
        return raw
    if not isinstance(value, list) or len(value) != shape[0]:
        raise ValueError("Array shape mismatch")
    return b"".join(packed_array(v, shape[1:]) for v in value)


def receipt(name, raw):
    return {"file": name, "bytes": len(raw), "sha256": sha(raw)}


def write_json(path, value):
    raw = (json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode()
    path.write_bytes(raw)
    return receipt(path.name, raw)


def write_gzip(path, raw):
    zipped = gzip.compress(raw, compresslevel=9, mtime=0)
    path.write_bytes(zipped)
    if gzip.decompress(zipped) != raw:
        raise ValueError("Compression round trip failed")
    return {**receipt(path.name, zipped), "decoded_bytes": len(raw),
            "decoded_sha256": sha(raw),
            "compression_created_by_byte_readback": True,
            "decoded_payload_is_complete_original_bytes": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact-directory", type=Path, required=True)
    parser.add_argument("--original85-status", type=Path, required=True)
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    outputs = (
        "2026-11-15-actual88-byte-audit.json.gz",
        "2026-11-15-actual88-byte-audit-summary.json",
        "2026-11-15-actual88-original-full-analysis.json.gz",
        "2026-11-15-actual88-original-status85.json.gz",
        "2026-11-15-actual88-literal-readout.json.gz",
    )
    if any((args.out / name).exists() for name in outputs):
        raise ValueError("Do not overwrite a frozen audit/readout")
    checks = []

    def check(label, condition):
        checks.append({"label": label, "passed": bool(condition)})
        if not condition:
            raise ValueError("Byte/structure mismatch: " + label)

    input_files = []
    payloads = {}
    for name, (size, digest) in FILES.items():
        raw = (args.artifact_directory / name).read_bytes()
        check("file " + name, len(raw) == size and sha(raw) == digest)
        payloads[name] = raw
        input_files.append(receipt(name, raw))
    check("exact eight non-hidden original artifact files",
          set(FILES) == {str(p.relative_to(args.artifact_directory))
                         for p in args.artifact_directory.rglob("*")
                         if p.is_file() and not any(x.startswith(".") for x in p.relative_to(args.artifact_directory).parts)})
    full_name = "saved85-direction-spectrum/large-arrays/saved-direction-analysis.json"
    summary_name = "saved85-direction-spectrum/saved-direction-summary.json"
    status_name = "saved85-direction-spectrum/actual85-original-status.json"
    full = json.loads(payloads[full_name])
    summary = json.loads(payloads[summary_name])
    status = json.loads(payloads[status_name])
    identity = json.loads(payloads["request88-input-and-source-identity.json"])
    command = json.loads(payloads["saved85-direction-spectrum-command.json"])
    readback = json.loads(payloads["saved85-direction-spectrum-readback.json"])
    log = json.loads(payloads["saved85-direction-spectrum.log"])
    original85 = args.original85_status.read_bytes()
    check("complete copied original85 status bytes", original85 == payloads[status_name])
    check("completed diagnostic, not candidate", full["schema"] == SCHEMA
          and full["phase"] == "diagnostic-completed" and full["diagnostic_completed"] is True
          and status["success"] is False and status["low_mode_candidate_has_small_full_recorded_right_residual"] is False)
    check("actual run and consumer source", identity["source_commit"] == ACTUAL88["source_commit"]
          and full["source_sha256"] == CONSUMER_SHA)
    check("all eight original steps and all three declared eta models", len(full["rows"]) == 8
          and len(status["searches"]) == 8 and full["comparisons_requested"] == ["0.01", "0.001"])
    check("original eta and trial controls unchanged", status["damping_cli_text"] == "0.1"
          and equal_bits(status["damping_binary64"], .1) and status["candidate_iteration_budget"] == 8
          and status["original_backtrack_budget"] == 20
          and equal_bits(status["original_armijo_coefficient"], .2)
          and equal_bits(status["candidate_resonance_tolerance"], 1e-8))
    false_fields = (
        "field_RHS_J_tail_FD_or_optimizer_called", "original_status_modified",
        "original_criteria_modified", "projective_or_geometric_normalization_performed",
        "new_candidate_accepted", "existence_or_transversality_proved",
        "original_actual85_candidate_success",
    )
    check("scope flags in complete result", all(full[k] is False for k in false_fields))
    check("original input binding receipts only", equal_bits(full["original_input_bindings"], status["input_sha256"])
          and equal_bits(full["original_input_bindings"], identity["request"]["original_mathematical_input_sha256_receipts"])
          and identity["original_input_bindings_are_receipts_not_reaudited_payloads"] is True)
    check("complete full result descriptor", equal_bits(summary["full_analysis"],
          receipt("large-arrays/saved-direction-analysis.json", payloads[full_name])))
    check("original status descriptor", equal_bits(full["verified_original_status"],
          receipt("actual85-original-status.json", original85)))
    check("command completed once without original solver", command["completed"] is True
          and command["returncode"] == 0 and command["consumer_invocations"] == 1
          and command["original_nonlinear_solver_invocations"] == 0
          and command["argv"][command["argv"].index("--comparison-damping") + 1:
                              command["argv"].index("--out")] == ["0.01", "0.001"])
    check("readback summary descriptor", equal_bits(readback["original_summary"], receipt(summary_name, payloads[summary_name])))
    check("console result descriptor", equal_bits(log["full_analysis"], summary["full_analysis"])
          and log["rows"] == 8 and log["diagnostic_completed"] is True)
    for key, value in readback["original_fields"].items():
        check("readback original field " + key, equal_bits(value, summary.get(key)))
    for key, value in full.items():
        if key != "rows":
            check("summary complete top field " + key, equal_bits(value, summary[key]))
    check("summary scope label", summary["summary_is_saved_array_arithmetic_not_a_candidate_gate"] is True)

    # Re-read exact dispatch Git blobs. Current HEAD may contain later publisher
    # versions, so no mutable working-tree file is substituted for actual88.
    source_receipts = []
    original_sources = status["consumed_source_sha256"]
    all_sources = dict(original_sources)
    all_sources.update({CONSUMER: CONSUMER_SHA, PUBLISHER: PUBLISHER_SHA})
    check("eleven original and thirteen full source pins", len(original_sources) == 11
          and len(all_sources) == 13 and equal_bits(all_sources, identity["request"]["source_sha256"]))
    source_desc = {r["file"]: r for r in identity["verified_sources"]}
    check("full thirteen request source descriptor set", set(source_desc) == set(all_sources))
    consumed_desc = {r["file"]: r for r in full["verified_consumed_sources"]}
    check("full eleven consumed source descriptor set", set(consumed_desc) == set(original_sources))
    for name, digest in all_sources.items():
        check("safe source basename " + name, Path(name).name == name)
        spec = ACTUAL88["source_commit"] + ":topics/visible-flex-larger-amplitude/computations/" + name
        raw = subprocess.run(["git", "show", spec], cwd=args.repository, check=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout
        check("dispatch source " + name, sha(raw) == digest
              and source_desc[name]["sha256"] == digest and source_desc[name]["bytes"] == len(raw)
              and source_desc[name]["mathematical_import_or_call"] is False)
        if name in consumed_desc:
            check("consumed source " + name, consumed_desc[name]["sha256"] == digest
                  and consumed_desc[name]["bytes"] == len(raw)
                  and consumed_desc[name]["imported_or_executed"] is False)
        ast.parse(raw, filename=name)
        source_receipts.append({**receipt(name, raw), "read_from_exact_dispatch_commit": ACTUAL88["source_commit"],
                                "AST_parsed_without_import": True, "executed": False})

    original_array_receipts = []
    derived_array_receipts = []
    literal_rows = []
    for index, (row, old, compact) in enumerate(zip(full["rows"], status["searches"], summary["rows"])):
        prefix = "row " + str(index) + " "
        model = old["direction_model"]
        check(prefix + "sequence and original pointer", row["iteration"] == index == old["iteration"]
              and row["original_status_pointer"] == "searches/" + str(index))
        pairs = {
            "parameters": old["parameters"], "original_equation": old["residual"],
            "original_jacobian": old["derivative"], "original_coordinate_scale": model["coordinate_scale"],
            "original_scaled_jacobian": model["scaled_jacobian"],
            "original_saved_direction_model": model,
            "original_true_model_merit_slope": old["true_model_merit_slope"],
            "original_trials": old["trials"],
            "original_next_equation": (status["searches"][index + 1]["residual"]
                                       if index + 1 < len(status["searches"]) else status["final"]["low_equations_used"]),
        }
        for key, value in pairs.items():
            check(prefix + "complete original field " + key, equal_bits(row[key], value))
        check(prefix + "original one full accepted step", old["accepted"] is True and len(old["trials"]) == 1
              and old["trials"][0]["accepted"] is True and equal_bits(old["trials"][0]["alpha"], 1.))
        for key, (oldkey, shape) in ORIGINAL_ARRAYS.items():
            raw = packed_array(model[oldkey], shape)
            desc = row["original_array_identities"][key]
            check(prefix + "array " + key, desc["shape"] == list(shape)
                  and desc["dtype"] == "little-endian-float64"
                  and desc["bytes"] == len(raw) and desc["sha256"] == sha(raw))
            original_array_receipts.append({"iteration": index, "array": key,
                "original_status_pointer": "searches/" + str(index) + "/direction_model/" + oldkey,
                **desc, "all_original_JSON_numeric_words_reserialized_and_hash_verified": True})
        compact_expected = {key: row[key] for key in (
            "iteration", "parameters", "original_equation", "original_saved_direction_readback", "consistency_readbacks")}
        compact_expected.update({key: row["new_direct_A_SVD"][key] for key in (
            "singular_values", "residual_coordinates", "half_squared_residual_by_singular_direction")})
        compact_expected["local_model_predictions"] = [
            {key: prediction[key] for key in PREDICTION_SUMMARY_KEYS}
            for prediction in row["local_model_predictions"]]
        check(prefix + "entire summary projection", equal_bits(compact, compact_expected))
        check(prefix + "three ordered local predictions", [p["damping_cli_text"] for p in row["local_model_predictions"]]
              == ["0.1", "0.01", "0.001"])
        svd = row["new_direct_A_SVD"]
        for key in ("U", "singular_values", "Vh", "residual_coordinates", "half_squared_residual_by_singular_direction"):
            shape = (3, 3) if key in ("U", "Vh") else (3,)
            raw = packed_array(svd[key], shape)
            derived_array_receipts.append({"iteration": index, "pointer": "new_direct_A_SVD/" + key,
                "shape": list(shape), "bytes": len(raw), "sha256": sha(raw),
                "identity_of_recorded_JSON_words_only": True, "arithmetic_recomputed": False})
        for prediction in row["local_model_predictions"]:
            eta = prediction["damping_cli_text"]
            check(prefix + "no predicted trial " + eta, prediction["actual_nonlinear_trial_performed"] is False
                  and prediction["nonlinear_acceptance_claimed"] is False)
            check(prefix + "same residual-coordinate input " + eta,
                  equal_bits(prediction["singular_residual_coordinates_before"], svd["residual_coordinates"]))
            for key in PREDICTION_VECTOR_KEYS:
                raw = packed_array(prediction[key], (3,))
                derived_array_receipts.append({"iteration": index, "pointer": "local_model_predictions/" + eta + "/" + key,
                    "shape": [3], "bytes": len(raw), "sha256": sha(raw),
                    "identity_of_recorded_JSON_words_only": True, "arithmetic_recomputed": False})
        saved = row["original_saved_direction_readback"]
        check(prefix + "readback original action", equal_bits(saved["original_action"], model["original_jacobian_times_recovered_direction"]))
        check(prefix + "readback original merits", equal_bits(saved["actual_saved_merit_before"], old["trials"][0]["merit_before"])
              and equal_bits(saved["actual_saved_merit_after"], old["trials"][0]["actual_merit"]))
        literal_rows.append(row)
    for key, value in full["copied_original_final_description"].items():
        check("complete copied final field " + key, equal_bits(value, status["final"][key]))
    check("seventy-two original arrays", len(original_array_receipts) == 72)

    full_gz = write_gzip(args.out / outputs[2], payloads[full_name])
    status_gz = write_gzip(args.out / outputs[3], original85)
    readout = {
        "schema": "actual88-complete-literal-report-readback-v1",
        "classification": "Original public Actions numerical evidence; this file performs no new scientific arithmetic",
        "actual88": ACTUAL88, "original_full_report": receipt(full_name, payloads[full_name]),
        "original_status85": receipt(status_name, original85),
        "copying_semantics": "All eight complete rows, including every original model field and all 24 predictions, are copied from the parsed original report; the separate gzip preserves its exact original bytes.",
        "original_full_report_metadata": {k: v for k, v in full.items() if k != "rows"},
        "rows": literal_rows,
        "local_scientific_arithmetic_performed": False,
    }
    readout_raw = (json.dumps(readout, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode()
    readout_gz = write_gzip(args.out / outputs[4], readout_raw)
    readout_gz["decoded_payload_is_complete_original_bytes"] = False
    readout_gz["all_eight_complete_rows_copied_without_scientific_arithmetic"] = True
    report = {
        "schema": "actual88-original-reports-byte-audit-v1", "classification": "pure byte/structure readback",
        "actual88": ACTUAL88, "completed": True, "passed": True,
        "scope": {
            "original_artifact_regular_files_read": len(input_files),
            "original_eight_models_complete_fields_compared": 8,
            "original_array_descriptors_verified": len(original_array_receipts),
            "original_array_binary64_words_serialized": sum(x["bytes"] // 8 for x in original_array_receipts),
            "original_array_serialized_bytes": sum(x["bytes"] for x in original_array_receipts),
            "all_local_prediction_objects_compared_or_structurally_read": 24,
            "derived_array_word_identities_recorded": len(derived_array_receipts),
            "full_original_consumed_sources": 11, "exact_dispatch_source_payloads": len(source_receipts),
            "all_eight_summary_rows_verified_against_complete_original_result": True,
            "complete_original85_status_matches_independent_existing85_artifact_copy": True,
            "four_large_mathematical_inputs_reaudited": False,
            "scientific_module_imported_or_executed": False,
            "scientific_matrix_norm_SVD_filter_ratio_Fraction_arithmetic_recomputed": False,
            "new_original_equation_J_or_trial_called": False,
            "new_candidate_or_acceptance_gate": False,
            "artifact_ZIP_refetched_or_reverified_by_this_script": False,
            "root_reported_original_ZIP_metadata_size_SHA_CRC_verified": True,
        },
        "input_files": input_files, "source_payloads": source_receipts,
        "original_array_receipts": original_array_receipts,
        "derived_array_word_receipts": derived_array_receipts,
        "checks": checks, "preserved_outputs": [full_gz, status_gz, readout_gz],
        "audit_source": receipt(Path(__file__).name, Path(__file__).read_bytes()),
        "interpretation_limits": full["interpretation_limits"],
    }
    audit_raw = (json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode()
    audit_desc = write_gzip(args.out / outputs[0], audit_raw)
    audit_desc["decoded_payload_is_complete_original_bytes"] = False
    audit_desc["decoded_payload_is_complete_byte_audit"] = True
    short = {"schema": "actual88-byte-audit-summary-v1", "completed": True, "passed": True,
             "actual88": ACTUAL88, "scope": report["scope"], "passed_check_count": len(checks),
             "complete_byte_audit": audit_desc, "original_full_analysis": full_gz,
             "original85_status": status_gz, "complete_literal_readout": readout_gz,
             "audit_source": report["audit_source"], "new_scientific_arithmetic": False}
    short_desc = write_json(args.out / outputs[1], short)
    print(json.dumps({"passed": True, "scope": report["scope"], "audit": audit_desc,
                      "summary": short_desc, "preserved_outputs": report["preserved_outputs"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
