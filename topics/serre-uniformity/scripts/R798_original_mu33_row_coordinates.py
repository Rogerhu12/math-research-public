#!/usr/bin/env python3
"""R798: exact short-row coordinates and on-demand original mu_33 products."""
import argparse
from fractions import Fraction
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
from flint import fmpz, fmpz_poly, nmod_mat

RESULT = "R798-original-mu33-row-coordinates"
FINAL = "p41-original-mu33-row-coordinate-certificate.json"
P, LEVEL, ROWS, CYC, REAL = 41, 82, 82, 40, 20
SOURCE_DIM, TARGET_DIM, FULL = 690, 1506, 1640
PACK_XI, PACK_T = 79, 39
R793_SHA = "6f716b64432227244a46d91f01ae2f46ba6d4a5f893666693ed07dec9e2e5cab"
R786_CERT_SHA = "dc6c23568f80b861d839280846c3250063abdfb2716a20481779816bb7cd37d9"
R795_CERT_SHA = "c5cffbd3979b5cd04e1e66c8c132de64974d81caf3b542e97a7a5ce479e3b0ae"


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


def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    raw = (json.dumps(data, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"))+"\n").encode("utf-8")
    if path.suffix == ".gz":
        with temporary.open("wb") as stream:
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb",
                               mtime=0, compresslevel=2) as compressed:
                compressed.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def packed(rows, stride):
    values = [0]*(stride*ROWS)
    assert len(rows) == ROWS
    for n, row in enumerate(rows):
        for r, value in enumerate(row):
            values[stride*n+r] = int(value)
    return fmpz_poly(values)


class Retained:
    def __init__(self, root, label, spec):
        self.directory, self.spec = Path(root)/label, spec
        mp = self.directory/"full-outputs-manifest.json"
        assert sha(mp) == spec["manifest_sha256"]
        manifest = read(mp)
        assert manifest["result"] == spec["result"]
        self.files = {row["file"]: row for row in manifest["files"]}
        run, core, initial = (self.raw(name) for name in
                             ("run-receipt.json", "core-receipt.json", "public-actions-input.json"))
        assert run["result"] == spec["result"] and run["complete"] is True
        assert run["process_exit_code"] == 0
        assert str(run["workflow_run_id"]) == str(spec["run_id"])
        assert run["source_commit"] == spec["source_commit"]
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        assert core["complete"] is True and core["source_sha256"] == spec["core_sha256"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["source_commit"] == spec["source_commit"]
        assert initial["core_sha256"] == spec["core_sha256"]
        name = spec["certificate_name"]
        assert core["certificate_sha256"] == spec["files"][name] == self.files[name]["sha256"]
        self.certificate = self.raw(name)
        assert self.certificate["complete"] is True and self.certificate["result"] == spec["result"]
        self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == spec["core_sha256"]
        assert self.tag["python_flint"] == "0.9.0"

    def raw(self, name, expected=None):
        assert Path(name).name == name
        entry = self.files[name]
        if expected is not None:
            assert entry["sha256"] == expected
        if name in self.spec["files"]:
            assert entry["sha256"] == self.spec["files"][name]
        path = self.directory/name
        assert path.stat().st_size == entry["bytes"] and sha(path) == entry["sha256"]
        return read(path)

    def get(self, name, expected=None):
        data = self.raw(name, expected)
        assert data["complete"] is True and data["configuration"] == self.tag
        return data

    def get_spec(self, entry):
        assert self.files[entry["file"]]["bytes"] == entry["bytes"]
        return self.get(entry["file"], entry["sha256"])


class BudgetStop(RuntimeError):
    pass


class Job:
    """The reusable interface keeps V3 in its old basis and V6 in selected-row coordinates."""

    def __init__(self, args):
        guard()
        self.args, self.out = args, args.output
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        self.config = read(args.config)
        assert flint.__version__ == "0.9.0"
        assert self.config["result"] == RESULT and self.config["p"] == P
        assert self.config["producer_inputs_pending"] is False
        assert self.config["core_sha256"] == sha(__file__)
        assert sha(args.proof) == self.config["R798_proof_sha256"]
        assert sha(args.method) == self.config["R798_method_sha256"]
        assert sha(args.rr_proof) == self.config["R793_proof_sha256"] == R793_SHA
        assert self.config["anchor_index"] == 0
        assert self.config["auxiliary_prime_start"] >= 2
        assert set(self.config["retained_artifacts"]) == {"R786", "R795"}
        self.r786, self.r795 = (Retained(args.retained, label, self.config["retained_artifacts"][label])
                                for label in ("R786", "R795"))
        c3, c6 = self.r786.certificate, self.r795.certificate
        assert self.r786.spec["files"][self.r786.spec["certificate_name"]] == R786_CERT_SHA
        assert self.r795.spec["files"][self.r795.spec["certificate_name"]] == R795_CERT_SHA
        assert c3["exact_K_basis_prefix_bound_qY"] == 128
        assert c3["basis_in_original_R775_saved_order"] is True
        assert c3["all_original_R775_mod739_short_series_compared"] is True
        assert c6["ordinary_power"] == 6 and c6["exact_power6_basis_dimension"] == TARGET_DIM
        assert c6["exact_K_basis_prefix_bound_qY"] == 81
        assert c6["basis_integer_scale"] == str(LEVEL**12)
        assert c6["all_original_real_cyclotomic_transports_verified"] is True
        assert c6["basis_in_original_R775_saved_order"] is True
        assert self.r795.tag["retained_artifacts"]["R786"]["manifest_sha256"] == \
               self.r786.spec["manifest_sha256"]
        manifest3 = self.r786.get_spec(c3["stages_manifest"])
        manifest6 = self.r795.get_spec(c6["stage_manifest"])
        self.entries3 = {row["file"]: row for row in manifest3["files"]}
        self.entries6 = {row["file"]: row for row in manifest6["files"]}
        self.basis6 = self.r795.get_spec(c6["basis_index"])
        assert self.basis6["dimension"] == TARGET_DIM
        assert self.basis6["ordinary_power"] == 6 and self.basis6["bound_qY"] == 81
        assert self.basis6["integer_scale"] == str(LEVEL**12)
        assert [row["index"] for row in self.basis6["basis_rows"]] == list(range(TARGET_DIM))
        assert self.r786.spec["stage_selection"] == {
            "ordinary_power": 3, "dimension": SOURCE_DIM, "anchor_witness_powers": [1, 2],
            "anchor_witness_index": 0}
        assert self.r795.spec["stage_selection"] == {"ordinary_power": 6, "dimension": TARGET_DIM}
        self.tag = {"result": RESULT, "source_sha256": sha(__file__),
            "python_flint": flint.__version__, "p": P,
            "R798_proof_sha256": sha(args.proof), "R798_method_sha256": sha(args.method),
            "R793_proof_sha256": sha(args.rr_proof),
            "retained_artifacts": self.config["retained_artifacts"],
            "source_dimension": SOURCE_DIM, "target_dimension": TARGET_DIM,
            "full_coordinate_count": FULL, "prefix_highest_exponent": 81,
            "source_integer_scale": str(LEVEL**6), "target_integer_scale": str(LEVEL**12),
            "v_parameter": "v=xi41^-10*qY", "t_parameter": "t=xi41+xi41^-1",
            "full_row_order": "20*n+r; 0<=n<=81; 0<=r<=19",
            "target_basis_order": "original R795/R775 ordinary power6 order",
            "target_coordinate_convention": "Psi_I(s)=C(s)_I; old coefficients c give A_I*c",
            "auxiliary_prime_start": self.config["auxiliary_prime_start"],
            "auxiliary_prime_policy": "increasing primes; actual short-matrix transpose RREF",
            "anchor_index": 0}
        T = fmpz_poly([0, 1])
        self.chebyshev = [fmpz_poly([2]), T]
        for _ in range(2, 21):
            self.chebyshev.append(T*self.chebyshev[-1]-self.chebyshev[-2])
        self.gt = fmpz_poly([1])
        for value in self.chebyshev[1:]:
            self.gt += value
        assert self.gt.degree() == REAL and self.gt[REAL] == 1
        self.selected = None

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes:
            raise BudgetStop("Completed row transports, prime stages and products retained.")

    def path(self, name):
        assert Path(name).name == name and name.startswith("R798-")
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

    def target_columns(self):
        columns = []
        for j, indexed in enumerate(self.basis6["basis_rows"]):
            name = "R795-exact-power-6-row-"+str(j).zfill(4)+".json.gz"
            entry = self.entries6[name]
            assert indexed["file"] == name
            assert indexed["sha256"] == entry["sha256"] and indexed["bytes"] == entry["bytes"]
            row = self.r795.get_spec(entry)
            assert row["index"] == j and row["weight"] == 12 and row["bound_qY"] == 81
            assert row["integer_scale"] == str(LEVEL**12)
            assert row["v_parameter"] == self.tag["v_parameter"]
            assert row["t_parameter"] == self.tag["t_parameter"]
            assert row["all_original_phase_involutions_verified"] is True
            assert row["averaging_used"] is False
            values = row["integer_v_t_coefficients"]
            assert len(values) == ROWS and all(len(v) == REAL for v in values)
            columns.append([int(value) for v in values for value in v])
            if j % 128 == 0:
                self.budget()
        return columns

    def select_rows(self):
        name = "R798-selected-short-rows"
        saved = self.cached(name)
        if saved is None:
            columns = self.target_columns()
            prime = self.config["auxiliary_prime_start"]
            attempts = []
            while True:
                while not fmpz(prime).is_prime():
                    prime += 1
                trial_name = "R798-target-prime-"+str(prime).zfill(10)
                trial = self.cached(trial_name)
                if trial is None:
                    self.budget()
                    print(json.dumps({"stage": "target_short_matrix_rref", "prime": prime,
                                      "transpose_shape": [TARGET_DIM, FULL]}), flush=True)
                    transposed = nmod_mat([[x % prime for x in col] for col in columns], prime)
                    reduced, rank = transposed.rref()
                    pivots = [next(j for j in range(FULL) if reduced[i, j]) for i in range(rank)]
                    assert pivots == sorted(set(pivots))
                    determinant = None
                    if rank == TARGET_DIM:
                        square = nmod_mat([[columns[j][i] % prime for j in range(TARGET_DIM)]
                                           for i in pivots], prime)
                        determinant = int(square.det())
                        assert determinant % prime != 0
                    self.store(trial_name, {"prime": prime, "actual_rank_mod_prime": rank,
                        "selected_row_indices": pivots, "actual_minor_determinant_mod_prime": determinant,
                        "matrix_shape": [FULL, TARGET_DIM],
                        "target_basis_index": self.r795.certificate["basis_index"],
                        "old_R775_long_minor_reused_as_short_minor": False})
                    trial = self.cached(trial_name)
                assert trial["prime"] == prime
                attempts.append(file_spec(self.path(trial_name)))
                if trial["actual_rank_mod_prime"] == TARGET_DIM:
                    I = trial["selected_row_indices"]
                    assert len(I) == TARGET_DIM and I == sorted(set(I))
                    J = [i for i in range(FULL) if i not in set(I)]
                    assert len(J) == FULL-TARGET_DIM
                    self.store(name, {"selected_row_indices": I, "complement_row_indices": J,
                        "prime": prime,
                        "actual_short_minor_determinant_mod_prime": trial["actual_minor_determinant_mod_prime"],
                        "actual_short_rank_mod_prime": TARGET_DIM, "actual_prime_stages": attempts,
                        "target_basis_index": self.r795.certificate["basis_index"],
                        "target_stage_manifest": self.r795.certificate["stage_manifest"],
                        "matrix_shape": [FULL, TARGET_DIM],
                        "original_basis_to_selected_coordinates": "A_I; columns from source R795 rows",
                        "inverse_over_Q_computed": False, "old_R775_long_minor_reused_as_short_minor": False})
                    break
                prime += 1
            saved = self.cached(name)
        assert saved["actual_short_rank_mod_prime"] == TARGET_DIM
        assert int(saved["actual_short_minor_determinant_mod_prime"]) % saved["prime"]
        I, J = saved["selected_row_indices"], saved["complement_row_indices"]
        assert len(I) == TARGET_DIM and len(J) == FULL-TARGET_DIM
        assert I == sorted(set(I)) and J == sorted(set(J))
        assert sorted(I+J) == list(range(FULL))
        self.selected = saved
        return file_spec(self.path(name))

    @lru_cache(maxsize=12)
    def original_row(self, power, index):
        assert power in (1, 2, 3)
        assert 0 <= index < ({1: 146, 2: 418, 3: SOURCE_DIM}[power])
        name = "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"
        entry = self.entries3[name]
        data = self.r786.get_spec(entry)
        assert data["weight"] == 2*power and data["bound_qY"] == 128
        assert data["integer_scale"] == str(LEVEL**(2*power))
        assert data["original_R775_finite_coefficients_verified"] is True
        values = data["integer_qY_xi_coefficients"]
        assert len(values) == 129 and all(len(v) == CYC for v in values)
        rows = [[int(x) for x in v] for v in values[:ROWS]]
        return {"rows": rows, "packed": packed(rows, PACK_XI),
                "source": entry, "recipe": data["recipe"]}

    def real_coordinates(self, rows):
        answer = []
        for n, values in enumerate(rows):
            cyclic = [0]*P
            for r, value in enumerate(values):
                cyclic[(r+10*n) % P] += int(value)
            reduced = [value-cyclic[40] for value in cyclic[:40]]+[0]
            assert all(reduced[r] == reduced[P-r] for r in range(1, 21)), \
                (n, "original real-phase involution")
            value = fmpz_poly([reduced[0]])
            for r in range(1, 21):
                value += self.chebyshev[r]*reduced[r]
            value %= self.gt
            answer.append([int(value[r]) for r in range(REAL)])
        return answer

    @lru_cache(maxsize=12)
    def real_prefix(self, index):
        name = "R798-V3-real-prefix-"+str(index).zfill(4)
        old = self.original_row(3, index)
        data = self.cached(name)
        if data is None:
            self.budget()
            rows = self.real_coordinates(old["rows"])
            self.store(name, {"index": index, "original_R786_row": old["source"],
                "original_recipe": old["recipe"], "weight": 6, "bound_v": 81,
                "integer_scale": str(LEVEL**6),
                "integer_v_t_coefficients": [[str(x) for x in row] for row in rows],
                "all_original_phase_involutions_verified": True, "averaging_used": False,
                "old_qY_coefficients_recomputed": False})
            data = self.cached(name)
        assert data["index"] == index and data["original_R786_row"] == old["source"]
        assert data["integer_scale"] == str(LEVEL**6)
        rows = [[int(x) for x in row] for row in data["integer_v_t_coefficients"]]
        assert len(rows) == ROWS and all(len(row) == REAL for row in rows)
        return {"rows": rows, "packed": packed(rows, PACK_T),
                "source": file_spec(self.path(name)), "old_source": old["source"]}

    def anchor(self):
        name = "R798-anchor-recipe"
        if self.cached(name) is None:
            rows = [self.original_row(power, 0) for power in (1, 2, 3)]
            assert rows[1]["recipe"] == {"kind": "product", "left_power": 1, "left_index": 0,
                                         "right_power": 1, "right_index": 0}
            assert rows[2]["recipe"] == {"kind": "product", "left_power": 1, "left_index": 0,
                                         "right_power": 2, "right_index": 0}
            self.store(name, {"original_rows": [row["source"] for row in rows],
                "original_recipes": [row["recipe"] for row in rows],
                "original_scales": [str(LEVEL**(2*r)) for r in (1, 2, 3)],
                "identity": "original scaled V3[0] = original scaled M2[0]^3",
                "identity_from_completed_original_recipes": True,
                "old_anchor_products_recomputed": False,
                "CM_nonvanishing_claimed": False})
        return file_spec(self.path(name))

    def _full_product(self, raw_left, real_left, raw_right, real_right):
        """Return all 1640 integers, with both original-coordinate convolutions verified."""
        qproduct = raw_left.mul_low(raw_right, PACK_XI*ROWS)
        qrows = []
        for n in range(ROWS):
            cyclic = [0]*P
            for r in range(2*CYC-1):
                cyclic[r % P] += int(qproduct[PACK_XI*n+r])
            qrows.append([cyclic[r]-cyclic[40] for r in range(CYC)])
        transported = self.real_coordinates(qrows)
        vproduct = real_left.mul_low(real_right, PACK_T*ROWS)
        direct = []
        for n in range(ROWS):
            value = fmpz_poly([vproduct[PACK_T*n+r] for r in range(2*REAL-1)]) % self.gt
            direct.append([int(value[r]) for r in range(REAL)])
        assert direct == transported, "full original qY/xi versus v/t product"
        return [value for row in direct for value in row]

    def _encode_verified_product(self, full, denominator=1):
        # Internal only: callers must supply the output of _full_product for
        # source-bound V3 factors, never an arbitrary ambient 1640-vector.
        assert len(full) == FULL and denominator > 0 and self.selected is not None
        return {"selected_coordinates": [str(full[i]) for i in self.selected["selected_row_indices"]],
                "complement_coordinates": [str(full[i]) for i in self.selected["complement_row_indices"]],
                "coordinate_denominator": str(denominator),
                "selected_rows": file_spec(self.path("R798-selected-short-rows")),
                "integer_scale": str(LEVEL**12),
                "all_1640_original_coordinate_products_verified": True,
                "V6_membership_witness": "product of two source-bound original V3 sections",
                "original_V6_basis_coordinates_computed": False}

    def product(self, left_index, right_index):
        """Compute or reuse one exact basis product, without a global multiplication table."""
        if self.selected is None:
            self.select_rows()
        assert 0 <= left_index < SOURCE_DIM and 0 <= right_index < SOURCE_DIM
        i, j = sorted((left_index, right_index))
        name = "R798-mu33-product-"+str(i).zfill(4)+"-"+str(j).zfill(4)
        saved = self.cached(name)
        if saved is None:
            self.budget()
            left, right = self.original_row(3, i), self.original_row(3, j)
            real_left, real_right = self.real_prefix(i), self.real_prefix(j)
            full = self._full_product(left["packed"], real_left["packed"],
                                     right["packed"], real_right["packed"])
            self.store(name, dict(self._encode_verified_product(full), source_indices=[i, j],
                original_R786_rows=[left["source"], right["source"]],
                transported_source_rows=[real_left["source"], real_right["source"]],
                product_recipe="original scaled V3[i] * original scaled V3[j]"))
        else:
            assert saved["source_indices"] == [i, j]
            assert saved["selected_rows"] == file_spec(self.path("R798-selected-short-rows"))
            assert saved["coordinate_denominator"] == "1"
            assert saved["all_1640_original_coordinate_products_verified"] is True
        return file_spec(self.path(name))

    @staticmethod
    def normalize_combination(terms):
        """terms are [source_index, numerator, denominator]; no floats are accepted."""
        coefficients = {}
        for index, numerator, denominator in terms:
            assert isinstance(index, int) and 0 <= index < SOURCE_DIM
            assert isinstance(numerator, (int, str)) and isinstance(denominator, (int, str))
            value = Fraction(int(numerator), int(denominator))
            coefficients[index] = coefficients.get(index, Fraction(0))+value
        return [[index, str(value.numerator), str(value.denominator)]
                for index, value in sorted(coefficients.items()) if value]

    def combination(self, terms):
        normalized = self.normalize_combination(terms)
        denominator = math.lcm(*(int(term[2]) for term in normalized)) if normalized else 1
        qtotal, vtotal = fmpz_poly([]), fmpz_poly([])
        sources = []
        for index, numerator, divisor in normalized:
            scalar = int(numerator)*(denominator//int(divisor))
            old, real = self.original_row(3, index), self.real_prefix(index)
            qtotal += scalar*old["packed"]
            vtotal += scalar*real["packed"]
            sources.append({"index": index, "original_row": old["source"],
                            "transported_row": real["source"]})
        return qtotal, vtotal, denominator, normalized, sources

    def rational_combination_product(self, left_terms, right_terms):
        """Reusable exact Q-bilinear interface; consumers extend K/L componentwise."""
        if self.selected is None:
            self.select_rows()
        left = self.normalize_combination(left_terms)
        right = self.normalize_combination(right_terms)
        key = hashlib.sha256(json.dumps([left, right], separators=(",", ":")).encode()).hexdigest()
        name = "R798-mu33-combination-"+key
        if self.cached(name) is None:
            self.budget()
            ql, vl, dl, nl, sl = self.combination(left)
            qr, vr, dr, nr, sr = self.combination(right)
            full = self._full_product(ql, vl, qr, vr)
            self.store(name, dict(self._encode_verified_product(full, dl*dr),
                original_rational_left_combination=nl, original_rational_right_combination=nr,
                original_left_sources=sl, original_right_sources=sr,
                product_recipe="two explicit rational combinations of original scaled V3 rows"))
        return file_spec(self.path(name))

    def run(self):
        selected = self.select_rows()
        anchor = self.anchor()
        products, prefixes = [], []
        for j in range(SOURCE_DIM):
            self.real_prefix(j)
            prefixes.append(dict(file_spec(self.path("R798-V3-real-prefix-"+str(j).zfill(4))), index=j))
            products.append(dict(self.product(0, j), source_indices=[0, j]))
            if j % 32 == 0 or j+1 == SOURCE_DIM:
                print(json.dumps({"stage": "exact_anchor_embedding", "completed": j+1,
                                  "total": SOURCE_DIM, "seconds": time.monotonic()-self.started}), flush=True)
        source_index = self.store("R798-V3-real-prefix-index", {"basis_rows": prefixes,
            "dimension": SOURCE_DIM, "highest_exponent": 81, "integer_scale": str(LEVEL**6),
            "source_stage_manifest": self.r786.certificate["stages_manifest"]})
        anchor_index = self.store("R798-anchor-embedding-index", {"products": products,
            "count": len(products), "anchor_source_index": 0, "anchor_recipe": anchor,
            "selected_rows": selected, "source_dimension": SOURCE_DIM,
            "injectivity_reason": "nonzero original tau^3 on the original integral curve",
            "actual_anchor_modular_rank_computed": False,
            "all_1640_original_coordinate_products_verified": True})
        stages = self.store("R798-stage-manifest", {"files": [file_spec(path)
            for path in sorted(self.out.glob("R798-*.json.gz"))
            if path.name != "R798-stage-manifest.json.gz"]})
        certificate = {"result": RESULT, "complete": True, "configuration": self.tag, "p": P,
            "source_dimension": SOURCE_DIM, "target_dimension": TARGET_DIM,
            "full_coordinate_count": FULL, "selected_coordinate_count": TARGET_DIM,
            "complement_coordinate_count": FULL-TARGET_DIM,
            "source_integer_scale": str(LEVEL**6), "target_integer_scale": str(LEVEL**12),
            "actual_short_minor_prime": self.selected["prime"],
            "actual_short_minor_determinant_mod_prime": self.selected["actual_short_minor_determinant_mod_prime"],
            "actual_short_matrix_rank_mod_prime": self.selected["actual_short_rank_mod_prime"],
            "completed_anchor_products": len(products), "anchor_is_original_tau_cubed": True,
            "all_anchor_products_full_1640_verified": True,
            "original_basis_inverse_over_Q_computed": False,
            "original_V6_basis_coordinates_computed": False, "full_690_squared_table_generated": False,
            "old_qY_coefficients_period_Hom_or_Laurent_recomputed": False,
            "actual_polar_divisors_eta_beta_or_heights_computed": False,
            "selected_rows": selected, "anchor_recipe": anchor, "source_real_basis_index": source_index,
            "anchor_embedding_index": anchor_index, "stage_manifest": stages,
            "seconds": time.monotonic()-self.started}
        final = self.out/FINAL
        save(final, certificate)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(final),
            "actual_short_matrix_rank_mod_prime": self.selected["actual_short_rank_mod_prime"],
            "completed_anchor_products": len(products),
            "actual_polar_divisors_eta_beta_or_heights_computed": False})
        return 0


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "retained", "output", "proof", "method", "rr-proof"):
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

