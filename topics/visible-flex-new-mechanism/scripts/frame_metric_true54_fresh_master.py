#!/usr/bin/env python3
"""Strictly increasing original-row exchange problems at the newly constructed true54 model."""
from __future__ import annotations
import copy
import time
import numpy as np
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_metric_true54_fresh_input import (
    assemble_fresh_master,finite_candidate,vector_record)
from frame_metric_true54_fresh_core import (
    Fresh54FiniteLedger,solve_fresh_master)
from frame_metric_true54_fresh_scope import POLICY,require


class Fresh54Master:
    def __init__(self,model,ledger):
        self.ledger=ledger
        self.data=assemble_fresh_master(model,ledger)
        self.original_receipt=copy.deepcopy(self.data["receipt"])
        self.original_A=self.data["A"]
        self.original_b=self.data["b"]
        self.original_tol=self.data["row_tol"]
        self.original_kind=list(self.data["row_kind"])
        self.known={(row["grid"],row["flat_row_id"])
                    for row in model["original_domain"]["selected_metric_original_row_tags"]}
        self.known.update((row["original_row"]["grid"],row["original_row"]["flat_row_id"])
                         for row in model["additional_metric_gradients_not_already_in_selected_J"])
        self.extra=[]
        self.extra_A=[]
        self.extra_b=[]
        self.problems=[]
        self.last_finite_x=self.data["initial_x"].copy()
        self.last_result=None
        self.last_candidate=None
        self.seed_tags=copy.deepcopy(model["seed_original_metric_tags_from_closed_source"])
        self.seed_count=len(model["additional_metric_gradients_not_already_in_selected_J"])
        require(len(self.seed_tags)==19 and self.seed_count<=19,
                "all nineteen original tag-only seeds were refreshed at54")
    def add(self,row,*,source):
        self.ledger.check()
        key=(row["grid"],row["flat_row_id"])
        if key in self.known:
            return False
        g=np.asarray(row["gradient159"],dtype=np.float64)
        require(g.shape==(159,) and np.all(np.isfinite(g))
                and array_digest(g)==row["gradient_sha256"],
                "one complete original physical159 gradient is required")
        base=float(row["base_phi"])
        require(np.isfinite(base) and row["original_row"]["grid"]==key[0]
                and row["original_row"]["flat_row_id"]==key[1],
                "same original row/branch identity required")
        self.extra_A.append(np.r_[g*self.data["step"],self.data["mu"],self.data["radius"]])
        self.extra_b.append(self.data["phi0"]-base)
        self.extra.append({"grid":key[0],"flat_row_id":key[1],
                          "original_row":copy.deepcopy(row["original_row"]),
                          "gradient_sha256":row["gradient_sha256"],"base_phi":base,
                          "source":source})
        self.known.add(key)
        return True
    def assemble(self):
        self.ledger.check()
        require(len(self.extra)+self.seed_count>=0,"nonnegative fresh original row count")
        d=dict(self.data)
        d.update(A=(np.vstack((self.original_A,np.asarray(self.extra_A)))
                    if self.extra_A else self.original_A.copy()),
                 b=np.r_[self.original_b,np.asarray(self.extra_b)],
                 row_tol=np.r_[self.original_tol,np.full(len(self.extra),1e-9)],
                 row_kind=self.original_kind+["metric"]*len(self.extra),
                 initial_x=self.last_finite_x.copy())
        binding={"source_model_binding_sha256":self.original_receipt["source_model_binding_sha256"],
                 "original_fresh54_rows_A_sha256":self.original_receipt["A_sha256"],
                 "original_fresh54_rows_b_sha256":self.original_receipt["b_sha256"],
                 "additional_rows":copy.deepcopy(self.extra),
                 "A_sha256":array_digest(d["A"]),"b_sha256":array_digest(d["b"]),
                 "row_tol_sha256":array_digest(d["row_tol"]),
                 "row_count":len(d["b"])}
        return d,binding,digest(binding)
    def solve(self,*,emit):
        d,binding,key=self.assemble()
        local=Fresh54FiniteLedger(self.ledger,problem_binding=key,
                                   added_row_count=self.seed_count+len(self.extra))
        result=solve_fresh_master(
            d["A"],d["b"],d["row_tol"],d["row_kind"],
            d["outer_lo"],d["outer_hi"],d["initial_x"],ledger=local)
        local.finish(result)
        self.last_result=result
        if result.get("last_finite_x") is not None:
            self.last_finite_x=np.asarray(result["last_finite_x"],dtype=np.float64).copy()
        candidate=finite_candidate(d,result.get("last_finite_x"))
        self.last_candidate=candidate
        result["problem_binding"]=binding
        result["problem_binding_sha256"]=key
        result["new_augmented_problem_number"]=len(self.problems)+1
        result["candidate"]=candidate
        receipt=emit("FINITE_RESULT",result)
        summary={
            "number":len(self.problems)+1,"problem_binding_sha256":key,
            "original_row_count":len(d["b"]),"additional_row_count":len(self.extra),
            "solver_status":result["status"],"last_summary":copy.deepcopy(result.get("last_summary")),
            "terminal":copy.deepcopy(result.get("terminal")),
            "per_problem_account":local.report(),"original_result_receipt":receipt,
            "finite_candidate":copy.deepcopy(candidate)}
        self.problems.append(summary)
        self.ledger.check()
        return result,candidate,summary
    def report(self):
        return {"schema":POLICY+"-augmented-finite-problems",
                "original_paid_model_assembly":copy.deepcopy(self.original_receipt),
                "seed_original_rows":copy.deepcopy(self.seed_tags),
                "refreshed_seed_rows_outside_current_selected_J":self.seed_count,
                "additional_original_rows":copy.deepcopy(self.extra),
                "attempted_problems":copy.deepcopy(self.problems),
                "last_finite_candidate":copy.deepcopy(self.last_candidate),
                "last_finite_x":vector_record(self.last_finite_x),
                "same_original_domain_and_objective_in_every_new_problem":True,
                "every_problem_uses_new54_hard_and_soft_derivatives":True,
                "strictly_new_row_set_before_each_subsequent_problem":True,
                "no_source_finite_solve_or_old_direction_replayed":True}

