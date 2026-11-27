"""Public DWT2 then BR7 on the immutable whole-result publication engine.

The complete ASR parent is admitted before one necessary original-grid
restoration. Both direct-w errors precede the first complete inverse rows.
"""
from pathlib import Path
import hashlib

BASE_NAME = "fourfold_codazzi_reflected_waist_rows_public_worker.py"
BASE_SHA256 = "9a474a43f065843af583edaab3bf774eddd845dab47a589aabe8cedcdd2b2490"

VALIDATOR = '''    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"], "whole complete DWT2 and original BR7 result")
        doc = parse(raw)
        identity = doc["identity"]
        require(identity["kind"] == manifest["scientific_kind"]
                and identity["scalar_stage"] == manifest["stage"]
                and identity["source_sha256"] == by_role["science"]["sha256"]
                and identity["manifest_sha256"] == args.manifest_sha
                and identity["run_id"] == run and identity["run_attempt"] == attempt
                and identity["arithmetic_bits"] == 320
                and all(identity[role+"_sha256"] == by_role[role]["sha256"]
                    for role in ("AS_actual", "AS_execution", "AS_manifest", "BR_math", "proposal",
                                 "DWT_math", "UDR_math", "grid_restore")),
                "the complete original ASR parent and all nine first direct-w/row targets")
        count, rows, modes = doc["saved_record_count"], doc["complete_residual_row_count"], doc["complete_w_mode_count"]
        require(type(count) is int and 0 <= count <= 9 and type(rows) is int and 0 <= rows <= 96
                and type(modes) is int and 0 <= modes <= 2048
                and doc["completed_targets"] == manifest["target_order"][:count]
                and set(doc["new_records"]) == set(doc["completed_targets"])
                and doc["parameters"] == manifest["parameters"]
                and sorted(doc) == manifest["allowed_scientific_fields"]
                and doc["old_scientific_target_calls"] == 0
                and doc["necessary_carrier_rematerializations"] in (0, 1)
                and doc["new_arrays_published"] == doc["new_artifacts"] == doc["new_Releases"] == 0,
                "all complete modes/rows and natural scalar prefixes without old target replay")
        for record in doc["new_records"].values():
            require(set(record) == {"ball", "bound"} and record["bound"] == "upper"
                    and isinstance(record["ball"], str), "one whole new formal upper")
        if modes or rows or count:
            restored = doc["carrier_restoration"]
            require(doc["necessary_carrier_rematerializations"] == 1
                    and restored["complete"] is True and restored["failure"] is None
                    and restored["result"]["complete"] is True
                    and restored["result"]["whole_original_endpoint_raw_grid_SHA_required"] is True
                    and restored["result"]["same_entire_original_rotation_and_source_phase"] is True
                    and restored["result"]["old_alpha_trial_materialized_or_used"] is False
                    and restored["result"]["old_quadrature_or_cohomological_mode_calls"] == 0
                    and restored["result"]["old_scientific_target_calls"] == 0
                    and restored["result"]["CORETYPE"] == "unset"
                    and doc["unit_disk_input_receipt"]["complete_nodes"] == 8192
                    and doc["unit_disk_input_receipt"]["every_complete_point_and_radius_saved_and_read"] is True
                    and doc["unit_disk_input_receipt"]["whole_original_grid_sha256"]
                        == restored["result"]["grid"]["sha256"],
                    "the same whole original grid and all new input disks precede every w mode")
        if count:
            w, saved_modes = doc["private_w_trial_receipt"], doc["private_w_modes_receipt"]
            require(modes == saved_modes["complete_positive_modes"] == w["positive_modes"] == 2048
                    and w["exact_mean"] == "0" and w["negative_modes_are_exact_conjugates"] is True
                    and w["same_original_w_equals_vi_minus_alpha"] is True
                    and saved_modes["complete_nodes_per_mode"] == 8192
                    and saved_modes["all_whole_mode_inputs_and_error_records_saved_read"] is True
                    and saved_modes["original_cohomological_divisor_phase_and_source192_retained"] is True
                    and saved_modes["whole_new_w_trial_sha256"] == w["sha256"]
                    and saved_modes["new_unit_disk_input_sha256"] == w["new_unit_disk_input_sha256"]
                        == doc["unit_disk_input_receipt"]["sha256"],
                    "every signed direct-w coefficient and its whole error input is formal")
        if rows or count > 2:
            require(doc["complete_DWT_error_records"]
                        == {name: doc["new_records"][name] for name in manifest["target_order"][:2]}
                    and doc["private_trial_receipt"]["bytes"] == 294912
                    and doc["private_trial_receipt"]["shape"] == [192, 96, 2]
                    and doc["private_row_trial_receipt"]["rows"] == 96
                    and doc["private_row_trial_receipt"]["positive_modes"] == 192
                    and doc["private_row_trial_receipt"]["exact_mean"] == "0"
                    and doc["private_row_trial_receipt"]["negative_modes_are_exact_conjugates"] is True
                    and isinstance(doc["complete_true_phase_a_ball"], str),
                    "both whole direct-w errors and every true row input precede all BR residual rows")
        if count > 2:
            residual = doc["private_residual_receipt"]
            require(rows == 96 and residual["rows"] == 96 and residual["positive_modes"] == 2240
                    and residual["all_finite_tail_outputs193_through2240_retained"] is True
                    and residual["negative_modes_are_exact_conjugates"] is True
                    and residual["true_phase_and_all_finite_rounding_enclosed"] is True,
                    "all96x2240 signed finite residuals precede any BR scalar")
        if doc["complete"]:
            result = doc["result"]
            require(doc["proved"] is True and doc["actual_returncode"] == 0 and doc["failure"] is None
                    and count == 9 and rows == 96 and modes == 2048
                    and doc["candidate_record"] is doc["current_target"] is None
                    and doc["stage"] == "complete_"+manifest["stage"]+"_branch"
                    and result["complete_new_record_order"] == doc["completed_targets"]
                    and result["complete_new_record_count"] == 9 and result["complete_true_inverse_row_count"] == 96
                    and result["complete_finite_residual_positive_modes"] == 2240
                    and result["old_quadrature_or_cohomological_mode_calls"] == 0,
                    "all nine whole bounds and the complete true inverse96-row enclosure")
            choice = doc["complete_product_choice"]
            require(choice["candidate_order"] == manifest["target_order"][5:7]
                    and choice["selected"] in choice["candidate_order"]
                    and choice["selected_whole_upper"] == doc["new_records"][choice["selected"]]
                    and choice["selection_on_complete_saved_records"] is True,
                    "both whole w-error product candidates remain formal before selection")
            require(all(result[key] is True for key in (
                "same_original_target_B_and_same_sign_projection_order",
                "whole_original_endpoint_raw_grid_restored_with_all_SHA",
                "complete_new_w2048_trial_with_original_phase_and_zero_mean",
                "both_complete_DWT_errors_saved_read_before_BR",
                "complete_old_ASR_tail_envelope_reused_without_recomputation",
                "all96_true_original_B_inverse_rows_enclosed_in_full_L2",
                "whole_space_energy_inverse_onto_and_norm_one_used",
                "true_target_phase_and_all_exact_rational_row_trials_retained",
                "all2240_outputs_and_complete_w_infinite_error_paid",
                "both_whole_w_product_candidates_saved_before_selection",
                "all_signed_residual_balls_saved_and_read"))
                and all(result[key] is False for key in (
                "old_alpha_trial_materialized_or_used", "BW_actual_claimed",
                "old_BW_ASR_cohomology_norm_or_transport_targets_recomputed",
                "extra_sqrt96_applied_to_joint_row_error", "physical_mean_slots_eliminated",
                "finite_Galerkin_solve_used_as_full_inverse_certificate",
                "SC_raw96_pairings_used_as_full_physical_columns",
                "physical_PDE_or_full_Schur_proved", "topic_completion_proved")),
                "full-space original row error, both means and all physical PDE obligations")
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

REPORT = '''        report = ("# Actual direct w and original target-B inverse96 rows\\n\\nRun "+run+"/"+attempt
                  +"; complete: "+str(state["complete"])+".\\n\\n"
                  "The entire successful source192 ASR actual and its original closure precede this target. "
                  "The exact original endpoint/raw/grid restoration stops before old alpha quadrature; "
                  "all needed whole hashes and the original phases remain required. A new8192-point disk "
                  "input certifies all2048 exact signed w coefficients directly with the original divisor. "
                  "Both whole w errors use the already completed original infinite tail and are saved/read "
                  "before the seven first original B-inverse row targets. No BW actual is asserted. "
                  "The new192-mode trial supplies all96 rows of E96_a* B^-1 for B=Id+T_w I. "
                  "Every signed output through2240 and the entire true-w infinite error are paid. "
                  "The original full-space energy inverse supplies the joint full-L2 row enclosure. "
                  "Both physical means and all physical PDE/full-Schur obligations remain. "
                  "No completed alpha, cohomology, transport, norm or UDR row target repeats.\\n").encode()


