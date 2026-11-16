#!/usr/bin/env python3
"""Original two-endpoint reference ideals and norm frames.

All new arithmetic runs only in the original public repository Actions.
Completed R917 orders, R923 target values and R879 exact sections are sources.
"""
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
import traceback
from flint import nmod_mat

RESULT = "R927-original-two-endpoint-reference-ideal-and-norm-frames"
FINAL = "p41-original-two-endpoint-reference-norm-frames-certificate.json"
PREFIX = "R927-reference-"
CURRENT = PREFIX + "current.json.gz"
INVENTORY = PREFIX + "stage-manifest.json.gz"
PRIME, ZETA, SROOT = 1000000753, 549966761, 99932770
DIM, NORMAL, CAP = 8, 272, 9
EPS = [0] + [1]*144 + [2]*127
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
META = ("public-actions-input.json", "run-receipt.json", "core-receipt.json")
SOURCES = ("R923", "R917", "R914", "R879", "R872")
PROOFS = ("R927", "R912", "R923", "R879", "R876", "R872")
HELPER_SHA = "c728c8e06cef3dfbe4d33f3a988cbbc1c3012909d67b4684d941effdec67033d"
H64 = re.compile(r"[0-9a-f]{64}")
DEFINITIONS = {
    "R923": ("R923-original-two-endpoint-target-normal-coordinates",
        "4aef4b448338f62216d3ce44135ace89f83c5be966acb6f90dc47adaed4d334c"),
    "R917": ("R917-original-two-endpoint-normal-orders",
        "f0e321a19ef6dbd259e88de1b670f514b0f9ed0df5b24659a9f787978b8fd743"),
    "R914": ("R914-original-full-V1-involution-and-P1-local-jets",
        "c7dded45af13c7cd37b9c5261d917c2e81d3c179debe963296bbd8caf746e004"),
    "R879": ("R879-original-reference-pole254-pencil",
        "a8573c2a0dfd830cd3cd41dda0858fa108dbcfe0e0fc1ad1d4f78a1b95a2bf33"),
    "R872": ("R872-original-P0-jets-and-fixed-Picard-RR-spaces",
        "0e5897512a2f45baaed9cd1b6b2badcb6bf6ee2b100fcd45db871ad9f6db1874"),
}
STRATEGY = {
    "scope": "original_reference_only_two_endpoint_ideal_coordinates_and_Norm_frames",
    "original_auxiliary_prime": PRIME, "original_zeta_root": ZETA, "original_s_root": SROOT,
    "complete_endpoint_rank": DIM, "normal_target_dimension": NORMAL,
    "endpoint_parameters": ["rho0=z-z0", "rho1=iota^*rho0=z-2*beta72-z0"],
    "reference_exact_function": "v0=f/u=-g/b; original ug+bf=0",
    "original_reference_pole_order": 254,
    "old_numerator_P0_order": 18, "old_denominator_P0_order": 272,
    "original_V1_scale_already_in_source": 6724, "new_scale_applied": 1,
    "target_P0_ideal_generators": "U-z0 and gamma_i-e_(i+1)(P0)/tau for i1..144",
    "normal_ring_generation": "all degree2 normal basis rows are original V1 products",
    "complete_P0_primary_summand": "annihilator of eighth power of pulled-back maximal ideal",
    "idempotent_lift": "e -> 3e^2-2e^3; entire two summands retained",
    "working_rho_precision_cap": CAP,
    "target_P0_parameter_norm_order_bound": 8,
    "reference_regular_complement": "(f-eta*g)/(u+eta*b), eta0..8 with entire block unit",
    "common_reference_frame_parameter_candidates": list(range(17)),
    "original_nine_parameters": list(range(9)),
    "original_P0_pole_summand_relative_matrices": "0 and lambda^-1*identity modulo rho",
    "reference_norm_leading": "lambda^r*U272^(-r)*LC(Norm(qrho0))^(-254)*C_complement(lambda)",
    "reference_norm_order": "-254*ord(Norm(qrho0))",
    "original_t_frame": "rho-leading*c_epsilon^(-rho-order), c1=-c0",
    "reference_generic_frame_and_both_dual7_determinants_retained": True,
    "all_factors_and_nilpotents_preserved": True,
    "zero_truncation": "NeedPrecision, never zero function or inactive",
    "five_target_sources": {"R903": None, "R907": None},
    "new_values_are_at_original_auxiliary_place_not_expanded_char0": True,
    "old_normal_orders_target_coordinates_jets_RR_or_reference_solution_recomputed": False,
    "only_budget_and_transport_paths_excluded_from_identity": True,
}


class BudgetStop(RuntimeError):
    pass


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            h.update(block)
    return h.hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                    ensure_ascii=False).encode()).hexdigest()


def plain(value):
    answer = {k: value[k] for k in ("file", "bytes", "sha256")}
    assert Path(answer["file"]).name == answer["file"] and "\\" not in answer["file"]
    assert isinstance(answer["bytes"], int) and answer["bytes"] >= 0
    assert H64.fullmatch(answer["sha256"])
    return answer


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def read(path):
    path = Path(path)
    with (gzip.open(path, "rt", encoding="utf-8") if path.name.endswith(".gz")
          else path.open("r", encoding="utf-8")) as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    data = (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False) + "\n").encode()
    with tmp.open("wb") as raw:
        if path.name.endswith(".gz"):
            with gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0, compresslevel=2) as stream:
                stream.write(data)
        else:
            raw.write(data)
        raw.flush()
        os.fsync(raw.fileno())
    tmp.replace(path)


def identity(value):
    return {k: str(value[k]) for k in BASE}


def source_identity(value):
    return {**identity(value), "configuration_sha256": value["configuration_sha256"],
        "selected_files_sha256": value["selected_files_sha256"],
        "selected_file_count": value["selected_file_count"],
        "certificate": plain(value["certificate"])}


def expected_tag(item):
    return {"result": RESULT, "source_sha256": item["core_sha256"],
        "helper_sha256": item["helper_sha256"], "p": 41, "prime": PRIME,
        "python_flint": "0.9.0", "method_sha256": item["method_sha256"],
        "proofs_sha256": {k: item["proofs"][k]["sha256"] for k in PROOFS},
        "sources": {k: source_identity(item["sources"][k]) for k in SOURCES},
        "inputs": item["inputs"], "strategy": STRATEGY}


