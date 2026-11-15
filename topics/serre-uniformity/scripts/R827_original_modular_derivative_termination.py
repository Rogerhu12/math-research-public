#!/usr/bin/env python3
"""R827: a genuine original residue-field certificate for derivative termination.

All new arithmetic is restricted to this public repository's GitHub Actions.
The ordinary q-prefixes, canonical kernel, primitive operator and cusp ideal
are immutable producer inputs.  No characteristic-zero operator CRT is done.
"""
import argparse
import gc
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import time

import flint
from flint import fmpz, nmod_mat, nmod_poly
import R827_finite_polynomial_modules as modules

RESULT = "R827-original-global-modular-derivative-termination"
FINAL = "p41-original-global-modular-derivative-termination-certificate.json"
MODE = "tau_polynomial_Hermite_and_sigma_infinity_rank"
PROOF_SHA = "17e9c828e01e652b1a73281bf2249ae2b39133faae3cf22384a5fd6d6a3d4a71"
FREE, S5, ROWS = 272, 1234, 1380
EPS = [0]+[1]*144+[2]*127
PRIME = 1000000753
LABELS = {"R806", "R813", "R820", "R824", "R809", "R787"}
BASE_KEYS = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
OLD_PREFIX = "R787-prime-1000000753-"
OLD_PINNED = {
    OLD_PREFIX+"chart.json.gz": "47ac1ce2a95781417a4e3b51f2128d2dd4836e5d1793cf2a50793911dcedce96",
    OLD_PREFIX+"selection.json.gz": "a420d94a9a2f56fa449946bac6379f437e7e53120a651d7df95b5f9ef9b07adb",
    OLD_PREFIX+"branch-00.json.gz": "c5b75f48b5c5d1cf2d98390e814a245306fa63f10ae43dae194dbfd560d895d7",
    OLD_PREFIX+"rational-blocks.json.gz": "fb8a82957474e657fc476aa2baa0d8ce9f4c8b6cc86c2b55a79e75913d610b3b",
}


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Original R827 arithmetic belongs to this public repository's Actions.")


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for data in iter(lambda: stream.read(1024*1024), b""):
            digest.update(data)
    return digest.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    modules.generic.save(path, value)


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def plain(value):
    return {key: value[key] for key in ("file", "bytes", "sha256")}


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def same_identity(left, right):
    for key in BASE_KEYS:
        assert str(left[key]) == str(right[key]), ("Changed original producer", key)


def matrix_rows(matrix):
    return [[int(matrix[i, j]) for j in range(matrix.ncols())] for i in range(matrix.nrows())]


def zero(rows=FREE, columns=FREE, prime=PRIME):
    return nmod_mat(rows, columns, [0]*(rows*columns), prime)


def identity(size=FREE, prime=PRIME):
    return nmod_mat([[int(i == j) for j in range(size)] for i in range(size)], prime)


def evaluate(matrices, value, prime=PRIME):
    assert matrices
    result = zero(matrices[0].nrows(), matrices[0].ncols(), prime)
    for matrix in reversed(matrices):
        result = result*value+matrix
    return result


def derivative(matrices):
    return [matrix*k for k, matrix in enumerate(matrices) if k] or \
           [zero(matrices[0].nrows(), matrices[0].ncols())]


def interpolate_weights(points, prime=PRIME):
    count = len(points)
    assert count == len(set(points)) and all(0 <= point < prime for point in points)
    answer = [[0]*count for _ in range(count)]
    for i, point in enumerate(points):
        coeff, denominator = [1], 1
        for j, other in enumerate(points):
            if j == i:
                continue
            new = [0]*(len(coeff)+1)
            for k, value in enumerate(coeff):
                new[k] = (new[k]-other*value) % prime
                new[k+1] = (new[k+1]+value) % prime
            coeff, denominator = new, denominator*(point-other) % prime
        inverse = pow(denominator, -1, prime)
        for k, value in enumerate(coeff):
            answer[k][i] = value*inverse % prime
    return answer


def s3_position(index):
    if index < 4:
        return 0, index
    if index < 436:
        return 1+(index-4)//3, (index-4) % 3
    return 145+(index-436)//2, (index-436) % 2


class BudgetStop(RuntimeError):
    pass


class UnitFailure(RuntimeError):
    pass


