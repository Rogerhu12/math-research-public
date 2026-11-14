"""Whole actual R153 field at common split-fine coast quadrature points.

This is a new finite cell rule. It replaces the old affine-G8/raw-plus-Delta
G2 mixture only on cells meeting the frozen coast support. All n/m endpoint
functions remain exact. Outside those cells the frozen R155 consumer is
used unchanged. The actual field, target, mesh and angular rows do not change.
"""
from __future__ import annotations

import copy
import numpy as np
from scipy import sparse

from fd2d_gc_archive_arrays import identity
from fd2d_gc_codazzi_complement import _high, _bound_model
from fd2d_gc_d2_complements import d2_high_rows
from fd2d_gc_gauss_cell_frozen_operator_compatible import gauss_cell_positive_trace_frozen_operator_compatible as _old_trace
from fd2d_gc_hybrid_lifting_codazzi_d2 import fixed_lifting_breaks, point_view, quadrature_on_parts
from fd2d_gc_positive_gauss_l import positive_gauss_l_delta, gauss_delta_direction, gauss_delta_state_columns


def _project(problem, rows, n, m, *, high_n=None, high_m=None):
    low = np.concatenate((problem.PE@n, problem.PO@m), axis=0)
    high_n = n if high_n is None else high_n
    high_m = m if high_m is None else high_m
    high = np.concatenate((rows.project(_high(high_n, problem.E, problem.PE), 'even'),
                           rows.project(_high(high_m, problem.O, problem.PO), 'odd')), axis=0)
    return low, high


def _actual_packet(view, correction, parameters, jacobian):
    ops = view.operators(parameters[view.profile_parameter_slice])
    jet = ops['jet']
    if not np.array_equal(np.asarray(jet['radial_scale']), np.ones(view.N)):
        raise ValueError('The grouped coast consumer uses physical s exactly')
    lift = view.lifting(parameters[view.profile_parameter_slice], parameters[view.tail_parameter_slice])
    raw = np.stack((view.E@correction[:, :view.e].T,
                    view.O@correction[:, view.e:view.d].T,
                    view.E@correction[:, view.d:].T), axis=-1)
    raw_xi = np.stack((view.Ex@correction[:, :view.e].T,
                       view.Ox@correction[:, view.e:view.d].T,
                       view.Ex@correction[:, view.d:].T), axis=-1)
    L, Lxi = np.asarray(lift['values']), np.asarray(lift['xi'])
    fields, angular = raw+L, raw_xi+Lxi
    window = view.window()
    D = positive_gauss_l_delta(fields, angular, jet['K'][None, :], window[None, :],
                               minimum_active_n=view.minimum_active_n)
    actual = fields.copy(); actual[:, :, 2] = D['actual_l']
    actual_xi = angular.copy(); actual_xi[:, :, 2] = D['actual_l_xi']
    inv, adv = np.asarray(ops['inv']), np.asarray(ops['adv'])
    c, pref = np.asarray(jet['c']), 1/np.asarray(jet['a'])
    rhs = np.stack((inv*actual_xi[:, :, 1]+c[None, :]*(actual[:, :, 2]-actual[:, :, 0])+adv*actual_xi[:, :, 0],
                    inv*actual_xi[:, :, 2]-2*c[None, :]*actual[:, :, 1]+adv*actual_xi[:, :, 1]), axis=-1)
    # Remove analytically retained raw terms before projecting the high
    # rows. This subtraction is a row-coordinate identity, not a model fit.
    retained_raw = np.stack((pref[None, :]*raw_xi[:, :, 1]
                            +c[None, :]*((1-window[None, :])*raw[:, :, 2]-raw[:, :, 0]),
                            pref[None, :]*(1-window[None, :])*raw_xi[:, :, 2]
                            -2*c[None, :]*raw[:, :, 1]), axis=-1)
    nonlow = rhs-retained_raw
    groups = ()
    if jacobian:
        _, _, _, groups = _bound_model(view, np.r_[correction.ravel(), parameters], {'lift': lift}, True)
    return dict(ops=ops, jet=jet, lift=lift, raw=raw, raw_xi=raw_xi,
        actual=actual, actual_xi=actual_xi, window=window, delta=D,
        rhs=rhs, nonlow=nonlow, groups=groups,
        gauss=actual[:, :, 0]*actual[:, :, 2]-actual[:, :, 1]**2-jet['K'][None, :])


