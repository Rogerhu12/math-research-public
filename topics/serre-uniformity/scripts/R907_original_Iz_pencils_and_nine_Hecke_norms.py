#!/usr/bin/env python3
"""R907 actual original Iz pencils and nine complete-Artin Hecke norms."""
import argparse
import gc
import gzip
import hashlib
import importlib.util
import itertools
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import time
import traceback
import flint
from flint import nmod_mat
import R885_whole_Artin_algebra as algebra
import R907_complete_pencil_norm_algebra as pencil_algebra

REPOSITORY="Rogerhu12/math-research-public"
RESULT="R907-original-Iz-pencils-and-nine-Hecke-norm-generators"
FINAL="p41-original-Iz-pencils-and-nine-Hecke-norm-generators-certificate.json"
PREFIX="R907-"
P=1000000753
EPS=[0]+[1]*144+[2]*127
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
RHO_ORDERS=[-686,-182,-231,-707,-1659]
POWERS=[12,8,8,13,14]
PNUM=[165,93,100,168,371]
QDEN=[67,67,67,67,134]
SIGMA_BRANCHES=[0,6,1,2,4,3,5]
ARTIN_SHA="e47cd50d254700b98446866297d79694c100f1435c46f3b4f42e3835763f897d"
STRATEGY={
    "original_curve":"genus127 Y, p41, level82, original minus3 descent",
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "normal_basis_degrees":EPS,
    "space":"R903 H0(3H-DZ-Dchi-18P0), dim128, positive Phi=QZ/qchi",
    "pencil":"unchanged first P0-unit column, then original positive-integer power combination",
    "pencil_fibre_matrix_shape":[816,836],"required_pencil_rank":672,
    "pencil_common_Phi_cancelled_only_for_rank":True,
    "complete_fibre_count_per_pencil_matrix":3,"whole_fibre_dimension":272,
    "source_node_schedule":list(range(7)),
    "norm_source":"completed R885 full A272 and E2176, all272 original target coordinates",
    "norm_pencil":"one division-free Berkowitz over A[T], degrees0..8, full E[T] Cayley-Hamilton",
    "norm_Phi":"positive complete rank8 norm, no assumption Phi or pencil sections are units",
    "all_expression_denominators_required_units_on_entire_E":True,
    "norm_parameters":list(range(9)),
    "source_sigma_branch_order":SIGMA_BRANCHES,
    "reference":"R879 (1,v0), old R885 nine values reused",
    "two_chart_ideal":"same nine exact global functions on both original charts; Jj*inverse(J0)",
    "inverse_ideal":"colon {x:x*J0 subset R}, not a sum of generator reciprocals",
    "frozen_Hecke_direction":"Nm_target(source_pullback I), via original canonical dual7",
    "endpoint_P0_P1_det_fibre_expressions_retained":True,
    "endpoint_numeric_calibration_not_in_this_scope":True,
    "old_flips_Krylov_target_coordinates_reference_norms_or_jets_recomputed":False,
    "Q_fixed_basis_or_modular_inactive_claimed":False,
    "budget_trial_prefix_direction_prefix_excluded_from_identity":True}

class BudgetStop(RuntimeError):
    pass
class ScopeStop(RuntimeError):
    pass

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(4*1024*1024),b""):
            h.update(block)
    return h.hexdigest()
def read(path):
    path=Path(path)
    with (gzip.open if path.suffix==".gz" else open)(path,"rt",encoding="utf-8") as f:
        return json.load(f)
def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".tmp")
    data=(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n").encode()
    if path.suffix==".gz":
        with tmp.open("wb") as f:
            with gzip.GzipFile(filename="",fileobj=f,mode="wb",mtime=0,compresslevel=2) as z:
                z.write(data)
    else:
        tmp.write_bytes(data)
    tmp.replace(path)
def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def plain(value):
    out={k:value[k] for k in ("file","bytes","sha256")}
    name=PurePosixPath(out["file"])
    assert len(name.parts)==1 and name.name not in ("",".","..") and "\\" not in out["file"]
    assert isinstance(out["bytes"],int) and out["bytes"]>=0
    assert re.fullmatch("[0-9a-f]{64}",out["sha256"])
    return out
def spec(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}
def group_ref(group,row):
    return {**plain(row),"source_group":group}
def identity(item):
    out={k:item[k] for k in BASE}
    out["configuration_sha256"]=item["configuration_sha256"]
    out["selected_files_sha256"]=fingerprint(item["files"])
    if item.get("certificate") is not None:
        out["certificate"]=plain(item["certificate"])
    else:
        out["configuration_stage"]=plain(item["configuration_stage"])
    return out
def same_source(a,b):
    assert all(str(a[k])==str(b[k]) for k in BASE)
    assert a["configuration_sha256"]==b["configuration_sha256"]
def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],
        "helper_sha256":item["helper_sha256"],"original_Artin_helper_sha256":ARTIN_SHA,
        "python_flint":"0.9.0","p":41,"method_sha256":item["method_sha256"],"proofs":item["proofs"],
        "sources":{g:identity(v) for g,v in sorted(item["sources"].items())},
        "inputs":item["inputs"],"strategy":STRATEGY}
def positions(weight):
    return [(i,k) for i,e in enumerate(EPS) for k in range(weight-e+1)]
def shape(raw,m,n):
    assert len(raw)==m and all(len(r)==n for r in raw)
def vector(raw,n):
    assert isinstance(raw,list) and len(raw)==n
    assert all(isinstance(x,int) and 0<=x<P for x in raw)
    return raw
def mat(raw):
    return nmod_mat(raw,P)
def rows(a):
    return [[int(a[i,j]) for j in range(a.ncols())] for i in range(a.nrows())]
def sub(a,I,J):
    return mat([[int(a[i,j]) for j in J] for i in I])
def eye(n):
    return mat([[int(i==j) for j in range(n)] for i in range(n)])
def pivots(a,rank):
    answer=[]
    for i in range(rank):
        j=next(j for j in range(a.ncols()) if int(a[i,j]))
        assert int(a[i,j])==1
        answer.append(j)
    assert len(set(answer))==rank
    return answer

class Source:
    def __init__(self,label,item,root):
        self.label=label;self.item=item;self.directory=Path(root)/label;self.checked=set()
        self.files={k:plain(v) for k,v in item["files"].items()}
        assert all(k==v["file"] for k,v in self.files.items())
        m=self.directory/"full-outputs-manifest.json"
        assert sha(m)==item["manifest_sha256"]
        manifest=read(m)
        assert manifest["result"]==item["result"]
        entries={r["file"]:plain(r) for r in manifest["files"]}
        assert len(entries)==len(manifest["files"])
        entries[m.name]=spec(m)
        assert all(entries[k]==v for k,v in self.files.items())
        self.initial=self.get("public-actions-input.json")
        run=self.get("run-receipt.json");core=self.get("core-receipt.json")
        assert self.initial["source_commit"]==run["source_commit"]==item["source_commit"]
        assert str(run["workflow_run_id"])==str(item["run_id"])
        source_sha=self.initial.get("core_sha256",self.initial.get("job",{}).get("core_sha256"))
        assert source_sha==core["source_sha256"]==item["core_sha256"]
        if run.get("core_receipt_sha256") is not None:
            assert run["core_receipt_sha256"]==self.files["core-receipt.json"]["sha256"]
        if item.get("certificate") is None:
            assert label=="R827" and run["complete"] is False and core["complete"] is False
            assert run["process_exit_code"]==124
            anchor=self.get(item["configuration_stage"]["file"])
            assert anchor["complete"] is True
            self.tag=anchor["configuration"];self.certificate=None
        else:
            assert run["complete"] is True and run["process_exit_code"]==0 and core["complete"] is True
            self.certificate=self.get(item["certificate"]["file"])
            assert self.files[item["certificate"]["file"]]==plain(item["certificate"])
            assert self.certificate["complete"] is True and self.certificate["result"]==item["result"]
            assert core["certificate_sha256"]==item["certificate"]["sha256"]
            self.tag=self.certificate["configuration"]
        assert fingerprint(self.tag)==item["configuration_sha256"]
        assert self.tag.get("source_sha256",self.tag.get("core_sha256"))==item["core_sha256"]
    def get(self,name):
        row=self.files[name];path=self.directory/name
        if name not in self.checked:
            assert spec(path)==row,(self.label,name)
            self.checked.add(name)
        return read(path)
    def stage(self,row):
        row=plain(row);assert self.files[row["file"]]==row
        value=self.get(row["file"])
        assert value["complete"] is True and value["configuration"]==self.tag
        return value

