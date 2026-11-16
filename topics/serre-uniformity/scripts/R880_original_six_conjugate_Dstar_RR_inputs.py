#!/usr/bin/env python3
"""Six actual Galois conjugates of the original bounded Dstar RR source.
Only new branch arithmetic runs; original W/operators, K0 inverses, S5
products, normal conversion, point jets, and branch-zero charts are inputs.
"""
import argparse
import gc
import hashlib
import importlib.util
import json
from math import comb
import os
from pathlib import Path
import sys
import time
import traceback

RESULT="R880-original-six-conjugate-Dstar-RR-inputs"
FINAL="p41-original-six-conjugate-Dstar-RR-inputs-certificate.json"
PREFIX="R880-six-Dstar-"
PRIME=1000000753
EPS=[0]+[1]*144+[2]*127
NODES=[0,1,2,3,4]
MULTIPLICITIES=[3,3,2,2,2]
SIGMA_COLUMNS=[0]+list(range(73,92))
LEGACY_SHA="ca46e8f9a9410be240ad77c0863b193e77ef701b06186a31b3edb20eb3e997a4"
PROOF_SHA="b2e523171c08f61b4c1f66ee7738e8fb687f45a3e1dd72ccd6956800cc9d2d84"
PROOFS=("six_D","R880","R887")
SOURCE_GROUPS=("AB","R827","R842","R845","R880","R887","R872")
INPUTS=(
 "seven_inputs","AB_audit","W_reduction","place_audit","g_index","Gamma_index","operator_identity",
 "T11_chart","T5_chart","D_chart","D_matrix","rank1111","old_sections","normal_index","alias_audit",
 "old_anchor_selection","V3_jets","standardizing_kernel","standardizing_basis","old_v","old_w",
 "rank962","old_Dstar","old_principal","u_C","Cstar_principal","Cstar_basis",
 "chi_anchor","chi_divisor","chi_kernel")
STRATEGY={
 "prime":PRIME,"original_zeta_root":549966761,"original_s_root":99932770,
 "original_branch_zero_integral_B_root":3197390,"canonical_free_column":1186,
 "new_branches":"six nonzero original sigma powers, read actual orbit",
 "old_nodes":NODES,"Hasse_multiplicities":MULTIPLICITIES,
 "confluent_polynomial_dimension":12,"old_K0_and_inverse_copied_from_source":True,
 "new_shared_K_and_inverse_jet_orders":"1 through m_i+1",
 "F0_jet_orders":"0 through m_i+1","F1_jet_orders":"0 through m_i","F2_jet_orders":"0 through m_i-1",
 "matrix_entry_degree_bounds":[7,9,11],
 "sigma_first_layer":"z*F1-(5+epsilon_column)*Mg*F0",
 "original_sigma_generator_columns":SIGMA_COLUMNS,
 "selected_T11_shape":[2866,2451],"T11_quotient_shape":[415,2866],
 "T5_two_pencil_shape":[830,1234],"T5_quotient_shape":[415,1234],
 "D_constraint_shape":[830,690],"D_basis_dimension":295,
 "original_1111_kernel_dimension":269,"point_jet_constraint_shape":[123,269],
 "standardizing_dimension":146,"new_Dstar_kernel_dimension":418,
 "all_original_pivot_rows_columns_free_coordinates_v_and_trial_preserved":True,
 "no_new_rank_selection_defines_conjugate_objects":True,
 "same_original_82_scales_preserved_without_extra_multiplication":True,
 "old_S5_products_and_inverse_normal_conversion_and_point_jets_recomputed":False,
 "old_branch_zero_RR_or_products_recomputed":False,
 "complete_new_relation_residuals_required":True,
 "exact_objects":"Galois images of the original fixed unit-solve expressions",
 "modular_arrays_are_not_reconstructed_characteristic_zero_coefficients":True,
 "new_principal_function":"(a_j/v_j)^3*(u_C/tau^2)/(u_chi/tau^2)^4",
 "new_principal_rho_order":-1205,
 "new_t_parameter_or_Picard_height_computed":False,
 "only_budget_branch_limit_and_transport_excluded_from_identity":True,
}

def load_legacy():
    path=Path(__file__).resolve().parent/"R880_original_D_and_cusp_bounded_RR_inputs.py"
    assert hashlib.sha256(path.read_bytes()).hexdigest()==LEGACY_SHA
    spec0=importlib.util.spec_from_file_location("R880_six_Dstar_frozen_helpers",path)
    module=importlib.util.module_from_spec(spec0)
    spec0.loader.exec_module(module)
    return module

L=load_legacy()
read,save,sha,spec,plain,bound,fingerprint=L.read,L.save,L.sha,L.spec,L.plain,L.bound,L.fingerprint
rows,shape,positions=L.rows,L.shape,L.positions
BudgetStop,UnitFailure=L.BudgetStop,L.UnitFailure

def source_identity(v):
    return L.source_identity(v)

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
      "legacy_R880_core_sha256":LEGACY_SHA,"method_sha256":item["method_sha256"],
      "proofs_sha256":{k:item["proofs"][k]["sha256"] for k in PROOFS},
      "sources":{k:source_identity(item["sources"][k]) for k in SOURCE_GROUPS},
      "inputs":item["inputs"],"normal_basis_degrees":EPS,"strategy":STRATEGY}

