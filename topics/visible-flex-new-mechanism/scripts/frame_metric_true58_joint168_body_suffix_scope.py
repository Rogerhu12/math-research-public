#!/usr/bin/env python3
"""Remaining account of the same joint168 problem after its pre-solver source error."""
from __future__ import annotations
import copy
import math
import time

POLICY = "true58-joint168-body-suffix-v1"
ORIGINAL_JOINT_SCIENCE_LIMIT_SECONDS = 1800.
PRIOR_JOINT_SCIENCE_SECONDS = 26.784710984000014
REMAINING_JOINT_SCIENCE_SECONDS = 1773.215289016
PRIOR_JOINT_STARTED_COUNTS = {
    "actual_grid_values":0,"actual_trial_pairs":0,
    "joint_body_suffix_model_builds":1,"joint_body_suffix_solver_sessions":0,
    "new_joint_input_preparations":1,"nonlinear_candidate_predictions":0,
    "paid_first_jet_bindings":2,"paid_metric_bindings":1,
}
PRIOR_JOINT_SOURCE = {
    "run_id":"43923038659","job_id":"133495072427",
    "source_commit":"47942fb212bcc2f424fdf546437cd38b08c2d7e1",
    "error_type":"ValueError",
    "error_message":"every original physical172 row has an actual full168 direction",
    "implementation_error_before_solver":True,
}
LIMITS = {
    "science_seconds": REMAINING_JOINT_SCIENCE_SECONDS,
    "paid_metric_bindings": 1,
    "paid_first_jet_bindings": 2,
    "joint_body_suffix_model_builds": 1,
    "new_joint_input_preparations": 1,
    "joint_body_suffix_solver_sessions": 1,
    "nonlinear_candidate_predictions": 1,
    "actual_trial_pairs": 1,
    "actual_grid_values": 2,
}
SOLVER_TIME_LIMIT_SECONDS = 1200.
SOLVER_MAXITER = 240
MAX_COMPLETE_EVALUATIONS = 480
MAX_BACKEND_EVALUATIONS = 960
SOLVER_OPTIONS = {"maxiter":240,"ftol":1.e-9,"disp":False}
K_BOUNDS_EXACT = ("1000/61","58")
INITIAL_K_EXACT = "58"
NORM_REGULARIZATION_EXACT = "1/1000000"
TARGET_EXACT = "1000/61"
INTERNAL_METRIC_MARGIN_EXACT = "1/100000000"
SOURCE_ETA = .26600541463999305
MINIMUM_DECREASE_EXACT = "1/10000000"
FIXED_SUFFIX_LOWER_EXACT = "153/200"
SOURCE_INDEX = 58
NEXT_INDEX = 59
ORIGINAL_CLOSED_FULL62_SECONDS = 3757.97482037
ANCESTOR_SECONDS = 3784.759531354
ANCESTOR_VALUES = 147

def require(condition, message):
    if not bool(condition):
        raise ValueError(message)

class Suffix58Limit(RuntimeError):
    def __init__(self, kind, used, limit, stage=""):
        self.kind, self.used, self.limit, self.stage = kind, used, limit, stage
        super().__init__("joint168 scope %s: %s / %s at %s" % (kind, used, limit, stage))

