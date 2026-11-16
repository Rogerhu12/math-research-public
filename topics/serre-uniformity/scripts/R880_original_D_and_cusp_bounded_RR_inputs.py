#!/usr/bin/env python3
"""R880: bounded original D and cusp RR inputs from completed source blocks.

The characteristic-zero columns are exact unit-solve expressions.  This
consumer computes their actual images at the original p753, branch-zero
place and proves completeness with the pinned geometric rank bounds.
Only the public repository's GitHub Actions may execute new mathematics.
"""
import argparse
import gc
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import traceback

RESULT = "R880-original-D-and-cusp-bounded-RR-inputs"
FINAL = "p41-original-D-and-cusp-bounded-RR-inputs-certificate.json"
PREFIX = "R880-"
PRIME, RANK, V3 = 1000000753, 272, 690
EPS = [0]+[1]*144+[2]*127
ROOT_ZETA, ROOT_S, ROOT_B = 549966761, 99932770, 3197390
PAPER_SHA = "5a833046b269b1682f4e6c33c6cc54b6f9d09354f0d40ccf2c47e1455747101e"
SOURCES = ("R845","R872","R827","R820","R842","R849")
PROOFS = ("R880","R872","R845")
BASE = ("result","run_id","source_commit","core_sha256","manifest_sha256")
INPUTS = (
    "old_rank","old_sections","old_normal_index","old_alias_audit","old_pole_DAG",
    "D_basis","D_matrix","point_jets","point_linearization","V2_jets",
    "chi_divisor","chi_kernel","chi_anchor","cusp_reduction","place_audit",
    "W_reduction","global_DAG")
STRATEGY = {
    "scope":"original_D_bounded_representative_and_complete_common_cusp_space",
    "prime":PRIME,"original_branch":0,
    "original_integral_B_root":ROOT_B,"original_s_root":ROOT_S,
    "original_zeta_root":ROOT_ZETA,
    "field":"original L=Q(b,zeta); fixed cusp and chi inputs first over K",
    "normal_basis_degrees":EPS,"normal_integer_scale_applied_again":False,
    "old_fiber_nodes":[0,1,2,3,4],"old_product_matrix_shape":[1360,1380],
    "old_pencil_rank":1111,"old_complete_relation_dimension":269,
    "old_rank_selection_recomputed":False,"old_products_recomputed":False,
    "old_selected_inverse_was_not_saved":True,
    "P0_section_selection":"old a if its actual value is a unit, else old b if unit",
    "point_jet_orders_required":[0,251],
    "V3_jet_matrix_shape":[252,690],"old_V2_jet_columns_copied":418,
    "new_highest_normal_z_power_columns":272,
    "residual_jet_matrix_shape":[123,269],"standardizing_space_dimension":146,
    "standardizing_section_selection":"first unit order123 coefficient, no rescaling",
    "fixed_v_fiber_products_shared_across_trials":True,
    "second_anchor_schedule":"sum(integer_parameter^j * exact_U_j), j=0..145",
    "new_pencil_required_rank":962,"complete_Dstar_dimension":418,
    "common_cusp_constraint_shape":[272,690],
    "common_cusp_rows":20,"common_P0_jet_rows":252,
    "complete_common_cusp_dimension":418,
    "C_quotient_is_a_module_map_not_asserted_a_ring_homomorphism":True,
    "old_Krylov_inverses_normal_conversion_and_P0_jets_recomputed":False,
    "no_sixth_fiber_or_full_polynomial_multiplier_required":True,
    "exact_objects":"original source-bound unit-solve expressions",
    "characteristic_zero_coefficients_reconstructed":False,
    "principal_function":"(a_star/v)^3/(u_chi/tau^2)^4",
    "principal_function_P0_order":-1457,
    "original_five_Lj_RR128_or_144_computed":False,
    "only_budget_trial_limit_and_transport_excluded_from_identity":True,
}

class BudgetStop(RuntimeError):
    pass

class UnitFailure(RuntimeError):
    pass

class SearchStop(RuntimeError):
    pass

def sha(path):
    digest=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(4*1024*1024),b""):
            digest.update(block)
    return digest.hexdigest()

def read(path):
    path=Path(path)
    with (gzip.open(path,"rt",encoding="utf-8") if path.name.endswith(".gz")
          else path.open("r",encoding="utf-8")) as stream:
        return json.load(stream)

def save(path,value):
    path=Path(path);temporary=path.with_name(path.name+".tmp")
    data=json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode("utf-8")
    if path.name.endswith(".gz"):
        with temporary.open("wb") as stream:
            with gzip.GzipFile(filename="",mode="wb",fileobj=stream,mtime=0,compresslevel=1) as zipped:
                zipped.write(data)
    else:
        temporary.write_bytes(data+b"\n")
    os.replace(temporary,path)

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
        ensure_ascii=False).encode("utf-8")).hexdigest()

def plain(entry):
    return {key:entry[key] for key in ("file","bytes","sha256")}

def spec(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}

def bound(directory,entry):
    entry=plain(entry);assert Path(entry["file"]).name==entry["file"]
    path=Path(directory)/entry["file"]
    assert spec(path)==entry,str(path)
    return path

def identity(value):
    return {key:value[key] for key in BASE}

def source_identity(value):
    answer=identity(value)
    for key in ("configuration_sha256","selected_file_count","selected_files_sha256"):
        answer[key]=value[key]
    answer["certificate"]=plain(value["certificate"]) if value.get("certificate") else None
    answer["configuration_stage"]=plain(value["configuration_stage"]) if value.get("configuration_stage") else None
    return answer

def expected_tag(item):
    return {
        "result":RESULT,"source_sha256":item["core_sha256"],"p":41,"python_flint":"0.9.0",
        "method_sha256":item["method_sha256"],
        "proofs_sha256":{key:item["proofs"][key]["sha256"] for key in PROOFS},
        "sources":{label:source_identity(item["sources"][label]) for label in SOURCES},
        "inputs":item["inputs"],"strategy":STRATEGY,
    }

def positions(power):
    return [(i,k) for i in range(RANK) for k in range(max(0,power-EPS[i]+1))]

def rows(matrix):
    return [[int(matrix[i,j]) for j in range(matrix.ncols())] for i in range(matrix.nrows())]

def shape(value,height,width):
    assert len(value)==height and all(len(row)==width for row in value),(height,width)

def pivots(matrix,rank):
    answer=[]
    for i in range(rank):
        answer.append(next(j for j in range(matrix.ncols()) if matrix[i,j]))
    assert answer==sorted(set(answer))
    return answer

