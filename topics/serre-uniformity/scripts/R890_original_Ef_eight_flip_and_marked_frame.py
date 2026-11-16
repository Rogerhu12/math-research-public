#!/usr/bin/env python3
"""R890: eight complete original bounded flips and the marked t-leading term."""
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
RESULT="R890-original-Ef-eight-flip-and-marked-frame"
FINAL="p41-original-Ef-eight-flip-and-marked-frame-certificate.json"
PREFIX="R890-"
MANIFEST="full-outputs-manifest.json"
P=1000000753
N=272
EPS=[0]+[1]*144+[2]*127
GROUPS=("R887","R880","R872","R883","R827")
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
CHAIN=(("A","D","D"),("B","A","H"),("C","B","D"),
       ("D2","X","X"),("E","D2","D2"),("F","Cstar","C"),
       ("G","F","E"),("DE","G","H"))
STRATEGY={
    "original_curve":"original genus127 Y, level82 and minus3 descent",
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "original_integral_B_root":3197390,"original_free_direction":1186,
    "normal_basis_degrees":EPS,"normal_V3_dimension":690,"complete_divisor_space_dimension":418,
    "old_fibres":[0,1,2,3,4,5,6],"complete_evaluation_length":1904,
    "degree6H":1632,"original_W_and_Krylov_inverses_recomputed":False,
    "product_image_dimension":962,"product_anchor_schedule":"original first-input kernel columns, in order",
    "product_rank_extension":"new residual Schur block, old selected span and inverse reused",
    "membership_anchors":["tau^3","sigma^3"],"full_membership_matrix_shape":[1884,690],
    "complete_U_dimension":146,"U_unit_selection":"first nonzero original P0 evaluation, no rescaling",
    "pencil_second_anchor":"sum(n^j*U_j), j0..145, positive integer n",
    "complete_pencil_matrix_shape":[1904,1380],"complete_relation_kernel_dimension":418,
    "projection":"second690 rows of complete kernel of [uV3,vV3]",
    "neutral_divisor":"div_H(tau), represented by tau V2 in original normal V3",
    "chain":[list(row) for row in CHAIN],
    "principal_recurrence":"Fnew=1/(q*Fa*Fb), q=u/tau^3",
    "target_class_coefficients_Cstar_Dstar_Dchi":[-1,3,4],
    "target_identity":"Ef-1206P0=(DE-H)+div(Qtilde*F_DE)",
    "original_rho_order":-1205,"original_t_leading":"rho_leading * original_c^1205",
    "old_three418_spaces_point_jets_or_t_c_recomputed":False,
    "characteristic_zero_arrays_expanded":False,"other_six_branches_or_five_Lj_computed":False,
    "only_budget_finite_search_limits_and_transport_excluded_from_identity":True}

class BudgetStop(RuntimeError):
    pass
class UnitFailure(RuntimeError):
    pass
class SearchStop(RuntimeError):
    pass

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
    temporary=path.with_name(path.name+".tmp")
    raw=(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n").encode()
    if path.suffix==".gz":
        with temporary.open("wb") as f:
            with gzip.GzipFile(filename="",fileobj=f,mode="wb",mtime=0,compresslevel=2) as z:
                z.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)
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
    answer={**{k:source[k] for k in BASE},"configuration_sha256":source["configuration_sha256"],
            "selected_files_sha256":fingerprint(source["files"])}
    if source.get("certificate") is not None:
        answer["certificate"]=plain(source["certificate"])
    else:
        answer["configuration_stage"]=plain(source["configuration_stage"])
    return answer
def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
            "method_sha256":item["method_sha256"],"proofs":item["proofs"],
            "sources":{g:identity(item["sources"][g]) for g in GROUPS},
            "inputs":item["inputs"],"strategy":STRATEGY}
def shape(raw,m,n):
    assert len(raw)==m and all(len(row)==n for row in raw),(m,n)
