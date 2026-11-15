#!/usr/bin/env python3
"""Independent R815 consumer: eight simultaneous probes and one complete 9D lattice.
Completed original three columns, scalar failures and identical-candidate rejections
are immutable inputs. All new mathematical arithmetic belongs to public Actions.
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
from flint import fmpz_mat
import R815_three_known_columns_reconstruction as three
import R815_original_normal_derivation_operators as legacy
import R811_original_regular_multipliers as framework
from R815_three_known_columns_reconstruction import (
    RESULT, FINAL, SCOPE, FREE, S3, EPS, TARGETS, INPUT_LABELS, FIELD,
    R806_CORE_SHA, R813_CORE_SHA, FRAMEWORK_SHA, guard, LEGACY_SHA,
    KNOWN_COLUMNS, KNOWN_COLUMN_SLOT, POINT_NAME, ORIGINAL_SCALARS, SOURCE_KEYS,
    checkpoint_identity, centered, SearchExhausted,
    Retained, BudgetStop, sha, read, save, spec, plain, fingerprint,
    producer_identity, same_producer, rows, S3_position,
)

THREE_SHA = "515e15557ea3681055178f5da742d5c4fcee9d5d6a313e5c5892124872a72f83"
THREE_METHOD_SHA = "6d12fe13d77ba1f8d970cc697faf229027d812f7b7a067590bd6a3946426f6d4"
THREE_TAG_SHA = "e9bdaaad21dad23d7180383deee207bc279639a8d157029b98ef5fa2236e2c37"
PROJECTIVE_MODE = "three-known-columns-and-eight-simultaneous-probes-in-nine-dimensional-lattice"
PROBE_INDICES = (10, 11, 12, 13, 15, 17, 20, 24)
SEARCH_STRATEGY = {
    "probe_indices": list(PROBE_INDICES),
    "probe_source": "four completed original three-column pairs; no new scalar RR or scan",
    "known_columns": [0, 1, 271],
    "known_denominator": "completed jointly reduced d012, not the full operator denominator",
    "integer_row_lattice": "first row [d012,center(d012*r_i) for eight probes]; remaining rows diag M",
    "dimension": 9, "column_weights": [1]*9, "number_of_new_LLL_calls": 1,
    "LLL_parameters": {"delta": "0.99", "eta": "0.51"},
    "LLL_certificate": "all nine returned rows; integer U*H=R and det U=+1 or -1",
    "candidate_rows": "all nine original rows; positive D, d012 divides D, gcd(D,M)=1",
    "candidate_matrix": "exact D/d012 times completed columns0/1/271; all other coefficients=center(D*r)",
    "duplicate_policy": "same integer D and same original current, known columns, W, weighted order and frozen candidate code",
    "old_rejections": "source-bound exact nonzero required commutator entry; never rerun identical candidate",
    "success_exit": "original three columns, weighted support, full exact seven-point commutator, then frozen Gamma",
    "height_or_reconstruction_rectangle": None,
}


def completed_source_identity(source):
    answer = {key: str(source[key]) for key in SOURCE_KEYS}
    assert answer["result"] == RESULT and answer["core_sha256"] == THREE_SHA
    assert answer["run_id"] == "43762388370"
    assert answer["source_commit"] == "ca1fe0d562497055f9e5441edc17ac588a25229c"
    assert answer["manifest_sha256"] == "0f2be930adc35c414f8f7f69c7dfd2ada3b0b5fe076d66f7c08583d416cd1718"
    answer["configuration_sha256"] = source["configuration_sha256"]
    assert answer["configuration_sha256"] == THREE_TAG_SHA
    for key in ("certificate", "stage_manifest", "known_columns", "scan", "source_audit",
                "input_bundle", "previous_scan_input_bundle"):
        answer[key] = plain(source[key])
    answer["probe_pairs"] = [plain(value) for value in source["probe_pairs"]]
    assert len(answer["probe_pairs"]) == 4
    return answer


class Job(three.Job):
    def __init__(self, args):
        self.args, self.out, self.started = args, args.output, time.monotonic()
        self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        assert self.item["producer_inputs_pending"] is False
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert self.item["core_sha256"] == sha(__file__)
        assert sha(legacy.__file__) == self.item["legacy_core_sha256"] == LEGACY_SHA
        assert sha(args.projective_method) == self.item["projective_method_sha256"]
        assert sha(three.__file__) == self.item["three_column_core_sha256"] == THREE_SHA
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
        self.previous_source = self.item["previous_projective_scan"]
        assert self.previous_source["core_sha256"] == "0008796890a0cfcf0b9aaaa40e26f0d8d26be38f8168c8fe918d86a7585a0ec1"
        self.previous_scan_identity = {
            **{key: str(self.previous_source[key]) for key in SOURCE_KEYS},
            "configuration_sha256": self.previous_source["configuration_sha256"],
            "scan": plain(self.previous_source["scan"]),
            "probe_pairs": [plain(x) for x in self.previous_source["probe_pairs"]],
            "source_audit": plain(self.previous_source["source_audit"]),
            "certificate": plain(self.previous_source["certificate"]),
            "known_columns": plain(self.previous_source["known_columns"]),
            "imported_scalar_scan": plain(self.previous_source["imported_scalar_scan"]),
        }
        self.previous_prefix = None
        self.tag.update({
            "projective_mode": three.PROJECTIVE_MODE,
            "projective_method_sha256": THREE_METHOD_SHA,
            "legacy_R815_core_sha256": sha(legacy.__file__),
            "projective_source_identity": self.source_identity,
            "source_original_425_configuration_sha256": fingerprint(self.old_tag),
            "source_original_425_current": self.current_spec,
            "source_original_425_receipt": self.receipt_spec,
            "projective_search_strategy": three.SEARCH_STRATEGY,
            "original_425_Mg_prime_arithmetic_recomputed": False,
            "previous_projective_scalar_scan_source": self.previous_scan_identity,
            "three_exact_original_columns_identity": "Mg e0=vg; We0=e1; We1=e271; Mg e1=Wvg; Mg e271=W(Wvg)",
            "only_budget_and_probe_pair_limit_excluded_from_mathematical_identity": True,
        })
        self.tag["source_sha256"] = THREE_SHA
        self.three_tag = dict(self.tag)
        assert fingerprint(self.three_tag) == THREE_TAG_SHA
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
        self.three_target_tags = {key: dict(value) for key, value in self.target_tags.items()}
        self.completed_source = self.item["completed_three_columns_source"]
        self.completed_identity = completed_source_identity(self.completed_source)
        self.tag = dict(self.three_tag,
            source_sha256=sha(__file__), projective_mode=PROJECTIVE_MODE,
            projective_method_sha256=sha(args.projective_method),
            projective_search_strategy=SEARCH_STRATEGY,
            frozen_three_column_core_sha256=THREE_SHA,
            completed_three_columns_source_identity=self.completed_identity,
            source_three_column_configuration_sha256=THREE_TAG_SHA,
            old_49_candidate_rejections_reused_only_for_identical_D_M_and_known_columns=True,
            old_three_dimensional_LLL_and_scalar_RR_recomputed=False,
            only_runtime_budget_excluded_from_mathematical_identity=True)
        self.tag.pop("only_budget_and_probe_pair_limit_excluded_from_mathematical_identity")
        self.target_tags = {
            key: dict(value, basis_configuration_sha256=fingerprint(self.tag))
            for key, value in self.three_target_tags.items()}
        self.completed_loaded = False
        self.old_rejections = {}
        self.fixed_probes = []

    def completed_raw(self, name):
        assert Path(name).name == name
        entry = plain(self.completed_source["files"][name])
        path = self.args.previous_three_columns/name
        assert spec(path) == entry
        return read(path)

    def completed_stage(self, entry, target=None, current=False):
        entry = plain(entry)
        assert entry == self.completed_index[entry["file"]]
        assert entry == plain(self.completed_source["files"][entry["file"]])
        value = self.completed_raw(entry["file"])
        assert value["configuration"] == self.three_tag
        assert value["complete"] is (not current)
        if target is None:
            assert "target_configuration" not in value
        else:
            assert value["target_configuration"] == self.three_target_tags[target]
            assert value["target_configuration_sha256"] == fingerprint(self.three_target_tags[target])
        return value

    def load_completed_source(self):
        if self.completed_loaded:
            return
        source = self.completed_source
        manifest = self.completed_raw("full-outputs-manifest.json")
        assert manifest["result"] == RESULT
        assert plain(source["files"]["full-outputs-manifest.json"])["sha256"] == source["manifest_sha256"]
        by_name = {entry["file"]: plain(entry) for entry in manifest["files"]}
        assert len(by_name) == len(manifest["files"]) == 198
        assert len(source["files"]) == 198
        for name, entry in source["files"].items():
            if name not in ("full-outputs-manifest.json", "full-outputs-manifest-reference.json"):
                assert plain(entry) == by_name[name]
        reference = self.completed_raw("full-outputs-manifest-reference.json")
        assert reference["result"] == RESULT and reference["file_count"] == 198
        assert reference["manifest_file"] == "full-outputs-manifest.json"
        assert reference["manifest_sha256"] == source["manifest_sha256"]
        assert reference["manifest_bytes"] == source["files"]["full-outputs-manifest.json"]["bytes"]
        for key in ("input_bundle", "previous_scan_input_bundle"):
            assert plain(source[key]) == by_name[source[key]["file"]]
            assert source[key]["file"] not in source["files"]
        initial = self.completed_raw("public-actions-input.json")
        run = self.completed_raw("run-receipt.json")
        core = self.completed_raw("core-receipt.json")
        final = self.completed_raw(source["certificate"]["file"])
        assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
        assert str(run["workflow_run_id"]) == str(source["run_id"])
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == core["source_sha256"] == THREE_SHA
        assert initial["driver_sha256"] == source["wrapper_sha256"]
        assert run["complete"] is core["complete"] is final["complete"] is False
        assert run["process_exit_code"] == 2 and run["error"] is None
        assert run["core_receipt_sha256"] == source["files"]["core-receipt.json"]["sha256"]
        assert core["certificate_sha256"] == source["certificate"]["sha256"]
        assert initial["actual_projective_configuration"] == final["configuration"] == self.three_tag
        assert final["target_configurations"] == self.three_target_tags
        assert final["projective_mode"] == three.PROJECTIVE_MODE
        assert final["source_original_current"] == self.current_spec
        assert final["source_original_latest_receipt"] == self.receipt_spec
        assert final["stage_manifest"] == plain(source["stage_manifest"])
        assert final["exact_three_known_columns_input"] == plain(source["known_columns"])
        inventory = self.completed_raw(source["stage_manifest"]["file"])
        assert inventory["configuration"] == self.three_tag and inventory["complete"] is True
        entries = inventory["files"]+inventory.get("current_checkpoints", [])
        self.completed_index = {value["file"]: plain(value) for value in entries}
        assert len(self.completed_index) == len(entries)
        for name, entry in self.completed_index.items():
            assert entry == by_name[name] == plain(source["files"][name])
        audit = self.completed_stage(source["source_audit"])
        assert final["original_425_source_audit"] == plain(source["source_audit"])
        assert audit["source_original_current"] == self.current_spec
        assert audit["source_original_latest_receipt"] == self.receipt_spec
        assert audit["source_original_configuration_sha256"] == fingerprint(self.old_tag)
        assert audit["source_original_W_integer_polynomial"] == self.w_input_spec
        assert audit["source_original_g_vector"] == self.target_component("g", 0)["source"]
        assert audit["all690_original_first_column_CRT_congruences_verified"] is True
        assert audit["source_original_425_prime_arithmetic_recomputed"] is False
        self.completed_audit = audit
        known = self.completed_stage(source["known_columns"], "g")
        assert known["source_original_current"] == self.current_spec
        assert known["source_original_M_w"] == self.w_input_spec
        assert known["source_original_g_vector"] == self.target_component("g", 0)["source"]
        assert known["known_column_indices"] == list(KNOWN_COLUMNS)
        assert known["known_column_coefficient_counts"] == [690, 962, 1234]
        assert known["known_column_total_coefficient_count"] == 2886
        assert known["normal_affine_basis_rank"] == FREE and known["normal_affine_basis_degrees"] == EPS
        for key in ("original_We0_equals_e1_and_We1_equals_e271_verified_coefficientwise",
                    "all_three_weighted_supports_verified_coefficientwise",
                    "raw_third_column_powers6_and7_verified_zero",
                    "common_denominator_is_positive_and_jointly_reduced",
                    "all2886_original_current_congruences_verified",
                    "new_exact_W_times_completed_second_column_actually_performed",
                    "all_original_scalar_and_field_normalizations_preserved"):
            assert known[key] is True
        assert known["original_completed_Wvg_recomputed"] is False
        assert known["original_g_reduced_denominator"] == str(self.dg)
        assert known["original_W_common_positive_denominator"] == str(self.w_denominator)
        self.known_columns_spec = plain(source["known_columns"])
        self.d012 = int(known["common_positive_denominator"])
        assert self.d012 > 0 and math.gcd(self.d012, self.modulus) == 1
        self.known_columns = [[[int(value) for value in polynomial] for polynomial in column]
                              for column in known["column_integer_numerators"]]
        assert len(self.known_columns) == 3
        assert all(len(column) == 6 and all(len(line) == FREE for line in column)
                   for column in self.known_columns)
        scan = self.completed_stage(source["scan"], current=True)
        assert scan["source_original_current"] == self.current_spec
        assert scan["next_coefficient_index"] == 25 and scan["completed_pair_count"] == 4
        assert scan["scalar_RR_failure_count"] == 8
        assert scan["scan_finished"] is False and scan["unpaired_failure"] is None
        probes = []
        for number, pair_spec in enumerate(source["probe_pairs"]):
            pair = self.completed_stage(pair_spec)
            assert pair["source_original_current"] == self.current_spec
            assert pair["pair_number"] == number and len(pair["probes"]) == 2
            assert pair["fallback_after_exhausting_actual_coordinate_order"] is False
            assert pair["resume_after_pair"]["completed_pair_count"] == number+1
            assert pair["resume_after_pair"]["scalar_RR_failure_count"] == 2*(number+1)
            probes.extend(pair["probes"])
        assert tuple(entry["coefficient_index"] for entry in probes) == PROBE_INDICES
        for probe in probes:
            index = probe["coefficient_index"]
            assert list(self.location(index)) == probe["weighted_location"]
            assert self.location(index)[1] not in KNOWN_COLUMNS
            assert probe["residue_mod_original_M"] == str(self.residue(index))
        self.fixed_probes = probes
        old_rejections = {}
        for name, entry in sorted(self.completed_index.items()):
            if not (name.startswith("R815-projective-g-candidate-") and name.endswith("-definition.json.gz")):
                continue
            definition = self.completed_stage(entry, "g")
            D = int(definition["D"])
            stem = three.Job.projective_stem(self, D)
            assert name == stem+"-definition.json.gz"
            assert D > 0 and D % self.d012 == 0 and math.gcd(D, self.modulus) == 1
            assert definition["source_original_current"] == self.current_spec
            assert definition["source_exact_three_known_columns"] == self.known_columns_spec
            assert definition["projective_candidate_id"] == stem
            assert definition["D_is_positive_multiple_of_actual_reduced_d012_and_unit_mod_M"] is True
            assert definition["all_three_known_columns_use_exact_unbounded_lift"] is True
            reject_spec = self.completed_index[stem+"-rejected.json.gz"]
            reject = self.completed_stage(reject_spec, "g")
            assert reject["candidate_id"] == stem and reject["source_original_current"] == self.current_spec
            assert reject["additional"]["source_candidate_definition"] == entry
            early_spec = plain(reject["additional"]["failed_exact_entry"])
            early = self.completed_stage(early_spec, "g")
            assert early["source_candidate_definition"] == entry
            assert early["source_original_M_w"] == self.w_input_spec
            assert early["candidate_denominator_before_block_content_reduction"] == str(D)
            assert early["original_W_common_positive_denominator"] == str(self.w_denominator)
            assert early["zero"] is False and int(early["exact_integer_commutator_residual"]) != 0
            point = [early["exact_integer_point"], early["output_row"], early["input_column"]]
            assert point in definition["early_exact_commutator_entries"]
            assert point == [0, 0, 2]
            assert early["entry_is_part_of_the_required_full_seven_point_identity"] is True
            assert reject["no_exact_characteristic_zero_multiplier_claimed"] is True
            assert reject["discarded_candidate_file_history"] == []
            assert str(D) not in old_rejections
            old_rejections[str(D)] = {
                "candidate_id": stem, "D": str(D), "definition": entry,
                "failed_exact_entry": early_spec, "rejection": reject_spec,
                "failed_required_entry": point}
        assert len(old_rejections) == 49 and str(self.d012) in old_rejections
        self.old_rejections = old_rejections
        self.completed_loaded = True

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
        assert len(primes) == len(indices) == len(set(primes)) == 425
        assert indices == sorted(set(indices))
        assert all(self.prime_at(i) == p for i, p in zip(indices, primes))
        assert primes[-1] == self.old_receipt["latest_prime"] == 1000008791
        modulus = int(data["modulus"])
        assert modulus == math.prod(primes) and modulus.bit_length() == 12707
        assert len(data["lifted_coefficients"]) == self.total_coefficients
        assert data["previous_checkpoint_sha256"] == self.old_receipt["previous_checkpoint_sha256"]
        assert data["previous_CRT_receipt"] == self.old_receipt["previous_CRT_receipt"]
        self.old_current, self.modulus = data, modulus
        self.dg = self.target_component("g", 0)["denominator"]
        self.load_completed_source()
        assert self.completed_audit["actual_reduced_g_first_column_denominator"] == str(self.dg)
        name = "R815-eight-probe-completed-source-audit"
        old = self.cached(name)
        payload = {
            "source_original_425_identity": self.source_identity,
            "source_original_current": self.current_spec,
            "source_original_latest_receipt": self.receipt_spec,
            "completed_three_columns_source": self.completed_identity,
            "source_exact_three_known_columns": self.known_columns_spec,
            "known_columns_source_group": "completed_three_columns_source",
            "source_original_M_w": self.w_input_spec,
            "source_original_g_vector": self.target_component("g", 0)["source"],
            "all2886_congruences_imported_from_complete_source_not_recomputed": True,
            "known_columns_and_joint_content_not_recomputed": True,
            "fixed_actual_failure_indices": list(PROBE_INDICES),
            "source_probe_pairs": self.completed_identity["probe_pairs"],
            "original_scalar_RR_and_old_three_dimensional_LLL_recomputed": False,
            "source_modulus_bits": 12707,
            "source_exact_known_denominator": str(self.d012),
            "original_49_rejections": list(self.old_rejections.values()),
            "actual_distinct_old_rejections": 49,
            "original_425_prime_arithmetic_recomputed": False,
        }
        if old is None:
            self.store(name, payload)
        else:
            for key, value in payload.items():
                assert old[key] == value
        self.audit_spec = spec(self.path(name))

    def nine_dimensional_lattice(self):
        raw_name = "R815-eight-probe-nine-dimensional-raw-LLL"
        final_name = "R815-eight-probe-nine-dimensional-certified-LLL"
        final = self.cached(final_name)
        if final is not None:
            assert final["source_completed_source_audit"] == self.audit_spec
            assert final["source_exact_three_known_columns"] == self.known_columns_spec
            assert final["probe_indices"] == list(PROBE_INDICES)
            assert final["full_basis_change_equality_verified"] is True
            assert len(final["candidates"]) == 9
            raw_spec = final["source_raw_LLL"]
            assert spec(self.path(raw_spec["file"])) == raw_spec
            return final, spec(self.path(final_name))
        raw = self.cached(raw_name)
        if raw is None:
            self.budget()
            residuals = [int(entry["residue_mod_original_M"]) for entry in self.fixed_probes]
            centered_known = [centered(self.d012*r, self.modulus) for r in residuals]
            matrix = [[self.d012]+centered_known]
            matrix += [[0]+[self.modulus if row == column else 0 for column in range(8)]
                       for row in range(8)]
            original = fmpz_mat(matrix)
            reduced = original.lll(delta=0.99, eta=0.51)
            # Save immediately after LLL returns, before any later budget check.
            self.store(raw_name, {
                "source_completed_source_audit": self.audit_spec,
                "source_original_current": self.current_spec,
                "source_exact_three_known_columns": self.known_columns_spec,
                "source_probe_pairs": self.completed_identity["probe_pairs"],
                "probe_indices": list(PROBE_INDICES), "dimension": 9,
                "actual_integer_lattice_rows": rows(original, strings=True),
                "actual_returned_LLL_rows": rows(reduced, strings=True),
                "LLL_parameters": {"delta": "0.99", "eta": "0.51"},
                "column_weights": [1]*9,
                "number_of_new_LLL_calls": 1,
                "returned_rows_saved_before_full_basis_certification": True,
                "complete_basis_or_multiplier_claimed_by_this_raw_stage": False,
            })
            raw = self.cached(raw_name)
        self.budget()
        assert raw["source_completed_source_audit"] == self.audit_spec
        assert raw["source_original_current"] == self.current_spec
        assert raw["source_exact_three_known_columns"] == self.known_columns_spec
        assert raw["probe_indices"] == list(PROBE_INDICES)
        matrix = [[int(value) for value in line] for line in raw["actual_integer_lattice_rows"]]
        reduced_rows = [[int(value) for value in line] for line in raw["actual_returned_LLL_rows"]]
        assert len(matrix) == len(reduced_rows) == 9
        assert all(len(line) == 9 for line in matrix+reduced_rows)
        residuals = [int(entry["residue_mod_original_M"]) for entry in self.fixed_probes]
        centers = [centered(self.d012*r, self.modulus) for r in residuals]
        assert matrix[0] == [self.d012]+centers
        for row in range(8):
            assert matrix[row+1] == [0]+[self.modulus if row == column else 0 for column in range(8)]
        transformations, candidates = [], []
        for row, values in enumerate(reduced_rows):
            assert values[0] % self.d012 == 0
            a = values[0]//self.d012
            numerators = [values[j+1]-a*centers[j] for j in range(8)]
            assert all(value % self.modulus == 0 for value in numerators)
            transformations.append([a]+[value//self.modulus for value in numerators])
            sign = 1 if values[0] >= 0 else -1
            D = sign*values[0]
            n = [sign*value for value in values[1:]]
            assert all((value-D*r) % self.modulus == 0 for value, r in zip(n, residuals))
            reason = ("zero_denominator" if D == 0 else
                      "denominator_not_a_unit_at_original_CRT" if math.gcd(D, self.modulus) != 1 else None)
            candidates.append({
                "LLL_row": row, "row_sign": sign, "D": str(D),
                "probe_numerators": [str(value) for value in n],
                "original_eight_congruences_verified": True,
                "denominator_is_multiple_of_actual_d012": D % self.d012 == 0,
                "search_rejection_reason": reason,
                "same_D_in_completed_49_rejections": str(D) in self.old_rejections,
                "height_or_reconstruction_rectangle_used": False,
            })
        U, H, R = fmpz_mat(transformations), fmpz_mat(matrix), fmpz_mat(reduced_rows)
        determinant = int(U.det())
        assert abs(determinant) == 1 and U*H == R
        self.store(final_name, {
            "source_completed_source_audit": self.audit_spec,
            "source_original_current": self.current_spec,
            "source_exact_three_known_columns": self.known_columns_spec,
            "source_probe_pairs": self.completed_identity["probe_pairs"],
            "source_raw_LLL": spec(self.path(raw_name)),
            "dimension": 9, "probe_indices": list(PROBE_INDICES),
            "actual_integer_lattice_rows": raw["actual_integer_lattice_rows"],
            "actual_LLL_rows": raw["actual_returned_LLL_rows"],
            "exact_integral_basis_change": rows(U, strings=True),
            "exact_basis_change_determinant": determinant,
            "full_basis_change_equality_verified": True,
            "original_lattice_determinant": str(self.d012*self.modulus**8),
            "full_congruence_lattice_not_a_sublattice": True,
            "candidates": candidates,
            "number_of_new_LLL_calls": 1,
            "any_candidate_or_height_guarantee_claimed": False,
        })
        return self.cached(final_name), spec(self.path(final_name))

    def reuse_previous_rejection(self, D):
        old = self.old_rejections[str(D)]
        stem = three.Job.projective_stem(self, D)
        name = "R815-eight-probe-"+stem[len("R815-projective-"):]+"-previous-rejection"
        payload = {
            "target": "g", "field_component": 0, "candidate_id": stem, "D": str(D),
            "source_original_current": self.current_spec,
            "source_exact_three_known_columns": self.known_columns_spec,
            "source_original_M_w": self.w_input_spec,
            "completed_three_columns_source": self.completed_identity,
            "source_previous_definition": old["definition"],
            "source_previous_failed_exact_entry": old["failed_exact_entry"],
            "source_previous_rejection": old["rejection"],
            "source_failed_required_entry": old["failed_required_entry"],
            "same_integer_denominator_and_same_complete_candidate": True,
            "frozen_candidate_constructor_sha256": THREE_SHA,
            "old_nonzero_residual_recomputed": False,
            "old_source_relabelled": False,
            "candidate_strictly_rejected_by_original_exact_equation": True,
        }
        data = self.cached(name, "g")
        if data is None:
            self.store(name, payload, "g")
        else:
            for key, value in payload.items():
                assert data[key] == value
        return spec(self.path(name))

    def component(self, target, component):
        if target == "Gamma":
            return legacy.Job.component(self, target, component)
        assert target == "g" and component == 0
        self.load_w()
        self.load_current()
        selected_name = "R815-eight-probe-selected-g-index"
        selected = self.cached(selected_name, "g")
        if selected is not None:
            assert selected["source_original_current"] == self.current_spec
            assert selected["exact_three_known_columns"] == self.known_columns_spec
            entry = selected["certified_multiplier_index"]
            self.validate_completed_component("g", 0, entry)
            self.lattice_spec = selected["complete_nine_dimensional_lattice"]
            assert spec(self.path(self.lattice_spec["file"])) == self.lattice_spec
            self.baseline_rejection_spec = selected["baseline_previous_rejection"]
            assert spec(self.path(self.baseline_rejection_spec["file"])) == self.baseline_rejection_spec
            self.resume_spec = spec(self.path("R815-eight-probe-candidate-search-current"))
            resumed = self.cached(self.resume_spec["file"], current=True)
            assert resumed["accepted_multiplier_index"] == entry
            self.old_current = None
            gc.collect()
            return entry
        self.baseline_rejection_spec = self.reuse_previous_rejection(self.d012)
        lattice, self.lattice_spec = self.nine_dimensional_lattice()
        state_name = "R815-eight-probe-candidate-search-current"
        state = self.cached(state_name, current=True)
        if state is None:
            state = {
                "source_original_current": self.current_spec,
                "complete_nine_dimensional_lattice": self.lattice_spec,
                "baseline_previous_rejection": self.baseline_rejection_spec,
                "next_LLL_row": 0, "row_decisions": [], "accepted_multiplier_index": None,
                "fixed_schedule_exhausted": False,
            }
            self.store(state_name, state, current=True)
            state = self.cached(state_name, current=True)
        assert state["complete_nine_dimensional_lattice"] == self.lattice_spec
        assert state["source_original_current"] == self.current_spec
        assert state["baseline_previous_rejection"] == self.baseline_rejection_spec
        assert 0 <= state["next_LLL_row"] <= 9
        assert len(state["row_decisions"]) == state["next_LLL_row"]
        self.resume_spec = spec(self.path(state_name))
        decisions = []
        distinct = {}
        for ordinal, entry in enumerate(state["row_decisions"]):
            assert spec(self.path(entry["file"])) == entry
            decision = self.cached(entry["file"])
            assert decision["LLL_row"] == ordinal
            assert decision["source_complete_lattice"] == self.lattice_spec
            assert decision["D"] == lattice["candidates"][ordinal]["D"]
            decisions.append((decision, entry))
            if decision["search_rejection_reason"] is None:
                distinct.setdefault(decision["D"], entry)

        def accept(entry, decision_spec):
            self.validate_completed_component("g", 0, entry)
            self.store(selected_name, {
                "target": "g", "field_component": 0,
                "source_original_current": self.current_spec,
                "original_425_source_audit": self.audit_spec,
                "exact_three_known_columns": self.known_columns_spec,
                "exact_three_known_columns_source_group": "completed_three_columns_source",
                "complete_nine_dimensional_lattice": self.lattice_spec,
                "baseline_previous_rejection": self.baseline_rejection_spec,
                "accepted_row_decision": decision_spec,
                "certified_multiplier_index": entry,
                "original_first_column_and_all_seven_complete_exact_commutators_verified": True,
                "source_original_425_prime_arithmetic_recomputed": False,
            }, "g")
            self.old_current = None
            gc.collect()
            return entry

        if state["accepted_multiplier_index"] is not None:
            return accept(state["accepted_multiplier_index"], state["row_decisions"][-1])
        for ordinal in range(state["next_LLL_row"], 9):
            self.budget()
            candidate = lattice["candidates"][ordinal]
            D = int(candidate["D"])
            name = "R815-eight-probe-row-"+str(ordinal).zfill(2)+"-decision"
            decision = self.cached(name)
            if decision is None:
                certified = None
                reason = candidate["search_rejection_reason"]
                if reason is not None:
                    outcome, witness = "search_filter", None
                elif str(D) in distinct:
                    outcome, witness = "duplicate_in_new_nine_rows", distinct[str(D)]
                elif str(D) in self.old_rejections:
                    outcome, witness = "same_completed_candidate_rejected", self.reuse_previous_rejection(D)
                else:
                    self.load_current()
                    certified = three.Job.try_denominator(
                        self, D, "complete_nine_dimensional_integer_LLL_row",
                        self.lattice_spec, self.fixed_probes, ordinal)
                    if certified is None:
                        outcome = "new_exact_candidate_rejected"
                        witness = spec(self.path(self.projective_stem(D)+"-rejected"))
                        assert self.cached(witness["file"], "g") is not None
                    else:
                        outcome, witness = "original_multiplier_certified", certified
                self.store(name, {
                    "source_complete_lattice": self.lattice_spec,
                    "LLL_row": ordinal, "D": str(D), "row_sign": candidate["row_sign"],
                    "search_rejection_reason": reason, "outcome": outcome,
                    "witness": witness, "certified_multiplier_index": certified,
                    "new_scalar_RR_or_old_LLL_performed": False,
                })
                decision = self.cached(name)
            assert decision["source_complete_lattice"] == self.lattice_spec
            assert decision["LLL_row"] == ordinal and decision["D"] == str(D)
            entry = spec(self.path(name))
            if candidate["search_rejection_reason"] is None:
                distinct.setdefault(str(D), entry)
            state["row_decisions"].append(entry)
            state["next_LLL_row"] = ordinal+1
            state["fixed_schedule_exhausted"] = ordinal == 8
            state["accepted_multiplier_index"] = decision["certified_multiplier_index"]
            self.store(state_name, state, current=True, replace=True)
            decisions.append((decision, entry))
            self.resume_spec = spec(self.path(state_name))
            if decision["certified_multiplier_index"] is not None:
                return accept(decision["certified_multiplier_index"], entry)
        self.resume_spec = spec(self.path(state_name))
        counts = {}
        for decision, _ in decisions:
            counts[decision["outcome"]] = counts.get(decision["outcome"], 0)+1
        self.search_stop = {
            "candidate_search_exhausted": True,
            "fixed_nine_row_schedule_exhausted": True,
            "probe_pair_limit_reached": False,
            "actual_new_LLL_lattices": 1, "actual_LLL_rows": 9,
            "actual_processed_LLL_rows": state["next_LLL_row"],
            "actual_distinct_admissible_new_lattice_denominators": len(distinct),
            "row_outcome_counts": counts,
            "baseline_old_rejection_reused_without_arithmetic": True,
            "new_scalar_RR_or_425_prime_arithmetic_performed": False,
        }
        raise SearchExhausted("The one complete nine-dimensional lattice and all nine rows were consumed without an exact Mg certificate.")

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
            "completed_scope": "eight_probe_lattice_and_candidate_search_only",
            "requested_targets": list(TARGETS), "target_configurations": self.target_tags,
            "projective_mode": PROJECTIVE_MODE,
            "source_original_425_identity": self.source_identity,
            "source_original_current": self.current_spec, "source_original_latest_receipt": self.receipt_spec,
            "original_425_source_audit": getattr(self, "audit_spec", None),
            "exact_three_known_columns_input": getattr(self, "known_columns_spec", None),
            "completed_original_scalar_scan_reused": self.completed_identity,
            "completed_three_columns_source": self.completed_identity,
            "exact_three_known_columns_source_group": "completed_three_columns_source",
            "frozen_three_column_core_sha256": THREE_SHA,
            "complete_nine_dimensional_lattice": getattr(self, "lattice_spec", None),
            "resume_state": getattr(self, "resume_spec", None),
            "baseline_previous_rejection": getattr(self, "baseline_rejection_spec", None),
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
            "legacy_R815_core_sha256": sha(legacy.__file__), "frozen_three_column_core_sha256": THREE_SHA,
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
            "exact_three_known_columns_input": self.known_columns_spec,
            "known_column_indices": list(KNOWN_COLUMNS),
            "known_column_coefficient_counts": [690, 962, 1234],
            "all2886_original_current_congruences_verified": True,
            "all2886_congruences_and_three_columns_imported_without_recomputation": True,
            "completed_original_scalar_scan_reused": self.completed_identity,
            "completed_three_columns_source": self.completed_identity,
            "exact_three_known_columns_source_group": "completed_three_columns_source",
            "frozen_three_column_core_sha256": THREE_SHA,
            "complete_nine_dimensional_lattice": getattr(self, "lattice_spec", None),
            "resume_state": getattr(self, "resume_spec", None),
            "baseline_previous_rejection": getattr(self, "baseline_rejection_spec", None),
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
            "legacy_R815_core_sha256": sha(legacy.__file__), "frozen_three_column_core_sha256": THREE_SHA,
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
    for name in ("config", "proof", "nested-proof", "method", "projective-method", "retained", "previous-three-columns", "output"):
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
            "source_sha256": sha(__file__), "legacy_R815_core_sha256": sha(legacy.__file__), "frozen_three_column_core_sha256": THREE_SHA,
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
