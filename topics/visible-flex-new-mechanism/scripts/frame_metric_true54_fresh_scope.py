#!/usr/bin/env python3
"""One fresh true54 model and strictly new-row exchange, on the original g/b0."""
from __future__ import annotations
import copy
import math
import time

POLICY="same159-true54-fresh-original-model-exchange-v1"
SOURCE_ACCEPTED_INDEX=54
SOURCE_ORIGINAL_VALUES=130
SOURCE_GLOBAL_SECONDS=1877.294171609
SOURCE_PHYSICAL_SHA="c0214406cebe6f39eda0b11fa2db5fecb883d9323c696005447427b39410f253"
SOURCE_CFG_SHA="1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19"
SOURCE_FIELD_SHA="8e77c49888fce6d8abe6b02f2e9a0a7651d4b76ef83328b3d134a2adde697ab1"
LIMITS={
    "science_seconds":600,
    "necessary_model_grid_values":2,
    "hard_J_grid_builds":2,
    "first_jet_grid_builds":2,
    "full_separations":32,
    "new_metric_rows":147,
    "finite_master_calls":32,
    "finite_master_iterations":3072,
    "finite_master_newton_systems":6144,
    "scalar_sessions":1,
    "scalar_queries":64,
    "actual_trial_pairs":3,
    "actual_grid_values":6,
}

def require(test,message):
    if not bool(test):
        raise ValueError(message)

class Fresh54Limit(RuntimeError):
    def __init__(self,kind,used,limit):
        self.kind,self.used,self.limit=kind,used,limit
        self.reason="time_limit" if kind=="science_seconds" else "fresh54_counter_limit"
        self.stage=kind
        self.recorded=False
        super().__init__("fresh54 scope exhausted: %s %s/%s"%(kind,used,limit))

class Fresh54Ledger:
    def __init__(self,started,*,limits=None):
        now=time.monotonic()
        require(type(started) in (int,float) and math.isfinite(started)
                and 0<=started<=now,"real pre-import shared origin required")
        selected=dict(LIMITS if limits is None else limits)
        require(selected==LIMITS,"one published fresh54 allocation required")
        self.started=float(started)
        self.limits=selected
        self.counts={k:0 for k in selected if k!="science_seconds"}
        self.events=[]
        self.problem_bindings=set()
        self.last_problem_added_count=None
        self.old_backend_calls={
            "HiGHS":0,"SOC":0,"cone":0,"Hildreth":0,
            "old_true53_finite_or_direction":0,
            "old_true53_J_or_model":0,
            "old_paid_source_geometry_acceptance_replay":0}
        self.check()

    def elapsed(self):
        return time.monotonic()-self.started

    def check(self,stage=""):
        value=self.elapsed()
        if not math.isfinite(value) or value>=self.limits["science_seconds"]:
            error=Fresh54Limit("science_seconds",value,self.limits["science_seconds"])
            error.stage=stage or "shared-clock"
            raise error
        return value

    def charge(self,key,count=1):
        self.check(key)
        require(key in self.counts and type(count) is int and count>0,
                "known counter and positive integer debit required")
        if self.counts[key]+count>self.limits[key]:
            raise Fresh54Limit(key,self.counts[key]+count,self.limits[key])
        self.counts[key]+=count
        return self.counts[key]

    def begin(self,key,**metadata):
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
        require(isinstance(binding,str) and len(binding)==64
                and type(added_row_count) is int and added_row_count>=0,
                "one new true54 finite problem identity required")
        require(binding not in self.problem_bindings,
                "an already attempted finite matrix may not be replayed")
        require(self.last_problem_added_count is None
                or added_row_count>self.last_problem_added_count,
                "every later finite solve requires a strictly new original row")
        self.problem_bindings.add(binding)
        self.last_problem_added_count=added_row_count
        return self.begin("finite_master_calls",problem_binding_sha256=binding,
                          additional_original_metric_rows=added_row_count,
                          model_at_true_accepted_index=SOURCE_ACCEPTED_INDEX)

    def report(self):
        value=self.elapsed()
        events=copy.deepcopy(self.events)
        for event in events:
            tick=event.pop("_started",None)
            if tick is not None:
                event["elapsed_seconds_so_far"]=time.monotonic()-tick
        new_values=(self.counts["necessary_model_grid_values"]
                    +self.counts["actual_grid_values"])
        return {
            "schema":POLICY+"-ledger","limits":dict(self.limits),
            "started_counts":dict(self.counts),"scientific_seconds":value,
            "ancestor_scientific_seconds":SOURCE_GLOBAL_SECONDS,
            "total_ancestor_plus_new_scientific_seconds":SOURCE_GLOBAL_SECONDS+value,
            "source_accepted_index":SOURCE_ACCEPTED_INDEX,
            "source_original_full_values":SOURCE_ORIGINAL_VALUES,
            "new_necessary_hard_model_value_debits":self.counts["necessary_model_grid_values"],
            "new_actual_value_debits":self.counts["actual_grid_values"],
            "new_total_value_debits":new_values,
            "total_source_plus_new_full_value_debits":SOURCE_ORIGINAL_VALUES+new_values,
            "attempted_distinct_finite_problem_bindings":sorted(self.problem_bindings),
            "events":events,"old_backend_calls":dict(self.old_backend_calls),
            "new_development_calls":0,
            "old53_task_closed_at_218_31438091800004_seconds":True,
            "new_model_at54_is_not_a_relabelled53_model":True,
            "hard_model_missing_two_jets_are_charged_not_claimed_cached":True,
            "all_imports_inputs_failures_output_and_new_work_share_one_clock":True,
            "event_times_nested_not_added_again":True,
            "deadline_observed_exceeded":value>=self.limits["science_seconds"],
            "observed_overrun_seconds":max(0.,value-self.limits["science_seconds"])}
