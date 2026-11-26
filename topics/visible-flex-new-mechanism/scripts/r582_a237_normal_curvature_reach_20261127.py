#!/usr/bin/env python3
"""New complete geometry of real a237 using same-cell normal curvature.

First certify the NEW circle carrying this q's complete mean controls.
Only then reconstruct the unsaved endpoint field once, require the actual
mesh hash, and enclose the full nonround material map relative to that
circle. No old fine grid, Jacobian, optimizer, seed fit or diagnostic is
replayed. All science runs in the declared public Actions scope.
"""
import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import struct
import sys
import time
from types import SimpleNamespace

import r611_circular_reference_global_geometry_20261127 as backend
from r582_same_field_radial_intervals_20261127 import (
    SameFieldRadialDesign, rounded_core_angular_boxes, exact,
)
from r582_same_field_mean_intervals_20261127 import SameFieldMeanGeometry
from r604_rotating_frame_continuous_norms_20261127 import Jet
from r621_normal_projected_curvature_20261127 import radial_block_with_normal_curvature
from r582_stable_material_field_20261126 import StableField, COUNTS as STABLE_COUNTS
from r582_paid_resonant_field_20261126 import paid_source

I = backend.I
SCHEMA = 'r582-actual-a237-new-mean-circle-normal-projected-reach-v1'
Q_SHA = 'a2377220dacda9eefe63f25a2000441f0169a0db5de9bc23840f90e5037a895e'
MESH_SHA = '0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991'
NORM_NAMES = ('C0_upper', 'C1_difference_upper',
              'reference_covariant_C2_difference_upper', 'R621_principal_curvature_upper')


def emit(tag, value):
    print('RETAINED_CONTINUOUS_'+tag+' '+json.dumps(value, sort_keys=True,
        separators=(',', ':'), allow_nan=False), flush=True)


def identity(values):
    return hashlib.sha256(b''.join(struct.pack('<d', float(x)) for x in values)).hexdigest()


class Clock:
    def __init__(self, deadline):
        self.deadline = deadline

    def check(self):
        if time.monotonic() >= self.deadline:
            raise backend.original.ClockCheckpoint('new continuous geometry clock')


class MeanContext:
    """Only the fields consumed by the exact mean interface; no material ODE."""
    def __init__(self, q, clock):
        self.q, self.hermite = tuple(q), clock
        self.b, self.I = backend, I
        self.reference_core_radius = .38

    def background_jets(self, s):
        chi, _, first, second = backend.step_jets(s, backend.C, backend.BACKGROUND_END)
        return (chi, first, second), (1-chi, -first, -second)


class ReconstructedField(StableField):
    def local_diagnostics(self):
        return {'already_paid_and_not_replayed': True,
            'source_run': 45842923121, 'source_job': 139989034161,
            'source_FIELD_JSON_sha256':
                'aed0e08c3e62c80e90a00f148bdde34c96bf35d819426fb40eaa2e5dce75cc99',
            'new_diagnostic_points': 0}


def new_reference_jets(mean, left, right, clock):
    """The NEW 8+8+1 inputs, without the old CompactGeometry.jets method."""
    clock.check()
    s = I(left, right)
    if right <= backend.C:
        radius = (I(.38), I(0), I(0))
        height = (I(backend.original.CORE_HALF)+s, I(1), I(0))
    else:
        radius = mean._radius_jets(s, I(.38), True)
        height = mean._height_jets(s, mean.analytic_height_jets(s), True)
    row = mean.dictionary(radius, height)
    speed2 = row['a_s']**2+row['z_s']**2
    if speed2.lo <= 0:
        raise ArithmeticError('new reference speed lower bound unresolved')
    row['speed'] = backend.sqrt_i(speed2)
    row['curvature'] = backend.hull_abs(
        row['a_s']*row['z_ss']-row['z_s']*row['a_ss'])/(speed2*row['speed'])
    return row


