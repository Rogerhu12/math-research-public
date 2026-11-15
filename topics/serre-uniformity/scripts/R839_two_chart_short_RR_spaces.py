#!/usr/bin/env python3
"""Complete the original R839 source by its actual second-chart columns."""
import argparse
import gc
import hashlib
import importlib.util
import json
from pathlib import Path
import time
import traceback

LEGACY_SHA = "0a027c2dd83cfab37181e6386cfd8b22baf176421b727d81a7584d7b351d0c36"
LEGACY_NAME = "R839_original_short_RR_spaces.py"


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


legacy_path = Path(__file__).resolve().parent/LEGACY_NAME
assert sha(legacy_path) == LEGACY_SHA
loader = importlib.util.spec_from_file_location("R839_frozen_original_short_RR_math", legacy_path)
L = importlib.util.module_from_spec(loader)
loader.loader.exec_module(L)

RESULT = "R839-original-two-chart-short-RR-spaces-and-D-kernel"
FINAL = "p41-original-two-chart-short-RR-and-D-kernel-certificate.json"
INVENTORY = "R839-two-chart-stage-manifest.json.gz"
PRIME, FREE, EPS = L.PRIME, L.FREE, L.EPS
OLD_CONFIGURATION = "111621ab17dfb725e3898319e9b421883663d0eac2bfc7dc28d11e42ef978e33"
OLD_MATRIX = "R839-T11-shifted-source-matrix.json.gz"
OLD_RANK = "R839-T11-source-column-rank.json.gz"
SIGMA_JETS = "R827-sigma-layer-001-precision-0004-index.json.gz"
SIGMA_INFINITY = "R827-sigma-infinity-order-0004-certificate.json.gz"
SIGMA_COLUMNS = [0]+list(range(73, 92))
SIGMA_INDEXES = {target: "R827-target-"+target+"-sigma-polynomial-index.json.gz"
                 for target in ("B", "g", "Gamma")}
SCOPE = {
    "auxiliary_prime": PRIME, "original_branch": 0,
    "normal_basis_rank": FREE, "normal_basis_degrees": EPS,
    "uniform_homogeneous_weight": 11,
    "old_tau_matrix_shape": [2866, 2886], "old_actual_tau_rank": 2431,
    "sigma_first_derivative_columns": SIGMA_COLUMNS,
    "old_sigma_coefficient_range": [0, 4], "new_sigma_coefficient_range": [4, 10],
    "new_sigma_shifted_matrix_shape": [2866, 81],
    "old_selected_column_quotient_shape": [435, 2866],
    "incremental_quotient_matrix_shape": [435, 81],
    "required_added_rank": 20, "T11_required_rank": 2451,
    "T5_matrix_shape": [830, 1234], "T5_required_rank": 415,
    "D_matrix_shape": [830, 690], "D_required_rank": 395, "D_RR_dimension": 295,
    "old_tau_matrix_or_complete_column_RREF_recomputed": False,
    "old_sigma_coefficients_zero_through_three_recomputed": False,
    "sigma_stored_g_already_is_signed_base_variable_derivative": True,
    "old_same_prime_S5_inverse_or_Fourier_prefixes_recomputed": False,
    "all_new_global_sources_are_original_sigma_homogenizations": True,
    "old_tau_rank_not_asserted_as_full_characteristic_zero_tau_rank": True,
    "accurate_characteristic_zero_objects_are_source_bound_unit_solve_expressions": True,
    "budget_and_absolute_directories_excluded_from_mathematical_identity": True,
}
read, save, plain, spec = L.read, L.save, L.plain, L.spec
rows, pivots, submatrix = L.rows, L.pivots, L.submatrix
zero, identity, nmod_mat = L.matrix_zero, L.identity, L.nmod_mat


