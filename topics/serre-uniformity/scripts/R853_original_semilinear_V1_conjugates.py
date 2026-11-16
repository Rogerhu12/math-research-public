#!/usr/bin/env python3
"""Three original V1 conjugates; all new mathematics only in public Actions."""

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

import flint
from flint import fmpq, fmpq_mat


RESULT = "R853-original-semilinear-V1-generator-conjugates"
FINAL = "p41-original-semilinear-V1-conjugates-certificate.json"
PREFIX = "R853-"
INVENTORY = "R853-stage-manifest.json.gz"
BASE_KEYS = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
PROOFS = ("proof", "descent_proof", "affine_proof", "method")
H64 = re.compile(r"[0-9a-f]{64}")
DIM = 146
ORDERS = 14
XI = 40
ROWS = ORDERS * XI
EPS = [0] + [1] * 144 + [2] * 127
TARGETS = ("tau", "sigma", "w0")
MINOR = "R837-original-V1-reflection-minor.json.gz"
ACCEPTED = "R806-accepted-primitive-candidate.json.gz"
MULTIPLIER = "R806-exact-polynomial-multiplier-in-original-normal-basis.json.gz"
FREE_BASIS = {
    "file": "R805-graded-free-basis.json.gz", "bytes": 11649,
    "sha256": "74311a7a143fafc43a36d1a43f6146e6aa3cb28809a020e3fa1337fdc4e475c9",
}
DEFINITIONS = {
    "R786": {
        "result": "R786-exact-original-power5-short-basis",
        "core_sha256": "4508095a95a2bcaec8c8db8fcd550fbc618b017d2bc0007945783bc109dbf851",
        "certificate": "p41-exact-original-power5-short-basis-certificate.json",
        "stage_manifest": "R786-exact-stages-manifest.json.gz",
    },
    "R837": {
        "result": "R837-original-fixed-branch-pencil",
        "core_sha256": "5702b42ee014ab7552e61383e24b738fe5ed48955dfc207ad3d85cae08e8b924",
        "certificate": "p41-original-fixed-branch-pencil-certificate.json",
        "stage_manifest": "R837-stage-manifest.json.gz",
    },
    "R806": {
        "result": "R806-original-primitive-multiplication",
        "core_sha256": "b014f9b3cb4923421e6a879eddb4da58dd0baefb28d61a2191f6b0a33e51810d",
        "certificate": "p41-original-primitive-multiplication-certificate.json",
        "stage_manifest": "R806-stage-manifest.json.gz",
    },
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if path.suffix == ".gz":
        with temporary.open("wb") as stream:
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb", mtime=0, compresslevel=2) as out:
                out.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def plain(value):
    answer = {key: value[key] for key in ("file", "bytes", "sha256")}
    assert Path(answer["file"]).name == answer["file"] and "\\" not in answer["file"]
    assert answer["file"] not in (".", "..")
    assert isinstance(answer["bytes"], int) and answer["bytes"] >= 0
    assert H64.fullmatch(answer["sha256"])
    return answer


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def qencode(value):
    value = fmpq(value)
    return [str(value.numer()), str(value.denom())]


def qdecode(value):
    assert isinstance(value, list) and len(value) == 2
    assert int(value[1]) > 0
    return fmpq(int(value[0]), int(value[1]))


class BudgetStop(RuntimeError):
    pass


class Source:
    def __init__(self, label, item):
        self.label = label
        self.directory = Path(item["directory"])
        definition = DEFINITIONS[label]
        self.identity = {key: item[key] for key in BASE_KEYS}
        assert self.identity["result"] == definition["result"]
        assert self.identity["core_sha256"] == definition["core_sha256"]
        self.files = {name: plain(row) for name, row in item["files"].items()}
        assert all(name == row["file"] for name, row in self.files.items())
        selected_hash = fingerprint([self.files[name] for name in sorted(self.files)])
        assert selected_hash == item["selected_files_sha256"]
        for row in self.files.values():
            path = self.directory / row["file"]
            assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
        assert "full-outputs-manifest.json" in self.files
        assert self.files["full-outputs-manifest.json"]["sha256"] == self.identity["manifest_sha256"]
        full = read(self.directory / "full-outputs-manifest.json")
        assert full["result"] == self.identity["result"]
        full_files = {row["file"]: plain(row) for row in full["files"]}
        assert len(full_files) == len(full["files"])
        self.full_files = full_files
        for name, row in self.files.items():
            if name != "full-outputs-manifest.json":
                assert full_files[name] == row
        self.certificate_spec = plain(item["certificate"])
        self.stage_manifest_spec = plain(item["stage_manifest"])
        assert self.certificate_spec["file"] == definition["certificate"]
        assert self.stage_manifest_spec["file"] == definition["stage_manifest"]
        assert self.files[self.certificate_spec["file"]] == self.certificate_spec
        assert self.files[self.stage_manifest_spec["file"]] == self.stage_manifest_spec
        self.certificate = read(self.directory / self.certificate_spec["file"])
        assert self.certificate["complete"] is True
        assert self.certificate["result"] == self.identity["result"]
        self.tag = self.certificate["configuration"]
        self.tag_hash = fingerprint(self.tag)
        assert self.tag_hash == item["configuration_sha256"]
        assert self.tag["result"] == self.identity["result"]
        assert self.tag["source_sha256"] == self.identity["core_sha256"]
        manifest = read(self.directory / self.stage_manifest_spec["file"])
        assert manifest["complete"] is True and manifest["configuration"] == self.tag
        self.stages = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(self.stages) == len(manifest["files"])
        initial = read(self.directory / "public-actions-input.json")
        run = read(self.directory / "run-receipt.json")
        core = read(self.directory / "core-receipt.json")
        for data in (initial, run, core):
            assert data["result"] == self.identity["result"]
        assert initial["source_commit"] == run["source_commit"] == self.identity["source_commit"]
        assert initial["core_sha256"] == core["source_sha256"] == self.identity["core_sha256"]
        assert str(run["workflow_run_id"]) == str(self.identity["run_id"])
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert core["complete"] is True
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        assert core["certificate_sha256"] == self.certificate_spec["sha256"]
        self.bound_identity = dict(self.identity,
            configuration_sha256=self.tag_hash,
            selected_files_sha256=selected_hash,
            selected_file_count=len(self.files),
            certificate=self.certificate_spec,
            stage_manifest=self.stage_manifest_spec)

    def stage(self, name):
        assert self.files[name] == self.stages[name]
        value = read(self.directory / name)
        assert value["complete"] is True and value["configuration"] == self.tag
        assert value.get("result", self.tag["result"]) == self.identity["result"]
        return value

    def spec(self, name):
        return self.files[name]


class Job:
    def __init__(self, args):
        self.args = args
        self.started = time.monotonic()
        self.deadline = self.started + args.budget_minutes * 60
        self.out = Path(args.out)
        self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert self.item["producer_inputs_pending"] is False
        assert self.item["core"] == Path(__file__).name
        assert self.item["core_sha256"] == sha(__file__)
        assert 0 < args.budget_minutes <= 300
        assert flint.__version__ == "0.9.0"
        for key in PROOFS:
            assert sha(self.item[key]) == self.item[key + "_sha256"]
        assert set(self.item["sources"]) == set(DEFINITIONS)
        self.sources = {label: Source(label, self.item["sources"][label]) for label in sorted(DEFINITIONS)}
        self.r786, self.r837, self.r806 = (self.sources[label] for label in ("R786", "R837", "R806"))
        for old in (self.r837.tag["sources"]["R786"], self.r806.tag["retained_artifacts"]["R786"]):
            assert {key: old[key] for key in BASE_KEYS} == self.r786.identity
        assert self.r806.tag["original_tau_index"] == 0
        assert self.r806.tag["actual_sigma_integer_n"] == 1
        assert self.r806.tag["normal_affine_basis_degrees"] == EPS
        assert self.r806.tag["R805_proof_sha256"] == self.item["affine_proof_sha256"]
        self.accepted = self.r806.stage(ACCEPTED)
        assert self.r806.certificate["accepted_candidate"] == self.r806.spec(ACCEPTED)
        self.definition_spec = plain(self.accepted["candidate_definition"])
        self.definition = self.r806.stage(self.definition_spec["file"])
        assert self.r806.spec(self.definition_spec["file"]) == self.definition_spec
        assert self.definition["recipe"] == {"kind": "original_M2", "index": 2}
        expected_w = [int(i == 2) for i in range(DIM)]
        for data in (self.definition, self.accepted):
            assert [int(x) for x in data["w0_original_M2_integer_coordinates"]] == expected_w
        assert [int(x) for x in self.r806.certificate["actual_w0_original_M2_integer_coordinates"]] == expected_w
        assert self.definition["original_integer_scale"] == "6724"
        assert self.definition["membership_in_original_V1_by_generation"] is True
        assert self.accepted["original_function_field_primitive_generator_certified"] is True
        assert self.r806.certificate["original_function_field_primitive_generator_certified"] is True
        self.multiplier = self.r806.stage(MULTIPLIER)
        assert self.r806.certificate["polynomial_multiplier"] == self.r806.spec(MULTIPLIER)
        assert plain(self.multiplier["original_R805_free_basis"]) == FREE_BASIS
        assert self.multiplier["normal_affine_basis_degrees"] == EPS
        assert self.multiplier["all272_columns_verified_in_all820_original_rows"] is True
        self.w_groups = [plain(row) for row in self.multiplier["coordinate_groups"]]
        assert len(self.w_groups) == 34
        for row in self.w_groups:
            assert self.r806.stages[row["file"]] == self.r806.full_files[row["file"]] == row
        self.cyclic_spec = plain(self.accepted["cyclic_witness"])
        assert self.r806.stages[self.cyclic_spec["file"]] == self.r806.full_files[self.cyclic_spec["file"]] == self.cyclic_spec
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__, "p": 41,
            **{key + "_sha256": self.item[key + "_sha256"] for key in PROOFS},
            "sources": {label: self.sources[label].bound_identity for label in sorted(self.sources)},
            "original_V1_dimension": DIM, "original_qY_prefix_orders": ORDERS,
            "original_xi_coordinates_per_order": XI, "full_original_coordinate_rows": ROWS,
            "original_V1_integer_scale": "6724", "target_order": list(TARGETS),
            "original_tau_index": 0, "actual_sigma_integer_n": 1, "actual_w0_index": 2,
            "original_coefficient_field": "K=Q(s),s**2=-3;zeta=(-1+s)/2",
            "coefficient_c0_action": "s->-s,xi41->xi41; original integer xi coefficients fixed",
            "geometric_twist_action": "qY->-qY, even-weight automorphy factor1",
            "matrix_convention": "row40*n+r, original V1 column i; A*C=sign(n)*A*V",
            "original_normal_free_basis": FREE_BASIS,
            "normal_basis_degrees": EPS,
            "new_exact_right_hand_side_count": 3,
            "old_reflection_minor_recomputed": False,
            "old_Fourier_or_CM_values_recomputed": False,
            "full_normal_involution_matrix_computed": False,
            "budget_and_absolute_directories_excluded_from_mathematical_identity": True,
        }
        self.A = None
        self.prefix_sources = []
        self.selected = None
        self.minor = None
        self.audit_spec = None
        self.coordinate_spec = None
        self.dag_spec = None

    def check(self):
        if time.monotonic() >= self.deadline:
            raise BudgetStop("R853 budget reached; complete original-source stages retained")

    def path(self, name):
        if not name.endswith(".json.gz"):
            name += ".json.gz"
        assert Path(name).name == name and name.startswith(PREFIX)
        return self.out / name

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["configuration"] == self.tag and value["complete"] is True
        assert value.get("result", self.tag["result"]) == RESULT
        return value

    def put(self, name, data):
        path = self.path(name)
        assert not path.exists(), "A completed mathematical stage must not be replaced"
        value = dict(data, result=RESULT, configuration=self.tag, complete=True)
        save(path, value)
        print("R853_STAGE=" + json.dumps(spec(path), sort_keys=True), flush=True)
        return value

    def output_spec(self, name):
        return spec(self.path(name))

    def target(self, row, target):
        if target == 0:
            return row[0]
        if target == 1:
            return row[1] + row[73]
        assert target == 2
        return row[2]

    def load_prefix(self):
        columns = []
        sources = []
        for i in range(DIM):
            self.check()
            name = "R786-exact-power-1-row-" + str(i).zfill(4) + ".json.gz"
            data = self.r786.stage(name)
            assert data["weight"] == 2 and data["bound_qY"] == 128
            assert data["integer_scale"] == "6724"
            assert data["original_R775_finite_coefficients_verified"] is True
            assert data["recipe"]["kind"] == "det_semilinear_E1_pair_trace"
            assert data["recipe"]["exact_global_field"] == "K"
            coefficients = data["integer_qY_xi_coefficients"]
            assert len(coefficients) == 129 and all(len(row) == XI for row in coefficients)
            column = [int(coefficients[n][r]) for n in range(ORDERS) for r in range(XI)]
            assert len(column) == ROWS
            columns.append(column)
            sources.append(self.r786.spec(name))
        self.A = [[columns[i][r] for i in range(DIM)] for r in range(ROWS)]
        self.prefix_sources = sources
        self.minor = self.r837.stage(MINOR)
        assert self.minor["matrix_shape"] == [ROWS, DIM]
        assert self.minor["actual_modular_rank"] == self.minor["expected_characteristic_zero_rank"] == DIM
        assert self.minor["selected_columns"] == list(range(DIM))
        assert self.minor["minor_determinant_mod_prime"] != 0
        self.selected = self.minor["selected_rows"]
        assert len(self.selected) == DIM and len(set(self.selected)) == DIM
        assert all(isinstance(i, int) and 0 <= i < ROWS for i in self.selected)
        attempt_spec = plain(self.minor["successful_attempt"])
        attempt = self.r837.stage(attempt_spec["file"])
        assert self.r837.spec(attempt_spec["file"]) == attempt_spec
        for key in ("matrix_shape", "actual_modular_rank", "selected_rows", "selected_columns",
                    "prime", "prime_index", "minor_determinant_mod_prime"):
            assert attempt[key] == self.minor[key]

    def source_audit(self):
        name = "R853-original-V1-prefix-and-source-audit"
        old = self.cached(name)
        if old is None:
            self.check()
            old = self.put(name, {
                "original_R786_prefix_rows": self.prefix_sources,
                "original_reflection_minor": self.r837.spec(MINOR),
                "original_reflection_successful_attempt": self.minor["successful_attempt"],
                "selected_original_prefix_rows": self.selected,
                "original_minor_prime": self.minor["prime"],
                "original_minor_determinant_mod_prime": self.minor["minor_determinant_mod_prime"],
                "original_primitive_candidate": self.r806.spec(ACCEPTED),
                "original_primitive_definition": self.definition_spec,
                "original_polynomial_multiplier_index": self.r806.spec(MULTIPLIER),
                "original_normal_free_basis": FREE_BASIS,
                "prefix_matrix_shape": [ROWS, DIM],
                "qY_prefix_orders": ORDERS, "xi_coordinates_per_order": XI,
                "three_target_original_V1_terms": {
                    "tau": [[0, 1]], "sigma": [[1, 1], [73, 1]], "w0": [[2, 1]],
                },
                "all_selected_source_bytes_and_original_configurations_verified": True,
                "all_three_producers_share_the_same_original_R786_source": True,
                "original_rank_or_minor_arithmetic_recomputed": False,
                "original_CM_values_or_reflected_P0_values_recomputed": False,
                "actual_original_w0_not_assumed_from_candidate_number": True,
            })
        assert old["original_R786_prefix_rows"] == self.prefix_sources
        assert old["original_reflection_minor"] == self.r837.spec(MINOR)
        assert old["selected_original_prefix_rows"] == self.selected
        self.audit_spec = self.output_spec(name)

    def coordinates(self):
        name = "R853-three-exact-original-V1-conjugates"
        old = self.cached(name)
        if old is None:
            self.check()
            square = fmpq_mat([self.A[i] for i in self.selected])
            selected_rhs = [[((-1) ** (r // XI)) * self.target(self.A[r], j)
                             for j in range(3)] for r in self.selected]
            rhs = fmpq_mat(selected_rhs)
            coordinates = square.solve(rhs)
            assert square * coordinates == rhs
            original = fmpq_mat(self.A)
            full_rhs = [[((-1) ** (r // XI)) * self.target(self.A[r], j)
                         for j in range(3)] for r in range(ROWS)]
            recovered = original * coordinates
            assert recovered == fmpq_mat(full_rhs)
            # This uses the just computed full image, not a second solve or a new reflection table.
            for r in range(ROWS):
                sign = (-1) ** (r // XI)
                for j in range(3):
                    assert sign * recovered[r, j] == self.target(self.A[r], j)
            for j in range(3):
                assert any(coordinates[i, j] for i in range(DIM))
            old = self.put(name, {
                "source_audit": self.audit_spec,
                "source_original_reflection_minor": self.r837.spec(MINOR),
                "original_R786_prefix_rows": self.prefix_sources,
                "original_selected_rows": self.selected,
                "target_order": list(TARGETS), "coordinate_matrix_shape": [DIM, 3],
                "coordinates_in_original_integer_scaled_V1_basis": [
                    [qencode(coordinates[i, j]) for j in range(3)] for i in range(DIM)],
                "original_integer_scale": "6724",
                "coefficient_field_of_saved_coordinates": "Q; obtained by the exact rational selected-row solve",
                "selected_system_shape": [DIM, DIM], "new_right_hand_side_count": 3,
                "all560_original_coordinates_verified_for_each_conjugate": True,
                "full_verified_coordinate_count": ROWS * 3,
                "all_three_original_conjugates_nonzero": True,
                "twice_original_semilinear_action_verified_in_all560_coordinates": True,
                "complete_global_identity_reason": "R802 arithmetic action and original V1 injectivity of14 full coefficients",
                "old_source_prefixes_or_original_reflection_rank_recomputed": False,
                "full146_column_conjugation_matrix_computed": False,
            })
        assert old["source_audit"] == self.audit_spec
        assert old["source_original_reflection_minor"] == self.r837.spec(MINOR)
        assert old["original_R786_prefix_rows"] == self.prefix_sources
        assert old["target_order"] == list(TARGETS)
        assert old["all560_original_coordinates_verified_for_each_conjugate"] is True
        assert old["twice_original_semilinear_action_verified_in_all560_coordinates"] is True
        raw = old["coordinates_in_original_integer_scaled_V1_basis"]
        assert len(raw) == DIM and all(len(row) == 3 for row in raw)
        self.coordinate_spec = self.output_spec(name)
        return [[qdecode(raw[i][j]) for i in range(DIM)] for j in range(3)]

    def function_dag(self, columns):
        name = "R853-original-semilinear-function-field-generator-DAG"
        old = self.cached(name)
        if old is None:
            self.check()
            normal = []
            for target, column in zip(TARGETS, columns):
                # Only degree0/degree1 rows occur.  The degree2 rows stay zero.
                table = [[fmpq(0), fmpq(0)] for unused in range(272)]
                table[0] = [column[0], column[1]]
                for i in range(2, DIM):
                    table[i - 1][0] = column[i]
                table[72][0] -= column[1]
                recovered = [fmpq(0)] * DIM
                recovered[0], recovered[1] = table[0]
                for i in range(2, DIM):
                    recovered[i] = table[i - 1][0]
                recovered[73] += table[0][1]
                assert recovered == column
                assert all(table[i] == [0, 0] for i in range(145, 272))
                assert all(table[i][1] == 0 for i in range(1, 272))
                terms = [{"normal_basis_row": i, "power_of_z": power, "coefficient_Q": qencode(value)}
                         for i, pair in enumerate(table) for power, value in enumerate(pair) if value]
                assert terms
                normal.append({
                    "target": target,
                    "function": "c_Y(" + target + ")/original_tau",
                    "normal_basis_rank": 272, "original_normal_free_basis": FREE_BASIS,
                    "sparse_normal_polynomial_terms": terms,
                    "exact_reconstruction_in_original_V1_basis_verified": True,
                    "extra_section_or_integer_scale_inserted": False,
                })
            nodes = [{"id": "section_" + target, "operation": "original_V1_linear_combination",
                      "coordinate_stage": self.coordinate_spec, "coordinate_column": j,
                      "original_integer_scale": "6724"}
                     for j, target in enumerate(TARGETS)]
            nodes += [{"id": "normal_" + target, "operation": "divide_original_section_by_original_tau",
                       "section": "section_" + target, "exact_normal_expression_index": j}
                      for j, target in enumerate(TARGETS)]
            nodes += [
                {"id": "original_W", "operation": "external_certified_original_polynomial_multiplier",
                 "producer": self.r806.identity, "index": self.r806.spec(MULTIPLIER),
                 "exact_coordinate_groups": self.w_groups,
                 "entry_rule": self.multiplier["exact_entry_rule"],
                 "normal_basis_rank": 272, "original_normal_free_basis": FREE_BASIS},
                {"id": "original_Krylov", "operation": "original_cyclic_columns",
                 "multiplier": "original_W", "unit_basis_row": 0, "powers": [0, 271],
                 "original_nonzero_cyclic_witness": self.cyclic_spec},
            ]
            for target in TARGETS:
                nodes.append({"id": "power_coordinates_" + target, "operation": "unit_matrix_solve",
                              "matrix": "original_Krylov", "right_hand_side": "normal_" + target,
                              "coefficient_field": "K(z)", "evaluation_deferred": True})
                nodes.append({"id": "function_" + target, "operation": "polynomial_in_original_w",
                              "coefficient_vector": "power_coordinates_" + target,
                              "powers": [0, 271], "variable": "w=original_e2/original_tau"})
            nodes += [
                {"id": "arithmetic_conjugate_z", "operation": "field_division",
                 "numerator": "function_sigma", "denominator": "function_tau"},
                {"id": "arithmetic_conjugate_w", "operation": "field_division",
                 "numerator": "function_w0", "denominator": "function_tau"},
            ]
            old = self.put(name, {
                "source_audit": self.audit_spec, "exact_three_coordinates": self.coordinate_spec,
                "original_primitive_definition": self.definition_spec,
                "original_polynomial_multiplier_index": self.r806.spec(MULTIPLIER),
                "original_normal_free_basis": FREE_BASIS,
                "normal_expressions": normal, "nodes": nodes,
                "outputs": {"c_Y_z": "arithmetic_conjugate_z", "c_Y_w": "arithmetic_conjugate_w"},
                "constant_field_action": {"s": "-s", "zeta": "-1-zeta", "rationals": "fixed"},
                "denominator_nonzero_proof": {
                    "function": "normal_tau", "reason": "nonzero original tau under the actual R802 field involution",
                    "exact_coordinate_stage": self.coordinate_spec,
                },
                "entire_original_function_field_action_defined": True,
                "original_arithmetic_twist_not_coefficient_conjugation_alone": True,
                "source_K_Y_equals_K_z_w_certified_by_original_R806": True,
                "all_three_normal_linear_transports_verified": True,
                "three_K_z_w_unit_solve_expressions_source_bound": True,
                "three_Krylov_coordinate_solves_executed": False,
                "full272_column_involution_matrix_computed": False,
                "Krylov_coordinate_or_multiplier_arithmetic_recomputed": False,
                "new_RR_spaces_connections_periods_or_heights_computed": False,
            })
        assert old["source_audit"] == self.audit_spec
        assert old["exact_three_coordinates"] == self.coordinate_spec
        assert old["original_normal_free_basis"] == FREE_BASIS
        assert old["entire_original_function_field_action_defined"] is True
        assert old["all_three_normal_linear_transports_verified"] is True
        self.dag_spec = self.output_spec(name)

    def run(self):
        if (self.out / FINAL).exists():
            old = read(self.out / FINAL)
            assert old["configuration"] == self.tag
            if old["complete"] is True:
                for key in ("source_audit", "three_conjugate_coordinates", "function_field_action_DAG", "stage_manifest"):
                    value = plain(old[key])
                    assert spec(self.out / value["file"]) == value
                self.audit_spec = old["source_audit"]
                self.coordinate_spec = old["three_conjugate_coordinates"]
                self.dag_spec = old["function_field_action_DAG"]
                return
        self.load_prefix()
        self.source_audit()
        columns = self.coordinates()
        self.function_dag(columns)

    def inventory(self):
        entries = []
        for path in sorted(self.out.glob(PREFIX + "*.json.gz")):
            if path.name == INVENTORY:
                continue
            value = read(path)
            assert value["configuration"] == self.tag and value["complete"] is True
            entries.append(spec(path))
        save(self.out / INVENTORY, {"result": RESULT, "configuration": self.tag,
            "complete": True, "files": entries, "only_completed_mathematical_stages_listed": True})
        return spec(self.out / INVENTORY)

    def finish(self, complete, stop_reason, error):
        if (self.out / FINAL).exists():
            previous = read(self.out / FINAL)
            assert previous["configuration"] == self.tag
            if previous["complete"] is True:
                assert complete
                return previous
        manifest = self.inventory()
        coordinates = self.cached("R853-three-exact-original-V1-conjugates")
        dag = self.cached("R853-original-semilinear-function-field-generator-DAG")
        conjugates_done = bool(coordinates and coordinates["all560_original_coordinates_verified_for_each_conjugate"])
        action_done = bool(dag and dag["entire_original_function_field_action_defined"])
        if complete:
            assert conjugates_done and action_done
        final = {
            "result": RESULT, "configuration": self.tag, "complete": bool(complete), "p": 41,
            "original_three_V1_conjugates_certified": conjugates_done,
            "original_semilinear_function_field_generator_action_certified": action_done,
            "original_qY_prefix_orders": ORDERS, "original_xi_coordinates_per_order": XI,
            "full_original_coordinate_rows": ROWS, "new_exact_right_hand_side_count": 3,
            "source_audit": self.output_spec("R853-original-V1-prefix-and-source-audit")
                if self.cached("R853-original-V1-prefix-and-source-audit") else None,
            "three_conjugate_coordinates": self.output_spec("R853-three-exact-original-V1-conjugates") if coordinates else None,
            "function_field_action_DAG": self.output_spec("R853-original-semilinear-function-field-generator-DAG") if dag else None,
            "stage_manifest": manifest, "stop_reason": stop_reason, "error": error,
            "original_scales_preserved": True,
            "original_Fourier_CM_or_reflection_minor_arithmetic_recomputed": False,
            "full146_or272_column_conjugation_matrix_computed": False,
            "new_RR_spaces_connections_periods_or_heights_computed": False,
            "seconds": time.monotonic() - self.started,
        }
        save(self.out / FINAL, final)
        return final


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--budget-minutes", type=float, required=True)
    args = parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("All new R853 mathematics belongs to the public repository's GitHub Actions.")
    started = time.monotonic()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    job, final, error = None, None, None
    status, stop_reason = 1, "initialization_incomplete"
    try:
        job = Job(args)
        job.run()
        status, stop_reason = 0, "certified_three_original_V1_conjugates"
    except BudgetStop as exc:
        status, stop_reason, error = 124, "budget_stop", str(exc)
    except BaseException as exc:
        status, stop_reason, error = 1, "exception", type(exc).__name__ + ": " + str(exc)
        traceback.print_exc()
    if job is not None:
        try:
            final = job.finish(status == 0, stop_reason, error)
        except BaseException as exc:
            status, stop_reason, error = 1, "finalization_exception", type(exc).__name__ + ": " + str(exc)
            traceback.print_exc()
    complete = status == 0 and final is not None and final["complete"] is True
    receipt = {
        "result": RESULT, "p": 41, "source_sha256": sha(__file__), "complete": complete,
        "process_exit_code": status, "stop_reason": stop_reason, "error": error,
        "certificate_sha256": sha(out / FINAL) if final is not None else None,
        "original_three_V1_conjugates_certified": bool(final and final["original_three_V1_conjugates_certified"]),
        "original_semilinear_function_field_generator_action_certified": bool(final and final["original_semilinear_function_field_generator_action_certified"]),
        "stage_manifest": final["stage_manifest"] if final else None,
        "new_RR_spaces_connections_periods_or_heights_computed": False,
        "seconds": time.monotonic() - started,
    }
    save(out / "core-receipt.json", receipt)
    print("R853_CORE_RECEIPT=" + json.dumps(receipt, sort_keys=True), flush=True)
    return status


if __name__ == "__main__":
    sys.set_int_max_str_digits(0)
    sys.exit(main())
