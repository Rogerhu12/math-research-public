#!/usr/bin/env python3
"""R824: source-bound original weight-five/six polar generators.

All arithmetic belongs to this public repository's Actions.  The original
R787 reserved free column is consumed only after its own exact completion.
"""
from __future__ import annotations

import argparse
import gc
import gzip
import hashlib
import importlib.util
import json
import math
import os
import re
import sys
import time
from functools import lru_cache
from pathlib import Path

import flint
from flint import (
    fmpq, fmpq_mat, fmpz, fmpz_mat, fmpz_poly, nmod_mat, nmod_poly,
    fmpz_mod_ctx, fmpz_mod_mat, fmpz_mod_poly_ctx,
)

RESULT = "R824-original-global-polar-generators"
FINAL = "p41-original-global-polar-generators-certificate.json"
FIELD_CORE_SHA = "d024a7a6f5febd4658e8b5b5e5e3659f3c5fcc0daa39d70569ac408ef83a8751"
OLD_CORE_SHA = "93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04"
PROOF_SHA = "3a32e69f5ff3fb74ad7b262357e6b9d00da5e1f4348f65b1cdc0705d6fef7be1"
ORIGINAL_PRIME = 1000000753
DIMENSION = {5: 1234, 6: 1506}
ORDERS = {5: 129, 6: 142}
KERNEL_DIMENSION = {5: 28, 6: 300}
REAL, LDEG, FDEG, PACK = 20, 14, 280, 1521
RESERVED_FREE_COLUMN = 1186
PINNED_OLD_FILES = {
    "R787-prime-1000000753-chart.json.gz":
        "47ac1ce2a95781417a4e3b51f2128d2dd4836e5d1793cf2a50793911dcedce96",
    "R787-prime-1000000753-selection.json.gz":
        "a420d94a9a2f56fa449946bac6379f437e7e53120a651d7df95b5f9ef9b07adb",
    "R787-prime-1000000753-branch-00.json.gz":
        "c5b75f48b5c5d1cf2d98390e814a245306fa63f10ae43dae194dbfd560d895d7",
    "R787-prime-1000000753-rational-blocks.json.gz":
        "fb8a82957474e657fc476aa2baa0d8ce9f4c8b6cc86c2b55a79e75913d610b3b",
}


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New R824 arithmetic is restricted to public repository Actions.")


