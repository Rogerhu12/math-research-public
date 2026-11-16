#!/usr/bin/env python3
"""R922: shared low-weight trace dual on the original Y, with whole polynomial checks."""
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
RESULT="R922-original-shared-low-weight-trace-dual-multiplier"
FINAL="p41-original-shared-low-weight-trace-dual-multiplier-certificate.json"
PREFIX="R922-trace-dual-"
MANIFEST="full-outputs-manifest.json"
P=1000000753
N=272
EPS=[0]+[1]*144+[2]*127
GROUPS=("R827","POLY")
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
STRATEGY={
    "original_curve":"original genus127 Y, level82, original minus3 descent",
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "normal_basis_rank":N,"normal_basis_degrees":EPS,
    "trace_pairing":"G_ij=Tr_original_Y/k(z)(beta_i*beta_j)",
    "multiplier":"R=M_g*G^-1, column j is g*beta_j_trace_dual in the original normal basis",
    "old_node_schedule":[0,1,2,3,4],
    "Gram_nodes":"all five original completed nodes, including nonreduced fibres",
    "R_nodes":"first four nodes of the same fixed schedule with whole chi_prime polynomial gcd equal to one",
    "power_dual":"q_j=(T^(271-j)+c1*T^(270-j)+...+c_(271-j))/chi_prime",
    "matrix_inverse_policy":"reuse original K inverse; new power trace inverse by polynomial xgcd and companion multiplication, no dense inverse call",
    "Gram_degree_bound":"epsilon_i+epsilon_j",
    "R_degree_bound":"3-epsilon_i-epsilon_j; negative bound means exactly zero",
    "original_Mg_coefficient_count":6,
    "interpolation":"five Gram values and four accepted R values, exact scalar Lagrange",
    "full_acceptance":"all eight polynomial coefficients of R*G=M_g, R transpose symmetry, all weighted zeros",
    "source_factor_or_nilpotent_discarding":False,
    "separability_scope":"only for four interpolation nodes; no claim on future target fibre denominators",
    "old_W_K_inverse_Mg_or_273_characteristic_nodes_recomputed":False,
    "characteristic_zero_semantics":"exact original trace dual expression; finite arrays are only its p753 reduction",
    "seven_connections_or_Hecke_trace_or_height_computed":False,
    "budget_excluded_from_identity":True}

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


def zero():
    return nmod_mat(N,N,P)

def unit():
    return nmod_mat([[int(i==j) for j in range(N)] for i in range(N)],P)

def polynomial_rows(value):
    return [int(value[i]) for i in range(max(0,value.degree()+1))]

def horner(coefficients,a):
    result=0
    for c in reversed(coefficients):result=(result*a+int(c))%P
    return result

def evaluate_matrices(coefficients,a):
    out=zero()
    for coefficient in reversed(coefficients):out=out*a+coefficient
    return out

def scalar_lagrange(points):
    basis=[]
    for i,a in enumerate(points):
        f=nmod_poly([1],P);denominator=1
        for j,b in enumerate(points):
            if i!=j:
                f*=nmod_poly([-b,1],P)
                denominator=denominator*((a-b)%P)%P
        assert denominator
        f*=pow(denominator,-1,P)
        assert all(int(f(b))==int(i==j) for j,b in enumerate(points))
        basis.append([int(f[k]) for k in range(len(points))])
    return basis

