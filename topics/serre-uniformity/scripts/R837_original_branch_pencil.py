#!/usr/bin/env python3
"""Original P0 evaluation and the fixed 21-point pencil (public Actions only).

Every old CM or Fourier coefficient is read from its original source.  New
arithmetic consists of two rational reflection right hand sides, the complete
fixed-point kernel, and products of the new two anchors with original V3.
"""

import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
import time
import traceback

from flint import fmpq, fmpq_mat, fmpz, nmod_mat, nmod_poly


RESULT = "R837-original-fixed-branch-pencil"
FINAL = "p41-original-fixed-branch-pencil-certificate.json"
PREFIX = "R837-"
INVENTORY = "R837-stage-manifest.json.gz"
BASE_KEYS = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
PROOFS = ("proof", "method", "descent_proof", "CM_proof")
H64 = re.compile(r"[0-9a-f]{64}")
XI = 40
ORDERS = 69
STRIDE = 79
V1 = 146
V2 = 418
V3 = 690
U_DIM = 397
PENCIL_RANK = 1213
PRODUCT_BATCH = 17
SOURCE_DEFINITIONS = {
    "R790": {
        "result": "R790-original-CM-fiber-jets",
        "core_sha256": "981eb543b791db416fad355d83eedb9bfe3b86b3e5461483fe4397e2129040b6",
        "certificate": "p41-original-CM-fiber-jets-certificate.json",
        "stage_manifest": "R790-stage-manifest.json.gz",
    },
    "R786": {
        "result": "R786-exact-original-power5-short-basis",
        "core_sha256": "4508095a95a2bcaec8c8db8fcd550fbc618b017d2bc0007945783bc109dbf851",
        "certificate": "p41-exact-original-power5-short-basis-certificate.json",
        "stage_manifest": "R786-exact-stages-manifest.json.gz",
    },
}
SEARCH_STRATEGY = {
    "fixed_u": "first u0+c*u1, c=1,2,3, with at least two original V2 terms",
    "second_anchor": "sum(a**j*u_j,j=0..396), a=0,1,-1,2,-2,...",
    "one_term_second_anchor": "record and skip without repeating an old monomial product",
    "prime_sequence": "increasing primes >=1000000009 congruent to 1 modulo 3",
    "zeta_root": "first nontrivial cubic root obtained from a=2,3,...",
    "trial_order": "diagonal prime-index plus parameter-index; increasing prime-index",
    "coordinates": "original 69 qY coefficients in 1,xi,...,xi**39",
    "product_stride": STRIDE,
    "new_product_batch_size": PRODUCT_BATCH,
    "success": "actual rank1213 and nonzero1213 minor on the entire 2760-coordinate matrix",
    "modular_failure_is_not_characteristic_zero_failure": True,
    "runtime_and_trial_limit_excluded_from_mathematical_identity": True,
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if path.suffix == ".gz":
        with temporary.open("wb") as stream:
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb", mtime=0, compresslevel=2) as out:
                out.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def plain(value):
    answer = {key: value[key] for key in ("file", "bytes", "sha256")}
    assert isinstance(answer["file"], str) and Path(answer["file"]).name == answer["file"]
    assert "\\" not in answer["file"] and answer["file"] not in (".", "..")
    assert isinstance(answer["bytes"], int) and answer["bytes"] >= 0
    assert H64.fullmatch(answer["sha256"])
    return answer


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def qdecode(value):
    assert isinstance(value, list) and len(value) == 2
    answer = fmpq(int(value[0]), int(value[1]))
    assert answer.denom() > 0
    return answer


def qencode(value):
    value = fmpq(value)
    return [str(value.numer()), str(value.denom())]


def kdecode(value):
    assert isinstance(value, list) and len(value) == 2
    return qdecode(value[0]), qdecode(value[1])


def kencode(value):
    return [qencode(value[0]), qencode(value[1])]


def kzero():
    return fmpq(0), fmpq(0)


def kadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def ksub(a, b):
    return a[0] - b[0], a[1] - b[1]


def kscale(a, value):
    value = fmpq(value)
    return a[0] * value, a[1] * value


def kmul(a, b):
    # zeta**2=-zeta-1.
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0] - a[1] * b[1]


def kinv(a):
    denominator = a[0] * a[0] - a[0] * a[1] + a[1] * a[1]
    assert denominator
    answer = ((a[0] - a[1]) / denominator, -a[1] / denominator)
    assert kmul(a, answer) == (fmpq(1), fmpq(0))
    return answer


def knonzero(a):
    return bool(a[0] or a[1])


def sparse_encode(value):
    return [{"original_V2_index": i, "coefficient_K_1_zeta": kencode(value[i])}
            for i in sorted(value) if knonzero(value[i])]


def sparse_decode(value):
    result = {}
    for row in value:
        i = int(row["original_V2_index"])
        assert 0 <= i < V2 and i not in result
        pair = kdecode(row["coefficient_K_1_zeta"])
        assert knonzero(pair)
        result[i] = pair
    return result


def sparse_sum(terms):
    answer = {}
    for coefficient, vector in terms:
        coefficient = fmpq(coefficient)
        if not coefficient:
            continue
        for i, pair in vector.items():
            answer[i] = kadd(answer.get(i, kzero()), kscale(pair, coefficient))
    return {i: pair for i, pair in answer.items() if knonzero(pair)}


