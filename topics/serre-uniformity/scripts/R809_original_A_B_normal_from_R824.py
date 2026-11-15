#!/usr/bin/env python3
"""Only A/B normal coordinates from one real R824 relation and the completed R809 S5 block."""
import argparse
import gc
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
FRAMEWORK_NAME = "R809_original_S5_normal_coordinates.py"
FRAMEWORK_SHA = "dedb5d6149a3c3ae86ad09e51f30c1424951a09010bf48afd948d2628e1ec21d"
ADAPTER_NAME = "R824_original_exact_relation_adapter.py"
ADAPTER_SHA = "5a6a100a561ce02350a5d538df908d4cca9575e21b251a848a3bfba9d3df1958"
PROOF_SHA = "68793d3f3911d6c2ab3d530575634a70953580c221c4c4fed5fa542a2ed88a40"
METHOD_SHA = "b38777a5fc6baadbb5bd832c5b6897338c7649f9b80b5a505dde541710dd5108"
RELATION_METHOD_SHA = "68877a988f4df5dc3a7609ea46d4f40129d40af40b5467200456829df730d818"
R787_SHA = "93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04"
R786_SHA = "4508095a95a2bcaec8c8db8fcd550fbc618b017d2bc0007945783bc109dbf851"
RESULT = "R809-original-A-B-normal-coordinates-from-R824"
FINAL = "p41-original-A-B-normal-coordinates-from-R824-certificate.json"
SOURCE_STAGE = "R809-R824-original-source-interface"
PREFIX = "R809-"
LABELS = {"R809", "R786", "R787", "R824"}
S5_INDEX_SHA = "f6f6f0ee2bae106ef474d2cff32c743b1d8e0a886f80c26aaf8708c89ea1c119"
R786_INDEX_SHA = "0bb7cfeda48d6759f1553dec74485a28dc16e31cf3d500a095963888973c9b35"
INVERSE_SHA = "d61b9eb35866dfca066aa5bb22042465d68b5aacf4372f75be0908e5fa9115ca"


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


assert sha(HERE/FRAMEWORK_NAME) == FRAMEWORK_SHA
assert sha(HERE/ADAPTER_NAME) == ADAPTER_SHA
loader = importlib.util.spec_from_file_location("R809_R824_frozen_exact_framework", HERE/FRAMEWORK_NAME)
base = importlib.util.module_from_spec(loader)
loader.loader.exec_module(base)
loader = importlib.util.spec_from_file_location("R809_R824_actual_relation_reader", HERE/ADAPTER_NAME)
adapter = importlib.util.module_from_spec(loader)
loader.loader.exec_module(adapter)
read, save, file_spec = base.read, base.save, base.file_spec
plain, fingerprint = base.plain_spec, base.fingerprint
fmpz_mat, fmpq, nmod_mat = base.fmpz_mat, base.fmpq, base.nmod_mat
P, LEVEL, REAL, COUNT, DIM, ROWS, FREE, LDEG = 41, 82, 20, 69, 1234, 1380, 272, 14
EPS, FIELD_BASIS = base.EPS, base.FIELD_BASIS


def producer_identity(spec):
    value = {key: spec[key] for key in adapter.BASE_KEYS}
    name = spec.get("certificate_name")
    if name is not None:
        value["certificate"] = {"file": name, "sha256": spec["files"][name]}
    return value


