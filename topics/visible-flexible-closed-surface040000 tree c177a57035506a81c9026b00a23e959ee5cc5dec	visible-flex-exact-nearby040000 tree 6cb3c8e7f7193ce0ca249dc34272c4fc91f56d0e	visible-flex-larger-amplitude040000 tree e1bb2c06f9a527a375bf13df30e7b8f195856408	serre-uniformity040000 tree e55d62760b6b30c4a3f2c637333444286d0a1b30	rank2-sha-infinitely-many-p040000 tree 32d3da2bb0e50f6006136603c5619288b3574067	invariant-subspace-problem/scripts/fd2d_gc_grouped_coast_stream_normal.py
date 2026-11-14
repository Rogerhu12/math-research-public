"""R159 local normals for the separately declared R165 grouped coast rule.

This separate adapter preserves the frozen assembly and accepts a callable
for the same complete finite cell equations; the default is the original.
No class-name spoofing or change to the guarded background consumers occurs.

The full physical field and nonlinear maps are the frozen provider's.
Only node packets and bounded cell chunks are live. All row construction,
Jacobian mapping and normal.add operations match the frozen subset stream.
The selected R165 cell consumer changes the finite coast equations; this
wrapper only aggregates its different diagnostics without inventing an
independent known-lifting quantity. Subsets remain explicitly incomplete.
"""
from __future__ import annotations
import copy
import time
import numpy as np
from scipy import sparse
from fd2d_gc_local_normal_system import LocalNormalSystem
from fd2d_gc_codazzi_complement import _high
from fd2d_gc_d2_complements import d2_high_rows
from fd2d_gc_positive_trace_merit import curvature_merit
from fd2d_gc_raw_bump_positive_trace import actual_state_columns
from fd2d_gc_grouped_coast_codazzi import gauss_cell_positive_trace_grouped_coast


def radial_view(problem, indices):
    """Same frozen functions at explicitly selected saved radial nodes."""
    indices = np.asarray(indices, int)
    view = copy.copy(problem)
    view.x = np.asarray(problem.x[indices], float).copy()
    view.N, view.h = len(indices), np.diff(view.x)
    view.size = view.N*view.q+view.parameter_count
    view.residual_size = view.N*view.q+2*view.K+2
    view.coords = {key: np.asarray(value[:, indices], float).copy()
                   for key, value in problem.coords.items()}
    view._operator_cache = {}
    view._cell_gauss_view_cache = None
    view._chunked_gauss_codazzi_views = None
    return view


def _assert_local_cells(matrix, rows_per_cell, cell_count, q):
    coo = matrix.tocoo(copy=False)
    fields = (coo.col < (cell_count+1)*q) & (coo.data != 0.)
    cell, node = coo.row[fields]//rows_per_cell, coo.col[fields]//q
    if np.any((node != cell) & (node != cell+1)):
        raise ArithmeticError('A claimed local cell Jacobian has a non-adjacent field column')


