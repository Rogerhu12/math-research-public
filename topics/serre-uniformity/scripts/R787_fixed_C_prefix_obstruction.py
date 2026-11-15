#!/usr/bin/env python3
"""The original fixed-C next-digit obstruction on branch 0 and 146 rows.

Every new operation is performed only in the public repository Actions.
The complete 430-digit lift, original inverse, and the 98 completed 42/56-search
denominators are immutable sources.  A nonzero obstruction strictly excludes
that fixed precontent C.  A zero prefix is only a necessary-condition pass.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpz_mat, fmpz_poly, nmod_mat, nmod_poly

RESULT = "R787-original-fixed-C-prefix-obstructions"
FINAL = "p41-original-fixed-C-prefix-obstructions-certificate.json"
PREFIX = "R787-fixed-C-"
ORIGINAL_RESULT = "R787-original-power5-function-relation"
ORIGINAL_FINAL = "p41-original-power5-function-relation-certificate.json"
ORIGINAL_PREFIX = "R787-projective-"
OLD_CORE = "93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04"
OLD_METHOD = "1d91bfc7bdf61c40c4deda19833a5f50491630a61a7a25feb7a3a1e0b451204b"
R786_PROOF = "c46008726fb18f52a5430b72c4994ce76164f11bea51044f1677278294f7011d"
FIELD_CORE = "d024a7a6f5febd4658e8b5b5e5e3659f3c5fcc0daa39d70569ac408ef83a8751"
OLD_TAG = "71ea66416a42e024de61cf5927bc493fbc8422dc1b5970d75c51bd788d88529d"
N, NC, LD, TD, ORDERS = 1234, 1214, 14, 20, 129
PRIME, DIGITS = 1000000753, 430

PROOF_SHA = "5c4ab25ce03bdca9dfe49def80e93fa01e481778171426cc1cef5a2fd5f26564"
METHOD_SHA = "01f4a93d1d63643e66520544221f19ffd72c555893a789ae6abf8549177f3240"
TWO_CORE = "73bac3a27c27e8e5411a0950d6efe7575c7b6e7d60dc1ed0b7eca94de1fcb093"
TWO_METHOD = "17c8927190cdc66aedf644004fe25ad7e3c24f042f5f6a660758d54c05c49a05"
THREE_CORE = "c642ec35823dace0ccac4e225e43581398dcce5737dd51cae6a2a903f6028700"
THREE_METHOD = "58a7713f7265ec4606f30f36a7eea2536f86068e7606f266b249470e48dd1cfe"
A_COUNT, COUNT, EQ, REM, CHUNK = 69, 70, 1380, 146, 5
SCOPE = {
    "source_mode": "from_original_430_cleared_residual",
    "source_Dixon_digits": 430, "working_Dixon_digits": 431,
    "original_branch": 0, "A_prefix_blocks": 69, "B_prefix_blocks": 70,
    "prefix_equation_count": 1380, "complement_equation_count": 146,
    "expected_candidate_count": 98, "source_evaluation_block_size": 5}
CONTRACT = {
    "positive_uncleared_residual": True,
    "division_by_M_before_L_branch_evaluation": True,
    "original_precontent_D_and_qC": True,
    "no_Schur_branch_inverse_used": True,
    "no_normalized_Dixon_lift_computed": True}
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



def imatrix(matrix):
    return [[int(matrix[i, j]) for j in range(matrix.ncols())]
            for i in range(matrix.nrows())]


def plain(spec):
    return {key: spec[key] for key in ("file", "bytes", "sha256")}


def import_source(name, path, expected):
    assert sha(path) == expected
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Job:
    def __init__(self, args):
        assert flint.__version__ == "0.9.0"
        self.args, self.out = args, args.output
        self.started = time.monotonic()
        self.item = read(args.config)
        assert self.item["producer_inputs_pending"] is False
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert self.item["core_sha256"] == sha(__file__)
        assert sha(args.proof) == self.item["proof_sha256"] == PROOF_SHA
        assert sha(args.method) == self.item["method_sha256"] == METHOD_SHA
        assert sha(args.field_core) == self.item["field_core_sha256"] == FIELD_CORE
        assert sha(args.original_core) == self.item["original_core_sha256"] == OLD_CORE
        assert self.item["R787_method_sha256"] == OLD_METHOD
        assert self.item["R786_proof_sha256"] == R786_PROOF
        assert self.item["pinned_R787_configuration_sha256"] == OLD_TAG
        for key, value in SCOPE.items():
            assert self.item[key] == value
        self.maximum_candidates = int(self.item.get("maximum_candidates", 98))
        assert 0 <= self.maximum_candidates <= 98
        self.out.mkdir(parents=True, exist_ok=True)
        self.source = Source(args.retained/"R787", self.item["retained_source"])
        assert self.source.spec["result"] == ORIGINAL_RESULT
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
        assert self.old_tag["original_map_index"] == 4
        assert self.old_tag["original_map_degree"] == "1206"
        assert self.old_tag["ordinary_power"] == 5 and self.old_tag["basis_dimension"] == N
        assert self.old_tag["qY_bound"] == 128 and self.old_tag["Laurent_exponents"] == [-1, 127]
        assert self.old_tag["full_L_unknown_dimension_over_Q"] == LD
        assert self.old_tag["t_coordinates"] == TD
        assert self.chart["prime"] == PRIME and self.chart["actual_modular_rank"] == 1186
        assert self.chart["other_free_columns_set_to_zero"] is True
        self.pivots = [int(x) for x in self.chart["pivot_columns"]]
        assert len(self.pivots) == len(set(self.pivots)) == 1186
        assert all(0 <= x < NC for x in self.pivots)
        self.free = int(self.chart["chosen_free_column"])
        self.free_columns = [j for j in range(NC) if j not in set(self.pivots)]
        self.free_set = set(self.free_columns)
        assert self.free == 1186 and len(self.free_columns) == 28
        assert self.free in self.free_set

        self.selection = self.source.stage(checkpoint["selection_file"])
        assert self.selection["prime"] == PRIME and self.selection["prime_proved"] is True
        assert self.selection["all_14_L_branches_distinct"] is True
        assert self.selection["all_rational_denominators_units"] is True
        assert self.selection["all_kappa_reductions_invertible"] is True
        self.roots = [tuple(int(x) for x in pair) for pair in self.selection["roots_B_s"]]
        assert len(self.roots) == len(set(self.roots)) == 14
        evaluation = integer_rows(self.selection["evaluation_matrix"], LD, LD)
        assert all(0 <= x < PRIME for row in evaluation for x in row)
        self.weights = evaluation[0]
        b0, s0 = self.roots[0]
        assert self.weights == [pow(b0, i, PRIME)*pow(s0, j, PRIME) % PRIME
                                for j in range(2) for i in range(7)]
        inverse_kappa = integer_rows(self.selection["kappa_inverse_at_each_L_branch"], LD, TD)
        self.inverse_kappa = inverse_kappa[0]
        assert all(0 <= x < PRIME for x in self.inverse_kappa)

        blocks = self.source.stage(checkpoint["rational_blocks_file"])
        assert blocks["prime"] == PRIME and blocks["exact_E0_Z_zero_verified"] is True
        assert blocks["A_minor_det_mod_prime"] and blocks["B_constant_minor_det_mod_prime"]
        assert blocks["A_inverse_over_Q_computed"] is False
        self.ZP = [int(x) for x in blocks["B_constant_pivot_columns"]]
        self.ZQ = [int(x) for x in blocks["B_constant_free_columns"]]
        assert len(self.ZP) == TD and len(self.ZQ) == NC
        assert sorted(self.ZP+self.ZQ) == list(range(N))
        zp = integer_rows(blocks["Z_pivot_integer_rows"], TD, NC)
        self.Zp = fmpz_mat(zp)
        self.Zp_mod = nmod_mat([[x % PRIME for x in row] for row in zp], PRIME)
        self.Zd = int(blocks["Z_free_diagonal"])
        assert self.Zd > 0 and self.Zd % PRIME
        self.J = [int(x) for x in blocks["A_pivot_rows"]]
        assert len(self.J) == len(set(self.J)) == N
        assert all(0 <= x < EQ for x in self.J)
        self.Rpre = sorted(set(range(EQ))-set(self.J))
        assert len(self.Rpre) == REM
        ar = [int(x) for x in blocks["A_remaining_rows"]]
        assert ar == [i for i in range(128*TD) if i not in set(self.J)]
        assert self.Rpre == [i for i in ar if i < EQ]
        inverse = integer_rows(blocks["A_inverse_mod_prime"], N, N)
        assert all(0 <= x < PRIME for row in inverse for x in row)
        self.U0 = nmod_mat(inverse, PRIME)
        self.original_A_minor = int(blocks["A_minor_det_mod_prime"])
        del blocks, inverse, zp

        lift = self.source.stage(checkpoint["lift_file"])
        assert lift["prime"] == PRIME and lift["digits"] == DIGITS
        self.M = int(lift["modulus"])
        assert self.M == PRIME**DIGITS
        self.Q = self.M*PRIME
        assert lift["chart_sha256"] == self.source.files[checkpoint["chart_file"]]["sha256"]
        assert lift["full_original_modular_relations_verified"] is True
        self.a_lift = integer_rows(lift["A_L_coordinates"], N, LD)
        self.c_lift = integer_rows(lift["C_L_coordinates"], NC, LD)
        assert all(0 <= x < self.M for matrix in (self.a_lift, self.c_lift)
                   for row in matrix for x in row)
        assert self.c_lift[self.free] == [1]+[0]*13
        assert all(self.c_lift[j] == [0]*LD for j in self.free_set if j != self.free)
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
        module = import_source("fixed_C_original_R781", args.field_core, FIELD_CORE)
        field_input = self.r781.stage("R781-original-real-field-input.json.gz")
        self.f = module.Field(field_input["field"]["original_b_minimal_polynomial"])
        assert self.f.description == field_input["field"] == self.old_tag["field"]
        self.order = IntegralOrder(self.f.description["integral_B_minimal_polynomial"])
        assert self.f.lam % PRIME
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__),
            "python_flint": flint.__version__, "p": 41,
            "proof_sha256": sha(args.proof), "method_sha256": sha(args.method),
            "field_core_sha256": FIELD_CORE, "original_core_sha256": OLD_CORE,
            "pinned_R787_configuration_sha256": OLD_TAG,
            "field": self.f.description,
            "retained_source": self.item["retained_source"],
            "retained_artifacts": self.item["retained_artifacts"],
            "checkpoint": checkpoint,
            "completed_three_probe_source": self.item["completed_three_probe_source"],
            "previous_two_probe_source": self.item["previous_two_probe_source"],
            **SCOPE, **CONTRACT}
        original = import_source("fixed_C_original_R787", args.original_core, OLD_CORE)
        class PrefixField(original.ModularField):
            def convolution(inner, left, right):
                assert len(left) == len(right) == COUNT
                assert all(len(row) == LD*TD for row in left+right)
                aa, bb = [0]*(1521*COUNT), [0]*(1521*COUNT)
                for n in range(COUNT):
                    for index, a, b in zip(inner.indices, left[n], right[n]):
                        aa[1521*n+index], bb[1521*n+index] = a, b
                product = inner.ctx(aa).mul_low(inner.ctx(bb), 1521*COUNT)
                return [inner.reduced(product, 1521*n) for n in range(COUNT)]
        self.PrefixField = PrefixField
        self.ring = None
        self.R, self.K = [], []
        prior = None
        for n in range(COUNT+1):
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
            if n < COUNT:
                self.R.append(self.f.decode(row["coefficients"]["R"]))
            prior = name
        assert len(self.K) == 71 and len(self.R) == 70
        assert self.K[0] == self.f.one and self.K[1] == self.kappa and self.R[0] == self.f.one
        cert = self.r786.certificate
        assert cert["exact_power5_basis_dimension"] == N
        assert cert["exact_K_basis_prefix_bound_qY"] == 128
        assert cert["basis_integer_scale"] == self.old_tag["basis_integer_scale"]
        self.index_spec = cert["basis_index"]
        assert self.r786.ref(self.index_spec["file"]) == plain(self.index_spec)
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
            assert row["all_original_phase_involutions_verified"] is True
            assert row["averaging_used"] is False
            values = row["integer_t_coefficients"]
            assert len(values) == ORDERS and all(len(v) == TD for v in values)
            # Full original file SHA is bound; only these already-made prefix
            # integers are retained in memory.  No Fourier coefficient is made.
            columns.append([int(x) for vector in values[:COUNT] for x in vector])
            real_specs.append(self.source.ref(name))
        frows = [list(row) for row in zip(*columns)]
        self.F = fmpz_mat(frows)
        self.Fmod = nmod_mat([[x % PRIME for x in row] for row in frows], PRIME)
        self.Frem = nmod_mat([[x % PRIME for x in frows[i]] for i in self.Rpre], PRIME)
        del columns, frows
        assert self.F.nrows() == COUNT*TD and self.F.ncols() == N
        self.Tred_mod = nmod_mat([[int(self.f.Tred[i, j]) % PRIME for j in range(TD)]
                                  for i in range(39)], PRIME)
        self.gt_mod = nmod_poly([int(x) % PRIME for x in self.f.gt.coeffs()], PRIME)
        self.candidate_sources = {}
        self.candidates = self.read_candidates()
        audit = self.cache(PREFIX+"source-audit")
        audit_data = {
            "original_R787_configuration_sha256": OLD_TAG,
            "checkpoint": {key: self.source.ref(checkpoint[key]) for key in
                ("lift_file", "chart_file", "rational_blocks_file", "selection_file")},
            "real_rows": real_specs, "real_row_count": N,
            "retained_real_prefix_count": COUNT,
            "R781_used_files": [self.r781.ref(name) for name in sorted(self.r781.used)],
            "R786_used_files": [self.r786.ref(name) for name in sorted(self.r786.used)],
            "completed_searches": {
                label: {"source": source.spec, "configuration_sha256": fingerprint(source.tag),
                        "used_files": [source.ref(name) for name in sorted(source.used)]}
                for label, source in self.candidate_sources.items()},
            "candidate_sources": self.candidates,
            "actual_distinct_candidates": len(self.candidates),
            "basis_integer_scale": self.old_tag["basis_integer_scale"],
            "actual_free_column": self.free,
            "actual_original_A_pivot_rows": self.J,
            "original_equation_rows": self.Rpre,
            "original_A_minor_mod_prime": self.original_A_minor,
            "actual_branch_roots_B_s": list(self.roots[0]),
            "actual_branch_evaluation_weights": self.weights,
            "all_original_source_bytes_SHA_and_mathematical_tags_verified": True,
            "old_mathematics_recomputed": False,
            "old_candidate_failure_is_not_a_fixed_C_obstruction": True,
            "no_original_Schur_branch_file_or_inverse_required": True}
        if audit is None:
            self.store(PREFIX+"source-audit", audit_data)
        else:
            assert {key: audit[key] for key in audit_data} == audit_data
        self.audit_spec = self.reference(PREFIX+"source-audit")


    def read_candidates(self):
        answer, seen = [], set()
        expected = {
            "two_probe": ("previous_two_probe_source", TWO_CORE, TWO_METHOD, 42),
            "three_probe": ("completed_three_probe_source", THREE_CORE, THREE_METHOD, 56)}
        for label in ("two_probe", "three_probe"):
            key, core, method, count = expected[label]
            spec = self.item[key]
            assert spec["core_sha256"] == core
            assert spec["projective_method_sha256"] == method
            source = Source(self.args.candidates/label, dict(spec, result=ORIGINAL_RESULT))
            self.candidate_sources[label] = source
            assert (source.directory/"full-outputs-manifest.json").stat().st_size == spec["manifest_bytes"]
            assert len(source.files) == spec["manifest_file_count"]
            if label == "two_probe":
                assert str(spec["run_id"]) == "43748801736"
                assert spec["source_commit"] == "e2ac3449ac480c6f00bce197c0bd5202f8b1fda4"
                assert spec["manifest_sha256"] == "2a18a2f48509695e6f316087c09c6fa9c8fd92bcf47b26c768174b6290c95845"
                pin_keys = ("lattice_stage", "search_state", "certificate", "input_bundle")
            else:
                assert str(spec["run_id"]) == "43754407301"
                assert spec["source_commit"] == "1827d794565f94455e4f251f20d1979b55fee783"
                assert spec["manifest_sha256"] == "7418100ba952913eeab8a60604d92ad4ad5ffdd49d3204602897641198ef77f0"
                pin_keys = ("lattice_stage", "raw_lattice_stage", "input_stage",
                            "source_basis_stage", "search_state", "certificate",
                            "stage_manifest", "input_bundle", "previous_search_bundle")
            for key in pin_keys:
                assert source.ref(spec[key]["file"]) == plain(spec[key])
            lattice = source.stage(spec["lattice_stage"]["file"])
            tag = source.tag
            assert tag["source_sha256"] == core
            assert tag["projective_method_sha256"] == method
            assert tag["projective_mode"] is True
            assert tag["pinned_R787_configuration_sha256"] == OLD_TAG
            assert tag["retained_source"] == self.item["retained_source"]
            assert tag["checkpoint"] == self.item["checkpoint"]
            for key, value in self.old_tag.items():
                if key != "source_sha256":
                    assert tag[key] == value
            assert tag["actual_free_coordinate_equals_unreduced_candidate_D"] is True
            if label == "three_probe":
                assert tag["previous_two_probe_source"] == self.item["previous_two_probe_source"]
            assert lattice["result"] == ORIGINAL_RESULT and lattice["probe_pair_index"] == 0
            assert lattice["lattice_dimension"] == count
            assert lattice["all_"+str(count)+"_reduced_rows_saved"] is True
            assert lattice["all_candidates_use_original_normalized_lift_directly"] is True
            assert lattice["sufficient_uniqueness_bound_not_used"] is True
            if label == "two_probe":
                assert lattice["probe_indices_C_then_A"] == [0, 1]
                assert lattice["all_84_original_probe_congruences_verified"] is True
                rows = integer_rows(lattice["all_42_reduced_rows"], 42, 42)
            else:
                assert lattice["reduced_basis_stage"] == spec["raw_lattice_stage"]
                assert lattice["input_basis_stage"] == spec["input_stage"]
                raw = source.stage(spec["raw_lattice_stage"]["file"])
                inp = source.stage(spec["input_stage"]["file"])
                old_basis = source.stage(spec["source_basis_stage"]["file"])
                assert raw["input_basis"] == spec["input_stage"]
                assert raw["all_56_reduced_rows_saved"] is True
                assert inp["source_basis_certificate"] == spec["source_basis_stage"]
                assert inp["previous_lattice_stage"] == self.item["previous_two_probe_source"]["lattice_stage"]
                assert old_basis["previous_two_probe_source"] == self.item["previous_two_probe_source"]
                assert old_basis["third_probe_found"] is True
                assert old_basis["old_42_dimensional_LLL_reexecuted"] is False
                assert lattice["all_168_original_probe_congruences_verified"] is True
                assert lattice["new_56_rows_are_a_full_integer_lattice_basis"] is True
                assert lattice["new_basis_change_times_canonical_equals_reduced_basis"] is True
                assert int(lattice["new_basis_change_determinant"]) in (-1, 1)
                assert lattice["old_42_dimensional_LLL_reexecuted"] is False
                rows = integer_rows(raw["all_56_reduced_rows"], 56, 56)
                third = old_basis["third_probe"]
                third_index = int(third["source_row"])
                assert third["source_kind"] == "A"
                assert third["global_index"] == NC+third_index
                assert 0 <= third_index < N
                assert [int(x) for x in third["original_modular_L_coordinates"]] == self.a_lift[third_index]
                assert lattice["probe_indices_C_then_A"] == [0, 1, NC+third_index]
            for index, probe in enumerate(lattice["probes"]):
                global_index = lattice["probe_indices_C_then_A"][index]
                vector = self.c_lift[global_index] if global_index < NC else self.a_lift[global_index-NC]
                assert probe["global_index"] == global_index
                assert [int(x) for x in probe["original_modular_L_coordinates"]] == vector
            queue = source.raw(spec["search_state"]["file"])
            certificate = source.raw(spec["certificate"]["file"])
            assert queue["result"] == certificate["result"] == ORIGINAL_RESULT
            assert queue["configuration"] == certificate["configuration"] == tag
            assert queue["complete"] is False and certificate["complete"] is False
            assert queue["probe_pair_index"] >= 1 and 0 in queue["completed_lattice_indices"]
            assert certificate["actual_y_map_recovered"] is False
            assert certificate["resume_state"] == spec["search_state"]
            assert certificate["actual_Dixon_digits"] == DIGITS
            assert certificate["additional_Dixon_digits_computed"] == 0
            assert source.ref(certificate["source_audit"]["file"]) == plain(certificate["source_audit"])
            old_audit = source.stage(certificate["source_audit"]["file"])
            assert old_audit["all_original_source_bytes_SHA_and_mathematical_tags_verified"] is True
            assert old_audit["original_R787_configuration_sha256"] == OLD_TAG
            assert old_audit["old_mathematics_recomputed"] is False
            if label == "three_probe":
                assert certificate["previous_exact_candidate_rejections_referenced"] == 0
                assert certificate["new_exact_candidate_evaluations"] == 56
                assert certificate["stage_manifest"] == spec["stage_manifest"]
                source.stage(spec["stage_manifest"]["file"])
            assert len(lattice["candidates"]) == count
            assert len(queue["processed_node_ids"]) == count
            assert len(set(queue["processed_node_ids"])) == count
            assert set(queue["processed_node_ids"]) == {node["id"] for node in lattice["candidates"]}
            for node in lattice["candidates"]:
                self.budget()
                index, sign = int(node["source_LLL_row"]), int(node["source_LLL_row_sign"])
                assert 0 <= index < count and sign in (-1, 1)
                assert node["source_probe_pair_index"] == 0
                denominator = [int(x) for x in node["denominator"]]
                assert [str(x) for x in denominator] == node["denominator"]
                assert denominator == [sign*x for x in rows[index][:LD]]
                assert any(denominator) and next(x for x in denominator if x) > 0
                candidate_id = fingerprint({"denominator": node["denominator"]})
                assert candidate_id == node["id"] and candidate_id not in seen
                seen.add(candidate_id)
                stem = ORIGINAL_PREFIX+"candidate-"+candidate_id
                outcome_name, rejected_name, closed_name = (
                    stem+"-result.json.gz", stem+"-exact-rejected.json.gz",
                    stem+"-closed-work-receipt.json.gz")
                outcome = source.stage(outcome_name)
                rejected = source.stage(rejected_name)
                closed = source.stage(closed_name)
                assert outcome["node_id"] == rejected["node_id"] == closed["node_id"] == candidate_id
                assert outcome["denominator"] == node["denominator"]
                assert outcome["exact_relation_found"] is False and outcome["relation_spec"] is None
                assert outcome["source_lattice"] == spec["lattice_stage"]
                assert outcome["source_reduced_row"] == index
                assert outcome["exact_rejection"] == source.ref(rejected_name)
                if label == "three_probe":
                    assert outcome["previous_exact_rejection_reused"] is False
                assert rejected["not_a_characteristic_zero_relation"] is True
                assert rejected["no_original_function_recovery_claimed"] is True
                assert 0 <= rejected["first_nonzero_relation_order"] < ORDERS
                assert outcome["first_nonzero_relation_order"] == rejected["first_nonzero_relation_order"]
                assert closed["completed_outcome"] == source.ref(outcome_name)
                assert closed["completed_rejection"] == source.ref(rejected_name)
                assert closed["current_or_successful_candidate_payload_never_retired"] is True
                assert closed["retired_payloads_never_recomputed_for_this_completed_candidate"] is True
                retired = {row["file"]: plain(row) for row in closed["retired_work_files"]}
                old_candidate_name = stem+"-candidate.json.gz"
                assert old_candidate_name in retired
                assert retired[old_candidate_name]["sha256"] == rejected["candidate_sha256"]
                answer.append({
                    "candidate_id": candidate_id, "source_group": label,
                    "source_LLL_row": index, "source_LLL_row_sign": sign,
                    "denominator": list(node["denominator"]),
                    "source_configuration_sha256": fingerprint(tag),
                    "source_lattice": plain(spec["lattice_stage"]),
                    "original_complete_outcome": source.ref(outcome_name),
                    "original_exact_rejection": source.ref(rejected_name),
                    "original_closed_work_receipt": source.ref(closed_name),
                    "original_retired_candidate": retired[old_candidate_name],
                    "original_first_nonzero_relation_order": rejected["first_nonzero_relation_order"],
                    "unremoved_common_content_denominator": True})
        assert len(answer) == len(seen) == 98
        assert sum(x["source_group"] == "two_probe" for x in answer) == 42
        assert sum(x["source_group"] == "three_probe" for x in answer) == 56
        return answer

    def budget(self):
        if time.monotonic()-self.started >= self.args.budget_minutes*60:
            raise BudgetStop("Fixed-C budget reached; all atomic shared stages and candidate decisions are retained.")

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
        assert name.startswith(PREFIX)
        obj = {"result": RESULT, "configuration": self.tag, "complete": True}
        obj.update(value)
        assert obj["result"] == RESULT and obj["configuration"] == self.tag
        assert obj["complete"] is True
        save(self.path(name), obj)
        print("FIXED_C_STAGE="+json.dumps({
            "stage": self.path(name).name, "seconds": time.monotonic()-self.started,
            "complete": True}), flush=True)
        return obj

    def reference(self, name):
        return file_spec(self.path(name))

    def check_reference(self, spec):
        assert self.reference(spec["file"]) == plain(spec)

    def value_mod(self, value, modulus):
        scale = int(value.scale.numer())*pow(int(value.scale.denom()), -1, modulus) % modulus
        return [int(x)*scale % modulus for x in self.f.vector(value)]

    def ring_Q(self):
        if self.ring is None:
            self.ring = self.PrefixField(self.f, self.Q)
        return self.ring

    def slice_F(self, first_row, stop_row):
        assert 0 <= first_row <= stop_row <= COUNT*TD
        return fmpz_mat([[int(self.F[i, j]) for j in range(N)]
                         for i in range(first_row, stop_row)])

    def source_B_expansion(self):
        name = PREFIX+"source-B-expansion"
        cached = self.cache(name)
        if cached is not None:
            assert cached["source_lift"] == self.source.ref(self.item["checkpoint"]["lift_file"])
            assert cached["source_rational_blocks"] == self.source.ref(self.item["checkpoint"]["rational_blocks_file"])
            assert cached["modulus"] == str(self.Q)
            return cached
        self.budget()
        pivots = self.Zp*fmpz_mat(self.c_lift)
        rows = [[0]*LD for _ in range(N)]
        for i, target in enumerate(self.ZP):
            rows[target] = [int(pivots[i, j]) % self.Q for j in range(LD)]
        for i, target in enumerate(self.ZQ):
            rows[target] = [self.Zd*x % self.Q for x in self.c_lift[i]]
        return self.store(name, {
            "source_lift": self.source.ref(self.item["checkpoint"]["lift_file"]),
            "source_rational_blocks": self.source.ref(self.item["checkpoint"]["rational_blocks_file"]),
            "modulus": str(self.Q), "B_coordinates_mod_Q": strings(rows),
            "original_Z_pivot_and_free_scale_preserved": True,
            "old_characteristic_zero_candidate_not_reconstructed": True})

    def source_evaluations(self):
        result = []
        aa, bb = None, None
        for first in range(0, COUNT, CHUNK):
            stop = min(first+CHUNK, COUNT)
            name = PREFIX+"source-evaluation-"+str(first).zfill(3)+"-"+str(stop).zfill(3)
            data = self.cache(name)
            if data is None:
                self.budget()
                if aa is None:
                    aa = fmpz_mat(self.a_lift)
                    expanded = self.source_B_expansion()
                    bb = fmpz_mat(integer_rows(expanded["B_coordinates_mod_Q"], N, LD))
                a_stop = min(stop, A_COUNT)
                A = self.slice_F(first*TD, a_stop*TD)*aa
                B = self.slice_F(first*TD, stop*TD)*bb
                av = [[int(A[(n-first)*TD+r, i]) % self.Q
                       for i in range(LD) for r in range(TD)] for n in range(first, a_stop)]
                bv = [[int(B[(n-first)*TD+r, i]) % self.Q
                       for i in range(LD) for r in range(TD)] for n in range(first, stop)]
                if first == 0:
                    assert all(x == 0 for x in bv[0])
                data = self.store(name, {
                    "source_audit": self.audit_spec,
                    "source_B_expansion": self.reference(PREFIX+"source-B-expansion"),
                    "first_q": first, "stop_q": stop, "A_stop_q": a_stop,
                    "modulus": str(self.Q), "A_values_mod_Q": strings(av),
                    "B_values_mod_Q": strings(bv),
                    "A69_not_computed": True,
                    "old_integer_Fourier_rows_only_read": True})
            assert data["source_audit"] == self.audit_spec
            self.check_reference(data["source_B_expansion"])
            assert data["first_q"] == first and data["stop_q"] == stop
            assert data["A_stop_q"] == min(stop, A_COUNT)
            assert data["modulus"] == str(self.Q)
            assert len(data["A_values_mod_Q"]) == min(stop, A_COUNT)-first
            assert len(data["B_values_mod_Q"]) == stop-first
            result.append(self.reference(name))
        return result

    def weighted_B(self, evaluations):
        result = []
        for spec in evaluations:
            data = self.cache(spec["file"])
            first, stop = data["first_q"], data["stop_q"]
            name = PREFIX+"source-weighted-B-"+str(first).zfill(3)+"-"+str(stop).zfill(3)
            cached = self.cache(name)
            if cached is None:
                self.budget()
                rows = integer_rows(data["B_values_mod_Q"], stop-first, LD*TD)
                values = []
                for j, row in enumerate(rows, start=first):
                    self.budget()
                    kk = self.value_mod(self.K[j], self.Q)
                    values.append(self.ring_Q().multiply(kk, row))
                cached = self.store(name, {
                    "source_evaluation": spec, "first_q": first, "stop_q": stop,
                    "modulus": str(self.Q), "weighted_B_values_mod_Q": strings(values),
                    "weight_is_original_kappa_to_actual_q_power": True})
            assert cached["source_evaluation"] == spec
            assert cached["first_q"] == first and cached["stop_q"] == stop
            assert cached["modulus"] == str(self.Q)
            result.append(self.reference(name))
        return result

    def source_convolution(self, weighted):
        name = PREFIX+"source-convolution-070"
        cached = self.cache(name)
        if cached is not None:
            assert cached["weighted_B_stages"] == weighted
            assert cached["modulus"] == str(self.Q) and cached["q_count"] == COUNT
            return cached
        self.budget()
        bv = []
        for spec in weighted:
            data = self.cache(spec["file"])
            bv.extend(integer_rows(data["weighted_B_values_mod_Q"],
                                   data["stop_q"]-data["first_q"], LD*TD))
        assert len(bv) == COUNT and all(x == 0 for x in bv[0])
        rr = [self.value_mod(value, self.Q) for value in self.R]
        total = self.ring_Q().convolution(rr, bv)
        assert len(total) == COUNT and all(len(row) == LD*TD for row in total)
        assert all(0 <= x < self.Q for row in total for x in row)
        assert all(x == 0 for x in total[0])
        # Commit the returned expensive convolution before further budget checks.
        # Its additions and exact divisions are separate short resumable blocks.
        return self.store(name, {
            "weighted_B_stages": weighted, "modulus": str(self.Q),
            "q_count": COUNT, "q_packing_stride": 1521,
            "convolution_values_mod_Q": strings(total),
            "exact_low_70_convolution_only": True,
            "constant_coefficient_zero_verified": True})


    def shared_divided_residual(self, evaluations, weighted):
        name = PREFIX+"shared-cleared-residual-divided"
        cached = self.cache(name)
        if cached is not None:
            assert cached["source_evaluation_stages"] == evaluations
            assert cached["weighted_B_stages"] == weighted
            self.check_reference(cached["source_convolution"])
            assert cached["source_digits"] == DIGITS and cached["working_digits"] == DIGITS+1
            assert cached["first_m"] == 1 and cached["stop_m"] == COUNT
            assert cached["positive_cleared_residual"] is True
            return cached
        convolution = self.source_convolution(weighted)
        convolution_spec = self.reference(PREFIX+"source-convolution-070")
        total = integer_rows(convolution["convolution_values_mod_Q"], COUNT, LD*TD)
        del convolution
        av = []
        for spec in evaluations:
            data = self.cache(spec["file"])
            av.extend(integer_rows(data["A_values_mod_Q"],
                                   data["A_stop_q"]-data["first_q"], LD*TD))
        assert len(av) == A_COUNT
        rows, blocks = [], []
        for first in range(1, COUNT, CHUNK):
            stop = min(first+CHUNK, COUNT)
            block_name = PREFIX+"shared-cleared-residual-block-"+str(first).zfill(3)+"-"+str(stop).zfill(3)
            data = self.cache(block_name)
            if data is None:
                self.budget()
                values = []
                for m in range(first, stop):
                    self.budget()
                    kk = self.value_mod(self.K[m+1], self.Q)
                    term = self.ring_Q().multiply(kk, av[m-1])
                    residue = [(x+246**3*y) % self.Q for x, y in zip(total[m], term)]
                    assert all(x % self.M == 0 for x in residue)
                    values.append([x//self.M for x in residue])
                assert all(0 <= x < PRIME for row in values for x in row)
                data = self.store(block_name, {
                    "source_convolution": convolution_spec,
                    "source_evaluation_stages": evaluations,
                    "first_m": first, "stop_m": stop,
                    "positive_cleared_residual_divided_by_M_mod_prime": values,
                    "coordinate_count": LD*TD,
                    "all_original_280_coordinates_divisible_by_M": True,
                    "no_branch_evaluation_before_integer_division": True,
                    "no_negative_correction_rhs_used": True})
            assert data["source_convolution"] == convolution_spec
            assert data["source_evaluation_stages"] == evaluations
            assert data["first_m"] == first and data["stop_m"] == stop
            values = integer_rows(data["positive_cleared_residual_divided_by_M_mod_prime"],
                                  stop-first, LD*TD)
            assert all(0 <= x < PRIME for row in values for x in row)
            rows.extend(values)
            blocks.append(self.reference(block_name))
        assert len(rows) == A_COUNT
        return self.store(name, {
            "source_evaluation_stages": evaluations, "weighted_B_stages": weighted,
            "source_convolution": convolution_spec, "residual_blocks": blocks,
            "source_digits": DIGITS, "working_digits": DIGITS+1,
            "first_m": 1, "stop_m": COUNT,
            "positive_cleared_residual_divided_by_M_mod_prime": rows,
            "positive_cleared_residual": True,
            "all_280_coordinate_integer_divisions_verified": True,
            "branch_evaluation_not_yet_performed": True,
            "constant_B_and_cleared_residual_zero_verified": True,
            "new_normalized_Dixon_digits_computed": 0})

    def branch_evaluation(self, row):
        assert len(row) == LD*TD
        return [sum(self.weights[i]*row[TD*i+r] for i in range(LD)) % PRIME
                for r in range(TD)]

    def branch_normalization(self):
        name = PREFIX+"branch-00-normalization"
        cached = self.cache(name)
        if cached is not None:
            assert cached["source_selection"] == self.source.ref(self.item["checkpoint"]["selection_file"])
            assert cached["evaluation_weights"] == self.weights
            assert cached["branch"] == 0 and cached["Y_count"] == COUNT
            assert cached["first_clear_inverse_power"] == 2
            assert cached["last_clear_inverse_power"] == COUNT
            return cached
        self.budget()
        inverse = nmod_poly(self.inverse_kappa, PRIME)
        inverse_power = inverse
        inverse_246 = pow(246**3, -1, PRIME)
        yy, clear = [], []
        for m in range(COUNT):
            vector = self.value_mod(self.R[m], PRIME)
            rr = nmod_poly(self.branch_evaluation(vector), PRIME)
            value = (-rr*inverse_power*inverse_246) % self.gt_mod
            yy.append([int(value[r]) for r in range(TD)])
            if m:
                scale = inverse_power*inverse_246 % self.gt_mod
                clear.append([int(scale[r]) for r in range(TD)])
            if m+1 < COUNT:
                inverse_power = inverse_power*inverse % self.gt_mod
        assert len(yy) == COUNT and len(clear) == A_COUNT
        return self.store(name, {
            "source_selection": self.source.ref(self.item["checkpoint"]["selection_file"]),
            "branch": 0, "evaluation_weights": self.weights,
            "actual_branch_roots_B_s": list(self.roots[0]),
            "original_kappa_inverse_mod_prime": self.inverse_kappa,
            "Y_count": COUNT, "Y_mod_prime": yy,
            "inverse_clear_multipliers_mod_prime": clear,
            "first_clear_inverse_power": 2, "last_clear_inverse_power": COUNT,
            "Y_is_v_times_original_y_with_original_minus_sign": True,
            "inverse_kappa_read_from_selection_not_recomputed": True,
            "branch_roots_never_used_mod_M_times_prime": True})

    def project_complement(self, rhs):
        assert len(rhs) == EQ
        assert all(0 <= x < PRIME for x in rhs)
        uj = self.U0*nmod_mat([[rhs[i]] for i in self.J], PRIME)
        contribution = self.Frem*uj
        answer = [(rhs[row]-int(contribution[k, 0])) % PRIME
                  for k, row in enumerate(self.Rpre)]
        return answer, [int(uj[i, 0]) for i in range(N)]

    def shared_obstruction(self):
        name = PREFIX+"shared-prefix-obstruction"
        cached = self.cache(name)
        if cached is not None:
            assert cached["source_audit"] == self.audit_spec
            assert cached["original_equation_rows"] == self.Rpre
            assert cached["actual_original_A_pivot_rows"] == self.J
            self.check_reference(cached["shared_divided_residual"])
            self.check_reference(cached["branch_normalization"])
            assert cached["branch"] == 0
            assert len(cached["rho0_mod_prime"]) == EQ
            assert len(cached["Omega0_mod_prime"]) == REM
            return cached
        evaluations = self.source_evaluations()
        weighted = self.weighted_B(evaluations)
        residual = self.shared_divided_residual(evaluations, weighted)
        normalized = self.branch_normalization()
        self.budget()
        values = integer_rows(residual["positive_cleared_residual_divided_by_M_mod_prime"],
                              A_COUNT, LD*TD)
        multipliers = integer_rows(normalized["inverse_clear_multipliers_mod_prime"], A_COUNT, TD)
        rho = []
        for row, multiplier in zip(values, multipliers):
            # Only now apply the true mod-ell embedding to the already divided
            # 280 coordinates.  The clear multiplier has positive sign here.
            p = nmod_poly(self.branch_evaluation(row), PRIME)
            value = p*nmod_poly(multiplier, PRIME) % self.gt_mod
            rho.extend(int(value[r]) for r in range(TD))
        omega, uj = self.project_complement(rho)
        return self.store(name, {
            "source_audit": self.audit_spec,
            "shared_divided_residual": self.reference(PREFIX+"shared-cleared-residual-divided"),
            "branch_normalization": self.reference(PREFIX+"branch-00-normalization"),
            "branch": 0, "actual_original_A_pivot_rows": self.J,
            "original_equation_rows": self.Rpre,
            "rho0_mod_prime": rho, "Omega0_mod_prime": omega,
            "U0_rho0_J_mod_prime": uj,
            "original_A_inverse_source": self.source.ref(self.item["checkpoint"]["rational_blocks_file"]),
            "positive_uncleared_residual": True,
            "original_1234_inverse_consumed_without_reinversion": True,
            "complement_is_146_rows_not_full_1326": True,
            "normalized_Dixon_correction_not_computed": True})

    def node_prefix(self, node):
        return PREFIX+"candidate-"+node["candidate_id"]

    def node_identity(self, node):
        return {key: node[key] for key in
                ("candidate_id", "source_group", "source_LLL_row", "source_LLL_row_sign")}

    def quotient(self, node):
        name = self.node_prefix(node)+"-quotient"
        cached = self.cache(name)
        if cached is not None:
            assert cached["source_candidate"] == node
            assert cached["source_lift"] == self.source.ref(self.item["checkpoint"]["lift_file"])
            assert cached["original_free_columns"] == self.free_columns
            assert cached["selected_free_quotient_zero"] is True
            return cached
        self.budget()
        denominator = [int(x) for x in node["denominator"]]
        assert len(denominator) == LD and any(denominator)
        assert fingerprint({"denominator": node["denominator"]}) == node["candidate_id"]
        q = []
        for i, row in enumerate(self.c_lift):
            self.budget()
            if i in self.free_set:
                # c_free is the exact unbounded D, not center(D mod M).
                q.append([0]*LD)
                continue
            product = self.order.multiply(denominator, row)
            values = []
            for coefficient in product:
                u = coefficient % self.Q
                v = u % self.M
                centered = v-self.M if v > self.M//2 else v
                assert (u-centered) % self.M == 0
                values.append(((u-centered)//self.M) % PRIME)
            q.append(values)
        assert len(q) == NC and all(len(row) == LD for row in q)
        branch = [sum(a*b for a, b in zip(self.weights, row)) % PRIME for row in q]
        d0 = sum(a*b for a, b in zip(self.weights, denominator)) % PRIME
        return self.store(name, {
            **self.node_identity(node), "source_candidate": node,
            "source_lift": self.source.ref(self.item["checkpoint"]["lift_file"]),
            "source_digits": DIGITS, "working_digits": DIGITS+1,
            "original_free_columns": self.free_columns, "selected_free_column": self.free,
            "qC_mod_prime_in_original_integral_L_basis": q,
            "qC_branch0_mod_prime": branch,
            "D_branch0_mod_prime": d0,
            "D_branch0_is_field_evaluation_not_constant_coordinate": True,
            "selected_free_quotient_zero": True,
            "all_other_free_quotients_zero": True,
            "candidate_D_precedes_common_integer_content_removal": True,
            "full_candidate_A_or_B_reconstruction_performed": False,
            "old_exact_A_B_rejection_recomputed": False,
            "all_quotient_integer_divisibilities_verified": True,
            "quotient_identity_is_cprime_equals_D_cbar_minus_M_qC": True})

    def prefix_image(self, node, quotient):
        name = self.node_prefix(node)+"-prefix-image"
        qref = self.reference(self.node_prefix(node)+"-quotient")
        normalized = self.branch_normalization()
        normalization_ref = self.reference(PREFIX+"branch-00-normalization")
        cached = self.cache(name)
        if cached is not None:
            assert cached["quotient"] == qref
            assert cached["branch_normalization"] == normalization_ref
            assert cached["original_equation_rows"] == self.Rpre
            assert cached["candidate_id"] == node["candidate_id"]
            return cached
        self.budget()
        qc = [int(x) for x in quotient["qC_branch0_mod_prime"]]
        assert len(qc) == NC and all(0 <= x < PRIME for x in qc)
        pivot_values = self.Zp_mod*nmod_mat([[x] for x in qc], PRIME)
        expanded = [0]*N
        for i, target in enumerate(self.ZP):
            expanded[target] = int(pivot_values[i, 0])
        for i, target in enumerate(self.ZQ):
            expanded[target] = self.Zd*qc[i] % PRIME
        evaluated = self.Fmod*nmod_mat([[x] for x in expanded], PRIME)
        gg = [[int(evaluated[n*TD+r, 0]) for r in range(TD)] for n in range(COUNT)]
        assert all(x == 0 for x in gg[0])
        yy = integer_rows(normalized["Y_mod_prime"], COUNT, TD)
        packed_y, packed_g = [0]*(39*COUNT), [0]*(39*COUNT)
        for n in range(COUNT):
            packed_y[39*n:39*n+TD] = yy[n]
            packed_g[39*n:39*n+TD] = gg[n]
        product = nmod_poly(packed_y, PRIME).mul_low(nmod_poly(packed_g, PRIME), 39*COUNT)
        reduced = nmod_mat([[int(product[39*n+r]) for r in range(39)]
                            for n in range(COUNT)], PRIME)*self.Tred_mod
        assert all(not reduced[0, r] for r in range(TD))
        rhs = [int(reduced[n, r]) for n in range(1, COUNT) for r in range(TD)]
        projected, uj = self.project_complement(rhs)
        return self.store(name, {
            **self.node_identity(node), "quotient": qref,
            "branch_normalization": normalization_ref,
            "original_Z_and_A_inverse_source": self.source.ref(self.item["checkpoint"]["rational_blocks_file"]),
            "G_count": COUNT, "G_mod_prime": gg,
            "Cy_qC_prefix_mod_prime": rhs,
            "projected_Cy_qC_prefix_mod_prime": projected,
            "U0_Cy_qC_J_mod_prime": uj,
            "original_equation_rows": self.Rpre,
            "t_packing_stride": 39,
            "constant_G_and_YG_zero_verified": True,
            "single_right_hand_side_only_not_full_Cy_matrix": True,
            "original_Zd_scale_preserved": True,
            "no_Schur_branch_inverse_used": True})

    def candidate_result(self, node, shared):
        name = self.node_prefix(node)+"-result"
        shared_ref = self.reference(PREFIX+"shared-prefix-obstruction")
        cached = self.cache(name)
        if cached is not None:
            for key, value in self.node_identity(node).items():
                assert cached[key] == value
            assert cached["source_candidate"] == node
            assert cached["shared_prefix_obstruction"] == shared_ref
            self.check_reference(cached["quotient"])
            self.check_reference(cached["prefix_image"])
            assert cached["original_equation_rows"] == self.Rpre
            return cached
        q = self.quotient(node)
        image = self.prefix_image(node, q)
        self.budget()
        d0 = int(q["D_branch0_mod_prime"])
        omega0 = [int(x) for x in shared["Omega0_mod_prime"]]
        projected = [int(x) for x in image["projected_Cy_qC_prefix_mod_prime"]]
        assert len(omega0) == len(projected) == REM
        omega = [(d0*a+b) % PRIME for a, b in zip(omega0, projected)]
        first = next((i for i, x in enumerate(omega) if x != 0), None)
        row = None if first is None else self.Rpre[first]
        return self.store(name, {
            **self.node_identity(node), "source_candidate": node,
            "shared_prefix_obstruction": shared_ref,
            "quotient": self.reference(self.node_prefix(node)+"-quotient"),
            "prefix_image": self.reference(self.node_prefix(node)+"-prefix-image"),
            "branch": 0, "prime": PRIME, "original_equation_rows": self.Rpre,
            "D_branch0_mod_prime": d0,
            "D_branch0_is_field_evaluation_not_constant_coordinate": True,
            "Omega_mod_prime": omega,
            "first_nonzero_complement_position": first,
            "first_nonzero_original_equation_row": row,
            "first_nonzero_projected_source_m": None if row is None else row//TD+1,
            "first_nonzero_projected_source_t_coordinate": None if row is None else row % TD,
            "nonzero_is_a_projected_equation_not_raw_Laurent_first_failure": True,
            "strict_fixed_C_rejected": first is not None,
            "prefix_only_zero": first is None,
            "necessary_condition_only_if_all_146_entries_zero": True,
            "old_candidate_A_centering_or_rejection_not_used_as_new_proof": True,
            "actual_exact_C_recovered": False,
            "actual_y_map_recovered": False,
            "complete_129_function_relation_verified": False,
            "beta_or_height_computed": False,
            "new_normalized_Dixon_digits_computed": 0})

    def state(self):
        name = PREFIX+"current"
        path = self.path(name)
        ids = [x["candidate_id"] for x in self.candidates]
        if path.exists():
            data = read(path)
            assert data["result"] == RESULT and data["configuration"] == self.tag
            assert data["complete"] is False
            n = int(data["next_candidate_position"])
            assert 0 <= n <= len(ids)
            assert data["processed_candidate_ids"] == ids[:n]
            for node in self.candidates[:n]:
                result = self.cache(self.node_prefix(node)+"-result")
                assert result is not None and result["candidate_id"] == node["candidate_id"]
            return data
        data = {"result": RESULT, "configuration": self.tag, "complete": False,
                "next_candidate_position": 0, "processed_candidate_ids": [],
                "actual_source_candidate_count": len(ids),
                "candidate_order": "completed_two_probe_then_completed_three_probe_saved_candidate_order",
                "new_normalized_Dixon_digits_computed": 0}
        save(path, data)
        return data

    def acknowledge(self, state, node):
        n = state["next_candidate_position"]
        assert node["candidate_id"] == self.candidates[n]["candidate_id"]
        assert node["candidate_id"] not in state["processed_candidate_ids"]
        assert self.path(self.node_prefix(node)+"-result").exists()
        state["processed_candidate_ids"].append(node["candidate_id"])
        state["next_candidate_position"] = n+1
        save(self.path(PREFIX+"current"), state)

    def inventory(self):
        name = PREFIX+"exact-stages-manifest"
        files = []
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name in (name+".json.gz", PREFIX+"current.json.gz"):
                continue
            value = read(path)
            assert value["result"] == RESULT and value["configuration"] == self.tag
            assert value["complete"] is True
            files.append(file_spec(path))
        self.store(name, {"files": files})
        return self.reference(name)

    def certificate(self, state):
        decisions, strict, zero = [], 0, 0
        count = int(state["next_candidate_position"])
        assert state["processed_candidate_ids"] == [x["candidate_id"] for x in self.candidates[:count]]
        for node in self.candidates[:count]:
            result = self.cache(self.node_prefix(node)+"-result")
            assert result is not None and result["source_candidate"] == node
            rejected, passed = result["strict_fixed_C_rejected"], result["prefix_only_zero"]
            assert isinstance(rejected, bool) and isinstance(passed, bool) and rejected != passed
            strict += int(rejected)
            zero += int(passed)
            decisions.append({
                "candidate_id": node["candidate_id"], "source_group": node["source_group"],
                "source_LLL_row": node["source_LLL_row"],
                "stage": self.reference(self.node_prefix(node)+"-result"),
                "strict_fixed_C_rejected": rejected, "prefix_only_zero": passed})
        assert strict+zero == count
        assert self.path(PREFIX+"source-audit").exists()
        assert self.path(PREFIX+"shared-prefix-obstruction").exists()
        complete = count == len(self.candidates) == 98
        manifest = self.inventory()
        value = {
            "result": RESULT, "configuration": self.tag, "complete": complete,
            "p": 41, **SCOPE,
            "actual_candidate_count": count,
            "actual_source_candidate_count": len(self.candidates),
            "strict_fixed_C_rejected_count": strict, "prefix_only_zero_count": zero,
            "source_audit": self.audit_spec,
            "shared_prefix_obstruction": self.reference(PREFIX+"shared-prefix-obstruction"),
            "candidate_decisions": decisions, "stage_manifest": manifest,
            "resume_state": self.reference(PREFIX+"current"),
            "actual_exact_C_recovered": False, "actual_y_map_recovered": False,
            "complete_129_function_relation_verified": False,
            "beta_or_height_computed": False,
            "new_normalized_Dixon_digits_computed": 0,
            "complete_means_all_98_prefix_necessary_condition_decisions_only": True,
            "actual_run_maximum_candidates": self.maximum_candidates,
            "seconds": time.monotonic()-self.started}
        save(self.out/FINAL, value)
        return value

    def complete(self):
        final = self.out/FINAL
        if final.exists():
            old = read(final)
            assert old["result"] == RESULT and old["configuration"] == self.tag
            if old["complete"] is True:
                self.check_reference(old["stage_manifest"])
                inventory = self.cache(old["stage_manifest"]["file"])
                for spec in inventory["files"]:
                    self.check_reference(spec)
                assert old["actual_candidate_count"] == 98
                return old
        shared = self.shared_obstruction()
        state = self.state()
        while state["next_candidate_position"] < min(len(self.candidates), self.maximum_candidates):
            node = self.candidates[state["next_candidate_position"]]
            # A complete result may precede the atomic current update.  Its
            # restoration only acknowledges metadata, never repeats quotient.
            existing = self.cache(self.node_prefix(node)+"-result")
            if existing is None:
                self.budget()
            result = self.candidate_result(node, shared)
            self.acknowledge(state, node)
            print("FIXED_C_CANDIDATE_DECISION="+json.dumps({
                "candidate_id": node["candidate_id"], "source_group": node["source_group"],
                "source_LLL_row": node["source_LLL_row"],
                "strict_fixed_C_rejected": result["strict_fixed_C_rejected"],
                "prefix_only_zero": result["prefix_only_zero"],
                "first_nonzero_complement_position": result["first_nonzero_complement_position"],
                "processed_count": state["next_candidate_position"],
                "old_A_B_or_LLL_not_recomputed": True}), flush=True)
        return self.certificate(state)


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New exact arithmetic belongs to public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "proof", "method", "field-core", "original-core",
                 "retained", "candidates", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    started, job = time.monotonic(), None
    try:
        job = Job(args)
        certificate = job.complete()
        complete = certificate["complete"]
        receipt = {
            "result": RESULT, "complete": complete, "source_sha256": sha(__file__),
            "certificate_sha256": sha(args.output/FINAL),
            "actual_candidate_count": certificate["actual_candidate_count"],
            "strict_fixed_C_rejected_count": certificate["strict_fixed_C_rejected_count"],
            "prefix_only_zero_count": certificate["prefix_only_zero_count"],
            "source_Dixon_digits": DIGITS, "working_Dixon_digits": DIGITS+1,
            "new_normalized_Dixon_digits_computed": 0,
            "actual_exact_C_recovered": False, "actual_y_map_recovered": False,
            "complete_129_function_relation_verified": False, "beta_or_height_computed": False,
            "all_atomic_shared_and_per_candidate_stages_preserved": True,
            "time_budget_reached": False,
            "candidate_control_limit_reached": not complete,
            "seconds": time.monotonic()-started}
        save(args.output/"core-receipt.json", receipt)
        print("FIXED_C_CORE_RECEIPT="+json.dumps(receipt, sort_keys=True), flush=True)
        return 0 if complete else 2
    except BaseException as error:
        certificate_hash = None
        if job is not None and isinstance(error, BudgetStop) and \
           job.path(PREFIX+"shared-prefix-obstruction").exists():
            # Metadata-only inventory of already committed results.  No partial
            # residual or candidate is promoted to a completed decision.
            state = job.state()
            certificate = job.certificate(state)
            certificate_hash = sha(args.output/FINAL)
        receipt = {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "certificate_sha256": certificate_hash,
            "error": type(error).__name__+": "+str(error),
            "source_Dixon_digits": DIGITS, "working_Dixon_digits": DIGITS+1,
            "new_normalized_Dixon_digits_computed": 0,
            "actual_exact_C_recovered": False, "actual_y_map_recovered": False,
            "complete_129_function_relation_verified": False, "beta_or_height_computed": False,
            "all_atomic_shared_and_per_candidate_stages_preserved": True,
            "time_budget_reached": isinstance(error, BudgetStop),
            "seconds": time.monotonic()-started}
        save(args.output/"core-receipt.json", receipt)
        print("FIXED_C_CORE_RECEIPT="+json.dumps(receipt, sort_keys=True), flush=True)
        if isinstance(error, BudgetStop):
            return 124
        raise


if __name__ == "__main__":
    sys.exit(main())
