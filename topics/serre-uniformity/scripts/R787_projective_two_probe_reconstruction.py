#!/usr/bin/env python3
"""Direct two-probe projective reconstruction of the original R787 relation.

New arithmetic runs only in the public repository Actions.  The frozen 430-digit
lift and every old mathematical stage are read as inputs.  New 42-dimensional LLL problems
generate candidates without a denominator-height acceptance bound; only the complete original 129-by-280 characteristic-zero
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
PROBE_PAIRS = ((0, 1), (0, 2), (1, 2), (0, NC), (1, NC), (NC, NC+1))
ALGORITHM = "integral-L-direct-two-probe-42-lattice-v2"
PREVIOUS_SEARCH = {
    "run_id": "43745966802",
    "source_commit": "d71d40bb6cbea1cecc9c23f2efd47401da35cc53",
    "core_sha256": "e0a5ad95b06bbd75319b1464f5c1b629d3f64d919758fbe7e0a76ad3c41963cb",
    "manifest_sha256": "422319cdb4ecdaaa54dfa5231855a4ae32cb72e67e1331bb51855876a72b9192",
    "certificate_sha256": "380717ae1b382198ed282e72e2e20c9180a926d5d63d4a62f1e35594f8ccedd5",
    "actual_all_five_28_row_searches_rejected_only_by_denominator_bound": True,
    "previous_reduced_rows_not_retained_and_not_recomputed": True}
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
            "probe_pair_schedule_C_then_A": [list(pair) for pair in PROBE_PAIRS],
            "LLL_integer_lattice_dimension": 42,
            "LLL_three_integer_weights": [1, 1, 1],
            "all_42_reduced_rows_retained": True,
            "denominator_height_or_unique_rectangle_is_acceptance_condition": False,
            "direct_original_normalized_probes_without_denominator_multiplication": True,
            "actual_free_coordinate_equals_unreduced_candidate_D": True,
            "previous_ended_search": PREVIOUS_SEARCH,
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
        controls = self.item.get("projective_search_controls", {})
        self.maximum_nodes = int(controls.get("maximum_nodes", 42))
        self.maximum_lattices = int(controls.get("maximum_lattices", 1))
        assert self.maximum_nodes >= 1 and 1 <= self.maximum_lattices <= len(PROBE_PAIRS)

    def budget(self):
        if time.monotonic()-self.started >= self.args.budget_minutes*60:
            raise BudgetStop("Two-probe budget reached; full LLL rows, complete decisions and current candidate are retained.")

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

    def node(self, denominator, pair_index, reduced_row, row_sign):
        denominator = list(denominator)
        assert len(denominator) == LD and any(denominator)
        assert next(x for x in denominator if x) > 0
        identity_data = {"denominator": [str(x) for x in denominator]}
        return dict(identity_data, id=fingerprint(identity_data),
                    source_probe_pair_index=pair_index,
                    source_LLL_row=reduced_row, source_LLL_row_sign=row_sign)

    def node_prefix(self, node):
        return PREFIX+"candidate-"+node["id"]

    def load_state(self):
        path = self.path(PREFIX+"search-current")
        if path.exists():
            obj = read(path)
            assert obj["configuration"] == self.tag and obj["result"] == RESULT
            assert obj["complete"] is False
            assert 0 <= obj["probe_pair_index"] <= len(PROBE_PAIRS)
            assert obj["next_candidate_position"] >= 0
            assert len(obj["processed_node_ids"]) == len(set(obj["processed_node_ids"]))
            assert len(obj["completed_lattice_indices"]) == len(set(obj["completed_lattice_indices"]))
            return obj
        obj = {"result": RESULT, "configuration": self.tag, "complete": False,
               "probe_pair_index": 0, "next_candidate_position": 0,
               "processed_node_ids": [], "completed_lattice_indices": [],
               "consumed_LLL_candidate_rows": 0, "finite_search_exhausted": False}
        save(path, obj)
        return obj

    def save_state(self, state):
        assert state["configuration"] == self.tag and state["complete"] is False
        save(self.path(PREFIX+"search-current"), state)

    def source_row(self, global_index):
        assert 0 <= global_index < NC+N
        return self.c_lift[global_index] if global_index < NC else self.a_lift[global_index-NC]

    def probe_spec(self, index):
        return {"global_index": index, "source_kind": "C" if index < NC else "A",
                "source_row": index if index < NC else index-NC}

    def lattice_name(self, pair_index):
        return PREFIX+"pair-"+str(pair_index).zfill(3)+"-two-probe-LLL"

    def lattice(self, pair_index):
        name = self.lattice_name(pair_index)
        cached = self.cache(name)
        if cached is not None:
            assert cached["probe_pair_index"] == pair_index
            assert cached["probe_indices_C_then_A"] == list(PROBE_PAIRS[pair_index])
            assert cached["all_42_reduced_rows_saved"] is True
            return cached
        self.budget()
        indices = PROBE_PAIRS[pair_index]
        assert len(indices) == 2 and indices[0] != indices[1]
        probes = [self.source_row(i) for i in indices]
        blocks = [self.order.multiplication_rows(value, self.modulus) for value in probes]
        blocks = [[[x-self.modulus if x > self.modulus//2 else x for x in row]
                   for row in block] for block in blocks]
        rows = []
        for i in range(LD):
            rows.append([int(i == j) for j in range(LD)]+blocks[0][i]+blocks[1][i])
        for i in range(LD):
            rows.append([0]*LD+[self.modulus*int(i == j) for j in range(LD)]+[0]*LD)
        for i in range(LD):
            rows.append([0]*(2*LD)+[self.modulus*int(i == j) for j in range(LD)])
        reduced = fmpz_mat(rows).lll(delta=0.99, eta=0.51)
        assert reduced.nrows() == reduced.ncols() == 3*LD
        reduced_rows = [[int(reduced[i,j]) for j in range(3*LD)] for i in range(3*LD)]
        order = sorted(range(3*LD), key=lambda i: (sum(x*x for x in reduced_rows[i]), i))
        candidates, diagnostics, seen = [], [], set()
        for index in order:
            row = reduced_rows[index]
            denominator, nums = row[:LD], [row[LD:2*LD], row[2*LD:]]
            for probe, numerator in zip(probes, nums):
                product = self.order.multiply(denominator, probe)
                assert all((x-y) % self.modulus == 0 for x, y in zip(product, numerator))
            diagnostic = {"LLL_row": index,
                          "weighted_squared_norm": str(sum(x*x for x in row)),
                          "maximum_D_bits": max(abs(x).bit_length() for x in denominator),
                          "both_original_probe_congruences_verified": True}
            if not any(denominator):
                diagnostic["candidate_status"] = "zero_denominator"
                diagnostics.append(diagnostic)
                continue
            sign = 1 if next(x for x in denominator if x) > 0 else -1
            denominator = [sign*x for x in denominator]
            node = self.node(denominator, pair_index, index, sign)
            diagnostic.update({
                "candidate_id": node["id"], "candidate_sign": sign,
                "ell_unit_diagnostic_only": self.ell_unit(denominator),
                "height_and_unit_properties_not_used_as_acceptance_bounds": True})
            if node["id"] in seen:
                diagnostic["candidate_status"] = "duplicate_denominator_in_this_lattice"
            else:
                seen.add(node["id"])
                diagnostic["candidate_status"] = "retained_for_original_exact_verification"
                candidates.append(node)
            diagnostics.append(diagnostic)
        self.store(name, {
            "probe_pair_index": pair_index,
            "probe_indices_C_then_A": list(indices),
            "probes": [dict(self.probe_spec(i),
                            original_modular_L_coordinates=[str(x) for x in self.source_row(i)])
                       for i in indices],
            "lattice_dimension": 42, "weights": ["1", "1", "1"],
            "lattice_input_sha256": fingerprint(strings(rows)),
            "all_42_reduced_rows": strings(reduced_rows),
            "all_42_reduced_rows_saved": True,
            "all_84_original_probe_congruences_verified": True,
            "candidate_order_by_exact_squared_norm": order,
            "row_diagnostics": diagnostics, "candidates": candidates,
            "all_nonzero_distinct_denominators_retained": True,
            "sufficient_uniqueness_bound_not_used": True,
            "all_candidates_use_original_normalized_lift_directly": True,
            "old_28_dimensional_LLL_reexecuted": False,
            "LLL_is_only_candidate_generation": True})
        print("PROJECTIVE_TWO_PROBE_LLL="+json.dumps({
            "pair_index": pair_index, "probe_indices": list(indices),
            "dimension": 42, "all_rows_saved": True, "candidate_count": len(candidates)}), flush=True)
        return self.cache(name)

    def accepted_numerators(self, node):
        denominator = [int(x) for x in node["denominator"]]
        assert any(denominator) and len(denominator) == LD
        # D is never silently reduced modulo M.  The chosen free coordinate
        # records this actual integral scale even when its coefficients exceed M/2.
        cc = []
        free_set = set(self.free_columns)
        for index in range(NC):
            if index == self.free:
                cc.append(list(denominator))
            elif index in free_set:
                cc.append([0]*LD)
            else:
                cc.append(self.order.centered_product(denominator, self.c_lift[index], self.modulus))
        aa = [self.order.centered_product(denominator, row, self.modulus) for row in self.a_lift]
        assert cc[self.free] == denominator
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

    def candidate_recipe(self, node):
        name = self.node_prefix(node)+"-candidate"
        cached = self.cache(name)
        if cached is not None:
            assert cached["node_id"] == node["id"]
            return name, cached
        aa, cc = self.accepted_numerators(node)
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
            "node_id": node["id"],
            "source_lattice": self.reference(self.lattice_name(node["source_probe_pair_index"])),
            "source_reduced_row": node["source_LLL_row"],
            "source_reduced_row_sign": node["source_LLL_row_sign"],
            "nonfree_coordinates_are_centered_original_modular_products": True,
            "chosen_free_coordinate_is_actual_D_without_centering": True,
            "height_acceptance_bound_used": False,
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

    def exact_verification(self, node):
        name, recipe = self.candidate_recipe(node)
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

    def retire_rejected_work(self, node):
        """Keep the complete rejection and all LLL rows; retire only closed payloads.

        The receipt is saved before any deletion.  No retired payload can be
        requested again: process_node first reuses its complete outcome.
        An interrupted current candidate retains every payload needed to resume.
        """
        prefix = self.node_prefix(node)
        outcome = self.cache(prefix+"-result")
        assert outcome is not None and outcome["exact_relation_found"] is False
        rejected = self.cache(prefix+"-exact-rejected")
        assert rejected is not None and rejected["node_id"] == node["id"]
        name = prefix+"-closed-work-receipt"
        receipt = self.cache(name)
        if receipt is None:
            names = [prefix+"-candidate"]
            names += [prefix+"-exact-expansion-"+str(m).zfill(3) for m in range(ORDERS)]
            names += [prefix+"-exact-verification-"+str(m).zfill(3) for m in range(ORDERS)]
            files = [self.reference(n) for n in names if self.path(n).exists()]
            assert any(spec["file"] == prefix+"-candidate.json.gz" for spec in files)
            assert rejected["candidate_sha256"] == next(
                spec["sha256"] for spec in files if spec["file"] == prefix+"-candidate.json.gz")
            receipt = self.store(name, {
                "node_id": node["id"], "completed_rejection": self.reference(prefix+"-exact-rejected"),
                "completed_outcome": self.reference(prefix+"-result"),
                "retired_work_files": files,
                "all_original_42_LLL_rows_and_exact_failure_retained": True,
                "current_or_successful_candidate_payload_never_retired": True,
                "retired_payloads_never_recomputed_for_this_completed_candidate": True})
        for spec in receipt["retired_work_files"]:
            path = self.path(spec["file"])
            if path.exists():
                assert self.reference(spec["file"]) == spec
                path.unlink()

    def process_node(self, node):
        assert fingerprint({"denominator": node["denominator"]}) == node["id"]
        name = self.node_prefix(node)+"-result"
        outcome = self.cache(name)
        if outcome is not None:
            assert outcome["node_id"] == node["id"]
            if not outcome["exact_relation_found"]:
                self.retire_rejected_work(node)
            return outcome
        self.budget()
        relation = self.exact_verification(node)
        rejected = self.cache(self.node_prefix(node)+"-exact-rejected") if relation is None else None
        outcome = {
            "node_id": node["id"], "denominator": node["denominator"],
            "source_lattice": self.reference(self.lattice_name(node["source_probe_pair_index"])),
            "source_reduced_row": node["source_LLL_row"],
            "exact_relation_found": relation is not None, "relation_spec": relation,
            "height_bound_was_not_an_acceptance_condition": True,
            "same_normalized_direction_claimed_only_if_all_129_exact": True,
            "first_nonzero_relation_order": rejected["first_nonzero_relation_order"] if rejected else None,
            "exact_rejection": self.reference(self.node_prefix(node)+"-exact-rejected") if rejected else None,
            "no_failure_residual_is_reinterpreted_as_an_input_coordinate": True}
        self.store(name, outcome)
        if relation is None:
            self.retire_rejected_work(node)
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
            "candidate_search_exhausted": state["probe_pair_index"] == len(PROBE_PAIRS) and not complete,
            "search_node_budget_reached": (
                state["probe_pair_index"] < len(PROBE_PAIRS)
                and len(state["processed_node_ids"]) >= self.maximum_nodes and not complete),
            "search_lattice_budget_reached": (
                state["probe_pair_index"] < len(PROBE_PAIRS)
                and state["probe_pair_index"] >= self.maximum_lattices and not complete),
            "remaining_schedule": [
                {"probe_pair_index": i, "probe_indices_C_then_A": list(PROBE_PAIRS[i]),
                 "next_candidate_position": state["next_candidate_position"] if i == state["probe_pair_index"] else 0}
                for i in range(state["probe_pair_index"], len(PROBE_PAIRS))],
            "completed_search_nodes": len(state["processed_node_ids"]),
            "consumed_LLL_candidate_rows": state["consumed_LLL_candidate_rows"],
            "actual_run_maximum_candidates": self.maximum_nodes,
            "actual_run_maximum_lattices": self.maximum_lattices,
            "remaining_probe_pairs": len(PROBE_PAIRS)-state["probe_pair_index"],
            "next_candidate_position": state["next_candidate_position"],
            "completed_lattice_indices": state["completed_lattice_indices"],
            "all_42_reduced_rows_per_completed_lattice_retained": True,
            "height_uniqueness_bound_used_for_success": False,
            "previous_28_dimensional_LLL_recomputed": False,
            "closed_rejected_work_retained_as_complete_decision_and_SHA_receipt": True,
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
            return self.final_certificate(True, state, self.reference(RECIPE))
        while state["probe_pair_index"] < len(PROBE_PAIRS):
            self.budget()
            pair_index = state["probe_pair_index"]
            if pair_index >= self.maximum_lattices or len(state["processed_node_ids"]) >= self.maximum_nodes:
                break
            data = self.lattice(pair_index)
            if pair_index not in state["completed_lattice_indices"]:
                state["completed_lattice_indices"].append(pair_index)
                self.save_state(state)
            candidates = data["candidates"]
            assert 0 <= state["next_candidate_position"] <= len(candidates)
            if state["next_candidate_position"] == len(candidates):
                state["probe_pair_index"] += 1
                state["next_candidate_position"] = 0
                state["finite_search_exhausted"] = state["probe_pair_index"] == len(PROBE_PAIRS)
                self.save_state(state)
                continue
            node = candidates[state["next_candidate_position"]]
            outcome = self.process_node(node)
            if node["id"] not in state["processed_node_ids"]:
                state["processed_node_ids"].append(node["id"])
            state["next_candidate_position"] += 1
            state["consumed_LLL_candidate_rows"] += 1
            if state["next_candidate_position"] == len(candidates):
                state["probe_pair_index"] += 1
                state["next_candidate_position"] = 0
                state["finite_search_exhausted"] = state["probe_pair_index"] == len(PROBE_PAIRS)
            self.save_state(state)
            print("PROJECTIVE_TWO_PROBE_CANDIDATE="+json.dumps({
                "probe_pair_index": pair_index,
                "source_LLL_row": node["source_LLL_row"],
                "candidate_id": node["id"],
                "exact_relation_found": outcome["exact_relation_found"],
                "first_nonzero_relation_order": outcome["first_nonzero_relation_order"],
                "completed_candidates": len(state["processed_node_ids"]),
                "next_candidate_position": state["next_candidate_position"]}), flush=True)
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
            "search_lattice_budget_reached": certificate["search_lattice_budget_reached"],
            "search_time_budget_reached": False,
            "all_completed_decisions_and_reduced_rows_preserved": True,
            "only_closed_rejected_payloads_retired_with_SHA_receipt": True,
            "seconds": time.monotonic()-started}
        save(args.output/"core-receipt.json", receipt)
        print("PROJECTIVE_CORE_RECEIPT="+json.dumps(receipt), flush=True)
        return 0 if complete else 2
    except BaseException as error:
        receipt = {
            "result": RESULT, "projective_mode": True, "complete": False,
            "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error),
            "search_time_budget_reached": isinstance(error, BudgetStop),
            "all_completed_decisions_and_reduced_rows_preserved": True,
            "only_closed_rejected_payloads_retired_with_SHA_receipt": True,
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
