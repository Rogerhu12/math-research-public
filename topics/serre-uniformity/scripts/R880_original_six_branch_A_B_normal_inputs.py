#!/usr/bin/env python3
"""R880: twelve new normal RHSs for the six remaining original same-s branches."""
import argparse
from fractions import Fraction
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
import traceback

S=Path(__file__).resolve().parent
LEGACY_CORE_SHA="a40ed5b1bbb27b29cb54c94dca36322276c17c4534f43134e422acbb6f33983a"
LEGACY=S/"R877_original_canonical_A_normal_input.py"
assert hashlib.sha256(LEGACY.read_bytes()).hexdigest()==LEGACY_CORE_SHA
loader=importlib.util.spec_from_file_location("R880_six_original_R877_source_definitions",LEGACY)
L=importlib.util.module_from_spec(loader);loader.loader.exec_module(L)
RESULT="R880-original-six-branch-A-B-normal-inputs"
FINAL="p41-original-six-branch-A-B-normal-inputs-certificate.json"
PREFIX="R880-six-branch-"
PRIME,DIM,ROWS,RANK=1000000753,1234,1380,272
EPS=[0]+[1]*144+[2]*127
SOURCES=("R877","R824","R827","R842","R787","R849")
PROOFS=("R880","GP")
INPUTS=("canonical_coefficients","B_normal","S5_inverse","S5_matrix","global_DAG",
        "place_audit","original_chart","original_rational_blocks","original_selection",
        "parent_source_audit","parent_normal_A","parent_normal_fraction","parent_full_rhs","R824_chart")
STRATEGY={
    "scope":"six_remaining_original_same_s_branches_twelve_A_B_normal_RHSs",
    "prime":PRIME,"original_branch0":0,"original_s_root":99932770,
    "original_zeta_root":549966761,"canonical_free_column":1186,
    "branch_order":"original roots_B_s indices; sigma powers computed from original R849 sigma(b)",
    "source_A_C":"original reserved R787 direction copied into completed R824 profiles",
    "B_expansion":"original Z_pivot_integer_rows and Z_free_diagonal, once",
    "source_F69":"twenty complete original R877 prefix-column stages",
    "S5_matrix":"completed original R842 1380 by 1234 matrix",
    "S5_inverse":"completed original R827 prime753 selected inverse",
    "new_rhs_count":12,"prefix_blocks":69,"real_coordinates_per_block":20,
    "source_column_chunk_size":64,"all1380_by12_original_coordinates_required":True,
    "normal_polynomial_bound":"5-epsilon_output",
    "original_branch0_A_B_recomputed":False,
    "original_Fourier_rows_or_F69_recomputed":False,
    "original_1186_inverse_or_Dixon_recomputed":False,
    "original_S5_inverse_recomputed":False,"additional_original_scale_inserted":False,
    "characteristic_zero_coordinates_reconstructed":False,
    "original_Dstar_pencils_or_five_Lj_RR_spaces_computed":False,
    "only_budget_and_transport_excluded_from_mathematical_identity":True,
}
sha,read,save,fingerprint,plain,spec,bound=L.sha,L.read,L.save,L.fingerprint,L.plain,L.spec,L.bound
identity,stable_source,Source=L.identity,L.stable_source,L.Source

class BudgetStop(RuntimeError):pass

def shape(value,n,m):
    assert isinstance(value,list) and len(value)==n
    assert all(isinstance(row,list) and len(row)==m for row in value)

def rows(matrix):
    return [[int(matrix[i,j]) for j in range(matrix.ncols())] for i in range(matrix.nrows())]

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
        "method_sha256":item["method_sha256"],"legacy_R877_core_sha256":LEGACY_CORE_SHA,
        "proofs_sha256":{key:item["proofs"][key]["sha256"] for key in PROOFS},
        "sources":{label:stable_source(item["sources"][label]) for label in SOURCES},
        "inputs":item["inputs"],"prefix_groups":item["prefix_groups"],
        "branch_profiles":item["branch_profiles"],"normal_basis_degrees":EPS,"strategy":STRATEGY}

def rational(value):
    if isinstance(value,dict):
        assert set(value)>={"numerator","denominator"}
        return Fraction(int(value["numerator"]),int(value["denominator"]))
    if isinstance(value,(tuple,list)):
        assert len(value)==2
        return Fraction(int(value[0]),int(value[1]))
    return Fraction(str(value))

def rational_mod(value):
    q=rational(value);den=q.denominator%PRIME
    assert den,"Original rational denominator is not a unit at the fixed place"
    return q.numerator%PRIME*pow(den,-1,PRIME)%PRIME