class Job(L.Job):
    def __init__(self, args):
        self.args, self.started = args, time.monotonic()
        self.item = read(args.config)
        assert self.item["result"] == RESULT and self.item["core_sha256"] == sha(__file__)
        assert self.item["legacy_core"] == LEGACY_NAME
        assert self.item["legacy_core_sha256"] == LEGACY_SHA
        for key in ("proof", "completion_proof", "method"):
            assert sha(self.item[key]) == self.item[key+"_sha256"]
        self.out = args.out
        self.out.mkdir(parents=True, exist_ok=True)
        self.sources = {label: L.Source(label, self.item["sources"][label]) for label in L.LABELS}
        self.previous = L.Source("R839_tau", self.item["previous_tau_source"])
        assert self.previous.identity["result"] == L.RESULT
        assert self.previous.identity["core_sha256"] == LEGACY_SHA
        assert self.previous.identity["configuration_sha256"] == OLD_CONFIGURATION
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "python_flint": L.flint.__version__,
            "p": 41, "legacy_R839_core_sha256": LEGACY_SHA,
            "R839_corrected_proof_sha256": self.item["proof_sha256"],
            "R839_two_chart_completion_proof_sha256": self.item["completion_proof_sha256"],
            "R839_two_chart_method_sha256": self.item["method_sha256"],
            "sources": {label: self.sources[label].stable() for label in L.LABELS},
            "previous_tau_source": self.previous.stable(),
            "frozen_original_tail_scope": L.MATH_SCOPE,
            **SCOPE,
        }
        self.r827, self.r838, self.r837 = (self.sources[x] for x in ("R827", "R838", "R837"))
        self.r809, self.r786 = self.sources["R809"], self.sources["R786"]
        self.positions11, self.positions5 = L.normal_positions(11), L.normal_positions(5)
        self.position11_index = {value: i for i, value in enumerate(self.positions11)}
        self.current_stage = "initializing"
        self.last_ranks = {"T11": None, "T5": None, "D": None}
        self.audit_data = None
        self.Phi = self.Pi = self.Q5 = self.S5 = self.S5inv = None
        self.Phi_spec = self.quotient_spec = self.q5_spec = self.kernel_spec = None
        self.s5_matrix_source = None
        self.g_t, self.chebyshev = None, None
        self.complete = False
        self.T0 = self.Pi0 = self.sigma_matrix = self.added_image = None
        self.old_row_quotient_spec = self.sigma_matrix_spec = self.augmentation_spec = None
        self.sigma_arrays = None

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

    def source_audit(self):
        # This inherited method only checks the original producer expressions.
        original_audit = super().source_audit()
        name = "R839-two-chart-original-source-audit"
        old = self.get(name)
        final = self.previous.certificate
        assert final is not None and final["complete"] is False
        assert final["actual_T11_rank"] == 2431
        assert final["actual_T5_rank"] is None and final["actual_D_kernel_rank"] is None
        assert final["stop_reason"] == "T11_actual_modular_rank_below_required_sufficient_rank"
        assert final["error"] is None
        previous_tag = final["configuration"]
        assert L.fingerprint(previous_tag) == OLD_CONFIGURATION
        for label in L.LABELS:
            original = previous_tag["sources"][label]
            current = self.sources[label].stable()
            for key in L.BASE_KEYS:
                assert original[key] == current[key]
            assert original["certificate_name"] == current["certificate_name"]
            for file, source in original["files"].items():
                assert source == current["files"][file]
        run = self.previous.raw("run-receipt.json")
        core = self.previous.raw("core-receipt.json")
        initial = self.previous.raw("public-actions-input.json")
        assert run["complete"] is False and run["process_exit_code"] == 2 and run["error"] is None
        assert run["source_commit"] == initial["source_commit"] == self.previous.identity["source_commit"]
        assert str(run["workflow_run_id"]) == str(self.previous.identity["run_id"])
        assert core["source_sha256"] == initial["core_sha256"] == LEGACY_SHA
        assert run["core_receipt_sha256"] == self.previous.files["core-receipt.json"]["sha256"]
        assert core["certificate_sha256"] == self.previous.files[self.previous.item["certificate_name"]]["sha256"]
        self.old_selection = self.previous.stage(OLD_RANK)
        assert self.old_selection["actual_rank"] == 2431
        assert self.old_selection["required_rank"] == 2451
        assert self.old_selection["all_2866_rows_and_2886_columns_used"] is True
        assert plain(self.old_selection["source_matrix"]) == plain(self.previous.source(OLD_MATRIX))
        self.old_columns = self.old_selection["independent_original_source_column_indices"]
        assert len(self.old_columns) == len(set(self.old_columns)) == 2431
        assert self.old_columns == sorted(self.old_columns) and 0 <= self.old_columns[0] <= self.old_columns[-1] < 2886
        self.infinity = self.r827.stage(SIGMA_INFINITY)
        assert self.infinity["prime"] == PRIME and self.infinity["actual_rank_mod_prime"] == FREE
        assert self.infinity["actual_full_minor_determinant_mod_prime"] == 695832206
        assert self.infinity["whole_infinity_fiber_surjective"] is True
        assert self.infinity["actual_C_sigma_determinant_at_zero"] != 0
        assert self.infinity["actual_selected_pivot_columns"] == list(range(252))+[272]+list(range(345, 364))
        assert [i-FREE for i in self.infinity["actual_selected_pivot_columns"] if i >= FREE] == SIGMA_COLUMNS
        assert plain(self.infinity["source_layer_jets"][1]["source"]) == plain(self.r827.source(SIGMA_JETS))
        self.sigma_jet_index = self.r827.stage(SIGMA_JETS)
        assert self.sigma_jet_index["chart"] == "sigma" and self.sigma_jet_index["derivative_order"] == 1
        assert self.sigma_jet_index["precision_stop"] == 4
        assert self.sigma_jet_index["full_polynomial_coefficients_computed"] is False
        assert self.sigma_jet_index["all_required_coefficient_blocks_complete"] is True
        assert len(self.sigma_jet_index["coefficient_row_blocks"]) == 68
        self.sigma_operator_indexes = {}
        identities = self.r827.stage("R827-complete-short-operator-identities-and-sigma-transport.json.gz")
        for target, filename in SIGMA_INDEXES.items():
            assert plain(identities["operator_indexes"][target]["sigma"]) == plain(self.r827.source(filename))
            index = self.r827.stage(filename)
            assert index["target"] == target and index["chart"] == "sigma" and index["prime"] == PRIME
            assert index["normal_basis_rank"] == FREE and index["normal_basis_degrees"] == EPS
            assert index["regular_degree_bound"] == {"B": 5, "g": 3, "Gamma": 2}[target]
            assert index["all_negative_powers_and_weighted_zeros_verified"] is True
            assert index["g_matrix_means_negative_sigma_base_derivative"] is (target == "g")
            assert len(index["row_blocks"]) == 17
            self.sigma_operator_indexes[target] = index
        if old is None:
            self.mark(name)
            old = self.put(name, {
                "prime": PRIME, "source_original_audit": original_audit,
                "source_previous_tau_certificate": self.previous.source(self.previous.item["certificate_name"]),
                "source_previous_tau_matrix": self.previous.source(OLD_MATRIX),
                "source_previous_tau_column_selection": self.previous.source(OLD_RANK),
                "previous_actual_tau_rank": 2431,
                "source_original_sigma_infinity_certificate": self.r827.source(SIGMA_INFINITY),
                "selected_sigma_first_derivative_columns": SIGMA_COLUMNS,
                "source_completed_sigma_jets": self.r827.source(SIGMA_JETS),
                "source_sigma_operator_indexes": {k:self.r827.source(v) for k,v in SIGMA_INDEXES.items()},
                "old_output_stages_keep_their_original_tags": True,
                "original_global_I2_source_completed_by_actual_infinity_minor": True,
                "previous_tau_rank_not_promoted_to_characteristic_zero_equality": True,
                "new_Fourier_or_normalized_Dixon_arithmetic": False,
            })
        assert old["source_previous_tau_column_selection"] == self.previous.source(OLD_RANK)
        return self.output_source(name)

    def old_selected_matrix(self):
        if self.T0 is not None:
            return self.T0
        value = self.previous.stage(OLD_MATRIX)
        assert value["prime"] == PRIME and value["matrix_shape"] == [2866, 2886]
        assert value["row_labels"] == [list(x) for x in self.positions11]
        assert value["all_original_weight_bounds_verified"] is True
        assert value["source_original_layer_indexes"] == self.layer_sources
        data = value["matrix_mod_prime"]
        L.checked_shape(data, 2866, 2886)
        self.T0 = nmod_mat([[row[c] for c in self.old_columns] for row in data], PRIME)
        del value, data
        gc.collect()
        return self.T0

    def old_row_quotient(self):
        name = "R839-two-chart-old-selected-column-unit-quotient"
        old = self.get(name)
        T = self.old_selected_matrix()
        if old is None:
            self.mark(name)
            echelon, rank = T.transpose().rref()
            assert rank == 2431
            I = pivots(echelon, rank)
            occupied = set(I)
            R = [i for i in range(2866) if i not in occupied]
            assert len(R) == 435
            square = submatrix(T, I, list(range(rank)))
            determinant = int(square.det())
            assert determinant
            P = [[0]*2866 for _ in R]
            for r, original in enumerate(R):
                P[r][original] = 1
                for j, pivot in enumerate(I):
                    P[r][pivot] = (-int(echelon[j, original])) % PRIME
            matrix = nmod_mat(P, PRIME)
            assert matrix*T == zero(435, 2431)
            assert submatrix(matrix, list(range(435)), R) == identity(435)
            old = self.put(name, {
                "prime": PRIME, "source_previous_tau_matrix": self.previous.source(OLD_MATRIX),
                "source_previous_tau_column_selection": self.previous.source(OLD_RANK),
                "selected_original_source_columns": self.old_columns,
                "selected_original_rows": I, "complement_original_rows": R,
                "actual_rank": rank, "actual_minor_determinant_mod_prime": determinant,
                "quotient_matrix_mod_prime": P,
                "all_selected_2431_columns_annihilated_in_all435_rows": True,
                "complement_identity_verified": True,
                "old_full_2886_column_RREF_recomputed": False,
                "exact_kernel_only_asserted_to_be_the_selected_original_column_span": True,
                "exact_unit_solve_expression": {
                    "operation": "x_R-T0_R*solve(T0_I,x_I)",
                    "original_matrix": self.previous.source(OLD_MATRIX),
                    "selected_columns": self.old_columns,
                    "selected_rows": I, "complement_rows": R,
                    "no_assertion_of_full_tau_characteristic_zero_rank": True,
                },
            })
            del echelon, square, matrix
        assert old["source_previous_tau_matrix"] == self.previous.source(OLD_MATRIX)
        assert old["selected_original_source_columns"] == self.old_columns
        L.checked_shape(old["quotient_matrix_mod_prime"], 435, 2866)
        self.old_row_data = old
        self.Pi0 = nmod_mat(old["quotient_matrix_mod_prime"], PRIME)
        self.old_row_quotient_spec = self.output_source(name)
        return self.old_row_quotient_spec

    def sigma_operator(self, target):
        index = self.sigma_operator_indexes[target]
        degree = index["regular_degree_bound"]
        count = degree+3
        width = len(SIGMA_COLUMNS) if target == "B" else FREE
        data = [[[0]*width for _ in range(FREE)] for _ in range(count)]
        covered = set()
        for entry in index["row_blocks"]:
            value = self.r827.stage(entry)
            first, stop = value["row_first"], value["row_stop"]
            assert value["prime"] == PRIME and value["target"] == target and value["chart"] == "sigma"
            assert value["regular_degree_bound"] == degree
            assert value["all_negative_powers_and_weighted_zeros_verified"] is True
            assert value["g_matrix_means_negative_sigma_base_derivative"] is (target == "g")
            assert 0 <= first < stop <= FREE and stop-first <= 16
            coeffs = value["coefficient_matrices_low_to_high"]
            assert len(coeffs) == count
            for n, block in enumerate(coeffs):
                L.checked_shape(block, stop-first, FREE)
                for local, row in enumerate(block):
                    key = n, first+local
                    assert key not in covered
                    covered.add(key)
                    for c, x in enumerate(row):
                        if n > degree+EPS[c]-EPS[first+local]:
                            assert x == 0
                    data[n][first+local] = [row[c] for c in SIGMA_COLUMNS] if target == "B" else row
        assert len(covered) == count*FREE
        return [nmod_mat(a, PRIME) for a in data]

    def completed_sigma_coefficients(self):
        old_values = [[[0]*len(SIGMA_COLUMNS) for _ in range(FREE)] for _ in range(4)]
        covered = set()
        original_sources = []
        for entry in self.sigma_jet_index["coefficient_row_blocks"]:
            value = self.r827.stage(entry)
            first, stop, n = value["row_first"], value["row_stop"], value["coefficient_exponent"]
            assert value["chart"] == "sigma" and value["derivative_order"] == 1
            assert value["prime"] == PRIME and 0 <= n < 4
            assert value["original_weighted_support_verified"] is True
            assert value["sigma_negative_base_derivative_preserved"] is True
            assert value["source_original_generator_weights"] == [5+e for e in EPS]
            assert plain(value["source_previous_layer"]) == plain(self.r827.source(SIGMA_INDEXES["B"]))
            assert plain(value["source_Gamma_operator"]) == plain(self.r827.source(SIGMA_INDEXES["Gamma"]))
            assert plain(value["source_base_derivative_operator"]) == plain(self.r827.source(SIGMA_INDEXES["g"]))
            block = value["coefficient_matrix_mod_prime"]
            L.checked_shape(block, stop-first, FREE)
            for local, row in enumerate(block):
                key = n, first+local
                assert key not in covered
                covered.add(key)
                old_values[n][first+local] = [row[c] for c in SIGMA_COLUMNS]
            original_sources.append(self.r827.source(entry))
        assert len(covered) == 4*FREE
        # Compare the copied constant coefficient with its already completed
        # infinity minor; this is source identity, not a new determinant.
        minor = self.infinity["actual_full_minor_matrix_mod_prime"]
        L.checked_shape(minor, FREE, FREE)
        for r in range(FREE):
            for j in range(len(SIGMA_COLUMNS)):
                assert old_values[0][r][j] == minor[r][252+j]
        values = [nmod_mat(a, PRIME) for a in old_values]
        new_sources = []
        sigma_B = sigma_Gamma = sigma_g = None
        for n in range(4, 10):
            name = "R839-two-chart-sigma-first-selected-coefficient-"+str(n).zfill(2)
            old = self.get(name)
            if old is None:
                self.mark(name)
                if sigma_B is None:
                    sigma_B = self.sigma_operator("B")
                    sigma_Gamma = self.sigma_operator("Gamma")
                    sigma_g = self.sigma_operator("g")
                value = zero(FREE, len(SIGMA_COLUMNS))
                for a, matrix in enumerate(sigma_Gamma):
                    b = n-a
                    if 0 <= b < len(sigma_B):
                        value += matrix*sigma_B[b]
                for a, matrix in enumerate(sigma_g):
                    b = n-a+1
                    if 1 <= b < len(sigma_B):
                        value += (matrix*sigma_B[b])*b
                raw = rows(value)
                for r in range(FREE):
                    for j, c in enumerate(SIGMA_COLUMNS):
                        if n > 7+EPS[c]-EPS[r]:
                            assert raw[r][j] == 0
                if n == 9:
                    assert value == zero(FREE, len(SIGMA_COLUMNS))
                old = self.put(name, {
                    "prime": PRIME, "chart": "sigma", "derivative_order": 1,
                    "coefficient_exponent": n, "original_normal_columns": SIGMA_COLUMNS,
                    "coefficient_matrix_mod_prime": raw,
                    "source_original_sigma_operator_indexes": {
                        target:self.r827.source(filename) for target,filename in SIGMA_INDEXES.items()},
                    "source_original_sigma_operator_blocks": {
                        target:[self.r827.source(row) for row in self.sigma_operator_indexes[target]["row_blocks"]]
                        for target in SIGMA_INDEXES},
                    "source_completed_lower_sigma_coefficients": self.r827.source(SIGMA_JETS),
                    "old_coefficients_zero_through_three_recomputed": False,
                    "stored_sigma_g_used_with_original_negative_sign_once": True,
                    "all_original_weighted_support_zeros_verified": True,
                    "complete_new_row_range": [0, FREE],
                    "exact_characteristic_zero_expression": {
                        "operation": "original_sigma_connection_first_derivative_coefficient",
                        "coefficient_exponent": n, "original_columns": SIGMA_COLUMNS,
                        "formula": "sum(Gamma_a*B_b,a+b=n)+sum(Gderiv_a*b*B_b,a+b-1=n)",
                        "all_sources_are_original_unit_chart_operator_expressions": True,
                    },
                })
                del value
            assert old["coefficient_exponent"] == n and old["original_normal_columns"] == SIGMA_COLUMNS
            assert old["source_completed_lower_sigma_coefficients"] == self.r827.source(SIGMA_JETS)
            assert old["all_original_weighted_support_zeros_verified"] is True
            L.checked_shape(old["coefficient_matrix_mod_prime"], FREE, len(SIGMA_COLUMNS))
            values.append(nmod_mat(old["coefficient_matrix_mod_prime"], PRIME))
            new_sources.append(self.output_source(name))
        for n, value in enumerate(values):
            for r in range(FREE):
                for j, c in enumerate(SIGMA_COLUMNS):
                    if n > 7+EPS[c]-EPS[r]:
                        assert not value[r, j]
        self.sigma_arrays = values
        self.sigma_original_sources = original_sources
        self.sigma_new_sources = new_sources
        del sigma_B, sigma_Gamma, sigma_g
        gc.collect()

    def sigma_shifted_matrix(self):
        name = "R839-two-chart-sigma-first-81-shifted-columns"
        old = self.get(name)
        if old is None:
            self.completed_sigma_coefficients()
            self.mark(name)
            matrix = [[0]*81 for _ in range(2866)]
            labels = []
            position = 0
            for j, c in enumerate(SIGMA_COLUMNS):
                weight = 7+EPS[c]
                for shift in range(12-weight):
                    labels.append(["sigma", 1, c, shift])
                    for n, coefficient in enumerate(self.sigma_arrays):
                        for r in range(FREE):
                            value = int(coefficient[r, j])
                            exponent = weight-EPS[r]-n
                            if exponent < 0:
                                assert value == 0
                            elif value:
                                target = exponent+shift
                                assert 0 <= target <= 11-EPS[r]
                                matrix[self.position11_index[r, target]][position] = value
                    position += 1
            assert position == 81
            old = self.put(name, {
                "prime": PRIME, "matrix_shape": [2866, 81],
                "row_labels": [list(x) for x in self.positions11],
                "column_labels": labels, "matrix_mod_prime": matrix,
                "source_original_infinity_certificate": self.r827.source(SIGMA_INFINITY),
                "source_completed_original_sigma_coefficients": self.sigma_original_sources,
                "source_new_sigma_coefficients": self.sigma_new_sources,
                "all_original_weighted_support_and_reflection_indices_verified": True,
                "old_zero_through_three_coefficients_only_copied": True,
                "exact_source_expression": {
                    "operation": "homogenize_original_sigma_first_derivative_columns",
                    "original_columns": SIGMA_COLUMNS,
                    "uniform_weight": 11,
                    "tau_coordinate_formula": "z^(7+eps_c-eps_b)*F1_sigma_bc(1/z)",
                    "original_global_weight": "7+eps_c",
                    "shift_rule": "tau^(11-w-k)*sigma^k",
                    "contains_no_discarded_negative_power": True,
                },
            })
            self.sigma_arrays = None
            gc.collect()
        assert old["row_labels"] == [list(x) for x in self.positions11]
        assert old["source_original_infinity_certificate"] == self.r827.source(SIGMA_INFINITY)
        L.checked_shape(old["matrix_mod_prime"], 2866, 81)
        self.sigma_matrix = nmod_mat(old["matrix_mod_prime"], PRIME)
        self.sigma_matrix_spec = self.output_source(name)
        return self.sigma_matrix_spec

    def incremental_columns(self):
        name = "R839-two-chart-incremental-435-by81-column-rank"
        old = self.get(name)
        if old is None:
            self.mark(name)
            image = self.Pi0*self.sigma_matrix
            reduced, rank = image.rref()
            assert rank <= 20, "True original source columns cannot exceed the exact T11 dimension."
            J = pivots(reduced, rank)
            old = self.put(name, {
                "prime": PRIME, "source_old_selected_column_quotient": self.old_row_quotient_spec,
                "source_new_sigma_columns": self.sigma_matrix_spec,
                "matrix_shape": [435, 81], "matrix_mod_prime": rows(image),
                "actual_added_rank": rank, "required_added_rank": 20,
                "actual_combined_selected_rank": 2431+rank,
                "independent_new_sigma_column_indices": J,
                "original_tau_full_column_RREF_repeated": False,
                "actual_rank_is_sufficient": rank == 20,
                "rank_deficiency_does_not_negate_global_two_chart_source_generation": rank != 20,
            })
            del image, reduced
        assert old["source_old_selected_column_quotient"] == self.old_row_quotient_spec
        assert old["source_new_sigma_columns"] == self.sigma_matrix_spec
        L.checked_shape(old["matrix_mod_prime"], 435, 81)
        self.added_image = nmod_mat(old["matrix_mod_prime"], PRIME)
        self.augmentation_spec = self.output_source(name)
        self.last_ranks["T11"] = old["actual_combined_selected_rank"]
        return old

    def completed_T11_quotient(self, augmentation):
        name = "R839-T11-unit-quotient"
        old = self.get(name)
        assert augmentation["actual_added_rank"] == 20
        J = augmentation["independent_new_sigma_column_indices"]
        assert len(J) == 20
        if old is None:
            self.mark(name)
            added = submatrix(self.added_image, list(range(435)), J)
            reduced, rank = added.transpose().rref()
            assert rank == 20
            I = pivots(reduced, rank)
            occupied = set(I)
            R = [i for i in range(435) if i not in occupied]
            assert len(R) == 415
            square = submatrix(added, I, list(range(20)))
            schur_determinant = int(square.det())
            assert schur_determinant
            solve_coeffs = nmod_mat([[int(reduced[j, r]) for j in range(20)] for r in R], PRIME)
            quotient = submatrix(self.Pi0, R, list(range(2866))) - \
                       solve_coeffs*submatrix(self.Pi0, I, list(range(2866)))
            complement = [self.old_row_data["complement_original_rows"][r] for r in R]
            original_rows = self.old_row_data["selected_original_rows"] + \
                            [self.old_row_data["complement_original_rows"][r] for r in I]
            assert len(original_rows) == len(set(original_rows)) == 2451
            assert quotient*self.T0 == zero(415, 2431)
            assert quotient*submatrix(self.sigma_matrix, list(range(2866)), J) == zero(415, 20)
            assert submatrix(quotient, list(range(415)), complement) == identity(415)
            combined_determinant = self.old_row_data["actual_minor_determinant_mod_prime"]*schur_determinant % PRIME
            assert combined_determinant
            old = self.put(name, {
                "prime": PRIME,
                "source_previous_tau_matrix": self.previous.source(OLD_MATRIX),
                "source_previous_tau_column_selection": self.previous.source(OLD_RANK),
                "source_old_selected_column_quotient": self.old_row_quotient_spec,
                "source_new_sigma_columns": self.sigma_matrix_spec,
                "source_incremental_column_selection": self.augmentation_spec,
                "actual_rank": 2451,
                "selected_original_tau_columns": self.old_columns,
                "selected_new_sigma_columns": J,
                "selected_original_rows": original_rows,
                "complement_original_rows": complement,
                "actual_20_by20_schur_minor_determinant_mod_prime": schur_determinant,
                "actual_minor_determinant_mod_prime": combined_determinant,
                "combined_minor_row_order": "old selected rows followed by selected old-complement rows",
                "combined_minor_column_order": "old selected tau columns followed by selected new sigma columns",
                "quotient_matrix_mod_prime": rows(quotient),
                "all_2451_source_columns_annihilated_in_all415_rows": True,
                "complement_identity_verified": True,
                "exact_original_T11_as_unit_chart_expression_certified": True,
                "expanded_characteristic_zero_coordinates_computed": False,
                "exact_unit_solve_expression": {
                    "operation": "x_R-T_R*solve(T_I,x_I)",
                    "original_tau_matrix": self.previous.source(OLD_MATRIX),
                    "new_sigma_matrix": self.sigma_matrix_spec,
                    "tau_columns": self.old_columns, "sigma_columns": J,
                    "selected_rows": original_rows, "complement_rows": complement,
                    "selected_matrix_column_order": "tau then sigma",
                    "unit_certificate": "product of the two recorded original block minors",
                    "exact_kernel": "H0(11H-E2)", "exact_kernel_dimension": 2451,
                },
            })
            del added, reduced, square, solve_coeffs, quotient
        assert old["source_old_selected_column_quotient"] == self.old_row_quotient_spec
        assert old["source_new_sigma_columns"] == self.sigma_matrix_spec
        assert old["source_incremental_column_selection"] == self.augmentation_spec
        assert old["exact_original_T11_as_unit_chart_expression_certified"] is True
        L.checked_shape(old["quotient_matrix_mod_prime"], 415, 2866)
        self.Pi = nmod_mat(old["quotient_matrix_mod_prime"], PRIME)
        self.quotient_spec = self.output_source(name)
        return self.quotient_spec

    def inventory(self):
        entries = []
        for path in sorted(self.out.glob("R839-*.json.gz")):
            if path.name == INVENTORY:
                continue
            value = read(path)
            assert value["complete"] is True and value["configuration"] == self.tag
            assert value["result"] == RESULT
            entries.append(spec(path))
        save(self.out/INVENTORY, {
            "result": RESULT, "configuration": self.tag, "complete": True,
            "files": entries, "only_actual_complete_source_bound_stages_listed": True,
            "inventory_does_not_list_itself": True,
        })
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
        optional = lambda name: self.output_source(name) if self.get(name) is not None else None
        certificate = {
            "result": RESULT, "configuration": self.tag, "complete": complete,
            "p": 41, "prime": PRIME, "original_branch": 0, **flags,
            "actual_T11_rank": self.last_ranks["T11"],
            "actual_T5_rank": self.last_ranks["T5"],
            "actual_D_kernel_rank": self.last_ranks["D"],
            "actual_D_RR_dimension": 295 if flags["exact_original_D_RR_space_as_unit_chart_expression_certified"] else None,
            "source_audit": optional("R839-two-chart-original-source-audit"),
            "old_selected_column_quotient": optional("R839-two-chart-old-selected-column-unit-quotient"),
            "sigma_shifted_columns": optional("R839-two-chart-sigma-first-81-shifted-columns"),
            "incremental_rank": optional("R839-two-chart-incremental-435-by81-column-rank"),
            "T11_quotient": optional("R839-T11-unit-quotient") if t11 else None,
            "T5_quotient": optional("R839-T5-independent-original-row-quotient") if t5 else None,
            "D_kernel_basis": optional("R839-original-D-unit-kernel-basis") if d else None,
            "stage_manifest": manifest, "complete_math_stage_count": count,
            "stop_reason": reason, "error": error,
            "previous_tau_full_matrix_and_column_selection_recomputed": False,
            "old_sigma_coefficients_zero_through_three_recomputed": False,
            "old_derivatives_or_same_prime_S5_inverse_recomputed": False,
            "all_original_anchor_and_82power_scales_preserved": True,
            "expanded_characteristic_zero_coordinates_computed": False,
            "actual_eta_or_height_computed": False,
            "seconds": time.monotonic()-self.started,
        }
        save(self.out/FINAL, certificate)
        save(self.out/"core-receipt.json", {
            "result": RESULT, "source_sha256": sha(__file__), "complete": complete,
            "certificate_sha256": sha(self.out/FINAL), **flags,
            "actual_T11_rank": self.last_ranks["T11"], "actual_T5_rank": self.last_ranks["T5"],
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
        self.old_row_quotient()
        self.sigma_shifted_matrix()
        augmentation = self.incremental_columns()
        if augmentation["actual_added_rank"] != 20:
            self.finish("two_chart_T11_added_rank_below_required_twenty")
            return 2
        self.completed_T11_quotient(augmentation)
        self.T0 = self.Pi0 = self.sigma_matrix = self.added_image = None
        gc.collect()
        matrix5, source5 = self.T5_matrix()
        quotient = self.T5_quotient(matrix5, source5)
        if quotient["actual_rank"] != 415:
            self.finish("T5_actual_modular_rank_below_exact_characteristic_zero_rank")
            return 2
        del matrix5
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
        if kernel["actual_rank"] != 395:
            self.finish("D_actual_modular_rank_below_exact_characteristic_zero_rank")
            return 2
        assert self.finish("certified_original_two_chart_short_RR_and_D_kernel")
        return 0


def main():
    L.guard()
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
    except L.BudgetStop as error:
        if job is not None:
            job.finish("budget_stop", str(error))
        else:
            save(args.out/"core-receipt.json", {"result": RESULT, "source_sha256": sha(__file__),
                 "complete": False, "stop_reason": "budget_stop_during_initialization", "error": str(error)})
        return 124
    except Exception as error:
        traceback.print_exc()
        if job is not None:
            job.finish("exception", str(error))
        else:
            save(args.out/"core-receipt.json", {"result": RESULT, "source_sha256": sha(__file__),
                 "complete": False, "stop_reason": "exception_during_initialization", "error": str(error)})
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
