#!/usr/bin/env python3
"""R813: two original Wronskians in the completed S3 chart; no new primitive search."""
import argparse
from collections import OrderedDict
import gc
import gzip
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpq, fmpz, fmpz_mat, fmpz_poly, nmod_mat

RESULT = "R813-original-Wronskian-derivation-inputs"
FINAL = "p41-original-Wronskian-derivation-inputs-certificate.json"
P, LEVEL, CYC, REAL, COUNT = 41, 82, 40, 20, 41
DIM, ROWS, FREE = 690, 820, 272
EPS = [0]+[1]*144+[2]*127
LABELS = {"R805", "R786", "R806"}
R805_CORE_SHA = "730a7d8f51d76d1153386c63f2e082285ada4573a2baf8d87d1825d3ce75b420"
R806_CORE_SHA = "b014f9b3cb4923421e6a879eddb4da58dd0baefb28d61a2191f6b0a33e51810d"
R805_PROOF_SHA = "b48d9f8dd5d8d1a89aa2574ab7f9ee014b83ca21baf41694252b9c53993571e8"


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("All new exact arithmetic belongs to public repository Actions.")


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


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def same_producer(left, right):
    for key in ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256", "certificate_name"):
        assert str(left[key]) == str(right[key]), ("producer identity", key)
    certificate = left["certificate_name"]
    assert left["files"][certificate] == right["files"][certificate]
    for name in set(left["files"]) & set(right["files"]):
        assert left["files"][name] == right["files"][name]


def pairs(value):
    return [str(value.numer()), str(value.denom())]


def dq(value):
    assert len(value) == 2 and int(value[1]) > 0
    return fmpq(int(value[0]), int(value[1]))


def matrix_rows(matrix, strings=False):
    convert = str if strings else int
    return [[convert(matrix[i, j]) for j in range(matrix.ncols())] for i in range(matrix.nrows())]


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
        self.initial = initial
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

    def load_inventory(self):
        cert = self.certificate
        spec = cert.get("stage_manifest", cert.get("stages_manifest"))
        assert spec is not None and plain_spec(spec) == plain_spec(self.files[spec["file"]])
        inventory = self.stage(spec["file"], spec["sha256"])
        self.inventory = {row["file"]: plain_spec(row) for row in inventory["files"]}
        assert len(self.inventory) == len(inventory["files"])
        return inventory

    def indexed(self, spec):
        assert plain_spec(spec) == self.inventory[spec["file"]]
        assert plain_spec(spec) == plain_spec(self.files[spec["file"]])
        return self.stage(spec["file"], spec["sha256"])


class BudgetStop(RuntimeError):
    pass


def S_position(index):
    assert 0 <= index < DIM
    offset = 0
    for a, eps in enumerate(EPS):
        width = 4-eps
        if index < offset+width:
            return a, index-offset
        offset += width
    raise AssertionError("S3 index outside original graded free basis")


def producer_identity(spec):
    keys = ("result", "run_id", "source_commit", "core_sha256",
            "manifest_sha256", "certificate_name")
    answer = {key: spec[key] for key in keys}
    answer["certificate_sha256"] = spec["files"][spec["certificate_name"]]
    return answer


