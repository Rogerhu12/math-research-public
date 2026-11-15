#!/usr/bin/env python3
"""R800: append only original M2 qY129..195, preserving all old prefixes."""
import argparse
from collections import Counter
from functools import lru_cache
from pathlib import Path
import json
import os
import sys
import time

import flint
from flint import fmpz_poly

import R786_exact_power5_short_basis as original
import R795_exact_power6_short_basis as retained_io
from R795_exact_power6_short_basis import Retained, read, save, sha, file_spec

RESULT = "R800-original-M2-tail-129-195"
FINAL = "p41-original-M2-tail-129-195-certificate.json"
FIRST, LAST, DIMENSION = 129, 195, 146
P, LEVEL, ELL, XI = 41, 82, 739, 538
M2_NAME = "R775-basis-M2.json.gz"
M2_SHA = "51113988c90b301cb6117fec5c294b77110e1826bf00229b7993ba82144f5d3d"
COSETS_NAME = "R775-determinant-cosets.json.gz"
COSETS_SHA = "759d6f7643032fa358a0da02417d576f5d6f89a3996f9e6fb4b3bf954c52ecac"
R786_CORE = "4508095a95a2bcaec8c8db8fcd550fbc618b017d2bc0007945783bc109dbf851"
R795_CORE = "2a338672b32a9d760a78b234a0df08f05c10eb4ba513a2a3e3759f1e6e6b7aac"
PROOFS = {
    "R772_proof_sha256": "30006eca29d55c9b2e227f490e0ec9ffe128073f1c49c6dab25d3e532f4db59d",
    "R781_proof_sha256": "152c723da76b5c899b433db640fb6ac69082b46543f3d6bfa85d1cead7d78de0",
    "R793_proof_sha256": "6f716b64432227244a46d91f01ae2f46ba6d4a5f893666693ed07dec9e2e5cab"}


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematical execution belongs to public repository Actions.")


