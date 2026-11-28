"""One public BGR3 execution using the existing complete publication engine."""
from pathlib import Path
import hashlib

BASE_NAME = "fourfold_codazzi_reflected_waist_rows_public_worker.py"
BASE_SHA256 = "9a474a43f065843af583edaab3bf774eddd845dab47a589aabe8cedcdd2b2490"

VALIDATOR = '''    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"], "whole new BGR3 result")
        doc = parse(raw)
        ident = doc["identity"]
        require(ident["kind"] == manifest["scientific_kind"] and ident["scalar_stage"] == manifest["stage"]
                and ident["manifest_sha256"] == args.manifest_sha
                and ident["source_sha256"] == by_role["science"]["sha256"]
                and ident["run_id"] == run and ident["run_attempt"] == attempt,
                "whole actual BGR3 identity")
        count = doc["saved_record_count"]
        require(type(count) is int and 0 <= count <= 3
                and doc["completed_targets"] == manifest["target_order"][:count]
                and set(doc["new_records"]) == set(doc["completed_targets"])
                and sorted(doc) == manifest["allowed_scientific_fields"]
                and doc["parameters"] == manifest["parameters"]
                and doc["old_scientific_target_calls"] == 0
                and all(doc[name] == 0 for name in ("new_arrays_published", "new_artifacts", "new_Releases")),
                "every whole BGR3 field, full target prefix and unchanged old-target count")
        require(all(set(value) == {"ball", "bound"} and value["bound"] == "upper"
                    and isinstance(value["ball"], str) for value in doc["new_records"].values()),
                "each saved new bound has its full directed ball")
        if count:
            require(doc["complete_Gram_receipt"]["shape"] == [96, 96]
                    and doc["complete_Gram_receipt"]["all_signed_entries_saved_before_norm"] is True
                    and doc["row_restoration"]["all_complete_original_carrier_SHA_matched"] is True,
                    "the entire Gram follows all original SHA-matched rows")
        if doc["complete"]:
            require(count == 3 and doc["proved"] is True and doc["actual_returncode"] == 0
                    and doc["failure"] is None and doc["current_target"] is None
                    and doc["result"]["complete_whole_same_operator_row_bound_proved"] is True
                    and doc["result"]["full_Schur_or_final_closed_family_proved"] is False,
                    "the completed whole row estimate keeps its exact mathematical scope")
        return doc

'''


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("the complete existing publication engine changed")
    source = raw.decode()
    changes = {
        "R149_complete_reflected_finite_waist_row_inputs_v1": "R149_complete_target_B_Gram_inputs_v1",
        '"reflected_finite_waist_rows"': '"target_B_Gram"',
        'manifest["complete_record_counts"] == [96]': 'manifest["complete_record_counts"] == [3]',
        "one complete actual 96-row reflected-waist manifest": "one complete new BGR3 manifest",
        "actual-reflected-waist-rows": "actual-target-B-Gram",
        "R149_complete_reflected_finite_waist_rows_execution_v1": "R149_complete_target_B_Gram_execution_v1",
        "consumed_R149_complete_reflected_finite_waist_rows_target_v1": "consumed_R149_complete_target_B_Gram_v1",
        "whole_actual_conjugacy_inputs_reserved_for_one_new_complete_96row_target": "whole_original_DWTB9_reserved_for_three_new_Gram_targets",
        "visible-exact: reserve exact reflected waist ": "visible-exact: reserve three new complete B Gram ",
        "visible-exact: preserve exact reflected waist ": "visible-exact: preserve three new complete B Gram ",
        'destination = source_dir / (spec["role"] + Path(spec["path"]).suffix)':
            'destination = source_dir / ("input_" + spec["role"] + Path(spec["path"]).suffix)',
        'target = history_dir/(spec["role"]+".json.gz")': 'target = history_dir/topic_path(spec["path"])',
        '{item["role"]: item for item in specs+history_specs})':
            '{item["role"]: item for item in specs+history_specs}, manifest, snapshots)',
        'state["current_input_receipts"] = specs':
            'state["current_input_receipts"] = {"reconstruct_from": "whole manifest.files", "manifest_sha256": args.manifest_sha, "complete_count": len(specs), "complete_descriptors_sha256": sha(encode(specs))}',
    }
    for old, new in changes.items():
        if old not in source:
            raise ValueError("the exact BGR engine adaptation did not match: "+old)
        source = source.replace(old, new)
    start = source.index("    require(len(history_specs) == 4\n")
    end = source.index("    marker_path =", start)
    source = source[:start]+'''    require(len(history_specs) == manifest["expected_historical_input_count"] == 51
            and op["readme_pull_interval_seconds"] == 1800
            and op["automatic_scientific_retry"] is False,
            "all original whole carrier inputs, periodic rule checks and no old-target retry")
'''+source[end:]
    start = source.index("    def validate_output(raw):\n")
    end = source.index("    try:\n        head = pull()\n", start)
    source = source[:start]+VALIDATOR+source[end:]
    start = source.index("        report = (", source.index("    def final_files():"))
    end = source.index("        return {**staged", start)
    source = source[:start]+'''        report = ("# Actual complete target B trial Gram\\n\\nRun "+run+"/"+attempt
                  +"; complete: "+str(state["complete"])+".\\n\\n"
                  "The complete original DWTB9, exact full row carriers and both frequency signs are retained. "
                  "Only the full signed 96x96 Gram, its new infinity product and whole row-error bound are new targets. "
                  "No old residual, norm, BNC observation or BFP target is recomputed. "
                  "Read the complete actual and execution together; full Schur and the nonlinear closed family remain open.\\n").encode()

'''+source[end:]
    return source


if __name__ == "__main__":
    exec(compile(patched_source(), __file__, "exec"), {"__name__": "__main__", "__file__": __file__})
