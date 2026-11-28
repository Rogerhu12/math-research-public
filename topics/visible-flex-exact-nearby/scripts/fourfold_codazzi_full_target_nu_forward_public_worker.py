"""First complete BFP19 public execution; all old results stay immutable."""
from pathlib import Path
import hashlib

BASE_NAME = "fourfold_codazzi_reflected_waist_rows_public_worker.py"
BASE_SHA256 = "9a474a43f065843af583edaab3bf774eddd845dab47a589aabe8cedcdd2b2490"

VALIDATOR = '''    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"], "whole small new BFP19 actual")
        doc = parse(raw)
        ident = doc["identity"]
        require(ident["kind"] == manifest["scientific_kind"] and ident["scalar_stage"] == manifest["stage"]
                and ident["manifest_sha256"] == args.manifest_sha
                and ident["source_sha256"] == by_role["science"]["sha256"]
                and ident["run_id"] == run and ident["run_attempt"] == attempt,
                "the complete actual BFP identity")
        count = doc["saved_record_count"]
        require(type(count) is int and 0 <= count <= 19
                and doc["completed_targets"] == manifest["target_order"][:count]
                and set(doc["new_records"]) == set(doc["completed_targets"])
                and sorted(doc) == manifest["allowed_scientific_fields"]
                and doc["parameters"] == manifest["parameters"]
                and doc["old_scientific_target_calls"] == 0
                and all(doc[name] == 0 for name in ("new_arrays_published", "new_artifacts", "new_Releases")),
                "all entire new BFP fields and the actual complete target prefix")
        require(all(set(doc["new_records"][name]) == {"ball", "bound"}
                    and doc["new_records"][name]["bound"] == "upper"
                    and isinstance(doc["new_records"][name]["ball"], str)
                    for name in doc["completed_targets"][:18]), "all full directed scalar records")
        if count == 19:
            signed = doc["new_records"][manifest["target_order"][18]]
            require(signed["rows"] == 96 and len(signed["all96_exact_signed_centers"]) == 96
                    and len(signed["all96_true_signed_balls"]) == 96
                    and signed["true_infinite_source_or_output_high_modes_set_to_zero"] is False
                    and signed["original_full_Theta_error_used"] is True
                    and signed["low96_Theta_error_substituted"] is False
                    and signed["physical_mean_phase_height_Schur_claimed"] is False
                    and signed["joint_l2_error_upper"] == doc["new_records"][manifest["target_order"][17]]
                    and signed["whole_true_target_column_error_upper"] == doc["new_records"][manifest["target_order"][13]],
                    "the whole true signed96 column retains the global operator error and physical meanings")
        if doc["complete"]:
            require(count == 19 and doc["proved"] is True and doc["actual_returncode"] == 0
                    and doc["failure"] is None and doc["current_target"] is None
                    and doc["result"]["whole_forward_B_column_error_proved"] is True
                    and doc["result"]["whole_original_Theta_column_error_proved"] is True
                    and doc["result"]["full_homogeneous_inverse_or_physical_Schur_proved"] is False
                    and doc["result"]["topic_completion_proved"] is False,
                    "all nineteen complete new bounds with their precise scope")
        return doc

'''


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("the original whole publication engine changed")
    source = raw.decode()
    changes = {
        "R149_complete_reflected_finite_waist_row_inputs_v1": "R147_complete_full_target_nu_forward_inputs_v1",
        '"reflected_finite_waist_rows"': '"full_target_nu_forward"',
        'manifest["complete_record_counts"] == [96]': 'manifest["complete_record_counts"] == [19]',
        "one complete actual 96-row reflected-waist manifest": "one complete first BFP19 manifest",
        "actual-reflected-waist-rows": "actual-full-target-nu-forward",
        "R149_complete_reflected_finite_waist_rows_execution_v1": "R147_complete_full_target_nu_forward_execution_v1",
        "consumed_R149_complete_reflected_finite_waist_rows_target_v1": "consumed_R147_complete_full_target_nu_forward_v1",
        "whole_actual_conjugacy_inputs_reserved_for_one_new_complete_96row_target": "whole_original_BNC_and_UACT_inputs_reserved_for_nineteen_new_forward_targets",
        "visible-exact: reserve exact reflected waist ": "visible-exact: reserve nineteen new complete forward nu ",
        "visible-exact: preserve exact reflected waist ": "visible-exact: preserve nineteen new complete forward nu ",
        'destination = source_dir / (spec["role"] + Path(spec["path"]).suffix)':
            'destination = source_dir / ("input_" + spec["role"] + Path(spec["path"]).suffix)',
        'target = history_dir/(spec["role"]+".json.gz")': 'target = history_dir/topic_path(spec["path"])',
        '{item["role"]: item for item in specs+history_specs})':
            '{item["role"]: item for item in specs+history_specs}, manifest, snapshots)',
        'state["current_input_receipts"] = specs':
            'state["current_input_receipts"] = {"reconstruct_from": "whole manifest.files", "manifest_sha256": args.manifest_sha, "complete_count": len(specs), "complete_descriptors_sha256": sha(encode(specs))}',
    }
    for old, new in changes.items():
        if old not in source:
            raise ValueError("exact BFP engine adaptation did not match: "+old)
        source = source.replace(old, new)
    start = source.index("    require(len(history_specs) == 4\n")
    end = source.index("    marker_path =", start)
    source = source[:start]+'''    require(len(history_specs) == manifest["expected_historical_input_count"]
            and len(history_specs) >= 51 and op["readme_pull_interval_seconds"] == 1800
            and op["automatic_scientific_retry"] is False,
            "all original whole historical inputs, periodic rule checks and no target rerun")
'''+source[end:]
    start = source.index("    def validate_output(raw):\n")
    end = source.index("    try:\n        head = pull()\n", start)
    source = source[:start]+VALIDATOR+source[end:]
    start = source.index("        report = (", source.index("    def final_files():"))
    end = source.index("        return {**staged", start)
    source = source[:start]+'''        report = ("# Actual complete full target strict-nu forward column\\n\\nRun "+run+"/"+attempt
                  +"; complete: "+str(state["complete"])+".\\n\\n"
                  "The full512-mode trial, all2560 finite B images, all8192 pullback points and all96 original Theta pairings enter the new bounds. "
                  "Original global Theta errors, the complete true phase and both independent physical density means are retained. "
                  "No old norm, residual, BNC observation or certified target is recomputed. "
                  "Read the whole actual and execution together. Full homogeneous inverse, physical Schur and the exact closed family remain open.\\n").encode()

'''+source[end:]
    return source


if __name__ == "__main__":
    exec(compile(patched_source(), __file__, "exec"), {"__name__": "__main__", "__file__": __file__})