def rows(A):
    return [[int(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())]
def mat(raw):
    return nmod_mat(raw,P)
def zero(m,n):
    return nmod_mat(m,n,P)
def eye(n):
    return mat([[int(i==j) for j in range(n)] for i in range(n)])
def sub(A,I,J):
    return mat([[int(A[i,j]) for j in J] for i in I])
def pivots(A,rank):
    answer=[next(j for j in range(A.ncols()) if A[i,j]) for i in range(rank)]
    assert answer==sorted(set(answer))
    return answer
def hcat(A,B):
    assert A.nrows()==B.nrows()
    return mat([[int(A[i,j]) for j in range(A.ncols())]+
                [int(B[i,j]) for j in range(B.ncols())] for i in range(A.nrows())])
def positions(power):
    return [(i,k) for i in range(N) for k in range(max(0,power-EPS[i]+1))]
def same_source(left,right):
    assert all(str(left[k])==str(right[k]) for k in BASE)
    if left.get("configuration_sha256") is not None:
        assert left["configuration_sha256"]==right["configuration_sha256"]

class Source:
    def __init__(self,label,item,root):
        self.label=label;self.item=item;self.folder=Path(root)/label;self.checked=set()
        self.files={name:plain(row) for name,row in item["files"].items()}
        manifest_path=self.folder/MANIFEST
        assert sha(manifest_path)==item["manifest_sha256"]
        manifest=read(manifest_path);assert manifest["result"]==item["result"]
        entries={row["file"]:plain(row) for row in manifest["files"]}
        assert len(entries)==len(manifest["files"])
        entries[MANIFEST]=spec(manifest_path)
        for name,row in self.files.items():
            assert name==row["file"]
            if name!="full-outputs-manifest-reference.json":
                assert entries[name]==row,(label,name)
        initial=self.get("public-actions-input.json");run=self.get("run-receipt.json")
        assert initial["source_commit"]==run["source_commit"]==item["source_commit"]
        assert str(run["workflow_run_id"])==str(item["run_id"])
        core_sha=initial.get("core_sha256",initial.get("job",{}).get("core_sha256"))
        assert core_sha==item["core_sha256"]
        self.certificate=None
        if item.get("certificate") is not None:
            self.certificate=self.get(item["certificate"]["file"])
            assert self.certificate["result"]==item["result"] and self.certificate["complete"] is True
            assert self.files[item["certificate"]["file"]]==plain(item["certificate"])
            assert run["complete"] is True and run["process_exit_code"]==0
            self.tag=self.certificate["configuration"]
        else:
            assert label=="R827" and run["complete"] is False and run["process_exit_code"]==124
            anchor=self.get(item["configuration_stage"]["file"])
            assert anchor["complete"] is True
            self.tag=anchor["configuration"]
        assert fingerprint(self.tag)==item["configuration_sha256"]
        assert self.tag.get("source_sha256",self.tag.get("core_sha256"))==item["core_sha256"]
        if run.get("core_receipt_sha256") is not None:
            assert run["core_receipt_sha256"]==self.files["core-receipt.json"]["sha256"]
            core=self.get("core-receipt.json")
            assert core["source_sha256"]==item["core_sha256"]
            if core.get("configuration") is not None:
                assert core["configuration"]==self.tag
            if core.get("configuration_sha256") is not None:
                assert core["configuration_sha256"]==item["configuration_sha256"]
            if self.certificate is not None:
                assert core["complete"] is True
                assert core["certificate_sha256"]==item["certificate"]["sha256"]
    def get(self,name):
        path=self.folder/name
        if name not in self.checked:
            assert spec(path)==self.files[name],(self.label,name)
            self.checked.add(name)
        return read(path)
    def stage(self,row):
        assert self.files[row["file"]]==plain(row)
        value=self.get(row["file"])
        assert value["complete"] is True and value["configuration"]==self.tag
        return value

class Job:
    def __init__(self,args):
        self.args=args;self.started=time.monotonic();self.out=Path(args.output)
        self.out.mkdir(parents=True,exist_ok=True);self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41
        assert self.item["producer_inputs_pending"] is False
        assert sha(__file__)==self.item["core_sha256"] and flint.__version__=="0.9.0"
        topic=Path(__file__).resolve().parent.parent
        assert sha(topic/self.item["method"])==self.item["method_sha256"]
        for proof in self.item["proofs"].values():
            assert sha(topic/proof["path"])==proof["sha256"]
        assert set(self.item["sources"])==set(GROUPS)
        self.tag=expected_tag(self.item);self.refs={};self.flip_refs=[];self.current=None
        self.sources={g:Source(g,self.item["sources"][g],args.retained) for g in GROUPS}
        self.inputs=self.item["inputs"];self.spaces={};self.space_cache={};self.fibres={}
        self.phase="source-initialization"
    def budget(self):
        if time.monotonic()-self.started>=self.args.budget_minutes*60-30:
            raise BudgetStop("R890 complete atomic stages retained; phase="+self.phase)
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
    def put(self,name,value):
        assert not any(k in value for k in ("result","configuration","complete"))
        payload={"result":RESULT,"configuration":self.tag,"complete":True,**value}
        path=self.path(name)
        if path.exists():
            assert read(path)==payload
        else:
            save(path,payload)
        self.refs[name]=spec(path)
        print("R890_STAGE="+json.dumps({"file":path.name,"seconds":time.monotonic()-self.started}),flush=True)
        return payload
    def checkpoint(self,phase):
        self.phase=phase
        value={"result":RESULT,"configuration":self.tag,"complete":False,
               "phase":phase,"completed_stages":self.refs,"complete_flip_certificates":self.flip_refs}
        save(self.path("current"),value);self.current=spec(self.path("current"))
    def source(self,key):
        row=self.inputs[key]
        return self.sources[row["source_group"]].stage(row)
    def own(self,row):
        path=self.out/row["file"];assert spec(path)==plain(row)
        value=read(path)
        assert value["configuration"]==self.tag and value["complete"] is True
        return value

    def prepare(self):
        self.V3=positions(3);self.V2=positions(2)
        assert len(self.V3)==690 and len(self.V2)==418
        self.Cstar=self.source("Cstar");self.Dstar=self.source("Dstar");self.Dchi=self.source("Dchi")
        self.point_jets=self.source("point_jets");self.point=self.source("point_linear_functional")
        self.Qtilde=self.source("Qtilde");self.frame=self.source("t_frame")
        self.W=self.source("original_W");self.grid=self.source("original_grid");self.place=self.source("original_place")
        assert self.W["prime"]==self.place["prime"]==P and self.place["original_zeta_root"]==549966761
        assert self.grid["points"][:7]==list(range(7)) and len(self.grid["points"])==8
        assert self.grid["all_eight_actual_determinants_nonzero"] is True
        assert len(self.inputs["original_Krylov_points"])==7
        self.points={}
        for z,row in enumerate(self.inputs["original_Krylov_points"]):
            assert plain(row)==plain(self.grid["Krylov_point_stages"][z])
            point=self.sources["R827"].stage(row)
            assert point["z0"]==z and point["prime"]==P and point["usable"] is True
            assert point["actual_cyclic_rank"]==272 and point["both_inverse_products_verified"] is True
            assert plain(point["source_original_W"])==plain(self.inputs["original_W"])
            shape(point["W_evaluated_mod_prime"],272,272)
            shape(point["inverse_Krylov_matrix_mod_prime"],272,272)
            self.points[z]=point
        assert self.point["chosen_local_parameter"]=="z_minus_z0"
        self.zP0=int(self.point["z0_mod_prime"])
        assert self.zP0==110702704 and self.point["w0_mod_prime"]==645975656
        self.betaP0=self.point["point_evaluation_mod_prime"]
        assert len(self.betaP0)==272 and self.betaP0[0]==1
        assert self.point_jets["matrix_shape"]==[273,418]
        assert self.point_jets["V2_basis"]==[
            {"normal_basis_row":i,"power_of_z":k} for i,k in self.V2]
        assert self.Qtilde["all_three_effective_degree272_representatives_avoid_original_P0"] is True
        assert self.Qtilde["complete_Cstar_418_certified"] is True
        assert self.Qtilde["original_Qtilde_order_minus1205_certified"] is True
        assert self.Qtilde["actual_rho_order"]==-1205 and self.Qtilde["actual_local_parameter"]=="z_minus_z0"
        for field,key in (("source_complete_Cstar_418","Cstar"),
                          ("source_complete_original_Dstar_418","Dstar"),
                          ("source_complete_original_Dchi_418","Dchi")):
            assert plain(self.Qtilde[field])==plain(self.inputs[key])
        assert self.frame["original_t_first_order_unit_certified"] is True
        assert self.frame["original_s_root"]==99932770
        assert self.frame["original_t_over_rho_constant_mod_prime"]==354813668
        assert self.frame["actual_c_powers_mod_prime"]["1205"]==201313487
        assert self.frame["quotient_all_three_coefficients_multiplied_back"] is True
        assert self.frame["exact_zero_not_inferred_from_modular_zero"] is True
        source_spaces=(("Cstar","Cstar",self.Cstar,"normal_V3_basis_mod_prime",[1,0,0]),
                       ("D","Dstar",self.Dstar,"normal_V3_basis_mod_prime",[0,1,0]),
                       ("X","Dchi",self.Dchi,"V3_kernel_basis_mod_prime",[0,0,1]))
        for name,key,value,column_key,kappa in source_spaces:
            assert value["prime"]==P
            raw=value[column_key];shape(raw,690,418)
            if key!="Dchi":
                assert value["complete_RR_space_certified"] is True
                assert value["actual_projected_rank"]==418 and value["accepted"] is True
            else:
                assert value["full_characteristic_zero_dimension"]==418
                assert value["all1234_by418_complete_V5_relations_zero"] is True
                assert value["normal_integer_scale_applied_again"] is False
            self.spaces[name]={"matrix":mat(raw),"reference":self.inputs[key],
                               "kappa":kappa,"Fvalue":1,
                               "function":{"operation":"one_for_initial_representative","space":self.inputs[key]}}
        name="neutral-H-and-original-P0-functional"
        old=self.old(name)
        if old is None:
            self.budget()
            lookup={pair:j for j,pair in enumerate(self.V3)}
            raw=[[0]*418 for _ in range(690)]
            for j,pair in enumerate(self.V2):
                raw[lookup[pair]][j]=1
            functional=[int(self.betaP0[i])*pow(self.zP0,k,P)%P for i,k in self.V3]
            old=self.put(name,{
                "prime":P,"normal_V3_basis":[list(x) for x in self.V3],
                "source_original_point":self.inputs["point_linear_functional"],
                "source_original_V2_jets":self.inputs["point_jets"],
                "neutral_W_H_normal_V3_basis_mod_prime":raw,
                "normal_V3_P0_functional_mod_prime":functional,
                "neutral_effective_divisor":"div_H(original tau)","neutral_degree":272,
                "neutral_avoids_original_P0":True,"tau_V2_is_complete_W_H":True,
                "old_Hensel_jets_or_old_normal_conversion_recomputed":False,
                "exact_P0_functional":"sum c_(i,k)*z(P0)^k*beta_i(P0) in original tau frame"})
        self.point_row=mat([old["normal_V3_P0_functional_mod_prime"]])
        self.spaces["H"]={"matrix":mat(old["neutral_W_H_normal_V3_basis_mod_prime"]),
                          "reference":self.refs[name],"kappa":[0,0,0],"Fvalue":1,
                          "function":{"operation":"one_for_neutral_tau_divisor","source":self.refs[name]}}
        audit="original-source-audit"
        if self.old(audit) is None:
            self.put(audit,{
                "sources":{g:identity(self.item["sources"][g]) for g in GROUPS},"inputs":self.inputs,
                "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
                "original_integral_B_root":3197390,"normal_basis_degrees":EPS,
                "Cstar_Dstar_and_Dchi_complete_normal418_inputs":True,
                "old_original_W_Krylov_inverses_and_jets_not_recomputed":True,
                "original_t_first_order_and_powers_consumed_without_recomputation":True,
                "original_characteristic_zero_unit_solve_definitions_retained":True,
                "all_new_mathematics_only_in_public_Actions":True})
        self.checkpoint("complete-original-sources")
        self.normal_fibres()

    def normal_fibres(self):
        for z in range(7):
            name=f"normal-V3-fibre-{z}"
            value=self.old(name)
            if value is None:
                self.budget()
                E=[[0]*690 for _ in range(272)]
                inverse=self.points[z]["inverse_Krylov_matrix_mod_prime"]
                cyclic=[[0]*690 for _ in range(272)]
                for j,(i,k) in enumerate(self.V3):
                    power=pow(z,k,P);E[i][j]=power
                    for row in range(272):
                        cyclic[row][j]=int(inverse[row][i])*power%P
                value=self.put(name,{
                    "prime":P,"z0":z,"normal_V3_basis":[list(x) for x in self.V3],
                    "source_original_Krylov_point":self.inputs["original_Krylov_points"][z],
                    "source_original_W":self.inputs["original_W"],
                    "normal_evaluation_mod_prime":E,"cyclic_evaluation_mod_prime":cyclic,
                    "normal_evaluation_shape":[272,690],
                    "cyclic_formula":"old_K_inverse * original_normal_V3_evaluation",
                    "old_W_K_or_Kinverse_recomputed":False,
                    "normal_integer_scale_applied_again":False})
            assert value["source_original_Krylov_point"]==self.inputs["original_Krylov_points"][z]
            self.fibres[z]={"E":mat(value["normal_evaluation_mod_prime"]),
                            "C":mat(value["cyclic_evaluation_mod_prime"]),
                            "W":mat(self.points[z]["W_evaluated_mod_prime"]),
                            "reference":self.refs[name]}
            self.checkpoint(name)

    def space_fibre(self,label,z):
        key=(label,z)
        if key in self.space_cache:
            return self.space_cache[key]
        space=self.spaces[label];name=f"space-{label}-fibre-{z}"
        value=self.old(name)
        if value is None:
            self.budget()
            fibre=self.fibres[z]
            E=fibre["E"]*space["matrix"]
            C=fibre["C"]*space["matrix"]
            value=self.put(name,{
                "prime":P,"space":label,"z0":z,"source_complete_normal418_space":space["reference"],
                "source_complete_normal_V3_fibre":fibre["reference"],
                "normal_evaluation_mod_prime":rows(E),"cyclic_evaluation_mod_prime":rows(C),
                "evaluation_shape":[272,418],"all418_original_columns_evaluated":True,
                "old_K_inverse_or_completed_space_recomputed":False})
        assert value["source_complete_normal418_space"]==space["reference"]
        answer=(mat(value["normal_evaluation_mod_prime"]),mat(value["cyclic_evaluation_mod_prime"]),self.refs[name])
        self.space_cache[key]=answer
        return answer

    def anchor(self,name,coordinates,definition):
        value=self.old(name)
        if value is None:
            assert len(coordinates)==690
            value=self.put(name,{"prime":P,"normal_V3_coordinates_mod_prime":coordinates,
                "exact_anchor_definition":definition,"original_scalar_not_rescaled":True})
        assert value["exact_anchor_definition"]==definition
        return value,self.refs[name]

    def product_fibres(self,prefix,anchor,anchor_ref,other):
        data=[];refs=[]
        for z in range(7):
            name=prefix+f"-fibre-{z}"
            value=self.old(name)
            if other=="V3":
                CE=self.fibres[z]["C"];other_ref=self.fibres[z]["reference"];width=690
            else:
                _,CE,other_ref=self.space_fibre(other,z);width=418
            if value is None:
                self.budget()
                fibre=self.fibres[z]
                coordinate=mat([[x] for x in anchor["normal_V3_coordinates_mod_prime"]])
                vector=fibre["E"]*coordinate
                current=vector;columns=[]
                for j in range(272):
                    columns.append([int(current[i,0]) for i in range(272)])
                    if j<271:
                        current=fibre["W"]*current
                product=mat(columns).transpose()*CE
                value=self.put(name,{
                    "prime":P,"z0":z,"source_anchor":anchor_ref,"other_complete_space":other_ref,
                    "source_original_Krylov_point":self.inputs["original_Krylov_points"][z],
                    "matrix_shape":[272,width],"product_evaluation_mod_prime":rows(product),
                    "section_evaluation_mod_prime":rows(vector),
                    "formula":"[v,Wv,...,W^271v] * (old_Kinverse * other_space)",
                    "all_original_complete_fibre_coordinates_retained":True,
                    "old_W_or_Kinverse_recomputed":False})
            assert value["source_anchor"]==anchor_ref and value["other_complete_space"]==other_ref
            raw=value["product_evaluation_mod_prime"];shape(raw,272,width)
            data.extend(raw);refs.append(self.refs[name]);self.checkpoint(name)
        return mat(data),refs

    def rank_profile(self,name,M,rank,source_refs):
        value=self.old(name)
        if value is None:
            self.budget()
            reduced,actual=M.rref()
            assert actual<=rank,("geometric_rank_upper_bound",name,actual,rank)
            value={"prime":P,"matrix_shape":[M.nrows(),M.ncols()],
                   "required_rank":rank,"actual_rank":actual,"accepted":actual==rank,
                   "source_references":source_refs,"geometric_characteristic_zero_rank_upper_bound":rank}
            if actual==rank:
                J=pivots(reduced,actual);selected=sub(M,list(range(M.nrows())),J)
                tr,actual2=selected.transpose().rref();assert actual2==rank
                I=pivots(tr,actual2)
                value.update({"selected_columns":J,"selected_rows":I,
                              "unit_minor_lower_bound_certifies_exact_rank":True})
            value=self.put(name,value)
        assert value["source_references"]==source_refs
        return value

    def complete_kernel(self,name,M,profile,profile_ref,definition):
        value=self.old(name)
        r=profile["required_rank"];n=M.ncols();m=M.nrows()
        assert profile["accepted"] is True and profile["actual_rank"]==r
        if value is None:
            self.budget()
            I,J=profile["selected_rows"],profile["selected_columns"]
            free=[j for j in range(n) if j not in set(J)]
            A=sub(M,I,J);inverse=A.inv()
            assert A*inverse==eye(r) and inverse*A==eye(r)
            coordinates=-(inverse*sub(M,I,free))
            raw=[[0]*len(free) for _ in range(n)]
            for column,j in enumerate(free):
                raw[j][column]=1
                for k,pivot in enumerate(J):
                    raw[pivot][column]=int(coordinates[k,column])
            K=mat(raw)
            assert M*K==zero(m,len(free))
            value=self.put(name,{
                "prime":P,"source_rank_profile":profile_ref,"matrix_shape":[m,n],
                "actual_rank":r,"actual_kernel_dimension":len(free),
                "selected_rows":I,"selected_columns":J,"free_columns":free,
                "inverse_selected_minor_mod_prime":rows(inverse),"kernel_basis_mod_prime":raw,
                "both_selected_inverse_products_verified":True,
                "all_original_matrix_rows_times_complete_kernel_zero":True,
                "free_normalization_identity_verified":True,
                "exact_complete_space_definition":definition,
                "exact_unit_solve_expression":{
                    "operation":"kernel_of_complete_original_source_matrix",
                    "source_rank_profile":profile_ref,"selected_rows":I,"selected_columns":J,
                    "free_columns":free,"pivot_formula":"-inverse(selected_minor)*selected_free_columns",
                    "geometric_rank_upper_bound_and_actual_unit_minor_retained":True},
                "characteristic_zero_coefficients_reconstructed":False})
        assert value["source_rank_profile"]==profile_ref
        return mat(value["kernel_basis_mod_prime"]),self.refs[name]

    def rebuild_span(self,state):
        raw=[[] for _ in range(1904)]
        for block in state["selected_blocks"]:
            offset=0
            for ref in block["source_fibre_products"]:
                value=self.own(ref);part=value["product_evaluation_mod_prime"]
                shape(part,272,418)
                for row in part:
                    raw[offset].extend(row[j] for j in block["selected_columns"])
                    offset+=1
            assert offset==1904
        shape(raw,1904,state["actual_rank"])
        return mat(raw)

    def span_inverse(self,state):
        if "inverse_selected_minor_mod_prime" in state:
            return mat(state["inverse_selected_minor_mod_prime"])
        return self.span_inverse(self.own(state["same_inverse_as"]))

    def product_span(self,stem,left,right):
        final_name=stem+"-complete-product-image-962"
        final=self.old(final_name)
        if final is not None:
            state=self.own(final["selected_span_state"])
            assert final["left_space"]==self.spaces[left]["reference"]
            assert final["right_space"]==self.spaces[right]["reference"]
            assert state["actual_rank"]==962
            return self.rebuild_span(state),self.span_inverse(state),state["selected_rows"],self.refs[final_name]
        state=None;state_ref=None;basis=None;inverse=None
        for ordinal in range(self.item["maximum_product_anchors"]):
            assert ordinal<418
            name=stem+f"-product-anchor-{ordinal:03d}"
            coordinates=[int(self.spaces[left]["matrix"][i,ordinal]) for i in range(690)]
            anchor,anchor_ref=self.anchor(name,coordinates,{
                "operation":"unchanged_original_kernel_column",
                "source_complete_space":self.spaces[left]["reference"],"column":ordinal})
            B,products=self.product_fibres(name+"-times-"+right,anchor,anchor_ref,right)
            state_name=stem+f"-product-span-after-{ordinal:03d}"
            old=self.old(state_name)
            if old is not None:
                assert old["previous_span_state"]==state_ref and old["new_product_sources"]==products
                state=old;state_ref=self.refs[state_name]
                basis=self.rebuild_span(state);inverse=self.span_inverse(state)
            else:
                oldrank=0 if state is None else state["actual_rank"]
                I=[] if state is None else state["selected_rows"]
                source_refs={"previous_span_state":state_ref,"new_product_sources":products,
                             "left_complete_space":self.spaces[left]["reference"],
                             "right_complete_space":self.spaces[right]["reference"]}
                residual_name=state_name+"-new-residual"
                residual=self.old(residual_name)
                if residual is None:
                    self.budget()
                    T=B if oldrank==0 else B-basis*(inverse*sub(B,I,list(range(418))))
                    if oldrank:
                        assert sub(T,I,list(range(418)))==zero(oldrank,418)
                    residual=self.put(residual_name,{
                        "prime":P,"source_references":source_refs,"matrix_shape":[1904,418],
                        "residual_mod_prime":rows(T),"old_span_selected_rows_zero":True,
                        "old_span_or_old_inverse_recomputed":False})
                else:
                    assert residual["source_references"]==source_refs
                    T=mat(residual["residual_mod_prime"])
                profile_name=state_name+"-new-rank-profile"
                profile=self.old(profile_name)
                if profile is None:
                    self.budget()
                    reduced,added=T.rref()
                    assert oldrank+added<=962,("complete_product_geometric_bound",oldrank,added)
                    J=pivots(reduced,added)
                    if added:
                        TJ=sub(T,list(range(1904)),J)
                        tr,rr=TJ.transpose().rref();assert rr==added
                        added_rows=pivots(tr,rr)
                        assert not(set(I)&set(added_rows))
                    else:
                        added_rows=[]
                    profile=self.put(profile_name,{
                        "prime":P,"source_new_residual":self.refs[residual_name],
                        "old_rank":oldrank,"added_rank":added,"actual_rank":oldrank+added,
                        "new_selected_columns":J,"new_selected_rows":added_rows,
                        "old_selected_span_reduced_again":False,
                        "geometric_rank_upper_bound":962})
                assert profile["source_new_residual"]==self.refs[residual_name]
                added=profile["added_rank"];J=profile["new_selected_columns"]
                additional=profile["new_selected_rows"]
                selected=[] if state is None else state["selected_blocks"]
                if added:
                    self.budget()
                    S=sub(T,additional,J);Sinv=S.inv()
                    assert S*Sinv==eye(added) and Sinv*S==eye(added)
                    new_columns=sub(B,list(range(1904)),J)
                    if oldrank:
                        upper=inverse*sub(B,I,J)
                        lower=sub(basis,additional,list(range(oldrank)))*inverse
                        top=hcat(inverse+upper*Sinv*lower,-(upper*Sinv))
                        bottom=hcat(-(Sinv*lower),Sinv)
                        next_inverse=mat(rows(top)+rows(bottom))
                        next_basis=hcat(basis,new_columns)
                    else:
                        next_inverse=Sinv;next_basis=new_columns
                    next_rows=I+additional
                    A=sub(next_basis,next_rows,list(range(oldrank+added)))
                    assert A*next_inverse==eye(oldrank+added)
                    assert next_inverse*A==eye(oldrank+added)
                    selected=selected+[{"source_fibre_products":products,"selected_columns":J}]
                    answer={"inverse_selected_minor_mod_prime":rows(next_inverse),
                            "new_Schur_inverse_mod_prime":rows(Sinv),
                            "both_new_Schur_inverse_products_verified":True,
                            "both_complete_selected_inverse_products_verified":True}
                    basis=next_basis;inverse=next_inverse
                else:
                    assert state is not None
                    next_rows=I
                    answer={"same_inverse_as":state_ref,
                            "zero_new_residual_rank_certified":True}
                state=self.put(state_name,{
                    "prime":P,"previous_span_state":state_ref,"new_product_sources":products,
                    "new_residual":self.refs[residual_name],"new_rank_profile":self.refs[profile_name],
                    "actual_rank":oldrank+added,"added_rank":added,"selected_rows":next_rows,
                    "selected_blocks":selected,"old_span_inverse_recomputed":False,**answer})
                state_ref=self.refs[state_name]
            self.checkpoint(state_name)
            if state["actual_rank"]==962:
                final=self.put(final_name,{
                    "prime":P,"left_space":self.spaces[left]["reference"],
                    "right_space":self.spaces[right]["reference"],
                    "selected_span_state":state_ref,"actual_product_image_dimension":962,
                    "number_of_original_left_anchors_used":ordinal+1,
                    "complete_product_image_is_H0_6H_minus_D1_minus_D2":True,
                    "evaluation_injective_on_entire_V6":True,
                    "full_seven_fibre_length":1904,"degree6H":1632,
                    "no_geometric_point_or_reduced_fibre_selected":True,
                    "exact_basis_definition":"selected original products and the bound unit minor",
                    "original_full418_by418_product_list_materialized":False})
                return basis,inverse,state["selected_rows"],self.refs[final_name]
            gc.collect()
        raise SearchStop("Finite ordered product-anchor prefix did not certify rank962; all actual ranks retained.")

    def membership_space(self,stem,basis,inverse,I,image_ref):
        name=stem+"-complete-two-anchor-membership"
        value=self.old(name)
        if value is None:
            self.budget()
            Eraw=[];Sraw=[]
            for z in range(7):
                part=rows(self.fibres[z]["E"])
                Eraw.extend(part);power=pow(z,3,P)
                Sraw.extend([[x*power%P for x in row] for row in part])
            E=mat(Eraw);S=mat(Sraw)
            complement=[i for i in range(1904) if i not in set(I)]
            assert len(complement)==942
            R0=E-basis*(inverse*sub(E,I,list(range(690))))
            R3=S-basis*(inverse*sub(S,I,list(range(690))))
            assert sub(R0,I,list(range(690)))==zero(962,690)
            assert sub(R3,I,list(range(690)))==zero(962,690)
            restriction=rows(sub(R0,complement,list(range(690))))+rows(sub(R3,complement,list(range(690))))
            value=self.put(name,{
                "prime":P,"source_complete_product_image":image_ref,
                "source_normal_fibres":[self.fibres[z]["reference"] for z in range(7)],
                "source_selected_rows":I,"complementary_rows":complement,
                "membership_anchors":["tau^3","sigma^3"],"matrix_shape":[1884,690],
                "matrix_mod_prime":restriction,
                "all_selected_row_residuals_zero":True,
                "two_anchors_have_no_common_zero":True,
                "exact_complete_kernel_space":"H0(3H-D1-D2)",
                "exact_dimension_by_degree272_Riemann_Roch":146})
        assert value["source_complete_product_image"]==image_ref
        M=mat(value["matrix_mod_prime"]);shape(value["matrix_mod_prime"],1884,690)
        profile_name=stem+"-membership-rank544"
        profile=self.rank_profile(profile_name,M,544,{"complete_membership":self.refs[name]})
        if not profile["accepted"]:
            raise UnitFailure("Complete membership matrix lacks required rank544 at the fixed place.")
        kernel,kref=self.complete_kernel(stem+"-complete-U146",M,profile,self.refs[profile_name],{
            "space":"H0(3H-D1-D2)","dimension":146,"degree":272,
            "source_two_anchor_membership":self.refs[name],
            "all_original_1884_conditions_required":True})
        return kernel,kref,self.refs[name]

    def first_unit_anchor(self,stem,U,Uref):
        name=stem+"-unscaled-P0-unit-anchor"
        value=self.old(name)
        if value is None:
            self.budget()
            evaluation=self.point_row*U
            values=[int(evaluation[0,j]) for j in range(146)]
            selected=next((j for j,x in enumerate(values) if x),None)
            if selected is None:
                self.put(name+"-unit-failure",{
                    "prime":P,"source_complete_U146":Uref,"P0_values_mod_prime":values,
                    "only_fixed_residue_unit_criterion_failed":True})
                raise UnitFailure("No P0-unit column in the complete original U146 at this fixed place.")
            coordinates=[int(U[i,selected]) for i in range(690)]
            value=self.put(name,{
                "prime":P,"source_complete_U146":Uref,
                "source_original_P0_functional":self.refs["neutral-H-and-original-P0-functional"],
                "all146_P0_values_mod_prime":values,"selected_original_column":selected,
                "normal_V3_coordinates_mod_prime":coordinates,
                "q_P0_value_mod_prime":values[selected],"q_P0_value_is_unit":True,
                "original_scalar_not_rescaled":True,
                "exact_anchor_definition":{"operation":"unchanged_original_complete_kernel_column",
                                          "source_complete_U146":Uref,"column":selected},
                "exact_function":"u/tau^3",
                "exact_divisor_identity":"D1+D2+D3-3H=div(u/tau^3)",
                "D3_effective_degree272_and_avoids_P0":True})
        assert value["source_complete_U146"]==Uref
        return value,self.refs[name]

    def recover_complete_space(self,stem,U,Uref,u,uref):
        complete_name=stem+"-complete-normal418-space"
        complete=self.old(complete_name)
        if complete is not None:
            assert complete["source_original_unscaled_u"]==uref
            assert complete["source_complete_U146"]==Uref
            return mat(complete["normal_V3_basis_mod_prime"]),self.refs[complete_name],complete
        left,leftrefs=self.product_fibres(stem+"-fixed-u-times-V3",u,uref,"V3")
        for trial in range(1,self.item["maximum_pencil_trials"]+1):
            anchor_name=stem+f"-trial-{trial:04d}-v"
            v=self.old(anchor_name)
            if v is None:
                self.budget()
                coefficients=[];power=1
                for j in range(146):
                    coefficients.append(power);power=power*trial%P
                coordinates=U*mat([[x] for x in coefficients])
                v=self.put(anchor_name,{
                    "prime":P,"source_complete_U146":Uref,"integer_parameter":trial,
                    "coefficients_in_original_U_basis_mod_prime":coefficients,
                    "normal_V3_coordinates_mod_prime":[int(coordinates[i,0]) for i in range(690)],
                    "exact_anchor_definition":{"operation":"sum_integer_parameter_powers_times_original_kernel_columns",
                                              "source_complete_U146":Uref,"integer_parameter":trial},
                    "original_scalar_not_rescaled":True})
            assert v["source_complete_U146"]==Uref and v["integer_parameter"]==trial
            vref=self.refs[anchor_name]
            right,rightrefs=self.product_fibres(stem+f"-trial-{trial:04d}-v-times-V3",v,vref,"V3")
            M=hcat(left,right)
            source_refs={"fixed_u":uref,"candidate_v":vref,
                         "all_seven_u_fibre_products":leftrefs,"all_seven_v_fibre_products":rightrefs}
            profile_name=stem+f"-trial-{trial:04d}-pencil-rank962"
            profile=self.rank_profile(profile_name,M,962,source_refs)
            self.checkpoint(profile_name)
            if not profile["accepted"]:
                continue
            K,kref=self.complete_kernel(stem+f"-trial-{trial:04d}-complete-relation418",
                M,profile,self.refs[profile_name],{
                    "relation":"u*r+v*s=0 in original V3 direct sum V3",
                    "fixed_common_zero_divisor":"D1+D2","degree":544,
                    "actual_rank962_excludes_any_additional_common_zero":True,
                    "kernel_dimension":418})
            self.budget()
            projected=sub(K,list(range(690,1380)),list(range(418)))
            reduced,rank=projected.transpose().rref()
            assert rank==418
            I=pivots(reduced,rank)
            A=sub(projected,I,list(range(418)));inverse=A.inv()
            assert A*inverse==eye(418) and inverse*A==eye(418)
            complete=self.put(complete_name,{
                "prime":P,"source_complete_U146":Uref,"source_original_unscaled_u":uref,
                "source_accepted_v":vref,"source_rank962_profile":self.refs[profile_name],
                "source_complete_relation_kernel":kref,"accepted_integer_parameter":trial,
                "matrix_shape":[690,418],"normal_V3_basis_mod_prime":rows(projected),
                "normal_V3_basis":[list(x) for x in self.V3],
                "projection_rows":[690,1380],"actual_projected_rank":418,
                "projection_unit_rows":I,"projection_unit_inverse_mod_prime":rows(inverse),
                "both_projection_inverse_products_verified":True,
                "all1904_rows_of_original_relation_verified":True,
                "complete_RR_space_certified":True,"exact_RR_space":"H0(3H-D3)",
                "D3_effective_degree272_and_avoids_original_P0":True,
                "exact_D3_definition":"div_3H(original unscaled u)-D1-D2",
                "normal_conversion_or_original_source_spaces_recomputed":False,
                "characteristic_zero_coefficients_reconstructed":False})
            self.checkpoint(complete_name)
            return projected,self.refs[complete_name],complete
        raise SearchStop("No rank962 pencil in the retained finite trial prefix; original complete U146 retained.")

    def principal_step(self,stem,new,left,right,u,uref,space_ref):
        name=stem+"-principal-function-and-P0-unit"
        value=self.old(name);a=self.spaces[left];b=self.spaces[right]
        if value is None:
            self.budget()
            q0=int(u["q_P0_value_mod_prime"])
            assert 0<q0<P and 0<a["Fvalue"]<P and 0<b["Fvalue"]<P
            denominator=q0*a["Fvalue"]%P*b["Fvalue"]%P
            F0=pow(denominator,-1,P);assert denominator*F0%P==1
            kappa=[-x-y for x,y in zip(a["kappa"],b["kappa"])]
            value=self.put(name,{
                "prime":P,"new_space_label":new,"left_space_label":left,"right_space_label":right,
                "source_left_complete_space":a["reference"],"source_right_complete_space":b["reference"],
                "source_original_unscaled_u":uref,"source_complete_new_normal418":space_ref,
                "left_original_class_coefficients":a["kappa"],
                "right_original_class_coefficients":b["kappa"],
                "new_original_class_coefficients":kappa,
                "class_coordinate_order":["Cstar-H","Dstar-H","Dchi-H"],
                "exact_q_function":{"operation":"divide_original_unscaled_section_by_tau_cubed",
                                    "source_original_section":uref,"section_frame":"original normal V3"},
                "exact_q_divisor_identity":"(Dleft-H)+(Dright-H)+(Dnew-H)=div(q)",
                "exact_F_function_DAG":{"operation":"inverse_of_product",
                    "factors":[{"operation":"q_u_over_tau_cubed","source":uref},
                               a["function"],b["function"]],
                    "repeated_parent_factors_are_retained_twice":True},
                "exact_class_and_function_identity":"kappa_new=(Dnew-H)+div(Fnew)",
                "q_P0_value_mod_prime":q0,"left_F_P0_value_mod_prime":a["Fvalue"],
                "right_F_P0_value_mod_prime":b["Fvalue"],
                "F_P0_value_mod_prime":F0,"F_P0_unit_inverse_product_verified":True,
                "all_selected_original_scalars_retained":True,
                "original_rho_order_of_F":0,
                "characteristic_zero_function_or_unit_value_expanded":False})
        assert value["source_left_complete_space"]==a["reference"]
        assert value["source_right_complete_space"]==b["reference"]
        assert value["source_original_unscaled_u"]==uref
        assert value["source_complete_new_normal418"]==space_ref
        return value,self.refs[name]

    def one_flip(self,index,new,left,right):
        stem=f"flip-{index:02d}-{new}"
        name=stem+"-complete-flip-certificate"
        old=self.old(name)
        if old is None:
            self.budget()
            basis,inverse,I,image_ref=self.product_span(stem,left,right)
            U,Uref,membership_ref=self.membership_space(stem,basis,inverse,I,image_ref)
            u,uref=self.first_unit_anchor(stem,U,Uref)
            matrix,space_ref,space=self.recover_complete_space(stem,U,Uref,u,uref)
            principal,principal_ref=self.principal_step(stem,new,left,right,u,uref,space_ref)
            old=self.put(name,{
                "prime":P,"flip_index":index,"new_space_label":new,"input_labels":[left,right],
                "left_complete_space":self.spaces[left]["reference"],
                "right_complete_space":self.spaces[right]["reference"],
                "complete_product_image":image_ref,"complete_membership_matrix":membership_ref,
                "complete_U146":Uref,"original_unscaled_P0_unit_section":uref,
                "complete_normal418_space":space_ref,"principal_function_and_P0_unit":principal_ref,
                "actual_product_image_dimension":962,"actual_U_dimension":146,
                "actual_pencil_rank":962,"actual_complete_space_dimension":418,
                "all1904_by418_pencil_relations_verified":True,
                "all1884_by146_membership_relations_verified":True,
                "effective_degree272_and_original_P0_avoidance_certified":True,
                "complete_characteristic_zero_space_defined_by_original_unit_minors":True,
                "original_function_divisor_identity_and_unit_retained":True,
                "characteristic_zero_arrays_reconstructed":False})
        else:
            assert old["flip_index"]==index and old["input_labels"]==[left,right]
            assert old["left_complete_space"]==self.spaces[left]["reference"]
            assert old["right_complete_space"]==self.spaces[right]["reference"]
            space_ref=old["complete_normal418_space"]
            space=self.own(space_ref);matrix=mat(space["normal_V3_basis_mod_prime"])
            principal_ref=old["principal_function_and_P0_unit"]
            principal=self.own(principal_ref)
        self.spaces[new]={"matrix":matrix,"reference":space_ref,
            "kappa":principal["new_original_class_coefficients"],
            "Fvalue":principal["F_P0_value_mod_prime"],
            "function":{"operation":"previous_exact_principal_function_DAG","source":principal_ref}}
        self.flip_refs.append(self.refs[name])
        self.checkpoint("complete-"+stem)
        gc.collect()
        return self.refs[name]

    def marked_principal(self):
        name="original-Ef-bounded-representative-and-marked-principal-QE"
        value=self.old(name)
        if value is None:
            self.budget()
            terminal=self.spaces["DE"]
            assert terminal["kappa"]==[-1,3,4] and len(self.flip_refs)==8
            original=int(self.Qtilde["actual_leading_coefficient_mod_prime"])
            assert original==267133051 and self.Qtilde["actual_rho_order"]==-1205
            correction=terminal["Fvalue"]
            rho_leading=original*correction%P
            cpower=int(self.frame["actual_c_powers_mod_prime"]["1205"])
            t_leading=rho_leading*cpower%P
            assert rho_leading and t_leading
            value=self.put(name,{
                "prime":P,"source_original_Qtilde":self.inputs["Qtilde"],
                "source_original_t_frame":self.inputs["t_frame"],
                "source_complete_DE_normal418":terminal["reference"],
                "source_all_eight_complete_flips":self.flip_refs,
                "target_original_class_coefficients":[-1,3,4],
                "class_coordinate_order":["Cstar-H","Dstar-H","Dchi-H"],
                "exact_QE_function_DAG":{"operation":"multiply",
                    "left":{"operation":"original_Qtilde","source":self.inputs["Qtilde"]},
                    "right":terminal["function"]},
                "exact_original_divisor_identity":"Ef-1206P0=(DE-H)+div(QE)",
                "original_fractional_ideal_principal_factor_direction":"positive multiplication by QE",
                "DE_effective_degree":272,"DE_avoids_original_P0":True,
                "complete_W_DE_dimension":418,"exact_space":"H0(3H-DE)",
                "original_local_parameter":"rho=z-z0","actual_rho_order":-1205,
                "source_Qtilde_rho_leading_mod_prime":original,
                "terminal_F_P0_unit_mod_prime":correction,
                "actual_QE_rho_leading_mod_prime":rho_leading,
                "actual_original_c_power1205_mod_prime":cpower,
                "actual_QE_t_leading_mod_prime":t_leading,
                "exact_t_leading_expression":{
                    "operation":"multiply_original_Qtilde_leading_F_P0_and_c_power1205",
                    "Qtilde_source":self.inputs["Qtilde"],"F_source":terminal["function"],
                    "c_source":self.inputs["t_frame"],
                    "original_c_definition":self.frame["exact_c_expression"],
                    "positive_exponent":1205},
                "all_eight_original_unscaled_q_P0_units_retained":True,
                "actual_original_t_frame_evaluated":True,
                "auxiliary_unit_asserted_to_be_41_adic_unit":False,
                "characteristic_zero_RR_coefficients_or_leading_scalar_expanded":False,
                "other_six_Galois_representatives_computed":False,
                "five_original_Lj_RR128_or144_computed":False,
                "Hecke_active_support_nonp_connection_period_or_height_computed":False})
        assert value["source_all_eight_complete_flips"]==self.flip_refs
        assert value["source_complete_DE_normal418"]==self.spaces["DE"]["reference"]
        self.checkpoint("complete-original-Ef-and-t-frame")
        return self.refs[name]

    def inventory(self):
        entries=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name==PREFIX+"current.json.gz" or path.name.startswith(PREFIX+"stage-manifest-"):
                continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
            entries.append(spec(path))
        value={"result":RESULT,"configuration":self.tag,"complete":True,
               "files":entries,"current_excluded":True,"all_complete_stages_retained":True}
        path=self.path("stage-manifest-"+fingerprint(value))
        if path.exists():
            assert read(path)==value
        else:
            save(path,value)
        return spec(path),len(entries)

    def finish(self,complete,reason):
        self.checkpoint("completed" if complete else self.phase)
        inventory,count=self.inventory()
        marked=self.refs.get("original-Ef-bounded-representative-and-marked-principal-QE")
        if complete:
            assert len(self.flip_refs)==8 and marked is not None
            assert self.spaces["DE"]["kappa"]==[-1,3,4]
        cert={"result":RESULT,"configuration":self.tag,"complete":bool(complete),
              "p":41,"actual_auxiliary_prime":P,
              "source_audit":self.refs.get("original-source-audit"),
              "actual_complete_flip_count":len(self.flip_refs),
              "complete_flip_certificates":self.flip_refs,"marked_principal_QE":marked,
              "actual_all_eight_complete_normal418_spaces_certified":len(self.flip_refs)==8,
              "actual_original_Ef_bounded_divisor_identity_certified":marked is not None,
              "actual_original_t_leading_coefficient_computed":marked is not None,
              "original_characteristic_zero_functions_defined_by_bound_unit_solve_DAGs":True,
              "old_three418_spaces_W_Krylov_jets_or_original_c_recomputed":False,
              "original_selected_scalars_rescaled_to_one":False,
              "characteristic_zero_coefficients_or_leading_scalar_expanded":False,
              "other_six_Galois_representatives_computed":False,
              "five_original_Lj_RR128_or144_computed":False,
              "Hecke_active_support_nonp_connection_period_or_height_computed":False,
              "actual_complete_math_stage_count":count,
              "stage_manifest":inventory,"resume_state":self.current,
              "stop_reason":reason,"seconds":time.monotonic()-self.started}
        save(self.out/FINAL,cert)
        return cert

    def run(self):
        self.prepare()
        assert 1<=self.item["maximum_product_anchors"]<=418
        assert 1<=self.item["maximum_pencil_trials"]<=1000
        for index,(new,left,right) in enumerate(CHAIN,1):
            self.one_flip(index,new,left,right)
        self.marked_principal()
        return self.finish(True,None)

def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise SystemExit("R890 new mathematics only runs in the authorized public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    for key in ("config","retained","output"):
        parser.add_argument("--"+key,required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args();assert 0<args.budget_minutes<=300
    started=time.monotonic();out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    job=None;cert=None;code=1;error=None
    try:
        job=Job(args);cert=job.run();code=0 if cert["complete"] else 2
    except BudgetStop as exc:
        code=124;error={"type":"BudgetStop","message":str(exc)}
    except (UnitFailure,SearchStop) as exc:
        code=2;error={"type":type(exc).__name__,"message":str(exc)}
    except Exception as exc:
        error={"type":type(exc).__name__,"message":str(exc)};traceback.print_exc()
    if cert is None and job is not None:
        try:
            cert=job.finish(False,error)
        except Exception:
            traceback.print_exc()
    receipt={"result":RESULT,"source_sha256":sha(__file__),"complete":code==0,
             "process_exit_code":code,"error":error,"seconds":time.monotonic()-started,
             "configuration":None if job is None else job.tag,
             "configuration_sha256":None if job is None else fingerprint(job.tag),
             "certificate_sha256":sha(out/FINAL) if (out/FINAL).exists() else None,
             "actual_complete_flip_count":0 if cert is None else cert["actual_complete_flip_count"],
             "actual_original_t_leading_coefficient_computed":bool(cert and cert["actual_original_t_leading_coefficient_computed"]),
             "old_three418_spaces_W_Krylov_jets_or_original_c_recomputed":False,
             "new_mathematics_only_in_public_Actions":True}
    save(out/"core-receipt.json",receipt)
    printed={k:v for k,v in receipt.items() if k!="configuration"}
    print("R890_CORE_RECEIPT="+json.dumps(printed,sort_keys=True),flush=True)
    raise SystemExit(code)
if __name__=="__main__":
    main()
