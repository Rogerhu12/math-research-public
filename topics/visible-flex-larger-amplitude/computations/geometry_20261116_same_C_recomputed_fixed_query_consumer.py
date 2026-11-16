#!/usr/bin/env python3
"""R504 fixed-query facade: consume R489 complete queries without a new oracle.

This role retains the original fixed R418 call scope. It reuses the exact
R500 validation, independent refined-query class, and complete-cover bounds
method, but does not instantiate LiveQueryTarget or an additional budget.
Every source, field, deadline and original error responsibility remains real.
Scientific binding/evaluation occurs only in the named public Actions.
"""
from __future__ import annotations

import copy
import importlib.util
import math
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
SCHEMA = "R504-same-C-recomputed-fixed-tail-query-consumer-v1"
TAIL_NAME = "geometry_20261116_same_C_refined_head_tail_queries.py"
TAIL_SHA = "2ab6b97fc77c520ed8b888d31a766d9e4e744fb40dc8af46dfd4d287f015b580"


def tail_library(comp):
    import hashlib
    path = Path(comp).resolve(strict=True)/TAIL_NAME
    if path.parent != HERE or hashlib.sha256(path.read_bytes()).hexdigest() != TAIL_SHA:
        raise ValueError("Use the complete actual R500 source in this same computations HERE")
    name = "_r504_tail_"+str(time.monotonic_ns())
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(name,None)
        raise
    return module


def bind_loaded_fixed_same_C_tail_queries(current, *, args, output,
        metric_started, budget_check=None):
    """Use the fixed branch only; no c_query arguments or refinement call."""
    Tail = tail_library(args.computations)
    Tail.actions()
    comp = Path(args.computations).resolve(strict=True)
    Tail.require(comp == HERE,"Use the actual fixed consumer HERE")
    Tail.require(type(metric_started) in (int,float) and math.isfinite(metric_started)
        and type(args.budget_seconds) in (int,float) and math.isfinite(args.budget_seconds)
        and args.budget_seconds > 0,"Keep the original fixed-metric allowance")
    Tail.actual_leaf_owner(current,comp)
    p = current.provider
    if budget_check is not None:
        budget_check()
    p.check()
    output = Path(output).resolve(strict=True)
    namespace = p.R.inside(p.input["namespace"],Tail.os.environ["RUNNER_TEMP"])
    large = output/"large-arrays"
    Tail.require(output.is_relative_to(namespace) and large.is_dir()
        and not large.is_symlink() and large.resolve().parent == output
        and not (large/"same-C-fixed-refined-tail-binding.json").exists(),
        "Use the actual caller-owned temporary output without replacing a binding")
    for name,expected in Tail.PINS.items():
        Tail.require(Tail.receipt(comp/name,p.check)["sha256"] == expected,
            "An actual inherited complete query source differs: "+name)
    Metric = Tail.load(comp,Tail.METRIC_NAME)
    C = Tail.load(comp,Tail.C_NAME)
    original = Metric.ActualCompleteCTarget(C,current,
        args.continuous_e_result,args.continuous_e_result_sha256)
    Tail.require(original.supplied
        and Tail.same_payload(original.receipts["result"],p.actual["actual_original_C"])
        and Tail.same_payload(original.receipts["input_binding"],p.actual["actual_original_C_binding"])
        and Tail.identity(current.target.definition) == p.definition_id,
        "The actual old factory query source or unchanged exact definition differs")

    class FixedQueryOnly:
        def __init__(self,refined):
            self.refined = refined
            self.cache = {}

        def bounds(self,a,b):
            return self.refined.bounds(a,b)

    class FixedTail(Tail.SameCTailQueries):
        def __init__(self):
            self.C,self.Metric,self.current = C,Metric,current
            self.original,self.provider = original,p
            self.domain,self.supplied = original.domain,True
            self.expected,self.expected_binding = original.expected,original.expected_binding
            self.expected_result,self.explicit_target = original.expected_result,original.explicit_target
            self.receipts = copy.deepcopy(original.receipts)
            self.producer_report,self.binding,self.query_plan = (
                original.producer_report,original.binding,original.query_plan)
            self.refined = Tail.FixedRefinedQueries(C,Metric,original,current,p)
            self.conditions_proved = bool(original.conditions_proved or self.refined.conditions_proved)
            self.natural_radius = original.natural_radius
            if self.natural_radius is not None and self.refined.natural_radius is not None:
                lo = max(self.natural_radius[0],self.refined.natural_radius[0])
                hi = min(self.natural_radius[1],self.refined.natural_radius[1])
                Tail.require(lo <= hi,
                    "Same-root natural-radius enclosures are disjoint; no bound fabricated")
                self.natural_radius = (lo,hi)
            self.cuts = sorted(set(original.cuts+self.refined.cuts))
            self.live = FixedQueryOnly(self.refined)
            self.parameters = {}
            self.counts = dict(bounds_calls=0,both_complete_intersections=0,
                strict_width_reductions_observed=0,mixed_complete_cover_uses=0)
            self.binding_receipt = Tail.write(large/"same-C-fixed-refined-tail-binding.json",
                dict(schema=SCHEMA+"-binding",source=Tail.receipt(__file__),
                    R500_source=Tail.receipt(comp/TAIL_NAME),
                    original_factory_target=copy.deepcopy(self.receipts),
                    actual_refined_C_queries=copy.deepcopy(self.refined.receipts),
                    actual_R489_result=p.report_id,
                    original_deadline=p.actual["original_deadline"],
                    original_fixed_metric_started_monotonic=metric_started,
                    original_fixed_metric_budget_seconds=args.budget_seconds,
                    original_target_identity=Tail.identity(self.explicit_target),
                    no_live_oracle_started=True,no_query_budget_created=True,
                    derivative_order_consumed_from_complete_tail_queries=0))

        def refine(self,a,b,cell):
            # The fixed original caller never requests this method. If a
            # caller asks explicitly, do not invent a live budget or result.
            return dict(attempted=False,reason="explicit_fixed_query_only_role",
                actual_requested_closed_radius=[str(a),str(b)],
                original_existing_coarse_bounds_preserved=True)

        def close(self):
            return {}

        def live_status(self):
            return dict(schema=SCHEMA+"-fixed-only-status",
                actual_binding=self.binding_receipt,
                no_live_oracle_started=True,no_subquery_arithmetic_called=True,
                no_query_ledger_or_new_budget_created=True,
                complete_actual_R489_fixed_queries_retained=True,
                original_deadline=p.actual["original_deadline"])

        def describe(self):
            result = super().describe()
            result.update(schema=SCHEMA,source=Tail.receipt(__file__),
                reused_complete_query_algebra_source=Tail.receipt(comp/TAIL_NAME),
                actually_registered_outer_role="R504-fixed-original112",
                no_live_oracle_started=True,
                outer_source_registration_is_not_an_actual_metric_result=True)
            return result

    result = FixedTail()
    if budget_check is not None:
        budget_check()
    p.check()
    return result
