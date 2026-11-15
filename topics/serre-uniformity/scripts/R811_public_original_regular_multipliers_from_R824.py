#!/usr/bin/env python3
"""R811 public IO runner; never imports a mathematical core while reviewing artifacts."""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import signal
import subprocess
import sys
import tarfile
import zipfile

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R811-public-original-regular-multipliers-from-R824-request.json"
RESULT = "R811-original-regular-multipliers-from-R824-normal-vectors"
FINAL = "p41-original-regular-multipliers-from-R824-certificate.json"
INPUT_BUNDLE = "R811-R824-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
LABELS = ("R806", "R809", "R809_basis")
FRAMEWORK_NAME = "R811_original_regular_multipliers.py"
FRAMEWORK_SHA = "849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3"
IO_NAME = "R824_public_original_global_polar_generators.py"
IO_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
CORE_NAME = "R811_original_regular_multipliers_from_R824.py"
CORE_SHA = "9760b10a1d6113a0e9c9b1bbe408252b275c84185c51f54ee3d0d7a5a22ba313"
PROOF_SHA = "263d8a15085c3fc053dac1df546ad0c3efb565d67ce312c78ec6e5ddb4dccf78"
METHOD_SHA = "b700c4ca03ba3d198e68c54b5c9a6eb9deb44d9a85b03b41e9583619db94f66d"
R809_AB_RESULT = "R809-original-A-B-normal-coordinates-from-R824"
R809_AB_SHA = "cdc381fc5e1b9dfab705608f1d62a8ab80b282984479499a6edd635ea05fa62b"
R809_BASIS_SHA = "dedb5d6149a3c3ae86ad09e51f30c1424951a09010bf48afd948d2628e1ec21d"
S5_INDEX_SHA = "f6f6f0ee2bae106ef474d2cff32c743b1d8e0a886f80c26aaf8708c89ea1c119"
EPS = [0]+[1]*144+[2]*127
FIELD_BASIS = "b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b"
META = ("full-outputs-manifest.json", "run-receipt.json",
        "core-receipt.json", "public-actions-input.json")
PATTERN_SHA = re.compile(r"[0-9a-f]{64}")


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Execution and new mathematics belong to public repository Actions.")


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        with temporary.open("wb") as stream:
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb", mtime=0, compresslevel=2) as compressed:
                compressed.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def plain(row):
    return {key: row[key] for key in ("file", "bytes", "sha256")}


def check_spec(row):
    assert Path(row["file"]).name == row["file"] and row["file"] not in ("", ".", "..")
    assert isinstance(row["bytes"], int) and row["bytes"] >= 0
    assert PATTERN_SHA.fullmatch(row["sha256"])


