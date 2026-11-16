#!/usr/bin/env python3
"""R497: reuse completed original inverse boxes with unchanged logical work.

The caller must explicitly instantiate the returned subclass. No old module
global, original complete_box body, scientific threshold or result is patched.
Scientific use belongs to this repository's public GitHub Actions.
Author: ChatGPT /root (AI), 2026-11-16.
"""
from __future__ import annotations
from collections import OrderedDict
from copy import deepcopy
from pathlib import Path
import hashlib
import os
import sys

SCHEMA="R497-current-C-completed-inverse-box-cache-v1"
REPOSITORY="Rogerhu12/math-research-public"
HELPER_NAME="geometry_20261116_completed_inverse_box_cache.py"
BASELINES={
    "geometry_20261115_current_C_pruefer_joint_radial_sampling.py":
        "32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4",
    "geometry_20261116_current_C_cached_inverse_joint_radial_sampling.py":
        "ae9dde7a93cd0477d7d8669593459bedf75fdc58083625beee40dd047eab5594",
}
DEPENDENCIES={
    "geometry_20261115_stored_C_finite_head_pruefer_positive.py":
        "c2f515aa276890da63871fe0e9e1440775950d4985465457e9d6025976d914c8",
    "geometry_20261115_stored_continuous_E_cover_v3.py":
        "f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df",
}