def _point_parameter_rhs(view, packet, group):
    """Complete actual-field/metric columns at all current point nodes."""
    ops, jet, D = packet['ops'], packet['jet'], packet['delta']
    ids = group['indices']
    profile = bool(ids[0] >= view.profile_parameter_slice.start)
    kp = jet['K_parameters'][None, :, :] if profile else np.zeros((1, view.N, len(ids)))
    dv, dx = gauss_delta_direction(D, group['values'], group['xi'], kp)
    actual_p = np.array(group['values'], copy=True)
    angular_p = np.array(group['xi'], copy=True)
    actual_p[:, :, 2] += dv
    angular_p[:, :, 2] += dx
    inv, adv = np.asarray(ops['inv']), np.asarray(ops['adv'])
    a, c = np.asarray(jet['a']), np.asarray(jet['c'])
    ap, cp = group['a'], group['c']
    inv_p = -inv[:, :, None]*ap[None, :, :]/a[None, :, None]
    actual, angular = packet['actual'], packet['actual_xi']
    fn = (inv_p*angular[:, :, 1, None]+inv[:, :, None]*angular_p[:, :, 1]
          +cp[None, :, :]*(actual[:, :, 2]-actual[:, :, 0])[:, :, None]
          +c[None, :, None]*(actual_p[:, :, 2]-actual_p[:, :, 0])
          +adv[:, :, None]*angular_p[:, :, 0])
    fm = (inv_p*angular[:, :, 2, None]+inv[:, :, None]*angular_p[:, :, 2]
          -2*cp[None, :, :]*actual[:, :, 1, None]-2*c[None, :, None]*actual_p[:, :, 1]
          +adv[:, :, None]*angular_p[:, :, 1])
    pref_p = -ap/a[:, None]**2
    raw, raw_xi, window = packet['raw'], packet['raw_xi'], packet['window']
    low_n = (pref_p[None, :, :]*raw_xi[:, :, 1, None]
             +cp[None, :, :]*((1-window[None, :])*raw[:, :, 2]-raw[:, :, 0])[:, :, None])
    low_m = (pref_p[None, :, :]*(1-window[None, :, None])*raw_xi[:, :, 2, None]
             -2*cp[None, :, :]*raw[:, :, 1, None])
    return ids, fn, fm, fn-low_n, fm-low_m


