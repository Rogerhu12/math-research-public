#!/usr/bin/env python3
"""R777: exact short K-defined RR series and original Hodge-cube coordinates.

This is the first exact input stage of original function recovery. It does not
claim an A/B map or a number-field kernel. All new arithmetic is public Actions.
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

import flint
from flint import fmpz_poly, fmpq, fmpq_mat, nmod_mat

RESULT = "R777-exact-short-K-basis-and-Hodge-cube-coordinates"
FINAL = "p41-exact-short-K-basis-and-Hodge-cube-certificate.json"
P, LEVEL, ELL, XI, CYC, CYCLIC, PACK = 41, 82, 739, 538, 40, 41, 79
BOUND, H3_BOUND = 142, 41
ROWS, SCALE = BOUND+1, 82
PACK_LENGTH = PACK*ROWS
R774_CERT_SHA = "aea27ac34e9a82203f723af27265db3cbd8d75e615247e11e0591fb2ed249b59"
R774_MANIFEST_SHA = "4d97bb53b106fa53958a943f9ae9e5d00870f7cf774d4617a727b3fa857ac222"
R774_CORE_SHA = "b7e8bf0f7b629881d973afaec01a2b905c4100573d46920841a9d48489e597fa"
R771_CERT_SHA = "9eb870af949167895daa4e180c16848860f8fea1c9efe1b105ab3cd3a667009f"
R771_MANIFEST_SHA = "024ed12029720cc1c5d7ec0612aa484b04cdde8f763fceb852a0fdeabc2c3d74"
R772_PROOF_SHA = "30006eca29d55c9b2e227f490e0ec9ffe128073f1c49c6dab25d3e532f4db59d"


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    data = (json.dumps(obj, ensure_ascii=False, sort_keys=True,
                       separators=(",", ":"))+"\n").encode("utf-8")
    if path.suffix == ".gz":
        with open(temporary, "wb") as raw:
            with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, compresslevel=2) as out:
                out.write(data)
    else:
        temporary.write_bytes(data)
    temporary.replace(path)


def mm(a, b):
    x, y, z, t = a
    u, v, w, r = b
    return ((x*u+y*w) % LEVEL, (x*v+y*r) % LEVEL,
            (z*u+t*w) % LEVEL, (z*v+t*r) % LEVEL)


def action(label, matrix):
    x, y = label
    a, b, c, d = matrix
    return ((x*a+y*c) % LEVEL, (x*b+y*d) % LEVEL)


def phase(exponent):
    """xi82^exponent = (-1)^exponent * xi41^(21*exponent)."""
    exponent %= LEVEL
    return (-1 if exponent % 2 else 1), (21*exponent) % P


def canonical_sparse(terms):
    return [(n, r, int(v)) for (n, r), v in sorted(terms.items()) if v]


def e1_scaled(a, b):
    """Exact sparse 82*E_(a,b), in the cyclic 41-coordinate presentation."""
    if a == 0 and b == 0:
        return []
    terms = {}
    def add(n, exponent, value):
        sign, r = phase(exponent)
        key = (n, r)
        terms[key] = terms.get(key, 0)+sign*value
    if a:
        add(0, 0, 41-a)
    else:
        order = LEVEL//math.gcd(LEVEL, b)
        for k in range(order):
            add(0, b*k, -(LEVEL//order)*k)
        add(0, 0, -41)
    for sign, residue, exponent in ((1, a, b), (-1, (-a) % LEVEL, (-b) % LEVEL)):
        start = residue if residue else LEVEL
        for m in range(start, BOUND+1, LEVEL):
            for n in range(1, BOUND//m+1):
                add(m*n, exponent*n, sign*LEVEL)
    return canonical_sparse(terms)


def sparse_product(a, b):
    answer = {}
    for n, r, v in a:
        for m, s, w in b:
            if n+m > BOUND:
                break
            key = (n+m, (r+s) % P)
            answer[key] = answer.get(key, 0)+v*w
    return canonical_sparse(answer)


def sparse_to_poly(terms):
    blocks = [[0]*P for _ in range(ROWS)]
    for n, r, value in terms:
        blocks[n][r] += int(value)
    coefficients = [0]*PACK_LENGTH
    for n, block in enumerate(blocks):
        for r in range(CYC):
            coefficients[PACK*n+r] = block[r]-block[40]
    return fmpz_poly(coefficients)


def poly_rows(poly, last=BOUND):
    return [[int(poly[PACK*n+r]) for r in range(CYC)] for n in range(last+1)]


def encode_poly(poly):
    return [[str(x) for x in row] for row in poly_rows(poly)]


def decode_poly(rows):
    assert len(rows) == ROWS and all(len(row) == CYC for row in rows)
    values = [0]*PACK_LENGTH
    for n, row in enumerate(rows):
        for r, value in enumerate(row):
            values[PACK*n+r] = int(value)
    return fmpz_poly(values)


def multiply(a, b):
    """Every factor has xi-degree <=39; 79 prevents a qY block carry."""
    product = a.mul_low(b, PACK_LENGTH)
    answer = [0]*PACK_LENGTH
    for n in range(ROWS):
        block = [0]*P
        offset = PACK*n
        for r in range(2*CYC-1):
            block[r % P] += int(product[offset+r])
        for r in range(CYC):
            answer[offset+r] = block[r]-block[40]
    return fmpz_poly(answer)


def rational_pair(value):
    return [str(value.numerator), str(value.denominator)]


class BudgetStop(RuntimeError):
    pass


class Retained:
    def __init__(self, directory, manifest_sha, certificate_name, certificate_sha):
        self.directory = Path(directory)
        mp = self.directory/"full-outputs-manifest.json"
        cp = self.directory/certificate_name
        assert sha(mp) == manifest_sha and sha(cp) == certificate_sha
        self.manifest, self.certificate = read(mp), read(cp)
        assert self.certificate["complete"]
        self.tag = self.certificate["configuration"]
        self.rows = {row["file"]: row for row in self.manifest["files"]}

    @lru_cache(maxsize=8)
    def stage(self, name):
        assert Path(name).name == name
        item = self.rows[name]
        path = self.directory/name
        assert sha(path) == item["sha256"] and path.stat().st_size == item["bytes"]
        data = read(path)
        assert data["complete"] and data["configuration"] == self.tag
        return data


class Job:
    def __init__(self, args):
        assert flint.__version__ == "0.9.0"
        self.args, self.out = args, args.output
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        self.config = read(args.config)
        assert self.config["producer_inputs_pending"] is False
        assert sha(args.proof) == self.config["R778_proof_sha256"]
        assert sha(args.descent_proof) == R772_PROOF_SHA
        kspec = self.config["retained_artifacts"]["R775"]
        self.kbasis = Retained(args.retained/"R775", kspec["manifest_sha256"],
            "p41-original-K-defined-RR-basis-certificate.json",
            kspec["files"]["p41-original-K-defined-RR-basis-certificate.json"])
        self.old = Retained(args.retained/"R771", R771_MANIFEST_SHA,
            "p41-original-quotient-RR-basis-certificate.json", R771_CERT_SHA)
        self.cube = Retained(args.retained/"R774", R774_MANIFEST_SHA,
            "p41-original-Hodge-cube-certificate.json", R774_CERT_SHA)
        assert self.cube.tag["source_sha256"] == R774_CORE_SHA
        assert self.cube.certificate["actual_cusp_ramification_e"] == 1
        assert self.cube.certificate["selected_original_map_index"] == 4
        assert self.cube.certificate["selected_original_map_degree"] == "1206"
        assert self.kbasis.tag["source_sha256"] == kspec["core_sha256"]
        assert self.kbasis.tag["xi41_mod_ell"] == XI
        assert self.kbasis.tag["level"] == LEVEL and self.kbasis.tag["prime"] == ELL
        assert self.kbasis.certificate["all_recipes_defined_over_original_K"]
        assert self.kbasis.certificate["M2_dimension"] == 146
        assert self.kbasis.certificate["M6_dimension"] == 694
        assert self.kbasis.certificate["M12_dimension"] == 1514
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__),
            "python_flint": flint.__version__,
            "R778_proof_sha256": sha(args.proof), "R772_proof_sha256": R772_PROOF_SHA,
            "R774_certificate_sha256": R774_CERT_SHA,
            "R774_manifest_sha256": R774_MANIFEST_SHA,
            "R775_producer": kspec, "R771_certificate_sha256": R771_CERT_SHA,
            "R771_manifest_sha256": R771_MANIFEST_SHA,
            "qY_bound": BOUND, "M6_arithmetic_injection_bound": H3_BOUND,
            "p": P, "level": LEVEL, "coordinate_basis": "xi41^0 through xi41^39",
            "target_H3_coordinate_basis": "b^0..b^6,s*b^0..s*b^6",
            "reference_cusp": "original coset0, qY=Q^3=exp(2*pi*i*tau/82)",
            "original_c1": 4424, "new_c1_phase": False,
            "integral_basis_scale": "82^weight",
            "phase": "xi82=-xi41^21, original determinant odd lift",
        }
        self.group = self.old.stage("R771-original-level82-Eisenstein-label-group.json.gz")
        self.cosets = self.kbasis.stage("R775-determinant-cosets.json.gz")["cosets"]
        assert len(self.group["H82_mod_center"]) == 126 and len(self.cosets) == 40
        self.xipowers = [pow(XI, r, ELL) for r in range(P)]
        self.eis_rows = {}
        self.poly_cache = {}
        self.basic = {}

    def budget(self):
        if time.monotonic()-self.started > 60*self.args.budget_minutes:
            raise BudgetStop("Exact completed stages preserved; resume the same configuration")

    def path(self, name):
        return self.out/(name+".json.gz")

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["configuration"] == self.tag
        return value

    def store(self, name, value):
        save(self.path(name), dict(value, configuration=self.tag))
        return dict(value, configuration=self.tag)

    def check_finite(self, poly, original, weight):
        factor = pow(82, weight, ELL)
        for n in range(ROWS):
            value = sum(int(poly[PACK*n+r])*self.xipowers[r] for r in range(CYC)) % ELL
            expected = factor*(int(original[n]) if n < len(original) else 0) % ELL
            assert value == expected, (weight, n, value, expected)

    def eisenstein_row(self, a):
        if a in self.eis_rows:
            return self.eis_rows[a]
        name = "R777-exact-integral-E1-row-"+str(a).zfill(2)
        prior = self.cached(name)
        if prior and prior["complete"]:
            result = [[(int(n), int(r), int(v)) for n, r, v in row]
                      for row in prior["sparse_series_by_second_coordinate"]]
        else:
            self.budget()
            oldrow = self.old.stage("R771-Eisenstein-row-"+str(a).zfill(2)+".json.gz")
            result = [e1_scaled(a, b) for b in range(LEVEL)]
            for b, terms in enumerate(result):
                values = [0]*ROWS
                for n, r, value in terms:
                    values[n] += value*self.xipowers[r]
                reference = oldrow["series_by_second_coordinate"][b]
                for n in range(ROWS):
                    expected = 82*(int(reference[n]) if n < len(reference) else 0) % ELL
                    assert values[n] % ELL == expected, (a, b, n)
            self.store(name, {"complete": True, "first_label_coordinate": a,
                "bound_qY": BOUND, "scale": 82,
                "sparse_series_by_second_coordinate": result,
                "original_R771_finite_coefficients_verified": True})
        self.eis_rows[a] = result
        return result

    def eisenstein(self, label):
        a, b = label
        return self.eisenstein_row(a)[b]

    @lru_cache(maxsize=2048)
    def pair(self, first, second):
        return sparse_product(self.eisenstein(first), self.eisenstein(second))

    def coset_image(self, r, position, seed):
        name = "R777-integral-seed-"+str(r).zfill(3)+"-coset-"+str(position).zfill(2)
        prior = self.cached(name)
        if prior and prior["complete"]:
            assert prior["original_seed"] == seed
            return [(int(n), int(s), int(v)) for n, s, v in prior["cyclic_terms"]]
        self.budget()
        matrix = tuple(self.cosets[position]["matrix"])
        pairs = Counter()
        for h in self.group["H82_mod_center"]:
            hg = mm(tuple(h), matrix)
            pair = tuple(sorted((action(seed["lambda"], hg), action(seed["mu"], hg))))
            pairs[pair] += 1
        total = {}
        for (first, second), multiplicity in pairs.items():
            for n, s, v in self.pair(first, second):
                key = (n, s)
                total[key] = total.get(key, 0)+multiplicity*v
        terms = canonical_sparse(total)
        self.store(name, {"complete": True, "original_seed": seed,
            "seed_index": r, "coset_position": position,
            "determinant_mod82": self.cosets[position]["det_mod82"],
            "scale": 82**2, "cyclic_terms": terms,
            "trace_terms_with_multiplicity": sum(pairs.values())})
        return terms

    def original_basis(self, kind, index):
        filename = "R775-basis-"+kind+".json.gz"
        stage = self.kbasis.stage(filename)
        return stage["basis"][index]

    def get_m2(self, index):
        key = ("power", 1, index)
        if key in self.poly_cache:
            return self.poly_cache[key]
        name = "R777-exact-power-1-row-"+str(index).zfill(4)
        prior = self.cached(name)
        original = self.original_basis("M2", index)
        recipe = original["recipe"]
        if prior and prior["complete"]:
            assert prior["recipe"] == recipe
            ans = decode_poly(prior["integer_qY_xi_coefficients"])
        else:
            self.budget()
            r, j = recipe["R771_seed_index"], recipe["j"]
            seed = self.old.certificate["M2_exact_seeds"][r]
            assert recipe["lambda"] == seed["lambda"] and recipe["mu"] == seed["mu"]
            total = {}
            for position, spec in enumerate(self.cosets):
                sign, shift = phase(j*spec["det_mod82"])
                for n, s, value in self.coset_image(r, position, seed):
                    location = (n, (s+shift) % P)
                    total[location] = total.get(location, 0)+sign*value
            ans = sparse_to_poly(canonical_sparse(total))
            self.check_finite(ans, original["coefficients_mod_ell"], 2)
            self.store(name, {"complete": True, "recipe": recipe, "weight": 2,
                "integer_scale": str(82**2), "bound_qY": BOUND,
                "integer_qY_xi_coefficients": encode_poly(ans),
                "original_R775_finite_coefficients_verified": True})
        self.poly_cache[key] = ans
        return ans

    def get_power(self, power, index):
        if power == 1:
            return self.get_m2(index)
        key = ("power", power, index)
        if key in self.poly_cache:
            return self.poly_cache[key]
        name = "R777-exact-power-"+str(power)+"-row-"+str(index).zfill(4)
        prior = self.cached(name)
        original = self.original_basis("power-"+str(power), index)
        recipe = original["recipe"]
        if prior and prior["complete"]:
            assert prior["recipe"] == recipe
            ans = decode_poly(prior["integer_qY_xi_coefficients"])
        else:
            self.budget()
            assert recipe["kind"] == "product"
            left = self.get_power(recipe["left_power"], recipe["left_index"])
            right = self.get_power(recipe["right_power"], recipe["right_index"])
            assert recipe["left_power"]+recipe["right_power"] == power
            ans = multiply(left, right)
            self.check_finite(ans, original["coefficients_mod_ell"], 2*power)
            self.store(name, {"complete": True, "recipe": recipe, "weight": 2*power,
                "integer_scale": str(82**(2*power)), "bound_qY": BOUND,
                "integer_qY_xi_coefficients": encode_poly(ans),
                "original_R775_finite_coefficients_verified": True})
        self.poly_cache[key] = ans
        return ans

    def level_one(self, name):
        if name in self.basic:
            return self.basic[name]
        # These are the exact integral level-one series through qY^142.
        if name == "E4":
            terms = [(0, 0, 1), (82, 0, 240)]
        elif name == "E6":
            terms = [(0, 0, 1), (82, 0, -504)]
        elif name == "eta12":
            terms = [(41, 0, 1), (123, 0, -12)]
        elif name == "E4E6":
            return multiply(self.level_one("E4"), self.level_one("E6"))
        else:
            raise ValueError("Unrecognized original level-one recipe")
        ans = sparse_to_poly(terms)
        oldrow = self.old.stage("R771-original-E4-E6-eta12-and-RR-denominators.json.gz")
        for n in range(ROWS):
            expected = int(oldrow[name][n]) if n < len(oldrow[name]) else 0
            assert int(ans[PACK*n]) % ELL == expected % ELL
        self.basic[name] = ans
        return ans

    def get_modular(self, weight, index):
        key = ("modular", weight, index)
        if key in self.poly_cache:
            return self.poly_cache[key]
        name = "R777-exact-M"+str(weight)+"-row-"+str(index).zfill(4)
        prior = self.cached(name)
        original = self.original_basis("M"+str(weight)+"-complete", index)
        recipe = original["recipe"]
        if prior and prior["complete"]:
            assert prior["recipe"] == recipe
            ans = decode_poly(prior["integer_qY_xi_coefficients"])
        else:
            self.budget()
            kind = recipe["kind"]
            if kind == "power_basis":
                assert 2*recipe["power"] == weight
                ans = self.get_power(recipe["power"], recipe["index"])
            elif kind == "elliptic_layer_product":
                power = recipe["power"]
                ans = multiply(self.level_one(recipe["factor"]),
                               self.get_power(power, recipe["index"]))
                ans *= 82**(weight-2*power)
            elif kind == "level_one":
                ans = self.level_one(recipe["name"])*82**weight
            elif kind == "level_one_product":
                ans = multiply(self.level_one(recipe["first"]),
                               self.level_one(recipe["second"]))*82**weight
            else:
                raise ValueError("Unrecognized actual R775 basis recipe")
            self.check_finite(ans, original["coefficients_mod_ell"], weight)
            self.store(name, {"complete": True, "recipe": recipe, "weight": weight,
                "integer_scale": str(82**weight), "bound_qY": BOUND,
                "integer_qY_xi_coefficients": encode_poly(ans),
                "original_R775_finite_coefficients_verified": True})
        self.poly_cache[key] = ans
        return ans

    def h3_rhs(self):
        scalars = self.cube.stage("R774-original-L-cubic-scalars.json.gz")
        scales = [fmpq(int(a), int(b)) for a, b in scalars["rational_row_scales"]]
        assert len(scales) == 14
        rhs = [[0]*14 for _ in range((H3_BOUND+1)*CYC)]
        for spec in self.cube.certificate["H3_blocks"]:
            first = int(spec["file"].split("-qY-")[1].split("-")[0])
            if first > H3_BOUND:
                continue
            data = self.cube.stage(spec["file"])
            assert data["rational_row_scale_stage_sha256"] == \
                self.cube.rows["R774-original-L-cubic-scalars.json.gz"]["sha256"]
            lo, hi = data["first_exponent"], data["last_exponent_exclusive"]
            for n in range(lo, min(hi, H3_BOUND+1)):
                for r in range(CYC):
                    for k in range(14):
                        rhs[CYC*n+r][k] = int(data["integer_numerators"][k][CYC*(n-lo)+r])
        return scales, rhs

    def h3_coordinates(self, basis):
        name = "R777-exact-original-H3-coordinates-in-K-basis"
        prior = self.cached(name)
        if prior and prior["complete"]:
            return prior
        self.budget()
        column_count, row_count = 694, CYC*(H3_BOUND+1)
        assert len(basis) == column_count
        columns = [[int(poly[PACK*n+r])
                    for n in range(H3_BOUND+1) for r in range(CYC)] for poly in basis]
        pivot_name = "R777-short-M6-rational-row-minor"
        minor = self.cached(pivot_name)
        if not (minor and minor["complete"]):
            modular = nmod_mat([[x % ELL for x in column] for column in columns], ELL)
            reduced, rank = modular.rref()
            assert rank == column_count, \
                "This actual auxiliary-prime short minor did not reach rank694"
            indices = [next(j for j in range(row_count) if reduced[i, j])
                       for i in range(rank)]
            square_mod = nmod_mat([[columns[j][i] % ELL for j in range(column_count)]
                                  for i in indices], ELL)
            determinant = int(square_mod.det())
            assert determinant
            minor = self.store(pivot_name, {"complete": True, "rank": rank,
                "prime": ELL, "determinant_mod_prime": determinant,
                "selected_original_coordinate_rows": indices,
                "row_labels": [[i//CYC, i % CYC] for i in indices],
                "full_rational_matrix_shape": [row_count, column_count]})
        indices = minor["selected_original_coordinate_rows"]
        A = fmpq_mat([[columns[j][i] for j in range(column_count)] for i in indices])
        scales, rhs = self.h3_rhs()
        B = fmpq_mat([rhs[i] for i in indices])
        self.budget()
        X = A.solve(B, algorithm="dixon")
        assert A*X == B
        # Membership of the ORIGINAL H^3 and R778 injectivity certify the
        # global equality from this exact original-coordinate solve.
        numerator, denominator = X.numer_denom()
        assert fmpq_mat(numerator) == X*denominator
        coordinates = [
            [rational_pair(X[j, k]*scales[k]*82**6) for k in range(14)]
            for j in range(column_count)]
        return self.store(name, {"complete": True,
            "basis": "actual R775 M6-complete, in its original saved order",
            "coordinate_basis_L": "b^0..b^6,s*b^0..s*b^6",
            "coordinates_in_unscaled_original_K_basis": coordinates,
            "primitive_rhs_solution_numerator": [
                [str(numerator[i, j]) for j in range(14)] for i in range(column_count)],
            "primitive_rhs_solution_denominator": str(denominator),
            "R774_rational_row_scales": [rational_pair(x) for x in scales],
            "scaled_basis_factor": str(82**6),
            "selected_row_minor": minor,
            "exact_rational_matrix_equation_verified": True,
            "original_H3_membership_from_R772": True,
            "global_equality_from_R778_arithmetic_injection": True,
            "original_H3_recomputed": False})

    def complete(self):
        final = self.out/FINAL
        if final.exists():
            cert = read(final)
            assert cert["complete"] and cert["configuration"] == self.tag
            inventory_spec = cert["stages_manifest"]
            assert sha(self.out/inventory_spec["file"]) == inventory_spec["sha256"]
            inventory = read(self.out/inventory_spec["file"])
            assert inventory["configuration"] == self.tag and inventory["complete"]
            for item in inventory["files"]:
                assert sha(self.out/item["file"]) == item["sha256"]
            return cert
        weight_six = [self.get_modular(6, j) for j in range(694)]
        h3 = self.h3_coordinates(weight_six)
        # The same exact source recipes, now through qY142, are the inputs
        # for all 143 original Laurent equations. No global kernel is assumed.
        for j in range(1514):
            self.get_modular(12, j)
        inventory_name = "R777-exact-stages-manifest"
        stages = [{"file": p.name, "bytes": p.stat().st_size, "sha256": sha(p)}
                  for p in sorted(self.out.glob("R777-*.json.gz"))
                  if p != self.path(inventory_name)]
        self.store(inventory_name, {"complete": True, "files": stages})
        inventory_path = self.path(inventory_name)
        inventory_spec = {"file": inventory_path.name, "bytes": inventory_path.stat().st_size,
                          "sha256": sha(inventory_path), "stage_count": len(stages)}
        cert = {
            "result": RESULT, "complete": True, "configuration": self.tag,
            "p": P, "actual_cusp_ramification_e": 1,
            "original_map_index": 4, "original_map_degree": "1206",
            "exact_K_basis_prefix_bound_qY": BOUND,
            "exact_M6_basis_dimension": 694, "exact_M12_basis_dimension": 1514,
            "all_series_scaled_by_82_to_their_weight": True,
            "all_original_R775_mod739_series_compared": True,
            "exact_H3_coordinates_in_original_K_basis_computed": True,
            "H3_actual_short_minor": h3["selected_row_minor"],
            "H3_exact_rational_solve_shape": [694, 694, 14],
            "H3_global_equality_from_known_membership_and_injection": True,
            "old_H3_topology_periods_lattice_or_basis_selection_recomputed": False,
            "actual_L_kernel_or_y_map_or_beta_or_height_computed": False,
            "next_function_recovery_uses_all_143_exact_Laurent_equations": True,
            "stages_manifest": inventory_spec, "seconds": time.monotonic()-self.started}
        save(final, cert)
        return cert


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New exact arithmetic belongs to public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--retained", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--proof", type=Path, required=True)
    parser.add_argument("--descent-proof", type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=80)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        job = Job(args)
        cert = job.complete()
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": True, "source_sha256": sha(__file__),
            "certificate_sha256": sha(args.output/FINAL),
            "exact_H3_coordinates": True, "exact_M12_prefix_qY": BOUND,
            "actual_y_map_claimed": False})
        print(json.dumps({"result": RESULT, "complete": True,
            "seconds": cert["seconds"]}), flush=True)
    except BaseException as error:
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "error": type(error).__name__+": "+str(error),
            "all_completed_exact_stages_preserved": True})
        raise


if __name__ == "__main__":
    main()
