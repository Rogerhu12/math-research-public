#!/usr/bin/env python3
"""R926: seven bounded polynomial connection numerators, reusing the completed R905 charts."""
import argparse
import gzip
import hashlib
import json
from math import comb
import os
from pathlib import Path, PurePosixPath
import re
import sys
import time
import traceback
import flint
from flint import nmod_mat

REPOSITORY="Rogerhu12/math-research-public"
RESULT="R926-original-seven-bounded-connection-polynomial-numerators"
FINAL="p41-original-seven-bounded-connection-polynomial-numerators-certificate.json"
PREFIX="R926-"
MANIFEST="full-outputs-manifest.json"
P=1000000753
N=272
EPS=[0]+[1]*144+[2]*127
LABELS=("D1","D2","D3","D4","D5","X","DN")
GROUPS=("R905",)
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
BLOCK=16
STRATEGY={
    "original_curve":"original genus127 Y, level82, original minus3 descent",
    "prime":P,"normal_basis_rank":N,"normal_basis_degrees":EPS,
    "divisor_order":list(LABELS),
    "original_differential_basis":"(z-a)^k times trace dual of original F column times dz",
    "original_F_column_section_weights":[2]*146+[3]*126,
    "original_543_selection_and_all670_solution_coefficients_preserved":True,
    "whole_D_multiplier":"Z=Q_D*L_a*T_tau*E_D on the full canonical quotient, dimension272",
    "denominator":"d(a+t)=det(I-tZ)=det(F(a+t))/det(F(a))",
    "norm_algorithm":"new characteristic polynomial of the actual full Z matrix, reverse all273 coefficients",
    "Taylor_recurrence":"x_r=F0^-t*(c_r-sum_(m=1)^min(3,r) F_m^t*x_(r-m))",
    "Taylor_vector_count":274,"Taylor_atomic_block_size":BLOCK,
    "numerator":"y=(d*x) modulo t^274, with exact global degree bound271+epsilon_i",
    "full_acceptance":"all272 rows of F^t*y=d*c at all277 polynomial coefficients",
    "basis_coordinate":"t=z-a explicitly retained; also emit actual z coefficients",
    "old_F_inverse_543_system_original_D_primitive_or_old_characteristic_relation_recomputed":False,
    "source_factors_ramification_nilpotents_or_D_H_intersections_discarded":False,
    "actual_output_only_original_p753_reduction":True,
    "shared_R_target_units_Hecke_calibration_or_height_computed":False,
    "budget_and_requested_divisor_count_excluded_from_identity":True}
