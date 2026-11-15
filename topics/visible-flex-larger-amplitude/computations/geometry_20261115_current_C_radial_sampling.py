#!/usr/bin/env python3
"""Actual same-C radial samples and complete nondividing finite-far rows.

All scientific work is restricted to the named public Actions repository.
The input C primitive enclosures and R312 rows are unchanged original sources.
A numerical representative is disclosed as a finite sampled approximation,
not identified with a jointly realized exact C root choice.
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
from pathlib import Path
import struct
import sys
import time

SCHEMA="current-C-physical-radial-samples-and-general-far-v1"
GEOMETRY_SCHEMA="current-C-native-radial-geometry-bundle-v1"
MODEL="R286-original-stored-continuous-model-convention-C-v1"
F_NAME="geometry_20261115_stored_C_finite_head_flux.py"
F_SHA="4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d"
B_NAME="geometry_20261115_stored_continuous_E_cover_v3.py"
B_SHA="f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df"
REPOSITORY="Rogerhu12/math-research-public"
M,K,DEPTH=112,224,576
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
    if rec["sha256"]!=F_SHA:raise ValueError("Use unchanged complete R324 formulas")
    spec=importlib.util.spec_from_file_location("_current_C_original_flux",path)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module
    spec.loader.exec_module(module);F=module
    runtime,sources,proof=F.load_runtime(args);B=F.B
    if sources[B_NAME]["sha256"]!=B_SHA:raise ValueError("Actual v3 target source differs")
    return runtime,dict(original_flux=rec,original_runtime_sources=sources),proof


class OwnedBudget:
    def __init__(self,seconds,limit,label):
        self.started=time.monotonic();self.seconds=seconds;self.limit=limit
        self.attempts=0;self.label=label

    def check(self):
        if time.monotonic()-self.started>=self.seconds:
            raise F.WorkStop("Declared "+self.label+" resource wall budget reached")

    def attempt(self):
        self.check()
        if self.attempts>=self.limit:
            raise F.WorkStop("Declared "+self.label+" work-unit limit reached")
        self.attempts+=1


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


def point_column(far,data,required,by_panel,geometry,args,budget,steps,tubes,unpaid,r_far):
    """R324 full two-coordinate propagation; no height quotient is evaluated."""
    m=far["physical_frequency"];state,initial=F.initial_column(far,data)
    whole=dict(u=None,k=None);coverage={};accepted=0;coarse=0;stack=[];index=0;in_flight=None
    first_step,first_tube=steps.rows,tubes.rows
    error=None;last_paid=None
    try:
        for index,item in enumerate(required):
            panel=item["panel"];stack=[(item["left"],item["right"],0)]
            while stack:
                budget.attempt();lo,hi,depth=stack.pop();in_flight=(lo,hi,depth)
                try:
                    coeff=geometry.get(panel,lo,hi)
                    candidate=F.advance_candidate(state,coeff,m,lo,hi,args)
                except (ArithmeticError,ZeroDivisionError,OverflowError) as failure:
                    if depth<args.max_depth:
                        mid=(lo+hi)/2;stack.extend(((mid,hi,depth+1),(lo,mid,depth+1)))
                        in_flight=None;continue
                    stack.append((lo,hi,depth));in_flight=None
                    raise F.PanelUnpaid("Whole far-point coefficient map unresolved: "+str(failure))
                if candidate["needs_norm_split"] or (not candidate["work_goal_met"] and depth<args.max_depth):
                    if depth>=args.max_depth:
                        stack.append((lo,hi,depth));in_flight=None
                        raise F.PanelUnpaid("Whole far-point panel norm work bound unresolved")
                    mid=(lo+hi)/2;stack.extend(((mid,hi,depth+1),(lo,mid,depth+1)))
                    in_flight=None;continue
                original_flux=F.restore_flux(candidate["tube"],candidate["framed"])
                u,j=original_flux
                if not coeff["w"]>0:raise ArithmeticError("Complete original far-point w must remain positive")
                k=j/coeff["w"];F.finite([u,j,k])
                for leaf in by_panel.get(panel["row"],[]):
                    a,b=max(lo,leaf["left"]),min(hi,leaf["right"])
                    if a>b:continue
                    if whole["u"] is None:whole=dict(u=u,k=k)
                    else:whole=dict(u=whole["u"].union(u),k=whole["k"].union(k))
                    old=coverage.get(leaf["leaf_row"])
                    if old is None:
                        if a!=leaf["left"]:raise ValueError("A possible far-point inverse leaf lost its initial interval")
                        coverage[leaf["leaf_row"]]=(a,b)
                    else:
                        if a>old[1]:raise ValueError("A possible far-point inverse leaf has a gap")
                        coverage[leaf["leaf_row"]]=(old[0],max(old[1],b))
                    tubes.add(dict(schema=SCHEMA+"-physical-far-column-tube",
                        physical_frequency=m,physical_far_word=word(r_far),
                        possible_inverse_leaf_row=leaf["leaf_row"],
                        original_source_panel_row=panel["row"],source_piece=panel["source_piece"],
                        closed_step_interval=[str(lo),str(hi)],closed_leaf_intersection=[str(a),str(b)],
                        complete_physical_u=B.record(u),complete_flux_j=B.record(j),
                        complete_physical_k=B.record(k),same_original_w=B.record(coeff["w"]),
                        original_QF_one_normalization_restored=True,
                        every_root_family_choice_and_previous_error_retained=True))
                steps.add(dict(schema=SCHEMA+"-complete-accepted-far-point-panel",
                    physical_frequency=m,physical_far_word=word(r_far),
                    original_source_panel_row=panel["row"],source_piece=panel["source_piece"],
                    closed_parameter_interval=[str(lo),str(hi)],subdivision_depth=depth,
                    original_complete_incoming_state=F.state_record(state),
                    framed_complete_incoming_state=F.state_record(candidate["framed"]),
                    complete_outgoing_state=F.state_record(candidate["next_state"]),
                    coefficient_row=coeff["coefficient_row"],
                    full_balanced_coefficient_matrix=F.rec_matrix(candidate["M"]),
                    exact_dyadic_constant_center=F.rec_matrix(candidate["M0"]),
                    beta=B.record(candidate["beta"]),epsilon=B.record(candidate["epsilon"]),
                    alpha=B.record(candidate["alpha"]),norm_length=B.record(candidate["norm_length"]),
                    full_fundamental_Duhamel_defect=B.record(candidate["defect"]),
                    entire_incoming_norm=B.record(candidate["initial_norm"]),
                    whole_solution_error_radius=B.record(candidate["vector_error"]),
                    endpoint_Taylor_remainder=B.record(candidate["endpoint_tail"]),
                    whole_tube_Taylor_remainder=B.record(candidate["tube_tail"]),
                    whole_solution_tube=[B.record(v) for v in candidate["tube"]],
                    input_power_shift=candidate["input_column_shift"],
                    output_power_shift=candidate["output_column_shift"],
                    local_work_goal_met=candidate["work_goal_met"],
                    valid_coarse_enclosure_retained=not candidate["work_goal_met"]))
                state=candidate["next_state"];accepted+=1;coarse+=int(not candidate["work_goal_met"])
                last_paid=dict(original_source_panel_row=panel["row"],source_piece=panel["source_piece"],
                    parameter=str(hi),full_state=F.state_record(state))
                in_flight=None
            index+=1
        for leaves in by_panel.values():
            for leaf in leaves:
                if coverage.get(leaf["leaf_row"])!=(leaf["left"],leaf["right"]):
                    raise ValueError("A complete possible inverse interval was not covered by propagated tubes")
        if whole["u"] is None:raise AssertionError("Complete far-point propagation has no physical column")
    except Exception as failure:
        if in_flight is not None:stack.append(in_flight)
        error=dict(type=type(failure).__name__,message=str(failure))
        unpaid.add(dict(kind="current-physical-far-linear-column",physical_frequency=m,
            physical_far_word=word(r_far),error=error,last_paid=last_paid,
            complete_pending_scope=F.pending_description(required,index,stack),
            entire_two_coordinate_column_remains_unpaid=True))
    return dict(schema=SCHEMA+"-complete-far-point-mode",physical_frequency=m,
        initial_R312_column=initial,complete=error is None,error=error,
        physical_far_word=word(r_far),complete_physical_column=(
            {key:B.record(value) for key,value in whole.items()} if error is None else None),
        full_interval_objects=whole if error is None else None,
        complete_step_rows=dict(first=first_step,stop=steps.rows),
        complete_far_tube_rows=dict(first=first_tube,stop=tubes.rows),
        last_paid=last_paid,accepted_panels=accepted,valid_coarse_panels=coarse,
        division_by_height_performed=False,all_original_root_choices_included=True,
        exact_global_family_member_not_selected=True)


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
    r=B.exact(Q(r_far));w=far_sample["boxes"]["w"] if "boxes" in far_sample else None
    # w is reconstructed from the original exact enclosure receipt, never from exp of its numeric representative.
    if w is None:w=F.as_ball(far_sample["numerical_word_receipts"]["w"]["exact_real_enclosure"])
    if not w>0:raise ArithmeticError("Same exact C far w range not positive")
    result=[];matrix=[]
    for row in rows:
        m=row["physical_frequency"];u=row["full_interval_objects"]["u"];k=row["full_interval_objects"]["k"]
        aa=-k*r**4+u*m*m*r**3
        bb=u*B.exact(12).sqrt()*B.exact(Q(mu))/(r**4*w)
        F.finite([aa,bb])
        scale=max(F.abs_upper_q(aa),F.abs_upper_q(bb))
        if scale==0:raise ArithmeticError("Exact normalized far-row enclosure is identically zero")
        power=F.floor_log2(scale);an,bn=aa*B.p2(-power),bb*B.p2(-power)
        av,ar=numerical_representative(an);bv,br=numerical_representative(bn)
        if av==0 and bv==0:raise ArithmeticError("Both numerical far-row coefficients rounded to zero; no row fabricated")
        values=[0.0]*K;i=m//2-1;values[i]=av;values[M+i]=bv;matrix.extend(values)
        result.append(dict(physical_frequency=m,complete_physical_u=B.record(u),
            complete_physical_k=B.record(k),original_common_column_normalization="Q_F=1",
            physical_radius_word=word(r_far),same_C_w=B.record(w),mu_word=word(mu),
            exact_orientation=1,exact_common_row_power=power,
            complete_Q_coefficient=ar,complete_Pi_coefficient=br,
            coordinate_rule="(-k*r^4+u*m^2*r^3, u*sqrt(12)*mu/(r^4*w))",
            no_height_division=True,selected_numeric_row_is_not_an_exact_family_member=True,
            simultaneous_global_C_realization_of_numeric_rows_certified=False))
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
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--precision-bits",type=int,default=256)
    p.add_argument("--linear-budget-seconds",type=float,required=True)
    p.add_argument("--sampling-budget-seconds",type=float,required=True)
    p.add_argument("--max-panels",type=int,default=200000)
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
           args.max_geometry_cache_records>0 and args.sample_max_nodes>0):
        raise ValueError("Declared finite source controls out of range")
    args.out.mkdir(parents=True);large=args.out/"large-arrays";large.mkdir()
    started=time.monotonic();report=dict(schema=SCHEMA,source_sha256=sha(Path(__file__).read_bytes()),
        target_model_schema=MODEL,repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"],completed=False,native_geometry_ready=False,
        error=None,old_graphs_or_gains_used=False,no_height_division_in_far_rows=True,
        exact_global_C_realization_of_numeric_representatives_certified=False,
        nonlinear_solve_or_DN_computed=False,closed_field_or_BVP_accepted=False)
    journals={};exit_code=2;rows=[];point_index=0;grid=None;sampler=None;linear=None;sampling=None
    try:
        runtime,sources,proof=load_runtime(args)
        data=F.bind_inputs(args)
        report.update(runtime=runtime,frozen_sources=sources,actual_R324_proof=proof,
            actual_original_input_binding=data["binding"],
            actual_original_scope_conditions=data["facts"])
        for name in ("coefficient-boxes","sample-inverse-leaves","complete-unpaid-scope",
                     "far-accepted-panels","far-complete-tubes","far-all-mode-rows",
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
            sampling=OwnedBudget(args.sampling_budget_seconds,args.sample_max_nodes,"C physical-point sampling")
            geom=F.GeometryCache(head,data["panels"],args,journals["coefficient-boxes"],sampling)
            sampler=InverseSampler(head,data,args,geom,journals["sample-inverse-leaves"],unpaid,sampling)
            far_sample=sampler.sample(r_far,"explicit-finite-physical-far",True)
            report["far_point_sample"]=far_sample
            far_leaves=sampler.leaf_cache[struct.pack("<d",r_far).hex()]
            by_panel,required,after=finite_point_required(data,far_leaves)
            report["finite_far_required_prefix"]=emit(args.out/"required-source-panels.json",
                dict(actual_physical_radius=word(r_far),all_possible_inverse_leaves_included=True,
                    original_complete_source_stream=data["cover"]["ledgers"]["source_radial_panels"],
                    required=[dict(original_source_panel_row=x["panel"]["row"],
                        source_piece=x["panel"]["source_piece"],
                        closed_parameter_interval=[str(x["left"]),str(x["right"])]) for x in required],
                    complete_not_needed_outer_suffix=after))
            linear=OwnedBudget(args.linear_budget_seconds,args.max_panels,"C explicit finite-far propagation")
            geom.budget=linear
            for far in data["far_rows"]:
                linear.check()
                row=point_column(far,data,required,by_panel,geom,args,linear,
                    journals["far-accepted-panels"],journals["far-complete-tubes"],unpaid,r_far)
                rows.append(row)
                journals["far-all-mode-rows"].add({k:v for k,v in row.items() if k!="full_interval_objects"})
                print(json.dumps(dict(event="current_C_nondividing_far_mode",
                    physical_frequency=far["physical_frequency"],complete=row["complete"],
                    error=row["error"],accepted_panels=row["accepted_panels"],
                    elapsed_seconds=time.monotonic()-linear.started)),flush=True)
                if not row["complete"]:break
            report["far_completed_modes"]=[r["physical_frequency"] for r in rows if r["complete"]]
            if len(rows)!=M or not all(r["complete"] for r in rows):
                unpaid.add(dict(kind="complete-finite-far-unstarted-mode-suffix",
                    remaining_modes=list(F.MODES[len(rows):]),all_required_modes=list(F.MODES),
                    complete_native_geometry_not_returned=True))
            else:
                # Sampling receives its own explicit elapsed phase after propagation.
                # The already used sampling time remains charged; no hidden budget reset.
                sampling.started+=time.monotonic()-linear.started
                geom.budget=sampling
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
                far_matrix,far_rows=momentum_rows(rows,r_far,far_sample,mu[-1])
                row_receipt=emit(args.out/"actual-general-far-row-intervals-and-representatives.json",dict(
                    schema=SCHEMA+"-all112-general-far-rows",physical_radius_word=word(r_far),
                    complete_rows=far_rows,old_graph_or_height_division_used=False))
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
                        original_R324_formula_source_sha256=F_SHA,
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
            raw_owned_temporary_only=True,new_nonlinear_acceptance_gate=False)
        result=emit(args.out/"result.json",report)
        print(json.dumps(dict(event="current_C_actual_geometry_result",result=result,
            native_geometry_ready=report["native_geometry_ready"],completed=report["completed"],
            actual_far_modes_completed=report["actual_far_modes_completed"],error=report["error"])),flush=True)
    return exit_code


if __name__=="__main__":
    raise SystemExit(main())
