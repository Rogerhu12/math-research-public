#!/usr/bin/env python3
"""Actual R824-origin A/B normal inputs for the unchanged R811 multiplier arithmetic."""
import argparse
import importlib.util
import math
from pathlib import Path
import sys
import time

FRAMEWORK_NAME = "R811_original_regular_multipliers.py"
FRAMEWORK_SHA = "849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3"
PROOF_SHA = "263d8a15085c3fc053dac1df546ad0c3efb565d67ce312c78ec6e5ddb4dccf78"
METHOD_SHA = "b700c4ca03ba3d198e68c54b5c9a6eb9deb44d9a85b03b41e9583619db94f66d"
R809_AB_RESULT = "R809-original-A-B-normal-coordinates-from-R824"
R809_AB_SHA = "cdc381fc5e1b9dfab705608f1d62a8ab80b282984479499a6edd635ea05fa62b"
R809_BASIS_SHA = "dedb5d6149a3c3ae86ad09e51f30c1424951a09010bf48afd948d2628e1ec21d"
S5_INDEX_SHA = "f6f6f0ee2bae106ef474d2cff32c743b1d8e0a886f80c26aaf8708c89ea1c119"

def source_sha(path):
    import hashlib
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()

framework = Path(__file__).resolve().parent/FRAMEWORK_NAME
assert source_sha(framework) == FRAMEWORK_SHA
loader = importlib.util.spec_from_file_location("R811_R824_frozen_arithmetic", framework)
base = importlib.util.module_from_spec(loader)
loader.loader.exec_module(base)
flint = base.flint
sha, read, save, fingerprint, spec = base.sha, base.read, base.save, base.fingerprint, base.spec
Retained, producer_identity, same_producer = base.Retained, base.producer_identity, base.same_producer
FREE, LDEG, S5, EPS, FIELD_BASIS = base.FREE, base.LDEG, base.S5, base.EPS, base.FIELD_BASIS
R806_RESULT, R809_RESULT, TARGETS, SCOPE = base.R806_RESULT, base.R809_RESULT, base.TARGETS, base.SCOPE
RESULT = "R811-original-regular-multipliers-from-R824-normal-vectors"
FINAL = "p41-original-regular-multipliers-from-R824-certificate.json"

