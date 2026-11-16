#!/usr/bin/env python3
"""R885 original whole Artin target normal coordinates and nine reference norms."""
import argparse
from array import array
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
from flint import nmod_mat
import R885_whole_Artin_algebra as algebra
from R885_whole_Artin_algebra import SourceAlgebra, CorrespondenceAlgebra, UnitFailure

REPOSITORY="Rogerhu12/math-research-public"
RESULT="R885-original-whole-Artin-reference-norms"
FINAL="p41-original-whole-Artin-reference-norms-certificate.json"
PREFIX="R885-Artin-"
MANIFEST="full-outputs-manifest.json"
P=1000000753
N=272
EPS=[0]+[1]*144+[2]*127
GROUPS=("POLY","R827","R882","R873","R879","R807")
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
STRATEGY={
    "original_curve":"original genus127 Y, p41, original level82 and minus3 descent",
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "source_algebra":"Fp[X]/chi(a,X), entire272-dimensional Artin fibre",
    "source_nodes":"completed original eight cyclic nodes, in their actual saved order",
    "correspondence_algebra":"A[U]/(P(U)/a8), free rank8 over entire A",
    "target_w":"K(U)/Pprime(U)","normal_basis_rank":272,"normal_basis_degrees":EPS,
    "normal_column_block_size":16,"T_Horner_checkpoint_levels":16,
    "target_adjugate":"completed polynomial r(U,V), one complete original left row",
    "target_normalization":"gamma_j=r_j/r_0, only if r_0 is a unit on entire E",
    "target_verification":"all272 components gamma*(V*I-W(U))=0 and gamma0=1",
    "base_unit":"unreduced polynomial Bezout identity and full A product",
    "extension_unit":"division-free8 Berkowitz norm and complete E product",
    "reference_function":"original R879 f/u in its unchanged normal basis",
    "nine_norms":"one8 characteristic polynomial, det(I+t*M_x) for t0..8",
    "original_frame":"R879 t^-254 and lc(t/x)^254/U272 retained, never replaced by1",
    "norm_orientation":"Nm_source(target^*section), transported to frozen Nm_target(source^*I) by original dual7 involution",
    "factors_removed_or_semisimplicity_assumed":False,
    "old_polynomial_adjugate_Krylov_or17_coordinates_recomputed":False,
    "old_reference_system_theta_or_E6_clearing_recomputed":False,
    "finite_fibre_values_used_as_global_Picard_or_height_certificate":False,
    "budget_and_requested_fibre_count_excluded_from_identity":True}

class BudgetStop(RuntimeError):
    pass

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(4*1024*1024),b""):
            h.update(b)
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
            with gzip.GzipFile(filename="",fileobj=f,mode="wb",mtime=0,compresslevel=2) as z:
                z.write(raw)
    else:
        tmp.write_bytes(raw)
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
    answer={**{k:source[k] for k in BASE},"configuration_sha256":source["configuration_sha256"],
            "selected_files_sha256":fingerprint(source["files"])}
    if source.get("certificate") is not None:
        answer["certificate"]=plain(source["certificate"])
    else:
        answer["configuration_stage"]=plain(source["configuration_stage"])
    return answer

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"helper_sha256":item["helper_sha256"],
            "python_flint":"0.9.0","p":41,"method_sha256":item["method_sha256"],"proofs":item["proofs"],
            "sources":{g:identity(item["sources"][g]) for g in GROUPS},
            "inputs":item["inputs"],"strategy":STRATEGY}

def same_source(left,right):
    assert all(str(left[k])==str(right[k]) for k in BASE)
    assert left["configuration_sha256"]==right["configuration_sha256"]

def matrix(raw):
    return nmod_mat(raw,P)

def rows(mat):
    return [[int(mat[i,j]) for j in range(mat.ncols())] for i in range(mat.nrows())]

def shape(raw,m,n):
    assert len(raw)==m and all(len(row)==n for row in raw)

class Source:
    def __init__(self,label,item,root):
        self.label=label;self.item=item;self.directory=Path(root)/label;self.checked=set()
        self.files={name:plain(v) for name,v in item["files"].items()}
        assert all(k==v["file"] for k,v in self.files.items())
        mpath=self.directory/MANIFEST
        assert sha(mpath)==item["manifest_sha256"]
        manifest=read(mpath)
        assert manifest["result"]==item["result"]
        entries={r["file"]:plain(r) for r in manifest["files"]}
        assert len(entries)==len(manifest["files"])
        entries[MANIFEST]=spec(mpath)
        assert all(entries[k]==v for k,v in self.files.items())
        initial=self.get("public-actions-input.json")
        run=self.get("run-receipt.json");core=self.get("core-receipt.json")
        assert initial["source_commit"]==run["source_commit"]==item["source_commit"]
        assert str(run["workflow_run_id"])==str(item["run_id"])
        recorded=initial["core_sha256"] if "core_sha256" in initial else initial["job"]["core_sha256"]
        assert recorded==core["source_sha256"]==item["core_sha256"]
        if run.get("core_receipt_sha256") is not None:
            assert run["core_receipt_sha256"]==self.files["core-receipt.json"]["sha256"]
        if label=="R827":
            assert item.get("certificate") is None
            assert run["complete"] is False and core["complete"] is False
            assert run["process_exit_code"]==124
            self.certificate=None
            anchor=self.get(item["configuration_stage"]["file"])
            assert anchor["complete"] is True
            self.tag=anchor["configuration"]
        else:
            assert run["complete"] is True and run["process_exit_code"]==0 and core["complete"] is True
            self.certificate=self.get(item["certificate"]["file"])
            assert self.certificate["complete"] is True and self.certificate["result"]==item["result"]
            assert self.files[item["certificate"]["file"]]==plain(item["certificate"])
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

