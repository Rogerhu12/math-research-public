#!/usr/bin/env python3
"""R806: one primitive multiplier in the original normal affine basis."""
import argparse
import gzip
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpq, fmpz, fmpz_mat, fmpz_poly, nmod_mat

RESULT = "R806-original-primitive-multiplication"
FINAL = "p41-original-primitive-multiplication-certificate.json"
P, LEVEL, CYC, REAL, COUNT = 41, 82, 40, 20, 41
DIM, ROWS, FREE = 690, 820, 272
DIMS = {1: 146, 2: 418, 3: 690}
EPS = [0]+[1]*144+[2]*127
R805_CORE_SHA = "730a7d8f51d76d1153386c63f2e082285ada4573a2baf8d87d1825d3ce75b420"
SEARCH_DEGREE_BOUND = 36458
FAMILY_PARAMETER_BOUND = 143*(272*271//2)
CANDIDATE_COUNT = 287+FAMILY_PARAMETER_BOUND
LABELS = {"R805", "R786"}


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
    temporary = path.with_name(path.name+".tmp")
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        with temporary.open("wb") as stream:
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb", mtime=0, compresslevel=2) as gz:
                gz.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def plain_spec(spec):
    return {key: spec[key] for key in ("file", "bytes", "sha256")}


def packed(rows, stride):
    values = [0]*(stride*len(rows))
    for n, row in enumerate(rows):
        values[n*stride:n*stride+len(row)] = row
    return fmpz_poly(values)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def same_producer(left, right):
    for key in ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256", "certificate_name"):
        assert str(left[key]) == str(right[key]), ("producer identity", key)
    certificate = left["certificate_name"]
    assert left["files"][certificate] == right["files"][certificate]
    for name in set(left["files"]) & set(right["files"]):
        assert left["files"][name] == right["files"][name]


def pairs(value):
    return [str(value.numer()), str(value.denom())]


def dq(value):
    assert len(value) == 2 and int(value[1]) > 0
    return fmpq(int(value[0]), int(value[1]))


def matrix_rows(matrix, strings=False):
    convert = str if strings else int
    return [[convert(matrix[i, j]) for j in range(matrix.ncols())] for i in range(matrix.nrows())]


def rational_reconstruct(value, modulus):
    value %= modulus
    if value == 0:
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


class Retained:
    def __init__(self, root, label, spec):
        self.label, self.spec, self.directory = label, spec, Path(root)/label
        path = self.directory/"full-outputs-manifest.json"
        assert sha(path) == spec["manifest_sha256"]
        manifest = read(path)
        assert manifest["result"] == spec["result"]
        self.files = {row["file"]: row for row in manifest["files"]}
        assert len(self.files) == len(manifest["files"])
        self.checked = set()
        run, core, initial = (self.raw(name) for name in
            ("run-receipt.json", "core-receipt.json", "public-actions-input.json"))
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert str(run["workflow_run_id"]) == str(spec["run_id"])
        assert run["result"] == core["result"] == initial["result"] == spec["result"]
        assert run["source_commit"] == initial["source_commit"] == spec["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["core_sha256"] == spec["core_sha256"]
        assert initial["job"]["core_sha256"] == spec["core_sha256"]
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        assert core["complete"] is True and core["source_sha256"] == spec["core_sha256"]
        name = spec["certificate_name"]
        assert core["certificate_sha256"] == self.files[name]["sha256"] == spec["files"][name]
        self.certificate = self.raw(name)
        assert self.certificate["complete"] is True and self.certificate["result"] == spec["result"]
        self.initial = initial
        self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == spec["core_sha256"]
        assert self.tag["python_flint"] == "0.9.0"

    def raw(self, name, digest=None):
        assert Path(name).name == name
        spec = self.files[name]
        if digest is not None:
            assert spec["sha256"] == digest
        if name in self.spec["files"]:
            assert spec["sha256"] == self.spec["files"][name]
        path = self.directory/name
        if name not in self.checked:
            assert path.stat().st_size == spec["bytes"] and sha(path) == spec["sha256"]
            self.checked.add(name)
        return read(path)

    def stage(self, name, digest=None):
        value = self.raw(name, digest)
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def source(self, name):
        return dict(plain_spec(self.files[name]), producer=self.label)

    def cert_stage(self, name):
        entries = {row["file"]: row for row in self.certificate["stages"]}
        assert plain_spec(entries[name]) == plain_spec(self.files[name])
        return self.stage(name, entries[name]["sha256"])


class BudgetStop(RuntimeError):
    pass


def S_position(index):
    if index < 4:
        return 0, index
    if index < 436:
        return 1+(index-4)//3, (index-4) % 3
    return 145+(index-436)//2, (index-436) % 2


def modular_rows(matrix, prime):
    return nmod_mat([[int(matrix[i, j]) % prime for j in range(matrix.ncols())]
                     for i in range(matrix.nrows())], prime)


class Job:
    def __init__(self, args):
        self.args, self.out, self.started = args, args.output, time.monotonic()
        self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        assert self.item["producer_inputs_pending"] is False
        assert self.item["result"] == RESULT and self.item["p"] == P
        assert self.item["core_sha256"] == sha(__file__)
        assert sha(args.proof) == self.item["R805_proof_sha256"]
        assert sha(args.method) == self.item["R806_method_sha256"]
        assert flint.__version__ == "0.9.0"
        assert self.item["qY_count"] == COUNT
        assert self.item["requested_stage"] == "primitive_multiplication_and_cyclic_certificate"
        assert self.item["auxiliary_prime_start"] == 1000000007
        assert self.item["dixon_group_columns"] == 8
        assert self.item["reconstruct_every_digits"] == 8
        assert set(self.item["retained_artifacts"]) == LABELS
        self.inputs = {label: Retained(args.retained, label, self.item["retained_artifacts"][label])
                       for label in ("R805", "R786")}
        self.r805, self.r786 = self.inputs["R805"], self.inputs["R786"]
        assert self.r805.spec["result"] == "R805-original-affine-pencil-free-basis"
        assert self.r805.spec["core_sha256"] == R805_CORE_SHA
        same_producer(self.r805.tag["retained_artifacts"]["R786"], self.r786.spec)
        same_producer(self.r805.initial["job"]["retained_artifacts"]["R786"], self.r786.spec)
        assert self.r805.tag["R805_proof_sha256"] == sha(args.proof)
        cert = self.r805.certificate
        assert cert["completed_scope"] == "pencil_and_graded_free_basis"
        assert cert["affine_free_module_rank"] == FREE
        assert cert["graded_free_basis_degrees"] == [1, 144, 127]
        assert cert["degree3_S_basis_dimension"] == DIM
        assert cert["degree3_S_prefix_count"] == COUNT
        assert cert["degree3_S_full_real_coordinates"] == ROWS
        assert cert["all_S_rows_original_and_real_coordinates_verified"] is True
        assert cert["original_82_scales_preserved"] is True
        spec = cert["stage_manifest"]
        assert plain_spec(spec) == plain_spec(self.r805.files[spec["file"]])
        inventory805 = self.r805.stage(spec["file"], spec["sha256"])
        self.entries805 = {row["file"]: plain_spec(row) for row in inventory805["files"]}
        assert len(self.entries805) == len(inventory805["files"])
        self.pencil = self.stage805(cert["pencil_stage"])
        self.free = self.stage805(cert["graded_free_basis_stage"])
        self.S_index = self.stage805(cert["S_basis_index"])
        self.alias805 = self.stage805(cert["alias_index"])
        self.old_minor = self.stage805(self.S_index["short_minor"])
        self.I = self.old_minor["row_indices"]
        assert len(self.I) == DIM and self.I == sorted(set(self.I))
        assert all(0 <= i < ROWS for i in self.I)
        assert self.old_minor["column_indices"] == list(range(DIM))
        assert self.old_minor["actual_rank"] == DIM
        assert self.old_minor["full_coordinate_rows"] == ROWS
        assert self.old_minor["actual_determinant_mod_prime"] % self.old_minor["prime"]
        assert self.old_minor["all_source_rows"] == self.S_index["basis_rows"]
        assert self.free["pencil_stage"] == cert["pencil_stage"]
        assert self.free["degree_distribution"] == [1, 144, 127]
        assert self.free["degree1_original_indices"] == list(range(2, 146))
        assert len(self.free["degree2_original_indices"]) == 127
        assert self.free["degree2_original_indices"] == sorted(set(self.free["degree2_original_indices"]))
        assert all(0 <= i < 418 for i in self.free["degree2_original_indices"])
        assert self.pencil["actual_rank"] == 690
        assert self.pencil["basepoint_free_certified_by_actual_unit_minor"] is True
        assert self.S_index["integer_scale"] == str(LEVEL**6)
        assert self.S_index["all_original_and_real_coordinates_verified"] is True
        assert self.S_index["not_old_R786_V3_coefficient_basis"] is True
        assert self.S_index["dimension"] == len(self.S_index["basis_rows"]) == DIM
        assert self.r786.certificate["exact_K_basis_prefix_bound_qY"] == 128
        assert self.r786.certificate["basis_in_original_R775_saved_order"] is True
        spec = self.r786.certificate["stages_manifest"]
        assert plain_spec(spec) == plain_spec(self.r786.files[spec["file"]])
        inventory786 = self.r786.stage(spec["file"], spec["sha256"])
        self.entries786 = {row["file"]: plain_spec(row) for row in inventory786["files"]}
        assert len(self.entries786) == len(inventory786["files"])
        self.tag = {"result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "p": P, "R805_proof_sha256": sha(args.proof), "R806_method_sha256": sha(args.method),
            "retained_artifacts": self.item["retained_artifacts"],
            "qY_count": COUNT, "full_coordinate_rows": ROWS, "S_basis_dimension": DIM,
            "normal_affine_basis_rank": FREE, "normal_affine_basis_degrees": EPS,
            "original_R805_S_basis_index": cert["S_basis_index"],
            "original_R805_short_minor": self.S_index["short_minor"],
            "coordinate_row_indices": self.I, "basis_integer_scale": str(LEVEL**6),
            "original_tau_index": 0, "actual_sigma_integer_n": self.pencil["n"],
            "auxiliary_prime_start": self.item["auxiliary_prime_start"],
            "dixon_group_columns": self.item["dixon_group_columns"],
            "reconstruct_every_digits": self.item["reconstruct_every_digits"],
            "candidate_order": "e2; each e_j,e2+e_j for j=3..145; then sum(a^(i-1)*b_i),a=1..D",
            "family_parameter_bound": FAMILY_PARAMETER_BOUND,
            "cyclic_determinant_degree_bound": SEARCH_DEGREE_BOUND,
            "search_order": "diagonals candidate_index+prime_index+integer_z0; distinct residues only",
            "matrix_convention": "column input E_a, row output E_b; M_ba(z)",
            "source_alias_policy": "R786 original product; R805 complete product; new R806 product",
            "old_R805_ranks_selection_or_saved_products_recomputed": False,
            "characteristic_zero_Krylov_matrix_or_inverse_computed": False}
        self.sources, self.recipes, self.leaves, self.aliases = {}, {}, {}, {}
        self.old_products, self.product_cache, self.old_cache = {}, {}, {}
        self.C, self.A, self.chart_spec = None, None, None
        self.prime_values, self.solver_cache = [], {}
        self.accepted = None
        T = fmpz_poly([0, 1])
        self.chebyshev = [fmpz_poly([2]), T]
        for _ in range(2, 21):
            self.chebyshev.append(T*self.chebyshev[-1]-self.chebyshev[-2])
        self.gt = fmpz_poly([1])
        for poly in self.chebyshev[1:]:
            self.gt += poly
        self.load_aliases()

    def stage805(self, spec):
        assert plain_spec(spec) == self.entries805[spec["file"]]
        assert plain_spec(spec) == plain_spec(self.r805.files[spec["file"]])
        return self.r805.stage(spec["file"], spec["sha256"])

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes-45:
            raise BudgetStop("Complete products, modular screens, rational groups and latest exact lifts retained.")

    def path(self, name):
        assert name.startswith("R806-") and Path(name).name == name
        return self.out/(name if name.endswith(".json.gz") else name+".json.gz")

    def cached(self, name, current=False):
        path = self.path(name)
        if not path.exists():
            return None
        data = read(path)
        assert data["configuration"] == self.tag
        assert data["complete"] is (not current)
        if current:
            assert name.endswith("-dixon-current")
            assert data["complete_coordinates_claimed"] is False
        return data

    def store(self, name, value, current=False):
        assert not current or name.endswith("-dixon-current")
        save(self.path(name), dict(value, complete=not current, configuration=self.tag))
        return file_spec(self.path(name))

    def load_aliases(self):
        rows = self.alias805["rows"]
        assert len(rows) == 1254 and self.alias805["source_powers"] == [1, 2, 3]
        for position, row in enumerate(rows):
            power, index = row["power"], row["index"]
            assert power in DIMS and 0 <= index < DIMS[power]
            assert (power, index) not in self.sources
            name = "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"
            source = self.r786.source(name)
            assert row["source"] == source
            assert plain_spec(source) == self.entries786[name]
            leaves = tuple(row["sorted_M2_leaf_indices"])
            assert len(leaves) == power and leaves == tuple(sorted(leaves))
            assert all(0 <= i < 146 for i in leaves)
            recipe = row["recipe"]
            if power == 1:
                assert leaves == (index,) and recipe["kind"] == "det_semilinear_E1_pair_trace"
            else:
                assert recipe["kind"] == "product"
                lp, li, rp, ri = (recipe[key] for key in
                    ("left_power", "left_index", "right_power", "right_index"))
                assert lp+rp == power and lp < power and rp < power
                assert leaves == tuple(sorted(self.leaves[lp, li]+self.leaves[rp, ri]))
            self.sources[power, index] = source
            self.recipes[power, index] = recipe
            self.leaves[power, index] = leaves
            self.aliases.setdefault(leaves, (power, index))
        assert set(self.sources) == {(r, i) for r in DIMS for i in range(DIMS[r])}
        for name, spec in self.entries805.items():
            prefix, suffix = "R805-new-monomial-", ".json.gz"
            if name.startswith(prefix) and name.endswith(suffix):
                leaves = tuple(int(x) for x in name[len(prefix):-len(suffix)].split("-"))
                assert 2 <= len(leaves) <= 3 and leaves == tuple(sorted(leaves))
                assert leaves not in self.old_products
                self.old_products[leaves] = spec

    def real_rows(self, rows):
        answer = []
        for n, row in enumerate(rows):
            cyclic = [0]*P
            for r, value in enumerate(row):
                cyclic[(r+10*n) % P] += int(value)
            reduced = [value-cyclic[40] for value in cyclic[:40]]+[0]
            assert all(reduced[r] == reduced[P-r] for r in range(1, 21))
            poly = fmpz_poly([reduced[0]])
            for r in range(1, 21):
                poly += self.chebyshev[r]*reduced[r]
            poly %= self.gt
            answer.append([int(poly[r]) for r in range(REAL)])
        return answer

    def original(self, power, index):
        key = power, index
        if key not in self.old_cache:
            source = self.sources[key]
            data = self.r786.stage(source["file"], source["sha256"])
            assert data["weight"] == 2*power and data["bound_qY"] == 128
            assert data["integer_scale"] == str(LEVEL**(2*power))
            assert data["recipe"] == self.recipes[key]
            assert data["original_R775_finite_coefficients_verified"] is True
            raw = data["integer_qY_xi_coefficients"]
            assert len(raw) == 129 and all(len(row) == CYC for row in raw)
            raw = [[int(x) for x in row] for row in raw[:COUNT]]
            self.old_cache[key] = {"q": raw, "v": self.real_rows(raw),
                "source": source, "integer_scale": data["integer_scale"], "leaves": self.leaves[key]}
        return self.old_cache[key]

    def multiply(self, left, right):
        qproduct = packed(left["q"], 79).mul_low(packed(right["q"], 79), 79*COUNT)
        raw = []
        for n in range(COUNT):
            cyclic = [0]*P
            for r in range(79):
                cyclic[r % P] += int(qproduct[79*n+r])
            raw.append([cyclic[r]-cyclic[40] for r in range(CYC)])
        real = self.real_rows(raw)
        vproduct = packed(left["v"], 39).mul_low(packed(right["v"], 39), 39*COUNT)
        direct = []
        for n in range(COUNT):
            poly = fmpz_poly([vproduct[39*n+r] for r in range(39)]) % self.gt
            direct.append([int(poly[r]) for r in range(REAL)])
        assert real == direct
        return raw, real

    def monomial(self, leaves):
        leaves = tuple(sorted(leaves))
        assert 1 <= len(leaves) <= 3
        if leaves in self.product_cache:
            return self.product_cache[leaves]
        if leaves in self.aliases:
            answer = self.original(*self.aliases[leaves])
            self.product_cache[leaves] = answer
            return answer
        name = "R806-new-monomial-"+"-".join(str(i).zfill(3) for i in leaves)
        if leaves in self.old_products:
            spec = self.old_products[leaves]
            data = self.stage805(spec)
            source = self.r805.source(spec["file"])
        else:
            data = self.cached(name)
            if data is None:
                self.budget()
                if len(leaves) == 2:
                    left, right = self.monomial(leaves[:1]), self.monomial(leaves[1:])
                else:
                    def known(pair):
                        return pair in self.aliases or pair in self.old_products or \
                            self.path("R806-new-monomial-"+"-".join(str(i).zfill(3) for i in pair)).exists()
                    pair = next((tuple(sorted(pair)) for pair in itertools.combinations(leaves, 2)
                                 if known(tuple(sorted(pair)))), tuple(leaves[:2]))
                    rest = list(leaves)
                    for i in pair:
                        rest.remove(i)
                    left, right = self.monomial(pair), self.monomial(tuple(rest))
                raw, real = self.multiply(left, right)
                self.store(name, {"sorted_M2_leaf_indices": list(leaves), "weight": 2*len(leaves),
                    "integer_scale": str(LEVEL**(2*len(leaves))), "qY_count": COUNT,
                    "integer_qY_xi_coefficients": [[str(x) for x in row] for row in raw],
                    "integer_v_t_coefficients": [[str(x) for x in row] for row in real],
                    "factor_sources": [left["source"], right["source"]],
                    "all_original_and_real_coordinates_verified": True,
                    "old_recipe_alias_exists": False, "old_R805_product_exists": False,
                    "old_saved_product_recomputed": False})
                data = self.cached(name)
            assert data["old_R805_product_exists"] is False
            source = dict(file_spec(self.path(name)), producer="R806")
        assert data["sorted_M2_leaf_indices"] == list(leaves)
        assert data["qY_count"] == COUNT and data["old_recipe_alias_exists"] is False
        assert data["integer_scale"] == str(LEVEL**(2*len(leaves)))
        assert data["all_original_and_real_coordinates_verified"] is True
        answer = {"q": [[int(x) for x in row] for row in data["integer_qY_xi_coefficients"]],
            "v": [[int(x) for x in row] for row in data["integer_v_t_coefficients"]],
            "source": source, "integer_scale": data["integer_scale"], "leaves": leaves}
        assert len(answer["q"]) == len(answer["v"]) == COUNT
        assert all(len(row) == CYC for row in answer["q"])
        assert all(len(row) == REAL for row in answer["v"])
        self.product_cache[leaves] = answer
        return answer

    def load_chart(self):
        if self.C is not None:
            return
        columns = []
        for index, spec in enumerate(self.S_index["basis_rows"]):
            self.budget()
            assert spec["index"] == index
            row = self.stage805(spec)
            assert row["index"] == index and row["recipe"] == spec["recipe"]
            assert row["integer_scale"] == str(LEVEL**6)
            assert row["qY_count"] == COUNT
            assert row["free_basis_stage"] == self.r805.certificate["graded_free_basis_stage"]
            assert row["all_original_and_real_coordinates_verified"] is True
            assert row["V3_membership_has_original_product_generation_witness"] is True
            real = row["integer_v_t_coefficients"]
            assert len(real) == COUNT and all(len(line) == REAL for line in real)
            columns.append([int(x) for line in real for x in line])
        self.C = fmpz_mat(columns).transpose()
        self.A = fmpz_mat([[int(self.C[i, j]) for j in range(DIM)] for i in self.I])
        name = "R806-original-input-and-coordinate-chart"
        payload = {"original_R805_alias_index": self.r805.certificate["alias_index"],
            "original_R805_pencil": self.r805.certificate["pencil_stage"],
            "original_R805_free_basis": self.r805.certificate["graded_free_basis_stage"],
            "original_R805_S_basis_index": self.r805.certificate["S_basis_index"],
            "original_R805_short_minor": self.S_index["short_minor"],
            "all_original_S_basis_rows": self.S_index["basis_rows"],
            "coordinate_row_indices": self.I, "full_rows": ROWS, "columns": DIM,
            "integer_scale": str(LEVEL**6), "normal_affine_basis_degrees": EPS,
            "old_R805_ranks_selection_or_saved_products_recomputed": False,
            "original_coefficient_basis_changed": False}
        old = self.cached(name)
        if old is None:
            self.store(name, payload)
        else:
            for key, value in payload.items():
                assert old[key] == value
        self.chart_spec = file_spec(self.path(name))

    def candidate_definition(self, index):
        assert 0 <= index < CANDIDATE_COUNT
        name = "R806-candidate-"+str(index).zfill(10)+"-definition"
        old = self.cached(name)
        if old is None:
            values = [0]*146
            if index == 0:
                values[2] = 1
                recipe = {"kind": "original_M2", "index": 2}
            elif index <= 286:
                j = 3+(index-1)//2
                values[j] = 1
                if index % 2 == 0:
                    values[2] = 1
                    recipe = {"kind": "sum_two_original_M2", "indices": [2, j]}
                else:
                    recipe = {"kind": "original_M2", "index": j}
            else:
                parameter = index-286
                assert 1 <= parameter <= FAMILY_PARAMETER_BOUND
                value = 1
                for j in range(2, 146):
                    values[j] = value
                    value *= parameter
                recipe = {"kind": "original_V1_one_parameter_family", "a": parameter,
                          "equation": "sum a^(i-1)*b_i, i=1..144"}
            assert values[0] == values[1] == 0 and any(values)
            self.store(name, {"candidate_index": index, "recipe": recipe,
                "w0_original_M2_integer_coordinates": [str(x) for x in values],
                "original_integer_scale": str(LEVEL**2),
                "w_definition": "w=w0/tau, tau=original integer-scaled e0",
                "membership_in_original_V1_by_generation": True,
                "normal_affine_basis_preserved": True})
            old = self.cached(name)
        assert old["candidate_index"] == index
        values = [int(x) for x in old["w0_original_M2_integer_coordinates"]]
        assert len(values) == 146 and values[0] == values[1] == 0 and any(values)
        return old, file_spec(self.path(name)), values

    def candidate_products(self, candidate):
        definition, definition_spec, coordinates = self.candidate_definition(candidate)
        index_name = "R806-candidate-"+str(candidate).zfill(10)+"-product-index"
        complete_index = self.cached(index_name)
        if complete_index is not None:
            assert complete_index["candidate_index"] == candidate
            assert complete_index["candidate_definition"] == definition_spec
            assert complete_index["column_count"] == FREE and complete_index["full_coordinate_rows"] == ROWS
            assert complete_index["integer_scale"] == str(LEVEL**6)
            specs = complete_index["product_columns"]
            assert len(specs) == FREE and [row["column"] for row in specs] == list(range(FREE))
            return file_spec(self.path(index_name)), specs
        specs = []
        for column in range(FREE):
            self.budget()
            if column == 0:
                base = (0, 0)
            elif column <= 144:
                base = (0, column+1)
            else:
                base = self.leaves[2, self.free["degree2_original_indices"][column-145]]
            assert len(base) == 2
            terms = [(tuple(sorted(base+(index,))), value)
                     for index, value in enumerate(coordinates) if value]
            name = "R806-candidate-"+str(candidate).zfill(10)+"-product-"+str(column).zfill(3)
            old = self.cached(name)
            encoded = [{"sorted_M2_leaf_indices": list(leaves), "integer_coefficient": str(value)}
                       for leaves, value in terms]
            if old is None:
                raw, real, sources = [[0]*CYC for _ in range(COUNT)], [[0]*REAL for _ in range(COUNT)], []
                for leaves, coefficient in terms:
                    self.budget()
                    product = self.monomial(leaves)
                    assert product["integer_scale"] == str(LEVEL**6)
                    sources.append({"sorted_M2_leaf_indices": list(leaves),
                                    "coefficient": str(coefficient), "source": product["source"]})
                    for order in range(COUNT):
                        for k in range(CYC):
                            raw[order][k] += coefficient*product["q"][order][k]
                        for k in range(REAL):
                            real[order][k] += coefficient*product["v"][order][k]
                assert real == self.real_rows(raw)
                self.store(name, {"candidate_index": candidate, "column": column,
                    "input_normal_basis_degree": EPS[column], "candidate_definition": definition_spec,
                    "equation": "P_a=tau^(2-epsilon_a)*w0*d_a",
                    "expanded_integer_monomials": encoded, "monomial_sources": sources,
                    "integer_scale": str(LEVEL**6), "qY_count": COUNT,
                    "integer_qY_xi_coefficients": [[str(x) for x in row] for row in raw],
                    "integer_v_t_coefficients": [[str(x) for x in row] for row in real],
                    "all_original_and_real_coordinates_verified": True,
                    "membership_in_original_V3_by_generation": True,
                    "old_saved_products_recomputed": False})
                old = self.cached(name)
            assert old["candidate_index"] == candidate and old["column"] == column
            assert old["candidate_definition"] == definition_spec
            assert old["input_normal_basis_degree"] == EPS[column]
            assert old["expanded_integer_monomials"] == encoded
            assert old["integer_scale"] == str(LEVEL**6) and old["qY_count"] == COUNT
            assert old["all_original_and_real_coordinates_verified"] is True
            assert old["membership_in_original_V3_by_generation"] is True
            specs.append(dict(file_spec(self.path(name)), column=column))
        name = "R806-candidate-"+str(candidate).zfill(10)+"-product-index"
        payload = {"candidate_index": candidate, "candidate_definition": definition_spec,
            "product_columns": specs, "column_count": FREE, "full_coordinate_rows": ROWS,
            "integer_scale": str(LEVEL**6), "all_original_generation_witnesses_present": True}
        old = self.cached(name)
        if old is None:
            self.store(name, payload)
        else:
            for key, value in payload.items():
                assert old[key] == value
        return file_spec(self.path(name)), specs

    def targets(self, candidate, columns=None):
        if columns is None:
            columns = list(range(FREE))
        index_spec, specs = self.candidate_products(candidate)
        vectors, selected_specs = [], []
        for column in columns:
            assert file_spec(self.path(specs[column]["file"])) == plain_spec(specs[column])
            data = self.cached(specs[column]["file"])
            assert data["column"] == column and data["candidate_index"] == candidate
            values = data["integer_v_t_coefficients"]
            assert len(values) == COUNT and all(len(row) == REAL for row in values)
            vectors.append([int(x) for row in values for x in row])
            selected_specs.append(specs[column])
        return fmpz_mat(vectors).transpose(), index_spec, selected_specs

    def prime_at(self, index):
        while len(self.prime_values) <= index:
            value = self.item["auxiliary_prime_start"] if not self.prime_values else self.prime_values[-1]+2
            while not fmpz(value).is_prime():
                value += 2
            assert value < 2**63, "Use an arbitrary-modulus matrix backend if a future continuation reaches this bound."
            self.prime_values.append(value)
        return self.prime_values[index]

    def solver(self, prime):
        if prime in self.solver_cache:
            return self.solver_cache[prime]
        self.load_chart()
        rejected = "R806-prime-"+str(prime)+"-rejected-fixed-minor"
        if self.cached(rejected) is not None:
            return None
        name = "R806-prime-"+str(prime)+"-fixed-minor-inverse"
        data = self.cached(name)
        if data is None:
            self.budget()
            assert fmpz(prime).is_prime() and LEVEL % prime
            square = modular_rows(self.A, prime)
            try:
                inverse = square.inv()
            except ZeroDivisionError:
                self.store(rejected, {"prime": prime, "original_coordinate_chart": self.chart_spec,
                    "coordinate_row_indices": self.I, "fixed_minor_singular_mod_prime": True,
                    "characteristic_zero_rank_loss_claimed": False,
                    "old_row_selection_or_R805_rank_recomputed": False})
                return None
            identity = nmod_mat([[int(i == j) for j in range(DIM)] for i in range(DIM)], prime)
            assert square*inverse == identity
            self.store(name, {"prime": prime, "prime_proved": True,
                "original_coordinate_chart": self.chart_spec,
                "original_R805_short_minor": self.S_index["short_minor"],
                "coordinate_row_indices": self.I, "fixed_minor_dimension": DIM,
                "inverse_mod_prime": matrix_rows(inverse),
                "modular_inverse_identity_verified": True,
                "new_row_selection_or_old_R805_rank_recomputed": False,
                "characteristic_zero_inverse_matrix_formed": False})
            data = self.cached(name)
        assert data["prime"] == prime and data["prime_proved"] is True
        assert data["original_coordinate_chart"] == self.chart_spec
        assert data["coordinate_row_indices"] == self.I
        assert data["modular_inverse_identity_verified"] is True
        inverse = nmod_mat(data["inverse_mod_prime"], prime)
        assert inverse.nrows() == inverse.ncols() == DIM
        answer = {"prime": prime, "inverse": inverse, "spec": file_spec(self.path(name)),
                  "full_modular_matrix": modular_rows(self.C, prime)}
        # The immutable inverse stage survives; only one prime occupies RAM.
        self.solver_cache = {prime: answer}
        return answer

    @staticmethod
    def weighted_support(coordinates):
        assert len(coordinates) == DIM and all(len(row) == FREE for row in coordinates)
        for row in range(DIM):
            output, degree = S_position(row)
            for column in range(FREE):
                if degree > 1+EPS[column]-EPS[output]:
                    assert not coordinates[row][column], (row, column, "weighted multiplication support")

    def modular_multiplier(self, candidate, prime, solver):
        name = "R806-candidate-"+str(candidate).zfill(10)+"-prime-"+str(prime)+"-modular-multiplier"
        data = self.cached(name)
        if data is None:
            target, product_index, product_specs = self.targets(candidate)
            self.budget()
            selected = nmod_mat([[int(target[i, j]) % prime for j in range(FREE)] for i in self.I], prime)
            coordinates = solver["inverse"]*selected
            assert solver["full_modular_matrix"]*coordinates == modular_rows(target, prime)
            rows = matrix_rows(coordinates)
            self.weighted_support(rows)
            definition, definition_spec, _ = self.candidate_definition(candidate)
            self.store(name, {"candidate_index": candidate, "prime": prime,
                "candidate_definition": definition_spec,
                "original_coordinate_chart": self.chart_spec,
                "fixed_minor_inverse": solver["spec"],
                "product_index": product_index, "product_columns": product_specs,
                "coordinates_mod_prime": rows,
                "integer_scale": str(LEVEL**6), "full_coordinate_rows": ROWS,
                "coordinate_dimension": DIM, "input_normal_basis_columns": FREE,
                "all820_modular_equations_verified": True,
                "weighted_polynomial_support_verified": True,
                "genuine_characteristic_zero_V3_membership_by_generation": True,
                "characteristic_zero_coordinates_recovered": False})
            data = self.cached(name)
        assert data["candidate_index"] == candidate and data["prime"] == prime
        assert data["fixed_minor_inverse"] == solver["spec"]
        assert data["original_coordinate_chart"] == self.chart_spec
        assert data["all820_modular_equations_verified"] is True
        assert data["weighted_polynomial_support_verified"] is True
        rows = data["coordinates_mod_prime"]
        assert len(rows) == DIM and all(len(row) == FREE for row in rows)
        assert all(0 <= int(x) < prime for row in rows for x in row)
        return data, file_spec(self.path(name))

    @staticmethod
    def specialize_modular(coordinates, prime, z0):
        matrix = [[0]*FREE for _ in range(FREE)]
        powers = [pow(z0, degree, prime) for degree in range(4)]
        for row in range(DIM):
            output, degree = S_position(row)
            for column in range(FREE):
                matrix[output][column] = (matrix[output][column]+
                    int(coordinates[row][column])*powers[degree]) % prime
        return nmod_mat(matrix, prime)

    def cyclic(self, candidate, prime, z0, solver):
        assert 0 <= z0 < prime and z0 <= SEARCH_DEGREE_BOUND
        name = "R806-candidate-"+str(candidate).zfill(10)+"-prime-"+str(prime)+"-z-"+str(z0)+"-cyclic"
        data = self.cached(name)
        if data is None:
            modular, modular_spec = self.modular_multiplier(candidate, prime, solver)
            self.budget()
            matrix = self.specialize_modular(modular["coordinates_mod_prime"], prime, z0)
            vector = nmod_mat([[int(i == 0)] for i in range(FREE)], prime)
            columns = []
            for exponent in range(FREE):
                self.budget()
                columns.append([int(vector[i, 0]) for i in range(FREE)])
                if exponent+1 < FREE:
                    vector = matrix*vector
            krylov = nmod_mat(columns, prime).transpose()
            determinant = int(krylov.det())
            if determinant:
                rank = FREE
            else:
                _, rank = krylov.rref()
                assert rank < FREE
            value = {"candidate_index": candidate, "prime": prime, "z0": z0,
                "source_modular_multiplier": modular_spec,
                "actual_cyclic_rank": rank, "actual_determinant_mod_prime": determinant,
                "full_krylov_columns_computed": FREE,
                "initial_vector": "1 in original normal affine basis",
                "primitive_generator_certified_by_actual_minor": bool(determinant),
                "characteristic_zero_nonprimitive_claimed_from_failure": False,
                "normal_integral_basis_preserved": True}
            if determinant:
                value["successful_krylov_matrix_mod_prime"] = matrix_rows(krylov)
            self.store(name, value)
            data = self.cached(name)
            print(json.dumps({"stage": "cyclic_specialization", "candidate": candidate,
                "prime": prime, "z0": z0, "actual_rank": rank, "determinant": determinant,
                "seconds": time.monotonic()-self.started}), flush=True)
        assert data["candidate_index"] == candidate and data["prime"] == prime and data["z0"] == z0
        assert data["primitive_generator_certified_by_actual_minor"] == bool(data["actual_determinant_mod_prime"])
        assert data["characteristic_zero_nonprimitive_claimed_from_failure"] is False
        return data, file_spec(self.path(name))

    def select_primitive(self):
        name = "R806-accepted-primitive-candidate"
        data = self.cached(name)
        if data is None:
            # Each diagonal is finite. No already completed triple is repeated.
            for diagonal in itertools.count():
                for candidate in range(min(diagonal, CANDIDATE_COUNT-1)+1):
                    for prime_index in range(diagonal-candidate+1):
                        self.budget()
                        z0 = diagonal-candidate-prime_index
                        if z0 > SEARCH_DEGREE_BOUND:
                            continue
                        prime = self.prime_at(prime_index)
                        if z0 >= prime:
                            continue
                        trial_name = "R806-candidate-"+str(candidate).zfill(10)+"-prime-"+str(prime)+"-z-"+str(z0)+"-cyclic"
                        previous = self.cached(trial_name)
                        if previous is not None and not previous["actual_determinant_mod_prime"]:
                            assert previous["candidate_index"] == candidate and previous["prime"] == prime
                            assert previous["z0"] == z0
                            continue
                        solver = self.solver(prime)
                        if solver is None:
                            continue
                        cyclic, cyclic_spec = self.cyclic(candidate, prime, z0, solver)
                        if not cyclic["actual_determinant_mod_prime"]:
                            continue
                        definition, definition_spec, _ = self.candidate_definition(candidate)
                        self.store(name, {"candidate_index": candidate,
                            "candidate_definition": definition_spec,
                            "w0_original_M2_integer_coordinates": definition["w0_original_M2_integer_coordinates"],
                            "prime": prime, "z0": z0,
                            "actual_determinant_mod_prime": cyclic["actual_determinant_mod_prime"],
                            "actual_cyclic_rank": FREE, "cyclic_witness": cyclic_spec,
                            "source_modular_multiplier": cyclic["source_modular_multiplier"],
                            "fixed_minor_inverse": solver["spec"],
                            "original_coordinate_chart": self.chart_spec,
                            "search_diagonal": diagonal,
                            "original_function_field_primitive_generator_certified": True,
                            "characteristic_zero_Krylov_matrix_or_inverse_computed": False})
                        data = self.cached(name)
                        break
                    if data is not None:
                        break
                if data is not None:
                    break
        assert data["actual_cyclic_rank"] == FREE
        assert data["actual_determinant_mod_prime"] % data["prime"]
        assert data["original_coordinate_chart"] == self.chart_spec
        assert data["original_function_field_primitive_generator_certified"] is True
        self.accepted = data
        self.accepted_spec = file_spec(self.path(name))
        self.accepted_solver = self.solver(data["prime"])
        assert self.accepted_solver is not None
        assert self.accepted_solver["spec"] == data["fixed_minor_inverse"]
        self.accepted_modular = self.cached(data["source_modular_multiplier"]["file"])
        assert file_spec(self.path(data["source_modular_multiplier"]["file"])) == data["source_modular_multiplier"]
        assert self.accepted_modular["candidate_index"] == data["candidate_index"]
        assert self.accepted_modular["prime"] == data["prime"]
        assert self.accepted_modular["all820_modular_equations_verified"] is True

    def reconstruct(self, lifted, modulus, target):
        count = target.ncols()
        values = []
        for row in lifted:
            recovered = []
            for value in row:
                rational = rational_reconstruct(value, modulus)
                if rational is None:
                    return None
                recovered.append(rational)
            values.append(recovered)
        assert len(values) == DIM and all(len(row) == count for row in values)
        denominators = []
        for column in range(count):
            denominator = 1
            for row in values:
                denominator = math.lcm(denominator, int(row[column].denom()))
            denominators.append(denominator)
        numerators = fmpz_mat([
            [int(value.numer())*(denominators[j]//int(value.denom())) for j, value in enumerate(row)]
            for row in values])
        actual = self.C*numerators
        for i in range(ROWS):
            for j in range(count):
                if actual[i, j] != target[i, j]*denominators[j]:
                    return None
        return numerators, denominators

    def solve_group(self, group):
        candidate, prime = self.accepted["candidate_index"], self.accepted["prime"]
        first = group*self.item["dixon_group_columns"]
        columns = list(range(first, min(first+self.item["dixon_group_columns"], FREE)))
        assert columns
        stem = "R806-candidate-"+str(candidate).zfill(10)+"-group-"+str(group).zfill(3)
        name, current_name = stem+"-exact-coordinates", stem+"-dixon-current"
        old = self.cached(name)
        if old is not None:
            assert old["candidate_index"] == candidate and old["column_indices"] == columns
            assert old["accepted_primitive_candidate"] == self.accepted_spec
            assert old["fixed_minor_inverse"] == self.accepted_solver["spec"]
            assert old["all820_original_coordinates_verified"] is True
            if self.path(current_name).exists():
                current = self.cached(current_name, current=True)
                assert current["candidate_index"] == candidate and current["column_indices"] == columns
                assert current["prime"] == prime and current["accepted_primitive_candidate"] == self.accepted_spec
                assert current["fixed_minor_inverse"] == self.accepted_solver["spec"]
                self.path(current_name).unlink()
            return file_spec(self.path(name))
        target, product_index, product_specs = self.targets(candidate, columns)
        count = len(columns)
        assert target.nrows() == ROWS and target.ncols() == count
        binding = {"candidate_index": candidate, "column_indices": columns,
            "product_index": product_index, "product_columns": product_specs,
            "original_coordinate_chart": self.chart_spec,
            "accepted_primitive_candidate": self.accepted_spec}
        binding_sha = fingerprint(binding)
        ni = [[int(target[i, j]) for j in range(count)] for i in self.I]
        current = self.cached(current_name, current=True)
        if current is None:
            lifted, residual, digits, modulus = [[0]*count for _ in range(DIM)], ni, 0, 1
            previous_sha = None
        else:
            assert current["candidate_index"] == candidate and current["column_indices"] == columns
            assert current["prime"] == prime
            assert current["rhs_binding_sha256"] == binding_sha
            assert current["accepted_primitive_candidate"] == self.accepted_spec
            assert current["fixed_minor_inverse"] == self.accepted_solver["spec"]
            digits, modulus = current["digits"], int(current["modulus"])
            assert digits >= 1 and modulus == prime**digits
            lifted = [[int(x) for x in row] for row in current["lifted_integer_coordinates"]]
            residual = [[int(x) for x in row] for row in current["exact_divided_residual"]]
            assert len(lifted) == len(residual) == DIM
            assert all(len(row) == count for row in lifted+residual)
            assert all(0 <= value < modulus for row in lifted for value in row)
            actual = self.A*fmpz_mat(lifted)
            assert all(actual[i, j]+modulus*residual[i][j] == ni[i][j]
                       for i in range(DIM) for j in range(count))
            previous_sha = sha(self.path(current_name))
        inverse = self.accepted_solver["inverse"]
        while True:
            self.budget()
            if digits and (digits == 1 or digits % self.item["reconstruct_every_digits"] == 0):
                recovered = self.reconstruct(lifted, modulus, target)
                if recovered is not None:
                    numerators, denominators = recovered
                    for offset, column in enumerate(columns):
                        assert denominators[offset] > 0 and denominators[offset] % prime
                        inverse_denominator = pow(denominators[offset], -1, prime)
                        for row in range(DIM):
                            output, degree = S_position(row)
                            coefficient = int(numerators[row, offset])
                            if degree > 1+EPS[column]-EPS[output]:
                                assert coefficient == 0
                            assert coefficient*inverse_denominator % prime == \
                                int(self.accepted_modular["coordinates_mod_prime"][row][column])
                    self.store(name, {"candidate_index": candidate, "group": group,
                        "column_indices": columns, "basis_dimension": DIM, "full_coordinate_rows": ROWS,
                        "coordinate_numerators": matrix_rows(numerators, strings=True),
                        "column_denominators": [str(value) for value in denominators],
                        "coordinate_convention": "coefficient in original scaled S basis is numerator/column_denominator",
                        "integer_scale": str(LEVEL**6),
                        "source_rhs": binding, "rhs_binding_sha256": binding_sha,
                        "accepted_primitive_candidate": self.accepted_spec,
                        "source_modular_multiplier": self.accepted["source_modular_multiplier"],
                        "fixed_minor_inverse": self.accepted_solver["spec"],
                        "actual_prime": prime, "actual_Dixon_digits": digits,
                        "actual_reconstruction_modulus": str(modulus),
                        "all820_original_coordinates_verified": True,
                        "weighted_polynomial_support_verified": True,
                        "reduction_equals_successful_modular_multiplier": True,
                        "rational_reconstruction_used_uniform_strict_rectangular_bound": True,
                        "characteristic_zero_inverse_matrix_formed": False})
                    self.path(current_name).unlink(missing_ok=True)
                    print(json.dumps({"stage": "exact_primitive_multiplication_group", "candidate": candidate,
                        "group": group, "columns": columns, "digits": digits,
                        "modulus_bits": modulus.bit_length(), "full_rows_verified": ROWS,
                        "seconds": time.monotonic()-self.started}), flush=True)
                    return file_spec(self.path(name))
            if digits == 0:
                # Reuse the completed full modular screen, including its first correction.
                delta = [[int(self.accepted_modular["coordinates_mod_prime"][i][column])
                          for column in columns] for i in range(DIM)]
            else:
                correction = inverse*nmod_mat([[value % prime for value in row] for row in residual], prime)
                delta = matrix_rows(correction)
            product = self.A*fmpz_mat(delta)
            updated = []
            for i in range(DIM):
                row = []
                for j in range(count):
                    numerator = residual[i][j]-int(product[i, j])
                    assert numerator % prime == 0
                    row.append(numerator//prime)
                    lifted[i][j] += modulus*delta[i][j]
                updated.append(row)
            residual, modulus, digits = updated, modulus*prime, digits+1
            self.store(current_name, {"candidate_index": candidate, "group": group,
                "column_indices": columns, "prime": prime, "digits": digits, "modulus": str(modulus),
                "rhs_binding_sha256": binding_sha,
                "accepted_primitive_candidate": self.accepted_spec,
                "fixed_minor_inverse": self.accepted_solver["spec"],
                "lifted_integer_coordinates": [[str(x) for x in row] for row in lifted],
                "exact_divided_residual": [[str(x) for x in row] for row in residual],
                "previous_checkpoint_sha256": previous_sha,
                "invariant": "A*X+prime^digits*residual=P_I",
                "first_modular_correction_reused_from_completed_screen": True,
                "complete_coordinates_claimed": False,
                "only_current_full_lift_vector_retained": True}, current=True)
            current_sha = sha(self.path(current_name))
            history_name = stem+"-dixon-digit-"+str(digits).zfill(6)+"-receipt"
            history = {"candidate_index": candidate, "group": group, "column_indices": columns,
                "prime": prime, "digits": digits, "modulus_bits": modulus.bit_length(),
                "current_checkpoint_sha256": current_sha,
                "previous_checkpoint_sha256": previous_sha,
                "rhs_binding_sha256": binding_sha,
                "exact_divided_residual_invariant_preserved": True,
                "large_lift_vector_or_residual_embedded": False}
            prior_history = self.cached(history_name)
            if prior_history is None:
                self.store(history_name, history)
            else:
                for key, value in history.items():
                    assert prior_history[key] == value
            previous_sha = current_sha
            if digits == 1 or digits % self.item["reconstruct_every_digits"] == 0:
                print(json.dumps({"stage": "Dixon_current_primitive_group", "candidate": candidate,
                    "group": group, "digits": digits, "modulus_bits": modulus.bit_length(),
                    "seconds": time.monotonic()-self.started}), flush=True)

    def polynomial_interface(self, solutions):
        mapping = [{"S_row": row, "normal_basis_row": S_position(row)[0],
                    "power_of_z": S_position(row)[1]} for row in range(DIM)]
        assert len({(entry["normal_basis_row"], entry["power_of_z"]) for entry in mapping}) == DIM
        all_columns = []
        for spec in solutions:
            assert file_spec(self.path(spec["file"])) == spec
            data = self.cached(spec["file"])
            assert data["accepted_primitive_candidate"] == self.accepted_spec
            assert data["integer_scale"] == str(LEVEL**6)
            assert data["all820_original_coordinates_verified"] is True
            assert data["weighted_polynomial_support_verified"] is True
            assert data["reduction_equals_successful_modular_multiplier"] is True
            columns, numerators, denominators = data["column_indices"], data["coordinate_numerators"], data["column_denominators"]
            assert len(numerators) == DIM and all(len(row) == len(columns) for row in numerators)
            assert len(denominators) == len(columns)
            all_columns.extend(columns)
        assert all_columns == list(range(FREE))
        name = "R806-exact-polynomial-multiplier-in-original-normal-basis"
        payload = {"candidate_index": self.accepted["candidate_index"],
            "w0_original_M2_integer_coordinates": self.accepted["w0_original_M2_integer_coordinates"],
            "w": "w0/tau; original tau=e0",
            "coordinate_chart": self.chart_spec,
            "accepted_primitive_candidate": self.accepted_spec,
            "normal_affine_basis_rank": FREE, "normal_affine_basis_degrees": EPS,
            "original_R805_free_basis": self.r805.certificate["graded_free_basis_stage"],
            "original_R805_S_basis_index": self.r805.certificate["S_basis_index"],
            "coordinate_groups": solutions, "S_row_to_polynomial_coefficient": mapping,
            "matrix_convention": "M_ba(z) is output row b, input column a",
            "exact_entry_rule": "M_ba coefficient of z^j equals X_(S_row(b,j),a); coordinate groups encode X=N/D_a",
            "coefficient_field": "Q, certified by exact original rational coordinate equations",
            "weighted_degree_bound": "deg(M_ba)<=1+epsilon_a-epsilon_b; negative bound means zero",
            "all272_columns_verified_in_all820_original_rows": True,
            "all_weighted_support_zeros_verified": True,
            "reduction_equals_successful_modular_multiplier": True,
            "actual_cyclic_witness": self.accepted["cyclic_witness"],
            "original_function_field_primitive_generator_certified": True,
            "normal_integral_basis_preserved": True,
            "K_z_w_assumed_normal": False,
            "characteristic_zero_Krylov_matrix_or_inverse_computed": False,
            "field_coordinate_transport_computed": False,
            "M6_clearing_computed": False, "original_function_DAG_computed": False,
            "polar_ideals_or_KM_representatives_computed": False,
            "actual_eta_rigidification_or_height_computed": False}
        old = self.cached(name)
        if old is None:
            self.store(name, payload)
        else:
            for key, value in payload.items():
                assert old[key] == value
        return file_spec(self.path(name))

    def run(self):
        final = self.out/FINAL
        if final.exists():
            certificate = read(final)
            assert certificate["result"] == RESULT and certificate["complete"] is True
            assert certificate["configuration"] == self.tag
            manifest = certificate["stage_manifest"]
            assert file_spec(self.out/manifest["file"]) == manifest
            for entry in read(self.out/manifest["file"])["files"]:
                assert file_spec(self.out/entry["file"]) == entry
        else:
            self.load_chart()
            self.select_primitive()
            solutions = [self.solve_group(group)
                         for group in range((FREE+self.item["dixon_group_columns"]-1)//self.item["dixon_group_columns"])]
            interface = self.polynomial_interface(solutions)
            assert not list(self.out.glob("R806-*-dixon-current.json.gz"))
            files = [file_spec(path) for path in sorted(self.out.glob("R806-*.json.gz"))
                     if path.name != "R806-stage-manifest.json.gz"]
            manifest = self.store("R806-stage-manifest", {"files": files})
            certificate = {"result": RESULT, "complete": True, "p": P, "configuration": self.tag,
                "completed_scope": "primitive_multiplication_and_cyclic_certificate",
                "normal_affine_basis_rank": FREE, "S_basis_dimension": DIM,
                "qY_count": COUNT, "full_coordinate_rows": ROWS, "integer_scale": str(LEVEL**6),
                "actual_candidate_index": self.accepted["candidate_index"],
                "actual_w0_original_M2_integer_coordinates": self.accepted["w0_original_M2_integer_coordinates"],
                "actual_cyclic_minor": {"prime": self.accepted["prime"], "z0": self.accepted["z0"],
                    "rank": FREE, "determinant_mod_prime": self.accepted["actual_determinant_mod_prime"]},
                "coordinate_chart": self.chart_spec, "accepted_candidate": self.accepted_spec,
                "exact_coordinate_groups": solutions, "polynomial_multiplier": interface,
                "stage_manifest": manifest,
                "exact_polynomial_multiplication_computed": True,
                "all272_columns_verified_in_all820_original_rows": True,
                "actual_cyclic_minor_certified": True,
                "original_function_field_primitive_generator_certified": True,
                "normal_integral_basis_preserved": True,
                "old_R805_ranks_selection_or_saved_products_recomputed": False,
                "characteristic_zero_Krylov_matrix_or_inverse_computed": False,
                "field_coordinate_transport_computed": False,
                "M6_clearing_computed": False, "original_function_DAG_computed": False,
                "polar_ideals_or_KM_representatives_computed": False,
                "actual_eta_rigidification_or_height_computed": False,
                "seconds": time.monotonic()-self.started}
            save(final, certificate)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(final),
            "exact_polynomial_multiplication_computed": True,
            "original_function_field_primitive_generator_certified": True,
            "normal_integral_basis_preserved": True,
            "actual_eta_rigidification_or_height_computed": False})
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
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error),
            "complete_source_bound_stages_and_latest_Dixon_vectors_preserved": True})
        raise


if __name__ == "__main__":
    sys.exit(main())
