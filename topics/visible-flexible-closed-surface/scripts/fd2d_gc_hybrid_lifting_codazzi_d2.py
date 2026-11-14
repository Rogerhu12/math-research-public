"""R152: Gauss2 correction with separately integrated known lifting.

The mathematical field, target and angular atlas stay fixed. This is a new
finite quadrature rule. State columns are copied from the frozen endpoint
Gauss2 consumer; only known-lifting residuals and parameter columns change.
No high-order zero-field state Jacobian is constructed or added.
"""
from __future__ import annotations
import copy
import numpy as np
from scipy import sparse
from fd2d_gc_codazzi_complement import _high, _bound_model
from fd2d_gc_d2_complements import d2_high_rows
from fd2d_gc_gauss_cell_codazzi_endpoint_d2 import gauss_cell_codazzi_endpoint_d2


def fixed_lifting_breaks(problem):
    """All declared common radial piece boundaries; none depends on p.

    The tail entries below are its radial lifting window. Angle-dependent
    kappa(a(s) sin U) clamps remain the original smooth piecewise function;
    they are not falsely represented as common parameter-frozen s knots.
    """
    if problem.profile_kind != 'physical_bumps':
        raise ValueError('Use the explicit fixed-physical-s profile')
    rows = []
    def add(values, kind):
        for value in np.asarray(values, float).ravel():
            if not np.isfinite(value):
                raise ValueError('Nonfinite declared lifting boundary')
            rows.append((float(value), kind))
    add(problem.profile.breaks, 'physical_profile_or_bump_support')
    for piece in problem.profile.segments:
        if piece['kind'] == 'turn':
            add([piece['s0']+.08*piece['L'], piece['s0']+.92*piece['L']], 'physical_turn_internal_piece')
    seed = problem.seed_weight_definition
    if seed.get('step') != 5:
        raise ValueError('Only the explicitly declared quintic seed weight is supported')
    add([seed['start'], seed['end']], 'actual_seed_weight')
    # The legacy seed was algebraically replaced, but its evaluation still
    # appears in the frozen implementation, so retain its boundaries too.
    legacy = getattr(problem, 'legacy_seed_weight_definition', None)
    if legacy is not None:
        add([legacy['start'], legacy['end']], 'legacy_seed_algebraic_cancellation')
    add([.42*problem.profile.end, problem.profile.end], 'tail_radial_lifting_weight')
    ref = problem.coast_reference
    e, length, rim = float(ref.entry_s), float(ref.length), float(problem.reference_rim_fraction)
    add([e, e+length*rim, e+length*(1-rim), e+length], 'frozen_reference_window')
    atlas = problem.chart.chart_definition()
    if atlas.get('parameters_frozen') is not True:
        raise ValueError('The known-lifting quadrature requires the explicit parameter-frozen atlas')
    if atlas.get('schema') != 'fd2d-global-positive-frozen-ruling-atlas-v1':
        raise ValueError('This consumer binds the R149 global frozen ruling atlas')
    for key in ('entry_transition', 'coast', 'exit_transition'):
        add(atlas[key], 'atlas_'+key)
    add(atlas['original_chart']['blend_interval'], 'original_chart_blend')
    rows.sort()
    knots = np.array(sorted(set(value for value, _ in rows)), float)
    definitions = [dict(s=float(value), kinds=sorted(set(kind for v, kind in rows if v == value)))
                   for value in knots]
    return knots, definitions


def point_view(problem, points):
    """Small evaluation-only view, sharing frozen functions but no op cache."""
    view = copy.copy(problem)
    view.x = np.asarray(points, float).copy()
    view.N = len(view.x); view.h = np.diff(view.x)
    view.size = view.N*view.q+view.parameter_count
    view.residual_size = view.N*view.q+2*view.K+2
    view.coords = {k: np.asarray(v, float) for k, v in view.chart.coordinates(view.x).items()}
    view.profile = copy.copy(problem.profile)
    view.profile.coefficients = np.array(problem.profile.coefficients, copy=True)
    view.profile._cache = {}
    view._operator_cache = {}
    view._cell_gauss_view_cache = None
    view._chunked_gauss_codazzi_views = None
    view._hybrid_known_lifting_cache = None
    return view


