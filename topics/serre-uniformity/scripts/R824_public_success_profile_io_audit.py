#!/usr/bin/env python3
"""Read only selected original R824 success members over immutable ZIP64 HTTP Range."""
import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R824-public-success-profile-io-audit-request.json"
IO_NAME = "R824_public_original_global_polar_generators.py"
IO_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
RESULT = "R824-existing-global-generator-profile-IO-review"
ORIGINAL = "R824-original-global-polar-generators"
CERT = "p41-original-global-polar-generators-certificate.json"
REFERENCE = "full-outputs-manifest-reference.json"


def sha(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            value.update(block)
    return value.hexdigest()


assert sha(S/IO_NAME) == IO_SHA
loader = importlib.util.spec_from_file_location("R824_profile_frozen_IO", S/IO_NAME)
IO = importlib.util.module_from_spec(loader)
loader.loader.exec_module(IO)


def bootstrap_reference(archive, selected):
    """The small reference is read from the same immutable, identity-checked artifact."""
    members = archive.by_name.get(REFERENCE, [])
    assert len(members) == 1 and 0 < members[0].file_size < 1024*1024
    with archive.zip.open(members[0], "r") as stream:
        raw = stream.read(1024*1024+1)
    assert len(raw) == members[0].file_size
    data = json.loads(raw)
    assert data["result"] == ORIGINAL and data["manifest_file"] == "full-outputs-manifest.json"
    assert IO.H64.fullmatch(data["manifest_sha256"])
    assert data["manifest_bytes"] > 0 and data["file_count"] == 359
    assert data["full_outputs_artifact"] == archive.item["artifact_name"]
    path = selected/REFERENCE
    path.write_bytes(raw)
    return data, IO.file_spec(path)


def run(out):
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    request = IO.read(REQUEST)
    item = dict(request["original_producer"])
    assert request["io_helper_sha256"] == sha(S/IO_NAME) == IO_SHA
    assert request["audit_script_sha256"] == sha(__file__)
    assert sha(REPO/"README.md") == request["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md") == request["readme_sha256"]["topic"]
    assert item["result"] == ORIGINAL
    assert item["core_sha256"] == "1ece3cf45f57fda2d1fe40f38efb3e225d2e05ce910a917eb38dbcd85fe3d1cb"
    out.mkdir(parents=True, exist_ok=True)
    selected = out/"selected-original-R824"
    selected.mkdir(parents=True, exist_ok=True)
    archive = IO.Archive(item, out.parent/"range-transfer", whole=False)
    try:
        reference, reference_spec = bootstrap_reference(archive, selected)
        if item.get("manifest_sha256") is not None:
            assert item["manifest_sha256"] == reference["manifest_sha256"]
        item["manifest_sha256"] = reference["manifest_sha256"]
        path = archive.extract_bound("full-outputs-manifest.json", item["manifest_sha256"],
                                     selected/"full-outputs-manifest.json", reference["manifest_bytes"])
        source = IO.Producer("R824", item, selected, archive)
        assert len(source.files) == reference["file_count"] == 359
        cert = source.certificate
        assert IO.file_spec(selected/CERT) == request["expected_certificate"]
        assert cert["completed_requested_scopes"] == ["common_operators", "modular_generator_profile"]
        assert cert["exact_weight5_generators"] == cert["exact_weight6_generators"] == 0
        assert cert["exact_weight7_generators"] == cert["global_generator_count"] == 0
        assert cert["all_272_generators_exact"] is False
        assert cert["actual_complete_polar_module_certified"] is False
        assert cert["original_R787_reserved_target_recomputed"] is False
        assert cert["new_weight7_or_Laurent_tail_computed"] is False
        assert cert["normal_polynomial_ideal_matrices_computed"] is False
        assert cert["radical_or_Jacobian_eta_or_height_computed"] is False
        assert cert["configuration"]["generator_profile_weights_5_6_7"] == [28, 244, 0]
        inventory = source.stage(cert["stage_manifest"])
        assert IO.plain(cert["stage_manifest"]) == request["expected_stage_manifest"]
        stages = {row["file"]: IO.plain(row) for row in inventory["files"]}
        assert len(stages) == len(inventory["files"])
        for name, row in stages.items():
            assert row == IO.plain(source.files[name])
        index = source.stage(cert["generator_index"])
        assert IO.plain(cert["generator_index"]) == request["expected_generator_index"]
        assert index["exact_generators"] == [] and index["complete_polar_module_certified"] is False
        assert index["original_R787_reserved_generator_present"] is False
        assert IO.plain(source.files["R824-retained-producer-inputs.tar.gz"]) == request["expected_original_input_bundle"]
        def stage(entry):
            if isinstance(entry, str):
                entry = stages[entry]
            assert IO.plain(entry) == stages[entry["file"]]
            return source.stage(entry)
        branch_name = "R824-power5-prime-1000000753-branch-00.json.gz"
        branch = stage(branch_name)
        chart5 = stage(branch["chart"])
        assert branch["ordinary_power"] == 5 and branch["prime"] == 1000000753
        assert branch["branch"] == 0 and branch["roots_B_s"] == [3197390, 99932770]
        assert branch["actual_Schur_rank"] == 1186 and branch["selected_minor_det_mod_prime"] == 296007862
        assert branch["original_reserved_column_retained_without_new_lift"] is True
        assert branch["full_original_modular_relations_verified_for_all_new_free_targets"] is True
        assert len(branch["kernel_free_columns"]) == 28 and 1186 in branch["kernel_free_columns"]
        assert len(branch["kernel_A_mod_prime"]) == 1234
        assert all(len(row) == 28 for row in branch["kernel_A_mod_prime"])
        assert len(branch["kernel_C_mod_prime"]) == 1214
        assert all(len(row) == 28 for row in branch["kernel_C_mod_prime"])
        assert chart5["actual_rank"] == 1186 and chart5["kernel_dimension"] == 28
        assert chart5["chart_choice_from_original_R787"] is True
        assert branch["original_branch_inverse_reused_from"]["sha256"] == \
            "c5b75f48b5c5d1cf2d98390e814a245306fa63f10ae43dae194dbfd560d895d7"
        assert branch["rational_block"]["sha256"] == \
            "fb8a82957474e657fc476aa2baa0d8ce9f4c8b6cc86c2b55a79e75913d610b3b"
        profile_name = "R824-power6-selected-generator-profile.json.gz"
        profile = stage(profile_name)
        chart6, supplement = stage(profile["weight6_chart"]), stage(profile["supplement_chart"])
        if profile["weight5_chart"]["file"] != branch["chart"]["file"]:
            stage(profile["weight5_chart"])
        assert profile["weight5_kernel_dimension"] == 28 and profile["weight6_kernel_dimension"] == 300
        assert profile["actual_lower_span_rank_in_each_branch"] == 56
        assert profile["exact_weight6_generators_claimed"] is False
        assert len(profile["selected_weight6_free_columns"]) == len(set(profile["selected_weight6_free_columns"])) == 244
        assert len(profile["selected_weight6_free_positions"]) == 244
        assert chart6["actual_rank"] == 1186 and chart6["kernel_dimension"] == 300
        assert supplement["prime"] == profile["prime"] and supplement["actual_lower_span_rank"] == 56
        assert len(supplement["selected_lower_span_rows"]) == 56
        span_specs = profile["branch_lower_span_stages"]
        assert len(span_specs) == 14
        source.prefetch(row["file"] for row in span_specs)
        spans = []
        for number, row in enumerate(span_specs):
            value = stage(row)
            assert value["prime"] == profile["prime"] and value["branch"] == number
            assert value["actual_lower_span_rank"] == 56
            assert value["actual_selected_minor_determinant_mod_prime"] != 0
            assert value["common_row_indices"] == supplement["selected_lower_span_rows"]
            assert value["all_1640_original_product_coordinates_verified"] is True
            assert value["all_B6_coordinates_in_saved_sixfold_kernel_verified"] is True
            assert value["new_exact_weight5_prefix_or_weight6_basis_computed"] is False
            assert len(value["lower_span_in_weight6_free_coordinates"]) == 300
            assert all(len(vector) == 56 for vector in value["lower_span_in_weight6_free_coordinates"])
            spans.append({"branch": number, "actual_minor_determinant_mod_prime":
                          value["actual_selected_minor_determinant_mod_prime"], "source": IO.plain(row),
                          "weight5_kernel": value["weight5_kernel_stage"],
                          "weight6_kernel": value["weight6_kernel_stage"]})
        operator_specs = [stages["R824-common-clear-operator-N"+str(count)+".json.gz"] for count in (129, 142)]
        source_closure = source.closure_receipt()
        summary = {
            "result": RESULT, "complete": True, "new_mathematical_arithmetic_executed": False,
            "original_producer": item,
            "original_full_manifest": IO.file_spec(path), "original_reference": reference_spec,
            "original_certificate": IO.file_spec(selected/CERT),
            "original_stage_manifest": IO.plain(cert["stage_manifest"]),
            "original_generator_index": IO.plain(cert["generator_index"]),
            "original_input_bundle_identity_only": IO.plain(source.files["R824-retained-producer-inputs.tar.gz"]),
            "original_frozen_verify_reported_by_success_job": {
                "workflow_run_id": "43729293174", "job_id": "132857969568",
                "complete_output_manifest_files": 359, "complete_original_input_bundle_members": 7741,
                "whole_manifest_and_bundle_reverified_in_this_subset_audit": False},
            "completed_requested_scopes": cert["completed_requested_scopes"],
            "actual_exact_weight5_generators": cert["exact_weight5_generators"],
            "actual_exact_weight6_generators": cert["exact_weight6_generators"],
            "actual_complete_polar_module_certified": cert["actual_complete_polar_module_certified"],
            "actual_common_operator_specs_not_downloaded_again": operator_specs,
            "original_prime753_branch0": {
                "source": IO.plain(source.files[branch_name]), "chart": IO.plain(branch["chart"]),
                "roots_B_s": branch["roots_B_s"], "actual_Schur_rank": 1186,
                "actual_nonzero_minor": branch["selected_minor_det_mod_prime"],
                "kernel_dimension": 28, "reserved_free_column": 1186,
                "reserved_original_column_copied_without_lift": True,
                "field": cert["configuration"]["field"],
                "original_rational_block": branch["rational_block"],
                "original_branch_inverse": branch["original_branch_inverse_reused_from"]},
            "actual_modular_generator_profile": {
                "source": IO.plain(source.files[profile_name]), "prime": profile["prime"],
                "weight5_kernel_dimension": 28, "weight6_kernel_dimension": 300,
                "lower_span_rank_in_each_of_14_branches": 56, "selected_weight6_supplement_count": 244,
                "weight5_chart": profile["weight5_chart"], "weight6_chart": profile["weight6_chart"],
                "supplement_chart": profile["supplement_chart"], "branch_minor_sources": spans},
            "core_seconds": cert["seconds"],
            "selected_original_files": source_closure["files"],
            "selected_original_member_count": len(source_closure["files"]),
            "selected_original_bytes": sum(row["bytes"] for row in source_closure["files"]),
            "archive_subset_transfer": archive.receipt(),
            "reproducible_raw_outputs_published_to_git_or_release": False,
            "read_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        }
        IO.save(out/"R824-success-profile-IO-review-summary.json", summary)
        IO.save(out/"R824-success-profile-IO-audit-input.json", {
            "result": RESULT, "request": request,
            "audit_script_sha256": sha(__file__), "io_helper_sha256": IO_SHA,
            "actual_audit_source_commit": os.environ["GITHUB_SHA"],
            "actual_audit_workflow_run_id": os.environ["GITHUB_RUN_ID"]})
        printable = dict(summary)
        printable["original_prime753_branch0"] = dict(summary["original_prime753_branch0"])
        field = printable["original_prime753_branch0"].pop("field")
        printable["original_prime753_branch0"]["original_field_description_sha256"] = IO.fingerprint(field)
        print("R824_PROFILE_IO_REVIEW_SUMMARY="+json.dumps(printable, sort_keys=True, separators=(",", ":")), flush=True)
        return 0
    finally:
        archive.close()


if __name__ == "__main__":
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.output))
