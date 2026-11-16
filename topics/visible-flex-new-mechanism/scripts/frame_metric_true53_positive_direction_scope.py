#!/usr/bin/env python3
"""One new positive-direction task; closed source accounts are never reset."""
from __future__ import annotations
import copy
import math
import time

POLICY = "same159-true53-paid-master-positive-direction-v1"
SOURCE_ACCEPTED_INDEX = 53
SOURCE_ORIGINAL_VALUES = 128
SOURCE_GLOBAL_SECONDS = 1608.573003992
SOURCE_PHYSICAL_SHA = "9ffba0f1400c504343f9b0b8847be7f14745144f66b3cd89dfe698f45d81548e"
SOURCE_CFG_SHA = "1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19"
SOURCE_FIELD_SHA = "8e77c49888fce6d8abe6b02f2e9a0a7651d4b76ef83328b3d134a2adde697ab1"
SOURCE_DIRECTION_SHA = "3fade7f704238c45a9eca095af36035ab10c4741e059d000359cc9d0600f5e09"
LIMITS = {
    "science_seconds": 600,
    "first_jet_input_restores": 1,
    "pair_first_jet_jvps": 2,
    "new_attainer_gradients": 4,
    "scalar_sessions": 1,
    "scalar_queries": 64,
    "actual_trial_pairs": 3,
    "actual_grid_values": 6,
    "necessary_base_geometry": 0,
}

def require(test, message):
    if not bool(test):
        raise ValueError(message)

class PositiveDirectionLimit(RuntimeError):
    def __init__(self, kind, used, limit):
        self.kind,self.used,self.limit=kind,used,limit
        super().__init__("positive-direction scope exhausted: %s %s/%s"%(kind,used,limit))

class PositiveDirectionLedger:
    """One pre-import clock; event times are nested and are not resummed."""
    def __init__(self, started, *, limits=None):
        now=time.monotonic()
        require(type(started) in (int,float) and math.isfinite(started)
                and 0 <= started <= now, "real pre-input monotonic clock required")
        selected=dict(LIMITS if limits is None else limits)
        require(selected==LIMITS, "the new direction task has one immutable scope")
        self.started=float(started)
        self.limits=selected
        self.counts={key:0 for key in selected if key!="science_seconds"}
        self.events=[]
        self.old_backend_calls={"HiGHS":0,"SOC":0,"cone":0,"Hildreth":0,"paid_finite_LP":0}
        self.check()
    def elapsed(self):
        return time.monotonic()-self.started
    def check(self):
        elapsed=self.elapsed()
        if not math.isfinite(elapsed) or elapsed>self.limits["science_seconds"]:
            raise PositiveDirectionLimit("science_seconds",elapsed,self.limits["science_seconds"])
        return elapsed
    def charge(self,key,count=1):
        self.check()
        require(key in self.counts and type(count) is int and count>0,
                "known counter and positive integer debit required")
        if self.counts[key]+count>self.limits[key]:
            raise PositiveDirectionLimit(key,self.counts[key]+count,self.limits[key])
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
    def report(self):
        elapsed=self.elapsed()
        events=copy.deepcopy(self.events)
        for event in events:
            tick=event.pop("_started",None)
            if tick is not None:
                event["elapsed_seconds_so_far"]=time.monotonic()-tick
        return {
            "schema":POLICY+"-ledger","limits":dict(self.limits),
            "started_counts":dict(self.counts),"scientific_seconds":elapsed,
            "ancestor_scientific_seconds":SOURCE_GLOBAL_SECONDS,
            "total_ancestor_plus_new_scientific_seconds":SOURCE_GLOBAL_SECONDS+elapsed,
            "source_original_full_values":SOURCE_ORIGINAL_VALUES,
            "new_actual_value_debits":self.counts["actual_grid_values"],
            "total_source_plus_new_full_value_debits":
                SOURCE_ORIGINAL_VALUES+self.counts["actual_grid_values"],
            "events":events,"old_backend_calls":dict(self.old_backend_calls),
            "all_input_imports_restoration_failures_and_output_share_this_clock":True,
            "event_times_nested_not_added_again":True,
            "old64_old32_Hildreth_and_paid_finite_master_are_closed":True,
            "base_geometry_cap":0,
            "deadline_observed_exceeded":elapsed>self.limits["science_seconds"],
            "observed_overrun_seconds":max(0.,elapsed-self.limits["science_seconds"]),
        }