class Source:
    def __init__(self, label, item):
        self.label, self.item, self.path = label, item, Path(item["directory"])
        assert (item["result"], item["core_sha256"]) == DEFINITIONS[label]
        self.files = {name: plain(v) for name, v in item["files"].items()}
        assert len(self.files) == item["selected_file_count"]
        assert fingerprint(self.files) == item["selected_files_sha256"]
        for name, row in self.files.items():
            assert name == row["file"] and spec(self.path/name) == row, (label, name)
        manifest = self.get("full-outputs-manifest.json")
        assert self.files["full-outputs-manifest.json"]["sha256"] == item["manifest_sha256"]
        assert manifest["result"] == item["result"]
        entries = {r["file"]: plain(r) for r in manifest["files"]}
        assert len(entries) == len(manifest["files"]) == item["manifest_file_count"]
        for name, row in self.files.items():
            if name != "full-outputs-manifest.json":
                assert entries[name] == row, (label, name)
        initial, run, core = (self.get(name) for name in META)
        assert initial["source_commit"] == run["source_commit"] == item["source_commit"]
        assert str(run["workflow_run_id"]) == str(item["run_id"])
        recorded = initial["core_sha256"] if "core_sha256" in initial else initial["job"]["core_sha256"]
        assert recorded == core["source_sha256"] == item["core_sha256"]
        if run.get("core_receipt_sha256") is not None:
            assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert core["complete"] is True
        self.cert = self.get(item["certificate"]["file"])
        assert self.cert["complete"] is True and self.cert["result"] == item["result"]
        assert self.files[item["certificate"]["file"]] == plain(item["certificate"])
        assert core["certificate_sha256"] == item["certificate"]["sha256"]
        self.tag = self.cert["configuration"]
        assert fingerprint(self.tag) == item["configuration_sha256"]
        assert self.tag.get("source_sha256", self.tag.get("core_sha256")) == item["core_sha256"]

    def get(self, name):
        assert name in self.files, (self.label, name)
        return read(self.path/name)

    def stage(self, row):
        assert self.files[row["file"]] == plain(row)
        value = self.get(row["file"])
        assert value["complete"] is True and value["configuration"] == self.tag
        assert value.get("result", self.tag["result"]) == self.item["result"]
        return value


def vadd(R, a, b):
    return [R.add(x, y) for x, y in zip(a, b)]


def vsub(R, a, b):
    return [R.sub(x, y) for x, y in zip(a, b)]


def vscale(R, a, scalar):
    return [R.scale(x, scalar) for x in a]


def vpack(R, a):
    return [R.pack(x) for x in a]


def mpack(R, a):
    return [[R.pack(x) for x in row] for row in a]


def mread(R, a):
    return [[R.element(x) for x in row] for row in a]


def midentity(R, n):
    return [[R.element(int(i == j)) for j in range(n)] for i in range(n)]


def mvec(R, a, b):
    return [sum_poly(R, (R.mul(x, y) for x, y in zip(row, b))) for row in a]


def sum_poly(R, xs):
    out = R.zero
    for x in xs:
        out = R.add(out, x)
    return out


