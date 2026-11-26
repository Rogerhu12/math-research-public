"""IR public first execution, using the fixed complete RW publication engine.

Only the new target identity, six whole native restorations, full result
schema, report and long-job prefix publication are adapted. The immutable
engine retains all whole-byte checks, source pins, README checks, complete
topic capacity accounting and immediate non-fast-forward rebase/push loop.
"""
from pathlib import Path
import hashlib

BASE_NAME = "fourfold_codazzi_reflected_waist_rows_public_worker.py"
BASE_SHA256 = "9a474a43f065843af583edaab3bf774eddd845dab47a589aabe8cedcdd2b2490"

VALIDATOR = '''    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"], "entire IR scientific result")
        doc = parse(raw)
        identity = doc["identity"]
        require(identity["kind"] == manifest["scientific_kind"]
                and identity["scalar_stage"] == manifest["stage"]
                and identity["source_sha256"] == by_role["science"]["sha256"]
                and identity["IR_math_sha256"] == by_role["IR_math"]["sha256"]
                and identity["DC_math_sha256"] == by_role["DC_math"]["sha256"]
                and identity["DB_math_sha256"] == by_role["DB_math"]["sha256"]
                and identity["IL_actual_sha256"] == by_role["IL_actual"]["sha256"]
                and identity["manifest_sha256"] == args.manifest_sha
                and identity["run_id"] == run and identity["run_attempt"] == attempt
                and identity["arithmetic_bits"] == manifest["parameters"]["arithmetic_bits"],
                "same whole IL/DC/DB/IR source and actual original coordinate rows")
        count = doc["saved_record_count"]
        require(type(count) is int and 0 <= count <= 99
                and doc["completed_targets"] == manifest["target_order"][:count]
                and set(doc["new_records"]) == set(doc["completed_targets"])
                and doc["old_scientific_target_calls"] == 0
                and doc["new_arrays_published"] == doc["new_artifacts"] == doc["new_Releases"] == 0
                and doc["parameters"] == manifest["parameters"]
                and sorted(doc) == manifest["allowed_scientific_fields"],
                "complete new row prefix without IL or other old target replay")
        rows = min(count, 96)
        require(type(doc["private_complete_row_count"]) is int
                and rows <= doc["private_complete_row_count"] <= min(96, rows+1),
                "a whole private signed carrier precedes each completed residual row")
        for index, name in enumerate(doc["completed_targets"]):
            record = doc["new_records"][name]
            if index < 96:
                require(set(record) == {"H", "L2", "analytic_model_H", "analytic_model_L2", "real_model_L2"},
                        "same complete residual in both norms and all model alternatives")
                for key, value in record.items():
                    if value is None:
                        require(key == "real_model_L2"
                                and doc["global_bounds"]["real_model_bound_available"] is False,
                                "only an explicitly unavailable optional homotopy bound may be null")
                    else:
                        require(set(value) == {"ball", "bound"} and value["bound"] == "upper"
                                and isinstance(value["ball"], str), "entire saved row scalar ball")
            else:
                require(set(record) == {"ball", "bound"} and record["bound"] == "upper"
                        and isinstance(record["ball"], str), "entire joint residual bound")
        if count:
            require(doc["private_grid_receipt"]["complete_count"] == 4096
                    and doc["private_trial_receipt"]["shape"] == [192, 96, 2]
                    and doc["private_trial_receipt"]["bytes"] == 192*96*2*8
                    and doc["private_trial_receipt"]["dtype"] == "<f8"
                    and doc["private_trial_receipt"]["exact_binary64_dyadic_definition"] is True
                    and len(doc["private_sample_chain_sha256"]) == len(doc["private_head_chain_sha256"]) == 64,
                    "whole original grid and exact complete finite trial, with full signed-head hashes")
        if doc["complete"]:
            result = doc["result"]
            require(count == 99 and doc["proved"] is True
                    and doc["failure"] is None and doc["actual_returncode"] == 0
                    and doc["candidate_record"] is None and doc["current_target"] is None
                    and doc["stage"] == "complete_"+manifest["stage"]+"_branch"
                    and result["complete_new_record_order"] == doc["completed_targets"]
                    and result["complete_new_record_count"] == 99
                    and result["complete_row_count"] == doc["private_complete_row_count"] == 96
                    and result["complete_joint_record_count"] == 3
                    and all(result[key] is True for key in (
                        "same_full_signed_residual_used_in_both_norms",
                        "all_frequencies_aliases_and_true_map_errors_paid",
                        "positive_input_positive_output_then_negative_conjugate",
                        "exact_output_mean_is_zero",
                        "whole_private_grids_trials_and_heads_saved_and_read_back",
                        "complete_original_coordinate_rows_on_L2_proved",
                        "all_joint_bounds_use_all96_formal_saved_rows"))
                    and all(result[key] is False for key in (
                        "additional_sqrt96_after_joint_error", "original_A_already_applied",
                        "whole_VQ_or_Theta_rows_claimed", "independent_physical_density_mean_rows_paid",
                        "full_nu_phase_mean_Schur_proved", "IL_or_other_old_scientific_targets_recomputed",
                        "topic_completion_proved")),
                    "all original coordinate rows, with A/Theta/mean/nu/phase obligations retained")
        return doc

'''

