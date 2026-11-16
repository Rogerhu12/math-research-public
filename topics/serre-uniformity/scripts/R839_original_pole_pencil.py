#!/usr/bin/env python3
"""Original D pencil by five old fibers; eight exact pole-ideal generators."""
import argparse
import gc
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path

LEGACY_NAME = "R839_original_short_RR_spaces.py"
LEGACY_SHA = "0a027c2dd83cfab37181e6386cfd8b22baf176421b727d81a7584d7b351d0c36"


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            h.update(block)
    return h.hexdigest()


legacy_path = Path(__file__).resolve().with_name(LEGACY_NAME)
assert sha(legacy_path) == LEGACY_SHA
loader = importlib.util.spec_from_file_location("R839_pole_pencil_exact_helpers", legacy_path)
L = importlib.util.module_from_spec(loader)
loader.loader.exec_module(L)

RESULT = "R839-original-D-pencil-and-eight-generator-pole-ideal"
FINAL = "p41-original-D-pencil-and-pole-ideal-certificate.json"
INVENTORY = "R839-pole-pencil-stage-manifest.json.gz"
PRIME, FREE, V3, V5 = 1000000753, 272, 690, 1234
EPS = [0]+[1]*144+[2]*127
NODES = list(range(5))
LABELS = ("R842", "R827", "R787", "R786", "R775", "R809", "R837")
BASE_KEYS = L.BASE_KEYS
S5_INDEX = "R809-S5-basis-index.json.gz"
S5_INVERSE = "R827-prime-1000000753-S5-fixed-minor-inverse.json.gz"
S5_MATRIX = "R839-original-S5-fixed-place-matrix.json.gz"
D_KERNEL = "R839-original-D-unit-kernel-basis.json.gz"
GRID = "R827-eight-original-unit-cyclic-nodes.json.gz"
INDEX5 = "R786-exact-power5-basis-index.json.gz"
R842_RESULT = "R839-original-two-chart-short-RR-spaces-and-D-kernel"
R842_CORE = "6fe0a0d3f37592b1ac3081a8347a205503de41cdd54e41a05529c837a7b3c73e"
R775_POWER4_SHA = "85beb7662eee64f4eca9e205314a6625506e3041bea199985489c7cf1f62dd4e"
R775_POWER5_SHA = "7aff6faa89a91649db5549bbf9360647534bff6f9586ce3f5963e322d33c30ba"
STRATEGY = {
    "auxiliary_prime": PRIME, "original_branch": 0,
    "normal_basis_rank": FREE, "normal_basis_degrees": EPS,
    "original_V3_dimension": V3, "original_D_RR_dimension": 295,
    "normal_conversion_rhs_count": V3, "normal_conversion_batch_size": 30,
    "old_S5_prefix_shape": [1380, V5], "normal_V3_coordinate_count": V3,
    "old_fiber_nodes": NODES, "fiber_evaluation_matrix_shape": [1360, 1380],
    "required_pencil_rank": 1111,
    "fixed_a_original_D_basis_column": 0,
    "b_candidate_family": "sum_{j=0}^{294} integer_parameter^j original_D_basis_column_j",
    "candidate_parameter_start": 1,
    "all_690_tau_squared_V3_products_are_original_V5_same_index_aliases": True,
    "old_S5_inverse_or_Krylov_inverse_or_Fourier_products_recomputed": False,
    "rank_certificate_only_requires_evaluation_lower_bound": True,
    "five_fibers_not_assumed_to_avoid_D": True,
    "candidate_pole_ideal_generators": 8,
    "original_pole_divisor_identity": "E_y = fixed_21_branch_points + 3*original_D",
    "char0_sections_remain_original_unit_solve_expressions": True,
    "budget_maximum_trials_and_absolute_directories_excluded_from_mathematical_identity": True,
}
read, save, plain, spec = L.read, L.save, L.plain, L.spec
rows, submatrix, pivots, nmod_mat = L.rows, L.submatrix, L.pivots, L.nmod_mat


def zero(height, width):
    return nmod_mat([[0]*width for _ in range(height)], PRIME)


