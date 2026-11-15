#!/usr/bin/env python3
"""Public source-bound A/B-only normal-coordinate runner; all verifier operations are IO."""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import signal
import subprocess
import sys
import tarfile

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R809-public-A-B-normal-from-R824-request.json"
RESULT = "R809-original-A-B-normal-coordinates-from-R824"
FINAL = "p41-original-A-B-normal-coordinates-from-R824-certificate.json"
BUNDLE = "R809-R824-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
IO_NAME = "R824_public_original_global_polar_generators.py"
IO_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
CORE_NAME = "R809_original_A_B_normal_from_R824.py"
CORE_SHA = "cdc381fc5e1b9dfab705608f1d62a8ab80b282984479499a6edd635ea05fa62b"
FRAMEWORK_NAME = "R809_original_S5_normal_coordinates.py"
FRAMEWORK_SHA = "dedb5d6149a3c3ae86ad09e51f30c1424951a09010bf48afd948d2628e1ec21d"
ADAPTER_NAME = "R824_original_exact_relation_adapter.py"
ADAPTER_SHA = "5a6a100a561ce02350a5d538df908d4cca9575e21b251a848a3bfba9d3df1958"
PROOF_SHA = "68793d3f3911d6c2ab3d530575634a70953580c221c4c4fed5fa542a2ed88a40"
METHOD_SHA = "b38777a5fc6baadbb5bd832c5b6897338c7649f9b80b5a505dde541710dd5108"
RELATION_METHOD_SHA = "68877a988f4df5dc3a7609ea46d4f40129d40af40b5467200456829df730d818"
R787_SHA = "93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04"
R786_SHA = "4508095a95a2bcaec8c8db8fcd550fbc618b017d2bc0007945783bc109dbf851"
S5_INDEX_SHA = "f6f6f0ee2bae106ef474d2cff32c743b1d8e0a886f80c26aaf8708c89ea1c119"
R786_INDEX_SHA = "0bb7cfeda48d6759f1553dec74485a28dc16e31cf3d500a095963888973c9b35"
INVERSE_SHA = "d61b9eb35866dfca066aa5bb22042465d68b5aacf4372f75be0908e5fa9115ca"
LABELS = {"R809", "R786", "R787", "R824"}
EPS = [0]+[1]*144+[2]*127
SCALE5 = "13744803133596058624"
FIELD_BASIS = "b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b"


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


assert sha(S/IO_NAME) == IO_SHA
assert sha(S/ADAPTER_NAME) == ADAPTER_SHA
loader = importlib.util.spec_from_file_location("R809_R824_frozen_IO", S/IO_NAME)
IO = importlib.util.module_from_spec(loader)
loader.loader.exec_module(IO)
loader = importlib.util.spec_from_file_location("R809_R824_relation_IO", S/ADAPTER_NAME)
adapter = importlib.util.module_from_spec(loader)
loader.loader.exec_module(adapter)
read, save, file_spec = IO.read, IO.save, IO.file_spec
plain, fingerprint, META = IO.plain, IO.fingerprint, IO.META


def identity(spec):
    value = {key: spec[key] for key in adapter.BASE_KEYS}
    name = spec.get("certificate_name")
    if name is not None:
        value["certificate"] = {"file": name, "sha256": spec["files"][name]}
    return value


def guard():
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"


def check(item):
    assert item["result"] == RESULT and item["p"] == 41
    assert item["producer_inputs_pending"] is False
    assert set(item["retained_artifacts"]) == LABELS
    assert item["requested_target_groups"] == ["A", "B"]
    assert item["qY_count"] == 69 and item["auxiliary_prime_start"] == 1000000007
    assert item["dixon_group_columns"] == 7 and item["reconstruct_every_digits"] == 8
    assert item["core"] == CORE_NAME and item["core_sha256"] == sha(S/CORE_NAME) == CORE_SHA
    assert item["wrapper_sha256"] == sha(__file__)
    assert item["normal_framework"] == FRAMEWORK_NAME
    assert item["normal_framework_sha256"] == sha(S/FRAMEWORK_NAME) == FRAMEWORK_SHA
    assert item["relation_adapter"] == ADAPTER_NAME
    assert item["relation_adapter_sha256"] == sha(S/ADAPTER_NAME) == ADAPTER_SHA
    assert item["R809_proof_sha256"] == sha(IO.topic_path(item["proof"])) == PROOF_SHA
    assert item["A_B_consumer_method_sha256"] == sha(IO.topic_path(item["method"])) == METHOD_SHA
    assert item["relation_adapter_method_sha256"] == RELATION_METHOD_SHA
    assert item["io_helper"] == IO_NAME and item["io_helper_sha256"] == IO_SHA
    assert sha(REPO/"README.md") == item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md") == item["readme_sha256"]["topic"]
    adapter.plain(item["relation_spec"])
    for source in item["retained_artifacts"].values():
        assert IO.H64.fullmatch(source["archive_sha256"])
        assert IO.H64.fullmatch(source["manifest_sha256"])
        assert IO.H64.fullmatch(source["core_sha256"])
        assert isinstance(source["artifact_id"], int) and source["artifact_id"] > 0


