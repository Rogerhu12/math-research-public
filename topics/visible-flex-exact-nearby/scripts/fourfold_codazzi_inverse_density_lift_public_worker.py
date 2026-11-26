"""IL task adapter for the fixed whole-input RW publication worker.

It restores six entire original native files; only four NEW scalar targets
run. All complete capacity, periodic README and immediate rebase/push rules
of the byte-pinned publication engine remain in force.
"""
from pathlib import Path
import hashlib

BASE_NAME = "fourfold_codazzi_reflected_waist_rows_public_worker.py"
BASE_SHA256 = "9a474a43f065843af583edaab3bf774eddd845dab47a589aabe8cedcdd2b2490"

VALIDATOR = '''    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"], "entire IL scientific object")
        doc = parse(raw)
        identity = doc["identity"]
        require(identity["kind"] == manifest["scientific_kind"]
                and identity["scalar_stage"] == manifest["stage"]
                and identity["source_sha256"] == by_role["science"]["sha256"]
                and identity["DC_math_sha256"] == by_role["DC_math"]["sha256"]
                and identity["manifest_sha256"] == args.manifest_sha
                and identity["run_id"] == run and identity["run_attempt"] == attempt
                and identity["arithmetic_bits"] == manifest["parameters"]["arithmetic_bits"],
                "same original inverse lift, complete new source and actual run")
        count = doc["saved_record_count"]
        require(type(count) is int and 0 <= count <= 4
                and doc["completed_targets"] == manifest["target_order"][:count]
                and set(doc["new_records"]) == set(doc["completed_targets"])
                and doc["old_scientific_target_calls"] == 0
                and doc["new_arrays_published"] == doc["new_artifacts"] == doc["new_Releases"] == 0
                and doc["parameters"] == manifest["parameters"]
                and sorted(doc) == manifest["allowed_scientific_fields"],
                "complete IL prefix and no old target replay")
        for name in doc["completed_targets"]:
            record = doc["new_records"][name]
            require(set(record) == {"ball", "bound"}
                    and isinstance(record["ball"], str) and record["bound"] == "upper",
                    "every entire new directed scalar is preserved")
        if doc["complete"]:
            result = doc["result"]
            require(count == 4 and doc["proved"] is True
                    and doc["failure"] is None and doc["actual_returncode"] == 0
                    and doc["candidate_record"] is None and doc["current_target"] is None
                    and doc["stage"] == "complete_"+manifest["stage"]+"_scalar_branch"
                    and result["complete_new_record_order"] == doc["completed_targets"]
                    and result["complete_new_record_count"] == 4
                    and result["whole_original_inverse_lift_error_proved"] is True
                    and result["all_three_trial_derivative_bounds_proved"] is True
                    and result["original_full_terminal_coefficients_and_means_retained"] is True
                    and result["same_selected_parameter_and_true_root_used"] is True
                    and result["all_old_unprojected_transport_and_root_fees_retained"] is True
                    and result["all_new_scalars_saved_and_read_back"] is True
                    and result["new_or_old_ray_ODE_called"] is False
                    and result["complete_density_compression_rows_proved"] is False
                    and result["whole_Theta_one_loss_paid"] is False
                    and result["full_nu_phase_mean_Schur_proved"] is False
                    and result["topic_completion_proved"] is False,
                    "whole original inverse lift, with every remaining PDE and Schur obligation")
        return doc

'''

REPORT = '''        report = ("# Actual original inverse-density lift\\n\\nRun "+run+"/"+attempt
                  +"; complete: "+str(state["complete"])+".\\n\\n"
                  "Six entire original native objects are restored byte for byte. The "
                  "original complete cover and widened Wiener native have identical two-leg "
                  "terminal coefficients, including both central means. The only new targets "
                  "are the same selected inverse-lift error on physical strip1/256 and three "
                  "whole real-axis derivatives of K48 composed with the original second leg. "
                  "No original flow, KAM, fit, DFT or norm target is repeated. New density "
                  "compression rows, whole Theta one-loss, true PDE matrices and the full "
                  "physical nu/phase/mean Schur condition remain separate.\\n").encode()

'''


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("whole immutable RW publication source changed")
    source = raw.decode()
    replacements = {
        "R149_complete_reflected_finite_waist_row_inputs_v1": "R149_complete_inverse_density_lift_inputs_v1",
        '"reflected_finite_waist_rows"': '"original_inverse_density_lift"',
        'manifest["complete_record_counts"] == [96]': 'manifest["complete_record_counts"] == [4]',
        "one complete actual 96-row reflected-waist manifest": "one complete four-scalar original inverse-lift manifest",
        "actual-reflected-waist-rows": "actual-original-inverse-density-lift",
        "R149_complete_reflected_finite_waist_rows_execution_v1": "R149_complete_inverse_density_lift_execution_v1",
        "consumed_R149_complete_reflected_finite_waist_rows_target_v1": "consumed_R149_complete_inverse_density_lift_target_v1",
        "whole_actual_conjugacy_inputs_reserved_for_one_new_complete_96row_target": "whole_original_one_leg_inputs_reserved_for_four_new_scalars",
        "visible-exact: reserve exact reflected waist ": "visible-exact: reserve original inverse-density lift ",
        "visible-exact: preserve exact reflected waist ": "visible-exact: preserve original inverse-density lift ",
        'require(len(history_specs) == 4': 'require(len(history_specs) == 6',
        '== {"W_native", "R31_native", "K_native", "H_native"}':
            '== {"W_native", "R31_native", "K_native", "H_native", "terminal_cover_native", "wiener_native"}',
        'and 0 < item["bytes"] < 100000 for item in history_specs)':
            'and 0 < item["bytes"] < 200000 for item in history_specs)',
        "four whole immutable native inputs, periodic rule check and no science retry":
            "six whole immutable native inputs, periodic rule check and no science retry",
        'destination = source_dir / (spec["role"] + Path(spec["path"]).suffix)':
            'destination = source_dir / ("input_" + spec["role"] + Path(spec["path"]).suffix)',
    }
    for old, new in replacements.items():
        if old not in source:
            raise ValueError("fixed whole RW task patch did not match: "+old)
        source = source.replace(old, new)
    start = source.index("    def validate_output(raw):\n")
    end = source.index("    try:\n        head = pull()\n", start)
    source = source[:start]+VALIDATOR+source[end:]
    start = source.index("        report = (", source.index("    def final_files():"))
    end = source.index("        return {**staged", start)
    source = source[:start]+REPORT+source[end:]
    return source


if __name__ == "__main__":
    exec(compile(patched_source(), __file__, "exec"),
         {"__name__": "__main__", "__file__": __file__})
