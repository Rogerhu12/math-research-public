#!/usr/bin/env python3
"""R805 minimal producer: original pencil and graded free basis, no polar ideals."""
import argparse
import gzip
import hashlib
import itertools
import json
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpz, fmpz_poly, nmod_mat

RESULT = "R805-original-affine-pencil-free-basis"
FINAL = "p41-original-affine-pencil-free-basis-certificate.json"
P, LEVEL, CYC, REAL, COUNT = 41, 82, 40, 20, 41
DIMS = {1: 146, 2: 418, 3: 690}
P6 = "R775-basis-power-6.json.gz"
INDEX799 = "R799-original-power7-basis-index.json.gz"
INDEX799_SHA = "b7889ae6e3ccf8607ce40215d68ca65f0075ac2f8638284690d8a4108e244847"
SELECT799 = "R799-power7-selection-progress.json.gz"
SELECT799_SHA = "3da403c7552b496e3b337f13f9bc7aa35b2d48cbeced025c675f24b226ee01d1"


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematical execution belongs to public repository Actions.")


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


def pivot_columns(reduced, rank):
    answer = [next(j for j in range(reduced.ncols()) if reduced[i, j])
              for i in range(rank)]
    assert answer == sorted(set(answer))
    return answer


def modular(columns, prime, count=None):
    if count is None:
        count = len(columns[0])
    assert all(len(column) >= count for column in columns)
    return nmod_mat([[int(columns[j][i]) % prime for j in range(len(columns))]
                     for i in range(count)], prime)


def minor_certificate(matrix, columns, prime):
    independent = nmod_mat(
        [[int(matrix[i, j]) for j in columns] for i in range(matrix.nrows())],
        prime)
    reduced, rank = independent.transpose().rref()
    assert rank == len(columns)
    rows = pivot_columns(reduced, rank)
    square = nmod_mat([[int(matrix[i, j]) for j in columns] for i in rows],
                      prime)
    determinant = int(square.det())
    assert determinant
    return {"row_indices": rows, "column_indices": columns,
            "actual_determinant_mod_prime": determinant}


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


