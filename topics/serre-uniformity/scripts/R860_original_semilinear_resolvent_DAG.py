#!/usr/bin/env python3
"""R860: source-complete original semilinear cofactor expressions; no expansion.

The matrices and rational coefficients are the original accepted R806 outputs.
This consumer constructs exact determinant-expression nodes.  It does not
claim to have expanded either bivariate determinant, a power-basis coordinate
vector, a new Riemann--Roch kernel, or any period.
"""

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time
import traceback

RESULT = "R860-original-semilinear-resolvent-DAG"
FINAL = "p41-original-semilinear-resolvent-DAG-certificate.json"
PREFIX = "R860-"
MANIFEST = "full-outputs-manifest.json"
META = ("public-actions-input.json", "run-receipt.json", "core-receipt.json")
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
RANK = 272
EPS = [0] + [1] * 144 + [2] * 127
S3 = 690
GROUPS = 34
TARGET = 72
SOURCE_COUNTS = {"R805": 7, "R806": 45, "R853": 9}
CERTIFICATES = {
    "R805": "p41-original-affine-pencil-free-basis-certificate.json",
    "R806": "p41-original-primitive-multiplication-certificate.json",
    "R853": "p41-original-semilinear-V1-conjugates-certificate.json",
}
PROOF_KEYS = ("R802", "R805", "R806", "R813", "R853", "FM", "R860")
STRATEGY = {
    "scope": "two_original_cofactor_expressions_and_fixed_differential",
    "normal_basis_rank": 272,
    "original_target_normal_basis_index": 72,
    "original_target_V1_index": 73,
    "matrix_convention": "row_output_column_input",
    "denominator_deleted_row": 0,
    "denominator_deleted_column": 0,
    "numerator_deleted_row": 72,
    "numerator_deleted_column": 0,
    "numerator_cofactor_sign": 1,
    "denominator_T_degree": 271,
    "denominator_total_degree_bound": 271,
    "numerator_T_degree_bound": 270,
    "numerator_total_degree_bound": 272,
    "denominator_nonzero_basis": "monic_T_degree271_below_original_minimal_degree272",
    "source_coefficients": "original_R806_numerator_over_original_column_denominator",
    "old_integer_scale_reinserted": False,
    "full_characteristic_zero_Krylov_inverse_computed": False,
    "expanded_bivariate_cofactors_computed": False,
    "expanded_power_basis_coordinates_computed": False,
    "original_RR_kernel_or_connection_or_period_computed": False,
    "derivation_action": "c_Y_delta_equals_delta_c_Y",
    "differential_action": "c_Y_nu_equals_nu",
    "original_D0": "qY/82*d/dqY",
    "original_nu": "82*tau*dqY/qY",
    "only_transport_directory_resume_and_budget_excluded_from_mathematical_identity": True,
}


class BudgetStop(Exception):
    pass


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open(path, "rt", encoding="utf-8") if path.name.endswith(".gz")
          else path.open("r", encoding="utf-8")) as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, sort_keys=True, ensure_ascii=False,
                         separators=(",", ":")).encode() + b"\n"
    temp = path.with_name(path.name + ".tmp")
    with temp.open("wb") as stream:
        if path.name.endswith(".gz"):
            with gzip.GzipFile(fileobj=stream, mode="wb", mtime=0) as compressed:
                compressed.write(payload)
        else:
            stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temp, path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def plain(value):
    assert isinstance(value, dict)
    result = {key: value[key] for key in ("file", "bytes", "sha256")}
    assert Path(result["file"]).name == result["file"]
    assert isinstance(result["bytes"], int) and result["bytes"] >= 0
    assert re.fullmatch(r"[0-9a-f]{64}", result["sha256"])
    return result


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def bound(directory, entry):
    entry = plain(entry)
    path = Path(directory) / entry["file"]
    assert path.is_file(), entry["file"]
    assert path.stat().st_size == entry["bytes"], entry["file"]
    assert sha(path) == entry["sha256"], entry["file"]
    return path