def rational_polynomial_mod(record,b):
    assert isinstance(record,dict) and set(record)>={"numerator","denominator"}
    numerator=record["numerator"];assert isinstance(numerator,list) and len(numerator)<=7
    den=int(record["denominator"])%PRIME;assert den
    value=0
    for c in reversed(numerator):value=(value*b+int(c))%PRIME
    return value*pow(den,-1,PRIME)%PRIME

class Job:
    def __init__(self,args):
        import flint
        assert flint.__version__=="0.9.0"
        self.mat=flint.nmod_mat;self.args=args;self.started=time.monotonic()
        self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41 and not self.item["producer_inputs_pending"]
        assert self.item["core_sha256"]==sha(__file__)
        assert self.item["legacy_R877_core_sha256"]==LEGACY_CORE_SHA
        assert self.item["method_sha256"]==sha(self.item["method"])
        assert set(self.item["proofs"])==set(PROOFS)
        for ref in self.item["proofs"].values():assert sha(ref["path"])==ref["sha256"]
        assert set(self.item["sources"])==set(SOURCES) and set(self.item["inputs"])==set(INPUTS)
        assert len(self.item["prefix_groups"])==20 and len(self.item["branch_profiles"])==6
        self.tag=expected_tag(self.item);self.out=Path(args.out);self.out.mkdir(parents=True,exist_ok=True)
        self.status="initializing";self.refs={};self.coefficient_refs=[];self.pair_refs=[]
        self.next_chunk=0;self.sources={};self.orbit=None;self.labels=[]

    def budget(self):
        if time.monotonic()-self.started>=60*self.args.budget_minutes-30:
            raise BudgetStop("Completed source-bound stages retained; stage="+self.status)

    def path(self,name):
        name=name if name.startswith(PREFIX) else PREFIX+name
        assert Path(name).name==name
        return self.out/(name if name.endswith(".json.gz") else name+".json.gz")

    def ref(self,name):return spec(self.path(name))

    def old(self,name):
        path=self.path(name)
        if not path.exists():return None
        value=read(path)
        assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
        return value

    def put(self,name,value):
        assert not any(k in value for k in ("result","configuration","complete"))
        old=self.old(name)
        if old is not None:return old
        value=dict(value,result=RESULT,configuration=self.tag,complete=True)
        save(self.path(name),value)
        print(json.dumps({"stage":self.path(name).name,"seconds":time.monotonic()-self.started}),flush=True)
        return value

    def checkpoint(self,status):
        self.status=status
        value={"result":RESULT,"configuration":self.tag,"complete":False,"status":status,
            "next_original_prefix_chunk":self.next_chunk,"source_audit":self.refs.get("source_audit"),
            "original_Galois_orbit":self.refs.get("orbit"),
            "coefficient_sources":self.coefficient_refs,"full1380_rhs":self.refs.get("rhs"),
            "all12_normal_solve":self.refs.get("solve"),"normal_pairs":self.pair_refs,
            "seven_Galois_normal_inputs":self.refs.get("seven")}
        save(self.path("current"),value);return self.ref("current")

    def source(self,key):
        ref=self.item["inputs"][key]
        assert ref["source_group"] in SOURCES
        return self.sources[ref["source_group"]].stage(ref)

    def prepare(self):
        self.status="original source audit"
        self.sources={label:Source(label,self.item["sources"][label]) for label in SOURCES}
        self.r877,self.r824,self.r827,self.r842,self.r787,self.r849=(self.sources[x] for x in SOURCES)
        self.canonical=self.source("canonical_coefficients")
        self.B0=self.source("B_normal");self.A0=self.source("parent_normal_A")
        self.fraction0=self.source("parent_normal_fraction");self.rhs0=self.source("parent_full_rhs")
        self.parent_audit=self.source("parent_source_audit")
        self.inverse=self.source("S5_inverse");self.S5data=self.source("S5_matrix")
        self.graph=self.source("global_DAG");self.place=self.source("place_audit")
        self.chart=self.source("original_chart");self.blocks=self.source("original_rational_blocks")
        self.selection=self.source("original_selection");self.profile_chart=self.source("R824_chart")
        assert self.r877.value["core_sha256"]==LEGACY_CORE_SHA
        assert self.r877.certificate["canonical_A_normal_input_certified"] is True
        assert self.r877.certificate["original_global_y_normal_fraction_input_certified"] is True
        assert self.r877.certificate["all1380_original_short_coordinates_verified"] is True
        for field,key in (("normal_A","parent_normal_A"),("normal_fraction_input","parent_normal_fraction"),
                          ("source_audit","parent_source_audit"),("full1380_rhs","parent_full_rhs")):
            assert plain(self.r877.certificate[field])==plain(self.item["inputs"][key])
        for label in ("R827","R842","R787","R849"):
            assert identity(self.r877.tag["sources"][label])==identity(self.sources[label].value)
            assert self.r877.tag["sources"][label]["configuration_sha256"]==fingerprint(self.sources[label].tag)
        for value in (self.r824.tag,self.r827.tag,self.r849.tag):
            assert identity(value["source_identities"]["R787"])==identity(self.r787.value)
        assert self.graph["global_y_exact_unit_expression_defined"] is True
        assert self.r849.certificate["global_y_exact_unit_expression_defined"] is True
        assert plain(self.r849.certificate["exact_expression_DAG"])==plain(self.item["inputs"]["global_DAG"])
        assert self.chart["chosen_free_column"]==1186 and self.chart["actual_modular_rank"]==1186
        assert self.chart["other_free_columns_set_to_zero"] is True
        assert self.blocks["exact_E0_Z_zero_verified"] is True
        assert self.selection["prime"]==PRIME and self.selection["prime_proved"] is True
        for key in ("all_14_L_branches_distinct","all_rational_denominators_units",
                    "all_kappa_reductions_invertible"):assert self.selection[key] is True
        assert self.profile_chart["prime"]==PRIME and self.profile_chart["ordinary_power"]==5
        assert self.profile_chart["actual_rank"]==1186 and self.profile_chart["kernel_dimension"]==28
        assert self.profile_chart["chart_choice_from_original_R787"] is True
        assert plain(self.profile_chart["original_chart"])==plain(self.item["inputs"]["original_chart"])
        for key in ("pivot_rows","pivot_columns"):assert self.profile_chart[key]==self.chart[key]
        self.field=self.graph["original_field"]
        assert self.field==self.r787.tag["field"]==self.r824.tag["field"]
        assert self.field["dimension_over_Q"]==280 and self.field["original_b_replaced_by_another_twist"] is False
        scale=self.r787.tag["basis_integer_scale"]
        assert scale==self.canonical["original_V5_integer_scale"]==self.S5data["original_integer_scale"]=="13744803133596058624"
        for value in (self.canonical,self.B0,self.place,self.A0):
            assert value["prime"]==PRIME and value["original_branch"]==0
            assert value["canonical_free_column"]==1186
        assert self.place["original_zeta_root"]==self.canonical["original_zeta_root"]==549966761
        assert self.place["original_s_root"]==self.canonical["original_s_root"]==99932770
        assert self.place["original_lambda_is_a_unit"] is True
        for key in ("same_original_reserved_normalization_verified",
                    "abstract_original_p_integral_lift_certified_by_unit_minor_and_rank_bound"):
            assert self.canonical[key] is True
        for value in (self.B0,self.A0):
            assert value["all1380_original_short_coordinates_verified"] is True
            assert value["same_original_82power10_scales_preserved"] is True
            assert value["normal_basis_rank"]==RANK and value["normal_basis_degrees"]==EPS
            assert value["regular_degree_bound"]==5
        assert self.A0["abstract_p_integral_original_normal_A_lift_certified"] is True
        assert self.B0["abstract_p_integral_original_normal_lift_certified"] is True
        assert plain(self.B0["source_original_B_expansion"])==plain(self.item["inputs"]["canonical_coefficients"])
        assert plain(self.inverse["S5_basis_index"])==plain(self.B0["source_S5_index"])==plain(self.S5data["source_S5_index"])
        assert self.inverse["prime"]==self.S5data["prime"]==PRIME
        assert self.inverse["both_inverse_products_verified"] is True and self.inverse["actual_determinant_mod_prime"]!=0
        assert self.inverse["column_indices"]==list(range(DIM))
        assert plain(self.S5data["source_completed_inverse"])==plain(self.item["inputs"]["S5_inverse"])
        self.mapping=[[a,k] for a in range(RANK) for k in range(6-EPS[a])]
        assert self.S5data["matrix_shape"]==[ROWS,DIM] and self.S5data["normal_basis_row_mapping"]==self.mapping
        assert len(self.mapping)==DIM
        self.I=list(self.inverse["row_indices"])
        assert len(self.I)==len(set(self.I))==DIM and all(0<=i<ROWS for i in self.I)
        shape(self.inverse["inverse_mod_prime"],DIM,DIM)
        shape(self.S5data["columns_mod_prime"],DIM,ROWS)
        self.U=self.mat(self.inverse["inverse_mod_prime"],PRIME)
        self.S5=self.mat(self.S5data["columns_mod_prime"],PRIME).transpose()
        self.P=list(self.blocks["B_constant_pivot_columns"]);self.Q=list(self.blocks["B_constant_free_columns"])
        assert len(self.P)==20 and len(self.Q)==1214
        assert len(set(self.P+self.Q))==DIM and sorted(self.P+self.Q)==list(range(DIM))
        shape(self.blocks["Z_pivot_integer_rows"],20,1214)
        self.Z=self.mat([[int(x)%PRIME for x in row] for row in self.blocks["Z_pivot_integer_rows"]],PRIME)
        self.Zd=int(self.blocks["Z_free_diagonal"])%PRIME;assert self.Zd
        self.roots=self.selection["roots_B_s"];assert len(self.roots)==14
        assert self.roots[0]==[3197390,99932770]
        self.same=[i for i,pair in enumerate(self.roots) if pair[1]==99932770]
        self.remaining=[i for i in self.same if i!=0]
        assert len(self.same)==7 and len(self.remaining)==6
        assert [row["original_branch"] for row in self.item["branch_profiles"]]==self.remaining
        self.profiles={row["original_branch"]:row["source"] for row in self.item["branch_profiles"]}
        assert all(ref["source_group"]=="R824" for ref in self.profiles.values())
        self.nodes={node["id"]:node for node in self.graph["graph_nodes"]}
        assert len(self.nodes)==len(self.graph["graph_nodes"])
        self.galois_id=self.graph["original_Galois_automorphism_node"]
        self.galois=self.nodes[self.galois_id]
        assert self.galois["operation"]=="original_Galois_automorphism_definition"
        gd=self.galois["data"]
        assert gd["fixes_zeta"] is True and gd["order"]==7 and gd["fixes_original_z_w_and_normal_basis"] is True
        assert gd["original_field"]==self.field
        assert gd["source_encoding"]=="two rational b-polynomials a(b)+zeta*bpoly(b)"
        self.sigma_b=gd["image_of_original_b"]
        assert isinstance(self.sigma_b,list) and len(self.sigma_b)==2
        realrows=self.parent_audit["original_real_V5_rows"];assert len(realrows)==DIM
        assert [plain(x) for x in realrows]==[plain(x) for x in self.B0["source_original_V5_rows"]]
        self.original_rows=realrows
        for first,entry in zip(range(0,DIM,64),self.item["prefix_groups"]):
            assert entry["source_group"]=="R877"
            name="R877-original-V5-prefix-and-A-part-"+str(first).zfill(4)+"-"+str(min(DIM,first+64)).zfill(4)+".json.gz"
            assert entry["file"]==name
        name="original-source-audit"
        if self.old(name) is None:
            self.put(name,{"prime":PRIME,"canonical_free_column":1186,
                "original_s_root":99932770,"original_zeta_root":549966761,
                "original_branch0":0,"remaining_original_branch_indices":self.remaining,
                "source_completed_R877":self.r877.ref(self.item["sources"]["R877"]["certificate"]),
                "source_completed_R824":self.r824.ref(self.item["sources"]["R824"]["certificate"]),
                "source_original_S5_inverse":self.item["inputs"]["S5_inverse"],
                "source_original_S5_matrix":self.item["inputs"]["S5_matrix"],
                "source_original_R787_chart":self.item["inputs"]["original_chart"],
                "source_original_R787_selection":self.item["inputs"]["original_selection"],
                "source_original_Z":self.item["inputs"]["original_rational_blocks"],
                "source_original_global_DAG":self.item["inputs"]["global_DAG"],
                "source_original_Galois_node":self.galois_id,
                "completed_prefix_groups":self.item["prefix_groups"],
                "source_branch_profiles":self.item["branch_profiles"],
                "original_V5_integer_scale":scale,
                "same_original_unit_chart_and_free1186_direction_certified":True,
                "old_F69_and_S5_inverse_are_complete_bound_inputs":True,
                "branch0_A_B_read_without_recomputation":True,
                "arbitrary_modular_kernel_lift_used":False,
                "new_normalized_Dixon_digits_computed":0})
        self.refs["source_audit"]=self.ref(name);self.checkpoint("original_sources_bound")

    def galois_orbit(self):
        name="original-Galois-seven-cycle";value=self.old(name)
        if value is None:
            self.status=name;self.budget()
            lam=rational_mod(self.field["lambda"]);assert lam
            invlam=pow(lam,-1,PRIME);zeta=549966761
            assert (1+2*zeta)%PRIME==99932770
            bvalues={i:int(self.roots[i][0])*invlam%PRIME for i in self.same}
            assert len(set(bvalues.values()))==7
            inverse={v:i for i,v in bvalues.items()}
            orbit=[];seen=set();branch=0
            for j in range(7):
                assert branch not in seen
                seen.add(branch);b=bvalues[branch]
                image=(rational_polynomial_mod(self.sigma_b[0],b)+
                       zeta*rational_polynomial_mod(self.sigma_b[1],b))%PRIME
                assert image in inverse
                following=inverse[image]
                orbit.append({"sigma_power":j,"original_branch":branch,"roots_B_s":self.roots[branch],
                              "original_b_reduction":b,"sigma_b_reduction":image,
                              "next_original_branch":following})
                branch=following
            assert branch==0 and seen==set(self.same)
            self.put(name,{"prime":PRIME,"source_audit":self.refs["source_audit"],
                "source_original_selection":self.item["inputs"]["original_selection"],
                "source_original_Galois_DAG":self.item["inputs"]["global_DAG"],
                "source_original_Galois_node":self.galois_id,
                "original_lambda_mod_prime":lam,"original_zeta_root":zeta,"original_s_root":99932770,
                "original_same_s_seven_cycle":orbit,"actual_order":7,
                "all_original_rational_denominators_used_here_are_units":True,
                "fixes_original_z_w_and_normal_basis":True,
                "branch_labels_not_assigned_by_guessing_sorted_roots":True})
            value=self.old(name)
        assert value["source_audit"]==self.refs["source_audit"] and value["actual_order"]==7
        self.orbit=value["original_same_s_seven_cycle"]
        self.power={row["original_branch"]:row["sigma_power"] for row in self.orbit}
        assert set(self.power)==set(self.same) and self.power[0]==0
        self.refs["orbit"]=self.ref(name);self.checkpoint("original_Galois_cycle_certified")

    def branch_coefficients(self,branch):
        name=f"branch-{branch:02d}-original-A-C-and-ZB";old=self.old(name)
        source=self.profiles[branch]
        if old is None:
            self.status=name;self.budget()
            value=self.r824.stage(source)
            assert value["ordinary_power"]==5 and value["prime"]==PRIME and value["branch"]==branch
            assert value["roots_B_s"]==self.roots[branch]
            assert value["actual_Schur_rank"]==1186 and value["selected_minor_det_mod_prime"]!=0
            assert plain(value["chart"])==plain(self.item["inputs"]["R824_chart"])
            assert plain(value["rational_block"])==plain(self.item["inputs"]["original_rational_blocks"])
            assert value["original_reserved_column_retained_without_new_lift"] is True
            assert value["full_original_modular_relations_verified_for_all_new_free_targets"] is True
            origin=plain(value["original_branch_inverse_reused_from"])
            original=read(self.r787.directory/"full-outputs-manifest.json")
            indexed={v["file"]:plain(v) for v in original["files"]}
            assert indexed[origin["file"]]==origin
            assert origin["file"]==f"R787-prime-{PRIME}-branch-{branch:02d}.json.gz"
            free=value["kernel_free_columns"]
            assert len(free)==len(set(free))==28 and 1186 in free
            assert free==[j for j in range(1214) if j not in set(self.chart["pivot_columns"])]
            position=free.index(1186)
            shape(value["kernel_A_mod_prime"],DIM,28);shape(value["kernel_C_mod_prime"],1214,28)
            A=[int(row[position]) for row in value["kernel_A_mod_prime"]]
            C=[int(row[position]) for row in value["kernel_C_mod_prime"]]
            assert all(0<=x<PRIME for x in A+C)
            assert all(C[j]==int(j==1186) for j in free)
            pp=self.Z*self.mat([[x] for x in C],PRIME)
            B=[0]*DIM
            for i,j in enumerate(self.P):B[j]=int(pp[i,0])
            for i,j in enumerate(self.Q):B[j]=self.Zd*C[i]%PRIME
            assert any(A) and any(B)
            self.put(name,{"prime":PRIME,"original_branch":branch,"sigma_power":self.power[branch],
                "roots_B_s":self.roots[branch],"canonical_free_column":1186,
                "canonical_column_position":position,"source_original_profile":source,
                "source_original_reserved_R787_branch":origin,
                "source_original_chart":self.item["inputs"]["original_chart"],
                "source_original_rational_blocks":self.item["inputs"]["original_rational_blocks"],
                "source_original_Galois_cycle":self.refs["orbit"],
                "original_unit_minor_determinant_mod_prime":value["selected_minor_det_mod_prime"],
                "A_coefficients_mod_prime_in_original_V5_basis":A,
                "C_coefficients_mod_prime_in_original_constant_kernel":C,
                "B_coefficients_mod_prime_in_original_V5_basis":B,
                "all_original_free_coordinates_match_1186_normalization":True,
                "source_reserved_A_C_not_recomputed":True,
                "original_Z_expanded_once_for_this_new_B_RHS":True,
                "original_common_clear_or_lambda_factor_inserted":False,
                "characteristic_zero_coefficient_definition":{
                    "operation":"apply_original_L_over_K_sigma_to_R849_unit_chart_solution",
                    "source_original_DAG":self.item["inputs"]["global_DAG"],
                    "A_node":self.graph["global_unit_chart_nodes"]["A_coefficients"],
                    "C_node":self.graph["global_unit_chart_nodes"]["C_coefficients"],
                    "sigma_power":self.power[branch],"original_free_column":1186,
                    "B_formula":"original Z times original C; no change of scale"},
                "characteristic_zero_coefficients_reconstructed":False})
            old=self.old(name)
        assert old["source_original_profile"]==source and old["sigma_power"]==self.power[branch]
        ref=self.ref(name)
        self.coefficient_refs.append(ref)
        return old

    def full_rhs(self,coefficients):
        self.labels=[{"original_branch":b,"sigma_power":self.power[b],"target":target}
                     for b in self.remaining for target in ("A","B")]
        matrix_columns=[]
        for v in coefficients:
            matrix_columns.extend([v["A_coefficients_mod_prime_in_original_V5_basis"],
                                   v["B_coefficients_mod_prime_in_original_V5_basis"]])
        assert len(matrix_columns)==12
        coefficient_rows=[list(row) for row in zip(*matrix_columns)]
        shape(coefficient_rows,DIM,12)
        name="new-twelve-full1380-right-hand-sides";old=self.old(name)
        if old is None:
            groups=[]
            for chunk,(first,entry) in enumerate(zip(range(0,DIM,64),self.item["prefix_groups"])):
                self.next_chunk=chunk;stop=min(DIM,first+64)
                partname=f"new-twelve-RHS-part-{first:04d}-{stop:04d}"
                part=self.old(partname)
                if part is None:
                    self.status=partname;self.budget()
                    origin=self.r877.stage(entry)
                    assert origin["first_column"]==first and origin["stop_column"]==stop and origin["prime"]==PRIME
                    assert plain(origin["source_audit"])==plain(self.item["inputs"]["parent_source_audit"])
                    assert [plain(x) for x in origin["source_original_V5_rows"]]==[plain(x) for x in self.original_rows[first:stop]]
                    assert origin["original_prefix_coordinate_order"]=="v^n*t^r, n0..68,r0..19"
                    shape(origin["original_prefix_columns_mod_prime"],stop-first,ROWS)
                    F=self.mat(origin["original_prefix_columns_mod_prime"],PRIME).transpose()
                    V=self.mat(coefficient_rows[first:stop],PRIME)
                    product=F*V
                    self.put(partname,{"prime":PRIME,"source_audit":self.refs["source_audit"],
                        "source_completed_F69_chunk":entry,"source_original_coefficients":self.coefficient_refs,
                        "first_column":first,"stop_column":stop,"target_labels":self.labels,
                        "matrix_shape":[ROWS,12],"partial_right_hand_sides_mod_prime":rows(product),
                        "original_F69_not_reduced_or_constructed_again":True})
                    part=self.old(partname)
                assert part["source_completed_F69_chunk"]==entry
                assert part["source_original_coefficients"]==self.coefficient_refs and part["target_labels"]==self.labels
                groups.append(self.ref(partname))
                self.next_chunk=chunk+1;self.checkpoint("new_twelve_RHS_parts")
            self.budget();total=[[0]*12 for _ in range(ROWS)]
            for reference in groups:
                part=read(bound(self.out,reference));values=part["partial_right_hand_sides_mod_prime"]
                shape(values,ROWS,12)
                for i in range(ROWS):
                    for j in range(12):total[i][j]=(total[i][j]+int(values[i][j]))%PRIME
            assert all(total[i][j]==0 for i in range(20) for j in range(1,12,2))
            self.put(name,{"prime":PRIME,"source_audit":self.refs["source_audit"],
                "source_parts":groups,"source_original_coefficients":self.coefficient_refs,
                "target_labels":self.labels,"matrix_shape":[ROWS,12],"right_hand_sides_mod_prime":total,
                "original_constant_block_retained":True,"all_six_B_constant_blocks_zero":True,
                "old_branch0_A_B_or_F69_recomputed":False})
            old=self.old(name)
        assert old["source_original_coefficients"]==self.coefficient_refs and old["target_labels"]==self.labels
        self.refs["rhs"]=self.ref(name);self.next_chunk=20;self.checkpoint("twelve_full1380_RHS_complete")
        return old

    def solve(self,rhs):
        name="all-twelve-S5-unit-solves-and-full1380-verification";old=self.old(name)
        if old is None:
            self.status=name;self.budget()
            data=rhs["right_hand_sides_mod_prime"];shape(data,ROWS,12)
            solution=self.U*self.mat([data[i] for i in self.I],PRIME)
            target=self.mat(data,PRIME)
            assert self.S5*solution==target
            values=rows(solution);shape(values,DIM,12)
            assert all(any(values[i][j] for i in range(DIM)) for j in range(12))
            self.put(name,{"prime":PRIME,"source_rhs":self.refs["rhs"],
                "source_original_S5_matrix":self.item["inputs"]["S5_matrix"],
                "source_completed_S5_inverse":self.item["inputs"]["S5_inverse"],
                "target_labels":self.labels,"selected_row_indices":self.I,
                "solution_shape":[DIM,12],"S5_coordinates_mod_prime":values,
                "all1380_by12_original_coordinates_verified":True,
                "all_twelve_original_reductions_nonzero":True,
                "original_normal_basis_row_mapping":self.mapping,
                "old_S5_inverse_or_branch0_solve_recomputed":False,
                "characteristic_zero_selected_unit_solve_defined":True,
                "characteristic_zero_coordinates_reconstructed":False})
            old=self.old(name)
        assert old["source_rhs"]==self.refs["rhs"] and old["target_labels"]==self.labels
        self.refs["solve"]=self.ref(name);self.checkpoint("all_twelve_complete_S5_solves")
        return old

    def normal_pairs(self,solution):
        values=solution["S5_coordinates_mod_prime"]
        for j,branch in enumerate(self.remaining):
            name=f"branch-{branch:02d}-original-normal-A-B-pair";old=self.old(name)
            if old is None:
                self.status=name;self.budget()
                vectors=[]
                for offset,target in enumerate(("A","B")):
                    normal=[[0]*RANK for _ in range(6)]
                    for i,(a,k) in enumerate(self.mapping):normal[k][a]=int(values[i][2*j+offset])
                    assert all(normal[k][a]==0 for k in range(6) for a in range(RANK) if k>5-EPS[a])
                    assert any(any(row) for row in normal)
                    vectors.append(normal)
                exact={"operation":"original_S5_selected_unit_solve_for_sigma_A_and_B",
                    "source_original_global_DAG":self.item["inputs"]["global_DAG"],
                    "source_original_Galois_node":self.galois_id,"sigma_power":self.power[branch],
                    "original_A_function_node":self.graph["global_function_nodes"]["A_over_tau5"],
                    "original_B_function_node":self.graph["global_function_nodes"]["B_over_tau5"],
                    "source_original_F69_chunks":self.item["prefix_groups"],
                    "source_original_S5_matrix":self.item["inputs"]["S5_matrix"],
                    "selected_row_indices":self.I,
                    "source_actual_selected_unit_inverse":self.item["inputs"]["S5_inverse"],
                    "original_free_column":1186,"formula":"normal_map(S5[I]^-1*(F69*sigma^j(A or ZC))[I])",
                    "membership_reason":"original sigma fixes K and the complete V5/S5 basis",
                    "original_scale_applied_again":False}
                self.put(name,{"prime":PRIME,"original_branch":branch,"sigma_power":self.power[branch],
                    "roots_B_s":self.roots[branch],"original_zeta_root":549966761,"canonical_free_column":1186,
                    "source_original_coefficients":self.coefficient_refs[j],
                    "source_all_twelve_normal_solves":self.refs["solve"],
                    "normal_basis_rank":RANK,"normal_basis_degrees":EPS,"regular_degree_bound":5,
                    "A_vector_coefficients_mod_prime":vectors[0],
                    "B_vector_coefficients_mod_prime":vectors[1],
                    "all1380_original_coordinates_for_each_vector_verified":True,
                    "all_original_weighted_support_bounds_verified":True,
                    "same_original_82power10_scales_preserved":True,
                    "both_original_function_reductions_nonzero":True,
                    "abstract_p_integral_original_normal_lifts_certified":True,
                    "exact_unit_solve_expression":exact,
                    "normal_fraction":"sigma^j(y)=(sigma^j(A)/tau^5)/(sigma^j(B)/tau^5)",
                    "finite_fiber_B_invertibility_checked":False,
                    "characteristic_zero_coordinates_reconstructed":False})
                old=self.old(name)
            assert old["source_all_twelve_normal_solves"]==self.refs["solve"] and old["sigma_power"]==self.power[branch]
            self.pair_refs.append(self.ref(name));self.checkpoint("new_normal_pairs_retained")
        name="seven-original-Galois-normal-inputs";old=self.old(name)
        if old is None:
            lookup={branch:ref for branch,ref in zip(self.remaining,self.pair_refs)}
            ordered=[]
            for record in self.orbit:
                branch=record["original_branch"]
                if branch==0:
                    ordered.append({"sigma_power":0,"original_branch":0,"roots_B_s":self.roots[0],
                        "source_original_A_normal":self.item["inputs"]["parent_normal_A"],
                        "source_original_B_normal":self.item["inputs"]["B_normal"],
                        "source_original_fraction":self.item["inputs"]["parent_normal_fraction"],
                        "old_original_A_B_recomputed":False})
                else:ordered.append({"sigma_power":record["sigma_power"],"original_branch":branch,
                    "roots_B_s":self.roots[branch],"source_original_normal_pair":lookup[branch]})
            self.put(name,{"prime":PRIME,"source_audit":self.refs["source_audit"],
                "source_original_Galois_cycle":self.refs["orbit"],
                "original_s_root":99932770,"original_zeta_root":549966761,
                "source_original_global_DAG":self.item["inputs"]["global_DAG"],
                "original_global_y_node":self.graph["global_function_nodes"]["original_y"],
                "normal_basis_rank":RANK,"normal_basis_degrees":EPS,"regular_degree_bound":5,
                "ordered_original_sigma_powers":ordered,"actual_normal_pair_count":7,
                "new_right_hand_side_count":12,"all_seven_original_Galois_normal_inputs_certified":True,
                "same_original_unit_chart_normalization_for_every_branch":True,
                "original_global_fraction_defined_by_exact_source_unit_solves":True,
                "all_other_s_branches_used":False,"source_scales_changed":False,
                "all_seven_Dstar_pencils_computed":False,
                "original_five_Lj_RR128_or_144_computed":False,
                "connection_rigidification_period_or_height_computed":False})
        self.refs["seven"]=self.ref(name);self.checkpoint("seven_original_Galois_normal_inputs_complete")

    def inventory(self):
        entries=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name in (self.path("current").name,self.path("stage-manifest").name):continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag and value["complete"] is True
            entries.append(spec(path))
        save(self.path("stage-manifest"),{"result":RESULT,"configuration":self.tag,"complete":True,
            "files":entries,"current_excluded":True,"all_complete_stages_retained":True})
        return self.ref("stage-manifest")

    def finish(self,complete,reason=None):
        current=self.checkpoint(self.status)
        final={"result":RESULT,"configuration":self.tag,"complete":bool(complete),"p":41,"prime":PRIME,
            "source_audit":self.refs.get("source_audit"),"original_Galois_orbit":self.refs.get("orbit"),
            "original_coefficient_sources":self.coefficient_refs,"full1380_rhs":self.refs.get("rhs"),
            "all_twelve_normal_solves":self.refs.get("solve"),"new_normal_pairs":self.pair_refs,
            "seven_Galois_normal_inputs":self.refs.get("seven"),
            "new_right_hand_side_count":12 if self.refs.get("solve") else 0,
            "actual_new_normal_pair_count":len(self.pair_refs),
            "all_seven_original_Galois_normal_inputs_certified":bool(self.refs.get("seven")),
            "all1380_by12_original_coordinates_verified":bool(self.refs.get("solve")),
            "original_Galois_seven_cycle_certified":bool(self.refs.get("orbit")),
            "old_branch0_A_B_F69_or_inverse_recomputed":False,
            "characteristic_zero_normal_coordinates_reconstructed":False,
            "all_seven_Dstar_pencils_computed":False,
            "original_five_Lj_RR128_or_144_computed":False,
            "connection_Poincare_period_or_height_computed":False,
            "stage_manifest":self.inventory(),"resume_state":current,
            "stop_reason":reason,"seconds":time.monotonic()-self.started}
        if complete:
            assert final["all_seven_original_Galois_normal_inputs_certified"]
            assert final["all1380_by12_original_coordinates_verified"] and len(self.pair_refs)==6
        save(self.out/FINAL,final);return final

    def run(self):
        self.prepare();self.galois_orbit()
        coefficients=[self.branch_coefficients(branch) for branch in self.remaining]
        rhs=self.full_rhs(coefficients);solution=self.solve(rhs)
        self.normal_pairs(solution);return self.finish(True)