class Source:
    def __init__(self, root, label, item):
        self.root, self.label, self.item = Path(root)/label, label, item
        path = self.root/"full-outputs-manifest.json"
        assert sha(path) == item["manifest_sha256"]
        manifest = read(path)
        assert manifest["result"] == item["result"]
        self.files = {entry["file"]: entry for entry in manifest["files"]}
        assert len(self.files) == len(manifest["files"])
        self.checked = set()
        run, receipt, initial = [self.raw(name) for name in
                                ("run-receipt.json", "core-receipt.json", "public-actions-input.json")]
        assert run["result"] == receipt["result"] == initial["result"] == item["result"]
        assert str(run["workflow_run_id"]) == str(item["run_id"])
        assert run["source_commit"] == initial["source_commit"] == item["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == item["core_sha256"]
        assert receipt["source_sha256"] == item["core_sha256"]
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        self.initial, self.run = initial, run
        name = item.get("certificate_name")
        if name is None:
            assert label in ("R787", "R809") and item["expected_conclusion"] == "failure"
            assert run["complete"] is False and receipt["complete"] is False
            permitted = item.get("accepted_checkpoint_exit_codes", [124])
            assert run["process_exit_code"] in permitted and 0 not in permitted
            anchor = OLD_PREFIX+"chart.json.gz" if label == "R787" else "R809-S5-basis-index.json.gz"
            data = self.raw(anchor)
            assert data["complete"] is True
            self.certificate, self.tag = None, data["configuration"]
        else:
            assert run["complete"] is True and run["process_exit_code"] == 0
            assert receipt["complete"] is True
            assert receipt["certificate_sha256"] == item["files"][name] == self.files[name]["sha256"]
            self.certificate = self.raw(name)
            assert self.certificate["complete"] is True and self.certificate["result"] == item["result"]
            self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == item["core_sha256"] and self.tag["python_flint"] == "0.9.0"
        self.stable_identity = {key: item[key] for key in BASE_KEYS}
        if name is not None:
            self.stable_identity["certificate"] = plain(self.files[name])

    def raw(self, name, expected=None):
        assert Path(name).name == name
        record = self.files[name]
        if expected is not None:
            assert plain(record) == plain(expected)
        if name in self.item.get("files", {}):
            assert record["sha256"] == self.item["files"][name]
        path = self.root/name
        if name not in self.checked:
            assert path.stat().st_size == record["bytes"] and sha(path) == record["sha256"]
            self.checked.add(name)
        return read(path)

    def stage(self, entry):
        if isinstance(entry, str):
            entry = self.files[entry]
        data = self.raw(entry["file"], entry)
        assert data["complete"] is True and data["configuration"] == self.tag
        return data

    def source(self, entry):
        if isinstance(entry, str):
            entry = self.files[entry]
        assert plain(self.files[entry["file"]]) == plain(entry)
        return dict(plain(entry), producer=self.label)


class Job:
    def __init__(self, args):
        guard()
        assert flint.__version__ == "0.9.0"
        self.args, self.out, self.started = args, Path(args.output), time.monotonic()
        self.item = read(args.config)
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert self.item["producer_inputs_pending"] is False
        assert self.item["core_sha256"] == sha(__file__)
        assert sha(args.proof) == self.item["R827_proof_sha256"] == PROOF_SHA
        assert sha(args.method) == self.item["R827_method_sha256"]
        assert sha(modules.__file__) == self.item["finite_helper_sha256"]
        assert sha(modules.generic.__file__) == self.item["poly_framework_sha256"] == modules.GENERIC_SHA
        assert self.item["auxiliary_prime"] == PRIME
        assert self.item["original_branch"] == 0
        assert self.item["canonical_free_column"] == 1186
        assert self.item["matrix_row_block_size"] == 16 and self.item["hermite_tile_size"] == FREE
        assert self.item["certification_mode"] == MODE
        for entry in self.item.get("reusable_stage_sources", []):
            assert entry["role"] in {"Krylov_point", "operator_point", "operator_modular_image"}
            assert entry["prime"] == PRIME
            if entry["role"] != "Krylov_point":
                assert entry["target"] in ("g", "Gamma")
        self.q = self.item["requested_derivative_order"]
        assert isinstance(self.q, int) and 0 <= self.q <= 1206
        assert set(self.item["retained_sources"]) == LABELS
        self.sources = {label: Source(args.retained, label, item)
                        for label, item in self.item["retained_sources"].items()}
        self.r806, self.r813, self.r820, self.r824, self.r809, self.r787 = \
            [self.sources[key] for key in ("R806", "R813", "R820", "R824", "R809", "R787")]
        for name, digest in OLD_PINNED.items():
            assert self.r787.files[name]["sha256"] == digest
        assert self.r787.tag["source_sha256"] == \
            "93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04"
        assert self.r787.tag["original_map_index"] == 4 and self.r787.tag["original_map_degree"] == "1206"
        assert self.r787.tag["ordinary_power"] == 5 and self.r787.tag["basis_dimension"] == S5
        same_identity(self.r824.tag["source_identities"]["R787"], self.r787.item)
        same_identity(self.r813.tag["producer_identities"]["R806"], self.r806.item)
        same_identity(self.r820.tag["producer_identities"]["R806"], self.r806.item)
        same_identity(self.r809.tag["basis_producers"]["R786"], self.r787.tag["retained_artifacts"]["R786"])
        same_identity(self.r809.tag["basis_producers"]["R805"], self.r806.tag["retained_artifacts"]["R805"])
        assert self.r824.tag["R824_proof_sha256"] == \
            "3a32e69f5ff3fb74ad7b262357e6b9d00da5e1f4348f65b1cdc0705d6fef7be1"
        self.field = self.r824.tag["field"]
        self.w_spec = self.r806.certificate["polynomial_multiplier"]
        self.w_index = self.r806.stage(self.w_spec)
        self.witness_spec = self.w_index["actual_cyclic_witness"]
        self.witness = self.r806.stage(self.witness_spec)
        assert self.w_index["normal_affine_basis_rank"] == FREE
        assert self.w_index["normal_affine_basis_degrees"] == EPS
        assert self.w_index["coefficient_field"] == "Q, certified by exact original rational coordinate equations"
        assert self.w_index["original_function_field_primitive_generator_certified"] is True
        assert [int(x) for x in self.r806.certificate["actual_w0_original_M2_integer_coordinates"]] == \
            [int(i == 2) for i in range(146)]
        assert self.w_index["all272_columns_verified_in_all820_original_rows"] is True
        self.free_spec = self.w_index["original_R805_free_basis"]
        assert self.free_spec == self.r813.tag["original_graded_free_basis"]
        assert self.free_spec == self.r820.tag["original_R805_free_basis"]
        assert self.free_spec == self.r809.tag["original_graded_free_basis"]
        assert self.r809.tag["actual_sigma_integer_n"] == self.r806.tag["actual_sigma_integer_n"] == 1
        assert self.r820.tag["actual_pencil_n"] == 1
        self.gh_spec = self.r813.certificate["exact_coordinate_stage"]
        self.gh = self.r813.stage(self.gh_spec)
        self.normal_spec = self.r813.certificate["normal_vector_interface"]
        self.normal = self.r813.stage(self.normal_spec)
        assert self.normal["actual_R806_polynomial_multiplier_index"] == self.w_spec
        assert self.normal["original_R805_graded_free_basis"] == self.free_spec
        assert self.gh["target_names"] == ["g", "h"] and self.gh["column_indices"] == [0, 1]
        assert self.gh["all820_original_coordinates_verified"] is True
        assert self.gh["original_D0_qY_multiplier"] == ["1", "82"]
        assert self.gh["original_S3_integer_scale"] == str(82**6)
        assert self.normal["normal_basis_degrees"] == EPS
        self.s5_index_spec = self.r809.source("R809-S5-basis-index.json.gz")
        self.s5_index = self.r809.stage(self.s5_index_spec)
        assert self.s5_index["dimension"] == S5 and self.s5_index["qY_count"] == 69
        assert self.s5_index["full_coordinate_rows"] == ROWS
        assert self.s5_index["integer_scale"] == str(82**10)
        assert self.s5_index["normal_basis_degrees"] == EPS
        assert self.s5_index["original_graded_free_basis"] == self.free_spec
        assert len(self.s5_index["basis_rows"]) == S5
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "R827_proof_sha256": PROOF_SHA, "R827_method_sha256": sha(args.method),
            "finite_helper_sha256": sha(modules.__file__),
            "poly_framework_sha256": modules.GENERIC_SHA,
            "p": 41, "auxiliary_prime": PRIME, "original_branch": 0, "canonical_free_column": 1186,
            "normal_basis_rank": FREE, "normal_basis_degrees": EPS, "S5_dimension": S5,
            "qY_count": 69, "full_coordinate_rows": ROWS,
            "matrix_row_block_size": 16, "hermite_tile_size": FREE,
            "source_identities": {key: self.sources[key].stable_identity for key in sorted(LABELS)},
            "original_field_coordinates": "B=lambda*b, s=1+2*zeta; exact original branch",
            "certification_mode": MODE,
            "requested_order_and_budget_excluded_from_mathematical_identity": True,
        }
        self.out.mkdir(parents=True, exist_ok=True)
        self.S = modules.Store(self.out, self.tag, self.budget)
        self.A = modules.Algebra(PRIME, self.budget)
        self.blocks = [(first, min(first+16, FREE)) for first in range(0, FREE, 16)]
        self.operator_arrays, self.layer_arrays = {}, {}
        self.shared_identity = {
            "R806_producer": {key: self.r806.item[key] for key in BASE_KEYS},
            "R806_polynomial_multiplier": self.w_spec, "R806_cyclic_witness": self.witness_spec,
            "original_R805_free_basis": self.free_spec,
            "original_R805_S_basis_index": self.w_index["original_R805_S_basis_index"],
            "normal_affine_basis_rank": FREE, "normal_basis_degrees": EPS,
            "coordinate_convention": "column input, row output; e0 is original unit", "coefficient_field": "Q",
        }

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes-60:
            raise BudgetStop("Only completed original-field stages and atomic polynomial checkpoints retained.")

    def path(self, name):
        assert Path(name).name == name and name.startswith("R827-")
        return self.S.path(name)

    def cache(self, name):
        return self.S.load(name) if self.S.exists(name) else None

    def put(self, name, data):
        return self.S.put(name, data)

    def inv(self, value, context):
        value = int(value)
        if value % PRIME == 0:
            raise UnitFailure("Nonunit original coefficient: "+context)
        return pow(value % PRIME, -1, PRIME)

    def rational(self, pair, context):
        assert len(pair) == 2
        return int(pair[0]) % PRIME*self.inv(pair[1], context) % PRIME

    def source_audit(self):
        name = "R827-original-place-and-unit-source-audit"
        old = self.cache(name)
        if old is not None:
            self.B_source = old["canonical_B_expansion"]
            return self.S.spec(name)
        assert bool(fmpz(PRIME).is_prime())
        selection = self.r787.stage(OLD_PREFIX+"selection.json.gz")
        for key in ("prime_proved", "all_14_L_branches_distinct",
                    "all_rational_denominators_units", "all_kappa_reductions_invertible"):
            assert selection[key] is True
        assert selection["prime"] == PRIME
        B_root, s_root = [int(x) for x in selection["roots_B_s"][0]]
        assert [B_root, s_root] == [3197390, 99932770]
        lam = int(self.field["lambda"])
        b_root = B_root*self.inv(lam, "original lambda") % PRIME
        zeta_root = (s_root-1)*self.inv(2, "original zeta adapter") % PRIME
        fB = nmod_poly([int(x) % PRIME for x in self.field["integral_B_minimal_polynomial"]], PRIME)
        original = self.field["original_b_minimal_polynomial"]
        invden = self.inv(original["denominator"], "original b minimal polynomial")
        fb = nmod_poly([int(x)*invden % PRIME for x in original["numerator"]], PRIME)
        assert int(fB(B_root)) == int(fb(b_root)) == 0
        assert fB.derivative()(B_root) and fb.derivative()(b_root)
        assert (s_root*s_root+3) % PRIME == 0 and (zeta_root*zeta_root+zeta_root+1) % PRIME == 0
        assert (2*s_root) % PRIME
        chart = self.r787.stage(OLD_PREFIX+"chart.json.gz")
        rational = self.r787.stage(OLD_PREFIX+"rational-blocks.json.gz")
        original_branch = self.r787.stage(OLD_PREFIX+"branch-00.json.gz")
        assert chart["actual_modular_rank"] == 1186 and chart["chosen_free_column"] == 1186
        assert len(chart["pivot_rows"]) == len(chart["pivot_columns"]) == 1186
        assert rational["A_minor_det_mod_prime"] == 336446771
        assert rational["B_constant_minor_det_mod_prime"] == 322380492
        assert rational["exact_E0_Z_zero_verified"] is True
        assert original_branch["actual_Schur_rank"] == 1186
        assert original_branch["selected_minor_det_mod_prime"] == 296007862
        assert original_branch["roots_B_s"] == [B_root, s_root]
        assert original_branch["chart_sha256"] == OLD_PINNED[OLD_PREFIX+"chart.json.gz"]
        assert "modular_generator_profile" in self.r824.certificate["completed_requested_scopes"]
        branch_name = "R824-power5-prime-1000000753-branch-00.json.gz"
        branch = self.r824.stage(branch_name)
        assert branch["prime"] == PRIME and branch["ordinary_power"] == 5 and branch["branch"] == 0
        assert branch["roots_B_s"] == [B_root, s_root] and branch["actual_Schur_rank"] == 1186
        assert branch["selected_minor_det_mod_prime"] == 296007862
        assert branch["original_reserved_column_retained_without_new_lift"] is True
        assert plain(branch["original_branch_inverse_reused_from"]) == plain(self.r787.files[OLD_PREFIX+"branch-00.json.gz"])
        assert plain(branch["rational_block"]) == plain(self.r787.files[OLD_PREFIX+"rational-blocks.json.gz"])
        local_chart = self.r824.stage(branch["chart"])
        assert local_chart["pivot_rows"] == chart["pivot_rows"]
        assert local_chart["pivot_columns"] == chart["pivot_columns"]
        free = branch["kernel_free_columns"]
        assert len(free) == 28 and free == [i for i in range(1214) if i not in set(chart["pivot_columns"])]
        position = free.index(1186)
        C = [int(row[position]) % PRIME for row in branch["kernel_C_mod_prime"]]
        A = [int(row[position]) % PRIME for row in branch["kernel_A_mod_prime"]]
        assert len(C) == 1214 and len(A) == S5
        assert [C[i] for i in free] == [int(i == position) for i in range(28)]
        assert C == [int(x) % PRIME for x in original_branch["initial_C"]]
        assert A == [int(x) % PRIME for x in original_branch["initial_A"]]
        P, Q = rational["B_constant_pivot_columns"], rational["B_constant_free_columns"]
        Zd = int(rational["Z_free_diagonal"])
        self.inv(Zd, "original constant-kernel diagonal")
        assert len(P) == 20 and len(Q) == 1214 and sorted(P+Q) == list(range(S5))
        Z = nmod_mat([[int(x) % PRIME for x in row] for row in rational["Z_pivot_integer_rows"]], PRIME)
        Cp = nmod_mat([[x] for x in C], PRIME)
        pivot_values = Z*Cp
        B = [0]*S5
        for j, index in enumerate(P):
            B[index] = int(pivot_values[j, 0])
        for j, index in enumerate(Q):
            B[index] = Zd*C[j] % PRIME
        assert any(B)
        self.B_source = self.put("R827-canonical-B-original-V5-expansion", {
            "prime": PRIME, "original_branch": 0, "canonical_free_column": 1186,
            "source_R824_branch": self.r824.source(branch_name),
            "source_R787_branch": self.r787.source(OLD_PREFIX+"branch-00.json.gz"),
            "source_original_rational_blocks": self.r787.source(OLD_PREFIX+"rational-blocks.json.gz"),
            "source_original_chart": self.r787.source(OLD_PREFIX+"chart.json.gz"),
            "original_B_lambda_b_root": B_root, "original_b_root": b_root,
            "original_s_root": s_root, "original_zeta_root": zeta_root, "lambda": str(lam),
            "B_coefficients_mod_prime_in_original_V5_basis": B,
            "A_coefficients_mod_prime_in_original_V5_basis": A,
            "canonical_C_coefficients_mod_prime": C,
            "original_V5_integer_scale": str(82**10),
            "same_original_reserved_normalization_verified": True,
            "characteristic_zero_coefficients_reconstructed": False,
            "abstract_original_p_integral_lift_certified_by_unit_minor_and_rank_bound": True,
        })
        return self.put(name, {
            "prime": PRIME, "original_branch": 0, "canonical_free_column": 1186,
            "original_field": self.field,
            "original_integral_B_root": B_root, "original_b_root": b_root,
            "original_s_root": s_root, "original_zeta_root": zeta_root,
            "original_lambda_is_a_unit": True,
            "original_minimal_polynomials_and_simple_residue_roots_verified": True,
            "original_selection": self.r787.source(OLD_PREFIX+"selection.json.gz"),
            "original_A_constant_and_Schur_unit_minor_sources": [
                self.r787.source(OLD_PREFIX+"rational-blocks.json.gz"),
                self.r787.source(OLD_PREFIX+"branch-00.json.gz")],
            "canonical_B_expansion": self.B_source,
            "genuine_DVR_lift_source_not_an_arbitrary_modular_kernel_candidate": True,
        })

    def ordinary_inputs(self):
        name = "R827-original-W-g-h-reductions"
        old = self.cache(name)
        if old is None:
            W = [[[0]*FREE for _ in range(FREE)] for _ in range(4)]
            columns, records = [], []
            assert len(self.w_index["S_row_to_polynomial_coefficient"]) == 690
            for i, entry in enumerate(self.w_index["S_row_to_polynomial_coefficient"]):
                assert entry == {"S_row": i, "normal_basis_row": s3_position(i)[0],
                                 "power_of_z": s3_position(i)[1]}
            for entry in self.w_index["coordinate_groups"]:
                self.budget()
                group = self.r806.stage(entry)
                assert group["all820_original_coordinates_verified"] is True
                assert group["weighted_polynomial_support_verified"] is True
                assert group["reduction_equals_successful_modular_multiplier"] is True
                assert group["integer_scale"] == str(82**6)
                indices = group["column_indices"]
                columns.extend(indices)
                assert len(group["coordinate_numerators"]) == 690
                for local, column in enumerate(indices):
                    invden = self.inv(group["column_denominators"][local], "original W column "+str(column))
                    for i, row in enumerate(group["coordinate_numerators"]):
                        output, power = s3_position(i)
                        numerator = int(row[local])
                        if column == 0:
                            expected = int(group["column_denominators"][local]) if output == 1 and power == 0 else 0
                            assert numerator == expected
                        if power > 1+EPS[column]-EPS[output]:
                            assert numerator == 0
                        W[power][output][column] = numerator*invden % PRIME
                records.append(self.r806.source(entry))
            assert columns == list(range(FREE))
            for k in range(4):
                assert all(W[k][i][0] == int(k == 0 and i == 1) for i in range(FREE))
            gh = {}
            for column, target in enumerate(("g", "h")):
                scale = [int(x) for x in self.gh["original_target_rational_scales"][column]]
                assert scale == [6724, 1]
                inverse = self.inv(self.gh["column_denominators"][column], target+" coordinate denominator")
                inverse = inverse*self.inv(scale[1], target+" original rational scale") % PRIME
                values = [[0]*FREE for _ in range(4)]
                for i, row in enumerate(self.gh["coordinate_numerators"]):
                    output, power = s3_position(i)
                    assert power <= 3-EPS[output]
                    values[power][output] = int(row[column])*scale[0]*inverse % PRIME
                gh[target] = values
            self.put(name, {
                "prime": PRIME, "source_R806_multiplier": self.r806.source(self.w_spec),
                "source_R806_coordinate_groups": records,
                "source_R813_coordinates": self.r813.source(self.gh_spec),
                "source_R813_normal_interface": self.r813.source(self.normal_spec),
                "W_coefficients_mod_prime": W, "g_vector_coefficients_mod_prime": gh["g"],
                "h_vector_coefficients_mod_prime": gh["h"],
                "original_rational_denominators_all_units": True,
                "original_R813_target_scales_applied_once": [[6724, 1], [6724, 1]],
                "original_W_e0_equals_e1_verified": True,
                "original_primitive_coordinate_solutions_not_recomputed": True,
            })
            old = self.cache(name)
        assert old["prime"] == PRIME
        self.W = [nmod_mat(matrix, PRIME) for matrix in old["W_coefficients_mod_prime"]]
        self.Wprime = derivative(self.W)
        self.gh_mod = {target: [nmod_mat([[int(x)] for x in row], PRIME)
                               for row in old[target+"_vector_coefficients_mod_prime"]]
                       for target in ("g", "h")}
        self.W_source = self.S.spec(name)
        return self.W_source

    def cusp_inputs(self):
        name = "R827-original-two-chart-C-reduction"
        old = self.cache(name)
        if old is None:
            assert self.r820.certificate["original_two_chart_cusp_ideals_computed"] is True
            assert self.r820.certificate["complete_polynomial_kernels_certified"] is True
            assert self.r820.certificate["same_original_cusp_field_and_two_chart_transitions_verified"] is True
            charts, source_indexes = {}, {}
            for chart, entry in self.r820.certificate["two_chart_cusp_ideal_indexes"].items():
                assert chart in ("tau", "sigma")
                index = self.r820.stage(entry)
                columns = index["Hermite_columns_in_original_basis_order"]
                assert len(columns) == FREE
                q, P, sources = [], None, []
                for j, column_spec in enumerate(columns):
                    data = self.r820.stage(column_spec)
                    assert data["kind"] == "first_dependence"
                    assert data["exact_original_normal_basis_column"] == j
                    assert data["complete_relation_evaluation_zero_in_all_20_original_coordinates"] is True
                    assert data["monic_diagonal_degree"] == (20 if j == 271 else 0)
                    values = {}
                    for term in data["column_terms"]:
                        row, power = term["normal_basis_row"], term["power"]
                        key = row, power
                        assert key not in values
                        values[key] = self.rational(term["coefficient"], chart+" C column "+str(j))
                    if j < 271:
                        assert values.pop((j, 0)) == 1
                        assert all(row == 271 and 0 <= k < 20 for row, k in values)
                        polynomial = [0]*20
                        for (_, k), value in values.items():
                            polynomial[k] = -value % PRIME
                        while polynomial and not polynomial[-1]:
                            polynomial.pop()
                        q.append(polynomial)
                    else:
                        assert all(row == 271 and 0 <= k <= 20 for row, k in values)
                        P = [values.get((271, k), 0) for k in range(21)]
                        assert P[20] == 1
                    sources.append(self.r820.source(column_spec))
                assert P is not None and len(q) == 271
                if not P[0]:
                    raise UnitFailure("Original "+chart+" cusp polynomial has nonunit constant.")
                charts[chart] = {"q_polynomials": q, "P_polynomial": P,
                                 "original_column_sources": sources}
                source_indexes[chart] = self.r820.source(entry)
            assert set(charts) == {"tau", "sigma"}
            a, b = charts["tau"]["P_polynomial"], charts["sigma"]["P_polynomial"]
            assert list(reversed(a)) == [a[0]*x % PRIME for x in b]
            self.put(name, {
                "prime": PRIME, "source_R820_indexes": source_indexes, "charts": charts,
                "all_original_rational_coefficients_p_integral": True,
                "both_P_constant_terms_units": True,
                "actual_degree_twenty_monic_polynomials_preserved": True,
                "original_reciprocal_relation_verified_mod_prime": True,
                "original_exact_two_chart_transition_certificate_preserved": True,
                "complete_flat_target_not_squarefree_replacement": True,
            })
            old = self.cache(name)
        self.C_data = old["charts"]
        self.C_source = self.S.spec(name)
        return self.C_source

    def normal_B(self):
        name = "R827-canonical-B-normal-vector"
        old = self.cache(name)
        if old is not None:
            self.vB = [nmod_mat([[x] for x in row], PRIME)
                       for row in old["vector_coefficients_mod_prime"]]
            self.vB_source = self.S.spec(name)
            return self.vB_source
        Bdata = self.S.load(self.B_source)
        B = Bdata["B_coefficients_mod_prime_in_original_V5_basis"]
        matrix_columns, source_rows, mapping = [], [], []
        for i, entry in enumerate(self.s5_index["basis_rows"]):
            self.budget()
            assert entry["index"] == i
            row = self.r809.stage(entry["source"])
            assert row["index"] == i and row["integer_scale"] == str(82**10)
            assert row["qY_count"] == 69 and row["real_coordinate_count"] == 20
            assert row["all_original_term_phases_and_scales_verified"] is True
            assert row["original_R805_free_generator_unchanged"] is True
            a, power = row["normal_basis_index"], row["z_degree"]
            assert entry["normal_basis_index"] == a and entry["z_degree"] == power
            assert row["normal_basis_degree"] == EPS[a]
            assert 0 <= power <= 5-EPS[a]
            mapping.append((a, power))
            values = [int(x) % PRIME for vector in row["integer_v_t_coefficients"] for x in vector]
            assert len(values) == ROWS
            matrix_columns.append(values)
            source_rows.append(self.r809.source(entry["source"]))
        assert mapping == [(a, j) for a in range(FREE) for j in range(6-EPS[a])]
        matrix = nmod_mat(matrix_columns, PRIME).transpose()
        del matrix_columns
        target = [0]*ROWS
        original_sources = []
        for i in range(S5):
            self.budget()
            old_name = "R787-real-power5-row-"+str(i).zfill(4)+".json.gz"
            row = self.r787.stage(old_name)
            assert row["index"] == i and row["all_original_phase_involutions_verified"] is True
            values = row["integer_t_coefficients"]
            assert len(values) == 129 and all(len(v) == 20 for v in values)
            if B[i]:
                for n, vector in enumerate(values[:69]):
                    for r, value in enumerate(vector):
                        target[20*n+r] = (target[20*n+r]+B[i]*int(value)) % PRIME
            original_sources.append(self.r787.source(old_name))
        assert not any(target[:20]) and any(target)
        rhs = nmod_mat([[x] for x in target], PRIME)
        minor_name = "R827-prime-1000000753-S5-fixed-minor-inverse"
        minor = self.cache(minor_name)
        if minor is None:
            source_minor = self.r809.stage("R809-accepted-S5-short-minor.json.gz")
            assert source_minor["actual_rank"] == S5 and source_minor["full_coordinate_rows"] == ROWS
            assert plain(source_minor["S5_basis_index"]) == plain(self.s5_index_spec)
            I = list(source_minor["row_indices"])
            assert len(I) == S5 and len(set(I)) == S5
            square = nmod_mat([[int(matrix[i, j]) for j in range(S5)] for i in I], PRIME)
            det = int(square.det())
            selected_again = False
            if not det:
                rref, rank = matrix.transpose().rref()
                if rank != S5:
                    raise UnitFailure("Actual S5 matrix has deficient rank at the original prime753.")
                I = [next(j for j in range(ROWS) if rref[i, j]) for i in range(S5)]
                square = nmod_mat([[int(matrix[i, j]) for j in range(S5)] for i in I], PRIME)
                det = int(square.det())
                assert det
                selected_again = True
                del rref
            old_inverse = None
            old_inverse_name = "R809-S5-fixed-modular-inverse.json.gz"
            if old_inverse_name in self.r809.files and (self.r809.root/old_inverse_name).exists():
                candidate = self.r809.stage(old_inverse_name)
                if candidate["prime"] == PRIME:
                    assert source_minor["prime"] == PRIME and not selected_again
                    assert plain(candidate["minor_stage"]) == plain(self.r809.files["R809-accepted-S5-short-minor.json.gz"])
                    assert plain(candidate["S5_basis_index"]) == plain(self.s5_index_spec)
                    assert candidate["inverse_product_exactly_verified_mod_prime"] is True
                    old_inverse = candidate
            inverse = nmod_mat(old_inverse["inverse_mod_prime"], PRIME) if old_inverse is not None else square.inv()
            assert square*inverse == identity(S5) and inverse*square == identity(S5)
            self.put(minor_name, {
                "prime": PRIME, "S5_basis_index": self.s5_index_spec,
                "row_indices": I, "column_indices": list(range(S5)),
                "actual_determinant_mod_prime": det, "inverse_mod_prime": matrix_rows(inverse),
                "both_inverse_products_verified": True,
                "old_row_selection_replaced_only_after_actual_zero_at_new_prime": selected_again,
                "old_same_prime_inverse_reused": (
                    self.r809.source(old_inverse_name) if old_inverse is not None else None),
                "original_Q_matrix_and_69_term_rows_recomputed": False,
            })
            minor = self.cache(minor_name)
        I = minor["row_indices"]
        inverse = nmod_mat(minor["inverse_mod_prime"], PRIME)
        selected = nmod_mat([[target[i]] for i in I], PRIME)
        solution = inverse*selected
        assert matrix*solution == rhs
        values = [[0]*FREE for _ in range(6)]
        for i, (a, power) in enumerate(mapping):
            values[power][a] = int(solution[i, 0])
        assert any(value for row in values for value in row)
        self.vB_source = self.put(name, {
            "prime": PRIME, "canonical_free_column": 1186, "original_branch": 0,
            "source_original_B_expansion": self.B_source,
            "source_S5_index": self.s5_index_spec, "source_S5_rows": source_rows,
            "source_original_V5_rows": original_sources,
            "source_actual_unit_minor": self.S.spec(minor_name),
            "vector_coefficients_mod_prime": values, "regular_degree_bound": 5,
            "normal_basis_rank": FREE, "normal_basis_degrees": EPS,
            "all1380_original_short_coordinates_verified": True,
            "same_original_82power10_scales_preserved": True,
            "original_Q_prefix_and_large_characteristic_zero_solve_recomputed": False,
            "abstract_p_integral_original_normal_lift_certified": True,
            "characteristic_zero_coordinates_reconstructed": False,
        })
        self.vB = [nmod_mat([[x] for x in row], PRIME) for row in values]
        del matrix, inverse, solution, rhs
        gc.collect()
        return self.vB_source

    def external(self, role, point=None, target=None):
        """Read explicitly supplied original cache bytes; never rewrite their tag."""
        matches = []
        for entry in self.item.get("reusable_stage_sources", []):
            if entry["role"] != role or entry.get("prime") != PRIME:
                continue
            if point is not None and entry.get("z0") != point:
                continue
            if target is not None and entry.get("target") != target:
                continue
            matches.append(entry)
        assert len(matches) <= 1
        if not matches:
            return None, None
        entry = matches[0]
        relative = Path(entry["relative_path"])
        assert not relative.is_absolute() and ".." not in relative.parts
        path = Path(self.args.retained)/relative
        assert spec(path) == plain(entry["stage"])
        data = read(path)
        assert data["complete"] is True and data["prime"] == PRIME
        tag = data["configuration"]
        assert tag["source_sha256"] == entry["source_identity"]["core_sha256"]
        assert tag["result"] == entry["source_identity"]["result"] and tag["python_flint"] == "0.9.0"
        same_identity(tag["R806_producer"], self.r806.item)
        assert tag["R806_polynomial_multiplier"] == self.w_spec
        assert tag["R806_cyclic_witness"] == self.witness_spec
        assert tag["original_R805_free_basis"] == self.free_spec
        assert tag["normal_basis_degrees"] == EPS
        if role == "Krylov_point":
            original = data["shared_point_mathematical_identity"]
            same_identity(original["R806_producer"], self.r806.item)
            assert original["R806_polynomial_multiplier"] == self.w_spec
            assert original["R806_cyclic_witness"] == self.witness_spec
            assert original["original_R805_free_basis"] == self.free_spec
            assert original["normal_basis_degrees"] == EPS
            assert data["source_bound_external_cache_consumption_allowed"] is True
        else:
            target_tag = data["target_configuration"]
            same_identity(target_tag["R813_producer"], self.r813.item)
            assert target_tag["source_R813_exact_coordinates"] == self.gh_spec
            assert target_tag["source_R813_normal_interface"] == self.normal_spec
            assert data["target"] == target and data["field_component"] == 0
        return data, entry

    def external_support(self, entry, specification, parent):
        relative = Path(entry["relative_path"])
        assert Path(specification["file"]).name == specification["file"]
        path = Path(self.args.retained)/relative.parent/specification["file"]
        assert spec(path) == plain(specification)
        data = read(path)
        assert data["complete"] is True and data["configuration"] == parent["configuration"]
        if "target_configuration" in data:
            assert data["target_configuration"] == parent["target_configuration"]
        return data

    def point(self, z0):
        name = "R827-prime-1000000753-z-"+str(z0)+"-Krylov"
        data = self.cache(name)
        if data is not None:
            return data, self.S.spec(name)
        self.budget()
        W = evaluate(self.W, z0)
        imported, import_spec = self.external("Krylov_point", z0)
        if imported is not None:
            assert imported["z0"] == z0
            assert imported["usable"] is bool(imported["actual_determinant_mod_prime"])
            det = int(imported["actual_determinant_mod_prime"]) % PRIME
            payload = {
                "prime": PRIME, "z0": z0, "usable": bool(det), "actual_determinant_mod_prime": det,
                "source_original_W": self.W_source, "source_original_cyclic_witness": self.r806.source(self.witness_spec),
                "source_bound_external_stage": import_spec,
                "old_same_prime_Krylov_inverse_reused": True,
                "new_same_prime_Krylov_inverse_computed": False,
            }
            if det:
                assert imported["actual_cyclic_rank"] == FREE
                assert imported["both_inverse_products_verified"] is True
                assert matrix_rows(W) == imported["W_evaluated_mod_prime"]
                payload.update({
                    "W_evaluated_mod_prime": imported["W_evaluated_mod_prime"],
                    "inverse_Krylov_matrix_mod_prime": imported["inverse_Krylov_matrix_mod_prime"],
                    "Krylov_matrix_sha256": imported["Krylov_matrix_sha256"],
                    "actual_cyclic_rank": FREE, "both_inverse_products_verified": True,
                    "Krylov_matrix_mod_prime": imported.get("Krylov_matrix_mod_prime"),
                })
            self.put(name, payload)
            return self.cache(name), self.S.spec(name)
        vector = nmod_mat([[int(i == 0)] for i in range(FREE)], PRIME)
        columns = []
        for k in range(FREE):
            self.budget()
            columns.append([int(vector[i, 0]) for i in range(FREE)])
            if k+1 < FREE:
                vector = W*vector
        K = nmod_mat(columns, PRIME).transpose()
        det = int(K.det())
        payload = {
            "prime": PRIME, "z0": z0, "usable": bool(det), "actual_determinant_mod_prime": det,
            "source_original_W": self.W_source, "source_original_cyclic_witness": self.r806.source(self.witness_spec),
            "source_bound_external_stage": None,
            "old_same_prime_Krylov_inverse_reused": False,
            "new_same_prime_Krylov_inverse_computed": bool(det),
            "failure_is_only_this_original_residue_specialization": not bool(det),
        }
        if det:
            inverse = K.inv()
            assert K*inverse == identity() and inverse*K == identity()
            raw = matrix_rows(K)
            payload.update({
                "W_evaluated_mod_prime": matrix_rows(W),
                "Krylov_matrix_mod_prime": raw, "Krylov_matrix_sha256": fingerprint(raw),
                "inverse_Krylov_matrix_mod_prime": matrix_rows(inverse),
                "actual_cyclic_rank": FREE, "both_inverse_products_verified": True,
            })
        self.put(name, payload)
        return self.cache(name), self.S.spec(name)

    def grid(self):
        name = "R827-eight-original-unit-cyclic-nodes"
        old = self.cache(name)
        if old is not None:
            assert len(old["points"]) == 8 and len(set(old["points"])) == 8
            self.grid_data, self.grid_source = old, self.S.spec(name)
            return self.grid_source
        points, stages = [], []
        for z0 in range(36458+8):
            self.budget()
            data, entry = self.point(z0)
            if data["usable"]:
                points.append(z0)
                stages.append(entry)
                if len(points) == 8:
                    break
        if len(points) != 8:
            raise UnitFailure("The chosen original residue place did not supply eight unit cyclic nodes.")
        self.grid_source = self.put(name, {
            "prime": PRIME, "points": points, "Krylov_point_stages": stages,
            "original_Krylov_determinant_degree_bound": 36458,
            "all_eight_actual_determinants_nonzero": True,
            "distinct_residue_values_and_unit_Vandermonde_certified": True,
            "targets_and_node_counts": {"B": 8, "g": 6, "Gamma": 5},
            "characteristic_zero_Krylov_matrix_or_inverse_computed": False,
        })
        self.grid_data = self.cache(name)
        return self.grid_source

    def point_target(self, target, z0):
        assert target in ("B", "g", "Gamma")
        name = "R827-target-"+target+"-prime-1000000753-z-"+str(z0)
        old = self.cache(name)
        if old is not None:
            return old, self.S.spec(name)
        point, point_spec = self.point(z0)
        assert point["usable"]
        W = nmod_mat(point["W_evaluated_mod_prime"], PRIME)
        inverse = nmod_mat(point["inverse_Krylov_matrix_mod_prime"], PRIME)
        imported, import_spec = self.external("operator_point", z0, target) if target != "B" else (None, None)
        if imported is not None:
            assert imported["z0"] == z0 and imported["target"] == target
            answer = nmod_mat(imported["matrix_mod_prime"], PRIME)
            source = import_spec
        elif target in ("B", "g"):
            vector = evaluate(self.vB if target == "B" else self.gh_mod["g"], z0)
            v0 = vector
            columns = []
            for k in range(FREE):
                self.budget()
                columns.append([int(vector[i, 0]) for i in range(FREE)])
                if k+1 < FREE:
                    vector = W*vector
            answer = nmod_mat(columns, PRIME).transpose()*inverse
            assert answer*W == W*answer
            assert all(int(answer[i, 0]) == int(v0[i, 0]) for i in range(FREE))
            source = None
        else:
            gname = "R827-target-g-prime-1000000753-z-"+str(z0)
            if self.cache(gname) is not None:
                gpoint = self.cache(gname)
                Mg = nmod_mat(gpoint["matrix_mod_prime"], PRIME)
                gspec = self.S.spec(gname)
            else:
                # A complete imported g-image is evaluated for this new Gamma RHS.
                Mg = evaluate(self.operator_arrays["g"], z0)
                gspec = self.S.spec("R827-target-g-tau-polynomial-index")
            Wprime = evaluate(self.Wprime, z0)
            vh = evaluate(self.gh_mod["h"], z0)
            raw_K = point.get("Krylov_matrix_mod_prime")
            recovered_columns = None
            if raw_K is None:
                # A producer may retain only K's SHA and inverse. These columns
                # are required by the new K' RHS, not a new cyclic/minor search.
                v = nmod_mat([[int(i == 0)] for i in range(FREE)], PRIME)
                recovered_columns = []
                for k in range(FREE):
                    recovered_columns.append([int(v[i, 0]) for i in range(FREE)])
                    if k+1 < FREE:
                        v = W*v
                raw_K = matrix_rows(nmod_mat(recovered_columns, PRIME).transpose())
                assert fingerprint(raw_K) == point["Krylov_matrix_sha256"]
            d = zero(FREE, 1)
            hpower, columns = vh, []
            for k in range(FREE):
                self.budget()
                value = zero(FREE, 1) if k == 0 else hpower*k-Mg*d
                columns.append([int(value[i, 0]) for i in range(FREE)])
                if k+1 < FREE:
                    Kcolumn = nmod_mat([[raw_K[i][k]] for i in range(FREE)], PRIME)
                    d = Wprime*Kcolumn+W*d
                    if k >= 1:
                        hpower = W*hpower
            answer = nmod_mat(columns, PRIME).transpose()*inverse
            assert all(not answer[i, 0] for i in range(FREE))
            H = answer*W-W*answer+Mg*Wprime
            assert all(int(H[i, 0]) == int(vh[i, 0]) for i in range(FREE))
            assert H*W == W*H
            source = None
        self.put(name, {
            "target": target, "prime": PRIME, "z0": z0,
            "source_unit_node": point_spec, "source_original_B_vector": self.vB_source,
            "source_original_g_h_and_W": self.W_source,
            "matrix_mod_prime": matrix_rows(answer),
            "matrix_convention": "output row, input column; right multiply original inverse_K",
            "source_bound_external_stage": source,
            "original_true_operator_point_value": True,
            "no_separate_Mh_or_characteristic_zero_CRT": True,
        })
        return self.cache(name), self.S.spec(name)

    def operator(self, target):
        if target in self.operator_arrays:
            return self.operator_arrays[target]
        degree = {"B": 5, "g": 3, "Gamma": 2}[target]
        count = degree+3
        name = "R827-target-"+target+"-tau-polynomial-index"
        index = self.cache(name)
        if index is None and target != "B":
            imported, import_spec = self.external("operator_modular_image", target=target)
            if imported is not None:
                assert imported["regular_degree_bound"] == degree
                assert imported["all_modular_entries_interpolated_in_original_normal_basis"] is True
                assert imported["weighted_support_and_original_first_column_verified"] is True
                assert len(imported["interpolated_blocks"]) == len(self.blocks)
                entries = []
                for old_entry, (first, stop) in zip(imported["interpolated_blocks"], self.blocks):
                    self.budget()
                    block_name = "R827-target-"+target+"-tau-rows-"+str(first).zfill(3)
                    if self.cache(block_name) is None:
                        old_block = self.external_support(import_spec, old_entry, imported)
                        assert old_block["prime"] == PRIME and old_block["target"] == target
                        assert (old_block["row_first"], old_block["row_stop"]) == (first, stop)
                        assert old_block["regular_degree_bound"] == degree
                        assert old_block["weighted_support_and_original_first_column_verified"] is True
                        coefficients = old_block["coefficients_mod_prime"]
                        raw = [[[0]*FREE for _ in range(stop-first)] for _ in range(count)]
                        position = 0
                        for r in range(first, stop):
                            for col in range(FREE):
                                for power in range(degree+EPS[col]-EPS[r]+1):
                                    value = coefficients[position]
                                    assert isinstance(value, int) and 0 <= value < PRIME
                                    raw[power][r-first][col] = value
                                    position += 1
                        assert position == len(coefficients)
                        self.put(block_name, {
                            "target": target, "chart": "tau", "prime": PRIME,
                            "row_first": first, "row_stop": stop, "regular_degree_bound": degree,
                            "coefficient_matrices_low_to_high": raw,
                            "source_unit_grid": self.grid_source, "source_point_values": [],
                            "source_bound_completed_modular_image": import_spec,
                            "source_original_modular_block": old_entry,
                            "original_weighted_support_verified": True,
                            "old_completed_modular_interpolation_recomputed": False,
                            "actual_characteristic_zero_coefficients_reconstructed": False,
                            "true_p_integral_operator_reduction_by_unit_nodes_and_original_degree_bound": True,
                        })
                    entries.append(self.S.spec(block_name))
                self.put(name, {
                    "target": target, "chart": "tau", "prime": PRIME, "regular_degree_bound": degree,
                    "normal_basis_rank": FREE, "normal_basis_degrees": EPS,
                    "row_blocks": entries, "source_unit_grid": self.grid_source,
                    "actual_interpolation_points": None, "source_point_values": [],
                    "source_bound_completed_modular_image": import_spec,
                    "construction": "unchanged original modular coefficients in an explicit new storage layout",
                    "old_completed_modular_interpolation_recomputed": False,
                    "all_weighted_support_zeros_verified": True,
                    "original_true_operator_reduction_certified": True,
                    "independent_Mh_matrix_or_char0_CRT_computed": False,
                })
                index = self.cache(name)
        if index is None:
            points = self.grid_data["points"][:count]
            values, point_specs = [], []
            for z0 in points:
                data, entry = self.point_target(target, z0)
                values.append(data["matrix_mod_prime"])
                point_specs.append(entry)
            weights = nmod_mat(interpolate_weights(points), PRIME)
            entries = []
            for first, stop in self.blocks:
                self.budget()
                block_name = "R827-target-"+target+"-tau-rows-"+str(first).zfill(3)
                block = self.cache(block_name)
                if block is None:
                    specialized = nmod_mat([
                        [values[k][r][c] for r in range(first, stop) for c in range(FREE)]
                        for k in range(count)], PRIME)
                    coefficients = weights*specialized
                    raw = [[[0]*FREE for _ in range(stop-first)] for _ in range(count)]
                    for r in range(first, stop):
                        for c in range(FREE):
                            position = (r-first)*FREE+c
                            bound = degree+EPS[c]-EPS[r]
                            for k in range(count):
                                value = int(coefficients[k, position])
                                if k > bound:
                                    assert value == 0
                                raw[k][r-first][c] = value
                    self.put(block_name, {
                        "target": target, "chart": "tau", "prime": PRIME,
                        "row_first": first, "row_stop": stop, "regular_degree_bound": degree,
                        "coefficient_matrices_low_to_high": raw,
                        "source_unit_grid": self.grid_source, "source_point_values": point_specs,
                        "original_weighted_support_verified": True,
                        "actual_characteristic_zero_coefficients_reconstructed": False,
                        "true_p_integral_operator_reduction_by_unit_nodes_and_original_degree_bound": True,
                    })
                entries.append(self.S.spec(block_name))
            self.put(name, {
                "target": target, "chart": "tau", "prime": PRIME,
                "regular_degree_bound": degree, "normal_basis_rank": FREE, "normal_basis_degrees": EPS,
                "row_blocks": entries, "source_unit_grid": self.grid_source,
                "actual_interpolation_points": points, "source_point_values": point_specs,
                "all_weighted_support_zeros_verified": True,
                "original_true_operator_reduction_certified": True,
                "independent_Mh_matrix_or_char0_CRT_computed": False,
            })
            index = self.cache(name)
        answer = [zero() for _ in range(count)]
        for entry, (first, stop) in zip(index["row_blocks"], self.blocks):
            block = self.S.load(entry)
            assert (block["row_first"], block["row_stop"]) == (first, stop)
            assert block["target"] == target and block["regular_degree_bound"] == degree
            raw = block["coefficient_matrices_low_to_high"]
            assert len(raw) == count
            for k in range(count):
                assert len(raw[k]) == stop-first
                for r in range(first, stop):
                    assert len(raw[k][r-first]) == FREE
                    for c in range(FREE):
                        value = raw[k][r-first][c]
                        assert isinstance(value, int) and 0 <= value < PRIME
                        if k > degree+EPS[c]-EPS[r]:
                            assert value == 0
                        answer[k][r, c] = value
        self.operator_arrays[target] = answer
        return answer

    def verify_and_transport_operators(self):
        name = "R827-complete-short-operator-identities-and-sigma-transport"
        old = self.cache(name)
        B, g, Gamma = [self.operator(target) for target in ("B", "g", "Gamma")]
        if old is None:
            for target, matrices, vector in (("B", B, self.vB), ("g", g, self.gh_mod["g"])):
                degree = 5 if target == "B" else 3
                for k, matrix in enumerate(matrices):
                    for i in range(FREE):
                        expected = int(vector[k][i, 0]) if k < len(vector) else 0
                        assert int(matrix[i, 0]) == expected
                for z0 in range(degree+4):
                    check_name = "R827-identity-"+target+"-commutator-z-"+str(z0)
                    if self.cache(check_name) is None:
                        self.budget()
                        M, W = evaluate(matrices, z0), evaluate(self.W, z0)
                        assert M*W == W*M
                        self.put(check_name, {
                            "target": target, "prime": PRIME, "z0": z0,
                            "entry_degree_bound": degree+3, "whole_matrix_commutator_zero": True,
                            "unit_Krylov_node_required_for_this_check": False,
                        })
            for k, matrix in enumerate(Gamma):
                for i in range(FREE):
                    assert not matrix[i, 0]
                    expected = int(self.gh_mod["h"][k][i, 0]) if k < 4 else 0
                    assert int(matrix[i, 1]) == expected
            for z0 in range(7):
                check_name = "R827-identity-Gamma-nested-commutator-z-"+str(z0)
                if self.cache(check_name) is None:
                    self.budget()
                    Q, W, Mg, Wprime = (evaluate(value, z0) for value in (Gamma, self.W, g, self.Wprime))
                    H = Q*W-W*Q+Mg*Wprime
                    assert H*W == W*H
                    vh = evaluate(self.gh_mod["h"], z0)
                    assert all(int(H[i, 0]) == int(vh[i, 0]) for i in range(FREE))
                    self.put(check_name, {
                        "prime": PRIME, "z0": z0, "whole_nested_commutator_zero": True,
                        "original_h_first_column_verified": True, "entry_degree_bound": 6,
                        "independent_Mh_reconstruction": False,
                    })
        sigma = {}
        for target, matrices, degree in (("B", B, 5), ("g", g, 3), ("Gamma", Gamma, 2)):
            index_name = "R827-target-"+target+"-sigma-polynomial-index"
            index = self.cache(index_name)
            if index is None:
                entries = []
                for first, stop in self.blocks:
                    block_name = "R827-target-"+target+"-sigma-rows-"+str(first).zfill(3)
                    block = self.cache(block_name)
                    if block is None:
                        raw = [[[0]*FREE for _ in range(stop-first)] for _ in range(degree+3)]
                        for r in range(first, stop):
                            for c in range(FREE):
                                terms = {}
                                if target in ("B", "g"):
                                    sign = 1 if target == "B" else -1
                                    for k, matrix in enumerate(matrices):
                                        power = degree-EPS[r]+EPS[c]-k
                                        value = sign*int(matrix[r, c]) % PRIME
                                        terms[power] = (terms.get(power, 0)+value) % PRIME
                                else:
                                    for k, matrix in enumerate(Gamma):
                                        power = 1-EPS[r]+EPS[c]-k
                                        terms[power] = (terms.get(power, 0)+int(matrix[r, c])) % PRIME
                                    for k, matrix in enumerate(g):
                                        power = 2-EPS[r]+EPS[c]-k
                                        terms[power] = (terms.get(power, 0)-EPS[c]*int(matrix[r, c])) % PRIME
                                for k, value in terms.items():
                                    if k < 0 or k > degree+EPS[c]-EPS[r]:
                                        assert value == 0
                                    else:
                                        raw[k][r-first][c] = value
                        self.put(block_name, {
                            "target": target, "chart": "sigma", "prime": PRIME,
                            "row_first": first, "row_stop": stop, "regular_degree_bound": degree,
                            "coefficient_matrices_low_to_high": raw,
                            "source_tau_operator": self.S.spec("R827-target-"+target+"-tau-polynomial-index"),
                            "source_tau_g_operator": self.S.spec("R827-target-g-tau-polynomial-index"),
                            "all_negative_powers_and_weighted_zeros_verified": True,
                            "g_matrix_means_negative_sigma_base_derivative": target == "g",
                            "same_original_function_derivation_and_connection_preserved": True,
                        })
                    entries.append(self.S.spec(block_name))
                self.put(index_name, {
                    "target": target, "chart": "sigma", "prime": PRIME, "regular_degree_bound": degree,
                    "normal_basis_rank": FREE, "normal_basis_degrees": EPS, "row_blocks": entries,
                    "source_tau_operator": self.S.spec("R827-target-"+target+"-tau-polynomial-index"),
                    "all_negative_powers_and_weighted_zeros_verified": True,
                    "g_matrix_means_negative_sigma_base_derivative": target == "g",
                })
                index = self.cache(index_name)
            answer = [zero() for _ in range(degree+3)]
            for entry, (first, stop) in zip(index["row_blocks"], self.blocks):
                block = self.S.load(entry)
                for k, rows in enumerate(block["coefficient_matrices_low_to_high"]):
                    for r, row in enumerate(rows):
                        for c, value in enumerate(row):
                            answer[k][first+r, c] = value
            sigma[target] = answer
        self.sigma_operators = sigma
        if old is None:
            self.put(name, {
                "prime": PRIME, "operator_indexes": {
                    target: {chart: self.S.spec("R827-target-"+target+"-"+chart+"-polynomial-index")
                             for chart in ("tau", "sigma")} for target in ("B", "g", "Gamma")},
                "B_first_column_is_original_vB": True, "g_first_column_is_original_vg": True,
                "Gamma_first_column_zero_and_second_column_original_vh": True,
                "B_commutator_full_polynomial_identity_certified_by_nine_points": True,
                "g_commutator_full_polynomial_identity_certified_by_seven_points": True,
                "Gamma_nested_full_polynomial_identity_certified_by_seven_points": True,
                "all_sigma_negative_powers_and_original_minus_sign_verified": True,
                "all_operators_are_true_original_p_integral_reductions": True,
                "actual_characteristic_zero_operator_CRT_repeated": False,
            })
        return self.S.spec(name)

    def layer(self, chart, k, precision=None):
        assert chart in ("tau", "sigma") and k >= 0
        full_count = 8+2*k
        requested = full_count if chart == "tau" else min(int(precision), full_count)
        assert 1 <= requested <= full_count
        if k == 0:
            matrices = self.operator_arrays["B"] if chart == "tau" else self.sigma_operators["B"]
            return matrices, self.S.spec("R827-target-B-"+chart+"-polynomial-index")
        key = chart, k, requested
        if key in self.layer_arrays:
            return self.layer_arrays[key]
        previous_precision = None if chart == "tau" else requested+1
        previous, previous_source = self.layer(chart, k-1, previous_precision)
        Gamma = self.operator_arrays["Gamma"] if chart == "tau" else self.sigma_operators["Gamma"]
        G = self.operator_arrays["g"] if chart == "tau" else self.sigma_operators["g"]
        index_name = "R827-"+chart+"-layer-"+str(k).zfill(3)+"-precision-"+str(requested).zfill(4)+"-index"
        index = self.cache(index_name)
        if index is None:
            records = []
            for n in range(requested):
                for first, stop in self.blocks:
                    block_name = "R827-"+chart+"-layer-"+str(k).zfill(3)+"-coefficient-"+str(n).zfill(4)+"-rows-"+str(first).zfill(3)
                    old = self.cache(block_name)
                    if old is None:
                        self.budget()
                        value = zero(stop-first, FREE)
                        for a, matrix in enumerate(Gamma):
                            b = n-a
                            if 0 <= b < len(previous):
                                left = nmod_mat([[int(matrix[r, c]) for c in range(FREE)]
                                                 for r in range(first, stop)], PRIME)
                                value += left*previous[b]
                        for a, matrix in enumerate(G):
                            b = n-a+1
                            if 1 <= b < len(previous):
                                left = nmod_mat([[int(matrix[r, c]) for c in range(FREE)]
                                                 for r in range(first, stop)], PRIME)
                                value += (left*previous[b])*b
                        raw = matrix_rows(value)
                        for r in range(first, stop):
                            for c in range(FREE):
                                if n > 5+EPS[c]+2*k-EPS[r]:
                                    assert raw[r-first][c] == 0
                        self.put(block_name, {
                            "chart": chart, "derivative_order": k, "coefficient_exponent": n,
                            "row_first": first, "row_stop": stop, "prime": PRIME,
                            "coefficient_matrix_mod_prime": raw,
                            "source_previous_layer": previous_source,
                            "source_Gamma_operator": self.S.spec("R827-target-Gamma-"+chart+"-polynomial-index"),
                            "source_base_derivative_operator": self.S.spec("R827-target-g-"+chart+"-polynomial-index"),
                            "previous_available_coefficient_count": len(previous),
                            "previous_full_polynomial_degree_bound": 7+2*(k-1),
                            "all_required_previous_coefficients_present_or_structurally_zero": True,
                            "source_original_generator_weights": [5+e for e in EPS],
                            "original_weighted_support_verified": True,
                            "sigma_negative_base_derivative_preserved": chart == "sigma",
                            "old_completed_coefficient_not_recomputed": True,
                        })
                        old = self.cache(block_name)
                    assert old["chart"] == chart and old["derivative_order"] == k
                    assert old["coefficient_exponent"] == n and old["original_weighted_support_verified"] is True
                    assert (old["row_first"], old["row_stop"]) == (first, stop)
                    records.append(self.S.spec(block_name))
            self.put(index_name, {
                "chart": chart, "derivative_order": k, "prime": PRIME,
                "precision_stop": requested, "full_polynomial_degree_bound": 7+2*k,
                "full_polynomial_coefficients_computed": requested == full_count,
                "coefficient_row_blocks": records, "normal_basis_rank": FREE,
                "normal_basis_degrees": EPS, "original_generator_weights": [5+e for e in EPS],
                "all_required_coefficient_blocks_complete": True,
                "higher_requested_precision_can_append_without_repeating_completed_coefficients": True,
            })
            index = self.cache(index_name)
        answer = [zero() for _ in range(requested)]
        assert len(index["coefficient_row_blocks"]) == requested*len(self.blocks)
        for entry in index["coefficient_row_blocks"]:
            data = self.S.load(entry)
            n, first, stop = data["coefficient_exponent"], data["row_first"], data["row_stop"]
            assert 0 <= n < requested
            for local, row in enumerate(data["coefficient_matrix_mod_prime"]):
                assert len(row) == FREE
                for c, value in enumerate(row):
                    assert isinstance(value, int) and 0 <= value < PRIME
                    answer[n][first+local, c] = value
        result = answer, self.S.spec(index_name)
        self.layer_arrays[key] = result
        return result

    def infinity_certificate(self):
        name = "R827-sigma-infinity-order-"+str(self.q).zfill(4)+"-certificate"
        old = self.cache(name)
        if old is not None:
            return self.S.spec(name)
        constants, layer_sources = [], []
        for k in range(self.q+1):
            self.budget()
            values, entry = self.layer("sigma", k, self.q+1-k)
            constants.append(values[0])
            layer_sources.append({"derivative_order": k, "source": entry,
                                  "required_precision_stop": self.q+1-k})
        matrix = nmod_mat([[int(constants[k][r, c]) for k in range(self.q+1) for c in range(FREE)]
                          for r in range(FREE)], PRIME)
        reduced, rank = matrix.rref()
        pivots = [next(j for j in range(matrix.ncols()) if reduced[i, j]) for i in range(rank)]
        minor, determinant = None, None
        if rank == FREE:
            minor_matrix = nmod_mat([[int(matrix[i, j]) for j in pivots] for i in range(FREE)], PRIME)
            determinant = int(minor_matrix.det())
            assert determinant
            minor = matrix_rows(minor_matrix)
        P0 = self.C_data["sigma"]["P_polynomial"][0]
        assert P0
        return self.put(name, {
            "prime": PRIME, "derivative_order": self.q, "chart": "sigma", "base_point": 0,
            "source_C_reduction": self.C_source, "actual_C_sigma_determinant_at_zero": P0,
            "source_layer_jets": layer_sources, "initial_jet_precision_stop": self.q+1,
            "jet_precision_decreases_by_one_per_derivative": True,
            "matrix_rows": FREE, "matrix_columns": FREE*(self.q+1),
            "column_order": "derivative_order=0..q, original_B_times_normal_basis_index=0..271",
            "actual_rank_mod_prime": rank, "actual_selected_pivot_columns": pivots,
            "actual_full_minor_matrix_mod_prime": minor,
            "actual_full_minor_determinant_mod_prime": determinant,
            "whole_infinity_fiber_surjective": rank == FREE,
            "raw_normal_columns_have_same_rank_as_complete_C_coordinates": True,
            "failure_does_not_negate_other_global_sources_or_characteristic_zero_Iq": rank != FREE,
            "characteristic_zero_or_new_torsion_jets_computed": False,
        })

    def C_column(self, k, column):
        name = "R827-tau-layer-"+str(k).zfill(3)+"-C-column-"+str(column).zfill(3)
        old = self.cache(name)
        if old is not None:
            return old, self.S.spec(name)
        values, source = self.layer("tau", k)
        self.budget()
        original = [nmod_poly([int(matrix[r, column]) for matrix in values], PRIME) for r in range(FREE)]
        q = [nmod_poly(row, PRIME) for row in self.C_data["tau"]["q_polynomials"]]
        P = nmod_poly(self.C_data["tau"]["P_polynomial"], PRIME)
        numerator = original[271]
        for r in range(271):
            numerator += q[r]*original[r]
        quotient, remainder = divmod(numerator, P)
        assert not remainder and P*quotient == numerator
        assert quotient.degree() <= 5+EPS[column]+2*k-1
        answer = [list(map(int, value.coeffs())) for value in original[:271]]
        answer.append([int(x) for x in quotient.coeffs()])
        restored = P*quotient
        for r in range(271):
            restored -= q[r]*original[r]
        assert restored == original[271]
        self.put(name, {
            "prime": PRIME, "chart": "tau", "derivative_order": k,
            "original_B_times_normal_basis_index": column,
            "original_generator_weight": 5+EPS[column],
            "source_original_layer": source, "source_complete_C": self.C_source,
            "column_coefficients_in_original_C_basis": answer,
            "exact_monic_degree20_division_and_original_column_multiplyback_verified": True,
            "complete_C_basis_change_not_an_ideal_quotient": True,
        })
        return self.cache(name), self.S.spec(name)

    def tau_certificate(self):
        name = "R827-tau-order-"+str(self.q).zfill(4)+"-certificate"
        old = self.cache(name)
        if old is not None:
            return self.S.spec(name)
        previous = None
        for path in self.out.glob("R827-tau-order-*-certificate.json.gz"):
            digits = path.name[len("R827-tau-order-"):].split("-")[0]
            if not digits.isdigit():
                continue
            order = int(digits)
            if order < self.q and (previous is None or order > previous["derivative_order"]):
                previous = self.S.load(spec(path))
                previous["actual_source_certificate"] = spec(path)
        if previous is not None and previous["whole_affine_polynomial_module_surjective"]:
            return previous["actual_source_certificate"]
        borrowed, first_layer, source_previous = [], 0, None
        if previous is not None:
            source_previous = previous["actual_source_certificate"]
            previous_final = self.S.load(previous["reduction_final_index"])
            count = FREE if previous["full_row_rank_reduction_complete"] else previous_final["vector_count"]
            borrowed = list(previous_final["vectors"][:count])
            first_layer = previous["derivative_order"]+1
        count = len(borrowed)+FREE*(self.q-first_layer+1)
        label = "R827-tau-order-"+str(self.q).zfill(4)+"-Hermite"
        matrix = modules.Matrix(self.S, self.A, label, count, FREE, "columns", FREE)
        source = {
            "prime": PRIME, "derivative_order": self.q, "source_complete_C": self.C_source,
            "previous_complete_module_certificate": source_previous,
            "borrowed_transformed_columns": borrowed,
            "new_derivative_orders": list(range(first_layer, self.q+1)),
            "all_generator_columns_are_true_original_reductions": True,
        }
        if matrix.state is None:
            vectors = list(borrowed)
            offset = len(borrowed)
            for k in range(first_layer, self.q+1):
                for c in range(FREE):
                    self.budget()
                    data, entry = self.C_column(k, c)
                    index = offset+(k-first_layer)*FREE+c
                    if not matrix.initial_tile_exists(index, 0):
                        matrix.put_initial_tile(index, 0, data["column_coefficients_in_original_C_basis"], entry)
                    vectors.append(matrix.initial_vector(index))
            matrix.initialize(vectors, modules.generic.reducer_control(FREE, True), source)
        else:
            original_initial = self.S.load(matrix.state["initialization"])
            matrix.initialize(original_initial["vectors"], modules.generic.reducer_control(FREE, True), source)
        missing = None
        if not matrix.finished:
            try:
                modules.reduce_columns(matrix, FREE)
            except AssertionError as error:
                # This one specific outcome is a valid failed sufficient test,
                # not a source error and not a claimed exact total rank.
                if str(error) != "Actual polynomial matrix failed its required full row rank":
                    raise
                control = matrix.state["control"]
                assert control["phase"] == "find_pivot"
                row = control["pivot_row"]
                assert all(not matrix.entry(matrix.state["vectors"][j], row)
                           for j in range(row, matrix.count))
                missing = row
                matrix.finish({
                    "full_row_rank_reduction_complete": False,
                    "first_missing_pivot_row": row,
                    "pivot_row_is_not_reported_as_the_total_rank": True,
                    "remaining_entries_of_that_pivot_row_verified_zero": True,
                    "completed_unimodular_transformation_preserves_entire_source_module": True,
                    "exact_total_rank_computed": False,
                    "actual_pivot_rank": None, "canonical_column_Hermite_remainders": False,
                })
        if matrix.state.get("full_row_rank_reduction_complete") is False:
            missing = matrix.state["first_missing_pivot_row"]
            surjective, full_rank, diagonals = False, False, None
        else:
            assert matrix.state["actual_pivot_rank"] == FREE
            diagonals = matrix.state["actual_diagonal"]
            assert len(diagonals) == FREE
            full_rank = True
            surjective = all(row["degree"] == 0 for row in diagonals)
            if surjective:
                for c, values in modules.all_final_entries(matrix):
                    assert all(value == int(c == r) for r, value in enumerate(values))
        archives = modules.archive_history(matrix)
        return self.put(name, {
            "prime": PRIME, "chart": "tau", "derivative_order": self.q,
            "source_complete_C": self.C_source, "previous_module_certificate": source_previous,
            "source_generator_weights": [5+e for e in EPS],
            "source_module_in_complete_C_basis": source,
            "reduction_final_index": self.S.spec(matrix.final_name),
            "full_row_rank_reduction_complete": full_rank,
            "first_missing_pivot_row": missing,
            "exact_total_rank_claimed_if_missing_pivot": False,
            "actual_Hermite_diagonal": diagonals,
            "whole_affine_polynomial_module_surjective": surjective,
            "all_entries_and_zero_remainder_columns_verified_when_surjective": surjective,
            "complete_unimodular_polynomial_generation_history_verified": True,
            "history_archive_indexes": archives,
            "no_characteristic_zero_Bezout_or_module_Hermite_computed": True,
            "failure_is_only_this_sufficient_original_residue_test": not surjective,
        })

    def finish(self, source_audit, operator_index, infinity_spec, tau_spec):
        infinity = self.S.load(infinity_spec)
        tau = self.S.load(tau_spec) if tau_spec is not None else None
        success = infinity["whole_infinity_fiber_surjective"] and \
                  tau is not None and tau["whole_affine_polynomial_module_surjective"]
        assert infinity["derivative_order"] == self.q
        if tau is not None:
            assert tau["derivative_order"] <= self.q
        history_indexes, archive_files = [], []
        for path in sorted(self.out.glob("R827-*-history-*-index.json.gz")):
            data = self.S.load(spec(path))
            assert spec(self.out/data["archive"]["file"]) == data["archive"]
            history_indexes.append(spec(path))
            archive_files.append(data["archive"])
        result_name = "R827-derivative-order-"+str(self.q).zfill(4)+"-result"
        result = {
            "prime": PRIME, "original_branch": 0, "canonical_free_column": 1186,
            "certification_mode": MODE, "actual_derivative_order": self.q,
            "source_audit": source_audit, "normal_B_vector": self.vB_source,
            "operator_identity_and_transport_certificate": operator_index,
            "operator_indexes": self.S.load(operator_index)["operator_indexes"],
            "tau_Hermite_certificate": tau_spec, "sigma_infinity_certificate": infinity_spec,
            "whole_tau_polynomial_module_surjective": bool(tau and tau["whole_affine_polynomial_module_surjective"]),
            "whole_sigma_infinity_fiber_surjective": infinity["whole_infinity_fiber_surjective"],
            "tau_Hermite_skipped_because_infinity_test_failed": tau is None,
            "original_characteristic_zero_Iq_equals_C": success,
            "safe_D_multiplicity_bound": self.q//3 if success else None,
            "original_D_reduced_certified": bool(success and self.q//3 <= 1),
            "actual_maximum_D_multiplicity_computed": False,
            "actual_D_eta_or_height_computed": False,
            "failure_does_not_assert_Iq_not_equal_C": not success,
            "history_archive_indexes": history_indexes,
        }
        result_spec = self.put(result_name, result)
        manifest_name = "R827-complete-stage-manifest"
        completed, current = [], []
        for path in sorted(self.out.glob("R827-*.json.gz")):
            if path.name == manifest_name+".json.gz":
                continue
            data = read(path)
            assert data["configuration"] == self.tag
            (completed if data["complete"] is True else current).append(spec(path))
        inventory = self.S.put(manifest_name, {
            "files": completed, "current_checkpoints": current,
            "history_archives": archive_files, "history_archive_indexes": history_indexes,
            "only_active_exact_outputs_not_committed_or_released": True,
        }, replace=True)
        final = dict(result, result=RESULT, p=41, complete=True, configuration=self.tag,
                     requested_derivative_order=self.q, derivative_order_result=result_spec,
                     completed_scope="original_residue_sufficient_termination_test",
                     normal_basis_rank=FREE, normal_basis_degrees=EPS,
                     stage_manifest=inventory, history_archives=archive_files,
                     seconds=time.monotonic()-self.started)
        save(self.out/FINAL, final)
        save(self.out/"core-receipt.json", {
            "result": RESULT, "complete": True, "source_sha256": sha(__file__),
            "certificate_sha256": sha(self.out/FINAL),
            "actual_derivative_order": self.q,
            "original_characteristic_zero_Iq_equals_C": success,
            "safe_D_multiplicity_bound": self.q//3 if success else None,
            "actual_D_eta_or_height_computed": False,
        })
        return 0

    def run(self):
        source = self.source_audit()
        self.ordinary_inputs()
        self.cusp_inputs()
        self.normal_B()
        self.grid()
        operators = self.verify_and_transport_operators()
        infinity = self.infinity_certificate()
        tau = self.tau_certificate() if self.S.load(infinity)["whole_infinity_fiber_surjective"] else None
        return self.finish(source, operators, infinity, tau)


def main():
    guard()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--proof", type=Path, required=True)
    parser.add_argument("--method", type=Path, required=True)
    parser.add_argument("--retained", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    try:
        job = Job(args)
        return job.run()
    except BudgetStop as error:
        args.output.mkdir(parents=True, exist_ok=True)
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "budget_stop": str(error),
            "completed_source_bound_stages_and_atomic_module_checkpoints_retained": True,
            "actual_D_eta_or_height_computed": False,
        })
        return 124
    except UnitFailure as error:
        args.output.mkdir(parents=True, exist_ok=True)
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "original_place_sufficient_unit_condition_failed": str(error),
            "characteristic_zero_failure_claimed": False,
            "completed_source_bound_stages_retained": True,
        })
        return 125


if __name__ == "__main__":
    raise SystemExit(main())
