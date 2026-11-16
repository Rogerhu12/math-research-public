#!/usr/bin/env python3
"""Original target normal functions in the two completed rank-eight endpoint orders.

New arithmetic is executed only by this core in the original public repository
Actions. Original order/characteristic/adjugate stages are read, never recomputed.
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

RESULT = "R923-original-two-endpoint-target-normal-coordinates"
FINAL = "p41-original-two-endpoint-target-normal-coordinates-certificate.json"
PREFIX = "R923-target-"
CURRENT = PREFIX + "current.json.gz"
INVENTORY = PREFIX + "stage-manifest.json.gz"
PRIME, ZETA, SROOT = 1000000753, 549966761, 99932770
DIM, NORMAL, COLUMN_BLOCK, LEVEL_BLOCK = 8, 272, 16, 16
EPS = [0] + [1] * 144 + [2] * 127
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
META = ("public-actions-input.json", "run-receipt.json", "core-receipt.json")
SOURCES = ("R917", "POLY", "R827", "R873")
PROOFS = ("R923", "R917", "R912", "R860", "R885", "R873")
HELPER_SHA = "c728c8e06cef3dfbe4d33f3a988cbbc1c3012909d67b4684d941effdec67033d"
H64 = re.compile(r"[0-9a-f]{64}")
DEFINITIONS = {
    "R917": ("R917-original-two-endpoint-normal-orders",
        "f0e321a19ef6dbd259e88de1b670f514b0f9ed0df5b24659a9f787978b8fd743"),
    "POLY": ("R885-original-polynomial-one-row-adjugate",
        "dd4ef0d445e7c90caf568d7aa87951166d6730cc86da0a44be11b664742d3035"),
    "R827": ("R827-original-global-modular-derivative-termination",
        "d9cf773976f3beff7f44ff30f8b593665f481470cb52297239710e0ce6e062d2"),
    "R873": ("R873-original-cyclic-seven-correspondence",
        "3c4922ee5b83d82123d234df47e67f82d7c8032f1152c6cf14df34622101918c"),
}
STRATEGY = {
    "scope": "two_original_endpoint_target_w_and_all272_normal_functions",
    "original_auxiliary_prime": PRIME, "original_zeta_root": ZETA, "original_s_root": SROOT,
    "rank": DIM, "normal_dimension": NORMAL,
    "endpoint_parameters": ["rho0=z-z0", "rho1=iota^*rho0=z-2*beta72-z0"],
    "actual_R917_primitive_h": 0, "actual_R917_primitive_precision": 273,
    "actual_R917_primitive_discriminant_order": 6,
    "actual_R917_normal_order_precision": 271,
    "target_w": "B_inverse*adj(M_mprime)*(Ktilde/Ptilde8), then divide old primitive disc",
    "old_primitive_discriminant_recomputed": False,
    "target_w_uniform_precision": 267,
    "shared_adjugate_algorithm": "seven constant-unit Newton matrix steps; both adjugate products",
    "polynomial_source": "complete original R885 row levels0..271; no z0 coordinate substitution",
    "normal_column_block": COLUMN_BLOCK, "Horner_level_block": LEVEL_BLOCK,
    "first_cofactor_block_precedes_shared_denominator_decision": True,
    "integral_quotient_precision": "N-vrho(det); deflate all numerators before unit inversion",
    "zero_truncation": "NeedPrecision, never an exact zero or inactive flag",
    "full_verification": "Ptilde_U*V=Ktilde; chi(U,V)=0; gamma0=1; gamma1=V; all272 gammaW=Vgamma",
    "all_factors_nilpotents_and_original_P_K_preserved": True,
    "basis_and_original_t_frame": "unchanged source R917, both determinant factors under original dual7",
    "exact_nu": "82*tau*dqY/qY; iota fixes nu; no new numeric differential transport",
    "no_original_W_Krylov_273nodes_polynomial_adjugate_or_idealizer_recomputed": True,
    "characteristic_zero_expanded_coordinates": False,
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
    payload = (json.dumps(value, sort_keys=True, separators=(",", ":"),
                          ensure_ascii=False) + "\n").encode()
    with tmp.open("wb") as raw:
        if path.name.endswith(".gz"):
            with gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0, compresslevel=2) as stream:
                stream.write(payload)
        else:
            raw.write(payload)
        raw.flush()
        os.fsync(raw.fileno())
    tmp.replace(path)


def identity(value):
    return {k: str(value[k]) for k in BASE}


def source_identity(value):
    return {**identity(value), "configuration_sha256": value["configuration_sha256"],
        "selected_files_sha256": value["selected_files_sha256"],
        "selected_file_count": value["selected_file_count"],
        "certificate": None if value.get("certificate") is None else plain(value["certificate"]),
        "configuration_stage": None if value.get("configuration_stage") is None
                                    else plain(value["configuration_stage"])}


def expected_tag(item):
    return {"result": RESULT, "source_sha256": item["core_sha256"],
        "helper_sha256": item["helper_sha256"], "p": 41, "prime": PRIME,
        "python_flint": "0.9.0", "method_sha256": item["method_sha256"],
        "proofs_sha256": {k: item["proofs"][k]["sha256"] for k in PROOFS},
        "sources": {k: source_identity(item["sources"][k]) for k in SOURCES},
        "inputs": item["inputs"],
        "requested_minimum_output_precision": item["requested_minimum_output_precision"],
        "strategy": STRATEGY}


class Source:
    def __init__(self, label, item):
        self.label, self.item = label, item
        self.path = Path(item["directory"])
        assert (item["result"], item["core_sha256"]) == DEFINITIONS[label]
        self.files = {name: plain(v) for name, v in item["files"].items()}
        assert len(self.files) == item["selected_file_count"]
        assert fingerprint(self.files) == item["selected_files_sha256"]
        for name, row in self.files.items():
            assert name == row["file"] and spec(self.path/name) == row, (label, name)
        manifest = self.get("full-outputs-manifest.json")
        assert self.files["full-outputs-manifest.json"]["sha256"] == item["manifest_sha256"]
        assert manifest["result"] == item["result"]
        entries = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(entries) == len(manifest["files"])
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
        if label == "R827":
            assert item.get("certificate") is None
            assert run["complete"] is False and core["complete"] is False
            assert run["process_exit_code"] == 124
            self.cert = None
            anchor = self.get(item["configuration_stage"]["file"])
            assert anchor["complete"] is True
            self.tag = anchor["configuration"]
        else:
            assert run["complete"] is True and run["process_exit_code"] == 0 and core["complete"] is True
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


def vec_pack(R, vector):
    return [R.pack(x) for x in vector]


def mat_pack(R, matrix):
    return [[R.pack(x) for x in row] for row in matrix]


def mat_read(R, matrix):
    assert len(matrix) == DIM and all(len(row) == DIM for row in matrix)
    return [[R.element(x) for x in row] for row in matrix]


def mat_identity(R):
    return [[R.element(int(i == j)) for j in range(DIM)] for i in range(DIM)]


def vec_add(R, a, b):
    return [R.add(x, y) for x, y in zip(a, b)]


def mat_vec(R, A, b):
    out = [R.zero for _ in range(DIM)]
    for i in range(DIM):
        for j in range(DIM):
            out[i] = R.add(out[i], R.mul(A[i][j], b[j]))
    return out


def mat_mul(R, A, B):
    out = [[R.zero for _ in range(DIM)] for _ in range(DIM)]
    for i in range(DIM):
        for k in range(DIM):
            if A[i][k] == R.zero:
                continue
            for j in range(DIM):
                out[i][j] = R.add(out[i][j], R.mul(A[i][k], B[k][j]))
    return out


def multiplication_matrix(order, value):
    R = order.R
    answer = [[R.zero for _ in range(DIM)] for _ in range(DIM)]
    for j in range(DIM):
        for r in range(DIM):
            if value[r] != R.zero:
                for i in range(DIM):
                    answer[i][j] = R.add(answer[i][j], R.mul(value[r], order.table[r][j][i]))
    return answer


def adjugate_and_product(R, M, budget):
    # Newton/Faddeev uses only the explicitly invertible constants 1,...,7.
    # For size eight the exact adjugate is -B7; no series pivot is inverted.
    B = mat_identity(R)
    constants = []
    for k in range(1, DIM):
        budget()
        B = mat_mul(R, M, B)
        trace = R.zero
        for i in range(DIM):
            trace = R.add(trace, B[i][i])
        c = R.scale(trace, -pow(k, -1, PRIME) % PRIME)
        constants.append(c)
        for i in range(DIM):
            B[i][i] = R.add(B[i][i], c)
    adj = [[R.neg(x) for x in row] for row in B]
    left, right = mat_mul(R, M, adj), mat_mul(R, adj, M)
    delta = left[0][0]
    for i in range(DIM):
        for j in range(DIM):
            expected = delta if i == j else R.zero
            assert left[i][j] == right[i][j] == expected, ("adjugate_product", i, j)
    return adj, delta, constants


def crop_order(H, raw, N):
    assert 0 < N <= raw["absolute_rho_precision"]
    changed = dict(raw, absolute_rho_precision=N,
        multiplication_structure_coefficients=[[[v[:N] for v in row] for row in plane]
            for plane in raw["multiplication_structure_coefficients"]],
        one_coordinates=[v[:N] for v in raw["one_coordinates"]])
    return H.Order.unpack(changed)


def vector_from_Laurent(R, entries):
    out = []
    for v in entries:
        assert v["exact_finite_Laurent_polynomial_over_residue_field"] is True
        low, coeff = v["lowest_exponent"], v["coefficients_ascending"]
        assert not coeff or low >= 0
        out.append(R.element(([0] * low + coeff)[:R.N] if coeff else []))
    return out


def exact_nonnegative_matrix(R, raw):
    assert len(raw) == DIM and all(len(row) == DIM for row in raw)
    return [vector_from_Laurent(R, row) for row in raw]


class Job:
    def __init__(self, args):
        self.started = time.monotonic()
        self.deadline = self.started + 60 * float(args.budget_minutes)
        self.item = read(args.config)
        self.out = Path(args.out)
        self.out.mkdir(parents=True, exist_ok=True)
        item = self.item
        assert item["result"] == RESULT and item["p"] == 41
        assert item["producer_inputs_pending"] is False
        assert item["future_target_sources"] == {"R903": None, "R907": None}
        assert 1 <= item["requested_minimum_output_precision"] <= 267
        assert sha(__file__) == item["core_sha256"]
        assert item["helper_sha256"] == HELPER_SHA
        topic = Path(item["topic_directory"])
        assert sha(topic/item["method"]) == item["method_sha256"]
        assert set(item["proofs"]) == set(PROOFS)
        for value in item["proofs"].values():
            assert sha(topic/value["file"]) == value["sha256"]
        helper_path = Path(__file__).resolve().parent / item["helper"]
        assert helper_path.name == "R917_endpoint_order_arithmetic.py"
        assert sha(helper_path) == HELPER_SHA
        loader = importlib.util.spec_from_file_location("R923_source_bound_R917_arithmetic", helper_path)
        self.H = importlib.util.module_from_spec(loader)
        loader.loader.exec_module(self.H)
        assert self.H.P == PRIME and self.H.D == DIM
        assert set(item["sources"]) == set(SOURCES)
        self.sources = {label: Source(label, item["sources"][label]) for label in SOURCES}
        self.tag = expected_tag(item)
        self.inputs = item["inputs"]
        self.refs, self.endpoints, self.endpoint_stops = {}, {}, {}
        self.active, self.current = None, None
        self.row_cache = {}
        self.checkpoint()
        self.prepare()

    def budget(self):
        if time.monotonic() >= self.deadline:
            raise BudgetStop("Actual mathematical budget reached; complete atomic stages retained")

    def input(self, key):
        value = self.inputs[key]
        return self.sources[value["source_group"]].stage(value)

    def endpoint_input(self, epsilon, key):
        value = self.inputs["endpoints"][str(epsilon)][key]
        return self.sources["R917"].stage(value)

    def path(self, name):
        return self.out / (PREFIX + name + ".json.gz")

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
        old = self.old(name)
        if old is not None:
            return old
        self.budget()
        self.active = name
        self.checkpoint()
        value = produce()
        assert "result" not in value and "configuration" not in value and "complete" not in value
        value = {"result": RESULT, "configuration": self.tag, "complete": True, **value}
        save(self.path(name), value)
        self.refs[name] = spec(self.path(name))
        self.active = None
        self.checkpoint()
        print("R923_TARGET_STAGE=" + json.dumps(self.refs[name], sort_keys=True), flush=True)
        return value

    def checkpoint(self, stop=None):
        value = {"result": RESULT, "configuration": self.tag, "complete": False,
            "active_stage": self.active, "completed_endpoint_certificates": self.endpoints,
            "endpoint_stops": self.endpoint_stops, "completed_stage_refs": self.refs,
            "last_stop": stop, "seconds": time.monotonic()-self.started}
        save(self.out/CURRENT, value)
        self.current = spec(self.out/CURRENT)

    def prepare(self):
        self.DAG = self.input("correspondence_DAG")
        self.exact = self.input("exact_coordinate_expression")
        self.audit917 = self.input("completed_order_source_audit")
        self.char = self.input("characteristic_relation")
        self.adjindex = self.input("adjugate_row_index")
        self.Wdata = self.input("original_W")
        self.place = self.input("original_place")
        assert plain(self.DAG["coefficient_unit_solve"]) == plain(self.inputs["exact_coordinate_expression"])
        assert self.DAG["rigidified_Hecke_transport"]["frozen_direction"] == "Nm_pi_t(pi_s^*I)"
        assert self.DAG["rigidified_Hecke_transport"]["determinant_numerator_and_denominator_both_transported"] is True
        assert plain(self.audit917["characteristic_zero_exact_P_K_unit_solve"]) == plain(self.inputs["exact_coordinate_expression"])
        assert identity(self.audit917["source_identities"]["R873"]) == identity(self.item["sources"]["R873"])
        assert self.audit917["original_dual7"] == self.DAG["rigidified_Hecke_transport"]
        assert self.place["prime"] == PRIME and self.place["original_zeta_root"] == ZETA
        assert (2 * ZETA + 1) % PRIME == SROOT
        assert self.Wdata["prime"] == PRIME and self.Wdata["original_rational_denominators_all_units"] is True
        self.W = self.Wdata["W_coefficients_mod_prime"]
        assert len(self.W) == 4
        assert all(len(a) == NORMAL and all(len(row) == NORMAL for row in a) for a in self.W)
        self.Wmat = [nmod_mat(a, PRIME) for a in self.W]
        self.chi = self.char["coefficient_polynomials_ascending_z"]
        assert len(self.chi) == 273 and self.chi[0] == [1]
        assert self.char["exact_original_modular_characteristic_polynomial_certified"] is True
        assert self.char["all273_nodes_for_all273_T_coefficients_verified"] is True
        assert self.adjindex["r_is_exactly_original_e0_transpose_adjugate"] is True
        assert self.adjindex["all272_polynomial_components_of_terminal_row_zero"] is True
        assert plain(self.adjindex["characteristic_relation"]) == plain(self.inputs["characteristic_relation"])
        assert len(self.inputs["row_levels"]) == len(self.adjindex["adjugate_row_T_terms"]) == NORMAL
        for k, (term, source) in enumerate(zip(self.adjindex["adjugate_row_T_terms"], self.inputs["row_levels"])):
            assert source["source_group"] == "POLY"
            assert term["b_level"] == k and term["T_power"] == 271-k
            assert plain(term["source"]) == plain(source)
        self.source_endpoints = {}
        for epsilon in (0, 1):
            cert = self.endpoint_input(epsilon, "certificate")
            primitive = self.endpoint_input(epsilon, "primitive")
            olddisc = self.endpoint_input(epsilon, "primitive_discriminant")
            normal = self.endpoint_input(epsilon, "normal_order")
            cleared = self.endpoint_input(epsilon, "common_cleared")
            frame = self.endpoint_input(epsilon, "frame")
            refs = self.inputs["endpoints"][str(epsilon)]
            assert cert["normal_order_certified"] is True and cert["full_length8_special_fibre_preserved"] is True
            assert cert["endpoint"] == epsilon and cert["actual_initial_discriminant_order"] == 6
            assert cert["actual_total_index_length"] == 1 and cert["actual_remaining_rho_precision"] == 271
            assert cert["source_primitive_order"] == plain(refs["primitive"])
            assert cert["complete_normal_order"] == plain(refs["normal_order"])
            assert cert["source_common_cleared_jets"] == plain(refs["common_cleared"])
            assert cert["primitive_and_t_frames"] == plain(refs["frame"])
            assert primitive["original_Ptilde8_order"] == primitive["original_Theta_rho_power"] == 0
            assert primitive["absolute_rho_precision"] == primitive["order"]["absolute_rho_precision"] == 273
            assert normal["order"]["absolute_rho_precision"] == 271
            assert normal["order"]["all_factors_and_nilpotents_retained"] is True
            assert olddisc["source_order"] == plain(refs["primitive"])
            assert olddisc["discriminant_order"] == 6 and olddisc["absolute_rho_precision"] == 273
            assert olddisc["division_free_determinant"] is True
            assert cleared["absolute_rho_precision"] == 273 and cleared["column_order"] == "P0..P8,K0..K7"
            assert cleared["local_parameter"] == STRATEGY["endpoint_parameters"][epsilon]
            assert len(cleared["common_cleared_coefficient_jets_mod_prime"]) == 17
            assert all(len(col) == 273 for col in cleared["common_cleared_coefficient_jets_mod_prime"])
            assert frame["both_determinant_factors_required_under_dual7"] is True
            assert frame["original_dual7"] == self.DAG["rigidified_Hecke_transport"]
            assert frame["original_nu"]["iota_fixes_nu"] is True
            assert frame["determinant_rho_order_relative_to_1_U_to_U7"] == -1
            assert frame["original_t_over_rho_mod_prime"] == (354813668 if epsilon == 0 else 645187085)
            assert plain(frame["original_target_w_exact_expression"]["source_exact_global_P_K"]) == plain(self.inputs["correspondence_DAG"])
            for row in normal["order"]["primitive_Theta_powers_in_basis"]:
                for entry in row:
                    assert entry["exact_finite_Laurent_polynomial_over_residue_field"] is True
                    assert not entry["coefficients_ascending"] or entry["lowest_exponent"] >= 0
            self.source_endpoints[epsilon] = dict(certificate=cert, primitive=primitive,
                primitive_discriminant=olddisc, normal_order=normal, common_cleared=cleared, frame=frame)
        self.stage("source-audit", lambda: {
            "prime": PRIME, "original_zeta_root": ZETA, "original_s_root": SROOT,
            "source_identities": {k: source_identity(self.item["sources"][k]) for k in SOURCES},
            "actual_selected_original_file_count": sum(self.item["sources"][k]["selected_file_count"] for k in SOURCES),
            "inputs": self.inputs, "exact_original_P_K": self.inputs["correspondence_DAG"],
            "exact_original_2058_unit_solve": self.inputs["exact_coordinate_expression"],
            "original_dual7": self.DAG["rigidified_Hecke_transport"],
            "old_order_273_jets_and_polynomial_row_recomputed": False,
            "original_W_four_blocks_reused": True,
            "source_primitives_have_h0_and_discriminant_order6": True,
            "source_normal_inverse_bases_have_no_negative_exponents": True,
            "characteristic_zero_coordinates_not_inferred_from_modular_values": True})

    def primitive_adjugate(self, epsilon):
        source = self.source_endpoints[epsilon]
        refs = self.inputs["endpoints"][str(epsilon)]
        def produce():
            primitive = source["primitive"]
            order = self.H.Order.unpack(primitive["order"])
            R = order.R
            monic = [R.element(x) for x in primitive["monic_coefficients_ascending_Theta"]]
            derivative = [R.scale(monic[i], i) for i in range(1, 9)]
            M = multiplication_matrix(order, derivative)
            adj, delta, constants = adjugate_and_product(R, M, self.budget)
            old = R.element(source["primitive_discriminant"]["discriminant_series"])
            assert delta == old, "derivative_norm_equals_original_primitive_discriminant"
            return {"endpoint": epsilon, "absolute_rho_precision": R.N,
                "source_primitive_order": plain(refs["primitive"]),
                "source_original_primitive_discriminant": plain(refs["primitive_discriminant"]),
                "multiplication_by_original_mprime": mat_pack(R, M),
                "adjugate_matrix": mat_pack(R, adj),
                "newton_coefficients_c1_through_c7": [R.pack(c) for c in constants],
                "actual_original_discriminant_order": 6,
                "both_adjugate_products_equal_old_primitive_discriminant": True,
                "old_discriminant_series_recomputed": False,
                "only_constant_denominators_1_through7_inverted": True,
                "normal_basis_discriminant_order4_not_used_as_derivative_norm": True}
        return self.stage(f"P{epsilon}-primitive-derivative-adjugate", produce)

    def target_w(self, epsilon):
        adjstage = self.primitive_adjugate(epsilon)
        refs = self.inputs["endpoints"][str(epsilon)]
        source = self.source_endpoints[epsilon]
        name = f"P{epsilon}-target-w-normal-coordinates"
        def produce():
            primitive = source["primitive"]
            R = self.H.SeriesRing(273)
            ainv = R.element(primitive["deflated_leading_unit_inverse"])
            columns = source["common_cleared"]["common_cleared_coefficient_jets_mod_prime"]
            a8 = R.element(columns[8])
            assert R.mul(a8, ainv) == R.one
            rhs = [R.mul(R.element(x), ainv) for x in columns[9:]]
            adj = mat_read(R, adjstage["adjugate_matrix"])
            numerator_primitive = mat_vec(R, adj, rhs)
            inverse_basis = exact_nonnegative_matrix(R,
                source["normal_order"]["order"]["primitive_Theta_powers_in_basis"])
            numerator = mat_vec(R, inverse_basis, numerator_primitive)
            for i, value in enumerate(numerator):
                assert all(int(value[k]) == 0 for k in range(6)), ("target_w_integrality", epsilon, i)
            T = 267
            S = self.H.SeriesRing(T)
            olddisc = source["primitive_discriminant"]["discriminant_series"]
            unit = S.element(olddisc[6:])
            inverse = S.unit_inverse(unit)
            values = [S.mul(S.element(R.pack(x)[6:]), inverse) for x in numerator]
            order = crop_order(self.H, source["normal_order"]["order"], T)
            U = vector_from_Laurent(order.R, source["frame"]["original_U_coordinates_in_normal_order_basis"])
            MU = multiplication_matrix(order, U)
            def evaluate(cs):
                answer = [order.R.zero for _ in range(DIM)]
                for c in reversed(cs):
                    answer = mat_vec(order.R, MU, answer)
                    answer = vec_add(order.R, answer,
                                     [order.R.mul(order.R.element(c[:T]), x) for x in order.one])
                return answer
            dcoef = [[i * int(v) % PRIME for v in columns[i][:T]] for i in range(1,9)]
            dvalue, kval = evaluate(dcoef), evaluate(columns[9:])
            assert order.multiply(dvalue, values) == kval, "full_original_Ptilde_derivative_times_V_equals_Ktilde"
            return {"endpoint": epsilon, "absolute_rho_precision": T,
                "source_original_adjugate": self.refs[f"P{epsilon}-primitive-derivative-adjugate"],
                "source_original_normal_order": plain(refs["normal_order"]),
                "source_original_primitive_discriminant": plain(refs["primitive_discriminant"]),
                "source_original_common_cleared_jets": plain(refs["common_cleared"]),
                "source_original_basis_and_t_frame": plain(refs["frame"]),
                "source_exact_global_P_K": self.inputs["correspondence_DAG"],
                "original_Ptilde8_inverse_reused": True,
                "normal_numerator_before_deflation": vec_pack(R, numerator),
                "all48_coefficients_below_discriminant_order6_are_zero": True,
                "discriminant_unit_part": S.pack(unit),
                "discriminant_unit_inverse": S.pack(inverse),
                "target_w_normal_coordinates_mod_prime": vec_pack(S, values),
                "target_w_definition": "Ktilde(U)/d_U_Ptilde(U)",
                "basis_transport_precedes_discriminant_deflation": True,
                "full_original_Ptilde_derivative_times_V_equals_Ktilde_verified": True,
                "all8_coordinates_retained": True,
                "characteristic_zero_expanded_target_w": False}
        return self.stage(name, produce)

    def target_operators(self, epsilon, w):
        source = self.source_endpoints[epsilon]
        refs = self.inputs["endpoints"][str(epsilon)]
        T = w["absolute_rho_precision"]
        def produce():
            order = crop_order(self.H, source["normal_order"]["order"], T)
            R = order.R
            U = vector_from_Laurent(R, source["frame"]["original_U_coordinates_in_normal_order_basis"])
            V = [R.element(x) for x in w["target_w_normal_coordinates_mod_prime"]]
            return {"endpoint": epsilon, "absolute_rho_precision": T,
                "source_original_normal_order": plain(refs["normal_order"]),
                "source_target_w": self.refs[f"P{epsilon}-target-w-normal-coordinates"],
                "source_original_basis_and_t_frame": plain(refs["frame"]),
                "target_U_coordinates": vec_pack(R, U),
                "multiplication_by_target_U": mat_pack(R, multiplication_matrix(order, U)),
                "multiplication_by_target_V": mat_pack(R, multiplication_matrix(order, V)),
                "complete_rank8_multiplication_operators": True,
                "basis_or_original_parameter_replaced": False}
        return self.stage(f"P{epsilon}-integral-target-multiplication-operators", produce)

    def powers(self, epsilon, operators):
        T = operators["absolute_rho_precision"]
        source = self.source_endpoints[epsilon]
        order = crop_order(self.H, source["normal_order"]["order"], T)
        R, values, refs = order.R, [], []
        MU = mat_read(R, operators["multiplication_by_target_U"])
        value = order.one[:]
        for first in range(0,274,32):
            stop = min(274, first+32)
            name = f"P{epsilon}-target-U-powers-{first:03d}-{stop:03d}"
            previous = None if not refs else refs[-1]
            def produce(first=first, stop=stop, value=value, previous=previous):
                current = value[:]
                answer = []
                for degree in range(first, stop):
                    self.budget()
                    answer.append(vec_pack(R, current))
                    current = mat_vec(R, MU, current)
                return {"endpoint": epsilon, "absolute_rho_precision": T,
                    "source_target_operators": self.refs[f"P{epsilon}-integral-target-multiplication-operators"],
                    "source_previous_power_block": previous,
                    "degrees": list(range(first,stop)), "powers_normal_coordinates": answer,
                    "next_power_normal_coordinates": vec_pack(R, current),
                    "all_complete8_coordinates_retained": True}
            block = self.stage(name, produce)
            assert block["degrees"] == list(range(first,stop))
            assert block["source_previous_power_block"] == previous
            values.extend(block["powers_normal_coordinates"])
            value = [R.element(x) for x in block["next_power_normal_coordinates"]]
            refs.append(self.refs[name])
        assert len(values) == 274
        return R, values, refs

    def target_characteristic(self, epsilon, operators, R, powers, power_refs):
        def produce():
            self.budget()
            flat = [[x for coordinate in value for x in coordinate] for value in powers]
            coefficients = [row + [0] * (274-len(row)) for row in self.chi]
            assert all(len(row) == 274 for row in coefficients)
            evaluated = nmod_mat(coefficients, PRIME) * nmod_mat(flat, PRIME)
            MV = mat_read(R, operators["multiplication_by_target_V"])
            answer = [R.zero for _ in range(DIM)]
            for k in range(273):
                self.budget()
                coefficient = [R.element([int(evaluated[k,i*R.N+n]) for n in range(R.N)])
                               for i in range(DIM)]
                answer = vec_add(R, mat_vec(R, MV, answer), coefficient)
            assert all(x == R.zero for x in answer), "full_target_characteristic_relation"
            return {"endpoint": epsilon, "absolute_rho_precision": R.N,
                "source_characteristic_relation": self.inputs["characteristic_relation"],
                "source_target_operators": self.refs[f"P{epsilon}-integral-target-multiplication-operators"],
                "source_target_power_blocks": power_refs,
                "full_original_chi_U_V_equals_zero": True,
                "all8_series_coordinates_checked": True,
                "new_characteristic_polynomial_computed": False}
        return self.stage(f"P{epsilon}-original-target-characteristic-relation", produce)

    def source_row(self, k):
        if k not in self.row_cache:
            source = self.inputs["row_levels"][k]
            value = self.sources["POLY"].stage(source)
            assert value["row_level"] == k and value["shape"] == [k+3, NORMAL]
            assert value["full_weighted_support_verified"] is True
            assert plain(value["source_characteristic_relation"]) == plain(self.inputs["characteristic_relation"])
            coefficients = value["coefficient_rows_ascending_z"]
            assert len(coefficients) == k+3 and all(len(row)==NORMAL for row in coefficients)
            self.row_cache[k] = coefficients
        return self.row_cache[k]

    def cofactor_block(self, epsilon, first, operators, R, powers, power_refs, prefixes):
        stop = min(NORMAL, first+COLUMN_BLOCK)
        MV = mat_read(R, operators["multiplication_by_target_V"])
        value = [[R.zero for _ in range(DIM)] for _ in range(stop-first)]
        previous = None
        for start in range(0,NORMAL,LEVEL_BLOCK):
            end = min(NORMAL, start+LEVEL_BLOCK)
            name = f"P{epsilon}-cofactor-{first:03d}-{stop:03d}-levels-{start:03d}-{end:03d}"
            def produce(start=start, end=end, value=value, previous=previous):
                current = [row[:] for row in value]
                for k in range(start,end):
                    self.budget()
                    if k+3 not in prefixes:
                        flat = [[x for coordinate in row for x in coordinate] for row in powers[:k+3]]
                        prefixes[k+3] = nmod_mat(flat, PRIME)
                    original = self.source_row(k)
                    coefficients = [[original[d][j] for d in range(k+3)] for j in range(first,stop)]
                    evaluated = nmod_mat(coefficients, PRIME) * prefixes[k+3]
                    for slot in range(stop-first):
                        ck = [R.element([int(evaluated[slot,i*R.N+n]) for n in range(R.N)])
                              for i in range(DIM)]
                        current[slot] = vec_add(R, mat_vec(R,MV,current[slot]), ck)
                return {"endpoint": epsilon, "absolute_rho_precision": R.N,
                    "normal_columns": [first,stop], "included_b_levels": [0,end],
                    "source_previous_Horner_block": previous,
                    "source_new_row_levels": self.inputs["row_levels"][start:end],
                    "source_target_operators": self.refs[f"P{epsilon}-integral-target-multiplication-operators"],
                    "source_target_power_blocks": power_refs,
                    "cofactor_values_normal_coordinates": [vec_pack(R,row) for row in current],
                    "all8_coordinates_and_nilpotents_retained": True,
                    "Horner_T_is_actual_target_w": True}
            block = self.stage(name,produce)
            assert block["normal_columns"] == [first,stop] and block["included_b_levels"] == [0,end]
            assert block["source_previous_Horner_block"] == previous
            assert block["source_new_row_levels"] == self.inputs["row_levels"][start:end]
            value = [[R.element(x) for x in row] for row in block["cofactor_values_normal_coordinates"]]
            previous = self.refs[name]
        return block,previous

    def shared_denominator(self, epsilon, head, head_ref, R):
        source = self.source_endpoints[epsilon]
        order = crop_order(self.H, source["normal_order"]["order"], R.N)
        name = f"P{epsilon}-shared-r0-adjugate"
        def produce():
            r0 = [R.element(x) for x in head["cofactor_values_normal_coordinates"][0]]
            M = multiplication_matrix(order,r0)
            adj,delta,constants = adjugate_and_product(R,M,self.budget)
            visible = next((i for i in range(R.N) if int(delta[i])),None)
            return {"endpoint":epsilon,"absolute_rho_precision":R.N,
                "source_original_normal_order":plain(self.inputs["endpoints"][str(epsilon)]["normal_order"]),
                "source_first_complete_cofactor_block":head_ref,
                "multiplication_by_r0":mat_pack(R,M),"adjugate_matrix":mat_pack(R,adj),
                "newton_coefficients_c1_through_c7":[R.pack(c) for c in constants],
                "determinant_series":R.pack(delta),
                "determinant_order_visible":visible is not None,
                "actual_determinant_order":visible,
                "determinant_valuation_lower_bound":R.N if visible is None else visible,
                "both_adjugate_products_equal_determinant_identity":True,
                "zero_truncation_is_not_exact_zero":True,
                "shared_by_all272_right_hand_sides":True}
        value = self.stage(name,produce)
        if value["actual_determinant_order"] is None:
            raise self.H.NeedPrecision("Original endpoint r0 determinant is zero only through available precision",
                {"endpoint":epsilon,"denominator_stage":self.refs[name],
                 "absolute_rho_precision":R.N,"valuation_lower_bound":R.N,
                 "algorithm_original_jet_precision_lower_bound":R.N+6+self.item["requested_minimum_output_precision"],
                 "not_a_function_zero_or_Picard_inactive_certificate":True})
        d = value["actual_determinant_order"]
        T = R.N-d
        if T < self.item["requested_minimum_output_precision"]:
            raise self.H.NeedPrecision("Actual shared r0 determinant leaves too few requested output terms",
                {"endpoint":epsilon,"denominator_stage":self.refs[name],"actual_determinant_order":d,
                 "available_output_precision":T,
                 "algorithm_original_jet_precision_required":6+d+self.item["requested_minimum_output_precision"]})
        def inverse():
            S = self.H.SeriesRing(T)
            unit = S.element(value["determinant_series"][d:])
            inv = S.unit_inverse(unit)
            return {"endpoint":epsilon,"source_shared_adjugate":self.refs[name],
                "input_absolute_rho_precision":R.N,"actual_determinant_order":d,
                "output_absolute_rho_precision":T,
                "determinant_unit_part":S.pack(unit),"determinant_unit_inverse":S.pack(inv),
                "unit_product_verified":True,"division_precedes_unit_inverse":True}
        inv = self.stage(f"P{epsilon}-shared-r0-unit-inverse",inverse)
        return value,inv

    def normalize_block(self, epsilon, first, cofactor, cofactor_ref, shared, inverse):
        stop = min(NORMAL,first+COLUMN_BLOCK)
        N = shared["absolute_rho_precision"]
        d,T = inverse["actual_determinant_order"],inverse["output_absolute_rho_precision"]
        R,S = self.H.SeriesRing(N),self.H.SeriesRing(T)
        name = f"P{epsilon}-target-normal-{first:03d}-{stop:03d}"
        def produce():
            adj = mat_read(R,shared["adjugate_matrix"])
            unitinv = S.element(inverse["determinant_unit_inverse"])
            coords = []
            for slot,raw in enumerate(cofactor["cofactor_values_normal_coordinates"]):
                self.budget()
                numerator = mat_vec(R,adj,[R.element(x) for x in raw])
                for coordinate,value in enumerate(numerator):
                    assert all(int(value[n])==0 for n in range(d)), (
                        "target_normal_integrality",epsilon,first+slot,coordinate,d)
                coords.append([S.mul(S.element(R.pack(x)[d:]),unitinv) for x in numerator])
            M = mat_read(S,shared["multiplication_by_r0"])
            for slot,value in enumerate(coords):
                expected = [S.element(x) for x in cofactor["cofactor_values_normal_coordinates"][slot]]
                assert mat_vec(S,M,value)==expected,("full_r0_gamma_equals_ri",first+slot)
            order = crop_order(self.H,self.source_endpoints[epsilon]["normal_order"]["order"],T)
            if first == 0:
                assert coords[0] == order.one
                target_w = self.old(f"P{epsilon}-target-w-normal-coordinates")
                assert coords[1] == [S.element(x) for x in target_w["target_w_normal_coordinates_mod_prime"]]
            return {"endpoint":epsilon,"normal_columns":[first,stop],
                "absolute_rho_precision":T,"shared_denominator_order":d,
                "source_complete_cofactor_block":cofactor_ref,
                "source_shared_r0_adjugate":self.refs[f"P{epsilon}-shared-r0-adjugate"],
                "source_shared_r0_unit_inverse":self.refs[f"P{epsilon}-shared-r0-unit-inverse"],
                "source_original_normal_order":plain(self.inputs["endpoints"][str(epsilon)]["normal_order"]),
                "normal_values_in_original_endpoint_order_mod_prime":[vec_pack(S,x) for x in coords],
                "all_low_numerator_coefficients_below_shared_d_vanish":True,
                "actual_low_coefficients_checked":(stop-first)*DIM*d,
                "all_complete8_r0_times_gamma_equals_ri_equations_verified":True,
                "gamma0_and_gamma1_checked_when_present":first==0,
                "exact_source_expression":"r_i(U,V)/r_0(U,V), with original polynomial row",
                "characteristic_zero_expanded_coordinates":False,
                "source_normal_basis_and_original_t_frame_unchanged":True}
        return self.stage(name,produce)

    def verify_all(self, epsilon, normal_refs, operators, T):
        S = self.H.SeriesRing(T)
        gamma = []
        for blockref in normal_refs:
            value = read(self.out/blockref["file"])
            assert spec(self.out/blockref["file"]) == plain(blockref)
            assert value["configuration"] == self.tag and value["complete"] is True
            first,stop = value["normal_columns"]
            assert first == len(gamma) and value["absolute_rho_precision"] == T
            gamma.extend([S.element(x) for x in row]
                         for row in value["normal_values_in_original_endpoint_order_mod_prime"])
        assert len(gamma) == NORMAL
        flat = nmod_mat([[int(row[i][n]) for i in range(DIM) for n in range(T)]
                         for row in gamma],PRIME).transpose()
        products = []
        for degree in range(4):
            name = f"P{epsilon}-normal-times-original-W-{degree}"
            def produce(degree=degree):
                self.budget()
                value = (flat*self.Wmat[degree]).transpose()
                return {"endpoint":epsilon,"absolute_rho_precision":T,"W_power":degree,
                    "source_normal_coordinate_blocks":normal_refs,
                    "source_original_W":self.inputs["original_W"],
                    "coefficient_order":"normal component, then endpoint basis, then rho degree",
                    "products_flat_mod_prime":[[int(value[j,i]) for i in range(DIM*T)]
                                              for j in range(NORMAL)],
                    "all272_original_columns_used":True}
            products.append(self.stage(name,produce))
        def complete():
            MU = mat_read(S,operators["multiplication_by_target_U"])
            MV = mat_read(S,operators["multiplication_by_target_V"])
            for j in range(NORMAL):
                self.budget()
                answer = [S.zero for _ in range(DIM)]
                for degree in (3,2,1,0):
                    row = products[degree]["products_flat_mod_prime"][j]
                    coefficient = [S.element(row[i*T:(i+1)*T]) for i in range(DIM)]
                    answer = vec_add(S,mat_vec(S,MU,answer),coefficient)
                assert answer == mat_vec(S,MV,gamma[j]),("original_gamma_W_equals_V_gamma",epsilon,j)
            return {"endpoint":epsilon,"absolute_rho_precision":T,
                "source_normal_coordinate_blocks":normal_refs,
                "source_target_operators":self.refs[f"P{epsilon}-integral-target-multiplication-operators"],
                "source_original_W":self.inputs["original_W"],
                "source_four_original_coefficient_products":[self.refs[f"P{epsilon}-normal-times-original-W-{d}"]
                                                               for d in range(4)],
                "all272_original_target_equations_verified":True,
                "all8_series_coordinates_of_every_equation_checked":True,
                "all_factors_and_nilpotents_retained":True,
                "no_characteristic_zero_coordinate_reconstruction_claimed":True}
        return self.stage(f"P{epsilon}-all272-original-normal-equations",complete)

    def endpoint(self, epsilon):
        certname = f"P{epsilon}-complete-target-normal-coordinate-certificate"
        done = self.old(certname)
        if done is not None:
            self.endpoints[str(epsilon)] = self.refs[certname]
            return done
        w = self.target_w(epsilon)
        operators = self.target_operators(epsilon,w)
        R,powers,power_refs = self.powers(epsilon,operators)
        self.target_characteristic(epsilon,operators,R,powers,power_refs)
        prefixes = {}
        head,headref = self.cofactor_block(epsilon,0,operators,R,powers,power_refs,prefixes)
        shared,inverse = self.shared_denominator(epsilon,head,headref,R)
        normal_refs,cofactor_refs = [],[]
        for first in range(0,NORMAL,COLUMN_BLOCK):
            self.budget()
            if first == 0:
                block,ref = head,headref
            else:
                block,ref = self.cofactor_block(epsilon,first,operators,R,powers,power_refs,prefixes)
            self.normalize_block(epsilon,first,block,ref,shared,inverse)
            stop = min(NORMAL,first+COLUMN_BLOCK)
            normal_refs.append(self.refs[f"P{epsilon}-target-normal-{first:03d}-{stop:03d}"])
            cofactor_refs.append(ref)
        prefixes.clear()
        T = inverse["output_absolute_rho_precision"]
        self.verify_all(epsilon,normal_refs,operators,T)
        def certificate():
            source_refs = self.inputs["endpoints"][str(epsilon)]
            return {"endpoint":epsilon,"prime":PRIME,"original_zeta_root":ZETA,"original_s_root":SROOT,
                "local_parameter":STRATEGY["endpoint_parameters"][epsilon],
                "source_original_order_certificate":plain(source_refs["certificate"]),
                "source_original_normal_order":plain(source_refs["normal_order"]),
                "source_original_special_fibre":plain(source_refs["special_fibre"]),
                "source_original_primitive_and_t_frames":plain(source_refs["frame"]),
                "target_w":self.refs[f"P{epsilon}-target-w-normal-coordinates"],
                "target_operators":self.refs[f"P{epsilon}-integral-target-multiplication-operators"],
                "complete_cofactor_blocks":cofactor_refs,
                "complete_target_normal_coordinate_blocks":normal_refs,
                "shared_r0_adjugate":self.refs[f"P{epsilon}-shared-r0-adjugate"],
                "shared_r0_unit_inverse":self.refs[f"P{epsilon}-shared-r0-unit-inverse"],
                "target_characteristic_equation":self.refs[f"P{epsilon}-original-target-characteristic-relation"],
                "all_original_normal_equations":self.refs[f"P{epsilon}-all272-original-normal-equations"],
                "actual_target_w_precision":267,
                "actual_shared_denominator_order":inverse["actual_determinant_order"],
                "actual_target_normal_coordinate_precision":T,
                "all272_original_target_normal_coordinates_computed":True,
                "all272_by8_series_original_equations_verified":True,
                "complete_length8_endpoint_algebra_and_nilpotents_retained":True,
                "original_basis_parameter_nu_and_dual7_frames_preserved":True,
                "characteristic_zero_expanded_coordinates":False,
                "target_ideal_NormPhi_reference_or_height_evaluated":False}
        done = self.stage(certname,certificate)
        self.endpoints[str(epsilon)] = self.refs[certname]
        self.checkpoint()
        return done

    def inventory(self):
        files = []
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name in (CURRENT,INVENTORY):
                continue
            value = read(path)
            assert value["result"] == RESULT and value["configuration"] == self.tag
            assert value["complete"] is True
            files.append(spec(path))
        save(self.out/INVENTORY,{"result":RESULT,"configuration":self.tag,"complete":True,
            "files":files,"only_actual_complete_stages_listed":True,
            "current_checkpoint_excluded":True})
        return spec(self.out/INVENTORY)

    def finish(self, complete, reason=None):
        self.checkpoint(reason)
        inventory = self.inventory()
        final = {"result":RESULT,"configuration":self.tag,"complete":bool(complete),
            "p":41,"prime":PRIME,"original_zeta_root":ZETA,"original_s_root":SROOT,
            "actual_completed_endpoint_count":len(self.endpoints),
            "completed_endpoint_certificates":self.endpoints,
            "endpoint_stops":self.endpoint_stops,"stop_reason":reason,
            "source_identities":{k:source_identity(self.item["sources"][k]) for k in SOURCES},
            "source_audit":self.refs.get("source-audit"),
            "requested_minimum_output_precision":self.item["requested_minimum_output_precision"],
            "actual_original_two_endpoint_target_normal_coordinates_certified":bool(complete),
            "actual_full_length8_endpoint_algebras_preserved":bool(complete),
            "original_R917_orders_and_frames_recomputed":False,
            "original_W_charpoly_adjugate_273nodes_or_2058_solve_recomputed":False,
            "characteristic_zero_expanded_target_coordinates":False,
            "five_target_endpoint_ideal_lattices_computed":False,
            "P0_endpoint_numeric_Norm_calibration_computed":False,
            "P1_endpoint_numeric_Norm_calibration_computed":False,
            "NmPhi_detU_and_reference_original_frames_evaluated":False,
            "Hecke_Picard_active_support_or_height_computed":False,
            "future_target_sources":{"R903":None,"R907":None},
            "stage_manifest":inventory,"resume_state":self.current,
            "seconds":time.monotonic()-self.started}
        save(self.out/FINAL,final)
        return final

    def run(self):
        for epsilon in (0,1):
            try:
                self.endpoint(epsilon)
                self.endpoint_stops.pop(str(epsilon),None)
            except self.H.NeedPrecision as exc:
                self.endpoint_stops[str(epsilon)] = exc.to_data()
                self.active = None
                self.checkpoint(exc.to_data())
                print("R923_ENDPOINT_NEED_PRECISION="+json.dumps(
                    {"endpoint":epsilon,**exc.to_data()},sort_keys=True),flush=True)
        done = len(self.endpoints)==2
        return self.finish(done,None if done else
            {"kind":"NeedPrecision","endpoints":self.endpoint_stops,
             "zero_truncation_not_exact_zero":True})


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New R923 mathematical arithmetic is allowed only in the original public repository Actions")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser()
    parser.add_argument("--config",required=True)
    parser.add_argument("--out",required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args = parser.parse_args()
    out = Path(args.out);out.mkdir(parents=True,exist_ok=True)
    started = time.monotonic();job=None;code=1;error=None;certificate=None
    try:
        job = Job(args)
        certificate = job.run()
        code = 0 if certificate["complete"] else 2
        error = certificate["stop_reason"]
    except Exception as exc:
        traceback.print_exc()
        if job is not None and isinstance(exc,job.H.NeedPrecision):
            error,code = exc.to_data(),2
        elif isinstance(exc,BudgetStop):
            error,code = {"kind":"BudgetStop","reason":str(exc)},2
        else:
            error = {"kind":type(exc).__name__,"reason":str(exc)}
        if job is not None:
            certificate = job.finish(False,error)
    receipt = {"result":RESULT,"source_sha256":sha(__file__),"complete":code==0,
        "process_exit_code":code,"error":error,"seconds":time.monotonic()-started,
        "configuration_sha256":None if job is None else fingerprint(job.tag),
        "certificate_sha256":sha(out/FINAL) if (out/FINAL).exists() else None,
        "stage_manifest":None if certificate is None else certificate["stage_manifest"],
        "actual_completed_endpoint_count":0 if certificate is None else certificate["actual_completed_endpoint_count"],
        "actual_original_two_endpoint_target_normal_coordinates_certified":code==0,
        "endpoint_target_NormPhi_frames_or_height_computed":False}
    save(out/"core-receipt.json",receipt)
    print("R923_TARGET_CORE_RECEIPT="+json.dumps(receipt,sort_keys=True),flush=True)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
