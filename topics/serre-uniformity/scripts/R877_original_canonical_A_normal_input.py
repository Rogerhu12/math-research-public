#!/usr/bin/env python3
"""R877: one new canonical A right hand side in the original S5 normal basis.
The completed B conversion, S5 matrix and selected modular inverse are inputs.
All new mathematics is restricted to this repository's public GitHub Actions.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time
import traceback

RESULT = "R877-original-canonical-A-normal-input"
FINAL = "p41-original-canonical-A-normal-input-certificate.json"
PREFIX = "R877-"
PRIME, DIM, ROWS, RANK = 1000000753, 1234, 1380, 272
EPS = [0]+[1]*144+[2]*127
SOURCES = ("R827","R842","R787","R849")
PROOFS = ("R872","GP")
BASE = ("result","run_id","source_commit","core_sha256","manifest_sha256")
STRATEGY = {
    "scope":"one_original_canonical_A_normal_right_hand_side",
    "prime":PRIME,"original_branch":0,"canonical_free_column":1186,
    "source_A":"same characteristic-zero U.1 unit-chart solution as R849",
    "source_B":"completed R827 normal vector, read without recomputation",
    "S5_matrix":"completed R842 original 1380 by 1234 matrix",
    "S5_inverse":"completed R827 prime753 selected inverse",
    "original_V5_prefix_blocks":69,"real_coordinates_per_block":20,
    "new_rhs_count":1,"source_column_chunk_size":64,
    "old_original_Fourier_rows_recomputed":False,
    "old_S5_matrix_reduced_again":False,
    "old_S5_inverse_or_determinant_recomputed":False,
    "old_B_normal_conversion_recomputed":False,
    "original_scale_applied_again":False,
    "exact_coordinate_definition":"solve original S5 selected rows against original F69*A_U1",
    "finite_image_verified_in_all1380_original_coordinates":True,
    "normal_polynomial_bound":"5+0-epsilon_output",
    "characteristic_zero_A_coefficients_reconstructed":False,
    "characteristic_zero_normal_coordinates_reconstructed":False,
    "Galois_conjugate_normal_inputs_computed":False,
    "original_five_Lj_RR_spaces_computed":False,
    "only_budget_and_transport_excluded_from_identity":True,
}

class BudgetStop(RuntimeError):
    pass

def sha(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(4*1024*1024),b""):
            value.update(block)
    return value.hexdigest()

def read(path):
    path = Path(path)
    with (gzip.open(path,"rt",encoding="utf-8") if path.suffix==".gz"
          else path.open("r",encoding="utf-8")) as stream:
        return json.load(stream)

def save(path,value):
    path = Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    if path.suffix==".gz":
        with temporary.open("wb") as raw:
            with gzip.GzipFile(filename="",mode="wb",fileobj=raw,mtime=0,compresslevel=2) as stream:
                stream.write((json.dumps(value,sort_keys=True,separators=(",",":"))+"\n").encode())
    else:
        temporary.write_text(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n",encoding="utf-8")
    temporary.replace(path)

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def plain(value):
    answer = {key:value[key] for key in ("file","bytes","sha256")}
    assert Path(answer["file"]).name==answer["file"] and "\\" not in answer["file"]
    assert isinstance(answer["bytes"],int) and answer["bytes"]>=0
    assert re.fullmatch(r"[0-9a-f]{64}",answer["sha256"])
    return answer

def spec(path):
    path = Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}

def bound(directory,value):
    value=plain(value);path=Path(directory)/value["file"]
    assert spec(path)==value,path.name
    return path

def identity(value):
    return {key:value[key] for key in BASE}

def stable_source(value):
    return {**identity(value),
        "certificate":plain(value["certificate"]) if value.get("certificate") else None,
        "configuration_stage":plain(value["configuration_stage"]) if value.get("configuration_stage") else None,
        "configuration_sha256":value["configuration_sha256"],
        "selected_file_count":value["selected_file_count"],
        "selected_files_sha256":value["selected_files_sha256"]}

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
        "method_sha256":item["method_sha256"],
        "proofs_sha256":{key:item["proofs"][key]["sha256"] for key in PROOFS},
        "sources":{label:stable_source(item["sources"][label]) for label in SOURCES},
        "inputs":item["inputs"],"normal_basis_degrees":EPS,"strategy":STRATEGY}

def matrix_rows(matrix):
    return [[int(matrix[i,j]) for j in range(matrix.ncols())] for i in range(matrix.nrows())]

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
            assert label in ("R827","R787")
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
        self.mat=flint.nmod_mat
        self.args,self.started=args,time.monotonic()
        self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41
        assert self.item["producer_inputs_pending"] is False
        assert sha(__file__)==self.item["core_sha256"]
        assert sha(self.item["method"])==self.item["method_sha256"]
        assert set(self.item["proofs"])==set(PROOFS)
        for value in self.item["proofs"].values():
            assert sha(value["path"])==value["sha256"]
        assert set(self.item["sources"])==set(SOURCES)
        assert set(self.item["inputs"])=={
            "canonical_coefficients","B_normal","S5_inverse","S5_matrix",
            "global_DAG","place_audit","original_chart","original_rational_blocks"}
        self.tag=expected_tag(self.item)
        self.out=args.out;self.out.mkdir(parents=True,exist_ok=True)
        self.sources={}
        self.status="initializing";self.next_column=0
        self.audit_spec=self.rhs_spec=self.normal_spec=self.pair_spec=None

    def budget(self):
        if time.monotonic()-self.started>=60*self.args.budget_minutes-30:
            raise BudgetStop("Retained completed source-bound stages; stage="+self.status)

    def path(self,name):
        assert name.startswith(PREFIX) and Path(name).name==name
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
        assert not any(key in value for key in ("result","configuration","complete"))
        existing=self.old(name)
        if existing is not None:
            return existing
        value={**value,"result":RESULT,"configuration":self.tag,"complete":True}
        save(self.path(name),value)
        print(json.dumps({"stage":name,"seconds":time.monotonic()-self.started}),flush=True)
        return value

    def source_input(self,key):
        entry=self.item["inputs"][key]
        assert entry["source_group"] in SOURCES
        return self.sources[entry["source_group"]].stage(entry)

    def prepare(self):
        self.status="source audit"
        self.sources={label:Source(label,self.item["sources"][label]) for label in SOURCES}
        self.canonical=self.source_input("canonical_coefficients")
        self.Bdata=self.source_input("B_normal")
        self.inverse=self.source_input("S5_inverse")
        self.S5data=self.source_input("S5_matrix")
        self.global_graph=self.source_input("global_DAG")
        self.place=self.source_input("place_audit")
        self.chart=self.source_input("original_chart")
        self.blocks=self.source_input("original_rational_blocks")
        self.r827,self.r842,self.r787,self.r849=(self.sources[x] for x in SOURCES)
        assert self.r849.certificate["global_y_exact_unit_expression_defined"] is True
        assert plain(self.r849.certificate["exact_expression_DAG"])==plain(self.item["inputs"]["global_DAG"])
        for key in ("same_original_reserved_normalization_verified",
                    "abstract_original_p_integral_lift_certified_by_unit_minor_and_rank_bound"):
            assert self.canonical[key] is True
        assert self.canonical["characteristic_zero_coefficients_reconstructed"] is False
        assert self.canonical["prime"]==self.Bdata["prime"]==self.place["prime"]==PRIME
        assert self.canonical["original_branch"]==self.Bdata["original_branch"]==self.place["original_branch"]==0
        assert self.canonical["canonical_free_column"]==self.Bdata["canonical_free_column"]==self.place["canonical_free_column"]==1186
        assert plain(self.place["canonical_B_expansion"])==plain(self.item["inputs"]["canonical_coefficients"])
        assert self.place["genuine_DVR_lift_source_not_an_arbitrary_modular_kernel_candidate"] is True
        assert self.place["original_lambda_is_a_unit"] is True
        assert self.place["original_zeta_root"]==self.canonical["original_zeta_root"]==549966761
        assert self.place["original_s_root"]==self.canonical["original_s_root"]==99932770
        assert identity(self.r827.tag["source_identities"]["R787"])==identity(self.r787.value)
        assert identity(self.r849.tag["source_identities"]["R787"])==identity(self.r787.value)
        assert identity(self.r849.tag["source_identities"]["R809"])==identity(self.r827.tag["source_identities"]["R809"])
        assert plain(self.canonical["source_original_chart"])==plain(self.item["inputs"]["original_chart"])
        assert plain(self.canonical["source_original_rational_blocks"])==plain(self.item["inputs"]["original_rational_blocks"])
        assert self.chart["chosen_free_column"]==1186 and self.chart["actual_modular_rank"]==1186
        assert self.chart["other_free_columns_set_to_zero"] is True
        assert self.blocks["exact_E0_Z_zero_verified"] is True
        assert self.r787.tag["basis_dimension"]==DIM
        scale=self.r787.tag["basis_integer_scale"]
        assert scale==self.canonical["original_V5_integer_scale"]==self.S5data["original_integer_scale"]=="13744803133596058624"
        assert plain(self.Bdata["source_original_B_expansion"])==plain(self.item["inputs"]["canonical_coefficients"])
        assert self.Bdata["abstract_p_integral_original_normal_lift_certified"] is True
        assert self.Bdata["all1380_original_short_coordinates_verified"] is True
        assert self.Bdata["same_original_82power10_scales_preserved"] is True
        assert self.Bdata["normal_basis_rank"]==RANK and self.Bdata["normal_basis_degrees"]==EPS
        assert self.Bdata["regular_degree_bound"]==5
        assert plain(self.Bdata["source_actual_unit_minor"])==plain(self.item["inputs"]["S5_inverse"])
        assert self.inverse["prime"]==self.S5data["prime"]==PRIME
        assert self.inverse["both_inverse_products_verified"] is True
        assert self.inverse["actual_determinant_mod_prime"]!=0
        assert self.inverse["column_indices"]==list(range(DIM))
        assert plain(self.S5data["source_completed_inverse"])==plain(self.item["inputs"]["S5_inverse"])
        assert plain(self.S5data["source_S5_index"])==plain(self.Bdata["source_S5_index"])==plain(self.inverse["S5_basis_index"])
        assert self.S5data["matrix_shape"]==[ROWS,DIM]
        self.mapping=[[i,j] for i in range(RANK) for j in range(6-EPS[i])]
        assert len(self.mapping)==DIM and self.S5data["normal_basis_row_mapping"]==self.mapping
        assert [plain(x) for x in self.S5data["source_original_S5_rows"]]==[plain(x) for x in self.Bdata["source_S5_rows"]]
        self.original_rows=self.Bdata["source_original_V5_rows"]
        assert len(self.original_rows)==DIM
        for i,entry in enumerate(self.original_rows):
            assert entry["producer"]=="R787"
            assert entry["file"]=="R787-real-power5-row-"+str(i).zfill(4)+".json.gz"
            assert self.r787.files[entry["file"]]==plain(entry)
        nodes={value["id"]:value for value in self.global_graph["graph_nodes"]}
        assert len(nodes)==len(self.global_graph["graph_nodes"])
        unit=self.global_graph["global_unit_chart_nodes"]
        fnode=nodes[unit["F"]]
        assert fnode["operation"]=="original_power5_real_coefficient_matrix"
        assert fnode["data"]["original_integer_scale"]==scale
        assert [plain(x) for x in fnode["data"]["sources"]]==[plain(x) for x in self.original_rows]
        assert nodes[unit["A_coefficients"]]["operation"]=="vector_slice"
        assert nodes[unit["A_coefficients"]]["data"]["first"]==0
        assert nodes[unit["A_coefficients"]]["data"]["stop"]==DIM
        assert nodes[unit["A_coefficients"]]["inputs"]==[unit["solution"]]
        assert nodes[unit["solution"]]["operation"]=="unit_matrix_solve"
        fill=nodes[unit["C_coefficients"]]
        assert fill["operation"]=="fill_original_free_and_pivot_coordinates"
        assert fill["data"]["pivot_columns"]==self.chart["pivot_columns"]
        assert fill["data"]["free_values"]["1186"]==1
        assert all(int(value)==int(key=="1186") for key,value in fill["data"]["free_values"].items())
        unit_proof=self.global_graph["nonzero_proof_obligations"]["original_unit_chart"]
        assert any(plain(x)==plain(self.item["inputs"]["original_chart"]) for x in unit_proof["sources"])
        assert self.global_graph["global_y_exact_unit_expression_defined"] is True
        self.A=[int(x) for x in self.canonical["A_coefficients_mod_prime_in_original_V5_basis"]]
        assert len(self.A)==DIM and all(0<=x<PRIME for x in self.A)
        self.I=list(self.inverse["row_indices"])
        assert len(self.I)==len(set(self.I))==DIM and all(0<=i<ROWS for i in self.I)
        assert len(self.inverse["inverse_mod_prime"])==DIM
        assert all(len(row)==DIM for row in self.inverse["inverse_mod_prime"])
        assert len(self.S5data["columns_mod_prime"])==DIM
        assert all(len(row)==ROWS for row in self.S5data["columns_mod_prime"])
        self.S5=self.mat(self.S5data["columns_mod_prime"],PRIME).transpose()
        self.U=self.mat(self.inverse["inverse_mod_prime"],PRIME)
        audit=self.put(PREFIX+"original-source-audit",{
            "prime":PRIME,"original_branch":0,"canonical_free_column":1186,
            "source_original_A_coefficients":self.item["inputs"]["canonical_coefficients"],
            "source_original_B_normal":self.item["inputs"]["B_normal"],
            "source_original_S5_matrix":self.item["inputs"]["S5_matrix"],
            "source_original_S5_inverse":self.item["inputs"]["S5_inverse"],
            "source_original_global_DAG":self.item["inputs"]["global_DAG"],
            "source_original_unit_chart":self.item["inputs"]["original_chart"],
            "source_original_rational_blocks":self.item["inputs"]["original_rational_blocks"],
            "source_original_field":self.global_graph["original_field"],
            "source_original_A_coefficient_node":unit["A_coefficients"],
            "source_original_normal_A_function_node":self.global_graph["global_function_nodes"]["A_over_tau5"],
            "source_original_normal_B_function_node":self.global_graph["global_function_nodes"]["B_over_tau5"],
            "source_original_global_y_node":self.global_graph["global_function_nodes"]["original_y"],
            "original_real_V5_rows":self.original_rows,
            "same_full_original_U1_free1186_solution_certified":True,
            "same_original_F69_rows_and_S5_basis_certified":True,
            "original_82power10_scale":scale,
            "old_S5_matrix_inverse_and_B_conversion_recomputed":False,
            "exact_selected_S5_row_set_may_differ_from_R849_but_same_complete_basis":True})
        self.audit_spec=spec(self.path(PREFIX+"original-source-audit"))
        return audit

    def prefix_rhs(self):
        name=PREFIX+"new-A-full1380-right-hand-side"
        old=self.old(name)
        if old is not None:
            assert old["source_audit"]==self.audit_spec
            self.rhs_spec=spec(self.path(name))
            return [int(x) for x in old["rhs_mod_prime"]]
        groups=[]
        for first in range(0,DIM,64):
            self.next_column=first;stop=min(DIM,first+64)
            chunkname=PREFIX+"original-V5-prefix-and-A-part-"+str(first).zfill(4)+"-"+str(stop).zfill(4)
            self.status=chunkname
            old=self.old(chunkname)
            if old is None:
                self.budget()
                columns=[]
                for i in range(first,stop):
                    value=self.r787.stage(self.original_rows[i])
                    assert value["index"]==i and value["all_original_phase_involutions_verified"] is True
                    coefficients=value["integer_t_coefficients"]
                    assert len(coefficients)==129 and all(len(row)==20 for row in coefficients)
                    columns.append([int(x)%PRIME for row in coefficients[:69] for x in row])
                matrix=self.mat(columns,PRIME).transpose()
                vector=self.mat([[x] for x in self.A[first:stop]],PRIME)
                product=matrix*vector
                old=self.put(chunkname,{
                    "source_audit":self.audit_spec,"prime":PRIME,"first_column":first,"stop_column":stop,
                    "source_original_V5_rows":self.original_rows[first:stop],
                    "source_original_A_coefficients":self.item["inputs"]["canonical_coefficients"],
                    "original_prefix_coordinate_order":"v^n*t^r, n0..68,r0..19",
                    "old_integer_coefficients_only_reduced_for_new_RHS":True,
                    "original_prefix_columns_mod_prime":columns,
                    "partial_A_rhs_mod_prime":[int(product[i,0]) for i in range(ROWS)],
                    "source_original_A_coefficient_slice":self.A[first:stop],
                    "any_B_rhs_or_old_inverse_recomputed":False})
            assert old["source_audit"]==self.audit_spec
            assert old["first_column"]==first and old["stop_column"]==stop
            assert old["source_original_V5_rows"]==self.original_rows[first:stop]
            assert old["source_original_A_coefficient_slice"]==self.A[first:stop]
            assert len(old["partial_A_rhs_mod_prime"])==ROWS
            groups.append(spec(self.path(chunkname)))
        self.budget()
        total=[0]*ROWS
        for ref in groups:
            value=read(bound(self.out,ref))
            total=[(x+int(y))%PRIME for x,y in zip(total,value["partial_A_rhs_mod_prime"])]
        self.put(name,{"source_audit":self.audit_spec,"source_prefix_groups":groups,
            "prime":PRIME,"new_right_hand_side_count":1,
            "matrix_shape":[ROWS,DIM],"rhs_mod_prime":total,
            "original_constant_block_retained":True,
            "old_B_rhs_or_original_phase_conversion_recomputed":False})
        self.next_column=DIM;self.rhs_spec=spec(self.path(name))
        return total

    def solve(self,rhs):
        name=PREFIX+"canonical-A-normal-vector"
        self.status=name
        old=self.old(name)
        if old is None:
            self.budget()
            target=self.mat([[x] for x in rhs],PRIME)
            selected=self.mat([[rhs[i]] for i in self.I],PRIME)
            solution=self.U*selected
            assert self.S5*solution==target
            normal=[[0]*RANK for _ in range(6)]
            for i,(a,power) in enumerate(self.mapping):
                normal[power][a]=int(solution[i,0])
            for power in range(6):
                for a in range(RANK):
                    if power>5-EPS[a]:
                        assert normal[power][a]==0
            exact_definition={
                "operation":"original_S5_selected_unit_solve_for_original_canonical_A",
                "source_original_global_DAG":self.item["inputs"]["global_DAG"],
                "source_original_A_coefficient_node":self.global_graph["global_unit_chart_nodes"]["A_coefficients"],
                "source_original_A_global_function_node":self.global_graph["global_function_nodes"]["A_over_tau5"],
                "source_original_F69_rows":self.original_rows,
                "source_original_S5_rows":self.S5data["source_original_S5_rows"],
                "source_original_S5_index":self.S5data["source_S5_index"],
                "selected_row_indices":self.I,
                "selected_unit_minor_source":self.item["inputs"]["S5_inverse"],
                "formula":"v_A=normal_map(S5[I]^-1*(F69*A_U1)[I]); original A_U1 free1186=1",
                "field":"original L=Q(b,zeta), with original B_field=lambda*b",
                "normal_function":"original A/tau^5",
                "global_exact_membership_reason":"original A is in V5 and original S5 is its complete basis",
                "original_scale_applied_again":False,
                "same_original_A_as_R849_independent_of_selected_S5_row_set":True,
                "characteristic_zero_coefficients_reconstructed":False}
            old=self.put(name,{
                "source_audit":self.audit_spec,"source_rhs":self.rhs_spec,
                "source_completed_inverse":self.item["inputs"]["S5_inverse"],
                "source_completed_S5_matrix":self.item["inputs"]["S5_matrix"],
                "prime":PRIME,"original_branch":0,"canonical_free_column":1186,
                "source_original_zeta_root":self.place["original_zeta_root"],
                "source_original_b_root":self.place["original_b_root"],
                "normal_basis_rank":RANK,"normal_basis_degrees":EPS,
                "regular_degree_bound":5,"normal_basis_row_mapping":self.mapping,
                "S5_coordinates_mod_prime":[int(solution[i,0]) for i in range(DIM)],
                "vector_coefficients_mod_prime":normal,
                "all1380_original_short_coordinates_verified":True,
                "all_weighted_support_bounds_verified":True,
                "original_A_reduction_is_nonzero":any(any(row) for row in normal),
                "same_original_82power10_scales_preserved":True,
                "abstract_p_integral_original_normal_A_lift_certified":True,
                "exact_unit_solve_expression":exact_definition,
                "characteristic_zero_coordinates_reconstructed":False,
                "new_right_hand_side_count":1,
                "old_S5_matrix_inverse_and_B_conversion_recomputed":False})
        assert old["source_rhs"]==self.rhs_spec and old["source_audit"]==self.audit_spec
        assert old["all1380_original_short_coordinates_verified"] is True
        self.normal_spec=spec(self.path(name))
        return old

    def normal_pair(self,normal):
        name=PREFIX+"original-global-y-normal-fraction-input"
        self.status=name
        old=self.old(name)
        if old is None:
            B=self.Bdata["vector_coefficients_mod_prime"]
            assert len(B)==6 and all(len(row)==RANK for row in B)
            assert any(any(int(x) for x in row) for row in B)
            for power in range(6):
                for a in range(RANK):
                    if power>5-EPS[a]:
                        assert int(B[power][a])==0
            old=self.put(name,{
                "source_audit":self.audit_spec,"source_original_global_DAG":self.item["inputs"]["global_DAG"],
                "source_new_A_normal":self.normal_spec,"source_completed_B_normal":self.item["inputs"]["B_normal"],
                "prime":PRIME,"original_branch":0,"canonical_free_column":1186,
                "original_global_y_node":self.global_graph["global_function_nodes"]["original_y"],
                "normal_fraction":"original y=(A/tau^5)/(B/tau^5)",
                "A_exact_function_node":self.global_graph["global_function_nodes"]["A_over_tau5"],
                "B_exact_function_node":self.global_graph["global_function_nodes"]["B_over_tau5"],
                "both_regular_degree_bounds":5,"same_original_U1_normalization_preserved":True,
                "global_characteristic_zero_fraction_defined_and_modular_inputs_certified":True,
                "B_normal_conversion_recomputed":False,
                "finite_fiber_B_invertibility_checked":False,
                "finite_fiber_original_y_values_computed":False,
                "Galois_conjugate_normal_inputs_computed":False,
                "original_Lj_RR128_or_144_computed":False})
        self.pair_spec=spec(self.path(name))
        return old

    def inventory(self):
        entries=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name in (PREFIX+"current.json.gz",) or path.name.startswith(PREFIX+"stage-manifest-"):
                continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag
            assert value["complete"] is True
            entries.append(spec(path))
        name=PREFIX+"stage-manifest-"+fingerprint(entries)[:20]
        self.put(name,{"files":entries})
        return spec(self.path(name))

    def finish(self,complete,error=None):
        self.current={
            "result":RESULT,"configuration":self.tag,"complete":False,
            "status":self.status,"next_original_V5_column":self.next_column,
            "source_audit":self.audit_spec,"full1380_rhs":self.rhs_spec,
            "normal_A":self.normal_spec,"normal_fraction_input":self.pair_spec}
        save(self.path(PREFIX+"current"),self.current)
        final={"result":RESULT,"configuration":self.tag,"complete":complete,"p":41,
            "prime":PRIME,"original_branch":0,"canonical_free_column":1186,
            "new_right_hand_side_count":1 if self.normal_spec else 0,
            "source_audit":self.audit_spec,"full1380_rhs":self.rhs_spec,
            "normal_A":self.normal_spec,"normal_fraction_input":self.pair_spec,
            "canonical_A_normal_input_certified":bool(self.normal_spec),
            "original_global_y_normal_fraction_input_certified":bool(self.pair_spec),
            "all1380_original_short_coordinates_verified":bool(self.normal_spec),
            "old_S5_matrix_inverse_and_B_conversion_recomputed":False,
            "characteristic_zero_normal_coordinates_reconstructed":False,
            "Galois_conjugate_normal_inputs_computed":False,
            "original_five_Lj_RR128_or_144_computed":False,
            "original_connection_rigidification_or_height_computed":False,
            "stage_manifest":self.inventory(),
            "resume_state":spec(self.path(PREFIX+"current")),
            "error":error,"seconds":time.monotonic()-self.started}
        assert not complete or (self.normal_spec is not None and self.pair_spec is not None)
        save(self.out/FINAL,final)
        return final

    def run(self):
        self.prepare()
        final_path=self.out/FINAL
        if final_path.exists():
            prior=read(final_path)
            assert prior["configuration"]==self.tag
            if prior["complete"] is True:
                for key in ("full1380_rhs","normal_A","normal_fraction_input"):
                    bound(self.out,prior[key])
                self.rhs_spec=prior["full1380_rhs"]
                self.normal_spec=prior["normal_A"]
                self.pair_spec=prior["normal_fraction_input"]
                self.next_column=DIM;self.status="complete"
                return self.finish(True)
        rhs=self.prefix_rhs()
        normal=self.solve(rhs)
        self.normal_pair(normal)
        self.status="complete"
        return self.finish(True)

def main():
    sys.set_int_max_str_digits(0)
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public"
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args()
    assert 0<args.budget_minutes<=300
    args.out.mkdir(parents=True,exist_ok=True)
    started=time.monotonic();job=None;final=None;error=None;code=1
    try:
        job=Job(args);final=job.run();code=0
    except BudgetStop as exc:
        error={"type":type(exc).__name__,"message":str(exc)};code=124
        if job is not None:
            final=job.finish(False,error)
    except BaseException as exc:
        error={"type":type(exc).__name__,"message":str(exc)}
        traceback.print_exc()
        if job is not None:
            try:
                final=job.finish(False,error)
            except BaseException:
                traceback.print_exc()
    receipt={"result":RESULT,"source_sha256":sha(__file__),
        "configuration":job.tag if job is not None else None,
        "process_exit_code":code,"complete":bool(final and final["complete"]),
        "certificate_sha256":sha(args.out/FINAL) if final is not None else None,
        "error":error,"seconds":time.monotonic()-started,
        "canonical_A_normal_input_certified":bool(final and final["canonical_A_normal_input_certified"]),
        "original_global_y_normal_fraction_input_certified":bool(final and final["original_global_y_normal_fraction_input_certified"]),
        "original_five_Lj_RR128_or_144_computed":False,
        "original_connection_rigidification_or_height_computed":False}
    save(args.out/"core-receipt.json",receipt)
    print(json.dumps(receipt,sort_keys=True),flush=True)
    raise SystemExit(code)

if __name__=="__main__":
    main()
