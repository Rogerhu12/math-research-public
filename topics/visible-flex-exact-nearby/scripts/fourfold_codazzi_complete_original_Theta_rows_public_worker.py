"""OT first complete original Theta execution on the immutable RW engine.

All publication, exact-byte restoration, hourly rules and non-fast-forward
rebase/push semantics are inherited. Only the new contract, whole parent
admission, private carrier children and complete result schema change.
"""
from pathlib import Path
import hashlib

BASE_NAME = "fourfold_codazzi_reflected_waist_rows_public_worker.py"
BASE_SHA256 = "9a474a43f065843af583edaab3bf774eddd845dab47a589aabe8cedcdd2b2490"

VALIDATOR = '''    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"], "whole original Theta result")
        doc = parse(raw)
        identity = doc["identity"]
        require(identity["kind"] == manifest["scientific_kind"]
                and identity["scalar_stage"] == manifest["stage"]
                and identity["source_sha256"] == by_role["science"]["sha256"]
                and identity["manifest_sha256"] == args.manifest_sha
                and identity["run_id"] == run and identity["run_attempt"] == attempt
                and identity["arithmetic_bits"] == 320
                and all(identity[role+"_sha256"] == by_role[role]["sha256"]
                        for role in ("IR_actual", "AS_actual", "DT_math", "TM_math", "TP_math")),
                "the complete same original IR/AS/DT/TM/TP identity")
        count = doc["saved_record_count"]
        require(type(count) is int and 0 <= count <= 10
                and doc["completed_targets"] == manifest["target_order"][:count]
                and set(doc["new_records"]) == set(doc["completed_targets"])
                and doc["parameters"] == manifest["parameters"]
                and sorted(doc) == manifest["allowed_scientific_fields"]
                and doc["old_scientific_target_calls"] == 0
                and doc["necessary_carrier_rematerializations"] in (0, 1, 2)
                and doc["new_arrays_published"] == doc["new_artifacts"] == doc["new_Releases"] == 0
                and type(doc["private_complete_row_count"]) is int
                and 0 <= doc["private_complete_row_count"] <= 96,
                "complete original Theta prefix with no old target replay")
        for record in doc["new_records"].values():
            require(set(record) == {"ball", "bound"} and record["bound"] == "upper"
                    and isinstance(record["ball"], str), "one whole formal new scalar ball")
        if count:
            require(doc["necessary_carrier_rematerializations"] == 2
                    and set(doc["carrier_restorations"]) == {"IR", "AS"}
                    and all(value["complete"] is True and value["failure"] is None
                            and value["result"]["whole_original_SHA_required"] is True
                            and value["result"]["old_scientific_target_calls"] == 0
                            for value in doc["carrier_restorations"].values()),
                    "both complete original carrier identities precede every new target")
        if doc["complete"]:
            result = doc["result"]
            require(doc["proved"] is True and doc["actual_returncode"] == 0
                    and doc["failure"] is None and count == 10
                    and doc["candidate_record"] is doc["current_target"] is None
                    and doc["stage"] == "complete_"+manifest["stage"]+"_branch"
                    and doc["private_complete_row_count"] == 96
                    and doc["private_DT_rows_receipt"]["positive_modes"] == 2240
                    and doc["private_model_rows_receipt"]["real_modes"] == 2240
                    and doc["private_Theta_trial_receipt"]["shape"] == [96, 2240]
                    and doc["private_Theta_trial_receipt"]["bytes"] == 96*2240*8
                    and doc["private_Theta_trial_receipt"]["dtype"] == "<f8"
                    and doc["private_model_multipliers_receipt"]["complete_modes"] == 2240
                    and doc["actual_model_input_records"]["same_full_beta_minus_mu_over4_inside_original_native"] is True
                    and result["complete_new_record_order"] == doc["completed_targets"]
                    and result["complete_new_record_count"] == 10
                    and result["complete_signed_row_count"] == 96
                    and result["complete_finite_row_modes"] == 2240,
                    "every original signed model row and complete joint error")
            require(all(result[key] is True for key in (
                    "whole_original_VQ_and_Theta_errors_proved", "same_true_model_low_reference_and_phases_retained",
                    "both_complete_alpha_product_candidates_saved_before_choice",
                    "all_aliases_infinite_tails_true_map_and_alpha_errors_retained",
                    "all_original_carrier_whole_SHA_identical", "two_independent_original_carrier_runtimes_retained",
                    "every_signed_model_action_ball_saved_and_read", "true_target_orthonormal_basis_used"))
                    and all(result[key] is False for key in (
                    "extra_sqrt96_applied", "physical_mean_slots_eliminated",
                    "old_norm_residual_cohomology_or_gap_targets_recomputed",
                    "actual_true_PDE_signed_square_or_full_Schur_proved", "topic_completion_proved")),
                    "the actual whole original Theta, with all independent physical obligations retained")
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

REPORT = '''        report = ("# Actual complete original Theta rows\\n\\nRun "+run+"/"+attempt
                  +"; complete: "+str(state["complete"])+".\\n\\n"
                  "The entire original IR and AS actual objects, all their prerequisites, the actual "
                  "SDI inputs and the full original CYA finite/native-infinite scope are admitted. "
                  "Two isolated private children rematerialize only the original exact finite "
                  "carriers under their original runtime schedules and require every original "
                  "whole SHA. No completed residual, norm, cohomology or Cayley target repeats. "
                  "The new calculation keeps the original same-sign Astar, all96x2240 signed "
                  "model rows, the low reference one, true phases and moving mean. Complete "
                  "Linfinity and L2 alpha products are saved before whole-candidate selection. "
                  "The full VQ and original Theta joint errors include infinite residual tails, "
                  "true-map differences, alpha errors and every finite model rounding radius. "
                  "Two physical mean slots, true PDE columns, nu/phase and the full Schur "
                  "inverse remain independent obligations. Private arrays are never published.\\n").encode()

'''


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("whole immutable publication engine changed")
    source = raw.decode()
    changes = {
        "R149_complete_reflected_finite_waist_row_inputs_v1": "R149_complete_original_Theta_rows_inputs_v1",
        '"reflected_finite_waist_rows"': '"complete_original_Theta_rows"',
        'manifest["complete_record_counts"] == [96]': 'manifest["complete_record_counts"] == [10]',
        "one complete actual 96-row reflected-waist manifest": "one complete original Theta96-row manifest",
        "actual-reflected-waist-rows": "actual-complete-original-Theta-rows",
        "R149_complete_reflected_finite_waist_rows_execution_v1": "R149_complete_original_Theta_rows_execution_v1",
        "consumed_R149_complete_reflected_finite_waist_rows_target_v1": "consumed_R149_complete_original_Theta_rows_target_v1",
        "whole_actual_conjugacy_inputs_reserved_for_one_new_complete_96row_target": "whole_actual_IR_AS_inputs_reserved_for_complete_original_Theta",
        "visible-exact: reserve exact reflected waist ": "visible-exact: reserve complete original Theta ",
        "visible-exact: preserve exact reflected waist ": "visible-exact: preserve complete original Theta ",
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
'''+old)
    start = source.index("        report = (", source.index("    def final_files():"))
    end = source.index("        return {**staged", start)
    source = source[:start]+REPORT+source[end:]
    return source


if __name__ == "__main__":
    exec(compile(patched_source(), __file__, "exec"), {"__name__": "__main__", "__file__": __file__})
