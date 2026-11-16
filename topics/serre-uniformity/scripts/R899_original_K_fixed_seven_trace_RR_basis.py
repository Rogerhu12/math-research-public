#!/usr/bin/env python3
"""R899: K-fixed complete trace RR basis from whole-fibre coordinate normalization.

All new arithmetic is restricted to the authorized public Actions workflow.
Stored finite-field matrices are images of the exact original source-bound
unit-solve objects, not reconstructed characteristic-zero coefficients.
"""
import argparse
import gc
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import sys
import time
import traceback
import flint
from flint import nmod_mat

REPOSITORY="Rogerhu12/math-research-public"
RESULT="R899-original-K-fixed-seven-trace-RR-basis"
FINAL="p41-original-K-fixed-seven-trace-RR-basis-certificate.json"
PREFIX="R899-"
MANIFEST="full-outputs-manifest.json"
P=1000000753
N=272
DIM=418
V3DIM=690
EPS=[0]+[1]*144+[2]*127
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
GROUPS=("R894","R890","SIXD","R880","R887","R872","R883","R827","R885","R845")
PROOF_SHA="eff6a8abf489bedf2cda8549a027ebd250717b2ddedece420f2a9d729cebc044"
TRACE_CORE="9a2793c79e552c04ea384f5c6bfb673e6e7d506ff91cf9e246fbc00a76f2da56"
FLIP_CORE="da8498fc6ab0f143ba347f4a7dec91c7474bbe2520c349bf33a84bba8e65420f"
ARTIN_SHA="e47cd50d254700b98446866297d79694c100f1435c46f3b4f42e3835763f897d"
CHAIN=(("A1","D0","D1"),("A2","D2","D3"),("A3","A1","A2"),
       ("A4","A3","D4"),("A5","D5","D6"),("A6","A4","A5"),
       ("A7","A6","A6"),("A8","A7","H"),("A9","A8","A6"),
       ("B3","Cstar","H"),("B4","B3","X4"),("B5","B4","B4"),
       ("B6","B5","B5"),("B7","B6","B4"),("B8","B7","B5"),("DN","A9","B8"))
STRATEGY={
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "original_integral_B_root":3197390,
    "normal_basis_degrees":EPS,"normal_V3_dimension":V3DIM,"fixed_RR_dimension":DIM,
    "constant_field_descent":"original Gal(L/K) of order7, K=Q(zeta3)",
    "space":"H0(2H-T_f^0), T_f^0=sum_sigma(E_f)-8442P0",
    "positive_identification":"Q_N * H0(3H-D_N)",
    "old_fibre_schedule":[0,1,2,3,4,5,6],"initial_usable_fibres":3,
    "no_automatic_three_fibre_injectivity_assumed":True,
    "acceptance":"actual 418-row unit minor of all computed K-coordinate evaluations",
    "every_required_division_in_complete272_Artin_algebra":True,
    "QN_itself_not_required_to_be_a_unit":True,
    "original_charpoly_Krylov_inverse_and_V3_evaluation_recomputed":False,
    "zero_branch_a_old_fibres":[0,1,2,3,4],
    "zero_branch_a_missing_node_rule":"only if needed: degree<=3-epsilon interpolation from old0..3, checked on old4",
    "normal_basis_change":"B_N times inverse(selected_QN_times_WN_evaluation)",
    "exact_old_descent_matrix":"A^-1 sigma(A), expression only",
    "exact_new_fixed_basis_action":"I418 by uniqueness of K-linear selected coordinates",
    "new_sigma_replay_or_old_flip_repetition":False,
    "source_flip_chain":[list(x) for x in CHAIN],
    "original_QN_rho_order":-8435,"original_t_leading_exponent":8435,
    "original_P0_values_and_all_scalars_preserved_without_rescaling":True,
    "characteristic_zero_arrays_expanded":False,
    "Q_fixed_basis_Hecke_norm_connection_or_height_computed":False,
    "only_budget_and_transport_excluded_from_mathematical_identity":True}

class BudgetStop(RuntimeError):
    pass
class SearchStop(RuntimeError):
    pass

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(4*1024*1024),b""):
            h.update(b)
    return h.hexdigest()
def read(path):
    p=Path(path)
    with (gzip.open if p.suffix==".gz" else open)(p,"rt",encoding="utf-8") as f:
        return json.load(f)
def save(path,value):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    q=p.with_name(p.name+".tmp")
    data=(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n").encode()
    if p.suffix==".gz":
        with q.open("wb") as f:
            with gzip.GzipFile(filename="",fileobj=f,mode="wb",mtime=0,compresslevel=2) as z:
                z.write(data)
    else:
        q.write_bytes(data)
    q.replace(p)
def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def plain(value):
    row={k:value[k] for k in ("file","bytes","sha256")}
    p=PurePosixPath(row["file"])
    assert len(p.parts)==1 and p.name not in ("",".","..") and "\\" not in p.name
    assert isinstance(row["bytes"],int) and row["bytes"]>=0
    return row
def spec(path):
    p=Path(path)
    return {"file":p.name,"bytes":p.stat().st_size,"sha256":sha(p)}
def group_ref(group,row):
    return {"source_group":group,**plain(row)}
def identity(source):
    out={k:source[k] for k in BASE}
    out.update(configuration_sha256=source["configuration_sha256"],
               selected_files_sha256=fingerprint(source["files"]))
    if source.get("certificate") is not None:
        out["certificate"]=plain(source["certificate"])
    else:
        out["configuration_stage"]=plain(source["configuration_stage"])
    return out
def same_source(a,b):
    assert all(str(a[k])==str(b[k]) for k in BASE)
    if a.get("configuration_sha256") is not None and b.get("configuration_sha256") is not None:
        assert a["configuration_sha256"]==b["configuration_sha256"]
def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
            "method_sha256":item["method_sha256"],"proofs":item["proofs"],
            "artin_helper_sha256":ARTIN_SHA,
            "sources":{g:identity(item["sources"][g]) for g in GROUPS},
            "inputs":item["inputs"],"strategy":STRATEGY}
def positions(weight):
    return [(i,k) for i in range(N) for k in range(max(0,weight-EPS[i]+1))]
def shape(raw,m,n):
    assert len(raw)==m and all(len(row)==n for row in raw),(m,n)
    assert all(isinstance(v,int) and 0<=v<P for row in raw for v in row)