class Source(IO.Producer):
    def __init__(self, label, item, directory, archive=None, relation_spec=None):
        self.label, self.item, self.directory, self.archive = label, item, Path(directory), archive
        self.directory.mkdir(parents=True, exist_ok=True)
        self.selected = {}
        mp = self.materialize(META[0], item["manifest_sha256"])
        self.manifest = read(mp)
        assert self.manifest["result"] == item["result"]
        self.files = {row["file"]: row for row in self.manifest["files"]}
        assert len(self.files) == len(self.manifest["files"])
        for row in self.files.values():
            IO.check_spec(row)
        run, core, initial = (self.raw(name) for name in META[1:])
        assert run["result"] == core["result"] == initial["result"] == item["result"]
        assert str(run["workflow_run_id"]) == str(item["run_id"])
        assert run["source_commit"] == initial["source_commit"] == item["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert core["source_sha256"] == initial["core_sha256"] == initial["job"]["core_sha256"] == item["core_sha256"]
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        name = item.get("certificate_name")
        self.certificate = None
        if name is None:
            assert label in ("R787", "R824")
            assert item["allow_completed_checkpoint"] is True and item["expected_conclusion"] == "failure"
            assert run["complete"] is False and core["complete"] is False
            assert run["process_exit_code"] in item["accepted_checkpoint_exit_codes"]
            assert run["process_exit_code"] != 0
            if label == "R787":
                configuration_stage = "R787-prime-1000000753-chart.json.gz"
            else:
                assert relation_spec is not None
                configuration_stage = relation_spec["file"]
                assert plain(self.files[configuration_stage]) == plain(relation_spec)
            assert item["configuration_stage"] == configuration_stage
            value = self.raw(configuration_stage)
            assert value["complete"] is True
            self.tag = value["configuration"]
        else:
            assert run["complete"] is core["complete"] is True and run["process_exit_code"] == 0
            assert core["certificate_sha256"] == item["files"][name] == self.files[name]["sha256"]
            self.certificate = self.raw(name)
            assert self.certificate["complete"] is True and self.certificate["result"] == item["result"]
            self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == item["core_sha256"] and self.tag["python_flint"] == "0.9.0"
        self.initial = initial


def select_sources(sources, item):
    assert set(sources) == LABELS
    r809, r786, r787, r824 = (sources[label] for label in ("R809", "R786", "R787", "R824"))
    assert r809.item["core_sha256"] == FRAMEWORK_SHA
    assert r786.item["core_sha256"] == R786_SHA and r787.item["core_sha256"] == R787_SHA
    adapter.same_producer(r809.tag["basis_producers"]["R786"], r786.item)
    adapter.same_producer(r787.tag["retained_artifacts"]["R786"], r786.item)
    r787.stage("R787-prime-1000000753-chart.json.gz")
    assert r809.tag["R809_proof_sha256"] == PROOF_SHA
    c = r809.certificate
    assert c["S5_dimension"] == 1234 and c["qY_count"] == 69 and c["full_real_coordinates"] == 1380
    assert c["normal_basis_rank"] == 272 and c["normal_basis_degrees"] == EPS
    assert c["basis_integer_scale"] == SCALE5 and c["coefficient_field_basis"] == FIELD_BASIS
    assert c["all_requested_targets_verified_in_all1380_rows"] is True
    assert c["original_scalar_and_field_normalizations_preserved"] is True
    assert c["actual_prime"] == 1000000007 and c["actual_short_minor_determinant"] == 29693114
    assert c["S5_basis_index"]["sha256"] == S5_INDEX_SHA
    assert c["modular_inverse_stage"]["sha256"] == INVERSE_SHA
    inventory = r809.stage(c["stage_manifest"])
    stages = {row["file"]: plain(row) for row in inventory["files"]}
    assert len(stages) == len(inventory["files"])
    def s809(entry):
        assert plain(entry) == stages[entry["file"]]
        return r809.stage(entry)
    basis = s809(c["S5_basis_index"])
    assert basis["dimension"] == 1234 and basis["qY_count"] == 69
    assert basis["real_coordinate_count"] == 20 and basis["full_coordinate_rows"] == 1380
    assert basis["integer_scale"] == SCALE5
    assert basis["normal_affine_basis_rank"] == 272 and basis["normal_basis_degrees"] == EPS
    mapping = [(a, j) for a, eps in enumerate(EPS) for j in range(6-eps)]
    assert len(basis["basis_rows"]) == len(mapping) == 1234
    r809.prefetch(row["source"]["file"] for row in basis["basis_rows"])
    for i, (row, pair) in enumerate(zip(basis["basis_rows"], mapping)):
        a, j = pair
        assert row["index"] == i and row["normal_basis_index"] == a
        assert row["normal_basis_degree"] == EPS[a] and row["z_degree"] == j
        data = s809(row["source"])
        for key in ("index", "normal_basis_index", "normal_basis_degree", "z_degree", "recipe"):
            assert data[key] == row[key]
        assert data["qY_count"] == 69 and data["real_coordinate_count"] == 20
        assert data["integer_scale"] == SCALE5
        assert data["all_original_term_phases_and_scales_verified"] is True
        assert data["original_R805_free_generator_unchanged"] is True
        assert len(data["integer_v_t_coefficients"]) == 69
        assert all(len(values) == 20 for values in data["integer_v_t_coefficients"])
    minor = s809(c["minor_stage"])
    rank = s809(minor["actual_rank_stage"])
    assert minor["S5_basis_index"] == rank["S5_basis_index"] == c["S5_basis_index"]
    assert minor["actual_rank"] == rank["actual_rank"] == 1234
    assert minor["row_indices"] == rank["row_indices"]
    assert minor["prime"] == rank["prime"] == 1000000007
    assert minor["actual_determinant_mod_prime"] == rank["actual_determinant_mod_prime"] == 29693114
    assert minor["minor_is_from_actual_69_term_matrix"] is True
    assert minor["column_indices"] == list(range(1234)) and minor["full_coordinate_rows"] == 1380
    inverse = s809(c["modular_inverse_stage"])
    assert inverse["prime"] == 1000000007 and inverse["minor_stage"] == c["minor_stage"]
    assert inverse["S5_basis_index"] == c["S5_basis_index"]
    assert inverse["inverse_product_exactly_verified_mod_prime"] is True
    assert inverse["composite_modulus_matrix_inversion"] is False
    assert len(inverse["inverse_mod_prime"]) == 1234
    assert all(len(row) == 1234 for row in inverse["inverse_mod_prime"])
    c786 = r786.certificate
    assert c786["basis_index"]["sha256"] == R786_INDEX_SHA
    assert c786["exact_power5_basis_dimension"] == 1234
    assert c786["basis_integer_scale"] == SCALE5 and c786["exact_K_basis_prefix_bound_qY"] == 128
    assert c786["basis_in_original_R775_saved_order"] is True
    old_basis = r786.stage(c786["basis_index"])
    assert old_basis["dimension"] == 1234 and old_basis["bound_qY"] == 128
    assert len(old_basis["basis_rows"]) == 1234
    row_names = ["R787-real-power5-row-"+str(i).zfill(4)+".json.gz" for i in range(1234)]
    r787.prefetch(row_names)
    for i, old_row in enumerate(old_basis["basis_rows"]):
        assert old_row["index"] == i
        value = r787.stage(row_names[i])
        assert value["index"] == i and value["R786_row_sha256"] == old_row["sha256"]
        assert value["all_original_phase_involutions_verified"] is True and value["averaging_used"] is False
        assert len(value["integer_t_coefficients"]) == 129
        assert all(len(row) == 20 for row in value["integer_t_coefficients"])
    relation = r824.stage(item["relation_spec"])
    r824.prefetch(row["file"] for row in relation["full_relation_verification_stages"])
    if r824.certificate is not None:
        r824.stage(r824.certificate["stage_manifest"])
        r824.stage(r824.certificate["generator_index"])
    actual = adapter.OriginalWeightFiveRelation(r824.directory, r824.item, item["relation_spec"],
        r786.item, c786["basis_index"], c["original_b_model"])
    adapter.same_producer(actual.configuration["source_identities"]["R787"], r787.item)
    for entry in actual.selected.values():
        r824.materialize(entry["file"], entry["sha256"], entry["bytes"])
    tag = {
        "result": RESULT, "source_sha256": CORE_SHA, "python_flint": "0.9.0",
        "R809_proof_sha256": PROOF_SHA, "A_B_consumer_method_sha256": METHOD_SHA,
        "relation_adapter_method_sha256": RELATION_METHOD_SHA,
        "normal_framework_sha256": FRAMEWORK_SHA, "relation_adapter_sha256": ADAPTER_SHA,
        "p": 41, "qY_count": 69, "full_coordinate_rows": 1380,
        "S5_dimension": 1234, "normal_basis_rank": 272, "normal_basis_degrees": EPS,
        "basis_integer_scale": SCALE5, "coefficient_field_basis": FIELD_BASIS,
        "original_b_model": c["original_b_model"], "actual_sigma_integer_n": c["actual_sigma_integer_n"],
        "source_identities": {label: identity(item["retained_artifacts"][label])
                              for label in ("R809", "R786", "R787")},
        "actual_R824_source": actual.identity, "actual_R824_relation": plain(item["relation_spec"]),
        "original_S5_configuration_sha256": fingerprint(r809.tag),
        "original_S5_basis_index": plain(c["S5_basis_index"]),
        "original_S5_minor": plain(c["minor_stage"]), "original_S5_modular_inverse": plain(c["modular_inverse_stage"]),
        "original_R786_basis_index": plain(c786["basis_index"]),
        "auxiliary_prime_start": item["auxiliary_prime_start"],
        "dixon_group_columns": item["dixon_group_columns"],
        "reconstruct_every_digits": item["reconstruct_every_digits"],
        "old_S5_C_targets_fixed_inverse_and_q_rows_recomputed": False,
        "original_R824_common_denominator_or_content_reinserted": False,
        "requested_targets_budget_and_wrapper_excluded_from_mathematical_identity": True,
    }
    return {"configuration": tag, "actual_R824_relation_receipt": actual.receipt(),
        "original_S5_configuration": r809.tag,
        "original_S5_basis_index": plain(c["S5_basis_index"]),
        "original_S5_minor": plain(c["minor_stage"]), "original_S5_modular_inverse": plain(c["modular_inverse_stage"]),
        "original_R786_basis_index": plain(c786["basis_index"]),
        "old_S5_row_count": 1234, "old_V5_real_row_count": 1234,
        "old_prefix_S5_inverse_or_C_targets_recomputed": False,
        "new_field_arithmetic_performed_by_IO": False}


def verify_bundle(path, groups, destination=None):
    expected = {(label, row["file"]): row for label, group in groups.items() for row in group["files"]}
    assert len(expected) == sum(len(group["files"]) for group in groups.values())
    seen = set()
    with tarfile.open(path, "r|gz") as archive:
        for member in archive:
            name = PurePosixPath(member.name)
            assert member.isfile() and len(name.parts) == 2 and not name.is_absolute()
            assert ".." not in name.parts and "\\" not in member.name
            key = tuple(name.parts)
            assert key in expected and key not in seen
            row = expected[key]
            assert member.size == row["bytes"]
            seen.add(key)
            target, temporary, output = None, None, None
            if destination is not None:
                target = Path(destination)/name
                target.parent.mkdir(parents=True, exist_ok=True)
                temporary = target.with_name(target.name+".download")
                output = temporary.open("wb")
            count, digest = 0, hashlib.sha256()
            try:
                with archive.extractfile(member) as raw:
                    for block in iter(lambda: raw.read(4*1024*1024), b""):
                        count += len(block)
                        digest.update(block)
                        if output is not None:
                            output.write(block)
            finally:
                if output is not None:
                    output.close()
            assert count == row["bytes"] and digest.hexdigest() == row["sha256"]
            if temporary is not None:
                if target.exists():
                    assert file_spec(target) == plain(row)
                    temporary.unlink()
                else:
                    temporary.replace(target)
    assert seen == set(expected)
    return len(seen)


def input_bundle(out, sources):
    groups = {label: source.closure_receipt() for label, source in sorted(sources.items())}
    temporary = out/(BUNDLE+".tmp")
    with temporary.open("wb") as stream:
        with gzip.GzipFile(fileobj=stream, mode="wb", compresslevel=2, mtime=0) as compressed:
            with tarfile.open(fileobj=compressed, mode="w|") as archive:
                for label, source in sorted(sources.items()):
                    for name, path in sorted(source.selected.items()):
                        info = archive.gettarinfo(str(path), arcname=label+"/"+name)
                        assert info.isfile()
                        info.uid = info.gid = 0
                        info.uname = info.gname = ""
                        info.mtime = 0
                        with path.open("rb") as raw:
                            archive.addfile(info, raw)
    temporary.replace(out/BUNDLE)
    count = verify_bundle(out/BUNDLE, groups)
    return groups, file_spec(out/BUNDLE), count


def restore(item, out, retained):
    previous = item.get("resume")
    if previous is None:
        return None
    assert previous["result"] == RESULT and previous["core_sha256"] == CORE_SHA
    archive = IO.Archive(previous, out.parent/"resume-transfer", whole=True)
    try:
        directory = out.parent/"resume-metadata"
        directory.mkdir(parents=True, exist_ok=True)
        mp = archive.extract_bound(META[0], previous["manifest_sha256"], directory/META[0])
        manifest = read(mp)
        assert manifest["result"] == RESULT
        files = archive.verify_all(manifest)
        def old(name):
            row = files[name]
            return archive.extract_bound(name, row["sha256"], directory/name, row["bytes"])
        initial, run, core = (read(old(name)) for name in ("public-actions-input.json", "run-receipt.json", "core-receipt.json"))
        assert initial["result"] == run["result"] == core["result"] == RESULT
        assert initial["source_commit"] == run["source_commit"] == previous["source_commit"]
        assert str(run["workflow_run_id"]) == str(previous["run_id"])
        assert core["source_sha256"] == initial["core_sha256"] == CORE_SHA
        assert run["core_receipt_sha256"] == files["core-receipt.json"]["sha256"]
        old_item = initial["job"]
        keys = ("result", "p", "core_sha256", "normal_framework_sha256", "relation_adapter_sha256",
                "R809_proof_sha256", "A_B_consumer_method_sha256", "relation_adapter_method_sha256",
                "qY_count", "auxiliary_prime_start", "dixon_group_columns", "reconstruct_every_digits",
                "requested_target_groups", "retained_artifacts", "relation_spec")
        for key in keys:
            assert old_item[key] == item[key], ("Changed actual A/B mathematics on resume", key)
        receipt = read(old("retained-inputs-receipt.json"))
        assert receipt["complete"] is True and set(receipt["producers"]) == LABELS
        assert plain(receipt["bundle"]) == plain(files[BUNDLE])
        for label in LABELS:
            assert receipt["producers"][label]["identity"] == IO.identity(item["retained_artifacts"][label])
        count = verify_bundle(old(BUNDLE), receipt["producers"], retained)
        stages = []
        for name, row in files.items():
            if name.startswith("R809-") and name.endswith(".json.gz"):
                path = archive.extract_bound(name, row["sha256"], out/name, row["bytes"])
                value = read(path)
                assert value["configuration"] == receipt["source_schema"]["configuration"]
                current = name.endswith("-dixon-current.json.gz")
                assert value["complete"] is (not current)
                if current:
                    assert value["complete_coordinates_claimed"] is False
                stages.append(plain(row))
        result = {"result": RESULT, "resumed": True, "previous": previous,
            "all_original_manifest_bytes_SHA_verified": len(files),
            "all_original_input_bundle_members_SHA_verified": count,
            "complete_stages_and_current_lifts_restored": stages,
            "original_source_schema": receipt["source_schema"], "archive": archive.receipt()}
        save(out/"resume-receipt.json", result)
        return result
    finally:
        archive.close()


def prepare(item, out):
    check(item)
    out.mkdir(parents=True, exist_ok=True)
    retained = out.parent/"retained"
    retained.mkdir(parents=True, exist_ok=True)
    resumed = restore(item, out, retained)
    sources, archives = {}, {}
    try:
        for label in sorted(LABELS):
            source_item = item["retained_artifacts"][label]
            archive = None
            if resumed is None:
                archive = IO.Archive(source_item, out.parent/("download-"+label), whole=False)
                archives[label] = archive
            sources[label] = Source(label, source_item, retained/label, archive, item["relation_spec"])
        schema = select_sources(sources, item)
        if resumed is not None:
            assert schema == resumed["original_source_schema"]
        for path in out.glob("R809-*.json.gz"):
            assert read(path)["configuration"] == schema["configuration"]
        groups, bundle, count = input_bundle(out, sources)
        receipt = {"result": RESULT, "complete": True,
            "configuration": schema["configuration"], "source_schema": schema,
            "producers": groups, "bundle": bundle, "file_count": count,
            "source_transfers": {label: archive.receipt() for label, archive in archives.items()},
            "all_selected_source_and_bundle_member_SHA_verified": True,
            "new_field_arithmetic_performed_by_IO": False}
        save(out/"retained-inputs-receipt.json", receipt)
        if resumed is None:
            save(out/"resume-receipt.json", {"result": RESULT, "resumed": False})
        print("R809_R824_INPUT_REVIEW="+json.dumps({
            "actual_R824_relation": item["relation_spec"],
            "actual_R824_source_state": schema["actual_R824_relation_receipt"]["actual_source_state"],
            "original_S5_basis_index": schema["original_S5_basis_index"],
            "original_S5_modular_inverse": schema["original_S5_modular_inverse"],
            "selected_original_files": count, "bundle": bundle,
            "all_selected_source_and_bundle_SHA_verified": True,
            "old_S5_C_targets_or_inverse_recomputed": False,
            "new_field_arithmetic_performed_by_IO": False}), flush=True)
        return retained
    finally:
        for archive in archives.values():
            archive.close()


def output_manifest(out):
    for path in out.iterdir():
        if path.is_file() and path.name.endswith((".tmp", ".download", ".partial")):
            path.unlink()
    artifact = "serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    rows = [dict(file_spec(path), artifact=artifact, included_in_git=False)
            for path in sorted(out.iterdir()) if path.is_file() and path.name not in (META[0], REFERENCE)]
    assert not any(path.is_dir() for path in out.iterdir())
    save(out/META[0], {"result": RESULT, "files": rows,
        "temporary_active_checkpoint_artifact": artifact, "temporary_active_checkpoint_retention_days": 1,
        "reproducible_data_in_git_or_release": False})
    save(out/REFERENCE, {"result": RESULT, "manifest_file": META[0],
        "manifest_bytes": (out/META[0]).stat().st_size, "manifest_sha256": sha(out/META[0]),
        "file_count": len(rows), "full_outputs_artifact": artifact,
        "automatic_git_or_release_publication": False})


