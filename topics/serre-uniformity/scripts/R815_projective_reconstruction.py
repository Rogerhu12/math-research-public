#!/usr/bin/env python3
"""Independent R815 consumer: a true 425-prime source, 3D Q denominator candidates,
the original complete Mg certificate, then the frozen Gamma arithmetic.
No old stage is relabelled. All new mathematical work belongs to public Actions.
"""
import argparse
import gc
import json
import math
import re
import sys
import time
from pathlib import Path

import flint
from flint import fmpq, fmpz, fmpz_mat
import R815_original_normal_derivation_operators as legacy
import R811_original_regular_multipliers as framework
from R815_original_normal_derivation_operators import (
    RESULT, FINAL, SCOPE, FREE, S3, EPS, TARGETS, INPUT_LABELS, FIELD,
    R806_CORE_SHA, R813_CORE_SHA, FRAMEWORK_SHA, guard,
)
from R811_original_regular_multipliers import (
    Retained, BudgetStop, sha, read, save, spec, plain, fingerprint,
    producer_identity, same_producer, rows, matrix_block, integer_evaluate,
    S3_position, rational_reconstruct,
)

LEGACY_SHA = "80516ff9598fdb6251628c00794dc3529b998a7c563fe80fd9c31406e3896c7d"
PROJECTIVE_MODE = "known-first-column-and-three-dimensional-Q-common-denominator"
SHIFTS = (0, 256, -256, 1024, -1024, 4096, -4096)
SEARCH_STRATEGY = {
    "probe_order": "weighted output_row,input_column,power; omit column0; consecutive strict-RR failures at the actual 425 modulus",
    "probe_fallback": "at end, one failing entry may pair with first distinct nonzero non-column0 entry; all-successful RR supplies its actual lcm",
    "known_denominator": "the reduced exact original g-first-column common denominator dg",
    "integer_row_lattice": "[(dg,center(dg*ri),center(dg*rj)),(0,M,0),(0,0,M)]",
    "column_weights": "wd=2^max(shift,0), wn=2^max(-shift,0)",
    "fixed_shifts": list(SHIFTS),
    "LLL_rows_consumed": "all three basis rows with complete integral unimodular witnesses; no height bound",
    "known_column_lift": "column0=D*vg exactly; every other coefficient=center(D*residue)",
    "exact_early_entries": "a subset of the same seven complete commutators, at integer points 0 and 1",
    "success_exit": "original full first column, weighted support, and all 272x272 entries at exact z=0,...,6",
}
POINT_NAME = re.compile(r"R815-prime-[0-9]+-z-[0-9]+-Krylov-inverse[.]json[.]gz")
ORIGINAL_SCALARS = (
    "R815-original-primitive-polynomial-input.json.gz",
    "R815-target-g-component-00-original-vector.json.gz",
    "R815-target-h-component-00-original-vector.json.gz",
)
SOURCE_KEYS = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")


def checkpoint_identity(item):
    answer = {key: str(item[key]) for key in SOURCE_KEYS}
    assert answer["result"] == RESULT
    assert answer["core_sha256"] == LEGACY_SHA
    assert answer["run_id"] == "43719622321"
    assert answer["source_commit"] == "2a3300a9edec73c23e72f23127a0ae7d8222d13e"
    assert answer["manifest_sha256"] == "4e78095e2adc217beb86d4f760e6207a4aa60c4492bbfcc739a8544f376842e5"
    return answer


def centered(value, modulus):
    answer = value % modulus
    return answer-modulus if 2*answer > modulus else answer


class SearchExhausted(Exception):
    pass


