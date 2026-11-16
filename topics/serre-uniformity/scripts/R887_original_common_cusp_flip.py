#!/usr/bin/env python3
"""R887: common cusp flip and complete bounded representative.
Only public Actions execute the new finite-field operations. Original exact
objects remain source-bound unit-solve expressions, not reconstructed arrays.
"""
import argparse
import gc
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
import traceback
import hashlib

LEGACY_CORE="R880_original_D_and_cusp_bounded_RR_inputs.py"
LEGACY_SHA="ca46e8f9a9410be240ad77c0863b193e77ef701b06186a31b3edb20eb3e997a4"
PAPER_SHA="1ebbc0bff297913a9a2f49a507998d49b173fe96ec6944a0e1ac81cd1295763d"
ROOT=Path(__file__).resolve().parent
legacy_path=ROOT/LEGACY_CORE
assert hashlib.sha256(legacy_path.read_bytes()).hexdigest()==LEGACY_SHA
loader=importlib.util.spec_from_file_location("R887_frozen_R880_finite_matrix_methods",legacy_path)
L=importlib.util.module_from_spec(loader);loader.loader.exec_module(L)

RESULT="R887-original-common-cusp-flip-and-bounded-RR-space"
FINAL="p41-original-common-cusp-flip-and-bounded-RR-certificate.json"
PREFIX="R887-"
PRIME,RANK=1000000753,272
EPS=L.EPS
SOURCES=("R880","R845","R872","R827")
PROOFS=("R887","R880","R872","R845")
INPUTS=("parent_cusp_matrix","parent_complete_cusp","parent_principal_inputs",
        "parent_source_audit","V2_jets","old_normal_index","old_rank","W_reduction","place_audit")
STRATEGY={
    "scope":"common_Cstar_full418_and_exact_Qtilde_minus1205",
    "prime":PRIME,"original_branch":0,"original_zeta_root":549966761,
    "original_s_root":99932770,"original_integral_B_root":3197390,
    "normal_basis_degrees":EPS,
    "original_divisor":"D_C=C+252P0, degree272",
    "restriction_shape":[272,418],"restriction_kernel_dimension":146,
    "new_original_Hensel_jets_computed":False,
    "u_C_selection":"first original kernel basis column with unit jet252, no rescaling",
    "second_anchor_schedule":"sum(integer_parameter^j * U_j), j=0..145",
    "fixed_u_C_products_shared_across_trials":True,
    "old_fiber_nodes":[0,1,2,3,4],"new_pencil_shape":[1360,1380],
    "required_new_pencil_rank":962,"Cstar_complete_space_dimension":418,
    "Cstar_divisor":"div_2H(u_C)-C-252P0, degree272",
    "Cstar_avoids_original_P0":True,
    "principal_function":"old_Q_f * (u_C/tau^2)",
    "principal_function_rho_order":-1205,
    "old_C_jets_normal_conversion_and_Krylov_inverses_recomputed":False,
    "exact_sources":"original characteristic-zero unit-solve expressions",
    "characteristic_zero_coefficients_reconstructed":False,
    "original_Lj_RR128_or_144_computed":False,
    "only_budget_trial_limit_and_transport_excluded_from_identity":True,
}
sha,read,save,spec,plain,bound=L.sha,L.read,L.save,L.spec,L.plain,L.bound
fingerprint,identity,source_identity=L.fingerprint,L.identity,L.source_identity
rows,shape,pivots=L.rows,L.shape,L.pivots
BudgetStop,UnitFailure,SearchStop=L.BudgetStop,L.UnitFailure,L.SearchStop

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
        "legacy_R880_core_sha256":LEGACY_SHA,"method_sha256":item["method_sha256"],
        "proofs_sha256":{key:item["proofs"][key]["sha256"] for key in PROOFS},
        "sources":{label:source_identity(item["sources"][label]) for label in SOURCES},
        "inputs":item["inputs"],"strategy":STRATEGY}

