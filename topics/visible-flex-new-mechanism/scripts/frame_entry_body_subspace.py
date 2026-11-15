#!/usr/bin/env python3
"""Pure-array 103-column entry/body proposal models for the published 163 layout.

No geometry, research input loader or optimizer is imported. The exact support
classification is a proved property of this one declared layout, not a test of
small Jacobian entries. Original whole-grid gates remain the caller's duty.
The only CLI executes artificial arrays; it cannot load a research candidate.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
import hashlib
import json
from numbers import Integral
from pathlib import Path
import numpy as np

SCHEMA = 'same-163-entry-body103-array-model-v1'
GROUP_COUNT = 11
ACTUAL_FLAGS = (
    'regularity_screen_pass', 'previous_metric_budget_pass',
    'single_grid_hard_gate_pass', 'hard_ball_pass', 'hard_strip_pass',
    'outer_strip_pass', 'signed_height_pass', 'mirror_polynomial_pass',
    'independent_direct_mirror_radius_pass', 'curvature_lambda_bound_pass',
    'curvature_scaled_PSD_row_pass', 'independent_direct_curvature_pass',
    'single_grid_admissible_recovery_point', 'cap_and_box_eligible')


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                     allow_nan=False).encode()).hexdigest()


def exact(value):
    """An explicit rational identity; never reinterpret an unlabelled float."""
    if isinstance(value, bool):
        raise ValueError('boolean is not an exact rational node')
    if isinstance(value, Q):
        return value
    if isinstance(value, Integral):
        return Q(int(value))
    if isinstance(value, str):
        return Q(value)
    if isinstance(value, dict) and set(value) == {'numerator', 'denominator'}:
        n, d = value['numerator'], value['denominator']
        if (isinstance(n, bool) or isinstance(d, bool)
                or not isinstance(n, Integral) or not isinstance(d, Integral) or d <= 0):
            raise ValueError('integer numerator and positive integer denominator required')
        return Q(int(n), int(d))
    raise ValueError('exact rational string/integer/Fraction identity required')


def finite(value, shape=None):
    out = np.array(value, dtype=np.float64, copy=True)
    if (shape is not None and out.shape != shape) or not np.all(np.isfinite(out)):
        raise ValueError('finite array with the declared shape required')
    out.flags.writeable = False
    return out


def array_digest(value):
    a = np.ascontiguousarray(value)
    return digest({'dtype': a.dtype.str, 'shape': list(a.shape),
                   'bytes_sha256': hashlib.sha256(a.tobytes()).hexdigest()})


def expected_layout():
    tc, tf, delta = Q(9, 250), Q(423, 500), Q(81, 1000)
    knots = [tc]*6 + [tc+j*delta for j in range(1, 10)] + [tf]*6
    return {'schema': 'published-entry-single-Q-163-layout-v1',
        'nunknown': 163, 'slices': {'u': [0, 81], 'v': [81, 154],
            'height': [154, 163], 'metric': [163, 163]},
        'flattening': 'radial-major/angular-minor', 'radial_free': 9,
        'u_angular_columns': 9, 'v_angular_columns_before_Q': 8,
        'radial_degree': 5, 'retained_original_basis_indices': list(range(3, 12)),
        'clamped_knots_exact': [str(x) for x in knots],
        'entry_left_exact': str(tc), 'entry_length_exact': '81/1000',
        'entry_cutoff': '1 on [0,ell/3]; 1-S9((3*x/ell-1)/2) to ell; 0 afterwards',
        'entry_weight': '1-chi+chi*(x/ell)^power',
        'entry_weight_powers': {'u': 2, 'v': 5},
        'normalized_Q_parameter_index': 153, 'Q_radial_basis_index': 3,
        'Q_weight_power': 5, 'length_exact': '9/10',
        'current_height_independent_of_current_u_v': True}


class EntryBody103Subspace:
    """The exact existing columns, with a full-state lift and no state loader."""
    def __init__(self, layout):
        want = expected_layout()
        if not isinstance(layout, dict) or set(layout) != set(want):
            raise ValueError('complete published layout descriptor required')
        normalized = dict(layout)
        normalized['clamped_knots_exact'] = [str(exact(x)) for x in layout['clamped_knots_exact']]
        for key in ['entry_left_exact', 'entry_length_exact', 'length_exact']:
            normalized[key] = str(exact(layout[key]))
        if normalized != want:
            raise ValueError('the proved support belongs to this exact 163-column layout only')
        self.layout = want
        self.columns = np.r_[np.arange(54), np.arange(81, 129), [153]].astype(np.int64)
        self.fixed_columns = np.setdiff1d(np.arange(163), self.columns)
        self.columns.flags.writeable = self.fixed_columns.flags.writeable = False
        self.left, self.right, self.length = Q(9, 250), Q(153, 200), Q(9, 10)
        self.definition = {'schema': SCHEMA, 'layout': want,
            'columns': self.columns.tolist(), 'fixed_columns': self.fixed_columns.tolist(),
            'variable_radial_open_interval_exact': [str(self.left), str(self.right)],
            'endpoints_are_constant_by_zero_two_jets': True,
            'fixed_height_and_fixed_radial_metric_required': True,
            'classification_uses_exact_radial_support_not_small_Jacobian': True}
        self.definition_sha256 = digest(self.definition)

    def lift_step(self, selected):
        selected = finite(selected, (103,))
        full = np.zeros(163)
        full[self.columns] = selected
        return full

    def apply(self, state, selected):
        state = finite(state, (163,))
        out = state.copy()
        out[self.columns] = state[self.columns] + finite(selected, (103,))
        if out[self.fixed_columns].tobytes() != state[self.fixed_columns].tobytes():
            raise ArithmeticError('fixed 60 coefficients changed')
        return out

    def restrict_jacobian(self, jacobian):
        J = finite(jacobian)
        if J.ndim != 2 or J.shape[1] != 163:
            raise ValueError('full original 163-column selected-row Jacobian required')
        return J[:, self.columns]


class RationalRowGrid:
    def __init__(self, label, radial_nodes_exact, angular_nodes):
        if (not isinstance(label, str) or not label or isinstance(angular_nodes, bool)
                or not isinstance(angular_nodes, Integral) or angular_nodes < 4 or angular_nodes % 4):
            raise ValueError('named full uniform angular grid, positive multiple of four required')
        self.nodes = tuple(exact(x) for x in radial_nodes_exact)
        if (len(self.nodes) < 2 or self.nodes[0] != 0 or self.nodes[-1] != Q(9, 10)
                or any(a >= b for a, b in zip(self.nodes, self.nodes[1:]))):
            raise ValueError('strict complete rational radial chart [0,9/10] required')
        self.label, self.nt = label, int(angular_nodes)
        self.nr = len(self.nodes)
        self.point_count = self.nr*self.nt
        self.total_rows = GROUP_COUNT*self.point_count
        self.definition = {'schema': 'original-group-major-rational-row-grid-v1',
            'label': label, 'radial_nodes_exact': [str(x) for x in self.nodes],
            'angular_nodes': self.nt, 'theta_rule': '2*pi*j/Ntheta', 'groups': 11,
            'flat_index_rule': 'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index'}
        self.definition_sha256 = digest(self.definition)

    def ids(self, values):
        a = np.asarray(values)
        if not a.size:
            a = np.array([], dtype=np.int64)
        if (a.ndim != 1 or a.dtype.kind not in 'iu' or len(np.unique(a)) != len(a)
                or np.any(a < 0) or np.any(a >= self.total_rows)):
            raise ValueError('distinct original integer row IDs required')
        return np.asarray(a, dtype=np.int64)

    def classify(self, values, subspace):
        ids = self.ids(values)
        groups = ids//self.point_count
        points = ids % self.point_count
        radial, angular = points//self.nt, points % self.nt
        variable_nodes = np.array([subspace.left < t < subspace.right for t in self.nodes])
        variable = variable_nodes[radial]
        return {'ids': ids, 'groups': groups, 'radial_indices': radial,
            'angular_indices': angular, 'variable': variable,
            'constant_soft': (~variable) & (groups < 2),
            'constant_hard': (~variable) & (groups >= 2)}

    def coordinate(self, flat_id):
        flat = int(self.ids([flat_id])[0])
        group, point = divmod(flat, self.point_count)
        ri, ai = divmod(point, self.nt)
        return {'grid': self.label, 'flat_row_id': flat, 'group': group,
            'radial_index': ri, 'theta_index': ai, 't_exact': str(self.nodes[ri]),
            'theta_over_pi_exact': str(Q(2*ai, self.nt))}


class FullGridValues:
    """Already evaluated full rows, actual eta and fixed common b, never geometry."""
    def __init__(self, grid, rows, eta, b, tolerances, mean_Xs=None):
        self.grid = grid
        self.rows = finite(rows, (11, grid.nr, grid.nt))
        self.eta = finite(eta, (grid.nr, grid.nt))
        self.b = finite(b, (grid.nr,))
        t = np.asarray(tolerances, float)
        if t.shape == (11,):
            t = np.broadcast_to(t[:, None, None], self.rows.shape)
        self.tolerances = finite(t, self.rows.shape)
        if np.any(self.eta < 0) or np.any(self.tolerances < 0):
            raise ValueError('nonnegative actual eta and declared row tolerances required')
        self.mean_Xs = None if mean_Xs is None else finite(mean_Xs, (grid.nr, 3))


def fixed_domain_summary(subspace, full_grids):
    if (len(full_grids) != 2 or full_grids[0].grid.label == full_grids[1].grid.label
            or full_grids[0].grid.nodes != full_grids[1].grid.nodes
            or full_grids[1].grid.nt != 2*full_grids[0].grid.nt
            or not np.array_equal(full_grids[0].b, full_grids[1].b)):
        raise ValueError('both original/doubled angle grids and same fixed common b required')
    rho_out, eta_out, eta_all, b_bound = 0., -1., -1., 0.
    rho_location = eta_location = global_location = b_location = None
    details = []
    invariant_hard_pass = True
    for item in full_grids:
        g = item.grid
        outside = np.array([not(subspace.left < t < subspace.right) for t in g.nodes])
        outside_ids = np.flatnonzero(outside)
        soft = item.rows[:2, outside, :]
        sk = np.unravel_index(int(np.argmin(soft)), soft.shape)
        sg, sr, st = sk[0], int(outside_ids[sk[1]]), sk[2]
        candidate = max(0., -float(soft[sk]))
        sloc = g.coordinate(sg*g.point_count+sr*g.nt+st)
        if rho_location is None or candidate > rho_out:
            rho_out, rho_location = candidate, sloc
        ext_eta = item.eta[outside]
        ek = np.unravel_index(int(np.argmax(ext_eta)), ext_eta.shape)
        eri, eai = int(outside_ids[ek[0]]), ek[1]
        ev = float(ext_eta[ek]); eloc = g.coordinate(eri*g.nt+eai)
        if ev > eta_out:
            eta_out, eta_location = ev, eloc
        ak = np.unravel_index(int(np.argmax(item.eta)), item.eta.shape)
        av = float(item.eta[ak]); aloc = g.coordinate(ak[0]*g.nt+ak[1])
        if av > eta_all:
            eta_all, global_location = av, aloc
        hard_margin = item.rows[2:, outside, :] + item.tolerances[2:, outside, :]
        hk = np.unravel_index(int(np.argmin(hard_margin)), hard_margin.shape)
        hloc = g.coordinate((hk[0]+2)*g.point_count+int(outside_ids[hk[1]])*g.nt+hk[2])
        hp = bool(np.min(hard_margin) >= 0)
        invariant_hard_pass = invariant_hard_pass and hp
        bounds = np.maximum(0., item.b**2-1.)
        bi = int(np.argmax(bounds)); bv = float(bounds[bi])
        if b_location is None or bv > b_bound:
            b_bound = bv
            b_location = {'grid': g.label, 'radial_index': bi,
                't_exact': str(g.nodes[bi]), 'b_evaluated': float(item.b[bi])}
        consistency = None
        if item.mean_Xs is not None:
            target = np.zeros_like(item.mean_Xs); target[:, 2] = item.b
            consistency = float(np.max(abs(item.mean_Xs-target)))
        details.append({'grid': g.definition, 'full_values_are_not_only_pool_values': True,
            'outside_radial_count': int(outside.sum()),
            'outside_soft_row_count': int(2*outside.sum()*g.nt),
            'outside_soft_lower_bound': candidate, 'outside_soft_attainer': sloc,
            'outside_true_eta': ev, 'outside_true_eta_location': eloc,
            'full_true_eta': av, 'full_true_eta_location': aloc,
            'outside_hard_original_tolerance_pass': hp,
            'outside_hard_minimum_value_plus_tolerance': float(np.min(hard_margin)),
            'outside_hard_minimum_location': hloc,
            'fixed_height_Jensen_lower_bound_evaluated': bv,
            'fixed_height_bound_location': {'t_exact': str(g.nodes[bi]), 'radial_index': bi},
            'mean_Xs_minus_fixed_b_ez_max': consistency})
    return {'schema': SCHEMA+'-fixed-domain', 'subspace_sha256': subspace.definition_sha256,
        'rho_out': rho_out, 'rho_out_attainer': rho_location,
        'eta_out': eta_out, 'eta_out_location': eta_location,
        'full_true_eta': eta_all, 'full_true_eta_location': global_location,
        'maximum_drop_before_fixed_outside_floor': eta_all-eta_out,
        'fixed_height_Jensen_lower_bound_evaluated': b_bound,
        'fixed_height_bound_location': b_location,
        'outside_hard_original_tolerance_pass': invariant_hard_pass,
        'grids': details, 'no_additional_geometry_call': True,
        'finite_values_are_not_continuous_error_bounds': True,
        'fixed_b_Jensen_diagnostic_is_not_used_as_a_validated_numeric_rejection': True}


@dataclass(frozen=True)
class ConstantCapGate:
    affine_margin: float
    reconstructed_margin: float
    height_tolerance: float
    reconstruction_difference_absolute: float
    reconstruction_consistency_tolerance: float

    def report(self):
        a = finite([self.affine_margin, self.reconstructed_margin, self.height_tolerance,
                    self.reconstruction_difference_absolute, self.reconstruction_consistency_tolerance])
        if np.any(a[2:] < 0):
            raise ValueError('nonnegative original constant-cap tolerances required')
        return {'schema': 'fixed-u-v-independent-cap-original-gate-v1',
            'affine_margin': float(a[0]), 'reconstructed_margin': float(a[1]),
            'height_tolerance': float(a[2]), 'reconstruction_difference_absolute': float(a[3]),
            'reconstruction_consistency_tolerance': float(a[4]),
            'original_tolerance_pass': bool(min(a[0], a[1]) >= -a[2] and a[3] <= a[4]),
            'strict_nonnegative_margins': bool(min(a[0], a[1]) >= 0),
            'no_strict_zero_Jacobian_LP_row_added': True}


def initial_restriction_decision(summary, original_gate_flags, *, new_target_qualified,
        minimum_drop_exact='1/10000000', target_exact='13/50', actual_eta_tolerance=1e-9):
    if not isinstance(new_target_qualified, bool):
        raise ValueError('actual two-grid new-target decision must be explicit')
    labels = [r['grid']['label'] for r in summary['grids']]
    gates_pass = all(original_gate_flags.get(label, {}).get(k) is True
                     for label in labels for k in ACTUAL_FLAGS)
    old, outside = float(summary['full_true_eta']), float(summary['eta_out'])
    drop, target = float(exact(minimum_drop_exact)), float(exact(target_exact))
    if min(drop, actual_eta_tolerance) < 0 or not all(np.isfinite([old, outside, drop, target, actual_eta_tolerance])):
        raise ValueError('finite original acceptance thresholds required')
    if not gates_pass or not summary['outside_hard_original_tolerance_pass']:
        status = 'initial-original-whole-grid-gate-failed'
    elif new_target_qualified:
        status = 'new-target-already-qualified-no-LP'
    elif outside >= old:
        status = 'fixed-outside-locks-current-strict-maximum-no-LP'
    elif old-outside < drop and outside > target+actual_eta_tolerance:
        status = 'fixed-outside-prevents-minimum-accepted-drop-and-target-no-LP'
    else:
        status = 'eligible-for-declared-restricted-proposal'
    return {'status': status, 'may_call_LP': status == 'eligible-for-declared-restricted-proposal',
        'original_all_grid_flags_pass': gates_pass, 'full_true_eta': old, 'eta_out': outside,
        'minimum_accepted_drop_exact': str(exact(minimum_drop_exact)),
        'target_exact': str(exact(target_exact)), 'actual_eta_tolerance': actual_eta_tolerance,
        'no_changed_actual_gate_or_continuous_nonexistence_claim': True}


class SelectedRows:
    def __init__(self, subspace, full_grid, original_ids, full_jacobian):
        self.full = full_grid
        self.parts = full_grid.grid.classify(original_ids, subspace)
        self.ids = self.parts['ids']
        self.J = finite(full_jacobian, (len(self.ids), 163))
        self.values = full_grid.rows.reshape(-1)[self.ids]
        self.tolerances = full_grid.tolerances.reshape(-1)[self.ids]


def _validate_center(subspace, state, lower, upper, cap):
    state, lower, upper = (finite(v, (163,)) for v in (state, lower, upper))
    if np.any(lower >= upper) or np.any(state < lower) or np.any(state > upper):
        raise ValueError('accepted full163 state must obey all original boxes')
    cr = cap.report()
    if not cr['original_tolerance_pass']:
        raise ValueError('constant cap does not pass its original gate')
    return state, lower, upper, cr


class ArrayLP:
    """A scalar affine LP description only; no solver or acceptance authority."""
    def __init__(self, A, b, c, lower, upper, *, information):
        self.A, self.b, self.c = finite(A), finite(b), finite(c)
        self.lower = np.array(lower, float, copy=True)
        self.upper = np.array(upper, float, copy=True)
        if (self.A.shape != (len(self.b), len(self.c))
                or self.lower.shape != self.c.shape or self.upper.shape != self.c.shape
                or np.any(np.isnan(self.lower)) or np.any(np.isnan(self.upper))
                or np.any(self.lower > self.upper)):
            raise ValueError('consistent LP arrays and intervals required')
        self.lower.flags.writeable = self.upper.flags.writeable = False
        self.information = information

    def residual(self, variables):
        x = finite(variables, self.c.shape)
        return {'maximum_original_linear_row_violation': max(0., float(np.max(self.A@x-self.b))),
            'maximum_original_linear_bound_violation': max(0., float(np.max(self.lower-x)), float(np.max(x-self.upper))),
            'objective_evaluated': float(self.c@x)}


def build_primary(subspace, full_grids, selections, state, lower, upper, cap, *,
        trust_exact, fraction_to_boundary_exact='1/2', physical_norm_weight_exact='1/1000',
        strip_floor_exact='1/10000000', curvature_floor_exact='1/10000000'):
    state, lower, upper, cap_record = _validate_center(subspace, state, lower, upper, cap)
    summary = fixed_domain_summary(subspace, full_grids)
    if not summary['outside_hard_original_tolerance_pass']:
        raise ValueError('constant outside hard row fails original tolerance')
    if len(selections) != 2 or any(s.full is not f for s, f in zip(selections, full_grids)):
        raise ValueError('selected J rows must belong to these same complete coarse/fine values')
    r, gamma, weight = map(float, [exact(trust_exact), exact(fraction_to_boundary_exact), exact(physical_norm_weight_exact)])
    strip_floor, curve_floor = float(exact(strip_floor_exact)), float(exact(curvature_floor_exact))
    if not(r > 0 and 0 < gamma <= 1 and weight >= 0 and min(strip_floor, curve_floor) >= 0):
        raise ValueError('positive declared trust and valid original target constants required')
    values, jacobians, groups, tols, tags = [], [], [], [], []
    invariant_rows, outside_J_max = [], 0.
    for selection in selections:
        parts, grid = selection.parts, selection.full.grid
        if np.any(selection.values[parts['groups'] >= 2] < -selection.tolerances[parts['groups'] >= 2]):
            raise ValueError('selected accepted hard rows must satisfy original tolerances')
        variable = parts['variable']
        Jsub = selection.J[:, subspace.columns]
        if np.any(~variable):
            outside_J_max = max(outside_J_max, float(np.max(abs(Jsub[~variable]))))
        for i in np.flatnonzero(~variable):
            invariant_rows.append({**grid.coordinate(int(selection.ids[i])),
                'role': 'outside-soft-aggregated' if parts['groups'][i] < 2 else 'outside-hard-original-tolerance'})
        values.extend(selection.values[variable]); jacobians.extend(Jsub[variable])
        groups.extend(parts['groups'][variable]); tols.extend(selection.tolerances[variable])
        tags.extend(grid.coordinate(int(i)) for i in selection.ids[variable])
    values, groups, tols = np.array(values, float), np.array(groups, int), np.array(tols, float)
    J = np.array(jacobians, float).reshape(-1, 103)
    n, m = 103, len(values); soft, hard = groups < 2, groups >= 2
    width = upper[subspace.columns]-lower[subspace.columns]
    scale = r*width
    target = values-gamma*(values+tols)
    target[soft] = 0.
    target[np.isin(groups, [4, 5])] = np.maximum(target[np.isin(groups, [4, 5])], strip_floor)
    target[np.isin(groups, [7, 8, 9, 10])] = np.maximum(target[np.isin(groups, [7, 8, 9, 10])], curve_floor)
    A, b = np.zeros((m+2*n, n+2)), np.zeros(m+2*n)
    A[:m, :n] = -J*scale; b[:m] = values
    b[:m][hard] = values[hard]-target[hard]
    A[:m, n][soft] = -1.
    for j in range(n):
        A[m+j, j] = 1.; A[m+j, n+1] = -1.
        A[m+n+j, j] = -1.; A[m+n+j, n+1] = -1.
    lo = np.maximum(-1., (lower[subspace.columns]-state[subspace.columns])/scale)
    hi = np.minimum(1., (upper[subspace.columns]-state[subspace.columns])/scale)
    c = np.r_[np.zeros(n), 1., weight*r]
    rho0 = max(summary['rho_out'], 0., float(np.max(-values[soft])) if np.any(soft) else 0.)
    center_signature = {'subspace': subspace.definition_sha256, 'state': array_digest(state),
        'lower': array_digest(lower), 'upper': array_digest(upper), 'cap': cap_record,
        'selected_tags': tags, 'values': array_digest(values), 'Jacobian103': array_digest(J),
        'tolerances': array_digest(tols), 'outside_soft_lower_bound': summary['rho_out'],
        'fraction_to_boundary_exact': str(exact(fraction_to_boundary_exact)),
        'physical_norm_weight_exact': str(exact(physical_norm_weight_exact)),
        'strip_floor_exact': str(exact(strip_floor_exact)), 'curvature_floor_exact': str(exact(curvature_floor_exact))}
    info = {'schema': SCHEMA+'-primary', 'subspace_definition_sha256': subspace.definition_sha256,
        'trust_exact': str(exact(trust_exact)), 'trust_evaluated': r,
        'variables': '103 normalized selected steps, rho, one infinity-norm auxiliary',
        'physical_norm_weight_exact': str(exact(physical_norm_weight_exact)),
        'auxiliary_objective_coefficient': weight*r, 'rho_out': summary['rho_out'],
        'initial_selected_and_constant_metric_slack': rho0,
        'cap_invariant': cap_record, 'fixed_domain': summary,
        'active_original_rows': tags, 'invariant_original_rows': invariant_rows,
        'in_domain_zero_J_rows_kept': int(np.sum(np.all(J == 0, axis=1))),
        'outside_selected_J_max_diagnostic_only': outside_J_max,
        'row_classification_did_not_use_J_values': True,
        'no_cap_LP_row_added': True, 'original_complete_pools_not_mutated': True,
        'radius_independent_model_sha256': digest(center_signature)}
    result = ArrayLP(A, b, c, np.r_[lo, summary['rho_out'], 0.], np.r_[hi, np.inf, 1.], information=info)
    result.subspace, result.full_grids, result.selections = subspace, full_grids, selections
    result.state, result.original_lower, result.original_upper = state, lower, upper
    result.active_values, result.active_J, result.active_groups, result.active_tolerances = values, J, groups, tols
    result.targets, result.width, result.step_scale, result.trust = target, width, scale, r
    return result


def primary_physical_step(model, variables):
    x = finite(variables, model.c.shape)
    return model.subspace.lift_step(model.step_scale*x[:103])


def radius_mapped_witness(old_model, new_model, variables):
    if old_model.information['radius_independent_model_sha256'] != new_model.information['radius_independent_model_sha256']:
        raise ValueError('radius containment compares one center, row set, D and physical objective only')
    if new_model.trust < old_model.trust:
        raise ValueError('only enlargement is the declared feasible-set inclusion')
    x = finite(variables, old_model.c.shape).copy()
    ratio = old_model.trust/new_model.trust
    x[:103] *= ratio; x[-1] *= ratio
    return x


def constant_soft_budget_feasible(rho_out, budget):
    vals = finite([rho_out, budget])
    return bool(vals[1] >= vals[0])


def build_correction(primary, trial_full_grids, full_primary_step, *,
        physical_margin_retention_exact='1/4', predicted_descent_retention_exact='1/2',
        correction_relative_radius_exact='1/2', strip_floor_exact='1/10000000',
        curvature_floor_exact='1/10000000', improvement_floor=1e-10):
    """Original-unit SOC arrays; a separate positive scaling helper may consume them."""
    p = finite(full_primary_step, (163,)); S = primary.subspace.columns
    if np.any(p[primary.subspace.fixed_columns] != 0):
        raise ValueError('SOC primary step must have only the declared 103 coordinates')
    if len(trial_full_grids) != 2 or any(a.grid.definition != b.grid.definition
            for a, b in zip(primary.full_grids, trial_full_grids)):
        raise ValueError('actual same-y rows on the same full grids required')
    if any(not np.array_equal(a.b, b.b) for a, b in zip(primary.full_grids, trial_full_grids)):
        raise ValueError('fixed common height changed in trial input')
    trial = []
    for original, actual in zip(primary.selections, trial_full_grids):
        ids = original.ids[original.parts['variable']]
        trial.extend(actual.rows.reshape(-1)[ids])
    trial = np.array(trial, float)
    base, J, groups = primary.active_values, primary.active_J, primary.active_groups
    soft, hard = groups < 2, groups >= 2
    outside = primary.information['rho_out']
    linear = base+J@p[S]
    rho0 = primary.information['initial_selected_and_constant_metric_slack']
    rho1 = max(outside, 0., float(np.max(-linear[soft])) if np.any(soft) else 0.)
    norm = float(np.max(abs(p[S])/primary.width)); gain = rho0-rho1
    retention = float(exact(predicted_descent_retention_exact))
    gamma = float(exact(physical_margin_retention_exact)); relative = float(exact(correction_relative_radius_exact))
    if not(0 < retention <= 1 and 0 <= gamma <= 1 and relative > 0):
        raise ValueError('valid declared original SOC retention and radius required')
    info = {'schema': SCHEMA+'-SOC', 'source_primary_model_sha256': primary.information['radius_independent_model_sha256'],
        'initial_metric_slack': rho0, 'primary_predicted_metric_slack': rho1,
        'primary_predicted_improvement': gain, 'primary_box_normalized_norm': norm,
        'rho_out': outside, 'actual_y_rows_not_base_linear_rows': True,
        'full_original_rows_and_J_layout_unchanged_outside_this_array_projection': True}
    if norm == 0 or gain <= improvement_floor:
        return None, dict(info, status='no-primary-predicted-restoration-for-SOC')
    radius = relative*norm; budget = rho0-retention*gain
    info.update(metric_slack_budget=budget, maximum_box_normalized_correction=radius)
    if not constant_soft_budget_feasible(outside, budget):
        return None, dict(info, status='SOC-budget-below-fixed-outside-soft-bound')
    target = gamma*np.maximum(base, 0.)
    for gs, floor in [([4, 5], float(exact(strip_floor_exact))), ([7, 8, 9, 10], float(exact(curvature_floor_exact)))]:
        if floor < 0:
            raise ValueError('proposal floor must be nonnegative')
        mask = np.isin(groups, gs); target[mask] = np.maximum(target[mask], floor)
    n, m = 103, len(base)
    A, b = np.zeros((m+2*n, 2*n)), np.zeros(m+2*n)
    A[:m, :n] = -J*primary.width; b[:m] = trial-target
    b[:m][soft] = trial[soft]+budget
    for j in range(n):
        A[m+j, j] = 1.; A[m+j, n+j] = -1.
        A[m+n+j, j] = -1.; A[m+n+j, n+j] = -1.
    y = primary.state+p
    lo = np.maximum(-radius, (primary.original_lower[S]-y[S])/primary.width)
    hi = np.minimum(radius, (primary.original_upper[S]-y[S])/primary.width)
    if np.any(lo > hi):
        return None, dict(info, status='SOC-original-box-and-relative-radius-empty')
    info.update(status='original-unit-restricted-SOC-arrays-ready',
        active_original_rows=primary.information['active_original_rows'],
        no_cap_or_external_hard_restoration_row_added=True,
        original_unit_objective='sum h_j, h_j>=abs(D_S^-1 w_S_j)',
        caller_must_keep_original_unit_residual_and_all_whole_grid_gates=True)
    model = ArrayLP(A, b, np.r_[np.zeros(n), np.ones(n)], np.r_[lo, np.zeros(n)],
                    np.r_[hi, np.full(n, radius)], information=info)
    model.subspace, model.width, model.radius = primary.subspace, primary.width, radius
    model.active_trial_values, model.targets = trial, target
    return model, info


def developer_check():
    """Only small artificial arrays; no geometry construction or solver call."""
    import copy
    S = EntryBody103Subspace(expected_layout())
    nodes = ['0', '9/250', '9/100', '99/500', '33/50', '153/200', '39/50', '9/10']
    gc, gf = RationalRowGrid('coarse', nodes, 4), RationalRowGrid('fine', nodes, 8)
    arrays = []
    for g in [gc, gf]:
        rows = np.ones((11, g.nr, g.nt)); eta = np.full((g.nr, g.nt), .22)
        rows[:2] = -.01; eta[4] = .28
        rows[0, 0, 0] = -.012; rows[1, 6, -1] = -.013
        rows[8, 6] = 2e-8  # legal old hard value, below positive proposal floor
        b = np.ones(g.nr)*.7; means = np.zeros((g.nr, 3)); means[:, 2] = b
        arrays.append(FullGridValues(g, rows, eta, b, np.ones(11)*1e-9, means))
    cap = ConstantCapGate(0., -2.78e-17, 1e-9, 2.78e-17, 1e-10)
    state = np.linspace(-.2, .2, 163); state[54] = -0.
    lower, upper = np.full(163, -1.), np.full(163, 1.)
    chosen = []
    for item in arrays:
        g = item.grid
        ids = [0, g.point_count+6*g.nt+g.nt-1,
               2*g.nt, g.point_count+2*g.nt, 8*g.point_count+6*g.nt,
               8*g.point_count+4*g.nt]
        J = np.zeros((len(ids), 163)); J[2, 0] = 1.; J[3, 0] = 1.
        chosen.append(SelectedRows(S, item, ids, J))
    model = build_primary(S, arrays, chosen, state, lower, upper, cap, trust_exact='1/4000')
    summary = model.information['fixed_domain']
    flags = {g.label: {k: True for k in ACTUAL_FLAGS} for g in [gc, gf]}
    decision = initial_restriction_decision(summary, flags, new_target_qualified=False)
    step = np.linspace(-.001, .001, 103)
    lifted, candidate = S.lift_step(step), S.apply(state, step)
    layout_rejects = {}
    for key, value in [('nunknown', 162), ('normalized_Q_parameter_index', 152), ('radial_free', 10)]:
        bad = expected_layout(); bad[key] = value
        try: EntryBody103Subspace(bad); layout_rejects[key] = False
        except ValueError: layout_rejects[key] = True
    bad = expected_layout(); bad['clamped_knots_exact'][7] = .198
    try: EntryBody103Subspace(bad); layout_rejects['unlabelled-float-knot'] = False
    except ValueError: layout_rejects['unlabelled-float-knot'] = True
    endpoint_ids = [gc.nt, 5*gc.nt, 2*gc.nt]
    endpoint = gc.classify(endpoint_ids, S)
    variable_zero = [j for j, tag in enumerate(model.information['active_original_rows'])
                     if tag['group'] == 8 and tag['t_exact'] == '33/50']
    soft_constant = summary['rho_out']
    equiv = True
    for rho in [-.1, 0., .012, .013, .02]:
        all_rows = True
        for item in arrays:
            outside = np.array([not(S.left < t < S.right) for t in item.grid.nodes])
            all_rows = all_rows and bool(np.all(item.rows[:2, outside, :]+rho >= 0))
        equiv = equiv and ((rho >= soft_constant) == (rho >= 0 and all_rows))
    x = np.zeros(105); x[103] = .02
    feasible_original = max(model.residual(x).values()) == .02  # objective .02, residuals zero
    larger = build_primary(S, arrays, chosen, state, lower, upper, cap, trust_exact='1/2000')
    witness = x.copy(); witness[0] = .25; witness[-1] = .25
    mapped = radius_mapped_witness(model, larger, witness)
    containment = (model.residual(witness)['maximum_original_linear_row_violation'] == 0
        and larger.residual(mapped)['maximum_original_linear_row_violation'] == 0
        and larger.residual(mapped)['maximum_original_linear_bound_violation'] == 0
        and np.array_equal(primary_physical_step(model, witness), primary_physical_step(larger, mapped))
        and model.residual(witness)['objective_evaluated'] == larger.residual(mapped)['objective_evaluated'])
    # Same exact t but arbitrarily small/nonzero J does not alter classification.
    changed_J = chosen[0].J.copy(); changed_J[4, :] = 1e-200
    alt = SelectedRows(S, arrays[0], chosen[0].ids, changed_J)
    class_independent = np.array_equal(alt.parts['variable'], chosen[0].parts['variable'])
    false_floor = (model.information['fixed_domain']['outside_hard_original_tolerance_pass']
        and any(t['group'] == 8 and t['t_exact'] == '39/50'
                for t in model.information['invariant_original_rows'])
        and all(not(t['group'] == 8 and t['t_exact'] == '39/50')
                for t in model.information['active_original_rows']) and feasible_original)
    hard_zero_kept = bool(variable_zero and all(np.all(model.active_J[j] == 0) for j in variable_zero))
    # A low *internal* zero-J row is retained even if its floor makes this LP infeasible.
    inside_bad = []
    for item in arrays:
        rows = item.rows.copy(); rows[8, 4, 0] = 2e-8
        inside_bad.append(FullGridValues(item.grid, rows, item.eta, item.b, item.tolerances, item.mean_Xs))
    bad_selections = [SelectedRows(S, item, old.ids, old.J) for item, old in zip(inside_bad, chosen)]
    low_inside = build_primary(S, inside_bad, bad_selections, state, lower, upper, cap, trust_exact='1/4000')
    low_j = next(j for j, tag in enumerate(low_inside.information['active_original_rows'])
                 if tag['group'] == 8 and tag['t_exact'] == '33/50')
    internal_not_deleted = bool(np.all(low_inside.A[low_j] == 0) and low_inside.b[low_j] < 0)
    gate_rejects = []
    for badcap in [ConstantCapGate(0., -2e-9, 1e-9, 2e-9, 1e-8),
                   ConstantCapGate(0., 0., 1e-9, 2e-10, 1e-10)]:
        try: build_primary(S, arrays, chosen, state, lower, upper, badcap, trust_exact='1/4000'); gate_rejects.append(False)
        except ValueError: gate_rejects.append(True)
    frozen_bad = state.copy(); frozen_bad[60] = 2.
    try: build_primary(S, arrays, chosen, frozen_bad, lower, upper, cap, trust_exact='1/4000'); fixed_box_reject = False
    except ValueError: fixed_box_reject = True
    locked = copy.deepcopy(summary); locked['eta_out'] = locked['full_true_eta']
    lock_decision = initial_restriction_decision(locked, flags, new_target_qualified=False)
    narrow = copy.deepcopy(summary); narrow['eta_out'] = narrow['full_true_eta']-5e-8
    narrow_decision = initial_restriction_decision(narrow, flags, new_target_qualified=False)
    target_possible = copy.deepcopy(summary); target_possible['full_true_eta'] = .26000002; target_possible['eta_out'] = .25999999
    target_decision = initial_restriction_decision(target_possible, flags, new_target_qualified=False)
    # SOC actual-y data differs from base+Jp, and must appear in b exactly.
    soc_arrays, soc_selections = [], []
    for item in arrays:
        rows = item.rows.copy(); rows[:2, 2] = -.02
        soc_arrays.append(FullGridValues(item.grid, rows, item.eta, item.b, item.tolerances, item.mean_Xs))
    soc_selections = [SelectedRows(S, item, old.ids, old.J) for item, old in zip(soc_arrays, chosen)]
    pbase = build_primary(S, soc_arrays, soc_selections, state, lower, upper, cap, trust_exact='1/4000')
    p = S.lift_step(np.r_[.001, np.zeros(102)])
    trials = []
    for item in soc_arrays:
        rows = item.rows.copy(); rows[:2, 2] = -.01925
        trials.append(FullGridValues(item.grid, rows, item.eta, item.b, item.tolerances, item.mean_Xs))
    corr, cinfo = build_correction(pbase, trials, p)
    soft = pbase.active_groups < 2
    soc_actual = bool(corr is not None and np.array_equal(corr.b[:len(soft)][soft],
        corr.active_trial_values[soft]+cinfo['metric_slack_budget'])
        and corr.A.shape[1] == 206 and corr.information['no_cap_or_external_hard_restoration_row_added'])
    checks = {'layout_validation': all(layout_rejects.values()),
        'selected103_fixed60_and_Q153': len(S.columns) == 103 and len(S.fixed_columns) == 60 and S.columns[-1] == 153,
        'full_lift_and_fixed_coefficients_bitwise': bool(np.all(lifted[S.fixed_columns] == 0)
            and candidate[S.fixed_columns].tobytes() == state[S.fixed_columns].tobytes()),
        'exact_endpoint_classification': endpoint['variable'].tolist() == [False, False, True],
        'classification_not_a_small_J_test': class_independent,
        'outside_hard_floor_does_not_create_false_empty_LP': false_floor,
        'two_branch_all_grid_constant_soft_equivalence': equiv and soft_constant == .013,
        'internal_zero_J_rows_kept': hard_zero_kept and internal_not_deleted,
        'negative_constant_cap_passes_only_original_tolerance': cap.report()['original_tolerance_pass']
            and not cap.report()['strict_nonnegative_margins'] and all(gate_rejects),
        'all_fixed_parameters_original_box_still_required': fixed_box_reject,
        'same_center_radius_inclusion_and_same_physical_objective': containment,
        'initial_fixed_max_exits_before_LP': not lock_decision['may_call_LP'],
        'insufficient_drop_exits_unless_target_still_possible': not narrow_decision['may_call_LP'] and target_decision['may_call_LP'],
        'ordinary_initial_has_no_false_rejection': decision['may_call_LP'],
        'SOC_uses_actual_y_soft_rows_and_restricted_original_box': soc_actual,
        'SOC_budget_cannot_ignore_outside_constant': not constant_soft_budget_feasible(.02, .019),
        'no_geometry_loader_or_optimizer_called': True}
    checks = {key: bool(value) for key, value in checks.items()}
    return {'schema': SCHEMA+'-artificial-development', 'passed': all(checks.values()),
        'artificial_arrays_only': True, 'checks': checks, 'layout_rejections': layout_rejects,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'array_dimensions': {'primary': list(model.A.shape), 'SOC': list(corr.A.shape)},
        'full_report_or_real_candidate_not_read': True,
        'no_claim_of_real_descent_feasibility_or_continuous_certificate': True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only', action='store_true', required=True)
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    result = developer_check()
    text = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+'\n'
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True); args.out.write_text(text)
    print(text, end='')
    if not result['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
