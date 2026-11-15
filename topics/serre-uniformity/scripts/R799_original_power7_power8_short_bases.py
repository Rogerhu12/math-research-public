#!/usr/bin/env python3
"""R799: only the missing V6 interval and new minimal original V7/V8 bases."""
import argparse
from functools import lru_cache
import gzip
import hashlib
from itertools import combinations_with_replacement
import json
import math
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpz_poly, nmod_mat, nmod_poly

RESULT = "R799-original-power7-power8-short-bases"
FINAL = "p41-original-power7-power8-short-bases-certificate.json"
P, LEVEL, CYC, REAL = 41, 82, 40, 20
OLD_DIM, TAIL_FIRST, TAIL_STOP = 1506, 82, 109
ANCHORS, DIMENSIONS, BOUNDS = (0, 1, 73), {7: 1778, 8: 2050}, {7: 95, 8: 108}
ELL, XI = 739, 538
PROOF_SHA = "ca6abba83ba9bb0c843f3ef37b6fe3f703c380bc7e0be3339c05df9a7b7a54b4"
METHOD_SHA = "d1e489cdf8dfeb2b7fc2607e10831b599b6dcd8b20330e554b9e8203020133f9"
R775_POWER6 = "R775-basis-power-6.json.gz"
R775_POWER6_SHA = "05c5580b73eeba72b832e2a871221c19c482baf1c9656cab62a0c2c694ffafa1"
PRODUCERS = {
    "R775": {"result": "R775-p41-original-K-defined-RR-bases",
        "run_id": "43679160495", "source_commit": "032899cc3bcd937497a857df0c271261fc709ae5",
        "manifest_sha256": "c563b43979633152cf2dd58bc7127a0bd138edf3cccef6b51ba629b4851d6906",
        "core_sha256": "8b02496a1809e1f11e90bad84df1a4fa3a39ac6ad615f7871115b0988d2af4ee",
        "certificate_sha256": "ce92a3aacd8a1c6f44bef82b6890bb00298d9b1ea1fc2b8caf1af1cce7c1d203"},
    "R786": {"result": "R786-exact-original-power5-short-basis",
        "run_id": "43682100611", "source_commit": "dd262672a8b1e2af82277b15e0fa766038609670",
        "manifest_sha256": "e3c29e85236c8cc665bdf88e9ffd2bbab9180b6f977f0b2b22f54266762f405a",
        "core_sha256": "4508095a95a2bcaec8c8db8fcd550fbc618b017d2bc0007945783bc109dbf851",
        "certificate_sha256": "dc6c23568f80b861d839280846c3250063abdfb2716a20481779816bb7cd37d9"},
    "R795": {"result": "R795-exact-original-power6-short-basis",
        "run_id": "43692029484", "source_commit": "ac6d8fff1e1905539339bf1bec39365fd62312ba",
        "manifest_sha256": "fb4a8f656c66d5ae10dee052baab79c07b43c7e7f19bb66b6e7d71be13b83ada",
        "core_sha256": "2a338672b32a9d760a78b234a0df08f05c10eb4ba513a2a3e3759f1e6e6b7aac",
        "certificate_sha256": "c5cffbd3979b5cd04e1e66c8c132de64974d81caf3b542e97a7a5ce479e3b0ae"}}


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematical execution belongs to public repository Actions.")


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


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
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb", mtime=0, compresslevel=2) as out:
                out.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def plain_spec(row):
    return {key: row[key] for key in ("file", "bytes", "sha256")}


def matrix_rows(matrix):
    return [[int(matrix[i, j]) for j in range(matrix.ncols())] for i in range(matrix.nrows())]


def pivot_columns(matrix):
    reduced, rank = matrix.rref()
    pivots = [next(j for j in range(reduced.ncols()) if reduced[i, j]) for i in range(rank)]
    assert pivots == sorted(set(pivots))
    return pivots


def is_prime(value):
    return value >= 2 and all(value % d for d in range(2, math.isqrt(value)+1))


def next_prime(value):
    value += 1
    while not is_prime(value) or LEVEL % value == 0:
        value += 1
    return value


def pack(rows, stride, prime=None):
    assert rows and stride >= CYC
    values = [0]*(stride*(len(rows)-1)+CYC)
    for n, row in enumerate(rows):
        assert len(row) == CYC
        for r, value in enumerate(row):
            value = int(value)
            values[n*stride+r] = value if prime is None else value % prime
    return fmpz_poly(values) if prime is None else nmod_poly(values, prime)


def unpack(product, count, stride, max_xi_degree, prime=None):
    assert max_xi_degree < stride
    answer = []
    for n in range(count):
        cyclic = [0]*P
        for r in range(max_xi_degree+1):
            cyclic[r % P] += int(product[n*stride+r])
        row = [cyclic[r]-cyclic[40] for r in range(CYC)]
        answer.append(row if prime is None else [value % prime for value in row])
    return answer