class Job:
    def __init__(self,args):
        self.args=args;self.started=time.monotonic();self.out=Path(args.output)
        self.out.mkdir(parents=True,exist_ok=True)
        self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41 and self.item["producer_inputs_pending"] is False
        assert sha(__file__)==self.item["core_sha256"] and flint.__version__=="0.9.0"
        assert sha(algebra.__file__)==self.item["helper_sha256"]
        assert Path(algebra.__file__).name==self.item["helper"]
        topic=Path(__file__).resolve().parent.parent
        assert sha(topic/self.item["method"])==self.item["method_sha256"]
        for value in self.item["proofs"].values():
            assert sha(topic/value["path"])==value["sha256"]
        assert set(self.item["sources"])==set(GROUPS)
        self.sources={g:Source(g,self.item["sources"][g],args.retained) for g in GROUPS}
        self.tag=expected_tag(self.item);self.refs={};self.current=None;self.outcomes=[]
        self.inputs=self.item["inputs"]
        self.char=self.input("characteristic_relation")
        self.adj=self.input("adjugate_row_index")
        self.Wdata=self.input("original_W")
        self.grid=self.input("original_grid")
        self.place=self.input("original_place")
        assert self.place["prime"]==P and self.place["original_zeta_root"]==549966761
        self.C17=self.input("seventeen_coordinates")
        self.common=self.input("same_place_interface")
        self.DAG=self.input("correspondence_DAG")
        self.reference=self.input("reference_function")
        self.theta=self.input("theta")
        self.clearing=self.input("E6_clearing")
        self.chi=self.char["coefficient_polynomials_ascending_z"]
        assert len(self.chi)==273 and self.chi[0]==[1]
        assert self.char["exact_original_modular_characteristic_polynomial_certified"] is True
        assert self.char["all273_nodes_for_all273_T_coefficients_verified"] is True
        assert self.adj["r_is_exactly_original_e0_transpose_adjugate"] is True
        assert self.adj["all272_polynomial_components_of_terminal_row_zero"] is True
        assert self.adj["characteristic_relation"]==plain(self.inputs["characteristic_relation"])
        assert len(self.adj["adjugate_row_T_terms"])==272
        assert len(self.inputs["row_levels"])==272
        for k,(term,source) in enumerate(zip(self.adj["adjugate_row_T_terms"],self.inputs["row_levels"])):
            assert term["b_level"]==k and term["T_power"]==271-k and plain(term["source"])==plain(source)
        assert len(self.grid["points"])==len(set(self.grid["points"]))==8
        assert len(self.inputs["original_characteristic_nodes"])==len(self.inputs["original_Krylov_points"])==8
        for j in range(8):
            assert plain(self.inputs["original_characteristic_nodes"][j])==plain(self.char["source_node_stages"][j])
            assert plain(self.inputs["original_Krylov_points"][j])==plain(self.grid["Krylov_point_stages"][j])
        assert self.grid["all_eight_actual_determinants_nonzero"] is True
        assert self.Wdata["prime"]==self.C17["prime"]==P
        self.W=self.Wdata["W_coefficients_mod_prime"]
        assert len(self.W)==4
        for row in self.W:
            shape(row,272,272)
        self.Wmat=[matrix(a) for a in self.W]
        self.coordinate=matrix(self.C17["coordinate_matrix_mod_prime"])
        assert self.coordinate.nrows()==2058 and self.coordinate.ncols()==17
        assert self.C17["same_characteristic_zero_coefficients_integral_at_new_place"] is True
        assert plain(self.C17["source_exact_R873_unit_solve"])==plain(self.DAG["coefficient_unit_solve"])
        assert self.sources["R882"].certificate["all2200_by17_original_equations_verified"] is True
        assert self.sources["R882"].certificate["actual_auxiliary_prime"]==P
        assert self.sources["R882"].certificate["original_zeta_root"]==549966761
        assert self.common["prime"]==P and self.common["original_zeta_root"]==549966761
        assert self.common["all2200_by17_original_equations_verified"] is True
        assert plain(self.common["source_R873_correspondence_DAG"])==plain(self.inputs["correspondence_DAG"])
        assert plain(self.common["new_modular_coordinates"])==plain(self.inputs["seventeen_coordinates"])
        assert self.reference["prime"]==P and self.reference["original_zeta_root"]==549966761
        assert self.reference["normal_basis_degrees"]==EPS
        assert self.reference["actual_reference_basepoint_free_pencil_certified"] is True
        for key in ("numerator_normal_polynomial_mod_prime","denominator_normal_polynomial_mod_prime"):
            shape(self.reference[key],3,272)
        assert self.theta["original_M2_integer_scale"]=="6724"
        assert len(self.theta["theta_in_original_integer_scaled_M2_basis"])==146
        assert self.theta["theta_nonzero_by_original_independent_M2_input"] is True
        assert plain(self.theta["M6_index692_cleared_coordinate_stage"])==plain(self.inputs["E6_clearing"])
        assert self.clearing["M6_index"]==692 and self.clearing["basis_dimension"]==962
        assert self.clearing["all1100_rows_verified"] is True and self.clearing["exact_global_V4_membership_certified"] is True
        assert self.clearing["basis_integer_scale"]==str(82**8)
        assert len(self.clearing["solution_numerators"])==962
        assert plain(self.DAG["E6hat_over_tau3"]["theta_source"])==plain(self.inputs["theta"])
        assert plain(self.DAG["E6hat_over_tau3"]["V4_coordinate_source"])==plain(self.inputs["E6_clearing"])
        assert self.DAG["E6hat_over_tau3"]["new_scale_applied"]=="1"
        assert self.DAG["rigidified_Hecke_transport"]["frozen_direction"]=="Nm_pi_t(pi_s^*I)"
        same_source(self.sources["POLY"].tag["source_R827"],identity(self.item["sources"]["R827"]))
        same_source(self.sources["R882"].tag["sources"]["R873"],identity(self.item["sources"]["R873"]))
        same_source(self.sources["R873"].tag["sources"]["R807"],identity(self.item["sources"]["R807"]))
        assert self.item["required_successful_fibres"]>=1
        assert self.item["required_successful_fibres"]<=self.item["maximum_source_nodes"]<=8
        self.row_cache={}
        self.source_audit()

    def input(self,key):
        row=self.inputs[key]
        return self.sources[row["source_group"]].stage(row)

    def read_ref(self,row):
        return self.sources[row["source_group"]].stage(row)

    def budget(self):
        if time.monotonic()-self.started>=self.args.budget_minutes*60:
            raise BudgetStop("R885 Artin budget: all completed source fibre stages are retained.")

    def path(self,name):
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
        payload={"result":RESULT,"configuration":self.tag,"complete":True,**value}
        path=self.path(name)
        if path.exists():
            assert read(path)==payload
        else:
            save(path,payload)
        self.refs[name]=spec(path)
        return payload

    def checkpoint(self,phase):
        save(self.path("current"),{"result":RESULT,"complete":False,"configuration":self.tag,
                                  "phase":phase,"completed_stages":self.refs,"fibre_outcomes":self.outcomes})
        self.current=spec(self.path("current"))

    def source_audit(self):
        if self.old("source-audit") is None:
            self.put("source-audit",{
                "sources":{g:identity(self.item["sources"][g]) for g in GROUPS},"inputs":self.inputs,
                "source_node_schedule":self.grid["points"],"prime":P,
                "original_zeta_root":549966761,"original_s_root":99932770,
                "original_272_normal_basis_degrees":EPS,
                "old_complete_one_row_polynomial_source_preserved":True,
                "old17_coordinates_and_reference_system_not_recomputed":True,
                "old_theta_E6_clearing_and_Krylov_inverses_not_recomputed":True,
                "whole_Artin_fibre_required":True})
        self.checkpoint("sources")

    def b_flat(self,k):
        if k not in self.row_cache:
            value=self.read_ref(self.inputs["row_levels"][k])
            assert value["row_level"]==k and value["shape"]==[k+3,272]
            assert value["full_weighted_support_verified"] is True
            assert value["source_characteristic_relation"]==plain(self.inputs["characteristic_relation"])
            raw=value["coefficient_rows_ascending_z"];shape(raw,k+3,272)
            self.row_cache[k]=array("I",(x for row in raw for x in row))
        return self.row_cache[k]

    def fibre_source(self,ordinal,z0):
        stem=f"node-{ordinal:02d}"
        old=self.old(stem+"-source-functions")
        node=self.read_ref(self.inputs["original_characteristic_nodes"][ordinal])
        point=self.read_ref(self.inputs["original_Krylov_points"][ordinal])
        assert node["z_value"]==point["z0"]==z0 and point["prime"]==P
        assert point["usable"] is True and point["both_inverse_products_verified"] is True
        assert point["actual_cyclic_rank"]==272
        assert point["source_original_W"]==plain(self.inputs["original_W"])
        assert node["source_original_Krylov"]==plain(self.inputs["original_Krylov_points"][ordinal])
        modulus=node["characteristic_coefficients_ascending_T"]
        A=SourceAlgebra(modulus)
        if old is not None:
            assert old["source_characteristic_node"]==self.inputs["original_characteristic_nodes"][ordinal]
            assert old["source_node_value"]==z0 and old["complete_source_algebra_modulus"]==modulus
            coefficients=[A.unpack(row) for row in old["seventeen_values_over_A"]]
            assert len(coefficients)==17
            return stem,A,coefficients
        self.budget()
        inverse=point["inverse_Krylov_matrix_mod_prime"];shape(inverse,272,272)
        beta=[A.element([inverse[i][j] for i in range(272)]) for j in range(272)]
        assert beta[0]==A.one
        e=[A.one,A.sub(A.element(z0),beta[72])]+[beta[i-1] for i in range(2,146)]
        assert len(e)==146 and e[2]==A.X
        theta=A.zero
        for value,coefficient in zip(e,self.theta["theta_in_original_integer_scaled_M2_basis"]):
            assert len(coefficient)==2
            theta=A.add(theta,A.mul(value,A.fraction(coefficient[0],coefficient[1])))
        theta_inverse,theta_proof=A.inverse(theta,"theta_over_tau")
        memo={():A.one}
        def product(indices):
            key=tuple(sorted(indices))
            assert all(isinstance(i,int) and 0<=i<146 for i in key)
            if key not in memo:
                memo[key]=A.mul(product(key[:-1]),e[key[-1]])
            return memo[key]
        denominator=int(self.clearing["solution_common_denominator"])
        if denominator%P==0:
            raise UnitFailure("completed_N692_common_denominator",{
                "original_denominator":str(denominator),"prime":P,"denominator_residue":0,
                "source":self.inputs["E6_clearing"],"whole_fibre_retained":True})
        inverse_denominator=pow(denominator%P,-1,P)
        numerator=A.zero
        used=[]
        for row in self.DAG["E6hat_over_tau3"]["nonzero_V4_monomials"]:
            index=row["source_coordinate_index"]
            assert row["original_V4_index"]==index and 0<=index<962
            indices=row["original_M2_leaf_indices"];assert len(indices)==4
            coefficient=int(self.clearing["solution_numerators"][index])*inverse_denominator%P
            numerator=A.add(numerator,A.scale(product(indices),coefficient))
            used.append(index)
        assert used==[i for i,x in enumerate(self.clearing["solution_numerators"]) if int(x)]
        E6hat=A.mul(numerator,theta_inverse)
        square=A.mul(E6hat,E6hat)
        functions=[]
        for index,row in enumerate(self.DAG["old_V8_over_tau8"]):
            assert row["index"]==index and len(row["original_M2_leaf_indices"])==8
            functions.append(product(row["original_M2_leaf_indices"]))
        assert len(functions)==2050
        for k,row in enumerate(self.DAG["new_eight_complement_functions"]):
            assert row["index"]==2050+k and len(row["original_M2_leaf_indices"])==2
            functions.append(A.mul(square,product(row["original_M2_leaf_indices"])))
        assert len(functions)==2058
        raw=[A.pack(value) for value in functions]
        image=matrix(raw).transpose()*self.coordinate
        coefficients=[A.element([int(image[i,j]) for i in range(272)]) for j in range(17)]
        self.put(stem+"-source-functions",{
            "source_node_ordinal":ordinal,"source_node_value":z0,"prime":P,
            "source_characteristic_node":self.inputs["original_characteristic_nodes"][ordinal],
            "source_original_Krylov":self.inputs["original_Krylov_points"][ordinal],
            "source_DAG":self.inputs["correspondence_DAG"],
            "source_seventeen_coordinates":self.inputs["seventeen_coordinates"],
            "source_theta":self.inputs["theta"],"source_E6_clearing":self.inputs["E6_clearing"],
            "complete_source_algebra_modulus":modulus,"source_algebra_dimension":272,
            "original_M2_functions_over_A":[A.pack(value) for value in e],
            "theta_unit_certificate":theta_proof,"E6hat_over_tau3":A.pack(E6hat),
            "completed_N692_common_denominator":str(denominator),
            "new_scale_applied":"1","original82_scales_retained_once":True,
            "original2058_basis_function_values_over_A":raw,
            "seventeen_values_over_A":[A.pack(value) for value in coefficients],
            "column_order":"P0..P8,K0..K7","all2058_functions_consumed":True,
            "old739_values_used_or_old_exact_norm_recomputed":False,
            "complete_fibre_factors_or_multiplicities_removed":False})
        self.checkpoint(stem+"-source-functions")
        return stem,A,coefficients

    def correspondence(self,stem,A,coefficients):
        name=stem+"-correspondence-algebra"
        old=self.old(name)
        if old is not None:
            assert old["source_functions"]==self.refs[stem+"-source-functions"]
            monic=[A.unpack(row) for row in old["monic_correspondence_coefficients"]]
            E=CorrespondenceAlgebra(A,monic)
            return E,E.unpack(old["target_w"])
        self.budget()
        p=coefficients[:9];k=coefficients[9:]
        a8_inverse,a8_proof=A.inverse(p[8],"P_leading_a8")
        monic=[A.mul(x,a8_inverse) for x in p]
        assert monic[-1]==A.one
        E=CorrespondenceAlgebra(A,monic)
        derivative=E.element([A.scale(p[i],i) for i in range(1,9)])
        derivative_inverse,derivative_proof=E.inverse(derivative,"Pprime_at_U")
        K=E.element(k)
        V=E.mul(K,derivative_inverse)
        assert E.mul(derivative,V)==K
        self.put(name,{
            "source_functions":self.refs[stem+"-source-functions"],"prime":P,
            "base_algebra_dimension":272,"correspondence_rank":8,"full_scalar_dimension":2176,
            "leading_coefficient_unit_certificate":a8_proof,
            "monic_correspondence_coefficients":[A.pack(x) for x in monic],
            "original_P_coefficients":[A.pack(x) for x in p],
            "original_K_coefficients":[A.pack(x) for x in k],
            "Pprime_at_U":E.pack(derivative),"Pprime_unit_certificate":derivative_proof,
            "target_z":"U","target_w":E.pack(V),
            "full_Pprime_times_target_w_equals_K_verified":True,
            "target_source_R873_formula_preserved":True,
            "any_source_factor_or_multiplicity_discarded":False})
        self.checkpoint(name)
        return E,V

    def powers(self,stem,E):
        name=stem+"-target-z-power-table"
        old=self.old(name)
        if old is None:
            self.budget()
            values=[];x=E.one
            for degree in range(274):
                values.append(E.flat(x))
                if degree<273:
                    x=E.mul_U(x)
            old=self.put(name,{
                "source_correspondence_algebra":self.refs[stem+"-correspondence-algebra"],
                "powers":list(range(274)),"flat_coefficient_order":"U-degree then X-degree",
                "scalar_dimension":2176,"power_table_mod_prime":values,
                "all_powers_of_original_target_U_computed_in_complete_E":True})
        assert old["source_correspondence_algebra"]==self.refs[stem+"-correspondence-algebra"]
        table=old["power_table_mod_prime"];shape(table,274,2176)
        self.checkpoint(name)
        return table

    def target_relation(self,stem,E,V,powers):
        name=stem+"-target-characteristic-relation"
        old=self.old(name)
        if old is not None:
            assert old["full_chi_U_V_equals_zero"] is True
            return
        self.budget()
        padded=[row+[0]*(274-len(row)) for row in self.chi]
        evaluated=matrix(padded)*matrix(powers)
        value=E.zero
        for k in range(273):
            ck=E.from_flat([int(evaluated[k,j]) for j in range(2176)])
            value=E.add(E.mul(value,V),ck)
        assert value==E.zero,"complete_target_characteristic_relation"
        self.put(name,{
            "source_characteristic_relation":self.inputs["characteristic_relation"],
            "source_correspondence_algebra":self.refs[stem+"-correspondence-algebra"],
            "source_target_z_power_table":self.refs[stem+"-target-z-power-table"],
            "full_scalar_dimension":2176,"full_chi_U_V_equals_zero":True,
            "all_original_coefficients_evaluated_at_target_U":True,
            "source_or_target_factor_removed":False})
        self.checkpoint(name)

    def cofactor_row(self,stem,E,V,powers):
        final_name=stem+"-evaluated-cofactor-row-index"
        final=self.old(final_name)
        if final is not None:
            return final
        # Exact C matrices, not new arithmetic: reused table prefixes avoid repeated Python coercion.
        prefixes={}
        block_specs=[]
        for first in range(0,272,16):
            stop=min(272,first+16);previous=None;value=None
            for start in range(0,272,16):
                end=min(272,start+16)
                name=f"{stem}-cofactor-{first:03d}-{stop:03d}-levels-{start:03d}-{end:03d}"
                old=self.old(name)
                if old is None:
                    self.budget()
                    if value is None:
                        assert start==0
                        value=[E.zero for _ in range(stop-first)]
                    for k in range(start,end):
                        if k+3 not in prefixes:
                            prefixes[k+3]=matrix(powers[:k+3])
                        flat=self.b_flat(k)
                        coefficients=[[flat[d*272+j] for d in range(k+3)] for j in range(first,stop)]
                        evaluated=matrix(coefficients)*prefixes[k+3]
                        for slot in range(stop-first):
                            bk=E.from_flat([int(evaluated[slot,j]) for j in range(2176)])
                            value[slot]=E.add(E.mul(value[slot],V),bk)
                    old=self.put(name,{
                        "normal_columns":[first,stop],"included_b_levels":[0,end],
                        "source_new_b_levels":self.inputs["row_levels"][start:end],
                        "source_previous_Horner_block":previous,
                        "source_target_z_power_table":self.refs[stem+"-target-z-power-table"],
                        "source_correspondence_algebra":self.refs[stem+"-correspondence-algebra"],
                        "T_Horner_uses_original_target_w":True,
                        "cofactor_values_over_E":[E.pack(x) for x in value],
                        "all_correspondence_coefficients_preserve_complete2176_algebra":True})
                else:
                    assert old["normal_columns"]==[first,stop]
                    assert old["included_b_levels"]==[0,end]
                    assert old["source_previous_Horner_block"]==previous
                    assert old["source_new_b_levels"]==self.inputs["row_levels"][start:end]
                    value=[E.unpack(x) for x in old["cofactor_values_over_E"]]
                previous=self.refs[name]
                self.checkpoint(name)
            block_specs.append({"normal_columns":[first,stop],"source":previous})
        final=self.put(final_name,{
            "source_complete_polynomial_adjugate":self.inputs["adjugate_row_index"],
            "source_correspondence_algebra":self.refs[stem+"-correspondence-algebra"],
            "blocks":block_specs,"all272_original_left_cofactors_evaluated":True,
            "all272_b_levels_used_once_per_normal_column":True,
            "target_normalization_not_yet_claimed":True})
        self.checkpoint(final_name)
        return final

    def load_evaluated_row(self,E,index,key):
        answer=[]
        for entry in index["blocks"]:
            value=read(self.out/entry["source"]["file"])
            assert spec(self.out/entry["source"]["file"])==plain(entry["source"])
            assert value["configuration"]==self.tag and value["complete"] is True
            first,stop=entry["normal_columns"]
            assert first==len(answer) and stop-first==len(value[key])
            answer.extend(E.unpack(row) for row in value[key])
        assert len(answer)==272
        return answer

    def normalize_row(self,stem,E,cofactor_index):
        final_name=stem+"-target-normal-row-index"
        old=self.old(final_name)
        if old is not None:
            return old
        r=self.load_evaluated_row(E,cofactor_index,"cofactor_values_over_E")
        name=stem+"-r0-unit"
        unit=self.old(name)
        if unit is None:
            self.budget()
            inverse,witness=E.inverse(r[0],"original_r0")
            unit=self.put(name,{
                "source_evaluated_row_index":self.refs[stem+"-evaluated-cofactor-row-index"],
                "unit_certificate":witness,"inverse_r0":E.pack(inverse),
                "original_principal271_minor_unit_on_complete_E":True})
        else:
            inverse=E.unpack(unit["inverse_r0"])
        blocks=[]
        for first in range(0,272,16):
            stop=min(272,first+16);name=f"{stem}-target-normal-{first:03d}-{stop:03d}"
            block=self.old(name)
            if block is None:
                self.budget()
                gamma=[E.mul(x,inverse) for x in r[first:stop]]
                if first==0:
                    assert gamma[0]==E.one
                block=self.put(name,{
                    "normal_columns":[first,stop],"source_r0_unit":self.refs[stem+"-r0-unit"],
                    "source_evaluated_row_index":self.refs[stem+"-evaluated-cofactor-row-index"],
                    "normal_values_over_E":[E.pack(x) for x in gamma],
                    "all_values_equal_original_rj_times_same_r0_inverse":True})
            blocks.append({"normal_columns":[first,stop],"source":self.refs[name]})
        old=self.put(final_name,{
            "source_evaluated_row_index":self.refs[stem+"-evaluated-cofactor-row-index"],
            "source_r0_unit":self.refs[stem+"-r0-unit"],"blocks":blocks,
            "all272_target_normal_coordinates_computed":True,
            "target_gamma0_equals_one":True,"full_original_system_checked_in_next_stage":True})
        self.checkpoint(final_name)
        return old

    def verify_target_row(self,stem,E,V,index):
        name=stem+"-full-target-normal-equations"
        old=self.old(name)
        if old is not None:
            assert old["all272_original_target_equations_verified"] is True
            return
        gamma=self.load_evaluated_row(E,index,"normal_values_over_E")
        assert gamma[0]==E.one
        flat=matrix([E.flat(x) for x in gamma]).transpose()
        contributions=[];products=[]
        for degree in range(4):
            subname=f"{stem}-normal-times-W-{degree}"
            product=self.old(subname)
            if product is None:
                self.budget()
                raw=rows((flat*self.Wmat[degree]).transpose())
                product=self.put(subname,{
                    "source_target_normal_row":self.refs[stem+"-target-normal-row-index"],
                    "source_original_W":self.inputs["original_W"],"W_power":degree,
                    "coefficient_order":"normal component, then U-degree, then X-degree",
                    "products_flat_mod_prime":raw,"full272_times_original_W_coefficient_block_used":True})
            raw=product["products_flat_mod_prime"];shape(raw,272,2176)
            contributions.append(raw);products.append(self.refs[subname])
        self.budget()
        for j in range(272):
            rhs=E.zero
            for degree in (3,2,1,0):
                rhs=E.add(E.mul_U(rhs),E.from_flat(contributions[degree][j]))
            assert rhs==E.mul(V,gamma[j]),("full_target_equation",j)
        self.put(name,{
            "source_target_normal_row":self.refs[stem+"-target-normal-row-index"],
            "source_original_W":self.inputs["original_W"],
            "source_correspondence_algebra":self.refs[stem+"-correspondence-algebra"],
            "source_four_coefficient_products":products,
            "all272_original_target_equations_verified":True,"target_gamma0_equals_one":True,
            "all2176_scalar_coordinates_of_each_equation_checked":True,
            "normalized_row_is_original_R876_unique271_solution":True,
            "no_factor_or_nilpotent_component_discarded":True})
        self.checkpoint(name)

    def reference_value(self,stem,E,index):
        name=stem+"-original-reference-value"
        old=self.old(name)
        if old is not None:
            return E.unpack(old["target_reference_v0"])
        self.budget()
        gamma=self.load_evaluated_row(E,index,"normal_values_over_E")
        flat=matrix([E.flat(x) for x in gamma]).transpose()
        values=[]
        for key in ("numerator_normal_polynomial_mod_prime","denominator_normal_polynomial_mod_prime"):
            raw=self.reference[key]
            products=flat*matrix(raw).transpose()
            value=E.zero
            for degree in (2,1,0):
                coefficient=E.from_flat([int(products[i,degree]) for i in range(2176)])
                value=E.add(E.mul_U(value),coefficient)
            values.append(value)
        numerator,denominator=values
        inverse,witness=E.inverse(denominator,"target_original_reference_u")
        value=E.mul(numerator,inverse)
        assert E.mul(value,denominator)==numerator
        self.put(name,{
            "source_original_reference_function":self.inputs["reference_function"],
            "source_target_normal_row":self.refs[stem+"-target-normal-row-index"],
            "source_full_original_target_equations":self.refs[stem+"-full-target-normal-equations"],
            "target_f_over_tau_squared":E.pack(numerator),
            "target_u_over_tau_squared":E.pack(denominator),
            "denominator_unit_certificate":witness,"target_reference_v0":E.pack(value),
            "full_original_target_reference_quotient_verified":True,
            "original_reference_t_frame":self.reference["original_t_frame"],
            "original_t_frame_scalar_not_replaced_by_one":True,
            "old_reference_unit_solution_or_theta_recomputed":False})
        self.checkpoint(name)
        return value

    def nine_norms(self,stem,E,x):
        name=stem+"-nine-reference-norms"
        old=self.old(name)
        if old is not None:
            return old
        self.budget()
        coefficients,proof=E.characteristic(x)
        A=E.A
        values=[]
        for t in range(9):
            value=A.zero
            for j in range(8,-1,-1):
                value=A.add(A.scale(value,(-t)%P),coefficients[j])
            values.append(value)
        assert values[0]==A.one
        old=self.put(name,{
            "source_target_reference_value":self.refs[stem+"-original-reference-value"],
            "source_correspondence_algebra":self.refs[stem+"-correspondence-algebra"],
            "full_source_algebra_dimension":272,"full_correspondence_scalar_dimension":2176,
            "one_multiplication_characteristic_polynomial":proof,
            "norm_polynomial_coefficient_order":"constant1 through t^8; coefficient_j=(-1)^j*d_j",
            "norm_polynomial_over_A":[A.pack(A.scale(coefficients[j],(-1)**j)) for j in range(9)],
            "parameters":list(range(9)),"nine_norm_values_over_entire_A":[A.pack(v) for v in values],
            "parameter_zero_norm_equals_one":True,
            "one_new_rank8_characteristic_polynomial_for_all_nine_values":True,
            "nine_separate_determinants_computed":False,
            "original_generic_frame_shared_by_all_values":True,
            "original_reference_t_frame":self.reference["original_t_frame"],
            "original_Hecke_transport":self.DAG["rigidified_Hecke_transport"],
            "direct_norm_direction":"Nm_pi_s(pi_t^*(1+t*v0))",
            "frozen_Hecke_direction_recovered_by_original_dual7":True,
            "single_geometric_point_or_reduced_quotient_used":False,
            "global_Picard_nonzero_or_principal_calibration_certified":False})
        self.checkpoint(name)
        return old

    def global_expression_program(self):
        name="original-global-reference-norm-expression-program"
        if self.old(name) is not None:
            return
        self.put(name,{
            "source_original_correspondence_DAG":self.inputs["correspondence_DAG"],
            "source_original_reference_function":self.inputs["reference_function"],
            "original_exact_reference_definition":self.reference["exact_function_definition"],
            "original_exact_correspondence_function_field":self.DAG["correspondence_function_field"],
            "original_rigidified_Hecke_transport":self.DAG["rigidified_Hecke_transport"],
            "original_reference_t_frame":self.reference["original_t_frame"],
            "exact_expression_family":{
                "parameters":list(range(9)),
                "operation":"field_norm_from_original_degree8_correspondence_to_source",
                "argument":"1+t*original_target_pullback(v0)",
                "target_pullback":"the exact source-bound original R873 target embedding",
                "coefficient_field":"the original K(Y), not a finite fibre",
                "determinant_basis":"1,U,...,U^7 in the original normalized source function field",
                "same_generic_frame_and_denominator_used_for_all_parameters":True},
            "exact_global_expressions_defined_by_existing_sources_and_R876":True,
            "characteristic_zero_norm_coefficients_expanded":False,
            "finite_modular_target_coordinates_not_substituted_for_characteristic_zero_functions":True,
            "original_t_frame_scalar_not_replaced_by_one":True,
            "global_norm_ideal_Hermite_or_actual_active_Picard_support_computed":False})

    def one_fibre(self,ordinal,z0):
        stem=f"node-{ordinal:02d}"
        success=self.old(stem+"-complete-fibre-certificate")
        if success is not None:
            assert success["source_node_value"]==z0 and success["whole_fibre_success"] is True
            return {"ordinal":ordinal,"z0":z0,"success":True,"certificate":self.refs[stem+"-complete-fibre-certificate"]}
        failure=self.old(stem+"-whole-fibre-unit-failure")
        if failure is not None:
            assert failure["source_node_value"]==z0
            return {"ordinal":ordinal,"z0":z0,"success":False,"certificate":self.refs[stem+"-whole-fibre-unit-failure"],
                    "unit_failure_label":failure["unit_failure_label"]}
        try:
            stem,A,coefficients=self.fibre_source(ordinal,z0)
            E,V=self.correspondence(stem,A,coefficients)
            powers=self.powers(stem,E)
            self.target_relation(stem,E,V,powers)
            row=self.cofactor_row(stem,E,V,powers)
            normal=self.normalize_row(stem,E,row)
            self.verify_target_row(stem,E,V,normal)
            value=self.reference_value(stem,E,normal)
            self.nine_norms(stem,E,value)
            self.put(stem+"-complete-fibre-certificate",{
                "source_node_ordinal":ordinal,"source_node_value":z0,"prime":P,
                "whole_fibre_success":True,"source_dimension":272,"correspondence_scalar_dimension":2176,
                "source_functions":self.refs[stem+"-source-functions"],
                "correspondence_algebra":self.refs[stem+"-correspondence-algebra"],
                "target_characteristic_relation":self.refs[stem+"-target-characteristic-relation"],
                "evaluated_cofactor_row":self.refs[stem+"-evaluated-cofactor-row-index"],
                "r0_unit":self.refs[stem+"-r0-unit"],
                "target_normal_row":self.refs[stem+"-target-normal-row-index"],
                "full_target_equations":self.refs[stem+"-full-target-normal-equations"],
                "original_reference_value":self.refs[stem+"-original-reference-value"],
                "nine_reference_norms":self.refs[stem+"-nine-reference-norms"],
                "all_required_units_on_entire_algebras_verified":True,
                "all272_original_target_normal_coordinates_certified":True,
                "all_nine_reference_norms_on_entire_source_fibre_computed":True,
                "factors_multiplicities_or_ramification_components_discarded":False,
                "old_producer_arithmetic_recomputed":False,
                "global_Picard_support_nonp_terms_or_height_computed":False})
            self.checkpoint(stem+"-complete")
            return {"ordinal":ordinal,"z0":z0,"success":True,"certificate":self.refs[stem+"-complete-fibre-certificate"]}
        except UnitFailure as exc:
            self.put(stem+"-whole-fibre-unit-failure",{
                "source_node_ordinal":ordinal,"source_node_value":z0,"prime":P,
                "whole_fibre_success":False,"unit_failure_label":exc.label,
                "complete_original_algebra_failure_witness":exc.witness,
                "source_characteristic_node":self.inputs["original_characteristic_nodes"][ordinal],
                "original_characteristic_zero_formula_not_refuted":True,
                "failing_factors_not_removed_and_no_partial_fibre_promoted":True})
            self.checkpoint(stem+"-honest-unit-failure")
            return {"ordinal":ordinal,"z0":z0,"success":False,
                    "certificate":self.refs[stem+"-whole-fibre-unit-failure"],"unit_failure_label":exc.label}

    def manifest(self):
        entries=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name==PREFIX+"current.json.gz" or path.name.startswith(PREFIX+"stage-manifest-"):
                continue
            value=read(path)
            assert value["result"]==RESULT and value["complete"] is True and value["configuration"]==self.tag
            entries.append(spec(path))
        current=spec(self.path("current")) if self.path("current").exists() else None
        inventory={"result":RESULT,"complete":True,"configuration":self.tag,"files":entries,
                   "current_checkpoints":[] if current is None else [current]}
        path=self.path("stage-manifest-"+fingerprint(inventory))
        if path.exists():
            assert read(path)==inventory
        else:
            save(path,inventory)
        return spec(path)

    def finish(self,complete,error):
        successful=[x for x in self.outcomes if x["success"]]
        failed=[x for x in self.outcomes if not x["success"]]
        normalized=[]
        for ordinal,z0 in enumerate(self.grid["points"]):
            path=self.path(f"node-{ordinal:02d}-full-target-normal-equations")
            if path.exists():
                value=read(path)
                assert value["configuration"]==self.tag and value["all272_original_target_equations_verified"] is True
                normalized.append({"ordinal":ordinal,"z0":z0,"certificate":spec(path)})
        if complete:
            assert len(successful)>=self.item["required_successful_fibres"]
        value={
            "result":RESULT,"complete":bool(complete),"configuration":self.tag,"p":41,"actual_auxiliary_prime":P,
            "requested_successful_fibres":self.item["required_successful_fibres"],
            "maximum_source_nodes":self.item["maximum_source_nodes"],
            "actual_tested_fibres":len(self.outcomes),"actual_successful_fibres":len(successful),
            "actual_failed_unit_fibres":len(failed),"source_node_schedule":self.grid["points"],
            "source_audit":self.refs.get("source-audit"),
            "exact_global_reference_norm_expression_program":self.refs.get("original-global-reference-norm-expression-program"),
            "fibre_outcomes":self.outcomes,"successful_fibre_certificates":successful,
            "complete_original_target_normal_coordinate_certificates":normalized,
            "actual_whole_Artin_target_normal_coordinates_certified":bool(normalized),
            "actual_nine_reference_norm_values_computed":bool(successful),
            "actual_source_dimension_for_every_accepted_fibre":272,
            "actual_correspondence_scalar_dimension_for_every_accepted_fibre":2176,
            "all_required_units_certified_on_entire_accepted_fibres":bool(successful),
            "complete_factors_and_nilpotent_multiplicities_retained":True,
            "characteristic_zero_expanded_norm_coefficients_computed":False,
            "old_W_Krylov_polynomial_adjugate_17coordinates_or_reference_solve_recomputed":False,
            "original_Hecke_active_support_principal_calibration_nonp_terms_or_height_computed":False,
            "finite_schedule_exhausted":len(self.outcomes)==self.item["maximum_source_nodes"],
            "stage_manifest":self.manifest(),"resume_state":self.current,
            "failure_or_stop_reason":error,"seconds":time.monotonic()-self.started}
        save(self.out/FINAL,value)
        return value

    def run(self):
        self.global_expression_program()
        for ordinal,z0 in enumerate(self.grid["points"][:self.item["maximum_source_nodes"]]):
            self.budget()
            outcome=self.one_fibre(ordinal,z0)
            self.outcomes.append(outcome)
            self.checkpoint("fibre-outcome-committed")
            if sum(bool(x["success"]) for x in self.outcomes)>=self.item["required_successful_fibres"]:
                return self.finish(True,None)
        return self.finish(False,"The finite original-node schedule did not provide the requested number of whole unit fibres.")