def power_multiplication_matrix(poly,modulus):
    """Columns of multiplication by poly in 1,T,...,T^271; no matrix inverse."""
    assert len(modulus)==N+1 and modulus[N]==1
    p=nmod_poly(poly,P)%nmod_poly(modulus,P)
    current=[int(p[i]) for i in range(N)];columns=[]
    for j in range(N):
        columns.append(current)
        lead=current[-1]
        current=[(-lead*modulus[0])%P]+[
            (current[i-1]-lead*modulus[i])%P for i in range(1,N)]
    return nmod_mat(columns,P).transpose()

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
        self.tag=expected_tag(self.item);self.refs={};self.current=None
        self.inputs=self.item["inputs"]
        self.W=self.input("original_W");self.place=self.input("original_place")
        self.oi=self.input("operator_identity");self.Mg_index=self.input("original_Mg")
        self.chi=self.input("characteristic_relation")
        self.points=[]
        assert len(self.inputs["original_Krylov_points"])==5
        for ordinal,ref in enumerate(self.inputs["original_Krylov_points"]):
            point=self.source_stage(ref)
            assert point["prime"]==P and point["z0"]==ordinal
            assert point["usable"] is True and point["actual_cyclic_rank"]==N
            assert point["both_inverse_products_verified"] is True
            assert 0<point["actual_determinant_mod_prime"]<P
            assert plain(point["source_original_W"])==plain(self.inputs["original_W"])
            for key in ("Krylov_matrix_mod_prime","inverse_Krylov_matrix_mod_prime","W_evaluated_mod_prime"):
                shape(point[key],N,N)
            self.points.append(point)
        self.validate_sources()
        self.Mg=self.read_Mg()
        self.gram_specs=[];self.R_specs=[];self.R_nodes=[];self.G=None;self.R=None
        self.source_audit()

    def input(self,key):
        return self.source_stage(self.inputs[key])

    def source_stage(self,row):
        return self.sources[row["source_group"]].stage(row)

    def validate_sources(self):
        assert self.W["prime"]==self.place["prime"]==P
        assert self.W["original_rational_denominators_all_units"] is True
        assert self.W["original_W_e0_equals_e1_verified"] is True
        assert self.place["original_zeta_root"]==549966761
        assert self.place["original_s_root"]==99932770
        assert self.place["original_integral_B_root"]==3197390
        assert self.place["original_branch"]==0
        for key in ("g_vector_coefficients_mod_prime","h_vector_coefficients_mod_prime"):
            shape(self.W[key],4,N)
        assert len(self.W["W_coefficients_mod_prime"])==4
        for value in self.W["W_coefficients_mod_prime"]:shape(value,N,N)
        index=self.Mg_index
        assert index["prime"]==P and index["target"]=="g" and index["chart"]=="tau"
        assert index["regular_degree_bound"]==3 and index["normal_basis_rank"]==N
        assert index["normal_basis_degrees"]==EPS
        assert index["all_weighted_support_zeros_verified"] is True
        assert index["original_true_operator_reduction_certified"] is True
        assert len(index["row_blocks"])==len(self.inputs["Mg_blocks"])==17
        assert all(plain(a)==plain(b) for a,b in zip(index["row_blocks"],self.inputs["Mg_blocks"]))
        assert self.oi["all_operators_are_true_original_p_integral_reductions"] is True
        assert plain(self.oi["operator_indexes"]["g"]["tau"])==plain(self.inputs["original_Mg"])
        chi=self.chi
        assert chi["prime"]==P and chi["matrix_rank"]==N
        assert plain(chi["source_original_W"])==plain(self.inputs["original_W"])
        assert chi["coefficient_order"]=="T^272,c1*T^271,...,c272"
        assert chi["coefficient_degree_bounds"]==list(range(N+1))
        assert chi["all273_nodes_for_all273_T_coefficients_verified"] is True
        assert chi["degree_bounds_from_original_principal_minor_weights_verified"] is True
        assert chi["exact_original_modular_characteristic_polynomial_certified"] is True
        assert len(chi["coefficient_polynomials_ascending_z"])==N+1
        assert chi["coefficient_polynomials_ascending_z"][0]==[1]
        for k,poly in enumerate(chi["coefficient_polynomials_ascending_z"]):
            assert len(poly)==k+1 and all(isinstance(x,int) and 0<=x<P for x in poly)
        assert self.sources["POLY"].certificate["actual_original_modular_characteristic_polynomial_certified"] is True
        assert plain(self.sources["POLY"].certificate["characteristic_relation"])==plain(self.inputs["characteristic_relation"])
        same_source(self.sources["POLY"].tag["source_R827"],identity(self.item["sources"]["R827"]))

    def read_Mg(self):
        raw=[[[0]*N for _ in range(N)] for _ in range(6)]
        nextrow=0
        for ref in self.inputs["Mg_blocks"]:
            block=self.source_stage(ref)
            first,stop=block["row_first"],block["row_stop"]
            assert first==nextrow and stop==min(first+16,N)
            assert block["target"]=="g" and block["chart"]=="tau" and block["prime"]==P
            assert block["regular_degree_bound"]==3
            assert block["original_weighted_support_verified"] is True
            assert block["true_p_integral_operator_reduction_by_unit_nodes_and_original_degree_bound"] is True
            parts=block["coefficient_matrices_low_to_high"];assert len(parts)==6
            for degree,part in enumerate(parts):
                shape(part,stop-first,N)
                for r,row in enumerate(part):
                    for c,value in enumerate(row):
                        assert isinstance(value,int) and 0<=value<P
                        if degree>3+EPS[c]-EPS[first+r]:assert value==0
                    raw[degree][first+r]=row
            nextrow=stop
        assert nextrow==N
        for degree in range(6):
            for r in range(N):
                assert raw[degree][r][0]==(self.W["g_vector_coefficients_mod_prime"][degree][r] if degree<4 else 0)
        return [matrix(part) for part in raw]

    def budget(self):
        if time.monotonic()-self.started>=60*self.args.budget_minutes:
            raise BudgetStop("R922 budget; only immutable complete stages and atomic current are retained.")

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

    def checkpoint(self,phase):
        save(self.path("current"),{"result":RESULT,"complete":False,"configuration":self.tag,
            "phase":phase,"completed_stages":self.refs,
            "actual_Gram_node_count":len(getattr(self,"gram_specs",[])),
            "actual_R_nodes":getattr(self,"R_nodes",[])})
        self.current=spec(self.path("current"))

    def source_audit(self):
        if self.old("source-audit") is None:
            self.put("source-audit",{
                "sources":{g:identity(self.item["sources"][g]) for g in GROUPS},
                "inputs":self.inputs,"prime":P,"normal_basis_rank":N,"normal_basis_degrees":EPS,
                "original_node_schedule":[0,1,2,3,4],
                "all_inputs_are_original_completed_stages":True,
                "original_Mg_six_coefficient_matrices_preserved":True,
                "original_Krylov_and_inverse_bytes_not_recomputed":True,
                "old_273_characteristic_polynomial_values_not_recomputed":True,
                "original_82_scale_and_minus3_descent_preserved":True,
                "characteristic_zero_Mg_expanded":False})
        self.checkpoint("source-bound")

    def exact_expression(self):
        if self.old("exact-original-trace-dual-expression") is None:
            self.put("exact-original-trace-dual-expression",{
                "proof":self.item["proofs"]["R922"],
                "source_original_Mg":self.inputs["original_Mg"],
                "source_original_W":self.inputs["original_W"],
                "source_original_characteristic_polynomial":self.inputs["characteristic_relation"],
                "original_functions":{"delta_z":"g","nu":"dz/g","divisor_nu":"H-Cusp"},
                "normal_trace_dual":{"trace_pairing":"Tr(beta_i*beta_j_star)=Kronecker_delta_ij",
                    "r_j":"g*beta_j_star","module_identity":"g*R_tau_dual=Cusp_ideal_tau",
                    "r_j_RR_inclusion":"H0((3-epsilon_j)H-Cusp)"},
                "exact_R_definition":{"operation":"original_multiplication_matrix_times_inverse_trace_Gram",
                    "left":"M_g","right":"G^-1","trace":"original function field / original k(z)"},
                "coefficient_bounds":[[3-EPS[i]-EPS[j] for j in range(N)] for i in range(N)],
                "source_identity_does_not_replace_target_U_V":True,
                "target_coordinate_reminder":"V=K(U)/P_U(U), eight K columns are numerators",
                "exact_characteristic_zero_expression_defined":True,
                "characteristic_zero_R_coordinates_expanded":False,
                "finite_arrays_are_original_p753_reductions_only":True,
                "target_fibre_or_seven_connection_evaluation_completed":False})

    def characteristic_at(self,a):
        descending=[horner(poly,a) for poly in self.chi["coefficient_polynomials_ascending_z"]]
        assert descending[0]==1
        return list(reversed(descending))

    def gram_node(self,a):
        name=f"node-{a:02d}-whole-trace-Gram";value=self.old(name)
        if value is None:
            self.budget()
            ascending=self.characteristic_at(a)
            c=list(reversed(ascending))
            moments=[N%P]
            for k in range(1,2*N-1):
                if k<=N:
                    acc=k*c[k]+sum(c[i]*moments[k-i] for i in range(1,k))
                else:
                    acc=sum(c[i]*moments[k-i] for i in range(1,N+1))
                moments.append((-acc)%P)
            H=matrix([[moments[i+j] for j in range(N)] for i in range(N)])
            Ki=matrix(self.points[a]["inverse_Krylov_matrix_mod_prime"])
            G=Ki.transpose()*H*Ki
            assert G==G.transpose()
            value=self.put(name,{
                "prime":P,"z_value":a,
                "source_original_Krylov":self.inputs["original_Krylov_points"][a],
                "source_original_characteristic_polynomial":self.inputs["characteristic_relation"],
                "characteristic_coefficients_ascending_T":ascending,
                "power_trace_moments_exponents_0_through_542":moments,
                "whole_original_trace_Gram_mod_prime":rows(G),
                "trace_computed_by_Newton_recurrence_on_full_degree272_polynomial":True,
                "no_separability_assumption_for_Gram":True,
                "no_factor_or_nilpotent_discarded":True,
                "old_Krylov_inverse_recomputed":False})
        assert value["z_value"]==a
        assert value["source_original_Krylov"]==self.inputs["original_Krylov_points"][a]
        assert value["source_original_characteristic_polynomial"]==self.inputs["characteristic_relation"]
        shape(value["whole_original_trace_Gram_mod_prime"],N,N)
        assert len(value["power_trace_moments_exponents_0_through_542"])==2*N-1
        assert len(value["characteristic_coefficients_ascending_T"])==N+1
        return value

    def separability(self,a,gram):
        name=f"node-{a:02d}-whole-separability";value=self.old(name)
        if value is None:
            self.budget()
            chi=nmod_poly(gram["characteristic_coefficients_ascending_T"],P)
            derivative=chi.derivative();g,u,v=derivative.xgcd(chi)
            assert derivative*u+chi*v==g
            isunit=g.degree()==0 and int(g[0])!=0
            if isunit:
                scale=pow(int(g[0]),-1,P);u*=scale;v*=scale
                assert derivative*u+chi*v==nmod_poly([1],P)
            value=self.put(name,{
                "prime":P,"z_value":a,"source_whole_Gram":self.refs[f"node-{a:02d}-whole-trace-Gram"],
                "whole_polynomial_unit":bool(isunit),"gcd_degree":g.degree(),
                "gcd_coefficients_ascending_T":polynomial_rows(g),
                "inverse_chi_prime_mod_chi":polynomial_rows(u%chi) if isunit else None,
                "Bezout_coefficient_for_chi_prime":polynomial_rows(u),
                "Bezout_coefficient_for_chi":polynomial_rows(v),
                "full_polynomial_Bezout_identity_verified":True,
                "rejected_factor_retained_without_quotienting":not isunit,
                "old_fibre_cyclicity_not_used_as_separability":True})
        assert value["z_value"]==a
        assert value["source_whole_Gram"]==self.refs[f"node-{a:02d}-whole-trace-Gram"]
        return value

    def R_node(self,a,gram,separable):
        assert separable["whole_polynomial_unit"] is True
        name=f"node-{a:02d}-low-weight-R";value=self.old(name)
        if value is None:
            self.budget()
            ascending=gram["characteristic_coefficients_ascending_T"]
            c=list(reversed(ascending))
            rawQ=[[0]*N for _ in range(N)]
            for j in range(N):
                for r in range(N-j):rawQ[N-1-j-r][j]=c[r]
            Q=matrix(rawQ)
            M=power_multiplication_matrix(separable["inverse_chi_prime_mod_chi"],ascending)
            Hinv=M*Q
            moments=gram["power_trace_moments_exponents_0_through_542"]
            H=matrix([[moments[i+j] for j in range(N)] for i in range(N)])
            I=unit()
            assert H*Hinv==I and Hinv*H==I
            K=matrix(self.points[a]["Krylov_matrix_mod_prime"])
            Mg=evaluate_matrices(self.Mg,a)
            R=Mg*K*Hinv*K.transpose()
            G=matrix(gram["whole_original_trace_Gram_mod_prime"])
            assert R*G==Mg and R==R.transpose()
            value=self.put(name,{
                "prime":P,"z_value":a,"source_whole_Gram":self.refs[f"node-{a:02d}-whole-trace-Gram"],
                "source_whole_separability":self.refs[f"node-{a:02d}-whole-separability"],
                "source_original_Mg":self.inputs["original_Mg"],
                "source_original_Krylov":self.inputs["original_Krylov_points"][a],
                "R_matrix_mod_prime":rows(R),
                "power_dual_column_formula":"q_j/chi_prime; q_j=sum_(r=0)^(271-j) c_r*T^(271-j-r)",
                "both_full_power_trace_inverse_products_verified":True,
                "full_R_times_G_equals_original_Mg_at_node_verified":True,
                "full_R_symmetry_verified":True,
                "dense_matrix_inverse_called":False,
                "whole_original_fibre_retained":True})
        assert value["z_value"]==a
        assert value["source_original_Mg"]==self.inputs["original_Mg"]
        shape(value["R_matrix_mod_prime"],N,N)
        return value

    def all_nodes(self):
        gramvalues=[]
        for a in range(5):
            gram=self.gram_node(a)
            self.gram_specs.append(self.refs[f"node-{a:02d}-whole-trace-Gram"])
            gramvalues.append(gram)
            self.checkpoint("original-Gram-nodes")
        Rvalues=[]
        for a,gram in enumerate(gramvalues):
            if len(Rvalues)==4:break
            sep=self.separability(a,gram)
            if sep["whole_polynomial_unit"]:
                value=self.R_node(a,gram,sep)
                self.R_specs.append(self.refs[f"node-{a:02d}-low-weight-R"])
                self.R_nodes.append(a);Rvalues.append(value)
            self.checkpoint("whole-separable-R-nodes")
        if len(Rvalues)<4:
            raise ScopeStop("Fewer than four entire separable fibres among the five completed original nodes; no factor discarded and no new Krylov node computed.")
        return gramvalues,Rvalues

    def interpolate(self,gramvalues,Rvalues):
        name="complete-polynomial-Gram";value=self.old(name)
        if value is None:
            self.budget();weights=scalar_lagrange(list(range(5)))
            values=[matrix(q["whole_original_trace_Gram_mod_prime"]) for q in gramvalues]
            coeffs=[]
            for d in range(5):
                self.budget();C=zero()
                for i in range(5):C+=values[i]*weights[i][d]
                assert C==C.transpose()
                for i in range(N):
                    for j in range(N):
                        if d>EPS[i]+EPS[j]:assert not C[i,j]
                coeffs.append(C)
            assert all(evaluate_matrices(coeffs,a)==values[a] for a in range(5))
            value=self.put(name,{
                "prime":P,"normal_basis_rank":N,"normal_basis_degrees":EPS,
                "source_original_W":self.inputs["original_W"],
                "source_whole_trace_Gram_nodes":self.gram_specs,"interpolation_nodes":list(range(5)),
                "coefficient_matrices_low_to_high":[rows(q) for q in coeffs],
                "coefficient_count":5,"weighted_degree_bound":"epsilon_i+epsilon_j",
                "all_weighted_degree_zeros_verified":True,
                "all_five_whole_node_matrices_verified":True,
                "original_trace_Gram_polynomial_certified":True})
        assert value["source_whole_trace_Gram_nodes"]==self.gram_specs
        assert len(value["coefficient_matrices_low_to_high"])==5
        self.G=[matrix(q) for q in value["coefficient_matrices_low_to_high"]]
        self.checkpoint("polynomial-Gram")
        name="complete-polynomial-low-weight-R";value=self.old(name)
        if value is None:
            self.budget();weights=scalar_lagrange(self.R_nodes)
            values=[matrix(q["R_matrix_mod_prime"]) for q in Rvalues]
            coeffs=[]
            for d in range(4):
                self.budget();C=zero()
                for i in range(4):C+=values[i]*weights[i][d]
                assert C==C.transpose()
                for i in range(N):
                    for j in range(N):
                        if d>3-EPS[i]-EPS[j]:assert not C[i,j]
                coeffs.append(C)
            assert all(evaluate_matrices(coeffs,a)==values[i] for i,a in enumerate(self.R_nodes))
            value=self.put(name,{
                "prime":P,"normal_basis_rank":N,"normal_basis_degrees":EPS,
                "source_original_Mg":self.inputs["original_Mg"],
                "source_R_nodes":self.R_specs,"interpolation_nodes":self.R_nodes,
                "source_Gram_polynomial":self.refs["complete-polynomial-Gram"],
                "coefficient_matrices_low_to_high":[rows(q) for q in coeffs],
                "coefficient_count":4,"weighted_degree_bound":"3-epsilon_i-epsilon_j",
                "negative_weight_bound_entries_are_zero":True,
                "all_weighted_degree_zeros_verified":True,
                "all_four_whole_node_matrices_verified":True,
                "full_matrix_symmetry_verified":True,
                "all_127_by127_weight_two_block_entries_zero":True,
                "finite_R_polynomial_before_full_multiplication_check":True})
        assert value["source_R_nodes"]==self.R_specs and value["interpolation_nodes"]==self.R_nodes
        assert len(value["coefficient_matrices_low_to_high"])==4
        self.R=[matrix(q) for q in value["coefficient_matrices_low_to_high"]]
        self.checkpoint("polynomial-R")

    def full_identity(self):
        name="complete-original-RG-equals-Mg";value=self.old(name)
        if value is None:
            blocks=[]
            for degree in range(8):
                partname=f"polynomial-product-coefficient-{degree:02d}"
                part=self.old(partname)
                if part is None:
                    self.budget();product=zero()
                    for i in range(4):
                        j=degree-i
                        if 0<=j<5:product+=self.R[i]*self.G[j]
                    expected=self.Mg[degree] if degree<6 else zero()
                    assert product==expected,("full_polynomial_RG",degree)
                    part=self.put(partname,{
                        "prime":P,"coefficient_of_z":degree,
                        "source_R_polynomial":self.refs["complete-polynomial-low-weight-R"],
                        "source_Gram_polynomial":self.refs["complete-polynomial-Gram"],
                        "source_original_Mg":self.inputs["original_Mg"],
                        "original_Mg_coefficient_or_zero":degree if degree<6 else None,
                        "all272_by272_coefficients_checked":True,
                        "full_product_equals_original_Mg_coefficient":True,
                        "product_matrix_sha256":fingerprint(rows(product)),
                        "expected_matrix_sha256":fingerprint(rows(expected))})
                assert part["coefficient_of_z"]==degree
                assert part["source_R_polynomial"]==self.refs["complete-polynomial-low-weight-R"]
                assert part["source_Gram_polynomial"]==self.refs["complete-polynomial-Gram"]
                blocks.append(self.refs[partname]);self.checkpoint("complete-polynomial-product")
            value=self.put(name,{
                "prime":P,"source_R_polynomial":self.refs["complete-polynomial-low-weight-R"],
                "source_Gram_polynomial":self.refs["complete-polynomial-Gram"],
                "source_original_Mg":self.inputs["original_Mg"],
                "coefficient_checks":blocks,"all_eight_z_coefficients_checked":True,
                "all272_by272_polynomial_entries_checked":True,
                "whole_polynomial_R_times_G_equals_original_Mg_verified":True,
                "true_original_trace_dual_identified_by_nonzero_Gram":True,
                "R_weighted_degrees_and_symmetry_verified":True,
                "auxiliary_prime_reduction_of_original_characteristic_zero_R_certified":True,
                "characteristic_zero_R_coordinates_expanded":False,
                "old_Mg_W_K_inverse_or_characteristic_polynomial_recomputed":False,
                "finite_fibre_factors_or_nilpotents_discarded":False})
        assert len(value["coefficient_checks"])==8
        self.checkpoint("full-identity-certified")

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

    def finish(self,complete,error):
        done="complete-original-RG-equals-Mg" in self.refs
        value={"result":RESULT,"configuration":self.tag,"complete":bool(complete),"p":41,
            "actual_auxiliary_prime":P,"normal_basis_rank":N,"normal_basis_degrees":EPS,
            "source_audit":self.refs.get("source-audit"),
            "exact_original_trace_dual_expression":self.refs.get("exact-original-trace-dual-expression"),
            "polynomial_trace_Gram":self.refs.get("complete-polynomial-Gram"),
            "polynomial_low_weight_R":self.refs.get("complete-polynomial-low-weight-R"),
            "complete_polynomial_identity":self.refs.get("complete-original-RG-equals-Mg"),
            "actual_Gram_nodes":list(range(len(self.gram_specs))),
            "actual_R_nodes":self.R_nodes,
            "actual_original_low_weight_R_mod_p_certified":done,
            "actual_all_polynomial_RG_equal_Mg_entries_verified":done,
            "exact_characteristic_zero_trace_dual_expression_defined":"exact-original-trace-dual-expression" in self.refs,
            "characteristic_zero_R_coordinates_expanded":False,
            "old_W_Mg_Krylov_inverse_or_273_characteristic_nodes_recomputed":False,
            "seven_connection_numerators_evaluated_on_target":False,
            "target_denominators_or_differential_frame_units_certified":False,
            "original_Hecke_projector_endpoint_nonp_or_height_computed":False,
            "stage_manifest":self.manifest(),"resume_state":self.current,
            "failure_or_stop_reason":error,"seconds":time.monotonic()-self.started}
        if complete:assert done and len(self.gram_specs)==5 and len(self.R_nodes)==4
        save(self.out/FINAL,value);return value

    def run(self):
        self.exact_expression()
        gramvalues,Rvalues=self.all_nodes()
        self.interpolate(gramvalues,Rvalues);self.full_identity()
        return self.finish(True,None)

