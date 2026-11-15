#!/usr/bin/env python3
"""Read selected original R809 success metadata over identity-bound ZIP64 HTTP Range."""
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
REQUEST = TOPIC/"notes/R809-public-success-source-io-audit-request.json"
IO_NAME = "R824_public_original_global_polar_generators.py"
IO_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
RESULT = "R809-existing-normal-coordinate-source-IO-review"
ORIGINAL = "R809-original-S5-normal-coordinates"
CERT = "p41-original-S5-normal-coordinate-certificate.json"
REFERENCE = "full-outputs-manifest-reference.json"
FIELD_BASIS = "b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b"
EPS = [0]+[1]*144+[2]*127
TARGETS = ["C"+str(i) for i in range(6)]


def sha(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            value.update(block)
    return value.hexdigest()


assert sha(S/IO_NAME) == IO_SHA
loader = importlib.util.spec_from_file_location("R809_source_frozen_IO", S/IO_NAME)
IO = importlib.util.module_from_spec(loader)
loader.loader.exec_module(IO)


def bootstrap_reference(archive, selected):
    members = archive.by_name.get(REFERENCE, [])
    assert len(members) == 1 and 0 < members[0].file_size < 1024*1024
    with archive.zip.open(members[0], "r") as stream:
        raw = stream.read(1024*1024+1)
    assert len(raw) == members[0].file_size
    data = json.loads(raw)
    assert data["result"] == ORIGINAL and data["manifest_file"] == "full-outputs-manifest.json"
    assert IO.H64.fullmatch(data["manifest_sha256"])
    assert data["manifest_bytes"] > 0 and data["file_count"] > 0
    assert data["full_outputs_artifact"] == archive.item["artifact_name"]
    path = selected/REFERENCE
    path.write_bytes(raw)
    return data, IO.file_spec(path)


def run(out):
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    request = IO.read(REQUEST)
    item = dict(request["original_producer"])
    item["files"] = dict(item.get("files", {}))
    assert request["io_helper_sha256"] == sha(S/IO_NAME) == IO_SHA
    assert request["audit_script_sha256"] == sha(__file__)
    assert sha(REPO/"README.md") == request["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md") == request["readme_sha256"]["topic"]
    assert item["result"] == ORIGINAL and item["certificate_name"] == CERT
    assert item["core_sha256"] == "dedb5d6149a3c3ae86ad09e51f30c1424951a09010bf48afd948d2628e1ec21d"
    out.mkdir(parents=True, exist_ok=True)
    selected = out/"selected-original-R809"
    selected.mkdir(parents=True, exist_ok=True)
    archive = IO.Archive(item, out.parent/"range-transfer", whole=False)
    try:
        reference, reference_spec = bootstrap_reference(archive, selected)
        if item.get("manifest_sha256") is not None:
            assert item["manifest_sha256"] == reference["manifest_sha256"]
        item["manifest_sha256"] = reference["manifest_sha256"]
        manifest_path = archive.extract_bound(
            "full-outputs-manifest.json", item["manifest_sha256"],
            selected/"full-outputs-manifest.json", reference["manifest_bytes"])
        manifest = IO.read(manifest_path)
        assert manifest["result"] == ORIGINAL
        files = {row["file"]: row for row in manifest["files"]}
        assert len(files) == len(manifest["files"]) == reference["file_count"]
        for row in files.values():
            IO.check_spec(row)
        if CERT in item["files"]:
            assert item["files"][CERT] == files[CERT]["sha256"]
        item["files"][CERT] = files[CERT]["sha256"]
        source = IO.Producer("R809", item, selected, archive)
        cert = source.certificate
        assert cert["p"] == 41 and cert["completed_scope"] == "requested_actual_normal_coordinate_targets"
        assert cert["requested_target_groups"] == cert["completed_target_groups"] == TARGETS
        assert cert["completed_rational_RHS_columns"] == 84
        assert cert["S5_dimension"] == 1234 and cert["qY_count"] == 69
        assert cert["full_real_coordinates"] == 1380
        assert cert["normal_basis_rank"] == 272 and cert["normal_basis_degrees"] == EPS
        assert cert["coefficient_field_basis"] == FIELD_BASIS
        assert cert["basis_integer_scale"] == str(82**10) and cert["actual_sigma_integer_n"] == 1
        assert cert["actual_prime"] == 1000000007 and cert["actual_short_minor_determinant"] == 29693114
        for name in ("all_requested_targets_verified_in_all1380_rows",
                     "all_completed_C_targets_highest_S5_coefficients_zero",
                     "original_scalar_and_field_normalizations_preserved",
                     "basis_identity_excludes_requested_scope_budget_and_future_R787"):
            assert cert[name] is True
        for name in ("actual_original_y_normal_vectors_computed", "all_112_rational_targets_computed",
                     "old_mathematical_producer_stages_recomputed",
                     "actual_polar_ideal_or_eta_or_height_computed", "characteristic_zero_Krylov_inverse_computed"):
            assert cert[name] is False
        inventory = source.stage(cert["stage_manifest"])
        stages = {row["file"]: IO.plain(row) for row in inventory["files"]}
        assert len(stages) == len(inventory["files"])
        for name, row in stages.items():
            assert row == IO.plain(files[name])
        def stage(entry, target=None):
            if isinstance(entry, str):
                entry = stages[entry]
            assert IO.plain(entry) == stages[entry["file"]]
            value = source.stage(entry)
            if target is not None:
                assert value["target_configuration"] == cert["completed_target_configurations"][target]
                assert value["target_configuration_sha256"] == IO.fingerprint(value["target_configuration"])
            return value
        basis = stage(cert["S5_basis_index"])
        assert cert["S5_basis_index"]["file"] == "R809-S5-basis-index.json.gz"
        assert basis["dimension"] == 1234 and basis["qY_count"] == 69
        assert basis["real_coordinate_count"] == 20 and basis["full_coordinate_rows"] == 1380
        assert basis["integer_scale"] == str(82**10)
        assert basis["normal_affine_basis_rank"] == 272 and basis["normal_basis_degrees"] == EPS
        assert basis["all_original_term_phases_and_scales_verified"] is True
        mapping = [(a, power) for a, eps in enumerate(EPS) for power in range(6-eps)]
        assert len(basis["basis_rows"]) == len(mapping) == 1234
        for i, (row, pair) in enumerate(zip(basis["basis_rows"], mapping)):
            a, power = pair
            assert row["index"] == i and row["normal_basis_index"] == a and row["z_degree"] == power
            assert row["normal_basis_degree"] == EPS[a]
            assert IO.plain(row["source"]) == stages[row["source"]["file"]]
        minor = stage(cert["minor_stage"])
        assert cert["minor_stage"]["file"] == "R809-accepted-S5-short-minor.json.gz"
        rank = stage(minor["actual_rank_stage"])
        assert minor["S5_basis_index"] == cert["S5_basis_index"]
        assert minor["actual_rank"] == rank["actual_rank"] == 1234
        assert minor["full_coordinate_rows"] == 1380 and minor["column_indices"] == list(range(1234))
        assert minor["row_indices"] == rank["row_indices"]
        assert len(minor["row_indices"]) == 1234 and minor["row_indices"] == sorted(set(minor["row_indices"]))
        assert all(0 <= i < 1380 for i in minor["row_indices"])
        assert minor["prime"] == rank["prime"] == cert["actual_prime"]
        assert minor["actual_determinant_mod_prime"] == rank["actual_determinant_mod_prime"] == cert["actual_short_minor_determinant"]
        assert minor["minor_is_from_actual_69_term_matrix"] is True
        assert rank["S5_basis_index"] == cert["S5_basis_index"]
        assert IO.plain(cert["modular_inverse_stage"]) == stages[cert["modular_inverse_stage"]["file"]]
        assert set(cert["normal_vectors"]) == set(TARGETS)
        vectors = {}
        for target in TARGETS:
            value = stage(cert["normal_vectors"][target], target)
            assert value["target"] == target and value["normal_basis_rank"] == 272
            assert value["normal_basis_degrees"] == EPS and value["regular_degree_bound"] == 4
            assert value["coefficient_field_basis"] == FIELD_BASIS
            assert value["S5_basis_index"] == cert["S5_basis_index"]
            assert len(value["coordinate_groups"]) == 2
            for spec in value["coordinate_groups"]:
                assert IO.plain(spec) == stages[spec["file"]]
            for key in ("all14_original_field_columns_retained", "normal_vector_actually_nonzero",
                        "all1380_original_coordinates_verified", "weighted_polynomial_support_verified",
                        "literal_tau_factor_highest_S5_coefficients_zero",
                        "original_field_and_scalar_normalizations_preserved"):
                assert value[key] is True
            assert value["normal_ring_multiplication_or_field_division_computed"] is False
            assert value["actual_polar_ideal_or_eta_or_height_computed"] is False
            vectors[target] = {
                "normal_vector_index": IO.plain(cert["normal_vectors"][target]),
                "normal_function": value["normal_function"], "regular_degree_bound": 4,
                "coefficient_field_basis": FIELD_BASIS,
                "coordinate_groups_not_downloaded_again": [IO.plain(row) for row in value["coordinate_groups"]],
                "coefficient_reconstruction": value["coefficient_reconstruction"],
                "all1380_original_coordinates_verified_in_original_success_run": True,
                "highest_S5_coefficients_zero_verified_in_original_success_run": True}
        interface = stage(cert["normal_function_interface"])
        assert interface["normal_vectors"] == cert["normal_vectors"]
        assert interface["actual_normal_ring_multipliers_or_field_quotients_computed"] is False
        assert interface["actual_derivation_polar_ideal_eta_or_height_computed"] is False
        input_bundles = [IO.plain(row) for row in files.values()
                         if "retained-producer-inputs" in row["file"] and row["file"].endswith(".tar.gz")]
        assert len(input_bundles) == 1
        closure = source.closure_receipt()
        consumer = dict(item)
        consumer["files"] = {name: files[name]["sha256"] for name in
            (CERT, cert["stage_manifest"]["file"], cert["S5_basis_index"]["file"],
             cert["minor_stage"]["file"], minor["actual_rank_stage"]["file"])}
        consumer["expected_conclusion"] = "success"
        summary = {
            "result": RESULT, "complete": True, "new_mathematical_arithmetic_executed": False,
            "original_producer": item, "R827_ready_original_producer_spec": consumer,
            "original_full_manifest": IO.file_spec(manifest_path), "original_reference": reference_spec,
            "original_certificate": IO.file_spec(selected/CERT),
            "original_stage_manifest": IO.plain(cert["stage_manifest"]),
            "original_basis_index": IO.plain(cert["S5_basis_index"]),
            "original_minor_index": IO.plain(cert["minor_stage"]),
            "original_rank_stage": IO.plain(minor["actual_rank_stage"]),
            "original_modular_inverse_identity_only": IO.plain(cert["modular_inverse_stage"]),
            "original_input_bundle_identity_only": input_bundles[0],
            "original_basis_configuration": cert["configuration"],
            "actual_completed_target_groups": TARGETS, "actual_rational_RHS_columns": 84,
            "actual_short_minor_prime": cert["actual_prime"],
            "actual_short_minor_determinant": cert["actual_short_minor_determinant"],
            "actual_S5_dimension": 1234, "actual_full_coordinate_rows": 1380,
            "original_S5_row_count": len(basis["basis_rows"]),
            "original_S5_rows_not_redownloaded_or_recomputed": True,
            "actual_C_normal_vectors": vectors,
            "actual_A_B_normal_vectors_computed": False,
            "actual_polar_ideal_eta_or_height_computed": False,
            "core_seconds": cert["seconds"],
            "original_frozen_verify_success_already_reported": {
                "workflow_run_id": "43712427063", "job_id": "132806699613",
                "all_output_bytes_original_input_bundle_and_full1380_coordinates_reviewed_in_original_success_job": True,
                "whole_ZIP_manifest_bundle_or_big_coordinate_groups_reverified_in_this_subset_audit": False},
            "selected_original_files": closure["files"],
            "selected_original_member_count": len(closure["files"]),
            "selected_original_bytes": sum(row["bytes"] for row in closure["files"]),
            "archive_subset_transfer": archive.receipt(),
            "reproducible_raw_outputs_published_to_git_or_release": False,
            "read_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        }
        IO.save(out/"R809-success-source-IO-review-summary.json", summary)
        IO.save(out/"R809-success-source-IO-audit-input.json", {
            "result": RESULT, "request": request,
            "audit_script_sha256": sha(__file__), "io_helper_sha256": IO_SHA,
            "actual_audit_source_commit": os.environ["GITHUB_SHA"],
            "actual_audit_workflow_run_id": os.environ["GITHUB_RUN_ID"]})
        printable = dict(summary)
        tag = printable.pop("original_basis_configuration")
        printable["original_basis_configuration_sha256"] = IO.fingerprint(tag)
        print("R809_SOURCE_IO_REVIEW_SUMMARY="+json.dumps(
            printable, sort_keys=True, separators=(",", ":")), flush=True)
        return 0
    finally:
        archive.close()


if __name__ == "__main__":
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.output))