def quadrature_on_parts(left, right, cuts, order):
    roots, ww = np.polynomial.legendre.leggauss(int(order))
    points, weights, panels = [], [], []
    for a, b in zip(cuts[:-1], cuts[1:]):
        if not left <= a < b <= right:
            raise ValueError('Invalid strictly positive quadrature subpanel')
        xx = a+(b-a)*((roots+1)/2)
        local_weights = ww/2
        fallback = None
        if not (np.all((xx > a)&(xx < b)) and np.all(np.diff(xx)>0)):
            # Keep the full weight of a genuine tiny physical subpanel.
            # A coalesced computational knot can be a few ulps away from a
            # physical piece boundary. No interval is silently discarded.
            middle = float((np.longdouble(a)+np.longdouble(b))/2)
            if not a < middle < b:
                following = np.nextafter(a, b)
                middle = float(following if following < b else a)
            xx, local_weights = np.array([middle]), np.array([1.])
            fallback = 'Explicit midpoint (or left endpoint if no binary interior exists); complete positive panel weight retained'
        points.extend(xx.tolist())
        weights.extend(((b-a)/(right-left)*local_weights).tolist())
        panels.append(dict(endpoints=[float(a),float(b)], requested_order=int(order),
            actual_point_count=len(xx), narrow_panel_fallback=fallback))
    return np.asarray(points, float), np.asarray(weights, float), panels


def known_pde_average(problem, parameters, points, weights, *, jacobian, point_batch=8):
    """Q(F_p L_p), with only actual lifting/profile parameter derivatives."""
    p = np.asarray(parameters, float)
    out = np.zeros((problem.work, 2))
    partial = np.zeros((problem.work, 2, problem.parameter_count)) if jacobian else None
    for start in range(0, len(points), point_batch):
        stop = min(start+point_batch, len(points))
        view = point_view(problem, points[start:stop])
        delta, tail = p[view.profile_parameter_slice], p[view.tail_parameter_slice]
        ops = view.operators(delta)
        lift = view.lifting(delta, tail)
        zero_vector = np.r_[np.zeros(view.N*view.q), p]
        _, _, ops, groups = _bound_model(view, zero_vector, {'lift': lift}, jacobian)
        jet = ops['jet']
        if not np.array_equal(np.asarray(jet['radial_scale'], float), np.ones(view.N)):
            raise ValueError('The actual s coordinate must have scale exactly one')
        L, Lxi = np.asarray(lift['values'], float), np.asarray(lift['xi'], float)
        a, c = np.asarray(jet['a'], float), np.asarray(jet['c'], float)
        inv, adv = np.asarray(ops['inv'], float), np.asarray(ops['adv'], float)
        omega = np.asarray(view.coords['u_xi'], float)
        fn = inv*Lxi[:, :, 1]+c[None, :]*(L[:, :, 2]-L[:, :, 0])+adv*Lxi[:, :, 0]
        fm = inv*Lxi[:, :, 2]-2*c[None, :]*L[:, :, 1]+adv*Lxi[:, :, 1]
        w = weights[start:stop]
        out[:, 0] += fn@w; out[:, 1] += fm@w
        for group in groups:
            ids = group['indices']
            lp, lxp = group['values'], group['xi']
            ap, cp = group['a'], group['c']
            inv_p = -ap[None, :, :]/(a[None, :, None]**2*omega[:, :, None])
            fnp = (inv_p*Lxi[:, :, 1, None]+inv[:, :, None]*lxp[:, :, 1]
                +cp[None, :, :]*(L[:, :, 2]-L[:, :, 0])[:, :, None]
                +c[None, :, None]*(lp[:, :, 2]-lp[:, :, 0])
                +adv[:, :, None]*lxp[:, :, 0])
            fmp = (inv_p*Lxi[:, :, 2, None]+inv[:, :, None]*lxp[:, :, 2]
                -2*cp[None, :, :]*L[:, :, 1, None]-2*c[None, :, None]*lp[:, :, 1]
                +adv[:, :, None]*lxp[:, :, 1])
            # Use explicit column assignment to avoid NumPy advanced-index
            # axis reordering on the W x equation x parameter array.
            partial[:, 0, ids] += np.einsum('wnp,n->wp', fnp, w)
            partial[:, 1, ids] += np.einsum('wnp,n->wp', fmp, w)
        del view, lift, ops, groups
    if not np.all(np.isfinite(out)) or (partial is not None and not np.all(np.isfinite(partial))):
        raise FloatingPointError('Nonfinite known-lifting PDE average or parameter derivative')
    return out, partial


