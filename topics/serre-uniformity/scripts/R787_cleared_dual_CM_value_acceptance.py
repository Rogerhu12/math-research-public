#!/usr/bin/env python3
"""A new, source-bound dual RHS for the original CM-value identity.

All mathematical arithmetic is confined to the public repository's Actions.
The old primal Dixon vector is neither required nor reinterpreted as a dual
approximation.  All fourteen old prime inverses are consumed without recomputing
them.  Acceptance requires the complete rational transpose identity and Delta=0.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import sys
import time
import traceback

import flint
from flint import fmpq, fmpz_mat, fmpz_poly, nmod_mat, nmod_poly

RESULT = "R787-original-cleared-dual-CM-value-acceptance"
FINAL = "p41-original-cleared-dual-CM-value-acceptance-certificate.json"
PREFIX = "R787-cleared-dual-"
ELL, N, D, RANK, T, LD, ORDERS, FREE = 1000000753, 1234, 1214, 1186, 20, 14, 129, 1186
OLD_CORE = "93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04"
FIELD_CORE = "d024a7a6f5febd4658e8b5b5e5e3659f3c5fcc0daa39d70569ac408ef83a8751"
OLD_TAG = "71ea66416a42e024de61cf5927bc493fbc8422dc1b5970d75c51bd788d88529d"
PROOF = "eb5893ec0b8dcc4dd256648a96daa7a605d4cb96efc94a5c42544c0c6dea572b"
METHOD = "c6ca7d3a8036c2c0b5cfca69fd66ca7108555fae9f90614d7e3618c3044288bd"
SCALE = "13744803133596058624"
CHART = "R787-prime-1000000753-chart.json.gz"
BLOCKS = "R787-prime-1000000753-rational-blocks.json.gz"
SELECTION = "R787-prime-1000000753-selection.json.gz"
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
STRATEGY = {
    "unknown": "128 original t-polynomials with 14 original L coefficients each",
    "transpose_pairing": "J[r,s]=coefficient of t^19 in t^(r+s) modulo the original monic g20",
    "square_output_order": "1234 A coordinates, 1186 original Schur-pivot coordinates, 140 original outside rows",
    "positive_residual": "246^3*kappa^(m+1)*A_(m-1)+sum_j R_(m-j)*kappa^j*B_j",
    "reverse_convolution": "U_j=[v^(128-j)](R(v)*sum_(n=0)^127 chi_(128-n)*v^n)",
    "prime_inverse": "old Ainv^t and fourteen old Schur-inverse transposes; no inverse is recomputed",
    "high_precision_inverse": False,
    "dual_initial_precision": 1,
    "primal_518_digits_relabelled_as_dual": False,
    "rational_reconstruction": "coordinatewise strict symmetric rectangle; candidate only until exact full multiplication",
    "acceptance": "Theta(chi)=d*(e,-q*eZ_P,0) in all 35840 rational coordinates; then Delta=0 exactly",
    "original_CM_responses_or_prefixes_recomputed": False,
    "operating_controls_excluded_from_mathematical_identity": True}


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        for chunk in iter(lambda: source.read(1024*1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as source:
        return json.load(source)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    payload = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        with temporary.open("wb") as raw:
            with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, compresslevel=2) as target:
                target.write(payload)
    else:
        temporary.write_bytes(payload)
    temporary.replace(path)


def plain(item):
    return {key: item[key] for key in ("file", "bytes", "sha256")}


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def integer_matrix(value):
    return [[int(value[i, j]) for j in range(value.ncols())] for i in range(value.nrows())]


def decode_q(value):
    assert len(value) == 2 and int(value[1]) > 0
    return fmpq(int(value[0]), int(value[1]))


def encode_q(value):
    return [str(value.numer()), str(value.denom())]


def shape(rows, height, width):
    assert len(rows) == height and all(len(row) == width for row in rows)


def module_from_path(name, path, digest):
    assert sha(path) == digest
    definition = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(definition)
    definition.loader.exec_module(module)
    return module


class BudgetStop(RuntimeError):
    pass


class Source:
    """Read-only producer; metadata is checked by the public stdlib runner too."""
    def __init__(self, root, name, item):
        self.directory, self.name, self.item = root/name, name, item
        manifest_path = self.directory/"full-outputs-manifest.json"
        assert sha(manifest_path) == item["manifest_sha256"]
        manifest = read(manifest_path)
        assert manifest["result"] == item["result"]
        self.inventory = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(self.inventory) == len(manifest["files"])
        self.files, self.verified = item["files"], set()
        assert fingerprint([self.files[name] for name in sorted(self.files)]) == item["selected_files_sha256"]
        for filename, row in self.files.items():
            assert filename == row["file"] and Path(filename).name == filename
            if filename == "full-outputs-manifest.json":
                assert row["sha256"] == item["manifest_sha256"]
            else:
                assert plain(row) == self.inventory[filename]
        self.certificate = None
        if item.get("certificate"):
            self.certificate = self.get_spec(item["certificate"], tagged=False)
            assert self.certificate["result"] == item["result"] and self.certificate["complete"] is True
            self.tag = self.certificate["configuration"]
        else:
            assert name == "R787"
            self.tag = self.get(CHART, tagged=False)["configuration"]
        assert self.tag["source_sha256"] == item["core_sha256"]
        assert fingerprint(self.tag) == item["configuration_sha256"]
        self.identity = {key: item[key] for key in BASE}
        self.identity.update(configuration_sha256=item["configuration_sha256"],
                             selected_files_sha256=item["selected_files_sha256"])
        if self.certificate:
            self.identity["certificate"] = plain(item["certificate"])

    def path(self, name):
        item = self.files[name]
        path = self.directory/name
        if name not in self.verified:
            assert path.stat().st_size == item["bytes"] and sha(path) == item["sha256"]
            self.verified.add(name)
        return path

    def get(self, name, tagged=True):
        value = read(self.path(name))
        if tagged:
            assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def get_spec(self, item, tagged=True):
        assert plain(item) == self.files[item["file"]]
        return self.get(item["file"], tagged)


class ClearedDualOperator:
    def __init__(self, job):
        self.job, self.field, self.legacy = job, job.field, job.legacy
        self.R, self.K, self.F = job.R, job.K, job.F
        self.blocks, self.chart, self.selection = job.blocks, job.chart, job.selection
        self.rowsJ, self.rowsI, self.outside = job.rowsJ, job.rowsI, job.outside
        self.pivots = job.pivots
        self.Zp = fmpz_mat([[int(x) for x in row] for row in self.blocks["Z_pivot_integer_rows"]])
        self.Zpt = self.Zp.transpose()
        self.Zd = int(self.blocks["Z_free_diagonal"])
        self.ZP, self.ZQ = self.blocks["B_constant_pivot_columns"], self.blocks["B_constant_free_columns"]
        self.Jpair, self.Jinv = fmpz_mat(job.pairing["J"]), fmpz_mat(job.pairing["J_inverse"])
        self.Jt = self.Jpair.transpose()
        self.Jinv_prime_t = nmod_mat(job.pairing["J_inverse"], ELL).transpose()
        self.Ft = self.F.transpose()
        self.FAt = fmpz_mat([[int(self.F[r, c]) for r in range(128*T)] for c in range(N)])
        self.FIt = nmod_mat([[int(self.F[r, c]) % ELL for r in self.rowsI] for c in range(N)], ELL)
        self.Ainvt = nmod_mat(self.blocks["A_inverse_mod_prime"], ELL).transpose()
        self.Et = nmod_mat(self.selection["evaluation_matrix"], ELL).transpose()
        self.Einvt = nmod_mat(self.selection["inverse_evaluation_matrix"], ELL).transpose()
        self.gt_prime = nmod_poly([int(x) for x in self.field.gt.coeffs()], ELL)
        self.branches = []
        self.modular_cache = None
        self.load_old_branches()

    def load_old_branches(self):
        source = self.job.sources["R787"]
        for branch in range(14):
            self.job.budget()
            name = "R787-prime-1000000753-branch-"+str(branch).zfill(2)+".json.gz"
            data = source.get(name)
            assert data["prime"] == ELL and data["branch"] == branch
            assert data["roots_B_s"] == self.selection["roots_B_s"][branch]
            assert data["chart_sha256"] == source.files[CHART]["sha256"]
            assert data["actual_Schur_rank"] == RANK and data["selected_minor_det_mod_prime"] % ELL
            assert data["all_2560_original_uncleared_rows_verified"] is True
            shape(data["Schur_minor_inverse_mod_prime"], RANK, RANK)
            shape(data["C_J_pivot_columns"], N, RANK)
            shape(data["inverse_original_clear_multipliers"], 128, T)
            self.branches.append({
                "Schur_inverse_transpose": nmod_mat(data["Schur_minor_inverse_mod_prime"], ELL).transpose(),
                "C_J_pivot_transpose": nmod_mat(data["C_J_pivot_columns"], ELL).transpose(),
                "inverse_clear": [nmod_poly(row, ELL) for row in data["inverse_original_clear_multipliers"]],
                "source": source.files[name]})
            del data

    def rational_mod(self, value, modulus):
        denominator = int(value.scale.denom())
        assert denominator % ELL
        factor = int(value.scale.numer())*pow(denominator, -1, modulus) % modulus
        return [int(x)*factor % modulus for x in self.field.vector(value)]

    def modular_data(self, modulus):
        if self.modular_cache is None or self.modular_cache[0] != modulus:
            self.modular_cache = (modulus, self.legacy.ModularField(self.field, modulus),
                [self.rational_mod(x, modulus) for x in self.R],
                [self.rational_mod(x, modulus) for x in self.K])
        return self.modular_cache[1:]

    def pair_mod(self, vector, modulus):
        rows = [vector[20*i:20*(i+1)] for i in range(14)]
        value = fmpz_mat(rows)*self.Jt
        return [int(value[i, r]) % modulus for i in range(14) for r in range(20)]

    def pair_exact(self, value):
        vector = self.field.vector(value)
        rows = [vector[20*i:20*(i+1)] for i in range(14)]
        result = fmpz_mat(rows)*self.Jt
        return self.field.from_vector([result[i, r] for i in range(14) for r in range(20)], value.scale)

    @staticmethod
    def to_rows(blocks):
        return [[int(block[20*i+r]) for i in range(14)] for block in blocks for r in range(20)]

    @staticmethod
    def to_blocks(rows):
        shape(rows, 2560, 14)
        return [[int(rows[20*m+r][i]) for i in range(14) for r in range(20)] for m in range(128)]

    def z_transpose(self, values):
        dense = self.Zpt*fmpz_mat([values[row] for row in self.ZP])
        return [[int(dense[j, k])+self.Zd*values[self.ZQ[j]][k] for k in range(14)] for j in range(D)]

    def apply_mod(self, chi, modulus):
        shape(chi, 128, 280)
        self.job.budget()
        ring, rr, kk = self.modular_data(modulus)
        lam = []
        for m in range(1, 129):
            value = ring.multiply(kk[m+1], chi[m-1])
            value = self.pair_mod(value, modulus)
            lam.append([(246**3*x) % modulus for x in value])
        reversed_chi = list(reversed(chi))+[[0]*280]
        convolution = ring.convolution(rr, reversed_chi)
        vv = []
        for j in range(129):
            self.job.budget()
            value = ring.multiply(kk[j], convolution[128-j])
            vv.append(self.pair_mod(value, modulus))
        lam_rows = self.to_rows(lam)
        AA = self.FAt*fmpz_mat(lam_rows)
        YY = self.Ft*fmpz_mat(self.to_rows(vv))
        yy = [[int(YY[i, k]) % modulus for k in range(14)] for i in range(N)]
        zz = self.z_transpose(yy)
        return {
            "A": [[int(AA[i, k]) % modulus for k in range(14)] for i in range(N)],
            "P": [[x % modulus for x in zz[j]] for j in self.pivots],
            "outside": [[x % modulus for x in lam_rows[j]] for j in self.outside],
            "free": [x % modulus for x in zz[FREE]]}

    def clear_inverse_from_branch_columns(self, columns):
        assert len(columns) == 14 and all(len(column) == 2560 for column in columns)
        result_columns = []
        for branch, column in enumerate(columns):
            self.job.budget()
            rows = [column[20*m:20*(m+1)] for m in range(128)]
            paired = nmod_mat(rows, ELL)*self.Jinv_prime_t
            output = []
            for m in range(128):
                poly = nmod_poly([int(paired[m, r]) for r in range(20)], ELL)
                value = (self.branches[branch]["inverse_clear"][m]*poly) % self.gt_prime
                output.extend(int(value[r]) for r in range(20))
            result_columns.append(output)
        matrix = nmod_mat([list(row) for row in zip(*result_columns)], ELL)*self.Einvt
        return self.to_blocks(integer_matrix(matrix))

    def solve_mod_prime(self, rhs):
        shape(rhs["A"], N, 14)
        shape(rhs["P"], RANK, 14)
        shape(rhs["outside"], 140, 14)
        outside_rows = [[0]*14 for _ in range(2560)]
        for i, row in enumerate(self.outside):
            outside_rows[row] = [int(x) % ELL for x in rhs["outside"][i]]
        outside_evaluated = nmod_mat(outside_rows, ELL)*self.Et
        outside_columns = [[int(outside_evaluated[r, branch]) for r in range(2560)] for branch in range(14)]
        if any(x for row in rhs["outside"] for x in row):
            chi_out = self.clear_inverse_from_branch_columns(outside_columns)
            contribution = self.apply_mod(chi_out, ELL)
            assert contribution["outside"] == [[int(x) % ELL for x in row] for row in rhs["outside"]]
            bA = [[(a-b) % ELL for a, b in zip(left, right)]
                  for left, right in zip(rhs["A"], contribution["A"])]
            bP = [[(a-b) % ELL for a, b in zip(left, right)]
                  for left, right in zip(rhs["P"], contribution["P"])]
        else:
            bA, bP = rhs["A"], rhs["P"]
        Aeval, Peval = nmod_mat(bA, ELL)*self.Et, nmod_mat(bP, ELL)*self.Et
        columns = []
        for branch, old in enumerate(self.branches):
            self.job.budget()
            b1 = nmod_mat([[int(Aeval[i, branch])] for i in range(N)], ELL)
            b2 = nmod_mat([[int(Peval[i, branch])] for i in range(RANK)], ELL)
            u0 = self.Ainvt*b1
            tt = old["Schur_inverse_transpose"]*(old["C_J_pivot_transpose"]*u0+b2)
            uu = u0+self.Ainvt*(self.FIt*tt)
            column = list(outside_columns[branch])
            for i, row in enumerate(self.rowsJ):
                column[row] = int(uu[i, 0])
            for i, row in enumerate(self.rowsI):
                column[row] = -int(tt[i, 0]) % ELL
            columns.append(column)
        return self.clear_inverse_from_branch_columns(columns)


class Job:
    def __init__(self, args):
        assert flint.__version__ == "0.9.0"
        self.args, self.out, self.started = args, args.output, time.monotonic()
        self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert self.item["producer_inputs_pending"] is False
        assert self.item["core_sha256"] == sha(__file__)
        assert sha(args.proof) == self.item["proof_sha256"] == PROOF
        assert sha(args.method) == self.item["method_sha256"] == METHOD
        assert self.item["legacy_core_sha256"] == OLD_CORE and self.item["field_core_sha256"] == FIELD_CORE
        self.legacy = module_from_path("original_R787_dual_source", args.legacy_core, OLD_CORE)
        self.field_module = module_from_path("original_R781_dual_field", args.field_core, FIELD_CORE)
        assert set(self.item["retained_sources"]) == {"R787", "R781", "R786", "CM"}
        self.sources = {name: Source(args.retained, name, value)
                        for name, value in self.item["retained_sources"].items()}
        source = self.sources["R787"]
        assert source.tag["result"] == "R787-original-power5-function-relation"
        assert fingerprint(source.tag) == OLD_TAG and source.tag["source_sha256"] == OLD_CORE
        self.chart, self.blocks, self.selection = (source.get(name) for name in (CHART, BLOCKS, SELECTION))
        assert self.chart["actual_modular_rank"] == RANK and self.chart["chosen_free_column"] == FREE
        assert self.chart["other_free_columns_set_to_zero"] is True
        assert self.selection["prime"] == self.blocks["prime"] == self.chart["prime"] == ELL
        assert self.selection["prime_proved"] and self.selection["all_14_L_branches_distinct"]
        assert self.selection["all_rational_denominators_units"] and self.selection["all_kappa_reductions_invertible"]
        assert self.blocks["exact_E0_Z_zero_verified"] is True
        assert self.blocks["A_inverse_over_Q_computed"] is False
        assert self.blocks["A_minor_det_mod_prime"] % ELL and self.blocks["B_constant_minor_det_mod_prime"] % ELL
        self.rowsJ = [int(x) for x in self.blocks["A_pivot_rows"]]
        remaining = [int(x) for x in self.blocks["A_remaining_rows"]]
        self.rowsI = [remaining[int(x)] for x in self.chart["pivot_rows"]]
        self.pivots = [int(x) for x in self.chart["pivot_columns"]]
        assert len(self.rowsJ) == N and len(self.rowsI) == len(self.pivots) == RANK
        assert sorted(self.rowsJ+remaining) == list(range(2560))
        assert len(set(self.rowsI)) == len(set(self.pivots)) == RANK and FREE not in self.pivots
        selected = set(self.rowsJ+self.rowsI)
        assert len(selected) == 2420
        self.outside = [row for row in range(2560) if row not in selected]
        assert len(self.outside) == 140
        for label in ("R781", "R786"):
            old = source.tag["retained_artifacts"][label]
            child = self.sources[label]
            for key in BASE:
                assert str(old[key]) == str(child.item[key])
            assert old["files"][old["certificate_name"]] == child.item["certificate"]["sha256"]
        inputs = self.sources["R781"].get("R781-original-real-field-input.json.gz")
        self.field = self.field_module.Field(inputs["field"]["original_b_minimal_polynomial"])
        assert self.field.description == inputs["field"] == source.tag["field"]
        self.tag = {"result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "proof_sha256": PROOF, "method_sha256": METHOD, "legacy_core_sha256": OLD_CORE,
            "field_core_sha256": FIELD_CORE, "original_configuration_sha256": OLD_TAG,
            "source_identities": {key: value.identity for key, value in self.sources.items()},
            "p": 41, "auxiliary_prime": ELL, "original_map_index": 4,
            "original_map_degree": "1206", "field": self.field.description,
            "normalization_free_column": FREE, "unknown_shape": [128, 280],
            "rational_unknown_dimension": 35840, "square_L_output_shape": [1234, 1186, 140],
            "basis_integer_scale": SCALE, "strategy": STRATEGY}
        self.latest = None
        self.R, self.K = self.load_original_coefficients()
        self.F = self.load_original_rows()
        self.pairing = self.coefficient_pairing()
        self.target = self.exact_target()
        self.operator = ClearedDualOperator(self)
        self.source_audit = self.audit()

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes:
            raise BudgetStop("The new dual RHS remains source-bound and every complete stage is retained.")

    def path(self, name):
        assert name.startswith(PREFIX) and Path(name).name == name
        return self.out/(name+".json.gz")

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def store(self, name, value):
        save(self.path(name), dict(value, complete=True, configuration=self.tag))
        print(json.dumps({"stage": name, "complete": True,
                          "seconds": time.monotonic()-self.started}), flush=True)
        return spec(self.path(name))

    def load_original_coefficients(self):
        source = self.sources["R781"]
        assert source.tag["selected_map_index"] == 4 and source.tag["selected_map_degree"] == "1206"
        rr, kk, previous = [], [], None
        for n in range(130):
            self.budget()
            name = "R781-inverse-free-Laurent-"+str(n).zfill(3)+".json.gz"
            row = source.get(name)
            assert row["order"] == n and row["exact_differential_identity_at_this_order"]
            if n:
                assert row["previous_stage_sha256"] == source.files[previous]["sha256"]
            else:
                assert row["input_stage_sha256"] == source.files["R781-original-real-field-input.json.gz"]["sha256"]
            kk.append(self.field.decode(row["coefficients"]["kappa_power"]))
            if n < 129:
                rr.append(self.field.decode(row["coefficients"]["R"]))
            previous = name
        assert kk[0] == rr[0] == self.field.one
        assert all(int(value.scale.denom()) % ELL for value in rr+kk)
        return rr, kk

    def load_original_rows(self):
        parent, old = self.sources["R786"], self.sources["R787"]
        cert = parent.certificate
        assert cert["original_map_index"] == 4 and cert["original_map_degree"] == "1206"
        assert cert["exact_power5_basis_dimension"] == N and cert["basis_integer_scale"] == SCALE
        assert cert["exact_K_basis_prefix_bound_qY"] == 128
        index = parent.get_spec(cert["basis_index"])
        assert index["dimension"] == N and index["bound_qY"] == 128
        columns = []
        for i, item in enumerate(index["basis_rows"]):
            self.budget()
            assert item["index"] == i
            name = "R787-real-power5-row-"+str(i).zfill(4)+".json.gz"
            row = old.get(name)
            assert row["index"] == i and row["R786_row_sha256"] == item["sha256"]
            assert row["all_original_phase_involutions_verified"] is True and row["averaging_used"] is False
            shape(row["integer_t_coefficients"], 129, 20)
            columns.append([int(x) for block in row["integer_t_coefficients"] for x in block])
        assert len(columns) == N
        return fmpz_mat([list(row) for row in zip(*columns)])

    def coefficient_pairing(self):
        name = PREFIX+"coefficient-pairing"
        cached = self.cached(name)
        if cached:
            return cached
        jj = [[int(self.field.Tred[r+s, 19]) for s in range(20)] for r in range(20)]
        lower = [list(reversed(row)) for row in jj]
        assert all(lower[i][i] == 1 for i in range(20))
        assert all(not lower[i][j] for i in range(20) for j in range(i+1, 20))
        inverse = [[int(i == j) for j in range(20)] for i in range(20)]
        for i in range(20):
            for j in range(i):
                inverse[i][j] = -sum(lower[i][k]*inverse[k][j] for k in range(j, i))
        ji = list(reversed(inverse))
        identity = fmpz_mat([[int(i == j) for j in range(20)] for i in range(20)])
        assert fmpz_mat(jj)*fmpz_mat(ji) == identity and fmpz_mat(ji)*fmpz_mat(jj) == identity
        self.store(name, {"J": jj, "J_inverse": ji,
            "ordinary_coefficient_transpose_not_trace_or_Hermitian": True,
            "integer_unimodular_pairing_and_full_inverse_identity_verified": True,
            "original_t_modulus": [str(x) for x in self.field.gt.coeffs()]})
        return self.cached(name)

    def exact_target(self):
        name = PREFIX+"exact-target"
        cached = self.cached(name)
        if cached:
            return cached
        cm = self.sources["CM"]
        cert = cm.certificate
        assert cert["result"] == "R787-original-implicit-CM-value"
        assert cert["original_map_index"] == 4 and cert["original_map_degree"] == "1206"
        assert cert["source_Dixon_digits"] == 518 and cert["new_Dixon_digits_computed"] == 0
        assert cert["characteristic_zero_B0_nonzero_certified"] and cert["exact_finite_y_implicit_expression_defined"]
        for key in BASE:
            assert str(cm.tag["source_identities"]["R787"][key]) == str(self.sources["R787"].item[key])
        assert cm.tag["source_identities"]["R787"]["configuration_sha256"] == OLD_TAG
        expression = cm.get_spec(cert["implicit_expression"])
        assert expression["original_field"] == self.field.description
        assert expression["original_relation_exactly_defined_by_unit_chart"] is True
        assert expression["unit_chart_solve"]["free_column"] == FREE
        unit = cm.get_spec(cert["denominator_unit_witness"])
        assert unit["all_14_branches_units"] and unit["characteristic_zero_B0_nonzero_certified"]
        candidate = cm.get_spec(cert["coordinate_candidates"])
        qinfo = candidate["candidates"]["value_y0"]
        assert qinfo["all14_reconstructed"] is True and len(qinfo["coordinates"]) == 14
        qq = [decode_q(x) for x in qinfo["coordinates"]]
        index = cm.get_spec(cert["power5_CM_values_and_jets"])
        assert index["dimension"] == N and index["integer_scale"] == SCALE
        ee = [None]*N
        value_specs = []
        for item in index["completed_blocks"]:
            if not item["file"].startswith("R787-implicit-CM-power-5-jets-block-"):
                continue
            self.budget()
            data = cm.get_spec(item)
            assert data["power"] == 5 and data["integer_scale"] == SCALE
            assert data["exact_K_basis"] == "1,s; s^2=-3"
            for row in data["rows"]:
                i = int(row["index"])
                assert ee[i] is None
                ee[i] = [decode_q(x) for x in row["value"]]
            value_specs.append(plain(item))
        assert all(value is not None and len(value) == 2 for value in ee)
        ez_index = cm.get_spec(cert["exact_eZ"])
        assert ez_index["columns"] == D and ez_index["integer_scale"] == SCALE
        assert ez_index["exact_K_basis"] == "1,s; s^2=-3" and ez_index["eZ_computed_in_characteristic_zero"]
        ez = [None]*D
        for item in ez_index["blocks"]:
            self.budget()
            data = cm.get_spec(item)
            assert data["Z_pivot_rows_already_include_minus_sign"] is True
            assert plain(data["exact_original_Z"]) == self.sources["R787"].files[BLOCKS]
            assert plain(data["power5_jets"]) == plain(cert["power5_CM_values_and_jets"])
            for row in data["rows"]:
                i = int(row["index"])
                assert ez[i] is None
                ez[i] = [decode_q(x) for x in row["value"]]
        assert all(value is not None and len(value) == 2 for value in ez)

        def multiply_k(a, b):
            return [a*qq[i]-3*b*qq[7+i] for i in range(7)]+[b*qq[i]+a*qq[7+i] for i in range(7)]

        A = [[value[0]]+[fmpq(0)]*6+[value[1]]+[fmpq(0)]*6 for value in ee]
        P = [[-x for x in multiply_k(*ez[j])] for j in self.pivots]
        denominator = 1
        for row in A+P:
            for x in row:
                denominator = math.lcm(denominator, int(x.denom()))
        target = [[str(int((x*denominator).numer())) for x in row] for row in A+P]
        target.extend([["0"]*14 for _ in range(140)])
        assert all((x*denominator).denom() == 1 for row in A+P for x in row)
        addend = [x*denominator for x in multiply_k(*ez[FREE])]
        self.store(name, {"candidate_y": [encode_q(x) for x in qq],
            "candidate_y_source": cert["coordinate_candidates"], "candidate_y_field": "value_y0",
            "target_common_positive_denominator": str(denominator),
            "target_integer_L_rows": target,
            "free_obstruction_addend_d_q_Ef": [encode_q(x) for x in addend],
            "original_e_values": value_specs, "original_eZ_index": cert["exact_eZ"],
            "original_B0_nonzero_witness": cert["denominator_unit_witness"],
            "original_unit_chart_expression": cert["implicit_expression"],
            "original_scale_applied_once": SCALE, "old_CM_values_or_eZ_recomputed": False,
            "original_value_identity_not_yet_accepted": True})
        return self.cached(name)

    def audit(self):
        name = PREFIX+"source-audit"
        cached = self.cached(name)
        if cached:
            return spec(self.path(name))
        self.store(name, {"source_identities": self.tag["source_identities"],
            "original_A_rows": self.rowsJ, "original_Schur_rows_in_full_order": self.rowsI,
            "original_outside_rows": self.outside, "original_pivot_columns": self.pivots,
            "original_free_column": FREE, "original_complete_branch_stages":
                [branch["source"] for branch in self.operator.branches],
            "old_prime_inverses_read_without_recomputation": True,
            "A_inverse_over_Q_computed": False, "old_primal_current_consumed": False,
            "pairing": spec(self.path(PREFIX+"coefficient-pairing")),
            "exact_target": spec(self.path(PREFIX+"exact-target")),
            "original_exact_129_real_rows_read": N,
            "new_dual_precision_begins_at_one": True})
        return spec(self.path(name))

    @staticmethod
    def square_rows(value):
        return value["A"]+value["P"]+value["outside"]

    @staticmethod
    def split_rows(rows):
        shape(rows, 2560, 14)
        return {"A": rows[:N], "P": rows[N:N+RANK], "outside": rows[N+RANK:]}

    def current_name(self, digits):
        return PREFIX+"current-"+str(digits).zfill(8)

    def current_value(self, current):
        assert current["prime"] == ELL and int(current["modulus"]) == ELL**current["digits"]
        assert current["exact_target"] == spec(self.path(PREFIX+"exact-target"))
        assert current["full_square_modular_identity_verified"] is True
        values = [[int(x) for x in row] for row in current["chi_integer_coordinates"]]
        shape(values, 128, 280)
        modulus = int(current["modulus"])
        assert all(0 <= x < modulus for row in values for x in row)
        return values

    def repair_history_and_compact(self, current):
        """Only IO/ledger work after a complete current has been committed."""
        digits = current["digits"]
        latest_spec = spec(self.path(self.current_name(digits)))
        name = PREFIX+"checkpoint-history"
        old = self.cached(name)
        entries = [] if old is None else old["entries"]
        indexed = {row["digits"]: row for row in entries}
        if digits not in indexed:
            if digits > 1:
                assert digits-1 in indexed
                assert current["previous_completed_checkpoint_sha256"] == indexed[digits-1]["checkpoint"]["sha256"]
            else:
                assert not entries
            row = {"digits": digits, "checkpoint": latest_spec,
                   "previous_completed_checkpoint_sha256": current.get("previous_completed_checkpoint_sha256"),
                   "full_square_modular_identity_verified": True}
            if current.get("step_intermediates"):
                row["step_intermediates"] = current["step_intermediates"]
            entries.append(row)
            self.store(name, {"entries": entries, "latest_digits": digits,
                "latest_checkpoint": latest_spec, "history_entries_are_hash_records_not_required_live_arrays": True})
        else:
            assert indexed[digits]["checkpoint"] == latest_spec
            assert digits == max(indexed)
        save(self.path(PREFIX+"current-index"), {"complete": False, "configuration": self.tag,
            "latest_complete_checkpoint": latest_spec, "digits": digits,
            "history": spec(self.path(name))})
        # Once the new current and its history are committed, old arrays are
        # redundant: the current reduces to all earlier precisions. Hash history
        # remains explicit; no old current is represented as a live file.
        for path in self.out.glob(PREFIX+"current-*.json.gz"):
            match = re.fullmatch(re.escape(PREFIX)+r"current-(\d{8})\.json\.gz", path.name)
            if match and int(match.group(1)) < digits:
                old_number = int(match.group(1))
                assert old_number in {entry["digits"] for entry in entries}
                path.unlink()
        for item in current.get("step_intermediates", []):
            path = self.out/item["file"]
            if path.exists():
                assert spec(path) == item
                path.unlink()
        self.latest = current

    def restore_current(self):
        found = []
        for path in self.out.glob(PREFIX+"current-*.json.gz"):
            match = re.fullmatch(re.escape(PREFIX)+r"current-(\d{8})\.json\.gz", path.name)
            if match:
                found.append((int(match.group(1)), path))
        if not found:
            return None
        number, path = max(found)
        current = self.cached(path.name.removesuffix(".json.gz"))
        assert current["digits"] == number
        self.current_value(current)
        self.repair_history_and_compact(current)
        return current

    def initial_current(self):
        target = [[int(x) % ELL for x in row] for row in self.target["target_integer_L_rows"]]
        solution = self.operator.solve_mod_prime(self.split_rows(target))
        actual = self.square_rows(self.operator.apply_mod(solution, ELL))
        assert actual == target, "The new transpose RHS did not verify in all original coordinates."
        value = {"prime": ELL, "digits": 1, "modulus": str(ELL),
            "chi_integer_coordinates": [[str(x) for x in row] for row in solution],
            "exact_target": spec(self.path(PREFIX+"exact-target")),
            "source_audit": self.source_audit, "previous_completed_checkpoint_sha256": None,
            "full_square_modular_identity_verified": True,
            "verification": "new RHS; all 2560*14 original coordinates verified modulo the original prime",
            "old_primal_precision_or_vector_reused_as_dual": False}
        self.store(self.current_name(1), value)
        current = self.cached(self.current_name(1))
        self.repair_history_and_compact(current)
        return current

    def step(self, current):
        self.budget()
        digits, modulus = current["digits"], int(current["modulus"])
        next_digits = digits+1
        old_spec = spec(self.path(self.current_name(digits)))
        old_values = self.current_value(current)
        prefix = PREFIX+"step-"+str(next_digits).zfill(8)
        residue_name, correction_name = prefix+"-positive-residual", prefix+"-prime-correction"
        residual = self.cached(residue_name)
        if residual is None:
            actual = self.square_rows(self.operator.apply_mod(old_values, modulus*ELL))
            target = self.target["target_integer_L_rows"]
            divided = []
            for left, right in zip(actual, target):
                values = [(x-int(y)) % (modulus*ELL) for x, y in zip(left, right)]
                assert all(x % modulus == 0 for x in values), "The complete retained dual current lost divisibility."
                divided.append([x//modulus for x in values])
            self.store(residue_name, {"from_current": old_spec,
                "digits_divided": digits, "division_in_original_L_coordinates_before_branch_evaluation": True,
                "positive_residual_divided_mod_prime": divided,
                "all35840_coordinates_divisible_by_previous_modulus": True})
            residual = self.cached(residue_name)
        assert residual["from_current"] == old_spec and residual["digits_divided"] == digits
        divided = residual["positive_residual_divided_mod_prime"]
        shape(divided, 2560, 14)
        assert all(0 <= x < ELL for row in divided for x in row)
        correction = self.cached(correction_name)
        if correction is None:
            rhs = [[(-int(x)) % ELL for x in row] for row in divided]
            delta = self.operator.solve_mod_prime(self.split_rows(rhs))
            verified = self.square_rows(self.operator.apply_mod(delta, ELL))
            assert verified == rhs, "The full new transpose correction did not cancel the divided positive residual."
            self.store(correction_name, {"from_current": old_spec,
                "positive_residual": spec(self.path(residue_name)),
                "chi_prime_correction": delta, "all35840_prime_correction_coordinates_verified": True,
                "RHS_is_negative_divided_positive_residual": True})
            correction = self.cached(correction_name)
        assert correction["from_current"] == old_spec
        assert correction["positive_residual"] == spec(self.path(residue_name))
        assert correction["all35840_prime_correction_coordinates_verified"] is True
        delta = correction["chi_prime_correction"]
        shape(delta, 128, 280)
        values = [[a+modulus*int(b) for a, b in zip(row, change)] for row, change in zip(old_values, delta)]
        assert all(0 <= x < modulus*ELL for row in values for x in row)
        value = {"prime": ELL, "digits": next_digits, "modulus": str(modulus*ELL),
            "chi_integer_coordinates": [[str(x) for x in row] for row in values],
            "exact_target": spec(self.path(PREFIX+"exact-target")), "source_audit": self.source_audit,
            "previous_completed_checkpoint_sha256": old_spec["sha256"],
            "step_intermediates": [spec(self.path(residue_name)), spec(self.path(correction_name))],
            "full_square_modular_identity_verified": True,
            "verification": "all original positive residual coordinates divisible; all prime corrections cancel; exact linearity",
            "old_primal_precision_or_vector_reused_as_dual": False}
        self.store(self.current_name(next_digits), value)
        completed = self.cached(self.current_name(next_digits))
        self.repair_history_and_compact(completed)
        return completed

    def reconstruction(self, current):
        digits, modulus = current["digits"], int(current["modulus"])
        name = PREFIX+"reconstruction-attempt-"+str(digits).zfill(8)
        old = self.cached(name)
        if old is not None:
            return old.get("witness")
        denominator, coordinates = 1, []
        for i, row in enumerate(current["chi_integer_coordinates"]):
            self.budget()
            values = []
            for j, text in enumerate(row):
                value = self.legacy.rational_reconstruct(int(text), modulus)
                if value is None:
                    self.store(name, {"source_current": spec(self.path(self.current_name(digits))),
                        "digits": digits, "all35840_coordinates_reconstructed": False,
                        "first_failed_coordinate": [i, j], "candidate_y_rejected": False,
                        "new_dual_precision_not_original_primal_precision": True})
                    return None
                denominator = math.lcm(denominator, int(value.denom()))
                values.append(value)
            coordinates.append(values)
        numerators = [[str(int(value.numer())*(denominator//int(value.denom()))) for value in row]
                      for row in coordinates]
        raw = {"coordinate_numerators": numerators, "common_positive_denominator": str(denominator)}
        key = fingerprint(raw)
        witness_name = PREFIX+"witness-"+key
        if self.cached(witness_name) is None:
            self.store(witness_name, dict(raw,
                source_current=spec(self.path(self.current_name(digits))),
                reconstructed_at_dual_digits=digits, exact_target=spec(self.path(PREFIX+"exact-target")),
                candidate_only_until_full_exact_transpose_verification=True,
                projective_rescaling_or_content_removal_used=False))
        witness = spec(self.path(witness_name))
        self.store(name, {"source_current": spec(self.path(self.current_name(digits))),
            "digits": digits, "all35840_coordinates_reconstructed": True,
            "witness": witness, "candidate_y_rejected": False,
            "new_dual_precision_not_original_primal_precision": True})
        return witness

    def exact_element(self, name, function, dependencies):
        cached = self.cached(name)
        if cached is None:
            self.budget()
            value = function()
            self.store(name, {"dependencies": dependencies, "value": self.field.encode(value)})
            return value
        assert cached["dependencies"] == dependencies
        return self.field.decode(cached["value"])

    def exact_reverse_convolution(self, base, witness, values, denominator):
        name = base+"-reverse-convolution"
        cached = self.cached(name)
        if cached is not None:
            assert cached["witness"] == witness
            return cached
        self.budget()
        rden = 1
        for value in self.R:
            rden = math.lcm(rden, int(value.scale.denom()))
        aa, bb = [0]*(1521*129), [0]*(1521*129)
        indices = [r+39*i+507*j for j in range(2) for i in range(7) for r in range(20)]
        for n in range(129):
            scalar = self.R[n].scale*rden
            assert scalar.denom() == 1
            left = [int(x)*int(scalar.numer()) for x in self.field.vector(self.R[n])]
            right = values[127-n] if n < 128 else [0]*280
            offset = 1521*n
            for index, a, b in zip(indices, left, right):
                aa[offset+index], bb[offset+index] = a, int(b)
        product = fmpz_poly(aa).mul_low(fmpz_poly(bb), 1521*129)
        del aa, bb
        vectors = []
        for n in range(129):
            offset = 1521*n
            rows = []
            for j in range(2):
                for i in range(13):
                    if j == 0:
                        rows.append([int(product[offset+r+39*i])-3*int(product[offset+r+39*i+1014])
                                     for r in range(39)])
                    else:
                        rows.append([int(product[offset+r+39*i+507]) for r in range(39)])
            reduced = self.field.Bred*fmpz_mat(rows)*self.field.Tred
            vectors.append([str(reduced[i, r]) for i in range(14) for r in range(20)])
        self.store(name, {"witness": witness,
            "convolution_integer_vectors_in_increasing_v_order": vectors,
            "common_positive_denominator": str(rden*denominator),
            "packed_stride1521_and_original_reductions": True,
            "chi_zero_at_reversed_order128": True,
            "old_R_or_kappa_powers_recomputed": False})
        return self.cached(name)

    def rational_elements_to_integer_rows(self, values):
        denominator = 1
        for value in values:
            denominator = math.lcm(denominator, int(value.scale.denom()))
        blocks = []
        for value in values:
            factor = value.scale*denominator
            assert factor.denom() == 1
            blocks.append([int(x)*int(factor.numer()) for x in self.field.vector(value)])
        return self.operator.to_rows(blocks), denominator

    def exact_matrix_product(self, base, suffix, matrix, integer_rows, denominator, witness):
        result, specs = [], []
        for first in range(0, N, 64):
            self.budget()
            stop = min(first+64, N)
            name = base+"-"+suffix+"-"+str(first).zfill(4)
            cached = self.cached(name)
            if cached is None:
                block = fmpz_mat([[int(matrix[i, j]) for j in range(matrix.ncols())]
                                 for i in range(first, stop)])*fmpz_mat(integer_rows)
                rows = [[str(block[i, j]) for j in range(14)] for i in range(stop-first)]
                self.store(name, {"witness": witness, "first_row": first, "stop_row": stop,
                    "integer_coordinate_rows": rows, "common_positive_denominator": str(denominator),
                    "all_original_input_rows_used": matrix.ncols()})
                cached = self.cached(name)
            assert cached["witness"] == witness and cached["first_row"] == first and cached["stop_row"] == stop
            assert int(cached["common_positive_denominator"]) == denominator
            shape(cached["integer_coordinate_rows"], stop-first, 14)
            result.extend([[int(x) for x in row] for row in cached["integer_coordinate_rows"]])
            specs.append(spec(self.path(name)))
        assert len(result) == N
        return result, specs

    def reject_witness(self, base, witness, region, row, column, residual):
        name = base+"-not-an-exact-dual-witness"
        self.store(name, {"witness": witness, "first_failed_region": region,
            "first_failed_row": row, "first_failed_L_coordinate": column,
            "exact_nonzero_residual": encode_q(residual),
            "only_this_reconstructed_dual_vector_rejected": True,
            "original_candidate_y_strictly_rejected": False})
        return None

    def verify_exact(self, witness):
        witness_path = self.out/witness["file"]
        assert spec(witness_path) == witness
        w = read(witness_path)
        assert w["complete"] and w["configuration"] == self.tag
        assert w["exact_target"] == spec(self.path(PREFIX+"exact-target"))
        base = witness["file"].removesuffix(".json.gz")
        finished = self.cached(base+"-exact-value-obstruction")
        if finished is not None:
            return spec(self.path(base+"-exact-value-obstruction"))
        if self.cached(base+"-not-an-exact-dual-witness") is not None:
            return None
        numerator = [[int(x) for x in row] for row in w["coordinate_numerators"]]
        denominator = int(w["common_positive_denominator"])
        shape(numerator, 128, 280)
        assert denominator > 0
        chi = [self.field.from_vector(row, fmpq(1, denominator)) for row in numerator]
        lambda_values, lambda_specs = [], []
        for m in range(1, 129):
            name = base+"-lambda-"+str(m).zfill(3)
            value = self.exact_element(name,
                lambda m=m: self.operator.pair_exact(self.field.multiply(self.K[m+1], chi[m-1]).scaled(246**3)),
                {"witness": witness, "m": m, "kappa_exponent": m+1})
            lambda_values.append(value)
            lambda_specs.append(spec(self.path(name)))
        lam_rows, lam_den = self.rational_elements_to_integer_rows(lambda_values)
        for i, row in enumerate(self.outside):
            for k, value in enumerate(lam_rows[row]):
                if value:
                    return self.reject_witness(base, witness, "outside", i, k, fmpq(value, lam_den))
        AA, a_specs = self.exact_matrix_product(base, "A-transpose", self.operator.FAt,
                                               lam_rows, lam_den, witness)
        target = self.target["target_integer_L_rows"]
        for i, row in enumerate(AA):
            for k, value in enumerate(row):
                residual = fmpq(value, lam_den)-int(target[i][k])
                if residual:
                    return self.reject_witness(base, witness, "A", i, k, residual)
        conv = self.exact_reverse_convolution(base, witness, numerator, denominator)
        cden = int(conv["common_positive_denominator"])
        conv_spec = spec(self.path(base+"-reverse-convolution"))
        vv, v_specs = [], []
        for j in range(129):
            name = base+"-V-"+str(j).zfill(3)
            def form(j=j):
                row = conv["convolution_integer_vectors_in_increasing_v_order"][128-j]
                u = self.field.from_vector([int(x) for x in row], fmpq(1, cden))
                return self.operator.pair_exact(self.field.multiply(self.K[j], u))
            vv.append(self.exact_element(name, form,
                {"witness": witness, "reverse_convolution": conv_spec, "j": j, "kappa_exponent": j}))
            v_specs.append(spec(self.path(name)))
        vrows, vden = self.rational_elements_to_integer_rows(vv)
        YY, y_specs = self.exact_matrix_product(base, "B-pre-Z-transpose", self.operator.Ft,
                                               vrows, vden, witness)
        zname = base+"-B-Z-transpose"
        zz_stage = self.cached(zname)
        if zz_stage is None:
            self.budget()
            ZZ = self.operator.z_transpose(YY)
            self.store(zname, {"witness": witness, "source_products": y_specs,
                "common_positive_denominator": str(vden),
                "original_Z_transpose_integer_coordinate_rows": [[str(x) for x in row] for row in ZZ],
                "Z_pivot_sign_preserved": True, "Z_free_diagonal_applied_once": True})
            zz_stage = self.cached(zname)
        assert zz_stage["witness"] == witness and zz_stage["source_products"] == y_specs
        assert int(zz_stage["common_positive_denominator"]) == vden
        ZZ = [[int(x) for x in row] for row in zz_stage["original_Z_transpose_integer_coordinate_rows"]]
        shape(ZZ, D, 14)
        for i, original_column in enumerate(self.pivots):
            for k, value in enumerate(ZZ[original_column]):
                residual = fmpq(value, vden)-int(target[N+i][k])
                if residual:
                    return self.reject_witness(base, witness, "P", i, k, residual)
        full_name = base+"-exact-transpose-certificate"
        if self.cached(full_name) is None:
            self.store(full_name, {"witness": witness, "exact_target": spec(self.path(PREFIX+"exact-target")),
                "lambda_blocks": lambda_specs, "A_transpose_products": a_specs,
                "reverse_convolution": conv_spec, "V_blocks": v_specs,
                "B_pre_Z_transpose_products": y_specs, "B_Z_transpose": spec(self.path(zname)),
                "all35840_rational_coordinates_verified": True,
                "verified_L_coordinate_groups": [1234, 1186, 140],
                "ordinary_transpose_not_Hermitian": True,
                "old_exact_CM_response_recomputed": False})
        addend = [decode_q(x) for x in self.target["free_obstruction_addend_d_q_Ef"]]
        delta = [fmpq(ZZ[FREE][k], vden)+addend[k] for k in range(14)]
        accepted = all(not x for x in delta)
        result_name = base+"-exact-value-obstruction"
        self.store(result_name, {"witness": witness,
            "exact_transpose_certificate": spec(self.path(full_name)),
            "Delta_original_L_coordinates": [encode_q(x) for x in delta],
            "identity": "d*(A0-q*B0)=-Delta for the original normalized free-1186 relation",
            "target_common_positive_denominator": self.target["target_common_positive_denominator"],
            "dual_linear_system_exactly_solved": True,
            "original_value_rowspace_zero_A1_proved": accepted,
            "original_candidate_y_strictly_rejected": not accepted,
            "original_candidate_y_source": self.target["candidate_y_source"],
            "exact_original_y_value_coordinates": self.target["candidate_y"] if accepted else None,
            "expanded_x_and_derivative_acceptance_requires_separate_small_L_source": True,
            "actual_eta_or_height_computed": False})
        return spec(self.path(result_name))

    def inventory(self):
        files, currents = [], []
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name.startswith(PREFIX+"stage-manifest-"):
                continue
            data = read(path)
            assert data["configuration"] == self.tag
            (files if data.get("complete") is True else currents).append(spec(path))
        body = {"files": files, "current_checkpoints": currents,
            "historical_full_current_arrays_compacted_after_committed_new_current": True,
            "history_only_old_SHA_records": spec(self.path(PREFIX+"checkpoint-history"))
                if self.path(PREFIX+"checkpoint-history").exists() else None}
        name = PREFIX+"stage-manifest-"+fingerprint(body)[:24]
        if self.cached(name) is None:
            self.store(name, body)
        return spec(self.path(name))

    def finish(self, obstruction=None, reason=None):
        solved, accepted, rejected = False, False, False
        if obstruction:
            path = self.out/obstruction["file"]
            assert spec(path) == obstruction
            value = read(path)
            assert value["configuration"] == self.tag and value["complete"]
            solved = value["dual_linear_system_exactly_solved"]
            accepted = value["original_value_rowspace_zero_A1_proved"]
            rejected = value["original_candidate_y_strictly_rejected"]
            assert solved and accepted != rejected
        value = {"result": RESULT, "configuration": self.tag, "complete": solved,
            "p": 41, "original_map_index": 4, "original_map_degree": "1206",
            "source_audit": self.source_audit, "exact_target": spec(self.path(PREFIX+"exact-target")),
            "source_CM_Dixon_digits": 518, "source_CM_Dixon_digits_used_as_dual_precision": False,
            "actual_new_dual_digits": None if self.latest is None else self.latest["digits"],
            "latest_dual_current": None if self.latest is None else spec(self.path(self.current_name(self.latest["digits"]))),
            "dual_linear_system_exactly_solved": solved,
            "original_value_rowspace_zero_A1_proved": accepted,
            "original_candidate_y_strictly_rejected": rejected,
            "exact_original_y_value_accepted": accepted,
            "original_expanded_x_and_derivative_accepted": False,
            "old_primal_inverse_Laurent_CM_or_function_Dixon_arithmetic_recomputed": False,
            "old_primal_complete_function_recipe_produced": False,
            "actual_eta_or_height_computed": False,
            "exact_value_obstruction": obstruction, "reason": reason,
            "resume_state": spec(self.path(PREFIX+"current-index"))
                if self.path(PREFIX+"current-index").exists() else None,
            "stage_manifest": self.inventory(), "seconds": time.monotonic()-self.started}
        save(self.out/FINAL, value)
        return value

    def run(self):
        final_path = self.out/FINAL
        if final_path.exists():
            value = read(final_path)
            assert value["configuration"] == self.tag
            if value["complete"] is True:
                item = value["stage_manifest"]
                assert spec(self.out/item["file"]) == item
                inventory = read(self.out/item["file"])
                for row in inventory["files"]+inventory["current_checkpoints"]:
                    assert spec(self.out/row["file"]) == row
                return value
        current = self.restore_current()
        if current is None:
            current = self.initial_current()
        start_digits = current["digits"]
        every = int(self.item.get("reconstruct_every_digits", 8))
        added_limit = self.item.get("maximum_new_digits")
        if added_limit is not None:
            added_limit = int(added_limit)
            assert added_limit >= 0
        assert every >= 1
        while True:
            self.budget()
            if current["digits"] % every == 0 or bool(self.item.get("try_reconstruction_at_start", True)) and current["digits"] == start_digits:
                witness = self.reconstruction(current)
                if witness:
                    obstruction = self.verify_exact(witness)
                    if obstruction:
                        return self.finish(obstruction)
            if added_limit is not None and current["digits"]-start_digits >= added_limit:
                return self.finish(reason="requested number of genuinely new dual digits reached; no exact decision")
            current = self.step(current)


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New arithmetic runs only in the public repository Actions.")
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--proof", type=Path, required=True)
    parser.add_argument("--method", type=Path, required=True)
    parser.add_argument("--legacy-core", type=Path, required=True)
    parser.add_argument("--field-core", type=Path, required=True)
    parser.add_argument("--retained", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, required=True)
    args = parser.parse_args()
    assert args.budget_minutes > 0
    started, job, final, error, code = time.monotonic(), None, None, None, 1
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        job = Job(args)
        final = job.run()
        code = 0 if final["complete"] else 2
    except BudgetStop as exc:
        error, code = str(exc), 124
        if job is not None:
            final = job.finish(reason=error)
    except BaseException as exc:
        error = type(exc).__name__+": "+str(exc)
        traceback.print_exc()
        if isinstance(exc, KeyboardInterrupt):
            code = 130
    receipt = {"result": RESULT, "source_sha256": sha(__file__),
        "configuration": None if job is None else job.tag,
        "complete": bool(final and final["complete"]), "exit_code": code,
        "actual_new_dual_digits": final["actual_new_dual_digits"] if final is not None else
            None if job is None or job.latest is None else job.latest["digits"],
        "dual_linear_system_exactly_solved": bool(final and final["dual_linear_system_exactly_solved"]),
        "original_value_rowspace_zero_A1_proved": bool(final and final["original_value_rowspace_zero_A1_proved"]),
        "original_candidate_y_strictly_rejected": bool(final and final["original_candidate_y_strictly_rejected"]),
        "old_primal_or_CM_arithmetic_recomputed": False,
        "seconds": time.monotonic()-started, "error": error,
        "final": spec(args.output/FINAL) if final is not None else None}
    save(args.output/"core-receipt.json", receipt)
    print("DUAL_RECEIPT="+json.dumps(receipt, sort_keys=True, separators=(",", ":")), flush=True)
    return code


if __name__ == "__main__":
    sys.exit(main())