def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise SystemExit("R922 new arithmetic runs only in the authorized public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    for name in ("config","retained","output"):parser.add_argument("--"+name,required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args();assert 0<args.budget_minutes<=300
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    job=None;code=1;error=None;started=time.monotonic()
    try:
        job=Job(args);certificate=job.run();code=0 if certificate["complete"] else 2
    except ScopeStop as exc:code=2;error=str(exc)
    except BudgetStop as exc:code=124;error=str(exc)
    except Exception as exc:error=type(exc).__name__+": "+str(exc);traceback.print_exc()
    if code in (1,2,124) and job is not None:job.finish(False,error)
    receipt={"result":RESULT,"source_sha256":sha(__file__),"complete":code==0,
        "process_exit_code":code,"error":error,"seconds":time.monotonic()-started,
        "configuration":None if job is None else job.tag,
        "certificate_sha256":sha(out/FINAL) if (out/FINAL).exists() else None,
        "new_arithmetic_only_in_public_Actions":True}
    save(out/"core-receipt.json",receipt)
    log={k:v for k,v in receipt.items() if k!="configuration"}
    log["configuration_sha256"]=None if job is None else fingerprint(job.tag)
    print("R922_CORE_RECEIPT="+json.dumps(log,sort_keys=True),flush=True)
    raise SystemExit(code)
if __name__=="__main__":main()
