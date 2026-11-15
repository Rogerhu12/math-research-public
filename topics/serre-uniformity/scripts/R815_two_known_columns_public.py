#!/usr/bin/env python3
"""R815 two-known-column public IO runner; preserves both completed source identities.

Only standard-library source and checkpoint IO is imported here.  All new
common-denominator candidates and exact arithmetic run in the separately pinned
Actions core.  Range transfers are never called fresh whole-ZIP verification.
"""
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
REQUEST = TOPIC/"notes/R815_two_known_columns-public-request.json"
RESULT = "R815-original-normal-derivation-operators"
FINAL = "p41-original-normal-derivation-operator-certificate.json"
INPUT_BUNDLE = "R815-retained-producer-inputs.tar.gz"
PREVIOUS_SCAN_BUNDLE = "R815-two-columns-previous-scan-inputs.tar.gz"
PREVIOUS_SCAN_GROUP = "R815P1"
REFERENCE = "full-outputs-manifest-reference.json"
LABELS = ("R806", "R813")
ALL_LABELS = ("R806", "R813", "R815")
EPS = [0]+[1]*144+[2]*127
FIELD_BASIS = "Q in the unchanged original K-normal basis"
META = ("full-outputs-manifest.json", "run-receipt.json",
        "core-receipt.json", "public-actions-input.json")
PATTERN_SHA = re.compile(r"[0-9a-f]{64}")
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
LEGACY_CORE_SHA = "80516ff9598fdb6251628c00794dc3529b998a7c563fe80fd9c31406e3896c7d"
IO_HELPER_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
OLD_CURRENT = "R815-target-g-component-00-CRT-current.json.gz"
OLD_LAST_RECEIPT = "R815-target-g-component-00-CRT-step-000425-receipt.json.gz"
OLD_W = "R815-original-primitive-polynomial-input.json.gz"
OLD_VECTOR = {key: "R815-target-"+key+"-component-00-original-vector.json.gz" for key in ("g", "h")}
POINT_PATTERN = re.compile(r"R815-prime-([0-9]+)-z-([0-9]+)-Krylov-inverse\.json\.gz")
STEP_PATTERN = re.compile(r"R815-target-g-component-00-CRT-step-([0-9]{6})-receipt\.json\.gz")
PROJECTIVE_MODE = "two-known-columns-and-three-dimensional-Q-common-denominator"
SHIFTS = (0, 256, -256, 1024, -1024, 4096, -4096)
PROJECTIVE_STRATEGY = {
    "probe_order": "weighted output_row,input_column,power; omit columns0/1; reuse completed old prefix and only then new strict-RR failures at actual425 modulus",
    "probe_fallback": "at end, one failing entry may pair with first distinct nonzero entry outside columns0/1; all-successful RR supplies its actual lcm",
    "known_denominator": "the reduced common denominator d01 of the exact original vg and Wvg columns",
    "integer_row_lattice": "[(d01,center(d01*ri),center(d01*rj)),(0,M,0),(0,0,M)]",
    "column_weights": "wd=2^max(shift,0), wn=2^max(-shift,0)",
    "fixed_shifts": list(SHIFTS),
    "LLL_rows_consumed": "all three basis rows with complete integral unimodular witnesses; no height bound",
    "known_column_lift": "column0=D*vg and column1=D*Wvg exactly; every other coefficient=center(D*residue)",
    "exact_early_entries": "a subset of the same seven complete commutators at z0/1, input columns1/2; column0 is a construction identity",
    "success_exit": "original two full columns, weighted support, and all 272x272 entries at exact z=0,...,6",
    "known_column_stage": "exact Wvg once, joint minimal positive denominator, all1652 current congruences",
    "completed_scalar_scan": "source-bound original one-column prefix classification imported without repeated RR",
}
IO = None


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
    r806, r813 = producers["R806"], producers["R813"]
    c806, c813 = r806.certificate, r813.certificate
    assert r806.item["result"] == "R806-original-primitive-multiplication"
    assert r813.item["result"] == "R813-original-Wronskian-derivation-inputs"
    assert r806.item["core_sha256"] == "b014f9b3cb4923421e6a879eddb4da58dd0baefb28d61a2191f6b0a33e51810d"
    assert r813.item["core_sha256"] == "830ae652ebb08a035c6636c7738ab4823322111944932ffc77b1136caf7a07bc"
    assert c806["normal_affine_basis_rank"] == 272
    for key in ("exact_polynomial_multiplication_computed", "all272_columns_verified_in_all820_original_rows",
                "actual_cyclic_minor_certified", "original_function_field_primitive_generator_certified",
                "normal_integral_basis_preserved"):
        assert c806[key] is True
    assert [int(x) for x in c806["actual_w0_original_M2_integer_coordinates"]] == [int(i == 2) for i in range(146)]
    assert c813["completed_scope"] == "two_original_S3_Wronskian_inputs"
    assert c813["target_names"] == ["g", "h"] and c813["actual_rational_RHS_columns"] == 2
    assert c813["S3_basis_dimension"] == 690 and c813["qY_count"] == 41
    assert c813["full_coordinate_rows"] == 820
    assert c813["normal_basis_rank"] == 272 and c813["normal_basis_degrees"] == EPS
    assert c813["regular_degree_bound"] == 3 and c813["original_D0_qY_multiplier"] == ["1", "82"]
    for key in ("all820_original_coordinates_verified_for_both_targets",
                "both_original_normal_vectors_actually_nonzero",
                "original_1_over82_and_all_integer_scales_preserved"):
        assert c813[key] is True
    assert c813["actual_Mg_Mh_or_Gamma_computed"] is False
    same_identity(r813.tag["producer_identities"]["R806"], r806.item)
    same_identity(r813.tag["producer_identities"]["R805"], r806.tag["retained_artifacts"]["R805"])
    assert c813["actual_sigma_integer_n"] == r806.tag["actual_sigma_integer_n"]
    interface = r806.indexed(c806["polynomial_multiplier"])
    assert interface["coordinate_groups"] == c806["exact_coordinate_groups"]
    assert interface["normal_affine_basis_rank"] == 272 and interface["normal_affine_basis_degrees"] == EPS
    assert interface["original_R805_free_basis"] == r813.tag["original_graded_free_basis"]
    assert interface["original_R805_S_basis_index"] == r813.tag["original_S3_basis_index"]
    assert interface["coefficient_field"] == "Q, certified by exact original rational coordinate equations"
    assert interface["matrix_convention"] == "M_ba(z) is output row b, input column a"
    for key in ("all272_columns_verified_in_all820_original_rows", "all_weighted_support_zeros_verified",
                "reduction_equals_successful_modular_multiplier",
                "original_function_field_primitive_generator_certified", "normal_integral_basis_preserved"):
        assert interface[key] is True
    columns = []
    for entry in interface["coordinate_groups"]:
        group = r806.indexed(entry)
        indices = group["column_indices"]
        assert len(group["coordinate_numerators"]) == 690
        assert all(len(row) == len(indices) for row in group["coordinate_numerators"])
        assert len(group["column_denominators"]) == len(indices)
        assert group["integer_scale"] == str(82**6)
        assert group["all820_original_coordinates_verified"] is True
        assert group["weighted_polynomial_support_verified"] is True
        assert group["reduction_equals_successful_modular_multiplier"] is True
        columns.extend(indices)
    assert columns == list(range(272))
    witness = r806.indexed(interface["actual_cyclic_witness"])
    assert witness["actual_cyclic_rank"] == 272 and witness["actual_determinant_mod_prime"] != 0
    assert witness["candidate_index"] == interface["candidate_index"]
    assert witness["primitive_generator_certified_by_actual_minor"] is True
    assert len(witness["successful_krylov_matrix_mod_prime"]) == 272
    assert all(len(row) == 272 for row in witness["successful_krylov_matrix_mod_prime"])
    chart = r806.indexed(c806["coordinate_chart"])
    accepted = r806.indexed(c806["accepted_candidate"])
    assert chart["original_R805_free_basis"] == interface["original_R805_free_basis"]
    assert accepted["cyclic_witness"] == interface["actual_cyclic_witness"]
    definition_name = "R806-candidate-"+str(interface["candidate_index"]).zfill(10)+"-definition.json.gz"
    definition = r806.indexed(plain(r806.files[definition_name]))
    assert definition["candidate_index"] == interface["candidate_index"]
    coordinate_spec = c813["exact_coordinate_stage"]
    coordinates = r813.indexed(coordinate_spec)
    assert coordinates["target_names"] == ["g", "h"] and coordinates["column_indices"] == [0, 1]
    assert coordinates["S3_basis_dimension"] == 690 and coordinates["normal_basis_rank"] == 272
    assert coordinates["full_coordinate_rows"] == 820 and coordinates["original_S3_integer_scale"] == str(82**6)
    assert coordinates["original_D0_qY_multiplier"] == ["1", "82"]
    for key in ("all820_original_coordinates_verified", "both_original_Wronskians_actually_nonzero",
                "original_1_over82_and_all_integer_scales_preserved"):
        assert coordinates[key] is True
    assert len(coordinates["coordinate_numerators"]) == 690
    assert all(len(row) == 2 for row in coordinates["coordinate_numerators"])
    assert len(coordinates["column_denominators"]) == len(coordinates["original_target_rational_scales"]) == 2
    assert all(int(d) > 0 for d in coordinates["column_denominators"])
    assert all(len(pair) == 2 and int(pair[1]) > 0 and int(pair[0]) != 0
               for pair in coordinates["original_target_rational_scales"])
    normal_spec = c813["normal_vector_interface"]
    normal = r813.indexed(normal_spec)
    assert normal["target_column_indices"] == {"g": 0, "h": 1}
    assert normal["source_exact_S3_coordinates"] == coordinate_spec
    assert normal["normal_basis_rank"] == 272 and normal["normal_basis_degrees"] == EPS
    assert normal["regular_degree_bound"] == 3 and normal["coefficient_field"] == FIELD_BASIS
    assert normal["actual_R806_polynomial_multiplier_index"] == c806["polynomial_multiplier"]
    assert normal["actual_R806_primitive_candidate"] == c806["accepted_candidate"]
    assert normal["original_R805_graded_free_basis"] == interface["original_R805_free_basis"]
    assert normal["all820_original_coordinates_verified"] is True
    assert normal["original_1_over82_and_all_integer_scales_preserved"] is True
    assert normal["actual_Mg_Mh_or_Gamma_computed"] is False
    mapping = normal["S3_row_to_polynomial_coefficient"]
    assert len(mapping) == 690
    for index, row in enumerate(mapping):
        if index < 4:
            basis, power = 0, index
        elif index < 436:
            basis, power = 1+(index-4)//3, (index-4) % 3
        else:
            basis, power = 145+(index-436)//2, (index-436) % 2
        assert row == {"S_row": index, "normal_basis_row": basis, "power_of_z": power}
    return {
        "R806_polynomial_multiplier": c806["polynomial_multiplier"],
        "R806_cyclic_witness": interface["actual_cyclic_witness"],
        "R806_exact_coordinate_groups": interface["coordinate_groups"],
        "R806_original_free_basis": interface["original_R805_free_basis"],
        "R813_exact_coordinate_stage": coordinate_spec, "R813_normal_vector_interface": normal_spec,
        "original_input_columns": ["g", "h"], "actual_operator_targets": ["g", "Gamma"],
        "old_Fourier_Wronskian_or_S3_rows_selected_for_recomputation": False}




