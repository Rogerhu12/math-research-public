#!/usr/bin/env python3
"""Source-bound precision increment of the completed original 56-dimensional lattice.

The future current must be an actually published complete original R787 stage.
This consumer never runs Dixon or an old LLL.  Its new kernel lattice, one new
LLL and the original complete 129-by-280 characteristic-zero test run in Actions.
"""
import argparse
import gc
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpz_mat
import R787_projective_three_probe_reconstruction as legacy
from R787_projective_three_probe_reconstruction import (
    RESULT, FINAL, PREFIX, RECIPE, OLD_CORE, OLD_METHOD, R786_PROOF,
    FIELD_CORE, OLD_TAG, N, NC, LD, TD, ORDERS, PRIME, DIGITS,
    CHILD_EXPECTED, Source, IntegralOrder, BudgetStop,
    sha, fingerprint, read, save, file_spec, integer_rows, strings)

LEGACY_CORE = "c642ec35823dace0ccac4e225e43581398dcce5737dd51cae6a2a903f6028700"
METHOD = "bc91a89140d912b1e3f7da9ec9c12b742884084e60860cc408cbacb9d7b54f0f"
ALGORITHM = "integral-L-fixed-three-probe-precision-kernel-56-lattice-v1"
FIXED_PROBES = (0, 1, NC)
DIMENSION, RESIDUAL_RANK = 56, 42
STRATEGY = {
    "old_complete_basis": "unchanged full 56 rows from the actual completed C0,C1,A0 lattice",
    "fixed_original_probe_indices_C_then_A": list(FIXED_PROBES),
    "full_A_and_C_reduction_compatibility_required": True,
    "residual": "((N_i-D*x_i_new) mod M_new)/M_old in the original integral 14-coordinate order",
    "minor": "first independent original rows of E mod ell; all42 target columns retained",
    "inverse": "42x42 prime inverse, then V*(2I-U*V) with precision doubling modulo ell^d",
    "kernel_rows": "free_rows_then_pivot_rows; K=[I,-E_F*U_inverse;0,qI]*Pi",
    "new_basis": "H_new=K*H_old over Z",
    "LLL": "one new 56-dimensional LLL; all rows and a full canonical-graph unimodular witness",
    "candidate_lift": "nonfree coordinates=center(D*new_original_lift); actual chosen free C=D",
    "old_exact_or_Omega_rejection_reused": False,
    "success": "unchanged complete original129-by280 equations and nonzero B",
    "output_names": "new configuration only: R787-projective-*.json.gz and original RECIPE",
    "normalized_Dixon_digits_computed": 0,
}


def reduce_matrix(matrix, modulus):
    return fmpz_mat([[int(matrix[i, j]) % modulus for j in range(matrix.ncols())]
                     for i in range(matrix.nrows())])


def identity_mod(matrix, modulus):
    assert matrix.nrows() == matrix.ncols()
    return all((int(matrix[i, j])-int(i == j)) % modulus == 0
               for i in range(matrix.nrows()) for j in range(matrix.ncols()))


def first_independent_rows(values, prime):
    echelon, selected = [], []
    for index, row in enumerate(values):
        v = [int(x) % prime for x in row]
        for pivot, old in echelon:
            if v[pivot]:
                factor = v[pivot]
                v = [(a-factor*b) % prime for a, b in zip(v, old)]
        pivot = next((i for i, value in enumerate(v) if value), None)
        if pivot is None:
            continue
        inverse = pow(v[pivot], -1, prime)
        v = [x*inverse % prime for x in v]
        echelon.append((pivot, v))
        echelon.sort(key=lambda pair: pair[0])
        selected.append(index)
        if len(selected) == len(row):
            break
    assert len(selected) == RESIDUAL_RANK
    return selected


def prime_inverse(values, prime):
    size = len(values)
    assert size == RESIDUAL_RANK and all(len(row) == size for row in values)
    augmented = [[int(x) % prime for x in row]+[int(i == j) for j in range(size)]
                 for i, row in enumerate(values)]
    determinant = 1
    for column in range(size):
        pivot = next((i for i in range(column, size) if augmented[i][column]), None)
        assert pivot is not None
        if pivot != column:
            augmented[pivot], augmented[column] = augmented[column], augmented[pivot]
            determinant = -determinant
        entry = augmented[column][column]
        determinant = determinant*entry % prime
        inverse = pow(entry, -1, prime)
        augmented[column] = [x*inverse % prime for x in augmented[column]]
        for row in range(size):
            if row != column and augmented[row][column]:
                factor = augmented[row][column]
                augmented[row] = [(a-factor*b) % prime
                                  for a, b in zip(augmented[row], augmented[column])]
    assert all(augmented[i][j] == int(i == j) for i in range(size) for j in range(size))
    return [row[size:] for row in augmented], determinant % prime