def _coast_block(problem, vector, *, high_weight, jacobian, fine_order, point_batch):
    """Every cell in this input block meets the declared coast interval."""
    y, p = problem.unpack(np.asarray(vector, float))
    background = problem.coast_background_view()
    rows = d2_high_rows(problem)
    cells, W, q, pc = problem.N-1, problem.work, problem.q, problem.parameter_count
    if float(problem.x[-1]) >= problem.trace_start:
        raise ValueError('The R153 and R155 windows must remain disjoint')
    knots, definitions = fixed_lifting_breaks(problem)
    # Use the actual saved plateau endpoints as well, rather than trusting
    # two algebraically equivalent floating constructions to share a bit.
    extra = np.asarray(problem.gauss_l_definition['gauss_plateau'], float)
    knots = np.array(sorted(set(knots.tolist()+extra.tolist())))
    endpoint = background.lifting(p[background.profile_parameter_slice], p[background.tail_parameter_slice])
    endpoint_values = np.array(endpoint['values'][:, :, :2], copy=True)
    endpoint_groups = []
    if jacobian:
        for section, key in ((problem.tail_parameter_slice, 'parameters'),
                             (problem.profile_parameter_slice, 'profile_parameters')):
            endpoint_groups.append((np.arange(section.start, section.stop),
                                     np.array(endpoint[key][:, :, :2], copy=True)))
    del endpoint
    full = np.empty((W, cells, 2)); omitted = np.empty_like(full)
    retained = np.empty((cells, problem.d))
    old_g2_gauss = np.empty((W, 2*cells)); old_g2_points = np.empty(2*cells)
    fine_observations = []
    low_parts = [[], [], []]; high_parts = [[], [], []]
    def add(parts, offset, columns, values):
        values = np.asarray(values, float)
        ii, jj = np.nonzero(values)
        if len(ii):
            parts[0].append(offset+ii); parts[1].append(np.asarray(columns)[jj]); parts[2].append(values[ii, jj])
    if jacobian:
        zn = np.zeros((W, q)); zm = zn.copy(); zl = zn.copy()
        zxn = zn.copy(); zxm = zn.copy(); zxl = zn.copy()
        zn[:, :problem.e] = problem.E
        zm[:, problem.e:problem.d] = problem.O
        zl[:, problem.d:] = problem.E
        zxn[:, :problem.e] = problem.Ex
        zxm[:, problem.e:problem.d] = problem.Ox
        zxl[:, problem.d:] = problem.Ex
    for cell in range(cells):
        left, right = map(float, problem.x[cell:cell+2]); h = right-left
        cuts = [left]+knots[(knots > left)&(knots < right)].tolist()+[right]
        xx, weights, panels = quadrature_on_parts(left, right, cuts, fine_order)
        avg = np.zeros((W, 2)); high_avg = np.zeros_like(avg)
        if jacobian:
            jl = -problem.select/h; jr = problem.select/h
            hl = np.zeros((rows.cell_rows, q)); hr = hl.copy()
            jp = np.zeros((problem.d, pc)); hp = np.zeros((rows.cell_rows, pc))
            for ids, values in endpoint_groups:
                v = (values[:, cell+1]-values[:, cell])/h
                a, b = _project(problem, rows, v[:, 0], v[:, 1])
                jp[:, ids] += a; hp[:, ids] += b
        fine_gauss_maximum = 0.; minimum_active_n = np.inf
        fine_location = None
        for start in range(0, len(xx), point_batch):
            sample = xx[start:start+point_batch]
            weight = weights[start:start+point_batch]
            tau = (sample-left)/h
            view = point_view(background, sample)
            yy = (1-tau[:, None])*y[cell]+tau[:, None]*y[cell+1]
            packet = _actual_packet(view, yy, p, jacobian)
            avg += np.einsum('wne,n->we', packet['rhs'], weight)
            high_avg += np.einsum('wne,n->we', packet['nonlow'], weight)
            where = np.unravel_index(int(np.argmax(abs(packet['gauss']))), packet['gauss'].shape)
            g = float(packet['gauss'][where])
            if fine_location is None or abs(g) > fine_gauss_maximum:
                fine_gauss_maximum = abs(g)
                fine_location = dict(angular_index=int(where[0]), xi=float(problem.chart.theta[where[0]]),
                                     s=float(sample[where[1]]), signed_value=g)
            nmin = packet['delta']['sampled_minimum_active_n']
            if nmin is not None:
                minimum_active_n = min(minimum_active_n, nmin)
            if jacobian:
                parameter_rhs = [_point_parameter_rhs(view, packet, group) for group in packet['groups']]
                for j, (t, w) in enumerate(zip(tau, weight)):
                    dv, dx = gauss_delta_state_columns(view, packet['delta'], j)
                    actual_l, actual_lxi = zl+dv, zxl+dx
                    inv = packet['ops']['inv'][:, j, None]
                    adv = packet['ops']['adv'][:, j, None]
                    c = packet['jet']['c'][j]; pref = 1/packet['jet']['a'][j]
                    win = packet['window'][j]
                    sn = inv*zxm+c*(actual_l-zn)+adv*zxn
                    sm = inv*actual_lxi-2*c*zm+adv*zxm
                    nonlow_n = sn-(pref*zxm+c*((1-win)*zl-zn))
                    nonlow_m = sm-(pref*(1-win)*zxl-2*c*zm)
                    a, b = _project(problem, rows, sn, sm, high_n=nonlow_n, high_m=nonlow_m)
                    jl -= w*(1-t)*a; jr -= w*t*a
                    hl -= w*(1-t)*b; hr -= w*t*b
                    for ids, fn, fm, hn, hm in parameter_rhs:
                        a, b = _project(problem, rows, fn[:, j], fm[:, j], high_n=hn[:, j], high_m=hm[:, j])
                        jp[:, ids] -= w*a; hp[:, ids] -= w*b
                del parameter_rhs
            del packet, view
        end = (endpoint_values[:, cell+1]-endpoint_values[:, cell])/h
        raw_end = (y[cell+1, :problem.d]-y[cell, :problem.d])/h
        full[:, cell] = np.stack((problem.E@raw_end[:problem.e], problem.O@raw_end[problem.e:]), axis=-1)+end-avg
        retained[cell] = raw_end+np.r_[problem.PE@(end[:, 0]-avg[:, 0]), problem.PO@(end[:, 1]-avg[:, 1])]
        omitted[:, cell, 0] = _high(end[:, 0]-high_avg[:, 0], problem.E, problem.PE)
        omitted[:, cell, 1] = _high(end[:, 1]-high_avg[:, 1], problem.O, problem.PO)
        if jacobian:
            for node, a, b in ((cell, jl, hl), (cell+1, jr, hr)):
                cols = node*q+np.arange(q)
                add(low_parts, cell*problem.d, cols, a)
                add(high_parts, cell*rows.cell_rows, cols, high_weight*b)
            cols = problem.N*q+np.arange(pc)
            add(low_parts, cell*problem.d, cols, jp)
            add(high_parts, cell*rows.cell_rows, cols, high_weight*hp)
        # Keep the legacy diagnostic grid/shape explicit. Fine-point
        # Gauss values are separately named observations, never relabelled G2.
        gx, gw, _ = quadrature_on_parts(left, right, [left, right], 2)
        gv = point_view(background, gx); gt = (gx-left)/h
        gy = (1-gt[:, None])*y[cell]+gt[:, None]*y[cell+1]
        gd = _actual_packet(gv, gy, p, False)
        old_g2_gauss[:, 2*cell:2*cell+2] = gd['gauss']
        old_g2_points[2*cell:2*cell+2] = gx
        del gd, gv
        fine_observations.append(dict(local_cell=cell, endpoints=[left, right], cuts=cuts,
            points=xx.tolist(), average_weights=weights.tolist(), panels=panels,
            fine_sampled_Gauss_maximum=fine_gauss_maximum, fine_Gauss_location=fine_location,
            fine_sampled_minimum_active_n=None if np.isinf(minimum_active_n) else float(minimum_active_n)))
    def matrix(parts, count):
        if not parts[2]:
            return sparse.csc_matrix((count, problem.size))
        out = sparse.coo_matrix((np.concatenate(parts[2]), (np.concatenate(parts[0]), np.concatenate(parts[1]))),
                               shape=(count, problem.size)).tocsc()
        out.eliminate_zeros(); return out
    high = high_weight*np.concatenate((rows.project(omitted[:, :, 0], 'even'),
                                      rows.project(omitted[:, :, 1], 'odd')), axis=0).T.ravel()
    info = dict(schema='fd2d-whole-actual-R153-split-fine-coast-cell-v1',
        source_sha256=identity(__file__)['sha256'], order=2, diagnostic_Gauss_order=2,
        selected_coast_local_cells=list(range(cells)), grouped_coast_local_cells=list(range(cells)),
        grouped_actual_field_order=int(fine_order),
        finite_equations_changed=True, actual_field_changed=False, physical_g_changed=False,
        unknown_mesh_changed=False, full_actual_field_integrated_at_common_points=True,
        exact_endpoint_lifting_difference_preserved=True, only_nonlinear_delta_refined=False,
        full_nonlinear_state_and_parameter_columns=True, parameter_fixed_quadrature=True,
        formula='complete n/m endpoint difference minus split-fine average of the whole actual R153 physical PDE',
        point_gauss_scope='Original Gauss2 diagnostic points only; same shape and ordering as legacy chunk consumers',
        fine_Gauss_scope='Separate finite observations in grouped_coast_rules; not included in point_gauss or sampled_interior_Gauss_maximum',
        grouped_coast_rules=fine_observations, declared_common_piece_boundaries=definitions,
        additional_saved_plateau_endpoints=extra.tolist(),
        retained_cell_maximum=float(np.max(abs(retained), initial=0.)),
        sampled_full_average_codazzi_maximum=float(np.max(abs(full), initial=0.)),
        sampled_omitted_average_codazzi_maximum=float(np.max(abs(omitted), initial=0.)),
        sampled_interior_Gauss_maximum=float(np.max(abs(old_g2_gauss), initial=0.)),
        fine_sampled_interior_Gauss_maximum=max(o['fine_sampled_Gauss_maximum'] for o in fine_observations),
        row_definition=rows.definition(), known_affine_lifting_separately_reintegrated=False,
        known_lifting_change_maximum_not_separately_evaluated=True,
        continuous_certificate=False, finite_fine_rule_is_not_an_exact_integral=True)
    out = dict(retained_residual=retained.ravel(), high_residual=high,
        retained_cells=retained, omitted_codazzi_cells=omitted, full_codazzi_cells=full,
        point_gauss=old_g2_gauss, quadrature_points=old_g2_points, info=info,
        retained_jacobian=None, high_jacobian=None)
    if jacobian:
        out['retained_jacobian'] = matrix(low_parts, cells*problem.d)
        out['high_jacobian'] = matrix(high_parts, cells*rows.cell_rows)
        info['retained_jacobian_nonzeros'] = out['retained_jacobian'].nnz
        info['high_jacobian_nonzeros'] = out['high_jacobian'].nnz
    return out


