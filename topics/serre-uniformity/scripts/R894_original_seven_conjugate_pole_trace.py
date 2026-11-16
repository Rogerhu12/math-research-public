#!/usr/bin/env python3
"""R894: original seven-conjugate pole trace, using the frozen R890 flip."""
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
RESULT="R894-original-seven-conjugate-pole-trace-bounded-descent"
FINAL="p41-original-seven-conjugate-pole-trace-certificate.json"
PREFIX="R894-"
LEGACY_FILE="R890_original_Ef_eight_flip_and_marked_frame.py"
LEGACY_SHA="da8498fc6ab0f143ba347f4a7dec91c7474bbe2520c349bf33a84bba8e65420f"
P=1000000753
EPS=[0]+[1]*144+[2]*127
OLD_GROUPS=("R887","R880","R872","R883","R827")
GROUPS=OLD_GROUPS+("R890","SIXD")
CLASS_ORDER=["Cstar-H"]+["sigma^%d(Dstar)-H"%j for j in range(7)]+["Dchi-H"]
TARGET=[-7]+[3]*7+[28]
NEW_CHAIN=(
    ("A1","D0","D1"),("A2","D2","D3"),("A3","A1","A2"),
    ("A4","A3","D4"),("A5","D5","D6"),("A6","A4","A5"),
    ("A7","A6","A6"),("A8","A7","H"),("A9","A8","A6"),
    ("B3","Cstar","H"),("B4","B3","X4"),("B5","B4","B4"),
    ("B6","B5","B5"),("B7","B6","B4"),("B8","B7","B5"),
    ("DN","A9","B8"))
STRATEGY={
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "original_b_branch_order_by_sigma_power":[0,6,1,2,4,3,5],
    "normal_basis_degrees":EPS,"normal_V3_dimension":690,
    "complete_divisor_space_dimension":418,"complete_U_dimension":146,
    "old_fibres":[0,1,2,3,4,5,6],"complete_fibre_length":1904,
    "original_W_Krylov_and_V3_fibres_recomputed":False,
    "legacy_flip_core_sha256":LEGACY_SHA,
    "legacy_flip_algebra_methods_used_without_monkey_patch":True,
    "product_image_rank":962,"membership_shape":[1884,690],
    "complete_relation_shape":[1904,1380],"complete_relation_kernel_dimension":418,
    "product_anchor_schedule":"unchanged ordered original left kernel columns",
    "pencil_schedule":"unchanged positive integer power combinations of complete U146",
    "P0_unit_selection":"unchanged first nonzero column, no scalar rescaling",
    "new_flip_chain":[list(x) for x in NEW_CHAIN],
    "reused_R890_nodes":{"X2":"flip-04-D2","X4":"flip-05-E"},
    "total_mathematical_flip_nodes":18,"new_mathematical_flip_nodes":16,
    "class_coordinate_order":CLASS_ORDER,"target_class_coordinates":TARGET,
    "principal_recurrence":"Fnew=1/(q*Fleft*Fright), repeated factors retained",
    "original_trace":"sum of seven original constant-field conjugate pole divisors",
    "target_identity":"T_f^0=(D_N-H)+div(Q_orbit*F_N), T_f^0=sum sigma^j(E_f)-8442P0",
    "Q_orbit":"product of seven unchanged original Qtilde conjugates",
    "actual_rho_order":-8435,"original_t_leading_exponent":8435,
    "t_power_source":"seventh power of the already certified c^1205",
    "descent_factor":"sigma(Q_N)/Q_N, not its inverse",
    "descent_space_identity":"Q_N*W_DN=H0(2H-T_f^0) tensor_K L",
    "terminal_divisor_or_basis_asserted_K_fixed":False,
    "Hecke_correspondence_norm_computed":False,
    "product_witness_compaction":"selected original 1904x962 product basis, exact column identities and inverse",
    "closed_work_retention":"only remove non-live scan work after complete flip certificate and atomic hash history",
    "active_or_pending_work_discarded":False,
    "only_budget_search_limits_disk_floor_and_transport_excluded_from_identity":True}

def own_sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(4*1024*1024),b""):
            h.update(block)
    return h.hexdigest()

legacy_path=Path(__file__).resolve().parent/LEGACY_FILE
assert own_sha(legacy_path)==LEGACY_SHA
description=importlib.util.spec_from_file_location("R894_frozen_R890_arithmetic",legacy_path)
L=importlib.util.module_from_spec(description)
description.loader.exec_module(L)
sha,read,save,fingerprint,plain,spec=L.sha,L.read,L.save,L.fingerprint,L.plain,L.spec
mat,rows,shape,eye,zero=L.mat,L.rows,L.shape,L.eye,L.zero
BudgetStop,UnitFailure,SearchStop=L.BudgetStop,L.UnitFailure,L.SearchStop

