#!/usr/bin/env python3
"""R796: source-bound original CM quadratic chart and incremental local jets.

Use retained R786 M2 q^0..27 and R790 values/first coarse jets.  Only public
repository Actions may execute new arithmetic.  A modular minor selects the
416 products; every one of the 144 resulting relations is verified over K.
"""
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
from flint import fmpq, fmpq_mat, fmpz, fmpz_mat, fmpz_poly, nmod_mat, nmod_poly

RESULT = "R796-original-CM-quadratic-chart"
FINAL = "p41-original-CM-quadratic-chart-certificate.json"
M2, WP, U2, PRODUCTS = 146, 145, 144, 416
ORDERS, XI, STRIDE = 28, 40, 80
ROWS = ORDERS*XI
M2_RECIPE_SHA = "51113988c90b301cb6117fec5c294b77110e1826bf00229b7993ba82144f5d3d"
PRODUCERS = {
    "R786": {
        "result": "R786-exact-original-power5-short-basis",
        "manifest": "e3c29e85236c8cc665bdf88e9ffd2bbab9180b6f977f0b2b22f54266762f405a",
        "certificate": "dc6c23568f80b861d839280846c3250063abdfb2716a20481779816bb7cd37d9",
        "certificate_name": "p41-exact-original-power5-short-basis-certificate.json",
        "core": "4508095a95a2bcaec8c8db8fcd550fbc618b017d2bc0007945783bc109dbf851",
        "stages_key": "stages_manifest"},
    "R790": {
        "result": "R790-original-CM-fiber-jets",
        "manifest": "49b5ccda0bbe3bc9d06a263fa3b15632f34b97ce518bc3825002583fb74afa60",
        "certificate": "672044345934c0fc16b81ec2e2eaeb2a3282fa785069d53e240845d26b65e1fd",
        "certificate_name": "p41-original-CM-fiber-jets-certificate.json",
        "core": "981eb543b791db416fad355d83eedb9bfe3b86b3e5461483fe4397e2129040b6",
        "stages_key": "stage_manifest"}}


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
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb", mtime=0, compresslevel=2) as out:
                out.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def eq(x):
    return [str(x.numer()), str(x.denom())]


def dq(x):
    return fmpq(int(x[0]), int(x[1]))


def ek(x):
    return [eq(x[0]), eq(x[1])]


def dk(x):
    return dq(x[0]), dq(x[1])


ZERO, ONE = (fmpq(0), fmpq(0)), (fmpq(1), fmpq(0))


def ka(a, b):
    return a[0]+b[0], a[1]+b[1]


def kn(a):
    return -a[0], -a[1]


def ks(a, b):
    return ka(a, kn(b))


def km(a, b):
    ac, bd = a[0]*b[0], a[1]*b[1]
    return ac-bd, a[0]*b[1]+a[1]*b[0]-bd


def ki(a):
    norm = a[0]*a[0]-a[0]*a[1]+a[1]*a[1]
    assert norm
    return (a[0]-a[1])/norm, -a[1]/norm


def kd(a, b):
    return km(a, ki(b))


def kscale(a, q):
    return a[0]*q, a[1]*q


