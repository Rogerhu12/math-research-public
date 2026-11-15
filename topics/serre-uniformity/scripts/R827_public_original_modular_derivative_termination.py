#!/usr/bin/env python3
"""R827 public source-bound IO and continuation runner.

Only standard-library IO is imported here.  Mathematical arithmetic is executed
by the separate frozen core inside this public repository's Actions.
"""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import signal
import subprocess
import sys
import tarfile

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R827-public-original-modular-derivative-termination-request.json"
RESULT = "R827-original-global-modular-derivative-termination"
FINAL = "p41-original-global-modular-derivative-termination-certificate.json"
BUNDLE = "R827-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
IO_NAME = "R824_public_original_global_polar_generators.py"
IO_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
POLY_SHA = "09f21a903e4906666d63f58575b389be7a04c20b68c7fcac624d3821837a9126"
LABELS = {"R806", "R813", "R820", "R824", "R809", "R787"}
EPS = [0]+[1]*144+[2]*127
MODE = "tau_polynomial_Hermite_and_sigma_infinity_rank"
FIELD_BASIS = "Q in the unchanged original K-normal basis"
R787_PREFIX = "R787-prime-1000000753-"
R824_BRANCH = "R824-power5-prime-1000000753-branch-00.json.gz"
R824_PROFILE = "R824-power6-selected-generator-profile.json.gz"
S5_INDEX = "R809-S5-basis-index.json.gz"
S5_MINOR = "R809-accepted-S5-short-minor.json.gz"
INT = re.compile(r"-?(0|[1-9][0-9]*)")
H64 = re.compile(r"[0-9a-f]{64}")


