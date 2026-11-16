#!/usr/bin/env python3
"""R905/R909: seven actual bounded-divisor connections and five exact I_Z DAGs.

Numerical arithmetic is only the new auxiliary-place unit charts.  Exact
characteristic-zero objects remain source-bound unit-solve expressions.
"""
import argparse
import gc
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import traceback

import flint
import R905_trace_dual_linear_algebra as A

REPOSITORY = "Rogerhu12/math-research-public"
RESULT = "R905-original-seven-bounded-divisor-connections-and-five-Picard-inputs"
FINAL = "p41-original-seven-bounded-divisor-connections-and-five-Picard-inputs-certificate.json"
PREFIX = "R905-"
MANIFEST = "full-outputs-manifest.json"
P, N, EPS = A.P, A.N, A.EPS
GROUPS = ("R896", "R894", "R872", "R827", "GLOBAL", "R883")
LABELS = ("D1", "D2", "D3", "D4", "D5", "X", "DN")
POWERS = (12, 8, 8, 13, 14)
DEGREES = (2970, 1674, 1800, 3024, 3339)
P_NUMERATORS = (165, 93, 100, 168, 371)
Q_DENOMINATORS = (67, 67, 67, 67, 134)
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
STRATEGY = {
    "original_curve": "original level82 minus3 twist Y, genus127, p41",
    "prime": P, "normal_basis_degrees": EPS,
    "original_s_root": 99932770, "original_zeta_root": 549966761,
    "original_integral_B_root": 3197390,
    "source_divisor_order": list(LABELS),
    "complete_source_spaces": "five R896 W_Dj, R872 W_X, R894 W_DN; each H0(3H-D), dimension418",
    "U_source": "new exact kernel of each final W_D modulo V2; never an unrelated old flip146",
    "bundle_source_weights": [1]*146+[0]*126,
    "bundle_auxiliary_schedule": "z=a, a=0,1,2,...; first actual complete272 unit graph",
    "bundle_complement": "first independent columns of [U_D(a),W_D(a)] after all146 U columns",
    "full_differential_basis": "(z-a)^k theta_i dz, k<=2-column_weight_i; length670",
    "full_principal_parts": "V3/(tau U_D), length544, perfect residue pairing including intersections and nilpotents",
    "principal_part_entry": "-[u^(2-k)](F(a+u)^-1 p_s(a+u))_i",
    "only_new_inverse_jets": [1,2], "existing_F0_inverse_recomputed": False,
    "target": "whole Artin trace on H minus whole Artin trace on D",
    "H_trace": "one common trace row; h_a restricts to sigma on H for every a",
    "primitive_section": "s_n=sum_(i=0)^145 n^i ell_i, original normal V1 basis, n=1,2,...",
    "primitive_whole_algebras": "dimension272, no support reduction or factor peeling",
    "new_weight1_multiplier_nodes": [0,1,2,3],
    "old_W_Krylov_inverses_or_273_point_charpoly_recomputed": False,
    "new_weight1_multiplier_bound": "degree(M_s)_ij<=1+epsilon_j-epsilon_i<=3",
    "target_trace_method": "actual full cyclic unit basis, complete companion relation and Newton trace identities",
    "principal_parts_rank": 543,
    "connection_gauge": "first canonical543 row/column unit chart, other127 coefficients zero",
    "characteristic_zero_solution": "same exact selected system; full image follows complete residue theorem, plus all544 modular rows verified",
    "special_case": "no characteristic-zero h0=1 claim from a modular kernel; preserve failure and explicit finite fallback contract",
    "seven_source_transport": "q sum_sigma alpha_Dj+7q(n-2)alpha_X-p average_sigma(alpha_DN-dlog QN)-q dlog Norm(Qj)",
    "true_Q_descent": "(alpha+cY(alpha))/2; cY(z)=z-2 adj(TI-W)0,72/adj(TI-W)0,0; cY(w)=w; cY(s)=-s",
    "original_nu_fixed": True,
    "original_principal_units_and_P0_t_frame_retained": True,
    "Hecke_calibration_nonp_period_or_height_computed": False,
    "only_budget_and_finite_search_scope_excluded_from_identity": True,
}


class BudgetStop(RuntimeError):
    pass


class ScopeStop(RuntimeError):
    pass


def guard():
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == REPOSITORY


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as f:
        return json.load(f)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_bytes(gzip.compress(data, mtime=0) if path.suffix == ".gz" else data)
    temporary.replace(path)


def plain(row):
    output = {k: row[k] for k in ("file", "bytes", "sha256")}
    assert Path(output["file"]).name == output["file"] and "\\" not in output["file"]
    return output


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def identity(source):
    out = {k: source[k] for k in BASE}
    out["configuration_sha256"] = source["configuration_sha256"]
    out["selected_files_sha256"] = fingerprint(source["files"])
    out["stage_result_location"] = source["stage_result_location"]
    for key in ("certificate", "configuration_stage"):
        if source.get(key) is not None:
            out[key] = plain(source[key])
    return out


def expected_tag(item):
    return {"result": RESULT, "source_sha256": item["core_sha256"],
            "python_flint": "0.9.0", "p": 41,
            "method_sha256": item["method_sha256"], "proofs": item["proofs"],
            "linear_algebra_helper_sha256": item["linear_algebra_helper_sha256"],
            "sources": {g: identity(item["sources"][g]) for g in GROUPS},
            "inputs": item["inputs"], "strategy": STRATEGY}


class Source:
    def __init__(self, group, item, root):
        self.group, self.item = group, item
        self.folder = Path(root)/group
        self.files = {name: plain(row) for name, row in item["files"].items()}
        self.checked = set()
        assert spec(self.folder/MANIFEST) == self.files[MANIFEST]
        assert self.files[MANIFEST]["sha256"] == item["manifest_sha256"]
        manifest = read(self.folder/MANIFEST)
        assert manifest["result"] == item["result"]
        indexed = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(indexed) == len(manifest["files"])
        indexed[MANIFEST] = self.files[MANIFEST]
        for name, row in self.files.items():
            assert name == row["file"]
            if name != "full-outputs-manifest-reference.json":
                assert indexed[name] == row, (group, name)
        initial = self.raw("public-actions-input.json")
        run = self.raw("run-receipt.json")
        assert initial["source_commit"] == run["source_commit"] == item["source_commit"]
        assert str(run["workflow_run_id"]) == str(item["run_id"])
        assert initial.get("core_sha256", initial.get("job", {}).get("core_sha256")) == item["core_sha256"]
        self.certificate = None
        if item.get("certificate") is not None:
            self.certificate = self.raw(item["certificate"]["file"])
            assert self.files[item["certificate"]["file"]] == plain(item["certificate"])
            assert self.certificate["result"] == item["result"] and self.certificate["complete"] is True
            assert run["complete"] is True and run["process_exit_code"] == 0
            self.tag = self.certificate["configuration"]
        else:
            assert group == "R827" and run["complete"] is False
            assert run["process_exit_code"] in item["accepted_process_exit_codes"]
            assert 0 not in item["accepted_process_exit_codes"]
            anchor = self.raw(item["configuration_stage"]["file"])
            assert anchor["complete"] is True
            self.tag = anchor["configuration"]
        assert fingerprint(self.tag) == item["configuration_sha256"]
        assert self.tag.get("source_sha256", self.tag.get("core_sha256")) == item["core_sha256"]
        assert self.tag["result"] == item["result"]
        assert item["stage_result_location"] == ("configuration" if group == "R827" else "top_level")
        if run.get("core_receipt_sha256") is not None:
            assert self.files["core-receipt.json"]["sha256"] == run["core_receipt_sha256"]
            receipt = self.raw("core-receipt.json")
            assert receipt["source_sha256"] == item["core_sha256"]
            if receipt.get("configuration") is not None:
                assert receipt["configuration"] == self.tag
            if receipt.get("configuration_sha256") is not None:
                assert receipt["configuration_sha256"] == item["configuration_sha256"]
            if self.certificate is not None:
                assert receipt["complete"] is True
                assert receipt["certificate_sha256"] == item["certificate"]["sha256"]

    def raw(self, name):
        if name not in self.checked:
            assert spec(self.folder/name) == self.files[name], (self.group, name)
            self.checked.add(name)
        return read(self.folder/name)

    def stage(self, row):
        assert self.files[row["file"]] == plain(row)
        value = self.raw(row["file"])
        assert value["complete"] is True and value["configuration"] == self.tag
        if self.item["stage_result_location"] == "configuration":
            assert "result" not in value and value["configuration"]["result"] == self.item["result"]
        else:
            assert value.get("result") == self.item["result"], (self.group, row["file"], "stage_result")
        return value


