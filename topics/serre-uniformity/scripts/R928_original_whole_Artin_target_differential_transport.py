#!/usr/bin/env python3
"""R928: eight original delta-K coefficients and whole-Artin differential-frame transport."""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
import time
import traceback
import flint
from flint import nmod_mat
import R885_whole_Artin_algebra as algebra
from R885_whole_Artin_algebra import SourceAlgebra, CorrespondenceAlgebra, UnitFailure

REPOSITORY="Rogerhu12/math-research-public"
RESULT="R928-original-whole-Artin-target-differential-transport"
FINAL="p41-original-whole-Artin-target-differential-transport-certificate.json"
PREFIX="R928-"
MANIFEST="full-outputs-manifest.json"
P=1000000753
EPS=[0]+[1]*144+[2]*127
GROUPS=("R919","R885","R827","R882","R873")
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
STRATEGY={
    "original_curve":"original genus127 Y, level82, original minus3 descent",
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "source_node_ordinal":0,"source_z":0,
    "source_algebra":"entire original Fp[X]/chi_0(X), dimension272",
    "correspondence":"entire A0[U]/(P(U)/a8), rank8",
    "original_target_w":"V=K(U)/P_U(U), K is the original numerator in columns9..16",
    "new_delta_K":"33 completed derivative blocks times the final8 original R882 columns",
    "derivative_block_size":64,"target_normal_block_size":16,
    "dotU":"completed R919 negative_deltaP_times_original_PU_inverse",
    "dotV":"old_PU_inverse*(deltaK+K_U*dotU-V*(deltaP_U+P_UU*dotU))",
    "target_g_h":"all272 original target normal coordinates contracted with original four coefficient vectors",
    "frame_trial_sequence":"integers0..2176 in this order; finite prefixes can be extended",
    "transport":"ell=g_target+t*h_target; J=(dotU+t*dotV)/ell",
    "acceptance":"ell whole-E unit and all2176 coordinates of J*g_target=dotU and J*h_target=dotV",
    "unit_algorithm":"division-free rank8 characteristic polynomial plus full A0 Bezout and E multiplication back",
    "J_inverse_or_J_unit_required":False,
    "old_2058_derivatives_nine_deltaP_dotU_a8_PU_or_Gamma_recomputed":False,
    "old_target_coordinates_Krylov_or_correspondence_recomputed":False,
    "delta_claimed_to_descend_to_source_fibre":False,
    "source_factors_nilpotents_or_multiplicities_discarded":False,
    "finite_values_claimed_char0_expanded_or_global_calibration":False,
    "budget_and_maximum_frame_trials_excluded_from_identity":True}

class BudgetStop(RuntimeError):
    pass

class ScopeStop(RuntimeError):
    pass

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(4*1024*1024),b""):h.update(b)
    return h.hexdigest()

def read(path):
    path=Path(path)
    with (gzip.open if path.suffix==".gz" else open)(path,"rt",encoding="utf-8") as f:
        return json.load(f)

def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".tmp")
    raw=(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n").encode()
    if path.suffix==".gz":
        with tmp.open("wb") as f:
            with gzip.GzipFile(filename="",fileobj=f,mode="wb",mtime=0,compresslevel=2) as z:z.write(raw)
    else:tmp.write_bytes(raw)
    tmp.replace(path)

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def plain(row):
    out={k:row[k] for k in ("file","bytes","sha256")}
    p=PurePosixPath(out["file"])
    assert len(p.parts)==1 and p.name not in ("",".","..") and "\\" not in out["file"]
    assert isinstance(out["bytes"],int) and out["bytes"]>=0 and re.fullmatch("[0-9a-f]{64}",out["sha256"])
    return out

def spec(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}

def identity(source):
    out={**{k:source[k] for k in BASE},"configuration_sha256":source["configuration_sha256"],
         "selected_files_sha256":fingerprint(source["files"]),
         "stage_result_location":source["stage_result_location"]}
    key="certificate" if source.get("certificate") is not None else "configuration_stage"
    out[key]=plain(source[key])
    return out

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"helper_sha256":item["helper_sha256"],
            "python_flint":"0.9.0","p":41,"method_sha256":item["method_sha256"],"proofs":item["proofs"],
            "sources":{g:identity(item["sources"][g]) for g in GROUPS},"inputs":item["inputs"],"strategy":STRATEGY}

def same_source(left,right):
    assert all(str(left[k])==str(right[k]) for k in BASE)
    assert left["configuration_sha256"]==right["configuration_sha256"]

def shape(raw,m,n):
    assert len(raw)==m and all(len(row)==n for row in raw),(m,n)

def matrix(raw):
    return nmod_mat(raw,P)

def rows(mat):
    return [[int(mat[i,j]) for j in range(mat.ncols())] for i in range(mat.nrows())]