class Job(L.Job):
    def __init__(self,args):
        import flint
        assert flint.__version__=="0.9.0"
        self.Matrix,self.Poly=flint.nmod_mat,flint.nmod_poly
        self.args,self.started=args,time.monotonic()
        self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41
        assert self.item["producer_inputs_pending"] is False
        assert self.item["core_sha256"]==sha(__file__)
        assert self.item["legacy_core"]==LEGACY_CORE and self.item["legacy_core_sha256"]==LEGACY_SHA
        assert sha(self.item["method"])==self.item["method_sha256"]
        assert set(self.item["proofs"])==set(PROOFS)
        assert self.item["proofs"]["R887"]["sha256"]==PAPER_SHA
        for value in self.item["proofs"].values():
            assert sha(value["path"])==value["sha256"]
        assert set(self.item["sources"])==set(SOURCES) and set(self.item["inputs"])==set(INPUTS)
        self.tag=expected_tag(self.item)
        self.out=Path(args.out);self.out.mkdir(parents=True,exist_ok=True)
        self.status="initializing";self.refs={};self.sources={};self.current=None
        self.maximum_trials=int(self.item.get("maximum_trials",4));assert self.maximum_trials>=1
        self.V2,self.V3=L.positions(2),L.positions(3)
        self.V3map={pair:i for i,pair in enumerate(self.V3)}
        self.accepted_trial=None;self.actual_rank=None

    def path(self,name):
        name=PREFIX+name if not name.startswith(PREFIX) else name
        assert Path(name).name==name
        return self.out/(name if name.endswith(".json.gz") else name+".json.gz")

    def old(self,name):
        path=self.path(name)
        if not path.exists():return None
        value=read(path)
        assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
        return value

    def put(self,name,value):
        self.status=name
        assert not any(k in value for k in ("result","configuration","complete"))
        save(self.path(name),dict(value,result=RESULT,configuration=self.tag,complete=True))
        print(json.dumps({"stage":name,"seconds":round(time.monotonic()-self.started,6)}),flush=True)
        return self.old(name)

    def checkpoint(self,stage,**detail):
        save(self.path("current"),{"result":RESULT,"configuration":self.tag,"complete":False,
            "stage":stage,"references":self.refs,**detail})
        self.current=self.ref("current")

    def prepare(self):
        self.sources={label:L.Source(label,self.item["sources"][label]) for label in SOURCES}
        for key in INPUTS:
            value,ref=self.source_input(key)
            setattr(self,key,value);setattr(self,key+"_ref",ref)
        self.parent,self.r845,self.r872,self.r827=(self.sources[x] for x in ("R880","R845","R872","R827"))
        final=self.parent.certificate
        assert final["complete"] is True
        assert final["actual_complete_common_cusp_418_space_certified"] is True
        assert final["actual_complete_Dstar_418_space_certified"] is True
        assert final["actual_original_Qf_principal_identity_certified"] is True
        assert final["original_zeta_root"]==549966761 and final["original_s_root"]==99932770
        assert final["original_integral_B_root"]==3197390 and final["prime"]==PRIME
        for key,sourcekey in (("common_cusp_constraint_matrix","parent_cusp_matrix"),
                             ("complete_common_cusp_418_kernel","parent_complete_cusp"),
                             ("original_D_cusp_chi_principal_inputs","parent_principal_inputs"),
                             ("source_audit","parent_source_audit")):
            assert plain(final[key])==plain(getattr(self,sourcekey+"_ref"))
        for label in ("R845","R872","R827"):
            assert self.parent.tag["sources"][label]==source_identity(self.item["sources"][label])
        assert self.parent_complete_cusp["accepted"] is True
        assert self.parent_complete_cusp["actual_rank_mod_prime"]==272
        assert self.parent_complete_cusp["actual_kernel_dimension"]==418
        assert self.parent_complete_cusp["all_original_equations_verified"] is True
        assert self.parent_complete_cusp["full_characteristic_zero_kernel_certified"] is True
        assert plain(self.parent_complete_cusp["source_references"]["constraint_matrix"])==plain(self.parent_cusp_matrix_ref)
        assert self.parent_cusp_matrix["matrix_shape"]==[272,690]
        assert self.parent_cusp_matrix["exact_divisor"]=="D_C=C+252P0"
        assert self.parent_cusp_matrix["all20_original_cusp_field_coordinates_retained"] is True
        assert self.parent_cusp_matrix["original_P0_not_in_C"] is True
        assert self.parent_principal_inputs["Q_f_order_in_actual_local_parameter"]==-1457
        assert self.parent_principal_inputs["ideal_principal_factor_direction"]=="positive multiplication by Q_f"
        assert self.parent_principal_inputs["complete_original_Dstar_space_certified"] is True
        assert self.parent_principal_inputs["complete_original_common_cusp_space_certified"] is True
        self.parameter=self.parent_principal_inputs["actual_local_parameter"]
        assert self.parameter in ("z_minus_z0","w_minus_w0")
        assert self.V2_jets["matrix_shape"]==[273,418]
        assert self.V2_jets["row_orders"]==list(range(273))
        assert self.V2_jets["V2_basis"]==[{"normal_basis_row":i,"power_of_z":k} for i,k in self.V2]
        assert self.V2_jets["normal_integer_scale_applied_again"] is False
        assert self.old_normal_index["normal_row_mapping"]==[list(x) for x in self.V3]
        assert self.old_normal_index["all690_rhs_and_all1380_equations_and_weighted_support_verified"] is True
        for name,value in (("original_zeta_root",549966761),("original_s_root",99932770),
                           ("original_integral_B_root",3197390),("original_b_root",637573097),
                           ("canonical_free_column",1186),("original_branch",0),("prime",PRIME)):
            assert self.place_audit[name]==value
        self.fibers=[]
        for z0,entry in enumerate(self.old_rank["source_fiber_products"]):
            product=self.r845.stage(entry["a"])
            eref=product["source_original_fiber_evaluation"]
            E=self.r845.stage(eref);kref=E["source_original_Krylov_point"]
            point=self.r827.stage(kref)
            assert point["prime"]==PRIME and point["z0"]==z0 and point["usable"] is True
            assert point["actual_cyclic_rank"]==272 and point["both_inverse_products_verified"] is True
            assert plain(point["source_original_W"])==plain(self.W_reduction_ref)
            shape(E["original_V3_Krylov_coordinates_mod_prime"],272,690)
            self.fibers.append((E,self.r845.ref(eref),point,self.r827.ref(kref)))
        assert len(self.fibers)==5
        self.normal_matrix()
        name="original-source-audit"
        if self.old(name) is None:
            self.put(name,{"prime":PRIME,"original_branch":0,
                "source_completed_R880":self.parent.ref(self.item["sources"]["R880"]["certificate"]),
                "source_original_C_constraint_matrix":self.parent_cusp_matrix_ref,
                "source_original_complete_common_cusp_kernel":self.parent_complete_cusp_ref,
                "source_original_Q_f":self.parent_principal_inputs_ref,
                "source_original_V2_jets":self.V2_jets_ref,
                "source_original_normal_index":self.old_normal_index_ref,
                "source_original_place":self.place_audit_ref,
                "same_original_K_and_L_place_verified":True,
                "no_original_C_jets_or_Krylov_arithmetic_recomputed":True,
                "prior_944_source_identity_retained_in_original_R880_tag":True,
                "unneeded_R820_R842_R849_carriers_not_retransported":True,
                "exact_objects_remain_original_unit_solve_expressions":True})
        self.refs["source_audit"]=self.ref(name)
        self.checkpoint("original_sources_bound")

    def restriction(self):
        name="original-418-column-restriction";old=self.old(name)
        chosen=[self.V3map[pair] for pair in self.V2]
        if old is None:
            self.status=name;self.budget()
            original=self.parent_cusp_matrix["matrix_mod_prime"]
            matrix=[[row[j] for j in chosen] for row in original]
            shape(matrix,272,418)
            self.put(name,{"prime":PRIME,"matrix_shape":[272,418],
                "matrix_mod_prime":matrix,"source_original_C_constraint_matrix":self.parent_cusp_matrix_ref,
                "selected_original_V3_columns":chosen,
                "V2_basis":[{"normal_basis_row":i,"power_of_z":k} for i,k in self.V2],
                "exact_kernel":"H0(2H-C-252P0)","exact_dimension":146,
                "tau_embedding_no_additional_scale":True,
                "old_constraints_only_selected_not_recomputed":True})
            old=self.old(name)
        assert old["selected_original_V3_columns"]==chosen
        self.refs["restriction"]=self.ref(name)
        kernel,kref=self.full_row_kernel("complete-U_C-146-kernel",
            self.mat(old["matrix_mod_prime"]),{"constraint_matrix":self.ref(name)},
            {"space":"H0(2H-C-252P0)","dimension":146,
             "degree_after_subtraction":272,"full_constraint_rank":272})
        self.U=kernel;self.refs["complete_U_C_146"]=kref
        name2="original-order252-functional-and-u_C";selected=self.old(name2)
        if selected is None:
            self.status=name2;self.budget()
            row=self.V2_jets["matrix_mod_prime"][252]
            values=rows(self.mat([row])*kernel)[0]
            choices=[i for i,v in enumerate(values) if v]
            accepted=bool(choices);column=choices[0] if choices else None
            coords=rows(self.sub(kernel,list(range(418)),[column])) if accepted else None
            self.put(name2,{"prime":PRIME,"accepted":accepted,
                "source_complete_U_C_146":kref,"source_original_V2_jets":self.V2_jets_ref,
                "original_jet_order":252,"order252_coefficients_mod_prime":values,
                "selected_first_unit_column":column,
                "u_C_normal_V2_coordinates_mod_prime":coords,
                "actual_order252_unit_mod_prime":values[column] if accepted else None,
                "actual_local_parameter":self.parameter,
                "selected_exact_section":{
                    "operation":"column_of_original_complete_U_C_unit_kernel",
                    "source_kernel":kref,"column":column,"additional_rescaling":False},
                "Cstar_definition":"div_2H(u_C)-C-252P0",
                "Cstar_degree":272,"Cstar_avoids_original_P0":accepted,
                "complete_Cstar_418_space_already_computed":False})
            selected=self.old(name2)
        if not selected["accepted"]:
            raise UnitFailure("No original U_C column has a unit order252 coefficient at this place")
        assert selected["source_complete_U_C_146"]==kref
        self.u_index=selected["selected_first_unit_column"]
        self.u252=selected["actual_order252_unit_mod_prime"]
        assert self.u252
        self.refs["u_C"]=self.ref(name2)
        self.checkpoint("complete_U_C_and_exact_u_C")
        return selected

    def second_anchor(self,trial):
        name=f"trial-{trial:06d}-v_C";old=self.old(name)
        if old is None:
            self.status=name;self.budget()
            coefficients=[pow(trial,j,PRIME) for j in range(146)]
            coords=self.U*self.mat([[v] for v in coefficients])
            self.put(name,{"prime":PRIME,"integer_parameter":trial,
                "source_complete_U_C_146":self.refs["complete_U_C_146"],
                "normal_V2_coordinates_mod_prime":rows(coords),
                "exact_section_definition":{
                    "operation":"integer_moment_curve_in_complete_original_U_C",
                    "source_kernel":self.refs["complete_U_C_146"],
                    "integer_parameter":trial,"j_range":[0,146],"coefficient_formula":"integer_parameter^j"}})
            old=self.old(name)
        assert old["integer_parameter"]==trial
        assert old["source_complete_U_C_146"]==self.refs["complete_U_C_146"]
        return old,self.ref(name)

    def product(self,role,trial,coordinates,source,z0):
        label="fixed-u_C" if role=="u" else f"trial-{trial:06d}-v_C"
        name=label+f"-fiber-{z0}-times-original-V3";old=self.old(name)
        E,eref,point,kref=self.fibers[z0]
        if old is None:
            self.status=name;self.budget()
            values=[0]*272
            for j,(i,k) in enumerate(self.V2):
                values[i]=(values[i]+int(coordinates[j][0])*pow(z0,k,PRIME))%PRIME
            W=self.mat(point["W_evaluated_mod_prime"]);current=self.mat([[v] for v in values])
            columns=[]
            for j in range(272):
                columns.append([int(current[i,0]) for i in range(272)])
                if j+1<272:current=W*current
            result=self.mat(columns).transpose()*self.mat(E["original_V3_Krylov_coordinates_mod_prime"])
            self.put(name,{"prime":PRIME,"role":role,"integer_parameter":None if role=="u" else trial,
                "z0":z0,"source_exact_section":source,
                "source_original_fiber_evaluation":eref,"source_original_Krylov":kref,
                "source_original_W":self.W_reduction_ref,
                "matrix_shape":[272,690],"product_evaluation_matrix_mod_prime":rows(result),
                "normal_section_evaluation_mod_prime":values,
                "source_K_inverse_V3_reused":True,
                "fixed_u_products_shared_across_trials":role=="u",
                "old_source_arithmetic_recomputed":False})
            old=self.old(name)
        assert old["source_exact_section"]==source and old["z0"]==z0
        assert old["source_original_Krylov"]==kref
        return old,self.ref(name)

    def trial(self,n,u):
        v,vref=self.second_anchor(n)
        data=[];sources=[]
        for z0 in range(5):
            a,ar=self.product("u",None,u["u_C_normal_V2_coordinates_mod_prime"],self.refs["u_C"],z0)
            b,br=self.product("v",n,v["normal_V2_coordinates_mod_prime"],vref,z0)
            data.extend([x+y for x,y in zip(a["product_evaluation_matrix_mod_prime"],
                                            b["product_evaluation_matrix_mod_prime"])])
            sources.append({"z0":z0,"u":ar,"v":br})
            self.checkpoint("new_anchor_products",trial=n,last_fiber=z0)
        matrix=self.mat(data);del data
        name=f"trial-{n:06d}-complete-pencil-profile";profile=self.old(name)
        if profile is None:
            self.status=name;self.budget()
            reduced,rank=matrix.rref()
            assert rank<=962
            value={"prime":PRIME,"trial":n,"source_exact_u_C":self.refs["u_C"],
                "source_exact_v_C":vref,"source_fiber_products":sources,
                "matrix_shape":[1360,1380],"actual_rank":rank,"required_rank":962,
                "accepted":rank==962,"additional_common_zero_degree":0 if rank==962 else None,
                "failure_only_this_sufficient_residue_pencil_test":rank!=962}
            if rank==962:
                J=pivots(reduced,rank)
                selected=self.sub(matrix,list(range(1360)),J)
                second,rank2=selected.transpose().rref();assert rank2==rank
                I=pivots(second,rank)
                value.update({"selected_rows":I,"selected_columns":J,
                    "image_is_complete_H0_5H_minus_D_C":True,
                    "finite_evaluation_injective_on_the_complete_original_image":True})
            self.put(name,value);profile=self.old(name)
        assert profile["source_fiber_products"]==sources and profile["source_exact_v_C"]==vref
        self.actual_rank=profile["actual_rank"]
        if not profile["accepted"]:
            self.checkpoint("sufficient_pencil_test_failed",trial=n,rank=self.actual_rank)
            return False
        kernel,kref=self.selected_kernel(f"trial-{n:06d}-new-962",matrix,
            profile["selected_rows"],profile["selected_columns"],
            {"profile":self.ref(name),"u_C":self.refs["u_C"],"v_C":vref,"fiber_products":sources},
            {"relation":"u_C*r+v_C*s=0","dimension":418,
             "common_zero_divisor":"D_C=C+252P0","common_zero_degree":272,
             "projection_image":"H0(3H-Cstar)"})
        projected,pref=self.project_second(f"trial-{n:06d}-Cstar",kernel,kref,418,
            {"space":"H0(3H-Cstar)","degree_Cstar":272,"dimension":418,
             "Cstar_definition":"div_2H(u_C)-C-252P0","P0_not_in_Cstar":True})
        self.refs["complete_Cstar_418"]=pref
        self.refs["accepted_profile"]=self.ref(name)
        self.refs["accepted_v_C"]=vref
        self.accepted_trial=n
        self.checkpoint("complete_Cstar_418_space",trial=n)
        del matrix,kernel;gc.collect()
        return True

    def principal(self):
        name="original-Cstar-and-Qtilde-principal-inputs";old=self.old(name)
        if old is None:
            self.status=name;self.budget()
            previous=int(self.parent_principal_inputs["Q_f_leading_coefficient_mod_prime"])
            leading=previous*self.u252%PRIME;assert leading
            self.put(name,{
                "prime":PRIME,"source_original_Q_f":self.parent_principal_inputs_ref,
                "source_exact_u_C":self.refs["u_C"],
                "source_complete_Cstar_418":self.refs["complete_Cstar_418"],
                "source_complete_original_Dstar_418":self.parent.ref(self.parent_principal_inputs["source_complete_Dstar_418_space"]),
                "source_complete_original_Dchi_418":self.parent_principal_inputs["source_complete_D_chi_418_space"],
                "Cstar_definition":"div_2H(u_C)-C-252P0","Cstar_degree":272,
                "Cstar_avoids_original_P0":True,
                "exact_principal_function":{
                    "operation":"multiply","left":{"operation":"original_R880_Q_f","source":self.parent_principal_inputs_ref},
                    "right":{"operation":"original_u_C_over_tau_squared","source":self.refs["u_C"]}},
                "exact_divisor_identity":"E_f-1206P0=-(Cstar-H)+3(Dstar-H)+4(Dchi-H)+div(Qtilde)",
                "ideal_principal_factor_direction":"positive multiplication by Qtilde",
                "actual_local_parameter":self.parameter,"actual_rho_order":-1205,
                "actual_leading_coefficient_mod_prime":leading,
                "exact_leading_coefficient_expression":{
                    "operation":"multiply_original_Q_f_leading_coefficient_by_u_C_jet252",
                    "left_source":self.parent_principal_inputs_ref,"right_source":self.refs["u_C"],
                    "no_actual_unit_rescaled_to_one":True},
                "conditional_original_t_leading_coefficient":"rho_leading_coefficient * (t/rho at P0)^1205",
                "original_t_frame_value_computed":False,
                "all_three_effective_degree272_representatives_avoid_original_P0":True,
                "original_Cstar_and_qC_are_fixed_by_L_over_K_Galois_action":True,
                "Q_rational_descent_asserted_from_modular_arrays":False,
                "Galois_norm_identity":"sum_sigma(E_f^sigma)-8442P0=-7(Cstar-H)+3sum_sigma(Dstar^sigma-H)+28(Dchi-H)+div(N_sigma(Qtilde))",
                "Galois_norm_rho_order":-8435,
                "complete_Cstar_418_certified":True,"original_Qtilde_order_minus1205_certified":True,
                "five_original_Lj_RR128_or_144_computed":False,
                "connection_Poincare_period_or_height_computed":False})
            old=self.old(name)
        assert old["source_complete_Cstar_418"]==self.refs["complete_Cstar_418"]
        self.refs["principal_inputs"]=self.ref(name)
        self.checkpoint("complete_original_common_cusp_flip")
        return self.ref(name)

    def run(self):
        self.prepare();u=self.restriction()
        for n in range(1,self.maximum_trials+1):
            self.budget()
            if self.trial(n,u):
                self.principal();return self.finish(True,None)
        raise SearchStop("No complete Cstar pencil among the finite retained trials")

    def inventory(self):
        entries=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name in (self.path("current").name,self.path("exact-stages-manifest").name):continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
            entries.append(spec(path))
        save(self.path("exact-stages-manifest"),{"result":RESULT,"configuration":self.tag,"complete":True,
            "files":entries,"all_complete_stages_retained":True,"current_excluded":True})
        return self.ref("exact-stages-manifest")

    def finish(self,complete,reason):
        final={"result":RESULT,"configuration":self.tag,"complete":bool(complete),"p":41,"prime":PRIME,
            "source_audit":self.refs.get("source_audit"),"restriction":self.refs.get("restriction"),
            "complete_U_C_146":self.refs.get("complete_U_C_146"),"u_C":self.refs.get("u_C"),
            "accepted_profile":self.refs.get("accepted_profile"),"accepted_v_C":self.refs.get("accepted_v_C"),
            "complete_Cstar_418":self.refs.get("complete_Cstar_418"),
            "original_principal_inputs":self.refs.get("principal_inputs"),
            "complete_U_C_146_certified":bool(self.refs.get("complete_U_C_146")),
            "original_u_C_order252_certified":bool(self.refs.get("u_C")),
            "complete_Cstar_418_certified":bool(self.refs.get("complete_Cstar_418")),
            "original_Qtilde_order_minus1205_certified":bool(self.refs.get("principal_inputs")),
            "accepted_trial":self.accepted_trial,"actual_pencil_rank":self.actual_rank,
            "exact_objects_are_original_unit_solve_expressions":True,
            "characteristic_zero_RR_coefficients_reconstructed":False,
            "new_original_Hensel_jets_computed":False,
            "original_t_frame_value_computed":False,
            "five_original_Lj_RR128_or_144_computed":False,
            "connection_Poincare_period_or_height_computed":False,
            "stop_reason":reason,"stage_manifest":self.inventory(),"resume_state":self.current,
            "seconds":time.monotonic()-self.started}
        if complete:
            assert final["complete_Cstar_418_certified"] and final["original_Qtilde_order_minus1205_certified"]
            assert final["actual_pencil_rank"]==962
        save(self.out/FINAL,final);return final

