#!/usr/bin/env python3
"""Actual same-C radial samples and oriented projective finite-far rows.

All scientific work is restricted to the named public Actions repository.
The input C primitive enclosures and R312 rows are unchanged original sources.
Complete R347 two-chart propagation retains every nonzero amplitude factor.
Each candidate Robin row is normalized with its proved amplitude sign and
strictly positive Euclidean norm before a cross-candidate hull is formed.
A numerical representative is a finite sampled approximation, not identified
with a jointly realized exact C root choice. The native geometry bundle v1
layout is unchanged; this independent sampler and all row provenance are new.
Author: geometry agent (AI), 2026-11-15.
"""
from __future__ import annotations
import argparse
import bisect
from collections import OrderedDict
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
import os
import shutil
from pathlib import Path
import struct
import sys
import time

SCHEMA="current-C-projective-physical-radial-samples-and-general-far-v1"
GEOMETRY_SCHEMA="current-C-native-radial-geometry-bundle-v1"
MODEL="R286-original-stored-continuous-model-convention-C-v1"
F_NAME="geometry_20261115_stored_C_finite_head_projective.py"
F_SHA="5440e2e0457b360120c180a2531e3db899d8534cf6366183fd68d111ede18216"
B_NAME="geometry_20261115_stored_continuous_E_cover_v3.py"
B_SHA="f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df"
REPOSITORY="Rogerhu12/math-research-public"
M,K,DEPTH=112,224,576
UNIT_ROW_PROOF_SHA="286f17eeab74b44716985fd199d5085cde667fb2626a9eb508ef72d35bc29140"
F=B=None