def mmul(R, a, b):
    if not a:
        return []
    n, k = len(a), len(b)
    m = len(b[0]) if b else 0
    assert all(len(row) == k for row in a) and all(len(row) == m for row in b)
    out = [[R.zero for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(k):
            if a[i][j] == R.zero:
                continue
            for z in range(m):
                out[i][z] = R.add(out[i][z], R.mul(a[i][j], b[j][z]))
    return out


def madd(R, a, b):
    return [[R.add(x, y) for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def mscale(R, a, scalar):
    return [[R.scale(x, scalar) for x in row] for row in a]


def multiplication_matrix(order, vector):
    R = order.R
    return [[sum_poly(R, (R.mul(vector[r], order.table[r][j][i]) for r in range(DIM)))
             for j in range(DIM)] for i in range(DIM)]


def minverse_unit(H, R, a, budget):
    n = len(a)
    assert all(len(row) == n for row in a)
    if not n:
        return []
    inv0, _ = H.inverse([[int(x[0]) for x in row] for row in a])
    out = [[R.element(x) for x in row] for row in inv0]
    I = midentity(R, n)
    precision = 1
    while precision < R.N:
        budget()
        product = mmul(R, a, out)
        correction = [[R.sub(R.scale(I[i][j], 2), product[i][j])
                       for j in range(n)] for i in range(n)]
        out = mmul(R, out, correction)
        precision *= 2
    assert mmul(R, a, out) == I and mmul(R, out, a) == I
    return out


def crop_order(H, data, N):
    assert 1 <= N <= data["absolute_rho_precision"]
    R = H.SeriesRing(N)
    return H.Order(N, [[[R.element(x) for x in row] for row in plane]
                     for plane in data["multiplication_structure_coefficients"]],
        [R.element(x) for x in data["one_coordinates"]],
        [[H.lp_unpack(x) for x in row] for row in data["basis_in_primitive_Theta_powers"]],
        [[H.lp_unpack(x) for x in row] for row in data["primitive_Theta_powers_in_basis"]],
        data["total_index_length"], data["basis_determinant_unit_mod_prime"],
        data["initial_Theta_rho_power"])


def constant_matrix(a):
    return [[int(x[0]) for x in row] for row in a]


def columns(matrix):
    return [list(x) for x in zip(*matrix)] if matrix and matrix[0] else []


def from_columns(cols, n=DIM):
    return [[int(c[i]) % PRIME for c in cols] for i in range(n)]


def column_basis(H, cols):
    matrix = from_columns(cols)
    if not cols:
        return matrix, []
    _, pivots = H.rref(matrix, len(cols))
    return from_columns([cols[i] for i in pivots]), pivots


def constant_multiply(table, a, b):
    out = [0]*DIM
    for i in range(DIM):
        if a[i]:
            for j in range(DIM):
                if b[j]:
                    v = a[i]*b[j] % PRIME
                    for k in range(DIM):
                        out[k] = (out[k] + v*table[i][j][k]) % PRIME
    return out


def characteristic(R, a):
    n = len(a)
    if not n:
        return [R.one]
    old = characteristic(R, [row[1:] for row in a[1:]])
    q = [R.one, R.neg(a[0][0])]
    v = [a[i][0] for i in range(1, n)]
    tail = [row[1:] for row in a[1:]]
    for k in range(n-1):
        q.append(R.neg(sum_poly(R, (R.mul(a[0][j+1], v[j]) for j in range(n-1)))))
        if k+1 < n-1:
            v = mvec(R, tail, v)
    return [sum_poly(R, (R.mul(q[k-j], old[j])
                        for j in range(max(0, k-n), min(k, n-1)+1))) for k in range(n+1)]


def eval_poly(coefficients, x):
    value = 0
    for c in reversed(coefficients):
        value = (value*x + int(c)) % PRIME
    return value


def determinant_constant(a):
    if not a:
        return 1
    return int(nmod_mat(a, PRIME).det())



class Job:
    def __init__(self, args):
        self.started = time.monotonic()
        self.deadline = self.started + 60*float(args.budget_minutes)
        self.item = read(args.config)
        self.out = Path(args.out)
        self.out.mkdir(parents=True, exist_ok=True)
        item = self.item
        assert item["result"] == RESULT and item["p"] == 41
        assert item["producer_inputs_pending"] is False
        assert item["future_target_sources"] == {"R903": None, "R907": None}
        assert sha(__file__) == item["core_sha256"] and item["helper_sha256"] == HELPER_SHA
        topic = Path(item["topic_directory"])
        assert sha(topic/item["method"]) == item["method_sha256"]
        assert set(item["proofs"]) == set(PROOFS)
        for value in item["proofs"].values():
            assert sha(topic/value["file"]) == value["sha256"]
        hp = Path(__file__).resolve().parent/item["helper"]
        assert hp.name == "R917_endpoint_order_arithmetic.py" and sha(hp) == HELPER_SHA
        loader = importlib.util.spec_from_file_location("R927_source_bound_R917_arithmetic", hp)
        self.H = importlib.util.module_from_spec(loader)
        loader.loader.exec_module(self.H)
        assert self.H.P == PRIME and self.H.D == DIM
        assert set(item["sources"]) == set(SOURCES)
        self.sources = {k: Source(k,item["sources"][k]) for k in SOURCES}
        self.tag = expected_tag(item)
        self.inputs = item["inputs"]
        self.refs, self.ready, self.endpoints, self.endpoint_stops = {}, {}, {}, {}
        self.active, self.current, self.contexts = None, None, {}
        self.checkpoint()
        self.prepare()

    def budget(self):
        if time.monotonic() >= self.deadline:
            raise BudgetStop("Actual mathematical budget reached; complete atomic stages retained")

    def input(self, name):
        row = self.inputs[name]
        return self.sources[row["source_group"]].stage(row)

    def eref(self, epsilon, name):
        return self.inputs["endpoints"][str(epsilon)][name]

    def endpoint_input(self, epsilon, name):
        row = self.eref(epsilon,name)
        return self.sources[row["source_group"]].stage(row)

    def path(self, name):
        return self.out/(PREFIX+name+".json.gz")

    def old(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["result"] == RESULT and value["configuration"] == self.tag
        assert value["complete"] is True
        self.refs[name] = spec(path)
        return value

    def stage(self, name, produce):
        value = self.old(name)
        if value is not None:
            return value
        self.budget()
        self.active = name
        self.checkpoint()
        value = produce()
        assert not {"result","configuration","complete"} & set(value)
        save(self.path(name), {"result":RESULT,"configuration":self.tag,"complete":True,**value})
        self.refs[name] = spec(self.path(name))
        self.active = None
        self.checkpoint()
        print("R927_REFERENCE_STAGE="+json.dumps(self.refs[name],sort_keys=True),flush=True)
        return read(self.path(name))

    def checkpoint(self, reason=None):
        value = {"result":RESULT,"configuration":self.tag,"complete":False,
            "active_stage":self.active,"prepared_endpoint_records":self.ready,
            "completed_endpoint_certificates":self.endpoints,
            "endpoint_stops":self.endpoint_stops,"completed_stage_refs":self.refs,
            "last_stop":reason,"seconds":time.monotonic()-self.started}
        save(self.out/CURRENT,value)
        self.current = spec(self.out/CURRENT)

    def prepare(self):
        self.reference = self.input("reference_function")
        self.u_source, self.b_source = self.input("anchor_u"), self.input("anchor_b")
        self.chi_source = self.input("fixed_chi_divisor")
        self.old_point = self.input("P0_V1_jets")
        self.point_check = self.input("P1_point_check")
        reference = self.reference
        assert self.sources["R923"].cert["actual_original_two_endpoint_target_normal_coordinates_certified"] is True
        assert self.sources["R917"].cert["actual_original_two_endpoint_normal_orders_certified"] is True
        assert identity(self.sources["R923"].cert["source_identities"]["R917"]) == identity(self.item["sources"]["R917"])
        assert self.sources["R914"].cert["actual_full146_exact_geometric_iota_certified"] is True
        assert identity(self.sources["R917"].cert["source_identities"]["R914"]) == identity(self.item["sources"]["R914"])
        assert self.sources["R879"].cert["actual_reference_pole254_function_certified"] is True
        assert self.sources["R879"].cert["actual_reference_basepoint_free_pencil_certified"] is True
        assert plain(self.sources["R879"].cert["reference_function_and_pencil"]) == plain(self.inputs["reference_function"])
        assert identity(reference["source_R872"]) == identity(self.item["sources"]["R872"])
        for key in ("anchor_u","anchor_b"):
            assert plain(reference["source_"+key]) == plain(self.inputs[key])
        assert plain(self.sources["R872"].cert["anchor_u"]) == plain(self.inputs["anchor_u"])
        assert plain(self.sources["R872"].cert["accepted_anchor_b"]) == plain(self.inputs["anchor_b"])
        assert plain(self.sources["R872"].cert["fixed_chi_divisor_and_principal_function"]) == plain(self.inputs["fixed_chi_divisor"])
        assert self.chi_source["D_chi_effective_and_avoids_original_P0"] is True
        assert self.chi_source["actual_complete_fixed_chi_RR_space_certified"] is True
        assert plain(self.chi_source["source_complete_W_Dchi"]) == plain(reference["source_paired_kernel"])
        assert plain(self.sources["R872"].cert["complete_fixed_chi_418_kernel"]) == plain(reference["source_paired_kernel"])
        assert reference["prime"] == PRIME and reference["original_zeta_root"] == ZETA
        assert reference["chosen_local_parameter"] == "z_minus_z0"
        assert reference["actual_reference_pole254_function_certified"] is True
        assert reference["actual_reference_basepoint_free_pencil_certified"] is True
        assert reference["exact_function_definition"]["global_certificate"] == "f/u=-g/b from the full old syzygy"
        assert reference["exact_function_definition"]["old_global_syzygy_inherited_by_exact_linear_combination"] is True
        assert reference["exact_function_definition"]["extra_82_or_tau_scale_applied"] is False
        assert reference["exact_pole_divisor"] == {"point":"original_P0","multiplicity":254,"all_other_poles_excluded":True}
        assert reference["numerator_first19_local_coefficients_mod_prime"] == [0]*18+[1]
        assert reference["normal_basis_degrees"] == EPS and reference["normal_basis_rank"] == NORMAL
        self.V2 = [(i,a) for i in range(NORMAL) for a in range(3-EPS[i])]
        assert reference["V2_basis"] == [{"normal_basis_row":i,"power_of_z":a} for i,a in self.V2]
        assert len(self.V2) == 418
        self.U272 = int(reference["denominator_order272_unit_mod_prime"])
        assert 0 < self.U272 < PRIME
        assert self.u_source["order272_is_exact"] is True
        assert self.U272 == self.u_source["exact_order272_unit"]
        assert self.b_source["trial"] == 1
        for value in (self.u_source,self.b_source):
            assert value["normal_integer_scale_applied_again"] is False
            assert value["vanishes_at_original_P0_to_order_at_least272"] is True
            assert len(value["V2_coordinates_mod_prime"]) == 418
        assert reference["denominator_V2_coordinates_mod_prime"] == self.u_source["V2_coordinates_mod_prime"]
        self.polynomials = {}
        for name,field,vector in (
            ("f","numerator_normal_polynomial_mod_prime","numerator_V2_coordinates_mod_prime"),
            ("g","paired_normal_polynomial_mod_prime","paired_V2_coordinates_mod_prime"),
            ("u","denominator_normal_polynomial_mod_prime","denominator_V2_coordinates_mod_prime")):
            raw = reference[field]
            assert len(raw) == 3 and all(len(row) == NORMAL for row in raw)
            assert [raw[a][i] for i,a in self.V2] == reference[vector]
            assert all(raw[a][i] == 0 for i in range(NORMAL) for a in range(3-EPS[i],3))
            self.polynomials[name] = raw
        b = [[0]*NORMAL for _ in range(3)]
        for x,(i,a) in zip(self.b_source["V2_coordinates_mod_prime"],self.V2):
            b[a][i] = int(x)
        self.polynomials["b"] = b
        point = self.old_point
        assert point["prime"] == PRIME and point["matrix_shape"] == [273,146]
        assert point["local_parameter"] == "rho0=z-z0"
        assert point["function_order"] == "e0/tau=1,e1/tau=z-beta72,ei/tau=beta_(i-1) for i=2..145"
        assert point["old273_Hensel_coefficients_recomputed"] is False
        assert point["extra_integer_scale_applied"] is False
        assert len(point["matrix_mod_prime"]) == 273 and all(len(r)==146 for r in point["matrix_mod_prime"])
        self.point_row = [int(x) for x in point["matrix_mod_prime"][0]]
        assert self.point_row[0] == 1
        self.z0 = (self.point_row[1]+self.point_row[73]) % PRIME
        assert self.point_check["both_original146_zero_order_rows_match_completed_P0_and_P1_values"] is True
        assert self.point_check["exact_K_point_row_transport_multiplied_back"] is True
        assert plain(point["source_original_normal_free_basis"]) == plain(self.point_check["source_original_free_basis"])
        self.source_endpoints = {}
        for epsilon in (0,1):
            ec = self.endpoint_input(epsilon,"target_certificate")
            op = self.endpoint_input(epsilon,"target_operators")
            order_cert = self.endpoint_input(epsilon,"order_certificate")
            normal = self.endpoint_input(epsilon,"normal_order")
            frame = self.endpoint_input(epsilon,"frame")
            assert ec["endpoint"] == epsilon
            for key in ("all272_original_target_normal_coordinates_computed",
                        "all272_by8_series_original_equations_verified",
                        "complete_length8_endpoint_algebra_and_nilpotents_retained",
                        "original_basis_parameter_nu_and_dual7_frames_preserved"):
                assert ec[key] is True
            assert plain(self.sources["R923"].cert["completed_endpoint_certificates"][str(epsilon)]) == plain(self.eref(epsilon,"target_certificate"))
            assert plain(self.sources["R917"].cert["completed_endpoint_certificates"][str(epsilon)]) == plain(self.eref(epsilon,"order_certificate"))
            assert plain(ec["target_operators"]) == plain(self.eref(epsilon,"target_operators"))
            assert plain(ec["source_original_normal_order"]) == plain(self.eref(epsilon,"normal_order"))
            assert plain(ec["source_original_order_certificate"]) == plain(self.eref(epsilon,"order_certificate"))
            assert plain(ec["source_original_primitive_and_t_frames"]) == plain(self.eref(epsilon,"frame"))
            assert order_cert["normal_order_certified"] is True and order_cert["full_length8_special_fibre_preserved"] is True
            assert order_cert["actual_final_discriminant_order"] == 4
            assert plain(order_cert["complete_normal_order"]) == plain(self.eref(epsilon,"normal_order"))
            assert plain(order_cert["primitive_and_t_frames"]) == plain(self.eref(epsilon,"frame"))
            assert normal["order"]["rank"] == DIM and normal["order"]["all_factors_and_nilpotents_retained"] is True
            assert frame["local_parameter"] == STRATEGY["endpoint_parameters"][epsilon]
            assert frame["both_determinant_factors_required_under_dual7"] is True
            assert frame["original_nu"]["iota_fixes_nu"] is True
            assert frame["original_dual7"]["frozen_direction"] == "Nm_pi_t(pi_s^*I)"
            assert frame["original_dual7"]["determinant_numerator_and_denominator_both_transported"] is True
            assert op["endpoint"] == epsilon and op["complete_rank8_multiplication_operators"] is True
            source_N = int(ec["actual_target_normal_coordinate_precision"])
            N = min(CAP,source_N,normal["order"]["absolute_rho_precision"],op["absolute_rho_precision"])
            assert N >= 1
            order = crop_order(self.H,normal["order"],N)
            R = order.R
            U = [R.element(x) for x in op["target_U_coordinates"]]
            assert len(U) == DIM
            gamma = []
            blocks = self.eref(epsilon,"target_blocks")
            assert [plain(x) for x in ec["complete_target_normal_coordinate_blocks"]] == [plain(x) for x in blocks]
            for first,row in enumerate(blocks):
                value = self.sources["R923"].stage(row)
                assert value["endpoint"] == epsilon
                raw = value["normal_values_in_original_endpoint_order_mod_prime"]
                assert len(raw) <= 16 and all(len(x)==DIM for x in raw)
                assert value["normal_columns"] == [len(gamma),len(gamma)+len(raw)]
                assert value["absolute_rho_precision"] == source_N
                for vector in raw:
                    assert all(len(x) >= N for x in vector)
                    gamma.append([R.element(x) for x in vector])
            assert len(gamma) == NORMAL and gamma[0] == order.one
            self.contexts[epsilon] = {"order":order,"R":R,"U":U,"gamma":gamma,
                "frame":frame,"source_precision":source_N,"N":N}
            self.source_endpoints[epsilon] = ec
        assert (self.contexts[0]["frame"]["original_t_over_rho_mod_prime"]+
                self.contexts[1]["frame"]["original_t_over_rho_mod_prime"]) % PRIME == 0
        assert self.contexts[0]["frame"]["original_dual7"] == self.contexts[1]["frame"]["original_dual7"]
        self.stage("source-audit",lambda:{
            "prime":PRIME,"original_zeta_root":ZETA,"original_s_root":SROOT,
            "source_identities":{k:source_identity(self.item["sources"][k]) for k in SOURCES},
            "inputs":self.inputs,"original_reference_function":reference["exact_function_definition"],
            "original_reference_t_frame":reference["original_t_frame"],
            "original_U272_mod_prime":self.U272,
            "original_tau_normalized_P0_V1_row_mod_prime":self.point_row,
            "original_z0_mod_prime":self.z0,
            "actual_endpoint_input_precisions":{str(e):self.contexts[e]["source_precision"] for e in (0,1)},
            "actual_endpoint_working_precisions":{str(e):self.contexts[e]["N"] for e in (0,1)},
            "original_dual7":self.contexts[0]["frame"]["original_dual7"],
            "new_target_normal_evaluations_or_old_point_jets_recomputed":False,
            "five_original_target_pencil_sources":{"R903":None,"R907":None},
            "new_arithmetic_only_at_the_original_auxiliary_place":True,
            "characteristic_zero_reference_definition_preserved_not_expanded":True})

    def evaluate_normal_polynomial(self, epsilon, raw):
        ctx = self.contexts[epsilon]
        order,R,U,gamma = ctx["order"],ctx["R"],ctx["U"],ctx["gamma"]
        out = [R.zero]*DIM
        for degree in (2,1,0):
            out = order.multiply(U,out)
            coefficients = raw[degree]
            value = [sum_poly(R,(R.scale(gamma[i][k],coefficients[i])
                                for i in range(NORMAL) if coefficients[i]))
                     for k in range(DIM)]
            out = vadd(R,out,value)
        return out

    def functions(self, epsilon):
        ctx = self.contexts[epsilon]
        order,R = ctx["order"],ctx["R"]
        def produce():
            values = {key:self.evaluate_normal_polynomial(epsilon,raw)
                      for key,raw in self.polynomials.items()}
            assert vadd(R,order.multiply(values["u"],values["g"]),
                          order.multiply(values["b"],values["f"])) == [R.zero]*DIM
            qrho = vsub(R,ctx["U"],vscale(R,order.one,self.z0))
            return {"endpoint":epsilon,"absolute_rho_precision":R.N,
                "source_reference_function":self.inputs["reference_function"],
                "source_anchor_u":self.inputs["anchor_u"],"source_anchor_b":self.inputs["anchor_b"],
                "source_target_certificate":self.eref(epsilon,"target_certificate"),
                "source_target_blocks":self.eref(epsilon,"target_blocks"),
                "source_original_normal_order":self.eref(epsilon,"normal_order"),
                "original_normal_values":{key:vpack(R,value) for key,value in values.items()},
                "target_pullback_original_rho0_coordinates":vpack(R,qrho),
                "all8_ug_plus_bf_series_coordinates_zero":True,
                "polynomial_order":"power0..2 of original target z, then all272 original normal rows",
                "additional_tau_or_integer_scale_applied":False,
                "original_v0_not_yet_divided_by_u":True}
        return self.stage(f"P{epsilon}-original-reference-normal-functions",produce)

    def residue_summand(self, epsilon):
        ctx = self.contexts[epsilon]
        order,R,gamma,U = ctx["order"],ctx["R"],ctx["gamma"],ctx["U"]
        def produce():
            table = [[[int(x[0]) for x in row] for row in plane] for plane in order.table]
            one = [int(x[0]) for x in order.one]
            generators = [[(int(U[k][0])-self.z0*one[k])%PRIME for k in range(DIM)]]
            labels = [{"original_function":"z-z0"}]
            for i in range(1,145):
                value = self.point_row[i+1]
                generators.append([(int(gamma[i][k][0])-value*one[k])%PRIME for k in range(DIM)])
                labels.append({"original_function":"beta_i-beta_i(P0)","normal_basis_row":i,
                               "original_V1_column":i+1})
            standard = [[int(i==j) for i in range(DIM)] for j in range(DIM)]
            products = [constant_multiply(table,g,e) for g in generators for e in standard]
            I,selected = column_basis(self.H,products)
            previous = columns(I)
            powers = [{"power":1,"basis_mod_prime":I,"selected_generator_products":selected,
                       "dimension":len(previous)}]
            first = previous[:]
            for exponent in range(2,9):
                self.budget()
                new = [constant_multiply(table,x,y) for x in previous for y in first]
                basis,pivots = column_basis(self.H,new)
                powers.append({"power":exponent,"basis_mod_prime":basis,
                    "selected_previous_times_I_columns":pivots,"dimension":len(columns(basis)),
                    "all_product_columns_mod_prime":from_columns(new)})
                previous = columns(basis)
            I8 = from_columns(previous)
            equations = []
            for h in previous:
                multiplication = from_columns([constant_multiply(table,h,e) for e in standard])
                equations.extend(multiplication)
            annihilator = self.H.kernel(equations,DIM)
            ann = annihilator["kernel_basis_mod_prime"]
            r = annihilator["kernel_dimension"]
            combined = [ann[i]+I8[i] for i in range(DIM)]
            assert all(len(row)==DIM for row in combined)
            inverse,det = self.H.inverse(combined)
            coordinates = [sum(inverse[i][j]*one[j] for j in range(DIM))%PRIME for i in range(DIM)]
            e = [sum(combined[i][j]*coordinates[j] for j in range(r))%PRIME for i in range(DIM)]
            ec = [(x-y)%PRIME for x,y in zip(one,e)]
            assert constant_multiply(table,e,e)==e
            assert constant_multiply(table,ec,ec)==ec
            assert constant_multiply(table,e,ec)==[0]*DIM
            assert all(constant_multiply(table,e,h)==[0]*DIM for h in previous)
            assert all(constant_multiply(table,ec,h)==h for h in previous)
            assert all(constant_multiply(table,e,h)==h for h in columns(ann))
            return {"endpoint":epsilon,"source_target_certificate":self.eref(epsilon,"target_certificate"),
                "source_original_P0_V1_row":self.inputs["P0_V1_jets"],
                "source_original_normal_order":self.eref(epsilon,"normal_order"),
                "normal_ring_generator_identity":"beta1..144 are e2..145/tau; remaining beta are original V1 products",
                "source_original_free_basis":self.old_point["source_original_normal_free_basis"],
                "generator_labels":labels,"target_P0_ideal_generators_mod_prime":generators,
                "complete_ideal_power_sequence":powers,"annihilator_of_I8":annihilator,
                "target_P0_block_rank":r,"complement_rank":DIM-r,
                "complete_residue_basis_mod_prime":combined,"complete_residue_basis_inverse_mod_prime":inverse,
                "complete_residue_basis_determinant_mod_prime":det,
                "target_P0_idempotent_mod_prime":e,"complement_idempotent_mod_prime":ec,
                "whole_identity_mod_prime":one,
                "all_complete_ideal_and_annihilator_products_verified":True,
                "all_eight_dimensions_and_nilpotents_retained":True,
                "empty_target_P0_block":r==0,"empty_complement":r==DIM}
        return self.stage(f"P{epsilon}-target-P0-complete-residue-summand",produce)

    def lift_summand(self, epsilon, residue):
        ctx = self.contexts[epsilon]
        order,R = ctx["order"],ctx["R"]
        def produce():
            e = [R.element(x) for x in residue["target_P0_idempotent_mod_prime"]]
            bound,history = 1,[]
            while bound < R.N:
                self.budget()
                e2 = order.multiply(e,e); e3 = order.multiply(e2,e)
                e = vsub(R,vscale(R,e2,3),vscale(R,e3,2))
                bound = min(2*bound,R.N)
                history.append({"guaranteed_precision":bound,"idempotent_coordinates":vpack(R,e)})
            ec = vsub(R,order.one,e)
            assert order.multiply(e,e)==e and order.multiply(ec,ec)==ec
            assert order.multiply(e,ec)==[R.zero]*DIM
            r = residue["target_P0_block_rank"]
            raw = columns(residue["complete_residue_basis_mod_prime"])
            cols = [order.multiply(e if j<r else ec,[R.element(x) for x in row])
                    for j,row in enumerate(raw)]
            change = [[cols[j][i] for j in range(DIM)] for i in range(DIM)]
            inverse = minverse_unit(self.H,R,change,self.budget)
            return {"endpoint":epsilon,"absolute_rho_precision":R.N,
                "source_complete_residue_summand":self.refs[f"P{epsilon}-target-P0-complete-residue-summand"],
                "source_original_normal_order":self.eref(epsilon,"normal_order"),
                "target_P0_block_rank":r,"complement_rank":DIM-r,
                "idempotent_lift_history":history,"target_P0_idempotent":vpack(R,e),
                "complement_idempotent":vpack(R,ec),
                "complete_block_basis_in_original_basis":mpack(R,change),
                "original_basis_in_complete_block_basis":mpack(R,inverse),
                "both_full8_basis_inverse_products_verified":True,
                "full_idempotent_orthogonality_and_sum_one_verified":True,
                "no_factors_or_nilpotents_removed":True}
        return self.stage(f"P{epsilon}-complete-lifted-summand-basis",produce)

    def block_values(self, epsilon, functions, lifted):
        ctx=self.contexts[epsilon]
        order,R=ctx["order"],ctx["R"]
        def produce():
            C = mread(R,lifted["complete_block_basis_in_original_basis"])
            Ci = mread(R,lifted["original_basis_in_complete_block_basis"])
            r = lifted["target_P0_block_rank"]
            values={k:[R.element(x) for x in raw] for k,raw in functions["original_normal_values"].items()}
            values["qrho0"]=[R.element(x) for x in functions["target_pullback_original_rho0_coordinates"]]
            result={}
            for name,value in values.items():
                self.budget()
                old=multiplication_matrix(order,value)
                new=mmul(R,mmul(R,Ci,old),C)
                assert all(new[i][j]==R.zero for i in range(r) for j in range(r,DIM))
                assert all(new[i][j]==R.zero for i in range(r,DIM) for j in range(r))
                result[name]={"target_P0_multiplication":mpack(R,[row[:r] for row in new[:r]]),
                              "complement_multiplication":mpack(R,[row[r:] for row in new[r:]])}
            return {"endpoint":epsilon,"absolute_rho_precision":R.N,
                "target_P0_block_rank":r,"complement_rank":DIM-r,
                "source_functions":self.refs[f"P{epsilon}-original-reference-normal-functions"],
                "source_complete_block_basis":self.refs[f"P{epsilon}-complete-lifted-summand-basis"],
                "complete_block_multiplication_operators":result,
                "all_full8_off_block_coordinates_zero":True,
                "all_original_target_P0_and_complement_factors_preserved":True}
        return self.stage(f"P{epsilon}-complete-reference-block-operators",produce)


    def parameter_norm(self, epsilon, blocks):
        R=self.contexts[epsilon]["R"]
        def produce():
            r=blocks["target_P0_block_rank"]
            raw=blocks["complete_block_multiplication_operators"]["qrho0"]["target_P0_multiplication"]
            M=mread(R,raw)
            assert len(M)==r and all(len(row)==r for row in M)
            norm=R.determinant(M)
            if r==0:
                assert norm==R.one
                m,leading=0,1
            else:
                try:
                    m=R.valuation(norm,f"P{epsilon}: Norm(target rho0 on complete P0 block)")
                except self.H.NeedPrecision:
                    if R.N >= CAP:
                        raise AssertionError("No parameter-norm leading term within the proved degree-eight bound")
                    raise
                assert 1 <= m <= 8
                leading=int(norm[m])
                assert leading
            return {"endpoint":epsilon,"absolute_rho_precision":R.N,
                "source_complete_block_operators":self.refs[f"P{epsilon}-complete-reference-block-operators"],
                "target_P0_block_rank":r,
                "complete_parameter_norm_series":R.pack(norm),
                "actual_parameter_norm_order":m,
                "actual_parameter_norm_leading_mod_prime":leading,
                "original_parameter":"q*(z-z(P0)); target rho0, not source rho_epsilon",
                "order_upper_bound_from_original_target_map_degree":8,
                "all_target_P0_factors_including_ramification_retained":True,
                "empty_block_norm_equals_one":r==0,
                "no_new_original_order272_jet_requested":True}
        return self.stage(f"P{epsilon}-target-P0-parameter-norm-leading",produce)

    def regular_complement(self, epsilon, blocks):
        R=self.contexts[epsilon]["R"]
        def produce():
            rc=blocks["complement_rank"]
            operators=blocks["complete_block_multiplication_operators"]
            def get(key):
                matrix=mread(R,operators[key]["complement_multiplication"])
                assert len(matrix)==rc and all(len(row)==rc for row in matrix)
                return matrix
            Mu,Mb,Mf,Mg=(get(k) for k in ("u","b","f","g"))
            candidates=[]
            eta=None
            for parameter in range(9):
                constant=constant_matrix(madd(R,Mu,mscale(R,Mb,parameter)))
                det=determinant_constant(constant)
                candidates.append({"integer_parameter":parameter,"actual_complete_block_determinant_mod_prime":det})
                if det:
                    eta=parameter
                    break
            assert eta is not None, "The original u,b ideal must be the entire target-complement algebra"
            denominator=madd(R,Mu,mscale(R,Mb,eta))
            numerator=madd(R,Mf,mscale(R,Mg,-eta))
            inverse=minverse_unit(self.H,R,denominator,self.budget)
            value=mmul(R,inverse,numerator)
            assert mmul(R,denominator,value)==numerator
            assert mmul(R,value,denominator)==numerator
            # A characteristic polynomial of the entire block, including all nilpotents.
            S=self.H.SeriesRing(1)
            const=[[S.element(int(x[0])) for x in row] for row in value]
            chi=characteristic(S,const)
            norm_coefficients=[((-1)**k*int(x[0]))%PRIME for k,x in enumerate(chi)]
            assert norm_coefficients[0]==1 and len(norm_coefficients)==rc+1
            I=midentity(S,rc)
            check=mscale(S,I,int(chi[0][0]))
            for coefficient in chi[1:]:
                check=madd(S,mmul(S,check,const),mscale(S,I,int(coefficient[0])))
            assert check==[[S.zero]*rc for _ in range(rc)]
            return {"endpoint":epsilon,"absolute_rho_precision":R.N,
                "source_complete_block_operators":self.refs[f"P{epsilon}-complete-reference-block-operators"],
                "source_original_reference_function":self.inputs["reference_function"],
                "source_original_anchor_b":self.inputs["anchor_b"],
                "complement_rank":rc,"actual_unit_representation_parameter_eta":eta,
                "actual_unit_parameter_scan":candidates,
                "complete_denominator_multiplication":mpack(R,denominator),
                "complete_denominator_inverse":mpack(R,inverse),
                "complete_numerator_multiplication":mpack(R,numerator),
                "complete_reference_multiplication":mpack(R,value),
                "exact_same_function_identity":"v0=(f-eta*g)/(u+eta*b)=f/u=-g/b",
                "both_complete_unit_inverse_products_verified":True,
                "both_complete_quotient_products_verified":True,
                "reference_characteristic_coefficients_descending": [int(x[0]) for x in chi],
                "C_complement_coefficients_ascending_T_mod_prime":norm_coefficients,
                "complete_characteristic_matrix_identity_verified":True,
                "C_complement_zero_parameter_is_one":True,
                "no_nonunit_denominator_or_reduced_quotient_used":True,
                "empty_complement_unit_and_norm_equal_one":rc==0}
        return self.stage(f"P{epsilon}-reference-regular-complement",produce)

    def prepare_endpoint(self, epsilon):
        old=self.old(f"P{epsilon}-prepared-reference-endpoint")
        if old is not None:
            self.ready[str(epsilon)]=self.refs[f"P{epsilon}-prepared-reference-endpoint"]
            return old
        f=self.functions(epsilon)
        residue=self.residue_summand(epsilon)
        lifted=self.lift_summand(epsilon,residue)
        blocks=self.block_values(epsilon,f,lifted)
        norm=self.parameter_norm(epsilon,blocks)
        regular=self.regular_complement(epsilon,blocks)
        def produce():
            r=blocks["target_P0_block_rank"]
            C=regular["C_complement_coefficients_ascending_T_mod_prime"]
            d=[0]*r+C
            assert len(d)<=9 and any(d)
            return {"endpoint":epsilon,"prime":PRIME,"original_zeta_root":ZETA,
                "absolute_rho_precision":self.contexts[epsilon]["N"],
                "source_original_functions":self.refs[f"P{epsilon}-original-reference-normal-functions"],
                "source_complete_residue_summand":self.refs[f"P{epsilon}-target-P0-complete-residue-summand"],
                "source_complete_block_basis":self.refs[f"P{epsilon}-complete-lifted-summand-basis"],
                "source_complete_block_operators":self.refs[f"P{epsilon}-complete-reference-block-operators"],
                "source_parameter_norm":self.refs[f"P{epsilon}-target-P0-parameter-norm-leading"],
                "source_reference_regular_complement":self.refs[f"P{epsilon}-reference-regular-complement"],
                "target_P0_block_rank":r,"complement_rank":DIM-r,
                "actual_parameter_norm_order":norm["actual_parameter_norm_order"],
                "actual_parameter_norm_leading_mod_prime":norm["actual_parameter_norm_leading_mod_prime"],
                "reference_frame_choice_polynomial_coefficients_ascending_T":d,
                "full_rank8_choice_polynomial_degree_at_most8":True,
                "new_reference_endpoint_preparation_complete":True,
                "future_five_target_pencils_computed":False}
        value=self.stage(f"P{epsilon}-prepared-reference-endpoint",produce)
        self.ready[str(epsilon)]=self.refs[f"P{epsilon}-prepared-reference-endpoint"]
        self.checkpoint()
        return value

    def common_reference_frame(self, prepared):
        def produce():
            scan=[]
            chosen=None
            for lam in range(17):
                vals={str(e):eval_poly(prepared[e]["reference_frame_choice_polynomial_coefficients_ascending_T"],lam)
                      for e in (0,1)}
                scan.append({"integer_parameter":lam,"endpoint_polynomial_values_mod_prime":vals})
                if all(vals.values()):
                    chosen=lam
                    break
            assert chosen is not None, "Two nonzero degree-eight polynomials cannot exclude all seventeen integers"
            return {"prime":PRIME,"original_zeta_root":ZETA,
                "source_prepared_endpoints":self.ready,
                "candidate_integer_range":[0,16],"actual_parameter_scan":scan,
                "actual_common_integer_parameter_lambda0":chosen,
                "same_global_reference_generator_at_both_endpoints":True,
                "exact_generator":{
                    "operation":"original_rank8_field_norm",
                    "argument":{"operation":"sum","constant_one":True,
                        "integer_parameter":chosen,"target_pullback_original_reference_function":self.inputs["reference_function"]},
                    "equivalent_argument":"q*((u+lambda0*f)/u)",
                    "original_generic_frame_one":True},
                "original_nine_global_parameters_unchanged":list(range(9)),
                "selected_nonempty_P0_blocks_have_nonzero_lambda":all(
                    prepared[e]["target_P0_block_rank"]==0 or chosen!=0 for e in (0,1)),
                "five_target_sources":{"R903":None,"R907":None}}
        return self.stage("same-global-reference-integer-frame",produce)

    def endpoint_certificate(self, epsilon, prepared, common):
        name=f"P{epsilon}-complete-reference-ideal-and-norm-frame"
        old=self.old(name)
        if old is not None:
            self.endpoints[str(epsilon)]=self.refs[name]
            return old
        def produce():
            ctx=self.contexts[epsilon]
            lifted=self.old(f"P{epsilon}-complete-lifted-summand-basis")
            regular=self.old(f"P{epsilon}-reference-regular-complement")
            assert lifted is not None and regular is not None
            r=prepared["target_P0_block_rank"];rc=DIM-r
            lam=common["actual_common_integer_parameter_lambda0"]
            C=regular["C_complement_coefficients_ascending_T_mod_prime"]
            Cvalue=eval_poly(C,lam)
            assert Cvalue
            S=self.H.SeriesRing(1)
            value=[[S.element(x[0]) for x in row] for row in regular["complete_reference_multiplication"]]
            denominator=madd(S,midentity(S,rc),mscale(S,value,lam))
            Acomp=minverse_unit(self.H,S,denominator,self.budget)
            Bcomp=mmul(S,Acomp,value)
            blockA=[[0]*DIM for _ in range(DIM)]
            blockB=[[0]*DIM for _ in range(DIM)]
            if r:
                assert lam
                li=pow(lam,-1,PRIME)
                for i in range(r):
                    blockB[i][i]=li
            for i in range(rc):
                for j in range(rc):
                    blockA[r+i][r+j]=int(Acomp[i][j][0])
                    blockB[r+i][r+j]=int(Bcomp[i][j][0])
            change=[[int(x[0]) for x in row] for row in lifted["complete_block_basis_in_original_basis"]]
            inverse=[[int(x[0]) for x in row] for row in lifted["original_basis_in_complete_block_basis"]]
            C0=self.H.matmul(self.H.matmul(change,blockA),inverse)
            C1=self.H.matmul(self.H.matmul(change,blockB),inverse)
            assert [[(C0[i][j]+lam*C1[i][j])%PRIME for j in range(DIM)]
                    for i in range(DIM)]==self.H.identity(DIM)
            d=prepared["reference_frame_choice_polynomial_coefficients_ascending_T"]
            denom=eval_poly(d,lam)
            assert denom
            deninv=pow(denom,-1,PRIME)
            relative=[]
            for i in range(9):
                actual=determinant_constant([[(a+i*b)%PRIME for a,b in zip(ar,br)]
                                             for ar,br in zip(C0,C1)])
                formula=eval_poly(d,i)*deninv%PRIME
                assert actual==formula
                relative.append(actual)
            assert any(relative)
            mstar=int(prepared["actual_parameter_norm_order"])
            lcstar=int(prepared["actual_parameter_norm_leading_mod_prime"])
            rho_order=-254*mstar
            rho_leading=pow(lam,r,PRIME)*pow(self.U272,-r,PRIME)%PRIME
            rho_leading=rho_leading*pow(lcstar,-254,PRIME)%PRIME*Cvalue%PRIME
            assert rho_leading
            tunit=int(ctx["frame"]["original_t_over_rho_mod_prime"])
            assert tunit
            tleading=rho_leading*pow(tunit,-rho_order,PRIME)%PRIME
            return {"endpoint":epsilon,"prime":PRIME,"original_zeta_root":ZETA,"original_s_root":SROOT,
                "local_parameter":STRATEGY["endpoint_parameters"][epsilon],
                "source_prepared_endpoint":self.ready[str(epsilon)],
                "source_common_global_reference_frame":self.refs["same-global-reference-integer-frame"],
                "source_complete_block_basis":self.refs[f"P{epsilon}-complete-lifted-summand-basis"],
                "source_reference_regular_complement":self.refs[f"P{epsilon}-reference-regular-complement"],
                "source_original_reference_function":self.inputs["reference_function"],
                "source_original_normal_order":self.eref(epsilon,"normal_order"),
                "source_original_target_certificate":self.eref(epsilon,"target_certificate"),
                "source_original_order_and_t_frame":self.eref(epsilon,"frame"),
                "actual_original_target_input_precision":ctx["source_precision"],
                "actual_working_rho_precision":ctx["N"],
                "target_P0_block_rank":r,"complement_rank":rc,
                "actual_common_integer_parameter_lambda0":lam,
                "complete_relative_first_generator_matrix_mod_rho":C0,
                "complete_relative_second_generator_matrix_mod_rho":C1,
                "all64_reverse_identity_coefficients_verified":True,
                "original_P0_block_exact_inverse_reference_order_lower_bound":254,
                "P0_block_relative_matrix_zero_bound_in_rho":84 if r else None,
                "original_nine_parameters":list(range(9)),
                "nine_reference_relative_coordinates_mod_prime":relative,
                "all9_complete_rank8_determinants_equal_primitive_polynomial_values":True,
                "actual_reference_norm_rho_order":rho_order,
                "actual_reference_norm_rho_leading_mod_prime":rho_leading,
                "actual_original_t_over_rho_mod_prime":tunit,
                "actual_reference_norm_t_leading_mod_prime":tleading,
                "original_reference_lattice_exact_expression":{
                    "operation":"positive_principal_fractional_B_ideal",
                    "generator":"1+lambda0*q*(v0)=q*((u+lambda0*f)/u)",
                    "lambda0":lam,"source_original_reference":self.inputs["reference_function"],
                    "basis":"generator times every one of the original eight normal-order basis columns",
                    "relative_generators":["1","q*(v0)"],
                    "exact_reverse_relation":"C0+lambda0*C1=identity"},
                "original_determinant_exact_expression":{
                    "operation":"quotient","numerator":"Norm(q*(u+lambda0*f))","denominator":"Norm(q*u)",
                    "same_original_reference_scalar_and_generic_frame_retained":True},
                "original_reference_t_frame":self.reference["original_t_frame"],
                "original_dual7":ctx["frame"]["original_dual7"],
                "original_nu":ctx["frame"]["original_nu"],
                "both_determinant_factors_under_dual7_retained":True,
                "actual_reference_local_ideal_and_relative_coordinates_at_original_place_certified":True,
                "actual_reference_complete_Norm_frame_at_original_place_computed":True,
                "all_original_eight_factors_and_nilpotents_preserved":True,
                "characteristic_zero_expanded_coordinates_or_observed_orders_claimed":False,
                "full_Laurent_lattice_basis_expanded":False,
                "five_target_NormPhi_or_Poincare_frame_computed":False,
                "Picard_inactive_or_height_computed":False}
        value=self.stage(name,produce)
        self.endpoints[str(epsilon)]=self.refs[name]
        self.checkpoint()
        return value

    def compare(self, endpoints):
        def produce():
            left,right=endpoints[0],endpoints[1]
            assert left["actual_common_integer_parameter_lambda0"]==right["actual_common_integer_parameter_lambda0"]
            lc0=left["actual_reference_norm_t_leading_mod_prime"]
            lc1=right["actual_reference_norm_t_leading_mod_prime"]
            ratio=lc1*pow(lc0,-1,PRIME)%PRIME
            return {"prime":PRIME,"original_zeta_root":ZETA,
                "source_two_complete_reference_frames":self.endpoints,
                "source_same_global_integer_frame":self.refs["same-global-reference-integer-frame"],
                "same_global_reference_norm_function_at_both_original_endpoints":True,
                "actual_original_t_frame_leading_ratio_P1_over_P0_mod_prime":ratio,
                "actual_endpoint_reference_rho_orders":{str(e):endpoints[e]["actual_reference_norm_rho_order"] for e in (0,1)},
                "actual_endpoint_reference_t_leading_values":{str(e):endpoints[e]["actual_reference_norm_t_leading_mod_prime"] for e in (0,1)},
                "original_dual7":self.contexts[0]["frame"]["original_dual7"],
                "both_original_determinant_factors_and_reference_norm_retained":True,
                "five_target_NormPhi_detU_and_reference_comparison_computed":False,
                "original_theta_Poincare_nonp_or_height_computed":False}
        return self.stage("complete-reference-two-endpoint-t-frame-comparison",produce)

    def inventory(self):
        files=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name in (CURRENT,INVENTORY):
                continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag
            assert value["complete"] is True
            files.append(spec(path))
        save(self.out/INVENTORY,{"result":RESULT,"configuration":self.tag,"complete":True,
            "files":files,"only_actual_complete_stages_listed":True,
            "current_checkpoint_excluded":True})
        return spec(self.out/INVENTORY)

    def finish(self, complete, reason=None):
        self.checkpoint(reason)
        inventory=self.inventory()
        final={"result":RESULT,"configuration":self.tag,"complete":bool(complete),
            "p":41,"prime":PRIME,"original_zeta_root":ZETA,"original_s_root":SROOT,
            "source_identities":{k:source_identity(self.item["sources"][k]) for k in SOURCES},
            "source_audit":self.refs.get("source-audit"),
            "prepared_endpoint_records":self.ready,"completed_endpoint_certificates":self.endpoints,
            "actual_completed_endpoint_count":len(self.endpoints),
            "same_global_reference_integer_frame":self.refs.get("same-global-reference-integer-frame"),
            "complete_original_t_frame_comparison":self.refs.get("complete-reference-two-endpoint-t-frame-comparison"),
            "endpoint_stops":self.endpoint_stops,"stop_reason":reason,
            "actual_original_two_endpoint_reference_ideals_and_relative_coordinates_certified":bool(complete),
            "actual_original_two_endpoint_reference_Norm_frames_computed":bool(complete),
            "actual_full_length8_algebras_and_nilpotents_preserved":bool(complete),
            "old_R917_normal_orders_R923_target_coordinates_or_R879_solution_recomputed":False,
            "new_original_point_jets_or_char0_coefficients_reconstructed":False,
            "full_Laurent_lattice_bases_expanded":False,
            "characteristic_zero_observed_content_orders_claimed":False,
            "five_target_endpoint_ideal_lattices_computed":False,
            "five_target_NormPhi_detU_complete_calibration_computed":False,
            "Hecke_Picard_inactive_theta_Poincare_nonp_or_height_computed":False,
            "future_target_sources":{"R903":None,"R907":None},
            "stage_manifest":inventory,"resume_state":self.current,
            "seconds":time.monotonic()-self.started}
        save(self.out/FINAL,final)
        return final

    def run(self):
        prepared={}
        for epsilon in (0,1):
            try:
                prepared[epsilon]=self.prepare_endpoint(epsilon)
                self.endpoint_stops.pop(str(epsilon),None)
            except self.H.NeedPrecision as exc:
                self.endpoint_stops[str(epsilon)]=exc.to_data()
                self.checkpoint(exc.to_data())
        if len(prepared)!=2:
            return self.finish(False,{"kind":"NeedPrecision","endpoints":self.endpoint_stops})
        common=self.common_reference_frame(prepared)
        endpoints={e:self.endpoint_certificate(e,prepared[e],common) for e in (0,1)}
        self.compare(endpoints)
        return self.finish(True)


def main():
    sys.set_int_max_str_digits(0)
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("New mathematical arithmetic is restricted to the original public repository Actions")
    parser=argparse.ArgumentParser()
    parser.add_argument("--config",required=True)
    parser.add_argument("--out",required=True)
    parser.add_argument("--budget-minutes",type=float,required=True)
    args=parser.parse_args()
    started=time.monotonic();job=None;final=None;error=None;code=1
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    try:
        job=Job(args)
        final=job.run()
        code=0 if final["complete"] else 2
    except BudgetStop as exc:
        error={"kind":"BudgetStop","message":str(exc)}
        if job is not None:
            final=job.finish(False,error)
        code=1
    except BaseException as exc:
        traceback.print_exc()
        error={"kind":type(exc).__name__,"message":str(exc)}
        if job is not None:
            try:
                final=job.finish(False,error)
            except BaseException:
                traceback.print_exc()
        code=1
    receipt={"result":RESULT,"source_sha256":sha(__file__),"complete":bool(final and final["complete"]),
        "process_exit_code":code,"error":error,"seconds":time.monotonic()-started,
        "configuration_sha256":None if job is None else fingerprint(job.tag),
        "certificate_sha256":sha(out/FINAL) if (out/FINAL).exists() else None,
        "stage_manifest":None if final is None else final["stage_manifest"],
        "actual_completed_endpoint_count":0 if final is None else final["actual_completed_endpoint_count"],
        "actual_original_two_endpoint_reference_Norm_frames_computed":bool(final and final["complete"]),
        "five_target_NormPhi_theta_Poincare_or_height_computed":False}
    save(out/"core-receipt.json",receipt)
    print("R927_REFERENCE_CORE_RECEIPT="+json.dumps(receipt,sort_keys=True),flush=True)
    raise SystemExit(code)


if __name__=="__main__":
    main()