class Job:
    def __init__(self, args):
        self.args, self.out, self.started = args, args.output, time.monotonic()
        self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        assert self.item["result"] == RESULT and self.item["p"] == P
        assert self.item["producer_inputs_pending"] is False
        assert self.item["core_sha256"] == sha(__file__)
        assert sha(args.proof) == self.item["R805_proof_sha256"]
        assert sha(args.method) == self.item["R805_method_sha256"]
        assert flint.__version__ == "0.9.0"
        assert self.item["qY_count"] == COUNT
        assert self.item["auxiliary_prime_start"] == 739
        assert self.item["requested_stage"] == "pencil_and_graded_free_basis"
        assert set(self.item["retained_artifacts"]) == {"R775", "R786", "R799"}
        self.inputs = {label: Retained(args.retained, label, self.item["retained_artifacts"][label])
                       for label in ("R775", "R786", "R799")}
        self.r775, self.r786, self.r799 = (self.inputs[x] for x in ("R775", "R786", "R799"))
        source6 = self.r775.cert_stage(P6)
        assert source6["rank"] == len(source6["basis"]) == 1506
        assert source6["characteristic_zero_independence_certified_by_unit_reduction"] is True
        anchors = set()
        for row in source6["basis"]:
            recipe = row["recipe"]
            assert recipe["kind"] == "product" and recipe["left_power"] == 1 and recipe["right_power"] == 5
            anchors.add(recipe["left_index"])
        assert anchors == {0, 1, 73}
        assert self.r799.tag["retained_artifacts"]["R775"]["files"][P6] == self.r775.files[P6]["sha256"]
        assert self.r799.certificate["three_original_anchor_basepoint_free_input_verified"] is True
        old799 = self.r799.stage(INDEX799, INDEX799_SHA)
        assert self.r799.files[SELECT799]["sha256"] == SELECT799_SHA
        assert old799["dimension"] == 1778 and old799["ordinary_power"] == 7
        assert old799["anchor_indices"] == [0, 1, 73]
        assert old799["two_anchor_basepoint_free_certified_by_actual_minor"] is False
        assert old799["actual_nonzero_minor"]["prime"] == 739
        assert old799["actual_nonzero_minor"]["determinant_mod_prime"] == 534
        assert old799["candidate_cursor"] == 4518
        selected799 = old799["basis_rows"]
        assert len(selected799) == 1778
        assert selected799[1757]["index"] == 1757 and selected799[1757]["recipe"]["left_index"] == 1
        assert selected799[1758]["index"] == 1758 and selected799[1758]["recipe"]["left_index"] == 73
        assert all(row["recipe"]["left_index"] in (0, 1) for row in selected799[:1758])
        self.old_two_anchor = {"source": self.r799.source(INDEX799),
            "selection_stage_sha256": SELECT799_SHA, "ordinary_power": 7,
            "prime": 739, "actual_two_anchor_rank_from_saved_selection": 1758,
            "actual_full_three_anchor_rank": 1778, "actual_full_minor_mod_prime": 534,
            "characteristic_zero_two_anchor_failure_claimed": False,
            "old_rank_arithmetic_recomputed": False}
        certificate = self.r786.certificate
        assert certificate["exact_K_basis_prefix_bound_qY"] == 128
        assert certificate["basis_in_original_R775_saved_order"] is True
        entry = certificate["stages_manifest"]
        assert plain_spec(entry) == plain_spec(self.r786.files[entry["file"]])
        inventory = self.r786.stage(entry["file"], entry["sha256"])
        self.entries786 = {row["file"]: row for row in inventory["files"]}
        self.tag = {"result": RESULT, "source_sha256": sha(__file__),
            "python_flint": flint.__version__, "p": P,
            "R805_proof_sha256": sha(args.proof), "R805_method_sha256": sha(args.method),
            "retained_artifacts": self.item["retained_artifacts"],
            "qY_count": COUNT, "source_powers": [1, 2, 3],
            "source_dimensions": {str(r): DIMS[r] for r in DIMS},
            "basis_scales": {str(r): str(LEVEL**(2*r)) for r in DIMS},
            "tau_original_index": 0, "sigma_formula": "e1+n*e73",
            "pencil_candidate_order": "1..272,then0; skip old (prime739,n0) negative modular witness",
            "auxiliary_prime_start": 739,
            "integer_basis_coordinate_order": "qY exponent0..40 then xi exponent0..39",
            "real_coordinate_order": "20*n+r; v=xi^-10*qY; t=xi+xi^-1",
            "graded_free_basis_degree_distribution": [1, 144, 127],
            "source_alias_policy": "all saved V2/V3 monomial recipes before any new product",
            "old_saved_products_recomputed": False}
        T = fmpz_poly([0, 1])
        self.chebyshev = [fmpz_poly([2]), T]
        for _ in range(2, 21):
            self.chebyshev.append(T*self.chebyshev[-1]-self.chebyshev[-2])
        self.gt = fmpz_poly([1])
        for poly in self.chebyshev[1:]:
            self.gt += poly
        self.sources, self.recipes, self.leaves, self.aliases = {}, {}, {}, {}
        self.old_cache, self.product_cache = {}, {}
        self.new_product_specs = []
        self.accepted, self.free = None, None

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes-45:
            raise BudgetStop("Completed source-bound products, ranks and basis rows retained.")

    def path(self, name):
        assert name.startswith("R805-") and Path(name).name == name
        return self.out/(name if name.endswith(".json.gz") else name+".json.gz")

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        data = read(path)
        assert data["complete"] is True and data["configuration"] == self.tag
        return data

    def store(self, name, value):
        save(self.path(name), dict(value, complete=True, configuration=self.tag))
        return file_spec(self.path(name))

    def original_name(self, power, index):
        assert power in DIMS and 0 <= index < DIMS[power]
        return "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"

    def scan_recipes(self):
        for power in (1, 2, 3):
            for index in range(DIMS[power]):
                self.budget()
                name = self.original_name(power, index)
                entry = self.entries786[name]
                assert plain_spec(entry) == plain_spec(self.r786.files[name])
                data = self.r786.stage(name, entry["sha256"])
                assert data["weight"] == 2*power and data["bound_qY"] == 128
                assert data["integer_scale"] == str(LEVEL**(2*power))
                assert data["original_R775_finite_coefficients_verified"] is True
                recipe = data["recipe"]
                if power == 1:
                    assert recipe["kind"] == "det_semilinear_E1_pair_trace"
                    leaves = (index,)
                else:
                    assert recipe["kind"] == "product"
                    lp, li, rp, ri = (recipe[k] for k in
                        ("left_power", "left_index", "right_power", "right_index"))
                    assert lp < power and rp < power and lp+rp == power
                    leaves = tuple(sorted(self.leaves[lp, li]+self.leaves[rp, ri]))
                self.recipes[power, index] = recipe
                self.sources[power, index] = self.r786.source(name)
                self.leaves[power, index] = leaves
                self.aliases.setdefault(leaves, (power, index))
        name = "R805-original-monomial-alias-index"
        value = {"source_powers": [1, 2, 3],
            "rows": [{"power": r, "index": i, "sorted_M2_leaf_indices": list(self.leaves[r, i]),
                      "source": self.sources[r, i], "recipe": self.recipes[r, i]}
                     for r in (1, 2, 3) for i in range(DIMS[r])],
            "old_two_anchor_record": self.old_two_anchor,
            "three_anchor_power6_source": self.r775.source(P6),
            "three_anchor_basepoint_free_input_verified": True,
            "old_basis_or_rank_arithmetic_recomputed": False}
        old = self.cached(name)
        if old is None:
            self.store(name, value)
        else:
            for key, val in value.items():
                assert old[key] == val
        self.alias_spec = file_spec(self.path(name))

    def real_rows(self, rows):
        answer = []
        for n, row in enumerate(rows):
            cyclic = [0]*P
            for r, value in enumerate(row):
                cyclic[(r+10*n) % P] += int(value)
            reduced = [value-cyclic[40] for value in cyclic[:40]]+[0]
            assert all(reduced[r] == reduced[P-r] for r in range(1, 21)), (n, "original real phase")
            poly = fmpz_poly([reduced[0]])
            for r in range(1, 21):
                poly += self.chebyshev[r]*reduced[r]
            poly %= self.gt
            answer.append([int(poly[r]) for r in range(REAL)])
        return answer

    def original(self, power, index):
        key = power, index
        if key not in self.old_cache:
            data = self.r786.stage(self.original_name(power, index), self.sources[key]["sha256"])
            raw = data["integer_qY_xi_coefficients"]
            assert len(raw) == 129 and all(len(row) == CYC for row in raw)
            raw = [[int(x) for x in row] for row in raw[:COUNT]]
            real = self.real_rows(raw)
            self.old_cache[key] = {"q": raw, "v": real,
                "source": self.sources[key], "integer_scale": str(LEVEL**(2*power)),
                "leaves": self.leaves[key], "old_saved_product_recomputed": False}
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
        assert real == direct, "New product failed all original/real coordinate comparisons."
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
        name = "R805-new-monomial-"+"-".join(str(i).zfill(3) for i in leaves)
        old = self.cached(name)
        if old is None:
            self.budget()
            if len(leaves) == 2:
                left, right = self.monomial(leaves[:1]), self.monomial(leaves[1:])
            else:
                pair = next((tuple(sorted(pair)) for pair in itertools.combinations(leaves, 2)
                             if tuple(sorted(pair)) in self.aliases), tuple(leaves[:2]))
                remaining = list(leaves)
                for i in pair:
                    remaining.remove(i)
                left, right = self.monomial(pair), self.monomial(tuple(remaining))
            raw, real = self.multiply(left, right)
            self.store(name, {"sorted_M2_leaf_indices": list(leaves), "weight": 2*len(leaves),
                "integer_scale": str(LEVEL**(2*len(leaves))), "qY_count": COUNT,
                "integer_qY_xi_coefficients": [[str(x) for x in row] for row in raw],
                "integer_v_t_coefficients": [[str(x) for x in row] for row in real],
                "factor_sources": [left["source"], right["source"]],
                "all_original_and_real_coordinates_verified": True,
                "old_recipe_alias_exists": False, "old_saved_product_recomputed": False})
            old = self.cached(name)
        assert old["sorted_M2_leaf_indices"] == list(leaves)
        assert old["qY_count"] == COUNT and old["old_recipe_alias_exists"] is False
        assert old["integer_scale"] == str(LEVEL**(2*len(leaves)))
        assert old["all_original_and_real_coordinates_verified"] is True
        answer = {"q": [[int(x) for x in row] for row in old["integer_qY_xi_coefficients"]],
            "v": [[int(x) for x in row] for row in old["integer_v_t_coefficients"]],
            "source": dict(file_spec(self.path(name)), producer="R805"),
            "integer_scale": old["integer_scale"], "leaves": leaves,
            "old_saved_product_recomputed": False}
        assert len(answer["q"]) == len(answer["v"]) == COUNT
        assert all(len(row) == CYC for row in answer["q"])
        assert all(len(row) == REAL for row in answer["v"])
        self.product_cache[leaves] = answer
        return answer

    def flattened(self, leaves, count=COUNT):
        return [x for row in self.monomial(leaves)["v"][:count] for x in row]

    def pencil(self):
        name = "R805-accepted-pencil"
        old = self.cached(name)
        if old is not None:
            assert old["actual_rank"] == 690
            assert old["actual_determinant_mod_prime"] % old["prime"]
            assert old["original_alias_index_sha256"] == self.alias_spec["sha256"]
            self.accepted = old
            return
        columns = {a: [] for a in (0, 1, 73)}
        for a in (0, 1, 73):
            for i in range(DIMS[2]):
                self.budget()
                columns[a].append(self.flattened((a,)+self.leaves[2, i]))
        prime = self.item["auxiliary_prime_start"]
        while True:
            if not fmpz(prime).is_prime():
                prime += 2
                continue
            for n in list(range(1, 273))+[0]:
                self.budget()
                if prime == 739 and n == 0:
                    continue
                attempt = "R805-pencil-prime-"+str(prime)+"-n-"+str(n)
                saved = self.cached(attempt)
                if saved is not None:
                    assert saved["prime"] == prime and saved["n"] == n
                    assert saved["actual_rank"] < 690
                    continue
                sigma = [[x+n*y for x, y in zip(first, second)]
                         for first, second in zip(columns[1], columns[73])]
                matrix = modular(columns[0]+sigma, prime)
                reduced, rank = matrix.rref()
                assert rank <= 690
                if rank < 690:
                    self.store(attempt, {"prime": prime, "n": n, "actual_rank": rank,
                        "characteristic_zero_basepoints_inferred": False,
                        "original_alias_index_sha256": self.alias_spec["sha256"]})
                    continue
                selected = pivot_columns(reduced, rank)
                witness = minor_certificate(matrix, selected, prime)
                self.store(name, dict(witness, prime=prime, n=n, actual_rank=690,
                    full_row_count=COUNT*REAL, full_column_count=836,
                    column_order="tau*V2[0..417],(e1+n*e73)*V2[0..417]",
                    original_alias_index_sha256=self.alias_spec["sha256"],
                    original_tau_index=0, original_sigma_indices=[1, 73],
                    original_sigma_integer_coefficients=[1, n],
                    basepoint_free_certified_by_actual_unit_minor=True,
                    old_two_anchor_record=self.old_two_anchor,
                    new_matrix_entries_have_original_product_generation_witnesses=True))
                self.accepted = self.cached(name)
                print(json.dumps({"stage": "accepted_pencil", "n": n, "prime": prime,
                    "rank": rank, "determinant": witness["actual_determinant_mod_prime"]}), flush=True)
                return
            prime += 2

    def free_basis(self):
        name = "R805-graded-free-basis"
        old = self.cached(name)
        if old is not None:
            assert old["pencil_stage"] == file_spec(self.path("R805-accepted-pencil"))
            assert old["degree1_original_indices"] == list(range(2, 146))
            assert len(old["degree2_original_indices"]) == 127
            assert len(set(old["degree2_original_indices"])) == 127
            assert old["actual_degree2_rank"] == 418
            assert old["actual_pencil_degree2_subspace_rank"] == 291
            assert old["actual_determinant_mod_prime"] % old["prime"]
            self.free = old
            return
        n = self.accepted["n"]
        tau_columns = [self.flattened((0, i), 28) for i in range(146)]
        sigma_columns = []
        for i in range(146):
            first = self.flattened((1, i), 28)
            second = self.flattened((73, i), 28)
            sigma_columns.append([a+n*b for a, b in zip(first, second)])
        old_columns = [[x for row in self.original(2, i)["v"][:28] for x in row]
                       for i in range(418)]
        columns = tau_columns+sigma_columns+old_columns
        prime = self.accepted["prime"]
        while True:
            self.budget()
            if not fmpz(prime).is_prime():
                prime += 2
                continue
            rejected = "R805-degree2-complement-prime-"+str(prime)+"-rejected"
            cached = self.cached(rejected)
            if cached is not None:
                prime += 2
                continue
            first = modular(tau_columns+sigma_columns, prime)
            reduced_first, rank_first = first.rref()
            assert rank_first <= 291
            matrix = modular(columns, prime)
            reduced, rank = matrix.rref()
            assert rank <= 418
            if rank != 418 or rank_first != 291:
                self.store(rejected, {"prime": prime,
                    "actual_degree2_rank": rank, "actual_pencil_subspace_rank": rank_first,
                    "characteristic_zero_dimension_loss_claimed": False})
                prime += 2
                continue
            selected = pivot_columns(reduced, rank)
            first_selected = [i for i in selected if i < 292]
            extra = [i-292 for i in selected if i >= 292]
            assert len(first_selected) == 291 and len(extra) == 127
            witness = minor_certificate(matrix, selected, prime)
            self.store(name, dict(witness, prime=prime,
                pencil_stage=file_spec(self.path("R805-accepted-pencil")),
                original_alias_index_sha256=self.alias_spec["sha256"],
                degree0_basis="1",
                degree1_original_indices=list(range(2, 146)),
                degree1_change_of_basis_determinant=1,
                degree2_original_indices=extra,
                degree2_original_sources=[self.sources[2, i] for i in extra],
                degree2_original_recipes=[self.recipes[2, i] for i in extra],
                degree2_original_M2_leaves=[list(self.leaves[2, i]) for i in extra],
                actual_pencil_degree2_subspace_rank=291, actual_degree2_rank=418,
                degree_distribution=[1, 144, 127], affine_free_module_rank=272,
                column_order="tau*V1,(e1+n*e73)*V1,old_V2; each in original order",
                full_coordinate_rows=560, integer_scale=str(LEVEL**4),
                characteristic_zero_complement_certified=True,
                graded_freeness_uses_original_R805_Koszul_proof=True,
                old_V1_rank_recomputed=False))
            self.free = self.cached(name)
            print(json.dumps({"stage": "graded_free_basis", "prime": prime,
                "degree_distribution": [1, 144, 127],
                "determinant": witness["actual_determinant_mod_prime"]}), flush=True)
            return

    @staticmethod
    def expand_factors(factors):
        terms = {(): 1}
        for factor in factors:
            next_terms = {}
            for leaves, coefficient in terms.items():
                for index, scalar in factor:
                    if not scalar:
                        continue
                    key = tuple(sorted(leaves+(index,)))
                    next_terms[key] = next_terms.get(key, 0)+coefficient*scalar
            terms = {key: value for key, value in next_terms.items() if value}
        return terms

    def S_basis_recipes(self):
        n = self.accepted["n"]
        tau, sigma = [(0, 1)], [(1, 1), (73, n)]
        recipes = []
        for sigma_power in range(4):
            recipes.append({"kind": "degree0_free_generator",
                "tau_power": 3-sigma_power, "sigma_power": sigma_power,
                "terms": self.expand_factors([tau]*(3-sigma_power)+[sigma]*sigma_power)})
        for index in self.free["degree1_original_indices"]:
            for sigma_power in range(3):
                recipes.append({"kind": "degree1_free_generator", "original_M2_index": index,
                    "tau_power": 2-sigma_power, "sigma_power": sigma_power,
                    "terms": self.expand_factors(
                        [tau]*(2-sigma_power)+[sigma]*sigma_power+[[(index, 1)]])})
        for index in self.free["degree2_original_indices"]:
            leaf = self.leaves[2, index]
            for sigma_power in range(2):
                recipes.append({"kind": "degree2_free_generator", "original_V2_index": index,
                    "tau_power": 1-sigma_power, "sigma_power": sigma_power,
                    "terms": self.expand_factors([tau]*(1-sigma_power)+[sigma]*sigma_power+
                                                 [[(leaf[0], 1)], [(leaf[1], 1)]])})
        assert len(recipes) == 690
        return recipes

    def S_basis(self):
        index_name = "R805-degree3-S-basis-index"
        basis_rows, columns = [], []
        for index, recipe in enumerate(self.S_basis_recipes()):
            self.budget()
            terms = recipe.pop("terms")
            encoded = [{"sorted_M2_leaf_indices": list(key), "integer_coefficient": str(value)}
                       for key, value in sorted(terms.items())]
            name = "R805-degree3-S-row-"+str(index).zfill(4)
            old = self.cached(name)
            if old is None:
                raw = [[0]*CYC for _ in range(COUNT)]
                real = [[0]*REAL for _ in range(COUNT)]
                sources = []
                for leaves, coefficient in sorted(terms.items()):
                    product = self.monomial(leaves)
                    sources.append({"sorted_M2_leaf_indices": list(leaves),
                                    "coefficient": str(coefficient), "source": product["source"]})
                    for order in range(COUNT):
                        for k in range(CYC):
                            raw[order][k] += coefficient*product["q"][order][k]
                        for k in range(REAL):
                            real[order][k] += coefficient*product["v"][order][k]
                assert real == self.real_rows(raw), "S basis original/real linear combination mismatch."
                self.store(name, {"index": index, "recipe": recipe,
                    "expanded_integer_monomials": encoded, "monomial_sources": sources,
                    "free_basis_stage": file_spec(self.path("R805-graded-free-basis")),
                    "integer_scale": str(LEVEL**6), "weight": 6, "qY_count": COUNT,
                    "integer_qY_xi_coefficients": [[str(x) for x in row] for row in raw],
                    "integer_v_t_coefficients": [[str(x) for x in row] for row in real],
                    "all_original_and_real_coordinates_verified": True,
                    "old_saved_products_recomputed": False,
                    "V3_membership_has_original_product_generation_witness": True})
                old = self.cached(name)
            assert old["index"] == index and old["recipe"] == recipe
            assert old["expanded_integer_monomials"] == encoded
            assert old["free_basis_stage"] == file_spec(self.path("R805-graded-free-basis"))
            assert old["integer_scale"] == str(LEVEL**6) and old["qY_count"] == COUNT
            assert old["all_original_and_real_coordinates_verified"] is True
            values = old["integer_v_t_coefficients"]
            assert len(values) == COUNT and all(len(row) == REAL for row in values)
            columns.append([int(x) for row in values for x in row])
            basis_rows.append(dict(file_spec(self.path(name)), index=index, recipe=recipe))
        minor_name = "R805-degree3-S-basis-short-minor"
        minor = self.cached(minor_name)
        if minor is None:
            prime = self.free["prime"]
            while True:
                self.budget()
                if not fmpz(prime).is_prime():
                    prime += 2
                    continue
                rejected = "R805-degree3-S-prime-"+str(prime)+"-rejected"
                previous = self.cached(rejected)
                if previous is not None:
                    prime += 2
                    continue
                matrix = modular(columns, prime)
                reduced, rank = matrix.transpose().rref()
                assert rank <= 690
                if rank != 690:
                    self.store(rejected, {"prime": prime, "actual_rank": rank,
                        "characteristic_zero_dimension_loss_claimed": False})
                    prime += 2
                    continue
                witness = minor_certificate(matrix, list(range(690)), prime)
                self.store(minor_name, dict(witness, prime=prime, actual_rank=690,
                    full_coordinate_rows=820, full_columns=690,
                    integer_scale=str(LEVEL**6),
                    all_source_rows=basis_rows,
                    new_short_minor_certified=True,
                    characteristic_zero_inverse_matrix_formed=False,
                    modular_inverse_matrix_formed=False))
                minor = self.cached(minor_name)
                break
        assert minor["actual_rank"] == 690
        assert minor["all_source_rows"] == basis_rows
        assert minor["actual_determinant_mod_prime"] % minor["prime"]
        value = {"dimension": 690, "qY_count": COUNT, "full_coordinate_rows": 820,
            "integer_scale": str(LEVEL**6),
            "original_pencil_stage": file_spec(self.path("R805-accepted-pencil")),
            "graded_free_basis_stage": file_spec(self.path("R805-graded-free-basis")),
            "basis_rows": basis_rows, "short_minor": file_spec(self.path(minor_name)),
            "basis_order": "4 degree0 terms; 144 times3 degree1 terms; 127 times2 degree2 terms",
            "not_old_R786_V3_coefficient_basis": True,
            "all_new_S_rows_have_original_generation_witnesses": True,
            "all_original_and_real_coordinates_verified": True,
            "primitive_multiplication_computed": False,
            "M6_clearing_computed": False}
        old = self.cached(index_name)
        if old is None:
            self.store(index_name, value)
        else:
            for key, val in value.items():
                assert old[key] == val
        self.S_index_spec = file_spec(self.path(index_name))
        self.S_minor = minor

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
            self.scan_recipes()
            self.pencil()
            self.free_basis()
            self.S_basis()
            files = [file_spec(path) for path in sorted(self.out.glob("R805-*.json.gz"))
                     if path.name != "R805-stage-manifest.json.gz"]
            manifest = self.store("R805-stage-manifest", {"files": files})
            certificate = {"result": RESULT, "complete": True, "p": P,
                "configuration": self.tag, "completed_scope": "pencil_and_graded_free_basis",
                "actual_pencil_n": self.accepted["n"],
                "actual_pencil_prime": self.accepted["prime"],
                "actual_pencil_rank": self.accepted["actual_rank"],
                "actual_pencil_minor": self.accepted["actual_determinant_mod_prime"],
                "affine_free_module_rank": 272, "graded_free_basis_degrees": [1, 144, 127],
                "degree3_S_basis_dimension": 690, "degree3_S_prefix_count": COUNT,
                "degree3_S_full_real_coordinates": 820,
                "degree3_S_actual_minor": {
                    "prime": self.S_minor["prime"], "rank": self.S_minor["actual_rank"],
                    "determinant": self.S_minor["actual_determinant_mod_prime"]},
                "alias_index": self.alias_spec,
                "pencil_stage": file_spec(self.path("R805-accepted-pencil")),
                "graded_free_basis_stage": file_spec(self.path("R805-graded-free-basis")),
                "S_basis_index": self.S_index_spec, "stage_manifest": manifest,
                "all_S_rows_original_and_real_coordinates_verified": True,
                "original_82_scales_preserved": True,
                "old_saved_V1_V2_V3_products_recomputed": False,
                "old_two_anchor_V7_mod739_rank_recomputed": False,
                "primitive_multiplication_computed": False,
                "field_coordinate_transport_computed": False,
                "M6_clearing_computed": False,
                "function_DAG_computed": False,
                "polar_ideals_or_KM_representatives_computed": False,
                "actual_eta_rigidification_or_height_computed": False,
                "seconds": time.monotonic()-self.started}
            save(final, certificate)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(final),
            "completed_scope": "pencil_and_graded_free_basis",
            "affine_free_module_rank": 272, "degree3_S_basis_dimension": 690,
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
            "completed_source_bound_stages_preserved": True})
        raise


if __name__ == "__main__":
    sys.exit(main())