def require_actions():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise RuntimeError("Actual C sampling and propagation only in this public repository Actions")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def json_bytes(value):
    return (json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()


def emit(path,value):
    raw=json_bytes(value);path=Path(path)
    with path.open("xb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    return dict(file=path.name,bytes=len(raw),sha256=sha(raw))


def word(x):
    x=float(x)
    return dict(value=x if math.isfinite(x) else None,f64le=struct.pack("<d",x).hex(),
        classification="negative-zero" if x==0 and math.copysign(1,x)<0 else "finite" if math.isfinite(x)
        else "NaN" if math.isnan(x) else "positive-infinity" if x>0 else "negative-infinity")


def file_receipt(path):
    h=hashlib.sha256();count=0
    with Path(path).open("rb") as stream:
        while block:=stream.read(1048576):h.update(block);count+=len(block)
    return dict(file=Path(path).name,bytes=count,sha256=h.hexdigest())


def load_runtime(args):
    global F,B
    require_actions()
    path=args.code_directory/F_NAME
    rec=file_receipt(path)
    if rec["sha256"]!=F_SHA:raise ValueError("Use the frozen complete R347 projective propagator")
    spec=importlib.util.spec_from_file_location("_current_C_projective_flux",path)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module
    spec.loader.exec_module(module);F=module
    runtime,sources,proof=F.load_runtime(args);B=F.B
    unit_proof=file_receipt(args.unit_row_proof)
    if unit_proof["sha256"]!=UNIT_ROW_PROOF_SHA:
        raise ValueError("Use the frozen R357 original-orientation unit-row proof")
    if sources[B_NAME]["sha256"]!=B_SHA:raise ValueError("Actual v3 target source differs")
    return runtime,dict(projective_flux=rec,original_runtime_sources=sources),dict(
        projective_propagation=proof,oriented_unit_Robin_rows=unit_proof)


class OwnedBudget:
    """One explicitly charged phase, plus actual owned-output storage reserve."""
    def __init__(self,seconds,limit,label,out,free_bytes_reserve):
        self.started=time.monotonic();self.seconds=seconds;self.limit=limit
        self.attempts=0;self.label=label;self.out=Path(out)
        self.reserve=free_bytes_reserve;self.stop=None
        self.checks=0;self.checks_since_storage=0;self.storage_observations=0
        self.last_storage_time=None;self.last_storage=None;self.finished=None

    def halt(self,kind,**facts):
        if self.stop is None:
            self.stop=dict(kind=kind,phase=self.label,
                actual_elapsed_seconds=time.monotonic()-self.started,
                actual_work_units=self.attempts,**facts)
        raise F.WorkStop(kind)

    def check(self):
        now=time.monotonic();self.checks+=1;self.checks_since_storage+=1
        if (self.last_storage_time is None or now-self.last_storage_time>=1
                or self.checks_since_storage>=256):
            try:disk=shutil.disk_usage(self.out)
            except OSError as failure:
                self.halt("actual-owned-output-capacity-observation-failed",
                    original_error=dict(type=type(failure).__name__,message=str(failure)))
            self.last_storage=dict(total=disk.total,used=disk.used,free=disk.free,
                required_free_reserve=self.reserve,phase_elapsed_seconds=now-self.started)
            self.storage_observations+=1;self.last_storage_time=now
            self.checks_since_storage=0
            if disk.free<self.reserve:
                self.halt("declared-owned-output-free-reserve-reached",
                    actual_storage=self.last_storage)
        if now-self.started>=self.seconds:
            self.halt("declared-phase-wall-budget-reached",declared_seconds=self.seconds)

    def attempt(self):
        self.check()
        if self.attempts>=self.limit:
            self.halt("declared-phase-work-unit-limit-reached",declared_work_units=self.limit)
        self.attempts+=1

    def finish(self):
        if self.finished is None:self.finished=time.monotonic()

    def elapsed(self):
        return (time.monotonic() if self.finished is None else self.finished)-self.started

    def record(self):
        return dict(phase=self.label,actual_work_units=self.attempts,
            declared_work_units=self.limit,declared_seconds=self.seconds,
            actual_elapsed_seconds=self.elapsed(),phase_finished=self.finished is not None,
            source_binding_and_runtime_setup_excluded_from_phase_clock=True,
            free_bytes_reserve=self.reserve,actual_checks=self.checks,
            storage_observations=self.storage_observations,
            last_actual_storage=self.last_storage,stop=self.stop,
            every_resource_stop_is_partial_scope_not_mathematical_refutation=True)

def numerical_representative(box):
    lo,hi=F.lower_q(box),F.upper_q(box)
    center=(lo+hi)/2
    x=float(center)
    if not math.isfinite(x):raise ArithmeticError("Finite current numeric representative unavailable")
    error=box-B.exact(Q(x))
    return x,dict(actual_word=word(x),exact_real_enclosure=B.record(box),
        difference_exact_quantity_minus_numeric_word=B.record(error),
        representative_need_not_lie_in_the_interval=True,
        representative_is_not_a_selected_exact_root_family_member=True)


class InverseSampler:
    """Complete inverse sets, using both old endpoint primitives and positive D.

    Only dyadic parameter splitting and existing R324 endpoint/range formulas
    are used. No finite 48-step selector, no old node-radius table, no new
    approximate antiderivative is substituted for the original true radius.
    """
    def __init__(self,head,data,args,geometry,ledger,unpaid,budget):
        self.head,self.data,self.args=head,data,args
        self.geometry,self.ledger,self.unpaid,self.budget=geometry,ledger,unpaid,budget
        self.panels=data["panels"];self.cache={};self.leaf_cache={}
        self.lefts=[F.record_bounds(p["radius_left"])[0] for p in self.panels]
        self.rights=[F.record_bounds(p["radius_right"])[1] for p in self.panels]
        self.monotone=(all(a<=b for a,b in zip(self.lefts,self.lefts[1:]))
            and all(a<=b for a,b in zip(self.rights,self.rights[1:])))
        self.point_count=0;self.range_count=0;self.coarse_count=0

    def original_candidates(self,r):
        if self.monotone:
            first=bisect.bisect_left(self.rights,r)
            stop=bisect.bisect_right(self.lefts,r)
            return self.panels[first:stop]
        return [p for p,lo,hi in zip(self.panels,self.lefts,self.rights) if lo<=r<=hi]

    def complete_box(self,panel,lo,hi):
        self.budget.attempt();self.range_count+=1
        piece=self.head.pieces[panel["source_piece"]]
        v=piece.range(lo,hi)
        radius,method=self.geometry.radial_range(panel,lo,hi)
        if not(v["w"]>0 and v["radial_speed"]>0):
            raise ArithmeticError("Complete positive C point geometry not separated")
        logw=v["w"].log()
        log_derivative=v["w_r"]/v["w"]
        F.finite([radius,v["w"],v["w_r"],logw,log_derivative])
        return dict(radius=radius,w=v["w"],w_r=v["w_r"],logw=logw,
            dlogwdr=log_derivative,branches=v["branches"],radius_method=method)

    def work_met(self,v):
        goal=B.p2(-self.args.sample_value_bits)
        for key in ("logw","dlogwdr"):
            q=v[key];scale=max(Q(1),F.abs_upper_q(q))
            if not (q.upper()-q.lower())<=goal*B.exact(scale):return False
        return True

    def sample(self,r_float,role,keep_leaves=False):
        self.budget.check()
        if not math.isfinite(r_float) or r_float<=0:raise ValueError("Positive actual physical radius word required")
        key=struct.pack("<d",r_float).hex()
        if key in self.cache:
            cached=self.cache[key]
            if keep_leaves and key not in self.leaf_cache:raise AssertionError("Required far leaves were not retained")
            return cached
        r=Q(r_float)
        inner=F.record_bounds(self.data["far"]["original_R286_deep_geometry"]["radius"])[1]
        outer=F.record_bounds(self.data["cover"]["natural_outer_radius"])[0]
        if not inner<r<=outer:
            raise ValueError("The actual binary radius is not proved inside every C family source domain")
        roots=self.original_candidates(r)
        if not roots:raise ArithmeticError("A proved radius has no complete original inverse candidates")
        stack=[(p,p["left"],p["right"],0) for p in reversed(roots)]
        retained=[];in_flight=None;start=self.ledger.rows
        try:
            while stack:
                self.budget.check()
                panel,lo,hi,depth=stack.pop();in_flight=(panel,lo,hi,depth)
                try:
                    box=self.complete_box(panel,lo,hi)
                except (ArithmeticError,ZeroDivisionError,OverflowError):
                    if depth>=self.args.sample_inverse_depth:
                        raise
                    mid=(lo+hi)/2
                    stack.extend(((panel,mid,hi,depth+1),(panel,lo,mid,depth+1)))
                    in_flight=None;continue
                if r<F.lower_q(box["radius"]) or r>F.upper_q(box["radius"]):
                    in_flight=None;continue
                met=self.work_met(box)
                if not met and depth<self.args.sample_inverse_depth:
                    mid=(lo+hi)/2
                    stack.extend(((panel,mid,hi,depth+1),(panel,lo,mid,depth+1)))
                    in_flight=None;continue
                row=dict(schema=SCHEMA+"-complete-possible-inverse-leaf",
                    point_index=self.point_count,radius_word=word(r_float),role=role,
                    original_source_panel_row=panel["row"],source_piece=panel["source_piece"],
                    original_cell=159-panel["source_piece"]//9,original_segment=panel["source_piece"]%9,
                    closed_parameter_interval=[str(lo),str(hi)],subdivision_depth=depth,
                    complete_possible_cap_branches=box["branches"],
                    radius_inclusion_method=box["radius_method"],whole_radius_range=B.record(box["radius"]),
                    complete_w=B.record(box["w"]),complete_w_r=B.record(box["w_r"]),
                    complete_logw=B.record(box["logw"]),complete_dlogwdr=B.record(box["dlogwdr"]),
                    every_original_exact_root_choice_included=True,
                    entire_possible_inverse_fragment_retained=True,
                    numerical_work_resolution_met=met,
                    valid_coarse_enclosure_retained=not met)
                number=self.ledger.rows;self.ledger.add(row)
                retained.append(dict(leaf_row=number,source_piece=panel["source_piece"],
                    original_source_panel_row=panel["row"],left=lo,right=hi,box=box,original=row))
                self.coarse_count+=int(not met);in_flight=None
        except Exception as error:
            if in_flight is not None:stack.append(in_flight)
            self.unpaid.add(dict(kind="actual-current-C-physical-point-inverse",
                point_index=self.point_count,radius_word=word(r_float),role=role,
                actual_error_type=type(error).__name__,actual_error=str(error),
                all_pending_closed_fragments=[dict(original_source_panel_row=p["row"],
                    source_piece=p["source_piece"],closed_parameter_interval=[str(a),str(b)],depth=d)
                    for p,a,b,d in reversed(stack)],
                retained_original_leaf_rows=dict(first=start,stop=self.ledger.rows),
                complete_point_not_returned=True))
            raise
        if not retained:raise AssertionError("Complete inverse inclusion lost a proved nonempty point")
        all_boxes={key:B.hull(v["box"][key] for v in retained)
            for key in ("w","w_r","logw","dlogwdr")}
        numerical={};representatives={}
        for name,box in all_boxes.items():
            numerical[name],representatives[name]=numerical_representative(box)
        result=dict(point_index=self.point_count,physical_radius_word=word(r_float),
            numerical=numerical,numerical_word_receipts=representatives,
            all_closed_inverse_leaves=dict(first=start,stop=self.ledger.rows),
            complete_closed_point_inclusion=True,
            work_resolution_complete=all(self.work_met(v["box"]) for v in retained),
            old_finite_inverse_selector_used=False,
            common_exact_global_C_realization_of_all_representatives_certified=False)
        self.point_count+=1
        if keep_leaves:self.leaf_cache[key]=retained
        self.cache[key]=result
        return result


def choose_far_radius(data):
    """One explicit dyadic physical point, not a renamed uncertain C node."""
    target=(159-8)*9+8
    candidates=[p for p in data["panels"] if p["source_piece"]==target and p["right"]==1]
    if len(candidates)!=1:raise ValueError("Actual complete source cell8 outer boundary absent")
    boundary=candidates[0]
    upper=F.record_bounds(boundary["radius_right"])[1]
    x=float(upper)
    if not math.isfinite(x) or x<=0:raise ArithmeticError("A positive finite native far radius is unavailable")
    if Q(x)<=upper:x=math.nextafter(x,math.inf)
    if not Q(x)>upper:raise AssertionError("The explicit far word did not lie beyond the entire node8 radius box")
    cut=float(data["cut"])
    if not Q(x)<data["cut"]:raise ArithmeticError("Current finite far and original cut do not leave a positive radial interval")
    return x,dict(schema=SCHEMA+"-explicit-physical-far-choice",
        source_piece=target,original_source_panel_row=boundary["row"],
        original_cell=8,original_segment=8,original_parameter="1",
        uncertain_original_node_radius=boundary["radius_right"],
        rule="next binary64 strictly greater than complete node8 radius upper endpoint",
        physical_far_word=word(x),original_binary_cut_word=word(cut),
        radius_not_claimed_equal_to_original_uncertain_node=True,
        whole_C_family_source_domain_rechecked=True,
        no_height_column_division_used=True)


def finite_point_required(data,leaves):
    by_panel={}
    for leaf in leaves:
        row=leaf["original_source_panel_row"]
        p=data["panels"][row]
        if p["source_piece"]!=leaf["source_piece"] or not p["left"]<=leaf["left"]<leaf["right"]<=p["right"]:
            raise ValueError("All far inverse fragments must retain their true original panel")
        by_panel.setdefault(row,[]).append(leaf)
    last=max(by_panel);last_right=max(x["right"] for x in by_panel[last])
    required=[]
    for panel in data["panels"][:last+1]:
        hi=last_right if panel["row"]==last else panel["right"]
        required.append(dict(panel=panel,left=panel["left"],right=hi))
    return by_panel,required,dict(last_original_source_panel_row=last,
        after_last_parameter=str(last_right),unneeded_source_panel_suffix=[last+1,len(data["panels"])],
        original_full_source_bytes_remain_bound=True)


def squared_interval_bounds(value):
    """Exact rational squared-range endpoints, without a rounded midpoint."""
    lo,hi=F.lower_q(value),F.upper_q(value)
    minimum=Q(0) if lo<=0<=hi else min(lo*lo,hi*hi)
    maximum=max(lo*lo,hi*hi)
    return minimum,maximum


def oriented_unit_far_row(height,k,w,r_far,mu,mode,amplitude_sign):
    """Enclose the original Q_F=1 Robin row after positive norm scaling.

    The input height and k are divided by one common nonzero panel amplitude.
    Its certified sign restores the original orientation. No height is divided.
    Each candidate is normalized before any cross-candidate hull is formed.
    """
    if amplitude_sign not in (-1,1):
        raise ValueError("A proved nonzero original amplitude sign is required")
    if not w>0:raise ArithmeticError("Same complete candidate w must be positive")
    r=B.exact(Q(r_far));muw=B.exact(Q(mu))
    if not (r>0 and muw>0):
        raise ArithmeticError("Positive actual radius and momentum scale words required")
    aa=-k*r**4+height*mode*mode*r**3
    bb=height*B.exact(12).sqrt()*muw/(r**4*w)
    F.finite([aa,bb])
    maximum=max(F.abs_upper_q(aa),F.abs_upper_q(bb))
    power=F.floor_log2(maximum) if maximum>0 else 0
    scaled=[aa*B.p2(-power),bb*B.p2(-power)]
    lower=[];upper=[]
    for value in scaled:
        a,b=squared_interval_bounds(value);lower.append(a);upper.append(b)
    norm_square_lower=sum(lower,Q(0));norm_square_upper=sum(upper,Q(0))
    proved=norm_square_lower>0
    norm=B.interval(norm_square_lower,norm_square_upper).sqrt()
    F.finite(scaled+[norm])
    units=None
    if proved:
        if not norm>0:
            raise ArithmeticError("The positive exact squared lower bound was lost in the norm enclosure")
        units=[B.exact(amplitude_sign)*x/norm for x in scaled]
        F.finite(units)
    receipt=dict(schema=SCHEMA+"-oriented-unit-Robin-candidate",
        physical_frequency=mode,physical_radius_word=word(r_far),mu_word=word(mu),
        original_coordinate_order=["Q","Pi"],
        exact_coordinate_rule="(-k*r^4+u*m^2*r^3, u*sqrt(12)*mu/(r^4*w))",
        candidate_common_amplitude_sign=amplitude_sign,
        complete_homogeneous_Q_coefficient=B.record(aa),
        complete_homogeneous_Pi_coefficient=B.record(bb),
        exact_positive_row_power_of_two_removed=power,
        complete_scaled_homogeneous_coefficients=[B.record(x) for x in scaled],
        exact_squared_norm_lower=str(norm_square_lower),
        exact_squared_norm_upper=str(norm_square_upper),
        complete_scaled_row_norm=B.record(norm),
        complete_row_norm_strictly_positive_proved=proved,
        unit_orientation_rule="sign(actual_panel_amplitude) * scaled_R / norm(scaled_R)",
        complete_original_QF_one_unit_row=(
            [B.record(x) for x in units] if units is not None else None),
        division_by_physical_height=False,
        all_candidates_need_not_share_a_nonzero_component=True,
        different_candidate_amplitudes_not_hulled_as_original_columns=True,
        no_point_of_the_unit_row_box_claimed_to_be_a_realized_global_C_choice=True)
    return units,receipt


def prepare_far_tubes(candidate,coeff,panel,lo,hi,leaves,mode,coverage,
                      transaction_index,r_far,mu):
    if not coeff["w"]>0:raise ArithmeticError("Complete same-C candidate w must be positive")
    framed=candidate["framed"];u,j0=candidate["tube"]
    j=B.p2(framed["balance_power"])*j0
    k=j/coeff["w"];F.finite([u,j,k])
    matches=[]
    for leaf in leaves:
        left,right=max(lo,leaf["left"]),min(hi,leaf["right"])
        if left<=right:matches.append((leaf,left,right))
    if not matches:return [],[],{}
    units,normalization=oriented_unit_far_row(
        u,k,coeff["w"],r_far,mu,mode,framed["amplitude_sign"])
    amplitude=dict(sign=framed["amplitude_sign"],
        log_absolute_value=B.record(framed["amplitude_logabs"]),
        prior_factor_count=framed["factor_count"],
        prior_factor_chain_sha256=framed["factor_chain_sha256"],
        pending_exact_power_of_two=framed["pending_exact_amplitude_power_of_two"],
        exact_semantics="a_f=a_at_incoming_endpoint*2^pending_power",
        amplitude_nonzero_and_sign_proved_separately_from_row_norm=True)
    rows,values,updates=[],[],{}
    for leaf,left,right in matches:
        old=coverage.get(leaf["leaf_row"])
        if old is None:
            if left!=leaf["left"]:
                raise ValueError("A possible physical-far inverse leaf lost its initial closed interval")
            update=dict(left=left,right=right,candidate_count=0,unit_rows=0,norm_unproved=0)
        else:
            if left>old["right"]:raise ValueError("A possible physical-far inverse leaf has a gap")
            update=dict(old,right=max(old["right"],right))
        update["candidate_count"]+=1;update["unit_rows"]+=int(units is not None)
        update["norm_unproved"]+=int(units is None)
        updates[leaf["leaf_row"]]=update
        rows.append(dict(schema=SCHEMA+"-physical-far-projective-tube",
            physical_frequency=mode,transaction_index=transaction_index,
            physical_far_word=word(r_far),mu_word=word(mu),
            possible_inverse_leaf_row=leaf["leaf_row"],
            original_source_panel_row=panel["row"],source_piece=panel["source_piece"],
            closed_step_interval=[str(lo),str(hi)],closed_leaf_intersection=[str(left),str(right)],
            coefficient_row=coeff["coefficient_row"],
            complete_normalized_tube=[B.record(u),B.record(j0)],
            fixed_flux_balance_power_of_two=framed["balance_power"],
            normalized_physical_height=B.record(u),normalized_physical_flux=B.record(j),
            normalized_physical_k=B.record(k),same_complete_candidate_w=B.record(coeff["w"]),
            original_column_nonzero_panel_amplitude=amplitude,
            original_QF_one_column_materialized=False,
            complete_original_uncertainty_retained=True,
            unit_row_normalization=normalization,
            same_closed_endpoint_not_discarded=True))
        values.append(units)
    return rows,values,updates


def point_column(far,data,required,by_panel,geometry,args,budget,steps,tubes,
                 commits,coverage_journal,unpaid,r_far,mu):
    """Whole R347 two-chart propagation to the explicit physical far point."""
    m=far["physical_frequency"];state,initial=F.initial_column(far,data)
    coverage={};unit_hull=None;accepted=coarse=candidate_count=unit_count=0
    norm_splits=defect_splits=range_splits=pivot_splits=row_norm_splits=0
    stack=[];index=0;in_flight=None;error=None;last_paid=None
    last_unaccepted=None;transaction_open=None
    first_step,first_tube=steps.rows,tubes.rows
    first_commit,first_coverage=commits.rows,coverage_journal.rows
    committed_step_stop,committed_tube_stop=first_step,first_tube
    try:
        for index,item in enumerate(required):
            panel=item["panel"];stack=[(item["left"],item["right"],0)]
            while stack:
                budget.attempt();lo,hi,depth=stack.pop();in_flight=(lo,hi,depth)
                can_split=depth<args.max_depth and lo<hi
                try:
                    coeff=geometry.get(panel,lo,hi)
                    candidate=F.advance_candidate(state,coeff,m,lo,hi,args)
                except (ArithmeticError,ZeroDivisionError,OverflowError) as failure:
                    last_unaccepted=dict(original_source_panel_row=panel["row"],
                        closed_parameter_interval=[str(lo),str(hi)],subdivision_depth=depth,
                        incoming_factorized_state=F.state_record(state),
                        error=dict(type=type(failure).__name__,message=str(failure)))
                    if can_split:
                        mid=(lo+hi)/2;stack.extend(((mid,hi,depth+1),(lo,mid,depth+1)))
                        range_splits+=1;in_flight=None;continue
                    raise F.PanelUnpaid("Complete physical-far coefficient/exponential enclosure unresolved: "+str(failure))
                if candidate["needs_norm_split"] or candidate.get("needs_pivot_split"):
                    last_unaccepted=dict(original_source_panel_row=panel["row"],
                        closed_parameter_interval=[str(lo),str(hi)],subdivision_depth=depth,
                        incoming_factorized_state=F.state_record(state),
                        candidate=F.candidate_record(candidate))
                    if can_split:
                        mid=(lo+hi)/2;stack.extend(((mid,hi,depth+1),(lo,mid,depth+1)))
                        norm_splits+=int(candidate["needs_norm_split"])
                        pivot_splits+=int(not candidate["needs_norm_split"])
                        in_flight=None;continue
                    if candidate["needs_norm_split"]:
                        raise F.PanelUnpaid("Complete physical-far panel norm work bound unresolved")
                    raise F.PanelUnpaid("Neither complete physical-far endpoint component excludes zero")
                if not candidate["work_goal_met"] and can_split:
                    mid=(lo+hi)/2;stack.extend(((mid,hi,depth+1),(lo,mid,depth+1)))
                    defect_splits+=1;in_flight=None;continue
                try:
                    far_rows,unit_values,updates=prepare_far_tubes(
                        candidate,coeff,panel,lo,hi,by_panel.get(panel["row"],[]),
                        m,coverage,accepted,r_far,mu)
                except (ArithmeticError,ZeroDivisionError,OverflowError) as failure:
                    last_unaccepted=dict(original_source_panel_row=panel["row"],
                        closed_parameter_interval=[str(lo),str(hi)],subdivision_depth=depth,
                        incoming_factorized_state=F.state_record(state),
                        error=dict(type=type(failure).__name__,message=str(failure)))
                    if can_split:
                        mid=(lo+hi)/2;stack.extend(((mid,hi,depth+1),(lo,mid,depth+1)))
                        range_splits+=1;in_flight=None;continue
                    raise F.PanelUnpaid("Complete physical-far homogeneous row enclosure unresolved: "+str(failure))
                if any(value is None for value in unit_values) and can_split:
                    last_unaccepted=dict(original_source_panel_row=panel["row"],
                        closed_parameter_interval=[str(lo),str(hi)],subdivision_depth=depth,
                        candidate_row_norm_conditions=[row["unit_row_normalization"] for row in far_rows],
                        incoming_factorized_state=F.state_record(state))
                    mid=(lo+hi)/2;stack.extend(((mid,hi,depth+1),(lo,mid,depth+1)))
                    row_norm_splits+=1;in_flight=None;continue
                before=F.state_record(state)
                step=dict(schema=SCHEMA+"-prepared-projective-far-panel",
                    physical_frequency=m,physical_far_word=word(r_far),transaction_index=accepted,
                    original_source_panel_row=panel["row"],source_piece=panel["source_piece"],
                    closed_parameter_interval=[str(lo),str(hi)],subdivision_depth=depth,
                    original_complete_incoming_state=before,coefficient_row=coeff["coefficient_row"],
                    complete_projective_enclosure=F.candidate_record(candidate),
                    commit_required_before_this_row_belongs_to_the_paid_prefix=True)
                new_hull=unit_hull;new_candidate_count=candidate_count;new_unit_count=unit_count
                for units in unit_values:
                    new_candidate_count+=1
                    if units is not None:
                        new_unit_count+=1
                        new_hull=(list(units) if new_hull is None
                            else [old.union(value) for old,value in zip(new_hull,units)])
                new_coverage=dict(coverage);new_coverage.update(updates)
                new_last_paid=dict(original_source_panel_row=panel["row"],
                    source_piece=panel["source_piece"],parameter=str(hi),
                    complete_factorized_state=F.state_record(candidate["next_state"]),
                    panel_commit_row=commits.rows)
                coarse_increment=int(not candidate["work_goal_met"])
                step_sha=F.sha(F.canonical(step));step_row=steps.rows;tube_first=tubes.rows
                transaction_open=dict(transaction_index=accepted,
                    original_source_panel_row=panel["row"],closed_parameter_interval=[str(lo),str(hi)],
                    prepared_panel_row=step_row,
                    prepared_far_rows=dict(first=tube_first,stop=tube_first+len(far_rows)),
                    prior_complete_state=before,
                    candidate_outgoing_state=F.state_record(candidate["next_state"]))
                budget.check()
                steps.add(step)
                for row in far_rows:
                    row["prepared_panel_row"]=step_row;tubes.add(row)
                commits.add(dict(schema=SCHEMA+"-committed-projective-far-panel",
                    physical_frequency=m,transaction_index=accepted,
                    prepared_panel_row=step_row,prepared_panel_canonical_sha256=step_sha,
                    far_contribution_span=dict(first=tube_first,stop=tubes.rows),
                    complete_outgoing_factor_chain_sha256=candidate["next_state"]["factor_chain_sha256"],
                    all_prepared_rows_precede_this_commit=True))
                # Commit is the final write. No resource check or scientific
                # operation intervenes before this prepared state is installed.
                state=candidate["next_state"];coverage=new_coverage;unit_hull=new_hull
                candidate_count=new_candidate_count;unit_count=new_unit_count
                accepted+=1;coarse+=coarse_increment
                committed_step_stop=steps.rows;committed_tube_stop=tubes.rows
                last_paid=new_last_paid;transaction_open=None;in_flight=None;last_unaccepted=None
            index+=1
        for leaves in by_panel.values():
            for leaf in leaves:
                covered=coverage.get(leaf["leaf_row"])
                if covered is None or (covered["left"],covered["right"])!=(leaf["left"],leaf["right"]):
                    raise ValueError("A complete possible physical-far inverse leaf was not covered")
        if candidate_count==0:raise AssertionError("Complete far propagation has no inverse contribution")
    except Exception as failure:
        if in_flight is not None and in_flight not in stack:stack.append(in_flight)
        error=dict(type=type(failure).__name__,message=str(failure))
    pending=F.pending_description(required,index,stack) if error is not None else None
    spatial_complete=error is None
    completed_leaves=0;required_leaf_count=0
    for leaves in by_panel.values():
        for leaf in leaves:
            required_leaf_count+=1;covered=coverage.get(leaf["leaf_row"])
            paid=covered is not None and (covered["left"],covered["right"])==(leaf["left"],leaf["right"])
            completed_leaves+=int(paid)
            coverage_journal.add(dict(schema=SCHEMA+"-physical-far-inverse-leaf-coverage",
                physical_frequency=m,physical_far_word=word(r_far),
                possible_inverse_leaf_row=leaf["leaf_row"],source_piece=leaf["source_piece"],
                required_closed_parameter_interval=[str(leaf["left"]),str(leaf["right"])],
                committed_covered_closed_interval=(
                    [str(covered["left"]),str(covered["right"])] if covered else None),
                complete_original_inverse_leaf_spatial_scope_paid=paid,
                committed_candidate_count=covered["candidate_count"] if covered else 0,
                complete_unit_row_count=covered["unit_rows"] if covered else 0,
                unit_row_norm_unproved_count=covered["norm_unproved"] if covered else 0,
                same_closed_endpoint_retained=True))
    row_ready=bool(spatial_complete and candidate_count>0 and unit_count==candidate_count and unit_hull is not None)
    if error is not None:
        unpaid.add(dict(kind="current-physical-far-projective-mode",
            physical_frequency=m,physical_far_word=word(r_far),error=error,last_paid=last_paid,
            complete_pending_scope=pending,complete_current_state=F.state_record(state),
            last_unaccepted_candidate=last_unaccepted,uncommitted_transaction=transaction_open,
            entire_mode_spatial_scope_remains_partial=True,
            original_QF_one_column_not_materialized=True))
    if spatial_complete and not row_ready:
        unpaid.add(dict(kind="complete-physical-far-family-with-unpaid-unit-row-norm",
            physical_frequency=m,physical_far_word=word(r_far),
            complete_family_candidate_count=candidate_count,complete_unit_row_count=unit_count,
            row_norm_unproved_count=candidate_count-unit_count,
            committed_far_tube_rows=dict(first=first_tube,stop=committed_tube_stop),
            complete_original_leaf_coverage_rows=dict(first=first_coverage,stop=coverage_journal.rows),
            complete_projective_family_retained=True,
            interval_zero_not_claimed_actual_resonance_or_zero_column=True))
    return dict(schema=SCHEMA+"-complete-physical-far-mode",
        physical_frequency=m,mode_index=far["mode_index"],
        initial_R312_factorized_column=initial,complete=row_ready,
        complete_required_far_propagation=spatial_complete,
        complete_unit_row_family_enclosed=row_ready,error=error,
        physical_far_word=word(r_far),mu_word=word(mu),
        whole_candidate_unit_row_hull=(
            [B.record(v) for v in unit_hull] if row_ready else None),
        partial_legal_unit_row_hull=(
            [B.record(v) for v in unit_hull] if unit_hull is not None else None),
        partial_hull_is_not_complete_family_unless_all_candidate_conditions_paid=True,
        full_interval_objects=dict(unit_row=unit_hull) if row_ready else None,
        candidate_count=candidate_count,complete_unit_row_count=unit_count,
        row_norm_unproved_count=candidate_count-unit_count,
        complete_step_rows=dict(first=first_step,stop=committed_step_stop),
        complete_far_tube_rows=dict(first=first_tube,stop=committed_tube_stop),
        complete_panel_commit_rows=dict(first=first_commit,stop=commits.rows),
        complete_far_leaf_coverage_rows=dict(first=first_coverage,stop=coverage_journal.rows),
        uncommitted_written_step_span=dict(first=committed_step_stop,stop=steps.rows),
        uncommitted_written_far_span=dict(first=committed_tube_stop,stop=tubes.rows),
        required_leaf_count=required_leaf_count,completed_leaf_count=completed_leaves,
        last_paid=last_paid,complete_current_factorized_state=F.state_record(state),
        complete_pending_scope=pending,last_unaccepted_candidate=last_unaccepted,
        uncommitted_transaction=transaction_open,accepted_panels=accepted,valid_coarse_panels=coarse,
        coefficient_range_splits=range_splits,norm_work_splits=norm_splits,
        defect_work_splits=defect_splits,uncertain_endpoint_pivot_splits=pivot_splits,
        uncertain_far_row_norm_splits=row_norm_splits,
        division_by_height_performed=False,
        division_flag_scope="far Robin row only; endpoint charts may normalize either strictly nonzero component",
        original_QF_one_column_materialized=False,
        all_original_root_choices_included=True,exact_global_family_member_not_selected=True,
        all_numeric_far_rows_pending_until_complete112_and_word_binding=True)


def radial_grid(r_far,r_cut,steps):
    """Explicit finite sampling grid; not an old stored C radius/port schedule."""
    if not(0<r_far<r_cut) or steps<=0:raise ValueError("A positive ordered actual radial grid is required")
    a,b=math.log(r_far),math.log(r_cut)
    nodes=[math.exp(b+(a-b)*(n/DEPTH)) for n in range(DEPTH+1)]
    nodes[0]=r_cut;nodes[-1]=r_far
    if any(not(math.isfinite(r) and r>0) for r in nodes) or not all(x>y for x,y in zip(nodes,nodes[1:])):
        raise ArithmeticError("The chosen complete finite radial grid is not representably strictly ordered")
    h=1.0/steps
    xs={struct.pack("<d",0.0).hex():0.0,struct.pack("<d",1.0).hex():1.0}
    for k in range(steps):
        x=k/steps
        for y in (x,x+h/2,x+h):
            xs[struct.pack("<d",y).hex()]=y
    for k in range(steps+1):
        x=k/steps;xs[struct.pack("<d",x).hex()]=x
    ordered=sorted(xs.values())
    plan=[]
    for n in range(DEPTH):
        left,right=nodes[n+1],nodes[n];dr=right-left
        if not(math.isfinite(dr) and dr>0):raise ArithmeticError("Actual finite stage radial speed was lost")
        fields=[]
        for x in ordered:
            r=left if x==0 else right if x==1 else left+dr*x
            if not(math.isfinite(r) and r>0):raise ArithmeticError("Actual RK field radius is not finite positive")
            # Original x+h rounding can put a field just beyond the nominal endpoint.
            # Do not clip or replace that word: the sampler separately checks the
            # actual radius against the complete C domain and encloses that point.
            fields.append(dict(x_word=word(x),r_word=word(r),drdx_word=word(dr)))
        plan.append(dict(stage=n,rawCell=n//72,rawSegment=(n%72)//8,
            shootingSubsegment=n%8,fields=fields))
    return nodes,plan,dict(
        schema=SCHEMA+"-explicit-finite-radial-grid",mode_count=M,depth=DEPTH,
        physical_radius_domain=[word(r_far),word(r_cut)],node_count=DEPTH+1,
        node_generation="binary64 exp(log(cut)+(log(far)-log(cut))*n/576), endpoints original exact words",
        rawNode=[72*i for i in range(9)],old_source_piece_partition_reused=False,
        stage_parameter="outward affine physical radius; all actual RK/audit argument words explicitly enumerated",
        steps_per_stage=steps,all_RK4_midpoint_and_endpoint_words_included=True,
        every_actual_rounded_field_radius_checked_against_original_C_domain=True,
        rounded_outside_nominal_grid_endpoints_not_clipped=True,
        numerical_discretization_is_new_and_explicit=True)


def momentum_rows(rows,r_far,far_sample,mu):
    """Only already complete, consistently oriented unit-row families are hulled."""
    result=[];matrix=[]
    for index,row in enumerate(rows):
        m=2*(index+1)
        if (row["physical_frequency"]!=m or not row["complete_unit_row_family_enclosed"]
                or row["physical_far_word"]["f64le"]!=word(r_far)["f64le"]
                or row["mu_word"]["f64le"]!=word(mu)["f64le"]):
            raise ValueError("Actual complete112 row, radius or momentum-coordinate identity differs")
        an,bn=row["full_interval_objects"]["unit_row"];F.finite([an,bn])
        av,ar=numerical_representative(an);bv,br=numerical_representative(bn)
        if av==0 and bv==0:
            raise ArithmeticError("Both explicit unit-row representatives rounded to zero; no numeric boundary fabricated")
        values=[0.0]*K;values[index]=av;values[M+index]=bv;matrix.extend(values)
        result.append(dict(physical_frequency=m,physical_radius_word=word(r_far),mu_word=word(mu),
            original_common_orientation="unit row of the original Q_F=1 propagated column",
            complete_original_QF_one_unit_row=[B.record(an),B.record(bn)],
            complete_Q_coefficient=ar,complete_Pi_coefficient=br,
            normalization_rule="each candidate sign(a_f)*R/norm(R), then complete candidate hull",
            original_QF_one_column_materialized=False,
            every_candidate_amplitude_nonzero_and_sign_proved=True,
            every_candidate_Robin_row_norm_strictly_positive_proved=True,
            candidate_count=row["candidate_count"],
            complete_far_tube_rows=row["complete_far_tube_rows"],
            complete_far_leaf_coverage_rows=row["complete_far_leaf_coverage_rows"],
            division_by_far_physical_height=False,
            endpoint_chart_normalization_may_use_either_proved_nonzero_component=True,
            different_original_column_scales_never_directly_hulled=True,
            selected_numeric_row_is_not_an_exact_family_member=True,
            simultaneous_global_C_realization_of_numeric_rows_certified=False,
            arbitrary_numeric_row_not_claimed_to_have_unit_length_exactly=True))
    if len(result)!=M:raise ValueError("Every original physical frequency is required")
    return matrix,result


def raw_array(path,values,shape):
    if len(values)!=math.prod(shape):raise AssertionError("Complete original raw array shape differs")
    h=hashlib.sha256();count=0
    with Path(path).open("xb") as stream:
        for x in values:
            if not math.isfinite(x):raise ArithmeticError("A declared finite native array is nonfinite")
            raw=struct.pack("<d",x);stream.write(raw);h.update(raw);count+=8
        stream.flush();os.fsync(stream.fileno())
    return dict(file="large-arrays/"+Path(path).name,bytes=count,sha256=h.hexdigest(),
        dtype="<f8",order="C",shape=shape,completed=True)


def parser():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--cover-directory",type=Path,required=True)
    p.add_argument("--cover-result-sha256",required=True)
    p.add_argument("--far-directory",type=Path,required=True)
    p.add_argument("--far-result-sha256",required=True)
    p.add_argument("--code-directory",type=Path,required=True)
    p.add_argument("--proof",type=Path,required=True)
    p.add_argument("--unit-row-proof",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--precision-bits",type=int,default=256)
    p.add_argument("--linear-budget-seconds",type=float,required=True)
    p.add_argument("--sampling-budget-seconds",type=float,required=True)
    p.add_argument("--max-panels",type=int,default=25000000)
    p.add_argument("--free-bytes-reserve",type=int,default=2147483648)
    p.add_argument("--max-depth",type=int,default=32)
    p.add_argument("--local-defect-bits",type=int,default=12)
    p.add_argument("--panel-norm-limit",type=Q,default=Q(1,2))
    p.add_argument("--taylor-terms",type=int,default=24)
    p.add_argument("--max-geometry-cache-records",type=int,default=65536)
    p.add_argument("--sample-max-nodes",type=int,default=200000)
    p.add_argument("--sample-inverse-depth",type=int,default=24)
    p.add_argument("--sample-value-bits",type=int,default=32)
    p.add_argument("--steps",type=int,required=True)
    return p


def main(argv=None):
    require_actions();args=parser().parse_args(argv)
    if args.out.exists():raise FileExistsError("Fresh exclusively owned sampling output required")
    if args.steps<=0 or not 64<=args.precision_bits<=4096 or args.max_panels<=0:
        raise ValueError("Use explicit complete finite numerical controls")
    for x in (args.linear_budget_seconds,args.sampling_budget_seconds):
        if not math.isfinite(x) or x<=0:raise ValueError("Positive explicit resource budget required")
    if not(0<=args.max_depth<=60 and 0<=args.sample_inverse_depth<=60 and
           0<=args.sample_value_bits<=1024 and 0<=args.local_defect_bits<=1024 and
           1<=args.taylor_terms<=256 and 0<args.panel_norm_limit<=16 and
           args.max_geometry_cache_records>0 and args.sample_max_nodes>0 and args.free_bytes_reserve>=0):
        raise ValueError("Declared finite source controls out of range")
    args.out.mkdir(parents=True);large=args.out/"large-arrays";large.mkdir()
    started=time.monotonic();report=dict(schema=SCHEMA,source_sha256=sha(Path(__file__).read_bytes()),
        target_model_schema=MODEL,repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"],completed=False,native_geometry_ready=False,
        error=None,old_graphs_or_gains_used=False,no_height_division_in_far_rows=True,
        exact_global_C_realization_of_numeric_representatives_certified=False,
        nonlinear_solve_or_DN_computed=False,closed_field_or_BVP_accepted=False)
    journals={};exit_code=2;rows=[];point_index=0;grid=None;sampler=None;linear=None;sampling=None
    sampling_paused_for_linear=False
    try:
        runtime,sources,proof=load_runtime(args)
        data=F.bind_inputs(args)
        report.update(runtime=runtime,frozen_sources=sources,actual_R347_proof=proof["projective_propagation"],actual_R357_proof=proof["oriented_unit_Robin_rows"],
            actual_original_input_binding=data["binding"],
            actual_original_scope_conditions=data["facts"])
        for name in ("coefficient-boxes","sample-inverse-leaves","complete-unpaid-scope",
                     "far-accepted-panels","far-complete-tubes","far-all-mode-rows",
                     "far-panel-commits","far-inverse-leaf-coverage",
                     "numeric-point-values-and-errors"):
            journals[name]=B.Journal(large/(name+".jsonl"),args.out)
        unpaid=journals["complete-unpaid-scope"]
        if not data["ready"]:
            unpaid.add(dict(kind="whole-current-C-native-geometry",all_required_modes=list(F.MODES),
                actual_original_scope_conditions=data["facts"],all_native_stages_unstarted=[0,DEPTH],
                no_missing_source_piece_or_cut_domain_assumed=True))
        else:
            cb=data["core"]
            head=B.ContinuousHead(cb["physical_parameters"],cb["original_shallow_rows"],
                cb["original_frozen_warp_alpha"],cb)
            r_far,far_choice=choose_far_radius(data);r_cut=float(data["cut"])
            report["actual_far_radius_choice"]=far_choice
            sampling=OwnedBudget(args.sampling_budget_seconds,args.sample_max_nodes,"C physical-point sampling",
                args.out,args.free_bytes_reserve)
            geom=F.GeometryCache(head,data["panels"],args,journals["coefficient-boxes"],sampling)
            sampler=InverseSampler(head,data,args,geom,journals["sample-inverse-leaves"],unpaid,sampling)
            far_sample=sampler.sample(r_far,"explicit-finite-physical-far",True)
            report["far_point_sample"]=far_sample
            mu_far=math.exp(7*math.log(r_far)+far_sample["numerical"]["logw"])
            if not(math.isfinite(mu_far) and mu_far>0):
                raise ArithmeticError("Actual far momentum-coordinate word is not finite positive")
            report["actual_far_coordinate_mu_word"]=word(mu_far)
            far_leaves=sampler.leaf_cache[struct.pack("<d",r_far).hex()]
            by_panel,required,after=finite_point_required(data,far_leaves)
            report["finite_far_required_prefix"]=emit(args.out/"required-source-panels.json",
                dict(actual_physical_radius=word(r_far),all_possible_inverse_leaves_included=True,
                    original_complete_source_stream=data["cover"]["ledgers"]["source_radial_panels"],
                    required=[dict(original_source_panel_row=x["panel"]["row"],
                        source_piece=x["panel"]["source_piece"],
                        closed_parameter_interval=[str(x["left"]),str(x["right"])]) for x in required],
                    complete_not_needed_outer_suffix=after))
            linear=OwnedBudget(args.linear_budget_seconds,args.max_panels,"C explicit projective finite-far propagation",
                args.out,args.free_bytes_reserve)
            geom.budget=linear;sampling_paused_for_linear=True
            for far in data["far_rows"]:
                linear.check()
                row=point_column(far,data,required,by_panel,geom,args,linear,
                    journals["far-accepted-panels"],journals["far-complete-tubes"],
                    journals["far-panel-commits"],journals["far-inverse-leaf-coverage"],unpaid,r_far,mu_far)
                rows.append(row)
                journals["far-all-mode-rows"].add({k:v for k,v in row.items() if k!="full_interval_objects"})
                print(json.dumps(dict(event="current_C_nondividing_far_mode",
                    physical_frequency=far["physical_frequency"],complete=row["complete"],
                    error=row["error"],accepted_panels=row["accepted_panels"],
                    elapsed_seconds=time.monotonic()-linear.started)),flush=True)
                if not row["complete_required_far_propagation"]:break
            linear.finish()
            report["far_completed_modes"]=[r["physical_frequency"] for r in rows if r["complete"]]
            if len(rows)!=M or not all(r["complete"] for r in rows):
                unpaid.add(dict(kind="complete-finite-far-unstarted-mode-suffix",
                    remaining_modes=list(F.MODES[len(rows):]),all_required_modes=list(F.MODES),
                    complete_native_geometry_not_returned=True,
                    attempted_modes_with_unpaid_unit_rows=[r["physical_frequency"] for r in rows if not r["complete"]]))
            else:
                # Sampling receives its own explicit elapsed phase after propagation.
                # The already used sampling time remains charged; no hidden budget reset.
                sampling.started+=linear.elapsed();sampling_paused_for_linear=False
                geom.budget=sampling
                far_matrix,far_rows=momentum_rows(rows,r_far,far_sample,mu_far)
                row_receipt=emit(args.out/"actual-general-far-row-intervals-and-representatives.json",dict(
                    schema=SCHEMA+"-all112-general-far-rows",physical_radius_word=word(r_far),
                    complete_rows=far_rows,old_graph_or_height_division_used=False,
                    exact_unit_row_orientation_and_all_candidate_dependencies_retained=True))
                nodes,grid,grid_identity=radial_grid(r_far,r_cut,args.steps)
                report["grid_identity"]=grid_identity
                plan_receipt=emit(args.out/"actual-radial-field-plan.json",dict(
                    schema=SCHEMA+"-complete-field-plan",grid_identity=grid_identity,
                    nodes=[word(v) for v in nodes],stages=grid))
                numeric_nodes=[];mu=[]
                for n,r in enumerate(nodes):
                    s=sampler.sample(r,"actual-node-"+str(n))
                    numeric_nodes.append(s)
                    value=math.exp(7*math.log(r)+s["numerical"]["logw"])
                    if not(math.isfinite(value) and value>0):
                        raise ArithmeticError("Declared numerical coordinate mu is not finite positive at node "+str(n))
                    mu.append(value)
                if word(mu[-1])["f64le"]!=word(mu_far)["f64le"]:
                    raise AssertionError("The original node-far coordinate expression changed its actual word")
                stage_packets=[]
                field_words=[];field_width=None
                for n,stage in enumerate(grid):
                    sampling.check()
                    packet=dict(stage=n,rawCell=stage["rawCell"],rawSegment=stage["rawSegment"],
                        shootingSubsegment=stage["shootingSubsegment"],fields=[],
                        mu_word=word(mu[n+1]),output_node_mu_word=word(mu[n]),
                        port_ratio_word=word(mu[n]/mu[n+1]))
                    if not(math.isfinite(mu[n]/mu[n+1]) and mu[n]/mu[n+1]>0):
                        raise ArithmeticError("Actual complete momentum port ratio unavailable")
                    for entry in stage["fields"]:
                        s=sampler.sample(entry["r_word"]["value"],"stage-"+str(n)+"-field")
                        logw=s["numerical"]["logw"]
                        dlog=entry["drdx_word"]["value"]*s["numerical"]["dlogwdr"]
                        if not math.isfinite(dlog):raise ArithmeticError("Actual finite dlogwdx overflow")
                        true_dlogwdx=B.exact(Q(entry["drdx_word"]["value"]))*F.as_ball(
                            s["numerical_word_receipts"]["dlogwdr"]["exact_real_enclosure"])
                        record=dict(stage=n,x_word=entry["x_word"],r_word=entry["r_word"],
                            drdx_word=entry["drdx_word"],logw_word=word(logw),dlogwdx_word=word(dlog),
                            same_C_sample=s,complete_target_dlogwdx=B.record(true_dlogwdx),
                            target_dlogwdx_minus_actual_numeric_word=B.record(true_dlogwdx-B.exact(Q(dlog))),
                            finite_derived_dlogwdx_rounding_not_an_exact_derivative_identity=True)
                        journals["numeric-point-values-and-errors"].add(record)
                        packet["fields"].append(dict(x_word=entry["x_word"],point_index=s["point_index"]))
                        field_words.extend([entry["x_word"]["value"],entry["r_word"]["value"],
                            entry["drdx_word"]["value"],logw,dlog])
                        point_index+=1
                    if field_width is None:field_width=len(stage["fields"])
                    if field_width!=len(stage["fields"]):raise AssertionError("Complete stage sampling width differs")
                    stage_packets.append(packet)
                arrays=dict(
                    node_radii=raw_array(large/"node-radii.f64le",nodes,[DEPTH+1]),
                    node_mu=raw_array(large/"node-mu.f64le",mu,[DEPTH+1]),
                    field_geometry=raw_array(large/"full-stage-field-geometry.f64le",
                        field_words,[DEPTH,field_width,5]),
                    far_matrix=raw_array(large/"complete-general-far-matrix.f64le",far_matrix,[M,K]))
                geometry_identity=dict(schema=SCHEMA+"-numeric-geometry-identity",
                    sampler_source_sha256=report["source_sha256"],actual_source_binding=data["binding"],
                    original_C_model=MODEL,actual_radial_field_plan=plan_receipt,
                    all_point_enclosures_and_representative_errors=journals["numeric-point-values-and-errors"].finish(),
                    general_far_row_enclosures_and_representatives=row_receipt,
                    complete_native_arrays=arrays,
                    exact_global_C_realization_of_numeric_representatives_certified=False,
                    finite_evaluator_error_not_paid_by_native_residual=True,
                    every_actual_C_point_and_far_row_is_interval_enclosed=True,
                    actual_original_engine_exp_and_exp_twice_logw_rounding_error_certified=False,
                    original_engine_must_record_its_actual_w_w2_E_words=True)
                geometry=dict(schema=GEOMETRY_SCHEMA,model_schema=MODEL,modes=M,spacing=2,
                    orientation=1,stage_count=DEPTH,rawNode=[72*i for i in range(9)],
                    cut_radius=r_cut,finite_far_radius=r_far,
                    native_old_graphs_or_gains_used=False,
                    original_C_input_binding=data["binding"],numeric_geometry_identity=geometry_identity,
                    arrays=arrays,stage_packets=stage_packets,
                    field_columns=["x","r","drdx","logw","dlogwdx"],
                    steps_per_stage=args.steps,field_count_per_stage=field_width,
                    coordinate_mu_rule="positive finite binary64 exp(7 log(actual node r)+actual numeric logw)",
                    finite_far_rows_are_nondividing_approximations_with_bound_error=True,
                    exact_global_same_C_and_infinite_nonlinear_DN_not_certified=True,
                    far_identity=dict(physical_radius_word=word(r_far),general_rows=row_receipt,
                        original_R312_complete_rows=data["far"]["complete_rows"],
                        original_R324_formula_source_sha256=F.BASE_PROPAGATOR_SHA,
                        actual_R347_projective_source_sha256=F_SHA,
                        row_normalization="complete original QF=1 unit orientation, not materialized column",
                        complete_all112_general_matrix=arrays["far_matrix"],
                        no_height_division=True))
                report.update(geometry=emit(args.out/"geometry.json",geometry),
                    native_geometry_ready=True,completed=True,
                    complete_native_field_occurrences=point_index,
                    complete_unique_sample_points=sampler.point_count,
                    numerical_sample_work_resolution_complete=all(
                        x["work_resolution_complete"] for x in sampler.cache.values()))
                exit_code=0
    except Exception as error:
        report["error"]=dict(type=type(error).__name__,message=str(error),
            scientific_or_resource_scope_not_relabelled_as_native_rejection=True)
        if "complete-unpaid-scope" in journals:
            journals["complete-unpaid-scope"].add(dict(kind="current-C-native-sampling-unfinished",
                error=report["error"],completed_far_modes=[r["physical_frequency"] for r in rows if r["complete"]],
                unstarted_far_modes=list(F.MODES[len(rows):]),complete_native_field_occurrences_done=point_index,
                all_remaining_field_plan_preserved=grid is not None,
                no_unread_point_or_row_claimed_complete=True))
    finally:
        if linear is not None:linear.finish()
        if sampling is not None:
            if sampling_paused_for_linear:
                sampling.started+=linear.elapsed();sampling_paused_for_linear=False
            sampling.finish()
        ledgers={}
        for name,journal in journals.items():
            # The actual frozen B.Journal.finish is idempotent. Reuse its returned
            # descriptor even when a later metadata write failed after closure.
            ledgers[name]=journal.finish()
        report.update(detailed_ledgers=ledgers,elapsed_seconds=time.monotonic()-started,
            actual_far_modes_attempted=[r["physical_frequency"] for r in rows],
            actual_far_modes_completed=[r["physical_frequency"] for r in rows if r["complete"]],
            actual_not_started_far_modes=list(range(2*(len(rows)+1),225,2)),
            actual_point_count=None if sampler is None else sampler.point_count,
            actual_inverse_range_count=None if sampler is None else sampler.range_count,
            actual_coarse_valid_point_leaves=None if sampler is None else sampler.coarse_count,
            linear_phase_attempts=None if linear is None else linear.attempts,
            sampling_phase_attempts=None if sampling is None else sampling.attempts,
            complete_factorized_far_modes=[r["physical_frequency"] for r in rows
                if r["complete_required_far_propagation"]],
            complete_unit_far_row_modes=[r["physical_frequency"] for r in rows if r["complete"]],
            linear_phase_resource_receipt=None if linear is None else linear.record(),
            sampling_phase_resource_receipt=None if sampling is None else sampling.record(),
            raw_owned_temporary_only=True,new_nonlinear_acceptance_gate=False)
        result=emit(args.out/"result.json",report)
        print(json.dumps(dict(event="current_C_actual_geometry_result",result=result,
            native_geometry_ready=report["native_geometry_ready"],completed=report["completed"],
            actual_far_modes_completed=report["actual_far_modes_completed"],error=report["error"])),flush=True)
    return exit_code


if __name__=="__main__":
    raise SystemExit(main())
