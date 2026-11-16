#!/usr/bin/env python3
"""R500: same-semantic-C complete tail queries for a real R492/R495 field.

The old ActualCompleteCTarget first binds its genuine factory/result payload.
The complete R489 result then supplies an independent actual query baseline.
Its original full source panels, cumulative radii, and all-root deep formula
feed ONE original R426 live-query instance. Old valid closed bounds survive.
No CP, exact definition, nodal/material word, field, or source global is changed.

Only E values are queried here. E_r/E_rr at the cut and the accurate cut six
jets remain the actual R492 responsibility; no new whole-tail derivative API,
accepted field, error decrease, run, or performance claim is fabricated.
All scientific evaluation executes only in the named public Actions.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time
from types import SimpleNamespace

REPOSITORY = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "R500-same-semantic-C-refined-head-complete-tail-queries-v1"
LEAF_NAME = "geometry_20261116_same_C_refined_leaf_target_and_cut.py"
LEAF_SHA = "a7b1bd9d64db43986b5718d664dc6209227cd89a0cd9fb490e8dc6f9f4482aa7"
PROVIDER_NAME = "geometry_20261116_same_C_full_head_refinement.py"
PROVIDER_SHA = "0ce2f7ab8d1cfc95097ac8089c41ecc1f888343c8432255bd91b1d6cc5d3f8f8"
METRIC_NAME = "geometry_20261115_current_C_ten_live_query_complete_metric.py"
METRIC_SHA = "77be1d98c7401c4d0962adae7b824fd22c66b3a0127885b080859edc0f4a7892"
LIVE_NAME = "geometry_20261115_same_job_C_live_query_provider.py"
LIVE_SHA = "07fc4e41a6318c43a6e03313356df4df7538ccd5ea110406434b2e420c09bcd9"
C_NAME = "geometry_20261115_stored_continuous_E_cover_v3.py"
C_SHA = "f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df"
PINS = {LEAF_NAME:LEAF_SHA, PROVIDER_NAME:PROVIDER_SHA,
        METRIC_NAME:METRIC_SHA, LIVE_NAME:LIVE_SHA, C_NAME:C_SHA}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
        "Execute same-C interval query evaluation only in the named public Actions")


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",",":"),
        ensure_ascii=True, allow_nan=False)+"\n").encode("ascii")


def identity(value):
    raw = canonical(value)
    return dict(canonical_bytes=len(raw), canonical_sha256=hashlib.sha256(raw).hexdigest())


def receipt(path, check=None):
    if check is not None:
        check()
    path = Path(path).resolve(strict=True)
    raw = path.read_bytes()
    if check is not None:
        check()
    return dict(file=str(path), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def same_payload(a, b):
    return isinstance(a, dict) and isinstance(b, dict) and all(
        a.get(key) == b.get(key) for key in ("bytes","sha256"))


def write(path, value):
    path = Path(path)
    raw = canonical(value)
    with path.open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    return dict(file=str(path.resolve()), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def load(comp, name):
    path = comp/name
    require(receipt(path)["sha256"] == PINS[name], "Actual query dependency differs: "+name)
    label = "_r500_"+path.stem+"_"+str(time.monotonic_ns())
    spec = importlib.util.spec_from_file_location(label,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[label] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(label,None)
        raise
    return module


def actual_leaf_owner(current, comp):
    module = sys.modules.get(type(current).__module__)
    require(module is not None and getattr(module,"RefinedCutBundle",None) is type(current),
        "Use the genuinely loaded independent R492 refined bundle")
    path = Path(module.__file__).resolve(strict=True)
    require(path == comp/LEAF_NAME and receipt(path)["sha256"] == LEAF_SHA,
        "The actual loaded refined-bundle class owner differs")
    require(type(current.provider) is module.RefinedLeafProvider
        and type(current.target) is module.RefinedTenTarget
        and current.target.provider is current.provider,
        "Keep the actual same provider and target evaluation instance")
    require(identity(current.target.definition) == current.provider.definition_id
        and current.target.definition is current.original.target.definition
        and current.source_bundle is current.original.source_bundle,
        "No original definition or source bundle may be relabelled")
    return module


class FixedRefinedQueries:
    """An independently named actual query view, never an original factory result."""
    def __init__(self, C, Metric, baseline, current, provider):
        self.C, self.Metric, self.provider = C, Metric, provider
        self.domain = baseline.domain
        self.supplied = True
        self.rows, self.cuts, self.query_status = [], [], []
        self.original_factory_result = copy.deepcopy(baseline.expected_result)
        self.explicit_target = copy.deepcopy(baseline.explicit_target)
        self.definition_identity = identity(current.target.definition)
        provider.check()
        R = provider.R
        fresh_dir = provider.directory/"refined-C"
        report, rid, binding, bid = R.checked_C(
            fresh_dir,provider.actual["actual_refined_C"])
        require(same_payload(rid,provider.report["actual_refined_C"])
            and same_payload(bid,provider.actual["actual_refined_C_binding"]),
            "The full refined C and binding must be the actual R489 members")
        equality = R.semantic_bindings(baseline.binding,binding)
        require(canonical(equality) == canonical(provider.report["semantic_input_equivalence"]),
            "Every original non-work C/root input must be exactly the same")
        require(report.get("schema") == C.SCHEMA
            and report.get("source_sha256") == C_SHA
            and report.get("repository") == REPOSITORY
            and report.get("run_id") == os.environ.get("GITHUB_RUN_ID")
            and report.get("source_commit") == os.environ.get("GITHUB_SHA")
            and report.get("target_model_schema") == C.MODEL_SCHEMA
            and report.get("deep_definition") == "original-exact-root-family"
            and report.get("model_choice_is_explicit_and_not_original_finite_output_relabel") is True
            and report.get("original_finite_output_certified_as_continuous_solution") is False
            and report.get("R26_numerical_certificate_or_rational_deep_target_used") is False
            and report.get("global_warp_alpha_or_original_cut_renormalised") is False
            and report.get("original_real_profile_and_model_C_unchanged") is True
            and report.get("preserved_original_producer_source",{}).get("sha256") == C.BASE_SOURCE_SHA256
            and report.get("preserved_unit_panel_producer_source",{}).get("sha256") == C.UNIT_PANEL_SOURCE_SHA256,
            "Retain the real complete-or-partial original C result, all roots, and source semantics")
        plan, pid = Metric.bound_member(C,fresh_dir,report["query_plan"])
        queries, qid = Metric.bound_member(C,fresh_dir,report["query_results"])
        require(binding.get("schema") == C.SCHEMA+"-input-binding"
            and binding.get("source_sha256") == C_SHA
            and binding.get("original_source_revision") == C.REVISION
            and binding.get("proof",{}).get("sha256") == C.PROOF_SHA
            and canonical(binding["preserved_original_producer_source"])
                == canonical(report["preserved_original_producer_source"])
            and canonical(binding["preserved_unit_panel_producer_source"])
                == canonical(report["preserved_unit_panel_producer_source"])
            and set(binding["original_sources"]) == set(C.PINS)
            and all(binding["original_sources"][name]["sha256"] == expected
                for name,expected in C.PINS.items())
            and plan.get("schema") == C.QUERY_SCHEMA
            and plan.get("input_binding_sha256") == bid["sha256"]
            and queries.get("schema") == C.SCHEMA+"-queries",
            "Retain all actual original sources, input, proof and complete query members")
        convention = binding["convention"]
        require(convention.get("schema") == C.MODEL_SCHEMA
            and convention.get("explicit_model_layer_choice") is True
            and convention.get("deep_definition") == report["deep_definition"]
            and convention.get("deep_bounds_valid_for_every_original_root_in_half_to_two") is True
            and convention.get("deep_roots_numerically_selected_or_computed") is False
            and convention.get("natural_outer_radius_reidentified_as_nominal_cut") is False
            and convention.get("global_lambda_reselected") is False
            and self.domain[0] == C.rat(binding["physical_parameters"]["rCuff"])
            and self.domain[1] == Metric.rational(self.explicit_target["original_binary_cut_exact_rational"]),
            "The fixed physical domain and the complete unselected root family differ")
        self.conditions_proved = bool(
            report.get("declared_continuous_model_family_conditions_proved") is True
            and report.get("original_exact_deep_root_existence_proved") is True
            and report.get("all_admissible_original_root_choices_uniformly_enclosed") is True
            and report.get("full_finite_head_complete") is True
            and report.get("complete_original_pieces") == 1440
            and report.get("original_piece_count") == 1440
            and report.get("original_finite_cell_count") == 160
            and report.get("protected_join",{}).get("proved") is True
            and report.get("finite_joins",{}).get("proved") is True
            and convention.get("root_existence_proved") is True)
        self.natural_radius = (None if report.get("natural_outer_radius") is None
            else Metric.producer_interval(report["natural_outer_radius"]))
        self.receipts = dict(result=rid,input_binding=bid,query_plan=pid,query_results=qid)
        self.producer_report,self.binding,self.query_plan = report,binding,plan
        self.expected_binding = binding
        self.expected_result = rid
        self.semantic_equivalence = equality
        self.directory = fresh_dir
        requested,returned = plan["queries"],queries["results"]
        require(isinstance(requested,list) and isinstance(returned,list)
            and type(report.get("requested_query_count")) is int
            and type(report.get("returned_query_count")) is int
            and len(requested) == report["requested_query_count"]
            and len(returned) == report["returned_query_count"]
            and len(returned) <= len(requested)
            and canonical(requested) == canonical(baseline.query_plan["queries"])
            and canonical(queries.get("unvisited_query_suffix"))
                == canonical(report.get("unvisited_query_suffix")),
            "The original entire plan and the actual returned prefix/suffix must be preserved")
        for index,row in enumerate(returned):
            provider.check()
            q = row["query"]
            require(canonical(q) == canonical(requested[index])
                and type(q.get("index")) is int and q["index"] == index
                and q.get("left_closed") is True and q.get("right_closed") is True,
                "Keep every real query in order with both closed endpoints")
            status = dict(index=index,query=copy.deepcopy(q),usable=False,
                actual_original_status={key:copy.deepcopy(row[key]) for key in Metric.QUERY_KEYS if key in row})
            self.query_status.append(status)
            if not (self.conditions_proved and self.natural_radius is not None
                and row.get("complete_closed_domain_bound") is True
                and row.get("domain_containment_proved") is True
                and row.get("continuous_model_family_conditions_proved") is True):
                continue
            if q["kind"] == "whole-natural-domain":
                require(q["left"] == "original-exact-dyadic-rCuff"
                    and q["right"] == "natural-real-integral-R_out",
                    "A whole-natural-domain query was relabelled")
                left,right = self.domain[0],self.natural_radius[0]
            elif q["kind"] == "closed-rational-radius-interval":
                left,right = Metric.rational(q["left"]),Metric.rational(q["right"])
                require(self.domain[0] <= left <= right <= self.natural_radius[0],
                    "A purported complete query exceeds its actual common natural domain")
            else:
                raise ValueError("Unsupported original closed query kind")
            lo,hi = Metric.producer_interval(row["E"])
            require(hi >= 1,"The original exact formula E=1+w^2 contradicts this E record")
            left,right = max(left,self.domain[0]),min(right,self.domain[1])
            if left > right:
                status["unused_reason"] = "Actual closed query lies outside the unchanged field"
                continue
            self.rows.append(dict(index=index,left=left,right=right,lower=max(Q(1),lo),upper=hi,
                query_kind=q["kind"],original_E=copy.deepcopy(row["E"]),
                work_resolution_complete=row.get("work_resolution_complete")))
            status.update(usable=True,effective_closed_field_interval=[str(left),str(right)],
                E_lower_used=str(max(Q(1),lo)),E_upper_used=str(hi),
                analytic_E_ge_one_intersection=True)
        self.rows.sort(key=lambda row:(row["left"],row["right"],row["index"]))
        self.cuts = sorted({x for row in self.rows for x in (row["left"],row["right"])})
        provider.check()

    def bounds(self,a,b):
        # This original pure closed-interval coverage function consumes the
        # explicitly separate rows above; no original object is relabelled.
        return self.Metric.ActualCompleteCTarget.bounds(self,a,b)

    def describe(self):
        report = self.producer_report
        return dict(schema=SCHEMA+"-actual-refined-fixed-query-view",
            actual_refined_result_and_members=copy.deepcopy(self.receipts),
            original_factory_C_result=copy.deepcopy(self.original_factory_result),
            unchanged_target_identity=identity(self.explicit_target),
            unchanged_accurate_definition_identity=self.definition_identity,
            semantic_input_equivalence=copy.deepcopy(self.semantic_equivalence),
            complete_field_radial_domain=list(map(str,self.domain)),
            actual_natural_radius=None if self.natural_radius is None else list(map(str,self.natural_radius)),
            original_model_family_conditions_proved=self.conditions_proved,
            complete_field_radial_domain_covered=self.bounds(*self.domain) is not None,
            every_actual_refined_query=copy.deepcopy(self.query_status),
            actual_not_returned_query_index_suffix=[len(self.query_status),len(self.query_plan["queries"])],
            actual_producer_unvisited_query_suffix=copy.deepcopy(report.get("unvisited_query_suffix")),
            actual_producer_unvisited_source_piece_suffix=copy.deepcopy(report.get("unvisited_source_piece_suffix")),
            actual_producer_error=copy.deepcopy(report.get("error")),
            actual_original_unpaid_rows=report.get("resource_or_unpaid_scope_rows"),
            actual_original_ledger_descriptors=copy.deepcopy(report.get("ledgers")),
            original_resolution_flags={key:report[key] for key in (
                "all_requested_closed_query_bounds_complete","numerical_work_resolution_complete",
                "continuous_convention_C_query_enclosures_complete") if key in report},
            fixed_original_query_rows_use_new_full_head_cumulative_radii=True,
            E_value_order_only=True,whole_tail_Er_Err_returned_by_this_API=False,
            query_resolution_is_not_an_acceptance_condition=True,
            all_original_root_sequences_retained=True,
            primitive_inverse_ledger_values_not_independently_reaudited=True)

    def necessary(self):
        return self.describe()


class ExistingBudgetWithNamespace:
    """One existing query budget, with the already bound original job clock."""
    def __init__(self,budget,provider):
        object.__setattr__(self,"_original",budget)
        object.__setattr__(self,"_provider",provider)

    def __getattr__(self,name):
        return getattr(self._original,name)

    def __setattr__(self,name,value):
        if name in ("_original","_provider"):
            object.__setattr__(self,name,value)
        else:
            setattr(self._original,name,value)

    def check(self):
        self._provider.check()
        self._original.check()

    def panel(self):
        self.check()
        self._original.panel()

    def query(self):
        self.check()
        self._original.query()

    def begin(self):
        self.check()
        self._original.begin()

    def end(self):
        self._original.end()

    def describe(self):
        result = self._original.describe()
        result.update(original_namespace_deadline_unix_seconds=self._provider.deadline,
            actual_deadline=copy.deepcopy(self._provider.actual["original_deadline"]),
            new_query_budget_or_clock_created_by_wrapper=False)
        return result


class SameCTailQueries:
    """Public original-tail interface with two actual enclosures of one target."""
    def __init__(self, C, Metric, Live, baseline, current, args, output, metric_started):
        self.C,self.Metric,self.current = C,Metric,current
        self.original,self.provider = baseline,current.provider
        self.domain,self.supplied = baseline.domain,True
        self.expected,self.expected_binding = baseline.expected,baseline.expected_binding
        self.expected_result,self.explicit_target = baseline.expected_result,baseline.explicit_target
        self.receipts = copy.deepcopy(baseline.receipts)
        self.producer_report,self.binding,self.query_plan = (
            baseline.producer_report,baseline.binding,baseline.query_plan)
        self.conditions_proved = baseline.conditions_proved
        self.natural_radius = baseline.natural_radius
        self.refined = FixedRefinedQueries(C,Metric,baseline,current,self.provider)
        # Either actual proof applies to the SAME semantic root family; usable
        # query rows retain their own complete-condition checks above.
        self.conditions_proved = bool(baseline.conditions_proved or self.refined.conditions_proved)
        if self.natural_radius is not None and self.refined.natural_radius is not None:
            lo = max(self.natural_radius[0],self.refined.natural_radius[0])
            hi = min(self.natural_radius[1],self.refined.natural_radius[1])
            require(lo <= hi,"Same-root natural-radius enclosures are disjoint; no refutation inferred")
            self.natural_radius = (lo,hi)
        # Immutable initial root cuts may include both complete, genuinely
        # returned query partitions. Later live queries never mutate this list.
        self.cuts = sorted(set(baseline.cuts+self.refined.cuts))
        local = SimpleNamespace(**vars(args))
        local.continuous_e_result = self.refined.directory/"result.json"
        local.continuous_e_result_sha256 = self.refined.receipts["result"]["sha256"]
        local.out = Path(output)
        # Exactly one original LiveQueryTarget and one original budget. This
        # replaces the caller's original construction, not a second oracle.
        self.live = Live.LiveQueryTarget(C,self.refined,local,Path(output),metric_started)
        self.live.budget = ExistingBudgetWithNamespace(self.live.budget,self.provider)
        self.parameters = self.live.parameters
        self.counts = dict(bounds_calls=0,both_complete_intersections=0,
            strict_width_reductions_observed=0,mixed_complete_cover_uses=0)
        self.binding_receipt = write(Path(output)/"large-arrays"/"same-C-refined-tail-binding.json",
            dict(schema=SCHEMA+"-binding",source=receipt(__file__),
                actual_sources={name:receipt(HERE/name) for name in PINS},
                original_factory_target=copy.deepcopy(self.receipts),
                actual_refined_C_queries=copy.deepcopy(self.refined.receipts),
                actual_R489_result=self.provider.report_id,
                actual_R492_leaf_file=self.provider.actual["actual_refined_leaf_file"],
                original_live_query_binding=self.live.binding_receipt,
                original_deadline=self.provider.actual["original_deadline"],
                original_metric_started_monotonic=metric_started,
                original_metric_budget_seconds=args.budget_seconds,
                actual_query_parameters=self.parameters,
                complete_exact_target_identity=identity(self.explicit_target),
                original_CP_definition_ten_parameters_material_and_field_unchanged=True,
                derivative_order_consumed_from_complete_tail_queries=0,
                cut_twojet_and_accurate_sixjets_owned_by_R492=True))

    def __getattr__(self,name):
        return getattr(self.original,name)

    def _available_rows(self):
        rows = []
        for label,view in (("original",self.original),("R489",self.refined)):
            rows.extend(dict(left=v["left"],right=v["right"],lower=v["lower"],upper=v["upper"],
                source=dict(kind=label,index=v["index"])) for v in view.rows)
        rows.extend(dict(left=v["left"],right=v["right"],lower=v["lo"],upper=v["hi"],
            source=dict(kind="R500-live-from-R489",index=v["index"]))
            for v in self.live.cache.values() if v.get("complete") is True)
        return rows

    def bounds(self,a,b):
        require(self.domain[0] <= a <= b <= self.domain[1],
            "Query only the unchanged actual physical closed field domain")
        old = self.original.bounds(a,b)
        fresh = self.live.bounds(a,b)
        self.counts["bounds_calls"] += 1
        candidates,sources = [],[]
        if old is not None:
            candidates.append(old[:2])
            sources.append(dict(kind="original_complete_closed_query_cover",indices=old[2]))
        if fresh is not None:
            candidates.append(fresh[:2])
            sources.append(dict(kind="R489_complete_closed_and_actual_live_query_cover",
                actual_complete_query_sources=fresh[2]))
        if not candidates:
            selected = sorted((v for v in self._available_rows()
                if v["left"] <= b and a <= v["right"]),
                key=lambda v:(v["left"],v["right"]))
            cursor,started = a,False
            for v in selected:
                if v["left"] > cursor:
                    break
                if v["right"] >= cursor:
                    cursor,started = max(cursor,v["right"]),True
                if cursor >= b:
                    break
            if not started or cursor < b:
                return None
            candidates.append((min(v["lower"] for v in selected),max(v["upper"] for v in selected)))
            sources.append(dict(kind="union_of_actual_complete_closed_subintervals",
                intervals=[dict(source=v["source"],closed_radius=[str(v["left"]),str(v["right"])])
                    for v in selected]))
            self.counts["mixed_complete_cover_uses"] += 1
        lo,hi = max(v[0] for v in candidates),min(v[1] for v in candidates)
        require(lo <= hi,"Actual same-C closed value enclosures are disjoint; do not fabricate a bound")
        if old is not None and fresh is not None:
            self.counts["both_complete_intersections"] += 1
            if hi-lo < old[1]-old[0]:
                self.counts["strict_width_reductions_observed"] += 1
        return lo,hi,sources

    def refine(self,a,b,cell):
        self.provider.check()
        result = self.live.refine(a,b,cell)
        result.update(actual_same_semantic_C_refinement=self.provider.report_id,
            source_panels_belong_to_actual_R489_refined_C=self.refined.receipts["result"],
            all_original_coarse_bounds_remain_usable=True,
            finite_head_cumulative_radii_are_the_real_recomputed_ones=True)
        self.provider.check()
        return result

    def close(self):
        # Metadata/close must remain available after a resource stop.
        return self.live.close()

    def live_status(self):
        return dict(schema=SCHEMA+"-live-status",source=receipt(__file__),
            actual_original_R426_live_status=self.live.live_status(),
            query_baseline_is_actual_R489_complete_head=True,
            original_factory_C_remains_separately_bound=True,
            new_1440_head_not_reexecuted_by_this_bridge=True,
            only_subqueries_execute_during_this_metric_call=True,
            original_old_and_new_unpaid_scopes_not_discarded=True,
            same_actual_namespace_deadline=self.provider.actual["original_deadline"])

    def describe(self):
        original = self.original.describe()
        refined = self.refined.describe()
        return dict(schema=SCHEMA,source=receipt(__file__),
            original_factory_query_target=original,
            actual_R489_query_target=refined,
            actual_refined_leaf_evaluation=self.provider.describe(),
            actual_live_queries=self.live_status(),
            complete_field_radial_domain=list(map(str,self.domain)),
            complete_field_radial_domain_covered=self.bounds(*self.domain) is not None,
            fixed_original_target_identity=identity(self.explicit_target),
            complete_original_input_binding_identity=identity(self.expected_binding),
            immutable_initial_query_cuts=list(map(str,self.cuts)),
            original_metric_allowance_and_original_absolute_clock=True,
            real_query_counts=copy.deepcopy(self.counts),
            work_resolution_never_used_as_new_scientific_acceptance=True,
            original_field_CP_B_material_and_all_t_parameters_unchanged=True,
            E_value_queries_only_no_whole_tail_derivative_upgrade=True,
            query_bound_width_reduction_not_an_accepted_field_or_error_decrease=True,
            no_new_outer_consumer_or_experiment_registered_by_this_helper=True)

    def necessary(self):
        return self.describe()


def bind_loaded_same_C_tail_queries(current, *, args, output, metric_started,
        budget_check=None):
    """Replace ONE original LiveQueryTarget construction after R492/R495 load.

    Required existing args: computations, continuous_e_result,
    continuous_e_result_sha256, budget_seconds and all eleven original
    c_query_* fields. current is the actual R492 RefinedCutBundle, including
    the four explicitly registered R495 families. The R489 source currently
    retains its explicit actual202205 origin; no new origin is inferred here.
    """
    actions()
    comp = Path(args.computations).resolve(strict=True)
    require(comp == HERE,"Run the true independent helper and dependencies in one actual HERE")
    require(type(metric_started) in (int,float) and math.isfinite(metric_started)
        and type(args.budget_seconds) in (int,float)
        and math.isfinite(args.budget_seconds) and args.budget_seconds > 0,
        "Retain the caller's actual finite start and original positive allowance")
    Leaf = actual_leaf_owner(current,comp)
    p = current.provider
    require(p.comp == comp and type(p) is Leaf.RefinedLeafProvider,
        "Use the actual same-job loaded provider")
    if budget_check is not None:
        budget_check()
    p.check()
    output = Path(output).resolve(strict=True)
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    namespace = p.R.inside(p.input["namespace"],runner)
    require(output != runner and output.is_relative_to(namespace)
        and (output/"large-arrays").is_dir()
        and not (output/"large-arrays").is_symlink()
        and (output/"large-arrays").resolve().parent == output
        and not (output/"large-arrays"/"live-C-queries").exists()
        and not (output/"large-arrays"/"same-C-refined-tail-binding.json").exists(),
        "Use the caller's actual owned output with no existing live oracle or binding")
    for name,expected in PINS.items():
        require(receipt(comp/name,p.check)["sha256"] == expected,
            "A real required source was changed: "+name)
    Metric,Live,C = (load(comp,METRIC_NAME),load(comp,LIVE_NAME),load(comp,C_NAME))
    # Full old four-member/factory/physical/root binding runs unchanged.
    original = Metric.ActualCompleteCTarget(C,current,
        args.continuous_e_result,args.continuous_e_result_sha256)
    require(original.supplied
        and same_payload(original.receipts["result"],p.actual["actual_original_C"])
        and same_payload(original.receipts["input_binding"],p.actual["actual_original_C_binding"])
        and identity(current.target.definition) == p.definition_id,
        "The old actual query result is not this unchanged accurate field's original C")
    p.check()
    result = SameCTailQueries(C,Metric,Live,original,current,args,output,metric_started)
    if budget_check is not None:
        budget_check()
    p.check()
    return result
