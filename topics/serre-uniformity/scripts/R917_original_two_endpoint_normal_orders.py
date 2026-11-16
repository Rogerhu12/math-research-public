#!/usr/bin/env python3
"""Original rank-eight orders at the two marked endpoints; public Actions only."""
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

import flint
from flint import nmod_mat

RESULT = "R917-original-two-endpoint-normal-orders"
FINAL = "p41-original-two-endpoint-normal-orders-certificate.json"
PREFIX = "R917-endpoint-"
CURRENT = PREFIX + "current.json.gz"
INVENTORY = PREFIX + "stage-manifest.json.gz"
PRIME, ZETA, SROOT = 1000000753, 549966761, 99932770
COUNT, LEAVES, BLOCK = 273, 146, 64
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
SOURCES = ("R873", "R882", "R807", "R883", "R914")
PROOFS = ("R912", "R917", "R873", "R882", "R883", "R914", "R860")
META = ("public-actions-input.json", "run-receipt.json", "core-receipt.json")
H64 = re.compile(r"[0-9a-f]{64}")
DEFINITIONS = {
    "R873": ("R873-original-cyclic-seven-correspondence",
        "3c4922ee5b83d82123d234df47e67f82d7c8032f1152c6cf14df34622101918c"),
    "R882": ("R882-original-cyclic-seven-common-place-coefficients",
        "901466ae4d34bf1b558132a3b7c57c1c0bf6f2a8f097bc2283cd562607ba2e0f"),
    "R807": ("R807-original-M6-pole-clearing",
        "d92cf79bb3a30fe8e28709a4e2eaa706a724e195c8d8393e7649466a79cec018"),
    "R883": ("R883-original-t-first-order-frame",
        "2778a81b5639a1eb6285718574af0ce4b48b00e92b648c6ac29ffe70c1da66f7"),
    "R914": ("R914-original-full-V1-involution-and-P1-local-jets",
        "c7dded45af13c7cd37b9c5261d917c2e81d3c179debe963296bbd8caf746e004"),
}
STRATEGY = {
    "scope": "two_original_rank8_normal_orders_and_primitive_t_frames_only",
    "original_curve": "Y with original minus3 descent; no replacement twist",
    "original_auxiliary_prime": PRIME, "original_zeta_root": ZETA, "original_s_root": SROOT,
    "rank": 8, "geometric_special_fibre_lengths": [1, 1, 3, 3],
    "normal_order_discriminant_order": 4,
    "endpoint_parameters": ["rho0=z-z0", "rho1=iota^*rho0=z-2*beta72-z0"],
    "input_leaf_jet_count": COUNT, "original_V1_dimension": LEAVES,
    "original_ei_scale_already_in_source": "6724", "new_scale_applied": "1",
    "coefficient_order": "P0..P8,K0..K7",
    "common_clear": "Ptilde=theta0^2*P; Ktilde=theta0^2*K; theta0=theta/tau",
    "regular_coefficient_weight": 10,
    "initial_integrality": "Theta=rho^h*U; minimal nonnegative h from actual coefficient valuations",
    "initial_uniform_precision": "input_N-vrho(Ptilde8) after integral numerator deflation",
    "order_enlargement": "End_O(radical(rho O)) via full four-block conditions at orders0,1",
    "each_enlargement_uniform_precision_loss": 2,
    "discriminant_algorithm": "division-free Berkowitz over the complete truncated series ring",
    "basis_convention": "columns in original Theta power basis; exact Laurent polynomial inverse retained",
    "stop_rule": "actual complete integral table and actual discriminant order4",
    "old_P0_theta_A_first3_values_copied": True,
    "monomial_block_size": BLOCK,
    "all_factors_nilpotents_and_original_P_K_preserved": True,
    "source_target_direction": "original Nm_pi_t(pi_s^*I), transported by canonical dual7 on both determinants",
    "exact_nu": "82*tau*dqY/qY; iota fixes nu",
    "t_frame": "t-epsilon=c_epsilon*rho_epsilon+...; c1=-c0; leading multiplies c_epsilon^(-order)",
    "characteristic_zero_order_basis_expanded": False,
    "target272_coordinates_or_target_Norm_frames_computed": False,
    "only_budget_enlargement_limit_and_transport_paths_excluded_from_identity": True,
}


class BudgetStop(RuntimeError):
    pass


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for b in iter(lambda: stream.read(1048576), b""):
            h.update(b)
    return h.hexdigest()


def fingerprint(v):
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=False).encode()).hexdigest()