def compute(item, out):
    guard()
    check(item)
    out.mkdir(parents=True, exist_ok=True)
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    for name in (FINAL, "run-receipt.json", "core-receipt.json", META[0], REFERENCE):
        (out/name).unlink(missing_ok=True)
    save(out/"public-actions-input.json", {
        "result": RESULT, "source_repository": "Rogerhu12/math-research-public",
        "source_commit": source, "job": item, "core_sha256": CORE_SHA,
        "driver_sha256": sha(__file__), "normal_framework_sha256": FRAMEWORK_SHA,
        "relation_adapter_sha256": ADAPTER_SHA, "proof_sha256": PROOF_SHA,
        "method_sha256": METHOD_SHA, "relation_adapter_method_sha256": RELATION_METHOD_SHA,
        "io_helper_sha256": IO_SHA, "request_sha256": sha(REQUEST),
        "workflow_sha256": sha(REPO/item["workflow"]),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    code, error, process = 1, None, None
    try:
        retained = prepare(item, out)
        config = out.parent/"R809-R824-math-config.json"
        save(config, item)
        command = [sys.executable, str(S/item["core"]), "--config", str(config),
            "--proof", str(IO.topic_path(item["proof"])), "--method", str(IO.topic_path(item["method"])),
            "--retained", str(retained), "--output", str(out), "--budget-minutes", str(item["budget_minutes"])]
        def stop(signum, frame):
            if process is not None and process.poll() is None:
                process.send_signal(signum)
        signal.signal(signal.SIGTERM, stop)
        signal.signal(signal.SIGINT, stop)
        with (out/"core.log").open("w") as log:
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, text=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                error = "Outer wallclock limit reached; complete stages and the latest source-bound checkpoint retained."
                if process.poll() is None:
                    process.terminate()
                try:
                    process.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait()
                code = 124
    except BaseException as exc:
        error = type(exc).__name__+": "+str(exc)
        print("R809_R824_RUNNER_ERROR="+error, flush=True)
        code = 1
    finally:
        if not (out/"core-receipt.json").exists():
            save(out/"core-receipt.json", {
                "result": RESULT, "complete": False, "source_sha256": CORE_SHA,
                "runner_error": error, "process_exit_code": code,
                "complete_source_bound_stages_and_current_lifts_preserved": True})
        complete = code == 0 and (out/FINAL).exists() and read(out/"core-receipt.json")["complete"] is True
        receipt = {"result": RESULT, "source_commit": source,
            "workflow_run_id": os.environ["GITHUB_RUN_ID"], "workflow_run_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
            "process_exit_code": code, "complete": complete,
            "core_receipt_sha256": sha(out/"core-receipt.json"),
            "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "runner_error": error, "automatic_git_or_release_publication": False}
        save(out/"run-receipt.json", receipt)
        output_manifest(out)
        print("R809_R824_RUN_RECEIPT="+json.dumps(receipt, sort_keys=True), flush=True)
    return code


def target_tag(target, item, schema, source):
    receipt = schema["actual_R824_relation_receipt"]
    return {
        "basis_configuration_sha256": fingerprint(schema["configuration"]), "target": target,
        "coefficient_field_basis": FIELD_BASIS,
        "original_b_model": source.certificate["original_b_model"],
        "original_b_model_source": dict(file_spec(source.directory/source.item["certificate_name"]), producer="R809"),
        "actual_R824_source": receipt["actual_producer"],
        "actual_R824_relation": plain(item["relation_spec"]),
        "original_R824_free_column": receipt["actual_free_column"],
        "original_field_lambda": receipt["field"]["lambda"],
        "original_R786_basis_index": schema["original_R786_basis_index"],
        "original_S5_producer": identity(source.item),
        "original_S5_basis_index": schema["original_S5_basis_index"],
        "homogeneous_target": target, "normal_function": target+"/tau^5",
        "regular_degree_bound": 5, "common_R824_denominator_or_content_reinserted": False,
        "Bfield_to_b_column_factor": "lambda^(column mod7), same two s blocks",
    }


def verify(out):
    """Verify the complete artifact and original source closure, with no arithmetic imports."""
    out = Path(out)
    manifest = read(out/META[0])
    assert manifest["result"] == RESULT
    files = {row["file"]: row for row in manifest["files"]}
    assert len(files) == len(manifest["files"])
    assert {path.name for path in out.iterdir() if path.is_file()} == set(files) | {META[0], REFERENCE}
    for name, row in files.items():
        IO.check_spec(row)
        assert file_spec(out/name) == plain(row)
    reference = read(out/REFERENCE)
    assert reference["result"] == RESULT and reference["manifest_sha256"] == sha(out/META[0])
    assert reference["manifest_bytes"] == (out/META[0]).stat().st_size
    assert reference["file_count"] == len(files)
    initial, run, core = (read(out/name) for name in ("public-actions-input.json", "run-receipt.json", "core-receipt.json"))
    item = initial["job"]
    assert initial["result"] == run["result"] == core["result"] == RESULT
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert initial["source_commit"] == run["source_commit"]
    assert initial["core_sha256"] == item["core_sha256"] == core["source_sha256"] == CORE_SHA
    assert initial["driver_sha256"] == item["wrapper_sha256"]
    assert initial["normal_framework_sha256"] == FRAMEWORK_SHA
    assert initial["relation_adapter_sha256"] == ADAPTER_SHA
    assert initial["proof_sha256"] == PROOF_SHA and initial["method_sha256"] == METHOD_SHA
    assert run["complete"] is core["complete"] is True and run["process_exit_code"] == 0
    assert run["core_receipt_sha256"] == files["core-receipt.json"]["sha256"]
    assert core["certificate_sha256"] == files[FINAL]["sha256"]
    receipt = read(out/"retained-inputs-receipt.json")
    assert receipt["complete"] is True and set(receipt["producers"]) == LABELS
    assert plain(receipt["bundle"]) == plain(files[BUNDLE])
    retained = out.parent/"retained"
    count = verify_bundle(out/BUNDLE, receipt["producers"], retained)
    assert count == receipt["file_count"]
    sources = {label: Source(label, item["retained_artifacts"][label], retained/label,
                             relation_spec=item["relation_spec"]) for label in LABELS}
    schema = select_sources(sources, item)
    assert schema == receipt["source_schema"] and receipt["configuration"] == schema["configuration"]
    for label, source in sources.items():
        group = receipt["producers"][label]
        assert group["identity"] == IO.identity(item["retained_artifacts"][label])
        assert {row["file"] for row in group["files"]} == set(source.selected)
    cert = read(out/FINAL)
    tag = schema["configuration"]
    assert cert["result"] == RESULT and cert["complete"] is True and cert["configuration"] == tag
    assert cert["completed_scope"] == "A_and_B_only_from_one_true_R824_relation"
    assert cert["requested_target_groups"] == cert["completed_target_groups"] == ["A", "B"]
    assert cert["completed_rational_RHS_columns"] == 28 and cert["S5_dimension"] == 1234
    assert cert["qY_count"] == 69 and cert["full_real_coordinates"] == 1380
    assert cert["normal_basis_rank"] == 272 and cert["normal_basis_degrees"] == EPS
    assert cert["basis_integer_scale"] == SCALE5 and cert["coefficient_field_basis"] == FIELD_BASIS
    assert cert["actual_prime"] == 1000000007 and cert["actual_short_minor_determinant"] == 29693114
    assert cert["original_b_model"] == sources["R809"].certificate["original_b_model"]
    assert cert["original_S5_producer"] == identity(item["retained_artifacts"]["R809"])
    for key, original in (("S5_basis_index", "original_S5_basis_index"),
                          ("minor_stage", "original_S5_minor"),
                          ("modular_inverse_stage", "original_S5_modular_inverse")):
        assert cert[key] == schema[original]
    assert cert["external_S5_references_keep_their_original_configuration"] is True
    assert cert["actual_R824_source"] == schema["actual_R824_relation_receipt"]["actual_producer"]
    assert cert["actual_R824_relation"] == item["relation_spec"]
    assert cert["original_R824_free_column"] == schema["actual_R824_relation_receipt"]["actual_free_column"]
    for key in ("all28_rational_RHS_columns_verified_in_all1380_rows", "actual_A_B_normal_vectors_computed",
                "original_scalar_and_field_normalizations_preserved"):
        assert cert[key] is True
    for key in ("old_C_targets_recomputed", "old_S5_rows_or_fixed_inverse_recomputed",
                "old_original_q_rows_or_phase_conversions_recomputed",
                "original_R824_denominator_and_content_reinserted",
                "synthetic_original_R809_or_R787_result_created",
                "actual_regular_multipliers_polar_ideal_eta_or_height_computed",
                "characteristic_zero_inverse_matrix_formed"):
        assert cert[key] is False
    assert cert["normal_function_equation"] == "y=normal(A)/normal(B)"
    inventory_spec = cert["stage_manifest"]
    assert plain(inventory_spec) == plain(files[inventory_spec["file"]])
    inventory = read(out/inventory_spec["file"])
    assert inventory["complete"] is True and inventory["configuration"] == tag
    stages = {row["file"]: plain(row) for row in inventory["files"]}
    assert len(stages) == len(inventory["files"])
    expected_current = {name for name in files if name.startswith("R809-") and name.endswith(".json.gz")
                        and not name.startswith("R809-R824-stage-manifest-")}
    assert expected_current == set(stages)
    assert not any(name.endswith("-dixon-current.json.gz") for name in files)
    def stage(entry, target=None):
        assert plain(entry) == stages[entry["file"]] == plain(files[entry["file"]])
        data = read(out/entry["file"])
        assert data["configuration"] == tag and data["complete"] is True
        if target is not None:
            expected = target_tag(target, item, schema, sources["R809"])
            assert data["target_configuration"] == expected
            assert data["target_configuration_sha256"] == fingerprint(expected)
        return data
    for entry in stages.values():
        data = stage(entry)
        if "target_configuration" in data:
            assert data["target"] in ("A", "B")
            stage(entry, data["target"])
    relation = stage(cert["relation_source_receipt"])
    assert relation["actual_R824_relation_receipt"] == schema["actual_R824_relation_receipt"]
    assert relation["original_S5_configuration"] == schema["original_S5_configuration"]
    assert relation["original_S5_basis_index"] == schema["original_S5_basis_index"]
    assert relation["old_S5_or_C_targets_or_fixed_inverse_recomputed"] is False
    assert set(cert["normal_vectors"]) == {"A", "B"}
    digits = {}
    for target in ("A", "B"):
        expected = target_tag(target, item, schema, sources["R809"])
        assert cert["completed_target_configurations"][target] == expected
        vector = stage(cert["normal_vectors"][target], target)
        assert vector["target"] == target and vector["normal_basis_rank"] == 272
        assert vector["normal_basis_degrees"] == EPS and vector["regular_degree_bound"] == 5
        assert vector["coefficient_field_basis"] == FIELD_BASIS
        assert vector["S5_basis_index"] == schema["original_S5_basis_index"]
        assert vector["normal_function"] == target+"/tau^5"
        for key in ("all14_original_field_columns_retained", "normal_vector_actually_nonzero",
                    "all1380_original_coordinates_verified", "weighted_polynomial_support_verified",
                    "original_field_and_scalar_normalizations_preserved"):
            assert vector[key] is True
        assert vector["literal_tau_factor_highest_S5_coefficients_zero"] is False
        assert vector["normal_ring_multiplication_or_field_division_computed"] is False
        assert vector["actual_polar_ideal_or_eta_or_height_computed"] is False
        assert len(vector["coordinate_groups"]) == 2
        coverage, target_digits = [], []
        for group, entry in enumerate(vector["coordinate_groups"]):
            value = stage(entry, target)
            indices = list(range(7*group, 7*group+7))
            assert value["target"] == target and value["group"] == group and value["column_indices"] == indices
            assert value["basis_dimension"] == 1234 and value["normal_basis_rank"] == 272
            assert value["S5_basis_index"] == schema["original_S5_basis_index"]
            assert value["fixed_minor_inverse"] == schema["original_S5_modular_inverse"]
            assert value["basis_integer_scale"] == SCALE5 and value["coefficient_field_basis"] == FIELD_BASIS
            assert value["actual_prime"] == 1000000007 and value["actual_Dixon_digits"] >= 1
            assert value["full_coordinate_rows"] == 1380 and value["all1380_original_coordinates_verified"] is True
            assert value["regular_degree_bound"] == 5 and value["literal_tau_factor_highest_S5_coefficients_zero"] is False
            assert value["rational_reconstruction_used_uniform_strict_rectangular_bound"] is True
            assert value["characteristic_zero_inverse_matrix_formed"] is False
            assert len(value["coordinate_numerators"]) == 1234
            assert all(len(row) == 7 for row in value["coordinate_numerators"])
            assert len(value["column_denominators"]) == len(value["original_target_rational_scales"]) == 7
            assert all(int(denominator) > 0 for denominator in value["column_denominators"])
            full = stage(value["source_full_target"], target)
            assert full["coefficient_field_basis"] == FIELD_BASIS
            assert full["homogeneous_basis_scale"] == SCALE5
            assert full["qY_count"] == 69 and full["full_coordinate_rows"] == 1380
            assert full["target_known_globally_in_original_V5"] is True
            assert full["old_real_rows_or_original_phase_conversion_recomputed"] is False
            assert len(full["primitive_integer_columns"]) == len(full["rational_scales"]) == 14
            assert all(len(column) == 1380 for column in full["primitive_integer_columns"])
            assert value["original_target_rational_scales"] == [full["rational_scales"][k] for k in indices]
            assert full["source_inputs"]["actual_R824_relation"] == item["relation_spec"]
            assert full["source_inputs"]["original_R824_common_denominator_or_content_reinserted"] is False
            coverage.extend(indices)
            target_digits.append(value["actual_Dixon_digits"])
        assert coverage == list(range(14))
        digits[target] = target_digits
    summary = {"result": RESULT, "complete": True,
        "source_commit": initial["source_commit"], "workflow_run_id": run["workflow_run_id"],
        "whole_output_manifest_files_verified": len(files),
        "all_retained_input_bundle_members_verified": count,
        "complete_math_stages_verified": len(stages),
        "actual_R824_relation": item["relation_spec"], "actual_A_B_normal_vectors_computed": True,
        "completed_rational_RHS_columns": 28, "full_original_rows": 1380,
        "actual_Dixon_digits": digits, "normal_vectors": cert["normal_vectors"],
        "original_S5_basis_index": schema["original_S5_basis_index"],
        "original_fixed_inverse": schema["original_S5_modular_inverse"],
        "old_S5_C_targets_or_inverse_recomputed": False,
        "actual_polar_ideal_eta_or_height_computed": False,
        "certificate": file_spec(out/FINAL), "stage_manifest": inventory_spec,
        "core_seconds": cert["seconds"], "new_field_arithmetic_executed_by_verifier": False}
    print("R809_R824_COMPLETE_IO_REVIEW="+json.dumps(summary, sort_keys=True, separators=(",", ":")), flush=True)
    return summary


def main():
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--prepare-only", action="store_true")
    args = parser.parse_args()
    if args.verify:
        verify(args.output)
        return 0
    item = read(REQUEST)["job"]
    if args.prepare_only:
        guard()
        prepare(item, args.output)
        return 0
    return compute(item, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
