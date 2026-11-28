"""First DCP18 publication, preserving the original entire worker gates."""
from pathlib import Path
import hashlib

BASE_NAME = "fourfold_codazzi_reflected_waist_rows_public_worker.py"
BASE_SHA256 = "9a474a43f065843af583edaab3bf774eddd845dab47a589aabe8cedcdd2b2490"

VALIDATOR = '''    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"], "one entire new DCP18 actual")
        doc = parse(raw)
        ident = doc["identity"]
        require(ident["kind"] == manifest["scientific_kind"] and ident["scalar_stage"] == manifest["stage"]
                and ident["manifest_sha256"] == args.manifest_sha
                and ident["source_sha256"] == by_role["science"]["sha256"]
                and ident["run_id"] == run and ident["run_attempt"] == attempt
                and ident["whole_BFP_actual_sha256"] == by_role["BFP_actual"]["sha256"]
                and ident["whole_WMT_actual_sha256"] == by_role["WMT_actual"]["sha256"]
                and doc["whole_BFP_parent_identity"] == manifest["complete_BFP_parent_identity"]
                and doc["whole_WMT_parent_identity"] == manifest["complete_WMT_parent_identity"],
                "the whole new actual and its genuinely completed original parent")
        count = doc["saved_record_count"]
        require(type(count) is int and 0 <= count <= 18
                and doc["completed_targets"] == manifest["target_order"][:count]
                and set(doc["new_records"]) == set(doc["completed_targets"])
                and sorted(doc) == manifest["allowed_scientific_fields"]
                and doc["parameters"] == manifest["parameters"]
                and doc["old_scientific_target_calls"] == 0
                and all(doc[name] == 0 for name in ("new_arrays_published", "new_artifacts", "new_Releases")),
                "all full fields, exact natural target prefix and zero old targets")
        for index in range(count):
            value = doc["new_records"][manifest["target_order"][index]]
            if index not in (15, 17):
                require(set(value) == {"ball", "bound"} and value["bound"] == "upper"
                        and isinstance(value["ball"], str), "one whole new scalar record")
            else:
                error_index = 14 if index == 15 else 16
                require(value["rows"] == len(value["all96_exact_signed_centers"])
                            == len(value["all96_signed_balls"]) == 96
                        and value["joint_l2_error_upper"] == doc["new_records"][manifest["target_order"][error_index]]
                        and value["same_complete_original_BFP512_reference"] is True
                        and value["all_true_target_source_and_root_phases_retained"] is True
                        and value["true_infinite_high_modes_set_to_zero"] is False
                        and value["old_low96_Theta_error_used_globally"] is False
                        and value["full_physical_Schur_claimed"] is False,
                        "all96 signed true-root coordinates with their whole joint error")
                if index == 17:
                    require(value["prior_two_independent_density_means"]
                                == doc["copied_complete_input_records"]["prior_two_independent_density_means"]
                            and value["whole_BFP_target_column_error"]
                                == doc["copied_complete_input_records"]["original_BFP_full_target_error"]
                            and value["whole_global_Theta_error"]
                                == doc["whole_global_Theta_choice"]["both_complete_candidates"][doc["whole_global_Theta_choice"]["selected"]]
                            and doc["whole_global_Theta_choice"]["same_original_Theta_and_trial"] is True
                            and doc["whole_global_Theta_choice"]["low96_error_used_globally"] is False,
                            "the complete original infinite-column error, global operator error and both means")
        if doc["complete"]:
            require(count == 18 and doc["proved"] is True and doc["actual_returncode"] == 0
                    and doc["failure"] is None and doc["current_target"] is None
                    and doc["result"]["true_entire_C_inverse_and_Krein_identity_used"] is True
                    and doc["result"]["complete_new_particular_Theta_reference_proved"] is True
                    and doc["result"]["complete_true_Theta_nu_column_proved"] is True
                    and doc["result"]["old_IR96_DWT96_or_Theta96_trial_restored"] is False
                    and doc["result"]["full_physical_Schur_proved"] is False
                    and doc["result"]["topic_completion_proved"] is False,
                    "all eighteen actually completed new targets with their exact scope")
        return doc

'''


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("the entire immutable publication engine changed")
    source = raw.decode()
    changes = {
        "R149_complete_reflected_finite_waist_row_inputs_v1": "R149_complete_particular_density_Theta_inputs_v1",
        '"reflected_finite_waist_rows"': '"particular_density_Theta"',
        'manifest["complete_record_counts"] == [96]': 'manifest["complete_record_counts"] == [18]',
        "one complete actual 96-row reflected-waist manifest": "one first complete DCP18 manifest",
        "actual-reflected-waist-rows": "actual-particular-density-Theta",
        "R149_complete_reflected_finite_waist_rows_execution_v1": "R149_complete_particular_density_Theta_execution_v1",
        "consumed_R149_complete_reflected_finite_waist_rows_target_v1": "consumed_R149_complete_particular_density_Theta_v1",
        "whole_actual_conjugacy_inputs_reserved_for_one_new_complete_96row_target": "whole_successful_BFP_inputs_reserved_for_eighteen_new_particular_Theta_targets",
        "visible-exact: reserve exact reflected waist ": "visible-exact: reserve complete particular density Theta ",
        "visible-exact: preserve exact reflected waist ": "visible-exact: preserve complete particular density Theta ",
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
            raise ValueError("the exact DCP engine adaptation did not match: "+old)
        source = source.replace(old, new)
    start = source.index("    require(len(history_specs) == 4\n")
    end = source.index("    marker_path =", start)
    source = source[:start]+'''    require(len(history_specs) == manifest["expected_historical_input_count"] == 53
            and op["readme_pull_interval_seconds"] == 1800
            and op["automatic_scientific_retry"] is False,
            "all complete original inputs, periodic rule checks and no old-target replay")
'''+source[end:]
    start = source.index("    def validate_output(raw):\n")
    end = source.index("    try:\n        head = pull()\n", start)
    source = source[:start]+VALIDATOR+source[end:]
    start = source.index("        report = (", source.index("    def final_files():"))
    end = source.index("        return {**staged", start)
    source = source[:start]+'''        report = ("# Actual complete particular density Theta receiver\\n\\nRun "+run+"/"+attempt
                  +"; complete: "+str(state["complete"])+".\\n\\n"
                  "The complete successful BFP reference, true source/target phases, original C energy-adjoint order and both physical means remain. "
                  "New signed direct density action and the entire opposite-sign leakage use the actual full Krein inverse. "
                  "Both alias rays, infinite tail, true-map and alpha products, and the original full BFP/global Theta error are paid. "
                  "No old IR96, DWT96, Theta96 or BFP scientific target is replayed. Full physical Schur and the exact closed family remain open.\\n").encode()

'''+source[end:]
    return source


if __name__ == "__main__":
    exec(compile(patched_source(), __file__, "exec"), {"__name__": "__main__", "__file__": __file__})