class Suffix58Ledger:
    """No closed source time, unsuccessful solve or unused budget can be reset."""
    def __init__(self, started_monotonic, *, ancestor_receipt, limits=None):
        now=time.monotonic()
        require(type(started_monotonic) in (int,float)
                and math.isfinite(started_monotonic) and 0<=started_monotonic<=now,
                "real pre-import/pre-input origin required")
        chosen=dict(LIMITS if limits is None else limits)
        require(chosen==LIMITS,"the remaining joint168 implementation-continuation account is frozen")
        require(isinstance(ancestor_receipt,dict)
                and ancestor_receipt.get("source_original_full_values")==ANCESTOR_VALUES
                and ancestor_receipt.get("ancestor_final_original_scientific_seconds")==ANCESTOR_SECONDS,
                "literal closed actual58 ancestor account required")
        self.started=float(started_monotonic)
        self.limits=chosen
        self.ancestor_receipt=copy.deepcopy(ancestor_receipt)
        self.counts={k:0 for k in chosen if k!="science_seconds"}
        self.prior_joint_counts=copy.deepcopy(PRIOR_JOINT_STARTED_COUNTS)
        self.events=[]
        self.check("ledger.entry")
    def elapsed(self):
        return float(time.monotonic()-self.started)
    def check(self,stage=""):
        elapsed=self.elapsed()
        if not math.isfinite(elapsed) or elapsed>=self.limits["science_seconds"]:
            raise Suffix58Limit("science_seconds",elapsed,self.limits["science_seconds"],stage)
        return elapsed
    def charge(self,key,count=1):
        self.check(key)
        require(key in self.counts and type(count) is int and count>0,
                "one declared positive started debit required")
        value=self.counts[key]+count
        if value>self.limits[key]:
            raise Suffix58Limit(key,value,self.limits[key],key)
        self.counts[key]=value
        return value
    def begin(self,key,**metadata):
        ordinal=self.charge(key)
        event={"counter":key,"ordinal":ordinal,"status":"started",
               "started_scientific_seconds":self.elapsed(),"_started":time.monotonic(),
               **copy.deepcopy(metadata)}
        self.events.append(event)
        return event
    def end(self,event,error=None,**metadata):
        require(event in self.events and event.get("status")=="started",
                "each own started event is finished once")
        started=event.pop("_started")
        event.update(copy.deepcopy(metadata))
        event["elapsed_seconds"]=float(time.monotonic()-started)
        event["finished_scientific_seconds"]=self.elapsed()
        event["status"]="complete" if error is None else "raised"
        if error is not None:
            event["error"]={"type":type(error).__name__,"message":str(error)}
    def note(self,stage,**metadata):
        self.events.append({"stage":str(stage),"status":"metadata",
            "scientific_seconds":self.elapsed(),**copy.deepcopy(metadata)})
    def report(self):
        elapsed=self.elapsed()
        events=copy.deepcopy(self.events)
        for event in events:
            started=event.pop("_started",None)
            if started is not None:
                event["elapsed_seconds_so_far"]=float(time.monotonic()-started)
        new_values=self.counts["actual_grid_values"]
        whole_problem_counts={key:self.prior_joint_counts.get(key,0)+value
            for key,value in self.counts.items()}
        return {"schema":POLICY+"-ledger","limits":dict(self.limits),
            "started_counts":dict(self.counts),"scientific_seconds":elapsed,
            "current_attempt_counts_are_not_the_whole_problem_counts":True,
            "prior_joint_attempt_started_counts":copy.deepcopy(self.prior_joint_counts),
            "whole_problem_started_counts":whole_problem_counts,
            "prior_joint_attempt_source":copy.deepcopy(PRIOR_JOINT_SOURCE),
            "prior_joint_attempt_scientific_seconds":PRIOR_JOINT_SCIENCE_SECONDS,
            "whole_problem_scientific_seconds":PRIOR_JOINT_SCIENCE_SECONDS+elapsed,
            "original_whole_problem_science_limit_seconds":ORIGINAL_JOINT_SCIENCE_LIMIT_SECONDS,
            "this_attempt_scientific_allowance_is_only_original_remainder":True,
            "same_mathematical_problem_implementation_continuation":True,
            "prior_attempt_failed_before_any_solver_geometry_J_prediction_or_actual":True,
            "one_new_build_and_prepare_are_attempt_work_not_erasure_of_prior_work":True,
            "original_closed_full62_scientific_seconds":ORIGINAL_CLOSED_FULL62_SECONDS,
            "remaining_scientific_seconds":max(0.,self.limits["science_seconds"]-elapsed),
            "deadline_observed_exceeded":elapsed>=self.limits["science_seconds"],
            "observed_overrun_seconds":max(0.,elapsed-self.limits["science_seconds"]),
            "ancestor_receipt_unchanged":copy.deepcopy(self.ancestor_receipt),
            "ancestor_scientific_seconds":ANCESTOR_SECONDS,
            "source_original_values_closed":ANCESTOR_VALUES,
            "new_actual_values":new_values,"model_point_values_and_derivative_work_counted_in_model_report":True,
            "total_ancestor_plus_new_scientific_seconds":ANCESTOR_SECONDS+elapsed,
            "total_source_plus_new_started_values":ANCESTOR_VALUES+new_values,
            "events":events,
            "all_inputs_imports_failures_serialization_share_this_clock":True,
            "nested_phase_seconds_are_not_added_to_final_clock":True,
            "closed_source57_nonlinear_task_not_reopened":True,
            "closed_original_R2_ring17_task_not_reopened":True,
            "closed_reflection_projection_and_selected_R2_LP_not_reopened":True,
            "closed_joint_reflection_amplitude_R2_task_not_reopened":True,
            "closed_free_R1_R2_ring_solve_not_reopened":True,
            "closed_prefix102_necessity_task_not_reopened":True,
            "closed_whole34_iteration_limited_task_not_reopened":True,
            "closed_full51_clock_limited_task_not_reopened":True,
            "closed_full62_strict_metric_failed_task_not_reopened":True,
            "one_new_joint_body_suffix_solver_no_restart":True,
            "whole_problem_solver_sessions_limit":1,
            "prior_solver_sessions":self.prior_joint_counts["joint_body_suffix_solver_sessions"],
            "first_failed_build_and_all_paid_binding_costs_remain_in_ancestor":True,
            "maximum_distinct_new_point_value_evaluations":480,
            "maximum_distinct_backend170_evaluations":960,
            "new_point_cap_counts":"distinct new actual q168 geometry byte inputs; different backend170 K/h values counted separately with cap960",
            "analytic_Jacobian_evaluations_only_on_initial_scaling_or_actual_backend_request":True,
            "unnecessary_current58_baseline_or_old_J_replays":0,
            "new_development_calls":0,
            "new_full168_body_and_suffix_values_Pi_and_requested_J_are_new_scientific_work":True,
            "model_and_solver_internal_subcalls_are_in_the_same_clock":True,
            "paid_unaccepted_seed_suffix_arrays_are_not_recomputed":True,
            "one_required_initial_shared_body_and_suffix_value_is_at_true58":True,
            "actual14_acceptance_is_distinct_from_ring_LP_or_predictions":True}
