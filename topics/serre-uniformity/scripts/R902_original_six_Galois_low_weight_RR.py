#!/usr/bin/env python3
"""R902: strict fixed-chart constant-field conjugates, two initial RHS only.
All new arithmetic belongs to the named public repository Actions.
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
import R902_fixed_Galois_unit_charts as charts

REPOSITORY="Rogerhu12/math-research-public"
RESULT="R902-original-six-Galois-five-sum-Hom-low-weight-RR"
FINAL="p41-original-six-Galois-five-sum-Hom-low-weight-RR-certificate.json"
PREFIX="R902-"
MANIFEST="full-outputs-manifest.json"
P=1000000753
N=272
EPS=[0]+[1]*144+[2]*127
POWERS=[12,8,8,13,14]
DEGREES=[2970,1674,1800,3024,3339]
FIBRES=[23,15,15,25,27]
DELTAS=[294,502,376,512,469]
INITIAL_DIMS=[168,376,250,386,343]
RESIDUAL_DIMS=[396,188,314,178,221]
PADDING=[250,42,168,32,75]
SIGMA_BRANCHES=[0,6,1,2,4,3,5]
FIELD_BASIS="b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b"
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
MANDATORY=("R893","R896","R849","R877","R809","R827","AB","SIXD","R872","R883","JETS","R890")
STRATEGY={
 "original_curve":"original genus127 Y, level82 and original minus3 descent",
 "prime":P,"s_root":99932770,"zeta_root":549966761,
 "original_sigma_branch_order":SIGMA_BRANCHES,"canonical_free_column":1186,
 "normal_basis_degrees":EPS,"initial_powers":POWERS,"pole_degrees":DEGREES,
 "original_fibre_counts":FIBRES,"initial_space_dimensions":INITIAL_DIMS,
 "residual_dimensions":RESIDUAL_DIMS,"padding_orders":PADDING,
 "fixed_task_order":[[j,r] for j in range(1,6) for r in range(1,7)],
 "sigma0":"external original R893/R896 stages, never recomputed or relabelled",
 "phase":"sigma^r(rho_j)^-3; T^7=zeta^2 retained; sigma^7 is identity on constants",
 "complete_initial_space":"same exact I,J,F unit-solve defines the entire conjugate space",
 "initial_numeric_columns":2,
 "two_free_RHS":"original B0 canonical column and original integer B1 power weights",
 "initial_Schur":"only old selected rows, with unchanged scalar Lagrange blocks",
 "strict_selection":"no new rows, columns, free order, projection rows or integer anchors",
 "fixed_nodes":"exact original node lists; no replacement after a new nonunit",
 "whole_fibre":"all272 factors and multiplicities, single actual Q unit and full Q*y=P",
 "only_new_derivative":"delta A at original sigma_power6; all other A/B derivatives reused",
 "low_weight":"complete residual kernel, complete146 and complete418, all original rows",
 "final_product_fibres":7,"V6_injection_length":1904,
 "principal":"Q=sigma(B0/tau^n)/(sigma(v)/tau^3)*qchi^(-(n-2))",
 "frame":"unscaled rho leading times original c^(deg(E)-1)",
 "transport_aliases":"source groups are IO labels; old producer configurations stay unchanged",
 "characteristic_zero_coordinates_reconstructed":False,
 "scope_control_and_budget_excluded_from_mathematical_identity":True,
}

class BudgetStop(RuntimeError):
    pass
class UnitFailure(RuntimeError):
    pass
class ScopeStop(RuntimeError):
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

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
        "method_sha256":item["method_sha256"],"proofs":item["proofs"],
        "fixed_chart_helper_sha256":item["fixed_chart_helper_sha256"],
        "sources":{g:identity(item["sources"][g]) for g in sorted(item["sources"])},
        "inputs":item["inputs"],"strategy":STRATEGY}

def hcat(A,B):
    assert A.nrows()==B.nrows()
    return matrix([[int(A[i,j]) for j in range(A.ncols())]+[int(B[i,j]) for j in range(B.ncols())]
                   for i in range(A.nrows())])

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
        self.inventory=indexed
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
        if self.label in ("R827","R809"):
            # Frozen producers store the result inside their exact configuration.
            assert "result" not in value,(self.label,row["file"],"historical_stage_schema")
            assert value["configuration"]["result"]==self.item["result"]
        else:
            assert value.get("result")==self.item["result"],(self.label,row["file"],"stage_result")
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
        assert sha(topic/self.item["fixed_chart_helper"])==self.item["fixed_chart_helper_sha256"]
        assert Path(charts.__file__).resolve()==(topic/self.item["fixed_chart_helper"]).resolve()
        for entry in self.item["proofs"].values():
            assert sha(topic/entry["path"])==entry["sha256"]
        assert set(MANDATORY)==set(self.item["sources"])
        self.tag=expected_tag(self.item);self.refs={};self.done={};self.current=None
        self.phase="source_initialization";self.active_pair=None
        self.sources={g:Source(g,v,args.retained) for g,v in self.item["sources"].items()}
        self.inputs=self.item["inputs"]
        self.limit=int(self.item.get("maximum_pairs",30));assert 1<=self.limit<=30
        self.V3=positions(3);self.V3map={p:i for i,p in enumerate(self.V3)}
        assert len(self.V3)==690
        self.fibres={};self.templates={};self.C_cache={};self.new_multipliers={}
    def budget(self):
        if time.monotonic()-self.started>=self.args.budget_minutes*60-30:
            raise BudgetStop("Completed source-bound stages retained; phase="+self.phase)
    def path(self,name):
        assert Path(name).name==name
        return self.out/(PREFIX+name+".json.gz")
    def old(self,name):
        path=self.path(name)
        if not path.exists():
            return None
        obj=read(path)
        assert obj["result"]==RESULT and obj["configuration"]==self.tag and obj["complete"] is True
        self.refs[name]=spec(path);return obj
    def put(self,name,payload):
        assert not set(payload)&{"result","configuration","complete"}
        obj={"result":RESULT,"configuration":self.tag,"complete":True,**payload}
        path=self.path(name)
        if path.exists():
            assert read(path)==obj
        else:
            save(path,obj)
        self.refs[name]=spec(path)
        print("R902_STAGE="+json.dumps({"file":path.name,"seconds":time.monotonic()-self.started}),flush=True)
        return obj
    def ref(self,name):
        return self.refs[name]
    def checkpoint(self,phase):
        self.phase=phase
        save(self.path("current"),{"result":RESULT,"configuration":self.tag,"complete":False,
            "phase":phase,"active_pair":self.active_pair,
            "complete_direction_conjugate_certificates":self.done,"complete_stages":self.refs})
        self.current=spec(self.path("current"));return self.current
    def source(self,row):
        return self.sources[row["source_group"]].stage(row)
    def input(self,key):
        return self.source(self.inputs[key])
    def own(self,row):
        path=self.out/row["file"];assert spec(path)==plain(row)
        obj=read(path)
        assert obj["result"]==RESULT and obj["configuration"]==self.tag and obj["complete"] is True
        return obj
    def resolve(self,parent,row,readable=True):
        """Resolve original source-group labels by immutable producer identity."""
        key=parent
        if row.get("source_group") is not None:
            oldkey=row["source_group"]
            if oldkey!=parent:
                source_ids=self.sources[parent].tag.get("sources",{})
                origin=source_ids.get(oldkey)
                if origin is None and oldkey in self.sources:
                    origin=self.item["sources"][oldkey]
                assert origin is not None,(parent,oldkey)
                choices=[g for g,v in self.item["sources"].items()
                         if all(str(v[k])==str(origin[k]) for k in BASE)]
                assert len(choices)==1,(parent,oldkey,choices)
                key=choices[0]
        src=self.sources[key]
        assert src.inventory[row["file"]]==plain(row),(parent,row["file"])
        ref={"source_group":key,**plain(row)}
        if readable:
            assert src.files[row["file"]]==plain(row)
        return ref
    def inherited(self,parent,row):
        ref=self.resolve(parent,row);return self.source(ref),ref
    def same_input(self,parent,oldkey,newkey):
        assert self.resolve(parent,self.sources[parent].tag["inputs"][oldkey])==self.inputs[newkey]
    def stem(self,j,r):
        return f"j{j}-sigma-{r:02d}"
    def fail_scalar(self,name,value0,reason,source_refs):
        if int(value0)%P==0:
            self.put(name,{"prime":P,"reason":reason,"source_references":source_refs,
                "actual_value_mod_prime":0,"original_fixed_chart_failed_at_this_place":True,
                "new_selection_or_rescaling_performed":False,
                "original_characteristic_zero_conjugate_disproved":False})
            self.checkpoint(name)
            raise UnitFailure(reason)

    def prepare(self):
        self.budget()
        initial=self.sources["R893"];low=self.sources["R896"]
        assert initial.certificate["all_five_complete_initial_RR_spaces_certified"] is True
        assert low.certificate["all_five_complete_low_weight_RR_spaces_certified"] is True
        same_origin(low.tag["sources"]["R893"],self.item["sources"]["R893"])
        for oldkey,newkey in (("R880","AB"),("R877","R877"),("R809","R809"),
                              ("R849","R849"),("R827","R827"),("DSTAR","SIXD")):
            same_origin(initial.tag["sources"][oldkey],self.item["sources"][newkey])
        for oldkey,newkey in (("R880","JETS"),("R872","R872"),("R883","R883"),
                              ("R827","R827"),("R890","R890")):
            same_origin(low.tag["sources"][oldkey],self.item["sources"][newkey])
        self.graph=self.input("global_DAG");self.field=self.graph["original_field"]
        assert self.graph["global_y_exact_unit_expression_defined"] is True
        assert self.graph["five_original_addition_pole_ideals_as_fractional_DAGs_certified"] is True
        nodes={v["id"]:v for v in self.graph["graph_nodes"]}
        assert len(nodes)==len(self.graph["graph_nodes"])
        self.galois_node=nodes[self.graph["original_Galois_automorphism_node"]]
        assert self.galois_node["operation"]=="original_Galois_automorphism_definition"
        assert self.galois_node["data"]["fixes_zeta"] is True
        assert self.galois_node["data"]["fixes_original_z_w_and_normal_basis"] is True
        self.rho_exact={}
        for j in range(1,6):
            out=self.graph["five_original_polar_and_eta_outputs"][str(j)]
            assert out["original_Hom_word"]=="1+T^"+str(j)
            assert int(out["original_map_degree"])==DEGREES[j-1]
            node=nodes[self.graph["relative_original_functions"][str(j)]["rho"]]
            assert node["operation"]=="original_R791_rho_iterate"
            assert node["data"]["original_index"]==j
            self.rho_exact[j]=node["data"]["source_value"]
        place=self.input("original_place")
        assert place["prime"]==P and place["original_branch"]==0 and place["original_field"]==self.field
        assert place["original_integral_B_root"]==3197390 and place["canonical_free_column"]==1186
        assert place["original_s_root"]==99932770 and place["original_zeta_root"]==549966761
        assert place["original_lambda_is_a_unit"] is True
        assert place["original_minimal_polynomials_and_simple_residue_roots_verified"] is True
        self.lam=rational_mod(self.field["lambda"],"original lambda")
        seven=self.input("seven_normal_inputs")
        assert self.sources["AB"].certificate["all_seven_original_Galois_normal_inputs_certified"] is True
        assert self.sources["AB"].certificate["all1380_by12_original_coordinates_verified"] is True
        assert plain(self.sources["AB"].certificate["seven_Galois_normal_inputs"])==plain(self.inputs["seven_normal_inputs"])
        self.ordered=seven["ordered_original_sigma_powers"]
        assert [v["sigma_power"] for v in self.ordered]==list(range(7))
        assert [v["original_branch"] for v in self.ordered]==SIGMA_BRANCHES
        assert seven["normal_basis_degrees"]==EPS and seven["regular_degree_bound"]==5
        assert plain(seven["source_original_global_DAG"])==plain(self.inputs["global_DAG"])
        self.broots=[int(row["roots_B_s"][0])*inverse(self.lam,"lambda")%P for row in self.ordered]
        assert self.broots[0]==int(place["original_b_root"])
        assert all(int(row["roots_B_s"][1])==99932770 for row in self.ordered)
        self.normal=[];self.normal_refs=[]
        A0=self.input("zero_branch_A");B0=self.input("zero_branch_B")
        for data in (A0,B0):
            assert data["prime"]==P and data["original_branch"]==0 and data["canonical_free_column"]==1186
            assert data["normal_basis_degrees"]==EPS and data["regular_degree_bound"]==5
            assert data["all1380_original_short_coordinates_verified"] is True
            assert data["same_original_82power10_scales_preserved"] is True
        assert plain(self.ordered[0]["source_original_A_normal"])==plain(self.inputs["zero_branch_A"])
        assert plain(self.ordered[0]["source_original_B_normal"])==plain(self.inputs["zero_branch_B"])
        self.normal.append([A0["vector_coefficients_mod_prime"],B0["vector_coefficients_mod_prime"]])
        self.normal_refs.append({"A":self.inputs["zero_branch_A"],"B":self.inputs["zero_branch_B"]})
        assert len(self.inputs["other_normal_pairs"])==6
        for r,ref in enumerate(self.inputs["other_normal_pairs"],1):
            data=self.source(ref);order=self.ordered[r]
            assert plain(ref)==plain(order["source_original_normal_pair"])
            assert data["sigma_power"]==r and data["original_branch"]==order["original_branch"]
            assert data["roots_B_s"]==order["roots_B_s"] and data["prime"]==P
            assert data["all1380_original_coordinates_for_each_vector_verified"] is True
            assert data["abstract_p_integral_original_normal_lifts_certified"] is True
            self.normal.append([data["A_vector_coefficients_mod_prime"],data["B_vector_coefficients_mod_prime"]])
            self.normal_refs.append({"A":ref,"B":ref})
        for pair in self.normal:
            for raw in pair:
                shape(raw,6,N)
                assert all(int(raw[k][i])==0 for k in range(6) for i in range(N) if k>5-EPS[i])
        for key in ("global_DAG","original_place","original_W","seven_normal_inputs", "zero_branch_A",
                    "zero_branch_B","g_index","Gamma_index","operator_identity","S5_index"):
            self.same_input("R893",key,key)
        self.operator_indexes={}
        identity_stage=self.input("operator_identity")
        for flag in ("g_first_column_is_original_vg","Gamma_first_column_zero_and_second_column_original_vh",
                     "g_commutator_full_polynomial_identity_certified_by_seven_points",
                     "Gamma_nested_full_polynomial_identity_certified_by_seven_points",
                     "all_sigma_negative_powers_and_original_minus_sign_verified",
                     "all_operators_are_true_original_p_integral_reductions"):
            assert identity_stage[flag] is True
        for target,key in (("g","g_index"),("Gamma","Gamma_index")):
            data=self.input(key)
            assert data["prime"]==P and data["target"]==target and data["chart"]=="tau"
            assert data["normal_basis_degrees"]==EPS and len(data["row_blocks"])==17
            assert data["original_true_operator_reduction_certified"] is True
            assert plain(identity_stage["operator_indexes"][target]["tau"])==plain(self.inputs[key])
            self.operator_indexes[target]=data
        self.S5=self.input("S5_index")
        assert self.S5["dimension"]==1234 and self.S5["integer_scale"]=="13744803133596058624"
        self.mapping=[(v["normal_basis_index"],v["z_degree"]) for v in self.S5["basis_rows"]]
        assert self.mapping==positions(5)
        assert self.sources["R809"].certificate["coefficient_field_basis"]==FIELD_BASIS
        assert self.sources["R809"].certificate["original_b_model"]==self.field["original_b_minimal_polynomial"]
        assert len(self.inputs["C_indexes"])==6
        for j,ref in enumerate(self.inputs["C_indexes"]):
            assert plain(self.sources["R809"].certificate["normal_vectors"]["C"+str(j)])==plain(ref)
        for key in ("point_linear_functional","normal_V3_point_jets","fixed_chi_divisor",
                    "fixed_chi_anchor","t_frame"):
            self.same_input("R896",key,key)
        self.point=self.input("point_linear_functional");self.jets=self.input("normal_V3_point_jets")
        self.zP0=int(self.point["z0_mod_prime"]);self.betaP0=self.point["point_evaluation_mod_prime"]
        assert self.zP0==110702704 and self.point["w0_mod_prime"]==645975656
        assert self.point["chosen_local_parameter"]=="z_minus_z0"
        assert len(self.betaP0)==N and self.betaP0[0]==1
        assert self.jets["row_orders"]==list(range(252)) and self.jets["matrix_shape"]==[252,690]
        assert self.jets["V3_basis"]==[{"normal_basis_row":i,"power_of_z":k} for i,k in self.V3]
        shape(self.jets["matrix_mod_prime"],252,690);self.J3=matrix(self.jets["matrix_mod_prime"])
        chi=self.input("fixed_chi_divisor");u=self.input("fixed_chi_anchor");frame=self.input("t_frame")
        assert chi["actual_complete_fixed_chi_RR_space_certified"] is True
        assert chi["exact_divisor_identity"]=="chi-(D_chi-H)=-div(u/tau^2)"
        assert plain(chi["source_exact_u"])==plain(self.inputs["fixed_chi_anchor"])
        assert u["order272_is_exact"] is True and u["normal_integer_scale_applied_again"] is False
        self.uchi_leading=int(u["exact_order272_unit"]);assert self.uchi_leading%P
        assert frame["original_t_first_order_unit_certified"] is True
        assert frame["exact_zero_not_inferred_from_modular_zero"] is True
        self.t_over_rho=int(frame["original_t_over_rho_constant_mod_prime"]);assert self.t_over_rho==354813668
        assert set(self.inputs["initial_certificates"])==set(self.inputs["low_weight_certificates"])==set(map(str,range(1,6)))
        for j in range(1,6):
            assert plain(self.inputs["initial_certificates"][str(j)])==plain(initial.certificate["complete_initial_RR_certificates"][str(j)])
            assert plain(self.inputs["low_weight_certificates"][str(j)])==plain(low.certificate["complete_direction_certificates"][str(j)])
        assert set(self.inputs["original_algebras"])==set(self.inputs["normal_V3_fibres"])==set(map(str,range(27)))
        self.import_derivatives()
        name="original-source-audit"
        if self.old(name) is None:
            self.put(name,{"prime":P,"sources":{g:identity(v) for g,v in self.item["sources"].items()},
                "inputs":self.inputs,"original_sigma_branch_order":SIGMA_BRANCHES,
                "original_b_roots_in_sigma_order":self.broots,"original_s_root":99932770,
                "normal_basis_degrees":EPS,"original_c0_multiplicity":1,
                "source_original_c0_order_proof":self.sources["R896"].tag["proofs"],
                "all_sigma0_stages_kept_under_original_source_identity":True,
                "strict_fixed_selection_and_integer_anchor_contract":True,
                "only_missing_derivative_is_sigma6_A":True,
                "no_original_Krylov_characteristic_S5_AB_Hom_or_jet_arithmetic_recomputed":True})
        self.checkpoint(name)

    def import_derivatives(self):
        self.derivatives={};self.derivative_refs={}
        assert set(self.inputs["completed_A_derivatives"])==set(map(str,range(6)))
        assert set(self.inputs["completed_B_derivatives"])==set(map(str,range(7)))
        for target,count in (("A",6),("B",7)):
            for r in range(count):
                ref=self.inputs["completed_"+target+"_derivatives"][str(r)]
                obj=self.source(ref)
                assert obj["prime"]==P and obj["normal_basis_degrees"]==EPS
                if target=="B" and r==6:
                    assert obj["sigma_power"]==6 and obj["original_branch"]==SIGMA_BRANCHES[6]
                    assert plain(obj["source_original_B"])==plain(self.normal_refs[6]["B"])
                    assert obj["regular_degree_bounds"]==[7,9]
                    assert obj["first_column_copied_from_actual_completed_derivative_matrices"] is True
                    raw=obj["delta_B_coefficients_mod_prime"]
                else:
                    assert obj["regular_degree_bound"]==7
                    if r or target=="A":
                        assert obj["sigma_power"]==r and obj["target"]==target
                        assert plain(obj["source_original_normal"])==plain(self.normal_refs[r][target])
                    raw=obj["vector_coefficients_mod_prime"]
                shape(raw,8,N)
                assert all(int(raw[k][i])==0 for k in range(8) for i in range(N) if k>7-EPS[i])
                self.derivatives[r,target]=raw;self.derivative_refs[r,target]=ref

    def original_low_chart(self,complete_ref):
        cert=self.source(complete_ref)
        assert cert["complete_characteristic_zero_space_certified"] is True
        assert cert["all_original_rows_times_complete_kernel_zero"] is True
        assert cert["canonical_free_identity_verified"] is True
        raw,rawref=self.inherited("R896",cert["source_canonical_kernel"])
        assert raw["canonical_free_identity_verified"] is True
        assert raw["all_selected_original_rows_times_kernel_zero"] is True
        oldminor=self.resolve("R896",cert["source_selected_unit_inverse"],False)
        return charts.chart_template(complete_ref,oldminor,raw["selected_rows"],raw["pivot_columns"],
            raw["free_columns"],cert["matrix_shape"],cert["actual_rank"],
            {"source_raw_canonical_kernel":rawref,"definition":cert["exact_complete_space_definition"]})

    def template(self,j):
        if j in self.templates:
            return self.templates[j]
        n=POWERS[j-1];d=272*n-126;dim=INITIAL_DIMS[j-1]
        iref=self.inputs["initial_certificates"][str(j)];ic=self.source(iref)
        lref=self.inputs["low_weight_certificates"][str(j)];lc=self.source(lref)
        assert ic["j"]==lc["j"]==j and ic["ordinary_power"]==lc["ordinary_power"]==n
        assert ic["complete_initial_RR_space_certified"] is True
        assert ic["all_complete_fibre_original_A_minus_yB_relations_verified"] is True
        assert lc["complete_original_low_weight_RR_and_marked_principal_certified"] is True
        assert lc["full_original_low_weight_products_and_kernel_rows_verified"] is True
        assert plain(lc["source_complete_initial_RR"])==plain(iref)
        B,Bref=self.inherited("R893",ic["complete_B_kernel"])
        minor,mref=self.inherited("R893",ic["source_original_unit_minor"])
        assert B["canonical_free_identity_verified"] is True
        assert B["all_original_Schur_rows_times_full_kernel_zero"] is True
        exact=B["exact_unit_solve_expression"]
        assert exact["complete_characteristic_zero_rank"]==DEGREES[j-1]
        I=exact["row_indices"];J=exact["pivot_columns"];F=exact["free_columns"]
        assert minor["row_indices"]==I and minor["column_indices"]==J
        assert minor["actual_determinant_mod_prime"]!=0
        initial_chart=charts.chart_template(Bref,mref,I,J,F,[272*FIBRES[j-1]-d,d],DEGREES[j-1],exact)
        selected,sref=self.inherited("R893",ic["source_complete_fibres"])
        nodes=selected["nodes"]
        assert len(nodes)==FIBRES[j-1] and nodes==list(range(FIBRES[j-1]))
        assert selected["all_denominators_units_in_the_whole_fibres"] is True
        assert selected["residue_field_factors_or_multiplicities_removed"] is False
        row_labels=[[i,l] for i in range(N) for l in range(n-EPS[i]+1,len(nodes))]
        assert minor["original_row_labels"]==[row_labels[k] for k in I]
        mapping=positions(n)
        assert B["original_column_mapping"]==[list(x) for x in mapping]
        assert minor["original_column_labels"]==[list(mapping[k]) for k in J]
        interp_ref=self.inputs["initial_scalar_blocks"][str(j)];interp=self.source(interp_ref)
        assert interp["j"]==j and interp["nodes"]==nodes and interp["ordinary_power"]==n
        assert plain(interp["source_complete_fibres"])==plain(sref)
        for m in (n+1,n,n-1):
            b=interp["blocks"][str(m)]
            assert b["interpolation_nodes"]==nodes[:m]
            assert b["both_scalar_Vandermonde_inverse_products_verified"] is True
            shape(b["Lagrange_coefficient_matrix"],m,m)
            shape(b["evaluation_rows_at_all_nodes"],len(nodes),m)
        marked,marked_ref=self.inherited("R896",lc["source_marked_original_pair"])
        assert marked["original_kernel_column"]<dim
        assert marked["actual_A0_P0_value_mod_prime"]!=0
        assert marked["exact_B0_rho_order"]==1
        assert plain(marked["source_complete_B_kernel"])==plain(Bref)
        residual,residual_ref=self.inherited("R896",lc["source_complete_two_B_residual_certificate"])
        B1,B1ref=self.inherited("R896",residual["source_B1"])
        parameter=residual["accepted_B1_integer_parameter"]
        assert isinstance(parameter,int) and 1<=parameter<P
        assert B1["trial"]==parameter and B1["exact_section_definition"]["integer_parameter"]==parameter
        assert B1["exact_section_definition"]["coefficients_are_exact_integer_powers_not_arbitrary_residue_lifts"] is True
        assert plain(B1["source_complete_B_kernel"])==plain(Bref)
        residual_kernel_ref=self.resolve("R896",residual["source_complete_relation_kernel"])
        residual_chart=self.original_low_chart(residual_kernel_ref)
        assert residual_chart["rank"]==690+DELTAS[j-1]
        projected,projected_ref=self.inherited("R896",residual["complete_residual_normal_V3_space"])
        assert projected["actual_projected_rank"]==RESIDUAL_DIMS[j-1]
        U,Uref=self.inherited("R896",lc["complete_padding146_space"])
        pad_kernel_ref=self.resolve("R896",U["source_complete_padding_kernel"])
        pad_chart=self.original_low_chart(pad_kernel_ref)
        assert pad_chart["matrix_shape"]==[PADDING[j-1],RESIDUAL_DIMS[j-1]]
        assert pad_chart["rank"]==PADDING[j-1]
        v,vref=self.inherited("R896",lc["source_unscaled_exact_v"])
        vcolumn=v["exact_section_definition"]["column"]
        assert vcolumn==U["first_unit_next_order_column"]
        assert v["original_scalar_not_rescaled"] is True
        assert v["exact_order_equals_padding_certified"] is True
        bounded,bounded_ref=self.inherited("R896",lc["source_complete_Dstd_certificate"])
        w,wref=self.inherited("R896",bounded["source_exact_w"])
        parameter2=bounded["accepted_second_anchor_parameter"]
        assert isinstance(parameter2,int) and 1<=parameter2<P
        assert w["trial"]==parameter2 and w["exact_section_definition"]["integer_parameter"]==parameter2
        assert w["original_scalar_not_rescaled"] is True
        final_kernel_ref=self.resolve("R896",bounded["source_complete_relation_kernel"])
        final_chart=self.original_low_chart(final_kernel_ref)
        assert final_chart["rank"]==962 and final_chart["matrix_shape"]==[1904,1380]
        final_projected,final_projection_ref=self.inherited("R896",bounded["complete_normal_V3_space"])
        assert final_projected["actual_projected_rank"]==418
        principal,pref=self.inherited("R896",lc["marked_principal_Q"])
        assert principal["actual_Q_rho_order"]==principal["actual_Q_t_order"]==1-DEGREES[j-1]
        assert principal["original_fixed_chi_sign_is_negative_power_in_Q"] is True
        assert principal["exact_principal_and_original_t_leading_defined"] is True
        assert principal["exact_Galois_transport_contract"]["keep_original_indices_and_integer_combinations"] is True
        assert principal["exact_Galois_transport_contract"]["do_not_reselect_anchors_and_relabel_as_conjugates"] is True
        out={"j":j,"n":n,"d":d,"dim":dim,"nodes":nodes,
            "initial_reference":iref,"low_reference":lref,"initial_certificate":ic,
            "initial_B_reference":Bref,"initial_chart":initial_chart,"initial_row_labels":row_labels,
            "source_selected_fibres":sref,"scalar_reference":interp_ref,"scalar":interp,
            "B0_column":marked["original_kernel_column"],"B1_parameter":parameter,
            "marked_reference":marked_ref,"B1_reference":B1ref,
            "residual_chart":residual_chart,"source_residual_certificate":residual_ref,
            "residual_projection_reference":projected_ref,
            "residual_projection_rows":projected["independent_normal_V3_rows"],
            "padding_chart":pad_chart,"source_original_U":Uref,
            "v_column":vcolumn,"source_original_v":vref,"second_parameter":parameter2,
            "source_original_w":wref,"bounded_chart":final_chart,
            "source_original_bounded_certificate":bounded_ref,
            "bounded_projection_reference":final_projection_ref,
            "bounded_projection_rows":final_projected["independent_normal_V3_rows"],
            "source_original_marked_Q":pref,"source_original_Q":principal}
        self.templates[j]=out
        del B;gc.collect()
        return out

    def fibre(self,a):
        if a in self.fibres:
            return self.fibres[a]
        ref=self.inputs["original_algebras"][str(a)];data=self.source(ref)
        assert data["prime"]==P and data["z0"]==a and data["usable"] is True
        assert plain(data["source_original_W"])==plain(self.inputs["original_W"])
        if "source_original_Krylov" in data:
            point,pref=self.inherited("R893",data["source_original_Krylov"])
            assert point["prime"]==P and point["z0"]==a and point["usable"] is True
            assert point["actual_cyclic_rank"]==272 and point["both_inverse_products_verified"] is True
            assert data["original_Krylov_matrix_or_inverse_or_k272_recomputed"] is False
            Wraw=point["W_evaluated_mod_prime"];Kraw=point["Krylov_matrix_mod_prime"]
            Kiraw=point["inverse_Krylov_matrix_mod_prime"]
            chi=data["characteristic_coefficients_ascending_T"]
        else:
            assert data["both_inverse_products_verified"] is True and data["actual_cyclic_rank"]==272
            built,pref=self.inherited("R893",data["source_new_Krylov_matrix"])
            assert built["full_original_characteristic_relation_on_cyclic_vector_verified"] is True
            Wraw=built["W_evaluated_mod_prime"];Kraw=built["Krylov_matrix_mod_prime"]
            Kiraw=data["inverse_Krylov_matrix_mod_prime"]
            chi=built["characteristic_coefficients_ascending_T"]
        assert len(chi)==273 and int(chi[-1])==1
        vref=self.inputs["normal_V3_fibres"][str(a)];normal=self.source(vref)
        assert normal["prime"]==P and normal["z0"]==a
        assert normal["normal_V3_basis"]==[list(p) for p in self.V3]
        assert plain(normal["source_original_W"])==plain(self.inputs["original_W"])
        if "source_complete_original_fibre" in normal:
            assert plain(normal["source_complete_original_fibre"])==plain(ref)
        else:
            assert plain(normal["source_original_Krylov_point"])==plain(pref)
        shape(Wraw,272,272);shape(Kraw,272,272);shape(Kiraw,272,272)
        shape(normal["normal_evaluation_mod_prime"],272,690)
        shape(normal["cyclic_evaluation_mod_prime"],272,690)
        out={"W":matrix(Wraw),"K":matrix(Kraw),"Ki":matrix(Kiraw),"modulus":poly(chi),
            "E":matrix(normal["normal_evaluation_mod_prime"]),
            "CE":matrix(normal["cyclic_evaluation_mod_prime"]),
            "algebra_ref":ref,"normal_ref":vref,"matrix_ref":pref}
        self.fibres[a]=out;return out

    def new_A6_derivative(self):
        name="sigma-06-A-original-derivative";old=self.old(name)
        if old is None:
            blocks=[];whole=[[0]*N for _ in range(10)]
            V=[matrix([[int(self.normal[6][0][k][i])] for i in range(N)]) for k in range(6)]
            for ordinal,first in enumerate(range(0,N,16)):
                stop=min(N,first+16);bn=f"sigma-06-A-original-derivative-rows-{first:03d}"
                block=self.old(bn)
                gref={"source_group":"R827",**plain(self.operator_indexes["g"]["row_blocks"][ordinal])}
                qref={"source_group":"R827",**plain(self.operator_indexes["Gamma"]["row_blocks"][ordinal])}
                if block is None:
                    self.budget();gg=self.source(gref);qq=self.source(qref)
                    for obj,target,degree in ((gg,"g",3),(qq,"Gamma",2)):
                        assert obj["prime"]==P and obj["target"]==target and obj["chart"]=="tau"
                        assert (obj["row_first"],obj["row_stop"])==(first,stop)
                        assert obj["regular_degree_bound"]==degree and obj["original_weighted_support_verified"] is True
                    G=[matrix(raw) for raw in gg["coefficient_matrices_low_to_high"]]
                    Q=[matrix(raw) for raw in qq["coefficient_matrices_low_to_high"]]
                    assert len(G)==6 and len(Q)==5
                    answer=[zero(stop-first,1) for _ in range(10)]
                    for a,op in enumerate(Q):
                        for k,v in enumerate(V):
                            answer[a+k]+=op*v
                    for a,op in enumerate(G):
                        for k in range(1,6):
                            answer[a+k-1]+=(op*V[k])*k
                    raw=[[int(v[i,0]) for i in range(stop-first)] for v in answer]
                    assert all(raw[k][i]==0 for k in range(10) for i in range(stop-first) if k>7-EPS[first+i])
                    block=self.put(bn,{"prime":P,"sigma_power":6,"target":"A",
                        "source_original_normal":self.normal_refs[6]["A"],
                        "source_g_row_block":gref,"source_Gamma_row_block":qref,
                        "row_first":first,"row_stop":stop,"coefficient_rows_mod_prime":raw,
                        "only_previously_missing_sigma6_A_derivative_computed":True,
                        "all_original_weighted_support_zeros_verified":True})
                    self.checkpoint(bn)
                assert block["source_original_normal"]==self.normal_refs[6]["A"]
                assert block["source_g_row_block"]==gref and block["source_Gamma_row_block"]==qref
                for k,row in enumerate(block["coefficient_rows_mod_prime"]):
                    assert len(row)==stop-first;whole[k][first:stop]=row
                blocks.append(self.ref(bn))
            assert not any(whole[k][i] for k in (8,9) for i in range(N))
            old=self.put(name,{"prime":P,"sigma_power":6,"original_branch":SIGMA_BRANCHES[6],
                "target":"A","source_original_normal":self.normal_refs[6]["A"],
                "source_new_derivative_blocks":blocks,"vector_coefficients_mod_prime":whole[:8],
                "normal_basis_degrees":EPS,"regular_degree_bound":7,
                "all_original_weighted_support_zeros_verified":True,
                "exact_original_derivative_formula":"Gamma*a+Mg*partial_z(a)",
                "old_derivatives_or_operators_recomputed":False})
            self.checkpoint(name)
        assert old["source_original_normal"]==self.normal_refs[6]["A"]
        self.derivatives[6,"A"]=old["vector_coefficients_mod_prime"]
        self.derivative_refs[6,"A"]=self.ref(name)

    def hodge(self,r):
        if r in self.C_cache:
            return self.C_cache[r]
        result=[];refs=[]
        for j,iref in enumerate(self.inputs["C_indexes"]):
            name=f"sigma-{r:02d}-C{j}-original-Hodge-normal-reduction";obj=self.old(name)
            index=self.source(iref)
            assert index["target"]=="C"+str(j) and index["regular_degree_bound"]==4
            assert index["normal_basis_degrees"]==EPS and index["all14_original_field_columns_retained"] is True
            assert index["weighted_polynomial_support_verified"] is True
            assert index["literal_tau_factor_highest_S5_coefficients_zero"] is True
            assert index["normal_function"]=="theta*U_"+str(j)+"/tau^4"
            assert index["target_configuration"]["original_b_model"]==self.field["original_b_minimal_polynomial"]
            if obj is None:
                self.budget();normal=[[0]*N for _ in range(5)];indices=[];groups=[]
                for ref0 in index["coordinate_groups"]:
                    ref={"source_group":"R809",**plain(ref0)};group=self.source(ref)
                    assert group["target_configuration"]==index["target_configuration"]
                    assert group["coefficient_field_basis"]==FIELD_BASIS
                    assert group["all1380_original_coordinates_verified"] is True
                    assert group["original_field_and_scalar_normalizations_preserved"] is True
                    assert plain(group["S5_basis_index"])==plain(self.inputs["S5_index"])
                    cols=group["column_indices"];assert len(cols)==7
                    shape(group["coordinate_numerators"],1234,7)
                    coeff=[]
                    for local,k in enumerate(cols):
                        scale=rational_mod(group["original_target_rational_scales"][local],"original C scale")
                        den=inverse(group["column_denominators"][local],"original C coordinate denominator")
                        coeff.append(scale*den*pow(self.broots[r],k%7,P)*(99932770 if k>=7 else 1)%P)
                    for row,(i,power) in enumerate(self.mapping):
                        numerators=group["coordinate_numerators"][row]
                        if power>4-EPS[i]:
                            assert all(int(x)==0 for x in numerators)
                        else:
                            normal[power][i]=(normal[power][i]+sum(int(x)*c for x,c in zip(numerators,coeff)))%P
                    indices.extend(cols);groups.append(ref)
                assert indices==list(range(14))
                obj=self.put(name,{"prime":P,"sigma_power":r,"original_branch":SIGMA_BRANCHES[r],
                    "original_b_root":self.broots[r],"target":"C"+str(j),
                    "source_original_index":iref,"source_original_groups":groups,
                    "source_original_S5_index":self.inputs["S5_index"],
                    "vector_coefficients_mod_prime":normal,"normal_basis_degrees":EPS,
                    "regular_degree_bound":4,"all14_original_field_columns_consumed":True,
                    "original_scales_applied_exactly_once":True,
                    "old_exact_C_coordinates_or_S5_arithmetic_recomputed":False})
                self.checkpoint(name)
            assert obj["original_b_root"]==self.broots[r] and obj["source_original_index"]==iref
            result.append(obj["vector_coefficients_mod_prime"]);refs.append(self.ref(name))
        self.C_cache[r]=(result,refs);return result,refs

    def element(self,raw,a,Ki):
        normal=matrix([[sum(int(raw[k][i])*pow(a,k,P) for k in range(len(raw)))%P] for i in range(N)])
        cyclic=Ki*normal
        return poly([int(cyclic[i,0]) for i in range(N)])

    def single_denominator(self,j,r,a):
        name=self.stem(j,r)+f"-node-{a:06d}-single-denominator";obj=self.old(name)
        if obj is not None:
            if not obj["whole_fibre_unit"]:
                raise UnitFailure("Fixed original node has a nonunit conjugate denominator: "+name)
            return obj,self.ref(name)
        self.budget();fibre=self.fibre(a);modulus=fibre["modulus"];Ki=fibre["Ki"]
        other=(r+j)%7;rho=original_QK(self.rho_exact[j],self.broots[r],"true conjugate rho")
        assert pow(rho,6,P)*self.broots[r]%P==self.broots[other]
        phase=inverse(pow(rho,3,P),"true conjugate rho cube")
        H,Hrefs=self.hodge(r)
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
        A=self.element(self.normal[r][0],a,Ki);B=self.element(self.normal[r][1],a,Ki)
        C=self.element(self.normal[other][0],a,Ki)*phase
        D=self.element(self.normal[other][1],a,Ki)
        dA=self.element(self.derivatives[r,"A"],a,Ki);dB=self.element(self.derivatives[r,"B"],a,Ki)
        dC=self.element(self.derivatives[other,"A"],a,Ki)*phase
        dD=self.element(self.derivatives[other,"B"],a,Ki)
        c0=self.element(H[0],a,Ki);cj=self.element(H[j],a,Ki)
        F=(mul(A,A)-mul(B,B)*self.broots[r])%modulus
        Fj=(mul(C,C)-mul(D,D)*self.broots[r])%modulus
        W=(mul(B,dA)-mul(A,dB))%modulus;Wj=(mul(D,dC)-mul(C,dD))%modulus
        R=mul(mul(cj,Fj),W);S=mul(mul(c0,F),Wj)
        Delta=(R-S)%modulus;Xi=(mul(C,B)-mul(A,D))%modulus
        Q=mul(mul(B,power(D,3)),power(Delta,3))
        numerator=(-mul(mul(A,power(D,3)),power(Delta,3))+
            mul(mul(mul(Xi,power(D,2)),power(Delta,2)),2*S+R)-
            mul(mul(mul(power(Xi,3),power(c0,3)),power(F,2)),power(Wj,3)))%modulus
        gcd,u,v=Q.xgcd(modulus);assert u*Q+v*modulus==gcd
        unit=gcd.degree()==0 and int(gcd[0])!=0
        payload={"prime":P,"original_direction":j,"sigma_power":r,"original_branch":SIGMA_BRANCHES[r],
            "z0":a,"source_original_complete_fibre":fibre["algebra_ref"],
            "source_global_DAG":self.inputs["global_DAG"],
            "source_original_zero_power_pole_ideal_nodes":self.graph["five_original_polar_and_eta_outputs"][str(j)]["global_pole_ideals"],
            "exact_pole_ideal_transport":{"operation":"apply_original_constant_field_Galois","sigma_power":r,
                "source_original_galois_node":self.graph["original_Galois_automorphism_node"]},
            "source_normal_pairs":[self.normal_refs[r],self.normal_refs[other]],
            "source_Hodge_reductions":[Hrefs[0],Hrefs[j]],
            "source_derivatives":[self.derivative_refs[r,"A"],self.derivative_refs[r,"B"],
                                  self.derivative_refs[other,"A"],self.derivative_refs[other,"B"]],
            "original_b_root":self.broots[r],"original_other_sigma_power":other,
            "actual_sigma_r_rho_j_mod_prime":rho,"original_rho_phase_applied_once":True,
            "complete_algebra_modulus":pack(modulus,273),
            "P_coefficients_ascending_w":pack(numerator,272),"Q_coefficients_ascending_w":pack(Q,272),
            "gcd_with_full_characteristic":pack(gcd),"Bezout_Q_coefficient":pack(u),
            "Bezout_characteristic_coefficient":pack(v),"full_polynomial_Bezout_identity_verified":True,
            "whole_fibre_unit":unit,"factors_or_nilpotents_removed":False,
            "single_F_cancelled_exactly_once":True,"extra_F_C0_Wj_unit_conditions_imposed":False,
            "common_homogeneous_weight":98,"direct_sigma_chart_weight":95,
            "old_original_node_replaced":False,"old_Krylov_or_characteristic_arithmetic_recomputed":False}
        if unit:
            qinv=u*inverse(int(gcd[0]),"whole fibre constant gcd")%modulus
            y=mul(numerator,qinv)
            assert mul(Q,qinv)==poly([1]) and mul(Q,y)==numerator
            normal=fibre["K"]*matrix([[int(y[i])] for i in range(N)])
            payload.update({"Q_inverse_coefficients_ascending_w":pack(qinv,272),
                "y_coefficients_ascending_w":pack(y,272),
                "y_normal_coordinates_mod_prime":[int(normal[i,0]) for i in range(N)],
                "whole_Q_times_inverse_equals_one":True,"all272_original_Q_times_y_equals_P_verified":True})
        obj=self.put(name,payload);self.checkpoint(name)
        if not unit:
            raise UnitFailure("Fixed original node has a nonunit conjugate denominator: "+name)
        return obj,self.ref(name)

    def multiplier(self,j,r,a):
        key=(j,r,a)
        if key in self.new_multipliers:
            return self.new_multipliers[key]
        name=self.stem(j,r)+f"-node-{a:06d}-normal-multiplier";obj=self.old(name)
        single,sref=self.single_denominator(j,r,a)
        if obj is None:
            self.budget();fibre=self.fibre(a)
            section=matrix([[int(x)] for x in single["y_normal_coordinates_mod_prime"]])
            current=section;columns=[]
            for k in range(N):
                columns.append([int(current[i,0]) for i in range(N)])
                if k+1<N:
                    current=fibre["W"]*current
            KY=matrix(columns).transpose();M=KY*fibre["Ki"]
            assert M*fibre["K"]==KY and sub(M,list(range(N)),[0])==section
            obj=self.put(name,{"prime":P,"original_direction":j,"sigma_power":r,"z0":a,
                "source_actual_single_denominator":sref,
                "source_original_algebra":fibre["algebra_ref"],
                "normal_multiplication_matrix_mod_prime":rows(M),
                "all272_original_cyclic_action_columns_multiplied_back":True,
                "first_column_is_actual_complete_conjugate_y":True,
                "old_original_Krylov_inverse_recomputed":False})
            self.checkpoint(name)
        assert obj["source_actual_single_denominator"]==sref
        out=(matrix(obj["normal_multiplication_matrix_mod_prime"]),self.ref(name))
        self.new_multipliers[key]=out;return out

    def evaluate_columns(self,M,n,a):
        assert M.nrows()==272*n-126
        answer=[];offset=0
        for i in range(N):
            m=n-EPS[i]+1
            block=sub(M,list(range(offset,offset+m)),list(range(M.ncols())))
            v=matrix([[pow(a,k,P) for k in range(m)]])*block
            answer.append([int(v[0,k]) for k in range(M.ncols())]);offset+=m
        assert offset==M.nrows()
        return matrix(answer)

    def initial_two_columns(self,j,r,T):
        stem=self.stem(j,r);n=T["n"];d=T["d"];dim=T["dim"];rank=DEGREES[j-1]
        chart=T["initial_chart"];I=chart["selected_rows"];J=chart["pivot_columns"];F=chart["free_columns"]
        nodes=T["nodes"];mapping=positions(n)
        weights=matrix([[int(i==T["B0_column"]),pow(T["B1_parameter"],i,P)] for i in range(dim)])
        freearray=[[0,0] for _ in range(d)]
        for i,col in enumerate(F):
            freearray[col]=[int(weights[i,k]) for k in range(2)]
        freepolys=matrix(freearray);forcing=[];forcing_refs=[];multipliers=[];multiplier_refs=[]
        for a in nodes:
            M,mref=self.multiplier(j,r,a);multipliers.append(M);multiplier_refs.append(mref)
            name=stem+f"-node-{a:06d}-two-free-coordinate-forcing";obj=self.old(name)
            if obj is None:
                self.budget();freevalue=self.evaluate_columns(freepolys,n,a);answer=M*freevalue
                obj=self.put(name,{"prime":P,"original_direction":j,"sigma_power":r,"z0":a,
                    "source_original_chart":chart,"source_conjugate_y_multiplier":mref,
                    "original_B0_column":T["B0_column"],"original_B1_integer_parameter":T["B1_parameter"],
                    "free_polynomial_values_mod_prime":rows(freevalue),
                    "y_times_free_polynomial_values_mod_prime":rows(answer),"matrix_shape":[272,2],
                    "exact_free_weights_are_original_integer_vectors":True})
                self.checkpoint(name)
            assert obj["source_conjugate_y_multiplier"]==mref
            forcing.append(matrix(obj["y_times_free_polynomial_values_mod_prime"]));forcing_refs.append(self.ref(name))
        chosen={i:[] for i in range(N)}
        for original_row in I:
            i,l=T["initial_row_labels"][original_row];chosen[i].append((original_row,l))
        selected_blocks=[];square_rows=[];rhs_rows=[];all_labels=[]
        for first in range(0,N,16):
            stop=min(N,first+16);name=stem+f"-selected-Schur-rows-{first:03d}";obj=self.old(name)
            if obj is None:
                self.budget();raw=[];rhs=[];labels=[]
                for i in range(first,stop):
                    if not chosen[i]:
                        continue
                    m=n-EPS[i]+1;later=[l for _,l in chosen[i]]
                    prior_rows=list(range(m));all_needed=prior_rows+later
                    H=matrix([[int(multipliers[l][i,mapping[col][0]])*pow(nodes[l],mapping[col][1],P)%P
                               for col in J] for l in all_needed])
                    Hfree=matrix([[int(forcing[l][i,k]) for k in range(2)] for l in all_needed])
                    L=matrix([T["scalar"]["blocks"][str(m)]["evaluation_rows_at_all_nodes"][l] for l in later])
                    local= sub(H,list(range(m,len(all_needed))),list(range(rank)))-L*sub(H,prior_rows,list(range(rank)))
                    localrhs=sub(Hfree,list(range(m,len(all_needed))),[0,1])-L*sub(Hfree,prior_rows,[0,1])
                    raw.extend(rows(local));rhs.extend(rows(localrhs));labels.extend([v[0] for v in chosen[i]])
                obj=self.put(name,{"prime":P,"original_direction":j,"sigma_power":r,
                    "source_original_chart":chart,"source_old_scalar_blocks":T["scalar_reference"],
                    "source_conjugate_y_multipliers":multiplier_refs,"source_free_forcing":forcing_refs,
                    "normal_output_interval":[first,stop],"original_Schur_row_indices":labels,
                    "selected_pivot_columns":J,"selected_square_rows_mod_prime":raw,
                    "two_free_RHS_rows_mod_prime":rhs,
                    "Schur_sign":"H_remaining-Lambda*H_selected",
                    "full_new_Schur_or_full_free_column_solve_materialized":False})
                self.checkpoint(name)
            assert obj["source_original_chart"]==chart
            assert obj["source_conjugate_y_multipliers"]==multiplier_refs
            assert obj["source_free_forcing"]==forcing_refs
            square_rows.extend(obj["selected_square_rows_mod_prime"])
            rhs_rows.extend(obj["two_free_RHS_rows_mod_prime"])
            all_labels.extend(obj["original_Schur_row_indices"]);selected_blocks.append(self.ref(name))
        assert all_labels==I
        shape(square_rows,rank,rank);shape(rhs_rows,rank,2)
        definition={"operation":"strict_original_constant_field_Galois_transport","sigma_power":r,
            "source_original_complete_initial_space":T["initial_reference"],
            "source_original_marked_B0":T["marked_reference"],"source_original_B1":T["B1_reference"],
            "original_B0_column":T["B0_column"],"original_B1_integer_parameter":T["B1_parameter"],
            "all_original_fibres_unchanged":nodes,"source_global_DAG":self.inputs["global_DAG"]}
        B,Bdata,Bref=charts.solve_fixed_two_rhs(self,stem+"-initial",matrix(square_rows),matrix(rhs_rows),chart,
            weights,selected_blocks,definition)
        del square_rows,rhs_rows,freearray,freepolys;gc.collect()
        values=[];value_refs=[]
        for a,M,mref in zip(nodes,multipliers,multiplier_refs):
            name=stem+f"-node-{a:06d}-two-complete-B-values";obj=self.old(name)
            if obj is None:
                self.budget();vb=self.evaluate_columns(B,n,a);target=M*vb
                cyclic=self.fibre(a)["Ki"]*vb
                obj=self.put(name,{"prime":P,"original_direction":j,"sigma_power":r,"z0":a,
                    "source_actual_two_B_columns":Bref,"source_actual_y_multiplier":mref,
                    "B_fibre_values_mod_prime":rows(vb),"B_cyclic_values_mod_prime":rows(cyclic),
                    "y_times_B_fibre_values_mod_prime":rows(target),"matrix_shape":[272,2],
                    "all272_fibre_coordinates_retained":True,"materialized_initial_B_columns":2,
                    "full_conjugate_initial_B_basis_numerically_materialized":False})
                self.checkpoint(name)
            assert obj["source_actual_two_B_columns"]==Bref and obj["source_actual_y_multiplier"]==mref
            values.append(matrix(obj["y_times_B_fibre_values_mod_prime"]));value_refs.append(self.ref(name))
        aname=stem+"-two-initial-A-columns";Adata=self.old(aname)
        if Adata is None:
            self.budget();raw=[]
            for i in range(N):
                m=n-EPS[i]+1
                target=matrix([[int(values[l][i,k]) for k in range(2)] for l in range(m)])
                L=matrix(T["scalar"]["blocks"][str(m)]["Lagrange_coefficient_matrix"])
                raw.extend(rows(L*target))
            shape(raw,d,2)
            Adata=self.put(aname,{"prime":P,"original_direction":j,"sigma_power":r,
                "ordinary_power":n,"source_actual_two_B_columns":Bref,
                "source_old_scalar_blocks":T["scalar_reference"],"source_complete_yB_values":value_refs,
                "A_coefficients_mod_prime":raw,"matrix_shape":[d,2],
                "exact_formula":"A=old_scalar_Lagrange*(Y*E*B)_selected",
                "new_dense_A_inverse_or_full_initial_A_basis_materialized":False})
            self.checkpoint(aname)
        assert Adata["source_actual_two_B_columns"]==Bref
        A=matrix(Adata["A_coefficients_mod_prime"]);checks=[]
        for a,target,vref in zip(nodes,values,value_refs):
            name=stem+f"-node-{a:06d}-all-original-two-column-relations";obj=self.old(name)
            if obj is None:
                self.budget();assert self.evaluate_columns(A,n,a)==target
                obj=self.put(name,{"prime":P,"original_direction":j,"sigma_power":r,"z0":a,
                    "source_actual_two_A_columns":self.ref(aname),"source_actual_two_B_columns":Bref,
                    "source_actual_complete_B_values":vref,"checked_shape":[272,2],
                    "all_original_A_minus_yB_coordinates_zero":True,
                    "factors_multiplicities_or_rows_removed":False})
                self.checkpoint(name)
            assert obj["source_actual_two_A_columns"]==self.ref(aname)
            checks.append(self.ref(name))
        name=stem+"-complete-initial-space-and-two-columns-certificate";cert=self.old(name)
        if cert is None:
            cert=self.put(name,{"prime":P,"original_direction":j,"sigma_power":r,"original_branch":SIGMA_BRANCHES[r],
                "source_original_complete_initial_space":T["initial_reference"],
                "source_original_low_weight_direction":T["low_reference"],
                "source_actual_unit_minor":Bdata["source_actual_conjugate_unit_minor"],
                "source_actual_two_B_columns":Bref,"source_actual_two_A_columns":self.ref(aname),
                "source_all_original_relations":checks,"source_all_complete_B_values":value_refs,
                "original_nodes":nodes,"all_original_rows_checked":272*len(nodes),
                "complete_initial_space_exact_unit_solve_defined":True,
                "actual_complete_initial_space_dimension":dim,"materialized_initial_B_columns":2,
                "full_conjugate_initial_B_basis_numerically_materialized":False,
                "all_original_two_column_A_minus_yB_relations_verified":True,
                "strict_original_selection_and_integer_anchors_preserved":True,
                "exact_two_columns_are_original_B0_B1_conjugates":True,
                "all_factors_and_multiplicities_retained":True,
                "characteristic_zero_coefficients_expanded":False})
            self.checkpoint(name)
        return A,B,self.ref(aname),Bref,{a:v for a,v in zip(nodes,value_refs)},self.ref(name)

    def marked_pair(self,j,r,T,A,B,Aref,Bref,initial_ref):
        name=self.stem(j,r)+"-original-unscaled-marked-A-B";obj=self.old(name)
        if obj is None:
            self.budget();eval0=[];eval1=[]
            beta1=[int(self.J3[1,self.V3map[(i,0)]]) for i in range(N)]
            assert beta1[0]==0 and int(self.J3[1,self.V3map[(0,1)]])==1
            for i,k in positions(T["n"]):
                power=pow(self.zP0,k,P)
                eval0.append(power*int(self.betaP0[i])%P)
                eval1.append((power*beta1[i]+(k*pow(self.zP0,k-1,P)*int(self.betaP0[i]) if k else 0))%P)
            A0=matrix([eval0])*A;B0=matrix([eval0])*B;B1=matrix([eval1])*B
            av=int(A0[0,0]);first=int(B1[0,0])
            assert int(B0[0,0])==int(B0[0,1])==0
            refs={"source_actual_two_A_columns":Aref,"source_actual_two_B_columns":Bref,
                  "source_original_marked_pair":T["marked_reference"]}
            self.fail_scalar(name+"-A0-unit-failure",av,"The inherited original A0 column is nonunit at P0",refs)
            self.fail_scalar(name+"-B0-first-unit-failure",first,"The inherited original B0 first coefficient is nonunit",refs)
            obj=self.put(name,{"prime":P,"original_direction":j,"sigma_power":r,"original_branch":SIGMA_BRANCHES[r],
                **refs,"source_actual_initial_two_column_certificate":initial_ref,
                "source_original_P0":self.inputs["point_linear_functional"],
                "source_completed_normal_V3_jets":self.inputs["normal_V3_point_jets"],
                "original_kernel_column":T["B0_column"],"ordinary_power":T["n"],
                "A_coordinates_mod_prime":[int(A[i,0]) for i in range(T["d"])],
                "B_coordinates_mod_prime":[int(B[i,0]) for i in range(T["d"])],
                "actual_A0_P0_value_mod_prime":av,"actual_B0_constant_mod_prime":0,
                "actual_B0_first_coefficient_mod_prime":first,
                "exact_B0_rho_order":1,"F0_degree":DELTAS[j-1],"F0_avoids_original_P0":True,
                "exact_zero_follows_from_true_conjugation_of_original_relation_and_c0_pole":True,
                "exact_zero_not_inferred_from_modular_zero":True,
                "original_scalar_not_rescaled":True,
                "no_new_P0_column_selection_performed":True,
                "exact_definition":{"operation":"original_constant_field_Galois_transport",
                    "sigma_power":r,"source_original_marked_pair":T["marked_reference"],
                    "actual_same_chart_two_RHS_source":Bref}})
            self.checkpoint(name)
        assert obj["source_actual_two_B_columns"]==Bref
        othername=self.stem(j,r)+"-original-integer-B1";other=self.old(othername)
        if other is None:
            other=self.put(othername,{"prime":P,"original_direction":j,"sigma_power":r,
                "source_original_B1":T["B1_reference"],"source_actual_two_B_columns":Bref,
                "original_integer_parameter":T["B1_parameter"],
                "B_coordinates_mod_prime":[int(B[i,1]) for i in range(T["d"])],
                "original_scalar_not_rescaled":True,
                "exact_definition":{"operation":"original_constant_field_Galois_transport",
                    "sigma_power":r,"source_original_B1":T["B1_reference"],
                    "original_integer_parameter":T["B1_parameter"],
                    "actual_same_chart_two_RHS_source":Bref}})
            self.checkpoint(othername)
        assert other["source_actual_two_B_columns"]==Bref
        return obj,self.ref(name),other,self.ref(othername)

    def products(self,stem,T,anchor_ref,vector=None,initial_values=None,initial_column=None):
        is_initial=initial_values is not None
        assert is_initial==(initial_column is not None)
        assert is_initial==(vector is None)
        nodes=T["nodes"] if is_initial else T["nodes"][:7]
        refs=[];raw=[]
        for a in nodes:
            name=stem+f"-node-{a:06d}-times-normal-V3";obj=self.old(name)
            if obj is None:
                self.budget();fibre=self.fibre(a)
                if is_initial:
                    values=self.own(initial_values[a])["B_fibre_values_mod_prime"]
                    shape(values,272,2)
                    section=matrix([[int(row[initial_column])] for row in values])
                else:
                    assert len(vector)==690
                    section=fibre["E"]*matrix([[int(x)] for x in vector])
                current=section;columns=[]
                for k in range(N):
                    columns.append([int(current[i,0]) for i in range(N)])
                    if k+1<N:
                        current=fibre["W"]*current
                product=matrix(columns).transpose()*fibre["CE"]
                obj=self.put(name,{"prime":P,"z0":a,"source_actual_conjugate_anchor":anchor_ref,
                    "source_original_complete_fibre":fibre["algebra_ref"],
                    "source_original_normal_V3_fibre":fibre["normal_ref"],
                    "source_already_completed_two_B_values":initial_values[a] if is_initial else None,
                    "initial_B_column":initial_column,
                    "section_evaluation_mod_prime":[int(section[i,0]) for i in range(N)],
                    "product_evaluation_mod_prime":rows(product),"matrix_shape":[272,690],
                    "all272_original_fibre_coordinates_retained":True,
                    "formula":"[v,Wv,...,W^271v]*(old_Kinverse*normal_V3)",
                    "old_Krylov_inverse_normal_V3_or_initial_AB_values_recomputed":False})
                self.checkpoint(name)
            assert obj["source_actual_conjugate_anchor"]==anchor_ref
            assert obj["initial_B_column"]==initial_column
            shape(obj["product_evaluation_mod_prime"],272,690)
            raw.extend(obj["product_evaluation_mod_prime"]);refs.append(self.ref(name))
        return matrix(raw),refs

    def low_weight(self,j,r,T,marked,marked_ref,B1ref,initial_values,initial_ref):
        stem=self.stem(j,r)
        left,lrefs=self.products(stem+"-B0",T,marked_ref,initial_values=initial_values,initial_column=0)
        right,rrefs=self.products(stem+"-B1",T,B1ref,initial_values=initial_values,initial_column=1)
        M=hcat(left,right)
        exact={"operation":"original_constant_field_Galois_transport","sigma_power":r,
            "source_original_complete_kernel":T["residual_chart"]["source_original_complete_kernel"],
            "source_actual_B0":marked_ref,"source_actual_B1":B1ref,
            "source_actual_initial_two_columns":initial_ref,"original_integer_parameter":T["B1_parameter"],
            "source_B0_products":lrefs,"source_B1_products":rrefs,
            "original_nodes":T["nodes"],"N_strictly_greater_than_weight_n_plus3":len(T["nodes"])>T["n"]+3,
            "complete_space":"relations B0*r+B1*s=0 in V3^2"}
        K,kdata,kref=charts.solve_fixed_unit_kernel(self,stem+"-two-B",M,T["residual_chart"],exact)
        F,Fdata,Fref=charts.fixed_second_projection(self,stem+"-complete-F0-normal-space",K,kref,
            T["residual_projection_reference"],T["residual_projection_rows"],RESIDUAL_DIMS[j-1],
            {"space":"sigma^r H0(3H-F0)","sigma_power":r,
             "source_original_complete_residual_space":T["residual_projection_reference"],
             "source_actual_marked_pair":marked_ref,"degree_F0":DELTAS[j-1],"F0_avoids_P0":True})
        residualname=stem+"-complete-residual-space-certificate";residual=self.old(residualname)
        if residual is None:
            residual=self.put(residualname,{"prime":P,"original_direction":j,"sigma_power":r,
                "source_original_residual_certificate":T["source_residual_certificate"],
                "source_actual_marked_pair":marked_ref,"source_actual_B1":B1ref,
                "source_complete_relation_kernel":kref,"complete_residual_normal_V3_space":Fref,
                "source_B0_products":lrefs,"source_B1_products":rrefs,
                "original_nodes":T["nodes"],"actual_product_rank":690+DELTAS[j-1],
                "actual_residual_dimension":RESIDUAL_DIMS[j-1],
                "strict_original_selection_and_integer_anchors_preserved":True,
                "common_zero_divisor_is_exact_original_E_conjugate":True,
                "complete_conjugate_residual_space_certified":True,
                "all_original_product_rows_verified":True})
            self.checkpoint(residualname)
        residual_ref=self.ref(residualname)
        del left,right,M,K;gc.collect()
        padname=stem+"-padding-original-jet-matrix";pdata=self.old(padname);k=PADDING[j-1]
        if pdata is None:
            self.budget();pad=sub(self.J3,list(range(k)),list(range(690)))*F
            nextrow=sub(self.J3,[k],list(range(690)))*F
            pdata=self.put(padname,{"prime":P,"original_direction":j,"sigma_power":r,
                "source_complete_residual_space":Fref,"source_complete_residual_certificate":residual_ref,
                "source_original_normal_V3_point_jets":self.inputs["normal_V3_point_jets"],
                "matrix_shape":[k,RESIDUAL_DIMS[j-1]],"matrix_mod_prime":rows(pad),
                "next_order":k,"next_order_functional_mod_prime":rows(nextrow)[0],
                "old_point_jets_recomputed":False})
            self.checkpoint(padname)
        assert pdata["source_complete_residual_space"]==Fref
        pad=matrix(pdata["matrix_mod_prime"])
        Ucoeff,Ucert,Ucref=charts.solve_fixed_unit_kernel(self,stem+"-padding",pad,T["padding_chart"],
            {"operation":"original_constant_field_Galois_transport","sigma_power":r,
             "source_original_complete_padding_kernel":T["padding_chart"]["source_original_complete_kernel"],
             "source_actual_residual_space":Fref,"source_actual_jet_matrix":self.ref(padname),
             "space":"H0(3H-sigma(F0)-kP0)","dimension":146})
        uname=stem+"-complete-unscaled-146-normal-space";Udata=self.old(uname)
        if Udata is None:
            self.budget();U=F*Ucoeff
            assert sub(self.J3,list(range(k)),list(range(690)))*U==zero(k,146)
            extra=matrix([pdata["next_order_functional_mod_prime"]])*Ucoeff
            row=rows(extra)[0];selected_value=row[T["v_column"]]
            self.fail_scalar(uname+"-fixed-v-unit-failure",selected_value,
                "The inherited original v column has a nonunit padding coefficient",
                {"source_original_v":T["source_original_v"],"source_actual_padding_kernel":Ucref})
            Udata=self.put(uname,{"prime":P,"original_direction":j,"sigma_power":r,
                "source_original_146_space":T["source_original_U"],
                "source_actual_residual_space":Fref,"source_complete_padding_kernel":Ucref,
                "source_original_normal_V3_point_jets":self.inputs["normal_V3_point_jets"],
                "normal_V3_basis":[list(x) for x in self.V3],"normal_V3_basis_mod_prime":rows(U),
                "matrix_shape":[690,146],"padding_order":k,
                "actual_next_order_coefficients_mod_prime":row,"original_selected_v_column":T["v_column"],
                "actual_original_v_coefficient_is_unit":True,
                "all_padding_rows_times_full146_space_zero":True,
                "complete_conjugate_146_space_certified":True,
                "new_v_column_selection_or_rescaling_performed":False})
            self.checkpoint(uname)
        assert Udata["source_complete_padding_kernel"]==Ucref
        U=matrix(Udata["normal_V3_basis_mod_prime"]);Uref=self.ref(uname)
        vname=stem+"-original-unscaled-v";v=self.old(vname)
        if v is None:
            v=self.put(vname,{"prime":P,"original_direction":j,"sigma_power":r,"role":"v",
                "source_original_v":T["source_original_v"],"source_complete_conjugate_146_space":Uref,
                "original_column":T["v_column"],
                "normal_V3_coordinates_mod_prime":[int(U[i,T["v_column"]]) for i in range(690)],
                "actual_coefficient_at_padding_mod_prime":Udata["actual_next_order_coefficients_mod_prime"][T["v_column"]],
                "padding_order":k,"exact_order_equals_padding_certified":True,
                "exact_definition":{"operation":"original_constant_field_Galois_transport","sigma_power":r,
                    "source_original_v":T["source_original_v"],"source_actual_146_space":Uref,
                    "same_original_column":T["v_column"]},"original_scalar_not_rescaled":True})
            self.checkpoint(vname)
        wname=stem+"-original-integer-second-anchor";w=self.old(wname)
        if w is None:
            self.budget();weights=matrix([[pow(T["second_parameter"],i,P)] for i in range(146)])
            vector=U*weights
            w=self.put(wname,{"prime":P,"original_direction":j,"sigma_power":r,"role":"w",
                "source_original_w":T["source_original_w"],"source_complete_conjugate_146_space":Uref,
                "original_integer_parameter":T["second_parameter"],
                "normal_V3_coordinates_mod_prime":[int(vector[i,0]) for i in range(690)],
                "exact_definition":{"operation":"original_integer_power_combination_of_same_conjugate_146_space",
                    "integer_parameter":T["second_parameter"],"exponents":[0,145]},
                "original_scalar_not_rescaled":True,"new_integer_trial_chosen":False})
            self.checkpoint(wname)
        vref=self.ref(vname);wref=self.ref(wname)
        left,lrefs=self.products(stem+"-v",T,vref,vector=v["normal_V3_coordinates_mod_prime"])
        right,rrefs=self.products(stem+"-w",T,wref,vector=w["normal_V3_coordinates_mod_prime"])
        M=hcat(left,right)
        K,kdata,kref=charts.solve_fixed_unit_kernel(self,stem+"-bounded",M,T["bounded_chart"],
            {"operation":"original_constant_field_Galois_transport","sigma_power":r,
             "source_original_complete_kernel":T["bounded_chart"]["source_original_complete_kernel"],
             "source_actual_v":vref,"source_actual_w":wref,
             "source_v_products":lrefs,"source_w_products":rrefs,
             "original_nodes":T["nodes"][:7],"full_V6_injection_length":1904,
             "original_second_integer_parameter":T["second_parameter"],"complete_relation_dimension":418})
        space,sdata,sref=charts.fixed_second_projection(self,stem+"-Dstd-complete-normal418-space",K,kref,
            T["bounded_projection_reference"],T["bounded_projection_rows"],418,
            {"space":"sigma^r H0(3H-Dstd)","sigma_power":r,
             "source_original_Dstd_space":T["bounded_projection_reference"],
             "source_actual_v":vref,"degree_Dstd":272,"Dstd_avoids_P0":True})
        name=stem+"-complete-Dstd-418-certificate";bounded=self.old(name)
        if bounded is None:
            bounded=self.put(name,{"prime":P,"original_direction":j,"sigma_power":r,
                "source_original_bounded_certificate":T["source_original_bounded_certificate"],
                "source_complete_146_space":Uref,"source_exact_v":vref,"source_exact_w":wref,
                "source_complete_relation_kernel":kref,"complete_normal_V3_space":sref,
                "source_v_products":lrefs,"source_w_products":rrefs,"original_nodes":T["nodes"][:7],
                "actual_product_rank":962,"actual_complete_normal_space_dimension":418,
                "all1904_original_rows_verified":True,"strict_original_selection_and_integer_anchors_preserved":True,
                "full_conjugate_bounded_space_certified":True,"Dstd_degree":272,"Dstd_avoids_P0":True})
            self.checkpoint(name)
        del F,U,Ucoeff,left,right,M,K,space;gc.collect()
        return {"residual_ref":residual_ref,"Fref":Fref,"Uref":Uref,"v":v,"vref":vref,
                "space_ref":sref,"bounded_ref":self.ref(name)}

    def principal(self,j,r,T,marked,marked_ref,initial_ref,low):
        name=self.stem(j,r)+"-original-bounded-divisor-and-marked-principal-Q";obj=self.old(name)
        if obj is not None:
            return obj,self.ref(name)
        self.budget();n=T["n"];degree=DEGREES[j-1];k=PADDING[j-1]
        b1=int(marked["actual_B0_first_coefficient_mod_prime"])
        vk=int(low["v"]["actual_coefficient_at_padding_mod_prime"])
        leadingG=b1*inverse(vk,"inherited v coefficient")%P
        leadingQ=leadingG*pow(inverse(self.uchi_leading,"old chi coefficient"),n-2,P)%P
        cpow=pow(self.t_over_rho,degree-1,P);leadingt=leadingQ*cpow%P
        assert leadingQ and leadingt and 1-k-272*(n-2)==1-degree
        dag=[
            {"id":"B0","operation":"original_conjugated_section_divided_by_tau_power",
             "source":marked_ref,"tau_power":n,"normal_arrays_already_tau_normalized":True},
            {"id":"v","operation":"original_conjugated_section_divided_by_tau_power",
             "source":low["vref"],"tau_power":3,"normal_arrays_already_tau_normalized":True},
            {"id":"G","operation":"divide","numerator":"B0","denominator":"v",
             "homogeneous_formula":"tau^(3-n)*B0/v","homogeneous_tau_exponent":3-n,
             "additional_tau_factor_on_normal_arrays":0},
            {"id":"qchi","operation":"completed_original_K_function",
             "source":self.inputs["fixed_chi_anchor"],"source_divisor_identity":self.inputs["fixed_chi_divisor"],
             "formula":"u_chi/tau^2","fixed_by_original_constant_field_Galois":True},
            {"id":"Q","operation":"multiply","left":"G",
             "right":{"operation":"integer_power","base":"qchi","exponent":-(n-2)}}]
        obj=self.put(name,{"prime":P,"original_direction":j,"j":j,"sigma_power":r,
            "original_branch":SIGMA_BRANCHES[r],"original_b_root":self.broots[r],
            "source_original_sigma0_marked_principal_Q":T["source_original_marked_Q"],
            "source_original_sigma0_complete_low_weight_certificate":T["low_reference"],
            "source_actual_initial_two_column_certificate":initial_ref,
            "source_actual_marked_pair":marked_ref,"source_complete_residual_certificate":low["residual_ref"],
            "source_complete_146_space":low["Uref"],"source_exact_v":low["vref"],
            "source_complete_bounded_certificate":low["bounded_ref"],"complete_normal418_space":low["space_ref"],
            "source_original_fixed_chi_divisor":self.inputs["fixed_chi_divisor"],
            "source_original_chi_anchor":self.inputs["fixed_chi_anchor"],"source_original_t_frame":self.inputs["t_frame"],
            "ordinary_power":n,"original_pole_degree":degree,"P0_pole_multiplicity":1,
            "F0_degree":DELTAS[j-1],"padding_order":k,"Dstd_degree":272,
            "exact_principal_nodes":dag,"exact_principal_root":"Q","Q_root":"Q","G_root":"G",
            "exact_conjugation_definition":{"operation":"apply_original_constant_field_Galois",
                "sigma_power":r,"source_original_Q":T["source_original_marked_Q"],
                "source_original_Q_root":T["source_original_Q"]["Q_root"],
                "source_original_global_DAG":self.inputs["global_DAG"],
                "source_original_galois_node":self.graph["original_Galois_automorphism_node"],
                "same_indices_free_coordinates_integer_anchors_and_unscaled_frames":True},
            "exact_Q_divisor_identity":"sigma^r(E)-deg(E)P0=(sigma^r(Dstd)-H)+(n-2)(Dchi-H)+div(Q)",
            "actual_Q_rho_order":1-degree,"actual_Q_t_order":1-degree,
            "actual_B0_first_coefficient_mod_prime":b1,"actual_v_padding_coefficient_mod_prime":vk,
            "actual_G_rho_leading_mod_prime":leadingG,"actual_chi_order272_coefficient_mod_prime":self.uchi_leading,
            "actual_Q_rho_leading_mod_prime":leadingQ,"actual_Q_t_leading_mod_prime":leadingt,
            "actual_original_t_over_rho_mod_prime":self.t_over_rho,
            "actual_original_t_scaling_power":degree-1,"actual_original_c_power_mod_prime":cpow,
            "exact_marked_leading_expression":{"rho":"B0_first/v_padding*u_chi_272^(-(n-2))",
                "t":"rho_leading*original_c^(deg(E)-1)","source_B0":marked_ref,"source_v":low["vref"],
                "source_u_chi":self.inputs["fixed_chi_anchor"],"source_c":self.inputs["t_frame"]},
            "strict_original_selection_and_integer_anchors_preserved":True,
            "original_fixed_chi_sign_is_negative_power_in_Q":True,
            "original_tau_weight_and_unscaled_constants_preserved":True,
            "exact_principal_and_original_t_leading_defined":True,
            "auxiliary_unit_not_asserted_at41":True,"characteristic_zero_coefficients_expanded":False,
            "Hecke_Picard_support_connection_period_or_height_computed":False})
        self.checkpoint(name);return obj,self.ref(name)

    def direction(self,j,r):
        finalname=self.stem(j,r)+"-complete-low-weight-RR-certificate";old=self.old(finalname)
        if old is not None:
            assert old["complete_strict_conjugate_low_weight_RR_and_marked_principal_certified"] is True
            self.done.setdefault(str(j),{})[str(r)]=self.ref(finalname);return
        self.active_pair=[j,r];T=self.template(j)
        A,B,Aref,Bref,values,initial_ref=self.initial_two_columns(j,r,T)
        marked,mref,B1,B1ref=self.marked_pair(j,r,T,A,B,Aref,Bref,initial_ref)
        low=self.low_weight(j,r,T,marked,mref,B1ref,values,initial_ref)
        principal,pref=self.principal(j,r,T,marked,mref,initial_ref,low)
        self.put(finalname,{"prime":P,"original_direction":j,"sigma_power":r,"original_branch":SIGMA_BRANCHES[r],
            "source_original_sigma0_complete_initial_space":T["initial_reference"],
            "source_original_sigma0_complete_low_weight_space":T["low_reference"],
            "source_actual_initial_space_and_two_columns":initial_ref,
            "source_actual_marked_pair":mref,"source_complete_two_B_residual_certificate":low["residual_ref"],
            "complete_residual_normal_V3_space":low["Fref"],"complete_padding146_space":low["Uref"],
            "source_unscaled_exact_v":low["vref"],"source_complete_Dstd_certificate":low["bounded_ref"],
            "complete_normal418_space":low["space_ref"],"marked_principal_Q":pref,
            "ordinary_power":T["n"],"original_pole_degree":DEGREES[j-1],
            "complete_initial_space_exact_unit_solve_defined":True,
            "actual_complete_initial_space_dimension":INITIAL_DIMS[j-1],"materialized_initial_B_columns":2,
            "full_conjugate_initial_B_basis_numerically_materialized":False,
            "complete_residual_space_certified":True,"residual_dimension":RESIDUAL_DIMS[j-1],
            "complete_146_space_certified":True,"complete_418_space_certified":True,
            "strict_original_selection_and_integer_anchors_preserved":True,
            "all_original_complete_fibre_relations_and_low_weight_kernel_rows_verified":True,
            "complete_strict_conjugate_low_weight_RR_and_marked_principal_certified":True,
            "original_tau_weight_negative_chi_power_and_t_frame_preserved":True,
            "old_sigma0_Krylov_Schur_derivatives_or_jets_recomputed":False,
            "characteristic_zero_coefficients_expanded":False,
            "Hecke_Picard_support_connection_period_or_height_computed":False})
        self.done.setdefault(str(j),{})[str(r)]=self.ref(finalname)
        self.checkpoint(finalname);self.new_multipliers={}
        del A,B;gc.collect()

    def inventory(self):
        files=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name==PREFIX+"current.json.gz" or path.name.startswith(PREFIX+"stage-manifest-"):
                continue
            value0=read(path)
            assert value0["result"]==RESULT and value0["configuration"]==self.tag and value0["complete"] is True
            files.append(spec(path))
        name="stage-manifest-"+fingerprint({"files":files,"current":self.current})
        self.put(name,{"files":files,"file_count":len(files),"files_sha256":fingerprint(files),
            "current_checkpoints":[self.current] if self.current is not None else [],
            "only_complete_atomic_new_stages_listed":True,"original_source_files_not_retagged":True})
        return self.ref(name)

    def finish(self,complete,reason):
        for j,r in STRATEGY["fixed_task_order"]:
            name=self.stem(j,r)+"-complete-low-weight-RR-certificate"
            obj=self.old(name)
            if obj is not None:
                assert obj["complete_strict_conjugate_low_weight_RR_and_marked_principal_certified"] is True
                self.done.setdefault(str(j),{})[str(r)]=self.ref(name)
        count=sum(len(v) for v in self.done.values());assert not complete or count==30
        current=self.checkpoint(self.phase)
        final={"result":RESULT,"configuration":self.tag,"complete":bool(complete),"p":41,"prime":P,
            "source_audit":self.refs.get("original-source-audit"),
            "original_sigma0_direction_certificates":self.inputs.get("low_weight_certificates",{}),
            "complete_direction_conjugate_certificates":self.done,"actual_complete_conjugate_count":count,
            "all_thirty_strict_conjugate_complete_low_weight_spaces_certified":count==30,
            "source_original_t_frame":self.inputs.get("t_frame"),
            "source_new_sigma6_A_derivative":self.refs.get("sigma-06-A-original-derivative"),
            "complete_initial_spaces_defined_by_original_unit_charts":True,
            "materialized_initial_B_columns_per_completed_pair":2,
            "full_conjugate_initial_B_bases_numerically_materialized":False,
            "complete_later146_and418_kernels_not_reduced_to_two_columns":True,
            "strict_original_selection_and_integer_anchors_preserved":True,
            "sigma0_or_old_Krylov_characteristic_S5_AB_derivatives_jets_recomputed":False,
            "characteristic_zero_coefficients_expanded":False,
            "Hecke_Picard_support_connection_period_or_height_computed":False,
            "stage_manifest":self.inventory(),"resume_state":current,
            "scope_stop_reason":reason,"seconds":time.monotonic()-self.started}
        save(self.out/FINAL,final)
        print("R902_FINAL_SUMMARY="+json.dumps({key:final[key] for key in (
            "complete","actual_complete_conjugate_count",
            "all_thirty_strict_conjugate_complete_low_weight_spaces_certified",
            "materialized_initial_B_columns_per_completed_pair","scope_stop_reason","seconds")}),flush=True)
        return final

    def run(self):
        existing=self.out/FINAL
        if existing.exists():
            final=read(existing)
            assert final["configuration"]==self.tag
            if final["complete"]:
                return final
        self.prepare();self.new_A6_derivative()
        for ordinal,(j,r) in enumerate(STRATEGY["fixed_task_order"]):
            if ordinal>=self.limit:
                return self.finish(False,"scope_pair_limit_reached")
            self.budget();self.direction(j,r)
        self.active_pair=None
        return self.finish(True,None)

def main():
    guard();sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    parser.add_argument("--config",required=True);parser.add_argument("--retained",required=True)
    parser.add_argument("--output",required=True);parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args();out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    assert 0<args.budget_minutes<=300
    job=None;code=1;error=None;final=None;started=time.monotonic()
    try:
        job=Job(args);final=job.run();code=0 if final["complete"] else 2
    except BudgetStop as exc:
        code=124;error={"type":"BudgetStop","message":str(exc)}
        if job is not None:
            final=job.finish(False,"budget")
    except (UnitFailure,charts.FixedChartNonunit,ScopeStop) as exc:
        code=2;error={"type":type(exc).__name__,"message":str(exc)}
        if job is not None:
            final=job.finish(False,str(exc))
    except Exception as exc:
        error={"type":type(exc).__name__,"message":str(exc)};traceback.print_exc()
        if job is not None:
            try:
                final=job.finish(False,"unexpected_error")
            except Exception:
                traceback.print_exc()
    receipt={"result":RESULT,"source_sha256":sha(__file__),"complete":code==0,
        "configuration":job.tag if job is not None else None,
        "configuration_sha256":fingerprint(job.tag) if job is not None else None,
        "process_exit_code":code,"error":error,"seconds":time.monotonic()-started,
        "certificate_sha256":sha(out/FINAL) if (out/FINAL).exists() else None,
        "actual_completed_conjugates":sum(len(v) for v in job.done.values()) if job is not None else 0,
        "all_new_mathematics_only_in_original_public_Actions":True}
    save(out/"core-receipt.json",receipt)
    print("R902_CORE_RECEIPT="+json.dumps(receipt,sort_keys=True),flush=True)
    return code

if __name__=="__main__":
    raise SystemExit(main())

