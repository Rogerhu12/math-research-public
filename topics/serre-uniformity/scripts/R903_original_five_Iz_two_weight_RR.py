#!/usr/bin/env python3
"""R903: original five I_Z two-weight RR spaces through one product image per direction."""
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
RESULT="R903-original-five-Iz-two-weight-RR-and-marked-frame"
FINAL="p41-original-five-Iz-two-weight-RR-certificate.json"
PREFIX="R903-"
LEGACY_FILE="R890_original_Ef_eight_flip_and_marked_frame.py"
LEGACY_SHA="da8498fc6ab0f143ba347f4a7dec91c7474bbe2520c349bf33a84bba8e65420f"
COMPACT_FILE="R894_original_seven_conjugate_pole_trace.py"
COMPACT_SHA="9a2793c79e552c04ea384f5c6bfb673e6e7d506ff91cf9e246fbc00a76f2da56"
R901_CORE_SHA="2cacb66f8b111746cdb8e51879f1c861e0aa59f0fb15d891c18c3c7c749fc920"
P=1000000753
EPS=[0]+[1]*144+[2]*127
GROUPS=("R827","R872","R880","R883","R890","R901")
RHO_ORDERS=[-686,-182,-231,-707,-1659]
STRATEGY={
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "normal_basis_degrees":EPS,"original_z_P0_mod_prime":110702704,
    "original_t_over_rho_mod_prime":354813668,
    "original_R901_core_sha256":R901_CORE_SHA,
    "legacy_product_core_sha256":LEGACY_SHA,"compact_product_core_sha256":COMPACT_SHA,
    "frozen_methods_imported_without_monkey_patch":True,
    "original_directions":[1,2,3,4,5],
    "original_line_bundle":"M_j=I_Zj(254P0), not the real-descent cubed ideal",
    "positive_global_multiplier":"Phi_j=QZ_j/qchi",
    "original_qchi_divisor":"Dchi-2H+272P0",
    "old_fibres":[0,1,2,3,4,5,6],"complete_fibre_length":1904,
    "old_V3_dimension":690,"new_V4_dimension":962,
    "single_product_image_dimension":962,"product_quotient_dimension":942,
    "membership_matrix_shapes":{"3":[1884,690],"4":[1884,962]},
    "two_anchor_powers":{"3":3,"4":2},"membership_rank":544,
    "complete_unpadded_dimensions":{"3":146,"4":418},
    "old_jet_orders_used":list(range(19)),"padding_orders":list(range(18)),
    "padded_dimensions":{"3":128,"4":400},
    "weight_one_prefix":"original tau*A128 followed by original sigma*A128",
    "weight_one_prefix_dimension":256,"weight_one_complement_dimension":144,
    "complement_rule":"canonical 400 coordinate rows; keep the original 256 columns and supplement original C columns",
    "complete_two_chart_rank":272,
    "normal_function_coordinates_divided_by_tau_again":False,
    "original_QZ_rho_orders":RHO_ORDERS,
    "selected_P0_column_not_rescaled":True,
    "t_frame_formula":"LCrho(QZ)*a18/LCrho(qchi) * c^(254-ord(QZ))",
    "complete_marked_QZ_source_tree_retained":True,
    "old_sources_W_Krylov_V3_fibres_Hensel_jets_or_126_flips_recomputed":False,
    "closed_product_work_retained_by_selected_columns_and_full_unit_solve":True,
    "split_trial_scope":"only the seven already completed whole fibres; a failed trial is not a negative Picard conclusion",
    "all_new_mathematics_only_in_public_Actions":True,
    "bounds_budget_search_prefix_and_transport_excluded_from_mathematical_identity":True}

def own_sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(4*1024*1024),b""):
            h.update(block)
    return h.hexdigest()

path=Path(__file__).resolve().parent/COMPACT_FILE
assert own_sha(path)==COMPACT_SHA
description=importlib.util.spec_from_file_location("R903_frozen_R894_product_compaction",path)
M=importlib.util.module_from_spec(description)
description.loader.exec_module(M)
L=M.L
assert own_sha(Path(__file__).resolve().parent/LEGACY_FILE)==LEGACY_SHA
sha,read,save,fingerprint,plain,spec=L.sha,L.read,L.save,L.fingerprint,L.plain,L.spec
mat,rows,shape,eye,zero,sub,hcat=L.mat,L.rows,L.shape,L.eye,L.zero,L.sub,L.hcat
BudgetStop,UnitFailure,SearchStop=L.BudgetStop,L.UnitFailure,L.SearchStop

