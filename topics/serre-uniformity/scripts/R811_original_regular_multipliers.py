#!/usr/bin/env python3
"""R811 first scope: original A/B regular multipliers, without a rational Krylov inverse.

All arithmetic is confined to the public repository Actions.  This core does not
implement the later polynomial-ideal preimage or the five-function DAG.
"""
import argparse
import gc
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpq, fmpz, fmpz_mat, nmod_mat

RESULT = "R811-original-regular-multipliers-and-polar-preimages"
FINAL = "p41-original-regular-multiplier-certificate.json"
FREE, LDEG, S5, S3 = 272, 14, 1234, 690
EPS = [0]+[1]*144+[2]*127
FIELD_BASIS = "b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b"
R806_RESULT = "R806-original-primitive-multiplication"
R809_RESULT = "R809-original-S5-normal-coordinates"
SCOPE = "base_regular_multipliers"
TARGETS = ("A", "B")


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("All new exact arithmetic belongs to public repository Actions.")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name+".tmp")
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        with tmp.open("wb") as stream:
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb", mtime=0, compresslevel=2) as compressed:
                compressed.write(raw)
    else:
        tmp.write_bytes(raw)
    tmp.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def plain(value):
    return {key: value[key] for key in ("file", "bytes", "sha256")}


def producer_identity(value):
    out = {key: value[key] for key in
           ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256", "certificate_name")}
    out["certificate_sha256"] = value["files"][value["certificate_name"]]
    return out


def same_producer(left, right):
    if "files" in left:
        left = producer_identity(left)
    if "files" in right:
        right = producer_identity(right)
    assert set(left) == set(right)
    for key in left:
        assert str(left[key]) == str(right[key]), ("Original mathematical producer identity changed.", key)


def rows(matrix, strings=False):
    convert = str if strings else int
    return [[convert(matrix[i, j]) for j in range(matrix.ncols())]
            for i in range(matrix.nrows())]


def matrix_block(matrix, first, stop):
    return fmpz_mat([[int(matrix[i, j]) for j in range(matrix.ncols())]
                     for i in range(first, stop)])


def integer_evaluate(coefficients, point):
    answer = fmpz_mat(FREE, FREE)
    for coefficient in reversed(coefficients):
        answer = answer*point+coefficient
    return answer


def rational_reconstruct(value, modulus):
    value %= modulus
    if not value:
        return fmpq(0)
    bound = math.isqrt((modulus-1)//2)
    assert 2*bound*bound < modulus
    r0, r1, t0, t1 = modulus, value, 0, 1
    while abs(r1) > bound:
        quotient = r0//r1
        r0, r1, t0, t1 = r1, r0-quotient*r1, t1, t0-quotient*t1
    if not t1 or abs(t1) > bound or math.gcd(r1, t1) != 1:
        return None
    if t1 < 0:
        r1, t1 = -r1, -t1
    if (value*t1-r1) % modulus:
        return None
    return fmpq(r1, t1)


def interpolation_weights(points, prime):
    """Coefficient row k contains L_i's z^k for the exact Lagrange polynomials."""
    count = len(points)
    assert len(set(points)) == count and all(0 <= point < prime for point in points)
    answer = [[0]*count for _ in range(count)]
    for i, point in enumerate(points):
        coefficients, denominator = [1], 1
        for j, other in enumerate(points):
            if i == j:
                continue
            updated = [0]*(len(coefficients)+1)
            for k, value in enumerate(coefficients):
                updated[k] = (updated[k]-other*value) % prime
                updated[k+1] = (updated[k+1]+value) % prime
            coefficients = updated
            denominator = denominator*(point-other) % prime
        inverse = pow(denominator, -1, prime)
        for k, value in enumerate(coefficients):
            answer[k][i] = value*inverse % prime
    return answer


def S3_position(index):
    if index < 4:
        return 0, index
    if index < 436:
        return 1+(index-4)//3, (index-4) % 3
    return 145+(index-436)//2, (index-436) % 2


class BudgetStop(RuntimeError):
    pass


class Retained:
    def __init__(self, root, label, identity):
        self.root, self.label, self.identity = Path(root)/label, label, identity
        manifest_path = self.root/"full-outputs-manifest.json"
        assert sha(manifest_path) == identity["manifest_sha256"]
        manifest = read(manifest_path)
        assert manifest["result"] == identity["result"]
        self.files = {entry["file"]: entry for entry in manifest["files"]}
        assert len(self.files) == len(manifest["files"])
        self.checked = set()
        run, core, initial = (self.raw(name) for name in
            ("run-receipt.json", "core-receipt.json", "public-actions-input.json"))
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert str(run["workflow_run_id"]) == str(identity["run_id"])
        assert run["result"] == core["result"] == initial["result"] == identity["result"]
        assert run["source_commit"] == initial["source_commit"] == identity["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == identity["core_sha256"]
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        assert core["complete"] is True and core["source_sha256"] == identity["core_sha256"]
        name = identity["certificate_name"]
        assert core["certificate_sha256"] == self.files[name]["sha256"] == identity["files"][name]
        self.certificate = self.raw(name)
        assert self.certificate["complete"] is True and self.certificate["result"] == identity["result"]
        self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == identity["core_sha256"]
        assert self.tag["python_flint"] == "0.9.0"
        self.initial = initial
        inventory_spec = self.certificate["stage_manifest"]
        inventory = self.stage(inventory_spec)
        self.inventory = {entry["file"]: plain(entry) for entry in inventory["files"]}
        assert len(self.inventory) == len(inventory["files"])
        for name, entry in self.inventory.items():
            assert entry == plain(self.files[name])

    def raw(self, name, expected=None):
        assert Path(name).name == name
        entry = self.files[name]
        if expected is not None:
            assert plain(entry) == plain(expected)
        if name in self.identity["files"]:
            assert entry["sha256"] == self.identity["files"][name]
        path = self.root/name
        if name not in self.checked:
            assert path.stat().st_size == entry["bytes"] and sha(path) == entry["sha256"]
            self.checked.add(name)
        return read(path)

    def stage(self, entry):
        value = self.raw(entry["file"], entry)
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def indexed(self, entry):
        assert self.inventory[entry["file"]] == plain(entry)
        return self.stage(entry)

    def source(self, entry):
        assert plain(self.files[entry["file"]]) == plain(entry)
        return dict(plain(entry), producer=self.label)


class Job:
    def __init__(self, args):
        self.args, self.out, self.started = args, args.output, time.monotonic()
        self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        assert self.item["producer_inputs_pending"] is False
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert self.item["core_sha256"] == sha(__file__)
        assert sha(args.proof) == self.item["R811_proof_sha256"]
        assert sha(args.method) == self.item["R811_method_sha256"]
        assert flint.__version__ == "0.9.0"
        assert self.item["requested_stage"] == SCOPE
        assert self.item["requested_targets"] == list(TARGETS)
        assert self.item["auxiliary_prime_start"] == 1000000007
        assert self.item["matrix_row_block_size"] == 16
        assert self.item["reconstruct_every_primes"] >= 1
        assert self.item["exact_commutator_mode"] == "deterministic_integer_points_with_weighted_degree_bound"
        assert set(self.item["retained_artifacts"]) == {"R806", "R809"}
        self.r806 = Retained(args.retained, "R806", self.item["retained_artifacts"]["R806"])
        self.r809 = Retained(args.retained, "R809", self.item["retained_artifacts"]["R809"])
        assert self.r806.identity["result"] == R806_RESULT
        assert self.r809.identity["result"] == R809_RESULT
        c806, c809 = self.r806.certificate, self.r809.certificate
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
        assert c809["actual_original_y_normal_vectors_computed"] is True
        assert c809["original_scalar_and_field_normalizations_preserved"] is True
        assert c809["coefficient_field_basis"] == FIELD_BASIS
        assert set(TARGETS) <= set(c809["completed_target_groups"])
        same_producer(self.r806.tag["retained_artifacts"]["R805"],
                      self.r809.tag["basis_producers"]["R805"])
        assert self.r806.tag["actual_sigma_integer_n"] == self.r809.tag["actual_sigma_integer_n"]
        self.w_spec = c806["polynomial_multiplier"]
        self.w_interface = self.r806.indexed(self.w_spec)
        interface = self.w_interface
        assert interface["normal_affine_basis_rank"] == FREE
        assert interface["normal_affine_basis_degrees"] == EPS
        assert interface["coefficient_field"] == "Q, certified by exact original rational coordinate equations"
        assert interface["matrix_convention"] == "M_ba(z) is output row b, input column a"
        assert interface["coordinate_groups"] == c806["exact_coordinate_groups"]
        assert interface["original_R805_free_basis"] == self.r809.tag["original_graded_free_basis"]
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
        self.s5_index = self.r809.indexed(self.s5_spec)
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
            "p": 41, "normal_affine_basis_rank": FREE, "normal_basis_degrees": EPS,
            "coefficient_field_basis": FIELD_BASIS,
            "R806_producer": producer_identity(self.r806.identity),
            "R806_polynomial_multiplier": self.w_spec, "R806_cyclic_witness": self.witness_spec,
            "R809_basis_configuration_sha256": fingerprint(self.r809.tag),
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

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes-45:
            raise BudgetStop("Completed original multipliers and current exact CRT states retained.")

    def path(self, name):
        assert name.startswith("R811-") and Path(name).name == name
        return self.out/(name if name.endswith(".json.gz") else name+".json.gz")

    def cached(self, name, target=None, current=False):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["configuration"] == self.tag
        assert value["complete"] is (not current)
        if target is not None:
            assert value["target_configuration"] == self.target_tags[target]
            assert value["target_configuration_sha256"] == fingerprint(self.target_tags[target])
        else:
            assert "target_configuration" not in value
        return value

    def store(self, name, value, target=None, current=False, replace=False):
        path = self.path(name)
        assert current or replace or not path.exists(), "A completed mathematical stage cannot be overwritten."
        if current:
            assert name.endswith("-current") or name.endswith("-current.json.gz")
        value = dict(value, complete=not current, configuration=self.tag)
        if target is not None:
            value["target_configuration"] = self.target_tags[target]
            value["target_configuration_sha256"] = fingerprint(self.target_tags[target])
        save(path, value)
        return spec(path)

    def source_stage(self, name, target=None):
        value = self.cached(name, target)
        assert value is not None
        return value, spec(self.path(name))

    def prime_at(self, index):
        while len(self.prime_values) <= index:
            value = self.item["auxiliary_prime_start"] if not self.prime_values else self.prime_values[-1]+2
            while not fmpz(value).is_prime():
                value += 2
            assert self.search_degree+16 < value < 2**63
            self.prime_values.append(value)
        return self.prime_values[index]

    def load_w(self):
        if self.w_coefficients is not None:
            return
        name = "R811-original-primitive-polynomial-input"
        data = self.cached(name)
        mapping = self.w_interface["S_row_to_polynomial_coefficient"]
        assert len(mapping) == S3
        for index, entry in enumerate(mapping):
            assert entry == {"S_row": index, "normal_basis_row": S3_position(index)[0],
                             "power_of_z": S3_position(index)[1]}
        if data is None:
            denominators, groups, columns = [], [], []
            for entry in self.w_interface["coordinate_groups"]:
                group = self.r806.indexed(entry)
                indices = group["column_indices"]
                assert group["all820_original_coordinates_verified"] is True
                assert group["weighted_polynomial_support_verified"] is True
                assert group["reduction_equals_successful_modular_multiplier"] is True
                assert group["integer_scale"] == str(82**6)
                assert len(group["coordinate_numerators"]) == S3
                assert all(len(row) == len(indices) for row in group["coordinate_numerators"])
                ds = [int(x) for x in group["column_denominators"]]
                assert len(ds) == len(indices) and all(x > 0 for x in ds)
                denominators.extend(ds)
                columns.extend(indices)
                groups.append(group)
            assert columns == list(range(FREE))
            denominator = math.lcm(*denominators)
            coefficients = [fmpz_mat(FREE, FREE) for _ in range(4)]
            for group in groups:
                for local, column in enumerate(group["column_indices"]):
                    factor = denominator//int(group["column_denominators"][local])
                    for index, row in enumerate(group["coordinate_numerators"]):
                        output, power = S3_position(index)
                        value = int(row[local])*factor
                        if power > 1+EPS[column]-EPS[output]:
                            assert value == 0
                        coefficients[power][output, column] = value
            self.store(name, {
                "source_polynomial_multiplier": self.w_spec,
                "source_exact_coordinate_groups": self.w_interface["coordinate_groups"],
                "normal_affine_basis_rank": FREE, "normal_basis_degrees": EPS,
                "common_positive_denominator": str(denominator),
                "integer_coefficient_matrices_low_to_high": [rows(x, strings=True) for x in coefficients],
                "coefficient_convention": "M_w(z)=sum z^k integer_matrix[k]/common_positive_denominator",
                "original_scaled_S3_coordinates_consumed_exactly_once": True,
                "weighted_support_verified": True,
                "old_original_product_Dixon_or_cyclic_search_recomputed": False,
            })
            data = self.cached(name)
        assert data["source_polynomial_multiplier"] == self.w_spec
        assert data["source_exact_coordinate_groups"] == self.w_interface["coordinate_groups"]
        assert data["normal_affine_basis_rank"] == FREE and data["normal_basis_degrees"] == EPS
        assert data["weighted_support_verified"] is True
        self.w_denominator = int(data["common_positive_denominator"])
        assert self.w_denominator > 0
        raw = data["integer_coefficient_matrices_low_to_high"]
        assert len(raw) == 4 and all(len(x) == FREE for x in raw)
        assert all(len(row) == FREE for matrix in raw for row in matrix)
        self.w_coefficients = [fmpz_mat([[int(x) for x in row] for row in matrix]) for matrix in raw]
        for power, matrix in enumerate(self.w_coefficients):
            for output in range(FREE):
                for column in range(FREE):
                    if power > 1+EPS[column]-EPS[output]:
                        assert matrix[output, column] == 0
        self.w_input_spec = spec(self.path(name))

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
                "no_R787_removed_common_denominator_or_content_reinserted": True,
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

    def point(self, prime, point):
        self.load_w()
        assert self.w_denominator % prime and 0 <= point < prime
        name = "R811-prime-"+str(prime)+"-z-"+str(point)+"-Krylov-inverse"
        data = self.cached(name)
        if data is None:
            self.budget()
            inverse_denominator = pow(self.w_denominator, -1, prime)
            integer_matrix = integer_evaluate(self.w_coefficients, point)
            matrix = nmod_mat([[int(integer_matrix[i, j])*inverse_denominator % prime
                               for j in range(FREE)] for i in range(FREE)], prime)
            reused = prime == self.witness["prime"] and point == self.witness["z0"]
            if reused:
                raw = self.witness["successful_krylov_matrix_mod_prime"]
                assert len(raw) == FREE and all(len(row) == FREE for row in raw)
                krylov = nmod_mat([[int(x) % prime for x in row] for row in raw], prime)
                determinant = int(self.witness["actual_determinant_mod_prime"]) % prime
                assert determinant
            else:
                vector = nmod_mat([[int(i == 0)] for i in range(FREE)], prime)
                columns = []
                for exponent in range(FREE):
                    columns.append([int(vector[i, 0]) for i in range(FREE)])
                    if exponent+1 < FREE:
                        vector = matrix*vector
                krylov = nmod_mat(columns, prime).transpose()
                determinant = int(krylov.det())
            payload = {
                "prime": prime, "z0": point, "source_original_primitive_matrix": self.w_input_spec,
                "source_R806_cyclic_witness": self.witness_spec,
                "normal_affine_basis_rank": FREE, "actual_determinant_mod_prime": determinant,
                "usable": bool(determinant), "original_R806_successful_Krylov_matrix_reused": reused,
                "characteristic_zero_Krylov_matrix_or_inverse_computed": False,
                "failure_means_only_this_modular_specialization": not bool(determinant),
            }
            if determinant:
                inverse = krylov.inv()
                identity = nmod_mat([[int(i == j) for j in range(FREE)] for i in range(FREE)], prime)
                assert krylov*inverse == identity and inverse*krylov == identity
                payload.update({
                    "W_evaluated_mod_prime": rows(matrix),
                    "inverse_Krylov_matrix_mod_prime": rows(inverse),
                    "Krylov_matrix_sha256": fingerprint(rows(krylov)),
                    "actual_cyclic_rank": FREE, "both_inverse_products_verified": True,
                    "Krylov_column_order": "1,w,...,w^271 in original normal basis",
                })
            self.store(name, payload)
            data = self.cached(name)
        assert data["prime"] == prime and data["z0"] == point
        assert data["source_original_primitive_matrix"] == self.w_input_spec
        assert data["source_R806_cyclic_witness"] == self.witness_spec
        assert data["usable"] is bool(data["actual_determinant_mod_prime"])
        if data["usable"]:
            assert data["actual_cyclic_rank"] == FREE and data["both_inverse_products_verified"] is True
            for key in ("W_evaluated_mod_prime", "inverse_Krylov_matrix_mod_prime"):
                assert len(data[key]) == FREE and all(len(row) == FREE for row in data[key])
        return data, spec(self.path(name))

    def grid(self, prime, degree):
        self.load_w()
        name = "R811-prime-"+str(prime)+"-regular-grid-r"+str(degree)
        data = self.cached(name)
        if data is None:
            needed = degree+3
            if self.w_denominator % prime == 0:
                self.store(name, {
                    "prime": prime, "regular_degree_bound": degree, "usable": False,
                    "source_original_primitive_matrix": self.w_input_spec,
                    "reason": "Original rational M_w denominator is not a unit.",
                    "characteristic_zero_failure_claimed": False,
                })
                return self.cached(name), spec(self.path(name))
            seed = self.witness["z0"] % prime
            seed_data, seed_spec = self.point(prime, seed)
            if not seed_data["usable"]:
                self.store(name, {
                    "prime": prime, "regular_degree_bound": degree, "usable": False,
                    "source_original_primitive_matrix": self.w_input_spec,
                    "source_seed_point": seed_spec,
                    "reason": "The fixed characteristic-zero cyclic seed specializes singularly at this prime.",
                    "characteristic_zero_failure_claimed": False,
                })
                return self.cached(name), spec(self.path(name))
            points, point_specs = [seed], [seed_spec]
            for point in range(self.search_degree+needed):
                self.budget()
                if len(points) == needed:
                    break
                if point == seed:
                    continue
                point_data, point_spec = self.point(prime, point)
                if point_data["usable"]:
                    points.append(point)
                    point_specs.append(point_spec)
            assert len(points) == needed and len(set(points)) == needed
            weights = interpolation_weights(points, prime)
            # Full Vandermonde identity certifies the exact interpolation convention.
            vandermonde = nmod_mat([[pow(point, k, prime) for k in range(needed)]
                                   for point in points], prime)
            inverse = nmod_mat(weights, prime)
            identity = nmod_mat([[int(i == j) for j in range(needed)] for i in range(needed)], prime)
            assert inverse*vandermonde == identity and vandermonde*inverse == identity
            self.store(name, {
                "prime": prime, "regular_degree_bound": degree, "usable": True,
                "source_original_primitive_matrix": self.w_input_spec,
                "modular_interpolation_points": points, "Krylov_point_stages": point_specs,
                "Lagrange_coefficient_weights": weights,
                "actual_point_count": needed, "polynomial_maximum_degree": degree+2,
                "Vandermonde_both_inverse_products_verified": True,
                "fixed_seed_success_certifies_nonzero_cyclic_polynomial_mod_prime": True,
                "no_splitting_prime_of_L_required": True,
            })
            data = self.cached(name)
        assert data["prime"] == prime and data["regular_degree_bound"] == degree
        assert data["source_original_primitive_matrix"] == self.w_input_spec
        if data["usable"]:
            assert data["actual_point_count"] == degree+3
            assert len(data["modular_interpolation_points"]) == len(data["Krylov_point_stages"]) == degree+3
            assert data["Vandermonde_both_inverse_products_verified"] is True
        return data, spec(self.path(name))

    def component_stem(self, target, component):
        return "R811-target-"+target+"-component-"+str(component).zfill(2)

    def prime_point_multiplier(self, target, component, prime, point, point_spec):
        vector_data = self.target_component(target, component)
        degree = vector_data["degree"]
        assert vector_data["denominator"] % prime
        stem = self.component_stem(target, component)+"-prime-"+str(prime)
        name = stem+"-z-"+str(point)+"-modular-multiplier"
        data = self.cached(name, target)
        if data is None:
            self.budget()
            point_data = self.cached(point_spec["file"])
            assert spec(self.path(point_spec["file"])) == point_spec
            assert point_data["usable"] and point_data["prime"] == prime and point_data["z0"] == point
            inverse = nmod_mat(point_data["inverse_Krylov_matrix_mod_prime"], prime)
            matrix = nmod_mat(point_data["W_evaluated_mod_prime"], prime)
            denominator_inverse = pow(vector_data["denominator"], -1, prime)
            value = [0]*FREE
            for power in reversed(range(degree+1)):
                value = [(entry*point+vector_data["values"][power][i]) % prime
                         for i, entry in enumerate(value)]
            value = [entry*denominator_inverse % prime for entry in value]
            vector = nmod_mat([[entry] for entry in value], prime)
            columns = []
            for exponent in range(FREE):
                columns.append([int(vector[i, 0]) for i in range(FREE)])
                if exponent+1 < FREE:
                    vector = matrix*vector
            Kf = nmod_mat(columns, prime).transpose()
            answer = Kf*inverse
            assert all(int(answer[i, 0]) == value[i] for i in range(FREE))
            assert answer*matrix == matrix*answer
            self.store(name, {
                "target": target, "field_component": component, "prime": prime, "z0": point,
                "source_original_vector": vector_data["source"], "source_Krylov_point": point_spec,
                "matrix_mod_prime": rows(answer),
                "matrix_convention": "M_f=K_f*K_inverse; column input, row output",
                "full_first_column_and_commutator_verified_mod_prime": True,
                "exact_characteristic_zero_multiplier_claimed": False,
            }, target)
            data = self.cached(name, target)
        assert data["source_original_vector"] == vector_data["source"]
        assert data["source_Krylov_point"] == point_spec
        assert data["prime"] == prime and data["z0"] == point
        assert data["field_component"] == component
        assert data["full_first_column_and_commutator_verified_mod_prime"] is True
        assert len(data["matrix_mod_prime"]) == FREE and all(len(row) == FREE for row in data["matrix_mod_prime"])
        return data, spec(self.path(name))

    def coefficient_count(self, degree, first=0, stop=FREE):
        return sum(max(0, degree+EPS[column]-EPS[output]+1)
                   for output in range(first, stop) for column in range(FREE))

    def modular_image(self, target, component, prime, grid_data, grid_spec):
        vector = self.target_component(target, component)
        degree = vector["degree"]
        stem = self.component_stem(target, component)+"-prime-"+str(prime)
        index_name = stem+"-modular-image-index"
        index = self.cached(index_name, target)
        if index is None:
            point_data, point_specs = [], []
            for point, entry in zip(grid_data["modular_interpolation_points"], grid_data["Krylov_point_stages"]):
                data, source = self.prime_point_multiplier(target, component, prime, point, entry)
                point_data.append(data["matrix_mod_prime"])
                point_specs.append(source)
            weights = nmod_mat(grid_data["Lagrange_coefficient_weights"], prime)
            block_specs = []
            inverse_denominator = pow(vector["denominator"], -1, prime)
            for first, stop in self.block_ranges:
                self.budget()
                name = stem+"-interpolated-rows-"+str(first).zfill(3)+"-"+str(stop).zfill(3)
                block = self.cached(name, target)
                if block is None:
                    specialized = nmod_mat([
                        [point_data[i][b][a] for b in range(first, stop) for a in range(FREE)]
                        for i in range(degree+3)], prime)
                    coefficients = weights*specialized
                    values = []
                    for output in range(first, stop):
                        for column in range(FREE):
                            local = (output-first)*FREE+column
                            bound = degree+EPS[column]-EPS[output]
                            for power in range(degree+3):
                                value = int(coefficients[power, local])
                                if power > bound:
                                    assert value == 0, "Interpolation violates the original weighted polynomial bound."
                                else:
                                    values.append(value)
                                    if column == 0:
                                        expected = vector["values"][power][output] if power <= degree else 0
                                        assert value == expected*inverse_denominator % prime
                    assert len(values) == self.coefficient_count(degree, first, stop)
                    self.store(name, {
                        "target": target, "field_component": component, "prime": prime,
                        "source_original_vector": vector["source"], "source_grid": grid_spec,
                        "source_point_multipliers": point_specs,
                        "row_first": first, "row_stop": stop, "regular_degree_bound": degree,
                        "entry_order": "output_row, input_column, power=0..r+eps_column-eps_row",
                        "coefficients_mod_prime": values,
                        "weighted_support_and_original_first_column_verified": True,
                        "exact_characteristic_zero_multiplier_claimed": False,
                    }, target)
                    block = self.cached(name, target)
                assert block["source_original_vector"] == vector["source"] and block["source_grid"] == grid_spec
                assert block["source_point_multipliers"] == point_specs
                assert (block["row_first"], block["row_stop"]) == (first, stop)
                assert block["weighted_support_and_original_first_column_verified"] is True
                assert len(block["coefficients_mod_prime"]) == self.coefficient_count(degree, first, stop)
                block_specs.append(spec(self.path(name)))
            self.store(index_name, {
                "target": target, "field_component": component, "prime": prime,
                "source_original_vector": vector["source"], "source_grid": grid_spec,
                "point_multipliers": point_specs, "interpolated_blocks": block_specs,
                "regular_degree_bound": degree, "coefficient_count": self.coefficient_count(degree),
                "all_modular_entries_interpolated_in_original_normal_basis": True,
                "weighted_support_and_original_first_column_verified": True,
                "consumable_into_current_CRT_without_future_recomputation": True,
                "full_temporary_images_prunable_only_after_atomic_CRT_commit": True,
            }, target)
            index = self.cached(index_name, target)
        assert index["source_original_vector"] == vector["source"] and index["source_grid"] == grid_spec
        assert index["field_component"] == component and index["prime"] == prime
        assert index["coefficient_count"] == self.coefficient_count(degree)
        values = []
        assert len(index["interpolated_blocks"]) == len(self.block_ranges)
        for entry, (first, stop) in zip(index["interpolated_blocks"], self.block_ranges):
            assert spec(self.path(entry["file"])) == entry
            block = self.cached(entry["file"], target)
            assert (block["row_first"], block["row_stop"]) == (first, stop)
            assert block["prime"] == prime
            assert block["source_original_vector"] == vector["source"] and block["source_grid"] == grid_spec
            values.extend(block["coefficients_mod_prime"])
        assert len(values) == self.coefficient_count(degree)
        assert all(isinstance(value, int) and 0 <= value < prime for value in values)
        index_spec = spec(self.path(index_name))
        temporary = index["point_multipliers"]+index["interpolated_blocks"]+[index_spec]
        return values, index_spec, temporary

    def CRT_history_and_cleanup(self, target, component, current):
        stem = self.component_stem(target, component)
        current_name = stem+"-CRT-current"
        current_spec = spec(self.path(current_name))
        assert current["target"] == target and current["field_component"] == component
        history_name = stem+"-CRT-step-"+str(current["prime_count"]).zfill(6)+"-receipt"
        receipt = {
            "target": target, "field_component": component, "prime_count": current["prime_count"],
            "latest_prime": current["consumed_primes"][-1],
            "latest_prime_index": current["consumed_prime_indices"][-1],
            "modulus_bits": int(current["modulus"]).bit_length(),
            "current_full_CRT_checkpoint": current_spec,
            "previous_checkpoint_sha256": current["previous_checkpoint_sha256"],
            "previous_CRT_receipt": current["previous_CRT_receipt"],
            "source_original_vector": current["source_original_vector"],
            "latest_consumed_modular_image": current["latest_consumed_modular_image"],
            "consumed_modular_temporary_file_history": current["latest_modular_temporary_files"],
            "full_temporary_images_discarded_only_after_CRT_commit": True,
            "large_vector_or_matrix_embedded": False,
            "current_CRT_contains_all_consumed_primes": True,
        }
        prior = self.cached(history_name, target)
        if prior is None:
            self.store(history_name, receipt, target)
        else:
            for key, value in receipt.items():
                assert prior[key] == value
        for entry in current["latest_modular_temporary_files"]:
            path = self.path(entry["file"])
            if path.exists():
                assert spec(path) == entry
                path.unlink()
        return spec(self.path(history_name))

    def candidate_cleanup(self, target, component, attempt, reason, additional=None):
        stem = self.component_stem(target, component)+"-attempt-"+str(attempt).zfill(6)
        name = stem+"-rejected"
        data = self.cached(name, target)
        if data is None:
            remove = [spec(path) for path in sorted(self.out.glob(stem+"-reconstructed-rows-*.json.gz"))]
            candidate = self.path(stem+"-candidate-index")
            if candidate.exists():
                remove.append(spec(candidate))
            data = {"target": target, "field_component": component, "attempt_prime_count": attempt,
                    "reason": reason, "additional": additional,
                    "discarded_candidate_file_history": remove,
                    "no_exact_characteristic_zero_multiplier_claimed": True}
            self.store(name, data, target)
            data = self.cached(name, target)
        for entry in data["discarded_candidate_file_history"]:
            path = self.path(entry["file"])
            if path.exists():
                assert spec(path) == entry
                path.unlink()
        return spec(self.path(name))

    def reconstruct_candidate(self, target, component, current):
        vector = self.target_component(target, component)
        degree, attempt = vector["degree"], current["prime_count"]
        stem = self.component_stem(target, component)+"-attempt-"+str(attempt).zfill(6)
        rejected = self.cached(stem+"-rejected", target)
        if rejected is not None:
            self.candidate_cleanup(target, component, attempt, rejected["reason"], rejected["additional"])
            return None
        current_spec = spec(self.path(self.component_stem(target, component)+"-CRT-current"))
        index_name = stem+"-candidate-index"
        index = self.cached(index_name, target)
        if index is not None:
            assert index["source_CRT_checkpoint"] == current_spec
            return index, spec(self.path(index_name))
        modulus = int(current["modulus"])
        residues = [int(value) for value in current["lifted_coefficients"]]
        bound = math.isqrt((modulus-1)//2)
        assert 2*bound*bound < modulus
        block_specs, offset = [], 0
        for first, stop in self.block_ranges:
            self.budget()
            count = self.coefficient_count(degree, first, stop)
            name = stem+"-reconstructed-rows-"+str(first).zfill(3)+"-"+str(stop).zfill(3)
            block = self.cached(name, target)
            if block is None:
                recovered, denominator = [], 1
                for local in range(count):
                    rational = rational_reconstruct(residues[offset+local], modulus)
                    if rational is None:
                        self.candidate_cleanup(target, component, attempt,
                            "A coefficient has no rational reconstruction in the uniform strict rectangle.",
                            {"coefficient_index": offset+local, "modulus_bits": modulus.bit_length()})
                        return None
                    recovered.append(rational)
                    denominator = math.lcm(denominator, int(rational.denom()))
                assert denominator > 0 and math.gcd(denominator, modulus) == 1
                inverse = pow(denominator, -1, modulus)
                numerators = [int(value.numer())*(denominator//int(value.denom())) for value in recovered]
                assert all(numerator*inverse % modulus == residues[offset+i]
                           for i, numerator in enumerate(numerators))
                self.store(name, {
                    "target": target, "field_component": component, "attempt_prime_count": attempt,
                    "source_original_vector": vector["source"], "source_CRT_checkpoint": current_spec,
                    "row_first": first, "row_stop": stop, "regular_degree_bound": degree,
                    "entry_order": "output_row, input_column, power=0..r+eps_column-eps_row",
                    "common_positive_denominator": str(denominator),
                    "coefficient_numerators": [str(value) for value in numerators],
                    "uniform_rational_reconstruction_bound": str(bound),
                    "all_reconstructed_fractions_checked_against_current_CRT": True,
                    "reconstruction_is_only_a_candidate_until_full_exact_identity_verification": True,
                }, target)
                block = self.cached(name, target)
            assert block["source_CRT_checkpoint"] == current_spec
            assert block["source_original_vector"] == vector["source"]
            assert (block["row_first"], block["row_stop"]) == (first, stop)
            assert block["regular_degree_bound"] == degree
            assert block["uniform_rational_reconstruction_bound"] == str(bound)
            assert block["all_reconstructed_fractions_checked_against_current_CRT"] is True
            assert len(block["coefficient_numerators"]) == count
            block_specs.append(spec(self.path(name)))
            offset += count
        assert offset == len(residues) == self.coefficient_count(degree)
        self.store(index_name, {
            "target": target, "field_component": component, "attempt_prime_count": attempt,
            "source_original_vector": vector["source"], "source_CRT_checkpoint": current_spec,
            "regular_degree_bound": degree, "normal_affine_basis_rank": FREE,
            "matrix_row_blocks": block_specs, "coefficient_count": len(residues),
            "uniform_rational_reconstruction_bound": str(bound), "CRT_modulus": current["modulus"],
            "matrix_convention": "M_ba output b input a",
            "complete_characteristic_zero_identity_verified": False,
        }, target)
        return self.cached(index_name, target), spec(self.path(index_name))

    def component(self, target, component):
        self.load_w()
        vector = self.target_component(target, component)
        stem = self.component_stem(target, component)
        complete_name = stem+"-certified-multiplier-index"
        old = self.cached(complete_name, target)
        if old is not None:
            self.validate_completed_component(target, component, spec(self.path(complete_name)))
            assert old["source_original_vector"] == vector["source"]
            assert old["original_first_column_verified_coefficientwise"] is True
            assert old["complete_polynomial_commutator_identity_verified"] is True
            current = self.cached(stem+"-CRT-current", target, current=True)
            if current is not None:
                self.CRT_history_and_cleanup(target, component, current)
                self.path(stem+"-CRT-current").unlink()
            return spec(self.path(complete_name))
        if vector["zero"]:
            self.store(complete_name, {
                "target": target, "field_component": component,
                "source_original_vector": vector["source"], "regular_degree_bound": vector["degree"],
                "coefficient_field_basis": FIELD_BASIS,
                "zero_component_proved_from_exact_original_vector": True,
                "tau_chart_matrix_is_exact_zero": True, "sigma_chart_matrix_is_exact_zero": True,
                "matrix_row_blocks_tau": [], "matrix_row_blocks_sigma": [],
                "weighted_degree_bound_verified": True,
                "original_first_column_verified_coefficientwise": True,
                "complete_polynomial_commutator_identity_verified": True,
                "zero_identity_follows_exactly_without_modular_zero_assumption": True,
                "all_original_scalar_and_field_normalizations_preserved": True,
                "actual_CRT_prime_count": 0,
            }, target)
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
                    accepted, index_spec = self.verify_and_transport(target, component, current, *candidate)
                    if accepted:
                        self.path(current_name).unlink(missing_ok=True)
                        return index_spec
            prime_index, prime = next_index, self.prime_at(next_index)
            next_index += 1
            if vector["denominator"] % prime == 0:
                name = stem+"-prime-"+str(prime)+"-rejected-vector-denominator"
                if self.cached(name, target) is None:
                    self.store(name, {
                        "target": target, "field_component": component, "prime": prime,
                        "source_original_vector": vector["source"],
                        "reason": "The exact original vector denominator is not a unit.",
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
            print(json.dumps({"stage": "CRT_regular_multiplier", "target": target, "field_component": component,
                              "prime_count": len(primes), "prime": prime, "modulus_bits": modulus.bit_length(),
                              "coefficient_count": len(values), "seconds": time.monotonic()-self.started}), flush=True)

    def verify_and_transport(self, target, component, current, candidate, candidate_spec):
        vector = self.target_component(target, component)
        degree, attempt = vector["degree"], current["prime_count"]
        stem = self.component_stem(target, component)
        attempt_stem = stem+"-attempt-"+str(attempt).zfill(6)
        assert candidate["source_original_vector"] == vector["source"]
        assert candidate["source_CRT_checkpoint"] == spec(self.path(stem+"-CRT-current"))
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
                        rejection = self.candidate_cleanup(target, component, attempt,
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
                            rejection = self.candidate_cleanup(target, component, attempt,
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
        current_receipt = self.CRT_history_and_cleanup(target, component, current)
        complete_name = stem+"-certified-multiplier-index"
        self.store(complete_name, {
            "target": target, "field_component": component,
            "source_original_vector": vector["source"], "regular_degree_bound": degree,
            "coefficient_field_basis": FIELD_BASIS,
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

    def validate_completed_component(self, target, component, entry):
        """Follow the complete output references; missing arrays cannot masquerade as a resume."""
        assert spec(self.path(entry["file"])) == entry
        value = self.cached(entry["file"], target)
        assert value["target"] == target and value["field_component"] == component
        assert value["source_original_vector"] == self.target_component(target, component)["source"]
        assert value["weighted_degree_bound_verified"] is True
        assert value["original_first_column_verified_coefficientwise"] is True
        assert value["complete_polynomial_commutator_identity_verified"] is True
        if value["zero_component_proved_from_exact_original_vector"]:
            assert self.target_component(target, component)["zero"] is True
            assert value["matrix_row_blocks_tau"] == value["matrix_row_blocks_sigma"] == []
            return value
        candidate_spec = value["source_candidate"]
        assert spec(self.path(candidate_spec["file"])) == candidate_spec
        candidate = self.cached(candidate_spec["file"], target)
        assert candidate["matrix_row_blocks"] == value["matrix_row_blocks_tau"]
        assert candidate["source_original_vector"] == value["source_original_vector"]
        assert len(value["matrix_row_blocks_tau"]) == len(value["matrix_row_blocks_sigma"]) == len(self.block_ranges)
        for tau_spec, sigma_spec, (first, stop) in zip(
                value["matrix_row_blocks_tau"], value["matrix_row_blocks_sigma"], self.block_ranges):
            for block_spec in (tau_spec, sigma_spec):
                assert spec(self.path(block_spec["file"])) == block_spec
                block = self.cached(block_spec["file"], target)
                assert (block["row_first"], block["row_stop"]) == (first, stop)
                assert block["target"] == target and block["field_component"] == component
                assert int(block["common_positive_denominator"]) > 0
                assert len(block["coefficient_numerators"]) == self.coefficient_count(
                    value["regular_degree_bound"], first, stop)
            sigma = self.cached(sigma_spec["file"], target)
            assert sigma["source_tau_matrix_row_block"] == tau_spec
            assert sigma["source_exact_candidate"] == candidate_spec
            assert sigma["every_transition_exponent_nonnegative"] is True
            assert sigma["transported_original_first_column_verified_coefficientwise"] is True
        first_spec = value["exact_first_column_certificate"]
        assert spec(self.path(first_spec["file"])) == first_spec
        first = self.cached(first_spec["file"], target)
        assert first["source_candidate"] == candidate_spec
        assert first["original_first_column_verified_coefficientwise"] is True
        degree = value["regular_degree_bound"]
        assert value["commutator_maximum_degree"] == degree+3
        assert value["exact_commutator_points"] == list(range(degree+4))
        assert len(value["exact_full_matrix_point_certificates"]) == degree+4
        for point, point_spec in zip(value["exact_commutator_points"],
                                     value["exact_full_matrix_point_certificates"]):
            assert spec(self.path(point_spec["file"])) == point_spec
            point_data = self.cached(point_spec["file"], target)
            assert point_data["source_candidate"] == candidate_spec
            assert point_data["source_original_M_w"] == self.w_input_spec
            assert point_data["exact_integer_point"] == point
            assert point_data["all_exact_commutator_entries_zero"] is True
            assert len(point_data["full_row_block_certificates"]) == len(self.block_ranges)
            for block_spec, (first, stop) in zip(point_data["full_row_block_certificates"], self.block_ranges):
                assert spec(self.path(block_spec["file"])) == block_spec
                block = self.cached(block_spec["file"], target)
                assert block["source_candidate"] == candidate_spec
                assert block["source_original_M_w"] == self.w_input_spec
                assert (block["row_first"], block["row_stop"]) == (first, stop)
                assert block["exact_integer_point"] == point and block["column_count"] == FREE
                assert block["all_exact_integer_commutator_entries_zero"] is True
        receipt_spec = value["latest_CRT_history_receipt"]
        assert spec(self.path(receipt_spec["file"])) == receipt_spec
        receipt = self.cached(receipt_spec["file"], target)
        assert receipt["current_full_CRT_checkpoint"] == candidate["source_CRT_checkpoint"]
        assert receipt["prime_count"] == value["actual_CRT_prime_count"]
        return value

    def target_index(self, target):
        components = [self.component(target, component) for component in range(LDEG)]
        for component, entry in enumerate(components):
            self.validate_completed_component(target, component, entry)
        payload = {
            "target": target, "source_R809_normal_vector": self.target_specs[target],
            "regular_degree_bound": 5, "normal_affine_basis_rank": FREE,
            "normal_basis_degrees": EPS, "coefficient_field_basis": FIELD_BASIS,
            "field_component_multipliers": components,
            "reconstruction": "M_target=sum_(c=0..6)b^c*M_c + s*sum_(c=0..6)b^c*M_(c+7)",
            "all14_components_verified_in_original_field_basis": True,
            "all_first_columns_verified_coefficientwise": True,
            "all_complete_polynomial_commutator_identities_verified": True,
            "two_regular_charts_use_original_homogeneous_degree": True,
            "original_target_actually_nonzero": True,
            "normal_integral_basis_preserved": True,
            "original_scalar_and_field_normalizations_preserved": True,
            "actual_polar_ideal_or_eta_or_height_computed": False,
        }
        name = "R811-target-"+target+"-two-chart-regular-multiplier-index"
        old = self.cached(name, target)
        if old is None:
            self.store(name, payload, target)
        else:
            for key, value in payload.items():
                assert old[key] == value
        return spec(self.path(name))

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
                 if not path.name.startswith("R811-stage-manifest-")]
        manifest_name = "R811-stage-manifest-"+fingerprint(files)[:24]
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
                "R806": producer_identity(self.r806.identity), "R809": producer_identity(self.r809.identity)},
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
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "proof", "method", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    try:
        return Job(args).run()
    except BaseException as error:
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "error": type(error).__name__+": "+str(error),
            "completed_source_bound_stages_and_current_CRT_preserved": True,
            "base_polar_preimages_computed": False, "eta_or_height_computed": False,
        })
        raise


if __name__ == "__main__":
    sys.exit(main())
