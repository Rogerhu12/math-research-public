#!/usr/bin/env python3
"""R901: five original marked pole differences through one fixed flip DAG."""
import argparse
import gc
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import sys
import time
import traceback

REPOSITORY="Rogerhu12/math-research-public"
RESULT="R901-original-five-Z-shared-bounded-flip-DAG"
FINAL="p41-original-five-Z-shared-bounded-flip-certificate.json"
PREFIX="R901-"
LEGACY_FILE="R890_original_Ef_eight_flip_and_marked_frame.py"
LEGACY_SHA="da8498fc6ab0f143ba347f4a7dec91c7474bbe2520c349bf33a84bba8e65420f"
COMPACT_FILE="R894_original_seven_conjugate_pole_trace.py"
COMPACT_SHA="9a2793c79e552c04ea384f5c6bfb673e6e7d506ff91cf9e246fbc00a76f2da56"
P=1000000753
EPS=[0]+[1]*144+[2]*127
OLD_GROUPS=("R827","R872","R883")
DIRECT_GROUPS=("R890","R896","R900","R902")
GROUPS=OLD_GROUPS+DIRECT_GROUPS
CLASS_ORDER=["Dchi-H","DK-H"]+[
    "sigma^%d(Dstd_%d)-H"%(k,j) for j in range(1,6) for k in range(7)]
POWERS=[12,8,8,13,14]
DEGREES=[2970,1674,1800,3024,3339]
P_NUMERATORS=[165,93,100,168,371]
Q_DENOMINATORS=[67,67,67,67,134]
RHO_ORDERS=[-686,-182,-231,-707,-1659]
BRANCH_ORDER=[0,6,1,2,4,3,5]
STRATEGY={
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "original_b_branch_order_by_sigma_power":BRANCH_ORDER,
    "normal_basis_degrees":EPS,"normal_V3_dimension":690,
    "complete_divisor_space_dimension":418,"complete_U_dimension":146,
    "old_fibres":[0,1,2,3,4,5,6],"complete_fibre_length":1904,
    "legacy_flip_core_sha256":LEGACY_SHA,"compact_flip_core_sha256":COMPACT_SHA,
    "frozen_methods_imported_without_monkey_patch":True,
    "product_image_rank":962,"membership_shape":[1884,690],
    "complete_relation_shape":[1904,1380],"complete_relation_kernel_dimension":418,
    "product_anchor_schedule":"unchanged ordered original left kernel columns",
    "pencil_schedule":"unchanged positive integer power combinations of complete U146",
    "P0_unit_selection":"unchanged first nonzero column; no scalar rescaling",
    "new_flip_count":126,"reused_flip_count":2,
    "original_R890_reused_nodes":{"Xminus2":"flip-04-D2","X4":"flip-05-E"},
    "class_coordinate_order":CLASS_ORDER,
    "original_Hom_words":["1+T^"+str(j) for j in range(1,6)],
    "ordinary_powers":POWERS,"original_pole_degrees":DEGREES,
    "original_p_numerators":P_NUMERATORS,"original_q_denominators":Q_DENOMINATORS,
    "original_QZ_rho_orders":RHO_ORDERS,
    "principal_recurrence":"Fnew=1/(qnew*Fleft*Fright), repeated parents retained twice",
    "terminal_principal":"QZ_j=F_j*(product_k sigma^k(Q_j))^q_j*QK^(-p_j)",
    "equivalent_NormG_qchi_formula_is_audit_only_not_an_additional_factor":True,
    "original_I_Z_identity":"I_Zj=QZ_j*I_DZj*I_H_inverse, positive multiplication",
    "descent_factor":"sigma(QZ_j)/QZ_j",
    "descent_space_identity":"QZ_j*W_DZj=H0(2H-Z_j) tensor_K L",
    "negative_support_of_Zj_not_assumed_to_be_only_P0":True,
    "later_K_evaluation_requires_actual_whole_Artin_denominator_units_and_418_minor":True,
    "terminal_divisor_or_normal_basis_asserted_K_fixed":False,
    "old_W_Krylov_fibres_jets_original_RR_or_two_old_flips_recomputed":False,
    "closed_work_retention":"R894 exact selected product columns, full basis/inverse and live unit-solve closure",
    "only_complete_work_compacted_active_or_pending_work_preserved":True,
    "reference_count_eviction_discards_only_in_memory_matrices_not_live_proof_bytes":True,
    "search_limits_budget_disk_floor_and_transport_excluded_from_mathematical_identity":True}

def own_sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(4*1024*1024),b""):
            h.update(block)
    return h.hexdigest()

module_path=Path(__file__).resolve().parent/COMPACT_FILE
assert own_sha(module_path)==COMPACT_SHA
description=importlib.util.spec_from_file_location("R901_frozen_R894_compact_flip",module_path)
M=importlib.util.module_from_spec(description)
description.loader.exec_module(M)
L=M.L
assert own_sha(Path(__file__).resolve().parent/LEGACY_FILE)==LEGACY_SHA
sha,read,save,fingerprint,plain,spec=L.sha,L.read,L.save,L.fingerprint,L.plain,L.spec
mat,rows,shape,eye,zero=L.mat,L.rows,L.shape,L.eye,L.zero
BudgetStop,UnitFailure,SearchStop=L.BudgetStop,L.UnitFailure,L.SearchStop
live_refs=M.live_refs

