"""Recovery implementation of the declared complete R182/R165 cell rule.

This text was reconstructed during executor unavailability. It is not
claimed byte-identical to the pre-outage signed36 adapter. The four frozen
R182 kernel sources and the frozen R165 coast integration are reused.
A recovery baseline has its own source and output identity.
"""
from __future__ import annotations
import copy
import numpy as np
from scipy import sparse
from fd2d_gc_archive_arrays import identity
from fd2d_gc_grouped_coast_codazzi import _coast_block, _block_view
from fd2d_gc_signed_trace_cells import gauss_cell_signed_trace
from fd2d_gc_gauss_cell_frozen_operator_compatible import _OriginalR153BackgroundOnly

FINITE_RULE = ('R182 signed actual field: complete same-point split Gauss8 on cells '
    'meeting new signed supports; R165 complete same-point split Gauss8 on the '
    'original coast; original R152/R153/R155 outside those supports; exact full '
    'n/m endpoints; dynamic actual Gauss platform rows and declared interior G2 rows')
_COMPATIBLE = {}


def _outside(problem, vector, **settings):
    original = type(problem)
    if issubclass(original, _OriginalR153BackgroundOnly):
        return gauss_cell_signed_trace(problem, vector, **settings)
    if original not in _COMPATIBLE:
        _COMPATIBLE[original] = type('ExplicitSignedOriginalR153Background',
            (_OriginalR153BackgroundOnly, original), {})
    view = copy.copy(problem)
    view.__class__ = _COMPATIBLE[original]
    return gauss_cell_signed_trace(view, vector, **settings)


def gauss_cell_signed_trace_grouped(problem, vector, *, order=2, high_weight=1.,
        jacobian=True, fine_order=8, point_batch=2):
    if order != 2 or int(fine_order) != fine_order or not 2 <= fine_order <= 16:
        raise ValueError('Keep original G2 diagnostics and an explicit fine order')
    if not np.isfinite(high_weight) or high_weight < 0:
        raise ValueError('A finite nonnegative high weight is required')
    if int(point_batch) != point_batch or not 1 <= point_batch <= 8:
        raise ValueError('Use a bounded quadrature point batch')
    z = np.asarray(vector, float)
    if z.shape != (problem.size,) or not np.all(np.isfinite(z)):
        raise ValueError('Wrong actual finite vector')
    e, f = problem.gauss_l_definition['support']
    coast = (problem.x[:-1] < f) & (problem.x[1:] > e)
    y, p = problem.unpack(z)
    cuts = np.r_[0, np.flatnonzero(coast[1:] != coast[:-1])+1, problem.N-1]
    keys = ('retained_residual', 'high_residual', 'retained_cells',
        'omitted_codazzi_cells', 'full_codazzi_cells', 'point_gauss',
        'quadrature_points')
    values = {k: [] for k in keys}
    matrices = {k: [] for k in ('retained_jacobian', 'high_jacobian')}
    infos = []; coast_rules = []; signed_rules = []
    for first, last in zip(cuts[:-1], cuts[1:]):
        first, last = int(first), int(last)
        view = _block_view(problem, first, last)
        local = np.r_[y[first:last+1].ravel(), p]
        if coast[first]:
            answer = _coast_block(view, local, high_weight=high_weight,
                jacobian=jacobian, fine_order=int(fine_order), point_batch=int(point_batch))
        else:
            answer = _outside(view, local, order=2, high_weight=high_weight,
                jacobian=jacobian, fine_order=int(fine_order), point_batch=int(point_batch))
        for key in keys:
            values[key].append(answer[key])
        infos.append(answer['info'])
        for key, target in (('grouped_coast_rules', coast_rules),
                            ('grouped_signed_rules', signed_rules)):
            for row in answer['info'].get(key, []):
                target.append(dict(row, local_cell=first+int(row['local_cell'])))
        if jacobian:
            for key in matrices:
                a = answer[key].tocoo(copy=False)
                limit = view.N*view.q
                columns = np.where(a.col < limit, a.col+first*problem.q,
                    a.col-limit+problem.N*problem.q)
                matrices[key].append(sparse.coo_matrix((a.data, (a.row, columns)),
                    shape=(a.shape[0], problem.size)).tocsc())
    out = {key: np.concatenate(rows, axis=1 if key in
        ('omitted_codazzi_cells', 'full_codazzi_cells', 'point_gauss') else 0)
        for key, rows in values.items()}
    for key, rows in matrices.items():
        out[key] = sparse.vstack(rows, format='csc') if jacobian else None
        if jacobian:
            out[key].eliminate_zeros()
    fine = [float(r['fine_sampled_Gauss_maximum']) for r in coast_rules+signed_rules]
    info = dict(infos[0], schema='fd2d-recovery-complete-signed-and-coast-cell-v1',
        source_sha256=identity(__file__)['sha256'], order=2,
        grouped_coast_local_cells=np.flatnonzero(coast).tolist(),
        grouped_coast_rules=coast_rules,
        grouped_signed_local_cells=[int(r['local_cell']) for r in signed_rules],
        grouped_signed_rules=signed_rules,
        known_lifting_full_change_maximum=None,
        known_lifting_change_maximum_not_separately_evaluated=True,
        fine_sampled_interior_Gauss_maximum=max(fine) if fine else None,
        point_gauss_scope='Original G2 points only; both fine rules reported separately',
        all_subblock_info=infos, finite_radial_scheme=FINITE_RULE,
        continuous_certificate=False)
    for key in ('retained_cell_maximum', 'sampled_full_average_codazzi_maximum',
                'sampled_omitted_average_codazzi_maximum', 'sampled_interior_Gauss_maximum'):
        info[key] = max(float(row[key]) for row in infos)
    if jacobian:
        info['retained_jacobian_nonzeros'] = int(out['retained_jacobian'].nnz)
        info['high_jacobian_nonzeros'] = int(out['high_jacobian'].nnz)
    out['info'] = info
    return out
