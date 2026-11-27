"""First full-space original target-B inverse96 rows on the public engine.

The whole completed BW carrier/error is admitted before reservation.
Only one new row trial and all of its2240-mode residuals are certified;
the full true-w error and both product candidates remain in the result.
"""
from pathlib import Path
import hashlib

BASE_NAME = "fourfold_codazzi_reflected_waist_rows_public_worker.py"
BASE_SHA256 = "9a474a43f065843af583edaab3bf774eddd845dab47a589aabe8cedcdd2b2490"

VALIDATOR = '''    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"], "whole complete original target-B row result")
        doc = parse(raw)
        identity = doc["identity"]
        require(identity["kind"] == manifest["scientific_kind"]
                and identity["scalar_stage"] == manifest["stage"]
                and identity["source_sha256"] == by_role["science"]["sha256"]
                and identity["manifest_sha256"] == args.manifest_sha
                and identity["run_id"] == run and identity["run_attempt"] == attempt
                and identity["arithmetic_bits"] == 320
                and all(identity[role+"_sha256"] == by_role[role]["sha256"]
                    for role in ("BW_actual", "BW_execution", "BW_manifest", "BR_math", "proposal")),
                "the complete same BW parent and all seven new inverse-row targets")
        count, rows = doc["saved_record_count"], doc["complete_residual_row_count"]
        require(type(count) is int and 0 <= count <= 7 and type(rows) is int and 0 <= rows <= 96
                and doc["completed_targets"] == manifest["target_order"][:count]
                and set(doc["new_records"]) == set(doc["completed_targets"])
                and doc["parameters"] == manifest["parameters"]
                and sorted(doc) == manifest["allowed_scientific_fields"]
                and doc["old_scientific_target_calls"] == 0
                and doc["necessary_carrier_rematerializations"] in (0, 1)
                and doc["new_arrays_published"] == doc["new_artifacts"] == doc["new_Releases"] == 0,
                "all complete residual rows and saved scalars without old target replay")
        for record in doc["new_records"].values():
            require(set(record) == {"ball", "bound"} and record["bound"] == "upper"
                    and isinstance(record["ball"], str), "one whole new formal row upper")
        if rows or count:
            restored = doc["carrier_restoration"]
            require(doc["necessary_carrier_rematerializations"] == 1
                    and restored["complete"] is True and restored["failure"] is None
                    and restored["result"]["complete"] is True
                    and restored["result"]["whole_original_SHA_required"] is True
                    and restored["result"]["old_scientific_target_calls"] == 0
                    and restored["result"]["CORETYPE"] == "unset"
                    and doc["private_trial_receipt"]["bytes"] == 294912
                    and doc["private_trial_receipt"]["shape"] == [192, 96, 2]
                    and doc["private_row_trial_receipt"]["rows"] == 96
                    and doc["private_row_trial_receipt"]["positive_modes"] == 192
                    and doc["private_row_trial_receipt"]["exact_mean"] == "0"
                    and doc["private_row_trial_receipt"]["negative_modes_are_exact_conjugates"] is True
                    and isinstance(doc["complete_true_phase_a_ball"], str),
                    "original signed w and full true phase precede every new whole residual")
        if count:
            residual = doc["private_residual_receipt"]
            require(rows == 96 and residual["rows"] == 96 and residual["positive_modes"] == 2240
                    and residual["all_finite_tail_outputs193_through2240_retained"] is True
                    and residual["negative_modes_are_exact_conjugates"] is True
                    and residual["true_phase_and_all_finite_rounding_enclosed"] is True,
                    "all96x2240 signed finite residuals before each scalar conclusion")
        if doc["complete"]:
            result = doc["result"]
            require(doc["proved"] is True and doc["actual_returncode"] == 0 and doc["failure"] is None
                    and count == 7 and rows == 96 and doc["candidate_record"] is doc["current_target"] is None
                    and doc["stage"] == "complete_"+manifest["stage"]+"_branch"
                    and result["complete_new_record_order"] == doc["completed_targets"]
                    and result["complete_new_record_count"] == 7 and result["complete_true_inverse_row_count"] == 96
                    and result["complete_finite_residual_positive_modes"] == 2240,
                    "all seven whole bounds and the complete true inverse96-row enclosure")
            choice = doc["complete_product_choice"]
            require(choice["candidate_order"] == manifest["target_order"][3:5]
                    and choice["selected"] in choice["candidate_order"]
                    and choice["selected_whole_upper"] == doc["new_records"][choice["selected"]]
                    and choice["selection_on_complete_saved_records"] is True,
                    "both whole w-error product candidates are retained before taking the smaller bound")
            require(all(result[key] is True for key in (
                "same_original_target_B_and_same_sign_projection_order",
                "whole_original_BW_carriers_restored_with_all_SHA",
                "all96_true_original_B_inverse_rows_enclosed_in_full_L2",
                "whole_space_energy_inverse_onto_and_norm_one_used",
                "true_target_phase_and_all_exact_rational_row_trials_retained",
                "all2240_outputs_and_complete_w_infinite_error_paid",
                "both_whole_w_product_candidates_saved_before_selection",
                "all_signed_residual_balls_saved_and_read"))
                and all(result[key] is False for key in (
                "old_BW_ASR_cohomology_norm_or_transport_targets_recomputed",
                "extra_sqrt96_applied_to_joint_row_error", "physical_mean_slots_eliminated",
                "finite_Galerkin_solve_used_as_full_inverse_certificate",
                "SC_raw96_pairings_used_as_full_physical_columns",
                "physical_PDE_or_full_Schur_proved", "topic_completion_proved")),
                "full-space row error only, retaining both means and all physical PDE obligations")
        return doc

'''