def e1_tail(a, b):
    """Only the new signed divisor contributions, never the old constant/prefix."""
    terms = {}
    for sign, residue, exponent in ((1, a, b), (-1, (-a) % LEVEL, (-b) % LEVEL)):
        start = residue if residue else LEVEL
        for m in range(start, LAST+1, LEVEL):
            for n in range(max(1, (FIRST+m-1)//m), LAST//m+1):
                phase_sign, r = original.phase(exponent*n)
                key = (m*n, r)
                terms[key] = terms.get(key, 0)+phase_sign*sign*LEVEL
    return original.canonical_sparse(terms)


def product_tail(left, right):
    answer = {}
    for n, r, v in left:
        for m, s, w in right:
            degree = n+m
            if degree > LAST:
                break
            if degree < FIRST:
                continue
            key = (degree, (r+s) % P)
            answer[key] = answer.get(key, 0)+v*w
    return original.canonical_sparse(answer)


class BudgetStop(RuntimeError):
    pass


class Job:
    def __init__(self, args):
        self.args, self.out = args, args.output
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        self.item = read(args.config)
        assert flint.__version__ == "0.9.0"
        assert self.item["result"] == RESULT and self.item["p"] == P
        assert self.item["producer_inputs_pending"] is False
        assert self.item["first_exponent"] == FIRST and self.item["last_exponent_exclusive"] == LAST+1
        assert self.item["core_sha256"] == sha(__file__)
        assert sha(args.method) == self.item["R800_method_sha256"]
        assert sha(original.__file__) == self.item["R786_core_helper_sha256"] == R786_CORE
        assert sha(retained_io.__file__) == self.item["R795_io_helper_sha256"] == R795_CORE
        for key, path in (("R772_proof_sha256", args.descent_proof),
                          ("R781_proof_sha256", args.tangent_proof),
                          ("R793_proof_sha256", args.rr_proof)):
            assert sha(path) == self.item[key] == PROOFS[key]
        assert set(self.item["retained_artifacts"]) == {"R771", "R775", "R786"}
        self.sources = {label: Retained(args.retained, label, spec)
                        for label, spec in self.item["retained_artifacts"].items()}
        self.r771, self.r775, self.r786 = (self.sources[label] for label in ("R771", "R775", "R786"))
        self.source_stages = {}
        for label in ("R771", "R775"):
            self.source_stages[label] = {row["file"]: row for row in self.sources[label].certificate["stages"]}
        spec = self.r786.certificate["stages_manifest"]
        self.source_stages["R786"] = {row["file"]: row for row in self.r786.get_spec(spec)["files"]}
        self.basis = self.get("R775", M2_NAME)
        assert self.r775.files[M2_NAME]["sha256"] == M2_SHA
        assert self.r775.files[COSETS_NAME]["sha256"] == COSETS_SHA
        assert self.basis["rank"] == DIMENSION and len(self.basis["basis"]) == DIMENSION
        assert self.basis["coefficient_bound"] >= LAST
        assert self.basis["characteristic_zero_independence_certified_by_unit_reduction"] is True
        assert self.r775.certificate["all_recipes_defined_over_original_K"] is True
        assert self.r775.tag["xi41_mod_ell"] == self.r771.tag["xi41_mod_ell"] == XI
        assert self.r775.tag["prime"] == self.r771.tag["prime"] == ELL
        assert self.r775.tag["R771_manifest_sha256"] == self.r786.tag["R771_manifest_sha256"] == \
            self.item["retained_artifacts"]["R771"]["manifest_sha256"]
        assert self.r775.tag["R771_certificate_sha256"] == self.r786.tag["R771_certificate_sha256"] == \
            self.r771.files[self.r771.spec["certificate_name"]]["sha256"]
        old_prefix = self.r786.tag["R775_completed_prefix_producer"]
        assert old_prefix["files"][M2_NAME] == M2_SHA
        assert old_prefix["files"][COSETS_NAME] == COSETS_SHA
        self.group = self.get("R771", "R771-original-level82-Eisenstein-label-group.json.gz")
        self.cosets = self.get("R775", COSETS_NAME)["cosets"]
        assert len(self.group["H82_mod_center"]) == 126 and len(self.cosets) == 40
        self.seed_ids = sorted({row["recipe"]["R771_seed_index"] for row in self.basis["basis"]})
        assert self.seed_ids == [0, 1, 2, 3, 11]
        self.tag = {"result": RESULT, "p": P, "source_sha256": sha(__file__),
            "python_flint": flint.__version__, "R800_method_sha256": sha(args.method),
            **PROOFS, "R786_core_helper_sha256": R786_CORE, "R795_io_helper_sha256": R795_CORE,
            "retained_artifacts": self.item["retained_artifacts"],
            "first_exponent": FIRST, "last_exponent_exclusive": LAST+1,
            "original_M2_recipe_sha256": M2_SHA, "original_determinant_cosets_sha256": COSETS_SHA,
            "M2_dimension": DIMENSION, "integer_scale": "6724", "E1_integer_scale": 82,
            "original_qY": "qY=exp(2*pi*i*tau/82); original reference cusp coset0",
            "original_phase": "xi82=-xi41^21; original odd determinant lift",
            "real_tangent_parameter": "v=xi41^-10*qY; t=xi41+xi41^-1",
            "old_prefix_through_128_recomputed": False,
            "ordinary_higher_powers_or_Laurent_recomputed": False}
        self.eis_rows = {}
        self.xipowers = [pow(XI, r, ELL) for r in range(P)]
        T = fmpz_poly([0, 1])
        self.chebyshev = [fmpz_poly([2]), T]
        for _ in range(2, 21):
            self.chebyshev.append(T*self.chebyshev[-1]-self.chebyshev[-2])
        self.real_modulus = fmpz_poly([1])
        for value in self.chebyshev[1:]:
            self.real_modulus += value
        assert self.real_modulus.degree() == 20 and self.real_modulus[20] == 1

    def get(self, label, name):
        source = self.sources[label]
        entry = self.source_stages[label][name]
        assert source.files[name]["sha256"] == entry["sha256"]
        assert source.files[name]["bytes"] == entry["bytes"]
        return source.get(name, entry["sha256"])

    def old_spec(self, label, name):
        row = self.sources[label].files[name]
        return {"file": name, "bytes": row["bytes"], "sha256": row["sha256"]}

    def budget(self):
        if time.monotonic()-self.started >= self.args.budget_minutes*60-45:
            raise BudgetStop("Complete original tail stages preserved for exact continuation.")

    def path(self, name):
        assert name.startswith("R800-") and Path(name).name == name
        return self.out/(name+".json.gz")

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def store(self, name, payload):
        path = self.path(name)
        assert not path.exists(), "A completed tail stage is immutable: "+path.name
        save(path, dict(payload, complete=True, configuration=self.tag))
        print(json.dumps({"stage": path.name, "complete": True, "sha256": sha(path),
                          "seconds": time.monotonic()-self.started}), flush=True)
        self.budget()
        return read(path)

    def eisenstein_row(self, a):
        if a in self.eis_rows:
            return self.eis_rows[a]
        old_name = "R786-exact-integral-E1-row-"+str(a).zfill(2)+".json.gz"
        old = self.get("R786", old_name)
        assert old["first_label_coordinate"] == a and old["bound_qY"] == FIRST-1
        assert old["scale"] == LEVEL and old["original_R771_finite_coefficients_verified"] is True
        prefix = old["sparse_series_by_second_coordinate"]
        assert len(prefix) == LEVEL
        name = "R800-original-E1-tail-row-"+str(a).zfill(2)
        stage = self.cached(name)
        if stage is None:
            self.budget()
            finite_name = "R771-Eisenstein-row-"+str(a).zfill(2)+".json.gz"
            finite = self.get("R771", finite_name)
            assert finite["first_label_coordinate"] == a and finite["last_exponent"] >= LAST
            tails = [e1_tail(a, b) for b in range(LEVEL)]
            for b, terms in enumerate(tails):
                values = [0]*(LAST-FIRST+1)
                for n, r, coefficient in terms:
                    assert FIRST <= n <= LAST and 0 <= r < P
                    values[n-FIRST] += coefficient*self.xipowers[r]
                reference = finite["series_by_second_coordinate"][b]
                for offset, actual in enumerate(values):
                    n = FIRST+offset
                    expected = LEVEL*(int(reference[n]) if n < len(reference) else 0) % ELL
                    assert actual % ELL == expected, (a, b, n)
            stage = self.store(name, {"first_label_coordinate": a,
                "first_exponent": FIRST, "last_exponent_exclusive": LAST+1, "integer_scale": LEVEL,
                "sparse_new_terms_by_second_coordinate": tails,
                "original_R786_prefix": self.old_spec("R786", old_name),
                "original_R771_finite_comparison": self.old_spec("R771", finite_name),
                "all_new_mod739_coefficients_verified": True,
                "old_constant_or_coefficients_through_128_recomputed": False})
        assert stage["first_label_coordinate"] == a
        assert stage["original_R786_prefix"] == self.old_spec("R786", old_name)
        rows = []
        for old_terms, new_terms in zip(prefix, stage["sparse_new_terms_by_second_coordinate"]):
            before = [tuple(int(x) for x in term) for term in old_terms]
            after = [tuple(int(x) for x in term) for term in new_terms]
            assert all(0 <= n < FIRST and 0 <= r < P for n, r, v in before)
            assert all(FIRST <= n <= LAST and 0 <= r < P for n, r, v in after)
            assert before == sorted(before) and after == sorted(after)
            rows.append(before+after)
        assert len(rows) == LEVEL
        self.eis_rows[a] = rows
        return rows

    @lru_cache(maxsize=2048)
    def pair(self, first, second):
        self.budget()
        return product_tail(self.eisenstein_row(first[0])[first[1]],
                            self.eisenstein_row(second[0])[second[1]])

    def seed_tail(self, r, position):
        name = "R800-original-seed-tail-"+str(r).zfill(3)+"-coset-"+str(position).zfill(2)
        seed = self.r771.certificate["M2_exact_seeds"][r]
        stage = self.cached(name)
        if stage is not None:
            assert stage["seed_index"] == r and stage["coset_position"] == position
            assert stage["original_seed"] == seed
            return stage["cyclic_new_terms"]
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
            for n, s, coefficient in self.pair(first, second):
                key = (n, s)
                total[key] = total.get(key, 0)+multiplicity*coefficient
        terms = original.canonical_sparse(total)
        stage = self.store(name, {"seed_index": r, "coset_position": position, "original_seed": seed,
            "determinant_mod82": self.cosets[position]["det_mod82"],
            "first_exponent": FIRST, "last_exponent_exclusive": LAST+1, "integer_scale": 6724,
            "cyclic_new_terms": terms, "trace_terms_with_multiplicity": 126,
            "old_seed_prefix_recomputed": False})
        return stage["cyclic_new_terms"]

    def real_row(self, row, n):
        cyclic = [0]*P
        for r, value in enumerate(row):
            cyclic[(r+10*n) % P] += value
        reduced = [value-cyclic[40] for value in cyclic[:40]]+[0]
        assert all(reduced[r] == reduced[P-r] for r in range(1, 21)), n
        polynomial = fmpz_poly([reduced[0]])
        for r in range(1, 21):
            polynomial += self.chebyshev[r]*reduced[r]
        polynomial %= self.real_modulus
        return [str(polynomial[r]) for r in range(20)]

    def m2_tail(self, index):
        name = "R800-original-M2-tail-row-"+str(index).zfill(4)
        old_name = "R786-exact-power-1-row-"+str(index).zfill(4)+".json.gz"
        old = self.get("R786", old_name)
        original_basis = self.basis["basis"][index]
        recipe = original_basis["recipe"]
        assert old["recipe"] == recipe and old["weight"] == 2
        assert old["integer_scale"] == "6724" and old["bound_qY"] == FIRST-1
        assert len(old["integer_qY_xi_coefficients"]) == FIRST
        assert all(len(row) == 40 for row in old["integer_qY_xi_coefficients"])
        stage = self.cached(name)
        if stage is None:
            self.budget()
            r, j = recipe["R771_seed_index"], recipe["j"]
            seed = self.r771.certificate["M2_exact_seeds"][r]
            assert recipe["lambda"] == seed["lambda"] and recipe["mu"] == seed["mu"]
            blocks = [[0]*P for _ in range(LAST-FIRST+1)]
            for position, coset in enumerate(self.cosets):
                sign, shift = original.phase(j*coset["det_mod82"])
                for n, s, coefficient in self.seed_tail(r, position):
                    assert FIRST <= n <= LAST
                    blocks[n-FIRST][(s+shift) % P] += sign*coefficient
            rows = [[block[r]-block[40] for r in range(40)] for block in blocks]
            reference = original_basis["coefficients_mod_ell"]
            for offset, row in enumerate(rows):
                n = FIRST+offset
                actual = sum(value*self.xipowers[r] for r, value in enumerate(row)) % ELL
                expected = 6724*(int(reference[n]) if n < len(reference) else 0) % ELL
                assert actual == expected, (index, n)
            real = [self.real_row(row, FIRST+offset) for offset, row in enumerate(rows)]
            stage = self.store(name, {"index": index, "recipe": recipe, "weight": 2,
                "integer_scale": "6724", "first_exponent": FIRST, "last_exponent_exclusive": LAST+1,
                "integer_qY_xi_coefficients": [[str(x) for x in row] for row in rows],
                "integer_v_t_coefficients": real,
                "original_R786_prefix": self.old_spec("R786", old_name),
                "original_R775_recipe_source_sha256": M2_SHA,
                "all_new_original_mod739_coefficients_verified": True,
                "all_new_real_tangent_involutions_verified": True,
                "old_prefix_recomputed": False, "old_prefix_bytes_modified": False})
        assert stage["index"] == index and stage["recipe"] == recipe
        assert stage["original_R786_prefix"] == self.old_spec("R786", old_name)
        return file_spec(self.path(name))

    def run(self):
        rows = [self.m2_tail(index) for index in range(DIMENSION)]
        index_name = "R800-original-M2-tail-index"
        index = self.cached(index_name)
        if index is None:
            index = self.store(index_name, {"dimension": DIMENSION, "first_exponent": FIRST,
                "last_exponent_exclusive": LAST+1, "integer_scale": "6724",
                "tail_rows_in_original_order": rows, "old_prefix_bound_qY": FIRST-1,
                "no_old_q_coefficients_recomputed": True})
        else:
            assert index["tail_rows_in_original_order"] == rows
        files = [file_spec(path) for path in sorted(self.out.glob("R800-*.json.gz"))
                 if path.name != "R800-stage-manifest.json.gz"]
        seed_count = len([row for row in files if row["file"].startswith("R800-original-seed-tail-")])
        assert seed_count == 40*len(self.seed_ids)
        inventory = self.path("R800-stage-manifest")
        save(inventory, {"result": RESULT, "complete": True, "configuration": self.tag, "files": files})
        certificate = {"result": RESULT, "complete": True, "p": P, "configuration": self.tag,
            "original_M2_dimension": DIMENSION, "first_exponent": FIRST,
            "last_exponent_exclusive": LAST+1, "new_coefficient_count_per_row": LAST-FIRST+1,
            "original_M2_integer_scale": "6724", "xi_coordinate_count": 40, "real_t_coordinate_count": 20,
            "actual_seed_indices": self.seed_ids, "actual_seed_coset_tail_count": seed_count,
            "actual_E1_tail_row_count": len([row for row in files if row["file"].startswith("R800-original-E1-tail-row-")]),
            "all_original_recipes_and_old_prefix_identities_preserved": True,
            "all_new_original_mod739_coefficients_verified": True,
            "all_new_real_tangent_involutions_verified": True,
            "old_E1_M2_seed_or_other_prefixes_recomputed": False,
            "ordinary_power2_to8_Laurent_rational_maps_eta_or_heights_computed": False,
            "basis_tail_index": file_spec(self.path(index_name)), "stage_manifest": file_spec(inventory),
            "seconds": time.monotonic()-self.started}
        save(self.out/FINAL, certificate)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(self.out/FINAL),
            "original_M2_dimension": DIMENSION, "new_exponents_inclusive": [FIRST, LAST]})
        return 0


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "method", "descent-proof", "tangent-proof", "rr-proof", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=int, default=300)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        return Job(args).run()
    except BaseException as error:
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error),
            "completed_new_tail_stages_preserved": True})
        raise


if __name__ == "__main__":
    sys.exit(main())
