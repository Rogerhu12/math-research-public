#!/usr/bin/env python3
"""R885 original polynomial characteristic relation and one complete adjugate row."""
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
from flint import nmod_mat, nmod_poly
REPOSITORY="Rogerhu12/math-research-public"
RESULT="R885-original-polynomial-one-row-adjugate"
FINAL="p41-original-polynomial-one-row-adjugate-certificate.json"
PREFIX="R885-adjugate-"
MANIFEST="full-outputs-manifest.json"
P=1000000753
N=272
EPS=[0]+[1]*144+[2]*127
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
STRATEGY={
    "scope": "universal-original-one-row-adjugate",
    "original_curve": "original genus127 Y; p41; level82; original minus3 descent",
    "auxiliary_prime": 1000000753,
    "normal_basis_rank": 272,
    "normal_basis_degrees": [
        0,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2
    ],
    "W_degree": 3,
    "weighted_W_bound": "1+epsilon_input-epsilon_output",
    "characteristic_coefficient_bound": "degree_z(c_k)<=k",
    "interpolation_node_count": 273,
    "interpolation_nodes": "all actual completed original eight cyclic nodes in saved order, then least unused nonnegative integers",
    "old_nodes": "reuse original W(a),K,Kinv; only missing k272 and relation are new",
    "new_nodes": "original polynomial W evaluation and exact nmod_mat charpoly; no new Krylov inverse",
    "characteristic_interpolation": "first k+1 nodes for c_k; complete all273-node substitution",
    "row_convention": "left e0 transpose",
    "row_recurrence": "b0=e0^T; b_k=b_(k-1)*W+c_k*e0^T",
    "row_bound": "degree_z(b_k,j)<=k+epsilon_j",
    "full_terminal_Cayley_Hamilton_row_verified": True,
    "whole_adjugate_matrix_computed": False,
    "old_W_or_Krylov_arithmetic_recomputed": False,
    "target_Artin_normal_coordinates_or_nine_norms_computed": False,
    "Picard_support_or_nonp_calibration_or_height_computed": False,
    "budget_excluded_from_identity": True
}

class BudgetStop(RuntimeError):
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
    tmp=path.with_name(path.name+".tmp")
    raw=(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n").encode()
    if path.suffix==".gz":
        with tmp.open("wb") as f:
            with gzip.GzipFile(filename="",fileobj=f,mode="wb",mtime=0) as g:
                g.write(raw)
    else:
        tmp.write_bytes(raw)
    tmp.replace(path)

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def plain(row):
    ans={k:row[k] for k in ("file","bytes","sha256")}
    p=PurePosixPath(ans["file"])
    assert len(p.parts)==1 and p.name not in ("",".","..") and "\\" not in ans["file"]
    assert isinstance(ans["bytes"],int) and ans["bytes"]>=0
    assert re.fullmatch("[0-9a-f]{64}",ans["sha256"])
    return ans

def spec(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}



def identity(source):
    return {**{k:source[k] for k in BASE},
            "configuration_sha256":source["configuration_sha256"],
            "configuration_stage":plain(source["configuration_stage"]),
            "selected_files_sha256":fingerprint(source["files"])}

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"p":41,
            "python_flint":"0.9.0","method_sha256":item["method_sha256"],
            "proofs":item["proofs"],"source_R827":identity(item["source"]),
            "inputs":item["inputs"],"strategy":STRATEGY}

def mat(a):
    return nmod_mat(a,P)

def rows(a):
    return [[int(a[i,j]) for j in range(a.ncols())] for i in range(a.nrows())]

def dimensions(a,m,n):
    assert len(a)==m and all(len(row)==n for row in a)