def known_lifting_correction(problem, parameters, *, known_order=8, jacobian=True, point_batch=8):
    """The state-independent Q2(F L)-Qfine(F L) for every current cell."""
    if int(known_order) != known_order or not 2 <= int(known_order) <= 16:
        raise ValueError('Use a declared known-lifting Gauss order between 2 and 16')
    if int(point_batch) != point_batch or point_batch < 1:
        raise ValueError('Use a positive bounded point batch')
    known_order, point_batch = int(known_order), int(point_batch)
    p = np.asarray(parameters, float)
    knots, definitions = fixed_lifting_breaks(problem)
    key = (known_order, point_batch, p.tobytes(), np.asarray(problem.x, float).tobytes(), knots.tobytes())
    cache = getattr(problem, '_hybrid_known_lifting_cache', None)
    if cache is not None and cache[0] == key and (not jacobian or cache[1]['partial'] is not None):
        return cache[1]
    cells = problem.N-1
    change = np.zeros((problem.work, cells, 2))
    partial = np.zeros((problem.work, cells, 2, problem.parameter_count)) if jacobian else None
    cell_rows = []
    for j, (left, right) in enumerate(zip(problem.x[:-1], problem.x[1:])):
        cuts = np.r_[left, knots[(knots > left)&(knots < right)], right]
        coarse_x, coarse_w, coarse_panels = quadrature_on_parts(left, right, [left, right], 2)
        if any(row['narrow_panel_fallback'] is not None for row in coarse_panels):
            raise ValueError('The original correction cell cannot represent its unchanged Gauss2 rule')
        fine_x, fine_w, panels = quadrature_on_parts(left, right, cuts, known_order)
        coarse, cp = known_pde_average(problem, p, coarse_x, coarse_w,
            jacobian=jacobian, point_batch=point_batch)
        fine, fp = known_pde_average(problem, p, fine_x, fine_w,
            jacobian=jacobian, point_batch=point_batch)
        change[:, j] = coarse-fine
        if jacobian:
            partial[:, j] = cp-fp
        cell_rows.append(dict(local_cell=j, endpoints=[float(left), float(right)],
            split_knots=cuts.tolist(), fine_point_count=len(fine_x),
            fine_points=fine_x.tolist(), fine_average_weights=fine_w.tolist(),
            normalized_weight_sum=float(fine_w.sum()), panels=panels))
    result = dict(change=change, partial=partial, cells=cell_rows, fixed_boundaries=definitions,
        known_order=known_order, point_batch=point_batch)
    problem._hybrid_known_lifting_cache = (key, result)
    return result