def primitive_sparse(vector):
    denominator = 1
    for pair in vector.values():
        for value in pair:
            denominator = math.lcm(denominator, int(value.denom()))
    integer = {}
    content = 0
    for i, pair in vector.items():
        row = [int((value * denominator).numer()) for value in pair]
        if any(row):
            integer[i] = row
            for value in row:
                content = math.gcd(content, abs(value))
    assert content
    integer = {i: [value // content for value in pair] for i, pair in integer.items()}
    scale = fmpq(denominator, content)
    assert all(kscale(vector[i], scale) == tuple(fmpq(x) for x in pair)
               for i, pair in integer.items())
    assert set(integer) == set(vector)
    return integer, scale, denominator, content


def integer_sparse_encode(value):
    return [{"original_V2_index": i, "integer_coefficients_K_1_zeta": [str(x) for x in value[i]]}
            for i in sorted(value)]


def integer_sparse_decode(value):
    result = {}
    for row in value:
        i = row["original_V2_index"]
        assert isinstance(i, int) and 0 <= i < V2 and i not in result
        pair = tuple(int(x) for x in row["integer_coefficients_K_1_zeta"])
        assert len(pair) == 2 and any(pair)
        result[i] = pair
    assert result
    return result


def pivots(matrix):
    reduced, rank = matrix.rref()
    answer = [next(j for j in range(reduced.ncols()) if reduced[i, j]) for i in range(rank)]
    assert len(answer) == len(set(answer)) == rank
    return answer


def parameter_value(index):
    assert index >= 0
    if not index:
        return 0
    return (index + 1) // 2 if index % 2 else -(index // 2)


def trial_pair(index):
    diagonal = 0
    remainder = index
    while remainder > diagonal:
        remainder -= diagonal + 1
        diagonal += 1
    return remainder, diagonal - remainder


def anchor_scope(trial, which, ell):
    assert which in ("u", "v")
    if which == "u":
        return "R837-fixed-u-prime-" + str(ell)
    return "R837-trial-" + str(trial).zfill(5) + "-anchor-v"


def packed(rows, ell):
    assert len(rows) == ORDERS and all(len(row) == XI for row in rows)
    values = [0] * (STRIDE * (ORDERS - 1) + XI)
    for n, row in enumerate(rows):
        values[n * STRIDE:n * STRIDE + XI] = [int(x) % ell for x in row]
    return nmod_poly(values, ell)


def unpack_product(value, ell):
    answer = []
    for n in range(ORDERS):
        folded = [0] * 41
        for r in range(79):
            folded[r % 41] = (folded[r % 41] + int(value[n * STRIDE + r])) % ell
        top = folded[40]
        answer.extend((folded[r] - top) % ell for r in range(40))
    assert len(answer) == ORDERS * XI
    return answer


class BudgetStop(RuntimeError):
    pass


class TrialLimit(RuntimeError):
    pass


class Source:
    def __init__(self, label, item):
        self.label = label
        self.directory = Path(item["directory"])
        definition = SOURCE_DEFINITIONS[label]
        self.identity = {key: item[key] for key in BASE_KEYS}
        assert self.identity["result"] == definition["result"]
        assert self.identity["core_sha256"] == definition["core_sha256"]
        self.files = {name: plain(row) for name, row in item["files"].items()}
        assert all(name == row["file"] for name, row in self.files.items())
        self.file_fingerprint = fingerprint([self.files[name] for name in sorted(self.files)])
        assert self.file_fingerprint == item["selected_files_sha256"]
        for row in self.files.values():
            path = self.directory / row["file"]
            assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
        self.certificate_spec = plain(item["certificate"])
        self.manifest_spec = plain(item["stage_manifest"])
        assert self.certificate_spec["file"] == definition["certificate"]
        assert self.manifest_spec["file"] == definition["stage_manifest"]
        assert self.files[self.certificate_spec["file"]] == self.certificate_spec
        assert self.files[self.manifest_spec["file"]] == self.manifest_spec
        self.certificate = read(self.directory / self.certificate_spec["file"])
        assert self.certificate["result"] == self.identity["result"] and self.certificate["complete"] is True
        self.tag = self.certificate["configuration"]
        self.tag_hash = fingerprint(self.tag)
        assert self.tag_hash == item["configuration_sha256"]
        assert self.tag["result"] == self.identity["result"]
        assert self.tag["source_sha256"] == self.identity["core_sha256"]
        self.stage_manifest = read(self.directory / self.manifest_spec["file"])
        assert self.stage_manifest["complete"] is True and self.stage_manifest["configuration"] == self.tag
        self.stages = {row["file"]: plain(row) for row in self.stage_manifest["files"]}
        assert len(self.stages) == len(self.stage_manifest["files"])
        self.bound_identity = dict(self.identity, configuration_sha256=self.tag_hash,
            selected_files_sha256=self.file_fingerprint, selected_file_count=len(self.files),
            certificate=self.certificate_spec, stage_manifest=self.manifest_spec)
        if "index" in item:
            self.bound_identity["index"] = plain(item["index"])
            assert self.files[item["index"]["file"]] == plain(item["index"])

    def stage(self, name):
        assert self.files[name] == self.stages[name]
        answer = read(self.directory / name)
        assert answer["complete"] is True and answer["configuration"] == self.tag
        return answer

    def spec(self, name):
        return self.files[name]


class Job:
    def __init__(self, args):
        self.args = args
        self.started = time.monotonic()
        self.deadline = self.started + args.budget_minutes * 60
        self.out = Path(args.out)
        self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert self.item["producer_inputs_pending"] is False
        assert self.item["core_sha256"] == sha(__file__)
        assert self.item["core"] == Path(__file__).name
        assert 0 < args.budget_minutes <= 300
        self.maximum_trials = self.item["controls"]["maximum_pencil_trials"]
        assert isinstance(self.maximum_trials, int) and self.maximum_trials > 0
        for key in PROOFS:
            assert sha(self.item[key]) == self.item[key + "_sha256"]
        assert set(self.item["sources"]) == set(SOURCE_DEFINITIONS)
        self.sources = {label: Source(label, self.item["sources"][label])
                        for label in sorted(SOURCE_DEFINITIONS)}
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "python_flint": "0.9.0", "p": 41,
            **{key + "_sha256": self.item[key + "_sha256"] for key in PROOFS},
            "sources": {label: self.sources[label].bound_identity for label in sorted(self.sources)},
            "coefficient_field": "K=Q(zeta), zeta**2+zeta+1=0",
            "original_qY_xi_basis": "1,xi41,...,xi41**39 with Phi41=0",
            "original_integer_scales": {"power1": "6724", "power2": "45212176", "power3": "304006671424"},
            "reflection_prefix_orders": 14, "product_prefix_orders": ORDERS,
            "fixed_branch_degree": 21, "fixed_branch_space_dimension": U_DIM,
            "target_pencil_rank": PENCIL_RANK, "search_strategy": SEARCH_STRATEGY,
        }
        self.V = {}
        self.recipes = {}
        self.CM = []
        self.spec_rows = {}
        self.prime_values = []
        self.packed_V3 = {}
        self.last_rank = None
        self.success_stage = None

    def check(self):
        if time.monotonic() >= self.deadline:
            raise BudgetStop("R837 public core budget reached; complete stages retained")

    def path(self, name):
        if name.endswith(".json.gz"):
            filename = name
        else:
            filename = name + ".json.gz"
        assert filename.startswith(PREFIX) and Path(filename).name == filename
        return self.out / filename

    def cache(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["configuration"] == self.tag and value["complete"] is True
        assert value.get("result", self.tag["result"]) == RESULT
        return value

    def store(self, name, value):
        path = self.path(name)
        assert not path.exists(), "A completed mathematical stage must not be replaced"
        data = dict(value, result=RESULT, complete=True, configuration=self.tag)
        save(path, data)
        print("R837_STAGE=" + json.dumps({"file": path.name, "sha256": sha(path)}, sort_keys=True), flush=True)
        return data

    def spec(self, name):
        return file_spec(self.path(name))

    def load_original_inputs(self):
        source = self.sources["R786"]
        for power, count, orders in ((1, V1, 14), (2, V2, ORDERS), (3, V3, ORDERS)):
            vectors, recipes, specs = [], [], []
            for i in range(count):
                self.check()
                name = "R786-exact-power-" + str(power) + "-row-" + str(i).zfill(4) + ".json.gz"
                data = source.stage(name)
                assert data["weight"] == 2 * power and data["bound_qY"] == 128
                assert data["integer_scale"] == str(82 ** (2 * power))
                assert data["original_R775_finite_coefficients_verified"] is True
                coefficients = data["integer_qY_xi_coefficients"]
                assert len(coefficients) == 129 and all(len(row) == XI for row in coefficients)
                recipe = data["recipe"]
                if power == 1:
                    assert recipe["kind"] == "det_semilinear_E1_pair_trace"
                    assert recipe["exact_global_field"] == "K"
                else:
                    assert recipe["kind"] == "product" and recipe["left_power"] == 1
                    assert recipe["right_power"] == power - 1
                    assert 0 <= recipe["left_index"] < V1
                    assert 0 <= recipe["right_index"] < (V1 if power == 2 else V2)
                vectors.append([[int(x) for x in row] for row in coefficients[:orders]])
                recipes.append(recipe)
                specs.append(source.spec(name))
            self.V[power], self.recipes[power], self.spec_rows[power] = vectors, recipes, specs
        cm_source = self.sources["R790"]
        for i in range(V1):
            self.check()
            name = "R790-M2-CM-jet-" + str(i).zfill(4) + ".json.gz"
            data = cm_source.stage(name)
            assert data["index"] == i and data["integer_scale"] == "6724"
            assert data["R786_power1_scale_preserved"] is True
            assert data["K_basis"] == ["1", "zeta=(-1+sqrt(-3))/2"]
            assert data["original_c1"] == 4424
            assert data["original_recipe"] == self.recipes[1][i]
            self.CM.append(kdecode(data["value_K_1_zeta"]))
        name = "R837-original-source-audit"
        cached = self.cache(name)
        if cached is None:
            self.store(name, {"original_CM_point": "P1", "original_c1": 4424,
                "original_CM_value_count": V1, "original_power_counts": {"1": V1, "2": V2, "3": V3},
                "all_selected_source_bytes_verified": True, "all_original_tags_verified": True,
                "all_original_recipes_and_scales_verified": True,
                "power1_recipes_equal_original_R790_recipes": True,
                "old_CM_torsion_trace_or_Fourier_arithmetic_recomputed": False,
                "mathematical_sources": {label: source.bound_identity for label, source in self.sources.items()}})

    def prime(self, index):
        while len(self.prime_values) <= index:
            i = len(self.prime_values)
            name = "R837-prime-" + str(i).zfill(4)
            data = self.cache(name)
            if data is None:
                ell = 1000000009 if not self.prime_values else self.prime_values[-1][0] + 2
                while ell % 3 != 1 or not fmpz(ell).is_prime():
                    self.check()
                    ell += 2
                assert ell < 2 ** 63
                base = 2
                while True:
                    root = pow(base, (ell - 1) // 3, ell)
                    if root not in (0, 1):
                        break
                    base += 1
                assert (root * root + root + 1) % ell == 0
                data = self.store(name, {"prime_index": i, "prime": ell, "zeta_root": root,
                    "root_source_base": base, "prime_proved": True, "zeta_root_verified": True})
            assert data["prime_index"] == i and data["prime_proved"] is True
            self.prime_values.append((data["prime"], data["zeta_root"]))
        return self.prime_values[index]

    def rational_minor(self, name, matrix, expected_rank):
        success = self.cache(name)
        if success is not None:
            assert success["actual_modular_rank"] == expected_rank
            return success
        prime_index = 0
        while True:
            self.check()
            ell, unused = self.prime(prime_index)
            attempt_name = name + "-prime-index-" + str(prime_index).zfill(4)
            data = self.cache(attempt_name)
            if data is None:
                columns = pivots(nmod_mat([[int(x) % ell for x in row] for row in matrix], ell))
                rank = len(columns)
                assert rank <= expected_rank
                if rank == expected_rank:
                    transposed = [[matrix[i][j] % ell for i in range(len(matrix))] for j in columns]
                    rows = pivots(nmod_mat(transposed, ell))
                    assert len(rows) == expected_rank
                    minor = nmod_mat([[matrix[i][j] % ell for j in columns] for i in rows], ell)
                    determinant = int(minor.det())
                    assert determinant
                else:
                    rows, determinant = [], None
                data = self.store(attempt_name, {"prime": ell, "prime_index": prime_index,
                    "matrix_shape": [len(matrix), len(matrix[0])], "expected_characteristic_zero_rank": expected_rank,
                    "actual_modular_rank": rank, "selected_rows": rows, "selected_columns": columns,
                    "minor_determinant_mod_prime": determinant,
                    "modular_rank_failure_does_not_assert_characteristic_zero_failure": rank != expected_rank})
            if data["actual_modular_rank"] == expected_rank:
                return self.store(name, {key: value for key, value in data.items()
                    if key not in ("configuration", "result", "complete")} | {"successful_attempt": self.spec(attempt_name)})
            prime_index += 1

    def P0_evaluation(self):
        name = "R837-original-P0-evaluation"
        cached = self.cache(name)
        if cached is not None:
            assert cached["original_P0_evaluation_certified"] is True
            return [kdecode(value) for value in cached["P0_values_K_1_zeta"]]
        matrix = [[self.V[1][i][n][r] for i in range(V1)] for n in range(14) for r in range(XI)]
        minor = self.rational_minor("R837-original-V1-reflection-minor", matrix, V1)
        assert minor["selected_columns"] == list(range(V1))
        selected = minor["selected_rows"]
        A = [[matrix[i][j] for j in range(V1)] for i in selected]
        self.check()
        Aq = fmpq_mat(A)
        right = fmpq_mat([[self.CM[i][c] for c in range(2)] for i in range(V1)])
        dual = Aq.transpose().solve(right)
        assert Aq.transpose() * dual == right
        result = []
        for j in range(V1):
            value = tuple(sum((dual[k, c] * ((-1) ** (selected[k] // XI)) * A[k][j]
                               for k in range(V1)), fmpq(0)) for c in range(2))
            result.append(value)
        dual_rows = [[qencode(dual[i, c]) for i in range(V1)] for c in range(2)]
        # Verify the saved dual formula independently of its subsequent use.
        for c in range(2):
            for j in range(V1):
                assert sum((qdecode(dual_rows[c][i]) * A[i][j] for i in range(V1)), fmpq(0)) == self.CM[j][c]
                assert sum((qdecode(dual_rows[c][i]) * ((-1) ** (selected[i] // XI)) * A[i][j]
                            for i in range(V1)), fmpq(0)) == result[j][c]
        self.store(name, {"original_P0_evaluation_certified": True, "value_count": V1,
            "coefficient_basis": ["1", "zeta=(-1+sqrt(-3))/2"],
            "original_source_point": "P1", "original_target_point": "P0=phi(c0)",
            "original_involution": "T**41; tY->1-tY; qY->-qY; even-weight factor1",
            "original_frame": "Phi_i=(82**2*T_i)*E6/E4**2, same frame at P0 and P1",
            "integer_scale_already_in_source": "6724", "additional_scale_inserted": False,
            "selected_prefix_rows": selected, "minor": self.spec("R837-original-V1-reflection-minor"),
            "dual_rows_Q": dual_rows, "P1_values_K_1_zeta": [kencode(x) for x in self.CM],
            "P0_values_K_1_zeta": [kencode(x) for x in result],
            "both_exact_dual_systems_multiplied_back": True,
            "all_146_reflected_outputs_verified": True,
            "full_reflection_matrix_not_constructed": True,
            "R790_source_rows": [self.sources["R790"].spec("R790-M2-CM-jet-" + str(i).zfill(4) + ".json.gz") for i in range(V1)],
            "R786_source_rows": self.spec_rows[1]})
        return result

    def V2_point_values(self, point):
        name = "R837-original-V2-P0-evaluation"
        cached = self.cache(name)
        if cached is not None:
            return [kdecode(x) for x in cached["P0_values_K_1_zeta"]]
        values = []
        for recipe in self.recipes[2]:
            values.append(kmul(point[recipe["left_index"]], point[recipe["right_index"]]))
        self.store(name, {"original_P0_evaluation": self.spec("R837-original-P0-evaluation"),
            "P0_values_K_1_zeta": [kencode(x) for x in values], "value_count": V2,
            "original_integer_scale_already_in_products": "45212176",
            "all_418_original_product_recipes_used_without_rescaling": True,
            "source_rows": self.spec_rows[2]})
        return values

    def cusp_kernel(self):
        name = "R837-original-V2-cusp-kernel"
        cached = self.cache(name)
        if cached is not None:
            assert cached["kernel_dimension"] == 398 and cached["all_40_rows_multiplied_back"] is True
            return [{row["original_V2_index"]: qdecode(row["coefficient_Q"])
                     for row in column} for column in cached["kernel_columns"]]
        C = [[self.V[2][j][0][r] for j in range(V2)] for r in range(XI)]
        minor = self.rational_minor("R837-original-V2-cusp-minor", C, 20)
        pivot_rows, pivot_columns = minor["selected_rows"], minor["selected_columns"]
        free_columns = [j for j in range(V2) if j not in set(pivot_columns)]
        assert len(free_columns) == 398
        A = fmpq_mat([[C[i][j] for j in pivot_columns] for i in pivot_rows])
        right = fmpq_mat([[-C[i][j] for j in free_columns] for i in pivot_rows])
        self.check()
        X = A.solve(right)
        left_full = fmpq_mat([[C[i][j] for j in pivot_columns] for i in range(XI)])
        right_full = fmpq_mat([[C[i][j] for j in free_columns] for i in range(XI)])
        residual = left_full * X + right_full
        assert all(not residual[i, j] for i in range(XI) for j in range(398))
        columns = []
        for j, free in enumerate(free_columns):
            vector = {free: fmpq(1)}
            for i, original in enumerate(pivot_columns):
                if X[i, j]:
                    vector[original] = X[i, j]
            columns.append(vector)
        self.store(name, {"matrix_shape": [40, 418], "actual_characteristic_zero_rank": 20,
            "kernel_dimension": 398, "minor": self.spec("R837-original-V2-cusp-minor"),
            "pivot_rows": pivot_rows, "pivot_columns": pivot_columns, "free_columns": free_columns,
            "kernel_columns": [[{"original_V2_index": i, "coefficient_Q": qencode(v[i])} for i in sorted(v)] for v in columns],
            "all_40_rows_multiplied_back": True,
            "complete_twenty_cusp_closed_point_condition": True,
            "old_R820_cusp_field_or_normal_ideal_not_recomputed": True})
        return columns

    def fixed_space(self, point_values):
        name = "R837-original-fixed-twenty-one-point-space"
        cached = self.cache(name)
        if cached is not None:
            assert cached["complete_fixed_branch_space_certified"] is True
            assert cached["dimension"] == U_DIM
            return [sparse_decode(x) for x in cached["basis_columns"]]
        cusp = self.cusp_kernel()
        values = []
        for column in cusp:
            result = kzero()
            for i, value in column.items():
                result = kadd(result, kscale(point_values[i], value))
            values.append(result)
        pivot = next(i for i, value in enumerate(values) if knonzero(value))
        pivot_inverse = kinv(values[pivot])
        answer = []
        source_indices = []
        for j, column in enumerate(cusp):
            if j == pivot:
                continue
            self.check()
            ratio = kmul(values[j], pivot_inverse)
            vector = {i: (value, fmpq(0)) for i, value in column.items()}
            for i, value in cusp[pivot].items():
                vector[i] = ksub(vector.get(i, kzero()), kscale(ratio, value))
            vector = {i: pair for i, pair in vector.items() if knonzero(pair)}
            assert vector
            for r in range(XI):
                residual = kzero()
                for i, pair in vector.items():
                    residual = kadd(residual, kscale(pair, self.V[2][i][0][r]))
                assert not knonzero(residual)
            residual = kzero()
            for i, pair in vector.items():
                residual = kadd(residual, kmul(pair, point_values[i]))
            assert not knonzero(residual)
            answer.append(vector)
            source_indices.append(j)
        assert len(answer) == U_DIM
        self.store(name, {"complete_fixed_branch_space_certified": True,
            "space": "H0(2H-D_cusp-P0)", "dimension": U_DIM, "degree": 523,
            "cusp_kernel": self.spec("R837-original-V2-cusp-kernel"),
            "P0_evaluation": self.spec("R837-original-V2-P0-evaluation"),
            "cusp_kernel_P0_values": [kencode(x) for x in values],
            "evaluation_pivot": pivot, "evaluation_pivot_value": kencode(values[pivot]),
            "evaluation_pivot_inverse": kencode(pivot_inverse),
            "source_cusp_kernel_columns": source_indices,
            "basis_columns": [sparse_encode(x) for x in answer],
            "all_397_by_40_cusp_equations_verified": True,
            "all_397_P0_equations_verified": True,
            "complete_dimension_from_actual_nonzero_evaluation_and_RR": True})
        return answer

    def fixed_anchor(self, basis):
        name = "R837-fixed-first-anchor"
        cached = self.cache(name)
        if cached is not None:
            return cached
        for coefficient in (1, 2, 3):
            vector = sparse_sum(((1, basis[0]), (coefficient, basis[1])))
            if len(vector) >= 2:
                break
        else:
            raise AssertionError("Two independent U basis vectors cannot hit three coordinate axes")
        integer, scale, denominator, content = primitive_sparse(vector)
        assert len(integer) >= 2
        return self.store(name, {"fixed_space": self.spec("R837-original-fixed-twenty-one-point-space"),
            "basis_combination": [{"U_index": 0, "coefficient": "1"}, {"U_index": 1, "coefficient": str(coefficient)}],
            "unscaled_sparse_coordinates": sparse_encode(vector),
            "integer_sparse_coordinates": integer_sparse_encode(integer),
            "primitive_normalization_scale": qencode(scale),
            "cleared_denominator": str(denominator), "integer_content_removed": str(content),
            "original_V2_nonzero_term_count": len(integer),
            "exact_nonzero_member_of_U": True, "not_an_old_single_recipe_product": True})

    def second_anchor(self, basis, parameter_index):
        name = "R837-second-anchor-parameter-" + str(parameter_index).zfill(5)
        cached = self.cache(name)
        if cached is not None:
            return cached
        a = parameter_value(parameter_index)
        self.check()
        power = 1
        terms = []
        for vector in basis:
            terms.append((power, vector))
            power *= a
        vector = sparse_sum(terms)
        assert vector
        integer, scale, denominator, content = primitive_sparse(vector)
        return self.store(name, {"fixed_space": self.spec("R837-original-fixed-twenty-one-point-space"),
            "parameter_index": parameter_index, "parameter": a,
            "basis_combination_rule": "sum(a**j*U_j,j=0..396)",
            "unscaled_sparse_coordinates": sparse_encode(vector),
            "integer_sparse_coordinates": integer_sparse_encode(integer),
            "primitive_normalization_scale": qencode(scale),
            "cleared_denominator": str(denominator), "integer_content_removed": str(content),
            "original_V2_nonzero_term_count": len(integer), "exact_nonzero_member_of_U": True,
            "not_an_old_single_recipe_product": len(integer) >= 2,
            "skip_single_original_V2_term": len(integer) < 2})

    def anchor_prefix(self, trial, which, anchor, anchor_spec, ell, root):
        name = anchor_scope(trial, which, ell) + "-prefix"
        cached = self.cache(name)
        if cached is not None:
            assert cached["prime"] == ell and cached["zeta_root"] == root
            assert cached["source_anchor"] == anchor_spec
            return [[int(x) for x in row] for row in cached["qY_xi_mod_prime"]]
        coordinate = integer_sparse_decode(anchor["integer_sparse_coordinates"])
        rows = [[0] * XI for unused in range(ORDERS)]
        for i, pair in coordinate.items():
            scalar = (pair[0] + root * pair[1]) % ell
            if not scalar:
                continue
            for n in range(ORDERS):
                rows[n] = [(x + scalar * y) % ell for x, y in zip(rows[n], self.V[2][i][n])]
        self.store(name, {"trial_index": trial if which == "v" else None,
            "shared_fixed_u_for_all_trials_at_this_prime": which == "u",
            "which_anchor": which, "source_anchor": anchor_spec,
            "prime": ell, "zeta_root": root, "qY_prefix_orders": ORDERS,
            "qY_xi_mod_prime": rows, "whole_prefix_zero_mod_prime": not any(x for row in rows for x in row),
            "original_power2_integer_scale": "45212176", "additional_rescaling": False,
            "all_contributing_R786_rows": [self.spec_rows[2][i] for i in sorted(coordinate)]})
        return rows

    def product_groups(self, trial, which, anchor_rows, ell, root):
        scope = anchor_scope(trial, which, ell)
        prefix_name = scope + "-prefix"
        prefix_spec = self.spec(prefix_name)
        anchor_polynomial = None
        if ell not in self.packed_V3:
            self.packed_V3[ell] = [packed(row, ell) for row in self.V[3]]
        all_rows, groups = [], []
        for first in range(0, V3, PRODUCT_BATCH):
            stop = min(V3, first + PRODUCT_BATCH)
            name = scope + "-products-" + str(first).zfill(4) + "-" + str(stop).zfill(4)
            cached = self.cache(name)
            if cached is None:
                self.check()
                if anchor_polynomial is None:
                    anchor_polynomial = packed(anchor_rows, ell)
                vectors = []
                for i in range(first, stop):
                    product = anchor_polynomial.mul_low(self.packed_V3[ell][i], STRIDE * ORDERS)
                    vectors.append(unpack_product(product, ell))
                cached = self.store(name, {"trial_index": trial if which == "v" else None,
                    "shared_fixed_u_for_all_trials_at_this_prime": which == "u", "which_anchor": which,
                    "prime": ell, "zeta_root": root, "anchor_prefix": prefix_spec,
                    "first_original_V3_index": first, "stop_original_V3_index": stop,
                    "source_original_V3_rows": self.spec_rows[3][first:stop],
                    "product_integer_scale_before_anchor_normalization": str(82 ** 10),
                    "prefix_orders": ORDERS, "xi_coordinates_per_order": XI,
                    "product_vectors_mod_prime": vectors,
                    "exact_packed_product_and_Phi41_reduction": True,
                    "old_single_recipe_products_not_recomputed": True})
            assert cached["trial_index"] == (trial if which == "v" else None) and cached["which_anchor"] == which
            assert cached["shared_fixed_u_for_all_trials_at_this_prime"] == (which == "u")
            assert cached["prime"] == ell and cached["zeta_root"] == root and cached["anchor_prefix"] == prefix_spec
            assert cached["first_original_V3_index"] == first and cached["stop_original_V3_index"] == stop
            assert cached["source_original_V3_rows"] == self.spec_rows[3][first:stop]
            vectors = cached["product_vectors_mod_prime"]
            assert len(vectors) == stop - first and all(len(v) == ORDERS * XI for v in vectors)
            all_rows.extend(vectors)
            groups.append(self.spec(name))
        assert len(all_rows) == V3
        return all_rows, groups

    def pencil_trial(self, index, basis, first_anchor):
        name = "R837-trial-" + str(index).zfill(5) + "-result"
        cached = self.cache(name)
        if cached is not None:
            if cached.get("actual_pencil_rank") is not None:
                self.last_rank = cached["actual_pencil_rank"]
            return cached
        prime_index, parameter_index = trial_pair(index)
        ell, root = self.prime(prime_index)
        second_anchor = self.second_anchor(basis, parameter_index)
        second_name = "R837-second-anchor-parameter-" + str(parameter_index).zfill(5)
        base = {"trial_index": index, "prime_index": prime_index, "parameter_index": parameter_index,
            "parameter": second_anchor["parameter"], "prime": ell, "zeta_root": root,
            "first_anchor": self.spec("R837-fixed-first-anchor"), "second_anchor": self.spec(second_name),
            "fixed_branch_pencil_certified": False,
            "geometric_upper_bound_rank": PENCIL_RANK,
            "modular_failure_does_not_assert_characteristic_zero_failure": True}
        if second_anchor["skip_single_original_V2_term"]:
            return self.store(name, dict(base, skipped_single_old_recipe=True, actual_pencil_rank=None))
        u = self.anchor_prefix(index, "u", first_anchor, base["first_anchor"], ell, root)
        v = self.anchor_prefix(index, "v", second_anchor, base["second_anchor"], ell, root)
        self.check()
        u_products, u_groups = self.product_groups(index, "u", u, ell, root)
        v_products, v_groups = self.product_groups(index, "v", v, ell, root)
        product_rows = u_products + v_products
        self.check()
        coordinates = pivots(nmod_mat(product_rows, ell))
        rank = len(coordinates)
        assert rank <= PENCIL_RANK
        self.last_rank = rank
        columns, determinant = [], None
        if rank == PENCIL_RANK:
            self.check()
            selected_coordinate_matrix = [[product_rows[j][i] for j in range(2 * V3)] for i in coordinates]
            columns = pivots(nmod_mat(selected_coordinate_matrix, ell))
            assert len(columns) == PENCIL_RANK
            minor = nmod_mat([[product_rows[j][i] for j in columns] for i in coordinates], ell)
            determinant = int(minor.det())
            assert determinant
        return self.store(name, dict(base,
            actual_pencil_rank=rank, fixed_branch_pencil_certified=rank == PENCIL_RANK,
            skipped_single_old_recipe=False, source_product_groups=u_groups + v_groups,
            matrix_shape=[ORDERS * XI, 2 * V3],
            actual_minor_coordinate_rows=coordinates, actual_minor_product_columns=columns,
            minor_determinant_mod_prime=determinant,
            complete_2760_coordinate_matrix_used=True,
            raw_xi_coordinates_not_replaced_by_one_xi_evaluation=True,
            rank1213_implies_exact_common_zero_divisor_Dcusp_plus_P0=rank == PENCIL_RANK,
            modular_failure_does_not_assert_characteristic_zero_failure=rank != PENCIL_RANK))

    def run(self):
        final_path = self.out / FINAL
        if final_path.exists():
            previous = read(final_path)
            if previous.get("complete"):
                assert previous["configuration"] == self.tag
                stage = self.cache(previous["pencil_certificate"]["file"])
                assert self.spec(previous["pencil_certificate"]["file"]) == plain(previous["pencil_certificate"])
                assert stage["fixed_branch_pencil_certified"] is True
                self.success_stage = previous["pencil_certificate"]
                self.last_rank = PENCIL_RANK
                return
        self.load_original_inputs()
        point = self.P0_evaluation()
        point2 = self.V2_point_values(point)
        basis = self.fixed_space(point2)
        first_anchor = self.fixed_anchor(basis)
        for trial in range(self.maximum_trials):
            self.check()
            answer = self.pencil_trial(trial, basis, first_anchor)
            if answer["fixed_branch_pencil_certified"]:
                self.success_stage = self.spec("R837-trial-" + str(trial).zfill(5) + "-result")
                return
        raise TrialLimit("The configured finite pencil-trial limit was reached without a rank1213 certificate")

    def finish(self, completed, stop_reason, error):
        files = []
        for path in sorted(self.out.glob(PREFIX + "*.json.gz")):
            if path.name == INVENTORY:
                continue
            value = read(path)
            assert value["complete"] is True and value["configuration"] == self.tag
            files.append(file_spec(path))
        save(self.out / INVENTORY, {"result": RESULT, "configuration": self.tag, "complete": True,
            "files": files, "completed_stage_count": len(files),
            "only_complete_current_source_stages_listed": True})
        point = self.cache("R837-original-P0-evaluation")
        space = self.cache("R837-original-fixed-twenty-one-point-space")
        flags = {
            "original_P0_evaluation_certified": point is not None and point["original_P0_evaluation_certified"] is True,
            "complete_fixed_branch_space_certified": space is not None and space["complete_fixed_branch_space_certified"] is True,
            "fixed_branch_pencil_certified": self.success_stage is not None,
        }
        complete = bool(completed and all(flags.values()) and self.last_rank == PENCIL_RANK)
        trials = [row for row in files if re.fullmatch(r"R837-trial-[0-9]+-result\.json\.gz", row["file"])]
        final = {"result": RESULT, "configuration": self.tag, "complete": complete, "p": 41, **flags,
            "actual_pencil_rank": self.last_rank,
            "original_P0_evaluation": self.spec("R837-original-P0-evaluation") if point is not None else None,
            "fixed_branch_space": self.spec("R837-original-fixed-twenty-one-point-space") if space is not None else None,
            "pencil_certificate": self.success_stage,
            "fixed_branch_divisor": "20 original cusps plus P0=phi(c0)",
            "fixed_branch_degree": 21, "fixed_space_dimension": U_DIM if space is not None else None,
            "pencil_domain_powers": [2, 3], "pencil_target_power": 5,
            "original_scales_preserved": True,
            "complete_trial_results": trials, "completed_trial_count": len(trials),
            "requested_maximum_pencil_trials": self.maximum_trials,
            "stage_manifest": file_spec(self.out / INVENTORY),
            "stop_reason": stop_reason, "error": error,
            "old_CM_torsion_trace_or_Fourier_arithmetic_recomputed": False,
            "actual_D_or_eta_or_height_computed": False,
            "seconds": time.monotonic() - self.started}
        save(self.out / FINAL, final)
        return final


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--budget-minutes", type=float, required=True)
    args = parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("All new R837 mathematics belongs to the public repository's GitHub Actions.")
    started = time.monotonic()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    job, final, error = None, None, None
    status, stop_reason = 1, "initialization_incomplete"
    try:
        job = Job(args)
        job.run()
        status, stop_reason = 0, "certified_fixed_branch_pencil"
    except BudgetStop as exc:
        status, stop_reason, error = 124, "budget_stop", str(exc)
    except TrialLimit as exc:
        status, stop_reason, error = 2, "pencil_trial_limit", str(exc)
    except BaseException as exc:
        status, stop_reason, error = 1, "exception", type(exc).__name__ + ": " + str(exc)
        traceback.print_exc()
    if job is not None:
        try:
            final = job.finish(status == 0, stop_reason, error)
        except BaseException as exc:
            status, stop_reason, error = 1, "finalization_exception", type(exc).__name__ + ": " + str(exc)
            traceback.print_exc()
    complete = status == 0 and final is not None and final["complete"] is True
    receipt = {"result": RESULT, "p": 41, "source_sha256": sha(__file__),
        "complete": complete, "process_exit_code": status, "stop_reason": stop_reason, "error": error,
        "certificate_sha256": sha(out / FINAL) if final is not None else None,
        "original_P0_evaluation_certified": bool(final and final["original_P0_evaluation_certified"]),
        "complete_fixed_branch_space_certified": bool(final and final["complete_fixed_branch_space_certified"]),
        "fixed_branch_pencil_certified": bool(final and final["fixed_branch_pencil_certified"]),
        "actual_pencil_rank": final["actual_pencil_rank"] if final is not None else None,
        "stage_manifest": final["stage_manifest"] if final is not None else None,
        "seconds": time.monotonic() - started}
    save(out / "core-receipt.json", receipt)
    print("R837_CORE_RECEIPT=" + json.dumps(receipt, sort_keys=True), flush=True)
    return status


if __name__ == "__main__":
    sys.set_int_max_str_digits(0)
    sys.exit(main())
