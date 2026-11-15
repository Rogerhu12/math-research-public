#!/usr/bin/env python3
"""R807: one exact V4 block, five projections, a real residual kernel, four M6 clearing rows."""
import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpq, fmpz, fmpz_mat, fmpz_poly, nmod_mat

RESULT = "R807-original-M6-pole-clearing"
FINAL = "p41-original-M6-pole-clearing-certificate.json"
P, LEVEL, CYC, REAL, COUNT, ROWS, DIM = 41, 82, 40, 20, 55, 1100, 962
M6 = "R775-basis-M6-complete.json.gz"
M6_SHA = "70ff7536b50bf99ffb422b7c17dd320b535738fcfcc562fd1597eebcb7a0b299"
P2 = "R775-basis-power-2.json.gz"
P2_SHA = "734a61e967c51ba3c9cd93eaff1a81fba165600110abb941dfdbbeed41b6ebe4"
M2_INDICES = (0, 1, 2, 3, 4, 73)
OLD_PAIR_ALIASES = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3,
                    (0, 4): 4, (0, 73): 73, (1, 73): 218, (2, 73): 345}
NEW_PAIRS = ((3, 73), (4, 73))
NEW_PAIR_SOURCE_HASHES = {
    (3, 73): "4ecfd61fd3e47d49231075da11bcce17e1e4e577d8c4266d44e3e2b2267d45a4",
    (4, 73): "e94730bd1cc3ddad1e0c6ae3c2710c1ac0419a5097629d8631d2509ab65eb450",
}
M6_RECIPES = {
    690: {"factor": "E4", "index": 0, "kind": "elliptic_layer_product", "power": 1},
    691: {"factor": "E4", "index": 73, "kind": "elliptic_layer_product", "power": 1},
    692: {"kind": "level_one", "name": "E6"},
    693: {"kind": "level_one", "name": "eta12"},
}


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
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb", mtime=0, compresslevel=2) as output:
                output.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def plain_spec(row):
    return {key: row[key] for key in ("file", "bytes", "sha256")}


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def same_producer(left, right):
    for key in ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256", "certificate_name"):
        assert str(left[key]) == str(right[key]), ("producer identity", key)
    name = left["certificate_name"]
    assert left["files"][name] == right["files"][name]
    for name in set(left["files"]) & set(right["files"]):
        assert left["files"][name] == right["files"][name]


def eq(value):
    return [str(value.numer()), str(value.denom())]


def dq(value):
    assert len(value) == 2 and int(value[1]) > 0
    return fmpq(int(value[0]), int(value[1]))


