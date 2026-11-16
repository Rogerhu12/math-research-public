#!/usr/bin/env python3
"""R930: seven original connection values and differential traces on the whole Artin correspondence."""
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
RESULT="R930-original-seven-whole-Artin-connection-traces"
FINAL="p41-original-seven-whole-Artin-connection-traces-certificate.json"
PREFIX="R930-"
MANIFEST="full-outputs-manifest.json"
P=1000000753
N=272
EPS=[0]+[1]*144+[2]*127
LABELS=("D1","D2","D3","D4","D5","X","DN")
BLOCK=16
GROUPS=("R922","R926","R928","R905","R885","R919")
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
STRATEGY={
    "original_curve":"original genus127 Y, level82, original minus3 descent",
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "source_node_ordinal":0,"source_z":0,"source_algebra_dimension":272,"whole_correspondence_rank":8,
    "divisor_order":list(LABELS),"normal_basis_degrees":EPS,
    "connection":"alpha_D=(y_D^t*R*beta/d_D)*nu with the original R905 gauge and section1",
    "new_global_contraction":"r_D=y_D^t R, coefficient bound274-epsilon_j",
    "polynomial_product_coefficients_checked":277,"contraction_block_size":BLOCK,
    "target_substitution":"matrix-contract all272 completed target beta, then U-Horner; never source-specialize coefficients",
    "denominator":"full d_D(U) unit on all of E, no factor cancellation claimed",
    "differential_transport":"reuse the completed original R928 J and its two full identities",
    "trace":"whole rank8 multiplication trace on B_D*J",
    "ordinary_trace_row":"old_a8_inverse*[U^7](U^i*old_P_U mod old_monic_P), all8 checked by full multiplication",
    "second_trace_identity":"old_L(B*ell^-1*(1+t*old_PU^-1*H_K))+t*T(B*ell^-1*old_PU^-1*Delta_K)",
    "old_R_G_y_d_J_deltaK_deltaP_inverses_Gamma_or_target_coordinates_recomputed":False,
    "source_factors_nilpotents_or_multiplicities_discarded":False,
    "J_inverse_or_J_unit_required":False,
    "five_Picard_sigma_cY_or_principal_combinations_computed":False,
    "budget_and_maximum_divisors_excluded_from_identity":True}

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
        self.tag=expected_tag(self.item);self.refs={};self.current=None;self.done={};self.failed={}
        self.inputs=self.item["inputs"];self.limit=self.item.get("maximum_divisors",7)
        assert isinstance(self.limit,int) and 1<=self.limit<=7
        for key in ("R_low_weight_polynomial","R_complete_identity","R_exact_expression",
                    "source_functions","correspondence_algebra","fibre_certificate","target_normal_index",
                    "full_target_equations","Euler_trace_row","full_eight_basis_identity",
                    "target_transport","target_quotient_derivative","target_g_h","target_frame_unit",
                    "exact_transport_DAG"):
            setattr(self,key,self.input(key))
        self.divisors={label:{k:self.stage_ref(r) for k,r in self.inputs["divisors"][label].items()} for label in LABELS}
        self.validate_sources()
        self.A=SourceAlgebra(self.source_functions["complete_source_algebra_modulus"])
        self.E=CorrespondenceAlgebra(self.A,[self.A.unpack(v) for v in self.correspondence_algebra["monic_correspondence_coefficients"]])
        self.R=[matrix(x) for x in self.R_low_weight_polynomial["coefficient_matrices_low_to_high"]]
        target=[]
        for ref in self.inputs["target_normal_blocks"]:
            self.budget();block=self.stage_ref(ref);first,stop=block["normal_columns"]
            assert first==len(target) and stop==first+16
            for row in block["normal_values_over_E"]:
                shape(row,8,272);target.append([x for part in row for x in part])
        shape(target,272,2176);self.target_matrix=matrix(target)
        self.J=self.E.unpack(self.target_transport["J_over_E"])
        self.D=self.E.unpack(self.correspondence_algebra["Pprime_at_U"])
        self.Dinv=self.E.unpack(self.correspondence_algebra["Pprime_unit_certificate"]["inverse"])
        self.a8inv=self.A.unpack(self.correspondence_algebra["leading_coefficient_unit_certificate"]["inverse"])
        self.oldL=[self.A.unpack(v) for v in self.Euler_trace_row["linear_functional_coefficients_over_A"]]
        self.frame_inverse=self.E.unpack(self.target_frame_unit["unit_certificate"]["inverse"])
        self.frame_t=self.target_transport["selected_t"]
        self.Delta=self.E.unpack(self.target_quotient_derivative["Delta_K_at_U"])
        self.H=self.E.unpack(self.target_quotient_derivative["H_K_at_U"])
        self.source_audit()

    def input(self,key):
        return self.stage_ref(self.inputs[key])

    def stage_ref(self,row):
        return self.sources[row["source_group"]].stage(row)

    def validate_sources(self):
        cr=self.sources["R922"].certificate;cy=self.sources["R926"].certificate
        cj=self.sources["R928"].certificate;cd=self.sources["R905"].certificate
        assert cr["actual_original_low_weight_R_mod_p_certified"] is True
        assert cr["actual_all_polynomial_RG_equal_Mg_entries_verified"] is True
        for field,key in (("polynomial_low_weight_R","R_low_weight_polynomial"),
                          ("complete_polynomial_identity","R_complete_identity"),
                          ("exact_original_trace_dual_expression","R_exact_expression")):
            assert plain(cr[field])==plain(self.inputs[key])
        R=self.R_low_weight_polynomial;proof=self.R_complete_identity
        assert R["prime"]==P and R["normal_basis_rank"]==272 and R["normal_basis_degrees"]==EPS
        assert R["coefficient_count"]==4 and len(R["coefficient_matrices_low_to_high"])==4
        for part in R["coefficient_matrices_low_to_high"]:shape(part,272,272)
        for field in ("negative_weight_bound_entries_are_zero","all_weighted_degree_zeros_verified",
                      "full_matrix_symmetry_verified","all_127_by127_weight_two_block_entries_zero"):
            assert R[field] is True
        assert plain(proof["source_R_polynomial"])==plain(self.inputs["R_low_weight_polynomial"])
        assert proof["whole_polynomial_R_times_G_equals_original_Mg_verified"] is True
        assert proof["all_eight_z_coefficients_checked"] is True
        assert proof["true_original_trace_dual_identified_by_nonzero_Gram"] is True
        assert self.R_exact_expression["exact_characteristic_zero_expression_defined"] is True
        assert self.R_exact_expression["normal_trace_dual"]["r_j"]=="g*beta_j_star"
        assert self.R_exact_expression["target_coordinate_reminder"]=="V=K(U)/P_U(U), eight K columns are numerators"
        assert cy["actual_seven_original_bounded_connection_numerators_certified"] is True
        assert cy["source_divisor_order"]==list(LABELS)
        assert cd["actual_seven_complete_full_principal_parts_solutions"] is True
        assert cd["actual_completed_source_connections"]==7
        same_source(self.sources["R926"].tag["sources"]["R905"],identity(self.item["sources"]["R905"]))
        old_r827=self.sources["R928"].tag["sources"]["R827"]
        same_source(self.sources["R922"].tag["sources"]["R827"],old_r827)
        same_source(self.sources["R905"].tag["sources"]["R827"],old_r827)
        for group in ("R922","R926","R928"):
            assert self.sources[group].tag["proofs"]["R922"]==self.item["proofs"]["R922"]
        for label in LABELS:
            refs=self.inputs["divisors"][label];data=self.divisors[label]
            assert set(refs)=={"certificate","denominator","numerator"}
            complete=data["certificate"];den=data["denominator"];num=data["numerator"]
            assert plain(cy["complete_bounded_connection_certificates"][label])==plain(refs["certificate"])
            assert plain(complete["source_original_connection"])==plain(cd["complete_source_connection_certificates"][label])
            for value in (complete,den,num):assert value["prime"]==P and value["label"]==label
            assert plain(complete["denominator"])==plain(refs["denominator"])
            assert plain(complete["bounded_numerator"])==plain(refs["numerator"])
            for flag in ("all277_coefficients_times272_rows_verified",
                         "full_original_F_transpose_times_y_equals_d_times_c_verified",
                         "all_original_numerator_degree_bounds_verified",
                         "original_543_gauge_and_full_logarithmic_principal_parts_preserved",
                         "whole_D_norm_all_length272_multiplicities_preserved"):
                assert complete[flag] is True
            assert complete["characteristic_zero_numerator_denominator_coordinates_expanded"] is False
            assert complete["exact_characteristic_zero_expression"]["alpha"]=="sum_i (y_i/d)*beta_i_trace_dual*dz"
            assert complete["exact_characteristic_zero_expression"]["proof"]==self.item["proofs"]["R922"]
            assert plain(num["source_denominator"])==plain(refs["denominator"])
            assert plain(num["source_original_connection"])==plain(complete["source_original_connection"])
            assert num["normal_basis_degrees"]==EPS and num["numerator_degree_bounds"]==[271+e for e in EPS]
            assert num["all_original_weighted_numerator_degree_bounds_verified"] is True
            shape(num["numerator_coefficients_in_z_low_to_high"],274,272)
            assert len(den["denominator_coefficients_in_z_low_to_high"])==273
            assert den["full_rank272_characteristic_polynomial_computed"] is True
            assert den["denominator_is_det_I_minus_tZ"] is True
            assert den["normalization_and_all_multiplicities_preserved"] is True
            assert den["nilpotent_zero_eigenparts_not_removed"] is True
            assert den["same_original_determinant_ratio_expression"]=="det(F(z))/det(F(a))"
        for flag in ("actual_eight_original_numerator_delta_K_values_certified",
                     "actual_full_quotient_derivative_identity_verified","actual_target_g_h_on_whole_E_computed",
                     "actual_whole_E_target_frame_unit_and_both_transport_identities_certified",
                     "original_V_equals_K_over_P_U_preserved","whole_source_factors_and_nilpotents_retained"):
            assert cj[flag] is True
        for field,key in (("target_differential_transport","target_transport"),
                          ("whole_quotient_derivative","target_quotient_derivative"),
                          ("whole_target_g_h","target_g_h"),
                          ("exact_characteristic_zero_expression_DAG","exact_transport_DAG")):
            assert plain(cj[field])==plain(self.inputs[key])
        j=self.target_transport;q=self.target_quotient_derivative;u=self.target_frame_unit
        assert j["both_complete2176_transport_identities_verified"] is True and j["whole_E_ell_unit_certified"] is True
        assert j["J_unit_not_claimed"] is True and j["J_inverse_computed"] is False
        assert plain(j["source_quotient_derivative"])==plain(self.inputs["target_quotient_derivative"])
        assert plain(j["source_target_g_h"])==plain(self.inputs["target_g_h"])
        assert plain(j["selected_whole_E_unit_trial"])==plain(self.inputs["target_frame_unit"])
        assert u["whole_E_unit"] is True and u["t"]==j["selected_t"]
        assert u["unit_certificate"]["whole_fibre_unit"] is True
        assert u["unit_certificate"]["complete2176_scalar_product_equals_one"] is True
        assert plain(u["source_target_g_h"])==plain(self.inputs["target_g_h"])
        assert q["complete_2176_coordinate_quotient_identity_verified"] is True
        assert q["original_V_definition"]=="K(U)/P_U(U)"
        assert q["quotient_identity_left"]==q["quotient_identity_right"]
        for key in ("J_over_E","J_g_target_over_E","J_h_target_over_E"):shape(j[key],8,272)
        for key in ("Delta_K_at_U","H_K_at_U","dotV_over_E"):shape(q[key],8,272)
        assert j["J_h_target_over_E"]==q["dotV_over_E"]
        assert self.exact_transport_DAG["canonical_dual7_transports_both_determinant_frames"] is True
        assert self.exact_transport_DAG["scalar7_diamond_original_minus3_descent_and_kappa_nu_retained"] is True
        oldjob=self.sources["R928"].raw("public-actions-input.json")["job"]
        for group in ("R885","R919"):
            same_source(self.sources["R928"].tag["sources"][group],identity(self.item["sources"][group]))
            for name,row in self.item["sources"][group]["files"].items():
                assert oldjob["sources"][group]["files"][name]==row
        for key in ("source_functions","correspondence_algebra","fibre_certificate","target_normal_index",
                    "full_target_equations","target_normal_blocks","Euler_trace_row","full_eight_basis_identity"):
            assert self.inputs[key]==oldjob["inputs"][key]
        s=self.source_functions;c=self.correspondence_algebra
        assert s["prime"]==P and s["source_node_ordinal"]==0 and s["source_node_value"]==0
        assert s["original82_scales_retained_once"] is True and s["new_scale_applied"]=="1"
        assert s["complete_fibre_factors_or_multiplicities_removed"] is False
        assert c["base_algebra_dimension"]==272 and c["correspondence_rank"]==8 and c["full_scalar_dimension"]==2176
        assert c["full_Pprime_times_target_w_equals_K_verified"] is True
        assert c["Pprime_unit_certificate"]["whole_fibre_unit"] is True
        assert c["leading_coefficient_unit_certificate"]["whole_fibre_unit"] is True
        assert plain(q["source_original_P_K_PU_inverse_V"])==plain(self.inputs["correspondence_algebra"])
        f=self.fibre_certificate
        assert f["whole_fibre_success"] is True and f["all272_original_target_normal_coordinates_certified"] is True
        for field,key in (("source_functions","source_functions"),("correspondence_algebra","correspondence_algebra"),
                          ("target_normal_row","target_normal_index"),("full_target_equations","full_target_equations")):
            assert plain(f[field])==plain(self.inputs[key])
        idx=self.target_normal_index
        assert idx["all272_target_normal_coordinates_computed"] is True and idx["target_gamma0_equals_one"] is True
        assert len(idx["blocks"])==len(self.inputs["target_normal_blocks"])==17
        for ordinal,(part,ref) in enumerate(zip(idx["blocks"],self.inputs["target_normal_blocks"])):
            assert part["normal_columns"]==[ordinal*16,(ordinal+1)*16]
            assert plain(part["source"])==plain(ref)
        assert self.full_target_equations["all272_original_target_equations_verified"] is True
        assert self.full_target_equations["all2176_scalar_coordinates_of_each_equation_checked"] is True
        row=self.Euler_trace_row;all8=self.full_eight_basis_identity
        assert row["input_frame"]=="dz_target" and row["output_frame"]=="nu_source"
        assert row["complete_rank8_and_all272_source_coordinates_preserved"] is True
        assert plain(row["source_original_correspondence"])==plain(self.inputs["correspondence_algebra"])
        assert plain(all8["source_Euler_row"])==plain(self.inputs["Euler_trace_row"])
        assert all8["all8_basis_identities_in_entire_A0_verified"] is True
        shape(row["linear_functional_coefficients_over_A"],8,272)

    def budget(self):
        if time.monotonic()-self.started>=60*self.args.budget_minutes:
            raise BudgetStop("R930 budget; every completed contraction, Horner block and unit witness is retained.")

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

    def checkpoint(self,phase,label=None):
        save(self.path("current"),{"result":RESULT,"complete":False,"configuration":self.tag,
             "phase":phase,"label":label,"completed_stages":self.refs,
             "complete_target_connections":self.done,"retained_nonunit_denominators":self.failed})
        self.current=spec(self.path("current"))

    def source_audit(self):
        if self.old("source-audit") is None:
            self.put("source-audit",{
                "sources":{g:identity(self.item["sources"][g]) for g in GROUPS},"inputs":self.inputs,
                "prime":P,"source_node":0,"source_algebra_dimension":272,"correspondence_scalar_dimension":2176,
                "original_normal_basis_degrees":EPS,"original_82_scales_and_same_auxiliary_place_preserved":True,
                "seven_original_R905_gauges_and_complete_principal_parts_preserved":True,
                "old_R_G_numerators_denominators_J_deltaK_deltaP_Gamma_or_inverses_recomputed":False,
                "five_Picard_connections_or_Galois_averages_claimed_complete":False})
        self.checkpoint("sources")
    def evaluate_scalar_polynomial_U(self,coefficients):
        value=self.E.zero
        for i,c in enumerate(reversed(coefficients)):
            if i%32==0:self.budget()
            value=self.E.add(self.E.mul_U(value),self.E.scalar(c))
        return value

    def ordinary_trace_row(self):
        name="complete-ordinary-trace-row";value=self.old(name);A=self.A;E=self.E
        if value is None:
            self.budget();shift=self.D;basis=E.one;answers=[];checks=[]
            for i in range(8):
                self.budget();predicted=A.mul(self.a8inv,shift[7])
                col=basis;diag=[]
                for k in range(8):
                    diag.append(col[k])
                    if k<7:col=E.mul_U(col)
                actual=A.zero
                for x in diag:actual=A.add(actual,x)
                assert actual==predicted
                answers.append(A.pack(actual));checks.append({
                    "basis_power":i,"multiplication_diagonal_over_A":[A.pack(x) for x in diag],
                    "actual_trace_over_A":A.pack(actual),"Euler_coefficient_over_A":A.pack(predicted),
                    "all272_source_coordinates_verified":True})
                if i<7:shift=E.mul_U(shift);basis=E.mul_U(basis)
            value=self.put(name,{
                "source_original_a8_PU_and_monic_relation":self.inputs["correspondence_algebra"],
                "basis_powers":list(range(8)),"linear_functional_coefficients_over_A":answers,
                "basis_checks":checks,"coefficient_formula":"a8^-1*[U^7](h*P_U mod monic_P)",
                "all8_full_multiplication_trace_identities_verified":True,
                "whole_rank8_and_all272_source_factors_retained":True,
                "old_a8_or_PU_inverse_recomputed":False})
        assert value["source_original_a8_PU_and_monic_relation"]==self.inputs["correspondence_algebra"]
        self.trace_row=[A.unpack(v) for v in value["linear_functional_coefficients_over_A"]]
        self.checkpoint(name)

    def trace_transport_factors(self):
        name="completed-trace-transport-factors";value=self.old(name);E=self.E
        if value is None:
            self.budget()
            a=E.mul(self.frame_inverse,E.add(E.one,E.scale(E.mul(self.Dinv,self.H),self.frame_t)))
            b=E.mul(self.frame_inverse,E.mul(self.Dinv,self.Delta))
            value=self.put(name,{
                "source_completed_R928_transport":self.inputs["target_transport"],
                "source_completed_R928_quotient_data":self.inputs["target_quotient_derivative"],
                "source_completed_frame_inverse":self.inputs["target_frame_unit"],
                "source_original_PU_inverse":self.inputs["correspondence_algebra"],
                "selected_original_t":self.frame_t,
                "coefficient_for_old_L_over_E":E.pack(a),
                "coefficient_for_t_times_ordinary_trace_over_E":E.pack(b),
                "identity":"Tr(B*J)=L(B*ell^-1*(1+t*D^-1*H_K))+t*T(B*ell^-1*D^-1*Delta_K)",
                "old_J_deltaK_deltaP_PU_inverse_or_frame_inverse_recomputed":False})
        self.Lfactor=E.unpack(value["coefficient_for_old_L_over_E"])
        self.Tfactor=E.unpack(value["coefficient_for_t_times_ordinary_trace_over_E"])
        self.checkpoint(name)

    def denominator(self,label):
        name=label+"-whole-target-denominator-unit";value=self.old(name);E=self.E
        if value is None:
            self.budget();ref=self.inputs["divisors"][label]["denominator"]
            raw=self.divisors[label]["denominator"]["denominator_coefficients_in_z_low_to_high"]
            target=self.evaluate_scalar_polynomial_U(raw)
            try:
                inverse,proof=E.inverse(target,"original_"+label+"_whole_target_d")
                good=True
            except UnitFailure as exc:
                good=False;proof=exc.witness
            value=self.put(name,{
                "prime":P,"label":label,"source_completed_original_denominator":ref,
                "source_original_correspondence":self.inputs["correspondence_algebra"],
                "d_target_over_E":E.pack(target),"whole_E_unit":good,"unit_certificate":proof,
                "full_original_rank8_over_272_source_dimension":True,
                "factor_removal_or_cancellation_claimed":False,
                "source_F0_unit_not_used_as_target_unit":True})
        assert value["source_completed_original_denominator"]==self.inputs["divisors"][label]["denominator"]
        if not value["whole_E_unit"]:self.failed[label]=self.refs[name]
        self.checkpoint("target-denominator-unit",label)
        return value

    def numerator_contractions(self,label):
        source=self.inputs["divisors"][label];y=self.divisors[label]["numerator"]["numerator_coefficients_in_z_low_to_high"]
        parts=[]
        for first in range(0,277,BLOCK):
            stop=min(first+BLOCK,277);name=label+f"-normal-target-contraction-{first:03d}-{stop:03d}"
            value=self.old(name)
            if value is None:
                self.budget();product=nmod_mat(stop-first,N,P)
                for m in range(4):
                    shifted=matrix([y[k-m] if 0<=k-m<274 else [0]*N for k in range(first,stop)])
                    product+=shifted*self.R[m]
                raw=rows(product)
                for k,row in enumerate(raw,first):
                    for j,c in enumerate(row):
                        if k>274-EPS[j]:assert c==0,(label,"normal_numerator_degree",k,j)
                target=product*self.target_matrix
                values=[[[int(target[i,272*j+r]) for r in range(272)] for j in range(8)]
                        for i in range(stop-first)]
                value=self.put(name,{
                    "prime":P,"label":label,"first":first,"stop":stop,
                    "source_original_bounded_numerator":source["numerator"],
                    "source_completed_low_weight_R":self.inputs["R_low_weight_polynomial"],
                    "source_completed_all272_target_coordinates":self.inputs["target_normal_index"],
                    "normal_numerator_coefficients_mod_prime":raw,
                    "target_normal_contracted_coefficients_over_E":values,
                    "normal_numerator_degree_bounds":[274-e for e in EPS],
                    "all_original_weighted_product_degree_bounds_verified":True,
                    "actual_z_coefficients_before_target_U_Horner":True,
                    "old_R_y_or_target_normal_coordinates_recomputed":False})
            assert value["source_original_bounded_numerator"]==source["numerator"]
            assert value["source_completed_low_weight_R"]==self.inputs["R_low_weight_polynomial"]
            parts.append({"first":first,"stop":stop,"source":self.refs[name]});self.checkpoint("target-numerator-contraction",label)
        name=label+"-target-numerator-contraction-index";value=self.old(name)
        if value is None:
            self.put(name,{"prime":P,"label":label,"blocks":parts,"complete_coefficient_range":[0,277],
                "source_original_bounded_numerator":source["numerator"],
                "source_completed_low_weight_R":self.inputs["R_low_weight_polynomial"],
                "source_completed_all272_target_coordinates":self.inputs["target_normal_index"],
                "all277_times272_product_coordinates_and_weights_verified":True,
                "zero_tail_degrees275_and276_certified":True})
        else:assert value["blocks"]==parts
        self.checkpoint("target-numerator-index",label)
        return parts

    def numerator_Horner(self,label,parts):
        E=self.E;previous=None;current=E.zero
        for part in reversed(parts):
            first,stop=part["first"],part["stop"];name=label+f"-U-Horner-{first:03d}-{stop:03d}"
            value=self.old(name)
            if value is None:
                self.budget();data=read(self.out/part["source"]["file"])
                assert spec(self.out/part["source"]["file"])==part["source"]
                assert data["configuration"]==self.tag
                if previous is not None:
                    previous_data=read(self.out/previous["file"])
                    assert spec(self.out/previous["file"])==previous and previous_data["configuration"]==self.tag
                    current=E.unpack(previous_data["accumulator_over_E"])
                for raw in reversed(data["target_normal_contracted_coefficients_over_E"]):
                    current=E.add(E.mul_U(current),E.unpack(raw))
                value=self.put(name,{
                    "prime":P,"label":label,"first":first,"stop":stop,
                    "source_coefficient_block":part["source"],"previous_higher_degree_block":previous,
                    "accumulator_over_E":E.pack(current),
                    "complete_rank8_U_Horner_without_point_specialization":True})
            assert value["previous_higher_degree_block"]==previous
            assert value["source_coefficient_block"]==part["source"]
            previous=self.refs[name];current=E.unpack(value["accumulator_over_E"])
            self.checkpoint("target-U-Horner",label)
        assert parts[0]["first"]==0
        return current,previous

    def apply_row(self,row,value):
        answer=self.A.zero
        for a,b in zip(row,value):answer=self.A.add(answer,self.A.mul(a,b))
        return answer

    def connection_trace(self,label,numerator,horner,denominator):
        E=self.E;A=self.A
        name=label+"-complete-whole-target-connection-and-trace";value=self.old(name)
        if value is None:
            self.budget()
            d=E.unpack(denominator["d_target_over_E"])
            inv=E.unpack(denominator["unit_certificate"]["inverse"])
            B=E.mul(numerator,inv)
            back=E.mul(d,B);assert back==numerator
            integrand=E.mul(B,self.J)
            col=integrand;diagonal=[]
            for k in range(8):
                diagonal.append(col[k])
                if k<7:col=E.mul_U(col)
            direct=A.zero
            for row in diagonal:direct=A.add(direct,row)
            trace=self.apply_row(self.trace_row,integrand)
            assert trace==direct
            first=E.mul(B,self.Lfactor);second=E.mul(B,self.Tfactor)
            Lvalue=self.apply_row(self.oldL,first);Tvalue=self.apply_row(self.trace_row,second)
            alternative=A.add(Lvalue,A.scale(Tvalue,self.frame_t))
            assert alternative==trace
            refs=self.inputs["divisors"][label]
            value=self.put(name,{
                "prime":P,"label":label,"source_original_bounded_connection":refs["certificate"],
                "source_original_bounded_numerator":refs["numerator"],"source_original_denominator":refs["denominator"],
                "source_complete_numerator_contraction_index":self.refs[label+"-target-numerator-contraction-index"],
                "source_complete_target_U_Horner":horner,
                "source_complete_whole_target_denominator_unit":self.refs[label+"-whole-target-denominator-unit"],
                "source_completed_original_J":self.inputs["target_transport"],
                "source_completed_old_L":self.inputs["Euler_trace_row"],
                "source_new_full_ordinary_trace_row":self.refs["complete-ordinary-trace-row"],
                "source_trace_transport_factors":self.refs["completed-trace-transport-factors"],
                "numerator_target_over_E":E.pack(numerator),"B_D_target_over_E":E.pack(B),
                "denominator_times_B_D_over_E":E.pack(back),"B_D_times_J_over_E":E.pack(integrand),
                "full_multiplication_diagonal_over_A":[A.pack(x) for x in diagonal],
                "actual_complete_differential_trace_over_A":A.pack(trace),
                "actual_direct_rank8_multiplication_trace_over_A":A.pack(direct),
                "input_to_original_L_over_E":E.pack(first),"input_to_new_T_over_E":E.pack(second),
                "original_L_term_over_A":A.pack(Lvalue),"ordinary_T_term_before_multiply_t_over_A":A.pack(Tvalue),
                "actual_R922_quotient_transport_trace_over_A":A.pack(alternative),
                "selected_original_frame_t":self.frame_t,
                "all2176_target_connection_quotient_coordinates_verified":True,
                "all272_trace_coordinates_verified_by_full_rank8_multiplication":True,
                "all272_R922_quotient_transport_trace_coordinates_verified":True,
                "direct_correspondence_direction":"Tr_pi_s(pi_t^*alpha_D)",
                "source_output_differential_frame":"nu_source",
                "original_target_rational_connection_section":"1 of O(H-D)",
                "original_target_principal_parts":"H-D",
                "original_R905_gauge_and_normalization_preserved":True,
                "whole_source_and_target_factors_multiplicities_retained":True,
                "canonical_dual7_frames_scalar7_diamond_and_minus3_transport_retained":True,
                "endpoint_kappa_nu_numerical_calibration_computed":False,
                "five_Picard_sigma_cY_combinations_computed":False,
                "characteristic_zero_connection_or_trace_coordinates_expanded":False,
                "nonp_terms_Poincare_period_or_height_computed":False})
        assert value["source_original_bounded_connection"]==self.inputs["divisors"][label]["certificate"]
        assert value["all2176_target_connection_quotient_coordinates_verified"] is True
        self.done[label]=self.refs[name]
        self.checkpoint("connection-complete",label)

    def direction(self,label):
        name=label+"-complete-whole-target-connection-and-trace";value=self.old(name)
        if value is not None:
            assert value["source_original_bounded_connection"]==self.inputs["divisors"][label]["certificate"]
            self.done[label]=self.refs[name];return
        den=self.denominator(label)
        if not den["whole_E_unit"]:return
        parts=self.numerator_contractions(label)
        numerator,horner=self.numerator_Horner(label,parts)
        self.connection_trace(label,numerator,horner,den)

    def exact_expression(self):
        name="seven-original-exact-target-connection-trace-DAG";value=self.old(name)
        if value is not None:return
        self.put(name,{
            "source_R922_proof":self.item["proofs"]["R922"],
            "source_exact_original_R":self.inputs["R_exact_expression"],
            "source_exact_original_target_transport":self.inputs["exact_transport_DAG"],
            "original_rigidified_Hecke_transport":self.exact_transport_DAG["original_rigidified_Hecke_transport"],
            "original_cY_definition_retained_but_not_applied":self.exact_transport_DAG["original_cY"],
            "connections":{label:{
                "source_completed_original_bounded_connection":self.inputs["divisors"][label]["certificate"],
                "source_original_full_principal_parts_connection":
                    self.divisors[label]["certificate"]["source_original_connection"],
                "same_original_unit_solve_expression":
                    self.divisors[label]["certificate"]["exact_characteristic_zero_expression"],
                "target_B":{"operation":"evaluate_rational_original_function_on_full_target_U_V",
                    "formula":"sum_ij y_i(U)*R_ij(U)*beta_j(U,V)/d(U)",
                    "required_unit":"whole d(U)"},
                "differential_trace":{"operation":"full_original_correspondence_trace",
                    "formula":"Tr_E/A0(B_D*J)*nu_source","target_frame":"nu_target",
                    "direct_direction":"Tr_pi_s(pi_t^*alpha_D)"},
                "canonical_dual7_transports_both_frames_to_frozen_Hecke_direction":True}
                for label in LABELS},
            "exact_original_characteristic_zero_expressions_defined":True,
            "all_original_section1_gauges_and_principal_parts_H_minus_D_preserved":True,
            "scalar7_diamond_original_minus3_descent_and_kappa_nu_retained":True,
            "finite_fibre_values_substituted_for_global_functions":False,
            "characteristic_zero_coordinates_expanded":False,
            "five_Picard_sigma_cY_or_principal_function_combinations_computed":False,
            "Hecke_calibration_nonp_terms_periods_or_height_computed":False})
        self.checkpoint(name)

    def manifest(self):
        entries=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name==PREFIX+"current.json.gz" or path.name.startswith(PREFIX+"stage-manifest-"):continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
            entries.append(spec(path))
        current=spec(self.path("current")) if self.path("current").exists() else None
        value={"result":RESULT,"complete":True,"configuration":self.tag,
               "files":entries,"current_checkpoints":[] if current is None else [current]}
        target=self.path("stage-manifest-"+fingerprint(value))
        if target.exists():assert read(target)==value
        else:save(target,value)
        return spec(target)

    def finish(self,complete,reason):
        value={"result":RESULT,"configuration":self.tag,"complete":bool(complete),"p":41,
            "prime":P,"source_node":0,"source_algebra_dimension":272,"correspondence_rank":8,
            "correspondence_scalar_dimension":2176,"source_divisor_order":list(LABELS),
            "source_audit":self.refs.get("source-audit"),
            "complete_ordinary_trace_row":self.refs.get("complete-ordinary-trace-row"),
            "complete_trace_transport_factors":self.refs.get("completed-trace-transport-factors"),
            "exact_original_target_connection_trace_DAG":self.refs.get("seven-original-exact-target-connection-trace-DAG"),
            "complete_original_target_connection_certificates":dict(self.done),
            "nonunit_target_denominators":dict(self.failed),"actual_completed_connections":len(self.done),
            "actual_all_seven_whole_target_connection_values_and_differential_traces_certified":len(self.done)==7,
            "all_original_factors_nilpotents_multiplicities_and_section_gauges_retained":True,
            "old_R_G_y_d_J_deltaK_deltaP_Gamma_or_inverses_recomputed":False,
            "J_inverse_computed_or_J_unit_claimed":False,
            "actual_characteristic_zero_connection_coordinates_expanded":False,
            "five_Picard_sigma_cY_or_principal_function_combinations_computed":False,
            "original_Hecke_projector_or_endpoint_calibration_computed":False,
            "nonp_terms_Poincare_period_or_height_computed":False,
            "stage_manifest":self.manifest(),"resume_state":self.current,
            "scope_stop_reason":reason,"seconds":time.monotonic()-self.started}
        if complete:assert len(self.done)==7 and not self.failed
        save(self.out/FINAL,value);return value

    def run(self):
        self.exact_expression();self.ordinary_trace_row();self.trace_transport_factors()
        for ordinal,label in enumerate(LABELS):
            if ordinal>=self.limit:return self.finish(False,"requested_divisor_prefix_complete")
            self.budget();self.direction(label)
        good=len(self.done)==7
        return self.finish(good,None if good else "one_or_more_entire_target_denominators_are_nonunits")

def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise SystemExit("R930 new arithmetic runs only in the authorized public repository Actions.")
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
    if (code in (1,124) or (code==2 and error is not None)) and job is not None:job.finish(False,error)
    receipt={"result":RESULT,"source_sha256":sha(__file__),"helper_sha256":sha(algebra.__file__),
        "complete":code==0,"process_exit_code":code,"error":error,"seconds":time.monotonic()-started,
        "configuration":None if job is None else job.tag,
        "certificate_sha256":sha(out/FINAL) if (out/FINAL).exists() else None,
        "new_arithmetic_only_in_public_Actions":True}
    save(out/"core-receipt.json",receipt)
    log={k:v for k,v in receipt.items() if k!="configuration"}
    log["configuration_sha256"]=None if job is None else fingerprint(job.tag)
    print("R930_CORE_RECEIPT="+json.dumps(log,sort_keys=True),flush=True)
    raise SystemExit(code)
if __name__=="__main__":main()
