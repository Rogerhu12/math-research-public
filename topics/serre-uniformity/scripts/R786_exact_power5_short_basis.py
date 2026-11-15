#!/usr/bin/env python3
"""R786: exact original power5 K basis through qY128.

Consume only the completed R775 power1..5 stages, even if its full run timed out.
All new mathematics runs in public repository Actions. No actual y is claimed.
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
from flint import fmpz_poly

RESULT = "R786-exact-original-power5-short-basis"
FINAL = "p41-exact-original-power5-short-basis-certificate.json"
P, LEVEL, ELL, XI, CYC, CYCLIC, PACK = 41, 82, 739, 538, 40, 41, 79
BOUND, POWER, DIMENSION = 128, 5, 1234
ROWS, SCALE = BOUND+1, 82
PACK_LENGTH = PACK*ROWS



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


class CompletePrefix:
    """Only completed, individually bound stages of a budget-limited producer."""
    def __init__(self, directory, spec):
        self.directory, self.spec = Path(directory), spec
        mp = self.directory/"full-outputs-manifest.json"
        assert sha(mp) == spec["manifest_sha256"]
        self.manifest = read(mp)
        assert self.manifest["result"] == "R775-p41-original-K-defined-RR-bases"
        self.rows = {row["file"]: row for row in self.manifest["files"]}
        self.tag = None
        anchor = self.stage("R775-basis-M2.json.gz")
        self.tag = anchor["configuration"]
        assert self.tag["source_sha256"] == spec["core_sha256"]
        assert self.tag["result"] == "R775-p41-original-K-defined-RR-bases"
        assert self.tag["R771_manifest_sha256"] == R771_MANIFEST_SHA
        assert self.tag["R771_certificate_sha256"] == R771_CERT_SHA

    @lru_cache(maxsize=8)
    def stage(self, name):
        assert Path(name).name == name
        item = self.rows[name]
        path = self.directory/name
        assert item["sha256"] == self.spec["files"][name]
        assert sha(path) == item["sha256"] and path.stat().st_size == item["bytes"]
        data = read(path)
        assert data["complete"] is True
        if self.tag is not None:
            assert data["configuration"] == self.tag
        return data


class Job:
    def __init__(self, args):
        assert flint.__version__ == "0.9.0"
        self.args, self.out = args, args.output
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        self.config = read(args.config)
        assert self.config["producer_inputs_pending"] is False
        assert sha(args.proof) == self.config["R786_proof_sha256"]
        assert sha(args.descent_proof) == R772_PROOF_SHA
        kspec = self.config["retained_artifacts"]["R775"]
        self.kbasis = CompletePrefix(args.retained/"R775", kspec)
        self.old = Retained(args.retained/"R771", R771_MANIFEST_SHA,
            "p41-original-quotient-RR-basis-certificate.json", R771_CERT_SHA)
        assert self.kbasis.tag["xi41_mod_ell"] == XI
        assert self.kbasis.tag["level"] == LEVEL and self.kbasis.tag["prime"] == ELL
        self.input_minors = {}
        for power, dimension in ((1, 146), (2, 418), (3, 690), (4, 962), (5, DIMENSION)):
            name = "R775-basis-M2.json.gz" if power == 1 else \
                   "R775-basis-power-"+str(power)+".json.gz"
            stage = self.kbasis.stage(name)
            assert stage["configuration"] == self.kbasis.tag
            assert stage["rank"] == dimension and len(stage["basis"]) == dimension
            assert stage["coefficient_bound"] >= 272*power
            minor = stage["actual_nonzero_minor"]
            assert minor["prime"] == ELL and int(minor["determinant_mod_ell"]) % ELL
            assert minor["rows"] == dimension and minor["columns"] == dimension
            assert stage["characteristic_zero_independence_certified_by_unit_reduction"]
            self.input_minors[str(power)] = minor
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__),
            "python_flint": flint.__version__,
            "R786_proof_sha256": sha(args.proof), "R772_proof_sha256": R772_PROOF_SHA,
            "R775_completed_prefix_producer": kspec,
            "R775_full_run_success_required": False,
            "R775_full_M6_M12_certificate_consumed": False,
            "R771_certificate_sha256": R771_CERT_SHA,
            "R771_manifest_sha256": R771_MANIFEST_SHA,
            "qY_bound": BOUND, "ordinary_power": POWER,
            "ordinary_power_dimension": DIMENSION,
            "p": P, "level": LEVEL, "coordinate_basis": "xi41^0 through xi41^39",
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
        name = "R786-exact-integral-E1-row-"+str(a).zfill(2)
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
        name = "R786-integral-seed-"+str(r).zfill(3)+"-coset-"+str(position).zfill(2)
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
        assert sum(pairs.values()) == 126
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
        name = "R786-exact-power-1-row-"+str(index).zfill(4)
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
        assert 1 <= power <= POWER
        if power == 1:
            return self.get_m2(index)
        key = ("power", power, index)
        if key in self.poly_cache:
            return self.poly_cache[key]
        name = "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)
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
            assert 1 <= recipe["left_power"] < power
            assert 1 <= recipe["right_power"] < power
            assert recipe["left_power"]+recipe["right_power"] == power
            ans = multiply(left, right)
            self.check_finite(ans, original["coefficients_mod_ell"], 2*power)
            self.store(name, {"complete": True, "recipe": recipe, "weight": 2*power,
                "integer_scale": str(82**(2*power)), "bound_qY": BOUND,
                "integer_qY_xi_coefficients": encode_poly(ans),
                "original_R775_finite_coefficients_verified": True})
        if power < POWER:
            self.poly_cache[key] = ans
        return ans

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
                assert (self.out/item["file"]).stat().st_size == item["bytes"]
            return cert
        final_rows = []
        for index in range(DIMENSION):
            self.budget()
            poly = self.get_power(POWER, index)
            path = self.path("R786-exact-power-5-row-"+str(index).zfill(4))
            assert path.is_file()
            final_rows.append({"index": index, "file": path.name,
                               "bytes": path.stat().st_size, "sha256": sha(path)})
            del poly
            if index % 16 == 0 or index+1 == DIMENSION:
                print(json.dumps({"stage": "exact_power5", "complete_rows": index+1,
                    "total_rows": DIMENSION,
                    "seconds": time.monotonic()-self.started}), flush=True)
        index_name = "R786-exact-power5-basis-index"
        self.store(index_name, {"complete": True, "basis_rows": final_rows,
            "ordinary_line_bundle": "5*(K_Y+cusp_divisor), degree1360",
            "dimension": DIMENSION, "bound_qY": BOUND,
            "integer_scale": str(82**10),
            "actual_R775_minor": self.input_minors["5"],
            "basis_selection_recomputed": False})
        inventory_name = "R786-exact-stages-manifest"
        stages = [{"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}
                  for path in sorted(self.out.glob("R786-*.json.gz"))
                  if path != self.path(inventory_name)]
        self.store(inventory_name, {"complete": True, "files": stages})
        inventory_path = self.path(inventory_name)
        inventory_spec = {"file": inventory_path.name,
                          "bytes": inventory_path.stat().st_size,
                          "sha256": sha(inventory_path), "stage_count": len(stages)}
        index_path = self.path(index_name)
        cert = {
            "result": RESULT, "complete": True, "configuration": self.tag,
            "p": P, "original_map_index": 4, "original_map_degree": "1206",
            "source_quotient_genus": 127, "ordinary_line_bundle_degree": 1360,
            "exact_power5_basis_dimension": DIMENSION,
            "exact_K_basis_prefix_bound_qY": BOUND,
            "basis_in_original_R775_saved_order": True,
            "basis_integer_scale": str(82**10),
            "all_original_R775_mod739_short_series_compared": True,
            "actual_R775_power5_minor": self.input_minors["5"],
            "R775_completed_powers_reused": [1, 2, 3, 4, 5],
            "R775_incomplete_power6_not_used": True,
            "R775_full_final_certificate_not_used": True,
            "old_basis_selection_topology_periods_lattice_or_H3_recomputed": False,
            "actual_L_kernel_or_y_map_or_beta_or_height_computed": False,
            "next_Laurent_exponents_inclusive": [-1, 127],
            "next_relation_matrix_max_shape_over_L": [2580, 2468],
            "next_theoretical_kernel_dimension_lower_bound_only": 28,
            "next_actual_kernel_rank_claimed": False,
            "basis_index": {"file": index_path.name,
                            "bytes": index_path.stat().st_size,
                            "sha256": sha(index_path)},
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
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        job = Job(args)
        cert = job.complete()
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": True, "source_sha256": sha(__file__),
            "certificate_sha256": sha(args.output/FINAL),
            "exact_power5_dimension": DIMENSION, "exact_prefix_qY": BOUND,
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