class Source:
    def __init__(self,source):
        self.source=source;self.directory=Path(source["directory"]);self.checked=set()
        self.files={name:plain(v) for name,v in source["files"].items()}
        path=self.directory/MANIFEST
        assert sha(path)==source["manifest_sha256"]
        manifest=read(path)
        assert manifest["result"]==source["result"]
        entries={row["file"]:plain(row) for row in manifest["files"]}
        assert len(entries)==len(manifest["files"])
        entries[MANIFEST]=spec(path)
        assert all(entries[name]==row for name,row in self.files.items())
        initial=self.get("public-actions-input.json");run=self.get("run-receipt.json")
        assert initial["result"]==run["result"]==source["result"]
        assert initial["source_commit"]==run["source_commit"]==source["source_commit"]
        assert str(run["workflow_run_id"])==str(source["run_id"])
        assert initial["core_sha256"]==source["core_sha256"]
        assert run["complete"] is False and run["process_exit_code"]==124
        core=self.get("core-receipt.json")
        assert run["core_receipt_sha256"]==self.files["core-receipt.json"]["sha256"]
        assert core["result"]==source["result"] and core["source_sha256"]==source["core_sha256"]
        assert core["complete"] is False
        anchor=self.get(source["configuration_stage"]["file"])
        assert anchor["complete"] is True
        self.tag=anchor["configuration"]
        assert fingerprint(self.tag)==source["configuration_sha256"]
        assert self.tag["result"]==source["result"] and self.tag["source_sha256"]==source["core_sha256"]

    def get(self,name):
        row=self.files[name];path=self.directory/name
        if name not in self.checked:
            assert spec(path)==row;self.checked.add(name)
        return read(path)

    def stage(self,row):
        row=plain(row);assert self.files[row["file"]]==row
        value=self.get(row["file"])
        assert value["complete"] is True and value["configuration"]==self.tag
        if "result" in value:
            assert value["result"]==self.source["result"]
        return value

