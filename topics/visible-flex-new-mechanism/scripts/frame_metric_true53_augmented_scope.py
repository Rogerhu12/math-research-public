#!/usr/bin/env python3
"""One genuinely augmented master: four new paid cuts before the first solve."""
from __future__ import annotations
import copy
import math
import time

POLICY="same159-true53-four-cut-exchange-master-v1"
SOURCE_ACCEPTED_INDEX=53
SOURCE_ORIGINAL_VALUES=128
SOURCE_GLOBAL_SECONDS=1658.9797906909998
CARRIED_SCIENCE_SECONDS=36.79963991600005
CARRIED_FAILED_SOURCE={
    "run_id": "43825241350",
    "job_id": "133157415075",
    "source_commit": "5189a1a78eac6215db75bf5c7d851a8913c6db0f",
    "workflow": ".github/workflows/visible-true53-augmented-master.yml",
    "log_bytes": 3741178,
    "log_sha256": "997e9b9ddaa0ec6ae72f27a94f66895bfe6a1cc51be5850ae204cc4d70566944"
}
CARRIED_FINAL_CLOCK={
    "tag": "FINAL_CLOCK",
    "ordinal": 1,
    "JSON_plus_LF_bytes": 6015,
    "JSON_plus_LF_sha256": "a9648db960caa66e4f2562bbd4af2e32c9cd72cb34cdd69a58625fafafd4ffe9"
}
SOURCE_PHYSICAL_SHA="9ffba0f1400c504343f9b0b8847be7f14745144f66b3cd89dfe698f45d81548e"
SOURCE_CFG_SHA="1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19"
SOURCE_FIELD_SHA="8e77c49888fce6d8abe6b02f2e9a0a7651d4b76ef83328b3d134a2adde697ab1"
LIMITS={
    "science_seconds":600,
    "finite_master_calls":32,
    "finite_master_iterations":3072,
    "finite_master_newton_systems":6144,
    "first_jet_input_restores":1,
    # The first restore failed after producing ephemeral fields only. Its one
    # debit is retained; one explicit repair restores those unavailable fields.
    "first_jet_input_restore_repairs":1,
    "pair_first_jet_jvps":32,
    "new_attainer_gradients":128,
    "scalar_sessions":1,
    "scalar_queries":64,
    "actual_trial_pairs":3,
    "actual_grid_values":6,
    "necessary_base_geometry":0,
}

def require(test,message):
    if not bool(test):
        raise ValueError(message)

class AugmentedDirectionLimit(RuntimeError):
    def __init__(self,kind,used,limit):
        self.kind,self.used,self.limit=kind,used,limit
        self.reason="time_limit" if kind=="science_seconds" else "new_task_counter_limit"
        self.stage=kind
        self.recorded=False
        super().__init__("augmented scope exhausted: %s %s/%s"%(kind,used,limit))

