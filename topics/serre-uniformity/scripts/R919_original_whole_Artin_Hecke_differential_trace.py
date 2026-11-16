#!/usr/bin/env python3
"""R919: new original derivative/Euler values on the completed whole Artin fibre."""
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
from flint import nmod_mat
import R885_whole_Artin_algebra as algebra
from R885_whole_Artin_algebra import SourceAlgebra, CorrespondenceAlgebra

REPOSITORY="Rogerhu12/math-research-public"
RESULT="R919-original-whole-Artin-Hecke-differential-trace"
FINAL="p41-original-whole-Artin-Hecke-differential-trace-certificate.json"
PREFIX="R919-"
MANIFEST="full-outputs-manifest.json"
P=1000000753
EPS=[0]+[1]*144+[2]*127
GROUPS=("R885","R827","R882","R873","R807")
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
STRATEGY={
    "original_curve":"original genus127 Y, level82, original minus3 descent",
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "source_node_ordinal":0,"source_z":0,
    "source_algebra":"entire original Fp[X]/chi_0(X), dimension272",
    "correspondence":"entire A0[U]/(P(U)/a8), rank8",
    "derivation":"delta=g*d/dz on the original function field, evaluated only after original-leaf differentiation",
    "M2_leaves":"1,z-beta72,beta1,...,beta144 with original82 scales retained once",
    "derivative_basis_block_size":64,"target_normal_block_size":16,
    "new_coefficient_columns":"delta(P0),...,delta(P8), nine columns only",
    "Euler_row":"L(h)=-a8^-1*[U^7](h*deltaP mod (P/a8))",
    "row_domain_basis":"1,U,...,U^7 over the entire A0",
    "input_differential_frame":"dz_target","output_differential_frame":"original nu_source=dz_source/g_source",
    "exact_check":"all8 basis values equal -Tr_E/A0(h*deltaP/Pprime), using the completed original inverse",
    "target_application":"all272 completed original target normal coordinates",
    "old_theta_a8_Pprime_Krylov_inverses_recomputed":False,
    "old2058_values_17coordinates_adjugate_or_correspondence_recomputed":False,
    "delta_claimed_to_descend_to_source_fibre":False,
    "source_factors_nilpotents_or_multiplicities_discarded":False,
    "finite_values_claimed_char0_expanded_or_global_calibration":False,
    "budget_excluded_from_identity":True}