class Job:
    def __init__(self,args):
        self.args=args;self.started=time.monotonic();self.out=Path(args.output)
        self.out.mkdir(parents=True,exist_ok=True)
        self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41
        assert self.item["producer_inputs_pending"] is False
        assert self.item["core_sha256"]==sha(__file__) and flint.__version__=="0.9.0"
        topic=Path(__file__).resolve().parent.parent
        assert sha(topic/self.item["method"])==self.item["method_sha256"]
        for value in self.item["proofs"].values():
            assert sha(topic/value["path"])==value["sha256"]
        self.source=Source(self.item["source"]);self.tag=expected_tag(self.item)
        self.refs={};self.current=None;self.node_specs=[];self.row_specs=[]
        self.Wdata=self.source.stage(self.item["inputs"]["W_reduction"])
        self.place=self.source.stage(self.item["inputs"]["place_audit"])
        self.grid=self.source.stage(self.item["inputs"]["cyclic_grid"])
        assert self.Wdata["prime"]==self.place["prime"]==P
        assert self.place["original_zeta_root"]==549966761
        assert self.Wdata["original_rational_denominators_all_units"] is True
        assert self.Wdata["original_W_e0_equals_e1_verified"] is True
        assert self.grid["distinct_residue_values_and_unit_Vandermonde_certified"] is True
        assert self.grid["all_eight_actual_determinants_nonzero"] is True
        assert len(self.grid["points"])==len(self.grid["Krylov_point_stages"])==8
        assert self.item["inputs"]["Krylov_points"]==self.grid["Krylov_point_stages"]
        self.old_points={}
        for z0,entry in zip(self.grid["points"],self.item["inputs"]["Krylov_points"]):
            value=self.source.stage(entry)
            assert value["prime"]==P and value["z0"]==z0
            assert value["usable"] is True and value["actual_cyclic_rank"]==N
            assert value["both_inverse_products_verified"] is True
            assert value["source_original_W"]==plain(self.item["inputs"]["W_reduction"])
            dimensions(value["Krylov_matrix_mod_prime"],N,N)
            dimensions(value["inverse_Krylov_matrix_mod_prime"],N,N)
            dimensions(value["W_evaluated_mod_prime"],N,N)
            assert 0<value["actual_determinant_mod_prime"]<P
            assert isinstance(z0,int) and 0<=z0<P and z0 not in self.old_points
            self.old_points[z0]=(value,plain(entry))
        self.nodes=list(self.grid["points"])
        a=0
        while len(self.nodes)<N+1:
            if a not in self.nodes:
                self.nodes.append(a)
            a+=1
        assert len(self.nodes)==len(set(self.nodes))==N+1 and max(self.nodes)<P
        self.rawW=self.Wdata["W_coefficients_mod_prime"]
        assert len(self.rawW)==4
        self.W=[]
        for d,data in enumerate(self.rawW):
            dimensions(data,N,N)
            for i,row in enumerate(data):
                for j,value in enumerate(row):
                    assert isinstance(value,int) and 0<=value<P
                    if d>1+EPS[j]-EPS[i]:
                        assert value==0,(d,i,j,"original_weighted_support")
            self.W.append(mat(data))
        self.supports=[[i for i,row in enumerate(data) if any(row)] for data in self.rawW]
        self.right_blocks=[mat([self.rawW[d][i] for i in support]) if support else None
                           for d,support in enumerate(self.supports)]
        self.source_audit()

    def budget(self):
        if time.monotonic()-self.started>=self.args.budget_minutes*60:
            raise BudgetStop("R885 budget reached; completed nodes and row levels are reusable.")

    def path(self,name):
        return self.out/(PREFIX+name+".json.gz")

    def old(self,name):
        path=self.path(name)
        if not path.exists():
            return None
        value=read(path)
        assert value["result"]==RESULT and value["complete"] is True and value["configuration"]==self.tag
        self.refs[name]=spec(path)
        return value

    def put(self,name,value):
        payload={"result":RESULT,"complete":True,"configuration":self.tag,**value}
        path=self.path(name)
        if path.exists():
            assert read(path)==payload
        else:
            save(path,payload)
        self.refs[name]=spec(path);return payload

    def checkpoint(self,phase):
        save(self.path("current"),{"result":RESULT,"complete":False,"configuration":self.tag,
                                  "phase":phase,"completed_stages":self.refs})
        self.current=spec(self.path("current"))

    def source_audit(self):
        if self.old("source-audit") is None:
            self.put("source-audit",{
                "source_R827":identity(self.item["source"]),"inputs":self.item["inputs"],
                "prime":P,"normal_basis_rank":N,"normal_basis_degrees":EPS,
                "all_original_weighted_W_entries_verified":True,
                "original_W_power_nonzero_rows":self.supports,
                "old_completed_cyclic_nodes":self.grid["points"],
                "actual_interpolation_nodes":self.nodes,
                "complete_original_Krylov_matrices_and_inverses_reused":True,
                "old_source_node_polynomials_or_k272_were_not_previously_stored":True,
                "source_failure_only_ended_later_Hermite_scope":True,
                "old_W_and_original_primitive_solutions_not_recomputed":True})
        self.checkpoint("original_sources_bound")

    def characteristic_nodes(self):
        self.node_specs=[];self.node_values=[]
        for ordinal,a in enumerate(self.nodes):
            name=f"charpoly-node-{ordinal:03d}"
            value=self.old(name)
            if value is None:
                self.budget()
                if a in self.old_points:
                    data,oldspec=self.old_points[a]
                    W=mat(data["W_evaluated_mod_prime"])
                    K=mat(data["Krylov_matrix_mod_prime"])
                    Ki=mat(data["inverse_Krylov_matrix_mod_prime"])
                    last=mat([[data["Krylov_matrix_mod_prime"][i][N-1]] for i in range(N)])
                    kn=W*last
                    h=Ki*kn
                    assert K*h==kn
                    ascending=[(-int(h[i,0]))%P for i in range(N)]+[1]
                    payload={"kind":"one_new_k272_from_completed_original_Krylov",
                             "source_original_Krylov":oldspec,
                             "new_k272":[int(kn[i,0]) for i in range(N)],
                             "relation_coefficients":[int(h[i,0]) for i in range(N)],
                             "full_K_times_relation_equals_k272":True,
                             "completed_original_Krylov_inverse_recomputed":False,
                             "new_dense_charpoly_called":False}
                else:
                    W=self.W[3]
                    for d in (2,1,0):
                        W=W*a+self.W[d]
                    polynomial=W.charpoly()
                    assert polynomial.degree()==N and int(polynomial[N])==1
                    ascending=[int(polynomial[i]) for i in range(N+1)]
                    payload={"kind":"new_nmod_mat_characteristic_polynomial",
                             "source_original_Krylov":None,"new_dense_charpoly_called":True,
                             "new_Krylov_matrix_or_inverse_computed":False}
                value=self.put(name,{
                    "prime":P,"ordinal":ordinal,"z_value":a,
                    "source_original_W":self.item["inputs"]["W_reduction"],
                    "characteristic_coefficients_ascending_T":ascending,
                    "polynomial_degree":N,"monic":True,**payload})
            assert value["prime"]==P and value["ordinal"]==ordinal and value["z_value"]==a
            co=value["characteristic_coefficients_ascending_T"]
            assert len(co)==N+1 and co[N]==1
            self.node_values.append(co);self.node_specs.append(self.refs[name])
            self.checkpoint("characteristic_nodes")

    def interpolate(self):
        value=self.old("polynomial-characteristic-relation")
        if value is None:
            self.budget()
            # Newton basis product_(j<i)(z-a_j), shared across the 272 coefficient interpolations.
            basis=[nmod_poly([1],P)]
            for a in self.nodes[:-1]:
                basis.append(basis[-1]*nmod_poly([-a,1],P))
            coefficients=[[1]]
            for k in range(1,N+1):
                table=[self.node_values[j][N-k] for j in range(k+1)]
                leading=[table[0]]
                for order in range(1,k+1):
                    table=[(table[j+1]-table[j])*pow((self.nodes[j+order]-self.nodes[j])%P,-1,P)%P
                           for j in range(k-order+1)]
                    leading.append(table[0])
                polynomial=nmod_poly([],P)
                for j,coefficient in enumerate(leading):
                    polynomial+=basis[j]*coefficient
                assert polynomial.degree()<=k
                raw=[int(polynomial[i]) for i in range(k+1)]
                for a,expected in zip(self.nodes,self.node_values):
                    assert int(polynomial(a))==expected[N-k],("all273_node_check",k,a)
                coefficients.append(raw)
            value=self.put("polynomial-characteristic-relation",{
                "prime":P,"source_original_W":self.item["inputs"]["W_reduction"],
                "source_node_stages":self.node_specs,"actual_interpolation_nodes":self.nodes,
                "matrix_rank":N,"coefficient_order":"T^272,c1*T^271,...,c272",
                "coefficient_polynomials_ascending_z":coefficients,
                "coefficient_degree_bounds":list(range(N+1)),
                "all273_nodes_for_all273_T_coefficients_verified":True,
                "degree_bounds_from_original_principal_minor_weights_verified":True,
                "exact_original_modular_characteristic_polynomial_certified":True,
                "old_Krylov_inverse_or_char0_matrix_recomputed":False})
        assert value["source_node_stages"]==self.node_specs
        self.chi=value["coefficient_polynomials_ascending_z"]
        assert len(self.chi)==N+1 and self.chi[0]==[1]
        for k,row in enumerate(self.chi):
            assert len(row)==k+1
        self.checkpoint("characteristic_polynomial_complete")

    def adjugate_row(self):
        self.row_specs=[];previous=None;current=None
        for k in range(N+1):
            name=f"row-level-{k:03d}"
            value=self.old(name)
            if value is None:
                self.budget()
                if k==0:
                    current=[[int(j==0 and degree==0) for j in range(N)] for degree in range(3)]
                else:
                    assert current is not None
                    length=len(current)
                    full=[[0]*N for _ in range(length+3)]
                    for d,support in enumerate(self.supports):
                        if not support:
                            continue
                        left=mat([[row[i] for i in support] for row in current])
                        product=left*self.right_blocks[d]
                        for degree in range(length):
                            row=full[degree+d]
                            for j in range(N):
                                row[j]=(row[j]+int(product[degree,j]))%P
                    for degree,c in enumerate(self.chi[k]):
                        full[degree][0]=(full[degree][0]+c)%P
                    for degree,row in enumerate(full):
                        for j,x in enumerate(row):
                            if degree>k+EPS[j]:
                                assert x==0,("weighted_adjugate_bound",k,degree,j)
                    current=full[:k+3]
                assert len(current)==k+3
                for degree,row in enumerate(current):
                    for j,x in enumerate(row):
                        if degree>k+EPS[j]:
                            assert x==0
                terminal=k==N
                if terminal:
                    assert all(x==0 for row in current for x in row), "full_original_Cayley_Hamilton_row"
                value=self.put(name,{
                    "prime":P,"row_level":k,"coefficient_rows_ascending_z":current,
                    "shape":[k+3,N],"component_degree_bounds":[k+e for e in EPS],
                    "source_previous_row":previous,
                    "source_characteristic_relation":self.refs["polynomial-characteristic-relation"],
                    "source_original_W":self.item["inputs"]["W_reduction"],
                    "full_weighted_support_verified":True,
                    "full_left_row_recurrence_computed":True,
                    "is_terminal_Cayley_Hamilton_row":terminal,
                    "terminal_complete_polynomial_row_zero":terminal,
                    "full_adjugate_matrix_computed":False})
            else:
                assert value["row_level"]==k and value["source_previous_row"]==previous
                assert value["source_characteristic_relation"]==self.refs["polynomial-characteristic-relation"]
                current=value["coefficient_rows_ascending_z"]
                dimensions(current,k+3,N)
                assert value["full_weighted_support_verified"] is True
                if k==N:
                    assert value["terminal_complete_polynomial_row_zero"] is True
            previous=self.refs[name];self.row_specs.append(previous)
            self.checkpoint("one_row_adjugate")
        if self.old("full-polynomial-adjugate-certificate") is None:
            self.put("full-polynomial-adjugate-certificate",{
                "prime":P,"source_original_W":self.item["inputs"]["W_reduction"],
                "characteristic_relation":self.refs["polynomial-characteristic-relation"],
                "adjugate_row_T_terms":[{"T_power":N-1-k,"b_level":k,"source":self.row_specs[k]} for k in range(N)],
                "terminal_Cayley_Hamilton_row":self.row_specs[N],
                "polynomial_identity":"r(z,T)*(T*I-W(z))=chi(z,T)*e0^T",
                "r_is_exactly_original_e0_transpose_adjugate":True,
                "all272_polynomial_components_of_terminal_row_zero":True,
                "all_coefficient_bounds_k_plus_epsilon_verified":True,
                "entire_adjugate_matrix_materialized":False,
                "characteristic_zero_polynomial_coefficients_expanded":False,
                "target_Artin_substitution_or_r0_unit_certified":False,
                "nine_reference_norms_computed":False,"original_Picard_support_or_height_computed":False})
        self.checkpoint("complete_polynomial_certificate")

    def manifest(self):
        entries=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name==self.path("current").name or path.name.startswith(PREFIX+"stage-manifest-"):
                continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
            entries.append(spec(path))
        current=spec(self.path("current")) if self.path("current").exists() else None
        value={"result":RESULT,"complete":True,"configuration":self.tag,
               "files":entries,"current_checkpoints":[] if current is None else [current]}
        path=self.path("stage-manifest-"+fingerprint(value))
        if path.exists():
            assert read(path)==value
        else:
            save(path,value)
        return spec(path)

    def finish(self,complete,error):
        done="full-polynomial-adjugate-certificate" in self.refs
        value={"result":RESULT,"configuration":self.tag,"complete":bool(complete),"p":41,
               "actual_auxiliary_prime":P,"normal_basis_rank":N,
               "source_audit":self.refs.get("source-audit"),
               "characteristic_relation":self.refs.get("polynomial-characteristic-relation"),
               "one_row_adjugate":self.refs.get("full-polynomial-adjugate-certificate"),
               "actual_interpolation_nodes":self.nodes,
               "actual_completed_node_count":len(self.node_specs),
               "actual_completed_row_level_count":len(self.row_specs),
               "actual_original_modular_characteristic_polynomial_certified":"polynomial-characteristic-relation" in self.refs,
               "actual_original_complete_polynomial_adjugate_row_certified":done,
               "full_terminal_Cayley_Hamilton_row_verified":done,
               "old_Krylov_inverses_or_original_W_recomputed":False,
               "full_adjugate_matrix_computed":False,
               "target_Artin_normal_coordinates_computed":False,"nine_reference_norms_computed":False,
               "original_Picard_support_or_nonp_calibration_or_height_computed":False,
               "stage_manifest":self.manifest(),"resume_state":self.current,
               "failure_or_stop_reason":error,"seconds":time.monotonic()-self.started}
        if complete:
            assert done
        save(self.out/FINAL,value);return value

    def run(self):
        self.characteristic_nodes();self.interpolate();self.adjugate_row()
        return self.finish(True,None)

def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise SystemExit("New R885 arithmetic only runs in the authorized public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    parser.add_argument("--config",required=True)
    parser.add_argument("--output",required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args();assert 0<args.budget_minutes<=300
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    job=None;code=1;error=None;started=time.monotonic()
    try:
        job=Job(args);job.run();code=0
    except BudgetStop as exc:
        code=124;error=str(exc)
    except Exception as exc:
        error=type(exc).__name__+": "+str(exc);traceback.print_exc()
    if code and job is not None:
        job.finish(False,error)
    receipt={"result":RESULT,"source_sha256":sha(__file__),"complete":code==0,"process_exit_code":code,
             "error":error,"seconds":time.monotonic()-started,
             "configuration":None if job is None else job.tag,
             "certificate_sha256":sha(out/FINAL) if (out/FINAL).exists() else None}
    save(out/"core-receipt.json",receipt)
    print("R885_CORE_RECEIPT="+json.dumps(receipt,sort_keys=True),flush=True)
    raise SystemExit(code)
if __name__=="__main__":
    main()
