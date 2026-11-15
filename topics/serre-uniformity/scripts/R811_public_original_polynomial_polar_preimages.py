#!/usr/bin/env python3
"""R811 complete polar-preimage IO runner; verification imports no mathematical code."""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import signal
import subprocess
import sys
import tarfile
import tempfile

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R811-public-original-polynomial-polar-preimages-request.json"
RESULT = "R811-original-polynomial-polar-preimages"
FINAL = "p41-original-polynomial-polar-preimages-certificate.json"
SCOPE = "complete_base_y_two_chart_polar_preimages"
REGULAR_RESULT = "R811-original-regular-multipliers-and-polar-preimages"
REGULAR_CORE = "849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3"
IO_HELPER = "R811_public_original_regular_multipliers.py"
IO_SHA = "2a1d1c286ca26e37b784bdc94d587e056e69732f9a60bb26840ee8f07f340e8a"
FIELD_SHA = "f196cb805d1ca91e8995866032a0a3ec3f96aac06e03b67a7c1f196fff759251"
PROOF_SHA = "263d8a15085c3fc053dac1df546ad0c3efb565d67ce312c78ec6e5ddb4dccf78"
INPUT_BUNDLE = "R811-polar-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
EPS = [0]+[1]*144+[2]*127
FREE, LDEG, DEGREE = 272, 14, 5
FIELD_BASIS = "b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b"
INT = re.compile(r"-?(0|[1-9][0-9]*)")


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


# Only the previously frozen standard-library IO runner is imported.
# The field and polynomial helpers are passed exclusively to the Actions subprocess.
assert sha(S/IO_HELPER) == IO_SHA
module_spec = importlib.util.spec_from_file_location("R811_frozen_regular_IO_only", S/IO_HELPER)
IO = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(IO)
read, save, file_spec, plain = IO.read, IO.save, IO.file_spec, IO.plain
fingerprint, identity, same_identity = IO.fingerprint, IO.identity, IO.same_identity
Archive, Producer, check_spec = IO.Archive, IO.Producer, IO.check_spec


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New original polynomial arithmetic belongs to public repository Actions.")


def topic_path(relative):
    path = (TOPIC/relative).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def source_integer(value):
    assert isinstance(value, str) and INT.fullmatch(value)
    return int(value)


def field_coefficient(value):
    """Representation/schema only, without field operations or normalization."""
    assert isinstance(value, list) and len(value) == 2
    for part in value:
        assert set(part) == {"numerator", "denominator"}
        assert 0 <= len(part["numerator"]) <= 7
        assert source_integer(part["denominator"]) > 0
        for integer in part["numerator"]:
            source_integer(integer)
        if part["numerator"]:
            assert part["numerator"][-1] != "0"


def polynomial(value):
    assert isinstance(value, list)
    for coefficient in value:
        field_coefficient(coefficient)
    if value:
        assert any(part["numerator"] for part in value[-1])


def laurent(value):
    assert set(value) == {"power", "polynomial"}
    assert isinstance(value["power"], int)
    polynomial(value["polynomial"])


