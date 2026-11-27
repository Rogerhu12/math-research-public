"""TQC complete unit-disk operator Theta low square on the immutable RW engine.

All publication, exact-byte restoration, hourly rules and non-fast-forward
rebase/push semantics are inherited. Only the new contract, whole parent
admission, private carrier children and complete result schema change.
"""
from pathlib import Path
import hashlib

BASE_NAME = "fourfold_codazzi_reflected_waist_rows_public_worker.py"
BASE_SHA256 = "9a474a43f065843af583edaab3bf774eddd845dab47a589aabe8cedcdd2b2490"

VALIDATOR = '''    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"], "whole original Theta low-square result")
        doc = parse(raw)
        identity = doc["identity"]
        require(identity["kind"] == manifest["scientific_kind"]
                and identity["scalar_stage"] == manifest["stage"]
                and identity["source_sha256"] == by_role["science"]["sha256"]
                and identity["manifest_sha256"] == args.manifest_sha
                and identity["run_id"] == run and identity["run_attempt"] == attempt
                and identity["arithmetic_bits"] == 320
                and all(identity[role+"_sha256"] == by_role[role]["sha256"]
                        for role in ("OT_actual", "TQ_math", "TQL_math", "carrier_restore", "UDR_math", "GYN_math")),
                "the same whole completed OT and complete low-square source identity")
        count = doc["saved_record_count"]
        require(type(count) is int and 0 <= count <= 21
                and doc["completed_targets"] == manifest["target_order"][:count]
                and set(doc["new_records"]) == set(doc["completed_targets"])
                and doc["parameters"] == manifest["parameters"]
                and sorted(doc) == manifest["allowed_scientific_fields"]
                and doc["old_scientific_target_calls"] == 0
                and doc["necessary_carrier_rematerializations"] in (0, 1, 2)
                and doc["new_arrays_published"] == doc["new_artifacts"] == doc["new_Releases"] == 0
                and doc["private_complete_row_count"] in (0, 96),
                "whole complete low-square prefix without an old target replay")
        for record in doc["new_records"].values():
            require(set(record) == {"ball", "bound"} and record["bound"] == "upper"
                    and isinstance(record["ball"], str), "one complete new scalar upper")
        modes = doc["complete_unit_disk_mode_count"]
        require(type(modes) is int and 0 <= modes <= 2048,
                "the whole new unit-disk natural mode prefix")
        if modes:
            require(doc["unit_disk_input_receipt"]["complete_nodes"] == 8192
                    and doc["unit_disk_input_receipt"]["every_complete_point_and_radius_saved_and_read"] is True,
                    "all new point centers and disks are formal before any mode")
        if count or modes:
            restored = doc["original_Theta_carrier_restoration"]
            require(doc["necessary_carrier_rematerializations"] == 2
                    and set(doc["carrier_restorations"]) == {"IR", "AS"}
                    and all(value["complete"] is True and value["failure"] is None
                            and value["result"]["whole_original_SHA_required"] is True
                            and value["result"]["old_scientific_target_calls"] == 0
                            for value in doc["carrier_restorations"].values())
                    and doc["private_complete_row_count"] == 96
                    and restored["complete"] is restored["whole_original_SHA_required"] is True
                    and restored["complete_signed_rows"] == 96 and restored["complete_modes_per_row"] == 2240
                    and restored["completed_OT_norm_or_error_targets_replayed"] == 0
                    and restored["all_original_IR_AS_norm_residual_or_cohomology_targets_replayed"] == 0
                    and set(restored["original_carriers"]) == {"private_DT_rows_receipt",
                        "private_model_multipliers_receipt", "private_model_rows_receipt", "private_Theta_trial_receipt"},
                    "all original complete carrier SHA identities precede every new scalar")
        if count:
            GY = doc["private_GY_real_matrix_receipt"]
            require(GY["shape"] == [384, 96]
                    and GY["whole_original_IR_trial_sha256"] == (
                        doc["carrier_restorations"]["IR"]["result"]["trial"]["sha256"])
                    and GY["all36864_signed_entries_saved_read_before_absolute_values"] is True
                    and GY["complete_normalized_real_basis_and_physical_frequency_factor"] == 4
                    and GY["old_Hilbert_Schmidt_reducer_calls"] == 0
                    and type(GY["bytes"]) is int and GY["bytes"] > 0
                    and isinstance(GY["sha256"], str) and len(GY["sha256"]) == 64,
                    "all whole signed real matrix entries precede any new scalar")
        if count > 3 or modes:
            GY_choice = doc["complete_GY_operator_norm_choice"]
            candidates = {"new_complete_GY_operator_Schur": doc["new_records"][manifest["target_order"][2]],
                "old_complete_GY_Hilbert_Schmidt": doc["copied_complete_OT_records"][
                    "complete_G_trial_Hilbert_Schmidt_upper"]}
            require(GY_choice["both_complete_candidates"] == candidates
                    and GY_choice["selected_complete_candidate"] in candidates
                    and GY_choice["both_whole_candidates_formal_before_selection"] is True
                    and GY_choice["same_whole_original_GY_operator"] is True
                    and GY_choice["old_Hilbert_Schmidt_target_recomputed"] is False,
                    "the complete new operator and old HS candidates precede every UDR mode")
        if count > 3:
            residuals = doc["private_unit_disk_modes_receipt"]
            require(modes == residuals["complete_positive_modes"] == 2048
                    and residuals["complete_nodes_per_mode"] == 8192
                    and residuals["all_original_mean_phase_and_divisor_payments_retained"] is True
                    and residuals["all_records_saved_read_before_complete_products"] is True
                    and residuals["new_input_sha256"] == doc["unit_disk_input_receipt"]["sha256"],
                    "every whole new product pays all2048 residual modes and the entire original tail")
        if count >= 8:
            choices = doc["unit_disk_product_choices"]
            require(set(choices) == {"finite_trial", "whole_inverse_error"},
                    "both complete joint-operator choices are retained")
            for label, indices in (("finite_trial", (3, 4)), ("whole_inverse_error", (5, 6))):
                names = [manifest["target_order"][index] for index in indices]
                choice = choices[label]
                require(choice["selected_complete_candidate"] in names
                        and choice["both_complete_candidates"] == {name: doc["new_records"][name] for name in names}
                        and choice["all2048_modes_and_complete_tail_retained"] is True
                        and choice["choice_after_whole_save_readback"] is True
                        and choice["extra_sqrt96"] is False,
                        "only already formal whole candidates enter a new row bound")
        if doc["complete"]:
            result, gate = doc["result"], doc["complete_coordinate_inverse"]
            require(doc["proved"] is True and doc["actual_returncode"] == 0 and doc["failure"] is None
                    and count == 21 and doc["candidate_record"] is doc["current_target"] is None
                    and doc["stage"] == "complete_"+manifest["stage"]+"_branch"
                    and result["complete_new_record_order"] == doc["completed_targets"]
                    and result["complete_new_record_count"] == 21
                    and result["complete_new_disk_modes"] == 2048 and result["complete_new_disk_grid_points"] == 8192
                    and result["complete_square_dimension"] == 96
                    and result["all_original_carrier_rows"] == 96 and result["all_original_carrier_modes"] == 2240
                    and doc["private_square_receipt"]["shape"] == [96, 96]
                    and doc["private_square_receipt"]["bytes"] == 73728
                    and doc["private_trial_inverse_receipt"]["shape"] == [96, 96]
                    and doc["private_trial_inverse_receipt"]["bytes"] == 73728
                    and doc["private_signed_residual_receipt"]["shape"] == [96, 96]
                    and set(doc["complete_norm_choices"]) == {"trial_inverse_", "trial_residual_"},
                    "both whole matrices, the signed residual and all complete norm choices")
            require(type(gate["finite_coordinate_inverse_proved"]) is bool
                    and gate["strict_whole_residual_upper_less_than_one"] == gate["finite_coordinate_inverse_proved"]
                    and result["finite_coordinate_inverse_proved"] == gate["finite_coordinate_inverse_proved"]
                    and (gate["complete_coordinate_inverse_two_upper"] is None) == (not gate["finite_coordinate_inverse_proved"])
                    and gate["complete_preconditioned_residual_record"] == doc["new_records"][manifest["target_order"][-1]]
                    and gate["sufficient_gate_false_is_not_a_singularity_proof"] is True
                    and gate["physical_PDE_column_inverse_proved"] is gate["full_physical_Schur_proved"] is False,
                    "the strict coordinate gate is evaluated without assuming its success")
            if gate["finite_coordinate_inverse_proved"]:
                bound = gate["complete_coordinate_inverse_two_upper"]
                require(set(bound) == {"ball", "bound"} and bound["bound"] == "upper"
                        and isinstance(bound["ball"], str), "the complete conditional coordinate-inverse bound")
            require(all(result[key] is True for key in (
                    "all_original_whole_carrier_SHA_identical", "complete_low_model_isometry_and_all9216_radii_used",
                    "whole_global_and_low_error_candidates_saved_before_choice",
                    "complete_signed_inverse_and_residual_norm_candidates_saved_before_choice",
                    "full_source_phase_mean_and_infinite_errors_retained", "strict_gate_completely_evaluated",
                    "all_four_new_products_saved_before_any_choice",
                    "coefficient_error_on_infinite_inverse_error_paid",
                    "all_seven_UDR_records_formal_before_first_TQC_target",
                    "all_three_GYN_records_formal_before_first_UDR_target",
                    "all36864_signed_GY_entries_before_new_induced_norms",
                    "new_operator_and_old_HS_whole_candidates_formal_before_choice"))
                    and all(result[key] is False for key in (
                    "extra_sqrt96_or_high_model512_on_low_isometry",
                    "completed_old_norm_residual_or_cohomology_targets_recomputed", "physical_mean_slots_eliminated",
                    "actual_true_PDE_inverse_or_full_Schur_proved", "topic_completion_proved",
                    "old_ASR_scalar_targets_or_old_OT_norms_recomputed",
                    "old_GY_Hilbert_Schmidt_target_recomputed")),
                    "the whole coordinate result keeps every separate physical and nonlinear obligation")
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
                                state["last_published_complete_target_count"] = prefix_doc["saved_record_count"]
                                state["last_published_complete_row_count"] = prefix_doc["private_complete_row_count"]
                                state["partial_prefix_publication_count"] = state.get("partial_prefix_publication_count", 0)+1
                                state["scientific_files"] = [dict(path=p, bytes=len(b), sha256=sha(b))
                                                               for p, b in staged.items()]
                                def prefix_files():
                                    receipt = encode(state)
                                    require(len(receipt) <= op["maximum_execution_bytes"], "whole original Theta prefix receipt")
                                    return {**staged, output_dir+"/execution.json": receipt}
                                publish(prefix_files, "visible-exact: preserve complete original Theta prefix")
'''