def shared_cache_identity(producers):
    r806 = producers["R806"]
    interface = r806.indexed(r806.certificate["polynomial_multiplier"])
    return {
        "R806_producer": identity(r806.item),
        "R806_polynomial_multiplier": r806.certificate["polynomial_multiplier"],
        "R806_cyclic_witness": interface["actual_cyclic_witness"],
        "original_R805_free_basis": interface["original_R805_free_basis"],
        "original_R805_S_basis_index": interface["original_R805_S_basis_index"],
        "normal_affine_basis_rank": 272, "normal_basis_degrees": EPS,
        "coordinate_convention": "column input, row output; e0 is original unit",
        "coefficient_field": "Q"}




def old_expected_configuration(item, producers):
    r806 = producers["R806"]
    interface = r806.indexed(r806.certificate["polynomial_multiplier"])
    return {
        "result": RESULT, "source_sha256": item["core_sha256"], "python_flint": "0.9.0",
        "R813_proof_sha256": item["R813_proof_sha256"], "R817_proof_sha256": item["R817_proof_sha256"],
        "R815_method_sha256": item["R815_method_sha256"],
        "framework_sha256": item["framework_sha256"], "p": 41,
        "normal_affine_basis_rank": 272, "normal_basis_degrees": EPS,
        "coefficient_field_basis": FIELD_BASIS,
        "R806_producer": identity(r806.item),
        "R806_polynomial_multiplier": r806.certificate["polynomial_multiplier"],
        "R806_cyclic_witness": interface["actual_cyclic_witness"],
        "original_R805_free_basis": interface["original_R805_free_basis"],
        "actual_sigma_integer_n": r806.tag["actual_sigma_integer_n"],
        "shared_point_mathematical_identity": shared_cache_identity(producers),
        "matrix_convention": "output row b, input column a",
        "auxiliary_prime_start": item["auxiliary_prime_start"],
        "matrix_row_block_size": item["matrix_row_block_size"],
        "reconstruct_every_primes": item["reconstruct_every_primes"],
        "point_search": "original successful z0 first; then distinct nonnegative residues",
        "exact_identity_mode": item["exact_identity_mode"],
        "no_characteristic_zero_Krylov_matrix_or_inverse": True,
        "R813_targets_budget_and_transport_artifacts_excluded_from_shared_basis_identity": True}




def expected_target_configurations(tag, producers):
    r813 = producers["R813"]
    coordinate_spec = r813.certificate["exact_coordinate_stage"]
    coordinates = r813.indexed(coordinate_spec)
    common = {
        "basis_configuration_sha256": fingerprint(tag),
        "R813_producer": identity(r813.item),
        "source_R813_exact_coordinates": coordinate_spec,
        "source_R813_normal_interface": r813.certificate["normal_vector_interface"],
        "coefficient_field_basis": FIELD_BASIS,
        "original_D0_qY_multiplier": ["1", "82"]}
    answer = {}
    for column, target in enumerate(("g", "h")):
        answer[target] = dict(common, target=target, source_R813_column=column,
            operator_kind="multiplication" if target == "g" else "original_vector_only",
            regular_degree_bound=3, polynomial_maximum_degree=5,
            original_rational_scale=coordinates["original_target_rational_scales"][column])
    answer["Gamma"] = dict(common, target="Gamma", operator_kind="normal_derivation_connection",
        weighted_degree_shift=2, polynomial_maximum_degree=4, first_column_constraint="Gamma*e0=0",
        defining_identity="[Gamma*Mw-Mw*Gamma+Mg*dMw/dz,Mw]=0; H*e0=v_h",
        independent_Mh_reconstruction=False,
        right_hand_side_multiplication_order="Mg on the left of dMw/dz")
    return answer





def load_io(item):
    global IO
    path = S/item["io_helper"]
    assert sha(path) == item["io_helper_sha256"] == IO_HELPER_SHA
    module_spec = importlib.util.spec_from_file_location("R815_projective_frozen_IO", path)
    IO = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(IO)


def source_identity(value):
    return {key: str(value[key]) for key in BASE}


def same_source(left, right):
    assert source_identity(left) == source_identity(right)