def identity(source):
    return {key: source[key] for key in BASE}


def source_identity(source):
    return {
        **identity(source),
        "certificate": plain(source["certificate"]),
        "configuration_sha256": source["configuration_sha256"],
        "selected_files_sha256": fingerprint(source["files"]),
        "selected_file_count": len(source["files"]),
    }


def expected_tag(item):
    return {
        "result": RESULT,
        "source_sha256": item["core_sha256"],
        "p": 41,
        "arithmetic": "stdlib_exact_source_and_determinant_expression_program",
        "proofs_sha256": {key: item["proofs"][key]["sha256"] for key in PROOF_KEYS},
        "method_sha256": item["method_sha256"],
        "sources": {key: source_identity(item["sources"][key]) for key in sorted(SOURCE_COUNTS)},
        "normal_basis_degrees": EPS,
        "strategy": STRATEGY,
    }


class Source:
    def __init__(self, label, source):
        self.label = label
        self.source = source
        self.directory = Path(source["directory"])
        self.files = {name: plain(entry) for name, entry in source["files"].items()}
        assert len(self.files) == SOURCE_COUNTS[label]
        assert all(name == entry["file"] for name, entry in self.files.items())
        for entry in self.files.values():
            bound(self.directory, entry)
        manifest = read(self.directory / MANIFEST)
        assert self.files[MANIFEST]["sha256"] == source["manifest_sha256"]
        entries = {entry["file"]: plain(entry) for entry in manifest["files"]}
        assert len(entries) == len(manifest["files"])
        for name, entry in self.files.items():
            if name != MANIFEST:
                assert entries[name] == entry, (label, name)
        initial, run, core = (read(self.directory / name) for name in META)
        assert initial["result"] == run["result"] == core["result"] == source["result"]
        assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
        assert str(run["workflow_run_id"]) == str(source["run_id"])
        assert initial["core_sha256"] == core["source_sha256"] == source["core_sha256"]
        assert run["process_exit_code"] == 0 and run["complete"] is True
        assert run["error"] is None and core["complete"] is True
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        self.certificate_spec = plain(source["certificate"])
        assert self.certificate_spec["file"] == CERTIFICATES[label]
        assert self.files[self.certificate_spec["file"]] == self.certificate_spec
        self.certificate = read(self.directory / self.certificate_spec["file"])
        assert self.certificate["result"] == source["result"]
        assert self.certificate["complete"] is True
        assert core["certificate_sha256"] == self.certificate_spec["sha256"]
        self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == source["core_sha256"]
        assert self.tag["result"] == source["result"]
        assert fingerprint(self.tag) == source["configuration_sha256"]

    def indexed(self, entry):
        entry = plain(entry)
        assert self.files[entry["file"]] == entry
        value = read(self.directory / entry["file"])
        assert value["complete"] is True
        assert value["configuration"] == self.tag
        return value

    def named(self, name):
        return self.indexed(self.files[name])