class Source:
    def __init__(self,group,item,root):
        self.group,self.item=group,item
        self.folder=Path(root)/group
        self.files={n:plain(r) for n,r in item["files"].items()};self.checked=set()
        assert all(k==r["file"] for k,r in self.files.items())
        assert spec(self.folder/MANIFEST)==self.files[MANIFEST]
        assert self.files[MANIFEST]["sha256"]==item["manifest_sha256"]
        manifest=read(self.folder/MANIFEST)
        assert manifest["result"]==item["result"]
        indexed={r["file"]:plain(r) for r in manifest["files"]}
        assert len(indexed)==len(manifest["files"])
        indexed[MANIFEST]=self.files[MANIFEST]
        assert all(indexed[n]==r for n,r in self.files.items())
        initial=self.raw("public-actions-input.json");run=self.raw("run-receipt.json")
        core=self.raw("core-receipt.json")
        assert initial["source_commit"]==run["source_commit"]==item["source_commit"]
        assert str(run["workflow_run_id"])==str(item["run_id"])
        recorded=initial["core_sha256"] if "core_sha256" in initial else initial["job"]["core_sha256"]
        assert recorded==core["source_sha256"]==item["core_sha256"]
        assert run["core_receipt_sha256"]==self.files["core-receipt.json"]["sha256"]
        self.certificate=None
        if item.get("certificate") is not None:
            self.certificate=self.raw(item["certificate"]["file"])
            assert self.files[item["certificate"]["file"]]==plain(item["certificate"])
            assert self.certificate["complete"] is True and self.certificate["result"]==item["result"]
            assert run["complete"] is True and core["complete"] is True and run["process_exit_code"]==0
            assert core["certificate_sha256"]==item["certificate"]["sha256"]
            self.tag=self.certificate["configuration"]
        else:
            assert group=="R827" and run["complete"] is False and core["complete"] is False
            assert run["process_exit_code"]==124
            anchor=self.raw(item["configuration_stage"]["file"])
            assert anchor["complete"] is True
            self.tag=anchor["configuration"]
        assert fingerprint(self.tag)==item["configuration_sha256"]
        assert self.tag["result"]==item["result"]
        assert self.tag.get("source_sha256",self.tag.get("core_sha256"))==item["core_sha256"]
        if core.get("configuration") is not None:assert core["configuration"]==self.tag
        if core.get("configuration_sha256") is not None:assert core["configuration_sha256"]==item["configuration_sha256"]
        assert item["stage_result_location"]==("configuration" if group=="R827" else "top_level")

    def raw(self,name):
        if name not in self.checked:
            assert spec(self.folder/name)==self.files[name],(self.group,name)
            self.checked.add(name)
        return read(self.folder/name)

    def stage(self,row):
        row=plain(row);assert self.files[row["file"]]==row
        value=self.raw(row["file"])
        assert value["complete"] is True and value["configuration"]==self.tag,(self.group,row["file"])
        if self.item["stage_result_location"]=="configuration":
            assert "result" not in value and value["configuration"]["result"]==self.item["result"]
        else:
            assert value["result"]==self.item["result"]
        return value