def select_inputs(producer):
    certificate = producer.certificate
    assert producer.item["result"] == REGULAR_RESULT
    assert producer.item["core_sha256"] == REGULAR_CORE
    assert certificate["completed_scope"] == "base_regular_multipliers"
    assert certificate["requested_targets"] == ["A", "B"]
    assert certificate["normal_affine_basis_rank"] == FREE and certificate["normal_basis_degrees"] == EPS
    assert certificate["coefficient_field_basis"] == FIELD_BASIS
    assert producer.tag["R811_proof_sha256"] == PROOF_SHA
    for key in ("regular_multipliers_computed", "two_chart_regular_pairs_computed",
                "all_weighted_degree_bounds_verified", "all_original_first_columns_verified_coefficientwise",
                "all_complete_polynomial_commutator_identities_verified",
                "all_original_scalar_and_field_normalizations_preserved", "normal_integral_basis_preserved"):
        assert certificate[key] is True
    assert certificate["base_polar_preimages_computed"] is False
    assert certificate["commutator_maximum_degree"] == 8
    assert certificate["exact_commutator_points"] == list(range(9))
    pair = certificate["original_y_operator_pair"]
    assert pair["numerator"] == "A" and pair["denominator"] == "B"
    assert pair["common_t_power_cancels_exactly"] == DEGREE and pair["source_B_actually_nonzero"] is True
    targets = certificate["target_multipliers"]
    assert set(targets) == {"A", "B"}
    models, target_hashes, component_specs = {}, {}, {}
    row_ranges = [(first, min(first+16, FREE)) for first in range(0, FREE, 16)]
    counts = {}
    for target in ("A", "B"):
        index = producer.indexed(targets[target])
        assert index["target"] == target and index["regular_degree_bound"] == DEGREE
        assert index["normal_affine_basis_rank"] == FREE and index["normal_basis_degrees"] == EPS
        assert index["coefficient_field_basis"] == FIELD_BASIS
        for key in ("all14_components_verified_in_original_field_basis",
                    "all_complete_polynomial_commutator_identities_verified",
                    "all_first_columns_verified_coefficientwise",
                    "two_regular_charts_use_original_homogeneous_degree", "original_target_actually_nonzero"):
            assert index[key] is True
        tag = index["target_configuration"]
        assert index["target_configuration_sha256"] == fingerprint(tag)
        assert tag["basis_configuration_sha256"] == fingerprint(producer.tag)
        assert tag["target"] == target and tag["regular_degree_bound"] == DEGREE
        assert tag["coefficient_field_basis"] == FIELD_BASIS
        assert tag["source_R809_normal_vector"] == certificate["source_R809_normal_vectors"][target]
        original = tag["source_R809_target_configuration"]
        assert tag["source_R809_target_configuration_sha256"] == fingerprint(original)
        assert tag["original_b_model"] == original["original_b_model"]
        model = tag["original_b_model"]
        assert set(model) == {"numerator", "denominator"} and len(model["numerator"]) == 8
        assert source_integer(model["denominator"]) > 0
        assert model["numerator"][-1] == model["denominator"]
        models[target], target_hashes[target] = model, fingerprint(tag)
        entries = index["field_component_multipliers"]
        assert len(entries) == LDEG
        component_specs[target] = entries
        nonzero = 0
        for component, entry in enumerate(entries):
            data = producer.indexed(entry)
            assert data["target"] == target and data["field_component"] == component
            assert data["target_configuration"] == tag and data["target_configuration_sha256"] == fingerprint(tag)
            assert data["coefficient_field_basis"] == FIELD_BASIS and data["regular_degree_bound"] == DEGREE
            assert data["weighted_degree_bound_verified"] is True
            assert data["original_first_column_verified_coefficientwise"] is True
            assert data["complete_polynomial_commutator_identity_verified"] is True
            if data["zero_component_proved_from_exact_original_vector"]:
                assert data["matrix_row_blocks_tau"] == data["matrix_row_blocks_sigma"] == []
                assert data["zero_identity_follows_exactly_without_modular_zero_assumption"] is True
                continue
            nonzero += 1
            assert data["primitive_cyclic_uniqueness_identifies_true_regular_multiplier"] is True
            assert data["sigma_regular_transition_preserves_original_section"] is True
            assert data["exact_commutator_points"] == list(range(9))
            assert len(data["matrix_row_blocks_tau"]) == len(data["matrix_row_blocks_sigma"]) == 17
            for block_index, (first, stop) in enumerate(row_ranges):
                count = sum(DEGREE+EPS[column]-EPS[row]+1
                            for row in range(first, stop) for column in range(FREE))
                for chart in ("tau", "sigma"):
                    block = producer.indexed(data["matrix_row_blocks_"+chart][block_index])
                    assert block["target"] == target and block["field_component"] == component
                    assert block["target_configuration"] == tag
                    assert block["target_configuration_sha256"] == fingerprint(tag)
                    assert (block["row_first"], block["row_stop"]) == (first, stop)
                    assert block["regular_degree_bound"] == DEGREE
                    assert source_integer(block["common_positive_denominator"]) > 0
                    assert len(block["coefficient_numerators"]) == count
                    if chart == "sigma":
                        assert block["every_transition_exponent_nonnegative"] is True
                        assert block["common_homogeneous_factor_in_pair"] == "t^5"
                        assert block["source_tau_matrix_row_block"] == data["matrix_row_blocks_tau"][block_index]
        counts[target] = nonzero
    assert models["A"] == models["B"]
    return {
        "original_R811_producer": identity(producer.item), "original_R811_certificate": plain(
            producer.files[producer.item["certificate_name"]]),
        "source_target_multipliers": targets, "source_field_component_indexes": component_specs,
        "source_original_b_model": models["A"],
        "original_b_model_source_target_configuration_hashes": target_hashes,
        "actual_nonzero_rational_components": counts,
        "original_R805_free_basis": producer.tag["original_R805_free_basis"],
        "actual_sigma_integer_n": certificate["actual_sigma_integer_n"],
        "only_completed_original_A_B_regular_matrices_selected": True,
        "old_Fourier_or_function_or_regular_multiplier_inputs_for_recomputation_selected": False}


def expected_configuration(item, producer, selection):
    return {
        "result": RESULT, "source_sha256": item["core_sha256"], "python_flint": "0.9.0",
        "R811_proof_sha256": item["R811_proof_sha256"],
        "polynomial_method_sha256": item["polynomial_method_sha256"],
        "module_helper_sha256": item["module_helper_sha256"], "field_core_sha256": item["field_core_sha256"],
        "R811_regular_producer": identity(producer.item),
        "R811_regular_certificate": selection["original_R811_certificate"],
        "source_target_multipliers": selection["source_target_multipliers"],
        "source_original_b_model": selection["source_original_b_model"],
        "original_b_model_source_target_configuration_hashes":
            selection["original_b_model_source_target_configuration_hashes"],
        "original_R805_free_basis": selection["original_R805_free_basis"],
        "actual_sigma_integer_n": selection["actual_sigma_integer_n"],
        "normal_affine_basis_rank": FREE, "normal_basis_degrees": EPS,
        "source_coefficient_field_basis": FIELD_BASIS,
        "arithmetic_coefficient_field": "original L=Q(b,zeta); zeta^2+zeta+1=0",
        "field_basis_conversion": "a+s*c -> (a+c)+2*c*zeta; s=1+2*zeta",
        "polynomial_product_b_stride": 13, "matrix_tile_size": 16,
        "original_regular_pair_degree": DEGREE,
        "original_function_pair": "(A/tau^5)/(B/tau^5)=(A/sigma^5)/(B/sigma^5)",
        "matrix_convention": "output normal row, input normal column",
        "new_embedding_or_model_scalar_chosen": False,
        "only_current_large_work_vectors_and_necessary_final_ideal_basis_retained": True,
        "expected_degree_not_used_to_fill_any_kernel_rank_or_ideal_degree": True}


def bundle_members(bundle, root=None):
    seen = set()
    with tarfile.open(bundle, "r:gz") as archive:
        for member in archive:
            path = PurePosixPath(member.name)
            assert member.isfile() and len(path.parts) == 2 and path.parts[0] == "R811"
            assert not path.is_absolute() and ".." not in path.parts and member.name not in seen
            seen.add(member.name)
            destination = None if root is None else Path(root)/path.parts[0]/path.parts[1]
            temporary = None if destination is None else destination.with_name(destination.name+".transfer")
            if temporary is not None:
                temporary.parent.mkdir(parents=True, exist_ok=True)
            digest, total = hashlib.sha256(), 0
            source = archive.extractfile(member)
            target = None if temporary is None else temporary.open("wb")
            try:
                for block in iter(lambda: source.read(1024*1024), b""):
                    digest.update(block)
                    total += len(block)
                    if target is not None:
                        target.write(block)
            finally:
                source.close()
                if target is not None:
                    target.close()
            assert total == member.size
            if temporary is not None:
                temporary.replace(destination)
            yield member.name, {"file": path.parts[1], "bytes": total, "sha256": digest.hexdigest()}