REPORT = '''        report = ("# Actual complete unit-disk operator Theta low square\\n\\nRun "+run+"/"+attempt
                  +"; complete: "+str(state["complete"])+".\\n\\n"
                  "The entire successful OT result and all inherited original objects are admitted. "
                  "The full96x2240 signed carriers are restored with all four original whole SHA "
                  "identities before their low square is used. Completed OT/IR/AS norms and residual "
                  "targets never repeat. Three new complete induced operator-norm records retain "
                  "all36864 entries of the normalized original GY real matrix. The entire new "
                  "Schur and old Hilbert--Schmidt candidates are saved before selection. "
                  "A new8192-node unit-disk phase input next certifies all2048 "
                  "residual modes to the identical old signed alpha trial. Four whole products "
                  "pay its action on both the finite rows and their full infinite inverse error; "
                  "all seven new joint row bounds are saved before the first low-square target. "
                  "New complete9216-entry low model radii use the exact "
                  "low-reference isometry and preserve every infinite error and true phase. Both "
                  "whole global/low candidates and all signed inverse/residual norm candidates are "
                  "saved before selection. The strict residual gate is evaluated explicitly; "
                  "a false sufficient gate is not a singularity theorem. Coordinate inverse gate: "
                  +str(state.get("finite_coordinate_inverse_proved"))+". Physical PDE columns, "
                  "two physical means, the full Schur operator and nonlinear completion remain "
                  "separate obligations. Private arrays are never published.\\n").encode()

'''


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("whole immutable publication engine changed")
    source = raw.decode()
    changes = {
        "R149_complete_reflected_finite_waist_row_inputs_v1": "R149_complete_unit_disk_operator_Theta_low_square_inputs_v1",
        '"reflected_finite_waist_rows"': '"unit_disk_operator_Theta_low_square"',
        'manifest["complete_record_counts"] == [96]': 'manifest["complete_record_counts"] == [21]',
        "one complete actual 96-row reflected-waist manifest": "one complete original Theta low96-square manifest",
        "actual-reflected-waist-rows": "actual-unit-disk-operator-Theta-low-square",
        "R149_complete_reflected_finite_waist_rows_execution_v1": "R149_complete_unit_disk_operator_Theta_low_square_execution_v1",
        "consumed_R149_complete_reflected_finite_waist_rows_target_v1": "consumed_R149_complete_unit_disk_operator_Theta_low_square_target_v1",
        "whole_actual_conjugacy_inputs_reserved_for_one_new_complete_96row_target": "whole_actual_OT_inputs_reserved_for_unit_disk_operator_Theta_low_square",
        "visible-exact: reserve exact reflected waist ": "visible-exact: reserve complete unit-disk operator Theta low square ",
        "visible-exact: preserve exact reflected waist ": "visible-exact: preserve complete unit-disk operator Theta low square ",
        'require(len(history_specs) == 4': 'require(len(history_specs) == 6',
        '== {"W_native", "R31_native", "K_native", "H_native"}':
            '== {"W_native", "R31_native", "K_native", "H_native", "terminal_cover_native", "wiener_native"}',
        'and 0 < item["bytes"] < 100000 for item in history_specs)':
            'and 0 < item["bytes"] < 200000 for item in history_specs)',
        "four whole immutable native inputs, periodic rule check and no science retry":
            "six whole immutable IR inputs plus the full inherited AS closure, no science retry",
        'destination = source_dir / (spec["role"] + Path(spec["path"]).suffix)':
            'destination = source_dir / ("input_" + spec["role"] + Path(spec["path"]).suffix)',
        '{item["role"]: item for item in specs+history_specs})':
            '{item["role"]: item for item in specs+history_specs}, manifest)',
    }
    for old, new in changes.items():
        if old not in source:
            raise ValueError("the unique original Theta task patch did not match: "+old)
        source = source.replace(old, new)
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
    state["necessary_original_carrier_children"] = (result or {}).get("carrier_restorations", {})
    state["complete_original_signed_Theta_rows"] = (result or {}).get("private_complete_row_count", 0)
    state["complete_original_OT_carrier_restoration"] = (result or {}).get("original_Theta_carrier_restoration")
    state["finite_coordinate_inverse_proved"] = ((result or {}).get("result") or {}).get("finite_coordinate_inverse_proved")
    state["completed_unit_disk_modes"] = (result or {}).get("complete_unit_disk_mode_count",0)
    state["complete_unit_disk_mode_carrier"] = (result or {}).get("private_unit_disk_modes_receipt")
    state["complete_new_GY_real_matrix_receipt"] = (result or {}).get("private_GY_real_matrix_receipt")
    state["complete_GY_operator_norm_choice"] = (result or {}).get("complete_GY_operator_norm_choice")
'''+old)
    start = source.index("        report = (", source.index("    def final_files():"))
    end = source.index("        return {**staged", start)
    source = source[:start]+REPORT+source[end:]
    return source


if __name__ == "__main__":
    exec(compile(patched_source(), __file__, "exec"), {"__name__": "__main__", "__file__": __file__})
