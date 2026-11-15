#!/usr/bin/env python3
"""R815: Q-valued original Wronskian multipliers and the normal derivation connection.

The frozen R811 framework supplies the shared original M_w point/Krylov/CRT
machinery.  R813 is a real distinct producer, and Gamma has a separate
nonhomogeneous identity; it is not a regular multiplication operator.
"""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpq, fmpz, fmpz_mat, nmod_mat
import R811_original_regular_multipliers as framework
from R811_original_regular_multipliers import (
    Retained, BudgetStop, sha, read, save, spec, plain, fingerprint,
    producer_identity, same_producer, rows, matrix_block, integer_evaluate,
    S3_position,
)

RESULT = "R815-original-normal-derivation-operators"
FINAL = "p41-original-normal-derivation-operator-certificate.json"
SCOPE = "original_normal_derivation_operators"
FREE, S3 = 272, 690
EPS = [0]+[1]*144+[2]*127
TARGETS = ("g", "Gamma")
INPUT_LABELS = ("g", "h", "Gamma")
FIELD = "Q in the unchanged original K-normal basis"
R806_CORE_SHA = "b014f9b3cb4923421e6a879eddb4da58dd0baefb28d61a2191f6b0a33e51810d"
R813_CORE_SHA = "830ae652ebb08a035c6636c7738ab4823322111944932ffc77b1136caf7a07bc"
FRAMEWORK_SHA = "849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3"


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("All new exact arithmetic belongs to public repository Actions.")


def evaluate_mod(coefficients, denominator, point, prime):
    assert denominator % prime
    inverse = pow(denominator, -1, prime)
    answer = []
    for i in range(FREE):
        row = []
        for j in range(FREE):
            value = 0
            for coefficient in reversed(coefficients):
                value = (value*point+int(coefficient[i, j])) % prime
            row.append(value*inverse % prime)
        answer.append(row)
    return nmod_mat(answer, prime)


