#!/usr/bin/env python3
"""R873: genuine original cyclic-seven correspondence, only missing sources.

The new public Actions arithmetic appends four original M2 rows, constructs
seventeen exact norm coefficients in H0(8H+4E), and records a source-bound
characteristic-zero unit-solve expression and its actual modular realization.
It does not declare a Picard support, a principal calibration, or a height.
"""
import argparse
from collections import Counter
from functools import lru_cache
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time
import traceback

import flint
from flint import fmpz_poly, nmod_mat
import R786_exact_power5_short_basis as original

RESULT = "R873-original-cyclic-seven-correspondence"
FINAL = "p41-original-cyclic-seven-correspondence-certificate.json"
PREFIX = "R873-"
REPOSITORY = "Rogerhu12/math-research-public"
MANIFEST = "full-outputs-manifest.json"
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
GROUPS = ("R771", "R775", "R786", "R799", "R800", "R801", "R807")
COUNT, OLD_DIM, DIM, REAL, CYC = 110, 2050, 2058, 20, 40
FIRST, STOP, LEVEL, P = 196, 764, 82, 41
M2_INDICES = (0, 1, 2, 73)
ORIGINAL_SHA = "4508095a95a2bcaec8c8db8fcd550fbc618b017d2bc0007945783bc109dbf851"
STRATEGY = {
    "original_curve": "Y=X1/mu3; original minus3 descent; genus127",
    "original_level": 82,
    "original_three_sections": {"tau": [0], "sigma": [1, 73], "w0": [2]},
    "original_M2_scale_already_present": "6724",
    "source_projection": "retain E and original G-level82",
    "target_projection": "quotient E by its chosen cyclic7 subgroup",
    "slash": "det(A)*(c*tau+d)^-2*f(A*tau)",
    "finite_branch_coefficient_automorphism": 6,
    "infinity_branch_coefficient_automorphism": 7,
    "automorphisms_fix_s": True,
    "norm_scalar": "7^6; cancels 7*(1/7)^7",
    "primitive_target": "z=sigma/tau; nonzero q1 distinguishes all eight branches",
    "coarse_norm_space": "H0(8H+4(P0+P1))",
    "coarse_norm_space_dimension": DIM,
    "old_V8_dimension": OLD_DIM,
    "new_complement_dimension": 8,
    "complement_family": "(82^6 E6)^2 times original V2, in original order",
    "common_section_integer_scale": str(82**16),
    "qY_count": COUNT,
    "full_original_xi_coordinates": CYC,
    "full_original_real_coordinates": REAL,
    "selected_M2_indices": list(M2_INDICES),
    "new_M2_exponent_interval": [FIRST, STOP],
    "old_M2_or_E1_prefix_through_195_recomputed": False,
    "old_V8_or_V2_coefficients_or_basis_recomputed": False,
    "old_2050_inverse_previously_available": False,
    "norm_algorithm": "eight T values; division-free 7x7 Berkowitz over Z[xi][q,S]/(q^110,S^2)",
    "interpolation_nodes": list(range(8)),
    "target_coefficients": "P=F(T,0), K=-dF/dS(T,0)",
    "target_function_embedding": "z->U, w->K(U)/P'(U)",
    "char0_coordinate_output": "exact original integer minor inverse applied to exact selected RHS",
    "char0_coordinates_expanded": False,
    "norm_of_line_bundle": "Nm_target(source*I); dual7 involution required for source-norm implementation",
    "original_descent": "cY tau=tau; cY w0=w0; cY sigma=e1-e73; cY z=z-2 e73/tau",
    "old_W_theta_E6_or_Hecke_matrix_recomputed": False,
    "active_eta_support_or_principal_calibration_computed": False,
    "auxiliary_prime_policy": "ascending primes from739 excluding2,3,7,41 and singular old minor",
    "complement_batch_size": 32,
    "budget_excluded_from_mathematical_identity": True,
}


class BudgetStop(RuntimeError):
    pass


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
        raise SystemExit("New R873 mathematical computation belongs to this public repository Actions.")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name+".tmp")
    encoded = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        with temp.open("wb") as stream:
            with gzip.GzipFile(filename="", mode="wb", fileobj=stream, mtime=0) as target:
                target.write(encoded)
    else:
        temp.write_bytes(encoded)
    temp.replace(path)


def plain(row):
    out = {k: row[k] for k in ("file", "bytes", "sha256")}
    assert Path(out["file"]).name == out["file"] and out["file"] not in ("", ".", "..")
    assert isinstance(out["bytes"], int) and out["bytes"] >= 0
    assert len(out["sha256"]) == 64
    return out


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def source_identity(value):
    return {**{k: value[k] for k in BASE},
            "configuration_sha256": value["configuration_sha256"],
            "certificate": plain(value["certificate"]),
            "selected_files_sha256": fingerprint(value["files"])}


def ref(group, row):
    return dict(plain(row), source_group=group)


def prime_generator():
    n = 739
    while True:
        if n not in (2, 3, 7, 41) and all(n % d for d in range(2, math.isqrt(n)+1)):
            yield n
        n += 1


