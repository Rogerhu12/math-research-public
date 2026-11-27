"""BW first signed target-w execution on the immutable public RW engine.

The entire successful ASR closure, actual and execution are admitted before
reservation. One necessary original carrier pass feeds four new error balls.
No private coefficient or quadrature array is published.
"""
from pathlib import Path
import hashlib

BASE_NAME = "fourfold_codazzi_reflected_waist_rows_public_worker.py"
BASE_SHA256 = "9a474a43f065843af583edaab3bf774eddd845dab47a589aabe8cedcdd2b2490"

VALIDATOR = '''    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"], "whole complete BW result")
        doc = parse(raw)
        identity = doc["identity"]
        require(identity["kind"] == manifest["scientific_kind"]
                and identity["scalar_stage"] == manifest["stage"]
                and identity["source_sha256"] == by_role["science"]["sha256"]
                and identity["manifest_sha256"] == args.manifest_sha
                and identity["run_id"] == run and identity["run_attempt"] == attempt
                and identity["arithmetic_bits"] == 320
                and all(identity[role+"_sha256"] == by_role[role]["sha256"]
                    for role in ("AS_actual", "AS_execution", "AS_manifest", "BW_math", "carrier_original_owner")),
                "same complete ASR parent and the four new target-w errors")
        count, prefix = doc["saved_record_count"], doc["complete_mode_prefix"]
        require(type(count) is int and 0 <= count <= 4
                and doc["completed_targets"] == manifest["target_order"][:count]
                and set(doc["new_records"]) == set(doc["completed_targets"])
                and doc["parameters"] == manifest["parameters"]
                and sorted(doc) == manifest["allowed_scientific_fields"]
                and doc["old_scientific_target_calls"] == 0
                and doc["necessary_carrier_rematerializations"] in (0, 1)
                and doc["new_arrays_published"] == doc["new_artifacts"] == doc["new_Releases"] == 0
                and type(prefix["complete_modes"]) is int and 0 <= prefix["complete_modes"] <= 2048,
                "whole new mode/error prefix without old target replay")
        for record in doc["new_records"].values():
            require(set(record) == {"ball", "bound"} and record["bound"] == "upper"
                    and isinstance(record["ball"], str), "one complete new formal upper")
        if prefix["complete_modes"] or count:
            restored, observed = doc["original_carrier_restoration"], doc["private_quadrature_receipt"]
            require(doc["necessary_carrier_rematerializations"] == 1
                    and restored["complete"] is True and restored["whole_original_SHA_required"] is True
                    and restored["old_scientific_target_calls"] == 0
                    and restored["SN_endpoint"]["bytes"] == 245885
                    and restored["SN_endpoint"]["sha256"]
                        == "3048266ba668164d7d9b5475c5262f1f3568cfe32a6e42c7bb496e4bda6c62b6"
                    and observed["positive_modes"] == 2048 and observed["quadrature_passes"] == 1
                    and observed["original_return_values_unchanged"] is True
                    and observed["old_norm_targets_called"] == 0,
                    "one full old carrier identity and its unchanged integral observations precede every new mode")
            for key in ("head_Linf_upper", "head_L2_square_upper"):
                require(set(prefix[key]) == {"ball", "bound"} and prefix[key]["bound"] == "upper"
                        and isinstance(prefix[key]["ball"], str), "one complete new prefix accumulator")
        if doc["complete"]:
            result = doc["result"]
            require(doc["proved"] is True and doc["actual_returncode"] == 0 and doc["failure"] is None
                    and count == 4 and prefix["complete_modes"] == 2048
                    and doc["candidate_record"] is doc["current_target"] is None
                    and doc["stage"] == "complete_"+manifest["stage"]+"_branch"
                    and doc["private_modes_receipt"]["sha256"] == prefix["whole_private_mode_prefix_sha256"]
                    and doc["private_modes_receipt"]["positive_modes"] == 2048
                    and doc["private_modes_receipt"]["all_sources_aliases_model_and_rounding_fees_retained"] is True
                    and result["complete_new_record_order"] == doc["completed_targets"]
                    and result["complete_new_record_count"] == 4 and result["complete_positive_modes"] == 2048,
                    "all2048 new signed modes and all four whole error balls")
            for key in ("private_vi_trial_receipt", "private_w_trial_receipt"):
                require(doc[key]["positive_modes"] == 2048 and doc[key]["exact_mean"] == "0"
                        and doc[key]["negative_modes_are_exact_conjugates"] is True
                        and doc[key]["complete_trial_only_restoration_without_error_targets"] is True,
                        "whole exact new signed carrier with a later carrier-only recovery")
            require(all(result[key] is True for key in (
                    "same_original_target_w_vi_minus_alpha", "same_original_target_B_Id_plus_same_sign_Tw_I",
                    "both_signed_modes_and_exact_zero_mean", "both_original_reflection_phases_retained",
                    "whole_original_raw_grid_alpha_SHA_identical", "one_original_quadrature_pass_only",
                    "all_infinite_tails_aliases_true_map_source_and_rounding_errors_retained",
                    "exact_rational_vi_minus_alpha_without_new_midpoint", "both_full_vi_and_w_Linf_L2_errors_proved"))
                    and all(result[key] is False for key in (
                    "old_cohomology_alpha_error_SN_norm_or_transport_targets_recomputed",
                    "physical_mean_slots_eliminated", "target_B_inverse_rows_certified",
                    "physical_PDE_or_full_Schur_proved", "topic_completion_proved")),
                    "same original target coefficient and all retained physical obligations")
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
                                state["last_published_complete_modes"] = prefix_doc["complete_mode_prefix"]["complete_modes"]
                                state["partial_prefix_publication_count"] = state.get("partial_prefix_publication_count", 0)+1
                                state["scientific_files"] = [dict(path=p, bytes=len(b), sha256=sha(b))
                                                               for p, b in staged.items()]
                                def prefix_files():
                                    receipt = encode(state)
                                    require(len(receipt) <= op["maximum_execution_bytes"], "whole BW prefix receipt")
                                    return {**staged, output_dir+"/execution.json": receipt}
                                publish(prefix_files, "visible-exact: preserve complete target w prefix")
'''