def relation_source_identity(item):
    value = {key: item[key] for key in
             ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")}
    name = item["certificate_name"]
    value["certificate"] = {"file": name, "sha256": item["files"][name]}
    return value

class Job(base.Job):
    def __init__(self, args):
        self.args, self.out, self.started = args, args.output, time.monotonic()
        self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        assert self.item["producer_inputs_pending"] is False
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert self.item["core_sha256"] == sha(__file__)
        assert self.item["multiplier_framework"] == FRAMEWORK_NAME
        assert self.item["multiplier_framework_sha256"] == FRAMEWORK_SHA
        assert sha(args.proof) == self.item["R811_proof_sha256"] == PROOF_SHA
        assert sha(args.method) == self.item["R811_method_sha256"] == METHOD_SHA
        assert flint.__version__ == "0.9.0"
        assert self.item["requested_stage"] == SCOPE
        assert self.item["requested_targets"] == list(TARGETS)
        assert self.item["auxiliary_prime_start"] == 1000000007
        assert self.item["matrix_row_block_size"] == 16
        assert self.item["reconstruct_every_primes"] >= 1
        assert self.item["exact_commutator_mode"] == "deterministic_integer_points_with_weighted_degree_bound"
        assert set(self.item["retained_artifacts"]) == {"R806", "R809", "R809_basis"}
        self.r806 = Retained(args.retained, "R806", self.item["retained_artifacts"]["R806"])
        self.r809 = Retained(args.retained, "R809", self.item["retained_artifacts"]["R809"])
        self.r809_basis = Retained(args.retained, "R809_basis", self.item["retained_artifacts"]["R809_basis"])
        assert self.r806.identity["result"] == R806_RESULT
        assert self.r809.identity["result"] == R809_AB_RESULT
        assert self.r809.identity["core_sha256"] == R809_AB_SHA
        assert self.r809_basis.identity["result"] == R809_RESULT
        assert self.r809_basis.identity["core_sha256"] == R809_BASIS_SHA
        c806, c809 = self.r806.certificate, self.r809.certificate
        cbasis = self.r809_basis.certificate
        assert c809["completed_scope"] == "A_and_B_only_from_one_true_R824_relation"
        assert c809["completed_rational_RHS_columns"] == 28
        assert c809["actual_A_B_normal_vectors_computed"] is True
        assert c809["all28_rational_RHS_columns_verified_in_all1380_rows"] is True
        assert c809["external_S5_references_keep_their_original_configuration"] is True
        assert c809["normal_function_equation"] == "y=normal(A)/normal(B)"
        assert c809["original_R824_denominator_and_content_reinserted"] is False
        assert c809["synthetic_original_R809_or_R787_result_created"] is False
        assert c809["original_S5_producer"] == relation_source_identity(self.r809_basis.identity)
        assert self.r809.tag["source_identities"]["R809"] == relation_source_identity(self.r809_basis.identity)
        assert self.r809.tag["original_S5_configuration_sha256"] == fingerprint(self.r809_basis.tag)
        assert c809["actual_R824_source"] == self.r809.tag["actual_R824_source"]
        assert c809["actual_R824_relation"] == self.r809.tag["actual_R824_relation"]
        assert c809["original_b_model"] == cbasis["original_b_model"]
        assert cbasis["normal_basis_rank"] == FREE and cbasis["normal_basis_degrees"] == EPS
        assert cbasis["S5_dimension"] == S5 and cbasis["qY_count"] == 69
        assert cbasis["full_real_coordinates"] == 1380
        assert cbasis["all_requested_targets_verified_in_all1380_rows"] is True
        assert cbasis["coefficient_field_basis"] == FIELD_BASIS
        assert c809["actual_sigma_integer_n"] == cbasis["actual_sigma_integer_n"]
        assert self.r809.tag["actual_sigma_integer_n"] == self.r809_basis.tag["actual_sigma_integer_n"]
        assert c806["completed_scope"] == "primitive_multiplication_and_cyclic_certificate"
        assert c806["normal_affine_basis_rank"] == FREE
        for key in ("exact_polynomial_multiplication_computed",
                    "all272_columns_verified_in_all820_original_rows",
                    "actual_cyclic_minor_certified",
                    "original_function_field_primitive_generator_certified",
                    "normal_integral_basis_preserved"):
            assert c806[key] is True
        assert c809["normal_basis_rank"] == FREE and c809["normal_basis_degrees"] == EPS
        assert c809["S5_dimension"] == S5 and c809["qY_count"] == 69
        assert c809["full_real_coordinates"] == 1380
        assert c809["original_scalar_and_field_normalizations_preserved"] is True
        assert c809["coefficient_field_basis"] == FIELD_BASIS
        assert set(TARGETS) <= set(c809["completed_target_groups"])
        same_producer(self.r806.tag["retained_artifacts"]["R805"],
                      self.r809_basis.tag["basis_producers"]["R805"])
        assert self.r806.tag["actual_sigma_integer_n"] == self.r809_basis.tag["actual_sigma_integer_n"]
        self.w_spec = c806["polynomial_multiplier"]
        self.w_interface = self.r806.indexed(self.w_spec)
        interface = self.w_interface
        assert interface["normal_affine_basis_rank"] == FREE
        assert interface["normal_affine_basis_degrees"] == EPS
        assert interface["coefficient_field"] == "Q, certified by exact original rational coordinate equations"
        assert interface["matrix_convention"] == "M_ba(z) is output row b, input column a"
        assert interface["coordinate_groups"] == c806["exact_coordinate_groups"]
        assert interface["original_R805_free_basis"] == self.r809_basis.tag["original_graded_free_basis"]
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
        self.s5_spec = c809["S5_basis_index"]
        assert self.s5_spec == cbasis["S5_basis_index"] == self.r809.tag["original_S5_basis_index"]
        assert self.s5_spec["sha256"] == S5_INDEX_SHA
        self.s5_index = self.r809_basis.indexed(self.s5_spec)
        assert self.s5_index["dimension"] == S5
        assert self.s5_index["normal_affine_basis_rank"] == FREE
        assert self.s5_index["normal_basis_degrees"] == EPS
        assert self.s5_index["original_graded_free_basis"] == interface["original_R805_free_basis"]
        assert self.s5_index["integer_scale"] == str(82**10)
        assert self.s5_index["all_original_term_phases_and_scales_verified"] is True
        self.s5_mapping = [(a, j) for a in range(FREE) for j in range(6-EPS[a])]
        assert len(self.s5_mapping) == S5 == len(self.s5_index["basis_rows"])
        for index, ((a, j), entry) in enumerate(zip(self.s5_mapping, self.s5_index["basis_rows"])):
            assert entry["index"] == index
            assert (entry["normal_basis_index"], entry["z_degree"]) == (a, j)
            assert entry["normal_basis_degree"] == EPS[a]
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "R811_proof_sha256": sha(args.proof), "R811_method_sha256": sha(args.method),
            "multiplier_framework_sha256": FRAMEWORK_SHA,
            "R809_normal_producer": producer_identity(self.r809.identity),
            "R809_basis_producer": producer_identity(self.r809_basis.identity),
            "R809_normal_configuration_sha256": fingerprint(self.r809.tag),
            "actual_R824_source": c809["actual_R824_source"],
            "actual_R824_relation": c809["actual_R824_relation"],
            "actual_R824_free_column": c809["original_R824_free_column"],
            "external_S5_configuration_preserved": True,
            "p": 41, "normal_affine_basis_rank": FREE, "normal_basis_degrees": EPS,
            "coefficient_field_basis": FIELD_BASIS,
            "R806_producer": producer_identity(self.r806.identity),
            "R806_polynomial_multiplier": self.w_spec, "R806_cyclic_witness": self.witness_spec,
            "R809_basis_configuration_sha256": fingerprint(self.r809_basis.tag),
            "R809_S5_basis_index": self.s5_spec,
            "original_R805_free_basis": interface["original_R805_free_basis"],
            "actual_sigma_integer_n": self.r806.tag["actual_sigma_integer_n"],
            "matrix_convention": "M_ba output b input a",
            "auxiliary_prime_start": self.item["auxiliary_prime_start"],
            "matrix_row_block_size": self.item["matrix_row_block_size"],
            "reconstruct_every_primes": self.item["reconstruct_every_primes"],
            "point_search": "original successful z0 first; then distinct nonnegative residues",
            "exact_commutator_mode": self.item["exact_commutator_mode"],
            "no_characteristic_zero_Krylov_matrix_or_inverse": True,
            "requested_targets_budget_and_transport_artifacts_excluded_from_mathematical_identity": True,
        }
        self.target_data, self.target_specs, self.target_tags = {}, {}, {}
        for target in TARGETS:
            target_spec = c809["normal_vectors"][target]
            data = self.r809.indexed(target_spec)
            assert data["target"] == target and data["normal_basis_rank"] == FREE
            assert data["normal_basis_degrees"] == EPS and data["regular_degree_bound"] == 5
            assert data["coefficient_field_basis"] == FIELD_BASIS
            assert data["S5_basis_index"] == self.s5_spec
            for key in ("all14_original_field_columns_retained", "normal_vector_actually_nonzero",
                        "all1380_original_coordinates_verified", "weighted_polynomial_support_verified",
                        "original_field_and_scalar_normalizations_preserved"):
                assert data[key] is True
            original_target = c809["completed_target_configurations"][target]
            assert data["target_configuration"] == original_target
            assert data["target_configuration_sha256"] == fingerprint(original_target)
            assert original_target["basis_configuration_sha256"] == fingerprint(self.r809.tag)
            assert original_target["coefficient_field_basis"] == FIELD_BASIS
            assert original_target["original_b_model"] == data["original_b_model"] == c809["original_b_model"]
            self.target_specs[target], self.target_data[target] = target_spec, data
            self.target_tags[target] = {
                "basis_configuration_sha256": fingerprint(self.tag), "target": target,
                "source_R809_normal_vector": target_spec,
                "source_R809_target_configuration": original_target,
                "source_R809_target_configuration_sha256": fingerprint(original_target),
                "regular_degree_bound": 5, "coefficient_field_basis": FIELD_BASIS,
                "original_b_model": data["original_b_model"],
            }
        self.w_coefficients = None
        self.w_denominator = None
        self.prime_values = []
        self.target_vectors = {}
        self.block_ranges = [(first, min(first+self.item["matrix_row_block_size"], FREE))
                             for first in range(0, FREE, self.item["matrix_row_block_size"])]

        audit = {
            "normal_producer": producer_identity(self.r809.identity),
            "basis_producer": producer_identity(self.r809_basis.identity),
            "normal_configuration_sha256": fingerprint(self.r809.tag),
            "original_S5_configuration_sha256": fingerprint(self.r809_basis.tag),
            "source_S5_basis_index": self.s5_spec,
            "actual_R824_source": c809["actual_R824_source"],
            "actual_R824_relation": c809["actual_R824_relation"],
            "actual_R824_free_column": c809["original_R824_free_column"],
            "normal_vectors": self.target_specs,
            "original_relation_common_denominator_or_content_reinserted": False,
            "synthetic_R787_or_C_only_R809_A_B_output_created": False,
        }
        prior = self.cached("R811-R824-normal-source-audit")
        if prior is None:
            self.store("R811-R824-normal-source-audit", audit)
        else:
            for key, value in audit.items():
                assert prior[key] == value

    def target_component(self, target, component):
        assert target in TARGETS and 0 <= component < LDEG
        key = target, component
        if key in self.target_vectors:
            return self.target_vectors[key]
        source = self.target_data[target]
        degree = source["regular_degree_bound"]
        group_specs = source["coordinate_groups"]
        assert len(group_specs) == 2
        group_spec = group_specs[component//7]
        group = self.r809.indexed(group_spec)
        indices = group["column_indices"]
        assert indices == list(range((component//7)*7, (component//7+1)*7))
        assert group["target"] == target and group["normal_basis_rank"] == FREE
        assert group["basis_dimension"] == S5 and group["full_coordinate_rows"] == 1380
        assert group["all1380_original_coordinates_verified"] is True
        assert group["original_field_and_scalar_normalizations_preserved"] is True
        assert group["coefficient_field_basis"] == FIELD_BASIS
        assert group["regular_degree_bound"] == degree
        assert group["S5_basis_index"] == self.s5_spec
        assert group["target_configuration"] == source["target_configuration"]
        assert group["target_configuration_sha256"] == source["target_configuration_sha256"]
        assert len(group["coordinate_numerators"]) == S5
        assert all(len(row) == 7 for row in group["coordinate_numerators"])
        assert len(group["column_denominators"]) == len(group["original_target_rational_scales"]) == 7
        local = component % 7
        group_denominator = int(group["column_denominators"][local])
        scale = group["original_target_rational_scales"][local]
        scale_num, scale_den = int(scale[0]), int(scale[1])
        assert group_denominator > 0 and scale_den > 0
        name = "R811-target-"+target+"-component-"+str(component).zfill(2)+"-original-vector"
        data = self.cached(name, target)
        if data is None:
            denominator = group_denominator*scale_den
            values = [[0]*FREE for _ in range(degree+1)]
            for row, (output, power) in enumerate(self.s5_mapping):
                numerator = int(group["coordinate_numerators"][row][local])*scale_num
                if power > degree-EPS[output]:
                    assert numerator == 0
                else:
                    values[power][output] = numerator
            content = denominator
            for row in values:
                for value in row:
                    content = math.gcd(content, value)
            assert content > 0
            denominator //= content
            values = [[value//content for value in row] for row in values]
            self.store(name, {
                "target": target, "field_component": component,
                "regular_degree_bound": degree, "normal_affine_basis_rank": FREE,
                "source_normal_vector": self.target_specs[target],
                "source_exact_coordinate_group": group_spec,
                "source_field_column_index": component,
                "original_target_rational_scale": scale,
                "original_group_column_denominator": str(group_denominator),
                "source_original_S5_index": self.s5_spec,
                "common_positive_denominator": str(denominator),
                "integer_vector_coefficients_low_to_high": [[str(x) for x in row] for row in values],
                "exactly_zero_component": not any(value for row in values for value in row),
                "original_rational_scale_applied_exactly_once": True,
                "no_original_relation_removed_common_denominator_or_content_reinserted": True,
                "all_original_14_field_columns_preserved": True,
                "weighted_support_verified": True,
            }, target)
            data = self.cached(name, target)
        assert data["source_normal_vector"] == self.target_specs[target]
        assert data["source_exact_coordinate_group"] == group_spec
        assert data["original_target_rational_scale"] == scale
        assert data["original_group_column_denominator"] == str(group_denominator)
        assert data["field_component"] == component and data["regular_degree_bound"] == degree
        denominator = int(data["common_positive_denominator"])
        assert denominator > 0
        values = [[int(x) for x in row] for row in data["integer_vector_coefficients_low_to_high"]]
        assert len(values) == degree+1 and all(len(row) == FREE for row in values)
        for power, row in enumerate(values):
            for output, value in enumerate(row):
                if power > degree-EPS[output]:
                    assert value == 0
        zero = not any(value for row in values for value in row)
        assert data["exactly_zero_component"] is zero
        answer = {"values": values, "denominator": denominator, "degree": degree,
                  "zero": zero, "source": spec(self.path(name))}
        self.target_vectors[key] = answer
        return answer

    def run(self):
        previous = self.out/FINAL
        if previous.exists():
            old = read(previous)
            assert old["result"] == RESULT and old["complete"] is True
            assert old["configuration"] == self.tag and old["completed_scope"] == SCOPE
            inventory_spec = old["stage_manifest"]
            assert spec(self.path(inventory_spec["file"])) == inventory_spec
            inventory = self.cached(inventory_spec["file"])
            for entry in inventory["files"]:
                assert spec(self.path(entry["file"])) == entry
        self.load_w()
        indexes = {target: self.target_index(target) for target in TARGETS}
        assert not list(self.out.glob("R811-*-CRT-current.json.gz"))
        files = [spec(path) for path in sorted(self.out.glob("R811-*.json.gz"))
                 if not path.name.startswith("R811-R824-stage-manifest-")]
        manifest_name = "R811-R824-stage-manifest-"+fingerprint(files)[:24]
        inventory = self.cached(manifest_name)
        if inventory is None:
            manifest_spec = self.store(manifest_name, {"files": files})
        else:
            assert inventory["files"] == files
            manifest_spec = spec(self.path(manifest_name))
        nonzero_components, prime_counts = {}, {}
        for target in TARGETS:
            entries = self.cached(indexes[target]["file"], target)["field_component_multipliers"]
            data = [self.cached(entry["file"], target) for entry in entries]
            nonzero_components[target] = [i for i, value in enumerate(data)
                                          if not value["zero_component_proved_from_exact_original_vector"]]
            assert nonzero_components[target], "Original nonzero A or B vector cannot vanish in all14 field components."
            prime_counts[target] = [value["actual_CRT_prime_count"] for value in data]
        certificate = {
            "result": RESULT, "complete": True, "configuration": self.tag, "p": 41,
            "completed_scope": SCOPE, "requested_targets": list(TARGETS),
            "normal_affine_basis_rank": FREE, "normal_basis_degrees": EPS,
            "coefficient_field_basis": FIELD_BASIS,
            "actual_sigma_integer_n": self.r806.tag["actual_sigma_integer_n"],
            "source_R806_polynomial_multiplier": self.w_spec,
            "source_R806_cyclic_witness": self.witness_spec,
            "source_R809_S5_basis_index": self.s5_spec,
            "source_R809_normal_vectors": self.target_specs,
            "actual_input_producers": {
                "R806": producer_identity(self.r806.identity), "R809": producer_identity(self.r809.identity),
                "R809_basis": producer_identity(self.r809_basis.identity)},
            "original_S5_configuration_preserved": True,
            "source_original_S5_producer": producer_identity(self.r809_basis.identity),
            "source_original_S5_configuration_sha256": fingerprint(self.r809_basis.tag),
            "actual_R824_source": self.r809.certificate["actual_R824_source"],
            "actual_R824_relation": self.r809.certificate["actual_R824_relation"],
            "actual_R824_free_column": self.r809.certificate["original_R824_free_column"],
            "actual_normal_input_result": R809_AB_RESULT,
            "synthetic_R787_or_C_only_R809_A_B_output_created": False,
            "original_relation_denominator_or_content_reinserted": False,
            "target_multipliers": indexes, "actual_nonzero_field_components": nonzero_components,
            "actual_CRT_prime_counts_by_field_component": prime_counts,
            "original_y_operator_pair": {"numerator": "A", "denominator": "B",
                "tau_chart": "(A/tau^5)/(B/tau^5)",
                "sigma_chart": "(A/sigma^5)/(B/sigma^5)",
                "common_t_power_cancels_exactly": 5, "source_B_actually_nonzero": True},
            "regular_multipliers_computed": True, "two_chart_regular_pairs_computed": True,
            "all_weighted_degree_bounds_verified": True,
            "all_original_first_columns_verified_coefficientwise": True,
            "commutator_maximum_degree": 8, "exact_commutator_points": list(range(9)),
            "all_complete_polynomial_commutator_identities_verified": True,
            "all_original_scalar_and_field_normalizations_preserved": True,
            "normal_integral_basis_preserved": True,
            "old_Fourier_Hom_Laurent_S5_or_Dixon_producer_results_recomputed": False,
            "characteristic_zero_Krylov_matrix_or_inverse_computed": False,
            "base_polar_preimages_computed": False,
            "five_original_function_DAG_computed": False,
            "eta_or_height_computed": False,
            "stage_manifest": manifest_spec, "seconds": time.monotonic()-self.started,
        }
        save(previous, certificate)
        save(self.out/"core-receipt.json", {
            "result": RESULT, "complete": True, "source_sha256": sha(__file__),
            "certificate_sha256": sha(previous), "completed_scope": SCOPE,
            "regular_multipliers_computed": True,
            "all_complete_polynomial_commutator_identities_verified": True,
            "base_polar_preimages_computed": False, "eta_or_height_computed": False,
        })
        return 0


def main():
    base.guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "proof", "method", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    try:
        return Job(args).run()
    except base.BudgetStop as error:
        args.output.mkdir(parents=True, exist_ok=True)
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "budget_stop": str(error),
            "completed_source_bound_stages_and_current_CRT_preserved": True,
            "base_polar_preimages_computed": False, "eta_or_height_computed": False})
        return 124
    except BaseException as error:
        args.output.mkdir(parents=True, exist_ok=True)
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "error": type(error).__name__+": "+str(error),
            "completed_source_bound_stages_and_current_CRT_preserved": True,
            "base_polar_preimages_computed": False, "eta_or_height_computed": False})
        raise

if __name__ == "__main__":
    raise SystemExit(main())
