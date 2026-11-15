#!/usr/bin/env python3
"""Read one actually completed original R824 weight-five relation.

This module uses only the standard library.  It authenticates original source
bytes and exposes their unchanged coefficients; it performs no field arithmetic.
"""
import gzip
import hashlib
import json
from pathlib import Path
import re

RESULT = "R824-original-global-polar-generators"
CORE_SHA = "1ece3cf45f57fda2d1fe40f38efb3e225d2e05ce910a917eb38dbcd85fe3d1cb"
PROOF_SHA = "3a32e69f5ff3fb74ad7b262357e6b9d00da5e1f4348f65b1cdc0705d6fef7be1"
METHOD_SHA = "1bbba5fc3dcee565af90ed9b773a5a13e0ab3e4026e15608e4492d281c56fa76"
FIELD_CORE_SHA = "d024a7a6f5febd4658e8b5b5e5e3659f3c5fcc0daa39d70569ac408ef83a8751"
R786_INDEX_SHA = "0bb7cfeda48d6759f1553dec74485a28dc16e31cf3d500a095963888973c9b35"
SCALE = "13744803133596058624"
FIELD_ORDER = "B_fld^i*s^j; j=0,1 outer; i=0..6; B_fld=lambda*b"
BASE_KEYS = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
META = ("full-outputs-manifest.json", "run-receipt.json",
        "core-receipt.json", "public-actions-input.json")