def _block_view(problem, start, stop):
    view = copy.copy(problem)
    view.x = np.array(problem.x[start:stop+1], copy=True)
    view.N = len(view.x); view.h = np.diff(view.x)
    view.size = view.N*view.q+view.parameter_count
    view.residual_size = view.N*view.q+2*view.K+2
    view.coords = {k: np.asarray(v, float) for k, v in view.chart.coordinates(view.x).items()}
    view._operator_cache = {}; view._cell_gauss_view_cache = None
    view._chunked_gauss_codazzi_views = None; view._positive_known_coast_view = None
    return view


def gauss_cell_positive_trace_grouped_coast(problem, vector, *, order=2, high_weight=1.,
                                           jacobian=True, fine_order=8, point_batch=2):
    """Drop-in cell consumer, including unchanged outside-coast R155 terms."""
    if order != 2 or int(fine_order) != fine_order or not 2 <= fine_order <= 16:
        raise ValueError('Keep legacy G2 diagnostics and choose a declared fine order from 2 to 16')
    if not np.isfinite(high_weight) or high_weight < 0 or int(point_batch) != point_batch or not 1 <= int(point_batch) <= 8:
        raise ValueError('Use a finite nonnegative high weight and a small point batch')
    if problem.profile_kind != 'physical_bumps':
        raise ValueError('The actual independent-tail physical-bump representation is required')
    z = np.asarray(vector, float)
    if z.shape != (problem.size,) or not np.all(np.isfinite(z)):
        raise ValueError('Wrong actual defining vector')
    e, f = problem.gauss_l_definition['support']
    selected = (problem.x[:-1] < f)&(problem.x[1:] > e)
    if not np.any(selected):
        answer = _old_trace(problem, z, order=2, high_weight=high_weight, jacobian=jacobian)
        info = dict(answer['info']); info.update(grouped_coast_local_cells=[],
            grouped_coast_consumer_source_sha256=identity(__file__)['sha256'],
            grouped_coast_applied=False, all_rows_from_frozen_outside_coast_consumer=True)
        answer['info'] = info
        return answer
    if np.all(selected):
        return _coast_block(problem, z, high_weight=high_weight, jacobian=jacobian,
                            fine_order=int(fine_order), point_batch=int(point_batch))
    y, p = problem.unpack(z)
    cut = np.r_[0, np.flatnonzero(selected[1:] != selected[:-1])+1, problem.N-1]
    collected = {k: [] for k in ('retained_residual', 'high_residual', 'retained_cells',
        'omitted_codazzi_cells', 'full_codazzi_cells', 'point_gauss', 'quadrature_points')}
    matrices = {k: [] for k in ('retained_jacobian', 'high_jacobian')}
    infos = []; fine_rules = []
    for start, stop in zip(cut[:-1], cut[1:]):
        view = _block_view(problem, int(start), int(stop))
        local = np.r_[y[start:stop+1].ravel(), p]
        if selected[start]:
            result = _coast_block(view, local, high_weight=high_weight, jacobian=jacobian,
                                  fine_order=int(fine_order), point_batch=int(point_batch))
            fine_rules.extend(dict(row, local_cell=row['local_cell']+int(start)) for row in result['info']['grouped_coast_rules'])
        else:
            result = _old_trace(view, local, order=2, high_weight=high_weight, jacobian=jacobian)
        for key in collected:
            collected[key].append(result[key])
        infos.append(result['info'])
        if jacobian:
            for key in matrices:
                coo = result[key].tocoo(copy=False); poffset = view.N*view.q
                columns = np.where(coo.col < poffset, coo.col+int(start)*problem.q,
                                   coo.col-poffset+problem.N*problem.q)
                matrices[key].append(sparse.coo_matrix((coo.data, (coo.row, columns)),
                    shape=(coo.shape[0], problem.size)).tocsc())
    answer = {key: np.concatenate(values, axis=1 if key in
        ('omitted_codazzi_cells', 'full_codazzi_cells', 'point_gauss') else 0)
        for key, values in collected.items()}
    info = dict(schema='fd2d-R153-grouped-fine-coast-and-frozen-R155-outside-v1',
        source_sha256=identity(__file__)['sha256'], order=2,
        grouped_coast_local_cells=np.flatnonzero(selected).tolist(), grouped_coast_rules=fine_rules,
        grouped_actual_field_order=int(fine_order), outside_coast_formula_unchanged=True,
        actual_field_changed=False, physical_g_changed=False, unknown_mesh_changed=False,
        finite_equations_changed=True, complete_state_and_parameter_jacobian=True,
        point_gauss_scope='Original G2 points only, including in grouped coast cells',
        fine_sampled_interior_Gauss_maximum=max(q['fine_sampled_Gauss_maximum'] for q in fine_rules),
        all_subblock_info=infos, continuous_certificate=False)
    for key in ('retained_cell_maximum', 'sampled_full_average_codazzi_maximum',
                'sampled_omitted_average_codazzi_maximum', 'sampled_interior_Gauss_maximum'):
        info[key] = max(row[key] for row in infos)
    answer['retained_jacobian'] = None; answer['high_jacobian'] = None
    if jacobian:
        for key in matrices:
            answer[key] = sparse.vstack(matrices[key], format='csc'); answer[key].eliminate_zeros()
        info['retained_jacobian_nonzeros'] = answer['retained_jacobian'].nnz
        info['high_jacobian_nonzeros'] = answer['high_jacobian'].nnz
    answer['info'] = info
    return answer