class Job(legacy.Job):
    def __init__(self, args):
        self.args, self.out, self.started = args, args.output, time.monotonic()
        self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        assert self.item["producer_inputs_pending"] is False
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert self.item["core_sha256"] == sha(__file__)
        assert sha(legacy.__file__) == self.item["legacy_core_sha256"] == LEGACY_SHA
        assert sha(args.projective_method) == self.item["projective_method_sha256"]
        self.external_root = args.retained/"R815"
        self.source = self.item["projective_source"]
        self.source_identity = checkpoint_identity(self.source)
        self.source_files = self.source["files"]
        for name, entry in self.source_files.items():
            assert Path(name).name == name and plain(entry)["file"] == name
        self.external_aliases = {
            name for name in self.source_files
            if name in ORIGINAL_SCALARS or POINT_NAME.fullmatch(name)
        }
        assert set(ORIGINAL_SCALARS).issubset(self.external_aliases)
        self.old_receipt = self.raw_source(self.source["latest_CRT_receipt"]["file"])
        self.old_tag = self.old_receipt["configuration"]
        assert self.old_receipt["complete"] is True
        assert self.old_receipt["target"] == "g" and self.old_receipt["field_component"] == 0
        self.old_target_tags = {}
        self.old_current = None
        self.current_spec = plain(self.source["current"])
        self.receipt_spec = plain(self.source["latest_CRT_receipt"])
        assert plain(self.source_files[self.current_spec["file"]]) == self.current_spec
        assert plain(self.source_files[self.receipt_spec["file"]]) == self.receipt_spec
        assert self.old_receipt["current_full_CRT_checkpoint"] == self.current_spec
        assert self.old_receipt["prime_count"] == 425
        assert self.old_receipt["latest_prime"] == 1000008791
        assert self.old_receipt["modulus_bits"] == 12707
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
        expected_old_tag = dict(self.tag, source_sha256=LEGACY_SHA)
        assert self.old_tag == expected_old_tag
        self.tag.update({
            "projective_mode": PROJECTIVE_MODE,
            "projective_method_sha256": sha(args.projective_method),
            "legacy_R815_core_sha256": sha(legacy.__file__),
            "projective_source_identity": self.source_identity,
            "source_original_425_configuration_sha256": fingerprint(self.old_tag),
            "source_original_425_current": self.current_spec,
            "source_original_425_receipt": self.receipt_spec,
            "projective_search_strategy": SEARCH_STRATEGY,
            "original_425_Mg_prime_arithmetic_recomputed": False,
            "only_budget_and_probe_pair_limit_excluded_from_mathematical_identity": True,
        })
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
        self.old_target_tags = {
            target: dict(value, basis_configuration_sha256=fingerprint(self.old_tag))
            for target, value in self.target_tags.items()
        }
        assert self.old_receipt["target_configuration"] == self.old_target_tags["g"]
        assert self.old_receipt["target_configuration_sha256"] == fingerprint(self.old_target_tags["g"])
        self.w_coefficients = None
        self.w_denominator = None
        self.prime_values, self.target_vectors = [], {}
        self.block_ranges = [(first, min(first+self.item["matrix_row_block_size"], FREE))
                             for first in range(0, FREE, self.item["matrix_row_block_size"])]
        self.operator_indices, self.operator_matrices = {}, {}



    @staticmethod
    def canonical_name(name):
        assert Path(name).name == name
        if name.startswith("R811-"):
            name = "R815-"+name[5:]
        assert name.startswith("R815-")
        return name if name.endswith(".json.gz") else name+".json.gz"

    def raw_source(self, name):
        assert Path(name).name == name and name in self.source_files
        path = self.external_root/name
        assert spec(path) == plain(self.source_files[name])
        return read(path)

    def external_stage(self, name, target=None, current=False):
        data = self.raw_source(name)
        assert data["configuration"] == self.old_tag
        assert data["complete"] is (not current)
        if target is None:
            assert "target_configuration" not in data
        else:
            assert data["target_configuration"] == self.old_target_tags[target]
            assert data["target_configuration_sha256"] == fingerprint(self.old_target_tags[target])
        if POINT_NAME.fullmatch(name):
            assert target is None and not current
            assert data["shared_point_mathematical_identity"] == self.cache_identity
            assert data["source_bound_external_cache_consumption_allowed"] is True
            assert data["external_consumer_must_preserve_original_R815_stage_identity"] is True
        return data

    def path(self, name):
        canonical = self.canonical_name(name)
        if canonical in getattr(self, "external_aliases", set()):
            return self.external_root/canonical
        return legacy.Job.path(self, name)

    def cached(self, name, target=None, current=False):
        canonical = self.canonical_name(name)
        if canonical in self.external_aliases:
            assert not current
            return self.external_stage(canonical, target)
        return legacy.Job.cached(self, name, target, current)

    def store(self, name, value, target=None, current=False, replace=False):
        assert self.canonical_name(name) not in self.external_aliases, \
            "An immutable external original stage cannot be overwritten or relabelled."
        return legacy.Job.store(self, name, value, target, current, replace)

    def positions(self):
        if hasattr(self, "offsets"):
            return
        self.offsets, self.row_starts = [], []
        cursor = 0
        for output in range(FREE):
            self.row_starts.append(cursor)
            line = []
            for column in range(FREE):
                line.append(cursor)
                cursor += 4+EPS[column]-EPS[output]
            self.offsets.append(line)
        self.total_coefficients = cursor
        assert cursor == 295936 == self.coefficient_count(3)

    def location(self, index):
        assert 0 <= index < self.total_coefficients
        import bisect
        output = bisect.bisect_right(self.row_starts, index)-1
        column = bisect.bisect_right(self.offsets[output], index)-1
        power = index-self.offsets[output][column]
        assert 0 <= power <= 3+EPS[column]-EPS[output]
        return output, column, power

    def residue(self, index):
        value = int(self.old_current["lifted_coefficients"][index])
        assert 0 <= value < self.modulus
        return value

    def load_current(self):
        if self.old_current is not None:
            return
        self.positions()
        data = self.external_stage(self.current_spec["file"], "g", current=True)
        assert data["target"] == "g" and data["field_component"] == 0
        assert data["regular_degree_bound"] == 3
        assert data["source_original_vector"] == self.target_component("g", 0)["source"]
        assert data["prime_count"] == 425
        primes, indices = data["consumed_primes"], data["consumed_prime_indices"]
        assert len(primes) == len(indices) == 425 and len(set(primes)) == 425
        assert indices == sorted(set(indices))
        assert all(self.prime_at(i) == p for i, p in zip(indices, primes))
        assert primes[-1] == self.old_receipt["latest_prime"] == 1000008791
        modulus = int(data["modulus"])
        assert modulus == math.prod(primes) and modulus.bit_length() == 12707
        assert len(data["lifted_coefficients"]) == self.total_coefficients
        assert data["previous_checkpoint_sha256"] == self.old_receipt["previous_checkpoint_sha256"]
        assert data["previous_CRT_receipt"] == self.old_receipt["previous_CRT_receipt"]
        self.old_current, self.modulus = data, modulus
        vector = self.target_component("g", 0)
        dg = vector["denominator"]
        assert dg > 0 and math.gcd(dg, modulus) == 1
        content = dg
        for line in vector["values"]:
            for value in line:
                content = math.gcd(content, value)
        assert content == 1, "Use the true reduced first-column common denominator."
        self.dg = dg
        audit_name = "R815-projective-original-425-source-audit"
        audit = self.cached(audit_name)
        if audit is None:
            inverse = pow(dg, -1, modulus)
            count = 0
            for output in range(FREE):
                for power in range(4-EPS[output]):
                    index = self.offsets[output][0]+power
                    assert self.residue(index) == vector["values"][power][output]*inverse % modulus
                    count += 1
            assert count == 690
            self.store(audit_name, {
                "source_original_425_identity": self.source_identity,
                "source_original_configuration_sha256": fingerprint(self.old_tag),
                "source_original_current": self.current_spec,
                "source_original_latest_receipt": self.receipt_spec,
                "source_original_g_vector": vector["source"],
                "source_original_h_vector": self.target_component("h", 0)["source"],
                "source_original_W_integer_polynomial": self.w_input_spec,
                "coefficient_count": self.total_coefficients,
                "prime_count": len(primes), "latest_prime": primes[-1],
                "modulus_bits": modulus.bit_length(),
                "actual_reduced_g_first_column_denominator": str(dg),
                "all690_original_first_column_CRT_congruences_verified": True,
                "complete_current_bytes_and_SHA_checked_before_use": True,
                "old_point_stages_consumed_with_original_configuration": True,
                "source_original_425_prime_arithmetic_recomputed": False,
                "original_Mg_or_Gamma_claimed_from_CRT": False,
            })
            audit = self.cached(audit_name)
        assert audit["source_original_current"] == self.current_spec
        assert audit["actual_reduced_g_first_column_denominator"] == str(dg)
        assert audit["all690_original_first_column_CRT_congruences_verified"] is True
        self.audit_spec = spec(self.path(audit_name))

    def probe_state(self):
        name = "R815-projective-probe-scan-current"
        data = self.cached(name, current=True)
        if data is None:
            data = {
                "source_original_current": self.current_spec,
                "next_coefficient_index": 0, "unpaired_failure": None,
                "completed_pair_count": 0, "first_nonzero_nonfirst_column_positions": [],
                "all_scalar_RR_denominator_if_no_failure": "1",
                "scalar_RR_failure_count": 0, "scan_finished": False,
            }
            self.store(name, data, current=True)
            data = self.cached(name, current=True)
        assert data["source_original_current"] == self.current_spec
        assert 0 <= data["next_coefficient_index"] <= self.total_coefficients
        return data

    def commit_probe_state(self, data):
        self.store("R815-projective-probe-scan-current", data, current=True)

    def publish_probe_pair(self, state, first, second, fallback=False):
        number = state["completed_pair_count"]
        name = "R815-projective-probe-pair-"+str(number).zfill(6)
        assert first != second
        probes = []
        for index in (first, second):
            location = self.location(index)
            assert location[1] != 0
            probes.append({
                "coefficient_index": index, "weighted_location": list(location),
                "residue_mod_original_M": str(self.residue(index)),
            })
        continuation = dict(state, completed_pair_count=number+1, unpaired_failure=None)
        expected = {
            "resume_after_pair": continuation,
            "pair_number": number, "source_original_current": self.current_spec,
            "probe_selection": SEARCH_STRATEGY["probe_order"],
            "fallback_after_exhausting_actual_coordinate_order": bool(fallback),
            "probes": probes, "original_modulus_bits": self.modulus.bit_length(),
            "new_scalar_RR_only_at_actual_425_modulus": True,
            "old_424_attempt_or_modular_image_recomputed": False,
        }
        existing = self.cached(name)
        if existing is None:
            self.store(name, expected)
        else:
            for key, value in expected.items():
                assert existing[key] == value
        state["completed_pair_count"] += 1
        state["unpaired_failure"] = None
        self.commit_probe_state(state)
        return self.cached(name), spec(self.path(name))

    def next_probe_pair(self, number):
        old_name = "R815-projective-probe-pair-"+str(number).zfill(6)
        old = self.cached(old_name)
        if old is not None:
            assert old["source_original_current"] == self.current_spec
            state = self.probe_state()
            if state["completed_pair_count"] <= number:
                assert state["completed_pair_count"] == number
                self.commit_probe_state(old["resume_after_pair"])
            return old, spec(self.path(old_name))
        state = self.probe_state()
        assert state["completed_pair_count"] == number
        if state["scan_finished"]:
            return None
        since_commit = 0
        while state["next_coefficient_index"] < self.total_coefficients:
            self.budget()
            index = state["next_coefficient_index"]
            location = self.location(index)
            state["next_coefficient_index"] += 1
            if location[1] == 0:
                continue
            residue = self.residue(index)
            if residue and len(state["first_nonzero_nonfirst_column_positions"]) < 2:
                state["first_nonzero_nonfirst_column_positions"].append(index)
            rational = rational_reconstruct(residue, self.modulus)
            if rational is None:
                state["scalar_RR_failure_count"] += 1
                state["all_scalar_RR_denominator_if_no_failure"] = None
                if state["unpaired_failure"] is not None:
                    first = state["unpaired_failure"]
                    return self.publish_probe_pair(state, first, index)
                state["unpaired_failure"] = index
            elif state["all_scalar_RR_denominator_if_no_failure"] is not None:
                state["all_scalar_RR_denominator_if_no_failure"] = str(math.lcm(
                    int(state["all_scalar_RR_denominator_if_no_failure"]), int(rational.denom())))
            since_commit += 1
            if since_commit >= 128:
                self.commit_probe_state(state)
                since_commit = 0
        state["scan_finished"] = True
        if state["unpaired_failure"] is not None:
            first = state["unpaired_failure"]
            alternatives = [x for x in state["first_nonzero_nonfirst_column_positions"] if x != first]
            if alternatives:
                return self.publish_probe_pair(state, first, alternatives[0], fallback=True)
        self.commit_probe_state(state)
        return None


    def lattice_candidates(self, pair, pair_spec, shift):
        number = pair["pair_number"]
        label = ("plus" if shift >= 0 else "minus")+str(abs(shift))
        name = "R815-projective-pair-"+str(number).zfill(6)+"-weight-"+label+"-LLL"
        data = self.cached(name)
        if data is None:
            self.budget()
            wd, wn = 1 << max(shift, 0), 1 << max(-shift, 0)
            r0, r1 = [int(x["residue_mod_original_M"]) for x in pair["probes"]]
            c0, c1 = centered(self.dg*r0, self.modulus), centered(self.dg*r1, self.modulus)
            lattice = fmpz_mat([
                [self.dg*wd, c0*wn, c1*wn],
                [0, self.modulus*wn, 0],
                [0, 0, self.modulus*wn],
            ])
            reduced = lattice.lll(delta=0.99, eta=0.51)
            transformations, entries = [], []
            for row in range(3):
                raw = [int(reduced[row, j]) for j in range(3)]
                assert raw[0] % wd == raw[1] % wn == raw[2] % wn == 0
                D, n0, n1 = raw[0]//wd, raw[1]//wn, raw[2]//wn
                assert D % self.dg == 0
                a = D//self.dg
                assert (n0-a*c0) % self.modulus == (n1-a*c1) % self.modulus == 0
                transformations.append([a, (n0-a*c0)//self.modulus, (n1-a*c1)//self.modulus])
                row_sign = 1 if D >= 0 else -1
                D, n0, n1 = row_sign*D, row_sign*n0, row_sign*n1
                assert (n0-D*r0) % self.modulus == (n1-D*r1) % self.modulus == 0
                reason = ("zero_denominator" if D == 0 else
                          "denominator_not_a_unit_at_original_CRT" if math.gcd(D, self.modulus) != 1 else None)
                entries.append({
                    "LLL_row": row, "row_sign": row_sign,
                    "D": str(D), "probe_numerators": [str(n0), str(n1)],
                    "original_congruences_verified": True,
                    "denominator_is_multiple_of_actual_dg": D % self.dg == 0,
                    "search_rejection_reason": reason,
                    "no_height_rectangle_used": True,
                })
            change = fmpz_mat(transformations)
            determinant = int(change.det())
            assert abs(determinant) == 1 and change*lattice == reduced
            self.store(name, {
                "source_original_current": self.current_spec,
                "source_probe_pair": pair_spec, "pair_number": number, "shift": shift,
                "positive_column_weights": [str(wd), str(wn), str(wn)],
                "original_integer_lattice_rows": rows(lattice, strings=True),
                "actual_LLL_rows": rows(reduced, strings=True),
                "exact_integral_basis_change": rows(change, strings=True),
                "exact_basis_change_determinant": determinant,
                "full_basis_change_equality_verified": True,
                "unweighted_lattice_determinant": str(self.dg*self.modulus*self.modulus),
                "candidates": entries,
                "M_power_two_thirds_success_or_height_guarantee_claimed": False,
                "LLL_is_only_candidate_generation": True,
            })
            data = self.cached(name)
        assert data["source_original_current"] == self.current_spec
        assert data["source_probe_pair"] == pair_spec and data["shift"] == shift
        assert data["full_basis_change_equality_verified"] is True
        assert len(data["candidates"]) == 3
        return data, spec(self.path(name))

    def projective_stem(self, denominator):
        return "R815-projective-g-candidate-"+fingerprint({"D": str(denominator)})[:32]

    def projective_entry(self, D, output, column, point):
        if column == 0:
            vector = self.target_component("g", 0)
            return (D//self.dg)*sum(
                vector["values"][power][output]*(point**power)
                for power in range(4-EPS[output]))
        bound = 3+EPS[column]-EPS[output]
        offset = self.offsets[output][column]
        value = 0
        for power in range(bound, -1, -1):
            value = value*point+centered(D*self.residue(offset+power), self.modulus)
        return value

    def reject_projective_candidate(self, stem, reason, additional):
        name = stem+"-rejected"
        data = self.cached(name, "g")
        if data is None:
            removed = [spec(path) for path in sorted(self.out.glob(stem+"-reconstructed-rows-*.json.gz"))]
            self.store(name, {
                "target": "g", "field_component": 0, "candidate_id": stem,
                "source_original_current": self.current_spec,
                "reason": reason, "additional": additional,
                "discarded_candidate_file_history": removed,
                "only_inactive_rejected_large_candidate_blocks_pruned": True,
                "original_source_current_or_Krylov_cache_deleted": False,
                "no_exact_characteristic_zero_multiplier_claimed": True,
            }, "g")
            data = self.cached(name, "g")
        for entry in data["discarded_candidate_file_history"]:
            path = self.path(entry["file"])
            if path.exists():
                assert spec(path) == entry
                path.unlink()
        return spec(self.path(name))

    def candidate_early_entries(self, D, stem, definition, definition_spec):
        checks = definition["early_exact_commutator_entries"]
        for ordinal, (point, output, column) in enumerate(checks):
            name = stem+"-early-exact-entry-"+str(ordinal).zfill(2)
            data = self.cached(name, "g")
            if data is None:
                self.budget()
                # This is one entry of the very same exact [N,W] at z=0 or 1.
                residual = 0
                for k in range(FREE):
                    w_left = sum(int(self.w_coefficients[j][output, k])*(point**j)
                                 for j in range(len(self.w_coefficients)))
                    w_right = sum(int(self.w_coefficients[j][k, column])*(point**j)
                                  for j in range(len(self.w_coefficients)))
                    if w_right:
                        residual += self.projective_entry(D, output, k, point)*w_right
                    if w_left:
                        residual -= w_left*self.projective_entry(D, k, column, point)
                self.store(name, {
                    "target": "g", "field_component": 0,
                    "source_candidate_definition": definition_spec,
                    "source_original_M_w": self.w_input_spec,
                    "exact_integer_point": point, "output_row": output, "input_column": column,
                    "candidate_denominator_before_block_content_reduction": str(D),
                    "original_W_common_positive_denominator": str(self.w_denominator),
                    "exact_integer_commutator_residual": str(residual),
                    "zero": residual == 0,
                    "entry_is_part_of_the_required_full_seven_point_identity": True,
                    "partial_pass_is_not_a_certificate": True,
                }, "g")
                data = self.cached(name, "g")
            assert data["source_candidate_definition"] == definition_spec
            assert (data["exact_integer_point"], data["output_row"], data["input_column"]) == \
                (point, output, column)
            if not data["zero"]:
                return False, self.reject_projective_candidate(
                    stem, "A required exact commutator entry is nonzero.",
                    {"failed_exact_entry": spec(self.path(name)),
                     "source_candidate_definition": definition_spec})
        return True, [spec(self.path(stem+"-early-exact-entry-"+str(i).zfill(2)))
                      for i in range(len(checks))]

    def construct_projective_candidate(self, D, stem, definition_spec, early_specs):
        index_name = stem+"-candidate-index"
        old = self.cached(index_name, "g")
        if old is not None:
            assert old["source_CRT_checkpoint"] == self.current_spec
            assert old["source_candidate_definition"] == definition_spec
            return old, spec(self.path(index_name))
        vector, block_specs = self.target_component("g", 0), []
        for first, stop in self.block_ranges:
            self.budget()
            name = stem+"-reconstructed-rows-"+str(first).zfill(3)+"-"+str(stop).zfill(3)
            block = self.cached(name, "g")
            if block is None:
                values, content = [], D
                for output in range(first, stop):
                    for column in range(FREE):
                        offset = self.offsets[output][column]
                        for power in range(4+EPS[column]-EPS[output]):
                            residue = self.residue(offset+power)
                            if column == 0:
                                value = (D//self.dg)*vector["values"][power][output]
                            else:
                                value = centered(D*residue, self.modulus)
                            assert (value-D*residue) % self.modulus == 0
                            values.append(value)
                            content = math.gcd(content, value)
                assert content > 0 and D % content == 0
                denominator = D//content
                values = [value//content for value in values]
                assert len(values) == self.coefficient_count(3, first, stop)
                self.store(name, {
                    "target": "g", "field_component": 0, "projective_candidate_id": stem,
                    "source_original_vector": vector["source"],
                    "source_CRT_checkpoint": self.current_spec,
                    "source_candidate_definition": definition_spec,
                    "row_first": first, "row_stop": stop, "regular_degree_bound": 3,
                    "entry_order": "output_row, input_column, power=0..r+eps_column-eps_row",
                    "common_positive_denominator": str(denominator),
                    "coefficient_numerators": [str(x) for x in values],
                    "projective_denominator_before_block_content_reduction": str(D),
                    "removed_integer_block_content": str(content),
                    "all_reconstructed_fractions_checked_against_current_CRT": True,
                    "known_first_column_lift": "exact D*vg, not centered",
                    "remaining_coefficients_lift": "centered D*original_CRT_residue",
                    "no_uniform_reconstruction_rectangle_used": True,
                    "reconstruction_is_only_a_candidate_until_full_exact_identity_verification": True,
                }, "g")
                block = self.cached(name, "g")
            assert block["source_CRT_checkpoint"] == self.current_spec
            assert block["source_candidate_definition"] == definition_spec
            assert (block["row_first"], block["row_stop"]) == (first, stop)
            assert block["projective_denominator_before_block_content_reduction"] == str(D)
            assert len(block["coefficient_numerators"]) == self.coefficient_count(3, first, stop)
            block_specs.append(spec(self.path(name)))
        self.store(index_name, {
            "target": "g", "field_component": 0, "projective_candidate_id": stem,
            "source_original_vector": vector["source"], "source_CRT_checkpoint": self.current_spec,
            "source_candidate_definition": definition_spec,
            "regular_degree_bound": 3, "normal_affine_basis_rank": FREE,
            "matrix_row_blocks": block_specs, "coefficient_count": self.total_coefficients,
            "CRT_modulus": str(self.modulus),
            "source_actual_CRT_prime_count": 425,
            "projective_candidate_id_is_not_a_new_CRT_prime_count": True,
            "early_required_exact_entries": early_specs,
            "matrix_convention": "M_ba output row b input column a",
            "complete_characteristic_zero_identity_verified": False,
        }, "g")
        return self.cached(index_name, "g"), spec(self.path(index_name))

    def imported_CRT_receipt(self, current):
        name = "R815-projective-imported-original-425-CRT-receipt"
        data = self.cached(name, "g")
        if data is None:
            self.store(name, {
                "target": "g", "field_component": 0,
                "prime_count": current["prime_count"],
                "current_full_CRT_checkpoint": self.current_spec,
                "original_external_CRT_source": self.source_identity,
                "original_external_CRT_receipt": self.receipt_spec,
                "original_external_CRT_configuration_sha256": fingerprint(self.old_tag),
                "original_external_current_preserves_its_own_configuration": True,
                "source_original_vector": self.target_component("g", 0)["source"],
                "original_425_prime_arithmetic_recomputed": False,
                "source_checkpoint_or_source_temporary_files_deleted": False,
                "receipt_is_a_new_source_import_record_not_a_relabelled_old_stage": True,
            }, "g")
            data = self.cached(name, "g")
        assert data["current_full_CRT_checkpoint"] == self.current_spec
        assert data["original_external_CRT_receipt"] == self.receipt_spec
        assert data["prime_count"] == 425
        return spec(self.path(name))

    def verify_projective_and_transport(self, current, candidate, candidate_spec):
        target, component = 'g', 0
        vector = self.target_component(target, component)
        degree = vector["degree"]
        stem = candidate["projective_candidate_id"]
        attempt_stem = stem
        assert candidate["source_original_vector"] == vector["source"]
        assert candidate["source_CRT_checkpoint"] == self.current_spec
        assert candidate["regular_degree_bound"] == degree
        blocks = []
        common_denominator = 1
        assert len(candidate["matrix_row_blocks"]) == len(self.block_ranges)
        for entry, (first, stop) in zip(candidate["matrix_row_blocks"], self.block_ranges):
            assert spec(self.path(entry["file"])) == entry
            block = self.cached(entry["file"], target)
            assert block["source_original_vector"] == vector["source"]
            assert (block["row_first"], block["row_stop"]) == (first, stop)
            denominator = int(block["common_positive_denominator"])
            assert denominator > 0
            common_denominator = math.lcm(common_denominator, denominator)
            blocks.append(block)
        coefficients = [fmpz_mat(FREE, FREE) for _ in range(degree+3)]
        for block, (first, stop) in zip(blocks, self.block_ranges):
            factor = common_denominator//int(block["common_positive_denominator"])
            raw = [int(value) for value in block["coefficient_numerators"]]
            assert len(raw) == self.coefficient_count(degree, first, stop)
            offset = 0
            for output in range(first, stop):
                for column in range(FREE):
                    bound = degree+EPS[column]-EPS[output]
                    for power in range(max(0, bound+1)):
                        coefficients[power][output, column] = raw[offset]*factor
                        offset += 1
            assert offset == len(raw)
        # Construction only writes the proven weighted support; audit that support explicitly.
        for power, matrix in enumerate(coefficients):
            for output in range(FREE):
                for column in range(FREE):
                    if power > degree+EPS[column]-EPS[output]:
                        assert matrix[output, column] == 0
        first_name = attempt_stem+"-exact-first-column"
        first_certificate = self.cached(first_name, target)
        if first_certificate is None:
            for power, matrix in enumerate(coefficients):
                for output in range(FREE):
                    expected = vector["values"][power][output] if power <= degree else 0
                    if int(matrix[output, 0])*vector["denominator"] != expected*common_denominator:
                        rejection = self.reject_projective_candidate(stem,
                            "The reconstructed candidate does not yet equal the exact original first column.",
                            {"power": power, "output_row": output, "source_candidate": candidate_spec})
                        return False, rejection
            self.store(first_name, {
                "target": target, "field_component": component, "source_candidate": candidate_spec,
                "source_original_vector": vector["source"],
                "regular_degree_bound": degree,
                "original_first_column_verified_coefficientwise": True,
                "candidate_weighted_support_verified_for_every_entry": True,
                "original_M_w_weighted_support_verified_for_every_entry": True,
                "source_original_M_w": self.w_input_spec,
                "commutator_entry_bound": "r+1+eps_input-eps_output",
                "commutator_maximum_degree": degree+3,
            }, target)
            first_certificate = self.cached(first_name, target)
        assert first_certificate["source_candidate"] == candidate_spec
        assert first_certificate["source_original_vector"] == vector["source"]
        assert first_certificate["original_first_column_verified_coefficientwise"] is True
        assert first_certificate["commutator_maximum_degree"] == degree+3
        first_spec = spec(self.path(first_name))
        exact_points = list(range(degree+4))
        point_certificates = []
        for point in exact_points:
            self.budget()
            point_name = attempt_stem+"-exact-commutator-z-"+str(point)+"-index"
            point_certificate = self.cached(point_name, target)
            if point_certificate is None:
                pending, verified_blocks = [], []
                for first, stop in self.block_ranges:
                    block_name = attempt_stem+"-exact-commutator-z-"+str(point)+"-rows-"+str(first).zfill(3)+"-"+str(stop).zfill(3)
                    block_certificate = self.cached(block_name, target)
                    if block_certificate is None:
                        pending.append((first, stop, block_name))
                    else:
                        assert block_certificate["source_candidate"] == candidate_spec
                        assert block_certificate["source_original_M_w"] == self.w_input_spec
                        assert block_certificate["exact_integer_point"] == point
                        assert (block_certificate["row_first"], block_certificate["row_stop"]) == (first, stop)
                        assert block_certificate["all_exact_integer_commutator_entries_zero"] is True
                if pending:
                    numerator_value = integer_evaluate(coefficients, point)
                    w_value = integer_evaluate(self.w_coefficients, point)
                    for first, stop, block_name in pending:
                        self.budget()
                        residual = matrix_block(numerator_value, first, stop)*w_value \
                                   - matrix_block(w_value, first, stop)*numerator_value
                        failure = None
                        for row in range(stop-first):
                            for column in range(FREE):
                                if residual[row, column]:
                                    failure = {"output_row": first+row, "input_column": column,
                                               "exact_integer_residual": str(residual[row, column])}
                                    break
                            if failure is not None:
                                break
                        if failure is not None:
                            rejection = self.reject_projective_candidate(stem,
                                "The reconstructed candidate has a nonzero exact commutator.",
                                dict(failure, exact_integer_point=point, source_candidate=candidate_spec))
                            return False, rejection
                        self.store(block_name, {
                            "target": target, "field_component": component,
                            "source_candidate": candidate_spec, "source_original_M_w": self.w_input_spec,
                            "exact_integer_point": point, "row_first": first, "row_stop": stop,
                            "column_count": FREE,
                            "candidate_common_positive_denominator": str(common_denominator),
                            "original_M_w_common_positive_denominator": str(self.w_denominator),
                            "both_products_computed_over_Z_after_exact_denominator_clearing": True,
                            "all_exact_integer_commutator_entries_zero": True,
                            "random_modular_evaluation_used_as_exact_identity": False,
                        }, target)
                for first, stop in self.block_ranges:
                    block_name = attempt_stem+"-exact-commutator-z-"+str(point)+"-rows-"+str(first).zfill(3)+"-"+str(stop).zfill(3)
                    block_certificate = self.cached(block_name, target)
                    assert block_certificate["source_candidate"] == candidate_spec
                    assert block_certificate["all_exact_integer_commutator_entries_zero"] is True
                    verified_blocks.append(spec(self.path(block_name)))
                self.store(point_name, {
                    "target": target, "field_component": component,
                    "source_candidate": candidate_spec, "source_original_M_w": self.w_input_spec,
                    "exact_integer_point": point, "full_row_block_certificates": verified_blocks,
                    "full_matrix_shape": [FREE, FREE], "all_exact_commutator_entries_zero": True,
                    "Krylov_invertibility_not_required_at_exact_verification_point": True,
                }, target)
                point_certificate = self.cached(point_name, target)
            assert point_certificate["source_candidate"] == candidate_spec
            assert point_certificate["source_original_M_w"] == self.w_input_spec
            assert point_certificate["exact_integer_point"] == point
            assert point_certificate["all_exact_commutator_entries_zero"] is True
            point_certificates.append(spec(self.path(point_name)))
        assert len(exact_points) == degree+4 and len(set(exact_points)) == degree+4
        # The validated weighted bounds imply every commutator entry has degree <=r+3.
        # Therefore these exact r+4 zeros certify the complete polynomial identity.
        sigma_specs = []
        for entry, block, (first, stop) in zip(candidate["matrix_row_blocks"], blocks, self.block_ranges):
            self.budget()
            name = stem+"-sigma-rows-"+str(first).zfill(3)+"-"+str(stop).zfill(3)
            old = self.cached(name, target)
            if old is None:
                raw = [int(value) for value in block["coefficient_numerators"]]
                transformed, offset = [], 0
                for output in range(first, stop):
                    for column in range(FREE):
                        bound = degree+EPS[column]-EPS[output]
                        count = max(0, bound+1)
                        piece = raw[offset:offset+count]
                        assert len(piece) == count
                        transported = list(reversed(piece))
                        if column == 0:
                            for power, numerator in enumerate(transported):
                                old_power = degree-EPS[output]-power
                                assert old_power >= 0
                                expected = vector["values"][old_power][output]
                                assert numerator*vector["denominator"] == \
                                    expected*int(block["common_positive_denominator"])
                        transformed.extend(transported)
                        offset += count
                assert offset == len(raw) == len(transformed)
                self.store(name, {
                    "target": target, "field_component": component,
                    "source_tau_matrix_row_block": entry, "source_exact_candidate": candidate_spec,
                    "row_first": first, "row_stop": stop, "regular_degree_bound": degree,
                    "entry_order": "output_row, input_column, power=0..r+eps_column-eps_row",
                    "common_positive_denominator": block["common_positive_denominator"],
                    "coefficient_numerators": [str(value) for value in transformed],
                    "transition": "M_(F/sigma^r)(t)=t^r*D(t)*M_(F/tau^r)(1/t)*D(t)^-1",
                    "D": "diag(t^-eps_a); output rows left, input columns right",
                    "entry_exponent_from_original_k": "r+eps_input-eps_output-k",
                    "every_transition_exponent_nonnegative": True,
                    "transported_original_first_column_verified_coefficientwise": True,
                    "same_function_transition_omits_common_t_power": True,
                    "common_homogeneous_factor_in_pair": "t^"+str(degree),
                    "original_function_or_section_rescaled_by_unit": False,
                }, target)
                old = self.cached(name, target)
            assert old["source_tau_matrix_row_block"] == entry
            assert old["source_exact_candidate"] == candidate_spec
            assert old["regular_degree_bound"] == degree
            assert old["every_transition_exponent_nonnegative"] is True
            assert old["transported_original_first_column_verified_coefficientwise"] is True
            sigma_specs.append(spec(self.path(name)))
        current_receipt = self.imported_CRT_receipt(current)
        complete_name = stem+"-certified-multiplier-index"
        self.store(complete_name, {
            "target": target, "field_component": component,
            "source_original_vector": vector["source"], "regular_degree_bound": degree,
            "coefficient_field_basis": FIELD,
            "zero_component_proved_from_exact_original_vector": False,
            "source_candidate": candidate_spec,
            "matrix_row_blocks_tau": candidate["matrix_row_blocks"],
            "matrix_row_blocks_sigma": sigma_specs,
            "coefficient_storage": "each block gives common_positive_denominator and weighted flattened integer numerators",
            "weighted_entry_order": "output_row, input_column, power=0..r+eps_column-eps_row",
            "matrix_convention": "M_ba output row b input column a",
            "exact_first_column_certificate": first_spec,
            "weighted_degree_bound_verified": True,
            "original_first_column_verified_coefficientwise": True,
            "commutator_entry_degree_bound": "r+1+eps_input-eps_output",
            "commutator_maximum_degree": degree+3,
            "exact_commutator_points": exact_points,
            "exact_full_matrix_point_certificates": point_certificates,
            "complete_polynomial_commutator_identity_verified": True,
            "identity_certified_by_strict_degree_and_r_plus_4_distinct_exact_points": True,
            "primitive_cyclic_uniqueness_identifies_true_regular_multiplier": True,
            "source_R806_cyclic_witness": self.witness_spec,
            "sigma_regular_transition_preserves_original_section": True,
            "all_original_scalar_and_field_normalizations_preserved": True,
            "actual_CRT_prime_count": current["prime_count"],
            "projective_candidate_id": stem,
            "original_external_CRT_source": self.source_identity,
            "original_external_CRT_checkpoint": self.current_spec,
            "original_external_CRT_receipt": self.receipt_spec,
            "projective_search_supplies_no_height_or_uniqueness_claim": True,
            "actual_CRT_primes": current["consumed_primes"],
            "actual_CRT_modulus_bits": int(current["modulus"]).bit_length(),
            "latest_CRT_history_receipt": current_receipt,
            "no_characteristic_zero_Krylov_inverse_formed": True,
            "polar_ideal_or_original_function_DAG_computed": False,
        }, target)
        print(json.dumps({"stage": "certified_regular_multiplier_component", "target": target,
                          "field_component": component, "CRT_prime_count": current["prime_count"],
                          "commutator_degree_bound": degree+3, "exact_points": exact_points,
                          "seconds": time.monotonic()-self.started}), flush=True)
        return True, spec(self.path(complete_name))



    def try_denominator(self, denominator, source_kind, source_spec=None, probes=None, LLL_row=None):
        self.load_current()
        D = int(denominator)
        assert D > 0 and D % self.dg == 0 and math.gcd(D, self.modulus) == 1
        stem = self.projective_stem(D)
        rejected = self.cached(stem+"-rejected", "g")
        if rejected is not None:
            self.reject_projective_candidate(stem, rejected["reason"], rejected["additional"])
            return None
        complete_name = stem+"-certified-multiplier-index"
        accepted = self.cached(complete_name, "g")
        if accepted is not None:
            entry = spec(self.path(complete_name))
            self.validate_completed_component("g", 0, entry)
            return entry
        definition_name = stem+"-definition"
        definition = self.cached(definition_name, "g")
        if definition is None:
            actual_probes = probes or []
            outputs = [x["weighted_location"][0] for x in actual_probes]
            entries = [(0, outputs[0] if outputs else 0, 0),
                       (1, outputs[1] if len(outputs) > 1 else 1, 0),
                       (0, 0, 1)]
            entries = [list(x) for i, x in enumerate(entries) if x not in entries[:i]]
            self.store(definition_name, {
                "target": "g", "field_component": 0, "projective_candidate_id": stem,
                "D": str(D), "source_original_current": self.current_spec,
                "source_kind": source_kind, "source_candidate_generator": source_spec,
                "source_LLL_row": LLL_row, "probes": actual_probes,
                "early_exact_commutator_entries": entries,
                "D_is_positive_multiple_of_actual_reduced_dg_and_unit_mod_M": True,
                "only_known_first_column_uses_exact_unbounded_lift": True,
                "no_unknown_height_bound_is_asserted": True,
            }, "g")
            definition = self.cached(definition_name, "g")
        assert definition["D"] == str(D) and definition["source_original_current"] == self.current_spec
        definition_spec = spec(self.path(definition_name))
        passed, early = self.candidate_early_entries(D, stem, definition, definition_spec)
        if not passed:
            return None
        candidate, candidate_spec = self.construct_projective_candidate(D, stem, definition_spec, early)
        # The full current is an immutable source. Release its large residue list before exact
        # integer matrices; re-reading it for a later candidate is IO, never prime recomputation.
        current_header = {key: value for key, value in self.old_current.items() if key != "lifted_coefficients"}
        self.old_current = None
        gc.collect()
        accepted, answer = self.verify_projective_and_transport(current_header, candidate, candidate_spec)
        return answer if accepted else None

    def component(self, target, component):
        if target == "Gamma":
            return legacy.Job.component(self, target, component)
        assert target == "g" and component == 0
        self.load_w()
        selected_name = "R815-projective-selected-g-index"
        selected = self.cached(selected_name, "g")
        if selected is not None:
            assert selected["source_original_current"] == self.current_spec
            entry = selected["certified_multiplier_index"]
            self.validate_completed_component("g", 0, entry)
            self.audit_spec = selected["original_425_source_audit"]
            assert spec(self.path(self.audit_spec["file"])) == self.audit_spec
            return entry
        self.load_current()

        def accept(entry):
            self.validate_completed_component("g", 0, entry)
            self.store(selected_name, {
                "target": "g", "field_component": 0,
                "source_original_current": self.current_spec,
                "source_original_425_identity": self.source_identity,
                "original_425_source_audit": self.audit_spec,
                "certified_multiplier_index": entry,
                "original_first_column_and_all_seven_complete_exact_commutators_verified": True,
                "source_original_425_prime_arithmetic_recomputed": False,
                "new_own_configuration_preserves_external_source_identity": True,
            }, "g")
            self.old_current = None
            gc.collect()
            return entry

        entry = self.try_denominator(self.dg, "actual_known_first_column_denominator")
        if entry is not None:
            return accept(entry)
        controls = self.item.get("projective_controls", {})
        limit = int(controls.get("maximum_probe_pairs", 4))
        assert limit >= 1
        for number in range(limit):
            self.load_current()
            pair_answer = self.next_probe_pair(number)
            if pair_answer is None:
                state = self.probe_state()
                d = state["all_scalar_RR_denominator_if_no_failure"]
                if d is not None and state["scan_finished"]:
                    entry = self.try_denominator(math.lcm(self.dg, int(d)),
                                                 "actual_425_all_scalar_RR_denominator_lcm")
                    if entry is not None:
                        return accept(entry)
                self.search_stop = {
                    "candidate_search_exhausted": True, "probe_pair_limit_reached": False,
                    "actual_completed_probe_pairs": state["completed_pair_count"],
                    "all_original_coordinate_positions_scanned": state["scan_finished"],
                    "actual_scalar_RR_failure_count": state["scalar_RR_failure_count"],
                }
                raise SearchExhausted("All available actual probe pairs in this fixed finite strategy were consumed.")
            pair, pair_spec = pair_answer
            for shift in SHIFTS:
                self.load_current()
                lattice, lattice_spec = self.lattice_candidates(pair, pair_spec, shift)
                for candidate in lattice["candidates"]:
                    if candidate["search_rejection_reason"] is not None:
                        continue
                    entry = self.try_denominator(
                        int(candidate["D"]), "three_dimensional_integer_LLL_row",
                        lattice_spec, pair["probes"], candidate["LLL_row"])
                    if entry is not None:
                        return accept(entry)
        state = self.probe_state()
        self.search_stop = {
            "candidate_search_exhausted": False, "probe_pair_limit_reached": True,
            "actual_completed_probe_pairs": state["completed_pair_count"],
            "all_original_coordinate_positions_scanned": state["scan_finished"],
            "actual_scalar_RR_failure_count": state["scalar_RR_failure_count"],
        }
        raise SearchExhausted("The permitted probe-pair prefix was consumed without an exact Mg certificate.")

    def projective_manifest(self):
        complete_files, checkpoints = [], []
        for path in sorted(self.out.glob("R815-*.json.gz")):
            if path.name.startswith("R815-stage-manifest-"):
                continue
            entry = spec(path)
            if path.name.endswith("-current.json.gz"):
                checkpoints.append(entry)
            else:
                complete_files.append(entry)
        payload = {
            "files": complete_files, "current_checkpoints": checkpoints,
            "external_original_stages_stay_in_retained_R815_with_original_configuration": True,
            "rejected_candidate_pruning_history_preserved_in_completed_rejection_receipts": True,
        }
        name = "R815-stage-manifest-"+fingerprint(payload)[:24]
        old = self.cached(name)
        if old is None:
            self.store(name, payload)
        else:
            for key, value in payload.items():
                assert old[key] == value
        return spec(self.path(name))

    def write_search_stop(self, message):
        manifest_spec = self.projective_manifest()
        certificate = {
            "result": RESULT, "complete": False, "configuration": self.tag, "p": 41,
            "completed_scope": "projective_candidate_search_only",
            "requested_targets": list(TARGETS), "target_configurations": self.target_tags,
            "projective_mode": PROJECTIVE_MODE,
            "source_original_425_identity": self.source_identity,
            "source_original_current": self.current_spec, "source_original_latest_receipt": self.receipt_spec,
            "original_425_source_audit": getattr(self, "audit_spec", None),
            "search_stop": self.search_stop,
            "error": message,
            "original_Mg_computed": False,
            "original_normal_derivation_connection_computed": False,
            "all_complete_polynomial_defining_identities_verified": False,
            "candidate_failure_proves_original_matrix_nonexistence_or_insufficient_CRT": False,
            "old_425_prime_arithmetic_recomputed": False,
            "independent_Mh_reconstructed_or_stored": False,
            "original_function_DAG_polar_divisors_eta_or_height_computed": False,
            "stage_manifest": manifest_spec, "seconds": time.monotonic()-self.started,
        }
        save(self.out/FINAL, certificate)
        save(self.out/"core-receipt.json", {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "legacy_R815_core_sha256": sha(legacy.__file__),
            "framework_sha256": sha(framework.__file__),
            "projective_mode": PROJECTIVE_MODE,
            "certificate_sha256": sha(self.out/FINAL),
            "error": message, "search_stop": self.search_stop,
            "source_original_425_prime_arithmetic_recomputed": False,
            "original_Mg_computed": False, "original_normal_derivation_connection_computed": False,
            "completed_source_bound_stages_and_current_CRT_preserved": True,
        })
        print(json.dumps({"stage": "projective_search_stopped", **self.search_stop,
                          "seconds": time.monotonic()-self.started}), flush=True)
        return 2

    def run(self):
        final = self.out/FINAL
        if final.exists():
            prior = read(final)
            assert prior["result"] == RESULT and prior["configuration"] == self.tag
            assert prior["target_configurations"] == self.target_tags
            if prior["complete"]:
                assert prior["completed_scope"] == SCOPE
                manifest_spec = prior["stage_manifest"]
                assert spec(self.path(manifest_spec["file"])) == manifest_spec
                manifest = self.cached(manifest_spec["file"])
                for entry in manifest["files"]+manifest.get("current_checkpoints", []):
                    assert spec(self.path(entry["file"])) == entry
            # An old search-only FINAL is a historical receipt. Its probe-current may
            # have advanced in a later interrupted run; the current atomic stages win.
        self.load_w()
        # The h vector is input only. No independent Mh matrix or CRT state is constructed.
        self.target_component("h", 0)
        for target in TARGETS:
            self.operator_indices[target] = self.component(target, 0)
            self.validate_completed_component(target, 0, self.operator_indices[target])
        assert not list(self.out.glob("R815-*-CRT-current.json.gz"))
        assert not list(self.out.glob("R815-target-h-*-CRT-*.json.gz"))
        manifest_spec = self.projective_manifest()
        indexes = {target: self.cached(entry["file"], target)
                   for target, entry in self.operator_indices.items()}
        certificate = {
            "result": RESULT, "complete": True, "configuration": self.tag, "p": 41,
            "completed_scope": SCOPE, "requested_targets": list(TARGETS),
            "target_configurations": self.target_tags,
            "normal_affine_basis_rank": FREE, "normal_basis_degrees": EPS,
            "coefficient_field_basis": FIELD,
            "actual_sigma_integer_n": self.r806.tag["actual_sigma_integer_n"],
            "projective_mode": PROJECTIVE_MODE,
            "projective_method_sha256": self.tag["projective_method_sha256"],
            "legacy_R815_core_sha256": LEGACY_SHA,
            "source_original_425_identity": self.source_identity,
            "source_original_current": self.current_spec,
            "source_original_latest_receipt": self.receipt_spec,
            "original_425_source_audit": self.audit_spec,
            "original_425_prime_arithmetic_recomputed": False,
            "original_vector_input_source_group": "R815",
            "external_old_W_and_Krylov_stages_preserve_original_configuration": True,
            "projective_probe_scan_is_not_an_unfinished_operator": True,
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
            "legacy_R815_core_sha256": sha(legacy.__file__),
            "projective_mode": PROJECTIVE_MODE,
            "source_original_425_prime_arithmetic_recomputed": False,
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
    for name in ("config", "proof", "nested-proof", "method", "projective-method", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    job = None
    try:
        job = Job(args)
        return job.run()
    except SearchExhausted as error:
        assert job is not None
        return job.write_search_stop(str(error))
    except BaseException as error:
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "legacy_R815_core_sha256": sha(legacy.__file__),
            "framework_sha256": sha(framework.__file__),
            "projective_mode": PROJECTIVE_MODE,
            "error": type(error).__name__+": "+str(error),
            "completed_source_bound_stages_and_current_CRT_preserved": True,
            "source_original_425_prime_arithmetic_recomputed": False,
            "original_Mg_computed": bool(job and "g" in job.operator_indices),
            "original_normal_derivation_connection_computed": False,
            "independent_Mh_reconstructed_or_stored": False,
            "original_function_DAG_polar_divisors_eta_or_height_computed": False,
        })
        raise


if __name__ == "__main__":
    sys.exit(main())
