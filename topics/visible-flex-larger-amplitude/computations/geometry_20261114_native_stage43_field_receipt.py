#!/usr/bin/env python3
"""Read only: extract four original actual41 fields for old stage43, step11.

No numerical module, constructor, RHS, root, geometry, derivative, integration,
norm, stability parameter, threshold, or solve is evaluated. All numeric
records are copied from the pinned original packet. No input is modified.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
from pathlib import Path

RESULT_SHA = "6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf"
RESULT_BYTES = 78403
REPORT = dict(file="stage-043-completed-report.json", bytes=18731,
              sha256="95dc94bf3bb5ec288899d38333d652de888b3aeeb986fcc2b1116701383f40b7")
WINDOW = dict(file="stage-043-step-window-identity.json", bytes=4316,
              sha256="0d9b8b9804d7ea9f6c969f85fd1e8c04eb5e905472db581697344a656200d15d")
PACKET = dict(file="large-arrays/stage-043-field-observations.json.gz",
              bytes=10581,
              sha256="0174ec338f1a6e263f40a1aff89266aefabddedb958752bab9502f0375f4fcbc",
              raw_bytes=104426,
              raw_sha256="0773eabe6e9bbb2cf6677212928da5cda12fcf7e3dfad18580cfc032ff2f8122",
              encoding="json-gzip")
CAPTURE_SOURCE = "c2341018c6293e15ee8e5ba9109b331b29bee2e3e944514e1a0308afe8e6ffd5"
CAPTURE_HOOK = "2695cd2dc0abc66fe3f8ae8987b6ae3b50b884f692a418198347a61dddf24435"
WINDOW_SOURCE = "07dd6101569097a9524c35457c1467002a250911dd049bcb720b3b8c700efd2b"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def require(condition, label):
    if not condition:
        raise ValueError("Pinned original receipt mismatch: " + label)


def located(directory, name):
    relative = Path(name)
    require(not relative.is_absolute() and ".." not in relative.parts, "relative path")
    path = (directory / relative).resolve()
    require(path.is_relative_to(directory) and path.is_file(), "read-only input path " + name)
    return path


def read_pinned(directory, descriptor):
    path = located(directory, descriptor["file"])
    require(path.stat().st_size == descriptor["bytes"], "file size " + descriptor["file"])
    raw = path.read_bytes()
    require(sha(raw) == descriptor["sha256"], "file hash " + descriptor["file"])
    return raw


def inventory_entry(rows, descriptor):
    matches = [row for row in rows if row["file"] == descriptor["file"]]
    require(len(matches) == 1, "one inventory entry " + descriptor["file"])
    require(all(matches[0][key] == descriptor[key] for key in ("file", "bytes", "sha256")),
            "inventory descriptor " + descriptor["file"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture-dir", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    directory = args.capture_dir.resolve()
    out = args.out.resolve()
    require(directory.is_dir(), "capture directory")
    require(not out.is_relative_to(directory), "output is independent of immutable capture")
    result_descriptor = dict(file="result.json", bytes=RESULT_BYTES, sha256=RESULT_SHA)
    result = json.loads(read_pinned(directory, result_descriptor))
    require(result["capture_completed"] is True and result["planned_probe_stop_observed"] is True,
            "completed actual41 capture")
    require(result["source_sha256"] == CAPTURE_SOURCE and
            result["hook_sha256"] == CAPTURE_HOOK and
            result["window_module_sha256"] == WINDOW_SOURCE, "frozen capture sources")
    inventory_entry(result["small_output_files"], REPORT)
    inventory_entry(result["stage_reports"], REPORT)
    inventory_entry(result["small_output_files"], WINDOW)
    report = json.loads(read_pinned(directory, REPORT))
    require(report["schema"] == "original-native-rawcell0-original-stage-steps-v1",
            "original stage report schema")
    require((report["stage"], report["rawCell"], report["rawSegment"], report["part"],
             report["parts"], report["step_count"], report["completed_original_field_calls"]) ==
            (43, 0, 3, 4, 8, 12, 48), "exact original stage and counts")
    require(report["identity"] == WINDOW and report["field_observations"] == PACKET,
            "stage-linked window and field packet")
    require(report["original_guards_returned"] is True and
            report["all_actual_original_steps_saved"] is True and
            report["complete226_state_kept_between_all_steps"] is True,
            "original completed stage flags")
    window = json.loads(read_pinned(directory, WINDOW))
    require(window["schema"] == "original-native-rawcell0-step-window-v1" and
            window["stage"] == 43 and window["steps"] == 12 and
            window["full_state_dimension"] == 226, "original window")
    packed = read_pinned(directory, PACKET)
    raw = gzip.decompress(packed)
    require(len(raw) == PACKET["raw_bytes"] and sha(raw) == PACKET["raw_sha256"],
            "complete original decompressed packet")
    packet = json.loads(raw)
    require(packet["schema"] == "original-native-rawcell0-actual-field-geometry-v1" and
            packet["stage"] == 43 and packet["partial"] is False and
            packet["observed_calls"] == 48 and len(packet["fields"]) == 48,
            "original completed field packet")
    require(packet["source_sha256"] == CAPTURE_SOURCE and
            packet["hook_sha256"] == CAPTURE_HOOK and
            packet["spec_sha256"] == result["spec_sha256"], "packet source and spec identities")
    schedules = [row for row in report["schedule"] if row["global_step"] == 11]
    require(len(schedules) == 1, "one original step11")
    step = schedules[0]
    require((step["profile_index"], step["grid_index"], step["grid_branch"],
             step["field_calls"]) == (0, 11, "ordinary", 4), "original selected schedule")
    fields = [row for row in packet["fields"] if row["global_step"] == 11]
    require(len(fields) == 4 and [row["field_index"] for row in fields] == [0, 1, 2, 3],
            "all four original returned fields")
    for row in fields:
        require((row["profile_index"], row["grid_index"], row["grid_branch"]) ==
                (step["profile_index"], step["grid_index"], step["grid_branch"]),
                "field belongs to selected original step")
        require(row["h"] == step["h"], "unchanged original step h record")
        require(all(row["requested_geometry_keys_present"].get(key) is True and
                    key in row["geometry_number_fields"]
                    for key in ("r", "drdx", "w", "w2", "E")),
                "complete requested original geometry records")
    output = dict(
        schema="pinned-actual41-stage43-step11-original-field-receipt-v1",
        source_sha256=sha(Path(__file__).read_bytes()),
        original_public_run="43622149326",
        inputs=dict(result=result_descriptor, completed_report=REPORT,
                    window=WINDOW, complete_field_packet=PACKET),
        original_capture_sources=dict(source_sha256=CAPTURE_SOURCE,
                                      hook_sha256=CAPTURE_HOOK,
                                      window_module_sha256=WINDOW_SOURCE),
        original_spec_sha256=result["spec_sha256"],
        original_stage=43, original_flow_step=11,
        window_identity=window,
        original_profile_schedules=report["profile_schedules"],
        original_step_schedule=step,
        original_sigma=report["original_sigma"],
        original_port_ratio=report["original_port_ratio"],
        original_stage_reference_descriptors=dict(
            input=report["original_input_reference"],
            output=report["original_output_reference"],
            guard_mean=report["original_guard_mean_reference"]),
        original_stage_exit_comparison=report["withJac_comparison_to_actual28"],
        original_stage_final_mean_state=report["final_mean_state"],
        complete_original_fields=fields,
        original_field_packet_source=packet["source"],
        full_226_states_are_not_reconstructed_from_hashes=True,
        copied_numberRecord_float64le_hex_is_authoritative=True,
        original_JSON_files_and_packet_hashes_preserved=True,
        selected_JSON_is_reserialized_not_claimed_original_raw_text=True,
        read_only_original_metadata=True,
        new_RHS_root_geometry_J_evaluations=0,
        new_RK_steps=0, new_norm_or_stability_parameter_calculations=0,
        no_gamma_xi_eigenvalue_or_threshold_computed=True,
        native_accepted=False, task_completed=False)
    encoded = (json.dumps(output, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode()
    require(len(encoded) <= 90000, "bounded small-text receipt at most90000bytes")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("xb") as stream:
        stream.write(encoded)
    print(json.dumps(dict(file=str(out), bytes=len(encoded), sha256=sha(encoded),
                          copied_original_fields=4, read_only_metadata=True)))


if __name__ == "__main__":
    main()