class Job:
    def __init__(self,args):
        self.args=args;self.started=time.monotonic();self.out=Path(args.output)
        self.out.mkdir(parents=True,exist_ok=True);self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41 and self.item["producer_inputs_pending"] is False
        assert sha(__file__)==self.item["core_sha256"] and flint.__version__=="0.9.0"
        assert Path(algebra.__file__).name==self.item["helper"] and sha(algebra.__file__)==self.item["helper_sha256"]
        topic=Path(__file__).resolve().parent.parent
        assert sha(topic/self.item["method"])==self.item["method_sha256"]
        for row in self.item["proofs"].values():assert sha(topic/row["path"])==row["sha256"]
        assert set(self.item["sources"])==set(GROUPS)
        self.sources={g:Source(g,self.item["sources"][g],args.retained) for g in GROUPS}
        self.tag=expected_tag(self.item);self.refs={};self.current=None
        self.inputs=self.item["inputs"]
        self.limit=self.item.get("maximum_frame_trials",8)
        assert isinstance(self.limit,int) and 1<=self.limit<=2177
        for key in ("source_functions","correspondence_algebra","fibre_certificate","target_normal_index",
                    "full_target_equations","original_W","original_place","seventeen_coordinates",
                    "same_place_interface","correspondence_DAG","basis_derivative_index",
                    "source_leaf_derivatives","nine_delta_P_coefficients","Euler_trace_row",
                    "full_eight_basis_identity","completed_dotU","exact_R919_DAG"):
            setattr(self,key,self.input(key))
        self.validate_sources()
        self.A=SourceAlgebra(self.source_functions["complete_source_algebra_modulus"])
        self.E=CorrespondenceAlgebra(self.A,[self.A.unpack(x) for x in self.correspondence_algebra["monic_correspondence_coefficients"]])
        self.oldP=[self.A.unpack(v) for v in self.correspondence_algebra["original_P_coefficients"]]
        self.oldK=[self.A.unpack(v) for v in self.correspondence_algebra["original_K_coefficients"]]
        self.oldDeltaP=[self.A.unpack(v) for v in self.nine_delta_P_coefficients["delta_P_coefficients_over_A"]]
        self.D=self.E.unpack(self.correspondence_algebra["Pprime_at_U"])
        self.Dinverse=self.E.unpack(self.correspondence_algebra["Pprime_unit_certificate"]["inverse"])
        self.V=self.E.unpack(self.correspondence_algebra["target_w"])
        self.dotU=self.E.unpack(self.completed_dotU["negative_h_deltaP_over_Pprime_in_E"])
        self.source_audit()

    def input(self,key):
        row=self.inputs[key];return self.sources[row["source_group"]].stage(row)

    def stage_ref(self,row):
        return self.sources[row["source_group"]].stage(row)

    def validate_sources(self):
        old=self.sources["R919"];cert=old.certificate
        assert cert["actual_auxiliary_prime"]==P and cert["original_source_node"]==0
        assert cert["source_algebra_dimension"]==272 and cert["correspondence_rank"]==8
        assert cert["correspondence_scalar_dimension"]==2176
        for flag in ("actual_nine_original_delta_P_values_certified",
                     "actual_complete_A0_linear_Euler_row_certified","actual_all8_trace_basis_identities_verified",
                     "actual_all272_target_normal_differential_traces_computed","whole_source_factors_and_nilpotents_retained"):
            assert cert[flag] is True
        for field in ("basis_derivative_index","source_leaf_derivatives","nine_delta_P_coefficients",
                      "Euler_trace_row","full_eight_basis_identity"):
            assert plain(cert[field])==plain(self.inputs[field])
        assert plain(cert["exact_characteristic_zero_expression_DAG"])==plain(self.inputs["exact_R919_DAG"])
        oldjob=old.raw("public-actions-input.json")["job"]
        assert oldjob["core_sha256"]==old.item["core_sha256"]
        for group in GROUPS:
            if group=="R919":continue
            same_source(old.tag["sources"][group],identity(self.item["sources"][group]))
            same_source(oldjob["sources"][group],self.item["sources"][group])
            for name,row in self.item["sources"][group]["files"].items():
                assert oldjob["sources"][group]["files"][name]==row,(group,name)
        for key in ("source_functions","correspondence_algebra","fibre_certificate","target_normal_index",
                    "full_target_equations","original_W","original_place","seventeen_coordinates",
                    "same_place_interface","correspondence_DAG","target_normal_blocks"):
            assert self.inputs[key]==oldjob["inputs"][key],key
        s=self.source_functions;c=self.correspondence_algebra;f=self.fibre_certificate
        assert s["source_node_ordinal"]==0 and s["source_node_value"]==0 and s["prime"]==P
        assert s["source_algebra_dimension"]==272 and s["all2058_functions_consumed"] is True
        assert s["original82_scales_retained_once"] is True and s["new_scale_applied"]=="1"
        assert s["column_order"]=="P0..P8,K0..K7" and s["complete_fibre_factors_or_multiplicities_removed"] is False
        shape(s["seventeen_values_over_A"],17,272)
        assert plain(s["source_seventeen_coordinates"])==plain(self.inputs["seventeen_coordinates"])
        assert plain(s["source_DAG"])==plain(self.inputs["correspondence_DAG"])
        assert c["original_P_coefficients"]==s["seventeen_values_over_A"][:9]
        assert c["original_K_coefficients"]==s["seventeen_values_over_A"][9:]
        assert c["base_algebra_dimension"]==272 and c["correspondence_rank"]==8 and c["full_scalar_dimension"]==2176
        assert c["full_Pprime_times_target_w_equals_K_verified"] is True
        assert c["any_source_factor_or_multiplicity_discarded"] is False
        assert c["leading_coefficient_unit_certificate"]["whole_fibre_unit"] is True
        assert c["Pprime_unit_certificate"]["whole_fibre_unit"] is True
        assert plain(c["source_functions"])==plain(self.inputs["source_functions"])
        shape(c["Pprime_at_U"],8,272);shape(c["target_w"],8,272)
        assert f["whole_fibre_success"] is True and f["all_required_units_on_entire_algebras_verified"] is True
        assert f["all272_original_target_normal_coordinates_certified"] is True
        for field,key in (("source_functions","source_functions"),("correspondence_algebra","correspondence_algebra"),
                          ("target_normal_row","target_normal_index"),("full_target_equations","full_target_equations")):
            assert plain(f[field])==plain(self.inputs[key])
        idx=self.target_normal_index
        assert idx["all272_target_normal_coordinates_computed"] is True and idx["target_gamma0_equals_one"] is True
        assert len(idx["blocks"])==len(self.inputs["target_normal_blocks"])==17
        for ordinal,(part,ref) in enumerate(zip(idx["blocks"],self.inputs["target_normal_blocks"])):
            assert part["normal_columns"]==[16*ordinal,min(16*ordinal+16,272)]
            assert plain(part["source"])==plain(ref)
        assert self.full_target_equations["all272_original_target_equations_verified"] is True
        assert self.full_target_equations["all2176_scalar_coordinates_of_each_equation_checked"] is True
        assert self.full_target_equations["no_factor_or_nilpotent_component_discarded"] is True
        place=self.original_place
        assert place["prime"]==P and place["original_zeta_root"]==549966761 and place["original_s_root"]==99932770
        assert place["original_integral_B_root"]==3197390 and place["original_branch"]==0
        assert self.original_W["prime"]==P and self.original_W["original_rational_denominators_all_units"] is True
        for field in ("g_vector_coefficients_mod_prime","h_vector_coefficients_mod_prime"):
            shape(self.original_W[field],4,272)
        cc=self.seventeen_coordinates
        assert cc["prime"]==P and cc["same_characteristic_zero_coefficients_integral_at_new_place"] is True
        shape(cc["coordinate_matrix_mod_prime"],2058,17)
        dag=self.correspondence_DAG
        assert plain(cc["source_exact_R873_unit_solve"])==plain(dag["coefficient_unit_solve"])
        assert self.same_place_interface["all2200_by17_original_equations_verified"] is True
        assert self.same_place_interface["prime"]==P and self.same_place_interface["original_zeta_root"]==549966761
        assert plain(self.same_place_interface["new_modular_coordinates"])==plain(self.inputs["seventeen_coordinates"])
        assert plain(self.same_place_interface["source_R873_correspondence_DAG"])==plain(self.inputs["correspondence_DAG"])
        assert dag["exact_original_correspondence_expression_certified"] is True
        assert dag["rigidified_Hecke_transport"]["frozen_direction"]=="Nm_pi_t(pi_s^*I)"
        assert dag["P_over_tau8_coefficients"]=={"powers_U":list(range(9)),"unit_solve_columns":list(range(9))}
        ix=self.basis_derivative_index
        assert ix["basis_dimension"]==2058 and ix["all2058_original_basis_derivatives_evaluated"] is True
        assert plain(ix["source_original_DAG"])==plain(self.inputs["correspondence_DAG"])
        expected=[(i,min(i+64,2058)) for i in range(0,2058,64)]
        assert [(p["first"],p["stop"]) for p in ix["blocks"]]==expected
        assert len(self.inputs["basis_derivative_blocks"])==33
        for part,ref in zip(ix["blocks"],self.inputs["basis_derivative_blocks"]):
            assert plain(part["source"])==plain(ref)
        leaf=self.source_leaf_derivatives
        assert leaf["derivation_applied_before_fibre_reduction"] is True and leaf["delta_claimed_to_descend_to_A0"] is False
        assert leaf["old_source_values_or_inverse_recomputed"] is False
        assert plain(leaf["source_DAG"])==plain(self.inputs["correspondence_DAG"])
        dp=self.nine_delta_P_coefficients
        assert plain(dp["source_basis_derivatives"])==plain(self.inputs["basis_derivative_index"])
        assert plain(dp["source_original_seventeen_coordinates"])==plain(self.inputs["seventeen_coordinates"])
        assert dp["coefficient_indices"]==list(range(9))
        shape(dp["delta_P_coefficients_over_A"],9,272)
        assert dp["all2058_rows_and_nine_original_P_columns_consumed"] is True
        assert dp["delta_K_or_new_coefficient_solve_computed"] is False
        row=self.Euler_trace_row
        assert plain(row["source_original_correspondence"])==plain(self.inputs["correspondence_algebra"])
        assert plain(row["source_nine_delta_P_coefficients"])==plain(self.inputs["nine_delta_P_coefficients"])
        assert row["input_frame"]=="dz_target" and row["output_frame"]=="nu_source"
        assert row["a8_inverse_reused_from_original_complete_certificate"] is True
        tr=self.full_eight_basis_identity
        assert tr["all8_basis_identities_in_entire_A0_verified"] is True
        assert plain(tr["source_Euler_row"])==plain(self.inputs["Euler_trace_row"])
        assert plain(tr["basis_certificates"][0])==plain(self.inputs["completed_dotU"])
        du=self.completed_dotU
        assert du["basis_U_power"]==0
        assert plain(du["source_Euler_row"])==plain(self.inputs["Euler_trace_row"])
        assert plain(du["source_original_Pprime_inverse"])==plain(self.inputs["correspondence_algebra"])
        assert du["complete_all272_coordinate_equality_verified"] is True and du["new_inverse_computed"] is False
        shape(du["negative_h_deltaP_over_Pprime_in_E"],8,272)
        assert self.exact_R919_DAG["exact_characteristic_zero_expression_defined"] is True
        assert self.exact_R919_DAG["finite_fibre_values_substituted_for_global_functions"] is False
        assert self.exact_R919_DAG["original_rigidified_Hecke_transport"]==dag["rigidified_Hecke_transport"]

    def budget(self):
        if time.monotonic()-self.started>=60*self.args.budget_minutes:
            raise BudgetStop("R928 budget; completed new contractions and unit trials remain reusable.")

    def path(self,name):
        return self.out/(PREFIX+name+".json.gz")

    def old(self,name):
        path=self.path(name)
        if not path.exists():return None
        value=read(path)
        assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
        self.refs[name]=spec(path);return value

    def put(self,name,value):
        payload={"result":RESULT,"configuration":self.tag,"complete":True,**value}
        path=self.path(name)
        if path.exists():assert read(path)==payload
        else:save(path,payload)
        self.refs[name]=spec(path);return payload

    def checkpoint(self,phase):
        save(self.path("current"),{"result":RESULT,"complete":False,"configuration":self.tag,
             "phase":phase,"completed_stages":self.refs})
        self.current=spec(self.path("current"))

    def source_audit(self):
        if self.old("source-audit") is None:
            self.put("source-audit",{
                "sources":{g:identity(self.item["sources"][g]) for g in GROUPS},"inputs":self.inputs,
                "original_source_z":0,"prime":P,"source_algebra_dimension":272,"correspondence_scalar_dimension":2176,
                "original_82_scales_retained_once":True,"old_complete_p753_source_identities_verified":True,
                "all_source_arrays_are_actual_completed_outputs":True,
                "historical_R827_result_in_configuration_preserved":True,
                "old_33_derivative_blocks_nine_deltaP_dotU_a8_PU_and_target_coordinates_reused":True,
                "original_Gamma_blocks_not_required_or_recomputed":True})
        self.checkpoint("sources")
    def delta_K(self):
        aggregate=self.old("eight-original-delta-K-coefficients")
        if aggregate is not None:
            assert aggregate["source_basis_derivatives"]==self.inputs["basis_derivative_index"]
            assert aggregate["source_original_seventeen_coordinates"]==self.inputs["seventeen_coordinates"]
            shape(aggregate["delta_K_coefficients_over_A"],8,272)
            return [self.A.unpack(v) for v in aggregate["delta_K_coefficients_over_A"]]
        parts=[]
        for part,ref in zip(self.basis_derivative_index["blocks"],self.inputs["basis_derivative_blocks"]):
            first,stop=part["first"],part["stop"]
            name=f"delta-K-contraction-{first:04d}-{stop:04d}";value=self.old(name)
            if value is None:
                self.budget();source=self.stage_ref(ref)
                assert source["first"]==first and source["stop"]==stop
                assert plain(source["source_original_DAG"])==plain(self.inputs["correspondence_DAG"])
                assert plain(source["source_original_values"])==plain(self.inputs["source_functions"])
                assert plain(source["source_new_leaf_derivatives"])==plain(self.inputs["source_leaf_derivatives"])
                assert source["product_and_quotient_rules_include_all_original_factors"] is True
                assert source["old_complete_V8_values_recomputed"] is False and source["old_input_scales_changed"] is False
                values=source["delta_basis_values_over_A"];shape(values,stop-first,272)
                constants=[row[9:17] for row in self.seventeen_coordinates["coordinate_matrix_mod_prime"][first:stop]]
                image=matrix(values).transpose()*matrix(constants)
                value=self.put(name,{"source_completed_basis_derivative_block":ref,
                    "source_original_seventeen_coordinates":self.inputs["seventeen_coordinates"],
                    "first":first,"stop":stop,"original_coordinate_columns":list(range(9,17)),
                    "contributions_to_eight_delta_K_over_A":[[int(image[i,j]) for i in range(272)] for j in range(8)],
                    "old_basis_function_derivatives_recomputed":False,"old_nine_delta_P_recomputed":False})
            assert value["source_completed_basis_derivative_block"]==ref
            shape(value["contributions_to_eight_delta_K_over_A"],8,272)
            parts.append(self.refs[name]);self.checkpoint(name)
        self.budget();answer=[self.A.zero for _ in range(8)]
        for ref in parts:
            value=read(self.out/ref["file"])
            for i,row in enumerate(value["contributions_to_eight_delta_K_over_A"]):
                answer[i]=self.A.add(answer[i],self.A.unpack(row))
        self.put("eight-original-delta-K-coefficients",{
            "source_basis_derivatives":self.inputs["basis_derivative_index"],
            "source_original_seventeen_coordinates":self.inputs["seventeen_coordinates"],
            "source_original_same_place_certificate":self.inputs["same_place_interface"],
            "completed_contractions":parts,"original_coordinate_columns":list(range(9,17)),
            "numerator_powers_U":list(range(8)),"delta_K_coefficients_over_A":[self.A.pack(v) for v in answer],
            "all2058_rows_and_original_eight_numerator_columns_consumed":True,
            "original_K_is_numerator_not_target_w":True,"derivative_of_original_unit_solve_constants_is_zero":True,
            "old_2058_derivatives_and_nine_deltaP_recomputed":False})
        self.checkpoint("eight-original-delta-K-coefficients")
        return answer

    def quotient_derivative(self,deltaK):
        name="whole-quotient-derivative";value=self.old(name);A=self.A;E=self.E
        if value is None:
            self.budget()
            dK=E.element(deltaK)
            KU=E.element([A.scale(self.oldK[i],i) for i in range(1,8)])
            dPU=E.element([A.scale(self.oldDeltaP[i],i) for i in range(1,9)])
            PUU=E.element([A.scale(self.oldP[i],i*(i-1)) for i in range(2,9)])
            Delta=E.sub(dK,E.mul(self.V,dPU))
            H=E.sub(KU,E.mul(self.V,PUU))
            dotV=E.mul(self.Dinverse,E.add(Delta,E.mul(H,self.dotU)))
            left=E.add(E.mul(self.D,dotV),E.mul(self.V,E.add(dPU,E.mul(PUU,self.dotU))))
            right=E.add(dK,E.mul(KU,self.dotU))
            assert left==right
            value=self.put(name,{
                "source_new_eight_delta_K":self.refs["eight-original-delta-K-coefficients"],
                "source_completed_nine_delta_P":self.inputs["nine_delta_P_coefficients"],
                "source_completed_dotU":self.inputs["completed_dotU"],
                "source_original_P_K_PU_inverse_V":self.inputs["correspondence_algebra"],
                "delta_K_at_U":E.pack(dK),"K_U_at_U":E.pack(KU),
                "delta_P_U_at_U":E.pack(dPU),"P_UU_at_U":E.pack(PUU),
                "Delta_K_at_U":E.pack(Delta),"H_K_at_U":E.pack(H),"dotV_over_E":E.pack(dotV),
                "quotient_identity_left":E.pack(left),"quotient_identity_right":E.pack(right),
                "complete_2176_coordinate_quotient_identity_verified":True,
                "original_V_definition":"K(U)/P_U(U)",
                "dotV_formula":"P_U_inverse*(deltaK+K_U*dotU-V*(deltaP_U+P_UU*dotU))",
                "derivative_before_specialization":True,"delta_claimed_to_descend_to_A0":False,
                "old_PU_inverse_dotU_nine_deltaP_or_Gamma_recomputed":False})
        assert value["source_new_eight_delta_K"]==self.refs["eight-original-delta-K-coefficients"]
        assert value["complete_2176_coordinate_quotient_identity_verified"] is True
        shape(value["dotV_over_E"],8,272);self.checkpoint(name)
        return E.unpack(value["dotV_over_E"])

    def target_g_h(self):
        name="whole-target-g-h";value=self.old(name);E=self.E
        if value is not None:
            assert value["source_original_W_g_h"]==self.inputs["original_W"]
            return E.unpack(value["g_target_over_E"]),E.unpack(value["h_target_over_E"])
        parts=[]
        g=self.original_W["g_vector_coefficients_mod_prime"]
        h=self.original_W["h_vector_coefficients_mod_prime"]
        for ref in self.inputs["target_normal_blocks"]:
            source=self.stage_ref(ref);first,stop=source["normal_columns"]
            blockname=f"target-g-h-contraction-{first:03d}-{stop:03d}";block=self.old(blockname)
            if block is None:
                self.budget();raw=source["normal_values_over_E"]
                assert len(raw)==stop-first
                for x in raw:shape(x,8,272)
                flat=[[c for row in x for c in row] for x in raw]
                constants=[[g[k][j] for k in range(4)]+[h[k][j] for k in range(4)] for j in range(first,stop)]
                image=matrix(flat).transpose()*matrix(constants)
                vectors=[E.pack(E.from_flat([int(image[i,j]) for i in range(2176)])) for j in range(8)]
                block=self.put(blockname,{
                    "normal_columns":[first,stop],"source_original_target_normal_block":ref,
                    "source_original_W_g_h":self.inputs["original_W"],
                    "four_g_coefficient_contributions_over_E":vectors[:4],
                    "four_h_coefficient_contributions_over_E":vectors[4:],
                    "target_functions_not_source_z0_specializations":True,
                    "original_target_normal_coordinates_recomputed":False})
            assert block["source_original_target_normal_block"]==ref
            parts.append(self.refs[blockname]);self.checkpoint(blockname)
        self.budget();acc=[[E.zero for _ in range(4)] for _ in range(2)]
        for ref in parts:
            block=read(self.out/ref["file"])
            for q,field in enumerate(("four_g_coefficient_contributions_over_E","four_h_coefficient_contributions_over_E")):
                assert len(block[field])==4
                for k,row in enumerate(block[field]):acc[q][k]=E.add(acc[q][k],E.unpack(row))
        result=[]
        for coeffs in acc:
            value=E.zero
            for coefficient in reversed(coeffs):value=E.add(E.mul_U(value),coefficient)
            result.append(value)
        self.put(name,{"source_original_W_g_h":self.inputs["original_W"],
            "source_all272_target_normal_index":self.inputs["target_normal_index"],
            "source_original_full_target_equations":self.inputs["full_target_equations"],
            "completed_contractions":parts,
            "original_normal_coefficient_powers":[0,1,2,3],
            "g_target_over_E":E.pack(result[0]),"h_target_over_E":E.pack(result[1]),
            "all272_original_target_normal_coordinates_consumed":True,
            "complete_rank8_over_entire_A0_preserved":True,
            "target_functions_not_source_z0_specializations":True,
            "old_target_normal_or_Gamma_recomputed":False})
        self.checkpoint(name);return tuple(result)

    def frame_transport(self,dotV,g,h):
        E=self.E;name="complete-target-differential-transport";done=self.old(name)
        if done is not None:
            assert done["source_quotient_derivative"]==self.refs["whole-quotient-derivative"]
            assert done["source_target_g_h"]==self.refs["whole-target-g-h"]
            assert done["both_complete2176_transport_identities_verified"] is True
            return done
        trials=[]
        for t in range(self.limit):
            trialname=f"frame-unit-trial-{t:04d}";trial=self.old(trialname)
            if trial is None:
                self.budget();ell=E.add(g,E.scale(h,t))
                try:
                    inverse,proof=E.inverse(ell,"original_target_g_plus_t_h_"+str(t))
                    trial=self.put(trialname,{
                        "t":t,"source_target_g_h":self.refs["whole-target-g-h"],
                        "ell_over_E":E.pack(ell),"whole_E_unit":True,"unit_certificate":proof,
                        "complete_original_2176_dimensional_algebra_preserved":True,
                        "factors_or_nilpotents_removed":False})
                except UnitFailure as exc:
                    trial=self.put(trialname,{
                        "t":t,"source_target_g_h":self.refs["whole-target-g-h"],
                        "ell_over_E":E.pack(ell),"whole_E_unit":False,"unit_certificate":exc.witness,
                        "complete_original_2176_dimensional_algebra_preserved":True,
                        "factors_or_nilpotents_removed":False})
            assert trial["t"]==t and trial["source_target_g_h"]==self.refs["whole-target-g-h"]
            trials.append(self.refs[trialname]);self.checkpoint(trialname)
            if not trial["whole_E_unit"]:continue
            self.budget();ell=E.unpack(trial["ell_over_E"]);inverse=E.unpack(trial["unit_certificate"]["inverse"])
            J=E.mul(E.add(self.dotU,E.scale(dotV,t)),inverse)
            Jg=E.mul(J,g);Jh=E.mul(J,h)
            assert Jg==self.dotU and Jh==dotV
            done=self.put(name,{
                "selected_t":t,"trials_in_original_integer_order":trials,
                "selected_whole_E_unit_trial":self.refs[trialname],
                "source_quotient_derivative":self.refs["whole-quotient-derivative"],
                "source_target_g_h":self.refs["whole-target-g-h"],
                "source_completed_dotU":self.inputs["completed_dotU"],
                "J_over_E":E.pack(J),"J_g_target_over_E":E.pack(Jg),"J_h_target_over_E":E.pack(Jh),
                "both_complete2176_transport_identities_verified":True,
                "whole_E_ell_unit_certified":True,
                "source_differential_frame":"nu_source","target_differential_frame":"nu_target",
                "J_definition":"pullback(nu_target)/pullback(nu_source)",
                "J_inverse_computed":False,"J_unit_not_claimed":True,
                "all_ramification_nilpotents_and_original_frames_preserved":True,
                "canonical_dual7_scalar7_diamond_and_original_minus3_descent_preserved":True,
                "kappa_nu_endpoint_constants_replaced_or_evaluated":False})
            self.checkpoint(name);return done
        raise ScopeStop("No whole-E unit g_target+t*h_target in the completed deterministic prefix; all factors retained.")

    def exact_expression(self):
        name="original-characteristic-zero-target-transport-DAG"
        if self.old(name) is not None:return
        d=self.correspondence_DAG
        self.put(name,{
            "source_original_correspondence_DAG":self.inputs["correspondence_DAG"],
            "source_completed_R919_expression":self.inputs["exact_R919_DAG"],
            "source_R922_proof":self.item["proofs"]["R922"],
            "original_coefficient_unit_solve":d["coefficient_unit_solve"],
            "original_function_field":d["correspondence_function_field"],
            "eight_numerator_derivative_nodes":[{"operation":"original_derivation_before_specialization",
                "input":{"operation":"original_2058_basis_linear_combination",
                    "basis_source":self.inputs["correspondence_DAG"],
                    "exact_unit_solve":d["coefficient_unit_solve"],"unit_solve_column":9+i,"U_power":i}}
                for i in range(8)],
            "old_dotU":{"operation":"reuse_exact_negative_deltaP_over_P_U",
                "source":self.inputs["exact_R919_DAG"],"actual_value":self.inputs["completed_dotU"]},
            "target_w":{"operation":"divide","numerator":"K(U)","denominator":"P_U(U)",
                "source":self.inputs["correspondence_DAG"]},
            "dotV":{"operation":"full_quotient_derivative","formula":
                "P_U^-1*(deltaK+K_U*dotU-V*(deltaP_U+P_UU*dotU))",
                "deltaP_U":"formal_U_derivative_of_the_completed_nine_deltaP",
                "P_UU":"second_formal_U_derivative_of_original_P","old_P_U_inverse":self.inputs["correspondence_algebra"]},
            "target_g_h":{"operation":"evaluate_actual_original_normal_functions_at_target_U_V",
                "source_normal_functions":self.inputs["original_W"],
                "source_completed_target_normal_coordinates":self.inputs["target_normal_index"],
                "original_characteristic_zero_g_h_definition_retained":True,
                "modular_vectors_claimed_characteristic_zero_expansions":False},
            "transport":{"operation":"divide_linear_combination_of_dotU_dotV_by_target_g_h",
                "formula":"J=(dotU+t*dotV)/(g_target+t*h_target)",
                "required_unit":"g_target+t*h_target on the entire E",
                "required_products":["J*g_target=dotU","J*h_target=dotV"],
                "source_frame":"nu_source","target_frame":"nu_target",
                "J_inverse_required":False},
            "original_rigidified_Hecke_transport":d["rigidified_Hecke_transport"],
            "original_cY":d["original_cY"],
            "canonical_dual7_transports_both_determinant_frames":True,
            "scalar7_diamond_original_minus3_descent_and_kappa_nu_retained":True,
            "exact_original_characteristic_zero_expression_defined":True,
            "actual_characteristic_zero_derivative_coordinates_expanded":False,
            "original_Gamma_characteristic_zero_expanded":False,
            "finite_fibre_values_substituted_for_global_functions":False,
            "seven_connections_Hecke_calibration_nonp_period_or_height_computed":False})
        self.checkpoint(name)

    def manifest(self):
        entries=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name==PREFIX+"current.json.gz" or path.name.startswith(PREFIX+"stage-manifest-"):continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
            entries.append(spec(path))
        current=spec(self.path("current")) if self.path("current").exists() else None
        value={"result":RESULT,"complete":True,"configuration":self.tag,"files":entries,
               "current_checkpoints":[] if current is None else [current]}
        target=self.path("stage-manifest-"+fingerprint(value))
        if target.exists():assert read(target)==value
        else:save(target,value)
        return spec(target)

    def finish(self,complete,error):
        mapping={"source_audit":"source-audit","eight_delta_K_coefficients":"eight-original-delta-K-coefficients",
                 "whole_quotient_derivative":"whole-quotient-derivative","whole_target_g_h":"whole-target-g-h",
                 "target_differential_transport":"complete-target-differential-transport",
                 "exact_characteristic_zero_expression_DAG":"original-characteristic-zero-target-transport-DAG"}
        for name in mapping.values():
            if complete:assert self.old(name) is not None
            elif self.path(name).exists():self.old(name)
        result={"result":RESULT,"complete":bool(complete),"configuration":self.tag,"p":41,
            "actual_auxiliary_prime":P,"original_source_node":0,"source_algebra_dimension":272,
            "correspondence_rank":8,"correspondence_scalar_dimension":2176,
            **{key:self.refs.get(name) for key,name in mapping.items()},
            "actual_eight_original_numerator_delta_K_values_certified":self.refs.get("eight-original-delta-K-coefficients") is not None,
            "actual_full_quotient_derivative_identity_verified":self.refs.get("whole-quotient-derivative") is not None,
            "actual_target_g_h_on_whole_E_computed":self.refs.get("whole-target-g-h") is not None,
            "actual_whole_E_target_frame_unit_and_both_transport_identities_certified":bool(complete),
            "original_V_equals_K_over_P_U_preserved":True,
            "whole_source_factors_and_nilpotents_retained":True,
            "J_inverse_computed":False,"J_unit_not_claimed":True,
            "old_2058_derivatives_nine_deltaP_dotU_a8_PU_Gamma_or_target_coordinates_recomputed":False,
            "actual_characteristic_zero_derivative_coordinates_expanded":False,
            "actual_original_Gamma_characteristic_zero_expanded":False,
            "seven_connection_numerator_evaluations_computed":False,
            "original_Hecke_projector_or_endpoint_calibration_computed":False,
            "nonp_terms_Poincare_period_or_height_computed":False,
            "stage_manifest":self.manifest(),"resume_state":self.current,
            "failure_or_stop_reason":error,"maximum_frame_trials_requested":self.limit,
            "seconds":time.monotonic()-self.started}
        save(self.out/FINAL,result);return result

    def run(self):
        self.exact_expression()
        dK=self.delta_K()
        dotV=self.quotient_derivative(dK)
        g,h=self.target_g_h()
        self.frame_transport(dotV,g,h)
        return self.finish(True,None)