def vector(raw,n):
    if len(raw)==n and all(isinstance(x,list) and len(x)==1 for x in raw):
        raw=[x[0] for x in raw]
    assert len(raw)==n and all(isinstance(v,int) and 0<=v<P for v in raw)
    return list(raw)
def mat(raw):
    return nmod_mat(raw,P)
def rows(A):
    return [[int(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())]
def eye(n):
    return mat([[int(i==j) for j in range(n)] for i in range(n)])
def sub(A,I,J):
    return mat([[int(A[i,j]) for j in J] for i in I])
def pivots(A,rank):
    result=[next(j for j in range(A.ncols()) if A[i,j]) for i in range(rank)]
    assert result==sorted(set(result))
    return result

class Source:
    def __init__(self,label,item,root):
        self.label=label;self.item=item;self.folder=Path(root)/label;self.checked=set()
        self.files={n:plain(v) for n,v in item["files"].items()}
        assert all(n==v["file"] for n,v in self.files.items())
        mpath=self.folder/MANIFEST
        assert sha(mpath)==item["manifest_sha256"]
        m=read(mpath)
        assert m["result"]==item["result"]
        entries={v["file"]:plain(v) for v in m["files"]}
        assert len(entries)==len(m["files"])
        entries[MANIFEST]=spec(mpath)
        for name,row in self.files.items():
            if name!="full-outputs-manifest-reference.json":
                assert entries[name]==row,(label,name)
        initial=self.get("public-actions-input.json")
        run=self.get("run-receipt.json")
        assert initial["source_commit"]==run["source_commit"]==item["source_commit"]
        assert str(run["workflow_run_id"])==str(item["run_id"])
        assert initial.get("core_sha256",initial.get("job",{}).get("core_sha256"))==item["core_sha256"]
        self.certificate=None
        if item.get("certificate") is not None:
            assert self.files[item["certificate"]["file"]]==plain(item["certificate"])
            self.certificate=self.get(item["certificate"]["file"])
            assert self.certificate["result"]==item["result"] and self.certificate["complete"] is True
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
            assert self.files["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
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
        p=self.folder/name
        if name not in self.checked:
            assert spec(p)==self.files[name],(self.label,name)
            self.checked.add(name)
        return read(p)
    def stage(self,row):
        assert self.files[row["file"]]==plain(row)
        value=self.get(row["file"])
        assert value["complete"] is True and value["configuration"]==self.tag
        assert value.get("result",value["configuration"]["result"])==self.item["result"]
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
        assert self.item["proofs"]["R899"]["sha256"]==PROOF_SHA
        for proof in self.item["proofs"].values():
            assert sha(topic/proof["path"])==proof["sha256"]
        helper=Path(__file__).resolve().parent/self.item["artin_helper"]
        assert self.item["artin_helper_sha256"]==ARTIN_SHA==sha(helper)
        ms=importlib.util.spec_from_file_location("r899_original_complete_artin_helper",helper)
        self.AH=importlib.util.module_from_spec(ms);ms.loader.exec_module(self.AH)
        assert set(self.item["sources"])==set(GROUPS)
        self.tag=expected_tag(self.item);self.inputs=self.item["inputs"]
        self.refs={};self.current=None;self.phase="sources"
        self.node_decisions=[];self.accepted_nodes=[];self.base_fibres={};self.normalized_fibres={}
        self.rank=0;self.selected_rows=None;self.fixed_basis_ref=None;self.point_ref=None
        self.sources={g:Source(g,self.item["sources"][g],args.retained) for g in GROUPS}
        self.points={};self.fibres={};self.sections={};self.flip_records=[]
    def budget(self):
        if time.monotonic()-self.started>=max(0,self.args.budget_minutes*60-30):
            raise BudgetStop("R899 original complete atomic stages retained; phase="+self.phase)
    def path(self,name):
        assert Path(name).name==name
        return self.out/(PREFIX+name+".json.gz")
    def old(self,name):
        p=self.path(name)
        if not p.exists():return None
        value=read(p)
        assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
        self.refs[name]=spec(p)
        return value
    def put(self,name,value):
        assert not any(k in value for k in ("result","configuration","complete"))
        value={"result":RESULT,"configuration":self.tag,"complete":True,**value}
        p=self.path(name)
        if p.exists():assert read(p)==value
        else:save(p,value)
        self.refs[name]=spec(p)
        print("R899_STAGE="+json.dumps({"file":p.name,"seconds":time.monotonic()-self.started}),flush=True)
        return value
    def checkpoint(self,phase):
        self.phase=phase
        save(self.path("current"),{
            "result":RESULT,"configuration":self.tag,"complete":False,"phase":phase,
            "completed_stages":self.refs,"node_decisions":self.node_decisions,
            "accepted_nodes":self.accepted_nodes,"actual_evaluation_rank":self.rank,
            "completed_normalized_space_fibres":self.normalized_fibres})
        self.current=spec(self.path("current"))
    def source(self,ref):
        return self.sources[ref["source_group"]].stage(ref)
    def input(self,key):
        return self.source(self.inputs[key])
    def own(self,ref):
        p=self.out/plain(ref)["file"];assert spec(p)==plain(ref)
        value=read(p);assert value["complete"] is True and value["configuration"]==self.tag
        return value
    def equal_input(self,row,key):
        assert plain(row)==plain(self.inputs[key]),key
    def embed_V2(self,raw):
        v=vector(raw,DIM);lookup={pair:i for i,pair in enumerate(self.V3)}
        out=[0]*V3DIM
        for c,pair in zip(v,self.V2):out[lookup[pair]]=c
        return out
    def prepare(self):
        self.V3=positions(3);self.V2=positions(2)
        assert len(self.V3)==690 and len(self.V2)==418
        trace=self.sources["R894"];tc=trace.certificate
        assert trace.item["core_sha256"]==TRACE_CORE
        assert tc["actual_all_sixteen_new_complete_normal418_spaces_certified"] is True
        assert tc["actual_original_seven_pole_trace_bounded_identity_certified"] is True
        assert tc["actual_new_complete_flip_count"]==16 and tc["actual_reused_R890_complete_flip_count"]==2
        assert tc["terminal_divisor_or_basis_claimed_K_fixed"] is False
        self.equal_input(tc["marked_principal_and_descent"],"marked_QN")
        for g in ("R890","SIXD","R880","R887","R872","R883","R827"):
            same_source(trace.tag["sources"][g],self.item["sources"][g])
        assert self.sources["R890"].item["core_sha256"]==FLIP_CORE
        same_source(self.sources["R880"].tag["sources"]["R845"],self.item["sources"]["R845"])
        self.marked=self.input("marked_QN")
        assert self.marked["actual_rho_order"]==-8435 and self.marked["DN_avoids_original_P0"] is True
        assert self.marked["DN_effective_degree"]==272 and self.marked["complete_W_DN_dimension"]==418
        assert self.marked["Q_orbit_fixed_by_original_Gal_L_over_K"] is True
        assert self.marked["original_fractional_ideal_principal_factor_direction"]=="positive multiplication by Q_N"
        assert self.marked["exact_original_divisor_identity"]=="T_f^0=(D_N-H)+div(Q_N)"
        self.equal_input(self.marked["source_complete_DN_normal418"],"terminal_normal418")
        self.Bstage=self.input("terminal_normal418")
        assert self.Bstage["complete_RR_space_certified"] is True and self.Bstage["actual_projected_rank"]==418
        assert self.Bstage["normal_V3_basis"]==[list(x) for x in self.V3]
        shape(self.Bstage["normal_V3_basis_mod_prime"],690,418)
        self.BN=mat(self.Bstage["normal_V3_basis_mod_prime"])
        self.neutral=self.input("original_neutral")
        assert self.neutral["normal_V3_basis"]==[list(x) for x in self.V3]
        self.point_row=vector(self.neutral["normal_V3_P0_functional_mod_prime"],690)
        self.place=self.input("original_place")
        assert self.place["prime"]==P and self.place["original_zeta_root"]==549966761
        self.W=self.input("original_W");assert self.W["prime"]==P
        self.frame=self.input("original_t_frame")
        assert self.frame["original_t_first_order_unit_certified"] is True
        self.equal_input(self.marked["source_original_t_frame"],"original_t_frame")
        assert self.marked["actual_original_c_power1205_mod_prime"]==self.frame["actual_c_powers_mod_prime"]["1205"]
        for key in ("actual_QN_rho_leading_mod_prime","actual_QN_t_leading_mod_prime","actual_original_c_power8435_mod_prime"):
            assert 0<int(self.marked[key])<P
        assert len(self.inputs["original_Krylov_points"])==len(self.inputs["original_normal_V3_fibres"])==7
        self.charrelation=self.input("original_characteristic_relation")
        assert self.charrelation["exact_original_modular_characteristic_polynomial_certified"] is True
        self.equal_input(self.charrelation["source_original_W"],"original_W")
        assert len(self.inputs["original_characteristic_nodes"])==7
        self.chars={}
        for z in range(7):
            kr=self.inputs["original_Krylov_points"][z]
            point=self.source(kr)
            assert point["prime"]==P and point["z0"]==z and point["usable"] is True
            assert point["actual_cyclic_rank"]==272 and point["both_inverse_products_verified"] is True
            self.equal_input(point["source_original_W"],"original_W")
            shape(point["Krylov_matrix_mod_prime"],272,272)
            shape(point["inverse_Krylov_matrix_mod_prime"],272,272)
            fr=self.inputs["original_normal_V3_fibres"][z]
            fibre=self.source(fr)
            assert fibre["prime"]==P and fibre["z0"]==z
            assert plain(fibre["source_original_Krylov_point"])==plain(kr)
            self.equal_input(fibre["source_original_W"],"original_W")
            shape(fibre["normal_evaluation_mod_prime"],272,690)
            shape(fibre["cyclic_evaluation_mod_prime"],272,690)
            cr=self.inputs["original_characteristic_nodes"][z]
            assert plain(self.charrelation["source_node_stages"][z])==plain(cr)
            char=self.source(cr)
            assert char["prime"]==P and char["ordinal"]==z and char["z_value"]==z
            assert char["monic"] is True and char["polynomial_degree"]==272
            assert char["full_K_times_relation_equals_k272"] is True
            assert char["completed_original_Krylov_inverse_recomputed"] is False
            assert plain(char["source_original_Krylov"])==plain(kr)
            self.equal_input(char["source_original_W"],"original_W")
            self.points[z]=point;self.fibres[z]=fibre;self.chars[z]=char
        point=self.input("original_point_linearization")
        assert point["z0_mod_prime"]==110702704 and point["chosen_local_parameter"]=="z_minus_z0"
        assert all(z!=point["z0_mod_prime"] for z in range(7))
        self.zero_selection=self.input("original_zero_a_selection")
        assert self.zero_selection["accepted"] is True and self.zero_selection["selected_original_role"]=="a"
        assert self.zero_selection["block_swap_used"] is False and self.zero_selection["no_rescaling"] is True
        self.zero_candidate=self.input("original_zero_a_candidate")
        self.equal_input(self.zero_selection["source_original_sections"],"original_zero_a_candidate")
        assert self.zero_candidate["a_exact_D_basis_column"]==0
        assert self.zero_candidate["a_and_b_are_the_original_unit_solve_sections"] is True
        assert self.zero_candidate["extra_rescaling_or_reconstruction_used"] is False
        self.zero_values={}
        assert len(self.inputs["original_zero_a_old_fibres"])==5
        for z,ref in enumerate(self.inputs["original_zero_a_old_fibres"]):
            val=self.source(ref)
            assert val["prime"]==P and val["z0"]==z and val["which"]=="a"
            assert val["a_exact_D_basis_column"]==0
            assert plain(val["source_complete_original_D_basis"])==plain(self.zero_candidate["source_complete_original_D_basis"])
            assert plain(val["source_original_Krylov_point"])==plain(self.inputs["original_Krylov_points"][z])
            self.zero_values[z]=vector(val["section_evaluation_mod_prime"],272)
        self.zero_v=self.input("original_zero_v")
        assert self.zero_v["which"]=="v" and self.zero_v["order123_is_exact"] is True
        assert self.zero_v["no_rescaling_or_new_coefficient_reconstruction"] is True
        self.baseprincipal=self.input("original_zero_Qf")
        self.equal_input(self.baseprincipal["source_original_anchor_selection"],"original_zero_a_selection")
        self.equal_input(self.baseprincipal["source_exact_v"],"original_zero_v")
        self.q0=self.input("original_zero_Qtilde")
        self.equal_input(self.q0["source_original_Q_f"],"original_zero_Qf")
        self.equal_input(self.q0["source_exact_u_C"],"original_u_C")
        assert self.q0["original_Cstar_and_qC_are_fixed_by_L_over_K_Galois_action"] is True
        self.uC=self.input("original_u_C")
        assert self.uC["accepted"] is True and self.uC["actual_order252_unit_mod_prime"]
        self.uchi=self.input("original_u_chi")
        assert self.uchi["role"]=="u" and self.uchi["order272_is_exact"] is True
        assert self.uchi["normal_integer_scale_applied_again"] is False
        assert plain(self.baseprincipal["exact_function_DAG"]["u_chi_over_tau2"]["source_section"])==plain(self.inputs["original_u_chi"])
        self.sections["v0"]=(self.inputs["original_zero_v"],vector(self.zero_v["normal_V3_coordinates_mod_prime"],690))
        self.sections["qC"]=(self.inputs["original_u_C"],self.embed_V2(self.uC["u_C_normal_V2_coordinates_mod_prime"]))
        self.sections["qchi"]=(self.inputs["original_u_chi"],self.embed_V2(self.uchi["V2_coordinates_mod_prime"]))
        self.orbit_principals=[self.inputs["original_zero_Qtilde"]]
        assert len(self.inputs["six_original_branches"])==6
        for j,record in enumerate(self.inputs["six_original_branches"],1):
            principal=self.source(record["principal"])
            a=self.source(record["a"]);v=self.source(record["v"])
            assert principal["sigma_power"]==a["sigma_power"]==v["sigma_power"]==j
            assert principal["original_branch"]==[0,6,1,2,4,3,5][j]
            assert principal["roots_B_s"][1]==99932770
            assert plain(principal["source_actual_a"])==plain(record["a"])
            assert plain(principal["source_actual_v"])==plain(record["v"])
            self.equal_input(principal["source_original_common_u_C"],"original_u_C")
            self.equal_input(principal["source_original_common_u_chi"],"original_u_chi")
            self.equal_input(principal["source_original_zero_branch_Qtilde"],"original_zero_Qtilde")
            assert principal["exact_original_Galois_conjugate_not_a_new_linearly_equivalent_choice"] is True
            assert a["no_rescaling"] is True and a["block_swap_used"] is False
            assert v["no_rescaling_or_new_column_selection"] is True and v["which"]=="v"
            self.sections["a"+str(j)]=(record["a"],vector(a["a_normal_V3_coordinates_mod_prime"],690))
            self.sections["v"+str(j)]=(record["v"],vector(v["normal_V3_coordinates_mod_prime"],690))
            self.orbit_principals.append(record["principal"])
        assert [plain(x["source"]) for x in self.marked["source_all_seven_original_principals"]]==[plain(x) for x in self.orbit_principals]
        self.prepare_flips()
        name="original-source-audit"
        if self.old(name) is None:
            self.put(name,{
                "prime":P,"sources":{g:identity(self.item["sources"][g]) for g in GROUPS},
                "inputs":self.inputs,"source_original_QN":self.inputs["marked_QN"],
                "same_original_Galois_orbit_and_all_unscaled_leaves_bound":True,
                "complete_terminal_WN_dimension":418,"original_K_defined_RR_space_degree":544,
                "original_K_defined_RR_dimension":418,"full_Artin_dimension":272,
                "actual_418_minor_not_presumed":True,
                "old_zero_branch_a_five_section_values_reused_without_recomputation":True,
                "old_sixteen_flips_Krylov_charpoly_V3_evaluation_and_P0_jets_recomputed":False,
                "all_new_mathematics_only_in_public_Actions":True})
        self.checkpoint("original-sources-bound")
    def prepare_flips(self):
        old=self.inputs["two_original_chi_flips"]
        assert len(old)==2
        for ordinal,(record,label,source_label,parents) in enumerate(zip(old,("X2","X4"),("D2","E"),(("X","X"),("X2","X2"))),4):
            complete=self.source(record["complete"]);principal=self.source(record["principal"]);u=self.source(record["u"])
            assert complete["flip_index"]==ordinal and complete["new_space_label"]==source_label
            assert complete["actual_complete_space_dimension"]==418
            assert plain(complete["principal_function_and_P0_unit"])==plain(record["principal"])
            assert plain(complete["original_unscaled_P0_unit_section"])==plain(record["u"])
            assert plain(principal["source_original_unscaled_u"])==plain(record["u"])
            assert principal["new_space_label"]==source_label
            assert principal["all_selected_original_scalars_retained"] is True
            assert u["original_scalar_not_rescaled"] is True and u["q_P0_value_is_unit"] is True
            self.sections["q-"+label]=(record["u"],vector(u["normal_V3_coordinates_mod_prime"],690))
            self.flip_records.append((label,parents[0],parents[1],record))
        new=self.inputs["new_trace_flips"]
        assert len(new)==16
        assert [plain(x["complete"]) for x in new]==[plain(x) for x in self.marked["source_all_new_complete_flips"]]
        for ordinal,(record,definition) in enumerate(zip(new,CHAIN),1):
            label,left,right=definition
            complete=self.source(record["complete"]);principal=self.source(record["principal"]);u=self.source(record["u"])
            assert complete["flip_index"]==ordinal and complete["new_space_label"]==label
            assert complete["input_labels"]==[left,right]
            assert complete["actual_complete_space_dimension"]==418
            assert plain(complete["principal_function_and_P0_unit"])==plain(record["principal"])
            assert plain(complete["original_unscaled_P0_unit_section"])==plain(record["u"])
            assert plain(principal["source_original_unscaled_u"])==plain(record["u"])
            assert principal["new_space_label"]==label and principal["left_space_label"]==left and principal["right_space_label"]==right
            assert principal["all_selected_original_scalars_retained"] is True
            assert u["original_scalar_not_rescaled"] is True and u["q_P0_value_is_unit"] is True
            self.sections["q-"+label]=(record["u"],vector(u["normal_V3_coordinates_mod_prime"],690))
            self.flip_records.append((label,left,right,record))
        assert plain(new[-1]["space"])==plain(self.inputs["terminal_normal418"])
        for label,left,right,record in self.flip_records:
            p=self.source(record["principal"])
            assert p["exact_F_function_DAG"]["operation"]=="inverse_of_product"
            assert p["exact_F_function_DAG"]["repeated_parent_factors_are_retained_twice"] is True
    def algebra(self,z):
        return self.AH.SourceAlgebra(self.chars[z]["characteristic_coefficients_ascending_T"],P)
    def zero_a_interpolation(self):
        name="zero-branch-a-normal-polynomial-from-old-five-fibres"
        value=self.old(name)
        if value is None:
            self.budget()
            V=mat([[pow(z,k,P) for k in range(4)] for z in range(4)])
            inverse=V.inv()
            assert V*inverse==eye(4) and inverse*V==eye(4)
            values=mat([self.zero_values[z] for z in range(4)])
            coeff=inverse*values
            for i in range(N):
                for k in range(4-EPS[i],4):assert coeff[k,i]==0
            for z in range(5):
                answer=mat([[pow(z,k,P) for k in range(4)]])*coeff
                assert rows(answer)[0]==self.zero_values[z]
            packed=[int(coeff[k,i]) for i,k in self.V3]
            value=self.put(name,{
                "prime":P,"source_original_a_selection":self.inputs["original_zero_a_selection"],
                "source_five_original_a_fibre_values":self.inputs["original_zero_a_old_fibres"],
                "interpolation_nodes":[0,1,2,3],"extra_check_node":4,
                "coefficient_degrees_by_normal_row":[3-e for e in EPS],
                "normal_polynomial_coefficients_mod_prime":rows(coeff),
                "normal_V3_coordinates_mod_prime":packed,
                "both_four_by_four_inverse_products_verified":True,
                "all_five_old272_values_multiplied_back":True,
                "all_original_weighted_degree_bounds_verified":True,
                "exact_definition":"unique original normal V3 section with these same old four complete fibre values",
                "old_V3_normal_conversion_or_old_a_fibre_multiplication_recomputed":False})
        return value,self.refs[name]
    def element(self,z,key,A):
        name=f"node-{z}-leaf-{key}"
        value=self.old(name)
        if value is None:
            self.budget()
            if key=="a0":
                if z<=4:
                    normal=self.zero_values[z]
                    source=self.inputs["original_zero_a_old_fibres"][z]
                    exact={"operation":"already_completed_original_a_whole_fibre_value","source":source}
                else:
                    interpolated,source=self.zero_a_interpolation()
                    coordinates=vector(interpolated["normal_V3_coordinates_mod_prime"],690)
                    normal=rows(mat(self.fibres[z]["normal_evaluation_mod_prime"])*mat([[x] for x in coordinates]))
                    normal=vector(normal,272)
                    exact={"operation":"evaluate_original_V3_unique_interpolation","source":source,"z0":z}
            else:
                source,coordinates=self.sections[key]
                normal=vector(rows(mat(self.fibres[z]["normal_evaluation_mod_prime"])*mat([[x] for x in coordinates])),272)
                exact={"operation":"original_section_over_its_original_tau_frame","source":source,
                       "normal_coordinates_embedded_without_rescaling":True}
            cyclic=vector(rows(mat(self.points[z]["inverse_Krylov_matrix_mod_prime"])*mat([[x] for x in normal])),272)
            value=self.put(name,{
                "prime":P,"z0":z,"role":key,"source_exact_leaf":source,
                "source_original_normal_V3_fibre":self.inputs["original_normal_V3_fibres"][z],
                "source_original_Krylov_point":self.inputs["original_Krylov_points"][z],
                "normal_coordinates_mod_prime":normal,"cyclic_coordinates_mod_prime":cyclic,
                "exact_fibre_value_definition":exact,"original_section_scalar_rescaled":False})
        return A.unpack(value["cyclic_coordinates_mod_prime"]),self.refs[name]
    def inverse(self,z,key,A,sources,compute):
        name=f"node-{z}-unit-{key}"
        old=self.old(name)
        if old is None:
            self.budget()
            value=compute()
            try:
                inverse,proof=A.inverse(value,key)
            except self.AH.UnitFailure as exc:
                self.put(name,{"prime":P,"z0":z,"accepted":False,
                    "source_values":sources,"whole_Artin_unit_witness":exc.witness,
                    "failure_only_this_complete_fibre_DAG_evaluation":True})
                raise
            old=self.put(name,{"prime":P,"z0":z,"accepted":True,
                "source_values":sources,"whole_Artin_unit_witness":proof,
                "inverse_cyclic_coordinates_mod_prime":A.pack(inverse),
                "all_factors_and_multiplicities_retained":True})
        assert old["source_values"]==sources
        if not old["accepted"]:
            raise self.AH.UnitFailure(key,old["whole_Artin_unit_witness"])
        return A.unpack(old["inverse_cyclic_coordinates_mod_prime"]),self.refs[name]
    def scalar_value(self,z,key,A,compute,sources,definition):
        name=f"node-{z}-value-{key}"
        value=self.old(name)
        if value is None:
            self.budget()
            raw=compute()
            value=self.put(name,{"prime":P,"z0":z,"role":key,
                "source_values":sources,"cyclic_coordinates_mod_prime":A.pack(raw),
                "exact_value_definition":definition,"original_scalars_preserved":True})
        assert value["source_values"]==sources
        return A.unpack(value["cyclic_coordinates_mod_prime"]),self.refs[name]
    def QN(self,z,A):
        name=f"node-{z}-complete-QN-value"
        old=self.old(name)
        if old is not None:
            assert old["source_original_QN"]==self.inputs["marked_QN"]
            return A.unpack(old["cyclic_coordinates_mod_prime"]),self.refs[name]
        qC,qCr=self.element(z,"qC",A)
        qchi,qchir=self.element(z,"qchi",A)
        qchii,qchiir=self.inverse(z,"qchi",A,[qchir],lambda:qchi)
        common,commonr=self.scalar_value(z,"common-qC-over-qchi4",A,
            lambda:A.mul(qC,A.power(qchii,4)),[qCr,qchir,qchiir],
            {"operation":"qC_over_qchi_fourth","original_tau_degrees":[2,2]})
        orbit=A.one;orbitrefs=[]
        for j in range(7):
            a,ar=self.element(z,"a"+str(j),A)
            v,vr=self.element(z,"v"+str(j),A)
            vi,vir=self.inverse(z,"v"+str(j),A,[vr],lambda:v)
            value,value_ref=self.scalar_value(z,"original-Qtilde-"+str(j),A,
                lambda:A.mul(A.power(A.mul(a,vi),3),common),[ar,vr,vir,commonr],
                {"operation":"positive_original_Qtilde","source_principal":self.orbit_principals[j]})
            orbit=A.mul(orbit,value);orbitrefs.append(value_ref)
        orbit,orbref=self.scalar_value(z,"original-Q-orbit",A,lambda:orbit,orbitrefs,
            {"operation":"product_all_seven_original_constant_field_Qtilde","source":self.inputs["marked_QN"]})
        fs={key:(A.one,None) for key in ("H","Cstar","X","D0","D1","D2","D3","D4","D5","D6")}
        for label,left,right,record in self.flip_records:
            q,qr=self.element(z,"q-"+label,A)
            lv,lr=fs[left];rv,rr=fs[right]
            inv,ir=self.inverse(z,"F-"+label,A,[qr,lr,rr],lambda:A.mul(A.mul(q,lv),rv))
            fv,fr=self.scalar_value(z,"F-"+label,A,lambda:inv,[qr,lr,rr,ir],
                {"operation":"inverse_of_product","source_original_principal":record["principal"],
                 "left_label":left,"right_label":right,"same_parent_kept_twice":left==right})
            fs[label]=(fv,fr)
        terminal,fr=fs["DN"];answer=A.mul(orbit,terminal)
        self.budget()
        normal=vector(rows(mat(self.points[z]["Krylov_matrix_mod_prime"])*mat([[x] for x in A.pack(answer)])),272)
        old=self.put(name,{"prime":P,"z0":z,"source_original_QN":self.inputs["marked_QN"],
            "source_orbit_value":orbref,"source_terminal_F_value":fr,
            "source_complete_characteristic_polynomial":self.inputs["original_characteristic_nodes"][z],
            "source_original_Krylov_point":self.inputs["original_Krylov_points"][z],
            "cyclic_coordinates_mod_prime":A.pack(answer),"normal_coordinates_mod_prime":normal,
            "all_required_denominators_are_units_on_complete272_algebra":True,
            "QN_itself_inverted_or_assumed_unit":False,
            "original_16_flips_or_characteristic_relation_recomputed":False})
        return answer,self.refs[name]
    def base_fibre(self,z):
        name=f"node-{z}-original-terminal-WN-fibre"
        value=self.old(name)
        if value is None:
            self.budget()
            E=mat(self.fibres[z]["normal_evaluation_mod_prime"])
            CE=mat(self.fibres[z]["cyclic_evaluation_mod_prime"])
            ev=E*self.BN;cev=CE*self.BN
            value=self.put(name,{
                "prime":P,"z0":z,"source_complete_DN_normal418":self.inputs["terminal_normal418"],
                "source_original_normal_V3_fibre":self.inputs["original_normal_V3_fibres"][z],
                "source_original_Krylov_point":self.inputs["original_Krylov_points"][z],
                "normal_evaluation_mod_prime":rows(ev),"cyclic_evaluation_mod_prime":rows(cev),
                "matrix_shape":[272,418],"original_QN_factor_included":False})
        self.base_fibres[str(z)]=self.refs[name]
        return value,self.refs[name]
    def evaluate_node(self,z):
        name=f"node-{z}-decision"
        decision=self.old(name)
        if decision is not None:
            return decision,self.refs[name]
        self.phase=f"whole-fibre-{z}";self.budget()
        A=self.algebra(z)
        try:
            QN,qr=self.QN(z,A)
        except self.AH.UnitFailure as exc:
            decision=self.put(name,{"prime":P,"z0":z,"accepted":False,
                "failure_label":exc.label,"failure_witness":exc.witness,
                "whole_Artin_fibre_preserved":True,"geometric_nonexistence_concluded":False,
                "source_characteristic_node":self.inputs["original_characteristic_nodes"][z]})
            return decision,self.refs[name]
        base,br=self.base_fibre(z)
        evalname=f"node-{z}-K-coordinate-function-evaluation"
        value=self.old(evalname)
        if value is None:
            self.budget()
            cyclic=base["cyclic_evaluation_mod_prime"]
            columns=[]
            for j in range(DIM):
                if j%32==0:self.budget()
                columns.append(A.pack(A.mul(QN,A.element([cyclic[i][j] for i in range(N)]))))
            multiplied=mat(columns).transpose()
            normal=mat(self.points[z]["Krylov_matrix_mod_prime"])*multiplied
            value=self.put(evalname,{"prime":P,"z0":z,
                "source_original_QN_value":qr,"source_original_WN_fibre":br,
                "source_original_characteristic_node":self.inputs["original_characteristic_nodes"][z],
                "source_original_Krylov_point":self.inputs["original_Krylov_points"][z],
                "matrix_mod_prime":rows(normal),"cyclic_matrix_mod_prime":rows(multiplied),
                "matrix_shape":[272,418],"row_labels":[[z,i] for i in range(N)],
                "original_QN_factor_included":True,
                "exact_function_definition":"original Q_N times each original W_N column",
                "coordinates_in_original_K_defined_normal_basis":True,
                "all_complete272_coordinates_preserved":True})
        decision=self.put(name,{"prime":P,"z0":z,"accepted":True,
            "complete_evaluation":self.refs[evalname],
            "source_original_QN_value":qr,"source_original_WN_fibre":br,
            "actual_row_count":272,"no_automatic_injectivity_assumed":True})
        return decision,self.refs[name]
    def profile(self):
        zs=list(self.accepted_nodes)
        name="evaluation-profile-nodes-"+"-".join(map(str,zs))
        value=self.old(name)
        evalrefs=[];data=[];labels=[]
        for z in zs:
            v=self.old(f"node-{z}-K-coordinate-function-evaluation")
            assert v is not None
            evalrefs.append(self.refs[f"node-{z}-K-coordinate-function-evaluation"])
            data.extend(v["matrix_mod_prime"]);labels.extend(v["row_labels"])
        H=mat(data)
        if value is None:
            self.budget()
            reduced,rank=H.transpose().rref()
            selected=pivots(reduced,rank)
            payload={"prime":P,"source_complete_evaluations":evalrefs,"nodes":zs,
                "matrix_shape":[len(data),DIM],"all_row_labels":labels,
                "actual_rank":rank,"required_rank":DIM,"accepted":rank==DIM,
                "selected_row_indices":selected,"selected_row_labels":[labels[i] for i in selected],
                "no_dimension_or_degree_shortcut_used_for_this_evaluation":True}
            if rank==DIM:
                square=sub(H,selected,list(range(DIM)))
                inverse=square.inv()
                assert square*inverse==eye(DIM) and inverse*square==eye(DIM)
                determinant=int(square.det());assert determinant
                transformed=H*inverse
                assert sub(transformed,selected,list(range(DIM)))==eye(DIM)
                payload.update({
                    "selected_square_mod_prime":rows(square),
                    "selected_inverse_mod_prime":rows(inverse),
                    "actual_selected_minor_determinant_mod_prime":determinant,
                    "both_selected_inverse_products_verified":True,
                    "complete_normalized_evaluation_mod_prime":rows(transformed),
                    "all_computed_rows_multiplied_by_same_inverse":True,
                    "selected_coordinates_of_all418_normalized_functions_are_identity":True,
                    "exact_inverse_definition":{"operation":"inverse_of_original_K_coordinate_evaluation",
                        "source_original_QN":self.inputs["marked_QN"],
                        "source_original_WN":self.inputs["terminal_normal418"],
                        "selected_rows":[labels[i] for i in selected],
                        "all_original_columns_in_original_order":list(range(DIM)),
                        "actual_unit_minor":determinant}})
            value=self.put(name,payload)
            del reduced;gc.collect()
        assert value["source_complete_evaluations"]==evalrefs
        self.rank=value["actual_rank"]
        if value["accepted"]:
            self.selected_rows=value["selected_row_labels"]
            self.accepted_profile=self.refs[name]
        self.checkpoint("evaluation-rank-"+str(self.rank))
        return value,H,self.refs[name]
    def normalize(self,profile,H,profile_ref):
        inverse=mat(profile["selected_inverse_mod_prime"])
        name="K-fixed-normal418-basis"
        value=self.old(name)
        if value is None:
            self.budget()
            changed=self.BN*inverse
            value=self.put(name,{"prime":P,"matrix_shape":[690,418],
                "normal_V3_basis":[list(x) for x in self.V3],
                "normal_V3_basis_mod_prime":rows(changed),
                "source_original_DN_normal418":self.inputs["terminal_normal418"],
                "source_selected_evaluation_inverse":profile_ref,
                "source_original_QN":self.inputs["marked_QN"],
                "exact_fixed_functions_DAG":{
                    "operation":"positive_multiply_original_QN",
                    "original_QN_source":self.inputs["marked_QN"],
                    "normal_sections":{"operation":"right_multiply_original_WN_basis",
                        "source_original_WN":self.inputs["terminal_normal418"],
                        "exact_basis_change_unit_solve":profile["exact_inverse_definition"]}},
                "fixed_function_space":"H0(2H-T_f^0) over original K",
                "normal_sections_without_QN_claimed_K_fixed":False,
                "all418_original_K_fixed_functions_certified":True,
                "proof_of_fixedness":"K-linear selected-coordinate isomorphism; each normalized column has rational identity coordinates",
                "old_basis_descent_matrix_exact_DAG":{"operation":"A_inverse_times_sigma_A",
                    "A_definition":profile["exact_inverse_definition"],
                    "sigma":"original constant-field Gal(L/K) generator",
                    "old_basis_multiplier":"sigma(Q_N)/Q_N"},
                "new_fixed_basis_descent_matrix":{"operation":"identity_matrix","dimension":418},
                "new_fixed_basis_action_identity_certified_by_uniqueness":True,
                "sevenfold_cocycle_certified_by_exact_telescoping":True,
                "old_descent_matrix_numeric_arrays_computed":False,
                "six_Galois_replays_or_old_16_flips_computed":False,
                "characteristic_zero_normal_coefficients_expanded":False,
                "Q_fixed_basis_asserted":False})
        shape(value["normal_V3_basis_mod_prime"],690,418)
        self.fixed_basis_ref=self.refs[name]
        self.fixed_basis=mat(value["normal_V3_basis_mod_prime"])
        self.checkpoint("complete-original-K-fixed418-basis")
        self.P0_leading()
        for z in self.accepted_nodes:
            self.normalized_fibre(z,inverse)
    def P0_leading(self):
        name="original-P0-leading-row"
        value=self.old(name)
        if value is None:
            self.budget()
            row=mat([self.point_row])*self.fixed_basis
            plain_values=rows(row)[0]
            rho=int(self.marked["actual_QN_rho_leading_mod_prime"])
            t=int(self.marked["actual_QN_t_leading_mod_prime"])
            rho_values=[rho*x%P for x in plain_values]
            t_values=[t*x%P for x in plain_values]
            first=next((j for j,x in enumerate(t_values) if x),None)
            value=self.put(name,{"prime":P,"source_K_fixed_normal_basis":self.fixed_basis_ref,
                "source_original_P0_functional":self.inputs["original_neutral"],
                "source_original_QN":self.inputs["marked_QN"],
                "source_original_t_frame":self.inputs["original_t_frame"],
                "normal_V3_P0_functional_mod_prime":self.point_row,
                "normal_V3_P0_values_mod_prime":plain_values,
                "rho_leading_coefficients_mod_prime":rho_values,
                "t_leading_coefficients_mod_prime":t_values,
                "actual_QN_rho_leading_mod_prime":rho,"actual_QN_t_leading_mod_prime":t,
                "actual_original_c_power8435_mod_prime":self.marked["actual_original_c_power8435_mod_prime"],
                "original_rho_and_t_order":-8435,"first_unit_column":first,
                "actual_marked_P0_unit_column_certified":first is not None,
                "selected_column_rescaled":False,"old_point_jets_or_t_constant_recomputed":False,
                "exact_selected_function_definition":None if first is None else {
                    "operation":"unchanged_column_of_original_K_fixed_function_basis",
                    "source_basis":self.fixed_basis_ref,"column":first,
                    "exact_P0_pole_order":8435},
                "exact_leading_definition":"original QN leading times original P0 functional times B_N A^-1",
                "characteristic_zero_nonzero_row_not_used_to_assume_modular_unit":True})
        self.point_ref=self.refs[name]
        self.checkpoint("original-P0-leading-row-retained")
    def normalized_fibre(self,z,inverse):
        name=f"node-{z}-normalized-regular-V3-space-fibre"
        value=self.old(name)
        base,br=self.base_fibre(z)
        if value is None:
            self.budget()
            normal=mat(base["normal_evaluation_mod_prime"])*inverse
            cyclic=mat(base["cyclic_evaluation_mod_prime"])*inverse
            value=self.put(name,{"prime":P,"z0":z,"matrix_shape":[272,418],
                "source_K_fixed_normal_basis":self.fixed_basis_ref,
                "source_original_WN_fibre":br,
                "source_selected_evaluation_inverse":self.accepted_profile,
                "source_original_normal_V3_fibre":self.inputs["original_normal_V3_fibres"][z],
                "source_original_Krylov_point":self.inputs["original_Krylov_points"][z],
                "normal_evaluation_mod_prime":rows(normal),"cyclic_evaluation_mod_prime":rows(cyclic),
                "original_QN_factor_included":False,
                "exact_values":"regular normal V3 sections w*A_inverse, not Q_N*w*A_inverse",
                "same_new_basis_change_applied_to_existing_WN_fibre":True,
                "old_normal_V3_fibre_or_Krylov_inverse_recomputed":False})
        assert value["original_QN_factor_included"] is False
        self.normalized_fibres[str(z)]=self.refs[name]
        self.checkpoint("normalized-regular-fibre-"+str(z))
    def inventory(self):
        entries=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name==PREFIX+"current.json.gz" or path.name.startswith(PREFIX+"stage-manifest-"):
                continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
            entries.append(spec(path))
        payload={"result":RESULT,"configuration":self.tag,"complete":True,"files":entries,
                 "current_excluded":True,"no_closed_live_source_removed":True}
        path=self.path("stage-manifest-"+fingerprint(payload))
        if path.exists():assert read(path)==payload
        else:save(path,payload)
        return spec(path),len(entries)
    def finish(self,complete,reason):
        self.checkpoint("completed" if complete else self.phase)
        inventory,count=self.inventory()
        point=self.own(self.point_ref) if self.point_ref is not None else None
        if complete:
            assert self.fixed_basis_ref is not None and self.rank==418 and self.point_ref is not None
        result={"result":RESULT,"configuration":self.tag,"complete":bool(complete),
            "p":41,"actual_auxiliary_prime":P,"source_audit":self.refs.get("original-source-audit"),
            "node_decisions":self.node_decisions,"actual_usable_fibre_nodes":self.accepted_nodes,
            "actual_evaluation_rank":self.rank,"actual_selected_row_labels":self.selected_rows,
            "selected_evaluation_inverse":getattr(self,"accepted_profile",None),
            "complete_K_fixed_normal_basis":self.fixed_basis_ref,
            "original_P0_leading_row":self.point_ref,
            "all418_original_K_fixed_functions_certified":self.fixed_basis_ref is not None,
            "new_fixed_basis_descent_identity_certified":self.fixed_basis_ref is not None,
            "old_basis_descent_matrix_numeric_arrays_computed":False,
            "original_marked_P0_unit_column_certified":bool(point and point["actual_marked_P0_unit_column_certified"]),
            "actual_first_P0_unit_column":point["first_unit_column"] if point else None,
            "completed_normalized_space_fibres":self.normalized_fibres,
            "original_normal_V3_fibres":self.inputs["original_normal_V3_fibres"],
            "original_Krylov_points":self.inputs["original_Krylov_points"],
            "original_W":self.inputs["original_W"],"marked_QN":self.inputs["marked_QN"],
            "source_inputs":self.inputs,"source_identities":{g:identity(self.item["sources"][g]) for g in GROUPS},
            "original_QN_and_selected_scalars_rescaled":False,
            "old_sixteen_flips_or_six_Galois_replays_computed":False,
            "old_charpoly_Krylov_V3_evaluations_point_jets_or_t_constant_recomputed":False,
            "characteristic_zero_coefficients_reconstructed":False,
            "Q_fixed_basis_K_defined_effective272_representative_or_height_computed":False,
            "actual_retained_complete_math_stage_count":count,"stage_manifest":inventory,
            "resume_state":self.current,"stop_reason":reason,"seconds":time.monotonic()-self.started}
        save(self.out/FINAL,result)
        return result
    def run(self):
        self.prepare()
        for z in range(7):
            self.budget()
            decision,ref=self.evaluate_node(z)
            self.node_decisions.append(ref)
            if decision["accepted"]:
                self.accepted_nodes.append(z)
            self.checkpoint("node-"+str(z)+"-decided")
            if len(self.accepted_nodes)<3:
                continue
            profile,H,pref=self.profile()
            if profile["accepted"]:
                self.normalize(profile,H,pref)
                return self.finish(True,None)
            del H;gc.collect()
        return self.finish(False,"all_seven_original_nodes_decided_without_a_unit418_coordinate_minor")

def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise SystemExit("R899 new mathematics runs only in the authorized public repository Actions")
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    parser.add_argument("--config",required=True);parser.add_argument("--retained",required=True)
    parser.add_argument("--output",required=True);parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args();started=time.monotonic();out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    job=None;certificate=None;error=None;code=0
    try:
        job=Job(args);certificate=job.run()
        if not certificate["complete"]:code=2
    except BudgetStop as exc:
        error=str(exc);code=124
        if job is not None:certificate=job.finish(False,error)
    except Exception as exc:
        error={"type":type(exc).__name__,"message":str(exc)};code=1;traceback.print_exc()
        if job is not None:
            try:certificate=job.finish(False,error)
            except Exception:traceback.print_exc()
    receipt={"result":RESULT,"source_sha256":sha(__file__),
        "complete":bool(certificate and certificate["complete"]),
        "configuration_sha256":fingerprint(job.tag) if job is not None else None,
        "certificate_sha256":sha(out/FINAL) if certificate is not None else None,
        "all418_original_K_fixed_functions_certified":bool(certificate and certificate["all418_original_K_fixed_functions_certified"]),
        "actual_evaluation_rank":certificate["actual_evaluation_rank"] if certificate else None,
        "original_marked_P0_unit_column_certified":bool(certificate and certificate["original_marked_P0_unit_column_certified"]),
        "actual_first_P0_unit_column":certificate["actual_first_P0_unit_column"] if certificate else None,
        "old_math_recomputed":False,"exit_code":code,"error":error,"seconds":time.monotonic()-started}
    save(out/"core-receipt.json",receipt)
    print("R899_CORE_SUMMARY="+json.dumps(receipt,sort_keys=True),flush=True)
    return code
if __name__=="__main__":
    raise SystemExit(main())

