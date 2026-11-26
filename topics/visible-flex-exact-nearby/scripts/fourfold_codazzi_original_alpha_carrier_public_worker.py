"""AS public first target on the fixed complete RW publication engine.

The original207-file SN closure is restored privately inside the owner,
before importing numerical modules. Its manifest and all original current
texts are whole public inputs here; no closure is copied into new JSON.
"""
from pathlib import Path
import hashlib

BASE_NAME = "fourfold_codazzi_reflected_waist_rows_public_worker.py"
BASE_SHA256 = "9a474a43f065843af583edaab3bf774eddd845dab47a589aabe8cedcdd2b2490"

VALIDATOR = '''    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"], "whole complete AS result")
        doc = parse(raw)
        identity = doc["identity"]
        require(identity["kind"] == manifest["scientific_kind"]
                and identity["scalar_stage"] == manifest["stage"]
                and identity["source_sha256"] == by_role["science"]["sha256"]
                and identity["alpha_math_sha256"] == by_role["alpha_math"]["sha256"]
                and identity["SN_restore_sha256"] == by_role["SN_restore"]["sha256"]
                and identity["SN_manifest_sha256"] == by_role["SN_manifest"]["sha256"]
                and identity["SN_execution_sha256"] == by_role["SN_execution"]["sha256"]
                and identity["manifest_sha256"] == args.manifest_sha
                and identity["run_id"] == run and identity["run_attempt"] == attempt
                and identity["arithmetic_bits"] == 320, "same complete original source-alpha identity")
        count = doc["saved_record_count"]
        prefix = doc["complete_mode_prefix"]
        require(type(count) is int and 0 <= count <= 2
                and doc["completed_targets"] == manifest["target_order"][:count]
                and set(doc["new_records"]) == set(doc["completed_targets"])
                and doc["old_scientific_target_calls"] == 0
                and doc["necessary_original_input_rematerializations"] in (0, 1)
                and doc["new_arrays_published"] == doc["new_artifacts"] == doc["new_Releases"] == 0
                and doc["parameters"] == manifest["parameters"]
                and sorted(doc) == manifest["allowed_scientific_fields"]
                and type(prefix["complete_modes"]) is int and 0 <= prefix["complete_modes"] <= 2048,
                "whole saved original-alpha prefix without old mathematical target replay")
        if prefix["complete_modes"]:
            require(doc["original_endpoint_restoration"]["complete"] is True
                    and doc["original_endpoint_restoration"]["bytes"] == 245885
                    and doc["original_endpoint_restoration"]["sha256"]
                        == "3048266ba668164d7d9b5475c5262f1f3568cfe32a6e42c7bb496e4bda6c62b6"
                    and len(prefix["whole_private_mode_prefix_sha256"]) == 64,
                    "whole original endpoint required before every new completed mode")
            for key in ("head_Linf_upper", "head_L2_square_upper"):
                require(set(prefix[key]) == {"ball", "bound"} and prefix[key]["bound"] == "upper"
                        and isinstance(prefix[key]["ball"], str), "whole formal prefix accumulator")
        for value in doc["new_records"].values():
            require(set(value) == {"ball", "bound"} and value["bound"] == "upper"
                    and isinstance(value["ball"], str), "one complete new alpha error ball")
        if doc["complete"]:
            result = doc["result"]
            require(doc["proved"] is True and doc["actual_returncode"] == 0 and doc["failure"] is None
                    and count == 2 and prefix["complete_modes"] == 2048
                    and doc["candidate_record"] is None and doc["current_target"] is None
                    and doc["stage"] == "complete_"+manifest["stage"]+"_branch"
                    and doc["private_grid_receipt"]["complete_count"] == 8192
                    and doc["private_modes_receipt"]["positive_modes"] == 2048
                    and doc["private_modes_receipt"]["sha256"] == prefix["whole_private_mode_prefix_sha256"]
                    and doc["private_alpha_trial_receipt"]["positive_modes"] == 2048
                    and doc["private_alpha_trial_receipt"]["exact_mean"] == "0"
                    and doc["private_alpha_trial_receipt"]["carrier_only_restoration_does_not_repeat_mode_error_norms"] is True
                    and doc["original_input_restoration"]["complete_files"] == 207
                    and doc["original_input_restoration"]["complete_bytes"] == 13612391
                    and doc["necessary_original_input_rematerializations"] == 1
                    and result["complete_new_record_order"] == doc["completed_targets"]
                    and result["complete_new_record_count"] == 2 and result["complete_positive_modes"] == 2048,
                    "all original alpha modes and both complete norm errors")
            require(all(result[key] is True for key in (
                    "both_signed_modes_and_exact_zero_mean", "same_original_alpha_vi_minus_w",
                    "actual_source_phase_b_a_plus_Omega_retained", "original_divisor_and_all_infinite_tails_paid",
                    "both_full_Linf_and_L2_trial_errors_proved", "old_complete_SN_endpoint_SHA_required_and_verified"))
                    and all(result[key] is False for key in (
                    "all_old_SN_validation_norm_or_cohomology_targets_replayed", "physical_mean_slots_eliminated",
                    "actual_Theta_or_full_Schur_proved", "topic_completion_proved")),
                    "same true operator, all phases/means and retained final obligations")
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
                                    require(len(receipt) <= op["maximum_execution_bytes"], "whole prefix execution receipt")
                                    return {**staged, output_dir+"/execution.json": receipt}
                                publish(prefix_files, "visible-exact: preserve original alpha complete carrier prefix")
'''

