#!/usr/bin/env python3
"""R787: recover one original L-valued power5 function relation.

Formal arithmetic is confined to the public repository's GitHub Actions.
Only prime-modulus matrices are inverted.  Every lifted candidate is finally
checked in characteristic zero against all 129 original twenty-coordinate
relations; neither a modular rank nor rational reconstruction certifies it.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time

import flint
from flint import (fmpq, fmpq_mat, fmpz, fmpz_mat, fmpz_mod_ctx,
                   fmpz_mod_mat, fmpz_mod_poly_ctx, fmpz_poly,
                   nmod_mat, nmod_poly)

RESULT = "R787-original-power5-function-relation"
FINAL = "p41-original-power5-function-relation-certificate.json"
N, D, T, LDEG, ORDERS = 1234, 1214, 20, 14, 129
R781_CORE = "d024a7a6f5febd4658e8b5b5e5e3659f3c5fcc0daa39d70569ac408ef83a8751"
R786_CORE = "4508095a95a2bcaec8c8db8fcd550fbc618b017d2bc0007945783bc109dbf851"
R786_PROOF = "c46008726fb18f52a5430b72c4994ce76164f11bea51044f1677278294f7011d"
PRODUCERS = {
    "R781": {
        "manifest": "ce0554fab03fda8d124e9e0ee338335bca6f7b39ee8499550bbec36358a1a7fd",
        "certificate": "b9e1a2282d6fc0de12df401abbc3014ded525757c7102d11967f0bd33a40f3f0",
        "certificate_file": "p41-original-inverse-free-Laurent-prefix-certificate.json",
        "core": R781_CORE,
        "result": "R781-original-p41-inverse-free-Laurent-prefix"},
    "R786": {
        "manifest": "e3c29e85236c8cc665bdf88e9ffd2bbab9180b6f977f0b2b22f54266762f405a",
        "certificate": "dc6c23568f80b861d839280846c3250063abdfb2716a20481779816bb7cd37d9",
        "certificate_file": "p41-exact-original-power5-short-basis-certificate.json",
        "core": R786_CORE,
        "result": "R786-exact-original-power5-short-basis"}}


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    data = (json.dumps(obj, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        with temporary.open("wb") as raw:
            with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, compresslevel=2) as stream:
                stream.write(data)
    else:
        temporary.write_bytes(data)
    temporary.replace(path)


def imatrix(matrix):
    return [[int(matrix[i, j]) for j in range(matrix.ncols())]
            for i in range(matrix.nrows())]


def smatrix(matrix):
    return [[str(matrix[i, j]) for j in range(matrix.ncols())]
            for i in range(matrix.nrows())]


def submatrix(matrix, rows, columns=None, ell=None):
    if columns is None:
        columns = range(matrix.ncols())
    data = [[int(matrix[i, j]) % ell if ell is not None else int(matrix[i, j])
             for j in columns] for i in rows]
    return nmod_mat(data, ell) if ell is not None else fmpz_mat(data)


def pivot_columns(matrix):
    reduced, rank = matrix.rref()
    pivots = []
    for i in range(rank):
        pivot = next(j for j in range(reduced.ncols()) if reduced[i, j])
        pivots.append(pivot)
    assert len(set(pivots)) == rank
    return pivots


def zero_matrix(matrix):
    return all(not x for row in matrix.tolist() for x in row)


def rational_reconstruct(value, modulus):
    value %= modulus
    if value == 0:
        return fmpq(0)
    bound = math.isqrt(modulus//2)
    r0, r1, t0, t1 = modulus, value, 0, 1
    while abs(r1) > bound:
        q = r0//r1
        r0, r1, t0, t1 = r1, r0-q*r1, t1, t0-q*t1
    if not t1 or abs(t1) > bound or math.gcd(r1, t1) != 1:
        return None
    if t1 < 0:
        r1, t1 = -r1, -t1
    if (value*t1-r1) % modulus:
        return None
    return fmpq(r1, t1)


class BudgetStop(RuntimeError):
    pass


class BadPrime(RuntimeError):
    pass


class Retained:
    def __init__(self, root, name, spec):
        self.directory = root/name
        expected = PRODUCERS[name]
        path = self.directory/"full-outputs-manifest.json"
        assert sha(path) == expected["manifest"] == spec["manifest_sha256"]
        self.files = {x["file"]: x for x in read(path)["files"]}
        path = self.directory/expected["certificate_file"]
        assert spec["certificate_name"] == expected["certificate_file"]
        assert sha(path) == expected["certificate"] == spec["files"][expected["certificate_file"]]
        self.certificate = read(path)
        assert self.certificate["complete"] and self.certificate["result"] == expected["result"]
        self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == expected["core"] == spec["core_sha256"]

    def get(self, name):
        path = self.directory/name
        item = self.files[name]
        assert path.stat().st_size == item["bytes"] and sha(path) == item["sha256"]
        obj = read(path)
        assert obj["complete"] and obj["configuration"] == self.tag
        return obj


class ModularField:
    """Monic quotient arithmetic only, valid also modulo ell^k.

    Products pack t,B,s with strides 1,39,507.  A further stride 1521
    separates successive q powers, since a product field block ends at 1520.
    There is no division or matrix inversion in this class.
    """
    def __init__(self, field, modulus):
        self.f, self.modulus = field, modulus
        self.ctx = fmpz_mod_poly_ctx(modulus)
        self.mctx = fmpz_mod_ctx(modulus)
        self.Bred = fmpz_mod_mat(imatrix(field.Bred), self.mctx)
        self.Tred = fmpz_mod_mat(imatrix(field.Tred), self.mctx)
        self.indices = [r+39*i+507*j for j in range(2) for i in range(7) for r in range(20)]

    def packed(self, vector):
        values = [0]*761
        for index, value in zip(self.indices, vector):
            values[index] = value
        return self.ctx(values)

    def reduced(self, product, offset=0):
        rows = []
        for j in range(2):
            for i in range(13):
                if j == 0:
                    rows.append([int(product[offset+r+39*i])-3*int(product[offset+r+39*i+1014])
                                 for r in range(39)])
                else:
                    rows.append([int(product[offset+r+39*i+507]) for r in range(39)])
        out = self.Bred*fmpz_mod_mat(rows, self.mctx)*self.Tred
        return [int(out[i, r]) for i in range(14) for r in range(20)]

    def multiply(self, left, right):
        return self.reduced(self.packed(left)*self.packed(right))

    def convolution(self, left, right):
        aa, bb = [0]*(1521*ORDERS), [0]*(1521*ORDERS)
        for n in range(ORDERS):
            offset = 1521*n
            for index, a, b in zip(self.indices, left[n], right[n]):
                aa[offset+index], bb[offset+index] = a, b
        product = self.ctx(aa).mul_low(self.ctx(bb), 1521*ORDERS)
        return [self.reduced(product, 1521*n) for n in range(ORDERS)]


class Job:
    def __init__(self, args):
        assert flint.__version__ == "0.9.0"
        self.args, self.out = args, args.output
        self.started = time.monotonic()
        self.item = read(args.config)
        assert self.item["producer_inputs_pending"] is False
        assert sha(args.proof) == R786_PROOF == self.item["R786_proof_sha256"]
        assert sha(args.method) == self.item["R787_method_sha256"]
        assert sha(args.field_core) == R781_CORE
        spec = importlib.util.spec_from_file_location("retained_R781", args.field_core)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.r781 = Retained(args.retained, "R781", self.item["retained_artifacts"]["R781"])
        self.r786 = Retained(args.retained, "R786", self.item["retained_artifacts"]["R786"])
        cert = self.r786.certificate
        assert cert["original_map_index"] == 4 and cert["original_map_degree"] == "1206"
        assert cert["exact_power5_basis_dimension"] == N and cert["exact_K_basis_prefix_bound_qY"] == 128
        assert cert["all_original_R775_mod739_short_series_compared"]
        inputs = self.r781.get("R781-original-real-field-input.json.gz")
        self.f = module.Field(inputs["field"]["original_b_minimal_polynomial"])
        assert self.f.description == inputs["field"]
        assert self.r781.tag["selected_map_index"] == 4 and self.r781.tag["selected_map_degree"] == "1206"
        self.R, self.K = [], []
        prior = None
        for n in range(130):
            name = "R781-inverse-free-Laurent-"+str(n).zfill(3)+".json.gz"
            row = self.r781.get(name)
            assert row["order"] == n and row["exact_differential_identity_at_this_order"]
            if n:
                assert row["previous_stage_sha256"] == self.r781.files[prior]["sha256"]
            else:
                assert row["input_stage_sha256"] == self.r781.files["R781-original-real-field-input.json.gz"]["sha256"]
                self.kappa = self.f.decode(row["kappa"])
            self.K.append(self.f.decode(row["coefficients"]["kappa_power"]))
            if n < ORDERS:
                self.R.append(self.f.decode(row["coefficients"]["R"]))
            prior = name
        assert self.K[0] == self.f.one and self.K[1] == self.kappa and self.R[0] == self.f.one
        index_spec = cert["basis_index"]
        assert self.r786.files[index_spec["file"]]["sha256"] == index_spec["sha256"]
        self.index = self.r786.get(index_spec["file"])
        assert self.index["dimension"] == N and self.index["bound_qY"] == 128
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "R786_proof_sha256": R786_PROOF, "R787_method_sha256": sha(args.method),
            "R781_field_core_sha256": R781_CORE, "retained_artifacts": self.item["retained_artifacts"],
            "original_map_index": 4, "original_map_degree": "1206",
            "field": self.f.description, "ordinary_power": 5, "basis_dimension": N,
            "basis_integer_scale": cert["basis_integer_scale"], "qY_bound": 128,
            "full_L_unknown_dimension_over_Q": 14, "Laurent_exponents": [-1, 127],
            "t_coordinates": 20, "Schur_shape": [1326, 1214],
            "auxiliary_prime_start": int(self.item.get("auxiliary_prime_start", 1000000007)),
            "reconstruct_every_digits": int(self.item.get("reconstruct_every_digits", 8)),
            "composite_modulus_matrix_inversion": False,
            "completed_producer_arithmetic_recomputed": False}
        assert self.tag["auxiliary_prime_start"] >= 1000
        assert self.tag["reconstruct_every_digits"] >= 1
        self.out.mkdir(parents=True, exist_ok=True)

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes:
            raise BudgetStop("All completed R787 stages remain available for exact resumption.")

    def path(self, name):
        return self.out/(name+".json.gz")

    def cache(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        obj = read(path)
        assert obj["complete"] and obj["configuration"] == self.tag
        return obj

    def store(self, name, obj):
        save(self.path(name), dict(obj, complete=True, configuration=self.tag))
        print(json.dumps({"stage": name, "seconds": time.monotonic()-self.started, "complete": True}), flush=True)
        return self.path(name)

    def prime_name(self, ell, suffix):
        return "R787-prime-"+str(ell)+"-"+suffix

    def real_basis(self):
        columns = []
        for i, item in enumerate(self.index["basis_rows"]):
            self.budget()
            assert item["index"] == i
            assert self.r786.files[item["file"]]["sha256"] == item["sha256"]
            row = self.r786.get(item["file"])
            assert row["weight"] == 10 and row["bound_qY"] == 128
            assert row["integer_scale"] == self.r786.certificate["basis_integer_scale"]
            name = "R787-real-power5-row-"+str(i).zfill(4)
            cached = self.cache(name)
            if cached:
                assert cached["R786_row_sha256"] == item["sha256"]
                columns.append([int(x) for values in cached["integer_t_coefficients"] for x in values])
                continue
            values = []
            assert len(row["integer_qY_xi_coefficients"]) == ORDERS
            for n, old in enumerate(row["integer_qY_xi_coefficients"]):
                assert len(old) == 40
                cyclic = [0]*41
                for r in range(40):
                    cyclic[(r+10*n) % 41] += int(old[r])
                reduced = [v-cyclic[40] for v in cyclic[:40]]+[0]
                assert all(reduced[r] == reduced[41-r] for r in range(1, 21)), (i, n, "weight10 phase")
                real = fmpz_poly([reduced[0]])
                for r in range(1, 21):
                    real += self.f.chebyshev[r]*reduced[r]
                real %= self.f.gt
                values.append([int(real[r]) for r in range(20)])
            self.store(name, {"index": i, "R786_row_sha256": item["sha256"],
                "integer_t_coefficients": [[str(v) for v in row] for row in values],
                "all_original_phase_involutions_verified": True, "averaging_used": False})
            columns.append([x for row in values for x in row])
        assert len(columns) == N
        self.F = fmpz_mat([list(row) for row in zip(*columns)])
        del columns
        assert self.F.nrows() == ORDERS*T and self.F.ncols() == N

    def value_mod(self, value, modulus):
        scale = int(value.scale.numer())*pow(int(value.scale.denom()), -1, modulus) % modulus
        return [int(x)*scale % modulus for x in self.f.vector(value)]

    def next_prime(self):
        search = self.cache("R787-search-state")
        if search:
            candidate = int(search["current_candidate"])
            if not self.cache(self.prime_name(candidate, "rejected")):
                selection = self.cache(self.prime_name(candidate, "selection"))
                if selection:
                    return selection
            candidate += 1
        else:
            candidate = self.tag["auxiliary_prime_start"]
        while True:
            self.budget()
            assert candidate < 2**31, "Auxiliary search exceeded the word-prime range."
            if not fmpz(candidate).is_prime():
                candidate += 1
                continue
            ell = candidate
            candidate += 1
            if any(int(value.scale.denom()) % ell == 0 for value in self.R+self.K):
                continue
            if 246 % ell == 0 or int(self.f.lam) % ell == 0:
                continue
            fB = nmod_poly([int(x) % ell for x in self.f.fB.coeffs()], ell)
            roots = fB.roots()
            if len(roots) != 7 or any(multiplicity != 1 for _, multiplicity in roots):
                continue
            ss = nmod_poly([3, 0, 1], ell).roots()
            if len(ss) != 2 or any(multiplicity != 1 for _, multiplicity in ss):
                continue
            pairs = [(int(b), int(s)) for s, _ in sorted(ss, key=lambda x: int(x[0]))
                     for b, _ in sorted(roots, key=lambda x: int(x[0]))]
            evaluations = [[pow(b, i, ell)*pow(s, j, ell) % ell
                            for j in range(2) for i in range(7)] for b, s in pairs]
            V = nmod_mat(evaluations, ell)
            inverse = V.inv()
            assert V*inverse == nmod_mat([[int(i == j) for j in range(14)] for i in range(14)], ell)
            gt = nmod_poly([int(x) for x in self.f.gt.coeffs()], ell)
            kv = self.value_mod(self.kappa, ell)
            inverses = []
            usable = True
            for weights in evaluations:
                k = nmod_poly([sum(weights[i]*kv[20*i+r] for i in range(14)) % ell for r in range(20)], ell)
                gcd, aa, bb = k.xgcd(gt)
                assert k*aa+gt*bb == gcd
                if gcd.degree() != 0:
                    usable = False
                    break
                inv = (aa*pow(int(gcd[0]), -1, ell)) % gt
                assert (k*inv) % gt == nmod_poly([1], ell)
                inverses.append([int(inv[r]) for r in range(20)])
            if not usable:
                continue
            selection = {"prime": ell, "prime_proved": True, "roots_B_s": pairs,
                "evaluation_matrix": evaluations, "inverse_evaluation_matrix": imatrix(inverse),
                "kappa_inverse_at_each_L_branch": inverses,
                "all_14_L_branches_distinct": True, "all_rational_denominators_units": True,
                "all_kappa_reductions_invertible": True}
            self.store(self.prime_name(ell, "selection"), selection)
            self.store("R787-search-state", {"current_candidate": ell})
            return self.cache(self.prime_name(ell, "selection"))

    def rational_blocks(self, selection):
        ell = selection["prime"]
        name = self.prime_name(ell, "rational-blocks")
        block = self.cache(name)
        if block is None:
            E = submatrix(self.F, range(20), ell=ell)
            pivots = pivot_columns(E)
            if len(pivots) != 20:
                raise BadPrime("The constant-cusp evaluation loses rank at this prime.")
            free = [j for j in range(N) if j not in set(pivots)]
            EP = submatrix(self.F, range(20), pivots)
            EQ = submatrix(self.F, range(20), free)
            rational = fmpq_mat(EP).solve(fmpq_mat(EQ))
            numerator, denominator = rational.numer_denom()
            Zp = -numerator
            assert zero_matrix(EP*Zp+EQ*denominator)
            assert int(denominator) % ell
            prefix = submatrix(self.F, range(69*T), ell=ell)
            J = pivot_columns(prefix.transpose())
            if len(J) != N:
                raise BadPrime("The rational A-prefix minor loses rank at this prime.")
            R = [i for i in range(128*T) if i not in set(J)]
            F0 = submatrix(self.F, J, ell=ell)
            inverse = F0.inv()
            assert F0*inverse == nmod_mat([[int(i == j) for j in range(N)] for i in range(N)], ell)
            block = {"prime": ell, "B_constant_pivot_columns": pivots,
                "B_constant_free_columns": free, "Z_pivot_integer_rows": smatrix(Zp),
                "Z_free_diagonal": str(denominator), "exact_E0_Z_zero_verified": True,
                "A_pivot_rows": J, "A_remaining_rows": R,
                "A_inverse_mod_prime": imatrix(inverse),
                "A_minor_det_mod_prime": int(F0.det()),
                "B_constant_minor_det_mod_prime": int(submatrix(EP, range(20), ell=ell).det()),
                "A_inverse_over_Q_computed": False}
            self.store(name, block)
        self.P = block["B_constant_pivot_columns"]
        self.Q = block["B_constant_free_columns"]
        self.Zp = fmpz_mat([[int(x) for x in row] for row in block["Z_pivot_integer_rows"]])
        self.Zd = int(block["Z_free_diagonal"])
        self.J, self.AR = block["A_pivot_rows"], block["A_remaining_rows"]
        self.Ainv = nmod_mat(block["A_inverse_mod_prime"], ell)
        self.FA = submatrix(self.F, range(128*T), ell=ell)
        self.FAR = submatrix(self.FA, self.AR, ell=ell)
        assert len(self.Q) == D and len(self.AR) == 1326
        # Z is kept sparse: only twenty pivot rows are dense.
        left = submatrix(self.F, range(ORDERS*T), self.Q, ell=ell)*(self.Zd % ell)
        right = submatrix(self.F, range(ORDERS*T), self.P, ell=ell)*submatrix(self.Zp, range(20), ell=ell)
        self.G = left+right
        assert zero_matrix(submatrix(self.G, range(20), ell=ell))
        return block

    def branch_laurent(self, selection, branch):
        ell = selection["prime"]
        weights = selection["evaluation_matrix"][branch]
        gt = nmod_poly([int(x) for x in self.f.gt.coeffs()], ell)
        inv = nmod_poly(selection["kappa_inverse_at_each_L_branch"][branch], ell)
        inv246 = pow(246**3, -1, ell)
        inverse_power = inv
        Y, inverse_clear = [], []
        for m in range(ORDERS):
            vector = self.value_mod(self.R[m], ell)
            rr = nmod_poly([sum(weights[i]*vector[20*i+r] for i in range(14)) % ell for r in range(20)], ell)
            yy = (-rr*inverse_power*inv246) % gt
            Y.append([int(yy[r]) for r in range(20)])
            # q^m in Y=v*y.  For n=m-1 the cleared multiplier is 246^3*kappa^(m+1).
            if m:
                scale = inverse_power*inv246 % gt
                inverse_clear.append([int(scale[r]) for r in range(20)])
            inverse_power = inverse_power*inv % gt
        assert len(inverse_clear) == 128
        return Y, inverse_clear

    def convolution_matrix(self, selection, branch, Y):
        ell = selection["prime"]
        raw_y = [0]*(39*ORDERS)
        for n, values in enumerate(Y):
            raw_y[39*n:39*n+20] = values
        polynomial = nmod_poly(raw_y, ell)
        reduction = nmod_mat(imatrix(self.f.Tred), ell)
        columns = []
        for first in range(0, D, 32):
            self.budget()
            name = self.prime_name(ell, "C-"+str(branch).zfill(2)+"-block-"+str(first).zfill(4))
            cached = self.cache(name)
            if cached:
                assert cached["first_column"] == first
                columns.extend(cached["columns"])
                continue
            block = []
            for column in range(first, min(first+32, D)):
                packed = [0]*(39*ORDERS)
                for n in range(ORDERS):
                    packed[39*n:39*n+20] = [int(self.G[20*n+r, column]) for r in range(20)]
                product = polynomial.mul_low(nmod_poly(packed, ell), 39*ORDERS)
                reduced = nmod_mat([[int(product[39*n+r]) for r in range(39)]
                                    for n in range(ORDERS)], ell)*reduction
                assert all(not reduced[0, r] for r in range(20))
                block.append([int(reduced[n, r]) for n in range(1, ORDERS) for r in range(20)])
            self.store(name, {"prime": ell, "branch": branch, "first_column": first, "columns": block})
            columns.extend(block)
        assert len(columns) == D
        return nmod_mat([list(row) for row in zip(*columns)], ell)

    def branches(self, selection):
        ell = selection["prime"]
        chart_name = self.prime_name(ell, "chart")
        chart = self.cache(chart_name)
        branches = []
        for branch in range(14):
            self.budget()
            name = self.prime_name(ell, "branch-"+str(branch).zfill(2))
            cached = self.cache(name)
            if cached:
                assert chart is not None and cached["chart_sha256"] == sha(self.path(chart_name))
                branches.append(cached)
                continue
            Y, inverse_clear = self.branch_laurent(selection, branch)
            C = self.convolution_matrix(selection, branch, Y)
            CJ = submatrix(C, self.J, ell=ell)
            CR = submatrix(C, self.AR, ell=ell)
            S = CR-self.FAR*self.Ainv*CJ
            if chart is None:
                columns = pivot_columns(S)
                rank = len(columns)
                assert rank <= 1186, ("Original structural rank bound violated", rank)
                if not rank:
                    raise BadPrime("The Schur reduction is identically zero.")
                rows = pivot_columns(submatrix(S, range(1326), columns, ell=ell).transpose())
                assert len(rows) == rank
                free_column = next(j for j in range(D) if j not in set(columns))
                chart = {"prime": ell, "actual_modular_rank": rank, "pivot_columns": columns,
                    "pivot_rows": rows, "chosen_free_column": free_column,
                    "other_free_columns_set_to_zero": True,
                    "theoretical_rank_upper_bound_only": 1186,
                    "all_14_branches_already_verified": False}
                self.store(chart_name, chart)
                chart = self.cache(chart_name)
            else:
                rank = int(S.rank())
                assert rank <= 1186
                if rank != chart["actual_modular_rank"]:
                    raise BadPrime("The fourteen L reductions have different Schur ranks.")
            rows, columns = chart["pivot_rows"], chart["pivot_columns"]
            square = submatrix(S, rows, columns, ell=ell)
            try:
                inverse = square.inv()
            except ZeroDivisionError as exc:
                raise BadPrime("The selected common L minor vanishes in another branch.") from exc
            cc = nmod_mat(D, 1, [0]*D, ell)
            cc[chart["chosen_free_column"], 0] = 1
            rhs = submatrix(S, rows, [chart["chosen_free_column"]], ell)
            cp = -inverse*rhs
            for i, column in enumerate(columns):
                cc[column, 0] = cp[i, 0]
            aa = self.Ainv*CJ*cc
            assert zero_matrix(S*cc) and zero_matrix(self.FA*aa-C*cc)
            cached = {"prime": ell, "branch": branch, "roots_B_s": selection["roots_B_s"][branch],
                "chart_sha256": sha(self.path(chart_name)), "actual_Schur_rank": rank,
                "selected_minor_det_mod_prime": int(square.det()),
                "Schur_minor_inverse_mod_prime": imatrix(inverse),
                "C_J_pivot_columns": imatrix(submatrix(CJ, range(N), columns, ell=ell)),
                "initial_A": [int(aa[i, 0]) for i in range(N)],
                "initial_C": [int(cc[i, 0]) for i in range(D)],
                "inverse_original_clear_multipliers": inverse_clear,
                "all_2560_original_uncleared_rows_verified": True}
            self.store(name, cached)
            branches.append(self.cache(name))
            # Completed branch inverse replaces the bulky temporary C-column blocks.
            for path in self.out.glob(self.prime_name(ell, "C-"+str(branch).zfill(2)+"-block-")+"*.json.gz"):
                path.unlink()
        return chart, branches

    def expand_B(self, cc, modulus=None):
        cp = self.Zp*fmpz_mat(cc)
        rows = [[0]*14 for _ in range(N)]
        for j, index in enumerate(self.P):
            rows[index] = [int(cp[j, k]) for k in range(14)]
        for j, index in enumerate(self.Q):
            rows[index] = [self.Zd*int(cc[j][k]) for k in range(14)]
        if modulus is not None:
            rows = [[x % modulus for x in row] for row in rows]
        return rows

    def residual(self, aa, cc, modulus):
        """All 129*20*14 original cleared coordinates modulo modulus."""
        self.budget()
        bb = self.expand_B(cc, modulus)
        A = self.F*fmpz_mat(aa)
        B = self.F*fmpz_mat(bb)
        av, bv = [], []
        for n in range(ORDERS):
            av.append([int(A[20*n+r, i]) % modulus for i in range(14) for r in range(20)])
            bv.append([int(B[20*n+r, i]) % modulus for i in range(14) for r in range(20)])
        ring = ModularField(self.f, modulus)
        rr = [self.value_mod(x, modulus) for x in self.R]
        kk = [self.value_mod(x, modulus) for x in self.K]
        weighted_B = [ring.multiply(kk[j], bv[j]) for j in range(ORDERS)]
        total = ring.convolution(rr, weighted_B)
        for m in range(1, ORDERS):
            self.budget()
            term = ring.multiply(kk[m+1], av[m-1])
            total[m] = [(x+246**3*y) % modulus for x, y in zip(total[m], term)]
        assert all(0 <= x < modulus for row in total for x in row)
        return total

    def initial_lift(self, selection, chart, branches):
        ell = selection["prime"]
        inverse = nmod_mat(selection["inverse_evaluation_matrix"], ell).transpose()
        aa = nmod_mat([[branch["initial_A"][i] for branch in branches] for i in range(N)], ell)*inverse
        cc = nmod_mat([[branch["initial_C"][i] for branch in branches] for i in range(D)], ell)*inverse
        answer = {"prime": ell, "digits": 1, "modulus": str(ell),
            "A_L_coordinates": [[str(x) for x in row] for row in imatrix(aa)],
            "C_L_coordinates": [[str(x) for x in row] for row in imatrix(cc)],
            "chart_sha256": sha(self.path(self.prime_name(ell, "chart"))),
            "full_original_modular_relations_verified": True,
            "verification": "all fourteen faithful branch equations, including B0=0"}
        self.store(self.prime_name(ell, "dixon-"+str(1).zfill(8)), answer)
        return answer

    def correction(self, selection, chart, branches, residual_divided):
        ell = selection["prime"]
        gt = nmod_poly([int(x) for x in self.f.gt.coeffs()], ell)
        pivots, rows = chart["pivot_columns"], chart["pivot_rows"]
        FARp = submatrix(self.FAR, rows, ell=ell)
        delta_A, delta_C = [], []
        for branch, data in enumerate(branches):
            self.budget()
            weights = selection["evaluation_matrix"][branch]
            rhs = []
            for m in range(1, ORDERS):
                vector = residual_divided[m]
                poly = nmod_poly([sum(weights[i]*vector[20*i+r] for i in range(14)) % ell
                                  for r in range(20)], ell)
                inverse_clear = nmod_poly(data["inverse_original_clear_multipliers"][m-1], ell)
                value = (-poly*inverse_clear) % gt
                rhs.extend([int(value[r]) for r in range(20)])
            rhsJ = nmod_mat([[rhs[i]] for i in self.J], ell)
            rhsR = nmod_mat([[rhs[self.AR[i]]] for i in rows], ell)
            inv = nmod_mat(data["Schur_minor_inverse_mod_prime"], ell)
            cp = inv*(FARp*self.Ainv*rhsJ-rhsR)
            aa = self.Ainv*(rhsJ+nmod_mat(data["C_J_pivot_columns"], ell)*cp)
            cc = [0]*D
            for i, column in enumerate(pivots):
                cc[column] = int(cp[i, 0])
            delta_A.append([int(aa[i, 0]) for i in range(N)])
            delta_C.append(cc)
        inverse = nmod_mat(selection["inverse_evaluation_matrix"], ell).transpose()
        aa = nmod_mat([list(row) for row in zip(*delta_A)], ell)*inverse
        cc = nmod_mat([list(row) for row in zip(*delta_C)], ell)*inverse
        return imatrix(aa), imatrix(cc)

    def try_exact(self, selection, chart, lift):
        self.budget()
        modulus = int(lift["modulus"])
        matrices = []
        denominator = 1
        for key in ("A_L_coordinates", "C_L_coordinates"):
            rows = []
            for old in lift[key]:
                values = []
                for x in old:
                    value = rational_reconstruct(int(x), modulus)
                    if value is None:
                        return None
                    denominator = math.lcm(denominator, int(value.denom()))
                    values.append(value)
                rows.append(values)
            matrices.append(rows)
        aa, cc = [[[int(value.numer())*(denominator//int(value.denom())) for value in row]
                   for row in matrix] for matrix in matrices]
        bb = self.expand_B(cc)
        content = 0
        for row in aa+bb:
            for value in row:
                content = math.gcd(content, value)
        assert content > 0
        aa = [[x//content for x in row] for row in aa]
        bb = [[x//content for x in row] for row in bb]
        assert any(x for row in bb for x in row)
        recipe = {"field": self.f.description, "L_basis": "B^i*s^j, j=0..1 outer, i=0..6; B=lambda*b",
            "original_R786_basis_order": True, "basis_integer_scale": self.tag["basis_integer_scale"],
            "R786_producer": self.item["retained_artifacts"]["R786"],
            "R786_basis_index": self.r786.certificate["basis_index"],
            "A_integer_L_coordinates": [[str(x) for x in row] for row in aa],
            "B_integer_L_coordinates": [[str(x) for x in row] for row in bb],
            "common_rational_denominator_cleared": str(denominator),
            "common_integer_content_removed": str(content), "rational_reconstruction_modulus": str(modulus),
            "candidate_only_until_full_exact_verification": True}
        key = hashlib.sha256(json.dumps(recipe, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        base = "R787-candidate-"+key
        if self.cache(base+"-rejected"):
            return None
        if self.cache(base) is None:
            self.store(base, recipe)
        A, B = self.F*fmpz_mat(aa), self.F*fmpz_mat(bb)
        av, bv = [], []
        for n in range(ORDERS):
            av.append(self.f.from_vector([A[20*n+r, i] for i in range(14) for r in range(20)], 1))
            bv.append(self.f.from_vector([B[20*n+r, i] for i in range(14) for r in range(20)], 1))
        weighted = []
        for j in range(ORDERS):
            self.budget()
            name = base+"-weighted-B-"+str(j).zfill(3)
            old = self.cache(name)
            if old:
                weighted.append(self.f.decode(old["value"]))
            else:
                value = self.f.multiply(self.K[j], bv[j])
                self.store(name, {"candidate_sha256": sha(self.path(base)),
                                 "order": j, "value": self.f.encode(value)})
                weighted.append(value)
        for m in range(ORDERS):
            self.budget()
            name = base+"-exact-verification-"+str(m).zfill(3)
            cached = self.cache(name)
            if cached:
                assert cached["candidate_sha256"] == sha(self.path(base))
                assert cached["all_280_Q_coordinates_zero"]
                continue
            total = self.f.zero
            for j in range(m+1):
                if weighted[j] and self.R[m-j]:
                    total += self.f.multiply(self.R[m-j], weighted[j])
            if m:
                total += self.f.multiply(self.K[m+1], av[m-1]).scaled(246**3)
            if total:
                self.store(base+"-rejected", {"first_nonzero_relation_order": m,
                    "candidate_sha256": sha(self.path(base)), "not_a_characteristic_zero_relation": True})
                return None
            self.store(name, {"candidate_sha256": sha(self.path(base)),
                "relation_index": m, "Laurent_exponent": m-1,
                "all_280_Q_coordinates_zero": True, "all_20_L_coordinates_zero": True})
        path = self.store("R787-original-function-recipe", dict(recipe,
            candidate_only_until_full_exact_verification=False,
            candidate_sha256=sha(self.path(base)), exact_original_A_equals_yB=True,
            B_nonzero=True, full_129_original_relations_verified=True))
        return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}

    def lift(self, selection, chart, branches):
        ell = selection["prime"]
        prefix = self.prime_name(ell, "dixon-")
        checkpoints = sorted(self.out.glob(prefix+"*.json.gz"))
        if checkpoints:
            current = self.cache(checkpoints[-1].name.removesuffix(".json.gz"))
            assert current["chart_sha256"] == sha(self.path(self.prime_name(ell, "chart")))
            assert current["full_original_modular_relations_verified"]
        else:
            current = self.initial_lift(selection, chart, branches)
        while True:
            self.budget()
            digits, modulus = int(current["digits"]), int(current["modulus"])
            assert modulus == ell**digits
            if digits % self.tag["reconstruct_every_digits"] == 0:
                relation = self.try_exact(selection, chart, current)
                if relation:
                    return relation, current
            aa = [[int(x) for x in row] for row in current["A_L_coordinates"]]
            cc = [[int(x) for x in row] for row in current["C_L_coordinates"]]
            residual = self.residual(aa, cc, modulus*ell)
            assert all(x % modulus == 0 for row in residual for x in row), "Retained full residual does not vanish."
            divided = [[x//modulus for x in row] for row in residual]
            da, dc = self.correction(selection, chart, branches, divided)
            correction_residual = self.residual(da, dc, ell)
            if any((a+b) % ell for row_a, row_b in zip(divided, correction_residual)
                   for a, b in zip(row_a, row_b)):
                raise BadPrime("The selected modular chart does not lift the full original system.")
            next_a = [[a+modulus*d for a, d in zip(row, delta)] for row, delta in zip(aa, da)]
            next_c = [[c+modulus*d for c, d in zip(row, delta)] for row, delta in zip(cc, dc)]
            free = chart["chosen_free_column"]
            assert next_c[free] == [1]+[0]*13
            previous_name = self.prime_name(ell, "dixon-"+str(digits).zfill(8))
            current = {"prime": ell, "digits": digits+1, "modulus": str(modulus*ell),
                "A_L_coordinates": [[str(x) for x in row] for row in next_a],
                "C_L_coordinates": [[str(x) for x in row] for row in next_c],
                "chart_sha256": sha(self.path(self.prime_name(ell, "chart"))),
                "previous_completed_checkpoint_sha256": sha(self.path(previous_name)),
                "full_original_modular_relations_verified": True,
                "verification": "all old residual coordinates divisible; all correction coordinates cancel"}
            self.store(self.prime_name(ell, "dixon-"+str(digits+1).zfill(8)), current)

    def complete(self):
        final = self.out/FINAL
        if final.exists():
            cert = read(final)
            assert cert["complete"] and cert["configuration"] == self.tag
            inventory = cert["stage_manifest"]
            assert sha(self.out/inventory["file"]) == inventory["sha256"]
            for item in read(self.out/inventory["file"])["files"]:
                assert (self.out/item["file"]).stat().st_size == item["bytes"]
                assert sha(self.out/item["file"]) == item["sha256"]
            return cert
        self.real_basis()
        while True:
            self.budget()
            selection = self.next_prime()
            ell = selection["prime"]
            try:
                self.rational_blocks(selection)
                chart, branches = self.branches(selection)
                relation, last = self.lift(selection, chart, branches)
                break
            except BadPrime as error:
                self.store(self.prime_name(ell, "rejected"), {
                    "prime": ell, "reason": str(error), "no_exact_y_claimed": True})
                # Rejected-prime matrices are replaceable temporary search data.
                keep = self.path(self.prime_name(ell, "rejected"))
                for path in self.out.glob("R787-prime-"+str(ell)+"-*.json.gz"):
                    if path != keep:
                        path.unlink()
        inventory_path = self.store("R787-exact-stages-manifest", {
            "files": [{"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}
                      for path in sorted(self.out.glob("R787-*.json.gz"))
                      if path.name != "R787-exact-stages-manifest.json.gz"]})
        rank = chart["actual_modular_rank"]
        cert = {"result": RESULT, "configuration": self.tag, "complete": True,
            "p": 41, "original_map_index": 4, "original_map_degree": "1206",
            "exact_nonzero_A_B_relation_verified": True, "original_full_L_retained": True,
            "exact_verified_Laurent_exponents": [-1, 127], "exact_verified_t_coordinates": 20,
            "exact_verified_Q_coordinates_per_order": 280, "exact_verified_orders": 129,
            "actual_y_map_recovered": True, "beta_or_height_computed": False,
            "relation_spec": relation,
            "actual_auxiliary_prime": ell, "actual_modular_Schur_rank": rank,
            "characteristic_zero_Schur_rank": 1186 if rank == 1186 else None,
            "full_characteristic_zero_kernel_claimed": False,
            "actual_Dixon_digits": last["digits"],
            "composite_modulus_matrix_inversion": False,
            "stage_manifest": {"file": inventory_path.name, "bytes": inventory_path.stat().st_size,
                               "sha256": sha(inventory_path)},
            "seconds": time.monotonic()-self.started}
        save(final, cert)
        return cert


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New exact arithmetic belongs to public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "proof", "method", "field-core", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        job = Job(args)
        cert = job.complete()
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(args.output/FINAL),
            "actual_y_map_recovered": True, "beta_or_height_computed": False,
            "exact_verified_orders": 129, "exact_verified_t_coordinates": 20})
        print(json.dumps({"result": RESULT, "complete": True, "seconds": cert["seconds"]}), flush=True)
    except BaseException as error:
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error),
            "all_completed_stages_preserved": True, "actual_y_map_recovered": False})
        raise


if __name__ == "__main__":
    main()