class Job:
    def __init__(self, args):
        self.args, self.started = args, time.monotonic()
        self.item = read(args.config)
        self.out = Path(args.output)
        self.out.mkdir(parents=True, exist_ok=True)
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert self.item["producer_inputs_pending"] is False
        assert sha(__file__) == self.item["core_sha256"] and flint.__version__ == "0.9.0"
        topic = Path(__file__).resolve().parent.parent
        assert sha(topic/self.item["method"]) == self.item["method_sha256"]
        assert sha(topic/self.item["linear_algebra_helper"]) == self.item["linear_algebra_helper_sha256"]
        assert Path(A.__file__).resolve() == (topic/self.item["linear_algebra_helper"]).resolve()
        for proof in self.item["proofs"].values():
            assert sha(topic/proof["path"]) == proof["sha256"]
        assert set(self.item["sources"]) == set(GROUPS)
        self.tag = expected_tag(self.item)
        self.refs, self.done, self.unresolved = {}, {}, {}
        self.current = None
        self.phase, self.active = "source_initialization", None
        self.inputs = self.item["inputs"]
        self.sources = {g: Source(g, self.item["sources"][g], args.retained) for g in GROUPS}
        self.max_nodes = int(self.item.get("maximum_auxiliary_fibres", 8))
        self.max_parameters = int(self.item.get("maximum_primitive_trials", 8))
        self.max_divisors = int(self.item.get("maximum_divisors", 7))
        assert 1 <= self.max_nodes <= 273 and 1 <= self.max_parameters < P
        assert 1 <= self.max_divisors <= 7
        self.V2, self.V3 = A.positions(2), A.positions(3)
        self.ix2, self.ix3 = {p:i for i,p in enumerate(self.V2)}, {p:i for i,p in enumerate(self.V3)}
        self.fibres, self.spaces, self.marked, self.multiplier_cache = {}, {}, {}, {}

    def budget(self):
        if time.monotonic()-self.started >= self.args.budget_minutes*60-30:
            raise BudgetStop("All complete R905 stages retained; phase="+self.phase)

    def path(self, name):
        assert Path(name).name == name
        return self.out/(PREFIX+name+".json.gz")

    def old(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["result"] == RESULT and value["configuration"] == self.tag and value["complete"] is True
        self.refs[name] = spec(path)
        return value

    def put(self, name, value):
        assert not set(value) & {"result", "configuration", "complete"}
        output = {"result": RESULT, "configuration": self.tag, "complete": True, **value}
        path = self.path(name)
        if path.exists():
            assert read(path) == output
        else:
            save(path, output)
        self.refs[name] = spec(path)
        print("R905_STAGE="+json.dumps({"file": path.name, "seconds": time.monotonic()-self.started}), flush=True)
        return output

    def ref(self, name):
        return self.refs[name]

    def checkpoint(self, phase):
        self.phase = phase
        save(self.path("current"), {"result": RESULT, "configuration": self.tag, "complete": False,
             "phase": phase, "active_divisor": self.active, "completed_connections": self.done,
             "unresolved_divisors": self.unresolved, "complete_stages": self.refs})
        self.current = spec(self.path("current"))

    def source(self, row):
        return self.sources[row["source_group"]].stage(row)

    def input(self, name):
        return self.source(self.inputs[name])

    def own(self, row):
        path = self.out/row["file"]
        assert spec(path) == plain(row)
        value = read(path)
        assert value["complete"] is True and value["configuration"] == self.tag and value["result"] == RESULT
        return value

    def prepare(self):
        self.budget()
        assert self.sources["R896"].certificate["all_five_complete_low_weight_RR_spaces_certified"] is True
        assert self.sources["R894"].certificate["actual_original_seven_pole_trace_bounded_identity_certified"] is True
        self.global_graph = self.input("global_function_DAG")
        assert self.global_graph["global_y_exact_unit_expression_defined"] is True
        assert self.global_graph["original_eta_Picard_input_DAGs_defined"] is True
        nodes = {v["id"]:v for v in self.global_graph["graph_nodes"]}
        assert len(nodes) == len(self.global_graph["graph_nodes"])
        self.sigma_node = nodes[self.global_graph["original_Galois_automorphism_node"]]
        assert self.sigma_node["operation"] == "original_Galois_automorphism_definition"
        assert self.sigma_node["data"]["fixes_zeta"] is True
        assert self.sigma_node["data"]["fixes_original_z_w_and_normal_basis"] is True
        self.frame = self.input("original_t_frame")
        assert self.frame["original_t_first_order_unit_certified"] is True
        assert self.frame["original_t_over_rho_constant_mod_prime"] == 354813668
        assert self.frame["original_s_root"] == 99932770
        assert set(self.inputs["divisors"]) == set(LABELS)
        for label in LABELS:
            entries = self.inputs["divisors"][label]
            space = self.source(entries["space"])
            certificate = self.source(entries["certificate"])
            principal = self.source(entries["principal"])
            assert space["prime"] == P
            key = "V3_kernel_basis_mod_prime" if label == "X" else "normal_V3_basis_mod_prime"
            A.shape(space[key], 690, 418)
            if label == "X":
                assert entries["space"]["source_group"] == "R872"
                assert space["full_characteristic_zero_dimension"] == 418
                assert space["all1234_by418_complete_V5_relations_zero"] is True
                assert space["normal_integer_scale_applied_again"] is False
            else:
                assert space["normal_V3_basis"] == [list(p) for p in self.V3]
                assert space["complete_RR_space_certified"] is True
                assert space["actual_projected_rank"] == 418
                if label == "DN":
                    assert entries["space"]["source_group"] == "R894"
                    assert certificate["effective_degree272_and_original_P0_avoidance_certified"] is True
                    assert plain(certificate["complete_normal418_space"]) == plain(entries["space"])
                    assert principal["DN_effective_degree"] == 272 and principal["DN_avoids_original_P0"] is True
                    assert principal["actual_rho_order"] == -8435
                    assert principal["exact_original_divisor_identity"] == "T_f^0=(D_N-H)+div(Q_N)"
                    assert plain(principal["source_complete_DN_normal418"]) == plain(entries["space"])
                else:
                    j = int(label[1:])
                    assert entries["space"]["source_group"] == "R896"
                    assert certificate["complete_characteristic_zero_H0_3H_minus_Dstd_certified"] is True
                    assert certificate["Dstd_effective_degree272_and_avoids_original_P0"] is True
                    assert plain(certificate["complete_normal_V3_space"]) == plain(entries["space"])
                    assert principal["j"] == j and principal["Dstd_degree"] == 272
                    assert principal["ordinary_power"] == POWERS[j-1]
                    assert principal["original_pole_degree"] == DEGREES[j-1]
                    assert principal["actual_Q_rho_order"] == principal["actual_Q_t_order"] == 1-DEGREES[j-1]
                    assert principal["original_fixed_chi_sign_is_negative_power_in_Q"] is True
                    assert plain(principal["complete_normal418_space"]) == plain(entries["space"])
                    old = self.global_graph["five_original_polar_and_eta_outputs"][str(j)]
                    assert old["original_Hom_word"] == "1+T^"+str(j)
                    assert old["original_map_degree"] == DEGREES[j-1]
                    assert old["p"] == P_NUMERATORS[j-1] and old["q"] == Q_DENOMINATORS[j-1]
                    assert principal["original_E_definition"] == old["global_pole_ideals"]
            self.spaces[label] = A.mat(space[key])
            self.marked[label] = principal
        original = self.input("original_W")
        assert original["prime"] == P and original["original_rational_denominators_all_units"] is True
        assert original["original_primitive_coordinate_solutions_not_recomputed"] is True
        assert self.sources["R827"].tag["normal_basis_degrees"] == EPS
        for a in range(4):
            ref = self.inputs["original_Krylov_points"][str(a)]
            point = self.source(ref)
            assert point["prime"] == P and point["z0"] == a and point["usable"] is True
            assert point["actual_cyclic_rank"] == 272 and point["both_inverse_products_verified"] is True
            assert plain(point["source_original_W"]) == plain(self.inputs["original_W"])
            for key in ("W_evaluated_mod_prime", "Krylov_matrix_mod_prime", "inverse_Krylov_matrix_mod_prime"):
                A.shape(point[key], N, N)
            self.fibres[a] = {"W": A.mat(point["W_evaluated_mod_prime"]),
                              "K": A.mat(point["Krylov_matrix_mod_prime"]),
                              "Ki": A.mat(point["inverse_Krylov_matrix_mod_prime"]), "source": ref}
        name = "original-source-audit"
        if self.old(name) is None:
            self.put(name, {"sources": {g:identity(self.item["sources"][g]) for g in GROUPS},
                "inputs": self.inputs, "prime": P, "original_normal_basis_degrees": EPS,
                "seven_actual_complete_H0_3H_minus_D418_spaces_consumed": True,
                "source_DN_not_assumed_K_fixed": True,
                "all_original_unscaled_Qj_QN_and_t_frame_sources_retained": True,
                "original_W_Krylov_and_inverses_not_recomputed": True,
                "original_Gamma_B_derivatives_charpoly_or_RR418_not_recomputed": True,
                "all_new_mathematics_only_in_public_Actions": True})
        self.checkpoint("original-sources-complete")

    def U_space(self, label):
        stem = label+"-same-divisor-U146"
        old = self.old(stem)
        if old is None:
            self.budget()
            W = self.spaces[label]
            high = [i for i, (row, k) in enumerate(self.V3) if k == 3-EPS[row]]
            M = A.sub(W, high, list(range(418)))
            rank, pivots, free, K = A.canonical_kernel(M)
            if rank != 272:
                self.put(stem+"-nonunit", {"source_original_W_D": self.inputs["divisors"][label]["space"],
                    "prime": P, "matrix_shape": [272,418], "actual_rank": rank,
                    "required_rank": 272, "source_characteristic_zero_space_disproved": False})
                raise ScopeStop(label+": same-D truncation chart is not a unit at this place")
            square = A.sub(M, list(range(272)), pivots)
            determinant = int(square.det())
            assert determinant != 0 and len(free) == 146
            U3 = W*K
            assert A.sub(U3, high, list(range(146))) == A.zero(272,146)
            low = [self.ix3[pos] for pos in self.V2]
            U = A.sub(U3, low, list(range(146)))
            projection_rank, I = A.independent_rows(U, 146)
            assert projection_rank == 146
            selected = A.sub(U, I, list(range(146)))
            inverse = selected.inv()
            assert selected*inverse == inverse*selected == A.eye(146)
            normalized = U*inverse
            assert A.sub(normalized, I, list(range(146))) == A.eye(146)
            old = self.put(stem, {"prime": P, "label": label,
                "source_original_final_418_space": self.inputs["divisors"][label]["space"],
                "source_original_divisor_certificate": self.inputs["divisors"][label]["certificate"],
                "high_normal_V3_rows": high, "truncation_matrix_mod_prime": A.rows(M),
                "actual_truncation_rank": 272, "selected_pivot_columns": pivots, "free_columns": free,
                "actual_truncation_minor_determinant_mod_prime": determinant,
                "free_identity_kernel_mod_prime": A.rows(K), "all272_by146_truncation_relations_verified": True,
                "V2_identity_rows": I, "projection_inverse_mod_prime": A.rows(inverse),
                "both_projection_inverse_products_verified": True,
                "normal_V2_basis": [list(p) for p in self.V2],
                "normal_V2_basis_mod_prime": A.rows(normalized),
                "exact_unit_solve_expression": {
                    "source_complete_W_D": self.inputs["divisors"][label]["space"],
                    "truncation_rows": high, "pivot_columns": pivots, "free_columns": free,
                    "kernel": "pivot=-M[:,J]^-1*M[:,F], free=identity",
                    "normalization": "right multiply inverse of the selected V2 rows",
                    "selected_normalization_rows": I,
                    "RR_proof_gives_exact_rank272_and_dimension146": self.item["proofs"]["R905"]},
                "exact_complete_space": "H0(2H-D), for this same final source D",
                "previous_flip_146_space_not_assumed_to_have_this_divisor": True,
                "characteristic_zero_coordinates_expanded": False})
            self.checkpoint(stem)
        assert old["source_original_final_418_space"] == self.inputs["divisors"][label]["space"]
        A.shape(old["normal_V2_basis_mod_prime"],418,146)
        return A.mat(old["normal_V2_basis_mod_prime"]), old["V2_identity_rows"], self.ref(stem)

    def bundle(self, label, U, Uref):
        name = label+"-complete-bundle-unit-graph"
        old = self.old(name)
        if old is None:
            Ucoef = A.coefficient_matrices(U,2)
            Wcoef = A.coefficient_matrices(self.spaces[label],3)
            for a in range(self.max_nodes):
                trialname = label+f"-bundle-node-{a:06d}-profile"
                trial = self.old(trialname)
                if trial is None:
                    self.budget()
                    U0, W0 = A.evaluate(Ucoef,a), A.evaluate(Wcoef,a)
                    ur, urank = U0.rref()
                    joined = A.hcat(U0,W0)
                    reduced, rank = joined.rref()
                    selected = A.pivot_columns(reduced,rank)
                    accepted = urank == 146 and rank == 272 and selected[:146] == list(range(146))
                    trial = self.put(trialname, {"prime":P,"label":label,"z0":a,
                        "source_same_D_U146":Uref,
                        "source_original_W_D":self.inputs["divisors"][label]["space"],
                        "actual_U_fibre_rank":urank,"actual_joined_fibre_rank":rank,
                        "selected_joined_columns":selected,"actual_unit_graph_candidate":accepted,
                        "whole_fibre_dimension":272,"single_point_or_reduced_support_used":False,
                        "nonunit_does_not_assert_characteristic_zero_h0_H_minus_D_equal_one":not accepted})
                    self.checkpoint(trialname)
                if not trial["actual_unit_graph_candidate"]:
                    continue
                selected = [j-146 for j in trial["selected_joined_columns"][146:]]
                assert len(selected)==126 and selected==sorted(set(selected))
                F = [A.hcat(Ucoef[k] if k<len(Ucoef) else A.zero(N,146),
                            A.sub(Wcoef[k],list(range(N)),selected)) for k in range(4)]
                F0 = A.evaluate(F,a)
                determinant = int(F0.det())
                assert determinant != 0
                inverse = F0.inv()
                assert F0*inverse == inverse*F0 == A.eye(N)
                old = self.put(name,{"prime":P,"label":label,"auxiliary_z":a,
                    "source_same_D_U146":Uref,
                    "source_original_W_D":self.inputs["divisors"][label]["space"],
                    "source_actual_fibre_profile":self.ref(trialname),
                    "selected_original_W_columns":selected,"column_weights":[1]*146+[0]*126,
                    "F_coefficients_low_to_high": [A.rows(x) for x in F],
                    "F_at_auxiliary_fibre_mod_prime":A.rows(F0),
                    "inverse_F_at_auxiliary_fibre_mod_prime":A.rows(inverse),
                    "actual_F_determinant_mod_prime":determinant,
                    "both_F_inverse_products_verified":True,
                    "full_rank272_equal_degree146_bundle_isomorphism_certified":True,
                    "D_and_H_disjoint_from_whole_auxiliary_fibre_certified":True,
                    "h0_H_minus_D_zero_follows_from_actual_unit_graph":True,
                    "trace_dual_differential_space_dimension":670,
                    "exact_unit_graph_expression":{
                        "first146_columns":Uref,"last126_columns":self.inputs["divisors"][label]["space"],
                        "selected_original_last_columns":selected,
                        "original_tau_normal_frame":True,
                        "equal_degree_global_isomorphism_proof":self.item["proofs"]["R905"]},
                    "characteristic_zero_coefficients_expanded":False})
                self.checkpoint(name)
                break
            if old is None:
                failure = label+"-unit-graph-scope-stop"
                # A later larger scope must not be bound to an earlier false endpoint.
                suffix = fingerprint({"count":self.max_nodes})[:16]
                self.put(failure+"-"+suffix,{"prime":P,"label":label,"attempted_node_count":self.max_nodes,
                    "source_same_D_U146":Uref,
                    "actual_unit_graph_observed":False,
                    "special_characteristic_zero_principal_case_claimed":False,
                    "finite_fallback_contract":{
                        "exact_special_case":"only an accurately certified h with div(h)=D-H permits -dlog(h)",
                        "otherwise":"the R905 two-chart complete polynomial-module fallback, with all relations retained",
                        "no_bad_factor_or_failed_fibre_discarded":True},
                    "no_false_connection_certificate_issued":True})
                raise ScopeStop(label+": no complete bundle unit graph in the retained node prefix")
        return [A.mat(x) for x in old["F_coefficients_low_to_high"]], A.mat(old["inverse_F_at_auxiliary_fibre_mod_prime"]), old["auxiliary_z"], self.ref(name)

    def common_multiplier(self, parameter):
        if parameter in self.multiplier_cache:
            return self.multiplier_cache[parameter]
        name = f"weight1-parameter-{parameter:08d}-global-multiplier"
        old = self.old(name)
        if old is None:
            values, references = [], []
            for a in range(4):
                pointname = f"weight1-parameter-{parameter:08d}-old-node-{a:02d}"
                point = self.old(pointname)
                if point is None:
                    self.budget()
                    fibre = self.fibres[a]
                    v = A.weight_one_fibre_vector(parameter,a)
                    value = A.multiplier_at_original_cyclic_point(fibre["W"],fibre["K"],fibre["Ki"],v,self.budget)
                    point = self.put(pointname,{"prime":P,"z0":a,"parameter":parameter,
                        "source_original_W":self.inputs["original_W"],
                        "source_original_complete_Krylov_point":fibre["source"],
                        "new_section":"sum_(i=0)^145 parameter^i ell_i, original normal V1 sections",
                        "original_normal_V1_basis":[list(p) for p in A.positions(1)],
                        "new_section_value_mod_prime":A.rows(v),
                        "new_weight1_multiplier_mod_prime":A.rows(value),
                        "new_multiplier_times_old_K_equals_new_power_columns":True,
                        "new_multiplier_first_column_is_actual_section":True,
                        "new_multiplier_commutes_with_original_W":True,
                        "old_K_W_or_inverse_recomputed":False,
                        "complete_272_dimensional_fibre_retained":True})
                    self.checkpoint(pointname)
                assert point["source_original_complete_Krylov_point"]==self.fibres[a]["source"]
                values.append(A.mat(point["new_weight1_multiplier_mod_prime"]))
                references.append(self.ref(pointname))
            self.budget()
            coefficients = A.interpolate_four(values,list(range(4)))
            old = self.put(name,{"prime":P,"parameter":parameter,
                "source_complete_four_nodes":references,
                "source_original_function_field":self.inputs["global_function_DAG"],
                "coefficient_matrices_low_to_high":[A.rows(x) for x in coefficients],
                "actual_weighted_degree_bound":"1+epsilon_input-epsilon_output",
                "all_four_complete_node_matrices_multiplied_back":True,
                "all_original_weighted_support_zeros_verified":True,
                "exact_characteristic_zero_operation":{
                    "operation":"multiply_by_original_V1_section_in_original_function_field",
                    "parameter":parameter,"normal_V1_basis":[list(p) for p in A.positions(1)],
                    "source_exact_field_DAG":self.inputs["global_function_DAG"],
                    "coefficients":"the exact integers parameter^i, no rescaling",
                    "four_point_modular_interpolation_uniqueness_proof":self.item["proofs"]["R909"]},
                "characteristic_zero_multiplier_coefficients_expanded":False,
                "old_273_node_characteristic_polynomial_or_old_multipliers_recomputed":False})
            self.checkpoint(name)
        productname = f"weight1-parameter-{parameter:08d}-times-normal-V2"
        product = self.old(productname)
        if product is None:
            self.budget()
            coefficients = [A.mat(x) for x in old["coefficient_matrices_low_to_high"]]
            T = A.weight_one_times_V2(coefficients)
            product = self.put(productname,{"prime":P,"parameter":parameter,
                "source_completed_weight1_multiplier":self.ref(name),
                "input_basis":[list(p) for p in self.V2],
                "output_basis":[list(p) for p in self.V3],
                "matrix_shape":[690,418],"multiplication_V2_to_V3_mod_prime":A.rows(T),
                "exact_operation":"the same new original weight1 section times each original normal V2 section",
                "weighted_degree_three_support_verified":True})
            self.checkpoint(productname)
        assert product["source_completed_weight1_multiplier"]==self.ref(name)
        result = (A.mat(product["multiplication_V2_to_V3_mod_prime"]),self.ref(productname))
        self.multiplier_cache[parameter] = result
        return result

    def common_H_trace(self):
        name = "common-H-complete-Artin-trace"
        old = self.old(name)
        if old is not None:
            return old,self.ref(name)
        for parameter in range(1,self.max_parameters+1):
            T,Tref = self.common_multiplier(parameter)
            trialname = f"common-H-parameter-{parameter:08d}-whole-algebra"
            trial = self.old(trialname)
            if trial is None:
                self.budget()
                M = A.H_quotient_multiplication(T)
                unit = A.mat([[int(i==0)] for i in range(N)])
                data = A.cyclic_trace(M,unit,self.budget)
                trial = self.put(trialname,{"prime":P,"parameter":parameter,
                    "source_new_weight1_product":Tref,
                    "quotient":"V2/(tau V1), represented by the272 highest normal coefficients",
                    "auxiliary_section_restriction":"h_a|H=sigma, independent of a",
                    "exact_multiplication":"s_parameter/sigma on the entire original H",
                    "nonreduced_H_and_all_ramification_multiplicities_retained":True,
                    **data})
                self.checkpoint(trialname)
            if not trial["actual_primitive_unit"]:
                continue
            self.budget()
            row = A.mat([trial["canonical_quotient_trace_row_mod_prime"]])
            full = row*A.H_test_function_map()
            old = self.put(name,{"prime":P,"source_complete_Artin_power_basis":self.ref(trialname),
                "accepted_integer_parameter":parameter,
                "canonical_quotient_trace_row_mod_prime":A.rows(row)[0],
                "all690_original_V3_test_function_traces_mod_prime":A.rows(full)[0],
                "complete_artin_algebra_length":272,
                "trace_of_unit_equals272":True,
                "same_trace_reused_for_every_D_and_every_auxiliary_a":True,
                "exact_trace_definition":{
                    "algebra":"H0(O_H), H is the original tau divisor",
                    "multiplication_source":Tref,
                    "power_basis_unit_solve":self.ref(trialname),
                    "trace_operation":"Newton traces of the exact complete companion relation",
                    "original_V3_test_functions":"s/h_a^3 restricts to s/sigma^3 on H"},
                "support_reduced_or_closed_points_split":False,
                "characteristic_zero_trace_coordinates_expanded":False})
            self.checkpoint(name)
            return old,self.ref(name)
        raise ScopeStop("No whole-H primitive unit in the retained finite section prefix")

    def local_models(self,label,U,I,Uref,F,inverse0,a,Fref):
        name = label+"-complete-quotient-and-h-division-models"
        old = self.old(name)
        if old is None:
            self.budget()
            freeD,QD,representatives = A.quotient_from_normalized_columns(U,I)
            assert len(freeD)==272
            I3 = [self.ix3[self.V2[i]] for i in I]
            assert I3==sorted(I3)
            freeP = [i for i in range(690) if i not in set(I3)]
            assert len(freeP)==544
            L,constant = A.divide_by_auxiliary_section(F,a,inverse0)
            h2 = A.auxiliary_power_vector(a,2,2)
            unitD = QD*h2
            # The full exact division has already checked all690 polynomial columns.
            old = self.put(name,{"prime":P,"label":label,"auxiliary_z":a,
                "source_same_D_U146":Uref,"source_complete_bundle_unit_graph":Fref,
                "V2_identity_rows":I,"V2_D_quotient_free_rows":freeD,
                "V3_identity_rows":I3,"V3_P_quotient_free_rows":freeP,
                "V2_D_quotient_projection_mod_prime":A.rows(QD),
                "V3_to_V2_h_division_mod_prime":A.rows(L),
                "source_F0_inverse_reused_without_recomputation":Fref,
                "W_remainder_constant_coefficients_mod_prime":A.rows(constant),
                "whole_D_algebra_unit_mod_prime":A.rows(unitD),
                "whole_D_algebra_dimension":272,"whole_D_plus_H_dimension":544,
                "all690_original_polynomial_division_identities_verified":True,
                "all146_U_relations_and272_canonical_quotient_rows_verified":True,
                "D_H_intersections_not_assumed_empty":True,
                "exact_h_division_expression":{
                    "formula":"(p_r(z)-F(z)F(a)^-1 p_r(a))/(z-a)",
                    "source_F":Fref,"source_original_U":Uref,
                    "exact_identity":"h_a*q_r=r-w_r with w_r in W_D",
                    "quotient_trivialization":"q/h_a^2 on O_D; s/h_a^3 on O_(D+H)"},
                "no_new_denominator_inverse_or_polynomial_Hermite_performed":True,
                "characteristic_zero_arrays_expanded":False})
            self.checkpoint(name)
        return old,self.ref(name)

    def principal_parts(self,label,U,Uref,F,inverse0,a,Fref,model,modelref):
        jetname = label+"-inverse-hasse-coefficients-0-through2"
        jets = self.old(jetname)
        if jets is None:
            self.budget()
            FF,G = A.inverse_hasse_three(F,a,inverse0)
            jets = self.put(jetname,{"prime":P,"label":label,"auxiliary_z":a,
                "source_existing_inverse0":Fref,
                "F_hasse_coefficients_0_through2":[A.rows(x) for x in FF],
                "new_inverse_hasse_coefficients_1_through2":[A.rows(x) for x in G[1:]],
                "both_inverse_series_products_mod_u3_verified":True,
                "zero_order_inverse_recomputed":False,
                "original_Gamma_or_derivative_of_normal_basis_computed":False,
                "hasse_convention":"ordinary coefficients of u^j, no extra factorial"})
            self.checkpoint(jetname)
        name = label+"-complete-principal-parts-544-by670"
        old = self.old(name)
        if old is None:
            self.budget()
            G = [inverse0]+[A.mat(x) for x in jets["new_inverse_hasse_coefficients_1_through2"]]
            labels,M = A.principal_part_matrix(G,a)
            U3 = A.embed(2,3)*U
            assert U3.transpose()*M == A.zero(146,670)
            freeP = model["V3_P_quotient_free_rows"]
            selected = A.sub(M,freeP,list(range(670)))
            h3 = A.auxiliary_power_vector(a,3,3)
            I3 = model["V3_identity_rows"]
            constant = A.sub(h3,freeP,[0])-A.sub(U3,freeP,list(range(146)))*A.sub(h3,I3,[0])
            assert constant.transpose()*selected == A.zero(1,670)
            old = self.put(name,{"prime":P,"label":label,"auxiliary_z":a,
                "source_complete_bundle_unit_graph":Fref,
                "source_complete_quotient_models":modelref,
                "source_three_inverse_coefficients":self.ref(jetname),
                "matrix_shape":[544,670],"matrix_mod_prime":A.rows(selected),
                "test_V3_rows":freeP,"differential_basis_indices":[list(x) for x in labels],
                "constant_function_coordinates_mod_prime":A.rows(constant),
                "all146_original_test_relations_times_all670_columns_zero":True,
                "all670_total_residues_zero_verified":True,
                "complete_principal_parts_not_residue_only":True,
                "all_nilpotents_ramification_and_D_H_intersections_preserved":True,
                "exact_matrix_definition":{
                    "entry":"-[u^(2-k)](F(a+u)^-1 p_s(a+u))_i",
                    "source_complete_F":Fref,"source_quotient_basis":modelref,
                    "global_residue_theorem_and_perfect_pairing":self.item["proofs"]["R909"],
                    "exact_image_rank_upper_bound":543},
                "characteristic_zero_matrix_expanded":False})
            self.checkpoint(name)
        return old,self.ref(name)

    def D_trace(self,label,model,modelref):
        name = label+"-complete-Artin-trace"
        old = self.old(name)
        if old is not None:
            return old,self.ref(name)
        QD = A.mat(model["V2_D_quotient_projection_mod_prime"])
        L = A.mat(model["V3_to_V2_h_division_mod_prime"])
        J = model["V2_D_quotient_free_rows"]
        unit = A.mat(model["whole_D_algebra_unit_mod_prime"])
        for parameter in range(1,self.max_parameters+1):
            T,Tref = self.common_multiplier(parameter)
            trialname = label+f"-parameter-{parameter:08d}-whole-Artin-algebra"
            trial = self.old(trialname)
            if trial is None:
                self.budget()
                M = QD*(L*A.sub(T,list(range(690)),J))
                data = A.cyclic_trace(M,unit,self.budget)
                trial = self.put(trialname,{"prime":P,"label":label,"parameter":parameter,
                    "source_complete_quotient_model":modelref,"source_new_weight1_product":Tref,
                    "exact_algebra":"H0(O_D), entire original effective degree272 divisor",
                    "exact_primitive_element":"s_parameter/h_a",
                    "exact_multiplication_formula":"Q_D*L_h*M_s*canonical_representatives",
                    **data})
                self.checkpoint(trialname)
            if not trial["actual_primitive_unit"]:
                continue
            self.budget()
            row = A.mat([trial["canonical_quotient_trace_row_mod_prime"]])
            traceV3 = row*QD*L
            old = self.put(name,{"prime":P,"label":label,
                "source_complete_Artin_power_basis":self.ref(trialname),
                "source_complete_quotient_model":modelref,
                "accepted_integer_parameter":parameter,
                "canonical_quotient_trace_row_mod_prime":A.rows(row)[0],
                "all690_original_V3_test_function_traces_mod_prime":A.rows(traceV3)[0],
                "complete_artin_algebra_length":272,"trace_of_unit_equals272":True,
                "all_finite_factors_and_nilpotent_multiplicities_retained":True,
                "exact_trace_definition":{
                    "algebra_source":self.inputs["divisors"][label]["certificate"],
                    "quotient_and_h_trivialization":modelref,
                    "power_basis_unit_solve":self.ref(trialname),
                    "operation":"Newton traces of exact full companion relation, followed by canonical quotient coordinates"},
                "characteristic_zero_trace_coordinates_expanded":False})
            self.checkpoint(name)
            return old,self.ref(name)
        raise ScopeStop(label+": no full Artin primitive unit in the retained finite section prefix")

    def target(self,label,U,Uref,model,modelref,pp,ppref,Htrace,Href,Dtrace,Dref):
        name = label+"-complete-logarithmic-principal-part-target"
        old = self.old(name)
        if old is None:
            self.budget()
            h = Htrace["all690_original_V3_test_function_traces_mod_prime"]
            d = Dtrace["all690_original_V3_test_function_traces_mod_prime"]
            assert len(h)==len(d)==690
            alltarget = A.mat([[(x-y)%P] for x,y in zip(h,d)])
            U3 = A.embed(2,3)*U
            assert U3.transpose()*alltarget == A.zero(146,1)
            b = A.sub(alltarget,model["V3_P_quotient_free_rows"],[0])
            constant = A.mat(pp["constant_function_coordinates_mod_prime"])
            assert constant.transpose()*b == A.zero(1,1)
            old = self.put(name,{"prime":P,"label":label,
                "source_common_complete_H_trace":Href,"source_complete_D_trace":Dref,
                "source_complete_quotient_model":modelref,"source_principal_parts_matrix":ppref,
                "all690_target_values_mod_prime":A.rows(alltarget),
                "target_vector_544_mod_prime":A.rows(b),
                "all146_U_test_relations_times_target_zero":True,
                "exact_total_residue_degH_minus_degD_zero":True,
                "constant_test_function_target_zero_verified":True,
                "exact_target":"Tr_(O_H)(s/h_a^3)-Tr_(O_D)(s/h_a^3)",
                "exact_logarithmic_principal_part":"H-D, in the original rational section1",
                "complete_full_principal_parts_via_perfect_pairing":True,
                "D_H_intersections_and_nonnormal_fibre_multiplicities_not_discarded":True,
                "exact_target_lies_in_full_image_by_global_residue_theorem":True,
                "proof":self.item["proofs"]["R909"]})
            self.checkpoint(name)
        return old,self.ref(name)

    def solve_connection(self,label,Uref,Fref,modelref,pp,ppref,target,targetref):
        name = label+"-complete-full-principal-parts-solution"
        solution = self.old(name)
        if solution is None:
            self.budget()
            M = A.mat(pp["matrix_mod_prime"])
            b = A.mat(target["target_vector_544_mod_prime"])
            data = A.selected_solution(M,b,543)
            solution = self.put(name,{"prime":P,"label":label,
                "source_full_principal_parts_matrix":ppref,"source_full_target":targetref,
                "required_full_principal_parts_rank":543,
                "exact_rank_upper_bound_from_R905_R909":543,
                "exact_target_in_image_by_residue_theorem":True,
                "all_new_arrays_only_auxiliary_place_images":True,**data})
            self.checkpoint(name)
        if not solution["rank_is_required"] or not solution.get("all_original_rows_multiplied_back",False):
            raise ScopeStop(label+": full543 chart or all544 logarithmic equations not certified at this place")
        cname = label+"-exact-regular-connection-DAG"
        connection = self.old(cname)
        if connection is None:
            self.budget()
            graph = {
                "operation":"trace_dual_basis_differential_combination",
                "field_source":self.inputs["global_function_DAG"],
                "source_same_divisor_U146":Uref,"source_complete_bundle_F":Fref,
                "source_full_test_quotient":modelref,
                "basis":{
                    "operation":"multiply_trace_dual_element_by_power_and_dz",
                    "trace_dual_basis_of_F_columns":{
                        "operation":"inverse_transpose_original_function_field_trace_pairing",
                        "source_original_normal_field":self.inputs["global_function_DAG"],
                        "source_exact_F_columns":Fref,
                        "trace_pairing_is_nondegenerate_in_characteristic_zero":True,
                        "formula":"theta_j=sum_i beta_i*(Tr(beta beta^t)^-1 F^-t)_ij"},
                    "indices":pp["differential_basis_indices"],"auxiliary_z":pp["auxiliary_z"],
                    "coefficient_power":"(z-a)^k","differential":"the original dz"},
                "coefficients":{
                    "operation":"exact_selected_unit_system_with_other_coefficients_zero",
                    "matrix":ppref,"target":targetref,
                    "rows":solution["selected_rows"],"columns":solution["selected_columns"],
                    "actual_auxiliary_unit_minor":self.ref(name),
                    "all_exact_unselected_rows_follow_from_rank543_and_full_residue_target":True},
                "original_rational_section":"1 of O(H-D)",
                "full_logarithmic_principal_parts":"H-D",
            }
            connection = self.put(cname,{"prime":P,"label":label,
                "source_original_complete_divisor_space":self.inputs["divisors"][label]["space"],
                "source_original_divisor_certificate":self.inputs["divisors"][label]["certificate"],
                "source_original_marked_principal":self.inputs["divisors"][label]["principal"],
                "source_complete_U146":Uref,"source_complete_bundle_unit_graph":Fref,
                "source_complete_quotient_models":modelref,"source_full_principal_parts_matrix":ppref,
                "source_full_target":targetref,"source_full543_unit_solution":self.ref(name),
                "exact_connection_DAG":graph,
                "complete_trace_dual_differential_basis_dimension":670,
                "complete_principal_parts_dimension":544,"actual_principal_parts_rank":543,
                "all544_principal_part_equations_multiplied_back":True,
                "exact_regular_connection_on_original_O_H_minus_D_as_expression_certified":True,
                "exact_full_principal_parts_not_only_residues_certified":True,
                "all_ramification_nilpotents_and_D_H_intersections_preserved":True,
                "characteristic_zero_connection_coefficients_expanded":False,
                "canonical_splitting_Hecke_period_or_height_computed":False})
            self.checkpoint(cname)
        self.done[label] = self.ref(cname)
        self.unresolved.pop(label,None)
        return connection,self.ref(cname)

    def direction(self,label,Htrace,Href):
        self.active = label
        old = self.old(label+"-exact-regular-connection-DAG")
        if old is not None:
            self.done[label] = self.ref(label+"-exact-regular-connection-DAG")
            return
        U,I,Uref = self.U_space(label)
        F,inverse0,a,Fref = self.bundle(label,U,Uref)
        model,modelref = self.local_models(label,U,I,Uref,F,inverse0,a,Fref)
        pp,ppref = self.principal_parts(label,U,Uref,F,inverse0,a,Fref,model,modelref)
        Dtrace,Dref = self.D_trace(label,model,modelref)
        target,targetref = self.target(label,U,Uref,model,modelref,pp,ppref,Htrace,Href,Dtrace,Dref)
        self.solve_connection(label,Uref,Fref,modelref,pp,ppref,target,targetref)
        self.checkpoint(label+"-complete")
        gc.collect()

    def original_Picard_connections(self):
        name = "five-original-Picard-regular-connection-DAGs"
        old = self.old(name)
        if old is not None:
            return old,self.ref(name)
        assert set(self.done)==set(LABELS)
        self.budget()
        nodes = []
        used = set()

        def node(identifier, operation, arguments=(), **data):
            assert identifier not in used
            assert all(x in used for x in arguments)
            used.add(identifier)
            nodes.append({"id":identifier,"operation":operation,
                          "arguments":list(arguments),"data":data})
            return identifier

        for label in LABELS:
            node("alpha_"+label,"completed_original_regular_connection",source=self.done[label],
                 line_bundle="O(H-D)",original_rational_section="1",residue_divisor="H-D")
        for label in list(LABELS[:5])+["DN"]:
            principal = self.inputs["divisors"][label]["principal"]
            node("Q_"+label,"original_unscaled_marked_function_DAG",source=principal,
                 root_field="exact_QN_function_DAG" if label=="DN" else "Q_root",
                 nodes_field=None if label=="DN" else "exact_principal_nodes",
                 all_original_nonzero_constants_and_tau_weights_preserved=True)
        sigma_definition = node("original_sigma","original_constant_field_Galois_action",
            source=self.inputs["global_function_DAG"],
            source_node=self.global_graph["original_Galois_automorphism_node"],
            order=7,fixes_original_curve_z_w_normal_basis=True,fixes_original_zeta=True,
            action_on_all_unit_solve_coefficients_and_function_leaves=True)
        node("original_cY","original_arithmetic_semilinear_curve_involution",
            original_function_field_source=self.inputs["global_function_DAG"],
            original_W_node=self.global_graph["original_global_derivative_nodes"]["W"],
            original_normal_matrix_convention="rows output, columns input",
            cofactor_denominator={"operation":"adjugate_entry","matrix":"TI-W(z)","row":0,"column":0},
            cofactor_numerator={"operation":"adjugate_entry","matrix":"TI-W(z)","row":0,"column":72},
            constant_action={"original_b":"fixed","s":"-s","zeta":"zeta^2"},
            curve_action={"z":"z-2*N(z,w)/D(z,w)","w":"w"},
            differential_action="substitute the full original field expression and pull back its differential",
            equivalent_original_nu_action="nu=dz/g is fixed; apply full cY to its coefficient",
            source_original_semilinear_proof=self.item["proofs"]["R860"],
            coefficient_conjugation_alone_is_not_used=True)
        node("dlog_QN","dlog_nonzero_original_function",["Q_DN"])
        node("connection_minus_Tf","subtract_differentials",["alpha_DN","dlog_QN"],
             exact_line_bundle="O(-T_f^0)",
             exact_divisor_identity="T_f^0=(D_N-H)+div(Q_N)",
             QN_transport_precedes_Galois_average=True)
        node("beta_N","rational_average_original_Galois_differentials",
             ["connection_minus_Tf",sigma_definition],order=7,rational_factor=[1,7],
             same_original_K_defined_line_bundle=True,
             terminal_DN_not_assumed_K_fixed=True)
        outputs = {}
        for j in range(1,6):
            p,q,n,e = P_NUMERATORS[j-1],Q_DENOMINATORS[j-1],POWERS[j-1],DEGREES[j-1]
            assert q*e==1206*p
            label = "D"+str(j)
            node("sum_alpha_"+str(j),"sum_seven_original_Galois_differentials",
                 ["alpha_"+label,sigma_definition],order=7,
                 all_conjugate_unit_solve_choices_are_transported_exactly=True,
                 new_conjugate_matrix_arithmetic_computed=False)
            node("Norm_Q_"+str(j),"product_seven_original_Galois_functions",
                 ["Q_"+label,sigma_definition],order=7,
                 original_Q_already_contains_negative_qchi_power=True,
                 no_extra_qchi_factor_inserted=True)
            node("dlog_Norm_Q_"+str(j),"dlog_nonzero_original_function",["Norm_Q_"+str(j)])
            node("alpha_K_"+str(j),"exact_integer_linear_combination_of_differentials",
                 ["sum_alpha_"+str(j),"alpha_X","beta_N","dlog_Norm_Q_"+str(j)],
                 coefficients=[q,7*q*(n-2),-p,-q],
                 original_divisor="Z_j",rational_section="1 of I_Zj=O(-Z_j)",
                 original_principal_product="(Norm Q_j)^q * Q_N^(-p)",
                 previous_126_aggregate_flips_not_required_for_this_connection=True)
            node("alpha_Q_"+str(j),"average_with_true_original_cY",
                 ["alpha_K_"+str(j),"original_cY"],rational_factor=[1,2],
                 original_ideal_and_parameter_frames_Q_defined_source=self.item["proofs"]["RF"],
                 no_Picard_class_or_polarization_or_kappa_replacement=True)
            output = self.global_graph["five_original_polar_and_eta_outputs"][str(j)]
            outputs[str(j)] = {
                "original_index":j,"original_Hom_word":"1+T^"+str(j),"p":p,"q":q,
                "n":n,"original_pole_degree":e,
                "source_original_polar_and_eta_DAG":self.inputs["global_function_DAG"],
                "source_original_I_Z_ideal_nodes":output["eta_degree_zero_fractional_ideal"],
                "source_original_eta_class":output["eta_Picard_class"],
                "exact_K_connection_root":"alpha_K_"+str(j),
                "exact_Q_connection_root":"alpha_Q_"+str(j),
                "source_original_Qj":self.inputs["divisors"][label]["principal"],
                "source_original_QN":self.inputs["divisors"]["DN"]["principal"],
                "source_original_t_frame":self.inputs["original_t_frame"],
                "P0_original_frame":"t^(7*(q-p))",
                "P0_rational_connection_residue":7*(p-q),
                "P0_frame_regular_connection":"alpha+7*(q-p)*dt/t",
                "P0_original_principal_order":7*(q-p),
                "P1_original_frame":"1; cancel the complete line-bundle principal parts before evaluation",
                "P0_or_P1_numeric_connection_value_computed":False,
                "exact_original_I_Z_regular_connection_as_expression_certified":True,
                "exact_original_eta_normalization_preserved":True,
                "true_Galois_and_cY_descent_applied_to_complete_connection":True,
                "canonical_Hecke_calibration_or_Y_period_or_nonp_terms_computed":False,
                "height_or_original_Tp_nonvanishing_certified":False,
            }
        old = self.put(name,{"expression_language":"source-bound exact function-field and differential DAG, version1",
            "source_seven_complete_regular_connections":self.done,
            "source_original_global_function_DAG":self.inputs["global_function_DAG"],
            "source_original_t_frame":self.inputs["original_t_frame"],
            "nodes":nodes,"five_original_outputs":outputs,
            "all_five_original_I_Z_regular_connections_as_exact_expressions_certified":True,
            "original_QN_corrected_before_average":True,
            "original_Qj_negative_chi_power_used_exactly_once":True,
            "true_curve_semilinear_action_not_coefficient_conjugation":True,
            "all_original_rigidification_constants_retained_by_source_reference":True,
            "seven_source_connections_only_new_principal_part_solves":7,
            "new_30_conjugate_numeric_connection_solves":0,
            "new_126_aggregate_flip_computations":0,
            "canonical_Hecke_calibration_nonp_period_and_height_computed":False,
            "characteristic_zero_connection_coordinates_expanded":False})
        self.checkpoint(name)
        return old,self.ref(name)

    def finish(self, complete, reason):
        files, currents = [], []
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name.startswith(PREFIX+"stage-manifest-"):
                continue
            value = read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag
            if value["complete"] is True:
                files.append(spec(path))
            else:
                assert path.name==PREFIX+"current.json.gz"
                currents.append(spec(path))
        digest = fingerprint({"files":files,"current_checkpoints":currents})
        manifest_name = "stage-manifest-"+digest
        manifest = self.put(manifest_name,{"files":files,"current_checkpoints":currents,
            "all_complete_stages_in_actual_output_listed":True,
            "only_new_same_tag_R905_mathematical_stages":True})
        program_path = self.path("five-original-Picard-regular-connection-DAGs")
        program_ref = spec(program_path) if program_path.exists() else None
        if complete:
            assert set(self.done)==set(LABELS) and program_ref is not None
            assert self.own(program_ref)["all_five_original_I_Z_regular_connections_as_exact_expressions_certified"] is True
        final = {"result":RESULT,"configuration":self.tag,"complete":bool(complete),"p":41,
            "prime":P,"source_audit":self.refs.get("original-source-audit"),
            "complete_source_connection_certificates":dict(self.done),
            "actual_completed_source_connections":len(self.done),
            "source_divisor_order":list(LABELS),"unresolved_divisors":dict(self.unresolved),
            "five_original_connection_DAGs":program_ref,
            "actual_seven_complete_full_principal_parts_solutions":len(self.done)==7,
            "actual_five_original_I_Z_regular_connections_as_expressions_certified":bool(complete),
            "actual_true_cY_and_Galois_descent_of_complete_connections_certified":bool(complete),
            "old_original_W_Krylov_or_inverse_or_418_spaces_recomputed":False,
            "old_273_node_characteristic_polynomial_Gamma_or_delta_B_recomputed":False,
            "original_P0_t_frames_Qj_QN_kappa_and_polarization_preserved":True,
            "source_characteristic_zero_arrays_or_connection_coordinates_expanded":False,
            "Hecke_calibration_nonp_Picard_period_height_or_Tp_nonvanishing_computed":False,
            "stage_manifest":self.ref(manifest_name),
            "resume_state":spec(self.path("current")) if self.path("current").exists() else None,
            "scope_stop_reason":reason,"seconds":time.monotonic()-self.started}
        save(self.out/FINAL,final)
        print("R905_FINAL="+json.dumps({k:v for k,v in final.items() if k not in ("configuration",)},sort_keys=True),flush=True)
        return final

    def run(self):
        path = self.out/FINAL
        if path.exists():
            previous = read(path)
            assert previous["configuration"]==self.tag and previous["result"]==RESULT
            if previous["complete"]:
                self.done = dict(previous["complete_source_connection_certificates"])
                return previous
        self.prepare()
        Htrace,Href = self.common_H_trace()
        for ordinal,label in enumerate(LABELS):
            if ordinal>=self.max_divisors:
                return self.finish(False,"scope_divisor_limit_reached")
            self.budget()
            try:
                self.direction(label,Htrace,Href)
            except ScopeStop as exc:
                self.unresolved[label] = str(exc)
                self.checkpoint(label+"-retained-scope-stop")
        self.active = None
        if set(self.done)!=set(LABELS):
            return self.finish(False,"one_or_more_complete_unit_charts_not_observed")
        self.original_Picard_connections()
        return self.finish(True,None)


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser()
    parser.add_argument("--config",required=True)
    parser.add_argument("--retained",required=True)
    parser.add_argument("--output",required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args = parser.parse_args()
    assert 0<args.budget_minutes<=300
    out = Path(args.output)
    out.mkdir(parents=True,exist_ok=True)
    job,final,error,code = None,None,None,1
    started = time.monotonic()
    try:
        job = Job(args)
        final = job.run()
        code = 0 if final["complete"] else 2
    except BudgetStop as exc:
        code,error = 124,{"type":"BudgetStop","message":str(exc)}
        if job is not None:
            final = job.finish(False,"budget")
    except ScopeStop as exc:
        code,error = 2,{"type":"ScopeStop","message":str(exc)}
        if job is not None:
            final = job.finish(False,str(exc))
    except Exception as exc:
        error = {"type":type(exc).__name__,"message":str(exc)}
        traceback.print_exc()
        if job is not None:
            try:
                final = job.finish(False,"unexpected_error")
            except Exception:
                traceback.print_exc()
    receipt = {"result":RESULT,"source_sha256":sha(__file__),"complete":code==0,
        "configuration":job.tag if job is not None else None,
        "configuration_sha256":fingerprint(job.tag) if job is not None else None,
        "process_exit_code":code,"error":error,"seconds":time.monotonic()-started,
        "certificate_sha256":sha(out/FINAL) if (out/FINAL).exists() else None,
        "actual_completed_source_connections":len(job.done) if job is not None else 0,
        "all_new_mathematics_only_in_original_public_Actions":True}
    save(out/"core-receipt.json",receipt)
    print("R905_CORE_RECEIPT="+json.dumps(receipt,sort_keys=True),flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