class Job:
    def __init__(self,args):
        import flint
        assert flint.__version__=="0.9.0"
        self.Matrix=flint.nmod_mat
        self.args=args;self.started=time.monotonic();self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41
        assert self.item["producer_inputs_pending"] is False
        assert self.item["core_sha256"]==sha(__file__)
        assert self.item["legacy_R880_core_sha256"]==LEGACY_SHA
        assert sha(self.item["method"])==self.item["method_sha256"]
        assert set(self.item["proofs"])==set(PROOFS)
        assert self.item["proofs"]["six_D"]["sha256"]==PROOF_SHA
        for v in self.item["proofs"].values():assert sha(v["path"])==v["sha256"]
        assert set(self.item["sources"])==set(SOURCE_GROUPS)
        assert set(self.item["inputs"])==set(INPUTS)
        self.tag=expected_tag(self.item);self.out=Path(args.out);self.out.mkdir(parents=True,exist_ok=True)
        self.status="initializing";self.refs={};self.completed=[];self.active_branch=None
        self.maximum_branches=int(self.item.get("maximum_branches",6))
        assert 1<=self.maximum_branches<=6
        self.pos3,self.pos5,self.pos11=positions(3),positions(5),positions(11)
        assert [len(x) for x in (self.pos3,self.pos5,self.pos11)]==[690,1234,2866]
        self.map11={v:i for i,v in enumerate(self.pos11)}
        self.tau_labels=[(r,c,k) for r in range(3) for c in range(272)
                         for k in range(12-(5+2*r+EPS[c]))]
        self.sigma_labels=[(c,k) for c in SIGMA_COLUMNS for k in range(12-(7+EPS[c]))]
        assert len(self.tau_labels)==2886 and len(self.sigma_labels)==81
        self.sources={};self.inputs={};self.ir={};self.K0={};self.J0={};self.fibers={}
        self.operator_cache={};self.shared_jets={};self.branch_records=[]

    def budget(self):
        if time.monotonic()-self.started>=self.args.budget_minutes*60-30:
            raise BudgetStop("All completed source-bound stages retained; next="+self.status)

    def mat(self,a):return self.Matrix(a,PRIME)
    def zero(self,h,w):return self.mat([[0]*w for _ in range(h)])
    def eye(self,n):return self.mat([[int(i==j) for j in range(n)] for i in range(n)])
    def sub(self,A,I,J):return self.mat([[int(A[i,j]) for j in J] for i in I])
    def col(self,A,j):return self.mat([[int(A[i,j])] for i in range(A.nrows())])

    def path(self,name):
        name=name if name.startswith(PREFIX) else PREFIX+name
        assert Path(name).name==name
        return self.out/(name if name.endswith(".json.gz") else name+".json.gz")

    def ref(self,name):return spec(self.path(name))

    def old(self,name):
        path=self.path(name)
        if not path.exists():return None
        v=read(path)
        assert v["result"]==RESULT and v["configuration"]==self.tag and v["complete"] is True
        return v

    def put(self,name,value):
        assert not any(k in value for k in ("result","configuration","complete"))
        old=self.old(name)
        if old is not None:return old
        save(self.path(name),dict(value,result=RESULT,configuration=self.tag,complete=True))
        print(json.dumps({"stage":self.path(name).name,"seconds":time.monotonic()-self.started}),flush=True)
        return self.old(name)

    def own(self,reference):
        reference=plain(reference)
        bound(self.out,reference)
        return self.old(reference["file"])

    def checkpoint(self,status):
        self.status=status
        value={"result":RESULT,"configuration":self.tag,"complete":False,
               "status":status,"source_audit":self.refs.get("source_audit"),
               "active_original_branch":self.active_branch,"completed_branches":self.completed,
               "shared_references":self.refs}
        save(self.path("current"),value)
        return self.ref("current")

    def source(self,label,entry):
        source=self.sources[label]
        if isinstance(entry,str):entry=source.files[entry]
        return source.stage(entry),source.ref(entry)

    def same_source(self,record,label):
        assert L.identity(record)==L.identity(self.sources[label].value)
        if "configuration_sha256" in record:
            assert record["configuration_sha256"]==self.sources[label].value["configuration_sha256"]

    def prepare(self):
        self.status="source audit"
        self.sources={k:L.Source(k,self.item["sources"][k]) for k in SOURCE_GROUPS}
        for key,ref in self.item["inputs"].items():
            assert ref["source_group"] in SOURCE_GROUPS
            self.inputs[key],self.ir[key]=self.source(ref["source_group"],ref)
        a=self.inputs;ab=self.sources["AB"];r0=self.sources["R880"]
        assert ab.certificate["all_seven_original_Galois_normal_inputs_certified"] is True
        assert ab.certificate["all1380_by12_original_coordinates_verified"] is True
        assert ab.certificate["original_Galois_seven_cycle_certified"] is True
        assert ab.certificate["new_right_hand_side_count"]==12
        assert a["seven_inputs"]["all_seven_original_Galois_normal_inputs_certified"] is True
        assert a["seven_inputs"]["same_original_unit_chart_normalization_for_every_branch"] is True
        assert a["seven_inputs"]["original_s_root"]==99932770
        assert a["seven_inputs"]["original_zeta_root"]==549966761
        records=a["seven_inputs"]["ordered_original_sigma_powers"]
        assert [x["sigma_power"] for x in records]==list(range(7))
        assert records[0]["original_branch"]==0 and records[0]["roots_B_s"]==[3197390,99932770]
        assert len({x["original_branch"] for x in records})==7
        self.branch_records=[]
        for r in records[1:]:
            value,ref=self.source("AB",r["source_original_normal_pair"])
            assert value["prime"]==PRIME and value["original_branch"]==r["original_branch"]
            assert value["sigma_power"]==r["sigma_power"] and value["roots_B_s"]==r["roots_B_s"]
            assert r["roots_B_s"][1]==99932770
            assert value["canonical_free_column"]==1186 and value["original_zeta_root"]==549966761
            assert value["all1380_original_coordinates_for_each_vector_verified"] is True
            assert value["all_original_weighted_support_bounds_verified"] is True
            assert value["abstract_p_integral_original_normal_lifts_certified"] is True
            assert value["same_original_82power10_scales_preserved"] is True
            shape(value["B_vector_coefficients_mod_prime"],6,272)
            self.branch_records.append(dict(r,pair=ref,pair_value=value))
        assert a["place_audit"]["prime"]==PRIME and a["place_audit"]["original_branch"]==0
        assert a["place_audit"]["original_zeta_root"]==549966761
        assert a["place_audit"]["original_s_root"]==99932770
        assert a["place_audit"]["canonical_free_column"]==1186
        assert a["W_reduction"]["original_rational_denominators_all_units"] is True
        assert a["W_reduction"]["original_W_e0_equals_e1_verified"] is True
        assert len(a["W_reduction"]["W_coefficients_mod_prime"])==4
        self.W=[self.mat(x) for x in a["W_reduction"]["W_coefficients_mod_prime"]]
        for v in self.W:assert (v.nrows(),v.ncols())==(272,272)
        identity=a["operator_identity"]
        assert identity["all_operators_are_true_original_p_integral_reductions"] is True
        assert identity["g_commutator_full_polynomial_identity_certified_by_seven_points"] is True
        assert identity["Gamma_nested_full_polynomial_identity_certified_by_seven_points"] is True
        for target,key in (("g","g_index"),("Gamma","Gamma_index")):
            assert plain(identity["operator_indexes"][target]["tau"])==plain(self.ir[key])
            index=a[key]
            assert index["prime"]==PRIME and index["target"]==target and index["chart"]=="tau"
            assert index["normal_basis_degrees"]==EPS
            assert index["original_true_operator_reduction_certified"] is True
            assert index["all_weighted_support_zeros_verified"] is True
            degree=3 if target=="g" else 2
            assert index["regular_degree_bound"]==degree and len(index["row_blocks"])==17
            raw=[[[0]*272 for _ in range(272)] for _ in range(degree+3)]
            nextrow=0
            for blockref in index["row_blocks"]:
                block,_=self.source("R827",blockref)
                first,stop=block["row_first"],block["row_stop"]
                assert first==nextrow and stop==min(first+16,272)
                assert block["target"]==target and block["chart"]=="tau" and block["prime"]==PRIME
                assert block["original_weighted_support_verified"] is True
                assert block["true_p_integral_operator_reduction_by_unit_nodes_and_original_degree_bound"] is True
                values=block["coefficient_matrices_low_to_high"]
                assert len(values)==degree+3
                for n,part in enumerate(values):
                    shape(part,stop-first,272)
                    raw[n][first:stop]=part
                nextrow=stop
            assert nextrow==272
            self.operator_cache[target]=[self.mat(x) for x in raw]
            del raw
        t11,t5,dk=a["T11_chart"],a["T5_chart"],a["D_chart"]
        assert t11["exact_original_T11_as_unit_chart_expression_certified"] is True and t11["actual_rank"]==2451
        assert len(t11["selected_original_tau_columns"])==2431 and len(t11["selected_new_sigma_columns"])==20
        assert len(t11["selected_original_rows"])==2451 and len(t11["complement_original_rows"])==415
        assert set(t11["selected_original_rows"])|set(t11["complement_original_rows"])==set(range(2866))
        assert t5["exact_original_T5_quotient_as_unit_chart_expression_certified"] is True
        assert t5["actual_rank"]==415 and t5["full_830_by1234_row_space_reconstruction_verified"] is True
        assert len(t5["selected_original_rows"])==len(t5["selected_original_columns"])==415
        assert dk["actual_rank"]==395 and dk["exact_original_D_RR_space_as_unit_chart_expression_certified"] is True
        assert dk["all830_original_equations_verified_for_all295_columns"] is True
        assert plain(dk["source_original_D_matrix"])==plain(self.ir["D_matrix"])
        assert a["D_matrix"]["actual_P0_multiplicity_in_D"]==0
        assert a["rank1111"]["actual_rank"]==1111
        assert a["old_sections"]["integer_parameter"]==1
        assert a["old_sections"]["a_exact_D_basis_column"]==0
        assert a["old_sections"]["b_exact_D_basis_coefficients"]["integer_parameter"]==1
        assert a["old_anchor_selection"]["block_swap_used"] is False
        assert a["old_anchor_selection"]["selected_original_role"]=="a"
        assert a["old_anchor_selection"]["no_rescaling"] is True
        assert a["standardizing_kernel"]["actual_rank_mod_prime"]==123
        assert a["standardizing_kernel"]["actual_kernel_dimension"]==146
        assert a["standardizing_kernel"]["free_normalization_identity_verified"] is True
        assert a["standardizing_basis"]["actual_complete_standardizing_RR_space_certified"] is True
        self.v_index=a["standardizing_basis"]["selected_first_order123_unit_column"]
        assert isinstance(self.v_index,int) and 0<=self.v_index<146
        assert a["rank962"]["accepted"] is True and a["rank962"]["actual_rank"]==962
        assert a["rank962"]["integer_parameter"]==1
        assert a["old_Dstar"]["complete_RR_space_certified"] is True
        assert a["old_Dstar"]["actual_projected_rank"]==418
        assert a["chi_anchor"]["order272_is_exact"] is True and a["chi_anchor"]["exact_order272_unit"]
        assert a["chi_anchor"]["normal_integer_scale_applied_again"] is False
        assert a["u_C"]["original_jet_order"]==252 and a["u_C"]["actual_order252_unit_mod_prime"]
        assert a["Cstar_principal"]["original_Cstar_and_qC_are_fixed_by_L_over_K_Galois_action"] is True
        assert a["Cstar_principal"]["actual_rho_order"]==-1205
        assert plain(a["Cstar_principal"]["source_exact_u_C"])==plain(self.ir["u_C"])
        assert plain(a["Cstar_principal"]["source_complete_Cstar_418"])==plain(self.ir["Cstar_basis"])
        assert a["Cstar_basis"]["complete_RR_space_certified"] is True
        assert a["Cstar_basis"]["actual_projected_rank"]==418
        assert plain(a["old_principal"]["source_complete_Dstar_418_space"])==plain(self.ir["old_Dstar"])
        assert plain(a["old_principal"]["source_complete_D_chi_418_space"])==plain(self.ir["chi_kernel"])
        assert plain(a["chi_divisor"]["source_exact_u"])==plain(self.ir["chi_anchor"])
        assert plain(a["chi_divisor"]["source_complete_W_Dchi"])==plain(self.ir["chi_kernel"])
        self.parameter=a["old_principal"]["actual_local_parameter"]
        assert self.parameter==a["Cstar_principal"]["actual_local_parameter"]==a["u_C"]["actual_local_parameter"]
        assert a["V3_jets"]["matrix_shape"]==[252,690]
        self.J3=self.mat(a["V3_jets"]["matrix_mod_prime"])
        for label in ("R827","R842","R845","R872"):
            self.same_source(r0.tag["sources"][label],label)
        for label in ("R827","R842"):
            self.same_source(self.sources["R845"].tag["sources"][label],label)
        self.same_source(self.sources["R842"].tag["sources"]["R827"],"R827")
        self.same_source(self.sources["R872"].tag["sources"]["R827"],"R827")
        for label in ("R827","R842"):
            self.same_source(ab.tag["sources"][label],label)
        self.same_source(self.sources["R887"].tag["sources"]["R880"],"R880")
        normal=a["normal_index"]
        assert normal["normal_row_mapping"]==[list(x) for x in self.pos3]
        assert normal["all690_rhs_and_all1380_equations_and_weighted_support_verified"] is True
        N=[[0]*690 for _ in range(690)];nextcol=0
        for ref in normal["blocks"]:
            block,_=self.source("R845",ref);first,stop=block["original_V3_indices"]
            assert first==nextcol and stop==min(first+30,690)
            assert block["all1380_original_equations_verified"] is True
            assert block["all_extra_weight5_coordinates_zero"] is True
            assert block["normal_row_mapping"]==[list(x) for x in self.pos3]
            shape(block["normal_coefficients_mod_prime"],690,stop-first)
            for row,part in zip(N,block["normal_coefficients_mod_prime"]):row[first:stop]=part
            nextcol=stop
        assert nextcol==690
        self.normal=self.mat(N);del N
        for i in NODES:
            point,pref=self.source("R827",f"R827-prime-{PRIME}-z-{i}-Krylov.json.gz")
            evaluation,eref=self.source("R845",f"R839-pole-fiber-{i}-original-V3.json.gz")
            assert point["prime"]==PRIME and point["z0"]==i and point["usable"] is True
            assert point["actual_cyclic_rank"]==272 and point["both_inverse_products_verified"] is True
            assert plain(point["source_original_W"])==plain(self.ir["W_reduction"])
            assert plain(evaluation["source_original_Krylov_point"])==plain(pref)
            assert plain(evaluation["source_original_V3_normal_index"])==plain(self.ir["normal_index"])
            assert evaluation["prime"]==PRIME and evaluation["z0"]==i
            self.K0[i]=self.mat(point["Krylov_matrix_mod_prime"])
            self.J0[i]=self.mat(point["inverse_Krylov_matrix_mod_prime"])
            self.fibers[i]=(evaluation,eref,point,pref)
        self.Mu,self.Mv,self.anchor_product_refs=self.read_original_fixed_products()
        name="original-source-and-fixed-chart-audit"
        if self.old(name) is None:
            self.put(name,{"prime":PRIME,"source_identities":{k:source_identity(v.value) for k,v in self.sources.items()},
                "input_references":self.ir,"original_sigma_powers":[r["sigma_power"] for r in self.branch_records],
                "original_branches":[r["original_branch"] for r in self.branch_records],
                "all_six_original_B_unit_solve_reductions_bound":True,
                "original_K_place_and_scales_preserved":True,
                "original_selected_charts_and_all_free_coordinates_unchanged":True,
                "old_operator_K0_inverse_S5_products_normal_conversion_and_point_jets_recomputed":False,
                "fixed_anchor_S5_product_groups":self.anchor_product_refs,
                "exact_objects_are_conjugates_of_original_characteristic_zero_unit_solves":True})
        self.refs["source_audit"]=self.ref(name);self.checkpoint("sources_and_original_fixed_blocks_ready")

    def read_original_fixed_products(self):
        matrices=[];allrefs={}
        for which in ("u","v"):
            columns=[];refs=[]
            for first in range(0,690,17):
                stop=min(first+17,690)
                value,ref=self.source("R842",f"R839-anchor-{which}-products-{first:04d}-{stop:04d}.json.gz")
                assert value["prime"]==PRIME and value["anchor"]==which
                assert value["first_original_V3_index"]==first and value["stop_original_V3_index"]==stop
                assert value["all1380_original_product_coordinates_verified"] is True
                assert value["additional_product_or_anchor_rescaling"] is False
                assert value["same_prime_S5_inverse_reused_without_new_inverse"] is True
                assert value["original_zeta_root"]==549966761
                shape(value["S5_coordinates_mod_prime"],1234,stop-first)
                for j in range(stop-first):columns.append([row[j] for row in value["S5_coordinates_mod_prime"]])
                refs.append(ref)
            assert len(columns)==690
            matrices.append(self.mat(columns).transpose());allrefs[which]=refs
        return matrices[0],matrices[1],allrefs

    def jet(self,coefficients,z0,count):
        assert coefficients
        h,w=coefficients[0].nrows(),coefficients[0].ncols()
        output=[]
        for n in range(count):
            value=self.zero(h,w)
            for k in range(n,len(coefficients)):
                scalar=comb(k,n)*pow(z0,k-n,PRIME)%PRIME
                if scalar:value=value+coefficients[k]*scalar
            output.append(value)
        return output

    def jet_product(self,left,right,n):
        assert left and right
        answer=self.zero(left[0].nrows(),right[0].ncols())
        for a in range(max(0,n-len(right)+1),min(n,len(left)-1)+1):
            answer=answer+left[a]*right[n-a]
        return answer

    def confluent_matrix(self):
        name="shared-twelve-Hasse-condition-inverse";old=self.old(name)
        labels=[(i,n) for i,m in enumerate(MULTIPLICITIES) for n in range(m)]
        if old is None:
            self.status=name;self.budget()
            data=[[comb(k,n)*pow(i,k-n,PRIME)%PRIME if k>=n else 0
                   for k in range(12)] for i,n in labels]
            V=self.mat(data);U=V.inv()
            assert V*U==self.eye(12) and U*V==self.eye(12)
            self.put(name,{"prime":PRIME,"condition_labels":labels,"matrix_mod_prime":data,
                "inverse_mod_prime":rows(U),"both_inverse_products_verified":True,
                "Hasse_coefficients_not_unscaled_derivative_values":True,
                "only_five_original_nodes_used":True,"new_Krylov_inverse_computed":False})
            old=self.old(name)
        assert old["condition_labels"]==[list(x) for x in labels]
        self.Hasse_inverse=self.mat(old["inverse_mod_prime"])
        self.refs["Hasse_interpolation"]=self.ref(name)

    def shared_K_jets(self,i):
        if i in self.shared_jets:return self.shared_jets[i]
        m=MULTIPLICITIES[i];wj=self.jet(self.W,i,m+2)
        assert wj[0]==self.mat(self.fibers[i][2]["W_evaluated_mod_prime"])
        K,J=[self.K0[i]],[self.J0[i]]
        source_point=self.fibers[i][3];refs=[]
        for n in range(1,m+2):
            name=f"shared-node-{i}-Krylov-jet-{n:02d}";old=self.old(name)
            previous=list(refs)
            if old is None:
                self.status=name;self.budget()
                values=[[0]*272 for _ in range(272)]
                current=self.zero(272,1)
                for c in range(1,272):
                    current=wj[0]*current
                    for a in range(1,min(n,3)+1):
                        current=current+wj[a]*self.col(K[n-a],c-1)
                    for r in range(272):values[r][c]=int(current[r,0])
                    if c%64==0:self.budget()
                kn=self.mat(values)
                value=self.zero(272,272)
                for a in range(1,n+1):value=value+(kn if a==n else K[a])*J[n-a]
                jn=-(J[0]*value)
                left=kn*J[0]+K[0]*jn
                right=jn*K[0]+J[0]*kn
                for a in range(1,n):
                    left=left+K[a]*J[n-a]
                    right=right+J[a]*K[n-a]
                assert left==self.zero(272,272) and right==self.zero(272,272)
                self.put(name,{"prime":PRIME,"z0":i,"Hasse_order":n,
                    "source_original_Krylov_point":source_point,"source_original_W":self.ir["W_reduction"],
                    "source_previous_positive_jet_orders":previous,
                    "Krylov_jet_mod_prime":values,"inverse_jet_mod_prime":rows(jn),
                    "both_truncated_inverse_products_verified_through_order":n,
                    "zero_order_Krylov_and_inverse_recomputed":False,
                    "exact_definition":"Hasse coefficients of the original polynomial K and its local inverse"})
                old=self.old(name)
            assert old["source_previous_positive_jet_orders"]==previous
            assert old["source_original_Krylov_point"]==source_point
            assert old["Hasse_order"]==n and old["z0"]==i
            K.append(self.mat(old["Krylov_jet_mod_prime"]))
            J.append(self.mat(old["inverse_jet_mod_prime"]))
            refs.append(self.ref(name))
        result=(K,J,refs,wj)
        self.shared_jets[i]=result
        return result

    def branch_prefix(self,record):
        return f"branch-{record['original_branch']:02d}"

    def node_layers(self,record,i):
        prefix=self.branch_prefix(record);m=MULTIPLICITIES[i]
        K,J,jrefs,wj=self.shared_K_jets(i)
        values=record["pair_value"]["B_vector_coefficients_mod_prime"]
        B=self.jet([self.mat([[v] for v in line]) for line in values],i,m+2)
        KB=[];F0=[];F1=[];F2=[];r0=[];r1=[];r2=[]
        for n in range(m+2):
            name=f"{prefix}-node-{i}-F0-jet-{n:02d}";old=self.old(name)
            previous=list(r0)
            if old is None:
                self.status=name;self.budget()
                current=B[n]
                data=[[int(current[r,0])]+[0]*271 for r in range(272)]
                for c in range(1,272):
                    current=wj[0]*current
                    for a in range(1,min(n,3)+1):
                        current=current+wj[a]*self.col(KB[n-a],c-1)
                    for r in range(272):data[r][c]=int(current[r,0])
                    if c%64==0:self.budget()
                kb=self.mat(data)
                f0=kb*J[0]
                for a in range(n):f0=f0+KB[a]*J[n-a]
                assert self.col(f0,0)==B[n]
                self.put(name,{"prime":PRIME,"original_branch":record["original_branch"],
                    "sigma_power":record["sigma_power"],"z0":i,"Hasse_order":n,
                    "source_original_normal_B":record["pair"],"source_original_Krylov_point":self.fibers[i][3],
                    "source_shared_positive_K_jets":jrefs[:n],"source_previous_F0_jets":previous,
                    "B_Krylov_jet_mod_prime":data,"matrix_mod_prime":rows(f0),
                    "first_column_is_original_B_jet_verified":True,
                    "matrix_formula":"sum(K_B_a * inverse_K_(n-a))",
                    "exact_original_multiplier_Hasse_coefficient":True})
                old=self.old(name)
            assert old["source_original_normal_B"]==record["pair"]
            assert old["source_previous_F0_jets"]==previous and old["source_shared_positive_K_jets"]==jrefs[:n]
            KB.append(self.mat(old["B_Krylov_jet_mod_prime"]))
            F0.append(self.mat(old["matrix_mod_prime"]));r0.append(self.ref(name))
        G=self.jet(self.operator_cache["g"],i,m+1)
        Gamma=self.jet(self.operator_cache["Gamma"],i,m+1)
        for n in range(m+1):
            name=f"{prefix}-node-{i}-F1-jet-{n:02d}";old=self.old(name)
            dependencies=r0[:n+2]
            if old is None:
                self.status=name;self.budget()
                value=self.zero(272,272)
                for a in range(n+1):
                    value=value+Gamma[a]*F0[n-a]+G[a]*(F0[n-a+1]*(n-a+1))
                self.put(name,{"prime":PRIME,"original_branch":record["original_branch"],
                    "sigma_power":record["sigma_power"],"z0":i,"Hasse_order":n,
                    "source_F0_jet_prefix":dependencies,"source_original_Gamma":self.ir["Gamma_index"],
                    "source_original_Mg":self.ir["g_index"],"matrix_mod_prime":rows(value),
                    "exact_original_derivative_order":1,"ordinary_derivative_Hasse_factor_included":True})
                old=self.old(name)
            assert old["source_F0_jet_prefix"]==dependencies
            F1.append(self.mat(old["matrix_mod_prime"]));r1.append(self.ref(name))
        for n in range(m):
            name=f"{prefix}-node-{i}-F2-jet-{n:02d}";old=self.old(name)
            dependencies=r1[:n+2]
            if old is None:
                self.status=name;self.budget()
                value=self.zero(272,272)
                for a in range(n+1):
                    value=value+Gamma[a]*F1[n-a]+G[a]*(F1[n-a+1]*(n-a+1))
                self.put(name,{"prime":PRIME,"original_branch":record["original_branch"],
                    "sigma_power":record["sigma_power"],"z0":i,"Hasse_order":n,
                    "source_F1_jet_prefix":dependencies,"source_original_Gamma":self.ir["Gamma_index"],
                    "source_original_Mg":self.ir["g_index"],"matrix_mod_prime":rows(value),
                    "exact_original_derivative_order":2,"ordinary_derivative_Hasse_factor_included":True})
                old=self.old(name)
            assert old["source_F1_jet_prefix"]==dependencies
            F2.append(self.mat(old["matrix_mod_prime"]));r2.append(self.ref(name))
        sig=[];srefs=[]
        for n in range(m):
            name=f"{prefix}-node-{i}-sigma1-jet-{n:02d}";old=self.old(name)
            if old is None:
                self.status=name;self.budget()
                first=self.sub(F1[n],list(range(272)),SIGMA_COLUMNS)*i
                if n:first=first+self.sub(F1[n-1],list(range(272)),SIGMA_COLUMNS)
                prod=self.zero(272,len(SIGMA_COLUMNS))
                for a in range(n+1):
                    prod=prod+G[a]*self.sub(F0[n-a],list(range(272)),SIGMA_COLUMNS)
                data=[[int(first[r,c])-(5+EPS[k])*int(prod[r,c])
                       for c,k in enumerate(SIGMA_COLUMNS)] for r in range(272)]
                data=[[x%PRIME for x in row] for row in data]
                self.put(name,{"prime":PRIME,"original_branch":record["original_branch"],
                    "sigma_power":record["sigma_power"],"z0":i,"Hasse_order":n,
                    "original_normal_columns":SIGMA_COLUMNS,
                    "source_F0_jet_prefix":r0[:n+1],"source_F1_jet_prefix":r1[:n+1],
                    "source_original_Mg":self.ir["g_index"],"matrix_mod_prime":data,
                    "formula":"z*F1_c-(5+epsilon_c)*Mg*F0_c",
                    "original_sigma_first_layer_in_tau_frame":True})
                old=self.old(name)
            assert old["source_F0_jet_prefix"]==r0[:n+1] and old["source_F1_jet_prefix"]==r1[:n+1]
            sig.append(self.mat(old["matrix_mod_prime"]));srefs.append(self.ref(name))
        del KB,F0,F1,F2,sig,K,J,G,Gamma,B
        gc.collect()
        return {"F0":r0[:m],"F1":r1[:m],"F2":r2,"sigma1":srefs}

    def polynomial_layers(self,record):
        prefix=self.branch_prefix(record)
        node_index=f"{prefix}-five-node-jet-index";node_data=self.old(node_index)
        if node_data is None:
            nodes=[]
            for i in NODES:
                nodes.append({"z0":i,"multiplicity":MULTIPLICITIES[i],"layers":self.node_layers(record,i)})
                self.checkpoint(f"{prefix}_node_{i}_jets_complete")
            self.put(node_index,{"prime":PRIME,"original_branch":record["original_branch"],
                "sigma_power":record["sigma_power"],"source_original_B":record["pair"],
                "nodes":nodes,"highest_polynomial_degree":11,
                "only_original_five_nodes_used":True,"new_Krylov_inverse_computed":False})
            node_data=self.old(node_index)
        assert node_data["source_original_B"]==record["pair"]
        output={}
        for label in ("F0","F1","F2","sigma1"):
            index_name=f"{prefix}-{label}-polynomial-index";index=self.old(index_name)
            if index is None:
                source_refs=[x for entry in node_data["nodes"] for x in entry["layers"][label]]
                assert len(source_refs)==12
                samples=[self.mat(self.own(x)["matrix_mod_prime"]) for x in source_refs]
                width=20 if label=="sigma1" else 272
                degree=7 if label=="sigma1" else 5+2*int(label[-1])
                entries=[]
                for first in range(0,272,17):
                    stop=min(first+17,272);name=f"{prefix}-{label}-polynomial-rows-{first:03d}"
                    block=self.old(name)
                    if block is None:
                        self.status=name;self.budget()
                        rhs=self.mat([[int(M[r,c]) for r in range(first,stop) for c in range(width)] for M in samples])
                        coefficients=self.Hasse_inverse*rhs
                        count=degree+3
                        raw=[[[0]*width for _ in range(stop-first)] for _ in range(count)]
                        for r in range(first,stop):
                            for c in range(width):
                                col=SIGMA_COLUMNS[c] if label=="sigma1" else c
                                limit=degree+EPS[col]-EPS[r];position=(r-first)*width+c
                                for power in range(12):
                                    v=int(coefficients[power,position])
                                    if power>limit:assert v==0,(label,power,r,col)
                                    if power<count:raw[power][r-first][c]=v
                                if label=="F0" and c==0:
                                    Bdata=record["pair_value"]["B_vector_coefficients_mod_prime"]
                                    for power in range(count):
                                        assert raw[power][r-first][0]==(Bdata[power][r] if power<6 else 0)
                        self.put(name,{"prime":PRIME,"original_branch":record["original_branch"],
                            "sigma_power":record["sigma_power"],"target":label,"row_first":first,"row_stop":stop,
                            "original_normal_columns":SIGMA_COLUMNS if label=="sigma1" else list(range(272)),
                            "regular_degree_bound":degree,"coefficient_matrices_low_to_high":raw,
                            "source_twelve_Hasse_conditions":source_refs,
                            "source_Hasse_interpolation":self.refs["Hasse_interpolation"],
                            "source_original_B":record["pair"],
                            "all_original_weighted_degree_zeros_verified":True,
                            "original_sigma_highest_layer_cancellation_verified":label=="sigma1",
                            "exact_original_polynomial_reduction_certified":True,
                            "characteristic_zero_coefficients_reconstructed":False})
                        block=self.old(name)
                    assert block["source_twelve_Hasse_conditions"]==source_refs
                    assert block["source_original_B"]==record["pair"]
                    entries.append(self.ref(name))
                self.put(index_name,{"prime":PRIME,"original_branch":record["original_branch"],
                    "sigma_power":record["sigma_power"],"target":label,"row_blocks":entries,
                    "source_original_B":record["pair"],"source_five_node_jets":self.ref(node_index),
                    "regular_degree_bound":degree,"normal_basis_degrees":EPS,
                    "all_weighted_support_zeros_verified":True,
                    "true_original_polynomial_reduction_certified":True})
                index=self.old(index_name);del samples
                gc.collect()
            assert index["source_original_B"]==record["pair"]
            output[label]=self.ref(index_name)
        return output

    def load_polynomial(self,reference):
        index=self.own(reference);degree=index["regular_degree_bound"]
        width=20 if index["target"]=="sigma1" else 272
        data=[[[0]*width for _ in range(272)] for _ in range(degree+3)]
        first=0
        for ref in index["row_blocks"]:
            block=self.own(ref);assert block["row_first"]==first
            stop=block["row_stop"]
            for n,coeff in enumerate(block["coefficient_matrices_low_to_high"]):data[n][first:stop]=coeff
            first=stop
        assert first==272
        return data

    def fixed_square_solve(self,name,square,rhs,source_references):
        n=square.nrows();assert square.ncols()==n and rhs.nrows()==n
        old=self.old(name)
        if old is None:
            self.status=name;self.budget()
            augmented=self.mat([[int(square[i,j]) for j in range(n)]+
                                [int(rhs[i,j]) for j in range(rhs.ncols())] for i in range(n)])
            reduced,augmented_rank=augmented.rref()
            prefix=self.sub(reduced,list(range(n)),list(range(n)))
            accepted=prefix==self.eye(n)
            if not accepted:
                self.put(name,{"prime":PRIME,"accepted":False,"selected_square_size":n,
                    "right_hand_side_count":rhs.ncols(),"source_references":source_references,
                    "selected_square_reduced_to_identity":False,
                    "augmented_rank_is_not_reported_as_original_square_rank":True,
                    "failure_only_this_original_residue_unit_chart":True})
                raise UnitFailure(name+": original selected minor is not a unit")
            solution=self.sub(reduced,list(range(n)),list(range(n,n+rhs.ncols())))
            assert square*solution==rhs
            self.put(name,{"prime":PRIME,"accepted":True,"selected_square_size":n,
                "right_hand_side_count":rhs.ncols(),"source_references":source_references,
                "solution_mod_prime":rows(solution),"selected_square_reduced_to_identity":True,
                "all_selected_equations_verified":True,
                "original_pivot_selection_recomputed":False,
                "unconsumed_full_inverse_or_determinant_computed":False,
                "exact_unit_solve_expression":{"operation":"solve_original_selected_square",
                    "source_references":source_references,
                    "modular_solution_not_reconstructed_characteristic_zero_coefficients":True}})
            old=self.old(name)
            del augmented,reduced,prefix,solution
            gc.collect()
        assert old["source_references"]==source_references
        if not old["accepted"]:raise UnitFailure(name+": retained nonunit original selected minor")
        assert old["selected_square_size"]==n and old["right_hand_side_count"]==rhs.ncols()
        assert old["all_selected_equations_verified"] is True
        return self.mat(old["solution_mod_prime"]),self.ref(name)

    def fixed_kernel(self,name,matrix,I,P,old_chart_ref,source_refs,geometry,expected_free=None):
        h,w=matrix.nrows(),matrix.ncols()
        assert len(I)==len(P) and len(set(I))==len(I) and len(set(P))==len(P)
        assert all(0<=i<h for i in I) and all(0<=j<w for j in P)
        free=[j for j in range(w) if j not in set(P)]
        if expected_free is not None:assert free==expected_free
        dependencies={"original_zero_branch_unit_chart":old_chart_ref,"source_matrix":source_refs,
                      "selected_rows":I,"selected_columns":P,"free_columns":free}
        old=self.old(name)
        if old is None:
            square=self.sub(matrix,I,P);rhs=self.sub(matrix,I,free)
            solution,sref=self.fixed_square_solve(name+"-selected-solve",square,rhs,dependencies)
            data=[[0]*len(free) for _ in range(w)]
            for j,f in enumerate(free):
                data[f][j]=1
                for k,pivot in enumerate(P):data[pivot][j]=-int(solution[k,j])%PRIME
            kernel=self.mat(data)
            self.status=name;self.budget()
            assert matrix*kernel==self.zero(h,len(free))
            assert self.sub(kernel,free,list(range(len(free))))==self.eye(len(free))
            self.put(name,{"prime":PRIME,"source_references":dependencies,
                "source_selected_solve":sref,"matrix_shape":[h,w],"actual_rank":len(P),
                "actual_kernel_dimension":len(free),"selected_rows":I,"selected_columns":P,
                "free_columns":free,"kernel_basis_mod_prime":data,
                "all_original_matrix_equations_verified":True,"free_identity_verified":True,
                "exact_complete_space":geometry,"complete_original_conjugate_kernel_certified":True,
                "exact_unit_solve_expression":{"operation":"same_original_selected_kernel_under_sigma",
                    "source_references":dependencies,"source_selected_solve":sref,
                    "pivot_coordinates":"-solve(selected_square,free_rhs)","free_coordinates":"identity",
                    "geometric_dimension_upper_bound_from_original_conjugate":len(free),
                    "characteristic_zero_coefficients_reconstructed":False}})
            old=self.old(name);del square,rhs,solution,kernel
            gc.collect()
        assert old["source_references"]==dependencies
        assert old["actual_rank"]==len(P) and old["actual_kernel_dimension"]==len(free)
        return self.mat(old["kernel_basis_mod_prime"]),self.ref(name)

    def derivative_vectors(self,record,polynomials):
        name=self.branch_prefix(record)+"-original-B-derivative-vectors";old=self.old(name)
        if old is None:
            data={}
            for order in (1,2):
                index=self.own(polynomials["F"+str(order)])
                target=[[0]*272 for _ in range(6+2*order)]
                for ref in index["row_blocks"]:
                    block=self.own(ref);first=block["row_first"];stop=block["row_stop"]
                    for n,part in enumerate(block["coefficient_matrices_low_to_high"]):
                        for row in range(first,stop):
                            v=part[row-first][0]
                            if n<len(target):target[n][row]=v
                            else:assert v==0
                data["delta_B" if order==1 else "delta2_B"]=target
            self.put(name,{"prime":PRIME,"original_branch":record["original_branch"],
                "sigma_power":record["sigma_power"],"source_original_B":record["pair"],
                "source_F1":polynomials["F1"],"source_F2":polynomials["F2"],
                "delta_B_coefficients_mod_prime":data["delta_B"],
                "delta2_B_coefficients_mod_prime":data["delta2_B"],
                "regular_degree_bounds":[7,9],"normal_basis_degrees":EPS,
                "first_column_copied_from_actual_completed_derivative_matrices":True,
                "additional_derivative_arithmetic_computed":False,
                "exact_reason":"beta0=1 and delta(beta0)=0; same original full-function Galois image"})
        return self.ref(name)

    def selected_T11(self,record,polynomials):
        prefix=self.branch_prefix(record);name=f"{prefix}-T11-original-selected-columns"
        old=self.old(name);chart=self.inputs["T11_chart"]
        tau=list(chart["selected_original_tau_columns"]);sigma=list(chart["selected_new_sigma_columns"])
        assert len(tau)==len(set(tau))==2431 and all(0<=v<2886 for v in tau)
        assert len(sigma)==len(set(sigma))==20 and all(0<=v<81 for v in sigma)
        if old is None:
            self.status=name;self.budget()
            data=[[0]*2451 for _ in range(2866)]
            for r in range(3):
                coeff=self.load_polynomial(polynomials[f"F{r}"])
                for j,k in enumerate(tau):
                    order,c,shift=self.tau_labels[k]
                    if order!=r:continue
                    for n,part in enumerate(coeff):
                        for i in range(272):
                            value=part[i][c]
                            if value:
                                assert n+shift<=11-EPS[i]
                                data[self.map11[(i,n+shift)]][j]=value
                del coeff
                self.budget()
            coeff=self.load_polynomial(polynomials["sigma1"])
            lookup={c:j for j,c in enumerate(SIGMA_COLUMNS)}
            for j,k in enumerate(sigma):
                c,shift=self.sigma_labels[k]
                for n,part in enumerate(coeff):
                    for i in range(272):
                        value=part[i][lookup[c]]
                        if value:
                            assert n+shift<=11-EPS[i]
                            data[self.map11[(i,n+shift)]][2431+j]=value
            self.put(name,{"prime":PRIME,"original_branch":record["original_branch"],
                "sigma_power":record["sigma_power"],"source_polynomial_layers":polynomials,
                "original_zero_branch_T11_unit_chart":self.ir["T11_chart"],
                "selected_original_tau_columns":tau,"selected_new_sigma_columns":sigma,
                "matrix_shape":[2866,2451],"matrix_mod_prime":data,
                "normal_V11_row_labels":[list(x) for x in self.pos11],
                "original_column_order":"old selected tau columns, then old selected sigma columns",
                "only_2451_original_selected_columns_materialized":True,
                "no_single_tau_global_generation_assumption":True,
                "exact_span":"H0(11H-C-sigma^j(D))"})
            old=self.old(name);del data,coeff
            gc.collect()
        assert old["source_polynomial_layers"]==polynomials
        return self.mat(old["matrix_mod_prime"]),self.ref(name)

    def quotient_T11(self,record,matrix,matrix_ref):
        prefix=self.branch_prefix(record);name=f"{prefix}-T11-complete-unit-quotient"
        old=self.old(name);chart=self.inputs["T11_chart"]
        I=list(chart["selected_original_rows"]);R=list(chart["complement_original_rows"])
        if old is None:
            square=self.sub(matrix,I,list(range(2451)))
            rhs=self.sub(matrix,R,list(range(2451)))
            solution,solve_ref=self.fixed_square_solve(name+"-transposed-solve",
                square.transpose(),rhs.transpose(),
                {"source_selected_columns":matrix_ref,"old_unit_chart":self.ir["T11_chart"],
                 "selected_rows":I,"complement_rows":R,"operation":"solve(T_I.T,T_R.T)"})
            product=solution.transpose()
            data=[[0]*2866 for _ in range(415)]
            for r,col in enumerate(R):
                data[r][col]=1
                for j,c in enumerate(I):data[r][c]=-int(product[r,j])%PRIME
            quotient=self.mat(data)
            self.status=name;self.budget()
            assert quotient*matrix==self.zero(415,2451)
            assert self.sub(quotient,list(range(415)),R)==self.eye(415)
            self.put(name,{"prime":PRIME,"original_branch":record["original_branch"],
                "sigma_power":record["sigma_power"],"source_T11_columns":matrix_ref,
                "source_transposed_selected_solve":solve_ref,
                "old_original_unit_chart":self.ir["T11_chart"],
                "selected_original_rows":I,"complement_original_rows":R,
                "quotient_matrix_mod_prime":data,"matrix_shape":[415,2866],
                "all2451_columns_annihilated_in_all415_rows":True,"complement_identity_verified":True,
                "exact_kernel":"H0(11H-C-sigma^j(D))","exact_kernel_dimension":2451,
                "same_original_quotient_coordinates_under_sigma":True,
                "complete_original_two_chart_space_certified":True})
            old=self.old(name);del square,rhs,solution,product,data,quotient
            gc.collect()
        assert old["source_T11_columns"]==matrix_ref
        return self.mat(old["quotient_matrix_mod_prime"]),self.ref(name)

    def quotient_T5(self,record,Pi,piref):
        prefix=self.branch_prefix(record);name=f"{prefix}-T5-two-pencil-matrix"
        old=self.old(name)
        if old is None:
            left=[self.map11[(a,k)] for a,k in self.pos5]
            right=[self.map11[(a,k+6)] for a,k in self.pos5]
            data=[[int(Pi[r,c]) for c in left] for r in range(415)]
            data+=[[int(Pi[r,c]) for c in right] for r in range(415)]
            self.put(name,{"prime":PRIME,"original_branch":record["original_branch"],
                "sigma_power":record["sigma_power"],"source_T11_quotient":piref,
                "tau_embedding_rows":left,"sigma_embedding_rows":right,
                "matrix_mod_prime":data,"matrix_shape":[830,1234],
                "both_basepointfree_pencil_conditions_preserved":True})
            old=self.old(name)
        assert old["source_T11_quotient"]==piref
        matrix=self.mat(old["matrix_mod_prime"]);mref=self.ref(name)
        output=f"{prefix}-T5-complete-unit-quotient";answer=self.old(output)
        chart=self.inputs["T5_chart"];I=list(chart["selected_original_rows"]);J=list(chart["selected_original_columns"])
        Q=self.sub(matrix,I,list(range(1234)))
        if answer is None:
            square=self.sub(Q,list(range(415)),J)
            allcols=self.sub(matrix,list(range(830)),J)
            solved,sref=self.fixed_square_solve(output+"-row-reconstruction-solve",
                square.transpose(),allcols.transpose(),
                {"source_two_pencil_matrix":mref,"old_unit_chart":self.ir["T5_chart"],
                 "selected_rows":I,"selected_columns":J,"operation":"solve(Q_J.T,M_J.T)"})
            self.status=output;self.budget()
            assert solved.transpose()*Q==matrix
            self.put(output,{"prime":PRIME,"original_branch":record["original_branch"],
                "sigma_power":record["sigma_power"],"source_two_pencil_matrix":mref,
                "source_full_row_reconstruction":sref,"old_original_unit_chart":self.ir["T5_chart"],
                "selected_original_rows":I,"selected_original_columns":J,
                "matrix_shape":[415,1234],"quotient_matrix_mod_prime":rows(Q),
                "all830_by1234_original_rows_reconstructed":True,
                "exact_kernel":"H0(5H-C-sigma^j(D))","exact_rank":415,
                "same_original_selected_rows_under_sigma":True})
            answer=self.old(output)
        assert answer["source_two_pencil_matrix"]==mref
        return self.mat(answer["quotient_matrix_mod_prime"]),self.ref(output)

    def original_D_basis(self,record,Q,qref):
        prefix=self.branch_prefix(record);name=f"{prefix}-D-original-830-constraint-matrix"
        old=self.old(name)
        if old is None:
            self.status=name;self.budget()
            left=Q*self.Mu;right=Q*self.Mv
            data=rows(left)+rows(right)
            self.put(name,{"prime":PRIME,"original_branch":record["original_branch"],
                "sigma_power":record["sigma_power"],"source_T5_quotient":qref,
                "source_fixed_K_anchor_product_groups":self.anchor_product_refs,
                "matrix_shape":[830,690],"matrix_mod_prime":data,
                "only_new_quotient_times_completed_original_products_computed":True,
                "old_S5_inverse_or_original_Fourier_products_recomputed":False,
                "exact_kernel":"H0(3H-sigma^j(D))"})
            old=self.old(name);del left,right,data
            gc.collect()
        assert old["source_T5_quotient"]==qref
        matrix=self.mat(old["matrix_mod_prime"])
        chart=self.inputs["D_chart"]
        kernel,kref=self.fixed_kernel(f"{prefix}-D-complete-original-295-kernel",matrix,
            list(chart["selected_original_equation_rows"]),list(chart["selected_original_V3_pivot_columns"]),
            self.ir["D_chart"],self.ref(name),
            {"space":"H0(3H-sigma^j(D))","dimension":295,"sigma_power":record["sigma_power"]},
            list(chart["original_V3_free_columns"]))
        return kernel,kref

    def original_sections(self,record,kernel,kref):
        prefix=self.branch_prefix(record);name=f"{prefix}-original-R845-a-b-sections";old=self.old(name)
        if old is None:
            self.status=name;self.budget()
            av=self.col(kernel,0)
            bv=kernel*self.mat([[1] for _ in range(295)])
            an=self.normal*av;bn=self.normal*bv
            value0=self.sub(self.J3,[0],list(range(690)))
            a0=int((value0*an)[0,0]);b0=int((value0*bn)[0,0])
            accepted=bool(a0)
            self.put(name,{"prime":PRIME,"original_branch":record["original_branch"],
                "sigma_power":record["sigma_power"],"source_complete_original_D_basis":kref,
                "source_original_zero_branch_sections":self.ir["old_sections"],
                "source_original_zero_branch_anchor_selection":self.ir["old_anchor_selection"],
                "source_original_normal_conversion":self.ir["normal_index"],
                "source_original_point_jets":self.ir["V3_jets"],
                "a_original_V3_coordinates_mod_prime":rows(av),"b_original_V3_coordinates_mod_prime":rows(bv),
                "a_normal_V3_coordinates_mod_prime":rows(an),"b_normal_V3_coordinates_mod_prime":rows(bn),
                "a_value_at_P0_mod_prime":a0,"b_value_at_P0_mod_prime":b0,
                "original_a_basis_column":0,"original_b_basis_coefficients":[1]*295,
                "accepted":accepted,"block_swap_used":False,"no_rescaling":True,
                "failure_only_this_original_residue_unit_chart":not accepted})
            old=self.old(name)
        assert old["source_complete_original_D_basis"]==kref
        if not old["accepted"]:raise UnitFailure(name+": original a(P0) not a unit; no replacement of original a")
        return old,self.ref(name)

    def new_fiber_product(self,record,which,coordinates,anchor_ref,i):
        prefix=self.branch_prefix(record);name=f"{prefix}-{which}-fiber-{i}-times-original-V3"
        old=self.old(name);evaluation,eref,point,pref=self.fibers[i]
        if old is None:
            self.status=name;self.budget()
            E=self.mat(evaluation["original_V3_evaluation_matrix_mod_prime"])
            W=self.mat(point["W_evaluated_mod_prime"])
            v=E*coordinates;current=v;columns=[]
            for k in range(272):
                columns.append([int(current[r,0]) for r in range(272)])
                if k<271:current=W*current
                if k%64==0:self.budget()
            value=self.mat(columns).transpose()*self.mat(evaluation["original_V3_Krylov_coordinates_mod_prime"])
            self.put(name,{"prime":PRIME,"original_branch":record["original_branch"],
                "sigma_power":record["sigma_power"],"which":which,"z0":i,
                "source_section":anchor_ref,"source_original_fiber_evaluation":eref,
                "source_original_Krylov_point":pref,"source_original_W":self.ir["W_reduction"],
                "matrix_shape":[272,690],"product_evaluation_matrix_mod_prime":rows(value),
                "section_evaluation_mod_prime":rows(v),
                "formula":"[a,Wa,...,W^271*a]*(old K^-1 E)",
                "old_inverse_and_original_V3_evaluation_recomputed":False})
            old=self.old(name)
        assert old["source_section"]==anchor_ref and old["source_original_fiber_evaluation"]==eref
        return old,self.ref(name)

    def paired_fiber_matrix(self,record,label,left,right,leftref,rightref):
        prefix=self.branch_prefix(record);name=f"{prefix}-{label}-five-fiber-matrix"
        old=self.old(name)
        if old is None:
            data=[];refs=[]
            for i in NODES:
                av,ar=self.new_fiber_product(record,label+"-left",left,leftref,i)
                bv,br=self.new_fiber_product(record,label+"-right",right,rightref,i)
                data.extend([a+b for a,b in zip(av["product_evaluation_matrix_mod_prime"],
                                              bv["product_evaluation_matrix_mod_prime"])])
                refs.append({"z0":i,"left":ar,"right":br})
                self.checkpoint(f"{prefix}_{label}_fiber_{i}_complete")
            self.put(name,{"prime":PRIME,"original_branch":record["original_branch"],
                "sigma_power":record["sigma_power"],"source_left":leftref,"source_right":rightref,
                "source_fiber_products":refs,"matrix_shape":[1360,1380],"matrix_mod_prime":data,
                "fiber_disjointness_or_reducedness_not_assumed":True,
                "complete_original_two_section_multiplication_evaluated":True})
            old=self.old(name)
        assert old["source_left"]==leftref and old["source_right"]==rightref
        return self.mat(old["matrix_mod_prime"]),self.ref(name)

    def projected_basis(self,record,label,kernel,kref,dimension,definition):
        prefix=self.branch_prefix(record);name=f"{prefix}-{label}-projected-original-V3-basis"
        old=self.old(name)
        if old is None:
            self.status=name;self.budget()
            projected=self.sub(kernel,list(range(690,1380)),list(range(dimension)))
            reduced,rank=projected.transpose().rref()
            if rank!=dimension:
                self.put(name,{"prime":PRIME,"accepted":False,"source_complete_kernel":kref,
                    "required_rank":dimension,"actual_projected_rank":rank,
                    "failure_only_this_original_residue_independence_certificate":True})
                raise UnitFailure(name+": original projected basis loses rank at this residue")
            witness=L.pivots(reduced,rank)
            normal=self.normal*projected
            self.put(name,{"prime":PRIME,"accepted":True,"original_branch":record["original_branch"],
                "sigma_power":record["sigma_power"],"source_complete_kernel":kref,
                "source_original_normal_index":self.ir["normal_index"],
                "projection_to_input_block":1,"matrix_shape":[690,dimension],
                "actual_projected_rank":dimension,"independent_original_V3_rows":witness,
                "original_V3_basis_mod_prime":rows(projected),"normal_V3_basis_mod_prime":rows(normal),
                "complete_RR_space_certified":True,"exact_RR_space":definition,
                "new_projected_independence_rows_only_witness_no_basis_change":True,
                "exact_unit_solve_expression":{"operation":"same_original_second_block_projection_under_sigma",
                    "source_complete_kernel":kref,"projection_rows":[690,1380],
                    "normal_conversion":self.ir["normal_index"],
                    "same_original_kernel_free_identity_preserved":True}})
            old=self.old(name)
        assert old["source_complete_kernel"]==kref
        if not old["accepted"]:raise UnitFailure(name+": retained projection independence failure")
        return old,self.ref(name)

    def residual_and_standardizing(self,record,sections,sref):
        prefix=self.branch_prefix(record)
        matrix,mref=self.paired_fiber_matrix(record,"original-1111",
            self.mat(sections["a_original_V3_coordinates_mod_prime"]),
            self.mat(sections["b_original_V3_coordinates_mod_prime"]),sref,sref)
        oldprofile=self.inputs["rank1111"]
        kernel,kref=self.fixed_kernel(f"{prefix}-original-1111-complete-269-kernel",matrix,
            list(oldprofile["selected_original_fiber_rows"]),list(oldprofile["selected_original_V3_pair_columns"]),
            self.ir["rank1111"],mref,
            {"space":"complete relation a_j*r+b_j*s=0","dimension":269,"common_zero_divisor":"sigma^j(D)"})
        F,fref=self.projected_basis(record,"residual-F",kernel,kref,269,
            {"space":"H0(3H-sigma^j(F))","dimension":269,"degree_F":421})
        del matrix,kernel;gc.collect()
        constraints=f"{prefix}-original-123-jet-constraints";old=self.old(constraints)
        if old is None:
            self.status=constraints;self.budget()
            normal=self.mat(F["normal_V3_basis_mod_prime"])
            J=self.sub(self.J3,list(range(123)),list(range(690)))
            M=J*normal;nextrow=self.sub(self.J3,[123],list(range(690)))*normal
            self.put(constraints,{"prime":PRIME,"original_branch":record["original_branch"],
                "sigma_power":record["sigma_power"],"source_residual_F_space":fref,
                "source_original_point_jets":self.ir["V3_jets"],
                "matrix_shape":[123,269],"matrix_mod_prime":rows(M),
                "order123_row_mod_prime":rows(nextrow)[0],
                "original_jet_orders":list(range(123)),"local_parameter":self.parameter})
            old=self.old(constraints)
        assert old["source_residual_F_space"]==fref
        chart=self.inputs["standardizing_kernel"]
        U,uref=self.fixed_kernel(f"{prefix}-standardizing-complete-146-kernel",
            self.mat(old["matrix_mod_prime"]),list(chart["selected_row_indices"]),
            list(chart["selected_pivot_columns"]),self.ir["standardizing_kernel"],self.ref(constraints),
            {"space":"H0(3H-sigma^j(F)-123P0)","dimension":146,"degree":272},
            list(chart["free_columns"]))
        name=f"{prefix}-standardizing-146-original-V3-basis";basis=self.old(name)
        if basis is None:
            self.status=name;self.budget()
            original=self.mat(F["original_V3_basis_mod_prime"])*U
            normal=self.mat(F["normal_V3_basis_mod_prime"])*U
            nextvalues=rows(self.mat([old["order123_row_mod_prime"]])*U)[0]
            accepted=bool(nextvalues[self.v_index])
            self.put(name,{"prime":PRIME,"accepted":accepted,"original_branch":record["original_branch"],
                "sigma_power":record["sigma_power"],"dimension":146,"matrix_shape":[690,146],
                "source_residual_F_space":fref,"source_complete_146_kernel":uref,
                "source_original_v_choice":self.ir["standardizing_basis"],
                "original_V3_basis_mod_prime":rows(original),"normal_V3_basis_mod_prime":rows(normal),
                "order123_coefficients_mod_prime":nextvalues,"selected_original_v_column":self.v_index,
                "selected_column_rescaled":False,"original_v_column_reselected":False,
                "actual_complete_standardizing_RR_space_certified":True,
                "failure_only_original_selected_v_not_unit_at_this_place":not accepted})
            basis=self.old(name)
        if not basis["accepted"]:raise UnitFailure(name+": original v order123 coefficient is not a unit")
        assert basis["selected_original_v_column"]==self.v_index
        return basis,self.ref(name),fref

    def standardizing_sections(self,record,basis,bref):
        prefix=self.branch_prefix(record);answer={}
        for which in ("v","w"):
            name=f"{prefix}-original-{which}-section";old=self.old(name)
            original_coefficient=self.inputs["old_"+which]["standardizing_basis_coefficients_mod_prime"]
            expected=[int(i==self.v_index) for i in range(146)] if which=="v" else [1]*146
            assert original_coefficient==expected
            if old is None:
                self.status=name;self.budget()
                C=self.mat([[x] for x in original_coefficient])
                original=self.mat(basis["original_V3_basis_mod_prime"])*C
                normal=self.mat(basis["normal_V3_basis_mod_prime"])*C
                v123=int(basis["order123_coefficients_mod_prime"][self.v_index])
                self.put(name,{"prime":PRIME,"original_branch":record["original_branch"],
                    "sigma_power":record["sigma_power"],"which":which,"trial":None if which=="v" else 1,
                    "source_complete_standardizing_space":bref,
                    "source_original_zero_branch_section":self.ir["old_"+which],
                    "standardizing_basis_coefficients_mod_prime":original_coefficient,
                    "original_V3_coordinates_mod_prime":rows(original),
                    "normal_V3_coordinates_mod_prime":rows(normal),
                    "order_at_original_P0_at_least123":True,"order123_is_exact":which=="v",
                    "order123_coefficient_mod_prime":v123 if which=="v" else None,
                    "no_rescaling_or_new_column_selection":True,
                    "exact_section_definition":{"operation":"sigma_of_the_same_original_v_or_w",
                        "source_original_section":self.ir["old_"+which],"sigma_power":record["sigma_power"],
                        "new_standardizing_basis":bref,"original_integer_coefficients":original_coefficient}})
                old=self.old(name)
            assert old["source_complete_standardizing_space"]==bref
            answer[which]=(old,self.ref(name))
        return answer

    def complete_Dstar(self,record,sections):
        prefix=self.branch_prefix(record);v,vref=sections["v"];w,wref=sections["w"]
        matrix,mref=self.paired_fiber_matrix(record,"original-962",
            self.mat(v["original_V3_coordinates_mod_prime"]),
            self.mat(w["original_V3_coordinates_mod_prime"]),vref,wref)
        chart=self.inputs["rank962"]
        kernel,kref=self.fixed_kernel(f"{prefix}-original-962-complete-418-kernel",matrix,
            list(chart["selected_rows"]),list(chart["selected_columns"]),
            self.ir["rank962"],mref,
            {"space":"complete relation v_j*r+w_j*s=0","dimension":418,
             "common_zero_divisor":"sigma^j(F)+123P0","degree_common_zero":544})
        basis,bref=self.projected_basis(record,"Dstar",kernel,kref,418,
            {"space":"H0(3H-sigma^j(Dstar))","dimension":418,"degree_Dstar":272,
             "original_definition":"div_3H(v_j)-sigma^j(F)-123P0",
             "P0_not_in_Dstar":True})
        del matrix,kernel;gc.collect()
        return basis,bref,kref,mref

    def principal(self,record,initial_sections,sref,standardizing_sections,dstar_ref):
        prefix=self.branch_prefix(record);name=f"{prefix}-original-Qtilde-principal-inputs"
        old=self.old(name);v,vref=standardizing_sections["v"]
        if old is None:
            self.status=name;self.budget()
            a0=int(initial_sections["a_value_at_P0_mod_prime"])
            v123=int(v["order123_coefficient_mod_prime"])
            u272=int(self.inputs["chi_anchor"]["exact_order272_unit"])
            u252=int(self.inputs["u_C"]["actual_order252_unit_mod_prime"])
            assert a0 and v123 and u272 and u252
            leading=a0**3%PRIME*u252%PRIME*pow(v123**3%PRIME*pow(u272,4,PRIME)%PRIME,-1,PRIME)%PRIME
            assert leading
            self.put(name,{"prime":PRIME,"original_branch":record["original_branch"],
                "sigma_power":record["sigma_power"],"roots_B_s":record["roots_B_s"],
                "source_original_sigma_orbit":self.ir["seven_inputs"],
                "source_actual_a":sref,"source_actual_v":vref,"source_complete_Dstar":dstar_ref,
                "source_original_common_u_C":self.ir["u_C"],"source_original_common_u_chi":self.ir["chi_anchor"],
                "source_original_zero_branch_Qtilde":self.ir["Cstar_principal"],
                "source_complete_common_Cstar":self.ir["Cstar_basis"],
                "source_complete_common_Dchi":self.ir["chi_kernel"],
                "actual_a0_mod_prime":a0,"actual_v123_mod_prime":v123,
                "actual_uC252_mod_prime":u252,"actual_uchi272_mod_prime":u272,
                "actual_local_parameter":self.parameter,"actual_rho_order":-1205,
                "actual_leading_coefficient_mod_prime":leading,
                "exact_principal_function":{"operation":"multiply",
                    "left":{"operation":"power","exponent":3,
                        "input":{"operation":"divide",
                            "numerator":{"operation":"a_j_over_tau3","source":sref},
                            "denominator":{"operation":"v_j_over_tau3","source":vref}}},
                    "right":{"operation":"divide",
                        "numerator":{"operation":"u_C_over_tau2","source":self.ir["u_C"]},
                        "denominator":{"operation":"power","exponent":4,
                            "input":{"operation":"u_chi_over_tau2","source":self.ir["chi_anchor"]}}}},
                "exact_divisor_identity":"E_(sigma^j f)-1206P0=-(Cstar-H)+3(sigma^j Dstar-H)+4(Dchi-H)+div(sigma^j Qtilde)",
                "principal_factor_direction":"positive multiplication",
                "exact_original_Galois_conjugate_not_a_new_linearly_equivalent_choice":True,
                "all_original_free_coordinates_and_section_scales_preserved":True,
                "original_t_frame_value_computed":False,"new_t_parameter_jets_computed":False,
                "conditional_t_leading_coefficient":"rho_leading*(original t/rho at P0)^1205",
                "five_original_Lj_RR128_or_144_computed":False,
                "connection_Poincare_period_or_height_computed":False})
            old=self.old(name)
        assert old["source_complete_Dstar"]==dstar_ref
        return self.ref(name)

    def branch(self,record):
        prefix=self.branch_prefix(record);final_name=f"{prefix}-complete-Dstar-input"
        old=self.old(final_name)
        if old is not None:
            assert old["source_original_normal_B"]==record["pair"]
            assert old["complete_original_conjugate_Dstar_418_certified"] is True
            return self.ref(final_name)
        self.active_branch=record["original_branch"];self.checkpoint(prefix+"_starting")
        polynomials=self.polynomial_layers(record)
        derivative_vectors=self.derivative_vectors(record,polynomials)
        T,tref=self.selected_T11(record,polynomials)
        Pi,piref=self.quotient_T11(record,T,tref);del T;gc.collect()
        Q,qref=self.quotient_T5(record,Pi,piref);del Pi;gc.collect()
        D,dref=self.original_D_basis(record,Q,qref);del Q;gc.collect()
        initial,sref=self.original_sections(record,D,dref);del D;gc.collect()
        U,uref,fref=self.residual_and_standardizing(record,initial,sref)
        vw=self.standardizing_sections(record,U,uref);del U;gc.collect()
        basis,bref,kref,mref=self.complete_Dstar(record,vw);del basis;gc.collect()
        principal=self.principal(record,initial,sref,vw,bref)
        self.put(final_name,{"prime":PRIME,"original_branch":record["original_branch"],
            "sigma_power":record["sigma_power"],"roots_B_s":record["roots_B_s"],
            "source_original_normal_B":record["pair"],"source_polynomial_layers":polynomials,
            "original_B_derivative_vectors":derivative_vectors,
            "complete_T11_quotient":piref,"complete_T5_quotient":qref,"complete_original_D_295_basis":dref,
            "original_a_b_sections":sref,"complete_residual_F_269_basis":fref,
            "complete_standardizing_146_basis":uref,
            "original_v":vw["v"][1],"original_w":vw["w"][1],
            "complete_Dstar_418_basis":bref,"complete_Dstar_relation_kernel":kref,
            "complete_new_two_anchor_matrix":mref,"original_principal_input":principal,
            "complete_original_conjugate_Dstar_418_certified":True,
            "same_original_zero_branch_unit_diagram_conjugated":True,
            "old_branch_zero_arithmetic_recomputed":False,
            "expanded_characteristic_zero_coefficients_computed":False})
        return self.ref(final_name)

    def inventory(self):
        entries=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name in (self.path("current").name,self.path("stage-manifest").name):continue
            v=read(path)
            assert v["result"]==RESULT and v["configuration"]==self.tag and v["complete"] is True
            entries.append(spec(path))
        save(self.path("stage-manifest"),{"result":RESULT,"configuration":self.tag,"complete":True,
            "files":entries,"all_actual_complete_stages_retained":True,"current_excluded":True})
        return self.ref("stage-manifest")

    def finish(self,complete,reason=None):
        current=self.checkpoint(self.status)
        if complete:assert len(self.completed)==6
        final={"result":RESULT,"configuration":self.tag,"complete":bool(complete),"p":41,"prime":PRIME,
            "source_audit":self.refs.get("source_audit"),
            "Hasse_interpolation":self.refs.get("Hasse_interpolation"),
            "completed_new_conjugate_inputs":self.completed,
            "actual_new_complete_Dstar_count":len(self.completed),
            "all_six_new_Dstar_418_spaces_certified":len(self.completed)==6,
            "all_seven_original_Dstar_inputs_certified":len(self.completed)==6,
            "original_branch_zero_Dstar":self.ir.get("old_Dstar"),
            "original_branch_zero_Qtilde":self.ir.get("Cstar_principal"),
            "common_Cstar_418":self.ir.get("Cstar_basis"),"common_Dchi_418":self.ir.get("chi_kernel"),
            "original_seven_Galois_order":self.ir.get("seven_inputs"),
            "old_branch_zero_arithmetic_recomputed":False,
            "old_S5_products_Krylov_inverses_or_P0_jets_recomputed":False,
            "actual_norm_polynomial_or_complete_five_Lj_RR128_or_144_computed":False,
            "expanded_characteristic_zero_coordinates_computed":False,
            "new_original_t_frame_values_computed":False,
            "connection_Poincare_period_or_height_computed":False,
            "stage_manifest":self.inventory(),"resume_state":current,
            "stop_reason":reason,"seconds":time.monotonic()-self.started}
        save(self.out/FINAL,final)
        return final

    def run(self):
        self.prepare();self.confluent_matrix()
        for i in NODES:self.shared_K_jets(i)
        for record in self.branch_records:
            if len(self.completed)>=self.maximum_branches:
                return self.finish(False,"requested new-branch limit reached")
            reference=self.branch(record)
            self.completed.append({"sigma_power":record["sigma_power"],"original_branch":record["original_branch"],
                "roots_B_s":record["roots_B_s"],"stage":reference})
            self.checkpoint("complete_conjugate_Dstar_"+str(record["sigma_power"]))
        self.active_branch=None
        return self.finish(True)