def _receipt(path):
    path=Path(path).resolve()
    raw=path.read_bytes()
    return dict(file=path.name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def _freeze(value):
    # All original numerical values are scalar Arb objects with immutable
    # semantics. The only mutable member is the complete branch-name list.
    return tuple((key,tuple(item) if key=="branches" else item)
                 for key,item in value.items())


def _fresh(value):
    # Preserve all original keys and order, and allocate a new branch list.
    # No ball is reconstructed through endpoints, decimal text or a midpoint.
    return {key:list(item) if key=="branches" else item for key,item in value}


def bind_completed_inverse_box_sampler(original_type,*,computations,
                                       helper_sha256,max_records=4096):
    """Return an explicitly instantiated subclass of the actual original class.

    The only registered class owners are the frozen original32b0 source and the
    exact five-edit R497 view. The latter changes imports, schema, two resource/
    source CLI arguments, actual construction, and final metadata selection.
    Its InverseSampler class body remains byte-for-byte original.
    """
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY):
        raise RuntimeError("Scientific inverse sampling belongs to public repository Actions")
    if type(max_records) is not int or not 0<=max_records<=65536:
        raise ValueError("Use an explicit finite cache capacity between zero and 65536")
    comp=Path(computations).resolve()
    here=Path(__file__).resolve()
    if here.parent!=comp or here.name!=HELPER_NAME:
        raise ValueError("The helper must be the explicit current computations source")
    helper=_receipt(here)
    if helper["sha256"]!=helper_sha256:
        raise ValueError("Actual helper bytes differ from the explicit caller pin")
    module=sys.modules.get(getattr(original_type,"__module__",None))
    if module is None or getattr(module,"InverseSampler",None) is not original_type:
        raise ValueError("Use the actual class owner, not a similar class from another load")
    owner_path=Path(module.__file__).resolve()
    owner=_receipt(owner_path)
    if owner_path.parent!=comp or BASELINES.get(owner["file"])!=owner["sha256"]:
        raise ValueError("This cache is registered only for the original class or exact R497 view")
    B,F=getattr(module,"B",None),getattr(module,"F",None)
    if B is None or F is None:
        raise ValueError("Complete the original runtime load before binding the sampler")
    dependencies=[]
    for runtime in (F,B):
        p=Path(runtime.__file__).resolve();item=_receipt(p)
        if p.parent!=comp or DEPENDENCIES.get(item["file"])!=item["sha256"]:
            raise ValueError("The original full head/radial-range source differs")
        dependencies.append(item)
    original_complete_box=original_type.complete_box
    original_schema=module.SCHEMA
    source_binding=dict(schema=SCHEMA+"-source-binding",helper=helper,
        actual_class_owner=owner,actual_original_schema=original_schema,
        original_sampler_ancestor_sha256=BASELINES[
            "geometry_20261115_current_C_pruefer_joint_radial_sampling.py"],
        full_original_dependencies=dependencies,
        actual_repository=os.environ["GITHUB_REPOSITORY"],
        actual_run_id=os.environ["GITHUB_RUN_ID"],actual_source_commit=os.environ["GITHUB_SHA"],
        old_source_global_replaced=False,original_complete_box_body_changed=False)

    class CompletedBoxInverseSampler(original_type):
        def __init__(self,head,data,args,geometry,ledger,unpaid,budget):
            super().__init__(head,data,args,geometry,ledger,unpaid,budget)
            self._R497_cache=OrderedDict()
            self._R497_stats=dict(calls_started=0,calls_completed=0,
                cache_lookup_hits=0,cache_hits_returned=0,
                original_evaluations_started=0,original_evaluations_completed=0,
                completed_entries_inserted=0,evictions=0,
                disabled_calls=0,context_change_bypasses=0,last_operation=None)

        def _R497_key(self,panel,lo,hi):
            # Per-instance ownership prevents sharing across C families/jobs.
            # No mutable interval is a key; endpoints are exact Fractions.
            piece=self.head.pieces[panel["source_piece"]]
            ctx=module.B.ctx
            speeds=self.geometry.base_speed
            return (id(self.head),id(self.geometry),id(piece),id(panel),
                panel["row"],panel["source_piece"],lo,hi,
                id(module.B),id(module.F),int(ctx.prec),getattr(ctx,"threads",None),
                panel["row"] in speeds,id(speeds.get(panel["row"])))

        def complete_box(self,panel,lo,hi):
            stats=self._R497_stats;stats["calls_started"]+=1
            key=self._R497_key(panel,lo,hi)
            last=dict(original_source_panel_row=panel["row"],source_piece=panel["source_piece"],
                closed_parameter_interval=[str(lo),str(hi)],precision_bits=key[10],
                branch=None,complete_return=False,
                original_work_charge="not-yet-observed",
                cache_not_a_point_or_field_certificate=True)
            stats["last_operation"]=last
            if max_records and key in self._R497_cache:
                stats["cache_lookup_hits"]+=1;last["branch"]="completed-cache-hit"
                # These are exactly the original two prelude statements, in
                # their original order. A cached box never evades the old cap.
                self.budget.attempt();self.range_count+=1
                last["original_work_charge"]="completed-on-hit"
                value=self._R497_cache.pop(key)
                self._R497_cache[key]=value
                result=_fresh(value)
                stats["cache_hits_returned"]+=1;stats["calls_completed"]+=1
                last["complete_return"]=True
                return result
            last["branch"]="original-complete-box"
            last["original_work_charge"]="owned-by-original-call-not-intercepted"
            stats["original_evaluations_started"]+=1
            if not max_records:stats["disabled_calls"]+=1
            # Includes the original work charge, positivity/finite conditions,
            # all cap branches, complete radial_range and every original error.
            # No exception is cached, swallowed, retried, or relabelled.
            result=original_complete_box(self,panel,lo,hi)
            stats["original_evaluations_completed"]+=1
            last["original_work_charge"]="completed-by-original-call"
            after=self._R497_key(panel,lo,hi)
            # original_speed may populate its original per-panel cache during
            # the first evaluation. Store under that real post-call state.
            if max_records and key[:-2]==after[:-2]:
                stored=_freeze(result)
                self._R497_cache[after]=stored
                self._R497_cache.move_to_end(after)
                stats["completed_entries_inserted"]+=1
                if len(self._R497_cache)>max_records:
                    self._R497_cache.popitem(last=False);stats["evictions"]+=1
            elif max_records:
                stats["context_change_bypasses"]+=1
            stats["calls_completed"]+=1;last["complete_return"]=True
            return result

        def completed_inverse_box_cache_readback(self):
            stats=dict(self._R497_stats)
            if stats["last_operation"] is not None:
                stats["last_operation"]=dict(stats["last_operation"])
                stats["last_operation"]["closed_parameter_interval"]=list(
                    stats["last_operation"]["closed_parameter_interval"])
            return dict(schema=SCHEMA+"-actual-necessary-metadata",
                source_binding=deepcopy(source_binding),capacity_records=max_records,
                current_records=len(self._R497_cache),statistics=stats,
                actual_original_point_count=self.point_count,
                actual_original_inverse_range_count=self.range_count,
                actual_original_budget_attempts=self.budget.attempts,
                every_hit_charges_original_attempt_and_range_count=True,
                all_original_candidates_closed_leaves_and_numeric_errors_preserved=True,
                no_exception_or_unreturned_box_cached=True,
                no_Arb_decimal_endpoint_or_midpoint_reconstruction=True,
                no_saved_ball_or_raw_array_in_necessary_metadata=True,
                original_head_inputs_must_remain_fixed_for_this_sampler=True,
                timing_or_same_resource_stop_or_complete_point_claimed=False,
                original_work_unit_limit_failure_not_removed=True)

    CompletedBoxInverseSampler.__name__="R497CompletedBoxInverseSampler"
    return CompletedBoxInverseSampler
