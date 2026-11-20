"""Four new actual G_H responses from whole completed scalar certificates.

No old producer, coefficient context, Green action, or saved target is run.
Only the four explicitly declared scalar combinations below are new science.
All numerical imports occur after whole-file and same-operator admission.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
import traceback

REPO = "Rogerhu12/math-research-public"
KIND = "complete_actual_GH_saved_Hthird_head_response_v1"
SOURCE_KIND = "complete_actual_GH_Hthird_source_fees_v1"
SOURCE_RUN = "44736533396"
SOURCE_MANIFEST_SHA = "69449ea01bbdfc202d6a6c763661a13f42efdcb08303fd356b1b32dc2f09887f"
RECORD_NAMES = [
    "actual_GH_raw_L2_from_complete_head_upper",
    "actual_GH_body_Z_sup_from_complete_head_upper",
    "actual_GH_root_outgoing_Z_from_complete_head_upper",
    "actual_GH_outer_even_Hminus5over6_from_complete_head_upper",
]
OLD_RECORD_NAMES = [
    "complete_centre_BHL_Hthird_collar_upper",
    "complete_centre_BHL_Hthird_body_upper",
    "complete_family_BHL_Hthird_collar_upper",
    "complete_family_BHL_Hthird_body_upper",
    "complete_family_BLH_raw_L2_upper",
]
OLD_TARGET_NAMES = [name.removesuffix("_upper") for name in OLD_RECORD_NAMES]
PARAMETERS = {"arithmetic_bits": 320, "decimal_record_digits": 75,
              "maximum_scientific_wall_seconds": 600,
              "new_target_count": 4, "new_record_count": 4,
              "old_completed_target_calls": 0,
              "original_source_window": "ordinary_dr_L2_Hphi_one_third",
              "ordinary_radial_measure": "dr", "normalised_angular_measure": True,
              "high_unknown_truncated": False,
              "outer_even_trace_factor": "5/388"}
SCI_FIELDS = sorted([
    "identity", "complete", "proved", "actual_returncode", "failure", "stage",
    "completed_targets", "current_target", "new_records", "saved_record_count",
    "parameters", "scope", "whole_completed_inputs", "whole_given_head_high_graphs",
    "reference_identity", "old_scientific_target_calls", "new_arrays_published",
    "new_artifacts", "new_Releases", "wall_seconds", "runtime",
])


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def git_blob(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False) + "\n").encode()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def atomic(path, raw):
    temporary = path.with_name(path.name + ".partial")
    with temporary.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)
    require(path.read_bytes() == raw, "whole new scalar prefix exact byte readback")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--input-map", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--checkout", required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO,
            "new numerical combinations only in this public Actions repository")
    manifest_raw = args.manifest.read_bytes()
    require(digest(manifest_raw) == args.manifest_sha, "whole pinned new consumer manifest")
    manifest = parse(manifest_raw)
    require(manifest["scientific_kind"] == KIND and manifest["parameters"] == PARAMETERS,
            "exact four new finite scalar targets")
    specs = {item["role"]: item for item in manifest["files"]}
    paths = parse(args.input_map.read_bytes())
    require(set(paths) == set(specs), "all complete current input snapshots")
    complete_bytes = {}
    for role, item in specs.items():
        raw = Path(paths[role]).read_bytes()
        require(0 < len(raw) < 100000 and len(raw) == item["bytes"]
                and digest(raw) == item["sha256"] and git_blob(raw) == item["git_blob_sha"],
                "whole input byte identity: " + role)
        complete_bytes[role] = raw
    require(digest(Path(__file__).read_bytes()) == specs["science"]["sha256"],
            "the exact publicly pinned numerical source")
    old = parse(complete_bytes["completed_five_sources"])
    old_execution = parse(complete_bytes["completed_five_sources_execution"])
    old_manifest = parse(complete_bytes["completed_five_sources_manifest"])
    require(digest(complete_bytes["completed_five_sources_manifest"]) == SOURCE_MANIFEST_SHA
            and old["kind"] == SOURCE_KIND and old["complete"] is True
            and old["proved"] is True and old["failure"] is None
            and old["actual_returncode"] == 0 and old["run_id"] == SOURCE_RUN
            and old["run_attempt"] == "1" and old["manifest_sha256"] == SOURCE_MANIFEST_SHA
            and old_execution["scientific_complete"] is True
            and old_execution["failure"] is None and old_execution["actual_child_returncode"] == 0
            and old_execution["run_id"] == SOURCE_RUN and old_execution["run_attempt"] == "1"
            and old_execution["manifest_sha256"] == SOURCE_MANIFEST_SHA
            and old_execution["scientific_children"] == 1
            and old_execution["completed_old_targets_recomputed"] == 0,
            "the one whole completed actual five-source computation and execution")
    matching = [item for item in old_execution["scientific_files"]
                if item["path"] == specs["completed_five_sources"]["path"]]
    require(len(matching) == 1 and matching[0]["bytes"] == len(complete_bytes["completed_five_sources"])
            and matching[0]["sha256"] == digest(complete_bytes["completed_five_sources"]),
            "old process identifies this entire actual scientific conclusion")
    require(old["completed_targets"] == OLD_TARGET_NAMES and old["saved_record_count"] == 5
            and set(old["new_records"]) == set(OLD_RECORD_NAMES)
            and old["source_comparison"]["complete_five_source_rates_proved"] is True
            and old["source_comparison"]["ordinary_Hthird_source_window"] is True
            and old["source_comparison"]["actual_GH_not_replaced_by_finite_F"] is True
            and old["return_parameters"]["same_actual_eta_and_original_S_inverse"] is True
            and old["return_parameters"]["comparison_panel_count"] == 155
            and old["return_parameters"]["original_parent_count"] == 153
            and old["return_parameters"]["full_family_mean_input_retained"] is True
            and old["return_parameters"]["actual_unknown_high_truncated"] is False,
            "all five complete source records and their exact whole-space qualification")
    for flag in ("actual_low_high_inverse_proved", "actual_physical_outer_rows_proved",
                 "complete_low_CFB_inverse_proved", "original_finite_rho_bridge_proved",
                 "original_seven_input_ports_proved", "either_original_RHS_proved",
                 "topic_completion_proved"):
        require(old["source_comparison"][flag] is False, "retain the original unpaid gate: " + flag)
    original_specs = {item["role"]: item for item in old_manifest["files"]}
    role_map = {"original_high_admission": "actual_GH_source_fees_math",
                "base0_summary": "completed_actual_base0_high_summary",
                "base0_process": "completed_actual_base0_high_process",
                "negative_summary": "negative_one_summary",
                "negative_process": "negative_one_process"}
    for role, previous in role_map.items():
        for name in ("path", "bytes", "sha256", "git_blob_sha"):
            require(specs[role][name] == original_specs[previous][name],
                    "the identical whole old high object: " + role + "/" + name)
    module_spec = importlib.util.spec_from_file_location(
        "_unchanged_actual_GH_metadata_admission", paths["original_high_admission"])
    require(module_spec is not None and module_spec.loader is not None, "pure old admission module")
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    base0, base_process = parse(complete_bytes["base0_summary"]), parse(complete_bytes["base0_process"])
    negative, negative_process = parse(complete_bytes["negative_summary"]), parse(complete_bytes["negative_process"])
    module.admit_original_high_reports(base0, base_process, negative, negative_process,
                                      specs["base0_summary"], specs["negative_summary"])
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "all metadata and complete old reports admitted before numerical imports")
    run, attempt = os.environ["GITHUB_RUN_ID"], os.environ["GITHUB_RUN_ATTEMPT"]
    require(attempt == "1" and not args.output.exists(), "one new never-overwritten target occurrence")
    args.output.parent.mkdir(parents=True, exist_ok=True)

    def reference(role):
        return {"file": copy.deepcopy(specs[role]), "json_path": [],
                "whole_prior_conclusion_and_all_scopes_retained": True}

    document = {
        "identity": {"kind": KIND, "source_sha256": specs["science"]["sha256"],
            "manifest_sha256": args.manifest_sha, "run_id": run, "run_attempt": attempt,
            "event_commit": os.environ["GITHUB_SHA"], "actual_checkout_commit": args.checkout,
            "completed_five_source_sha256": specs["completed_five_sources"]["sha256"],
            "original_base0_summary_sha256": specs["base0_summary"]["sha256"],
            "original_negative_summary_sha256": specs["negative_summary"]["sha256"],
            "arithmetic_bits": PARAMETERS["arithmetic_bits"]},
        "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "whole_completed_inputs_admitted", "completed_targets": [],
        "current_target": None, "new_records": {}, "saved_record_count": 0,
        "parameters": copy.deepcopy(PARAMETERS), "runtime": {},
        "whole_completed_inputs": {role: reference(role) for role in
            ("completed_five_sources", "completed_five_sources_execution", "completed_five_sources_manifest")},
        "whole_given_head_high_graphs": {role: reference(role) for role in
            ("base0_summary", "base0_process", "negative_summary", "negative_process")},
        "reference_identity": copy.deepcopy(old["reference_identity"]),
        "old_scientific_target_calls": 0, "new_arrays_published": 0,
        "new_artifacts": 0, "new_Releases": 0, "wall_seconds": 0.0,
        "scope": {"actual_complete_head_to_high_response_proved": False,
            "all_independent_high_ports_zero_only_in_this_homogeneous_head_response": True,
            "all_original_seven_port_and_exterior_mean_affine_rows_retained": True,
            "ordinary_Hthird_source_window": True, "actual_GH_not_finite_F": True,
            "entire_high_family_in_GH": True, "true_root_and_outer_frame_trace_used": True,
            "actual_unknown_high_truncated": False, "arbitrary_L2_trace_taken": False,
            "old_five_source_targets_recomputed": False, "old_high_graph_targets_recomputed": False,
            "low_inverse_or_receivers_evaluated": False, "low_family_target_evaluated": False,
            "actual_internal_feedback_inverse_proved": False,
            "actual_physical_outer_rows_proved": False, "complete_low_CFB_inverse_proved": False,
            "original_finite_rho_bridge_proved": False, "original_seven_input_ports_proved": False,
            "either_original_RHS_proved": False, "topic_completion_proved": False}}
    require(sorted(document) == SCI_FIELDS, "complete declared small scalar schema")
    began = time.perf_counter()

    def save():
        document["wall_seconds"] = time.perf_counter() - began
        raw = canonical(document)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"], "whole scalar prefix budget")
        atomic(args.output, raw)

    save()
    try:
        import flint
        import platform
        from importlib.metadata import version
        runtime = {"python": platform.python_version(), "packages": {"python-flint": version("python-flint")}}
        require(runtime == manifest["runtime"], "same completed public fixed directed runtime")
        document["runtime"] = runtime
        flint.ctx.prec = PARAMETERS["arithmetic_bits"]
        arb = flint.arb

        def upper(value):
            require(value.is_finite(), "finite complete directed scalar")
            point = value.upper()
            require(point.lower() >= 0, "nonnegative mathematical upper endpoint")
            return point

        def old_upper(record):
            require(isinstance(record, dict) and isinstance(record.get("ball"), str),
                    "whole original saved scalar ball")
            value = arb(record["ball"])
            if "lower" in record or "upper" in record:
                require(isinstance(record.get("lower"), str) and isinstance(record.get("upper"), str),
                        "both complete original endpoint strings")
                # Original record3/record5 semantics, including their display radii.
                value = arb(record["lower"]).lower().union(arb(record["upper"]).upper())
            return upper(value)

        def emit(name, value):
            require(RECORD_NAMES[document["saved_record_count"]] == name,
                    "declared four whole scalar records in exact order")
            original_upper = upper(value)
            record = {"ball": original_upper.str(PARAMETERS["decimal_record_digits"])}
            document["new_records"][name] = record
            document["saved_record_count"] += 1
            document["completed_targets"].append(name)
            document["current_target"] = None
            document["stage"] = "complete_new_scalar_record_saved"
            save()
            reread = parse(args.output.read_bytes())["new_records"][name]
            require(reread == record and arb(reread["ball"]).contains(original_upper),
                    "published whole decimal ball contains the original directed upper")
            print(canonical({"new_record_saved": name,
                             "completed_new_targets": document["saved_record_count"]}).decode(), end="", flush=True)
            return old_upper(reread)

        bc = upper(old_upper(old["new_records"][OLD_RECORD_NAMES[0]])
                   + old_upper(old["new_records"][OLD_RECORD_NAMES[2]]))
        bb = upper(old_upper(old["new_records"][OLD_RECORD_NAMES[1]])
                   + old_upper(old["new_records"][OLD_RECORD_NAMES[3]]))
        saved = {}
        for name, row_name in zip(RECORD_NAMES[:3],
                ("entire_positive_raw_L2", "body_Z_sup", "full_root_outgoing_unstable_port")):
            require(time.perf_counter() - began <= PARAMETERS["maximum_scientific_wall_seconds"],
                    "fixed four-target wall cap, complete prefix preserved")
            document["current_target"] = name
            save()
            row = base0["response_rows"][row_name]
            require(len(row) == 7, "the complete actual seven-column high response row")
            collar = upper(old_upper(row[1]) * bc)
            body = upper(old_upper(row[2]) * bb)
            square = upper(collar * collar + body * body)
            saved[name] = emit(name, upper(square.sqrt()))
        document["current_target"] = RECORD_NAMES[3]
        save()
        emit(RECORD_NAMES[3], upper((arb(5) / arb(388)) * saved[RECORD_NAMES[1]]))
        require(document["completed_targets"] == RECORD_NAMES
                and document["saved_record_count"] == 4, "all four new whole scalar conclusions")
        document["scope"]["actual_complete_head_to_high_response_proved"] = True
        document.update(complete=True, proved=True, actual_returncode=0, failure=None,
                        stage="complete_actual_GH_saved_head_response")
        save()
        return 0
    except BaseException as error:
        document.update(complete=False, proved=False, actual_returncode=1,
                        failure={"type": type(error).__name__, "message": str(error)[:2000],
                                 "traceback": traceback.format_exc()[:8000]},
                        stage="incomplete_new_scalar_response")
        save()
        raise


if __name__ == "__main__":
    raise SystemExit(main())
