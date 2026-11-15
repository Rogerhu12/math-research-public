#!/usr/bin/env python3
"""R809: source-bound S5 normal coordinates, incrementally requested actual targets."""
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

RESULT = "R809-original-S5-normal-coordinates"
FINAL = "p41-original-S5-normal-coordinate-certificate.json"
P, LEVEL, CYC, REAL, COUNT = 41, 82, 40, 20, 69
DIM, ROWS, FREE, LDEG = 1234, 1380, 272, 14
DIMS = {1: 146, 2: 418, 3: 690, 4: 962, 5: 1234}
EPS = [0]+[1]*144+[2]*127
REQUIRED = {"R805", "R786", "R803", "R807"}
TARGETS = ["C"+str(j) for j in range(6)]+["A", "B"]
FIELD_BASIS = "b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b"
R805_CORE_SHA = "730a7d8f51d76d1153386c63f2e082285ada4573a2baf8d87d1825d3ce75b420"
R805_PROOF_SHA = "b48d9f8dd5d8d1a89aa2574ab7f9ee014b83ca21baf41694252b9c53993571e8"
R803_CORE_SHA = "1233536f55fdcddad3fe1c48396fb32bcdee787a3f2df5d193f1b9472d4b1531"
R807_CORE_SHA = "d92cf79bb3a30fe8e28709a4e2eaa706a724e195c8d8393e7649466a79cec018"
M6_RECIPES = {
    690: {"factor": "E4", "index": 0, "kind": "elliptic_layer_product", "power": 1},
    691: {"factor": "E4", "index": 73, "kind": "elliptic_layer_product", "power": 1},
    692: {"kind": "level_one", "name": "E6"},
    693: {"kind": "level_one", "name": "eta12"},
}


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
        width = 6-eps
        if index < offset+width:
            return a, index-offset
        offset += width
    raise AssertionError("S5 index outside original graded free basis")


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