def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise SystemExit("All new six-conjugate RR mathematics runs only in the authorized public repository Actions")
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    parser.add_argument("--config",required=True);parser.add_argument("--out",required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args();out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    started=time.monotonic();job=None;final=None;code=0;error=None
    try:
        job=Job(args)
        if (out/FINAL).exists():
            old=read(out/FINAL)
            assert old["result"]==RESULT and old["configuration"]==job.tag
            if old["complete"] is True:
                for entry in read(bound(out,old["stage_manifest"]))["files"]:bound(out,entry)
                final=old
            else:final=job.run()
        else:final=job.run()
        if not final["complete"]:code=2
    except BudgetStop as exc:code=124;error=str(exc)
    except UnitFailure as exc:code=2;error=str(exc)
    except Exception as exc:code=1;error=str(exc);traceback.print_exc()
    if final is None and job is not None:
        try:final=job.finish(False,error)
        except Exception:traceback.print_exc()
    receipt={"result":RESULT,"source_sha256":sha(__file__),
        "configuration_sha256":fingerprint(job.tag) if job else None,
        "complete":bool(final and final["complete"]),
        "certificate_sha256":sha(out/FINAL) if final else None,
        "actual_new_complete_Dstar_count":final["actual_new_complete_Dstar_count"] if final else 0,
        "all_seven_original_Dstar_inputs_certified":bool(final and final["all_seven_original_Dstar_inputs_certified"]),
        "old_branch_zero_or_original_Krylov_inverse_recomputed":False,
        "original_five_Lj_RR128_or_144_or_height_computed":False,
        "exit_code":code,"error":error,"seconds":time.monotonic()-started}
    save(out/"core-receipt.json",receipt)
    print("R880_SIX_DSTAR_CORE_SUMMARY="+json.dumps(receipt,sort_keys=True),flush=True)
    return code

if __name__=="__main__":
    raise SystemExit(main())
