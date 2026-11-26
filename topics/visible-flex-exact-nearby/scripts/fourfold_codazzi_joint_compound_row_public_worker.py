"""JC public worker: reuse the fixed RW restoration and publication engine.

Only the new task identity, seven-scalar output validation and report differ.
The four original native restorations, README checks, full capacity accounting,
single-child rule and non-fast-forward publication loop remain byte-for-byte.
"""
from pathlib import Path
import hashlib

BASE_NAME = "fourfold_codazzi_reflected_waist_rows_public_worker.py"
BASE_SHA256 = "9a474a43f065843af583edaab3bf774eddd845dab47a589aabe8cedcdd2b2490"

VALIDATOR = '''    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"], "whole JC scalar stage")
        doc = parse(raw)
        identity = doc["identity"]
        require(identity["kind"] == manifest["scientific_kind"]
                and identity["scalar_stage"] == manifest["stage"]
                and identity["source_sha256"] == by_role["science"]["sha256"]
                and identity["joint_math_sha256"] == by_role["joint_math"]["sha256"]
                and identity["manifest_sha256"] == args.manifest_sha
                and identity["run_id"] == run and identity["run_attempt"] == attempt
                and identity["arithmetic_bits"] == manifest["parameters"]["arithmetic_bits"],
                "same whole JC source, selected object and actual run")
        count = doc["saved_record_count"]
        require(type(count) is int and 0 <= count <= 7
                and doc["completed_targets"] == manifest["target_order"][:count]
                and set(doc["new_records"]) == set(doc["completed_targets"])
                and doc["old_scientific_target_calls"] == 0
                and doc["new_arrays_published"] == doc["new_artifacts"] == doc["new_Releases"] == 0
                and doc["parameters"] == manifest["parameters"]
                and sorted(doc) == manifest["allowed_scientific_fields"],
                "complete saved JC prefix with no old-target replay")
        for i, name in enumerate(doc["completed_targets"]):
            record = doc["new_records"][name]
            require(set(record) == {"ball", "bound"}
                    and isinstance(record["ball"], str)
                    and record["bound"] == ("lower" if i < 3 else "upper"),
                    "every entire new directed scalar is saved")
        if doc["complete"]:
            require(count == 7 and doc["proved"] is True
                    and doc["failure"] is None and doc["actual_returncode"] == 0
                    and doc["candidate_record"] is None and doc["current_target"] is None
                    and doc["stage"] == "complete_"+manifest["stage"]+"_scalar_branch"
                    and doc["result"]["complete_new_record_order"] == doc["completed_targets"]
                    and doc["result"]["complete_new_record_count"] == 7
                    and doc["result"]["complete_joint_row_operator_error_proved"] is True
                    and doc["result"]["strict_positive_saved_homotopy_lower"] is True
                    and doc["result"]["all_DFT_alias_and_infinite_compound_tails_paid"] is True
                    and doc["result"]["all_dependent_scalars_use_formal_readback_bounds"] is True
                    and doc["result"]["original_RW_trials_unchanged"] is True
                    and doc["result"]["signed_PDE_columns_or_finite_inverse_proved"] is False
                    and doc["result"]["full_nu_phase_mean_Schur_proved"] is False
                    and doc["result"]["topic_completion_proved"] is False,
                    "complete JC theorem and its retained full-PDE obligations")
        return doc

'''

REPORT = '''        report = ("# Actual joint96 compound waist-row error\\n\\nRun "+run+"/"+attempt
                  +"; stage: "+manifest["stage"]+"; complete: "+str(state["complete"])+".\\n\\n"
                  "The child reads the whole original W/R31/K48/H and fixed normalizer records. "
                  "It computes only seven new joint-row scalar bounds. Every lower or upper is "
                  "saved and read back before it is used by a later scalar. Original DFT rows, "
                  "KAM, PDE residuals and old norm targets are not repeated. Full P224, true "
                  "PDE column errors, signed matrices and physical Schur conditions remain.\\n").encode()

'''


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("whole immutable RW worker source changed")
    source = raw.decode("utf-8")
    replacements = {
        "R149_complete_reflected_finite_waist_row_inputs_v1": "R149_complete_joint_compound_row_inputs_v1",
        '"reflected_finite_waist_rows"': '"joint_compound_waist_row_error"',
        'manifest["complete_record_counts"] == [96]': 'manifest["complete_record_counts"] == [7]',
        "one complete actual 96-row reflected-waist manifest": "one complete actual seven-scalar joint-row manifest",
        "actual-reflected-waist-rows": "actual-joint-compound-waist-row-error",
        "R149_complete_reflected_finite_waist_rows_execution_v1": "R149_complete_joint_compound_row_execution_v1",
        "consumed_R149_complete_reflected_finite_waist_rows_target_v1": "consumed_R149_complete_joint_compound_row_target_v1",
        "whole_actual_conjugacy_inputs_reserved_for_one_new_complete_96row_target": "whole_actual_conjugacy_inputs_reserved_for_seven_new_joint_scalars",
        "reserve exact reflected waist ": "reserve joint compound waist rows ",
        "preserve exact reflected waist ": "preserve joint compound waist rows ",
    }
    for old, new in replacements.items():
        if old not in source:
            raise ValueError("fixed RW task patch did not match: "+old)
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