def band_rectangles(a, b, c, d):
    """Disjoint rectangles containing exactly pairs 82 <= i+j < 109."""
    low, high = a+c, b+d-2
    if a >= b or c >= d or high < TAIL_FIRST or low >= TAIL_STOP:
        return
    if TAIL_FIRST <= low and high < TAIL_STOP:
        yield a, b, c, d
        return
    if b-a >= d-c:
        middle = (a+b)//2
        assert a < middle < b
        yield from band_rectangles(a, middle, c, d)
        yield from band_rectangles(middle, b, c, d)
    else:
        middle = (c+d)//2
        assert c < middle < d
        yield from band_rectangles(a, b, c, middle)
        yield from band_rectangles(a, b, middle, d)


class Retained:
    def __init__(self, directory, label, spec):
        self.directory, self.spec = Path(directory)/label, spec
        expected = PRODUCERS[label]
        for key in ("result", "run_id", "source_commit", "manifest_sha256", "core_sha256"):
            assert str(spec[key]) == expected[key]
        mp = self.directory/"full-outputs-manifest.json"
        assert sha(mp) == spec["manifest_sha256"]
        manifest = read(mp)
        assert manifest["result"] == spec["result"]
        self.files = {row["file"]: row for row in manifest["files"]}
        assert len(self.files) == len(manifest["files"])
        run, core, initial = (self.raw(name) for name in
            ("run-receipt.json", "core-receipt.json", "public-actions-input.json"))
        assert run["result"] == spec["result"] and run["complete"] is True
        assert run["process_exit_code"] == 0 and str(run["workflow_run_id"]) == str(spec["run_id"])
        assert run["source_commit"] == spec["source_commit"]
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        assert core["complete"] is True and core["source_sha256"] == spec["core_sha256"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["result"] == spec["result"] and initial["source_commit"] == spec["source_commit"]
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == spec["core_sha256"]
        self.initial = initial
        name = spec["certificate_name"]
        assert self.files[name]["sha256"] == expected["certificate_sha256"]
        assert self.files[name]["sha256"] == core["certificate_sha256"] == spec["files"][name]
        self.certificate = self.raw(name)
        assert self.certificate["complete"] is True and self.certificate["result"] == spec["result"]
        self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == spec["core_sha256"] and self.tag["python_flint"] == "0.9.0"

    def raw(self, name, expected=None):
        assert Path(name).name == name
        row = self.files[name]
        if expected is not None:
            assert row["sha256"] == expected
        if name in self.spec["files"]:
            assert row["sha256"] == self.spec["files"][name]
        path = self.directory/name
        assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
        return read(path)

    def get(self, name, expected=None):
        value = self.raw(name, expected)
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def get_spec(self, spec):
        assert self.files[spec["file"]]["bytes"] == spec["bytes"]
        return self.get(spec["file"], spec["sha256"])


class BudgetStop(RuntimeError):
    pass


class Job:
    def __init__(self, args):
        self.args, self.out, self.started = args, args.output, time.monotonic()
        self.out.mkdir(parents=True, exist_ok=True)
        self.config = read(args.config)
        assert flint.__version__ == "0.9.0"
        assert self.config["producer_inputs_pending"] is False
        assert self.config["result"] == RESULT and self.config["p"] == P
        assert self.config["core_sha256"] == sha(__file__)
        assert sha(args.proof) == self.config["R799_proof_sha256"] == PROOF_SHA
        assert sha(args.method) == self.config["R799_method_sha256"] == METHOD_SHA
        assert self.config["power6_new_interval"] == [TAIL_FIRST, TAIL_STOP]
        assert self.config["new_basis_dimensions"] == {str(k): v for k, v in DIMENSIONS.items()}
        assert self.config["new_basis_bounds_qY"] == {str(k): v for k, v in BOUNDS.items()}
        assert self.config["anchor_indices"] == list(ANCHORS)
        assert self.config["auxiliary_prime_start"] == ELL
        assert self.config["auxiliary_prime_policy"] == "ascending primes from739; omit divisors of82"
        assert self.config["selection_batch_size"] == 64
        assert set(self.config["retained_artifacts"]) == set(PRODUCERS)
        self.r775, self.r786, self.r795 = (Retained(args.retained, label, self.config["retained_artifacts"][label])
                                          for label in ("R775", "R786", "R795"))
        for label in ("R775", "R786"):
            assert self.r795.initial["job"]["retained_artifacts"][label] == self.config["retained_artifacts"][label]
            assert self.r795.tag["retained_artifacts"][label] == self.config["retained_artifacts"][label]
        c775 = self.r775.certificate
        assert c775["power_basis_dimensions"]["6"] == OLD_DIM
        assert c775["all_recipes_defined_over_original_K"] is True
        stages775 = {row["file"]: row for row in c775["stages"]}
        assert stages775[R775_POWER6]["sha256"] == R775_POWER6_SHA
        self.original_basis = self.r775.get_spec(stages775[R775_POWER6])
        assert self.original_basis["rank"] == len(self.original_basis["basis"]) == OLD_DIM
        assert self.original_basis["characteristic_zero_independence_certified_by_unit_reduction"] is True
        assert self.original_basis["coefficient_bound"] >= 1632
        old_minor = self.original_basis["actual_nonzero_minor"]
        assert old_minor["prime"] == ELL and int(old_minor["determinant_mod_ell"]) == 297
        assert old_minor["rows"] == old_minor["columns"] == OLD_DIM
        assert self.r775.tag["prime"] == ELL and self.r775.tag["xi41_mod_ell"] == XI
        for row in self.original_basis["basis"]:
            recipe = row["recipe"]
            assert recipe["kind"] == "product" and recipe["left_power"] == 1 and recipe["right_power"] == 5
            assert recipe["left_index"] in ANCHORS and 0 <= recipe["right_index"] < 1234
        assert sorted({row["recipe"]["left_index"] for row in self.original_basis["basis"]}) == list(ANCHORS)
        c786 = self.r786.certificate
        assert c786["basis_in_original_R775_saved_order"] is True
        assert c786["exact_power5_basis_dimension"] == 1234 and c786["exact_K_basis_prefix_bound_qY"] == 128
        self.index786 = self.r786.get_spec(c786["basis_index"])
        self.stages786 = {row["file"]: row for row in self.r786.get_spec(c786["stages_manifest"])["files"]}
        assert self.index786["dimension"] == len(self.index786["basis_rows"]) == 1234
        assert [row["index"] for row in self.index786["basis_rows"]] == list(range(1234))
        for name in ("R775-basis-M2.json.gz", "R775-basis-power-5.json.gz"):
            assert self.r786.tag["R775_completed_prefix_producer"]["files"][name] == stages775[name]["sha256"]
        c795 = self.r795.certificate
        assert c795["exact_power6_basis_dimension"] == OLD_DIM and c795["exact_K_basis_prefix_bound_qY"] == 81
        assert c795["basis_integer_scale"] == str(LEVEL**12) and c795["basis_in_original_R775_saved_order"] is True
        assert c795["all_original_R775_mod739_short_series_compared"] is True
        assert c795["all_original_real_cyclotomic_transports_verified"] is True
        self.index795 = self.r795.get_spec(c795["basis_index"])
        self.stages795 = {row["file"]: row for row in self.r795.get_spec(c795["stage_manifest"])["files"]}
        assert self.index795["dimension"] == len(self.index795["basis_rows"]) == OLD_DIM
        assert [row["index"] for row in self.index795["basis_rows"]] == list(range(OLD_DIM))
        self.tag = {"result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "R799_proof_sha256": sha(args.proof), "R799_method_sha256": sha(args.method),
            "retained_artifacts": self.config["retained_artifacts"], "p": P, "level": LEVEL,
            "power6_new_interval": [TAIL_FIRST, TAIL_STOP], "power6_integer_scale": str(LEVEL**12),
            "new_basis_dimensions": {str(k): v for k, v in DIMENSIONS.items()},
            "new_basis_bounds_qY": {str(k): v for k, v in BOUNDS.items()},
            "new_basis_integer_scales": {str(k): str(LEVEL**(2*k)) for k in DIMENSIONS},
            "anchor_indices": list(ANCHORS), "auxiliary_prime_start": ELL,
            "auxiliary_prime_policy": self.config["auxiliary_prime_policy"], "selection_batch_size": 64,
            "candidate_order": "power7 anchor then original V6 index; power8 unordered anchor pair then V6 index",
            "real_coordinate_count": REAL, "v_parameter": "v=xi41^-10*qY", "t_parameter": "t=xi41+xi41^-1",
            "old_power6_prefix_or_E1_M2_lower_power_arithmetic_recomputed": False}
        t = fmpz_poly([0, 1])
        chebyshev = [fmpz_poly([2]), t]
        for _ in range(2, 21):
            chebyshev.append(t*chebyshev[-1]-chebyshev[-2])
        modulus = fmpz_poly([1])
        for value in chebyshev[1:]:
            modulus += value
        assert modulus.degree() == REAL and modulus[REAL] == 1
        self.real_change = []
        for value in chebyshev:
            value %= modulus
            self.real_change.append([(j, int(value[j])) for j in range(REAL) if value[j]])
        self.rectangles = tuple(band_rectangles(0, TAIL_STOP, 0, TAIL_STOP))
        assert all(TAIL_FIRST <= a+c and b+d-2 < TAIL_STOP for a, b, c, d in self.rectangles)
        self.xipowers = [pow(XI, r, ELL) for r in range(CYC)]

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes:
            raise BudgetStop("Completed tails, exact candidates and modular progress retained for immediate continuation.")

    def path(self, name):
        assert name.startswith("R799-") and Path(name).name == name
        return self.out/(name+".json.gz")

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

    def stored_spec(self, spec):
        path = self.out/spec["file"]
        assert Path(spec["file"]).name == spec["file"]
        assert path.stat().st_size == spec["bytes"] and sha(path) == spec["sha256"]
        value = read(path)
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def factor_spec(self, power, index):
        name = "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"
        row = self.stages786[name]
        if power == 5:
            assert plain_spec(self.index786["basis_rows"][index]) == plain_spec(row)
        return plain_spec(row)

    @lru_cache(maxsize=24)
    def factor(self, power, index):
        assert (power == 1 and index in ANCHORS) or (power == 5 and 0 <= index < 1234)
        row = self.r786.get_spec(self.factor_spec(power, index))
        assert row["weight"] == 2*power and row["bound_qY"] == 128
        assert row["integer_scale"] == str(LEVEL**(2*power))
        assert row["original_R775_finite_coefficients_verified"] is True
        values = row["integer_qY_xi_coefficients"]
        assert len(values) == 129 and all(len(v) == CYC for v in values)
        return tuple(tuple(int(v) for v in row) for row in values[:TAIL_STOP])

    def prefix_spec(self, index):
        row = self.index795["basis_rows"][index]
        assert row["index"] == index
        assert row["file"] == "R795-exact-power-6-row-"+str(index).zfill(4)+".json.gz"
        assert plain_spec(row) == plain_spec(self.stages795[row["file"]])
        return plain_spec(row)

    @lru_cache(maxsize=24)
    def prefix(self, index):
        row = self.r795.get_spec(self.prefix_spec(index))
        recipe = self.original_basis["basis"][index]["recipe"]
        assert row["index"] == index and row["recipe"] == recipe
        assert row["weight"] == 12 and row["bound_qY"] == 81 and row["integer_scale"] == str(LEVEL**12)
        assert row["original_R775_finite_coefficients_verified"] is True
        assert row["all_original_phase_involutions_verified"] is True and row["averaging_used"] is False
        factors = row["original_R786_factor_rows"]
        assert len(factors) == 2
        for factor, power, j in zip(factors, (1, 5), (recipe["left_index"], recipe["right_index"])):
            assert factor["power"] == power and factor["index"] == j
            assert plain_spec(factor) == self.factor_spec(power, j)
        values = row["integer_qY_xi_coefficients"]
        assert len(values) == TAIL_FIRST and all(len(v) == CYC for v in values)
        assert len(row["integer_v_t_coefficients"]) == TAIL_FIRST
        return tuple(tuple(int(v) for v in line) for line in values)

    def real_coordinates(self, rows, first=0, prime=None):
        answer = []
        for n, values in enumerate(rows, first):
            cyclic = [0]*P
            for r, value in enumerate(values):
                cyclic[(r+10*n) % P] += value
            reduced = [value-cyclic[40] for value in cyclic[:40]]+[0]
            if prime is not None:
                reduced = [value % prime for value in reduced]
            assert all(reduced[r] == reduced[P-r] for r in range(1, 21)), (n, "original phase involution")
            real = [reduced[0]]+[0]*(REAL-1)
            for r in range(1, 21):
                scalar = reduced[r]
                if scalar:
                    for j, value in self.real_change[r]:
                        real[j] += scalar*value
            answer.append(real if prime is None else [value % prime for value in real])
        return answer

    @lru_cache(maxsize=None)
    def anchor_segment(self, index, first, stop):
        return pack(self.factor(1, index)[first:stop], 79)

    def tail_name(self, index):
        return "R799-original-power6-tail-row-"+str(index).zfill(4)

    def tail(self, index):
        name = self.tail_name(index)
        old = self.cached(name)
        recipe = self.original_basis["basis"][index]["recipe"]
        if old:
            assert old["index"] == index and old["recipe"] == recipe
            assert old["old_R795_prefix"] == self.prefix_spec(index)
            return file_spec(self.path(name))
        self.budget()
        self.prefix(index)  # Bind the original row and factors, without any old convolution.
        right = self.factor(5, recipe["right_index"])
        right_packs, product = {}, fmpz_poly([])
        for a, b, c, d in self.rectangles:
            key = (c, d)
            if key not in right_packs:
                right_packs[key] = pack(right[c:d], 79)
            piece = self.anchor_segment(recipe["left_index"], a, b)*right_packs[key]
            product += piece.left_shift(79*(a+c-TAIL_FIRST))
        assert product.length() <= 79*(TAIL_STOP-TAIL_FIRST)
        rows = unpack(product, TAIL_STOP-TAIL_FIRST, 79, 78)
        finite = self.original_basis["basis"][index]["coefficients_mod_ell"]
        finite_scale = pow(LEVEL, 12, ELL)
        for n, values in enumerate(rows, TAIL_FIRST):
            assert sum(a*b for a, b in zip(values, self.xipowers)) % ELL == \
                   finite_scale*(int(finite[n]) if n < len(finite) else 0) % ELL, (index, n, "old R775 finite tail")
        return self.store(name, {"index": index, "recipe": recipe, "weight": 12,
            "first_exponent": TAIL_FIRST, "last_exponent_exclusive": TAIL_STOP,
            "integer_scale": str(LEVEL**12),
            "integer_qY_xi_coefficients": [[str(v) for v in row] for row in rows],
            "integer_v_t_coefficients": [[str(v) for v in row] for row in self.real_coordinates(rows, TAIL_FIRST)],
            "old_R795_prefix": self.prefix_spec(index),
            "original_R786_factor_rows": [dict(self.factor_spec(power, j), power=power, index=j)
                for power, j in ((1, recipe["left_index"]), (5, recipe["right_index"]))],
            "band_rectangle_count": len(self.rectangles), "original_R775_mod739_tail_verified": True,
            "all_original_phase_involutions_verified": True, "old_prefix_recomputed": False,
            "old_prefix_bytes_modified": False, "old_factor_rows_recomputed": False})

    def tails(self):
        name = "R799-original-power6-tail-index"
        old = self.cached(name)
        if old:
            assert old["dimension"] == OLD_DIM and old["first_exponent"] == TAIL_FIRST
            assert old["last_exponent_exclusive"] == TAIL_STOP
            for row in old["basis_rows"]:
                self.stored_spec(row)
            self.tail_rows = old["basis_rows"]
            return file_spec(self.path(name))
        rows = []
        for index in range(OLD_DIM):
            rows.append(dict(self.tail(index), index=index))
            if index % 32 == 0 or index+1 == OLD_DIM:
                print(json.dumps({"stage": "only_V6_q82_to108", "rows": index+1,
                                  "total": OLD_DIM, "seconds": time.monotonic()-self.started}), flush=True)
        self.tail_rows = rows
        return self.store(name, {"dimension": OLD_DIM, "ordinary_power": 6, "basis_rows": rows,
            "first_exponent": TAIL_FIRST, "last_exponent_exclusive": TAIL_STOP,
            "integer_scale": str(LEVEL**12), "old_prefix_recomputed": False,
            "three_anchor_basepoint_free_input": {"indices": list(ANCHORS), "original_basis_size": OLD_DIM,
                "all_original_recipes_in_A_times_V5_verified": True, "proof": "R799 Corollary799.4"}})

    @lru_cache(maxsize=64)
    def power6(self, index):
        tail = self.stored_spec(self.tail_rows[index])
        assert tail["index"] == index and tail["old_R795_prefix"] == self.prefix_spec(index)
        assert tail["first_exponent"] == TAIL_FIRST and tail["last_exponent_exclusive"] == TAIL_STOP
        rows = tail["integer_qY_xi_coefficients"]
        assert len(rows) == TAIL_STOP-TAIL_FIRST and all(len(row) == CYC for row in rows)
        return self.prefix(index)+tuple(tuple(int(v) for v in row) for row in rows)

    @lru_cache(maxsize=128)
    def packed_power6(self, index, stride, count, prime):
        return pack(self.power6(index)[:count], stride, prime)

    @lru_cache(maxsize=48)
    def packed_anchor(self, anchor, stride, count, prime):
        return pack(self.factor(1, anchor)[:count], stride, prime)

    @lru_cache(maxsize=36)
    def packed_pair(self, left, right, count, prime):
        return self.packed_anchor(left, 121, count, prime).mul_low(
            self.packed_anchor(right, 121, count, prime), 121*count)

    def candidate_recipe(self, power, group, index):
        if power == 7:
            return {"kind": "product", "left_power": 1, "left_index": group[0],
                    "right_power": 6, "right_index": index}
        return {"kind": "triple_product", "anchor_indices": list(group),
                "anchor_powers": [1, 1], "right_power": 6, "right_index": index}

    def candidate_name(self, power, group, index):
        return "R799-power"+str(power)+"-candidate-a"+"-".join(str(a).zfill(3) for a in group)+"-j"+str(index).zfill(4)

    def candidate_product(self, power, group, index, prime=None):
        count = BOUNDS[power]+1
        stride = 79 if power == 7 else 121
        left = self.packed_anchor(group[0], stride, count, prime) if power == 7 else \
               self.packed_pair(group[0], group[1], count, prime)
        product = left.mul_low(self.packed_power6(index, stride, count, prime), stride*count)
        return unpack(product, count, stride, 78 if power == 7 else 117, prime)

    def candidate_mod(self, power, group, index, prime):
        old = self.cached(self.candidate_name(power, group, index))
        if old:
            assert old["recipe"] == self.candidate_recipe(power, group, index)
            assert old["ordinary_power"] == power and old["bound_qY"] == BOUNDS[power]
            rows = old["integer_v_t_coefficients"]
            assert len(rows) == BOUNDS[power]+1 and all(len(row) == REAL for row in rows)
            return [int(value) % prime for row in rows for value in row]
        rows = self.real_coordinates(self.candidate_product(power, group, index, prime), prime=prime)
        return [value for row in rows for value in row]

    def candidate_exact(self, power, group, index, prime, expected):
        name = self.candidate_name(power, group, index)
        recipe = self.candidate_recipe(power, group, index)
        old = self.cached(name)
        if old:
            assert old["ordinary_power"] == power and old["recipe"] == recipe
            real = old["integer_v_t_coefficients"]
            assert [int(v) % prime for row in real for v in row] == expected
            return file_spec(self.path(name))
        self.budget()
        rows = self.candidate_product(power, group, index)
        real = self.real_coordinates(rows)
        assert [v % prime for row in real for v in row] == expected, (power, group, index, "all modular coordinates")
        return self.store(name, {"ordinary_power": power, "recipe": recipe, "weight": 2*power,
            "bound_qY": BOUNDS[power], "integer_scale": str(LEVEL**(2*power)),
            "integer_qY_xi_coefficients": [[str(v) for v in row] for row in rows],
            "integer_v_t_coefficients": [[str(v) for v in row] for row in real],
            "original_M2_anchors": [dict(self.factor_spec(1, a), index=a) for a in group],
            "original_R795_power6_prefix": self.prefix_spec(index),
            "new_R799_power6_tail": plain_spec(self.tail_rows[index]),
            "initial_selection_prime": prime, "all_initial_modular_coordinates_verified": True,
            "all_original_phase_involutions_verified": True,
            "packing_stride": 79 if power == 7 else 121,
            "old_input_arithmetic_recomputed": False, "unrequested_high_coefficients_generated": False})

    def augment(self, state, vectors, dimension):
        """Extend an exact modular row span, without re-eliminating old columns."""
        prime, old_rows, old_pivots = state["prime"], state["echelon_rows"], state["pivot_coordinates"]
        batch = nmod_mat(vectors, prime)
        if old_rows:
            previous = nmod_mat(old_rows, prime)
            coefficients = nmod_mat([[row[j] for j in old_pivots] for row in vectors], prime)
            residual = batch-coefficients*previous
        else:
            previous, residual = None, batch
        selected = pivot_columns(residual.transpose())
        assert state["rank"]+len(selected) <= dimension
        if not selected:
            return [], old_rows, old_pivots
        independent = nmod_mat([[int(residual[i, j]) for j in range(residual.ncols())] for i in selected], prime)
        new_basis, new_rank = independent.rref()
        assert new_rank == len(selected)
        new_pivots = [next(j for j in range(new_basis.ncols()) if new_basis[i, j]) for i in range(new_rank)]
        assert not set(new_pivots) & set(old_pivots)
        new_rows = matrix_rows(new_basis)
        if previous is not None:
            coefficients = nmod_mat([[int(previous[i, j]) for j in new_pivots]
                                     for i in range(previous.nrows())], prime)
            old_rows = matrix_rows(previous-coefficients*new_basis)
        combined = sorted(zip(old_pivots+new_pivots, old_rows+new_rows))
        return selected, [row for _, row in combined], [pivot for pivot, _ in combined]

    def selection(self, power, anchors):
        index_name = "R799-original-power"+str(power)+"-basis-index"
        old_index = self.cached(index_name)
        if old_index:
            assert old_index["dimension"] == DIMENSIONS[power] and old_index["bound_qY"] == BOUNDS[power]
            for row in old_index["basis_rows"]:
                self.stored_spec(row)
            return file_spec(self.path(index_name)), old_index
        groups = [(a,) for a in anchors] if power == 7 else list(combinations_with_replacement(anchors, 2))
        progress_name = "R799-power"+str(power)+"-selection-progress"
        pending_name = "R799-power"+str(power)+"-selection-pending"
        dimension, coordinate_count = DIMENSIONS[power], REAL*(BOUNDS[power]+1)
        total, state = len(groups)*OLD_DIM, self.cached(progress_name)
        if state is None:
            state = {"ordinary_power": power, "prime": ELL, "rank": 0, "cursor": 0,
                "anchor_indices": list(anchors), "coordinate_count": coordinate_count,
                "expected_dimension": dimension, "selected": [], "pivot_coordinates": [],
                "echelon_rows": [], "basis_complete": False, "bad_prime_states": []}
            self.store(progress_name, state)
        while state["rank"] < dimension:
            assert state["ordinary_power"] == power and state["anchor_indices"] == list(anchors)
            assert state["coordinate_count"] == coordinate_count and state["expected_dimension"] == dimension
            assert state["rank"] == len(state["selected"]) == len(state["echelon_rows"]) == len(state["pivot_coordinates"])
            assert is_prime(state["prime"]) and LEVEL % state["prime"]
            pending = self.cached(pending_name)
            if pending and state["cursor"] == pending["next_cursor"]:
                # A hard stop can occur after atomic progress commit but before pending unlink.
                assert state["prime"] == pending["prime"]
                self.path(pending_name).unlink()
                pending = None
            if state["cursor"] == total:
                assert not self.path(pending_name).exists()
                bad_name = "R799-power"+str(power)+"-bad-prime-"+str(state["prime"])
                bad = self.store(bad_name, dict(state, only_modular_rank_deficiency=True,
                                               characteristic_zero_basepoint_claim=False))
                state = {"ordinary_power": power, "prime": next_prime(state["prime"]), "rank": 0,
                    "cursor": 0, "anchor_indices": list(anchors), "coordinate_count": coordinate_count,
                    "expected_dimension": dimension, "selected": [], "pivot_coordinates": [],
                    "echelon_rows": [], "basis_complete": False,
                    "bad_prime_states": state["bad_prime_states"]+[bad]}
                self.store(progress_name, state)
                self.packed_power6.cache_clear()
                self.packed_anchor.cache_clear()
                self.packed_pair.cache_clear()
                continue
            if pending is None:
                self.budget()
                cursor = state["cursor"]
                end = min(cursor+64, (cursor//OLD_DIM+1)*OLD_DIM, total)
                candidates, vectors = [], []
                for position in range(cursor, end):
                    group, index = groups[position//OLD_DIM], position % OLD_DIM
                    candidates.append({"candidate_position": position, "group": list(group), "original_V6_index": index})
                    vectors.append(self.candidate_mod(power, group, index, state["prime"]))
                selected, new_rows, new_pivots = self.augment(state, vectors, dimension)
                pending = {"ordinary_power": power, "prime": state["prime"],
                    "previous_progress": file_spec(self.path(progress_name)), "next_cursor": end,
                    "new_echelon_rows": new_rows, "new_pivot_coordinates": new_pivots,
                    "new_candidates": [dict(candidates[i], modular_coordinates=vectors[i]) for i in selected],
                    "modular_batch_arithmetic_complete": True, "new_exact_acceptances_complete": False}
                self.store(pending_name, pending)
            assert pending["prime"] == state["prime"] and pending["ordinary_power"] == power
            assert pending["previous_progress"] == file_spec(self.path(progress_name))
            accepted = []
            for candidate in pending["new_candidates"]:
                group, index = tuple(candidate["group"]), candidate["original_V6_index"]
                actual = self.candidate_exact(power, group, index, state["prime"], candidate["modular_coordinates"])
                accepted.append(dict(actual, candidate_position=candidate["candidate_position"],
                    recipe=self.candidate_recipe(power, group, index), all_current_prime_coordinates_verified=True))
            state = dict(state, cursor=pending["next_cursor"], rank=state["rank"]+len(accepted),
                selected=state["selected"]+accepted, echelon_rows=pending["new_echelon_rows"],
                pivot_coordinates=pending["new_pivot_coordinates"])
            self.store(progress_name, state)
            self.path(pending_name).unlink()
            print(json.dumps({"stage": "V"+str(power)+"_actual_modular_selection", "prime": state["prime"],
                "rank": state["rank"], "target": dimension, "candidates_scanned": state["cursor"],
                "candidate_limit": total, "seconds": time.monotonic()-self.started}), flush=True)
        if self.path(pending_name).exists():
            pending = self.cached(pending_name)
            assert state["cursor"] == pending["next_cursor"] and state["prime"] == pending["prime"]
            self.path(pending_name).unlink()
        prime, pivots = state["prime"], state["pivot_coordinates"]
        assert len(pivots) == dimension and len(set(pivots)) == dimension
        rows, square = [], []
        for index, selected in enumerate(state["selected"]):
            rows.append(dict(selected, index=index))
        if state["basis_complete"]:
            minor = state["actual_nonzero_minor"]
            assert minor["prime"] == prime and minor["coordinate_row_indices"] == pivots
            assert minor["rows"] == minor["columns"] == dimension and minor["determinant_mod_prime"] % prime
        else:
            self.budget()
            for selected in state["selected"]:
                data = self.stored_spec(selected)
                flat = [int(v) % prime for row in data["integer_v_t_coefficients"] for v in row]
                assert len(flat) == coordinate_count
                square.append([flat[j] for j in pivots])
            determinant = int(nmod_mat(square, prime).det())
            assert determinant % prime, (power, "actual new nonzero full coordinate minor")
            minor = {"prime": prime, "rows": dimension, "columns": dimension,
                "coordinate_row_indices": pivots, "selected_basis_column_indices": list(range(dimension)),
                "determinant_mod_prime": determinant,
                "coordinate_order": "n=0..bound_qY, t_power=0..19; index=20*n+t_power",
                "all_entries_from_saved_exact_integer_rows": True}
            state = dict(state, basis_complete=True, actual_nonzero_minor=minor)
            self.store(progress_name, state)
        used = list(anchors[:(state["cursor"]-1)//OLD_DIM+1]) if power == 7 else list(anchors)
        assert power != 7 or used in ([0, 1], [0, 1, 73])
        output = {"ordinary_power": power, "dimension": dimension, "bound_qY": BOUNDS[power],
            "integer_scale": str(LEVEL**(2*power)), "basis_rows": rows, "anchor_indices": used,
            "actual_nonzero_minor": minor, "candidate_cursor": state["cursor"],
            "candidate_order": self.tag["candidate_order"], "bad_prime_states": state["bad_prime_states"],
            "full_original_real_coordinates": REAL, "all_exact_rows_compared_with_selecting_modular_columns": True,
            "characteristic_zero_basis_certified": True,
            "short_prefix_injectivity": "20*(bound_qY+1)>272*ordinary_power",
            "basepoint_free_input": "actual original three-anchor V6 recipes; R799 Corollary799.4",
            "two_anchor_basepoint_free_certified_by_actual_minor": power == 7 and len(used) == 2}
        spec = self.store(index_name, output)
        return spec, output

    def run(self):
        final = self.out/FINAL
        if final.exists():
            cert = read(final)
            assert cert["result"] == RESULT and cert["complete"] is True and cert["configuration"] == self.tag
            inventory = self.stored_spec(cert["stage_manifest"])
            for row in inventory["files"]:
                path = self.out/row["file"]
                assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
        else:
            tails = self.tails()
            index7, data7 = self.selection(7, ANCHORS)
            index8, data8 = self.selection(8, tuple(data7["anchor_indices"]))
            manifest = self.store("R799-exact-stages-manifest", {"files": [file_spec(path)
                for path in sorted(self.out.glob("R799-*.json.gz"))
                if path.name != "R799-exact-stages-manifest.json.gz"]})
            cert = {"result": RESULT, "configuration": self.tag, "complete": True, "p": P,
                "power6_tail_dimension": OLD_DIM, "power6_new_interval": [TAIL_FIRST, TAIL_STOP],
                "new_exact_basis_dimensions": {"7": DIMENSIONS[7], "8": DIMENSIONS[8]},
                "new_exact_basis_bounds_qY": {"7": BOUNDS[7], "8": BOUNDS[8]},
                "all_original_power6_finite_tails_compared": True,
                "all_original_real_cyclotomic_transports_verified": True,
                "all_new_basis_rows_match_selecting_modular_columns": True,
                "three_original_anchor_basepoint_free_input_verified": True,
                "actual_anchor_indices": data7["anchor_indices"],
                "actual_new_nonzero_minors": {"7": data7["actual_nonzero_minor"], "8": data8["actual_nonzero_minor"]},
                "power6_tail_index": tails, "basis_indices": {"7": index7, "8": index8}, "stage_manifest": manifest,
                "old_power6_prefix_or_E1_M2_lower_power_arithmetic_recomputed": False,
                "power7_coefficients_after_qY95_or_power8_after_qY108_generated": False,
                "actual_original_function_polar_divisor_beta_eta_or_height_computed": False,
                "seconds": time.monotonic()-self.started}
            save(final, cert)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(final),
            "power6_new_interval": [TAIL_FIRST, TAIL_STOP], "new_basis_dimensions": {"7": 1778, "8": 2050},
            "new_basis_bounds_qY": {"7": 95, "8": 108},
            "actual_original_function_polar_divisor_beta_eta_or_height_computed": False})
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
            "completed_stages_preserved": True})
        raise


if __name__ == "__main__":
    sys.exit(main())
