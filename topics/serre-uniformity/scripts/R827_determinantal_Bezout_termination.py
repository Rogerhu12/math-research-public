#!/usr/bin/env python3
"""R827: determinant Bezout certificates from completed original C-basis columns.

All new arithmetic runs only in this public repository's GitHub Actions.
No original column, derivative layer, C division, Hermite operation or operator
is recomputed.  A right inverse is certified in adjugate-factored form only.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import time
import flint
from flint import nmod_mat, nmod_poly

REPOSITORY = "Rogerhu12/math-research-public"
RESULT = "R827-original-global-modular-derivative-termination"
FINAL = "p41-original-global-modular-derivative-termination-certificate.json"
MODE = "tau_determinantal_Bezout_and_sigma_infinity_rank"
PREFIX = "R827-det-"
SOURCE_CORE = "d9cf773976f3beff7f44ff30f8b593665f481470cb52297239710e0ce6e062d2"
ORIGINAL_PROOF = "17e9c828e01e652b1a73281bf2249ae2b39133faae3cf22384a5fd6d6a3d4a71"
PRIME, N, Q = 1000000753, 272, 4
EPS = [0]+[1]*144+[2]*127
PARAMETERS = (0, 1, -1, 2)
SOURCE_INVENTORY = "R827-determinantal-source-inventory.json"
AUDIT = "R827-original-place-and-unit-source-audit.json.gz"
C_SOURCE = "R827-original-two-chart-C-reduction.json.gz"
OPERATORS = "R827-complete-short-operator-identities-and-sigma-transport.json.gz"
INFINITY = "R827-sigma-infinity-order-0004-certificate.json.gz"
B_EXPANSION = "R827-canonical-B-original-V5-expansion.json.gz"
BASE_KEYS = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
STRATEGY = {
    "source_column_order": "derivative_order=0..4, original_normal_basis_column=0..271",
    "projection_family": "V(a)=(I,aI,a^2 I,a^3 I,a^4 I)^transpose",
    "ordered_integer_parameters": list(PARAMETERS),
    "determinant_nodes": "all consecutive integers 0 through the proven degree bound",
    "degree_formula": "sum(projected original homogeneous column weights)-398-20",
    "block_projection_degree_bounds": [1340, 3516, 3516, 3516],
    "interpolation": "exact forward differences / factorials in the original prime field",
    "node_determinants": "python-flint nmod_mat.det; singular nodes retained as zero",
    "success": "complete exact polynomial Bezout sum equals one and original sigma infinity certificate",
    "right_inverse": "sum(a_i V_i adj(G V_i)); adjugate entries are not materialized",
    "old_column_or_Hermite_arithmetic_recomputed": False,
    "projection_prefix_and_budget_excluded_from_mathematical_identity": True,
}


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
        raise SystemExit("R827 determinant arithmetic belongs to this public repository's Actions.")


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


def save(path, data):
    path = Path(path)
    raw = (json.dumps(data, sort_keys=True, separators=(",", ":"))+"\n").encode()
    temporary = path.with_name(path.name+".tmp")
    if path.suffix == ".gz":
        with temporary.open("wb") as stream:
            with gzip.GzipFile(fileobj=stream, mode="wb", mtime=0) as target:
                target.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def plain(entry):
    return {key: entry[key] for key in ("file", "bytes", "sha256")}


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def column_name(k, c):
    return "R827-tau-layer-"+str(k).zfill(3)+"-C-column-"+str(c).zfill(3)+".json.gz"


def layer_name(k):
    return "R827-target-B-tau-polynomial-index.json.gz" if k == 0 else \
        "R827-tau-layer-"+str(k).zfill(3)+"-precision-"+str(8+2*k).zfill(4)+"-index.json.gz"


def zero():
    return nmod_mat(N, N, PRIME)


def evaluate(coefficients, value):
    answer = zero()
    for matrix in reversed(coefficients):
        answer = answer*value+matrix
    return answer


class BudgetStop(RuntimeError):
    pass


class Source:
    def __init__(self, item, directory):
        self.item, self.root = item, Path(directory)
        inventory = read(self.root/SOURCE_INVENTORY)
        assert inventory["result"] == RESULT
        assert inventory["source"] == item["source"]
        assert sha(self.root/SOURCE_INVENTORY) == item["source_inventory_sha256"]
        self.files = {entry["file"]: plain(entry) for entry in inventory["selected_files"]}
        assert len(self.files) == len(inventory["selected_files"])
        assert inventory["source_configuration_sha256"] == item["source_configuration_sha256"]
        self.old_tag = self.load_raw(INFINITY)["configuration"]
        assert fingerprint(self.old_tag) == item["source_configuration_sha256"]
        assert self.old_tag["source_sha256"] == SOURCE_CORE
        assert self.old_tag["R827_proof_sha256"] == ORIGINAL_PROOF
        assert self.old_tag["python_flint"] == "0.9.0"
        assert self.old_tag["auxiliary_prime"] == PRIME and self.old_tag["original_branch"] == 0
        assert self.old_tag["canonical_free_column"] == 1186
        assert self.old_tag["normal_basis_rank"] == N and self.old_tag["normal_basis_degrees"] == EPS
        assert self.old_tag["certification_mode"] == "tau_polynomial_Hermite_and_sigma_infinity_rank"
        assert self.old_tag["original_field_coordinates"] == "B=lambda*b, s=1+2*zeta; exact original branch"
        self.inventory = inventory

    def load_raw(self, name):
        entry = self.files[name]
        assert Path(name).name == name and spec(self.root/name) == entry
        return read(self.root/name)

    def stage(self, name):
        data = self.load_raw(name)
        assert data["complete"] is True
        assert data["configuration"] == self.old_tag
        assert data["configuration"]["result"] == RESULT
        return data

    def entry(self, name):
        return dict(self.files[name])


class Job:
    def __init__(self, args):
        self.started = time.monotonic()
        self.item = read(args.config)
        assert self.item["core_sha256"] == sha(__file__)
        assert self.item["determinantal_proof_sha256"] == sha(args.proof)
        assert self.item["R827_proof_sha256"] == sha(args.original_proof) == ORIGINAL_PROOF
        assert flint.__version__ == "0.9.0"
        assert self.item["result"] == RESULT and self.item["certification_mode"] == MODE
        assert self.item["p"] == 41 and self.item["derivative_order"] == Q
        assert self.item["auxiliary_prime"] == PRIME
        assert self.item["producer_inputs_pending"] is False
        self.out = Path(args.output); self.out.mkdir(parents=True, exist_ok=True)
        self.limit = float(args.budget_minutes)*60
        self.requested = int(self.item["controls"]["maximum_projections"])
        assert 1 <= self.requested <= len(PARAMETERS)
        self.S = Source(self.item, args.retained)
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "p": 41, "auxiliary_prime": PRIME, "derivative_order": Q,
            "certification_mode": MODE, "normal_basis_rank": N, "normal_basis_degrees": EPS,
            "source_column_count": N*(Q+1),
            "determinantal_proof_sha256": sha(args.proof), "R827_proof_sha256": ORIGINAL_PROOF,
            "source_identity": {key: self.item["source"][key] for key in BASE_KEYS},
            "source_configuration_sha256": self.item["source_configuration_sha256"],
            "source_inventory_sha256": self.item["source_inventory_sha256"],
            "source_sigma_infinity_certificate": self.S.entry(INFINITY),
            "strategy": STRATEGY,
        }
        self.blocks = None
        self.completed_projections = 0
        self.source_check()

    def budget(self):
        if time.monotonic()-self.started >= self.limit:
            raise BudgetStop("Only completed source-bound projection blocks, determinant nodes and polynomial certificates retained.")

    def path(self, name):
        name = name if name.endswith(".json.gz") else name+".json.gz"
        assert Path(name).name == name and name.startswith(PREFIX)
        return self.out/name

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        data = read(path)
        assert data["result"] == RESULT and data["configuration"] == self.tag
        assert data["complete"] is True
        return data

    def put(self, name, data):
        assert self.cached(name) is None
        payload = dict(data, result=RESULT, configuration=self.tag, complete=True)
        save(self.path(name), payload)
        return spec(self.path(name))

    def source_check(self):
        name = PREFIX+"completed-source-interface"
        old = self.cached(name)
        audit = self.S.stage(AUDIT)
        C = self.S.stage(C_SOURCE)
        operators = self.S.stage(OPERATORS)
        infinity = self.S.stage(INFINITY)
        B = self.S.stage(B_EXPANSION)
        assert audit["prime"] == PRIME and audit["original_branch"] == 0 and audit["canonical_free_column"] == 1186
        for key in ("original_lambda_is_a_unit", "original_minimal_polynomials_and_simple_residue_roots_verified", "genuine_DVR_lift_source_not_an_arbitrary_modular_kernel_candidate"):
            assert audit[key] is True
        assert plain(audit["canonical_B_expansion"]) == self.S.entry(B_EXPANSION)
        assert B["abstract_original_p_integral_lift_certified_by_unit_minor_and_rank_bound"] is True
        assert B["same_original_reserved_normalization_verified"] is True
        for key in ("all_original_rational_coefficients_p_integral", "both_P_constant_terms_units", "actual_degree_twenty_monic_polynomials_preserved", "original_reciprocal_relation_verified_mod_prime", "original_exact_two_chart_transition_certificate_preserved", "complete_flat_target_not_squarefree_replacement"):
            assert C[key] is True
        for chart in ("tau", "sigma"):
            P = C["charts"][chart]["P_polynomial"]
            assert len(P) == 21 and P[-1] == 1 and P[0] != 0
            assert all(type(x) is int and 0 <= x < PRIME for x in P)
        for key in ("B_first_column_is_original_vB", "g_first_column_is_original_vg", "Gamma_first_column_zero_and_second_column_original_vh", "B_commutator_full_polynomial_identity_certified_by_nine_points", "g_commutator_full_polynomial_identity_certified_by_seven_points", "Gamma_nested_full_polynomial_identity_certified_by_seven_points", "all_sigma_negative_powers_and_original_minus_sign_verified", "all_operators_are_true_original_p_integral_reductions"):
            assert operators[key] is True
        assert infinity["prime"] == PRIME and infinity["derivative_order"] == Q
        assert infinity["chart"] == "sigma" and infinity["base_point"] == 0
        assert infinity["actual_rank_mod_prime"] == N and infinity["whole_infinity_fiber_surjective"] is True
        assert infinity["actual_full_minor_determinant_mod_prime"] == 695832206
        assert infinity["source_C_reduction"] == self.S.entry(C_SOURCE)
        assert infinity["actual_C_sigma_determinant_at_zero"] == C["charts"]["sigma"]["P_polynomial"][0]
        layers = []
        for k in range(Q+1):
            layer = self.S.stage(layer_name(k))
            assert layer["prime"] == PRIME and layer["normal_basis_rank"] == N
            assert layer["normal_basis_degrees"] == EPS
            if k == 0:
                assert layer["target"] == "B" and layer["chart"] == "tau"
                assert layer["regular_degree_bound"] == 5
            else:
                assert layer["chart"] == "tau" and layer["derivative_order"] == k
                assert layer["precision_stop"] == 8+2*k
                assert layer["full_polynomial_coefficients_computed"] is True
                assert layer["all_required_coefficient_blocks_complete"] is True
                assert layer["original_generator_weights"] == [5+e for e in EPS]
            layers.append(self.S.entry(layer_name(k)))
        columns = [self.S.entry(column_name(k,c)) for k in range(Q+1) for c in range(N)]
        if old is None:
            self.source_spec = self.put(name, {
                "prime": PRIME, "derivative_order": Q, "original_column_count": len(columns),
                "source_original_place_unit_audit": self.S.entry(AUDIT),
                "source_original_complete_C": self.S.entry(C_SOURCE),
                "source_original_operator_certificate": self.S.entry(OPERATORS),
                "source_original_canonical_B_expansion": self.S.entry(B_EXPANSION),
                "source_original_sigma_infinity_certificate": self.S.entry(INFINITY),
                "source_original_tau_layer_indexes": layers,
                "source_column_inventory_sha256": fingerprint(columns),
                "same_original_field_branch_free_column_and_C_preserved": True,
                "source_incomplete_Hermite_not_claimed_as_complete": True,
                "old_columns_divisions_operators_Hermite_or_infinity_arithmetic_recomputed": False,
            })
        else:
            assert old["source_column_inventory_sha256"] == fingerprint(columns)
            self.source_spec = spec(self.path(name))
        self.columns = columns
        self.layer_specs = layers

    def original_blocks(self):
        if self.blocks is not None:
            return self.blocks
        self.budget()
        blocks = [[zero() for _ in range(8+2*k)] for k in range(Q+1)]
        for k in range(Q+1):
            for c in range(N):
                data = self.S.stage(column_name(k,c))
                assert data["prime"] == PRIME and data["chart"] == "tau"
                assert data["derivative_order"] == k and data["original_B_times_normal_basis_index"] == c
                weight = 5+EPS[c]+2*k
                assert data["original_generator_weight"] == 5+EPS[c]
                assert data["source_original_layer"] == self.layer_specs[k]
                assert data["source_complete_C"] == self.S.entry(C_SOURCE)
                assert data["exact_monic_degree20_division_and_original_column_multiplyback_verified"] is True
                assert data["complete_C_basis_change_not_an_ideal_quotient"] is True
                rows = data["column_coefficients_in_original_C_basis"]
                assert len(rows) == N
                for r, values in enumerate(rows):
                    bound = weight-(EPS[r] if r < N-1 else 1)
                    assert len(values) <= bound+1
                    if values:
                        assert values[-1] != 0
                    for degree, value in enumerate(values):
                        assert type(value) is int and 0 <= value < PRIME
                        blocks[k][degree][r,c] = value
        self.blocks = blocks
        return blocks

    def projection(self, number):
        a = PARAMETERS[number]
        stem = PREFIX+"projection-"+str(number).zfill(3)
        maximum_layer = 0 if a == 0 else Q
        bound = N*(5+2*maximum_layer)-20
        assert bound == STRATEGY["block_projection_degree_bounds"][number] and bound < PRIME
        expected_count = 8+2*maximum_layer
        index_name = stem+"-polynomial-matrix-index"
        index = self.cached(index_name)
        if index is None:
            entries = []
            for power in range(expected_count):
                name = stem+"-coefficient-"+str(power).zfill(2)
                data = self.cached(name)
                if data is None:
                    self.budget()
                    originals = self.original_blocks()
                    matrix = zero()
                    for k in range(maximum_layer+1):
                        if power < len(originals[k]):
                            matrix += originals[k][power]*pow(a, k, PRIME)
                    self.put(name, {
                        "prime": PRIME, "projection_number": number, "integer_parameter": a,
                        "coefficient_exponent": power, "matrix_rows": N, "matrix_columns": N,
                        "coefficient_matrix_mod_prime": [[int(matrix[r,c]) for c in range(N)] for r in range(N)],
                        "source_completed_columns": self.source_spec,
                        "source_original_column_inventory_sha256": fingerprint(self.columns),
                        "only_new_constant_projection_linear_combination_performed": True,
                        "old_source_columns_recomputed": False,
                    })
                entries.append(spec(self.path(name)))
            self.put(index_name, {
                "prime": PRIME, "projection_number": number, "integer_parameter": a,
                "projection_kind": "scalar_blocks_identity", "source_layer_scalar_coefficients": [pow(a,k,PRIME) for k in range(Q+1)],
                "coefficient_blocks": entries, "polynomial_coefficient_count": expected_count,
                "source_homogeneous_column_weights": [5+EPS[c]+2*maximum_layer for c in range(N)],
                "original_normal_weight_sum": 398, "source_C_determinant_degree": 20,
                "proven_determinant_degree_bound": bound,
                "degree_bound_uses_original_complete_C_not_squarefree_replacement": True,
                "source_completed_columns": self.source_spec,
            })
            index = self.cached(index_name)
        assert index["projection_number"] == number and index["integer_parameter"] == a
        assert index["proven_determinant_degree_bound"] == bound
        assert len(index["coefficient_blocks"]) == expected_count
        coefficients = []
        for power, entry in enumerate(index["coefficient_blocks"]):
            assert spec(self.path(entry["file"])) == plain(entry)
            data = self.cached(entry["file"])
            assert data["coefficient_exponent"] == power and data["integer_parameter"] == a
            values = data["coefficient_matrix_mod_prime"]
            assert len(values) == N and all(len(row)==N for row in values)
            assert all(type(x) is int and 0 <= x < PRIME for row in values for x in row)
            coefficients.append(nmod_mat(values, PRIME))
        return coefficients, spec(self.path(index_name)), bound

    def determinant(self, number):
        stem = PREFIX+"projection-"+str(number).zfill(3)
        name = stem+"-exact-determinant-polynomial"
        old = self.cached(name)
        if old is not None:
            assert old["projection_number"] == number and old["integer_parameter"] == PARAMETERS[number]
            return nmod_poly(old["determinant_coefficients_mod_prime"], PRIME), spec(self.path(name))
        matrices, matrix_spec, bound = self.projection(number)
        nodes, values = [], []
        for point in range(bound+1):
            node_name = stem+"-node-"+str(point).zfill(8)
            node = self.cached(node_name)
            if node is None:
                self.budget()
                value = int(evaluate(matrices, point).det())
                self.put(node_name, {
                    "prime": PRIME, "projection_number": number, "integer_parameter": PARAMETERS[number],
                    "point": point, "matrix_rows": N, "matrix_columns": N,
                    "determinant_mod_prime": value, "source_projection_matrix": matrix_spec,
                    "proven_determinant_degree_bound": bound,
                    "singular_node_is_valid_zero_not_discarded": True,
                    "actual_exact_finite_field_determinant_computed": True,
                })
                node = self.cached(node_name)
            assert node["point"] == point and node["source_projection_matrix"] == matrix_spec
            value = node["determinant_mod_prime"]
            assert type(value) is int and 0 <= value < PRIME
            values.append(value); nodes.append(spec(self.path(node_name)))
            if (point+1) % 128 == 0:
                print(json.dumps({"stage":"determinant_nodes","projection":number,"completed_nodes":point+1,"required_nodes":bound+1}), flush=True)
        index_name = stem+"-complete-node-index"
        index = self.cached(index_name)
        if index is None:
            self.put(index_name, {
                "prime": PRIME, "projection_number": number, "integer_parameter": PARAMETERS[number],
                "source_projection_matrix": matrix_spec, "proven_determinant_degree_bound": bound,
                "node_count": bound+1, "points_are_exactly_consecutive_zero_through_bound": True,
                "node_records": nodes, "all_required_node_determinants_complete": True,
            })
        else:
            assert index["node_records"] == nodes
        self.budget()
        # A complete deterministic interpolation uses every bound+1 node.  No matrix
        # rank heuristic or shortened interpolation length is used.
        differences = list(values)
        product = nmod_poly([1], PRIME)
        polynomial = nmod_poly([], PRIME)
        inverse_factorial = 1
        for r in range(bound+1):
            polynomial += product*((differences[0]*inverse_factorial) % PRIME)
            if r < bound:
                differences = [(differences[j+1]-differences[j]) % PRIME for j in range(len(differences)-1)]
                product *= nmod_poly([-r, 1], PRIME)
                inverse_factorial = inverse_factorial*pow(r+1, -1, PRIME) % PRIME
        assert polynomial.degree() <= bound
        for point, value in enumerate(values):
            assert int(polynomial(point)) == value
        self.put(name, {
            "prime": PRIME, "projection_number": number, "integer_parameter": PARAMETERS[number],
            "source_projection_matrix": matrix_spec, "source_complete_nodes": spec(self.path(index_name)),
            "proven_determinant_degree_bound": bound, "actual_determinant_degree": polynomial.degree(),
            "determinant_coefficients_mod_prime": [int(x) for x in polynomial.coeffs()],
            "all_degree_bound_plus_one_nodes_exactly_verified": True,
            "exact_interpolant_is_the_entire_determinant_by_proven_degree_bound": True,
            "zero_polynomial_retained_as_valid_determinant": not bool(polynomial),
            "no_adjugate_coefficients_computed": True,
        })
        return polynomial, spec(self.path(name))

    def bezout(self, number, determinants, sources):
        name = PREFIX+"prefix-"+str(number+1).zfill(3)+"-exact-Bezout"
        old = self.cached(name)
        if old is not None:
            assert old["source_determinant_polynomials"] == sources
            h = nmod_poly(old["monic_gcd_coefficients_mod_prime"], PRIME)
            coefficients = [nmod_poly(row, PRIME) for row in old["Bezout_coefficients_mod_prime"]]
            assert len(coefficients) == len(determinants)
            # Cached complete certificate's own source-bound full identity was already
            # computed; no old Euclidean reduction is repeated.
            return h, coefficients, spec(self.path(name))
        self.budget()
        if number == 0:
            h = nmod_poly([], PRIME); previous_coefficients = []
        else:
            prior = self.cached(PREFIX+"prefix-"+str(number).zfill(3)+"-exact-Bezout")
            assert prior["source_determinant_polynomials"] == sources[:-1]
            h = nmod_poly(prior["monic_gcd_coefficients_mod_prime"], PRIME)
            previous_coefficients = [nmod_poly(row, PRIME) for row in prior["Bezout_coefficients_mod_prime"]]
        current = determinants[-1]
        if not h and not current:
            new_gcd = nmod_poly([], PRIME)
            coefficients = previous_coefficients+[nmod_poly([], PRIME)]
        else:
            new_gcd, left, right = h.xgcd(current)
            assert left*h+right*current == new_gcd
            inverse = pow(int(new_gcd.leading_coefficient()), -1, PRIME)
            new_gcd *= inverse; left *= inverse; right *= inverse
            coefficients = [left*x for x in previous_coefficients]+[right]
        total = nmod_poly([], PRIME)
        for coefficient, polynomial in zip(coefficients, determinants):
            total += coefficient*polynomial
        assert total == new_gcd
        if new_gcd:
            assert int(new_gcd.leading_coefficient()) == 1
        success = new_gcd == nmod_poly([1], PRIME)
        self.put(name, {
            "prime": PRIME, "completed_projection_count": number+1,
            "source_determinant_polynomials": sources,
            "monic_gcd_coefficients_mod_prime": [int(x) for x in new_gcd.coeffs()],
            "actual_monic_gcd_degree": new_gcd.degree(),
            "Bezout_coefficients_mod_prime": [[int(x) for x in value.coeffs()] for value in coefficients],
            "complete_polynomial_Bezout_multiplyback_verified": True,
            "sum_ai_actual_determinants_equals_one": success,
            "factored_right_inverse_formula": "sum_i a_i(z) V_i adj(G(z)V_i)",
            "adjugate_coefficients_materialized": False,
            "expanded_right_inverse_coefficients_materialized": False,
            "unit_gcd_failure_is_not_nonsurjectivity_certificate": not success,
        })
        return new_gcd, coefficients, spec(self.path(name))

    def inventory(self):
        entries = []
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name.startswith(PREFIX+"stage-manifest-") or path.name.endswith("-current.json.gz"):
                continue
            data = read(path)
            assert data["result"] == RESULT and data["configuration"] == self.tag and data["complete"] is True
            entries.append(spec(path))
        name = PREFIX+"stage-manifest-"+fingerprint(entries)[:24]
        old = self.cached(name)
        if old is None:
            self.put(name, {"files": entries, "all_listed_stages_complete": True,
                            "all_raw_outputs_remain_only_in_active_one_day_artifact": True})
        else:
            assert old["files"] == entries
        return spec(self.path(name))

    def finish(self, sources, bezout_spec, success):
        certificate = {
            "result": RESULT, "complete": True, "configuration": self.tag,
            "p": 41, "certification_mode": MODE, "completed_scope": "determinantal_sufficient_original_order4_termination_test",
            "requested_projection_prefix_length": self.requested,
            "actual_completed_projection_count": len(sources),
            "requested_derivative_order": Q, "actual_derivative_order": Q,
            "source_completed_column_interface": self.source_spec,
            "source_determinant_polynomials": sources, "tau_determinantal_Bezout_certificate": bezout_spec,
            "sigma_infinity_certificate": self.S.entry(INFINITY),
            "sigma_infinity_source_group": "original_R827",
            "whole_sigma_infinity_fiber_surjective": True,
            "whole_tau_affine_polynomial_module_surjective": success,
            "original_characteristic_zero_Iq_equals_C": success,
            "safe_D_multiplicity_bound": Q//3 if success else None,
            "factored_adjugate_right_inverse_certified": success,
            "adjugate_coefficients_materialized": False,
            "expanded_right_inverse_coefficients_materialized": False,
            "no_probability_or_finite_point_rank_used_as_global_certificate": True,
            "old_columns_derivatives_C_divisions_Hermite_or_infinity_arithmetic_recomputed": False,
            "actual_D_eta_or_height_computed": False,
            "failed_projection_prefix_does_not_disprove_original_termination": not success,
            "stage_manifest": self.inventory(), "seconds": time.monotonic()-self.started,
        }
        save(self.out/FINAL, certificate)
        save(self.out/"core-receipt.json", {
            "result": RESULT, "complete": True, "source_sha256": sha(__file__),
            "certificate_sha256": sha(self.out/FINAL), "certification_mode": MODE,
            "actual_derivative_order": Q, "actual_completed_projection_count": len(sources),
            "original_characteristic_zero_Iq_equals_C": success,
            "safe_D_multiplicity_bound": Q//3 if success else None,
            "actual_D_eta_or_height_computed": False,
        })
        print(json.dumps({"stage":"determinantal_test_complete","projections":len(sources),"original_I4_equals_C":success,"seconds":time.monotonic()-self.started}), flush=True)
        return 0

    def run(self):
        prior = self.out/FINAL
        if prior.exists():
            data = read(prior)
            assert data["result"] == RESULT and data["configuration"] == self.tag
            if data["complete"] and (data["original_characteristic_zero_Iq_equals_C"] or
                                     data["actual_completed_projection_count"] >= self.requested):
                return self.finish(data["source_determinant_polynomials"],
                                   data["tau_determinantal_Bezout_certificate"],
                                   data["original_characteristic_zero_Iq_equals_C"])
        determinants, sources = [], []
        for number in range(self.requested):
            determinant, entry = self.determinant(number)
            determinants.append(determinant); sources.append(entry)
            gcd, _, certificate = self.bezout(number, determinants, sources)
            self.completed_projections = number+1
            if gcd == nmod_poly([1], PRIME):
                return self.finish(sources, certificate, True)
        return self.finish(sources, certificate, False)


def main():
    guard()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--proof", type=Path, required=True)
    parser.add_argument("--original-proof", type=Path, required=True)
    parser.add_argument("--retained", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    job = None
    try:
        job = Job(args)
        return job.run()
    except BudgetStop as error:
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "certification_mode": MODE, "budget_stop": str(error),
            "actual_completed_projection_count": None if job is None else job.completed_projections,
            "all_completed_source_bound_nodes_and_projection_blocks_preserved": True,
            "actual_D_eta_or_height_computed": False,
        })
        print(json.dumps({"budget_stop":str(error)}), flush=True)
        return 124


if __name__ == "__main__":
    raise SystemExit(main())