def certify_new_reference(mean, q, args, clock, started):
    # R608's coefficient hypothesis is checked on exact stored numbers.
    if not all(abs(exact(v)) < Fraction(3, 5) for v in q[64:80]):
        raise ValueError('new mean controls do not satisfy the paid R608 tail hypothesis')
    if not q[-1] > backend.original.CORE_HALF:
        raise ValueError('new cap height is not above the exact central cylinder')
    rho = I(6072)/100000
    maximum_curvature = 1/rho
    tail_start = I(backend.L)-I(backend.ELL)*2/25
    compact_end = backend.up(tail_start.hi)
    points = {backend.C, compact_end, backend.BACKGROUND_END,
              backend.CONTROL_LEFT, backend.CONTROL_RIGHT}
    for k in range(1, 65):
        points.add(backend.C+(compact_end-backend.C)*k/65)
    for knot in (1/3, 2/3):
        points.add(backend.C+(backend.L-backend.C)*knot)
    points = sorted(x for x in points if backend.C <= x <= compact_end)
    stack = [(a, b, 0) for a, b in zip(points[:-1], points[1:])]
    digest = hashlib.sha256()
    extrema = {'a_min': math.inf, 'a_max': 0., 'z_s_min': math.inf,
               'speed_min': math.inf, 'curvature_max': 0.}
    examined = accepted = 0
    peak = failure = None
    unresolved = []
    while stack:
        if time.monotonic() >= clock.deadline:
            failure = 'new_reference_scientific_clock'
            break
        left, right, depth = stack.pop()
        examined += 1
        row = None
        reason = 'new reference radius, positive height speed or curvature unresolved'
        try:
            row = new_reference_jets(mean, left, right, clock)
            good = (row['a'].lo >= backend.RC and row['z_s'].lo > 0
                    and row['curvature'].hi <= maximum_curvature.lo)
        except backend.original.ClockCheckpoint as exc:
            unresolved.append({'interval':[left,right], 'reason':str(exc)})
            failure = 'new_reference_scientific_clock'
            break
        except ArithmeticError as exc:
            good, reason = False, str(exc)
        if good:
            accepted += 1
            digest.update((json.dumps([left, right, {k: [v.lo,v.hi]
                for k,v in row.items()}], sort_keys=True, separators=(',', ':'))+'\n').encode())
            for name, key in (('a_min','a'),('z_s_min','z_s'),('speed_min','speed')):
                extrema[name] = min(extrema[name], row[key].lo)
            extrema['a_max'] = max(extrema['a_max'], row['a'].hi)
            if row['curvature'].hi > extrema['curvature_max']:
                extrema['curvature_max'], peak = row['curvature'].hi, [left,right]
            continue
        if depth >= args.maximum_depth or examined >= args.maximum_reference_cells:
            unresolved.append({'interval':[left,right], 'depth':depth, 'reason':reason,
                'jets':None if row is None else {k:[v.lo,v.hi] for k,v in row.items()}})
            failure = 'new_reference_interval_capacity'
            break
        middle = left+(right-left)/2
        if middle in (left,right):
            raise ArithmeticError('new reference bisection lost resolution')
        stack.extend(((left,middle,depth+1),(middle,right,depth+1)))
        if examined % 1000 == 0:
            emit('REFERENCE_PROGRESS', {'examined':examined,'accepted':accepted,
                'pending':len(stack),'seconds':time.monotonic()-started})
    success = failure is None and not stack and not unresolved
    diameter = None
    if success:
        ar = max(extrema['a_max'], .38, .237)
        diameter = 2*backend.sqrt_i(I(ar)**2+I(q[-1])**2)
    return {'complete_new_reference':success,'failure':failure,
        'uses_actual_new_mean_controls_and_new_cap_height':True,
        'old_R611_compact_leaves_or_diameter_not_reused':True,
        'compact_interval':[backend.C,compact_end],
        'exact_R608_tail_start_enclosure':[tail_start.lo,tail_start.hi],
        'same_R608_coefficient_box_checked':True,
        'R599_all_closed_surface_hypotheses_paid_if_complete':success,
        'reach_lower_if_complete':rho.lo if success else None,
        'diameter_upper_if_complete':diameter.hi if success else None,
        'examined_cells':examined,'accepted_cells':accepted,'pending_cells':len(stack),
        'first_unresolved':unresolved,'accepted_leaf_stream_sha256':digest.hexdigest(),
        'extrema':{k:(v if math.isfinite(v) else None) for k,v in extrema.items()},
        'curvature_attaining_cell':peak,
        'leaf_tables_saved':False}