def exchange_directions(master,jets,domain,ledger,*,emit,compact_scan,progress):
    require(isinstance(progress,dict) and not progress,"fresh exchange progress required")
    progress.update(schema=POLICY+"-full-grid-exchange",
                    status="started",rounds=[],new_gradient_records=[],
                    source_accepted_index=54)
    handle=last_scan=None
    for number in range(1,33):
        ledger.check()
        result,candidate,finite=master.solve(emit=emit)
        item={"number":number,"finite_problem_binding_sha256":
                finite["problem_binding_sha256"],
              "finite_result_receipt":finite["original_result_receipt"]}
        progress["rounds"].append(item)
        if candidate is None or not candidate["finite_positive_primal"]:
            item["status"]="no-observed-original-domain-positive-finite-primal"
            progress["status"]=item["status"]
            break
        rounded=domain.rounded_direction(candidate)
        item["rounded_original_domain"]=copy.deepcopy(rounded["preliminary_original_domain"])
        if not rounded["preliminary_original_domain"]["eligible"]:
            item["status"]="original-rounded-domain-rejected-before-JVP"
            progress["status"]=item["status"]
            break
        last_scan=jets.scan(rounded["direction"],phase="new-augmented-problem-"+str(number))
        handle=domain.finish_direction(rounded,last_scan)
        record=compact_scan(last_scan)
        record["qualification"]=copy.deepcopy(handle["report"])
        record["new_augmented_problem_number"]=number
        item["full_grid_scan_receipt"]=emit("FULL_GRID_SCAN",record)
        item["qualification"]=copy.deepcopy(handle["report"])
        if handle["qualified"]:
            item["status"]="new-augmented-complete-grid-direction-qualified"
            progress["status"]=item["status"]
            progress["selected_round"]=number
            break
        added=[]
        seen=set()
        for row in last_scan["branches"]:
            key=(row["grid"],row["flat_row_id"])
            if key in seen or key in master.known:
                continue
            seen.add(key)
            gradient=jets.attainer_gradient(row["grid"],row["flat_row_id"],scan=last_scan)
            if master.add(gradient,source="new-complete-grid-attainer-round-"+str(number)):
                receipt=emit("ATTAINER_GRADIENT",gradient)
                progress["new_gradient_records"].append(
                    {"row":copy.deepcopy(gradient),"original_record_receipt":receipt})
                added.append({"grid":key[0],"flat_row_id":key[1],
                              "gradient_sha256":gradient["gradient_sha256"],
                              "original_record_receipt":receipt})
        item["new_rows_before_next_problem"]=added
        item["status"]="new-original-attainers-added" if added else "unqualified-no-new-original-row"
        if not added:
            progress["status"]="unqualified-no-new-original-row-no-identical-problem-retry"
            break
    else:
        progress["status"]="declared32-new-problem-exchange-scope-completed"
    progress["final_direction_qualified"]=bool(handle is not None and handle["qualified"])
    progress["all_new_cuts_retained_in_original_stdout"]=True
    progress["finite_or_exchange_stop_is_not_infeasibility_or_stationarity"]=True
    return handle,last_scan
