#!/usr/bin/env python3
"""Original short RR quotients and D kernel; new arithmetic only in public Actions."""

import argparse
import gc
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
from flint import nmod_mat, nmod_poly

RESULT = "R839-original-short-RR-spaces-and-D-kernel"
FINAL = "p41-original-short-RR-and-D-kernel-certificate.json"
PREFIX = "R839-"
INVENTORY = "R839-stage-manifest.json.gz"
PRIME = 1000000753
FREE = 272
EPS = [0]+[1]*144+[2]*127
V2, V3, V5 = 418, 690, 1234
N = 11
T11_DIM, T5_QUOTIENT_RANK, D_RANK = 2451, 415, 395
COORD11, COLS11 = 2866, 2886
ORDERS, XI, REAL, STRIDE = 69, 40, 20, 79
PRODUCT_BATCH = 17
LABELS = ("R827", "R838", "R837", "R809", "R786")
BASE_KEYS = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256", "configuration_sha256")
H64 = re.compile(r"[0-9a-f]{64}")
LAYER_INDEXES = (
    "R827-target-B-tau-polynomial-index.json.gz",
    "R827-tau-layer-001-precision-0010-index.json.gz",
    "R827-tau-layer-002-precision-0012-index.json.gz",
)
PLACE = "R827-original-place-and-unit-source-audit.json.gz"
S5_INVERSE = "R827-prime-1000000753-S5-fixed-minor-inverse.json.gz"
S5_INDEX = "R809-S5-basis-index.json.gz"
MATH_SCOPE = {
    "auxiliary_prime": PRIME,
    "original_branch": 0,
    "normal_basis_rank": FREE,
    "normal_basis_degrees": EPS,
    "uniform_homogeneous_weight": 11,
    "source_derivative_orders": [0, 1, 2],
    "source_generator_order": "derivative_order, original_normal_basis_index, z_shift",
    "target_normal_row_order": "normal_basis_index outer; z_degree increasing",
    "T11_matrix_shape": [COORD11, COLS11],
    "T11_required_rank": T11_DIM,
    "T5_matrix_shape": [830, V5],
    "T5_required_rank": T5_QUOTIENT_RANK,
    "D_matrix_shape": [830, V3],
    "D_required_rank": D_RANK,
    "D_RR_dimension": 295,
    "source_coordinate_order": "20*qY_exponent+t_degree; v=xi^-10*qY",
    "original_V2_integer_scale": str(82**4),
    "original_V3_integer_scale": str(82**6),
    "original_V5_integer_scale": str(82**10),
    "product_group_size": PRODUCT_BATCH,
    "old_derivatives_and_same_prime_S5_inverse_recomputed": False,
    "accurate_characteristic_zero_objects_are_source_bound_unit_solve_expressions": True,
    "budget_excluded_from_mathematical_identity": True,
}


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def plain(value):
    item = {key: value[key] for key in ("file", "bytes", "sha256")}
    assert isinstance(item["file"], str) and Path(item["file"]).name == item["file"]
    assert item["file"] not in (".", "..") and "\\" not in item["file"]
    assert isinstance(item["bytes"], int) and item["bytes"] >= 0
    assert H64.fullmatch(item["sha256"])
    return item


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


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
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb", mtime=0, compresslevel=2) as packed:
                packed.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def rows(matrix):
    return [[int(matrix[i, j]) for j in range(matrix.ncols())] for i in range(matrix.nrows())]


def matrix_zero(height, width):
    return nmod_mat([[0]*width for _ in range(height)], PRIME)


def identity(size):
    return nmod_mat([[int(i == j) for j in range(size)] for i in range(size)], PRIME)


def pivots(rref, rank):
    answer = []
    for i in range(rank):
        j = next(j for j in range(rref.ncols()) if rref[i, j])
        assert int(rref[i, j]) == 1
        assert not answer or answer[-1] < j
        answer.append(j)
    return answer


def submatrix(matrix, row_indices, column_indices):
    return nmod_mat([[int(matrix[r, c]) for c in column_indices] for r in row_indices], PRIME)


def normal_positions(weight):
    return [(a, j) for a in range(FREE) for j in range(weight-EPS[a]+1)]


def checked_mod(value):
    assert isinstance(value, int) and 0 <= value < PRIME
    return value


def checked_shape(data, height, width):
    assert isinstance(data, list) and len(data) == height
    assert all(isinstance(row, list) and len(row) == width for row in data)
    for row in data:
        for value in row:
            checked_mod(value)


def guard():
    assert os.environ.get("GITHUB_ACTIONS") == "true", "All new mathematics must run in public Actions."
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    assert flint.__version__ == "0.9.0"
    sys.set_int_max_str_digits(0)


class BudgetStop(RuntimeError):
    pass


class Source:
    def __init__(self, label, item):
        self.label, self.item = label, item
        self.root = Path(item["directory"])
        self.files = {name: plain(value) for name, value in item["files"].items()}
        assert all(name == value["file"] for name, value in self.files.items())
        self.identity = {key: item[key] for key in BASE_KEYS}
        for key in ("core_sha256", "manifest_sha256", "configuration_sha256"):
            assert H64.fullmatch(self.identity[key])
        self.checked = set()
        assert self.files["full-outputs-manifest.json"]["sha256"] == item["manifest_sha256"]
        manifest = self.raw("full-outputs-manifest.json")
        self.manifest_files = {entry["file"]: plain(entry) for entry in manifest["files"]}
        for name, value in self.files.items():
            if name not in ("full-outputs-manifest.json", "full-outputs-manifest-reference.json"):
                assert value == self.manifest_files[name]
        self.certificate = None
        if item.get("certificate_name"):
            self.certificate = self.raw(item["certificate_name"])
            assert self.certificate["result"] == item["result"]
            assert fingerprint(self.certificate["configuration"]) == item["configuration_sha256"]
        self.tag = None

    def raw(self, value):
        name = value if isinstance(value, str) else value["file"]
        entry = self.files[name]
        if not isinstance(value, str):
            assert plain(value) == entry
        path = self.root/name
        if name not in self.checked:
            assert path.stat().st_size == entry["bytes"] and sha(path) == entry["sha256"]
            self.checked.add(name)
        return read(path)

    def stage(self, value):
        item = self.raw(value)
        assert item["complete"] is True
        configuration = item["configuration"]
        assert configuration["result"] == self.identity["result"]
        assert configuration["source_sha256"] == self.identity["core_sha256"]
        assert configuration["python_flint"] == "0.9.0"
        assert fingerprint(configuration) == self.identity["configuration_sha256"]
        if self.tag is None:
            self.tag = configuration
        else:
            assert configuration == self.tag
        if "result" in item:
            assert item["result"] == configuration["result"]
        return item

    def source(self, value):
        name = value if isinstance(value, str) else value["file"]
        if not isinstance(value, str):
            assert plain(value) == self.files[name]
        return dict(self.files[name], producer=self.label)

    def stable(self):
        return dict(self.identity, certificate_name=self.item.get("certificate_name"), files=self.files)