def artanh_upper(x, terms=64):
    """Positive power series plus an exact geometric upper remainder."""
    if not 0 <= x.lo <= x.hi < 1:
        raise ArithmeticError('artanh enclosure requires 0<=x<1')
    square, power, value = x*x, x, I(0)
    for k in range(terms):
        value = value+power/(2*k+1)
        power = power*square
    return value+power/((2*terms+1)*(1-square))


def normal_chord_consequence(extrema, reference):
    delta, alpha = extrema['C0_upper'], extrema['C1_difference_upper']
    if alpha >= 1:
        return {'established':False,'reason':'uniform immersion difference is not below one'}
    rho = I(reference['reach_lower_if_complete'])
    # R621 encloses actual principal curvature cell by cell, after normal
    # projection. The full covariant-C2 difference remains a reported norm.
    curvature = I(extrema['R621_principal_curvature_upper'])
    if not math.isfinite(curvature.hi) or curvature.lo <= 0:
        return {'established':False,'reason':'positive global principal-curvature bound unavailable'}
    lambda_box = I(1)+I(alpha)
    lam, nu = I(lambda_box.hi), I(alpha)
    derived = {'derivative_upper':lam.hi,
        'normal_projection_difference_upper':nu.hi,
        'principal_curvature_upper':curvature.hi,
        'principal_curvature_source':'R621 maximum of complete same-cell normal-projected bounds',
        'reported_full_covariant_C2_difference_upper':extrema['reference_covariant_C2_difference_upper']}
    # R604 near-pair condition: 3 < pi is an exact conservative lower bound.
    # Searching only x<=3/4 is conservative; the verified lhs/rhs condition
    # below, rather than any presumed relation between K and rho, qualifies x.
    lo, hi = 0., .75
    for _ in range(32):
        middle = (lo+hi)/2
        lhs = 2*lam*rho*artanh_upper(I(middle))
        rhs = 3/(2*curvature)
        if lhs.hi <= rhs.lo:
            lo = middle
        else:
            hi = middle
    threshold_box = 2*rho*I(lo)
    threshold = I(threshold_box.lo)
    if threshold.lo <= 2*delta:
        return {'established':False,'reason':'far-pair displacement budget is not positive',
            'derived':derived,'near_pair_threshold_lower':threshold.lo}
    far = (threshold-2*I(delta))**2/(
        threshold**2/rho+2*nu*threshold+4*I(delta))
    tau = min((1/curvature).lo, far.lo)
    diameter = I(reference['diameter_upper_if_complete'])+2*I(delta)
    ratio = I(tau)/diameter
    return {'established':tau>0,'derived':derived,
        'near_pair_threshold_lower':threshold.lo,
        'artanh_positive_series_terms':64,'pi_lower_bound_used':3,
        'complete_material_injectivity_follows_from_R604':tau>0,
        'whole_surface_reach_lower':tau,'whole_surface_diameter_upper':diameter.hi,
        'whole_surface_reach_over_D_lower':ratio.lo,
        'reach_ratio_point03_met':ratio.lo >= (I(3)/100).hi,
        'metric_or_large_amplitude_or_fixed_g_claim':False}


