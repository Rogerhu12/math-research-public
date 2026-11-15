#!/usr/bin/env python3
"""R803: four original M6 rows, five mixed Hodge products, finite exact RHS."""
import argparse
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
from flint import fmpq, fmpq_poly, fmpz, fmpz_mat, nmod_mat

RESULT = "R803-original-M6-mixed-Hodge-ratios"
FINAL = "p41-original-M6-mixed-Hodge-ratios-certificate.json"
P, LEVEL, ORDERS, CYC, LDEG, DIM, ROWS = 41, 82, 42, 40, 14, 694, 1680
HODGE_DEN = 1722
M6 = "R775-basis-M6-complete.json.gz"
M6_SHA = "70ff7536b50bf99ffb422b7c17dd320b535738fcfcc562fd1597eebcb7a0b299"
SCALARS = "R774-original-L-cubic-scalars.json.gz"
SCALARS_SHA = "b5b1232fa0585e6437d0e8d5f92b81efe672e91ed417bce7f6bc66c6456d596e"
MODULE = "R794-original-CM-module-and-finite-norm-candidates.json.gz"
MODULE_SHA = "c7dbe30e9cc1d63032f8428cc47e6539ba328c3e35cd8e9186c9ec5dc95c47fc"
SELECTED = "R794-selected-original-low-degree-eta-basis.json.gz"
SELECTED_SHA = "5b96f623e1f43d834a7db21064ff2cb101284b9a4038e5434eb291b6e73f6e0f"
MAPS = "R759-original-integral-maps-and-bounded-recovery-input.json.gz"
MAPS_SHA = "037b56d016d502408173319d76a3067a65dd50250c31bc2225c0fca598396ecc"
H3_INPUTS = {
    "R774-exact-H3-qY-0001-0032.json.gz": "4ded35d80590f86802c55c3cb73e04e5e38e834823d47b21dc5b0bbaaa6aa612",
    "R774-exact-H3-qY-0033-0064.json.gz": "80a7ed979e5a4f283082211891af8e6e4be0bfc098c34106bffb9881620d5708"}
LABELS = {"R774", "R775", "R786", "R794", "R759"}


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
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb", mtime=0, compresslevel=2) as compressed:
                compressed.write(raw)
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
    certificate = left["certificate_name"]
    assert left["files"][certificate] == right["files"][certificate]
    for name in set(left["files"]) & set(right["files"]):
        assert left["files"][name] == right["files"][name]


def pairs(value):
    return [str(value.numer()), str(value.denom())]


def dq(value):
    assert len(value) == 2 and int(value[1]) > 0
    return fmpq(int(value[0]), int(value[1]))


def dp(value):
    return fmpq_poly([int(v) for v in value["numerator"]], int(value["denominator"]))


def ep(value):
    return {"numerator": [str(v) for v in value.numer().coeffs()], "denominator": str(value.denom())}


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


class OriginalL:
    """Original Q(b,zeta), b unchanged; no scaled B field or CM direction change."""
    def __init__(self, encoded_modulus):
        self.mod = dp(encoded_modulus)
        assert self.mod.degree() == 7 and self.mod[7] == 1

    def zero(self):
        return fmpq_poly([]), fmpq_poly([])

    def decode(self, value):
        assert len(value) == 2
        result = dp(value[0]), dp(value[1])
        assert all(poly.degree() < 7 for poly in result)
        return result

    def encode(self, value):
        return [ep(value[0]), ep(value[1])]

    def add(self, left, right):
        return left[0]+right[0], left[1]+right[1]

    def scale(self, value, scalar):
        return value[0]*scalar, value[1]*scalar

    def multiply(self, left, right):
        a, b = left
        c, d = right
        bd = b*d
        return (a*c-bd) % self.mod, (a*d+b*c-bd) % self.mod