def primitive(vector):
    denominator = 1
    for pair in vector:
        for q in pair:
            denominator = math.lcm(denominator, int(q.denom()))
    values = [[int((q*denominator).numer()) for q in pair] for pair in vector]
    content = 0
    for pair in values:
        for value in pair:
            content = math.gcd(content, abs(value))
    assert content
    scale = fmpq(denominator, content)
    answer = [(fmpq(pair[0]//content), fmpq(pair[1]//content)) for pair in values]
    assert all(kscale(a, scale) == b for a, b in zip(vector, answer))
    return answer, scale


def pivot_columns(matrix):
    reduced, rank = matrix.rref()
    pivots = [next(j for j in range(reduced.ncols()) if reduced[i, j]) for i in range(rank)]
    assert len(set(pivots)) == rank
    return pivots


def matrix_from_columns(columns, modulus=None):
    data = [list(row) for row in zip(*columns)]
    return nmod_mat(data, modulus) if modulus is not None else fmpz_mat(data)


def smatrix(matrix):
    return [[str(matrix[i, j]) for j in range(matrix.ncols())] for i in range(matrix.nrows())]


def zmatrix(data):
    return fmpz_mat([[int(x) for x in row] for row in data])


def selected_rows(matrix, indices):
    return fmpz_mat([[matrix[i, j] for j in range(matrix.ncols())] for i in indices])


def packed(flat, modular=None):
    values = [0]*(STRIDE*(ORDERS-1)+XI)
    for n in range(ORDERS):
        for r in range(XI):
            value = int(flat[n*XI+r])
            values[n*STRIDE+r] = value if modular is None else value % modular
    return fmpz_poly(values) if modular is None else nmod_poly(values, modular)


def reduced_flat(product, modular=None):
    # Phi_41=1+X+...+X^40, X^41=1. A product coefficient has degree <=78.
    answer = []
    for n in range(ORDERS):
        offset = n*STRIDE
        top = int(product[offset+40])
        for r in range(XI):
            value = int(product[offset+r])-top
            if r <= 37:
                value += int(product[offset+r+41])
            answer.append(value if modular is None else value % modular)
    return answer


class BudgetStop(RuntimeError):
    pass


class Retained:
    def __init__(self, directory, label, producer):
        expected = PRODUCERS[label]
        self.directory, self.producer = directory/label, producer
        manifest_path = self.directory/"full-outputs-manifest.json"
        assert sha(manifest_path) == producer["manifest_sha256"] == expected["manifest"]
        manifest = read(manifest_path)
        assert manifest["result"] == expected["result"] == producer["result"]
        self.entries = {row["file"]: row for row in manifest["files"]}
        name = expected["certificate_name"]
        assert producer["certificate_name"] == name
        assert sha(self.directory/name) == expected["certificate"] == producer["files"][name]
        self.certificate = read(self.directory/name)
        assert self.certificate["complete"] is True and self.certificate["result"] == expected["result"]
        self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == producer["core_sha256"] == expected["core"]
        assert self.tag["python_flint"] == "0.9.0"
        stage_spec = self.certificate[expected["stages_key"]]
        stage = self.get(stage_spec["file"], require_stage=False)
        assert sha(self.directory/stage_spec["file"]) == stage_spec["sha256"]
        assert (self.directory/stage_spec["file"]).stat().st_size == stage_spec["bytes"]
        self.stages = {row["file"]: row for row in stage["files"]}

    def get(self, name, require_stage=True):
        assert Path(name).name == name
        path = self.directory/name
        entry = self.entries[name]
        assert sha(path) == entry["sha256"] == self.producer["files"][name]
        assert path.stat().st_size == entry["bytes"]
        value = read(path)
        assert value["complete"] is True and value["configuration"] == self.tag
        if require_stage:
            assert self.stages[name]["sha256"] == entry["sha256"]
            assert self.stages[name]["bytes"] == entry["bytes"]
        return value


class Job:
    def __init__(self, args):
        self.args, self.out = args, args.output
        self.started = time.monotonic()
        self.deadline = self.started+args.budget_minutes*60-45
        self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        assert flint.__version__ == "0.9.0"
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert self.item["producer_inputs_pending"] is False
        assert sha(__file__) == self.item["core_sha256"]
        assert sha(args.proof) == self.item["R796_proof_sha256"]
        assert sha(args.method) == self.item["R796_method_sha256"]
        assert sha(args.rr_proof) == self.item["R793_proof_sha256"]
        assert self.item["requested_jet_length"] == args.target_length >= 2
        self.tag = {
            "result": RESULT, "p": 41, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "R796_proof_sha256": sha(args.proof), "R796_method_sha256": sha(args.method),
            "R793_proof_sha256": sha(args.rr_proof), "retained_artifacts": self.item["retained_artifacts"],
            "original_M2_recipe_sha256": M2_RECIPE_SHA,
            "cusp_coefficient_convention": "original integer xi41^0..39; qY^0..27; packed stride80",
            "cusp_highest_exponent": ORDERS-1, "CM_point": "original_P1", "coarse_coordinate": "a-1",
            "adapted_basis_policy": "first value and tangent anchors; primitive Z[zeta] columns",
            "monomial_order_policy": "lexicographic (a,b),0<=a<=b<=144",
            "auxiliary_prime_start": int(self.item.get("auxiliary_prime_start", 1000000007))}
        assert set(self.item["retained_artifacts"]) == {"R786", "R790"}
        self.R786 = Retained(args.retained, "R786", self.item["retained_artifacts"]["R786"])
        self.R790 = Retained(args.retained, "R790", self.item["retained_artifacts"]["R790"])
        assert self.R786.tag["R775_completed_prefix_producer"]["files"]["R775-basis-M2.json.gz"] == M2_RECIPE_SHA
        assert self.R790.tag["retained_artifacts"]["R775"]["files"]["R775-basis-M2.json.gz"] == M2_RECIPE_SHA
        cert790 = self.R790.certificate
        assert cert790["M2_dimension"] == M2 and cert790["cm_jet_order"] == 5
        assert cert790["original_psi_values_and_first_coarse_jets_verified"] is True
        assert cert790["original_M2_scale"] == "6724"
        self.rows, self.values, self.derivatives = [], [], []
        for i in range(M2):
            row = self.R786.get("R786-exact-power-1-row-"+str(i).zfill(4)+".json.gz")
            jet = self.R790.get("R790-M2-CM-jet-"+str(i).zfill(4)+".json.gz")
            assert row["weight"] == 2 and row["bound_qY"] == 128
            assert row["integer_scale"] == jet["integer_scale"] == "6724"
            assert row["recipe"] == jet["original_recipe"] and jet["index"] == i
            assert jet["M2_recipe_source_sha256"] == M2_RECIPE_SHA
            assert jet["R786_power1_scale_preserved"] is True
            coefficients = row["integer_qY_xi_coefficients"]
            assert len(coefficients) == 129 and all(len(r) == XI for r in coefficients)
            self.rows.append([int(x) for r in coefficients[:ORDERS] for x in r])
            self.values.append(dk(jet["value_K_1_zeta"]))
            self.derivatives.append(dk(jet["derivative_z_K_1_zeta"]))
        self.product_cache = {}
        self.candidate_pairs = [(a, b) for a in range(WP) for b in range(a, WP)]

    def check(self):
        if time.monotonic() >= self.deadline:
            raise BudgetStop("Resource budget reached at a complete source-bound stage.")

    def path(self, name):
        return self.out/(name if name.endswith(".json.gz") else name+".json.gz")

    def cache(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def store(self, name, payload):
        path = self.path(name)
        assert not path.exists(), "A completed mathematical stage is immutable: "+path.name
        value = dict(payload, result=RESULT, complete=True, configuration=self.tag)
        save(path, value)
        print(json.dumps({"stage": path.name, "sha256": sha(path), "complete": True}), flush=True)
        self.check()
        return value

    def adapt(self):
        name = "R796-original-CM-adapted-M2-basis"
        cached = self.cache(name)
        if cached:
            return cached
        i0 = next(i for i, value in enumerate(self.values) if value != ZERO)
        vt, dt = self.values[i0], self.derivatives[i0]
        ratios = [kd(v, vt) for v in self.values]
        tangents = [kd(ks(km(d, vt), km(v, dt)), km(vt, vt))
                    for v, d in zip(self.values, self.derivatives)]
        i1 = next(i for i, value in enumerate(tangents) if value != ZERO)
        tau = [ONE if i == i0 else ZERO for i in range(M2)]
        sigma = [ONE if i == i1 else kn(ratios[i1]) if i == i0 else ZERO for i in range(M2)]
        sigma, sigma_scale = primitive(sigma)
        lam = kscale(tangents[i1], sigma_scale)
        assert lam != ZERO
        columns = [tau, sigma]
        descriptions = [{"constant": ek(ONE), "linear": ek(ZERO), "x_index": None, "x_coefficient": ek(ZERO)}
                        for _ in range(M2)]
        descriptions[i0] = {"constant": ek(ONE), "linear": ek(ZERO), "x_index": None, "x_coefficient": ek(ZERO)}
        descriptions[i1] = {"constant": ek(ratios[i1]), "linear": ek((1/sigma_scale, fmpq(0))),
                            "x_index": None, "x_coefficient": ek(ZERO)}
        other = [i for i in range(M2) if i not in (i0, i1)]
        scales = [eq(sigma_scale)]
        for j, i in enumerate(other, start=1):
            beta = kd(tangents[i], lam)
            vector = [ks(ONE if k == i else ZERO,
                         ka(kscale(ratios[i], fmpq(int(k == i0))), km(beta, sigma[k])))
                      for k in range(M2)]
            vector, scale = primitive(vector)
            columns.append(vector)
            scales.append(eq(scale))
            descriptions[i] = {"constant": ek(ratios[i]), "linear": ek(beta),
                                "x_index": j, "x_coefficient": ek((1/scale, fmpq(0)))}
        assert len(columns) == M2 and len(other) == U2
        for j, column in enumerate(columns):
            value = ZERO
            derivative = ZERO
            for coefficient, v, d in zip(column, self.values, self.derivatives):
                value, derivative = ka(value, km(coefficient, v)), ka(derivative, km(coefficient, d))
            if j == 0:
                assert value == vt and derivative == dt
            elif j == 1:
                assert value == ZERO and kd(derivative, vt) == lam
            else:
                assert value == derivative == ZERO
        for i, desc in enumerate(descriptions):
            reconstructed = [ka(km(dk(desc["constant"]), tau[k]),
                                km(dk(desc["linear"]), sigma[k])) for k in range(M2)]
            if desc["x_index"] is not None:
                column = columns[desc["x_index"]+1]
                reconstructed = [ka(x, km(dk(desc["x_coefficient"]), c))
                                 for x, c in zip(reconstructed, column)]
            assert reconstructed == [ONE if k == i else ZERO for k in range(M2)]
        sparse = []
        for column in columns:
            entries = []
            for i, value in enumerate(column):
                if value != ZERO:
                    assert value[0].denom() == value[1].denom() == 1
                    entries.append({"original_index": i, "K_coefficient": ek(value)})
            sparse.append(entries)
        return self.store(name, {"tau_original_index": i0, "tangent_original_index": i1,
            "u_original_indices": other, "basis_sparse_columns": sparse,
            "primitive_scales_sigma_then_u": scales, "original_M2_ratio_decompositions": descriptions,
            "lambda_dt_dz_K_1_zeta": ek(lam), "tau_value_K_1_zeta": ek(vt),
            "all_value_and_first_jet_conditions_verified": True,
            "both_basis_change_identities_verified": True, "original_scale": "6724",
            "all_adapted_column_coefficients_in_Q": all(c[1] == 0 for col in columns for c in col)})

    def prefixes(self, adapted):
        name = "R796-adapted-original-M2-cusp-prefixes"
        value = self.cache(name)
        if value is None:
            rows = []
            for entries in adapted["basis_sparse_columns"]:
                a, b = [0]*ROWS, [0]*ROWS
                for entry in entries:
                    i = entry["original_index"]
                    coefficient = dk(entry["K_coefficient"])
                    c0, c1 = int(coefficient[0]), int(coefficient[1])
                    a = [x+c0*y for x, y in zip(a, self.rows[i])]
                    b = [x+c1*y for x, y in zip(b, self.rows[i])]
                rows.append([[str(x) for x in a], [str(x) for x in b]])
            value = self.store(name, {"adapted_basis_sha256": sha(self.path("R796-original-CM-adapted-M2-basis")),
                "bound_qY": ORDERS-1, "xi_coordinates": XI, "integer_scale": "6724",
                "rows_flat_K_integer_components": rows, "old_q_coefficients_recomputed": False})
        self.flat = [([int(x) for x in row[0]], [int(x) for x in row[1]])
                     for row in value["rows_flat_K_integer_components"]]
        self.polys = [(packed(a), packed(b)) for a, b in self.flat]
        assert len(self.flat) == M2
        self.pure_Q = adapted["all_adapted_column_coefficients_in_Q"]
        assert self.pure_Q == all(not any(b) for a, b in self.flat)

    def product_name(self, a, b):
        return "R796-quadratic-product-"+str(a).zfill(3)+"-"+str(b).zfill(3)

    def exact_product(self, a, b):
        key = (a, b)
        if key in self.product_cache:
            return self.product_cache[key]
        name = self.product_name(a, b)
        value = self.cache(name)
        if value is None:
            A, B = self.polys[a+1], self.polys[b+1]
            aa, bb = A[0]*B[0], A[1]*B[1]
            first = reduced_flat(aa-bb)
            second = reduced_flat(A[0]*B[1]+A[1]*B[0]-bb)
            value = self.store(name, {"WP_pair": [a, b], "bound_qY": ORDERS-1,
                "integer_scale": "45212176",
                "flat_K_integer_components": [[str(x) for x in first], [str(x) for x in second]]})
        assert value["WP_pair"] == [a, b]
        answer = tuple([int(x) for x in row] for row in value["flat_K_integer_components"])
        self.product_cache[key] = answer
        return answer

    def rhs(self):
        name = "R796-tau-times-second-order-basis"
        value = self.cache(name)
        if value is None:
            rows = []
            A = self.polys[0]
            for j in range(U2):
                B = self.polys[j+2]
                aa, bb = A[0]*B[0], A[1]*B[1]
                first = reduced_flat(aa-bb)
                second = reduced_flat(A[0]*B[1]+A[1]*B[0]-bb)
                rows.append([[str(x) for x in first], [str(x) for x in second]])
            value = self.store(name, {"rhs_order": "tau*u_1,...,tau*u_144",
                "bound_qY": ORDERS-1, "integer_scale": "45212176",
                "columns_flat_K_integer_components": rows})
        return tuple(matrix_from_columns([[int(x) for x in row[part]]
                     for row in value["columns_flat_K_integer_components"]]) for part in range(2))

    def select(self):
        final_name = "R796-WP2-selected-monomials"
        cached = self.cache(final_name)
        if cached:
            for pair in cached["WP_pairs"]:
                self.exact_product(*pair)
            return cached
        ell = self.tag["auxiliary_prime_start"]
        while True:
            self.check()
            while ell % 3 != 1 or not fmpz(ell).is_prime():
                ell += 1
            assert ell < 2**31
            prefix = "R796-prime-"+str(ell)
            if self.cache(prefix+"-rejected"):
                ell += 1
                continue
            root_stage = self.cache(prefix+"-root")
            if root_stage is None:
                roots = sorted(int(root) for root, multiplicity in nmod_poly([1, 1, 1], ell).roots())
                assert len(roots) == 2
                root_stage = self.store(prefix+"-root", {"prime": ell, "zeta_root": roots[0],
                    "other_zeta_root": roots[1], "prime_proved": True})
            root = root_stage["zeta_root"]
            completed = []
            for path in sorted(self.out.glob(prefix+"-round-*.json.gz")):
                stage = self.cache(path.name)
                completed.append(stage)
            if completed:
                last = completed[-1]
                selected = [tuple(pair) for pair in last["WP_pairs"]]
                processed, round_index = last["next_candidate"], last["round_index"]+1
                vectors = [[(a+root*b) % ell for a, b in zip(*self.exact_product(*pair))]
                           for pair in selected]
            else:
                selected, vectors, processed, round_index = [], [], 0, 0
            mods = [packed([(a+root*b) % ell for a, b in zip(A, B)], ell) for A, B in self.flat[1:]]
            while processed < len(self.candidate_pairs) and len(selected) < PRODUCTS:
                self.check()
                batch = self.candidate_pairs[processed:processed+64]
                trial_vectors = list(vectors)
                for a, b in batch:
                    trial_vectors.append(reduced_flat(mods[a]*mods[b], ell))
                trial_pairs = selected+batch
                pivots = pivot_columns(matrix_from_columns(trial_vectors, ell))
                assert len(pivots) <= PRODUCTS
                new_selected = [trial_pairs[i] for i in pivots]
                new_vectors = [trial_vectors[i] for i in pivots]
                for pair in new_selected:
                    if pair not in selected:
                        first, second = self.exact_product(*pair)
                        check = [(a+root*b) % ell for a, b in zip(first, second)]
                        assert check == new_vectors[new_selected.index(pair)]
                selected, vectors = new_selected, new_vectors
                processed += len(batch)
                self.store(prefix+"-round-"+str(round_index).zfill(4),
                    {"prime": ell, "zeta_root": root, "round_index": round_index,
                     "next_candidate": processed, "actual_rank": len(selected),
                     "WP_pairs": [list(pair) for pair in selected]})
                round_index += 1
            if len(selected) < PRODUCTS:
                self.store(prefix+"-rejected", {"prime": ell, "reason": "full finite product set lost rank",
                    "actual_modular_rank": len(selected), "theoretical_characteristic_zero_rank": PRODUCTS})
                ell += 1
                continue
            matrix = matrix_from_columns(vectors, ell)
            rows = pivot_columns(matrix.transpose())
            assert len(rows) == PRODUCTS
            minor = nmod_mat([[matrix[i, j] for j in range(PRODUCTS)] for i in rows], ell)
            determinant = int(minor.det())
            assert determinant
            return self.store(final_name, {"prime": ell, "zeta_root": root,
                "WP_pairs": [list(pair) for pair in selected], "actual_modular_rank": PRODUCTS,
                "minor_rows": rows, "minor_determinant_mod_prime": determinant,
                "actual_candidate_count_scanned": processed, "full_candidate_count": len(self.candidate_pairs),
                "characteristic_zero_independence_certified_by_nonzero_minor": True,
                "two_branch_Dixon_or_composite_modulus_inverse_used": False})

    def relations(self, selection, rhs):
        name = "R796-original-global-quadratic-relations"
        value = self.cache(name)
        if value:
            return value
        columns = [self.exact_product(*pair) for pair in selection["WP_pairs"]]
        P0 = matrix_from_columns([column[0] for column in columns])
        P1 = matrix_from_columns([column[1] for column in columns])
        rows = selection["minor_rows"]
        A0, A1 = selected_rows(P0, rows), selected_rows(P1, rows)
        B0, B1 = selected_rows(rhs[0], rows), selected_rows(rhs[1], rows)
        solve_name = "R796-exact-unique-quadratic-solution"
        solved = self.cache(solve_name)
        if solved is None:
            self.check()
            if self.pure_Q:
                assert all(not x for row in A1.tolist() for x in row)
                assert all(not x for row in B1.tolist() for x in row)
                solution = fmpq_mat(A0).solve(fmpq_mat(B0))
                numerators, denominator = solution.numer_denom()
                N0, N1 = numerators, fmpz_mat(PRODUCTS, U2)
                dimension = PRODUCTS
            else:
                block = fmpz_mat(
                    [[A0[i, j] for j in range(PRODUCTS)]+[-A1[i, j] for j in range(PRODUCTS)]
                     for i in range(PRODUCTS)] +
                    [[A1[i, j] for j in range(PRODUCTS)]+[A0[i, j]-A1[i, j] for j in range(PRODUCTS)]
                     for i in range(PRODUCTS)])
                right = fmpz_mat(B0.tolist()+B1.tolist())
                solution = fmpq_mat(block).solve(fmpq_mat(right))
                numerators, denominator = solution.numer_denom()
                N0 = selected_rows(numerators, range(PRODUCTS))
                N1 = selected_rows(numerators, range(PRODUCTS, 2*PRODUCTS))
                dimension = 2*PRODUCTS
            assert denominator > 0
            solved = self.store(solve_name, {"solution_common_denominator": str(denominator),
                "coefficient_numerators_1": smatrix(N0), "coefficient_numerators_zeta": smatrix(N1),
                "coefficient_shape": [PRODUCTS, U2], "exact_Q_solve_dimension": dimension,
                "pure_Q_optimization_verified_from_actual_K_data": self.pure_Q,
                "selected_minor_sha256": sha(self.path("R796-WP2-selected-monomials")),
                "all_full_rows_verified": False})
        N0, N1 = zmatrix(solved["coefficient_numerators_1"]), zmatrix(solved["coefficient_numerators_zeta"])
        denominator = fmpz(solved["solution_common_denominator"])
        self.check()
        assert P0*N0-P1*N1 == denominator*rhs[0]
        assert P0*N1+P1*N0-P1*N1 == denominator*rhs[1]
        return self.store(name, {"solution_common_denominator": str(denominator),
            "coefficient_numerators_1": smatrix(N0), "coefficient_numerators_zeta": smatrix(N1),
            "coefficient_shape": [PRODUCTS, U2], "WP_pairs": selection["WP_pairs"],
            "selected_minor_sha256": sha(self.path("R796-WP2-selected-monomials")),
            "solution_sha256": sha(self.path(solve_name)), "all_144_global_relations_verified": True,
            "verification_highest_qY_exponent": ORDERS-1, "full_xi_coordinate_count": XI,
            "complete_K_coordinate_count": 2, "all_exact_integer_residuals_zero": True,
            "section_degree": 544, "certified_zero_order_lower_bound": 560,
            "implicit_x_Jacobian_at_original_CM_point": "identity_144"})

    def jets(self, adapted, relations):
        N = self.args.target_length
        name = "R796-original-M2-ratio-jets-length-"+str(N).zfill(4)
        value = self.cache(name)
        if value:
            return value
        coefficients = [[ZERO, ZERO] for _ in range(U2)]
        denominator = fmpz(relations["solution_common_denominator"])
        N0 = zmatrix(relations["coefficient_numerators_1"]).transpose()
        N1 = zmatrix(relations["coefficient_numerators_zeta"]).transpose()
        C0, C1 = fmpq_mat(N0)/denominator, fmpq_mat(N1)/denominator
        pairs = relations["WP_pairs"]
        previous = sha(self.path("R796-original-CM-adapted-M2-basis"))
        relation_sha = sha(self.path("R796-original-global-quadratic-relations"))
        for n in range(2, N):
            self.check()
            stage_name = "R796-local-coefficient-"+str(n).zfill(4)
            stage = self.cache(stage_name)
            if stage is None:
                products = []
                for a, b in pairs:
                    total = ZERO
                    for r in range(1, n):
                        first = (ONE if r == 1 else ZERO) if a == 0 else coefficients[a-1][r]
                        second = (ONE if n-r == 1 else ZERO) if b == 0 else coefficients[b-1][n-r]
                        total = ka(total, km(first, second))
                    products.append(total)
                V0, V1 = (fmpq_mat([[v[part]] for v in products]) for part in range(2))
                X0, X1 = C0*V0-C1*V1, C0*V1+C1*V0-C1*V1
                degree_values = [(X0[j, 0], X1[j, 0]) for j in range(U2)]
                stage = self.store(stage_name, {"degree": n, "K_coefficients": [ek(x) for x in degree_values],
                    "previous_coefficient_sha256": previous, "global_relations_sha256": relation_sha,
                    "new_degree_only": True})
            assert stage["degree"] == n and stage["previous_coefficient_sha256"] == previous
            assert stage["global_relations_sha256"] == relation_sha
            assert len(stage["K_coefficients"]) == U2
            for j, item in enumerate(stage["K_coefficients"]):
                coefficients[j].append(dk(item))
            previous = sha(self.path(stage_name))
        rows = []
        for desc in adapted["original_M2_ratio_decompositions"]:
            series = [dk(desc["constant"]), dk(desc["linear"])]+[ZERO]*(N-2)
            if desc["x_index"] is not None:
                coefficient = dk(desc["x_coefficient"])
                x = coefficients[desc["x_index"]-1]
                series = [ka(s, km(coefficient, c)) for s, c in zip(series, x)]
            rows.append([ek(x) for x in series])
        vt, dt = self.values[adapted["tau_original_index"]], self.derivatives[adapted["tau_original_index"]]
        lam = dk(adapted["lambda_dt_dz_K_1_zeta"])
        for i, series in enumerate(rows):
            assert dk(series[0]) == kd(self.values[i], vt)
            expected = kd(ks(km(self.derivatives[i], vt), km(self.values[i], dt)), km(vt, vt))
            assert km(dk(series[1]), lam) == expected
        return self.store(name, {"completed_jet_length": N, "through_degree": N-1,
            "formal_variable": "t=sigma/tau", "lambda_dt_dz_K_1_zeta": ek(lam),
            "tau_original_index": adapted["tau_original_index"], "ratios": "original s_i/tau",
            "ratio_coefficients_K_1_zeta": rows, "global_relations_sha256": relation_sha,
            "last_coefficient_sha256": previous, "all_original_values_and_first_coarse_derivatives_preserved": True,
            "original_M2_integer_scale": "6724", "extra_power5_scale_multiplier_required": False,
            "actual_A_B_beta_eta_or_heights_computed": False})

    def finish(self, adapted, selection, relations, jets):
        files = [spec(path) for path in sorted(self.out.glob("R796-*.json.gz"))
                 if path.name != "R796-stage-manifest.json.gz"]
        stage_path = self.path("R796-stage-manifest")
        save(stage_path, {"result": RESULT, "complete": True, "configuration": self.tag, "files": files})
        certificate = {"result": RESULT, "p": 41, "complete": True, "configuration": self.tag,
            "original_M2_dimension": M2, "selected_WP2_monomials": PRODUCTS,
            "global_quadratic_relations": U2, "all_144_global_relations_verified": True,
            "implicit_x_Jacobian_at_original_CM_point": "identity_144",
            "requested_jet_length": self.args.target_length,
            "completed_jet_length": jets["completed_jet_length"],
            "tau_original_index": adapted["tau_original_index"],
            "tangent_original_index": adapted["tangent_original_index"],
            "lambda_dt_dz_K_1_zeta": adapted["lambda_dt_dz_K_1_zeta"],
            "actual_auxiliary_prime": selection["prime"], "actual_modular_rank": PRODUCTS,
            "actual_selected_monomial_count_scanned": selection["actual_candidate_count_scanned"],
            "cusp_verification_highest_exponent": ORDERS-1,
            "source_CM_values_or_first_derivatives_recomputed": False,
            "old_E1_M2_or_Laurent_prefixes_recomputed": False,
            "actual_beta_eta_or_heights_computed": False,
            "basis_adaptation": spec(self.path("R796-original-CM-adapted-M2-basis")),
            "selected_monomials": spec(self.path("R796-WP2-selected-monomials")),
            "global_relations": spec(self.path("R796-original-global-quadratic-relations")),
            "ratio_jets": spec(self.path("R796-original-M2-ratio-jets-length-"+str(self.args.target_length).zfill(4))),
            "stage_manifest": spec(stage_path), "seconds": time.monotonic()-self.started}
        save(self.out/FINAL, certificate)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(self.out/FINAL),
            "completed_jet_length": jets["completed_jet_length"]})
        print(json.dumps({key: certificate[key] for key in
            ("result", "complete", "selected_WP2_monomials", "global_quadratic_relations",
             "completed_jet_length", "actual_auxiliary_prime", "actual_selected_monomial_count_scanned")}), flush=True)

    def run(self):
        adapted = self.adapt()
        self.prefixes(adapted)
        selection = self.select()
        rhs = self.rhs()
        relations = self.relations(selection, rhs)
        jets = self.jets(adapted, relations)
        self.finish(adapted, selection, relations, jets)


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--retained", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--proof", type=Path, required=True)
    parser.add_argument("--method", type=Path, required=True)
    parser.add_argument("--rr-proof", type=Path, required=True)
    parser.add_argument("--target-length", type=int, required=True)
    parser.add_argument("--budget-minutes", type=int, default=300)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        Job(args).run()
    except BaseException as error:
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error),
            "completed_stages_preserved": True})
        raise


if __name__ == "__main__":
    main()