class OriginalRealRows:
    """Only previously completed R787 real V5 rows, never its unfinished relation."""
    def __init__(self, retained, spec, original_R786):
        self.spec, self.root = spec, Path(retained)/"R787"
        assert spec["result"] == "R787-original-power5-function-relation"
        assert spec["core_sha256"] == R787_SHA
        path = self.root/"full-outputs-manifest.json"
        assert sha(path) == spec["manifest_sha256"]
        manifest = read(path)
        assert manifest["result"] == spec["result"]
        self.files = {row["file"]: row for row in manifest["files"]}
        assert len(self.files) == len(manifest["files"])
        self.checked = set()
        run, core, initial = (self.raw(name) for name in
            ("run-receipt.json", "core-receipt.json", "public-actions-input.json"))
        assert run["result"] == core["result"] == initial["result"] == spec["result"]
        assert run["source_commit"] == initial["source_commit"] == spec["source_commit"]
        assert str(run["workflow_run_id"]) == str(spec["run_id"])
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == core["source_sha256"] == R787_SHA
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        if spec.get("certificate_name") is None:
            assert spec["expected_conclusion"] == "failure"
            assert spec["allow_completed_checkpoint"] is True
            assert run["complete"] is False and core["complete"] is False
            assert run["process_exit_code"] in spec["accepted_checkpoint_exit_codes"]
        else:
            assert run["complete"] is core["complete"] is True and run["process_exit_code"] == 0
            name = spec["certificate_name"]
            assert core["certificate_sha256"] == self.files[name]["sha256"] == spec["files"][name]
            cert = self.raw(name)
            assert cert["result"] == spec["result"] and cert["complete"] is True
        self.chart_name = "R787-prime-1000000753-chart.json.gz"
        chart = self.raw(self.chart_name)
        assert chart["complete"] is True
        self.tag = chart["configuration"]
        assert self.tag["source_sha256"] == R787_SHA and self.tag["python_flint"] == "0.9.0"
        adapter.same_producer(self.tag["retained_artifacts"]["R786"], original_R786)
        self.initial = initial

    def raw(self, name):
        assert Path(name).name == name
        row = self.files[name]
        if name in self.spec.get("files", {}):
            assert row["sha256"] == self.spec["files"][name]
        path = self.root/name
        if name not in self.checked:
            assert file_spec(path) == plain(row)
            self.checked.add(name)
        return read(path)

    def row(self, index, original_row):
        name = "R787-real-power5-row-"+str(index).zfill(4)+".json.gz"
        data = self.raw(name)
        assert data["complete"] is True and data["configuration"] == self.tag
        assert data["index"] == index
        assert data["R786_row_sha256"] == original_row["sha256"]
        assert data["all_original_phase_involutions_verified"] is True
        assert data["averaging_used"] is False
        rows = data["integer_t_coefficients"]
        assert len(rows) == 129 and all(len(row) == REAL for row in rows)
        return [int(value) for row in rows[:COUNT] for value in row], plain(self.files[name])


