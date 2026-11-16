#!/usr/bin/env python3
"""R896: complete low-weight residual RR spaces from the original two-B pencil.

Exact objects are the source-bound characteristic-zero unit-solve expressions.
Arrays are their images at the original p753 branch.  New arithmetic is allowed
only in this public repository's Actions; no source matrix is relabelled.
"""
import argparse
import gc
import gzip
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import sys
import time
import traceback
import flint
from flint import nmod_mat

REPOSITORY="Rogerhu12/math-research-public"
RESULT="R896-original-five-sum-Hom-low-weight-residual-RR"
FINAL="p41-original-five-sum-Hom-low-weight-residual-RR-certificate.json"
PREFIX="R896-"
MANIFEST="full-outputs-manifest.json"
P=1000000753
N=272
EPS=[0]+[1]*144+[2]*127
POWERS=[12,8,8,13,14]
POLE_DEGREES=[2970,1674,1800,3024,3339]
DELTAS=[294,502,376,512,469]
B_DIMENSIONS=[168,376,250,386,343]
FIBRE_COUNTS=[23,15,15,25,27]
RESIDUAL_DIMENSIONS=[396,188,314,178,221]
PADDING=[250,42,168,32,75]
MANDATORY=("R893","R880","R872","R883","R827","R890","C0")
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
STRATEGY={
    "original_curve":"original genus127 Y, level82 and original minus3 descent",
    "prime":P,"original_branch":0,"original_integral_B_root":3197390,
    "original_s_root":99932770,"original_zeta_root":549966761,
    "original_Hom_words":["1+T^"+str(j) for j in range(1,6)],
    "normal_basis_degrees":EPS,"ordinary_powers":POWERS,
    "original_pole_degrees":POLE_DEGREES,"residual_degrees":DELTAS,
    "complete_initial_B_dimensions":B_DIMENSIONS,"original_fibre_counts":FIBRE_COUNTS,
    "V3_dimension":690,"marked_B0":"first original A-kernel column with unit original P0 value; unscaled",
    "second_B":"sum(c^i*B_i), exact positive integer c=1,2,... in fixed original kernel",
    "two_B_product_rank":[690+d for d in DELTAS],
    "two_B_products_have_weight":"n+3; original N>n+3; no V2n injection assumed",
    "residual_complete_dimensions":RESIDUAL_DIMENSIONS,
    "kernel_projection":"second690 rows, full relation kernel of [B0 V3,B1 V3]",
    "padding_orders":PADDING,"padding_complete_dimension":146,
    "old_normal_V3_point_matrix_shape":[252,690],
    "v_selection":"first padding-kernel column with unit coefficient at exact padding order; unscaled",
    "w_schedule":"sum(c^i*U_i), exact positive integer c=1,2,...",
    "final_fibres":"first seven already accepted whole fibres for the same original direction",
    "final_pencil_matrix_shape":[1904,1380],"final_pencil_rank":962,
    "final_complete_space_shape":[690,418],
    "fixed_B0_and_v_products_shared_across_all_trials":True,
    "old_R890_normal_V3_fibres_0_through_6_reused":True,
    "old_initial_Schur_y_multipliers_Krylov_inverses_and_jets_recomputed":False,
    "principal_G":"(B0/tau^n)/(v/tau^3)=tau^(3-n)*B0/v",
    "principal_Q":"G*(u_chi/tau^2)^(-(n-2))",
    "class_identity":"E-deg(E)P0=(Dstd-H)+(n-2)(Dchi-H)+div(Q)",
    "P0_pole_multiplicity":1,"m0_source":"actual original R848 c0 nonzero tangents and original local model",
    "rho_leading_Q":"b1/v_k * u_chi_272^(-(n-2))",
    "t_leading_Q":"rho_leading_Q * original_c^(deg(E)-1)",
    "unit_is_only_at_the_original_auxiliary_place":True,
    "exact_Galois_transports_preserve_all_original_indices_and_integer_parameters":True,
    "normal_integer_scale_applied_again":False,
    "characteristic_zero_coefficients_reconstructed":False,
    "five_Lj128_Picard_support_connection_or_height_computed":False,
    "only_budget_requested_directions_and_trial_limits_excluded_from_identity":True,
}
class BudgetStop(RuntimeError):
    pass
class UnitFailure(RuntimeError):
    pass
class ScopeStop(RuntimeError):
    pass

def guard():
    assert os.environ.get("GITHUB_ACTIONS")=="true","New mathematics only in public Actions."
    assert os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for part in iter(lambda:f.read(4*1024*1024),b""):
            h.update(part)
    return h.hexdigest()
def read(path):
    path=Path(path)
    with (gzip.open if path.suffix==".gz" else open)(path,"rt",encoding="utf-8") as f:
        return json.load(f)
def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name(path.name+".tmp")
    raw=(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n").encode()
    if path.suffix==".gz":
        with temp.open("wb") as f:
            with gzip.GzipFile(filename="",fileobj=f,mode="wb",mtime=0,compresslevel=2) as z:
                z.write(raw)
    else:
        temp.write_bytes(raw)
    temp.replace(path)
def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def plain(row):
    answer={k:row[k] for k in ("file","bytes","sha256")}
    p=PurePosixPath(answer["file"])
    assert len(p.parts)==1 and p.name not in ("",".","..") and "\\" not in answer["file"]
    return answer
def spec(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}
def identity(source):
    out={k:source[k] for k in BASE}
    out["configuration_sha256"]=source["configuration_sha256"]
    out["selected_files_sha256"]=fingerprint(source["files"])
    if source.get("certificate") is not None:
        out["certificate"]=plain(source["certificate"])
    else:
        out["configuration_stage"]=plain(source["configuration_stage"])
        out["accepted_process_exit_codes"]=source["accepted_process_exit_codes"]
    return out
def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"p":41,"python_flint":"0.9.0",
            "method_sha256":item["method_sha256"],"proofs":item["proofs"],
            "sources":{k:identity(v) for k,v in sorted(item["sources"].items())},
            "inputs":item["inputs"],"strategy":STRATEGY}
def shape(a,m,n):
    assert len(a)==m and all(len(row)==n for row in a),(m,n)
def matrix(raw):
    return nmod_mat(raw,P)