class FunctionGraph:
    """Only original scalar functions; exact source definitions and modular arrays kept separate."""
    def __init__(self,job):
        self.J=job;self.nodes={};self.roots={};self.cache={}
        self.one=self.add({"operation":"constant_one"})
    def add(self,node):
        key=fingerprint(node)[:32]
        if key in self.nodes:
            assert self.nodes[key]==node
        else:
            self.nodes[key]=node
        return key
    def product(self,factors):
        return self.add({"operation":"multiply","factors":list(factors)})
    def power(self,base,n):
        assert isinstance(n,int)
        return self.add({"operation":"integer_power","base":base,"exponent":n})
    def divide(self,a,b):
        return self.product([a,self.power(b,-1)])
    def leaf(self,ref,field,weight):
        key=(ref["source_group"],ref["file"],field,weight)
        if key in self.cache:
            return self.cache[key]
        value=self.J.source(ref)
        v=vector(value[field],len(positions(weight)))
        if "original_column_mapping" in value:
            assert value["original_column_mapping"]==[list(x) for x in positions(weight)]
        name="function-leaf-"+fingerprint([ref,field,weight])[:24]
        old=self.J.old(name)
        if old is None:
            old=self.J.put(name,{"prime":P,"source_original_stage":ref,"source_field":field,
                "ordinary_weight":weight,"original_normal_positions":[list(x) for x in positions(weight)],
                "normal_coordinates_mod_prime":v,
                "exact_definition":"unchanged indicated original unit-solve section divided by its already included tau power",
                "additional_tau_power_or_integer_scale_applied":0,
                "modular_coordinates_not_claimed_reconstructed_characteristic_zero":True})
        assert old["source_original_stage"]==ref and old["source_field"]==field
        out=self.add({"operation":"original_normal_section",
            "source":self.J.ref(name),"original_source":ref,"source_field":field,"ordinary_weight":weight})
        self.cache[key]=out
        return out
    def local(self,ref,group):
        return self.J.locate(ref,group)
    def field_function(self,node,group):
        op=node["operation"]
        if op in ("one_for_original_neutral_H","one_for_original_initial_representative",
                  "one_for_same_original_Galois_representative","one_for_original_K_defined_representative",
                  "one_for_same_original_initial_representative"):
            return self.one
        if op=="q_u_over_tau_cubed":
            return self.leaf(self.local(node["source"],group),"normal_V3_coordinates_mod_prime",3)
        if op=="external_original_exact_principal_function_DAG":
            ref=self.local(node["source"],group);value=self.J.source(ref)
            field=node.get("field","exact_F_function_DAG")
            assert field=="exact_F_function_DAG"
            return self.field_function(value[field],ref["source_group"])
        if op=="inverse_of_product":
            return self.power(self.product([self.field_function(x,group) for x in node["factors"]]),-1)
        if op=="multiply":
            factors=node.get("factors")
            if factors is None:
                factors=[node["left"],node["right"]]
            return self.product([self.field_function(x,group) for x in factors])
        if op=="integer_power":
            return self.power(self.field_function(node["base"],group),int(node["exponent"]))
        if op=="product_of_all_seven_strict_original_constant_field_conjugates":
            assert len(node["factors"])==7
            assert node["original_sigma_branch_order"]==SIGMA_BRANCHES
            return self.product([self.field_function(x,group) for x in node["factors"]])
        if op=="completed_original_marked_Q_root":
            return self.Qj(self.local(node["source"],group),int(node["sigma_power"]))
        if op=="completed_original_K_defined_QK":
            return self.QK(self.local(node["source"],group))
        raise AssertionError(("unrecognized_original_function_operation",op))
    def Qj(self,ref,sigma_power):
        key=("Qj",ref["sha256"])
        if key in self.cache:
            return self.cache[key]
        v=self.J.source(ref);j=int(v["j"]);n=POWERS[j-1]
        assert v["ordinary_power"]==n and v["Q_root"]=="Q"
        assert v["original_fixed_chi_sign_is_negative_power_in_Q"] is True
        if sigma_power:
            assert v["sigma_power"]==sigma_power and v["original_branch"]==SIGMA_BRANCHES[sigma_power]
            assert v["strict_original_selection_and_integer_anchors_preserved"] is True
            bref=v["source_actual_marked_pair"]
        else:
            assert ref["source_group"]=="R896"
            bref=v["source_marked_original_pair"]
        b=self.leaf(self.local(bref,ref["source_group"]),"B_coordinates_mod_prime",n)
        vv=self.leaf(self.local(v["source_exact_v"],ref["source_group"]),"normal_V3_coordinates_mod_prime",3)
        assert plain(v["source_original_chi_anchor"])==plain(self.J.inputs["qchi_anchor"])
        q=self.product([self.divide(b,vv),self.power(self.qchi,-(n-2))])
        self.cache[key]=q
        return q
    def zero_a(self):
        inputs=self.J.inputs["QN_inputs"]
        ref=self.J.inputs.get("existing_a0_normal_polynomial")
        if ref is not None:
            old=self.J.source(ref)
            assert old["all_five_old272_values_multiplied_back"] is True
            assert old["all_original_weighted_degree_bounds_verified"] is True
            assert [plain(x) for x in old["source_five_original_a_fibre_values"]]==[
                plain(x) for x in inputs["original_zero_a_old_fibres"]]
            return self.leaf(ref,"normal_V3_coordinates_mod_prime",3)
        name="a0-normal-polynomial-from-original-five-complete-fibres"
        old=self.J.old(name)
        if old is None:
            self.J.budget();values=[]
            refs=inputs["original_zero_a_old_fibres"]
            assert len(refs)==5
            for z,r in enumerate(refs):
                a=self.J.source(r)
                assert a["prime"]==P and a["z0"]==z and a["which"]=="a" and a["a_exact_D_basis_column"]==0
                values.append(vector(a["section_evaluation_mod_prime"],272))
            V=mat([[pow(z,k,P) for k in range(4)] for z in range(4)])
            inv=V.inv();assert V*inv==eye(4) and inv*V==eye(4)
            coefficients=inv*mat(values[:4])
            for i in range(272):
                for k in range(4-EPS[i],4):
                    assert int(coefficients[k,i])==0
            for z in range(5):
                assert rows(mat([[pow(z,k,P) for k in range(4)]])*coefficients)[0]==values[z]
            old=self.J.put(name,{"prime":P,"source_five_original_a_fibre_values":refs,
                "source_original_a_selection":inputs["original_zero_a_selection"],
                "normal_polynomial_coefficients_mod_prime":rows(coefficients),
                "normal_V3_coordinates_mod_prime":[int(coefficients[k,i]) for i,k in positions(3)],
                "both_four_by_four_inverse_products_verified":True,
                "all_five_old272_values_multiplied_back":True,"all_original_weighted_degree_bounds_verified":True,
                "exact_definition":"unique same original normal V3 function determined by four old whole fibres",
                "old_a_fibre_multiplication_or_full_basis_conversion_recomputed":False})
        return self.leaf(self.J.ref(name),"normal_V3_coordinates_mod_prime",3)
    def QN(self):
        if "QN" in self.roots:
            return self.roots["QN"]
        I=self.J.inputs["QN_inputs"];marked=self.J.source(I["marked_QN"])
        assert marked["actual_rho_order"]==-8435
        assert marked["Q_orbit_fixed_by_original_Gal_L_over_K"] is True
        assert marked["original_fractional_ideal_principal_factor_direction"]=="positive multiplication by Q_N"
        qC=self.leaf(I["original_u_C"],"u_C_normal_V2_coordinates_mod_prime",2)
        common=self.product([qC,self.power(self.qchi,-4)])
        a=[self.zero_a()]
        v=[self.leaf(I["original_zero_v"],"normal_V3_coordinates_mod_prime",3)]
        principals=[I["original_zero_Qtilde"]]
        assert len(I["six_original_branches"])==6
        for k,row in enumerate(I["six_original_branches"],1):
            principal=self.J.source(row["principal"])
            assert principal["sigma_power"]==k and principal["original_branch"]==SIGMA_BRANCHES[k]
            assert principal["exact_original_Galois_conjugate_not_a_new_linearly_equivalent_choice"] is True
            assert plain(principal["source_actual_a"])==plain(row["a"])
            assert plain(principal["source_actual_v"])==plain(row["v"])
            a.append(self.leaf(row["a"],"a_normal_V3_coordinates_mod_prime",3))
            v.append(self.leaf(row["v"],"normal_V3_coordinates_mod_prime",3))
            principals.append(row["principal"])
        assert [plain(x["source"]) for x in marked["source_all_seven_original_principals"]]==[plain(x) for x in principals]
        orbit=self.product([self.product([self.power(self.divide(x,y),3),common]) for x,y in zip(a,v)])
        values={k:self.one for k in ("H","Cstar","X","D0","D1","D2","D3","D4","D5","D6")}
        records=[]
        for row,label,parents in zip(I["two_original_chi_flips"],("X2","X4"),(("X","X"),("X2","X2"))):
            records.append((label,*parents,row))
        assert len(records)==2 and len(I["new_trace_flips"])==16
        for row in I["new_trace_flips"]:
            p=self.J.source(row["principal"])
            records.append((p["new_space_label"],p["left_space_label"],p["right_space_label"],row))
        assert [plain(x["complete"]) for x in I["new_trace_flips"]]==[plain(x) for x in marked["source_all_new_complete_flips"]]
        for label,left,right,row in records:
            p=self.J.source(row["principal"]);u=self.J.source(row["u"])
            assert plain(p["source_original_unscaled_u"])==plain(row["u"])
            assert p["all_selected_original_scalars_retained"] is True
            assert p["exact_F_function_DAG"]["operation"]=="inverse_of_product"
            assert u["original_scalar_not_rescaled"] is True and u["q_P0_value_is_unit"] is True
            q=self.leaf(row["u"],"normal_V3_coordinates_mod_prime",3)
            values[label]=self.power(self.product([q,values[left],values[right]]),-1)
        self.roots["QN"]=self.product([orbit,values["DN"]])
        return self.roots["QN"]
    def QK(self,ref):
        key=("QK",ref["sha256"])
        if key in self.cache:
            return self.cache[key]
        value=self.J.source(ref)
        assert value["QK_root"]=="QK" and value["QK_defined_over_original_K"] is True
        assert value["original_unscaled_sections_and_tau_frames_preserved"] is True
        assert plain(value["source_original_QN"])==plain(self.J.inputs["QN_inputs"]["marked_QN"])
        w=self.leaf(self.local(value["source_unscaled_S0"],ref["source_group"]),"normal_V3_coordinates_mod_prime",3)
        v=self.leaf(self.local(value["source_unscaled_exact_v"],ref["source_group"]),"normal_V3_coordinates_mod_prime",3)
        self.cache[key]=self.product([self.QN(),self.divide(w,v)])
        return self.cache[key]
    def compile(self):
        self.qchi=self.leaf(self.J.inputs["qchi_anchor"],"V2_coordinates_mod_prime",2)
        self.QN()
        for j in range(1,6):
            record=self.J.inputs["directions"][str(j)]
            frame=self.J.source(record["frame"]);qref=record["QZ"];qz=self.J.source(qref)
            assert plain(frame["source_original_marked_QZ"])==plain(qref)
            assert plain(frame["source_original_qchi"])==plain(self.J.inputs["qchi_anchor"])
            assert qz["actual_QZ_rho_order"]==RHO_ORDERS[j-1]
            assert qz["negative_support_not_assumed_to_be_only_P0"] is True
            assert qz["original_degree_zero_coefficients"]=={"p":PNUM[j-1],"q":QDEN[j-1]}
            QZ=self.field_function(qz["exact_QZ_function_DAG"],qref["source_group"])
            self.roots["Phi"+str(j)]=self.divide(QZ,self.qchi)
        return self.J.put("compiled-original-marked-function-program",{
            "prime":P,"nodes":self.nodes,"roots":self.roots,
            "source_R899_QN_leaf_inventory":self.J.inputs["QN_provenance"],
            "source_R901_R903_original_principals":{str(j):self.J.inputs["directions"][str(j)] for j in range(1,6)},
            "original_global_functions_and_unscaled_leaf_identity_preserved":True,
            "additional_tau_power_applied_to_normal_arrays":0,
            "all_constant_field_conjugates_are_real_source_leaves_not_reordered_constants":True,
            "no_new_old_flip_or_RR_kernel_computed":True})

