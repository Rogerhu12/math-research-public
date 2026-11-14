"""R163 same-schema P1 refinement at explicit saved physical points.

All old knots remain byte-identical. Requested binary64 physical points
are either inserted exactly, already present exactly, or explicitly
reported as blocked. No point is snapped, no old knot/window is moved,
and no near-zero child is manufactured to hide a one-ulp discrepancy.

The existing R163 v3 constructor/checkpoint chain still rebuilds every
mesh-dependent support/gauge/index and preserves the original full field
schema. The only new operation is the finite P1 interpolation partition.
Real-arithmetic invariance and honest saved-binary64 rounding have the
same meaning as R163; no new physical g or nonlinear solve is supplied.
"""
from __future__ import annotations
import copy
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_midpoint_refined_positive_trace_v3 import (
    SCHEMA, create_midpoint_refined_problem,
    checkpoint_arrays as _checkpoint_arrays, same_bits, decoded)


class UnsafePointInsertion(ValueError):
    def __init__(self, definition):
        self.definition = definition
        super().__init__('Requested physical points were not all inserted exactly; inspect blocked_point_rows. No snapping or window change was performed.')


def _fraction(value):
    return F.from_float(float(value))


def saved_gauss_plateau_points(saved_field):
    saved = load_npz(saved_field) if isinstance(saved_field, (str, Path)) else saved_field
    # These two original binary64 values are copied, not recomputed from
    # entry/length or formatted decimal coordinates.
    values = decoded(saved['gauss_l_definition'])['gauss_plateau']
    if len(values) != 2:
        raise ValueError('The saved Gauss plateau must have two endpoints')
    return tuple(float(value) for value in values)


