#!/usr/bin/env python3
"""R797: new Laurent inputs for the five actually selected original Hom maps."""
import argparse
import gzip
import hashlib
import importlib.util
import itertools
import json
import math
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpq, fmpq_poly, fmpz_mat, fmpz_poly

RESULT = "R797-five-original-low-degree-Laurent-prefixes"
FINAL = "p41-five-original-low-degree-Laurent-prefixes-certificate.json"
R774_CORE = "b7e8bf0f7b629881d973afaec01a2b905c4100573d46920841a9d48489e597fa"
R781_CORE = "d024a7a6f5febd4658e8b5b5e5e3659f3c5fcc0daa39d70569ac408ef83a8751"
R781_PROOF = "152c723da76b5c899b433db640fb6ac69082b46543f3d6bfa85d1cead7d78de0"
R793_PROOF = "6f716b64432227244a46d91f01ae2f46ba6d4a5f893666693ed07dec9e2e5cab"
R794_CORE = "9fc7f30b06ebe4d2721fc5e67aecc40abae2d72a58268e8eac9164d3ff1c3d45"
R794_PROOF = "14a0a9e8bafdf8d45766aef148f9b4c8034dd5b326ac310972551fe51a4d2cf5"
MODEL_WITNESS = "R774-original-L-cubic-scalars.json.gz"
MODEL_WITNESS_SHA = "b5b1232fa0585e6437d0e8d5f92b81efe672e91ed417bce7f6bc66c6456d596e"
SELECTED = "R794-selected-original-low-degree-eta-basis.json.gz"
SELECTED_SHA = "5b96f623e1f43d834a7db21064ff2cb101284b9a4038e5434eb291b6e73f6e0f"
TARGETS = [(0, [0], 1485, 7, 170), (3, [3], 1521, 7, 172),
           (1, [1], 1602, 7, 176), (21, [0, 10], 1674, 8, 193),
           (15, [0, 4], 1728, 8, 196)]
DEN, CYC, OLD_BOUND = 1722, 40, 820
STATE_KEYS = ("R", "W", "R2", "W2", "U", "U2", "Atilde", "kappa_power")


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
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    raw = (json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"))+"\n").encode("utf-8")
    if path.suffix == ".gz":
        with temporary.open("wb") as stream:
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb", mtime=0,
                               compresslevel=2) as compressed:
                compressed.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def dp(value):
    return fmpq_poly([int(x) for x in value["numerator"]], int(value["denominator"]))


def ep(value):
    return {"numerator": [str(x) for x in value.numer().coeffs()],
            "denominator": str(value.denom())}


class OriginalL:
    """The same original Q[b,zeta], for NEW differential cubic scalars only."""
    def __init__(self, modulus):
        self.mod = dp(modulus)
        assert self.mod.degree() == 7 and self.mod[7] == 1

    def decode(self, value):
        assert len(value) == 2
        result = dp(value[0]), dp(value[1])
        assert all(a.degree() < 7 for a in result)
        return result

    def multiply(self, left, right):
        a, b = left
        c, d = right
        ac, bd = a*c, b*d
        return (ac-bd) % self.mod, (a*d+b*c-bd) % self.mod