def group_ref(group,row):
    return {**plain(row),"source_group":group}

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
        "legacy_product_core_sha256":LEGACY_SHA,"compact_product_core_sha256":COMPACT_SHA,
        "method_sha256":item["method_sha256"],"proofs":item["proofs"],
        "sources":{g:L.identity(item["sources"][g]) for g in GROUPS},
        "inputs":item["inputs"],"strategy":STRATEGY}

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
        assert set(self.item["sources"])==set(GROUPS)
        self.tag=expected_tag(self.item);self.refs={};self.closed_refs=[];self.current=None
        self.phase="source-initialization";self.completed_directions={}
        self.sources={g:L.Source(g,self.item["sources"][g],args.retained) for g in GROUPS}
        self.inputs=self.item["inputs"];self.spaces={};self.space_cache={};self.fibres={}
        self.weight4_fibres={};self.products={};self.QZ={}

    def budget(self):
        if time.monotonic()-self.started>=self.args.budget_minutes*60-30:
            raise BudgetStop("R903 complete atomic stages retained; phase="+self.phase)
        if shutil.disk_usage(self.out).free<int(self.item.get("minimum_free_disk_bytes",768*1024*1024)):
            raise BudgetStop("R903 disk floor; active or pending product work retained.")

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

    def put(self,name,value):
        assert not any(k in value for k in ("result","configuration","complete"))
        value={"result":RESULT,"configuration":self.tag,"complete":True,**value}
        path=self.path(name)
        if path.exists():
            assert read(path)==value
        else:
            save(path,value)
        self.refs[name]=spec(path)
        print("R903_STAGE="+json.dumps({"file":path.name,"seconds":time.monotonic()-self.started}),flush=True)
        return value

    def checkpoint(self,phase):
        self.phase=phase
        value={"result":RESULT,"configuration":self.tag,"complete":False,"phase":phase,
            "complete_direction_certificates":self.completed_directions,
            "closed_work_retention_receipts":self.closed_refs,"retained_complete_stages":self.refs}
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
        self.V3=L.positions(3);self.V4=L.positions(4)
        assert len(self.V3)==690 and len(self.V4)==962
        self.V3lookup={pair:i for i,pair in enumerate(self.V3)}
        self.V4lookup={pair:i for i,pair in enumerate(self.V4)}
        old=self.sources["R890"];old_inputs=old.tag["inputs"]
        assert old.tag["source_sha256"]==LEGACY_SHA
        assert old.certificate["actual_all_eight_complete_normal418_spaces_certified"] is True
        for group in ("R827","R872","R883"):
            L.same_source(old.tag["sources"][group],self.item["sources"][group])
        for key in ("Dchi","point_linear_functional","t_frame","original_W",
                    "original_grid","original_place","original_Krylov_points"):
            assert self.inputs[key]==old_inputs[key]
        self.W=self.source("original_W");self.place=self.source("original_place")
        assert self.W["prime"]==self.place["prime"]==P
        assert self.place["original_zeta_root"]==549966761
        self.grid=self.source("original_grid")
        assert self.grid["points"][:7]==list(range(7))
        assert self.grid["all_eight_actual_determinants_nonzero"] is True
        self.points={}
        for z,row in enumerate(self.inputs["original_Krylov_points"]):
            point=self.external(row)
            assert plain(row)==plain(self.grid["Krylov_point_stages"][z])
            assert point["z0"]==z and point["prime"]==P and point["usable"] is True
            assert point["actual_cyclic_rank"]==272 and point["both_inverse_products_verified"] is True
            assert plain(point["source_original_W"])==plain(self.inputs["original_W"])
            self.points[z]=point
        assert len(self.points)==7
        point=self.source("point_linear_functional")
        assert point["chosen_local_parameter"]=="z_minus_z0" and point["z0_mod_prime"]==110702704
        self.zP0=int(point["z0_mod_prime"])
        self.frame=self.source("t_frame")
        assert self.frame["original_t_first_order_unit_certified"] is True
        assert self.frame["original_s_root"]==99932770
        assert self.frame["original_t_over_rho_constant_mod_prime"]==354813668
        self.c=int(self.frame["original_t_over_rho_constant_mod_prime"])
        chi=self.source("Dchi")
        assert chi["full_characteristic_zero_dimension"]==418
        assert chi["all1234_by418_complete_V5_relations_zero"] is True
        assert chi["normal_integer_scale_applied_again"] is False
        shape(chi["V3_kernel_basis_mod_prime"],690,418)
        self.spaces["X"]={"matrix":mat(chi["V3_kernel_basis_mod_prime"]),"reference":self.inputs["Dchi"]}
        self.qchi=self.source("qchi_anchor");fixed=self.source("fixed_chi_divisor")
        r872=self.sources["R872"].certificate
        assert plain(r872["anchor_u"])==plain(self.inputs["qchi_anchor"])
        assert plain(r872["fixed_chi_divisor_and_principal_function"])==plain(self.inputs["fixed_chi_divisor"])
        assert plain(fixed["source_exact_u"])==plain(self.inputs["qchi_anchor"])
        assert plain(fixed["source_complete_W_Dchi"])==plain(self.inputs["Dchi"])
        assert fixed["D_chi_effective_and_avoids_original_P0"] is True
        assert fixed["actual_complete_fixed_chi_RR_space_certified"] is True
        assert fixed["principal_function"]["tau_power"]==2
        assert fixed["principal_function"]["no_additional_scalar_or_82_power"] is True
        assert self.qchi["role"]=="u" and self.qchi["order272_is_exact"] is True
        assert self.qchi["vanishes_at_original_P0_to_order_at_least272"] is True
        assert self.qchi["normal_integer_scale_applied_again"] is False
        self.qchi_lc=int(self.qchi["exact_order272_unit"]);assert 0<self.qchi_lc<P
        self.jets=self.source("normal_V3_point_jets")
        assert self.jets["matrix_shape"]==[252,690]
        assert self.jets["V3_basis"]==[{"normal_basis_row":i,"power_of_z":k} for i,k in self.V3]
        assert self.jets["row_orders"]==list(range(252)) and self.jets["local_parameter"]=="z_minus_z0"
        assert self.jets["no_original_Hensel_step_recomputed"] is True
        shape(self.jets["matrix_mod_prime"],252,690)
        self.J3=mat(self.jets["matrix_mod_prime"][:19])
        self.point_row=mat([self.jets["matrix_mod_prime"][0]])
        producer=self.sources["R901"];cert=producer.certificate
        assert producer.tag["source_sha256"]==R901_CORE_SHA
        assert cert["actual_new_complete_flip_count"]==126
        assert cert["actual_original_all_five_I_Z_bounded_representatives_certified"] is True
        assert cert["actual_original_all_five_t_leading_coefficients_computed"] is True
        assert cert["actual_all_five_exact_Galois_descent_data_recorded"] is True
        for group in ("R827","R872","R883","R890"):
            L.same_source(producer.tag["sources"][group],self.item["sources"][group])
        assert self.inputs["R890_cached_space_fibres"]=={}
        for j in range(1,6):
            record=self.inputs["directions"][str(j)]
            assert plain(cert["original_direction_marked_principal_and_descent"][str(j)])==plain(record["principal"])
            qz=self.external(record["principal"]);basis=self.external(record["space"])
            assert qz["original_direction"]==j and qz["prime"]==P
            assert plain(qz["source_complete_DZ_normal418"])==plain(record["space"])
            assert qz["DZ_effective_degree"]==272 and qz["DZ_avoids_original_P0"] is True
            assert qz["actual_QZ_rho_order"]==qz["actual_QZ_t_order"]==RHO_ORDERS[j-1]
            assert qz["principal_factor_direction"]=="positive multiplication"
            assert qz["negative_support_not_assumed_to_be_only_P0"] is True
            assert qz["terminal_divisor_or_normal_basis_claimed_K_fixed"] is False
            assert plain(qz["source_original_t_frame"])==plain(self.inputs["t_frame"])
            assert 0<int(qz["actual_QZ_rho_leading_mod_prime"])<P
            assert 0<int(qz["actual_QZ_t_leading_mod_prime"])<P
            assert basis["prime"]==P and basis["complete_RR_space_certified"] is True
            assert basis["actual_projected_rank"]==418
            assert basis["all1904_rows_of_original_relation_verified"] is True
            assert basis["D3_effective_degree272_and_avoids_original_P0"] is True
            shape(basis["normal_V3_basis_mod_prime"],690,418)
            self.spaces["D"+str(j)]={"matrix":mat(basis["normal_V3_basis_mod_prime"]),"reference":record["space"]}
            self.QZ[j]=qz
        self.normal_fibres()
        name="original-source-audit"
        if self.old(name) is None:
            self.put(name,{
                "prime":P,"source_identities":{g:L.identity(self.item["sources"][g]) for g in GROUPS},
                "inputs":self.inputs,"all_original_five_I_Z_targets_bound":True,
                "old_sources_W_Krylov_fibres_Hensel_jets_or_R901_flips_recomputed":False,
                "original_QZ_and_qchi_unscaled_global_source_functions_retained":True,
                "R901_nested_global_function_provenance_kept_in_original_carrier":True,
                "mathematical_objects":"M_j=I_Zj(254P0) and M_j(H), after positive Phi=QZ/qchi",
                "new_mathematics_executed_in_source_audit":False})
        self.weight4_source_extensions()
        self.checkpoint("complete-original-sources-and-weight4-highest-columns")

    def weight4_source_extensions(self):
        copied=[(j,self.V4lookup[pair]) for j,pair in enumerate(self.V3)]
        new=[(i,self.V3lookup[(i,3-EPS[i])],self.V4lookup[(i,4-EPS[i])]) for i in range(272)]
        assert sorted([b for _,b in copied]+[b for _,_,b in new])==list(range(962))
        for z in range(7):
            name=f"normal-V4-fibre-{z}";value=self.old(name)
            if value is None:
                self.budget();E3=rows(self.fibres[z]["E"]);C3=rows(self.fibres[z]["C"])
                E4=[[0]*962 for _ in range(272)];C4=[[0]*962 for _ in range(272)]
                for a,b in copied:
                    for row in range(272):
                        E4[row][b]=E3[row][a];C4[row][b]=C3[row][a]
                for _,a,b in new:
                    for row in range(272):
                        E4[row][b]=z*E3[row][a]%P;C4[row][b]=z*C3[row][a]%P
                value=self.put(name,{
                    "prime":P,"z0":z,"source_original_V3_fibre":self.fibres[z]["reference"],
                    "source_original_Krylov_point":self.inputs["original_Krylov_points"][z],
                    "normal_V4_basis":[list(x) for x in self.V4],
                    "copied_V3_column_pairs":[list(x) for x in copied],
                    "new_highest_column_mapping":[list(x) for x in new],
                    "normal_evaluation_mod_prime":E4,"cyclic_evaluation_mod_prime":C4,
                    "evaluation_shape":[272,962],"only272_highest_columns_newly_multiplied_by_node":True,
                    "old_V3_Krylov_and_inverse_recomputed":False,"normal_integer_scale_applied_again":False})
            assert value["source_original_V3_fibre"]==self.fibres[z]["reference"]
            self.weight4_fibres[z]={"E":mat(value["normal_evaluation_mod_prime"]),"reference":self.refs[name]}
        name="original-V4-nineteen-jet-extension";value=self.old(name)
        if value is None:
            self.budget();old=self.jets["matrix_mod_prime"];raw=[[0]*962 for _ in range(19)]
            for a,b in copied:
                for r in range(19):
                    raw[r][b]=old[r][a]
            for _,a,b in new:
                for r in range(19):
                    raw[r][b]=(self.zP0*old[r][a]+(old[r-1][a] if r else 0))%P
            value=self.put(name,{
                "prime":P,"source_original_V3_252_jets":self.inputs["normal_V3_point_jets"],
                "source_original_point":self.inputs["point_linear_functional"],
                "normal_V4_basis":[list(x) for x in self.V4],"row_orders":list(range(19)),
                "matrix_shape":[19,962],"matrix_mod_prime":raw,
                "copied_V3_column_pairs":[list(x) for x in copied],
                "new_highest_column_mapping":[list(x) for x in new],
                "new_column_formula":"z(P0)*a_r+a_(r-1), a_(-1)=0",
                "old_Hensel_jet_orders_recomputed":False,"only272_missing_highest_columns_computed":True})
        self.J4=mat(value["matrix_mod_prime"]);self.J4ref=self.refs[name]

    def quotient(self,stem,basis,inverse,I,image_ref):
        name=stem+"-shared-product-row-quotient";value=self.old(name)
        if value is None:
            self.budget();R=[i for i in range(1904) if i not in set(I)]
            assert len(I)==962 and len(R)==942
            T=sub(basis,R,list(range(962)))*inverse
            value=self.put(name,{
                "prime":P,"source_complete_product_image":image_ref,
                "selected_rows":I,"complementary_rows":R,"matrix_shape":[942,962],
                "complement_times_selected_inverse_mod_prime":rows(T),
                "quotient_formula":"y_R-P_R*(P_I inverse)*y_I",
                "same_selected_inverse_reused_for_both_weights":True,
                "old_selected_product_basis_or_inverse_recomputed":False})
        assert value["source_complete_product_image"]==image_ref and value["selected_rows"]==I
        return mat(value["complement_times_selected_inverse_mod_prime"]),value["complementary_rows"],self.refs[name]

    def membership(self,j,m,T,I,R,qref,image_ref):
        stem=f"j{j}-weight{m}";name=stem+"-complete-two-anchor-membership"
        value=self.old(name);width=690 if m==3 else 962
        dimension=146 if m==3 else 418;power=6-m
        refs=[self.fibres[z]["reference"] if m==3 else self.weight4_fibres[z]["reference"] for z in range(7)]
        if value is None:
            self.budget();Eraw=[];Zraw=[]
            for z in range(7):
                E=self.fibres[z]["E"] if m==3 else self.weight4_fibres[z]["E"]
                part=rows(E);Eraw.extend(part);factor=pow(z,power,P)
                Zraw.extend([[factor*x%P for x in row] for row in part])
            E=mat(Eraw);Z=mat(Zraw);allcols=list(range(width))
            first=sub(E,R,allcols)-T*sub(E,I,allcols)
            second=sub(Z,R,allcols)-T*sub(Z,I,allcols)
            value=self.put(name,{
                "prime":P,"ordinary_weight":m,"source_complete_product_image":image_ref,
                "source_shared_quotient":qref,"source_full_normal_fibres":refs,
                "selected_rows":I,"complementary_rows":R,
                "membership_anchors":["tau^"+str(power),"sigma^"+str(power)],
                "matrix_shape":[1884,width],"matrix_mod_prime":rows(first)+rows(second),
                "exact_complete_kernel_space":f"H0({m}H-D_Z{j}-Dchi)",
                "exact_geometric_rank":544,"exact_geometric_dimension":dimension,
                "all1904_original_fibre_coordinates_used":True,
                "two_anchors_have_no_common_zero":True,
                "ordinary_V6_evaluation_injective_by_1904_greater_than_1632":True})
        assert value["source_shared_quotient"]==qref
        A=mat(value["matrix_mod_prime"]);shape(value["matrix_mod_prime"],1884,width)
        pname=stem+"-membership-rank544"
        profile=self.rank_profile(pname,A,544,{"complete_membership":self.refs[name]})
        if not profile["accepted"]:
            raise UnitFailure("R903 weight membership lacks its fixed-place rank544 certificate.")
        U,uref=self.complete_kernel(stem+"-complete-U"+str(dimension),A,profile,self.refs[pname],{
            "space":f"H0({m}H-D_Z{j}-Dchi)","dimension":dimension,"degree":m*272-544,
            "source_complete_membership":self.refs[name],
            "exact_original_parent_spaces":[self.inputs["directions"][str(j)]["space"],self.inputs["Dchi"]]})
        assert U.nrows()==width and U.ncols()==dimension
        self.checkpoint(stem+"-complete-membership")
        return U,uref

    def padded(self,j,m,U,uref):
        stem=f"j{j}-weight{m}";name=stem+"-nineteen-jet-restriction"
        value=self.old(name);J=self.J3 if m==3 else self.J4
        d=146 if m==3 else 418;dim=128 if m==3 else 400;width=690 if m==3 else 962
        jref=self.inputs["normal_V3_point_jets"] if m==3 else self.J4ref
        if value is None:
            self.budget();R=J*U
            value=self.put(name,{
                "prime":P,"ordinary_weight":m,"source_complete_U":uref,"source_original_jet_matrix":jref,
                "matrix_shape":[19,d],"matrix_mod_prime":rows(R),
                "row_orders":list(range(19)),"constraint_orders":list(range(18)),
                "last_row_saved_for_original_unscaled_leading_term":True,
                "original_Hensel_jets_recomputed":False})
        assert value["source_complete_U"]==uref
        R=mat(value["matrix_mod_prime"]);A=sub(R,list(range(18)),list(range(d)))
        pname=stem+"-eighteen-jet-rank"
        profile=self.rank_profile(pname,A,18,{"nineteen_jet_restriction":self.refs[name]})
        if not profile["accepted"]:
            raise UnitFailure("R903 original eighteen jet rows lack the required unit minor.")
        K,kref=self.complete_kernel(stem+"-complete-padded-coordinate-kernel",A,profile,self.refs[pname],{
            "space":f"H0({m}H-D_Z{j}-Dchi-18P0)","dimension":dim,"degree":m*272-544-18,
            "source_nineteen_jet_restriction":self.refs[name],
            "all_original_eighteen_conditions_retained":True})
        output=stem+"-complete-normal"+str(dim);old=self.old(output)
        if old is None:
            self.budget();N=U*K
            uvalue=self.own(uref);kvalue=self.own(kref)
            canonical=[uvalue["free_columns"][i] for i in kvalue["free_columns"]]
            assert len(canonical)==dim
            assert sub(N,canonical,list(range(dim)))==eye(dim)
            leading=sub(R,[18],list(range(d)))*K
            assert sub(R,list(range(18)),list(range(d)))*K==zero(18,dim)
            old=self.put(output,{
                "prime":P,"ordinary_weight":m,"source_complete_U":uref,
                "source_complete_eighteen_jet_kernel":kref,"source_nineteen_jet_restriction":self.refs[name],
                "normal_basis_positions":[list(x) for x in (self.V3 if m==3 else self.V4)],
                "normal_basis_mod_prime":rows(N),"normal_shape":[width,dim],
                "canonical_normal_identity_rows":canonical,"canonical_identity_rows_verified":True,
                "order18_coefficients_mod_prime":[int(leading[0,k]) for k in range(dim)],
                "all_eighteen_jet_rows_times_complete_basis_zero":True,
                "exact_complete_RR_dimension":dim,
                "exact_unit_solve_expression":{
                    "operation":"compose_two_complete_original_unit_solve_kernels",
                    "source_U":uref,"source_jet_kernel":kref,
                    "canonical_normal_identity_rows":canonical,
                    "coefficient_arrays_are_original_modular_images_not_reconstructed_char0_coefficients":True},
                "original_global_multiplier_not_yet_applied_to_normal_arrays":True})
        assert old["source_complete_U"]==uref and old["source_complete_eighteen_jet_kernel"]==kref
        shape(old["normal_basis_mod_prime"],width,dim)
        self.checkpoint(output)
        return mat(old["normal_basis_mod_prime"]),self.refs[output]

    def supplement(self,j,A,aref,C,cref):
        stem=f"j{j}";name=stem+"-weight1-original256-prefix"
        prefix=self.old(name)
        if prefix is None:
            self.budget();raw=[[0]*256 for _ in range(962)]
            for old,(i,k) in enumerate(self.V3):
                a=self.V4lookup[(i,k)];b=self.V4lookup[(i,k+1)]
                for column in range(128):
                    v=int(A[old,column]);raw[a][column]=v;raw[b][128+column]=v
            T=mat(raw);cvalue=self.own(cref);I=cvalue["canonical_normal_identity_rows"]
            coordinates=sub(T,I,list(range(256)))
            assert C*coordinates==T
            prefix=self.put(name,{
                "prime":P,"source_complete_normal128":aref,"source_complete_normal400":cref,
                "normal_basis_positions":[list(x) for x in self.V4],
                "normal_matrix_shape":[962,256],"normal_prefix_mod_prime":raw,
                "C400_coordinate_matrix_shape":[400,256],"C400_coordinates_mod_prime":rows(coordinates),
                "C400_canonical_normal_identity_rows":I,
                "prefix_order":["original_tau_times_all128","original_sigma_times_all128"],
                "all962_normal_rows_represented_in_complete_C400":True,
                "no_second_tau_or_82_factor":True,
                "geometric_independence_reason":"H0(N_j-H)=0, degree -18"})
        assert prefix["source_complete_normal128"]==aref and prefix["source_complete_normal400"]==cref
        X=mat(prefix["C400_coordinates_mod_prime"])
        pname=stem+"-weight1-prefix-rank256"
        profile=self.rank_profile(pname,X,256,{"original_prefix":self.refs[name]})
        if not profile["accepted"]:
            raise UnitFailure("R903 original tau/sigma prefix lacks its actual rank256 certificate.")
        assert profile["selected_columns"]==list(range(256))
        outname=stem+"-weight1-original144-complement";value=self.old(outname)
        if value is None:
            self.budget();I=profile["selected_rows"];R=[i for i in range(400) if i not in set(I)]
            assert len(R)==144
            TI=sub(X,I,list(range(256)));inv=TI.inv()
            assert TI*inv==eye(256) and inv*TI==eye(256)
            lower=sub(X,R,list(range(256)))*inv
            draw=rows(X)
            for r in range(400):
                draw[r].extend([int(r==k) for k in R])
            D=mat(draw);iraw=[[0]*400 for _ in range(400)]
            for a in range(256):
                for b,row in enumerate(I):
                    iraw[a][row]=int(inv[a,b])
            for a,row in enumerate(R):
                iraw[256+a][row]=1
                for b,col in enumerate(I):
                    iraw[256+a][col]=(-int(lower[a,b]))%P
            inverse=mat(iraw)
            assert D*inverse==eye(400) and inverse*D==eye(400)
            B=sub(C,list(range(962)),R)
            full=hcat(mat(prefix["normal_prefix_mod_prime"]),B)
            assert C*D==full and full*inverse==C
            selected=self.own(cref)["canonical_normal_identity_rows"]
            assert sub(full,selected,list(range(400)))==D
            combined=hcat(sub(mat(prefix["normal_prefix_mod_prime"]),list(range(962)),list(range(128))),B)
            value=self.put(outname,{
                "prime":P,"source_original256_prefix":self.refs[name],
                "source_actual_prefix_rank256":self.refs[pname],
                "source_complete_normal128":aref,"source_complete_normal400":cref,
                "selected_prefix_coordinate_rows":I,"selected_original_C400_columns":R,
                "prefix_selected_inverse_mod_prime":rows(inv),
                "complete_400_coordinate_change_mod_prime":rows(D),
                "complete_400_coordinate_change_inverse_mod_prime":iraw,
                "selected_original_normal_rows_for_400_unit_minor":selected,
                "normal_144_complement_mod_prime":rows(B),"normal_complement_shape":[962,144],
                "normal_complete400_with_prefix_mod_prime":rows(full),
                "normal_tau_chart_272_columns_mod_prime":rows(combined),
                "complete_tau_chart_shape":[962,272],
                "both256_selected_inverse_products_verified":True,
                "both400_inverse_products_verified":True,
                "all962_normal_rows_of_complete400_basis_and_representation_verified":True,
                "exact_complete_weight1_basis_is_original256_prefix_plus_selected144":True,
                "exact_complement_definition":{
                    "operation":"selected_unscaled_columns_of_complete_original_C400",
                    "source":cref,"columns":R,
                    "preceding_columns":"unchanged tau*A128 followed by sigma*A128"},
                "original_scalars_not_rescaled":True,"extra_tau_factor":0})
        assert value["source_complete_normal128"]==aref and value["source_complete_normal400"]==cref
        self.checkpoint(outname)
        return mat(value["normal_tau_chart_272_columns_mod_prime"]),self.refs[outname]

    def splitting(self,j,combined,complement_ref):
        stem=f"j{j}";success=stem+"-complete-two-chart-splitting"
        old=self.old(success)
        if old is not None:
            assert old["source_complete128_and144"]==complement_ref
            return self.refs[success]
        trials=[]
        for z in range(int(self.item.get("maximum_split_fibres",7))):
            name=stem+f"-split-whole-fibre-{z}";value=self.old(name)
            if value is None:
                self.budget();F=self.weight4_fibres[z]["E"]*combined
                reduced,rank=F.rref();assert rank<=272
                value={"prime":P,"z0":z,"source_complete128_and144":complement_ref,
                    "source_original_V4_fibre":self.weight4_fibres[z]["reference"],
                    "source_original_Krylov_point":self.inputs["original_Krylov_points"][z],
                    "matrix_shape":[272,272],"matrix_mod_prime":rows(F),"actual_rank":rank,
                    "accepted":rank==272,"whole_Artin_fibre_not_replaced_by_points":True,
                    "normal_function_evaluation":"[a128,b144], with no extra division by tau",
                    "only_a_fixed_fibre_unit_criterion_is_tested":True}
                if rank==272:
                    inverse=F.inv()
                    assert F*inverse==eye(272) and inverse*F==eye(272)
                    value.update({"inverse_mod_prime":rows(inverse),
                        "both_complete272_inverse_products_verified":True,
                        "whole_fibre_regular_source_frame_certified_by_full_unit_matrix":True})
                value=self.put(name,value)
            assert value["source_complete128_and144"]==complement_ref
            trials.append(self.refs[name]);self.checkpoint(name)
            if value["accepted"]:
                self.put(success,{
                    "prime":P,"source_complete128_and144":complement_ref,
                    "actual_unit_whole_fibre":self.refs[name],"tested_whole_fibres":trials,
                    "actual_rank":272,"pushforward_rank":272,"both_vector_bundle_degrees":-144,
                    "source_global_membership_and_two_weight_RR_proofs_retained":True,
                    "degree_zero_determinant_nonzero_implies_everywhere_isomorphism":True,
                    "exact_split_bundle":"O^128 direct_sum O(-1)^144",
                    "tau_chart_normal_functions":"a128 and b144",
                    "sigma_chart_normal_functions":"a128 and b144/z",
                    "same_Phi_multiplies_both_charts":True,
                    "extra_tau_division":False,
                    "complete_two_affine_lattices_and_original_transition_certified":True})
                return self.refs[success]
        raise UnitFailure("R903 seven-node prefix has no observed full272 unit; use a later legitimate frame or node.")

    def marked_embedding(self,j,aref,cref,complement_ref,split_ref):
        name=f"j{j}-original-Iz-marked-embedding-and-P0-frame";value=self.old(name)
        if value is None:
            self.budget();a=self.own(aref);qz=self.QZ[j]
            leading=a["order18_coefficients_mod_prime"]
            column=next((i for i,x in enumerate(leading) if int(x)%P),None)
            if column is None:
                self.put(name+"-unit-failure",{
                    "prime":P,"source_complete_normal128":aref,"order18_coefficients_mod_prime":leading,
                    "only_fixed_place_unit_condition_failed":True})
                raise UnitFailure("R903 no observed order18 unit column in the complete128 space.")
            a18=int(leading[column]);rho=int(qz["actual_QZ_rho_leading_mod_prime"])*a18%P
            rho=rho*pow(self.qchi_lc,-1,P)%P
            order=RHO_ORDERS[j-1]-254;cpower=pow(self.c,-order,P);t=rho*cpower%P
            assert 0<rho<P and 0<t<P
            qref=self.inputs["directions"][str(j)]["principal"]
            Phi={"operation":"divide",
                "numerator":{"operation":"completed_original_R901_marked_QZ",
                    "source":qref,"field":"exact_QZ_function_DAG",
                    "nested_source_resolver":"preserved original R901 source inventory and carrier"},
                "denominator":{"operation":"original_unscaled_section_divided_by_tau_squared",
                    "source":self.inputs["qchi_anchor"],"original_tau_power":2,"extra_scalar":1}}
            value=self.put(name,{
                "prime":P,"original_direction":j,"source_original_marked_QZ":qref,
                "source_original_qchi":self.inputs["qchi_anchor"],
                "source_original_fixed_chi_divisor":self.inputs["fixed_chi_divisor"],
                "source_original_t_frame":self.inputs["t_frame"],
                "source_complete_normal128":aref,"source_complete_normal400":cref,
                "source_actual144_complement":complement_ref,"source_complete_two_chart_splitting":split_ref,
                "source_R901_opaque_function_provenance":self.inputs["R901_function_provenance"],
                "exact_positive_multiplier_Phi_DAG":Phi,
                "exact_original_line_bundle":"M_j=I_Zj(254P0)",
                "exact_domain_line_bundle":"O(3H-D_Zj-Dchi-18P0)",
                "exact_divisor_of_Phi":"Z_j+3H-D_Zj-Dchi-272P0",
                "positive_multiplication_is_an_isomorphism_at_every_curve_DVR":True,
                "target_128_functions":{"operation":"positive_multiply_every_basis_function",
                    "multiplier":Phi,"normal_basis_source":aref,"ordinary_weight":3,"extra_tau_division":0},
                "target_144_weight1_functions":{"operation":"positive_multiply_every_basis_function",
                    "multiplier":Phi,"normal_basis_source":complement_ref,
                    "basis_field":"normal_144_complement_mod_prime","extra_tau_division":0},
                "original_P0_selected_column":column,"selected_column_not_rescaled":True,
                "selected_order18_coefficient_mod_prime":a18,
                "original_qchi_order272_coefficient_mod_prime":self.qchi_lc,
                "actual_target_rho_order":order,"actual_target_t_order":order,
                "actual_rho_leading_mod_prime":rho,"actual_c_exponent":-order,
                "actual_c_power_mod_prime":cpower,"actual_t_frame_coefficient_mod_prime":t,
                "exact_rho_leading_expression":{
                    "operation":"divide","numerator":[{"source":qref,"field":"exact_rho_leading_expression"},
                        {"source":aref,"operation":"order18_of_unchanged_column","column":column}],
                    "denominator":{"source":self.inputs["qchi_anchor"],"operation":"original_order272_coefficient"}},
                "exact_t_frame_expression":"LCrho(QZ)*a18/LCrho(qchi) * c^(254-ord(QZ))",
                "same_exact_global_section_value_at_original_P1_computed":False,
                "P0_unit_claimed_to_certify_P1_unit":False,
                "auxiliary_unit_claimed_to_be_41_or_all_nonp_units":False,
                "negative_support_of_Z_not_assumed_to_be_only_P0":True,
                "exact_semilinear_descent_action":"v -> (sigma(QZ)/QZ)*sigma(v)",
                "source_original_descent_transition":qref,
                "sevenfold_cocycle_retained_from_original_QZ":True,
                "selected144_complement_claimed_Galois_stable":False,
                "K_or_Q_fixed_basis_computed":False,
                "real_descent_cubed_ideal_identified_with_I_Z":False,
                "original_Rcal_kappa_theta_torsion_nonp_or_height_changed":False})
        assert value["source_complete_normal128"]==aref and value["source_actual144_complement"]==complement_ref
        self.checkpoint(name)
        return self.refs[name]

    def direction(self,j):
        name=f"j{j}-complete-two-weight-RR-certificate";old=self.old(name)
        if old is not None:
            self.completed_directions[str(j)]=self.refs[name]
            self.close_direction_work(j,self.refs[name])
            return self.refs[name]
        stem=f"j{j}"
        basis,inverse,I,image_ref=self.product_span(stem,"D"+str(j),"X")
        T,R,qref=self.quotient(stem,basis,inverse,I,image_ref)
        del basis,inverse;gc.collect()
        U3,u3ref=self.membership(j,3,T,I,R,qref,image_ref)
        U4,u4ref=self.membership(j,4,T,I,R,qref,image_ref)
        A,aref=self.padded(j,3,U3,u3ref);C,cref=self.padded(j,4,U4,u4ref)
        del U3,U4,T;gc.collect()
        combined,complement_ref=self.supplement(j,A,aref,C,cref)
        del A,C;gc.collect()
        split_ref=self.splitting(j,combined,complement_ref)
        frame_ref=self.marked_embedding(j,aref,cref,complement_ref,split_ref)
        self.put(name,{
            "prime":P,"original_direction":j,"source_original_DZ_complete418":self.inputs["directions"][str(j)]["space"],
            "source_original_marked_QZ":self.inputs["directions"][str(j)]["principal"],
            "source_original_Dchi_complete418":self.inputs["Dchi"],
            "single_shared_product_image":image_ref,"shared_row_quotient":qref,
            "complete_U3_146":u3ref,"complete_U4_418":u4ref,
            "complete_original_normal128":aref,"complete_original_normal400":cref,
            "complete_original144_complement":complement_ref,
            "complete_two_chart_splitting":split_ref,"marked_original_P0_frame_and_embedding":frame_ref,
            "actual_shared_product_dimension":962,"actual_membership_ranks":[544,544],
            "actual_eighteen_jet_ranks":[18,18],"actual_padded_dimensions":[128,400],
            "actual_weight1_prefix_rank":256,"actual_complement_dimension":144,"actual_split_rank":272,
            "actual_original_Iz_128_RR_space_certified":True,
            "actual_original_Iz_weight1_400_RR_space_certified":True,
            "actual_original144_complement_with_original256_prefix_certified":True,
            "actual_original_two_affine_rank272_lattices_certified":True,
            "actual_original_unscaled_P0_frame_coefficient_certified":True,
            "coefficient_representation":"exact original unit-solve expressions with true modular images",
            "characteristic_zero_RR_coefficients_reconstructed":False,
            "original_P1_section_value_K_Q_descent_connection_period_nonp_height_computed":False})
        self.completed_directions[str(j)]=self.refs[name]
        self.close_direction_work(j,self.refs[name])
        return self.refs[name]

    def live_closure(self,root):
        todo=[root];seen={}
        while todo:
            row=todo.pop()
            if row.get("source_group") is not None:
                assert row["source_group"] in self.sources
                assert self.sources[row["source_group"]].files[row["file"]]==plain(row)
                continue
            name=row["file"];assert name.startswith(PREFIX)
            if name in seen:
                assert seen[name]==plain(row);continue
            value=self.own(row);seen[name]=plain(row)
            for ref in M.live_refs(value):
                if ref.get("source_group") is not None:
                    assert self.sources[ref["source_group"]].files[ref["file"]]==plain(ref)
                elif ref["file"].startswith(PREFIX):
                    todo.append(ref)
                else:
                    raise AssertionError("R903 unqualified external live reference: "+ref["file"])
        return seen

    def close_direction_work(self,j,certificate):
        stem=f"j{j}";name=stem+"-closed-product-work-retention"
        old=self.old(name);keep=self.live_closure(certificate)
        candidates=[p for p in sorted(self.out.glob(PREFIX+stem+"-*.json.gz")) if p.name!=self.path(name).name]
        if old is None:
            discarded=[spec(p) for p in candidates if p.name not in keep]
            old=self.put(name,{
                "prime":P,"complete_direction_certificate":certificate,
                "required_live_witness_files":list(sorted(keep.values(),key=lambda x:x["file"])),
                "discarded_intermediate_stage_history":discarded,
                "discarded_intermediate_count":len(discarded),
                "discarded_intermediate_bytes":sum(x["bytes"] for x in discarded),
                "historical_hashes_are_not_live_dependencies":True,
                "same_product_selected_column_identities_full_basis_and_inverse_retained":True,
                "both_membership_matrices_all_kernels_jets_and_two_chart_witness_retained":True,
                "cleanup_only_after_complete_direction_certificate":True,"active_or_pending_work_discarded":False})
        assert old["complete_direction_certificate"]==certificate
        assert {r["file"]:plain(r) for r in old["required_live_witness_files"]}==keep
        for row in old["discarded_intermediate_stage_history"]:
            assert row["file"].startswith(PREFIX+stem+"-") and row["file"] not in keep
            path=self.out/row["file"]
            if path.exists():
                assert spec(path)==plain(row);path.unlink()
            self.refs.pop(row["file"][len(PREFIX):-len(".json.gz")],None)
        if self.refs[name] not in self.closed_refs:
            self.closed_refs.append(self.refs[name])
        for key in list(self.space_cache):
            if key[0]=="D"+str(j):
                del self.space_cache[key]
        self.spaces["D"+str(j)].pop("matrix",None)
        self.checkpoint("closed-"+stem);gc.collect()

    def inventory(self):
        entries=[];histories=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name==PREFIX+"current.json.gz" or path.name.startswith(PREFIX+"stage-manifest-"):
                continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
            row=spec(path);entries.append(row)
            if "discarded_intermediate_stage_history" in value:
                histories.append(row)
        value={"result":RESULT,"configuration":self.tag,"complete":True,"files":entries,
            "current_excluded":True,"all_live_and_unclosed_work_retained":True,
            "closed_work_retention_receipts":histories,"historical_discarded_hashes_not_claimed_present":True}
        path=self.path("stage-manifest-"+fingerprint(value))
        if path.exists():
            assert read(path)==value
        else:
            save(path,value)
        return spec(path),len(entries)

    def finish(self,complete,reason):
        for j in range(1,6):
            name=f"j{j}-complete-two-weight-RR-certificate"
            if self.old(name) is not None:
                self.completed_directions[str(j)]=self.refs[name]
        self.checkpoint("completed" if complete else self.phase)
        inventory,count=self.inventory()
        if complete:
            assert set(self.completed_directions)=={"1","2","3","4","5"}
            assert len(self.closed_refs)==5
        partial={}
        for j in range(1,6):
            partial[str(j)]={key:self.refs.get(f"j{j}-"+suffix) for key,suffix in (
                ("complete_normal128","weight3-complete-normal128"),
                ("complete_normal400","weight4-complete-normal400"),
                ("complete144_complement","weight1-original144-complement"),
                ("complete272_splitting","complete-two-chart-splitting"))}
        allfive=len(self.completed_directions)==5
        final={"result":RESULT,"configuration":self.tag,"complete":bool(complete),"p":41,
            "actual_auxiliary_prime":P,"source_audit":self.refs.get("original-source-audit"),
            "complete_direction_certificates":self.completed_directions,
            "completed_directions":sorted(map(int,self.completed_directions)),
            "partial_direction_outputs":partial,"closed_work_retention_receipts":self.closed_refs,
            "actual_all_five_original_Iz_128_spaces_certified":allfive,
            "actual_all_five_original_weight1_400_spaces_certified":allfive,
            "actual_all_five_original144_complements_certified":allfive,
            "actual_all_five_complete_two_chart272_lattices_certified":allfive,
            "actual_all_five_original_P0_frame_coefficients_certified":allfive,
            "original_Hensel_W_Krylov_V3_fibres_R901_flips_recomputed":False,
            "original_P1_values_K_Q_fixed_bases_Hecke_norm_connection_period_nonp_height_computed":False,
            "real_descent_cubed_ideal_claimed_equal_to_Iz":False,
            "characteristic_zero_RR_coefficients_reconstructed":False,
            "actual_retained_complete_stage_count":count,"stage_manifest":inventory,
            "resume_state":self.current,"stop_reason":reason,"seconds":time.monotonic()-self.started}
        save(self.out/FINAL,final)
        return final

    def run(self):
        path=self.out/FINAL
        if path.exists():
            final=read(path)
            assert final["result"]==RESULT and final["configuration"]==self.tag
            if final["complete"] is True:
                inventory=self.own(final["stage_manifest"])
                for row in inventory["files"]:
                    assert spec(self.out/row["file"])==plain(row)
                return final
        assert 1<=self.item["maximum_product_anchors"]<=418
        assert 1<=self.item.get("maximum_split_fibres",7)<=7
        assert 1<=self.item.get("maximum_directions",5)<=5
        self.prepare()
        for j in range(1,6):
            if j>int(self.item.get("maximum_directions",5)):
                raise SearchStop("R903 requested complete-direction prefix ended; no remaining direction claimed.")
            self.direction(j)
        return self.finish(True,None)