REPORT = '''        report = ("# Actual complete original source alpha carrier\\n\\nRun "+run+"/"+attempt
                  +"; complete: "+str(state["complete"])+".\\n\\n"
                  "The entire successful SN receipt and its original207-file closure are admitted. "
                  "Only original finite point proposals are rematerialized, with the full original "
                  "two-branch245885-byte endpoint SHA required before use. No old SN residual, "
                  "energy, norm, KAM or cohomological target is repeated. One new2048-mode real "
                  "mean-zero alpha carrier retains the actual b=a+Omega phase, complete moving "
                  "means, true H/G difference, all quadrature aliases and the entire infinite "
                  "tail. Both complete Linfinity and L2 errors are saved. Private carriers stay "
                  "in the runner. Original A/Theta composition, physical means, true PDE matching "
                  "and full nonlinear completion remain separate obligations.\\n").encode()

'''


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("whole immutable publication engine changed")
    source = raw.decode()
    changes = {
        "R149_complete_reflected_finite_waist_row_inputs_v1": "R149_complete_original_alpha_carrier_inputs_v1",
        '"reflected_finite_waist_rows"': '"original_alpha_signed_carrier"',
        'manifest["complete_record_counts"] == [96]': 'manifest["complete_record_counts"] == [2]',
        "one complete actual 96-row reflected-waist manifest": "one complete original-alpha2048-mode manifest",
        "actual-reflected-waist-rows": "actual-original-alpha-carrier",
        "R149_complete_reflected_finite_waist_rows_execution_v1": "R149_complete_original_alpha_carrier_execution_v1",
        "consumed_R149_complete_reflected_finite_waist_rows_target_v1": "consumed_R149_complete_original_alpha_carrier_target_v1",
        "whole_actual_conjugacy_inputs_reserved_for_one_new_complete_96row_target": "whole_SN_inputs_reserved_for_one_new_original_alpha_carrier",
        "visible-exact: reserve exact reflected waist ": "visible-exact: reserve original alpha ",
        "visible-exact: preserve exact reflected waist ": "visible-exact: preserve original alpha ",
        'destination = source_dir / (spec["role"] + Path(spec["path"]).suffix)':
            'destination = source_dir / ("input_" + spec["role"] + Path(spec["path"]).suffix)',
    }
    for old, new in changes.items():
        if old not in source:
            raise ValueError("the original AS task patch did not match: "+old)
        source = source.replace(old, new)
    start = source.index("    require(len(history_specs) == 4\n")
    end = source.index("    marker_path =", start)
    source = source[:start]+'''    require(history_specs == []
            and op["readme_pull_interval_seconds"] == 1800
            and op["automatic_scientific_retry"] is False,
            "complete original207-file SN restoration is inherited from its whole pinned manifest")
'''+source[end:]
    start = source.index("    def validate_output(raw):\n")
    end = source.index("    try:\n        head = pull()\n", start)
    source = source[:start]+VALIDATOR+source[end:]
    periodic = "                        pull()\n                    except BaseException as exc:\n"
    if source.count(periodic) != 1:
        raise ValueError("the unique periodic complete-pull block changed")
    source = source.replace(periodic, PERIODIC+"                    except BaseException as exc:\n")
    old = '    state["finished_utc"] = utc()\n'
    if source.count(old) != 1:
        raise ValueError("the original final receipt block changed")
    source = source.replace(old, '''    state["old_numerical_producers_called"] = (result or {}).get("necessary_original_input_rematerializations", 0)
    state["necessary_original_SN_endpoint_restoration"] = (result or {}).get("original_endpoint_restoration")
    state["complete_original_SN_input_restoration"] = (result or {}).get("original_input_restoration")
    state["completed_original_alpha_modes"] = (result or {}).get("complete_mode_prefix", {}).get("complete_modes", 0)
'''+old)
    start = source.index("        report = (", source.index("    def final_files():"))
    end = source.index("        return {**staged", start)
    source = source[:start]+REPORT+source[end:]
    return source


if __name__ == "__main__":
    exec(compile(patched_source(), __file__, "exec"), {"__name__": "__main__", "__file__": __file__})
