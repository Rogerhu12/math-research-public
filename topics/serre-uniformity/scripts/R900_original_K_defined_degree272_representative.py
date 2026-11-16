#!/usr/bin/env python3
"""R900: original K-defined degree272 representative of the fixed Picard class.
Only source-bound characteristic-zero unit-solve expressions are certified.
The numeric arrays are their images at the original p753 place.
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
RESULT="R900-original-K-defined-degree272-representative"
FINAL="p41-original-K-defined-degree272-representative-certificate.json"
PREFIX="R900-"
MANIFEST="full-outputs-manifest.json"
P=1000000753
N=272
EPS=[0]+[1]*144+[2]*127
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
MANDATORY=("R899","R894","R883","R827","R890")
STRATEGY={
    "original_curve":"original genus127 Y, level82 and original minus3 descent",
    "ground_field":"original K=Q(zeta), not an auxiliary residue field",
    "prime":P,"original_branch":0,"original_integral_B_root":3197390,
    "original_s_root":99932770,"original_zeta_root":549966761,
    "normal_basis_degrees":EPS,"normal_V3_dimension":690,
    "input_K_fixed_functions":"S_i=original_QN*w_i; w_i are the already tau-normalized normal V3 functions",
    "input_normal_space_shape":[690,418],
    "first_anchor":"first unscaled original R899 column with unit pole-leading coefficient at P0",
    "second_anchor":"sum(c^i*S_i), exact positive integer c=1,2,...; same coefficients on w_i",
    "shared_QN_cancellation":"S0*r+S1*s=QN*(w0*r+w1*s); all normal V3 functions are already tau-normalized",
    "first_original_product_shape":[1904,1380],"first_product_rank":1234,
    "first_common_divisor_degree":272,"D0_degree":544,
    "complete_H0_3H_minus_D0_dimension":146,
    "first_kernel_projection":"second690 original V3 rows",
    "v_selection":"first unchanged canonical146 column with unit value at original P0",
    "second_pencil":"sum(c^i*U_i), exact positive integer c=1,2,...",
    "second_original_product_shape":[1904,1380],"second_product_rank":962,
    "DK_degree":272,"complete_H0_3H_minus_DK_dimension":418,
    "whole_source_fibres":[0,1,2,3,4,5,6],
    "whole_fibre_length":1904,"degree6H":1632,
    "whole_artin_factors_or_multiplicities_removed":False,
    "canonical_K_descent":"K-stable relation space plus free-coordinate identity; no new Galois sampling",
    "principal_QK":"QN*w0/v; w0 and v are already tau-normalized, with no additional tau power",
    "class_identity":"T0=(DK-H)+div(QK)",
    "original_QN_rho_order":-8435,"QK_rho_order":-8435,
    "QK_rho_leading":"original_LC_QN*w0(P0)/v(P0)",
    "QK_t_leading":"QK_rho_leading*original_c^8435",
    "old_16_flips_QN_K_basis_Krylov_normal_evaluations_and_point_jets_recomputed":False,
    "fixed_anchor_products_shared_across_trials":True,
    "normal_integer_scale_applied_again":False,
    "characteristic_zero_coordinates_reconstructed":False,
    "nonp_Hecke_support_Picard_principality_connection_period_or_height_computed":False,
    "only_budget_and_two_positive_integer_trial_limits_excluded_from_identity":True,
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
        if self.label=="R827":
            assert "result" not in value
            assert value["configuration"]["result"]==self.item["result"]
        else:
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
        self.tag=expected_tag(self.item);self.refs={};self.current=None
        self.phase="source_initialization"
        self.sources={g:Source(g,v,args.retained) for g,v in self.item["sources"].items()}
        self.inputs=self.item["inputs"]
        self.first_trials=int(self.item.get("maximum_first_pencil_trials",4))
        self.second_trials=int(self.item.get("maximum_second_pencil_trials",4))
        assert 1<=self.first_trials<P and 1<=self.second_trials<P
        self.V3=positions(3);assert len(self.V3)==690
        self.fibres={};self.completed={}
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
        print("R900_STAGE="+json.dumps({"file":path.name,"seconds":time.monotonic()-self.started}),flush=True)
        return value
    def checkpoint(self,phase):
        self.phase=phase
        value={"result":RESULT,"configuration":self.tag,"complete":False,
               "phase":phase,"completed_certificates":self.completed,"complete_stages":self.refs}
        save(self.path("current"),value);self.current=spec(self.path("current"))
        return self.current
    def source(self,row):
        return self.sources[row["source_group"]].stage(row)
    def input(self,key):
        return self.source(self.inputs[key])
    def own(self,row):
        path=self.out/plain(row)["file"];assert spec(path)==plain(row)
        value=read(path)
        assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
        return value
    def ref(self,name):
        return plain(self.refs[name])


    def prepare(self):
        source=self.sources["R899"]
        certificate=source.certificate
        assert certificate is not None and certificate["complete"] is True
        assert certificate["result"]=="R899-original-K-fixed-seven-trace-RR-basis"
        assert certificate["all418_original_K_fixed_functions_certified"] is True
        assert certificate["new_fixed_basis_descent_identity_certified"] is True
        for group in ("R894","R890","R827","R883"):
            same_origin(self.sources[group].item,certificate["source_identities"][group])
        assert plain(certificate["complete_K_fixed_normal_basis"])==plain(self.inputs["K_fixed_normal_basis"])
        assert plain(certificate["original_P0_leading_row"])==plain(self.inputs["P0_leading_row"])
        basis=self.input("K_fixed_normal_basis")
        local=self.input("P0_leading_row")
        shape(basis["normal_V3_basis_mod_prime"],690,418)
        assert basis["normal_V3_basis"]==[list(p) for p in self.V3]
        self.normal_basis=matrix(basis["normal_V3_basis_mod_prime"])
        self.QN_source=self.inputs["original_QN"]
        assert self.QN_source["source_group"]=="R894"
        assert plain(self.QN_source)==plain(basis["source_original_QN"])==plain(certificate["marked_QN"])
        same_origin(self.sources["R894"].item,certificate["source_identities"]["R894"])
        self.marked_QN=self.input("original_QN")
        assert self.marked_QN["actual_rho_order"]==-8435
        assert self.marked_QN["DN_avoids_original_P0"] is True
        assert self.marked_QN["DN_effective_degree"]==272
        assert self.marked_QN["complete_W_DN_dimension"]==418
        assert self.marked_QN["Q_orbit_fixed_by_original_Gal_L_over_K"] is True
        assert self.marked_QN["original_fractional_ideal_principal_factor_direction"]=="positive multiplication by Q_N"
        assert self.marked_QN["exact_original_divisor_identity"]=="T_f^0=(D_N-H)+div(Q_N)"
        assert isinstance(self.marked_QN["exact_QN_function_DAG"],dict)
        assert plain(self.marked_QN["source_complete_DN_normal418"])==plain(basis["source_original_DN_normal418"])
        definition=basis["exact_fixed_functions_DAG"]
        assert definition["operation"]=="positive_multiply_original_QN"
        assert plain(definition["original_QN_source"])==plain(self.QN_source)
        assert definition["normal_sections"]["operation"]=="right_multiply_original_WN_basis"
        assert plain(definition["normal_sections"]["source_original_WN"])==plain(basis["source_original_DN_normal418"])
        assert isinstance(definition["normal_sections"]["exact_basis_change_unit_solve"],dict)
        assert basis["all418_original_K_fixed_functions_certified"] is True
        assert basis["normal_sections_without_QN_claimed_K_fixed"] is False
        assert basis["new_fixed_basis_action_identity_certified_by_uniqueness"] is True
        assert plain(basis["source_selected_evaluation_inverse"]) in [
            plain(row) for row in source.item["files"].values()]
        # The stage contains the underlying normal w_i, not the full K-fixed functions S_i.
        self.P0_functional=local["normal_V3_P0_functional_mod_prime"]
        self.P0_values=local["normal_V3_P0_values_mod_prime"]
        self.rho_leading=local["rho_leading_coefficients_mod_prime"]
        self.t_leading=local["t_leading_coefficients_mod_prime"]
        assert len(self.P0_functional)==690
        assert len(self.P0_values)==len(self.rho_leading)==len(self.t_leading)==418
        for values in (self.P0_functional,self.P0_values,self.rho_leading,self.t_leading):
            assert all(isinstance(x,int) and 0<=x<P for x in values)
        self.first_unit_column=local["first_unit_column"]
        assert local["original_rho_and_t_order"]==-8435
        assert local["selected_column_rescaled"] is False
        assert local["old_point_jets_or_t_constant_recomputed"] is False
        assert plain(local["source_K_fixed_normal_basis"])==plain(self.inputs["K_fixed_normal_basis"])
        assert plain(local["source_original_QN"])==plain(self.QN_source)
        assert plain(local["source_original_t_frame"])==plain(self.inputs["t_frame"])
        actual=next((i for i in range(418) if self.P0_values[i] and self.rho_leading[i] and self.t_leading[i]),None)
        assert self.first_unit_column==actual
        self.fixed_T0={
            "definition":"the original fixed T0 in the completed R899 H0(2H-T0)",
            "source_R899_certificate":source.ref(source.item["certificate"]),
            "source_original_QN":self.QN_source,"source_R899_marked_QN_reference":certificate["marked_QN"],
            "source_complete_K_fixed_functions":self.inputs["K_fixed_normal_basis"],
            "same_original_trace_divisor_not_a_new_Picard_class":True}
        frame=self.input("t_frame")
        assert frame["original_t_first_order_unit_certified"] is True
        assert frame["exact_zero_not_inferred_from_modular_zero"] is True
        self.t_over_rho=int(frame["original_t_over_rho_constant_mod_prime"])
        assert self.t_over_rho==354813668
        assert int(local["actual_QN_rho_leading_mod_prime"])==int(self.marked_QN["actual_QN_rho_leading_mod_prime"])
        assert int(local["actual_QN_t_leading_mod_prime"])==int(self.marked_QN["actual_QN_t_leading_mod_prime"])
        assert int(local["actual_original_c_power8435_mod_prime"])==int(self.marked_QN["actual_original_c_power8435_mod_prime"])
        assert set(self.inputs["original_normal_V3_fibres"])==set(map(str,range(7)))
        assert set(self.inputs["original_Krylov_points"])==set(map(str,range(7)))
        assert set(self.inputs.get("completed_normalized_space_fibres",{}))<=set(map(str,range(7)))
        for a in range(7):
            for key in ("original_normal_V3_fibres","original_Krylov_points"):
                old=certificate[key][a] if isinstance(certificate[key],list) else certificate[key][str(a)]
                assert plain(old)==plain(self.inputs[key][str(a)])
        assert plain(certificate["original_W"])==plain(self.inputs["original_W"])
        assert {a:plain(row) for a,row in certificate["completed_normalized_space_fibres"].items()}=={
            a:plain(row) for a,row in self.inputs.get("completed_normalized_space_fibres",{}).items()}
        W=self.input("original_W")
        assert W["prime"]==P
        for a in range(7):
            self.fibre(a)
        for a,ref in self.inputs.get("completed_normalized_space_fibres",{}).items():
            value=self.source(ref)
            assert value["prime"]==P and value["z0"]==int(a)
            assert value["original_QN_factor_included"] is False
            assert plain(value["source_K_fixed_normal_basis"])==plain(self.inputs["K_fixed_normal_basis"])
            shape(value["normal_evaluation_mod_prime"],272,418)
            shape(value["cyclic_evaluation_mod_prime"],272,418)
        name="original-source-audit";audit=self.old(name)
        if audit is None:
            audit=self.put(name,{"prime":P,"sources":{g:identity(v) for g,v in self.item["sources"].items()},
                "inputs":self.inputs,"source_R899_certificate":source.ref(source.item["certificate"]),
                "source_original_DN_normal418":plain(basis["source_original_DN_normal418"]),
                "source_original_QN":self.QN_source,
                "source_QN_configuration":self.sources["R894"].tag,
                "original_QN_function_DAG_preserved":self.marked_QN["exact_QN_function_DAG"],
                "source_actual_K_normalizing_inverse":plain(basis["source_selected_evaluation_inverse"]),
                "exact_fixed_functions_DAG":basis["exact_fixed_functions_DAG"],
                "source_fixed_T0":self.fixed_T0,
                "normal_space_shape":[690,418],"normal_V3_basis":[list(p) for p in self.V3],
                "original_K_fixed_functions_include_positive_QN":True,
                "underlying_normal_columns_alone_not_claimed_K_fixed":True,
                "source_original_P0_functional_preserved":True,
                "source_first_unit_column":self.first_unit_column,
                "original_QN_rho_order":-8435,"whole_original_nodes":list(range(7)),
                "completed_R899_normalized_space_nodes":sorted(map(int,self.inputs.get("completed_normalized_space_fibres",{}))),
                "QN_units_in_all_seven_fibres_required":False,
                "old_W_K_Kinverse_normal_V3_and_point_functional_arithmetic_recomputed":False,
                "actual_K_fixed_space_source_required_before_new_arithmetic":True})
            self.checkpoint(name)
        assert audit["sources"]=={g:identity(v) for g,v in self.item["sources"].items()}
        assert audit["inputs"]==self.inputs


    def fibre(self,a):
        if a in self.fibres:
            return self.fibres[a]
        eref=self.inputs["original_normal_V3_fibres"][str(a)]
        kref=self.inputs["original_Krylov_points"][str(a)]
        Edata=self.source(eref);Kdata=self.source(kref)
        assert Edata["prime"]==Kdata["prime"]==P and Edata["z0"]==Kdata["z0"]==a
        assert Edata["normal_V3_basis"]==[list(p) for p in self.V3]
        assert Edata["normal_integer_scale_applied_again"] is False
        assert Edata["old_W_K_or_Kinverse_recomputed"] is False
        assert Kdata["usable"] is True and Kdata["actual_cyclic_rank"]==N
        assert Kdata["both_inverse_products_verified"] is True
        assert plain(Edata["source_original_Krylov_point"])==plain(kref)
        assert plain(Edata["source_original_W"])==plain(self.inputs["original_W"])
        for key in ("normal_evaluation_mod_prime","cyclic_evaluation_mod_prime"):
            shape(Edata[key],N,690)
        for key in ("W_evaluated_mod_prime","Krylov_matrix_mod_prime","inverse_Krylov_matrix_mod_prime"):
            shape(Kdata[key],N,N)
        value={"E":matrix(Edata["normal_evaluation_mod_prime"]),
               "CE":matrix(Edata["cyclic_evaluation_mod_prime"]),
               "W":matrix(Kdata["W_evaluated_mod_prime"]),
               "reference":eref,"K_reference":kref}
        self.fibres[a]=value
        return value

    def normalized_space_fibre(self,a):
        external=self.inputs.get("completed_normalized_space_fibres",{}).get(str(a))
        if external is not None:
            value=self.source(external)
            assert value["prime"]==P and value["z0"]==a
            assert value["original_QN_factor_included"] is False
            assert plain(value["source_K_fixed_normal_basis"])==plain(self.inputs["K_fixed_normal_basis"])
            assert plain(value["source_original_normal_V3_fibre"])==plain(self.inputs["original_normal_V3_fibres"][str(a)])
            assert plain(value["source_original_Krylov_point"])==plain(self.inputs["original_Krylov_points"][str(a)])
            shape(value["normal_evaluation_mod_prime"],N,418)
            shape(value["cyclic_evaluation_mod_prime"],N,418)
            return matrix(value["normal_evaluation_mod_prime"]),external
        name=f"completed-normalized-space-fibre-{a}"
        value=self.old(name)
        if value is None:
            self.budget()
            f=self.fibre(a)
            normal=f["E"]*self.normal_basis
            cyclic=f["CE"]*self.normal_basis
            value=self.put(name,{"prime":P,"z0":a,"matrix_shape":[272,418],
                "source_K_fixed_normal_basis":self.inputs["K_fixed_normal_basis"],
                "source_original_normal_V3_fibre":f["reference"],
                "source_original_Krylov_point":f["K_reference"],
                "normal_evaluation_mod_prime":rows(normal),
                "cyclic_evaluation_mod_prime":rows(cyclic),
                "original_QN_factor_included":False,
                "only_missing_new_normalized_basis_evaluation_computed":True,
                "old_original_normal_V3_or_Krylov_arithmetic_recomputed":False,
                "normal_integer_scale_applied_again":False})
            self.checkpoint(name)
        assert value["source_K_fixed_normal_basis"]==self.inputs["K_fixed_normal_basis"]
        return matrix(value["normal_evaluation_mod_prime"]),self.ref(name)

    def products(self,stem,anchor,anchor_ref,normalized=False):
        data=[];references=[]
        for a in range(7):
            name=stem+f"-fibre-{a}-times-original-V3"
            value=self.old(name)
            if value is None:
                self.budget()
                f=self.fibre(a)
                if normalized:
                    basis,bref=self.normalized_space_fibre(a)
                    vector=basis*matrix([[x] for x in anchor["original_basis_weights_mod_prime"]])
                    evaluation_source=bref
                else:
                    vector=f["E"]*matrix([[x] for x in anchor["normal_V3_coordinates_mod_prime"]])
                    evaluation_source=f["reference"]
                columns=[];current=vector
                for i in range(N):
                    columns.append([int(current[row,0]) for row in range(N)])
                    if i+1<N:
                        current=f["W"]*current
                product=matrix(columns).transpose()*f["CE"]
                value=self.put(name,{"prime":P,"z0":a,"source_anchor":anchor_ref,
                    "source_actual_anchor_evaluation":evaluation_source,
                    "source_original_normal_V3_fibre":f["reference"],
                    "source_original_Krylov_point":f["K_reference"],
                    "matrix_shape":[272,690],"product_evaluation_mod_prime":rows(product),
                    "anchor_evaluation_mod_prime":[int(vector[i,0]) for i in range(N)],
                    "formula":"[v,Wv,...,W^271v]*(old_Kinverse*normal_V3)",
                    "whole272_dimensional_Artin_fibre_retained":True,
                    "factors_or_nilpotents_removed":False,
                    "old_Krylov_inverse_QN_or_point_arithmetic_recomputed":False})
                self.checkpoint(name)
            assert value["source_anchor"]==anchor_ref and value["z0"]==a
            shape(value["product_evaluation_mod_prime"],N,690)
            data.extend(value["product_evaluation_mod_prime"]);references.append(self.ref(name))
        return matrix(data),references

    def original_anchor(self,trial=None):
        name="original-unscaled-S0" if trial is None else f"original-S1-trial-{trial:06d}"
        value=self.old(name)
        if value is None:
            self.budget()
            if trial is None:
                column=self.first_unit_column
                if column is None:
                    raise UnitFailure("No retained original K-fixed basis column has a unit P0 pole-leading value.")
                weights=[int(i==column) for i in range(418)]
                vector=[int(self.normal_basis[i,column]) for i in range(690)]
                local=self.P0_values[column]
                leadingrho=self.rho_leading[column];leadingt=self.t_leading[column]
                definition={"operation":"unchanged_original_K_fixed_basis_column",
                            "source_K_fixed_functions":self.inputs["K_fixed_normal_basis"],"column":column}
            else:
                assert 1<=trial<P
                weights=[pow(trial,i,P) for i in range(418)]
                computed=self.normal_basis*matrix([[x] for x in weights])
                vector=[int(computed[i,0]) for i in range(690)]
                local=sum(x*y for x,y in zip(self.P0_values,weights))%P
                leadingrho=sum(x*y for x,y in zip(self.rho_leading,weights))%P
                leadingt=sum(x*y for x,y in zip(self.t_leading,weights))%P
                column=None
                definition={"operation":"exact_positive_integer_power_combination_of_K_fixed_functions",
                            "source_K_fixed_functions":self.inputs["K_fixed_normal_basis"],
                            "integer_parameter":trial,"exponents":[0,417]}
            if trial is None:
                invert(local,"Original unscaled w0(P0)");invert(leadingrho,"Original S0 rho leading")
                invert(leadingt,"Original S0 t leading")
            value=self.put(name,{"prime":P,"trial":trial,"role":"S0" if trial is None else "S1",
                "source_K_fixed_normal_basis":self.inputs["K_fixed_normal_basis"],
                "source_original_P0_leading_row":self.inputs["P0_leading_row"],
                "source_original_QN":self.QN_source,
                "selected_original_column":column,"original_basis_weights_mod_prime":weights,
                "normal_V3_coordinates_mod_prime":vector,
                "actual_normal_value_at_P0_mod_prime":local,
                "actual_S_rho_leading_mod_prime":leadingrho,"actual_S_t_leading_mod_prime":leadingt,
                "S_P0_pole_order_bound":8435,"actual_order_minus8435_certified":trial is None,
                "exact_K_fixed_function_definition":definition,
                "full_function":"original_QN*already_tau_normalized_normal_V3_function",
                "extra_tau_power":0,
                "normal_section_alone_not_claimed_K_fixed":True,
                "original_scalar_not_rescaled":True,
                "first_anchor_has_residual_zero_divisor_degree544_avoiding_P0":trial is None,
                "exact_original_K_function_certified":True})
            self.checkpoint(name)
        assert value["source_K_fixed_normal_basis"]==self.inputs["K_fixed_normal_basis"]
        assert value["trial"]==trial
        return value,self.ref(name)

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


    def first_residual_space(self,S0,S0ref):
        name="complete-K-defined-D0-146-certificate"
        value=self.old(name)
        if value is not None:
            assert value["source_unscaled_S0"]==S0ref
            space=self.own(value["complete_normal146_space"])
            return matrix(space["normal_V3_basis_mod_prime"]),space,value["complete_normal146_space"],value,self.ref(name)
        fixed,fixed_refs=self.products("fixed-original-w0",S0,S0ref,normalized=True)
        for trial in range(1,self.first_trials+1):
            stem=f"first-pencil-trial-{trial:06d}";old=self.old(stem+"-rank")
            if old is not None and old["accepted"] is False:
                continue
            S1,S1ref=self.original_anchor(trial)
            right,right_refs=self.products(stem+"-w1",S1,S1ref,normalized=True)
            M=hcat(fixed,right)
            assert M.nrows()==1904 and M.ncols()==1380
            refs={"source_complete_K_fixed_functions":self.inputs["K_fixed_normal_basis"],
                  "source_unscaled_S0":S0ref,"source_S1":S1ref,
                  "source_w0_products":fixed_refs,"source_w1_products":right_refs,
                  "whole_original_nodes":list(range(7))}
            profile,pref=self.rank_profile(stem+"-rank",M,1234,refs,{
                "source_proof":self.item["proofs"]["R900"],
                "formula":"rank[w0 V3,w1 V3]=1234-deg(extra_common_zero)",
                "fixed_common_divisor":"original DN","fixed_common_divisor_degree":272,
                "complete_fibre_length":1904,"degree6H":1632,
                "shared_nonzero_QN_is_cancelled_before_evaluation":True,
                "full_original_V6_injection":True})
            if profile["accepted"] is not True:
                del M,right;gc.collect();continue
            K,kcert,kref=self.complete_kernel(stem,M,profile,pref,{
                "original_relation":"S0*r+S1*s=0",
                "same_relation_after_cancelling_QN":"w0*r+w1*s=0",
                "common_zero_of_w0_w1_exactly":"original DN",
                "complete_relation_dimension":146,"original_weight":6,
                "original_S0_and_S1_are_K_fixed":True,
                "K_fixed_relation_basis_by_unique_free_coordinate_identity":True,
                "not_from_modular_Galois_samples":True})
            U,space,sref=self.project_second(stem+"-complete-K-fixed-normal146-space",K,kref,146,{
                "space":"H0(3H-D0)","D0":"div(S0)+2H-T0",
                "degree_D0":544,"D0_effective_K_defined_and_avoids_P0":True,
                "source_unscaled_S0":S0ref,"source_K_fixed_basis":self.inputs["K_fixed_normal_basis"],
                "all_original_normal_V3_sections_are_K_defined":True,
                "K_fixed_by_canonical_relation_and_projection":True,
                "same_original_Y_and_tau_frame":True})
            value=self.put(name,{"prime":P,"accepted_second_anchor_integer":trial,
                "source_complete_K_fixed_functions":self.inputs["K_fixed_normal_basis"],
                "source_unscaled_S0":S0ref,"source_S1":S1ref,
                "source_w0_products":fixed_refs,"source_w1_products":right_refs,
                "source_rank_profile":pref,"source_complete_relation_kernel":kref,
                "complete_normal146_space":sref,
                "actual_product_rank":1234,"all_original_product_rows_checked":1904,
                "complete_relation_dimension":146,"second_projection_dimension":146,
                "D0_degree":544,"D0_effective":True,"D0_defined_over_original_K":True,
                "D0_avoids_original_P0":True,"exact_D0_definition":"div(S0)+2H-T0",
                "source_fixed_T0":self.fixed_T0,
                "whole_original_V6_evaluation_injective":True,
                "source_QN_not_evaluated_again":True,
                "canonical_relation_free_coordinates_give_K_fixed_basis":True,
                "complete_characteristic_zero_H0_3H_minus_D0_certified":True,
                "actual_arrays_are_only_modular_reductions":True})
            self.completed["D0_146"]=self.ref(name);self.checkpoint(name)
            del M,right,K;gc.collect()
            return U,space,sref,value,self.ref(name)
        raise ScopeStop("No first 1234 unit pencil in the completed finite positive-integer schedule.")

    def U_P0_values(self,U,Uref):
        name="complete-normal146-original-P0-values"
        value=self.old(name)
        if value is None:
            self.budget()
            evaluated=matrix([self.P0_functional])*U
            values=[int(evaluated[0,j]) for j in range(146)]
            column=next((j for j,x in enumerate(values) if x),None)
            value=self.put(name,{"prime":P,"source_complete_normal146_space":Uref,
                "source_original_P0_functional":self.inputs["P0_leading_row"],
                "normal_V3_P0_values_mod_prime":values,"first_unit_column":column,
                "original_P0_functional_recomputed":False,
                "new_complete146_space_evaluated_at_original_P0":True,
                "normal_integer_scale_applied_again":False})
            self.checkpoint(name)
        assert value["source_complete_normal146_space"]==Uref
        if value["first_unit_column"] is None:
            raise UnitFailure("No unit P0 column observed in the complete146 space at this place.")
        return value,self.ref(name)

    def U_anchor(self,U,Uref,local,localref,trial=None):
        name="original-unscaled-v" if trial is None else f"second-anchor-trial-{trial:06d}"
        value=self.old(name)
        if value is None:
            self.budget()
            if trial is None:
                column=local["first_unit_column"]
                weights=[int(i==column) for i in range(146)]
                vector=[int(U[i,column]) for i in range(690)]
                at0=local["normal_V3_P0_values_mod_prime"][column]
                definition={"operation":"unchanged_canonical_K_fixed146_column",
                            "source_complete146_space":Uref,"column":column}
            else:
                column=None;weights=[pow(trial,i,P) for i in range(146)]
                computed=U*matrix([[x] for x in weights])
                vector=[int(computed[i,0]) for i in range(690)]
                at0=sum(x*y for x,y in zip(local["normal_V3_P0_values_mod_prime"],weights))%P
                definition={"operation":"exact_positive_integer_power_combination",
                            "source_complete146_space":Uref,"integer_parameter":trial,"exponents":[0,145]}
            if trial is None:
                invert(at0,"Original unscaled v(P0)")
            value=self.put(name,{"prime":P,"role":"v" if trial is None else "second_pencil_w","trial":trial,
                "source_complete146_space":Uref,"source_complete146_P0_values":localref,
                "selected_original_column":column,"original_basis_weights_mod_prime":weights,
                "normal_V3_coordinates_mod_prime":vector,"actual_value_at_original_P0_mod_prime":at0,
                "exact_section_definition":definition,"section_defined_over_original_K":True,
                "original_scalar_not_rescaled":True,"exact_P0_unit_certified":trial is None,
                "normal_tau_power":3})
            self.checkpoint(name)
        assert value["source_complete146_space"]==Uref and value["trial"]==trial
        return value,self.ref(name)

    def second_bounded_space(self,U,Uref,local,localref,D0ref,v,vref):
        name="complete-K-defined-DK-418-certificate"
        value=self.old(name)
        if value is not None:
            assert value["source_exact_v"]==vref and value["source_complete_D0_certificate"]==D0ref
            space=self.own(value["complete_normal418_space"])
            return space,value["complete_normal418_space"],value,self.ref(name)
        fixed,fixed_refs=self.products("fixed-original-v",v,vref)
        for trial in range(1,self.second_trials+1):
            stem=f"second-pencil-trial-{trial:06d}";old=self.old(stem+"-rank")
            if old is not None and old["accepted"] is False:
                continue
            w,wref=self.U_anchor(U,Uref,local,localref,trial)
            right,right_refs=self.products(stem+"-w",w,wref)
            M=hcat(fixed,right)
            assert M.nrows()==1904 and M.ncols()==1380
            refs={"source_complete_D0_certificate":D0ref,"source_complete146_space":Uref,
                  "source_exact_v":vref,"source_exact_w":wref,
                  "source_v_products":fixed_refs,"source_w_products":right_refs,
                  "whole_original_nodes":list(range(7))}
            profile,pref=self.rank_profile(stem+"-rank",M,962,refs,{
                "source_proof":self.item["proofs"]["R900"],
                "formula":"rank[v V3,w V3]=962-deg(extra_common_zero)",
                "fixed_common_divisor":"D0","fixed_common_divisor_degree":544,
                "complete_fibre_length":1904,"degree6H":1632,"full_original_V6_injection":True})
            if profile["accepted"] is not True:
                del M,right;gc.collect();continue
            K,kcert,kref=self.complete_kernel(stem,M,profile,pref,{
                "original_relation":"v*r+w*s=0","common_zero_exactly":"D0",
                "complete_relation_dimension":418,"original_weight":6,
                "original_v_and_w_are_K_defined":True,
                "K_fixed_relation_basis_by_unique_free_coordinate_identity":True,
                "not_from_modular_Galois_samples":True})
            _,space,sref=self.project_second(stem+"-complete-K-fixed-normal418-space",K,kref,418,{
                "space":"H0(3H-DK)","DK":"div_3H(v)-D0","degree_DK":272,
                "DK_effective_K_defined_and_avoids_P0":True,
                "source_exact_v":vref,"source_complete_D0_certificate":D0ref,
                "K_fixed_by_canonical_relation_and_projection":True,
                "same_original_Y_and_tau_frame":True})
            value=self.put(name,{"prime":P,"accepted_second_anchor_integer":trial,
                "source_complete_D0_certificate":D0ref,"source_complete146_space":Uref,
                "source_exact_v":vref,"source_exact_w":wref,
                "source_rank_profile":pref,"source_complete_relation_kernel":kref,
                "complete_normal418_space":sref,
                "source_v_products":fixed_refs,"source_w_products":right_refs,
                "actual_product_rank":962,"all_original_product_rows_checked":1904,
                "complete_relation_dimension":418,"second_projection_dimension":418,
                "DK_degree":272,"DK_effective":True,"DK_defined_over_original_K":True,
                "DK_avoids_original_P0":True,"exact_DK_definition":"div_3H(v)-D0",
                "whole_original_V6_evaluation_injective":True,
                "canonical_relation_free_coordinates_give_K_fixed_basis":True,
                "complete_characteristic_zero_H0_3H_minus_DK_certified":True,
                "actual_arrays_are_only_modular_reductions":True})
            self.completed["DK_418"]=self.ref(name);self.checkpoint(name)
            del M,right,K;gc.collect()
            return space,sref,value,self.ref(name)
        raise ScopeStop("No final 962 unit pencil in the completed finite positive-integer schedule.")

    def principal(self,S0,S0ref,D0ref,Uref,v,vref,DKref,spaceref):
        name="original-K-defined-DK-and-marked-principal-QK"
        value=self.old(name)
        if value is None:
            self.budget()
            at0=int(v["actual_value_at_original_P0_mod_prime"])
            inv=invert(at0,"v(P0) in the marked principal")
            rho_leading=int(S0["actual_S_rho_leading_mod_prime"])*inv%P
            c_power=pow(self.t_over_rho,8435,P)
            t_leading=rho_leading*c_power%P
            assert t_leading==int(S0["actual_S_t_leading_mod_prime"])*inv%P
            assert rho_leading and t_leading
            nodes=[
                {"id":"QN","operation":"completed_original_marked_principal",
                 "source_original_QN":self.QN_source,
                 "source_completed_K_fixed_functions":self.inputs["K_fixed_normal_basis"]},
                {"id":"w0","operation":"unscaled_original_normal_V3_section_over_tau3",
                 "source":S0ref,"normal_coordinates_already_mean_section_over_tau3":True},
                {"id":"S0","operation":"positive_multiply","left":"QN","right":"w0",
                 "source_certified_K_fixed_function":S0["exact_K_fixed_function_definition"]},
                {"id":"v","operation":"unscaled_canonical_K_fixed_V3_section_over_tau3",
                 "source":vref,"normal_coordinates_already_mean_section_over_tau3":True},
                {"id":"QK","operation":"divide","numerator":"S0","denominator":"v",
                 "formula":"QN*w0/v with w0 and v already tau-normalized","extra_tau_power":0}]
            value=self.put(name,{"prime":P,"source_original_K_fixed_functions":self.inputs["K_fixed_normal_basis"],
                "source_original_P0_leading_row":self.inputs["P0_leading_row"],
                "source_original_QN":self.QN_source,
                "source_unscaled_S0":S0ref,"source_complete_D0_certificate":D0ref,
                "complete_normal146_space":Uref,"source_unscaled_exact_v":vref,
                "source_complete_DK_certificate":DKref,"complete_normal418_space":spaceref,
                "source_original_t_frame":self.inputs["t_frame"],"source_fixed_T0":self.fixed_T0,
                "exact_principal_DAG":nodes,"QK_root":"QK",
                "exact_D0_definition":"div(S0)+2H-T0","D0_degree":544,
                "exact_DK_definition":"div_3H(v)-D0","DK_degree":272,
                "exact_class_identity":"T0=(DK-H)+div(QK)",
                "QK_defined_over_original_K":True,"DK_defined_over_original_K":True,
                "D0_and_DK_avoid_original_P0":True,
                "actual_QK_rho_order":-8435,"actual_QK_t_order":-8435,
                "actual_original_w0_P0_mod_prime":S0["actual_normal_value_at_P0_mod_prime"],
                "actual_original_S0_rho_leading_mod_prime":S0["actual_S_rho_leading_mod_prime"],
                "actual_original_v_P0_mod_prime":at0,
                "actual_QK_rho_leading_mod_prime":rho_leading,
                "actual_original_t_over_rho_mod_prime":self.t_over_rho,
                "actual_original_t_scaling_power":8435,"actual_original_c_power_mod_prime":c_power,
                "actual_QK_t_leading_mod_prime":t_leading,
                "exact_marked_leading_expression":{
                    "rho":"original_LC_QN*w0(P0)/v(P0)","t":"rho_leading*original_c^8435",
                    "source_original_QN_P0":self.inputs["P0_leading_row"],
                    "source_w0":S0ref,"source_v":vref,"source_c":self.inputs["t_frame"]},
                "positive_QN_and_positive_c8435_retained":True,
                "original_unscaled_sections_and_tau_frames_preserved":True,
                "original_t_or_QN_jets_recomputed":False,
                "no_prime41_unit_claim_from_auxiliary_unit":True,
                "characteristic_zero_coordinates_reconstructed":False,
                "Picard_principality_Hecke_support_connection_period_or_height_computed":False})
            self.completed["marked_QK"]=self.ref(name);self.checkpoint(name)
        assert value["source_unscaled_S0"]==S0ref and value["source_unscaled_exact_v"]==vref
        return value,self.ref(name)


    def inventory(self):
        files=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name==PREFIX+"current.json.gz" or path.name.startswith(PREFIX+"stage-manifest-"):
                continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
            files.append(spec(path))
        name="stage-manifest-"+fingerprint({"files":files,"current":self.current})
        self.put(name,{"files":files,"file_count":len(files),"files_sha256":fingerprint(files),
            "current_checkpoints":[self.current] if self.current is not None else [],
            "only_complete_atomic_new_mathematical_stages_listed":True,
            "old_source_stages_remain_in_their_original_source_directories":True})
        return self.ref(name)

    def finish(self,complete,reason):
        endpoint={
            "D0_146":"complete-K-defined-D0-146-certificate",
            "DK_418":"complete-K-defined-DK-418-certificate",
            "marked_QK":"original-K-defined-DK-and-marked-principal-QK"}
        for key,name in endpoint.items():
            if self.old(name) is not None:
                self.completed[key]=self.ref(name)
        if complete:
            assert set(self.completed)==set(endpoint)
        current=self.checkpoint(self.phase)
        final={"result":RESULT,"configuration":self.tag,"complete":bool(complete),"p":41,"prime":P,
            "source_audit":self.refs.get("original-source-audit"),
            "source_original_R899_K_fixed_basis":self.inputs.get("K_fixed_normal_basis"),
            "source_original_P0_leading_row":self.inputs.get("P0_leading_row"),
            "source_original_t_frame":self.inputs.get("t_frame"),
            "complete_first_residual_certificate":self.completed.get("D0_146"),
            "complete_K_defined_degree272_certificate":self.completed.get("DK_418"),
            "marked_original_principal_QK":self.completed.get("marked_QK"),
            "complete_direction_certificates":self.completed,
            "actual_D0_degree":544 if "D0_146" in self.completed else None,
            "actual_DK_degree":272 if "DK_418" in self.completed else None,
            "actual_complete_H0_3H_minus_D0_dimension":146 if "D0_146" in self.completed else None,
            "actual_complete_H0_3H_minus_DK_dimension":418 if "DK_418" in self.completed else None,
            "original_K_defined_degree272_representative_certified":"DK_418" in self.completed,
            "original_K_defined_marked_principal_certified":"marked_QK" in self.completed,
            "canonical_K_fixed_relation_bases_certified":"DK_418" in self.completed,
            "full_seven_whole_fibres_for_V6_not_six_fibre_support_assumption":True,
            "QN_units_in_all_seven_fibres_required":False,
            "old_flips_QN_K_basis_Krylov_jets_or_V3_evaluations_recomputed":False,
            "characteristic_zero_coefficients_reconstructed":False,
            "nonp_Hecke_support_Picard_principality_connection_period_or_height_computed":False,
            "stage_manifest":self.inventory(),"resume_state":current,
            "scope_stop_reason":reason,"seconds":time.monotonic()-self.started}
        save(self.out/FINAL,final)
        print("R900_FINAL_SUMMARY="+json.dumps({k:final[k] for k in (
            "complete","original_K_defined_degree272_representative_certified",
            "original_K_defined_marked_principal_certified",
            "actual_complete_H0_3H_minus_D0_dimension","actual_complete_H0_3H_minus_DK_dimension",
            "scope_stop_reason","seconds")}),flush=True)
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
                assert old["original_K_defined_degree272_representative_certified"] is True
                assert old["original_K_defined_marked_principal_certified"] is True
                return old
        self.prepare()
        S0,S0ref=self.original_anchor()
        U,Udata,Uref,D0,D0ref=self.first_residual_space(S0,S0ref)
        local,localref=self.U_P0_values(U,Uref)
        v,vref=self.U_anchor(U,Uref,local,localref)
        space,sref,DK,DKref=self.second_bounded_space(U,Uref,local,localref,D0ref,v,vref)
        self.principal(S0,S0ref,D0ref,Uref,v,vref,DKref,sref)
        return self.finish(True,None)

def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config",type=Path,required=True)
    parser.add_argument("--retained",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--budget-minutes",type=float,required=True)
    args=parser.parse_args()
    assert 0<args.budget_minutes<=300
    args.output.mkdir(parents=True,exist_ok=True)
    job=None;code=1;error=None;certificate=None;started=time.monotonic()
    try:
        job=Job(args);certificate=job.run();code=0 if certificate["complete"] else 2
    except BudgetStop as exc:
        code=124;error=str(exc)
        if job is not None:
            certificate=job.finish(False,error)
    except (UnitFailure,ScopeStop) as exc:
        code=2;error=str(exc)
        if job is not None:
            certificate=job.finish(False,error)
    except Exception as exc:
        code=1;error=type(exc).__name__+": "+str(exc);traceback.print_exc()
    finally:
        path=args.output/FINAL
        receipt={"result":RESULT,"source_sha256":sha(__file__),
            "configuration":job.tag if job is not None else None,
            "configuration_sha256":fingerprint(job.tag) if job is not None else None,
            "complete":code==0,"process_exit_code":code,"error":error,
            "certificate_sha256":sha(path) if path.exists() else None,
            "seconds":time.monotonic()-started,
            "new_mathematics_executed_only_in_public_Actions":True}
        save(args.output/"core-receipt.json",receipt)
        print("R900_CORE_RECEIPT="+json.dumps(receipt,sort_keys=True),flush=True)
    return code

if __name__=="__main__":
    raise SystemExit(main())