def plain(value):
    out = {k: value[k] for k in ("file", "bytes", "sha256")}
    assert Path(out["file"]).name == out["file"] and "\\" not in out["file"]
    assert isinstance(out["bytes"], int) and out["bytes"] >= 0 and H64.fullmatch(out["sha256"])
    return out


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
    payload = (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode()
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
        self.label, self.item = label, item
        self.path = Path(item["directory"])
        assert (item["result"], item["core_sha256"]) == DEFINITIONS[label]
        self.files = {k: plain(v) for k, v in item["files"].items()}
        assert len(self.files) == item["selected_file_count"]
        assert fingerprint(self.files) == item["selected_files_sha256"]
        for name, row in self.files.items():
            assert name == row["file"] and spec(self.path/name) == row, (label,name)
        manifest = read(self.path/"full-outputs-manifest.json")
        assert sha(self.path/"full-outputs-manifest.json") == item["manifest_sha256"]
        assert manifest["result"] == item["result"]
        entries = {r["file"]: plain(r) for r in manifest["files"]}
        assert len(entries) == len(manifest["files"])
        for name, row in self.files.items():
            if name != "full-outputs-manifest.json":
                assert entries[name] == row
        self.cert = self.get(item["certificate"]["file"])
        assert self.cert["complete"] is True and self.cert["result"] == item["result"]
        self.tag = self.cert["configuration"]
        assert self.tag["source_sha256"] == item["core_sha256"]
        assert fingerprint(self.tag) == item["configuration_sha256"]
        initial, run, core = (self.get(n) for n in META)
        assert initial["source_commit"] == run["source_commit"] == item["source_commit"]
        assert str(run["workflow_run_id"]) == str(item["run_id"])
        assert initial["core_sha256"] == core["source_sha256"] == item["core_sha256"]
        assert run["process_exit_code"] == 0 and run["complete"] is True and core["complete"] is True
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        assert core["certificate_sha256"] == item["certificate"]["sha256"]

    def get(self, name):
        assert name in self.files, (self.label,name)
        return read(self.path/name)

    def stage(self, row):
        assert self.files[row["file"]] == plain(row)
        v = self.get(row["file"])
        assert v["complete"] is True and v["configuration"] == self.tag
        assert v.get("result", v["configuration"]["result"]) == self.item["result"]
        return v


class Job:
    def __init__(self, args):
        self.args = args
        self.item = read(args.config)
        self.out = Path(args.out)
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        self.deadline = self.started + 60*args.budget_minutes
        self.tag = expected_tag(self.item)
        self.refs = {}
        self.endpoints = {}
        self.active = None
        self.current = None
        assert self.item["result"] == RESULT and self.item.get("producer_inputs_pending") is False
        assert sha(__file__) == self.item["core_sha256"]
        self.topic = Path(self.item["topic_directory"])
        for row in self.item["proofs"].values():
            assert sha(self.topic/row["file"]) == row["sha256"]
        assert sha(self.topic/self.item["method"]) == self.item["method_sha256"]
        helper_path = self.topic/"scripts"/self.item["helper"]
        assert sha(helper_path) == self.item["helper_sha256"]
        module_spec = importlib.util.spec_from_file_location("R917_endpoint_order_arithmetic_bound", helper_path)
        self.H = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(self.H)
        assert str(flint.__version__) == "0.9.0"
        self.inputs = self.item["inputs"]
        self.maximum_steps = int(self.item.get("maximum_enlargement_steps", 128))
        assert self.maximum_steps >= 1
        self.sources = {k: Source(k,self.item["sources"][k]) for k in SOURCES}
        self.prepare()

    def budget(self):
        if time.monotonic() >= self.deadline:
            raise BudgetStop("The actual public execution budget is exhausted")

    def input(self, key):
        row = self.inputs[key]
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
        old = self.old(name)
        if old is not None:
            return old
        self.budget()
        self.active = name
        self.checkpoint()
        value = produce()
        assert isinstance(value,dict) and "configuration" not in value and "result" not in value
        value = {"result": RESULT, "configuration": self.tag, "complete": True, **value}
        save(self.path(name), value)
        self.refs[name] = spec(self.path(name))
        self.active = None
        self.checkpoint()
        print("R917_ENDPOINT_STAGE="+json.dumps(self.refs[name],sort_keys=True),flush=True)
        return value

    def checkpoint(self, stop=None):
        value = {"result": RESULT, "configuration": self.tag, "complete": False,
            "active_stage": self.active, "completed_stage_refs": self.refs,
            "completed_endpoint_certificates": self.endpoints,
            "last_stop": stop, "seconds": time.monotonic()-self.started}
        save(self.out/CURRENT,value)
        self.current = spec(self.out/CURRENT)

    def prepare(self):
        self.DAG = self.input("correspondence_DAG")
        self.exact = self.input("exact_coordinate_expression")
        self.coordinates = self.input("seventeen_coordinates")
        self.common = self.input("same_place_interface")
        self.theta = self.input("theta")
        self.A = self.input("E6_clearing")
        self.old3 = self.input("old_cleared_three_jets")
        self.frame0 = self.input("original_P0_t_frame")
        self.frame1 = self.input("P1_t_frame")
        verification = self.input("iota_verification")
        assert verification["all560_by146_original_exact_Fourier_equations_verified"] is True
        assert verification["exact_matrix_square_is_identity146"] is True
        assert self.sources["R914"].cert["actual_original_P1_normal_jets_through_order272_computed"] is True
        assert self.sources["R882"].cert["all2200_by17_original_equations_verified"] is True
        assert self.coordinates["same_characteristic_zero_coefficients_integral_at_new_place"] is True
        assert plain(self.coordinates["source_exact_R873_unit_solve"]) == plain(self.inputs["exact_coordinate_expression"])
        assert plain(self.DAG["coefficient_unit_solve"]) == plain(self.inputs["exact_coordinate_expression"])
        assert plain(self.common["source_R873_correspondence_DAG"]) == plain(self.inputs["correspondence_DAG"])
        assert plain(self.common["new_modular_coordinates"]) == plain(self.inputs["seventeen_coordinates"])
        assert self.common["prime"] == PRIME and self.common["original_zeta_root"] == ZETA
        assert self.common["original_s_root"] == SROOT
        assert self.DAG["rigidified_Hecke_transport"]["frozen_direction"] == "Nm_pi_t(pi_s^*I)"
        assert self.DAG["rigidified_Hecke_transport"]["determinant_numerator_and_denominator_both_transported"] is True
        assert self.DAG["E6hat_over_tau3"]["new_scale_applied"] == "1"
        assert plain(self.DAG["E6hat_over_tau3"]["theta_source"]) == plain(self.inputs["theta"])
        assert plain(self.DAG["E6hat_over_tau3"]["V4_coordinate_source"]) == plain(self.inputs["E6_clearing"])
        assert self.theta["original_M2_integer_scale"] == "6724"
        assert self.A["M6_index"] == 692 and self.A["basis_dimension"] == 962
        assert self.A["all1100_rows_verified"] is True and self.A["exact_global_V4_membership_certified"] is True
        assert self.A["basis_integer_scale"] == str(82**8)
        assert plain(self.theta["M6_index692_cleared_coordinate_stage"]) == plain(self.inputs["E6_clearing"])
        assert plain(self.old3["source_theta"]) == plain(self.inputs["theta"])
        assert plain(self.old3["source_coordinates"]["692"]) == plain(self.inputs["E6_clearing"])
        assert self.old3["all_R807_coordinate_denominators_units"] is True
        assert self.old3["theta_exact_order_two_certified"] is True
        self.C = self.coordinates["coordinate_matrix_mod_prime"]
        assert len(self.C) == 2058 and all(len(row)==17 for row in self.C)
        assert all(isinstance(x,int) and 0 <= x < PRIME for row in self.C for x in row)
        self.rec8 = self.DAG["old_V8_over_tau8"]
        self.rec2 = self.DAG["new_eight_complement_functions"]
        self.rec4 = self.DAG["E6hat_over_tau3"]["nonzero_V4_monomials"]
        assert len(self.rec8)==2050 and len(self.rec2)==8
        assert [x["original_V2_index"] for x in self.rec2] == [0,1,2,3,73,74,75,76]
        for n,row in enumerate(self.rec8):
            assert row["index"]==n and len(row["original_M2_leaf_indices"])==8
        for n,row in enumerate(self.rec2):
            assert row["index"]==2050+n and len(row["original_M2_leaf_indices"])==2
        support = [i for i,x in enumerate(self.A["solution_numerators"]) if int(x)]
        assert [x["source_coordinate_index"] for x in self.rec4] == support
        for row in self.rec4:
            assert row["original_V4_index"]==row["source_coordinate_index"]
            assert len(row["original_M2_leaf_indices"])==4
        recipes = self.rec2+self.rec4+self.rec8
        assert all(0<=int(i)<LEAVES for row in recipes for i in row["original_M2_leaf_indices"])
        self.monomials = sorted({tuple(sorted(row["original_M2_leaf_indices"])) for row in recipes},key=lambda x:(len(x),x))
        self.leaf_data = [self.input("P0_V1_jets"),self.input("P1_V1_jets")]
        for endpoint,data in enumerate(self.leaf_data):
            assert data["prime"]==PRIME and data["matrix_shape"]==[COUNT,LEAVES]
            assert data["row_orders"]==list(range(COUNT))
            assert data["local_parameter"]==STRATEGY["endpoint_parameters"][endpoint]
            assert len(data["matrix_mod_prime"])==COUNT
            assert all(len(row)==LEAVES for row in data["matrix_mod_prime"])
        assert self.frame1["original_zeta_root"]==ZETA and self.frame1["original_s_root"]==SROOT
        assert self.frame1["original_c0_mod_prime"]==self.frame0["original_t_over_rho_constant_mod_prime"]
        assert (self.frame1["original_c0_mod_prime"]+self.frame1["original_c1_mod_prime"])%PRIME==0
        self.c = [self.frame1["original_c0_mod_prime"], self.frame1["original_c1_mod_prime"]]
        assert all(self.c)
        self.theta_coordinates = []
        units = self.old3["theta_denominator_units"]
        assert len(units)==LEAVES
        for i,(raw,unit) in enumerate(zip(self.theta["theta_in_original_integer_scaled_M2_basis"],units)):
            assert unit["index"]==i and int(raw[1])%PRIME==unit["denominator_mod_prime"]
            assert unit["denominator_mod_prime"]*unit["inverse_mod_prime"]%PRIME==1
            self.theta_coordinates.append(int(raw[0])%PRIME*unit["inverse_mod_prime"]%PRIME)
        u=self.old3["coordinate_denominator_units"]["692"]
        assert int(self.A["solution_common_denominator"])%PRIME==u["denominator_mod_prime"]
        assert u["denominator_mod_prime"]*u["inverse_mod_prime"]%PRIME==1
        self.A_coordinates = [int(x)%PRIME*u["inverse_mod_prime"]%PRIME for x in self.A["solution_numerators"]]
        self.stage("source-audit",lambda:{"prime":PRIME,"original_zeta_root":ZETA,"original_s_root":SROOT,
            "source_identities":{k:source_identity(self.item["sources"][k]) for k in SOURCES},
            "actual_selected_original_file_count":sum(self.item["sources"][k]["selected_file_count"] for k in SOURCES),
            "inputs":self.inputs,"original_correspondence":self.DAG["correspondence_function_field"],
            "original_dual7":self.DAG["rigidified_Hecke_transport"],
            "old_theta_and_A_denominator_inverses_reused":True,
            "old_first3_coefficients_source":self.inputs["old_cleared_three_jets"],
            "original_2050_plus8_recipes_bound":True,
            "actual_requested_unique_monomial_count":len(self.monomials),
            "no_original_2058_inverse_or_Fourier_series_recomputed":True,
            "characteristic_zero_exact_P_K_unit_solve":self.inputs["exact_coordinate_expression"],
            "characteristic_zero_order_basis_not_inferred_from_modular_basis":True})

    def monomial_jets(self, endpoint):
        R = self.H.SeriesRing(COUNT)
        source = self.leaf_data[endpoint]["matrix_mod_prime"]
        memo = {():R.one}
        for i in range(LEAVES):
            memo[(i,)]=R.element([row[i] for row in source])
        def evaluate(key):
            if key not in memo:
                cut=len(key)//2
                memo[key]=R.mul(evaluate(key[:cut]),evaluate(key[cut:]))
            return memo[key]
        refs=[]
        for first in range(0,len(self.monomials),BLOCK):
            stop=min(len(self.monomials),first+BLOCK)
            name=f"P{endpoint}-monomial-jets-{first:04d}-{stop:04d}"
            def produce(first=first,stop=stop):
                columns=[]
                for key in self.monomials[first:stop]:
                    self.budget();columns.append(R.pack(evaluate(key)))
                return {"endpoint":endpoint,"absolute_rho_precision":COUNT,
                    "source_leaf_matrix":self.inputs[f"P{endpoint}_V1_jets"],
                    "source_correspondence_DAG":self.inputs["correspondence_DAG"],
                    "first_unique_monomial":first,"stop_unique_monomial":stop,
                    "original_M2_leaf_tuples":[list(x) for x in self.monomials[first:stop]],
                    "jet_columns_mod_prime":columns,"new_integer_scale_applied":False}
            data=self.stage(name,produce)
            for key,column in zip(self.monomials[first:stop],data["jet_columns_mod_prime"]):
                memo[key]=R.element(column)
            refs.append(self.refs[name])
        return R,memo,refs

    def regular_coefficients(self, endpoint):
        name=f"P{endpoint}-common-cleared-seventeen-jets"
        completed=self.old(name)
        if completed is not None:
            return completed
        R,memo,monomial_refs=self.monomial_jets(endpoint)
        def monomial(row):
            return memo[tuple(sorted(row["original_M2_leaf_indices"]))]
        leaf=self.leaf_data[endpoint]["matrix_mod_prime"]
        def theta_A():
            first=3 if endpoint==0 else 0
            theta=[0]*COUNT;A=[0]*COUNT
            if endpoint==0:
                theta[:3]=self.old3["theta_three_jet_mod_prime"]
                A[:3]=self.old3["M6_cleared_three_jets_mod_prime"]["692"]
            for n in range(first,COUNT):
                theta[n]=sum(c*leaf[n][i] for i,c in enumerate(self.theta_coordinates))%PRIME
            sums=R.zero
            for row in self.rec4:
                self.budget()
                term=monomial(row)
                if first:
                    term=R.element([0]*first+[int(term[n]) for n in range(first,COUNT)])
                sums=R.add(sums,R.scale(term,self.A_coordinates[row["source_coordinate_index"]]))
            for n in range(first,COUNT):
                A[n]=int(sums[n])
            return {"endpoint":endpoint,"absolute_rho_precision":COUNT,
                "theta0_jets_mod_prime":theta,"N692_over_tau4_jets_mod_prime":A,
                "source_original_theta":self.inputs["theta"],"source_original_N692":self.inputs["E6_clearing"],
                "source_monomial_blocks":monomial_refs,"source_original_leaf_jets":self.inputs[f"P{endpoint}_V1_jets"],
                "P0_first3_output_coefficients_copied":endpoint==0,
                "source_P0_first3":self.inputs["old_cleared_three_jets"] if endpoint==0 else None,
                "new_linear_combination_orders":[first,COUNT-1],"old_denominator_inverses_used":True,
                "additional_82_or_rational_scale_applied":False}
        section_name=f"P{endpoint}-theta-and-N692-jets"
        sections=self.stage(section_name,theta_A)
        partial=[]
        for first in range(0,2050,BLOCK):
            stop=min(2050,first+BLOCK);pn=f"P{endpoint}-V8-seventeen-partial-{first:04d}-{stop:04d}"
            def produce(first=first,stop=stop):
                values=nmod_mat([[int(monomial(self.rec8[i])[n]) for i in range(first,stop)]
                                  for n in range(COUNT)],PRIME)
                coords=nmod_mat(self.C[first:stop],PRIME)
                answer=values*coords
                return {"endpoint":endpoint,"first_original_V8_index":first,"stop_original_V8_index":stop,
                    "source_monomial_blocks":monomial_refs,"source_coordinate_matrix":self.inputs["seventeen_coordinates"],
                    "absolute_rho_precision":COUNT,"weighted_partial_jets_mod_prime":
                    [[int(answer[n,j]) for j in range(17)] for n in range(COUNT)]}
            data=self.stage(pn,produce);partial.append((data,self.refs[pn]))
        def produce():
            v=[[sum(data["weighted_partial_jets_mod_prime"][n][j] for data,_ in partial)%PRIME
                for j in range(17)] for n in range(COUNT)]
            mvals=nmod_mat([[int(monomial(row)[n]) for row in self.rec2] for n in range(COUNT)],PRIME)
            m=mvals*nmod_mat(self.C[2050:],PRIME)
            theta=R.element(sections["theta0_jets_mod_prime"])
            A=R.element(sections["N692_over_tau4_jets_mod_prime"])
            theta2,A2=R.mul(theta,theta),R.mul(A,A)
            columns=[]
            for j in range(17):
                col=R.add(R.mul(theta2,R.element([v[n][j] for n in range(COUNT)])),
                          R.mul(A2,R.element([int(m[n,j]) for n in range(COUNT)])))
                columns.append(R.pack(col))
            return {"endpoint":endpoint,"prime":PRIME,"original_zeta_root":ZETA,
                "local_parameter":STRATEGY["endpoint_parameters"][endpoint],
                "absolute_rho_precision":COUNT,"column_order":"P0..P8,K0..K7",
                "common_cleared_coefficient_jets_mod_prime":columns,
                "source_theta_A":self.refs[section_name],"source_V8_partial_blocks":[r for _,r in partial],
                "source_exact_coordinate_expression":self.inputs["exact_coordinate_expression"],
                "source_original_coordinate_matrix":self.inputs["seventeen_coordinates"],
                "exact_common_clear":{"Ptilde":"theta0^2*P","Ktilde":"theta0^2*K",
                    "regular_formula":"theta0^2*V8_part+(N692/tau^4)^2*V2_part",
                    "target_w_unchanged":"K/P_U=Ktilde/Ptilde_U","new_scale":"1"},
                "all17_regular_functions_have_original_weight10":True,
                "theta_inverse_computed":False,"old_P_K_coordinates_recomputed":False,
                "characteristic_zero_series_coefficients_expanded":False}
        return self.stage(name,produce)

    def primitive(self, endpoint, cleared):
        name=f"P{endpoint}-primitive-order"
        def produce():
            N=cleared["absolute_rho_precision"];R=self.H.SeriesRing(N)
            cols=cleared["common_cleared_coefficient_jets_mod_prime"]
            lead=R.element(cols[8]);a=R.valuation(lead,"Ptilde8 at P"+str(endpoint))
            vals=[]
            for i in range(8):
                b=next((n for n,x in enumerate(cols[i]) if x),N)
                vals.append({"index":i,"valuation_or_lower_bound":b,"known_nonzero":b<N})
            h=max([0]+[max(0,(a-v["valuation_or_lower_bound"]+7-v["index"])//(8-v["index"])) for v in vals])
            n=N-a
            if n<5:
                raise self.H.NeedPrecision("Too few source coefficients remain after the actual leading factor",
                    {"endpoint":endpoint,"input_precision":N,"leading_order":a,"remaining_precision":n,
                     "minimum_needed_for_discriminant4":5})
            ring=self.H.SeriesRing(n)
            unit=ring.element(cols[8][a:]);inv=ring.unit_inverse(unit)
            monic=[]
            for i in range(8):
                shift=h*(8-i)-a
                if shift<0:
                    assert all(not cols[i][j] for j in range(-shift))
                num=ring.element([cols[i][j-shift] if 0<=j-shift<N else 0 for j in range(n)])
                value=ring.mul(num,inv)
                assert ring.mul(value,unit)==num
                monic.append(ring.pack(value))
            monic.append(ring.pack(ring.one))
            order=self.H.Order.primitive(monic,n,h);order.verify_basis_and_unit()
            return {"endpoint":endpoint,"source_common_cleared_jets":self.refs[f"P{endpoint}-common-cleared-seventeen-jets"],
                "original_Ptilde8_order":a,"other_coefficient_valuations":vals,
                "original_Theta_rho_power":h,"absolute_rho_precision":n,
                "monic_coefficients_ascending_Theta":monic,
                "deflated_leading_unit_series":ring.pack(unit),"deflated_leading_unit_inverse":ring.pack(inv),
                "all_eight_complete_unit_quotient_products_verified":True,
                "all_possible_negative_initial_coefficients_verified_zero":True,
                "uniform_precision_is_input_N_minus_leading_order":True,
                "original_U_equals":"rho^(-h)*Theta","order":order.pack()}
        return self.stage(name,produce)

    def endpoint(self, epsilon):
        cert_name=f"P{epsilon}-normal-order-certificate"
        done=self.old(cert_name)
        if done is not None:
            self.endpoints[str(epsilon)]=self.refs[cert_name]
            return
        cleared=self.regular_coefficients(epsilon)
        primitive=self.primitive(epsilon,cleared)
        order=self.H.Order.unpack(primitive["order"])
        order_ref=self.refs[f"P{epsilon}-primitive-order"]
        initial_d=None;initial_leading=None;history=[]
        for step in range(self.maximum_steps+1):
            self.budget()
            dn=f"P{epsilon}-order-{step:03d}-discriminant"
            def produce_disc(order=order,order_ref=order_ref):
                data,_=order.discriminant()
                return {"endpoint":epsilon,"order_step":step,"source_order":order_ref,**data}
            disc=self.stage(dn,produce_disc)
            d=disc["discriminant_order"]
            if initial_d is None:
                initial_d=d;initial_leading=disc["discriminant_leading_mod_prime"]
            assert d==initial_d-2*order.index_length
            assert disc["discriminant_leading_mod_prime"]==initial_leading*pow(order.determinant_unit,2,PRIME)%PRIME
            if d==4:
                break
            if step==self.maximum_steps:
                raise BudgetStop("The configured number of actual idealizer enlargements is reached")
            kn=f"P{epsilon}-order-{step:03d}-idealizer-kernel"
            def produce_kernel(order=order,order_ref=order_ref):
                gram=[[order.R.element(x) for x in row] for row in disc["trace_gram_matrix"]]
                data=order.idealizer(gram)
                assert data["index_length_increment"]>0
                return {"endpoint":epsilon,"order_step":step,"source_order":order_ref,
                        "source_discriminant":self.refs[dn],**data}
            kernel=self.stage(kn,produce_kernel)
            en=f"P{epsilon}-order-{step+1:03d}-complete-table"
            def produce_enlargement(order=order,order_ref=order_ref):
                new,verification=order.enlarge(kernel)
                assert new.verify_original_monic_relation(primitive["monic_coefficients_ascending_Theta"])
                return {"endpoint":epsilon,"order_step":step+1,
                    "source_previous_order":order_ref,"source_idealizer_kernel":self.refs[kn],
                    "source_initial_primitive_order":self.refs[f"P{epsilon}-primitive-order"],
                    "original_primitive_relation_in_transported_table_verified":True,
                    "verification":verification,"order":new.pack()}
            expanded=self.stage(en,produce_enlargement)
            new=self.H.Order.unpack(expanded["order"])
            assert new.index_length==order.index_length+kernel["index_length_increment"]
            history.append({"step":step,"old_discriminant_order":d,
                "index_length_increment":kernel["index_length_increment"],
                "kernel":self.refs[kn],"new_order":self.refs[en],
                "constant_determinant":kernel["new_basis_constant_determinant"]})
            order,order_ref=new,self.refs[en]
        sn=f"P{epsilon}-complete-length8-special-fibre"
        special=self.stage(sn,lambda:{"endpoint":epsilon,"source_normal_order":order_ref,
            "source_discriminant":self.refs[dn],**order.special_fibre()})
        fn=f"P{epsilon}-primitive-and-original-t-determinant-frames"
        def produce_frame():
            m=28*order.initial_h-order.index_length
            unit=order.determinant_unit
            tunit=unit*pow(self.c[epsilon],-m,PRIME)%PRIME
            U_coordinates=[self.H.lp_pack(self.H.lp_scale(order.basis_inverse[i][1],1,-order.initial_h)) for i in range(8)]
            return {"endpoint":epsilon,"source_normal_order":order_ref,
                "source_original_parameter_frame":self.inputs["P1_t_frame"] if epsilon else self.inputs["original_P0_t_frame"],
                "local_parameter":STRATEGY["endpoint_parameters"][epsilon],
                "original_t_parameter":"t" if epsilon==0 else "t-1",
                "original_t_over_rho_mod_prime":self.c[epsilon],
                "initial_Theta_rho_power":order.initial_h,"total_index_length":order.index_length,
                "determinant_rho_order_relative_to_1_U_to_U7":m,
                "determinant_rho_leading_mod_prime":unit,"determinant_t_leading_mod_prime":tunit,
                "exact_residue_field_frame_formula":"unit*rho^(28*h-index); t-leading=unit*c_epsilon^(-order)",
                "original_U_coordinates_in_normal_order_basis":U_coordinates,
                "original_target_w_exact_expression":{"operation":"Ktilde(U)/d_U_Ptilde(U)",
                    "source_common_cleared_jets":self.refs[f"P{epsilon}-common-cleared-seventeen-jets"],
                    "source_exact_global_P_K":self.inputs["correspondence_DAG"]},
                "original_dual7":self.DAG["rigidified_Hecke_transport"],
                "original_nu":{"expression":"82*tau*dqY/qY","iota_fixes_nu":True,
                    "source_proof":self.item["proofs"]["R860"],"new_nu_over_rho_numeric_value_computed":False},
                "both_determinant_factors_required_under_dual7":True,
                "reference_or_target_NormPhi_detU_numeric_calibration_computed":False,
                "target_w_Laurent_inverse_or_272_normal_coordinates_computed":False,
                "characteristic_zero_basis_or_frame_scalar_expanded":False}
        frame=self.stage(fn,produce_frame)
        def produce_certificate():
            order.verify_basis_and_unit()
            assert order.verify_original_monic_relation(primitive["monic_coefficients_ascending_Theta"])
            return {"endpoint":epsilon,"prime":PRIME,"original_zeta_root":ZETA,
                "source_common_cleared_jets":self.refs[f"P{epsilon}-common-cleared-seventeen-jets"],
                "source_primitive_order":self.refs[f"P{epsilon}-primitive-order"],
                "complete_normal_order":order_ref,"complete_trace_discriminant":self.refs[dn],
                "complete_length8_special_fibre":self.refs[sn],"primitive_and_t_frames":self.refs[fn],
                "actual_initial_discriminant_order":initial_d,"actual_final_discriminant_order":4,
                "actual_enlargement_step_count":len(history),"actual_total_index_length":order.index_length,
                "actual_remaining_rho_precision":order.N,"enlargements":history,
                "common_cleared17_jets_computed":True,"normal_order_certified":True,
                "full_length8_special_fibre_preserved":True,
                "primitive_and_original_t_determinant_frames_computed":True,
                "all_original_primitive_relation_and_basis_inverse_products_verified":True,
                "full_discriminant_order_and_leading_determinant_change_verified":True,
                "normality_reason":"integral order discriminant4 equals original tame normal discriminant4",
                "characteristic_zero_expanded_order_basis_claimed":False,
                "target_coordinates_target_ideals_or_endpoint_Norms_computed":False}
        cert=self.stage(cert_name,produce_certificate)
        self.endpoints[str(epsilon)]=self.refs[cert_name]
        self.checkpoint()

    def manifest(self):
        files=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name in (CURRENT,INVENTORY):continue
            v=read(path)
            assert v["result"]==RESULT and v["configuration"]==self.tag and v["complete"] is True
            files.append(spec(path))
        value={"result":RESULT,"configuration":self.tag,"complete":True,"files":files,
               "only_actual_complete_mathematical_stages_listed":True}
        save(self.out/INVENTORY,value)
        return spec(self.out/INVENTORY)

    def finish(self, complete, stop):
        self.checkpoint(stop)
        value={"result":RESULT,"configuration":self.tag,"complete":bool(complete),
            "p":41,"prime":PRIME,"original_zeta_root":ZETA,"original_s_root":SROOT,
            "source_identities":{k:source_identity(self.item["sources"][k]) for k in SOURCES},
            "source_audit":self.refs.get("source-audit"),"completed_endpoint_certificates":self.endpoints,
            "actual_completed_endpoint_count":len(self.endpoints),
            "actual_original_two_endpoint_normal_orders_certified":len(self.endpoints)==2,
            "actual_full_length8_endpoint_algebras_preserved":len(self.endpoints)==2,
            "actual_primitive_and_original_t_order_frames_computed":len(self.endpoints)==2,
            "characteristic_zero_order_basis_expanded":False,
            "original_target272_endpoint_coordinates_computed":False,
            "five_target_endpoint_ideal_lattices_computed":False,
            "P0_endpoint_numeric_Norm_calibration_computed":False,
            "P1_endpoint_numeric_Norm_calibration_computed":False,
            "NmPhi_detU_and_reference_original_frames_evaluated":False,
            "Hecke_Picard_active_support_or_height_computed":False,
            "future_target_sources":{"R903":None,"R907":None},
            "stage_manifest":self.manifest(),"resume_state":self.current,
            "stop_reason":stop,"seconds":time.monotonic()-self.started}
        if complete:assert len(self.endpoints)==2
        save(self.out/FINAL,value)
        return value

    def run(self):
        for endpoint in (0,1):self.endpoint(endpoint)
        return self.finish(True,None)


def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise SystemExit("New R917 mathematical arithmetic is allowed only in the original public repository Actions")
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    parser.add_argument("--config",required=True);parser.add_argument("--out",required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args();out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    started=time.monotonic();job=None;code=1;error=None;certificate=None
    try:
        job=Job(args);certificate=job.run();code=0
    except Exception as exc:
        traceback.print_exc()
        if job is not None and isinstance(exc,job.H.NeedPrecision):
            error=exc.to_data();code=2
        elif isinstance(exc,BudgetStop):error={"kind":"BudgetStop","reason":str(exc)};code=2
        else:error={"kind":type(exc).__name__,"reason":str(exc)}
        if job is not None:
            certificate=job.finish(False,error)
    receipt={"result":RESULT,"source_sha256":sha(__file__),"complete":code==0,
        "process_exit_code":code,"error":error,"seconds":time.monotonic()-started,
        "configuration_sha256":None if job is None else fingerprint(job.tag),
        "certificate_sha256":sha(out/FINAL) if (out/FINAL).exists() else None,
        "stage_manifest":None if certificate is None else certificate["stage_manifest"],
        "actual_completed_endpoint_count":0 if certificate is None else certificate["actual_completed_endpoint_count"],
        "actual_original_two_endpoint_normal_orders_certified":code==0,
        "endpoint_target_NormPhi_frames_or_height_computed":False}
    save(out/"core-receipt.json",receipt)
    print("R917_ENDPOINT_CORE_RECEIPT="+json.dumps(receipt,sort_keys=True),flush=True)
    raise SystemExit(code)


if __name__=="__main__":main()