def band_rectangles(a, b, c, d, first, stop):
    if a >= b or c >= d or b+d-2 < first or a+c >= stop:
        return
    if a+c >= first and b+d-2 < stop:
        yield a, b, c, d
        return
    if b-a >= d-c:
        middle = (a+b)//2
        yield from band_rectangles(a, middle, c, d, first, stop)
        yield from band_rectangles(middle, b, c, d, first, stop)
    else:
        middle = (c+d)//2
        yield from band_rectangles(a, b, c, middle, first, stop)
        yield from band_rectangles(a, b, middle, d, first, stop)


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
        assert self.item["R809_proof_sha256"] == sha(args.proof)
        assert self.item["R809_method_sha256"] == sha(args.method)
        assert flint.__version__ == "0.9.0"
        assert self.item["qY_count"] == COUNT
        assert self.item["auxiliary_prime_start"] == 1000000007
        assert self.item["dixon_group_columns"] == 7
        assert self.item["reconstruct_every_digits"] == 8
        labels = set(self.item["retained_artifacts"])
        assert REQUIRED <= labels <= REQUIRED | {"R787"}
        self.requested = self.item["requested_target_groups"]
        assert self.requested and len(self.requested) == len(set(self.requested))
        assert all(name in TARGETS for name in self.requested)
        assert not set(self.requested) & {"A", "B"} or "R787" in labels
        self.inputs = {label: Retained(args.retained, label, self.item["retained_artifacts"][label])
                       for label in sorted(labels)}
        for producer in self.inputs.values():
            producer.load_inventory()
        self.r805, self.r786 = self.inputs["R805"], self.inputs["R786"]
        self.r803, self.r807 = self.inputs["R803"], self.inputs["R807"]
        self.r787 = self.inputs.get("R787")
        assert self.r805.spec["result"] == "R805-original-affine-pencil-free-basis"
        assert self.r805.spec["core_sha256"] == R805_CORE_SHA
        assert self.r803.spec["result"] == "R803-original-M6-mixed-Hodge-ratios"
        assert self.r803.spec["core_sha256"] == R803_CORE_SHA
        assert self.r807.spec["result"] == "R807-original-M6-pole-clearing"
        assert self.r807.spec["core_sha256"] == R807_CORE_SHA
        for producer in (self.r805, self.r803, self.r807):
            same_producer(producer.tag["retained_artifacts"]["R786"], self.r786.spec)
        same_producer(self.r807.tag["retained_artifacts"]["R805"], self.r805.spec)
        assert self.r805.tag["R805_proof_sha256"] == R805_PROOF_SHA
        assert self.r807.tag["R805_proof_sha256"] == R805_PROOF_SHA
        cert = self.r805.certificate
        assert cert["completed_scope"] == "pencil_and_graded_free_basis"
        assert cert["affine_free_module_rank"] == FREE
        assert cert["graded_free_basis_degrees"] == [1, 144, 127]
        assert cert["all_S_rows_original_and_real_coordinates_verified"] is True
        assert cert["original_82_scales_preserved"] is True
        self.pencil = self.r805.indexed(cert["pencil_stage"])
        self.free = self.r805.indexed(cert["graded_free_basis_stage"])
        self.alias805 = self.r805.indexed(cert["alias_index"])
        self.S3index = self.r805.indexed(cert["S_basis_index"])
        assert self.pencil["actual_rank"] == 690
        assert self.pencil["basepoint_free_certified_by_actual_unit_minor"] is True
        self.n = int(self.pencil["n"])
        assert self.free["pencil_stage"] == cert["pencil_stage"]
        assert self.free["degree_distribution"] == [1, 144, 127]
        assert self.free["degree1_original_indices"] == list(range(2, 146))
        self.free2 = self.free["degree2_original_indices"]
        assert len(self.free2) == 127 and self.free2 == sorted(set(self.free2))
        assert all(0 <= i < DIMS[2] for i in self.free2)
        assert self.r786.certificate["exact_K_basis_prefix_bound_qY"] == 128
        assert self.r786.certificate["basis_in_original_R775_saved_order"] is True
        cert803, cert807 = self.r803.certificate, self.r807.certificate
        assert cert803["M6_dimension"] == 694 and cert803["qY_count"] == 42
        assert cert803["all84_rational_RHS_columns_verified_in_all1680_original_rows"] is True
        assert cert803["all_original_1722_and_82power6_scales_preserved"] is True
        assert cert803["original_b_and_s_coordinate_basis_preserved"] is True
        self.M6index = self.r803.indexed(cert803["basis_index"])
        self.U_specs = cert803["coordinate_stages"]
        assert set(self.U_specs) == {str(j) for j in range(6)}
        assert cert807["actual_nonzero_theta_constructed"] is True
        assert cert807["actual_M6_pole_clearing_computed"] is True
        assert cert807["all_four_M6_products_verified_in_all1100_rows"] is True
        assert cert807["global_degree1092_vs_cusp_order1100_bound_used"] is True
        self.theta = self.r807.indexed(cert807["theta_stage"])
        self.cleared_index = self.r807.indexed(cert807["cleared_coordinate_index"])
        assert self.cleared_index["all_four_members_verified_in_all1100_real_coordinates"] is True
        assert self.cleared_index["theta_stage"] == cert807["theta_stage"]
        assert plain_spec(self.cleared_index["source_original_M6"]) == \
               plain_spec(self.M6index["original_M6_stage"])
        assert self.cleared_index["four_original_M6_recipes"] == {str(k): v for k, v in M6_RECIPES.items()}
        for key, spec in cert807["cleared_coordinate_stages"].items():
            assert key in {"690", "691", "692", "693"}
            data = self.r807.indexed(spec)
            assert data["all1100_rows_verified"] is True
        assert set(cert807["cleared_coordinate_stages"]) == {"690", "691", "692", "693"}
        assert self.theta["source_original_M2_indices"] == list(range(5))
        assert self.theta["original_M2_integer_scale"] == str(LEVEL**2)
        assert self.theta["theta_nonzero_by_original_independent_M2_input"] is True
        assert self.theta["theta_at_P0_and_P1_has_two_zeros_by_original_E6_principal_parts"] is True
        self.lambdas = [dq(pair) for pair in self.theta["lambda"]]
        assert len(self.lambdas) == 5 and any(self.lambdas)
        first = next(i for i, value in enumerate(self.lambdas) if value)
        assert self.theta["first_nonzero_lambda_index"] == first and self.lambdas[first] == 1
        assert self.theta["theta_in_original_integer_scaled_M2_basis"] == \
            self.theta["lambda"]+[["0", "1"] for _ in range(141)]
        model_name = "R803-mixed-original-Hodge-scalars-j1.json.gz"
        assert model_name in self.r803.inventory
        self.model_spec = self.r803.source(model_name)
        self.model = self.r803.indexed(self.model_spec)["original_b_model"]
        self.extra_sources = {}
        for index in range(690, 694):
            name = "R803-new-original-M6-short-row-"+str(index)+".json.gz"
            assert name in self.r803.inventory
            self.extra_sources[index] = self.r803.source(name)
        self.tail807 = {}
        for spec in cert807["actual_new_pair_tail_stages"]:
            data = self.r807.indexed(spec)
            pair = tuple(data["sorted_M2_leaf_indices"])
            assert pair in {(3, 73), (4, 73)} and pair not in self.tail807
            assert data["first_exponent"] == 41 and data["last_exponent_exclusive"] == 55
            assert data["integer_scale"] == str(LEVEL**4)
            assert data["only_new_sum_band_convolved"] is True
            assert data["old_R805_q0_through40_recomputed"] is False
            self.tail807[pair] = spec
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "R809_proof_sha256": sha(args.proof), "R809_method_sha256": sha(args.method),
            "p": P, "qY_count": COUNT, "real_coordinate_count": REAL, "full_coordinate_rows": ROWS,
            "S_basis_dimension": DIM, "normal_affine_basis_rank": FREE, "normal_basis_degrees": EPS,
            "basis_integer_scale": str(LEVEL**10), "original_tau_index": 0,
            "actual_sigma_integer_n": self.n,
            "basis_producers": {label: producer_identity(self.inputs[label].spec)
                                for label in ("R805", "R786", "R807")},
            "original_pencil": cert["pencil_stage"], "original_graded_free_basis": cert["graded_free_basis_stage"],
            "original_alias_index": cert["alias_index"],
            "actual_R807_available_pair_tails": cert807["actual_new_pair_tail_stages"],
            "S_basis_order": "a=0..271 outer; j=0..5-eps_a inner",
            "coefficient_field_basis": FIELD_BASIS,
            "auxiliary_prime_start": self.item["auxiliary_prime_start"],
            "dixon_group_columns": self.item["dixon_group_columns"],
            "reconstruct_every_digits": self.item["reconstruct_every_digits"],
            "old_R805_ranks_or_original_R786_prefixes_recomputed": False,
            "requested_targets_budget_and_future_R787_excluded_from_basis_identity": True,
        }
        self.tag_hash = fingerprint(self.tag)
        self.sources, self.recipes, self.leaves, self.aliases = {}, {}, {}, {}
        self.old_products = {}
        self.old_cache, self.product_cache = OrderedDict(), OrderedDict()
        self.C = self.square = self.inverse = self.M6matrix = None
        self.matrix_spec = self.minor_spec = self.inverse_spec = self.M6_spec = None
        self.factor_data = self.relation = None
        self.target_tags = {}
        T = fmpz_poly([0, 1])
        self.chebyshev = [fmpz_poly([2]), T]
        for _ in range(2, 21):
            self.chebyshev.append(T*self.chebyshev[-1]-self.chebyshev[-2])
        self.gt = fmpz_poly([1])
        for poly in self.chebyshev[1:]:
            self.gt += poly
        self.load_aliases()
        self.free_leaves = [()]+[(i,) for i in range(2, 146)]+[self.leaves[2, i] for i in self.free2]
        assert len(self.free_leaves) == FREE
        if self.r787 is not None:
            self.load_relation()

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes-45:
            raise BudgetStop("Complete source-bound rows, targets, coordinates and latest exact lifts retained.")

    def path(self, name):
        assert name.startswith("R809-") and Path(name).name == name
        return self.out/(name if name.endswith(".json.gz") else name+".json.gz")

    def target_tag(self, target):
        if target not in self.target_tags:
            assert target in TARGETS
            tag = {"basis_configuration_sha256": self.tag_hash, "target": target,
                   "coefficient_field_basis": FIELD_BASIS,
                   "original_b_model": self.model, "original_b_model_source": self.model_spec}
            if target.startswith("C"):
                j = int(target[1:])
                tag.update({
                    "target_producers": {label: producer_identity(self.inputs[label].spec)
                                         for label in ("R803", "R807")},
                    "original_Uj_coordinates": self.U_specs[str(j)],
                    "original_theta": self.r807.certificate["theta_stage"],
                    "original_full_M6_clearing": self.r807.certificate["cleared_coordinate_index"],
                    "original_four_member_certificates": self.r807.certificate["cleared_coordinate_stages"],
                    "original_M6_extra_prefixes": {str(i): spec for i, spec in self.extra_sources.items()},
                    "homogeneous_target": "tau*theta*U_"+str(j),
                    "normal_function": "theta*U_"+str(j)+"/tau^4",
                    "regular_degree_bound": 4, "literal_tau_factor_highest_S5_terms_zero": True,
                })
            else:
                assert self.r787 is not None and self.relation is not None
                tag.update({"target_producers": {"R787": producer_identity(self.r787.spec)},
                    "original_function_recipe": self.r787.certificate["relation_spec"],
                    "original_field_lambda": self.relation["field"]["lambda"],
                    "original_R786_basis_index": self.relation["R786_basis_index"],
                    "homogeneous_target": target, "normal_function": target+"/tau^5",
                    "regular_degree_bound": 5,
                    "common_R787_denominator_or_content_reinserted": False,
                    "Bfield_to_b_column_factor": "lambda^(column mod7), same two s blocks"})
            self.target_tags[target] = tag
        return self.target_tags[target]

    def cached(self, name, target=None, current=False):
        path = self.path(name)
        if not path.exists():
            return None
        data = read(path)
        assert data["configuration"] == self.tag and data["complete"] is (not current)
        if target is not None:
            assert data["target_configuration"] == self.target_tag(target)
            assert data["target_configuration_sha256"] == fingerprint(self.target_tag(target))
        else:
            assert "target_configuration" not in data
        if current:
            assert name.endswith("-dixon-current") and data["complete_coordinates_claimed"] is False
        return data

    def store(self, name, value, target=None, current=False):
        assert not current or name.endswith("-dixon-current")
        payload = dict(value, complete=not current, configuration=self.tag)
        if target is not None:
            payload["target_configuration"] = self.target_tag(target)
            payload["target_configuration_sha256"] = fingerprint(self.target_tag(target))
        save(self.path(name), payload)
        return file_spec(self.path(name))

    def old_name(self, power, index):
        return "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"

    def load_aliases(self):
        name = "R809-original-degree1-through5-alias-index"
        old = self.cached(name)
        if old is None:
            prior = {(row["power"], row["index"]): row for row in self.alias805["rows"]}
            assert len(prior) == 1254
            rows = []
            for power in DIMS:
                for index in range(DIMS[power]):
                    self.budget()
                    old_name = self.old_name(power, index)
                    source = self.r786.source(old_name)
                    assert plain_spec(source) == self.r786.inventory[old_name]
                    if (power, index) in prior:
                        row = prior[power, index]
                        assert row["source"] == source
                        recipe, leaves = row["recipe"], tuple(row["sorted_M2_leaf_indices"])
                    else:
                        data = self.r786.indexed(source)
                        assert data["weight"] == 2*power and data["bound_qY"] == 128
                        assert data["integer_scale"] == str(LEVEL**(2*power))
                        assert data["original_R775_finite_coefficients_verified"] is True
                        recipe = data["recipe"]
                        lp, li, rp, ri = (recipe[k] for k in
                            ("left_power", "left_index", "right_power", "right_index"))
                        assert recipe["kind"] == "product" and lp+rp == power and lp < power and rp < power
                        leaves = tuple(sorted(self.leaves[lp, li]+self.leaves[rp, ri]))
                    if power == 1:
                        assert leaves == (index,) and recipe["kind"] == "det_semilinear_E1_pair_trace"
                    else:
                        lp, li, rp, ri = (recipe[k] for k in
                            ("left_power", "left_index", "right_power", "right_index"))
                        assert recipe["kind"] == "product" and lp+rp == power
                        assert leaves == tuple(sorted(self.leaves[lp, li]+self.leaves[rp, ri]))
                    self.leaves[power, index] = leaves
                    rows.append({"power": power, "index": index, "recipe": recipe,
                                 "sorted_M2_leaf_indices": list(leaves), "source": source})
            self.store(name, {"source_powers": list(DIMS), "rows": rows,
                "source_R805_alias_index": self.r805.certificate["alias_index"],
                "only_original_recipes_read_no_old_mathematics_recomputed": True})
            old = self.cached(name)
        assert old["source_powers"] == list(DIMS) and len(old["rows"]) == sum(DIMS.values())
        for row in old["rows"]:
            power, index = row["power"], row["index"]
            assert power in DIMS and 0 <= index < DIMS[power]
            source = self.r786.source(self.old_name(power, index))
            assert row["source"] == source
            assert plain_spec(source) == self.r786.inventory[source["file"]]
            leaves = tuple(row["sorted_M2_leaf_indices"])
            assert len(leaves) == power and leaves == tuple(sorted(leaves))
            recipe = row["recipe"]
            if power == 1:
                assert leaves == (index,)
            else:
                lp, li, rp, ri = (recipe[k] for k in
                    ("left_power", "left_index", "right_power", "right_index"))
                assert leaves == tuple(sorted(self.leaves[lp, li]+self.leaves[rp, ri]))
            self.leaves[power, index] = leaves
            self.sources[power, index], self.recipes[power, index] = source, recipe
            self.aliases.setdefault(leaves, (power, index))
        assert set(self.sources) == {(r, i) for r in DIMS for i in range(DIMS[r])}
        self.alias_spec = file_spec(self.path(name))
        for filename, spec in self.r805.inventory.items():
            prefix, suffix = "R805-new-monomial-", ".json.gz"
            if filename.startswith(prefix) and filename.endswith(suffix):
                leaves = tuple(int(x) for x in filename[len(prefix):-len(suffix)].split("-"))
                assert 2 <= len(leaves) <= 3 and leaves == tuple(sorted(leaves))
                self.old_products[leaves] = spec

    def load_relation(self):
        cert = self.r787.certificate
        assert cert["result"] == "R787-original-power5-function-relation"
        assert cert["actual_y_map_recovered"] is True
        assert cert["exact_nonzero_A_B_relation_verified"] is True
        assert cert["original_map_index"] == 4 and cert["original_map_degree"] == "1206"
        assert cert["exact_verified_orders"] == 129
        assert cert["exact_verified_Laurent_exponents"] == [-1, 127]
        same_producer(self.r787.tag["retained_artifacts"]["R786"], self.r786.spec)
        data = self.r787.indexed(cert["relation_spec"])
        assert data["original_R786_basis_order"] is True
        assert data["basis_integer_scale"] == str(LEVEL**10)
        assert data["L_basis"] == "B^i*s^j, j=0..1 outer, i=0..6; B=lambda*b"
        assert data["candidate_only_until_full_exact_verification"] is False
        assert data["exact_original_A_equals_yB"] is True and data["B_nonzero"] is True
        assert data["full_129_original_relations_verified"] is True
        assert data["field"]["original_b_replaced_by_another_twist"] is False
        assert data["field"]["original_b_minimal_polynomial"] == self.model
        assert int(data["field"]["lambda"]) > 0
        for target in ("A", "B"):
            rows = data[target+"_integer_L_coordinates"]
            assert len(rows) == DIM and all(len(row) == LDEG for row in rows)
        assert any(int(x) for row in data["B_integer_L_coordinates"] for x in row)
        self.relation = data

    @staticmethod
    def remember(cache, key, value, maximum=40):
        cache[key] = value
        cache.move_to_end(key)
        while len(cache) > maximum:
            cache.popitem(last=False)
        return value

    def real_rows(self, rows, first=0):
        answer = []
        for offset, row in enumerate(rows):
            n = first+offset
            cyclic = [0]*P
            for r, value in enumerate(row):
                cyclic[(r+10*n) % P] += int(value)
            reduced = [value-cyclic[40] for value in cyclic[:40]]+[0]
            assert all(reduced[r] == reduced[P-r] for r in range(1, 21))
            poly = fmpz_poly([reduced[0]])
            for r in range(1, 21):
                poly += self.chebyshev[r]*reduced[r]
            poly %= self.gt
            answer.append([int(poly[r]) for r in range(REAL)])
        return answer

    def original(self, power, index):
        key = power, index
        if key in self.old_cache:
            self.old_cache.move_to_end(key)
            return self.old_cache[key]
        source = self.sources[key]
        data = self.r786.indexed(source)
        assert data["weight"] == 2*power and data["bound_qY"] == 128
        assert data["integer_scale"] == str(LEVEL**(2*power))
        assert data["recipe"] == self.recipes[key]
        assert data["original_R775_finite_coefficients_verified"] is True
        rows = data["integer_qY_xi_coefficients"]
        assert len(rows) == 129 and all(len(row) == CYC for row in rows)
        raw = [[int(value) for value in row] for row in rows[:COUNT]]
        answer = {"q": raw, "v": self.real_rows(raw), "source_chain": [source],
                  "leaves": self.leaves[key], "integer_scale": str(LEVEL**(2*power))}
        return self.remember(self.old_cache, key, answer)

    def product_band(self, left, right, first, stop):
        assert 0 <= first < stop <= COUNT
        assert len(left["q"]) >= stop and len(right["q"]) >= stop
        rectangles = list(band_rectangles(0, stop, 0, stop, first, stop))
        accumulators = {}
        for key, stride in (("q", 79), ("v", 39)):
            acc = [0]*(stride*(stop-first))
            for a, b, c, d in rectangles:
                self.budget()
                assert a+c >= first and b+d-2 < stop
                value = packed(left[key][a:b], stride).mul_low(
                    packed(right[key][c:d], stride), stride*(stop-a-c))
                shift = stride*(a+c-first)
                assert shift >= 0
                for k in range(value.degree()+1):
                    assert shift+k < len(acc)
                    acc[shift+k] += int(value[k])
            accumulators[key] = acc
        raw, direct = [], []
        for n in range(stop-first):
            cyclic = [0]*P
            for r in range(79):
                cyclic[r % P] += accumulators["q"][79*n+r]
            raw.append([cyclic[r]-cyclic[40] for r in range(CYC)])
            polynomial = fmpz_poly(accumulators["v"][39*n:39*(n+1)]) % self.gt
            direct.append([int(polynomial[r]) for r in range(REAL)])
        real = self.real_rows(raw, first)
        assert real == direct
        return raw, real, rectangles

    def product_factors(self, leaves):
        if len(leaves) == 2:
            return self.monomial(leaves[:1]), self.monomial(leaves[1:])
        if len(leaves) == 3:
            pair = next((tuple(sorted(pair)) for pair in itertools.combinations(leaves, 2)
                         if tuple(sorted(pair)) in self.aliases),
                        next((tuple(sorted(pair)) for pair in itertools.combinations(leaves, 2)
                              if tuple(sorted(pair)) in self.old_products), None))
            assert pair is not None, ("missing original completed pair", leaves)
            remaining = list(leaves)
            for i in pair:
                remaining.remove(i)
            return self.monomial(pair), self.monomial(tuple(remaining))
        assert len(leaves) == 5
        candidates = []
        for triple in sorted(set(itertools.combinations(leaves, 3))):
            remaining = list(leaves)
            for i in triple:
                remaining.remove(i)
            pair = tuple(remaining)
            if (triple in self.aliases or triple in self.old_products) and \
               (pair in self.aliases or pair in self.old_products):
                score = int(triple not in self.aliases)+int(pair not in self.aliases)
                candidates.append((score, triple, pair))
        assert candidates, ("S5 term lacks an actual completed 3+2 recipe", leaves)
        _, triple, pair = min(candidates)
        return self.monomial(triple), self.monomial(pair)

    def monomial(self, leaves):
        leaves = tuple(sorted(leaves))
        assert len(leaves) in (1, 2, 3, 5)
        if leaves in self.product_cache:
            self.product_cache.move_to_end(leaves)
            return self.product_cache[leaves]
        if leaves in self.aliases:
            return self.remember(self.product_cache, leaves, self.original(*self.aliases[leaves]))
        word = "-".join(str(i).zfill(3) for i in leaves)
        scale = str(LEVEL**(2*len(leaves)))
        if len(leaves) < 5:
            assert leaves in self.old_products, ("missing completed R805 prefix", leaves)
            spec805 = self.old_products[leaves]
            old = self.r805.indexed(spec805)
            assert old["sorted_M2_leaf_indices"] == list(leaves)
            assert old["qY_count"] == 41 and old["integer_scale"] == scale
            assert old["all_original_and_real_coordinates_verified"] is True
            assert old["old_recipe_alias_exists"] is False
            raw = [[int(x) for x in row] for row in old["integer_qY_xi_coefficients"]]
            real = [[int(x) for x in row] for row in old["integer_v_t_coefficients"]]
            assert len(raw) == len(real) == 41 and self.real_rows(raw) == real
            sources = [self.r805.source(spec805["file"])]
            first = 41
            if leaves in self.tail807:
                spec807 = self.tail807[leaves]
                prior = self.r807.indexed(spec807)
                assert prior["source_completed_R805_prefix"] == sources[0]
                qtail = [[int(x) for x in row] for row in prior["integer_qY_xi_coefficients"]]
                vtail = [[int(x) for x in row] for row in prior["integer_v_t_coefficients"]]
                assert len(qtail) == len(vtail) == 14 and self.real_rows(qtail, 41) == vtail
                raw.extend(qtail)
                real.extend(vtail)
                sources.append(self.r807.source(spec807["file"]))
                first = 55
            name = "R809-monomial-tail-"+word+"-"+str(first).zfill(4)+"-0069"
            data = self.cached(name)
            if data is None:
                left, right = self.product_factors(leaves)
                qtail, vtail, rectangles = self.product_band(left, right, first, COUNT)
                self.store(name, {
                    "sorted_M2_leaf_indices": list(leaves), "weight": 2*len(leaves),
                    "integer_scale": scale, "first_exponent": first, "last_exponent_exclusive": COUNT,
                    "completed_prefix_source_chain": sources,
                    "factor_source_chains": [left["source_chain"], right["source_chain"]],
                    "integer_qY_xi_coefficients": [[str(x) for x in row] for row in qtail],
                    "integer_v_t_coefficients": [[str(x) for x in row] for row in vtail],
                    "convolution_rectangles": [list(box) for box in rectangles],
                    "only_new_sum_band_convolved": True,
                    "all_original_and_real_coordinates_verified": True,
                    "old_saved_prefix_recomputed": False, "old_recipe_alias_exists": False,
                })
                data = self.cached(name)
            assert data["sorted_M2_leaf_indices"] == list(leaves)
            assert data["completed_prefix_source_chain"] == sources
            assert data["first_exponent"] == first and data["last_exponent_exclusive"] == COUNT
            assert data["integer_scale"] == scale and data["only_new_sum_band_convolved"] is True
            assert data["all_original_and_real_coordinates_verified"] is True
            raw.extend([[int(x) for x in row] for row in data["integer_qY_xi_coefficients"]])
            real.extend([[int(x) for x in row] for row in data["integer_v_t_coefficients"]])
            sources.append(dict(file_spec(self.path(name)), producer="R809"))
        else:
            name = "R809-new-degree5-monomial-"+word
            data = self.cached(name)
            if data is None:
                left, right = self.product_factors(leaves)
                raw, real, rectangles = self.product_band(left, right, 0, COUNT)
                self.store(name, {
                    "sorted_M2_leaf_indices": list(leaves), "weight": 10,
                    "integer_scale": scale, "qY_count": COUNT,
                    "integer_qY_xi_coefficients": [[str(x) for x in row] for row in raw],
                    "integer_v_t_coefficients": [[str(x) for x in row] for row in real],
                    "factor_source_chains": [left["source_chain"], right["source_chain"]],
                    "factorization_degrees": [len(left["leaves"]), len(right["leaves"])],
                    "all_original_and_real_coordinates_verified": True,
                    "old_recipe_alias_exists": False, "old_saved_product_recomputed": False,
                })
                data = self.cached(name)
            assert data["sorted_M2_leaf_indices"] == list(leaves)
            assert data["qY_count"] == COUNT and data["integer_scale"] == scale
            assert data["all_original_and_real_coordinates_verified"] is True
            assert data["old_recipe_alias_exists"] is False
            raw = [[int(x) for x in row] for row in data["integer_qY_xi_coefficients"]]
            real = [[int(x) for x in row] for row in data["integer_v_t_coefficients"]]
            sources = [dict(file_spec(self.path(name)), producer="R809")]
        assert len(raw) == len(real) == COUNT
        assert all(len(row) == CYC for row in raw) and all(len(row) == REAL for row in real)
        answer = {"q": raw, "v": real, "source_chain": sources, "leaves": leaves, "integer_scale": scale}
        return self.remember(self.product_cache, leaves, answer)

    def S_recipe(self, a, j):
        eps = EPS[a]
        assert 0 <= j <= 5-eps
        terms = {}
        for k in range(j+1):
            coefficient = math.comb(j, k)*self.n**k
            if coefficient:
                leaves = tuple(sorted((0,)*(5-eps-j)+(1,)*(j-k)+(73,)*k+self.free_leaves[a]))
                assert len(leaves) == 5
                terms[leaves] = terms.get(leaves, 0)+coefficient
        return {"normal_basis_index": a, "normal_basis_degree": eps, "z_degree": j,
            "tau_power": 5-eps-j, "sigma_power": j, "actual_sigma_integer_n": self.n,
            "free_generator_M2_leaves": list(self.free_leaves[a]),
            "terms": [{"sorted_M2_leaf_indices": list(leaves), "coefficient": str(coefficient)}
                      for leaves, coefficient in sorted(terms.items()) if coefficient]}

    def basis(self):
        if self.C is not None:
            return self.C
        columns, index_rows = [], []
        index = 0
        for a, eps in enumerate(EPS):
            for j in range(6-eps):
                self.budget()
                name = "R809-S5-row-"+str(index).zfill(4)
                recipe = self.S_recipe(a, j)
                data = self.cached(name)
                if data is None:
                    rows = [[0]*REAL for _ in range(COUNT)]
                    terms = []
                    for term in recipe["terms"]:
                        value = self.monomial(term["sorted_M2_leaf_indices"])
                        coefficient = int(term["coefficient"])
                        for n in range(COUNT):
                            for r in range(REAL):
                                rows[n][r] += coefficient*value["v"][n][r]
                        terms.append(dict(term, source_chain=value["source_chain"]))
                    self.store(name, {
                        "index": index, "recipe": recipe, "actual_terms": terms,
                        "normal_basis_index": a, "z_degree": j, "normal_basis_degree": eps,
                        "qY_count": COUNT, "real_coordinate_count": REAL,
                        "integer_scale": str(LEVEL**10),
                        "integer_v_t_coefficients": [[str(x) for x in row] for row in rows],
                        "all_original_term_phases_and_scales_verified": True,
                        "original_R805_free_generator_unchanged": True,
                    })
                    data = self.cached(name)
                assert data["index"] == index and data["recipe"] == recipe
                assert data["integer_scale"] == str(LEVEL**10)
                assert data["qY_count"] == COUNT and data["real_coordinate_count"] == REAL
                assert data["all_original_term_phases_and_scales_verified"] is True
                rows = data["integer_v_t_coefficients"]
                assert len(rows) == COUNT and all(len(row) == REAL for row in rows)
                columns.append([int(x) for row in rows for x in row])
                index_rows.append({"index": index, "normal_basis_index": a,
                    "normal_basis_degree": eps, "z_degree": j,
                    "source": file_spec(self.path(name)), "recipe": recipe})
                index += 1
                if index % 64 == 0 or index == DIM:
                    print(json.dumps({"stage": "S5_rows", "completed_rows": index,
                        "qY_count": COUNT, "seconds": time.monotonic()-self.started}), flush=True)
        assert index == DIM
        name = "R809-S5-basis-index"
        payload = {
            "dimension": DIM, "qY_count": COUNT, "real_coordinate_count": REAL,
            "full_coordinate_rows": ROWS, "integer_scale": str(LEVEL**10),
            "normal_affine_basis_rank": FREE, "normal_basis_degrees": EPS,
            "original_pencil": self.r805.certificate["pencil_stage"],
            "original_graded_free_basis": self.r805.certificate["graded_free_basis_stage"],
            "original_alias_index": self.alias_spec, "basis_rows": index_rows,
            "column_order": "normal_basis_index outer; z_degree=0..5-eps_a inner",
            "coefficient_row_order": "20*qY_exponent+t_degree; phase v=xi^-10*qY",
            "all_original_term_phases_and_scales_verified": True,
            "old_R786_or_R805_short_minor_reused_as_S5_minor": False,
        }
        old = self.cached(name)
        if old is None:
            self.store(name, payload)
        else:
            for key, value in payload.items():
                assert old[key] == value
        self.matrix_spec = file_spec(self.path(name))
        self.C = fmpz_mat(columns).transpose()
        del columns
        gc.collect()
        assert self.C.nrows() == ROWS and self.C.ncols() == DIM
        return self.C

    def solver(self):
        if self.inverse is not None:
            return
        C = self.basis()
        name = "R809-accepted-S5-short-minor"
        old = self.cached(name)
        if old is None:
            prime = self.item["auxiliary_prime_start"]
            while True:
                self.budget()
                assert fmpz(prime).is_prime()
                attempt_name = "R809-prime-"+str(prime)+"-short-rank"
                attempt = self.cached(attempt_name)
                if attempt is None:
                    modular = nmod_mat([[int(C[i, j]) % prime for i in range(ROWS)] for j in range(DIM)], prime)
                    reduced, rank = modular.rref()
                    indices = [next(j for j in range(ROWS) if reduced[i, j]) for i in range(rank)]
                    assert indices == sorted(set(indices))
                    payload = {"prime": prime, "actual_rank": rank,
                        "S5_basis_index": self.matrix_spec, "row_indices": indices,
                        "characteristic_zero_rank_failure_claimed": False}
                    if rank == DIM:
                        square = nmod_mat([[int(C[i, j]) % prime for j in range(DIM)] for i in indices], prime)
                        determinant = int(square.det())
                        assert determinant
                        payload["actual_determinant_mod_prime"] = determinant
                    self.store(attempt_name, payload)
                    attempt = self.cached(attempt_name)
                    del modular, reduced
                    gc.collect()
                assert attempt["prime"] == prime and attempt["S5_basis_index"] == self.matrix_spec
                if attempt["actual_rank"] == DIM:
                    self.store(name, {
                        "prime": prime, "actual_rank": DIM, "row_indices": attempt["row_indices"],
                        "column_indices": list(range(DIM)), "full_coordinate_rows": ROWS,
                        "actual_determinant_mod_prime": attempt["actual_determinant_mod_prime"],
                        "actual_rank_stage": file_spec(self.path(attempt_name)),
                        "S5_basis_index": self.matrix_spec,
                        "minor_is_from_actual_69_term_matrix": True,
                    })
                    old = self.cached(name)
                    break
                prime += 2
                while not fmpz(prime).is_prime():
                    prime += 2
        assert old["S5_basis_index"] == self.matrix_spec
        assert old["actual_rank"] == DIM and old["full_coordinate_rows"] == ROWS
        assert old["column_indices"] == list(range(DIM))
        assert old["minor_is_from_actual_69_term_matrix"] is True
        self.I, self.prime = old["row_indices"], old["prime"]
        assert len(self.I) == DIM and self.I == sorted(set(self.I))
        assert all(0 <= i < ROWS for i in self.I)
        assert old["actual_determinant_mod_prime"] % self.prime
        self.minor_spec = file_spec(self.path(name))
        self.square = fmpz_mat([[C[i, j] for j in range(DIM)] for i in self.I])
        inverse_name = "R809-S5-fixed-modular-inverse"
        data = self.cached(inverse_name)
        if data is None:
            self.budget()
            matrix = nmod_mat([[int(self.square[i, j]) % self.prime for j in range(DIM)]
                               for i in range(DIM)], self.prime)
            assert int(matrix.det()) == old["actual_determinant_mod_prime"]
            inverse = matrix.inv()
            product = matrix*inverse
            assert all(int(product[i, j]) == int(i == j) for i in range(DIM) for j in range(DIM))
            self.store(inverse_name, {
                "prime": self.prime, "minor_stage": self.minor_spec,
                "S5_basis_index": self.matrix_spec,
                "inverse_mod_prime": matrix_rows(inverse), "inverse_product_exactly_verified_mod_prime": True,
                "composite_modulus_matrix_inversion": False,
            })
            data = self.cached(inverse_name)
        assert data["prime"] == self.prime and data["minor_stage"] == self.minor_spec
        assert data["S5_basis_index"] == self.matrix_spec
        assert data["inverse_product_exactly_verified_mod_prime"] is True
        self.inverse = nmod_mat(data["inverse_mod_prime"], self.prime)
        assert self.inverse.nrows() == self.inverse.ncols() == DIM
        self.inverse_spec = file_spec(self.path(inverse_name))

    def tau_theta(self):
        if self.factor_data is not None:
            return self.factor_data
        name = "R809-original-tau-theta-factor"
        data = self.cached(name)
        sources = [self.sources[2, i] for i in range(5)]
        for i in range(5):
            assert self.leaves[2, i] == tuple(sorted((0, i)))
        if data is None:
            self.budget()
            integers, scale = primitive(self.lambdas)
            rows = [[0]*REAL for _ in range(COUNT)]
            for i, value in enumerate(integers):
                if value:
                    old = self.original(2, i)["v"]
                    for n in range(COUNT):
                        for r in range(REAL):
                            rows[n][r] += value*old[n][r]
            content = integer_content([x for row in rows for x in row])
            assert content and scale
            rows = [[x//content for x in row] for row in rows]
            scale *= content
            self.store(name, {
                "theta_stage": self.r807.certificate["theta_stage"],
                "original_V2_sources": sources, "original_V2_indices": list(range(5)),
                "original_V2_monomials": [[0, i] for i in range(5)],
                "lambda": self.theta["lambda"],
                "primitive_integer_v_t_coefficients": [[str(x) for x in row] for row in rows],
                "rational_scale": pairs(scale), "qY_count": COUNT,
                "integer_V2_basis_scale": str(LEVEL**4),
                "actual_factor": "tau*theta=sum(lambda_i*original_scaled_V2[i]),i0..4",
                "old_five_products_recomputed": False, "original_theta_normalization_preserved": True,
            })
            data = self.cached(name)
        assert data["theta_stage"] == self.r807.certificate["theta_stage"]
        assert data["original_V2_sources"] == sources and data["lambda"] == self.theta["lambda"]
        assert data["integer_V2_basis_scale"] == str(LEVEL**4)
        rows = [[int(x) for x in row] for row in data["primitive_integer_v_t_coefficients"]]
        assert len(rows) == COUNT and all(len(row) == REAL for row in rows)
        scale = dq(data["rational_scale"])
        assert scale and any(x for row in rows for x in row)
        self.factor_data = {"rows": rows, "scale": scale, "source": file_spec(self.path(name))}
        return self.factor_data

    def extra_M6(self, index):
        assert index in M6_RECIPES
        source = self.extra_sources[index]
        old = self.r803.indexed(source)
        assert old["index"] == index and old["recipe"] == M6_RECIPES[index]
        assert old["integer_scale"] == str(LEVEL**6) and old["bound_qY"] == 41
        assert old["new_complete_short_row_verified_against_original_M6_mod739"] is True
        raw = [[int(x) for x in row] for row in old["integer_qY_xi_coefficients"]]
        assert len(raw) == 42 and all(len(row) == CYC for row in raw)
        real = self.real_rows(raw)
        name = "R809-original-M6-extra-tail-"+str(index)+"-0042-0069"
        data = self.cached(name)
        if data is None:
            self.budget()
            if index < 692:
                original = self.original(1, M6_RECIPES[index]["index"])
                tail = [[value*LEVEL**4 for value in row] for row in original["q"][42:COUNT]]
                factors = original["source_chain"]
            else:
                tail = [[0]*CYC for _ in range(COUNT-42)]
                factors = []
            vtail = self.real_rows(tail, 42)
            self.store(name, {
                "index": index, "recipe": M6_RECIPES[index], "integer_scale": str(LEVEL**6),
                "first_exponent": 42, "last_exponent_exclusive": COUNT,
                "original_R803_producer": producer_identity(self.r803.spec),
                "completed_R803_prefix": source, "original_factor_sources": factors,
                "integer_qY_xi_coefficients": [[str(x) for x in row] for row in tail],
                "integer_v_t_coefficients": [[str(x) for x in row] for row in vtail],
                "only_new_42_through68_coefficients_generated": True,
                "old_M2_or_M6_prefix_recomputed": False,
                "E4_E6_first_possible_nonconstant_order": 82,
                "eta12_original_first_order": 41, "eta12_next_possible_order": 123,
            })
            data = self.cached(name)
        assert data["index"] == index and data["recipe"] == M6_RECIPES[index]
        assert data["completed_R803_prefix"] == source
        assert data["original_R803_producer"] == producer_identity(self.r803.spec)
        assert data["integer_scale"] == str(LEVEL**6)
        assert data["first_exponent"] == 42 and data["last_exponent_exclusive"] == COUNT
        tail = [[int(x) for x in row] for row in data["integer_qY_xi_coefficients"]]
        vtail = [[int(x) for x in row] for row in data["integer_v_t_coefficients"]]
        assert len(tail) == len(vtail) == COUNT-42 and self.real_rows(tail, 42) == vtail
        real.extend(vtail)
        return real, [source, dict(file_spec(self.path(name)), producer="R809")]

    def original_M6_matrix(self):
        if self.M6matrix is not None:
            return self.M6matrix
        columns, sources = [], []
        for index in range(690):
            self.budget()
            old = self.original(3, index)
            assert self.M6index["basis_rows"][index]["recipe"] == {"kind": "power_basis", "power": 3, "index": index}
            assert self.M6index["basis_rows"][index]["source"] == self.sources[3, index]
            columns.append([value for row in old["v"] for value in row])
            sources.append({"index": index, "source_chain": old["source_chain"]})
        for index in range(690, 694):
            rows, chain = self.extra_M6(index)
            columns.append([value for row in rows for value in row])
            sources.append({"index": index, "source_chain": chain})
        name = "R809-original-M6-prefix-index"
        payload = {
            "dimension": 694, "qY_count": COUNT, "real_coordinate_count": REAL,
            "integer_scale": str(LEVEL**6), "basis_rows": sources,
            "original_R803_producer": producer_identity(self.r803.spec),
            "original_M6_basis_index": self.r803.certificate["basis_index"],
            "old_ordinary_rows_or_original_four_short_prefixes_recomputed": False,
            "new_four_extra_tail_interval": [42, COUNT],
        }
        old = self.cached(name)
        if old is None:
            self.store(name, payload)
        else:
            for key, value in payload.items():
                assert old[key] == value
        self.M6_spec = file_spec(self.path(name))
        self.M6matrix = fmpz_mat(columns).transpose()
        del columns
        gc.collect()
        assert self.M6matrix.nrows() == ROWS and self.M6matrix.ncols() == 694
        return self.M6matrix

    def U_prefix(self, target):
        assert target.startswith("C")
        j = int(target[1:])
        name = "R809-target-"+target+"-original-U-prefix"
        old = self.cached(name, target)
        if old is not None:
            assert old["j"] == j and old["source_original_U_coordinates"] == self.U_specs[str(j)]
            assert old["coefficient_field_basis"] == FIELD_BASIS
            return old, file_spec(self.path(name))
        self.budget()
        matrix = self.original_M6_matrix()
        data = self.r803.indexed(self.U_specs[str(j)])
        assert data["j"] == j and data["basis_dimension"] == 694
        assert data["basis_integer_scale"] == str(LEVEL**6)
        assert data["original_M6_basis_index"] == self.r803.certificate["basis_index"]
        assert data["coefficient_field_basis"] == FIELD_BASIS
        assert data["all1680_original_coordinates_verified"] is True
        rows = data["coefficients_in_integer_scaled_original_M6_basis"]
        assert len(rows) == 694 and all(len(row) == LDEG for row in rows)
        integers, scales = [], []
        for k in range(LDEG):
            values, scale = primitive([dq(rows[i][k]) for i in range(694)])
            integers.append(values)
            scales.append(scale)
        combined = matrix*fmpz_mat(integers).transpose()
        prefix, actual_scales = [], []
        for k in range(LDEG):
            values = [int(combined[i, k]) for i in range(ROWS)]
            content = integer_content(values)
            if content:
                prefix.append([str(value//content) for value in values])
                actual_scales.append(pairs(scales[k]*content))
            else:
                prefix.append(["0"]*ROWS)
                actual_scales.append(["0", "1"])
        self.store(name, {
            "j": j, "qY_count": COUNT, "full_coordinate_rows": ROWS,
            "source_original_U_coordinates": self.U_specs[str(j)],
            "original_M6_prefix_index": self.M6_spec,
            "primitive_integer_columns": prefix, "rational_scales": actual_scales,
            "coefficient_field_basis": FIELD_BASIS,
            "actual_identity": "U_j=sum(original_R803_coordinates*82^6_original_M6_rows)",
            "source_original_basis_scale": str(LEVEL**6),
            "original_4_over_1722_cubed_and_b_s_scales_preserved": True,
            "old_Hodge_tensors_Hom_or_periods_recomputed": False,
        }, target)
        return self.cached(name, target), file_spec(self.path(name))

    def real_product(self, left, right):
        assert len(left) == len(right) == COUNT
        value = packed(left, 39).mul_low(packed(right, 39), 39*COUNT)
        answer = []
        for n in range(COUNT):
            polynomial = fmpz_poly([value[39*n+r] for r in range(39)]) % self.gt
            answer.extend(int(polynomial[r]) for r in range(REAL))
        assert len(answer) == ROWS
        return answer

    def target(self, target):
        name = "R809-target-"+target+"-full-prefix"
        old = self.cached(name, target)
        if old is not None:
            assert old["target"] == target and old["full_coordinate_rows"] == ROWS
            assert old["coefficient_field_basis"] == FIELD_BASIS
            return old, file_spec(self.path(name))
        self.budget()
        if target.startswith("C"):
            U, Uspec = self.U_prefix(target)
            factor = self.tau_theta()
            columns, scales = [], []
            for k in range(LDEG):
                self.budget()
                flat = [int(x) for x in U["primitive_integer_columns"][k]]
                assert len(flat) == ROWS
                rows = [flat[REAL*n:REAL*(n+1)] for n in range(COUNT)]
                scale = dq(U["rational_scales"][k])*factor["scale"]
                if scale:
                    values = self.real_product(rows, factor["rows"])
                    content = integer_content(values)
                    assert content, "Nonzero U coefficient disappeared in injective V5 prefix."
                    columns.append([str(value//content) for value in values])
                    scales.append(pairs(scale*content))
                else:
                    assert not any(flat)
                    columns.append(["0"]*ROWS)
                    scales.append(["0", "1"])
            sources = {"original_U_prefix": Uspec, "original_tau_theta_factor": factor["source"],
                "global_V5_membership": self.r807.certificate["cleared_coordinate_index"],
                "literal_tau_factor": True}
        else:
            assert self.relation is not None
            columns_old, sources_old = [], []
            for index in range(DIM):
                self.budget()
                original = self.original(5, index)
                columns_old.append([x for row in original["v"] for x in row])
                sources_old.append(self.sources[5, index])
            matrix = fmpz_mat(columns_old).transpose()
            del columns_old
            coefficients = [[int(x) for x in row] for row in self.relation[target+"_integer_L_coordinates"]]
            combined = matrix*fmpz_mat(coefficients)
            del matrix
            lam = int(self.relation["field"]["lambda"])
            columns, scales = [], []
            for k in range(LDEG):
                values = [int(combined[i, k]) for i in range(ROWS)]
                content = integer_content(values)
                if content:
                    columns.append([str(value//content) for value in values])
                    scales.append(pairs(fmpq(content*lam**(k % 7))))
                else:
                    columns.append(["0"]*ROWS)
                    scales.append(["0", "1"])
            sources = {"original_R787_function_recipe": self.r787.certificate["relation_spec"],
                "original_R786_V5_sources": sources_old,
                "original_R786_basis_index": self.relation["R786_basis_index"],
                "original_Bfield_equals_lambda_b": str(lam),
                "original_common_denominator_or_content_reinserted": False,
                "literal_tau_factor": False}
        assert len(columns) == len(scales) == LDEG
        assert all(len(column) == ROWS for column in columns)
        assert any(dq(scale) for scale in scales)
        self.store(name, {
            "target": target, "qY_count": COUNT, "full_coordinate_rows": ROWS,
            "primitive_integer_columns": columns, "rational_scales": scales,
            "source_inputs": sources, "coefficient_field_basis": FIELD_BASIS,
            "homogeneous_basis_scale": str(LEVEL**10),
            "target_known_globally_in_original_V5": True,
            "regular_degree_bound": 4 if target.startswith("C") else 5,
            "original_field_and_scalar_normalizations_preserved": True,
        }, target)
        return self.cached(name, target), file_spec(self.path(name))

    def reconstruct(self, lifted, modulus, target):
        count = target.ncols()
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
        for k in range(count):
            denominator = 1
            for row in values:
                denominator = math.lcm(denominator, int(row[k].denom()))
            denominators.append(denominator)
        numerators = fmpz_mat([
            [int(value.numer())*(denominators[k]//int(value.denom())) for k, value in enumerate(row)]
            for row in values])
        actual = self.C*numerators
        for i in range(ROWS):
            for k in range(count):
                if actual[i, k] != target[i, k]*denominators[k]:
                    return None
        return numerators, denominators

    def solve_group(self, target_name, group):
        self.solver()
        first = group*self.item["dixon_group_columns"]
        indices = list(range(first, min(first+self.item["dixon_group_columns"], LDEG)))
        assert indices and group in (0, 1)
        target_data, target_spec = self.target(target_name)
        scales = [target_data["rational_scales"][k] for k in indices]
        stem = "R809-target-"+target_name+"-group-"+str(group).zfill(2)
        name, current_name = stem+"-exact-coordinates", stem+"-dixon-current"
        old = self.cached(name, target_name)
        if old is not None:
            assert old["target"] == target_name and old["column_indices"] == indices
            assert old["source_full_target"] == target_spec
            assert old["fixed_minor_inverse"] == self.inverse_spec
            assert old["S5_basis_index"] == self.matrix_spec
            assert old["original_target_rational_scales"] == scales
            assert old["all1380_original_coordinates_verified"] is True
            if self.path(current_name).exists():
                current = self.cached(current_name, target_name, current=True)
                assert current["source_full_target"] == target_spec
                assert current["column_indices"] == indices and current["prime"] == self.prime
                assert current["fixed_minor_inverse"] == self.inverse_spec
                self.path(current_name).unlink()
            return file_spec(self.path(name))
        target = fmpz_mat([[int(target_data["primitive_integer_columns"][k][i]) for k in indices]
                          for i in range(ROWS)])
        count = len(indices)
        ni = [[int(target[i, k]) for k in range(count)] for i in self.I]
        binding = {
            "target": target_name, "column_indices": indices,
            "source_full_target": target_spec, "S5_basis_index": self.matrix_spec,
            "fixed_minor_inverse": self.inverse_spec,
            "original_target_rational_scales": scales,
        }
        binding_hash = fingerprint(binding)
        current = self.cached(current_name, target_name, current=True)
        if current is None:
            lifted, residual, digits, modulus = [[0]*count for _ in range(DIM)], ni, 0, 1
            previous_sha = None
        else:
            assert current["target"] == target_name and current["column_indices"] == indices
            assert current["prime"] == self.prime and current["source_full_target"] == target_spec
            assert current["fixed_minor_inverse"] == self.inverse_spec
            assert current["rhs_binding_sha256"] == binding_hash
            digits, modulus = current["digits"], int(current["modulus"])
            assert digits >= 1 and modulus == self.prime**digits
            lifted = [[int(x) for x in row] for row in current["lifted_integer_coordinates"]]
            residual = [[int(x) for x in row] for row in current["exact_divided_residual"]]
            assert len(lifted) == len(residual) == DIM
            assert all(len(row) == count for row in lifted+residual)
            assert all(0 <= value < modulus for row in lifted for value in row)
            actual = self.square*fmpz_mat(lifted)
            assert all(actual[i, k]+modulus*residual[i][k] == ni[i][k]
                       for i in range(DIM) for k in range(count))
            previous_sha = sha(self.path(current_name))
        while True:
            self.budget()
            if digits and (digits == 1 or digits % self.item["reconstruct_every_digits"] == 0):
                recovered = self.reconstruct(lifted, modulus, target)
                if recovered is not None:
                    numerators, denominators = recovered
                    assert all(denominator > 0 and denominator % self.prime for denominator in denominators)
                    if target_name.startswith("C"):
                        for row in range(DIM):
                            a, degree = S_position(row)
                            if degree == 5-EPS[a]:
                                assert all(numerators[row, k] == 0 for k in range(count))
                    self.store(name, {
                        "target": target_name, "group": group, "column_indices": indices,
                        "basis_dimension": DIM, "normal_basis_rank": FREE,
                        "coordinate_numerators": matrix_rows(numerators, strings=True),
                        "column_denominators": [str(x) for x in denominators],
                        "original_target_rational_scales": scales,
                        "coordinate_convention": "S5 coefficient=numerator/column_denominator*original_target_rational_scale",
                        "coefficient_field_basis": FIELD_BASIS,
                        "source_full_target": target_spec, "rhs_binding_sha256": binding_hash,
                        "S5_basis_index": self.matrix_spec, "fixed_minor_inverse": self.inverse_spec,
                        "basis_integer_scale": str(LEVEL**10),
                        "actual_prime": self.prime, "actual_Dixon_digits": digits,
                        "actual_reconstruction_modulus": str(modulus),
                        "full_coordinate_rows": ROWS, "all1380_original_coordinates_verified": True,
                        "regular_degree_bound": 4 if target_name.startswith("C") else 5,
                        "literal_tau_factor_highest_S5_coefficients_zero": target_name.startswith("C"),
                        "original_field_and_scalar_normalizations_preserved": True,
                        "rational_reconstruction_used_uniform_strict_rectangular_bound": True,
                        "characteristic_zero_inverse_matrix_formed": False,
                    }, target_name)
                    self.path(current_name).unlink(missing_ok=True)
                    print(json.dumps({"stage": "exact_S5_normal_coordinates", "target": target_name,
                        "group": group, "columns": indices, "digits": digits,
                        "full_rows_verified": ROWS, "seconds": time.monotonic()-self.started}), flush=True)
                    return file_spec(self.path(name))
            correction = self.inverse*nmod_mat(
                [[value % self.prime for value in row] for row in residual], self.prime)
            delta = matrix_rows(correction)
            if digits == 0:
                full = nmod_mat([[int(self.C[i, j]) % self.prime for j in range(DIM)]
                                  for i in range(ROWS)], self.prime)*correction
                assert all(int(full[i, k]) == int(target[i, k]) % self.prime
                           for i in range(ROWS) for k in range(count)), "Actual target outside original S5 mod span."
            product = self.square*fmpz_mat(delta)
            updated = []
            for i in range(DIM):
                row = []
                for k in range(count):
                    numerator = residual[i][k]-int(product[i, k])
                    assert numerator % self.prime == 0
                    row.append(numerator//self.prime)
                    lifted[i][k] += modulus*delta[i][k]
                updated.append(row)
            residual, modulus, digits = updated, modulus*self.prime, digits+1
            self.store(current_name, {
                "target": target_name, "group": group, "column_indices": indices,
                "prime": self.prime, "digits": digits, "modulus": str(modulus),
                "source_full_target": target_spec, "fixed_minor_inverse": self.inverse_spec,
                "rhs_binding_sha256": binding_hash,
                "lifted_integer_coordinates": [[str(x) for x in row] for row in lifted],
                "exact_divided_residual": [[str(x) for x in row] for row in residual],
                "previous_checkpoint_sha256": previous_sha,
                "invariant": "minor*lift+prime^digits*residual=primitive_target_I",
                "complete_coordinates_claimed": False,
                "only_current_full_lift_vector_retained": True,
            }, target_name, current=True)
            current_sha = sha(self.path(current_name))
            history_name = stem+"-dixon-digit-"+str(digits).zfill(6)+"-receipt"
            history = {
                "target": target_name, "group": group, "column_indices": indices,
                "prime": self.prime, "digits": digits, "modulus_bits": modulus.bit_length(),
                "rhs_binding_sha256": binding_hash,
                "current_checkpoint_sha256": current_sha, "previous_checkpoint_sha256": previous_sha,
                "exact_divided_residual_invariant_preserved": True,
                "large_lift_vector_or_residual_embedded": False,
            }
            prior = self.cached(history_name, target_name)
            if prior is None:
                self.store(history_name, history, target_name)
            else:
                for key, value in history.items():
                    assert prior[key] == value
            previous_sha = current_sha
            if digits == 1 or digits % self.item["reconstruct_every_digits"] == 0:
                print(json.dumps({"stage": "Dixon_S5_normal_coordinates", "target": target_name,
                    "group": group, "digits": digits, "modulus_bits": modulus.bit_length(),
                    "seconds": time.monotonic()-self.started}), flush=True)

    def normal_vector(self, target):
        name = "R809-target-"+target+"-normal-vector"
        groups = [self.solve_group(target, group) for group in range(2)]
        coverage, nonzero = [], False
        for spec in groups:
            data = self.cached(spec["file"], target)
            assert data["S5_basis_index"] == self.matrix_spec
            assert data["all1380_original_coordinates_verified"] is True
            indices = data["column_indices"]
            assert len(indices) == len(data["column_denominators"]) == len(data["original_target_rational_scales"]) == 7
            rows = data["coordinate_numerators"]
            assert len(rows) == DIM and all(len(row) == len(indices) for row in rows)
            for row_index, row in enumerate(rows):
                a, degree = S_position(row_index)
                for k, value in enumerate(row):
                    rational_scale = dq(data["original_target_rational_scales"][k])
                    if target.startswith("C") and degree > 4-EPS[a]:
                        assert int(value) == 0
                    if int(value) and rational_scale:
                        nonzero = True
            coverage.extend(indices)
        assert coverage == list(range(LDEG)) and nonzero
        payload = {
            "target": target, "normal_basis_rank": FREE, "normal_basis_degrees": EPS,
            "regular_degree_bound": 4 if target.startswith("C") else 5,
            "coefficient_field_basis": FIELD_BASIS, "original_b_model": self.model,
            "normal_function": self.target_tag(target)["normal_function"],
            "S5_basis_index": self.matrix_spec, "coordinate_groups": groups,
            "coefficient_reconstruction": "group numerator / group column_denominator * original_target_rational_scale; S5 row maps to normal_basis_index,z_degree",
            "coordinate_row_mapping": "S5_basis_index.basis_rows[index].normal_basis_index and .z_degree",
            "all14_original_field_columns_retained": True,
            "normal_vector_actually_nonzero": True,
            "all1380_original_coordinates_verified": True,
            "weighted_polynomial_support_verified": True,
            "literal_tau_factor_highest_S5_coefficients_zero": target.startswith("C"),
            "original_field_and_scalar_normalizations_preserved": True,
            "normal_ring_multiplication_or_field_division_computed": False,
            "actual_polar_ideal_or_eta_or_height_computed": False,
        }
        old = self.cached(name, target)
        if old is None:
            self.store(name, payload, target)
        else:
            for key, value in payload.items():
                assert old[key] == value
        return file_spec(self.path(name))

    def run(self):
        final = self.out/FINAL
        previous_final = None
        if final.exists():
            old = read(final)
            assert old["result"] == RESULT and old["complete"] is True
            assert old["configuration"] == self.tag
            previous_final = file_spec(final)
            spec = old["stage_manifest"]
            assert file_spec(self.out/spec["file"]) == spec
            inventory = self.cached(spec["file"])
            for row in inventory["files"]:
                assert file_spec(self.out/row["file"]) == row
        self.basis()
        # Materialize only actual targets; all completed source-bound targets are reused.
        for target in self.requested:
            self.target(target)
        self.M6matrix = None
        self.old_cache.clear()
        self.product_cache.clear()
        gc.collect()
        self.solver()
        for target in self.requested:
            self.normal_vector(target)
        completed, vectors = [], {}
        for target in TARGETS:
            name = "R809-target-"+target+"-normal-vector"
            if self.path(name).exists():
                data = self.cached(name, target)
                assert data["target"] == target and data["all1380_original_coordinates_verified"] is True
                completed.append(target)
                vectors[target] = file_spec(self.path(name))
        assert set(self.requested) <= set(completed)
        ratio_targets = [target for target in completed if target.startswith("C")]
        interface_payload = {
            "S5_basis_index": self.matrix_spec, "original_pencil": self.r805.certificate["pencil_stage"],
            "original_graded_free_basis": self.r805.certificate["graded_free_basis_stage"],
            "normal_basis_rank": FREE, "normal_basis_degrees": EPS,
            "coefficient_field_basis": FIELD_BASIS, "original_b_model": self.model,
            "normal_vectors": vectors,
            "original_y_equation": "normal(A)/normal(B)" if {"A", "B"} <= set(completed) else None,
            "original_Hodge_ratio_equations": {
                target: "normal("+target+")/normal(C0)=U_"+target[1:]+"/U_0"
                for target in ratio_targets if target != "C0" and "C0" in completed},
            "original_theta_not_inverted_separately": True,
            "all_original_CM_Hodge_and_target_scalars_preserved": True,
            "actual_normal_ring_multipliers_or_field_quotients_computed": False,
            "actual_derivation_polar_ideal_eta_or_height_computed": False,
        }
        interface_name = "R809-normal-function-consumer-interface-"+fingerprint(interface_payload)[:24]
        prior_interface = self.cached(interface_name)
        if prior_interface is None:
            interface = self.store(interface_name, interface_payload)
        else:
            for key, value in interface_payload.items():
                assert prior_interface[key] == value
            interface = file_spec(self.path(interface_name))
        files = [file_spec(path) for path in sorted(self.out.glob("R809-*.json.gz"))
                 if not path.name.startswith("R809-stage-manifest-") and not path.name.endswith("-dixon-current.json.gz")]
        manifest_name = "R809-stage-manifest-"+fingerprint(files)[:24]
        prior_inventory = self.cached(manifest_name)
        if prior_inventory is None:
            manifest = self.store(manifest_name, {"files": files})
        else:
            assert prior_inventory["files"] == files
            manifest = file_spec(self.path(manifest_name))
        pending = [file_spec(path) for path in sorted(self.out.glob("R809-*-dixon-current.json.gz"))]
        cert = {
            "result": RESULT, "complete": True, "configuration": self.tag,
            "p": P, "completed_scope": "requested_actual_normal_coordinate_targets",
            "requested_target_groups": self.requested, "completed_target_groups": completed,
            "completed_rational_RHS_columns": LDEG*len(completed),
            "S5_dimension": DIM, "qY_count": COUNT, "full_real_coordinates": ROWS,
            "normal_basis_rank": FREE, "normal_basis_degrees": EPS,
            "basis_integer_scale": str(LEVEL**10), "actual_sigma_integer_n": self.n,
            "coefficient_field_basis": FIELD_BASIS, "original_b_model": self.model,
            "S5_basis_index": self.matrix_spec, "minor_stage": self.minor_spec,
            "modular_inverse_stage": self.inverse_spec,
            "actual_prime": self.prime,
            "actual_short_minor_determinant": self.cached(self.minor_spec["file"])["actual_determinant_mod_prime"],
            "normal_vectors": vectors, "normal_function_interface": interface,
            "completed_target_configurations": {target: self.target_tag(target) for target in completed},
            "all_requested_targets_verified_in_all1380_rows": True,
            "all_completed_C_targets_highest_S5_coefficients_zero": True,
            "actual_original_y_normal_vectors_computed": {"A", "B"} <= set(completed),
            "all_112_rational_targets_computed": len(completed) == len(TARGETS),
            "original_scalar_and_field_normalizations_preserved": True,
            "old_mathematical_producer_stages_recomputed": False,
            "actual_polar_ideal_or_eta_or_height_computed": False,
            "characteristic_zero_Krylov_inverse_computed": False,
            "basis_identity_excludes_requested_scope_budget_and_future_R787": True,
            "previous_completed_scope_certificate": previous_final,
            "pending_unrequested_current_lifts": pending,
            "stage_manifest": manifest, "seconds": time.monotonic()-self.started,
        }
        save(final, cert)
        save(self.out/"core-receipt.json", {
            "result": RESULT, "complete": True, "source_sha256": sha(__file__),
            "certificate_sha256": sha(final), "requested_target_groups": self.requested,
            "completed_target_groups": completed, "completed_rational_RHS_columns": LDEG*len(completed),
            "all_requested_targets_verified_in_all1380_rows": True,
            "actual_original_y_normal_vectors_computed": {"A", "B"} <= set(completed),
            "actual_polar_ideal_or_eta_or_height_computed": False,
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
            "completed_basis_targets_coordinates_and_latest_exact_lifts_preserved": True,
            "actual_polar_ideal_or_eta_or_height_computed": False,
        })
        raise


if __name__ == "__main__":
    sys.exit(main())