class BudgetStop(RuntimeError):
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
    return {"result":RESULT,"source_sha256":item["core_sha256"],"helper_sha256":item["helper_sha256"],
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
        assert item["stage_result_location"]==("configuration" if group in ("R807","R827") else "top_level")

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

class Job:
    def __init__(self,args):
        self.args=args;self.started=time.monotonic();self.out=Path(args.output)
        self.out.mkdir(parents=True,exist_ok=True);self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41 and self.item["producer_inputs_pending"] is False
        assert sha(__file__)==self.item["core_sha256"] and flint.__version__=="0.9.0"
        assert Path(algebra.__file__).name==self.item["helper"] and sha(algebra.__file__)==self.item["helper_sha256"]
        topic=Path(__file__).resolve().parent.parent
        assert sha(topic/self.item["method"])==self.item["method_sha256"]
        for row in self.item["proofs"].values():assert sha(topic/row["path"])==row["sha256"]
        assert set(self.item["sources"])==set(GROUPS)
        self.sources={g:Source(g,self.item["sources"][g],args.retained) for g in GROUPS}
        self.tag=expected_tag(self.item);self.refs={};self.current=None
        self.inputs=self.item["inputs"]
        for key in ("fibre_certificate","source_functions","correspondence_algebra","target_normal_index",
                    "full_target_equations","original_W","original_place","original_Krylov","original_Gamma",
                    "operator_identity","seventeen_coordinates","same_place_interface","correspondence_DAG",
                    "theta","E6_clearing"):
            setattr(self,key,self.input(key))
        self.validate_sources()
        self.A=SourceAlgebra(self.source_functions["complete_source_algebra_modulus"])
        self.E=CorrespondenceAlgebra(self.A,[self.A.unpack(x) for x in self.correspondence_algebra["monic_correspondence_coefficients"]])
        self.e=[self.A.unpack(v) for v in self.source_functions["original_M2_functions_over_A"]]
        self.oldvalues=self.source_functions["original2058_basis_function_values_over_A"]
        self.old_E6=self.A.unpack(self.source_functions["E6hat_over_tau3"])
        self.theta_inverse=self.A.unpack(self.source_functions["theta_unit_certificate"]["inverse"])
        self.a8_inverse=self.A.unpack(self.correspondence_algebra["leading_coefficient_unit_certificate"]["inverse"])
        self.Pprime_inverse=self.E.unpack(self.correspondence_algebra["Pprime_unit_certificate"]["inverse"])
        self.source_audit()

    def input(self,key):
        row=self.inputs[key];return self.sources[row["source_group"]].stage(row)

    def stage_ref(self,row):
        return self.sources[row["source_group"]].stage(row)

    def validate_sources(self):
        s=self.source_functions;c=self.correspondence_algebra;f=self.fibre_certificate
        assert s["source_node_ordinal"]==0 and s["source_node_value"]==0
        assert s["prime"]==P and s["source_algebra_dimension"]==272
        assert s["all2058_functions_consumed"] is True and s["original82_scales_retained_once"] is True
        assert s["new_scale_applied"]=="1" and s["column_order"]=="P0..P8,K0..K7"
        assert s["complete_fibre_factors_or_multiplicities_removed"] is False
        shape(s["original_M2_functions_over_A"],146,272)
        shape(s["original2058_basis_function_values_over_A"],2058,272)
        shape(s["seventeen_values_over_A"],17,272)
        for field,key in (("source_DAG","correspondence_DAG"),("source_seventeen_coordinates","seventeen_coordinates"),
                          ("source_theta","theta"),("source_E6_clearing","E6_clearing"),
                          ("source_original_Krylov","original_Krylov")):
            assert plain(s[field])==plain(self.inputs[key])
        assert f["whole_fibre_success"] is True and f["all_required_units_on_entire_algebras_verified"] is True
        assert f["all272_original_target_normal_coordinates_certified"] is True
        for field,key in (("source_functions","source_functions"),("correspondence_algebra","correspondence_algebra"),
                          ("target_normal_row","target_normal_index"),("full_target_equations","full_target_equations")):
            assert plain(f[field])==plain(self.inputs[key])
        assert plain(c["source_functions"])==plain(self.inputs["source_functions"])
        assert c["base_algebra_dimension"]==272 and c["correspondence_rank"]==8 and c["full_scalar_dimension"]==2176
        assert c["original_P_coefficients"]==s["seventeen_values_over_A"][:9]
        assert c["original_K_coefficients"]==s["seventeen_values_over_A"][9:]
        for proof in (s["theta_unit_certificate"],c["leading_coefficient_unit_certificate"],c["Pprime_unit_certificate"]):
            assert proof["whole_fibre_unit"] is True
        assert c["full_Pprime_times_target_w_equals_K_verified"] is True
        assert c["any_source_factor_or_multiplicity_discarded"] is False
        idx=self.target_normal_index
        assert idx["all272_target_normal_coordinates_computed"] is True and idx["target_gamma0_equals_one"] is True
        assert len(idx["blocks"])==len(self.inputs["target_normal_blocks"])==17
        for ordinal,(part,ref) in enumerate(zip(idx["blocks"],self.inputs["target_normal_blocks"])):
            assert part["normal_columns"]==[16*ordinal,min(16*ordinal+16,272)]
            assert plain(part["source"])==plain(ref)
        assert self.full_target_equations["all272_original_target_equations_verified"] is True
        assert self.full_target_equations["all2176_scalar_coordinates_of_each_equation_checked"] is True
        assert self.full_target_equations["no_factor_or_nilpotent_component_discarded"] is True
        place=self.original_place
        assert place["prime"]==P and place["original_zeta_root"]==549966761 and place["original_s_root"]==99932770
        assert place["original_integral_B_root"]==3197390 and place["original_branch"]==0
        assert self.original_W["prime"]==P and self.original_W["original_rational_denominators_all_units"] is True
        assert self.original_W["original_W_e0_equals_e1_verified"] is True
        shape(self.original_W["g_vector_coefficients_mod_prime"],4,272)
        point=self.original_Krylov
        assert point["prime"]==P and point["z0"]==0
        assert plain(point["source_original_W"])==plain(self.inputs["original_W"])
        shape(point["inverse_Krylov_matrix_mod_prime"],272,272)
        gamma=self.original_Gamma
        assert gamma["prime"]==P and gamma["target"]=="Gamma" and gamma["chart"]=="tau"
        assert gamma["normal_basis_degrees"]==EPS and gamma["regular_degree_bound"]==2
        assert gamma["original_true_operator_reduction_certified"] is True and gamma["all_weighted_support_zeros_verified"] is True
        assert len(gamma["row_blocks"])==len(self.inputs["Gamma_blocks"])==17
        assert all(plain(a)==plain(b) for a,b in zip(gamma["row_blocks"],self.inputs["Gamma_blocks"]))
        oi=self.operator_identity
        assert oi["all_operators_are_true_original_p_integral_reductions"] is True
        assert oi["Gamma_nested_full_polynomial_identity_certified_by_seven_points"] is True
        assert oi["Gamma_first_column_zero_and_second_column_original_vh"] is True
        assert oi["all_sigma_negative_powers_and_original_minus_sign_verified"] is True
        assert plain(oi["operator_indexes"]["Gamma"]["tau"])==plain(self.inputs["original_Gamma"])
        assert self.seventeen_coordinates["prime"]==P
        assert self.seventeen_coordinates["same_characteristic_zero_coefficients_integral_at_new_place"] is True
        shape(self.seventeen_coordinates["coordinate_matrix_mod_prime"],2058,17)
        assert plain(self.seventeen_coordinates["source_exact_R873_unit_solve"])==plain(self.correspondence_DAG["coefficient_unit_solve"])
        assert self.same_place_interface["all2200_by17_original_equations_verified"] is True
        assert self.same_place_interface["prime"]==P and self.same_place_interface["original_zeta_root"]==549966761
        assert plain(self.same_place_interface["new_modular_coordinates"])==plain(self.inputs["seventeen_coordinates"])
        assert plain(self.same_place_interface["source_R873_correspondence_DAG"])==plain(self.inputs["correspondence_DAG"])
        dag=self.correspondence_DAG
        assert dag["exact_original_correspondence_expression_certified"] is True
        assert dag["rigidified_Hecke_transport"]["frozen_direction"]=="Nm_pi_t(pi_s^*I)"
        assert len(dag["old_V8_over_tau8"])==2050 and len(dag["new_eight_complement_functions"])==8
        for k,row in enumerate(dag["old_V8_over_tau8"]):
            assert row["index"]==k and len(row["original_M2_leaf_indices"])==8
        for k,row in enumerate(dag["new_eight_complement_functions"]):
            assert row["index"]==2050+k and len(row["original_M2_leaf_indices"])==2
        assert dag["new_eight_complement_functions"][0]["original_M2_leaf_indices"]==[0,0]
        assert dag["P_over_tau8_coefficients"]=={"powers_U":list(range(9)),"unit_solve_columns":list(range(9))}
        theta=self.theta;clear=self.E6_clearing
        assert theta["original_M2_integer_scale"]=="6724" and theta["theta_nonzero_by_original_independent_M2_input"] is True
        assert plain(theta["M6_index692_cleared_coordinate_stage"])==plain(self.inputs["E6_clearing"])
        assert clear["M6_index"]==692 and clear["basis_dimension"]==962 and len(clear["solution_numerators"])==962
        assert clear["all1100_rows_verified"] is True and clear["exact_global_V4_membership_certified"] is True
        assert clear["basis_integer_scale"]=="2044140858654976"
        assert str(clear["solution_common_denominator"])==s["completed_N692_common_denominator"]
        ed=dag["E6hat_over_tau3"]
        assert plain(ed["theta_source"])==plain(self.inputs["theta"])
        assert plain(ed["V4_coordinate_source"])==plain(self.inputs["E6_clearing"]) and ed["new_scale_applied"]=="1"
        for group in ("R827","R882","R873","R807"):
            same_source(self.sources["R885"].tag["sources"][group],identity(self.item["sources"][group]))
        same_source(self.sources["R882"].tag["sources"]["R873"],identity(self.item["sources"]["R873"]))
        same_source(self.sources["R873"].tag["sources"]["R807"],identity(self.item["sources"]["R807"]))

    def budget(self):
        if time.monotonic()-self.started>=60*self.args.budget_minutes:
            raise BudgetStop("R919 budget: every complete derivative/trace block remains reusable.")

    def path(self,name):
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
             "phase":phase,"completed_stages":self.refs})
        self.current=spec(self.path("current"))

    def source_audit(self):
        if self.old("source-audit") is None:
            self.put("source-audit",{
                "sources":{g:identity(self.item["sources"][g]) for g in GROUPS},"inputs":self.inputs,
                "original_source_z":0,"prime":P,"source_algebra_dimension":272,"correspondence_scalar_dimension":2176,
                "original_82_scales_retained_once":True,"old_complete_p753_source_identities_verified":True,
                "all_source_arrays_are_actual_completed_outputs":True,
                "historical_R807_R827_result_in_configuration_preserved":True,
                "old_Gamma_values_Krylov_theta_a8_Pprime_and_normal_coordinates_not_recomputed":True})
        self.checkpoint("sources")

    def monomial_engine(self,derivatives):
        A=self.A;e=self.e
        value_cache={():A.one};derivative_cache={():A.zero}
        def key(indices):
            q=tuple(sorted(indices));assert all(isinstance(i,int) and 0<=i<146 for i in q);return q
        def value(indices):
            q=key(indices)
            if q not in value_cache:value_cache[q]=A.mul(value(q[:-1]),e[q[-1]])
            return value_cache[q]
        def derivative(indices):
            q=key(indices)
            if q not in derivative_cache:
                derivative_cache[q]=A.add(A.mul(derivative(q[:-1]),e[q[-1]]),
                                          A.mul(value(q[:-1]),derivatives[q[-1]]))
            return derivative_cache[q]
        return value,derivative

    def leaf_derivatives(self):
        name="original-leaf-derivative-values";old=self.old(name)
        if old is not None:
            assert old["source_Gamma_index"]==self.inputs["original_Gamma"]
            return [self.A.unpack(x) for x in old["delta_original_M2_values_over_A"]],self.A.unpack(old["delta_E6hat_square_over_tau6"])
        self.budget();A=self.A
        normal=[[0]*146 for _ in range(272)]
        refs=[];nextrow=0
        for ref in self.inputs["Gamma_blocks"]:
            self.budget();block=self.stage_ref(ref)
            first,stop=block["row_first"],block["row_stop"]
            assert first==nextrow and stop==min(first+16,272)
            assert block["target"]=="Gamma" and block["chart"]=="tau" and block["prime"]==P
            assert block["original_weighted_support_verified"] is True
            assert block["true_p_integral_operator_reduction_by_unit_nodes_and_original_degree_bound"] is True
            coeffs=block["coefficient_matrices_low_to_high"];assert len(coeffs)==5
            for part in coeffs:shape(part,stop-first,272)
            for k in range(stop-first):
                assert coeffs[0][k][0]==0
                normal[first+k][0]=self.original_W["g_vector_coefficients_mod_prime"][0][first+k]
                normal[first+k][1:]=coeffs[0][k][:145]
            refs.append(ref);nextrow=stop
        assert nextrow==272
        # One new evaluation of the completed derivative coefficients in the old cyclic basis.
        image=matrix(self.original_Krylov["inverse_Krylov_matrix_mod_prime"])*matrix(normal)
        g=A.element([int(image[i,0]) for i in range(272)])
        db=[A.element([int(image[i,j+1]) for i in range(272)]) for j in range(145)]
        assert db[0]==A.zero
        de=[A.zero,A.sub(g,db[72])]+db[1:145]
        assert len(de)==146
        theta_d=A.zero
        for d,c in zip(de,self.theta["theta_in_original_integer_scaled_M2_basis"]):
            theta_d=A.add(theta_d,A.mul(d,A.fraction(c[0],c[1])))
        value,derivative=self.monomial_engine(de)
        den=int(self.E6_clearing["solution_common_denominator"])
        den_inverse=pow(den%P,-1,P);dn=A.zero;used=[]
        for row in self.correspondence_DAG["E6hat_over_tau3"]["nonzero_V4_monomials"]:
            self.budget();i=row["source_coordinate_index"]
            assert row["original_V4_index"]==i and 0<=i<962
            assert len(row["original_M2_leaf_indices"])==4
            c=int(self.E6_clearing["solution_numerators"][i])*den_inverse%P
            dn=A.add(dn,A.scale(derivative(row["original_M2_leaf_indices"]),c));used.append(i)
        assert used==[i for i,x in enumerate(self.E6_clearing["solution_numerators"]) if int(x)]
        dE=A.mul(self.theta_inverse,A.sub(dn,A.mul(self.old_E6,theta_d)))
        dE2=A.scale(A.mul(self.old_E6,dE),2)
        self.put(name,{
            "source_Gamma_index":self.inputs["original_Gamma"],"source_Gamma_blocks":refs,
            "source_original_Krylov":self.inputs["original_Krylov"],"source_original_g_vector":self.inputs["original_W"],
            "source_original_values":self.inputs["source_functions"],"source_theta":self.inputs["theta"],
            "source_E6_clearing":self.inputs["E6_clearing"],"source_DAG":self.inputs["correspondence_DAG"],
            "prime":P,"source_z":0,"delta_original_M2_values_over_A":[A.pack(x) for x in de],
            "delta_z_value_over_A":A.pack(g),"delta_theta_over_tau":A.pack(theta_d),
            "delta_N692_over_tau4":A.pack(dn),"delta_E6hat_over_tau3":A.pack(dE),
            "delta_E6hat_square_over_tau6":A.pack(dE2),
            "old_E6hat_square_value_reused_from_basis_index":2050,
            "quotient_rule":"delta(E)=theta_inverse*(delta(N)-old_E*delta(theta))",
            "complete_original_Gamma_all17_blocks_used":True,"original_M2_leaves_82_scale_unchanged":True,
            "derivation_applied_before_fibre_reduction":True,"delta_claimed_to_descend_to_A0":False,
            "old_source_values_or_inverse_recomputed":False})
        self.checkpoint(name);return de,dE2

    def basis_derivatives(self,de,dE2):
        A=self.A;value,derivative=self.monomial_engine(de);blocks=[]
        E2=A.unpack(self.oldvalues[2050])
        for first in range(0,2058,64):
            stop=min(first+64,2058);name=f"basis-derivatives-{first:04d}-{stop:04d}";old=self.old(name)
            if old is None:
                self.budget();computed=[]
                for i in range(first,stop):
                    self.budget()
                    if i<2050:
                        r=self.correspondence_DAG["old_V8_over_tau8"][i]
                        out=derivative(r["original_M2_leaf_indices"])
                    else:
                        r=self.correspondence_DAG["new_eight_complement_functions"][i-2050]
                        m=r["original_M2_leaf_indices"]
                        out=A.add(A.mul(dE2,value(m)),A.mul(E2,derivative(m)))
                    computed.append(A.pack(out))
                old=self.put(name,{
                    "first":first,"stop":stop,"source_original_DAG":self.inputs["correspondence_DAG"],
                    "source_original_values":self.inputs["source_functions"],
                    "source_new_leaf_derivatives":self.refs["original-leaf-derivative-values"],
                    "delta_basis_values_over_A":computed,
                    "original_completed_value_slice_sha256":fingerprint(self.oldvalues[first:stop]),
                    "product_and_quotient_rules_include_all_original_factors":True,
                    "old_complete_V8_values_recomputed":False,"old_input_scales_changed":False})
            assert old["first"]==first and old["stop"]==stop
            assert old["source_new_leaf_derivatives"]==self.refs["original-leaf-derivative-values"]
            shape(old["delta_basis_values_over_A"],stop-first,272)
            blocks.append({"first":first,"stop":stop,"source":self.refs[name]})
            self.checkpoint(name)
        if self.old("basis-derivative-index") is None:
            self.put("basis-derivative-index",{"basis_dimension":2058,"blocks":blocks,
                "all2058_original_basis_derivatives_evaluated":True,
                "source_original_DAG":self.inputs["correspondence_DAG"]})
        else:assert read(self.path("basis-derivative-index"))["blocks"]==blocks
        return blocks

    def delta_coefficients(self,blocks):
        name="nine-original-delta-P-coefficients";old=self.old(name)
        if old is None:
            self.budget();raw=[]
            for b in blocks:
                self.budget();x=read(self.out/b["source"]["file"])
                assert spec(self.out/b["source"]["file"])==b["source"] and x["configuration"]==self.tag
                raw.extend(x["delta_basis_values_over_A"])
            shape(raw,2058,272)
            c=[row[:9] for row in self.seventeen_coordinates["coordinate_matrix_mod_prime"]]
            image=matrix(raw).transpose()*matrix(c)
            values=[[int(image[i,j]) for i in range(272)] for j in range(9)]
            old=self.put(name,{
                "source_basis_derivatives":self.refs["basis-derivative-index"],
                "source_original_seventeen_coordinates":self.inputs["seventeen_coordinates"],
                "source_original_same_place_certificate":self.inputs["same_place_interface"],
                "coefficient_indices":list(range(9)),"delta_P_coefficients_over_A":values,
                "derivative_of_original_unit_solve_constants_is_zero":True,
                "all2058_rows_and_nine_original_P_columns_consumed":True,
                "delta_K_or_new_coefficient_solve_computed":False})
        assert old["source_basis_derivatives"]==self.refs["basis-derivative-index"]
        shape(old["delta_P_coefficients_over_A"],9,272);self.checkpoint(name)
        return [self.A.unpack(x) for x in old["delta_P_coefficients_over_A"]]

    def euler_row(self,deltaP):
        name="complete-Euler-row";old=self.old(name);A=self.A;E=self.E
        if old is None:
            self.budget();q=E.zero
            for c in reversed(deltaP):q=E.add(E.mul_U(q),E.constant(c))
            shifted=q;values=[];remainders=[]
            for j in range(8):
                self.budget();remainders.append(E.pack(shifted))
                values.append(A.pack(A.neg(A.mul(self.a8_inverse,shifted[7]))))
                if j<7:shifted=E.mul_U(shifted)
            old=self.put(name,{
                "source_original_correspondence":self.inputs["correspondence_algebra"],
                "source_nine_delta_P_coefficients":self.refs["nine-original-delta-P-coefficients"],
                "row_domain_basis_U_powers":list(range(8)),"linear_functional_coefficients_over_A":values,
                "deltaP_reduced_in_E":E.pack(q),"U_power_deltaP_remainders_over_E":remainders,
                "coefficient_formula":"minus old_a8_inverse times U^7 coefficient",
                "input_frame":"dz_target","output_frame":"nu_source",
                "complete_rank8_and_all272_source_coordinates_preserved":True,
                "a8_inverse_reused_from_original_complete_certificate":True})
        shape(old["linear_functional_coefficients_over_A"],8,272)
        assert old["source_nine_delta_P_coefficients"]==self.refs["nine-original-delta-P-coefficients"]
        self.checkpoint(name)
        return [A.unpack(x) for x in old["linear_functional_coefficients_over_A"]],E.unpack(old["deltaP_reduced_in_E"])

    def verify_eight_basis(self,functional,deltaP):
        A=self.A;E=self.E
        complete=self.old("complete-eight-basis-trace-identity")
        if complete is not None:
            assert complete["source_Euler_row"]==self.refs["complete-Euler-row"]
            assert complete["all8_basis_identities_in_entire_A0_verified"] is True
            return
        checks=[];seed=None
        for j in range(8):
            name=f"trace-identity-U-{j:02d}";old=self.old(name)
            if old is None:
                self.budget()
                if j==0:seed=E.neg(E.mul(deltaP,self.Pprime_inverse))
                else:
                    previous=read(self.path(f"trace-identity-U-{j-1:02d}"))
                    assert previous["configuration"]==self.tag
                    seed=E.unpack(previous["next_negative_h_deltaP_over_Pprime_in_E"])
                col=seed;diagonal=[]
                for k in range(8):
                    self.budget();diagonal.append(col[k])
                    if k<7:col=E.mul_U(col)
                tr=A.zero
                for d in diagonal:tr=A.add(tr,d)
                assert tr==functional[j]
                old=self.put(name,{
                    "basis_U_power":j,"source_Euler_row":self.refs["complete-Euler-row"],
                    "source_original_Pprime_inverse":self.inputs["correspondence_algebra"],
                    "negative_h_deltaP_over_Pprime_in_E":E.pack(seed),
                    "next_negative_h_deltaP_over_Pprime_in_E":E.pack(E.mul_U(seed)) if j<7 else None,
                    "multiplication_matrix_diagonal_over_A":[A.pack(x) for x in diagonal],
                    "actual_trace_over_A":A.pack(tr),"coefficient_functional_over_A":A.pack(functional[j]),
                    "complete_all272_coordinate_equality_verified":True,"new_inverse_computed":False})
            assert old["basis_U_power"]==j and old["source_Euler_row"]==self.refs["complete-Euler-row"]
            assert old["complete_all272_coordinate_equality_verified"] is True
            checks.append(self.refs[name]);self.checkpoint(name)
        self.put("complete-eight-basis-trace-identity",{
            "source_Euler_row":self.refs["complete-Euler-row"],"basis_certificates":checks,
            "source_algebra_dimension":272,"rank_over_source":8,
            "all8_basis_identities_in_entire_A0_verified":True,
            "all_source_nilpotent_multiplicities_retained":True,"new_inverse_computed":False})
        self.checkpoint("complete-eight-basis-trace-identity")

    def apply_target_normal(self,functional):
        A=self.A;blocks=[]
        for source in self.inputs["target_normal_blocks"]:
            old_source=self.stage_ref(source);first,stop=old_source["normal_columns"]
            name=f"target-normal-differential-traces-{first:03d}-{stop:03d}";old=self.old(name)
            if old is None:
                self.budget();values=old_source["normal_values_over_E"]
                assert len(values)==stop-first
                computed=[]
                for raw in values:
                    self.budget();shape(raw,8,272);x=A.zero
                    for coefficient,value in zip(functional,raw):x=A.add(x,A.mul(coefficient,A.unpack(value)))
                    computed.append(A.pack(x))
                old=self.put(name,{
                    "normal_columns":[first,stop],"source_original_target_normal_block":source,
                    "source_Euler_row":self.refs["complete-Euler-row"],
                    "source_full_rank8_trace_certificate":self.refs["complete-eight-basis-trace-identity"],
                    "Tr_beta_target_dz_target_over_nu_source":computed,
                    "full_eight_coefficients_and_entire_source_algebra_used":True,
                    "original_target_coordinates_recomputed":False,
                    "characteristic_zero_coordinates_expanded":False})
            assert old["source_original_target_normal_block"]==source
            shape(old["Tr_beta_target_dz_target_over_nu_source"],stop-first,272)
            blocks.append({"normal_columns":[first,stop],"source":self.refs[name]});self.checkpoint(name)
        assert [b["normal_columns"] for b in blocks]==[[i,min(i+16,272)] for i in range(0,272,16)]
        if self.old("all272-target-normal-differential-traces") is None:
            self.put("all272-target-normal-differential-traces",{
                "blocks":blocks,"source_original_target_normal_index":self.inputs["target_normal_index"],
                "source_original_full_target_equations":self.inputs["full_target_equations"],
                "source_Euler_row":self.refs["complete-Euler-row"],
                "all272_original_target_normal_differentials_evaluated":True,
                "complete_source_coordinate_count":272,"input_frame":"dz_target","output_frame":"nu_source",
                "connection_numerators_evaluated":False,"original_endpoint_calibration_computed":False})
        else:assert read(self.path("all272-target-normal-differential-traces"))["blocks"]==blocks
        self.checkpoint("all272-target-normal-differential-traces")

    def exact_expression(self):
        name="original-characteristic-zero-differential-expression-DAG"
        if self.old(name) is not None:return
        d=self.correspondence_DAG
        self.put(name,{
            "source_original_correspondence_DAG":self.inputs["correspondence_DAG"],
            "original_coefficient_unit_solve":d["coefficient_unit_solve"],
            "source_R915_proof":self.item["proofs"]["R915"],
            "original_function_field":d["correspondence_function_field"],
            "derivation":{"operation":"apply_original_rational_derivation_before_any_specialization",
                "symbol":"delta","definition":"nu^-1 d = g d/dz",
                "original_monomial_and_quotient_leaves":self.inputs["correspondence_DAG"],
                "constant_field_derivative":0,
                "finite_Gamma_expansion_is_only_a_reduction":self.inputs["original_Gamma"]},
            "nine_derivative_nodes":[{"operation":"original_derivation",
                "input":{"operation":"original_2058_basis_linear_combination",
                    "basis_source":self.inputs["correspondence_DAG"],
                    "exact_unit_solve":d["coefficient_unit_solve"],"unit_solve_column":i,"U_power":i}}
                for i in range(9)],
            "Euler_functional":{"operation":"minus_multiply_coefficient_of_monic_remainder",
                "scalar":"a8^-1","coefficient_U_power":7,"input":"h*delta(P)",
                "monic_modulus":"P/a8","source_original_leading_coefficient":{"source":self.inputs["correspondence_DAG"],"index":8},
                "source_original_Pprime_identity":"R915 Euler identity over the original rank8 function field"},
            "original_rigidified_Hecke_transport":d["rigidified_Hecke_transport"],
            "original_cY":d["original_cY"],
            "differential_transport":{"source_frame":"nu_s=dz_s/g_s","target_frame":"dz_t",
                "canonical_dual7_transports_both_determinant_frames":True,
                "scalar7_diamond_minus3_descent_retained":True,
                "kappa_nu_endpoint_constants_replaced":False},
            "exact_characteristic_zero_expression_defined":True,
            "characteristic_zero_derivative_or_Hecke_coordinates_expanded":False,
            "original_Gamma_characteristic_zero_expanded":False,
            "finite_fibre_values_substituted_for_global_functions":False,
            "original_connections_evaluated_or_calibrated":False,
            "nonp_terms_Poincare_period_or_height_computed":False})
        self.checkpoint(name)

    def manifest(self):
        entries=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name==PREFIX+"current.json.gz" or path.name.startswith(PREFIX+"stage-manifest-"):continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
            entries.append(spec(path))
        current=spec(self.path("current")) if self.path("current").exists() else None
        value={"result":RESULT,"complete":True,"configuration":self.tag,"files":entries,
               "current_checkpoints":[] if current is None else [current]}
        target=self.path("stage-manifest-"+fingerprint(value))
        if target.exists():assert read(target)==value
        else:save(target,value)
        return spec(target)

    def finish(self,complete,error):
        wanted=("source-audit","original-leaf-derivative-values","basis-derivative-index",
                "nine-original-delta-P-coefficients","complete-Euler-row","complete-eight-basis-trace-identity",
                "all272-target-normal-differential-traces","original-characteristic-zero-differential-expression-DAG")
        if complete:
            for name in wanted:assert self.old(name) is not None
        value={"result":RESULT,"complete":bool(complete),"configuration":self.tag,"p":41,
            "actual_auxiliary_prime":P,"original_source_node":0,"source_algebra_dimension":272,
            "correspondence_rank":8,"correspondence_scalar_dimension":2176,
            "source_audit":self.refs.get("source-audit"),
            "source_leaf_derivatives":self.refs.get("original-leaf-derivative-values"),
            "basis_derivative_index":self.refs.get("basis-derivative-index"),
            "nine_delta_P_coefficients":self.refs.get("nine-original-delta-P-coefficients"),
            "Euler_trace_row":self.refs.get("complete-Euler-row"),
            "full_eight_basis_identity":self.refs.get("complete-eight-basis-trace-identity"),
            "all272_target_normal_trace_table":self.refs.get("all272-target-normal-differential-traces"),
            "exact_characteristic_zero_expression_DAG":self.refs.get("original-characteristic-zero-differential-expression-DAG"),
            "actual_nine_original_delta_P_values_certified":bool(complete),
            "actual_complete_A0_linear_Euler_row_certified":bool(complete),
            "actual_all8_trace_basis_identities_verified":bool(complete),
            "actual_all272_target_normal_differential_traces_computed":bool(complete),
            "whole_source_factors_and_nilpotents_retained":True,
            "actual_characteristic_zero_derivative_coordinates_expanded":False,
            "actual_original_Gamma_characteristic_zero_expanded":False,
            "seven_connection_numerator_evaluations_computed":False,
            "original_Hecke_projector_or_endpoint_calibration_computed":False,
            "nonp_terms_Poincare_period_or_height_computed":False,
            "old_source_arithmetic_recomputed":False,
            "stage_manifest":self.manifest(),"resume_state":self.current,
            "failure_or_stop_reason":error,"seconds":time.monotonic()-self.started}
        save(self.out/FINAL,value);return value

    def run(self):
        self.exact_expression()
        de,dE2=self.leaf_derivatives()
        blocks=self.basis_derivatives(de,dE2)
        deltaP=self.delta_coefficients(blocks)
        functional,reduced=self.euler_row(deltaP)
        self.verify_eight_basis(functional,reduced)
        self.apply_target_normal(functional)
        return self.finish(True,None)