def gauss_cell_codazzi_hybrid_d2(problem, vector, *, order=2, high_weight=1.,
                                 jacobian=True, known_order=8, point_batch=8):
    """Chunk-compatible R152 residual with precisely the original state J.

    `order` is the correction rule and must remain 2. `known_order` controls
    the independently split known lifting. All original unknown columns and
    original node Gauss/boundary equations stay the caller's responsibility.
    """
    if order != 2:
        raise ValueError('The R152 hybrid keeps correction Gauss2 explicitly')
    if (type(problem).__module__ != 'fd2d_gc_raw_bump_ruling_atlas'
            or type(problem).__name__ != 'RulingAtlasRawBumpDAE'):
        raise ValueError('This closed consumer binds the affine R149 background; nonlinear field corrections require their own consistent composition')
    base = gauss_cell_codazzi_endpoint_d2(problem, vector, order=2,
        high_weight=high_weight, jacobian=jacobian)
    _, p = problem.unpack(np.asarray(vector, float))
    known = known_lifting_correction(problem, p, known_order=known_order,
        jacobian=jacobian, point_batch=point_batch)
    change = known['change']
    compression = d2_high_rows(problem)
    low = np.concatenate((problem.PE@change[:, :, 0], problem.PO@change[:, :, 1]), axis=0).T
    high = np.stack((_high(change[:, :, 0], problem.E, problem.PE),
                     _high(change[:, :, 1], problem.O, problem.PO)), axis=-1)
    result = dict(base)
    result['retained_cells'] = base['retained_cells']+low
    result['retained_residual'] = result['retained_cells'].ravel()
    result['full_codazzi_cells'] = base['full_codazzi_cells']+change
    result['omitted_codazzi_cells'] = base['omitted_codazzi_cells']+high
    high_delta = high_weight*np.concatenate((compression.project(high[:, :, 0], 'even'),
        compression.project(high[:, :, 1], 'odd')), axis=0).T.ravel()
    result['high_residual'] = base['high_residual']+high_delta
    if jacobian:
        cells, pc = problem.N-1, problem.parameter_count
        lowp = np.zeros((cells, problem.d, pc))
        highp = np.zeros((cells, compression.cell_rows, pc))
        for j in range(cells):
            dp = known['partial'][:, j]
            lowp[j] = np.concatenate((problem.PE@dp[:, 0], problem.PO@dp[:, 1]), axis=0)
            highp[j] = high_weight*np.concatenate((
                compression.project(_high(dp[:, 0], problem.E, problem.PE), 'even'),
                compression.project(_high(dp[:, 1], problem.O, problem.PO), 'odd')), axis=0)
        offset = problem.N*problem.q
        for name, addition in (('retained_jacobian', lowp), ('high_jacobian', highp)):
            old = base[name]
            # Copy every original state column unchanged. Only the shared
            # parameter block is added; J_fine(0)'s state columns do not exist.
            result[name] = sparse.hstack((old[:, :offset],
                old[:, offset:]+sparse.csc_matrix(addition.reshape(-1, pc))), format='csc')
            result[name].eliminate_zeros()
    info = dict(base['info'])
    info.update(schema='fd2d-R152-G2-correction-split-known-lifting-D2-v1',
        hybrid_definition='R_G2(y,p)+R_fine(0,p)-R_G2(0,p)',
        added_full_function='Q2(F_p L_p)-Qfine(F_p L_p); endpoint terms cancel exactly',
        correction_quadrature_order=2, known_lifting_quadrature_order=int(known_order),
        known_lifting_fixed_boundaries=known['fixed_boundaries'],
        known_lifting_cell_rules=known['cells'], maximum_evaluation_point_batch=int(point_batch),
        state_jacobian='Exactly the frozen endpoint Gauss2 state columns',
        parameter_jacobian='Original G2 columns plus derivative of the known-lifting average difference',
        zero_field_state_jacobian_constructed=False, zero_field_state_columns_added=False,
        source_field_or_metric_changed=False, finite_quadrature_equations_changed=True,
        field_scope='Original affine R149 P1 correction plus known lifting only; not a nonlinear Gauss-l window field',
        retained_cell_maximum=float(np.max(abs(result['retained_cells']), initial=0.)),
        sampled_full_average_codazzi_maximum=float(np.max(abs(result['full_codazzi_cells']), initial=0.)),
        sampled_omitted_average_codazzi_maximum=float(np.max(abs(result['omitted_codazzi_cells']), initial=0.)),
        known_lifting_full_change_maximum=float(np.max(abs(change), initial=0.)),
        point_gauss_scope='The original actual-field Gauss2 points only; known fine points do not replace this diagnostic',
        angular_tail_clamps='Original full functions at each fixed quadrature point, with complete parameter chain rule; not common radial knots',
        finite_symmetry_and_compression={key: compression.diagnostics(result['omitted_codazzi_cells'][:, :, j], parity)
            for j, (key, parity) in enumerate((('n', 'even'), ('m', 'odd')))},
        scope='New finite hybrid quadrature only; no continuous remainder or geometry certificate')
    if jacobian:
        info['retained_jacobian_nonzeros'] = int(result['retained_jacobian'].nnz)
        info['high_jacobian_nonzeros'] = int(result['high_jacobian'].nnz)
    result['info'] = info
    return result