def stream_positive_trace_normal(problem, vector, *, curvature_cap=7.2,
        curvature_weight=1., high_gauss_weight=1., high_codazzi_weight=1.,
        order=2, block_cells=8, node_indices=None, cell_indices=None,
        include_boundary=True, observer=None, progress=None,
        cell_consumer=gauss_cell_positive_trace_grouped_coast):
    """Return (LocalNormalSystem, finite diagnostics) without a whole J.

The optional observer receives raw local blocks only for one-off checks;
production callers must not use it to retain all rows. Caller-selected
subsets are marked incomplete and are never claimed to be the full merit.
    """
    start_time = time.monotonic()
    if not callable(cell_consumer):
        raise TypeError("cell_consumer must be a callable for the complete finite cell equations")
    if int(order) != 2:
        raise ValueError('Keep the declared order=2 interface and original G2 diagnostic grid')
    if int(block_cells) != block_cells or block_cells < 1:
        raise ValueError('Use a positive cell chunk size')
    for value in (curvature_weight, high_gauss_weight, high_codazzi_weight):
        if not np.isfinite(value) or value < 0:
            raise ValueError('Merit weights must be finite and nonnegative')
    y, p = problem.unpack(vector)
    problem.core(p[:problem.K])  # share the existing immutable core result in small views
    nodes = np.arange(problem.N) if node_indices is None else np.unique(np.asarray(node_indices, int))
    cells = np.arange(problem.N-1) if cell_indices is None else np.unique(np.asarray(cell_indices, int))
    if np.any((nodes < 0) | (nodes >= problem.N)) or np.any((cells < 0) | (cells >= problem.N-1)):
        raise ValueError('Fixture indices outside the actual saved mesh')
    normal = LocalNormalSystem(problem)
    angular_rows = d2_high_rows(problem)
    w = problem.window()
    selected = (w != 1.) & (problem.x < problem.trace_ramp_stop)
    selected[-1] = False
    maxima = dict(full_gauss=0., retained_gauss=0., omitted_gauss=0., formal_curvature=0.,
                  full_codazzi=0., retained_codazzi=0., omitted_codazzi=0., known_lifting_change=None,
                  G2_sampled_interior_Gauss=None, fine_sampled_interior_Gauss=None)
    grouped_rules = []; grouped_cells = []
    fine_minimum_active_n = None
    for node in nodes:
        view = radial_view(problem, [node])
        local = np.r_[y[node], p]
        _, data = view.evaluate(local)
        full = data['full_gauss'][:, 0]
        maxima['full_gauss'] = max(maxima['full_gauss'], float(np.max(abs(full))))
        if selected[node]:
            dn, dm, dl = actual_state_columns(view, data, 0)
            n, m, l = data['fields'][:, 0].T
            state = l[:, None]*dn+n[:, None]*dl-2*m[:, None]*dm
            fp = data['fields_parameters'][:, 0]
            par = l[:, None]*fp[:, 0]+n[:, None]*fp[:, 2]-2*m[:, None]*fp[:, 1]
            par[:, problem.profile_parameter_slice] -= data['profile_jet']['K_parameters'][0]
            retained = problem.PE@full
            jr = np.hstack((problem.PE@state, problem.PE@par))
            normal.add(retained, jr, (node,), label='node_G', observer=observer)
            omitted = _high(full[:, None], problem.E, problem.PE)[:, 0]
            high = high_gauss_weight*angular_rows.project(omitted, 'even')
            jh = high_gauss_weight*angular_rows.project(
                _high(np.hstack((state, par)), problem.E, problem.PE), 'even')
            normal.add(high, jh, (node,), label='node_high_G', observer=observer)
            maxima['retained_gauss'] = max(maxima['retained_gauss'], float(np.max(abs(retained), initial=0.)))
            maxima['omitted_gauss'] = max(maxima['omitted_gauss'], float(np.max(abs(omitted), initial=0.)))
        curvature = curvature_merit(view, local, cap=curvature_cap, weight=curvature_weight, data=data, jacobian=True)
        normal.add(curvature['residual'], curvature['jacobian'], (node,), label='node_curvature', observer=observer)
        maxima['formal_curvature'] = max(maxima['formal_curvature'], curvature['info']['sampled_formal_curvature_maximum'])
        del data, curvature, view
        if progress is not None:
            progress('node', int(node), normal.rows)
    position = 0
    while position < len(cells):
        first = int(cells[position])
        count = 1
        while (count < block_cells and position+count < len(cells)
               and cells[position+count] == first+count):
            count += 1
        stop = first+count
        view = radial_view(problem, np.arange(first, stop+1))
        local = np.r_[y[first:stop+1].ravel(), p]
        packet = cell_consumer(view, local, order=order,
            high_weight=high_codazzi_weight, jacobian=True)
        jr, jh = packet['retained_jacobian'], packet['high_jacobian']
        if len(packet['retained_residual']) != count*problem.d or len(packet['high_residual']) != count*angular_rows.cell_rows:
            raise ArithmeticError('Unexpected local cell row count')
        _assert_local_cells(jr, problem.d, count, problem.q)
        _assert_local_cells(jh, angular_rows.cell_rows, count, problem.q)
        for local_cell in range(count):
            cell = first+local_cell
            columns = np.r_[np.arange(local_cell*problem.q, (local_cell+2)*problem.q),
                            (count+1)*problem.q+np.arange(problem.parameter_count)]
            rsection = slice(local_cell*problem.d, (local_cell+1)*problem.d)
            hsection = slice(local_cell*angular_rows.cell_rows, (local_cell+1)*angular_rows.cell_rows)
            normal.add(packet['retained_residual'][rsection], jr[rsection][:, columns],
                (cell, cell+1), label='cell_C', observer=observer)
            normal.add(packet['high_residual'][hsection], jh[hsection][:, columns],
                (cell, cell+1), label='cell_high_C', observer=observer)
        for key, packet_key in (('full_codazzi', 'full_codazzi_cells'),
                                ('retained_codazzi', 'retained_cells'),
                                ('omitted_codazzi', 'omitted_codazzi_cells')):
            maxima[key] = max(maxima[key], float(np.max(abs(packet[packet_key]), initial=0.)))
        # R165 retains legacy point_gauss/point ordering but reports its
        # whole-actual fine points separately. No known-only comparison was
        # evaluated, so it must remain None even when all cells are outside.
        g2 = float(np.max(abs(packet['point_gauss']), initial=0.))
        previous = maxima['G2_sampled_interior_Gauss']
        maxima['G2_sampled_interior_Gauss'] = g2 if previous is None else max(previous, g2)
        selected_grouped = packet['info'].get('grouped_coast_local_cells', [])
        grouped_cells.extend(first+int(j) for j in selected_grouped)
        for observation in packet['info'].get('grouped_coast_rules', []):
            record = dict(observation, global_cell=first+int(observation['local_cell']),
                          stream_chunk_first_cell=first)
            grouped_rules.append(record)
            fine = float(observation['fine_sampled_Gauss_maximum'])
            previous = maxima['fine_sampled_interior_Gauss']
            maxima['fine_sampled_interior_Gauss'] = fine if previous is None else max(previous, fine)
            minimum = observation['fine_sampled_minimum_active_n']
            if minimum is not None:
                minimum = float(minimum)
                fine_minimum_active_n = minimum if fine_minimum_active_n is None else min(fine_minimum_active_n, minimum)
        del packet, jr, jh, view
        position += count
        if progress is not None:
            progress('cell_chunk', stop-1, normal.rows)
    if include_boundary:
        e, d, q, P = problem.e, problem.d, problem.q, problem.parameter_count
        J = np.zeros((e, q+P)); J[:, d:q] = np.eye(e)
        normal.add(y[-1, d:], J, (problem.N-1,), label='cut_l', observer=observer)
        J = np.zeros((d, q+P)); J[:, :d] = np.eye(d)
        J[:e, q:q+problem.K] = -problem.core_coefficients
        r = y[0, :d].copy(); r[:e] -= problem.core_coefficients@p[:problem.K]
        normal.add(r, J, (0,), label='central_boundary', observer=observer)
        J = np.zeros((d, q+P)); J[:, :d] = np.eye(d)
        normal.add(y[-1, :d], J, (problem.N-1,), label='cut_nm', observer=observer)
        _, axes = problem.core(p[:problem.K])
        J = np.zeros((1, P)); J[0, :problem.K] = np.asarray(axes['gap_jacobian'])/problem.gap
        normal.add([(float(axes['gap'])-problem.gap)/problem.gap], J, (), label='gap', observer=observer)
    info = dict(schema='fd2d-R159-R165-local-node-cell-normal-grouped-consumer-v1',
        cell_consumer_module=cell_consumer.__module__, cell_consumer_name=cell_consumer.__name__,
        full_finite_objective=(len(nodes) == problem.N and len(cells) == problem.N-1 and bool(include_boundary)),
        selected_node_indices=nodes.tolist(), selected_cell_indices=cells.tolist(),
        boundary_rows_included=bool(include_boundary), rows=normal.rows, local_blocks=normal.blocks,
        row_groups=normal.row_groups, finite_maxima=maxima, known_fine_coast_cells=None,
        known_lifting_full_change_maximum=None,
        known_lifting_change_maximum_not_separately_evaluated=True,
        grouped_coast_global_cells=grouped_cells, grouped_coast_cell_count=len(grouped_cells),
        grouped_coast_rules=grouped_rules,
        fine_sampled_interior_Gauss_maximum=maxima['fine_sampled_interior_Gauss'],
        fine_sampled_minimum_active_n=fine_minimum_active_n,
        point_gauss_scope='Only the original G2 diagnostic points; fine points remain separately named',
        fine_Gauss_scope='Only explicitly evaluated R165 grouped_coast_rules; None means no such sample in this subset',
        finite_objective_reference='Selected cell consumer; R165 is different from the old v25 coast rule',
        order=order, block_cells=block_cells, curvature_cap=curvature_cap,
        curvature_weight=curvature_weight, high_gauss_weight=high_gauss_weight, high_codazzi_weight=high_codazzi_weight,
        free_field_unknowns=normal.mapping.count, global_parameter_unknowns=problem.parameter_count,
        original_parameter_layout=problem.parameter_layout(),
        raw_equations_and_finite_merit_unchanged_in_exact_arithmetic=True,
        whole_tall_jacobian_stored=False, observation_callback_used=observer is not None,
        observer_may_store_tall_fixture_only=True, finite_certificate=False,
        field_normal_bandwidth='one adjacent radial-node block after exact elimination',
        unscaled_normal_storage_bytes=normal.storage_bytes(), seconds=time.monotonic()-start_time)
    normal.info = info
    return normal, info