def sha(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(
            path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    data = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if path.suffix == ".gz":
        with temporary.open("wb") as raw:
            with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0,
                              compresslevel=2) as stream:
                stream.write(data)
    else:
        temporary.write_bytes(data)
    temporary.replace(path)


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def plain_spec(value):
    return {key: value[key] for key in ("file", "bytes", "sha256")}


def imatrix(matrix):
    return [[int(matrix[i, j]) for j in range(matrix.ncols())]
            for i in range(matrix.nrows())]


def smatrix(matrix):
    return [[str(matrix[i, j]) for j in range(matrix.ncols())]
            for i in range(matrix.nrows())]


def submatrix(matrix, rows, columns=None, prime=None):
    if columns is None:
        columns = range(matrix.ncols())
    values = [[int(matrix[i, j]) % prime if prime is not None
               else int(matrix[i, j]) for j in columns] for i in rows]
    return nmod_mat(values, prime) if prime is not None else fmpz_mat(values)


def pivots(matrix):
    reduced, rank = matrix.rref()
    result = [next(j for j in range(reduced.ncols()) if reduced[i, j])
              for i in range(rank)]
    assert result == sorted(set(result))
    return result


def is_zero(matrix):
    return all(not matrix[i, j] for i in range(matrix.nrows())
               for j in range(matrix.ncols()))


def rational_reconstruct(value, modulus):
    value %= modulus
    if value == 0:
        return fmpq(0)
    bound = math.isqrt((modulus - 1) // 2)
    r0, r1, t0, t1 = modulus, value, 0, 1
    while abs(r1) > bound:
        quotient = r0 // r1
        r0, r1, t0, t1 = r1, r0 - quotient * r1, t1, t0 - quotient * t1
    if not t1 or abs(t1) > bound or math.gcd(r1, t1) != 1:
        return None
    if t1 < 0:
        r1, t1 = -r1, -t1
    if 2 * abs(r1) * t1 >= modulus or (value * t1 - r1) % modulus:
        return None
    return fmpq(r1, t1)


def next_prime(value):
    candidate = int(value)+1
    if candidate > 2 and candidate % 2 == 0:
        candidate += 1
    while not bool(fmpz(candidate).is_prime()):
        candidate += 1 if candidate == 2 else 2
    return candidate


class BudgetStop(RuntimeError):
    pass


class BadPrime(RuntimeError):
    pass


class Source:
    """One immutable producer identity; transfer location is not mathematics."""

    def __init__(self, root, label, identity):
        self.label, self.identity = label, identity
        self.directory = Path(root) / label
        manifest_path = self.directory / "full-outputs-manifest.json"
        assert sha(manifest_path) == identity["manifest_sha256"]
        manifest = read(manifest_path)
        assert manifest["result"] == identity["result"]
        self.files = {row["file"]: row for row in manifest["files"]}
        assert len(self.files) == len(manifest["files"])
        run = self.raw("run-receipt.json")
        assert str(run["workflow_run_id"]) == str(identity["run_id"])
        assert run["source_commit"] == identity["source_commit"]
        receipt = self.raw("core-receipt.json")
        assert receipt["source_sha256"] == identity["core_sha256"]
        certificate_name = identity.get("certificate_name")
        if certificate_name is None:
            assert label == "R787", "Only the explicitly retained R787 checkpoint may be partial."
            self.certificate = None
            config_source = self.raw("R787-prime-1000000753-chart.json.gz")
        else:
            self.certificate = self.raw(certificate_name)
            assert self.certificate["complete"] is True
            assert self.certificate["result"] == identity["result"]
            config_source = self.certificate
        self.tag = config_source["configuration"]
        assert self.tag["source_sha256"] == identity["core_sha256"]
        self.stable_identity = {
            key: identity[key] for key in
            ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
        }
        if certificate_name is not None:
            self.stable_identity["certificate"] = plain_spec(self.files[certificate_name])

    def path(self, name):
        assert Path(name).name == name
        path = self.directory / name
        entry = self.files[name]
        assert path.stat().st_size == entry["bytes"] and sha(path) == entry["sha256"]
        return path

    def raw(self, name):
        return read(self.path(name))

    def stage(self, name, expected=None):
        if expected is not None:
            assert plain_spec(self.files[name]) == plain_spec(expected)
        value = self.raw(name)
        assert value["complete"] is True
        assert value["configuration"] == self.tag
        return value

    def stage_spec(self, entry):
        return self.stage(entry["file"], entry)

    def file_spec(self, name):
        return dict(plain_spec(self.files[name]), producer=self.label)


class PackedField:
    """Exact two-factor arithmetic in the fixed integral 7*2*20 basis."""

    def __init__(self, field, modulus=None):
        self.field, self.modulus = field, modulus
        self.indices = [r + 39*i + 507*j for j in range(2)
                        for i in range(7) for r in range(20)]
        if modulus is None:
            self.poly = fmpz_poly
            self.Bred, self.Tred = field.Bred, field.Tred
        else:
            self.mctx = fmpz_mod_ctx(modulus)
            self.poly = fmpz_mod_poly_ctx(modulus)
            self.Bred = fmpz_mod_mat(imatrix(field.Bred), self.mctx)
            self.Tred = fmpz_mod_mat(imatrix(field.Tred), self.mctx)

    def pack(self, values, count=None, shift=0):
        if count is None:
            count = len(values) + shift
        assert 0 <= shift <= count and len(values) <= count - shift
        result = [0] * (PACK * count)
        for n, row in enumerate(values):
            assert len(row) == FDEG
            offset = PACK * (n + shift)
            for index, coefficient in zip(self.indices, row):
                coefficient = int(coefficient)
                result[offset + index] = (coefficient % self.modulus
                                          if self.modulus is not None else coefficient)
        return self.poly(result)

    def reduce_block(self, polynomial, exponent):
        offset = PACK * exponent
        rows = []
        for j in range(2):
            for i in range(13):
                if j == 0:
                    rows.append([int(polynomial[offset+r+39*i]) -
                                 3*int(polynomial[offset+r+39*i+1014])
                                 for r in range(39)])
                else:
                    rows.append([int(polynomial[offset+r+39*i+507])
                                 for r in range(39)])
        if self.modulus is None:
            reduced = self.Bred * fmpz_mat(rows) * self.Tred
        else:
            matrix = fmpz_mod_mat(rows, self.mctx)
            reduced = self.Bred * matrix * self.Tred
        return [int(reduced[i, r]) for i in range(14) for r in range(20)]

    def operator_product(self, operator, A, B):
        count = int(operator["orders"])
        assert len(A) == len(B) == count
        U = self.pack(operator["U_integer_coordinates"], count)
        Q = self.pack([operator["Q_integer_coordinates"]], 1)
        bpoly = self.pack(B, count)
        apoly = self.pack(A[:-1], count, shift=1)
        return U.mul_low(bpoly, PACK*count) + Q.mul_low(apoly, PACK*count)

    def residual(self, operator, A, B):
        total = self.operator_product(operator, A, B)
        return [self.reduce_block(total, m) for m in range(operator["orders"])]


class Job:
    def __init__(self, args):
        guard()
        assert flint.__version__ == "0.9.0"
        self.args, self.out = args, args.output
        self.started = time.monotonic()
        self.item = read(args.config)
        assert self.item["producer_inputs_pending"] is False
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert self.item["core_sha256"] == sha(__file__)
        assert sha(args.proof) == PROOF_SHA == self.item["R824_proof_sha256"]
        assert sha(args.method) == self.item["R824_method_sha256"]
        assert sha(args.field_core) == FIELD_CORE_SHA == self.item["field_core_sha256"]
        self.sources = {
            label: Source(args.retained, label, identity)
            for label, identity in self.item["retained_sources"].items()
            if label != "R787_complete"
        }
        required = {"R781", "R787", "R786", "R795", "R799", "R801", "R798", "R805"}
        assert required <= set(self.sources)
        self.r781, self.r787 = self.sources["R781"], self.sources["R787"]
        assert self.r781.identity["core_sha256"] == FIELD_CORE_SHA
        assert self.r787.identity["core_sha256"] == OLD_CORE_SHA
        for name, digest in PINNED_OLD_FILES.items():
            assert self.r787.files[name]["sha256"] == digest
        assert self.r787.tag["original_map_index"] == 4
        assert self.r787.tag["original_map_degree"] == "1206"
        assert self.r787.tag["ordinary_power"] == 5
        assert self.r787.tag["basis_dimension"] == 1234
        assert self.r787.tag["qY_bound"] == 128
        for label in ("R781", "R786"):
            old = self.r787.tag["retained_artifacts"][label]
            current = self.sources[label].identity
            for key in ("run_id", "source_commit", "core_sha256", "manifest_sha256"):
                assert str(old[key]) == str(current[key])
        field_input = self.r781.stage("R781-original-real-field-input.json.gz")
        loader = importlib.util.spec_from_file_location("R824_retained_R781", args.field_core)
        module = importlib.util.module_from_spec(loader)
        loader.loader.exec_module(module)
        self.field = module.Field(field_input["field"]["original_b_minimal_polynomial"])
        assert self.field.description == field_input["field"]
        self.R, self.K = [], []
        previous = None
        for n in range(143):
            name = "R781-inverse-free-Laurent-" + str(n).zfill(3) + ".json.gz"
            data = self.r781.stage(name)
            assert data["order"] == n and data["exact_differential_identity_at_this_order"] is True
            if n:
                assert data["previous_stage_sha256"] == self.r781.files[previous]["sha256"]
            else:
                assert data["input_stage_sha256"] == self.r781.files[
                    "R781-original-real-field-input.json.gz"]["sha256"]
                self.kappa = self.field.decode(data["kappa"])
            self.R.append(self.field.decode(data["coefficients"]["R"]))
            self.K.append(self.field.decode(data["coefficients"]["kappa_power"]))
            previous = name
        assert self.R[0] == self.K[0] == self.field.one
        assert self.K[1] == self.kappa and self.kappa
        pencil_cert = self.sources["R805"].certificate
        assert pencil_cert["actual_pencil_n"] == 1
        assert pencil_cert["actual_pencil_rank"] == 690
        assert pencil_cert["affine_free_module_rank"] == 272
        assert pencil_cert["graded_free_basis_degrees"] == [1, 144, 127]
        self.pencil = self.sources["R805"].stage_spec(pencil_cert["pencil_stage"])
        assert self.pencil["n"] == 1
        self.selected6 = self.sources["R798"].stage(
            "R798-selected-short-rows.json.gz")
        self.I6 = list(self.selected6["selected_row_indices"])
        assert len(self.I6) == 1506 and len(set(self.I6)) == 1506
        assert all(0 <= row < 1640 for row in self.I6)
        cert801 = self.sources["R801"].certificate
        self.frontier6_spec = cert801["basis_tail_indices"]["6"]
        self.frontier6 = self.sources["R801"].stage_spec(self.frontier6_spec)
        assert self.frontier6["dimension"] == 1506
        assert self.frontier6["coverage_stop"] == 142
        assert self.frontier6["integer_scale"] == str(82**12)
        assert len(self.frontier6["basis_rows"]) == 1506
        assert [row["index"] for row in self.frontier6["basis_rows"]] == list(range(1506))
        cert799 = self.sources["R799"].certificate
        self.index7_spec = cert799["basis_indices"]["7"]
        self.index7 = self.sources["R799"].stage_spec(self.index7_spec)
        assert self.index7["dimension"] == 1778 and self.index7["bound_qY"] == 95
        assert self.index7["integer_scale"] == str(82**14)
        assert self.index7["characteristic_zero_basis_certified"] is True
        assert [row["index"] for row in self.index7["basis_rows"]] == list(range(1778))
        self.I7 = list(self.index7["actual_nonzero_minor"]["coordinate_row_indices"])
        assert len(self.I7) == 1778 and len(set(self.I7)) == 1778
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "R824_proof_sha256": PROOF_SHA, "R824_method_sha256": sha(args.method),
            "R781_field_core_sha256": FIELD_CORE_SHA,
            "source_identities": {key: value.stable_identity for key, value in self.sources.items()},
            "original_map_index": 4, "original_map_degree": 1206,
            "field": self.field.description, "original_basis_dimensions": {"5": 1234, "6": 1506},
            "orders": {"5": 129, "6": 142}, "original_integer_scales": {"5": str(82**10), "6": str(82**12)},
            "generator_profile_weights_5_6_7": [28, 244, 0],
            "source_degree_sum": 1604, "ambient_epsilon_degree_sum": 398,
            "expected_global_colength": 1206,
            "reserved_R787_free_column": RESERVED_FREE_COLUMN,
            "R801_power6_frontier": plain_spec(self.frontier6_spec),
            "R799_power7_short_index": plain_spec(self.index7_spec),
            "R798_selected_rows": plain_spec(self.sources["R798"].files[
                "R798-selected-short-rows.json.gz"]),
            "operator": "D_N*(246^3*kappa^N*v*A+sum(R_n*kappa^(N-1-n)*v^n)*B) mod v^N",
            "packed_q_stride": PACK, "fixed_field_basis_degree": FDEG,
            "reconstruction": "strict 2*A*B<ell^digits; whole original relation checked",
            "new_weight7_or_Laurent_tail": False,
            "original_R787_reserved_target_recomputed": False,
        }
        self.out.mkdir(parents=True, exist_ok=True)
        self.active_power, self.F = None, None
        self.branch_cache = {}
        self.operator_cache = {}

    def budget(self):
        if time.monotonic() - self.started >= self.args.budget_minutes * 60:
            raise BudgetStop("Only complete source-bound stages and each latest lift need continuation.")

    def path(self, name):
        assert "/" not in name and "\\" not in name
        return self.out / (name + ".json.gz")

    def cache(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def store(self, name, value):
        # A completed operation is committed before the next arithmetic budget boundary.
        save(self.path(name), dict(value, complete=True, configuration=self.tag))
        print(json.dumps({"stage": name, "complete": True,
                          "seconds": time.monotonic()-self.started}), flush=True)
        return spec(self.path(name))

    def stored_spec(self, entry):
        path = self.out / entry["file"]
        assert path.name == entry["file"]
        assert plain_spec(spec(path)) == plain_spec(entry)
        return self.cache(path.name.removesuffix(".json.gz"))

    def operator(self, power):
        assert power in ORDERS
        if power in self.operator_cache:
            return self.operator_cache[power]
        count = ORDERS[power]
        name = "R824-common-clear-operator-N" + str(count)
        old = self.cache(name)
        if old is None:
            values, references = [], []
            for n in range(count):
                self.budget()
                stage_name = "R824-common-clear-N" + str(count) + "-coefficient-" + str(n).zfill(3)
                stage = self.cache(stage_name)
                expected = {
                    "R_stage": self.r781.file_spec("R781-inverse-free-Laurent-"+str(n).zfill(3)+".json.gz"),
                    "kappa_stage": self.r781.file_spec(
                        "R781-inverse-free-Laurent-"+str(count-1-n).zfill(3)+".json.gz"),
                }
                if stage is None:
                    value = self.field.multiply(self.R[n], self.K[count-1-n])
                    self.store(stage_name, {"orders": count, "index": n,
                        "sources": expected, "value": self.field.encode(value),
                        "original_R_or_kappa_power_recomputed": False})
                    stage = self.cache(stage_name)
                assert stage["orders"] == count and stage["index"] == n
                assert stage["sources"] == expected
                values.append(self.field.decode(stage["value"]))
                references.append(spec(self.path(stage_name)))
            Q = self.K[count].scaled(246**3)
            denominator = 1
            for value in values + [Q]:
                denominator = math.lcm(denominator, int(value.scale.denom()))
            rows = []
            for value in values + [Q]:
                scalar = value.scale * denominator
                assert scalar.denom() == 1
                rows.append([str(int(x)*int(scalar.numer()))
                             for x in self.field.vector(value)])
            self.store(name, {"ordinary_power": power, "orders": count,
                "common_positive_denominator": str(denominator),
                "U_integer_coordinates": rows[:-1], "Q_integer_coordinates": rows[-1],
                "coefficient_stages": references,
                "Q_original_kappa_source": self.r781.file_spec(
                    "R781-inverse-free-Laurent-"+str(count).zfill(3)+".json.gz"),
                "fixed_rational_multiplier": str(246**3),
                "all_N_original_relations_equivalent_by_nonzero_row_scalings": True,
                "exact_kappa_inverse_computed": False})
            old = self.cache(name)
        assert old["ordinary_power"] == power and old["orders"] == count
        assert len(old["U_integer_coordinates"]) == count
        assert all(len(row) == FDEG for row in old["U_integer_coordinates"])
        assert len(old["Q_integer_coordinates"]) == FDEG
        answer = dict(old,
            U_integer_coordinates=[[int(x) for x in row] for row in old["U_integer_coordinates"]],
            Q_integer_coordinates=[int(x) for x in old["Q_integer_coordinates"]])
        self.operator_cache[power] = answer
        return answer

    def power_rows(self, power, count=None):
        """Yield only retained exact rows; this method does not form products."""
        count = ORDERS[power] if count is None else count
        assert 1 <= count <= ORDERS[power]
        if power == 5:
            for index in range(1234):
                self.budget()
                name = "R787-real-power5-row-" + str(index).zfill(4) + ".json.gz"
                data = self.r787.stage(name)
                assert data["index"] == index
                assert data["all_original_phase_involutions_verified"] is True
                values = data["integer_t_coefficients"]
                assert len(values) == 129 and all(len(row) == REAL for row in values)
                yield [[int(x) for x in row] for row in values[:count]]
        else:
            assert power == 6
            for index, row in enumerate(self.frontier6["basis_rows"]):
                self.budget()
                assert row["index"] == index
                values, cursor = [], 0
                segments = row["original_prefix_segments"] + row["new_tail_segments"]
                for entry in segments:
                    if cursor >= count:
                        break
                    assert entry["first"] == cursor and cursor < entry["stop"] <= 142
                    source = self.sources[entry["producer"]]
                    data = source.stage_spec(entry)
                    assert data["weight"] == 12
                    assert data["integer_scale"] == str(82**12)
                    part = data["integer_v_t_coefficients"]
                    assert len(part) == entry["stop"]-entry["first"]
                    assert all(len(v) == REAL for v in part)
                    if entry["producer"] == "R801":
                        assert data["node_key"] == row["node_key"]
                        assert data["node_fingerprint"] == row["node_fingerprint"]
                        assert data["first_exponent"] == cursor
                        assert data["last_exponent_exclusive"] == entry["stop"]
                    else:
                        assert data["recipe"] == row["original_recipe"]
                        assert data["index"] == index
                    length = min(count, entry["stop"]) - cursor
                    values.extend([[int(x) for x in v] for v in part[:length]])
                    cursor = entry["stop"]
                assert len(values) == count
                yield values

    def basis(self, power):
        if self.active_power != power:
            self.F = None
            gc.collect()
            columns = [[x for row in values for x in row]
                       for values in self.power_rows(power)]
            assert len(columns) == DIMENSION[power]
            self.F = fmpz_mat([list(row) for row in zip(*columns)])
            del columns
            self.active_power = power
        assert self.F.nrows() == ORDERS[power]*REAL
        assert self.F.ncols() == DIMENSION[power]
        return self.F

    def basis_mod_prefix(self, power, count, prime):
        columns = [[x % prime for row in values for x in row]
                   for values in self.power_rows(power, count)]
        return nmod_mat([list(row) for row in zip(*columns)], prime)

    @lru_cache(maxsize=12)
    def m2_mod(self, index, count, prime):
        assert index in (0, 1, 73) and count <= 96
        name = "R786-exact-power-1-row-" + str(index).zfill(4) + ".json.gz"
        source = self.sources["R786"]
        data = source.stage(name)
        assert data["weight"] == 2 and data["integer_scale"] == str(82**2)
        values = data["integer_qY_xi_coefficients"]
        assert len(values) == 129
        answer = []
        # New finite-prime consumer only; the retained integral prefix is unchanged.
        for n, old in enumerate(values[:count]):
            assert len(old) == 40
            cyclic = [0]*41
            for r, coefficient in enumerate(old):
                cyclic[(r+10*n) % 41] = int(coefficient) % prime
            reduced = [(x-cyclic[40]) % prime for x in cyclic[:40]] + [0]
            assert all(reduced[r] == reduced[41-r] for r in range(1, 21))
            real = nmod_poly([reduced[0]], prime)
            for r in range(1, 21):
                real += nmod_poly([int(x) for x in self.field.chebyshev[r].coeffs()],
                                  prime) * reduced[r]
            real %= nmod_poly([int(x) for x in self.field.gt.coeffs()], prime)
            answer.append([int(real[r]) for r in range(20)])
        return tuple(tuple(row) for row in answer)

    def source_selection(self):
        value = self.r787.stage("R787-prime-1000000753-selection.json.gz")
        assert value["prime"] == ORIGINAL_PRIME
        assert value["prime_proved"] is True
        assert value["all_14_L_branches_distinct"] is True
        assert value["all_rational_denominators_units"] is True
        assert value["all_kappa_reductions_invertible"] is True
        return value

    def selection(self, prime):
        if prime == ORIGINAL_PRIME:
            return self.source_selection()
        name = "R824-prime-" + str(prime) + "-selection"
        old = self.cache(name)
        if old is not None:
            return old
        assert bool(fmpz(prime).is_prime()) and 3 < prime < 2**31
        fB = nmod_poly([int(x) for x in self.field.fB.coeffs()], prime)
        if fB.gcd(fB.derivative()).degree() != 0:
            raise BadPrime("Original B_fld polynomial is inseparable at this prime.")
        roots_B = [(int(v), int(m)) for v, m in fB.roots()]
        roots_s = [(int(v), int(m)) for v, m in nmod_poly([3, 0, 1], prime).roots()]
        if len(roots_B) != 7 or len(roots_s) != 2:
            raise BadPrime("This new prime does not give the requested fourteen faithful split branches.")
        assert all(int(mult) == 1 for _, mult in roots_B + roots_s)
        pairs = [[int(b), int(s)] for s, _ in sorted(roots_s)
                 for b, _ in sorted(roots_B)]
        evaluations = [[pow(b, i, prime)*pow(s, j, prime) % prime
                        for j in range(2) for i in range(7)] for b, s in pairs]
        V = nmod_mat(evaluations, prime)
        inverse = V.inv()
        assert V*inverse == nmod_mat([[int(i == j) for j in range(14)]
                                     for i in range(14)], prime)
        self.store(name, {"prime": prime, "prime_proved": True, "roots_B_s": pairs,
            "evaluation_matrix": evaluations, "inverse_evaluation_matrix": imatrix(inverse),
            "all_14_L_branches_distinct": True,
            "original_B_polynomial_all_seven_simple_roots_verified": True,
            "original_s_polynomial_both_roots_verified": True})
        return self.cache(name)

    def common_inverse_and_y(self, power, selection, branch):
        prime, weights = selection["prime"], selection["evaluation_matrix"][branch]
        operator = self.operator(power)
        if int(operator["common_positive_denominator"]) % prime == 0:
            raise BadPrime("The common original rational denominator is not a unit.")
        gt = nmod_poly([int(x) for x in self.field.gt.coeffs()], prime)
        def evaluate(vector):
            return nmod_poly([sum(int(weights[i])*int(vector[20*i+r])
                                  for i in range(14)) % prime for r in range(20)], prime)
        Q = evaluate(operator["Q_integer_coordinates"])
        gcd, inv, _ = Q.xgcd(gt)
        if gcd.degree() != 0:
            raise BadPrime("The original common clear multiplier is not a unit at this branch.")
        inv = (inv * pow(int(gcd[0]), -1, prime)) % gt
        assert (Q*inv) % gt == nmod_poly([1], prime)
        Y = []
        for vector in operator["U_integer_coordinates"]:
            value = (-evaluate(vector)*inv) % gt
            Y.append([int(value[r]) for r in range(20)])
        return [int(inv[r]) for r in range(20)], Y

    def old_chart(self):
        value = self.r787.stage("R787-prime-1000000753-chart.json.gz")
        assert value["actual_modular_rank"] == 1186
        assert value["chosen_free_column"] == RESERVED_FREE_COLUMN
        assert len(value["pivot_columns"]) == len(value["pivot_rows"]) == 1186
        return value

    def old_rational_blocks(self):
        value = self.r787.stage("R787-prime-1000000753-rational-blocks.json.gz")
        assert value["prime"] == ORIGINAL_PRIME
        assert value["A_minor_det_mod_prime"] == 336446771
        assert value["B_constant_minor_det_mod_prime"] == 322380492
        assert value["exact_E0_Z_zero_verified"] is True
        return value

    def constant_kernel6(self, prime):
        name = "R824-power6-exact-constant-kernel"
        old = self.cache(name)
        if old is not None:
            if int(old["Z_free_diagonal"]) % prime == 0:
                raise BadPrime("Retained sixfold constant-kernel denominator is not a unit.")
            return old
        F = self.basis(6)
        E = submatrix(F, range(20), prime=prime)
        P = pivots(E)
        if len(P) != 20:
            raise BadPrime("The original sixfold constant evaluation loses rank.")
        Q = [j for j in range(1506) if j not in set(P)]
        EP, EQ = submatrix(F, range(20), P), submatrix(F, range(20), Q)
        rational = fmpq_mat(EP).solve(fmpq_mat(EQ))
        numerator, denominator = rational.numer_denom()
        Zp = -numerator
        assert is_zero(EP*Zp + EQ*denominator)
        if int(denominator) % prime == 0:
            raise BadPrime("The newly selected constant-kernel denominator is not a unit.")
        self.store(name, {"B_constant_pivot_columns": P, "B_constant_free_columns": Q,
            "Z_pivot_integer_rows": smatrix(Zp), "Z_free_diagonal": str(denominator),
            "exact_E0_Z_zero_verified": True,
            "selecting_prime": prime,
            "actual_constant_minor_det_mod_prime": int(submatrix(EP, range(20), prime=prime).det())})
        return self.cache(name)

    def model(self, power, prime):
        if not hasattr(self, "models"):
            self.models = {}
        key = (power, prime)
        if key not in self.models:
            self.models[key] = ModularModel(self, power, self.selection(prime))
        return self.models[key]

    def scalar_series_product(self, left, right, count, prime):
        assert len(left) >= count and len(right) >= count
        aa, bb = [0]*(39*count), [0]*(39*count)
        for n in range(count):
            aa[39*n:39*n+20] = [int(x) % prime for x in left[n]]
            bb[39*n:39*n+20] = [int(x) % prime for x in right[n]]
        product = nmod_poly(aa, prime).mul_low(nmod_poly(bb, prime), 39*count)
        reduced = nmod_mat([[int(product[39*n+r]) for r in range(39)]
                            for n in range(count)], prime)*nmod_mat(imatrix(self.field.Tred), prime)
        return [[int(reduced[n, r]) for r in range(20)] for n in range(count)]

    def six_profile(self):
        final_name = "R824-power6-selected-generator-profile"
        old = self.cache(final_name)
        if old is not None:
            assert old["weight5_kernel_dimension"] == 28
            assert old["weight6_kernel_dimension"] == 300
            assert len(old["selected_weight6_free_columns"]) == 244
            return old
        search = self.cache("R824-sixfold-prime-search")
        prime = ORIGINAL_PRIME if search is None else int(search["next_prime"])
        while True:
            self.budget()
            try:
                selection = self.selection(prime)
                model5, model6 = self.model(5, prime), self.model(6, prime)
                model5.all_branches()
                model6.all_branches()
                name = "R824-power6-prime-"+str(prime)+"-supplement-chart"
                chart = self.cache(name)
                F5short = self.basis_mod_prefix(5, 82, prime)
                F6short = submatrix(model6.FA, range(1640), prime=prime)
                tau = self.m2_mod(0, 82, prime)
                sigma = [[(a+b) % prime for a, b in zip(first, second)]
                         for first, second in zip(self.m2_mod(1, 82, prime),
                                                  self.m2_mod(73, 82, prime))]
                records = []
                for branch in range(14):
                    self.budget()
                    stage_name = "R824-power6-prime-"+str(prime)+"-lower-span-branch-"+str(branch).zfill(2)
                    stage = self.cache(stage_name)
                    b5, b6 = model5.branch(branch), model6.branch(branch)
                    free6 = b6["kernel_free_columns"]
                    if stage is None:
                        B5 = nmod_mat(model5.expand_B(imatrix(b5["kernel_C_mod_prime"]), prime), prime)
                        jets5 = F5short*B5
                        columns = []
                        for multiplier in (tau, sigma):
                            for target in range(28):
                                values = [[int(jets5[20*n+r, target]) for r in range(20)]
                                          for n in range(82)]
                                product = self.scalar_series_product(multiplier, values, 82, prime)
                                columns.append([x for row in product for x in row])
                        jets6 = nmod_mat([list(row) for row in zip(*columns)], prime)
                        B6 = model6.Ainv*submatrix(jets6, self.I6, prime=prime)
                        assert F6short*B6 == jets6
                        invZ = pow(model6.Zd % prime, -1, prime)
                        C6 = nmod_mat([[int(B6[index, j])*invZ % prime for j in range(56)]
                                       for index in model6.Q], prime)
                        assert nmod_mat(model6.expand_B(imatrix(C6), prime), prime) == B6
                        U = submatrix(C6, free6, prime=prime)
                        assert b6["kernel_C_mod_prime"]*U == C6
                        if chart is None:
                            I = pivots(U.transpose())
                            if len(I) != 56:
                                raise BadPrime("The actual lower-degree span has deficient rank at this prime.")
                            self.store(name, {"prime": prime, "selected_lower_span_rows": I,
                                "weight6_free_columns": free6, "actual_lower_span_rank": 56})
                            chart = self.cache(name)
                        assert chart["weight6_free_columns"] == free6
                        square = submatrix(U, chart["selected_lower_span_rows"], prime=prime)
                        determinant = int(square.det())
                        if not determinant:
                            raise BadPrime("A common lower-span minor vanishes in another original branch.")
                        self.store(stage_name, {"prime": prime, "branch": branch,
                            "weight5_kernel_stage": spec(self.path(model5.base+"-branch-"+str(branch).zfill(2))),
                            "weight6_kernel_stage": spec(self.path(model6.base+"-branch-"+str(branch).zfill(2))),
                            "lower_span_in_weight6_free_coordinates": imatrix(U),
                            "common_row_indices": chart["selected_lower_span_rows"],
                            "actual_lower_span_rank": 56,
                            "actual_selected_minor_determinant_mod_prime": determinant,
                            "all_1640_original_product_coordinates_verified": True,
                            "all_B6_coordinates_in_saved_sixfold_kernel_verified": True,
                            "new_exact_weight5_prefix_or_weight6_basis_computed": False})
                        stage = self.cache(stage_name)
                    assert stage["common_row_indices"] == chart["selected_lower_span_rows"]
                    assert stage["actual_lower_span_rank"] == 56
                    assert stage["actual_selected_minor_determinant_mod_prime"] % prime
                    records.append(spec(self.path(stage_name)))
                selected_positions = [i for i in range(300)
                                      if i not in set(chart["selected_lower_span_rows"])]
                selected_columns = [chart["weight6_free_columns"][i] for i in selected_positions]
                assert len(selected_columns) == 244
                self.store(final_name, {"prime": prime,
                    "selection": (self.r787.file_spec("R787-prime-1000000753-selection.json.gz")
                                  if prime == ORIGINAL_PRIME else spec(self.path("R824-prime-"+str(prime)+"-selection"))),
                    "weight5_chart": spec(self.path(model5.chart_name)),
                    "weight6_chart": spec(self.path(model6.chart_name)),
                    "supplement_chart": spec(self.path(name)), "branch_lower_span_stages": records,
                    "weight5_kernel_dimension": 28, "weight6_kernel_dimension": 300,
                    "actual_lower_span_rank_in_each_branch": 56,
                    "selected_weight6_free_positions": selected_positions,
                    "selected_weight6_free_columns": selected_columns,
                    "exact_weight6_generators_claimed": False})
                return self.cache(final_name)
            except BadPrime as error:
                self.store("R824-sixfold-prime-"+str(prime)+"-rejected",
                           {"prime": prime, "reason": str(error),
                            "only_actual_modular_failure": True,
                            "characteristic_zero_rank_or_profile_changed": False})
                if hasattr(self, "models"):
                    self.models.pop((6, prime), None)
                    if prime != ORIGINAL_PRIME:
                        self.models.pop((5, prime), None)
                gc.collect()
                prime = next_prime(prime)
                self.store("R824-sixfold-prime-search", {"next_prime": prime})

    def target_configuration(self, model, free_column):
        branches = model.all_branches()
        assert all(free_column in branch["kernel_free_columns"] for branch in branches)
        assert not (model.power == 5 and free_column == RESERVED_FREE_COLUMN)
        common = {
            "ordinary_power": model.power, "free_column": free_column, "prime": model.prime,
            "chart": spec(self.path(model.chart_name)), "rational_block": model.block_spec,
            "branch_stages": [spec(self.path(model.base+"-branch-"+str(i).zfill(2)))
                              for i in range(14)],
            "common_clear_operator": spec(self.path(
                "R824-common-clear-operator-N"+str(model.N))),
            "normalization": "one common original L free coordinate is 1; all other free coordinates are 0",
            "original_R787_reserved_target_recomputed": False,
        }
        if model.power == 6:
            profile = self.six_profile()
            assert profile["prime"] == model.prime
            assert free_column in profile["selected_weight6_free_columns"]
            common["sixfold_supplement_profile"] = spec(self.path("R824-power6-selected-generator-profile"))
        return common

    def target_prefix(self, power, free_column):
        return "R824-power"+str(power)+"-free-"+str(free_column).zfill(4)

    def target_series(self, model, A, C, modulus=None):
        F = self.basis(model.power)
        B = model.expand_B(C, modulus)
        AA = F*fmpz_mat(A)
        BB = F*fmpz_mat(B)
        av, bv = [], []
        for n in range(model.N):
            aa = [int(AA[20*n+r, i]) for i in range(14) for r in range(20)]
            bb = [int(BB[20*n+r, i]) for i in range(14) for r in range(20)]
            if modulus is not None:
                aa, bb = [x % modulus for x in aa], [x % modulus for x in bb]
            av.append(aa)
            bv.append(bb)
        return av, bv

    def target_residual(self, model, A, C, modulus):
        self.budget()
        av, bv = self.target_series(model, A, C, modulus)
        return PackedField(self.field, modulus).residual(self.operator(model.power), av, bv)

    def initial_target(self, model, free_column, target):
        prefix = self.target_prefix(model.power, free_column)
        name = prefix+"-lift-"+str(1).zfill(8)
        old = self.cache(name)
        if old is not None:
            assert old["target_configuration"] == target
            return spec(self.path(name))
        aa, cc = [], []
        for branch in model.all_branches():
            j = branch["kernel_free_columns"].index(free_column)
            aa.append([int(branch["kernel_A_mod_prime"][i, j]) for i in range(model.n)])
            cc.append([int(branch["kernel_C_mod_prime"][i, j]) for i in range(model.d)])
        inverse = nmod_mat(model.selection["inverse_evaluation_matrix"], model.prime).transpose()
        A = nmod_mat([list(row) for row in zip(*aa)], model.prime)*inverse
        C = nmod_mat([list(row) for row in zip(*cc)], model.prime)*inverse
        av, cv = imatrix(A), imatrix(C)
        residual = self.target_residual(model, av, cv, model.prime)
        assert all(not x for row in residual for x in row)
        assert cv[free_column] == [1]+[0]*13
        self.store(name, {"target_configuration": target, "digits": 1,
            "prime": model.prime, "modulus": str(model.prime),
            "A_L_coordinates": [[str(x) for x in row] for row in av],
            "C_L_coordinates": [[str(x) for x in row] for row in cv],
            "previous_complete_lift": None,
            "full_original_modular_relations_verified": True})
        return spec(self.path(name))

    def advance_target_pointer(self, prefix, target, new_spec):
        pointer_name = prefix+"-current"
        current = self.cache(pointer_name)
        new = self.stored_spec(new_spec)
        assert new["target_configuration"] == target
        previous = new["previous_complete_lift"]
        if current is not None and current["lift"] == new_spec:
            pass
        else:
            if current is not None:
                assert current["target_configuration"] == target
                assert current["lift"] == previous
            else:
                assert previous is None
            receipt_name = prefix+"-history-"+str(new["digits"]).zfill(8)
            receipt = self.cache(receipt_name)
            evidence = {"target_configuration": target, "digits": new["digits"],
                "previous_complete_lift": previous, "new_complete_lift": new_spec,
                "large_historical_vectors_retained": False}
            if receipt is None:
                self.store(receipt_name, evidence)
            else:
                assert all(receipt[key] == value for key, value in evidence.items())
            self.store(pointer_name, {"target_configuration": target, "lift": new_spec,
                "history_receipt": spec(self.path(receipt_name))})
        if previous is not None:
            old_path = self.out/previous["file"]
            if old_path.exists():
                assert spec(old_path) == previous
                old_path.unlink()
        return new

    def correction(self, model, residual_divided):
        prime = model.prime
        gt = nmod_poly([int(x) for x in self.field.gt.coeffs()], prime)
        P, I = model.chart["pivot_columns"], model.chart["pivot_rows"]
        FARp = submatrix(model.FAR, I, prime=prime)
        delta_A, delta_C = [], []
        for index, branch in enumerate(model.all_branches()):
            self.budget()
            weights = model.selection["evaluation_matrix"][index]
            inverse_clear = nmod_poly(branch["common_clear_multiplier_inverse"], prime)
            rhs = []
            for m in range(1, model.N):
                vector = residual_divided[m]
                polynomial = nmod_poly([sum(int(weights[i])*int(vector[20*i+r])
                                            for i in range(14)) % prime
                                        for r in range(20)], prime)
                value = (-polynomial*inverse_clear) % gt
                rhs.extend([int(value[r]) for r in range(20)])
            rhsJ = nmod_mat([[rhs[i]] for i in model.J], prime)
            rhsR = nmod_mat([[rhs[model.AR[i]]] for i in I], prime)
            cp = branch["Schur_minor_inverse_mod_prime"]*(FARp*model.Ainv*rhsJ-rhsR)
            aa = model.Ainv*(rhsJ+branch["C_J_pivot_columns"]*cp)
            cc = [0]*model.d
            for i, column in enumerate(P):
                cc[column] = int(cp[i, 0])
            delta_A.append([int(aa[i, 0]) for i in range(model.n)])
            delta_C.append(cc)
        inverse = nmod_mat(model.selection["inverse_evaluation_matrix"], prime).transpose()
        A = nmod_mat([list(row) for row in zip(*delta_A)], prime)*inverse
        C = nmod_mat([list(row) for row in zip(*delta_C)], prime)*inverse
        return imatrix(A), imatrix(C)

    def try_exact(self, model, free_column, target, lift, lift_spec):
        prefix = self.target_prefix(model.power, free_column)
        final_name = prefix+"-exact-generator"
        old_final = self.cache(final_name)
        if old_final is not None:
            assert old_final["target_configuration"] == target
            return spec(self.path(final_name))
        modulus = int(lift["modulus"])
        denominator = 1
        matrices = []
        for key in ("A_L_coordinates", "C_L_coordinates"):
            rows = []
            for row in lift[key]:
                decoded = []
                for value in row:
                    entry = rational_reconstruct(int(value), modulus)
                    if entry is None:
                        return None
                    denominator = math.lcm(denominator, int(entry.denom()))
                    decoded.append(entry)
                rows.append(decoded)
            matrices.append(rows)
        A, C = [[[int(value.numer())*(denominator//int(value.denom())) for value in row]
                 for row in matrix] for matrix in matrices]
        B = model.expand_B(C)
        content = 0
        for row in A+B:
            for value in row:
                content = math.gcd(content, value)
        assert content > 0
        A = [[x//content for x in row] for row in A]
        B = [[x//content for x in row] for row in B]
        assert any(x for row in B for x in row)
        candidate = {
            "target_configuration": target, "ordinary_power": model.power,
            "original_basis_dimension": model.n, "basis_integer_scale": str(82**(2*model.power)),
            "field": self.field.description,
            "L_basis": "B_fld^i*s^j; j=0,1 outer; i=0..6; B_fld=lambda*b",
            "A_integer_L_coordinates": [[str(x) for x in row] for row in A],
            "B_integer_L_coordinates": [[str(x) for x in row] for row in B],
            "common_rational_denominator_cleared": str(denominator),
            "common_integer_content_removed": str(content),
            "reconstruction_modulus": str(modulus),
            "strict_reconstruction_bound": str(math.isqrt((modulus-1)//2)),
        }
        digest = fingerprint(candidate)
        base = prefix+"-candidate-"+digest
        if self.cache(base+"-rejected") is not None:
            return None
        if self.cache(base) is None:
            self.store(base, dict(candidate, candidate_only=True))
        residual_name = base+"-unreduced-verification-product"
        raw = self.cache(residual_name)
        if raw is None:
            F = self.basis(model.power)
            aa, bb = F*fmpz_mat(A), F*fmpz_mat(B)
            av = [[int(aa[20*n+r, i]) for i in range(14) for r in range(20)]
                  for n in range(model.N)]
            bv = [[int(bb[20*n+r, i]) for i in range(14) for r in range(20)]
                  for n in range(model.N)]
            total = PackedField(self.field).operator_product(self.operator(model.power), av, bv)
            self.store(residual_name, {"candidate_sha256": spec(self.path(base))["sha256"],
                "orders": model.N, "packed_q_stride": PACK,
                "integer_coefficients": [str(x) for x in total.coeffs()],
                "two_original_integer_operator_products_complete": True})
            raw = self.cache(residual_name)
        assert raw["candidate_sha256"] == spec(self.path(base))["sha256"]
        total = fmpz_poly([int(x) for x in raw["integer_coefficients"]])
        engine = PackedField(self.field)
        checks = []
        for first in range(0, model.N, 8):
            self.budget()
            stop = min(model.N, first+8)
            name = base+"-verified-orders-"+str(first).zfill(3)+"-"+str(stop).zfill(3)
            saved = self.cache(name)
            if saved is None:
                for m in range(first, stop):
                    value = engine.reduce_block(total, m)
                    if any(value):
                        self.store(base+"-rejected", {
                            "candidate_sha256": spec(self.path(base))["sha256"],
                            "first_nonzero_relation_order": m,
                            "unreduced_product": spec(self.path(residual_name)),
                            "candidate_not_an_exact_original_relation": True})
                        self.path(residual_name).unlink()
                        return None
                self.store(name, {"candidate_sha256": spec(self.path(base))["sha256"],
                    "unreduced_product_sha256": spec(self.path(residual_name))["sha256"],
                    "first_order": first, "stop_order": stop,
                    "all_original_280_Q_coordinates_zero_at_each_order": True})
                saved = self.cache(name)
            assert saved["candidate_sha256"] == spec(self.path(base))["sha256"]
            assert saved["first_order"] == first and saved["stop_order"] == stop
            assert saved["all_original_280_Q_coordinates_zero_at_each_order"] is True
            checks.append(spec(self.path(name)))
        original_basis = (self.sources["R786"].certificate["basis_index"] if model.power == 5
                          else self.frontier6_spec)
        self.store(final_name, dict(candidate, candidate_only=False,
            original_basis_index=plain_spec(original_basis),
            full_original_relation_orders=model.N, full_original_t_coordinates=20,
            full_original_Q_coordinates_per_order=280,
            exact_original_A_equals_yB=True, B_nonzero=True,
            full_relation_verification_stages=checks,
            common_clear_operator=spec(self.path("R824-common-clear-operator-N"+str(model.N))),
            candidate_stage=spec(self.path(base)),
            unreduced_product_digest_only=spec(self.path(residual_name)),
            final_lift_digest_only=lift_spec,
            actual_Dixon_digits=lift["digits"],
            full_polar_module_or_height_claimed=False))
        self.path(residual_name).unlink()
        return spec(self.path(final_name))

    def finish_target_cleanup(self, prefix, target, exact_spec):
        exact = self.stored_spec(exact_spec)
        assert exact["target_configuration"] == target
        assert exact["exact_original_A_equals_yB"] is True
        name = prefix+"-completed-lift-retention"
        old = self.cache(name)
        if old is None:
            files = [spec(path) for path in sorted(self.out.glob(prefix+"-lift-*.json.gz"))]
            self.store(name, {"target_configuration": target,
                "exact_generator": exact_spec, "historical_complete_lifts": files,
                "large_lifts_retained_after_exact_generator": False})
            old = self.cache(name)
        assert old["exact_generator"] == exact_spec
        for entry in old["historical_complete_lifts"]:
            path = self.out/entry["file"]
            if path.exists():
                assert spec(path) == entry
                path.unlink()
        pointer = self.path(prefix+"-current")
        if pointer.exists():
            current = self.cache(prefix+"-current")
            assert current["target_configuration"] == target
            pointer.unlink()
        residual = exact["unreduced_product_digest_only"]
        path = self.out/residual["file"]
        if path.exists():
            assert spec(path) == residual
            path.unlink()

    def lift_target(self, model, free_column):
        self.operator(model.power)
        target = self.target_configuration(model, free_column)
        prefix = self.target_prefix(model.power, free_column)
        final_name = prefix+"-exact-generator"
        final = self.cache(final_name)
        if final is not None:
            assert final["target_configuration"] == target
            result = spec(self.path(final_name))
            self.finish_target_cleanup(prefix, target, result)
            return result
        pointer = self.cache(prefix+"-current")
        if pointer is None:
            first = self.initial_target(model, free_column, target)
            current = self.advance_target_pointer(prefix, target, first)
            current_spec = first
        else:
            assert pointer["target_configuration"] == target
            current_spec = pointer["lift"]
            current = self.advance_target_pointer(prefix, target, current_spec)
        interval = int(self.item.get("reconstruct_every_digits", 8))
        assert interval >= 1
        while True:
            self.budget()
            digits, modulus = int(current["digits"]), int(current["modulus"])
            assert modulus == model.prime**digits
            if digits % interval == 0:
                result = self.try_exact(model, free_column, target, current, current_spec)
                if result is not None:
                    self.finish_target_cleanup(prefix, target, result)
                    return result
            name = prefix+"-lift-"+str(digits+1).zfill(8)
            next_state = self.cache(name)
            if next_state is None:
                A = [[int(x) for x in row] for row in current["A_L_coordinates"]]
                C = [[int(x) for x in row] for row in current["C_L_coordinates"]]
                residual = self.target_residual(model, A, C, modulus*model.prime)
                assert all(x % modulus == 0 for row in residual for x in row)
                divided = [[x//modulus for x in row] for row in residual]
                dA, dC = self.correction(model, divided)
                corrected = self.target_residual(model, dA, dC, model.prime)
                assert all((a+b) % model.prime == 0
                           for old, new in zip(divided, corrected) for a, b in zip(old, new))
                next_A = [[a+modulus*d for a, d in zip(row, delta)]
                          for row, delta in zip(A, dA)]
                next_C = [[a+modulus*d for a, d in zip(row, delta)]
                          for row, delta in zip(C, dC)]
                assert next_C[free_column] == [1]+[0]*13
                self.store(name, {"target_configuration": target, "prime": model.prime,
                    "digits": digits+1, "modulus": str(modulus*model.prime),
                    "A_L_coordinates": [[str(x) for x in row] for row in next_A],
                    "C_L_coordinates": [[str(x) for x in row] for row in next_C],
                    "previous_complete_lift": current_spec,
                    "full_original_modular_relations_verified": True,
                    "all_old_residual_coordinates_divisible": True,
                    "all_new_correction_coordinates_cancel": True})
                next_state = self.cache(name)
            assert next_state["target_configuration"] == target
            assert next_state["previous_complete_lift"] == current_spec
            next_spec = spec(self.path(name))
            current = self.advance_target_pointer(prefix, target, next_spec)
            current_spec = next_spec

    def reserved_recipe(self):
        identity = self.item["retained_sources"].get("R787_complete")
        if identity is None:
            return None
        producer = Source(self.args.retained, "R787_complete", identity)
        assert producer.tag == self.r787.tag
        cert = producer.certificate
        assert cert["complete"] is True
        assert cert["exact_nonzero_A_B_relation_verified"] is True
        assert cert["original_full_L_retained"] is True
        assert cert["exact_verified_orders"] == 129
        assert cert["exact_verified_t_coordinates"] == 20
        assert cert["exact_verified_Q_coordinates_per_order"] == 280
        entry = cert["relation_spec"]
        data = producer.stage_spec(entry)
        assert data["exact_original_A_equals_yB"] is True
        assert data["full_129_original_relations_verified"] is True
        assert data["B_nonzero"] is True
        assert data["field"] == self.field.description
        assert data["basis_integer_scale"] == str(82**10)
        assert len(data["A_integer_L_coordinates"]) == 1234
        assert len(data["B_integer_L_coordinates"]) == 1234
        assert all(len(row) == 14 for key in ("A_integer_L_coordinates", "B_integer_L_coordinates")
                   for row in data[key])
        assert cert["actual_auxiliary_prime"] == ORIGINAL_PRIME
        assert cert["actual_modular_Schur_rank"] == 1186
        assert data["R786_basis_index"] == self.sources["R786"].certificate["basis_index"]
        return {"source": dict(plain_spec(entry), producer="R787_complete"),
                "source_identity": producer.stable_identity, "data": data,
                "ordinary_power": 5, "free_column": RESERVED_FREE_COLUMN}

    def complete_generators(self):
        records = []
        free5 = [j for j in range(1214) if j not in set(self.old_chart()["pivot_columns"])]
        reserved = self.reserved_recipe()
        if reserved is not None:
            records.append(reserved)
        for column in free5:
            if column == RESERVED_FREE_COLUMN:
                continue
            name = self.target_prefix(5, column)+"-exact-generator"
            data = self.cache(name)
            if data is not None:
                assert data["exact_original_A_equals_yB"] is True
                records.append({"source": spec(self.path(name)), "data": data,
                                "ordinary_power": 5, "free_column": column})
        profile = self.cache("R824-power6-selected-generator-profile")
        if profile is not None:
            for column in profile["selected_weight6_free_columns"]:
                name = self.target_prefix(6, column)+"-exact-generator"
                data = self.cache(name)
                if data is not None:
                    assert data["exact_original_A_equals_yB"] is True
                    records.append({"source": spec(self.path(name)), "data": data,
                                    "ordinary_power": 6, "free_column": column})
        return sorted(records, key=lambda row: (row["ordinary_power"], row["free_column"]))

    @lru_cache(maxsize=16)
    def small_original_real_mod(self, power, index, count, prime):
        assert (power == 1 and index in (0, 1, 73)) or (power == 2 and index == 0)
        assert count <= 96
        name = "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"
        data = self.sources["R786"].stage(name)
        assert data["weight"] == 2*power and data["integer_scale"] == str(82**(2*power))
        if power == 2:
            assert data["recipe"] == {"kind": "product", "left_power": 1,
                "left_index": 0, "right_power": 1, "right_index": 0}
        values = data["integer_qY_xi_coefficients"]
        assert len(values) == 129
        gt = nmod_poly([int(x) for x in self.field.gt.coeffs()], prime)
        answer = []
        for n, original in enumerate(values[:count]):
            cyclic = [0]*41
            for r, coefficient in enumerate(original):
                cyclic[(r+10*n) % 41] = int(coefficient) % prime
            reduced = [(x-cyclic[40]) % prime for x in cyclic[:40]]+[0]
            assert all(reduced[r] == reduced[41-r] for r in range(1, 21))
            polynomial = nmod_poly([reduced[0]], prime)
            for r in range(1, 21):
                polynomial += nmod_poly([int(x) for x in self.field.chebyshev[r].coeffs()],
                                         prime)*reduced[r]
            polynomial %= gt
            answer.append([int(polynomial[r]) for r in range(20)])
        return tuple(tuple(row) for row in answer)

    def six_recipe_key(self, index):
        recipe = self.frontier6["basis_rows"][index]["original_recipe"]
        assert recipe["kind"] == "product"
        if recipe["left_power"] == 1 and recipe["right_power"] == 5:
            anchor, lower = recipe["left_index"], recipe["right_index"]
        else:
            assert recipe["left_power"] == 5 and recipe["right_power"] == 1
            anchor, lower = recipe["right_index"], recipe["left_index"]
        assert anchor in (0, 1, 73) and 0 <= lower < 1234
        return anchor, lower

    def fiber_products(self, prime):
        aliases = {}
        for entry in self.index7["basis_rows"]:
            recipe = entry["recipe"]
            assert recipe["kind"] == "product" and recipe["left_power"] == 1
            assert recipe["right_power"] == 6
            anchor, lower = self.six_recipe_key(recipe["right_index"])
            key = tuple(sorted((recipe["left_index"], anchor)))+(lower,)
            if key in aliases:
                assert aliases[key]["file"] == entry["file"]
            aliases[key] = entry
        source799 = self.sources["R799"]
        self.F, self.active_power = None, None
        gc.collect()
        rows6 = list(self.power_rows(6, 96))
        matrices, all_sources = {}, []
        for anchor in (0, 1, 73):
            columns = []
            multiplier = self.m2_mod(anchor, 96, prime)
            for first in range(0, 1506, 16):
                stop = min(first+16, 1506)
                name = "R824-fiber-prime-"+str(prime)+"-anchor-"+str(anchor).zfill(3)+"-block-"+str(first).zfill(4)
                old = self.cache(name)
                if old is None:
                    data_columns, inputs, new_indices = [], [], []
                    for index in range(first, stop):
                        other, lower = self.six_recipe_key(index)
                        key = tuple(sorted((anchor, other)))+(lower,)
                        entry = aliases.get(key)
                        if entry is not None:
                            source = source799.stage_spec(entry)
                            assert source["ordinary_power"] == 7 and source["bound_qY"] == 95
                            assert source["integer_scale"] == str(82**14)
                            values = [[int(x) % prime for x in row]
                                      for row in source["integer_v_t_coefficients"]]
                            inputs.append(dict(plain_spec(entry), producer="R799", target_index=index))
                        else:
                            values = self.scalar_series_product(multiplier, rows6[index], 96, prime)
                            new_indices.append(index)
                        flat = [x for row in values for x in row]
                        assert len(flat) == 1920
                        data_columns.append([flat[i] for i in self.I7])
                    self.store(name, {"prime": prime, "anchor": anchor, "first_index": first,
                        "stop_index": stop, "selected_coordinate_columns": data_columns,
                        "original_V7_coordinate_rows": self.I7,
                        "reused_original_exact_products": inputs,
                        "new_finite_product_indices": new_indices,
                        "original_integer_scale": str(82**14),
                        "original_exact_prefix_recomputed": False})
                    old = self.cache(name)
                assert old["original_V7_coordinate_rows"] == self.I7
                assert old["first_index"] == first and old["stop_index"] == stop
                columns.extend(old["selected_coordinate_columns"])
                all_sources.append(spec(self.path(name)))
            matrices[anchor] = nmod_mat([list(row) for row in zip(*columns)], prime)
            del columns
        tau2 = self.small_original_real_mod(2, 0, 96, prime)
        columns = []
        raw5 = iter(self.power_rows(5, 96))
        for first in range(0, 1234, 16):
            stop = min(first+16, 1234)
            values5 = [next(raw5) for _ in range(first, stop)]
            name = "R824-fiber-prime-"+str(prime)+"-tau2-weight5-block-"+str(first).zfill(4)
            old = self.cache(name)
            if old is None:
                data_columns, inputs, new_indices = [], [], []
                for offset, index in enumerate(range(first, stop)):
                    entry = aliases.get((0, 0, index))
                    if entry is not None:
                        source = source799.stage_spec(entry)
                        assert source["integer_scale"] == str(82**14)
                        values = [[int(x) % prime for x in row]
                                  for row in source["integer_v_t_coefficients"]]
                        inputs.append(dict(plain_spec(entry), producer="R799", target_index=index))
                    else:
                        values = self.scalar_series_product(tau2, values5[offset], 96, prime)
                        new_indices.append(index)
                    flat = [x for row in values for x in row]
                    assert len(flat) == 1920
                    data_columns.append([flat[i] for i in self.I7])
                self.store(name, {"prime": prime, "first_index": first, "stop_index": stop,
                    "selected_coordinate_columns": data_columns,
                    "original_V7_coordinate_rows": self.I7,
                    "reused_original_exact_products": inputs, "new_finite_product_indices": new_indices,
                    "original_integer_scale": str(82**14), "original_exact_prefix_recomputed": False})
                old = self.cache(name)
            assert old["original_V7_coordinate_rows"] == self.I7
            columns.extend(old["selected_coordinate_columns"])
            all_sources.append(spec(self.path(name)))
        matrices["tau2_weight5"] = nmod_mat([list(row) for row in zip(*columns)], prime)
        return matrices, all_sources

    def original_seventh_minor_at_prime(self, prime):
        name = "R824-fiber-prime-"+str(prime)+"-original-V7-minor"
        old = self.cache(name)
        if old is not None:
            return int(old["actual_determinant_mod_prime"])
        columns = []
        for entry in self.index7["basis_rows"]:
            self.budget()
            data = self.sources["R799"].stage_spec(entry)
            flat = [int(x) % prime for row in data["integer_v_t_coefficients"] for x in row]
            assert len(flat) == 1920
            columns.append([flat[i] for i in self.I7])
        matrix = nmod_mat([list(row) for row in zip(*columns)], prime)
        determinant = int(matrix.det())
        self.store(name, {"prime": prime, "original_basis_index": plain_spec(self.index7_spec),
            "original_coordinate_rows": self.I7, "actual_determinant_mod_prime": determinant,
            "only_new_prime_unit_check": True, "original_basis_reselected": False})
        return determinant

    def fiber_certificate(self, records):
        name = "R824-complete-global-polar-generator-fiber-certificate"
        old = self.cache(name)
        references = [{"ordinary_power": row["ordinary_power"], "free_column": row["free_column"],
                       "source": row["source"]} for row in records]
        assert sum(row["ordinary_power"] == 5 for row in records) == 28
        assert sum(row["ordinary_power"] == 6 for row in records) == 244
        assert len(records) == 272
        if old is not None:
            assert old["exact_generator_sources"] == references
            assert old["actual_nonzero_determinant_mod_prime"]
            return spec(self.path(name))
        search = self.cache("R824-fiber-search")
        prime = self.six_profile()["prime"] if search is None else int(search["next_prime"])
        attempt = 0 if search is None else int(search["prime_attempt_index"])
        while True:
            self.budget()
            try:
                selection = self.selection(prime)
                if not self.original_seventh_minor_at_prime(prime):
                    raise BadPrime("This prime annihilates the fixed original V7 coordinate minor.")
                matrices, product_sources = self.fiber_products(prime)
                weights = selection["evaluation_matrix"][0]
                by_weight = {power: [row for row in records if row["ordinary_power"] == power]
                             for power in (5, 6)}
                coefficients = {}
                for power in (5, 6):
                    rows = []
                    for index in range(DIMENSION[power]):
                        rows.append([sum(int(value)*int(weight) for value, weight in
                                         zip(target["data"]["B_integer_L_coordinates"][index], weights)) % prime
                                     for target in by_weight[power]])
                    coefficients[power] = nmod_mat(rows, prime)
                target5 = matrices["tau2_weight5"]*coefficients[5]
                target6 = matrices[0]*coefficients[6]
                right = [[int(target5[i, j]) for j in range(28)] +
                         [int(target6[i, j]) for j in range(244)] for i in range(1778)]
                # Increasing ranges give a fair search in both primes and integer fibers.
                stop_z = min(1207, 8+attempt)
                for z0 in range(stop_z):
                    self.budget()
                    trial_name = "R824-fiber-prime-"+str(prime)+"-z-"+str(z0).zfill(4)
                    trial = self.cache(trial_name)
                    if trial is None:
                        left = matrices[1]+matrices[73]-matrices[0]*z0
                        square = nmod_mat([[int(left[i, j]) for j in range(1506)]+right[i]
                                           for i in range(1778)], prime)
                        determinant = int(square.det())
                        self.store(trial_name, {"prime": prime, "z0": z0, "original_branch": 0,
                            "roots_B_s": selection["roots_B_s"][0],
                            "actual_determinant_mod_prime": determinant,
                            "rows": 1778, "columns": 1778,
                            "ordinary_power": 7, "integer_scale": str(82**14),
                            "original_V7_coordinate_rows": self.I7,
                            "exact_generator_sources": references,
                            "source_product_blocks": product_sources,
                            "actual_fiber_rank_1778": bool(determinant)})
                        trial = self.cache(trial_name)
                    assert trial["exact_generator_sources"] == references
                    determinant = int(trial["actual_determinant_mod_prime"])
                    if determinant:
                        self.store(name, {"prime": prime, "z0": z0, "original_branch": 0,
                            "roots_B_s": selection["roots_B_s"][0],
                            "actual_nonzero_determinant_mod_prime": determinant,
                            "actual_square_matrix_size": 1778,
                            "original_V6_columns": 1506, "actual_polar_generator_columns": 272,
                            "generator_weight_counts": {"5": 28, "6": 244, "7": 0},
                            "source_degree_sum": 1604, "ambient_epsilon_degree_sum": 398,
                            "actual_global_colength_from_homogeneous_certificate": 1206,
                            "exact_generator_sources": references, "actual_fiber_minor_stage": spec(self.path(trial_name)),
                            "all_original_A_equals_yB_relations_previously_certified": True,
                            "complete_polar_module_certified_by_R824_and_R822": True,
                            "normal_polynomial_matrices_computed": False,
                            "radical_Jacobian_eta_or_height_computed": False})
                        return spec(self.path(name))
                self.store("R824-fiber-prime-"+str(prime)+"-tested-fibers",
                           {"prime": prime, "tested_z0_interval": [0, stop_z],
                            "all_tested_determinants_zero": True,
                            "characteristic_zero_failure_claimed": False})
            except BadPrime as error:
                self.store("R824-fiber-prime-"+str(prime)+"-rejected",
                           {"prime": prime, "reason": str(error),
                            "characteristic_zero_failure_claimed": False})
            prime = next_prime(prime)
            attempt += 1
            self.store("R824-fiber-search", {"next_prime": prime, "prime_attempt_index": attempt})

    def run(self):
        requested = list(self.item["requested_scopes"])
        allowed = {"common_operators", "modular_generator_profile",
                   "weight5_generators", "weight6_generators", "global_fiber_certificate"}
        assert requested and len(requested) == len(set(requested)) and set(requested) <= allowed
        if "common_operators" in requested:
            self.operator(5)
            self.operator(6)
        model5 = None
        if set(requested) & {"modular_generator_profile", "weight5_generators"}:
            self.operator(5)
            model5 = self.model(5, ORIGINAL_PRIME)
            model5.all_branches()
        profile = None
        if set(requested) & {"modular_generator_profile", "weight6_generators", "global_fiber_certificate"}:
            self.operator(6)
            profile = self.six_profile()
        completed_request = []
        if "weight5_generators" in requested:
            free = model5.branch(0)["kernel_free_columns"]
            wanted = self.item.get("weight5_free_columns", "all_new")
            if wanted == "all_new":
                wanted = [column for column in free if column != RESERVED_FREE_COLUMN]
            assert isinstance(wanted, list) and len(wanted) == len(set(wanted))
            assert all(column in free and column != RESERVED_FREE_COLUMN for column in wanted)
            for column in wanted:
                self.lift_target(model5, int(column))
                completed_request.append({"ordinary_power": 5, "free_column": int(column)})
        if "weight6_generators" in requested:
            model6 = self.model(6, profile["prime"])
            wanted = self.item.get("weight6_free_columns", "all_selected")
            if wanted == "all_selected":
                wanted = profile["selected_weight6_free_columns"]
            assert isinstance(wanted, list) and len(wanted) == len(set(wanted))
            assert all(column in profile["selected_weight6_free_columns"] for column in wanted)
            for column in wanted:
                self.lift_target(model6, int(column))
                completed_request.append({"ordinary_power": 6, "free_column": int(column)})
        records = self.complete_generators()
        count5 = sum(row["ordinary_power"] == 5 for row in records)
        count6 = sum(row["ordinary_power"] == 6 for row in records)
        all_generators = count5 == 28 and count6 == 244
        fiber = None
        if "global_fiber_certificate" in requested or (all_generators and
                self.cache("R824-complete-global-polar-generator-fiber-certificate") is not None):
            if not all_generators:
                raise BudgetStop("Requested full fiber certificate awaits remaining exact generators, including the original R787 reserved target.")
            fiber = self.fiber_certificate(records)
        index = self.store("R824-completed-global-generator-index", {
            "exact_generators": [{"ordinary_power": row["ordinary_power"],
                "free_column": row["free_column"], "source": row["source"]}
                for row in records],
            "exact_weight5_generators": count5, "exact_weight6_generators": count6,
            "exact_weight7_generators": 0, "all_272_generators_exact": all_generators,
            "original_R787_reserved_generator_present": any(
                row["source"].get("producer") == "R787_complete" for row in records),
            "complete_polar_module_certified": fiber is not None,
            "fiber_certificate": fiber})
        inventory = self.store("R824-stage-manifest", {
            "files": [spec(path) for path in sorted(self.out.glob("R824-*.json.gz"))
                      if path.name != "R824-stage-manifest.json.gz"],
            "discarded_large_lift_and_verification_products_represented_by_small_digest_history": True})
        cert = {"result": RESULT, "configuration": self.tag, "complete": True,
            "p": 41, "completed_requested_scopes": requested,
            "completed_requested_generators": completed_request,
            "generator_index": index, "stage_manifest": inventory,
            "exact_weight5_generators": count5, "exact_weight6_generators": count6,
            "exact_weight7_generators": 0, "global_generator_count": len(records),
            "all_272_generators_exact": all_generators,
            "actual_complete_polar_module_certified": fiber is not None,
            "fiber_certificate": fiber,
            "actual_polar_module_colength": 1206 if fiber is not None else None,
            "weighted_source_degree": 1604 if fiber is not None else None,
            "ambient_epsilon_degree": 398,
            "normal_polynomial_ideal_matrices_computed": False,
            "radical_or_Jacobian_eta_or_height_computed": False,
            "original_R787_reserved_target_recomputed": False,
            "new_weight7_or_Laurent_tail_computed": False,
            "seconds": time.monotonic()-self.started}
        save(self.out/FINAL, cert)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(self.out/FINAL),
            "completed_requested_scopes": requested,
            "actual_complete_polar_module_certified": fiber is not None})
        return 0


class ModularModel:
    """One power and one real split prime; every branch uses a common chart."""

    def __init__(self, job, power, selection):
        self.job, self.power, self.selection = job, power, selection
        self.prime, self.N, self.n = selection["prime"], ORDERS[power], DIMENSION[power]
        self.d, self.k = self.n-20, KERNEL_DIMENSION[power]
        self.base = "R824-power"+str(power)+"-prime-"+str(self.prime)
        self._branches = {}
        source_block = job.old_rational_blocks() if power == 5 else job.constant_kernel6(self.prime)
        self.P = list(source_block["B_constant_pivot_columns"])
        self.Q = list(source_block["B_constant_free_columns"])
        self.Zp = fmpz_mat([[int(x) for x in row] for row in source_block["Z_pivot_integer_rows"]])
        self.Zd = int(source_block["Z_free_diagonal"])
        if self.Zd % self.prime == 0:
            raise BadPrime("The exact constant-kernel scale is not a unit.")
        assert len(self.P) == 20 and len(self.Q) == self.d
        F = job.basis(power)
        if power == 5:
            self.J = list(source_block["A_pivot_rows"])
        else:
            self.J = list(job.I6)
        self.AR = [i for i in range((self.N-1)*20) if i not in set(self.J)]
        assert len(self.J) == self.n
        assert len(self.AR) == {5: 1326, 6: 1314}[power]
        name = self.base+"-rational-blocks"
        block = job.cache(name)
        if power == 5 and self.prime == ORIGINAL_PRIME:
            block = source_block
            self.block_spec = job.r787.file_spec("R787-prime-1000000753-rational-blocks.json.gz")
        elif block is None:
            square = submatrix(F, self.J, prime=self.prime)
            try:
                inverse = square.inv()
            except ZeroDivisionError as error:
                raise BadPrime("The fixed original numerator minor is not a unit.") from error
            assert square*inverse == nmod_mat([[int(i == j) for j in range(self.n)]
                                               for i in range(self.n)], self.prime)
            job.store(name, {"prime": self.prime, "ordinary_power": power,
                "A_pivot_rows": self.J, "A_remaining_rows": self.AR,
                "A_inverse_mod_prime": imatrix(inverse),
                "A_minor_det_mod_prime": int(square.det()),
                "exact_constant_kernel_source": (
                    job.r787.file_spec("R787-prime-1000000753-rational-blocks.json.gz")
                    if power == 5 else spec(job.path("R824-power6-exact-constant-kernel"))),
                "B_constant_pivot_columns": self.P, "B_constant_free_columns": self.Q,
                "Z_pivot_integer_rows": smatrix(self.Zp), "Z_free_diagonal": str(self.Zd),
                "fixed_original_numerator_rows_reused": True})
            block = job.cache(name)
        if not (power == 5 and self.prime == ORIGINAL_PRIME):
            self.block_spec = spec(job.path(name))
        assert block["A_pivot_rows"] == self.J and block["A_remaining_rows"] == self.AR
        self.Ainv = nmod_mat(block["A_inverse_mod_prime"], self.prime)
        self.FA = submatrix(F, range((self.N-1)*20), prime=self.prime)
        self.FAR = submatrix(self.FA, self.AR, prime=self.prime)
        self.G = submatrix(F, range(self.N*20), self.Q, prime=self.prime)*(self.Zd % self.prime)
        self.G += submatrix(F, range(self.N*20), self.P, prime=self.prime)* \
                  submatrix(self.Zp, range(20), prime=self.prime)
        assert is_zero(submatrix(self.G, range(20), prime=self.prime))
        self.chart_name = self.base+"-chart"
        self.chart = job.cache(self.chart_name)
        if power == 5:
            old_chart = job.old_chart()
            expected = {key: old_chart[key] for key in ("pivot_rows", "pivot_columns")}
            if self.chart is None:
                job.store(self.chart_name, dict(expected, prime=self.prime, ordinary_power=5,
                    actual_rank=1186, kernel_dimension=28,
                    chart_choice_from_original_R787=True,
                    original_chart=job.r787.file_spec("R787-prime-1000000753-chart.json.gz"),
                    all_branches_certified_here=False))
                self.chart = job.cache(self.chart_name)
            assert all(self.chart[key] == value for key, value in expected.items())
        self.reducer = nmod_mat(imatrix(job.field.Tred), self.prime)

    def clear_inverse_y(self, branch):
        return self.job.common_inverse_and_y(self.power, self.selection, branch)

    def product_columns(self, Y, columns, suffix):
        """Return y times these actual B columns; n=0 vanishes by construction."""
        prime, count = self.prime, self.N
        polynomial = [0]*(39*count)
        for n, values in enumerate(Y):
            polynomial[39*n:39*n+20] = values
        polynomial = nmod_poly(polynomial, prime)
        completed = []
        for start in range(0, len(columns), 16):
            self.job.budget()
            chosen = list(columns[start:start+16])
            name = self.base+"-"+suffix+"-columns-"+str(start).zfill(4)
            old = self.job.cache(name)
            if old is None:
                block = []
                for column in chosen:
                    packed = [0]*(39*count)
                    for n in range(count):
                        packed[39*n:39*n+20] = [int(self.G[20*n+r, column])
                                                for r in range(20)]
                    product = polynomial.mul_low(nmod_poly(packed, prime), 39*count)
                    reduced = nmod_mat([[int(product[39*n+r]) for r in range(39)]
                                        for n in range(count)], prime)*self.reducer
                    assert all(not reduced[0, r] for r in range(20))
                    block.append([int(reduced[n, r]) for n in range(1, count)
                                  for r in range(20)])
                self.job.store(name, {"ordinary_power": self.power, "prime": prime,
                    "source_column_indices": chosen, "columns": block,
                    "source_rational_block": self.block_spec,
                    "new_right_hand_sides_only": suffix.startswith("reused")})
                old = self.job.cache(name)
            assert old["source_column_indices"] == chosen
            assert old["source_rational_block"] == self.block_spec
            completed.extend(old["columns"])
        return nmod_mat([list(row) for row in zip(*completed)], prime)

    def verify_vectors(self, Y, A, C, positions=None):
        """All retained original rows, without recreating a discarded full C matrix."""
        if positions is None:
            positions = range(C.ncols())
        positions = list(positions)
        AA = self.FA*submatrix(A, range(self.n), positions, prime=self.prime)
        BB = self.G*submatrix(C, range(self.d), positions, prime=self.prime)
        raw_y = [0]*(39*self.N)
        for n, row in enumerate(Y):
            raw_y[39*n:39*n+20] = row
        yy = nmod_poly(raw_y, self.prime)
        for j in range(len(positions)):
            self.job.budget()
            raw = [0]*(39*self.N)
            for n in range(self.N):
                raw[39*n:39*n+20] = [int(BB[20*n+r, j]) for r in range(20)]
            product = yy.mul_low(nmod_poly(raw, self.prime), 39*self.N)
            reduced = nmod_mat([[int(product[39*n+r]) for r in range(39)]
                                for n in range(self.N)], self.prime)*self.reducer
            assert all(not reduced[0, r] for r in range(20))
            assert all(int(reduced[n, r]) == int(AA[20*(n-1)+r, j])
                       for n in range(1, self.N) for r in range(20))

    def prune_product_blocks(self, branch, branch_spec):
        name = self.base+"-branch-"+str(branch).zfill(2)+"-product-retention"
        receipt = self.job.cache(name)
        if receipt is None:
            suffix = ("reused-branch-" if self.power == 5 and self.prime == ORIGINAL_PRIME
                      else "new-branch-")+str(branch).zfill(2)+"-columns-"
            files = [spec(path) for path in sorted(self.job.out.glob(self.base+"-"+suffix+"*.json.gz"))]
            self.job.store(name, {"complete_branch": branch_spec,
                "discarded_product_block_digests": files,
                "large_product_columns_replaced_by_complete_branch_inverse_and_kernel": True})
            receipt = self.job.cache(name)
        assert receipt["complete_branch"] == branch_spec
        for entry in receipt["discarded_product_block_digests"]:
            path = self.job.out/entry["file"]
            if path.exists():
                assert spec(path) == entry
                path.unlink()

    def branch(self, branch):
        if branch in self._branches:
            return self._branches[branch]
        self.job.budget()
        name = self.base+"-branch-"+str(branch).zfill(2)
        old = self.job.cache(name)
        invQ, Y = self.clear_inverse_y(branch)
        if old is None:
            if self.power == 5 and self.prime == ORIGINAL_PRIME:
                original_name = "R787-prime-1000000753-branch-"+str(branch).zfill(2)+".json.gz"
                original = self.job.r787.stage(original_name)
                assert original["actual_Schur_rank"] == 1186
                assert original["chart_sha256"] == PINNED_OLD_FILES[
                    "R787-prime-1000000753-chart.json.gz"]
                if branch == 0:
                    assert original["selected_minor_det_mod_prime"] == 296007862
                    assert original["roots_B_s"] == [3197390, 99932770]
                P, I = self.chart["pivot_columns"], self.chart["pivot_rows"]
                free = [j for j in range(self.d) if j not in set(P)]
                assert len(free) == 28 and RESERVED_FREE_COLUMN in free
                new_free = [j for j in free if j != RESERVED_FREE_COLUMN]
                Cfree = self.product_columns(Y, new_free, "reused-branch-"+str(branch).zfill(2))
                CJfree = submatrix(Cfree, self.J, prime=self.prime)
                CRfree = submatrix(Cfree, [self.AR[i] for i in I], prime=self.prime)
                inverse = nmod_mat(original["Schur_minor_inverse_mod_prime"], self.prime)
                CJp = nmod_mat(original["C_J_pivot_columns"], self.prime)
                cp = -inverse*(CRfree-submatrix(self.FAR, I, prime=self.prime)*self.Ainv*CJfree)
                anew = self.Ainv*(CJfree+CJp*cp)
                A = nmod_mat(self.n, 28, [0]*(self.n*28), self.prime)
                C = nmod_mat(self.d, 28, [0]*(self.d*28), self.prime)
                reserved_position = free.index(RESERVED_FREE_COLUMN)
                for i in range(self.n):
                    A[i, reserved_position] = int(original["initial_A"][i])
                for i in range(self.d):
                    C[i, reserved_position] = int(original["initial_C"][i])
                positions = []
                for j, column in enumerate(new_free):
                    target = free.index(column)
                    positions.append(target)
                    C[column, target] = 1
                    for i, pivot in enumerate(P):
                        C[pivot, target] = cp[i, j]
                    for i in range(self.n):
                        A[i, target] = anew[i, j]
                self.verify_vectors(Y, A, C, positions)
                inverse_rows = original["Schur_minor_inverse_mod_prime"]
                CJp_rows = original["C_J_pivot_columns"]
                determinant = int(original["selected_minor_det_mod_prime"])
                reuse = self.job.r787.file_spec(original_name)
            else:
                Cfull = self.product_columns(Y, list(range(self.d)),
                                             "new-branch-"+str(branch).zfill(2))
                CJ = submatrix(Cfull, self.J, prime=self.prime)
                CR = submatrix(Cfull, self.AR, prime=self.prime)
                S = CR-self.FAR*self.Ainv*CJ
                if self.chart is None:
                    P = pivots(S)
                    if len(P) != 1186:
                        raise BadPrime("The new sixfold Schur matrix has lower actual modular rank.")
                    I = pivots(submatrix(S, range(S.nrows()), P,
                                         prime=self.prime).transpose())
                    assert len(I) == 1186
                    self.job.store(self.chart_name, {"prime": self.prime,
                        "ordinary_power": self.power, "actual_rank": 1186,
                        "kernel_dimension": self.k, "pivot_columns": P, "pivot_rows": I,
                        "all_branches_certified_here": False})
                    self.chart = self.job.cache(self.chart_name)
                P, I = self.chart["pivot_columns"], self.chart["pivot_rows"]
                square = submatrix(S, I, P, prime=self.prime)
                try:
                    inverse = square.inv()
                except ZeroDivisionError as error:
                    raise BadPrime("The common original-field Schur minor vanishes in this branch.") from error
                free = [j for j in range(self.d) if j not in set(P)]
                assert len(free) == self.k
                cp = -inverse*submatrix(S, I, free, prime=self.prime)
                C = nmod_mat(self.d, self.k, [0]*(self.d*self.k), self.prime)
                for j, column in enumerate(free):
                    C[column, j] = 1
                for i, column in enumerate(P):
                    for j in range(self.k):
                        C[column, j] = cp[i, j]
                A = self.Ainv*CJ*C
                assert is_zero(S*C) and is_zero(self.FA*A-Cfull*C)
                determinant = int(square.det())
                inverse_rows = imatrix(inverse)
                CJp_rows = imatrix(submatrix(CJ, range(self.n), P, prime=self.prime))
                reuse = None
                del Cfull, CJ, CR, S, cp
            self.job.store(name, {"ordinary_power": self.power, "prime": self.prime,
                "branch": branch, "roots_B_s": self.selection["roots_B_s"][branch],
                "chart": spec(self.job.path(self.chart_name)),
                "rational_block": self.block_spec,
                "actual_Schur_rank": 1186, "selected_minor_det_mod_prime": determinant,
                "Schur_minor_inverse_mod_prime": inverse_rows,
                "C_J_pivot_columns": CJp_rows,
                "kernel_free_columns": free, "kernel_A_mod_prime": imatrix(A),
                "kernel_C_mod_prime": imatrix(C), "common_clear_multiplier_inverse": invQ,
                "full_original_modular_relations_verified_for_all_new_free_targets": True,
                "original_reserved_column_retained_without_new_lift": self.power == 5,
                "original_branch_inverse_reused_from": reuse})
            old = self.job.cache(name)
        assert old["ordinary_power"] == self.power and old["prime"] == self.prime
        assert old["branch"] == branch and old["actual_Schur_rank"] == 1186
        assert old["chart"] == spec(self.job.path(self.chart_name))
        assert old["rational_block"] == self.block_spec
        assert old["common_clear_multiplier_inverse"] == invQ
        if self.chart is None:
            self.chart = self.job.cache(self.chart_name)
        self.prune_product_blocks(branch, spec(self.job.path(name)))
        typed = dict(old)
        for key in ("Schur_minor_inverse_mod_prime", "C_J_pivot_columns",
                    "kernel_A_mod_prime", "kernel_C_mod_prime"):
            typed[key] = nmod_mat(old[key], self.prime)
        self._branches[branch] = typed
        return typed

    def all_branches(self):
        return [self.branch(branch) for branch in range(14)]

    def expand_B(self, C, modulus=None):
        C = fmpz_mat(C) if not isinstance(C, fmpz_mat) else C
        product = self.Zp*C
        rows = [[0]*C.ncols() for _ in range(self.n)]
        for j, index in enumerate(self.P):
            rows[index] = [int(product[j, i]) for i in range(C.ncols())]
        for j, index in enumerate(self.Q):
            rows[index] = [self.Zd*int(C[j, i]) for i in range(C.ncols())]
        if modulus is not None:
            rows = [[x % modulus for x in row] for row in rows]
        return rows



def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "proof", "method", "field-core", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        return Job(args).run()
    except BaseException as error:
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "exception_type": type(error).__name__,
            "error": str(error),
            "complete_stages_and_latest_lifts_preserved": True,
            "actual_complete_polar_module_certified": False})
        raise


if __name__ == "__main__":
    raise SystemExit(main())