def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise SystemExit("R887 new arithmetic runs only in the authorized public repository Actions")
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    parser.add_argument("--config",required=True);parser.add_argument("--out",required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args();started=time.monotonic()
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    job=None;final=None;error=None;code=0
    try:
        job=Job(args)
        if (out/FINAL).exists():
            previous=read(out/FINAL)
            assert previous["result"]==RESULT and previous["configuration"]==job.tag
            if previous["complete"] is True:
                for ref in read(bound(out,previous["stage_manifest"]))["files"]:bound(out,ref)
                final=previous
            else:final=job.run()
        else:final=job.run()
    except BudgetStop as exc:code=124;error=str(exc)
    except (UnitFailure,SearchStop) as exc:code=2;error=str(exc)
    except Exception as exc:code=1;error=str(exc);traceback.print_exc()
    if final is None and job is not None:
        try:final=job.finish(False,error)
        except Exception:traceback.print_exc()
    receipt={"result":RESULT,"source_sha256":sha(__file__),"complete":bool(final and final["complete"]),
        "configuration_sha256":fingerprint(job.tag) if job else None,
        "certificate_sha256":sha(out/FINAL) if final else None,
        "complete_U_C_146_certified":bool(final and final["complete_U_C_146_certified"]),
        "original_u_C_order252_certified":bool(final and final["original_u_C_order252_certified"]),
        "complete_Cstar_418_certified":bool(final and final["complete_Cstar_418_certified"]),
        "original_Qtilde_order_minus1205_certified":bool(final and final["original_Qtilde_order_minus1205_certified"]),
        "actual_pencil_rank":final.get("actual_pencil_rank") if final else None,
        "five_original_Lj_RR128_or_144_computed":False,
        "exit_code":code,"error":error,"seconds":time.monotonic()-started}
    save(out/"core-receipt.json",receipt)
    print("R887_CORE_SUMMARY="+json.dumps(receipt,sort_keys=True),flush=True)
    return code

if __name__=="__main__":
    raise SystemExit(main())
