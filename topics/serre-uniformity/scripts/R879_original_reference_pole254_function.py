#!/usr/bin/env python3
"""R879: one exact source-bound pole-254 function from completed R872 syzygies.

All new arithmetic is confined to the authorized public Actions runner.
Old R872 matrices and exact unit-solve leaves keep their original identities.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import traceback

RESULT = "R879-original-reference-pole254-pencil"
FINAL = "p41-original-reference-pole254-pencil-certificate.json"
PREFIX = "R879-reference-"
SOURCE_RESULT = "R872-original-P0-jets-and-fixed-Picard-RR-spaces"
SOURCE_CORE = "0e5897512a2f45baaed9cd1b6b2badcb6bf6ee2b100fcd45db871ad9f6db1874"
P = 1000000753
ROOT = 549966761
EPS = [0]+[1]*144+[2]*127
META = ("public-actions-input.json", "run-receipt.json", "core-receipt.json")
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
INPUTS = ("source_audit", "point_linearization", "V2_jets", "V2_point_kernel",
          "anchor_u", "anchor_b", "pencil_profile", "paired_kernel", "fixed_divisor")
STRATEGY = {
    "original_curve": "original genus127 Y at p41 with the original minus3 descent",
    "original_point": "original P0, finite tau chart",
    "source_exact_leaves": "completed R872 characteristic-zero unit-solve expressions",
    "coefficient_field": "K=Q(zeta); zeta^2+zeta+1=0",
    "prime": P, "original_zeta_root": ROOT,
    "normal_basis_degrees": EPS,
    "normal_basis_order": "normal row first, increasing z power",
    "V2_dimension": 418, "V3_dimension": 690,
    "source_paired_kernel_dimension": 418,
    "source_relation": "u*T(c)+b*S(c)=0 in original V5",
    "high_rows": "one z^(3-epsilon_i) row for each original normal row",
    "constraint_row_order": "272 S-high;272 T-high;J0*S-low through J18*S-low",
    "system_shape": [563,418], "exact_rank": 291,
    "right_hand_side": "zero at rows0..561 and one at row562",
    "row_profile": "left-to-right pivots of transpose",
    "column_profile": "left-to-right pivots in selected rows",
    "unselected_coordinates": "all127 free coordinates zero",
    "reference_function": "(S(c)/tau)/u",
    "paired_function_identity": "f/u=-g/b; u*g+b*f=0",
    "unique_pole": {"point":"P0","order":254},
    "reference_pencil": ["1","v0"],
    "reference_128_basis_computed": False,
    "new_pencil_672_minor_needed": False,
    "original_t_frame_scalar": "(leading_coefficient(t/x))^254 / U272",
    "original_t_frame_scalar_expanded": False,
    "old_jets_kernel_products_or_inverse_recomputed": False,
    "characteristic_zero_coefficients_reconstructed": False,
    "old_large_source_carrier_needed_for_this_finite_scope": False,
    "budget_and_transport_excluded_from_identity": True,
}

class BudgetStop(Exception):
    pass

class UnitFailure(Exception):
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
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+".tmp")
    data=json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
    if path.suffix==".gz":
        with temporary.open("wb") as raw:
            with gzip.GzipFile(filename="",mode="wb",fileobj=raw,mtime=0,compresslevel=1) as f:
                f.write(data)
    else:
        temporary.write_bytes(data+b"\n")
    temporary.replace(path)

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
                                     ensure_ascii=False).encode()).hexdigest()

def plain(row):
    ans={k:row[k] for k in ("file","bytes","sha256")}
    assert Path(ans["file"]).name==ans["file"] and "\\" not in ans["file"]
    return ans

def spec(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}

def bound(folder,row):
    row=plain(row);path=Path(folder)/row["file"]
    assert spec(path)==row,("source_bytes_or_sha",row["file"])
    return path

def identity(source):
    return {**{k:source[k] for k in BASE},
            "configuration_sha256":source["configuration_sha256"],
            "certificate":plain(source["certificate"]),
            "selected_file_count":len(source["files"]),
            "selected_files_sha256":fingerprint(source["files"])}

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"p":41,
            "python_flint":"0.9.0","method_sha256":item["method_sha256"],
            "proofs":{k:{q:v[q] for q in ("path","sha256")} for k,v in item["proofs"].items()},
            "source_R872":identity(item["source"]),
            "inputs":item["inputs"],"strategy":STRATEGY}

def basis(m):
    return [(i,a) for i in range(272) for a in range(m-EPS[i]+1)]

def rows(matrix):
    return [[int(matrix[i,j]) for j in range(matrix.ncols())]
            for i in range(matrix.nrows())]

def shape(value,m,n):
    assert isinstance(value,list) and len(value)==m
    assert all(isinstance(row,list) and len(row)==n for row in value)
    assert all(isinstance(x,int) and 0<=x<P for row in value for x in row)

def pivot_columns(matrix,rank):
    out=[]
    for i in range(rank):
        nz=[j for j in range(matrix.ncols()) if int(matrix[i,j])]
        assert nz
        out.append(nz[0])
    assert out==sorted(set(out))
    return out

class Source:
    def __init__(self,item):
        self.item=item
        self.directory=Path(item["directory"])
        assert item["result"]==SOURCE_RESULT and item["core_sha256"]==SOURCE_CORE
        mpath=self.directory/"full-outputs-manifest.json"
        assert sha(mpath)==item["manifest_sha256"]
        manifest=read(mpath)
        assert manifest["result"]==SOURCE_RESULT
        self.entries={r["file"]:plain(r) for r in manifest["files"]}
        assert len(self.entries)==len(manifest["files"])==314
        self.entries[mpath.name]=spec(mpath)
        for name,row in item["files"].items():
            assert name==row["file"] and self.entries[name]==plain(row)
            bound(self.directory,row)
        for name in META:
            assert name in item["files"]
        initial,run,core=[read(bound(self.directory,item["files"][name])) for name in META]
        assert initial["result"]==run["result"]==core["result"]==SOURCE_RESULT
        assert initial["source_commit"]==run["source_commit"]==item["source_commit"]
        assert str(run["workflow_run_id"])==str(item["run_id"])
        assert initial["core_sha256"]==core["source_sha256"]==SOURCE_CORE
        assert run["complete"] is True and run["process_exit_code"]==0 and run["error"] is None
        assert core["complete"] is True and core["error"] is None
        assert run["core_receipt_sha256"]==item["files"]["core-receipt.json"]["sha256"]
        self.certificate=read(bound(self.directory,item["certificate"]))
        assert self.certificate["result"]==SOURCE_RESULT and self.certificate["complete"] is True
        assert core["certificate_sha256"]==item["certificate"]["sha256"]
        self.tag=self.certificate["configuration"]
        assert self.tag["source_sha256"]==SOURCE_CORE and self.tag["result"]==SOURCE_RESULT
        assert fingerprint(self.tag)==item["configuration_sha256"]
        assert self.tag["normal_basis_degrees"]==EPS
        if "actual_configuration" in initial:
            assert initial["actual_configuration"]==self.tag
        for key in ("actual_original_P0_local_parameter_certified",
                    "actual_original_P0_jets_through_order272_computed",
                    "actual_original_complete_146_kernel_certified",
                    "actual_fixed_chi_complete_418_RR_space_certified"):
            assert self.certificate[key] is True
        assert self.certificate["actual_pencil_rank"]==962
        assert self.certificate["accepted_pencil_trial"]==1
        assert self.certificate["characteristic_zero_sources_are_exact_unit_solve_expressions"] is True
        assert self.certificate["characteristic_zero_jet_or_RR_coefficients_reconstructed"] is False

    def stage(self,row):
        row=plain(row)
        assert self.item["files"][row["file"]]==row==self.entries[row["file"]]
        value=read(bound(self.directory,row))
        assert value["result"]==SOURCE_RESULT and value["complete"] is True
        assert value["configuration"]==self.tag
        return value

class Job:
    def __init__(self,args):
        self.started=time.monotonic()
        self.budget_seconds=60*args.budget_minutes
        self.out=Path(args.output);self.out.mkdir(parents=True,exist_ok=True)
        self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41
        assert sha(__file__)==self.item["core_sha256"]
        assert self.item["producer_inputs_pending"] is False
        assert set(self.item["inputs"])==set(INPUTS)
        for row in self.item["proofs"].values():
            assert sha(row["file"])==row["sha256"]
        assert sha(self.item["method_file"])==self.item["method_sha256"]
        self.source=Source(self.item["source"])
        self.tag=expected_tag(self.item)
        self.refs={};self.current=None
        from flint import nmod_mat
        self.matrix=lambda x:nmod_mat(x,P)
        self.eye=lambda n:nmod_mat([[int(i==j) for j in range(n)] for i in range(n)],P)
        self.V2,self.V3=basis(2),basis(3)
        assert len(self.V2)==418 and len(self.V3)==690
        self.v3_index={pair:i for i,pair in enumerate(self.V3)}
        self.low=[self.v3_index[pair] for pair in self.V2]
        self.high=[self.v3_index[(i,3-EPS[i])] for i in range(272)]
        assert sorted(self.low+self.high)==list(range(690))
        self.data={k:self.source.stage(self.item["inputs"][k]) for k in INPUTS}
        self.review_source()

    def budget(self):
        if time.monotonic()-self.started>=self.budget_seconds:
            raise BudgetStop("R879 budget; all committed matrices and source bytes are retained.")

    def path(self,name):
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
        assert not self.path(name).exists()
        value={"result":RESULT,"configuration":self.tag,"complete":True,**value}
        save(self.path(name),value)
        self.refs[name]=spec(self.path(name))
        return self.refs[name]

    def checkpoint(self,phase):
        value={"result":RESULT,"configuration":self.tag,"complete":False,
               "phase":phase,"completed_stage_references":dict(self.refs)}
        save(self.path("current"),value)
        self.current=spec(self.path("current"))

    def review_source(self):
        cert=self.source.certificate;inp=self.item["inputs"];d=self.data
        mapping={"source_audit":"source_audit","point_linearization":"point_linearization",
                 "V2_jets":"original_V2_jet_matrix","V2_point_kernel":"complete_original_146_kernel",
                 "anchor_u":"anchor_u","anchor_b":"accepted_anchor_b",
                 "pencil_profile":"accepted_pencil_profile",
                 "paired_kernel":"complete_fixed_chi_418_kernel",
                 "fixed_divisor":"fixed_chi_divisor_and_principal_function"}
        assert all(plain(cert[right])==plain(inp[left]) for left,right in mapping.items())
        audit=d["source_audit"]
        assert audit["prime"]==P and audit["original_zeta_root"]==ROOT
        assert audit["chosen_parameter_derivative_is_a_unit"] is True
        assert audit["all_original_scales_preserved"] is True
        self.parameter=audit["chosen_local_parameter"]
        assert self.parameter in ("z_minus_z0","w_minus_w0")
        assert d["point_linearization"]["prime"]==P
        assert d["point_linearization"]["original_zeta_root"]==ROOT
        jets=d["V2_jets"]
        assert jets["matrix_shape"]==[273,418] and jets["row_orders"]==list(range(273))
        assert jets["V2_basis"]==[{"normal_basis_row":i,"power_of_z":a} for i,a in self.V2]
        shape(jets["matrix_mod_prime"],273,418)
        assert jets["normal_integer_scale_applied_again"] is False
        kernel=d["paired_kernel"]
        assert kernel["actual_kernel_dimension"]==418
        assert kernel["actual_pencil_rank_mod_prime"]==962
        assert kernel["full_characteristic_zero_dimension"]==418
        assert kernel["exact_full_characteristic_zero_W_Dchi_certified"] is True
        for key in ("all544_by418_quotient_residuals_zero",
                    "all1234_by418_complete_V5_relations_zero",
                    "both_selected_inverse_products_verified",
                    "combined_minor_nonzero_by_unit_block_Schur_factorization"):
            assert kernel[key] is True
        assert plain(kernel["source_anchor_u"])==plain(inp["anchor_u"])
        assert plain(kernel["source_anchor_b"])==plain(inp["anchor_b"])
        assert plain(kernel["source_rank_profile"])==plain(inp["pencil_profile"])
        assert kernel["divisor_definition"]["common_zero_of_u_b"]=="272*P0"
        assert kernel["divisor_definition"]["D_chi_avoids_original_P0"] is True
        assert kernel["exact_kernel_definition"]["full_global_relation"]=="u*t+b*s=0 in original V5"
        shape(kernel["V3_kernel_basis_mod_prime"],690,418)
        shape(kernel["paired_u_multiplier_coordinates_mod_prime"],690,418)
        self.S=kernel["V3_kernel_basis_mod_prime"]
        self.T=kernel["paired_u_multiplier_coordinates_mod_prime"]
        pointkernel=d["V2_point_kernel"]
        assert pointkernel["accepted"] is True
        assert pointkernel["actual_rank_mod_prime"]==272 and pointkernel["actual_kernel_dimension"]==146
        assert pointkernel["all272_by146_residuals_zero"] is True
        assert pointkernel["full_characteristic_zero_RR_kernel_certified"] is True
        u,b=d["anchor_u"],d["anchor_b"]
        for v,role in ((u,"u"),(b,"b")):
            assert v["role"]==role and v["vanishes_at_original_P0_to_order_at_least272"] is True
            assert plain(v["source_complete_kernel"])==plain(inp["V2_point_kernel"])
            assert len(v["V2_coordinates_mod_prime"])==418
            assert v["normal_integer_scale_applied_again"] is False
        assert u["order272_is_exact"] is True
        assert isinstance(u["exact_order272_unit"],int) and 0<u["exact_order272_unit"]<P
        assert u["exact_order272_unit"]==pointkernel["extra_order272_coefficients_mod_prime"][
            pointkernel["first_exact_order272_basis_index"]]
        assert b["trial"]==1
        profile=d["pencil_profile"]
        assert profile["accepted"] is True and profile["actual_pencil_rank_mod_prime"]==962
        divisor=d["fixed_divisor"]
        assert divisor["D_chi_effective_and_avoids_original_P0"] is True
        assert divisor["actual_complete_fixed_chi_RR_space_certified"] is True
        assert plain(divisor["source_complete_W_Dchi"])==plain(inp["paired_kernel"])
        old=self.old("source-audit")
        if old is None:
            self.put("source-audit",{
                "source_R872":identity(self.item["source"]),"inputs":inp,
                "prime":P,"original_zeta_root":ROOT,"chosen_local_parameter":self.parameter,
                "original_complete_paired_418_kernel_consumed":True,
                "original_273_by418_jet_matrix_consumed":True,
                "old_source_characteristic_zero_leaves_are_exact_unit_solve_expressions":True,
                "original_146_or418_kernel_or_jets_recomputed":False,
                "old_W_products_or_inverse_recomputed":False,
                "old_large_source_carrier_downloaded":False,
                "unread_source_dependencies_remain_certified_external_leaves":True,
                "all_selected_original_bytes_and_configurations_verified":True})
        else:
            assert old["source_R872"]==identity(self.item["source"])
            assert old["inputs"]==inp

    def form_system(self):
        old=self.old("system")
        if old is None:
            self.budget()
            slow=[self.S[i] for i in self.low]
            jet=self.matrix(self.data["V2_jets"]["matrix_mod_prime"][:19])
            new_jets=jet*self.matrix(slow)
            system=[self.S[i] for i in self.high]+[self.T[i] for i in self.high]+rows(new_jets)
            shape(system,563,418)
            self.put("system",{
                "source_paired_kernel":self.item["inputs"]["paired_kernel"],
                "source_original_V2_jets":self.item["inputs"]["V2_jets"],
                "source_anchor_u":self.item["inputs"]["anchor_u"],
                "V3_high_row_indices":self.high,"V3_low_row_indices_in_V2_order":self.low,
                "V2_basis":[{"normal_basis_row":i,"power_of_z":a} for i,a in self.V2],
                "matrix_shape":[563,418],"matrix_mod_prime":system,
                "right_hand_side_mod_prime":[0]*562+[1],
                "jet_row_orders":list(range(19)),
                "exact_matrix_definition":{
                    "kind":"original_paired_kernel_two_degree_truncations_and_original_jets",
                    "top_block":"272 highest normal z coefficients of S",
                    "second_block":"272 highest normal z coefficients of T",
                    "last_block":"original J[0:19] times low original S coordinates",
                    "no_new_old_product_or_jet_evaluation":True,
                    "exact_rank":291,"proof":"R879 RP.6-8"}})
            old=self.old("system")
        shape(old["matrix_mod_prime"],563,418)
        assert old["V3_high_row_indices"]==self.high
        assert old["V3_low_row_indices_in_V2_order"]==self.low
        self.A=self.matrix(old["matrix_mod_prime"])
        self.rhs=self.matrix([[int(i==562)] for i in range(563)])
        self.checkpoint("system_complete")

    def solve(self):
        old=self.old("unit-solution")
        if old is None:
            self.budget()
            row_reduced,rank=self.A.transpose().rref()
            selected_rows=pivot_columns(row_reduced,rank)
            assert rank<=291, "The new matrix exceeds the proven exact rank bound."
            if rank!=291:
                self.put("unit-solution",{
                    "source_system":self.refs["system"],"accepted":False,
                    "actual_rank_mod_prime":rank,"selected_rows":selected_rows,
                    "failure_only_this_residue_specialization":True})
                raise UnitFailure("The new R879 residue matrix did not have the proven characteristic-zero rank291.")
            assert len([i for i in selected_rows if i<544])==272
            assert selected_rows[-19:]==list(range(544,563))
            selected=self.matrix([[int(self.A[i,j]) for j in range(418)] for i in selected_rows])
            augmented=self.matrix([
                [int(selected[i,j]) for j in range(418)]+[int(i==j) for j in range(291)]
                for i in range(291)])
            reduced,total=augmented.rref()
            assert total==291
            pivots=[j for j in pivot_columns(reduced,291) if j<418]
            assert len(pivots)==291
            free=[j for j in range(418) if j not in set(pivots)]
            assert len(free)==127
            square=self.matrix([[int(self.A[i,j]) for j in pivots] for i in selected_rows])
            inverse=self.matrix([[int(reduced[i,418+j]) for j in range(291)] for i in range(291)])
            eye=self.eye(291)
            assert square*inverse==eye and inverse*square==eye
            determinant=int(square.det())
            assert determinant!=0
            rhs_selected=self.matrix([[int(i==562)] for i in selected_rows])
            selected_solution=inverse*rhs_selected
            c=[0]*418
            for k,j in enumerate(pivots):
                c[j]=int(selected_solution[k,0])
            column=self.matrix([[x] for x in c])
            assert self.A*column==self.rhs
            self.put("unit-solution",{
                "source_system":self.refs["system"],"accepted":True,
                "actual_rank_mod_prime":291,"actual_high_truncation_rank_mod_prime":272,
                "selected_rows":selected_rows,"selected_pivot_columns":pivots,"free_columns":free,
                "actual_minor_mod_prime":rows(square),"inverse_mod_prime":rows(inverse),
                "actual_minor_determinant_mod_prime":determinant,
                "both_exact_modular_inverse_products_verified":True,
                "solution_mod_prime":c,"free_coordinates_all_zero":True,
                "all563_original_equations_verified":True,
                "exact_solution_definition":{
                    "kind":"original_291_unit_minor_nonhomogeneous_solution",
                    "source_system":self.refs["system"],"selected_rows":selected_rows,
                    "selected_columns":pivots,"free_columns":free,"free_values":"all_zero",
                    "selected_values":"A_selected_inverse times original selected right hand side",
                    "full_system_consistency":"R879 RP.8, not inferred from a random modular residual",
                    "characteristic_zero_coefficients_expanded":False}})
            old=self.old("unit-solution")
        assert old["source_system"]==self.refs["system"]
        if old["accepted"] is not True:
            raise UnitFailure("The retained R879 residue unit-minor test was not accepted.")
        assert old["actual_rank_mod_prime"]==291
        assert old["all563_original_equations_verified"] is True
        self.c=old["solution_mod_prime"]
        assert len(self.c)==418
        self.checkpoint("unit_solution_complete")

    def function(self):
        old=self.old("function-and-pencil")
        if old is None:
            self.budget()
            c=self.matrix([[x] for x in self.c])
            f=self.matrix([self.S[i] for i in self.low])*c
            g=self.matrix([self.T[i] for i in self.low])*c
            jet19=self.matrix(self.data["V2_jets"]["matrix_mod_prime"][:19])*f
            assert rows(jet19)==[[int(i==18)] for i in range(19)]
            fvalues=[int(f[i,0]) for i in range(418)]
            gvalues=[int(g[i,0]) for i in range(418)]
            uvalues=list(self.data["anchor_u"]["V2_coordinates_mod_prime"])
            normal_f=[[0]*272 for _ in range(3)]
            normal_g=[[0]*272 for _ in range(3)]
            normal_u=[[0]*272 for _ in range(3)]
            for k,(i,a) in enumerate(self.V2):
                normal_f[a][i]=fvalues[k]
                normal_g[a][i]=gvalues[k]
                normal_u[a][i]=uvalues[k]
            self.put("function-and-pencil",{
                "source_R872":identity(self.item["source"]),
                "source_unit_solution":self.refs["unit-solution"],
                "source_paired_kernel":self.item["inputs"]["paired_kernel"],
                "source_anchor_u":self.item["inputs"]["anchor_u"],
                "source_anchor_b":self.item["inputs"]["anchor_b"],
                "source_original_V2_jets":self.item["inputs"]["V2_jets"],
                "prime":P,"original_zeta_root":ROOT,"chosen_local_parameter":self.parameter,
                "normal_basis_rank":272,"normal_basis_degrees":EPS,
                "V2_basis":[{"normal_basis_row":i,"power_of_z":a} for i,a in self.V2],
                "numerator_V2_coordinates_mod_prime":fvalues,
                "paired_V2_coordinates_mod_prime":gvalues,
                "denominator_V2_coordinates_mod_prime":uvalues,
                "numerator_normal_polynomial_mod_prime":normal_f,
                "paired_normal_polynomial_mod_prime":normal_g,
                "denominator_normal_polynomial_mod_prime":normal_u,
                "numerator_first19_local_coefficients_mod_prime":[0]*18+[1],
                "denominator_order272_unit_mod_prime":self.data["anchor_u"]["exact_order272_unit"],
                "exact_function_definition":{
                    "kind":"ratio_of_original_same_weight_sections",
                    "numerator":{"kind":"S_low_times_exact_291_unit_solution",
                                 "source_S":self.item["inputs"]["paired_kernel"],
                                 "low_rows_in_V2_order":self.low,
                                 "coefficients":self.refs["unit-solution"]},
                    "denominator":{"kind":"original_R872_u",
                                   "source":self.item["inputs"]["anchor_u"]},
                    "equal_normalized_ratio":"(f/tau^2)/(u/tau^2)",
                    "global_certificate":"f/u=-g/b from the full old syzygy",
                    "old_global_syzygy_inherited_by_exact_linear_combination":True,
                    "new_global_product_recomputed":False,
                    "extra_82_or_tau_scale_applied":False},
                "exact_pole_divisor":{"point":"original_P0","multiplicity":254,
                                      "all_other_poles_excluded":True},
                "exact_reference_line_bundle":"O_Y(254*P0)",
                "exact_reference_pencil":["constant_one","the_exact_function_v0"],
                "basepoint_free_by_one_off_P0_and_exact_order254_at_P0":True,
                "original_t_frame":{
                    "frame":"t^(-254); t=a^3",
                    "value_of_v0_in_this_frame":"(leading(t/x))^254 / U272",
                    "U272_source":self.item["inputs"]["anchor_u"],
                    "leading_t_over_x_not_replaced_by_one":True,
                    "source_t_over_x_evaluation_pending":True},
                "actual_reference_pole254_function_certified":True,
                "actual_reference_basepoint_free_pencil_certified":True,
                "characteristic_zero_reference_coefficients_expanded":False,
                "reference_complete_128_basis_computed":False,
                "reference_new_672_pencil_minor_computed":False,
                "original_t_frame_scalar_expanded":False,
                "nine_field_norms_or_Hecke_action_computed":False,
                "active_eta_support_or_height_computed":False})
            old=self.old("function-and-pencil")
        assert old["source_unit_solution"]==self.refs["unit-solution"]
        assert old["actual_reference_pole254_function_certified"] is True
        self.checkpoint("reference_pencil_complete")

    def run(self):
        self.form_system();self.solve();self.function()
        return self.finish(True,None)

    def manifest(self):
        entries=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name==self.path("current").name or path.name.startswith(PREFIX+"stage-manifest-"):
                continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag
            if value["complete"] is True:
                entries.append(spec(path))
        value={"result":RESULT,"configuration":self.tag,"complete":True,"files":entries,
               "all_committed_complete_mathematical_stages_retained":True,
               "current_checkpoint_excluded":True}
        path=self.path("stage-manifest-"+fingerprint(entries))
        if path.exists():
            assert read(path)==value
        else:
            save(path,value)
        return spec(path)

    def finish(self,complete,error):
        inventory=self.manifest()
        done="function-and-pencil" in self.refs
        value={"result":RESULT,"configuration":self.tag,"complete":bool(complete),"p":41,
               "prime":P,"original_zeta_root":ROOT,"source_R872":identity(self.item["source"]),
               "source_audit":self.refs.get("source-audit"),"constraint_system":self.refs.get("system"),
               "unit_solution":self.refs.get("unit-solution"),
               "reference_function_and_pencil":self.refs.get("function-and-pencil"),
               "actual_reference_pole254_function_certified":done,
               "actual_reference_basepoint_free_pencil_certified":done,
               "actual_reference_function_pole_order":254 if done else None,
               "actual_system_shape":[563,418] if "system" in self.refs else None,
               "actual_system_rank":291 if done else None,
               "old_jets_kernel_products_or_inverses_recomputed":False,
               "characteristic_zero_reference_coefficients_expanded":False,
               "reference_complete_128_basis_computed":False,
               "original_t_frame_scalar_expanded":False,
               "five_original_Lj_RR128_computed":False,
               "nine_field_norms_or_Hecke_action_computed":False,
               "active_eta_support_or_height_computed":False,
               "stage_manifest":inventory,"resume_state":self.current,
               "failure_or_stop_reason":error,"seconds":time.monotonic()-self.started}
        if complete:
            assert done
        save(self.out/FINAL,value)
        return value

def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise SystemExit("R879 arithmetic runs only in the authorized public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    parser.add_argument("--config",required=True)
    parser.add_argument("--output",required=True)
    parser.add_argument("--budget-minutes",type=float,default=30)
    args=parser.parse_args()
    assert 0<args.budget_minutes<=300
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    job=None;final=None;code=1;error=None;started=time.monotonic()
    try:
        job=Job(args)
        final=job.run();code=0
    except BudgetStop as exc:
        code=124;error=str(exc)
    except UnitFailure as exc:
        code=2;error=str(exc)
    except Exception as exc:
        error=type(exc).__name__+": "+str(exc)
        traceback.print_exc()
    if code and job is not None:
        final=job.finish(False,error)
    receipt={"result":RESULT,"source_sha256":sha(__file__),"complete":code==0,
             "process_exit_code":code,"error":error,"seconds":time.monotonic()-started,
             "configuration_sha256":fingerprint(job.tag) if job is not None else None,
             "certificate_sha256":sha(out/FINAL) if (out/FINAL).exists() else None,
             "actual_reference_pole254_function_certified":bool(final and final["actual_reference_pole254_function_certified"]),
             "actual_reference_basepoint_free_pencil_certified":bool(final and final["actual_reference_basepoint_free_pencil_certified"]),
             "characteristic_zero_reference_coefficients_expanded":False,
             "active_eta_support_or_height_computed":False}
    save(out/"core-receipt.json",receipt)
    print(json.dumps(receipt,sort_keys=True,separators=(",",":")),flush=True)
    raise SystemExit(code)

if __name__=="__main__":
    main()