class Job(framework.Job):
    def __init__(self, args):
        self.args, self.out, self.started = args, args.output, time.monotonic()
        self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        assert self.item["producer_inputs_pending"] is False
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert self.item["core_sha256"] == sha(__file__)
        assert sha(args.proof) == self.item["R813_proof_sha256"]
        assert sha(args.nested_proof) == self.item["R817_proof_sha256"]
        assert sha(args.method) == self.item["R815_method_sha256"]
        assert sha(framework.__file__) == self.item["framework_sha256"] == FRAMEWORK_SHA
        assert flint.__version__ == "0.9.0"
        assert self.item["requested_stage"] == SCOPE
        assert self.item["requested_targets"] == list(TARGETS)
        assert self.item["auxiliary_prime_start"] == 1000000007
        assert self.item["matrix_row_block_size"] == 16
        assert self.item["reconstruct_every_primes"] >= 1
        assert self.item["exact_identity_mode"] == "deterministic_integer_points_with_weighted_degree_bound"
        assert set(self.item["retained_artifacts"]) == {"R806", "R813"}
        self.r806 = Retained(args.retained, "R806", self.item["retained_artifacts"]["R806"])
        self.r813 = Retained(args.retained, "R813", self.item["retained_artifacts"]["R813"])
        assert self.r806.identity["result"] == "R806-original-primitive-multiplication"
        assert self.r813.identity["result"] == "R813-original-Wronskian-derivation-inputs"
        assert self.r806.identity["core_sha256"] == R806_CORE_SHA
        assert self.r813.identity["core_sha256"] == R813_CORE_SHA
        c806, c813 = self.r806.certificate, self.r813.certificate
        assert c806["completed_scope"] == "primitive_multiplication_and_cyclic_certificate"
        assert c806["normal_affine_basis_rank"] == FREE
        for key in ("exact_polynomial_multiplication_computed",
                    "all272_columns_verified_in_all820_original_rows",
                    "actual_cyclic_minor_certified",
                    "original_function_field_primitive_generator_certified",
                    "normal_integral_basis_preserved"):
            assert c806[key] is True
        assert c813["completed_scope"] == "two_original_S3_Wronskian_inputs"
        assert c813["target_names"] == ["g", "h"] and c813["actual_rational_RHS_columns"] == 2
        assert c813["S3_basis_dimension"] == S3
        assert c813["qY_count"] == 41 and c813["full_coordinate_rows"] == 820
        assert c813["normal_basis_rank"] == FREE and c813["normal_basis_degrees"] == EPS
        assert c813["regular_degree_bound"] == 3
        assert c813["original_D0_qY_multiplier"] == ["1", "82"]
        for key in ("all820_original_coordinates_verified_for_both_targets",
                    "both_original_normal_vectors_actually_nonzero",
                    "original_1_over82_and_all_integer_scales_preserved"):
            assert c813[key] is True
        assert c813["actual_Mg_Mh_or_Gamma_computed"] is False
        same_producer(self.r813.tag["producer_identities"]["R806"], self.r806.identity)
        same_producer(self.r813.tag["producer_identities"]["R805"],
                      self.r806.tag["retained_artifacts"]["R805"])
        assert c813["actual_sigma_integer_n"] == self.r806.tag["actual_sigma_integer_n"]
        self.w_spec = c806["polynomial_multiplier"]
        self.w_interface = self.r806.indexed(self.w_spec)
        interface = self.w_interface
        assert interface["normal_affine_basis_rank"] == FREE
        assert interface["normal_affine_basis_degrees"] == EPS
        assert interface["coefficient_field"] == "Q, certified by exact original rational coordinate equations"
        assert interface["matrix_convention"] == "M_ba(z) is output row b, input column a"
        assert interface["coordinate_groups"] == c806["exact_coordinate_groups"]
        assert interface["original_R805_free_basis"] == self.r813.tag["original_graded_free_basis"]
        assert interface["original_R805_S_basis_index"] == self.r813.tag["original_S3_basis_index"]
        for key in ("all272_columns_verified_in_all820_original_rows",
                    "all_weighted_support_zeros_verified",
                    "reduction_equals_successful_modular_multiplier",
                    "original_function_field_primitive_generator_certified",
                    "normal_integral_basis_preserved"):
            assert interface[key] is True
        self.witness_spec = interface["actual_cyclic_witness"]
        self.witness = self.r806.indexed(self.witness_spec)
        assert self.witness["candidate_index"] == interface["candidate_index"]
        assert self.witness["actual_cyclic_rank"] == FREE
        assert self.witness["actual_determinant_mod_prime"] % self.witness["prime"]
        assert self.witness["primitive_generator_certified_by_actual_minor"] is True
        self.search_degree = FREE*(FREE-1)//2-sum(EPS)
        assert self.search_degree == self.r806.tag["cyclic_determinant_degree_bound"]
        self.source_coordinate_spec = c813["exact_coordinate_stage"]
        self.source_coordinates = self.r813.indexed(self.source_coordinate_spec)
        coordinates = self.source_coordinates
        assert coordinates["target_names"] == ["g", "h"] and coordinates["column_indices"] == [0, 1]
        assert coordinates["S3_basis_dimension"] == S3 and coordinates["normal_basis_rank"] == FREE
        assert coordinates["full_coordinate_rows"] == 820
        assert coordinates["all820_original_coordinates_verified"] is True
        assert coordinates["both_original_Wronskians_actually_nonzero"] is True
        assert coordinates["original_1_over82_and_all_integer_scales_preserved"] is True
        assert coordinates["original_D0_qY_multiplier"] == ["1", "82"]
        assert coordinates["original_S3_integer_scale"] == str(82**6)
        assert len(coordinates["coordinate_numerators"]) == S3
        assert all(len(row) == 2 for row in coordinates["coordinate_numerators"])
        assert len(coordinates["column_denominators"]) == 2
        assert len(coordinates["original_target_rational_scales"]) == 2
        self.normal_interface_spec = c813["normal_vector_interface"]
        self.normal_interface = self.r813.indexed(self.normal_interface_spec)
        normal = self.normal_interface
        assert normal["target_column_indices"] == {"g": 0, "h": 1}
        assert normal["source_exact_S3_coordinates"] == self.source_coordinate_spec
        assert normal["normal_basis_rank"] == FREE and normal["normal_basis_degrees"] == EPS
        assert normal["regular_degree_bound"] == 3
        assert normal["coefficient_field"] == FIELD
        assert normal["actual_R806_polynomial_multiplier_index"] == self.w_spec
        assert normal["actual_R806_primitive_candidate"] == c806["accepted_candidate"]
        assert normal["original_R805_graded_free_basis"] == interface["original_R805_free_basis"]
        assert normal["all820_original_coordinates_verified"] is True
        assert normal["original_1_over82_and_all_integer_scales_preserved"] is True
        assert normal["actual_Mg_Mh_or_Gamma_computed"] is False
        mapping = normal["S3_row_to_polynomial_coefficient"]
        assert len(mapping) == S3
        for index, entry in enumerate(mapping):
            assert entry == {"S_row": index, "normal_basis_row": S3_position(index)[0],
                             "power_of_z": S3_position(index)[1]}
        self.s3_mapping = [S3_position(i) for i in range(S3)]
        self.cache_identity = {
            "R806_producer": producer_identity(self.r806.identity),
            "R806_polynomial_multiplier": self.w_spec,
            "R806_cyclic_witness": self.witness_spec,
            "original_R805_free_basis": interface["original_R805_free_basis"],
            "original_R805_S_basis_index": interface["original_R805_S_basis_index"],
            "normal_affine_basis_rank": FREE, "normal_basis_degrees": EPS,
            "coordinate_convention": "column input, row output; e0 is original unit",
            "coefficient_field": "Q",
        }
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "R813_proof_sha256": sha(args.proof), "R817_proof_sha256": sha(args.nested_proof),
            "R815_method_sha256": sha(args.method),
            "framework_sha256": sha(framework.__file__), "p": 41,
            "normal_affine_basis_rank": FREE, "normal_basis_degrees": EPS,
            "coefficient_field_basis": FIELD,
            "R806_producer": producer_identity(self.r806.identity),
            "R806_polynomial_multiplier": self.w_spec, "R806_cyclic_witness": self.witness_spec,
            "original_R805_free_basis": interface["original_R805_free_basis"],
            "actual_sigma_integer_n": self.r806.tag["actual_sigma_integer_n"],
            "shared_point_mathematical_identity": self.cache_identity,
            "matrix_convention": "output row b, input column a",
            "auxiliary_prime_start": self.item["auxiliary_prime_start"],
            "matrix_row_block_size": self.item["matrix_row_block_size"],
            "reconstruct_every_primes": self.item["reconstruct_every_primes"],
            "point_search": "original successful z0 first; then distinct nonnegative residues",
            "exact_identity_mode": self.item["exact_identity_mode"],
            "no_characteristic_zero_Krylov_matrix_or_inverse": True,
            "R813_targets_budget_and_transport_artifacts_excluded_from_shared_basis_identity": True,
        }
        common_target = {
            "basis_configuration_sha256": fingerprint(self.tag),
            "R813_producer": producer_identity(self.r813.identity),
            "source_R813_exact_coordinates": self.source_coordinate_spec,
            "source_R813_normal_interface": self.normal_interface_spec,
            "coefficient_field_basis": FIELD,
            "original_D0_qY_multiplier": ["1", "82"],
        }
        self.target_tags = {}
        for column, target in enumerate(("g", "h")):
            self.target_tags[target] = dict(common_target, target=target,
                source_R813_column=column,
                operator_kind="multiplication" if target == "g" else "original_vector_only",
                regular_degree_bound=3, polynomial_maximum_degree=5,
                original_rational_scale=self.source_coordinates["original_target_rational_scales"][column])
        self.target_tags["Gamma"] = dict(common_target, target="Gamma",
            operator_kind="normal_derivation_connection", weighted_degree_shift=2,
            polynomial_maximum_degree=4, first_column_constraint="Gamma*e0=0",
            defining_identity="[Gamma*Mw-Mw*Gamma+Mg*dMw/dz,Mw]=0; H*e0=v_h",
            independent_Mh_reconstruction=False,
            right_hand_side_multiplication_order="Mg on the left of dMw/dz")
        self.w_coefficients = None
        self.w_denominator = None
        self.prime_values, self.target_vectors = [], {}
        self.block_ranges = [(first, min(first+self.item["matrix_row_block_size"], FREE))
                             for first in range(0, FREE, self.item["matrix_row_block_size"])]
        self.operator_indices, self.operator_matrices = {}, {}

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes-45:
            raise BudgetStop("Complete original operator stages and latest CRT states retained.")

    def path(self, name):
        assert Path(name).name == name
        if name.startswith("R811-"):
            name = "R815-"+name[5:]
        assert name.startswith("R815-")
        return self.out/(name if name.endswith(".json.gz") else name+".json.gz")

    def store(self, name, value, target=None, current=False, replace=False):
        value = dict(value)
        if "coefficient_field_basis" in value:
            assert value["coefficient_field_basis"] in (framework.FIELD_BASIS, FIELD)
            value["coefficient_field_basis"] = FIELD
        if target is not None:
            assert target in INPUT_LABELS
            value["operator_kind"] = {"g": "multiplication", "h": "original_vector_only",
                                      "Gamma": "normal_derivation_connection"}[target]
            if "field_component" in value:
                assert value["field_component"] == 0
        if name.endswith("-Krylov-inverse") or name.endswith("-Krylov-inverse.json.gz"):
            value["shared_point_mathematical_identity"] = self.cache_identity
            value["source_bound_external_cache_consumption_allowed"] = True
            value["external_consumer_must_preserve_original_R815_stage_identity"] = True
        return super().store(name, value, target, current, replace)

    def point(self, prime, point):
        data, entry = super().point(prime, point)
        assert data["shared_point_mathematical_identity"] == self.cache_identity
        assert data["source_bound_external_cache_consumption_allowed"] is True
        return data, entry

    def component_stem(self, target, component):
        assert target in INPUT_LABELS and component == 0
        return "R815-target-"+target+"-component-00"

    def load_w(self):
        super().load_w()
        # Actual R806 output, not an inferred candidate label: w0=e2 and beta1=e2/tau.
        assert [int(x) for x in self.r806.certificate["actual_w0_original_M2_integer_coordinates"]] == \
            [int(i == 2) for i in range(146)]
        for power, matrix in enumerate(self.w_coefficients):
            for row in range(FREE):
                expected = self.w_denominator if power == 0 and row == 1 else 0
                assert int(matrix[row, 0]) == expected

    def target_component(self, target, component):
        assert target in INPUT_LABELS and component == 0
        key = target, component
        if key in self.target_vectors:
            return self.target_vectors[key]
        if target == "Gamma":
            name = "R815-target-Gamma-original-equation-input"
            data = self.cached(name, target)
            if data is None:
                g = self.target_component("g", 0)
                h = self.target_component("h", 0)
                self.store(name, {
                    "target": target, "field_component": 0,
                    "source_original_g_vector": g["source"], "source_original_h_vector": h["source"],
                    "source_R806_polynomial_multiplier": self.w_spec,
                    "normal_affine_basis_rank": FREE, "normal_basis_degrees": EPS,
                    "weighted_degree_shift": 2, "regular_degree_bound": 2,
                    "first_column_constraint": "Gamma*e0=0",
                    "first_column_is_a_constraint_not_a_zero_operator_input": True,
                    "zero_vector_shortcut_allowed": False,
                    "defining_identity": "[H,Mw]=0; H*e0=v_h; H=Gamma*Mw-Mw*Gamma+Mg*dMw/dz",
                    "independent_Mh_reconstruction": False,
                    "original_D0_scale_already_present_in_both_R813_vectors": True,
                }, target)
                data = self.cached(name, target)
            assert data["zero_vector_shortcut_allowed"] is False
            answer = {"values": [[0]*FREE for _ in range(3)], "denominator": 1,
                      "degree": 2, "zero": False, "source": spec(self.path(name)),
                      "operator_kind": "normal_derivation_connection"}
            self.target_vectors[key] = answer
            return answer
        column = 0 if target == "g" else 1
        coordinates = self.source_coordinates
        group_denominator = int(coordinates["column_denominators"][column])
        scale = coordinates["original_target_rational_scales"][column]
        scale_num, scale_den = int(scale[0]), int(scale[1])
        assert group_denominator > 0 and scale_den > 0 and scale_num
        name = self.component_stem(target, component)+"-original-vector"
        data = self.cached(name, target)
        if data is None:
            denominator = group_denominator*scale_den
            values = [[0]*FREE for _ in range(4)]
            for index, (output, power) in enumerate(self.s3_mapping):
                numerator = int(coordinates["coordinate_numerators"][index][column])*scale_num
                assert power <= 3-EPS[output]
                values[power][output] = numerator
            content = denominator
            for row in values:
                for value in row:
                    content = math.gcd(content, value)
            assert content > 0
            denominator //= content
            values = [[value//content for value in row] for row in values]
            assert any(value for row in values for value in row)
            self.store(name, {
                "target": target, "field_component": 0, "source_R813_column_index": column,
                "regular_degree_bound": 3, "normal_affine_basis_rank": FREE,
                "source_R813_normal_interface": self.normal_interface_spec,
                "source_R813_exact_coordinates": self.source_coordinate_spec,
                "original_target_rational_scale": scale,
                "original_coordinate_column_denominator": str(group_denominator),
                "common_positive_denominator": str(denominator),
                "integer_vector_coefficients_low_to_high": [[str(x) for x in row] for row in values],
                "exactly_zero_component": False,
                "original_rational_scale_applied_exactly_once": True,
                "original_D0_qY_multiplier": ["1", "82"],
                "no_extra_82_power_or_removed_content_reinserted": True,
                "weighted_support_verified": True,
                "original_full820_certificate_preserved": True,
            }, target)
            data = self.cached(name, target)
        assert data["source_R813_normal_interface"] == self.normal_interface_spec
        assert data["source_R813_exact_coordinates"] == self.source_coordinate_spec
        assert data["original_target_rational_scale"] == scale
        assert data["original_coordinate_column_denominator"] == str(group_denominator)
        assert data["source_R813_column_index"] == column
        assert data["regular_degree_bound"] == 3 and data["weighted_support_verified"] is True
        denominator = int(data["common_positive_denominator"])
        assert denominator > 0
        values = [[int(x) for x in row] for row in data["integer_vector_coefficients_low_to_high"]]
        assert len(values) == 4 and all(len(row) == FREE for row in values)
        for power, row in enumerate(values):
            for output, value in enumerate(row):
                if power > 3-EPS[output]:
                    assert value == 0
        assert any(value for row in values for value in row)
        answer = {"values": values, "denominator": denominator, "degree": 3,
                  "zero": False, "source": spec(self.path(name)),
                  "operator_kind": "multiplication" if target == "g" else "original_vector_only"}
        self.target_vectors[key] = answer
        return answer

    def load_certified_operator(self, target):
        assert target == "g"
        if target in self.operator_matrices:
            return self.operator_matrices[target]
        entry = self.operator_indices[target]
        data = self.validate_completed_component(target, 0, entry)
        assert data["operator_kind"] == "multiplication" and data["regular_degree_bound"] == 3
        denominator = 1
        for row in data["matrix_row_blocks_tau"]:
            block = self.cached(row["file"], target)
            denominator = math.lcm(denominator, int(block["common_positive_denominator"]))
        coefficients = [fmpz_mat(FREE, FREE) for _ in range(6)]
        for row, (first, stop) in zip(data["matrix_row_blocks_tau"], self.block_ranges):
            self.budget()
            assert spec(self.path(row["file"])) == row
            block = self.cached(row["file"], target)
            factor = denominator//int(block["common_positive_denominator"])
            raw, offset = block["coefficient_numerators"], 0
            for output in range(first, stop):
                for column in range(FREE):
                    bound = 3+EPS[column]-EPS[output]
                    for power in range(bound+1):
                        coefficients[power][output, column] = int(raw[offset])*factor
                        offset += 1
            assert offset == len(raw)
        self.operator_matrices[target] = (coefficients, denominator, entry)
        return self.operator_matrices[target]

    def prime_point_multiplier(self, target, component, prime, point, point_spec):
        if target != "Gamma":
            return super().prime_point_multiplier(target, component, prime, point, point_spec)
        assert component == 0
        vector_data = self.target_component(target, component)
        g_coefficients, g_denominator, g_spec = self.load_certified_operator("g")
        h = self.target_component("h", 0)
        assert g_denominator % prime and h["denominator"] % prime
        name = self.component_stem(target, component)+"-prime-"+str(prime)+"-z-"+str(point)+"-modular-connection"
        data = self.cached(name, target)
        if data is None:
            self.budget()
            assert spec(self.path(point_spec["file"])) == point_spec
            point_data = self.cached(point_spec["file"])
            assert point_data["usable"] and point_data["prime"] == prime and point_data["z0"] == point
            W = nmod_mat(point_data["W_evaluated_mod_prime"], prime)
            inverse = nmod_mat(point_data["inverse_Krylov_matrix_mod_prime"], prime)
            derivative = [self.w_coefficients[k]*k for k in range(1, len(self.w_coefficients))]
            Wprime = evaluate_mod(derivative, self.w_denominator, point, prime)
            Mg = evaluate_mod(g_coefficients, g_denominator, point, prime)
            h_inverse = pow(h["denominator"], -1, prime)
            vh = nmod_mat([[sum(h["values"][power][i]*pow(point, power, prime)
                               for power in range(4))*h_inverse % prime]
                           for i in range(FREE)], prime)
            k = nmod_mat([[int(i == 0)] for i in range(FREE)], prime)
            d = nmod_mat([[0] for _ in range(FREE)], prime)
            hpower = vh
            columns = []
            for exponent in range(FREE):
                if exponent == 0:
                    value = nmod_mat([[0] for _ in range(FREE)], prime)
                else:
                    value = nmod_mat([[int(hpower[i, 0])*exponent % prime] for i in range(FREE)], prime)-Mg*d
                columns.append([int(value[i, 0]) for i in range(FREE)])
                if exponent+1 < FREE:
                    d, k = Wprime*k+W*d, W*k
                    if exponent >= 1:
                        hpower = W*hpower
            answer = nmod_mat(columns, prime).transpose()*inverse
            assert all(int(answer[i, 0]) == 0 for i in range(FREE))
            H = answer*W-W*answer+Mg*Wprime
            assert all(H[i, 0] == vh[i, 0] for i in range(FREE))
            assert H*W == W*H
            self.store(name, {
                "target": target, "field_component": 0, "prime": prime, "z0": point,
                "source_original_vector": vector_data["source"], "source_Krylov_point": point_spec,
                "source_exact_Mg": g_spec, "source_original_h_vector": h["source"],
                "matrix_mod_prime": rows(answer),
                "matrix_convention": "Gamma*K columns=j*W^(j-1)*h-Mg*d(K_j)/dz; right multiply inverse_K",
                "full_zero_first_column_verified_mod_prime": True,
                "full_nested_commutator_verified_mod_prime": True,
                "original_h_first_column_verified_mod_prime": True,
                "defining_identity": "[H,W]=0; H*e0=v_h; H=Gamma*W-W*Gamma+Mg*Wprime",
                "independent_Mh_reconstruction": False,
                "Wprime_is_original_polynomial_derivative": True,
                "ordinary_commuting_multiplier_claimed": False,
                "exact_characteristic_zero_connection_claimed": False,
            }, target)
            data = self.cached(name, target)
        assert data["source_original_vector"] == vector_data["source"]
        assert data["source_Krylov_point"] == point_spec
        assert data["source_exact_Mg"] == g_spec
        assert data["source_original_h_vector"] == h["source"]
        assert data["prime"] == prime and data["z0"] == point
        assert data["full_zero_first_column_verified_mod_prime"] is True
        assert data["full_nested_commutator_verified_mod_prime"] is True
        assert data["original_h_first_column_verified_mod_prime"] is True
        assert data["ordinary_commuting_multiplier_claimed"] is False
        assert len(data["matrix_mod_prime"]) == FREE and all(len(row) == FREE for row in data["matrix_mod_prime"])
        return data, spec(self.path(name))

    def component(self, target, component):
        if target != "Gamma":
            assert target == "g" and component == 0
            return super().component(target, component)
        assert component == 0
        self.load_w()
        _, g_denominator, _ = self.load_certified_operator("g")
        h_vector = self.target_component("h", 0)
        vector = self.target_component(target, component)
        stem = self.component_stem(target, component)
        complete_name = stem+"-certified-connection-index"
        old = self.cached(complete_name, target)
        if old is not None:
            self.validate_completed_component(target, component, spec(self.path(complete_name)))
            assert old["source_original_vector"] == vector["source"]
            assert old["Gamma_zero_first_column_and_H_original_first_column_verified"] is True
            assert old["complete_nested_commutator_identity_verified"] is True
            current = self.cached(stem+"-CRT-current", target, current=True)
            if current is not None:
                self.CRT_history_and_cleanup(target, component, current)
                self.path(stem+"-CRT-current").unlink()
            return spec(self.path(complete_name))
        current_name = stem+"-CRT-current"
        current = self.cached(current_name, target, current=True)
        degree = vector["degree"]
        if current is None:
            values, modulus, primes, indices, next_index = [0]*self.coefficient_count(degree), 1, [], [], 0
            previous_sha, previous_receipt = None, None
        else:
            assert current["target"] == target and current["field_component"] == component
            assert current["source_original_vector"] == vector["source"]
            assert current["regular_degree_bound"] == degree
            values = [int(value) for value in current["lifted_coefficients"]]
            modulus = int(current["modulus"])
            primes, indices = current["consumed_primes"], current["consumed_prime_indices"]
            assert len(primes) == len(indices) == current["prime_count"]
            assert indices == sorted(set(indices)) and len(set(primes)) == len(primes)
            assert all(self.prime_at(i) == p for i, p in zip(indices, primes))
            assert math.prod(primes) == modulus
            assert len(values) == self.coefficient_count(degree) and all(0 <= value < modulus for value in values)
            next_index = indices[-1]+1
            previous_receipt = self.CRT_history_and_cleanup(target, component, current)
            previous_sha = sha(self.path(current_name))
        while True:
            self.budget()
            if current is not None and (len(primes) == 1 or len(primes) % self.item["reconstruct_every_primes"] == 0):
                candidate = self.reconstruct_candidate(target, component, current)
                if candidate is not None:
                    accepted, index_spec = self.verify_gamma_and_transport(target, component, current, *candidate)
                    if accepted:
                        self.path(current_name).unlink(missing_ok=True)
                        return index_spec
            prime_index, prime = next_index, self.prime_at(next_index)
            next_index += 1
            if (vector["denominator"]*g_denominator*h_vector["denominator"]) % prime == 0:
                name = stem+"-prime-"+str(prime)+"-rejected-vector-denominator"
                if self.cached(name, target) is None:
                    self.store(name, {
                        "target": target, "field_component": component, "prime": prime,
                        "source_original_vector": vector["source"],
                        "reason": "An exact original vector or certified Mg denominator is not a unit.",
                        "characteristic_zero_failure_claimed": False,
                    }, target)
                continue
            grid, grid_spec = self.grid(prime, degree)
            if not grid["usable"]:
                continue
            image, image_spec, temporary = self.modular_image(target, component, prime, grid, grid_spec)
            self.budget()
            inverse = pow(modulus % prime, -1, prime)
            assert len(image) == len(values)
            updated = [value+modulus*((image[i]-value) % prime*inverse % prime)
                       for i, value in enumerate(values)]
            new_modulus = modulus*prime
            assert all(0 <= value < new_modulus for value in updated)
            # Both congruences are checked, including every original accumulated residue.
            assert all(updated[i] % modulus == values[i] and updated[i] % prime == image[i]
                       for i in range(len(values)))
            primes, indices = primes+[prime], indices+[prime_index]
            self.store(current_name, {
                "target": target, "field_component": component, "regular_degree_bound": degree,
                "source_original_vector": vector["source"],
                "prime_count": len(primes), "consumed_primes": primes, "consumed_prime_indices": indices,
                "modulus": str(new_modulus), "lifted_coefficients": [str(value) for value in updated],
                "coefficient_count": len(updated),
                "entry_order": "output_row, input_column, power=0..r+eps_column-eps_row",
                "latest_consumed_modular_image": image_spec, "latest_modular_temporary_files": temporary,
                "previous_checkpoint_sha256": previous_sha, "previous_CRT_receipt": previous_receipt,
                "both_CRT_congruences_verified_for_every_coefficient": True,
                "only_latest_large_CRT_vector_retained": True,
                "complete_characteristic_zero_identity_claimed": False,
            }, target, current=True)
            current = self.cached(current_name, target, current=True)
            previous_receipt = self.CRT_history_and_cleanup(target, component, current)
            previous_sha = sha(self.path(current_name))
            values, modulus = updated, new_modulus
            print(json.dumps({"stage": "CRT_normal_connection", "target": target, "field_component": component,
                              "prime_count": len(primes), "prime": prime, "modulus_bits": modulus.bit_length(),
                              "coefficient_count": len(values), "seconds": time.monotonic()-self.started}), flush=True)

    def verify_gamma_and_transport(self, target, component, current, candidate, candidate_spec):
        assert target == "Gamma" and component == 0
        vector = self.target_component(target, component)
        h = self.target_component("h", 0)
        g_coefficients, g_denominator, g_spec = self.load_certified_operator("g")
        g_index = self.cached(g_spec["file"], "g")
        degree, attempt = 2, current["prime_count"]
        stem = self.component_stem(target, component)
        attempt_stem = stem+"-attempt-"+str(attempt).zfill(6)
        assert candidate["source_original_vector"] == vector["source"]
        assert candidate["source_CRT_checkpoint"] == spec(self.path(stem+"-CRT-current"))
        assert candidate["regular_degree_bound"] == degree
        assert len(candidate["matrix_row_blocks"]) == len(self.block_ranges)
        blocks, denominator = [], 1
        for entry, (first, stop) in zip(candidate["matrix_row_blocks"], self.block_ranges):
            self.budget()
            assert spec(self.path(entry["file"])) == entry
            block = self.cached(entry["file"], target)
            assert block["source_original_vector"] == vector["source"]
            assert (block["row_first"], block["row_stop"]) == (first, stop)
            d = int(block["common_positive_denominator"])
            assert d > 0 and len(block["coefficient_numerators"]) == self.coefficient_count(degree, first, stop)
            denominator = math.lcm(denominator, d)
            blocks.append(block)
        coefficients = [fmpz_mat(FREE, FREE) for _ in range(5)]
        for block, (first, stop) in zip(blocks, self.block_ranges):
            factor = denominator//int(block["common_positive_denominator"])
            raw, offset = block["coefficient_numerators"], 0
            for output in range(first, stop):
                for column in range(FREE):
                    bound = 2+EPS[column]-EPS[output]
                    for power in range(bound+1):
                        coefficients[power][output, column] = int(raw[offset])*factor
                        offset += 1
            assert offset == len(raw)
        for power, matrix in enumerate(coefficients):
            for output in range(FREE):
                for column in range(FREE):
                    if power > 2+EPS[column]-EPS[output]:
                        assert matrix[output, column] == 0
        # R806's actual w0=e2 and original free basis give W*e0=e1, Wprime*e0=0.
        # Thus H*e0=Gamma*e1, after Gamma*e0=0; both constraints are exact coefficients.
        first_name = attempt_stem+"-exact-original-column-constraints"
        first_certificate = self.cached(first_name, target)
        if first_certificate is None:
            for power, matrix in enumerate(coefficients):
                for output in range(FREE):
                    if matrix[output, 0]:
                        rejection = self.candidate_cleanup(target, component, attempt,
                            "The reconstructed connection does not yet kill the original unit.",
                            {"power": power, "output_row": output, "source_candidate": candidate_spec})
                        return False, rejection
                    expected = h["values"][power][output] if power < 4 else 0
                    if int(matrix[output, 1])*h["denominator"] != expected*denominator:
                        rejection = self.candidate_cleanup(target, component, attempt,
                            "The reconstructed connection's original w derivative is not yet the R813 h vector.",
                            {"power": power, "output_row": output, "source_candidate": candidate_spec})
                        return False, rejection
            self.store(first_name, {
                "target": target, "field_component": 0, "source_candidate": candidate_spec,
                "source_original_vector": vector["source"], "source_original_h_vector": h["source"],
                "source_original_M_w": self.w_input_spec, "source_exact_Mg": g_spec,
                "actual_w0_original_M2_is_e2": True,
                "actual_original_W_first_column_is_constant_e1": True,
                "Gamma_e0_zero_verified_coefficientwise": True,
                "Gamma_e1_equals_original_h_verified_coefficientwise": True,
                "H_e0_equals_original_h_verified_coefficientwise": True,
                "H_definition": "Gamma*W-W*Gamma+Mg*Wprime",
                "candidate_weighted_support_verified_for_every_entry": True,
                "H_weighted_degree_shift": 3,
                "nested_commutator_weighted_degree_shift": 4,
                "nested_commutator_maximum_degree": 6,
                "independent_Mh_reconstruction": False,
            }, target)
            first_certificate = self.cached(first_name, target)
        assert first_certificate["source_candidate"] == candidate_spec
        assert first_certificate["source_original_h_vector"] == h["source"]
        assert first_certificate["source_exact_Mg"] == g_spec
        assert first_certificate["Gamma_e0_zero_verified_coefficientwise"] is True
        assert first_certificate["H_e0_equals_original_h_verified_coefficientwise"] is True
        first_spec = spec(self.path(first_name))
        derivative = [self.w_coefficients[k]*k for k in range(1, len(self.w_coefficients))]
        H_denominator = math.lcm(denominator*self.w_denominator, g_denominator*self.w_denominator)
        gamma_factor = H_denominator//(denominator*self.w_denominator)
        g_factor = H_denominator//(g_denominator*self.w_denominator)
        exact_points, point_specs = list(range(7)), []
        for point in exact_points:
            self.budget()
            point_name = attempt_stem+"-exact-nested-commutator-z-"+str(point)+"-index"
            point_certificate = self.cached(point_name, target)
            if point_certificate is None:
                pending = []
                for first, stop in self.block_ranges:
                    name = attempt_stem+"-exact-nested-commutator-z-"+str(point)+"-rows-"+str(first).zfill(3)+"-"+str(stop).zfill(3)
                    old = self.cached(name, target)
                    if old is None:
                        pending.append((first, stop, name))
                    else:
                        assert old["source_candidate"] == candidate_spec and old["source_exact_Mg"] == g_spec
                        assert old["source_original_M_w"] == self.w_input_spec
                        assert old["exact_integer_point"] == point
                        assert (old["row_first"], old["row_stop"]) == (first, stop)
                        assert old["all_exact_integer_nested_commutator_entries_zero"] is True
                if pending:
                    A = integer_evaluate(coefficients, point)
                    W = integer_evaluate(self.w_coefficients, point)
                    Wprime = integer_evaluate(derivative, point)
                    Mg = integer_evaluate(g_coefficients, point)
                    H = (A*W-W*A)*gamma_factor+(Mg*Wprime)*g_factor
                    for first, stop, name in pending:
                        self.budget()
                        residual = matrix_block(H, first, stop)*W-matrix_block(W, first, stop)*H
                        failure = None
                        for local in range(stop-first):
                            for column in range(FREE):
                                if residual[local, column]:
                                    failure = {"output_row": first+local, "input_column": column,
                                               "exact_integer_residual": str(residual[local, column])}
                                    break
                            if failure is not None:
                                break
                        if failure is not None:
                            rejected = self.candidate_cleanup(target, component, attempt,
                                "The reconstructed connection has a nonzero exact nested commutator.",
                                dict(failure, exact_integer_point=point, source_candidate=candidate_spec))
                            return False, rejected
                        self.store(name, {
                            "target": target, "field_component": 0,
                            "source_candidate": candidate_spec, "source_exact_Mg": g_spec,
                            "source_original_M_w": self.w_input_spec,
                            "source_original_h_vector": h["source"],
                            "exact_integer_point": point, "row_first": first, "row_stop": stop,
                            "column_count": FREE,
                            "candidate_common_positive_denominator": str(denominator),
                            "Mg_common_positive_denominator": str(g_denominator),
                            "Mw_common_positive_denominator": str(self.w_denominator),
                            "H_common_positive_denominator": str(H_denominator),
                            "integer_H_factors": [str(gamma_factor), str(g_factor)],
                            "integer_H_construction": "factor0*(A*W-W*A)+factor1*Mg*Wprime",
                            "nested_identity": "[Gamma*W-W*Gamma+Mg*Wprime,W]=0",
                            "all_exact_integer_nested_commutator_entries_zero": True,
                            "H_is_only_evaluated_at_this_point_not_reconstructed_as_a_polynomial_table": True,
                            "no_random_or_modular_check_used_as_exact_identity": True,
                        }, target)
                    del A, W, Wprime, Mg, H
                block_specs = []
                for first, stop in self.block_ranges:
                    name = attempt_stem+"-exact-nested-commutator-z-"+str(point)+"-rows-"+str(first).zfill(3)+"-"+str(stop).zfill(3)
                    old = self.cached(name, target)
                    assert old["source_candidate"] == candidate_spec and old["source_exact_Mg"] == g_spec
                    assert old["all_exact_integer_nested_commutator_entries_zero"] is True
                    block_specs.append(spec(self.path(name)))
                self.store(point_name, {
                    "target": target, "field_component": 0,
                    "source_candidate": candidate_spec, "source_exact_Mg": g_spec,
                    "source_original_M_w": self.w_input_spec,
                    "source_original_h_vector": h["source"],
                    "exact_integer_point": point, "full_row_block_certificates": block_specs,
                    "full_matrix_shape": [FREE, FREE],
                    "all_exact_nested_commutator_entries_zero": True,
                    "Krylov_invertibility_not_required_at_exact_verification_point": True,
                }, target)
                point_certificate = self.cached(point_name, target)
            assert point_certificate["source_candidate"] == candidate_spec
            assert point_certificate["source_exact_Mg"] == g_spec
            assert point_certificate["source_original_M_w"] == self.w_input_spec
            assert point_certificate["exact_integer_point"] == point
            assert point_certificate["all_exact_nested_commutator_entries_zero"] is True
            point_specs.append(spec(self.path(point_name)))
        sigma_specs = []
        assert len(g_index["matrix_row_blocks_tau"]) == len(self.block_ranges)
        for gamma_entry, block, g_entry, (first, stop) in zip(
                candidate["matrix_row_blocks"], blocks, g_index["matrix_row_blocks_tau"], self.block_ranges):
            self.budget()
            name = stem+"-sigma-rows-"+str(first).zfill(3)+"-"+str(stop).zfill(3)
            old = self.cached(name, target)
            if old is None:
                assert spec(self.path(g_entry["file"])) == g_entry
                g_block = self.cached(g_entry["file"], "g")
                da, dg = int(block["common_positive_denominator"]), int(g_block["common_positive_denominator"])
                common = math.lcm(da, dg)
                fa, fg = common//da, common//dg
                raw_a, raw_g = block["coefficient_numerators"], g_block["coefficient_numerators"]
                offset_a, offset_g, transformed = 0, 0, []
                for output in range(first, stop):
                    for column in range(FREE):
                        bound = 2+EPS[column]-EPS[output]
                        piece_a = raw_a[offset_a:offset_a+bound+1]
                        piece_g = raw_g[offset_g:offset_g+bound+2]
                        assert len(piece_a) == bound+1 and len(piece_g) == bound+2
                        values = [0]*(bound+1)
                        negative = 0
                        for power, raw in enumerate(piece_a):
                            exponent = bound-1-power
                            value = int(raw)*fa
                            if exponent == -1:
                                negative += value
                            else:
                                assert 0 <= exponent <= bound
                                values[exponent] += value
                        for power, raw in enumerate(piece_g):
                            exponent = bound-power
                            value = -EPS[column]*int(raw)*fg
                            if exponent == -1:
                                negative += value
                            else:
                                assert 0 <= exponent <= bound
                                values[exponent] += value
                        assert negative == 0, "The complete original connection must be regular on the sigma chart."
                        if column == 0:
                            assert all(value == 0 for value in values)
                        transformed.extend(values)
                        offset_a += bound+1
                        offset_g += bound+2
                assert offset_a == len(raw_a) and offset_g == len(raw_g)
                assert len(transformed) == self.coefficient_count(2, first, stop)
                self.store(name, {
                    "target": target, "field_component": 0,
                    "source_tau_matrix_row_block": gamma_entry,
                    "source_Mg_tau_matrix_row_block": g_entry, "source_exact_Mg": g_spec,
                    "source_exact_candidate": candidate_spec,
                    "row_first": first, "row_stop": stop, "regular_degree_bound": 2,
                    "entry_order": "output_row, input_column, power=0..2+eps_column-eps_row",
                    "common_positive_denominator": str(common),
                    "coefficient_numerators": [str(value) for value in transformed],
                    "transition": "Gamma_sigma=t*D*Gamma_tau(1/t)*D^-1-t^2*D*Mg(1/t)*D^-1*diag(eps)",
                    "D": "diag(t^-eps_a); output rows left, input columns right",
                    "regular_derivation_relation": "delta_sigma=t*delta_tau",
                    "all_negative_power_coefficients_cancelled_exactly": True,
                    "weighted_degree_bound_verified": True,
                    "original_unit_column_zero_verified": True,
                    "homogeneous_matrix_reversal_used_as_connection": False,
                }, target)
                old = self.cached(name, target)
            assert old["source_tau_matrix_row_block"] == gamma_entry
            assert old["source_Mg_tau_matrix_row_block"] == g_entry
            assert old["source_exact_candidate"] == candidate_spec
            assert old["all_negative_power_coefficients_cancelled_exactly"] is True
            assert old["weighted_degree_bound_verified"] is True
            sigma_specs.append(spec(self.path(name)))
        receipt = self.CRT_history_and_cleanup(target, component, current)
        name = stem+"-certified-connection-index"
        self.store(name, {
            "target": target, "field_component": 0,
            "source_original_vector": vector["source"], "source_original_h_vector": h["source"],
            "source_exact_Mg": g_spec, "regular_degree_bound": 2, "weighted_degree_shift": 2,
            "coefficient_field_basis": FIELD,
            "source_candidate": candidate_spec,
            "matrix_row_blocks_tau": candidate["matrix_row_blocks"],
            "matrix_row_blocks_sigma": sigma_specs,
            "weighted_entry_order": "output_row, input_column, power=0..2+eps_column-eps_row",
            "matrix_convention": "Gamma_ba output row b input column a; delta(beta*v)=beta*(Gamma*v+Mg*vprime)",
            "exact_original_column_certificate": first_spec,
            "weighted_degree_bound_verified": True,
            "Gamma_zero_first_column_and_H_original_first_column_verified": True,
            "complete_nested_commutator_identity_verified": True,
            "H_definition": "Gamma*Mw-Mw*Gamma+Mg*dMw/dz",
            "nested_commutator_weighted_degree_shift": 4,
            "nested_commutator_maximum_degree": 6,
            "exact_nested_commutator_points": exact_points,
            "exact_full_matrix_point_certificates": point_specs,
            "identity_certified_by_strict_degree_and_7_distinct_exact_points": True,
            "cyclic_uniqueness_identifies_H_with_actual_Mh": True,
            "original_nonhomogeneous_connection_identity_therefore_verified": True,
            "source_R806_cyclic_witness": self.witness_spec,
            "independent_Mh_reconstructed_or_stored": False,
            "sigma_regular_connection_verified_with_original_derivation_change": True,
            "all_original_scalar_and_field_normalizations_preserved": True,
            "actual_CRT_prime_count": current["prime_count"],
            "actual_CRT_primes": current["consumed_primes"],
            "actual_CRT_modulus_bits": int(current["modulus"]).bit_length(),
            "latest_CRT_history_receipt": receipt,
            "no_characteristic_zero_Krylov_inverse_formed": True,
            "original_cusp_zero_ideal_computed": False,
            "polar_ideal_or_original_function_DAG_computed": False,
        }, target)
        print(json.dumps({"stage": "certified_original_normal_connection",
                          "CRT_prime_count": current["prime_count"],
                          "exact_nested_commutator_points": exact_points,
                          "seconds": time.monotonic()-self.started}), flush=True)
        return True, spec(self.path(name))

    def validate_completed_component(self, target, component, entry):
        if target != "Gamma":
            assert target == "g" and component == 0
            data = super().validate_completed_component(target, component, entry)
            assert data["operator_kind"] == "multiplication"
            assert data["coefficient_field_basis"] == FIELD
            assert data["regular_degree_bound"] == 3
            assert data["zero_component_proved_from_exact_original_vector"] is False
            return data
        assert component == 0 and spec(self.path(entry["file"])) == entry
        data = self.cached(entry["file"], target)
        assert data["target"] == target and data["field_component"] == component
        assert data["operator_kind"] == "normal_derivation_connection"
        assert data["coefficient_field_basis"] == FIELD
        assert data["source_original_vector"] == self.target_component("Gamma", 0)["source"]
        assert data["source_original_h_vector"] == self.target_component("h", 0)["source"]
        assert data["source_exact_Mg"] == self.operator_indices["g"]
        assert data["weighted_degree_shift"] == data["regular_degree_bound"] == 2
        for key in ("weighted_degree_bound_verified",
                    "Gamma_zero_first_column_and_H_original_first_column_verified",
                    "complete_nested_commutator_identity_verified",
                    "cyclic_uniqueness_identifies_H_with_actual_Mh",
                    "original_nonhomogeneous_connection_identity_therefore_verified",
                    "sigma_regular_connection_verified_with_original_derivation_change"):
            assert data[key] is True
        assert data["independent_Mh_reconstructed_or_stored"] is False
        candidate_spec = data["source_candidate"]
        assert spec(self.path(candidate_spec["file"])) == candidate_spec
        candidate = self.cached(candidate_spec["file"], target)
        assert candidate["matrix_row_blocks"] == data["matrix_row_blocks_tau"]
        assert candidate["source_original_vector"] == data["source_original_vector"]
        assert len(data["matrix_row_blocks_tau"]) == len(data["matrix_row_blocks_sigma"]) == len(self.block_ranges)
        g_index = self.cached(self.operator_indices["g"]["file"], "g")
        for tau_spec, sigma_spec, g_spec, (first, stop) in zip(
                data["matrix_row_blocks_tau"], data["matrix_row_blocks_sigma"],
                g_index["matrix_row_blocks_tau"], self.block_ranges):
            for block_spec in (tau_spec, sigma_spec):
                assert spec(self.path(block_spec["file"])) == block_spec
                block = self.cached(block_spec["file"], target)
                assert (block["row_first"], block["row_stop"]) == (first, stop)
                assert block["target"] == target and block["field_component"] == 0
                assert int(block["common_positive_denominator"]) > 0
                assert len(block["coefficient_numerators"]) == self.coefficient_count(2, first, stop)
            sigma = self.cached(sigma_spec["file"], target)
            assert sigma["source_tau_matrix_row_block"] == tau_spec
            assert sigma["source_Mg_tau_matrix_row_block"] == g_spec
            assert sigma["source_exact_candidate"] == candidate_spec
            assert sigma["all_negative_power_coefficients_cancelled_exactly"] is True
            assert sigma["original_unit_column_zero_verified"] is True
        first_spec = data["exact_original_column_certificate"]
        assert spec(self.path(first_spec["file"])) == first_spec
        first = self.cached(first_spec["file"], target)
        assert first["source_candidate"] == candidate_spec
        assert first["source_exact_Mg"] == self.operator_indices["g"]
        assert first["source_original_h_vector"] == data["source_original_h_vector"]
        assert first["Gamma_e0_zero_verified_coefficientwise"] is True
        assert first["H_e0_equals_original_h_verified_coefficientwise"] is True
        assert data["nested_commutator_maximum_degree"] == 6
        assert data["exact_nested_commutator_points"] == list(range(7))
        assert len(data["exact_full_matrix_point_certificates"]) == 7
        for point, point_spec in zip(range(7), data["exact_full_matrix_point_certificates"]):
            assert spec(self.path(point_spec["file"])) == point_spec
            point_data = self.cached(point_spec["file"], target)
            assert point_data["source_candidate"] == candidate_spec
            assert point_data["source_exact_Mg"] == self.operator_indices["g"]
            assert point_data["source_original_M_w"] == self.w_input_spec
            assert point_data["source_original_h_vector"] == data["source_original_h_vector"]
            assert point_data["exact_integer_point"] == point
            assert point_data["all_exact_nested_commutator_entries_zero"] is True
            assert len(point_data["full_row_block_certificates"]) == len(self.block_ranges)
            for block_spec, (first, stop) in zip(point_data["full_row_block_certificates"], self.block_ranges):
                assert spec(self.path(block_spec["file"])) == block_spec
                block = self.cached(block_spec["file"], target)
                assert block["source_candidate"] == candidate_spec
                assert block["source_exact_Mg"] == self.operator_indices["g"]
                assert block["source_original_M_w"] == self.w_input_spec
                assert block["exact_integer_point"] == point
                assert (block["row_first"], block["row_stop"]) == (first, stop)
                assert block["column_count"] == FREE
                assert block["all_exact_integer_nested_commutator_entries_zero"] is True
        receipt_spec = data["latest_CRT_history_receipt"]
        assert spec(self.path(receipt_spec["file"])) == receipt_spec
        receipt = self.cached(receipt_spec["file"], target)
        assert receipt["current_full_CRT_checkpoint"] == candidate["source_CRT_checkpoint"]
        assert receipt["prime_count"] == data["actual_CRT_prime_count"]
        return data

    def run(self):
        final = self.out/FINAL
        if final.exists():
            prior = read(final)
            assert prior["result"] == RESULT and prior["complete"] is True
            assert prior["configuration"] == self.tag and prior["completed_scope"] == SCOPE
            assert prior["target_configurations"] == self.target_tags
            manifest_spec = prior["stage_manifest"]
            assert spec(self.path(manifest_spec["file"])) == manifest_spec
            manifest = self.cached(manifest_spec["file"])
            for entry in manifest["files"]:
                assert spec(self.path(entry["file"])) == entry
        self.load_w()
        # The h vector is input only. No independent Mh matrix or CRT state is constructed.
        self.target_component("h", 0)
        for target in TARGETS:
            self.operator_indices[target] = self.component(target, 0)
            self.validate_completed_component(target, 0, self.operator_indices[target])
        assert not list(self.out.glob("R815-*-CRT-current.json.gz"))
        assert not list(self.out.glob("R815-target-h-*-CRT-*.json.gz"))
        files = [spec(path) for path in sorted(self.out.glob("R815-*.json.gz"))
                 if not path.name.startswith("R815-stage-manifest-")]
        manifest_name = "R815-stage-manifest-"+fingerprint(files)[:24]
        previous = self.cached(manifest_name)
        if previous is None:
            manifest_spec = self.store(manifest_name, {"files": files})
        else:
            assert previous["files"] == files
            manifest_spec = spec(self.path(manifest_name))
        indexes = {target: self.cached(entry["file"], target)
                   for target, entry in self.operator_indices.items()}
        certificate = {
            "result": RESULT, "complete": True, "configuration": self.tag, "p": 41,
            "completed_scope": SCOPE, "requested_targets": list(TARGETS),
            "target_configurations": self.target_tags,
            "normal_affine_basis_rank": FREE, "normal_basis_degrees": EPS,
            "coefficient_field_basis": FIELD,
            "actual_sigma_integer_n": self.r806.tag["actual_sigma_integer_n"],
            "source_R806_polynomial_multiplier": self.w_spec,
            "source_R806_cyclic_witness": self.witness_spec,
            "source_R813_exact_coordinates": self.source_coordinate_spec,
            "source_R813_normal_interface": self.normal_interface_spec,
            "actual_input_producers": {"R806": producer_identity(self.r806.identity),
                                      "R813": producer_identity(self.r813.identity)},
            "shared_point_mathematical_identity": self.cache_identity,
            "operator_indices": self.operator_indices,
            "original_vector_inputs": {target: self.target_component(target, 0)["source"] for target in ("g", "h")},
            "actual_CRT_prime_counts": {target: data["actual_CRT_prime_count"] for target, data in indexes.items()},
            "original_Mg_computed": True,
            "original_normal_derivation_connection_computed": True,
            "independent_Mh_reconstructed_or_stored": False,
            "original_Mh_identified_by_nested_commutator_and_original_first_column": True,
            "all_weighted_supports_and_original_column_constraints_verified": True,
            "all_complete_polynomial_defining_identities_verified": True,
            "Mg_exact_commutator_points": list(range(7)),
            "Gamma_exact_nested_commutator_points": list(range(7)),
            "Gamma_nonhomogeneous_identity_with_actual_Mh_certified": True,
            "original_tau_chart_derivation": "delta_tau=D0/tau; D0=(qY/82)d/dqY",
            "original_sigma_chart_derivation": "delta_sigma=t*delta_tau; t=1/z",
            "sigma_base_variable_derivative": {
                "matrix_blocks": indexes["g"]["matrix_row_blocks_sigma"],
                "rational_scalar": [-1, 1],
                "identity": "M_(delta_sigma t)=-t^3*D*Mg(1/t)*D^-1"},
            "normal_integral_basis_preserved": True,
            "all_original_scalar_and_field_normalizations_preserved": True,
            "old_Fourier_Wronskian_S3_Dixon_or_primitive_results_recomputed": False,
            "characteristic_zero_Krylov_matrix_or_inverse_computed": False,
            "original_cusp_zero_ideal_computed": False,
            "original_function_DAG_polar_divisors_eta_or_height_computed": False,
            "stage_manifest": manifest_spec, "seconds": time.monotonic()-self.started,
        }
        save(final, certificate)
        save(self.out/"core-receipt.json", {
            "result": RESULT, "complete": True, "source_sha256": sha(__file__),
            "framework_sha256": sha(framework.__file__), "certificate_sha256": sha(final),
            "completed_scope": SCOPE,
            "original_Mg_computed": True,
            "original_normal_derivation_connection_computed": True,
            "independent_Mh_reconstructed_or_stored": False,
            "all_complete_polynomial_defining_identities_verified": True,
            "original_cusp_zero_ideal_computed": False,
            "original_function_DAG_polar_divisors_eta_or_height_computed": False,
        })
        return 0


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "proof", "nested-proof", "method", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    try:
        return Job(args).run()
    except BaseException as error:
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "framework_sha256": sha(framework.__file__),
            "error": type(error).__name__+": "+str(error),
            "completed_source_bound_stages_and_current_CRT_preserved": True,
            "independent_Mh_reconstructed_or_stored": False,
            "original_cusp_zero_ideal_computed": False,
            "original_function_DAG_polar_divisors_eta_or_height_computed": False,
        })
        raise


if __name__ == "__main__":
    sys.exit(main())