class Job:
    def __init__(self, args):
        self.args, self.started = args, time.monotonic()
        self.item = read(args.config)
        assert self.item["result"] == RESULT and self.item["core_sha256"] == sha(__file__)
        assert self.item["legacy_core"] == LEGACY_NAME and self.item["legacy_core_sha256"] == LEGACY_SHA
        for key in ("proof", "method"):
            assert sha(self.item[key]) == self.item[key+"_sha256"]
        self.out = args.out
        self.out.mkdir(parents=True, exist_ok=True)
        self.sources = {name: L.Source(name, self.item["sources"][name]) for name in LABELS}
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "python_flint": L.flint.__version__,
            "p": 41, "legacy_R839_core_sha256": LEGACY_SHA,
            "pole_pencil_proof_sha256": self.item["proof_sha256"],
            "pole_pencil_method_sha256": self.item["method_sha256"],
            "sources": {name: source.stable() for name, source in self.sources.items()},
            **STRATEGY,
        }
        self.r842, self.r827, self.r787, self.r786, self.r775, self.r809, self.r837 = (
            self.sources[name] for name in LABELS)
        self.pos3, self.pos5 = L.normal_positions(3), L.normal_positions(5)
        self.pos5_map = {value: i for i, value in enumerate(self.pos5)}
        self.keep5 = [self.pos5_map[value] for value in self.pos3]
        self.extra5 = [i for i in range(V5) if i not in set(self.keep5)]
        self.current_stage = "initializing"
        self.S5 = self.S5_inverse = self.normal = self.kernel = None
        self.complete = False
        self.actual_rank = None
        self.accepted_parameter = None
        self.maximum_trials = int(self.item.get("maximum_trials", 4))
        assert self.maximum_trials >= 1
        self.audit_spec = self.normal_index_spec = None
        self.last_trial = None

    def budget(self):
        if time.monotonic()-self.started >= self.args.budget_minutes*60:
            raise L.BudgetStop("Public pole-pencil budget reached after completed atomic stage "+self.current_stage)

    def mark(self, name):
        self.current_stage = name
        self.budget()
        print("STAGE "+name, flush=True)

    def path(self, name):
        assert name.startswith("R839-pole-") and Path(name).name == name
        return self.out/(name if name.endswith(".json.gz") else name+".json.gz")

    def get(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["result"] == RESULT and value["complete"] is True and value["configuration"] == self.tag
        return value

    def put(self, name, value):
        assert "result" not in value and "configuration" not in value
        value = dict(value, result=RESULT, configuration=self.tag, complete=True)
        save(self.path(name), value)
        return value

    def source(self, name):
        return spec(self.path(name))

    def audit(self):
        name = "R839-pole-original-source-and-alias-audit"
        old = self.get(name)
        cert = self.r842.certificate
        assert self.r842.identity["result"] == R842_RESULT and self.r842.identity["core_sha256"] == R842_CORE
        assert cert is not None and cert["complete"] is True
        assert cert["prime"] == PRIME and cert["original_branch"] == 0
        assert cert["exact_original_D_RR_space_as_unit_chart_expression_certified"] is True
        assert cert["actual_T11_rank"] == 2451 and cert["actual_T5_rank"] == 415
        assert cert["actual_D_kernel_rank"] == 395 and cert["actual_D_RR_dimension"] == 295
        assert plain(cert["D_kernel_basis"]) == plain(self.r842.source(D_KERNEL))
        self.kernel_data = self.r842.stage(D_KERNEL)
        assert self.kernel_data["prime"] == PRIME
        assert self.kernel_data["exact_original_D_RR_space_as_unit_chart_expression_certified"] is True
        assert self.kernel_data["all830_original_equations_verified_for_all295_columns"] is True
        assert self.kernel_data["original_free_normalization_identity_verified"] is True
        assert self.kernel_data["actual_rank"] == 395 and self.kernel_data["actual_minor_determinant_mod_prime"]
        exact_basis = self.kernel_data["exact_unit_solve_expression"]
        assert exact_basis["operation"] == "normalized_kernel_of_original_selected_equations"
        assert exact_basis["exact_kernel"] == "H0(3H-D)" and exact_basis["exact_dimension"] == 295
        assert plain(exact_basis["original_matrix"]) == plain(self.kernel_data["source_original_D_matrix"])
        original_D_matrix = self.r842.stage(self.kernel_data["source_original_D_matrix"])
        assert original_D_matrix["matrix_shape"] == [830, V3]
        assert original_D_matrix["exact_kernel"] == "H0(3H-D)"
        assert original_D_matrix["exact_kernel_dimension"] == 295
        assert original_D_matrix["actual_P0_multiplicity_in_D"] == 0
        assert original_D_matrix["both_original_fixed_anchors_used"] is True
        L.checked_shape(self.kernel_data["kernel_basis_mod_prime"], V3, 295)
        self.kernel = nmod_mat(self.kernel_data["kernel_basis_mod_prime"], PRIME)
        self.free_columns = self.kernel_data["original_V3_free_columns"]
        assert len(self.free_columns) == len(set(self.free_columns)) == 295
        self.s5_data = self.r842.stage(S5_MATRIX)
        assert self.s5_data["prime"] == PRIME and self.s5_data["matrix_shape"] == [1380, V5]
        assert self.s5_data["normal_basis_row_mapping"] == [list(x) for x in self.pos5]
        assert self.s5_data["original_integer_scale"] == str(82**10)
        assert plain(self.s5_data["source_S5_index"]) == plain(self.r809.source(S5_INDEX))
        assert plain(self.s5_data["source_completed_inverse"]) == plain(self.r827.source(S5_INVERSE))
        self.s5_index = self.r809.stage(S5_INDEX)
        assert self.s5_index["dimension"] == V5 and self.s5_index["normal_basis_degrees"] == EPS
        assert self.s5_index["integer_scale"] == str(82**10)
        assert self.s5_index["all_original_term_phases_and_scales_verified"] is True
        assert len(self.s5_index["basis_rows"]) == V5
        for label in ("R827", "R809", "R786", "R837"):
            inherited = self.r842.tag["sources"][label]
            assert all(inherited[key] == self.sources[label].identity[key] for key in BASE_KEYS)
        for i, row in enumerate(self.s5_index["basis_rows"]):
            assert row["index"] == i
            assert (row["normal_basis_index"], row["z_degree"]) == self.pos5[i]
            assert plain(row["source"]) == plain(self.s5_data["source_original_S5_rows"][i])
            assert plain(self.r809.source(row["source"])) == plain(row["source"])
        self.inverse_data = self.r827.stage(S5_INVERSE)
        assert self.inverse_data["prime"] == PRIME and self.inverse_data["both_inverse_products_verified"] is True
        assert self.inverse_data["actual_determinant_mod_prime"]
        assert plain(self.inverse_data["S5_basis_index"]) == plain(self.r809.source(S5_INDEX))
        self.s5_rows = self.inverse_data["row_indices"]
        assert len(self.s5_rows) == len(set(self.s5_rows)) == V5
        assert self.inverse_data["column_indices"] == list(range(V5))
        for label in ("R787", "R809"):
            inherited = self.r827.tag["source_identities"][label]
            assert all(inherited[key] == self.sources[label].identity[key]
                       for key in BASE_KEYS if key != "configuration_sha256")
        self.index5 = self.r786.stage(INDEX5)
        assert self.index5["dimension"] == V5 and self.index5["integer_scale"] == str(82**10)
        assert self.index5["bound_qY"] == 128 and self.index5["basis_selection_recomputed"] is False
        for power, digest in ((4, R775_POWER4_SHA), (5, R775_POWER5_SHA)):
            filename = "R775-basis-power-"+str(power)+".json.gz"
            assert self.r775.files[filename]["sha256"] == digest
            value = self.r775.stage(filename)
            assert self.r786.tag["R775_completed_prefix_producer"]["files"][filename] == digest
            assert self.r786.tag["R775_completed_prefix_producer"]["core_sha256"] == self.r775.identity["core_sha256"]
            assert len(value["basis"]) >= V3
            for i in range(V3):
                assert value["basis"][i]["recipe"] == {
                    "kind": "product", "left_index": 0, "left_power": 1,
                    "right_index": i, "right_power": power-1}
        # Exact R775 stage byte identities are common to the original resumed producer.
        assert self.r786.certificate is not None and self.r786.certificate["complete"] is True
        assert self.r786.certificate["basis_integer_scale"] == str(82**10)
        self.grid = self.r827.stage(GRID)
        assert self.grid["prime"] == PRIME and self.grid["points"][:5] == NODES
        assert self.grid["all_eight_actual_determinants_nonzero"] is True
        assert self.grid["distinct_residue_values_and_unit_Vandermonde_certified"] is True
        assert len(self.grid["Krylov_point_stages"]) == 8
        common_W = common_cyclic = None
        for j, node in enumerate(NODES):
            point_name = "R827-prime-1000000753-z-"+str(node)+"-Krylov.json.gz"
            assert plain(self.grid["Krylov_point_stages"][j]) == plain(self.r827.source(point_name))
            point = self.r827.stage(point_name)
            assert point["prime"] == PRIME and point["z0"] == node and point["usable"] is True
            assert point["actual_cyclic_rank"] == FREE and point["actual_determinant_mod_prime"]
            assert point["both_inverse_products_verified"] is True
            L.checked_shape(point["W_evaluated_mod_prime"], FREE, FREE)
            L.checked_shape(point["inverse_Krylov_matrix_mod_prime"], FREE, FREE)
            if common_W is None:
                common_W, common_cyclic = point["source_original_W"], point["source_original_cyclic_witness"]
            else:
                assert point["source_original_W"] == common_W and point["source_original_cyclic_witness"] == common_cyclic
        self.common_W, self.common_cyclic = common_W, common_cyclic
        assert plain(common_W) == plain(self.r827.manifest_files[common_W["file"]])
        first_original_row = self.r787.stage("R787-real-power5-row-0000.json.gz")
        assert first_original_row["R786_row_sha256"] == self.index5["basis_rows"][0]["sha256"]
        inherited_R786 = self.r787.tag["retained_artifacts"]["R786"]
        assert all(inherited_R786[key] == self.r786.identity[key]
                   for key in BASE_KEYS if key != "configuration_sha256")
        c837 = self.r837.certificate
        assert c837 is not None and c837["complete"] is True and c837["fixed_branch_pencil_certified"] is True
        assert c837["actual_pencil_rank"] == 1213
        pencil_spec = c837["pencil_certificate"]
        pencil = self.r837.stage(pencil_spec)
        assert pencil["actual_pencil_rank"] == 1213 and pencil["fixed_branch_pencil_certified"] is True
        assert pencil["rank1213_implies_exact_common_zero_divisor_Dcusp_plus_P0"] is True
        assert pencil["minor_determinant_mod_prime"]
        self.anchor_sources = {"u": pencil["first_anchor"], "v": pencil["second_anchor"]}
        self.anchor_values = {key: self.r837.stage(value) for key, value in self.anchor_sources.items()}
        for key, value in self.anchor_values.items():
            assert value["exact_nonzero_member_of_U"] is True
            assert value["primitive_normalization_scale"] is not None
            assert len(value["integer_sparse_coordinates"]) == value["original_V2_nonzero_term_count"]
        if old is None:
            self.mark(name)
            old = self.put(name, {
                "prime": PRIME, "source_complete_original_D_basis": self.r842.source(D_KERNEL),
                "source_original_S5_matrix": self.r842.source(S5_MATRIX),
                "source_original_S5_basis_index": self.r809.source(S5_INDEX),
                "source_completed_same_prime_S5_inverse": self.r827.source(S5_INVERSE),
                "source_original_power5_basis_index": self.r786.source(INDEX5),
                "source_original_power4_recipe": self.r775.source("R775-basis-power-4.json.gz"),
                "source_original_power5_recipe": self.r775.source("R775-basis-power-5.json.gz"),
                "all_690_original_tau_squared_product_recipes_verified": True,
                "original_power3_and_power5_indices_identical": True,
                "source_original_unit_grid": self.r827.source(GRID),
                "source_original_W": common_W, "source_original_cyclic_witness": common_cyclic,
                "source_original_pencil": self.r837.source(pencil_spec),
                "source_original_fixed_anchors": {key: self.r837.source(value) for key, value in self.anchor_sources.items()},
                "original_D_not_replaced_by_a_linearly_equivalent_divisor": True,
                "old_S5_and_Krylov_inverse_arithmetic_repeated": False,
            })
        assert old["source_complete_original_D_basis"] == self.r842.source(D_KERNEL)
        self.audit_spec = self.source(name)
        return old

    def normal_V3(self):
        index_name = "R839-pole-original-V3-normal-index"
        index = self.get(index_name)
        blocks = []
        if index is not None:
            blocks = index["blocks"]
        else:
            self.S5 = nmod_mat(self.s5_data["columns_mod_prime"], PRIME).transpose()
            self.S5_inverse = nmod_mat(self.inverse_data["inverse_mod_prime"], PRIME)
            assert self.S5.nrows() == 1380 and self.S5.ncols() == V5
            for first in range(0, V3, 30):
                stop = min(first+30, V3)
                name = "R839-pole-original-V3-normal-"+str(first).zfill(4)+"-"+str(stop).zfill(4)
                value = self.get(name)
                if value is None:
                    self.mark(name)
                    columns, old_sources = [], []
                    for i in range(first, stop):
                        filename = "R787-real-power5-row-"+str(i).zfill(4)+".json.gz"
                        row = self.r787.stage(filename)
                        assert row["index"] == i and row["R786_row_sha256"] == self.index5["basis_rows"][i]["sha256"]
                        assert row["all_original_phase_involutions_verified"] is True and row["averaging_used"] is False
                        data = row["integer_t_coefficients"]
                        assert len(data) == 129 and all(len(block) == 20 for block in data)
                        columns.append([int(x) % PRIME for block in data[:69] for x in block])
                        old_sources.append(self.r787.source(filename))
                    rhs = nmod_mat(columns, PRIME).transpose()
                    small_rhs = submatrix(rhs, self.s5_rows, list(range(stop-first)))
                    solution = self.S5_inverse*small_rhs
                    assert self.S5*solution == rhs
                    assert submatrix(solution, self.extra5, list(range(stop-first))) == zero(len(self.extra5), stop-first)
                    normal = submatrix(solution, self.keep5, list(range(stop-first)))
                    value = self.put(name, {
                        "prime": PRIME, "original_V3_indices": [first, stop],
                        "normal_row_mapping": [list(x) for x in self.pos3],
                        "normal_coefficients_mod_prime": rows(normal),
                        "source_original_real_V5_rows": old_sources,
                        "source_original_S5_matrix": self.r842.source(S5_MATRIX),
                        "source_original_S5_inverse": self.r827.source(S5_INVERSE),
                        "source_original_alias_audit": self.audit_spec,
                        "original_source_integer_scale": str(82**10),
                        "all1380_original_equations_verified": True,
                        "all_extra_weight5_coordinates_zero": True,
                        "original_tau_squared_products_or_phase_conversion_recomputed": False,
                        "exact_unit_solve_expression": {
                            "operation": "solve_original_S5_selected_rows_for_tau_squared_times_original_V3",
                            "original_V3_indices": [first, stop], "original_V5_alias_indices": [first, stop],
                            "source_original_S5_basis": self.r809.source(S5_INDEX),
                            "selected_rows": self.s5_rows, "kept_S5_positions": self.keep5,
                            "quotient_by_tau_power": 3, "no_additional_scale": True},
                    })
                    del columns, rhs, small_rhs, solution, normal
                assert value["original_V3_indices"] == [first, stop]
                blocks.append(self.source(name))
            index = self.put(index_name, {
                "prime": PRIME, "dimension": V3, "normal_basis_rank": FREE,
                "normal_row_mapping": [list(x) for x in self.pos3], "blocks": blocks,
                "all690_rhs_and_all1380_equations_and_weighted_support_verified": True,
                "source_original_alias_audit": self.audit_spec,
                "same_prime_S5_inverse_recomputed": False,
            })
            self.S5 = self.S5_inverse = None
            gc.collect()
        matrix = [[0]*V3 for _ in range(V3)]
        expected_first = 0
        for item in blocks:
            assert plain(item) == spec(self.path(item["file"]))
            value = self.get(item["file"])
            first, stop = value["original_V3_indices"]
            assert first == expected_first and stop <= V3
            assert value["all1380_original_equations_verified"] is True
            assert value["all_extra_weight5_coordinates_zero"] is True
            L.checked_shape(value["normal_coefficients_mod_prime"], V3, stop-first)
            for i, row in enumerate(value["normal_coefficients_mod_prime"]):
                matrix[i][first:stop] = row
            expected_first = stop
        assert expected_first == V3
        self.normal = matrix
        self.normal_index_spec = self.source(index_name)
        return self.normal_index_spec

    def fiber(self, z0):
        name = "R839-pole-fiber-"+str(z0)+"-original-V3"
        value = self.get(name)
        point_name = "R827-prime-1000000753-z-"+str(z0)+"-Krylov.json.gz"
        point = self.r827.stage(point_name)
        if value is None:
            self.mark(name)
            data = [[0]*V3 for _ in range(FREE)]
            for i, (a, j) in enumerate(self.pos3):
                scalar = pow(z0, j, PRIME)
                if scalar:
                    data[a] = [(x+scalar*y) % PRIME for x, y in zip(data[a], self.normal[i])]
            E = nmod_mat(data, PRIME)
            Kinv = nmod_mat(point["inverse_Krylov_matrix_mod_prime"], PRIME)
            preimage = Kinv*E
            value = self.put(name, {
                "prime": PRIME, "z0": z0, "source_original_V3_normal_index": self.normal_index_spec,
                "source_original_Krylov_point": self.r827.source(point_name),
                "original_V3_evaluation_matrix_mod_prime": data,
                "original_V3_Krylov_coordinates_mod_prime": rows(preimage),
                "matrix_shape": [FREE, V3],
                "evaluation_uses_original_tau_cubic_trivialization": True,
                "old_inverse_recomputed": False,
                "fiber_not_assumed_reduced_or_disjoint_from_D": True,
            })
            del E, Kinv, preimage
        assert value["z0"] == z0
        assert value["source_original_V3_normal_index"] == self.normal_index_spec
        assert value["source_original_Krylov_point"] == self.r827.source(point_name)
        L.checked_shape(value["original_V3_evaluation_matrix_mod_prime"], FREE, V3)
        L.checked_shape(value["original_V3_Krylov_coordinates_mod_prime"], FREE, V3)
        return value, self.source(name), point

    def candidate(self, parameter):
        name = "R839-pole-candidate-"+str(parameter).zfill(6)+"-sections"
        value = self.get(name)
        if value is None:
            self.mark(name)
            weights = [pow(parameter, j, PRIME) for j in range(295)]
            b = self.kernel*nmod_mat([[v] for v in weights], PRIME)
            a = [int(self.kernel[i, 0]) for i in range(V3)]
            bc = [int(b[i, 0]) for i in range(V3)]
            assert a[self.free_columns[0]] == 1
            assert [bc[i] for i in self.free_columns] == weights
            value = self.put(name, {
                "prime": PRIME, "integer_parameter": parameter,
                "source_complete_original_D_basis": self.r842.source(D_KERNEL),
                "a_original_V3_coordinates_mod_prime": a,
                "b_original_V3_coordinates_mod_prime": bc,
                "a_exact_D_basis_column": 0,
                "b_exact_D_basis_coefficients": {"formula": "integer_parameter^j", "integer_parameter": parameter, "j_range": [0, 295]},
                "all_original_free_coordinates_verified": True,
                "a_and_b_are_the_original_unit_solve_sections": True,
                "extra_rescaling_or_reconstruction_used": False,
            })
        assert value["integer_parameter"] == parameter
        assert value["source_complete_original_D_basis"] == self.r842.source(D_KERNEL)
        return value, self.source(name)

    def product(self, which, parameter, candidate, candidate_source, z0):
        if which == "a":
            name = "R839-pole-fixed-a-fiber-"+str(z0)+"-times-V3"
        else:
            name = "R839-pole-candidate-"+str(parameter).zfill(6)+"-b-fiber-"+str(z0)+"-times-V3"
        value = self.get(name)
        evaluation, evaluation_source, point = self.fiber(z0)
        if value is None:
            self.mark(name)
            E = nmod_mat(evaluation["original_V3_evaluation_matrix_mod_prime"], PRIME)
            coefficients = candidate[which+"_original_V3_coordinates_mod_prime"]
            vector = E*nmod_mat([[x] for x in coefficients], PRIME)
            W = nmod_mat(point["W_evaluated_mod_prime"], PRIME)
            current = vector
            columns = []
            for k in range(FREE):
                self.budget()
                columns.append([int(current[i, 0]) for i in range(FREE)])
                if k+1 < FREE:
                    current = W*current
            K_section = nmod_mat(columns, PRIME).transpose()
            coordinates = nmod_mat(evaluation["original_V3_Krylov_coordinates_mod_prime"], PRIME)
            result = K_section*coordinates
            value = self.put(name, {
                "prime": PRIME, "z0": z0, "which": which,
                "integer_parameter": None if which == "a" else parameter,
                "source_original_fiber_evaluation": evaluation_source,
                "source_original_Krylov_point": evaluation["source_original_Krylov_point"],
                "source_complete_original_D_basis": self.r842.source(D_KERNEL),
                "source_candidate_sections": None if which == "a" else candidate_source,
                "a_exact_D_basis_column": 0 if which == "a" else None,
                "section_evaluation_mod_prime": [int(vector[i, 0]) for i in range(FREE)],
                "product_evaluation_matrix_mod_prime": rows(result),
                "matrix_shape": [FREE, V3],
                "exact_evaluation_formula": "[v,Wv,...,W^271v]*(old_K_inverse*original_V3_evaluation)",
                "old_Krylov_inverse_or_global_multiplication_table_recomputed": False,
                "fixed_a_product_independent_of_candidate_parameter": which == "a",
            })
            del E, vector, W, current, columns, K_section, coordinates, result
        assert value["which"] == which and value["z0"] == z0
        assert value["source_original_fiber_evaluation"] == evaluation_source
        assert value["source_complete_original_D_basis"] == self.r842.source(D_KERNEL)
        if which == "b":
            assert value["source_candidate_sections"] == candidate_source and value["integer_parameter"] == parameter
        L.checked_shape(value["product_evaluation_matrix_mod_prime"], FREE, V3)
        return value, self.source(name)

    def trial(self, parameter):
        candidate, candidate_source = self.candidate(parameter)
        name = "R839-pole-candidate-"+str(parameter).zfill(6)+"-five-fiber-rank"
        value = self.get(name)
        if value is None:
            data, sources = [], []
            for z0 in NODES:
                left, left_source = self.product("a", parameter, candidate, candidate_source, z0)
                right, right_source = self.product("b", parameter, candidate, candidate_source, z0)
                data.extend([a+b for a, b in zip(left["product_evaluation_matrix_mod_prime"], right["product_evaluation_matrix_mod_prime"])])
                sources.append({"z0": z0, "a": left_source, "b": right_source})
            self.mark(name)
            matrix = nmod_mat(data, PRIME)
            reduced, rank = matrix.rref()
            assert rank <= 1111, "Original D containment gives the characteristic-zero rank upper bound1111."
            value = {
                "prime": PRIME, "integer_parameter": parameter, "matrix_shape": [1360, 1380],
                "source_candidate_sections": candidate_source, "source_fiber_products": sources,
                "actual_rank": rank, "required_rank": 1111,
                "original_D_pencil_certified": rank == 1111,
                "rank_deficiency_is_only_failure_of_this_sufficient_residue_test": rank != 1111,
                "no_injectivity_of_fiber_evaluation_or_disjointness_from_D_assumed": True,
            }
            if rank == 1111:
                columns = pivots(reduced, rank)
                selected = submatrix(matrix, list(range(1360)), columns)
                second, second_rank = selected.transpose().rref()
                assert second_rank == rank
                indices = pivots(second, rank)
                minor = submatrix(matrix, indices, columns)
                determinant = int(minor.det())
                assert determinant
                value.update({
                    "selected_original_fiber_rows": indices,
                    "selected_original_V3_pair_columns": columns,
                    "actual_minor_determinant_mod_prime": determinant,
                    "characteristic_zero_rank_lower_bound": 1111,
                    "geometric_rank_upper_bound": 1111,
                    "additional_common_zero_divisor_degree": 0,
                    "image_is_exactly_H0_6H_minus_original_D": True,
                })
                del selected, second, minor
            self.put(name, value)
            value = self.get(name)
            del data, matrix, reduced
            gc.collect()
        assert value["source_candidate_sections"] == candidate_source
        self.last_trial, self.actual_rank = parameter, value["actual_rank"]
        return value, self.source(name), candidate_source

    def ideals(self, parameter, rank, rank_source, candidate_source):
        name = "R839-pole-original-D-and-Ey-eight-generator-DAG"
        value = self.get(name)
        assert rank["original_D_pencil_certified"] is True and rank["actual_rank"] == 1111
        if value is None:
            self.mark(name)
            sections = {
                "a": {"operation": "original_D_unit_kernel_basis_column", "basis_source": self.r842.source(D_KERNEL), "column": 0},
                "b": {"operation": "integer_moment_curve_combination_of_original_D_unit_kernel_basis", "basis_source": self.r842.source(D_KERNEL), "integer_parameter": parameter, "j_range": [0, 295]},
                "u": {"operation": "original_fixed_branch_anchor", "source": self.r837.source(self.anchor_sources["u"])},
                "v": {"operation": "original_fixed_branch_anchor", "source": self.r837.source(self.anchor_sources["v"])},
            }
            products = [{"fixed_anchor": anchor, "a_exponent": 3-j, "b_exponent": j, "homogeneous_degree": 11}
                        for anchor in ("u", "v") for j in range(4)]
            value = self.put(name, {
                "prime": PRIME, "integer_parameter": parameter,
                "source_actual_pencil_rank": rank_source, "source_candidate_sections": candidate_source,
                "source_original_fixed_branch_pencil_certificate": self.r837.source(self.r837.item["certificate_name"]),
                "sections": sections,
                "D_ideal_generators": {"tau": ["a/tau^3", "b/tau^3"], "sigma": ["a/sigma^3", "b/sigma^3"]},
                "Ey_homogeneous_generators": products,
                "Ey_chart_denominator_degrees": {"tau": 11, "sigma": 11},
                "overlap_coordinate": "t=tau/sigma",
                "D_chart_transition": "both generators multiply by t^3",
                "Ey_chart_transition": "all eight generators multiply by t^11",
                "accurate_divisor_identity": "E_y=f4_y_poles=fixed_21_branch_points+3*original_D",
                "accurate_ideal_identity": "I_Ey=I_fixed_branch*I_original_D^3",
                "original_D_degree": 395, "original_fixed_branch_degree": 21, "original_Ey_degree": 1206,
                "complete_original_D_ideal_certified": True,
                "complete_original_Ey_ideal_certified": True,
                "both_original_affine_chart_trivializations_preserved": True,
                "eight_source_bound_generators_supplied": True,
                "canonical_ideal_embedding_not_only_Picard_class": True,
                "unknown_scalar_or_new_cube_root_introduced": False,
                "expanded_V11_generator_coordinates_computed": False,
                "real_descent_pole_ideal_expression_supplied": False,
                "original_y_global_function_supplied_by_this_consumer": False,
                "Jacobian_standard_representative_computed": False,
                "actual_eta_or_height_computed": False,
                "existing_followup_identity": "I_EyR=(original_y^2-original_b)*I_Ey^3; requires the original global y DAG",
            })
        assert value["integer_parameter"] == parameter and value["source_actual_pencil_rank"] == rank_source
        self.accepted_parameter, self.complete = parameter, True
        return self.source(name)

    def inventory(self):
        entries = []
        for path in sorted(self.out.glob("R839-pole-*.json.gz")):
            if path.name == INVENTORY:
                continue
            value = read(path)
            assert value["complete"] is True and value["configuration"] == self.tag and value["result"] == RESULT
            entries.append(spec(path))
        save(self.out/INVENTORY, {"result": RESULT, "configuration": self.tag, "complete": True,
                                "files": entries, "inventory_does_not_list_itself": True})
        return spec(self.out/INVENTORY), len(entries)

    def finish(self, reason, error=None):
        ideal = self.get("R839-pole-original-D-and-Ey-eight-generator-DAG")
        if ideal is not None:
            self.complete, self.accepted_parameter = True, ideal["integer_parameter"]
            self.actual_rank = 1111
        manifest, count = self.inventory()
        complete = bool(ideal)
        certificate = {
            "result": RESULT, "configuration": self.tag, "complete": complete,
            "p": 41, "prime": PRIME, "original_branch": 0,
            "complete_original_D_pencil_certified": complete,
            "complete_original_Ey_ideal_certified": complete,
            "actual_pencil_rank": self.actual_rank, "accepted_integer_parameter": self.accepted_parameter,
            "last_completed_parameter": self.last_trial,
            "source_audit": self.source("R839-pole-original-source-and-alias-audit") if self.get("R839-pole-original-source-and-alias-audit") else None,
            "V3_normal_index": self.source("R839-pole-original-V3-normal-index") if self.get("R839-pole-original-V3-normal-index") else None,
            "pole_ideal_DAG": self.source("R839-pole-original-D-and-Ey-eight-generator-DAG") if ideal else None,
            "stage_manifest": manifest, "complete_math_stage_count": count,
            "maximum_trials_for_this_invocation": self.maximum_trials,
            "candidate_trial_limit_reached": not complete and reason == "finite_candidate_limit_reached",
            "stop_reason": reason, "error": error,
            "old_Fourier_products_S5_inverse_and_Krylov_inverses_recomputed": False,
            "expanded_characteristic_zero_coordinates_computed": False,
            "Jacobian_standard_representative_computed": False,
            "actual_eta_or_height_computed": False,
            "seconds": time.monotonic()-self.started,
        }
        save(self.out/FINAL, certificate)
        save(self.out/"core-receipt.json", {
            "result": RESULT, "source_sha256": sha(__file__), "complete": complete,
            "certificate_sha256": sha(self.out/FINAL),
            "complete_original_D_pencil_certified": complete,
            "complete_original_Ey_ideal_certified": complete,
            "actual_pencil_rank": self.actual_rank, "accepted_integer_parameter": self.accepted_parameter,
            "stop_reason": reason, "error": error, "seconds": time.monotonic()-self.started,
            "actual_eta_or_height_computed": False,
        })
        print(json.dumps({"complete": complete, "actual_pencil_rank": self.actual_rank,
                          "accepted_integer_parameter": self.accepted_parameter,
                          "stop_reason": reason, "seconds": certificate["seconds"]}), flush=True)
        return complete

    def run(self):
        self.audit()
        old = self.get("R839-pole-original-D-and-Ey-eight-generator-DAG")
        if old is not None:
            self.finish("reused_completed_original_pole_ideal_DAG")
            return 0
        self.normal_V3()
        for parameter in range(1, self.maximum_trials+1):
            rank, rank_source, candidate_source = self.trial(parameter)
            if rank["original_D_pencil_certified"]:
                self.ideals(parameter, rank, rank_source, candidate_source)
                assert self.finish("certified_original_D_pencil_and_eight_Ey_generators")
                return 0
        self.finish("finite_candidate_limit_reached")
        return 2


def main():
    L.guard()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, required=True)
    args = parser.parse_args()
    assert 0 < args.budget_minutes <= 300
    args.out.mkdir(parents=True, exist_ok=True)
    job = None
    try:
        job = Job(args)
        return job.run()
    except L.BudgetStop as exc:
        if job is not None:
            job.finish("budget_stop", str(exc))
        return 124
    except BaseException as exc:
        if job is not None:
            job.finish("arithmetic_or_source_error", type(exc).__name__+": "+str(exc))
        else:
            save(args.out/"core-receipt.json", {
                "result": RESULT, "source_sha256": sha(__file__), "complete": False,
                "error": type(exc).__name__+": "+str(exc), "phase": "initialization",
            })
        raise


if __name__ == "__main__":
    raise SystemExit(main())