def rows(A):
    return [[int(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())]
def zero(m,n):
    return nmod_mat(m,n,P)
def eye(n):
    return matrix([[int(i==j) for j in range(n)] for i in range(n)])
def sub(A,I,J):
    return matrix([[int(A[i,j]) for j in J] for i in I])
def hcat(A,B):
    assert A.nrows()==B.nrows()
    return matrix([[int(A[i,j]) for j in range(A.ncols())]+
                   [int(B[i,j]) for j in range(B.ncols())] for i in range(A.nrows())])
def pivots(A,r):
    answer=[next(j for j in range(A.ncols()) if A[i,j]) for i in range(r)]
    assert answer==sorted(set(answer))
    return answer
def positions(m):
    return [(i,k) for i in range(N) for k in range(max(0,m-EPS[i]+1))]
def invert(x,reason):
    x=int(x)%P
    if not x:
        raise UnitFailure(reason)
    return pow(x,-1,P)
def same_origin(a,b):
    assert all(str(a[k])==str(b[k]) for k in BASE)
    if a.get("configuration_sha256") is not None and b.get("configuration_sha256") is not None:
        assert a["configuration_sha256"]==b["configuration_sha256"]

class Source:
    def __init__(self,label,item,root):
        self.label=label;self.item=item;self.folder=Path(root)/label;self.checked=set()
        self.files={name:plain(row) for name,row in item["files"].items()}
        path=self.folder/MANIFEST
        assert spec(path)==self.files[MANIFEST] and sha(path)==item["manifest_sha256"]
        manifest=read(path);assert manifest["result"]==item["result"]
        indexed={row["file"]:plain(row) for row in manifest["files"]}
        assert len(indexed)==len(manifest["files"])
        indexed[MANIFEST]=spec(path)
        for name,row in self.files.items():
            assert name==row["file"]
            if name!="full-outputs-manifest-reference.json":
                assert indexed[name]==row,(label,name)
        initial=self.raw("public-actions-input.json");run=self.raw("run-receipt.json")
        assert initial["source_commit"]==run["source_commit"]==item["source_commit"]
        assert str(run["workflow_run_id"])==str(item["run_id"])
        oldcore=initial.get("core_sha256",initial.get("job",{}).get("core_sha256"))
        assert oldcore==item["core_sha256"]
        self.certificate=None
        if item.get("certificate") is not None:
            self.certificate=self.raw(item["certificate"]["file"])
            assert self.files[item["certificate"]["file"]]==plain(item["certificate"])
            assert self.certificate["result"]==item["result"] and self.certificate["complete"] is True
            assert run["complete"] is True and run["process_exit_code"]==0
            self.tag=self.certificate["configuration"]
        else:
            assert label=="R827" and run["complete"] is False
            assert run["process_exit_code"] in item["accepted_process_exit_codes"]
            assert 0 not in item["accepted_process_exit_codes"]
            anchor=self.raw(item["configuration_stage"]["file"])
            assert anchor["complete"] is True
            self.tag=anchor["configuration"]
        assert fingerprint(self.tag)==item["configuration_sha256"]
        assert self.tag.get("source_sha256",self.tag.get("core_sha256"))==item["core_sha256"]
        if run.get("core_receipt_sha256") is not None:
            assert self.files["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
            receipt=self.raw("core-receipt.json")
            assert receipt["source_sha256"]==item["core_sha256"]
            if receipt.get("configuration") is not None:
                assert receipt["configuration"]==self.tag
            if receipt.get("configuration_sha256") is not None:
                assert receipt["configuration_sha256"]==item["configuration_sha256"]
            if self.certificate is not None:
                assert receipt["complete"] is True
                assert receipt["certificate_sha256"]==item["certificate"]["sha256"]
    def raw(self,name):
        path=self.folder/name
        if name not in self.checked:
            assert spec(path)==self.files[name],(self.label,name)
            self.checked.add(name)
        return read(path)
    def stage(self,row):
        assert self.files[row["file"]]==plain(row)
        value=self.raw(row["file"])
        assert value["complete"] is True and value["configuration"]==self.tag
        assert value["result"]==self.item["result"]
        return value
    def ref(self,row):
        assert self.files[row["file"]]==plain(row)
        return {"source_group":self.label,**plain(row)}

class Job:
    def __init__(self,args):
        self.args=args;self.started=time.monotonic();self.item=read(args.config)
        self.out=Path(args.output);self.out.mkdir(parents=True,exist_ok=True)
        assert self.item["result"]==RESULT and self.item["p"]==41
        assert self.item["producer_inputs_pending"] is False
        assert sha(__file__)==self.item["core_sha256"] and flint.__version__=="0.9.0"
        topic=Path(__file__).resolve().parent.parent
        assert sha(topic/self.item["method"])==self.item["method_sha256"]
        for entry in self.item["proofs"].values():
            assert sha(topic/entry["path"])==entry["sha256"]
        assert set(self.item["sources"])==set(MANDATORY)
        self.tag=expected_tag(self.item);self.refs={};self.done={};self.current=None
        self.phase="source_initialization"
        self.sources={g:Source(g,v,args.retained) for g,v in self.item["sources"].items()}
        self.inputs=self.item["inputs"]
        self.requested=self.item.get("requested_directions",[1,2,3,4,5])
        assert self.requested and self.requested==sorted(set(self.requested))
        assert all(isinstance(j,int) and 1<=j<=5 for j in self.requested)
        self.B_trials=int(self.item.get("maximum_B_pencil_trials",4))
        self.U_trials=int(self.item.get("maximum_U_pencil_trials",4))
        assert 1<=self.B_trials<P and 1<=self.U_trials<P
        self.V3=positions(3);self.V3map={p:k for k,p in enumerate(self.V3)}
        assert len(self.V3)==690
        self.fibres={};self.original_directions={}
    def budget(self):
        if time.monotonic()-self.started>=self.args.budget_minutes*60-30:
            raise BudgetStop("Completed original stages retained; phase="+self.phase)
    def path(self,name):
        assert Path(name).name==name
        return self.out/(PREFIX+name+".json.gz")
    def old(self,name):
        path=self.path(name)
        if not path.exists():
            return None
        value=read(path)
        assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
        self.refs[name]=spec(path)
        return value
    def put(self,name,payload):
        assert not set(payload)&{"result","configuration","complete"}
        value={"result":RESULT,"configuration":self.tag,"complete":True,**payload}
        path=self.path(name)
        if path.exists():
            assert read(path)==value
        else:
            save(path,value)
        self.refs[name]=spec(path)
        print("R896_STAGE="+json.dumps({"file":path.name,"seconds":time.monotonic()-self.started}),flush=True)
        return value
    def checkpoint(self,phase):
        self.phase=phase
        value={"result":RESULT,"configuration":self.tag,"complete":False,
               "phase":phase,"complete_direction_certificates":self.done,"complete_stages":self.refs}
        save(self.path("current"),value);self.current=spec(self.path("current"))
        return self.current
    def source(self,row):
        return self.sources[row["source_group"]].stage(row)
    def input(self,key):
        return self.source(self.inputs[key])
    def own(self,row):
        path=self.out/row["file"];assert spec(path)==plain(row)
        value=read(path)
        assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
        return value
    def ref(self,name):
        return self.refs[name]
    def prepare(self):
        original=self.sources["R893"]
        assert original.certificate["all_five_complete_initial_RR_spaces_certified"] is True
        assert original.certificate["characteristic_zero_kernel_coordinates_reconstructed"] is False
        assert original.certificate["original_Hom_words"]==STRATEGY["original_Hom_words"]
        assert original.certificate["original_pole_degrees"]==POLE_DEGREES
        assert original.certificate["initial_RR_dimensions"]==B_DIMENSIONS
        assert set(self.inputs["initial_RR_certificates"])==set(map(str,range(1,6)))
        for j,row in self.inputs["initial_RR_certificates"].items():
            assert row["source_group"]=="R893"
            assert plain(row)==plain(original.certificate["complete_initial_RR_certificates"][j])
        for parent in ("R893","R890"):
            same_origin(self.sources[parent].tag["sources"]["R827"],self.item["sources"]["R827"])
        same_origin(self.sources["R880"].tag["sources"]["R872"],self.item["sources"]["R872"])
        same_origin(self.sources["R890"].tag["sources"]["R872"],self.item["sources"]["R872"])
        self.point=self.input("point_linear_functional")
        self.Jdata=self.input("normal_V3_point_jets")
        self.chi=self.input("fixed_chi_divisor");self.u_chi=self.input("fixed_chi_anchor")
        self.frame=self.input("t_frame")
        assert self.point["chosen_local_parameter"]=="z_minus_z0"
        assert self.point["z0_mod_prime"]==110702704 and self.point["w0_mod_prime"]==645975656
        self.zP0=int(self.point["z0_mod_prime"])
        self.betaP0=self.point["point_evaluation_mod_prime"]
        assert len(self.betaP0)==N and self.betaP0[0]==1
        assert self.Jdata["prime"]==P and self.Jdata["matrix_shape"]==[252,690]
        assert self.Jdata["row_orders"]==list(range(252))
        assert self.Jdata["local_parameter"]=="z_minus_z0"
        assert self.Jdata["V3_basis"]==[{"normal_basis_row":i,"power_of_z":k} for i,k in self.V3]
        assert self.Jdata["no_original_Hensel_step_recomputed"] is True
        shape(self.Jdata["matrix_mod_prime"],252,690)
        self.J3=matrix(self.Jdata["matrix_mod_prime"])
        assert self.chi["prime"]==P and self.chi["D_chi_degree"]==272
        assert self.chi["D_chi_effective_and_avoids_original_P0"] is True
        assert self.chi["actual_complete_fixed_chi_RR_space_certified"] is True
        assert self.chi["exact_divisor_identity"]=="chi-(D_chi-H)=-div(u/tau^2)"
        assert plain(self.chi["source_exact_u"])==plain(self.inputs["fixed_chi_anchor"])
        assert self.u_chi["prime"]==P and self.u_chi["role"]=="u"
        assert self.u_chi["order272_is_exact"] is True
        assert self.u_chi["normal_integer_scale_applied_again"] is False
        self.uchi_leading=int(self.u_chi["exact_order272_unit"])
        assert self.uchi_leading%P
        assert self.frame["original_t_first_order_unit_certified"] is True
        assert self.frame["original_s_root"]==99932770
        assert self.frame["quotient_all_three_coefficients_multiplied_back"] is True
        assert self.frame["exact_zero_not_inferred_from_modular_zero"] is True
        self.t_over_rho=int(self.frame["original_t_over_rho_constant_mod_prime"])
        assert self.t_over_rho==354813668
        c0=self.sources["C0"].certificate
        assert c0["all_six_original_lambda_cubes_and_logarithmic_derivatives_computed"] is True
        assert c0["all_original_nonzero_values_and_division_denominators_checked"] is True
        assert c0["original_pq_eta_directions_and_true_norm_constants_preserved"] is True
        assert set(self.inputs["c0_W_jets"])==set(map(str,range(1,6)))
        for j,row in self.inputs["c0_W_jets"].items():
            assert row["source_group"]=="C0" and plain(row)==plain(c0["W_jets"][j])
            jet=self.source(row)
            assert jet["j"]==int(j) and jet["original_map"]=="f4+T^"+j+" f4"
            assert jet["actual_W_and_lambda_cube_nonzero"] is True
            assert jet["all_field_inverses_and_displayed_quotients_multiplied_back"] is True
            assert jet["cubic_root_selected_or_extra_target_phase_inserted"] is False
        self.Wref=self.inputs["original_W"]
        assert self.Wref["source_group"]=="R827"
        assert plain(self.Wref)==plain(original.tag["inputs"]["original_W"])
        W=self.input("original_W")
        assert W["prime"]==P
        self.cache_refs=self.inputs["cached_normal_V3_fibres"]
        assert set(self.cache_refs)==set(map(str,range(7)))
        for z,row in self.cache_refs.items():
            assert row["source_group"]=="R890"
            cached=self.source(row)
            assert cached["z0"]==int(z) and cached["prime"]==P
            assert cached["old_W_K_or_Kinverse_recomputed"] is False
            assert cached["normal_integer_scale_applied_again"] is False
            assert cached["normal_V3_basis"]==[list(p) for p in self.V3]
            assert plain(cached["source_original_W"])==plain(self.Wref)
            shape(cached["normal_evaluation_mod_prime"],272,690)
            shape(cached["cyclic_evaluation_mod_prime"],272,690)
        name="original-source-audit"
        if self.old(name) is None:
            self.put(name,{
                "prime":P,"original_branch":0,"original_integral_B_root":3197390,
                "original_s_root":99932770,"original_zeta_root":549966761,
                "sources":{g:identity(v) for g,v in self.item["sources"].items()},"inputs":self.inputs,
                "normal_basis_degrees":EPS,
                "all_five_source_R893_complete_initial_spaces_certified":True,
                "old_normal_V3_jets_and_seven_completed_normal_fibres_reused":True,
                "original_c0_multiplicity":1,
                "original_c0_multiplicity_source":{
                    "certificate":self.item["sources"]["C0"]["certificate"],
                    "five_completed_lambda_cube_nonzero_stages":self.inputs["c0_W_jets"],
                    "theorem":self.item["proofs"]["R848"],
                    "local_nonramification_proof":self.item["proofs"]["c0"],
                    "exact_zero_not_inferred_from_modular_zero":True},
                "source_original_chi_principal_sign_verified":True,
                "original_frame_and_unscaled_section_conventions_preserved":True,
                "all_new_mathematics_only_in_public_Actions":True})
        self.checkpoint(name)

    def original_direction(self,j):
        if j in self.original_directions:
            return self.original_directions[j]
        source=self.sources["R893"];ref=self.inputs["initial_RR_certificates"][str(j)]
        cert=self.source(ref)
        n=POWERS[j-1];dim=B_DIMENSIONS[j-1];delta=DELTAS[j-1]
        assert cert["prime"]==P and cert["j"]==j and cert["ordinary_power"]==n
        assert cert["original_Hom_word"]=="1+T^"+str(j)
        assert cert["original_pole_degree"]==POLE_DEGREES[j-1]
        assert cert["residual_degree"]==delta and cert["complete_kernel_dimension"]==dim
        assert cert["complete_initial_RR_space_certified"] is True
        assert cert["all_original_Schur_rows_verified"] is True
        assert cert["all_complete_fibre_original_A_minus_yB_relations_verified"] is True
        assert cert["exact_unit_solve_expression_certified"] is True
        assert cert["actual_arrays_are_only_modular_reductions"] is True
        Aref=source.ref(cert["complete_A_kernel"]);Bref=source.ref(cert["complete_B_kernel"])
        A=source.stage(Aref);B=source.stage(Bref)
        mapping=[list(p) for p in positions(n)];d=272*n-126
        assert A["original_column_mapping"]==B["original_column_mapping"]==mapping
        assert A["normal_basis_degrees"]==B["normal_basis_degrees"]==EPS
        assert plain(A["source_complete_B_kernel"])==plain(Bref)
        assert A["array_is_modular_reduction_of_the_exact_unit_solve"] is True
        assert B["canonical_free_identity_verified"] is True
        assert B["all_original_Schur_rows_times_full_kernel_zero"] is True
        shape(A["A_coefficients_mod_prime"],d,dim);shape(B["B_coefficients_mod_prime"],d,dim)
        selected_ref=source.ref(cert["source_complete_fibres"]);selected=source.stage(selected_ref)
        nodes=selected["nodes"]
        assert len(nodes)==FIBRE_COUNTS[j-1] and nodes==sorted(set(nodes))
        assert all(isinstance(a,int) and 0<=a<P for a in nodes)
        assert selected["all_denominators_units_in_the_whole_fibres"] is True
        assert selected["residue_field_factors_or_multiplicities_removed"] is False
        assert len(nodes)>n+3
        assert len(A["source_complete_yB_fibre_values"])==len(nodes)
        assert len(cert["all_original_fibre_relation_certificates"])==len(nodes)
        values={};algebras={}
        for a,sr,vr,cr in zip(nodes,selected["full_fibre_sources"],
                A["source_complete_yB_fibre_values"],cert["all_original_fibre_relation_certificates"]):
            single=source.stage(sr);value=source.stage(vr);check=source.stage(cr)
            assert single["j"]==j and single["z0"]==a and single["whole_fibre_unit"] is True
            assert single["all272_original_Q_times_y_equals_P_verified"] is True
            assert single["factors_or_nilpotents_removed"] is False
            assert value["j"]==j and value["z0"]==a and value["prime"]==P
            assert plain(value["source_complete_B_kernel"])==plain(Bref)
            assert value["all_kernel_columns_evaluated_in_original_normal_basis"] is True
            shape(value["B_fibre_values_mod_prime"],272,dim)
            assert check["j"]==j and check["z0"]==a
            assert check["all272_times_complete_kernel_dimension_original_relations_zero"] is True
            assert plain(check["source_complete_A_kernel"])==plain(Aref)
            assert plain(check["source_complete_B_kernel"])==plain(Bref)
            assert plain(check["source_original_yB_values"])==plain(vr)
            values[a]=source.ref(vr)
            algebras[a]=source.ref(single["source_complete_fibre"])
        out={"certificate":cert,"reference":ref,"n":n,"dim":dim,"delta":delta,
             "A":A,"Aref":Aref,"B":B,"Bref":Bref,"nodes":nodes,
             "selected_ref":selected_ref,"values":values,"algebras":algebras}
        self.original_directions={j:out}
        return out

    def fibre(self,a,algebra_ref):
        if a in self.fibres:
            assert self.fibres[a]["algebra_ref"]==algebra_ref
            return self.fibres[a]
        algebra=self.source(algebra_ref)
        assert algebra["prime"]==P and algebra["z0"]==a and algebra["usable"] is True
        assert plain(algebra["source_original_W"])==plain(self.Wref)
        original_point_ref=None
        if "source_original_Krylov" in algebra:
            assert algebra["source_original_Krylov"]["source_group"]=="R827"
            original_point_ref={**algebra["source_original_Krylov"],"source_group":"R827"}
            point=self.source(original_point_ref)
            assert point["prime"]==P and point["z0"]==a and point["usable"] is True
            assert point["actual_cyclic_rank"]==272
            assert point["both_inverse_products_verified"] is True
            assert plain(point["source_original_W"])==plain(self.Wref)
            assert algebra["original_Krylov_matrix_or_inverse_or_k272_recomputed"] is False
            Wraw=point["W_evaluated_mod_prime"]
            Kiraw=point["inverse_Krylov_matrix_mod_prime"]
        else:
            assert algebra["both_inverse_products_verified"] is True
            assert algebra["actual_cyclic_rank"]==272 and algebra["no_factors_removed"] is True
            built=self.sources["R893"].stage(algebra["source_new_Krylov_matrix"])
            assert built["z0"]==a and built["prime"]==P
            assert built["full_original_characteristic_relation_on_cyclic_vector_verified"] is True
            Wraw=built["W_evaluated_mod_prime"]
            Kiraw=algebra["inverse_Krylov_matrix_mod_prime"]
        shape(Wraw,272,272);shape(Kiraw,272,272)
        if str(a) in self.cache_refs:
            normal_ref=self.cache_refs[str(a)];normal=self.source(normal_ref)
            assert original_point_ref is not None
            assert plain(normal["source_original_Krylov_point"])==plain(original_point_ref)
        else:
            name=f"node-{a:06d}-new-normal-V3-evaluation"
            normal=self.old(name)
            if normal is None:
                self.budget()
                E=[[0]*690 for _ in range(272)];cyclic=[[0]*690 for _ in range(272)]
                for j,(i,k) in enumerate(self.V3):
                    scalar=pow(a,k,P);E[i][j]=scalar
                    for row in range(272):
                        cyclic[row][j]=int(Kiraw[row][i])*scalar%P
                normal=self.put(name,{"prime":P,"z0":a,
                    "source_complete_original_fibre":algebra_ref,
                    "source_original_W":self.Wref,
                    "normal_V3_basis":[list(p) for p in self.V3],
                    "normal_evaluation_mod_prime":E,"cyclic_evaluation_mod_prime":cyclic,
                    "matrix_shape":[272,690],
                    "only_new_node_normal_V3_columns_formed":True,
                    "old_W_Krylov_or_inverse_arithmetic_recomputed":False,
                    "no_residue_factor_or_nilpotent_removed":True})
                self.checkpoint(name)
            assert normal["source_complete_original_fibre"]==algebra_ref
            normal_ref=self.ref(name)
        out={"W":matrix(Wraw),"E":matrix(normal["normal_evaluation_mod_prime"]),
             "CE":matrix(normal["cyclic_evaluation_mod_prime"]),
             "reference":normal_ref,"algebra_ref":algebra_ref}
        self.fibres[a]=out
        return out

    def mark_original_pair(self,j,original):
        name=f"j{j}-original-unscaled-marked-A-B"
        marked=self.old(name)
        if marked is None:
            self.budget()
            n=original["n"];mapping=positions(n);d=len(mapping);dim=original["dim"]
            beta1=[int(self.J3[1,self.V3map[(i,0)]]) for i in range(N)]
            assert int(self.J3[0,self.V3map[(0,0)]])==1 and beta1[0]==0
            assert int(self.J3[1,self.V3map[(0,1)]])==1
            eval0=[];eval1=[]
            for i,k in mapping:
                power=pow(self.zP0,k,P)
                eval0.append(int(self.betaP0[i])*power%P)
                slope=(power*beta1[i]+(k*pow(self.zP0,k-1,P)*int(self.betaP0[i]) if k else 0))%P
                eval1.append(slope)
            all_A=matrix([eval0])*matrix(original["A"]["A_coefficients_mod_prime"])
            avals=[int(all_A[0,k]) for k in range(dim)]
            chosen=next((k for k,x in enumerate(avals) if x),None)
            if chosen is None:
                self.put(name+"-unit-failure",{"prime":P,"j":j,
                    "source_complete_A_kernel":original["Aref"],
                    "source_original_P0":self.inputs["point_linear_functional"],
                    "actual_A_values_mod_prime":avals,"no_unit_column_found":True,
                    "original_space_or_nonramification_disproved":False})
                raise UnitFailure("No original A-kernel column has a unit P0 value for j="+str(j))
            a=[int(row[chosen]) for row in original["A"]["A_coefficients_mod_prime"]]
            b=[int(row[chosen]) for row in original["B"]["B_coefficients_mod_prime"]]
            b0=sum(x*y for x,y in zip(eval0,b))%P
            b1=sum(x*y for x,y in zip(eval1,b))%P
            assert b0==0,("source_c0_pole_and_exact_relation",j)
            invert(b1,"The selected original B first coefficient is not a unit at p753.")
            weights=[int(k==chosen) for k in range(dim)]
            marked=self.put(name,{
                "prime":P,"j":j,"ordinary_power":n,"original_Hom_word":"1+T^"+str(j),
                "source_complete_initial_RR":original["reference"],
                "source_complete_A_kernel":original["Aref"],"source_complete_B_kernel":original["Bref"],
                "source_original_P0":self.inputs["point_linear_functional"],
                "source_completed_normal_V3_jets":self.inputs["normal_V3_point_jets"],
                "source_original_c0_W_jet":self.inputs["c0_W_jets"][str(j)],
                "original_kernel_column":chosen,"kernel_weights_mod_prime":weights,
                "all_original_A_P0_values_mod_prime":avals,
                "actual_A0_P0_value_mod_prime":avals[chosen],
                "A_coordinates_mod_prime":a,"B_coordinates_mod_prime":b,
                "original_column_mapping":[list(p) for p in mapping],
                "actual_B0_constant_mod_prime":b0,"actual_B0_first_coefficient_mod_prime":b1,
                "original_rho_parameter":"z_minus_z0","exact_B0_rho_order":1,
                "P0_pole_multiplicity":1,"F0_degree":DELTAS[j-1],"F0_avoids_original_P0":True,
                "A0_P0_and_B0_first_coefficient_are_units":True,
                "original_scalar_not_rescaled":True,
                "exact_zero_inherited_from_original_global_relation_and_c0_pole":True,
                "exact_zero_not_inferred_from_modular_zero":True,
                "exact_pair_definition":{
                    "operation":"unchanged_column_of_completed_original_A_B_unit_solve",
                    "source_A":original["Aref"],"source_B":original["Bref"],"column":chosen,
                    "normal_tau_power":n,"extra_scalar":1},
                "new_first_jet_transport":{
                    "formula":"[rho] z^k beta_i=z0^k beta_i,1+k z0^(k-1) beta_i,0",
                    "source_existing_beta_orders":[0,1],"old_Hensel_steps_recomputed":False},
                "complete_B_space_or_A_kernel_recomputed":False})
            self.checkpoint(name)
        assert marked["source_complete_A_kernel"]==original["Aref"]
        assert marked["source_complete_B_kernel"]==original["Bref"]
        return marked,self.ref(name)

    def B_anchor(self,j,original,marked,marked_ref,trial=None):
        if trial is None:
            return marked,marked_ref
        name=f"j{j}-B1-trial-{trial:06d}-unscaled-section"
        value=self.old(name)
        if value is None:
            self.budget()
            dim=original["dim"];weights=[pow(trial,i,P) for i in range(dim)]
            vector=matrix(original["B"]["B_coefficients_mod_prime"])*matrix([[x] for x in weights])
            value=self.put(name,{"prime":P,"j":j,"ordinary_power":original["n"],
                "trial":trial,"source_complete_B_kernel":original["Bref"],
                "source_complete_initial_RR":original["reference"],
                "kernel_weights_mod_prime":weights,
                "B_coordinates_mod_prime":[int(vector[i,0]) for i in range(vector.nrows())],
                "exact_section_definition":{
                    "operation":"integer_power_combination_of_original_complete_B_kernel",
                    "source":original["Bref"],"integer_parameter":trial,"exponents":[0,dim-1],
                    "coefficients_are_exact_integer_powers_not_arbitrary_residue_lifts":True},
                "original_scalar_not_rescaled":True})
            self.checkpoint(name)
        assert value["source_complete_B_kernel"]==original["Bref"] and value["trial"]==trial
        return value,self.ref(name)

    def B_products(self,stem,j,original,anchor,anchor_ref):
        references=[];data=[]
        for a in original["nodes"]:
            name=stem+f"-node-{a:06d}-times-normal-V3"
            value=self.old(name)
            if value is None:
                self.budget()
                f=self.fibre(a,original["algebras"][a])
                raw=self.source(original["values"][a])["B_fibre_values_mod_prime"]
                weights=anchor["kernel_weights_mod_prime"]
                if "original_kernel_column" in anchor:
                    column=anchor["original_kernel_column"]
                    section=matrix([[row[column]] for row in raw])
                else:
                    section=matrix(raw)*matrix([[x] for x in weights])
                current=section;columns=[]
                for k in range(N):
                    columns.append([int(current[i,0]) for i in range(N)])
                    if k+1<N:
                        current=f["W"]*current
                product=matrix(columns).transpose()*f["CE"]
                value=self.put(name,{"prime":P,"j":j,"z0":a,"source_anchor":anchor_ref,
                    "source_complete_initial_B_values":original["values"][a],
                    "source_complete_original_fibre":original["algebras"][a],
                    "source_normal_V3_evaluation":f["reference"],
                    "matrix_shape":[272,690],"product_evaluation_mod_prime":rows(product),
                    "section_evaluation_mod_prime":[int(section[i,0]) for i in range(N)],
                    "source_original_B_values_reused_without_reevaluation":True,
                    "formula":"[B,W B,...,W^271 B]*(old_Kinverse*normal_V3)",
                    "all272_original_fibre_coordinates_retained":True,
                    "old_fibre_inverse_or_initial_yB_arithmetic_recomputed":False})
                self.checkpoint(name)
            assert value["source_anchor"]==anchor_ref
            assert value["source_complete_initial_B_values"]==original["values"][a]
            shape(value["product_evaluation_mod_prime"],272,690)
            data.extend(value["product_evaluation_mod_prime"]);references.append(self.ref(name))
        return matrix(data),references

    def V3_products(self,stem,j,original,anchor,anchor_ref):
        references=[];data=[]
        for a in original["nodes"][:7]:
            name=stem+f"-node-{a:06d}-times-normal-V3"
            value=self.old(name)
            if value is None:
                self.budget()
                f=self.fibre(a,original["algebras"][a])
                section=f["E"]*matrix([[x] for x in anchor["normal_V3_coordinates_mod_prime"]])
                current=section;columns=[]
                for k in range(N):
                    columns.append([int(current[i,0]) for i in range(N)])
                    if k+1<N:
                        current=f["W"]*current
                product=matrix(columns).transpose()*f["CE"]
                value=self.put(name,{"prime":P,"j":j,"z0":a,"source_anchor":anchor_ref,
                    "source_complete_original_fibre":original["algebras"][a],
                    "source_normal_V3_evaluation":f["reference"],
                    "matrix_shape":[272,690],"product_evaluation_mod_prime":rows(product),
                    "section_evaluation_mod_prime":[int(section[i,0]) for i in range(N)],
                    "all272_original_fibre_coordinates_retained":True,
                    "formula":"[v,Wv,...,W^271v]*(old_Kinverse*normal_V3)",
                    "old_fibre_inverse_or_initial_yB_arithmetic_recomputed":False})
                self.checkpoint(name)
            assert value["source_anchor"]==anchor_ref
            shape(value["product_evaluation_mod_prime"],272,690)
            data.extend(value["product_evaluation_mod_prime"]);references.append(self.ref(name))
        return matrix(data),references

    def rank_profile(self,name,M,required,source_refs,geometric_bound):
        value=self.old(name)
        if value is None:
            self.budget()
            reduced,rank=M.rref()
            assert rank<=required,("original_geometric_rank_upper_bound",name,rank,required)
            record={"prime":P,"matrix_shape":[M.nrows(),M.ncols()],
                    "required_rank":required,"actual_rank":rank,"accepted":rank==required,
                    "source_references":source_refs,"geometric_characteristic_zero_rank_upper_bound":required,
                    "geometric_rank_source":geometric_bound,
                    "failed_finite_trial_does_not_disprove_original_space":rank<required}
            if rank==required:
                J=pivots(reduced,rank)
                transposed,again=sub(M,list(range(M.nrows())),J).transpose().rref()
                assert again==required
                I=pivots(transposed,again)
                record.update({"selected_columns":J,"selected_rows":I,
                    "original_selected_minor_has_full_rank":True})
            value=self.put(name,record)
            del reduced;gc.collect();self.checkpoint(name)
        assert value["source_references"]==source_refs
        assert value["required_rank"]==required and value["geometric_rank_source"]==geometric_bound
        return value,self.ref(name)

    def complete_kernel(self,stem,M,profile,profile_ref,definition):
        assert profile["accepted"] is True
        r=profile["required_rank"];m,n=M.nrows(),M.ncols()
        I,J=profile["selected_rows"],profile["selected_columns"]
        assert len(I)==len(J)==r
        free=[j for j in range(n) if j not in set(J)]
        invname=stem+"-selected-unit-inverse";invdata=self.old(invname)
        if invdata is None:
            self.budget()
            A=sub(M,I,J);det=int(A.det())
            invert(det,"Selected original minor is not a unit: "+stem)
            inverse=A.inv()
            assert A*inverse==eye(r) and inverse*A==eye(r)
            invdata=self.put(invname,{"prime":P,"source_rank_profile":profile_ref,
                "selected_rows":I,"selected_columns":J,"matrix_shape":[r,r],
                "actual_selected_minor_determinant_mod_prime":det,
                "inverse_selected_minor_mod_prime":rows(inverse),
                "both_selected_inverse_products_verified":True,
                "characteristic_zero_minor_is_a_unit":True})
            self.checkpoint(invname)
        assert invdata["source_rank_profile"]==profile_ref
        rawname=stem+"-canonical-free-kernel";rawdata=self.old(rawname)
        if rawdata is None:
            self.budget()
            inverse=matrix(invdata["inverse_selected_minor_mod_prime"])
            C=-(inverse*sub(M,I,free))
            raw=[[0]*len(free) for _ in range(n)]
            for column,j in enumerate(free):
                raw[j][column]=1
                for k,pivot in enumerate(J):
                    raw[pivot][column]=int(C[k,column])
            K=matrix(raw)
            assert sub(K,free,list(range(len(free))))==eye(len(free))
            assert sub(M,I,list(range(n)))*K==zero(r,len(free))
            rawdata=self.put(rawname,{"prime":P,"source_rank_profile":profile_ref,
                "source_selected_unit_inverse":self.ref(invname),"matrix_shape":[n,len(free)],
                "selected_rows":I,"pivot_columns":J,"free_columns":free,
                "kernel_basis_mod_prime":raw,
                "all_selected_original_rows_times_kernel_zero":True,
                "canonical_free_identity_verified":True,
                "all_original_rows_yet_certified_here":False,
                "exact_candidate_definition":{
                    "operation":"canonical_original_selected_unit_solve",
                    "source_rank_profile":profile_ref,"selected_rows":I,"pivot_columns":J,
                    "free_columns":free,"pivot_formula":"-inverse(M[I,J])*M[I,F]","free_formula":"identity"}})
            self.checkpoint(rawname)
        assert rawdata["source_selected_unit_inverse"]==self.ref(invname)
        K=matrix(rawdata["kernel_basis_mod_prime"]);shape(rawdata["kernel_basis_mod_prime"],n,n-r)
        checks=[]
        for first in range(0,m,272):
            stop=min(m,first+272);name=stem+f"-full-rows-{first:06d}-{stop:06d}"
            check=self.old(name)
            if check is None:
                self.budget()
                assert sub(M,list(range(first,stop)),list(range(n)))*K==zero(stop-first,n-r)
                check=self.put(name,{"prime":P,"source_canonical_kernel":self.ref(rawname),
                    "source_rank_profile":profile_ref,"original_row_interval":[first,stop],
                    "checked_shape":[stop-first,n-r],"all_original_rows_in_interval_times_kernel_zero":True})
                self.checkpoint(name)
            assert check["source_canonical_kernel"]==self.ref(rawname)
            checks.append(self.ref(name))
        finalname=stem+"-complete-kernel";value=self.old(finalname)
        if value is None:
            value=self.put(finalname,{"prime":P,"matrix_shape":[m,n],
                "actual_rank":r,"actual_kernel_dimension":n-r,
                "source_rank_profile":profile_ref,"source_selected_unit_inverse":self.ref(invname),
                "source_canonical_kernel":self.ref(rawname),
                "source_all_original_row_checks":checks,"all_original_rows_checked":m,
                "all_original_rows_times_complete_kernel_zero":True,
                "canonical_free_identity_verified":True,"both_selected_inverse_products_verified":True,
                "complete_characteristic_zero_space_certified":True,
                "exact_complete_space_definition":definition,
                "exact_unit_solve_expression":{
                    "source_rank_profile":profile_ref,"source_kernel":self.ref(rawname),
                    "source_actual_unit_minor":self.ref(invname),
                    "rank_upper_bound_plus_unit_minor_gives_exact_rank":True,
                    "all_unselected_characteristic_zero_rows_follow_from_equal_rank":True},
                "arrays_are_only_modular_reductions":True,
                "characteristic_zero_coordinates_reconstructed":False})
            self.checkpoint(finalname)
        assert value["source_all_original_row_checks"]==checks
        return K,value,self.ref(finalname)

    def project_second(self,name,K,kernel_ref,dimension,definition):
        value=self.old(name)
        if value is None:
            self.budget()
            assert K.nrows()==1380 and K.ncols()==dimension
            projected=sub(K,list(range(690,1380)),list(range(dimension)))
            reduced,rank=projected.transpose().rref()
            if rank!=dimension:
                self.put(name+"-unit-failure",{"prime":P,"source_complete_kernel":kernel_ref,
                    "required_rank":dimension,"actual_projected_rank":rank,
                    "original_projection_or_space_disproved":False})
                raise UnitFailure("Second normal V3 projection lacks a unit minor: "+name)
            I=pivots(reduced,rank)
            minor=sub(projected,I,list(range(dimension)));det=int(minor.det())
            invert(det,"Projection unit determinant")
            value=self.put(name,{"prime":P,"source_complete_kernel":kernel_ref,
                "projection_rows":[690,1380],"normal_V3_basis":[list(p) for p in self.V3],
                "normal_V3_basis_mod_prime":rows(projected),"matrix_shape":[690,dimension],
                "actual_projected_rank":dimension,"independent_normal_V3_rows":I,
                "actual_projection_minor_determinant_mod_prime":det,
                "complete_RR_space_certified":True,"exact_RR_space":definition,
                "exact_unit_solve_expression":{
                    "operation":"second_normal_V3_block_of_complete_original_relation_kernel",
                    "source_complete_kernel":kernel_ref,"projection_rows":[690,1380],
                    "nonzero_first_anchor_gives_exact_projection_injectivity":True,
                    "actual_projection_unit_minor":{"rows":I,"determinant_mod_prime":det}},
                "normal_integer_scale_applied_again":False,
                "characteristic_zero_coordinates_reconstructed":False})
            self.checkpoint(name)
        assert value["source_complete_kernel"]==kernel_ref
        shape(value["normal_V3_basis_mod_prime"],690,dimension)
        return matrix(value["normal_V3_basis_mod_prime"]),value,self.ref(name)

    def residual_F_space(self,j,original,marked,marked_ref):
        stem=f"j{j}-two-B"
        finalname=stem+"-complete-residual-space-certificate"
        final=self.old(finalname)
        dimension=RESIDUAL_DIMENSIONS[j-1]
        if final is not None:
            assert final["source_marked_original_pair"]==marked_ref
            projected=self.own(final["complete_residual_normal_V3_space"])
            return matrix(projected["normal_V3_basis_mod_prime"]),projected,final["complete_residual_normal_V3_space"],self.ref(finalname)
        fixed,fixed_refs=self.B_products(f"j{j}-fixed-B0",j,original,marked,marked_ref)
        for trial in range(1,self.B_trials+1):
            trialstem=stem+f"-trial-{trial:06d}"
            pname=trialstem+"-rank"
            oldprofile=self.old(pname)
            if oldprofile is not None and oldprofile["accepted"] is False:
                continue
            other,other_ref=self.B_anchor(j,original,marked,marked_ref,trial)
            right,right_refs=self.B_products(trialstem+"-B1",j,original,other,other_ref)
            M=hcat(fixed,right)
            source_refs={"source_complete_initial_RR":original["reference"],
                         "source_B0":marked_ref,"source_B1":other_ref,
                         "source_B0_products":fixed_refs,"source_B1_products":right_refs,
                         "original_complete_nodes":original["nodes"]}
            definition={"formula":"rank[B0 V3,B1 V3]=690+delta-deg(Z)",
                        "original_delta":DELTAS[j-1],
                        "source_proof":self.item["proofs"]["R896"],"sections_in_same_complete_B_space":True,
                        "full_weight_n_plus_3_injection":len(original["nodes"])>original["n"]+3}
            profile,profile_ref=self.rank_profile(pname,M,690+DELTAS[j-1],source_refs,definition)
            if profile["accepted"] is not True:
                del M,right;gc.collect()
                continue
            K,kcert,kref=self.complete_kernel(trialstem,M,profile,profile_ref,{
                "relation":"B0*r+B1*s=0","weight":original["n"]+3,
                "same_original_complete_B_space":original["Bref"],
                "common_zero_divisor_exactly_original_E":True,
                "complete_relation_dimension":dimension})
            F,projected,projection_ref=self.project_second(trialstem+"-complete-F0-normal-space",
                K,kref,dimension,{"space":"H0(3H-F0)","degree_F0":DELTAS[j-1],
                    "F0":"div_nH(B0)-E","F0_avoids_original_P0":True,
                    "source_marked_original_pair":marked_ref})
            final=self.put(finalname,{"prime":P,"j":j,"ordinary_power":original["n"],
                "accepted_B1_integer_parameter":trial,"source_complete_initial_RR":original["reference"],
                "source_marked_original_pair":marked_ref,"source_B1":other_ref,
                "source_rank_profile":profile_ref,"source_complete_relation_kernel":kref,
                "source_B0_products":fixed_refs,"source_B1_products":right_refs,
                "complete_residual_normal_V3_space":projection_ref,
                "original_complete_nodes":original["nodes"],
                "all_original_product_rows_checked":272*len(original["nodes"]),
                "actual_product_rank":690+DELTAS[j-1],
                "actual_residual_dimension":dimension,"residual_degree":DELTAS[j-1],
                "two_original_B_sections_have_common_zero_exactly_E":True,
                "full_characteristic_zero_residual_space_certified":True,
                "residue_factors_or_multiplicities_removed":False,
                "initial_RR_or_whole_Q_arithmetic_recomputed":False})
            self.checkpoint(finalname)
            del M,right,K;gc.collect()
            return F,projected,projection_ref,self.ref(finalname)
        raise ScopeStop("No two-B unit certificate in the completed finite schedule for j="+str(j))

    def padding_space(self,j,F,Fref,residual_ref):
        k=PADDING[j-1];dimension=RESIDUAL_DIMENSIONS[j-1];stem=f"j{j}-padding"
        name=stem+"-original-jet-matrix";data=self.old(name)
        if data is None:
            self.budget()
            M=sub(self.J3,list(range(k)),list(range(690)))*F
            extra=sub(self.J3,[k],list(range(690)))*F
            data=self.put(name,{"prime":P,"j":j,"source_complete_residual_space":Fref,
                "source_complete_residual_certificate":residual_ref,
                "source_old_normal_V3_jets":self.inputs["normal_V3_point_jets"],
                "matrix_shape":[k,dimension],"matrix_mod_prime":rows(M),
                "next_order":k,"next_order_functional_mod_prime":rows(extra)[0],
                "original_vanishing_orders":list(range(k)),"local_parameter":"z_minus_z0",
                "no_old_point_jet_or_normal_conversion_recomputed":True})
            self.checkpoint(name)
        assert data["source_complete_residual_space"]==Fref
        M=matrix(data["matrix_mod_prime"]);shape(data["matrix_mod_prime"],k,dimension)
        profile,profile_ref=self.rank_profile(stem+"-rank",M,k,
            {"source_original_jet_constraints":self.ref(name)},
            {"source_proof":self.item["proofs"]["R896"],"space":"H0(3H-F0-kP0)",
             "residual_divisor_avoids_P0":True,"degree_after_padding":272,"full_dimension":146})
        if profile["accepted"] is not True:
            raise UnitFailure("The original padding jet matrix has no unit full row minor for j="+str(j))
        U,_,uref=self.complete_kernel(stem,M,profile,profile_ref,{
            "operation":"kernel_of_original_rho_jets_on_complete_H0(3H-F0)",
            "source_complete_residual_space":Fref,"source_exact_jet_constraints":self.ref(name),
            "space":"H0(3H-F0-kP0)","padding_order":k,"degree":272,"dimension":146})
        un=f"j{j}-complete-unscaled-146-normal-space";value=self.old(un)
        if value is None:
            self.budget()
            normal=F*U;extra=matrix([data["next_order_functional_mod_prime"]])*U
            assert sub(self.J3,list(range(k)),list(range(690)))*normal==zero(k,146)
            extra_row=rows(extra)[0]
            first=next((i for i,v in enumerate(extra_row) if v),None)
            if first is None:
                self.put(un+"-unit-failure",{"prime":P,"j":j,"source_padding_kernel":uref,
                    "padding_order":k,"actual_next_order_row_mod_prime":extra_row,
                    "original_line_bundle_or_global_generation_disproved":False})
                raise UnitFailure("No unscaled padding-kernel column has a unit exact-order coefficient.")
            value=self.put(un,{"prime":P,"j":j,"source_complete_residual_space":Fref,
                "source_complete_padding_kernel":uref,"source_original_jet_constraints":self.ref(name),
                "source_old_normal_V3_jets":self.inputs["normal_V3_point_jets"],
                "normal_V3_basis":[list(p) for p in self.V3],
                "normal_V3_basis_mod_prime":rows(normal),"matrix_shape":[690,146],
                "padding_order":k,"actual_next_order_coefficients_mod_prime":extra_row,
                "first_unit_next_order_column":first,
                "all_original_padding_rows_times_full146_kernel_zero":True,
                "complete_characteristic_zero_146_space_certified":True,
                "exact_unit_solve_expression":{
                    "operation":"multiply_exact_complete_residual_basis_by_exact_full_padding_kernel",
                    "source_residual_basis":Fref,"source_padding_kernel":uref,
                    "modular_arrays_not_relabelled_exact_coefficients":True},
                "no_original_basis_column_rescaled":True})
            self.checkpoint(un)
        assert value["source_complete_residual_space"]==Fref
        assert value["source_complete_padding_kernel"]==uref
        shape(value["normal_V3_basis_mod_prime"],690,146)
        return matrix(value["normal_V3_basis_mod_prime"]),value,self.ref(un)

    def V3_anchor(self,j,U,Udata,Uref,trial=None):
        role="v" if trial is None else f"w-trial-{trial:06d}"
        name=f"j{j}-unscaled-{role}"
        value=self.old(name)
        if value is None:
            self.budget()
            if trial is None:
                col=Udata["first_unit_next_order_column"]
                weights=[int(i==col) for i in range(146)]
                definition={"operation":"unchanged_unit_next_order_column","source_complete_U":Uref,"column":col}
            else:
                weights=[pow(trial,i,P) for i in range(146)]
                definition={"operation":"exact_integer_power_combination_of_complete_U",
                            "source_complete_U":Uref,"integer_parameter":trial,"exponents":[0,145]}
            vector=U*matrix([[x] for x in weights])
            leading=sum(x*y for x,y in zip(Udata["actual_next_order_coefficients_mod_prime"],weights))%P
            if trial is None:
                invert(leading,"The retained v coefficient must be a unit.")
            value=self.put(name,{"prime":P,"j":j,"role":"v" if trial is None else "w",
                "trial":trial,"source_complete_146_space":Uref,"kernel_weights_mod_prime":weights,
                "normal_V3_coordinates_mod_prime":[int(vector[i,0]) for i in range(690)],
                "exact_section_definition":definition,"original_scalar_not_rescaled":True,
                "vanishes_to_order_at_least":PADDING[j-1],"actual_coefficient_at_padding_mod_prime":leading,
                "exact_order_equals_padding_certified":trial is None,
                "local_parameter":"z_minus_z0","normal_tau_power":3})
            self.checkpoint(name)
        assert value["source_complete_146_space"]==Uref and value["trial"]==trial
        return value,self.ref(name)

    def complete_bounded_space(self,j,original,U,Udata,Uref,v,vref):
        name=f"j{j}-complete-Dstd-418-certificate"
        final=self.old(name)
        if final is not None:
            assert final["source_exact_v"]==vref and final["source_complete_146_space"]==Uref
            space=self.own(final["complete_normal_V3_space"])
            return space,final["complete_normal_V3_space"],final,self.ref(name)
        fixed,fixed_refs=self.V3_products(f"j{j}-fixed-v",j,original,v,vref)
        for trial in range(1,self.U_trials+1):
            stem=f"j{j}-bounded-pencil-trial-{trial:06d}"
            pname=stem+"-rank";oldprofile=self.old(pname)
            if oldprofile is not None and oldprofile["accepted"] is False:
                continue
            w,wref=self.V3_anchor(j,U,Udata,Uref,trial)
            right,right_refs=self.V3_products(stem+"-w",j,original,w,wref)
            M=hcat(fixed,right)
            assert M.nrows()==1904 and M.ncols()==1380
            source_refs={"source_complete_146_space":Uref,"source_v":vref,"source_w":wref,
                         "source_v_products":fixed_refs,"source_w_products":right_refs,
                         "original_nodes":original["nodes"][:7]}
            profile,pref=self.rank_profile(pname,M,962,source_refs,{
                "source_proof":self.item["proofs"]["R896"],
                "formula":"rank[vV3,wV3]=962-deg(extra_common_zero)",
                "fixed_common_divisor_degree":544,"full_original_V6_injection":True,
                "complete_fibre_length":1904,"degree6H":1632})
            if profile["accepted"] is not True:
                del M,right;gc.collect();continue
            K,kcert,kref=self.complete_kernel(stem,M,profile,pref,{
                "relation":"v*r+w*s=0","common_zero_exactly":"F0+kP0",
                "weight":6,"complete_relation_dimension":418,
                "first_seven_accepted_original_complete_fibres_used":True})
            _,space,sref=self.project_second(stem+"-complete-normal418-space",K,kref,418,{
                "space":"H0(3H-Dstd)","degree_Dstd":272,"Dstd":"div_3H(v)-F0-kP0",
                "Dstd_avoids_original_P0":True,"source_exact_v":vref,
                "source_complete_U":Uref,"same_original_Y_and_tau_frame":True})
            final=self.put(name,{"prime":P,"j":j,"accepted_second_anchor_parameter":trial,
                "source_complete_initial_RR":original["reference"],
                "source_complete_146_space":Uref,"source_exact_v":vref,"source_exact_w":wref,
                "source_rank_profile":pref,"source_complete_relation_kernel":kref,
                "complete_normal_V3_space":sref,"source_v_products":fixed_refs,"source_w_products":right_refs,
                "source_original_nodes":original["nodes"][:7],
                "actual_product_rank":962,"all_original_product_rows_checked":1904,
                "actual_complete_normal_space_dimension":418,
                "two_unscaled_anchors_have_common_zero_exactly_F0_plus_padding_P0":True,
                "Dstd_effective_degree272_and_avoids_original_P0":True,
                "complete_characteristic_zero_H0_3H_minus_Dstd_certified":True,
                "normal_integer_scale_applied_again":False})
            self.checkpoint(name)
            del M,right,K;gc.collect()
            return space,sref,final,self.ref(name)
        raise ScopeStop("No final 962 unit pencil in the completed finite schedule for j="+str(j))

    def principal(self,j,original,marked,marked_ref,residual_ref,Uref,v,vref,space_ref,bounded_ref):
        name=f"j{j}-original-bounded-divisor-and-marked-principal-Q"
        value=self.old(name)
        if value is None:
            self.budget()
            n=POWERS[j-1];degree=POLE_DEGREES[j-1];k=PADDING[j-1]
            b1=int(marked["actual_B0_first_coefficient_mod_prime"])
            vk=int(v["actual_coefficient_at_padding_mod_prime"])
            leadingG=b1*invert(vk,"v exact-order coefficient")%P
            chi_factor=pow(invert(self.uchi_leading,"old chi leading coefficient"),n-2,P)
            leadingQ=leadingG*chi_factor%P
            c_power=pow(self.t_over_rho,degree-1,P)
            leadingt=leadingQ*c_power%P
            assert leadingG and leadingQ and leadingt
            assert 1-k-272*(n-2)==1-degree
            nodes=[
                {"id":"B0","operation":"original_unscaled_marked_section_divided_by_tau_power",
                 "source":marked_ref,"section":"B_coordinates","tau_power":n,
                 "normal_coordinates_already_represent_section_over_tau_power":True},
                {"id":"v","operation":"original_unscaled_section_divided_by_tau_power",
                 "source":vref,"section":"normal_V3_coordinates","tau_power":3,
                 "normal_coordinates_already_represent_section_over_tau_power":True},
                {"id":"G","operation":"divide","numerator":"B0","denominator":"v",
                 "homogeneous_formula":"tau^(3-n)*B0/v","homogeneous_tau_exponent":3-n,
                 "no_second_tau_factor_applied_to_normal_arrays":True},
                {"id":"qchi","operation":"completed_original_function",
                 "source":self.inputs["fixed_chi_anchor"],"source_divisor_identity":self.inputs["fixed_chi_divisor"],
                 "formula":"u_chi/tau^2","normal_tau_power":2},
                {"id":"Q","operation":"multiply","left":"G",
                 "right":{"operation":"integer_power","base":"qchi","exponent":-(n-2)}}]
            value=self.put(name,{"prime":P,"j":j,"original_Hom_word":"1+T^"+str(j),
                "source_complete_initial_RR":original["reference"],
                "source_marked_original_pair":marked_ref,"source_complete_residual_certificate":residual_ref,
                "source_complete_146_space":Uref,"source_exact_v":vref,
                "source_complete_bounded_certificate":bounded_ref,"complete_normal418_space":space_ref,
                "source_original_c0_W_jet":self.inputs["c0_W_jets"][str(j)],
                "source_original_fixed_chi_divisor":self.inputs["fixed_chi_divisor"],
                "source_original_chi_anchor":self.inputs["fixed_chi_anchor"],
                "source_original_t_frame":self.inputs["t_frame"],
                "ordinary_power":n,"original_pole_degree":degree,"P0_pole_multiplicity":1,
                "F0_degree":DELTAS[j-1],"padding_order":k,"Dstd_degree":272,
                "original_E_definition":original["certificate"]["source_original_pole_ideal_nodes"],
                "exact_F0_definition":"div_nH(B0)-E",
                "exact_Dstd_definition":"div_3H(v)-F0-kP0",
                "F0_and_Dstd_avoid_original_P0":True,
                "exact_principal_nodes":nodes,"G_root":"G","Q_root":"Q",
                "exact_G_divisor_identity":"E-deg(E)P0=(Dstd-H)+(n-2)chi+div(G)",
                "exact_Q_divisor_identity":"E-deg(E)P0=(Dstd-H)+(n-2)(Dchi-H)+div(Q)",
                "class_coefficients_Dstd_Dchi":[1,n-2],
                "actual_G_rho_order":1-k,"actual_Q_rho_order":1-degree,
                "actual_Q_t_order":1-degree,
                "actual_B0_first_coefficient_mod_prime":b1,"actual_v_padding_coefficient_mod_prime":vk,
                "actual_G_rho_leading_mod_prime":leadingG,
                "actual_chi_order272_coefficient_mod_prime":self.uchi_leading,
                "actual_Q_rho_leading_mod_prime":leadingQ,
                "actual_original_t_over_rho_mod_prime":self.t_over_rho,
                "actual_original_t_scaling_power":degree-1,"actual_original_c_power_mod_prime":c_power,
                "actual_Q_t_leading_mod_prime":leadingt,
                "exact_marked_leading_expression":{
                    "rho":"B0_first/v_padding * u_chi_272^(-(n-2))",
                    "t":"rho_leading * original_c^(deg(E)-1)",
                    "source_B0":marked_ref,"source_v":vref,
                    "source_u_chi":self.inputs["fixed_chi_anchor"],"source_c":self.inputs["t_frame"]},
                "original_unscaled_constants_and_tau_weight_difference_preserved":True,
                "old_t_jets_or_original_c_recomputed":False,
                "original_fixed_chi_sign_is_negative_power_in_Q":True,
                "exact_principal_and_original_t_leading_defined":True,
                "unit_at_auxiliary_place_not_asserted_at41":True,
                "exact_Galois_transport_contract":{
                    "keep_original_indices_and_integer_combinations":True,
                    "do_not_reselect_anchors_and_relabel_as_conjugates":True,
                    "each_future_residue_place_requires_actual_unit_witnesses":True},
                "characteristic_zero_normal_coefficients_or_frame_values_expanded":False,
                "original_five_Lj128_or_Picard_support_or_height_computed":False})
            self.checkpoint(name)
        assert value["source_marked_original_pair"]==marked_ref and value["source_exact_v"]==vref
        return value,self.ref(name)

    def direction(self,j):
        finalname=f"j{j}-complete-low-weight-RR-certificate"
        final=self.old(finalname)
        if final is not None:
            assert final["complete_original_low_weight_RR_and_marked_principal_certified"] is True
            self.done[str(j)]=self.ref(finalname)
            return final
        original=self.original_direction(j)
        marked,marked_ref=self.mark_original_pair(j,original)
        F,_,Fref,residual_ref=self.residual_F_space(j,original,marked,marked_ref)
        U,Udata,Uref=self.padding_space(j,F,Fref,residual_ref)
        v,vref=self.V3_anchor(j,U,Udata,Uref)
        space,sref,bounded,bounded_ref=self.complete_bounded_space(j,original,U,Udata,Uref,v,vref)
        principal,pref=self.principal(j,original,marked,marked_ref,residual_ref,Uref,v,vref,sref,bounded_ref)
        final=self.put(finalname,{"prime":P,"j":j,"original_Hom_word":"1+T^"+str(j),
            "source_complete_initial_RR":original["reference"],
            "source_marked_original_pair":marked_ref,
            "source_complete_two_B_residual_certificate":residual_ref,
            "complete_residual_normal_V3_space":Fref,"complete_padding146_space":Uref,
            "source_unscaled_exact_v":vref,"source_complete_Dstd_certificate":bounded_ref,
            "complete_normal418_space":sref,"marked_principal_Q":pref,
            "ordinary_power":POWERS[j-1],"original_pole_degree":POLE_DEGREES[j-1],
            "residual_degree":DELTAS[j-1],"residual_dimension":RESIDUAL_DIMENSIONS[j-1],
            "padding_order":PADDING[j-1],"complete_padding_dimension":146,
            "complete_bounded_space_dimension":418,"Dstd_degree":272,
            "original_complete_fibres_reused":original["nodes"],
            "full_original_low_weight_products_and_kernel_rows_verified":True,
            "F0_and_Dstd_avoid_original_P0":True,
            "complete_original_low_weight_RR_and_marked_principal_certified":True,
            "correct_original_tau_weight_and_chi_sign_preserved":True,
            "original_t_frame_and_unscaled_constants_preserved":True,
            "true_characteristic_zero_unit_solve_expressions":True,
            "actual_arrays_are_only_modular_reductions":True,
            "characteristic_zero_coordinates_reconstructed":False,
            "initial_RR_Schur_whole_Q_or_old_jets_recomputed":False,
            "original_Lj128_Picard_support_or_height_computed":False})
        self.done[str(j)]=self.ref(finalname);self.checkpoint(finalname)
        del F,U;self.original_directions={};gc.collect()
        return final

    def inventory(self):
        files=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name==PREFIX+"current.json.gz" or path.name.startswith(PREFIX+"stage-manifest-"):
                continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
            files.append(spec(path))
        digest=fingerprint(files)
        name="stage-manifest-"+fingerprint({"files":files,"current":self.current})
        value={"files":files,"file_count":len(files),"files_sha256":digest,
               "current_checkpoints":[self.current] if self.current is not None else [],
               "only_complete_atomic_new_mathematical_stages_listed":True,
               "old_source_stages_remain_in_their_original_source_directories":True}
        self.put(name,value)
        return self.ref(name)

    def finish(self,complete,reason):
        for j in range(1,6):
            value=self.old(f"j{j}-complete-low-weight-RR-certificate")
            if value is not None:
                assert value["complete_original_low_weight_RR_and_marked_principal_certified"] is True
                self.done[str(j)]=self.ref(f"j{j}-complete-low-weight-RR-certificate")
        assert not complete or all(str(j) in self.done for j in self.requested)
        current=self.checkpoint(self.phase)
        final={"result":RESULT,"configuration":self.tag,"complete":bool(complete),"p":41,"prime":P,
            "source_audit":self.refs.get("original-source-audit"),
            "requested_directions":self.requested,"completed_directions":sorted(map(int,self.done)),
            "complete_direction_certificates":self.done,
            "all_five_complete_low_weight_RR_spaces_certified":len(self.done)==5,
            "requested_low_weight_RR_spaces_certified":all(str(j) in self.done for j in self.requested),
            "original_Hom_words":STRATEGY["original_Hom_words"],"original_pole_degrees":POLE_DEGREES,
            "initial_powers":POWERS,"residual_degrees":DELTAS,"residual_dimensions":RESIDUAL_DIMENSIONS,
            "padding_orders":PADDING,"complete_padding_dimension":146,"complete_bounded_dimension":418,
            "original_tau_weight_and_negative_chi_power_retained":True,
            "source_original_t_frame":self.inputs.get("t_frame"),
            "old_initial_RR_Schur_whole_Q_Krylov_inverses_and_jets_recomputed":False,
            "characteristic_zero_coefficients_reconstructed":False,
            "original_Lj128_Hecke_Picard_support_connection_period_or_height_computed":False,
            "stage_manifest":self.inventory(),"resume_state":current,
            "scope_stop_reason":reason,"seconds":time.monotonic()-self.started}
        save(self.out/FINAL,final)
        print("R896_FINAL_SUMMARY="+json.dumps({k:final[k] for k in (
            "complete","completed_directions","all_five_complete_low_weight_RR_spaces_certified",
            "residual_dimensions","padding_orders","scope_stop_reason","seconds")}),flush=True)
        return final

    def run(self):
        existing=self.out/FINAL
        if existing.exists():
            old=read(existing)
            assert old["result"]==RESULT and old["configuration"]==self.tag
            if old["complete"] is True:
                inventory=self.own(old["stage_manifest"])
                for row in inventory["files"]:
                    assert spec(self.out/row["file"])==plain(row)
                if all(str(j) in old["complete_direction_certificates"] for j in self.requested):
                    self.done=old["complete_direction_certificates"]
                    return old
        self.prepare()
        for j in self.requested:
            self.direction(j)
        return self.finish(True,None)

def main():
    guard()
    if hasattr(sys,"set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    parser.add_argument("--config",required=True);parser.add_argument("--retained",required=True)
    parser.add_argument("--output",required=True);parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args();assert 1<=args.budget_minutes<=300
    started=time.monotonic();job=None;code=1;error=None;trace=None;certificate=None
    try:
        job=Job(args);certificate=job.run();code=0
    except BudgetStop as exc:
        code=124;error=str(exc)
        if job is not None:
            certificate=job.finish(False,error)
    except (ScopeStop,UnitFailure) as exc:
        code=2;error=str(exc)
        if job is not None:
            certificate=job.finish(False,error)
    except Exception as exc:
        code=1;error=type(exc).__name__+": "+str(exc);trace=traceback.format_exc();print(trace,flush=True)
        if job is not None:
            try:
                certificate=job.finish(False,error)
            except Exception:
                traceback.print_exc()
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True);final=out/FINAL
    receipt={"result":RESULT,"source_sha256":sha(__file__),"complete":code==0,"exit_code":code,
        "configuration":job.tag if job is not None else None,
        "configuration_sha256":fingerprint(job.tag) if job is not None else None,
        "certificate_sha256":sha(final) if certificate is not None and final.exists() else None,
        "completed_directions":sorted(map(int,job.done)) if job is not None else [],
        "error":error,"traceback":trace,"seconds":time.monotonic()-started}
    save(out/"core-receipt.json",receipt)
    print("R896_CORE_RECEIPT="+json.dumps(receipt,sort_keys=True),flush=True)
    raise SystemExit(code)

if __name__=="__main__":
    main()