REPORT = '''        report = ("# Actual complete original inverse-density rows\\n\\nRun "+run+"/"+attempt
                  +"; complete: "+str(state["complete"])+".\\n\\n"
                  "The entire successful IL object and all six original native inputs are admitted. "
                  "One new finite192 trial for each of96 original coordinate rows is selected, "
                  "saved as an exact dyadic carrier and read back. Directed4096-point complex "
                  "DFT, every alias, the whole complementary Fourier tail and the true-map "
                  "difference certify the same signed residual in Hdot-minus-one-half and L2. "
                  "Only all96 complete formal rows authorize the joint conclusions. The "
                  "result is E96star Dplus_inverse C_inverse before the original A. Whole "
                  "VQ/Theta, physical means and the true nu/phase Schur condition retain their "
                  "original obligations. IL, old transport, KAM, RW/TC rows and all old targets "
                  "are not recomputed. Arrays remain private; complete hashes are published.\\n").encode()

'''

PERIODIC = '''                        pull()
                        if output.exists():
                            complete_prefix = output.read_bytes()
                            prefix_doc = validate_output(complete_prefix)
                            count_now = prefix_doc["saved_record_count"]
                            if count_now > state.get("last_published_prefix_count", 0):
                                staged[output_dir + "/" + output_name] = complete_prefix
                                state["last_published_prefix_count"] = count_now
                                state["partial_prefix_publication_count"] = state.get("partial_prefix_publication_count", 0)+1
                                state["scientific_files"] = [dict(path=p, bytes=len(b), sha256=sha(b))
                                                               for p, b in staged.items()]
                                def prefix_files():
                                    receipt = encode(state)
                                    require(len(receipt) <= op["maximum_execution_bytes"],
                                            "entire current prefix execution receipt")
                                    return {**staged, output_dir+"/execution.json": receipt}
                                publish(prefix_files, "visible-exact: preserve complete inverse-density row prefix")
'''


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("whole immutable publication engine changed")
    source = raw.decode()
    replacements = {
        "R149_complete_reflected_finite_waist_row_inputs_v1": "R149_complete_inverse_density_rows_inputs_v1",
        '"reflected_finite_waist_rows"': '"original_inverse_density_rows"',
        'manifest["complete_record_counts"] == [96]': 'manifest["complete_record_counts"] == [96, 3]',
        "one complete actual 96-row reflected-waist manifest": "one complete original inverse-density96-row manifest",
        "actual-reflected-waist-rows": "actual-original-inverse-density-rows",
        "R149_complete_reflected_finite_waist_rows_execution_v1": "R149_complete_inverse_density_rows_execution_v1",
        "consumed_R149_complete_reflected_finite_waist_rows_target_v1": "consumed_R149_complete_inverse_density_rows_target_v1",
        "whole_actual_conjugacy_inputs_reserved_for_one_new_complete_96row_target": "whole_actual_inverse_lift_reserved_for_original96_full_residual_rows",
        "visible-exact: reserve exact reflected waist ": "visible-exact: reserve original inverse-density rows ",
        "visible-exact: preserve exact reflected waist ": "visible-exact: preserve original inverse-density rows ",
        'require(len(history_specs) == 4': 'require(len(history_specs) == 6',
        '== {"W_native", "R31_native", "K_native", "H_native"}':
            '== {"W_native", "R31_native", "K_native", "H_native", "terminal_cover_native", "wiener_native"}',
        'and 0 < item["bytes"] < 100000 for item in history_specs)':
            'and 0 < item["bytes"] < 200000 for item in history_specs)',
        "four whole immutable native inputs, periodic rule check and no science retry":
            "six whole immutable native inputs, periodic rule check and no science retry",
        'destination = source_dir / (spec["role"] + Path(spec["path"]).suffix)':
            'destination = source_dir / ("input_" + spec["role"] + Path(spec["path"]).suffix)',
        'OMP_NUM_THREADS="1", MKL_NUM_THREADS="1", NUMEXPR_NUM_THREADS="1")':
            'OMP_NUM_THREADS="1", MKL_NUM_THREADS="1", NUMEXPR_NUM_THREADS="1", OPENBLAS_CORETYPE="Haswell")',
    }
    for old, new in replacements.items():
        if old not in source:
            raise ValueError("fixed publication task patch did not match: "+old)
        source = source.replace(old, new)
    start = source.index("    def validate_output(raw):\n")
    end = source.index("    try:\n        head = pull()\n", start)
    source = source[:start]+VALIDATOR+source[end:]
    old_periodic = "                        pull()\n                    except BaseException as exc:\n"
    if source.count(old_periodic) != 1:
        raise ValueError("the original unique periodic rule-check block changed")
    source = source.replace(old_periodic, PERIODIC+"                    except BaseException as exc:\n")
    start = source.index("        report = (", source.index("    def final_files():"))
    end = source.index("        return {**staged", start)
    source = source[:start]+REPORT+source[end:]
    return source


if __name__ == "__main__":
    exec(compile(patched_source(), __file__, "exec"),
         {"__name__": "__main__", "__file__": __file__})