def group_ref(group,row):
    return {**plain(row),"source_group":group}

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],
        "python_flint":"0.9.0","p":41,"legacy_flip_core_sha256":LEGACY_SHA,
        "method_sha256":item["method_sha256"],"proofs":item["proofs"],
        "sources":{g:L.identity(item["sources"][g]) for g in GROUPS},
        "inputs":item["inputs"],"strategy":STRATEGY}

def live_refs(value):
    """Only literal live references; historical work is deliberately not live."""
    if isinstance(value,dict):
        if {"file","bytes","sha256"}<=set(value):
            yield value
            return
        for key,child in value.items():
            if key in ("configuration","discarded_intermediate_stage_history",
                       "historical_product_work","original_source_provenance"):
                continue
            yield from live_refs(child)
    elif isinstance(value,list):
        for child in value:
            yield from live_refs(child)

class Job(L.Job):
    def __init__(self,args):
        self.args=args;self.started=time.monotonic();self.out=Path(args.output)
        self.out.mkdir(parents=True,exist_ok=True);self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41
        assert self.item["producer_inputs_pending"] is False
        assert sha(__file__)==self.item["core_sha256"]
        assert L.flint.__version__=="0.9.0"
        assert self.item["legacy_core"]==LEGACY_FILE
        assert self.item["legacy_core_sha256"]==LEGACY_SHA
        topic=Path(__file__).resolve().parent.parent
        assert sha(topic/self.item["method"])==self.item["method_sha256"]
        for proof in self.item["proofs"].values():
            assert sha(topic/proof["path"])==proof["sha256"]
        assert set(self.item["sources"])==set(GROUPS)
        self.tag=expected_tag(self.item);self.refs={};self.flip_refs=[]
        self.reused_flip_refs=[];self.current=None;self.phase="source-initialization"
        self.sources={g:L.Source(g,self.item["sources"][g],args.retained) for g in GROUPS}
        self.inputs=self.item["inputs"];self.spaces={};self.space_cache={};self.fibres={}
        self.closed_refs=[];self.original_principals=[]

    def budget(self):
        if time.monotonic()-self.started>=self.args.budget_minutes*60-30:
            raise BudgetStop("R894 complete atomic stages retained; phase="+self.phase)
        if shutil.disk_usage(self.out).free<int(self.item.get("minimum_free_disk_bytes",768*1024*1024)):
            raise BudgetStop("R894 disk floor reached; current unclosed work and all live witnesses retained.")

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
        assert not any(key in value for key in ("result","configuration","complete"))
        payload={"result":RESULT,"configuration":self.tag,"complete":True,**value}
        path=self.path(name)
        if path.exists():
            assert read(path)==payload
        else:
            save(path,payload)
        self.refs[name]=spec(path)
        print("R894_STAGE="+json.dumps({"file":path.name,"seconds":time.monotonic()-self.started}),flush=True)
        return payload

    def checkpoint(self,phase):
        self.phase=phase
        value={"result":RESULT,"configuration":self.tag,"complete":False,"phase":phase,
            "retained_complete_stages":self.refs,
            "complete_new_flip_certificates":self.flip_refs,
            "reused_R890_complete_flip_certificates":self.reused_flip_refs,
            "closed_work_retention_receipts":self.closed_refs}
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

    def prepare(self):
        self.V3=L.positions(3);self.V2=L.positions(2)
        assert len(self.V3)==690 and len(self.V2)==418
        old=self.sources["R890"]
        cert=old.certificate
        assert cert["actual_all_eight_complete_normal418_spaces_certified"] is True
        assert cert["actual_original_Ef_bounded_divisor_identity_certified"] is True
        assert cert["actual_complete_flip_count"]==8
        assert old.tag["source_sha256"]==LEGACY_SHA
        for group in OLD_GROUPS:
            assert L.identity(self.item["sources"][group])==old.tag["sources"][group]
        old_inputs=old.tag["inputs"]
        for key,row in old_inputs.items():
            assert self.inputs[key]==row
        self.points={}
        for z,row in enumerate(self.inputs["original_Krylov_points"]):
            point=self.external(row)
            assert point["prime"]==P and point["z0"]==z and point["usable"] is True
            assert point["actual_cyclic_rank"]==272
            assert point["both_inverse_products_verified"] is True
            assert plain(point["source_original_W"])==plain(self.inputs["original_W"])
            self.points[z]=point
        assert len(self.points)==7
        self.W=self.source("original_W");self.place=self.source("original_place")
        assert self.W["prime"]==self.place["prime"]==P
        assert self.place["original_zeta_root"]==549966761
        self.Qtilde=self.source("Qtilde");self.frame=self.source("t_frame")
        assert self.Qtilde["actual_rho_order"]==-1205
        assert self.Qtilde["actual_leading_coefficient_mod_prime"]==267133051
        assert self.frame["original_t_first_order_unit_certified"] is True
        assert self.frame["original_t_over_rho_constant_mod_prime"]==354813668
        assert self.frame["actual_c_powers_mod_prime"]["1205"]==201313487
        assert self.frame["original_s_root"]==99932770
        for key,field in (("Cstar","source_complete_Cstar_418"),
                          ("Dstar","source_complete_original_Dstar_418"),
                          ("Dchi","source_complete_original_Dchi_418")):
            assert plain(self.Qtilde[field])==plain(self.inputs[key])
        neutral=self.source("R890_neutral")
        assert neutral["neutral_avoids_original_P0"] is True
        assert neutral["tau_V2_is_complete_W_H"] is True
        assert neutral["source_original_point"]==old_inputs["point_linear_functional"]
        assert neutral["source_original_V2_jets"]==old_inputs["point_jets"]
        shape(neutral["neutral_W_H_normal_V3_basis_mod_prime"],690,418)
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
        self.spaces["H"]={"matrix":mat(alias["neutral_W_H_normal_V3_basis_mod_prime"]),
            "reference":self.refs[name],"kappa":[0]*9,"Fvalue":1,
            "function":{"operation":"one_for_original_neutral_H","source":self.inputs["R890_neutral"]}}
        for label,key,position in (("Cstar","Cstar",0),("D0","Dstar",1)):
            value=self.source(key)
            shape(value["normal_V3_basis_mod_prime"],690,418)
            assert value["actual_projected_rank"]==418 and value["complete_RR_space_certified"] is True
            coordinates=[0]*9;coordinates[position]=1
            self.spaces[label]={"matrix":mat(value["normal_V3_basis_mod_prime"]),
                "reference":self.inputs[key],"kappa":coordinates,"Fvalue":1,
                "function":{"operation":"one_for_original_initial_representative","source":self.inputs[key]}}
        self.original_principals=[{
            "sigma_power":0,"original_branch":0,"source":self.inputs["Qtilde"],
            "rho_leading_mod_prime":self.Qtilde["actual_leading_coefficient_mod_prime"]}]
        six=self.sources["SIXD"];sixcert=six.certificate
        assert sixcert["all_seven_original_Dstar_inputs_certified"] is True
        assert sixcert["all_six_new_Dstar_418_spaces_certified"] is True
        assert sixcert["actual_new_complete_Dstar_count"]==6
        assert plain(sixcert["original_branch_zero_Dstar"])==plain(self.inputs["Dstar"])
        assert plain(sixcert["original_branch_zero_Qtilde"])==plain(self.inputs["Qtilde"])
        assert plain(sixcert["common_Cstar_418"])==plain(self.inputs["Cstar"])
        assert plain(sixcert["common_Dchi_418"])==plain(self.inputs["Dchi"])
        audit=self.source("sixD_source_audit")
        assert audit["exact_objects_are_conjugates_of_original_characteristic_zero_unit_solves"] is True
        assert audit["original_selected_charts_and_all_free_coordinates_unchanged"] is True
        assert audit["original_sigma_powers"]==[1,2,3,4,5,6]
        assert audit["original_branches"]==[6,1,2,4,3,5]
        for group in ("R827","R872","R880","R887"):
            L.same_source(audit["source_identities"][group],self.item["sources"][group])
        assert len(self.inputs["six_Dstar_branches"])==6
        for j,row in enumerate(self.inputs["six_Dstar_branches"],1):
            record=sixcert["completed_new_conjugate_inputs"][j-1]
            assert record["sigma_power"]==row["sigma_power"]==j
            assert record["original_branch"]==row["original_branch"]==[0,6,1,2,4,3,5][j]
            assert plain(record["stage"])==plain(row["complete"])
            completed=self.external(row["complete"]);basis=self.external(row["space"])
            principal=self.external(row["principal"])
            assert completed["same_original_zero_branch_unit_diagram_conjugated"] is True
            assert completed["complete_original_conjugate_Dstar_418_certified"] is True
            assert completed["original_branch"]==principal["original_branch"]==row["original_branch"]
            assert completed["sigma_power"]==principal["sigma_power"]==j
            assert completed["roots_B_s"]==principal["roots_B_s"]==record["roots_B_s"]
            assert record["roots_B_s"][1]==99932770
            assert plain(completed["complete_Dstar_418_basis"])==plain(row["space"])
            assert plain(completed["original_principal_input"])==plain(row["principal"])
            assert plain(principal["source_complete_Dstar"])==plain(row["space"])
            assert plain(principal["source_complete_common_Cstar"])==plain(self.inputs["Cstar"])
            assert plain(principal["source_complete_common_Dchi"])==plain(self.inputs["Dchi"])
            assert plain(principal["source_original_zero_branch_Qtilde"])==plain(self.inputs["Qtilde"])
            assert principal["exact_original_Galois_conjugate_not_a_new_linearly_equivalent_choice"] is True
            assert principal["all_original_free_coordinates_and_section_scales_preserved"] is True
            assert principal["actual_rho_order"]==-1205
            assert principal["principal_factor_direction"]=="positive multiplication"
            shape(basis["normal_V3_basis_mod_prime"],690,418)
            assert basis["actual_projected_rank"]==418 and basis["complete_RR_space_certified"] is True
            coordinates=[0]*9;coordinates[1+j]=1
            label="D"+str(j)
            self.spaces[label]={"matrix":mat(basis["normal_V3_basis_mod_prime"]),
                "reference":row["space"],"kappa":coordinates,"Fvalue":1,
                "function":{"operation":"one_for_same_original_Galois_representative",
                            "source":row["space"],"sigma_power":j}}
            self.original_principals.append({
                "sigma_power":j,"original_branch":row["original_branch"],
                "source":row["principal"],"rho_leading_mod_prime":principal["actual_leading_coefficient_mod_prime"]})
        self.reuse_original_chi_flips()
        self.normal_fibres()
        name="original-source-audit"
        if self.old(name) is None:
            self.put(name,{
                "prime":P,"sources":{g:L.identity(self.item["sources"][g]) for g in GROUPS},
                "inputs":self.inputs,"legacy_flip_core_sha256":LEGACY_SHA,
                "original_sigma_branch_order":[0,6,1,2,4,3,5],
                "all_seven_same_original_Galois_Dstar_spaces_bound":True,
                "source_original_six_Dstar_conjugacy_audit":self.inputs["sixD_source_audit"],
                "two_completed_R890_chi_flips_reused":self.reused_flip_refs,
                "old_W_Krylov_V3_fibres_P0_and_normal_spaces_recomputed":False,
                "original_selected_scalars_preserved_without_rescaling":True,
                "class_coordinate_order":CLASS_ORDER,"target_class_coordinates":TARGET,
                "all_new_mathematics_only_in_public_Actions":True})
        self.checkpoint("complete-original-sources-and-two-reused-flips")

    def reuse_original_chi_flips(self):
        old=self.sources["R890"]
        self.reused_flip_refs=[]
        for label,oldlabel,index,coordinate in (("X2","D2",4,-2),("X4","E",5,4)):
            row=self.inputs["reused_complete_flips"][label]
            assert plain(row) in [plain(x) for x in old.certificate["complete_flip_certificates"]]
            completed=self.external(row)
            assert completed["flip_index"]==index and completed["new_space_label"]==oldlabel
            assert completed["actual_complete_space_dimension"]==418
            assert completed["all1904_by418_pencil_relations_verified"] is True
            assert completed["all1884_by146_membership_relations_verified"] is True
            assert completed["effective_degree272_and_original_P0_avoidance_certified"] is True
            basis_ref=group_ref("R890",completed["complete_normal418_space"])
            principal_ref=group_ref("R890",completed["principal_function_and_P0_unit"])
            u_ref=group_ref("R890",completed["original_unscaled_P0_unit_section"])
            basis=self.external(basis_ref);principal=self.external(principal_ref);u=self.external(u_ref)
            assert principal["new_original_class_coefficients"]==[0,0,coordinate]
            assert principal["class_coordinate_order"]==["Cstar-H","Dstar-H","Dchi-H"]
            assert principal["F_P0_unit_inverse_product_verified"] is True
            assert principal["all_selected_original_scalars_retained"] is True
            assert principal["original_rho_order_of_F"]==0
            assert plain(principal["source_complete_new_normal418"])==plain(basis_ref)
            assert plain(principal["source_original_unscaled_u"])==plain(u_ref)
            assert u["original_scalar_not_rescaled"] is True and u["q_P0_value_is_unit"] is True
            assert principal["q_P0_value_mod_prime"]==u["q_P0_value_mod_prime"]
            assert 0<principal["F_P0_value_mod_prime"]<P
            shape(basis["normal_V3_basis_mod_prime"],690,418)
            assert basis["complete_RR_space_certified"] is True
            coordinates=[0]*9;coordinates[-1]=coordinate
            self.spaces[label]={"matrix":mat(basis["normal_V3_basis_mod_prime"]),
                "reference":basis_ref,"kappa":coordinates,
                "Fvalue":principal["F_P0_value_mod_prime"],
                "function":{"operation":"external_original_exact_principal_function_DAG",
                    "source":principal_ref,"original_coordinate_order":principal["class_coordinate_order"]}}
            self.reused_flip_refs.append(row)
        d2=self.external(self.inputs["reused_complete_flips"]["X2"])
        e=self.external(self.inputs["reused_complete_flips"]["X4"])
        assert plain(d2["left_complete_space"])==plain(self.inputs["Dchi"])
        assert plain(d2["right_complete_space"])==plain(self.inputs["Dchi"])
        assert plain(e["left_complete_space"])==plain(d2["complete_normal418_space"])
        assert plain(e["right_complete_space"])==plain(d2["complete_normal418_space"])

    def normal_fibres(self):
        assert len(self.inputs["R890_normal_fibres"])==7
        for z,row in enumerate(self.inputs["R890_normal_fibres"]):
            value=self.external(row)
            assert value["z0"]==z and value["prime"]==P
            assert plain(value["source_original_Krylov_point"])==plain(self.inputs["original_Krylov_points"][z])
            assert plain(value["source_original_W"])==plain(self.inputs["original_W"])
            assert value["normal_integer_scale_applied_again"] is False
            shape(value["normal_evaluation_mod_prime"],272,690)
            shape(value["cyclic_evaluation_mod_prime"],272,690)
            self.fibres[z]={"E":mat(value["normal_evaluation_mod_prime"]),
                "C":mat(value["cyclic_evaluation_mod_prime"]),
                "W":mat(self.points[z]["W_evaluated_mod_prime"]),"reference":row}

    def space_fibre(self,label,z):
        if label not in self.inputs["R890_cached_space_fibres"]:
            return super().space_fibre(label,z)
        key=(label,z)
        if key not in self.space_cache:
            ref=self.inputs["R890_cached_space_fibres"][label][z]
            value=self.external(ref)
            assert value["prime"]==P and value["z0"]==z
            assert plain(value["source_complete_normal_V3_fibre"])==plain(self.inputs["R890_normal_fibres"][z])
            if label=="H":
                assert plain(value["source_complete_normal418_space"])==plain(self.inputs["R890_neutral"])
            elif label=="X4":
                assert plain(value["source_complete_normal418_space"])==plain(self.spaces[label]["reference"])
            else:
                raise AssertionError("Only actual old H and X4/E fibre arrays are aliases.")
            shape(value["normal_evaluation_mod_prime"],272,418)
            shape(value["cyclic_evaluation_mod_prime"],272,418)
            self.space_cache[key]=(mat(value["normal_evaluation_mod_prime"]),
                mat(value["cyclic_evaluation_mod_prime"]),ref)
        return self.space_cache[key]

    def product_span(self,stem,left,right):
        compact_name=stem+"-complete-product-image-962-compact"
        compact=self.old(compact_name)
        if compact is not None:
            assert compact["left_complete_space"]==self.spaces[left]["reference"]
            assert compact["right_complete_space"]==self.spaces[right]["reference"]
            shape(compact["selected_product_basis_mod_prime"],1904,962)
            shape(compact["inverse_selected_minor_mod_prime"],962,962)
            return (mat(compact["selected_product_basis_mod_prime"]),
                mat(compact["inverse_selected_minor_mod_prime"]),
                compact["selected_rows"],self.refs[compact_name])
        basis,inverse,I,original_ref=super().product_span(stem,left,right)
        original=self.own(original_ref)
        state=self.own(original["selected_span_state"])
        assert state["actual_rank"]==962 and state["selected_rows"]==I
        products=[]
        for block in state["selected_blocks"]:
            assert len(block["source_fibre_products"])==7
            first=self.own(block["source_fibre_products"][0])
            anchor=self.own(first["source_anchor"])
            definition=anchor["exact_anchor_definition"]
            assert definition["operation"]=="unchanged_original_kernel_column"
            assert definition["source_complete_space"]==self.spaces[left]["reference"]
            right_columns=block["selected_columns"]
            assert all(0<=int(j)<418 for j in right_columns)
            for z,ref in enumerate(block["source_fibre_products"]):
                value=self.own(ref)
                assert value["source_anchor"]==first["source_anchor"] and value["z0"]==z
                expected=self.space_fibre(right,z)[2]
                assert value["other_complete_space"]==expected
            products.append({"left_original_kernel_column":definition["column"],
                             "right_original_kernel_columns":right_columns})
        assert sum(len(x["right_original_kernel_columns"]) for x in products)==962
        # These arrays are copied from the already verified complete selected span.
        # No product, rank profile or inverse is evaluated a second time.
        compact=self.put(compact_name,{
            "prime":P,"left_complete_space":self.spaces[left]["reference"],
            "right_complete_space":self.spaces[right]["reference"],
            "selected_original_product_columns_in_order":products,
            "source_original_normal_fibres":[self.fibres[z]["reference"] for z in range(7)],
            "source_original_Krylov_points":self.inputs["original_Krylov_points"],
            "matrix_shape":[1904,962],"selected_product_basis_mod_prime":rows(basis),
            "selected_rows":I,"inverse_selected_minor_mod_prime":rows(inverse),
            "actual_product_image_dimension":962,
            "both_complete_selected_inverse_products_verified_in_frozen_method":True,
            "complete_product_image_is_H0_6H_minus_D1_minus_D2":True,
            "all1904_original_fibre_rows_retained":True,
            "number_of_original_left_anchors_used":original["number_of_original_left_anchors_used"],
            "exact_selected_product_definition":"left original kernel column times right original kernel column, in listed order",
            "exact_unit_solve_sources_closed_by_two_complete_parent_spaces":True,
            "already_computed_products_rank_profiles_and_inverses_recomputed":False,
            "historical_product_work":{"basename":original_ref["file"],"bytes":original_ref["bytes"],
                "sha256":original_ref["sha256"],"not_a_live_dependency":True}})
        return basis,inverse,I,self.refs[compact_name]

    def principal_step(self,stem,new,left,right,u,uref,space_ref):
        name=stem+"-principal-function-and-P0-unit"
        value=self.old(name);a=self.spaces[left];b=self.spaces[right]
        if value is None:
            self.budget()
            q0=int(u["q_P0_value_mod_prime"])
            assert 0<q0<P and 0<a["Fvalue"]<P and 0<b["Fvalue"]<P
            denominator=q0*a["Fvalue"]%P*b["Fvalue"]%P
            F0=pow(denominator,-1,P);assert denominator*F0%P==1
            coordinates=[-x-y for x,y in zip(a["kappa"],b["kappa"])]
            assert len(coordinates)==9
            value=self.put(name,{
                "prime":P,"new_space_label":new,"left_space_label":left,"right_space_label":right,
                "source_left_complete_space":a["reference"],"source_right_complete_space":b["reference"],
                "source_original_unscaled_u":uref,"source_complete_new_normal418":space_ref,
                "left_original_class_coefficients":a["kappa"],
                "right_original_class_coefficients":b["kappa"],
                "new_original_class_coefficients":coordinates,"class_coordinate_order":CLASS_ORDER,
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
            if not name.startswith(PREFIX):
                raise AssertionError("External source must retain its explicit source_group: "+name)
            if name in seen:
                assert seen[name]==plain(row)
                continue
            value=self.own(row);seen[name]=plain(row)
            for child in live_refs(value):
                if child.get("source_group") is not None:
                    # Completed producers preserve their complete original proof
                    # provenance; only declared selected external inputs are read here.
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
        old=self.old(name)
        keep=self.closed_witness_files(certificate)
        candidates=[path for path in sorted(self.out.glob(PREFIX+stem+"-*.json.gz"))
                    if path.name!=self.path(name).name]
        if old is None:
            discarded=[spec(path) for path in candidates if path.name not in keep]
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
            assert row["file"].startswith(PREFIX+stem+"-")
            assert row["file"] not in keep and row["file"]!=self.path(name).name
            path=self.out/row["file"]
            if path.exists():
                assert spec(path)==plain(row)
                path.unlink()
            short=row["file"][len(PREFIX):-len(".json.gz")]
            self.refs.pop(short,None)
        self.closed_refs.append(self.refs[name])
        self.checkpoint("closed-"+stem)

    def marked_trace_and_descent(self):
        name="original-seven-pole-trace-marked-principal-and-descent"
        value=self.old(name)
        terminal=self.spaces["DN"]
        if value is None:
            self.budget()
            assert terminal["kappa"]==TARGET and len(self.flip_refs)==16
            assert len(self.reused_flip_refs)==2 and len(self.original_principals)==7
            orbit_leading=1
            for row in self.original_principals:
                unit=int(row["rho_leading_mod_prime"]);assert 0<unit<P
                orbit_leading=orbit_leading*unit%P
            correction=terminal["Fvalue"]
            rho_leading=orbit_leading*correction%P
            c1205=int(self.frame["actual_c_powers_mod_prime"]["1205"])
            c8435=pow(c1205,7,P);t_leading=rho_leading*c8435%P
            assert rho_leading and t_leading
            orbit={"operation":"product_of_all_seven_original_Galois_Qtilde",
                   "factors":[{"operation":"original_Qtilde_conjugate","sigma_power":x["sigma_power"],
                               "source":x["source"]} for x in self.original_principals],
                   "constant_field_Galois_orbit_order":[0,6,1,2,4,3,5],
                   "source_fixed_chart_conjugacy":self.inputs["sixD_source_audit"]}
            QN={"operation":"multiply","left":orbit,"right":terminal["function"]}
            gamma_QN={"operation":"apply_original_constant_field_sigma_to_every_function_and_unit_solve_leaf",
                      "power":1,"input":QN,"source_fixed_chart_conjugacy":self.inputs["sixD_source_audit"],
                      "Y_normal_generators_fixed":True,
                      "original_selected_rows_columns_and_integer_parameters_unchanged":True}
            gamma_F={"operation":"apply_original_constant_field_sigma_to_every_function_and_unit_solve_leaf",
                     "power":1,"input":terminal["function"],
                     "source_fixed_chart_conjugacy":self.inputs["sixD_source_audit"]}
            transition={"operation":"divide","numerator":gamma_QN,"denominator":QN}
            value=self.put(name,{
                "prime":P,"source_all_new_complete_flips":self.flip_refs,
                "source_two_reused_R890_flips":self.reused_flip_refs,
                "source_all_seven_original_principals":self.original_principals,
                "source_complete_DN_normal418":terminal["reference"],
                "source_original_t_frame":self.inputs["t_frame"],
                "class_coordinate_order":CLASS_ORDER,"target_original_class_coefficients":TARGET,
                "exact_original_trace_divisor":"T_f^0=sum_(j=0)^6 sigma^j(E_f)-8442P0",
                "original_unbased_trace_degree":8442,"degree_zero_trace_degree":0,"exact_Q_orbit_function_DAG":orbit,
                "Q_orbit_fixed_by_original_Gal_L_over_K":True,
                "exact_QN_function_DAG":QN,
                "exact_original_divisor_identity":"T_f^0=(D_N-H)+div(Q_N)",
                "original_fractional_ideal_principal_factor_direction":"positive multiplication by Q_N",
                "exact_original_ideal_identity":"I_(T_f^0)=Q_N*I_DN*I_H_inverse",
                "DN_effective_degree":272,"DN_avoids_original_P0":True,
                "complete_W_DN_dimension":418,"complete_W_DN_definition":"H0(3H-D_N)",
                "actual_Q_orbit_rho_order":-8435,"actual_rho_order":-8435,
                "actual_Q_orbit_rho_leading_mod_prime":orbit_leading,
                "actual_terminal_F_P0_unit_mod_prime":correction,
                "actual_QN_rho_leading_mod_prime":rho_leading,
                "actual_original_c_power1205_mod_prime":c1205,
                "actual_original_c_power8435_mod_prime":c8435,
                "actual_QN_t_leading_mod_prime":t_leading,
                "exact_t_leading_expression":{"operation":"multiply","factors":[
                    {"operation":"product_original_seven_Qtilde_leading_coefficients",
                     "sources":[x["source"] for x in self.original_principals]},
                    {"operation":"original_F_at_P0","source":terminal["function"]},
                    {"operation":"power","exponent":7,"input":{
                        "operation":"already_certified_original_c_power1205","source":self.inputs["t_frame"]}}]},
                "exact_descent_transition_function_DAG":transition,
                "equivalent_descent_transition_using_F_DAG":{"operation":"divide",
                    "numerator":gamma_F,"denominator":terminal["function"]},
                "descent_divisor_identity":"div(sigma(Q_N)/Q_N)=D_N-sigma(D_N)",
                "exact_semilinear_action":"s -> (sigma(Q_N)/Q_N)*sigma(s)",
                "exact_sevenfold_cocycle":"product_(j=0)^6 sigma^j(sigma(Q_N)/Q_N)=1 by telescoping",
                "K_descent_identification":"Q_N*W_DN=H0(2H-T_f^0) tensor_K L",
                "terminal_DN_or_normal418_basis_claimed_K_fixed":False,
                "descent_matrix_or_K_fixed_basis_computed":False,
                "Hecke_correspondence_norm_computed":False,
                "all_eighteen_original_unscaled_q_P0_units_preserved":True,
                "original_c_or_t_jets_recomputed":False,
                "auxiliary_units_asserted_to_be_41_adic_units":False,
                "characteristic_zero_RR_coefficients_or_leading_scalar_expanded":False,
                "five_original_Lj_RR128_or144_computed":False,
                "connection_nonp_period_or_height_computed":False})
        assert value["source_all_new_complete_flips"]==self.flip_refs
        assert value["source_complete_DN_normal418"]==terminal["reference"]
        assert value["source_two_reused_R890_flips"]==self.reused_flip_refs
        self.checkpoint("complete-original-seven-pole-trace-and-descent")
        return self.refs[name]

    def inventory(self):
        entries=[];histories=[];discarded_count=0
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name==PREFIX+"current.json.gz" or path.name.startswith(PREFIX+"stage-manifest-"):
                continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag
            assert value["complete"] is True
            row=spec(path);entries.append(row)
            if "discarded_intermediate_stage_history" in value:
                histories.append(row);discarded_count+=value["discarded_intermediate_count"]
        payload={"result":RESULT,"configuration":self.tag,"complete":True,
            "files":entries,"current_excluded":True,
            "all_required_live_witnesses_and_unclosed_work_retained":True,
            "closed_work_retention_receipts":histories,
            "historical_discarded_intermediate_count":discarded_count,
            "historical_hashes_not_claimed_as_present_files":True}
        path=self.path("stage-manifest-"+fingerprint(payload))
        if path.exists():
            assert read(path)==payload
        else:
            save(path,payload)
        return spec(path),len(entries),discarded_count

    def finish(self,complete,reason):
        self.checkpoint("completed" if complete else self.phase)
        inventory,count,discarded_count=self.inventory()
        marked=self.refs.get("original-seven-pole-trace-marked-principal-and-descent")
        if complete:
            assert len(self.flip_refs)==16 and len(self.reused_flip_refs)==2 and marked is not None
            assert self.spaces["DN"]["kappa"]==TARGET
            assert len(self.closed_refs)==16
        certificate={"result":RESULT,"configuration":self.tag,"complete":bool(complete),
            "p":41,"actual_auxiliary_prime":P,
            "source_audit":self.refs.get("original-source-audit"),
            "actual_new_complete_flip_count":len(self.flip_refs),
            "actual_reused_R890_complete_flip_count":len(self.reused_flip_refs),
            "actual_total_complete_flip_count":len(self.flip_refs)+len(self.reused_flip_refs),
            "complete_new_flip_certificates":self.flip_refs,
            "reused_R890_complete_flip_certificates":self.reused_flip_refs,
            "closed_work_retention_receipts":self.closed_refs,
            "marked_principal_and_descent":marked,
            "actual_all_sixteen_new_complete_normal418_spaces_certified":len(self.flip_refs)==16,
            "actual_original_seven_pole_trace_bounded_identity_certified":marked is not None,
            "actual_original_t_leading_coefficient_computed":marked is not None,
            "exact_original_Galois_descent_datum_recorded":marked is not None,
            "terminal_divisor_or_basis_claimed_K_fixed":False,
            "descent_matrix_or_K_fixed_basis_computed":False,
            "old_seven_Dstar_Cstar_Dchi_and_R890_two_flips_recomputed":False,
            "old_W_Krylov_V3_fibres_P0_jets_or_t_constant_recomputed":False,
            "original_selected_scalars_rescaled_to_one":False,
            "characteristic_zero_RR_coefficients_reconstructed":False,
            "Hecke_norm_five_Lj_RR128_RR144_connection_or_height_computed":False,
            "actual_retained_complete_math_stage_count":count,
            "historical_discarded_intermediate_stage_count":discarded_count,
            "stage_manifest":inventory,"resume_state":self.current,
            "stop_reason":reason,"seconds":time.monotonic()-self.started}
        save(self.out/FINAL,certificate)
        return certificate

    def run(self):
        self.prepare()
        assert 1<=self.item["maximum_product_anchors"]<=418
        assert 1<=self.item["maximum_pencil_trials"]<=1000
        limit=int(self.item.get("maximum_new_flips",16));assert 1<=limit<=16
        for index,(new,left,right) in enumerate(NEW_CHAIN,1):
            if index>limit:
                raise SearchStop("Requested finite new-flip prefix completed; remaining original chain retained.")
            ref=super().one_flip(index,new,left,right)
            self.close_completed_work(index,new,ref)
            # Keep only small future-used matrices; completed proof bytes remain in output.
            gc.collect()
        self.marked_trace_and_descent()
        return self.finish(True,None)

def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise SystemExit("R894 new mathematics only runs in the authorized public repository Actions.")
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
        "actual_original_seven_pole_trace_bounded_identity_certified":bool(certificate and certificate["actual_original_seven_pole_trace_bounded_identity_certified"]),
        "actual_original_t_leading_coefficient_computed":bool(certificate and certificate["actual_original_t_leading_coefficient_computed"]),
        "old_original_inputs_or_two_completed_R890_flips_recomputed":False,
        "new_mathematics_only_in_public_Actions":True}
    save(out/"core-receipt.json",receipt)
    print("R894_CORE_RECEIPT="+json.dumps(receipt,sort_keys=True),flush=True)
    raise SystemExit(code)

if __name__=="__main__":
    main()