def verify_bundle(bundle, producer):
    expected = {"R811/"+name: file_spec(path) for name, path in producer.selected.items()}
    actual = dict(bundle_members(bundle))
    assert actual == expected
    return len(actual)


def prepare_inputs(item, out):
    root = out.parent/"retained"
    original = item["retained_artifacts"]["R811"]
    present = (root/"R811"/"full-outputs-manifest.json").exists()
    archive, transport = None, None
    if not present:
        carrier = original.get("input_carrier")
        if carrier is not None:
            assert carrier["role"] == "unchanged_original_selected_files"
            assert carrier["original_result"] == original["result"]
            assert str(carrier["original_run_id"]) == str(original["run_id"])
            assert carrier["original_source_commit"] == original["source_commit"]
        archive = Archive(carrier or original, out.parent/"download-original-R811")
        transport = archive.receipt
    producer = Producer("R811", original, root/"R811", archive)
    selection = select_inputs(producer)
    assert {path.name for path in producer.directory.iterdir() if path.is_file()} == set(producer.selected)
    bundle = out/INPUT_BUNDLE
    if not bundle.exists():
        temporary = bundle.with_name(bundle.name+".tmp")
        with tarfile.open(temporary, "w:gz") as target:
            for name in sorted(producer.selected):
                target.add(producer.selected[name], arcname="R811/"+name, recursive=False)
        temporary.replace(bundle)
    count = verify_bundle(bundle, producer)
    save(out/"retained-inputs-receipt.json", {
        "result": RESULT, "producer_identities": {"R811": identity(original)},
        "selection": selection, "selected_files": {"R811": [
            file_spec(path) for _, path in sorted(producer.selected.items())]},
        "input_bundle": file_spec(bundle), "actual_selected_file_count": count,
        "all_selected_bundle_members_individually_size_and_sha256_verified": True,
        "original_transport": transport, "restored_original_input_bundle_reused": present,
        "old_arithmetic_recomputed": False})
    if archive is not None:
        archive.zip.close()
        archive.path.unlink()
    return root, producer, selection


def restore_resume(item, out):
    previous = item.get("resume")
    if previous is None:
        return
    archive = Archive(previous, out.parent/"download-continuation", expected_conclusion="failure")
    path = archive.extract_bound("full-outputs-manifest.json", previous["manifest_sha256"],
                                 out.parent/"previous-full-outputs-manifest.json")
    manifest = read(path)
    assert manifest["result"] == RESULT
    entries = archive.verify_all_manifest_members(manifest)

    def bound(name):
        entry = entries[name]
        return archive.extract_bound(name, entry["sha256"], out.parent/"previous-small"/name, entry["bytes"])

    initial, run = read(bound("public-actions-input.json")), read(bound("run-receipt.json"))
    assert initial["result"] == run["result"] == RESULT
    assert initial["source_commit"] == run["source_commit"] == previous["source_commit"]
    assert str(run["workflow_run_id"]) == str(previous["run_id"])
    old = initial["job"]
    for key in ("result", "p", "core", "core_sha256", "proof", "R811_proof_sha256", "method",
                "polynomial_method_sha256", "module_helper", "module_helper_sha256", "field_core",
                "field_core_sha256", "io_helper", "io_helper_sha256", "requested_stage",
                "matrix_tile_size", "transcript_archive_operations_per_chunk",
                "expected_original_polar_degree_for_final_comparison_only"):
        assert old[key] == item[key], ("Changed same-core polynomial continuation", key)
    same_identity(old["retained_artifacts"]["R811"], item["retained_artifacts"]["R811"])
    for name in set(old["retained_artifacts"]["R811"]["files"]) & set(item["retained_artifacts"]["R811"]["files"]):
        assert old["retained_artifacts"]["R811"]["files"][name] == item["retained_artifacts"]["R811"]["files"][name]
    bundle = bound(INPUT_BUNDLE)
    root = out.parent/"retained"
    assert dict(bundle_members(bundle, root))
    producer = Producer("R811", item["retained_artifacts"]["R811"], root/"R811")
    selection = select_inputs(producer)
    count = verify_bundle(bundle, producer)
    shutil.copyfile(bundle, out/INPUT_BUNDLE)
    tag = expected_configuration(item, producer, selection)
    stages, partial, archives = 0, 0, 0
    for name, entry in entries.items():
        is_stage = name.startswith("R811-polar-") and name.endswith(".json.gz")
        is_archive = name.startswith("R811-polar-") and "-transcript-" in name and name.endswith(".tar.gz")
        if not (name == FINAL or is_stage or is_archive):
            continue
        destination = archive.extract_bound(name, entry["sha256"], out/name, entry["bytes"])
        if is_archive:
            archives += 1
            continue
        value = read(destination)
        assert value["configuration"] == tag
        current = name.endswith("-current.json.gz")
        assert value["complete"] is (not current)
        partial += int(current)
        stages += 1
    save(out/"resume-receipt.json", {
        "result": RESULT, "previous_actual_artifact": previous, "actual_archive_review": archive.receipt,
        "all_original_manifest_members_streamed_and_sha256_verified": True,
        "actual_previous_manifest_file_count": len(entries),
        "complete_and_partial_polynomial_stage_files_restored": stages,
        "partial_atomic_checkpoints_restored": partial,
        "unmodified_transcript_archives_restored": archives,
        "selected_original_bundle_members_verified": count, "input_bundle": file_spec(out/INPUT_BUNDLE),
        "same_mathematical_core_and_sources_preserved": True,
        "all_committed_and_pending_operation_tiles_preserved": True,
        "old_completed_arithmetic_recomputed": False})
    archive.zip.close()
    archive.path.unlink()
    print(json.dumps({"R811_POLAR_RESTORE_REVIEW": {
        "previous_run": previous["run_id"], "archive_sha256": previous["archive_sha256"],
        "all_manifest_files_verified": len(entries), "restored_stage_count": stages,
        "restored_partial_count": partial, "restored_transcript_archives": archives,
        "selected_bundle_files_verified": count}}), flush=True)