class BudgetStop(RuntimeError):pass

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
    return {"result":RESULT,"source_sha256":item["core_sha256"],
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



def positions(weight):
    return [(i,k) for i,e in enumerate(EPS) for k in range(max(0,weight-e+1))]

def zero(m,n=1):
    return nmod_mat(m,n,P)

def hasse_matrices(coefficients,a):
    result=[]
    for r in range(len(coefficients)):
        value=zero(N,N)
        for k in range(r,len(coefficients)):
            value+=coefficients[k]*(comb(k,r)*pow(a,k-r,P)%P)
        result.append(value)
    return result

def t_to_z_rows(coefficients,a):
    count=len(coefficients);width=len(coefficients[0])
    if a==0:return [list(row) for row in coefficients]
    transport=matrix([[comb(k,r)*pow(-a,k-r,P)%P if r<=k else 0
                       for k in range(count)] for r in range(count)])
    return rows(transport*matrix(coefficients))

class Job:
    def __init__(self,args):
        self.args=args;self.started=time.monotonic();self.out=Path(args.output)
        self.out.mkdir(parents=True,exist_ok=True);self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41
        assert self.item["producer_inputs_pending"] is False
        assert sha(__file__)==self.item["core_sha256"] and flint.__version__=="0.9.0"
        topic=Path(__file__).resolve().parent.parent
        assert sha(topic/self.item["method"])==self.item["method_sha256"]
        for row in self.item["proofs"].values():assert sha(topic/row["path"])==row["sha256"]
        assert set(self.item["sources"])==set(GROUPS)
        self.sources={g:Source(g,self.item["sources"][g],args.retained) for g in GROUPS}
        self.tag=expected_tag(self.item);self.refs={};self.current=None;self.done={}
        self.inputs=self.item["inputs"];assert set(self.inputs["divisors"])==set(LABELS)
        self.source=self.sources["R905"]
        cert=self.source.certificate
        assert cert["complete"] is True and cert["prime"]==P
        assert cert["source_divisor_order"]==list(LABELS)
        assert cert["actual_seven_complete_full_principal_parts_solutions"] is True
        assert cert["actual_completed_source_connections"]==7
        for label in LABELS:
            assert plain(cert["complete_source_connection_certificates"][label])==plain(self.inputs["divisors"][label]["connection"])
        self.max_divisors=int(self.item.get("maximum_divisors",7))
        assert 1<=self.max_divisors<=7
        self.V2,self.V3=positions(2),positions(3)
        assert len(self.V2)==418 and len(self.V3)==690
        self.lookup3={p:i for i,p in enumerate(self.V3)}
        self.source_audit()

    def budget(self):
        if time.monotonic()-self.started>=60*self.args.budget_minutes:
            raise BudgetStop("R926 budget: completed norm, Taylor and full-product blocks remain immutable.")

    def input(self,row):
        return self.sources[row["source_group"]].stage(row)

    def path(self,name):
        assert Path(name).name==name
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

    def checkpoint(self,phase,label=None,next_Taylor=None):
        save(self.path("current"),{"result":RESULT,"complete":False,"configuration":self.tag,
            "phase":phase,"active_divisor":label,"next_Taylor_index":next_Taylor,
            "completed_stages":self.refs,"completed_divisors":self.done})
        self.current=spec(self.path("current"))

    def source_audit(self):
        if self.old("source-audit") is None:
            self.put("source-audit",{
                "sources":{"R905":identity(self.item["sources"]["R905"])},"inputs":self.inputs,
                "source_divisor_order":list(LABELS),"prime":P,
                "all_original_seven_connections_already_certified":True,
                "all_original_543_choices_and_frames_preserved":True,
                "old_543_system_670_basis_F_inverse_and_whole_D_primitive_not_recomputed":True,
                "original_82_scale_minus3_descent_and_dz_frame_unchanged":True})
        self.checkpoint("source-bound")

    def data(self,label):
        source=self.inputs["divisors"][label]
        graph=self.input(source["bundle"]);model=self.input(source["quotient"])
        solution=self.input(source["solution"]);connection=self.input(source["connection"])
        for value in (graph,model,solution,connection):
            assert value["prime"]==P and value["label"]==label
        assert graph["both_F_inverse_products_verified"] is True
        assert graph["full_rank272_equal_degree146_bundle_isomorphism_certified"] is True
        assert graph["h0_H_minus_D_zero_follows_from_actual_unit_graph"] is True
        assert graph["column_weights"]==[1]*146+[0]*126
        assert graph["trace_dual_differential_space_dimension"]==670
        assert graph["actual_F_determinant_mod_prime"]!=0
        assert len(graph["F_coefficients_low_to_high"])==4
        for x in graph["F_coefficients_low_to_high"]:shape(x,N,N)
        shape(graph["F_at_auxiliary_fibre_mod_prime"],N,N)
        shape(graph["inverse_F_at_auxiliary_fibre_mod_prime"],N,N)
        a=graph["auxiliary_z"];assert isinstance(a,int) and 0<=a<P
        assert model["auxiliary_z"]==a and model["whole_D_algebra_dimension"]==272
        assert model["whole_D_plus_H_dimension"]==544
        assert model["all690_original_polynomial_division_identities_verified"] is True
        assert model["all146_U_relations_and272_canonical_quotient_rows_verified"] is True
        assert model["D_H_intersections_not_assumed_empty"] is True
        assert plain(model["source_complete_bundle_unit_graph"])==plain(source["bundle"])
        assert plain(model["source_F0_inverse_reused_without_recomputation"])==plain(source["bundle"])
        shape(model["V2_D_quotient_projection_mod_prime"],N,418)
        shape(model["V3_to_V2_h_division_mod_prime"],418,690)
        shape(model["whole_D_algebra_unit_mod_prime"],N,1)
        free=model["V2_D_quotient_free_rows"]
        assert len(free)==N and free==sorted(set(free)) and all(0<=i<418 for i in free)
        assert solution["actual_rank"]==solution["required_full_principal_parts_rank"]==543
        assert solution["rank_is_required"] is True and solution["all_original_rows_multiplied_back"] is True
        assert solution["free_coefficients_set_to_zero"] is True
        assert len(solution["solution_coefficients_mod_prime"])==670
        assert len(solution["selected_rows"])==len(solution["selected_columns"])==543
        assert connection["actual_principal_parts_rank"]==543
        for flag in ("all544_principal_part_equations_multiplied_back",
                     "exact_regular_connection_on_original_O_H_minus_D_as_expression_certified",
                     "exact_full_principal_parts_not_only_residues_certified",
                     "all_ramification_nilpotents_and_D_H_intersections_preserved"):
            assert connection[flag] is True
        assert plain(connection["source_complete_bundle_unit_graph"])==plain(source["bundle"])
        assert plain(connection["source_complete_quotient_models"])==plain(source["quotient"])
        assert plain(connection["source_full543_unit_solution"])==plain(source["solution"])
        assert plain(solution["source_full_principal_parts_matrix"])==plain(connection["source_full_principal_parts_matrix"])
        assert plain(solution["source_full_target"])==plain(connection["source_full_target"])
        dag=connection["exact_connection_DAG"]
        assert dag["original_rational_section"]=="1 of O(H-D)"
        assert dag["full_logarithmic_principal_parts"]=="H-D"
        assert dag["basis"]["auxiliary_z"]==a and dag["basis"]["coefficient_power"]=="(z-a)^k"
        assert dag["basis"]["differential"]=="the original dz"
        assert dag["coefficients"]["rows"]==solution["selected_rows"]
        assert dag["coefficients"]["columns"]==solution["selected_columns"]
        labels=[[i,k] for i in range(N) for k in range(2 if i<146 else 3)]
        assert dag["basis"]["indices"]==labels
        F=[matrix(x) for x in graph["F_coefficients_low_to_high"]]
        weights=[2]*146+[3]*126
        for degree,raw in enumerate(graph["F_coefficients_low_to_high"]):
            for i,row in enumerate(raw):
                for j,value in enumerate(row):
                    if degree>weights[j]-EPS[i]:assert value==0
        FF=F if a==0 else hasse_matrices(F,a)
        assert FF[0]==matrix(graph["F_at_auxiliary_fibre_mod_prime"])
        inverse0=matrix(graph["inverse_F_at_auxiliary_fibre_mod_prime"])
        return source,graph,model,solution,connection,labels,FF,inverse0,a

    def coefficient_vector(self,label,source,solution,labels,a):
        name=label+"-original-c-polynomial";old=self.old(name)
        if old is None:
            self.budget();raw=[[0]*N for _ in range(3)]
            for (i,k),value in zip(labels,solution["solution_coefficients_mod_prime"]):
                assert isinstance(value,int) and 0<=value<P
                raw[k][i]=value
            old=self.put(name,{
                "prime":P,"label":label,"auxiliary_z":a,
                "source_original_connection":source["connection"],
                "source_original_full543_solution":source["solution"],
                "source_original_differential_basis_indices":labels,
                "coefficient_vectors_in_t_low_to_high":raw,
                "original_selected_rows":solution["selected_rows"],
                "original_selected_columns":solution["selected_columns"],
                "all670_original_solution_coefficients_used_exactly_once":True,
                "new_543_solve_or_new_gauge_performed":False,
                "differential_frame":"original dz","coordinate":"t=z-a"})
        assert old["source_original_connection"]==source["connection"]
        assert old["source_original_full543_solution"]==source["solution"]
        shape(old["coefficient_vectors_in_t_low_to_high"],3,N)
        return old["coefficient_vectors_in_t_low_to_high"]

    def norm(self,label,source,model,a):
        multname=label+"-whole-D-tau-over-h-multiplier"
        value=self.old(multname)
        if value is None:
            self.budget()
            Q=matrix(model["V2_D_quotient_projection_mod_prime"])
            rawL=model["V3_to_V2_h_division_mod_prime"]
            selected=[self.lookup3[self.V2[i]] for i in model["V2_D_quotient_free_rows"]]
            LtauE=matrix([[row[j] for j in selected] for row in rawL])
            Z=Q*LtauE
            # tau*h_a / h_a^2 is the same whole-D element tau/h_a.
            tauh=[[0] for _ in self.V2]
            lookup2={p:i for i,p in enumerate(self.V2)}
            tauh[lookup2[(0,0)]][0]=(-a)%P
            tauh[lookup2[(0,1)]][0]=1
            element=Q*matrix(tauh)
            oldunit=matrix(model["whole_D_algebra_unit_mod_prime"])
            assert Z*oldunit==element
            value=self.put(multname,{
                "prime":P,"label":label,"auxiliary_z":a,
                "source_complete_quotient_model":source["quotient"],
                "canonical_quotient_free_rows":model["V2_D_quotient_free_rows"],
                "original_tau_V2_to_V3_columns":selected,
                "whole_multiplication_matrix_mod_prime":rows(Z),
                "whole_D_algebra_dimension":N,
                "tau_over_h_canonical_coordinates_mod_prime":rows(element),
                "multiplication_times_original_unit_equals_tau_over_h_verified":True,
                "exact_operator":"Q_D*L_a*T_tau*canonical_free_row_lift",
                "all_nilpotents_and_D_H_intersections_retained":True,
                "old_D_primitive_or_old_charpoly_recomputed":False})
        assert value["source_complete_quotient_model"]==source["quotient"]
        name=label+"-complete-denominator-norm";old=self.old(name)
        if old is None:
            self.budget()
            Z=matrix(value["whole_multiplication_matrix_mod_prime"])
            characteristic=Z.charpoly()
            assert characteristic.degree()==N and int(characteristic[N])==1
            ascending=[int(characteristic[k]) for k in range(N+1)]
            d=list(reversed(ascending));assert d[0]==1
            dz=[row[0] for row in t_to_z_rows([[x] for x in d],a)]
            actual_degree=max(k for k,x in enumerate(d) if x)
            old=self.put(name,{
                "prime":P,"label":label,"auxiliary_z":a,
                "source_whole_D_multiplier":self.refs[multname],
                "source_complete_bundle_F":source["bundle"],
                "characteristic_coefficients_ascending_T":ascending,
                "denominator_coefficients_in_t_low_to_high":d,
                "denominator_coefficients_in_z_low_to_high":dz,
                "actual_denominator_degree":actual_degree,
                "whole_norm_degree_count_before_possible_degree_drop":N,
                "new_norm_algorithm":"FLINT nmod_mat.charpoly on the entire new tau/h multiplication matrix",
                "full_rank272_characteristic_polynomial_computed":True,
                "denominator_is_det_I_minus_tZ":True,
                "denominator_at_original_auxiliary_point_equals_one":True,
                "same_original_determinant_ratio_expression":"det(F(z))/det(F(a))",
                "normalization_and_all_multiplicities_preserved":True,
                "nilpotent_zero_eigenparts_not_removed":True,
                "original_543_inverse_or_primitive_charpoly_recomputed":False})
        assert old["source_whole_D_multiplier"]==self.refs[multname]
        assert old["source_complete_bundle_F"]==source["bundle"]
        assert len(old["denominator_coefficients_in_t_low_to_high"])==N+1
        return old

    def Taylor(self,label,source,FF,inverse0,c,a):
        FT=[x.transpose() for x in FF];inverseT=inverse0.transpose()
        C=[matrix([[x] for x in row]) for row in c]
        vectors=[];previous=None;blocks=[]
        for first in range(0,274,BLOCK):
            stop=min(first+BLOCK,274);name=label+f"-Taylor-{first:03d}-{stop:03d}"
            old=self.old(name)
            if old is None:
                self.budget();new=[]
                for r in range(first,stop):
                    rhs=C[r] if r<3 else zero(N)
                    for m in range(1,min(3,r)+1):
                        rhs-=FT[m]*matrix([[x] for x in vectors[r-m]])
                    answer=inverseT*rhs
                    raw=[int(answer[i,0]) for i in range(N)]
                    vectors.append(raw);new.append(raw)
                old=self.put(name,{
                    "prime":P,"label":label,"auxiliary_z":a,"first":first,"stop":stop,
                    "source_original_F_and_zero_order_inverse":source["bundle"],
                    "source_original_c":self.refs[label+"-original-c-polynomial"],
                    "previous_complete_Taylor_block":previous,
                    "vectors_low_to_high":new,"vector_dimension":N,
                    "recurrence_uses_original_inverse_transpose":True,
                    "old_zero_order_inverse_or_prior_complete_vectors_recomputed":False})
            else:
                assert old["first"]==first and old["stop"]==stop
                assert old["previous_complete_Taylor_block"]==previous
                assert old["source_original_F_and_zero_order_inverse"]==source["bundle"]
                assert old["source_original_c"]==self.refs[label+"-original-c-polynomial"]
                shape(old["vectors_low_to_high"],stop-first,N)
                vectors.extend(old["vectors_low_to_high"])
            assert len(vectors)==stop
            previous=self.refs[name];blocks.append(previous)
            self.checkpoint("Taylor",label,stop)
        assert len(vectors)==274
        return vectors,blocks

    def numerator(self,label,source,c,denominator,vectors,blocks,a):
        name=label+"-complete-bounded-polynomial-numerator";old=self.old(name)
        if old is None:
            self.budget()
            d=denominator["denominator_coefficients_in_t_low_to_high"]
            convolution=matrix([[d[r-k] if 0<=r-k<len(d) else 0 for k in range(274)]
                                for r in range(274)])
            y=rows(convolution*matrix(vectors))
            for degree,row in enumerate(y):
                for i,value in enumerate(row):
                    if degree>271+EPS[i]:assert value==0
            yz=t_to_z_rows(y,a)
            for degree,row in enumerate(yz):
                for i,value in enumerate(row):
                    if degree>271+EPS[i]:assert value==0
            old=self.put(name,{
                "prime":P,"label":label,"auxiliary_z":a,
                "source_original_connection":source["connection"],
                "source_original_c":self.refs[label+"-original-c-polynomial"],
                "source_denominator":self.refs[label+"-complete-denominator-norm"],
                "complete_Taylor_blocks":blocks,"actual_Taylor_vector_count":274,
                "numerator_coefficients_in_t_low_to_high":y,
                "numerator_coefficients_in_z_low_to_high":yz,
                "coordinate_dimensions":[274,N],"normal_basis_degrees":EPS,
                "numerator_degree_bounds":[271+e for e in EPS],
                "all_original_weighted_numerator_degree_bounds_verified":True,
                "true_t_equals_z_minus_original_auxiliary_point":True,
                "finite_numerator_candidate_before_global_identity":True,
                "characteristic_zero_numerator_coordinates_expanded":False})
        assert old["source_original_connection"]==source["connection"]
        assert old["source_denominator"]==self.refs[label+"-complete-denominator-norm"]
        assert old["complete_Taylor_blocks"]==blocks
        shape(old["numerator_coefficients_in_t_low_to_high"],274,N)
        shape(old["numerator_coefficients_in_z_low_to_high"],274,N)
        self.checkpoint("bounded-numerator",label,274)
        return old

    def verify_polynomial(self,label,source,FF,c,denominator,numerator):
        yc=numerator["numerator_coefficients_in_t_low_to_high"]
        d=denominator["denominator_coefficients_in_t_low_to_high"]
        FT=[x.transpose() for x in FF]
        C=matrix(c).transpose()
        refs=[]
        for first in range(0,277,BLOCK):
            stop=min(first+BLOCK,277);name=label+f"-full-product-{first:03d}-{stop:03d}"
            old=self.old(name)
            if old is None:
                self.budget();product=zero(N,stop-first)
                for m in range(4):
                    block=matrix([yc[r-m] if 0<=r-m<274 else [0]*N for r in range(first,stop)]).transpose()
                    product+=FT[m]*block
                scalar=matrix([[d[r-k] if 0<=r-k<len(d) else 0 for r in range(first,stop)] for k in range(3)])
                expected=C*scalar
                assert product==expected,(label,"full_polynomial_F_transpose_y",first,stop)
                old=self.put(name,{
                    "prime":P,"label":label,"first":first,"stop":stop,
                    "source_original_F":source["bundle"],
                    "source_original_c":self.refs[label+"-original-c-polynomial"],
                    "source_denominator":self.refs[label+"-complete-denominator-norm"],
                    "source_numerator":self.refs[label+"-complete-bounded-polynomial-numerator"],
                    "all272_rows_for_each_coefficient_checked":True,
                    "complete_polynomial_product_equals_d_times_c":True,
                    "left_product_sha256":fingerprint(rows(product)),
                    "right_product_sha256":fingerprint(rows(expected))})
            assert old["first"]==first and old["stop"]==stop
            assert old["source_original_F"]==source["bundle"]
            assert old["source_numerator"]==self.refs[label+"-complete-bounded-polynomial-numerator"]
            refs.append(self.refs[name]);self.checkpoint("full-polynomial-identity",label,274)
        name=label+"-complete-bounded-connection-certificate";old=self.old(name)
        if old is None:
            self.put(name,{
                "prime":P,"label":label,"source_original_connection":source["connection"],
                "source_complete_bundle_F":source["bundle"],
                "source_original_full543_solution":source["solution"],
                "denominator":self.refs[label+"-complete-denominator-norm"],
                "bounded_numerator":self.refs[label+"-complete-bounded-polynomial-numerator"],
                "original_c":self.refs[label+"-original-c-polynomial"],
                "full_polynomial_coefficient_checks":refs,
                "all277_coefficients_times272_rows_verified":True,
                "full_original_F_transpose_times_y_equals_d_times_c_verified":True,
                "all_original_numerator_degree_bounds_verified":True,
                "original_543_gauge_and_full_logarithmic_principal_parts_preserved":True,
                "whole_D_norm_all_length272_multiplicities_preserved":True,
                "exact_characteristic_zero_expression":{
                    "operation":"same_original_trace_dual_connection_with_determinant_ratio_numerator",
                    "source_original_connection":source["connection"],
                    "source_original_exact_F":source["bundle"],
                    "source_original_exact_c_unit_solve":source["solution"],
                    "d":"det(F(z))/det(F(a))",
                    "y":"adjugate(F(z)^t)*c(z)/det(F(a))",
                    "alpha":"sum_i (y_i/d)*beta_i_trace_dual*dz",
                    "proof":self.item["proofs"]["R922"]},
                "finite_arrays_are_true_original_auxiliary_place_images":True,
                "characteristic_zero_numerator_denominator_coordinates_expanded":False,
                "target_denominator_units_or_target_connection_values_computed":False,
                "Hecke_calibration_nonp_period_or_height_computed":False})
        else:
            assert old["full_polynomial_coefficient_checks"]==refs
        self.done[label]=self.refs[name]
        self.checkpoint("divisor-complete",label,274)

    def direction(self,label):
        name=label+"-complete-bounded-connection-certificate"
        old=self.old(name)
        if old is not None:
            assert old["source_original_connection"]==self.inputs["divisors"][label]["connection"]
            self.done[label]=self.refs[name];return
        self.budget()
        source,graph,model,solution,connection,labels,FF,inverse0,a=self.data(label)
        c=self.coefficient_vector(label,source,solution,labels,a)
        denominator=self.norm(label,source,model,a)
        vectors,blocks=self.Taylor(label,source,FF,inverse0,c,a)
        numerator=self.numerator(label,source,c,denominator,vectors,blocks,a)
        self.verify_polynomial(label,source,FF,c,denominator,numerator)

    def manifest(self):
        entries=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name==self.path("current").name or path.name.startswith(PREFIX+"stage-manifest-"):continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
            entries.append(spec(path))
        current=spec(self.path("current")) if self.path("current").exists() else None
        value={"result":RESULT,"complete":True,"configuration":self.tag,
            "files":entries,"current_checkpoints":[] if current is None else [current]}
        path=self.path("stage-manifest-"+fingerprint(value))
        if path.exists():assert read(path)==value
        else:save(path,value)
        return spec(path)

    def finish(self,complete,reason):
        value={"result":RESULT,"configuration":self.tag,"complete":bool(complete),"p":41,
            "prime":P,"normal_basis_rank":N,"normal_basis_degrees":EPS,
            "source_audit":self.refs.get("source-audit"),
            "source_divisor_order":list(LABELS),"actual_completed_divisors":len(self.done),
            "complete_bounded_connection_certificates":dict(self.done),
            "actual_seven_original_bounded_connection_numerators_certified":len(self.done)==7,
            "same_original_543_choices_and_full_principal_parts_preserved":True,
            "source_characteristic_zero_numerator_denominator_arrays_expanded":False,
            "shared_low_weight_R_computed_in_this_scope":False,
            "whole_target_denominator_units_or_seven_target_values_computed":False,
            "Hecke_calibration_nonp_Picard_period_or_height_computed":False,
            "old_F_inverse_543_solution_or_D_primitive_recomputed":False,
            "stage_manifest":self.manifest(),"resume_state":self.current,
            "scope_stop_reason":reason,"seconds":time.monotonic()-self.started}
        if complete:assert set(self.done)==set(LABELS)
        save(self.out/FINAL,value);return value

    def run(self):
        for ordinal,label in enumerate(LABELS):
            if ordinal>=self.max_divisors:return self.finish(False,"requested_divisor_prefix_complete")
            self.direction(label)
        return self.finish(True,None)

def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise SystemExit("R926 new arithmetic runs only in the authorized public repository Actions.")
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
    except Exception as exc:error=type(exc).__name__+": "+str(exc);traceback.print_exc()
    if code in (1,124) and job is not None:job.finish(False,error)
    receipt={"result":RESULT,"source_sha256":sha(__file__),"complete":code==0,
        "process_exit_code":code,"error":error,"seconds":time.monotonic()-started,
        "configuration":None if job is None else job.tag,
        "certificate_sha256":sha(out/FINAL) if (out/FINAL).exists() else None,
        "all_new_arithmetic_only_in_public_Actions":True}
    save(out/"core-receipt.json",receipt)
    log={k:v for k,v in receipt.items() if k!="configuration"}
    log["configuration_sha256"]=None if job is None else fingerprint(job.tag)
    print("R926_CORE_RECEIPT="+json.dumps(log,sort_keys=True),flush=True)
    raise SystemExit(code)
if __name__=="__main__":main()