def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise SystemExit("New R885 complete-Artin arithmetic only runs in authorized public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    for name in ("config","retained","output"):
        parser.add_argument("--"+name,required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args();assert 0<args.budget_minutes<=300
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    job=None;code=1;error=None;started=time.monotonic()
    try:
        job=Job(args);certificate=job.run()
        code=0 if certificate["complete"] else 2
    except BudgetStop as exc:
        code=124;error=str(exc)
    except Exception as exc:
        error=type(exc).__name__+": "+str(exc);traceback.print_exc()
    if code in (1,124) and job is not None:
        job.finish(False,error)
    receipt={"result":RESULT,"source_sha256":sha(__file__),"helper_sha256":sha(algebra.__file__),
             "complete":code==0,"process_exit_code":code,"error":error,"seconds":time.monotonic()-started,
             "configuration":None if job is None else job.tag,
             "certificate_sha256":sha(out/FINAL) if (out/FINAL).exists() else None,
             "new_arithmetic_only_in_public_Actions":True}
    save(out/"core-receipt.json",receipt)
    log_receipt={key:value for key,value in receipt.items() if key!="configuration"}
    log_receipt["configuration_sha256"]=None if job is None else fingerprint(job.tag)
    print("R885_ARTIN_CORE_RECEIPT="+json.dumps(log_receipt,sort_keys=True),flush=True)
    raise SystemExit(code)
if __name__=="__main__":
    main()