def output_manifest(out):
    for path in out.iterdir():
        if path.is_file() and path.name.endswith((".tmp", ".download", ".partial")):
            path.unlink()
    artifact = "serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    entries = [dict(file_spec(path), artifact=artifact, included_in_git=False)
               for path in sorted(out.iterdir()) if path.is_file()
               and path.name not in ("full-outputs-manifest.json", REFERENCE)]
    manifest = out/"full-outputs-manifest.json"
    save(manifest, {"result": RESULT, "files": entries,
        "temporary_active_checkpoint_artifact": artifact, "temporary_active_checkpoint_retention_days": 1,
        "reproducible_rows_certificates_or_input_bundles_in_git_or_release": False})
    save(out/REFERENCE, {"result": RESULT, "manifest_file": manifest.name,
        "manifest_sha256": sha(manifest), "manifest_bytes": manifest.stat().st_size,
        "file_count": len(entries), "full_outputs_artifact": artifact,
        "automatic_git_or_release_publication": False})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    paths = {"core": S/item["core"], "proof": topic_path(item["proof"]),
             "method": topic_path(item["method"]), "module_helper": S/item["module_helper"],
             "field_core": S/item["field_core"], "io_helper": S/item["io_helper"]}
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {
        "result": RESULT, "p": 41, "source_repository": "Rogerhu12/math-research-public",
        "source_commit": source, "job": item,
        **{key+"_sha256": sha(path) for key, path in paths.items()},
        "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "workflow_sha256": sha(REPO/item["workflow"]),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "new_arithmetic": "complete original L-polynomial preimages and both Laurent overlap containments",
        "old_Fourier_CM_Hom_function_S5_regular_multiplier_computations_repeated": False,
        "five_function_DAG_radical_eta_or_height_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41 and item["requested_stage"] == SCOPE
        assert item["producer_inputs_pending"] is False
        assert set(item["retained_artifacts"]) == {"R811"}
        assert item["matrix_tile_size"] == 16 and item["transcript_archive_operations_per_chunk"] == 128
        assert item["expected_original_polar_degree_for_final_comparison_only"] == 1206
        assert sha(paths["core"]) == item["core_sha256"] and sha(__file__) == item["wrapper_sha256"]
        assert sha(paths["proof"]) == item["R811_proof_sha256"] == PROOF_SHA
        assert sha(paths["method"]) == item["polynomial_method_sha256"]
        assert sha(paths["module_helper"]) == item["module_helper_sha256"]
        assert sha(paths["field_core"]) == item["field_core_sha256"] == FIELD_SHA
        assert item["io_helper"] == IO_HELPER and sha(paths["io_helper"]) == item["io_helper_sha256"] == IO_SHA
        restore_resume(item, out)
        retained, _, _ = prepare_inputs(item, out)
        config = out.parent/"job-config.json"
        save(config, item)
        command = [sys.executable, "-u", str(paths["core"]), "--config", str(config),
            "--proof", str(paths["proof"]), "--method", str(paths["method"]),
            "--module-helper", str(paths["module_helper"]), "--field-core", str(paths["field_core"]),
            "--retained", str(retained), "--output", str(out),
            "--budget-minutes", str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w") as log:
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60+120)
            except subprocess.TimeoutExpired:
                error = "Budget reached; latest atomic operations, pending completed tiles and transcripts retained."
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                code = 124
    except Exception as exception:
        error = type(exception).__name__+": "+str(exception)
    core_receipt = out/"core-receipt.json"
    receipt = read(core_receipt) if core_receipt.exists() else {"complete": False}
    complete = code == 0 and receipt.get("complete") is True
    save(out/"run-receipt.json", {
        "result": RESULT, "p": 41, "complete": complete, "process_exit_code": code, "error": error,
        "source_commit": source, "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "execution_environment": "public-repository-github-actions",
        "core_receipt_sha256": sha(core_receipt) if core_receipt.exists() else None,
        "actual_original_base_map_polar_divisor_computed": complete,
        "five_function_DAG_radical_eta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete, "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)

class Review:
    """IO-only access to live complete stages and archived historical operation bytes."""
    def __init__(self, out, tag, certificate):
        self.out, self.tag = out, tag
        manifest = certificate["stage_manifest"]
        assert file_spec(out/manifest["file"]) == manifest
        data = read(out/manifest["file"])
        assert data["complete"] is True and data["configuration"] == tag
        assert data["archive_member_hashes_in_individual_archive_indexes"] is True
        assert data["historical_large_work_payloads_explicitly_pruned_only_after_exact_chart_completion"] is True
        self.entries = {row["file"]: row for row in data["files"]}
        self.archives = {row["file"]: row for row in data["transcript_archives"]}
        assert len(self.entries) == len(data["files"]) and len(self.archives) == len(data["transcript_archives"])
        for name, entry in self.entries.items():
            check_spec(entry)
            assert file_spec(out/name) == entry
            value = read(out/name)
            assert value["complete"] is True and value["configuration"] == tag
        for name, entry in self.archives.items():
            check_spec(entry)
            assert file_spec(out/name) == entry
        assert set(self.entries) == {path.name for path in out.glob("R811-polar-*.json.gz")
                                    if path.name != manifest["file"]}
        assert set(self.archives) == {path.name for path in out.glob("R811-polar-*-transcript-*.tar.gz")}
        assert not list(out.glob("R811-polar-*-current.json.gz"))
        self.archive_member_count = 0
        self.archives_reviewed = set()

    def stage(self, entry):
        assert self.entries[entry["file"]] == plain(entry)
        data = read(self.out/entry["file"])
        assert data["complete"] is True and data["configuration"] == self.tag
        return data

    def vector(self, entry, number, count, orientation="columns"):
        index = self.stage(entry)
        assert index["kind"] == "exact_polynomial_vector"
        assert index["vector_index"] == number and index["length"] == count
        assert index["orientation"] == orientation and index["tile_size"] == 16
        ranges = [(first, min(first+16, count)) for first in range(0, count, 16)]
        assert len(index["tiles"]) == len(ranges)
        for tile_spec, (first, stop) in zip(index["tiles"], ranges):
            assert (tile_spec["first"], tile_spec["stop"]) == (first, stop)
            tile = self.stage(tile_spec)
            assert tile["kind"] == "exact_polynomial_vector_tile"
            assert tile["matrix_label"] == index["matrix_label"] and tile["vector_index"] == number
            assert tile["orientation"] == orientation
            assert (tile["first"], tile["stop"]) == (first, stop)
            assert len(tile["coefficients"]) == stop-first
            for value in tile["coefficients"]:
                polynomial(value)
        return index

    def archived_records(self, entry):
        data = self.stage(entry)
        assert data["kind"] == "archived_original_unimodular_transcript"
        archive = data["archive"]
        assert self.archives[archive["file"]] == archive
        assert archive["file"] not in self.archives_reviewed
        self.archives_reviewed.add(archive["file"])
        assert data["original_plan_and_receipt_bytes_not_transformed"] is True
        assert data["mathematical_operations_not_replayed_during_archiving"] is True
        members = data["original_member_specs"]
        assert len(members) == 2*(data["last_operation_exclusive"]-data["first_operation"])
        assert len({row["file"] for row in members}) == len(members)
        with tarfile.open(self.out/archive["file"], "r:gz") as source:
            actual = iter(source)
            for specification in members:
                check_spec(specification)
                member = next(actual)
                assert member.isfile() and PurePosixPath(member.name).name == member.name == specification["file"]
                assert member.size == specification["bytes"]
                digest, total = hashlib.sha256(), 0
                # Preserve bounded memory even when an exact elementary coefficient becomes large.
                with tempfile.SpooledTemporaryFile(max_size=1024*1024) as temporary:
                    with source.extractfile(member) as stream:
                        for block in iter(lambda: stream.read(1024*1024), b""):
                            temporary.write(block)
                            digest.update(block)
                            total += len(block)
                    assert total == specification["bytes"] and digest.hexdigest() == specification["sha256"]
                    temporary.seek(0)
                    with gzip.GzipFile(fileobj=temporary, mode="rb") as compressed:
                        value = json.load(io.TextIOWrapper(compressed, encoding="utf-8"))
                assert value["configuration"] == self.tag and value["complete"] is True
                self.archive_member_count += 1
                yield specification, value
            assert next(actual, None) is None

    def transcript(self, final_spec, archived_specs, closed_spec):
        final = self.stage(final_spec)
        assert final["kind"] == "completed_polynomial_matrix"
        label = final["matrix_label"]
        initial = self.stage(final["initialization"])
        assert initial["kind"] == "matrix_initialization"
        for key in ("matrix_label", "vector_count", "vector_length", "orientation", "tile_size"):
            assert initial[key] == final[key]
        assert len(initial["vectors"]) == len(final["vectors"]) == final["vector_count"]
        vectors, previous, operation = list(initial["vectors"]), None, 0
        chunks = []
        for entry in archived_specs:
            row = self.stage(entry)
            if row["matrix_final_index"] == final_spec:
                chunks.append((row["first_operation"], entry, row))
        chunks.sort(key=lambda row: row[0])
        for first, entry, index in chunks:
            assert first == operation and index["closed_chart_certificate"] == closed_spec
            assert 0 < index["last_operation_exclusive"]-first <= 128
            iterator = iter(self.archived_records(entry))
            for number in range(first, index["last_operation_exclusive"]):
                plan_spec, plan = next(iterator)
                receipt_spec, receipt = next(iterator)
                assert plan_spec["file"] == label+"-op-"+str(number).zfill(10)+"-plan.json.gz"
                assert receipt_spec["file"] == label+"-op-"+str(number).zfill(10)+"-receipt.json.gz"
                assert plan["kind"] == "unimodular_operation_plan"
                assert receipt["kind"] == "completed_unimodular_operation"
                assert plan["matrix_label"] == receipt["matrix_label"] == label
                assert plan["operation_number"] == receipt["operation_number"] == number == operation
                assert receipt["operation_plan"] == plan_spec
                indices = plan["indices"]
                assert indices == receipt["indices"] and 1 <= len(indices) <= 2
                assert len(indices) == len(set(indices))
                assert all(0 <= i < len(vectors) for i in indices)
                assert receipt["before_vectors"] == plan["before_vectors"] == [vectors[i] for i in indices]
                assert receipt["previous_operation_receipt"] == plan["previous_operation_receipt"] == previous
                assert receipt["before_control"] == plan["before_control"]
                assert receipt["after_control"] == plan["after_control"]
                assert plan["operator_side"] == ("right_columns" if final["orientation"] == "columns" else "left_rows")
                assert plan["plan_complete_but_not_an_applied_matrix_checkpoint"] is True
                assert plan["unit_determinant_verified_over_original_L"] is True
                assert receipt["unit_determinant_verified_over_original_L"] is True
                assert receipt["all_affected_tiles_completed_before_checkpoint_commit"] is True
                assert receipt["actual_unit_determinant"] == plan["actual_unit_determinant"]
                determinant = plan["actual_unit_determinant"]
                polynomial(determinant)
                assert len(determinant) == 1
                operator = plan["elementary_matrix"]
                assert len(operator) == len(indices) and all(len(row) == len(indices) for row in operator)
                for row in operator:
                    for coefficient in row:
                        polynomial(coefficient)
                assert len(receipt["after_vectors"]) == len(indices)
                for i, value in zip(indices, receipt["after_vectors"]):
                    check_spec(value)
                    vectors[i] = value
                previous = receipt_spec
                operation += 1
            assert next(iterator, None) is None
        assert operation == final["operation_count"]
        assert vectors == final["vectors"] and previous == final["last_operation_receipt"]
        history = final["history"]
        assert history["operation_count"] == operation
        assert history["initialization"] == final["initialization"]
        assert history["last_operation_receipt"] == previous
        assert history["complete_unimodular_transcript_metadata_chain_verified"] is True
        assert history["all_operation_plans_and_receipts_retained"] is True
        assert history["superseded_large_intermediate_vectors_retained"] is False
        return final


def review_chart(review, chart, certificate):
    entry = certificate["complete_affine_preimages"][chart]
    data = review.stage(entry)
    assert data["chart"] == chart and data["variable"] == ("z" if chart == "tau" else "t")
    assert data["source_original_target_indexes"] == certificate["source_original_A_B_multiplier_indexes"]
    assert data["source_original_b_model"] == certificate["original_field_model"]
    assert data["normal_affine_basis_rank"] == FREE and data["normal_basis_degrees"] == EPS
    assert data["ideal_H_rows"] == [0, FREE] and data["denominator_relation_W_rows"] == [FREE, 2*FREE]
    for key in ("full_row_rank_from_actual_nonzero_original_denominator",
                "full_kernel_not_only_selected_solutions", "kernel_projection_injective_over_original_function_field",
                "all_final_Hermite_columns_transport_W_by_same_unimodular_operations",
                "actual_degree_counts_all_residue_degrees_and_multiplicities",
                "complete_original_normal_polar_preimage_certified", "ideal_equals_full_preimage_MA_v_in_MB_R"):
        assert data[key] is True
    for key in ("original_function_pair_constants_rescaled", "old_function_multipliers_or_CM_coordinates_recomputed",
                "global_degree_or_eta_claimed_from_single_chart"):
        assert data[key] is False
    named = {
        "source": data["immutable_unreduced_original_pair"],
        "reduced": data["unimodular_column_reduction"],
        "rows": data["reverse_time_original_left_operator_kernel"],
        "joint": data["joint_Hermite_kernel"]}
    ideal = certificate["original_polar_ideal_bases"][chart]
    assert ideal == {"joint_kernel": named["joint"], "ideal_rows": [0, FREE],
                     "companion_W_rows": [FREE, 2*FREE]}
    retention = review.stage(certificate["work_retention_receipts"][chart])
    assert retention["closed_chart_certificate"] == entry
    assert retention["retained_joint_Hermite_basis"] == named["joint"]
    assert retention["only_final_normal_ideal_joint_basis_retained_as_large_work_matrix"] is True
    assert retention["original_retained_R811_producer_files_deleted_or_changed"] is False
    assert retention["all_small_transcripts_retained_in_source_bound_exact_archives"] is True
    archives = retention["unmodified_transcript_archive_indexes"]
    final = {key: review.transcript(value, archives, entry) for key, value in named.items()}
    expected_shapes = {
        "source": (2*FREE, FREE, "columns"), "reduced": (2*FREE, FREE, "columns"),
        "rows": (2*FREE, FREE, "rows"), "joint": (FREE, 2*FREE, "columns")}
    for key, (count, length, orientation) in expected_shapes.items():
        value = final[key]
        assert (value["vector_count"], value["vector_length"], value["orientation"]) == (count, length, orientation)
        assert value["tile_size"] == 16
    original = final["source"]
    assert original["operator_pair_is_exact_original_MA_and_negative_MB"] is True
    assert original["source_original_pair_definition"] == {
        "original_R811_target_indexes": certificate["source_original_A_B_multiplier_indexes"],
        "chart": chart, "operator_pair": "[M_A,-M_B]", "source_original_b_model": certificate["original_field_model"]}
    assert original["source_B_actually_nonzero"] is True
    assert original["new_regular_multiplier_or_new_original_model_computed"] is False
    reduced, rows, joint = final["reduced"], final["rows"], final["joint"]
    assert reduced["actual_pivot_rank"] == joint["actual_pivot_rank"] == FREE
    assert reduced["canonical_column_Hermite_remainders"] is False
    assert joint["canonical_column_Hermite_remainders"] is True
    for value in (reduced, joint):
        assert value["all_diagonal_entries_nonzero_and_monic"] is True
        assert value["all_columns_after_pivot_block_zero_in_pivot_rows"] is True
        assert value["all_column_operations_unimodular_over_original_L_polynomial_ring"] is True
        assert value["exact_original_column_module_preserved"] is True
    assert rows["source_reduced_matrix"] == named["reduced"]
    assert rows["source_operation_count"] == reduced["operation_count"] == rows["operation_count"]
    assert rows["all_original_operators_left_multiplied_in_reverse_time"] is True
    assert rows["operators_inverted_or_reordered"] is False
    assert rows["complete_original_polynomial_kernel_basis_constructed"] is True
    init_reduced = review.stage(reduced["initialization"])
    assert init_reduced["source"] == {
        "immutable_unreduced_original_pair": named["source"],
        "borrowed_source_vectors_never_mutated_or_deleted_by_work_cleanup": True}
    assert init_reduced["vectors"] == original["vectors"]
    init_joint = review.stage(joint["initialization"])
    assert init_joint["source"] == {"source_kernel_row_matrix": named["rows"], "operation": "storage transpose"}
    diagonal = joint["actual_diagonal"]
    assert data["actual_diagonal"] == diagonal and len(diagonal) == FREE
    for index, row in enumerate(diagonal):
        assert row["index"] == index
        polynomial(row["polynomial"])
        assert len(row["polynomial"])-1 == row["degree"]
        assert 0 <= row["order_at_zero"] <= row["degree"]
    assert data["actual_polynomial_module_colength"] == sum(row["degree"] for row in diagonal)
    assert data["actual_variable_zero_boundary_length"] == sum(row["order_at_zero"] for row in diagonal)
    for column, vector_spec in enumerate(joint["vectors"]):
        review.vector(vector_spec, column, 2*FREE)
    verification = review.stage(data["direct_complete_original_polynomial_kernel_identity"])
    assert verification["source_original_pair_matrix"] == named["source"]
    assert verification["source_joint_Hermite_kernel"] == named["joint"]
    assert verification["full_matrix_shape"] == [FREE, FREE]
    assert verification["all_input_columns"] == 2*FREE
    assert verification["full_original_Mp_H_equals_Mq_W_verified_exactly"] is True
    assert verification["complete_kernel_from_unimodular_transcript_also_required"] is True
    blocks = verification["full_row_block_certificates"]
    assert len(blocks) == FREE*17
    for index, block_spec in enumerate(blocks):
        column, offset = divmod(index, 17)
        first, stop = offset*16, min(offset*16+16, FREE)
        block = review.stage(block_spec)
        assert block["source_original_pair_matrix"] == named["source"]
        assert block["source_joint_Hermite_kernel"] == named["joint"]
        assert block["source_kernel_column"] == joint["vectors"][column]
        assert block["kernel_column"] == column and (block["row_first"], block["row_stop"]) == (first, stop)
        assert block["all_input_columns_consumed"] == 2*FREE
        assert block["all_exact_polynomial_entries_zero"] is True
    pruning = review.stage(retention["superseded_work_file_pruning_plan"])
    assert pruning["closed_chart_certificate"] == entry
    assert pruning["retained_joint_Hermite_basis"] == named["joint"]
    prefixes = [final[key]["matrix_label"]+"-v-" for key in ("source", "reduced", "rows")]
    assert pruning["removable_matrix_prefixes"] == prefixes
    assert pruning["full_exact_Mp_H_equals_Mq_W_already_complete"] is True
    deleted = pruning["superseded_large_files"]
    assert len({row["file"] for row in deleted}) == len(deleted)
    for row in deleted:
        check_spec(row)
        assert any(row["file"].startswith(prefix) for prefix in prefixes)
        assert not (review.out/row["file"]).exists()
    assert retention["actual_superseded_large_file_count"] == len(deleted)
    assert retention["actual_superseded_large_bytes"] == sum(row["bytes"] for row in deleted)
    assert not any(name.startswith(prefix) for name in review.entries for prefix in prefixes)
    return data


def review_overlap(review, certificate, source_chart, target_chart):
    key = source_chart+"_to_"+target_chart
    index = review.stage(certificate["full_two_chart_overlap_containments"][key])
    source = certificate["original_polar_ideal_bases"][source_chart]["joint_kernel"]
    target = certificate["original_polar_ideal_bases"][target_chart]["joint_kernel"]
    assert index["source_basis"] == source and index["target_basis"] == target
    assert index["from_chart"] == source_chart and index["to_chart"] == target_chart
    assert index["normal_basis_rank"] == FREE and index["normal_basis_degrees"] == EPS
    assert index["full_exact_Laurent_module_containment_verified"] is True
    assert index["transport_formula"] == "diag(variable^-eps)*source_basis(1/variable)"
    assert index["reverse_direction_uses_D(1/z)^-1_equal_diag(z^-eps)"] is (source_chart == "sigma")
    assert index["source_function_pair_constant_preserved"] is True
    assert len(index["column_certificates"]) == FREE
    for column, entry in enumerate(index["column_certificates"]):
        data = review.stage(entry)
        assert data["source_basis"] == source and data["target_basis"] == target
        assert data["from_chart"] == source_chart and data["to_chart"] == target_chart
        assert data["source_column"] == column and len(data["containment_coefficients"]) == FREE
        for value in data["containment_coefficients"]:
            laurent(value)
        for key in ("all_reduced_denominators_are_constant_times_variable_powers",
                    "all_normal_rows_exactly_zero_after_triangular_multiply_back",
                    "homogeneous_function_pair_factor_has_already_canceled",
                    "ideal_basis_not_transported_as_a_degree_r_section"):
            assert data[key] is True


def verify(item, out):
    """Pure IO/schema review of the complete original polynomial certificate."""
    initial, run, core = (read(out/name) for name in
                           ("public-actions-input.json", "run-receipt.json", "core-receipt.json"))
    assert initial["job"] == item and initial["result"] == run["result"] == core["result"] == RESULT
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert initial["source_commit"] == run["source_commit"]
    assert initial["core_sha256"] == core["source_sha256"] == item["core_sha256"]
    assert initial["driver_sha256"] == item["wrapper_sha256"]
    assert initial["proof_sha256"] == item["R811_proof_sha256"] == PROOF_SHA
    assert initial["method_sha256"] == item["polynomial_method_sha256"]
    assert initial["module_helper_sha256"] == item["module_helper_sha256"]
    assert initial["field_core_sha256"] == item["field_core_sha256"] == FIELD_SHA
    assert initial["io_helper_sha256"] == item["io_helper_sha256"] == IO_SHA
    assert run["complete"] is True and run["process_exit_code"] == 0
    assert run["core_receipt_sha256"] == sha(out/"core-receipt.json")
    assert core["complete"] is True and core["certificate_sha256"] == sha(out/FINAL)
    assert core["completed_scope"] == SCOPE
    assert core["original_base_map_polar_divisor_computed"] is True
    assert core["complete_preimages_in_both_original_normal_affine_rings"] is True
    assert core["five_original_function_DAG_eta_or_height_computed"] is False
    root = out.parent/"retained"
    if not (root/"R811"/"full-outputs-manifest.json").exists():
        assert dict(bundle_members(out/INPUT_BUNDLE, root))
    producer = Producer("R811", item["retained_artifacts"]["R811"], root/"R811")
    selection = select_inputs(producer)
    count = verify_bundle(out/INPUT_BUNDLE, producer)
    retained = read(out/"retained-inputs-receipt.json")
    assert retained["selection"] == selection and retained["actual_selected_file_count"] == count
    assert retained["input_bundle"] == file_spec(out/INPUT_BUNDLE)
    assert retained["all_selected_bundle_members_individually_size_and_sha256_verified"] is True
    tag = expected_configuration(item, producer, selection)
    certificate = read(out/FINAL)
    assert certificate["result"] == RESULT and certificate["complete"] is True
    assert certificate["configuration"] == tag and certificate["completed_scope"] == SCOPE
    assert certificate["p"] == 41 and certificate["original_map_index"] == 4
    assert certificate["normal_affine_basis_rank"] == FREE and certificate["normal_basis_degrees"] == EPS
    assert certificate["source_R811_regular_producer"] == identity(producer.item)
    assert certificate["source_original_A_B_multiplier_indexes"] == selection["source_target_multipliers"]
    assert certificate["original_field_model"] == selection["source_original_b_model"]
    assert certificate["source_coefficient_field_basis"] == FIELD_BASIS
    assert certificate["actual_sigma_integer_n"] == selection["actual_sigma_integer_n"]
    for key in ("original_base_map_polar_divisor_computed",
                "all_polynomial_kernel_and_two_chart_containment_identities_verified",
                "complete_kernel_unimodularity_not_replaced_by_inclusion_only",
                "original_function_pair_homogeneous_factor_and_constants_preserved",
                "normal_integral_basis_preserved"):
        assert certificate[key] is True
    for key in ("cusp_radical_or_small_divisor_extraction_computed", "five_original_function_DAG_computed",
                "original_eta_rigidification_or_height_computed",
                "original_A_isogeny_kernel_coordinate_lift_computed",
                "old_CM_Hom_Laurent_S5_or_regular_multiplier_computation_repeated",
                "characteristic_zero_Krylov_matrix_or_inverse_computed"):
        assert certificate[key] is False
    review = Review(out, tag, certificate)
    tau, sigma = (review_chart(review, chart, certificate) for chart in ("tau", "sigma"))
    review_overlap(review, certificate, "tau", "sigma")
    review_overlap(review, certificate, "sigma", "tau")
    degree = review.stage(certificate["actual_degree_certificate"])
    assert degree["tau_complete_preimage"] == certificate["complete_affine_preimages"]["tau"]
    assert degree["sigma_complete_preimage"] == certificate["complete_affine_preimages"]["sigma"]
    assert degree["degree_on_tau_chart"] == tau["actual_polynomial_module_colength"] == certificate["degree_on_tau_chart"]
    assert degree["degree_on_missing_boundary_from_sigma_chart"] == sigma["actual_variable_zero_boundary_length"]
    assert degree["degree_on_missing_boundary_from_sigma_chart"] == certificate["degree_on_missing_boundary_from_sigma_chart"]
    assert degree["actual_global_degree"] == degree["degree_on_tau_chart"]+degree["degree_on_missing_boundary_from_sigma_chart"]
    assert degree["actual_global_degree"] == certificate["actual_global_pole_degree"]
    assert degree["independently_known_original_map_degree"] == item["expected_original_polar_degree_for_final_comparison_only"] == 1206
    for key in ("actual_count_matches_original_degree", "two_whole_affine_colengths_not_added",
                "residue_degrees_and_nonreduced_multiplicities_included",
                "known_degree_not_used_to_construct_or_adjust_output"):
        assert degree[key] is True
    assert degree["actual_global_degree"] == 1206
    assert review.archives_reviewed == set(review.archives)
    assert not any(re.fullmatch(r".+-op-[0-9]{10}-(plan|receipt)\.json\.gz", name) for name in review.entries)
    full = read(out/"full-outputs-manifest.json")
    assert full["result"] == RESULT
    names = set()
    for row in full["files"]:
        check_spec(row)
        assert row["file"] not in names and file_spec(out/row["file"]) == plain(row)
        names.add(row["file"])
    assert names == {path.name for path in out.iterdir() if path.is_file()
                     and path.name not in ("full-outputs-manifest.json", REFERENCE)}
    reference = read(out/REFERENCE)
    assert reference["manifest_sha256"] == sha(out/"full-outputs-manifest.json")
    assert reference["manifest_bytes"] == (out/"full-outputs-manifest.json").stat().st_size
    assert reference["file_count"] == len(names)
    print(json.dumps({"R811_POLAR_VERIFY_REVIEW": {
        "complete": True, "selected_original_input_files_verified": count,
        "complete_stage_files_verified": len(review.entries),
        "original_transcript_archives_verified": len(review.archives),
        "original_transcript_members_verified": review.archive_member_count,
        "actual_tau_colength": degree["degree_on_tau_chart"],
        "actual_missing_boundary_length": degree["degree_on_missing_boundary_from_sigma_chart"],
        "actual_original_polar_degree": certificate["actual_global_pole_degree"],
        "actual_core_seconds": certificate["seconds"],
        "both_full_272_by272_kernel_identities_and_both_Laurent_containments_certified": True,
        "radical_five_function_DAG_eta_or_height_computed": False}}), flush=True)
    return 0


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["compute", "verify"])
    args = parser.parse_args()
    out = Path(os.environ["RUNNER_TEMP"])/"serre-global"/RESULT/"output"
    if args.mode == "compute":
        request = read(REQUEST)
        assert request["session"] == "serre-public-astra-20261115"
        return compute(request["job"], out)
    return verify(read(out/"public-actions-input.json")["job"], out)


if __name__ == "__main__":
    sys.exit(main())