'''


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("the whole immutable public publication engine changed")
    source = raw.decode()
    changes = {
        "R149_complete_reflected_finite_waist_row_inputs_v1": "R149_complete_direct_w_and_target_B_rows_inputs_v1",
        '"reflected_finite_waist_rows"': '"direct_w_and_target_B_rows"',
        'manifest["complete_record_counts"] == [96]': 'manifest["complete_record_counts"] == [9]',
        "one complete actual 96-row reflected-waist manifest": "one complete original target-B inverse96-row manifest",
        "actual-reflected-waist-rows": "actual-direct-w-and-target-B-rows",
        "R149_complete_reflected_finite_waist_rows_execution_v1": "R149_complete_direct_w_and_target_B_rows_execution_v1",
        "consumed_R149_complete_reflected_finite_waist_rows_target_v1": "consumed_R149_complete_direct_w_and_target_B_rows_target_v1",
        "whole_actual_conjugacy_inputs_reserved_for_one_new_complete_96row_target": "whole_successful_ASR_reserved_for_first_DWT2_BR7",
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
            "the original whole ASR closure is inherited without another native source set")
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
    state["necessary_original_grid_restoration"] = (result or {}).get("carrier_restoration")
    state["complete_new_residual_rows"] = (result or {}).get("complete_residual_row_count", 0)
    state["completed_direct_w_modes"] = (result or {}).get("complete_w_mode_count", 0)
    state["complete_direct_w_carrier"] = (result or {}).get("private_w_trial_receipt")
    state["complete_DWT_error_records"] = (result or {}).get("complete_DWT_error_records")
'''+old)
    start = source.index("        report = (", source.index("    def final_files():"))
    end = source.index("        return {**staged", start)
    source = source[:start]+REPORT+source[end:]
    return source


if __name__ == "__main__":
    exec(compile(patched_source(), __file__, "exec"), {"__name__": "__main__", "__file__": __file__})