class Job:
    def __init__(self,args):
        self.args=args;self.started=time.monotonic();self.out=Path(args.output);self.out.mkdir(parents=True,exist_ok=True)
        self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41 and self.item["producer_inputs_pending"] is False
        assert sha(__file__)==self.item["core_sha256"] and flint.__version__=="0.9.0"
        assert sha(algebra.__file__)==ARTIN_SHA==self.item["original_Artin_helper_sha256"]
        assert sha(pencil_algebra.__file__)==self.item["helper_sha256"]
        topic=Path(__file__).resolve().parent.parent
        assert sha(topic/self.item["method"])==self.item["method_sha256"]
        for row in self.item["proofs"].values():
            assert sha(topic/row["path"])==row["sha256"]
        self.tag=expected_tag(self.item);self.refs={};self.current=None;self.phase="source-initialization";self.done={}
        self.sources={g:Source(g,s,args.retained) for g,s in self.item["sources"].items()}
        self.inputs=self.item["inputs"];self.directions=list(self.item.get("requested_directions",[1]))
        assert self.directions and sorted(set(self.directions))==self.directions and all(1<=j<=5 for j in self.directions)
        self.V2=positions(2);self.V3=positions(3)
        assert len(self.V2)==418 and len(self.V3)==690
        self.A={};self.E3={};self.CE3={};self.points={};self.bases={};self.graph=None;self.artins={}
        self.fibre_products={};self.pencils={};self.evaluation_cache={}
    def budget(self):
        if time.monotonic()-self.started>=self.args.budget_minutes*60-30:
            raise BudgetStop("R907 atomic stages retained; phase="+self.phase)
        if shutil.disk_usage(self.out).free<int(self.item.get("minimum_free_disk_bytes",536870912)):
            raise BudgetStop("R907 disk floor; no active mathematical stage removed")
    def path(self,name):
        assert Path(name).name==name
        return self.out/(PREFIX+name+".json.gz")
    def ref(self,name):
        return group_ref("R907",self.refs[name])
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
        value={"result":RESULT,"configuration":self.tag,"complete":True,**value}
        path=self.path(name)
        if path.exists():
            assert read(path)==value
        else:
            save(path,value)
        self.refs[name]=spec(path)
        print("R907_STAGE="+json.dumps({"file":path.name,"seconds":time.monotonic()-self.started}),flush=True)
        return value
    def source(self,row):
        if row["source_group"]=="R907":
            path=self.out/plain(row)["file"]
            assert spec(path)==plain(row)
            obj=read(path);assert obj["complete"] is True and obj["configuration"]==self.tag
            return obj
        return self.sources[row["source_group"]].stage(row)
    def locate(self,row,default):
        if row.get("source_group") is not None:
            return row
        name=plain(row)["file"]
        if default in self.sources and self.sources[default].files.get(name)==plain(row):
            return group_ref(default,row)
        matches=[g for g,s in self.sources.items() if s.files.get(name)==plain(row)]
        assert len(matches)==1,("ambiguous_original_reference",name,matches)
        return group_ref(matches[0],row)
    def checkpoint(self,phase):
        self.phase=phase
        save(self.path("current"),{"result":RESULT,"configuration":self.tag,"complete":False,"phase":phase,
            "complete_direction_certificates":self.done,"retained_complete_stages":self.refs})
        self.current=spec(self.path("current"))
    def prepare(self):
        r903=self.sources["R903"];cert=r903.certificate
        assert cert["actual_all_five_original_Iz_128_spaces_certified"] is True
        assert cert["actual_all_five_complete_two_chart272_lattices_certified"] is True
        r901=self.sources["R901"]
        same_source(r903.tag["sources"]["R901"],r901.item)
        r899=self.sources["R899"];audit=self.source(self.inputs["R899_source_audit"])
        assert audit["inputs"]==self.inputs["QN_inputs"]
        assert audit["same_original_Galois_orbit_and_all_unscaled_leaves_bound"] is True
        for group,old in r899.tag["sources"].items():
            same_source(old,self.item["sources"][group])
        qn_provenance=self.inputs["QN_provenance"]
        assert qn_provenance["source_R899_identity"]=={k:r899.item[k] for k in BASE}
        assert qn_provenance["input_inventory_sha256"]==self.inputs["R899_original_inventory"]["sha256"]
        qchi=self.source(self.inputs["qchi_anchor"])
        assert qchi["role"]=="u" and qchi["order272_is_exact"] is True
        frame=self.source(self.inputs["t_frame"])
        assert frame["original_t_first_order_unit_certified"] is True
        assert int(frame["original_t_over_rho_constant_mod_prime"])==354813668
        self.frame=frame
        lookup={x:i for i,x in enumerate(self.V3)};self.v2columns=[lookup[x] for x in self.V2]
        for z in range(7):
            ref=self.inputs["normal_V3_fibres"][str(z)];fibre=self.source(ref)
            kref=self.inputs["Krylov_points"][str(z)];point=self.source(kref)
            cref=self.inputs["characteristic_nodes"][str(z)];char=self.source(cref)
            assert fibre["z0"]==point["z0"]==char["z_value"]==z
            assert fibre["prime"]==point["prime"]==char["prime"]==P
            assert point["usable"] is True and point["both_inverse_products_verified"] is True
            assert point["actual_cyclic_rank"]==272 and char["monic"] is True
            assert plain(fibre["source_original_Krylov_point"])==plain(kref)
            assert plain(char["source_original_Krylov"])==plain(kref)
            assert char["completed_original_Krylov_inverse_recomputed"] is False
            shape(fibre["normal_evaluation_mod_prime"],272,690)
            shape(fibre["cyclic_evaluation_mod_prime"],272,690)
            self.E3[z]=mat(fibre["normal_evaluation_mod_prime"])
            self.CE3[z]=mat(fibre["cyclic_evaluation_mod_prime"])
            self.points[z]=point
            self.A[z]=algebra.SourceAlgebra(char["characteristic_coefficients_ascending_T"],P)
        for j in self.directions:
            record=self.inputs["directions"][str(j)]
            assert plain(record["complete"])==plain(cert["complete_direction_certificates"][str(j)])
            complete=self.source(record["complete"]);basis=self.source(record["basis"]);marked=self.source(record["frame"])
            assert complete["actual_original_Iz_128_RR_space_certified"] is True
            assert plain(complete["complete_original_normal128"])==plain(record["basis"])
            assert plain(complete["marked_original_P0_frame_and_embedding"])==plain(record["frame"])
            assert basis["normal_basis_positions"]==[list(x) for x in self.V3]
            assert basis["exact_complete_RR_dimension"]==128
            assert basis["all_eighteen_jet_rows_times_complete_basis_zero"] is True
            assert basis["original_global_multiplier_not_yet_applied_to_normal_arrays"] is True
            shape(basis["normal_basis_mod_prime"],690,128)
            assert marked["positive_multiplication_is_an_isomorphism_at_every_curve_DVR"] is True
            assert marked["selected_column_not_rescaled"] is True
            assert marked["actual_target_t_order"]==RHO_ORDERS[j-1]-254
            assert plain(marked["source_original_marked_QZ"])==plain(record["QZ"])
            assert plain(record["QZ"])==plain(r901.certificate["original_direction_marked_principal_and_descent"][str(j)])
            self.bases[j]=(mat(basis["normal_basis_mod_prime"]),basis,marked)
        artin=self.sources["ARTIN"]
        assert artin.certificate["actual_whole_Artin_target_normal_coordinates_certified"] is True
        assert artin.certificate["actual_nine_reference_norm_values_computed"] is True
        reference=self.source(self.inputs["reference_function"])
        assert reference["actual_reference_basepoint_free_pencil_certified"] is True
        self.reference=reference
        self.corr_DAG=self.source(self.inputs["correspondence_DAG"])
        assert "rigidified_Hecke_transport" in self.corr_DAG and "correspondence_function_field" in self.corr_DAG
        self.put("original-source-audit",{"prime":P,
            "source_identities":{g:identity(s.item) for g,s in self.sources.items()},"inputs":self.inputs,
            "three_complete_fibres_and_all_factors_required":True,
            "same_original_R903_membership_and_positive_Phi_bound":True,
            "R899_full_QN_function_leaf_sources_not_replaced_by_R901_metadata_only":True,
            "R885_completed_target_not_assumed_to_be_P0_or_P1":True,
            "old_target_embedding_reference_norms_flips_or_jets_recomputed":False})
        self.graph=FunctionGraph(self);self.graph.compile()
        self.checkpoint("actual-original-sources-and-function-program-bound")

    def pencil_section(self,j,trial):
        """The first column keeps the original scalar; the second uses exact integer powers."""
        name=f"j{j}-pencil-"+("fixed-a" if trial==0 else f"trial-{trial:04d}-b")
        value=self.old(name)
        if value is None:
            self.budget();B,basis,frame=self.bases[j]
            if trial==0:
                column=int(frame["original_P0_selected_column"])
                coefficients=[int(i==column) for i in range(128)]
                exact={"operation":"unchanged_original_R903_column","column":column}
            else:
                coefficients=[pow(trial,i,P) for i in range(128)]
                exact={"operation":"sum_actual_integer_powers_times_original_columns",
                       "integer_parameter":trial,"power_range":[0,127]}
            v=B*mat([[x] for x in coefficients])
            value=self.put(name,{"prime":P,"original_direction":j,
                "source_complete_normal128":self.inputs["directions"][str(j)]["basis"],
                "source_original_P0_frame":self.inputs["directions"][str(j)]["frame"],
                "integer_parameter":trial if trial else None,
                "coefficients_in_original_basis_mod_prime":coefficients,
                "normal_V3_coordinates_mod_prime":[int(v[i,0]) for i in range(690)],
                "exact_original_section_definition":exact,
                "original_scalar_not_rescaled":True,
                "same_positive_Phi_needed_to_obtain_actual_M_section":True})
        assert value["source_complete_normal128"]==self.inputs["directions"][str(j)]["basis"]
        return value,self.ref(name)

    def product_fibre(self,j,trial,z,section,sref):
        stem="fixed-a" if trial==0 else f"trial-{trial:04d}-b"
        name=f"j{j}-{stem}-times-V2-fibre-{z}"
        value=self.old(name)
        if value is None:
            self.budget()
            coordinates=mat([[x] for x in section["normal_V3_coordinates_mod_prime"]])
            evaluated=self.CE3[z]*coordinates
            A=self.A[z];a=A.unpack([int(evaluated[i,0]) for i in range(272)])
            products=[]
            for k in self.v2columns:
                b=A.unpack([int(self.CE3[z][i,k]) for i in range(272)])
                products.append(A.pack(A.mul(a,b)))
            value=self.put(name,{"prime":P,"original_direction":j,"source_node_value":z,
                "source_original_section":sref,
                "source_completed_normal_V3_fibre":self.inputs["normal_V3_fibres"][str(z)],
                "source_completed_Krylov_point":self.inputs["Krylov_points"][str(z)],
                "source_completed_characteristic_node":self.inputs["characteristic_nodes"][str(z)],
                "V2_original_positions":[list(x) for x in self.V2],
                "V2_columns_in_original_V3":self.v2columns,
                "section_cyclic_value_mod_prime":A.pack(a),
                "cyclic_product_matrix_mod_prime":[list(x) for x in zip(*products)],
                "whole_fibre_dimension":272,"product_column_count":418,
                "all_source_factors_and_nilpotents_preserved":True,
                "old_Krylov_V3_evaluation_or_Φ_evaluation_recomputed":False,
                "Phi_cancelled_only_for_the_rank_of_the_same_global_multiplication_map":True})
        assert value["source_original_section"]==sref
        shape(value["cyclic_product_matrix_mod_prime"],272,418)
        return value,self.ref(name)

    def pencil(self,j):
        complete_name=f"j{j}-complete-basepoint-free-pencil"
        old=self.old(complete_name)
        if old is not None:
            assert old["actual_pencil_rank"]==672 and old["actual_original_basepoint_free_pencil_certified"] is True
            self.pencils[j]=old
            return old,self.ref(complete_name)
        a,aref=self.pencil_section(j,0)
        triples=list(itertools.combinations(range(7),3))
        maximum=int(self.item.get("maximum_pencil_trials",4))
        triple_limit=int(self.item.get("maximum_fibre_triples",35))
        assert 1<=maximum and 1<=triple_limit<=len(triples)
        for trial in range(1,maximum+1):
            b,bref=self.pencil_section(j,trial)
            for ordinal,nodes in enumerate(triples[:triple_limit]):
                stem=f"j{j}-trial-{trial:04d}-triple-{ordinal:02d}"
                name=stem+"-rank-certificate";rank_cert=self.old(name)
                if rank_cert is None:
                    factors=[];raw=[]
                    for z in nodes:
                        left,lref=self.product_fibre(j,0,z,a,aref)
                        right,rref=self.product_fibre(j,trial,z,b,bref)
                        factors.append({"node":z,"left":lref,"right":rref})
                        raw.extend([x+y for x,y in zip(left["cyclic_product_matrix_mod_prime"],
                                                       right["cyclic_product_matrix_mod_prime"])])
                    self.budget();shape(raw,816,836);M=mat(raw)
                    echelon,rank=M.rref();assert rank<=672,("original_pencil_rank_upper_bound",j,trial,rank)
                    selected_columns=pivots(echelon,rank)
                    payload={"prime":P,"original_direction":j,"integer_parameter":trial,
                        "source_original_a":aref,"source_original_b":bref,
                        "source_complete_three_fibre_products":factors,
                        "matrix_shape":[816,836],"actual_rank":rank,
                        "whole_source_nodes":list(nodes),"selected_original_columns":selected_columns,
                        "original_rank_upper_bound":672,
                        "full_matrix_row_order":"three original nodes then all272 cyclic coefficients",
                        "full_matrix_column_order":"a times original V2, then b times original V2",
                        "geometric_point_selection_or_factor_deletion_used":False}
                    if rank==672:
                        independent=sub(M,range(816),selected_columns)
                        transposed,r2=independent.transpose().rref();assert r2==672
                        selected_rows=pivots(transposed,672)
                        minor=sub(independent,selected_rows,range(672))
                        inverse=minor.inv();assert minor*inverse==eye(672) and inverse*minor==eye(672)
                        payload.update({"selected_original_rows":selected_rows,
                            "selected_minor_mod_prime":rows(minor),"selected_minor_inverse_mod_prime":rows(inverse),
                            "actual_unit_minor_determinant_mod_prime":int(minor.det()),
                            "both_unit_inverse_products_verified":True,
                            "same_original_char0_rank_forced_by_672_lower_and_upper_bounds":True,
                            "original_common_zero_divisor_degree":0})
                    rank_cert=self.put(name,payload)
                    del M,echelon;gc.collect()
                if rank_cert["actual_rank"]==672:
                    assert rank_cert["both_unit_inverse_products_verified"] is True
                    value=self.put(complete_name,{"prime":P,"original_direction":j,
                        "source_complete_normal128":self.inputs["directions"][str(j)]["basis"],
                        "source_original_marked_embedding":self.inputs["directions"][str(j)]["frame"],
                        "source_original_a":aref,"source_original_b":bref,
                        "source_actual672_rank_certificate":self.ref(name),
                        "actual_pencil_rank":672,"actual_original_basepoint_free_pencil_certified":True,
                        "exact_original_pencil":{
                            "first":{"operation":"positive_multiply","multiplier_graph_root":self.graph.roots["Phi"+str(j)],"normal_section":aref},
                            "second":{"operation":"positive_multiply","multiplier_graph_root":self.graph.roots["Phi"+str(j)],"normal_section":bref},
                            "source_complete_function_program":self.ref("compiled-original-marked-function-program")},
                        "first_P0_scalar_not_rescaled":True,
                        "char0_complete_pencil_certified_not_coefficients_reconstructed":True,
                        "source_fibres_not_assumed_to_avoid_all_Z_support":True,
                        "P1_unit_or_numeric_frame_not_claimed":True})
                    self.pencils[j]=value;self.checkpoint(complete_name)
                    return value,self.ref(complete_name)
            self.checkpoint(f"j{j}-completed-pencil-trial-{trial:04d}")
        raise ScopeStop(f"direction {j}: finite pencil trial/triple prefix exhausted; no negative Picard conclusion")

    def artin_context(self,record):
        ordinal=int(record["ordinal"])
        if ordinal in self.artins:
            assert self.artins[ordinal]["record"]==record
            return self.artins[ordinal]
        complete=self.source(record["complete"])
        assert complete["source_node_ordinal"]==ordinal and complete["whole_fibre_success"] is True
        assert complete["source_dimension"]==272 and complete["correspondence_scalar_dimension"]==2176
        for key in ("source_functions","correspondence_algebra","target_normal_row","full_target_equations",
                    "original_reference_value","nine_reference_norms"):
            assert plain(complete[key])==plain(record[key])
        src=self.source(record["source_functions"]);corr=self.source(record["correspondence_algebra"])
        index=self.source(record["target_normal_row"]);eq=self.source(record["full_target_equations"])
        reference=self.source(record["original_reference_value"]);norms=self.source(record["nine_reference_norms"])
        z=complete["source_node_value"];assert src["source_node_value"]==z
        assert corr["full_Pprime_times_target_w_equals_K_verified"] is True
        assert corr["any_source_factor_or_multiplicity_discarded"] is False
        assert eq["all272_original_target_equations_verified"] is True
        assert eq["all2176_scalar_coordinates_of_each_equation_checked"] is True
        assert eq["normalized_row_is_original_R876_unique271_solution"] is True
        assert plain(eq["source_target_normal_row"])==plain(record["target_normal_row"])
        assert plain(corr["source_functions"])==plain(record["source_functions"])
        A=algebra.SourceAlgebra(src["complete_source_algebra_modulus"],P)
        E=algebra.CorrespondenceAlgebra(A,[A.unpack(x) for x in corr["monic_correspondence_coefficients"]])
        gamma=[];blocks=[]
        assert len(index["blocks"])==17 and len(record["target_normal_blocks"])==17
        for entry,ref in zip(index["blocks"],record["target_normal_blocks"]):
            assert plain(entry["source"])==plain(ref)
            value=self.source(ref);first,stop=entry["normal_columns"]
            assert value["normal_columns"]==[first,stop] and first==len(gamma)
            assert len(value["normal_values_over_E"])==stop-first
            gamma.extend(E.unpack(x) for x in value["normal_values_over_E"]);blocks.append(ref)
        assert len(gamma)==272 and gamma[0]==E.one
        assert reference["full_original_target_reference_quotient_verified"] is True
        assert norms["parameters"]==list(range(9))
        assert norms["parameter_zero_norm_equals_one"] is True
        assert norms["frozen_Hecke_direction_recovered_by_original_dual7"] is True
        assert plain(norms["source_target_reference_value"])==plain(record["original_reference_value"])
        assert plain(reference["source_original_reference_function"])==plain(self.inputs["reference_function"])
        shape(norms["nine_norm_values_over_entire_A"],9,272)
        self.artins[ordinal]={"record":record,"A":A,"E":E,"gamma":gamma,
            "flat_gamma":mat([E.flat(x) for x in gamma]).transpose(),
            "z0":z,"old_reference":reference,"old_norms":norms}
        name=f"Artin-{ordinal:02d}-original-completed-target-bound"
        if self.old(name) is None:
            self.put(name,{"prime":P,"original_ordinal":ordinal,"source_node_value":z,
                "source_completed_R885_fibre":record["complete"],
                "source_original_target_blocks":blocks,"source_correspondence_algebra":record["correspondence_algebra"],
                "source_full272_equations":record["full_target_equations"],
                "source_old_nine_reference_norms":record["nine_reference_norms"],
                "entire_source_dimension":272,"entire_correspondence_dimension":2176,
                "all_factors_and_nilpotents_retained":True,
                "old_target_adjugate_normalization_reference_norm_or_charpoly_recomputed":False,
                "this_fibre_identified_with_P0_or_P1":False})
        return self.artins[ordinal]

    def evaluate_section(self,context,coordinates,weight):
        self.budget();E=context["E"]
        vector(coordinates,len(positions(weight)))
        coefficients=[[0]*272 for _ in range(weight+1)]
        for x,(i,k) in zip(coordinates,positions(weight)):
            coefficients[k][i]=x
        packed=context["flat_gamma"]*mat(coefficients).transpose()
        value=E.zero
        for k in range(weight,-1,-1):
            value=E.add(E.mul_U(value),E.from_flat([int(packed[i,k]) for i in range(2176)]))
        return value

    def graph_value(self,context,key):
        ordinal=context["record"]["ordinal"];cache=(ordinal,key)
        if cache in self.evaluation_cache:
            return self.evaluation_cache[cache]
        node=self.graph.nodes[key];name=f"Artin-{ordinal:02d}-function-node-{key}"
        E=context["E"];old=self.old(name)
        if old is not None:
            assert old["exact_function_node"]==node and old["source_graph_root_id"]==key
            value=E.unpack(old["value_over_complete_E"])
            self.evaluation_cache[cache]=value
            return value
        failed=self.old(name+"-unit-failure")
        if failed is not None:
            raise algebra.UnitFailure(failed["unit_failure_label"],failed["whole_algebra_failure_witness"])
        self.budget();op=node["operation"];deps=[]
        try:
            if op=="constant_one":
                value=E.one
            elif op=="original_normal_section":
                leaf=self.source(node["source"])
                value=self.evaluate_section(context,leaf["normal_coordinates_mod_prime"],int(node["ordinary_weight"]))
                deps.append(node["source"])
            elif op=="multiply":
                value=E.one
                for k in node["factors"]:
                    value=E.mul(value,self.graph_value(context,k))
                    deps.append(self.ref(f"Artin-{ordinal:02d}-function-node-{k}"))
            elif op=="integer_power":
                base=self.graph_value(context,node["base"]);power=int(node["exponent"])
                deps.append(self.ref(f"Artin-{ordinal:02d}-function-node-{node['base']}"))
                if power<0:
                    inverse_name=name+"-whole-unit-inverse"
                    inverse_stage=self.old(inverse_name)
                    if inverse_stage is None:
                        self.budget();inverse,witness=E.inverse(base,"original-function-node-"+key)
                        inverse_stage=self.put(inverse_name,{"prime":P,
                            "source_complete_Artin_fibre":context["record"]["complete"],
                            "source_base_value":deps[0],"original_negative_integer_exponent":power,
                            "whole_fibre_unit_certificate":witness,"inverse_over_complete_E":E.pack(inverse),
                            "all2176_inverse_product_coordinates_verified":True})
                    else:
                        assert inverse_stage["source_base_value"]==deps[0]
                        inverse=E.unpack(inverse_stage["inverse_over_complete_E"])
                    deps.append(self.ref(inverse_name));value=E.power(inverse,-power)
                else:
                    value=E.power(base,power)
            else:
                raise AssertionError(("unrecognized_compiled_operation",op))
        except algebra.UnitFailure as exc:
            self.put(name+"-unit-failure",{"prime":P,
                "source_complete_Artin_fibre":context["record"]["complete"],
                "exact_function_node":node,"source_graph_root_id":key,
                "unit_failure_label":exc.label,"whole_algebra_failure_witness":exc.witness,
                "entire_source_and_correspondence_algebras_retained":True,
                "original_global_function_or_Picard_class_not_refuted":True})
            raise
        self.put(name,{"prime":P,"source_complete_Artin_fibre":context["record"]["complete"],
            "source_complete_function_program":self.ref("compiled-original-marked-function-program"),
            "source_graph_root_id":key,"exact_function_node":node,
            "source_evaluated_dependencies":deps,"value_over_complete_E":E.pack(value),
            "whole_scalar_dimension":2176,"all_actual_expression_denominators_certified_on_entire_E":True,
            "additional_tau_power_or_integer_scale_applied":0})
        self.evaluation_cache[cache]=value
        return value

    def pencil_target(self,j,context,section_ref,which):
        ordinal=context["record"]["ordinal"];name=f"j{j}-Artin-{ordinal:02d}-target-{which}"
        old=self.old(name);E=context["E"]
        if old is None:
            section=self.source(section_ref)
            value=self.evaluate_section(context,section["normal_V3_coordinates_mod_prime"],3)
            old=self.put(name,{"prime":P,"original_direction":j,
                "source_complete_Artin_fibre":context["record"]["complete"],
                "source_original_unscaled_normal_section":section_ref,
                "target_normal_section_value_over_E":E.pack(value),
                "normal_function_has_original_tau_normalization_already":True,
                "positive_Phi_not_yet_applied":True})
        assert old["source_original_unscaled_normal_section"]==section_ref
        return E.unpack(old["target_normal_section_value_over_E"]),self.ref(name)

    def norm_on_fibre(self,j,record,pencil,pencil_ref):
        ordinal=record["ordinal"];stem=f"j{j}-Artin-{ordinal:02d}"
        completed=self.old(stem+"-complete-nine-norms")
        if completed is not None:
            assert completed["actual_nine_full_A_values_computed"] is True
            return completed,self.ref(stem+"-complete-nine-norms")
        failed=self.old(stem+"-whole-expression-unit-failure")
        if failed is not None:
            return None,self.ref(stem+"-whole-expression-unit-failure")
        context=self.artin_context(record);E=context["E"];A=E.A
        try:
            phi_key=self.graph.roots["Phi"+str(j)]
            Phi=self.graph_value(context,phi_key)
            phi_ref=self.ref(f"Artin-{ordinal:02d}-function-node-{phi_key}")
            a,aref=self.pencil_target(j,context,pencil["source_original_a"],"a")
            b,bref=self.pencil_target(j,context,pencil["source_original_b"],"b")
            name=stem+"-positive-Phi-norm";phi_norm=self.old(name)
            if phi_norm is None:
                self.budget();coefficients,proof=E.characteristic(Phi)
                phi_norm=self.put(name,{"prime":P,"source_Phi_value":phi_ref,
                    "source_complete_Artin_fibre":record["complete"],
                    "characteristic_certificate":proof,"norm_Phi_over_A":A.pack(coefficients[-1]),
                    "norm_Phi_not_required_to_be_a_unit":True,
                    "positive_multiplication_in_original_M_embedding":True})
            assert phi_norm["source_Phi_value"]==phi_ref
            phi_norm_ref=self.ref(name);factor=A.unpack(phi_norm["norm_Phi_over_A"])
            name=stem+"-normal-pencil-norm-polynomial";poly=self.old(name)
            if poly is None:
                def load_level(size):
                    value=self.old(stem+f"-Berkowitz-size-{size:02d}")
                    if value is not None:
                        assert value["source_original_target_a"]==aref and value["source_original_target_b"]==bref
                    return value
                def save_level(size,payload):
                    self.put(stem+f"-Berkowitz-size-{size:02d}",{
                        "prime":P,"source_original_target_a":aref,"source_original_target_b":bref,
                        "source_complete_Artin_fibre":record["complete"],**payload})
                    self.checkpoint(stem+f"-Berkowitz-size-{size:02d}")
                coefficients,proof=pencil_algebra.pencil_characteristic(E,a,b,self.budget,load_level,save_level)
                poly=self.put(name,{"prime":P,"source_original_target_a":aref,"source_original_target_b":bref,
                    "source_complete_Artin_fibre":record["complete"],
                    "source_completed_Berkowitz_levels":[self.ref(stem+f"-Berkowitz-size-{s:02d}") for s in range(1,9)],
                    **proof})
            assert poly["source_original_target_a"]==aref and poly["source_original_target_b"]==bref
            assert poly["complete_E_T_Cayley_Hamilton_verified"] is True
            polyref=self.ref(name)
            name=stem+"-nine-positive-original-M-section-norms";values=self.old(name)
            if values is None:
                self.budget()
                normal=[A.unpack(x) for x in poly["norm_polynomial_over_A"]]
                scaled,nine=pencil_algebra.scale_norm_polynomial(A,normal,factor)
                values=self.put(name,{"prime":P,"original_direction":j,
                    "source_complete_basepoint_free_pencil":pencil_ref,
                    "source_complete_Artin_fibre":record["complete"],
                    "source_positive_Phi_norm":phi_norm_ref,"source_normal_pencil_polynomial":polyref,
                    "source_old_nine_reference_norms":record["nine_reference_norms"],
                    "norm_polynomial_over_entire_A":[A.pack(x) for x in scaled],
                    "parameters":list(range(9)),"nine_norm_values_over_entire_A":[A.pack(x) for x in nine],
                    "original_Mj_positive_Phi_factor_included":True,
                    "reference_nine_values_recomputed":False,"whole_A_dimension":272,
                    "source_factors_or_nilpotents_discarded":False,
                    "all_nine_values_from_one_polynomial_and_one_common_Phi_norm":True,
                    "finite_modular_values_not_claimed_expanded_characteristic_zero_functions":True})
            assert values["source_positive_Phi_norm"]==phi_norm_ref
            completed=self.put(stem+"-complete-nine-norms",{"prime":P,"original_direction":j,
                "source_complete_basepoint_free_pencil":pencil_ref,
                "source_complete_Artin_fibre":record["complete"],
                "source_actual_Phi_value":phi_ref,"source_positive_Phi_norm":phi_norm_ref,
                "source_complete_pencil_norm_polynomial":polyref,
                "nine_original_M_section_norms":self.ref(name),
                "nine_reference_M0_norms":record["nine_reference_norms"],
                "actual_nine_full_A_values_computed":True,
                "actual_entire_E_Phi_expression_evaluated":True,
                "all_original_expression_denominators_units_on_complete_E":True,
                "complete_E_T_Cayley_Hamilton_verified":True,
                "all_source_factors_and_nilpotents_retained":True,
                "source_node_value":context["z0"],"this_fibre_is_original_P0_or_P1":False})
            self.checkpoint(stem+"-complete")
            return completed,self.ref(stem+"-complete-nine-norms")
        except algebra.UnitFailure as exc:
            self.put(stem+"-whole-expression-unit-failure",{"prime":P,"original_direction":j,
                "source_complete_Artin_fibre":record["complete"],
                "source_complete_basepoint_free_pencil":pencil_ref,
                "unit_failure_label":exc.label,"whole_algebra_failure_witness":exc.witness,
                "no_factors_removed_and_no_partial_fibre_promoted":True,
                "original_global_function_Picard_class_or_other_fibre_not_refuted":True})
            self.checkpoint(stem+"-honest-unit-failure")
            return None,self.ref(stem+"-whole-expression-unit-failure")

    def global_ideal_and_frames(self,j,pencil,pencil_ref,full_norm_ref):
        name=f"j{j}-complete-two-chart-nine-generator-ideal-and-endpoint-expressions"
        old=self.old(name)
        if old is not None:
            return old,self.ref(name)
        frame=self.bases[j][2];Phi=self.graph.roots["Phi"+str(j)]
        generators=[]
        for t in range(9):
            generators.append({"parameter":t,
                "operation":"exact_rank8_field_norm_in_original_correspondence",
                "pullback":"original_pi_t","norm_map":"original_pi_s",
                "argument":{"operation":"positive_multiply",
                    "source_function_program":self.ref("compiled-original-marked-function-program"),
                    "multiplier_root":Phi,
                    "section":{"operation":"add","left":pencil["source_original_a"],
                               "right":{"operation":"integer_scalar_multiply","scalar":t,"source":pencil["source_original_b"]}}},
                "determinant_basis":"1,U,...,U^7 in the original function field",
                "source_original_correspondence":self.inputs["correspondence_DAG"],
                "exact_original_unit_solve_definitions_retained":True})
        reference={"source_exact_global_norm_program":self.inputs["reference_norm_program"],
            "source_original_reference_function":self.inputs["reference_function"],
            "parameters":list(range(9)),"same_generic_frame_1_and_original_M0":True}
        charts={}
        for chart in ("tau","sigma"):
            ring={"original_chart":chart,"curve":"original smooth Y","integral_normalization":"original R805 normal chart"}
            charts[chart]={"ring":ring,
                "numerator_ideal":{"operation":"sum_of_nine_principal_fractional_submodules","generators":generators},
                "denominator_ideal":reference,
                "denominator_inverse":{"operation":"colon_in_original_function_field",
                    "formula":"{x : x*J0 subset original_chart_ring}","source_ideal":reference},
                "quotient_ideal":{"operation":"multiply","formula":"Jj * colon(R,J0)"},
                "all_divisor_supports_and_all_ramification_retained":True,
                "generator_reciprocals_misused_as_inverse_ideal":False,
                "localized_by_a8_Pprime_or_r0":False}
        endpoint={}
        for point in ("P0","P1"):
            endpoint[point]={
                "original_point":point,
                "numerator":{"operation":"determinant_fibre",
                    "finite_flat_module":"pi_s* pi_t* M_j","rank":8,
                    "denominator_module":"pi_s* O_C7","denominator_rank":8,
                    "base_change":"tensor the complete original residue algebra at "+point},
                "reference":{"operation":"determinant_fibre",
                    "finite_flat_module":"pi_s* pi_t* O(254P0)","rank":8,
                    "denominator_module":"pi_s* O_C7","denominator_rank":8,
                    "source_original_reference_frame":self.reference["original_t_frame"]},
                "quotient":"numerator determinant-line fibre tensor inverse reference determinant-line fibre",
                "canonical_dual7_transports_both_determinants":True,
                "numeric_endpoint_algebra_and_transition_matrices":None,
                "numeric_endpoint_calibration_computed":False,
                "original_source_z0_fibre_substituted_for_endpoint":False}
        endpoint["P0"].update({
            "original_Iz_frame":f"t^({RHO_ORDERS[j-1]})",
            "original_Mj_frame":f"t^({RHO_ORDERS[j-1]-254})",
            "original_M0_frame":"t^(-254)",
            "source_original_Mj_P0_frame":self.inputs["directions"][str(j)]["frame"],
            "selected_Mj_section_t_frame_coefficient_mod_prime":frame["actual_t_frame_coefficient_mod_prime"],
            "selected_Mj_section_not_rescaled":True,
            "rigidification":"tensor by inverse of the same norm-quotient line at original P0"})
        endpoint["P1"].update({"original_Iz_frame":"original RF generic frame 1 at original P1",
            "source_original_P1_frame_and_polar_ideal_DAG":self.inputs["directions"][str(j)]["QZ"],
            "P0_unit_not_assumed_to_be_P1_unit":True})
        value=self.put(name,{"prime":P,"original_direction":j,
            "source_complete_basepoint_free_pencil":pencil_ref,
            "source_actual_complete_Artin_norms":full_norm_ref,
            "source_original_R903_Iz_embedding":self.inputs["directions"][str(j)]["frame"],
            "source_original_reference_function":self.inputs["reference_function"],
            "source_original_global_reference_norm_program":self.inputs["reference_norm_program"],
            "source_original_correspondence_DAG":self.inputs["correspondence_DAG"],
            "exact_global_nine_generators":generators,"complete_original_two_chart_fractional_ideals":charts,
            "direct_norm_direction":"Nm_pi_s pi_t_star",
            "frozen_original_Hecke_direction":"Nm_pi_t pi_s_star",
            "original_canonical_dual7_and_frames":self.corr_DAG["rigidified_Hecke_transport"],
            "original_function_field_correspondence":self.corr_DAG["correspondence_function_field"],
            "two_endpoint_determinant_fibre_expressions":endpoint,
            "exact_nine_generators_complete_by_actual_basepoint_free_pencil":True,
            "canonical_dual7_not_replaced_by_self_adjointness":True,
            "original_scalar7_diamond_and_minus3_descent_retained":True,
            "negative_support_of_Z_not_assumed_to_be_only_P0":True,
            "chosen_L_pencil_not_claimed_K_or_Q_fixed":True,
            "ideal_descent_datum":"norm functor applied to the original Iz descent; independent of the chosen complete generating pencil",
            "P0_endpoint_numeric_calibration_computed":False,
            "P1_endpoint_numeric_calibration_computed":False,
            "endpoint_transition_scalars_set_to_one":False,
            "materialized_global_Hermite_generators_computed":False,
            "real_descent_cubed_ideal_substituted_for_Iz":False,
            "modular_zero_used_to_mark_original_eta_inactive":False,
            "nonp_terms_Poincare_periods_or_height_computed":False})
        self.checkpoint(name)
        return value,self.ref(name)

    def direction(self,j):
        name=f"j{j}-complete-original-nine-Hecke-norm-consumer"
        complete=self.old(name)
        if complete is not None:
            assert complete["actual_original672_pencil_certified"] is True
            assert complete["actual_nine_norm_values_on_entire_Artin_fibre_computed"] is True
            self.done[str(j)]=self.ref(name);return
        pencil,pref=self.pencil(j);outcomes=[]
        for record in self.inputs["completed_artin_fibres"]:
            self.budget();value,nref=self.norm_on_fibre(j,record,pencil,pref)
            outcomes.append({"source_original_fibre":record["complete"],"success":value is not None,"stage":nref})
            if value is None:
                continue
            ideal,iref=self.global_ideal_and_frames(j,pencil,pref,nref)
            complete=self.put(name,{"prime":P,"original_direction":j,
                "source_complete_basepoint_free_pencil":pref,"source_actual_complete_Artin_nine_norms":nref,
                "complete_two_chart_Hecke_ideal_and_endpoint_expressions":iref,
                "actual_completed_fibre_outcomes":outcomes,
                "actual_original672_pencil_certified":True,
                "actual_nine_norm_values_on_entire_Artin_fibre_computed":True,
                "exact_nine_generator_Hecke_ideal_with_dual7_and_original_frame_defined":True,
                "old_reference_nine_norms_recomputed":False,
                "P0_endpoint_numeric_calibration_computed":False,"P1_endpoint_numeric_calibration_computed":False,
                "endpoint_transition_scalars_set_to_one":False,
                "global_Picard_inactivity_or_height_computed":False})
            self.done[str(j)]=self.ref(name);self.checkpoint(name);return
        raise ScopeStop(f"direction {j}: no completed R885 fibre allowed every original Phi expression denominator")

    def manifest(self):
        entries=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name==PREFIX+"current.json.gz" or path.name.startswith(PREFIX+"stage-manifest-"):
                continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag
            if value["complete"] is True:
                entries.append(spec(path))
        value={"result":RESULT,"configuration":self.tag,"complete":True,"files":entries,
            "all_complete_mathematical_stages_retained":True,"current_excluded":True}
        path=self.path("stage-manifest-"+fingerprint(entries))
        if path.exists():
            assert read(path)==value
        else:
            save(path,value)
        return spec(path)

    def finish(self,complete,error):
        if complete:
            assert all(str(j) in self.done for j in self.directions)
        value={"result":RESULT,"configuration":self.tag,"complete":bool(complete),"p":41,"prime":P,
            "requested_directions":self.directions,"actual_completed_directions":sorted(map(int,self.done)),
            "complete_direction_certificates":self.done,
            "source_audit":self.refs.get("original-source-audit"),
            "compiled_original_function_program":self.refs.get("compiled-original-marked-function-program"),
            "actual_all_requested_original672_pencils_certified":bool(complete),
            "actual_all_requested_nine_norms_on_entire_Artin_algebras_computed":bool(complete),
            "actual_all_requested_two_chart_ideals_dual7_frame_expressions_defined":bool(complete),
            "actual_all_five_directions_completed":all(str(j) in self.done for j in range(1,6)),
            "source_dimension":272,"correspondence_scalar_dimension":2176,
            "all_factors_and_nilpotent_multiplicities_retained":True,
            "old_flips_Krylov_target_embeddings_reference_norms_or_jets_recomputed":False,
            "P0_endpoint_numeric_calibration_computed":False,"P1_endpoint_numeric_calibration_computed":False,
            "endpoint_transition_scalars_set_to_one":False,
            "global_Hermite_Picard_inactivity_nonp_terms_or_height_computed":False,
            "stage_manifest":self.manifest(),"resume_state":self.current,
            "failure_or_stop_reason":error,"seconds":time.monotonic()-self.started}
        save(self.out/FINAL,value)
        return value

    def run(self):
        self.prepare();failures=[]
        for j in self.directions:
            try:
                self.direction(j)
            except ScopeStop as exc:
                failures.append(str(exc));self.checkpoint("honest-finite-scope-stop-j"+str(j))
        return self.finish(not failures,failures or None)