REPORT = '''        report = ("# Actual first complete signed target w carrier\\n\\nRun "+run+"/"+attempt
                  +"; complete: "+str(state["complete"])+".\\n\\n"
                  "The entire successful source192 ASR actual, execution and original input closure "
                  "are admitted. One necessary finite-carrier pass requires every old raw/grid/alpha "
                  "SHA and observes the same2048 original quadrature returns without changing them. "
                  "No old transport, cohomology, norm or alpha-error target repeats. The new vi "
                  "trial and exact rational w=vi-alpha carrier retain both signs, the true source "
                  "and target reflection phases, the original moving coefficient mean and both "
                  "independent physical means. Four whole new Linfinity/L2 error balls include "
                  "all sources, aliases, map errors, rounding and infinite tails. Private arrays "
                  "remain in the runner. Original B inverse rows, physical PDE matching and full "
                  "Schur completion remain independent obligations.\\n").encode()

'''


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("whole immutable publication engine changed")
    source = raw.decode()
    changes = {
        "R149_complete_reflected_finite_waist_row_inputs_v1": "R149_complete_target_w_signed_carrier_inputs_v1",
        '"reflected_finite_waist_rows"': '"target_w_signed_carrier"',
        'manifest["complete_record_counts"] == [96]': 'manifest["complete_record_counts"] == [4]',
        "one complete actual 96-row reflected-waist manifest": "one complete original target-w2048-mode manifest",
        "actual-reflected-waist-rows": "actual-target-w-signed-carrier",
        "R149_complete_reflected_finite_waist_rows_execution_v1": "R149_complete_target_w_signed_carrier_execution_v1",
        "consumed_R149_complete_reflected_finite_waist_rows_target_v1": "consumed_R149_complete_target_w_signed_carrier_target_v1",
        "whole_actual_conjugacy_inputs_reserved_for_one_new_complete_96row_target": "whole_successful_ASR_reserved_for_first_signed_target_w",
        "visible-exact: reserve exact reflected waist ": "visible-exact: reserve complete target w ",
        "visible-exact: preserve exact reflected waist ": "visible-exact: preserve complete target w ",
        'destination = source_dir / (spec["role"] + Path(spec["path"]).suffix)':
            'destination = source_dir / ("input_" + spec["role"] + Path(spec["path"]).suffix)',
        '{item["role"]: item for item in specs+history_specs})':
            '{item["role"]: item for item in specs+history_specs}, manifest)',
    }
    for old, new in changes.items():
        if old not in source:
            raise ValueError("the original target-w patch did not match: "+old)
        source = source.replace(old, new)
    start = source.index("    require(len(history_specs) == 4\n")
    end = source.index("    marker_path =", start)
    source = source[:start]+'''    require(history_specs == []
            and op["readme_pull_interval_seconds"] == 1800
            and op["automatic_scientific_retry"] is False,
            "whole original207-file native closure inherited through the complete ASR manifest")
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
    state["necessary_original_ASR_carrier_restoration"] = (result or {}).get("original_carrier_restoration")
    state["complete_original_quadrature_observation"] = (result or {}).get("private_quadrature_receipt")
    state["completed_new_vi_w_modes"] = (result or {}).get("complete_mode_prefix", {}).get("complete_modes", 0)
'''+old)
    start = source.index("        report = (", source.index("    def final_files():"))
    end = source.index("        return {**staged", start)
    source = source[:start]+REPORT+source[end:]
    return source


if __name__ == "__main__":
    exec(compile(patched_source(), __file__, "exec"), {"__name__": "__main__", "__file__": __file__})