class Job(base.Job):
    def __init__(self, args):
        self.args, self.out, self.started = args, args.output, time.monotonic()
        self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        item = self.item
        assert item["result"] == RESULT and item["p"] == P
        assert item["producer_inputs_pending"] is False
        assert item["core_sha256"] == sha(__file__)
        assert item["normal_framework"] == FRAMEWORK_NAME
        assert item["normal_framework_sha256"] == FRAMEWORK_SHA
        assert item["relation_adapter"] == ADAPTER_NAME and item["relation_adapter_sha256"] == ADAPTER_SHA
        assert item["R809_proof_sha256"] == sha(args.proof) == PROOF_SHA
        assert item["A_B_consumer_method_sha256"] == sha(args.method) == METHOD_SHA
        assert item["relation_adapter_method_sha256"] == RELATION_METHOD_SHA
        assert base.flint.__version__ == "0.9.0"
        assert item["qY_count"] == COUNT and item["auxiliary_prime_start"] == 1000000007
        assert item["dixon_group_columns"] == 7 and item["reconstruct_every_digits"] == 8
        assert set(item["retained_artifacts"]) == LABELS
        self.requested = ["A", "B"]
        assert item["requested_target_groups"] == self.requested
        self.r809 = base.Retained(args.retained, "R809", item["retained_artifacts"]["R809"])
        self.r786 = base.Retained(args.retained, "R786", item["retained_artifacts"]["R786"])
        assert self.r809.spec["result"] == "R809-original-S5-normal-coordinates"
        assert self.r809.spec["core_sha256"] == FRAMEWORK_SHA
        assert self.r786.spec["core_sha256"] == R786_SHA
        self.r809.load_inventory()
        c809, c786 = self.r809.certificate, self.r786.certificate
        assert c809["p"] == P and c809["S5_dimension"] == DIM and c809["qY_count"] == COUNT
        assert c809["full_real_coordinates"] == ROWS
        assert c809["normal_basis_rank"] == FREE and c809["normal_basis_degrees"] == EPS
        assert c809["basis_integer_scale"] == str(LEVEL**10)
        assert c809["coefficient_field_basis"] == FIELD_BASIS
        assert c809["all_requested_targets_verified_in_all1380_rows"] is True
        assert c809["original_scalar_and_field_normalizations_preserved"] is True
        assert self.r809.tag["R809_proof_sha256"] == PROOF_SHA
        adapter.same_producer(self.r809.tag["basis_producers"]["R786"], self.r786.spec)
        assert c786["exact_K_basis_prefix_bound_qY"] == 128
        assert c786["exact_power5_basis_dimension"] == DIM
        assert c786["basis_integer_scale"] == str(LEVEL**10)
        assert c786["basis_in_original_R775_saved_order"] is True
        self.old_basis_spec = plain(c786["basis_index"])
        assert self.old_basis_spec["sha256"] == R786_INDEX_SHA
        assert self.old_basis_spec == plain(self.r786.files[self.old_basis_spec["file"]])
        self.old_basis_index = self.r786.stage(self.old_basis_spec["file"], R786_INDEX_SHA)
        assert self.old_basis_index["dimension"] == DIM and self.old_basis_index["bound_qY"] == 128
        self.old_basis_rows = self.old_basis_index["basis_rows"]
        assert len(self.old_basis_rows) == DIM
        assert [row["index"] for row in self.old_basis_rows] == list(range(DIM))
        self.model = c809["original_b_model"]
        self.model_spec = dict(file_spec(self.r809.directory/self.r809.spec["certificate_name"]), producer="R809")
        self.actual_relation = adapter.OriginalWeightFiveRelation(
            Path(args.retained)/"R824", item["retained_artifacts"]["R824"], item["relation_spec"],
            self.r786.spec, self.old_basis_spec, self.model)
        self.relation = self.actual_relation.data
        self.r787 = OriginalRealRows(args.retained, item["retained_artifacts"]["R787"], self.r786.spec)
        adapter.same_producer(self.actual_relation.configuration["source_identities"]["R787"], self.r787.spec)
        self.matrix_spec = plain(c809["S5_basis_index"])
        self.minor_spec = plain(c809["minor_stage"])
        self.inverse_spec = plain(c809["modular_inverse_stage"])
        assert self.matrix_spec["sha256"] == S5_INDEX_SHA
        assert self.inverse_spec["sha256"] == INVERSE_SHA
        self.original_basis_index = self.r809.indexed(self.matrix_spec)
        index = self.original_basis_index
        assert index["dimension"] == DIM and index["qY_count"] == COUNT
        assert index["full_coordinate_rows"] == ROWS and index["real_coordinate_count"] == REAL
        assert index["integer_scale"] == str(LEVEL**10)
        assert index["normal_affine_basis_rank"] == FREE and index["normal_basis_degrees"] == EPS
        assert index["all_original_term_phases_and_scales_verified"] is True
        mapping = [(a, j) for a, eps in enumerate(EPS) for j in range(6-eps)]
        assert len(index["basis_rows"]) == len(mapping) == DIM
        for i, (row, pair) in enumerate(zip(index["basis_rows"], mapping)):
            a, j = pair
            assert row["index"] == i and row["normal_basis_index"] == a and row["z_degree"] == j
            assert row["normal_basis_degree"] == EPS[a]
            assert plain(row["source"]) == self.r809.inventory[row["source"]["file"]]
        self.n = c809["actual_sigma_integer_n"]
        assert self.n == self.r809.tag["actual_sigma_integer_n"] == 1
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "python_flint": base.flint.__version__,
            "R809_proof_sha256": PROOF_SHA, "A_B_consumer_method_sha256": METHOD_SHA,
            "relation_adapter_method_sha256": RELATION_METHOD_SHA,
            "normal_framework_sha256": FRAMEWORK_SHA, "relation_adapter_sha256": ADAPTER_SHA,
            "p": P, "qY_count": COUNT, "full_coordinate_rows": ROWS,
            "S5_dimension": DIM, "normal_basis_rank": FREE, "normal_basis_degrees": EPS,
            "basis_integer_scale": str(LEVEL**10), "coefficient_field_basis": FIELD_BASIS,
            "original_b_model": self.model, "actual_sigma_integer_n": self.n,
            "source_identities": {label: producer_identity(item["retained_artifacts"][label])
                                  for label in ("R809", "R786", "R787")},
            "actual_R824_source": self.actual_relation.identity,
            "actual_R824_relation": plain(item["relation_spec"]),
            "original_S5_configuration_sha256": fingerprint(self.r809.tag),
            "original_S5_basis_index": self.matrix_spec,
            "original_S5_minor": self.minor_spec, "original_S5_modular_inverse": self.inverse_spec,
            "original_R786_basis_index": self.old_basis_spec,
            "auxiliary_prime_start": item["auxiliary_prime_start"],
            "dixon_group_columns": item["dixon_group_columns"],
            "reconstruct_every_digits": item["reconstruct_every_digits"],
            "old_S5_C_targets_fixed_inverse_and_q_rows_recomputed": False,
            "original_R824_common_denominator_or_content_reinserted": False,
            "requested_targets_budget_and_wrapper_excluded_from_mathematical_identity": True,
        }
        self.tag_hash = fingerprint(self.tag)
        self.target_tags = {}
        self.C = self.square = self.inverse = self.F = None
        self.real_row_specs = None
        audit = {
            "actual_R824_relation_receipt": self.actual_relation.receipt(),
            "original_S5_producer": producer_identity(self.r809.spec),
            "original_S5_configuration": self.r809.tag,
            "original_S5_basis_index": self.matrix_spec,
            "original_S5_minor": self.minor_spec, "original_S5_modular_inverse": self.inverse_spec,
            "original_R786_producer": producer_identity(self.r786.spec),
            "original_R786_basis_index": self.old_basis_spec,
            "original_real_rows_producer": producer_identity(self.r787.spec),
            "original_14_column_basis": FIELD_BASIS,
            "old_S5_or_C_targets_or_fixed_inverse_recomputed": False,
        }
        prior = self.cached(SOURCE_STAGE)
        if prior is None:
            self.store(SOURCE_STAGE, audit)
        else:
            for key, value in audit.items():
                assert prior[key] == value

    def target_tag(self, target):
        assert target in ("A", "B")
        if target not in self.target_tags:
            self.target_tags[target] = {
                "basis_configuration_sha256": self.tag_hash, "target": target,
                "coefficient_field_basis": FIELD_BASIS,
                "original_b_model": self.model, "original_b_model_source": self.model_spec,
                "actual_R824_source": self.actual_relation.identity,
                "actual_R824_relation": plain(self.item["relation_spec"]),
                "original_R824_free_column": self.actual_relation.free_column,
                "original_field_lambda": self.relation["field"]["lambda"],
                "original_R786_basis_index": self.old_basis_spec,
                "original_S5_producer": producer_identity(self.r809.spec),
                "original_S5_basis_index": self.matrix_spec,
                "homogeneous_target": target, "normal_function": target+"/tau^5",
                "regular_degree_bound": 5,
                "common_R824_denominator_or_content_reinserted": False,
                "Bfield_to_b_column_factor": "lambda^(column mod7), same two s blocks",
            }
        return self.target_tags[target]

    def basis(self):
        if self.C is not None:
            return self.C
        columns = []
        for row in self.original_basis_index["basis_rows"]:
            self.budget()
            data = self.r809.indexed(row["source"])
            for key in ("index", "normal_basis_index", "normal_basis_degree", "z_degree"):
                assert data[key] == row[key]
            assert data["recipe"] == row["recipe"]
            assert data["integer_scale"] == str(LEVEL**10)
            assert data["qY_count"] == COUNT and data["real_coordinate_count"] == REAL
            assert data["all_original_term_phases_and_scales_verified"] is True
            assert data["original_R805_free_generator_unchanged"] is True
            values = data["integer_v_t_coefficients"]
            assert len(values) == COUNT and all(len(value) == REAL for value in values)
            columns.append([int(value) for part in values for value in part])
        self.C = fmpz_mat(columns).transpose()
        assert self.C.nrows() == ROWS and self.C.ncols() == DIM
        del columns
        gc.collect()
        return self.C

    def solver(self):
        if self.inverse is not None:
            return
        C = self.basis()
        minor = self.r809.indexed(self.minor_spec)
        rank = self.r809.indexed(minor["actual_rank_stage"])
        assert minor["S5_basis_index"] == rank["S5_basis_index"] == self.matrix_spec
        assert minor["actual_rank"] == rank["actual_rank"] == DIM
        assert minor["full_coordinate_rows"] == ROWS and minor["column_indices"] == list(range(DIM))
        assert minor["minor_is_from_actual_69_term_matrix"] is True
        assert minor["row_indices"] == rank["row_indices"]
        assert minor["prime"] == rank["prime"] == self.r809.certificate["actual_prime"] == 1000000007
        assert minor["actual_determinant_mod_prime"] == rank["actual_determinant_mod_prime"] == \
            self.r809.certificate["actual_short_minor_determinant"] == 29693114
        self.I, self.prime = minor["row_indices"], minor["prime"]
        assert self.I == sorted(set(self.I)) and len(self.I) == DIM
        assert all(0 <= i < ROWS for i in self.I)
        self.square = fmpz_mat([[C[i, j] for j in range(DIM)] for i in self.I])
        data = self.r809.indexed(self.inverse_spec)
        assert data["prime"] == self.prime and data["minor_stage"] == self.minor_spec
        assert data["S5_basis_index"] == self.matrix_spec
        assert data["inverse_product_exactly_verified_mod_prime"] is True
        assert data["composite_modulus_matrix_inversion"] is False
        self.inverse = nmod_mat(data["inverse_mod_prime"], self.prime)
        assert self.inverse.nrows() == self.inverse.ncols() == DIM

    def original_matrix(self):
        if self.F is not None:
            return self.F
        columns, sources = [], []
        for i, row in enumerate(self.old_basis_rows):
            self.budget()
            values, spec = self.r787.row(i, row)
            assert len(values) == ROWS
            columns.append(values)
            sources.append(spec)
        self.F = fmpz_mat(columns).transpose()
        self.real_row_specs = sources
        assert self.F.nrows() == ROWS and self.F.ncols() == DIM
        del columns
        gc.collect()
        return self.F

    def target(self, target):
        assert target in ("A", "B")
        name = "R809-target-"+target+"-full-prefix"
        old = self.cached(name, target)
        if old is not None:
            assert old["target"] == target and old["full_coordinate_rows"] == ROWS
            assert old["coefficient_field_basis"] == FIELD_BASIS
            return old, file_spec(self.path(name))
        self.budget()
        F = self.original_matrix()
        coefficients = [[int(value) for value in row] for row in self.relation[target+"_integer_L_coordinates"]]
        combined = F*fmpz_mat(coefficients)
        lam = int(self.relation["field"]["lambda"])
        columns, scales = [], []
        for k in range(LDEG):
            self.budget()
            values = [int(combined[i, k]) for i in range(ROWS)]
            content = base.integer_content(values)
            if content:
                columns.append([str(value//content) for value in values])
                scales.append(base.pairs(fmpq(content*lam**(k % 7))))
            else:
                columns.append(["0"]*ROWS)
                scales.append(["0", "1"])
        assert len(columns) == len(scales) == LDEG
        assert any(base.dq(scale) for scale in scales)
        sources = {
            "actual_R824_source": self.actual_relation.identity,
            "actual_R824_relation": plain(self.item["relation_spec"]),
            "original_R787_completed_real_rows": self.real_row_specs,
            "original_R787_completed_real_rows_producer": producer_identity(self.r787.spec),
            "original_R786_basis_index": self.old_basis_spec,
            "original_Bfield_equals_lambda_b": str(lam),
            "original_R824_common_denominator_or_content_reinserted": False,
            "literal_tau_factor": False,
        }
        self.store(name, {
            "target": target, "qY_count": COUNT, "full_coordinate_rows": ROWS,
            "primitive_integer_columns": columns, "rational_scales": scales,
            "source_inputs": sources, "coefficient_field_basis": FIELD_BASIS,
            "homogeneous_basis_scale": str(LEVEL**10),
            "target_known_globally_in_original_V5": True, "regular_degree_bound": 5,
            "original_field_and_scalar_normalizations_preserved": True,
            "old_real_rows_or_original_phase_conversion_recomputed": False,
        }, target)
        return self.cached(name, target), file_spec(self.path(name))

    def run(self):
        for target in self.requested:
            self.target(target)
        self.F = None
        gc.collect()
        vectors = {target: self.normal_vector(target) for target in self.requested}
        files = [file_spec(path) for path in sorted(self.out.glob("R809-*.json.gz"))
                 if not path.name.startswith("R809-R824-stage-manifest-")
                 and not path.name.endswith("-dixon-current.json.gz")]
        manifest_name = "R809-R824-stage-manifest-"+fingerprint(files)[:24]
        inventory = self.cached(manifest_name)
        if inventory is None:
            manifest = self.store(manifest_name, {"files": files})
        else:
            assert inventory["files"] == files
            manifest = file_spec(self.path(manifest_name))
        assert not list(self.out.glob("R809-*-dixon-current.json.gz"))
        cert = {
            "result": RESULT, "complete": True, "configuration": self.tag,
            "p": P, "completed_scope": "A_and_B_only_from_one_true_R824_relation",
            "requested_target_groups": self.requested, "completed_target_groups": self.requested,
            "completed_rational_RHS_columns": 28,
            "S5_dimension": DIM, "qY_count": COUNT, "full_real_coordinates": ROWS,
            "normal_basis_rank": FREE, "normal_basis_degrees": EPS,
            "basis_integer_scale": str(LEVEL**10), "actual_sigma_integer_n": self.n,
            "coefficient_field_basis": FIELD_BASIS, "original_b_model": self.model,
            "original_S5_producer": producer_identity(self.r809.spec),
            "S5_basis_index": self.matrix_spec, "minor_stage": self.minor_spec,
            "modular_inverse_stage": self.inverse_spec,
            "external_S5_references_keep_their_original_configuration": True,
            "actual_prime": self.prime, "actual_short_minor_determinant": 29693114,
            "actual_R824_source": self.actual_relation.identity,
            "actual_R824_relation": plain(self.item["relation_spec"]),
            "original_R824_free_column": self.actual_relation.free_column,
            "relation_source_receipt": file_spec(self.path(SOURCE_STAGE)),
            "normal_vectors": vectors, "normal_function_equation": "y=normal(A)/normal(B)",
            "completed_target_configurations": {target: self.target_tag(target) for target in self.requested},
            "all28_rational_RHS_columns_verified_in_all1380_rows": True,
            "actual_A_B_normal_vectors_computed": True, "old_C_targets_recomputed": False,
            "old_S5_rows_or_fixed_inverse_recomputed": False,
            "old_original_q_rows_or_phase_conversions_recomputed": False,
            "original_scalar_and_field_normalizations_preserved": True,
            "original_R824_denominator_and_content_reinserted": False,
            "synthetic_original_R809_or_R787_result_created": False,
            "actual_regular_multipliers_polar_ideal_eta_or_height_computed": False,
            "characteristic_zero_inverse_matrix_formed": False,
            "stage_manifest": manifest, "seconds": time.monotonic()-self.started,
        }
        save(self.out/FINAL, cert)
        save(self.out/"core-receipt.json", {
            "result": RESULT, "complete": True, "source_sha256": sha(__file__),
            "certificate_sha256": sha(self.out/FINAL),
            "completed_target_groups": self.requested, "completed_rational_RHS_columns": 28,
            "all28_rational_RHS_columns_verified_in_all1380_rows": True,
            "actual_A_B_normal_vectors_computed": True,
            "actual_regular_multipliers_polar_ideal_eta_or_height_computed": False})
        return 0


def main():
    base.guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "proof", "method", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    try:
        return Job(args).run()
    except base.BudgetStop as error:
        args.output.mkdir(parents=True, exist_ok=True)
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "budget_stop": str(error), "completed_source_bound_targets_and_current_lifts_preserved": True})
        return 124
    except BaseException as error:
        args.output.mkdir(parents=True, exist_ok=True)
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "error": type(error).__name__+": "+str(error),
            "completed_source_bound_targets_and_current_lifts_preserved": True})
        raise


if __name__ == "__main__":
    raise SystemExit(main())
