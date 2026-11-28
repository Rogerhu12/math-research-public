"""One complete WMT14 public execution using the existing publication engine."""
from pathlib import Path
import hashlib

BASE_NAME = "fourfold_codazzi_reflected_waist_rows_public_worker.py"
BASE_SHA256 = "9a474a43f065843af583edaab3bf774eddd845dab47a589aabe8cedcdd2b2490"

VALIDATOR = '''    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"], "whole new WMT14 actual")
        doc = parse(raw)
        ident = doc["identity"]
        require(ident["kind"] == manifest["scientific_kind"] and ident["scalar_stage"] == manifest["stage"]
                and ident["manifest_sha256"] == args.manifest_sha
                and ident["source_sha256"] == by_role["science"]["sha256"]
                and ident["run_id"] == run and ident["run_attempt"] == attempt,
                "the entire actual WMT identity")
        count = doc["saved_record_count"]
        require(type(count) is int and 0 <= count <= 14
                and doc["completed_targets"] == manifest["target_order"][:count]
                and set(doc["new_records"]) == set(doc["completed_targets"])
                and sorted(doc) == manifest["allowed_scientific_fields"]
                and doc["parameters"] == manifest["parameters"]
                and doc["old_scientific_target_calls"] == 0
                and all(doc[name] == 0 for name in ("new_arrays_published", "new_artifacts", "new_Releases")),
                "all whole fields, exact new target prefix and zero old targets")
        require(all(set(value) == {"ball", "bound"} and value["bound"] == "upper"
                    and isinstance(value["ball"], str) for value in doc["new_records"].values()),
                "each whole directed new scalar record")
        if doc["complete"]:
            require(count == 14 and doc["proved"] is True and doc["actual_returncode"] == 0
                    and doc["failure"] is None and doc["current_target"] is None
                    and doc["complete_model_head_count"] == 1048576
                    and doc["whole_Theta_candidate_choice"]["low96_error_is_not_a_global_candidate"] is True
                    and doc["whole_Theta_candidate_choice"]["same_original_Theta_and_trial"] is True
                    and doc["result"]["whole_original_Theta_global_error_proved"] is True
                    and doc["result"]["BFP_actual_consumed_or_Theta_nu_column_claimed"] is False
                    and doc["result"]["full_physical_Schur_proved"] is False
                    and doc["result"]["topic_completion_proved"] is False,
                    "all fourteen complete whole-operator bounds with their precise scope")
        return doc

'''


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("the entire immutable publication engine changed")
    source = raw.decode()
    changes = {
        "R149_complete_reflected_finite_waist_row_inputs_v1": "R149_complete_weighted_model_Theta_receiver_inputs_v1",
        '"reflected_finite_waist_rows"': '"weighted_model_Theta_receiver"',
        'manifest["complete_record_counts"] == [96]': 'manifest["complete_record_counts"] == [14]',
        "one complete actual 96-row reflected-waist manifest": "one first whole WMT14 manifest",
        "actual-reflected-waist-rows": "actual-weighted-model-Theta-receiver",
        "R149_complete_reflected_finite_waist_rows_execution_v1": "R149_complete_weighted_model_Theta_receiver_execution_v1",
        "consumed_R149_complete_reflected_finite_waist_rows_target_v1": "consumed_R149_complete_weighted_model_Theta_receiver_v1",
        "whole_actual_conjugacy_inputs_reserved_for_one_new_complete_96row_target": "whole_original_UACT_inputs_reserved_for_fourteen_new_weighted_Theta_targets",
        "visible-exact: reserve exact reflected waist ": "visible-exact: reserve whole weighted model Theta ",
        "visible-exact: preserve exact reflected waist ": "visible-exact: preserve whole weighted model Theta ",
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
            raise ValueError("exact WMT engine adaptation did not match: "+old)
        source = source.replace(old, new)
    start = source.index("    require(len(history_specs) == 4\n")
    end = source.index("    marker_path =", start)
    source = source[:start]+'''    require(len(history_specs) == manifest["expected_historical_input_count"] == 6
            and op["readme_pull_interval_seconds"] == 1800
            and op["automatic_scientific_retry"] is False,
            "all original whole inputs, periodic rule checks and no old-target replay")
'''+source[end:]
    start = source.index("    def validate_output(raw):\n")
    end = source.index("    try:\n        head = pull()\n", start)
    source = source[:start]+VALIDATOR+source[end:]
    start = source.index("        report = (", source.index("    def final_files():"))
    end = source.index("        return {**staged", start)
    source = source[:start]+'''        report = ("# Actual complete weighted-model Theta receiver\\n\\nRun "+run+"/"+attempt
                  +"; complete: "+str(state["complete"])+".\\n\\n"
                  "The same original IR trial, full new8192-grid derivative residual, all four signed Grams and the complete model head/tail are retained. "
                  "Both old and new global Theta candidates remain whole; low96 error is not used as a global bound. "
                  "No original IR99, UACT21, Cayley gap, AS/SN or BFP target is rerun. "
                  "Only the entire successful actual and execution can supply the new bound to a later complete BFP receipt consumer. "
                  "Full physical Schur and the exact closed family remain open.\\n").encode()

'''+source[end:]
    return source


if __name__ == "__main__":
    exec(compile(patched_source(), __file__, "exec"), {"__name__": "__main__", "__file__": __file__})