class AugmentedDirectionLedger:
    def __init__(self,started,*,limits=None):
        now=time.monotonic()
        require(type(started) in (int,float) and math.isfinite(started)
                and 0<=started<=now,"real pre-import shared time origin required")
        selected=dict(LIMITS if limits is None else limits)
        require(selected==LIMITS,"one immutable augmented task allocation required")
        self.started=float(started)
        self.limits=selected
        self.counts={k:0 for k in selected if k!="science_seconds"}
        self.counts["first_jet_input_restores"]=1
        self.carried_receipt_verified=False
        self.carried_receipt=None
        self.events=[]
        self.problem_bindings=set()
        self.old_backend_calls={"HiGHS":0,"SOC":0,"cone":0,"Hildreth":0,
                                "old_paid_finite_master":0,"old_positive_direction":0}
        self.check()
    def elapsed(self):
        return CARRIED_SCIENCE_SECONDS+time.monotonic()-self.started
    def bind_carried_failed_attempt(self,clock,receipt):
        require(not self.carried_receipt_verified,"one carried failed attempt only")
        prior=clock["ledger"]
        old_counts={k:0 for k in LIMITS
                    if k not in ("science_seconds","first_jet_input_restore_repairs")}
        old_counts["first_jet_input_restores"]=1
        require(receipt["source"]==CARRIED_FAILED_SOURCE
                and receipt["final_clock_record"]==CARRIED_FINAL_CLOCK
                and clock["status_at_final_emit"]=="new-augmented-input-or-scientific-error"
                and clock["scope_exhausted"] is False
                and prior["scientific_seconds"]==CARRIED_SCIENCE_SECONDS
                and prior["ancestor_scientific_seconds"]==SOURCE_GLOBAL_SECONDS
                and prior["total_ancestor_plus_new_scientific_seconds"]==1695.779430607
                and prior["started_counts"]==old_counts
                and prior["attempted_distinct_finite_problem_bindings"]==[]
                and prior["total_source_plus_new_full_value_debits"]==SOURCE_ORIGINAL_VALUES,
                "the exact failed input account must precede this continuation")
        self.carried_receipt=copy.deepcopy(receipt)
        self.carried_receipt_verified=True
        self.events=copy.deepcopy(prior["events"])+self.events
        for event in self.events:
            event["carried_from_original_failed_source"]=copy.deepcopy(CARRIED_FAILED_SOURCE)
        self.check("carried-failed-input-read")
    def check(self,stage=""):
        value=self.elapsed()
        if not math.isfinite(value) or value>=self.limits["science_seconds"]:
            error=AugmentedDirectionLimit("science_seconds",value,self.limits["science_seconds"])
            error.stage=stage or "shared-clock"
            raise error
        return value
    def charge(self,key,count=1):
        self.check(key)
        require(key in self.counts and type(count) is int and count>0,
                "known counter and positive integer debit required")
        if self.counts[key]+count>self.limits[key]:
            raise AugmentedDirectionLimit(key,self.counts[key]+count,self.limits[key])
        self.counts[key]+=count
        return self.counts[key]
    def begin(self,key,**metadata):
        if key=="first_jet_input_restores":
            require(self.carried_receipt_verified,
                    "read the carried input failure before its explicit repair")
            metadata["original_requested_counter"]=key
            metadata["repair_reason"]="completed coefficient contexts were not emitted before input failure"
            key="first_jet_input_restore_repairs"
        ordinal=self.charge(key)
        event={"counter":key,"ordinal":ordinal,"status":"started",
               "started_scientific_seconds":self.elapsed(),**copy.deepcopy(metadata)}
        event["_started"]=time.monotonic()
        self.events.append(event)
        return event
    def end(self,event,error=None,**metadata):
        tick=event.pop("_started",None)
        if tick is not None:
            event["elapsed_seconds"]=time.monotonic()-tick
        event.update(copy.deepcopy(metadata))
        event["status"]="complete" if error is None else "raised"
        if error is not None:
            event["error"]=copy.deepcopy(error) if isinstance(error,dict) else {
                "type":type(error).__name__,"message":str(error)}
    def claim_problem(self,binding,added_row_count):
        require(self.carried_receipt_verified,"carried source must be read before the first solve")
        require(isinstance(binding,str) and len(binding)==64
                and type(added_row_count) is int and added_row_count>=4,
                "every new finite problem must already contain the four new cuts")
        require(binding not in self.problem_bindings,
                "a previously attempted augmented finite problem is never replayed")
        self.problem_bindings.add(binding)
        return self.begin("finite_master_calls",problem_binding_sha256=binding,
                          additional_original_metric_rows=added_row_count)
    def report(self):
        value=self.elapsed()
        events=copy.deepcopy(self.events)
        for event in events:
            tick=event.pop("_started",None)
            if tick is not None:
                event["elapsed_seconds_so_far"]=time.monotonic()-tick
        return {
            "schema":POLICY+"-ledger","limits":dict(self.limits),
            "started_counts":dict(self.counts),"scientific_seconds":value,
            "current_attempt_scientific_seconds":time.monotonic()-self.started,
            "carried_failed_scientific_seconds":CARRIED_SCIENCE_SECONDS,
            "carried_failed_source":copy.deepcopy(CARRIED_FAILED_SOURCE),
            "carried_final_clock_record":copy.deepcopy(CARRIED_FINAL_CLOCK),
            "carried_failed_source_read_verified":self.carried_receipt_verified,
            "carried_failed_source_receipt":copy.deepcopy(self.carried_receipt),
            "same600_second_total_not_reset_after_input_failure":True,
            "original_restore_debit_retained_and_one_explicit_repair_added":True,
            "ancestor_scientific_seconds":SOURCE_GLOBAL_SECONDS,
            "total_ancestor_plus_new_scientific_seconds":SOURCE_GLOBAL_SECONDS+value,
            "source_original_full_values":SOURCE_ORIGINAL_VALUES,
            "new_actual_value_debits":self.counts["actual_grid_values"],
            "total_source_plus_new_full_value_debits":
                SOURCE_ORIGINAL_VALUES+self.counts["actual_grid_values"],
            "attempted_distinct_finite_problem_bindings":sorted(self.problem_bindings),
            "events":events,"old_backend_calls":dict(self.old_backend_calls),
            "all_imports_inputs_failures_output_and_all_exchange_rounds_share_one_clock":True,
            "event_times_nested_not_added_again":True,
            "old_finite_and_positive_direction_tasks_remain_closed":True,
            "deadline_observed_exceeded":value>=self.limits["science_seconds"],
            "observed_overrun_seconds":max(0.,value-self.limits["science_seconds"])}