def refine_at_physical_points(mesh, corrections, *, physical_points=(), midpoint_cells=(),
                             minimum_ulps=16, minimum_child_fraction=1e-12):
    """Return exact-request mesh, rounded P1 coefficients, and a full audit.

    This pure function may return an explicitly partial insertion when a
    request is blocked. The problem factory below refuses that partial
    result and exposes this audit in UnsafePointInsertion.definition.
    """
    x, y = np.asarray(mesh), np.asarray(corrections)
    if (x.dtype != np.float64 or y.dtype != np.float64 or x.ndim != 1
            or y.ndim != 2 or len(y) != len(x) or len(x) < 2
            or np.any(np.diff(x) <= 0) or not np.all(np.isfinite(x))
            or not np.all(np.isfinite(y))):
        raise ValueError('Expected the actual finite binary64 P1 mesh and coefficient array')
    if int(minimum_ulps) != minimum_ulps or minimum_ulps < 1:
        raise ValueError('Use a positive integer ulp separation for new child cells')
    if not np.isfinite(minimum_child_fraction) or not 0 <= minimum_child_fraction < .5:
        raise ValueError('The declared numerical child-width fraction must lie in [0,.5)')
    physical_points, midpoint_cells = tuple(physical_points), tuple(midpoint_cells)
    if any(int(j) != j for j in midpoint_cells):
        raise ValueError('Midpoint cell indices must be integers, not rounded numbers')
    cells = sorted(set(int(j) for j in midpoint_cells))
    if any(j < 0 or j >= len(x)-1 for j in cells):
        raise ValueError('Midpoint cells refer to the unchanged input mesh')
    proposals = []
    for number, value in enumerate(physical_points):
        point = float(value)
        if not np.isfinite(point):
            raise ValueError('Explicit physical points must be finite binary64 values')
        if isinstance(value, F) and F(point) != value:
            raise ValueError('A symbolic non-binary coordinate may not be silently rounded into an exact-point request')
        proposals.append(dict(kind='explicit_binary64_point', request_index=number,
                              point=point, exact_requested_coordinate=str(_fraction(point))))
    for j in cells:
        point = float(x[j]+.5*(x[j+1]-x[j]))
        exact_midpoint = (_fraction(x[j])+_fraction(x[j+1]))/2
        proposals.append(dict(kind='requested_cell_midpoint', request_cell=j, point=point,
            exact_requested_coordinate=str(exact_midpoint),
            exact_midpoint_coordinate_error=str(abs(_fraction(point)-exact_midpoint))))
    accepted_points = []
    request_rows, blocked = [], []
    for original in proposals:
        row = dict(original); point = row['point']; fp = _fraction(point)
        row.update(point_hex=point.hex(), stored_coordinate_exact=str(fp))
        if row['kind'] == 'requested_cell_midpoint':
            j = row['request_cell']
            if not x[j] < point < x[j+1]:
                row.update(status='blocked_no_distinct_binary64_midpoint',
                           old_cell=j, old_interval=[float(x[j]),float(x[j+1])])
                blocked.append(row); request_rows.append(row); continue
        exact = np.flatnonzero(x == point)
        if len(exact):
            row.update(status='already_exactly_present', old_node=int(exact[0]),
                       old_node_byte_identity=(np.float64(point).tobytes() == x[int(exact[0])].tobytes()))
            request_rows.append(row); continue
        if not x[0] < point < x[-1]:
            row.update(status='blocked_outside_open_input_domain')
            blocked.append(row); request_rows.append(row); continue
        if any(point == q for q in accepted_points):
            row.update(status='already_requested_identical_coordinate')
            request_rows.append(row); continue
        j = int(np.searchsorted(x, point)-1)
        lo, hi = _fraction(x[j]), _fraction(x[j+1])
        ulp = max(_fraction(abs(float(np.spacing(v)))) for v in (float(x[j]), point, float(x[j+1])))
        guard = max(int(minimum_ulps)*ulp, _fraction(minimum_child_fraction)*(hi-lo))
        neighbours = [lo, hi]+[_fraction(q) for q in accepted_points if x[j] < q < x[j+1]]
        distance = min(abs(fp-q) for q in neighbours)
        row.update(old_cell=j, old_interval=[float(x[j]), float(x[j+1])],
            nearest_existing_or_inserted_distance_exact=str(distance),
            declared_guard_exact=str(guard), left_distance_exact=str(fp-lo), right_distance_exact=str(hi-fp))
        if distance <= guard:
            row.update(status='blocked_near_existing_or_inserted_point',
                       point_snapped=False, old_mesh_or_window_moved=False)
            blocked.append(row); request_rows.append(row); continue
        accepted_points.append(point)
        row.update(status='inserted_at_exact_requested_binary64_coordinate')
        request_rows.append(row)

    points = np.array(sorted(accepted_points), dtype=np.float64)
    xx = np.sort(np.r_[x, points])
    old_ids, new_ids = np.searchsorted(xx, x), np.searchsorted(xx, points)
    yy = np.empty((len(xx), y.shape[1]), dtype=np.float64)
    yy[old_ids] = y
    source_cells = np.searchsorted(x, points)-1
    if len(points):
        theta = (points-x[source_cells])/(x[source_cells+1]-x[source_cells])
        yy[new_ids] = y[source_cells]+theta[:,None]*(y[source_cells+1]-y[source_cells])
    if not same_bits(xx[old_ids], x) or not same_bits(yy[old_ids], y):
        raise AssertionError('Existing defining bytes changed during pure interpolation')
    row_errors = [F(0)]*len(xx)
    rounding_rows = []
    for j, point, node in zip(source_cells, points, new_ids):
        lo, hi, actual = _fraction(x[j]), _fraction(x[j+1]), _fraction(point)
        theta = (actual-lo)/(hi-lo)
        error = F(0)
        for k in range(y.shape[1]):
            exact = (1-theta)*_fraction(y[j,k])+theta*_fraction(y[j+1,k])
            error = max(error, abs(_fraction(yy[node,k])-exact))
        row_errors[int(node)] = error
        rounding_rows.append(dict(old_cell=int(j), new_node=int(node), actual_s=float(point),
            actual_s_hex=float(point).hex(), actual_interpolation_fraction=str(theta),
            coefficient_error_exact_upper=str(error)))
    max_error = max(row_errors, default=F(0))
    # Multiple new points may occur in one old cell: both child endpoint
    # errors contribute. The one-midpoint-only slope estimate is not used.
    slope_error = max(((row_errors[j]+row_errors[j+1])/(_fraction(xx[j+1])-_fraction(xx[j]))
                       for j in range(len(xx)-1)), default=F(0))
    coordinate_error = max((F(row.get('exact_midpoint_coordinate_error', '0'))
                            for row in request_rows), default=F(0))
    maps = []
    for j in range(len(x)-1):
        children = list(range(int(old_ids[j]), int(old_ids[j+1])))
        maps.append(dict(old_cell=j, old_interval=[float(x[j]),float(x[j+1])],
            new_cells=children, new_cell_range=[children[0],children[-1]+1]))
    split = [j for j, row in enumerate(maps) if len(row['new_cells']) > 1]
    operation = 'physical_point_subdivision' if len(points) else 'restore_saved_mesh'
    definition = dict(schema=SCHEMA, operation=operation,
        insertion_kind='explicit saved binary64 physical points plus optional input-cell midpoints',
        old_mesh=x.tolist(), actual_mesh=xx.tolist(), split_old_cells=split,
        requested_midpoint_cells=cells, requested_explicit_points=[float(q) for q in physical_points],
        requested_point_rows=request_rows, blocked_point_rows=blocked,
        all_requested_points_exactly_present=not blocked,
        old_node_to_new_node=old_ids.tolist(), inserted_node_indices=new_ids.tolist(),
        inserted_coordinates=points.tolist(), old_cell_to_new_cells=maps,
        old_node_count=len(x), new_node_count=len(xx),
        all_old_node_bytes_preserved=True, old_raw_bytes_preserved_before_gauge=True,
        real_arithmetic_P1_injection_preserves_complete_function=True,
        saved_binary64_field_is_claimed_exactly_identical=not len(points),
        interpolation_rounding=dict(rows=rounding_rows,
            raw_coefficient_uniform_error_exact_upper=str(max_error),
            raw_coefficient_uniform_error_float=float(max_error),
            raw_coefficient_cell_slope_error_exact_upper=str(slope_error),
            raw_coefficient_cell_slope_error_float=float(slope_error),
            midpoint_coordinate_error_exact_upper=str(coordinate_error),
            explicit_binary64_requested_point_coordinate_error='0',
            slope_bound='(left endpoint error + right endpoint error)/actual child width'),
        near_point_policy=dict(minimum_ulps=int(minimum_ulps),
            minimum_child_fraction=float(minimum_child_fraction),
            comparison='exact rational distance <= max(minimum_ulps*local binary64 ulp, fraction*input-cell width)',
            action='report blocked request; never snap or move an original point/window'),
        minimum_actual_cell_width=float(np.min(np.diff(xx))),
        physical_metric_changed=False, full_function_definitions_changed=False,
        Fourier_order_changed=False, tail_degree_changed=False,
        new_finite_equations_and_quadrature=bool(len(points)),
        old_finite_residual_preservation_claimed=False, nonlinear_solve_performed=False)
    return xx, yy, definition