def sha(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            value.update(block)
    return value.hexdigest()


assert sha(S/IO_NAME) == IO_SHA
_loader = importlib.util.spec_from_file_location("R827_frozen_source_io", S/IO_NAME)
IO = importlib.util.module_from_spec(_loader)
_loader.loader.exec_module(IO)
read, save, file_spec = IO.read, IO.save, IO.file_spec
plain, check_spec, fingerprint = IO.plain, IO.check_spec, IO.fingerprint
Archive, extract_carrier = IO.Archive, IO.extract_carrier
META, BASE_KEYS = IO.META, IO.BASE_KEYS
topic_path = IO.topic_path


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("R827 mathematics belongs to this public repository's Actions.")


def cert_identity(item):
    if item.get("certificate") is not None:
        row = item["certificate"]
        return row["file"], row["sha256"]
    name = item.get("certificate_name")
    if name is None:
        return None
    digest = item.get("certificate_sha256")
    if digest is None:
        digest = item["files"][name]
    return name, digest


def same_identity(left, right):
    for key in BASE_KEYS:
        assert str(left[key]) == str(right[key]), ("Changed original producer", key)
    first, second = cert_identity(left), cert_identity(right)
    if first is not None and second is not None:
        assert first == second


def identity(item):
    return IO.identity(item)


def stage_identity(source):
    value = {key: source.item[key] for key in BASE_KEYS}
    name = source.item.get("certificate_name")
    if name is not None:
        value["certificate"] = plain(source.files[name])
    return value


class Producer(IO.Producer):
    """Complete source or explicitly bound, ended R809/R787 checkpoint."""
    def __init__(self, label, item, directory, archive=None):
        if label == "R787" or item.get("certificate_name") is not None:
            super().__init__(label, item, directory, archive)
        else:
            assert label == "R809" or label.startswith("shared/")
            assert item.get("allow_completed_checkpoint") is True
            assert item["expected_conclusion"] == "failure"
            anchor = item["configuration_stage"]
            assert Path(anchor).name == anchor
            if label == "R809":
                assert anchor == S5_INDEX
            self.label, self.item, self.directory, self.archive = label, item, Path(directory), archive
            self.directory.mkdir(parents=True, exist_ok=True)
            self.selected = {}
            path = self.materialize(META[0], item["manifest_sha256"])
            self.manifest = read(path)
            assert self.manifest["result"] == item["result"]
            self.files = {row["file"]: row for row in self.manifest["files"]}
            assert len(self.files) == len(self.manifest["files"])
            for row in self.files.values():
                check_spec(row)
            run, core, initial = (self.raw(name) for name in META[1:])
            assert run["result"] == core["result"] == initial["result"] == item["result"]
            assert str(run["workflow_run_id"]) == str(item["run_id"])
            assert run["source_commit"] == initial["source_commit"] == item["source_commit"]
            assert initial["source_repository"] == "Rogerhu12/math-research-public"
            assert initial["core_sha256"] == initial["job"]["core_sha256"] == item["core_sha256"]
            assert core["source_sha256"] == item["core_sha256"]
            assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
            assert run["complete"] is False and run["process_exit_code"] != 0
            assert core["complete"] is False
            assert anchor in item["files"]
            index = self.raw(anchor)
            assert index["complete"] is True
            self.certificate, self.initial, self.tag = None, initial, index["configuration"]
            assert self.tag["source_sha256"] == item["core_sha256"]
            assert self.tag["python_flint"] == "0.9.0"
        if self.certificate is None:
            permitted = item.get("accepted_checkpoint_exit_codes", [124])
            assert 0 not in permitted
            assert self.raw("run-receipt.json")["process_exit_code"] in permitted
        self.inventory = None
        if self.certificate is not None:
            entry = self.certificate.get("stage_manifest", self.certificate.get("stages_manifest"))
            if entry is not None:
                data = self.stage(entry)
                self.inventory = {row["file"]: plain(row) for row in data["files"]}
                assert len(self.inventory) == len(data["files"])
                for name, row in self.inventory.items():
                    assert row == plain(self.files[name])

    def indexed(self, entry):
        if isinstance(entry, str):
            entry = self.files[entry]
        if self.inventory is not None:
            assert self.inventory[entry["file"]] == plain(entry)
        return self.stage(entry)


def integer_rows(rows, count, width):
    assert len(rows) == count and all(len(row) == width for row in rows)
    for row in rows:
        for value in row:
            assert isinstance(value, str) and INT.fullmatch(value) and value != "-0"


def modular_rows(rows, count, width, prime=1000000753):
    assert len(rows) == count and all(len(row) == width for row in rows)
    assert all(isinstance(value, int) and 0 <= value < prime for row in rows for value in row)


def rational_pair(pair):
    assert len(pair) == 2
    assert all(isinstance(value, str) and INT.fullmatch(value) for value in pair)
    assert int(pair[1]) > 0


def select_W_and_derivation_inputs(producers):
    r806, r813 = producers["R806"], producers["R813"]
    c806, c813 = r806.certificate, r813.certificate
    assert r806.item["result"] == "R806-original-primitive-multiplication"
    assert r813.item["result"] == "R813-original-Wronskian-derivation-inputs"
    assert r806.item["core_sha256"] == "b014f9b3cb4923421e6a879eddb4da58dd0baefb28d61a2191f6b0a33e51810d"
    assert r813.item["core_sha256"] == "830ae652ebb08a035c6636c7738ab4823322111944932ffc77b1136caf7a07bc"
    assert c806["normal_affine_basis_rank"] == 272
    for key in ("exact_polynomial_multiplication_computed", "all272_columns_verified_in_all820_original_rows",
                "actual_cyclic_minor_certified", "original_function_field_primitive_generator_certified",
                "normal_integral_basis_preserved"):
        assert c806[key] is True
    assert [int(x) for x in c806["actual_w0_original_M2_integer_coordinates"]] == [int(i == 2) for i in range(146)]
    assert c813["completed_scope"] == "two_original_S3_Wronskian_inputs"
    assert c813["target_names"] == ["g", "h"] and c813["actual_rational_RHS_columns"] == 2
    assert c813["S3_basis_dimension"] == 690 and c813["qY_count"] == 41
    assert c813["full_coordinate_rows"] == 820
    assert c813["normal_basis_rank"] == 272 and c813["normal_basis_degrees"] == EPS
    assert c813["regular_degree_bound"] == 3 and c813["original_D0_qY_multiplier"] == ["1", "82"]
    for key in ("all820_original_coordinates_verified_for_both_targets",
                "both_original_normal_vectors_actually_nonzero",
                "original_1_over82_and_all_integer_scales_preserved"):
        assert c813[key] is True
    assert c813["actual_Mg_Mh_or_Gamma_computed"] is False
    same_identity(r813.tag["producer_identities"]["R806"], r806.item)
    same_identity(r813.tag["producer_identities"]["R805"], r806.tag["retained_artifacts"]["R805"])
    assert c813["actual_sigma_integer_n"] == r806.tag["actual_sigma_integer_n"]
    interface = r806.indexed(c806["polynomial_multiplier"])
    assert interface["coordinate_groups"] == c806["exact_coordinate_groups"]
    assert interface["normal_affine_basis_rank"] == 272 and interface["normal_affine_basis_degrees"] == EPS
    assert interface["original_R805_free_basis"] == r813.tag["original_graded_free_basis"]
    assert interface["original_R805_S_basis_index"] == r813.tag["original_S3_basis_index"]
    assert interface["coefficient_field"] == "Q, certified by exact original rational coordinate equations"
    assert interface["matrix_convention"] == "M_ba(z) is output row b, input column a"
    for key in ("all272_columns_verified_in_all820_original_rows", "all_weighted_support_zeros_verified",
                "reduction_equals_successful_modular_multiplier",
                "original_function_field_primitive_generator_certified", "normal_integral_basis_preserved"):
        assert interface[key] is True
    columns = []
    for entry in interface["coordinate_groups"]:
        group = r806.indexed(entry)
        indices = group["column_indices"]
        assert len(group["coordinate_numerators"]) == 690
        assert all(len(row) == len(indices) for row in group["coordinate_numerators"])
        assert len(group["column_denominators"]) == len(indices)
        assert group["integer_scale"] == str(82**6)
        assert group["all820_original_coordinates_verified"] is True
        assert group["weighted_polynomial_support_verified"] is True
        assert group["reduction_equals_successful_modular_multiplier"] is True
        columns.extend(indices)
    assert columns == list(range(272))
    witness = r806.indexed(interface["actual_cyclic_witness"])
    assert witness["actual_cyclic_rank"] == 272 and witness["actual_determinant_mod_prime"] != 0
    assert witness["candidate_index"] == interface["candidate_index"]
    assert witness["primitive_generator_certified_by_actual_minor"] is True
    assert len(witness["successful_krylov_matrix_mod_prime"]) == 272
    assert all(len(row) == 272 for row in witness["successful_krylov_matrix_mod_prime"])
    chart = r806.indexed(c806["coordinate_chart"])
    accepted = r806.indexed(c806["accepted_candidate"])
    assert chart["original_R805_free_basis"] == interface["original_R805_free_basis"]
    assert accepted["cyclic_witness"] == interface["actual_cyclic_witness"]
    definition_name = "R806-candidate-"+str(interface["candidate_index"]).zfill(10)+"-definition.json.gz"
    definition = r806.indexed(plain(r806.files[definition_name]))
    assert definition["candidate_index"] == interface["candidate_index"]
    coordinate_spec = c813["exact_coordinate_stage"]
    coordinates = r813.indexed(coordinate_spec)
    assert coordinates["target_names"] == ["g", "h"] and coordinates["column_indices"] == [0, 1]
    assert coordinates["S3_basis_dimension"] == 690 and coordinates["normal_basis_rank"] == 272
    assert coordinates["full_coordinate_rows"] == 820 and coordinates["original_S3_integer_scale"] == str(82**6)
    assert coordinates["original_D0_qY_multiplier"] == ["1", "82"]
    for key in ("all820_original_coordinates_verified", "both_original_Wronskians_actually_nonzero",
                "original_1_over82_and_all_integer_scales_preserved"):
        assert coordinates[key] is True
    assert len(coordinates["coordinate_numerators"]) == 690
    assert all(len(row) == 2 for row in coordinates["coordinate_numerators"])
    assert len(coordinates["column_denominators"]) == len(coordinates["original_target_rational_scales"]) == 2
    assert coordinates["original_target_rational_scales"] == [["6724", "1"], ["6724", "1"]]
    assert all(int(d) > 0 for d in coordinates["column_denominators"])
    assert all(len(pair) == 2 and int(pair[1]) > 0 and int(pair[0]) != 0
               for pair in coordinates["original_target_rational_scales"])
    normal_spec = c813["normal_vector_interface"]
    normal = r813.indexed(normal_spec)
    assert normal["target_column_indices"] == {"g": 0, "h": 1}
    assert normal["source_exact_S3_coordinates"] == coordinate_spec
    assert normal["normal_basis_rank"] == 272 and normal["normal_basis_degrees"] == EPS
    assert normal["regular_degree_bound"] == 3 and normal["coefficient_field"] == FIELD_BASIS
    assert normal["actual_R806_polynomial_multiplier_index"] == c806["polynomial_multiplier"]
    assert normal["actual_R806_primitive_candidate"] == c806["accepted_candidate"]
    assert normal["original_R805_graded_free_basis"] == interface["original_R805_free_basis"]
    assert normal["all820_original_coordinates_verified"] is True
    assert normal["original_1_over82_and_all_integer_scales_preserved"] is True
    assert normal["actual_Mg_Mh_or_Gamma_computed"] is False
    mapping = normal["S3_row_to_polynomial_coefficient"]
    assert len(mapping) == 690
    for index, row in enumerate(mapping):
        if index < 4:
            basis, power = 0, index
        elif index < 436:
            basis, power = 1+(index-4)//3, (index-4) % 3
        else:
            basis, power = 145+(index-436)//2, (index-436) % 2
        assert row == {"S_row": index, "normal_basis_row": basis, "power_of_z": power}
    return {
        "R806_polynomial_multiplier": c806["polynomial_multiplier"],
        "R806_cyclic_witness": interface["actual_cyclic_witness"],
        "R806_exact_coordinate_groups": interface["coordinate_groups"],
        "R806_original_free_basis": interface["original_R805_free_basis"],
        "R813_exact_coordinate_stage": coordinate_spec, "R813_normal_vector_interface": normal_spec,
        "original_R813_rational_scales": coordinates["original_target_rational_scales"],
        "original_input_columns": ["g", "h"], "actual_operator_targets": ["g", "Gamma"],
        "old_Fourier_Wronskian_or_S3_rows_selected_for_recomputation": False}




def select_cusp_columns(producers):
    p, w = producers["R820"], producers["R806"]
    cert = p.certificate
    assert cert["result"] == "R820-original-cusp-finite-algebra-and-ideals"
    assert cert["normal_basis_rank"] == 272 and cert["normal_basis_degrees"] == EPS
    assert cert["finite_field_degree"] == 20
    assert cert["actual_cusp_colengths"] == {"tau": 20, "sigma": 20}
    for key in ("original_two_chart_cusp_ideals_computed",
                "complete_polynomial_kernels_certified",
                "same_original_cusp_field_and_two_chart_transitions_verified"):
        assert cert[key] is True
    same_identity(p.tag["producer_identities"]["R806"], w.item)
    same_identity(p.tag["producer_identities"]["R805"], w.tag["retained_artifacts"]["R805"])
    interface = w.indexed(w.certificate["polynomial_multiplier"])
    assert p.tag["original_R805_free_basis"] == interface["original_R805_free_basis"]
    assert p.tag["original_R805_S3_index"] == interface["original_R805_S_basis_index"]
    assert p.tag["original_R806_Q_primitive_multiplier"] == w.certificate["polynomial_multiplier"]
    assert p.tag["actual_pencil_n"] == w.tag["actual_sigma_integer_n"] == 1
    answer = {}
    for chart in ("tau", "sigma"):
        entry = cert["two_chart_cusp_ideal_indexes"][chart]
        index = p.indexed(entry)
        assert index["chart"] == chart and index["normal_basis_rank"] == 272
        assert index["normal_basis_degrees"] == EPS
        assert index["actual_reachable_rank"] == index["actual_total_diagonal_degree"] == 20
        assert index["actual_diagonal_degrees"] == [0]*271+[20]
        for key in ("all_272_original_relations_verified_in_full_finite_algebra",
                    "canonical_lower_triangular_monic_and_reduced_conditions_verified",
                    "complete_polynomial_kernel_certified_by_inclusion_and_equal_colength",
                    "quotient_is_original_separable_cusp_field"):
            assert index[key] is True
        columns = index["Hermite_columns_in_original_basis_order"]
        assert len(columns) == 272
        p.prefetch(row["file"] for row in columns)
        for a, row in enumerate(columns):
            column = p.indexed(row)
            assert column["chart"] == chart and column["normal_basis_index"] == a
            assert column["kind"] == "first_dependence"
            assert column["first_dependent_power"] == index["actual_diagonal_degrees"][a]
            assert column["complete_relation_evaluation_zero_in_all_20_original_coordinates"] is True
            terms = column["column_terms"]
            seen, diagonal = set(), 0
            for term in terms:
                b, exponent = term["normal_basis_row"], term["power"]
                assert isinstance(b, int) and a <= b < 272
                assert isinstance(exponent, int) and exponent >= 0
                assert (b, exponent) not in seen
                seen.add((b, exponent))
                rational_pair(term["coefficient"])
                assert int(term["coefficient"][0]) != 0
                if b == a and exponent == index["actual_diagonal_degrees"][a]:
                    assert term["coefficient"] == ["1", "1"]
                    diagonal += 1
                else:
                    assert b == 271 and exponent < 20
            assert diagonal == 1
        answer[chart] = {"index": plain(entry), "column_count": len(columns),
                         "actual_colength": 20, "original_basis_order_preserved": True}
    return answer


def select_original_B_and_rows(producers):
    source, old = producers["R824"], producers["R787"]
    cert = source.certificate
    assert cert["result"] == "R824-original-global-polar-generators"
    assert "modular_generator_profile" in cert["completed_requested_scopes"]
    assert cert["original_R787_reserved_target_recomputed"] is False
    assert cert["new_weight7_or_Laurent_tail_computed"] is False
    same_identity(source.tag["source_identities"]["R787"], old.item)
    assert source.tag["original_map_index"] == old.tag["original_map_index"] == 4
    assert source.tag["original_map_degree"] == 1206 and old.tag["original_map_degree"] == "1206"
    assert source.tag["field"] == old.tag["field"]
    field = source.tag["field"]
    original_b_polynomial = field["original_b_minimal_polynomial"]
    assert set(original_b_polynomial) == {"numerator", "denominator"}
    assert len(original_b_polynomial["numerator"]) == 8
    assert int(original_b_polynomial["denominator"]) > 0
    assert len(field["integral_B_minimal_polynomial"]) == 8
    assert isinstance(field["lambda"], str) and INT.fullmatch(field["lambda"])
    assert int(field["lambda"]) > 0 and field["original_b_replaced_by_another_twist"] is False
    assert source.tag["original_integer_scales"]["5"] == old.tag["basis_integer_scale"] == str(82**10)
    assert source.tag["reserved_R787_free_column"] == 1186
    assert source.tag["generator_profile_weights_5_6_7"] == [28, 244, 0]
    for name, digest in IO.PINNED_OLD.items():
        assert old.files[name]["sha256"] == digest
    old.prefetch(IO.PINNED_OLD)
    selection = old.indexed(R787_PREFIX+"selection.json.gz")
    old_chart = old.indexed(R787_PREFIX+"chart.json.gz")
    block = old.indexed(R787_PREFIX+"rational-blocks.json.gz")
    old_branch = old.indexed(R787_PREFIX+"branch-00.json.gz")
    assert selection["prime"] == 1000000753
    assert selection["all_14_L_branches_distinct"] is True
    assert selection["all_rational_denominators_units"] is True
    assert selection["all_kappa_reductions_invertible"] is True
    assert len(selection["roots_B_s"]) == 14 and selection["roots_B_s"][0] == [3197390, 99932770]
    assert old_chart["actual_modular_rank"] == 1186 and old_chart["chosen_free_column"] == 1186
    assert len(old_chart["pivot_rows"]) == len(old_chart["pivot_columns"]) == 1186
    assert block["A_minor_det_mod_prime"] == 336446771
    assert block["B_constant_minor_det_mod_prime"] == 322380492
    assert block["exact_E0_Z_zero_verified"] is True
    assert len(block["B_constant_pivot_columns"]) == 20
    assert len(block["B_constant_free_columns"]) == 1214
    integer_rows(block["Z_pivot_integer_rows"], 20, 1214)
    assert INT.fullmatch(block["Z_free_diagonal"]) and int(block["Z_free_diagonal"]) != 0
    assert old_branch["selected_minor_det_mod_prime"] == 296007862
    assert old_branch["actual_Schur_rank"] == 1186 and old_branch["branch"] == 0
    assert old_branch["roots_B_s"] == selection["roots_B_s"][0]
    assert old_branch["all_2560_original_uncleared_rows_verified"] is True
    branch = source.indexed(R824_BRANCH)
    chart = source.indexed(branch["chart"])
    assert branch["ordinary_power"] == 5 and branch["prime"] == 1000000753
    assert branch["branch"] == 0 and branch["roots_B_s"] == selection["roots_B_s"][0]
    assert branch["actual_Schur_rank"] == 1186 and branch["selected_minor_det_mod_prime"] == 296007862
    assert branch["original_reserved_column_retained_without_new_lift"] is True
    assert branch["full_original_modular_relations_verified_for_all_new_free_targets"] is True
    assert plain(branch["rational_block"]) == plain(old.files[R787_PREFIX+"rational-blocks.json.gz"])
    assert plain(branch["original_branch_inverse_reused_from"]) == plain(old.files[R787_PREFIX+"branch-00.json.gz"])
    assert chart["prime"] == 1000000753 and chart["ordinary_power"] == 5
    assert chart["actual_rank"] == 1186 and chart["kernel_dimension"] == 28
    assert chart["chart_choice_from_original_R787"] is True
    assert plain(chart["original_chart"]) == plain(old.files[R787_PREFIX+"chart.json.gz"])
    assert chart["pivot_rows"] == old_chart["pivot_rows"] and chart["pivot_columns"] == old_chart["pivot_columns"]
    free = branch["kernel_free_columns"]
    assert len(free) == 28 and free == sorted(set(free)) and 1186 in free
    assert set(free).isdisjoint(set(chart["pivot_columns"]))
    assert set(free) | set(chart["pivot_columns"]) == set(range(1214))
    modular_rows(branch["kernel_A_mod_prime"], 1234, 28)
    modular_rows(branch["kernel_C_mod_prime"], 1214, 28)
    position = free.index(1186)
    assert [row[position] for row in branch["kernel_A_mod_prime"]] == old_branch["initial_A"]
    assert [row[position] for row in branch["kernel_C_mod_prime"]] == old_branch["initial_C"]
    profile = source.indexed(R824_PROFILE)
    assert len(profile["selected_weight6_free_columns"]) == 244
    assert len(set(profile["selected_weight6_free_columns"])) == 244
    assert profile["weight5_kernel_dimension"] == 28 and profile["weight6_kernel_dimension"] == 300
    assert profile["actual_lower_span_rank_in_each_branch"] == 56
    assert profile["exact_weight6_generators_claimed"] is False
    row_names = ["R787-real-power5-row-"+str(i).zfill(4)+".json.gz" for i in range(1234)]
    old.prefetch(row_names)
    for i, name in enumerate(row_names):
        data = old.indexed(name)
        assert data["index"] == i and data["all_original_phase_involutions_verified"] is True
        integer_rows(data["integer_t_coefficients"], 129, 20)
    return {"branch": plain(source.files[R824_BRANCH]),
        "chart": plain(branch["chart"]), "original_Schur_block": plain(branch["rational_block"]),
        "modular_profile": plain(source.files[R824_PROFILE]),
        "original_field": field, "original_roots_B_s": selection["roots_B_s"][0],
        "canonical_free_column": 1186, "retained_original_power5_rows": 1234,
        "original_row_orders_preserved": 129, "orders_selected_by_consumer": 69,
        "all_14_branches_mistaken_for_one_original_b_root": False,
        "original_R787_reserved_exact_lift_recomputed": False}


def select_S5_rows(producers):
    source, w = producers["R809"], producers["R806"]
    assert source.item["result"] == "R809-original-S5-normal-coordinates"
    assert source.item["core_sha256"] == "dedb5d6149a3c3ae86ad09e51f30c1424951a09010bf48afd948d2628e1ec21d"
    index = source.indexed(S5_INDEX)
    minor = source.indexed(S5_MINOR)
    rank = source.indexed(minor["actual_rank_stage"])
    interface = w.indexed(w.certificate["polynomial_multiplier"])
    same_identity(source.tag["basis_producers"]["R805"], w.tag["retained_artifacts"]["R805"])
    same_identity(source.tag["basis_producers"]["R786"],
                  producers["R787"].tag["retained_artifacts"]["R786"])
    assert source.tag["original_graded_free_basis"] == interface["original_R805_free_basis"]
    assert source.tag["actual_sigma_integer_n"] == w.tag["actual_sigma_integer_n"] == 1
    assert index["original_graded_free_basis"] == interface["original_R805_free_basis"]
    assert index["dimension"] == 1234 and index["qY_count"] == 69
    assert index["real_coordinate_count"] == 20 and index["full_coordinate_rows"] == 1380
    assert index["integer_scale"] == source.tag["basis_integer_scale"] == str(82**10)
    assert index["normal_affine_basis_rank"] == 272 and index["normal_basis_degrees"] == EPS
    assert index["all_original_term_phases_and_scales_verified"] is True
    assert len(index["basis_rows"]) == 1234
    assert minor["S5_basis_index"] == plain(source.files[S5_INDEX])
    assert minor["actual_rank"] == 1234 and minor["full_coordinate_rows"] == 1380
    assert minor["column_indices"] == list(range(1234))
    assert minor["minor_is_from_actual_69_term_matrix"] is True
    assert minor["actual_determinant_mod_prime"] != 0
    assert len(minor["row_indices"]) == 1234
    assert minor["row_indices"] == sorted(set(minor["row_indices"]))
    assert all(0 <= row < 1380 for row in minor["row_indices"])
    assert rank["S5_basis_index"] == minor["S5_basis_index"]
    assert rank["actual_rank"] == minor["actual_rank"]
    assert rank["row_indices"] == minor["row_indices"]
    assert rank["prime"] == minor["prime"]
    assert rank["actual_determinant_mod_prime"] == minor["actual_determinant_mod_prime"]
    mapping = [(a, j) for a, eps in enumerate(EPS) for j in range(6-eps)]
    assert len(mapping) == 1234
    source.prefetch(row["source"]["file"] for row in index["basis_rows"])
    for i, row in enumerate(index["basis_rows"]):
        a, j = mapping[i]
        assert row["index"] == i and row["normal_basis_index"] == a and row["z_degree"] == j
        assert row["normal_basis_degree"] == EPS[a]
        data = source.indexed(row["source"])
        assert data["index"] == i and data["recipe"] == row["recipe"]
        assert data["normal_basis_index"] == a and data["z_degree"] == j
        assert data["normal_basis_degree"] == EPS[a]
        assert data["integer_scale"] == str(82**10)
        assert data["qY_count"] == 69 and data["real_coordinate_count"] == 20
        assert data["all_original_term_phases_and_scales_verified"] is True
        assert data["original_R805_free_generator_unchanged"] is True
        integer_rows(data["integer_v_t_coefficients"], 69, 20)
    same_prime_inverse = None
    inverse_name = "R809-S5-fixed-modular-inverse.json.gz"
    if minor["prime"] == 1000000753 and inverse_name in source.files:
        inverse = source.indexed(inverse_name)
        assert inverse["prime"] == 1000000753
        assert inverse["minor_stage"] == plain(source.files[S5_MINOR])
        assert inverse["S5_basis_index"] == plain(source.files[S5_INDEX])
        assert inverse["inverse_product_exactly_verified_mod_prime"] is True
        modular_rows(inverse["inverse_mod_prime"], 1234, 1234)
        same_prime_inverse = plain(source.files[inverse_name])
    return {"S5_basis_index": plain(source.files[S5_INDEX]),
        "accepted_minor": plain(source.files[S5_MINOR]), "actual_rank_stage": plain(minor["actual_rank_stage"]),
        "same_prime_original_inverse": same_prime_inverse,
        "old_integer_row_count": 1234, "old_row_orders": 69, "old_Q_rows_recomputed": False,
        "partial_target_certificate_claimed": False,
        "ended_checkpoint_used": source.certificate is None}


def select_sources(producers):
    assert set(producers) == LABELS
    W = select_W_and_derivation_inputs(producers)
    C = select_cusp_columns(producers)
    B = select_original_B_and_rows(producers)
    S5 = select_S5_rows(producers)
    assert producers["R813"].tag["original_graded_free_basis"] == \
           producers["R806"].indexed(producers["R806"].certificate["polynomial_multiplier"])["original_R805_free_basis"]
    return {"W_and_original_derivation_inputs": W, "two_original_cusp_indexes": C,
            "original_B_residue_and_power5_rows": B, "original_S5_rows": S5,
            "new_mathematical_arithmetic_executed": False}



def cache_labels(item):
    specs = item.get("reusable_cache_producers", {})
    assert isinstance(specs, dict)
    assert all(re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", label) for label in specs)
    return {"shared/"+label: spec for label, spec in specs.items()}


def producer_item(item, label):
    return item["retained_sources"][label] if label in LABELS else cache_labels(item)[label]


def select_reusable_caches(item, caches, original):
    entries = item.get("reusable_stage_sources", [])
    assert isinstance(entries, list)
    selected, keys = [], set()
    W = original["R806"].indexed(original["R806"].certificate["polynomial_multiplier"])
    for entry in entries:
        role = entry["role"]
        assert role in ("Krylov_point", "operator_point", "operator_modular_image")
        assert entry["prime"] == 1000000753
        relative = PurePosixPath(entry["relative_path"])
        assert not relative.is_absolute() and ".." not in relative.parts and "\\" not in str(relative)
        assert len(relative.parts) == 3 and relative.parts[0] == "shared"
        label = "/".join(relative.parts[:2])
        assert label in caches
        source = caches[label]
        same_identity(entry["source_identity"], source.item)
        assert relative.name == entry["stage"]["file"]
        stage = source.indexed(entry["stage"])
        assert stage["prime"] == 1000000753
        same_identity(source.tag["R806_producer"], original["R806"].item)
        assert source.tag["R806_polynomial_multiplier"] == original["R806"].certificate["polynomial_multiplier"]
        assert source.tag["R806_cyclic_witness"] == W["actual_cyclic_witness"]
        assert source.tag["original_R805_free_basis"] == W["original_R805_free_basis"]
        assert source.tag["normal_basis_degrees"] == EPS
        key = role, entry.get("z0"), entry.get("target")
        assert key not in keys
        keys.add(key)
        if role != "operator_modular_image":
            assert isinstance(entry["z0"], int) and 0 <= entry["z0"] < 1000000753
            assert stage["z0"] == entry["z0"]
        support = []
        if role == "Krylov_point":
            shared = stage["shared_point_mathematical_identity"]
            same_identity(shared["R806_producer"], original["R806"].item)
            assert shared["R806_polynomial_multiplier"] == original["R806"].certificate["polynomial_multiplier"]
            assert shared["R806_cyclic_witness"] == W["actual_cyclic_witness"]
            assert shared["original_R805_free_basis"] == W["original_R805_free_basis"]
            assert shared["normal_basis_degrees"] == EPS
            assert stage["source_bound_external_cache_consumption_allowed"] is True
            assert stage["usable"] is bool(stage["actual_determinant_mod_prime"])
            if stage["usable"]:
                assert stage["actual_cyclic_rank"] == 272 and stage["both_inverse_products_verified"] is True
                modular_rows(stage["W_evaluated_mod_prime"], 272, 272)
                modular_rows(stage["inverse_Krylov_matrix_mod_prime"], 272, 272)
        else:
            target = entry["target"]
            assert target in ("g", "Gamma") and stage["target"] == target and stage["field_component"] == 0
            target_tag = stage["target_configuration"]
            same_identity(target_tag["R813_producer"], original["R813"].item)
            assert target_tag["source_R813_exact_coordinates"] == original["R813"].certificate["exact_coordinate_stage"]
            assert target_tag["source_R813_normal_interface"] == original["R813"].certificate["normal_vector_interface"]
            if role == "operator_point":
                modular_rows(stage["matrix_mod_prime"], 272, 272)
            else:
                degree = 3 if target == "g" else 2
                assert stage["regular_degree_bound"] == degree
                assert stage["all_modular_entries_interpolated_in_original_normal_basis"] is True
                assert stage["weighted_support_and_original_first_column_verified"] is True
                blocks = stage["interpolated_blocks"]
                assert len(blocks) == 17
                source.prefetch(row["file"] for row in blocks)
                for row, first in zip(blocks, range(0, 272, 16)):
                    data = source.indexed(row)
                    assert data["target"] == target and data["prime"] == 1000000753
                    assert data["target_configuration"] == target_tag
                    assert data["field_component"] == 0 and data["regular_degree_bound"] == degree
                    assert (data["row_first"], data["row_stop"]) == (first, min(first+16, 272))
                    assert data["weighted_support_and_original_first_column_verified"] is True
                    assert all(isinstance(value, int) and 0 <= value < 1000000753
                               for value in data["coefficients_mod_prime"])
                    support.append(plain(row))
        selected.append({"source_identity": identity(source.item),
            "role": role, "prime": 1000000753, "relative_path": str(relative),
            "stage": plain(entry["stage"]), "supporting_original_files": support,
            "original_configuration_and_bytes_preserved": True})
    assert set(caches) == {"/".join(PurePosixPath(entry["relative_path"]).parts[:2]) for entry in entries}
    return selected


def expected_configuration(item, producers):
    return {
        "result": RESULT, "source_sha256": item["core_sha256"], "python_flint": "0.9.0",
        "R827_proof_sha256": item["R827_proof_sha256"],
        "R827_method_sha256": item["R827_method_sha256"],
        "finite_helper_sha256": item["finite_helper_sha256"],
        "poly_framework_sha256": item["poly_framework_sha256"],
        "p": 41, "auxiliary_prime": 1000000753, "original_branch": 0,
        "canonical_free_column": 1186, "normal_basis_rank": 272,
        "normal_basis_degrees": EPS, "S5_dimension": 1234, "qY_count": 69,
        "full_coordinate_rows": 1380, "matrix_row_block_size": 16, "hermite_tile_size": 272,
        "source_identities": {label: stage_identity(producers[label]) for label in sorted(LABELS)},
        "original_field_coordinates": "B=lambda*b, s=1+2*zeta; exact original branch",
        "certification_mode": MODE,
        "requested_order_and_budget_excluded_from_mathematical_identity": True,
    }


def check_files(item):
    assert item["result"] == RESULT and item["p"] == 41
    assert item["producer_inputs_pending"] is False
    assert set(item["retained_sources"]) == LABELS
    assert item["auxiliary_prime"] == 1000000753 and item["original_branch"] == 0
    assert item["canonical_free_column"] == 1186
    assert isinstance(item["requested_derivative_order"], int) and 0 <= item["requested_derivative_order"] <= 1206
    assert item["matrix_row_block_size"] == 16 and item["hermite_tile_size"] == 272
    assert item["certification_mode"] == MODE
    assert item["core_sha256"] == sha(S/item["core"])
    assert item["wrapper_sha256"] == sha(__file__)
    assert item["io_helper"] == IO_NAME and item["io_helper_sha256"] == IO_SHA
    assert item["finite_helper_sha256"] == sha(S/item["finite_helper"])
    assert item["poly_framework_sha256"] == sha(S/item["poly_framework"]) == POLY_SHA
    assert item["R827_proof_sha256"] == sha(topic_path(item["proof"]))
    assert item["R827_method_sha256"] == sha(topic_path(item["method"]))
    assert item["R827_proof_sha256"] == "17e9c828e01e652b1a73281bf2249ae2b39133faae3cf22384a5fd6d6a3d4a71"
    assert isinstance(item.get("reusable_stage_sources", []), list)
    cache_labels(item)
    assert sha(REPO/"README.md") == item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md") == item["readme_sha256"]["topic"]
    for source in list(item["retained_sources"].values())+list(cache_labels(item).values()):
        assert H64.fullmatch(source["core_sha256"]) and H64.fullmatch(source["manifest_sha256"])
        assert H64.fullmatch(source["archive_sha256"]) and source["artifact_id"] > 0
        assert source["run_id"] and source["source_commit"]
    assert item["retained_sources"]["R787"]["certificate_name"] is None
    assert item["retained_sources"]["R787"]["expected_conclusion"] == "failure"


def read_parent_carrier_receipt(parent, original):
    name = "retained-inputs-receipt.json"
    receipt = parent.raw(name)
    assert receipt["result"] == parent.item["result"] and receipt["complete"] is True
    assert receipt["configuration"] == parent.tag
    assert receipt["all_selected_source_members_and_new_bundle_members_SHA_verified"] is True
    same_identity(parent.initial["job"]["retained_sources"]["R787"], original)
    group = receipt["producers"]["R787"]
    same_identity(group["identity"], original)
    files = {row["file"]: row for row in group["files"]}
    assert len(files) == len(group["files"])
    assert files["full-outputs-manifest.json"]["sha256"] == original["manifest_sha256"]
    bundle = receipt["bundle"]
    assert bundle["file"] == "R824-retained-producer-inputs.tar.gz"
    assert plain(bundle) == plain(parent.files[bundle["file"]])
    return receipt, files


def restore_R787_from_parent(parent, original, retained):
    receipt, files = read_parent_carrier_receipt(parent, original)
    names = set(META) | set(IO.PINNED_OLD) | {
        "R787-real-power5-row-"+str(i).zfill(4)+".json.gz" for i in range(1234)}
    assert names <= set(files)
    if all((retained/"R787"/name).is_file() and
           file_spec(retained/"R787"/name) == plain(files[name]) for name in names):
        return {"carrier": receipt["bundle"], "original_members_verified": len(names),
                "already_retained_exact_members_reused": True}
    row = receipt["bundle"]
    path = parent.materialize(row["file"], row["sha256"], row["bytes"])
    seen = extract_carrier(path, retained, {"R787": names}, {"R787": files})
    assert seen == {("R787", name) for name in names}
    parent.selected.pop(row["file"])
    path.unlink()
    return {"carrier": plain(row), "original_members_verified": len(seen),
            "already_retained_exact_members_reused": False,
            "nested_old_eight_producer_carrier_preserved_in_new_bundle": False}


def build_input_bundle(out, producers):
    rows = {label: source.closure_receipt() for label, source in sorted(producers.items())}
    temporary = out/(BUNDLE+".tmp")
    with temporary.open("wb") as stream:
        with gzip.GzipFile(fileobj=stream, mode="wb", mtime=0, compresslevel=2) as compressed:
            with tarfile.open(fileobj=compressed, mode="w|") as archive:
                for label, source in sorted(producers.items()):
                    for name, path in sorted(source.selected.items()):
                        info = archive.gettarinfo(str(path), arcname=label+"/"+name)
                        assert info.isfile()
                        info.uid = info.gid = 0
                        info.uname = info.gname = ""
                        info.mtime = 0
                        with path.open("rb") as raw:
                            archive.addfile(info, raw)
    temporary.replace(out/BUNDLE)
    verify_input_bundle(out/BUNDLE, rows)
    return rows, file_spec(out/BUNDLE)


def verify_input_bundle(bundle, producers, destination=None):
    expected = {(label, row["file"]): row for label, source in producers.items() for row in source["files"]}
    seen = set()
    with tarfile.open(bundle, "r|gz") as archive:
        for member in archive:
            assert member.isfile()
            path = PurePosixPath(member.name)
            assert len(path.parts) in (2, 3) and not path.is_absolute() and ".." not in path.parts
            assert len(path.parts) == 2 or path.parts[0] == "shared"
            assert "\\" not in member.name
            key = ("/".join(path.parts[:-1]), path.parts[-1])
            assert key in expected and key not in seen
            seen.add(key)
            row = expected[key]
            assert member.size == row["bytes"]
            count, digest, target, temporary, output = 0, hashlib.sha256(), None, None, None
            if destination is not None:
                target = Path(destination)/path
                target.parent.mkdir(parents=True, exist_ok=True)
                temporary = target.with_name(target.name+".download")
                output = temporary.open("wb")
            try:
                with archive.extractfile(member) as raw:
                    for block in iter(lambda: raw.read(4*1024*1024), b""):
                        count += len(block)
                        digest.update(block)
                        if output is not None:
                            output.write(block)
            finally:
                if output is not None:
                    output.close()
            assert count == row["bytes"] and digest.hexdigest() == row["sha256"]
            if temporary is not None:
                if target.exists():
                    assert file_spec(target) == plain(row)
                    temporary.unlink()
                else:
                    temporary.replace(target)
    assert seen == set(expected)
    return len(seen)


def restore(item, out, retained):
    previous = item.get("resume")
    if previous is None:
        return None
    assert previous["result"] == RESULT and previous["core_sha256"] == item["core_sha256"]
    archive = Archive(previous, out.parent/"resume-download", whole=True)
    try:
        staging = out.parent/"resume-metadata"
        staging.mkdir(parents=True, exist_ok=True)
        path = archive.extract_bound(META[0], previous["manifest_sha256"], staging/META[0])
        manifest = read(path)
        assert manifest["result"] == RESULT
        files = archive.verify_all(manifest)
        def old_file(name):
            row = files[name]
            return archive.extract_bound(name, row["sha256"], staging/name, row["bytes"])
        initial = read(old_file("public-actions-input.json"))
        old_item = initial["job"]
        assert initial["source_commit"] == previous["source_commit"]
        assert initial["core_sha256"] == item["core_sha256"]
        for key in ("core_sha256", "R827_proof_sha256", "R827_method_sha256",
                    "finite_helper_sha256", "poly_framework_sha256", "certification_mode",
                    "auxiliary_prime", "original_branch", "canonical_free_column",
                    "matrix_row_block_size", "hermite_tile_size"):
            assert old_item[key] == item[key]
        assert old_item["requested_derivative_order"] <= item["requested_derivative_order"]
        for label in LABELS:
            assert identity(old_item["retained_sources"][label]) == identity(item["retained_sources"][label])
        run, core = (read(old_file(name)) for name in ("run-receipt.json", "core-receipt.json"))
        assert run["result"] == core["result"] == RESULT
        assert run["source_commit"] == previous["source_commit"]
        assert str(run["workflow_run_id"]) == str(previous["run_id"])
        assert run["core_receipt_sha256"] == files["core-receipt.json"]["sha256"]
        assert core["source_sha256"] == item["core_sha256"]
        if run["complete"] is False:
            assert old_item["requested_derivative_order"] == item["requested_derivative_order"], \
                "Complete the current requested order before appending a larger order."
        receipt = read(old_file("retained-inputs-receipt.json"))
        assert receipt["result"] == RESULT and receipt["complete"] is True
        assert set(receipt["producers"]) == LABELS | set(cache_labels(old_item))
        assert set(cache_labels(old_item)) <= set(cache_labels(item))
        for label in cache_labels(old_item):
            assert identity(producer_item(old_item, label)) == identity(producer_item(item, label))
        assert {fingerprint(row) for row in old_item.get("reusable_stage_sources", [])} <= \
               {fingerprint(row) for row in item.get("reusable_stage_sources", [])}
        for label, group in receipt["producers"].items():
            assert group["identity"] == identity(producer_item(old_item, label))
        bundle = old_file(BUNDLE)
        assert plain(receipt["bundle"]) == plain(files[BUNDLE])
        members = verify_input_bundle(bundle, receipt["producers"], retained)
        restored = []
        for name, row in files.items():
            if not name.startswith("R827-") or name == BUNDLE:
                continue
            assert name.endswith((".json.gz", ".tar")), ("Unexpected mathematical stage type", name)
            assert not name.endswith((".tmp", ".download", ".partial"))
            target = archive.extract_bound(name, row["sha256"], out/name, row["bytes"])
            if name.endswith(".json.gz"):
                data = read(target)
                assert data["configuration"] == receipt["configuration"]
                assert isinstance(data["complete"], bool)
            restored.append(plain(row))
        result = {"result": RESULT, "resumed": True, "previous": previous,
            "previous_configuration": receipt["configuration"],
            "whole_previous_ZIP_and_all_manifest_members_SHA_verified": True,
            "all_previous_manifest_files_verified": len(files),
            "all_previous_input_bundle_members_verified": members,
            "restored_complete_or_atomic_current_files": restored,
            "no_completed_Hermite_or_operator_arithmetic_repeated_by_IO": True,
            "archive": archive.receipt()}
        save(out/"resume-receipt.json", result)
        return result
    finally:
        archive.close()


def prepare(item, out):
    check_files(item)
    out.mkdir(parents=True, exist_ok=True)
    retained = out.parent/"retained"
    retained.mkdir(parents=True, exist_ok=True)
    resumed = restore(item, out, retained)
    sources, archives, carrier = {}, {}, None
    try:
        if resumed is None:
            for label in ("R806", "R813", "R820", "R824", "R809"):
                source_item = item["retained_sources"][label]
                archive = Archive(source_item, out.parent/("download-"+label))
                archives[label] = archive
                sources[label] = Producer(label, source_item, retained/label, archive)
            carrier = restore_R787_from_parent(sources["R824"], item["retained_sources"]["R787"], retained)
            sources["R787"] = Producer("R787", item["retained_sources"]["R787"], retained/"R787")
        else:
            sources = {label: Producer(label, item["retained_sources"][label], retained/label)
                       for label in sorted(LABELS)}
        read_parent_carrier_receipt(sources["R824"], item["retained_sources"]["R787"])
        schema = select_sources(sources)
        caches = {}
        for label, source_item in cache_labels(item).items():
            archive = None
            if not (retained/label/META[0]).exists():
                archive = Archive(source_item, out.parent/("download-"+label.replace("/", "-")))
                archives[label] = archive
            caches[label] = Producer(label, source_item, retained/label, archive)
        schema["reused_original_modular_cache_stages"] = select_reusable_caches(item, caches, sources)
        configuration = expected_configuration(item, sources)
        if resumed is not None:
            assert configuration == resumed["previous_configuration"]
        groups, bundle = build_input_bundle(out, dict(sources, **caches))
        receipt = {"result": RESULT, "complete": True, "configuration": configuration,
            "producers": groups, "bundle": bundle,
            "file_count": sum(len(row["files"]) for row in groups.values()),
            "selected_total_bytes": sum(f["bytes"] for row in groups.values() for f in row["files"]),
            "source_schema": schema, "R824_original_R787_carrier_transfer": carrier,
            "source_subset_transfers": {label: archive.receipt() for label, archive in archives.items()},
            "all_selected_source_members_and_new_bundle_members_SHA_verified": True,
            "new_mathematical_arithmetic_executed": False}
        save(out/"retained-inputs-receipt.json", receipt)
        if resumed is None:
            save(out/"resume-receipt.json", {"result": RESULT, "resumed": False})
        print("R827_INPUT_REVIEW="+json.dumps({
            "source_labels": sorted(sources), "file_count": receipt["file_count"],
            "selected_total_bytes": receipt["selected_total_bytes"], "bundle": bundle,
            "auxiliary_prime": 1000000753, "original_branch": 0, "canonical_free_column": 1186,
            "R787_original_rows": 1234, "R809_original_S5_rows": 1234,
            "all_original_source_scales_preserved": True,
            "R809_ended_checkpoint_used": sources["R809"].certificate is None,
            "new_mathematical_arithmetic_executed": False}), flush=True)
        return retained, configuration
    finally:
        for archive in archives.values():
            archive.close()


def output_manifest(out):
    for path in out.iterdir():
        if path.is_file() and path.name.endswith((".tmp", ".download", ".partial")):
            path.unlink()
    artifact = "serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    entries = [dict(file_spec(path), artifact=artifact, included_in_git=False)
               for path in sorted(out.iterdir()) if path.is_file()
               and path.name not in (META[0], REFERENCE)]
    assert not any(path.is_dir() for path in out.iterdir()), "All continuation files must be manifest-bound."
    save(out/META[0], {"result": RESULT, "files": entries,
        "temporary_active_checkpoint_artifact": artifact,
        "temporary_active_checkpoint_retention_days": 1,
        "reproducible_data_in_git_or_release": False})
    path = out/META[0]
    save(out/REFERENCE, {"result": RESULT, "manifest_file": path.name,
        "manifest_bytes": path.stat().st_size, "manifest_sha256": sha(path),
        "file_count": len(entries), "full_outputs_artifact": artifact,
        "automatic_git_or_release_publication": False})


def verify_history_archive(out, index, entries, configuration):
    row = index["archive"]
    assert plain(row) == plain(entries[row["file"]])
    expected = index["members"]
    assert len({value["file"] for value in expected}) == len(expected)
    seen = []
    with tarfile.open(out/row["file"], "r:") as archive:
        for member in archive:
            assert member.isfile()
            name = PurePosixPath(member.name)
            assert len(name.parts) == 1 and not name.is_absolute() and ".." not in name.parts
            assert len(seen) < len(expected)
            original = expected[len(seen)]
            assert member.name == original["file"] and member.size == original["bytes"]
            count, digest, pieces = 0, hashlib.sha256(), []
            with archive.extractfile(member) as raw:
                for block in iter(lambda: raw.read(1024*1024), b""):
                    count += len(block)
                    digest.update(block)
                    pieces.append(block)
            assert count == original["bytes"] and digest.hexdigest() == original["sha256"]
            # One small plan or receipt is decoded at a time; no raw archive is retained in memory.
            value = json.loads(gzip.decompress(b"".join(pieces)))
            assert value["complete"] is True and value["configuration"] == configuration
            seen.append(original["file"])
    assert seen == [row["file"] for row in expected]
    assert index["original_completed_plan_and_receipt_bytes_preserved"] is True
    assert index["not_a_new_mathematical_reduction"] is True
    return len(seen)


def verify_sources_and_output_bytes(out):
    manifest = read(out/META[0])
    assert manifest["result"] == RESULT
    entries = {row["file"]: row for row in manifest["files"]}
    assert len(entries) == len(manifest["files"])
    assert {path.name for path in out.iterdir() if path.is_file()} == set(entries) | {META[0], REFERENCE}
    assert not any(path.is_dir() for path in out.iterdir())
    for name, row in entries.items():
        check_spec(row)
        assert file_spec(out/name) == plain(row)
    reference = read(out/REFERENCE)
    assert reference["manifest_sha256"] == sha(out/META[0])
    assert reference["manifest_bytes"] == (out/META[0]).stat().st_size
    assert reference["file_count"] == len(entries)
    initial, run, core = (read(out/name) for name in ("public-actions-input.json", "run-receipt.json", "core-receipt.json"))
    item = initial["job"]
    assert initial["result"] == run["result"] == core["result"] == RESULT
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert initial["source_commit"] == run["source_commit"]
    assert initial["core_sha256"] == item["core_sha256"] == core["source_sha256"]
    assert initial["driver_sha256"] == item["wrapper_sha256"]
    assert initial["proof_sha256"] == item["R827_proof_sha256"]
    assert initial["method_sha256"] == item["R827_method_sha256"]
    assert initial["finite_helper_sha256"] == item["finite_helper_sha256"]
    assert initial["poly_framework_sha256"] == item["poly_framework_sha256"]
    assert initial["io_helper_sha256"] == item["io_helper_sha256"] == IO_SHA
    assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
    assert run["complete"] is True and run["process_exit_code"] == 0 and core["complete"] is True
    assert core["certificate_sha256"] == entries[FINAL]["sha256"]
    receipt = read(out/"retained-inputs-receipt.json")
    assert receipt["result"] == RESULT and receipt["complete"] is True
    assert plain(receipt["bundle"]) == plain(entries[BUNDLE])
    assert receipt["all_selected_source_members_and_new_bundle_members_SHA_verified"] is True
    assert set(receipt["producers"]) == LABELS | set(cache_labels(item))
    retained = out.parent/"retained"
    for label, group in receipt["producers"].items():
        assert group["identity"] == identity(producer_item(item, label))
        assert len(group["files"]) == len({row["file"] for row in group["files"]})
    count = verify_input_bundle(out/BUNDLE, receipt["producers"], retained)
    producers = {label: Producer(label, item["retained_sources"][label], retained/label) for label in sorted(LABELS)}
    read_parent_carrier_receipt(producers["R824"], item["retained_sources"]["R787"])
    schema = select_sources(producers)
    caches = {label: Producer(label, source_item, retained/label)
              for label, source_item in cache_labels(item).items()}
    schema["reused_original_modular_cache_stages"] = select_reusable_caches(item, caches, producers)
    configuration = expected_configuration(item, producers)
    assert configuration == receipt["configuration"]
    assert schema == receipt["source_schema"]
    assert count == receipt["file_count"]
    assert receipt["selected_total_bytes"] == sum(
        row["bytes"] for group in receipt["producers"].values() for row in group["files"])
    for label, source in dict(producers, **caches).items():
        assert set(source.selected) == {row["file"] for row in receipt["producers"][label]["files"]}
    cert = read(out/FINAL)
    assert cert["result"] == RESULT and cert["complete"] is True and cert["configuration"] == configuration
    return entries, initial, run, cert, configuration, count


def compute(item, out):
    guard()
    check_files(item)
    out.mkdir(parents=True, exist_ok=True)
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    for name in (FINAL, "core-receipt.json", "run-receipt.json", META[0], REFERENCE):
        if (out/name).exists():
            (out/name).unlink()
    save(out/"public-actions-input.json", {
        "result": RESULT, "p": 41, "source_repository": "Rogerhu12/math-research-public",
        "source_commit": source, "job": item,
        "core_sha256": sha(S/item["core"]), "driver_sha256": sha(__file__),
        "finite_helper_sha256": sha(S/item["finite_helper"]),
        "poly_framework_sha256": sha(S/item["poly_framework"]),
        "io_helper_sha256": sha(S/item["io_helper"]),
        "proof_sha256": sha(topic_path(item["proof"])),
        "method_sha256": sha(topic_path(item["method"])),
        "request_sha256": sha(REQUEST), "workflow_sha256": sha(REPO/item["workflow"]),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "no_original_Q_rows_or_existing_characteristic_zero_operators_recomputed_by_IO": True})
    code, error, process = 1, None, None
    try:
        retained, configuration = prepare(item, out)
        configuration_path = out.parent/"R827-math-config.json"
        save(configuration_path, item)
        command = [sys.executable, str(S/item["core"]), "--config", str(configuration_path),
            "--proof", str(topic_path(item["proof"])), "--method", str(topic_path(item["method"])),
            "--retained", str(retained), "--output", str(out),
            "--budget-minutes", str(item["budget_minutes"])]
        with (out/"core.log").open("wb") as log:
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=60*(float(item["budget_minutes"])+15))
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=45)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                code, error = 124, "Outer budget boundary; complete stages and atomic module operations retained."
        if code == 0:
            cert = read(out/FINAL)
            assert cert["complete"] is True and cert["configuration"] == configuration
    except BaseException as failure:
        error = type(failure).__name__+": "+str(failure)
        if process is not None and process.poll() is None:
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=45)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
        code = 1
    finally:
        if not (out/"core-receipt.json").exists():
            save(out/"core-receipt.json", {"result": RESULT, "complete": False,
                "source_sha256": item["core_sha256"], "error": error,
                "mathematical_core_may_not_have_started": process is None,
                "original_characteristic_zero_Iq_equals_C": False,
                "actual_D_eta_or_height_computed": False})
        save(out/"run-receipt.json", {"result": RESULT, "p": 41,
            "source_commit": source, "workflow_run_id": os.environ["GITHUB_RUN_ID"],
            "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
            "process_exit_code": code, "complete": code == 0, "error": error,
            "core_receipt_sha256": sha(out/"core-receipt.json"),
            "execution_environment": "public-repository-github-actions",
            "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
        output_manifest(out)
    print("R827_RUN_RECEIPT="+json.dumps(read(out/"run-receipt.json")), flush=True)
    if (out/"core.log").exists():
        with (out/"core.log").open("rb") as log:
            log.seek(max(0, (out/"core.log").stat().st_size-50000))
            print(log.read().decode("utf-8", errors="replace"), flush=True)
    return code


def verify(out):
    """Full byte/schema review. This function never imports the arithmetic core."""
    out = Path(out)
    entries, initial, run, cert, configuration, source_count = verify_sources_and_output_bytes(out)
    item = initial["job"]
    def local(entry, complete=True):
        assert plain(entry) == plain(entries[entry["file"]])
        data = read(out/entry["file"])
        assert data["configuration"] == configuration and data["complete"] is complete
        return data
    inventory = local(cert["stage_manifest"])
    completed = {row["file"]: plain(row) for row in inventory["files"]}
    current = {row["file"]: plain(row) for row in inventory["current_checkpoints"]}
    archives = {row["file"]: plain(row) for row in inventory["history_archives"]}
    assert len(completed) == len(inventory["files"])
    assert len(current) == len(inventory["current_checkpoints"])
    assert len(archives) == len(inventory["history_archives"])
    assert not set(completed) & set(current)
    stage_names = {name for name in entries if name.startswith("R827-") and name.endswith(".json.gz")}
    assert stage_names == set(completed) | set(current) | {cert["stage_manifest"]["file"]}
    assert {name for name in entries if name.startswith("R827-") and name.endswith(".tar")} == set(archives)
    for row in completed.values():
        local(row)
    for row in current.values():
        local(row, complete=False)
    assert cert["history_archives"] == inventory["history_archives"]
    assert cert["history_archive_indexes"] == inventory["history_archive_indexes"]
    used_archives, archived_members = set(), 0
    for entry in inventory["history_archive_indexes"]:
        index = local(entry)
        archive = index["archive"]
        assert plain(archive) == archives[archive["file"]]
        assert archive["file"] not in used_archives
        used_archives.add(archive["file"])
        assert 0 <= index["first_operation"] < index["stop_operation"]
        assert index["stop_operation"]-index["first_operation"] <= 128
        assert len(index["members"]) == 2*(index["stop_operation"]-index["first_operation"])
        assert plain(index["completed_Hermite_index"]) in list(completed.values())
        archived_members += verify_history_archive(out, index, entries, configuration)
    assert used_archives == set(archives)
    def named(name):
        return local(completed[name])
    def polynomial(values):
        assert isinstance(values, list) and all(isinstance(v, int) and 0 <= v < 1000000753 for v in values)
        assert not values or values[-1] != 0
    source = local(cert["source_audit"])
    assert source["prime"] == 1000000753 and source["original_branch"] == 0
    assert source["canonical_free_column"] == 1186
    assert source["original_integral_B_root"] == 3197390 and source["original_s_root"] == 99932770
    assert 0 <= source["original_b_root"] < 1000000753 and 0 <= source["original_zeta_root"] < 1000000753
    for key in ("original_lambda_is_a_unit", "original_minimal_polynomials_and_simple_residue_roots_verified",
                "genuine_DVR_lift_source_not_an_arbitrary_modular_kernel_candidate"):
        assert source[key] is True
    expansion = local(source["canonical_B_expansion"])
    assert expansion["canonical_free_column"] == 1186 and expansion["original_branch"] == 0
    assert expansion["source_R824_branch"]["sha256"] == \
        item["retained_sources"]["R824"]["files"]["R824-power5-prime-1000000753-branch-00.json.gz"]
    assert expansion["source_R787_branch"]["sha256"] == IO.PINNED_OLD[R787_PREFIX+"branch-00.json.gz"]
    assert expansion["source_original_rational_blocks"]["sha256"] == IO.PINNED_OLD[R787_PREFIX+"rational-blocks.json.gz"]
    assert expansion["original_B_lambda_b_root"] == source["original_integral_B_root"]
    assert expansion["original_b_root"] == source["original_b_root"]
    assert expansion["original_s_root"] == source["original_s_root"]
    assert expansion["lambda"] == source["original_field"]["lambda"]
    assert expansion["original_V5_integer_scale"] == str(82**10)
    modular_rows([expansion["B_coefficients_mod_prime_in_original_V5_basis"]], 1, 1234)
    modular_rows([expansion["A_coefficients_mod_prime_in_original_V5_basis"]], 1, 1234)
    modular_rows([expansion["canonical_C_coefficients_mod_prime"]], 1, 1214)
    assert any(expansion["B_coefficients_mod_prime_in_original_V5_basis"])
    assert expansion["same_original_reserved_normalization_verified"] is True
    assert expansion["abstract_original_p_integral_lift_certified_by_unit_minor_and_rank_bound"] is True
    assert expansion["characteristic_zero_coefficients_reconstructed"] is False
    normal_B = local(cert["normal_B_vector"])
    assert normal_B["source_original_B_expansion"] == source["canonical_B_expansion"]
    assert normal_B["canonical_free_column"] == 1186 and normal_B["original_branch"] == 0
    assert normal_B["regular_degree_bound"] == 5 and normal_B["normal_basis_rank"] == 272
    assert normal_B["normal_basis_degrees"] == EPS
    modular_rows(normal_B["vector_coefficients_mod_prime"], 6, 272)
    assert len(normal_B["source_S5_rows"]) == len(normal_B["source_original_V5_rows"]) == 1234
    for key in ("all1380_original_short_coordinates_verified", "same_original_82power10_scales_preserved",
                "abstract_p_integral_original_normal_lift_certified"):
        assert normal_B[key] is True
    assert normal_B["original_Q_prefix_and_large_characteristic_zero_solve_recomputed"] is False
    assert normal_B["characteristic_zero_coordinates_reconstructed"] is False
    minor = local(normal_B["source_actual_unit_minor"])
    assert minor["prime"] == 1000000753 and minor["actual_determinant_mod_prime"] != 0
    assert len(minor["row_indices"]) == len(set(minor["row_indices"])) == 1234
    assert all(0 <= row < 1380 for row in minor["row_indices"])
    assert minor["column_indices"] == list(range(1234))
    assert minor["both_inverse_products_verified"] is True
    assert minor["original_Q_matrix_and_69_term_rows_recomputed"] is False
    modular_rows(minor["inverse_mod_prime"], 1234, 1234)
    ordinary = named("R827-original-W-g-h-reductions.json.gz")
    assert ordinary["original_rational_denominators_all_units"] is True
    assert ordinary["original_R813_target_scales_applied_once"] == [[6724, 1], [6724, 1]]
    assert ordinary["original_W_e0_equals_e1_verified"] is True
    assert ordinary["original_primitive_coordinate_solutions_not_recomputed"] is True
    assert len(ordinary["W_coefficients_mod_prime"]) == 4
    for matrix in ordinary["W_coefficients_mod_prime"]:
        modular_rows(matrix, 272, 272)
    for key in ("g_vector_coefficients_mod_prime", "h_vector_coefficients_mod_prime"):
        modular_rows(ordinary[key], 4, 272)
    C = named("R827-original-two-chart-C-reduction.json.gz")
    for key in ("all_original_rational_coefficients_p_integral", "both_P_constant_terms_units",
                "actual_degree_twenty_monic_polynomials_preserved",
                "original_reciprocal_relation_verified_mod_prime",
                "original_exact_two_chart_transition_certificate_preserved",
                "complete_flat_target_not_squarefree_replacement"):
        assert C[key] is True
    for chart in ("tau", "sigma"):
        data = C["charts"][chart]
        assert len(data["q_polynomials"]) == 271 and len(data["P_polynomial"]) == 21
        assert data["P_polynomial"][0] != 0 and data["P_polynomial"][20] == 1
        assert len(data["original_column_sources"]) == 272
        for poly in data["q_polynomials"]:
            polynomial(poly)
            assert len(poly) <= 20
    grid = named("R827-eight-original-unit-cyclic-nodes.json.gz")
    assert grid["prime"] == 1000000753
    points = grid["points"]
    assert len(points) == len(set(points)) == len(grid["Krylov_point_stages"]) == 8
    assert all(isinstance(point, int) and 0 <= point < 1000000753 for point in points)
    assert grid["targets_and_node_counts"] == {"B": 8, "g": 6, "Gamma": 5}
    assert grid["all_eight_actual_determinants_nonzero"] is True
    assert grid["distinct_residue_values_and_unit_Vandermonde_certified"] is True
    assert grid["characteristic_zero_Krylov_matrix_or_inverse_computed"] is False
    for point, entry in zip(points, grid["Krylov_point_stages"]):
        stage = local(entry)
        assert stage["prime"] == 1000000753 and stage["z0"] == point and stage["usable"] is True
        assert stage["actual_cyclic_rank"] == 272 and stage["actual_determinant_mod_prime"] != 0
        assert stage["both_inverse_products_verified"] is True
        modular_rows(stage["W_evaluated_mod_prime"], 272, 272)
        modular_rows(stage["inverse_Krylov_matrix_mod_prime"], 272, 272)
        if stage.get("Krylov_matrix_mod_prime") is not None:
            modular_rows(stage["Krylov_matrix_mod_prime"], 272, 272)
            assert fingerprint(stage["Krylov_matrix_mod_prime"]) == stage["Krylov_matrix_sha256"]
    operator_certificate = local(cert["operator_identity_and_transport_certificate"])
    assert operator_certificate["operator_indexes"] == cert["operator_indexes"]
    for key in ("B_first_column_is_original_vB", "g_first_column_is_original_vg",
                "Gamma_first_column_zero_and_second_column_original_vh",
                "B_commutator_full_polynomial_identity_certified_by_nine_points",
                "g_commutator_full_polynomial_identity_certified_by_seven_points",
                "Gamma_nested_full_polynomial_identity_certified_by_seven_points",
                "all_sigma_negative_powers_and_original_minus_sign_verified",
                "all_operators_are_true_original_p_integral_reductions"):
        assert operator_certificate[key] is True
    assert operator_certificate["actual_characteristic_zero_operator_CRT_repeated"] is False
    assert set(cert["operator_indexes"]) == {"B", "g", "Gamma"}
    block_ranges = [(first, min(first+16, 272)) for first in range(0, 272, 16)]
    for target, degree in (("B", 5), ("g", 3), ("Gamma", 2)):
        assert set(cert["operator_indexes"][target]) == {"tau", "sigma"}
        for chart in ("tau", "sigma"):
            index = local(cert["operator_indexes"][target][chart])
            assert index["target"] == target and index["chart"] == chart and index["prime"] == 1000000753
            assert index["regular_degree_bound"] == degree
            assert index["normal_basis_rank"] == 272 and index["normal_basis_degrees"] == EPS
            assert len(index["row_blocks"]) == 17
            imported = None
            if chart == "tau":
                assert index["all_weighted_support_zeros_verified"] is True
                assert index["original_true_operator_reduction_certified"] is True
                imported = index.get("source_bound_completed_modular_image")
                if imported is None:
                    assert index["actual_interpolation_points"] == points[:degree+3]
                    assert len(index["source_point_values"]) == degree+3
                    for point, entry in zip(points, index["source_point_values"]):
                        value = local(entry)
                        assert value["target"] == target and value["z0"] == point
                        assert value["original_true_operator_point_value"] is True
                        modular_rows(value["matrix_mod_prime"], 272, 272)
                else:
                    assert target in ("g", "Gamma") and imported in item["reusable_stage_sources"]
                    assert imported["role"] == "operator_modular_image" and imported["target"] == target
                    assert imported["prime"] == 1000000753
                    assert index["actual_interpolation_points"] is None and index["source_point_values"] == []
                    assert index["old_completed_modular_interpolation_recomputed"] is False
                    old_path = out.parent/"retained"/imported["relative_path"]
                    assert file_spec(old_path) == plain(imported["stage"])
                    old_image = read(old_path)
                    assert len(old_image["interpolated_blocks"]) == 17
            else:
                assert index["all_negative_powers_and_weighted_zeros_verified"] is True
                assert index["g_matrix_means_negative_sigma_base_derivative"] is (target == "g")
                assert index["source_tau_operator"] == cert["operator_indexes"][target]["tau"]
            for entry, (first, stop) in zip(index["row_blocks"], block_ranges):
                block = local(entry)
                assert block["target"] == target and block["chart"] == chart
                assert (block["row_first"], block["row_stop"]) == (first, stop)
                assert block["regular_degree_bound"] == degree
                raw = block["coefficient_matrices_low_to_high"]
                assert len(raw) == degree+3
                for power, matrix in enumerate(raw):
                    modular_rows(matrix, stop-first, 272)
                    for offset, row in enumerate(matrix):
                        for column, value in enumerate(row):
                            if power > degree+EPS[column]-EPS[first+offset]:
                                assert value == 0
                if chart == "tau":
                    assert block["original_weighted_support_verified"] is True
                    assert block["true_p_integral_operator_reduction_by_unit_nodes_and_original_degree_bound"] is True
                    if imported is not None:
                        assert block["source_bound_completed_modular_image"] == imported
                        assert block["source_original_modular_block"] == old_image["interpolated_blocks"][first//16]
                        assert block["source_point_values"] == []
                        assert block["old_completed_modular_interpolation_recomputed"] is False
                else:
                    assert block["all_negative_powers_and_weighted_zeros_verified"] is True
                    assert block["same_original_function_derivation_and_connection_preserved"] is True
        for point in range((degree+4) if target != "Gamma" else 7):
            suffix = ("-nested-commutator-z-" if target == "Gamma" else "-commutator-z-")
            stage = named("R827-identity-"+target+suffix+str(point)+".json.gz")
            assert stage["prime"] == 1000000753 and stage["z0"] == point
            if target == "Gamma":
                assert stage["whole_nested_commutator_zero"] is True and stage["entry_degree_bound"] == 6
                assert stage["original_h_first_column_verified"] is True
            else:
                assert stage["whole_matrix_commutator_zero"] is True and stage["entry_degree_bound"] == degree+3

    q = cert["requested_derivative_order"]
    assert q == cert["actual_derivative_order"] == item["requested_derivative_order"]
    assert cert["certification_mode"] == MODE
    assert cert["completed_scope"] == "original_residue_sufficient_termination_test"
    assert cert["normal_basis_rank"] == 272 and cert["normal_basis_degrees"] == EPS
    infinity = local(cert["sigma_infinity_certificate"])
    assert infinity["chart"] == "sigma" and infinity["base_point"] == 0
    assert infinity["derivative_order"] == q and infinity["prime"] == 1000000753
    assert infinity["actual_C_sigma_determinant_at_zero"] == C["charts"]["sigma"]["P_polynomial"][0] != 0
    assert infinity["initial_jet_precision_stop"] == q+1
    assert infinity["jet_precision_decreases_by_one_per_derivative"] is True
    assert infinity["matrix_rows"] == 272 and infinity["matrix_columns"] == 272*(q+1)
    rank = infinity["actual_rank_mod_prime"]
    assert isinstance(rank, int) and 0 <= rank <= 272
    pivots = infinity["actual_selected_pivot_columns"]
    assert len(pivots) == rank and pivots == sorted(set(pivots))
    assert all(0 <= i < 272*(q+1) for i in pivots)
    assert infinity["whole_infinity_fiber_surjective"] is (rank == 272)
    assert infinity["raw_normal_columns_have_same_rank_as_complete_C_coordinates"] is True
    assert infinity["failure_does_not_negate_other_global_sources_or_characteristic_zero_Iq"] is (rank != 272)
    assert infinity["characteristic_zero_or_new_torsion_jets_computed"] is False
    if rank == 272:
        assert infinity["actual_full_minor_determinant_mod_prime"] != 0
        modular_rows(infinity["actual_full_minor_matrix_mod_prime"], 272, 272)
    else:
        assert infinity["actual_full_minor_determinant_mod_prime"] is None
        assert infinity["actual_full_minor_matrix_mod_prime"] is None
    jets = infinity["source_layer_jets"]
    assert len(jets) == q+1
    for k, jet in enumerate(jets):
        assert jet["derivative_order"] == k and jet["required_precision_stop"] == q+1-k
        if k == 0:
            assert jet["source"] == cert["operator_indexes"]["B"]["sigma"]
            continue
        layer = local(jet["source"])
        count = min(q+1-k, 8+2*k)
        assert layer["chart"] == "sigma" and layer["derivative_order"] == k
        assert layer["precision_stop"] == count and layer["full_polynomial_degree_bound"] == 7+2*k
        assert layer["normal_basis_rank"] == 272 and layer["normal_basis_degrees"] == EPS
        assert layer["original_generator_weights"] == [5+eps for eps in EPS]
        assert layer["all_required_coefficient_blocks_complete"] is True
        assert layer["higher_requested_precision_can_append_without_repeating_completed_coefficients"] is True
        blocks = layer["coefficient_row_blocks"]
        assert len(blocks) == count*17
        for index, entry in enumerate(blocks):
            power, part = divmod(index, 17)
            first, stop = block_ranges[part]
            block = local(entry)
            assert block["chart"] == "sigma" and block["derivative_order"] == k
            assert block["coefficient_exponent"] == power
            assert (block["row_first"], block["row_stop"]) == (first, stop)
            modular_rows(block["coefficient_matrix_mod_prime"], stop-first, 272)
            for key in ("all_required_previous_coefficients_present_or_structurally_zero",
                        "original_weighted_support_verified", "sigma_negative_base_derivative_preserved",
                        "old_completed_coefficient_not_recomputed"):
                assert block[key] is True
    tau_entry = cert["tau_Hermite_certificate"]
    tau, reduction, tau_surjective = None, None, False
    if tau_entry is not None:
        tau = local(tau_entry)
        assert tau["chart"] == "tau" and tau["prime"] == 1000000753
        assert 0 <= tau["derivative_order"] <= q
        assert tau["source_generator_weights"] == [5+eps for eps in EPS]
        assert tau["complete_unimodular_polynomial_generation_history_verified"] is True
        assert tau["no_characteristic_zero_Bezout_or_module_Hermite_computed"] is True
        assert tau["exact_total_rank_claimed_if_missing_pivot"] is False
        reduction = local(tau["reduction_final_index"])
        assert reduction["kind"] == "completed_polynomial_matrix"
        assert reduction["orientation"] == "columns"
        assert reduction["vector_length"] == reduction["tile_size"] == 272
        count = reduction["vector_count"]
        assert isinstance(count, int) and count >= 272 and len(reduction["vectors"]) == count
        assert reduction["history"]["operation_count"] == reduction["operation_count"]
        assert reduction["history"]["complete_unimodular_transcript_metadata_chain_verified"] is True
        assert reduction["history"]["all_operation_plans_and_receipts_retained"] is True
        tau_surjective = tau["whole_affine_polynomial_module_surjective"]
        assert isinstance(tau_surjective, bool)
        assert tau["failure_is_only_this_sufficient_original_residue_test"] is (not tau_surjective)
        if tau["full_row_rank_reduction_complete"]:
            assert reduction["actual_pivot_rank"] == 272
            assert reduction["all_column_operations_unimodular_over_original_residue_polynomial_ring"] is True
            assert reduction["exact_original_column_module_preserved"] is True
            diagonals = tau["actual_Hermite_diagonal"]
            assert diagonals == reduction["actual_diagonal"] and len(diagonals) == 272
            for a, row in enumerate(diagonals):
                assert row["index"] == a
                polynomial(row["polynomial"])
                assert row["degree"] >= 0 and len(row["polynomial"]) == row["degree"]+1
                assert row["polynomial"][-1] == 1
            assert tau_surjective is all(row["degree"] == 0 for row in diagonals)
            assert tau["first_missing_pivot_row"] is None
        else:
            assert tau_surjective is False and tau["actual_Hermite_diagonal"] is None
            missing = tau["first_missing_pivot_row"]
            assert isinstance(missing, int) and 0 <= missing < 272
            assert reduction["full_row_rank_reduction_complete"] is False
            assert reduction["first_missing_pivot_row"] == missing
            assert reduction["pivot_row_is_not_reported_as_the_total_rank"] is True
            assert reduction["remaining_entries_of_that_pivot_row_verified_zero"] is True
            assert reduction["completed_unimodular_transformation_preserves_entire_source_module"] is True
            assert reduction["actual_pivot_rank"] is None and reduction["exact_total_rank_computed"] is False
        for column, entry in enumerate(reduction["vectors"]):
            vector = local(entry)
            assert vector["kind"] == "exact_polynomial_vector"
            assert vector["length"] == vector["tile_size"] == 272 and vector["orientation"] == "columns"
            assert vector["vector_index"] == column
            assert len(vector["tiles"]) == 1
            tile_entry = vector["tiles"][0]
            assert tile_entry["first"] == 0 and tile_entry["stop"] == 272
            tile = local(tile_entry)
            assert tile["kind"] == "exact_polynomial_vector_tile"
            assert tile["matrix_label"] == vector["matrix_label"] and tile["vector_index"] == column
            assert tile["first"] == 0 and tile["stop"] == 272
            assert len(tile["coefficients"]) == 272
            for row, poly in enumerate(tile["coefficients"]):
                polynomial(poly)
                if tau_surjective:
                    assert poly == ([1] if row == column else [])
        next_operation = 0
        for entry in tau["history_archive_indexes"]:
            block = local(entry)
            assert block["completed_Hermite_index"] == tau["reduction_final_index"]
            assert block["first_operation"] == next_operation
            next_operation = block["stop_operation"]
        assert next_operation == reduction["operation_count"]
    else:
        assert rank < 272
    success = tau_surjective and rank == 272
    assert cert["whole_tau_polynomial_module_surjective"] is tau_surjective
    assert cert["whole_sigma_infinity_fiber_surjective"] is (rank == 272)
    assert cert["tau_Hermite_skipped_because_infinity_test_failed"] is (tau_entry is None)
    assert cert["original_characteristic_zero_Iq_equals_C"] is success
    assert cert["safe_D_multiplicity_bound"] == (q//3 if success else None)
    assert cert["original_D_reduced_certified"] is bool(success and q//3 <= 1)
    assert cert["actual_maximum_D_multiplicity_computed"] is False
    assert cert["actual_D_eta_or_height_computed"] is False
    assert cert["failure_does_not_assert_Iq_not_equal_C"] is (not success)
    final_stage = local(cert["derivative_order_result"])
    for key in ("actual_derivative_order", "source_audit", "normal_B_vector", "operator_indexes",
                "operator_identity_and_transport_certificate", "tau_Hermite_certificate",
                "sigma_infinity_certificate", "original_characteristic_zero_Iq_equals_C",
                "safe_D_multiplicity_bound", "original_D_reduced_certified"):
        assert final_stage[key] == cert[key]
    summary = {
        "result": RESULT, "full_manifest_files_verified": len(entries),
        "complete_math_stages_verified": len(completed), "atomic_current_checkpoints_preserved": len(current),
        "complete_history_archives_verified": len(archives), "archived_plan_receipt_members_verified": archived_members,
        "all_original_retained_bundle_members_verified": source_count,
        "original_auxiliary_prime": 1000000753, "original_branch": 0, "canonical_free_column": 1186,
        "actual_derivative_order": q, "whole_tau_polynomial_module_surjective": tau_surjective,
        "actual_sigma_infinity_rank": rank,
        "original_characteristic_zero_Iq_equals_C": success,
        "safe_D_multiplicity_bound": cert["safe_D_multiplicity_bound"],
        "original_D_reduced_certified": cert["original_D_reduced_certified"],
        "actual_D_eta_or_height_computed": False,
        "original_b_residue": source["original_b_root"],
        "actual_unit_S5_determinant": minor["actual_determinant_mod_prime"],
        "actual_unit_cyclic_points": points,
        "core_seconds": cert["seconds"], "certificate": file_spec(out/FINAL),
        "stage_manifest": cert["stage_manifest"], "source_audit": cert["source_audit"],
        "normal_B_vector": cert["normal_B_vector"], "operator_indexes": cert["operator_indexes"],
        "source_commit": initial["source_commit"], "workflow_run_id": run["workflow_run_id"],
        "new_mathematical_arithmetic_executed_by_verifier": False}
    print("R827_COMPLETE_IO_REVIEW="+json.dumps(summary, sort_keys=True, separators=(",", ":")), flush=True)
    return summary


def main():
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--prepare-only", action="store_true")
    args = parser.parse_args()
    if args.verify:
        verify(args.output)
        return 0
    item = read(REQUEST)["job"]
    if args.prepare_only:
        guard()
        prepare(item, args.output)
        return 0
    return compute(item, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
