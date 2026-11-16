#!/usr/bin/env python3
"""R893: original five positive sum-Hom full-fibre initial RR kernels.
All new arithmetic is restricted to this public repository's Actions.
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
from fractions import Fraction
import flint
from flint import nmod_mat, nmod_poly

REPOSITORY="Rogerhu12/math-research-public"
RESULT="R893-original-five-sum-Hom-complete-initial-RR"
FINAL="p41-original-five-sum-Hom-complete-initial-RR-certificate.json"
PREFIX="R893-"
MANIFEST="full-outputs-manifest.json"
P=1000000753
N=272
EPS=[0]+[1]*144+[2]*127
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
MANDATORY=("R880","R877","R809","R849","R827","R885")
DEGREES=[2970,1674,1800,3024,3339]
POWERS=[12,8,8,13,14]
FIBRES=[23,15,15,25,27]
RESIDUAL_DEGREES=[294,502,376,512,469]
DIMENSIONS=[168,376,250,386,343]
PADDING=[250,42,168,32,75]
FIELD_BASIS="b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b"
STRATEGY={
 "original_curve":"original Y of genus127, level82, original minus3 descent",
 "original_Hom_words":["1+T^"+str(j) for j in range(1,6)],
 "prime":P,"original_s_root":99932770,"original_zeta_root":549966761,
 "original_integral_B_root":3197390,"canonical_free_column":1186,
 "normal_basis_degrees":EPS,"original_sigma_branch_order":[0,6,1,2,4,3,5],
 "Cj_semantics":"theta*U_j/tau^4=h_Tjf/h_f times C0; original rho phase already included",
 "Cj_scale":"each original field numerator/denominator times its own rational scale exactly once",
 "normal_derivative":"Gamma*a+Mg*partial_z(a), original tau operators",
 "same_target_conjugate":"C=rho_j^-3*sigma^j(A), D=sigma^j(B)",
 "single_denominator":"Q=B*D^3*(Cj*(C^2-bD^2)*W-C0*(A^2-bB^2)*Wj)^3",
 "single_numerator":"-A*D^3*Delta^3+Xi*D^2*Delta^2*(2*S+R)-Xi^3*C0^3*F^2*Wj^3",
 "common_homogeneous_weight":98,"direct_sigma_formula_weight":95,
 "true_weight98_sigma_transport":"multiply direct sigma formula by t^3; normal beta_i by t^epsilon_i",
 "whole_fibre_dimension":272,"characteristic_polynomial":"completed original R885, never recomputed",
 "node_schedule":"least nonnegative integers, old source-bound Krylov points reused",
 "only_denominator_unit_test":"Q in the whole degree272 Artin algebra; no factor removal",
 "initial_powers":POWERS,"original_pole_degrees":DEGREES,
 "required_complete_fibres":FIBRES,"residual_degrees":RESIDUAL_DEGREES,
 "complete_initial_kernel_dimensions":DIMENSIONS,"future_padding":PADDING,
 "normal_basis_order":"(i,k), i=0..271, k=0..n-epsilon_i",
 "A_elimination":"three scalar Vandermonde lengths n+1,n,n-1",
 "Schur_sign":"H_complement-Lambda*H_selected; H=Y*E",
 "minor_selection":"left-to-right RREF pivots of S^t choose original rows, then RREF chooses columns",
 "kernel_coordinates":"all nonpivot normal columns are free identity; pivot=-minor^-1*free",
 "complete_checks":"all Schur rows, all N*272 original A-yB rows, free identity",
 "exact_output":"source-bound characteristic-zero unit-solve expression and its actual modular reduction",
 "initial_nodes_are_not_generic_V2n_injection":True,
 "marked_pair_padding_or_five_Lj128_computed":False,
 "budget_node_limit_requested_directions_and_transport_excluded_from_identity":True
}

class BudgetStop(RuntimeError):
    pass
class ScopeStop(RuntimeError):
    pass
class UnitFailure(RuntimeError):
    pass

def guard():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise SystemExit("New mathematics belongs only to the specified public repository Actions.")
def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for part in iter(lambda:stream.read(4*1024*1024),b""):
            h.update(part)
    return h.hexdigest()
def read(path):
    path=Path(path)
    with (gzip.open if path.suffix==".gz" else open)(path,"rt",encoding="utf-8") as stream:
        return json.load(stream)
def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+".tmp")
    raw=(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n").encode()
    if path.suffix==".gz":
        with temporary.open("wb") as stream:
            with gzip.GzipFile(filename="",fileobj=stream,mode="wb",mtime=0,compresslevel=2) as zipped:
                zipped.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)
def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def plain(row):
    value={key:row[key] for key in ("file","bytes","sha256")}
    p=PurePosixPath(value["file"])
    assert len(p.parts)==1 and p.name not in ("",".","..") and "\\" not in value["file"]
    assert isinstance(value["bytes"],int) and value["bytes"]>=0
    return value
def spec(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}
def identity(source):
    answer={**{key:source[key] for key in BASE},
        "configuration_sha256":source["configuration_sha256"],
        "selected_files_sha256":fingerprint(source["files"])}
    if source.get("certificate") is not None:
        answer["certificate"]=plain(source["certificate"])
    else:
        answer["configuration_stage"]=plain(source["configuration_stage"])
    return answer
def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
        "method_sha256":item["method_sha256"],"proofs":item["proofs"],
        "sources":{key:identity(item["sources"][key]) for key in sorted(item["sources"])},
        "inputs":item["inputs"],"strategy":STRATEGY}
def matrix(raw):
    return nmod_mat(raw,P)
def rows(a):
    return [[int(a[i,j]) for j in range(a.ncols())] for i in range(a.nrows())]
def shape(raw,m,n):
    assert len(raw)==m and all(len(row)==n for row in raw),(m,n)
def zero(m,n):
    return nmod_mat(m,n,P)
def eye(n):
    return matrix([[int(i==j) for j in range(n)] for i in range(n)])
def sub(a,I,J):
    return matrix([[int(a[i,j]) for j in J] for i in I])
def pivots(a,rank):
    out=[next(j for j in range(a.ncols()) if a[i,j]) for i in range(rank)]
    assert out==sorted(set(out))
    return out
def positions(n):
    return [(i,k) for i in range(N) for k in range(n-EPS[i]+1)]
def poly(raw):
    return nmod_poly([int(x)%P for x in raw],P)
def pack(a,n=None):
    size=max(0,a.degree()+1) if n is None else n
    return [int(a[i]) for i in range(size)]
def value(raw,a):
    ans=0
    for c in reversed(raw):
        ans=(ans*a+int(c))%P
    return ans
def inverse(value0,context):
    v=int(value0)%P
    if v==0:
        raise UnitFailure("Nonunit fixed-place scalar: "+context)
    return pow(v,-1,P)
def rational_mod(pair,context):
    if isinstance(pair,(str,int)):
        q=Fraction(pair);n,d=q.numerator,q.denominator
    else:
        assert isinstance(pair,list) and len(pair)==2
        n,d=map(int,pair)
    return n%P*inverse(d,context)%P
def rational_polynomial(record,b,context):
    assert isinstance(record,dict) and set(record)>={"numerator","denominator"}
    assert len(record["numerator"])<=7
    return value(record["numerator"],b)*inverse(record["denominator"],context)%P
def original_QK(record,b,context):
    assert isinstance(record,list) and len(record)==2
    return (rational_polynomial(record[0],b,context+" real")+
            549966761*rational_polynomial(record[1],b,context+" zeta"))%P
def same_origin(left,right):
    assert all(str(left[key])==str(right[key]) for key in BASE)

class Source:
    def __init__(self,label,item,root):
        self.label=label;self.item=item;self.folder=Path(root)/label;self.checked=set()
        self.files={name:plain(row) for name,row in item["files"].items()}
        path=self.folder/MANIFEST
        assert sha(path)==item["manifest_sha256"]
        manifest=read(path);assert manifest["result"]==item["result"]
        inventory={row["file"]:plain(row) for row in manifest["files"]}
        assert len(inventory)==len(manifest["files"])
        inventory[MANIFEST]=spec(path)
        for name,row in self.files.items():
            assert name==row["file"]
            if name!="full-outputs-manifest-reference.json":
                assert inventory[name]==row,(label,name)
        initial=self.raw("public-actions-input.json");run=self.raw("run-receipt.json")
        assert initial["source_commit"]==run["source_commit"]==item["source_commit"]
        assert str(run["workflow_run_id"])==str(item["run_id"])
        original_core=initial.get("core_sha256",initial.get("job",{}).get("core_sha256"))
        assert original_core==item["core_sha256"]
        self.certificate=None
        if item.get("certificate") is not None:
            self.certificate=self.raw(item["certificate"]["file"])
            assert self.files[item["certificate"]["file"]]==plain(item["certificate"])
            assert self.certificate["result"]==item["result"] and self.certificate["complete"] is True
            assert run["complete"] is True and run["process_exit_code"]==0
            self.tag=self.certificate["configuration"]
        else:
            assert run["complete"] is False
            assert run["process_exit_code"] in item["accepted_process_exit_codes"]
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
        ans=self.raw(row["file"])
        assert ans["complete"] is True and ans["configuration"]==self.tag
        return ans
    def ref(self,row):
        assert self.files[row["file"]]==plain(row)
        return {"source_group":self.label,**plain(row)}

class Job:
    def __init__(self,args):
        self.started=time.monotonic();self.args=args
        self.item=read(args.config);self.out=Path(args.output);self.out.mkdir(parents=True,exist_ok=True)
        assert self.item["result"]==RESULT and self.item["p"]==41
        assert self.item["producer_inputs_pending"] is False
        assert sha(__file__)==self.item["core_sha256"] and flint.__version__=="0.9.0"
        topic=Path(__file__).resolve().parent.parent
        assert sha(topic/self.item["method"])==self.item["method_sha256"]
        for entry in self.item["proofs"].values():
            assert sha(topic/entry["path"])==entry["sha256"]
        assert set(MANDATORY)<=set(self.item["sources"])
        self.tag=expected_tag(self.item)
        self.sources={g:Source(g,item,args.retained) for g,item in self.item["sources"].items()}
        self.inputs=self.item["inputs"];self.refs={};self.done={};self.node_outcomes={}
        self.phase="source_initialization";self.current=None
        self.requested=self.item.get("requested_directions",[1,2,3,4,5])
        assert self.requested and self.requested==sorted(set(self.requested))
        assert all(isinstance(j,int) and 1<=j<=5 for j in self.requested)
        self.node_limit=int(self.item.get("maximum_node_attempts",128))
        assert 27<=self.node_limit<P
        self.known_points={};self.fibre_cache={};self.derivative_specs={}
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
        value0=read(path)
        assert value0["result"]==RESULT and value0["configuration"]==self.tag and value0["complete"] is True
        self.refs[name]=spec(path)
        return value0
    def put(self,name,payload):
        assert not set(payload)&{"result","configuration","complete"}
        v={"result":RESULT,"configuration":self.tag,"complete":True,**payload}
        path=self.path(name)
        if path.exists():
            assert read(path)==v
        else:
            save(path,v)
        self.refs[name]=spec(path)
        print("R893_STAGE="+json.dumps({"file":path.name,"seconds":time.monotonic()-self.started}),flush=True)
        return v
    def checkpoint(self,phase):
        self.phase=phase
        current={"result":RESULT,"configuration":self.tag,"complete":False,
            "phase":phase,"completed_directions":self.done,"node_outcomes":self.node_outcomes,
            "completed_stages":self.refs}
        save(self.path("current"),current);self.current=spec(self.path("current"))
        return self.current
    def source(self,row):
        return self.sources[row["source_group"]].stage(row)
    def input(self,key):
        return self.source(self.inputs[key])
    def own(self,row):
        path=self.out/row["file"];assert spec(path)==plain(row)
        v=read(path)
        assert v["result"]==RESULT and v["configuration"]==self.tag and v["complete"] is True
        return v
    def prepare(self):
        self.phase="source_audit";self.budget()
        graph=self.input("global_DAG");self.graph=graph
        assert graph["global_y_exact_unit_expression_defined"] is True
        assert graph["five_original_addition_pole_ideals_as_fractional_DAGs_certified"] is True
        assert graph["all_three_minor_formulas_are_exact_DVR_ideal_equalities"] is True
        assert plain(self.sources["R849"].certificate["exact_expression_DAG"])==plain(self.inputs["global_DAG"])
        self.field=graph["original_field"]
        nodes={x["id"]:x for x in graph["graph_nodes"]}
        assert len(nodes)==len(graph["graph_nodes"])
        gal=nodes[graph["original_Galois_automorphism_node"]]
        assert gal["operation"]=="original_Galois_automorphism_definition"
        assert gal["data"]["fixes_zeta"] and gal["data"]["fixes_original_z_w_and_normal_basis"]
        self.place=self.input("original_place")
        assert self.place["prime"]==P and self.place["original_branch"]==0
        assert self.place["canonical_free_column"]==1186
        assert self.place["original_field"]==self.field
        assert self.place["original_integral_B_root"]==3197390
        assert self.place["original_zeta_root"]==549966761 and self.place["original_s_root"]==99932770
        assert self.place["original_lambda_is_a_unit"] is True
        assert self.place["original_minimal_polynomials_and_simple_residue_roots_verified"] is True
        self.b=int(self.place["original_b_root"])
        self.lam=rational_mod(self.field["lambda"],"original lambda")
        assert self.lam and self.lam*self.b%P==3197390
        self.rho={}
        for j,degree in enumerate(DEGREES,1):
            output=graph["five_original_polar_and_eta_outputs"][str(j)]
            assert output["original_Hom_word"]=="1+T^"+str(j)
            assert int(output["original_map_degree"])==degree
            assert set(output["global_pole_ideals"])=={"tau","sigma"}
            rho_id=graph["relative_original_functions"][str(j)]["rho"]
            node=nodes[rho_id]
            assert node["operation"]=="original_R791_rho_iterate" and node["data"]["original_index"]==j
            self.rho[j]=original_QK(node["data"]["source_value"],self.b,"rho"+str(j))
            assert self.rho[j]
        seven=self.input("seven_normal_inputs")
        self.seven=seven
        assert plain(self.sources["R880"].certificate["seven_Galois_normal_inputs"])==plain(self.inputs["seven_normal_inputs"])
        assert self.sources["R880"].certificate["all1380_by12_original_coordinates_verified"] is True
        assert self.sources["R880"].certificate["all_seven_original_Galois_normal_inputs_certified"] is True
        assert seven["normal_basis_degrees"]==EPS and seven["regular_degree_bound"]==5
        assert seven["all_seven_original_Galois_normal_inputs_certified"] is True
        assert plain(seven["source_original_global_DAG"])==plain(self.inputs["global_DAG"])
        ordered=seven["ordered_original_sigma_powers"]
        assert [r["sigma_power"] for r in ordered]==list(range(7))
        assert [r["original_branch"] for r in ordered]==STRATEGY["original_sigma_branch_order"]
        self.normal=[];self.normal_refs=[]
        A0=self.input("zero_branch_A");B0=self.input("zero_branch_B")
        for data in (A0,B0):
            assert data["prime"]==P and data["original_branch"]==0
            assert data["canonical_free_column"]==1186 and data["normal_basis_degrees"]==EPS
            assert data["regular_degree_bound"]==5 and data["all1380_original_short_coordinates_verified"] is True
            assert data["same_original_82power10_scales_preserved"] is True
        assert plain(ordered[0]["source_original_A_normal"])==plain(self.inputs["zero_branch_A"])
        assert plain(ordered[0]["source_original_B_normal"])==plain(self.inputs["zero_branch_B"])
        self.normal.append([A0["vector_coefficients_mod_prime"],B0["vector_coefficients_mod_prime"]])
        self.normal_refs.append({"A":self.inputs["zero_branch_A"],"B":self.inputs["zero_branch_B"]})
        pair_refs=self.inputs["other_normal_pairs"]
        assert len(pair_refs)==6
        for j,row in enumerate(ordered[1:],1):
            ref=pair_refs[j-1];assert plain(ref)==plain(row["source_original_normal_pair"])
            pair=self.source(ref)
            assert pair["prime"]==P and pair["sigma_power"]==j
            assert pair["original_branch"]==row["original_branch"] and pair["roots_B_s"]==row["roots_B_s"]
            assert pair["normal_basis_degrees"]==EPS and pair["regular_degree_bound"]==5
            assert pair["all1380_original_coordinates_for_each_vector_verified"] is True
            assert pair["abstract_p_integral_original_normal_lifts_certified"] is True
            self.normal.append([pair["A_vector_coefficients_mod_prime"],pair["B_vector_coefficients_mod_prime"]])
            self.normal_refs.append({"A":ref,"B":ref})
        for j,pair in enumerate(self.normal):
            for part in pair:
                shape(part,6,N)
                assert all(int(part[k][i])==0 for k in range(6) for i in range(N) if k>5-EPS[i])
            if j:
                bj=int(ordered[j]["roots_B_s"][0])*inverse(self.lam,"lambda")%P
                if j<=5:
                    assert pow(self.rho[j],6,P)*self.b%P==bj
        self.Wsource=self.input("original_W")
        assert self.Wsource["prime"]==P and self.Wsource["original_rational_denominators_all_units"] is True
        self.W=[matrix(raw) for raw in self.Wsource["W_coefficients_mod_prime"]]
        assert len(self.W)==4 and all(a.nrows()==a.ncols()==N for a in self.W)
        characteristic=self.input("characteristic")
        assert characteristic["prime"]==P
        assert characteristic["exact_original_modular_characteristic_polynomial_certified"] is True
        assert characteristic["all273_nodes_for_all273_T_coefficients_verified"] is True
        assert plain(characteristic["source_original_W"])==plain(self.inputs["original_W"])
        self.chi=characteristic["coefficient_polynomials_ascending_z"]
        assert len(self.chi)==N+1 and self.chi[0]==[1]
        assert all(len(row)==k+1 for k,row in enumerate(self.chi))
        for ref in self.inputs["original_Krylov_points"]:
            point=self.source(ref)
            assert point["prime"]==P and point["usable"] is True
            assert point["both_inverse_products_verified"] is True and point["actual_cyclic_rank"]==N
            assert plain(point["source_original_W"])==plain(self.inputs["original_W"])
            z0=int(point["z0"]);assert z0 not in self.known_points
            shape(point["Krylov_matrix_mod_prime"],N,N)
            shape(point["inverse_Krylov_matrix_mod_prime"],N,N)
            self.known_points[z0]=(ref,point)
        assert set(range(8))<=set(self.known_points)
        self.operator_indexes={}
        for target,key in (("g","g_index"),("Gamma","Gamma_index")):
            index=self.input(key);assert index["target"]==target and index["chart"]=="tau"
            assert index["prime"]==P and index["normal_basis_degrees"]==EPS
            assert index["all_weighted_support_zeros_verified"] is True
            assert index["original_true_operator_reduction_certified"] is True
            assert len(index["row_blocks"])==17
            self.operator_indexes[target]=index
        self.operator_identity=self.input("operator_identity")
        assert self.operator_identity["prime"]==P
        for flag in ("g_first_column_is_original_vg",
                     "Gamma_first_column_zero_and_second_column_original_vh",
                     "g_commutator_full_polynomial_identity_certified_by_seven_points",
                     "Gamma_nested_full_polynomial_identity_certified_by_seven_points",
                     "all_sigma_negative_powers_and_original_minus_sign_verified",
                     "all_operators_are_true_original_p_integral_reductions"):
            assert self.operator_identity[flag] is True
        for target,key in (("g","g_index"),("Gamma","Gamma_index")):
            assert plain(self.operator_identity["operator_indexes"][target]["tau"])==plain(self.inputs[key])
        self.S5=self.input("S5_index")
        assert self.S5["dimension"]==1234 and self.S5["normal_basis_degrees"]==EPS
        assert self.S5["integer_scale"]=="13744803133596058624"
        self.mapping=[(r["normal_basis_index"],r["z_degree"]) for r in self.S5["basis_rows"]]
        assert self.mapping==positions(5)
        assert self.sources["R809"].certificate["coefficient_field_basis"]==FIELD_BASIS
        assert self.sources["R809"].certificate["original_b_model"]==self.field["original_b_minimal_polynomial"]
        assert plain(self.sources["R809"].certificate["S5_basis_index"])==plain(self.inputs["S5_index"])
        self.C_refs=self.inputs["C_indexes"]
        assert len(self.C_refs)==6
        for j,ref in enumerate(self.C_refs):
            assert plain(self.sources["R809"].certificate["normal_vectors"]["C"+str(j)])==plain(ref)
        self.reused_B={}
        for entry in self.inputs.get("completed_B_derivatives",[]):
            j=entry["sigma_power"];assert isinstance(j,int) and 0<=j<=6 and j not in self.reused_B
            self.reused_B[j]=entry["source"]
        name="original-source-audit"
        old=self.old(name)
        if old is None:
            self.put(name,{"prime":P,"original_b_root":self.b,"original_s_root":99932770,
                "original_zeta_root":549966761,"original_integral_B_root":3197390,
                "original_sigma_branch_order":[r["original_branch"] for r in ordered],
                "rho_iterates_mod_prime":{str(j):v for j,v in self.rho.items()},
                "source_original_global_DAG":self.inputs["global_DAG"],
                "source_original_seven_normal_inputs":self.inputs["seven_normal_inputs"],
                "source_original_pole_ideals":{str(j):graph["five_original_polar_and_eta_outputs"][str(j)]["global_pole_ideals"] for j in range(1,6)},
                "original_pole_degrees":DEGREES,
                "source_original_C_indexes":self.C_refs,
                "source_original_tau_operators":[self.inputs["g_index"],self.inputs["Gamma_index"],self.inputs["operator_identity"]],
                "source_original_W":self.inputs["original_W"],"source_completed_characteristic":self.inputs["characteristic"],
                "source_original_Krylov_points":self.inputs["original_Krylov_points"],
                "source_completed_B_derivatives":self.inputs.get("completed_B_derivatives",[]),
                "all_original_rational_scalars_used_here_are_units":True,
                "old_S5_or_fourier_or_seven_normal_solves_recomputed":False,
                "old_characteristic_polynomial_or_old_Krylov_inverses_recomputed":False,
                "original_positive_Hom_words_phase_and_twist_preserved":True})
        self.checkpoint("original_sources_bound")

    def hodge_reductions(self):
        self.C=[]
        for j,ref in enumerate(self.C_refs):
            name="C"+str(j)+"-original-Hodge-normal-reduction"
            prior=self.old(name)
            index=self.source(ref)
            assert index["target"]=="C"+str(j) and index["regular_degree_bound"]==4
            assert index["normal_basis_degrees"]==EPS
            assert index["normal_function"]=="theta*U_"+str(j)+"/tau^4"
            assert index["all14_original_field_columns_retained"] is True
            assert index["weighted_polynomial_support_verified"] is True
            assert index["literal_tau_factor_highest_S5_coefficients_zero"] is True
            assert plain(index["S5_basis_index"])==plain(self.inputs["S5_index"])
            assert index["target_configuration"]["original_b_model"]==self.field["original_b_minimal_polynomial"]
            assert len(index["coordinate_groups"])==2
            if prior is None:
                self.budget();normal=[[0]*N for _ in range(5)];columns=[];source_groups=[]
                for ref0 in index["coordinate_groups"]:
                    group_ref={"source_group":"R809",**plain(ref0)}
                    group=self.source(group_ref)
                    assert group["target_configuration"]==index["target_configuration"]
                    assert group["target"]=="C"+str(j)
                    assert group["coefficient_field_basis"]==FIELD_BASIS
                    assert group["all1380_original_coordinates_verified"] is True
                    assert group["original_field_and_scalar_normalizations_preserved"] is True
                    assert plain(group["S5_basis_index"])==plain(self.inputs["S5_index"])
                    indices=group["column_indices"];assert len(indices)==7
                    shape(group["coordinate_numerators"],1234,7)
                    assert len(group["column_denominators"])==len(group["original_target_rational_scales"])==7
                    coefficients=[]
                    for local,k in enumerate(indices):
                        scale=rational_mod(group["original_target_rational_scales"][local],"C original scale")
                        d=inverse(group["column_denominators"][local],"C original coordinate denominator")
                        phase=pow(self.b,k%7,P)*(99932770 if k>=7 else 1)%P
                        coefficients.append(scale*d*phase%P)
                    for row,(i,power) in enumerate(self.mapping):
                        numerator=group["coordinate_numerators"][row]
                        if power>4-EPS[i]:
                            assert all(int(x)==0 for x in numerator),("exact_C_weighted_zero",j,row)
                        else:
                            normal[power][i]=(normal[power][i]+sum(int(x)*c for x,c in zip(numerator,coefficients)))%P
                    columns.extend(indices);source_groups.append(group_ref)
                assert columns==list(range(14))
                prior=self.put(name,{"prime":P,"target":"C"+str(j),
                    "source_original_index":ref,"source_original_groups":source_groups,
                    "source_original_S5_row_mapping":self.inputs["S5_index"],
                    "source_original_target_configuration":index["target_configuration"],
                    "vector_coefficients_mod_prime":normal,"regular_degree_bound":4,
                    "normal_basis_degrees":EPS,"coefficient_field_basis":FIELD_BASIS,
                    "all14_original_field_columns_consumed":True,
                    "all_exact_weighted_zero_numerators_verified":True,
                    "original_rational_scales_applied_exactly_once":True,
                    "original_exact_C_or_S5_solve_recomputed":False,
                    "finite_fibre_C_unit_condition_assumed":False})
            assert prior["source_original_index"]==ref
            self.C.append(prior["vector_coefficients_mod_prime"])
            shape(self.C[-1],5,N)
            self.checkpoint(name)

    def base_B_derivative(self):
        name="sigma-00-B-original-derivative"
        prior=self.old(name)
        if prior is None:
            self.budget()
            # The original R827 derivative was already computed.  Its completed
            # C-coordinate column is transported back; Gamma*B is not repeated.
            ref=self.inputs["base_B_derivative_C_column"]
            old=self.source(ref);basis=self.input("C_basis_reduction")
            assert old["chart"]=="tau" and old["derivative_order"]==1
            assert old["original_B_times_normal_basis_index"]==0
            assert old["exact_monic_degree20_division_and_original_column_multiplyback_verified"] is True
            assert plain(old["source_complete_C"])==plain(self.inputs["C_basis_reduction"])
            raw=old["column_coefficients_in_original_C_basis"];assert len(raw)==N
            tau=basis["charts"]["tau"] if "charts" in basis else basis["tau"]
            q=tau["q_polynomials"];P0=poly(tau["P_polynomial"])
            assert len(q)==N-1 and P0.degree()==20
            functions=[poly(row) for row in raw[:N-1]]
            last=P0*poly(raw[N-1])
            for a,b in zip(q,functions):
                last-=poly(a)*b
            functions.append(last)
            normal=[[int(functions[i][k]) for i in range(N)] for k in range(8)]
            for i,f in enumerate(functions):
                assert f.degree()<=7-EPS[i]
            prior=self.put(name,{"prime":P,"sigma_power":0,"target":"B",
                "source_original_normal":self.normal_refs[0]["B"],
                "source_completed_derivative_C_column":ref,
                "source_complete_C":self.inputs["C_basis_reduction"],
                "vector_coefficients_mod_prime":normal,"regular_degree_bound":7,
                "normal_basis_degrees":EPS,
                "transport":"normal[0:271]=C[0:271]; normal271=P*C271-sum(q_i*C_i)",
                "complete_original_normal_basis_restored":True,
                "original_Gamma_times_B_arithmetic_recomputed":False,
                "source_completed_derivative_bytes_unchanged":True})
        self.derivative_specs[0,"B"]=self.refs[name]
        return prior["vector_coefficients_mod_prime"]

    def derivatives(self):
        self.dnormal={};self.dnormal[0,"B"]=self.base_B_derivative()
        for j,source in sorted(self.reused_B.items()):
            if j==0:
                raise AssertionError("Base B derivative uses the explicit original R827 C-column source")
            if j>5:
                continue
            name=f"sigma-{j:02d}-B-imported-original-derivative"
            prior=self.old(name)
            if prior is None:
                data=self.source(source)
                assert data["prime"]==P and data["sigma_power"]==j
                assert data["original_branch"]==STRATEGY["original_sigma_branch_order"][j]
                assert plain(data["source_original_B"])==plain(self.normal_refs[j]["B"])
                assert data["normal_basis_degrees"]==EPS and data["regular_degree_bounds"]==[7,9]
                assert data["first_column_copied_from_actual_completed_derivative_matrices"] is True
                assert data["additional_derivative_arithmetic_computed"] is False
                raw=data["delta_B_coefficients_mod_prime"];shape(raw,8,N)
                assert all(int(raw[k][i])==0 for k in range(8) for i in range(N) if k>7-EPS[i])
                prior=self.put(name,{"prime":P,"sigma_power":j,"target":"B",
                    "source_original_normal":self.normal_refs[j]["B"],
                    "source_completed_derivative":source,
                    "vector_coefficients_mod_prime":raw,"regular_degree_bound":7,
                    "normal_basis_degrees":EPS,"old_completed_derivative_arithmetic_recomputed":False})
            self.dnormal[j,"B"]=prior["vector_coefficients_mod_prime"]
            self.derivative_specs[j,"B"]=self.refs[name]
        needed=[(j,t) for j in range(6) for t in ("A","B") if (j,t) not in self.dnormal]
        # Keep all actual inputs, including sigma^5, on the original fixed branch.
        columns=[{"sigma_power":j,"target":t,"source_original_normal":self.normal_refs[j][t]} for j,t in needed]
        full=[[[0]*len(needed) for _ in range(N)] for _ in range(10)]
        input_matrices=[matrix([[self.normal[j][0 if t=="A" else 1][k][i] for j,t in needed]
                               for i in range(N)]) for k in range(6)]
        g=self.operator_indexes["g"];gamma=self.operator_indexes["Gamma"]
        block_specs=[]
        for index,first in enumerate(range(0,N,16)):
            stop=min(N,first+16);name=f"new-original-derivative-rows-{first:03d}"
            old=self.old(name)
            gref={"source_group":"R827",**plain(g["row_blocks"][index])}
            qref={"source_group":"R827",**plain(gamma["row_blocks"][index])}
            if old is None:
                self.budget()
                gg=self.source(gref);qq=self.source(qref)
                for data,target,degree in ((gg,"g",3),(qq,"Gamma",2)):
                    assert data["prime"]==P and data["target"]==target and data["chart"]=="tau"
                    assert (data["row_first"],data["row_stop"])==(first,stop)
                    assert data["regular_degree_bound"]==degree
                    assert data["original_weighted_support_verified"] is True
                G=[matrix(a) for a in gg["coefficient_matrices_low_to_high"]]
                Q=[matrix(a) for a in qq["coefficient_matrices_low_to_high"]]
                assert len(G)==6 and len(Q)==5
                answer=[zero(stop-first,len(needed)) for _ in range(10)]
                for a,op in enumerate(Q):
                    for k,v in enumerate(input_matrices):
                        answer[a+k]+=op*v
                for a,op in enumerate(G):
                    for k in range(1,6):
                        answer[a+k-1]+=(op*input_matrices[k])*k
                raw=[rows(a) for a in answer]
                for power,block in enumerate(raw):
                    for local,line in enumerate(block):
                        if power>7-EPS[first+local]:
                            assert not any(line),("derivative_weight",power,first+local)
                old=self.put(name,{"prime":P,"row_first":first,"row_stop":stop,
                    "source_g_row_block":gref,"source_Gamma_row_block":qref,
                    "column_sources":columns,"coefficient_blocks_mod_prime":raw,
                    "input_degree_bound":5,"output_regular_degree_bound":7,
                    "original_weighted_support_verified":True,
                    "old_completed_derivatives_omitted":True,
                    "all_products_are_new_required_derivative_columns":True})
            assert old["column_sources"]==columns
            assert old["source_g_row_block"]==gref and old["source_Gamma_row_block"]==qref
            raw=old["coefficient_blocks_mod_prime"];assert len(raw)==10
            for k,block in enumerate(raw):
                shape(block,stop-first,len(needed))
                full[k][first:stop]=block
            block_specs.append(self.refs[name]);self.checkpoint(name)
        for column,(j,t) in enumerate(needed):
            name=f"sigma-{j:02d}-{t}-original-derivative"
            old=self.old(name)
            if old is None:
                raw=[[full[k][i][column] for i in range(N)] for k in range(8)]
                assert not any(full[k][i][column] for k in (8,9) for i in range(N))
                old=self.put(name,{"prime":P,"sigma_power":j,"target":t,
                    "source_original_normal":self.normal_refs[j][t],"source_new_derivative_row_blocks":block_specs,
                    "source_column":column,"vector_coefficients_mod_prime":raw,
                    "regular_degree_bound":7,"normal_basis_degrees":EPS,
                    "exact_original_derivative_formula":"Gamma*a+Mg*partial_z(a)",
                    "all_original_weighted_support_verified":True,
                    "characteristic_zero_coordinates_reconstructed":False})
            self.dnormal[j,t]=old["vector_coefficients_mod_prime"]
            self.derivative_specs[j,t]=self.refs[name]
        assert len(self.dnormal)==12
        del input_matrices,full
        gc.collect();self.checkpoint("required_original_derivatives_complete")

    def characteristic_at(self,a):
        return [value(self.chi[N-k],a) for k in range(N+1)]
    def algebra(self,a):
        """Return the entire source fibre with old inverses reused verbatim."""
        if a in self.fibre_cache:
            return self.fibre_cache[a]
        name=f"node-{a:06d}-original-Krylov"
        if a in self.known_points:
            ref,old=self.known_points[a]
            W=matrix(old["W_evaluated_mod_prime"])
            K=matrix(old["Krylov_matrix_mod_prime"]);Ki=matrix(old["inverse_Krylov_matrix_mod_prime"])
            node_ref=self.inputs["original_characteristic_nodes"][a]
            node=self.source(node_ref)
            assert node["z_value"]==a
            assert plain(node["source_original_Krylov"])==plain(ref)
            modulus=node["characteristic_coefficients_ascending_T"]
            assert modulus==self.characteristic_at(a)
            assert node["full_K_times_relation_equals_k272"] is True
            receipt=self.old(name)
            if receipt is None:
                receipt=self.put(name,{"prime":P,"z0":a,"usable":True,
                    "source_original_Krylov":ref,"source_completed_characteristic_node":node_ref,
                    "source_characteristic_polynomial":self.inputs["characteristic"],
                    "source_original_W":self.inputs["original_W"],
                    "characteristic_coefficients_ascending_T":modulus,
                    "original_Krylov_matrix_or_inverse_or_k272_recomputed":False,
                    "both_original_inverse_products_previously_certified":True})
            source=self.refs[name]
        else:
            built=self.old(name+"-matrix")
            if built is None:
                self.budget()
                W=self.W[3]
                for k in (2,1,0):
                    W=W*a+self.W[k]
                v=matrix([[int(i==0)] for i in range(N)])
                columns=[]
                for k in range(N):
                    columns.append([int(v[i,0]) for i in range(N)])
                    v=W*v
                K=matrix(columns).transpose()
                modulus=self.characteristic_at(a)
                assert len(modulus)==N+1 and modulus[-1]==1
                coefficients=matrix([[modulus[i]] for i in range(N)])
                assert K*coefficients+v==zero(N,1)
                built=self.put(name+"-matrix",{"prime":P,"z0":a,
                    "source_original_W":self.inputs["original_W"],
                    "source_completed_characteristic":self.inputs["characteristic"],
                    "characteristic_coefficients_ascending_T":modulus,
                    "W_evaluated_mod_prime":rows(W),"Krylov_matrix_mod_prime":rows(K),
                    "new_k272":[int(v[i,0]) for i in range(N)],
                    "full_original_characteristic_relation_on_cyclic_vector_verified":True,
                    "old_characteristic_polynomial_arithmetic_repeated":False})
                self.checkpoint(name+"-matrix")
            modulus=built["characteristic_coefficients_ascending_T"]
            W=matrix(built["W_evaluated_mod_prime"]);K=matrix(built["Krylov_matrix_mod_prime"])
            receipt=self.old(name)
            if receipt is None:
                self.budget();det=int(K.det())
                info={"prime":P,"z0":a,"source_new_Krylov_matrix":self.refs[name+"-matrix"],
                    "source_original_W":self.inputs["original_W"],
                    "source_completed_characteristic":self.inputs["characteristic"],
                    "actual_determinant_mod_prime":det,"usable":bool(det),
                    "complete_original_fibre_dimension":N,"no_factors_removed":True}
                if det:
                    Ki=K.inv();assert K*Ki==eye(N) and Ki*K==eye(N)
                    info.update({"inverse_Krylov_matrix_mod_prime":rows(Ki),
                        "both_inverse_products_verified":True,"actual_cyclic_rank":N})
                receipt=self.put(name,info);self.checkpoint(name)
            source=self.refs[name]
            if not receipt["usable"]:
                self.fibre_cache[a]=None
                return None
            Ki=matrix(receipt["inverse_Krylov_matrix_mod_prime"])
        self.fibre_cache={a:(W,K,Ki,poly(modulus),source)}
        return self.fibre_cache[a]

    def element(self,raw,a,Ki):
        normal=matrix([[sum(int(row[i])*pow(a,k,P) for k,row in enumerate(raw))%P] for i in range(N)])
        transformed=Ki*normal
        return poly([int(transformed[i,0]) for i in range(N)])
    def sum_value(self,j,a,algebra):
        name=f"sum-{j}-node-{a:06d}-single-denominator"
        old=self.old(name)
        if old is not None:
            return old
        self.budget()
        W,K,Ki,modulus,algebra_ref=algebra
        mul=lambda x,y:(x*y)%modulus
        def power(x,n):
            answer=poly([1])
            while n:
                if n&1:
                    answer=mul(answer,x)
                n//=2
                if n:
                    x=mul(x,x)
            return answer
        A=self.element(self.normal[0][0],a,Ki);B=self.element(self.normal[0][1],a,Ki)
        phase=inverse(pow(self.rho[j],3,P),"rho^3")
        C=self.element(self.normal[j][0],a,Ki)*phase
        D=self.element(self.normal[j][1],a,Ki)
        dA=self.element(self.dnormal[0,"A"],a,Ki);dB=self.element(self.dnormal[0,"B"],a,Ki)
        dC=self.element(self.dnormal[j,"A"],a,Ki)*phase
        dD=self.element(self.dnormal[j,"B"],a,Ki)
        c0=self.element(self.C[0],a,Ki);cj=self.element(self.C[j],a,Ki)
        F=(mul(A,A)-mul(B,B)*self.b)%modulus
        Fj=(mul(C,C)-mul(D,D)*self.b)%modulus
        Wr=(mul(B,dA)-mul(A,dB))%modulus
        Wj=(mul(D,dC)-mul(C,dD))%modulus
        R=mul(mul(cj,Fj),Wr);S=mul(mul(c0,F),Wj)
        Delta=(R-S)%modulus;Xi=(mul(C,B)-mul(A,D))%modulus
        D3=power(D,3);Delta3=power(Delta,3)
        Q=mul(mul(B,D3),Delta3)
        numerator=(-mul(mul(A,D3),Delta3)+
            mul(mul(mul(Xi,power(D,2)),power(Delta,2)),2*S+R)-
            mul(mul(mul(power(Xi,3),power(c0,3)),power(F,2)),power(Wj,3)))%modulus
        gcd,u,v=Q.xgcd(modulus)
        assert u*Q+v*modulus==gcd
        info={"prime":P,"j":j,"z0":a,"original_Hom_word":"1+T^"+str(j),
            "source_complete_fibre":algebra_ref,
            "source_global_DAG":self.inputs["global_DAG"],
            "source_original_seven_normal_inputs":self.inputs["seven_normal_inputs"],
            "source_original_Hodge_reductions":[self.refs["C0-original-Hodge-normal-reduction"],
                                               self.refs["C"+str(j)+"-original-Hodge-normal-reduction"]],
            "source_original_derivatives":[self.derivative_specs[0,"A"],self.derivative_specs[0,"B"],
                                          self.derivative_specs[j,"A"],self.derivative_specs[j,"B"]],
            "original_rho_mod_prime":self.rho[j],
            "complete_original_algebra_modulus":pack(modulus,N+1),
            "P_coefficients_ascending_w":pack(numerator,N),"Q_coefficients_ascending_w":pack(Q,N),
            "gcd_with_full_characteristic":pack(gcd),
            "Bezout_Q_coefficient":pack(u),"Bezout_characteristic_coefficient":pack(v),
            "full_unreduced_polynomial_Bezout_identity_verified":True,
            "whole_fibre_unit":gcd.degree()==0 and bool(int(gcd[0])),
            "original_complete_fibre_dimension":N,"factors_or_nilpotents_removed":False,
            "single_F_factor_cancelled_exactly_once":True,
            "extra_C0_F_or_Wj_unit_conditions_imposed":False,
            "common_section_weight":98,"original_sigma_extra_frame_power":3,
            "original_global_pole_ideal_nodes":self.graph["five_original_polar_and_eta_outputs"][str(j)]["global_pole_ideals"]}
        if info["whole_fibre_unit"]:
            Qinv=(u*inverse(int(gcd[0]),"constant gcd"))%modulus
            assert mul(Q,Qinv)==poly([1])
            y=mul(numerator,Qinv);assert mul(Q,y)==numerator
            y_normal=K*matrix([[int(y[i])] for i in range(N)])
            info.update({"Q_inverse_coefficients_ascending_w":pack(Qinv,N),
                "y_coefficients_ascending_w":pack(y,N),
                "y_normal_coordinates_mod_prime":[int(y_normal[i,0]) for i in range(N)],
                "whole_original_Q_times_inverse_equals_one":True,
                "all272_original_Q_times_y_equals_P_verified":True,
                "no_original_field_constant_or_phase_discarded":True})
        old=self.put(name,info);self.checkpoint(name)
        return old

    def choose_fibres(self):
        selected={j:[] for j in self.requested}
        for a in range(self.node_limit):
            active=[j for j in self.requested if len(selected[j])<FIBRES[j-1]]
            if not active:
                break
            self.budget();algebra=self.algebra(a)
            if algebra is None:
                self.node_outcomes[str(a)]={"original_Krylov_unit":False}
                self.checkpoint("whole_fibre_search")
                continue
            outcomes={}
            for j in active:
                data=self.sum_value(j,a,algebra)
                outcomes[str(j)]=bool(data["whole_fibre_unit"])
                if data["whole_fibre_unit"]:
                    selected[j].append(a)
            self.node_outcomes[str(a)]={"original_Krylov_unit":True,"sum_Q_units":outcomes}
            self.checkpoint("whole_fibre_search")
        self.selected=selected
        for j in self.requested:
            name=f"sum-{j}-selected-complete-fibres"
            old=self.old(name)
            nodes=selected[j]
            if len(nodes)==FIBRES[j-1]:
                refs=[self.refs[f"sum-{j}-node-{a:06d}-single-denominator"] for a in nodes]
                if old is None:
                    old=self.put(name,{"prime":P,"j":j,"original_Hom_word":"1+T^"+str(j),
                        "original_pole_degree":DEGREES[j-1],"ordinary_power":POWERS[j-1],
                        "nodes":nodes,"full_fibre_sources":refs,"whole_fibre_count":len(nodes),
                        "complete_evaluation_length":N*len(nodes),
                        "section_degree_upper_bound":N*POWERS[j-1]+DEGREES[j-1],
                        "complete_global_section_evaluation_injective":True,
                        "all_denominators_units_in_the_whole_fibres":True,
                        "residue_field_factors_or_multiplicities_removed":False})
                else:
                    assert old["nodes"]==nodes and old["full_fibre_sources"]==refs
        if any(len(selected[j])<FIBRES[j-1] for j in self.requested):
            raise ScopeStop("Finite node schedule has insufficient complete unit fibres")
        self.checkpoint("complete_fibres_selected")

    def multiplication(self,j,a):
        name=f"sum-{j}-node-{a:06d}-normal-multiplier"
        old=self.old(name)
        if old is None:
            self.budget()
            W,K,Ki,modulus,algebra_ref=self.algebra(a)
            source=self.old(f"sum-{j}-node-{a:06d}-single-denominator")
            assert source["whole_fibre_unit"] is True
            v=matrix([[x] for x in source["y_normal_coordinates_mod_prime"]])
            columns=[];current=v
            for k in range(N):
                columns.append([int(current[i,0]) for i in range(N)])
                current=W*current
            Ky=matrix(columns).transpose()
            M=Ky*Ki
            assert M*K==Ky
            assert all(int(M[i,0])==int(v[i,0]) for i in range(N))
            old=self.put(name,{"prime":P,"j":j,"z0":a,
                "source_complete_fibre":algebra_ref,
                "source_single_denominator":self.refs[f"sum-{j}-node-{a:06d}-single-denominator"],
                "normal_multiplication_matrix_mod_prime":rows(M),
                "matrix_convention":"output normal row, input normal column",
                "full272_original_Krylov_action_product_verified":True,
                "first_column_is_the_complete_original_y_value":True,
                "no_original_fibre_factor_or_multiplicity_discarded":True,
                "old_Krylov_inverse_arithmetic_recomputed":False})
            self.checkpoint(name)
        return matrix(old["normal_multiplication_matrix_mod_prime"]),self.refs[name]

    def scalar_interpolation(self,j,nodes):
        n=POWERS[j-1];name=f"sum-{j}-three-scalar-interpolation-blocks"
        old=self.old(name)
        if old is None:
            self.budget();blocks={}
            for m in (n+1,n,n-1):
                prefix=nodes[:m]
                coefficients=[]
                denominators=[]
                for h,a in enumerate(prefix):
                    f=poly([1]);den=1
                    for k,b in enumerate(prefix):
                        if k==h:
                            continue
                        f*=poly([-b,1]);den=den*(a-b)%P
                    inv=inverse(den,"distinct original fibre nodes")
                    f*=inv;coefficients.append(pack(f,m));denominators.append(den)
                inverse_matrix=matrix(coefficients).transpose()
                V=matrix([[pow(a,k,P) for k in range(m)] for a in prefix])
                assert inverse_matrix*V==eye(m) and V*inverse_matrix==eye(m)
                evaluations=[[sum(coefficients[h][k]*pow(a,k,P) for k in range(m))%P
                              for h in range(m)] for a in nodes]
                assert evaluations[:m]==rows(eye(m))
                blocks[str(m)]={"interpolation_nodes":prefix,
                    "Lagrange_coefficient_matrix":rows(inverse_matrix),
                    "evaluation_rows_at_all_nodes":evaluations,
                    "nonzero_denominators_mod_prime":denominators,
                    "both_scalar_Vandermonde_inverse_products_verified":True,
                    "exact_characteristic_zero_formula":"L_h(z)=product_{k!=h}(z-a_k)/(a_h-a_k)"}
            old=self.put(name,{"prime":P,"j":j,"ordinary_power":n,
                "nodes":nodes,"normal_basis_degrees":EPS,"blocks":blocks,
                "source_complete_fibres":self.refs[f"sum-{j}-selected-complete-fibres"],
                "selected_A_rows":"for normal output i, first n-epsilon_i+1 nodes",
                "global_A_dense_inverse_computed":False,
                "all_original_node_differences_are_units":True})
        assert old["nodes"]==nodes
        return old,self.refs[name]

    def schur(self,j):
        n=POWERS[j-1];nodes=self.selected[j];d=272*n-126
        multipliers=[];multiplier_refs=[]
        for a in nodes:
            M,ref=self.multiplication(j,a)
            multipliers.append(M);multiplier_refs.append(ref)
        interp,iref=self.scalar_interpolation(j,nodes)
        mapping=positions(n);assert len(mapping)==d
        powers=[[pow(a,k,P) for k in range(n+1)] for a in nodes]
        chunks=[];labels=[]
        for first in range(0,N,16):
            stop=min(N,first+16);name=f"sum-{j}-Schur-normal-rows-{first:03d}"
            old=self.old(name)
            if old is None:
                self.budget();out=[];row_labels=[]
                for i in range(first,stop):
                    m=n-EPS[i]+1
                    # Rows of H=Y*E for this one output component.  No large
                    # normal-basis multiplication is rebuilt here.
                    H=matrix([[int(M[i,c])*powers[l][k]%P for c,k in mapping]
                              for l,M in enumerate(multipliers)])
                    HI=sub(H,list(range(m)),list(range(d)))
                    HC=sub(H,list(range(m,len(nodes))),list(range(d)))
                    L=matrix(interp["blocks"][str(m)]["evaluation_rows_at_all_nodes"][m:])
                    block=HC-L*HI
                    out.extend(rows(block))
                    row_labels.extend([[i,l] for l in range(m,len(nodes))])
                old=self.put(name,{"prime":P,"j":j,"ordinary_power":n,
                    "normal_output_first":first,"normal_output_stop":stop,
                    "source_original_multipliers":multiplier_refs,
                    "source_three_scalar_blocks":iref,
                    "row_labels_output_component_and_node_ordinal":row_labels,
                    "Schur_matrix_rows_mod_prime":out,
                    "column_count":d,"column_order":"(i,k), 0<=k<=n-epsilon_i",
                    "sign":"H_remaining-Lambda*H_selected",
                    "no_dense_A_inverse_or_new_large_original_operator_solve":True})
                self.checkpoint(name)
            assert old["source_original_multipliers"]==multiplier_refs
            assert old["source_three_scalar_blocks"]==iref
            chunks.append(self.refs[name]);labels.extend(old["row_labels_output_component_and_node_ordinal"])
        assert len(labels)==N*len(nodes)-d and len({tuple(row) for row in labels})==len(labels)
        indexname=f"sum-{j}-complete-Schur-index"
        index=self.old(indexname)
        if index is None:
            index=self.put(indexname,{"prime":P,"j":j,"ordinary_power":n,
                "original_pole_degree":DEGREES[j-1],"nodes":nodes,
                "Schur_shape":[len(labels),d],"normal_basis_degrees":EPS,
                "original_column_mapping":[list(x) for x in mapping],
                "complete_row_labels":labels,"row_blocks":chunks,
                "source_three_scalar_blocks":iref,"source_original_multipliers":multiplier_refs,
                "exact_matrix_definition":"H_R-Lambda*H_I, H=direct_sum(m_yj)*E_n",
                "independent_characteristic_zero_rank":DEGREES[j-1],
                "independent_complete_kernel_dimension":DIMENSIONS[j-1],
                "rank_reason":"R893 full degree bound and complete-fibre injection, not a candidate label"})
        all_rows=[]
        for ref in chunks:
            all_rows.extend(self.own(ref)["Schur_matrix_rows_mod_prime"])
        shape(all_rows,len(labels),d);S=matrix(all_rows)
        del all_rows,multipliers
        gc.collect()
        self.checkpoint(indexname)
        return S,index,self.refs[indexname]

    def kernel(self,j,S,index,index_ref):
        n=POWERS[j-1];d=272*n-126;r=DEGREES[j-1];nullity=DIMENSIONS[j-1]
        assert S.ncols()==d and S.nrows()==N*FIBRES[j-1]-d and d-r==nullity
        profile_name=f"sum-{j}-Schur-independent-original-rows"
        profile=self.old(profile_name)
        if profile is None:
            self.budget()
            reduced,rank=S.transpose().rref()
            assert rank<=r,("original_geometric_rank_upper_bound",j,rank,r)
            selected=pivots(reduced,rank)
            profile=self.put(profile_name,{"prime":P,"j":j,"source_complete_Schur":index_ref,
                "actual_rank":rank,"required_rank":r,"accepted":rank==r,
                "selected_original_rows":selected,
                "selected_row_labels":[index["complete_row_labels"][k] for k in selected],
                "rank_selection":"left-to-right pivots of original complete Schur transpose",
                "rank_deficiency_does_not_negate_other_places_or_original_RR":rank!=r})
            del reduced;gc.collect();self.checkpoint(profile_name)
        assert profile["source_complete_Schur"]==index_ref
        if not profile["accepted"]:
            return None
        I=profile["selected_original_rows"];assert len(I)==r
        chart_name=f"sum-{j}-Schur-unit-kernel-chart"
        chart=self.old(chart_name)
        if chart is None:
            self.budget()
            selected=sub(S,I,list(range(d)))
            reduced,rank=selected.rref();assert rank==r
            J=pivots(reduced,rank);free=[k for k in range(d) if k not in set(J)]
            assert len(free)==nullity
            assert sub(reduced,list(range(r)),J)==eye(r)
            pivot_solution=[[-int(reduced[i,k])%P for k in free] for i in range(r)]
            chart=self.put(chart_name,{"prime":P,"j":j,"source_complete_Schur":index_ref,
                "source_independent_original_rows":self.refs[profile_name],
                "selected_original_rows":I,"pivot_columns":J,"free_columns":free,
                "pivot_solution_mod_prime":pivot_solution,
                "canonical_free_identity":True,
                "RREF_selected_minor_is_identity":True,
                "exact_characteristic_zero_formula":"B_J=-S[I,J]^-1*S[I,F]; B_F=I"})
            del selected,reduced;gc.collect();self.checkpoint(chart_name)
        I=chart["selected_original_rows"];J=chart["pivot_columns"];free=chart["free_columns"]
        assert len(I)==len(J)==r and len(free)==nullity and sorted(J+free)==list(range(d))
        minor_name=f"sum-{j}-Schur-original-unit-minor"
        minor=self.old(minor_name)
        if minor is None:
            self.budget()
            square=sub(S,I,J);det=int(square.det());assert det
            minor=self.put(minor_name,{"prime":P,"j":j,"source_complete_Schur":index_ref,
                "source_kernel_chart":self.refs[chart_name],"row_indices":I,"column_indices":J,
                "matrix_shape":[r,r],"actual_determinant_mod_prime":det,
                "original_row_labels":[index["complete_row_labels"][k] for k in I],
                "original_column_labels":[index["original_column_mapping"][k] for k in J],
                "characteristic_zero_selected_minor_is_a_DVR_unit":True,
                "source_matrix_characteristic_zero_rank_already_known":r,
                "all_remaining_characteristic_zero_rows_follow_from_equal_rank":True,
                "large_inverse_expanded":False})
            del square;gc.collect();self.checkpoint(minor_name)
        kernel_name=f"sum-{j}-complete-initial-B-kernel"
        kernel=self.old(kernel_name)
        if kernel is None:
            self.budget()
            raw=[[0]*nullity for _ in range(d)]
            for column,k in enumerate(free):
                raw[k][column]=1
            shape(chart["pivot_solution_mod_prime"],r,nullity)
            for local,k in enumerate(J):
                raw[k]=chart["pivot_solution_mod_prime"][local]
            B=matrix(raw)
            assert S*B==zero(S.nrows(),nullity)
            assert sub(B,free,list(range(nullity)))==eye(nullity)
            kernel=self.put(kernel_name,{"prime":P,"j":j,"ordinary_power":n,
                "original_pole_degree":r,"residual_degree":RESIDUAL_DEGREES[j-1],
                "complete_kernel_dimension":nullity,
                "source_complete_Schur":index_ref,"source_unit_minor":self.refs[minor_name],
                "source_kernel_chart":self.refs[chart_name],
                "normal_basis_degrees":EPS,"original_column_mapping":index["original_column_mapping"],
                "B_coefficients_mod_prime":raw,"free_columns":free,
                "all_original_Schur_rows_times_full_kernel_zero":True,
                "canonical_free_identity_verified":True,
                "exact_unit_solve_expression":{
                    "source_original_global_y_DAG":self.inputs["global_DAG"],
                    "source_original_sum_Hom_word":"1+T^"+str(j),
                    "exact_Schur_source":index_ref,
                    "row_indices":I,"pivot_columns":J,"free_columns":free,
                    "formula":"B_J=-S[I,J]^-1*S[I,F]; B_F=I",
                    "unit_witness":self.refs[minor_name],
                    "complete_characteristic_zero_rank":r,
                    "all_full_original_global_relations_hold_by_R893_injection":True,
                    "array_is_modular_reduction_not_expanded_characteristic_zero_coordinates":True}})
            self.checkpoint(kernel_name)
        assert kernel["source_unit_minor"]==self.refs[minor_name]
        B=matrix(kernel["B_coefficients_mod_prime"])
        return B,self.refs[kernel_name],self.refs[minor_name]

    def evaluate_kernel(self,K,n,a):
        """Evaluate all normal polynomial columns, preserving their basis order."""
        mapping=positions(n);assert len(mapping)==K.nrows()
        answer=[];offset=0
        for i in range(N):
            m=n-EPS[i]+1
            block=sub(K,list(range(offset,offset+m)),list(range(K.ncols())))
            scalar=matrix([[pow(a,k,P) for k in range(m)]])
            row=scalar*block
            answer.append([int(row[0,j]) for j in range(K.ncols())])
            offset+=m
        assert offset==K.nrows()
        return matrix(answer)

    def recover_A_and_verify(self,j,B,Bref,minor_ref,index,index_ref):
        n=POWERS[j-1];nodes=self.selected[j];dim=DIMENSIONS[j-1];d=272*n-126
        values=[];value_refs=[]
        for a in nodes:
            name=f"sum-{j}-node-{a:06d}-full-kernel-denominator-value"
            old=self.old(name)
            if old is None:
                self.budget()
                vb=self.evaluate_kernel(B,n,a)
                multiplier,mref=self.multiplication(j,a)
                target=multiplier*vb
                old=self.put(name,{"prime":P,"j":j,"z0":a,"source_complete_B_kernel":Bref,
                    "source_original_y_multiplier":mref,
                    "B_fibre_values_mod_prime":rows(vb),"y_times_B_fibre_values_mod_prime":rows(target),
                    "all_kernel_columns_evaluated_in_original_normal_basis":True,
                    "full_fibre_dimension":N,"complete_kernel_dimension":dim})
                self.checkpoint(name)
            values.append(matrix(old["y_times_B_fibre_values_mod_prime"]))
            value_refs.append(self.refs[name])
        aname=f"sum-{j}-complete-initial-A-kernel"
        Adata=self.old(aname)
        if Adata is None:
            self.budget()
            interp=self.own(index["source_three_scalar_blocks"])
            raw=[]
            for i in range(N):
                m=n-EPS[i]+1
                selected=matrix([[int(values[l][i,k]) for k in range(dim)] for l in range(m)])
                L=matrix(interp["blocks"][str(m)]["Lagrange_coefficient_matrix"])
                raw.extend(rows(L*selected))
            shape(raw,d,dim)
            Adata=self.put(aname,{"prime":P,"j":j,"ordinary_power":n,
                "source_complete_B_kernel":Bref,"source_unit_minor":minor_ref,
                "source_three_scalar_blocks":index["source_three_scalar_blocks"],
                "source_complete_yB_fibre_values":value_refs,
                "A_coefficients_mod_prime":raw,"normal_basis_degrees":EPS,
                "original_column_mapping":index["original_column_mapping"],
                "exact_characteristic_zero_formula":"A=E_selected^-1*(Y*E*B)_selected",
                "large_original_A_inverse_computed":False,
                "array_is_modular_reduction_of_the_exact_unit_solve":True})
            self.checkpoint(aname)
        A=matrix(Adata["A_coefficients_mod_prime"]);Areference=self.refs[aname]
        checks=[]
        for a,target,value_ref in zip(nodes,values,value_refs):
            name=f"sum-{j}-node-{a:06d}-all-original-kernel-relations"
            check=self.old(name)
            if check is None:
                self.budget();actual=self.evaluate_kernel(A,n,a)
                assert actual==target,("complete_original_global_relation",j,a)
                check=self.put(name,{"prime":P,"j":j,"z0":a,
                    "source_complete_A_kernel":Areference,"source_complete_B_kernel":Bref,
                    "source_original_yB_values":value_ref,
                    "all272_times_complete_kernel_dimension_original_relations_zero":True,
                    "checked_shape":[N,dim],"complete_fibre_factors_or_multiplicities_removed":False})
                self.checkpoint(name)
            assert check["source_complete_A_kernel"]==Areference
            checks.append(self.refs[name])
        name=f"sum-{j}-complete-initial-RR-certificate"
        final=self.old(name)
        if final is None:
            assert N*len(nodes)>N*n+DEGREES[j-1]
            final=self.put(name,{"prime":P,"j":j,"original_Hom_word":"1+T^"+str(j),
                "ordinary_power":n,"original_pole_degree":DEGREES[j-1],
                "residual_degree":RESIDUAL_DEGREES[j-1],"complete_kernel_dimension":dim,
                "source_original_global_DAG":self.inputs["global_DAG"],
                "source_original_pole_ideal_nodes":self.graph["five_original_polar_and_eta_outputs"][str(j)]["global_pole_ideals"],
                "source_complete_fibres":self.refs[f"sum-{j}-selected-complete-fibres"],
                "source_complete_Schur":index_ref,"source_original_unit_minor":minor_ref,
                "complete_A_kernel":Areference,"complete_B_kernel":Bref,
                "all_original_fibre_relation_certificates":checks,
                "all_original_fibre_rows_checked":N*len(nodes),
                "independent_original_global_dimension":dim,
                "all_original_Schur_rows_verified":True,
                "all_complete_fibre_original_A_minus_yB_relations_verified":True,
                "complete_initial_RR_space_certified":True,
                "actual_arrays_are_only_modular_reductions":True,
                "exact_unit_solve_expression_certified":True,
                "characteristic_zero_coordinates_reconstructed":False,
                "original_c0_marked_pair_computed":False,
                "future_padding_to_544":PADDING[j-1],
                "later_V2n_injection_assumed_from_initial_fibres":False,
                "future_threeH_RR_padding_or_complete418_space_computed":False,
                "original_Lj128_Picard_support_or_height_computed":False})
        self.done[str(j)]=self.refs[name];self.checkpoint(name)
        return final

    def run(self):
        self.prepare();self.hodge_reductions();self.derivatives();self.choose_fibres()
        insufficient=[]
        for j in self.requested:
            finished=self.old(f"sum-{j}-complete-initial-RR-certificate")
            if finished is not None:
                assert finished["complete_initial_RR_space_certified"] is True
                self.done[str(j)]=self.refs[f"sum-{j}-complete-initial-RR-certificate"]
                continue
            S,index,index_ref=self.schur(j)
            result=self.kernel(j,S,index,index_ref)
            del S;gc.collect()
            if result is None:
                insufficient.append(j)
                continue
            B,Bref,minor_ref=result
            self.recover_A_and_verify(j,B,Bref,minor_ref,index,index_ref)
            del B;gc.collect()
        if insufficient:
            raise ScopeStop("Actual fixed-place Schur ranks are deficient for directions "+repr(insufficient))
        return self.finish(True,None)

    def inventory(self):
        entries=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name==self.path("current").name or path.name.startswith(PREFIX+"stage-manifest-"):
                continue
            v=read(path);assert v["result"]==RESULT and v["configuration"]==self.tag and v["complete"] is True
            entries.append(spec(path))
        name="stage-manifest-"+fingerprint(entries)[:24]
        self.put(name,{"files":entries,"complete_stages_only":True,
            "old_source_stages_not_relabelled_or_duplicated":True,"current_excluded":True})
        return self.refs[name]
    def finish(self,complete,error):
        for j in range(1,6):
            old=self.old(f"sum-{j}-complete-initial-RR-certificate")
            if old is not None:
                assert old["complete_initial_RR_space_certified"] is True
                self.done[str(j)]=self.refs[f"sum-{j}-complete-initial-RR-certificate"]
        assert not complete or all(str(j) in self.done for j in self.requested)
        current=self.checkpoint(self.phase)
        final={"result":RESULT,"configuration":self.tag,"complete":bool(complete),"p":41,"prime":P,
            "requested_directions":self.requested,"completed_directions":sorted(map(int,self.done)),
            "source_audit":self.refs.get("original-source-audit"),
            "complete_initial_RR_certificates":self.done,
            "all_five_complete_initial_RR_spaces_certified":len(self.done)==5,
            "requested_complete_initial_RR_spaces_certified":all(str(j) in self.done for j in self.requested),
            "original_Hom_words":["1+T^"+str(j) for j in range(1,6)],
            "original_pole_degrees":DEGREES,"initial_RR_powers":POWERS,
            "initial_RR_dimensions":DIMENSIONS,"future_padding_to_544":PADDING,
            "characteristic_zero_kernel_coordinates_reconstructed":False,
            "original_c0_marked_pairs_or_padding_spaces_computed":False,
            "original_Lj128_or_Hecke_Picard_support_computed":False,
            "connection_period_or_height_computed":False,
            "old_seven_normal_inputs_C_coordinates_derivative_operators_or_charpoly_recomputed":False,
            "stage_manifest":self.inventory(),"resume_state":current,
            "scope_stop_reason":error,"seconds":time.monotonic()-self.started}
        save(self.out/FINAL,final)
        print("R893_FINAL_SUMMARY="+json.dumps({key:final[key] for key in (
            "complete","completed_directions","all_five_complete_initial_RR_spaces_certified",
            "initial_RR_dimensions","scope_stop_reason","seconds")}),flush=True)
        return final

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
        job=Job(args)
        certificate=job.run();code=0
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
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    final_path=out/FINAL
    receipt={"result":RESULT,"source_sha256":sha(__file__),"complete":code==0,
        "exit_code":code,"configuration":job.tag if job is not None else None,
        "configuration_sha256":fingerprint(job.tag) if job is not None else None,
        "certificate_sha256":sha(final_path) if certificate is not None and final_path.exists() else None,
        "completed_directions":sorted(map(int,job.done)) if job is not None else [],
        "error":error,"traceback":trace,"seconds":time.monotonic()-started}
    save(out/"core-receipt.json",receipt)
    print("R893_CORE_RECEIPT="+json.dumps(receipt,sort_keys=True),flush=True)
    raise SystemExit(code)

if __name__=="__main__":
    main()