def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise SystemExit("R928 new arithmetic runs only in the authorized public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    for name in ("config","retained","output"):parser.add_argument("--"+name,required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args();assert 0<args.budget_minutes<=300
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    job=None;code=1;error=None;started=time.monotonic()
    try:
        job=Job(args);certificate=job.run();code=0 if certificate["complete"] else 2
    except BudgetStop as exc:code=124;error=str(exc)
    except ScopeStop as exc:code=2;error=str(exc)
    except Exception as exc:error=type(exc).__name__+": "+str(exc);traceback.print_exc()
    if code in (1,2,124) and job is not None:job.finish(False,error)
    receipt={"result":RESULT,"source_sha256":sha(__file__),"helper_sha256":sha(algebra.__file__),
        "complete":code==0,"process_exit_code":code,"error":error,"seconds":time.monotonic()-started,
        "configuration":None if job is None else job.tag,
        "certificate_sha256":sha(out/FINAL) if (out/FINAL).exists() else None,
        "new_arithmetic_only_in_public_Actions":True}
    save(out/"core-receipt.json",receipt)
    log={k:v for k,v in receipt.items() if k!="configuration"}
    log["configuration_sha256"]=None if job is None else fingerprint(job.tag)
    print("R928_CORE_RECEIPT="+json.dumps(log,sort_keys=True),flush=True)
    raise SystemExit(code)
if __name__=="__main__":main()