def primitive(values):
    denominator = 1
    for value in values:
        denominator = math.lcm(denominator, int(value.denom()))
    integers = [int(value.numer())*(denominator//int(value.denom())) for value in values]
    content = 0
    for value in integers:
        content = math.gcd(content, abs(value))
    if not content:
        return [0]*len(values), fmpq(0)
    return [value//content for value in integers], fmpq(content, denominator)


def integer_content(values):
    content = 0
    for value in values:
        content = math.gcd(content, abs(value))
    return content


def modular_rows(matrix, prime):
    return nmod_mat([[int(matrix[i, j]) % prime for j in range(matrix.ncols())]
                     for i in range(matrix.nrows())], prime)

class Job:
    def __init__(self, args):
        self.args, self.out, self.started = args, args.output, time.monotonic()
        self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        assert self.item["producer_inputs_pending"] is False
        assert self.item["result"] == RESULT and self.item["p"] == P
        assert self.item["core_sha256"] == sha(__file__)
        assert self.item["R813_proof_sha256"] == sha(args.proof)
        assert self.item["R813_method_sha256"] == sha(args.method)
        assert flint.__version__ == "0.9.0"
        assert self.item["qY_count"] == COUNT
        assert self.item["target_names"] == ["g", "h"]
        assert self.item["original_D0_qY_multiplier"] == ["1", "82"]
        assert self.item["reconstruct_every_digits"] == 8
        assert set(self.item["retained_artifacts"]) == LABELS
        self.inputs = {label: Retained(args.retained, label, self.item["retained_artifacts"][label])
                       for label in sorted(LABELS)}
        for producer in self.inputs.values():
            producer.load_inventory()
        self.r805, self.r786, self.r806 = (self.inputs[label] for label in ("R805", "R786", "R806"))
        assert self.r805.spec["core_sha256"] == R805_CORE_SHA
        assert self.r806.spec["core_sha256"] == R806_CORE_SHA
        assert self.r806.spec["result"] == "R806-original-primitive-multiplication"
        same_producer(self.r805.tag["retained_artifacts"]["R786"], self.r786.spec)
        for label in ("R805", "R786"):
            same_producer(self.r806.tag["retained_artifacts"][label], self.inputs[label].spec)
        assert self.r805.tag["R805_proof_sha256"] == R805_PROOF_SHA
        assert self.r806.tag["R805_proof_sha256"] == R805_PROOF_SHA
        cert805, cert806 = self.r805.certificate, self.r806.certificate
        assert cert805["completed_scope"] == "pencil_and_graded_free_basis"
        assert cert805["affine_free_module_rank"] == FREE
        assert cert805["all_S_rows_original_and_real_coordinates_verified"] is True
        assert cert806["completed_scope"] == "primitive_multiplication_and_cyclic_certificate"
        assert cert806["exact_polynomial_multiplication_computed"] is True
        assert cert806["all272_columns_verified_in_all820_original_rows"] is True
        assert cert806["original_function_field_primitive_generator_certified"] is True
        assert cert806["normal_integral_basis_preserved"] is True
        self.pencil = self.r805.indexed(cert805["pencil_stage"])
        self.free = self.r805.indexed(cert805["graded_free_basis_stage"])
        self.Sindex = self.r805.indexed(cert805["S_basis_index"])
        self.alias = self.r805.indexed(cert805["alias_index"])
        self.original_minor = self.r805.indexed(self.Sindex["short_minor"])
        assert self.pencil["actual_rank"] == 690
        assert self.pencil["basepoint_free_certified_by_actual_unit_minor"] is True
        self.n = int(self.pencil["n"])
        assert self.free["degree_distribution"] == [1, 144, 127]
        assert self.free["degree1_original_indices"] == list(range(2, 146))
        assert self.Sindex["dimension"] == DIM and self.Sindex["integer_scale"] == str(LEVEL**6)
        assert self.Sindex["all_original_and_real_coordinates_verified"] is True
        assert len(self.Sindex["basis_rows"]) == DIM
        self.chart = self.r806.indexed(cert806["coordinate_chart"])
        assert self.chart["original_R805_pencil"] == cert805["pencil_stage"]
        assert self.chart["original_R805_free_basis"] == cert805["graded_free_basis_stage"]
        assert self.chart["original_R805_S_basis_index"] == cert805["S_basis_index"]
        assert self.chart["original_R805_short_minor"] == self.Sindex["short_minor"]
        assert self.chart["all_original_S_basis_rows"] == self.Sindex["basis_rows"]
        assert self.chart["full_rows"] == ROWS and self.chart["columns"] == DIM
        assert self.chart["integer_scale"] == str(LEVEL**6)
        assert self.chart["normal_affine_basis_degrees"] == EPS
        self.I = self.chart["coordinate_row_indices"]
        assert self.I == self.original_minor["row_indices"]
        assert len(self.I) == DIM and self.I == sorted(set(self.I))
        assert all(0 <= index < ROWS for index in self.I)
        self.accepted = self.r806.indexed(cert806["accepted_candidate"])
        self.definition = self.r806.indexed(self.accepted["candidate_definition"])
        assert self.accepted["original_coordinate_chart"] == cert806["coordinate_chart"]
        assert self.accepted["original_function_field_primitive_generator_certified"] is True
        assert self.accepted["actual_cyclic_rank"] == FREE
        assert self.accepted["actual_determinant_mod_prime"] % self.accepted["prime"]
        assert self.definition["candidate_index"] == self.accepted["candidate_index"]
        assert self.definition["original_integer_scale"] == str(LEVEL**2)
        self.w0 = [int(x) for x in self.definition["w0_original_M2_integer_coordinates"]]
        assert len(self.w0) == 146 and self.w0[0] == self.w0[1] == 0 and any(self.w0)
        assert self.accepted["w0_original_M2_integer_coordinates"] == [str(x) for x in self.w0]
        assert cert806["actual_w0_original_M2_integer_coordinates"] == [str(x) for x in self.w0]
        self.Mw_index = self.r806.indexed(cert806["polynomial_multiplier"])
        assert self.Mw_index["accepted_primitive_candidate"] == cert806["accepted_candidate"]
        assert self.Mw_index["w0_original_M2_integer_coordinates"] == [str(x) for x in self.w0]
        assert self.Mw_index["all272_columns_verified_in_all820_original_rows"] is True
        assert self.Mw_index["coefficient_field"] == "Q, certified by exact original rational coordinate equations"
        self.mapping = self.Mw_index["S_row_to_polynomial_coefficient"]
        assert len(self.mapping) == DIM
        for index, row in enumerate(self.mapping):
            assert row == {"S_row": index, "normal_basis_row": S_position(index)[0],
                           "power_of_z": S_position(index)[1]}
        self.inverse_spec = self.accepted["fixed_minor_inverse"]
        self.inverse_data = self.r806.indexed(self.inverse_spec)
        assert self.inverse_data["original_coordinate_chart"] == cert806["coordinate_chart"]
        assert self.inverse_data["original_R805_short_minor"] == self.Sindex["short_minor"]
        assert self.inverse_data["coordinate_row_indices"] == self.I
        assert self.inverse_data["fixed_minor_dimension"] == DIM
        assert self.inverse_data["modular_inverse_identity_verified"] is True
        assert self.inverse_data["new_row_selection_or_old_R805_rank_recomputed"] is False
        self.prime = self.inverse_data["prime"]
        assert self.prime == self.accepted["prime"] and self.prime > LEVEL
        assert self.inverse_data["prime_proved"] is True
        assert len(self.inverse_data["inverse_mod_prime"]) == DIM
        assert all(len(row) == DIM for row in self.inverse_data["inverse_mod_prime"])
        self.sigma = [0]*146
        self.sigma[1], self.sigma[73] = 1, self.n
        self.support = sorted({0} | {i for i, value in enumerate(self.sigma) if value} |
                              {i for i, value in enumerate(self.w0) if value})
        self.original_sources, self.original_recipes = {}, {}
        alias_by_key = {(row["power"], row["index"]): row for row in self.alias["rows"]}
        assert len(alias_by_key) == 1254
        for i in range(146):
            row = alias_by_key[2, i]
            assert row["sorted_M2_leaf_indices"] == sorted((0, i))
            name = "R786-exact-power-2-row-"+str(i).zfill(4)+".json.gz"
            assert row["source"] == self.r786.source(name)
            assert plain_spec(row["source"]) == self.r786.inventory[name]
        for i in self.support:
            for power in (1, 2):
                row = alias_by_key[power, i]
                assert row["sorted_M2_leaf_indices"] == ([i] if power == 1 else sorted((0, i)))
                name = "R786-exact-power-"+str(power)+"-row-"+str(i).zfill(4)+".json.gz"
                assert row["source"] == self.r786.source(name)
                assert plain_spec(row["source"]) == self.r786.inventory[name]
                self.original_sources[power, i] = row["source"]
                self.original_recipes[power, i] = row["recipe"]
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "R813_proof_sha256": sha(args.proof), "R813_method_sha256": sha(args.method),
            "p": P, "qY_count": COUNT, "full_coordinate_rows": ROWS,
            "S3_basis_dimension": DIM, "normal_basis_rank": FREE, "normal_basis_degrees": EPS,
            "original_M2_integer_scale": str(LEVEL**2), "original_S3_integer_scale": str(LEVEL**6),
            "original_V2_integer_scale": str(LEVEL**4),
            "original_D0_qY_multiplier": ["1", "82"],
            "producer_identities": {label: producer_identity(self.inputs[label].spec) for label in sorted(LABELS)},
            "original_pencil": cert805["pencil_stage"], "original_S3_basis_index": cert805["S_basis_index"],
            "original_graded_free_basis": cert805["graded_free_basis_stage"],
            "original_coordinate_chart": cert806["coordinate_chart"],
            "actual_primitive_candidate": cert806["accepted_candidate"],
            "actual_candidate_definition": self.accepted["candidate_definition"],
            "actual_w0_original_M2_integer_coordinates": [str(x) for x in self.w0],
            "actual_sigma_integer_n": self.n, "reused_R806_modular_inverse": self.inverse_spec,
            "actual_reused_prime": self.prime, "coordinate_row_indices": self.I,
            "target_names": ["g", "h"], "reconstruct_every_digits": self.item["reconstruct_every_digits"],
            "Wronskian_generation": "D0(tau*s)-2*s*D0(tau); all tau*e_i are old V2[i]",
            "old_S3_selection_inverse_or_original_product_prefixes_recomputed": False,
            "actual_Mg_Mh_Gamma_or_height_computed": False,
        }
        self.original_cache = {}
        self.C = self.square = self.inverse = None
        self.coordinate_interface = None
        T = fmpz_poly([0, 1])
        self.chebyshev = [fmpz_poly([2]), T]
        for _ in range(2, 21):
            self.chebyshev.append(T*self.chebyshev[-1]-self.chebyshev[-2])
        self.gt = fmpz_poly([1])
        for poly in self.chebyshev[1:]:
            self.gt += poly

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes-45:
            raise BudgetStop("Completed two-Wronskian inputs and latest exact divided-residual lift retained.")

    def path(self, name):
        assert name.startswith("R813-") and Path(name).name == name
        return self.out/(name if name.endswith(".json.gz") else name+".json.gz")

    def cached(self, name, current=False):
        path = self.path(name)
        if not path.exists():
            return None
        data = read(path)
        assert data["configuration"] == self.tag
        assert data["complete"] is (not current)
        if current:
            assert name.endswith("-dixon-current") and data["complete_coordinates_claimed"] is False
        return data

    def store(self, name, value, current=False):
        assert not current or name.endswith("-dixon-current")
        save(self.path(name), dict(value, complete=not current, configuration=self.tag))
        return file_spec(self.path(name))

    def real_rows(self, rows):
        answer = []
        for n, row in enumerate(rows):
            cyclic = [0]*P
            for r, value in enumerate(row):
                cyclic[(r+10*n) % P] += int(value)
            reduced = [value-cyclic[40] for value in cyclic[:40]]+[0]
            assert all(reduced[r] == reduced[P-r] for r in range(1, 21))
            polynomial = fmpz_poly([reduced[0]])
            for r in range(1, 21):
                polynomial += self.chebyshev[r]*reduced[r]
            polynomial %= self.gt
            answer.append([int(polynomial[r]) for r in range(REAL)])
        return answer

    def original(self, power, index):
        key = power, index
        if key not in self.original_cache:
            source = self.original_sources[key]
            data = self.r786.indexed(source)
            assert data["weight"] == 2*power and data["bound_qY"] == 128
            assert data["integer_scale"] == str(LEVEL**(2*power))
            assert data["recipe"] == self.original_recipes[key]
            assert data["original_R775_finite_coefficients_verified"] is True
            rows = data["integer_qY_xi_coefficients"]
            assert len(rows) == 129 and all(len(row) == CYC for row in rows)
            raw = [[int(x) for x in row] for row in rows[:COUNT]]
            self.original_cache[key] = {"q": raw, "v": self.real_rows(raw), "source": source}
        return self.original_cache[key]

    def load_chart(self):
        if self.C is not None:
            return
        columns = []
        for index, spec in enumerate(self.Sindex["basis_rows"]):
            self.budget()
            data = self.r805.indexed(spec)
            assert data["index"] == index and data["recipe"] == spec["recipe"]
            assert data["integer_scale"] == str(LEVEL**6) and data["qY_count"] == COUNT
            assert data["free_basis_stage"] == self.r805.certificate["graded_free_basis_stage"]
            assert data["all_original_and_real_coordinates_verified"] is True
            assert data["V3_membership_has_original_product_generation_witness"] is True
            rows = data["integer_v_t_coefficients"]
            assert len(rows) == COUNT and all(len(row) == REAL for row in rows)
            columns.append([int(x) for row in rows for x in row])
        self.C = fmpz_mat(columns).transpose()
        self.square = fmpz_mat([[self.C[i, j] for j in range(DIM)] for i in self.I])
        self.inverse = nmod_mat(self.inverse_data["inverse_mod_prime"], self.prime)
        # The inverse was already certified by R806. This producer reuses it, rather than recomputing it.
        name = "R813-original-S3-coordinate-interface"
        payload = {
            "original_R805_S3_basis_index": self.r805.certificate["S_basis_index"],
            "original_R805_short_minor": self.Sindex["short_minor"],
            "original_R806_coordinate_chart": self.r806.certificate["coordinate_chart"],
            "reused_R806_modular_inverse": self.inverse_spec,
            "all_original_S3_basis_rows": self.Sindex["basis_rows"],
            "coordinate_row_indices": self.I, "S3_dimension": DIM, "full_coordinate_rows": ROWS,
            "original_S3_integer_scale": str(LEVEL**6),
            "normal_basis_rank": FREE, "normal_basis_degrees": EPS,
            "S3_row_to_polynomial_coefficient": self.mapping,
            "old_rank_row_selection_or_modular_inverse_recomputed": False,
        }
        old = self.cached(name)
        if old is None:
            self.store(name, payload)
        else:
            for key, value in payload.items():
                assert old[key] == value
        self.coordinate_interface = file_spec(self.path(name))

    def linear_input(self, target):
        assert target in ("g", "h")
        coordinates = self.sigma if target == "g" else self.w0
        name = "R813-"+target+"-original-linear-form-and-old-tau-product"
        old = self.cached(name)
        if old is None:
            raw = [[0]*CYC for _ in range(COUNT)]
            real = [[0]*REAL for _ in range(COUNT)]
            product_raw = [[0]*CYC for _ in range(COUNT)]
            product_real = [[0]*REAL for _ in range(COUNT)]
            sources = []
            for i, coefficient in enumerate(coordinates):
                if not coefficient:
                    continue
                self.budget()
                s, product = self.original(1, i), self.original(2, i)
                for n in range(COUNT):
                    for r in range(CYC):
                        raw[n][r] += coefficient*s["q"][n][r]
                        product_raw[n][r] += coefficient*product["q"][n][r]
                    for r in range(REAL):
                        real[n][r] += coefficient*s["v"][n][r]
                        product_real[n][r] += coefficient*product["v"][n][r]
                sources.append({"original_M2_index": i, "coefficient": str(coefficient),
                                "original_M2_source": s["source"], "old_tau_M2_product_source": product["source"]})
            assert self.real_rows(raw) == real and self.real_rows(product_raw) == product_real
            self.store(name, {
                "target": target, "s": "sigma" if target == "g" else "original_w0",
                "original_M2_integer_coordinates": [str(x) for x in coordinates],
                "original_M2_integer_scale": str(LEVEL**2),
                "original_tau_s_product_integer_scale": str(LEVEL**4),
                "actual_original_sources": sources, "qY_count": COUNT,
                "integer_qY_xi_coefficients": [[str(x) for x in row] for row in raw],
                "integer_v_t_coefficients": [[str(x) for x in row] for row in real],
                "old_tau_s_integer_qY_xi_coefficients": [[str(x) for x in row] for row in product_raw],
                "old_tau_s_integer_v_t_coefficients": [[str(x) for x in row] for row in product_real],
                "all_tau_e_i_products_read_from_original_V2_aliases": True,
                "old_product_coefficients_recomputed": False,
                "original_qY_v_and_xi_phases_preserved": True,
            })
            old = self.cached(name)
        assert old["target"] == target and old["original_M2_integer_coordinates"] == [str(x) for x in coordinates]
        assert old["all_tau_e_i_products_read_from_original_V2_aliases"] is True
        return old, file_spec(self.path(name))

    def weighted_product(self, target):
        source, source_spec = self.linear_input(target)
        name = "R813-"+target+"-new-weighted-formal-convolution"
        old = self.cached(name)
        tau = self.original(1, 0)
        if old is None:
            self.budget()
            raw_input = [[int(x) for x in row] for row in source["integer_qY_xi_coefficients"]]
            real_input = [[int(x) for x in row] for row in source["integer_v_t_coefficients"]]
            raw_derivative = [[n*x for x in row] for n, row in enumerate(tau["q"])]
            real_derivative = [[n*x for x in row] for n, row in enumerate(tau["v"])]
            qvalue = packed(raw_input, 79).mul_low(packed(raw_derivative, 79), 79*COUNT)
            vvalue = packed(real_input, 39).mul_low(packed(real_derivative, 39), 39*COUNT)
            raw, direct = [], []
            for n in range(COUNT):
                cyclic = [0]*P
                for r in range(79):
                    cyclic[r % P] += int(qvalue[79*n+r])
                raw.append([cyclic[r]-cyclic[40] for r in range(CYC)])
                polynomial = fmpz_poly([vvalue[39*n+r] for r in range(39)]) % self.gt
                direct.append([int(polynomial[r]) for r in range(REAL)])
            real = self.real_rows(raw)
            assert real == direct
            self.store(name, {
                "target": target, "source_original_s_and_tau_s": source_spec,
                "source_original_tau": tau["source"], "qY_count": COUNT,
                "formal_product": "s*(qY*d/dqY)(tau); the original D0 factor1/82 is applied later",
                "integer_qY_xi_coefficients": [[str(x) for x in row] for row in raw],
                "integer_v_t_coefficients": [[str(x) for x in row] for row in real],
                "one_new_weighted_convolution_per_target": True,
                "original_qY_v_and_xi_phases_verified": True,
                "this_formal_product_alone_claimed_to_be_a_modular_section": False,
                "old_unweighted_tau_s_product_recomputed": False,
            })
            old = self.cached(name)
        assert old["source_original_s_and_tau_s"] == source_spec
        assert old["source_original_tau"] == tau["source"]
        assert old["original_qY_v_and_xi_phases_verified"] is True
        return old, file_spec(self.path(name))

    def target(self, target):
        name = "R813-"+target+"-original-Wronskian-full-prefix"
        old = self.cached(name)
        if old is None:
            source, source_spec = self.linear_input(target)
            product, product_spec = self.weighted_product(target)
            old_raw = source["old_tau_s_integer_qY_xi_coefficients"]
            old_real = source["old_tau_s_integer_v_t_coefficients"]
            new_raw = product["integer_qY_xi_coefficients"]
            new_real = product["integer_v_t_coefficients"]
            raw = [[n*int(old_raw[n][r])-2*int(new_raw[n][r]) for r in range(CYC)] for n in range(COUNT)]
            real = [[n*int(old_real[n][r])-2*int(new_real[n][r]) for r in range(REAL)] for n in range(COUNT)]
            assert self.real_rows(raw) == real
            assert all(value == 0 for value in real[0]), "Original Wronskian must vanish at every cusp."
            flat = [value for row in real for value in row]
            content = integer_content(flat)
            assert content, "The actual nonconstant original function has zero Wronskian prefix."
            self.store(name, {
                "target": target, "qY_count": COUNT, "full_coordinate_rows": ROWS,
                "original_linear_form_and_old_product": source_spec,
                "new_weighted_formal_product": product_spec,
                "primitive_integer_v_t_coordinates": [str(value//content) for value in flat],
                "original_rational_scale": pairs(fmpq(content, LEVEL)),
                "original_D0_qY_multiplier": ["1", "82"],
                "exact_equation": "W(tau,s)=(qY*d/dqY)(old_tau_s)/82 -2*new_s_qY_dtau/82",
                "homogeneous_target": "G=W(tau,sigma)" if target == "g" else "J=W(tau,original_w0)",
                "normal_function": "delta(z)=G/tau^3" if target == "g" else "delta(w)=J/tau^3",
                "source_M2_scale": str(LEVEL**2), "coordinate_basis_S3_scale": str(LEVEL**6),
                "source_old_V2_scale": str(LEVEL**4),
                "scale_82_not_adjusted_by_weight_guess": True,
                "ordinary_V3_membership_by_original_Wronskian_proof": True,
                "constant_cusp_coefficient_exactly_zero": True,
                "actual_full_prefix_nonzero": True,
                "qY_xi_and_v_t_representations_exactly_agree": True,
            })
            old = self.cached(name)
        assert old["target"] == target and old["full_coordinate_rows"] == ROWS
        assert old["original_D0_qY_multiplier"] == ["1", "82"]
        assert old["actual_full_prefix_nonzero"] is True
        assert old["ordinary_V3_membership_by_original_Wronskian_proof"] is True
        values = [int(x) for x in old["primitive_integer_v_t_coordinates"]]
        assert len(values) == ROWS and any(values)
        assert dq(old["original_rational_scale"])
        return values, old["original_rational_scale"], file_spec(self.path(name))

    def reconstruct(self, lifted, modulus, target):
        values = []
        for row in lifted:
            recovered = []
            for value in row:
                rational = rational_reconstruct(value, modulus)
                if rational is None:
                    return None
                recovered.append(rational)
            values.append(recovered)
        denominators = []
        for column in range(2):
            denominator = 1
            for row in values:
                denominator = math.lcm(denominator, int(row[column].denom()))
            denominators.append(denominator)
        numerators = fmpz_mat([
            [int(value.numer())*(denominators[j]//int(value.denom())) for j, value in enumerate(row)]
            for row in values])
        actual = self.C*numerators
        for i in range(ROWS):
            for j in range(2):
                if actual[i, j] != target[i, j]*denominators[j]:
                    return None
        return numerators, denominators

    def exact_coordinates(self):
        self.load_chart()
        targets = [self.target(name) for name in ("g", "h")]
        target_specs = [item[2] for item in targets]
        scales = [item[1] for item in targets]
        name, current_name = "R813-two-exact-S3-Wronskian-coordinates", "R813-two-Wronskians-dixon-current"
        old = self.cached(name)
        if old is not None:
            assert old["target_names"] == ["g", "h"]
            assert old["source_target_prefixes"] == target_specs
            assert old["original_target_rational_scales"] == scales
            assert old["source_coordinate_interface"] == self.coordinate_interface
            assert old["reused_R806_modular_inverse"] == self.inverse_spec
            assert old["all820_original_coordinates_verified"] is True
            if self.path(current_name).exists():
                current = self.cached(current_name, current=True)
                assert current["source_target_prefixes"] == target_specs
                assert current["source_coordinate_interface"] == self.coordinate_interface
                assert current["reused_R806_modular_inverse"] == self.inverse_spec
                self.path(current_name).unlink()
            return old, file_spec(self.path(name))
        target = fmpz_mat([item[0] for item in targets]).transpose()
        assert target.nrows() == ROWS and target.ncols() == 2
        ni = [[int(target[i, j]) for j in range(2)] for i in self.I]
        binding = {
            "source_target_prefixes": target_specs, "original_target_rational_scales": scales,
            "source_coordinate_interface": self.coordinate_interface,
            "reused_R806_modular_inverse": self.inverse_spec,
            "target_names": ["g", "h"],
        }
        binding_hash = fingerprint(binding)
        current = self.cached(current_name, current=True)
        if current is None:
            lifted, residual, digits, modulus = [[0, 0] for _ in range(DIM)], ni, 0, 1
            previous_sha = None
        else:
            for key, value in binding.items():
                assert current[key] == value
            assert current["rhs_binding_sha256"] == binding_hash and current["prime"] == self.prime
            digits, modulus = current["digits"], int(current["modulus"])
            assert digits >= 1 and modulus == self.prime**digits
            lifted = [[int(x) for x in row] for row in current["lifted_integer_coordinates"]]
            residual = [[int(x) for x in row] for row in current["exact_divided_residual"]]
            assert len(lifted) == len(residual) == DIM
            assert all(len(row) == 2 for row in lifted+residual)
            assert all(0 <= value < modulus for row in lifted for value in row)
            actual = self.square*fmpz_mat(lifted)
            assert all(actual[i, j]+modulus*residual[i][j] == ni[i][j]
                       for i in range(DIM) for j in range(2))
            previous_sha = sha(self.path(current_name))
        while True:
            self.budget()
            if digits and (digits == 1 or digits % self.item["reconstruct_every_digits"] == 0):
                recovered = self.reconstruct(lifted, modulus, target)
                if recovered is not None:
                    numerators, denominators = recovered
                    assert all(denominator > 0 and denominator % self.prime for denominator in denominators)
                    assert all(any(numerators[i, j] for i in range(DIM)) for j in range(2))
                    self.store(name, {
                        "target_names": ["g", "h"], "column_indices": [0, 1],
                        "S3_basis_dimension": DIM, "normal_basis_rank": FREE,
                        "coordinate_numerators": matrix_rows(numerators, strings=True),
                        "column_denominators": [str(x) for x in denominators],
                        "original_target_rational_scales": scales,
                        "coordinate_convention": "actual S3 coordinate=numerator/column_denominator*original_target_rational_scale",
                        "original_D0_qY_multiplier": ["1", "82"],
                        "original_S3_integer_scale": str(LEVEL**6),
                        "source_target_prefixes": target_specs,
                        "source_coordinate_interface": self.coordinate_interface,
                        "reused_R806_modular_inverse": self.inverse_spec,
                        "rhs_binding_sha256": binding_hash,
                        "actual_prime": self.prime, "actual_Dixon_digits": digits,
                        "actual_reconstruction_modulus": str(modulus),
                        "full_coordinate_rows": ROWS, "all820_original_coordinates_verified": True,
                        "both_original_Wronskians_actually_nonzero": True,
                        "original_1_over82_and_all_integer_scales_preserved": True,
                        "rational_reconstruction_used_uniform_strict_rectangular_bound": True,
                        "old_modular_inverse_or_rank_recomputed": False,
                        "characteristic_zero_inverse_matrix_formed": False,
                    })
                    self.path(current_name).unlink(missing_ok=True)
                    print(json.dumps({"stage": "two_exact_original_Wronskians", "digits": digits,
                        "full_rows_verified": ROWS, "seconds": time.monotonic()-self.started}), flush=True)
                    return self.cached(name), file_spec(self.path(name))
            correction = self.inverse*nmod_mat(
                [[value % self.prime for value in row] for row in residual], self.prime)
            delta = matrix_rows(correction)
            if digits == 0:
                full = nmod_mat([[int(self.C[i, j]) % self.prime for j in range(DIM)]
                                  for i in range(ROWS)], self.prime)*correction
                assert all(int(full[i, j]) == int(target[i, j]) % self.prime
                           for i in range(ROWS) for j in range(2)), "Original Wronskians outside actual S3 span mod prime."
            product = self.square*fmpz_mat(delta)
            updated = []
            for i in range(DIM):
                row = []
                for j in range(2):
                    numerator = residual[i][j]-int(product[i, j])
                    assert numerator % self.prime == 0
                    row.append(numerator//self.prime)
                    lifted[i][j] += modulus*delta[i][j]
                updated.append(row)
            residual, modulus, digits = updated, modulus*self.prime, digits+1
            payload = dict(binding, prime=self.prime, digits=digits, modulus=str(modulus),
                rhs_binding_sha256=binding_hash,
                lifted_integer_coordinates=[[str(x) for x in row] for row in lifted],
                exact_divided_residual=[[str(x) for x in row] for row in residual],
                previous_checkpoint_sha256=previous_sha,
                invariant="original_minor*lift+prime^digits*residual=primitive_Wronskian_targets_I",
                complete_coordinates_claimed=False, only_current_full_lift_vector_retained=True)
            self.store(current_name, payload, current=True)
            current_sha = sha(self.path(current_name))
            receipt_name = "R813-two-Wronskians-dixon-digit-"+str(digits).zfill(6)+"-receipt"
            receipt = {
                "target_names": ["g", "h"], "prime": self.prime, "digits": digits,
                "modulus_bits": modulus.bit_length(), "rhs_binding_sha256": binding_hash,
                "current_checkpoint_sha256": current_sha, "previous_checkpoint_sha256": previous_sha,
                "exact_divided_residual_invariant_preserved": True,
                "large_lift_vector_or_residual_embedded": False,
            }
            prior = self.cached(receipt_name)
            if prior is None:
                self.store(receipt_name, receipt)
            else:
                for key, value in receipt.items():
                    assert prior[key] == value
            previous_sha = current_sha
            if digits == 1 or digits % self.item["reconstruct_every_digits"] == 0:
                print(json.dumps({"stage": "Dixon_two_original_Wronskians", "digits": digits,
                    "modulus_bits": modulus.bit_length(),
                    "seconds": time.monotonic()-self.started}), flush=True)

    def normal_interface(self, coordinates, coordinate_spec):
        name = "R813-original-g-h-normal-vector-interface"
        payload = {
            "target_names": ["g", "h"], "target_column_indices": {"g": 0, "h": 1},
            "original_functions": {"g": "delta(z)=W(tau,sigma)/tau^3",
                                   "h": "delta(w)=W(tau,original_w0)/tau^3"},
            "delta_definition": "D0/tau; D0=(qY/82)*d/dqY; original tau=e0",
            "normal_basis_rank": FREE, "normal_basis_degrees": EPS,
            "regular_degree_bound": 3, "coefficient_field": "Q in the unchanged original K-normal basis",
            "source_exact_S3_coordinates": coordinate_spec,
            "source_coordinate_interface": self.coordinate_interface,
            "S3_row_to_polynomial_coefficient": self.mapping,
            "original_R805_graded_free_basis": self.r805.certificate["graded_free_basis_stage"],
            "actual_R806_primitive_candidate": self.r806.certificate["accepted_candidate"],
            "actual_R806_polynomial_multiplier_index": self.r806.certificate["polynomial_multiplier"],
            "exact_coefficient_rule": "normal target coefficient at (a,j) = coordinate_numerators[S3_row][target_column] / column_denominators[target_column] * original_target_rational_scales[target_column]",
            "weighted_polynomial_support": "degree(v_target[a])<=3-eps_a",
            "both_original_normal_vectors_actually_nonzero": True,
            "all820_original_coordinates_verified": True,
            "original_1_over82_and_all_integer_scales_preserved": True,
            "original_Mw_coordinate_values_consumed": False,
            "actual_Mg_Mh_or_Gamma_computed": False,
            "actual_original_y_derivative_or_function_DAG_computed": False,
            "actual_polar_divisors_eta_or_height_computed": False,
        }
        assert coordinates["all820_original_coordinates_verified"] is True
        assert coordinates["source_coordinate_interface"] == self.coordinate_interface
        old = self.cached(name)
        if old is None:
            self.store(name, payload)
        else:
            for key, value in payload.items():
                assert old[key] == value
        return file_spec(self.path(name))

    def run(self):
        final = self.out/FINAL
        if final.exists():
            cert = read(final)
            assert cert["result"] == RESULT and cert["complete"] is True
            assert cert["configuration"] == self.tag
            manifest = cert["stage_manifest"]
            assert file_spec(self.out/manifest["file"]) == manifest
            for row in self.cached(manifest["file"])["files"]:
                assert file_spec(self.out/row["file"]) == row
        else:
            coordinates, coordinate_spec = self.exact_coordinates()
            interface = self.normal_interface(coordinates, coordinate_spec)
            assert not list(self.out.glob("R813-*-dixon-current.json.gz"))
            files = [file_spec(path) for path in sorted(self.out.glob("R813-*.json.gz"))
                     if not path.name.startswith("R813-stage-manifest-")]
            manifest = self.store("R813-stage-manifest-"+fingerprint(files)[:24], {"files": files})
            cert = {
                "result": RESULT, "complete": True, "configuration": self.tag,
                "p": P, "completed_scope": "two_original_S3_Wronskian_inputs",
                "target_names": ["g", "h"], "actual_rational_RHS_columns": 2,
                "S3_basis_dimension": DIM, "qY_count": COUNT, "full_coordinate_rows": ROWS,
                "normal_basis_rank": FREE, "normal_basis_degrees": EPS,
                "regular_degree_bound": 3,
                "actual_sigma_integer_n": self.n,
                "actual_R806_candidate_index": self.accepted["candidate_index"],
                "actual_w0_original_M2_integer_coordinates": [str(x) for x in self.w0],
                "actual_reused_prime": self.prime,
                "source_coordinate_interface": self.coordinate_interface,
                "reused_R806_modular_inverse": self.inverse_spec,
                "exact_coordinate_stage": coordinate_spec, "normal_vector_interface": interface,
                "source_actual_R806_primitive_multiplier": self.r806.certificate["polynomial_multiplier"],
                "all820_original_coordinates_verified_for_both_targets": True,
                "both_original_normal_vectors_actually_nonzero": True,
                "original_D0_qY_multiplier": ["1", "82"],
                "original_M2_integer_scale": str(LEVEL**2),
                "original_V2_integer_scale": str(LEVEL**4),
                "original_S3_integer_scale": str(LEVEL**6),
                "original_1_over82_and_all_integer_scales_preserved": True,
                "old_S3_rank_inverse_or_unweighted_products_recomputed": False,
                "actual_Mg_Mh_or_Gamma_computed": False,
                "actual_original_y_derivative_or_function_DAG_computed": False,
                "actual_polar_divisors_eta_or_height_computed": False,
                "stage_manifest": manifest, "seconds": time.monotonic()-self.started,
            }
            save(final, cert)
        save(self.out/"core-receipt.json", {
            "result": RESULT, "complete": True, "source_sha256": sha(__file__),
            "certificate_sha256": sha(final),
            "completed_scope": "two_original_S3_Wronskian_inputs",
            "actual_rational_RHS_columns": 2,
            "all820_original_coordinates_verified_for_both_targets": True,
            "actual_Mg_Mh_or_Gamma_computed": False,
            "actual_original_y_derivative_or_function_DAG_computed": False,
            "actual_polar_divisors_eta_or_height_computed": False,
        })
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
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "error": type(error).__name__+": "+str(error),
            "completed_original_inputs_and_latest_exact_lift_preserved": True,
            "actual_Mg_Mh_or_Gamma_computed": False,
            "actual_polar_divisors_eta_or_height_computed": False,
        })
        raise


if __name__ == "__main__":
    sys.exit(main())