class Source:
    def __init__(self,label,value):
        self.label,self.value=label,value
        self.directory=Path(value["directory"])
        self.files={name:plain(entry) for name,entry in value["files"].items()}
        assert all(name==entry["file"] for name,entry in self.files.items())
        assert len(self.files)==value["selected_file_count"]
        assert fingerprint(self.files)==value["selected_files_sha256"]
        for entry in self.files.values():
            bound(self.directory,entry)
        manifest=read(self.directory/"full-outputs-manifest.json")
        assert self.files["full-outputs-manifest.json"]["sha256"]==value["manifest_sha256"]
        assert manifest["result"]==value["result"]
        indexed={entry["file"]:plain(entry) for entry in manifest["files"]}
        assert len(indexed)==len(manifest["files"])
        for name,entry in self.files.items():
            if name not in ("full-outputs-manifest.json","full-outputs-manifest-reference.json"):
                assert indexed[name]==entry,(label,name)
        initial=read(self.directory/"public-actions-input.json")
        run=read(self.directory/"run-receipt.json")
        assert initial["result"]==run["result"]==value["result"]
        assert initial["source_commit"]==run["source_commit"]==value["source_commit"]
        assert initial["core_sha256"]==value["core_sha256"]
        assert str(run["workflow_run_id"])==str(value["run_id"])
        self.certificate=None
        if value.get("certificate"):
            self.certificate=read(bound(self.directory,value["certificate"]))
            assert self.certificate["complete"] is True and self.certificate["result"]==value["result"]
            assert run["complete"] is True and run["process_exit_code"]==0 and run["error"] is None
            self.tag=self.certificate["configuration"]
        else:
            assert label=="R827"
            assert run["complete"] is False
            assert run["process_exit_code"] in value["accepted_checkpoint_exit_codes"]
            assert 0 not in value["accepted_checkpoint_exit_codes"]
            anchor=read(bound(self.directory,value["configuration_stage"]))
            assert anchor["complete"] is True
            self.tag=anchor["configuration"]
        assert self.tag["source_sha256"]==value["core_sha256"]
        assert self.tag["result"]==value["result"]
        assert fingerprint(self.tag)==value["configuration_sha256"]
        if run.get("core_receipt_sha256") is not None:
            assert self.files["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
            core=read(self.directory/"core-receipt.json")
            assert core["result"]==value["result"] and core["source_sha256"]==value["core_sha256"]
            if self.certificate is not None:
                assert core["complete"] is True
                if "certificate_sha256" in core:
                    assert core["certificate_sha256"]==plain(value["certificate"])["sha256"]
            else:
                assert core["complete"] is False
        else:
            assert self.certificate is None and run["complete"] is False
        self.initial,self.run=initial,run

    def stage(self,entry):
        entry=plain(entry)
        assert self.files[entry["file"]]==entry
        value=read(self.directory/entry["file"])
        assert value["complete"] is True and value["configuration"]==self.tag
        if "result" in value:
            assert value["result"]==self.value["result"]
        return value

    def ref(self,entry):
        entry=plain(entry)
        assert self.files[entry["file"]]==entry
        return {"source_group":self.label,**entry}


class Job:
    def __init__(self,args):
        import flint
        assert flint.__version__=="0.9.0"
        self.Matrix,self.Poly=flint.nmod_mat,flint.nmod_poly
        self.args,self.started=args,time.monotonic()
        self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41
        assert self.item["producer_inputs_pending"] is False
        assert self.item["core_sha256"]==sha(__file__)
        assert self.item["proofs"]["R880"]["sha256"]==PAPER_SHA
        assert sha(self.item["method"])==self.item["method_sha256"]
        assert set(self.item["proofs"])==set(PROOFS)
        for value in self.item["proofs"].values():
            assert sha(value["path"])==value["sha256"]
        assert set(self.item["sources"])==set(SOURCES)
        assert set(self.item["inputs"])==set(INPUTS)
        self.tag=expected_tag(self.item)
        self.out=Path(args.out);self.out.mkdir(parents=True,exist_ok=True)
        self.status="initializing";self.refs={};self.sources={}
        self.current=None
        self.maximum_trials=int(self.item.get("maximum_trials",4))
        assert self.maximum_trials>=1
        self.V2,self.V3=positions(2),positions(3)
        assert len(self.V2)==418 and len(self.V3)==690
        self.V3map={pair:j for j,pair in enumerate(self.V3)}
        self.accepted_trial=None;self.actual_rank=None

    def budget(self):
        if time.monotonic()-self.started>=self.args.budget_minutes*60-20:
            raise BudgetStop("All completed original stages retained; next="+self.status)

    def mat(self,value):
        return self.Matrix(value,PRIME)

    def zero(self,h,w):
        return self.mat([[0]*w for _ in range(h)])

    def eye(self,n):
        return self.mat([[int(i==j) for j in range(n)] for i in range(n)])

    def sub(self,matrix,I,J):
        return self.mat([[int(matrix[i,j]) for j in J] for i in I])

    def path(self,name):
        name=PREFIX+name if not name.startswith(PREFIX) else name
        assert Path(name).name==name
        return self.out/(name if name.endswith(".json.gz") else name+".json.gz")

    def old(self,name):
        path=self.path(name)
        if not path.exists():
            return None
        value=read(path)
        assert value["result"]==RESULT and value["configuration"]==self.tag
        assert value["complete"] is True
        return value

    def put(self,name,value):
        self.status=name
        assert not any(k in value for k in ("result","configuration","complete"))
        save(self.path(name),dict(value,result=RESULT,configuration=self.tag,complete=True))
        print(json.dumps({"stage":name,"seconds":round(time.monotonic()-self.started,6)}),flush=True)
        return self.old(name)

    def own(self,entry):
        entry=plain(entry);assert spec(self.path(entry["file"]))==entry
        return self.old(entry["file"])

    def ref(self,name):
        return spec(self.path(name))

    def checkpoint(self,stage,**detail):
        value={"result":RESULT,"configuration":self.tag,"complete":False,
               "stage":stage,"references":self.refs,**detail}
        save(self.path("current"),value)
        self.current=self.ref("current")

    def source_input(self,key):
        entry=self.item["inputs"][key];source=self.sources[entry["source_group"]]
        return source.stage(entry),source.ref(entry)

    def inherited_identity(self,record,label):
        expected=self.sources[label].value
        assert identity(record)==identity(expected),(label,identity(record),identity(expected))
        if "configuration_sha256" in record:
            assert record["configuration_sha256"]==expected["configuration_sha256"]

    def prepare(self):
        self.sources={label:Source(label,self.item["sources"][label]) for label in SOURCES}
        for key in INPUTS:
            value,ref=self.source_input(key)
            setattr(self,key,value);setattr(self,key+"_ref",ref)
        self.r845,self.r872,self.r827,self.r820,self.r842,self.r849=(self.sources[x] for x in SOURCES)
        assert self.r845.certificate["complete_original_D_pencil_certified"] is True
        assert self.r845.certificate["complete_original_Ey_ideal_certified"] is True
        assert self.r845.certificate["actual_pencil_rank"]==1111
        assert self.r845.certificate["accepted_integer_parameter"]==1
        assert self.r845.certificate["original_branch"]==0
        assert self.old_rank["prime"]==PRIME and self.old_rank["actual_rank"]==1111
        assert self.old_rank["original_D_pencil_certified"] is True
        assert self.old_rank["image_is_exactly_H0_6H_minus_original_D"] is True
        assert self.old_rank["additional_common_zero_divisor_degree"]==0
        assert self.old_rank["actual_minor_determinant_mod_prime"]==633901576
        assert self.old_rank["matrix_shape"]==[1360,1380]
        assert plain(self.old_rank["source_candidate_sections"])==plain(self.old_sections_ref)
        assert self.old_sections["a_exact_D_basis_column"]==0
        assert self.old_sections["b_exact_D_basis_coefficients"]=={
            "formula":"integer_parameter^j","integer_parameter":1,"j_range":[0,295]}
        assert self.old_sections["all_original_free_coordinates_verified"] is True
        assert self.old_sections["a_and_b_are_the_original_unit_solve_sections"] is True
        assert self.old_sections["extra_rescaling_or_reconstruction_used"] is False
        assert plain(self.old_sections["source_complete_original_D_basis"])==plain(self.D_basis_ref)
        assert self.D_basis["exact_original_D_RR_space_as_unit_chart_expression_certified"] is True
        assert self.D_basis["actual_rank"]==395
        assert self.D_basis["all830_original_equations_verified_for_all295_columns"] is True
        assert self.D_basis["original_free_normalization_identity_verified"] is True
        assert plain(self.D_basis["source_original_D_matrix"])==plain(self.D_matrix_ref)
        assert self.D_basis["exact_unit_solve_expression"]["exact_kernel"]=="H0(3H-D)"
        assert self.D_basis["exact_unit_solve_expression"]["exact_dimension"]==295
        assert self.D_matrix["matrix_shape"]==[830,690]
        assert self.D_matrix["actual_P0_multiplicity_in_D"]==0
        assert self.D_matrix["both_original_fixed_anchors_used"] is True
        assert self.r842.certificate["original_branch"]==0
        assert self.old_normal_index["dimension"]==690
        assert self.old_normal_index["normal_basis_rank"]==272
        assert self.old_normal_index["normal_row_mapping"]==[list(x) for x in self.V3]
        assert self.old_normal_index["all690_rhs_and_all1380_equations_and_weighted_support_verified"] is True
        assert self.old_alias_audit["original_D_not_replaced_by_a_linearly_equivalent_divisor"] is True
        assert self.old_pole_DAG["complete_original_D_ideal_certified"] is True
        assert self.old_pole_DAG["complete_original_Ey_ideal_certified"] is True
        assert self.old_pole_DAG["original_D_degree"]==395
        assert self.old_pole_DAG["original_Ey_degree"]==1206

        # BASE identity and the actual original K/L place are separate checks.
        self.inherited_identity(self.r845.tag["sources"]["R827"],"R827")
        self.inherited_identity(self.r845.tag["sources"]["R842"],"R842")
        self.inherited_identity(self.r872.tag["sources"]["R827"],"R827")
        self.inherited_identity(self.r842.tag["sources"]["R827"],"R827")
        self.inherited_identity(self.r849.tag["source_identities"]["R845"],"R845")
        self.inherited_identity(self.r827.tag["source_identities"]["R820"],"R820")
        assert self.place_audit["prime"]==PRIME
        assert self.place_audit["original_branch"]==0
        assert self.place_audit["canonical_free_column"]==1186
        assert self.place_audit["original_integral_B_root"]==ROOT_B
        assert self.place_audit["original_s_root"]==ROOT_S
        assert self.place_audit["original_zeta_root"]==ROOT_ZETA
        assert self.place_audit["original_lambda_is_a_unit"] is True
        assert self.place_audit["genuine_DVR_lift_source_not_an_arbitrary_modular_kernel_candidate"] is True
        assert self.point_linearization["prime"]==PRIME
        assert self.point_linearization["original_zeta_root"]==ROOT_ZETA
        assert plain(self.point_linearization["source_W_reduction"])==plain(self.W_reduction_ref)
        assert self.W_reduction["prime"]==PRIME
        assert self.W_reduction["original_rational_denominators_all_units"] is True
        assert self.W_reduction["original_W_e0_equals_e1_verified"] is True
        assert self.r872.certificate["actual_original_P0_jets_through_order272_computed"] is True
        assert self.r872.certificate["actual_fixed_chi_complete_418_RR_space_certified"] is True
        assert self.point_jets["first_order"]==0 and self.point_jets["last_order"]==272
        assert self.point_jets["all273_orders_and_all272_normal_equations_verified"] is True
        assert self.point_jets["exact_characteristic_zero_Hensel_expressions_defined"] is True
        self.parameter=self.point_jets["local_parameter"]
        assert self.parameter==self.point_linearization["chosen_local_parameter"]
        assert self.parameter in ("z_minus_z0","w_minus_w0")
        assert self.V2_jets["matrix_shape"]==[273,418]
        assert self.V2_jets["V2_basis"]==[{"normal_basis_row":i,"power_of_z":k} for i,k in self.V2]
        assert plain(self.V2_jets["source_point_jets"])==plain(self.point_jets_ref)
        assert self.chi_divisor["actual_complete_fixed_chi_RR_space_certified"] is True
        assert self.chi_divisor["D_chi_degree"]==272
        assert self.chi_divisor["D_chi_effective_and_avoids_original_P0"] is True
        assert plain(self.chi_divisor["source_complete_W_Dchi"])==plain(self.chi_kernel_ref)
        assert plain(self.chi_divisor["source_exact_u"])==plain(self.chi_anchor_ref)
        assert self.chi_anchor["order272_is_exact"] is True and self.chi_anchor["exact_order272_unit"]
        assert self.chi_anchor["normal_integer_scale_applied_again"] is False
        assert self.r820.certificate["complete_polynomial_kernels_certified"] is True
        assert self.r820.certificate["same_original_cusp_field_and_two_chart_transitions_verified"] is True
        assert self.cusp_reduction["prime"]==PRIME
        assert self.cusp_reduction["all_original_rational_coefficients_p_integral"] is True
        assert self.cusp_reduction["original_exact_two_chart_transition_certificate_preserved"] is True
        assert self.cusp_reduction["complete_flat_target_not_squarefree_replacement"] is True
        assert set(self.cusp_reduction["charts"])=={"tau","sigma"}
        for chart in ("tau","sigma"):
            index=self.r820.stage(self.cusp_reduction["source_R820_indexes"][chart])
            originals=self.cusp_reduction["charts"][chart]["original_column_sources"]
            assert len(originals)==272
            assert [plain(x) for x in index["Hermite_columns_in_original_basis_order"]]==[plain(x) for x in originals]
            for entry in originals:
                assert self.r820.files[entry["file"]]==plain(entry)
        assert self.global_DAG["five_original_addition_pole_ideals_as_fractional_DAGs_certified"] is True
        assert self.global_DAG["original_eta_Picard_input_DAGs_defined"] is True
        outputs=self.global_DAG["five_original_polar_and_eta_outputs"]
        assert set(outputs)=={"1","2","3","4","5"}
        for j in range(1,6):
            assert set(outputs[str(j)]["eta_degree_zero_fractional_ideal"])=={"tau","sigma"}
        self.old_products=[];self.fibers=[]
        assert len(self.old_rank["source_fiber_products"])==5
        for z0,entry in enumerate(self.old_rank["source_fiber_products"]):
            assert entry["z0"]==z0
            a,b=self.r845.stage(entry["a"]),self.r845.stage(entry["b"])
            assert a["z0"]==b["z0"]==z0 and a["prime"]==b["prime"]==PRIME
            assert a["which"]=="a" and b["which"]=="b"
            assert a["matrix_shape"]==b["matrix_shape"]==[272,690]
            assert plain(a["source_original_fiber_evaluation"])==plain(b["source_original_fiber_evaluation"])
            ep=plain(a["source_original_fiber_evaluation"]);evaluation=self.r845.stage(ep)
            kp=plain(evaluation["source_original_Krylov_point"]);point=self.r827.stage(kp)
            assert point["prime"]==PRIME and point["z0"]==z0 and point["usable"] is True
            assert point["actual_cyclic_rank"]==272
            assert point["both_inverse_products_verified"] is True
            assert plain(point["source_original_W"])==plain(self.W_reduction_ref)
            assert plain(self.old_alias_audit["source_original_W"])==plain(self.W_reduction_ref)
            shape(a["product_evaluation_matrix_mod_prime"],272,690)
            shape(b["product_evaluation_matrix_mod_prime"],272,690)
            shape(evaluation["original_V3_evaluation_matrix_mod_prime"],272,690)
            shape(evaluation["original_V3_Krylov_coordinates_mod_prime"],272,690)
            self.old_products.append((a,b,self.r845.ref(entry["a"]),self.r845.ref(entry["b"])))
            self.fibers.append((evaluation,self.r845.ref(ep),point,self.r827.ref(kp)))
        name="original-source-place-and-block-audit"
        if self.old(name) is None:
            self.put(name,{
                "prime":PRIME,"original_branch":0,"original_integral_B_root":ROOT_B,
                "original_b_root":self.place_audit["original_b_root"],
                "original_s_root":ROOT_S,"original_zeta_root":ROOT_ZETA,
                "R845_R872_R842_same_original_R827_place_verified":True,
                "source_original_D_kernel":self.D_basis_ref,
                "source_original_1111_profile":self.old_rank_ref,
                "source_original_pencil_sections":self.old_sections_ref,
                "source_original_V3_normal_index":self.old_normal_index_ref,
                "source_original_point_jets":self.point_jets_ref,
                "source_original_V2_jet_matrix":self.V2_jets_ref,
                "source_complete_original_two_chart_C":self.cusp_reduction_ref,
                "source_complete_fixed_chi":self.chi_divisor_ref,
                "source_original_global_eta_DAG":self.global_DAG_ref,
                "original_eta_nodes":{str(j):outputs[str(j)]["eta_degree_zero_fractional_ideal"] for j in range(1,6)},
                "old_original_products_jets_or_inverse_arithmetic_recomputed":False,
                "finite_images_not_relabelled_as_characteristic_zero_coefficients":True,
            })
        self.refs["source_audit"]=self.ref(name)
        self.checkpoint("original_sources_bound")


    def normal_matrix(self):
        matrix=[[0]*690 for _ in range(690)];first_expected=0
        for entry in self.old_normal_index["blocks"]:
            block=self.r845.stage(entry);first,stop=block["original_V3_indices"]
            assert first==first_expected and first<stop<=690
            assert block["normal_row_mapping"]==[list(x) for x in self.V3]
            assert block["all1380_original_equations_verified"] is True
            assert block["all_extra_weight5_coordinates_zero"] is True
            assert block["exact_unit_solve_expression"]["no_additional_scale"] is True
            shape(block["normal_coefficients_mod_prime"],690,stop-first)
            for i,row in enumerate(block["normal_coefficients_mod_prime"]):
                matrix[i][first:stop]=row
            first_expected=stop
        assert first_expected==690
        self.normal=self.mat(matrix)
        return self.normal

    def V3_jets(self):
        name="original-V3-252-point-jet-matrix";old=self.old(name)
        if old is None:
            self.status=name;self.budget()
            jets=[];z=[];zz=[];zzz=[];originals=[]
            previous=None
            assert len(self.point_jets["orders"])==273
            for n,entry in enumerate(self.point_jets["orders"][:252]):
                value=self.r872.stage(entry)
                assert value["order"]==n and value["local_parameter"]==self.parameter
                assert plain(value["source_point_linearization"])==plain(self.point_linearization_ref)
                assert value["all272_original_eigenvector_equations_verified_at_this_order"] is True
                assert value["beta0_and_beta1_normalizations_verified"] is True
                assert len(value["normal_basis_jet_mod_prime"])==272
                if previous is not None:
                    assert plain(value["source_previous_order"])==previous
                jets.append(value["normal_basis_jet_mod_prime"])
                z.append(value["z_jet_mod_prime"])
                zz.append(value["shift_z_square_coefficient_mod_prime"])
                zzz.append(value["shift_z_cube_coefficient_mod_prime"])
                previous=plain(entry);originals.append(self.r872.ref(entry))
            z0=z[0]
            zp=[
                self.Poly([1],PRIME),self.Poly(z,PRIME),
                self.Poly([(z0*z0 if n==0 else 2*z0*z[n]+zz[n])%PRIME for n in range(252)],PRIME),
                self.Poly([(z0**3 if n==0 else 3*z0*z0*z[n]+3*z0*zz[n]+zzz[n])%PRIME
                           for n in range(252)],PRIME)]
            data=[[0]*690 for _ in range(252)]
            copied=[]
            for j,pair in enumerate(self.V2):
                target=self.V3map[pair];copied.append([j,target])
                for n in range(252):
                    data[n][target]=self.V2_jets["matrix_mod_prime"][n][j]
            new_columns=[]
            for i in range(272):
                self.budget()
                power=3-EPS[i];column=self.V3map[(i,power)]
                product=self.Poly([jets[n][i] for n in range(252)],PRIME)*zp[power]
                for n in range(252):
                    data[n][column]=int(product[n])
                new_columns.append(column)
            assert len(copied)==418 and len(new_columns)==272
            assert sorted([pair[1] for pair in copied]+new_columns)==list(range(690))
            self.put(name,{
                "prime":PRIME,"matrix_shape":[252,690],"matrix_mod_prime":data,
                "V3_basis":[{"normal_basis_row":i,"power_of_z":k} for i,k in self.V3],
                "row_orders":list(range(252)),"local_parameter":self.parameter,
                "source_point_jets":self.point_jets_ref,
                "source_original_V2_jet_matrix":self.V2_jets_ref,
                "original_jet_order_sources":originals,
                "copied_original_V2_to_V3_column_pairs":copied,
                "new_highest_power_columns":new_columns,
                "all418_original_columns_copied_without_recomputation":True,
                "only272_highest_power_columns_newly_computed":True,
                "no_original_Hensel_step_recomputed":True,
                "exact_matrix_definition":{
                    "operation":"original_normal_beta_times_original_z_power",
                    "source_point_jets":self.point_jets_ref,
                    "normal_basis_positions":[list(x) for x in self.V3],
                    "coefficient_orders":[0,251],"no_extra_82_scale":True},
            })
            old=self.old(name)
        assert old["source_point_jets"]==self.point_jets_ref
        assert old["source_original_V2_jet_matrix"]==self.V2_jets_ref
        shape(old["matrix_mod_prime"],252,690)
        self.J3=self.mat(old["matrix_mod_prime"])
        self.refs["V3_jets"]=self.ref(name)
        self.checkpoint("original_V3_jets_complete")
        return self.refs["V3_jets"]

    def full_row_kernel(self,name,matrix,source_refs,exact_description):
        old=self.old(name);height,width=matrix.nrows(),matrix.ncols()
        if old is None:
            self.status=name;self.budget()
            augmented=self.mat([[int(matrix[i,j]) for j in range(width)]
                                +[int(i==j) for j in range(height)] for i in range(height)])
            reduced,total_rank=augmented.rref()
            assert total_rank==height
            selected=[j for j in pivots(reduced,height) if j<width]
            rank=len(selected)
            if rank!=height:
                self.put(name,{
                    "prime":PRIME,"accepted":False,"matrix_shape":[height,width],
                    "actual_rank_mod_prime":rank,"required_rank":height,
                    "source_references":source_refs,"selected_pivot_columns":selected,
                    "failure_only_this_sufficient_residue_certificate":True})
                raise UnitFailure(name+": deficient residue row rank")
            free=[j for j in range(width) if j not in set(selected)]
            square=self.sub(matrix,list(range(height)),selected)
            inverse=self.sub(reduced,list(range(height)),list(range(width,width+height)))
            assert square*inverse==self.eye(height) and inverse*square==self.eye(height)
            data=[[0]*len(free) for _ in range(width)]
            for j,col in enumerate(free):
                data[col][j]=1
                for i,pivot in enumerate(selected):
                    data[pivot][j]=-int(reduced[i,col])%PRIME
            kernel=self.mat(data)
            assert matrix*kernel==self.zero(height,len(free))
            self.put(name,{
                "prime":PRIME,"accepted":True,"matrix_shape":[height,width],
                "actual_rank_mod_prime":height,"actual_kernel_dimension":len(free),
                "source_references":source_refs,"selected_row_indices":list(range(height)),
                "selected_pivot_columns":selected,"free_columns":free,
                "inverse_selected_minor_mod_prime":rows(inverse),
                "both_selected_inverse_products_verified":True,
                "kernel_basis_mod_prime":data,
                "all_original_equations_verified":True,
                "free_normalization_identity_verified":True,
                "full_characteristic_zero_kernel_certified":True,
                "exact_unit_solve_expression":{
                    "operation":"kernel_of_the_complete_original_source_matrix",
                    "source_references":source_refs,"row_indices":list(range(height)),
                    "selected_columns":selected,"free_columns":free,
                    "pivot_coordinates":"-inverse(selected_square)*original_free_columns",
                    "free_coordinates":"identity","geometric_definition":exact_description,
                    "modular_arrays_are_not_reconstructed_characteristic_zero_coefficients":True}})
            old=self.old(name)
        assert old["source_references"]==source_refs
        if old["accepted"] is not True:
            raise UnitFailure(name+": retained sufficient residue test failed")
        assert old["actual_rank_mod_prime"]==height
        assert old["actual_kernel_dimension"]==width-height
        return self.mat(old["kernel_basis_mod_prime"]),self.ref(name)

    def common_cusp(self):
        name="common-cusp-and-252P0-constraint-matrix";old=self.old(name)
        if old is None:
            self.status=name;self.budget()
            chart=self.cusp_reduction["charts"]["tau"]
            assert len(chart["q_polynomials"])==271
            P=self.Poly(chart["P_polynomial"],PRIME)
            assert P.degree()==20 and int(P[20])==1
            quotient=[[0]*690 for _ in range(20)]
            z=self.Poly([0,1],PRIME)
            for i in range(272):
                polynomial=self.Poly(chart["q_polynomials"][i] if i<271 else [1],PRIME)
                for k in range(4-EPS[i]):
                    col=self.V3map[(i,k)]
                    for n in range(20):
                        quotient[n][col]=int(polynomial[n])
                    polynomial=(polynomial*z)%P
            data=quotient+rows(self.J3)
            shape(data,272,690)
            self.put(name,{
                "prime":PRIME,"matrix_shape":[272,690],"matrix_mod_prime":data,
                "cusp_quotient_matrix_mod_prime":quotient,
                "source_original_two_chart_C":self.cusp_reduction_ref,
                "source_V3_point_jets":self.refs["V3_jets"],
                "all20_original_cusp_field_coordinates_retained":True,
                "point_jet_orders":list(range(252)),
                "C_quotient_convention":"rem_P(p271+sum(pj*qj,j<271))",
                "C_quotient_only_used_as_original_K_z_module_map":True,
                "both_original_chart_column_inventories_preserved":True,
                "original_C_rational_reduction_or_Hermite_not_recomputed":True,
                "exact_divisor":"D_C=C+252P0","exact_divisor_degree":272,
                "original_P0_not_in_C":True})
            old=self.old(name)
        assert old["source_original_two_chart_C"]==self.cusp_reduction_ref
        assert old["source_V3_point_jets"]==self.refs["V3_jets"]
        self.refs["common_cusp_matrix"]=self.ref(name)
        kernel,entry=self.full_row_kernel("complete-common-cusp-418-kernel",
            self.mat(old["matrix_mod_prime"]),
            {"constraint_matrix":self.ref(name)},
            {"RR_space":"H0(3H-(C+252P0))","dimension":418,
             "degree_after_subtraction":544,"full_constraint_rank":272,
             "both_original_affine_cusp_ideals":self.cusp_reduction_ref})
        assert kernel.nrows()==690 and kernel.ncols()==418
        self.refs["complete_common_cusp_kernel"]=entry
        self.checkpoint("complete_common_cusp_418_space")
        return entry

    def select_original_a(self):
        name="original-P0-unit-anchor-selection";old=self.old(name)
        if old is None:
            self.status=name;self.budget()
            first=self.sub(self.J3,[0],list(range(690)))*self.normal
            av=self.old_sections["a_original_V3_coordinates_mod_prime"]
            bv=self.old_sections["b_original_V3_coordinates_mod_prime"]
            assert len(av)==len(bv)==690
            values=first*self.mat([av,bv]).transpose()
            va,vb=int(values[0,0]),int(values[0,1])
            accepted=bool(va or vb)
            role="a" if va else ("b" if vb else None)
            self.put(name,{
                "prime":PRIME,"accepted":accepted,"selected_original_role":role,
                "source_original_sections":self.old_sections_ref,
                "source_original_normal_index":self.old_normal_index_ref,
                "source_original_point_jets":self.refs["V3_jets"],
                "old_a_value_mod_prime":va,"old_b_value_mod_prime":vb,
                "selected_P0_value_mod_prime":va if role=="a" else vb,
                "selected_exact_section_definition":{
                    "operation":"original_R845_section_unchanged",
                    "source":self.old_sections_ref,"role":role},
                "block_swap_used":role=="b","no_rescaling":True,
                "failure_only_this_sufficient_residue_certificate":not accepted})
            old=self.old(name)
        if not old["accepted"]:
            raise UnitFailure("Both original R845 anchors have nonunit P0 values at this place")
        assert old["selected_original_role"] in ("a","b")
        self.anchor_role=old["selected_original_role"]
        self.a0=int(old["selected_P0_value_mod_prime"])
        assert self.a0
        self.refs["original_a_selection"]=self.ref(name)
        return old

    def selected_kernel(self,label,matrix,I,J,source_refs,geometric_definition):
        rank=len(I);width=matrix.ncols();height=matrix.nrows()
        assert len(J)==rank and len(set(I))==rank and len(set(J))==rank
        assert all(0<=i<height for i in I) and all(0<=j<width for j in J)
        free=[j for j in range(width) if j not in set(J)]
        inverse_name=label+"-selected-inverse";inverse_data=self.old(inverse_name)
        if inverse_data is None:
            self.status=inverse_name;self.budget()
            square=self.sub(matrix,I,J)
            try:
                inverse=square.inv()
            except ZeroDivisionError:
                self.put(inverse_name,{
                    "prime":PRIME,"accepted":False,"source_references":source_refs,
                    "selected_rows":I,"selected_columns":J,
                    "failure_only_this_sufficient_residue_certificate":True})
                raise UnitFailure(inverse_name+": nonunit selected minor")
            assert square*inverse==self.eye(rank) and inverse*square==self.eye(rank)
            self.put(inverse_name,{
                "prime":PRIME,"accepted":True,"source_references":source_refs,
                "selected_rows":I,"selected_columns":J,
                "inverse_mod_prime":rows(inverse),
                "both_inverse_products_verified":True,
                "original_selected_rank_profile_not_recomputed":label=="original-1111",
                "exact_inverse_definition":{
                    "operation":"inverse_of_original_selected_square",
                    "source_references":source_refs,"rows":I,"columns":J}})
            inverse_data=self.old(inverse_name)
        if not inverse_data["accepted"]:
            raise UnitFailure(inverse_name+": retained nonunit minor")
        assert inverse_data["source_references"]==source_refs
        assert inverse_data["selected_rows"]==I and inverse_data["selected_columns"]==J
        name=label+"-complete-kernel";old=self.old(name)
        if old is None:
            self.status=name;self.budget()
            inverse=self.mat(inverse_data["inverse_mod_prime"])
            selected_rhs=self.sub(matrix,I,free)
            coordinates=-(inverse*selected_rhs)
            data=[[0]*len(free) for _ in range(width)]
            for k,col in enumerate(free):
                data[col][k]=1
                for i,pivot in enumerate(J):
                    data[pivot][k]=int(coordinates[i,k])
            kernel=self.mat(data)
            assert matrix*kernel==self.zero(height,len(free))
            self.put(name,{
                "prime":PRIME,"matrix_shape":[height,width],"actual_rank":rank,
                "actual_kernel_dimension":len(free),"source_references":source_refs,
                "source_selected_inverse":self.ref(inverse_name),
                "selected_rows":I,"selected_columns":J,"free_columns":free,
                "kernel_basis_mod_prime":data,
                "all_original_fiber_equations_verified":True,
                "free_normalization_identity_verified":True,
                "full_characteristic_zero_kernel_certified":True,
                "exact_unit_solve_expression":{
                    "operation":"complete_original_kernel_with_free_identity",
                    "source_references":source_refs,
                    "source_selected_inverse":self.ref(inverse_name),
                    "free_columns":free,"selected_columns":J,
                    "geometric_definition":geometric_definition,
                    "rank_upper_bound_from_complete_original_RR_space":rank,
                    "modular_arrays_not_reconstructed_characteristic_zero_coefficients":True}})
            old=self.old(name)
        assert old["source_references"]==source_refs
        assert old["source_selected_inverse"]==self.ref(inverse_name)
        assert old["actual_rank"]==rank and old["actual_kernel_dimension"]==len(free)
        return self.mat(old["kernel_basis_mod_prime"]),self.ref(name)

    def project_second(self,label,kernel,kernel_ref,dimension,RR_definition):
        name=label+"-projected-original-V3-basis";old=self.old(name)
        if old is None:
            self.status=name;self.budget()
            projected=self.sub(kernel,list(range(690,1380)),list(range(dimension)))
            reduced,rank=projected.transpose().rref()
            if rank!=dimension:
                self.put(name,{
                    "prime":PRIME,"accepted":False,"source_complete_kernel":kernel_ref,
                    "actual_projected_rank":rank,"required_rank":dimension,
                    "failure_only_this_sufficient_residue_certificate":True})
                raise UnitFailure(name+": projected columns lost independence modulo prime")
            row_indices=pivots(reduced,rank)
            normalized=self.normal*projected
            self.put(name,{
                "prime":PRIME,"accepted":True,"actual_projected_rank":dimension,
                "source_complete_kernel":kernel_ref,
                "source_original_normal_index":self.old_normal_index_ref,
                "projection_to_input_block":1,
                "original_V3_basis_mod_prime":rows(projected),
                "normal_V3_basis_mod_prime":rows(normalized),
                "matrix_shape":[690,dimension],"independent_original_V3_rows":row_indices,
                "exact_RR_space":RR_definition,
                "complete_RR_space_certified":True,
                "exact_unit_solve_expression":{
                    "operation":"second_block_projection_of_complete_original_relation_kernel",
                    "source_kernel":kernel_ref,"source_original_normal_index":self.old_normal_index_ref,
                    "projection_rows":[690,1380],
                    "nonzero_first_anchor_makes_projection_injective":True,
                    "modular_images_not_reconstructed_exact_coefficients":True}})
            old=self.old(name)
        if not old["accepted"]:
            raise UnitFailure(name+": retained projection unit certificate failed")
        assert old["source_complete_kernel"]==kernel_ref
        assert old["actual_projected_rank"]==dimension
        return old,self.ref(name)

    def residual_F_space(self):
        selection=self.select_original_a()
        swapped=selection["block_swap_used"]
        data=[];source_products=[]
        for z0,(a,b,ar,br) in enumerate(self.old_products):
            left,right=(b,a) if swapped else (a,b)
            data.extend([x+y for x,y in zip(left["product_evaluation_matrix_mod_prime"],
                                            right["product_evaluation_matrix_mod_prime"])])
            source_products.append({"z0":z0,"first":br if swapped else ar,"second":ar if swapped else br})
        matrix=self.mat(data);del data
        I=list(self.old_rank["selected_original_fiber_rows"])
        oldJ=list(self.old_rank["selected_original_V3_pair_columns"])
        J=[(j+690 if j<690 else j-690) for j in oldJ] if swapped else oldJ
        source_refs={"old_rank_profile":self.old_rank_ref,
                     "original_anchor_selection":self.refs["original_a_selection"],
                     "original_fiber_products":source_products}
        kernel,entry=self.selected_kernel("original-1111",matrix,I,J,source_refs,
            {"relation":"a_star*r+b_star*s=0","F":"div_3H(a_star)-D","degree_F":421,
             "dimension":269,"evaluation_injective_on_complete_original_image_by_R845":True})
        self.refs["old_complete_269_relation_kernel"]=entry
        projected,pref=self.project_second("residual-F",kernel,entry,269,
            {"space":"H0(3H-F)","degree_F":421,"dimension":269,
             "F_plus_D_is_divisor_of_original_a_star":True})
        self.refs["complete_residual_F_space"]=pref
        self.F_original=self.mat(projected["original_V3_basis_mod_prime"])
        self.F_normal=self.mat(projected["normal_V3_basis_mod_prime"])
        self.checkpoint("complete_269_residual_F_space")
        del matrix,kernel
        gc.collect()
        return pref

    def standardizing_space(self):
        name="residual-F-123P0-jet-constraints";old=self.old(name)
        if old is None:
            self.status=name;self.budget()
            matrix=self.sub(self.J3,list(range(123)),list(range(690)))*self.F_normal
            extra=self.sub(self.J3,[123],list(range(690)))*self.F_normal
            self.put(name,{
                "prime":PRIME,"matrix_shape":[123,269],"matrix_mod_prime":rows(matrix),
                "order123_row_mod_prime":rows(extra)[0],
                "source_complete_residual_F_space":self.refs["complete_residual_F_space"],
                "source_original_V3_jets":self.refs["V3_jets"],
                "vanishing_orders":list(range(123)),
                "extra_order123_used_for_simple_choice":True})
            old=self.old(name)
        assert old["source_complete_residual_F_space"]==self.refs["complete_residual_F_space"]
        U,uref=self.full_row_kernel("complete-standardizing-146-kernel",
            self.mat(old["matrix_mod_prime"]),{"constraint_matrix":self.ref(name)},
            {"space":"H0(3H-F-123P0)","dimension":146,
             "degree_after_subtraction":272,"full_constraint_rank":123})
        self.refs["standardizing_kernel"]=uref
        name2="standardizing-146-original-V3-basis";basis=self.old(name2)
        if basis is None:
            self.status=name2;self.budget()
            original=self.F_original*U;normal=self.F_normal*U
            extra=self.mat([old["order123_row_mod_prime"]])*U
            values=rows(extra)[0]
            candidates=[i for i,value in enumerate(values) if value]
            accepted=bool(candidates)
            self.put(name2,{
                "prime":PRIME,"accepted":accepted,"dimension":146,
                "source_complete_146_kernel":uref,
                "source_complete_residual_F_space":self.refs["complete_residual_F_space"],
                "source_original_123_jet_constraints":self.ref(name),
                "original_V3_basis_mod_prime":rows(original),
                "normal_V3_basis_mod_prime":rows(normal),
                "order123_coefficients_mod_prime":values,
                "selected_first_order123_unit_column":candidates[0] if candidates else None,
                "selected_column_rescaled":False,
                "actual_complete_standardizing_RR_space_certified":True,
                "exact_basis_definition":{
                    "operation":"compose_two_original_complete_unit_kernel_definitions",
                    "outer_basis":self.refs["complete_residual_F_space"],
                    "inner_kernel":uref}})
            basis=self.old(name2)
        assert basis["source_complete_146_kernel"]==uref
        if not basis["accepted"]:
            raise UnitFailure("No standardizing basis column has unit order123 at this place")
        self.U_original=self.mat(basis["original_V3_basis_mod_prime"])
        self.U_normal=self.mat(basis["normal_V3_basis_mod_prime"])
        self.v_index=basis["selected_first_order123_unit_column"]
        self.v123=int(basis["order123_coefficients_mod_prime"][self.v_index])
        assert self.v123
        self.refs["complete_standardizing_space"]=self.ref(name2)
        self.checkpoint("complete_146_standardizing_space")
        return self.ref(name2)


    def anchor(self,which,trial=None):
        assert which in ("v","w")
        assert trial is None if which=="v" else isinstance(trial,int) and trial>=1
        name="fixed-v-section" if which=="v" else f"trial-{trial:06d}-w-section"
        old=self.old(name)
        if old is None:
            self.status=name;self.budget()
            coeffs=[int(j==self.v_index) for j in range(146)] if which=="v" else [
                pow(trial,j,PRIME) for j in range(146)]
            column=self.mat([[x] for x in coeffs])
            original=self.U_original*column;normal=self.U_normal*column
            definition={"operation":"selected_exact_standardizing_basis_column",
                        "basis_source":self.refs["complete_standardizing_space"],
                        "column":self.v_index} if which=="v" else {
                        "operation":"integer_moment_curve_in_original_exact_standardizing_basis",
                        "basis_source":self.refs["complete_standardizing_space"],
                        "integer_parameter":trial,"j_range":[0,146],
                        "coefficient_formula":"integer_parameter^j"}
            self.put(name,{
                "prime":PRIME,"which":which,"trial":trial,
                "source_complete_standardizing_space":self.refs["complete_standardizing_space"],
                "original_V3_coordinates_mod_prime":rows(original),
                "normal_V3_coordinates_mod_prime":rows(normal),
                "standardizing_basis_coefficients_mod_prime":coeffs,
                "exact_section_definition":definition,
                "order_at_original_P0_at_least123":True,
                "order123_is_exact":which=="v",
                "order123_coefficient_mod_prime":self.v123 if which=="v" else None,
                "no_rescaling_or_new_coefficient_reconstruction":True})
            old=self.old(name)
        assert old["which"]==which and old["trial"]==trial
        assert old["source_complete_standardizing_space"]==self.refs["complete_standardizing_space"]
        shape(old["original_V3_coordinates_mod_prime"],690,1)
        if which=="v":
            self.refs["fixed_v"]=self.ref(name)
        return old,self.ref(name)

    def fiber_product(self,which,trial,anchor,anchor_ref,z0):
        label="fixed-v" if which=="v" else f"trial-{trial:06d}-w"
        name=label+f"-fiber-{z0}-times-original-V3";old=self.old(name)
        evaluation,eref,point,kref=self.fibers[z0]
        if old is None:
            self.status=name;self.budget()
            E=self.mat(evaluation["original_V3_evaluation_matrix_mod_prime"])
            original=self.mat(anchor["original_V3_coordinates_mod_prime"])
            vector=E*original
            W=self.mat(point["W_evaluated_mod_prime"])
            current=vector;columns=[]
            for j in range(272):
                columns.append([int(current[i,0]) for i in range(272)])
                if j+1<272:
                    current=W*current
            result=self.mat(columns).transpose()*self.mat(
                evaluation["original_V3_Krylov_coordinates_mod_prime"])
            self.put(name,{
                "prime":PRIME,"which":which,"trial":trial if which=="w" else None,
                "z0":z0,"matrix_shape":[272,690],
                "source_anchor":anchor_ref,"source_original_fiber_evaluation":eref,
                "source_original_Krylov_point":kref,
                "source_original_W_reduction":self.W_reduction_ref,
                "section_evaluation_mod_prime":rows(vector),
                "product_evaluation_matrix_mod_prime":rows(result),
                "matrix_direction":"[section,W*section,...,W^271*section] * old(K^-1*V3)",
                "old_Krylov_inverse_and_original_V3_evaluation_not_recomputed":True,
                "fixed_v_products_shared_across_all_trials":which=="v",
                "no_full_polynomial_multiplier_or_sixth_fiber_computed":True})
            old=self.old(name)
        assert old["source_anchor"]==anchor_ref
        assert old["source_original_fiber_evaluation"]==eref
        assert old["source_original_Krylov_point"]==kref
        assert old["z0"]==z0 and old["which"]==which
        return old,self.ref(name)

    def new_trial(self,trial,v,vref):
        w,wref=self.anchor("w",trial)
        data=[];sources=[]
        for z0 in range(5):
            left,lref=self.fiber_product("v",None,v,vref,z0)
            right,rref=self.fiber_product("w",trial,w,wref,z0)
            data.extend([a+b for a,b in zip(left["product_evaluation_matrix_mod_prime"],
                                           right["product_evaluation_matrix_mod_prime"])])
            sources.append({"z0":z0,"v":lref,"w":rref})
            self.checkpoint("new_anchor_products",trial=trial,last_fiber=z0)
        matrix=self.mat(data);del data
        name=f"trial-{trial:06d}-five-fiber-rank"
        profile=self.old(name)
        if profile is None:
            self.status=name;self.budget()
            reduced,rank=matrix.rref()
            assert rank<=962,"The complete original E=F+123P0 source gives the upper bound962."
            answer={
                "prime":PRIME,"integer_parameter":trial,"actual_rank":rank,
                "required_rank":962,"matrix_shape":[1360,1380],
                "source_fixed_v":vref,"source_candidate_w":wref,"source_fiber_products":sources,
                "accepted":rank==962,
                "full_3H_minus_E_pencil_certified":rank==962,
                "additional_common_zero_divisor_degree":0 if rank==962 else None,
                "rank_deficiency_only_fails_this_sufficient_residue_test":rank!=962,
                "fiber_disjointness_or_reducedness_not_assumed":True}
            if rank==962:
                J=pivots(reduced,rank)
                selected=self.sub(matrix,list(range(1360)),J)
                transposed,rank2=selected.transpose().rref()
                assert rank2==962
                I=pivots(transposed,rank2)
                answer.update({
                    "selected_rows":I,"selected_columns":J,
                    "geometric_characteristic_zero_rank_upper_bound":962,
                    "unit_rank_lower_bound":962,
                    "image_is_exactly_H0_6H_minus_F_minus_123P0":True,
                    "original_evaluation_injective_on_this_complete_image":True})
            self.put(name,answer);profile=self.old(name)
        assert profile["source_fixed_v"]==vref and profile["source_candidate_w"]==wref
        assert profile["source_fiber_products"]==sources
        self.actual_rank=profile["actual_rank"]
        if profile["accepted"] is not True:
            self.checkpoint("sufficient_pencil_test_failed",trial=trial,rank=self.actual_rank)
            return False
        source_refs={"profile":self.ref(name),"fixed_v":vref,"candidate_w":wref,
                     "original_fiber_products":sources}
        kernel,kref=self.selected_kernel(f"trial-{trial:06d}-new-962",
            matrix,profile["selected_rows"],profile["selected_columns"],source_refs,
            {"relation":"v*r+w*s=0","dimension":418,
             "common_zero_divisor":"F+123P0","degree_common_zero":544,
             "divisor_of_v":"F+123P0+Dstar","degree_Dstar":272})
        projected,pref=self.project_second(f"trial-{trial:06d}-Dstar",kernel,kref,418,
            {"space":"H0(3H-Dstar)","degree_Dstar":272,"dimension":418,
             "Dstar_definition":"div_3H(v)-F-123P0","P0_not_in_Dstar":True})
        assert projected["complete_RR_space_certified"] is True
        self.accepted_trial=trial
        self.refs["accepted_new_pencil_profile"]=self.ref(name)
        self.refs["accepted_w"]=wref
        self.refs["complete_Dstar_relation_kernel"]=kref
        self.refs["complete_Dstar_kernel"]=pref
        self.checkpoint("complete_original_Dstar_418_space",trial=trial)
        del matrix,kernel
        gc.collect()
        return True

    def principal_inputs(self):
        name="original-D-cusp-chi-principal-inputs"
        old=self.old(name)
        if old is None:
            self.status=name;self.budget()
            u272=int(self.chi_anchor["exact_order272_unit"])
            assert self.a0 and self.v123 and u272
            leading=pow(self.a0,3,PRIME)*pow(
                pow(self.v123,3,PRIME)*pow(u272,4,PRIME)%PRIME,-1,PRIME)%PRIME
            assert leading
            exact_a={"operation":"original_R845_anchor_over_tau_cubed",
                     "source_selection":self.refs["original_a_selection"]}
            exact_v={"operation":"selected_standardizing_section_over_tau_cubed",
                     "source_section":self.refs["fixed_v"]}
            exact_u={"operation":"original_chi_anchor_over_tau_squared",
                     "source_section":self.chi_anchor_ref}
            output={
                "prime":PRIME,"original_field":"L=Q(b,zeta)",
                "original_branch":0,"original_integral_B_root":ROOT_B,
                "original_b_root":self.place_audit["original_b_root"],
                "original_zeta_root":ROOT_ZETA,"original_s_root":ROOT_S,
                "source_original_pole_DAG":self.old_pole_DAG_ref,
                "source_original_global_eta_DAG":self.global_DAG_ref,
                "source_original_D_kernel":self.D_basis_ref,
                "source_original_anchor_selection":self.refs["original_a_selection"],
                "source_standardizing_146_space":self.refs["complete_standardizing_space"],
                "source_exact_v":self.refs["fixed_v"],
                "source_complete_Dstar_418_space":self.refs["complete_Dstar_kernel"],
                "source_complete_D_C_418_space":self.refs["complete_common_cusp_kernel"],
                "source_complete_D_chi_418_space":self.chi_kernel_ref,
                "source_D_chi_divisor":self.chi_divisor_ref,
                "divisors":{
                    "F":{"definition":"div_3H(a_star)-D","degree":421,"P0_not_in_divisor":True},
                    "Dstar":{"definition":"div_3H(v)-F-123P0","degree":272,"P0_not_in_divisor":True,
                             "complete_RR_space":self.refs["complete_Dstar_kernel"]},
                    "D_C":{"definition":"C+252P0","degree":272,
                           "complete_RR_space":self.refs["complete_common_cusp_kernel"]},
                    "D_chi":{"definition":"div_2H(u_chi)-272P0","degree":272,
                             "complete_RR_space":self.chi_kernel_ref}},
                "exact_function_DAG":{
                    "a_star_over_tau3":exact_a,"v_over_tau3":exact_v,
                    "u_chi_over_tau2":exact_u,
                    "G_D":{"operation":"divide","numerator":"a_star_over_tau3","denominator":"v_over_tau3"},
                    "Q_f":{"operation":"divide",
                           "numerator":{"operation":"power","input":"G_D","exponent":3},
                           "denominator":{"operation":"power","input":"u_chi_over_tau2","exponent":4}}},
                "exact_divisor_identities":[
                    "D-395P0=(Dstar-H)+chi+div(a_star/v)",
                    "C-20P0=(D_C-H)+chi",
                    "chi=(D_chi-H)-div(u_chi/tau^2)",
                    "E_f-1206P0=(D_C-H)+3(Dstar-H)+4(D_chi-H)+div(Q_f)"],
                "ideal_principal_factor_direction":"positive multiplication by Q_f",
                "Q_f_order_in_actual_local_parameter":-1457,
                "actual_local_parameter":self.parameter,
                "Q_f_leading_coefficient_mod_prime":leading,
                "source_exact_leading_coefficient_expression":{
                    "operation":"a_star_value_cubed_over_v123_cubed_u272_fourth",
                    "a_star_evaluation_source":self.refs["original_a_selection"],
                    "v123_source":self.refs["complete_standardizing_space"],
                    "u272_source":self.chi_anchor_ref,
                    "no_nontrivial_unit_normalization_suppressed":True},
                "Galois_norm_identity":{
                    "degree":7,"automorphism_source":"original R849 whole-function sigma action",
                    "principal_factor":"N_sigma(Q_f)",
                    "identity":"sum_sigma(E_f^sigma)-8442P0=7(D_C-H)+3sum_sigma(Dstar^sigma-H)+28(D_chi-H)+div(N_sigma(Q_f))",
                    "fixed_divisors":["C","H","P0","D_C","D_chi"],
                    "remaining_six_b_branches_each_A_and_B_RHS":12,
                    "remaining_Galois_input_arithmetic_completed":False},
                "original_five_eta_nodes":{
                    str(j):self.global_DAG["five_original_polar_and_eta_outputs"][str(j)]["eta_degree_zero_fractional_ideal"]
                    for j in range(1,6)},
                "complete_original_Dstar_space_certified":True,
                "complete_original_common_cusp_space_certified":True,
                "original_D_and_Ey_not_replaced_without_explicit_principal_factor":True,
                "all_original_scale_and_Hom_normalizations_preserved":True,
                "five_original_Lj_RR128_computed":False,
                "five_original_Lj_weight_one_144_complements_computed":False,
                "original_t_frame_calibration_computed":False,
                "original_t_equals_actual_local_parameter_asserted":False,
                "original_theta_rigidification_or_non_p_terms_changed":False,
                "connection_Poincare_period_or_height_computed":False}
            self.put(name,output);old=self.old(name)
        assert old["source_complete_Dstar_418_space"]==self.refs["complete_Dstar_kernel"]
        assert old["source_complete_D_C_418_space"]==self.refs["complete_common_cusp_kernel"]
        assert old["Q_f_order_in_actual_local_parameter"]==-1457
        self.refs["principal_inputs"]=self.ref(name)
        self.checkpoint("complete_bounded_original_inputs")
        return self.refs["principal_inputs"]

    def run(self):
        self.prepare()
        self.normal_matrix()
        self.V3_jets()
        self.common_cusp()
        self.residual_F_space()
        self.standardizing_space()
        v,vref=self.anchor("v")
        for trial in range(1,self.maximum_trials+1):
            self.budget()
            if self.new_trial(trial,v,vref):
                self.principal_inputs()
                return self.finish(True,None)
        raise SearchStop("No complete rank962 pencil among the retained finite candidate schedule")

    def inventory(self):
        entries=[]
        current=self.path("current").name;inventory=self.path("exact-stages-manifest").name
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name in (current,inventory):
                continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag
            if value["complete"] is True:
                entries.append(spec(path))
            else:
                raise AssertionError("Only the named current checkpoint may be incomplete: "+path.name)
        save(self.path("exact-stages-manifest"),{
            "result":RESULT,"configuration":self.tag,"complete":True,"files":entries,
            "all_complete_mathematical_stages_retained":True,
            "current_checkpoint_not_in_complete_inventory":True})
        return self.ref("exact-stages-manifest")

    def finish(self,complete,reason):
        final={
            "result":RESULT,"configuration":self.tag,"complete":bool(complete),
            "p":41,"prime":PRIME,"original_branch":0,
            "original_integral_B_root":ROOT_B,"original_zeta_root":ROOT_ZETA,"original_s_root":ROOT_S,
            "source_identities":{label:source_identity(self.item["sources"][label]) for label in SOURCES},
            "source_audit":self.refs.get("source_audit"),
            "original_V3_point_jets":self.refs.get("V3_jets"),
            "common_cusp_constraint_matrix":self.refs.get("common_cusp_matrix"),
            "complete_common_cusp_418_kernel":self.refs.get("complete_common_cusp_kernel"),
            "original_a_selection":self.refs.get("original_a_selection"),
            "original_269_relation_kernel":self.refs.get("old_complete_269_relation_kernel"),
            "complete_residual_F_269_space":self.refs.get("complete_residual_F_space"),
            "complete_standardizing_146_space":self.refs.get("complete_standardizing_space"),
            "fixed_v":self.refs.get("fixed_v"),"accepted_w":self.refs.get("accepted_w"),
            "accepted_new_pencil_profile":self.refs.get("accepted_new_pencil_profile"),
            "complete_Dstar_418_kernel":self.refs.get("complete_Dstar_kernel"),
            "original_D_cusp_chi_principal_inputs":self.refs.get("principal_inputs"),
            "actual_complete_common_cusp_418_space_certified":bool(self.refs.get("complete_common_cusp_kernel")),
            "actual_complete_residual_F_269_space_certified":bool(self.refs.get("complete_residual_F_space")),
            "actual_complete_standardizing_146_space_certified":bool(self.refs.get("complete_standardizing_space")),
            "actual_complete_Dstar_418_space_certified":bool(self.refs.get("complete_Dstar_kernel")),
            "actual_original_Qf_principal_identity_certified":bool(self.refs.get("principal_inputs")),
            "accepted_trial":self.accepted_trial,"actual_new_pencil_rank":self.actual_rank,
            "source_characteristic_zero_objects_are_exact_unit_solve_expressions":True,
            "characteristic_zero_RR_coefficients_reconstructed":False,
            "old_products_normal_conversion_Hensel_jets_or_Krylov_inverses_recomputed":False,
            "five_original_Lj_RR128_computed":False,
            "five_original_Lj_weight_one_144_complements_computed":False,
            "remaining_six_b_branches_A_B_computed":False,
            "original_t_frame_calibration_computed":False,
            "connection_Poincare_period_or_height_computed":False,
            "stop_reason":reason,"stage_manifest":self.inventory(),
            "resume_state":self.current,"seconds":time.monotonic()-self.started}
        if complete:
            assert final["actual_complete_common_cusp_418_space_certified"]
            assert final["actual_complete_Dstar_418_space_certified"]
            assert final["actual_original_Qf_principal_identity_certified"]
            assert final["actual_new_pencil_rank"]==962
        save(self.out/FINAL,final)
        return final


def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or \
       os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise SystemExit("R880 arithmetic runs only in the authorized public repository Actions")
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    parser.add_argument("--config",required=True)
    parser.add_argument("--out",required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args()
    started=time.monotonic();job=None;final=None;code=0;error=None
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    try:
        job=Job(args)
        if (out/FINAL).exists():
            existing=read(out/FINAL)
            assert existing["configuration"]==job.tag and existing["result"]==RESULT
            if existing["complete"] is True:
                for entry in read(bound(out,existing["stage_manifest"]))["files"]:
                    bound(out,entry)
                final=existing
            else:
                final=job.run()
        else:
            final=job.run()
    except BudgetStop as exc:
        code=124;error=str(exc)
    except (UnitFailure,SearchStop) as exc:
        code=2;error=str(exc)
    except Exception as exc:
        code=1;error=str(exc);traceback.print_exc()
    if final is None and job is not None:
        try:
            final=job.finish(False,error)
        except Exception:
            traceback.print_exc()
    receipt={
        "result":RESULT,"source_sha256":sha(__file__),
        "complete":bool(final and final["complete"]),
        "configuration_sha256":fingerprint(job.tag) if job is not None else None,
        "certificate_sha256":sha(out/FINAL) if final is not None else None,
        "actual_complete_common_cusp_418_space_certified":bool(final and final["actual_complete_common_cusp_418_space_certified"]),
        "actual_complete_Dstar_418_space_certified":bool(final and final["actual_complete_Dstar_418_space_certified"]),
        "actual_original_Qf_principal_identity_certified":bool(final and final["actual_original_Qf_principal_identity_certified"]),
        "actual_new_pencil_rank":final.get("actual_new_pencil_rank") if final else None,
        "five_original_Lj_RR128_computed":False,
        "five_original_Lj_weight_one_144_complements_computed":False,
        "old_mathematical_arithmetic_repeated":False,
        "exit_code":code,"error":error,"seconds":time.monotonic()-started}
    save(out/"core-receipt.json",receipt)
    print("R880_CORE_SUMMARY="+json.dumps(receipt,sort_keys=True),flush=True)
    return code

if __name__=="__main__":
    raise SystemExit(main())
