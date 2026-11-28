"""Publish each exact saved-column consequence once with the whole old gates."""
from pathlib import Path
import hashlib

BASE_NAME = "fourfold_codazzi_reflected_waist_rows_public_worker.py"
BASE_SHA256 = "9a474a43f065843af583edaab3bf774eddd845dab47a589aabe8cedcdd2b2490"

VALIDATOR = '''    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"], "one complete small saved-column actual")
        doc = parse(raw)
        ident, mode = doc["identity"], manifest["mode"]
        require(ident["kind"] == manifest["scientific_kind"] and ident["scalar_stage"] == manifest["stage"]
                and ident["mode"] == mode and ident["manifest_sha256"] == args.manifest_sha
                and ident["source_sha256"] == by_role["science"]["sha256"]
                and ident["run_id"] == run and ident["run_attempt"] == attempt
                and doc["whole_parent_receipts"] == manifest["whole_successful_parent_receipts"],
                "the exact new actual and both complete genuine original parents")
        count = doc["saved_record_count"]
        total = len(manifest["target_order"])
        require(type(count) is int and 0 <= count <= total
                and doc["completed_targets"] == manifest["target_order"][:count]
                and set(doc["new_records"]) == set(doc["completed_targets"])
                and sorted(doc) == manifest["allowed_scientific_fields"]
                and doc["parameters"] == manifest["parameters"] and doc["runtime"] == manifest["runtime"]
                and doc["old_scientific_target_calls"] == 0
                and all(doc[name] == 0 for name in ("new_arrays_published", "new_artifacts", "new_Releases")),
                "all full fields, natural completed prefix and no old scientific target")
        if count == total:
            body = doc["new_records"][manifest["target_order"][-1]]
            name = "BFP" if mode == "WBN" else "BNC"
            old_order = manifest["original_parent_target_orders"][name]
            group = "all_complete_original_BFP_scalar_and_signed_records" if mode == "WBN" else "all_complete_original_BNC_scalar_and_signed_records"
            source_name = "all96_exact_signed_centers" if mode == "WBN" else "all96_exact_signed_trial_rationals"
            old = body[group]
            centers = old[old_order[-1]][source_name]
            selected = body["new_signed_conclusion"]
            canonical_centers = (json.dumps(centers, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)+"\\n").encode()
            require(set(old) == set(old_order) and len(centers) == selected["rows"] == 96
                    and all(isinstance(value, str) for value in centers)
                    and selected["whole_center_array_sha256"] == sha(canonical_centers)
                    and selected["all_exact_centers_inherited_verbatim_from"] == group+"/"+old_order[-1]+"/"+source_name
                    and selected["each_real_coordinate_enclosed_by_its_exact_center_plus_minus_joint_error"] is True
                    and body["parent_receipts"] == {tag+str(receipt["all_original_targets_admitted"]): receipt
                            for tag, receipt in doc["whole_parent_receipts"].items()}
                    and body["complete"] is body["proved"] is True
                    and body["full_physical_Schur_proved"] is body["topic_completion_proved"] is False,
                    "all96 original exact centers stored once, whole parents and the new joint enclosure")
            mean_name = "prior_two_independent_density_means" if mode == "WBN" else "prior_two_independent_density_mean_balls"
            require(body["prior_two_independent_density_means"] == old[old_order[-1]][mean_name],
                    "both entire independent physical means copied verbatim")
            if mode == "WBN":
                require(body["changed_global_slot_only"] is True and body["low96_error_used_globally"] is False
                        and body["old_scientific_targets_recomputed"] == 0,
                        "only the one qualified complete global Theta slot changes")
            else:
                require(body["new_records"][manifest["target_order"][0]] == doc["new_records"][manifest["target_order"][0]]
                        and body["all_four_unchanged_original_fees"] == {key: old[key] for key in old_order[1:5]}
                        and body["whole_five_fee_positive_formula_preserved"] is True
                        and body["old_successful_targets_recomputed"] == 0
                        and body["old_upper_subtracted"] is body["different_Theta_nu_column_claimed"] is False,
                        "the new saved row fee and all four whole original unchanged fees")
        if doc["complete"]:
            require(count == total and doc["proved"] is True and doc["actual_returncode"] == 0
                    and doc["failure"] is None and doc["current_target"] is None
                    and doc["result"]["complete_new_record_count"] == total
                    and doc["result"]["all96_exact_centers_and_joint_error_preserved"] is True
                    and doc["result"]["both_independent_physical_means_retained"] is True
                    and doc["result"]["old_carriers_rematerialized"] is False
                    and doc["result"]["full_physical_Schur_proved"] is doc["result"]["topic_completion_proved"] is False,
                    "the entire newly completed saved-column consequence and its exact scope")
        return doc

'''


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("the entire immutable original publication engine changed")
    source = raw.decode()
    changes = {
        "R149_complete_reflected_finite_waist_row_inputs_v1": "R149_complete_saved_column_consequence_inputs_v1",
        '"reflected_finite_waist_rows"': '"saved_column_consequence"',
        'manifest["complete_record_counts"] == [96]': 'manifest["complete_record_counts"] in ([1], [2])',
        "one complete actual 96-row reflected-waist manifest": "one complete exact saved-column consequence manifest",
        "actual-reflected-waist-rows": "actual-saved-column-consequence",
        "R149_complete_reflected_finite_waist_rows_execution_v1": "R149_complete_saved_column_consequence_execution_v1",
        "consumed_R149_complete_reflected_finite_waist_rows_target_v1": "consumed_R149_complete_saved_column_consequence_v1",
        "whole_actual_conjugacy_inputs_reserved_for_one_new_complete_96row_target": "whole_successful_parent_results_reserved_for_one_new_saved_column_consequence",
        "visible-exact: reserve exact reflected waist ": "visible-exact: reserve complete saved column ",
        "visible-exact: preserve exact reflected waist ": "visible-exact: preserve complete saved column ",
        'destination = source_dir / (spec["role"] + Path(spec["path"]).suffix)':
            'destination = source_dir / ("input_" + spec["role"] + Path(spec["path"]).suffix)',
        '{item["role"]: item for item in specs+history_specs})':
            '{item["role"]: item for item in specs+history_specs}, manifest, snapshots)',
    }
    for old, new in changes.items():
        if old not in source:
            raise ValueError("the complete exact saved-column adaptation did not match: "+old)
        source = source.replace(old, new)
    start = source.index("    require(len(history_specs) == 4\n")
    end = source.index("    marker_path =", start)
    source = source[:start]+'''    require(history_specs == [] and manifest["expected_historical_input_count"] == 0
            and op["readme_pull_interval_seconds"] == 1800
            and op["automatic_scientific_retry"] is False,
            "only whole current saved results, periodic rule checks and no old target replay")
'''+source[end:]
    start = source.index("    def validate_output(raw):\n")
    end = source.index("    try:\n        head = pull()\n", start)
    source = source[:start]+VALIDATOR+source[end:]
    start = source.index("        report = (", source.index("    def final_files():"))
    end = source.index("        return {**staged", start)
    source = source[:start]+'''        report = ("# Actual whole saved-column consequence\\n\\nRun "+run+"/"+attempt
                  +"; mode: "+manifest["mode"]+"; complete: "+str(state["complete"])+".\\n\\n"
                  "Both entire successful parents and original validators were admitted before new exact rational arithmetic. "
                  "All96 exact signed centers are preserved once with the complete new joint radius and both original physical means. "
                  "WBN changes only the same global Theta slot. GBN changes only the complete row fee and retains all four other whole fees. "
                  "No old scientific target or carrier is recomputed. Full physical Schur and the closed nonlinear family remain open.\\n").encode()

'''+source[end:]
    return source


if __name__ == "__main__":
    exec(compile(patched_source(), __file__, "exec"), {"__name__": "__main__", "__file__": __file__})