def group_ref(group,row):
    return {**plain(row),"source_group":group}

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],
        "python_flint":"0.9.0","p":41,"legacy_flip_core_sha256":LEGACY_SHA,
        "compact_flip_core_sha256":COMPACT_SHA,"method_sha256":item["method_sha256"],
        "proofs":item["proofs"],"fixed_plan_sha256":item["fixed_plan_sha256"],
        "sources":{g:L.identity(item["sources"][g]) for g in GROUPS},
        "inputs":item["inputs"],"strategy":STRATEGY}

def exact_target(j):
    answer=[0]*37
    answer[0]=7*Q_DENOMINATORS[j-1]*(POWERS[j-1]-2)
    answer[1]=-P_NUMERATORS[j-1]
    for k in range(7):
        answer[2+7*(j-1)+k]=Q_DENOMINATORS[j-1]
    return answer

class Job(M.Job):
    def __init__(self,args):
        self.args=args;self.started=time.monotonic();self.out=Path(args.output)
        self.out.mkdir(parents=True,exist_ok=True);self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41
        assert self.item["producer_inputs_pending"] is False
        assert sha(__file__)==self.item["core_sha256"] and L.flint.__version__=="0.9.0"
        assert self.item["legacy_core"]==LEGACY_FILE and self.item["legacy_core_sha256"]==LEGACY_SHA
        assert self.item["compact_core"]==COMPACT_FILE and self.item["compact_core_sha256"]==COMPACT_SHA
        topic=Path(__file__).resolve().parent.parent
        assert sha(topic/self.item["method"])==self.item["method_sha256"]
        for proof in self.item["proofs"].values():
            assert sha(topic/proof["path"])==proof["sha256"]
        plan_path=topic/self.item["fixed_plan"]
        assert sha(plan_path)==self.item["fixed_plan_sha256"]
        self.plan=read(plan_path)
        assert self.plan["proof"]["sha256"]==self.item["proofs"]["R901"]["sha256"]
        assert self.plan["planned_new_flip_count"]==126
        assert self.plan["already_completed_reused_flip_count"]==2
        assert self.plan["actual_outputs"]["completed_new_flip_count"]==0
        assert self.plan["mathematical_source_placeholders"]["R900"] is None
        assert all(row is None for record in self.plan["mathematical_source_placeholders"]["R896_original_orbits"]
                   for row in record["conjugate_sources"])
        self.chain=[(r["id"],r["left"],r["right"]) for r in self.plan["nodes"]]
        assert len(self.chain)==126 and len({x[0] for x in self.chain})==126
        assert [x[0] for x in self.chain[-5:]]==["Z1","Z2","Z3","Z4","Z5"]
        assert set(self.item["sources"])==set(GROUPS)
        self.tag=expected_tag(self.item);self.refs={};self.flip_refs=[];self.closed_refs=[]
        self.reused_flip_refs=[];self.current=None;self.phase="source-initialization"
        self.sources={g:L.Source(g,self.item["sources"][g],args.retained) for g in GROUPS}
        self.inputs=self.item["inputs"];self.spaces={};self.space_cache={};self.fibres={}
        self.completed_directions={};self.original_principals={};self.node_states={}

    def budget(self):
        if time.monotonic()-self.started>=self.args.budget_minutes*60-30:
            raise BudgetStop("R901 complete atomic stages retained; phase="+self.phase)
        floor=int(self.item.get("minimum_free_disk_bytes",768*1024*1024))
        if shutil.disk_usage(self.out).free<floor:
            raise BudgetStop("R901 disk floor reached; all live and active witnesses retained.")

    def path(self,name):
        assert Path(name).name==name
        return self.out/(PREFIX+name+".json.gz")

    def old(self,name):
        path=self.path(name)
        if not path.exists():
            return None
        value=read(path)
        assert value["result"]==RESULT and value["configuration"]==self.tag
        assert value["complete"] is True
        self.refs[name]=spec(path)
        return value

    def put(self,name,value):
        assert not any(k in value for k in ("result","configuration","complete"))
        payload={"result":RESULT,"configuration":self.tag,"complete":True,**value}
        path=self.path(name)
        if path.exists():
            assert read(path)==payload
        else:
            save(path,payload)
        self.refs[name]=spec(path)
        print("R901_STAGE="+json.dumps({"file":path.name,"seconds":time.monotonic()-self.started}),flush=True)
        return payload

    def checkpoint(self,phase):
        self.phase=phase
        value={"result":RESULT,"configuration":self.tag,"complete":False,"phase":phase,
            "complete_new_flip_certificates":self.flip_refs,
            "reused_R890_complete_flip_certificates":self.reused_flip_refs,
            "closed_work_retention_receipts":self.closed_refs,
            "completed_original_directions":self.completed_directions,
            "completed_handwritten_node_ids":[x[0] for x in self.chain[:len(self.flip_refs)]],
            "retained_complete_stages":self.refs}
        save(self.path("current"),value);self.current=spec(self.path("current"))

    def external(self,row):
        return self.sources[row["source_group"]].stage(row)

    def own(self,row):
        if row.get("source_group") is not None:
            return self.external(row)
        path=self.out/plain(row)["file"]
        assert spec(path)==plain(row)
        value=read(path)
        assert value["configuration"]==self.tag and value["complete"] is True
        return value

    def install_initial(self,label,raw,reference,coordinate,function=None,Fvalue=1):
        shape(raw,690,418)
        assert len(coordinate)==37 and 0<Fvalue<P
        self.spaces[label]={"matrix":mat(raw),"reference":reference,"kappa":coordinate,
            "Fvalue":Fvalue,"function":function or {
                "operation":"one_for_same_original_initial_representative","source":reference}}

    def prepare(self):
        self.V3=L.positions(3);self.V2=L.positions(2)
        assert len(self.V3)==690 and len(self.V2)==418
        original=self.sources["R890"];cert=original.certificate
        assert cert["actual_all_eight_complete_normal418_spaces_certified"] is True
        assert cert["actual_original_Ef_bounded_divisor_identity_certified"] is True
        assert cert["actual_complete_flip_count"]==8 and original.tag["source_sha256"]==LEGACY_SHA
        old_inputs=original.tag["inputs"]
        for group in OLD_GROUPS:
            L.same_source(original.tag["sources"][group],self.item["sources"][group])
        for key in ("Dchi","point_jets","point_linear_functional","t_frame",
                    "original_W","original_grid","original_place","original_Krylov_points"):
            assert self.inputs[key]==old_inputs[key]
        self.points={}
        for z,row in enumerate(self.inputs["original_Krylov_points"]):
            point=self.external(row)
            assert point["prime"]==P and point["z0"]==z and point["usable"] is True
            assert point["actual_cyclic_rank"]==272 and point["both_inverse_products_verified"] is True
            assert plain(point["source_original_W"])==plain(self.inputs["original_W"])
            self.points[z]=point
        assert len(self.points)==7
        self.W=self.source("original_W");self.place=self.source("original_place")
        assert self.W["prime"]==self.place["prime"]==P
        assert self.place["original_zeta_root"]==549966761
        self.frame=self.source("t_frame")
        assert self.frame["original_t_first_order_unit_certified"] is True
        assert self.frame["original_t_over_rho_constant_mod_prime"]==354813668
        assert self.frame["original_s_root"]==99932770
        neutral=self.source("R890_neutral")
        assert neutral["neutral_avoids_original_P0"] is True
        assert neutral["tau_V2_is_complete_W_H"] is True
        assert neutral["source_original_point"]==old_inputs["point_linear_functional"]
        assert neutral["source_original_V2_jets"]==old_inputs["point_jets"]
        assert neutral["normal_V3_basis"]==[list(x) for x in self.V3]
        assert len(neutral["normal_V3_P0_functional_mod_prime"])==690
        name="neutral-H-and-original-P0-functional"
        alias=self.old(name)
        if alias is None:
            alias=self.put(name,{
                "prime":P,"source_original_R890_neutral":self.inputs["R890_neutral"],
                "neutral_W_H_normal_V3_basis_mod_prime":neutral["neutral_W_H_normal_V3_basis_mod_prime"],
                "normal_V3_P0_functional_mod_prime":neutral["normal_V3_P0_functional_mod_prime"],
                "normal_V3_basis":neutral["normal_V3_basis"],
                "old_complete_neutral_space_and_P0_functional_copied_without_arithmetic":True,
                "neutral_avoids_original_P0":True,"neutral_degree":272})
        assert alias["source_original_R890_neutral"]==self.inputs["R890_neutral"]
        self.point_row=mat([alias["normal_V3_P0_functional_mod_prime"]])
        self.install_initial("H",alias["neutral_W_H_normal_V3_basis_mod_prime"],self.refs[name],[0]*37)
        chi=self.source("Dchi")
        assert chi["full_characteristic_zero_dimension"]==418
        assert chi["all1234_by418_complete_V5_relations_zero"] is True
        assert chi["normal_integer_scale_applied_again"] is False
        coordinate=[0]*37;coordinate[0]=1
        self.install_initial("X",chi["V3_kernel_basis_mod_prime"],self.inputs["Dchi"],coordinate)
        self.reuse_original_chi_flips()
        self.prepare_original_T()
        self.prepare_original_orbits()
        self.normal_fibres()
        name="original-source-audit"
        if self.old(name) is None:
            self.put(name,{
                "prime":P,"source_identities":{g:L.identity(self.item["sources"][g]) for g in GROUPS},
                "inputs":self.inputs,"fixed_plan_sha256":self.item["fixed_plan_sha256"],
                "original_sigma_branch_order":BRANCH_ORDER,
                "all_five_by_seven_original_Dstd_spaces_and_principals_bound":True,
                "source_original_R900_K_defined_representative":self.inputs["R900_complete"],
                "source_original_R900_marked_QK":self.inputs["R900_QK"],
                "two_completed_R890_chi_flips_reused":self.reused_flip_refs,
                "original_D2_E_accumulated_F_not_reset":True,
                "old_W_Krylov_V3_fibres_P0_and_normal_spaces_recomputed":False,
                "all_original_selected_scalars_preserved_without_rescaling":True,
                "class_coordinate_order":CLASS_ORDER,
                "original_target_class_coordinates":{str(j):exact_target(j) for j in range(1,6)},
                "actual_new_flip_arithmetic_performed_in_source_audit":False,
                "all_new_mathematics_only_in_public_Actions":True})
        self.checkpoint("complete-original-sources-and-two-reused-flips")

    def reuse_original_chi_flips(self):
        original=self.sources["R890"]
        self.reused_flip_refs=[]
        for label,oldlabel,index,coefficient in (("Xminus2","D2",4,-2),("X4","E",5,4)):
            row=self.inputs["reused_complete_flips"][label]
            assert plain(row) in [plain(x) for x in original.certificate["complete_flip_certificates"]]
            completed=self.external(row)
            assert completed["flip_index"]==index and completed["new_space_label"]==oldlabel
            assert completed["actual_complete_space_dimension"]==418
            for key in ("all1904_by418_pencil_relations_verified","all1884_by146_membership_relations_verified",
                        "effective_degree272_and_original_P0_avoidance_certified"):
                assert completed[key] is True
            bref=group_ref("R890",completed["complete_normal418_space"])
            pref=group_ref("R890",completed["principal_function_and_P0_unit"])
            uref=group_ref("R890",completed["original_unscaled_P0_unit_section"])
            basis=self.external(bref);principal=self.external(pref);u=self.external(uref)
            assert principal["new_original_class_coefficients"]==[0,0,coefficient]
            assert principal["class_coordinate_order"]==["Cstar-H","Dstar-H","Dchi-H"]
            assert principal["F_P0_unit_inverse_product_verified"] is True
            assert principal["all_selected_original_scalars_retained"] is True
            assert principal["original_rho_order_of_F"]==0
            assert plain(principal["source_complete_new_normal418"])==plain(bref)
            assert plain(principal["source_original_unscaled_u"])==plain(uref)
            assert u["original_scalar_not_rescaled"] is True and u["q_P0_value_is_unit"] is True
            assert principal["q_P0_value_mod_prime"]==u["q_P0_value_mod_prime"]
            assert basis["complete_RR_space_certified"] is True
            coefficient_vector=[0]*37;coefficient_vector[0]=coefficient
            function={"operation":"external_original_exact_principal_function_DAG","source":pref,
                "original_coordinate_order":principal["class_coordinate_order"],
                "original_accumulated_F_retained_without_reinitialization":True}
            self.install_initial(label,basis["normal_V3_basis_mod_prime"],bref,coefficient_vector,
                                 function,principal["F_P0_value_mod_prime"])
            self.reused_flip_refs.append(row)
        first=self.external(self.inputs["reused_complete_flips"]["Xminus2"])
        second=self.external(self.inputs["reused_complete_flips"]["X4"])
        assert plain(first["left_complete_space"])==plain(self.inputs["Dchi"])
        assert plain(first["right_complete_space"])==plain(self.inputs["Dchi"])
        assert plain(second["left_complete_space"])==plain(first["complete_normal418_space"])
        assert plain(second["right_complete_space"])==plain(first["complete_normal418_space"])

    def prepare_original_T(self):
        producer=self.sources["R900"];cert=producer.certificate
        assert cert["original_K_defined_degree272_representative_certified"] is True
        assert cert["original_K_defined_marked_principal_certified"] is True
        assert plain(cert["complete_K_defined_degree272_certificate"])==plain(self.inputs["R900_complete"])
        assert plain(cert["marked_original_principal_QK"])==plain(self.inputs["R900_QK"])
        completed=self.source("R900_complete");principal=self.source("R900_QK")
        assert plain(completed["complete_normal418_space"])==plain(self.inputs["R900_space"])
        assert plain(principal["complete_normal418_space"])==plain(self.inputs["R900_space"])
        assert principal["QK_defined_over_original_K"] is True
        assert principal["DK_defined_over_original_K"] is True
        assert principal["D0_and_DK_avoid_original_P0"] is True
        assert principal["actual_QK_rho_order"]==principal["actual_QK_t_order"]==-8435
        assert principal["actual_original_t_over_rho_mod_prime"]==354813668
        assert plain(principal["source_original_t_frame"])==plain(self.inputs["t_frame"])
        assert principal["QK_root"]=="QK" and principal["exact_principal_DAG"]
        assert principal["original_unscaled_sections_and_tau_frames_preserved"] is True
        self.QK=principal
        basis=self.source("R900_space")
        coordinate=[0]*37;coordinate[1]=1
        self.install_initial("Tf",basis["normal_V3_basis_mod_prime"],self.inputs["R900_space"],coordinate)

    def prepare_original_orbits(self):
        original=self.sources["R896"];transport=self.sources["R902"]
        original_cert=original.certificate;transport_cert=transport.certificate
        assert original_cert["all_five_complete_low_weight_RR_spaces_certified"] is True
        assert original_cert["completed_directions"]==[1,2,3,4,5]
        assert original_cert["initial_powers"]==POWERS and original_cert["original_pole_degrees"]==DEGREES
        L.same_source(transport.tag["sources"]["R896"],self.item["sources"]["R896"])
        assert len(self.inputs["original_orbits"])==5
        for j,orbit in enumerate(self.inputs["original_orbits"],1):
            assert orbit["j"]==j and len(orbit["conjugates"])==7
            source0=self.inputs["original_orbits"][j-1]["conjugates"][0]
            assert plain(source0["complete"])==plain(original_cert["complete_direction_certificates"][str(j)])
            assert plain(transport_cert["original_sigma0_direction_certificates"][str(j)])==plain(source0["complete"])
            self.original_principals[str(j)]=[]
            for k,entry in enumerate(orbit["conjugates"]):
                assert entry["sigma_power"]==k and entry["original_branch"]==BRANCH_ORDER[k]
                group="R896" if k==0 else "R902"
                assert all(entry[key]["source_group"]==group for key in ("complete","space","principal"))
                if k:
                    recorded=transport_cert["complete_direction_conjugate_certificates"][str(j)][str(k)]
                    assert plain(recorded)==plain(entry["complete"])
                complete=self.external(entry["complete"])
                principal=self.external(entry["principal"]);basis=self.external(entry["space"])
                assert plain(complete["complete_normal418_space"])==plain(entry["space"])
                assert plain(complete["marked_principal_Q"])==plain(entry["principal"])
                assert plain(principal["complete_normal418_space"])==plain(entry["space"])
                assert principal["prime"]==basis["prime"]==P
                assert principal["actual_Q_rho_order"]==principal["actual_Q_t_order"]==1-DEGREES[j-1]
                assert principal["actual_original_t_over_rho_mod_prime"]==354813668
                assert plain(principal["source_original_t_frame"])==plain(self.inputs["t_frame"])
                if k==0:
                    assert complete["complete_original_low_weight_RR_and_marked_principal_certified"] is True
                    assert complete["true_characteristic_zero_unit_solve_expressions"] is True
                    assert complete["F0_and_Dstd_avoid_original_P0"] is True
                    assert principal["j"]==j and principal["ordinary_power"]==POWERS[j-1]
                    assert principal["original_pole_degree"]==DEGREES[j-1]
                    assert principal["original_fixed_chi_sign_is_negative_power_in_Q"] is True
                    assert principal["Q_root"]=="Q" and principal["exact_principal_nodes"]
                    root=principal["Q_root"]
                else:
                    assert principal["original_direction"]==j and principal["sigma_power"]==k
                    assert principal["original_branch"]==BRANCH_ORDER[k]
                    assert principal["strict_original_selection_and_integer_anchors_preserved"] is True
                    assert plain(principal["source_original_sigma0_marked_principal_Q"])==plain(source0["principal"])
                    assert principal["exact_principal_nodes"] and principal["exact_principal_root"]
                    root=principal["exact_principal_root"]
                lc=int(principal["actual_Q_rho_leading_mod_prime"])
                lt=int(principal["actual_Q_t_leading_mod_prime"])
                assert 0<lc<P and 0<lt<P
                coordinate=[0]*37;coordinate[2+7*(j-1)+k]=1
                label="D%d_%d"%(j,k)
                self.install_initial(label,basis["normal_V3_basis_mod_prime"],entry["space"],coordinate)
                self.original_principals[str(j)].append({
                    "original_direction":j,"sigma_power":k,"original_branch":BRANCH_ORDER[k],
                    "source":entry["principal"],"exact_root":root,
                    "rho_leading_mod_prime":lc,"t_leading_mod_prime":lt,
                    "rho_order":1-DEGREES[j-1]})

    def principal_step(self,stem,new,left,right,u,uref,space_ref):
        name=stem+"-principal-function-and-P0-unit"
        value=self.old(name);a=self.spaces[left];b=self.spaces[right]
        if value is None:
            self.budget()
            q0=int(u["q_P0_value_mod_prime"])
            assert 0<q0<P and 0<a["Fvalue"]<P and 0<b["Fvalue"]<P
            denominator=q0*a["Fvalue"]%P*b["Fvalue"]%P
            F0=pow(denominator,-1,P);assert denominator*F0%P==1
            coordinate=[-x-y for x,y in zip(a["kappa"],b["kappa"])]
            assert len(coordinate)==37
            value=self.put(name,{
                "prime":P,"new_space_label":new,"left_space_label":left,"right_space_label":right,
                "source_left_complete_space":a["reference"],"source_right_complete_space":b["reference"],
                "source_original_unscaled_u":uref,"source_complete_new_normal418":space_ref,
                "left_original_class_coefficients":a["kappa"],"right_original_class_coefficients":b["kappa"],
                "new_original_class_coefficients":coordinate,"class_coordinate_order":CLASS_ORDER,
                "exact_q_function":{"operation":"divide_original_unscaled_section_by_tau_cubed",
                    "source_original_section":uref,"section_frame":"original normal V3"},
                "exact_q_divisor_identity":"(Dleft-H)+(Dright-H)+(Dnew-H)=div(q)",
                "exact_F_function_DAG":{"operation":"inverse_of_product",
                    "factors":[{"operation":"q_u_over_tau_cubed","source":uref},a["function"],b["function"]],
                    "repeated_parent_factors_are_retained_twice":True},
                "exact_class_and_function_identity":"kappa_new=(Dnew-H)+div(Fnew)",
                "q_P0_value_mod_prime":q0,"left_F_P0_value_mod_prime":a["Fvalue"],
                "right_F_P0_value_mod_prime":b["Fvalue"],"F_P0_value_mod_prime":F0,
                "F_P0_unit_inverse_product_verified":True,"all_selected_original_scalars_retained":True,
                "original_rho_order_of_F":0,"characteristic_zero_function_or_unit_value_expanded":False})
        assert value["source_left_complete_space"]==a["reference"]
        assert value["source_right_complete_space"]==b["reference"]
        assert value["source_original_unscaled_u"]==uref
        assert value["source_complete_new_normal418"]==space_ref
        return value,self.refs[name]

    def closed_witness_files(self,certificate):
        todo=[plain(certificate)];seen={}
        while todo:
            row=todo.pop()
            if row.get("source_group") is not None:
                self.external(row);continue
            name=row["file"]
            assert name.startswith(PREFIX),("unqualified_external_live_reference",name)
            if name in seen:
                assert seen[name]==plain(row);continue
            value=self.own(row);seen[name]=plain(row)
            for child in live_refs(value):
                if child.get("source_group") is not None:
                    group=child["source_group"]
                    assert group in self.sources
                    assert self.sources[group].files[child["file"]]==plain(child)
                elif child["file"].startswith(PREFIX):
                    todo.append(plain(child))
                else:
                    raise AssertionError("Unqualified external live reference: "+child["file"])
        return seen

    def close_completed_work(self,index,label,certificate):
        stem="flip-%02d-%s"%(index,label)
        name=stem+"-closed-work-retention"
        old=self.old(name);keep=self.closed_witness_files(certificate)
        candidates=[p for p in sorted(self.out.glob(PREFIX+stem+"-*.json.gz")) if p.name!=self.path(name).name]
        if old is None:
            discarded=[spec(p) for p in candidates if p.name not in keep]
            old=self.put(name,{
                "prime":P,"complete_flip_certificate":certificate,
                "required_live_witness_files":list(sorted(keep.values(),key=lambda x:x["file"])),
                "discarded_intermediate_stage_history":discarded,
                "discarded_intermediate_count":len(discarded),
                "discarded_intermediate_bytes":sum(x["bytes"] for x in discarded),
                "discarded_items_are_hash_history_not_live_references":True,
                "all_needed_original_product_column_identities_retained":True,
                "complete_selected_product_basis_and_inverse_retained":True,
                "full_membership_U146_successful_pencil_kernel_418_and_qF_retained":True,
                "cleanup_started_only_after_complete_flip_certificate":True,
                "active_or_pending_work_discarded":False})
        assert old["complete_flip_certificate"]==certificate
        assert {x["file"]:plain(x) for x in old["required_live_witness_files"]}==keep
        for row in old["discarded_intermediate_stage_history"]:
            assert row["file"].startswith(PREFIX+stem+"-") and row["file"] not in keep
            path=self.out/row["file"]
            if path.exists():
                assert spec(path)==plain(row);path.unlink()
            self.refs.pop(row["file"][len(PREFIX):-len(".json.gz")],None)
        self.closed_refs.append(self.refs[name])
        self.checkpoint("closed-"+stem)

    def release_finished_memory(self,index):
        future={parent for _,a,b in self.chain[index:] for parent in (a,b)}
        for label,space in self.spaces.items():
            if label not in future:
                space.pop("matrix",None)
        for key in list(self.space_cache):
            if key[0] not in future:
                del self.space_cache[key]
        gc.collect()

    def marked_direction(self,j):
        name="j%d-original-Z-marked-principal-and-descent"%j
        value=self.old(name);terminal=self.spaces["Z"+str(j)]
        if value is None:
            self.budget()
            assert terminal["kappa"]==exact_target(j)
            p=P_NUMERATORS[j-1];q=Q_DENOMINATORS[j-1];n=POWERS[j-1];degree=DEGREES[j-1]
            assert q*degree==1206*p
            records=self.original_principals[str(j)]
            assert len(records)==7 and [r["sigma_power"] for r in records]==list(range(7))
            norm_lc=1;norm_tlc=1
            for row in records:
                norm_lc=norm_lc*row["rho_leading_mod_prime"]%P
                norm_tlc=norm_tlc*row["t_leading_mod_prime"]%P
            qk_lc=int(self.QK["actual_QK_rho_leading_mod_prime"])
            qk_tlc=int(self.QK["actual_QK_t_leading_mod_prime"])
            assert 0<qk_lc<P and 0<qk_tlc<P
            correction=terminal["Fvalue"]
            rho=correction*pow(norm_lc,q,P)%P*pow(qk_lc,-p,P)%P
            order=7*q*(1-degree)+8435*p
            assert order==RHO_ORDERS[j-1]==7*(q-p)
            c=int(self.frame["original_t_over_rho_constant_mod_prime"])
            cpower=pow(c,-order,P);t=rho*cpower%P
            via_old_t=correction*pow(norm_tlc,q,P)%P*pow(qk_tlc,-p,P)%P
            assert rho and t and via_old_t==t
            orbit={"operation":"product_of_all_seven_strict_original_constant_field_conjugates",
                "factors":[{"operation":"completed_original_marked_Q_root","source":r["source"],
                            "root":r["exact_root"],"sigma_power":r["sigma_power"]} for r in records],
                "already_contains_negative_qchi_power":True,
                "original_sigma_branch_order":BRANCH_ORDER,
                "source_exact_fixed_selection_conjugacy":self.inputs["R902_source_audit"]}
            QK={"operation":"completed_original_K_defined_QK","source":self.inputs["R900_QK"],
                "root":self.QK["QK_root"]}
            QZ={"operation":"multiply","factors":[terminal["function"],
                {"operation":"integer_power","base":orbit,"exponent":q},
                {"operation":"integer_power","base":QK,"exponent":-p}]}
            gamma={"operation":"apply_original_constant_field_sigma_to_whole_function_and_unit_solve",
                   "power":1,"input":QZ,"Y_normal_generators_fixed":True,
                   "source_strict_conjugacy":self.inputs["R902_source_audit"]}
            transition={"operation":"divide","numerator":gamma,"denominator":QZ}
            value=self.put(name,{
                "prime":P,"original_direction":j,"original_Hom_word":"1+T^"+str(j),
                "original_degree_zero_coefficients":{"p":p,"q":q},
                "original_pole_degree":degree,"ordinary_power":n,
                "source_complete_DZ_normal418":terminal["reference"],
                "source_terminal_flip":self.flip_refs[-1],
                "source_all_seven_original_Q":records,"source_original_QK":self.inputs["R900_QK"],
                "source_original_t_frame":self.inputs["t_frame"],
                "class_coordinate_order":CLASS_ORDER,"actual_terminal_class_coordinates":terminal["kappa"],
                "exact_original_Z_definition":"q_j*sum_k sigma^k(E_gj)-p_j*sum_k sigma^k(E_f)",
                "exact_norm_Qj_function_DAG":orbit,"norm_Qj_fixed_by_original_Gal_L_over_K":True,
                "exact_QZ_function_DAG":QZ,
                "equivalent_NormG_expression_for_audit_only":"F_j*(Norm G_j)^q_j*qchi^(-7*q_j*(n_j-2))*QK^(-p_j)",
                "equivalent_formula_not_multiplied_a_second_time":True,
                "exact_original_divisor_identity":"Z_j=(D_Zj-H)+div(QZ_j)",
                "exact_original_fractional_ideal_identity":"I_Zj=QZ_j*I_DZj*I_H_inverse",
                "principal_factor_direction":"positive multiplication",
                "DZ_effective_degree":272,"DZ_avoids_original_P0":True,
                "complete_W_DZ_dimension":418,"complete_W_DZ_definition":"H0(3H-D_Zj)",
                "actual_QZ_rho_order":order,"actual_QZ_t_order":order,
                "actual_norm_Qj_rho_leading_mod_prime":norm_lc,
                "actual_terminal_F_P0_unit_mod_prime":correction,
                "actual_QK_rho_leading_mod_prime":qk_lc,
                "actual_QZ_rho_leading_mod_prime":rho,
                "actual_original_c_exponent":-order,"actual_original_c_power_mod_prime":cpower,
                "actual_QZ_t_leading_mod_prime":t,
                "t_leading_agrees_with_product_of_original_t_leading_inputs":True,
                "exact_rho_leading_expression":"F_j(P0)*(product_k sigma^k LC_rho(Q_j))^q_j/LC_rho(QK)^p_j",
                "exact_t_leading_expression":"LC_rho(QZ_j)*c^(7*(p_j-q_j))",
                "exact_descent_transition_DAG":transition,
                "equivalent_transition_using_F_only":{"operation":"divide",
                    "numerator":{"operation":"apply_original_constant_field_sigma_to_whole_function_and_unit_solve",
                                 "power":1,"input":terminal["function"]},"denominator":terminal["function"]},
                "descent_divisor_identity":"div(sigma(QZ_j)/QZ_j)=D_Zj-sigma(D_Zj)",
                "exact_semilinear_action":"s -> (sigma(QZ_j)/QZ_j)*sigma(s)",
                "sevenfold_cocycle":"product_(k=0)^6 sigma^k(sigma(QZ_j)/QZ_j)=1 by telescoping",
                "K_descent_identification":"QZ_j*W_DZj=H0(2H-Z_j) tensor_K L",
                "terminal_divisor_or_normal_basis_claimed_K_fixed":False,
                "negative_support_not_assumed_to_be_only_P0":True,
                "later_K_coordinate_normalization_requires_actual_whole_Artin_units_and_418_minor":True,
                "old_original_sections_qchi_QK_frames_or_jets_recomputed":False,
                "all_original_unscaled_q_and_principal_leading_constants_preserved":True,
                "auxiliary_units_claimed_to_be_41_units":False,
                "real_descent_cube_identified_with_I_Z":False,
                "original_Rcal_kappa_theta_torsion_and_nonp_factors_changed":False,
                "Hecke_correspondence_norm_or_RR128_144_connection_or_height_computed":False})
        assert value["source_complete_DZ_normal418"]==terminal["reference"]
        assert value["actual_terminal_class_coordinates"]==exact_target(j)
        self.completed_directions[str(j)]=self.refs[name]
        self.checkpoint("complete-original-Z-"+str(j))
        return self.refs[name]

    def inventory(self):
        entries=[];histories=[];discarded=0
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name==PREFIX+"current.json.gz" or path.name.startswith(PREFIX+"stage-manifest-"):
                continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
            row=spec(path);entries.append(row)
            if "discarded_intermediate_stage_history" in value:
                histories.append(row);discarded+=value["discarded_intermediate_count"]
        payload={"result":RESULT,"configuration":self.tag,"complete":True,
            "files":entries,"current_excluded":True,
            "all_required_live_witnesses_and_unclosed_work_retained":True,
            "closed_work_retention_receipts":histories,
            "historical_discarded_intermediate_count":discarded,
            "historical_hashes_not_claimed_as_present_files":True}
        path=self.path("stage-manifest-"+fingerprint(payload))
        if path.exists():
            assert read(path)==payload
        else:
            save(path,payload)
        return spec(path),len(entries),discarded

    def finish(self,complete,reason):
        for j in range(1,6):
            name="j%d-original-Z-marked-principal-and-descent"%j
            if self.old(name) is not None:
                self.completed_directions[str(j)]=self.refs[name]
        self.checkpoint("completed" if complete else self.phase)
        inventory,count,discarded=self.inventory()
        if complete:
            assert len(self.flip_refs)==126 and len(self.reused_flip_refs)==2
            assert len(self.closed_refs)==126 and set(self.completed_directions)=={"1","2","3","4","5"}
        final={"result":RESULT,"configuration":self.tag,"complete":bool(complete),
            "p":41,"actual_auxiliary_prime":P,"source_audit":self.refs.get("original-source-audit"),
            "fixed_plan_sha256":self.item["fixed_plan_sha256"],
            "actual_new_complete_flip_count":len(self.flip_refs),
            "actual_reused_R890_complete_flip_count":len(self.reused_flip_refs),
            "actual_total_complete_flip_count":len(self.flip_refs)+len(self.reused_flip_refs),
            "complete_new_flip_certificates":self.flip_refs,
            "reused_R890_complete_flip_certificates":self.reused_flip_refs,
            "closed_work_retention_receipts":self.closed_refs,
            "completed_directions":sorted(map(int,self.completed_directions)),
            "original_direction_marked_principal_and_descent":self.completed_directions,
            "actual_all_126_new_complete_normal418_spaces_certified":len(self.flip_refs)==126,
            "actual_original_all_five_I_Z_bounded_representatives_certified":len(self.completed_directions)==5,
            "actual_original_all_five_t_leading_coefficients_computed":len(self.completed_directions)==5,
            "actual_all_five_exact_Galois_descent_data_recorded":len(self.completed_directions)==5,
            "original_Q_rho_orders":{str(j):RHO_ORDERS[j-1] for j in sorted(map(int,self.completed_directions))},
            "terminal_divisors_or_bases_claimed_K_fixed":False,
            "descent_matrices_or_K_fixed_bases_computed":False,
            "old_sources_original_conjugates_or_two_R890_flips_recomputed":False,
            "original_selected_scalars_rescaled_to_one":False,
            "characteristic_zero_RR_coordinates_reconstructed":False,
            "real_descent_cubed_ideal_claimed_equal_to_I_Z":False,
            "Hecke_norm_RR128_144_connection_period_nonp_or_height_computed":False,
            "actual_retained_complete_math_stage_count":count,
            "historical_discarded_intermediate_stage_count":discarded,
            "stage_manifest":inventory,"resume_state":self.current,
            "stop_reason":reason,"seconds":time.monotonic()-self.started}
        save(self.out/FINAL,final)
        return final

    def run(self):
        existing=self.out/FINAL
        if existing.exists():
            cert=read(existing)
            assert cert["result"]==RESULT and cert["configuration"]==self.tag
            if cert["complete"] is True:
                inventory=self.own(cert["stage_manifest"])
                for row in inventory["files"]:
                    assert spec(self.out/row["file"])==plain(row)
                return cert
        self.prepare()
        assert 1<=self.item["maximum_product_anchors"]<=418
        assert 1<=self.item["maximum_pencil_trials"]<=1000
        limit=int(self.item.get("maximum_new_flips",126));assert 1<=limit<=126
        for index,(new,left,right) in enumerate(self.chain,1):
            if index>limit:
                raise SearchStop("Requested finite original flip prefix completed; remaining fixed DAG retained.")
            ref=super().one_flip(index,new,left,right)
            expected=self.plan["nodes"][index-1]
            if expected["family"]=="shared_X":
                assert self.spaces[new]["kappa"]==[expected["expected_coefficient"]]+[0]*36
            elif expected["family"]=="shared_T":
                assert self.spaces[new]["kappa"]==[0,expected["expected_coefficient"]]+[0]*35
            if new in ("Z1","Z2","Z3","Z4","Z5"):
                self.marked_direction(int(new[1:]))
            self.close_completed_work(index,new,ref)
            self.release_finished_memory(index)
        return self.finish(True,None)