def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise SystemExit("New R907 mathematics runs only in authorized public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    for name in ("config","retained","output"):
        parser.add_argument("--"+name,required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args();assert 0<args.budget_minutes<=300
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    job=None;final=None;started=time.monotonic();code=1;error=None
    try:
        job=Job(args);final=job.run();code=0 if final["complete"] else 2
    except BudgetStop as exc:
        code=124;error=str(exc)
    except Exception as exc:
        error=type(exc).__name__+": "+str(exc);traceback.print_exc()
    if code in (1,124) and job is not None:
        final=job.finish(False,error)
    receipt={"result":RESULT,"source_sha256":sha(__file__),"helper_sha256":sha(pencil_algebra.__file__),
        "original_Artin_helper_sha256":sha(algebra.__file__),"complete":code==0,
        "process_exit_code":code,"error":error,"seconds":time.monotonic()-started,
        "configuration_sha256":fingerprint(job.tag) if job else None,
        "certificate_sha256":sha(out/FINAL) if (out/FINAL).exists() else None,
        "actual_completed_directions":final["actual_completed_directions"] if final else [],
        "actual_all_requested_original672_pencils_certified":bool(final and final["actual_all_requested_original672_pencils_certified"]),
        "actual_all_requested_nine_norms_on_entire_Artin_algebras_computed":bool(final and final["actual_all_requested_nine_norms_on_entire_Artin_algebras_computed"]),
        "P0_endpoint_numeric_calibration_computed":False,"P1_endpoint_numeric_calibration_computed":False,
        "global_Picard_inactivity_or_height_computed":False}
    save(out/"core-receipt.json",receipt);print(json.dumps(receipt,sort_keys=True,separators=(",",":")),flush=True)
    raise SystemExit(code)

if __name__=="__main__":
    main()

