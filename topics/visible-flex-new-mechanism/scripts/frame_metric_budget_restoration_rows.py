#!/usr/bin/env python3
"""Fixed-curvature / lower-metric row interfaces; arrays and artificial CLI only.

No optimizer, research-report loader or real candidate evaluator lives here.
The physical family is external and unchanged. A smaller metric budget changes
constraint identity; it does not change the physical metric or coefficients.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from frame_collar_residual_audit import digest
from frame_collar_bvp import atomic_save
from frame_metric_epigraph import geometry_values, metric_rows
from frame_metric_epigraph_dense import mirror_values
from frame_curvature_epigraph_exchange import GROUPS
from frame_curvature_mixed_grid_steps import physical_rows, selected_physical_derivatives
from frame_curvature_psd import (curvature_values, curvature_parameter_jacobian,
                                 independent_principal_curvatures)

SCHEMA = 'fixed-curvature-lower-metric-eleven-row-interface-v1'
ROLES = ('restoration-target', 'restoration-target') + ('hard',)*9
JETS = ('X', 'Xs', 'Xt', 'Xss', 'Xst', 'Xtt', 'T')
CONTEXT_KEYS = ('complete_metric_sha256', 'fixed_b0_definition_sha256',
                'physical_space_definition_sha256', 'height_gate_physical_sha256',
                'height_gate_numerical_sha256', 'geometry_evaluation_definition_sha256')


def implementation_hashes():
    # This small array interface does not claim to own the caller's geometry.
    import frame_curvature_psd, frame_curvature_mixed_grid_steps
    import frame_metric_epigraph, frame_metric_epigraph_dense, frame_curvature_epigraph_exchange
    files = [Path(__file__), Path(frame_curvature_psd.__file__),
             Path(frame_curvature_mixed_grid_steps.__file__), Path(frame_metric_epigraph.__file__),
             Path(frame_metric_epigraph_dense.__file__), Path(frame_curvature_epigraph_exchange.__file__)]
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in files}


def configuration(base, *, origin_budget_exact, target_budget_exact, curvature_cap_exact):
    old, target, cap = map(Q, (origin_budget_exact, target_budget_exact, curvature_cap_exact))
    if not 0 < target < old < 1 or cap <= 0:
        raise ValueError('0 < new metric target < previously valid budget < 1 and positive fixed curvature cap required')
    if Q(base['fixed_metric_budget_exact']) != old:
        raise ValueError('previously valid budget must match the supplied original configuration')
    result = copy.deepcopy(base)
    result.update(metric_restoration_schema=SCHEMA, previous_qualified_metric_budget_exact=str(old),
        fixed_metric_budget_exact=str(target), fixed_hard_curvature_cap_exact=str(cap),
        metric_recovery_group_indices=[0, 1], hard_group_indices=list(range(2, 11)),
        metric_recovery_row_roles=list(ROLES),
        hard_curvature_uses_complete_actual_position_two_jets=True,
        fine_hard_curvature_requires_new_groups_7_to_10=True,
        only_constraint_definition_not_physical_g_or_state_changes=True)
    return result


def _grid(radial, theta):
    r, th = np.asarray(radial, float), np.asarray(theta, float)
    if (r.ndim != 1 or th.ndim != 1 or len(r) < 2 or len(th) < 4
            or not np.all(np.isfinite(r)) or not np.all(np.isfinite(th))
            or r[0] != 0 or np.any(np.diff(r) <= 0)
            or not np.array_equal(th, np.arange(len(th))*2*np.pi/len(th))):
        raise ValueError('complete increasing radial chart from zero and original full uniform angle circle required')
    return r, th


def constraint_definition(cfg, context, radial, theta):
    r, th = _grid(radial, theta)
    if set(context) != set(CONTEXT_KEYS):
        raise ValueError('fixed context only: no changing current-state hash or omitted physical binding')
    if any(not isinstance(context[k], str) or len(context[k]) != 64
           or any(c not in '0123456789abcdef' for c in context[k]) for k in CONTEXT_KEYS):
        raise ValueError('complete hexadecimal fixed-context hashes required')
    result = {'schema': SCHEMA, 'fixed_physical_context': copy.deepcopy(context),
        'configuration': copy.deepcopy(cfg), 'group_order': list(GROUPS), 'roles': list(ROLES),
        'fine_flat_index_rule': 'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index',
        'radial_nodes_exact_binary64': [str(Q.from_float(float(x))) for x in r],
        'theta_nodes_exact_binary64': [str(Q.from_float(float(x))) for x in th],
        'legacy_first_seven_integer_row_indices_preserved': True,
        'complete_uniform_angle_queries_not_isolated_points': True,
        'batch_requires_original_zero_and_last_radial_nodes': True,
        'height_mean_and_common_primitive_do_not_follow_query_subset': True,
        'fine_curvature_batches_require_full_two_jet_jacobian': True,
        'physical_state_hash_owned_by_unchanged_external_family': True,
        'source_files_sha256': implementation_hashes()}
    result['definition_sha256'] = digest(result)
    return result


def _indices(values, total):
    raw = list(values)
    if any(isinstance(i, (bool, np.bool_)) or not isinstance(i, (int, np.integer)) for i in raw):
        raise ValueError('integer original-grid row indices required')
    result = np.asarray(sorted(set(int(i) for i in raw)), np.int64)
    if np.any(result < 0) or np.any(result >= total):
        raise ValueError('row index outside declared full grid')
    return result


def fine_coordinates(indices, radial, theta):
    r, th = _grid(radial, theta); Nr, Nt = len(r), len(th)
    ids = _indices(indices, 11*Nr*Nt)
    result = []
    for value in ids:
        group, point = divmod(int(value), Nr*Nt); ri, ti = divmod(point, Nt)
        result.append({'fine_flat_index': int(value), 'group_index': group, 'group': GROUPS[group],
            'role': ROLES[group], 'radial_index': ri, 'fine_theta_index': ti,
            't': float(r[ri]), 'theta': float(th[ti]),
            't_exact_binary64': str(Q.from_float(float(r[ri]))),
            'theta_exact_binary64': str(Q.from_float(float(th[ti]))),
            'theta_over_pi_exact': str(Q(2*ti, Nt))})
    return result


def extend_fine_pool(previous_record, additional_indices, radial, theta, *, maximum_rows=4096):
    """Append new groups after legacy 0..6; never renumber or delete old rows."""
    r, th = _grid(radial, theta); count = len(r)*len(th)
    old_names = previous_record.get('group_order')
    if old_names not in [list(GROUPS[:7]), list(GROUPS)]:
        raise ValueError('the predecessor must be an exact seven- or eleven-group pool')
    old = _indices(previous_record.get('row_indices', []), len(old_names)*count)
    if (not len(old) or old.tolist() != previous_record.get('row_indices')
            or previous_record.get('row_count') != len(old)
            or previous_record.get('row_indices_sha256') != digest(old.tolist())
            or previous_record.get('total_full_grid_rows') != len(old_names)*count
            or previous_record.get('flat_index_rule') != 'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index'):
        raise ValueError('predecessor indices/group/hash/layout differs')
    added = _indices(additional_indices, 11*count)
    combined = np.union1d(old, added)
    if len(combined) > maximum_rows:
        raise ValueError('explicit new pool capacity exceeded; do not drop old rows')
    new = np.setdiff1d(combined, old)
    return {'schema': SCHEMA+'-fine-pool', 'group_order': list(GROUPS), 'roles': list(ROLES),
        'source_previous_pool_sha256': digest(previous_record),
        'row_count': len(combined), 'row_indices': combined.tolist(),
        'row_indices_sha256': digest(combined.tolist()), 'total_full_grid_rows': 11*count,
        'flat_index_rule': 'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index',
        'added_row_indices': new.tolist(), 'added_original_grid_coordinates': fine_coordinates(new, r, th),
        'every_previous_integer_index_retained_without_reindexing': True,
        'old_row_values_must_be_rescored_under_explicit_new_gate_definition': True}


def required_parameter_jet_order(groups):
    values = np.asarray(groups)
    if values.ndim != 1 or values.dtype.kind not in 'iu' or np.any(values < 0) or np.any(values >= 11):
        raise ValueError('known eleven group integer labels required')
    return 2 if np.any(values >= 7) else 1


def _ordinary_consistency(data, a):
    T, Xt = np.asarray(data['T'], float), np.asarray(data['Xt'], float)
    if T.shape != Xt.shape or not T.shape or T.shape[-1] != 3:
        raise ValueError('matching complete T and Xtheta vectors required')
    radius = np.broadcast_to(np.asarray(a, float), T.shape[:-1])
    if np.any(radius <= 0) or not np.all(np.isfinite(radius)):
        raise ValueError('fixed finite positive target a required')
    difference = float(np.max(abs(Xt/radius[..., None]-T)))
    unit = float(np.max(abs(np.sum(T*T, axis=-1)-1)))
    if not np.all(np.isfinite(T)) or not np.all(np.isfinite(Xt)) or difference > 5e-12 or unit > 5e-12:
        raise ValueError('this direct metric formula requires the actual unit tangent T=Xtheta/a')
    return radius


def row_values(data, a, side, cfg):
    if side not in [-1, 1]:
        raise ValueError('side must be plus or minus one')
    radius = _ordinary_consistency(data, a)
    cap, scale = float(Q(cfg['fixed_hard_curvature_cap_exact'])), float(Q(cfg['curvature_scale_exact']))
    if cap <= 0 or scale <= 0:
        raise ValueError('positive fixed curvature cap and row scale required')
    actual = curvature_values(data, radius, 1/cap, area_floor=cfg['normal_area_numerical_floor'])
    factors = np.array([cap/scale, (cap/scale)**2, cap/scale, (cap/scale)**2])
    curvature = actual['rows']*factors
    physical = physical_rows(data, side, cfg)
    rows = np.concatenate([physical, np.moveaxis(curvature, -1, 0)])
    return {'rows': rows, 'eta': geometry_values(data)['eta'],
        'principal_curvatures': independent_principal_curvatures(actual),
        'normal_area': actual['q'], 'mirror': mirror_values(data, float(Q(cfg['mirror_target_exact']))),
        'fixed_curvature_cap_exact': cfg['fixed_hard_curvature_cap_exact'],
        'metric_target_exact': cfg['fixed_metric_budget_exact'], 'roles': ROLES,
        'configuration_sha256': digest(cfg),
        'ordinary_consistency_uses_same_a_and_T': True}


def selected_parameter_jacobian(data, a, groups, side, cfg):
    """One derivative row per selected point; no epigraph auxiliary column.

    The caller must form data using complete uniform-angle geometry queries,
    then select points. This function never evaluates a periodic primitive.
    """
    g = np.asarray(groups); order = required_parameter_jet_order(g)
    X, JX = np.asarray(data['X'], float), np.asarray(data['jac_X'], float)
    if X.ndim != 2 or X.shape != (len(g), 3) or JX.ndim != 3 or JX.shape[:2] != X.shape:
        raise ValueError('matching selected physical vectors and parameter axes required')
    radius = _ordinary_consistency(data, a)
    JT, Jt = np.asarray(data['jac_T'], float), np.asarray(data['jac_Xt'], float)
    if JT.shape != JX.shape or Jt.shape != JX.shape:
        raise ValueError('same-layout tangent and angular-position Jacobians required')
    scale_j = max(1., float(np.max(abs(JT))))
    if (np.max(abs(Jt/radius[:, None, None]-JT)) > 5e-12*scale_j
            or np.max(abs(np.einsum('ic,icn->in', data['T'], JT))) > 5e-12*scale_j):
        raise ValueError('parameter direction must respect fixed a and the actual unit tangent')
    result = np.empty((len(g), JX.shape[-1]))
    physical = g < 7; curved = ~physical
    if np.any(physical):
        small = {k: np.asarray(data[k])[physical] for k in
                 ['X', 'Xs', 'T', 'jac_X', 'jac_Xs', 'jac_T']}
        result[physical] = selected_physical_derivatives(small, g[physical], side, cfg)
    if order == 2:
        required = ['Xs', 'Xt', 'Xss', 'Xst', 'Xtt']
        if any('jac_'+k not in data for k in required):
            raise ValueError('fine hard-curvature rows require every true second-jet parameter derivative')
        small = {k: np.asarray(data[k])[curved] for k in required}
        small.update({'jac_'+k: np.asarray(data['jac_'+k])[curved] for k in required})
        cap, scale = float(Q(cfg['fixed_hard_curvature_cap_exact'])), float(Q(cfg['curvature_scale_exact']))
        jac = curvature_parameter_jacobian(small, radius[curved], 1/cap,
            area_floor=cfg['normal_area_numerical_floor'])
        factors = np.array([cap/scale, (cap/scale)**2, cap/scale, (cap/scale)**2])
        labels = g[curved]-7
        result[curved] = jac[np.arange(len(labels)), labels]*factors[labels, None]
    if not np.all(np.isfinite(result)):
        raise FloatingPointError('nonfinite new full-row parameter Jacobian')
    return result


def single_grid_decision(data, values, cfg, *, reconstructed_cap_and_box_pass):
    """Same immutable data/configuration; separate hard/old/new qualifications.

    The enclosing objective must bind the supplied data and values to the same
    physical state, as it already does for the other shared geometry caches.
    """
    if values.get('configuration_sha256') != digest(cfg):
        raise ValueError('row values and the exact constraint configuration differ')
    rows = values['rows']; eta = float(np.max(values['eta']))
    tolerance = np.array([cfg['metric_row_tolerance']]*2 + [cfg['signed_height_tolerance']] +
        [cfg['shape_constraint_tolerance']]*3 + [cfg['mirror_polynomial_tolerance']] +
        [cfg['curvature_row_tolerance']]*4)
    minima = np.min(rows.reshape(11, -1), axis=1)
    maximum_k = float(np.max(abs(values['principal_curvatures'])))
    cap = float(Q(cfg['fixed_hard_curvature_cap_exact']))
    mirror = values['mirror']['radius']; finite = np.isfinite(mirror)
    mirror_min = float(np.min(mirror[finite])) if np.any(finite) else None
    direct_mirror = mirror_min is None or mirror_min >= float(Q(cfg['mirror_target_exact']))-cfg['mirror_radius_tolerance']
    hard = bool(reconstructed_cap_and_box_pass and np.all(minima[2:] >= -tolerance[2:])
        and maximum_k <= cap+cfg['direct_curvature_tolerance'] and direct_mirror
        and np.min(values['normal_area']) > cfg['normal_area_numerical_floor'])
    e, f = geometry_values(data)['e'], geometry_values(data)['f']
    origin = float(Q(cfg['previous_qualified_metric_budget_exact']))
    old_rows = metric_rows(e, f, origin)
    old_pass = bool(eta <= origin+cfg['direct_eta_tolerance'] and
        min(float(np.min(v)) for v in old_rows) >= -cfg['metric_row_tolerance'])
    target_pass = bool(eta <= float(Q(cfg['fixed_metric_budget_exact']))+cfg['direct_eta_tolerance']
        and np.all(minima[:2] >= -tolerance[:2]))
    return {'single_grid_hard_gate_pass': hard, 'previous_metric_budget_pass': old_pass,
        'new_metric_target_pass': target_pass, 'single_grid_admissible_recovery_point': bool(hard and old_pass),
        'single_grid_new_target_qualified': bool(hard and target_pass),
        'direct_max_eta': eta, 'direct_maximum_absolute_principal_curvature': maximum_k,
        'direct_mirror_radius_min_finite': mirror_min, 'row_minima': dict(zip(GROUPS, minima.tolist())),
        'two_grid_monotone_eta_acceptance_still_required': True,
        'no_continuous_isometry_curvature_or_reach_certificate': True}


def _artificial_data(parameters, radial, theta):
    p = np.asarray(parameters, float); r, th = np.meshgrid(radial, theta, indexing='ij')
    shape = r.shape+(3,); js = shape+(3,)
    a = np.broadcast_to((1+.1*np.asarray(radial))[:, None], r.shape)
    X = np.stack([.1*np.cos(th), .1*np.sin(th), .2+.01*r], axis=-1)
    JX = np.broadcast_to(np.array([[.02,.01,-.02],[-.01,.03,.02],[.03,.02,.01]]), js).copy()
    X += np.einsum('...cn,n->...c', JX, p)
    U = np.stack([1+.05*r, .1*np.cos(th), .08*np.sin(th)], axis=-1)
    JU = np.broadcast_to(np.array([[0.,.1,0.],[0.,.03,.02],[0.,.02,-.03]]), js).copy()
    U += np.einsum('...cn,n->...c', JU, p)
    angle = th+.05*p[0]
    T = np.stack([np.zeros_like(th),np.cos(angle),np.sin(angle)],axis=-1)
    JT = np.zeros(js); JT[...,1,0]=-.05*np.sin(angle); JT[...,2,0]=.05*np.cos(angle)
    data = {'X':X,'Xs':U,'T':T,'Xt':a[...,None]*T,
        'jac_X':JX,'jac_Xs':JU,'jac_T':JT,'jac_Xt':a[...,None,None]*JT}
    for i, key in enumerate(['Xss','Xst','Xtt']):
        J = np.broadcast_to(np.array([[.01,.02,0.],[.02,0.,.01],[.03,-.02,.02]])*(i+1),js).copy()
        value = np.zeros(shape); value[...,2]=.3+.1*i
        value += np.einsum('...cn,n->...c',J,p)
        data[key]=value; data['jac_'+key]=J
    return data,a


def artificial_check():
    from frame_curvature_epigraph_exchange import configuration as base_configuration
    from frame_curvature_mixed_grid_steps import fine_row_coordinates
    base = base_configuration()
    cfg = configuration(base,origin_budget_exact='167/625',target_budget_exact='1/4',curvature_cap_exact='2')
    radial=np.array([0.,.4,1.]); theta=np.arange(8)*2*np.pi/8; count=len(radial)*len(theta)
    legacy_ids=[0,7,2*count+3,6*count+5]
    legacy={'row_indices':legacy_ids,'row_count':len(legacy_ids),'row_indices_sha256':digest(legacy_ids),
        'group_order':list(GROUPS[:7]),'total_full_grid_rows':7*count,
        'flat_index_rule':'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index'}
    pool=extend_fine_pool(legacy,[7*count+1,10*count+2],radial,theta)
    oldcoords=fine_row_coordinates(legacy_ids,radial,theta)
    newcoords=fine_coordinates(legacy_ids,radial,theta)
    retained=set(legacy_ids).issubset(pool['row_indices']) and all(
        all(a[k]==b[k] for k in ['fine_flat_index','group_index','group','radial_index','fine_theta_index','t','theta'])
        for a,b in zip(oldcoords,newcoords,strict=True))
    context={k:digest({'artificial':k}) for k in CONTEXT_KEYS}
    d1=constraint_definition(cfg,context,radial,theta)
    cfg2=configuration(base,origin_budget_exact='167/625',target_budget_exact='6/25',curvature_cap_exact='2')
    d2=constraint_definition(cfg2,context,radial,theta)
    identity=bool(d1['definition_sha256']!=d2['definition_sha256'] and d1['fixed_physical_context']==d2['fixed_physical_context'])
    p=np.array([.02,-.03,.01]); data,a=_artificial_data(p,radial,theta); values=row_values(data,a,1,cfg)
    groups=np.arange(11); pts=(2*groups)%count
    selected={k:np.asarray(v).reshape((-1,)+np.asarray(v).shape[2:])[pts] for k,v in data.items()}
    jac=selected_parameter_jacobian(selected,a.ravel()[pts],groups,1,cfg)
    errors=[]; step=2e-6
    for j in range(3):
        direction=np.eye(3)[j]
        plus,ap=_artificial_data(p+step*direction,radial,theta)
        minus,am=_artificial_data(p-step*direction,radial,theta)
        vp=row_values(plus,ap,1,cfg)['rows'].reshape(11,-1)[groups,pts]
        vm=row_values(minus,am,1,cfg)['rows'].reshape(11,-1)[groups,pts]
        errors.append(float(np.max(abs((vp-vm)/(2*step)-jac[:,j]))))
    missing=False
    try:
        bad=dict(selected); del bad['jac_Xss']; selected_parameter_jacobian(bad,a.ravel()[pts],groups,1,cfg)
    except ValueError:missing=True
    wrong_id=False
    try:extend_fine_pool(legacy,[11*count],radial,theta)
    except ValueError:wrong_id=True
    decision=single_grid_decision(data,values,cfg,reconstructed_cap_and_box_pass=True)
    separated=('previous_metric_budget_pass' in decision and 'new_metric_target_pass' in decision
        and decision['two_grid_monotone_eta_acceptance_still_required'])
    passed=bool(retained and identity and max(errors)<2e-8 and missing and wrong_id and separated
        and required_parameter_jet_order(np.array([0,6]))==1 and required_parameter_jet_order(np.array([0,10]))==2)
    return {'schema':SCHEMA+'-artificial-check','artificial_inputs_only':True,
        'research_candidate_loaded_evaluated_or_optimized':False,
        'legacy_fine_indices_and_coordinates_preserved':bool(retained),
        'new_budget_changes_constraint_identity_not_fixed_physical_context':identity,
        'complete_eleven_group_parameter_Jacobian_max_errors':errors,
        'missing_fine_second_jet_derivative_rejected':missing,'out_of_range_new_index_rejected':wrong_id,
        'old_budget_new_target_and_hard_decisions_separate':separated,
        'no_optimizer_or_actual_budget_configuration_selected':True,'passed':passed}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true'); parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if not args.check_only:
        parser.error('this interface has only an artificial --check-only CLI; no actual solver path')
    before=time.monotonic(); result=artificial_check()
    result.update(source_files_sha256=implementation_hashes(),elapsed_seconds=time.monotonic()-before)
    atomic_save(args.out,result); print(json.dumps({'out':str(args.out),'passed':result['passed']}))
    if not result['passed']:raise SystemExit(1)


if __name__=='__main__':main()