def main():
    if hasattr(sys,"set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
    parser=argparse.ArgumentParser()
    parser.add_argument("--config",required=True);parser.add_argument("--retained",required=True)
    parser.add_argument("--output",required=True);parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args();out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    started=time.monotonic();job=None;final=None;error=None;code=1
    try:
        job=Job(args);final=job.run();code=0 if final["complete"] else 2
    except (BudgetStop,UnitFailure,SearchStop) as exc:
        error={"type":type(exc).__name__,"message":str(exc)}
        if job is not None:
            final=job.finish(False,error)
        code=2
    except Exception as exc:
        error={"type":type(exc).__name__,"message":str(exc)};traceback.print_exc()
        if job is not None:
            try:
                final=job.finish(False,error)
            except Exception:
                traceback.print_exc()
        code=1
    receipt={"result":RESULT,"source_sha256":sha(__file__),"complete":bool(final and final["complete"]),
        "configuration":job.tag if job is not None else None,
        "configuration_sha256":fingerprint(job.tag) if job is not None else None,
        "actual_auxiliary_prime":P,"process_exit_code":code,"error":error,
        "certificate_file":FINAL if (out/FINAL).exists() else None,
        "certificate_sha256":sha(out/FINAL) if (out/FINAL).exists() else None,
        "actual_complete_direction_count":len(final["completed_directions"]) if final else 0,
        "actual_retained_complete_stage_count":final["actual_retained_complete_stage_count"] if final else 0,
        "actual_all_five_original_Iz_128_spaces_certified":bool(final and final["actual_all_five_original_Iz_128_spaces_certified"]),
        "actual_all_five_complete_two_chart272_lattices_certified":bool(final and final["actual_all_five_complete_two_chart272_lattices_certified"]),
        "original_P1_descent_connection_period_nonp_height_computed":False,
        "seconds":time.monotonic()-started}
    save(out/"core-receipt.json",receipt)
    print("R903_CORE_RECEIPT="+json.dumps(receipt,sort_keys=True),flush=True)
    return code

if __name__=="__main__":
    raise SystemExit(main())