def identity(item):
    value = {key: item[key] for key in
             ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256", "certificate_name")}
    value["certificate_sha256"] = item["files"][item["certificate_name"]]
    return value


def same_identity(left, right):
    if "files" in left:
        left = identity(left)
    if "files" in right:
        right = identity(right)
    assert set(left) == set(right)
    for key in left:
        assert str(left[key]) == str(right[key]), ("Changed mathematical producer", key)


def topic_path(relative):
    path = (TOPIC/relative).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def github(path):
    return json.loads(subprocess.check_output(
        ["gh", "api", "repos/Rogerhu12/math-research-public/"+path], text=True))


assert sha(S/IO_NAME) == IO_SHA
loader = importlib.util.spec_from_file_location("R811_R824_frozen_public_IO", S/IO_NAME)
IO = importlib.util.module_from_spec(loader)
loader.loader.exec_module(IO)


class Archive(IO.Archive):
    """Range-select original sources; fully hash same-core continuation archives."""
    def __init__(self, item, directory, expected_conclusion="success", whole=False):
        bound = dict(item)
        bound.setdefault("expected_conclusion", expected_conclusion)
        super().__init__(bound, directory, whole=whole)

    @property
    def receipt(self):
        return IO.Archive.receipt(self)

    def verify_all_manifest_members(self, manifest):
        return self.verify_all(manifest)


def relation_source_identity(item):
    value = {key: item[key] for key in
             ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")}
    name = item["certificate_name"]
    value["certificate"] = {"file": name, "sha256": item["files"][name]}
    return value


class Producer:
    def __init__(self, label, item, directory, archive=None):
        self.label, self.item, self.directory, self.archive = label, item, Path(directory), archive
        self.directory.mkdir(parents=True, exist_ok=True)
        self.selected = {}
        manifest_path = self.materialize("full-outputs-manifest.json", item["manifest_sha256"])
        manifest = read(manifest_path)
        assert manifest["result"] == item["result"]
        self.files = {entry["file"]: entry for entry in manifest["files"]}
        assert len(self.files) == len(manifest["files"])
        for entry in self.files.values():
            check_spec(entry)
        run, core, initial = (self.raw(name) for name in META[1:])
        assert run["result"] == core["result"] == initial["result"] == item["result"]
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert str(run["workflow_run_id"]) == str(item["run_id"])
        assert run["source_commit"] == initial["source_commit"] == item["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == item["core_sha256"]
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        assert core["complete"] is True and core["source_sha256"] == item["core_sha256"]
        certname = item["certificate_name"]
        assert core["certificate_sha256"] == self.files[certname]["sha256"] == item["files"][certname]
        self.certificate, self.initial = self.raw(certname), initial
        assert self.certificate["result"] == item["result"] and self.certificate["complete"] is True
        self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == item["core_sha256"] and self.tag["python_flint"] == "0.9.0"
        inventory_spec = self.certificate["stage_manifest"]
        inventory = self.stage(inventory_spec)
        self.inventory = {entry["file"]: plain(entry) for entry in inventory["files"]}
        assert len(self.inventory) == len(inventory["files"])
        for name, entry in self.inventory.items():
            assert entry == plain(self.files[name])

    def materialize(self, name, digest, expected_bytes=None):
        assert Path(name).name == name
        path = self.directory/name
        if self.archive is not None:
            self.archive.extract_bound(name, digest, path, expected_bytes)
        else:
            assert path.is_file() and sha(path) == digest
            if expected_bytes is not None:
                assert path.stat().st_size == expected_bytes
        self.selected[name] = path
        return path

    def raw(self, name):
        entry = self.files[name]
        if name in self.item["files"]:
            assert entry["sha256"] == self.item["files"][name]
        path = self.materialize(name, entry["sha256"], entry["bytes"])
        return read(path)

    def stage(self, entry):
        assert plain(entry) == plain(self.files[entry["file"]])
        data = self.raw(entry["file"])
        assert data["complete"] is True and data["configuration"] == self.tag
        return data

    def indexed(self, entry):
        assert self.inventory[entry["file"]] == plain(entry)
        return self.stage(entry)


def select_inputs(producers):
    r806, r809, basis = producers["R806"], producers["R809"], producers["R809_basis"]
    c806, c809 = r806.certificate, r809.certificate
    assert r806.item["result"] == "R806-original-primitive-multiplication"
    assert r809.item["result"] == R809_AB_RESULT and r809.item["core_sha256"] == R809_AB_SHA
    assert basis.item["result"] == "R809-original-S5-normal-coordinates"
    assert basis.item["core_sha256"] == R809_BASIS_SHA
    cbasis = basis.certificate
    assert c809["completed_scope"] == "A_and_B_only_from_one_true_R824_relation"
    assert c809["completed_rational_RHS_columns"] == 28
    assert c809["all28_rational_RHS_columns_verified_in_all1380_rows"] is True
    assert c809["external_S5_references_keep_their_original_configuration"] is True
    assert c809["normal_function_equation"] == "y=normal(A)/normal(B)"
    assert c809["original_R824_denominator_and_content_reinserted"] is False
    assert c809["synthetic_original_R809_or_R787_result_created"] is False
    assert c809["original_S5_producer"] == relation_source_identity(basis.item)
    assert r809.tag["source_identities"]["R809"] == relation_source_identity(basis.item)
    assert r809.tag["original_S5_configuration_sha256"] == fingerprint(basis.tag)
    assert c809["actual_R824_source"] == r809.tag["actual_R824_source"]
    assert c809["actual_R824_relation"] == r809.tag["actual_R824_relation"]
    assert c809["original_b_model"] == cbasis["original_b_model"]
    assert cbasis["normal_basis_rank"] == 272 and cbasis["normal_basis_degrees"] == EPS
    assert cbasis["S5_dimension"] == 1234 and cbasis["qY_count"] == 69
    assert cbasis["full_real_coordinates"] == 1380
    assert cbasis["all_requested_targets_verified_in_all1380_rows"] is True
    assert cbasis["coefficient_field_basis"] == FIELD_BASIS
    assert c809["actual_sigma_integer_n"] == cbasis["actual_sigma_integer_n"]
    assert r809.tag["actual_sigma_integer_n"] == basis.tag["actual_sigma_integer_n"]
    relation_receipt = r809.indexed(c809["relation_source_receipt"])
    assert relation_receipt["original_S5_producer"] == relation_source_identity(basis.item)
    assert relation_receipt["original_S5_configuration"] == basis.tag
    assert relation_receipt["original_S5_basis_index"] == cbasis["S5_basis_index"]
    assert c806["normal_affine_basis_rank"] == 272
    assert c806["exact_polynomial_multiplication_computed"] is True
    assert c806["all272_columns_verified_in_all820_original_rows"] is True
    assert c806["actual_cyclic_minor_certified"] is True
    assert c809["actual_A_B_normal_vectors_computed"] is True
    assert c809["normal_basis_rank"] == 272 and c809["normal_basis_degrees"] == EPS
    assert c809["coefficient_field_basis"] == FIELD_BASIS
    same_identity(r806.tag["retained_artifacts"]["R805"], basis.tag["basis_producers"]["R805"])
    assert r806.tag["actual_sigma_integer_n"] == basis.tag["actual_sigma_integer_n"]
    interface = r806.indexed(c806["polynomial_multiplier"])
    assert interface["coordinate_groups"] == c806["exact_coordinate_groups"]
    assert interface["normal_affine_basis_rank"] == 272 and interface["normal_affine_basis_degrees"] == EPS
    assert interface["original_R805_free_basis"] == basis.tag["original_graded_free_basis"]
    assert interface["coefficient_field"] == "Q, certified by exact original rational coordinate equations"
    assert interface["all272_columns_verified_in_all820_original_rows"] is True
    assert interface["all_weighted_support_zeros_verified"] is True
    coverage = []
    for entry in interface["coordinate_groups"]:
        group = r806.indexed(entry)
        columns = group["column_indices"]
        assert len(group["coordinate_numerators"]) == 690
        assert all(len(row) == len(columns) for row in group["coordinate_numerators"])
        assert len(group["column_denominators"]) == len(columns)
        assert group["all820_original_coordinates_verified"] is True
        assert group["weighted_polynomial_support_verified"] is True
        coverage.extend(columns)
    assert coverage == list(range(272))
    witness = r806.indexed(interface["actual_cyclic_witness"])
    assert witness["actual_cyclic_rank"] == 272 and witness["actual_determinant_mod_prime"] != 0
    assert witness["candidate_index"] == interface["candidate_index"]
    assert len(witness["successful_krylov_matrix_mod_prime"]) == 272
    assert all(len(row) == 272 for row in witness["successful_krylov_matrix_mod_prime"])
    # These small original records retain the actual free-basis and primitive generation chain.
    chart = r806.indexed(c806["coordinate_chart"])
    accepted = r806.indexed(c806["accepted_candidate"])
    assert chart["original_R805_free_basis"] == interface["original_R805_free_basis"]
    assert accepted["cyclic_witness"] == interface["actual_cyclic_witness"]
    assert c809["S5_basis_index"] == cbasis["S5_basis_index"] == r809.tag["original_S5_basis_index"]
    assert c809["S5_basis_index"]["sha256"] == S5_INDEX_SHA
    s5 = basis.indexed(c809["S5_basis_index"])
    assert s5["dimension"] == 1234 and s5["normal_affine_basis_rank"] == 272
    assert s5["normal_basis_degrees"] == EPS
    assert s5["original_graded_free_basis"] == interface["original_R805_free_basis"]
    assert len(s5["basis_rows"]) == 1234
    position = 0
    for a in range(272):
        for j in range(6-EPS[a]):
            row = s5["basis_rows"][position]
            assert row["index"] == position and row["normal_basis_index"] == a
            assert row["normal_basis_degree"] == EPS[a] and row["z_degree"] == j
            position += 1
    assert c809["minor_stage"] == cbasis["minor_stage"] == r809.tag["original_S5_minor"]
    minor = basis.indexed(cbasis["minor_stage"])
    rank = basis.indexed(minor["actual_rank_stage"])
    assert minor["actual_rank"] == rank["actual_rank"] == 1234
    assert minor["S5_basis_index"] == rank["S5_basis_index"] == cbasis["S5_basis_index"]
    normal_sources = {}
    for target in ("A", "B"):
        normal_spec = c809["normal_vectors"][target]
        normal = r809.indexed(normal_spec)
        assert normal["target"] == target and normal["regular_degree_bound"] == 5
        assert normal["normal_basis_rank"] == 272 and normal["normal_basis_degrees"] == EPS
        assert normal["coefficient_field_basis"] == FIELD_BASIS
        assert normal["S5_basis_index"] == c809["S5_basis_index"]
        assert normal["all1380_original_coordinates_verified"] is True
        assert normal["weighted_polynomial_support_verified"] is True
        assert normal["normal_vector_actually_nonzero"] is True
        assert normal["target_configuration"] == c809["completed_target_configurations"][target]
        assert normal["target_configuration_sha256"] == fingerprint(normal["target_configuration"])
        coverage = []
        for entry in normal["coordinate_groups"]:
            group = r809.indexed(entry)
            assert group["target_configuration"] == normal["target_configuration"]
            assert group["target_configuration_sha256"] == normal["target_configuration_sha256"]
            assert group["target"] == target and group["S5_basis_index"] == c809["S5_basis_index"]
            assert group["all1380_original_coordinates_verified"] is True
            assert group["original_field_and_scalar_normalizations_preserved"] is True
            assert group["coefficient_field_basis"] == FIELD_BASIS
            assert group["basis_integer_scale"] == str(82**10)
            assert len(group["coordinate_numerators"]) == 1234
            assert all(len(row) == 7 for row in group["coordinate_numerators"])
            assert len(group["column_denominators"]) == len(group["original_target_rational_scales"]) == 7
            assert all(len(pair) == 2 and int(pair[1]) > 0 for pair in group["original_target_rational_scales"])
            coverage.extend(group["column_indices"])
        assert coverage == list(range(14))
        normal_sources[target] = normal_spec
    return {"R806_polynomial_multiplier": c806["polynomial_multiplier"],
            "R806_cyclic_witness": interface["actual_cyclic_witness"],
            "R806_exact_coordinate_groups": interface["coordinate_groups"],
            "R806_original_free_basis": interface["original_R805_free_basis"],
            "R809_S5_basis_index": c809["S5_basis_index"], "R809_normal_vectors": normal_sources,
            "only_actual_successful_A_and_B_consumed": True,
            "actual_normal_result": R809_AB_RESULT,
            "normal_producer": identity(r809.item), "basis_producer": identity(basis.item),
            "actual_R824_source": c809["actual_R824_source"],
            "actual_R824_relation": c809["actual_R824_relation"],
            "external_S5_configuration_preserved": True,
            "old_Fourier_or_S5_rows_selected_for_recomputation": False}


def bundle_members(bundle, root=None):
    seen = set()
    with tarfile.open(bundle, "r:gz") as archive:
        for member in archive:
            path = PurePosixPath(member.name)
            assert member.isfile() and len(path.parts) == 2 and path.parts[0] in LABELS
            assert ".." not in path.parts and not path.is_absolute() and member.name not in seen
            seen.add(member.name)
            digest, total = hashlib.sha256(), 0
            target = None if root is None else Path(root)/path.parts[0]/path.parts[1]
            temporary = None if target is None else target.with_name(target.name+".transfer")
            if temporary is not None:
                temporary.parent.mkdir(parents=True, exist_ok=True)
            source = archive.extractfile(member)
            destination = open(temporary, "wb") if temporary is not None else None
            try:
                for block in iter(lambda: source.read(1024*1024), b""):
                    digest.update(block)
                    total += len(block)
                    if destination is not None:
                        destination.write(block)
            finally:
                source.close()
                if destination is not None:
                    destination.close()
            assert total == member.size
            if temporary is not None:
                temporary.replace(target)
            yield member.name, {"file": path.parts[1], "bytes": total, "sha256": digest.hexdigest()}


def verify_bundle(bundle, producers):
    expected = {label+"/"+name: file_spec(path) for label, producer in producers.items()
                for name, path in producer.selected.items()}
    actual = dict(bundle_members(bundle))
    assert actual == expected
    return len(actual)


def prepare_inputs(item, out):
    root = out.parent/"retained"
    present = [(root/label/"full-outputs-manifest.json").exists() for label in LABELS]
    assert all(present) or not any(present), "Partial unverified input transfer."
    archives, producers, transports = [], {}, []
    for label in LABELS:
        original = item["retained_artifacts"][label]
        archive = None
        if not all(present):
            carrier = original.get("input_carrier")
            if carrier is not None:
                assert carrier["role"] == "unchanged_original_selected_files"
                assert carrier["original_result"] == original["result"]
                assert str(carrier["original_run_id"]) == str(original["run_id"])
                assert carrier["original_source_commit"] == original["source_commit"]
            archive = Archive(carrier or original, out.parent/("download-"+label))
            archives.append(archive)
        producers[label] = Producer(label, original, root/label, archive)
    selection = select_inputs(producers)
    transports = [{"producer": label, "transport": producer.archive.receipt,
                   "original_mathematical_producer_preserved": True}
                  for label, producer in producers.items() if producer.archive is not None]
    for label, producer in producers.items():
        assert {path.name for path in producer.directory.iterdir() if path.is_file()} == set(producer.selected)
    bundle = out/INPUT_BUNDLE
    if not bundle.exists():
        temporary = bundle.with_name(bundle.name+".tmp")
        with tarfile.open(temporary, "w:gz") as archive:
            for label in LABELS:
                for name in sorted(producers[label].selected):
                    archive.add(producers[label].selected[name], arcname=label+"/"+name, recursive=False)
        temporary.replace(bundle)
    count = verify_bundle(bundle, producers)
    save(out/"retained-inputs-receipt.json", {
        "result": RESULT, "producer_identities": {label: identity(producer.item) for label, producer in producers.items()},
        "selection": selection,
        "selected_files": {label: [file_spec(path) for _, path in sorted(producer.selected.items())]
                           for label, producer in producers.items()},
        "input_bundle": file_spec(bundle), "actual_selected_file_count": count,
        "all_selected_bundle_members_individually_size_and_sha256_verified": True,
        "transport_artifacts": transports, "restored_original_input_bundle_reused": all(present),
        "no_old_arithmetic_recomputed": True,
    })
    for archive in archives:
        archive.close()
    return root, producers, selection

def expected_configuration(item, producers):
    r806, r809, basis = producers["R806"], producers["R809"], producers["R809_basis"]
    interface = r806.indexed(r806.certificate["polynomial_multiplier"])
    return {
        "result": RESULT, "source_sha256": item["core_sha256"], "python_flint": "0.9.0",
        "R811_proof_sha256": item["R811_proof_sha256"], "R811_method_sha256": item["R811_method_sha256"],
        "multiplier_framework_sha256": FRAMEWORK_SHA,
        "R809_normal_producer": identity(r809.item),
        "R809_basis_producer": identity(basis.item),
        "R809_normal_configuration_sha256": fingerprint(r809.tag),
        "actual_R824_source": r809.certificate["actual_R824_source"],
        "actual_R824_relation": r809.certificate["actual_R824_relation"],
        "actual_R824_free_column": r809.certificate["original_R824_free_column"],
        "external_S5_configuration_preserved": True,
        "p": 41, "normal_affine_basis_rank": 272, "normal_basis_degrees": EPS,
        "coefficient_field_basis": FIELD_BASIS,
        "R806_producer": identity(r806.item),
        "R806_polynomial_multiplier": r806.certificate["polynomial_multiplier"],
        "R806_cyclic_witness": interface["actual_cyclic_witness"],
        "R809_basis_configuration_sha256": fingerprint(basis.tag),
        "R809_S5_basis_index": r809.certificate["S5_basis_index"],
        "original_R805_free_basis": interface["original_R805_free_basis"],
        "actual_sigma_integer_n": r806.tag["actual_sigma_integer_n"],
        "matrix_convention": "M_ba output b input a",
        "auxiliary_prime_start": item["auxiliary_prime_start"],
        "matrix_row_block_size": item["matrix_row_block_size"],
        "reconstruct_every_primes": item["reconstruct_every_primes"],
        "point_search": "original successful z0 first; then distinct nonnegative residues",
        "exact_commutator_mode": item["exact_commutator_mode"],
        "no_characteristic_zero_Krylov_matrix_or_inverse": True,
        "requested_targets_budget_and_transport_artifacts_excluded_from_mathematical_identity": True,
    }


def expected_target_configurations(tag, producers):
    producer = producers["R809"]
    answer = {}
    for target in ("A", "B"):
        entry = producer.certificate["normal_vectors"][target]
        data = producer.indexed(entry)
        original = producer.certificate["completed_target_configurations"][target]
        answer[target] = {
            "basis_configuration_sha256": fingerprint(tag), "target": target,
            "source_R809_normal_vector": entry,
            "source_R809_target_configuration": original,
            "source_R809_target_configuration_sha256": fingerprint(original),
            "regular_degree_bound": 5, "coefficient_field_basis": FIELD_BASIS,
            "original_b_model": data["original_b_model"],
        }
    return answer


def restore_resume(item, out):
    previous = item.get("resume")
    if previous is None:
        return
    archive = Archive(previous, out.parent/"download-continuation", expected_conclusion="failure", whole=True)
    manifest_path = archive.extract_bound("full-outputs-manifest.json", previous["manifest_sha256"],
                                          out.parent/"previous-full-outputs-manifest.json")
    manifest = read(manifest_path)
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
    for key in ("result", "p", "core", "core_sha256", "proof", "R811_proof_sha256",
                "method", "R811_method_sha256", "requested_stage", "requested_targets",
                "auxiliary_prime_start", "reconstruct_every_primes", "matrix_row_block_size",
                "exact_commutator_mode", "multiplier_framework", "multiplier_framework_sha256"):
        assert old[key] == item[key], ("Changed same-core continuation", key)
    for label in LABELS:
        same_identity(old["retained_artifacts"][label], item["retained_artifacts"][label])
        left, right = old["retained_artifacts"][label]["files"], item["retained_artifacts"][label]["files"]
        for name in set(left) & set(right):
            assert left[name] == right[name]
    bundle = bound(INPUT_BUNDLE)
    root = out.parent/"retained"
    actual_bundle = dict(bundle_members(bundle, root))
    assert actual_bundle
    producers = {label: Producer(label, item["retained_artifacts"][label], root/label) for label in LABELS}
    select_inputs(producers)
    bundle_count = verify_bundle(bundle, producers)
    shutil.copyfile(bundle, out/INPUT_BUNDLE)
    tag = expected_configuration(item, producers)
    target_tags = expected_target_configurations(tag, producers)
    copied, current_count = 0, 0
    for name, entry in entries.items():
        if name != FINAL and not (name.startswith("R811-") and name.endswith(".json.gz")):
            continue
        destination = archive.extract_bound(name, entry["sha256"], out/name, entry["bytes"])
        data = read(destination)
        assert data["configuration"] == tag
        current = name.endswith("-CRT-current.json.gz")
        assert data["complete"] is (not current)
        if "target_configuration" in data:
            target = data["target"]
            assert target in target_tags and data["target_configuration"] == target_tags[target]
            assert data["target_configuration_sha256"] == fingerprint(target_tags[target])
        else:
            assert "target" not in data or name == FINAL
        if current:
            assert data["complete_characteristic_zero_identity_claimed"] is False
            assert data["only_latest_large_CRT_vector_retained"] is True
            current_count += 1
        copied += 1
    save(out/"resume-receipt.json", {
        "result": RESULT, "previous_actual_artifact": previous,
        "actual_archive_review": archive.receipt,
        "all_original_manifest_members_streamed_and_sha256_verified": True,
        "actual_previous_manifest_file_count": len(entries),
        "complete_and_current_stage_files_restored": copied,
        "current_CRT_vectors_restored": current_count,
        "all_original_selected_bundle_members_verified": bundle_count,
        "input_bundle": file_spec(out/INPUT_BUNDLE),
        "same_mathematical_core_and_sources_preserved": True,
        "old_completed_arithmetic_recomputed": False,
    })
    archive.close()
    print(json.dumps({"R811_RESTORE_REVIEW": {
        "previous_run": previous["run_id"], "archive_sha256": previous["archive_sha256"],
        "manifest_sha256": previous["manifest_sha256"], "all_manifest_files_verified": len(entries),
        "restored_stage_count": copied, "restored_current_CRT_count": current_count,
        "selected_bundle_files_verified": bundle_count}}), flush=True)


def output_manifest(out):
    for path in out.iterdir():
        if path.is_file() and path.name.endswith((".tmp", ".download", ".partial")):
            path.unlink()  # Only uncommitted atomic-write temporaries in this private output directory.
    artifact = "serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    entries = [dict(file_spec(path), artifact=artifact, included_in_git=False)
               for path in sorted(out.iterdir()) if path.is_file()
               and path.name not in ("full-outputs-manifest.json", REFERENCE)]
    manifest = out/"full-outputs-manifest.json"
    save(manifest, {"result": RESULT, "files": entries,
        "temporary_active_checkpoint_artifact": artifact,
        "temporary_active_checkpoint_retention_days": 1,
        "reproducible_rows_certificates_or_input_bundles_in_git_or_release": False})
    save(out/REFERENCE, {"result": RESULT, "manifest_file": manifest.name,
        "manifest_sha256": sha(manifest), "manifest_bytes": manifest.stat().st_size,
        "file_count": len(entries), "full_outputs_artifact": artifact,
        "automatic_git_or_release_publication": False})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core, proof, method = S/item["core"], topic_path(item["proof"]), topic_path(item["method"])
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {
        "result": RESULT, "p": 41, "source_repository": "Rogerhu12/math-research-public",
        "source_commit": source, "job": item, "core_sha256": sha(core),
        "proof_sha256": sha(proof), "method_sha256": sha(method), "driver_sha256": sha(__file__),
        "multiplier_framework_sha256": sha(S/FRAMEWORK_NAME), "io_helper_sha256": IO_SHA,
        "request_sha256": sha(REQUEST),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "workflow_sha256": sha(REPO/item["workflow"]),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "new_arithmetic": "original A/B regular multipliers and same-section second-chart transport",
        "old_Fourier_S5_or_Dixon_producers_recomputed": False,
        "polar_preimages_function_DAG_eta_or_height_claimed": False,
    })
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert item["producer_inputs_pending"] is False
        assert item["requested_stage"] == "base_regular_multipliers"
        assert item["requested_targets"] == ["A", "B"]
        assert set(item["retained_artifacts"]) == set(LABELS)
        assert item["core"] == CORE_NAME
        assert sha(core) == item["core_sha256"] == CORE_SHA and sha(__file__) == item["wrapper_sha256"]
        assert item["multiplier_framework"] == FRAMEWORK_NAME
        assert item["multiplier_framework_sha256"] == sha(S/FRAMEWORK_NAME) == FRAMEWORK_SHA
        assert item["io_helper"] == IO_NAME and item["io_helper_sha256"] == IO_SHA
        assert sha(REPO/"README.md") == item["readme_sha256"]["root"]
        assert sha(TOPIC/"README.md") == item["readme_sha256"]["topic"]
        assert sha(proof) == item["R811_proof_sha256"] == PROOF_SHA
        assert sha(method) == item["R811_method_sha256"] == METHOD_SHA
        restore_resume(item, out)
        retained, _, _ = prepare_inputs(item, out)
        config = out.parent/"job-config.json"
        save(config, item)
        command = [sys.executable, "-u", str(core), "--config", str(config),
            "--proof", str(proof), "--method", str(method), "--retained", str(retained),
            "--output", str(out), "--budget-minutes", str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                error = "Budget reached; exact completed components and current CRT states retained."
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=30)
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
        "actual_original_A_B_regular_multipliers_computed": complete,
        "base_polar_preimages_computed": False, "eta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
    })
    output_manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete, "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    """Only bytes, source identities and exact-core certificate structure; no new arithmetic."""
    initial = read(out/"public-actions-input.json")
    run, core = read(out/"run-receipt.json"), read(out/"core-receipt.json")
    assert initial["job"] == item
    assert initial["result"] == run["result"] == core["result"] == RESULT
    assert initial["core_sha256"] == core["source_sha256"] == item["core_sha256"] == CORE_SHA
    assert initial["driver_sha256"] == item["wrapper_sha256"]
    assert initial["proof_sha256"] == item["R811_proof_sha256"] == PROOF_SHA
    assert initial["method_sha256"] == item["R811_method_sha256"] == METHOD_SHA
    assert initial["multiplier_framework_sha256"] == item["multiplier_framework_sha256"] == FRAMEWORK_SHA
    assert initial["io_helper_sha256"] == item["io_helper_sha256"] == IO_SHA
    assert run["source_commit"] == initial["source_commit"]
    assert run["complete"] is True and run["process_exit_code"] == 0
    assert run["core_receipt_sha256"] == sha(out/"core-receipt.json")
    assert core["complete"] is True and core["certificate_sha256"] == sha(out/FINAL)
    assert core["regular_multipliers_computed"] is True
    assert core["all_complete_polynomial_commutator_identities_verified"] is True
    assert core["base_polar_preimages_computed"] is False and core["eta_or_height_computed"] is False
    root = out.parent/"retained"
    if not all((root/label/"full-outputs-manifest.json").exists() for label in LABELS):
        transferred = dict(bundle_members(out/INPUT_BUNDLE, root))
        assert transferred
    producers = {label: Producer(label, item["retained_artifacts"][label], root/label) for label in LABELS}
    selection = select_inputs(producers)
    count = verify_bundle(out/INPUT_BUNDLE, producers)
    retained_receipt = read(out/"retained-inputs-receipt.json")
    assert retained_receipt["selection"] == selection
    assert retained_receipt["actual_selected_file_count"] == count
    assert retained_receipt["all_selected_bundle_members_individually_size_and_sha256_verified"] is True
    assert retained_receipt["input_bundle"] == file_spec(out/INPUT_BUNDLE)
    tag = expected_configuration(item, producers)
    target_tags = expected_target_configurations(tag, producers)
    certificate = read(out/FINAL)
    assert certificate["result"] == RESULT and certificate["complete"] is True
    assert certificate["configuration"] == tag
    assert certificate["completed_scope"] == "base_regular_multipliers"
    assert certificate["requested_targets"] == ["A", "B"]
    assert certificate["normal_affine_basis_rank"] == 272 and certificate["normal_basis_degrees"] == EPS
    assert certificate["coefficient_field_basis"] == FIELD_BASIS
    assert certificate["actual_input_producers"] == {label: identity(item["retained_artifacts"][label]) for label in LABELS}
    assert certificate["original_S5_configuration_preserved"] is True
    assert certificate["source_original_S5_producer"] == identity(producers["R809_basis"].item)
    assert certificate["source_original_S5_configuration_sha256"] == fingerprint(producers["R809_basis"].tag)
    assert certificate["actual_R824_source"] == producers["R809"].certificate["actual_R824_source"]
    assert certificate["actual_R824_relation"] == producers["R809"].certificate["actual_R824_relation"]
    assert certificate["actual_R824_free_column"] == producers["R809"].certificate["original_R824_free_column"]
    assert certificate["actual_normal_input_result"] == R809_AB_RESULT
    assert certificate["synthetic_R787_or_C_only_R809_A_B_output_created"] is False
    assert certificate["original_relation_denominator_or_content_reinserted"] is False
    assert certificate["source_R809_normal_vectors"] == {
            target: producers["R809"].certificate["normal_vectors"][target] for target in ("A", "B")}
    for key in ("regular_multipliers_computed", "two_chart_regular_pairs_computed",
                "all_weighted_degree_bounds_verified", "all_original_first_columns_verified_coefficientwise",
                "all_complete_polynomial_commutator_identities_verified",
                "all_original_scalar_and_field_normalizations_preserved", "normal_integral_basis_preserved"):
        assert certificate[key] is True
    for key in ("old_Fourier_Hom_Laurent_S5_or_Dixon_producer_results_recomputed",
                "characteristic_zero_Krylov_matrix_or_inverse_computed",
                "base_polar_preimages_computed", "five_original_function_DAG_computed", "eta_or_height_computed"):
        assert certificate[key] is False
    assert certificate["commutator_maximum_degree"] == 8 and certificate["exact_commutator_points"] == list(range(9))
    assert certificate["original_y_operator_pair"] == {
        "numerator": "A", "denominator": "B", "tau_chart": "(A/tau^5)/(B/tau^5)",
        "sigma_chart": "(A/sigma^5)/(B/sigma^5)", "common_t_power_cancels_exactly": 5,
        "source_B_actually_nonzero": True}
    manifest_spec = certificate["stage_manifest"]
    assert file_spec(out/manifest_spec["file"]) == manifest_spec
    inventory = read(out/manifest_spec["file"])
    assert inventory["configuration"] == tag and inventory["complete"] is True
    entries = {entry["file"]: entry for entry in inventory["files"]}
    assert len(entries) == len(inventory["files"])
    for name, entry in entries.items():
        check_spec(entry)
        assert file_spec(out/name) == entry
        data = read(out/name)
        assert data["configuration"] == tag and data["complete"] is True
        if "target_configuration" in data:
            target = data["target"]
            assert target in target_tags
            assert data["target_configuration"] == target_tags[target]
            assert data["target_configuration_sha256"] == fingerprint(target_tags[target])
    expected_stage_names = {path.name for path in out.glob("R811-*.json.gz")
                            if not path.name.startswith("R811-R824-stage-manifest-")}
    assert set(entries) == expected_stage_names
    assert not list(out.glob("R811-*-CRT-current.json.gz"))

    def referenced(entry, target=None):
        assert entries[entry["file"]] == plain(entry)
        data = read(out/entry["file"])
        if target is not None:
            assert data["target_configuration"] == target_tags[target]
        return data

    row_ranges = [(first, min(first+16, 272)) for first in range(0, 272, 16)]
    nonzero, prime_counts = {}, {}
    for target in ("A", "B"):
        target_index = referenced(certificate["target_multipliers"][target], target)
        assert target_index["target"] == target and target_index["regular_degree_bound"] == 5
        assert target_index["normal_affine_basis_rank"] == 272
        assert target_index["normal_basis_degrees"] == EPS
        assert target_index["coefficient_field_basis"] == FIELD_BASIS
        assert target_index["source_R809_normal_vector"] == certificate["source_R809_normal_vectors"][target]
        assert target_index["all14_components_verified_in_original_field_basis"] is True
        assert target_index["all_complete_polynomial_commutator_identities_verified"] is True
        components = target_index["field_component_multipliers"]
        assert len(components) == 14
        nonzero[target], prime_counts[target] = [], []
        for component, entry in enumerate(components):
            data = referenced(entry, target)
            assert data["target"] == target and data["field_component"] == component
            assert data["regular_degree_bound"] == 5 and data["coefficient_field_basis"] == FIELD_BASIS
            vector = referenced(data["source_original_vector"], target)
            assert vector["field_component"] == component and vector["regular_degree_bound"] == 5
            assert vector["source_normal_vector"] == certificate["source_R809_normal_vectors"][target]
            assert vector["original_rational_scale_applied_exactly_once"] is True
            assert vector["no_original_relation_removed_common_denominator_or_content_reinserted"] is True
            assert vector["all_original_14_field_columns_preserved"] is True
            assert len(vector["integer_vector_coefficients_low_to_high"]) == 6
            assert all(len(row) == 272 for row in vector["integer_vector_coefficients_low_to_high"])
            assert int(vector["common_positive_denominator"]) > 0
            assert data["weighted_degree_bound_verified"] is True
            assert data["original_first_column_verified_coefficientwise"] is True
            assert data["complete_polynomial_commutator_identity_verified"] is True
            prime_counts[target].append(data["actual_CRT_prime_count"])
            if data["zero_component_proved_from_exact_original_vector"]:
                assert vector["exactly_zero_component"] is True
                assert data["tau_chart_matrix_is_exact_zero"] is True and data["sigma_chart_matrix_is_exact_zero"] is True
                assert data["matrix_row_blocks_tau"] == data["matrix_row_blocks_sigma"] == []
                assert data["actual_CRT_prime_count"] == 0
                continue
            nonzero[target].append(component)
            assert vector["exactly_zero_component"] is False
            candidate = referenced(data["source_candidate"], target)
            assert candidate["matrix_row_blocks"] == data["matrix_row_blocks_tau"]
            assert candidate["source_original_vector"] == data["source_original_vector"]
            first = referenced(data["exact_first_column_certificate"], target)
            assert first["source_candidate"] == data["source_candidate"]
            assert first["original_first_column_verified_coefficientwise"] is True
            assert first["commutator_maximum_degree"] == 8
            assert data["commutator_maximum_degree"] == 8 and data["exact_commutator_points"] == list(range(9))
            assert data["identity_certified_by_strict_degree_and_r_plus_4_distinct_exact_points"] is True
            assert data["primitive_cyclic_uniqueness_identifies_true_regular_multiplier"] is True
            assert data["source_R806_cyclic_witness"] == certificate["source_R806_cyclic_witness"]
            assert len(data["matrix_row_blocks_tau"]) == len(data["matrix_row_blocks_sigma"]) == len(row_ranges)
            for tau_spec, sigma_spec, (first_row, stop) in zip(
                    data["matrix_row_blocks_tau"], data["matrix_row_blocks_sigma"], row_ranges):
                count_coefficients = sum(6+EPS[a]-EPS[b] for b in range(first_row, stop) for a in range(272))
                for block_spec in (tau_spec, sigma_spec):
                    block = referenced(block_spec, target)
                    assert block["target"] == target and block["field_component"] == component
                    assert (block["row_first"], block["row_stop"]) == (first_row, stop)
                    assert block["regular_degree_bound"] == 5
                    assert int(block["common_positive_denominator"]) > 0
                    assert len(block["coefficient_numerators"]) == count_coefficients
                sigma = referenced(sigma_spec, target)
                assert sigma["source_tau_matrix_row_block"] == tau_spec
                assert sigma["source_exact_candidate"] == data["source_candidate"]
                assert sigma["every_transition_exponent_nonnegative"] is True
                assert sigma["transported_original_first_column_verified_coefficientwise"] is True
                assert sigma["same_function_transition_omits_common_t_power"] is True
                assert sigma["common_homogeneous_factor_in_pair"] == "t^5"
                assert sigma["original_function_or_section_rescaled_by_unit"] is False
            points = data["exact_full_matrix_point_certificates"]
            assert len(points) == 9
            for point, point_spec in enumerate(points):
                point_data = referenced(point_spec, target)
                assert point_data["source_candidate"] == data["source_candidate"]
                assert point_data["exact_integer_point"] == point
                assert point_data["full_matrix_shape"] == [272, 272]
                assert point_data["all_exact_commutator_entries_zero"] is True
                assert point_data["Krylov_invertibility_not_required_at_exact_verification_point"] is True
                blocks = point_data["full_row_block_certificates"]
                assert len(blocks) == len(row_ranges)
                for block_spec, (first_row, stop) in zip(blocks, row_ranges):
                    block = referenced(block_spec, target)
                    assert block["source_candidate"] == data["source_candidate"]
                    assert block["exact_integer_point"] == point
                    assert (block["row_first"], block["row_stop"]) == (first_row, stop)
                    assert block["column_count"] == 272
                    assert block["both_products_computed_over_Z_after_exact_denominator_clearing"] is True
                    assert block["all_exact_integer_commutator_entries_zero"] is True
                    assert block["random_modular_evaluation_used_as_exact_identity"] is False
            history = referenced(data["latest_CRT_history_receipt"], target)
            assert history["current_full_CRT_checkpoint"] == candidate["source_CRT_checkpoint"]
            assert history["prime_count"] == data["actual_CRT_prime_count"]
            assert history["large_vector_or_matrix_embedded"] is False
            assert history["full_temporary_images_discarded_only_after_CRT_commit"] is True
        assert nonzero[target]
    assert certificate["actual_nonzero_field_components"] == nonzero
    assert certificate["actual_CRT_prime_counts_by_field_component"] == prime_counts
    full = read(out/"full-outputs-manifest.json")
    assert full["result"] == RESULT
    names = set()
    for entry in full["files"]:
        check_spec(entry)
        assert entry["file"] not in names and file_spec(out/entry["file"]) == plain(entry)
        names.add(entry["file"])
    assert names == {path.name for path in out.iterdir() if path.is_file()
                     and path.name not in ("full-outputs-manifest.json", REFERENCE)}
    reference = read(out/REFERENCE)
    assert reference["manifest_sha256"] == sha(out/"full-outputs-manifest.json")
    assert reference["file_count"] == len(names)
    print(json.dumps({"R811_VERIFY_REVIEW": {
        "complete": True, "selected_input_files_verified": count, "complete_stage_files_verified": len(entries),
        "actual_nonzero_field_components": nonzero,
        "actual_CRT_prime_counts_by_field_component": prime_counts,
        "exact_commutator_points": list(range(9)), "normal_affine_basis_rank": 272,
        "actual_core_seconds": certificate["seconds"], "base_polar_preimages_computed": False}}), flush=True)
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