def certify_nonround(design, mean, core, reference, args, clock, started):
    # Removing knots in a proved identically-zero material suffix does not
    # alter the spline or its mesh. Other exact named gates remain present.
    partition = list(design.initial_partition())
    suffix = design.hermite.exact_zero_suffix
    zero_start = None if suffix is None else max(suffix, backend.BACKGROUND_END)
    if zero_start is not None:
        partition = sorted(set([x for x in partition if x <= zero_start]
            +[x for x in design.named_interfaces if x >= zero_start]+[zero_start,backend.L]))
    if partition[0] != 0. or partition[-1] != backend.L:
        raise ValueError('proof partition does not cover the whole material body')
    stack = [(a,b,0) for a,b in zip(partition[:-1],partition[1:])]
    maxima = dict.fromkeys(NORM_NAMES,0.)
    attainers = dict.fromkeys(NORM_NAMES,None)
    limits = {'C0_upper':args.norm_C0_budget,'C1_difference_upper':args.norm_C1_budget,
              'R621_principal_curvature_upper':args.principal_curvature_budget}
    attainer_records = dict.fromkeys(NORM_NAMES,None)
    digest = hashlib.sha256()
    accepted = examined = budget_exceeded = 0
    unresolved = []
    refinement_capacity_reached = False
    while stack:
        if time.monotonic() >= clock.deadline:
            unresolved.append({'reason':'continuous_norm_scientific_clock','remaining_cells':len(stack)})
            break
        left,right,depth = stack.pop()
        examined += 1
        bound = None
        reason = None
        try:
            angular = design.angular_box(left,right,core['u'],core['utheta'],core['uthetatheta'])
            jets = {key:Jet(*(angular[key][n] for n in ('value','s','ss','theta')))
                    for key in ('u','v')}
            means = mean.boxes(left,right,core['a0'])
            bound = radial_block_with_normal_curvature(means['current'],means['reference'],
                jets['u'],jets['v'],difference=means['difference'])
            if not all(math.isfinite(bound[k]) and bound[k]>=0 for k in NORM_NAMES):
                raise ArithmeticError('nonfinite same-field norm enclosure')
            within = all(bound[k] <= target for k,target in limits.items())
        except backend.original.ClockCheckpoint as exc:
            unresolved.append({'interval':[left,right], 'reason':str(exc)})
            break
        except ArithmeticError as exc:
            bound = None
            within,reason = False,str(exc)
        can_refine = (depth < args.norm_refinement_depth
                      and examined < args.maximum_norm_cells)
        if bound is not None and (within or not can_refine):
            accepted += 1
            if not within:
                budget_exceeded += 1
                refinement_capacity_reached |= examined >= args.maximum_norm_cells
            digest.update((json.dumps([left,right,bound],sort_keys=True,
                separators=(',', ':'))+'\n').encode())
            for key in NORM_NAMES:
                if bound[key]>maxima[key]:
                    maxima[key],attainers[key]=bound[key],[left,right]
                    attainer_records[key]={'interval':[left,right],'same_cell_bounds':bound}
        elif can_refine:
            middle = left+(right-left)/2
            if middle in (left,right):
                unresolved.append({'interval':[left,right],'reason':'binary64 split exhausted'})
                break
            stack.extend(((left,middle,depth+1),(middle,right,depth+1)))
        else:
            unresolved.append({'interval':[left,right],'depth':depth,
                'reason':reason or 'same-field norm is undefined'})
            break
        if examined % 2000 == 0:
            emit('NORM_PROGRESS',{'examined':examined,'accepted':accepted,'pending':len(stack),
                'current_uniform_bounds':maxima,'seconds':time.monotonic()-started})
    complete = not stack and not unresolved
    cap = mean.cap_disk_difference()
    maxima['C0_upper']=max(maxima['C0_upper'],cap['C0_upper'])
    # On the complete central cylinder z is the SAME material coordinate.
    # Its difference and reference connection are exactly those at s=0 in
    # the full [0,C] core already covered, not a reparameterized cylinder.
    result = {'complete_nonround_norm_coverage':complete,
        'all_theta_enclosed_by_same_core_and_original_complete_mode_fields':True,
        'central_cylinder_same_material_z_core_extension':True,
        'lower_body_is_the_original_orthogonal_reflection':True,
        'both_complete_Cartesian_caps_included':True,
        'cap_difference':{k:([v.lo,v.hi] if isinstance(v,I) else v) for k,v in cap.items()},
        'seed_exact_zero_suffix_proof_start':zero_start,
        'zero_suffix_partition_coalescing_does_not_change_material_mesh':True,
        'initial_proof_intervals':len(partition)-1,
        'examined_cells':examined,'accepted_cells':accepted,'pending_cells':len(stack),
        'budget_exceeding_but_valid_bound_cells':budget_exceeded,
        'refinement_capacity_reached':refinement_capacity_reached,
        'norm_budgets_are_refinement_targets_not_pass_gates':True,
        'principal_curvature_budget_is_refinement_target_not_a_clipped_curvature_bound':True,
        'full_C2_difference_is_reported_but_does_not_drive_refinement':True,
        'one_same_cell_radial_angular_jet_and_mean_assembly_for_all_four_bounds':True,
        'maximum_norm_cells_is_refinement_stop_not_coverage_cutoff':True,
        'first_unresolved':unresolved,'uniform_bounds':maxima,'attaining_cells':attainers,
        'small_same_cell_diagnostics_at_attainers':attainer_records,
        'accepted_leaf_stream_sha256':digest.hexdigest(),'leaf_tables_saved':False}
    result['R604_consequence'] = normal_chord_consequence(maxima,reference) if complete else None
    return result