class Job:
    def __init__(self, args):
        self.args = args
        self.out = args.out
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        self.item = read(args.config)
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert self.item["producer_inputs_pending"] is False
        assert self.item["core_sha256"] == sha(__file__)
        assert set(self.item["sources"]) == set(SOURCE_COUNTS)
        assert set(self.item["proofs"]) == set(PROOF_KEYS)
        for entry in self.item["proofs"].values():
            assert sha(Path(entry["path"])) == entry["sha256"]
        assert sha(Path(self.item["method"])) == self.item["method_sha256"]
        self.tag = expected_tag(self.item)
        self.phase = "source_read"
        self.sources = {label: Source(label, self.item["sources"][label])
                        for label in sorted(SOURCE_COUNTS)}
        self.refs = {}
        self.group_refs = []
        self.prepare()

    def budget(self):
        if time.monotonic() - self.started >= max(1, 60 * self.args.budget_minutes - 10):
            raise BudgetStop("Completed source-bound stages retained; same tag resumes.")

    def path(self, name):
        assert name.startswith(PREFIX) and Path(name).name == name
        return self.out / (name if name.endswith(".json.gz") else name + ".json.gz")

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["configuration"] == self.tag
        assert value["result"] == RESULT and value["complete"] is True
        return value

    def store(self, name, value):
        path = self.path(name)
        assert not path.exists(), "Complete stages cannot be replaced."
        value = dict(value, result=RESULT, configuration=self.tag, complete=True)
        save(path, value)
        return spec(path)

    def completed(self, name):
        value = self.cached(name)
        assert value is not None
        return value, spec(self.path(name))

    def prepare(self):
        s805, s806, s853 = (self.sources[key] for key in ("R805", "R806", "R853"))
        c805, c806, c853 = (s.certificate for s in (s805, s806, s853))
        self.free_spec = plain(c805["graded_free_basis_stage"])
        free = s805.indexed(self.free_spec)
        pencil = s805.indexed(c805["pencil_stage"])
        assert c805["affine_free_module_rank"] == free["affine_free_module_rank"] == RANK
        assert c805["graded_free_basis_degrees"] == free["degree_distribution"] == [1, 144, 127]
        assert free["degree1_original_indices"] == list(range(2, 146))
        assert len(free["degree2_original_indices"]) == 127
        assert free["characteristic_zero_complement_certified"] is True
        assert free["graded_freeness_uses_original_R805_Koszul_proof"] is True
        assert pencil["n"] == c805["actual_pencil_n"] == 1
        assert pencil["basepoint_free_certified_by_actual_unit_minor"] is True
        assert c805["original_82_scales_preserved"] is True
        assert c806["normal_affine_basis_rank"] == RANK
        assert c806["normal_integral_basis_preserved"] is True
        assert c806["original_function_field_primitive_generator_certified"] is True
        assert c806["all272_columns_verified_in_all820_original_rows"] is True
        assert c806["actual_cyclic_minor_certified"] is True
        self.w_spec = plain(c806["polynomial_multiplier"])
        self.w = s806.indexed(self.w_spec)
        assert self.w["original_R805_free_basis"] == self.free_spec
        assert self.w["normal_affine_basis_degrees"] == EPS
        assert self.w["normal_affine_basis_rank"] == RANK
        assert self.w["matrix_convention"] == "M_ba(z) is output row b, input column a"
        assert self.w["normal_integral_basis_preserved"] is True
        assert self.w["all272_columns_verified_in_all820_original_rows"] is True
        assert self.w["all_weighted_support_zeros_verified"] is True
        assert self.w["original_function_field_primitive_generator_certified"] is True
        assert self.w["characteristic_zero_Krylov_matrix_or_inverse_computed"] is False
        assert self.w["coordinate_groups"] == c806["exact_coordinate_groups"]
        assert len(self.w["coordinate_groups"]) == GROUPS
        assert self.w["w0_original_M2_integer_coordinates"] == [str(int(i == 2)) for i in range(146)]
        assert c806["actual_w0_original_M2_integer_coordinates"] == self.w["w0_original_M2_integer_coordinates"]
        assert identity(s806.tag["retained_artifacts"]["R805"]) == identity(s805.source)
        assert s806.tag["actual_sigma_integer_n"] == 1
        self.mapping = self.w["S_row_to_polynomial_coefficient"]
        expected = [{"S_row": k, "normal_basis_row": b, "power_of_z": j}
                    for k, (b, j) in enumerate((b, j) for b in range(RANK)
                                               for j in range(4 - EPS[b]))]
        assert self.mapping == expected and len(self.mapping) == S3
        self.accepted_spec = plain(self.w["accepted_primitive_candidate"])
        accepted = s806.indexed(self.accepted_spec)
        self.witness_spec = plain(self.w["actual_cyclic_witness"])
        witness = s806.indexed(self.witness_spec)
        assert self.witness_spec == plain(accepted["cyclic_witness"])
        assert c806["actual_cyclic_minor"]["rank"] == RANK
        assert c806["actual_cyclic_minor"]["determinant_mod_prime"] != 0
        assert witness["complete"] is True
        self.coordinates_spec = plain(c853["three_conjugate_coordinates"])
        self.old_dag_spec = plain(c853["function_field_action_DAG"])
        coordinates = s853.indexed(self.coordinates_spec)
        old_dag = s853.indexed(self.old_dag_spec)
        s853.indexed(c853["source_audit"])
        assert coordinates["target_order"] == ["tau", "sigma", "w0"]
        assert coordinates["coordinate_matrix_shape"] == [146, 3]
        assert coordinates["full_verified_coordinate_count"] == 1680
        assert coordinates["all560_original_coordinates_verified_for_each_conjugate"] is True
        assert coordinates["twice_original_semilinear_action_verified_in_all560_coordinates"] is True
        assert coordinates["original_integer_scale"] == "6724"
        for i, row in enumerate(coordinates["coordinates_in_original_integer_scaled_V1_basis"]):
            assert row == [[str(int(i == 0)), "1"],
                           [str(int(i == 1) - int(i == 73)), "1"],
                           [str(int(i == 2)), "1"]]
        assert c853["original_three_V1_conjugates_certified"] is True
        assert c853["original_semilinear_function_field_generator_action_certified"] is True
        assert old_dag["original_normal_free_basis"] == self.free_spec
        assert old_dag["original_polynomial_multiplier_index"] == self.w_spec
        assert old_dag["exact_three_coordinates"] == self.coordinates_spec
        assert old_dag["three_Krylov_coordinate_solves_executed"] is False
        assert old_dag["source_K_Y_equals_K_z_w_certified_by_original_R806"] is True
        assert old_dag["original_arithmetic_twist_not_coefficient_conjugation_alone"] is True
        assert old_dag["all_three_normal_linear_transports_verified"] is True
        terms = [value["sparse_normal_polynomial_terms"] for value in old_dag["normal_expressions"]]
        assert terms == [
            [{"coefficient_Q": ["1", "1"], "normal_basis_row": 0, "power_of_z": 0}],
            [{"coefficient_Q": ["1", "1"], "normal_basis_row": 0, "power_of_z": 1},
             {"coefficient_Q": ["-2", "1"], "normal_basis_row": 72, "power_of_z": 0}],
            [{"coefficient_Q": ["1", "1"], "normal_basis_row": 1, "power_of_z": 0}],
        ]
        assert identity(s853.tag["sources"]["R806"]) == identity(s806.source)

    def source_audit(self):
        name = "R860-original-source-audit"
        old = self.cached(name)
        if old is None:
            self.refs["source_audit"] = self.store(name, {
                "source_identities": self.tag["sources"],
                "original_W": self.w_spec,
                "original_W_coordinate_groups": [plain(x) for x in self.w["coordinate_groups"]],
                "original_normal_free_basis": self.free_spec,
                "original_cyclic_witness": self.witness_spec,
                "original_three_conjugates": self.coordinates_spec,
                "original_semilinear_generator_DAG": self.old_dag_spec,
                "actual_original_w0": {"original_V1_index": 2, "normal_basis_index": 1},
                "actual_original_beta72": {"original_V1_index": 73, "normal_basis_index": 72},
                "actual_pencil_n": 1,
                "full_original_selected_member_count": 61,
                "all_selected_source_bytes_and_original_metadata_verified": True,
                "all_three_sources_use_same_original_normal_basis_and_W": True,
                "old_W_S3_cyclic_and_three_conjugates_recomputed": False,
            })
        else:
            assert old["source_identities"] == self.tag["sources"]
            self.refs["source_audit"] = spec(self.path(name))

    def source_group(self, group_number):
        name = "R860-original-W-group-" + str(group_number).zfill(3) + "-source-check"
        source = plain(self.w["coordinate_groups"][group_number])
        old = self.cached(name)
        first, stop = 8 * group_number, min(8 * (group_number + 1), RANK)
        if old is None:
            self.budget()
            group = self.sources["R806"].indexed(source)
            assert group["group"] == group_number
            assert group["column_indices"] == list(range(first, stop))
            assert group["basis_dimension"] == S3 and group["full_coordinate_rows"] == 820
            assert group["integer_scale"] == "304006671424"
            for flag in ("all820_original_coordinates_verified", "weighted_polynomial_support_verified",
                         "reduction_equals_successful_modular_multiplier"):
                assert group[flag] is True
            denominators = group["column_denominators"]
            assert len(denominators) == stop - first
            assert all(isinstance(x, str) and re.fullmatch(r"[1-9][0-9]*", x) for x in denominators)
            rows = group["coordinate_numerators"]
            assert len(rows) == S3 and all(len(row) == stop - first for row in rows)
            forced_zero_positions = 0
            for row, location in zip(rows, self.mapping):
                b, j = location["normal_basis_row"], location["power_of_z"]
                for local, value in enumerate(row):
                    assert isinstance(value, str) and re.fullmatch(r"-?(?:0|[1-9][0-9]*)", value)
                    if j > 1 + EPS[first + local] - EPS[b]:
                        assert value == "0"
                        forced_zero_positions += 1
            answer = self.store(name, {
                "source_original_group": source,
                "source_original_multiplier": self.w_spec,
                "source_audit": self.refs["source_audit"],
                "group": group_number,
                "column_indices": list(range(first, stop)),
                "normal_basis_rank": RANK,
                "original_coordinate_shape": [S3, stop - first],
                "original_column_denominators_positive": True,
                "all_weighted_forced_zero_positions_checked": True,
                "actual_forced_zero_position_count": forced_zero_positions,
                "original_full820_certificate_consumed_not_recomputed": True,
                "original_scale_reapplied": False,
                "all_rational_coefficients_remain_in_original_source_bytes": True,
            })
            del group, rows
            return answer
        assert old["source_original_group"] == source
        assert old["column_indices"] == list(range(first, stop))
        assert old["source_audit"] == self.refs["source_audit"]
        return spec(self.path(name))

    def coefficient_index(self):
        name = "R860-original-W-coefficient-source-index"
        old = self.cached(name)
        if old is not None:
            assert old["source_group_checks"] == self.group_refs
            self.refs["coefficient_source_index"] = spec(self.path(name))
            return
        column_locations = [
            {"normal_input_column": column, "source_group": column // 8,
             "local_column": column % 8}
            for column in range(RANK)
        ]
        self.refs["coefficient_source_index"] = self.store(name, {
            "source_audit": self.refs["source_audit"],
            "source_group_checks": self.group_refs,
            "source_original_R806_producer": identity(self.sources["R806"].source),
            "source_original_multiplier": self.w_spec,
            "source_exact_coordinate_groups": [plain(x) for x in self.w["coordinate_groups"]],
            "normal_basis_rank": RANK, "normal_basis_degrees": EPS,
            "matrix_convention": STRATEGY["matrix_convention"],
            "S_row_to_polynomial_coefficient": self.mapping,
            "normal_column_source_locations": column_locations,
            "coefficient_rule": {
                "numerator_field": "coordinate_numerators",
                "numerator_indices": ["S_row", "local_column"],
                "denominator_field": "column_denominators",
                "denominator_index": "local_column",
                "power_variable": "z",
                "coefficient_Q": "numerator/denominator",
                "additional_scale": [1, 1],
            },
            "missing_polynomial_powers_mean_exact_zero": True,
            "original_weighted_support_checked_in_all_groups": True,
            "complete_original_coefficient_sources_retained": True,
        })

    def program(self):
        name = "R860-original-semilinear-resolvent-expression-DAG"
        old = self.cached(name)
        if old is not None:
            assert old["coefficient_source_index"] == self.refs["coefficient_source_index"]
            self.refs["expression_DAG"] = spec(self.path(name))
            return
        self.budget()
        nodes = []

        def node(identifier, operation, value_type, inputs=(), **data):
            known = {entry["id"] for entry in nodes}
            assert identifier not in known and all(x in known for x in inputs)
            nodes.append(dict(id=identifier, operation=operation, value_type=value_type,
                              inputs=list(inputs), **data))
            return identifier

        node("z", "original_affine_coordinate", "K(Y)", expression="sigma/tau")
        node("w", "original_primitive_function", "K(Y)", expression="e2/tau",
             source_original_multiplier=self.w_spec,
             source_original_cyclic_witness=self.witness_spec)
        node("s", "original_constant_field_generator", "K", minimal_polynomial=[3, 0, 1])
        node("T", "independent_polynomial_variable", "Q[z,T]")
        node("W", "source_polynomial_matrix", "Mat272(Q[z])",
             coefficient_source_index=self.refs["coefficient_source_index"],
             normal_basis_degrees=EPS, matrix_convention=STRATEGY["matrix_convention"])
        node("TI", "scalar_identity_matrix", "Mat272(Q[z,T])", ["T"], rank=RANK)
        node("A", "matrix_subtract", "Mat272(Q[z,T])", ["TI", "W"])
        node("chi", "determinant", "Q[z,T]", ["A"], matrix_size=RANK,
             expanded=False, T_degree=RANK, monic_in_T=True, total_degree_bound=RANK)
        for label, deleted_row, total_degree, T_degree in (
                ("D", 0, 271, 271), ("N", TARGET, 272, 270)):
            kept_rows = [i for i in range(RANK) if i != deleted_row]
            kept_columns = list(range(1, RANK))
            assert len(kept_rows) == len(kept_columns) == 271
            node(label + "_matrix", "matrix_minor", "Mat271(Q[z,T])", ["A"],
                 deleted_row=deleted_row, deleted_column=0,
                 retained_rows=kept_rows, retained_columns=kept_columns,
                 source_adjugate_entry=[0, deleted_row], cofactor_sign=1)
            node(label, "determinant", "Q[z,T]", [label + "_matrix"], matrix_size=271,
                 expanded=False, T_degree_bound=T_degree, total_degree_bound=total_degree,
                 leading_T_coefficient=1 if label == "D" else None,
                 degree_bound_from_original_weighted_entries=True)
            node(label + "_at_w", "evaluate_T_at_original_primitive_w", "K(Y)", [label, "w"])
        denominator_proof = {
            "id": "original_D_at_w_nonzero",
            "function_node": "D_at_w",
            "reason": "D_monic_T271_and_chi_original_irreducible_T272",
            "source_original_R806_certificate": self.sources["R806"].certificate_spec,
            "source_original_cyclic_witness": self.witness_spec,
            "source_original_W": self.w_spec,
            "proof_sha256": self.item["proofs"]["R860"]["sha256"],
            "function_field_nonzero_not_every_fiber_unit": True,
        }
        node("r", "function_division", "K(Y)", ["N_at_w", "D_at_w"],
             nonzero_denominator_proof=denominator_proof["id"],
             actual_original_normal_basis_index=TARGET,
             original_normal_basis_vector=[0] * TARGET + [1] + [0] * (RANK - TARGET - 1))
        node("minus_two_r", "integer_scalar_multiply", "K(Y)", ["r"], scalar=-2)
        node("cY_z", "function_add", "K(Y)", ["z", "minus_two_r"])
        node("cY_w", "identity", "K(Y)", ["w"])
        node("cY_s", "integer_scalar_multiply", "K", ["s"], scalar=-1)
        node("cY_r", "integer_scalar_multiply", "K(Y)", ["r"], scalar=-1)
        node("nu", "original_rational_differential", "Omega1(K(Y)/K)",
             original_Tate_expression="82*tau*dqY/qY",
             original_global_expression="dz/g; g=delta(z)",
             proof_sources={key: self.item["proofs"][key]["sha256"]
                            for key in ("R802", "R813", "R853", "R860")})
        node("cY_nu", "identity", "Omega1(K(Y)/K)", ["nu"])
        outputs = {"original_beta72_fraction": "r", "c_Y_z": "cY_z",
                   "c_Y_w": "cY_w", "c_Y_s": "cY_s", "c_Y_beta72": "cY_r",
                   "original_rational_differential": "nu", "c_Y_nu": "cY_nu"}
        assert len({entry["id"] for entry in nodes}) == len(nodes)
        self.refs["expression_DAG"] = self.store(name, {
            "source_audit": self.refs["source_audit"],
            "coefficient_source_index": self.refs["coefficient_source_index"],
            "nodes": nodes, "outputs": outputs,
            "nonzero_proofs": [denominator_proof],
            "source_original_three_conjugates": self.coordinates_spec,
            "source_original_semilinear_generator_DAG": self.old_dag_spec,
            "source_original_normal_free_basis": self.free_spec,
            "normal_to_function_template": {
                "input": "actual_original_normal_vector_v_with_its_full_source",
                "bordered_matrix": "[[T*I-W,v],[e0_transpose,0]]",
                "numerator": "negative_determinant_of_bordered_matrix",
                "denominator_node": "D_at_w",
                "substitute_T": "original_w",
                "rational_input_denominators_retained": True,
                "new_template_instances_computed": 0,
            },
            "semilinear_substitution": {
                "constants": {"Q": "fixed", "s": "-s", "zeta": "-1-zeta"},
                "z_node": "cY_z", "w_node": "cY_w",
                "is_original_arithmetic_twist": True,
                "source_involution": self.coordinates_spec,
                "original_tau_affine_chart_stable": True,
                "original_sigma_affine_chart_assumed_stable": False,
            },
            "differential_descent": {
                "original_D0_qY_factor": [1, 82],
                "c_Y_tau_equals_tau_source": self.coordinates_spec,
                "qY_action": "qY_maps_to_minus_qY",
                "original_even_weight_T41_automorphy_factor": 1,
                "c_Y_delta_equals_delta_c_Y": True,
                "c_Y_nu_equals_nu": True,
                "FM27_comparison_factor": [1, 1],
                "c_Y_h_equals_h": True,
                "c_Y_g": "g-2*delta(original_beta72)",
                "general_Gamma_or_new_connection_computed": False,
            },
            "normal_ring_kept_as_original_complete_normal_ring": True,
            "K_z_w_assumed_integrally_closed": False,
            "all_original_W_coefficients_source_complete": True,
            "exact_original_semilinear_fraction_DAG_constructed": True,
            "expanded_bivariate_cofactors_computed": False,
            "expanded_power_basis_coordinates_computed": False,
            "characteristic_zero_Krylov_matrix_or_inverse_computed": False,
            "new_full_normal_semilinear_matrix_computed": False,
            "actual_RR_kernel_connection_period_or_height_computed": False,
        })

    def inventory(self):
        files = []
        for path in sorted(self.out.glob(PREFIX + "*.json.gz")):
            if path.name == "R860-current.json.gz" or path.name.startswith("R860-stage-manifest-"):
                continue
            value = read(path)
            assert value["configuration"] == self.tag and value["result"] == RESULT
            assert value["complete"] is True
            files.append(spec(path))
        name = "R860-stage-manifest-" + fingerprint(files)[:20]
        old = self.cached(name)
        if old is None:
            return self.store(name, {"files": files, "actual_complete_stage_count": len(files),
                                     "current_checkpoint_excluded": True})
        assert old["files"] == files
        return spec(self.path(name))

    def finish(self, complete, reason, error=None):
        current = {
            "result": RESULT, "configuration": self.tag, "complete": False,
            "current_phase": self.phase,
            "completed_group_checks": self.group_refs,
            "completed_source_and_expression_stages": self.refs,
            "historical_false_FINAL_does_not_lock_current_inventory": True,
        }
        save(self.path("R860-current"), current)
        inventory = self.inventory()
        answer = {
            "result": RESULT, "configuration": self.tag, "complete": complete, "p": 41,
            "completed_scope": STRATEGY["scope"] if complete else "partial_source_or_expression",
            "source_audit": self.refs.get("source_audit"),
            "coefficient_source_index": self.refs.get("coefficient_source_index"),
            "exact_expression_DAG": self.refs.get("expression_DAG"),
            "completed_original_W_group_checks": self.group_refs,
            "actual_original_W_group_count": len(self.group_refs),
            "original_normal_basis_rank": RANK,
            "original_target_normal_basis_index": TARGET,
            "exact_original_semilinear_fraction_DAG_constructed": complete,
            "original_delta_and_nu_fixed_descent_source_bound": complete,
            "expanded_bivariate_cofactors_computed": False,
            "expanded_power_basis_coordinates_computed": False,
            "characteristic_zero_Krylov_matrix_or_inverse_computed": False,
            "new_full_normal_semilinear_matrix_computed": False,
            "actual_RR_kernel_connection_period_or_height_computed": False,
            "old_mathematical_source_arithmetic_recomputed": False,
            "stage_manifest": inventory,
            "resume_state": spec(self.path("R860-current")),
            "stop_reason": reason, "error": error,
            "seconds": time.monotonic() - self.started,
        }
        save(self.out / FINAL, answer)
        return answer

    def run(self):
        self.phase = "source_audit"
        self.source_audit()
        for group in range(GROUPS):
            self.phase = "original_W_group_" + str(group).zfill(3)
            self.group_refs.append(self.source_group(group))
        self.phase = "coefficient_source_index"
        self.budget()
        self.coefficient_index()
        self.phase = "exact_semilinear_resolvent_expression"
        self.program()
        self.phase = "completed"
        return self.finish(True, "exact_original_semilinear_fraction_DAG_constructed")


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematical consumers run only in the public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    started, job, answer, error = time.monotonic(), None, None, None
    code = 1
    try:
        job = Job(args)
        answer = job.run()
        code = 0
    except BudgetStop as exc:
        code, error = 124, str(exc)
        if job is not None:
            answer = job.finish(False, "BudgetStop", error)
        traceback.print_exc()
    except Exception as exc:
        error = type(exc).__name__ + ": " + str(exc)
        traceback.print_exc()
        if job is not None:
            try:
                answer = job.finish(False, "error", error)
            except Exception:
                traceback.print_exc()
    receipt = {
        "result": RESULT, "source_sha256": sha(__file__), "p": 41,
        "complete": code == 0, "process_exit_code": code, "error": error,
        "stop_reason": answer["stop_reason"] if answer else "initialization_error",
        "certificate_sha256": sha(args.out / FINAL) if (args.out / FINAL).exists() else None,
        "stage_manifest": answer["stage_manifest"] if answer else None,
        "exact_original_semilinear_fraction_DAG_constructed": code == 0,
        "expanded_bivariate_cofactors_computed": False,
        "expanded_power_basis_coordinates_computed": False,
        "actual_RR_kernel_connection_period_or_height_computed": False,
        "seconds": time.monotonic() - started,
    }
    save(args.out / "core-receipt.json", receipt)
    print("R860_CORE_RESULT=" + json.dumps(receipt, sort_keys=True), flush=True)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
