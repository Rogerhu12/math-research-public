"""The frozen Gauss-cell Codazzi formula assembled in bounded cell blocks.

Every cell depends only on its own two correction nodes and the shared
physical parameters. This module changes assembly/storage only. The old
unknown mesh, quadrature points, field and finite equations are identical.
"""
from __future__ import annotations
import copy
import numpy as np
from scipy import sparse
from fd2d_gc_gauss_cell_codazzi import gauss_cell_codazzi as _whole_formula


def _chunks(problem, block_cells):
    block_cells = int(block_cells)
    if block_cells < 1:
        raise ValueError('A block must contain at least one full radial cell')
    key = (block_cells, np.asarray(problem.x, float).tobytes())
    cached = getattr(problem, '_chunked_gauss_codazzi_views', None)
    if cached is not None and cached[0] == key:
        return cached[1]
    blocks = []
    for start in range(0, problem.N-1, block_cells):
        stop = min(start+block_cells, problem.N-1)
        view = copy.copy(problem)
        view.x = np.array(problem.x[start:stop+1], copy=True)
        view.N = len(view.x)
        view.h = np.diff(view.x)
        view.size = view.N*view.q+view.parameter_count
        view.residual_size = view.N*view.q+2*view.K+2
        view.coords = {k: np.asarray(v, float) for k, v in view.chart.coordinates(view.x).items()}
        view._operator_cache = {}
        view._cell_gauss_view_cache = None
        view._chunked_gauss_codazzi_views = None
        blocks.append((start, stop, view))
    problem._chunked_gauss_codazzi_views = (key, blocks)
    return blocks


def gauss_cell_codazzi(problem, vector, *, order=2, high_weight=1., jacobian=True,
                       block_cells=16, consumer=None):
    """Same return convention as the original helper; all columns stay global."""
    z = np.asarray(vector, float)
    if z.shape != (problem.size,) or not np.all(np.isfinite(z)):
        raise ValueError('Wrong or nonfinite original full unknown vector')
    consumer = _whole_formula if consumer is None else consumer
    if not callable(consumer):
        raise ValueError('The declared cell consumer must be callable')
    y, p = problem.unpack(z)
    collected = {k: [] for k in ('retained_residual', 'high_residual', 'retained_cells',
        'omitted_codazzi_cells', 'full_codazzi_cells', 'point_gauss', 'quadrature_points')}
    retained_matrices, high_matrices, infos = [], [], []
    global_parameter_offset = problem.N*problem.q
    def global_columns(matrix, start, view):
        coo = matrix.tocoo(copy=False)
        local_parameter_offset = view.N*view.q
        columns = np.where(coo.col < local_parameter_offset,
                           coo.col+start*problem.q,
                           coo.col-local_parameter_offset+global_parameter_offset)
        answer = sparse.coo_matrix((coo.data, (coo.row, columns)),
            shape=(matrix.shape[0], problem.size)).tocsc()
        answer.eliminate_zeros()
        return answer
    for start, stop, view in _chunks(problem, block_cells):
        local = np.r_[y[start:stop+1].ravel(), p]
        result = consumer(view, local, order=order, high_weight=high_weight, jacobian=jacobian)
        for key in collected:
            collected[key].append(result[key])
        infos.append(result['info'])
        if jacobian:
            retained_matrices.append(global_columns(result['retained_jacobian'], start, view))
            high_matrices.append(global_columns(result['high_jacobian'], start, view))
        # No full quadrature lifting packet or temporary local sparse matrix
        # survives this loop iteration. Cached profile operators remain small.
        del result
    answer = {key: np.concatenate(values, axis=1 if key in
        ('omitted_codazzi_cells', 'full_codazzi_cells', 'point_gauss') else 0)
        for key, values in collected.items()}
    info = dict(infos[0])
    info.update(assembly='bounded radial-cell blocks of the unchanged original formula',
                block_cells=int(block_cells), block_count=len(infos),
                cell_consumer=consumer.__module__+'.'+consumer.__name__,
                finite_equations_changed_by_chunking=False,
                independent_unknown_columns_preserved=True)
    for key in ('retained_cell_maximum', 'sampled_full_average_codazzi_maximum',
                'sampled_omitted_average_codazzi_maximum', 'sampled_interior_Gauss_maximum'):
        info[key] = max(row[key] for row in infos)
    answer['retained_jacobian'] = None
    answer['high_jacobian'] = None
    if jacobian:
        answer['retained_jacobian'] = sparse.vstack(retained_matrices, format='csc')
        answer['high_jacobian'] = sparse.vstack(high_matrices, format='csc')
        info['retained_jacobian_nonzeros'] = int(answer['retained_jacobian'].nnz)
        info['high_jacobian_nonzeros'] = int(answer['high_jacobian'].nnz)
    answer['info'] = info
    return answer