def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise SystemExit("New R880 six-branch arithmetic runs only in the authorized public repository Actions")
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    parser.add_argument("--config",required=True);parser.add_argument("--out",required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args();out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    started=time.monotonic();job=None;final=None;error=None;code=0
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
    except Exception as exc:code=1;error=str(exc);traceback.print_exc()
    if final is None and job is not None:
        try:final=job.finish(False,error)
        except Exception:traceback.print_exc()
    receipt={"result":RESULT,"source_sha256":sha(__file__),"complete":bool(final and final["complete"]),
        "configuration_sha256":fingerprint(job.tag) if job else None,
        "certificate_sha256":sha(out/FINAL) if final else None,
        "new_right_hand_side_count":final.get("new_right_hand_side_count",0) if final else 0,
        "all_seven_original_Galois_normal_inputs_certified":bool(final and final["all_seven_original_Galois_normal_inputs_certified"]),
        "all1380_by12_original_coordinates_verified":bool(final and final["all1380_by12_original_coordinates_verified"]),
        "old_branch0_A_B_F69_or_inverse_recomputed":False,
        "characteristic_zero_normal_coordinates_reconstructed":False,
        "original_five_Lj_RR128_or_144_computed":False,
        "exit_code":code,"error":error,"seconds":time.monotonic()-started}
    save(out/"core-receipt.json",receipt)
    print("R880_SIX_BRANCH_CORE_SUMMARY="+json.dumps(receipt,sort_keys=True),flush=True)
    return code

if __name__=="__main__":raise SystemExit(main())