PERIODIC = '''                        pull()
                        if output.exists():
                            complete_prefix = output.read_bytes()
                            prefix_doc = validate_output(complete_prefix)
                            digest_now = sha(complete_prefix)
                            if digest_now != state.get("last_published_complete_prefix_sha256"):
                                staged[output_dir+"/"+output_name] = complete_prefix
                                state["last_published_complete_prefix_sha256"] = digest_now
                                state["last_published_complete_residual_rows"] = prefix_doc["complete_residual_row_count"]
                                state["partial_prefix_publication_count"] = state.get("partial_prefix_publication_count", 0)+1
                                state["scientific_files"] = [dict(path=p, bytes=len(b), sha256=sha(b))
                                                               for p, b in staged.items()]
                                def prefix_files():
                                    receipt = encode(state)
                                    require(len(receipt) <= op["maximum_execution_bytes"], "whole BR prefix receipt")
                                    return {**staged, output_dir+"/execution.json": receipt}
                                publish(prefix_files, "visible-exact: preserve complete original B inverse-row prefix")
'''

REPORT = '''        report = ("# Actual original target-B inverse96 rows\\n\\nRun "+run+"/"+attempt
                  +"; complete: "+str(state["complete"])+".\\n\\n"
                  "The entire successful BW actual and original ASR closure precede the new target. "
                  "One carrier-only child requires the original whole endpoint, raw, grid, alpha, "
                  "quadrature, vi and w hashes; it repeats no completed error or norm. The new "
                  "192-mode trial supplies all96 rows of E96_a* B^-1 for the original B=Id+T_w I. "
                  "Every signed output through2240 and the whole infinite true-w error are paid. "
                  "The original full-space energy inverse gives the joint full-L2 row enclosure. "
                  "Both physical means remain independent. Raw96 pairings alone are not full "
                  "physical columns; the physical PDE and full Schur obligations remain.\\n").encode()

'''


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("the whole immutable public publication engine changed")
    source = raw.decode()
    changes = {
        "R149_complete_reflected_finite_waist_row_inputs_v1": "R149_complete_original_target_B_inverse_rows_inputs_v1",
        '"reflected_finite_waist_rows"': '"original_target_B_inverse_rows"',
        'manifest["complete_record_counts"] == [96]': 'manifest["complete_record_counts"] == [7]',
        "one complete actual 96-row reflected-waist manifest": "one complete original target-B inverse96-row manifest",
        "actual-reflected-waist-rows": "actual-original-target-B-inverse-rows",
        "R149_complete_reflected_finite_waist_rows_execution_v1": "R149_complete_original_target_B_inverse_rows_execution_v1",
        "consumed_R149_complete_reflected_finite_waist_rows_target_v1": "consumed_R149_complete_original_target_B_inverse_rows_target_v1",
        "whole_actual_conjugacy_inputs_reserved_for_one_new_complete_96row_target": "whole_successful_BW_reserved_for_first_complete_original_B_inverse_rows",
        "visible-exact: reserve exact reflected waist ": "visible-exact: reserve original target B inverse rows ",
        "visible-exact: preserve exact reflected waist ": "visible-exact: preserve original target B inverse rows ",
        'destination = source_dir / (spec["role"] + Path(spec["path"]).suffix)':
            'destination = source_dir / ("input_" + spec["role"] + Path(spec["path"]).suffix)',
        '{item["role"]: item for item in specs+history_specs})':
            '{item["role"]: item for item in specs+history_specs}, manifest)',
    }
    for old, new in changes.items():
        if old not in source:
            raise ValueError("the complete original B-row adaptation did not match: "+old)
        source = source.replace(old, new)
    start = source.index("    require(len(history_specs) == 4\n")
    end = source.index("    marker_path =", start)
    source = source[:start]+'''    require(history_specs == []
            and op["readme_pull_interval_seconds"] == 1800
            and op["automatic_scientific_retry"] is False,
            "the original whole BW/ASR closure is inherited without another native source set")
'''+source[end:]
    start = source.index("    def validate_output(raw):\n")
    end = source.index("    try:\n        head = pull()\n", start)
    source = source[:start]+VALIDATOR+source[end:]
    old = "                        pull()\n                    except BaseException as exc:\n"
    if source.count(old) != 1:
        raise ValueError("the original unique periodic rule-check block changed")
    source = source.replace(old, PERIODIC+"                    except BaseException as exc:\n")
    old = '    state["finished_utc"] = utc()\n'
    if source.count(old) != 1:
        raise ValueError("the original final receipt block changed")
    source = source.replace(old, '''    state["old_numerical_producers_called"] = (result or {}).get("necessary_carrier_rematerializations", 0)
    state["necessary_original_BW_carrier_restoration"] = (result or {}).get("carrier_restoration")
    state["complete_new_residual_rows"] = (result or {}).get("complete_residual_row_count", 0)
'''+old)
    start = source.index("        report = (", source.index("    def final_files():"))
    end = source.index("        return {**staged", start)
    source = source[:start]+REPORT+source[end:]
    return source


if __name__ == "__main__":
    exec(compile(patched_source(), __file__, "exec"), {"__name__": "__main__", "__file__": __file__})