class Job(legacy.Job):
    def __init__(self, args):
        assert flint.__version__ == "0.9.0"
        self.args, self.out = args, args.output
        self.started = time.monotonic()
        self.item = read(args.config)
        assert self.item["producer_inputs_pending"] is False
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert sha(__file__) == self.item["core_sha256"]
        assert sha(args.method) == self.item["projective_method_sha256"] == METHOD
        assert sha(legacy.__file__) == self.item["legacy_core_sha256"] == LEGACY_CORE
        assert self.item["R787_method_sha256"] == OLD_METHOD
        assert self.item["R786_proof_sha256"] == R786_PROOF
        assert sha(args.field_core) == self.item["field_core_sha256"] == FIELD_CORE
        assert self.item["pinned_R787_configuration_sha256"] == OLD_TAG
        self.out.mkdir(parents=True, exist_ok=True)
        self.source = Source(args.retained/"R787", self.item["retained_source"])
        assert self.source.spec["result"] == RESULT
        assert self.source.spec["core_sha256"] == OLD_CORE
        checkpoint = self.item["checkpoint"]
        assert checkpoint["prime"] == PRIME and checkpoint["digits"] == DIGITS
        self.chart = self.source.stage(checkpoint["chart_file"])
        self.old_tag = self.source.tag
        assert fingerprint(self.old_tag) == OLD_TAG
        assert self.old_tag["source_sha256"] == OLD_CORE
        assert self.old_tag["R787_method_sha256"] == OLD_METHOD
        assert self.old_tag["R786_proof_sha256"] == R786_PROOF
        assert self.old_tag["R781_field_core_sha256"] == FIELD_CORE
        assert self.old_tag["python_flint"] == "0.9.0"
        assert self.old_tag["retained_artifacts"] == self.item["retained_artifacts"]
        assert self.old_tag["basis_integer_scale"] == "13744803133596058624"
        assert self.old_tag["original_map_index"] == 4 and self.old_tag["original_map_degree"] == "1206"
        assert self.old_tag["ordinary_power"] == 5 and self.old_tag["basis_dimension"] == N
        assert self.old_tag["qY_bound"] == 128 and self.old_tag["Laurent_exponents"] == [-1, 127]
        assert self.old_tag["full_L_unknown_dimension_over_Q"] == LD
        assert self.old_tag["t_coordinates"] == TD
        assert self.item["new_current_source"] is not None and self.item["new_checkpoint"] is not None
        self.tag = dict(self.old_tag)
        self.tag.update({
            "result": RESULT, "source_sha256": sha(__file__),
            "projective_mode": True, "projective_algorithm": ALGORITHM,
            "projective_method_sha256": sha(args.method),
            "legacy_three_probe_core_sha256": sha(legacy.__file__),
            "pinned_R787_configuration_sha256": OLD_TAG,
            "retained_source": self.item["retained_source"],
            "checkpoint": checkpoint,
            "previous_two_probe_source": self.item["previous_two_probe_source"],
            "completed_three_probe_source": self.item["completed_three_probe_source"],
            "new_current_source": self.item["new_current_source"],
            "new_checkpoint": self.item["new_checkpoint"],
            "precision_increment_strategy": STRATEGY,
            "LLL_integer_lattice_dimension": DIMENSION,
            "original_lifting_reexecuted": False,
            "old_branch_inverse_used": False,
            "old_42_or_56_dimensional_LLL_reexecuted": False,
            "old_exact_or_Omega_rejection_reused": False,
            "parent_module_globals_or_source_identity_modified": False})
        assert self.chart["prime"] == PRIME and self.chart["actual_modular_rank"] == 1186
        assert self.chart["other_free_columns_set_to_zero"] is True
        self.pivots = [int(x) for x in self.chart["pivot_columns"]]
        assert len(self.pivots) == len(set(self.pivots)) == 1186
        assert all(0 <= x < NC for x in self.pivots)
        self.free = int(self.chart["chosen_free_column"])
        self.free_columns = [j for j in range(NC) if j not in set(self.pivots)]
        assert self.free in self.free_columns and len(self.free_columns) == 28
        self.selection = self.source.stage(checkpoint["selection_file"])
        assert self.selection["prime"] == PRIME and self.selection["prime_proved"] is True
        assert self.selection["all_14_L_branches_distinct"] is True
        assert self.selection["all_rational_denominators_units"] is True
        assert self.selection["all_kappa_reductions_invertible"] is True
        self.roots = [tuple(int(x) for x in pair) for pair in self.selection["roots_B_s"]]
        assert len(self.roots) == len(set(self.roots)) == 14
        blocks = self.source.stage(checkpoint["rational_blocks_file"])
        assert blocks["prime"] == PRIME and blocks["exact_E0_Z_zero_verified"] is True
        assert blocks["A_minor_det_mod_prime"] and blocks["B_constant_minor_det_mod_prime"]
        self.ZP, self.ZQ = list(blocks["B_constant_pivot_columns"]), list(blocks["B_constant_free_columns"])
        assert len(self.ZP) == 20 and len(self.ZQ) == NC
        assert sorted(self.ZP+self.ZQ) == list(range(N))
        self.Zp = fmpz_mat(integer_rows(blocks["Z_pivot_integer_rows"], 20, NC))
        self.Zd = int(blocks["Z_free_diagonal"])
        assert self.Zd > 0 and self.Zd % PRIME
        del blocks  # Its old A inverse is never used.
        lift = self.source.stage(checkpoint["lift_file"])
        assert lift["prime"] == PRIME and lift["digits"] == DIGITS
        self.old_modulus = int(lift["modulus"])
        assert self.old_modulus == PRIME**DIGITS
        assert lift["chart_sha256"] == self.source.files[checkpoint["chart_file"]]["sha256"]
        assert lift["full_original_modular_relations_verified"] is True
        old_a = integer_rows(lift["A_L_coordinates"], N, LD)
        old_c = integer_rows(lift["C_L_coordinates"], NC, LD)
        assert all(0 <= x < self.old_modulus for matrix in (old_a, old_c) for row in matrix for x in row)
        assert old_c[self.free] == [1]+[0]*13
        assert all(old_c[j] == [0]*14 for j in self.free_columns if j != self.free)
        del lift
        self.old_probes = [list(old_c[0]), list(old_c[1]), list(old_a[0])]
        self.initialize_new_current(checkpoint, old_a, old_c)
        del old_a, old_c
        gc.collect()
        self.children = {}
        for label in ("R781", "R786"):
            spec = self.old_tag["retained_artifacts"][label]
            expected = CHILD_EXPECTED[label]
            assert spec["result"] == expected["result"]
            assert spec["manifest_sha256"] == expected["manifest"]
            assert spec["core_sha256"] == expected["core"]
            child = Source(args.retained/label, spec)
            certificate = child.raw(spec["certificate_name"])
            assert child.files[spec["certificate_name"]]["sha256"] == expected["certificate"]
            assert certificate["result"] == expected["result"] and certificate["complete"] is True
            child.tag = certificate["configuration"]
            assert child.tag["source_sha256"] == expected["core"]
            child.certificate = certificate
            self.children[label] = child
        self.r781, self.r786 = self.children["R781"], self.children["R786"]
        module_spec = importlib.util.spec_from_file_location("frozen_R781_projective_field", args.field_core)
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        field_input = self.r781.stage("R781-original-real-field-input.json.gz")
        self.f = module.Field(field_input["field"]["original_b_minimal_polynomial"])
        assert self.f.description == field_input["field"] == self.old_tag["field"]
        self.order = IntegralOrder(self.f.description["integral_B_minimal_polynomial"])
        self.R, self.K = [], []
        prior = None
        for n in range(130):
            self.budget()
            name = "R781-inverse-free-Laurent-"+str(n).zfill(3)+".json.gz"
            row = self.r781.stage(name)
            assert row["order"] == n and row["exact_differential_identity_at_this_order"] is True
            if prior is None:
                assert row["input_stage_sha256"] == self.r781.files["R781-original-real-field-input.json.gz"]["sha256"]
                self.kappa = self.f.decode(row["kappa"])
            else:
                assert row["previous_stage_sha256"] == self.r781.files[prior]["sha256"]
            self.K.append(self.f.decode(row["coefficients"]["kappa_power"]))
            if n < ORDERS:
                self.R.append(self.f.decode(row["coefficients"]["R"]))
            prior = name
        assert self.K[0] == self.f.one and self.K[1] == self.kappa and self.R[0] == self.f.one
        cert = self.r786.certificate
        assert cert["exact_power5_basis_dimension"] == N and cert["exact_K_basis_prefix_bound_qY"] == 128
        assert cert["basis_integer_scale"] == self.tag["basis_integer_scale"]
        self.index_spec = cert["basis_index"]
        assert self.r786.files[self.index_spec["file"]]["sha256"] == self.index_spec["sha256"]
        self.index = self.r786.stage(self.index_spec["file"])
        assert self.index["dimension"] == N and self.index["bound_qY"] == 128
        assert len(self.index["basis_rows"]) == N
        columns, real_specs = [], []
        for i, spec in enumerate(self.index["basis_rows"]):
            self.budget()
            assert spec["index"] == i
            assert self.r786.files[spec["file"]]["sha256"] == spec["sha256"]
            name = "R787-real-power5-row-"+str(i).zfill(4)+".json.gz"
            row = self.source.stage(name)
            assert row["index"] == i and row["R786_row_sha256"] == spec["sha256"]
            assert row["all_original_phase_involutions_verified"] is True and row["averaging_used"] is False
            values = integer_rows(row["integer_t_coefficients"], ORDERS, TD)
            columns.append([x for vector in values for x in vector])
            real_specs.append(self.source.ref(name))
        self.F = fmpz_mat([list(row) for row in zip(*columns)])
        del columns
        assert self.F.nrows() == ORDERS*TD and self.F.ncols() == N
        self.initialize_completed_basis()
        audit = self.cache(PREFIX+"source-audit")
        if audit is None:
            audit = self.store(PREFIX+"source-audit", {
                "original_R787_configuration_sha256": OLD_TAG,
                "checkpoint": {key: self.source.ref(checkpoint[key]) for key in
                    ("lift_file", "chart_file", "rational_blocks_file", "selection_file")},
                "real_rows": real_specs, "real_row_count": N,
                "R781_used_files": [self.r781.ref(name) for name in sorted(self.r781.used)],
                "R786_used_files": [self.r786.ref(name) for name in sorted(self.r786.used)],
                "basis_integer_scale": self.tag["basis_integer_scale"],
                "all_original_source_bytes_SHA_and_mathematical_tags_verified": True,
                "old_mathematics_recomputed": False,
                "previous_two_probe_source": self.item["previous_two_probe_source"],
                "completed_three_probe_source": self.item["completed_three_probe_source"],
                "completed_56_configuration_sha256": fingerprint(self.basis_source.tag),
                "completed_56_used_files": [self.basis_source.ref(name) for name in sorted(self.basis_source.used)],
                "new_current_source": self.item["new_current_source"],
                "new_current_stage": self.new_current_spec,
                "full_source_compatibility": self.compatibility_spec,
                "actual_new_Dixon_digits": self.digits,
                "actual_precision_increment": self.increment,
                "new_normalized_Dixon_digits_computed": 0,
                "old_exact_rejections_reused": False})
        self.audit_spec = file_spec(self.path(PREFIX+"source-audit"))
        controls = self.item.get("projective_search_controls", {})
        self.maximum_nodes = int(controls.get("maximum_nodes", 56))
        self.maximum_lattices = int(controls.get("maximum_lattices", 1))
        assert self.maximum_nodes >= 1 and self.maximum_lattices == 1

    def initialize_new_current(self, old_checkpoint, old_a, old_c):
        source_spec = self.item["new_current_source"]
        checkpoint = self.item["new_checkpoint"]
        assert source_spec["result"] == RESULT and source_spec["core_sha256"] == OLD_CORE
        assert source_spec["configuration_sha256"] == OLD_TAG
        self.new_source = Source(self.args.new_current, source_spec)
        assert checkpoint["prime"] == PRIME and checkpoint["digits"] > DIGITS
        assert self.new_source.ref(checkpoint["lift_file"]) == source_spec["current"]
        for key in ("chart_file", "selection_file"):
            assert checkpoint[key] == old_checkpoint[key]
            assert self.new_source.ref(checkpoint[key]) == self.source.ref(old_checkpoint[key])
        assert checkpoint["rational_blocks_file"] == old_checkpoint["rational_blocks_file"]
        initial = self.new_source.raw("public-actions-input.json")
        run = self.new_source.raw("run-receipt.json")
        assert initial["result"] == run["result"] == RESULT
        assert initial["source_commit"] == run["source_commit"] == source_spec["source_commit"]
        assert str(run["workflow_run_id"]) == str(source_spec["run_id"])
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == OLD_CORE
        assert run["process_exit_code"] in source_spec["accepted_checkpoint_exit_codes"]
        if run.get("core_receipt_sha256") is not None:
            receipt = self.new_source.raw("core-receipt.json")
            assert self.new_source.ref("core-receipt.json")["sha256"] == run["core_receipt_sha256"]
            assert receipt["source_sha256"] == OLD_CORE
        lift = self.new_source.stage(checkpoint["lift_file"])
        assert self.new_source.tag == self.old_tag
        assert fingerprint(self.new_source.tag) == OLD_TAG
        assert lift["prime"] == PRIME
        self.digits = int(lift["digits"])
        assert self.digits == checkpoint["digits"] and self.digits > DIGITS
        self.increment = self.digits-DIGITS
        self.q = PRIME**self.increment
        self.modulus = int(lift["modulus"])
        assert self.modulus == PRIME**self.digits == self.old_modulus*self.q
        assert lift["chart_sha256"] == self.source.ref(old_checkpoint["chart_file"])["sha256"]
        assert lift["full_original_modular_relations_verified"] is True
        self.a_lift = integer_rows(lift["A_L_coordinates"], N, LD)
        self.c_lift = integer_rows(lift["C_L_coordinates"], NC, LD)
        assert all(0 <= x < self.modulus for matrix in (self.a_lift, self.c_lift)
                   for row in matrix for x in row)
        assert self.c_lift[self.free] == [1]+[0]*(LD-1)
        assert all(self.c_lift[j] == [0]*LD for j in self.free_columns if j != self.free)
        self.new_current_spec = self.new_source.ref(checkpoint["lift_file"])
        self.tag.update({
            "old_Dixon_digits": DIGITS, "new_Dixon_digits": self.digits,
            "precision_increment_digits": self.increment,
            "actual_precision_increment_modulus": str(self.q),
            "fixed_original_probe_indices_C_then_A": list(FIXED_PROBES),
            "new_normalized_Dixon_digits_computed": 0})
        name = PREFIX+"precision-complete-source-compatibility"
        cached = self.cache(name)
        expected = {
            "old_current": self.source.ref(old_checkpoint["lift_file"]),
            "new_current": self.new_current_spec,
            "old_Dixon_digits": DIGITS, "new_Dixon_digits": self.digits,
            "prime": PRIME, "old_modulus": str(self.old_modulus),
            "new_modulus": str(self.modulus), "increment_modulus": str(self.q),
            "A_dimensions": [N, LD], "C_dimensions": [NC, LD],
            "all_A_reductions_verified": True, "all_C_reductions_verified": True,
            "A_coordinate_count": N*LD, "C_coordinate_count": NC*LD,
            "same_original_chart_and_full_free_C_pattern_verified": True,
            "three_probe_reductions_verified": True,
            "old_exact_or_Omega_rejections_reused": False,
            "new_normalized_Dixon_digits_computed": 0}
        if cached is None:
            self.budget()
            for old_matrix, new_matrix in ((old_a, self.a_lift), (old_c, self.c_lift)):
                for old_row, new_row in zip(old_matrix, new_matrix):
                    assert all(new % self.old_modulus == old for old, new in zip(old_row, new_row))
            self.store(name, expected)
        else:
            for key, value in expected.items():
                assert cached[key] == value
        self.compatibility_spec = self.reference(name)
        self.new_probes = [list(self.source_row(i)) for i in FIXED_PROBES]
        assert all([x % self.old_modulus for x in new] == old
                   for old, new in zip(self.old_probes, self.new_probes))
        del lift

    def initialize_completed_basis(self):
        source = self.item["completed_three_probe_source"]
        assert str(source["run_id"]) == "43754407301"
        assert source["source_commit"] == "1827d794565f94455e4f251f20d1979b55fee783"
        assert source["core_sha256"] == LEGACY_CORE
        assert source["manifest_sha256"] == "7418100ba952913eeab8a60604d92ad4ad5ffdd49d3204602897641198ef77f0"
        self.basis_source = Source(self.args.previous_three_probe, source)
        for key in ("lattice_stage", "raw_lattice_stage", "input_stage", "source_basis_stage",
                    "certificate", "stage_manifest"):
            assert self.basis_source.ref(source[key]["file"]) == source[key]
        final = self.basis_source.raw(source["certificate"]["file"])
        initial = self.basis_source.raw("public-actions-input.json")
        run = self.basis_source.raw("run-receipt.json")
        core = self.basis_source.raw("core-receipt.json")
        assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
        assert str(run["workflow_run_id"]) == str(source["run_id"])
        assert initial["core_sha256"] == core["source_sha256"] == LEGACY_CORE
        assert initial["driver_sha256"] == source["wrapper_sha256"]
        assert run["process_exit_code"] == 2 and run["error"] is None
        assert run["core_receipt_sha256"] == self.basis_source.ref("core-receipt.json")["sha256"]
        assert core["certificate_sha256"] == source["certificate"]["sha256"]
        assert final["complete"] is False and final["completed_search_nodes"] == 56
        for key in ("retained_source", "retained_artifacts", "checkpoint", "previous_two_probe_source"):
            assert initial["job"][key] == self.item[key]
        witness = self.basis_source.stage(source["lattice_stage"]["file"])
        old_tag = self.basis_source.tag
        assert old_tag == final["configuration"]
        assert old_tag["source_sha256"] == LEGACY_CORE
        assert old_tag["pinned_R787_configuration_sha256"] == OLD_TAG
        assert old_tag["projective_algorithm"] == legacy.ALGORITHM
        assert old_tag["projective_method_sha256"] == source["projective_method_sha256"]
        assert old_tag["checkpoint"] == self.item["checkpoint"]
        assert old_tag["retained_source"] == self.item["retained_source"]
        assert old_tag["retained_artifacts"] == self.item["retained_artifacts"]
        assert old_tag["previous_two_probe_source"] == self.item["previous_two_probe_source"]
        raw = self.basis_source.stage(source["raw_lattice_stage"]["file"])
        augmented = self.basis_source.stage(source["input_stage"]["file"])
        earlier = self.basis_source.stage(source["source_basis_stage"]["file"])
        assert witness["reduced_basis_stage"] == source["raw_lattice_stage"]
        assert witness["input_basis_stage"] == source["input_stage"]
        assert raw["input_basis"] == source["input_stage"]
        assert augmented["source_basis_certificate"] == source["source_basis_stage"]
        assert witness["lattice_dimension"] == raw["lattice_dimension"] == DIMENSION
        assert witness["probe_indices_C_then_A"] == augmented["probe_indices_C_then_A"] == list(FIXED_PROBES)
        assert earlier["third_probe_found"] is True and earlier["actual_third_probe_A_index"] == 0
        assert earlier["third_probe"]["global_index"] == NC
        assert earlier["old_42_rows_are_a_full_integer_lattice_basis"] is True
        assert earlier["old_basis_change_times_canonical_equals_saved_basis"] is True
        assert abs(int(earlier["old_basis_change_determinant"])) == 1
        for key in ("all_56_reduced_rows_saved", "all_168_original_probe_congruences_verified",
                    "new_basis_change_times_canonical_equals_reduced_basis",
                    "new_56_rows_are_a_full_integer_lattice_basis"):
            assert witness[key] is True
        assert abs(int(witness["new_basis_change_determinant"])) == 1
        assert raw["all_56_reduced_rows_saved"] is True
        assert witness["weights"] == raw["weights"] == ["1", "1", "1", "1"]
        self.previous_rows = integer_rows(raw["all_56_reduced_rows"], DIMENSION, DIMENSION)
        assert len(witness["probes"]) == 3
        for index, old, probe in zip(FIXED_PROBES, self.old_probes, witness["probes"]):
            assert probe["global_index"] == index
            assert [int(x) for x in probe["original_modular_L_coordinates"]] == old
        self.previous_rejections = {}
        self.old_basis_spec = source["raw_lattice_stage"]
        name = PREFIX+"precision-source-basis"
        cached = self.cache(name)
        expected = {
            "old_complete_basis": self.old_basis_spec,
            "old_complete_basis_witness": source["lattice_stage"],
            "old_configuration_sha256": fingerprint(old_tag),
            "source_compatibility": self.compatibility_spec,
            "fixed_original_probe_indices_C_then_A": list(FIXED_PROBES),
            "old_probes": strings(self.old_probes), "new_probes": strings(self.new_probes),
            "third_probe_found": True, "actual_third_probe_A_index": 0,
            "third_probe": dict(self.probe_spec(NC),
                original_modular_L_coordinates=[str(x) for x in self.new_probes[2]]),
            "old_full_56_basis_consumed_with_unchanged_configuration": True,
            "old_basis_unimodular_witness_consumed_not_recomputed": True,
            "old_42_or_56_dimensional_LLL_reexecuted": False,
            "old_third_probe_selection_not_reexecuted": True,
            "old_exact_or_Omega_rejections_reused": False}
        if cached is None:
            self.store(name, expected)
        else:
            for key, value in expected.items():
                assert cached[key] == value

    def source_basis(self):
        data = self.cache(PREFIX+"precision-source-basis")
        assert data is not None and data["third_probe_found"] is True
        assert data["old_complete_basis"] == self.old_basis_spec
        return data

    def budget(self):
        if time.monotonic()-self.started >= self.args.budget_minutes*60:
            raise BudgetStop("Precision increment budget reached; completed kernel/LLL/candidate stages remain source-bound.")

    def previous_rejection_reference(self, node):
        # A denominator alone does not identify a candidate at a different modulus.
        return None

    def lattice_name(self, pair_index):
        assert pair_index == 0
        return PREFIX+"precision-increment-56-LLL"

    def precision_residuals(self):
        name = PREFIX+"precision-residual-matrix"
        cached = self.cache(name)
        if cached is not None:
            assert cached["old_complete_basis"] == self.old_basis_spec
            assert cached["new_current"] == self.new_current_spec
            assert cached["shape"] == [DIMENSION, RESIDUAL_RANK]
            return cached, self.reference(name)
        entries, values = [], []
        for index, row in enumerate(self.previous_rows):
            row_name = PREFIX+"precision-residual-row-"+str(index).zfill(3)
            old = self.cache(row_name)
            if old is None:
                self.budget()
                result = []
                for probe_index, probe in enumerate(self.new_probes):
                    product = self.order.multiply(row[:LD], probe)
                    numerator = row[LD*(probe_index+1):LD*(probe_index+2)]
                    for a, b in zip(numerator, product):
                        residue = (a-b) % self.modulus
                        quotient, remainder = divmod(residue, self.old_modulus)
                        assert remainder == 0 and 0 <= quotient < self.q
                        result.append(quotient)
                assert len(result) == RESIDUAL_RANK
                self.store(row_name, {
                    "old_complete_basis": self.old_basis_spec,
                    "new_current": self.new_current_spec, "old_basis_row": index,
                    "source_compatibility": self.compatibility_spec,
                    "positive_residual_order": "(old_N_i-old_D*x_i_new) mod M_new, divided by M_old",
                    "all42_integer_divisions_by_old_modulus_verified": True,
                    "residual_values_mod_increment": [str(x) for x in result],
                    "new_normalized_Dixon_digits_computed": 0})
                old = self.cache(row_name)
            assert old["old_complete_basis"] == self.old_basis_spec
            assert old["new_current"] == self.new_current_spec and old["old_basis_row"] == index
            assert old["all42_integer_divisions_by_old_modulus_verified"] is True
            value = [int(x) for x in old["residual_values_mod_increment"]]
            assert len(value) == RESIDUAL_RANK and all(0 <= x < self.q for x in value)
            values.append(value)
            entries.append(self.reference(row_name))
        self.store(name, {
            "old_complete_basis": self.old_basis_spec,
            "new_current": self.new_current_spec,
            "source_compatibility": self.compatibility_spec,
            "shape": [DIMENSION, RESIDUAL_RANK],
            "increment_modulus": str(self.q), "row_stages": entries,
            "residual_integer_rows_mod_increment": strings(values),
            "all56_source_rows_and168_original_order_products_completed": True,
            "all2352_integer_divisions_by_old_modulus_verified": True,
            "branch_evaluation_or_Schur_inverse_used": False,
            "new_normalized_Dixon_digits_computed": 0})
        return self.cache(name), self.reference(name)

    def precision_minor(self, residual, residual_spec):
        name = PREFIX+"precision-unit-minor"
        cached = self.cache(name)
        if cached is not None:
            assert cached["residual_matrix"] == residual_spec
            assert cached["minor_rank"] == RESIDUAL_RANK
            return cached, self.reference(name)
        self.budget()
        values = integer_rows(residual["residual_integer_rows_mod_increment"], DIMENSION, RESIDUAL_RANK)
        pivots = first_independent_rows(values, PRIME)
        free = [i for i in range(DIMENSION) if i not in set(pivots)]
        assert len(free) == LD
        unit = [[value % PRIME for value in values[i]] for i in pivots]
        inverse, determinant = prime_inverse(unit, PRIME)
        assert determinant != 0
        U, V = fmpz_mat(unit), fmpz_mat(inverse)
        assert identity_mod(U*V, PRIME) and identity_mod(V*U, PRIME)
        self.store(name, {
            "residual_matrix": residual_spec, "prime": PRIME,
            "minor_rank": RESIDUAL_RANK, "pivot_original_row_indices": pivots,
            "free_original_row_indices": free,
            "all42_target_columns_retained": True,
            "minor_integer_rows_mod_prime": strings(unit),
            "minor_inverse_integer_rows_mod_prime": strings(inverse),
            "actual_minor_determinant_mod_prime": str(determinant),
            "both_prime_inverse_products_verified": True,
            "selection": STRATEGY["minor"],
            "surjectivity_witness_actually_computed": True})
        return self.cache(name), self.reference(name)

    def precision_inverse(self, residual, residual_spec, minor, minor_spec):
        values = integer_rows(residual["residual_integer_rows_mod_increment"], DIMENSION, RESIDUAL_RANK)
        pivots = minor["pivot_original_row_indices"]
        full_unit = fmpz_mat([values[i] for i in pivots])
        size = RESIDUAL_RANK
        I = fmpz_mat([[int(i == j) for j in range(size)] for i in range(size)])
        precision, previous = 1, None
        inverse = fmpz_mat(integer_rows(minor["minor_inverse_integer_rows_mod_prime"], size, size))
        while True:
            modulus = PRIME**precision
            name = PREFIX+"precision-unit-inverse-"+str(precision).zfill(8)
            cached = self.cache(name)
            if cached is None:
                unit = reduce_matrix(full_unit, modulus)
                assert identity_mod(unit*inverse, modulus) and identity_mod(inverse*unit, modulus)
                self.store(name, {
                    "residual_matrix": residual_spec, "unit_minor": minor_spec,
                    "previous_inverse": previous, "prime": PRIME,
                    "precision_increment_exponent": precision, "modulus": str(modulus),
                    "inverse_integer_rows": strings([
                        [int(inverse[i, j]) for j in range(size)] for i in range(size)]),
                    "both_inverse_products_verified_mod_actual_power": True,
                    "old_normalized_Dixon_or_large_branch_inverse_computed": False})
                cached = self.cache(name)
            assert cached["residual_matrix"] == residual_spec and cached["unit_minor"] == minor_spec
            assert cached["previous_inverse"] == previous
            assert cached["precision_increment_exponent"] == precision and cached["modulus"] == str(modulus)
            assert cached["both_inverse_products_verified_mod_actual_power"] is True
            inverse = fmpz_mat(integer_rows(cached["inverse_integer_rows"], size, size))
            previous = self.reference(name)
            if precision == self.increment:
                return cached, previous
            next_precision = min(2*precision, self.increment)
            next_modulus = PRIME**next_precision
            next_name = PREFIX+"precision-unit-inverse-"+str(next_precision).zfill(8)
            next_cached = self.cache(next_name)
            if next_cached is None:
                self.budget()
                unit = reduce_matrix(full_unit, next_modulus)
                inverse = reduce_matrix(inverse*(2*I-unit*inverse), next_modulus)
            else:
                assert next_cached["previous_inverse"] == previous
                inverse = fmpz_mat(integer_rows(next_cached["inverse_integer_rows"], size, size))
            precision = next_precision

    def precision_kernel(self, residual, residual_spec, minor, minor_spec, inverse, inverse_spec):
        name = PREFIX+"precision-kernel-basis"
        cached = self.cache(name)
        if cached is not None:
            assert cached["residual_matrix"] == residual_spec
            assert cached["unit_minor"] == minor_spec and cached["precision_inverse"] == inverse_spec
            assert cached["old_complete_basis"] == self.old_basis_spec
            return cached, self.reference(name)
        self.budget()
        values = integer_rows(residual["residual_integer_rows_mod_increment"], DIMENSION, RESIDUAL_RANK)
        E = fmpz_mat(values)
        P, F = minor["pivot_original_row_indices"], minor["free_original_row_indices"]
        assert sorted(P+F) == list(range(DIMENSION)) and len(P) == RESIDUAL_RANK and len(F) == LD
        V = fmpz_mat(integer_rows(inverse["inverse_integer_rows"], RESIDUAL_RANK, RESIDUAL_RANK))
        assert inverse["modulus"] == str(self.q)
        U = fmpz_mat([values[i] for i in P])
        assert identity_mod(U*V, self.q) and identity_mod(V*U, self.q)
        W = reduce_matrix(-fmpz_mat([values[i] for i in F])*V, self.q)
        K_rows = []
        for row in range(LD):
            value = [0]*DIMENSION
            value[F[row]] = 1
            for j, pivot in enumerate(P):
                value[pivot] = int(W[row, j])
            K_rows.append(value)
        for pivot in P:
            value = [0]*DIMENSION
            value[pivot] = self.q
            K_rows.append(value)
        K = fmpz_mat(K_rows)
        KE = K*E
        assert all(int(KE[i, j]) % self.q == 0
                   for i in range(DIMENSION) for j in range(RESIDUAL_RANK))
        new_basis = K*fmpz_mat(self.previous_rows)
        new_rows = [[int(new_basis[i, j]) for j in range(DIMENSION)] for i in range(DIMENSION)]
        for row in new_rows:
            for index, probe in enumerate(self.new_probes):
                product = self.order.multiply(row[:LD], probe)
                numerator = row[LD*(index+1):LD*(index+2)]
                assert all((a-b) % self.modulus == 0 for a, b in zip(numerator, product))
        permutation = F+P
        sign = -1 if sum(permutation[i] > permutation[j]
                         for i in range(DIMENSION) for j in range(i+1, DIMENSION)) % 2 else 1
        self.store(name, {
            "old_complete_basis": self.old_basis_spec, "residual_matrix": residual_spec,
            "unit_minor": minor_spec, "precision_inverse": inverse_spec,
            "free_original_row_indices": F, "pivot_original_row_indices": P,
            "coefficient_row_permutation_F_then_P": permutation,
            "permutation_determinant": sign,
            "W_negative_E_free_times_U_inverse_mod_q": strings([
                [int(W[i, j]) for j in range(RESIDUAL_RANK)] for i in range(LD)]),
            "kernel_integer_rows_in_original_basis_order": strings(K_rows),
            "new_full_basis_rows": strings(new_rows),
            "dimension": DIMENSION, "residual_rank": RESIDUAL_RANK,
            "kernel_index_in_old_lattice": str(self.q**RESIDUAL_RANK),
            "kernel_determinant_from_block_triangle": str(sign*self.q**RESIDUAL_RANK),
            "kernel_determinant_derived_from_explicit_block_permutation_not_guessed": True,
            "kernel_times_E_zero_mod_q_verified": True,
            "new_basis_is_exact_K_times_old_basis": True,
            "all168_new_probe_congruences_verified": True,
            "complete_kernel_basis_certified_by_unit_minor_and_explicit_free_parameterization": True,
            "complete_new_precision_lattice_basis_certified": True,
            "new_lattice_full_index_formula": "(ell^new_digits)^42",
            "old_complete_basis_or_LLL_reexecuted": False,
            "new_normalized_Dixon_digits_computed": 0})
        return self.cache(name), self.reference(name)

    def lattice(self, pair_index):
        assert pair_index == 0
        name = self.lattice_name(pair_index)
        cached = self.cache(name)
        if cached is not None:
            assert cached["probe_indices_C_then_A"] == list(FIXED_PROBES)
            assert cached["all_56_reduced_rows_saved"] is True
            assert self.reference(cached["reduced_basis_stage"]["file"]) == cached["reduced_basis_stage"]
            return cached
        residual, residual_spec = self.precision_residuals()
        minor, minor_spec = self.precision_minor(residual, residual_spec)
        inverse, inverse_spec = self.precision_inverse(residual, residual_spec, minor, minor_spec)
        kernel, kernel_spec = self.precision_kernel(residual, residual_spec, minor, minor_spec, inverse, inverse_spec)
        input_rows = integer_rows(kernel["new_full_basis_rows"], DIMENSION, DIMENSION)
        reduced_name = PREFIX+"precision-increment-reduced-basis"
        raw = self.cache(reduced_name)
        if raw is None:
            self.budget()
            reduced = fmpz_mat(input_rows).lll(delta=0.99, eta=0.51)
            self.store(reduced_name, {
                "input_basis_stage": kernel_spec,
                "old_complete_basis": self.old_basis_spec,
                "new_current": self.new_current_spec,
                "lattice_dimension": DIMENSION,
                "weights": ["1", "1", "1", "1"],
                "all_56_reduced_rows": strings([
                    [int(reduced[i, j]) for j in range(DIMENSION)] for i in range(DIMENSION)]),
                "all_56_reduced_rows_saved": True,
                "full_integer_basis_witness_is_a_separate_required_stage": True,
                "old_42_or_56_dimensional_LLL_reexecuted": False,
                "LLL_is_only_candidate_generation": True})
            raw = self.cache(reduced_name)
        assert raw["input_basis_stage"] == kernel_spec and raw["new_current"] == self.new_current_spec
        reduced_rows = integer_rows(raw["all_56_reduced_rows"], DIMENSION, DIMENSION)
        self.budget()
        blocks, canonical = self.canonical_graph(self.new_probes)
        change, determinant = self.canonical_basis_change(reduced_rows, blocks, canonical)
        order = sorted(range(DIMENSION), key=lambda i: (sum(x*x for x in reduced_rows[i]), i))
        candidates, diagnostics, seen = [], [], set()
        for index in order:
            row = reduced_rows[index]
            denominator = row[:LD]
            diagnostic = {
                "LLL_row": index, "weighted_squared_norm": str(sum(x*x for x in row)),
                "maximum_D_bits": max(abs(x).bit_length() for x in denominator),
                "all_three_new_probe_congruences_verified": True}
            if not any(denominator):
                diagnostic["candidate_status"] = "zero_denominator"
                diagnostics.append(diagnostic)
                continue
            sign = 1 if next(x for x in denominator if x) > 0 else -1
            denominator = [sign*x for x in denominator]
            node = self.node(denominator, 0, index, sign)
            node["source_precision_increment_lattice_index"] = 0
            diagnostic.update({
                "candidate_id": node["id"], "candidate_sign": sign,
                "ell_unit_diagnostic_only": self.ell_unit(denominator),
                "height_and_unit_properties_not_used_as_acceptance_bounds": True,
                "old_exact_or_Omega_rejection_reused": False})
            if node["id"] in seen:
                diagnostic["candidate_status"] = "duplicate_denominator_in_this_new_lattice"
            else:
                seen.add(node["id"])
                diagnostic["candidate_status"] = "retained_for_new_original_exact_verification"
                candidates.append(node)
            diagnostics.append(diagnostic)
        self.store(name, {
            "probe_pair_index": 0, "probe_indices_C_then_A": list(FIXED_PROBES),
            "probes": [dict(self.probe_spec(i),
                       original_modular_L_coordinates=[str(x) for x in self.source_row(i)])
                       for i in FIXED_PROBES],
            "lattice_dimension": DIMENSION, "weights": ["1", "1", "1", "1"],
            "source_compatibility": self.compatibility_spec,
            "old_complete_basis": self.old_basis_spec,
            "new_current": self.new_current_spec,
            "residual_matrix": residual_spec, "unit_minor": minor_spec,
            "precision_inverse": inverse_spec, "kernel_basis_stage": kernel_spec,
            "reduced_basis_stage": self.reference(reduced_name),
            "all_56_reduced_rows_saved": True,
            "all_168_new_probe_congruences_verified": True,
            "new_canonical_graph_sha256": fingerprint(strings(canonical)),
            "new_basis_change_integer_rows": strings(change),
            "new_basis_change_determinant": str(determinant),
            "new_basis_change_times_new_canonical_equals_reduced_basis": True,
            "new_56_rows_are_a_full_integer_lattice_basis": True,
            "candidate_order_by_exact_squared_norm": order,
            "row_diagnostics": diagnostics, "candidates": candidates,
            "all_nonzero_distinct_denominators_retained": True,
            "sufficient_uniqueness_bound_not_used": True,
            "all_candidates_use_new_original_normalized_lift_directly": True,
            "old_42_or_56_dimensional_LLL_reexecuted": False,
            "new_normalized_Dixon_digits_computed": 0,
            "old_exact_or_Omega_rejection_reused": False,
            "LLL_is_only_candidate_generation": True})
        print("PROJECTIVE_PRECISION_LLL="+json.dumps({
            "old_digits": DIGITS, "new_digits": self.digits, "increment": self.increment,
            "probe_indices": list(FIXED_PROBES), "dimension": DIMENSION,
            "actual_unit_minor_determinant_mod_prime": minor["actual_minor_determinant_mod_prime"],
            "new_integer_basis_change_determinant": str(determinant),
            "candidate_count": len(candidates), "all_rows_saved": True}), flush=True)
        return self.cache(name)

    def candidate_recipe(self, node):
        name = self.node_prefix(node)+"-candidate"
        cached = self.cache(name)
        if cached is not None:
            assert cached["node_id"] == node["id"]
            return name, cached
        aa, cc = self.accepted_numerators(node)
        bb = self.expand_B(cc)
        assert any(x for row in bb for x in row)
        content = 0
        for row in aa+bb:
            for value in row:
                content = math.gcd(content, value)
        assert content > 0
        aa = [[x//content for x in row] for row in aa]
        bb = [[x//content for x in row] for row in bb]
        denominator = [int(x) for x in node["denominator"]]
        recipe = {
            "node_id": node["id"],
            "source_lattice": self.reference(self.lattice_name(node["source_probe_pair_index"])),
            "source_reduced_row": node["source_LLL_row"],
            "source_reduced_row_sign": node["source_LLL_row_sign"],
            "nonfree_coordinates_are_centered_original_modular_products": True,
            "chosen_free_coordinate_is_actual_D_without_centering": True,
            "height_acceptance_bound_used": False,
            "field": self.f.description,
            "L_basis": "B^i*s^j, j=0..1 outer, i=0..6; B=lambda*b",
            "original_R786_basis_order": True,
            "basis_integer_scale": self.tag["basis_integer_scale"],
            "R786_producer": self.tag["retained_artifacts"]["R786"],
            "R786_basis_index": self.index_spec,
            "A_integer_L_coordinates": strings(aa),
            "B_integer_L_coordinates": strings(bb),
            "common_rational_denominator_cleared": "1",
            "common_rational_denominator_field_applies_after_algebraic_scaling": True,
            "common_integer_content_removed": str(content),
            "algebraic_L_denominator_before_content": {
                "integer_L_coordinates": [str(x) for x in denominator],
                "rational_scale": ["1", "1"]},
            "algebraic_L_scale_after_content": {
                "integer_L_coordinates": [str(x) for x in denominator],
                "rational_scale": ["1", str(content)]},
            "rational_reconstruction_modulus": str(self.modulus),
            "projective_mode": True,
            "source_Dixon_digits": self.digits,
            "old_Dixon_digits": DIGITS,
            "precision_increment_digits": self.increment,
            "new_normalized_Dixon_digits_computed": 0,
            "source_lift": self.new_current_spec,
            "new_current_source": self.item["new_current_source"],
            "source_compatibility": self.compatibility_spec,
            "source_chart": self.source.ref(self.item["checkpoint"]["chart_file"]),
            "source_Z": self.source.ref(self.item["checkpoint"]["rational_blocks_file"]),
            "chosen_free_column": self.free,
            "free_C_column_equals_exact_algebraic_scale_before_content": True,
            "all_other_free_C_columns_zero_before_content": True,
            "Z_expansion_used_before_common_integer_content_removal": True,
            "candidate_only_until_full_exact_verification": True}
        self.store(name, recipe)
        return name, self.cache(name)

    def final_certificate(self, complete, state, relation=None):
        stage_manifest = self.stage_inventory()
        lattice_name = self.lattice_name(0)
        lattice = self.cache(lattice_name)
        assert lattice is not None
        certificate = {
            "result": RESULT, "configuration": self.tag, "complete": bool(complete),
            "projective_mode": True, "p": 41,
            "projective_algorithm": ALGORITHM,
            "original_map_index": 4, "original_map_degree": "1206",
            "original_full_L_retained": True,
            "exact_nonzero_A_B_relation_verified": bool(complete),
            "same_normalized_1186_direction_verified": bool(complete),
            "exact_verified_Laurent_exponents": [-1, 127] if complete else None,
            "exact_verified_t_coordinates": TD if complete else 0,
            "exact_verified_Q_coordinates_per_order": LD*TD if complete else 0,
            "exact_verified_orders": ORDERS if complete else 0,
            "actual_y_map_recovered": bool(complete), "beta_or_height_computed": False,
            "relation_spec": relation, "function_recipe": relation,
            "actual_auxiliary_prime": PRIME, "actual_modular_Schur_rank": 1186,
            "characteristic_zero_Schur_rank": 1186,
            "full_characteristic_zero_kernel_claimed": False,
            "actual_Dixon_digits": self.digits, "source_Dixon_digits": self.digits,
            "old_Dixon_digits": DIGITS, "precision_increment_digits": self.increment,
            "additional_Dixon_digits_computed": 0, "new_normalized_Dixon_digits_computed": 0,
            "original_source": self.item["retained_source"],
            "previous_two_probe_source": self.item["previous_two_probe_source"],
            "completed_three_probe_source": self.item["completed_three_probe_source"],
            "new_current_source": self.item["new_current_source"],
            "new_current_stage": self.new_current_spec,
            "legacy_three_probe_core_sha256": LEGACY_CORE,
            "source_audit": self.audit_spec,
            "source_compatibility": self.compatibility_spec,
            "old_complete_basis": self.old_basis_spec,
            "source_basis": self.reference(PREFIX+"precision-source-basis"),
            "precision_residual_matrix": lattice["residual_matrix"],
            "unit_minor": lattice["unit_minor"], "precision_inverse": lattice["precision_inverse"],
            "kernel_basis": lattice["kernel_basis_stage"],
            "new_lattice": self.reference(lattice_name),
            "fixed_probe_indices_C_then_A": list(FIXED_PROBES),
            "third_probe_found": True, "actual_third_probe_A_index": 0,
            "no_eligible_third_probe": False,
            "complete_new_precision_lattice_basis_certified": True,
            "all_full_A_and_C_source_reductions_verified": True,
            "small42_precision_residual_inverse_computed": True,
            "composite_modulus_matrix_inversion": self.increment > 1,
            "original_large_Schur_or_A_inverse_recomputed": False,
            "LLL_success_guarantee_claimed": False,
            "candidate_search_exhausted": state["probe_pair_index"] == 1 and not complete,
            "finite_search_scope": "one_actual_precision_increment_of_completed_C0_C1_A0_full56_basis",
            "search_node_budget_reached": (
                state["probe_pair_index"] < 1
                and len(state["processed_node_ids"]) >= self.maximum_nodes and not complete),
            "search_lattice_budget_reached": False,
            "remaining_schedule": [] if state["probe_pair_index"] == 1 else [{
                "precision_increment_lattice_index": 0,
                "probe_indices_C_then_A": list(FIXED_PROBES),
                "next_candidate_position": state["next_candidate_position"]}],
            "completed_search_nodes": len(state["processed_node_ids"]),
            "new_exact_candidate_evaluations": len(state["new_exact_candidate_ids"]),
            "previous_exact_candidate_rejections_referenced": 0,
            "consumed_LLL_candidate_rows": state["consumed_LLL_candidate_rows"],
            "actual_run_maximum_candidates": self.maximum_nodes,
            "actual_run_maximum_lattices": self.maximum_lattices,
            "remaining_probe_pairs": 1-state["probe_pair_index"],
            "next_candidate_position": state["next_candidate_position"],
            "completed_lattice_indices": state["completed_lattice_indices"],
            "all_56_reduced_rows_per_completed_lattice_retained": True,
            "old_42_or_56_dimensional_LLL_recomputed": False,
            "old_exact_or_Omega_rejections_reused": False,
            "height_uniqueness_bound_used_for_success": False,
            "closed_rejected_work_retained_as_complete_decision_and_SHA_receipt": True,
            "stage_manifest": stage_manifest,
            "resume_state": self.reference(PREFIX+"search-current"),
            "seconds": time.monotonic()-self.started}
        assert not state["referenced_previous_rejection_ids"]
        save(self.out/FINAL, certificate)
        return certificate


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New exact arithmetic belongs to public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "method", "field-core", "retained", "previous-search",
                 "previous-three-probe", "new-current", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    started, job = time.monotonic(), None
    try:
        job = Job(args)
        certificate = job.complete()
        complete = certificate["complete"]
        receipt = {
            "result": RESULT, "projective_mode": True, "complete": complete,
            "source_sha256": sha(__file__), "legacy_three_probe_core_sha256": sha(legacy.__file__),
            "projective_algorithm": ALGORITHM,
            "certificate_sha256": sha(args.output/FINAL),
            "actual_y_map_recovered": complete, "beta_or_height_computed": False,
            "same_normalized_1186_direction_verified": complete,
            "exact_verified_orders": ORDERS if complete else 0,
            "exact_verified_t_coordinates": TD if complete else 0,
            "old_Dixon_digits": DIGITS, "source_Dixon_digits": job.digits,
            "precision_increment_digits": job.increment,
            "additional_Dixon_digits_computed": 0, "new_normalized_Dixon_digits_computed": 0,
            "candidate_search_exhausted": certificate["candidate_search_exhausted"],
            "search_node_budget_reached": certificate["search_node_budget_reached"],
            "search_lattice_budget_reached": False, "search_time_budget_reached": False,
            "new_exact_candidate_evaluations": certificate["new_exact_candidate_evaluations"],
            "previous_exact_candidate_rejections_referenced": 0,
            "complete_new_precision_lattice_basis_certified": True,
            "old_42_or_56_dimensional_LLL_recomputed": False,
            "all_completed_decisions_and_reduced_rows_preserved": True,
            "only_closed_rejected_payloads_retired_with_SHA_receipt": True,
            "seconds": time.monotonic()-started}
        save(args.output/"core-receipt.json", receipt)
        print("PROJECTIVE_PRECISION_CORE_RECEIPT="+json.dumps(receipt), flush=True)
        return 0 if complete else 2
    except BaseException as error:
        receipt = {
            "result": RESULT, "projective_mode": True, "complete": False,
            "source_sha256": sha(__file__), "legacy_three_probe_core_sha256": sha(legacy.__file__),
            "projective_algorithm": ALGORITHM,
            "error": type(error).__name__+": "+str(error),
            "search_time_budget_reached": isinstance(error, BudgetStop),
            "source_Dixon_digits": getattr(job, "digits", None),
            "precision_increment_digits": getattr(job, "increment", None),
            "old_Dixon_digits": DIGITS, "additional_Dixon_digits_computed": 0,
            "new_normalized_Dixon_digits_computed": 0,
            "all_completed_decisions_and_reduced_rows_preserved": True,
            "only_closed_rejected_payloads_retired_with_SHA_receipt": True,
            "actual_y_map_recovered": False, "beta_or_height_computed": False,
            "seconds": time.monotonic()-started}
        save(args.output/"core-receipt.json", receipt)
        print("PROJECTIVE_PRECISION_CORE_RECEIPT="+json.dumps(receipt), flush=True)
        if isinstance(error, BudgetStop):
            return 124
        raise


if __name__ == "__main__":
    sys.exit(main())
