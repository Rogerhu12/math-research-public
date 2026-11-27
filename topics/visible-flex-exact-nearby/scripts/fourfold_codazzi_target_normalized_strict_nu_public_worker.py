"""Public first BNC column on the whole immutable publication engine."""
from pathlib import Path
import hashlib

BASE_NAME = "fourfold_codazzi_reflected_waist_rows_public_worker.py"
BASE_SHA256 = "9a474a43f065843af583edaab3bf774eddd845dab47a589aabe8cedcdd2b2490"

VALIDATOR = '''    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"], "one whole new true B-normalized parameter column")
        doc = parse(raw)
        ident = doc["identity"]
        require(ident["kind"] == manifest["scientific_kind"] and ident["scalar_stage"] == manifest["stage"]
                and ident["source_sha256"] == by_role["science"]["sha256"]
                and ident["manifest_sha256"] == args.manifest_sha
                and ident["run_id"] == run and ident["run_attempt"] == attempt
                and ident["arithmetic_bits"] == 320
                and ident["whole_parent_identities"] == {
                    tag: {name: by_role[tag+"_"+name]["sha256"] for name in ("manifest", "actual", "execution")}
                    for tag in ("NP", "PO", "SB", "DW")},
                "the whole actual result is bound to all four complete original parents")
        count, modes = doc["saved_record_count"], doc["complete_observation_modes"]
        require(type(count) is int and 0 <= count <= 7 and type(modes) is int and 0 <= modes <= 192
                and doc["completed_targets"] == manifest["target_order"][:count]
                and set(doc["new_records"]) == set(doc["completed_targets"])
                and doc["parameters"] == manifest["parameters"]
                and sorted(doc) == manifest["allowed_scientific_fields"]
                and doc["old_scientific_target_calls"] == 0
                and doc["necessary_carrier_rematerializations"] in (0, 1)
                and doc["new_arrays_published"] == doc["new_artifacts"] == doc["new_Releases"] == 0,
                "the entire natural first target prefix, with no old target replay")
        require(doc["whole_completed_inputs"] == {
                    "all_descriptors_sha256": manifest["complete_input_descriptors_sha256"],
                    "current_objects": len(manifest["files"]),
                    "historical_objects": len(manifest["historical_inputs"]),
                    "all_parent_bindings_recovered_from_whole_original_manifests": True},
                "all original inputs remain complete through their original manifests")
        for name in manifest["target_order"][:min(count, 6)]:
            record = doc["new_records"][name]
            require(set(record) == {"ball", "bound"} and record["bound"] == "upper"
                    and isinstance(record["ball"], str), "one whole new nonnegative formal component")
        if modes or count:
            restored = doc["carrier_restoration"]
            br, np_input = doc["necessary_B_row_carrier_receipt"], doc["necessary_NP_trial_receipt"]
            require(restored["complete"] is True and restored["failure"] is None
                    and restored["result"]["whole_original_endpoint_raw_grid_SHA_required"] is True
                    and restored["result"]["old_alpha_trial_materialized_or_used"] is False
                    and restored["result"]["old_quadrature_or_cohomological_mode_calls"] == 0
                    and br["complete"] is True and br["all_complete_original_carrier_SHA_matched"] is True
                    and br["old_DWT_coefficient_error_targets_called"] == br["old_DWT_whole_error_targets_called"]
                        == br["old_BR_residual_norm_targets_called"] == 0
                    and br["new_row_trial_selected"] is False
                    and br["row_trial"]["rows"] == 96 and br["row_trial"]["positive_modes"] == 192
                    and np_input["all_four_complete_arrays_read_back"] is True
                    and len(np_input["complete_original_array_receipts"]) == 4
                    and all(item["shape"] == [740, 193] for item in np_input["complete_original_array_receipts"])
                    and np_input["old_residual_cells_evaluated"] == np_input["old_signed_pairings_evaluated"]
                        == np_input["old_scientific_norm_targets_evaluated"] == 0
                    and np_input["new_trial_selected"] is False,
                    "both necessary old whole carrier identities precede every new physical observation")
            require(doc["private_physical_grid_receipt"]["nodes"] == 8192
                    and doc["private_physical_grid_receipt"]["source_positive_modes"] == 96
                    and doc["private_physical_grid_receipt"]["whole_original_G_phase_retained"] is True
                    and doc["private_unit_disk_input_receipt"]["nodes"] == 8192
                    and doc["private_unit_disk_input_receipt"]["all_complete_point_centers_and_radii_read_back"] is True,
                    "the whole new physical source and full unshifted G input")
        if count:
            require(modes == 192 and doc["private_complete_observation_receipt"]["complete_positive_modes"] == 192
                    and doc["private_complete_observation_receipt"]["complete_grid_points_per_mode"] == 8192
                    and doc["private_complete_observation_receipt"]["all_complete_modes_read_back"] is True
                    and doc["private_exact_column_receipt"]["rows"] == 96
                    and doc["private_exact_column_receipt"]["all_signs_and_complete192_row_support_retained"] is True,
                    "no incomplete mode prefix or projected row substitutes for the whole new column")
        if count == 7:
            signed = doc["new_records"][manifest["target_order"][6]]
            require(signed["kind"] == "BNC_complete_true_target_normalized_strict_nu_column_v1"
                    and signed["rows"] == len(signed["all96_exact_signed_trial_rationals"])
                        == len(signed["all96_true_signed_balls"]) == 96
                    and all(isinstance(value, str) for value in signed["all96_exact_signed_trial_rationals"])
                    and [value["row"] for value in signed["all96_true_signed_balls"]] == list(range(1, 97))
                    and all(set(value) == {"row", "ball", "bound"}
                            and isinstance(value["ball"], str) and value["bound"] == "signed_enclosure"
                            for value in signed["all96_true_signed_balls"])
                    and signed["joint_l2_error_upper"] == doc["new_records"][manifest["target_order"][5]]
                    and set(signed["prior_two_independent_density_mean_balls"]) == {"plus", "minus"}
                    and signed["physical_mean_slots_eliminated"] is False
                    and signed["nonlocal_phase_or_mean_height_column_claimed"] is False
                    and signed["true_full_physical_high_forcing_retained"] is True
                    and signed["whole_physical_column_used"] is True
                    and signed["original_target_normalizer_and_true_phase_retained"] is True,
                    "all96 true signed target coordinates, the stronger joint error and both independent means")
        if doc["complete"]:
            require(doc["proved"] is True and doc["failure"] is None and doc["actual_returncode"] == 0
                    and count == 7 and doc["current_target"] is doc["candidate_record"] is None
                    and doc["stage"] == "complete_"+manifest["stage"]+"_scalar_branch"
                    and doc["result"]["complete_new_record_count"] == 7
                    and doc["result"]["complete_new_record_order"] == manifest["target_order"]
                    and doc["result"]["complete_true_target_normalized_signed_rows"] == 96
                    and doc["result"]["joint_l2_column_error_proved"] is True
                    and doc["result"]["all_row_PDE_compound_alias_and_disk_fees_retained"] is True
                    and doc["result"]["both_independent_physical_means_retained"] is True
                    and doc["result"]["old_completed_scientific_targets_recomputed"] is False
                    and doc["result"]["full_homogeneous_inverse_or_high_Schur_proved"] is False
                    and doc["result"]["topic_completion_proved"] is False,
                    "the entire new column is complete; unrelated full-Schur obligations remain")
        else:
            require(doc["proved"] is False and doc["actual_returncode"] in (None, 1),
                    "an actual retained prefix is not declared a complete column")
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
                                state["last_published_complete_observation_modes"] = prefix_doc["complete_observation_modes"]
                                state["partial_prefix_publication_count"] = state.get("partial_prefix_publication_count", 0)+1
                                state["scientific_files"] = [dict(path=p, bytes=len(b), sha256=sha(b))
                                                               for p, b in staged.items()]
                                def prefix_files():
                                    receipt = encode(state)
                                    require(len(receipt) <= op["maximum_execution_bytes"], "whole BR prefix receipt")
                                    return {**staged, output_dir+"/execution.json": receipt}
                                publish(prefix_files, "visible-exact: preserve complete original B inverse-row prefix")
'''