HEX64 = re.compile(r"[0-9a-f]{64}")
INTEGER = re.compile(r"-?(0|[1-9][0-9]*)")
RELATION_NAME = re.compile(r"R824-power5-free-([0-9]{4})-exact-generator[.]json[.]gz")


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read(path):
    path = Path(path)
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def plain(entry):
    value = {key: entry[key] for key in ("file", "bytes", "sha256")}
    assert isinstance(value["file"], str) and Path(value["file"]).name == value["file"]
    assert "/" not in value["file"] and "\\" not in value["file"]
    assert isinstance(value["bytes"], int) and value["bytes"] >= 0
    assert HEX64.fullmatch(value["sha256"])
    return value


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def fingerprint(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def certificate_identity(value):
    if value.get("certificate") is not None:
        return value["certificate"]["file"], value["certificate"]["sha256"]
    name = value.get("certificate_name")
    if name is None:
        return None
    return name, value["files"][name]


def same_producer(left, right):
    for key in BASE_KEYS:
        assert str(left[key]) == str(right[key]), ("Changed actual producer", key)
    first, second = certificate_identity(left), certificate_identity(right)
    if first is not None and second is not None:
        assert first == second


class OriginalWeightFiveRelation:
    """A real R824 exact stage; no synthetic R787 producer or relation file."""

    def __init__(self, directory, producer, relation_spec,
                 original_R786_producer, original_R786_basis_index, original_b_polynomial):
        self.root, self.producer = Path(directory), producer
        self.relation_spec = plain(relation_spec)
        self.selected = {}
        assert producer["result"] == RESULT and producer["core_sha256"] == CORE_SHA
        assert HEX64.fullmatch(producer["manifest_sha256"])
        manifest_path = self.root/META[0]
        assert sha(manifest_path) == producer["manifest_sha256"]
        manifest = read(manifest_path)
        assert manifest["result"] == RESULT
        self.selected[META[0]] = file_spec(manifest_path)
        self.files = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(self.files) == len(manifest["files"])
        assert self.bound(self.relation_spec) == self.relation_spec
        assert producer["files"][self.relation_spec["file"]] == self.relation_spec["sha256"]
        match = RELATION_NAME.fullmatch(self.relation_spec["file"])
        assert match is not None
        self.free_column = int(match.group(1))
        assert 0 <= self.free_column < 1214 and self.free_column != 1186

        run, core, initial = (self.raw(name) for name in META[1:])
        assert run["result"] == core["result"] == initial["result"] == RESULT
        assert str(run["workflow_run_id"]) == str(producer["run_id"])
        assert run["source_commit"] == initial["source_commit"] == producer["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == CORE_SHA
        assert core["source_sha256"] == CORE_SHA
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        self.data = self.raw(self.relation_spec["file"])
        assert self.data["complete"] is True
        self.configuration = self.data["configuration"]
        tag = self.configuration
        assert tag["result"] == RESULT and tag["source_sha256"] == CORE_SHA
        assert tag["python_flint"] == "0.9.0"
        assert tag["R824_proof_sha256"] == initial["job"]["R824_proof_sha256"] == PROOF_SHA
        assert tag["R824_method_sha256"] == initial["job"]["R824_method_sha256"] == METHOD_SHA
        assert tag["R781_field_core_sha256"] == FIELD_CORE_SHA
        assert tag["original_map_index"] == 4 and tag["original_map_degree"] == 1206
        assert tag["original_basis_dimensions"] == {"5": 1234, "6": 1506}
        assert tag["orders"] == {"5": 129, "6": 142}
        assert tag["original_integer_scales"]["5"] == SCALE
        assert tag["reserved_R787_free_column"] == 1186
        assert tag["original_R787_reserved_target_recomputed"] is False
        same_producer(tag["source_identities"]["R786"], original_R786_producer)
        same_producer(initial["job"]["retained_sources"]["R786"], original_R786_producer)

        self.certificate = None
        self.completed_inventory = None
        certname = producer.get("certificate_name")
        if certname is not None:
            assert producer.get("expected_conclusion", "success") == "success"
            assert run["complete"] is True and run["process_exit_code"] == 0
            assert core["complete"] is True
            assert core["certificate_sha256"] == producer["files"][certname] == self.files[certname]["sha256"]
            cert = self.raw(certname)
            assert cert["result"] == RESULT and cert["complete"] is True
            assert cert["configuration"] == tag
            self.certificate = cert
            inventory = self.stage(cert["stage_manifest"])
            self.completed_inventory = {row["file"]: plain(row) for row in inventory["files"]}
            assert len(self.completed_inventory) == len(inventory["files"])
            for name, row in self.completed_inventory.items():
                assert self.files[name] == row
            assert self.completed_inventory[self.relation_spec["file"]] == self.relation_spec
            index = self.stage(cert["generator_index"])
            entries = [row for row in index["exact_generators"]
                       if row["ordinary_power"] == 5 and row["free_column"] == self.free_column]
            assert len(entries) == 1 and plain(entries[0]["source"]) == self.relation_spec
            self.source_state = "successful_R824_scope_with_this_exact_generator"
        else:
            assert producer.get("allow_completed_checkpoint") is True
            assert producer["expected_conclusion"] == "failure"
            assert producer["configuration_stage"] == self.relation_spec["file"]
            codes = producer["accepted_checkpoint_exit_codes"]
            assert isinstance(codes, list) and codes and all(isinstance(code, int) and code != 0 for code in codes)
            assert run["complete"] is False and core["complete"] is False
            assert run["process_exit_code"] in codes
            self.source_state = "ended_checkpoint_with_this_complete_exact_generator"
        self.identity = {key: producer[key] for key in BASE_KEYS}
        if certname is not None:
            self.identity["certificate"] = self.files[certname]

        data = self.data
        assert data["ordinary_power"] == 5 and data["original_basis_dimension"] == 1234
        assert data["candidate_only"] is False
        assert data["exact_original_A_equals_yB"] is True and data["B_nonzero"] is True
        assert data["basis_integer_scale"] == SCALE and data["L_basis"] == FIELD_ORDER
        assert data["field"] == tag["field"]
        assert data["field"]["original_b_minimal_polynomial"] == original_b_polynomial
        assert data["field"]["original_b_replaced_by_another_twist"] is False
        assert int(data["field"]["lambda"]) > 0
        assert plain(data["original_basis_index"]) == plain(original_R786_basis_index)
        assert data["original_basis_index"]["sha256"] == R786_INDEX_SHA
        for key in ("A_integer_L_coordinates", "B_integer_L_coordinates"):
            rows = data[key]
            assert len(rows) == 1234 and all(len(row) == 14 for row in rows)
            assert all(isinstance(value, str) and INTEGER.fullmatch(value) and value != "-0"
                       for row in rows for value in row)
        assert any(value != "0" for row in data["B_integer_L_coordinates"] for value in row)
        assert int(data["common_rational_denominator_cleared"]) > 0
        assert int(data["common_integer_content_removed"]) > 0
        assert data["full_original_relation_orders"] == 129
        assert data["full_original_t_coordinates"] == 20
        assert data["full_original_Q_coordinates_per_order"] == 280
        assert data["full_polar_module_or_height_claimed"] is False
        assert isinstance(data["actual_Dixon_digits"], int) and data["actual_Dixon_digits"] > 0
        target = data["target_configuration"]
        assert target["ordinary_power"] == 5 and target["free_column"] == self.free_column
        assert target["prime"] == 1000000753
        assert target["normalization"] == "one common original L free coordinate is 1; all other free coordinates are 0"
        assert target["original_R787_reserved_target_recomputed"] is False
        assert len(target["branch_stages"]) == 14
        for entry in [target["chart"]]+target["branch_stages"]:
            self.bound(entry)
        # The original power-five rational block is an unchanged R787 input,
        # not a new R824 output and not a newly computed matrix.
        block = plain(target["rational_block"])
        assert target["rational_block"]["producer"] == "R787"
        assert block == {
            "file": "R787-prime-1000000753-rational-blocks.json.gz",
            "bytes": 9169464,
            "sha256": "fb8a82957474e657fc476aa2baa0d8ce9f4c8b6cc86c2b55a79e75913d610b3b"}
        old_identity = tag["source_identities"]["R787"]
        same_producer(old_identity, initial["job"]["retained_sources"]["R787"])
        assert old_identity["result"] == "R787-original-power5-function-relation"
        assert old_identity["run_id"] == "43683912711"
        assert old_identity["source_commit"] == "eab5e58bbf951c48ccf13a109bbdf0b0289a6f23"
        assert old_identity["core_sha256"] == "93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04"
        assert old_identity["manifest_sha256"] == "613f436b2c398cdcd5c9a92c4eb47e72bc81f8d0e8395322eff6455c89c0821c"
        self.original_R787_rational_block_identity = old_identity
        assert plain(data["common_clear_operator"]) == plain(target["common_clear_operator"])
        self.bound(data["common_clear_operator"])
        self.bound(data["candidate_stage"])
        plain(data["unreduced_product_digest_only"])
        plain(data["final_lift_digest_only"])
        checks, next_order = [], 0
        for entry in data["full_relation_verification_stages"]:
            value = self.stage(entry)
            assert value["candidate_sha256"] == data["candidate_stage"]["sha256"]
            assert value["unreduced_product_sha256"] == data["unreduced_product_digest_only"]["sha256"]
            assert value["first_order"] == next_order
            assert next_order < value["stop_order"] <= min(next_order+8, 129)
            assert value["all_original_280_Q_coordinates_zero_at_each_order"] is True
            next_order = value["stop_order"]
            checks.append(plain(entry))
        assert next_order == 129 and checks
        self.verification_specs = checks
        self.original_R786_producer = original_R786_producer
        self.original_R786_basis_index = plain(original_R786_basis_index)

    def bound(self, entry):
        entry = plain(entry)
        assert self.files[entry["file"]] == entry
        return entry

    def raw(self, name):
        entry = self.files[name]
        if name in self.producer.get("files", {}):
            assert entry["sha256"] == self.producer["files"][name]
        path = self.root/name
        assert path.is_file() and file_spec(path) == entry
        self.selected[name] = entry
        return read(path)

    def stage(self, entry):
        entry = self.bound(entry)
        if self.completed_inventory is not None:
            assert self.completed_inventory[entry["file"]] == entry
        value = self.raw(entry["file"])
        assert value["complete"] is True and value["configuration"] == self.configuration
        return value

    def receipt(self):
        data = self.data
        return {
            "actual_producer": self.identity,
            "actual_source_state": self.source_state,
            "actual_exact_relation": self.relation_spec,
            "actual_free_column": self.free_column,
            "actual_target_configuration_sha256": fingerprint(data["target_configuration"]),
            "original_R786_producer": self.original_R786_producer,
            "original_R786_basis_index": self.original_R786_basis_index,
            "original_map_index": 4, "original_map_degree": 1206,
            "ordinary_power": 5, "original_basis_dimension": 1234,
            "basis_integer_scale": SCALE, "field": data["field"], "L_basis": FIELD_ORDER,
            "common_rational_denominator_cleared": data["common_rational_denominator_cleared"],
            "common_integer_content_removed": data["common_integer_content_removed"],
            "common_denominator_or_content_reinserted": False,
            "all129_original_relation_orders_verified": True,
            "original_Q_coordinates_per_order": 280,
            "full_relation_verification_stages": self.verification_specs,
            "common_clear_operator_identity_only": plain(data["common_clear_operator"]),
            "candidate_identity_only": plain(data["candidate_stage"]),
            "unchanged_original_R787_rational_block_identity_only": {
                "producer": self.original_R787_rational_block_identity,
                "file": plain(data["target_configuration"]["rational_block"])},
            "unreduced_product_digest_only": plain(data["unreduced_product_digest_only"]),
            "final_lift_digest_only": plain(data["final_lift_digest_only"]),
            "actual_Dixon_digits": data["actual_Dixon_digits"],
            "original_y_ratio_preserved": True,
            "original_R787_reserved_target_recomputed": False,
            "synthetic_R787_producer_or_relation_file_created": False,
            "new_field_arithmetic_performed_by_adapter": False,
            "selected_original_source_files": [self.selected[name] for name in sorted(self.selected)],
        }