class Retained:
    def __init__(self, root, label, spec):
        self.label, self.spec, self.directory = label, spec, Path(root)/label
        manifest_path = self.directory/"full-outputs-manifest.json"
        assert sha(manifest_path) == spec["manifest_sha256"]
        manifest = read(manifest_path)
        assert manifest["result"] == spec["result"]
        self.files = {row["file"]: row for row in manifest["files"]}
        assert len(self.files) == len(manifest["files"])
        self.checked = set()
        run, core, initial = (self.raw(name) for name in
            ("run-receipt.json", "core-receipt.json", "public-actions-input.json"))
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert str(run["workflow_run_id"]) == str(spec["run_id"])
        assert run["source_commit"] == initial["source_commit"] == spec["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["result"] == core["result"] == spec["result"]
        assert core["complete"] is True and core["source_sha256"] == spec["core_sha256"]
        if label == "R794":
            assert initial["job"]["core_sha256"] == spec["core_sha256"]
            assert "core_receipt_sha256" not in run and "core_sha256" not in initial
        else:
            assert run["result"] == spec["result"]
            assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
            assert initial["core_sha256"] == spec["core_sha256"]
            if label == "R759":
                assert "job" not in initial
            else:
                assert initial["job"]["core_sha256"] == spec["core_sha256"]
        self.initial = initial
        name = spec["certificate_name"]
        assert self.files[name]["sha256"] == core["certificate_sha256"] == spec["files"][name]
        self.certificate = self.raw(name)
        assert self.certificate["result"] == spec["result"] and self.certificate["complete"] is True
        self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == spec["core_sha256"] and self.tag["python_flint"] == "0.9.0"

    def raw(self, name, expected=None):
        assert Path(name).name == name
        spec = self.files[name]
        if expected is not None:
            assert spec["sha256"] == expected
        if name in self.spec["files"]:
            assert spec["sha256"] == self.spec["files"][name]
        path = self.directory/name
        if name not in self.checked:
            assert path.stat().st_size == spec["bytes"] and sha(path) == spec["sha256"]
            self.checked.add(name)
        return read(path)

    def stage(self, name, expected=None):
        value = self.raw(name, expected)
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def cert_stage(self, name, expected=None):
        stage_specs = {row["file"]: row for row in self.certificate["stages"]}
        assert plain_spec(stage_specs[name]) == plain_spec(self.files[name])
        return self.stage(name, expected)

    def source(self, name):
        return dict(plain_spec(self.files[name]), producer=self.label)


class BudgetStop(RuntimeError):
    pass


class Job:
    def __init__(self, args):
        self.args, self.out, self.started = args, args.output, time.monotonic()
        self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        assert self.item["producer_inputs_pending"] is False
        assert self.item["result"] == RESULT and self.item["p"] == P and self.item["core_sha256"] == sha(__file__)
        assert flint.__version__ == "0.9.0"
        assert sha(args.proof) == self.item["R803_proof_sha256"]
        assert sha(args.method) == self.item["R803_method_sha256"]
        assert self.item["qY_count"] == ORDERS and self.item["M6_dimension"] == DIM
        assert self.item["mixed_indices"] == [1, 2, 3, 4, 5]
        assert self.item["coordinate_indices"] == [0, 1, 2, 3, 4, 5]
        assert self.item["auxiliary_prime_start"] == 1000000007
        assert self.item["reconstruct_every_digits"] == 8
        assert set(self.item["retained_artifacts"]) == LABELS
        self.inputs = {label: Retained(args.retained, label, self.item["retained_artifacts"][label])
                       for label in ("R774", "R775", "R786", "R794", "R759")}
        self.r774, self.r775, self.r786, self.r794, self.r759 = \
            (self.inputs[label] for label in ("R774", "R775", "R786", "R794", "R759"))
        same_producer(self.r794.tag["retained_artifacts"]["R759"], self.r759.spec)
        same_producer(self.r794.initial["job"]["retained_artifacts"]["R759"], self.r759.spec)
        for name in (MAPS, self.r759.spec["certificate_name"]):
            assert self.r774.tag["retained_input_sha256"][name] == self.r759.files[name]["sha256"]
        assert self.r774.tag["H_normalization"] == "H=alpha*F/1722; alpha^3=4"
        assert self.r774.tag["cube_normalization"] == "H^3=4*F^3/1722^3"
        assert self.r774.tag["c1_phase_applied_a_second_time"] is False
        assert self.r774.certificate["qY_constant_coefficient_zero"] is True
        assert self.r774.certificate["exact_H_cubed_nonzero"] is True
        assert self.r774.certificate["no_Neron_Manin_or_KS_scale_changed"] is True
        self.witness = self.r774.cert_stage(SCALARS, SCALARS_SHA)
        self.L = OriginalL(self.witness["original_b_minimal_polynomial"])
        self.triples = list(itertools.combinations_with_replacement(range(6), 3))
        assert self.witness["triples"] == [list(row) for row in self.triples] and len(self.triples) == 56
        self.original_maps = self.r759.cert_stage(MAPS, MAPS_SHA)
        assert self.original_maps["selected_index"] == 4 and self.original_maps["selected_degree"] == "1206"
        assert self.original_maps["Z_basis_rank"] == 12 and self.original_maps["O_K_rank"] == 6
        assert self.original_maps["c1_coset"] == 4424
        all_maps = self.original_maps["all_twelve_integral_map_differential_vectors_in_original_omega_basis"]
        assert len(all_maps) == 12 and all(len(row) == 6 for row in all_maps)
        assert all_maps[4] == self.witness["selected_original_v_in_omega_basis"]
        self.all_v = [[self.L.decode(value) for value in row] for row in all_maps]
        self.v = self.all_v[4]
        self.module = self.r794.cert_stage(MODULE, MODULE_SHA)
        assert self.module["cyclic_basis"] == "T^k*f4, k=0..11; original R791 column action"
        assert self.module["Phi21_ascending"] == ["1", "-1", "0", "1", "-1", "0", "1", "0", "-1", "1", "0", "-1", "1"]
        self.cyclic = self.module["cyclic_basis_matrix"]
        assert len(self.cyclic) == 12 and all(len(row) == 12 for row in self.cyclic)
        assert all(dq(self.cyclic[i][0]) == int(i == 4) for i in range(12))
        assert all(value[1] == "1" for row in self.cyclic for value in row)
        selected = self.r794.cert_stage(SELECTED, SELECTED_SHA)
        assert selected["selected_candidate_indices"] == [0, 3, 1, 21, 15]
        assert selected["original_kappa_e_R_q_c0_c1_preserved"] is True
        assert len(selected["selected_maps"]) == 5
        for row in selected["selected_maps"]:
            assert len(row["a_in_Q_T_mod_Phi21"]) == 12
            assert all(value[1] == "1" for value in row["a_in_Q_T_mod_Phi21"])
        self.original_M6 = self.r775.cert_stage(M6, M6_SHA)
        assert self.original_M6["rank"] == len(self.original_M6["basis"]) == DIM
        assert self.original_M6["characteristic_zero_independence_certified_by_unit_reduction"] is True
        assert self.r775.tag["prime"] == 739 and self.r775.tag["xi41_mod_ell"] == 538
        expected_extra = [
            {"kind": "elliptic_layer_product", "factor": "E4", "power": 1, "index": 0},
            {"kind": "elliptic_layer_product", "factor": "E4", "power": 1, "index": 73},
            {"kind": "level_one", "name": "E6"}, {"kind": "level_one", "name": "eta12"}]
        assert [row["recipe"] for row in self.original_M6["basis"][690:]] == expected_extra
        for index, row in enumerate(self.original_M6["basis"][:690]):
            assert row["recipe"] == {"kind": "power_basis", "power": 3, "index": index}
        stages775 = {row["file"]: row for row in self.r775.certificate["stages"]}
        for name in ("R775-basis-M2.json.gz", "R775-basis-power-3.json.gz"):
            assert self.r786.tag["R775_completed_prefix_producer"]["files"][name] == stages775[name]["sha256"]
        inventory_spec = self.r786.certificate["stages_manifest"]
        assert plain_spec(inventory_spec) == plain_spec(self.r786.files[inventory_spec["file"]])
        inventory = self.r786.stage(inventory_spec["file"], inventory_spec["sha256"])
        self.rows786 = {row["file"]: row for row in inventory["files"]}
        assert len(self.rows786) == len(inventory["files"])
        self.tag = {"result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "R803_proof_sha256": sha(args.proof), "R803_method_sha256": sha(args.method),
            "retained_artifacts": self.item["retained_artifacts"], "p": P,
            "qY_count": ORDERS, "M6_dimension": DIM, "full_coordinate_rows": ROWS,
            "mixed_indices": [1, 2, 3, 4, 5], "coordinate_indices": [0, 1, 2, 3, 4, 5],
            "basis_integer_scale": str(LEVEL**6), "Hodge_common_denominator": HODGE_DEN,
            "auxiliary_prime_start": self.item["auxiliary_prime_start"],
            "reconstruct_every_digits": self.item["reconstruct_every_digits"],
            "original_reference_map": "R759 index4; f4(c0)=O; target y^2=x^3+b",
            "coordinate_basis": "b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b",
            "qY_parameter": "exp(2*pi*i*tau/82); original reference cusp",
            "old_U0_Hodge_monomials_Hom_periods_or_ordinary_basis_recomputed": False,
            "second_c1_phase_or_real_descent_isogeny_applied": False,
            "characteristic_zero_inverse_matrix_formed": False}
        self.A, self.basis_index_spec, self.short_sources = None, None, None
        self.tensor_matrix = None

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes-45:
            raise BudgetStop("Complete mixed stages and current exact RHS lifts retained for immediate continuation.")

    def path(self, name):
        assert name.startswith("R803-") and Path(name).name == name
        return self.out/(name+".json.gz")

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

    def old_power_row(self, power, index):
        name = "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"
        spec = self.rows786[name]
        assert plain_spec(spec) == plain_spec(self.r786.files[name])
        data = self.r786.stage(name, spec["sha256"])
        assert data["weight"] == 2*power and data["bound_qY"] == 128
        assert data["integer_scale"] == str(LEVEL**(2*power))
        assert data["original_R775_finite_coefficients_verified"] is True
        rows = data["integer_qY_xi_coefficients"]
        assert len(rows) == 129 and all(len(row) == CYC for row in rows)
        return [[int(x) for x in row] for row in rows[:ORDERS]], self.r786.source(name)

    def short_basis(self):
        if self.A is not None:
            return self.A
        columns, index_rows = [], []
        for index in range(690):
            rows, source = self.old_power_row(3, index)
            columns.append([x for row in rows for x in row])
            index_rows.append({"index": index, "recipe": self.original_M6["basis"][index]["recipe"],
                               "source": source, "source_prefix_read": [0, ORDERS],
                               "old_coefficients_recomputed": False})
        for index in range(690, DIM):
            name = "R803-new-original-M6-short-row-"+str(index)
            data = self.cached(name)
            recipe = self.original_M6["basis"][index]["recipe"]
            if data is None:
                self.budget()
                if index < 692:
                    raw, source = self.old_power_row(1, recipe["index"])
                    rows = [[value*LEVEL**4 for value in row] for row in raw]
                    sources = [source]
                else:
                    rows = [[0]*CYC for _ in range(ORDERS)]
                    rows[0 if index == 692 else 41][0] = LEVEL**6
                    sources = []
                finite = self.original_M6["basis"][index]["coefficients_mod_ell"]
                powers = [pow(538, r, 739) for r in range(CYC)]
                for n, row in enumerate(rows):
                    assert sum(value*power for value, power in zip(row, powers)) % 739 == \
                        pow(LEVEL, 6, 739)*(int(finite[n]) if n < len(finite) else 0) % 739
                self.store(name, {"index": index, "recipe": recipe,
                    "original_M6_stage": self.r775.source(M6), "original_factor_sources": sources,
                    "weight": 6, "integer_scale": str(LEVEL**6), "bound_qY": 41,
                    "integer_qY_xi_coefficients": [[str(x) for x in row] for row in rows],
                    "new_complete_short_row_verified_against_original_M6_mod739": True,
                    "old_M2_or_power3_prefix_recomputed": False, "coefficients_after_qY41_generated": False})
                data = self.cached(name)
            assert data["index"] == index and data["recipe"] == recipe
            assert data["integer_scale"] == str(LEVEL**6) and data["bound_qY"] == 41
            assert data["new_complete_short_row_verified_against_original_M6_mod739"] is True
            rows = data["integer_qY_xi_coefficients"]
            assert len(rows) == ORDERS and all(len(row) == CYC for row in rows)
            columns.append([int(x) for row in rows for x in row])
            index_rows.append({"index": index, "recipe": recipe,
                "source": dict(file_spec(self.path(name)), producer="R803"),
                "source_prefix_read": [0, ORDERS], "old_coefficients_recomputed": False})
        assert len(columns) == DIM and all(len(column) == ROWS for column in columns)
        name = "R803-original-M6-short-basis-index"
        data = self.cached(name)
        value = {"dimension": DIM, "qY_count": ORDERS, "xi_coordinate_count": CYC,
            "integer_scale": str(LEVEL**6), "coordinate_order": "qY exponent0..41, xi exponent0..39",
            "original_M6_stage": self.r775.source(M6), "basis_rows": index_rows,
            "old_power3_rows_read": 690, "new_short_rows": [690, 691, 692, 693],
            "original_basis_order_and_recipes_preserved": True, "old_coefficients_recomputed": False}
        if data is None:
            self.store(name, value)
        else:
            for key, expected in value.items():
                assert data[key] == expected
        self.basis_index_spec = file_spec(self.path(name))
        self.short_sources = index_rows
        self.A = fmpz_mat(columns).transpose()
        assert self.A.nrows() == ROWS and self.A.ncols() == DIM
        return self.A

    def tensors(self):
        if self.tensor_matrix is None:
            rows, sources = [], []
            for index, triple in enumerate(self.triples):
                name = "R774-cubic-monomial-"+str(index).zfill(2)+".json.gz"
                data = self.r774.cert_stage(name)
                assert data["indices"] == list(triple)
                assert data["G_exponent_range_exclusive"] == [0, 820] and data["xi_basis_degree"] == CYC
                for key in ("real_coefficients_flat_qY_xi", "s_coefficients_flat_qY_xi"):
                    assert len(data[key]) == 820*CYC
                    rows.append([int(x) for x in data[key][:(ORDERS-1)*CYC]])
                sources.append(self.r774.source(name))
            assert len(rows) == 112 and all(len(row) == (ORDERS-1)*CYC for row in rows)
            self.tensor_matrix = fmpz_mat(rows)
            self.tensor_sources = sources
        return self.tensor_matrix

    def mixed_scalars(self, j):
        assert 1 <= j <= 5
        name = "R803-mixed-original-Hodge-scalars-j"+str(j)
        old = self.cached(name)
        if old is not None:
            assert old["j"] == j and old["pure_U0_scalars_recomputed"] is False
            return old, file_spec(self.path(name))
        self.budget()
        column = [dq(self.cyclic[i][j]) for i in range(12)]
        w = []
        for a in range(6):
            value = self.L.zero()
            for i in range(12):
                value = self.L.add(value, self.L.scale(self.all_v[i][a], column[i]))
            w.append(value)
        assert any(a or b for a, b in w)
        products = {(a, b): self.L.multiply(self.v[a], self.v[b])
                    for a in range(6) for b in range(a, 6)}

        def term(a, b, c, scale=1):
            return self.L.scale(self.L.multiply(w[a], products[min(b, c), max(b, c)]), scale)

        mixed, rational = [], [[fmpq(0)]*112 for _ in range(LDEG)]
        for position, (a, b, c) in enumerate(self.triples):
            if a == c:
                value = term(a, a, a)
            elif a == b:
                value = self.L.add(term(c, a, a), term(a, a, c, 2))
            elif b == c:
                value = self.L.add(term(a, b, b), term(b, a, b, 2))
            else:
                value = self.L.add(self.L.add(term(a, b, c, 2), term(b, a, c, 2)), term(c, a, b, 2))
            value = self.L.scale(value, fmpq(4, HODGE_DEN**3))
            mixed.append(self.L.encode(value))
            real, imag = value[0]-value[1]/2, value[1]/2
            for i in range(7):
                rational[i][2*position], rational[i][2*position+1] = real[i], -3*imag[i]
                rational[7+i][2*position], rational[7+i][2*position+1] = imag[i], real[i]
        primitive, scales = [], []
        for row in rational:
            denominator = 1
            for value in row:
                denominator = math.lcm(denominator, int(value.denom()))
            integers = [int((value*denominator).numer()) for value in row]
            content = 0
            for value in integers:
                content = math.gcd(content, abs(value))
            if content:
                primitive.append([str(value//content) for value in integers])
                scales.append(pairs(fmpq(content, denominator)))
            else:
                primitive.append(["0"]*112)
                scales.append(["0", "1"])
        self.store(name, {"j": j, "map": "original T^"+str(j)+" f4",
            "source_cyclic_stage": self.r794.source(MODULE),
            "source_original_Hom_differentials": self.r759.source(MAPS),
            "source_cyclic_Hom_column": [pairs(value) for value in column],
            "original_w_j_in_omega_basis": [self.L.encode(value) for value in w],
            "original_v_f_in_omega_basis": self.witness["selected_original_v_in_omega_basis"],
            "mixed_scalars_in_original_1_zeta_by_triple": mixed,
            "triples": [list(triple) for triple in self.triples],
            "row_basis": ["b^"+str(i) for i in range(7)]+["s*b^"+str(i) for i in range(7)],
            "column_basis": "real,s parts of each old R774 monomial",
            "primitive_integer_matrix": primitive, "rational_row_scales": scales,
            "mixed_formula": "4*w_j*v_f*v_f/1722^3; exact mixed multiplicities; s^2=-3",
            "original_b_model": self.witness["original_b_minimal_polynomial"],
            "pure_U0_scalars_recomputed": False,
            "old_Hom_Galois_columns_or_periods_recomputed": False,
            "extra_rho_j_or_c1_phase_applied": False})
        return self.cached(name), file_spec(self.path(name))

    def rhs(self, j):
        assert 0 <= j <= 5
        if j == 0:
            rows = [[0]*ROWS for _ in range(LDEG)]
            covered, sources = {0}, [self.r774.source(SCALARS)]
            for name, digest in H3_INPUTS.items():
                block = self.r774.cert_stage(name, digest)
                first, stop = block["first_exponent"], block["last_exponent_exclusive"]
                assert (first, stop) in ((1, 33), (33, 65))
                assert block["rational_row_scale_stage_sha256"] == SCALARS_SHA
                assert block["coefficient_layout"] == "14 rows (b^i,s*b^i), columns (qY exponent,xi^r), r0..39"
                raw = block["integer_numerators"]
                assert len(raw) == LDEG and all(len(row) == (stop-first)*CYC for row in raw)
                for n in range(first, min(stop, ORDERS)):
                    assert n not in covered
                    covered.add(n)
                    for i in range(LDEG):
                        rows[i][n*CYC:(n+1)*CYC] = [int(x) for x in raw[i][(n-first)*CYC:(n+1-first)*CYC]]
                sources.append(self.r774.source(name))
            assert covered == set(range(ORDERS))
            scales = self.witness["rational_row_scales"]
        else:
            name = "R803-new-mixed-Hodge-prefix-j"+str(j)
            data = self.cached(name)
            if data is None:
                scalars, scalar_spec = self.mixed_scalars(j)
                self.budget()
                source = self.tensors()
                coefficient = fmpz_mat([[int(x) for x in row] for row in scalars["primitive_integer_matrix"]])
                target = coefficient*source
                assert target.nrows() == LDEG and target.ncols() == (ORDERS-1)*CYC
                values = [["0"]*CYC+[str(target[i, r]) for r in range(target.ncols())] for i in range(LDEG)]
                self.store(name, {"j": j, "first_exponent": 0, "last_exponent_exclusive": ORDERS,
                    "xi_coordinate_count": CYC, "L_coordinate_count": LDEG,
                    "integer_numerators": values, "rational_row_scales": scalars["rational_row_scales"],
                    "mixed_scalar_stage": scalar_spec, "source_old_monomials": self.tensor_sources,
                    "old_monomial_exponents_read": [0, 41], "qY_shift_applied_exactly_once": True,
                    "U_j_normalization": "H_(T^j f4)*H_f4^2, original 4/1722^3",
                    "old_U0_or_shared_monomial_coefficients_recomputed": False,
                    "coefficients_after_qY41_generated": False})
                data = self.cached(name)
            assert data["j"] == j and data["first_exponent"] == 0 and data["last_exponent_exclusive"] == ORDERS
            assert data["qY_shift_applied_exactly_once"] is True
            assert data["old_U0_or_shared_monomial_coefficients_recomputed"] is False
            rows = [[int(x) for x in row] for row in data["integer_numerators"]]
            scales = data["rational_row_scales"]
            sources = [dict(file_spec(self.path(name)), producer="R803"),
                       dict(data["mixed_scalar_stage"], producer="R803")]
        assert len(rows) == LDEG and all(len(row) == ROWS for row in rows)
        assert len(scales) == LDEG
        scale_values = [dq(value) for value in scales]
        binding = {"j": j, "original_sources": sources, "rational_row_scales": scales,
                   "coordinate_order": "qY0..41,xi0..39; columns b^0..b^6,s*b^0..s*b^6"}
        return fmpz_mat(rows).transpose(), scale_values, binding

    def modular_solver(self):
        self.short_basis()
        cached = sorted(path for path in self.out.glob("R803-prime-*-short-minor.json.gz")
                        if path.name[len("R803-prime-"):-len("-short-minor.json.gz")].isdigit())
        if cached:
            assert len(cached) == 1
            data = read(cached[0])
            assert data["complete"] is True and data["configuration"] == self.tag
            assert data["basis_index_sha256"] == self.basis_index_spec["sha256"]
        else:
            prime = self.item["auxiliary_prime_start"]
            while True:
                self.budget()
                if not fmpz(prime).is_prime():
                    prime += 2
                    continue
                rejected = self.cached("R803-prime-"+str(prime)+"-rejected-short-minor")
                if rejected is not None:
                    prime += 2
                    continue
                modular = nmod_mat([[int(self.A[i, j]) % prime for j in range(DIM)] for i in range(ROWS)], prime)
                reduced, rank = modular.transpose().rref()
                if rank != DIM:
                    self.store("R803-prime-"+str(prime)+"-rejected-short-minor",
                        {"prime": prime, "actual_rank": rank, "reason": "short integral matrix rank below694",
                         "no_characteristic_zero_rank_loss_inferred": True})
                    prime += 2
                    continue
                selected = [next(k for k in range(ROWS) if reduced[i, k]) for i in range(DIM)]
                assert selected == sorted(set(selected))
                square = nmod_mat([[int(self.A[i, j]) % prime for j in range(DIM)] for i in selected], prime)
                determinant = int(square.det())
                assert determinant
                inverse = square.inv()
                assert square*inverse == nmod_mat([[int(i == j) for j in range(DIM)] for i in range(DIM)], prime)
                name = "R803-prime-"+str(prime)+"-short-minor"
                self.store(name, {"prime": prime, "prime_proved": True,
                    "basis_index_sha256": self.basis_index_spec["sha256"], "full_rows": ROWS, "columns": DIM,
                    "coordinate_row_indices": selected, "selected_basis_column_indices": list(range(DIM)),
                    "actual_determinant_mod_prime": determinant, "inverse_mod_prime": matrix_rows(inverse),
                    "all_entries_from_original_exact_short_rows": True,
                    "characteristic_zero_basis_independence_certified": True,
                    "characteristic_zero_inverse_matrix_formed": False,
                    "modular_inverse_identity_verified": True})
                data = self.cached(name)
                break
        prime, selected = data["prime"], data["coordinate_row_indices"]
        assert data["prime_proved"] is True and data["full_rows"] == ROWS and data["columns"] == DIM
        assert data["characteristic_zero_basis_independence_certified"] is True
        assert data["modular_inverse_identity_verified"] is True
        assert data["actual_determinant_mod_prime"] % prime
        assert len(selected) == DIM and selected == sorted(set(selected))
        assert data["selected_basis_column_indices"] == list(range(DIM))
        self.minor = data
        self.prime = prime
        self.row_selection = selected
        self.inverse = nmod_mat(data["inverse_mod_prime"], prime)
        self.square = fmpz_mat([[int(self.A[i, j]) for j in range(DIM)] for i in selected])
        self.minor_spec = file_spec(self.path("R803-prime-"+str(prime)+"-short-minor"))
        return data

    def reconstruct(self, X, modulus, target):
        values = []
        for row in X:
            candidate = []
            for value in row:
                rational = rational_reconstruct(value, modulus)
                if rational is None:
                    return None
                candidate.append(rational)
            values.append(candidate)
        denominators = []
        for column in range(LDEG):
            denominator = 1
            for row in values:
                denominator = math.lcm(denominator, int(row[column].denom()))
            denominators.append(denominator)
        numerators = fmpz_mat([
            [int(value.numer())*(denominators[j]//int(value.denom())) for j, value in enumerate(row)]
            for row in values])
        actual = self.A*numerators
        for i in range(ROWS):
            for j in range(LDEG):
                if actual[i, j] != target[i, j]*denominators[j]:
                    return None
        return values, denominators

    def solve_rhs(self, j):
        name = "R803-exact-original-M6-coordinates-j"+str(j)
        old = self.cached(name)
        if old is not None:
            assert old["j"] == j and old["all1680_original_coordinates_verified"] is True
            assert old["basis_integer_scale"] == str(LEVEL**6)
            assert old["actual_prime"] == self.prime and old["minor_stage"] == self.minor_spec
            # A hard interruption can occur after the exact result is atomically
            # saved but before its now-obsolete current lift is removed.
            self.path("R803-prime-"+str(self.prime)+"-j"+str(j)+"-dixon-current").unlink(missing_ok=True)
            return file_spec(self.path(name))
        target, scales, binding = self.rhs(j)
        assert target.nrows() == ROWS and target.ncols() == LDEG
        binding_hash = fingerprint(binding)
        ni = [[int(target[i, j]) for j in range(LDEG)] for i in self.row_selection]
        prefix = "R803-prime-"+str(self.prime)+"-j"+str(j)+"-dixon-current"
        current = self.cached(prefix)
        if current is None:
            X, residual, digits, modulus = [[0]*LDEG for _ in range(DIM)], ni, 0, 1
            previous_sha = None
        else:
            assert current["j"] == j and current["prime"] == self.prime
            assert current["rhs_binding_sha256"] == binding_hash
            assert current["minor_stage_sha256"] == self.minor_spec["sha256"]
            digits, modulus = current["digits"], int(current["modulus"])
            assert digits >= 1 and modulus == self.prime**digits
            X = [[int(x) for x in row] for row in current["lifted_integer_coordinates"]]
            residual = [[int(x) for x in row] for row in current["exact_divided_residual"]]
            assert len(X) == len(residual) == DIM and all(len(row) == LDEG for row in X+residual)
            assert all(0 <= value < modulus for row in X for value in row)
            actual = self.square*fmpz_mat(X)
            assert all(actual[i, k]+modulus*residual[i][k] == ni[i][k]
                       for i in range(DIM) for k in range(LDEG)), "Retained exact Dixon invariant failed."
            previous_sha = sha(self.path(prefix))
        while True:
            self.budget()
            if digits and (digits == 1 or digits % self.item["reconstruct_every_digits"] == 0):
                recovered = self.reconstruct(X, modulus, target)
                if recovered is not None:
                    values, denominators = recovered
                    coordinates = [[pairs(value*scales[k]) for k, value in enumerate(row)] for row in values]
                    unscaled = [[pairs(value*scales[k]*LEVEL**6) for k, value in enumerate(row)] for row in values]
                    self.store(name, {"j": j, "U_j": "H_f4^3" if j == 0 else "H_(T^"+str(j)+" f4)*H_f4^2",
                        "basis_dimension": DIM, "basis_integer_scale": str(LEVEL**6),
                        "original_M6_basis_index": self.basis_index_spec,
                        "coefficient_field_basis": self.tag["coordinate_basis"],
                        "coefficients_in_integer_scaled_original_M6_basis": coordinates,
                        "coefficients_in_unscaled_original_M6_basis": unscaled,
                        "coordinate_equations": "U_j=sum X_i*(82^6 F_i)=sum (82^6 X_i)*F_i",
                        "source_rhs": binding, "source_rhs_binding_sha256": binding_hash,
                        "primitive_solution_column_denominators": [str(value) for value in denominators],
                        "actual_prime": self.prime, "actual_Dixon_digits": digits,
                        "actual_reconstruction_modulus": str(modulus),
                        "minor_stage": self.minor_spec,
                        "all1680_original_coordinates_verified": True,
                        "verification": "A_full*cleared_exact_numerators = primitive_rhs*column_denominators; original row scales restored",
                        "rational_reconstruction_used_uniform_strict_rectangular_bound": True,
                        "old_U0_recomputed": False, "characteristic_zero_inverse_matrix_formed": False})
                    self.path(prefix).unlink(missing_ok=True)
                    print(json.dumps({"stage": "exact_original_M6_coordinates", "j": j,
                        "digits": digits, "modulus_bits": modulus.bit_length(),
                        "full_coordinate_rows_verified": ROWS, "seconds": time.monotonic()-self.started}), flush=True)
                    return file_spec(self.path(name))
            reduced_rhs = nmod_mat([[value % self.prime for value in row] for row in residual], self.prime)
            correction = self.inverse*reduced_rhs
            delta = matrix_rows(correction)
            if digits == 0:
                # This catches a wrong original basis/phase/scale before an expensive lift.
                whole = nmod_mat([[int(self.A[i, k]) % self.prime for k in range(DIM)]
                                 for i in range(ROWS)], self.prime)*correction
                assert all(int(whole[i, k]) == int(target[i, k]) % self.prime
                           for i in range(ROWS) for k in range(LDEG)), "Original full short RHS is outside the selected M6 span."
            product = self.square*fmpz_mat(delta)
            new_residual = []
            for i in range(DIM):
                row = []
                for k in range(LDEG):
                    numerator = residual[i][k]-int(product[i, k])
                    assert numerator % self.prime == 0, "Dixon correction does not cancel the actual residual."
                    row.append(numerator//self.prime)
                    X[i][k] += modulus*delta[i][k]
                new_residual.append(row)
            residual = new_residual
            modulus *= self.prime
            digits += 1
            self.store(prefix, {"j": j, "prime": self.prime, "digits": digits, "modulus": str(modulus),
                "rhs_binding_sha256": binding_hash, "minor_stage_sha256": self.minor_spec["sha256"],
                "lifted_integer_coordinates": [[str(x) for x in row] for row in X],
                "exact_divided_residual": [[str(x) for x in row] for row in residual],
                "previous_checkpoint_sha256": previous_sha,
                "invariant": "A_I X + prime^digits residual = primitive_rhs_I",
                "complete_coordinates_claimed": False, "only_current_full_lift_vector_retained": True})
            previous_sha = sha(self.path(prefix))
            if digits == 1 or digits % self.item["reconstruct_every_digits"] == 0:
                print(json.dumps({"stage": "Dixon_current_exact_rhs", "j": j, "digits": digits,
                    "modulus_bits": modulus.bit_length(), "seconds": time.monotonic()-self.started}), flush=True)

    def run(self):
        final = self.out/FINAL
        if final.exists():
            cert = read(final)
            assert cert["result"] == RESULT and cert["complete"] is True and cert["configuration"] == self.tag
            manifest = cert["stage_manifest"]
            assert file_spec(self.out/manifest["file"]) == manifest
            for row in read(self.out/manifest["file"])["files"]:
                assert file_spec(self.out/row["file"]) == row
        else:
            self.short_basis()
            # New mixed inputs are persisted independently of the finite RHS solves.
            for j in range(1, 6):
                self.rhs(j)
            self.modular_solver()
            solutions = {str(j): self.solve_rhs(j) for j in range(6)}
            ratio_spec = self.store("R803-original-mixed-Hodge-ratio-interface", {
                "reference_map": "original R759 f4", "denominator_coordinate_index": 0,
                "numerator_coordinate_indices": [1, 2, 3, 4, 5],
                "ratio_equation": "U_j/U_0 = (T^j f4)^*omega_C / f4^*omega_C",
                "original_M6_basis_index": self.basis_index_spec, "coordinate_stages": solutions,
                "common_original_target_model": "C:y^2=x^3+b",
                "coordinate_basis": self.tag["coordinate_basis"],
                "U0_nonzero_from_original_R774_certificate": True,
                "old_Hom_cyclic_columns_reused": self.r794.source(MODULE),
                "selected_integral_cyclic_expressions_source": self.r794.source(SELECTED),
                "all_six_exact_forms_identified_by_full42_term_injective_prefix": True,
                "five_original_mixed_differential_ratios_computed": True,
                "actual_original_y_functions_polar_divisors_beta_eta_or_height_computed": False})
            files = [file_spec(path) for path in sorted(self.out.glob("R803-*.json.gz"))
                     if path.name != "R803-stage-manifest.json.gz"]
            manifest = self.store("R803-stage-manifest", {"files": files})
            cert = {"result": RESULT, "complete": True, "p": P, "configuration": self.tag,
                "M6_dimension": DIM, "qY_count": ORDERS, "xi_coordinate_count": CYC,
                "full_original_coordinate_rows": ROWS, "basis_integer_scale": str(LEVEL**6),
                "new_basis_row_indices": [690, 691, 692, 693], "old_ordinary_power3_rows_reused": 690,
                "new_mixed_Hodge_products": [1, 2, 3, 4, 5], "exact_coordinate_groups": [0, 1, 2, 3, 4, 5],
                "actual_nonzero_short_minor": {
                    "prime": self.prime, "rows": DIM, "columns": DIM,
                    "coordinate_row_indices": self.row_selection,
                    "determinant_mod_prime": self.minor["actual_determinant_mod_prime"]},
                "basis_index": self.basis_index_spec, "coordinate_stages": solutions,
                "ratio_interface": ratio_spec, "stage_manifest": manifest,
                "all84_rational_RHS_columns_verified_in_all1680_original_rows": True,
                "all_original_1722_and_82power6_scales_preserved": True,
                "original_b_and_s_coordinate_basis_preserved": True,
                "five_original_mixed_differential_ratios_computed": True,
                "old_U0_Hodge_monomials_Hom_periods_or_ordinary_basis_recomputed": False,
                "characteristic_zero_inverse_matrix_formed": False,
                "actual_original_y_functions_polar_divisors_beta_eta_or_height_computed": False,
                "seconds": time.monotonic()-self.started}
            save(final, cert)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(final),
            "M6_dimension": DIM, "qY_count": ORDERS, "full_original_coordinate_rows": ROWS,
            "five_original_mixed_differential_ratios_computed": True,
            "actual_original_y_functions_polar_divisors_beta_eta_or_height_computed": False})
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
            "completed_source_bound_stages_and_current_exact_RHS_lifts_preserved": True})
        raise


if __name__ == "__main__":
    sys.exit(main())