def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise SystemExit("R919 new arithmetic runs only in the authorized public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    for name in ("config","retained","output"):parser.add_argument("--"+name,required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args();assert 0<args.budget_minutes<=300
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    job=None;code=1;error=None;started=time.monotonic()
    try:
        job=Job(args);certificate=job.run();code=0 if certificate["complete"] else 2
    except BudgetStop as exc:code=124;error=str(exc)
    except Exception as exc:error=type(exc).__name__+": "+str(exc);traceback.print_exc()
    if code in (1,124) and job is not None:job.finish(False,error)
    receipt={"result":RESULT,"source_sha256":sha(__file__),"helper_sha256":sha(algebra.__file__),
        "complete":code==0,"process_exit_code":code,"error":error,"seconds":time.monotonic()-started,
        "configuration":None if job is None else job.tag,
        "certificate_sha256":sha(out/FINAL) if (out/FINAL).exists() else None,
        "new_arithmetic_only_in_public_Actions":True}
    save(out/"core-receipt.json",receipt)
    log={k:v for k,v in receipt.items() if k!="configuration"}
    log["configuration_sha256"]=None if job is None else fingerprint(job.tag)
    print("R919_CORE_RECEIPT="+json.dumps(log,sort_keys=True),flush=True)
    raise SystemExit(code)
if __name__=="__main__":main()