class EndedSource:
    """One real failed R815 producer, with all selected bytes kept under its own tag."""
    def __init__(self, item, directory, archive=None):
        self.item, self.directory, self.archive = item, Path(directory), archive
        self.directory.mkdir(parents=True, exist_ok=True)
        self.selected = {}
        assert item["result"] == RESULT and item["core_sha256"] == LEGACY_CORE_SHA
        assert item["expected_conclusion"] == "failure"
        assert str(item["run_id"]) == "43719622321"
        assert item["source_commit"] == "2a3300a9edec73c23e72f23127a0ae7d8222d13e"
        manifest_path = self.materialize("full-outputs-manifest.json",
                                         item["manifest_sha256"], item["manifest_bytes"])
        self.manifest = read(manifest_path)
        assert self.manifest["result"] == RESULT
        self.files = {entry["file"]: plain(entry) for entry in self.manifest["files"]}
        assert len(self.files) == len(self.manifest["files"]) == item["manifest_file_count"]
        for entry in self.files.values():
            check_spec(entry)
        self.files["full-outputs-manifest.json"] = file_spec(manifest_path)
        for key in ("current", "latest_CRT_receipt", "input_bundle"):
            entry = item[key]
            check_spec(entry)
            assert self.files[entry["file"]] == plain(entry)
        assert item["current"]["file"] == OLD_CURRENT
        assert item["latest_CRT_receipt"]["file"] == OLD_LAST_RECEIPT
        assert item["input_bundle"]["file"] == INPUT_BUNDLE
        run, core, initial = (self.raw(name) for name in META[1:])
        assert run["result"] == core["result"] == initial["result"] == RESULT
        assert run["complete"] is False and core["complete"] is False
        assert run["process_exit_code"] in item.get("accepted_checkpoint_exit_codes", [1])
        assert core["error"].startswith("BudgetStop:")
        assert str(run["workflow_run_id"]) == str(item["run_id"])
        assert run["source_commit"] == initial["source_commit"] == item["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == core["source_sha256"] == LEGACY_CORE_SHA
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        self.initial, self.old_job = initial, initial["job"]
        self.input_receipt = self.raw("retained-inputs-receipt.json")
        assert self.input_receipt["result"] == RESULT
        assert plain(self.input_receipt["input_bundle"]) == plain(item["input_bundle"])
        assert self.input_receipt["actual_selected_file_count"] == 53
        assert self.input_receipt["all_selected_bundle_members_individually_size_and_sha256_verified"] is True
        self.latest_receipt = self.raw(OLD_LAST_RECEIPT)
        self.tag = self.latest_receipt["configuration"]
        assert self.tag["result"] == RESULT and self.tag["source_sha256"] == LEGACY_CORE_SHA
        assert self.tag["python_flint"] == "0.9.0"
        assert self.latest_receipt["complete"] is True
        assert self.latest_receipt["target"] == "g"
        assert self.latest_receipt["field_component"] == 0
        assert self.latest_receipt["prime_count"] == 425
        assert plain(self.latest_receipt["current_full_CRT_checkpoint"]) == plain(item["current"])
        self.names = set(META) | {"retained-inputs-receipt.json", OLD_CURRENT, OLD_W,
                                 OLD_VECTOR["g"], OLD_VECTOR["h"]}
        steps, points = [], []
        for name in self.files:
            match = STEP_PATTERN.fullmatch(name)
            if match:
                steps.append((int(match.group(1)), name))
            if POINT_PATTERN.fullmatch(name):
                points.append(name)
        assert [number for number, _ in sorted(steps)] == list(range(1, 426))
        assert points, "The original completed Krylov cache is required."
        self.names.update(name for _, name in steps)
        self.names.update(points)
        self.point_names = sorted(points)
        self.step_names = [name for _, name in sorted(steps)]
        assert OLD_LAST_RECEIPT in self.names
        if "files" in item:
            assert item["files"] == {name: self.files[name] for name in sorted(self.names)}

    def materialize(self, name, digest, count=None):
        check_spec({"file": name, "bytes": 0 if count is None else count, "sha256": digest})
        path = self.directory/name
        if self.archive is not None:
            self.archive.extract_bound(name, digest, path, count)
        else:
            assert path.is_file() and sha(path) == digest, ("Missing unchanged source file", name)
            if count is not None:
                assert path.stat().st_size == count
        self.selected[name] = path
        return path

    def bound(self, name):
        entry = self.files[name]
        return self.materialize(name, entry["sha256"], entry["bytes"])

    def raw(self, name):
        return read(self.bound(name))

    def prefetch(self):
        if self.archive is not None:
            self.archive.extract_many([(name, self.files[name]["sha256"],
                                        self.directory/name, self.files[name]["bytes"])
                                       for name in sorted(self.names)])
        for name in sorted(self.names):
            self.bound(name)

    def stage(self, entry, target=None):
        assert entry["file"] in self.names
        assert plain(entry) == self.files[entry["file"]]
        assert entry["file"] != OLD_CURRENT, "The IO runner does not parse the large CRT vector."
        data = self.raw(entry["file"])
        assert data["complete"] is True and data["configuration"] == self.tag
        if target is not None:
            assert data["target"] == target
        return data

    def validate(self, item, producers):
        old_job = self.old_job
        for key in ("result", "p", "framework_sha256", "R813_proof_sha256", "R817_proof_sha256",
                    "R815_method_sha256", "requested_stage", "requested_targets",
                    "auxiliary_prime_start", "matrix_row_block_size", "reconstruct_every_primes",
                    "exact_identity_mode"):
            assert old_job[key] == item[key], ("Changed original 425-prime mathematical source", key)
        for label in LABELS:
            same_identity(old_job["retained_artifacts"][label], item["retained_artifacts"][label])
            assert self.input_receipt["producer_identities"][label] == identity(producers[label].item)
        assert self.tag == old_expected_configuration(old_job, producers)
        old_targets = expected_target_configurations(self.tag, producers)
        self.old_targets = old_targets
        cache = shared_cache_identity(producers)
        for name in self.step_names:
            data = self.stage(self.files[name], "g")
            assert data["target_configuration"] == old_targets["g"]
            assert data["target_configuration_sha256"] == fingerprint(old_targets["g"])
            number = int(STEP_PATTERN.fullmatch(name).group(1))
            assert data["prime_count"] == number
            assert data["large_vector_or_matrix_embedded"] is False
            assert data["full_temporary_images_discarded_only_after_CRT_commit"] is True
        for name in self.point_names:
            data = self.stage(self.files[name])
            assert data["shared_point_mathematical_identity"] == cache
            assert data["source_bound_external_cache_consumption_allowed"] is True
            assert data["external_consumer_must_preserve_original_R815_stage_identity"] is True
            match = POINT_PATTERN.fullmatch(name)
            assert int(data["prime"]) == int(match.group(1))
            assert int(data["z0"]) == int(match.group(2))
            assert data["usable"] is bool(data["actual_determinant_mod_prime"])
            if data["usable"]:
                assert data["both_inverse_products_verified"] is True
                assert data["actual_cyclic_rank"] == 272
                for key in ("W_evaluated_mod_prime", "inverse_Krylov_matrix_mod_prime"):
                    assert len(data[key]) == 272 and all(len(row) == 272 for row in data[key])
            else:
                assert data["failure_means_only_this_modular_specialization"] is True
        self.stage(self.files[OLD_W])
        for target in ("g", "h"):
            data = self.stage(self.files[OLD_VECTOR[target]], target)
            assert data["target_configuration"] == old_targets[target]
            assert data["target_configuration_sha256"] == fingerprint(old_targets[target])
            assert data["original_rational_scale_applied_exactly_once"] is True
            assert data["no_extra_82_power_or_removed_content_reinserted"] is True
        return {"producer": source_identity(self.item),
                "original_configuration_sha256": fingerprint(self.tag),
                "current": plain(self.item["current"]),
                "latest_CRT_receipt": plain(self.item["latest_CRT_receipt"]),
                "actual_completed_CRT_prime_count": 425,
                "actual_retained_CRT_receipt_count": len(self.step_names),
                "actual_retained_shared_Krylov_point_count": len(self.point_names),
                "original_W_and_g_h_vectors_preserved": True,
                "large_CRT_vector_decoded_or_new_arithmetic_run_by_IO": False,
                "files": [self.files[name] for name in sorted(self.names)]}

    def expanded_spec(self):
        value = dict(self.item)
        value["files"] = {name: self.files[name] for name in sorted(self.names)}
        return value


def bundle_members(bundle, root=None, labels=ALL_LABELS):
    seen = set()
    with tarfile.open(bundle, "r|gz") as archive:
        for member in archive:
            path = PurePosixPath(member.name)
            assert member.isfile() and len(path.parts) == 2 and path.parts[0] in labels
            assert ".." not in path.parts and not path.is_absolute() and "\\" not in member.name
            assert member.name not in seen
            seen.add(member.name)
            digest, total = hashlib.sha256(), 0
            target = None if root is None else Path(root)/path.parts[0]/path.parts[1]
            temporary = None if target is None else target.with_name(target.name+".transfer")
            if temporary is not None:
                temporary.parent.mkdir(parents=True, exist_ok=True)
            source = archive.extractfile(member)
            destination = open(temporary, "wb") if temporary is not None else None
            try:
                for block in iter(lambda: source.read(4*1024*1024), b""):
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


def selected_files(producers, original):
    answer = {label+"/"+name: file_spec(path)
              for label, producer in producers.items()
              for name, path in producer.selected.items()}
    answer.update({"R815/"+name: file_spec(original.directory/name) for name in sorted(original.names)})
    return answer


def verify_bundle(bundle, producers, original):
    actual, expected = dict(bundle_members(bundle)), selected_files(producers, original)
    assert actual == expected
    return len(actual)


def check_directory_closure(root, producers, original):
    expected = {label: set(producer.selected) for label, producer in producers.items()}
    expected["R815"] = set(original.names)
    for label in ALL_LABELS:
        actual = {path.name for path in (root/label).iterdir() if path.is_file()}
        assert actual == expected[label], ("Unbound selected source file", label, sorted(actual ^ expected[label]))


def expanded_job(item, original):
    answer = json.loads(json.dumps(item))
    answer["projective_source"] = original.expanded_spec()
    return answer



def previous_scan_identity(item):
    source = item["previous_projective_scan"]
    return {
        **{key: str(source[key]) for key in BASE},
        "configuration_sha256": source["configuration_sha256"],
        "scan": plain(source["scan"]),
        "probe_pairs": [plain(x) for x in source["probe_pairs"]],
        "source_audit": plain(source["source_audit"]),
        "certificate": plain(source["certificate"]),
    }


def review_previous_scan(item, root):
    source = item["previous_projective_scan"]
    folder = root/PREVIOUS_SCAN_GROUP
    assert str(source["run_id"]) == "43751142120"
    assert source["source_commit"] == "5abcb9ccfba85d6a708b1df94e6383ff549f72a7"
    assert source["core_sha256"] == "126469e2e7c8377c484a9e0844db463fe93e6c90b2971233a11de556a49d9ddb"
    assert source["wrapper_sha256"] == "3a0fa603b4b76a801a26b106a35eaa3e1ddc2a69a77b97078d08545e5bc27a57"
    assert set(path.name for path in folder.iterdir() if path.is_file()) == set(source["files"])
    for name, entry in source["files"].items():
        assert plain(entry)["file"] == name and file_spec(folder/name) == plain(entry)
    manifest = read(folder/"full-outputs-manifest.json")
    assert manifest["result"] == RESULT
    files = {entry["file"]: plain(entry) for entry in manifest["files"]}
    assert len(files) == len(manifest["files"])
    assert source["files"]["full-outputs-manifest.json"]["sha256"] == source["manifest_sha256"]
    for name, entry in source["files"].items():
        if name != "full-outputs-manifest.json":
            assert plain(entry) == files[name]
    assert plain(source["input_bundle"]) == files[INPUT_BUNDLE]
    initial, run, core = (read(folder/name) for name in
                          ("public-actions-input.json", "run-receipt.json", "core-receipt.json"))
    assert initial["result"] == run["result"] == core["result"] == RESULT
    assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
    assert str(run["workflow_run_id"]) == str(source["run_id"])
    assert initial["core_sha256"] == core["source_sha256"] == source["core_sha256"]
    assert initial["job"]["core_sha256"] == source["core_sha256"]
    assert initial["driver_sha256"] == source["wrapper_sha256"]
    assert run["complete"] is core["complete"] is False and run["process_exit_code"] == 2
    assert run["error"] is None
    assert run["core_receipt_sha256"] == files["core-receipt.json"]["sha256"]
    assert core["certificate_sha256"] == source["certificate"]["sha256"]
    final = read(folder/source["certificate"]["file"])
    tag = final["configuration"]
    assert final["result"] == RESULT and final["complete"] is False
    assert tag == initial["actual_projective_configuration"]
    assert fingerprint(tag) == source["configuration_sha256"]
    assert tag["projective_mode"] == "known-first-column-and-three-dimensional-Q-common-denominator"
    assert tag["source_sha256"] == source["core_sha256"]
    assert tag["source_original_425_current"] == plain(item["projective_source"]["current"])
    assert tag["source_original_425_receipt"] == plain(item["projective_source"]["latest_CRT_receipt"])
    assert source_identity(initial["job"]["projective_source"]) == source_identity(item["projective_source"])
    assert initial["job"]["retained_artifacts"] == item["retained_artifacts"]
    inventory = read(folder/source["stage_manifest"]["file"])
    assert inventory["configuration"] == tag and inventory["complete"] is True
    indexed = {entry["file"]: plain(entry) for entry in inventory["files"]+inventory["current_checkpoints"]}
    for entry in [source["scan"], source["source_audit"]]+source["probe_pairs"]:
        assert indexed[entry["file"]] == plain(entry) == files[entry["file"]]
        value = read(folder/entry["file"])
        assert value["configuration"] == tag
        assert value["source_original_current"] == plain(item["projective_source"]["current"])
        assert value["complete"] is (entry["file"] != source["scan"]["file"])
    scan = read(folder/source["scan"]["file"])
    assert scan["next_coefficient_index"] == 21 and scan["completed_pair_count"] == 4
    assert scan["scalar_RR_failure_count"] == 8 and scan["unpaired_failure"] is None
    assert scan["scan_finished"] is False
    return {"source": previous_scan_identity(item), "file_count": len(source["files"]),
            "files": [plain(source["files"][name]) for name in sorted(source["files"])],
            "old_scalar_RR_or_lattice_arithmetic_recomputed": False}


def restore_previous_scan_bundle(item, out, root):
    bundle = out/PREVIOUS_SCAN_BUNDLE
    assert bundle.is_file()
    expected = {PREVIOUS_SCAN_GROUP+"/"+name: plain(entry)
                for name, entry in item["previous_projective_scan"]["files"].items()}
    actual = dict(bundle_members(bundle, root, (PREVIOUS_SCAN_GROUP,)))
    assert actual == expected
    return review_previous_scan(item, root)


def prepare_previous_scan(item, out):
    source = item["previous_projective_scan"]
    root = out.parent/"retained"
    small = out/PREVIOUS_SCAN_BUNDLE
    archive = None
    parent_carrier_imported = False
    try:
        if small.exists():
            review = restore_previous_scan_bundle(item, out, root)
        else:
            archive = IO.Archive(source, out.parent/"download-previous-projective-scan", whole=False)
            manifest_entry = plain(source["files"]["full-outputs-manifest.json"])
            archive.extract_bound(manifest_entry["file"], manifest_entry["sha256"],
                                  root/PREVIOUS_SCAN_GROUP/manifest_entry["file"], manifest_entry["bytes"])
            manifest = read(root/PREVIOUS_SCAN_GROUP/"full-outputs-manifest.json")
            files = {entry["file"]: plain(entry) for entry in manifest["files"]}
            assert len(files) == len(manifest["files"])
            for name, entry in source["files"].items():
                if name != "full-outputs-manifest.json":
                    assert plain(entry) == files[name]
            archive.extract_many([(name, entry["sha256"], root/PREVIOUS_SCAN_GROUP/name, entry["bytes"])
                                  for name, entry in source["files"].items()])
            review = review_previous_scan(item, root)
            with tarfile.open(small.with_name(small.name+".tmp"), "w:gz") as carrier:
                for name in sorted(source["files"]):
                    carrier.add(root/PREVIOUS_SCAN_GROUP/name,
                                arcname=PREVIOUS_SCAN_GROUP+"/"+name, recursive=False)
            small.with_name(small.name+".tmp").replace(small)
        present = [(root/label/"full-outputs-manifest.json").exists() for label in ALL_LABELS]
        assert all(present) or not any(present)
        if not any(present):
            if archive is None:
                archive = IO.Archive(source, out.parent/"download-previous-projective-scan", whole=False)
            entry = plain(source["input_bundle"])
            archive.extract_bound(entry["file"], entry["sha256"], out/INPUT_BUNDLE, entry["bytes"])
            actual = dict(bundle_members(out/INPUT_BUNDLE, root))
            assert len(actual) == source["selected_original_member_count"] == 3037
            parent_carrier_imported = True
            # prepare_inputs immediately validates every extracted original source SHA,
            # its old configuration and the exact three-group closure. No retagging.
        save(out/"R815-two-columns-previous-scan-input-receipt.json", {
            "result": RESULT, "projective_mode": PROJECTIVE_MODE,
            "source_review": review, "input_bundle": file_spec(small),
            "source_original_three_group_carrier": plain(source["input_bundle"]),
            "parent_original_carrier_imported_without_repacking": parent_carrier_imported,
            "full_parent_ZIP_rehashed_in_this_range_transfer": False,
            "transport": None if archive is None else archive.receipt(),
            "new_mathematical_arithmetic_performed": False,
        })
        return review
    finally:
        if archive is not None:
            archive.close()



def prepare_inputs(item, out):
    root = out.parent/"retained"
    present = [(root/label/"full-outputs-manifest.json").exists() for label in ALL_LABELS]
    assert all(present) or not any(present), "Partial source restoration is not accepted."
    archive = None
    transport, extracted_carrier = None, None
    if not all(present):
        archive = IO.Archive(item["projective_source"], out.parent/"download-original-425", whole=False)
    try:
        original = EndedSource(item["projective_source"], root/"R815", archive)
        if archive is not None:
            carrier_spec = item["projective_source"]["input_bundle"]
            extracted_carrier = archive.extract_bound(
                carrier_spec["file"], carrier_spec["sha256"],
                out.parent/"original-53-inputs.tar.gz", carrier_spec["bytes"])
            original_members = dict(bundle_members(extracted_carrier, root, LABELS))
            assert len(original_members) == 53
        producers = {label: Producer(label, item["retained_artifacts"][label], root/label) for label in LABELS}
        selection = select_inputs(producers)
        actual_original = {label+"/"+name: file_spec(path)
                           for label, producer in producers.items()
                           for name, path in producer.selected.items()}
        assert len(actual_original) == 53
        assert {label: len(producer.selected) for label, producer in producers.items()} == {"R806": 45, "R813": 8}
        old_receipt_files = {label+"/"+entry["file"]: plain(entry)
                            for label, values in original.input_receipt["selected_files"].items()
                            for entry in values}
        assert actual_original == old_receipt_files
        if extracted_carrier is not None:
            assert original_members == actual_original
        assert original.input_receipt["selection"] == selection
        original.prefetch()
        source_review = original.validate(item, producers)
        check_directory_closure(root, producers, original)
        expanded = expanded_job(item, original)
        bundle = out/INPUT_BUNDLE
        if not bundle.exists():
            temporary = bundle.with_name(bundle.name+".tmp")
            with tarfile.open(temporary, "w:gz") as tar:
                for label, producer in sorted(producers.items()):
                    for name in sorted(producer.selected):
                        tar.add(producer.selected[name], arcname=label+"/"+name, recursive=False)
                for name in sorted(original.names):
                    tar.add(original.directory/name, arcname="R815/"+name, recursive=False)
            temporary.replace(bundle)
        count = verify_bundle(bundle, producers, original)
        if archive is not None:
            transport = archive.receipt()
        save(out/"retained-inputs-receipt.json", {
            "result": RESULT, "projective_mode": PROJECTIVE_MODE,
            "producer_identities": {label: identity(producers[label].item) for label in LABELS},
            "projective_source_identity": source_identity(original.item),
            "selection": selection, "original_425_source_review": source_review,
            "selected_files": {label: [file_spec(path) for _, path in sorted(producers[label].selected.items())]
                               for label in LABELS},
            "selected_original_R815_files": source_review["files"],
            "input_bundle": file_spec(bundle), "actual_selected_file_count": count,
            "original_53_carrier": plain(item["projective_source"]["input_bundle"]),
            "all_selected_bundle_members_individually_size_and_sha256_verified": True,
            "transport_artifact": transport,
            "restored_original_input_bundle_reused": all(present),
            "old_completed_arithmetic_recomputed": False,
            "all_original_425_modular_images_or_old_large_CRT_states_selected": False,
        })
        save(out/"public-actions-expanded-job.json", expanded)
        return root, producers, original, selection, expanded
    finally:
        if archive is not None:
            archive.close()
        if extracted_carrier is not None and extracted_carrier.exists():
            extracted_carrier.unlink()


def expected_configuration(item, producers, original):
    tag = old_expected_configuration(item, producers)
    tag.update({
        "projective_mode": PROJECTIVE_MODE,
        "projective_method_sha256": item["projective_method_sha256"],
        "legacy_R815_core_sha256": item["legacy_core_sha256"],
        "projective_source_identity": source_identity(original.item),
        "source_original_425_configuration_sha256": fingerprint(original.tag),
        "source_original_425_current": plain(original.item["current"]),
        "source_original_425_receipt": plain(original.item["latest_CRT_receipt"]),
        "projective_search_strategy": PROJECTIVE_STRATEGY,
        "original_425_Mg_prime_arithmetic_recomputed": False,
        "previous_projective_scalar_scan_source": previous_scan_identity(item),
        "two_exact_original_columns_identity": "Mg e0=vg; We0=e1; Mg e1=Wvg",
        "only_budget_and_probe_pair_limit_excluded_from_mathematical_identity": True,
    })
    return tag




def stable_job(item):
    value = json.loads(json.dumps(item))
    for key in ("resume", "budget_minutes", "projective_controls"):
        value.pop(key, None)
    if "projective_source" in value:
        value["projective_source"].pop("files", None)
    return value


def stable_expanded(item):
    value = json.loads(json.dumps(item))
    for key in ("resume", "budget_minutes", "projective_controls"):
        value.pop(key, None)
    return value


def restore_resume(item, out):
    previous = item.get("resume")
    if previous is None:
        return
    assert previous["core_sha256"] == item["core_sha256"]
    assert previous["result"] == RESULT
    archive = IO.Archive(previous, out.parent/"download-projective-continuation", whole=True)
    try:
        path = archive.extract_bound("full-outputs-manifest.json", previous["manifest_sha256"],
                                     out.parent/"previous-full-outputs-manifest.json")
        manifest = read(path)
        assert manifest["result"] == RESULT
        entries = archive.verify_all(manifest)

        def bound(name, destination=None):
            row = entries[name]
            return archive.extract_bound(name, row["sha256"],
                destination or out.parent/"previous-metadata"/name, row["bytes"])

        initial, run = read(bound("public-actions-input.json")), read(bound("run-receipt.json"))
        core = read(bound("core-receipt.json")) if "core-receipt.json" in entries else None
        assert initial["result"] == run["result"] == RESULT
        if core is not None:
            assert core["result"] == RESULT and core["source_sha256"] == item["core_sha256"]
            assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
        else:
            assert run["core_receipt_sha256"] is None
            assert run["complete"] is False and run["process_exit_code"] != 0
        assert initial["source_commit"] == run["source_commit"] == previous["source_commit"]
        assert str(run["workflow_run_id"]) == str(previous["run_id"])
        assert initial["core_sha256"] == item["core_sha256"]
        assert initial["driver_sha256"] == item["wrapper_sha256"]
        assert stable_job(initial["job"]) == stable_job(item)
        bundle = bound(INPUT_BUNDLE, out/INPUT_BUNDLE)
        bound(PREVIOUS_SCAN_BUNDLE, out/PREVIOUS_SCAN_BUNDLE)
        root = out.parent/"retained"
        restore_previous_scan_bundle(item, out, root)
        actual_bundle = dict(bundle_members(bundle, root))
        assert actual_bundle
        producers = {label: Producer(label, item["retained_artifacts"][label], root/label) for label in LABELS}
        select_inputs(producers)
        original = EndedSource(item["projective_source"], root/"R815")
        original.prefetch()
        original.validate(item, producers)
        check_directory_closure(root, producers, original)
        assert actual_bundle == selected_files(producers, original)
        expanded = expanded_job(item, original)
        old_expanded = read(bound("public-actions-expanded-job.json"))
        assert stable_expanded(old_expanded) == stable_expanded(expanded)
        assert initial["expanded_job_sha256"] == entries["public-actions-expanded-job.json"]["sha256"]
        tag = expected_configuration(item, producers, original)
        targets = expected_target_configurations(tag, producers)
        copied, checkpoint_names = 0, []
        for name, entry in entries.items():
            if name != FINAL and not (name.startswith("R815-") and name.endswith(".json.gz")):
                continue
            if name == FINAL:
                candidate = read(bound(name))
                assert candidate["configuration"] == tag and candidate["result"] == RESULT
                if candidate.get("complete") is not True:
                    continue  # Honest failed search metadata stays in the source archive.
            destination = bound(name, out/name)
            if name.endswith("-CRT-current.json.gz"):
                # The original small receipt and unchanged full-core identity bind this
                # very large byte object; the mathematical core validates its contents.
                checkpoint_names.append(name)
            else:
                data = read(destination)
                assert data["configuration"] == tag
                if "target_configuration" in data:
                    target = data["target"]
                    assert data["target_configuration"] == targets[target]
                    assert data["target_configuration_sha256"] == fingerprint(targets[target])
                if data.get("complete") is False:
                    checkpoint_names.append(name)
                else:
                    assert data.get("complete") is True
            copied += 1
        save(out/"resume-receipt.json", {
            "result": RESULT, "projective_mode": PROJECTIVE_MODE,
            "previous_actual_artifact": previous, "actual_archive_review": archive.receipt(),
            "all_original_manifest_members_streamed_and_sha256_verified": True,
            "actual_previous_manifest_file_count": len(entries),
            "complete_and_current_stage_files_restored": copied,
            "restored_incomplete_checkpoint_files": checkpoint_names,
            "all_original_selected_bundle_members_verified": len(actual_bundle),
            "input_bundle": file_spec(bundle),
            "same_new_projective_core_and_all_original_sources_preserved": True,
            "original_425_Mg_prime_arithmetic_recomputed": False,
            "no_completed_candidate_or_Gamma_CRT_step_recomputed": True,
        })
    finally:
        archive.close()
        downloaded = out.parent/"download-projective-continuation"/"artifact.zip"
        if downloaded.exists():
            downloaded.unlink()


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core, proof, method = S/item["core"], topic_path(item["proof"]), topic_path(item["method"])
    nested_proof, framework = topic_path(item["nested_proof"]), S/item["framework"]
    projective_method, legacy = topic_path(item["projective_method"]), S/item["legacy_core"]
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    initial = {
        "result": RESULT, "p": 41, "source_repository": "Rogerhu12/math-research-public",
        "source_commit": source, "job": item, "core_sha256": sha(core),
        "proof_sha256": sha(proof), "nested_proof_sha256": sha(nested_proof),
        "method_sha256": sha(method), "framework_sha256": sha(framework),
        "legacy_core_sha256": sha(legacy), "projective_method_sha256": sha(projective_method),
        "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "io_helper_sha256": sha(S/item["io_helper"]),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "workflow_sha256": sha(REPO/item["workflow"]),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "projective_mode": PROJECTIVE_MODE,
        "new_arithmetic": "new exact Wvg/d01 and two-column denominator candidates; same 425 source; exact Mg; original Gamma",
        "original_425_Mg_prime_arithmetic_recomputed": False,
        "independent_Mh_reconstruction": False,
        "polar_preimages_function_DAG_eta_or_height_claimed": False,
    }
    save(out/"public-actions-input.json", initial)
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert item["producer_inputs_pending"] is False
        assert item["requested_stage"] == "original_normal_derivation_operators"
        assert item["requested_targets"] == ["g", "Gamma"]
        assert set(item["retained_artifacts"]) == set(LABELS)
        assert set(item["projective_controls"]) == {"maximum_probe_pairs"}
        assert isinstance(item["projective_controls"]["maximum_probe_pairs"], int)
        assert item["projective_controls"]["maximum_probe_pairs"] > 0
        assert sha(core) == item["core_sha256"] and sha(__file__) == item["wrapper_sha256"]
        assert sha(proof) == item["R813_proof_sha256"] and sha(method) == item["R815_method_sha256"]
        assert sha(nested_proof) == item["R817_proof_sha256"]
        assert sha(projective_method) == item["projective_method_sha256"]
        assert sha(legacy) == item["legacy_core_sha256"] == LEGACY_CORE_SHA
        assert sha(framework) == item["framework_sha256"] == "849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3"
        load_io(item)
        restore_resume(item, out)
        prepare_previous_scan(item, out)
        retained, producers, original, _, expanded = prepare_inputs(item, out)
        initial["expanded_job_sha256"] = sha(out/"public-actions-expanded-job.json")
        initial["actual_original_425_configuration_sha256"] = fingerprint(original.tag)
        initial["actual_projective_configuration"] = expected_configuration(item, producers, original)
        save(out/"public-actions-input.json", initial)
        config = out.parent/"job-config.json"
        save(config, expanded)
        command = [sys.executable, "-u", str(core), "--config", str(config),
            "--proof", str(proof), "--nested-proof", str(nested_proof),
            "--method", str(method), "--projective-method", str(projective_method),
            "--retained", str(retained), "--output", str(out),
            "--budget-minutes", str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60+120)
            except subprocess.TimeoutExpired:
                error = "Budget reached; completed candidate stages and latest Gamma CRT states retained."
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
        "projective_mode": PROJECTIVE_MODE,
        "actual_original_Mg_and_Gamma_computed": complete,
        "original_425_Mg_prime_arithmetic_recomputed": False,
        "independent_Mh_reconstructed_or_stored": False,
        "base_polar_preimages_computed": False, "eta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
    })
    output_manifest(out)
    print(json.dumps({"result": RESULT, "projective_mode": PROJECTIVE_MODE,
                      "complete": complete, "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)




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




def verify(item, out):
    """Only IO, exact source bindings and certificate structure; never imports a math core."""
    initial = read(out/"public-actions-input.json")
    run, core = read(out/"run-receipt.json"), read(out/"core-receipt.json")
    assert initial["job"] == item
    assert initial["result"] == run["result"] == core["result"] == RESULT
    assert initial["core_sha256"] == core["source_sha256"] == item["core_sha256"]
    assert initial["driver_sha256"] == item["wrapper_sha256"]
    assert initial["proof_sha256"] == item["R813_proof_sha256"]
    assert initial["nested_proof_sha256"] == item["R817_proof_sha256"]
    assert initial["framework_sha256"] == core["framework_sha256"] == item["framework_sha256"]
    assert initial["method_sha256"] == item["R815_method_sha256"]
    assert run["source_commit"] == initial["source_commit"]
    assert run["complete"] is True and run["process_exit_code"] == 0
    assert run["core_receipt_sha256"] == sha(out/"core-receipt.json")
    assert core["complete"] is True and core["certificate_sha256"] == sha(out/FINAL)
    for key in ("original_Mg_computed", "original_normal_derivation_connection_computed",
                "all_complete_polynomial_defining_identities_verified"):
        assert core[key] is True
    for key in ("independent_Mh_reconstructed_or_stored", "original_cusp_zero_ideal_computed",
                "original_function_DAG_polar_divisors_eta_or_height_computed"):
        assert core[key] is False
    assert initial["projective_mode"] == PROJECTIVE_MODE
    assert initial["legacy_core_sha256"] == item["legacy_core_sha256"] == LEGACY_CORE_SHA
    assert initial["projective_method_sha256"] == item["projective_method_sha256"]
    assert initial["io_helper_sha256"] == item["io_helper_sha256"] == IO_HELPER_SHA
    root = out.parent/"retained"
    restore_previous_scan_bundle(item, out, root)
    review_previous_scan(item, root)
    if not all((root/label/"full-outputs-manifest.json").exists() for label in ALL_LABELS):
        assert dict(bundle_members(out/INPUT_BUNDLE, root))
    producers = {label: Producer(label, item["retained_artifacts"][label], root/label) for label in LABELS}
    selection = select_inputs(producers)
    original = EndedSource(item["projective_source"], root/"R815")
    original.prefetch()
    source_review = original.validate(item, producers)
    check_directory_closure(root, producers, original)
    count = verify_bundle(out/INPUT_BUNDLE, producers, original)
    retained_receipt = read(out/"retained-inputs-receipt.json")
    assert retained_receipt["selection"] == selection
    assert retained_receipt["original_425_source_review"] == source_review
    assert retained_receipt["actual_selected_file_count"] == count
    assert retained_receipt["all_selected_bundle_members_individually_size_and_sha256_verified"] is True
    assert retained_receipt["input_bundle"] == file_spec(out/INPUT_BUNDLE)
    assert retained_receipt["selected_original_R815_files"] == source_review["files"]
    expanded = read(out/"public-actions-expanded-job.json")
    assert expanded == expanded_job(item, original)
    assert initial["expanded_job_sha256"] == sha(out/"public-actions-expanded-job.json")
    tag = expected_configuration(item, producers, original)
    assert initial["actual_projective_configuration"] == tag
    assert initial["actual_original_425_configuration_sha256"] == fingerprint(original.tag)
    target_tags = expected_target_configurations(tag, producers)
    certificate = read(out/FINAL)
    assert certificate["result"] == RESULT and certificate["complete"] is True
    assert certificate["configuration"] == tag
    assert certificate["projective_mode"] == PROJECTIVE_MODE
    assert certificate["projective_method_sha256"] == item["projective_method_sha256"]
    assert certificate["legacy_R815_core_sha256"] == LEGACY_CORE_SHA
    assert certificate["source_original_425_identity"] == source_identity(original.item)
    assert certificate["source_original_current"] == plain(original.item["current"])
    assert certificate["source_original_latest_receipt"] == plain(original.item["latest_CRT_receipt"])
    assert certificate["original_425_prime_arithmetic_recomputed"] is False
    assert certificate["completed_original_scalar_scan_reused"] == previous_scan_identity(item)
    assert certificate["known_column_indices"] == [0, 1]
    assert certificate["known_column_coefficient_counts"] == [690, 962]
    previous_receipt = read(out/"R815-two-columns-previous-scan-input-receipt.json")
    assert previous_receipt["source_review"] == review_previous_scan(item, root)
    assert previous_receipt["input_bundle"] == file_spec(out/PREVIOUS_SCAN_BUNDLE)
    assert previous_receipt["new_mathematical_arithmetic_performed"] is False
    assert certificate["external_old_W_and_Krylov_stages_preserve_original_configuration"] is True
    assert certificate["completed_scope"] == "original_normal_derivation_operators"
    assert certificate["requested_targets"] == ["g", "Gamma"]
    assert certificate["target_configurations"] == target_tags
    assert certificate["normal_affine_basis_rank"] == 272 and certificate["normal_basis_degrees"] == EPS
    assert certificate["coefficient_field_basis"] == FIELD_BASIS
    assert certificate["actual_input_producers"] == {label: identity(producers[label].item) for label in LABELS}
    assert certificate["shared_point_mathematical_identity"] == shared_cache_identity(producers)
    assert certificate["source_R813_exact_coordinates"] == producers["R813"].certificate["exact_coordinate_stage"]
    assert certificate["source_R813_normal_interface"] == producers["R813"].certificate["normal_vector_interface"]
    for key in ("original_Mg_computed", "original_normal_derivation_connection_computed",
                "original_Mh_identified_by_nested_commutator_and_original_first_column",
                "all_weighted_supports_and_original_column_constraints_verified",
                "all_complete_polynomial_defining_identities_verified",
                "Gamma_nonhomogeneous_identity_with_actual_Mh_certified",
                "normal_integral_basis_preserved", "all_original_scalar_and_field_normalizations_preserved"):
        assert certificate[key] is True
    for key in ("independent_Mh_reconstructed_or_stored",
                "old_Fourier_Wronskian_S3_Dixon_or_primitive_results_recomputed",
                "characteristic_zero_Krylov_matrix_or_inverse_computed",
                "original_cusp_zero_ideal_computed",
                "original_function_DAG_polar_divisors_eta_or_height_computed"):
        assert certificate[key] is False
    assert certificate["Mg_exact_commutator_points"] == certificate["Gamma_exact_nested_commutator_points"] == list(range(7))
    manifest_spec = certificate["stage_manifest"]
    assert file_spec(out/manifest_spec["file"]) == manifest_spec
    inventory = read(out/manifest_spec["file"])
    assert inventory["configuration"] == tag and inventory["complete"] is True
    entries = {entry["file"]: entry for entry in inventory["files"]}
    assert len(entries) == len(inventory["files"])
    for name, entry in entries.items():
        check_spec(entry)
        assert file_spec(out/name) == entry
        value = read(out/name)
        assert value["configuration"] == tag and value["complete"] is True
        if "target_configuration" in value:
            target = value["target"]
            assert target in target_tags and value["target_configuration"] == target_tags[target]
            assert value["target_configuration_sha256"] == fingerprint(target_tags[target])
        if name.endswith("-Krylov-inverse.json.gz"):
            assert value["shared_point_mathematical_identity"] == certificate["shared_point_mathematical_identity"]
            assert value["external_consumer_must_preserve_original_R815_stage_identity"] is True
        for key in ("source_original_M_w", "source_original_primitive_matrix"):
            if key in value:
                assert plain(value[key]) == original.files[OLD_W]
        if "discarded_candidate_file_history" in value:
            assert value["no_exact_characteristic_zero_multiplier_claimed"] is True
            if value["target"] == "g":
                assert value["only_inactive_rejected_large_candidate_blocks_pruned"] is True
                assert value["original_source_current_or_Krylov_cache_deleted"] is False
                stem = value["candidate_id"]
                assert name == stem+"-rejected.json.gz" and stem.startswith("R815-projective-g-candidate-")
            else:
                assert value["target"] == "Gamma" and value["field_component"] == 0
                stem = "R815-target-Gamma-component-00-attempt-"+str(value["attempt_prime_count"]).zfill(6)
                assert name == stem+"-rejected.json.gz"
            for retired in value["discarded_candidate_file_history"]:
                check_spec(retired)
                assert retired["file"].startswith(stem+"-reconstructed-rows-") or (
                    value["target"] == "Gamma" and retired["file"] == stem+"-candidate-index.json.gz")
                if (out/retired["file"]).exists():
                    assert file_spec(out/retired["file"]) == plain(retired)
        if name.startswith("R815-projective-pair-") and name.endswith("-LLL.json.gz"):
            assert value["shift"] in SHIFTS
            assert value["source_original_current"] == plain(original.item["current"])
            assert value["full_basis_change_equality_verified"] is True
            assert value["exact_basis_change_determinant"] in (-1, 1)
            for key in ("actual_LLL_rows", "original_integer_lattice_rows", "exact_integral_basis_change"):
                assert len(value[key]) == 3 and all(len(row) == 3 for row in value[key])
            assert len(value["candidates"]) == 3
            assert value["LLL_is_only_candidate_generation"] is True
            assert value["M_power_two_thirds_success_or_height_guarantee_claimed"] is False
    checkpoint_specs = inventory.get("current_checkpoints", certificate.get("current_checkpoints", []))
    checkpoints = {entry["file"]: entry for entry in checkpoint_specs}
    assert len(checkpoints) == len(checkpoint_specs)
    for name, entry in checkpoints.items():
        check_spec(entry)
        assert name not in entries and name.startswith("R815-") and name.endswith(".json.gz")
        assert file_spec(out/name) == plain(entry)
        value = read(out/name)
        assert value["configuration"] == tag and value["complete"] is False
    expected_names = {path.name for path in out.glob("R815-*.json.gz")
                      if not path.name.startswith("R815-stage-manifest-")}
    assert set(entries) | set(checkpoints) == expected_names
    assert not list(out.glob("R815-*-CRT-current.json.gz"))
    assert not list(out.glob("R815-target-h-*-CRT-*.json.gz"))

    def referenced(entry, target=None, original_source=False):
        if original_source:
            assert entry["file"] in original.names
            assert plain(entry) == original.files[entry["file"]]
            data = original.stage(entry, target)
            if target is not None:
                assert data["target_configuration"] == original.old_targets[target]
            return data
        assert entries[entry["file"]] == plain(entry)
        data = read(out/entry["file"])
        if target is not None:
            assert data["target_configuration"] == target_tags[target]
        return data

    audit = referenced(certificate["original_425_source_audit"])
    assert audit["source_original_425_identity"] == source_identity(original.item)
    assert audit["source_original_configuration_sha256"] == fingerprint(original.tag)
    assert audit["source_original_current"] == plain(original.item["current"])
    assert audit["source_original_latest_receipt"] == plain(original.item["latest_CRT_receipt"])
    assert audit["coefficient_count"] == 295936 and audit["prime_count"] == 425
    assert audit["latest_prime"] == 1000008791 and audit["modulus_bits"] == 12707
    assert audit["all690_original_first_column_CRT_congruences_verified"] is True
    assert audit["source_original_425_prime_arithmetic_recomputed"] is False
    known_spec = plain(certificate["exact_two_known_columns_input"])
    known = referenced(known_spec, "g")
    assert known["source_original_g_vector"] == original.files[OLD_VECTOR["g"]]
    assert known["source_original_M_w"] == original.files[OLD_W]
    assert known["source_original_current"] == plain(original.item["current"])
    assert known["source_imported_previous_scalar_scan"] == previous_scan_identity(item)
    assert known["known_column_indices"] == [0, 1] and known["known_column_coefficient_counts"] == [690, 962]
    assert known["all1652_original_current_congruences_verified"] is True
    assert known["both_weighted_supports_verified_coefficientwise"] is True
    assert known["common_denominator_is_positive_and_jointly_reduced"] is True
    assert known["new_exact_multiplication_of_original_W_and_vg_actually_performed"] is True
    assert int(known["common_positive_denominator"]) > 0
    assert len(known["column_integer_numerators"]) == 2
    assert all(len(column) == 5 and all(len(row) == 272 for row in column)
               for column in known["column_integer_numerators"])
    assert audit["first690_congruences_imported_from_completed_source"] == plain(item["previous_projective_scan"]["source_audit"])
    assert audit["previous_first_column_audit_relabelled_or_recomputed"] is False
    row_ranges = [(first, min(first+16, 272)) for first in range(0, 272, 16)]
    assert certificate["original_vector_input_source_group"] == "R815"
    vector_specs = certificate["original_vector_inputs"]
    for column, target in enumerate(("g", "h")):
        assert plain(vector_specs[target]) == original.files[OLD_VECTOR[target]]
        vector = referenced(vector_specs[target], target, original_source=True)
        assert vector["source_R813_column_index"] == column
        assert vector["source_R813_exact_coordinates"] == certificate["source_R813_exact_coordinates"]
        assert vector["source_R813_normal_interface"] == certificate["source_R813_normal_interface"]
        assert vector["regular_degree_bound"] == 3 and vector["normal_affine_basis_rank"] == 272
        assert vector["original_rational_scale_applied_exactly_once"] is True
        assert vector["no_extra_82_power_or_removed_content_reinserted"] is True
        assert vector["original_D0_qY_multiplier"] == ["1", "82"]
        assert vector["exactly_zero_component"] is False
        assert len(vector["integer_vector_coefficients_low_to_high"]) == 4
        assert all(len(row) == 272 for row in vector["integer_vector_coefficients_low_to_high"])
        assert int(vector["common_positive_denominator"]) > 0
    indexes = certificate["operator_indices"]
    assert set(indexes) == {"g", "Gamma"}
    g_index = referenced(indexes["g"], "g")
    gamma_index = referenced(indexes["Gamma"], "Gamma")
    prime_counts = {}
    for target, index in (("g", g_index), ("Gamma", gamma_index)):
        assert index["target"] == target and index["field_component"] == 0
        assert index["coefficient_field_basis"] == FIELD_BASIS
        assert index["weighted_degree_bound_verified"] is True
        degree = 3 if target == "g" else 2
        assert index["regular_degree_bound"] == degree
        candidate = referenced(index["source_candidate"], target)
        assert candidate["matrix_row_blocks"] == index["matrix_row_blocks_tau"]
        assert candidate["source_original_vector"] == index["source_original_vector"]
        assert len(index["matrix_row_blocks_tau"]) == len(index["matrix_row_blocks_sigma"]) == len(row_ranges)
        for tau_spec, sigma_spec, (first, stop) in zip(
                index["matrix_row_blocks_tau"], index["matrix_row_blocks_sigma"], row_ranges):
            coefficient_count = sum(degree+1+EPS[a]-EPS[b] for b in range(first, stop) for a in range(272))
            for entry in (tau_spec, sigma_spec):
                block = referenced(entry, target)
                assert block["target"] == target and block["field_component"] == 0
                assert (block["row_first"], block["row_stop"]) == (first, stop)
                assert block["regular_degree_bound"] == degree
                assert int(block["common_positive_denominator"]) > 0
                assert len(block["coefficient_numerators"]) == coefficient_count
            sigma = referenced(sigma_spec, target)
            assert sigma["source_tau_matrix_row_block"] == tau_spec
            assert sigma["source_exact_candidate"] == index["source_candidate"]
            if target == "g":
                assert sigma["every_transition_exponent_nonnegative"] is True
                assert sigma["transported_original_first_column_verified_coefficientwise"] is True
                assert sigma["common_homogeneous_factor_in_pair"] == "t^3"
                assert sigma["original_function_or_section_rescaled_by_unit"] is False
            else:
                assert sigma["source_exact_Mg"] == indexes["g"]
                assert sigma["all_negative_power_coefficients_cancelled_exactly"] is True
                assert sigma["original_unit_column_zero_verified"] is True
                assert sigma["regular_derivation_relation"] == "delta_sigma=t*delta_tau"
                assert sigma["homogeneous_matrix_reversal_used_as_connection"] is False
        if target == "g":
            assert index["source_original_vector"] == vector_specs["g"]
            assert index["operator_kind"] == "multiplication"
            assert index["zero_component_proved_from_exact_original_vector"] is False
            assert index["original_first_column_verified_coefficientwise"] is True
            assert index["complete_polynomial_commutator_identity_verified"] is True
            assert index["commutator_maximum_degree"] == 6
            assert index["exact_commutator_points"] == list(range(7))
            assert index["primitive_cyclic_uniqueness_identifies_true_regular_multiplier"] is True
            first = referenced(index["exact_first_column_certificate"], target)
            assert first["original_first_column_verified_coefficientwise"] is True
            assert first["original_second_column_Wvg_verified_coefficientwise"] is True
            assert first["source_exact_two_known_columns"] == known_spec
            assert index["original_second_column_Wvg_verified_coefficientwise"] is True
            assert index["source_exact_two_known_columns"] == known_spec
        else:
            assert index["source_original_h_vector"] == vector_specs["h"]
            assert index["operator_kind"] == "normal_derivation_connection"
            assert index["source_exact_Mg"] == indexes["g"]
            assert index["weighted_degree_shift"] == 2
            assert index["Gamma_zero_first_column_and_H_original_first_column_verified"] is True
            assert index["complete_nested_commutator_identity_verified"] is True
            assert index["nested_commutator_maximum_degree"] == 6
            assert index["exact_nested_commutator_points"] == list(range(7))
            assert index["cyclic_uniqueness_identifies_H_with_actual_Mh"] is True
            assert index["original_nonhomogeneous_connection_identity_therefore_verified"] is True
            assert index["independent_Mh_reconstructed_or_stored"] is False
            assert index["sigma_regular_connection_verified_with_original_derivation_change"] is True
            equation = referenced(index["source_original_vector"], target)
            assert equation["source_original_g_vector"] == vector_specs["g"]
            assert equation["source_original_h_vector"] == vector_specs["h"]
            assert equation["zero_vector_shortcut_allowed"] is False
            first = referenced(index["exact_original_column_certificate"], target)
            assert first["actual_w0_original_M2_is_e2"] is True
            assert first["actual_original_W_first_column_is_constant_e1"] is True
            assert first["Gamma_e0_zero_verified_coefficientwise"] is True
            assert first["Gamma_e1_equals_original_h_verified_coefficientwise"] is True
            assert first["H_e0_equals_original_h_verified_coefficientwise"] is True
            assert first["source_original_h_vector"] == vector_specs["h"]
            assert first["source_exact_Mg"] == indexes["g"]
        assert first["source_candidate"] == index["source_candidate"]
        assert index["source_R806_cyclic_witness"] == certificate["source_R806_cyclic_witness"]
        points = index["exact_full_matrix_point_certificates"]
        assert len(points) == 7
        for point, entry in enumerate(points):
            data = referenced(entry, target)
            assert data["source_candidate"] == index["source_candidate"]
            assert data["exact_integer_point"] == point and data["full_matrix_shape"] == [272, 272]
            assert data["Krylov_invertibility_not_required_at_exact_verification_point"] is True
            assert data["all_exact_commutator_entries_zero" if target == "g" else "all_exact_nested_commutator_entries_zero"] is True
            blocks = data["full_row_block_certificates"]
            assert len(blocks) == len(row_ranges)
            for block_spec, (first, stop) in zip(blocks, row_ranges):
                block = referenced(block_spec, target)
                assert block["source_candidate"] == index["source_candidate"]
                assert block["exact_integer_point"] == point and block["column_count"] == 272
                assert (block["row_first"], block["row_stop"]) == (first, stop)
                if target == "g":
                    assert block["all_exact_integer_commutator_entries_zero"] is True
                    assert block["both_products_computed_over_Z_after_exact_denominator_clearing"] is True
                else:
                    assert block["all_exact_integer_nested_commutator_entries_zero"] is True
                    assert block["source_exact_Mg"] == indexes["g"]
                    assert block["source_original_h_vector"] == vector_specs["h"]
                    assert block["H_is_only_evaluated_at_this_point_not_reconstructed_as_a_polynomial_table"] is True
        history = referenced(index["latest_CRT_history_receipt"], target)
        assert history["current_full_CRT_checkpoint"] == candidate["source_CRT_checkpoint"]
        assert history["prime_count"] == index["actual_CRT_prime_count"]
        if target == "g":
            assert history["original_external_CRT_source"] == source_identity(original.item)
            assert history["original_external_CRT_receipt"] == plain(original.item["latest_CRT_receipt"])
            assert history["original_external_CRT_configuration_sha256"] == fingerprint(original.tag)
            assert history["original_external_current_preserves_its_own_configuration"] is True
            assert history["original_425_prime_arithmetic_recomputed"] is False
            assert history["source_checkpoint_or_source_temporary_files_deleted"] is False
            assert history["receipt_is_a_new_source_import_record_not_a_relabelled_old_stage"] is True
        else:
            assert history["large_vector_or_matrix_embedded"] is False
            assert history["full_temporary_images_discarded_only_after_CRT_commit"] is True
        prime_counts[target] = index["actual_CRT_prime_count"]
    assert certificate["actual_CRT_prime_counts"] == prime_counts
    assert prime_counts["g"] == 425
    assert g_index["original_external_CRT_source"]
    assert "projective_candidate_id" in g_index
    assert certificate["sigma_base_variable_derivative"] == {
        "matrix_blocks": g_index["matrix_row_blocks_sigma"], "rational_scalar": [-1, 1],
        "identity": "M_(delta_sigma t)=-t^3*D*Mg(1/t)*D^-1"}
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
    print(json.dumps({"R815_VERIFY_REVIEW": {
        "complete": True, "selected_input_files_verified": count, "complete_stage_files_verified": len(entries),
        "actual_CRT_prime_counts": prime_counts, "Mg_exact_points": list(range(7)),
        "Gamma_nested_exact_points": list(range(7)), "normal_affine_basis_rank": 272,
        "actual_core_seconds": certificate["seconds"], "independent_Mh_reconstructed_or_stored": False,
        "projective_mode": PROJECTIVE_MODE, "original_CRT_prime_count_reused": 425,
        "original_425_current_sha256": original.item["current"]["sha256"],
        "actual_original_shared_point_count": len(original.point_names),
        "original_cusp_zero_ideal_computed": False}}), flush=True)
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