def _plateau_audit(saved):
    original = decoded(saved['coast_reference_definition'])
    plateau = saved_gauss_plateau_points(saved)
    entry, exit = map(float, original['support'])
    # The factory supplies the live original reference for the length;
    # no new reference or window is constructed here.
    return plateau, entry, exit, float(original['rim_fraction'])


def create_physical_point_refined_problem(source, *, saved_field,
        physical_points=(), midpoint_cells=(), include_saved_gauss_plateau=False,
        minimum_ulps=16, minimum_child_fraction=1e-12, **kwargs):
    """Thin preprocessing followed by the unchanged R163 v3 reconstruction.

    No partial alignment is silently accepted. A blocked request raises
    UnsafePointInsertion with the complete exact audit, before constructing
    or modifying a problem. Subsequent restarts use existing v3 split_cells=().
    """
    saved = load_npz(saved_field) if isinstance(saved_field,(str,Path)) else saved_field
    midpoint_cells = tuple(midpoint_cells)
    explicit = list(physical_points)
    copied_plateau = saved_gauss_plateau_points(saved) if include_saved_gauss_plateau else ()
    explicit.extend(copied_plateau)
    xx, yy, definition = refine_at_physical_points(saved['mesh'], saved['corrections'],
        physical_points=explicit, midpoint_cells=midpoint_cells,
        minimum_ulps=minimum_ulps, minimum_child_fraction=minimum_child_fraction)
    definition['saved_gauss_plateau_endpoint_requests'] = list(copied_plateau)
    if definition['blocked_point_rows']:
        raise UnsafePointInsertion(definition)
    prepared = {key:np.array(value,copy=True) for key,value in saved.items()}
    prepared['mesh'], prepared['corrections'] = xx, yy
    # v3 constructs the original mathematical provider, verifies every
    # frozen definition, and recomputes the whole support/gauge/index set.
    problem = create_midpoint_refined_problem(source, saved_field=prepared, split_cells=(), **kwargs)
    rebind = copy.deepcopy(problem.radial_refinement_definition)
    plateau, entry, exit, fraction = _plateau_audit(saved)
    rim = float(problem.coast_reference.length*fraction)
    analytic_left, analytic_right = _fraction(entry)+_fraction(rim), _fraction(exit)-_fraction(rim)
    inward_left = _fraction(plateau[0])-analytic_left
    inward_right = analytic_right-_fraction(plateau[1])
    if inward_left < 0 or inward_right < 0:
        raise ValueError('The saved plateau is not an inward subset of the unchanged exact S5 platform; no window is moved by this helper')
    definition['whole_hat_platform_audit'] = dict(
        copied_declared_plateau=list(plateau), actual_rim_exact=str(_fraction(rim)),
        analytic_S5_platform_exact=[str(analytic_left),str(analytic_right)],
        left_declared_endpoint_inward_distance_exact=str(inward_left),
        right_declared_endpoint_inward_distance_exact=str(inward_right),
        stored_plateau_is_sufficient_for_exact_whole_hat_annihilation=True,
        analytic_window_or_stored_window_changed=False,
        declared_plateau_endpoints_exactly_in_new_mesh=[bool(np.any(xx==v)) for v in plateau],
        analytic_platform_boundary_claimed_equal_to_stored_binary_endpoint=False)
    for key in ('matched_function_packets','original_representation_kind','representation_kind_unchanged',
                'actual_trace_scalars_copied_from_saved_packet','new_raw_unknown_count',
                'new_original_equation_count','tail_parameter_count','physical_parameter_count',
                'independent_tail_layout_preserved'):
        definition[key] = rebind[key]
    definition.update(helper_source=identity(__file__),
        reused_R163_source=identity(Path(__file__).with_name('fd2d_gc_midpoint_refined_positive_trace_v3.py')),
        old_inactive_l_raw_nodes=np.asarray(saved['inactive_l_raw_nodes']).tolist(),
        new_inactive_l_raw_nodes=problem.inactive_l_raw_nodes.tolist(),
        old_inactive_trace_nodes=np.asarray(saved['inactive_raw_trace_nodes']).tolist(),
        new_inactive_trace_nodes=problem.inactive_trace_nodes.tolist(),
        new_trace_gauge_pairs=problem.trace_gauge_pairs.tolist())
    problem._subdivision_saved = {key:np.array(value,copy=True) for key,value in saved.items()}
    problem.radial_refinement_definition = definition
    problem.targeted_mesh_definition.update(actual_nodes=xx.tolist(), actual_node_count=len(xx),
        further_midpoint_subdivision=bool(tuple(midpoint_cells)), further_physical_point_subdivision=True,
        subdivision_parent_nodes=np.asarray(saved['mesh']).tolist())
    problem.atlas_mesh_definition = dict(schema='fd2d-explicit-ruling-atlas-computational-mesh-v1',
        old_nodes=np.asarray(saved['mesh']).tolist(),actual_nodes=xx.tolist(),
        added_nodes=definition['inserted_coordinates'],old_node_count=len(saved['mesh']),
        actual_node_count=len(xx),minimum_cell=float(np.min(np.diff(xx))),
        all_old_nodes_retained=True,physical_metric_changed=False,finite_representation_changed=bool(len(xx)!=len(saved['mesh'])))
    return problem


def checkpoint_arrays(problem, vector, candidate_sha256, *, refinement_definition):
    """The original schema/checkpoint writer maps each old interior interval to all children."""
    return _checkpoint_arrays(problem, vector, candidate_sha256,
                              refinement_definition=refinement_definition)
