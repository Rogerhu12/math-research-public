#!/usr/bin/env python3
"""Source-bound original p=41 four-response solver.

Only public Actions executes new arithmetic.  The original full cleared
operator, canonical free column and exact CM functionals are unchanged.
No auxiliary-prime coordinate ball or rational-reconstruction candidate is an
input.  R854_p41_DVR_linear_algebra supplies finite-ring arithmetic and the
explicit row-saturation/left-inverse certificate.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
import time

RESULT = "R854-original-p41-four-response-balls"
FINAL = "p41-original-p41-four-response-balls-certificate.json"
PREFIX = "R854-p41-"
REPOSITORY = "Rogerhu12/math-research-public"
P, T, LDEG, ORDERS = 41, 20, 14, 129
NA, NC, NU, NROWS = 1234, 1214, 2420, 2560
METHOD_SHA256 = "ab97016925872ede018de18cd8faf18de228ca65857daa06404d99caff42eb41"
SCALING_SHA256 = "92cb6ec5250ea4f8bb4dcc81746001770f9209edef4cb974d703db75ed7fb71f"
CONTRACT_SHA256 = "569aa684267e4c4ae76581ce6ad6c6b4fd2ad62b45869ed87809a4c22151eeee"
ZA_SHA256 = "268fa3fbb9647d7f6f3f781534d9425e09c45ad7945e9aea9a9abd2082834d97"
SCOPE = {
    "original_p": P, "original_map_index": 4, "original_map_degree": "1206",
    "unknown_dimension": NU, "full_cleared_equation_rows": NROWS,
    "t_coordinates": T, "full_L_coordinate_dimension": LDEG,
    "original_free_column": 1186, "other_original_free_columns": "zero",
    "field_basis": "B^0..B^6,s*B^0..s*B^6; s^2=-3; B=lambda*b",
    "uniformizer": "original B=lambda*b", "ramification_index": 7,
    "residue_degree": 2,
    "cleared_A_sign": 1, "cleared_C_sign": 1, "free_rhs_sign": -1,
    "initial_scale_rule": "geometric-original-row-scaling; Rtilde_n=41^(a*n+c)R_n, Ktilde_n=41^(a*n)K_n, c=max(0,a-3)",
    "inverse_bound_applies_to": "geometrically_scaled_original_tall_matrix",
    "residue_lift_rule": "a+s*b with a,b in 0..40",
    "row_saturation_rule": "independent rows unchanged; dependent differences divided by B",
    "residue_matrix_backend": "paired restriction of scalars to nmod_mat(41)",
    "composite_modulus_matrix_inverse_used": False,
    "original_kappa_algebraic_inverse_recomputed": False,
    "completed_auxiliary_prime_arithmetic_recomputed": False,
    "auxiliary_518_balls_are_p41_inputs": False,
    "unaccepted_A1_candidate_consumed": False,
    "precision_and_budget_excluded_from_mathematical_identity": True,
    "working_matrix_retention": "latest complete saturation state; immutable row operations and SHA retirement receipts",
}


class BudgetStop(RuntimeError):
    pass


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+".tmp")
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n"
    if path.suffix == ".gz":
        with temporary.open("wb") as raw:
            with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, compresslevel=2) as stream:
                stream.write(encoded.encode())
    else:
        temporary.write_text(encoded)
    temporary.replace(path)


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def check(path, item):
    path = Path(path)
    assert path.name == item["file"] and path.is_file()
    assert path.stat().st_size == item["bytes"] and sha(path) == item["sha256"]


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def stage_configuration(path):
    """Read the small own-stage tag without retaining its large numeric body."""
    token = '"configuration":'
    decoder = json.JSONDecoder()
    buffer = ""
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        while True:
            block = stream.read(65536)
            if not block:
                raise AssertionError("Own stage lacks a complete configuration: "+str(path))
            buffer += block
            position = buffer.find(token)
            if position < 0:
                # Own-stage metadata before the configuration can include a
                # completed coefficient array.  Retain only the token overlap.
                buffer = buffer[-len(token):]
                continue
            value = buffer[position+len(token):]
            try:
                return decoder.raw_decode(value)[0]
            except json.JSONDecodeError:
                buffer = buffer[position:]


def load_module(name, path, expected_sha):
    assert sha(path) == expected_sha
    entry = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(entry)
    entry.loader.exec_module(module)
    return module


class Source:
    def __init__(self, root, label, source):
        self.path, self.label, self.source = Path(root)/label, label, source
        self.files = source["files"]
        for name, item in self.files.items():
            assert name == item["file"] and Path(name).name == name
        self.identity = {key: source[key] for key in
            ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256",
             "configuration_sha256")}
        self.identity["selected_files_sha256"] = canonical_sha(self.files)

    def get(self, name):
        item = self.files[name]
        check(self.path/name, item)
        obj = read(self.path/name)
        if isinstance(obj, dict) and "configuration" in obj:
            assert canonical_sha(obj["configuration"]) == self.identity["configuration_sha256"]
            if "complete" in obj:
                assert obj["complete"] is True
        return obj

    def referenced(self, item):
        assert {k: item[k] for k in ("file", "bytes", "sha256")} == self.files[item["file"]]
        return self.get(item["file"])


class Job:
    def __init__(self, args):
        self.args, self.out, self.started = args, args.output, time.monotonic()
        self.item = read(args.config)
        assert self.item["producer_inputs_pending"] is False
        assert self.item["core_sha256"] == sha(__file__)
        assert sha(args.method) == self.item["method_sha256"] == METHOD_SHA256
        assert sha(args.scaling_method) == self.item["scaling_method_sha256"] == SCALING_SHA256
        assert self.item["single_Z_contract_sha256"] == CONTRACT_SHA256
        assert self.item["ZA_proof_sha256"] == ZA_SHA256
        self.la = load_module("R854_bound_DVR", args.linear_algebra,
                              self.item["linear_algebra_sha256"])
        self.la.authorize()
        self.original = load_module("R854_original_R787", args.original_core,
                                    self.item["original_R787_core_sha256"])
        assert self.original.RESULT == "R787-original-power5-function-relation"
        assert self.original.ORDERS == ORDERS
        self.sources = {label: Source(args.retained, label, source)
                        for label, source in self.item["retained_sources"].items()}
        assert {"R781", "R787", "CM"}.issubset(self.sources)
        self.r781, self.r787, self.cm = [self.sources[k] for k in ("R781", "R787", "CM")]
        self.implicit = self.cm.get("R787-implicit-CM-exact-source-bound-implicit-expression.json.gz")
        assert self.implicit["complete"] and not self.implicit["expanded_coordinates_exactly_certified"]
        self.description = self.r781.get("R781-original-real-field-input.json.gz")["field"]
        assert self.description == self.implicit["original_field"]
        assert self.description["original_b_replaced_by_another_twist"] is False
        self.field = self.la.DVR(self.description["integral_B_minimal_polynomial"])
        self.blocks = self.r787.referenced(self.implicit["unit_chart_solve"]["original_Z_and_A_row_selection"])
        self.chart = self.r787.referenced(self.implicit["unit_chart_solve"]["original_chart"])
        assert self.blocks["complete"] and self.blocks["exact_E0_Z_zero_verified"]
        assert self.blocks["configuration"] == self.chart["configuration"]
        self.original_basis_scale = self.blocks["configuration"]["basis_integer_scale"]
        assert self.chart["chosen_free_column"] == 1186 and self.chart["actual_modular_rank"] == 1186
        self.pivots = list(self.chart["pivot_columns"])
        self.free = self.chart["chosen_free_column"]
        assert len(self.pivots) == 1186 and len(set(self.pivots)) == 1186
        assert self.free not in self.pivots
        self.P = list(self.blocks["B_constant_pivot_columns"])
        self.Q = list(self.blocks["B_constant_free_columns"])
        assert len(self.P) == 20 and len(self.Q) == NC
        self.Zd = int(self.blocks["Z_free_diagonal"])
        self.Zp = [[int(x) for x in row] for row in self.blocks["Z_pivot_integer_rows"]]
        assert len(self.Zp) == 20 and all(len(row) == NC for row in self.Zp)
        self.tag = {"result": RESULT, "source_sha256": sha(__file__), "python_flint": "0.9.0",
                    "method_sha256": METHOD_SHA256, "single_Z_contract_sha256": CONTRACT_SHA256,
                    "scaling_method_sha256": SCALING_SHA256,
                    "ZA_proof_sha256": ZA_SHA256,
                    "linear_algebra_sha256": self.item["linear_algebra_sha256"],
                    "original_R787_core_sha256": self.item["original_R787_core_sha256"],
                    "source_identities": {k: s.identity for k, s in self.sources.items()},
                    "field": self.description, "original_pivot_columns": self.pivots,
                    "operator_column_block_size": int(self.item.get("operator_column_block_size", 8)),
                    "matrix_checkpoint_rows": int(self.item.get("matrix_checkpoint_rows", 32)),
                    **SCOPE}
        self.out.mkdir(parents=True, exist_ok=True)
        self.R, self.K = [], []
        previous = None
        for n in range(130):
            self.budget()
            name = "R781-inverse-free-Laurent-"+str(n).zfill(3)+".json.gz"
            row = self.r781.get(name)
            assert row["order"] == n and row["complete"]
            assert row["exact_differential_identity_at_this_order"] is True
            if previous:
                assert row["previous_stage_sha256"] == self.r781.files[previous]["sha256"]
            self.K.append(row["coefficients"]["kappa_power"])
            if n < ORDERS:
                self.R.append(row["coefficients"]["R"])
            previous = name
        self.row_specs = self.implicit["operator_recipe"]["original_F_rows"]
        assert len(self.row_specs) == NA
        self.raw_F = None
        self.model = self.tensor_model()
        self.store_if_absent("source-audit", {
            "source_identities": self.tag["source_identities"],
            "canonical_2420_unknowns_and_free1186_preserved": True,
            "all_129_R_and_130_K_source_rows_unchanged": True,
            "full_cleared_system_has_same_unique_solution_as_original_U1": True,
            "all_m0_rows_are_zero_from_original_exact_E0Z_identity": True,
            "auxiliary_current_or_candidate_read": False,
            "actual_new_p41_numeric_response_available": False})

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes:
            raise BudgetStop("Completed original p41 stages retained; no old digit may be recomputed.")

    def path(self, stem):
        return self.out/(PREFIX+stem+".json.gz")

    def cache(self, stem):
        path = self.path(stem)
        if not path.exists():
            return None
        obj = read(path)
        assert obj["configuration"] == self.tag
        assert obj["complete"] is True
        return obj

    def store(self, stem, obj):
        path = self.path(stem)
        save(path, {**obj, "complete": True, "configuration": self.tag})
        print(json.dumps({"stage": path.name, "complete": True,
                          "seconds": time.monotonic()-self.started}), flush=True)
        return spec(path)

    def store_if_absent(self, stem, obj):
        cached = self.cache(stem)
        if cached is None:
            return self.store(stem, obj)
        for key, value in obj.items():
            assert cached[key] == value
        return spec(self.path(stem))

    def referenced(self, item):
        check(self.out/item["file"], item)
        obj = read(self.out/item["file"])
        assert obj["configuration"] == self.tag and obj["complete"]
        return obj

    def previous_precision_stage(self, precision, suffix):
        candidates = []
        pattern = re.compile(re.escape(PREFIX)+r"N(\d{6})-"+re.escape(suffix)+r"\.json\.gz")
        for path in self.out.glob(PREFIX+"N*-"+suffix+".json.gz"):
            match = pattern.fullmatch(path.name)
            if match and int(match.group(1)) < precision:
                candidates.append((int(match.group(1)), path))
        if not candidates:
            return None
        prior_precision, path = max(candidates)
        data = read(path)
        assert data["configuration"] == self.tag and data["complete"] is True
        assert data["absolute_B_precision"] == prior_precision
        return data, spec(path)

    def preserve_matrix_prefix(self, precision, suffix, matrix_data):
        prior = self.previous_precision_stage(precision, suffix)
        if prior is None:
            return {"preserved_lower_precision_source": None}
        old, old_spec = prior
        old_data = old["matrix"]
        assert old_data["shape"] == matrix_data["shape"]
        old_precision = old_data["absolute_B_precision"]
        assert old_precision < precision == matrix_data["absolute_B_precision"]
        for k in range(LDEG):
            cap = self.field.cap(old_precision, k % 7)
            for old_row, row in zip(old_data["coefficients"][k], matrix_data["coefficients"][k]):
                for j, value in enumerate(row):
                    low, value = int(old_row[j]), int(value)
                    assert 0 <= low < cap and value % cap == low
                    # Preserve the actual previous low part and append only
                    # the new high part; it is not counted as a new low layer.
                    row[j] = str(low+cap*(value//cap))
        return {"preserved_lower_precision_source": old_spec,
                "preserved_lower_absolute_B_precision": old_precision,
                "new_precision_interval": [old_precision, precision],
                "all_completed_lower_field_coefficients_preserved": True}

    def tensor_model(self):
        """Monic reduction tables from actual source polynomials, no inversion."""
        from flint import fmpz_mat
        def reduction(polynomial):
            f = [int(x) for x in polynomial]
            degree = len(f)-1
            assert f[-1] == 1
            rows = []
            for k in range(2*degree-1):
                values = [0]*(2*degree-1)
                values[k] = 1
                for j in range(2*degree-2, degree-1, -1):
                    c = values[j]
                    for i in range(degree):
                        values[j-degree+i] -= c*f[i]
                rows.append(values[:degree])
            return rows
        B = reduction(self.description["integral_B_minimal_polynomial"])
        Tred = reduction(self.description["real_cyclotomic_minimal_polynomial"])
        assert len(B) == 13 and len(Tred) == 39
        class Model:
            pass
        answer = Model()
        answer.Tred = fmpz_mat(Tred)
        answer.Bred = fmpz_mat([[B[j][i] if block == source else 0
            for source in range(2) for j in range(13)]
            for block in range(2) for i in range(7)])
        return answer

    def coefficient_scale(self):
        cached = self.cache("original-coefficient-scale")
        if cached:
            return cached
        def exponent(rows):
            result = 0
            for row in rows:
                assert len(row["primitive_integer_vector"]) == 280
                a, b = map(int, row["rational_scale"])
                assert b > 0
                if a:
                    result = max(result, self.la.v41(b)-self.la.v41(a))
            return result
        er, ek = exponent(self.R), exponent(self.K)
        slope = 0
        for rows in (self.R, self.K):
            for n, row in enumerate(rows):
                a, b = map(int, row["rational_scale"])
                if not a:
                    continue
                valuation = self.la.v41(a)-self.la.v41(b)
                if n == 0:
                    assert valuation >= 0
                else:
                    slope = max(slope, (-valuation+n-1)//n)
        intercept = max(0, slope-3)
        assert intercept+3-slope >= 0
        self.store("original-coefficient-scale", {
            "global_R_safe_exponent_for_audit_only": er,
            "global_K_safe_exponent_for_audit_only": ek,
            "geometric_slope_a": slope, "geometric_intercept_c": intercept,
            "R_source_p41_exponents": [slope*n+intercept for n in range(ORDERS)],
            "K_source_p41_exponents": [slope*n for n in range(130)],
            "original_row_block_p41_scale_exponents": [slope*m+intercept for m in range(1, ORDERS)],
            "A_multiplier_integer": str(6**3*P**(intercept+3-slope)),
            "initial_row_transform_B_valuation_lower_bound": 0,
            "initial_row_transform_is_identity_on_declared_scaled_matrix": True,
            "original_rational_scales_are_each_applied_once": True,
            "original_246_cubed_in_A_block_preserved_by_geometric_identity": True,
            "scaling_proof_sha256": SCALING_SHA256})
        return self.cache("original-coefficient-scale")

    def source_vector_mod(self, encoded, scale_exponent, modulus):
        a, b = map(int, encoded["rational_scale"])
        values = [int(x) for x in encoded["primitive_integer_vector"]]
        assert len(values) == 280 and b > 0
        if not a:
            return [0]*280
        va, vb = self.la.v41(a), self.la.v41(b)
        assert scale_exponent+va-vb >= 0
        aa, bb = a//P**va, b//P**vb
        factor = aa*pow(bb, -1, modulus)*pow(P, scale_exponent+va-vb, modulus) % modulus
        return [x*factor % modulus for x in values]

    def field_layer(self, precision):
        stem = "N"+str(precision).zfill(6)+"-source-field-coefficients"
        cached = self.cache(stem)
        if cached:
            return cached
        scale = self.coefficient_scale()
        modulus = self.field.modulus(precision)
        prior = self.previous_precision_stage(precision, "source-field-coefficients")
        if prior and int(prior[0]["integer_modulus"]) == modulus:
            self.store(stem, {"absolute_B_precision": precision, "integer_modulus": str(modulus),
                "R_scaled_vectors": prior[0]["R_scaled_vectors"],
                "K_scaled_vectors": prior[0]["K_scaled_vectors"],
                "scale": spec(self.path("original-coefficient-scale")),
                "same_completed_integer_modulus_source": prior[1],
                "exact_original_rational_scales_consumed": True})
            return self.cache(stem)
        rr = [self.source_vector_mod(x, scale["R_source_p41_exponents"][n], modulus) for n, x in enumerate(self.R)]
        kk = [self.source_vector_mod(x, scale["K_source_p41_exponents"][n], modulus) for n, x in enumerate(self.K)]
        if prior:
            old_modulus = int(prior[0]["integer_modulus"])
            assert modulus % old_modulus == 0
            for values, old_values in ((rr, prior[0]["R_scaled_vectors"]), (kk, prior[0]["K_scaled_vectors"])):
                for row, old_row in zip(values, old_values):
                    for j, value in enumerate(row):
                        low = int(old_row[j])
                        assert value % old_modulus == low
                        row[j] = low+old_modulus*(value//old_modulus)
        self.store(stem, {"absolute_B_precision": precision, "integer_modulus": str(modulus),
            "R_scaled_vectors": [[str(x) for x in row] for row in rr],
            "K_scaled_vectors": [[str(x) for x in row] for row in kk],
            "scale": spec(self.path("original-coefficient-scale")),
            "preserved_previous_source": prior[1] if prior else None,
            "exact_original_rational_scales_consumed": True})
        return self.cache(stem)

    def F_mod(self, precision):
        """Read original F bytes, reduce only at the requested target place."""
        modulus = self.field.modulus(precision)
        stem = "N"+str(precision).zfill(6)+"-original-F-reduction"
        cached = self.cache(stem)
        if cached:
            assert cached["shape"] == [ORDERS*T, NA]
            return self.la.matrix(ORDERS*T, NA,
                [int(x) for row in cached["rows"] for x in row], modulus)
        prior = self.previous_precision_stage(precision, "original-F-reduction")
        if prior and self.field.modulus(prior[0]["absolute_B_precision"]) == modulus:
            self.store(stem, {"absolute_B_precision": precision, "shape": [ORDERS*T, NA],
                "original_F_source_rows": self.row_specs, "rows": prior[0]["rows"],
                "same_completed_integer_modulus_source": prior[1],
                "original_phase_conversion_recomputed": False})
            return self.la.matrix(ORDERS*T, NA,
                [int(x) for row in prior[0]["rows"] for x in row], modulus)
        columns = []
        for i, item in enumerate(self.row_specs):
            self.budget()
            row = self.r787.referenced(item)
            assert row["index"] == i and row["all_original_phase_involutions_verified"]
            assert len(row["integer_t_coefficients"]) == ORDERS
            values = [int(x) % modulus for old in row["integer_t_coefficients"] for x in old]
            assert len(values) == ORDERS*T
            columns.append(values)
        rows = [[columns[j][i] for j in range(NA)] for i in range(ORDERS*T)]
        if prior:
            old_modulus = self.field.modulus(prior[0]["absolute_B_precision"])
            for row, old_row in zip(rows, prior[0]["rows"]):
                for j, value in enumerate(row):
                    low = int(old_row[j])
                    assert value % old_modulus == low
                    row[j] = low+old_modulus*(value//old_modulus)
        self.store(stem, {"absolute_B_precision": precision, "shape": [ORDERS*T, NA],
            "original_F_source_rows": self.row_specs,
            "rows": [[str(x) for x in row] for row in rows],
            "preserved_previous_source": prior[1] if prior else None,
            "original_phase_conversion_recomputed": False})
        return self.la.matrix(ORDERS*T, NA, [x for row in rows for x in row], modulus)

    def G_mod(self, precision, F):
        modulus = int(F.modulus())
        stem = "N"+str(precision).zfill(6)+"-original-FZ-reduction"
        cached = self.cache(stem)
        if cached:
            assert cached["shape"] == [ORDERS*T, NC]
            return self.la.matrix(ORDERS*T, NC,
                [int(x) for row in cached["rows"] for x in row], modulus)
        prior = self.previous_precision_stage(precision, "original-FZ-reduction")
        if prior and self.field.modulus(prior[0]["absolute_B_precision"]) == modulus:
            self.store(stem, {"absolute_B_precision": precision, "shape": [ORDERS*T, NC],
                "original_Z": self.implicit["unit_chart_solve"]["original_Z_and_A_row_selection"],
                "rows": prior[0]["rows"], "same_completed_integer_modulus_source": prior[1],
                "all_m0_rows_zero_verified": True,
                "original_Z_sign_and_diagonal_scale_preserved": True})
            return self.la.matrix(ORDERS*T, NC,
                [int(x) for row in prior[0]["rows"] for x in row], modulus)
        left = self.la.select(F, range(ORDERS*T), self.Q)*(self.Zd % modulus)
        right = self.la.select(F, range(ORDERS*T), self.P)*self.la.matrix(
            20, NC, [x for row in self.Zp for x in row], modulus)
        answer = left+right
        assert self.la.select(answer, range(20)) == self.la.zeros(20, NC, modulus)
        if prior:
            old_modulus = self.field.modulus(prior[0]["absolute_B_precision"])
            for i, old_row in enumerate(prior[0]["rows"]):
                for j, old in enumerate(old_row):
                    value, low = int(answer[i, j]), int(old)
                    assert value % old_modulus == low
                    answer[i, j] = low+old_modulus*(value//old_modulus)
        self.store(stem, {"absolute_B_precision": precision, "shape": [ORDERS*T, NC],
            "original_Z": self.implicit["unit_chart_solve"]["original_Z_and_A_row_selection"],
            "rows": [[str(int(answer[i, j])) for j in range(NC)]
                     for i in range(ORDERS*T)],
            "all_m0_rows_zero_verified": True,
            "preserved_previous_source": prior[1] if prior else None,
            "original_Z_sign_and_diagonal_scale_preserved": True})
        return answer

    def clear_A_blocks(self, precision, F, scaled):
        from flint import fmpz_mod_mat, fmpz_mod_ctx
        modulus = self.field.modulus(precision)
        kk = [[int(x) for x in row] for row in scaled["K_scaled_vectors"]]
        scale = self.coefficient_scale()
        multiplier = int(scale["A_multiplier_integer"]) % modulus
        ring = self.original.ModularField(self.model, modulus)
        output = []
        for m in range(1, ORDERS):
            self.budget()
            stem = "N"+str(precision).zfill(6)+"-A-order-"+str(m).zfill(3)
            cached = self.cache(stem)
            if cached:
                assert cached["order"] == m and cached["absolute_B_precision"] == precision
                output.append(spec(self.path(stem)))
                continue
            # Each column of this tiny 280-by-20 table is K_(m+1)*t^r.
            multiplication_columns = []
            for r in range(T):
                basis = [0]*280
                basis[r] = 1
                multiplication_columns.append(ring.multiply(kk[m+1], basis))
            multiplication = self.la.matrix(280, T,
                [multiplication_columns[j][i] for i in range(280) for j in range(T)], modulus)
            rows = self.la.select(F, range((m-1)*T, m*T))
            product = multiplication*rows*multiplier
            coeff = [self.la.select(product, range(i*T, (i+1)*T)) for i in range(LDEG)]
            data = self.field.matrix(coeff, precision).to_data()
            preserved = self.preserve_matrix_prefix(precision, "A-order-"+str(m).zfill(3), data)
            output.append(self.store(stem, {"order": m, "absolute_B_precision": precision,
                "matrix": data, "columns": list(range(NA)),
                "formula": "246^3*41^(c-a)*Ktilde_(m+1)*F_(m-1)",
                "original_integer_scale_not_applied_again": True, **preserved}))
        return output

    def clear_C_blocks(self, precision, G, scaled):
        modulus = self.field.modulus(precision)
        ring = self.original.ModularField(self.model, modulus)
        rr = [[int(x) for x in row] for row in scaled["R_scaled_vectors"]]
        kk = [[int(x) for x in row] for row in scaled["K_scaled_vectors"]]
        # Only pivot and the canonical free column are needed, retaining the
        # actual original index in each record.
        required = self.pivots+[self.free]
        output = []
        width = int(self.item.get("operator_column_block_size", 8))
        assert 1 <= width <= 32
        for first in range(0, len(required), width):
            self.budget()
            stop = min(first+width, len(required))
            stem = "N"+str(precision).zfill(6)+"-C-columns-"+str(first).zfill(4)
            cached = self.cache(stem)
            if cached:
                assert cached["original_columns"] == required[first:stop]
                output.append(spec(self.path(stem)))
                continue
            all_columns = []
            for column in required[first:stop]:
                self.budget()
                weighted = []
                for n in range(ORDERS):
                    base = [int(G[T*n+r, column]) for r in range(T)]+[0]*260
                    weighted.append(ring.multiply(kk[n], base))
                value = ring.convolution(rr, weighted)
                assert all(x == 0 for x in value[0])
                all_columns.append(value)
            coeff = []
            for coordinate in range(LDEG):
                values = [all_columns[c][m][coordinate*T+r]
                    for m in range(1, ORDERS) for r in range(T)
                    for c in range(stop-first)]
                coeff.append(self.la.matrix(NROWS, stop-first, values, modulus))
            data = self.field.matrix(coeff, precision).to_data()
            preserved = self.preserve_matrix_prefix(precision, "C-columns-"+str(first).zfill(4), data)
            output.append(self.store(stem, {"first_required_column": first,
                "stop_required_column": stop, "original_columns": required[first:stop],
                "absolute_B_precision": precision,
                "matrix": data,
                "formula": "sum_j Rtilde_(m-j)*Ktilde_j*(FZ)_j",
                "all_m0_original_coordinates_zero_verified": True, **preserved}))
        return output

    def operator(self, precision):
        stem = "N"+str(precision).zfill(6)+"-full-cleared-operator-index"
        cached = self.cache(stem)
        if cached:
            return cached
        self.budget()
        scaled = self.field_layer(precision)
        F = self.F_mod(precision)
        G = self.G_mod(precision, F)
        aa = self.clear_A_blocks(precision, F, scaled)
        cc = self.clear_C_blocks(precision, G, scaled)
        self.store(stem, {"absolute_B_precision": precision, "shape": [NROWS, NU],
            "A_row_blocks": aa, "C_column_blocks": cc,
            "C_original_columns": self.pivots+[self.free],
            "right_hand_side_is_negative_original_free_column": True,
            "scale": spec(self.path("original-coefficient-scale")),
            "source_field_coefficients": spec(self.path("N"+str(precision).zfill(6)+"-source-field-coefficients")),
            "original_m0_zero_from_exact_E0Z_and_current_modular_check": True,
            "same_unique_original_U1_solution": True})
        return self.cache(stem)

    def materialize_operator(self, index):
        """IO assembly of already completed coefficient blocks, no new algebra."""
        precision = index["absolute_B_precision"]
        modulus = self.field.modulus(precision)
        aa = [self.la.zeros(NROWS, NU, modulus) for _ in range(LDEG)]
        rhs = [self.la.zeros(NROWS, 1, modulus) for _ in range(LDEG)]
        for item in index["A_row_blocks"]:
            self.budget()
            block = self.referenced(item)
            data = block["matrix"]["coefficients"]
            start = (block["order"]-1)*T
            for k in range(LDEG):
                for i in range(T):
                    for j in range(NA):
                        aa[k][start+i, j] = int(data[k][i][j])
        for item in index["C_column_blocks"]:
            self.budget()
            block = self.referenced(item)
            data = block["matrix"]["coefficients"]
            first = block["first_required_column"]
            width = block["stop_required_column"]-first
            for k in range(LDEG):
                for i in range(NROWS):
                    for j in range(width):
                        if first+j == len(self.pivots):
                            rhs[k][i, 0] = -int(data[k][i][j]) % modulus
                        else:
                            aa[k][i, NA+first+j] = int(data[k][i][j])
        return self.field.matrix(aa, precision), self.field.matrix(rhs, precision)

    def matrix_stage(self, stem, value, metadata=None):
        cached = self.cache(stem)
        if cached:
            assert cached["shape"] == [value.nrows, value.ncols]
            assert cached["absolute_B_precision"] == value.N
            return spec(self.path(stem))
        rows_per_block = int(self.item.get("matrix_checkpoint_rows", 32))
        assert 1 <= rows_per_block <= 128
        blocks = []
        for first in range(0, value.nrows, rows_per_block):
            self.budget()
            stop = min(first+rows_per_block, value.nrows)
            block_name = stem+"-rows-"+str(first).zfill(4)
            block = self.cache(block_name)
            if block is None:
                blocks.append(self.store(block_name, {"first_row": first, "stop_row": stop,
                    "matrix": value.select(range(first, stop)).to_data()}))
            else:
                assert block["first_row"] == first and block["stop_row"] == stop
                blocks.append(spec(self.path(block_name)))
        return self.store(stem, {"shape": [value.nrows, value.ncols],
            "absolute_B_precision": value.N, "blocks": blocks, **(metadata or {})})

    def load_matrix(self, item):
        index = self.referenced(item)
        nr, nc = index["shape"]
        precision = index["absolute_B_precision"]
        modulus = self.field.modulus(precision)
        result = [self.la.zeros(nr, nc, modulus) for _ in range(LDEG)]
        first = 0
        for block_spec in index["blocks"]:
            self.budget()
            block = self.referenced(block_spec)
            assert block["first_row"] == first
            stop = block["stop_row"]
            matrix_key = index.get("matrix_key", "matrix")
            assert block[matrix_key]["shape"] == [stop-first, nc]
            data = block[matrix_key]["coefficients"]
            for k in range(LDEG):
                for i in range(first, stop):
                    for j in range(nc):
                        result[k][i, j] = int(data[k][i-first][j])
            first = stop
        assert first == nr
        return self.field.matrix(result, precision)

    def profile(self, step, a):
        stem = "saturation-profile-"+str(step).zfill(6)
        cached = self.cache(stem)
        if cached:
            result = {key: cached[key] for key in
                ("rank", "independent_rows", "dependent_rows", "pivot_columns",
                 "full_residue_row_identity_verified")}
            result["minor_inverse"] = self.la.FqMatrix.from_data(cached["minor_inverse"])
            result["combinations"] = self.la.FqMatrix.from_data(cached["combinations"])
            # This is exact source compatibility, not another rank computation.
            residue = a.residue()
            assert canonical_sha(residue.to_data()) == cached["input_residue_sha256"]
            return result, spec(self.path(stem))
        residue = a.residue()
        result = self.la.residue_profile(residue, self.budget)
        payload = {key: result[key] for key in
            ("rank", "independent_rows", "dependent_rows", "pivot_columns",
             "full_residue_row_identity_verified")}
        payload["minor_inverse"] = result["minor_inverse"].to_data()
        payload["combinations"] = result["combinations"].to_data()
        payload["input_residue_sha256"] = canonical_sha(residue.to_data())
        payload["first_input_absolute_B_precision"] = a.N
        return result, self.store(stem, payload)

    def saturation_update(self, precision, step, a, b, bounds, profile, profile_spec, previous):
        """Commit independent row tiles; completed tiles survive any hard stop."""
        prefix = "N"+str(precision).zfill(6)+"-saturation-"
        next_name = prefix+str(step+1).zfill(6)
        I, J = profile["independent_rows"], profile["dependent_rows"]
        rank, width = len(I), self.tag["matrix_checkpoint_rows"]
        combinations = profile["combinations"]
        top, right_top = a.select(I), b.select(I)
        all_blocks, new_bounds = [], []
        spans = []
        for left, stop, kind in ((0, rank, "retained"), (rank, NROWS, "divided")):
            for first in range(left, stop, width):
                spans.append((first, min(first+width, stop), kind))
        for first, stop, kind in spans:
            self.budget()
            block_name = next_name+"-rows-"+str(first).zfill(4)
            cached = self.cache(block_name)
            if cached is not None:
                assert cached["first_row"] == first and cached["stop_row"] == stop
                assert cached["profile"] == profile_spec and cached["previous_state"] == previous
                all_blocks.append(spec(self.path(block_name)))
                new_bounds.extend(cached["row_transform_lower_bounds"])
                continue
            if kind == "retained":
                rows = I[first:stop]
                matrix_block = a.select(rows).truncate(a.N-1)
                right_block = b.select(rows).multiply_pi(b.N)
                local_bounds = [bounds[i] for i in rows]
            else:
                positions = list(range(first-rank, stop-rank))
                rows = [J[i] for i in positions]
                coeff = combinations.select(positions)
                difference = a.select(rows)-top.unramified_left(coeff, self.budget)
                assert difference.residue() == self.la.FqMatrix.zero(stop-first, NU)
                matrix_block = difference.divide_pi()
                right_block = b.select(rows)-right_top.unramified_left(coeff, self.budget)
                local_bounds = []
                for local, source_row in enumerate(rows):
                    used = [bounds[source_row]]
                    for k, old in enumerate(I):
                        if coeff.a[local, k] or coeff.b[local, k]:
                            used.append(bounds[old])
                    local_bounds.append(min(used)-1)
            all_blocks.append(self.store(block_name, {"first_row": first, "stop_row": stop,
                "profile": profile_spec, "previous_state": previous,
                "original_current_row_indices": rows, "operation": kind,
                "matrix": matrix_block.to_data(), "right_numerator": right_block.to_data(),
                "row_transform_lower_bounds": local_bounds,
                "division_multiplied_back_at_all_known_digits": kind == "divided",
                "right_common_B_exponent_change": -1}))
            new_bounds.extend(local_bounds)
        assert len(new_bounds) == NROWS
        matrix_ref = self.store(next_name+"-matrix", {"shape": [NROWS, NU],
            "absolute_B_precision": a.N-1, "blocks": all_blocks, "matrix_key": "matrix"})
        right_ref = self.store(next_name+"-right-numerator", {"shape": [NROWS, 1],
            "absolute_B_precision": b.N, "blocks": all_blocks, "matrix_key": "right_numerator"})
        return self.store(next_name, {"step": step+1, "previous_state": previous,
            "profile": profile_spec, "matrix": matrix_ref, "right_numerator": right_ref,
            "right_common_B_exponent": -(step+1),
            "row_transform_lower_bounds": new_bounds,
            "exact_source_row_transform_preserved": True,
            "each_completed_row_tile_reused_without_recomputation": True})

    def retire_previous_work(self, previous_state, new_state):
        old = self.referenced(previous_state)
        if old["step"] == 0:
            return
        new = self.referenced(new_state)
        assert new["previous_state"] == previous_state and new["step"] == old["step"]+1
        name = "retired-work-"+previous_state["file"][len(PREFIX):-len(".json.gz")]
        record = self.cache(name)
        if record is None:
            retired = {}
            for key in ("matrix", "right_numerator"):
                item = old[key]
                index = self.referenced(item)
                retired[item["file"]] = item
                for block in index["blocks"]:
                    retired[block["file"]] = block
            self.store(name, {"retired_files": list(retired.values()),
                "old_completed_state": previous_state, "superseding_completed_state": new_state,
                "all_row_operations_and_bounds_remain_retained": True,
                "old_work_is_not_a_new_mathematical_input": True})
            record = self.cache(name)
        assert record["superseding_completed_state"] == new_state
        for item in record["retired_files"]:
            path = self.out/item["file"]
            if path.exists():
                check(path, item)
                path.unlink()

    def saturate(self, precision, original_a, original_b):
        prefix = "N"+str(precision).zfill(6)+"-saturation-"
        scale = self.coefficient_scale()
        bound = scale["initial_row_transform_B_valuation_lower_bound"]
        a, b, bounds, step = original_a, original_b, [bound]*NROWS, 0
        previous = None
        states = [path for path in self.out.glob(PREFIX+prefix+"*.json.gz")
                  if re.fullmatch(re.escape(PREFIX+prefix)+r"\d{6}\.json\.gz", path.name)]
        if states:
            latest = max(states, key=lambda p: p.name)
            initial = read(latest)
            assert initial["configuration"] == self.tag and initial["complete"] is True
            step = initial["step"]
            if step:
                a, b = self.load_matrix(initial["matrix"]), self.load_matrix(initial["right_numerator"])
                bounds = list(initial["row_transform_lower_bounds"])
                previous = initial["previous_state"]
                self.retire_previous_work(previous, spec(latest))
        while True:
            self.budget()
            name = prefix+str(step).zfill(6)
            cached = self.cache(name)
            if cached:
                assert cached["step"] == step
                if step:
                    assert cached["previous_state"] == previous
                    if a.N != precision-step:
                        a, b = self.load_matrix(cached["matrix"]), self.load_matrix(cached["right_numerator"])
                        bounds = list(cached["row_transform_lower_bounds"])
                previous = spec(self.path(name))
            else:
                if step == 0:
                    self.store(name, {"step": 0,
                        "initial_operator": spec(self.path("N"+str(precision).zfill(6)+"-full-cleared-operator-index")),
                        "right_common_B_exponent": 0,
                        "row_transform_lower_bounds": bounds,
                        "initial_scale": spec(self.path("original-coefficient-scale"))})
                    previous = spec(self.path(name))
                else:
                    raise AssertionError("A saturation state may only be committed with its new matrices.")
            profile, profile_spec = self.profile(step, a)
            if profile["rank"] == NU:
                rows = profile["independent_rows"]
                assert profile["pivot_columns"] == list(range(NU))
                inverse = profile["minor_inverse"]
                assert a.residue().select(rows)*inverse == self.la.FqMatrix.eye(NU)
                actual_bound = self.la.certified_left_inverse_bound(bounds, rows)
                fixed_name = "original-unit-minor-and-left-inverse-bound"
                fixed = {"saturation_step": step, "selected_rows": rows,
                    "residue_profile": profile_spec, "row_transform_lower_bounds": bounds,
                    "shape": [NU, NU], "original_tall_shape": [NROWS, NU],
                    "full_selected_residue_inverse_product_verified": True,
                    "right_common_B_exponent": -step, **actual_bound}
                fixed_spec = self.store_if_absent(fixed_name, fixed)
                unit = a.select(rows)
                right = b.select(rows)
                return unit, right, inverse, step, fixed_spec
            if a.N <= 1:
                raise self.la.NeedPrecision("Original p41 saturation has no further known B digit.")
            next_name = prefix+str(step+1).zfill(6)
            completed_next = self.cache(next_name)
            if completed_next:
                # Next pass loads it without repeating any saturated arithmetic.
                previous = spec(self.path(name))
                step += 1
                continue
            new_state = self.saturation_update(precision, step, a, b, bounds,
                                               profile, profile_spec, previous)
            self.retire_previous_work(previous, new_state)
            step += 1

    def candidate_lift(self, value, precision):
        """Lift the chosen finite polynomial representative, NOT its ball."""
        assert precision >= value.N
        modulus = self.field.modulus(precision)
        coefficients = []
        for k, c in enumerate(value.coeff):
            cap = self.field.cap(value.N, k % 7)
            coefficients.append(self.la.matrix(value.nrows, value.ncols,
                [int(x) % cap for x in c.entries()], modulus))
        return self.field.matrix(coefficients, precision)

    def dixon(self, precision, unit, right, inverse, depth, fixed_unit_spec):
        scaling = self.cache("original-unit-right-scaling")
        if scaling is None:
            # Only a proved lower bound is divided out.  The scale becomes a
            # fixed source-bound stage for all later precision layers.
            shift = min(depth, right.valuation_lower_bound(), right.N-1)
            self.store("original-unit-right-scaling", {
                "right_integral_B_factor": shift,
                "solution_denominator_B_power": depth-shift,
                "unit_certificate": fixed_unit_spec,
                "scale_is_not_a_claim_of_exact_right_side_valuation": True})
            scaling = self.cache("original-unit-right-scaling")
        assert scaling["unit_certificate"] == fixed_unit_spec
        shift = scaling["right_integral_B_factor"]
        denominator_power = depth-shift
        v = right.divide_pi_power(shift, self.budget) if shift else right
        initial_precision = min(unit.N, v.N)
        unit, v = unit.truncate(initial_precision), v.truncate(initial_precision)
        digit_specs = []
        digits = []
        # A transition is the transaction journal.  It is committed before its
        # separate digit file.  Recover a committed transition without doing
        # the already completed matrix-vector product again.
        for path in sorted(self.out.glob(PREFIX+"unit-Dixon-transition-*.json.gz")):
            transition = read(path)
            assert transition["configuration"] == self.tag and transition["complete"] is True
            digit_name = transition["digit_stage_stem"]
            if not self.path(digit_name).exists():
                self.store(digit_name, transition["digit_payload"])
        for path in sorted(self.out.glob(PREFIX+"unit-Dixon-digit-*.json.gz")):
            digit = read(path)
            assert digit["configuration"] == self.tag and digit["complete"]
            assert digit["digit_index"] == len(digits)
            assert digit["unit_certificate"] == fixed_unit_spec
            digits.append(self.la.FqMatrix.from_data(digit["digit"]))
            digit_specs.append(spec(path))
        # A lower requested precision may reuse a prefix of an already longer
        # successful layer; the longer original files stay retained unchanged.
        digits, digit_specs = digits[:initial_precision], digit_specs[:initial_precision]
        state_name = "N"+str(precision).zfill(6)+"-Dixon-current"
        state = self.cache(state_name)
        if state:
            assert state["unit_certificate"] == fixed_unit_spec
            completed = state["completed_digits"]
            assert 0 <= completed <= len(digits)
            if completed:
                assert state["last_digit"] == digit_specs[completed-1]
            residual = None if state["residual"] is None else self.field.from_data(state["residual"])
        else:
            completed = len(digits)
            if completed:
                old = self.la.digits_to_integral(self.field, digits, completed, self.budget)
                chosen = self.candidate_lift(old, initial_precision)
                difference = v-self.la.polynomial_matrix_product(unit, chosen, self.budget)
                # A previous completed digit prefix is only imported if it
                # divides the actual new residual at the new local precision.
                residual = difference.divide_pi_power(completed, self.budget) if completed < initial_precision else None
                if completed == initial_precision:
                    assert difference.is_zero()
            else:
                residual = v
            self.store(state_name, {"completed_digits": completed,
                "unit_certificate": fixed_unit_spec,
                "last_digit": digit_specs[-1] if digit_specs else None,
                "residual": None if residual is None else residual.to_data(),
                "solution_denominator_B_power": denominator_power,
                "previous_completed_digits_recomputed": False})
        # A digit may have been committed immediately before a hard stop, while
        # the current residual was not.  Reconcile exactly one such transaction
        # from the saved transition, rather than recomputing the digit.
        while completed < len(digits):
            transition = self.cache("unit-Dixon-transition-"+str(completed).zfill(6))
            assert transition is not None
            assert transition["digit_stage_stem"]+".json.gz" == digit_specs[completed]["file"][len(PREFIX):]
            digit_source = self.referenced(digit_specs[completed])
            for key, value in transition["digit_payload"].items():
                assert digit_source[key] == value
            assert transition["input_residual_sha256"] == canonical_sha(residual.to_data())
            residual = None if transition["next_residual"] is None else self.field.from_data(transition["next_residual"])
            completed += 1
        while completed < initial_precision:
            self.budget()
            assert residual is not None
            transition_name = "unit-Dixon-transition-"+str(completed).zfill(6)
            transition = self.cache(transition_name)
            if transition is not None:
                # Transition precision is tied to the run in which this digit
                # was first completed.  A larger layer imports its digit only;
                # it does not relabel an old lower-precision residual.
                assert transition["input_residual_sha256"] == canonical_sha(residual.to_data())
                digit_ref = spec(self.path(transition["digit_stage_stem"]))
                digit_data = self.referenced(digit_ref)
                digit = self.la.FqMatrix.from_data(digit_data["digit"])
                next_residual = None if transition["next_residual"] is None else self.field.from_data(transition["next_residual"])
            else:
                digit, next_residual = self.la.dixon_digit(unit, inverse, residual, self.budget)
                digit_name = "unit-Dixon-digit-"+str(completed).zfill(6)
                digit_payload = {"digit_index": completed,
                    "digit": digit.to_data(), "unit_certificate": fixed_unit_spec,
                    "previous_digit": digit_specs[-1] if digit_specs else None,
                    "digit_is_for_original_p41_not_auxiliary_prime": True}
                self.store(transition_name, {"digit_stage_stem": digit_name,
                    "digit_payload": digit_payload,
                    "input_residual_sha256": canonical_sha(residual.to_data()),
                    "next_residual": None if next_residual is None else next_residual.to_data(),
                    "first_operator_B_precision": precision,
                    "all_residue_coordinates_zero_before_division_verified": True})
                digit_ref = self.store(digit_name, digit_payload)
            digits.append(digit)
            digit_specs.append(digit_ref)
            residual, completed = next_residual, completed+1
            self.store(state_name, {"completed_digits": completed,
                "unit_certificate": fixed_unit_spec, "last_digit": digit_ref,
                "residual": None if residual is None else residual.to_data(),
                "solution_denominator_B_power": denominator_power,
                "previous_completed_digits_recomputed": False})
        polynomial = self.la.digits_to_integral(self.field, digits, completed, self.budget)
        return polynomial, denominator_power, digit_specs

    def original_residual(self, precision, a, b, polynomial, denominator_power, unit_spec, digit_specs):
        stem = "N"+str(precision).zfill(6)+"-full-original-residual"
        cached = self.cache(stem)
        if cached:
            return cached
        vector_stem = stem+"-vector"
        saved_vector = self.cache(vector_stem)
        if saved_vector is None:
            candidate = self.candidate_lift(polynomial, precision)
            rhs = b
            for _ in range(denominator_power):
                rhs = rhs.multiply_pi(precision)
            residual = self.la.polynomial_matrix_product(a, candidate, self.budget)-rhs
            # This small vector is a single atomic mathematical stage.  A stop
            # before the certificate is written must not repeat its product.
            self.store(vector_stem, {"matrix": residual.to_data(),
                "unit_certificate": unit_spec, "last_digit": digit_specs[-1],
                "candidate_solution_denominator_B_power": denominator_power})
        else:
            assert saved_vector["unit_certificate"] == unit_spec
            assert saved_vector["last_digit"] == digit_specs[-1]
            assert saved_vector["candidate_solution_denominator_B_power"] == denominator_power
            residual = self.field.from_data(saved_vector["matrix"])
            assert residual.N == precision and residual.nrows == NROWS and residual.ncols == 1
        numerator_row_bounds = []
        for row in range(NROWS):
            bound = residual.N
            for k, component in enumerate(residual.coeff):
                degree = k % 7
                value = int(component[row, 0]) % self.field.cap(residual.N, degree)
                if value:
                    bound = min(bound, 7*self.la.v41(value)+degree)
            numerator_row_bounds.append(bound)
        block_scales = self.coefficient_scale()["original_row_block_p41_scale_exponents"]
        original_row_bounds = [value-denominator_power-7*block_scales[i//T]
                               for i, value in enumerate(numerator_row_bounds)]
        weighted_bound = min(numerator_row_bounds)-denominator_power
        # The exact original row scales are explicitly put back into the
        # weighted norm; no scaling gain is labelled as an unweighted residual.
        assert weighted_bound == min(value+7*block_scales[i//T]
                                     for i, value in enumerate(original_row_bounds))
        unit = self.referenced(unit_spec)
        w = unit["minimum_left_inverse_entry_valuation_lower_bound"]
        error_bound = weighted_bound+w
        row_refs = spec(self.path(vector_stem))
        self.store(stem, {"absolute_B_precision": precision,
            "original_rows_verified": NROWS, "original_L_coordinates_per_row": LDEG,
            "residual_numerator": row_refs,
            "residual_numerator_row_B_valuation_lower_bounds": numerator_row_bounds,
            "candidate_solution_denominator_B_power": denominator_power,
            "original_row_block_p41_scale_exponents": block_scales,
            "full_original_residual_row_B_valuation_lower_bounds": original_row_bounds,
            "full_original_unweighted_residual_B_valuation_lower_bound": min(original_row_bounds),
            "full_original_weighted_residual_B_valuation_lower_bound": weighted_bound,
            "inverse_bound_applies_to": SCOPE["inverse_bound_applies_to"],
            "exact_original_row_scales_removed_and_weightedly_restored": True,
            "unit_certificate": unit_spec,
            "minimum_left_inverse_entry_valuation_lower_bound": w,
            "certified_solution_error_absolute_B_precision": error_bound,
            "last_digit": digit_specs[-1],
            "completed_B_digits": len(digit_specs),
            "original_m0_twenty_by_fourteen_coordinates_exactly_zero": True,
            "full_129_by_20_by_14_original_cleared_identity_used": True,
            "inverse_norm_bound_used_not_residual_alone": True,
            "candidate_is_a_chosen_exact_finite_polynomial_not_an_A1_acceptance": True})
        return self.cache(stem)

    def exact_response_rows(self):
        source = self.implicit["linear_responses"]
        jets_index = self.cm.referenced(source["e0_e1"])
        ez_index = self.cm.referenced(source["e0Z_e1Z"])
        assert jets_index["dimension"] == NA and jets_index["derivative_order"] == 1
        assert ez_index["columns"] == NC and ez_index["eZ_computed_in_characteristic_zero"]
        assert ez_index["exact_K_basis"] == "1,s"
        assert jets_index["integer_scale"] == ez_index["integer_scale"] == self.original_basis_scale
        e, ez = {}, {}
        for item in jets_index["completed_blocks"]:
            data = self.cm.referenced(item)
            if data["power"] == 5:
                assert data["exact_K_basis"] == "1,s; s^2=-3"
                for row in data["rows"]:
                    assert row["index"] not in e
                    e[row["index"]] = row
        for item in ez_index["blocks"]:
            data = self.cm.referenced(item)
            assert data["Z_pivot_rows_already_include_minus_sign"] is True
            for row in data["rows"]:
                assert row["index"] not in ez
                ez[row["index"]] = row
        assert sorted(e) == list(range(NA)) and sorted(ez) == list(range(NC))
        zero = [["0", "1"], ["0", "1"]]
        rows, constants = [], []
        for name, key in (("A0", "value"), ("A1", "derivative_z")):
            rows.append([e[i][key] for i in range(NA)]+[zero]*1186)
            constants.append(zero)
        for name, key in (("B0", "value"), ("B1", "derivative_z")):
            rows.append([zero]*NA+[ez[j][key] for j in self.pivots])
            constants.append(ez[self.free][key])
        return rows, constants

    def response_balls(self, precision, polynomial, denominator_power, residual):
        stem = "N"+str(precision).zfill(6)+"-four-original-response-balls"
        cached = self.cache(stem)
        if cached:
            return cached
        rows, constants = self.exact_response_rows()
        shift = 0
        for value in [x for row in rows for x in row]+constants:
            for numerator, denominator in value:
                numerator, denominator = int(numerator), int(denominator)
                assert denominator > 0
                if numerator:
                    shift = max(shift, self.la.v41(denominator)-self.la.v41(numerator))
        modulus = self.field.modulus(precision)
        def rational(pair):
            a, b = map(int, pair)
            if not a:
                return 0
            va, vb = self.la.v41(a), self.la.v41(b)
            assert shift+va-vb >= 0
            return a//P**va*pow(b//P**vb, -1, modulus)*pow(P, shift+va-vb, modulus) % modulus
        weight = [self.la.zeros(4, NU, modulus) for _ in range(LDEG)]
        constant = [self.la.zeros(4, 1, modulus) for _ in range(LDEG)]
        for i in range(4):
            for j in range(NU):
                weight[0][i, j], weight[7][i, j] = rational(rows[i][j][0]), rational(rows[i][j][1])
            constant[0][i, 0], constant[7][i, 0] = rational(constants[i][0]), rational(constants[i][1])
        candidate = self.candidate_lift(polynomial, precision)
        value = self.la.polynomial_matrix_product(self.field.matrix(weight, precision), candidate, self.budget)
        const = self.field.matrix(constant, precision)
        for _ in range(denominator_power):
            const = const.multiply_pi(precision)
        value = value+const
        available = min(precision-denominator_power-7*shift,
                        residual["certified_solution_error_absolute_B_precision"]-7*shift)
        self.store(stem, {"labels": ["A0", "A1", "B0", "B1"],
            "numerators": value.to_data(), "common_denominator_B_power": denominator_power,
            "common_denominator_p41_power": shift,
            "absolute_B_precision": available,
            "absolute_p41_precision_rational": [available, 7],
            "full_original_residual_certificate": spec(self.path("N"+str(precision).zfill(6)+"-full-original-residual")),
            "exact_functionals": self.implicit["linear_responses"],
            "original_CM_scale_applied_again": False,
            "B_response_free1186_constant_preserved": True,
            "actual_original_p41_four_response_balls_certified": True,
            "expanded_exact_L_coordinates_accepted": False,
            "A1_exact_zero_proved": False})
        return self.cache(stem)

    def finish(self, responses=None, error=None):
        inventory = []
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name == PREFIX+"stage-manifest.json.gz":
                continue
            assert stage_configuration(path) == self.tag
            inventory.append(spec(path))
        manifest_spec = self.store("stage-manifest", {"files": inventory,
            "all_stages_are_new_original_p41_or_unchanged_source_references": True,
            "requested_precision": int(self.item.get("requested_response_B_precision", 7))})
        achieved = None if responses is None else responses["absolute_B_precision"]
        requested = int(self.item.get("requested_response_B_precision", 7))
        complete = achieved is not None and achieved >= requested
        final = {"result": RESULT, "configuration": self.tag, "complete": complete,
            "source_audit": spec(self.path("source-audit")), "stage_manifest": manifest_spec,
            "requested_response_absolute_B_precision": requested,
            "actual_response_absolute_B_precision": achieved,
            "four_response_balls": None if responses is None else spec(self.path(
                "N"+str(int(self.item.get("operator_B_precision", 56))).zfill(6)+"-four-original-response-balls")),
            "unit_minor_and_left_inverse_bound": spec(self.path("original-unit-minor-and-left-inverse-bound"))
                if self.path("original-unit-minor-and-left-inverse-bound").exists() else None,
            "actual_original_p41_four_response_balls_certified": responses is not None,
            "expanded_exact_L_coordinates_accepted": False,
            "A1_exact_zero_proved": False, "actual_Z_computed": False,
            "actual_height_computed": False,
            "auxiliary_prime_ball_used_as_p41": False,
            "precision_request_reason": error,
            "scope_seconds": time.monotonic()-self.started}
        save(self.out/FINAL, final)
        return final

    def run(self):
        precision = int(self.item.get("operator_B_precision", 56))
        assert precision >= 2
        existing = self.out/FINAL
        if existing.exists():
            final = read(existing)
            assert final["configuration"] == self.tag
            if final["complete"] and final["actual_response_absolute_B_precision"] >= int(self.item.get("requested_response_B_precision", 7)):
                return final
        index = self.operator(precision)
        original_a, original_b = self.materialize_operator(index)
        unit, right, inverse, depth, unit_spec = self.saturate(precision, original_a, original_b)
        polynomial, denominator_power, digits = self.dixon(precision, unit, right, inverse, depth, unit_spec)
        residual = self.original_residual(precision, original_a, original_b,
                                         polynomial, denominator_power, unit_spec, digits)
        responses = self.response_balls(precision, polynomial, denominator_power, residual)
        return self.finish(responses)


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
        raise SystemExit("New arithmetic is restricted to this public repository's Actions.")
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--method", type=Path, required=True)
    parser.add_argument("--scaling-method", type=Path, required=True)
    parser.add_argument("--linear-algebra", type=Path, required=True)
    parser.add_argument("--original-core", type=Path, required=True)
    parser.add_argument("--retained", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    started, job, final, error, exit_code = time.monotonic(), None, None, None, 0
    try:
        job = Job(args)
        final = job.run()
        if not final["complete"]:
            exit_code = 125
    except BudgetStop as exc:
        error, exit_code = str(exc), 124
        if job is not None:
            final = job.finish(error=error)
    except Exception as exc:
        error = type(exc).__name__+": "+str(exc)
        if job is not None and isinstance(exc, job.la.NeedPrecision):
            exit_code = 125
            final = job.finish(error=error)
        else:
            import traceback
            traceback.print_exc()
            exit_code = 1
    args.output.mkdir(parents=True, exist_ok=True)
    receipt = {"result": RESULT, "core_sha256": sha(__file__),
        "complete": bool(final and final["complete"]), "exit_code": exit_code,
        "configuration": None if job is None else job.tag,
        "configuration_sha256": None if job is None else canonical_sha(job.tag),
        "final_sha256": sha(args.output/FINAL) if (args.output/FINAL).exists() else None,
        "error": error, "seconds": time.monotonic()-started,
        "all_new_arithmetic_confined_to_original_p41": True,
        "A1_exact_zero_proved": False, "actual_height_computed": False}
    save(args.output/"core-receipt.json", receipt)
    print(json.dumps(receipt, sort_keys=True), flush=True)
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()