class Job:
    def __init__(self, args):
        self.args, self.started = args, time.monotonic()
        self.item = read(args.config)
        assert self.item["result"] == RESULT and self.item["core_sha256"] == sha(__file__)
        for key in ("proof", "method"):
            assert sha(self.item[key]) == self.item[key+"_sha256"]
        self.out = args.out
        self.out.mkdir(parents=True, exist_ok=True)
        self.sources = {label: Source(label, self.item["sources"][label]) for label in LABELS}
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "p": 41, "R839_proof_sha256": self.item["proof_sha256"],
            "R839_method_sha256": self.item["method_sha256"],
            "sources": {label: self.sources[label].stable() for label in LABELS},
            **MATH_SCOPE,
        }
        self.r827, self.r838, self.r837 = (self.sources[x] for x in ("R827", "R838", "R837"))
        self.r809, self.r786 = self.sources["R809"], self.sources["R786"]
        self.positions11, self.positions5 = normal_positions(11), normal_positions(5)
        assert len(self.positions11) == COORD11 and len(self.positions5) == V5
        self.position11_index = {value: i for i, value in enumerate(self.positions11)}
        self.current_stage = "initializing"
        self.last_ranks = {"T11": None, "T5": None, "D": None}
        self.audit_data = None
        self.Phi = self.Pi = self.Q5 = self.S5 = self.S5inv = None
        self.Phi_spec = self.quotient_spec = self.q5_spec = self.kernel_spec = None
        self.s5_matrix_source = None
        self.g_t, self.chebyshev = None, None
        self.complete = False

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes-45:
            raise BudgetStop("Only completed original source-bound stages retained; stage="+self.current_stage)

    def path(self, name):
        assert name.startswith(PREFIX) and Path(name).name == name
        return self.out/(name if name.endswith(".json.gz") else name+".json.gz")

    def get(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["complete"] is True and value["configuration"] == self.tag
        assert value["result"] == RESULT
        return value

    def put(self, name, value):
        assert "configuration" not in value and "result" not in value
        value = dict(value, result=RESULT, configuration=self.tag, complete=True)
        save(self.path(name), value)
        return value

    def output_source(self, name):
        return spec(self.path(name))

    def mark(self, name):
        self.current_stage = name
        print(json.dumps({"stage": name, "seconds": time.monotonic()-self.started}), flush=True)
        self.budget()

    def source_audit(self):
        name = "R839-original-source-audit"
        old = self.get(name)
        c838, c837 = self.r838.certificate, self.r837.certificate
        assert c838 is not None and c838["complete"] is True
        assert c838["original_characteristic_zero_J2_equals_I2"] is True
        assert c838["actual_P0_multiplicity_in_D"] == 0
        assert c838["actual_original_I2_colength"] == 415
        assert c838["configuration"]["source_configuration_sha256"] == self.r827.identity["configuration_sha256"]
        assert c838["configuration"]["source_identity"] == {
            key: self.r827.identity[key] for key in BASE_KEYS if key != "configuration_sha256"}
        assert c837 is not None and c837["complete"] is True
        assert c837["original_P0_evaluation_certified"] is True
        assert c837["complete_fixed_branch_space_certified"] is True
        assert c837["fixed_branch_pencil_certified"] is True
        assert c837["actual_pencil_rank"] == 1213
        assert all(c837["configuration"]["sources"]["R786"][key] == self.r786.identity[key]
                   for key in BASE_KEYS)
        place = self.r827.stage(PLACE)
        assert place["prime"] == PRIME and place["original_branch"] == 0
        assert place["canonical_free_column"] == 1186
        assert place["genuine_DVR_lift_source_not_an_arbitrary_modular_kernel_candidate"] is True
        assert all(self.r827.tag["source_identities"]["R809"][key] == self.r809.identity[key]
                   for key in BASE_KEYS if key != "configuration_sha256")
        operator_certificate_name = "R827-complete-short-operator-identities-and-sigma-transport.json.gz"
        operator_certificate = self.r827.stage(operator_certificate_name)
        assert operator_certificate["all_operators_are_true_original_p_integral_reductions"] is True
        assert operator_certificate["all_sigma_negative_powers_and_original_minus_sign_verified"] is True
        assert operator_certificate["B_commutator_full_polynomial_identity_certified_by_nine_points"] is True
        assert operator_certificate["Gamma_nested_full_polynomial_identity_certified_by_seven_points"] is True
        original_vB_name = "R827-canonical-B-normal-vector.json.gz"
        original_vB = self.r827.stage(original_vB_name)
        assert original_vB["abstract_p_integral_original_normal_lift_certified"] is True
        assert original_vB["all1380_original_short_coordinates_verified"] is True
        assert original_vB["same_original_82power10_scales_preserved"] is True
        assert original_vB["normal_basis_degrees"] == EPS
        assert plain(original_vB["source_S5_index"]) == plain(self.r809.source(S5_INDEX))
        assert plain(original_vB["source_actual_unit_minor"]) == plain(self.r827.source(S5_INVERSE))
        self.zeta_root = checked_mod(place["original_zeta_root"])
        assert (self.zeta_root*self.zeta_root+self.zeta_root+1) % PRIME == 0
        self.layer_sources = [self.r827.source(value) for value in LAYER_INDEXES]
        self.layer_indexes = [self.r827.stage(value) for value in LAYER_INDEXES]
        layer0 = self.layer_indexes[0]
        assert layer0["target"] == "B" and layer0["chart"] == "tau"
        assert layer0["prime"] == PRIME and layer0["regular_degree_bound"] == 5
        assert layer0["normal_basis_degrees"] == EPS
        assert layer0["all_weighted_support_zeros_verified"] is True
        assert layer0["original_true_operator_reduction_certified"] is True
        assert len(layer0["row_blocks"]) == 17
        for order, index in enumerate(self.layer_indexes[1:], 1):
            assert index["chart"] == "tau" and index["prime"] == PRIME
            assert index["derivative_order"] == order
            assert index["normal_basis_degrees"] == EPS
            assert index["original_generator_weights"] == [5+e for e in EPS]
            assert index["precision_stop"] == 8+2*order
            assert index["full_polynomial_coefficients_computed"] is True
            assert index["all_required_coefficient_blocks_complete"] is True
            assert len(index["coefficient_row_blocks"]) == 17*(8+2*order)
        self.pencil_spec = self.r837.source(c837["pencil_certificate"])
        pencil = self.r837.stage(self.pencil_spec)
        assert pencil["fixed_branch_pencil_certified"] is True
        assert pencil["actual_pencil_rank"] == 1213
        assert pencil["rank1213_implies_exact_common_zero_divisor_Dcusp_plus_P0"] is True
        self.anchor_specs = {"u": self.r837.source(pencil["first_anchor"]),
                             "v": self.r837.source(pencil["second_anchor"])}
        self.anchors = {which: self.r837.stage(value) for which, value in self.anchor_specs.items()}
        for value in self.anchors.values():
            assert value["exact_nonzero_member_of_U"] is True
            assert value["not_an_old_single_recipe_product"] is True
            assert len(value["integer_sparse_coordinates"]) == value["original_V2_nonzero_term_count"]
        self.s5_index = self.r809.stage(S5_INDEX)
        assert self.s5_index["normal_basis_degrees"] == EPS
        assert self.s5_index["dimension"] == V5 and self.s5_index["qY_count"] == ORDERS
        assert self.s5_index["integer_scale"] == str(82**10)
        assert self.s5_index["full_coordinate_rows"] == ORDERS*REAL
        assert self.s5_index["all_original_term_phases_and_scales_verified"] is True
        self.s5_inverse = self.r827.stage(S5_INVERSE)
        assert self.s5_inverse["prime"] == PRIME
        assert plain(self.s5_inverse["S5_basis_index"]) == plain(self.r809.source(S5_INDEX))
        assert self.s5_inverse["both_inverse_products_verified"] is True
        assert self.s5_inverse["original_Q_matrix_and_69_term_rows_recomputed"] is False
        assert self.s5_inverse["column_indices"] == list(range(V5))
        self.s5_selected = list(self.s5_inverse["row_indices"])
        assert len(self.s5_selected) == len(set(self.s5_selected)) == V5
        assert min(self.s5_selected) >= 0 and max(self.s5_selected) < ORDERS*REAL
        checked_shape(self.s5_inverse["inverse_mod_prime"], V5, V5)
        if old is None:
            self.mark(name)
            old = self.put(name, {
                "prime": PRIME, "original_branch": 0, "original_zeta_root": self.zeta_root,
                "source_place_audit": self.r827.source(PLACE),
                "source_original_operator_identities": self.r827.source(operator_certificate_name),
                "source_original_implicit_normal_B": self.r827.source(original_vB_name),
                "source_complete_I2_certificate": self.r838.source(self.r838.item["certificate_name"]),
                "actual_E2_degree": 415, "actual_P0_multiplicity_in_D": 0,
                "source_layer_indexes": self.layer_sources,
                "original_normal_F_not_C_basis_coordinates": True,
                "source_fixed_branch_pencil": self.pencil_spec,
                "source_anchors": self.anchor_specs,
                "source_S5_index": self.r809.source(S5_INDEX),
                "source_completed_S5_modular_inverse": self.r827.source(S5_INVERSE),
                "all_sources_keep_their_original_configurations": True,
                "old_CM_derivatives_or_S5_inverse_recomputed": False,
            })
        assert old["source_layer_indexes"] == self.layer_sources
        assert old["source_anchors"] == self.anchor_specs and old["original_zeta_root"] == self.zeta_root
        self.audit_data = old
        return self.output_source(name)

    def load_layer(self, order):
        index = self.layer_indexes[order]
        count = 8+2*order
        answer = [[[0]*FREE for _ in range(FREE)] for _ in range(count)]
        coverage = set()
        if order == 0:
            entries = index["row_blocks"]
            for entry in entries:
                self.budget()
                value = self.r827.stage(entry)
                first, stop = value["row_first"], value["row_stop"]
                assert value["target"] == "B" and value["chart"] == "tau"
                assert value["regular_degree_bound"] == 5 and value["prime"] == PRIME
                assert value["original_weighted_support_verified"] is True
                assert 0 <= first < stop <= FREE and stop-first <= 16
                coeffs = value["coefficient_matrices_low_to_high"]
                assert len(coeffs) == count
                for n, values in enumerate(coeffs):
                    checked_shape(values, stop-first, FREE)
                    for local, row in enumerate(values):
                        key = n, first+local
                        assert key not in coverage
                        coverage.add(key)
                        answer[n][first+local] = row
        else:
            entries = index["coefficient_row_blocks"]
            for entry in entries:
                self.budget()
                value = self.r827.stage(entry)
                first, stop, n = value["row_first"], value["row_stop"], value["coefficient_exponent"]
                assert value["derivative_order"] == order and value["chart"] == "tau"
                assert value["prime"] == PRIME and value["original_weighted_support_verified"] is True
                assert value["all_required_previous_coefficients_present_or_structurally_zero"] is True
                assert value["old_completed_coefficient_not_recomputed"] is True
                assert value["source_original_generator_weights"] == [5+e for e in EPS]
                assert 0 <= n < count and 0 <= first < stop <= FREE and stop-first <= 16
                values = value["coefficient_matrix_mod_prime"]
                checked_shape(values, stop-first, FREE)
                for local, row in enumerate(values):
                    key = n, first+local
                    assert key not in coverage
                    coverage.add(key)
                    answer[n][first+local] = row
        assert len(coverage) == count*FREE
        for n, matrix in enumerate(answer):
            for row in range(FREE):
                for col in range(FREE):
                    if n > 5+EPS[col]+2*order-EPS[row]:
                        assert matrix[row][col] == 0
        return answer, [self.r827.source(value) for value in entries]

    def homogeneous_matrix(self):
        name = "R839-T11-shifted-source-matrix"
        old = self.get(name)
        if old is None:
            self.mark(name)
            matrix = [[0]*COLS11 for _ in range(COORD11)]
            source_blocks, columns = [], []
            position = 0
            for order in range(3):
                layer, block_sources = self.load_layer(order)
                source_blocks.append(block_sources)
                for col in range(FREE):
                    weight = 5+EPS[col]+2*order
                    for shift in range(12-weight):
                        columns.append([order, col, shift])
                        for degree, coeffs in enumerate(layer):
                            for row in range(FREE):
                                value = coeffs[row][col]
                                if not value:
                                    continue
                                exponent = degree+shift
                                assert 0 <= exponent <= N-EPS[row]
                                matrix[self.position11_index[row, exponent]][position] = value
                        position += 1
                del layer
                self.budget()
            assert position == COLS11
            old = self.put(name, {
                "prime": PRIME, "matrix_shape": [COORD11, COLS11],
                "source_original_layer_indexes": self.layer_sources,
                "source_original_layer_blocks": source_blocks,
                "normal_basis_degrees": EPS, "row_labels": [list(value) for value in self.positions11],
                "column_labels": columns, "matrix_mod_prime": matrix,
                "all_original_weight_bounds_verified": True,
                "only_completed_coefficient_shifts_used": True,
                "original_V11_Fourier_or_derivative_arithmetic_recomputed": False,
                "exact_source_expression": {
                    "operation": "homogenize_original_global_source_columns",
                    "uniform_weight": 11, "sources": self.layer_sources,
                    "column_rule": "tau^(11-w-k)*sigma^k*s_(r,c)",
                    "source_weights": "w=5+epsilon_c+2*r",
                },
            })
            del matrix
        assert old["row_labels"] == [list(x) for x in self.positions11]
        assert old["matrix_shape"] == [COORD11, COLS11]
        assert old["source_original_layer_indexes"] == self.layer_sources
        assert old["all_original_weight_bounds_verified"] is True
        checked_shape(old["matrix_mod_prime"], COORD11, COLS11)
        self.Phi = nmod_mat(old["matrix_mod_prime"], PRIME)
        self.Phi_spec = self.output_source(name)
        return self.Phi_spec

    def T11_columns(self):
        name = "R839-T11-source-column-rank"
        old = self.get(name)
        if old is None:
            self.mark(name)
            reduced, rank = self.Phi.rref()
            selected = pivots(reduced, rank)
            assert rank <= T11_DIM, "A modular rank exceeding the exact RR bound signals a source error."
            old = self.put(name, {
                "prime": PRIME, "source_matrix": self.Phi_spec,
                "actual_rank": rank, "required_rank": T11_DIM,
                "independent_original_source_column_indices": selected,
                "actual_rank_is_sufficient": rank == T11_DIM,
                "failed_modular_rank_does_not_disprove_characteristic_zero_fullness": rank != T11_DIM,
                "all_2866_rows_and_2886_columns_used": True,
            })
            del reduced
        assert old["source_matrix"] == self.Phi_spec
        self.last_ranks["T11"] = old["actual_rank"]
        return old, self.output_source(name)

    def T11_quotient(self, selection, selection_spec):
        name = "R839-T11-unit-quotient"
        old = self.get(name)
        J = selection["independent_original_source_column_indices"]
        assert selection["actual_rank"] == T11_DIM and len(J) == T11_DIM
        if old is None:
            self.mark(name)
            T = submatrix(self.Phi, list(range(COORD11)), J)
            echelon, rank = T.transpose().rref()
            assert rank == T11_DIM
            I = pivots(echelon, rank)
            occupied = set(I)
            R = [i for i in range(COORD11) if i not in occupied]
            assert len(R) == T5_QUOTIENT_RANK
            square = submatrix(T, I, list(range(T11_DIM)))
            determinant = int(square.det())
            assert determinant
            projection = [[0]*COORD11 for _ in R]
            for row, original_row in enumerate(R):
                projection[row][original_row] = 1
                for j, pivot_row in enumerate(I):
                    projection[row][pivot_row] = (-int(echelon[j, original_row])) % PRIME
            P = nmod_mat(projection, PRIME)
            assert P*T == matrix_zero(len(R), T11_DIM)
            assert submatrix(P, list(range(len(R))), R) == identity(len(R))
            old = self.put(name, {
                "prime": PRIME, "source_matrix": self.Phi_spec,
                "source_column_selection": selection_spec,
                "actual_rank": rank, "selected_original_rows": I,
                "selected_original_source_columns": J, "complement_original_rows": R,
                "actual_minor_determinant_mod_prime": determinant,
                "quotient_matrix_mod_prime": projection,
                "all_2451_source_columns_annihilated_in_all415_rows": True,
                "complement_identity_verified": True,
                "exact_original_T11_as_unit_chart_expression_certified": True,
                "expanded_characteristic_zero_coordinates_computed": False,
                "exact_unit_solve_expression": {
                    "operation": "x_R-T_R*solve(T_I,x_I)",
                    "original_matrix": self.Phi_spec, "selected_columns": J,
                    "selected_rows": I, "complement_rows": R,
                    "coefficient_field": "the original L, reduced at the fixed branch0 place",
                    "unit_certificate": "the actual same selected minor recorded in this stage",
                    "exact_kernel": "H0(11H-E2)", "exact_kernel_dimension": T11_DIM,
                },
            })
            del T, echelon, square, P
        assert old["source_matrix"] == self.Phi_spec
        assert old["source_column_selection"] == selection_spec
        assert old["exact_original_T11_as_unit_chart_expression_certified"] is True
        checked_shape(old["quotient_matrix_mod_prime"], T5_QUOTIENT_RANK, COORD11)
        self.Pi = nmod_mat(old["quotient_matrix_mod_prime"], PRIME)
        self.quotient_spec = self.output_source(name)
        return self.quotient_spec

    def T5_matrix(self):
        name = "R839-T5-two-pencil-power-conditions"
        old = self.get(name)
        if old is None:
            self.mark(name)
            indices0 = [self.position11_index[a, j] for a, j in self.positions5]
            indices1 = [self.position11_index[a, j+6] for a, j in self.positions5]
            values = [[int(self.Pi[r, j]) for j in indices0] for r in range(T5_QUOTIENT_RANK)]
            values += [[int(self.Pi[r, j]) for j in indices1] for r in range(T5_QUOTIENT_RANK)]
            old = self.put(name, {
                "prime": PRIME, "source_T11_quotient": self.quotient_spec,
                "matrix_shape": [830, V5], "matrix_mod_prime": values,
                "source_embedding_tau_power": 6, "source_embedding_sigma_power": 6,
                "tau_embedding_original_T11_rows": indices0,
                "sigma_embedding_original_T11_rows": indices1,
                "original_V5_row_labels": self.positions5,
                "both_basepointfree_pencil_conditions_preserved": True,
                "exact_kernel": "H0(5H-E2)", "exact_kernel_dimension": 819,
                "exact_characteristic_zero_rank": T5_QUOTIENT_RANK,
                "new_Fourier_or_polynomial_multiplication_computed": False,
            })
        assert old["source_T11_quotient"] == self.quotient_spec
        checked_shape(old["matrix_mod_prime"], 830, V5)
        return nmod_mat(old["matrix_mod_prime"], PRIME), self.output_source(name)

    def T5_quotient(self, matrix, source):
        name = "R839-T5-independent-original-row-quotient"
        old = self.get(name)
        if old is None:
            self.mark(name)
            first, rank = matrix.rref()
            assert rank <= T5_QUOTIENT_RANK
            columns = pivots(first, rank)
            value = {
                "prime": PRIME, "source_two_pencil_matrix": source,
                "actual_rank": rank, "required_rank": T5_QUOTIENT_RANK,
                "exact_original_T5_quotient_as_unit_chart_expression_certified": False,
                "failed_modular_rank_does_not_disprove_characteristic_zero_fullness": rank != T5_QUOTIENT_RANK,
            }
            if rank == T5_QUOTIENT_RANK:
                selected_column_matrix = submatrix(matrix, list(range(830)), columns)
                second, second_rank = selected_column_matrix.transpose().rref()
                assert second_rank == rank
                selected_rows = pivots(second, rank)
                Q = submatrix(matrix, selected_rows, list(range(V5)))
                minor = submatrix(matrix, selected_rows, columns)
                determinant = int(minor.det())
                assert determinant
                row_combination = selected_column_matrix*minor.inv()
                assert row_combination*Q == matrix
                value.update({
                    "selected_original_rows": selected_rows,
                    "selected_original_columns": columns,
                    "actual_minor_determinant_mod_prime": determinant,
                    "quotient_matrix_mod_prime": rows(Q),
                    "full_830_by1234_row_space_reconstruction_verified": True,
                    "exact_original_T5_quotient_as_unit_chart_expression_certified": True,
                    "exact_unit_solve_expression": {
                        "operation": "select_original_rows",
                        "matrix_source": source, "row_indices": selected_rows,
                        "exact_kernel": "H0(5H-E2)", "exact_rank": T5_QUOTIENT_RANK,
                    },
                })
                del selected_column_matrix, second, Q, minor, row_combination
            old = self.put(name, value)
            del first
        assert old["source_two_pencil_matrix"] == source
        self.last_ranks["T5"] = old["actual_rank"]
        self.q5_spec = self.output_source(name)
        if old["actual_rank"] == T5_QUOTIENT_RANK:
            checked_shape(old["quotient_matrix_mod_prime"], T5_QUOTIENT_RANK, V5)
            self.Q5 = nmod_mat(old["quotient_matrix_mod_prime"], PRIME)
        return old

    def S5_matrix(self):
        name = "R839-original-S5-fixed-place-matrix"
        old = self.get(name)
        if old is None:
            self.mark(name)
            columns, sources, mapping = [], [], []
            for i, entry in enumerate(self.s5_index["basis_rows"]):
                self.budget()
                assert entry["index"] == i
                value = self.r809.stage(entry["source"])
                a, j = value["normal_basis_index"], value["z_degree"]
                assert entry["normal_basis_index"] == a and entry["z_degree"] == j
                assert value["index"] == i and value["normal_basis_degree"] == EPS[a]
                assert value["integer_scale"] == str(82**10)
                assert value["qY_count"] == ORDERS and value["real_coordinate_count"] == REAL
                assert value["all_original_term_phases_and_scales_verified"] is True
                assert value["original_R805_free_generator_unchanged"] is True
                data = value["integer_v_t_coefficients"]
                assert len(data) == ORDERS and all(len(row) == REAL for row in data)
                columns.append([int(x) % PRIME for row in data for x in row])
                sources.append(self.r809.source(entry["source"]))
                mapping.append((a, j))
            assert mapping == self.positions5 and len(columns) == V5
            old = self.put(name, {
                "prime": PRIME, "source_S5_index": self.r809.source(S5_INDEX),
                "source_original_S5_rows": sources,
                "normal_basis_row_mapping": [list(value) for value in mapping],
                "original_integer_scale": str(82**10),
                "columns_mod_prime": columns, "matrix_shape": [ORDERS*REAL, V5],
                "source_completed_inverse": self.r827.source(S5_INVERSE),
                "only_original_coefficients_reduced_for_new_product_rhs": True,
                "same_prime_inverse_rank_and_old_product_arithmetic_recomputed": False,
            })
        assert old["source_S5_index"] == self.r809.source(S5_INDEX)
        assert old["normal_basis_row_mapping"] == [list(value) for value in self.positions5]
        assert old["source_completed_inverse"] == self.r827.source(S5_INVERSE)
        checked_shape(old["columns_mod_prime"], V5, ORDERS*REAL)
        self.S5 = nmod_mat(old["columns_mod_prime"], PRIME).transpose()
        self.S5inv = nmod_mat(self.s5_inverse["inverse_mod_prime"], PRIME)
        self.s5_matrix_source = self.output_source(name)
        return self.s5_matrix_source

    def original_prefix(self, power, index):
        assert power in (2, 3) and 0 <= index < {2: V2, 3: V3}[power]
        name = "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"
        value = self.r786.stage(name)
        assert value["weight"] == 2*power and value["bound_qY"] == 128
        assert value["integer_scale"] == str(82**(2*power))
        assert value["original_R775_finite_coefficients_verified"] is True
        data = value["integer_qY_xi_coefficients"]
        assert len(data) == 129 and all(len(row) == XI for row in data)
        return [[int(x) % PRIME for x in row] for row in data[:ORDERS]], self.r786.source(name)

    def anchor_prefix(self, which):
        name = "R839-anchor-"+which+"-original-prefix-at-fixed-place"
        old = self.get(name)
        if old is None:
            self.mark(name)
            answer = [[0]*XI for _ in range(ORDERS)]
            input_sources, seen = [], set()
            anchor = self.anchors[which]
            assert self.r837.stage(self.pencil_spec)["prime"] != PRIME
            for entry in anchor["integer_sparse_coordinates"]:
                self.budget()
                index = entry["original_V2_index"]
                assert isinstance(index, int) and 0 <= index < V2 and index not in seen
                seen.add(index)
                coefficients = entry["integer_coefficients_K_1_zeta"]
                assert len(coefficients) == 2
                scalar = (int(coefficients[0])+self.zeta_root*int(coefficients[1])) % PRIME
                source_rows, source = self.original_prefix(2, index)
                input_sources.append(source)
                if scalar:
                    for n in range(ORDERS):
                        answer[n] = [(x+scalar*y) % PRIME for x, y in zip(answer[n], source_rows[n])]
            assert len(seen) == anchor["original_V2_nonzero_term_count"]
            old = self.put(name, {
                "prime": PRIME, "original_zeta_root": self.zeta_root, "anchor": which,
                "source_original_anchor": self.anchor_specs[which],
                "source_original_V2_rows": input_sources,
                "qY_xi_coefficients_mod_prime": answer,
                "qY_count": ORDERS, "xi_coordinate_count": XI,
                "original_V2_integer_scale": str(82**4),
                "original_primitive_normalization_scale_preserved": anchor["primitive_normalization_scale"],
                "additional_anchor_rescaling": False,
                "source_R837_product_prime": self.r837.stage(self.pencil_spec)["prime"],
                "new_required_place_not_the_original_R837_trial_place": True,
            })
        assert old["source_original_anchor"] == self.anchor_specs[which]
        assert old["prime"] == PRIME and old["original_zeta_root"] == self.zeta_root
        checked_shape(old["qY_xi_coefficients_mod_prime"], ORDERS, XI)
        return old["qY_xi_coefficients_mod_prime"], self.output_source(name)

    @staticmethod
    def pack(raw):
        assert len(raw) == ORDERS and all(len(row) == XI for row in raw)
        values = [0]*(ORDERS*STRIDE)
        for n, row in enumerate(raw):
            values[n*STRIDE:n*STRIDE+XI] = row
        return nmod_poly(values, PRIME)

    @staticmethod
    def unpack(product):
        assert product.degree() < ORDERS*STRIDE
        answer = []
        for n in range(ORDERS):
            cyclic = [0]*41
            for r in range(STRIDE):
                cyclic[r % 41] = (cyclic[r % 41]+int(product[n*STRIDE+r])) % PRIME
            answer.append([(cyclic[r]-cyclic[40]) % PRIME for r in range(XI)])
        return answer

    def real_rows(self, raw):
        if self.chebyshev is None:
            variable = nmod_poly([0, 1], PRIME)
            self.chebyshev = [nmod_poly([2], PRIME), variable]
            for _ in range(2, 21):
                self.chebyshev.append(variable*self.chebyshev[-1]-self.chebyshev[-2])
            self.g_t = nmod_poly([1], PRIME)
            for value in self.chebyshev[1:]:
                self.g_t += value
            assert self.g_t.degree() == REAL and int(self.g_t[REAL]) == 1
        answer = []
        for n, vector in enumerate(raw):
            assert len(vector) == XI
            cyclic = [0]*41
            for r, value in enumerate(vector):
                cyclic[(r+10*n) % 41] = (cyclic[(r+10*n) % 41]+value) % PRIME
            reduced = [(cyclic[r]-cyclic[40]) % PRIME for r in range(XI)]+[0]
            assert all(reduced[r] == reduced[41-r] for r in range(1, 21))
            polynomial = nmod_poly([reduced[0]], PRIME)
            for r in range(1, 21):
                polynomial += self.chebyshev[r]*reduced[r]
            polynomial %= self.g_t
            answer.append([int(polynomial[r]) for r in range(REAL)])
        return answer

    def anchor_products(self, which):
        prefix, prefix_spec = self.anchor_prefix(which)
        anchor_polynomial = None
        result_columns, entries = [], []
        for first in range(0, V3, PRODUCT_BATCH):
            stop = min(first+PRODUCT_BATCH, V3)
            name = "R839-anchor-"+which+"-products-"+str(first).zfill(4)+"-"+str(stop).zfill(4)
            old = self.get(name)
            if old is None:
                self.mark(name)
                if anchor_polynomial is None:
                    anchor_polynomial = self.pack(prefix)
                raw_products, real_products, original_sources = [], [], []
                for i in range(first, stop):
                    source_rows, source = self.original_prefix(3, i)
                    product = anchor_polynomial.mul_low(self.pack(source_rows), ORDERS*STRIDE)
                    raw = self.unpack(product)
                    real = self.real_rows(raw)
                    raw_products.append([x for row in raw for x in row])
                    real_products.append([x for row in real for x in row])
                    original_sources.append(source)
                target = nmod_mat(real_products, PRIME).transpose()
                selected = submatrix(target, self.s5_selected, list(range(stop-first)))
                coordinates = self.S5inv*selected
                assert self.S5*coordinates == target
                quotient_values = self.Q5*coordinates
                old = self.put(name, {
                    "prime": PRIME, "original_zeta_root": self.zeta_root, "anchor": which,
                    "first_original_V3_index": first, "stop_original_V3_index": stop,
                    "source_anchor_prefix": prefix_spec,
                    "source_original_V3_rows": original_sources,
                    "source_S5_matrix": self.s5_matrix_source,
                    "source_completed_S5_inverse": self.r827.source(S5_INVERSE),
                    "source_T5_quotient": self.q5_spec,
                    "qY_count": ORDERS, "xi_coordinate_count": XI,
                    "original_common_product_and_S5_integer_scale": str(82**10),
                    "original_xi_product_columns_mod_prime": raw_products,
                    "original_real_product_columns_mod_prime": real_products,
                    "S5_coordinates_mod_prime": rows(coordinates),
                    "Q5_image_mod_prime": rows(quotient_values),
                    "all_raw_xi_phase_symmetries_verified": True,
                    "all1380_original_product_coordinates_verified": True,
                    "same_prime_S5_inverse_reused_without_new_inverse": True,
                    "additional_product_or_anchor_rescaling": False,
                    "exact_unit_solve_expression": {
                        "operation": "coordinates_of_original_anchor_times_original_V3",
                        "anchor": self.anchor_specs[which], "original_V3_rows": original_sources,
                        "original_S5_index": self.r809.source(S5_INDEX),
                        "unit_minor_source": self.r827.source(S5_INVERSE),
                        "original_selected_rows": self.s5_selected,
                        "full_coordinate_window": [69, 20],
                        "exact_membership_reason": "original section multiplication V2 times V3 lies in V5",
                    },
                })
                del target, selected, coordinates, quotient_values
            assert old["prime"] == PRIME and old["anchor"] == which
            assert old["source_anchor_prefix"] == prefix_spec
            assert old["source_S5_matrix"] == self.s5_matrix_source
            assert old["source_completed_S5_inverse"] == self.r827.source(S5_INVERSE)
            assert old["source_T5_quotient"] == self.q5_spec
            assert (old["first_original_V3_index"], old["stop_original_V3_index"]) == (first, stop)
            assert old["all1380_original_product_coordinates_verified"] is True
            checked_shape(old["Q5_image_mod_prime"], T5_QUOTIENT_RANK, stop-first)
            for local in range(stop-first):
                result_columns.append([old["Q5_image_mod_prime"][r][local] for r in range(T5_QUOTIENT_RANK)])
            entries.append(self.output_source(name))
        assert len(result_columns) == V3
        return nmod_mat(result_columns, PRIME).transpose(), entries

    def D_matrix(self, U, U_sources, V, V_sources):
        name = "R839-original-D-short-kernel-matrix"
        old = self.get(name)
        if old is None:
            self.mark(name)
            data = rows(U)+rows(V)
            old = self.put(name, {
                "prime": PRIME, "matrix_shape": [830, V3],
                "matrix_mod_prime": data,
                "source_T5_quotient": self.q5_spec,
                "source_original_fixed_branch_pencil": self.pencil_spec,
                "source_u_product_groups": U_sources, "source_v_product_groups": V_sources,
                "domain": "the original R786 ordinary V3 basis, integer scale82^6",
                "exact_kernel": "H0(3H-D)", "exact_kernel_dimension": 295,
                "exact_characteristic_zero_rank": D_RANK,
                "P0_integral_colon_truncation_preserved": True,
                "actual_P0_multiplicity_in_D": 0,
                "both_original_fixed_anchors_used": True,
            })
        assert old["source_T5_quotient"] == self.q5_spec
        assert old["source_u_product_groups"] == U_sources and old["source_v_product_groups"] == V_sources
        checked_shape(old["matrix_mod_prime"], 830, V3)
        return nmod_mat(old["matrix_mod_prime"], PRIME), self.output_source(name)

    def D_kernel(self, matrix, source):
        name = "R839-original-D-unit-kernel-basis"
        old = self.get(name)
        if old is None:
            self.mark(name)
            echelon, rank = matrix.rref()
            assert rank <= D_RANK, "A rank above395 contradicts the exact original colon/RR bound."
            P = pivots(echelon, rank)
            value = {
                "prime": PRIME, "source_original_D_matrix": source,
                "actual_rank": rank, "required_rank": D_RANK,
                "exact_original_D_RR_space_as_unit_chart_expression_certified": False,
                "expanded_characteristic_zero_coordinates_computed": False,
                "failed_modular_rank_does_not_disprove_characteristic_zero_fullness": rank != D_RANK,
            }
            if rank == D_RANK:
                occupied = set(P)
                F = [j for j in range(V3) if j not in occupied]
                assert len(F) == 295
                pivot_matrix = submatrix(matrix, list(range(830)), P)
                row_echelon, row_rank = pivot_matrix.transpose().rref()
                assert row_rank == rank
                I = pivots(row_echelon, rank)
                square = submatrix(matrix, I, P)
                determinant = int(square.det())
                assert determinant
                basis = [[0]*len(F) for _ in range(V3)]
                for j, free in enumerate(F):
                    basis[free][j] = 1
                    for r, pivot in enumerate(P):
                        basis[pivot][j] = (-int(echelon[r, free])) % PRIME
                kernel = nmod_mat(basis, PRIME)
                assert matrix*kernel == matrix_zero(830, len(F))
                assert submatrix(kernel, F, list(range(len(F)))) == identity(len(F))
                value.update({
                    "selected_original_equation_rows": I,
                    "selected_original_V3_pivot_columns": P,
                    "original_V3_free_columns": F,
                    "actual_minor_determinant_mod_prime": determinant,
                    "kernel_basis_mod_prime": basis,
                    "all830_original_equations_verified_for_all295_columns": True,
                    "original_free_normalization_identity_verified": True,
                    "exact_original_D_RR_space_as_unit_chart_expression_certified": True,
                    "exact_unit_solve_expression": {
                        "operation": "normalized_kernel_of_original_selected_equations",
                        "original_matrix": source, "equation_rows": I,
                        "pivot_columns": P, "free_columns": F,
                        "pivot_coordinates": "-solve(K[I,P],K[I,f])",
                        "free_coordinates": "one original free coordinate1, all other free coordinates0",
                        "exact_kernel": "H0(3H-D)", "exact_dimension": 295,
                        "coefficient_field": "the original L, with the original K anchor scales",
                    },
                })
                del pivot_matrix, row_echelon, square, kernel
            old = self.put(name, value)
            del echelon
        assert old["source_original_D_matrix"] == source
        self.last_ranks["D"] = old["actual_rank"]
        self.kernel_spec = self.output_source(name)
        return old

    def inventory(self):
        entries = []
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name == INVENTORY:
                continue
            value = read(path)
            assert value["complete"] is True and value["configuration"] == self.tag
            assert value["result"] == RESULT
            entries.append(spec(path))
        value = {
            "result": RESULT, "configuration": self.tag, "complete": True,
            "files": entries, "only_actual_complete_source_bound_stages_listed": True,
            "inventory_does_not_list_itself": True,
        }
        save(self.out/INVENTORY, value)
        return spec(self.out/INVENTORY), len(entries)

    def finish(self, reason, error=None):
        t11 = self.get("R839-T11-unit-quotient")
        t5 = self.get("R839-T5-independent-original-row-quotient")
        d = self.get("R839-original-D-unit-kernel-basis")
        flags = {
            "exact_original_T11_as_unit_chart_expression_certified": bool(t11 and t11.get("exact_original_T11_as_unit_chart_expression_certified")),
            "exact_original_T5_quotient_as_unit_chart_expression_certified": bool(t5 and t5.get("exact_original_T5_quotient_as_unit_chart_expression_certified")),
            "exact_original_D_RR_space_as_unit_chart_expression_certified": bool(d and d.get("exact_original_D_RR_space_as_unit_chart_expression_certified")),
        }
        complete = all(flags.values())
        manifest, count = self.inventory()
        certificate = {
            "result": RESULT, "configuration": self.tag, "complete": complete, "p": 41,
            "prime": PRIME, "original_branch": 0,
            **flags,
            "actual_T11_rank": self.last_ranks["T11"],
            "actual_T5_rank": self.last_ranks["T5"],
            "actual_D_kernel_rank": self.last_ranks["D"],
            "actual_D_RR_dimension": 295 if flags["exact_original_D_RR_space_as_unit_chart_expression_certified"] else None,
            "source_audit": self.output_source("R839-original-source-audit") if self.get("R839-original-source-audit") else None,
            "T11_quotient": self.output_source("R839-T11-unit-quotient") if t11 else None,
            "T5_quotient": self.output_source("R839-T5-independent-original-row-quotient") if t5 else None,
            "D_kernel_basis": self.output_source("R839-original-D-unit-kernel-basis") if d else None,
            "stage_manifest": manifest, "complete_math_stage_count": count,
            "stop_reason": reason, "error": error,
            "expanded_characteristic_zero_coordinates_computed": False,
            "actual_eta_or_height_computed": False,
            "old_derivatives_or_same_prime_S5_inverse_recomputed": False,
            "all_original_anchor_and_82power_scales_preserved": True,
            "seconds": time.monotonic()-self.started,
        }
        save(self.out/FINAL, certificate)
        save(self.out/"core-receipt.json", {
            "result": RESULT, "source_sha256": sha(__file__), "complete": complete,
            "certificate_sha256": sha(self.out/FINAL), **flags,
            "actual_T11_rank": self.last_ranks["T11"],
            "actual_T5_rank": self.last_ranks["T5"],
            "actual_D_kernel_rank": self.last_ranks["D"],
            "stop_reason": reason, "error": error,
            "seconds": time.monotonic()-self.started,
            "expanded_characteristic_zero_coordinates_computed": False,
            "actual_eta_or_height_computed": False,
        })
        print(json.dumps({"complete": complete, **flags, "ranks": self.last_ranks,
                          "stop_reason": reason, "seconds": certificate["seconds"]}), flush=True)
        return complete

    def run(self):
        self.source_audit()
        self.homogeneous_matrix()
        selection, selection_spec = self.T11_columns()
        if selection["actual_rank"] != T11_DIM:
            self.finish("T11_actual_modular_rank_below_required_sufficient_rank")
            return 2
        self.T11_quotient(selection, selection_spec)
        del self.Phi
        self.Phi = None
        gc.collect()
        matrix5, source5 = self.T5_matrix()
        quotient = self.T5_quotient(matrix5, source5)
        if quotient["actual_rank"] != T5_QUOTIENT_RANK:
            self.finish("T5_actual_modular_rank_below_exact_characteristic_zero_rank")
            return 2
        del matrix5, self.Pi
        self.Pi = None
        gc.collect()
        self.S5_matrix()
        U, U_sources = self.anchor_products("u")
        V, V_sources = self.anchor_products("v")
        self.S5 = self.S5inv = None
        gc.collect()
        matrix_D, source_D = self.D_matrix(U, U_sources, V, V_sources)
        del U, V
        kernel = self.D_kernel(matrix_D, source_D)
        if kernel["actual_rank"] != D_RANK:
            self.finish("D_actual_modular_rank_below_exact_characteristic_zero_rank")
            return 2
        assert self.finish("certified_original_short_RR_and_D_kernel")
        return 0


def main():
    guard()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, required=True)
    args = parser.parse_args()
    assert args.budget_minutes > 0
    args.out.mkdir(parents=True, exist_ok=True)
    job = None
    try:
        job = Job(args)
        return job.run()
    except BudgetStop as error:
        if job is not None:
            job.finish("budget_stop", str(error))
        else:
            save(args.out/"core-receipt.json", {
                "result": RESULT, "source_sha256": sha(__file__), "complete": False,
                "stop_reason": "budget_stop_during_initialization", "error": str(error),
            })
        return 124
    except Exception as error:
        traceback.print_exc()
        if job is not None:
            job.finish("exception", str(error))
        else:
            save(args.out/"core-receipt.json", {
                "result": RESULT, "source_sha256": sha(__file__), "complete": False,
                "stop_reason": "exception_during_initialization", "error": str(error),
            })
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
