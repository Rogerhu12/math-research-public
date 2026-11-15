#!/usr/bin/env python3
"""Independent projective reconstruction of the original R787 relation.

New arithmetic runs only in the public repository Actions.  The frozen 430-digit
lift and every old mathematical stage are read as inputs.  Small LLL problems
generate candidates; only the complete original 129-by-280 characteristic-zero
identities and the unchanged free-column pattern certify a relation.
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
from flint import fmpz_mat, fmpz_poly

RESULT = "R787-original-power5-function-relation"
FINAL = "p41-original-power5-function-relation-certificate.json"
PREFIX = "R787-projective-"
RECIPE = "R787-original-function-recipe.json.gz"
OLD_CORE = "93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04"
OLD_METHOD = "1d91bfc7bdf61c40c4deda19833a5f50491630a61a7a25feb7a3a1e0b451204b"
R786_PROOF = "c46008726fb18f52a5430b72c4994ce76164f11bea51044f1677278294f7011d"
FIELD_CORE = "d024a7a6f5febd4658e8b5b5e5e3659f3c5fcc0daa39d70569ac408ef83a8751"
OLD_TAG = "71ea66416a42e024de61cf5927bc493fbc8422dc1b5970d75c51bd788d88529d"
N, NC, LD, TD, ORDERS = 1234, 1214, 14, 20, 129
PRIME, DIGITS = 1000000753, 430
SHIFTS = (0, 256, -256, 1024, -1024)
CHUNK = 64
CHILD_LIMIT = 8
ALGORITHM = "integral-L-denominator-28-lattice-v1"
CHILD_EXPECTED = {
    "R781": {
        "result": "R781-original-p41-inverse-free-Laurent-prefix",
        "manifest": "ce0554fab03fda8d124e9e0ee338335bca6f7b39ee8499550bbec36358a1a7fd",
        "certificate": "b9e1a2282d6fc0de12df401abbc3014ded525757c7102d11967f0bd33a40f3f0",
        "core": FIELD_CORE},
    "R786": {
        "result": "R786-exact-original-power5-short-basis",
        "manifest": "e3c29e85236c8cc665bdf88e9ffd2bbab9180b6f977f0b2b22f54266762f405a",
        "certificate": "dc6c23568f80b861d839280846c3250063abdfb2716a20481779816bb7cd37d9",
        "core": "4508095a95a2bcaec8c8db8fcd550fbc618b017d2bc0007945783bc109dbf851"}}


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    payload = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        with temporary.open("wb") as raw:
            with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, compresslevel=2) as stream:
                stream.write(payload)
    else:
        temporary.write_bytes(payload)
    temporary.replace(path)


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def spec_hash(value):
    return value["sha256"] if isinstance(value, dict) else value


def integer_rows(rows, count, width):
    assert len(rows) == count and all(len(row) == width for row in rows)
    return [[int(x) for x in row] for row in rows]


def strings(rows):
    return [[str(x) for x in row] for row in rows]


class BudgetStop(RuntimeError):
    pass


class Source:
    def __init__(self, directory, spec):
        self.directory, self.spec = Path(directory), spec
        manifest = self.directory/"full-outputs-manifest.json"
        assert sha(manifest) == spec["manifest_sha256"]
        obj = read(manifest)
        assert obj["result"] == spec["result"]
        self.files = {item["file"]: item for item in obj["files"]}
        assert len(self.files) == len(obj["files"])
        self.tag = None
        self.used = {}

    def raw(self, name):
        assert Path(name).name == name
        item = self.files[name]
        path = self.directory/name
        assert path.stat().st_size == item["bytes"] and sha(path) == item["sha256"]
        if name in self.spec.get("files", {}):
            assert item["sha256"] == spec_hash(self.spec["files"][name])
        self.used[name] = dict(item)
        return read(path)

    def stage(self, name):
        obj = self.raw(name)
        assert obj["complete"] is True
        if self.tag is None:
            self.tag = obj["configuration"]
        else:
            assert obj["configuration"] == self.tag
        return obj

    def ref(self, name):
        item = self.files[name]
        return {key: item[key] for key in ("file", "bytes", "sha256")}


class IntegralOrder:
    """O=Z[B,s], s^2=-3; row order 1,B,...,B^6,s,sB,...,sB^6."""
    def __init__(self, fB):
        self.fB = fmpz_poly([int(x) for x in fB])
        assert self.fB.degree() == 7 and self.fB[7] == 1

    def multiply(self, left, right):
        assert len(left) == len(right) == LD
        a, b = fmpz_poly(left[:7]), fmpz_poly(left[7:])
        c, d = fmpz_poly(right[:7]), fmpz_poly(right[7:])
        u, v = (a*c-3*b*d) % self.fB, (a*d+b*c) % self.fB
        return [int(u[i]) for i in range(7)]+[int(v[i]) for i in range(7)]

    def centered_product(self, left, right, modulus):
        half = modulus//2
        answer = []
        for value in self.multiply(left, right):
            value %= modulus
            answer.append(value-modulus if value > half else value)
        return answer

    def multiplication_rows(self, value, modulus=None):
        answer = []
        for i in range(LD):
            unit = [int(j == i) for j in range(LD)]
            row = self.multiply(unit, value)
            if modulus is not None:
                row = [x % modulus for x in row]
            answer.append(row)
        return answer

    def multiplication_bound(self):
        totals = [0]*LD
        for i in range(LD):
            left = [int(k == i) for k in range(LD)]
            for j in range(LD):
                right = [int(k == j) for k in range(LD)]
                for k, value in enumerate(self.multiply(left, right)):
                    totals[k] += abs(value)
        return max([1]+totals)


class Job:
    def __init__(self, args):
        assert flint.__version__ == "0.9.0"
        self.args, self.out = args, args.output
        self.started = time.monotonic()
        self.item = read(args.config)
        assert self.item["producer_inputs_pending"] is False
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert sha(__file__) == self.item["core_sha256"]
        assert sha(args.method) == self.item["projective_method_sha256"]
        assert self.item["R787_method_sha256"] == OLD_METHOD
        assert self.item["R786_proof_sha256"] == R786_PROOF
        assert sha(args.field_core) == self.item["field_core_sha256"] == FIELD_CORE
        assert self.item["pinned_R787_configuration_sha256"] == OLD_TAG
        self.out.mkdir(parents=True, exist_ok=True)
        self.source = Source(args.retained/"R787", self.item["retained_source"])
        assert self.source.spec["result"] == RESULT
        assert self.source.spec["core_sha256"] == OLD_CORE
        checkpoint = self.item["checkpoint"]
        assert checkpoint["prime"] == PRIME and checkpoint["digits"] == DIGITS
        self.chart = self.source.stage(checkpoint["chart_file"])
        self.old_tag = self.source.tag
        assert fingerprint(self.old_tag) == OLD_TAG
        assert self.old_tag["source_sha256"] == OLD_CORE
        assert self.old_tag["R787_method_sha256"] == OLD_METHOD
        assert self.old_tag["R786_proof_sha256"] == R786_PROOF
        assert self.old_tag["R781_field_core_sha256"] == FIELD_CORE
        assert self.old_tag["python_flint"] == "0.9.0"
        assert self.old_tag["retained_artifacts"] == self.item["retained_artifacts"]
        assert self.old_tag["basis_integer_scale"] == "13744803133596058624"
        assert self.old_tag["original_map_index"] == 4 and self.old_tag["original_map_degree"] == "1206"
        assert self.old_tag["ordinary_power"] == 5 and self.old_tag["basis_dimension"] == N
        assert self.old_tag["qY_bound"] == 128 and self.old_tag["Laurent_exponents"] == [-1, 127]
        assert self.old_tag["full_L_unknown_dimension_over_Q"] == LD
        assert self.old_tag["t_coordinates"] == TD
        self.tag = dict(self.old_tag)
        self.tag.update({
            "result": RESULT, "source_sha256": sha(__file__),
            "projective_mode": True, "projective_algorithm": ALGORITHM,
            "projective_method_sha256": sha(args.method),
            "pinned_R787_configuration_sha256": OLD_TAG,
            "retained_source": self.item["retained_source"],
            "checkpoint": checkpoint,
            "search_rectangle_shifts": list(SHIFTS),
            "LLL_integer_lattice_dimension": 28,
            "LLL_child_limit_per_node": CHILD_LIMIT,
            "LLL_weight_formula": "wd=2^(2max(shift,0)), wn=2^(2max(-shift,0))",
            "search_chunk_rows": CHUNK,
            "original_lifting_reexecuted": False,
            "old_branch_inverse_used": False})
        assert self.chart["prime"] == PRIME and self.chart["actual_modular_rank"] == 1186
        assert self.chart["other_free_columns_set_to_zero"] is True
        self.pivots = [int(x) for x in self.chart["pivot_columns"]]
        assert len(self.pivots) == len(set(self.pivots)) == 1186
        assert all(0 <= x < NC for x in self.pivots)
        self.free = int(self.chart["chosen_free_column"])
        self.free_columns = [j for j in range(NC) if j not in set(self.pivots)]
        assert self.free in self.free_columns and len(self.free_columns) == 28
        self.selection = self.source.stage(checkpoint["selection_file"])
        assert self.selection["prime"] == PRIME and self.selection["prime_proved"] is True
        assert self.selection["all_14_L_branches_distinct"] is True
        assert self.selection["all_rational_denominators_units"] is True
        assert self.selection["all_kappa_reductions_invertible"] is True
        self.roots = [tuple(int(x) for x in pair) for pair in self.selection["roots_B_s"]]
        assert len(self.roots) == len(set(self.roots)) == 14
        blocks = self.source.stage(checkpoint["rational_blocks_file"])
        assert blocks["prime"] == PRIME and blocks["exact_E0_Z_zero_verified"] is True
        assert blocks["A_minor_det_mod_prime"] and blocks["B_constant_minor_det_mod_prime"]
        self.ZP, self.ZQ = list(blocks["B_constant_pivot_columns"]), list(blocks["B_constant_free_columns"])
        assert len(self.ZP) == 20 and len(self.ZQ) == NC
        assert sorted(self.ZP+self.ZQ) == list(range(N))
        self.Zp = fmpz_mat(integer_rows(blocks["Z_pivot_integer_rows"], 20, NC))
        self.Zd = int(blocks["Z_free_diagonal"])
        assert self.Zd > 0 and self.Zd % PRIME
        del blocks  # Its old A inverse is never used.
        lift = self.source.stage(checkpoint["lift_file"])
        assert lift["prime"] == PRIME and lift["digits"] == DIGITS
        self.modulus = int(lift["modulus"])
        assert self.modulus == PRIME**DIGITS
        assert lift["chart_sha256"] == self.source.files[checkpoint["chart_file"]]["sha256"]
        assert lift["full_original_modular_relations_verified"] is True
        self.a_lift = integer_rows(lift["A_L_coordinates"], N, LD)
        self.c_lift = integer_rows(lift["C_L_coordinates"], NC, LD)
        assert all(0 <= x < self.modulus for matrix in (self.a_lift, self.c_lift) for row in matrix for x in row)
        assert self.c_lift[self.free] == [1]+[0]*13
        assert all(self.c_lift[j] == [0]*14 for j in self.free_columns if j != self.free)
        del lift
        self.children = {}
        for label in ("R781", "R786"):
            spec = self.old_tag["retained_artifacts"][label]
            expected = CHILD_EXPECTED[label]
            assert spec["result"] == expected["result"]
            assert spec["manifest_sha256"] == expected["manifest"]
            assert spec["core_sha256"] == expected["core"]
            child = Source(args.retained/label, spec)
            certificate = child.raw(spec["certificate_name"])
            assert child.files[spec["certificate_name"]]["sha256"] == expected["certificate"]
            assert certificate["result"] == expected["result"] and certificate["complete"] is True
            child.tag = certificate["configuration"]
            assert child.tag["source_sha256"] == expected["core"]
            child.certificate = certificate
            self.children[label] = child
        self.r781, self.r786 = self.children["R781"], self.children["R786"]
        module_spec = importlib.util.spec_from_file_location("frozen_R781_projective_field", args.field_core)
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        field_input = self.r781.stage("R781-original-real-field-input.json.gz")
        self.f = module.Field(field_input["field"]["original_b_minimal_polynomial"])
        assert self.f.description == field_input["field"] == self.old_tag["field"]
        self.order = IntegralOrder(self.f.description["integral_B_minimal_polynomial"])
        self.R, self.K = [], []
        prior = None
        for n in range(130):
            self.budget()
            name = "R781-inverse-free-Laurent-"+str(n).zfill(3)+".json.gz"
            row = self.r781.stage(name)
            assert row["order"] == n and row["exact_differential_identity_at_this_order"] is True
            if prior is None:
                assert row["input_stage_sha256"] == self.r781.files["R781-original-real-field-input.json.gz"]["sha256"]
                self.kappa = self.f.decode(row["kappa"])
            else:
                assert row["previous_stage_sha256"] == self.r781.files[prior]["sha256"]
            self.K.append(self.f.decode(row["coefficients"]["kappa_power"]))
            if n < ORDERS:
                self.R.append(self.f.decode(row["coefficients"]["R"]))
            prior = name
        assert self.K[0] == self.f.one and self.K[1] == self.kappa and self.R[0] == self.f.one
        cert = self.r786.certificate
        assert cert["exact_power5_basis_dimension"] == N and cert["exact_K_basis_prefix_bound_qY"] == 128
        assert cert["basis_integer_scale"] == self.tag["basis_integer_scale"]
        self.index_spec = cert["basis_index"]
        assert self.r786.files[self.index_spec["file"]]["sha256"] == self.index_spec["sha256"]
        self.index = self.r786.stage(self.index_spec["file"])
        assert self.index["dimension"] == N and self.index["bound_qY"] == 128
        assert len(self.index["basis_rows"]) == N
        columns, real_specs = [], []
        for i, spec in enumerate(self.index["basis_rows"]):
            self.budget()
            assert spec["index"] == i
            assert self.r786.files[spec["file"]]["sha256"] == spec["sha256"]
            name = "R787-real-power5-row-"+str(i).zfill(4)+".json.gz"
            row = self.source.stage(name)
            assert row["index"] == i and row["R786_row_sha256"] == spec["sha256"]
            assert row["all_original_phase_involutions_verified"] is True and row["averaging_used"] is False
            values = integer_rows(row["integer_t_coefficients"], ORDERS, TD)
            columns.append([x for vector in values for x in vector])
            real_specs.append(self.source.ref(name))
        self.F = fmpz_mat([list(row) for row in zip(*columns)])
        del columns
        assert self.F.nrows() == ORDERS*TD and self.F.ncols() == N
        audit = self.cache(PREFIX+"source-audit")
        if audit is None:
            audit = self.store(PREFIX+"source-audit", {
                "original_R787_configuration_sha256": OLD_TAG,
                "checkpoint": {key: self.source.ref(checkpoint[key]) for key in
                    ("lift_file", "chart_file", "rational_blocks_file", "selection_file")},
                "real_rows": real_specs, "real_row_count": N,
                "R781_used_files": [self.r781.ref(name) for name in sorted(self.r781.used)],
                "R786_used_files": [self.r786.ref(name) for name in sorted(self.r786.used)],
                "basis_integer_scale": self.tag["basis_integer_scale"],
                "all_original_source_bytes_SHA_and_mathematical_tags_verified": True,
                "old_mathematics_recomputed": False})
        self.audit_spec = file_spec(self.path(PREFIX+"source-audit"))
        arithmetic = self.cache(PREFIX+"integral-order-and-rectangles")
        if arithmetic is None:
            constant = self.order.multiplication_bound()
            base = math.isqrt((self.modulus-1)//(2*constant))
            rectangles = []
            for shift in SHIFTS:
                if shift >= 0:
                    upper_n, upper_d = base << shift, base >> shift
                else:
                    upper_n, upper_d = base >> (-shift), base << (-shift)
                if upper_n and upper_d and max(upper_n, upper_d) < self.modulus//2:
                    assert 2*constant*upper_n*upper_d < self.modulus
                    rectangles.append({"shift": shift, "numerator_bound": str(upper_n),
                                       "denominator_bound": str(upper_d)})
            self.store(PREFIX+"integral-order-and-rectangles", {
                "multiplication_constant": str(constant),
                "formula": "max(1,max_k sum_ij abs(mu_ij^k)); s^2=-3; original monic fB",
                "rectangles": rectangles,
                "fixed_rectangle_cross_product_uniqueness_verified": True,
                "actual_solution_height_bound_claimed": False})
        arithmetic = self.cache(PREFIX+"integral-order-and-rectangles")
        self.rectangles = arithmetic["rectangles"]
        constant = int(arithmetic["multiplication_constant"])
        for rect in self.rectangles:
            upper_n, upper_d = int(rect["numerator_bound"]), int(rect["denominator_bound"])
            assert min(upper_n, upper_d) > 0
            assert 2*constant*upper_n*upper_d < self.modulus
            assert max(upper_n, upper_d) < self.modulus//2
        self.maximum_nodes = int(self.item.get("projective_search_controls", {}).get("maximum_nodes", 96))
        assert self.maximum_nodes >= 1

    def budget(self):
        if time.monotonic()-self.started >= self.args.budget_minutes*60:
            raise BudgetStop("Projective budget reached; complete nodes and current queue are retained.")

    def path(self, name):
        assert Path(name).name == name
        return self.out/(name if name.endswith(".json.gz") else name+".json.gz")

    def cache(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        obj = read(path)
        assert obj["result"] == RESULT and obj["configuration"] == self.tag
        assert obj["complete"] is True
        return obj

    def store(self, name, value):
        obj = {"result": RESULT, "configuration": self.tag, "complete": True}
        obj.update(value)
        assert obj["complete"] is True and obj["configuration"] == self.tag
        save(self.path(name), obj)
        return obj

    def reference(self, name):
        return file_spec(self.path(name))

    def ell_unit(self, value):
        return all(sum(value[7*j+i]*pow(b, i, PRIME)*pow(s, j, PRIME)
                       for j in range(2) for i in range(7)) % PRIME for b, s in self.roots)

    def node(self, rectangle_index, denominator, parent=None):
        denominator = list(denominator)
        assert any(denominator)
        first = next(x for x in denominator if x)
        if first < 0:
            denominator = [-x for x in denominator]
        data = {"rectangle_index": rectangle_index,
                "denominator": [str(x) for x in denominator]}
        identity = fingerprint(data)
        data.update({"id": identity, "parent_node_id": parent})
        return data

    def node_prefix(self, node):
        return PREFIX+"node-"+node["id"]

    def load_state(self):
        path = self.path(PREFIX+"search-current")
        if path.exists():
            obj = read(path)
            assert obj["configuration"] == self.tag and obj["result"] == RESULT
            assert obj["complete"] is False
            assert len(obj["seen_node_ids"]) == len(set(obj["seen_node_ids"]))
            assert len(obj["processed_node_ids"]) == len(set(obj["processed_node_ids"]))
            return obj
        frontier = [self.node(i, [1]+[0]*13) for i in range(len(self.rectangles))]
        obj = {"result": RESULT, "configuration": self.tag, "complete": False,
               "frontier": frontier, "seen_node_ids": [x["id"] for x in frontier],
               "processed_node_ids": [], "finite_search_exhausted": not frontier}
        save(path, obj)
        return obj

    def save_state(self, state):
        assert state["configuration"] == self.tag and state["complete"] is False
        save(self.path(PREFIX+"search-current"), state)

    def source_row(self, global_index):
        assert 0 <= global_index < NC+N
        return self.c_lift[global_index] if global_index < NC else self.a_lift[global_index-NC]

    def scan(self, node):
        prefix = self.node_prefix(node)
        old = self.cache(prefix+"-scan")
        if old is not None:
            return old
        denominator = [int(x) for x in node["denominator"]]
        rect = self.rectangles[node["rectangle_index"]]
        upper_n, upper_d = int(rect["numerator_bound"]), int(rect["denominator_bound"])
        assert any(denominator) and max(abs(x) for x in denominator) <= upper_d
        assert self.ell_unit(denominator)
        chunks, maximum_bits = [], 0
        for first in range(0, NC+N, CHUNK):
            self.budget()
            last = min(first+CHUNK, NC+N)
            name = prefix+"-scan-chunk-"+str(first//CHUNK).zfill(4)
            data = self.cache(name)
            if data is None:
                rows, failure = [], None
                for index in range(first, last):
                    value = self.order.centered_product(denominator, self.source_row(index), self.modulus)
                    if index in self.free_columns:
                        assert value == (denominator if index == self.free else [0]*LD)
                    if max(abs(x) for x in value) > upper_n:
                        failure = {"global_index": index, "source_kind": "C" if index < NC else "A",
                                   "source_row": index if index < NC else index-NC,
                                   "centered_probe_L_coordinates": [str(x) for x in value]}
                        break
                    rows.append([str(x) for x in value])
                self.store(name, {
                    "node_id": node["id"], "denominator": node["denominator"],
                    "rectangle_index": node["rectangle_index"],
                    "first_global_index": first, "requested_end": last,
                    "accepted_numerator_rows": rows, "first_failure": failure,
                    "all_products_use_original_integral_L_multiplication": True,
                    "all_accepted_coordinates_in_fixed_rectangle": True})
                data = self.cache(name)
            assert data["node_id"] == node["id"] and data["denominator"] == node["denominator"]
            assert data["first_global_index"] == first and data["requested_end"] == last
            rows = data["accepted_numerator_rows"]
            assert all(len(row) == LD for row in rows)
            maximum_bits = max(maximum_bits, max(
                (abs(int(x)).bit_length() for row in rows for x in row), default=0))
            chunks.append(self.reference(name))
            if data["first_failure"] is not None:
                failure = data["first_failure"]
                assert failure["global_index"] == first+len(rows) < last
                self.store(prefix+"-scan", {
                    "node_id": node["id"], "rectangle_index": node["rectangle_index"],
                    "denominator": node["denominator"], "all_numerators_in_bound": False,
                    "accepted_prefix_length": failure["global_index"], "failure": failure,
                    "scan_chunks": chunks, "maximum_accepted_numerator_bits": maximum_bits,
                    "no_characteristic_zero_relation_claimed": True})
                return self.cache(prefix+"-scan")
            assert len(rows) == last-first
        self.store(prefix+"-scan", {
            "node_id": node["id"], "rectangle_index": node["rectangle_index"],
            "denominator": node["denominator"], "all_numerators_in_bound": True,
            "accepted_prefix_length": NC+N, "failure": None,
            "scan_chunks": chunks, "maximum_accepted_numerator_bits": maximum_bits,
            "candidate_only_until_full_exact_verification": True})
        return self.cache(prefix+"-scan")

    def children_for(self, node, scan):
        prefix = self.node_prefix(node)
        name = prefix+"-LLL-children"
        old = self.cache(name)
        if old is not None:
            return old["children"]
        self.budget()
        assert scan["all_numerators_in_bound"] is False
        probe = [int(x) for x in scan["failure"]["centered_probe_L_coordinates"]]
        assert len(probe) == LD
        rect = self.rectangles[node["rectangle_index"]]
        shift = int(rect["shift"])
        weight_d = 1 << (2*max(shift, 0))
        weight_n = 1 << (2*max(-shift, 0))
        rows = self.order.multiplication_rows(probe, self.modulus)
        rows = [[x-self.modulus if x > self.modulus//2 else x for x in row] for row in rows]
        lattice_rows = []
        for i in range(LD):
            lattice_rows.append([weight_d*int(i == j) for j in range(LD)]
                                +[weight_n*x for x in rows[i]])
        for i in range(LD):
            lattice_rows.append([0]*LD+[weight_n*self.modulus*int(i == j) for j in range(LD)])
        lattice = fmpz_mat(lattice_rows)
        reduced = lattice.lll(delta=0.99, eta=0.51)
        assert reduced.nrows() == reduced.ncols() == 2*LD
        candidates, rejected = [], {"zero_delta": 0, "nonunit_delta": 0,
                                   "denominator_bound": 0, "unchanged_or_duplicate": 0}
        denominator = [int(x) for x in node["denominator"]]
        upper_d = int(rect["denominator_bound"])
        seen = {node["id"]}
        order = sorted(range(2*LD), key=lambda i: sum(int(reduced[i,j])**2 for j in range(2*LD)))
        for index in order:
            row = [int(reduced[index,j]) for j in range(2*LD)]
            assert all(x % weight_d == 0 for x in row[:LD])
            assert all(x % weight_n == 0 for x in row[LD:])
            delta, numerator = [x//weight_d for x in row[:LD]], [x//weight_n for x in row[LD:]]
            product = self.order.multiply(delta, probe)
            assert all((x-y) % self.modulus == 0 for x, y in zip(product, numerator))
            if not any(delta):
                rejected["zero_delta"] += 1
                continue
            if not self.ell_unit(delta):
                rejected["nonunit_delta"] += 1
                continue
            # Do not center this product: it is the exact candidate scale in O.
            new_denominator = self.order.multiply(denominator, delta)
            assert any(new_denominator)
            if max(abs(x) for x in new_denominator) > upper_d:
                rejected["denominator_bound"] += 1
                continue
            row_sign = 1
            if next(x for x in new_denominator if x) < 0:
                row_sign = -1
                new_denominator = [-x for x in new_denominator]
                delta, numerator = [-x for x in delta], [-x for x in numerator]
            child = self.node(node["rectangle_index"], new_denominator, node["id"])
            if child["id"] in seen:
                rejected["unchanged_or_duplicate"] += 1
                continue
            seen.add(child["id"])
            candidates.append({
                "node": child, "LLL_row": index, "LLL_row_sign": row_sign,
                "delta_integer_L_coordinates": [str(x) for x in delta],
                "probe_numerator_integer_L_coordinates": [str(x) for x in numerator],
                "exact_congruence_verified": True,
                "new_scale_is_exact_integral_product_not_centered_modulus": True})
        kept = candidates[:CHILD_LIMIT]
        self.store(name, {
            "node_id": node["id"], "scan_sha256": sha(self.path(prefix+"-scan")),
            "lattice_dimension": 28, "weights": [str(weight_d), str(weight_n)],
            "lattice_input_sha256": fingerprint(strings(lattice_rows)),
            "all_28_reduced_rows_exact_congruences_checked": True,
            "LLL_is_only_candidate_generation": True,
            "rejected_counts": rejected, "admissible_candidates": len(candidates),
            "retained_candidate_witnesses": kept,
            "children": [x["node"] for x in kept],
            "no_LLL_success_or_height_guarantee_claimed": True})
        return [x["node"] for x in kept]

    def accepted_numerators(self, node, scan):
        assert scan["all_numerators_in_bound"] is True
        answer = []
        for spec in scan["scan_chunks"]:
            self.budget()
            assert self.reference(spec["file"]) == spec
            data = self.cache(spec["file"])
            assert data["node_id"] == node["id"] and data["first_failure"] is None
            assert data["first_global_index"] == len(answer)
            answer.extend(integer_rows(data["accepted_numerator_rows"],
                                       data["requested_end"]-data["first_global_index"], LD))
        assert len(answer) == NC+N
        cc, aa = answer[:NC], answer[NC:]
        denominator = [int(x) for x in node["denominator"]]
        assert cc[self.free] == denominator and any(denominator)
        assert all(cc[j] == [0]*LD for j in self.free_columns if j != self.free)
        return aa, cc

    def expand_B(self, cc):
        pivot_rows = self.Zp*fmpz_mat(cc)
        result = [[0]*LD for _ in range(N)]
        for j, target in enumerate(self.ZP):
            result[target] = [int(pivot_rows[j,k]) for k in range(LD)]
        for j, target in enumerate(self.ZQ):
            result[target] = [self.Zd*x for x in cc[j]]
        return result

    def candidate_recipe(self, node, scan):
        name = self.node_prefix(node)+"-candidate"
        cached = self.cache(name)
        if cached is not None:
            assert cached["node_id"] == node["id"]
            return name, cached
        aa, cc = self.accepted_numerators(node, scan)
        bb = self.expand_B(cc)
        assert any(x for row in bb for x in row)
        content = 0
        for row in aa+bb:
            for value in row:
                content = math.gcd(content, value)
        assert content > 0
        aa = [[x//content for x in row] for row in aa]
        bb = [[x//content for x in row] for row in bb]
        denominator = [int(x) for x in node["denominator"]]
        recipe = {
            "node_id": node["id"], "source_scan": self.reference(self.node_prefix(node)+"-scan"),
            "field": self.f.description,
            "L_basis": "B^i*s^j, j=0..1 outer, i=0..6; B=lambda*b",
            "original_R786_basis_order": True,
            "basis_integer_scale": self.tag["basis_integer_scale"],
            "R786_producer": self.tag["retained_artifacts"]["R786"],
            "R786_basis_index": self.index_spec,
            "A_integer_L_coordinates": strings(aa),
            "B_integer_L_coordinates": strings(bb),
            "common_rational_denominator_cleared": "1",
            "common_rational_denominator_field_applies_after_algebraic_scaling": True,
            "common_integer_content_removed": str(content),
            "algebraic_L_denominator_before_content": {
                "integer_L_coordinates": [str(x) for x in denominator],
                "rational_scale": ["1", "1"]},
            "algebraic_L_scale_after_content": {
                "integer_L_coordinates": [str(x) for x in denominator],
                "rational_scale": ["1", str(content)]},
            "rational_reconstruction_modulus": str(self.modulus),
            "projective_mode": True,
            "source_Dixon_digits": DIGITS,
            "source_lift": self.source.ref(self.item["checkpoint"]["lift_file"]),
            "source_chart": self.source.ref(self.item["checkpoint"]["chart_file"]),
            "source_Z": self.source.ref(self.item["checkpoint"]["rational_blocks_file"]),
            "chosen_free_column": self.free,
            "free_C_column_equals_exact_algebraic_scale_before_content": True,
            "all_other_free_C_columns_zero_before_content": True,
            "Z_expansion_used_before_common_integer_content_removal": True,
            "candidate_only_until_full_exact_verification": True}
        self.store(name, recipe)
        return name, self.cache(name)

    def exact_verification(self, node, scan):
        name, recipe = self.candidate_recipe(node, scan)
        candidate_sha = sha(self.path(name))
        rejected_name = self.node_prefix(node)+"-exact-rejected"
        rejected = self.cache(rejected_name)
        if rejected is not None:
            assert rejected["candidate_sha256"] == candidate_sha
            return None
        aa = fmpz_mat(integer_rows(recipe["A_integer_L_coordinates"], N, LD))
        bb = fmpz_mat(integer_rows(recipe["B_integer_L_coordinates"], N, LD))
        weighted, previous_a = [], None
        relations = []
        for m in range(ORDERS):
            self.budget()
            expansion_name = self.node_prefix(node)+"-exact-expansion-"+str(m).zfill(3)
            expansion = self.cache(expansion_name)
            if expansion is None:
                band = fmpz_mat([[self.F[TD*m+r, i] for i in range(N)] for r in range(TD)])
                av, bv = band*aa, band*bb
                value_a = self.f.from_vector([av[r,i] for i in range(LD) for r in range(TD)], 1)
                value_b = self.f.from_vector([bv[r,i] for i in range(LD) for r in range(TD)], 1)
                value_weighted = self.f.multiply(self.K[m], value_b)
                self.store(expansion_name, {
                    "candidate_sha256": candidate_sha, "order": m,
                    "A_coefficient": self.f.encode(value_a),
                    "B_coefficient": self.f.encode(value_b),
                    "kappa_power_times_B": self.f.encode(value_weighted),
                    "original_82_power10_scale_preserved": True})
                expansion = self.cache(expansion_name)
            assert expansion["candidate_sha256"] == candidate_sha and expansion["order"] == m
            value_a = self.f.decode(expansion["A_coefficient"])
            weighted.append(self.f.decode(expansion["kappa_power_times_B"]))
            verify_name = self.node_prefix(node)+"-exact-verification-"+str(m).zfill(3)
            verification = self.cache(verify_name)
            if verification is None:
                total = self.f.zero
                for j in range(m+1):
                    if weighted[j] and self.R[m-j]:
                        total += self.f.multiply(self.R[m-j], weighted[j])
                if m:
                    assert previous_a is not None
                    total += self.f.multiply(self.K[m+1], previous_a).scaled(246**3)
                if total:
                    self.store(rejected_name, {
                        "node_id": node["id"], "candidate_sha256": candidate_sha,
                        "first_nonzero_relation_order": m,
                        "exact_nonzero_residual": self.f.encode(total),
                        "not_a_characteristic_zero_relation": True,
                        "no_original_function_recovery_claimed": True})
                    return None
                self.store(verify_name, {
                    "candidate_sha256": candidate_sha,
                    "relation_index": m, "Laurent_exponent": m-1,
                    "all_280_Q_coordinates_zero": True,
                    "all_20_L_coordinates_zero": True})
                verification = self.cache(verify_name)
            assert verification["candidate_sha256"] == candidate_sha
            assert verification["relation_index"] == m and verification["all_280_Q_coordinates_zero"] is True
            relations.append(self.reference(verify_name))
            previous_a = value_a
        successful = dict(recipe)
        for key in ("result", "configuration", "complete"):
            successful.pop(key, None)
        successful.update({
            "candidate_only_until_full_exact_verification": False,
            "candidate_sha256": candidate_sha,
            "exact_original_A_equals_yB": True, "B_nonzero": True,
            "full_129_original_relations_verified": True,
            "same_normalized_1186_direction_verified": True,
            "same_direction_uses_original_unit_minor_and_free_pattern": True,
            "exact_relation_stages": relations})
        self.store(RECIPE, successful)
        return self.reference(RECIPE)

    def process_node(self, node):
        identity_data = {"rectangle_index": node["rectangle_index"], "denominator": node["denominator"]}
        assert fingerprint(identity_data) == node["id"]
        assert 0 <= node["rectangle_index"] < len(self.rectangles)
        name = self.node_prefix(node)+"-result"
        old = self.cache(name)
        if old is not None:
            assert old["node_id"] == node["id"]
            return old
        scan = self.scan(node)
        if scan["all_numerators_in_bound"]:
            relation = self.exact_verification(node, scan)
            outcome = {
                "node_id": node["id"], "all_numerators_in_fixed_rectangle": True,
                "exact_relation_found": relation is not None,
                "relation_spec": relation, "children": [],
                "same_normalized_direction_claimed_only_if_exact": True}
        else:
            children = self.children_for(node, scan)
            outcome = {
                "node_id": node["id"], "all_numerators_in_fixed_rectangle": False,
                "exact_relation_found": False, "relation_spec": None,
                "accepted_prefix_length": scan["accepted_prefix_length"],
                "children": children,
                "finite_search_candidate_not_a_nonexistence_certificate": True}
        self.store(name, outcome)
        return self.cache(name)

    def stage_inventory(self):
        name = PREFIX+"exact-stages-manifest"
        items = []
        for path in sorted(self.out.iterdir()):
            if not path.is_file() or path.name == name+".json.gz":
                continue
            if not ((path.name.startswith(PREFIX) and path.name.endswith(".json.gz")) or path.name == RECIPE):
                continue
            obj = read(path)
            assert obj["configuration"] == self.tag and obj["result"] == RESULT
            assert isinstance(obj["complete"], bool)
            if obj["complete"]:
                items.append(file_spec(path))
        self.store(name, {"files": items})
        return self.reference(name)

    def final_certificate(self, complete, state, relation=None):
        stage_manifest = self.stage_inventory()
        certificate = {
            "result": RESULT, "configuration": self.tag, "complete": bool(complete),
            "projective_mode": True, "p": 41,
            "original_map_index": 4, "original_map_degree": "1206",
            "original_full_L_retained": True,
            "exact_nonzero_A_B_relation_verified": bool(complete),
            "same_normalized_1186_direction_verified": bool(complete),
            "exact_verified_Laurent_exponents": [-1, 127] if complete else None,
            "exact_verified_t_coordinates": TD if complete else 0,
            "exact_verified_Q_coordinates_per_order": LD*TD if complete else 0,
            "exact_verified_orders": ORDERS if complete else 0,
            "actual_y_map_recovered": bool(complete),
            "beta_or_height_computed": False,
            "relation_spec": relation, "function_recipe": relation,
            "actual_auxiliary_prime": PRIME, "actual_modular_Schur_rank": 1186,
            "characteristic_zero_Schur_rank": 1186,
            "full_characteristic_zero_kernel_claimed": False,
            "actual_Dixon_digits": DIGITS, "additional_Dixon_digits_computed": 0,
            "original_source": self.item["retained_source"],
            "source_audit": self.audit_spec,
            "composite_modulus_matrix_inversion": False,
            "LLL_success_guarantee_claimed": False,
            "candidate_search_exhausted": not state["frontier"] and not complete,
            "search_node_budget_reached": bool(state["frontier"]) and not complete,
            "completed_search_nodes": len(state["processed_node_ids"]),
            "remaining_search_nodes": len(state["frontier"]),
            "stage_manifest": stage_manifest,
            "resume_state": self.reference(PREFIX+"search-current"),
            "seconds": time.monotonic()-self.started}
        save(self.out/FINAL, certificate)
        return certificate

    def complete(self):
        final = self.out/FINAL
        if final.exists():
            certificate = read(final)
            assert certificate["configuration"] == self.tag and certificate["result"] == RESULT
            if certificate["complete"]:
                assert certificate["same_normalized_1186_direction_verified"] is True
                spec = certificate["stage_manifest"]
                assert self.reference(spec["file"]) == spec
                inventory = self.cache(spec["file"])
                for item in inventory["files"]:
                    assert self.reference(item["file"]) == item
                return certificate
        state = self.load_state()
        existing = self.cache(RECIPE)
        if existing is not None:
            assert existing["candidate_only_until_full_exact_verification"] is False
            assert existing["full_129_original_relations_verified"] is True
            assert existing["same_normalized_1186_direction_verified"] is True
            # A hard exit may have happened after the recipe but before its node
            # or queue was finalized.  The recipe itself is a complete boundary.
            return self.final_certificate(True, state, self.reference(RECIPE))
        while state["frontier"] and len(state["processed_node_ids"]) < self.maximum_nodes:
            self.budget()
            node = state["frontier"][0]
            outcome = self.process_node(node)
            next_frontier = state["frontier"][1:]
            seen = set(state["seen_node_ids"])
            for child in outcome["children"]:
                if child["id"] not in seen:
                    seen.add(child["id"])
                    next_frontier.append(child)
            state["frontier"] = next_frontier
            state["seen_node_ids"] = sorted(seen)
            assert node["id"] not in state["processed_node_ids"]
            state["processed_node_ids"].append(node["id"])
            state["finite_search_exhausted"] = not next_frontier
            self.save_state(state)
            print("PROJECTIVE_NODE="+json.dumps({
                "node_id": node["id"], "rectangle": node["rectangle_index"],
                "accepted_prefix_length": outcome.get("accepted_prefix_length", NC+N),
                "exact_relation_found": outcome["exact_relation_found"],
                "completed_nodes": len(state["processed_node_ids"]),
                "remaining_nodes": len(next_frontier)}), flush=True)
            if outcome["exact_relation_found"]:
                return self.final_certificate(True, state, outcome["relation_spec"])
        return self.final_certificate(False, state)


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New exact arithmetic belongs to public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "method", "field-core", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    try:
        job = Job(args)
        certificate = job.complete()
        complete = certificate["complete"]
        receipt = {
            "result": RESULT, "projective_mode": True, "complete": complete,
            "source_sha256": sha(__file__),
            "certificate_sha256": sha(args.output/FINAL),
            "actual_y_map_recovered": complete, "beta_or_height_computed": False,
            "same_normalized_1186_direction_verified": complete,
            "exact_verified_orders": ORDERS if complete else 0,
            "exact_verified_t_coordinates": TD if complete else 0,
            "source_Dixon_digits": DIGITS, "additional_Dixon_digits_computed": 0,
            "candidate_search_exhausted": certificate["candidate_search_exhausted"],
            "search_node_budget_reached": certificate["search_node_budget_reached"],
            "all_completed_stages_preserved": True,
            "seconds": time.monotonic()-started}
        save(args.output/"core-receipt.json", receipt)
        print("PROJECTIVE_CORE_RECEIPT="+json.dumps(receipt), flush=True)
        return 0 if complete else 2
    except BaseException as error:
        receipt = {
            "result": RESULT, "projective_mode": True, "complete": False,
            "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error),
            "all_completed_stages_preserved": True,
            "actual_y_map_recovered": False, "beta_or_height_computed": False,
            "source_Dixon_digits": DIGITS, "additional_Dixon_digits_computed": 0,
            "seconds": time.monotonic()-started}
        save(args.output/"core-receipt.json", receipt)
        print("PROJECTIVE_CORE_RECEIPT="+json.dumps(receipt), flush=True)
        if isinstance(error, BudgetStop):
            return 124
        raise


if __name__ == "__main__":
    sys.exit(main())