class Retained:
    def __init__(self, root, label, spec):
        self.directory, self.spec = Path(root)/label, spec
        manifest_path = self.directory/"full-outputs-manifest.json"
        assert sha(manifest_path) == spec["manifest_sha256"]
        manifest = read(manifest_path)
        assert manifest["result"] == spec["result"]
        self.files = {row["file"]: row for row in manifest["files"]}
        assert len(self.files) == len(manifest["files"])
        run, core, initial = (self.raw(name) for name in
                             ("run-receipt.json", "core-receipt.json", "public-actions-input.json"))
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert str(run["workflow_run_id"]) == str(spec["run_id"])
        assert run["source_commit"] == initial["source_commit"] == spec["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["result"] == core["result"] == spec["result"]
        assert core["complete"] is True and core["source_sha256"] == spec["core_sha256"]
        assert initial["job"]["core_sha256"] == spec["core_sha256"]
        if label == "R774":
            assert run["result"] == spec["result"]
            assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
            assert initial["core_sha256"] == spec["core_sha256"]
        else:
            assert label == "R794"
            assert "core_receipt_sha256" not in run and "core_sha256" not in initial
        name = spec["certificate_name"]
        assert self.files[name]["sha256"] == core["certificate_sha256"] == spec["files"][name]
        self.certificate = self.raw(name)
        assert self.certificate["complete"] is True and self.certificate["result"] == spec["result"]
        self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == spec["core_sha256"] and self.tag["python_flint"] == "0.9.0"
        self.stages = {row["file"]: row for row in self.certificate["stages"]}

    def raw(self, name, expected=None):
        assert Path(name).name == name
        row = self.files[name]
        if expected is not None:
            assert row["sha256"] == expected
        if name in self.spec["files"]:
            assert row["sha256"] == self.spec["files"][name]
        path = self.directory/name
        assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
        return read(path)

    def get(self, name, expected=None):
        value = self.raw(name, expected)
        assert value["complete"] is True and value["configuration"] == self.tag
        assert self.stages[name]["sha256"] == self.files[name]["sha256"]
        assert self.stages[name]["bytes"] == self.files[name]["bytes"]
        return value


class BudgetStop(RuntimeError):
    pass


class Job:
    def __init__(self, args):
        self.args, self.out = args, args.output
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        self.config = read(args.config)
        assert flint.__version__ == "0.9.0"
        assert self.config["producer_inputs_pending"] is False
        assert self.config["result"] == RESULT and self.config["p"] == 41
        assert self.config["core_sha256"] == sha(__file__)
        assert sha(args.method) == self.config["R797_method_sha256"]
        assert sha(args.cusp_proof) == self.config["R793_proof_sha256"] == R793_PROOF
        assert sha(args.recurrence_proof) == self.config["R781_proof_sha256"] == R781_PROOF
        assert sha(args.laurent_core) == self.config["R781_core_sha256"] == R781_CORE
        assert set(self.config["retained_artifacts"]) == {"R774", "R794"}
        self.r774, self.r794 = (Retained(args.retained, label, self.config["retained_artifacts"][label])
                                for label in ("R774", "R794"))
        assert self.r774.tag["source_sha256"] == R774_CORE
        assert self.r794.tag["source_sha256"] == R794_CORE and self.r794.tag["proof_sha256"] == R794_PROOF
        for name in ("p41-original-integral-period-lattice-and-degree-certificate.json",
                     "R759-original-integral-maps-and-bounded-recovery-input.json.gz"):
            assert self.r774.tag["retained_input_sha256"][name] == \
                self.r794.tag["retained_artifacts"]["R759"]["files"][name]
        assert self.r774.tag["H_normalization"] == "H=alpha*F/1722; alpha^3=4"
        assert self.r774.tag["cube_normalization"] == "H^3=4*F^3/1722^3"
        assert self.r774.tag["c1_phase_applied_a_second_time"] is False
        assert self.r774.certificate["original_six_Fourier_rows_generated_through_Q"] == 2460
        assert self.r774.certificate["no_Neron_Manin_or_KS_scale_changed"] is True
        model_witness = self.r774.get(MODEL_WITNESS, MODEL_WITNESS_SHA)
        self.original_modulus = model_witness["original_b_minimal_polynomial"]
        self.L = OriginalL(self.original_modulus)
        self.triples = list(itertools.combinations_with_replacement(range(6), 3))
        assert len(self.triples) == 56 and model_witness["triples"] == [list(v) for v in self.triples]
        selected = self.r794.get(SELECTED, SELECTED_SHA)
        assert selected["selected_candidate_indices"] == self.r794.certificate["selected_candidate_indices"] == [v[0] for v in TARGETS]
        assert selected["selected_basis_rank"] == 5 and selected["original_kappa_e_R_q_c0_c1_preserved"] is True
        self.maps = selected["selected_maps"]
        assert len(self.maps) == len(self.config["maps"]) == 5
        for row, item, expected in zip(self.maps, self.config["maps"], TARGETS):
            candidate, sources, degree, power, count = expected
            assert row["candidate_index"] == item["candidate_index"] == candidate
            assert row["source_indices"] == sources
            assert int(row["map_degree"]) == int(item["map_degree"]) == degree
            bounds = row["R793_exact_engineering_bounds"]
            assert bounds["ordinary_section_power"] == item["ordinary_power"] == power
            assert bounds["complete_Laurent_conditions"] == item["complete_Laurent_conditions"] == count
            assert item["normalized_R_bound"] == count-1 and item["H3_bound"] == count
            assert bounds["Laurent_exponents"] == [-1, count-2]
            assert bounds["basis_highest_qY_exponent"] == count-1 and bounds["all_cusp_pole_orders"] == 1
            assert power == (degree+254+271)//272 and count == (272*power+degree)//20+1
            assert row["differential_coordinate_basis"] == "R759 original b^0..b^6 in 1,zeta for each R745 omega_0..omega_5"
            assert len(row["original_omega_differential_coordinates"]) == 6
            assert any(a or b for a, b in map(self.L.decode, row["original_omega_differential_coordinates"]))
            assert row["actual_original_weighted_trace_identity_verified"] is True
        source = importlib.util.spec_from_file_location("R797_retained_R781_arithmetic", args.laurent_core)
        implementation = importlib.util.module_from_spec(source)
        source.loader.exec_module(implementation)
        self.field = implementation.Field(self.original_modulus)
        self.tag = {"result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "R797_method_sha256": sha(args.method), "R793_proof_sha256": R793_PROOF,
            "R781_proof_sha256": R781_PROOF, "R781_core_sha256": R781_CORE,
            "retained_artifacts": self.config["retained_artifacts"], "maps": self.config["maps"],
            "p": 41, "field": self.field.description,
            "H3_normalization": "qY*sum(4*multinomial*v_i*v_j*v_k/1722^3 * old_G_iG_jG_k)",
            "original_qY": "qY=Q^3=exp(2*pi*i*tau/82), original reference cusp",
            "real_tangent_parameter": "v=xi41^-10*qY",
            "inverse_free_parameter_for_each_map": "v=kappa_f*w",
            "original_target": "y^2=x^3+b; original b and Neron differential",
            "target_translation": "original f(c0)=O",
            "old_f4_or_shared_Hodge_products_recomputed": False,
            "second_c1_phase_or_real_descent_isogeny_applied": False}
        self.monomials = None

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes:
            raise BudgetStop("Complete per-map/per-order checkpoints retained; resume without repeating them.")

    def path(self, name):
        assert name.startswith("R797-") and Path(name).name == name
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
        return self.path(name)

    def prefix(self, row):
        return "R797-map-"+str(row["candidate_index"]).zfill(3)

    def shared_monomials(self):
        if self.monomials is not None:
            return self.monomials
        rows, bound = [], max(item[4] for item in TARGETS)
        for index, triple in enumerate(self.triples):
            name = "R774-cubic-monomial-"+str(index).zfill(2)+".json.gz"
            value = self.r774.get(name)
            assert value["indices"] == list(triple)
            assert value["G_exponent_range_exclusive"] == [0, OLD_BOUND]
            assert value["xi_basis_degree"] == CYC and value["complete_low_product_computed"] is True
            assert value["coefficient_ring"] == "Z[s,xi41], s^2=-3, Phi41(xi41)=0"
            for key in ("real_coefficients_flat_qY_xi", "s_coefficients_flat_qY_xi"):
                assert len(value[key]) == OLD_BOUND*CYC
                rows.append([int(x) for x in value[key][:bound*CYC]])
        assert len(rows) == 112
        self.monomials = rows
        return rows

    def new_scalars(self, row):
        name = self.prefix(row)+"-new-L-cubic-scalars"
        old = self.cached(name)
        if old:
            assert old["candidate_index"] == row["candidate_index"]
            assert old["original_omega_differential_coordinates"] == row["original_omega_differential_coordinates"]
            return old
        self.budget()
        v = [self.L.decode(value) for value in row["original_omega_differential_coordinates"]]
        pairs = {(i, j): self.L.multiply(v[i], v[j]) for i in range(6) for j in range(i, 6)}
        rational = [[fmpq(0)]*112 for _ in range(14)]
        encoded_scalars = []
        for position, (i, j, k) in enumerate(self.triples):
            multiplicity = 1 if i == k else (3 if i == j or j == k else 6)
            a, b = self.L.multiply(pairs[i, j], v[k])
            scalar = fmpq(4*multiplicity, DEN**3)
            a, b = a*scalar, b*scalar
            encoded_scalars.append([ep(a), ep(b)])
            real, imaginary = a-b/2, b/2
            for power in range(7):
                rational[power][2*position], rational[power][2*position+1] = real[power], -3*imaginary[power]
                rational[7+power][2*position], rational[7+power][2*position+1] = imaginary[power], real[power]
        integer, scales = [], []
        for original in rational:
            denominator = 1
            for value in original:
                denominator = math.lcm(denominator, int(value.denom()))
            values = [int((value*denominator).numer()) for value in original]
            content = 0
            for value in values:
                content = math.gcd(content, abs(value))
            if content:
                scale = fmpq(content, denominator)
                integer.append([str(value//content) for value in values])
            else:
                scale = fmpq(0)
                integer.append([str(value) for value in values])
            scales.append([str(scale.numer()), str(scale.denom())])
        self.store(name, {"candidate_index": row["candidate_index"], "map_degree": row["map_degree"],
            "original_Hom_integer_column": row["original_Hom_integer_column"],
            "original_omega_differential_coordinates": row["original_omega_differential_coordinates"],
            "triples": [list(value) for value in self.triples], "new_original_L_scalars": encoded_scalars,
            "scalar_normalization": "4*multinomial*v_i*v_j*v_k/1722^3",
            "primitive_integer_matrix": integer, "rational_row_scales": scales,
            "row_basis": "b^0..b^6,s*b^0..s*b^6",
            "column_basis": "real,s of original R774 G_iG_jG_k, lexicographic nondecreasing triples",
            "original_b_minimal_polynomial": self.original_modulus,
            "old_f4_scalar_matrix_consumed": False, "old_shared_triples_recomputed": False})
        return self.cached(name)

    def real_inputs(self, row, scalars):
        name = self.prefix(row)+"-original-real-H3-input"
        old = self.cached(name)
        count = row["R793_exact_engineering_bounds"]["complete_Laurent_conditions"]
        scalar_sha = sha(self.path(self.prefix(row)+"-new-L-cubic-scalars"))
        if old:
            assert old["candidate_index"] == row["candidate_index"] and old["H3_bound"] == count
            assert old["new_scalar_stage_sha256"] == scalar_sha
            return old, [self.field.decode(value) for value in old["H3_coefficients_v"]]
        self.budget()
        f = self.field
        source_rows = self.shared_monomials()
        C = fmpz_mat([[int(value) for value in entries] for entries in scalars["primitive_integer_matrix"]])
        assert C.nrows() == 14 and C.ncols() == 112
        row_scales = [fmpq(int(a), int(b))/f.lam**(i % 7)
                      for i, (a, b) in enumerate(scalars["rational_row_scales"])]
        denominator = 1
        for value in row_scales:
            denominator = math.lcm(denominator, int(value.denom()))
        multipliers = []
        for value in row_scales:
            scaled = value*denominator
            assert scaled.denom() == 1
            multipliers.append(scaled.numer())
        kappas = [f.zero]
        for first in range(1, count+1, 16):
            self.budget()
            last = min(count+1, first+16)
            source = fmpz_mat([values[CYC*(first-1):CYC*(last-1)] for values in source_rows])
            target = C*source
            for n in range(first, last):
                offset, vector = CYC*(n-first), []
                for i in range(14):
                    cyclic = [0]*41
                    for r in range(CYC):
                        cyclic[(r+10*n) % 41] += int(target[i, offset+r])
                    reduced = [value-cyclic[40] for value in cyclic[:40]]+[0]
                    assert all(reduced[r] == reduced[41-r] for r in range(1, 21)), (row["candidate_index"], n, i)
                    polynomial = fmpz_poly([reduced[0]])
                    for r in range(1, 21):
                        polynomial += f.chebyshev[r]*reduced[r]
                    polynomial %= f.gt
                    vector.extend([multipliers[i]*polynomial[r] for r in range(20)])
                kappas.append(f.from_vector(vector, fmpq(1, denominator)))
        assert len(kappas) == count+1 and kappas[1]
        self.store(name, {"candidate_index": row["candidate_index"], "map_degree": row["map_degree"],
            "H3_bound": count, "normalized_R_bound": count-1, "new_scalar_stage_sha256": scalar_sha,
            "H3_coefficients_v": [f.encode(value) for value in kappas],
            "ordinary_common_denominator_D": str(denominator),
            "all_14_coordinate_involutions_verified_at_each_exponent": True,
            "involution_checks": 14*count, "actual_cusp_ramification_e": 1,
            "actual_kappa_nonzero": True, "qY_shift_applied_exactly_once": True,
            "c1_phase_applied_a_second_time": False, "real_descent_isogeny_applied": False,
            "H3_coefficients_after_required_bound_generated": False,
            "shared_R774_cubic_monomials_recomputed": False, "old_f4_H3_consumed": False,
            "kappa_algebraic_inverse_computed": False})
        return self.cached(name), kappas

    def one_map(self, row):
        prefix = self.prefix(row)
        count = row["R793_exact_engineering_bounds"]["complete_Laurent_conditions"]
        final_name = prefix+"-complete-prefix"
        old = self.cached(final_name)
        if old:
            assert old["candidate_index"] == row["candidate_index"] and old["map_degree"] == row["map_degree"]
            assert old["normalized_R_bound"] == count-1 and old["H3_bound"] == count
            for item in old["stages"]:
                path = self.out/item["file"]
                assert Path(item["file"]).name == item["file"]
                assert path.stat().st_size == item["bytes"] and sha(path) == item["sha256"]
            return file_spec(self.path(final_name))
        scalars = self.new_scalars(row)
        inputs, kappas = self.real_inputs(row, scalars)
        f, kappa = self.field, kappas[1]
        input_path = self.path(prefix+"-original-real-H3-input")
        initial_name = prefix+"-inverse-free-Laurent-000"
        initial = self.cached(initial_name)
        if initial is None:
            self.budget()
            k2 = f.multiply(kappa, kappa)
            k4 = f.multiply(k2, k2)
            cstar = f.multiply(f.b, k4).scaled(246**6)
            initial = {"candidate_index": row["candidate_index"], "order": 0,
                "input_stage_sha256": sha(input_path), "kappa": f.encode(kappa), "cstar": f.encode(cstar),
                "coefficients": {key: f.encode(f.one) for key in STATE_KEYS},
                "normalized_constant_R0_one": True, "exact_differential_identity_at_this_order": True}
            self.store(initial_name, initial)
        else:
            assert initial["candidate_index"] == row["candidate_index"] and initial["order"] == 0
            assert initial["input_stage_sha256"] == sha(input_path)
            assert initial["kappa"] == f.encode(kappa)
        cstar = f.decode(initial["cstar"])
        values = {key: [f.one] for key in STATE_KEYS}
        prior = self.path(initial_name)
        completed = [self.path(prefix+"-new-L-cubic-scalars"), input_path, prior]
        for n in range(1, count):
            name = prefix+"-inverse-free-Laurent-"+str(n).zfill(3)
            old = self.cached(name)
            if old:
                assert old["candidate_index"] == row["candidate_index"] and old["order"] == n
                assert old["previous_stage_sha256"] == sha(prior)
                assert old["exact_differential_identity_at_this_order"] is True
                for key in STATE_KEYS:
                    values[key].append(f.decode(old["coefficients"][key]))
                prior = self.path(name)
                completed.append(prior)
                continue
            self.budget()
            kp = kappa if n == 1 else f.multiply(values["kappa_power"][-1], kappa)
            a = kappas[n+1] if n == 1 else f.multiply(kappas[n+1], values["kappa_power"][n-1])
            values["Atilde"].append(a)
            r2_0 = f.square_convolution(values["R"], n)
            w2_0 = f.square_convolution(values["W"], n)
            u_0 = r2_0-(cstar if n == 2 else f.zero)
            u2_0 = u_0.scaled(2)+f.square_convolution(values["U"], n)
            left_0 = w2_0+f.convolution(values["W2"], values["W"], n, 1, n)
            right_0 = u2_0+f.convolution(values["Atilde"], values["U2"], n, 1, n+1)
            rn = (left_0-right_0).scaled(fmpq(1, 3*n+1))
            wn = rn.scaled(1-n)
            assert left_0+wn.scaled(3) == right_0+rn.scaled(4)
            current = {"R": rn, "W": wn, "R2": r2_0+rn.scaled(2),
                "W2": w2_0+wn.scaled(2), "U": u_0+rn.scaled(2),
                "U2": u2_0+rn.scaled(4), "kappa_power": kp}
            for key, value in current.items():
                values[key].append(value)
            current["Atilde"] = a
            prior = self.store(name, {"candidate_index": row["candidate_index"], "order": n,
                "previous_stage_sha256": sha(prior),
                "coefficients": {key: f.encode(value) for key, value in current.items()},
                "recurrence_divisor": 3*n+1, "exact_differential_identity_at_this_order": True,
                "R_coefficient_size": f.metrics(rn), "kappa_algebraic_inverse_computed": False,
                "ordinary_nonzero_integer_division_only": True})
            completed.append(prior)
        self.store(final_name, {"candidate_index": row["candidate_index"], "map_degree": row["map_degree"],
            "source_indices": row["source_indices"], "original_Hom_integer_column": row["original_Hom_integer_column"],
            "ordinary_power": row["R793_exact_engineering_bounds"]["ordinary_section_power"],
            "complete_Laurent_conditions": count, "Laurent_exponents": [-1, count-2],
            "normalized_R_bound": count-1, "H3_bound": count, "actual_cusp_ramification_e": 1,
            "actual_kappa_nonzero": True, "coefficient_field_dimension_over_Q": 280,
            "all_original_real_tangent_phases_verified": True,
            "all_recurrence_coefficients_verified_exactly": True,
            "algebraic_kappa_inverse_computed": False,
            "clear_original_relation": "246^3*kappa^(n+2)*A_n+sum_(j=0)^(n+1)kappa^j*R_(n-j+1)*B_j=0, n=-1..N-2",
            "required_relation_rows_over_L": 20*count,
            "actual_relation_matrix_rational_map_polar_divisor_eta_or_height_computed": False,
            "stages": [file_spec(path) for path in completed]})
        return file_spec(self.path(final_name))

    def run(self):
        final = self.out/FINAL
        if final.exists():
            cert = read(final)
            assert cert["complete"] is True and cert["configuration"] == self.tag
            inventory = cert["stage_manifest"]
            assert sha(self.out/inventory["file"]) == inventory["sha256"]
            for row in read(self.out/inventory["file"])["files"]:
                path = self.out/row["file"]
                assert Path(row["file"]).name == row["file"]
                assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
        else:
            summaries = [self.one_map(row) for row in self.maps]
            inventory = self.store("R797-Laurent-stages-manifest", {"files": [file_spec(path)
                for path in sorted(self.out.glob("R797-*.json.gz"))
                if path.name != "R797-Laurent-stages-manifest.json.gz"]})
            cert = {"result": RESULT, "complete": True, "configuration": self.tag, "p": 41,
                "selected_candidate_indices": [row[0] for row in TARGETS],
                "selected_map_degrees": [str(row[2]) for row in TARGETS],
                "complete_Laurent_condition_counts": [row[4] for row in TARGETS],
                "normalized_R_bounds": [row[4]-1 for row in TARGETS],
                "H3_bounds": [row[4] for row in TARGETS], "completed_map_count": 5,
                "coefficient_field_dimension_over_Q": 280,
                "all_actual_original_kappas_nonzero": True, "all_actual_cusp_orders_one": True,
                "all_original_real_tangent_phases_verified": True,
                "all_recurrence_coefficients_verified_exactly": True,
                "old_f4_H3_or_Laurent_recomputed": False,
                "old_newform_Fourier_Hodge_products_periods_or_Hom_recomputed": False,
                "coefficients_after_individual_required_bounds_generated": False,
                "algebraic_kappa_inverse_computed": False,
                "second_c1_phase_or_real_descent_isogeny_applied": False,
                "actual_relation_matrix_rational_map_polar_divisor_eta_or_height_computed": False,
                "map_prefix_certificates": summaries, "stage_manifest": file_spec(inventory),
                "seconds": time.monotonic()-self.started}
            save(final, cert)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(final), "completed_map_count": 5,
            "actual_relation_matrix_rational_map_polar_divisor_eta_or_height_computed": False})
        return 0


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "method", "cusp-proof", "recurrence-proof", "laurent-core", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    try:
        return Job(args).run()
    except BaseException as error:
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error),
            "completed_map_and_order_stages_preserved": True})
        raise


if __name__ == "__main__":
    sys.exit(main())