def identity_matrix(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matrix_rows(a):
    return [[int(a[i, j]) for j in range(a.ncols())] for i in range(a.nrows())]


class Source:
    def __init__(self, root, group, spec):
        self.group, self.spec = group, spec
        self.directory = Path(root)/group
        self.files = {n: plain(r) for n, r in spec["files"].items()}
        assert all(n == row["file"] for n, row in self.files.items())
        mpath = self.directory/MANIFEST
        assert sha(mpath) == spec["manifest_sha256"]
        manifest = read(mpath)
        assert manifest["result"] == spec["result"]
        self.entries = {r["file"]: plain(r) for r in manifest["files"]}
        assert len(self.entries) == len(manifest["files"])
        self.entries[MANIFEST] = file_spec(mpath)
        assert all(self.entries[n] == row for n, row in self.files.items())
        self.checked = set()
        self.certificate = self.get(plain(spec["certificate"])["file"])
        assert self.certificate["complete"] is True and self.certificate["result"] == spec["result"]
        self.tag = self.certificate["configuration"]
        assert fingerprint(self.tag) == spec["configuration_sha256"]
        recorded = self.tag.get("source_sha256", self.tag.get("core_sha256"))
        if recorded is not None:
            assert recorded == spec["core_sha256"]
        self.identity = source_identity(spec)

    def get(self, name):
        row = self.files[name]
        path = self.directory/name
        if name not in self.checked:
            assert file_spec(path) == row, (self.group, name, "source bytes")
            self.checked.add(name)
        return read(path)

    def stage(self, row):
        row = plain(row)
        assert self.files[row["file"]] == row
        out = self.get(row["file"])
        assert out["complete"] is True and out["configuration"] == self.tag
        return out

    def named(self, name):
        return self.stage(self.files[name])

    def reference(self, name):
        return ref(self.group, self.files[name])


class Series:
    """Z[xi41][q]/q^110, canonical 40 coefficients; stride79 prevents carries."""
    N, STRIDE = COUNT, 79

    def __init__(self, polynomial=None):
        self.poly = fmpz_poly([]) if polynomial is None else polynomial

    @classmethod
    def zero(cls):
        return cls()

    @classmethod
    def one(cls):
        return cls(fmpz_poly([1]))

    @classmethod
    def from_rows(cls, rows):
        assert len(rows) <= cls.N and all(len(row) == CYC for row in rows)
        a = [0]*(cls.N*cls.STRIDE)
        for n, row in enumerate(rows):
            for r, value in enumerate(row):
                a[cls.STRIDE*n+r] = int(value)
        return cls(fmpz_poly(a))

    def rows(self):
        return [[str(self.poly[self.STRIDE*n+r]) for r in range(CYC)] for n in range(self.N)]

    def __bool__(self):
        return not self.poly.is_zero()

    def __add__(self, other):
        return Series(self.poly+other.poly)

    def __neg__(self):
        return Series(-self.poly)

    def __sub__(self, other):
        return Series(self.poly-other.poly)

    def scale(self, scalar):
        return Series(self.poly*int(scalar))

    def shift(self, exponent):
        assert exponent >= 0
        return Series(self.poly.left_shift(exponent*self.STRIDE).truncate(self.N*self.STRIDE))

    def __mul__(self, other):
        if not self or not other:
            return Series.zero()
        product = self.poly.mul_low(other.poly, self.N*self.STRIDE)
        out = [0]*(self.N*self.STRIDE)
        for n in range(self.N):
            offset = n*self.STRIDE
            last = int(product[offset+40])
            for r in range(CYC):
                value = int(product[offset+r])-last
                if r+41 <= 78:
                    value += int(product[offset+r+41])
                out[offset+r] = value
        return Series(fmpz_poly(out))

    def divide_integer(self, divisor):
        divisor = int(divisor)
        assert divisor > 0
        out = [0]*(self.N*self.STRIDE)
        for n in range(self.N):
            offset = n*self.STRIDE
            for r in range(CYC):
                value = int(self.poly[offset+r])
                quotient, residue = divmod(value, divisor)
                assert residue == 0, ("exact interpolation integer division", divisor, n, r)
                out[offset+r] = quotient
        return Series(fmpz_poly(out))


class Dual:
    def __init__(self, constant=None, linear=None):
        self.a = Series.zero() if constant is None else constant
        self.b = Series.zero() if linear is None else linear

    @classmethod
    def one(cls):
        return cls(Series.one())

    def __add__(self, other):
        return Dual(self.a+other.a, self.b+other.b)

    def __neg__(self):
        return Dual(-self.a, -self.b)

    def __sub__(self, other):
        return Dual(self.a-other.a, self.b-other.b)

    def __mul__(self, other):
        return Dual(self.a*other.a, self.a*other.b+self.b*other.a)

    def rows(self):
        return {"constant": self.a.rows(), "S_coefficient": self.b.rows()}

    @classmethod
    def restore(cls, value):
        return cls(Series.from_rows(value["constant"]), Series.from_rows(value["S_coefficient"]))


class Job:
    def __init__(self, args):
        self.args, self.out, self.started = args, Path(args.output), time.monotonic()
        self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        assert self.item["result"] == RESULT and self.item["p"] == P
        assert self.item["producer_inputs_pending"] is False
        assert sha(__file__) == self.item["core_sha256"]
        assert sha(original.__file__) == self.item["original_helper_sha256"] == ORIGINAL_SHA
        assert flint.__version__ == "0.9.0"
        assert set(self.item["retained_sources"]) == set(GROUPS)
        topic = Path(__file__).resolve().parent.parent
        for key, value in self.item["proofs"].items():
            assert sha(topic/value["path"]) == value["sha256"], key
        self.sources = {g: Source(args.retained, g, self.item["retained_sources"][g]) for g in GROUPS}
        self.inputs = self.item["inputs"]
        self.tag = {"result": RESULT, "source_sha256": sha(__file__),
                    "python_flint": flint.__version__, "p": P,
                    "proofs": self.item["proofs"], "original_helper_sha256": ORIGINAL_SHA,
                    "sources": {g: self.sources[g].identity for g in GROUPS},
                    "inputs": self.inputs, "strategy": STRATEGY}
        self.old_index = self.input("V8_index")
        self.frontier = self.input("V8_frontier")
        self.plan = self.input("recipe_plan")
        self.basis1 = self.input("M2_recipe")
        self.cosets = self.input("determinant_cosets")["cosets"]
        self.group = self.input("label_group")
        assert self.old_index["dimension"] == OLD_DIM
        assert self.old_index["ordinary_power"] == 8 and self.old_index["bound_qY"] == 108
        assert self.old_index["integer_scale"] == str(LEVEL**16)
        assert self.old_index["characteristic_zero_basis_certified"] is True
        assert len(self.old_index["basis_rows"]) == OLD_DIM
        minor = self.old_index["actual_nonzero_minor"]
        assert minor["prime"] == 739 and minor["determinant_mod_prime"] == 148
        assert minor["rows"] == minor["columns"] == OLD_DIM
        self.J = list(minor["coordinate_row_indices"])
        assert len(self.J) == len(set(self.J)) == OLD_DIM
        assert all(0 <= j < 2180 for j in self.J)
        self.R = [i for i in range(2200) if i not in set(self.J)]
        assert len(self.R) == 150
        assert self.frontier["dimension"] == OLD_DIM and self.frontier["coverage_stop"] >= COUNT
        assert self.frontier["ordinary_power"] == 8 and self.frontier["new_first_exponent"] == 109
        assert len(self.frontier["basis_rows"]) == OLD_DIM
        assert self.basis1["rank"] == 146 and len(self.basis1["basis"]) == 146
        # R775's selection q-bound is 273; its saved polynomials still extend through q1640.
        assert self.basis1["coefficient_bound"] == 273
        assert self.sources["R775"].tag["max_exponent_qY"] >= STOP-1
        assert self.basis1["characteristic_zero_independence_certified_by_unit_reduction"] is True
        assert len(self.cosets) == 40 and len(self.group["H82_mod_center"]) == 126
        assert sorted({self.basis1["basis"][i]["recipe"]["R771_seed_index"] for i in M2_INDICES}) == [0, 3]
        self.finite_xi = [pow(538, i, 739) for i in range(CYC)]
        self.eis_rows = {}
        self.old_vectors = None
        T = fmpz_poly([0, 1])
        self.chebyshev = [fmpz_poly([2]), T]
        for _ in range(2, 21):
            self.chebyshev.append(T*self.chebyshev[-1]-self.chebyshev[-2])
        self.real_modulus = fmpz_poly([1])
        for term in self.chebyshev[1:]:
            self.real_modulus += term
        assert self.real_modulus.degree() == 20
        self.source_audit = self.audit()
        self.primitive = self.primitive_witness()

    def input(self, key):
        value = self.inputs[key]
        return self.sources[value["source_group"]].stage(value)

    def path(self, name):
        assert name.startswith(PREFIX) and Path(name).name == name
        return self.out/(name if name.endswith(".json.gz") else name+".json.gz")

    def budget(self):
        if time.monotonic()-self.started >= self.args.budget_minutes*60-45:
            raise BudgetStop("Completed R873 source-bound stages preserved.")

    def cached(self, name):
        p = self.path(name)
        if not p.exists():
            return None
        value = read(p)
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def store(self, name, value):
        p = self.path(name)
        assert not p.exists(), ("immutable R873 completed stage", p.name)
        save(p, dict(value, result=RESULT, complete=True, configuration=self.tag))
        print(json.dumps({"stage": p.name, "bytes": p.stat().st_size,
                          "sha256": sha(p), "seconds": time.monotonic()-self.started}), flush=True)
        return file_spec(p)

    def audit(self):
        name = "R873-original-source-audit"
        old = self.cached(name)
        if old is not None:
            return file_spec(self.path(name))
        records = {}
        for g, source in self.sources.items():
            for name0 in source.files:
                source.get(name0)
            records[g] = {"identity": source.identity, "selected_file_count": len(source.files)}
        return self.store(name, {
            "sources": records, "inputs": self.inputs,
            "old_source_tags_and_bytes_preserved": True,
            "source_fields_resolved_without_old_arithmetic": True,
            "ordinary_V8_not_assumed_to_contain_norms": True,
            "old_2050_minor_determinant": self.old_index["actual_nonzero_minor"],
            "old_2050_inverse_not_present_and_not_claimed": True,
            "new_complement_indices_not_prefilled": True})

    def primitive_witness(self):
        name = "R873-original-target-z-eight-branch-primitive-witness"
        old = self.cached(name)
        if old is not None:
            return file_spec(self.path(name))
        rows, refs = {}, {}
        for i in M2_INDICES:
            n = f"R786-exact-power-1-row-{i:04d}.json.gz"
            value = self.sources["R786"].named(n)
            assert value["bound_qY"] == 128 and value["integer_scale"] == "6724"
            assert value["recipe"] == self.basis1["basis"][i]["recipe"]
            rows[i] = value["integer_qY_xi_coefficients"]
            refs[str(i)] = self.sources["R786"].reference(n)
        assert any(int(x) for x in rows[0][0])
        assert not any(int(x) for x in rows[0][1])
        assert not any(int(x) for x in rows[1][1])
        assert not any(int(x) for x in rows[73][0])
        assert any(int(x) for x in rows[73][1])
        return self.store(name, {
            "original_short_rows": refs,
            "tau_constant_original_xi_coefficients": rows[0][0],
            "sigma_q1_original_xi_coefficients": rows[73][1],
            "tau_constant_nonzero_and_sigma_q1_nonzero": True,
            "tau_q1_e1_q1_and_e73_q0_all_zero": True,
            "finite_target_first_fractional_term": "sigma6(e73_q1/tau_q0)*zeta7^b*q^(1/7)",
            "infinity_target_has_only_q7_powers": True,
            "eight_target_z_values_separated_by_original_q1": True,
            "source_cover_connected_by_original_Gamma_mod7_surjection": True,
            "target_primitive_degree": 8,
            "proof": self.item["proofs"]["R873"]})

    def real_row(self, row, n):
        cyclic = [0]*P
        for r, value in enumerate(row):
            cyclic[(r+10*n) % P] += int(value)
        reduced = [cyclic[r]-cyclic[40] for r in range(40)]+[0]
        assert all(reduced[r] == reduced[P-r] for r in range(1, 21)), (n, "real original phase")
        polynomial = fmpz_poly([reduced[0]])
        for r in range(1, 21):
            polynomial += self.chebyshev[r]*reduced[r]
        polynomial %= self.real_modulus
        return [int(polynomial[i]) for i in range(20)]

    def sigma_row(self, row, exponent):
        cyclic = [0]*P
        for r, value in enumerate(row):
            cyclic[(r*exponent) % P] += int(value)
        return [cyclic[r]-cyclic[40] for r in range(40)]

    def eisenstein_row(self, a):
        if a in self.eis_rows:
            return self.eis_rows[a]
        old_name = f"R786-exact-integral-E1-row-{a:02d}.json.gz"
        tail_name = f"R800-original-E1-tail-row-{a:02d}.json.gz"
        before = self.sources["R786"].named(old_name)
        prior = self.sources["R800"].named(tail_name)
        assert before["first_label_coordinate"] == prior["first_label_coordinate"] == a
        assert before["bound_qY"] == 128 and before["scale"] == LEVEL
        assert prior["first_exponent"] == 129 and prior["last_exponent_exclusive"] == FIRST
        name = f"R873-original-E1-only-new-tail-{a:02d}"
        new = self.cached(name)
        if new is None:
            self.budget()
            finite_name = f"R771-Eisenstein-row-{a:02d}.json.gz"
            finite = self.sources["R771"].named(finite_name)
            assert finite["last_exponent"] >= STOP-1
            tails = []
            for b in range(LEVEL):
                terms = {}
                for sign, residue, exponent in ((1, a, b), (-1, (-a) % LEVEL, (-b) % LEVEL)):
                    start = residue if residue else LEVEL
                    for m in range(start, STOP, LEVEL):
                        for n in range(max(1, (FIRST+m-1)//m), (STOP-1)//m+1):
                            phase_sign, r = original.phase(exponent*n)
                            key = (m*n, r)
                            terms[key] = terms.get(key, 0)+phase_sign*sign*LEVEL
                tail = original.canonical_sparse(terms)
                values = [0]*(STOP-FIRST)
                for n, r, coefficient in tail:
                    values[n-FIRST] += coefficient*pow(538, r, 739)
                reference = finite["series_by_second_coordinate"][b]
                for offset, actual in enumerate(values):
                    exponent = FIRST+offset
                    expected = LEVEL*(int(reference[exponent]) if exponent < len(reference) else 0) % 739
                    assert actual % 739 == expected, (a, b, exponent)
                tails.append(tail)
            self.store(name, {
                "first_label_coordinate": a, "first_exponent": FIRST,
                "last_exponent_exclusive": STOP, "integer_scale": LEVEL,
                "sparse_new_terms_by_second_coordinate": tails,
                "original_R786_prefix": self.sources["R786"].reference(old_name),
                "original_R800_tail": self.sources["R800"].reference(tail_name),
                "original_R771_finite_comparison": self.sources["R771"].reference(finite_name),
                "all_new_mod739_coefficients_verified": True,
                "old_constant_or_coefficients_through_195_recomputed": False})
            new = self.cached(name)
        rows = []
        for p0, p1, p2 in zip(before["sparse_series_by_second_coordinate"],
                              prior["sparse_new_terms_by_second_coordinate"],
                              new["sparse_new_terms_by_second_coordinate"]):
            one = [tuple(map(int, row)) for row in p0]
            two = [tuple(map(int, row)) for row in p1]
            three = [tuple(map(int, row)) for row in p2]
            assert all(0 <= n < 129 for n, _, _ in one)
            assert all(129 <= n < FIRST for n, _, _ in two)
            assert all(FIRST <= n < STOP for n, _, _ in three)
            assert one == sorted(one) and two == sorted(two) and three == sorted(three)
            rows.append(one+two+three)
        assert len(rows) == LEVEL
        self.eis_rows[a] = rows
        return rows

    @lru_cache(maxsize=4096)
    def pair_tail(self, first, second):
        self.budget()
        left = self.eisenstein_row(first[0])[first[1]]
        right = self.eisenstein_row(second[0])[second[1]]
        total = {}
        for n, r, x in left:
            for m, s, y in right:
                degree = n+m
                if degree >= STOP:
                    break
                if degree < FIRST:
                    continue
                key = (degree, (r+s) % P)
                total[key] = total.get(key, 0)+x*y
        return original.canonical_sparse(total)

    def seed_tail(self, seed_index, position):
        name = f"R873-original-seed-only-new-tail-{seed_index:03d}-{position:02d}"
        old = self.cached(name)
        seed = self.sources["R771"].certificate["M2_exact_seeds"][seed_index]
        if old is not None:
            assert old["original_seed"] == seed and old["seed_index"] == seed_index
            return old["cyclic_new_terms"]
        self.budget()
        pairs = Counter()
        matrix = tuple(self.cosets[position]["matrix"])
        for h in self.group["H82_mod_center"]:
            hg = original.mm(tuple(h), matrix)
            pair = tuple(sorted((original.action(seed["lambda"], hg), original.action(seed["mu"], hg))))
            pairs[pair] += 1
        assert sum(pairs.values()) == 126
        total = {}
        for (first, second), multiplicity in pairs.items():
            for n, r, value in self.pair_tail(first, second):
                total[(n, r)] = total.get((n, r), 0)+multiplicity*value
        terms = original.canonical_sparse(total)
        self.store(name, {
            "seed_index": seed_index, "coset_position": position, "original_seed": seed,
            "determinant_mod82": self.cosets[position]["det_mod82"],
            "first_exponent": FIRST, "last_exponent_exclusive": STOP, "integer_scale": "6724",
            "cyclic_new_terms": terms, "trace_terms_with_multiplicity": 126,
            "old_seed_prefix_recomputed": False})
        return terms

    def m2_rows(self, index):
        assert index in M2_INDICES
        name = f"R873-original-selected-M2-only-new-tail-{index:04d}"
        old = self.cached(name)
        recipe = self.basis1["basis"][index]["recipe"]
        original_name = f"R786-exact-power-1-row-{index:04d}.json.gz"
        prior_name = f"R800-original-M2-tail-row-{index:04d}.json.gz"
        before = self.sources["R786"].named(original_name)
        prior = self.sources["R800"].named(prior_name)
        assert before["recipe"] == prior["recipe"] == recipe
        assert before["bound_qY"] == 128 and before["integer_scale"] == "6724"
        assert prior["first_exponent"] == 129 and prior["last_exponent_exclusive"] == FIRST
        if old is None:
            self.budget()
            r, j = recipe["R771_seed_index"], recipe["j"]
            seed = self.sources["R771"].certificate["M2_exact_seeds"][r]
            assert recipe["lambda"] == seed["lambda"] and recipe["mu"] == seed["mu"]
            blocks = [[0]*P for _ in range(STOP-FIRST)]
            for position, coset in enumerate(self.cosets):
                sign, shift = original.phase(j*coset["det_mod82"])
                for n, r0, value in self.seed_tail(r, position):
                    blocks[int(n)-FIRST][(int(r0)+shift) % P] += sign*int(value)
            rows = [[row[r0]-row[40] for r0 in range(CYC)] for row in blocks]
            finite = self.basis1["basis"][index]["coefficients_mod_ell"]
            for n, row in enumerate(rows, FIRST):
                actual = sum(x*y for x, y in zip(row, self.finite_xi)) % 739
                expected = 6724*(int(finite[n]) if n < len(finite) else 0) % 739
                assert actual == expected, (index, n, "original finite coefficient")
            real = [self.real_row(row, n) for n, row in enumerate(rows, FIRST)]
            self.store(name, {
                "index": index, "recipe": recipe, "weight": 2, "integer_scale": "6724",
                "first_exponent": FIRST, "last_exponent_exclusive": STOP,
                "integer_qY_xi_coefficients": [[str(x) for x in row] for row in rows],
                "integer_v_t_coefficients": [[str(x) for x in row] for row in real],
                "original_R786_prefix": self.sources["R786"].reference(original_name),
                "original_R800_tail": self.sources["R800"].reference(prior_name),
                "all_new_original_mod739_coefficients_verified": True,
                "all_new_real_tangent_involutions_verified": True,
                "old_prefix_recomputed": False})
            old = self.cached(name)
        result = [[int(x) for x in row] for row in before["integer_qY_xi_coefficients"]]
        result += [[int(x) for x in row] for row in prior["integer_qY_xi_coefficients"]]
        result += [[int(x) for x in row] for row in old["integer_qY_xi_coefficients"]]
        assert len(result) == STOP and all(len(row) == CYC for row in result)
        return result

    def original_v8_vectors(self):
        if self.old_vectors is not None:
            return self.old_vectors
        self.budget()
        nodes = {v["node_key"]: v for v in self.plan["nodes"]}
        assert len(nodes) == len(self.plan["nodes"])
        assert self.plan["primary_targets"]["8"] == [v["node_key"] for v in self.frontier["basis_rows"]]
        columns = []
        sources = []
        for i, (entry, frontier) in enumerate(zip(self.old_index["basis_rows"], self.frontier["basis_rows"])):
            self.budget()
            assert entry["index"] == frontier["index"] == i
            old = self.sources["R799"].stage(entry)
            assert old["integer_scale"] == str(LEVEL**16) and old["bound_qY"] == 108
            assert old["recipe"] == frontier["original_recipe"]
            node = nodes[frontier["node_key"]]
            assert node["node_fingerprint"] == frontier["node_fingerprint"]
            assert node["ordinary_power"] == 8 and node["original_recipe"] == old["recipe"]
            original_specs = [v for v in frontier["original_prefix_segments"]
                              if v["producer"] == "R799" and v["first"] == 0 and v["stop"] == 109]
            assert len(original_specs) == 1 and plain(original_specs[0]) == plain(entry)
            tails = [v for v in frontier["new_tail_segments"] if v["first"] <= 109 < v["stop"]]
            assert len(tails) == 1 and tails[0]["producer"] == "R801"
            tail = self.sources["R801"].stage(tails[0])
            assert tail["node_key"] == frontier["node_key"]
            assert tail["node_fingerprint"] == frontier["node_fingerprint"]
            assert tail["first_exponent"] == tails[0]["first"]
            assert tail["last_exponent_exclusive"] == tails[0]["stop"]
            assert tail["old_coefficients_recomputed"] is False
            rows = old["integer_v_t_coefficients"]
            assert len(rows) == 109 and all(len(row) == REAL for row in rows)
            last = tail["integer_v_t_coefficients"][109-tails[0]["first"]]
            assert len(last) == REAL
            flat = [int(v) for row in rows for v in row]+[int(v) for v in last]
            assert len(flat) == 2200
            columns.append(flat)
            sources.append({"index": i, "node_key": frontier["node_key"],
                            "original_prefix": ref("R799", entry), "only_q109_from": ref("R801", tails[0])})
        self.old_vectors = columns
        self.old_vector_sources = sources
        return columns

    def complement_candidate(self, index):
        name = f"R873-E6-square-V2-candidate-{index:04d}"
        value = self.cached(name)
        if value is None:
            self.budget()
            original_name = f"R786-exact-power-2-row-{index:04d}.json.gz"
            old = self.sources["R786"].named(original_name)
            assert old["bound_qY"] == 128 and old["weight"] == 4
            assert old["integer_scale"] == str(LEVEL**4)
            rows0 = old["integer_qY_xi_coefficients"]
            assert len(rows0) == 129 and all(len(row) == CYC for row in rows0)
            rows = [[LEVEL**12*(int(rows0[n][r])-1008*(int(rows0[n-82][r]) if n >= 82 else 0))
                     for r in range(CYC)] for n in range(COUNT)]
            real = [self.real_row(row, n) for n, row in enumerate(rows)]
            self.store(name, {
                "original_V2_index": index, "original_V2": self.sources["R786"].reference(original_name),
                "original_V2_recipe": old["recipe"],
                "section_expression": "(82^6 E6)^2 * original e_(2,index)",
                "integer_scale": str(LEVEL**16), "qY_count": COUNT,
                "E6_square_factor_to_q109": {"q0": str(LEVEL**12), "q82": str(-1008*LEVEL**12)},
                "integer_qY_xi_coefficients": [[str(x) for x in row] for row in rows],
                "integer_v_t_coefficients": [[str(x) for x in row] for row in real],
                "old_V2_product_recomputed": False,
                "exact_section_in_H0_8H_plus_4E": True,
                "all_original_real_phase_coordinates_verified": True})
            value = self.cached(name)
        return [int(x) for row in value["integer_v_t_coefficients"] for x in row], file_spec(self.path(name))

    def original_block_inverse(self, prime):
        name = f"R873-prime-{prime}-old2050-modular-inverse"
        value = self.cached(name)
        if value is None:
            self.budget()
            columns = self.original_v8_vectors()
            matrix = nmod_mat([[columns[c][r] % prime for c in range(OLD_DIM)] for r in self.J], prime)
            determinant = int(matrix.det())
            if prime == 739:
                assert determinant == 148
            if not determinant:
                return None, 0, None
            inverse = matrix.inv()
            unit = nmod_mat(identity_matrix(OLD_DIM), prime)
            assert matrix*inverse == unit and inverse*matrix == unit
            self.store(name, {
                "prime": prime, "original_V8_index": self.inputs["V8_index"],
                "selected_original_rows": self.J, "actual_determinant_mod_prime": determinant,
                "inverse_mod_prime": matrix_rows(inverse),
                "both_inverse_products_verified": True,
                "old2050_inverse_previously_available": False,
                "original_basis_recomputed": False})
            value = self.cached(name)
        assert value["prime"] == prime and value["selected_original_rows"] == self.J
        assert value["both_inverse_products_verified"] is True
        return nmod_mat(value["inverse_mod_prime"], prime), int(value["actual_determinant_mod_prime"]), file_spec(self.path(name))

    def choose_basis(self):
        name = "R873-original-2058-section-basis-unit-minor"
        accepted = self.cached(name)
        if accepted is not None:
            self.prime = accepted["prime"]
            self.accepted_basis = accepted
            self.accepted_basis_spec = file_spec(self.path(name))
            return self.accepted_basis_spec
        columns = self.original_v8_vectors()
        for prime in prime_generator():
            self.budget()
            bad_name = f"R873-prime-{prime}-basis-search-completed-nonunit"
            if self.cached(bad_name) is not None:
                continue
            inverse, det0, inverse_spec = self.original_block_inverse(prime)
            if inverse is None:
                self.store(bad_name, {"prime": prime, "reason": "old selected minor is zero at this prime",
                                     "characteristic_zero_dependence_claimed": False})
                continue
            bottom = nmod_mat([[columns[c][r] % prime for c in range(OLD_DIM)] for r in self.R], prime)
            selected, pivots, echelon = [], [], []
            for first in range(0, 418, 32):
                self.budget()
                batch_name = f"R873-prime-{prime}-eight-complement-batch-{first:04d}"
                batch = self.cached(batch_name)
                if batch is None:
                    stop = min(418, first+32)
                    candidate_data = [self.complement_candidate(i) for i in range(first, stop)]
                    top = nmod_mat([[v[r] % prime for v, _ in candidate_data] for r in self.J], prime)
                    projections = inverse*top
                    remaining = nmod_mat([[v[r] % prime for v, _ in candidate_data] for r in self.R], prime)
                    residual = remaining-bottom*projections
                    actual_stop = stop
                    for offset, (vector, spec0) in enumerate(candidate_data):
                        v = [int(residual[i, offset]) for i in range(150)]
                        for pivot, existing in zip(pivots, echelon):
                            scalar = v[pivot]
                            if scalar:
                                v = [(a-scalar*b) % prime for a, b in zip(v, existing)]
                        pivot = next((i for i, x in enumerate(v) if x), None)
                        if pivot is not None:
                            scalar = pow(v[pivot], -1, prime)
                            v = [(x*scalar) % prime for x in v]
                            selected.append({"original_V2_index": first+offset, "candidate": spec0})
                            pivots.append(pivot)
                            echelon.append(v)
                            if len(selected) == 8:
                                actual_stop = first+offset+1
                                break
                    self.store(batch_name, {
                        "prime": prime, "first_original_V2_index": first, "stop_original_V2_index": actual_stop,
                        "old_inverse": inverse_spec, "selected": selected, "residual_pivot_positions": pivots,
                        "residual_echelon_columns": echelon, "actual_selected_count": len(selected),
                        "actual_residual_dimension": 150, "rank_eight_preassigned": False})
                    batch = self.cached(batch_name)
                assert batch["prime"] == prime and batch["old_inverse"] == inverse_spec
                selected = list(batch["selected"])
                pivots = list(batch["residual_pivot_positions"])
                echelon = list(batch["residual_echelon_columns"])
                assert len(selected) == len(pivots) == len(echelon) <= 8
                if len(selected) == 8:
                    break
            if len(selected) != 8:
                self.store(bad_name, {"prime": prime, "reason": "actual complement rank below eight modulo prime",
                                     "actual_complement_rank": len(selected),
                                     "characteristic_zero_dependence_claimed": False})
                continue
            self.budget()
            extra = [self.complement_candidate(row["original_V2_index"])[0] for row in selected]
            top = nmod_mat([[v[r] % prime for v in extra] for r in self.J], prime)
            W = inverse*top
            new_rows = [self.R[i] for i in pivots]
            C = nmod_mat([[columns[c][r] % prime for c in range(OLD_DIM)] for r in new_rows], prime)
            D = nmod_mat([[v[r] % prime for v in extra] for r in new_rows], prime)
            schur = D-C*W
            detS = int(schur.det())
            assert detS
            Sinv = schur.inv()
            unit8 = nmod_mat(identity_matrix(8), prime)
            assert schur*Sinv == unit8 and Sinv*schur == unit8
            self.store(name, {
                "prime": prime, "old_inverse": inverse_spec, "old_2050_coordinate_rows": self.J,
                "new_eight_coordinate_rows": new_rows, "selected_coordinate_rows": self.J+new_rows,
                "selected_complement": selected, "old_minor_determinant": det0,
                "actual_schur_determinant": detS,
                "actual_2058_minor_determinant": det0*detS % prime,
                "Schur_matrix": matrix_rows(schur), "Schur_inverse": matrix_rows(Sinv),
                "old_inverse_times_eight_new_top_columns": matrix_rows(W),
                "both_Schur_inverse_products_verified": True,
                "original_space_dimension": 2058, "independent_columns": 2058,
                "actual_nonzero_minor_rank": 2058,
                "exact_section_basis_certified_by_original_RR_dimension": True,
                "ordinary_V8_containment_of_norms_claimed": False,
                "source_old_2050_index": self.inputs["V8_index"],
                "source_old_q109_frontier": self.inputs["V8_frontier"],
                "source_original_recipe_plan": self.inputs["recipe_plan"]})
            self.prime = prime
            self.accepted_basis = self.cached(name)
            self.accepted_basis_spec = file_spec(self.path(name))
            return self.accepted_basis_spec
        raise AssertionError("unreachable infinite prime iterator")

    def finite_norm_matrix(self, node, m2):
        tau, e1, w0, e73 = [m2[i] for i in (0, 1, 2, 73)]
        sigma = [[a+b for a, b in zip(e1[n], e73[n])] for n in range(STOP)]
        residue = []
        for r in range(7):
            arows, brows = [[0]*CYC for _ in range(COUNT)], [[0]*CYC for _ in range(COUNT)]
            for exponent in range(r, STOP, 7):
                k = (exponent-r)//7
                arows[k] = self.sigma_row([node*a-b for a, b in zip(tau[exponent], sigma[exponent])], 6)
                brows[k] = self.sigma_row([-a for a in w0[exponent]], 6)
            residue.append(Dual(Series.from_rows(arows), Series.from_rows(brows)))
        return [[Dual(residue[(i-j) % 7].a.shift(int(i < j)),
                      residue[(i-j) % 7].b.shift(int(i < j)))
                 for j in range(7)] for i in range(7)]

    def finite_norm_node(self, node, m2):
        final_name = f"R873-finite-seven-norm-T-{node}-Berkowitz-07"
        last = self.cached(final_name)
        if last is not None:
            return -Dual.restore(last["characteristic_coefficients"][-1])
        matrix = self.finite_norm_matrix(node, m2)
        prior = [Dual.one()]
        previous_spec = None
        for size in range(1, 8):
            self.budget()
            name = f"R873-finite-seven-norm-T-{node}-Berkowitz-{size:02d}"
            stage = self.cached(name)
            if stage is not None:
                prior = [Dual.restore(v) for v in stage["characteristic_coefficients"]]
                assert stage["size"] == size and stage["T_node"] == node
                previous_spec = file_spec(self.path(name))
                continue
            start = 7-size
            a = matrix[start][start]
            h = [Dual.one(), -a]
            if size >= 2:
                R = matrix[start][start+1:]
                C = [matrix[i][start] for i in range(start+1, 7)]
                M = [row[start+1:] for row in matrix[start+1:]]
                for exponent in range(size-1):
                    dot = Dual()
                    for x, y in zip(R, C):
                        dot = dot+x*y
                    h.append(-dot)
                    if exponent+1 < size-1:
                        next_C = []
                        for row in M:
                            value = Dual()
                            for x, y in zip(row, C):
                                value = value+x*y
                            next_C.append(value)
                        C = next_C
                    self.budget()
            assert len(h) == size+1 and len(prior) == size
            result = []
            for i in range(size+1):
                value = Dual()
                for j in range(min(i, size-1)+1):
                    value = value+h[i-j]*prior[j]
                result.append(value)
            previous_spec = self.store(name, {
                "T_node": node, "size": size, "principal_submatrix": "bottom-right",
                "previous_Berkowitz_stage": previous_spec,
                "characteristic_coefficients": [v.rows() for v in result],
                "coefficient_order": "descending characteristic-polynomial powers",
                "arithmetic": "division-free Berkowitz over Z[xi41][q,S]/(q^110,S^2)",
                "finite_input_tail_stages": [file_spec(self.path(f"R873-original-selected-M2-only-new-tail-{i:04d}"))
                                              for i in M2_INDICES],
                "norm_determinant_sign": -1 if size % 2 else 1,
                "qY_count": COUNT, "old_seed_or_prefix_recomputed": False})
            prior = result
        return -prior[-1]

    def norm_targets(self):
        index_name = "R873-seventeen-original-section-norm-target-index"
        old = self.cached(index_name)
        if old is not None:
            self.target_index = old
            self.target_index_spec = file_spec(self.path(index_name))
            return self.target_index_spec
        m2 = {i: self.m2_rows(i) for i in M2_INDICES}
        interp_name = "R873-finite-seven-norm-exact-T-interpolation"
        interpolation = self.cached(interp_name)
        if interpolation is None:
            values = [self.finite_norm_node(node, m2) for node in range(8)]
            difference = list(values)
            first = []
            while difference:
                first.append(difference[0])
                difference = [difference[i+1]-difference[i] for i in range(len(difference)-1)]
            denominator = math.factorial(7)
            falling = [1]
            raw = [Dual() for _ in range(8)]
            for k in range(8):
                scale = denominator//math.factorial(k)
                for j, coefficient in enumerate(falling):
                    raw[j] = raw[j]+Dual(first[k].a.scale(scale*coefficient),
                                         first[k].b.scale(scale*coefficient))
                next_falling = [0]*(len(falling)+1)
                for j, coefficient in enumerate(falling):
                    next_falling[j] -= k*coefficient
                    next_falling[j+1] += coefficient
                falling = next_falling
            result = [Dual(v.a.divide_integer(denominator), v.b.divide_integer(denominator)) for v in raw]
            assert not result[7].b
            for node, expected in enumerate(values):
                actual = Dual()
                for value in reversed(result):
                    actual = Dual(actual.a.scale(node), actual.b.scale(node))+value
                assert actual.a.poly == expected.a.poly and actual.b.poly == expected.b.poly
            self.store(interp_name, {
                "T_nodes": list(range(8)), "coefficients_ascending_T": [v.rows() for v in result],
                "finite_norm_constant_T_degree_bound": 7, "finite_norm_S_T_degree_bound": 6,
                "all_eight_original_node_values_verified": True,
                "all_interpolation_integer_divisions_verified": True,
                "new_nonintegral_coefficient_field_introduced": False,
                "finite_node_stages": [file_spec(self.path(f"R873-finite-seven-norm-T-{n}-Berkowitz-07"))
                                       for n in range(8)]})
            interpolation = self.cached(interp_name)
        finite = [Dual.restore(v) for v in interpolation["coefficients_ascending_T"]]
        tau_inf, sigma_inf, w_inf = [[[0]*CYC for _ in range(COUNT)] for _ in range(3)]
        for n in range((COUNT-1)//7+1):
            tau_inf[7*n] = self.sigma_row(m2[0][n], 7)
            sigma_inf[7*n] = self.sigma_row([a+b for a, b in zip(m2[1][n], m2[73][n])], 7)
            w_inf[7*n] = self.sigma_row(m2[2][n], 7)
        t, s, w = (Series.from_rows(v) for v in (tau_inf, sigma_inf, w_inf))
        targets = []
        for kind, size in (("P", 9), ("K", 8)):
            for j in range(size):
                self.budget()
                name = f"R873-original-norm-target-{kind}-{j:02d}"
                stage = self.cached(name)
                if stage is None:
                    left = finite[j-1] if j else Dual()
                    right = finite[j] if j < 8 else Dual()
                    value = left.a*t-right.a*s if kind == "P" else right.a*w-left.b*t+right.b*s
                    rows = value.rows()
                    real = [self.real_row(row, n) for n, row in enumerate(rows)]
                    if kind == "P" and j == 8:
                        assert value
                    self.store(name, {
                        "polynomial": kind, "T_power": j,
                        "integer_qY_xi_coefficients": rows,
                        "integer_v_t_coefficients": [[str(x) for x in row] for row in real],
                        "integer_scale": str(LEVEL**16), "qY_count": COUNT,
                        "source_finite_interpolation": file_spec(self.path(interp_name)),
                        "definition": "F=7^6 product(T tau-slash - sigma-slash - S w0-slash); P=F|S0,K=-dS F|S0",
                        "infinity_branch_sigma7_used": True, "finite_branch_sigma6_used": True,
                        "seven_power_scalar_cancelled_exactly": True,
                        "exact_membership_H0_8H_plus_4E_by_original_correspondence": True,
                        "all_original_real_phase_coordinates_verified": True,
                        "ordinary_V8_membership_claimed": False})
                targets.append(file_spec(self.path(name)))
        self.store(index_name, {
            "targets": targets, "actual_target_count": len(targets),
            "P_coefficients": targets[:9], "K_coefficients": targets[9:],
            "finite_interpolation": file_spec(self.path(interp_name)),
            "source_primitive_witness": self.primitive,
            "P_degree": 8, "K_degree_bound": 7,
            "P_leading_coefficient_nonzero": True,
            "P_over_fraction_field_irreducible_separable_degree8_by_original_branch_primitive_proof": True,
            "qY_count": COUNT, "all_17_source_bound_exact_sections_completed": True})
        self.target_index = self.cached(index_name)
        self.target_index_spec = file_spec(self.path(index_name))
        return self.target_index_spec

    def coordinate_expression(self):
        name = "R873-seventeen-exact-unit-solve-and-modular-coordinate-expression"
        stage = self.cached(name)
        if stage is not None:
            self.coordinate_spec = file_spec(self.path(name))
            return self.coordinate_spec
        self.budget()
        basis = self.accepted_basis
        prime = basis["prime"]
        columns = self.original_v8_vectors()
        inverse, det0, inverse_spec = self.original_block_inverse(prime)
        assert inverse_spec == basis["old_inverse"]
        extra = [self.complement_candidate(row["original_V2_index"])[0]
                 for row in basis["selected_complement"]]
        targets = [read(self.out/v["file"]) for v in self.target_index["targets"]]
        right = [[int(x) for row in v["integer_v_t_coefficients"] for x in row] for v in targets]
        assert len(right) == 17 and all(len(v) == 2200 for v in right)
        solve_name = f"R873-prime-{prime}-seventeen-coordinate-modular-solve"
        solved = self.cached(solve_name)
        if solved is None:
            top_rhs = nmod_mat([[v[r] % prime for v in right] for r in self.J], prime)
            top_solution = inverse*top_rhs
            new_rows = basis["new_eight_coordinate_rows"]
            C = nmod_mat([[columns[c][r] % prime for c in range(OLD_DIM)] for r in new_rows], prime)
            tail_rhs = nmod_mat([[v[r] % prime for v in right] for r in new_rows], prime)
            extra_solution = nmod_mat(basis["Schur_inverse"], prime)*(tail_rhs-C*top_solution)
            old_solution = top_solution-nmod_mat(basis["old_inverse_times_eight_new_top_columns"], prime)*extra_solution
            self.store(solve_name, {
                "prime": prime, "basis_minor": self.accepted_basis_spec,
                "target_index": self.target_index_spec,
                "modular_coordinates": matrix_rows(old_solution)+matrix_rows(extra_solution),
                "selected_row_solve_complete": True,
                "all2200_row_verification_not_yet_claimed": True})
            solved = self.cached(solve_name)
        assert solved["prime"] == prime and solved["basis_minor"] == self.accepted_basis_spec
        assert solved["target_index"] == self.target_index_spec
        old_solution = nmod_mat(solved["modular_coordinates"][:OLD_DIM], prime)
        extra_solution = nmod_mat(solved["modular_coordinates"][OLD_DIM:], prime)
        # Every original coordinate is checked, in bounded row batches.
        checked = []
        for first in range(0, 2200, 100):
            self.budget()
            stop = min(first+100, 2200)
            verify_name = f"R873-prime-{prime}-all17-coordinate-check-{first:04d}-{stop:04d}"
            prior = self.cached(verify_name)
            if prior is None:
                A = nmod_mat([[columns[c][r] % prime for c in range(OLD_DIM)]
                              for r in range(first, stop)], prime)
                B = nmod_mat([[v[r] % prime for v in extra] for r in range(first, stop)], prime)
                target = nmod_mat([[v[r] % prime for v in right] for r in range(first, stop)], prime)
                assert A*old_solution+B*extra_solution == target
                self.store(verify_name, {
                    "prime": prime, "first_coordinate": first, "stop_coordinate": stop,
                    "basis_minor": self.accepted_basis_spec, "target_index": self.target_index_spec,
                    "target_count": 17, "all_rows_mod_prime_verified": True,
                    "characteristic_zero_expanded_coordinate_claimed": False})
            checked.append(file_spec(self.path(verify_name)))
        rows = matrix_rows(old_solution)+matrix_rows(extra_solution)
        self.store(name, {
            "basis_minor": self.accepted_basis_spec, "target_index": self.target_index_spec,
            "selected_coordinate_rows": basis["selected_coordinate_rows"],
            "exact_expression": {
                "operation": "inverse_of_exact_original_integer_minor_times_selected_exact_integer_rhs",
                "matrix_shape": [2058, 2058], "rhs_shape": [2058, 17],
                "row_order": "selected_coordinate_rows; each coordinate is20*n+t_power",
                "column_order": "2050 original V8, then eight actual selected E6hat^2 V2",
                "matrix_source_basis": self.accepted_basis_spec,
                "rhs_sources": self.target_index["targets"],
                "source_prefix_injectivity": "20*110>deg(8H+4E)=2184",
                "prior_global_membership_and_complete_basis_proved": True,
                "exact_characteristic_zero_expression_defined": True,
                "characteristic_zero_inverse_or_coordinates_expanded": False},
            "prime": prime, "modular_coordinates": rows,
            "all2200_coordinates_for_all17_targets_verified_mod_prime": True,
            "coordinate_verification_stages": checked,
            "completed_modular_solve": file_spec(self.path(solve_name)),
            "exact_expression_not_a_rational_reconstruction_candidate": True,
            "auxiliary_prime_unit_denominator_certified": True,
            "exact_expanded_char0_coordinate_acceptance_claimed": False,
            "new2058_inverse_over_Q_computed": False,
            "old_completed_arithmetic_recomputed": False})
        self.coordinate_spec = file_spec(self.path(name))
        return self.coordinate_spec

    def function_program(self):
        name = "R873-original-cyclic-seven-source-target-function-DAG"
        stage = self.cached(name)
        if stage is not None:
            self.program_spec = file_spec(self.path(name))
            return self.program_spec
        self.budget()
        nodes = {row["node_key"]: row for row in self.plan["nodes"]}
        identity_keys = ("node_key", "ordinary_power", "original_recipe", "factor_nodes",
                         "integer_scale", "original_reference_index")
        memo = {}
        visiting = set()
        def leaves(key):
            if key in memo:
                return memo[key]
            assert key not in visiting
            visiting.add(key)
            node = nodes[key]
            assert fingerprint({k: node[k] for k in identity_keys}) == node["node_fingerprint"]
            power = node["ordinary_power"]
            assert node["integer_scale"] == str(LEVEL**(2*power))
            if power == 1:
                assert not node["factor_nodes"]
                i = node["original_reference_index"]
                assert 0 <= i < 146 and node["original_recipe"] == self.basis1["basis"][i]["recipe"]
                answer = [i]
            else:
                assert len(node["factor_nodes"]) == 2
                answer = sorted(leaves(node["factor_nodes"][0])+leaves(node["factor_nodes"][1]))
                assert len(answer) == power
            visiting.remove(key)
            memo[key] = answer
            return answer
        old_monomials = []
        for index, key in enumerate(self.plan["primary_targets"]["8"]):
            old_monomials.append({"index": index, "source_node_key": key,
                                  "original_M2_leaf_indices": leaves(key),
                                  "function": "product(e_i/tau) over original_M2_leaf_indices"})
        assert len(old_monomials) == 2050
        theta = self.input("theta")
        clearing = self.input("E6_clearing")
        assert theta["theta_nonzero_by_original_independent_M2_input"] is True
        assert theta["M6_index692_cleared_coordinate_stage"] == plain(self.inputs["E6_clearing"])
        assert clearing["M6_index"] == 692 and clearing["source_M6_recipe"] == {"kind": "level_one", "name": "E6"}
        assert clearing["all1100_rows_verified"] is True
        assert clearing["exact_global_V4_membership_certified"] is True
        assert clearing["basis_dimension"] == 962 and clearing["basis_integer_scale"] == str(LEVEL**8)
        assert len(clearing["solution_numerators"]) == 962
        assert int(clearing["solution_common_denominator"]) > 0
        v4 = []
        for index, numerator in enumerate(clearing["solution_numerators"]):
            if int(numerator):
                key = f"o04-i{index:04d}"
                v4.append({"original_V4_index": index, "original_M2_leaf_indices": leaves(key),
                           "source_coordinate_index": index})
        complement = []
        for i, row in enumerate(self.accepted_basis["selected_complement"]):
            j = row["original_V2_index"]
            key = f"o02-i{j:04d}"
            source = self.sources["R786"].named(f"R786-exact-power-2-row-{j:04d}.json.gz")
            assert nodes[key]["original_recipe"] == source["recipe"]
            complement.append({"index": 2050+i, "original_V2_index": j,
                               "original_M2_leaf_indices": leaves(key),
                               "function": "E6hat_over_tau3^2 * product(e_i/tau)",
                               "new_exact_section": row["candidate"]})
        self.store(name, {
            "source_field": "the original K(Y), not a replacement curve or a twist",
            "source_K_definition": "K=Q(s),s^2=-3; original level82 determinant normalization",
            "source_original_M2_recipes": self.inputs["M2_recipe"],
            "source_original_recipe_plan": self.inputs["recipe_plan"],
            "original_M2_function_leaf": "e_i/tau with original e_i=82^2*T_(1,i)",
            "original_tau_leaf_index": 0,
            "original_z_function": {"sum_M2_indices": [1, 73], "denominator_M2_index": 0},
            "original_w_function": {"M2_index": 2, "denominator_M2_index": 0},
            "old_V8_over_tau8": old_monomials,
            "E6hat_over_tau3": {
                "operation": "exact_quotient",
                "numerator": "sum original R807 c_k times original V4_k/tau^4",
                "denominator": "sum original R807 lambda_i times e_i/tau",
                "theta_source": self.inputs["theta"],
                "V4_coordinate_source": self.inputs["E6_clearing"],
                "nonzero_V4_monomials": v4,
                "all_R807_denominators_and_original_normalization_preserved": True,
                "E6hat_scale": str(LEVEL**6), "theta_scale": str(LEVEL**2),
                "V4_scale": str(LEVEL**8), "new_scale_applied": "1",
                "theta_nonzero_source_certified": True},
            "new_eight_complement_functions": complement,
            "coefficient_unit_solve": self.coordinate_spec,
            "coefficient_interpretation": "each exact unit-solve column multiplies the2058 listed functions",
            "P_over_tau8_coefficients": {"unit_solve_columns": list(range(9)), "powers_U": list(range(9))},
            "K_over_tau8_coefficients": {"unit_solve_columns": list(range(9, 17)), "powers_U": list(range(8))},
            "correspondence_function_field": {
                "definition": "K(Y)[U]/(P(U)/a8)",
                "degree_over_source": 8,
                "P_irreducible_and_separable_char0_from_eight_actual_branches": True,
                "source_projection": "pi_s(E,level,C7)=(E,level)",
                "target_projection": "pi_t(E,level,C7)=(E/C7,transported level)",
                "source_embedding": "identity on original K(Y)",
                "target_z": "U", "target_w": "K(U)/P'(U)",
                "leading_coefficient_a8_nonzero": True,
                "Pprime_nonzero_in_original_correspondence_function_field": True,
                "proper_curve": "normalization of original Y in the displayed degree8 function field",
                "poles_and_branch_locus_retained_by_normalization": True,
                "normalization_integral_bases_expanded": False,
                "finite_maps_source_and_target_degree": [8, 8],
                "modular_specialization_separability_not_presumed": True},
            "rigidified_Hecke_transport": {
                "frozen_direction": "Nm_pi_t(pi_s^*I)",
                "source_norm_alternative": "Nm_pi_s(j^*pi_s^*I)=Nm_pi_s(pi_t^*I)",
                "j": "canonical dual7-isogeny involution",
                "j_squared": "identity after scalar7I in the original level group",
                "original_minus3_descent_commutes_with_j": True,
                "determinant_numerator_and_denominator_both_transported": True,
                "Rig_P0_includes_actual_fibre_isomorphism": True,
                "endomorphism_self_adjointness_not_used_as_a_frame_identification": True},
            "original_cY": {"tau": "tau", "w0": "w0", "sigma": "e1-e73", "z": "z-2e73/tau",
                            "source_K_conjugation": "s->-s", "z_claimed_Q_fixed": False},
            "exact_original_correspondence_expression_certified": True,
            "coefficient_coordinates_expanded_over_Q": False,
            "ideal_norm_RR_or_principal_calibration_computed": False,
            "original_eta_active_support_computed": False,
            "height_or_period_computed": False})
        self.program_spec = file_spec(self.path(name))
        return self.program_spec

    def finish(self):
        files = [file_spec(p) for p in sorted(self.out.glob("R873-*.json.gz"))
                 if not p.name.startswith("R873-stage-manifest-")]
        digest = fingerprint(files)
        name = "R873-stage-manifest-"+digest[:20]
        inventory = self.cached(name)
        if inventory is None:
            self.store(name, {"files": files, "current_checkpoints": [],
                              "all_listed_stages_complete": True})
        else:
            assert inventory["files"] == files
        certificate = {
            "result": RESULT, "complete": True, "p": P, "configuration": self.tag,
            "source_audit": self.source_audit, "primitive_target_witness": self.primitive,
            "section_basis": self.accepted_basis_spec, "norm_target_index": self.target_index_spec,
            "exact_coordinate_expression": self.coordinate_spec, "correspondence_DAG": self.program_spec,
            "actual_auxiliary_prime": self.prime,
            "actual_new_complement_V2_indices": [r["original_V2_index"] for r in self.accepted_basis["selected_complement"]],
            "actual_nonzero_2058_minor": {
                "prime": self.prime, "determinant_mod_prime": self.accepted_basis["actual_2058_minor_determinant"],
                "rows": 2058, "columns": 2058},
            "exact_section_space": "H0(8H+4(P0+P1))", "exact_section_space_dimension": 2058,
            "old_V8_dimension_reused": 2050, "actual_new_basis_columns": 8,
            "qY_count": COUNT, "full_coordinate_rows": 2200,
            "new_M2_indices": list(M2_INDICES), "new_M2_interval": [FIRST, STOP],
            "actual_exact_norm_coefficients": 17, "P_degree": 8, "K_degree_bound": 7,
            "all17_exact_characteristic_zero_unit_solve_expressions_certified": True,
            "all2200_original_modular_coordinate_relations_verified": True,
            "actual_original_cyclic7_correspondence_source_target_expression_certified": True,
            "actual_new_E1_or_M2_prefixes_through195_recomputed": False,
            "old_V8_V2_W_Hecke_or_E6_clearing_recomputed": False,
            "ordinary_V8_membership_assumed": False,
            "expanded_characteristic_zero_coefficients_computed": False,
            "normalized_curve_integral_basis_computed": False,
            "actual_ideal_norm_or_Picard_support_computed": False,
            "actual_calibration_or_nonp_terms_computed": False,
            "actual_height_or_period_computed": False,
            "stage_manifest": file_spec(self.path(name)), "seconds": time.monotonic()-self.started}
        save(self.out/FINAL, certificate)
        return certificate

    def run(self):
        fp = self.out/FINAL
        if fp.exists():
            certificate = read(fp)
            assert certificate["complete"] is True and certificate["configuration"] == self.tag
            inventory = read(self.out/certificate["stage_manifest"]["file"])
            assert file_spec(self.out/certificate["stage_manifest"]["file"]) == certificate["stage_manifest"]
            for row in inventory["files"]:
                assert file_spec(self.out/row["file"]) == row
            return certificate
        self.norm_targets()
        self.choose_basis()
        self.coordinate_expression()
        self.function_program()
        return self.finish()


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    job, certificate, error, code = None, None, None, 0
    try:
        assert 0 < args.budget_minutes <= 300
        job = Job(args)
        certificate = job.run()
    except BudgetStop as exc:
        error, code = type(exc).__name__+": "+str(exc), 124
    except BaseException as exc:
        error, code = type(exc).__name__+": "+str(exc), 1
        traceback.print_exc()
    receipt = {
        "result": RESULT, "complete": code == 0 and certificate is not None,
        "source_sha256": sha(__file__), "configuration": None if job is None else job.tag,
        "process_exit_code": code, "error": error, "seconds": time.monotonic()-started,
        "certificate_sha256": sha(args.output/FINAL) if (args.output/FINAL).exists() else None,
        "all_completed_new_stages_preserved": True,
        "old_source_bytes_and_tags_preserved": True,
        "new_Hermite_Picard_norm_or_height_computed": False}
    save(args.output/"core-receipt.json", receipt)
    print("R873_CORE_RECEIPT="+json.dumps(receipt, sort_keys=True), flush=True)
    return code


if __name__ == "__main__":
    sys.exit(main())