REPORT = '''        report = ("# Actual first target-normalized strict parameter column\\n\\nRun "+run+"/"+attempt
                  +"; complete: "+str(state["complete"])+".\\n\\n"
                  "The complete mathematical outcome is in the paired actual JSON and execution receipt. "
                  "Every original NP, PO, ASB, JC and DWTB input is retained in full under its original identity. "
                  "Only necessary input carriers are restored; all old scalar, residual, norm and pairing targets remain completed inputs.\\n\\n"
                  "The new work forms all192 full physical observations and the complete96 signed target coordinates, "
                  "with full row, PDE, composition, infinite alias and disk errors. The true phase and both independent means remain. "
                  "A retained partial prefix is not a complete column or a full Schur certificate.\\n").encode()

'''

def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("the complete immutable public publication engine changed")
    source = raw.decode()
    changes = {
        "R149_complete_reflected_finite_waist_row_inputs_v1": "R147_complete_target_normalized_strict_nu_column_inputs_v1",
        '"reflected_finite_waist_rows"': '"target_normalized_strict_nu_column"',
        'manifest["complete_record_counts"] == [96]': 'manifest["complete_record_counts"] == [7]',
        "one complete actual 96-row reflected-waist manifest": "one complete first target-normalized strict-parameter column manifest",
        "actual-reflected-waist-rows": "actual-target-normalized-strict-nu-column",
        "R149_complete_reflected_finite_waist_rows_execution_v1": "R147_complete_target_normalized_strict_nu_column_execution_v1",
        "consumed_R149_complete_reflected_finite_waist_rows_target_v1": "consumed_R147_complete_target_normalized_strict_nu_column_v1",
        "whole_actual_conjugacy_inputs_reserved_for_one_new_complete_96row_target": "whole_completed_DWTB_and_NP_inputs_reserved_for_first_BNC_column",
        "visible-exact: reserve exact reflected waist ": "visible-exact: reserve first B-normalized parameter column ",
        "visible-exact: preserve exact reflected waist ": "visible-exact: preserve first B-normalized parameter column ",
        'destination = source_dir / (spec["role"] + Path(spec["path"]).suffix)':
            'destination = source_dir / ("input_" + spec["role"] + Path(spec["path"]).suffix)',
        '{item["role"]: item for item in specs+history_specs})':
            '{item["role"]: item for item in specs+history_specs}, manifest, snapshots)',
        'state["current_input_receipts"] = specs':
            'state["current_input_receipts"] = {"reconstruct_from": "whole manifest.files", "manifest_sha256": args.manifest_sha, "complete_count": len(specs), "complete_descriptors_sha256": sha(encode(specs))}',
    }
    for old, new in changes.items():
        if old not in source:
            raise ValueError("the complete BNC publication adaptation did not match: "+old)
        source = source.replace(old, new)
    start = source.index("    require(len(history_specs) == 4\n")
    end = source.index("    marker_path =", start)
    source = source[:start]+'''    require(len(history_specs) == manifest["expected_historical_input_count"] == 51
            and op["readme_pull_interval_seconds"] == 1800
            and op["automatic_scientific_retry"] is False,
            "the whole original NP native closure, with all shared W/H/K definitions")
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
        raise ValueError("the original complete final receipt block changed")
    source = source.replace(old, '''    state["old_numerical_producers_called"] = (result or {}).get("necessary_carrier_rematerializations", 0)
    state["necessary_original_grid_restoration"] = (result or {}).get("carrier_restoration")
    state["necessary_original_B_row_restoration"] = (result or {}).get("necessary_B_row_carrier_receipt")
    state["necessary_original_NP_trial_restoration"] = (result or {}).get("necessary_NP_trial_receipt")
    state["completed_new_physical_observations"] = (result or {}).get("complete_observation_modes", 0)
    state["complete_new_exact_column_receipt"] = (result or {}).get("private_exact_column_receipt")
'''+old)
    start = source.index("        report = (", source.index("    def final_files():"))
    end = source.index("        return {**staged", start)
    source = source[:start]+REPORT+source[end:]
    return source


if __name__ == "__main__":
    exec(compile(patched_source(), __file__, "exec"), {"__name__": "__main__", "__file__": __file__})