def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise SystemExit("R901 mathematics only runs in the authorized public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    for key in ("config","retained","output"):
        parser.add_argument("--"+key,required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args();assert 0<args.budget_minutes<=300
    started=time.monotonic();out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    job=None;certificate=None;code=1;error=None
    try:
        job=Job(args);certificate=job.run();code=0 if certificate["complete"] else 2
    except BudgetStop as exc:
        code=124;error={"type":"BudgetStop","message":str(exc)}
    except (UnitFailure,SearchStop) as exc:
        code=2;error={"type":type(exc).__name__,"message":str(exc)}
    except Exception as exc:
        error={"type":type(exc).__name__,"message":str(exc)};traceback.print_exc()
    if certificate is None and job is not None:
        try:
            certificate=job.finish(False,error)
        except Exception:
            traceback.print_exc()
    receipt={"result":RESULT,"source_sha256":sha(__file__),"complete":code==0,
        "process_exit_code":code,"error":error,"seconds":time.monotonic()-started,
        "configuration_sha256":None if job is None else fingerprint(job.tag),
        "certificate_sha256":sha(out/FINAL) if (out/FINAL).exists() else None,
        "actual_new_complete_flip_count":0 if certificate is None else certificate["actual_new_complete_flip_count"],
        "actual_reused_R890_complete_flip_count":0 if certificate is None else certificate["actual_reused_R890_complete_flip_count"],
        "completed_directions":[] if certificate is None else certificate["completed_directions"],
        "actual_original_all_five_I_Z_bounded_representatives_certified":bool(certificate and certificate["actual_original_all_five_I_Z_bounded_representatives_certified"]),
        "old_source_mathematics_or_original_conjugates_recomputed":False,
        "new_mathematics_only_in_public_Actions":True}
    save(out/"core-receipt.json",receipt)
    print("R901_CORE_RECEIPT="+json.dumps(receipt,sort_keys=True),flush=True)
    raise SystemExit(code)

if __name__=="__main__":
    main()