def main():
    if (os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'
            or not os.environ.get('GITHUB_RUN_ID')):
        raise RuntimeError('scientific execution requires the named public Actions repository')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-state-json',required=True)
    parser.add_argument('--source-state-sha256',required=True)
    parser.add_argument('--maximum-seconds',type=float,default=1800)
    parser.add_argument('--maximum-reference-cells',type=int,default=100000)
    parser.add_argument('--maximum-norm-cells',type=int,default=250000)
    parser.add_argument('--maximum-depth',type=int,default=28)
    parser.add_argument('--norm-refinement-depth',type=int,default=6)
    parser.add_argument('--norm-C0-budget',type=float,default=.0025)
    parser.add_argument('--norm-C1-budget',type=float,default=.015)
    parser.add_argument('--principal-curvature-budget',type=float,default=18.)
    parser.add_argument('--height-width-target',type=float,default=1e-6)
    parser.add_argument('--height-maximum-cells',type=int,default=65536)
    args = parser.parse_args()
    if (not 30 < args.maximum_seconds <= 1800
            or min(args.norm_C0_budget,args.norm_C1_budget,args.principal_curvature_budget) <= 0):
        raise ValueError('outside the declared a237 normal-curvature scope')
    raw=sys.stdin.buffer.read() if args.source_state_json=='@stdin' else args.source_state_json.encode()
    if hashlib.sha256(raw).hexdigest()!=args.source_state_sha256:
        raise ValueError('actual retained continuous geometry input changed')
    source=json.loads(raw)
    q=source['actual_retained_q']
    if (source['schema']!='actual-a237-new-mean-circle-normal-curvature-geometry-v1'
            or len(q)!=97 or identity(q)!=Q_SHA or source['p']!=.181
            or source['material_mesh_sha256']!=MESH_SHA
            or source['origin']['run_id']!=45887805731
            or source['origin']['job_id']!=140142780497
            or source['origin']['source_commit']!='0cce06dd57217f8b06af3a6eaf4018f445bda371'
            or source['origin']['FINAL_JSON_sha256']!='e3371193ba4dcaa4df4d8298c856dce0663d2c4793d0cf205d625203af35ae47'
            or source['comparison_reference']!='same_actual_mean_controls_fixed_circle_core_0.38'):
        raise ValueError('new geometry source is not the actual qualified retained state')
    paid_text=source['paid_seed_json']
    if hashlib.sha256(paid_text.encode()).hexdigest()!=source['paid_seed_json_sha256']:
        raise ValueError('necessary original paid material input changed')
    started=time.monotonic()
    clock=Clock(started+args.maximum_seconds-30)
    counts=defaultdict(int)
    state={'mu':-.040019082162222074,'nu':-.048942275258064924}
    provider=mean=None
    reference=nonround=field_receipt=design_receipt=None
    failure=None
    emit('DEFINITION',{'schema':SCHEMA,'source':source,
        'source_state_sha256':args.source_state_sha256,
        'arguments':{k:v for k,v in vars(args).items() if k!='source_state_json'},
        'new_reference_old_R611_result_not_replayed_or_transferred':True,
        'height_integral_reconstructed_once_because_interval_prefix_was_not_saved':True,
        'material_reconstruction_only_after_new_reference_passes':True,
        'zero_new_optimizer_Jacobian_fine_scan_or_old_diagnostic_calls':True,
        'new_a237_q_mean_circle_C0_C1_and_normal_curvature_all_paid_in_this_scope':True,
        'earlier_f1_geometry_not_transferred_to_new_q':True,
        'actual_K_from_R621_same_cell_normal_projection_not_global_beta':True,
        'one_field_box_pass_also_reports_original_C2_difference':True})
    try:
        provider=backend.CompactGeometry(state,clock.deadline,counts,
            args.height_width_target,args.height_maximum_cells)
        context=MeanContext(q,clock)
        mean=SameFieldMeanGeometry(context,provider,reference_q=q)
        reference=certify_new_reference(mean,q,args,clock,started)
        emit('REFERENCE',reference)
        if reference['complete_new_reference']:
            reconstruction=SimpleNamespace(initial_epsilon=.001,rtol=2e-11,atol=2e-13,max_step=.15)
            field=ReconstructedField(json.loads(paid_text),source['paid_positive_chart'],
                reconstruction,clock.deadline)
            field_receipt=field.receipt()
            design=SameFieldRadialDesign(field,q,source['p'],Q_SHA,MESH_SHA,
                deadline=clock.deadline,backend=backend)
            core=rounded_core_angular_boxes(source['p'],.18,.2,backend)
            mean=SameFieldMeanGeometry(design,provider,reference_q=q)
            emit('FIELD',{'field_receipt':field_receipt,'core_bounds':{
                k:[v.lo,v.hi] for k,v in core.items()},'seconds':time.monotonic()-started})
            nonround=certify_nonround(design,mean,core,reference,args,clock,started)
            design_receipt=design.receipt()
        else:
            failure='new_reference_not_certified_no_old_reach_transferred'
    except (backend.original.ClockCheckpoint,ArithmeticError,ValueError) as exc:
        failure=type(exc).__name__+': '+str(exc)
    emit('FINAL',{'schema':SCHEMA,'failure':failure,'new_reference':reference,
        'nonround_continuous_geometry':nonround,'same_material_receipt':design_receipt,
        'field_reconstruction_receipt':field_receipt,
        'mean_receipt':None if mean is None else mean.receipt(),
        'height_integral_receipt':None if provider is None else getattr(provider.height,'receipt',None),
        'interval_counts':dict(counts),'new_material_original_counts':dict(paid_source.COUNTS),
        'new_stable_material_counts':dict(STABLE_COUNTS),
        'new_scientific_seconds':time.monotonic()-started,
        'old_paid_costs_remain_in_source_receipts':True,
        'actual_q_binary64_sha256':Q_SHA,
        'material_mesh_binary64_sha256':MESH_SHA,
        'all_previous_geometry_and_optimizer_costs_remain_paid':True,
        'exact_infinite_kernel_identification_or_fixed_g_metric_claim':False,
        'README_completion_claim':False})


if __name__=='__main__':
    main()