def clear_vector(values):
    denominator = 1
    for value in values:
        denominator = math.lcm(denominator, int(value.denom()))
    numerators = [int(value.numer())*(denominator//int(value.denom())) for value in values]
    divisor = denominator
    for value in numerators:
        divisor = math.gcd(divisor, abs(value))
    return [value//divisor for value in numerators], denominator//divisor


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


def packed(rows):
    values = [0]*(79*len(rows))
    for n, row in enumerate(rows):
        assert len(row) == CYC
        values[79*n:79*n+CYC] = row
    return fmpz_poly(values)


def band_rectangles(a, b, c, d, first, stop):
    if a >= b or c >= d or b+d-2 < first or a+c >= stop:
        return
    if a+c >= first and b+d-2 < stop:
        yield a, b, c, d
        return
    if b-a >= d-c:
        middle = (a+b)//2
        yield from band_rectangles(a, middle, c, d, first, stop)
        yield from band_rectangles(middle, b, c, d, first, stop)
    else:
        middle = (c+d)//2
        yield from band_rectangles(a, b, c, middle, first, stop)
        yield from band_rectangles(a, b, middle, d, first, stop)


def exact_small_kernel(original):
    """Exact small elimination, actual pivot minor, and a verified full nullspace basis."""
    assert len(original) == 138 and all(len(row) == 5 for row in original)
    work = [list(row) for row in original]
    source_rows = list(range(len(work)))
    pivots, independent_rows, rank = [], [], 0
    for column in range(5):
        pivot = next((r for r in range(rank, len(work)) if work[r][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        source_rows[rank], source_rows[pivot] = source_rows[pivot], source_rows[rank]
        independent_rows.append(source_rows[rank])
        scalar = work[rank][column]
        work[rank] = [value/scalar for value in work[rank]]
        for r in range(len(work)):
            if r == rank or not work[r][column]:
                continue
            scalar = work[r][column]
            work[r] = [a-scalar*b for a, b in zip(work[r], work[rank])]
        pivots.append(column)
        rank += 1
    assert rank <= 4, "Five independent residuals contradict the original M6 principal parts."
    assert all(not value for row in work[rank:] for value in row)
    free = [column for column in range(5) if column not in pivots]
    nullspace = []
    for column in free:
        vector = [fmpq(0)]*5
        vector[column] = fmpq(1)
        for r, pivot in enumerate(pivots):
            vector[pivot] = -work[r][column]
        assert all(sum(a*b for a, b in zip(row, vector)) == 0 for row in original)
        nullspace.append(vector)
    assert len(nullspace) == 5-rank and free
    square = [[original[r][c] for c in pivots] for r in independent_rows]
    determinant = fmpq(1)
    for column in range(rank):
        pivot = next((r for r in range(column, rank) if square[r][column]), None)
        assert pivot is not None
        if pivot != column:
            square[column], square[pivot] = square[pivot], square[column]
            determinant = -determinant
        diagonal = square[column][column]
        determinant *= diagonal
        for r in range(column+1, rank):
            if square[r][column]:
                factor = square[r][column]/diagonal
                square[r] = [a-factor*b for a, b in zip(square[r], square[column])]
    assert determinant
    chosen = list(nullspace[0])
    first = next(i for i, value in enumerate(chosen) if value)
    leading = chosen[first]
    chosen = [value/leading for value in chosen]
    assert chosen[first] == 1
    assert all(sum(a*b for a, b in zip(row, chosen)) == 0 for row in original)
    return {"actual_rank": rank, "pivot_columns": pivots, "free_columns": free,
            "independent_original_row_indices": independent_rows,
            "actual_nonzero_rank_minor": eq(determinant),
            "rref_nonzero_rows": [[eq(value) for value in row] for row in work[:rank]],
            "full_nullspace_basis": [[eq(value) for value in row] for row in nullspace],
            "chosen_smallest_free_column": free[0], "first_nonzero_lambda_index": first,
            "lambda": [eq(value) for value in chosen],
            "all_138_rows_for_all_kernel_basis_vectors_verified": True,
            "rank_four_was_not_preassigned": True}


class Retained:
    def __init__(self, root, label, spec):
        self.label, self.spec, self.directory = label, spec, Path(root)/label
        mp = self.directory/"full-outputs-manifest.json"
        assert sha(mp) == spec["manifest_sha256"]
        manifest = read(mp)
        assert manifest["result"] == spec["result"]
        self.files = {row["file"]: row for row in manifest["files"]}
        assert len(self.files) == len(manifest["files"])
        self.checked = set()
        run, receipt, initial = (self.raw(name) for name in
            ("run-receipt.json", "core-receipt.json", "public-actions-input.json"))
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert str(run["workflow_run_id"]) == str(spec["run_id"])
        assert run["source_commit"] == initial["source_commit"] == spec["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert run["result"] == initial["result"] == receipt["result"] == spec["result"]
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        assert receipt["complete"] is True and receipt["source_sha256"] == spec["core_sha256"]
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == spec["core_sha256"]
        self.initial = initial
        name = spec["certificate_name"]
        assert self.files[name]["sha256"] == spec["files"][name] == receipt["certificate_sha256"]
        self.certificate = self.raw(name)
        assert self.certificate["complete"] is True and self.certificate["result"] == spec["result"]
        self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == spec["core_sha256"] and self.tag["python_flint"] == "0.9.0"

    def raw(self, name, digest=None):
        assert Path(name).name == name
        row = self.files[name]
        if digest is not None:
            assert row["sha256"] == digest
        if name in self.spec["files"]:
            assert row["sha256"] == self.spec["files"][name]
        path = self.directory/name
        if name not in self.checked:
            assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
            self.checked.add(name)
        return read(path)

    def stage(self, spec):
        assert plain_spec(spec) == plain_spec(self.files[spec["file"]])
        data = self.raw(spec["file"], spec["sha256"])
        assert data["complete"] is True and data["configuration"] == self.tag
        return data

    def cert_stage(self, name, digest):
        rows = {row["file"]: row for row in self.certificate["stages"]}
        assert rows[name]["sha256"] == digest
        return self.stage(rows[name])

    def source(self, name):
        return dict(plain_spec(self.files[name]), producer=self.label)


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
        assert sha(args.method) == self.item["R807_method_sha256"]
        assert flint.__version__ == "0.9.0"
        assert self.item["qY_count"] == COUNT and self.item["V4_dimension"] == DIM
        assert self.item["auxiliary_prime_start"] == 1000000007
        assert self.item["reconstruct_every_digits"] == 8
        assert self.item["requested_stage"] == "four_extra_M6_rows_cleared"
        assert set(self.item["retained_artifacts"]) == {"R775", "R786", "R805"}
        self.inputs = {label: Retained(args.retained, label, spec)
                       for label, spec in self.item["retained_artifacts"].items()}
        self.r775, self.r786, self.r805 = (self.inputs[label] for label in ("R775", "R786", "R805"))
        for label in ("R775", "R786"):
            same_producer(self.r805.tag["retained_artifacts"][label], self.inputs[label].spec)
            same_producer(self.r805.initial["job"]["retained_artifacts"][label], self.inputs[label].spec)
        self.original_M6 = self.r775.cert_stage(M6, M6_SHA)
        assert self.original_M6["rank"] == len(self.original_M6["basis"]) == 694
        for index, recipe in M6_RECIPES.items():
            assert self.original_M6["basis"][index]["recipe"] == recipe
        self.original_P2 = self.r775.cert_stage(P2, P2_SHA)
        assert self.original_P2["rank"] == len(self.original_P2["basis"]) == 418
        self.aliases = {}
        for index, row in enumerate(self.original_P2["basis"]):
            recipe = row["recipe"]
            assert recipe["kind"] == "product" and recipe["left_power"] == recipe["right_power"] == 1
            pair = tuple(sorted((recipe["left_index"], recipe["right_index"])))
            self.aliases.setdefault(pair, index)
        assert all(self.aliases[pair] == index for pair, index in OLD_PAIR_ALIASES.items())
        assert all(pair not in self.aliases for pair in NEW_PAIRS)
        certificate = self.r786.certificate
        assert certificate["exact_K_basis_prefix_bound_qY"] == 128
        assert certificate["basis_in_original_R775_saved_order"] is True
        old_inventory = self.r786.stage(certificate["stages_manifest"])
        self.old_entries = {row["file"]: row for row in old_inventory["files"]}
        assert len(self.old_entries) == len(old_inventory["files"])
        assert self.r805.tag["R805_proof_sha256"] == self.item["R805_proof_sha256"]
        certificate = self.r805.certificate
        assert certificate["completed_scope"] == "pencil_and_graded_free_basis"
        assert certificate["original_82_scales_preserved"] is True
        assert certificate["degree3_S_prefix_count"] == 41
        previous_inventory = self.r805.stage(certificate["stage_manifest"])
        self.previous_entries = {row["file"]: row for row in previous_inventory["files"]}
        self.tag = {"result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "p": P, "R805_proof_sha256": sha(args.proof), "R807_method_sha256": sha(args.method),
            "retained_artifacts": self.item["retained_artifacts"], "qY_count": COUNT,
            "V4_dimension": DIM, "full_real_coordinate_rows": ROWS,
            "basis_integer_scale": str(LEVEL**8), "original_M2_scale": str(LEVEL**2),
            "auxiliary_prime_start": self.item["auxiliary_prime_start"],
            "reconstruct_every_digits": self.item["reconstruct_every_digits"],
            "projection_original_M2_indices": [0, 1, 2, 3, 4],
            "extra_M6_indices": [690, 691, 692, 693],
            "real_coordinate_order": "20*n+r; v=xi^-10*qY; t=xi+xi^-1",
            "existing_R805_pair_prefix_count": 41, "new_pair_tail_interval": [41, 55],
            "original_V4_basis_order_preserved": True, "old_M2_V2_V4_prefixes_recomputed": False,
            "existing_R805_pair_prefixes_recomputed": False,
            "R803_mixed_coordinates_consumed": False, "local_high_jets_computed": False}
        T = fmpz_poly([0, 1])
        self.chebyshev = [fmpz_poly([2]), T]
        for _ in range(2, 21):
            self.chebyshev.append(T*self.chebyshev[-1]-self.chebyshev[-2])
        self.gt = fmpz_poly([1])
        for poly in self.chebyshev[1:]:
            self.gt += poly
        self.old_raw_cache, self.adapted_cache, self.pair_cache = {}, {}, {}
        self.A = None
        self.used_new_tail_specs = {}

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes-30:
            raise BudgetStop("Complete projections, residual/theta and current exact RHS lifts retained.")

    def path(self, name):
        assert name.startswith("R807-") and Path(name).name == name
        return self.out/(name if name.endswith(".json.gz") else name+".json.gz")

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        data = read(path)
        assert data["complete"] is True and data["configuration"] == self.tag
        return data

    def store(self, name, data):
        save(self.path(name), dict(data, complete=True, configuration=self.tag))
        return file_spec(self.path(name))

    def original_name(self, power, index):
        assert power in (1, 2, 4)
        assert 0 <= index < {1: 146, 2: 418, 4: 962}[power]
        return "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"

    def old_raw(self, power, index):
        key = power, index
        if key not in self.old_raw_cache:
            name = self.original_name(power, index)
            data = self.r786.stage(self.old_entries[name])
            assert data["weight"] == 2*power and data["bound_qY"] == 128
            assert data["integer_scale"] == str(LEVEL**(2*power))
            assert data["original_R775_finite_coefficients_verified"] is True
            raw = data["integer_qY_xi_coefficients"]
            assert len(raw) == 129 and all(len(row) == CYC for row in raw)
            result = ([[int(value) for value in row] for row in raw[:COUNT]],
                      self.r786.source(name), data["recipe"])
            if power != 4:
                self.old_raw_cache[key] = result
            return result
        return self.old_raw_cache[key]

    def real_rows(self, rows, first=0):
        answer = []
        for offset, row in enumerate(rows):
            n = first+offset
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

    def adapted(self, power, index):
        key = power, index
        if key in self.adapted_cache:
            return self.adapted_cache[key]
        name = "R807-original-real-prefix-power-"+str(power)+"-row-"+str(index).zfill(4)
        old = self.cached(name)
        source = self.r786.source(self.original_name(power, index))
        if old is None:
            self.budget()
            raw, actual_source, recipe = self.old_raw(power, index)
            assert actual_source == source
            real = self.real_rows(raw)
            self.store(name, {"ordinary_power": power, "index": index,
                "source_original_row": source, "original_recipe": recipe,
                "source_prefix_range": [0, COUNT], "qY_count": COUNT,
                "integer_scale": str(LEVEL**(2*power)),
                "integer_v_t_coefficients": [[str(value) for value in row] for row in real],
                "original_xi_inversion_and_phase_verified": True,
                "old_qY_coefficients_recomputed": False})
            old = self.cached(name)
        assert old["ordinary_power"] == power and old["index"] == index
        assert old["source_original_row"] == source and old["qY_count"] == COUNT
        assert old["integer_scale"] == str(LEVEL**(2*power))
        assert old["original_xi_inversion_and_phase_verified"] is True
        rows = [[int(value) for value in row] for row in old["integer_v_t_coefficients"]]
        assert len(rows) == COUNT and all(len(row) == REAL for row in rows)
        result = {"rows": rows, "source": dict(file_spec(self.path(name)), producer="R807"),
                  "original_source": source, "original_recipe": old["original_recipe"]}
        self.adapted_cache[key] = result
        return result

    def prepare_basis(self):
        if self.A is not None:
            return
        columns, rows = [], []
        for index in range(DIM):
            self.budget()
            data = self.adapted(4, index)
            columns.append([value for row in data["rows"] for value in row])
            rows.append({"index": index, "adapted_stage": data["source"],
                         "original_source": data["original_source"], "original_recipe": data["original_recipe"]})
        name = "R807-original-V4-real-short-basis-index"
        payload = {"dimension": DIM, "qY_count": COUNT, "full_real_coordinates": ROWS,
            "integer_scale": str(LEVEL**8), "basis_rows": rows,
            "original_R786_stages_manifest": self.r786.source(self.r786.certificate["stages_manifest"]["file"]),
            "source_prefix_only_read": [0, COUNT], "old_V4_coefficients_recomputed": False}
        old = self.cached(name)
        if old is None:
            self.store(name, payload)
        else:
            for key, value in payload.items():
                assert old[key] == value
        self.basis_spec = file_spec(self.path(name))
        self.A = fmpz_mat(columns).transpose()
        assert self.A.nrows() == ROWS and self.A.ncols() == DIM

    def modular_solver(self):
        self.prepare_basis()
        name = "R807-original-V4-accepted-short-minor"
        data = self.cached(name)
        if data is None:
            prime = self.item["auxiliary_prime_start"]
            while True:
                self.budget()
                if not fmpz(prime).is_prime():
                    prime += 2
                    continue
                rejected = "R807-V4-prime-"+str(prime)+"-rejected-short-minor"
                if self.cached(rejected) is not None:
                    prime += 2
                    continue
                modular = nmod_mat([[int(self.A[i, j]) % prime for j in range(DIM)]
                                    for i in range(ROWS)], prime)
                reduced, rank = modular.transpose().rref()
                if rank != DIM:
                    self.store(rejected, {"prime": prime, "actual_rank": rank,
                        "basis_index": self.basis_spec, "characteristic_zero_rank_loss_claimed": False})
                    prime += 2
                    continue
                selected = [next(k for k in range(ROWS) if reduced[i, k]) for i in range(DIM)]
                assert selected == sorted(set(selected))
                square = nmod_mat([[int(self.A[i, j]) % prime for j in range(DIM)] for i in selected], prime)
                determinant = int(square.det())
                assert determinant
                inverse = square.inv()
                assert square*inverse == nmod_mat([[int(i == j) for j in range(DIM)] for i in range(DIM)], prime)
                self.store(name, {"prime": prime, "prime_proved": True, "basis_index": self.basis_spec,
                    "full_rows": ROWS, "columns": DIM, "coordinate_row_indices": selected,
                    "selected_basis_column_indices": list(range(DIM)),
                    "actual_determinant_mod_prime": determinant,
                    "inverse_mod_prime": [[int(inverse[i, j]) for j in range(DIM)] for i in range(DIM)],
                    "all_entries_from_original_exact_short_rows": True,
                    "characteristic_zero_basis_independence_certified": True,
                    "characteristic_zero_inverse_matrix_formed": False,
                    "modular_inverse_identity_verified": True})
                data = self.cached(name)
                break
        assert data["basis_index"] == self.basis_spec and data["full_rows"] == ROWS and data["columns"] == DIM
        assert data["prime_proved"] is True and data["modular_inverse_identity_verified"] is True
        assert data["characteristic_zero_basis_independence_certified"] is True
        assert data["actual_determinant_mod_prime"] % data["prime"]
        self.prime, self.row_selection = data["prime"], data["coordinate_row_indices"]
        assert len(self.row_selection) == DIM and self.row_selection == sorted(set(self.row_selection))
        assert data["selected_basis_column_indices"] == list(range(DIM))
        chosen = set(self.row_selection)
        self.complement = [i for i in range(ROWS) if i not in chosen]
        assert len(self.complement) == 138
        self.inverse = nmod_mat(data["inverse_mod_prime"], self.prime)
        self.square = fmpz_mat([[int(self.A[i, j]) for j in range(DIM)] for i in self.row_selection])
        self.minor, self.minor_spec = data, file_spec(self.path(name))
        self.full_modular = None

    def projection_target(self, j):
        assert 0 <= j < 5
        name = "R807-E6-projection-target-j"+str(j)
        old = self.cached(name)
        if old is None:
            self.budget()
            source = self.adapted(1, j)
            values = [LEVEL**6*value for row in source["rows"] for value in row]
            self.store(name, {"projection_M2_index": j, "source_M2_adaptation": source["source"],
                "source_original_M2": source["original_source"],
                "source_original_M6": self.r775.source(M6),
                "source_M6_index": 692, "source_M6_recipe": M6_RECIPES[692],
                "formula": "(82^6 E6)*e_j; E6=1 modulo qY^55",
                "integer_numerators": [str(value) for value in values], "common_denominator": "1",
                "qY_count": COUNT, "full_real_coordinates": ROWS, "product_integer_scale": str(LEVEL**8),
                "individual_target_V4_membership_claimed": False,
                "old_M2_or_M6_prefixes_recomputed": False})
            old = self.cached(name)
        assert old["projection_M2_index"] == j and old["source_M6_index"] == 692
        assert old["individual_target_V4_membership_claimed"] is False
        assert old["product_integer_scale"] == str(LEVEL**8) and old["qY_count"] == COUNT
        assert old["common_denominator"] == "1" and len(old["integer_numerators"]) == ROWS
        return old, file_spec(self.path(name))

    def reconstruct(self, X, modulus, target, mode):
        values = []
        for value in X:
            candidate = rational_reconstruct(value, modulus)
            if candidate is None:
                return None
            values.append(candidate)
        numerators, denominator = clear_vector(values)
        vector = fmpz_mat([[value] for value in numerators])
        actual = self.square*vector
        if not all(int(actual[i, 0]) == target[row]*denominator
                   for i, row in enumerate(self.row_selection)):
            return None
        if mode == "member":
            full = self.A*vector
            assert all(int(full[i, 0]) == target[i]*denominator for i in range(ROWS)), \
                "The unique exact selected-row solution is not a global V4 member."
        else:
            assert mode == "projection"
        return values

    def solve_one(self, label, target_data, target_spec, mode):
        assert mode in ("projection", "member")
        name = "R807-exact-V4-"+label
        current_name = "R807-prime-"+str(self.prime)+"-"+label+"-dixon-current"
        old = self.cached(name)
        if old is not None:
            assert old["mode"] == mode and old["source_target_stage"] == target_spec
            assert old["minor_stage"] == self.minor_spec and old["original_V4_basis_index"] == self.basis_spec
            assert old["all962_selected_rows_verified"] is True
            assert old["all1100_rows_verified"] is (mode == "member")
            self.path(current_name).unlink(missing_ok=True)
            return old, file_spec(self.path(name))
        target = [int(value) for value in target_data["integer_numerators"]]
        target_denominator = int(target_data["common_denominator"])
        assert len(target) == ROWS and target_denominator > 0
        ni = [target[row] for row in self.row_selection]
        current = self.cached(current_name)
        if current is None:
            X, residual, digits, modulus = [0]*DIM, ni, 0, 1
            previous_sha = None
        else:
            assert current["source_target_stage"] == target_spec and current["mode"] == mode
            assert current["minor_stage"] == self.minor_spec and current["prime"] == self.prime
            digits, modulus = current["digits"], int(current["modulus"])
            assert digits >= 1 and modulus == self.prime**digits
            X = [int(value) for value in current["lifted_integer_coordinates"]]
            residual = [int(value) for value in current["exact_divided_residual"]]
            assert len(X) == len(residual) == DIM and all(0 <= value < modulus for value in X)
            actual = self.square*fmpz_mat([[value] for value in X])
            assert all(int(actual[i, 0])+modulus*residual[i] == ni[i] for i in range(DIM)), \
                "The retained exact Dixon invariant failed."
            previous_sha = sha(self.path(current_name))
        while True:
            self.budget()
            if digits and (digits == 1 or digits % self.item["reconstruct_every_digits"] == 0):
                values = self.reconstruct(X, modulus, target, mode)
                if values is not None:
                    coefficients = [value/target_denominator for value in values]
                    numerators, denominator = clear_vector(coefficients)
                    self.store(name, {"label": label, "mode": mode, "source_target_stage": target_spec,
                        "original_V4_basis_index": self.basis_spec, "minor_stage": self.minor_spec,
                        "solution_numerators": [str(value) for value in numerators],
                        "solution_common_denominator": str(denominator),
                        "basis_dimension": DIM, "basis_integer_scale": str(LEVEL**8),
                        "target_denominator_restored_exactly": str(target_denominator),
                        "actual_prime": self.prime, "actual_Dixon_digits": digits,
                        "actual_reconstruction_modulus": str(modulus),
                        "all962_selected_rows_verified": True,
                        "all1100_rows_verified": mode == "member",
                        "individual_V4_membership_claimed": mode == "member",
                        "rational_reconstruction_used_uniform_strict_rectangular_bound": True,
                        "characteristic_zero_inverse_matrix_formed": False,
                        "old_basis_coefficients_recomputed": False})
                    self.path(current_name).unlink(missing_ok=True)
                    print(json.dumps({"stage": "exact_V4_coordinates", "label": label, "mode": mode,
                        "digits": digits, "modulus_bits": modulus.bit_length(),
                        "rows_verified": ROWS if mode == "member" else DIM,
                        "seconds": time.monotonic()-self.started}), flush=True)
                    return self.cached(name), file_spec(self.path(name))
            reduced_rhs = nmod_mat([[value % self.prime] for value in residual], self.prime)
            correction = self.inverse*reduced_rhs
            delta = [int(correction[i, 0]) for i in range(DIM)]
            if digits == 0 and mode == "member":
                if self.full_modular is None:
                    self.full_modular = nmod_mat([[int(self.A[i, j]) % self.prime for j in range(DIM)]
                                                 for i in range(ROWS)], self.prime)
                whole = self.full_modular*correction
                assert all(int(whole[i, 0]) == target[i] % self.prime for i in range(ROWS)), \
                    "A claimed cleared member failed the full original first modular digit."
            # A projection deliberately has no full-row membership assertion.
            product = self.square*fmpz_mat([[value] for value in delta])
            next_residual = []
            for i in range(DIM):
                numerator = residual[i]-int(product[i, 0])
                assert numerator % self.prime == 0
                next_residual.append(numerator//self.prime)
                X[i] += modulus*delta[i]
            residual = next_residual
            modulus *= self.prime
            digits += 1
            self.store(current_name, {"label": label, "mode": mode, "source_target_stage": target_spec,
                "minor_stage": self.minor_spec, "prime": self.prime, "digits": digits, "modulus": str(modulus),
                "lifted_integer_coordinates": [str(value) for value in X],
                "exact_divided_residual": [str(value) for value in residual],
                "previous_checkpoint_sha256": previous_sha,
                "invariant": "A_I X + prime^digits residual = integer_target_I",
                "target_denominator_kept_until_final_coordinates": str(target_denominator),
                "complete_coordinates_claimed": False, "only_current_full_lift_vector_retained": True})
            previous_sha = sha(self.path(current_name))
            if digits == 1 or digits % self.item["reconstruct_every_digits"] == 0:
                print(json.dumps({"stage": "Dixon_current", "label": label, "mode": mode,
                    "digits": digits, "modulus_bits": modulus.bit_length(),
                    "seconds": time.monotonic()-self.started}), flush=True)

    @staticmethod
    def solution_values(data):
        denominator = int(data["solution_common_denominator"])
        assert denominator > 0 and len(data["solution_numerators"]) == DIM
        return [fmpq(int(value), denominator) for value in data["solution_numerators"]]

    def verify_member(self, numerators, denominator, target, target_denominator):
        assert len(numerators) == DIM and len(target) == ROWS
        assert denominator > 0 and target_denominator > 0
        product = self.A*fmpz_mat([[value] for value in numerators])
        assert all(int(product[i, 0])*target_denominator == target[i]*denominator for i in range(ROWS))

    def residual_and_theta(self, projections, target_stages):
        residual_name = "R807-original-five-projection-residual-and-kernel"
        theta_name = "R807-original-nonzero-pole-clearing-theta"
        coordinate_name = "R807-exact-V4-M6-index-692-from-kernel"
        projection_specs = [spec for data, spec in projections]
        target_specs = [spec for data, spec in target_stages]
        residual = self.cached(residual_name)
        if residual is None:
            self.budget()
            denominators = [int(data["solution_common_denominator"]) for data, spec in projections]
            numerator_columns = [[int(value) for value in data["solution_numerators"]] for data, spec in projections]
            product = self.A*fmpz_mat([[column[i] for column in numerator_columns] for i in range(DIM)])
            targets = [[int(value) for value in data["integer_numerators"]] for data, spec in target_stages]
            assert all(data["common_denominator"] == "1" for data, spec in target_stages)
            for i in self.row_selection:
                assert all(int(product[i, j]) == targets[j][i]*denominators[j] for j in range(5))
            integers = [[targets[j][i]*denominators[j]-int(product[i, j]) for j in range(5)]
                        for i in self.complement]
            rational = [[fmpq(value, denominators[j]) for j, value in enumerate(row)] for row in integers]
            kernel = exact_small_kernel(rational)
            self.store(residual_name, dict(kernel,
                projection_stages=projection_specs, projection_target_stages=target_specs,
                original_V4_basis_index=self.basis_spec, minor_stage=self.minor_spec,
                residual_original_row_indices=self.complement,
                residual_integer_numerators=[[str(value) for value in row] for row in integers],
                residual_column_denominators=[str(value) for value in denominators],
                all962_selected_row_residuals_zero_verified=True,
                individual_five_projection_membership_claimed=False))
            residual = self.cached(residual_name)
        assert residual["projection_stages"] == projection_specs and residual["projection_target_stages"] == target_specs
        assert residual["minor_stage"] == self.minor_spec and residual["original_V4_basis_index"] == self.basis_spec
        assert residual["residual_original_row_indices"] == self.complement
        assert residual["actual_rank"] <= 4 and residual["rank_four_was_not_preassigned"] is True
        residual_spec = file_spec(self.path(residual_name))
        values = [dq(value) for value in residual["lambda"]]
        assert len(values) == 5 and any(values)
        assert values[residual["first_nonzero_lambda_index"]] == 1
        theta = self.cached(theta_name)
        if theta is None:
            self.budget()
            coordinate = self.cached(coordinate_name)
            if coordinate is None:
                solution_columns = [self.solution_values(data) for data, spec in projections]
                coefficients = [sum(values[j]*solution_columns[j][i] for j in range(5)) for i in range(DIM)]
                numerators, denominator = clear_vector(coefficients)
                target_values = [sum(values[j]*int(target_stages[j][0]["integer_numerators"][i]) for j in range(5))
                                 for i in range(ROWS)]
                target_numerators, target_denominator = clear_vector(target_values)
                self.verify_member(numerators, denominator, target_numerators, target_denominator)
                self.store(coordinate_name, {"M6_index": 692, "source_M6_recipe": M6_RECIPES[692],
                    "source_original_M6": self.r775.source(M6), "residual_kernel_stage": residual_spec,
                    "projection_stages": projection_specs, "original_V4_basis_index": self.basis_spec,
                    "minor_stage": self.minor_spec, "lambda": [eq(value) for value in values],
                    "solution_numerators": [str(value) for value in numerators],
                    "solution_common_denominator": str(denominator),
                    "target_integer_numerators": [str(value) for value in target_numerators],
                    "target_common_denominator": str(target_denominator),
                    "basis_dimension": DIM, "basis_integer_scale": str(LEVEL**8),
                    "all1100_rows_verified": True, "exact_global_V4_membership_certified": True,
                    "coordinates_obtained_from_five_existing_projections": True,
                    "a_ninth_right_hand_side_solved": False})
            else:
                assert coordinate["residual_kernel_stage"] == residual_spec
                assert coordinate["projection_stages"] == projection_specs
                assert coordinate["lambda"] == residual["lambda"]
                assert coordinate["all1100_rows_verified"] is True
            coordinate_spec = file_spec(self.path(coordinate_name))
            self.store(theta_name, {"lambda": [eq(value) for value in values],
                "theta_in_original_integer_scaled_M2_basis": [eq(value) for value in values]+[["0", "1"] for _ in range(141)],
                "source_original_M2_indices": [0, 1, 2, 3, 4], "original_M2_integer_scale": str(LEVEL**2),
                "residual_kernel_stage": residual_spec, "M6_index692_cleared_coordinate_stage": coordinate_spec,
                "actual_residual_rank": residual["actual_rank"],
                "theta_nonzero_by_original_independent_M2_input": True,
                "first_nonzero_lambda_index": residual["first_nonzero_lambda_index"],
                "theta_at_P0_and_P1_has_two_zeros_by_original_E6_principal_parts": True,
                "global_comparison_degree_bound": 1092, "certified_cusp_zero_order_times_degree": 1100,
                "new_CM_jets_used": False, "full_142_dimensional_clearing_space_recomputed": False,
                "original_P0_P1_qY_or_M2_basis_changed": False})
            theta = self.cached(theta_name)
        assert theta["residual_kernel_stage"] == residual_spec and theta["lambda"] == residual["lambda"]
        assert len(theta["theta_in_original_integer_scaled_M2_basis"]) == 146
        assert theta["theta_nonzero_by_original_independent_M2_input"] is True
        coordinate_spec = theta["M6_index692_cleared_coordinate_stage"]
        assert file_spec(self.out/coordinate_spec["file"]) == coordinate_spec
        coordinate = read(self.out/coordinate_spec["file"])
        assert coordinate["complete"] is True and coordinate["configuration"] == self.tag
        assert coordinate["all1100_rows_verified"] is True and coordinate["residual_kernel_stage"] == residual_spec
        self.theta, self.theta_spec = theta, file_spec(self.path(theta_name))
        self.lambda_values = values
        self.residual_spec = residual_spec
        return coordinate_spec

    def pair_rows(self, pair):
        pair = tuple(sorted(pair))
        if pair in self.pair_cache:
            return self.pair_cache[pair]
        if pair in self.aliases:
            index = self.aliases[pair]
            assert OLD_PAIR_ALIASES[pair] == index
            data = self.adapted(2, index)
            assert data["original_recipe"] == self.original_P2["basis"][index]["recipe"]
            answer = {"rows": data["rows"], "sources": [data["source"]],
                      "source_kind": "unchanged_original_V2_alias", "original_V2_index": index}
            self.pair_cache[pair] = answer
            return answer
        assert pair in NEW_PAIRS
        old_name = "R805-new-monomial-"+"-".join(str(i).zfill(3) for i in pair)+".json.gz"
        assert self.previous_entries[old_name]["sha256"] == NEW_PAIR_SOURCE_HASHES[pair]
        old = self.r805.stage(self.previous_entries[old_name])
        assert old["sorted_M2_leaf_indices"] == list(pair)
        assert old["qY_count"] == 41 and old["weight"] == 4
        assert old["integer_scale"] == str(LEVEL**4)
        assert old["all_original_and_real_coordinates_verified"] is True
        assert old["old_recipe_alias_exists"] is False and old["old_saved_product_recomputed"] is False
        assert len(old["factor_sources"]) == 2
        for source, index in zip(old["factor_sources"], pair):
            assert source == self.r786.source(self.original_name(1, index))
        old_raw = [[int(value) for value in row] for row in old["integer_qY_xi_coefficients"]]
        old_real = [[int(value) for value in row] for row in old["integer_v_t_coefficients"]]
        assert len(old_raw) == len(old_real) == 41
        assert all(len(row) == CYC for row in old_raw) and all(len(row) == REAL for row in old_real)
        prefix_spec = self.r805.source(old_name)
        name = "R807-new-pair-tail-"+"-".join(str(i).zfill(3) for i in pair)+"-0041-0055"
        tail = self.cached(name)
        factor_sources = [self.r786.source(self.original_name(1, index)) for index in pair]
        if tail is None:
            self.budget()
            left, _, _ = self.old_raw(1, pair[0])
            right, _, _ = self.old_raw(1, pair[1])
            first, stop = 41, COUNT
            packed_output = [0]*(79*(stop-first))
            rectangles = list(band_rectangles(0, COUNT, 0, COUNT, first, stop))
            for a, b, c, d in rectangles:
                self.budget()
                assert a+c >= first and b+d-2 < stop
                product = packed(left[a:b]).mul_low(packed(right[c:d]), 79*(stop-a-c))
                shift = 79*(a+c-first)
                assert shift >= 0
                for r in range(product.degree()+1):
                    assert shift+r < len(packed_output)
                    packed_output[shift+r] += int(product[r])
            raw = []
            for n in range(stop-first):
                cyclic = [0]*P
                for r in range(79):
                    cyclic[r % P] += packed_output[79*n+r]
                raw.append([cyclic[r]-cyclic[40] for r in range(CYC)])
            real = self.real_rows(raw, first)
            self.store(name, {"sorted_M2_leaf_indices": list(pair),
                "source_completed_R805_prefix": prefix_spec,
                "source_original_M2_factors": factor_sources,
                "first_exponent": first, "last_exponent_exclusive": stop,
                "integer_scale": str(LEVEL**4), "weight": 4,
                "integer_qY_xi_coefficients": [[str(value) for value in row] for row in raw],
                "integer_v_t_coefficients": [[str(value) for value in row] for row in real],
                "convolution_rectangles": [list(box) for box in rectangles],
                "packed_stride": 79, "maximum_unreduced_xi_degree": 78,
                "only_new_sum_band_convolved": True,
                "original_phase_and_xi_inversion_verified": True,
                "old_R805_q0_through40_recomputed": False,
                "old_saved_V2_alias_recomputed": False})
            tail = self.cached(name)
        assert tail["source_completed_R805_prefix"] == prefix_spec
        assert tail["source_original_M2_factors"] == factor_sources
        assert tail["first_exponent"] == 41 and tail["last_exponent_exclusive"] == COUNT
        assert tail["integer_scale"] == str(LEVEL**4)
        assert tail["only_new_sum_band_convolved"] is True and tail["old_R805_q0_through40_recomputed"] is False
        rows = [[int(value) for value in row] for row in tail["integer_v_t_coefficients"]]
        assert len(rows) == 14 and all(len(row) == REAL for row in rows)
        answer = {"rows": old_real+rows, "sources": [prefix_spec, dict(file_spec(self.path(name)), producer="R807")],
                  "source_kind": "completed_R805_prefix_and_only_new_41_through54"}
        assert len(answer["rows"]) == COUNT
        self.used_new_tail_specs[pair] = file_spec(self.path(name))
        self.pair_cache[pair] = answer
        return answer

    def member_target(self, index):
        assert index in (690, 691, 693)
        name = "R807-cleared-M6-target-index-"+str(index)
        old = self.cached(name)
        if old is None:
            self.budget()
            lambda_numerators, denominator = clear_vector(self.lambda_values)
            rows = [[0]*REAL for _ in range(COUNT)]
            sources = []
            if index in (690, 691):
                anchor = 0 if index == 690 else 73
                for j, coefficient in enumerate(lambda_numerators):
                    if not coefficient:
                        continue
                    pair = tuple(sorted((anchor, j)))
                    data = self.pair_rows(pair)
                    sources.append({"M2_pair": list(pair), "lambda_index": j,
                        "integer_lambda_numerator": str(coefficient),
                        "source_kind": data["source_kind"], "sources": data["sources"]})
                    for n in range(COUNT):
                        for r in range(REAL):
                            rows[n][r] += coefficient*LEVEL**4*data["rows"][n][r]
                formula = "82^4 E4 theta*e_"+str(anchor)+"; E4=1 modulo qY^55"
            else:
                for j, coefficient in enumerate(lambda_numerators):
                    if not coefficient:
                        continue
                    data = self.adapted(1, j)
                    sources.append({"M2_index": j, "lambda_index": j,
                        "integer_lambda_numerator": str(coefficient), "source": data["source"]})
                    for n in range(41, COUNT):
                        for r in range(REAL):
                            rows[n][r] += coefficient*LEVEL**6*data["rows"][n-41][r]
                formula = "82^6 qY^41 theta; xi^(10*41)=1"
            flat = [value for row in rows for value in row]
            assert any(flat), "A nonzero cleared global form cannot have 55 vanishing cusp coefficients."
            self.store(name, {"M6_index": index, "source_M6_recipe": M6_RECIPES[index],
                "source_original_M6": self.r775.source(M6), "theta_stage": self.theta_spec,
                "formula": formula, "component_sources": sources,
                "integer_numerators": [str(value) for value in flat],
                "common_denominator": str(denominator),
                "qY_count": COUNT, "full_real_coordinates": ROWS,
                "product_integer_scale": str(LEVEL**8),
                "lambda_denominator_preserved": True, "eta_shift_original_phase_is_one": index == 693,
                "old_M2_V2_V4_or_R805_pair_prefixes_recomputed": False})
            old = self.cached(name)
        assert old["M6_index"] == index and old["source_M6_recipe"] == M6_RECIPES[index]
        assert old["theta_stage"] == self.theta_spec and old["source_original_M6"] == self.r775.source(M6)
        assert old["lambda_denominator_preserved"] is True
        assert old["qY_count"] == COUNT and old["product_integer_scale"] == str(LEVEL**8)
        assert len(old["integer_numerators"]) == ROWS and int(old["common_denominator"]) > 0
        return old, file_spec(self.path(name))

    def run(self):
        final = self.out/FINAL
        if final.exists():
            certificate = read(final)
            assert certificate["result"] == RESULT and certificate["complete"] is True
            assert certificate["configuration"] == self.tag
            manifest = certificate["stage_manifest"]
            assert file_spec(self.out/manifest["file"]) == manifest
            for row in read(self.out/manifest["file"])["files"]:
                assert file_spec(self.out/row["file"]) == row
        else:
            self.modular_solver()
            targets, projections = [], []
            for j in range(5):
                target = self.projection_target(j)
                targets.append(target)
                projections.append(self.solve_one("E6-projection-j"+str(j), target[0], target[1], "projection"))
            cleared = {"692": self.residual_and_theta(projections, targets)}
            for index in (690, 691, 693):
                target, target_spec = self.member_target(index)
                result, spec = self.solve_one("M6-index-"+str(index), target, target_spec, "member")
                assert result["all1100_rows_verified"] is True
                cleared[str(index)] = spec
            new_tails = [file_spec(path) for path in sorted(self.out.glob("R807-new-pair-tail-*.json.gz"))]
            index_name = "R807-original-four-M6-pole-clearing-coordinate-index"
            payload = {"extra_M6_indices": [690, 691, 692, 693], "coordinate_stages": cleared,
                "theta_stage": self.theta_spec, "residual_kernel_stage": self.residual_spec,
                "original_V4_basis_index": self.basis_spec, "source_original_M6": self.r775.source(M6),
                "ordinary_V4_integer_scale": str(LEVEL**8), "original_M6_integer_scale": str(LEVEL**6),
                "original_theta_M2_integer_scale": str(LEVEL**2),
                "four_original_M6_recipes": {str(index): recipe for index, recipe in M6_RECIPES.items()},
                "all_four_members_verified_in_all1100_real_coordinates": True,
                "all_five_initial_columns_are_only_selected_row_projections": True,
                "actual_nonzero_theta_constructed": True,
                "new_pair_tail_stages": new_tails,
                "R803_mixed_coordinates_consumed": False, "theta_Uj_functions_computed": False}
            old = self.cached(index_name)
            if old is None:
                self.store(index_name, payload)
            else:
                for key, value in payload.items():
                    assert old[key] == value
            index_spec = file_spec(self.path(index_name))
            files = [file_spec(path) for path in sorted(self.out.glob("R807-*.json.gz"))
                     if path.name != "R807-stage-manifest.json.gz"]
            assert not any(row["file"].endswith("-dixon-current.json.gz") for row in files)
            manifest = self.store("R807-stage-manifest", {"files": files})
            residual = read(self.out/self.residual_spec["file"])
            certificate = {"result": RESULT, "complete": True, "p": P, "configuration": self.tag,
                "completed_scope": "four_extra_M6_rows_cleared", "V4_dimension": DIM,
                "qY_count": COUNT, "full_real_coordinate_rows": ROWS,
                "ordinary_V4_integer_scale": str(LEVEL**8),
                "actual_short_minor": {"prime": self.prime, "rank": DIM,
                    "determinant_mod_prime": self.minor["actual_determinant_mod_prime"],
                    "coordinate_row_indices": self.row_selection},
                "basis_index": self.basis_spec, "minor_stage": self.minor_spec,
                "projection_stages": [spec for data, spec in projections],
                "projection_target_stages": [spec for data, spec in targets],
                "residual_kernel_stage": self.residual_spec,
                "actual_residual_rank": residual["actual_rank"],
                "actual_residual_kernel_dimension": len(residual["full_nullspace_basis"]),
                "theta_stage": self.theta_spec,
                "theta_first_nonzero_original_M2_index": self.theta["first_nonzero_lambda_index"],
                "cleared_coordinate_stages": cleared, "cleared_coordinate_index": index_spec,
                "actual_nonzero_theta_constructed": True,
                "actual_M6_pole_clearing_computed": True,
                "five_selected_row_projections_exactly_verified": True,
                "all_four_M6_products_verified_in_all1100_rows": True,
                "global_degree1092_vs_cusp_order1100_bound_used": True,
                "rank_four_not_preassigned": True,
                "individual_five_target_membership_claimed": False,
                "exact_right_hand_sides_solved": 8, "ninth_rhs_for_M6_index692_solved": False,
                "actual_new_pair_tail_stages": new_tails,
                "old_M2_V2_V4_or_R805_pair_prefixes_recomputed": False,
                "characteristic_zero_inverse_matrix_formed": False,
                "R803_mixed_coordinates_consumed": False, "theta_Uj_functions_computed": False,
                "local_high_jets_computed": False, "primitive_multiplication_computed": False,
                "polar_divisors_eta_rigidification_or_height_computed": False,
                "stage_manifest": manifest, "seconds": time.monotonic()-self.started}
            save(final, certificate)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(final),
            "completed_scope": "four_extra_M6_rows_cleared",
            "actual_nonzero_theta_constructed": True, "actual_M6_pole_clearing_computed": True,
            "all_four_M6_products_verified_in_all1100_rows": True,
            "polar_divisors_eta_rigidification_or_height_computed": False})
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
            "complete_projections_theta_member_coordinates_and_current_lifts_preserved": True})
        raise


if __name__ == "__main__":
    sys.exit(main())
