#!/usr/bin/env python3
"""One actual R159 small-row fixture, with an independent frozen tall direction.

No BVP, body reconstruction, full-field certification or repeated test grid
is run. Raw local rows are retained ONLY in this explicit comparison script.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import json
import time
import traceback
import resource
from pathlib import Path
import numpy as np
from scipy import sparse
from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_raw_bump_positive_trace import PositiveTraceRawBumpDAE
from fd2d_gc_nested_angular_positive_trace import FixedTailDegreePositiveTraceDAE
from fd2d_gc_local_normal_system import bounded_normal_direction
from fd2d_gc_positive_trace_stream_normal import stream_positive_trace_normal
from fd2d_gc_positive_trace_bounded_schur import bounded_bump_direction


def maximum(value):
    if sparse.issparse(value):
        return float(np.max(abs(value.data), initial=0.))
    return float(np.max(abs(np.asarray(value)), initial=0.))


def relative_difference(a, b):
    return maximum(a-b)/max(1., maximum(a), maximum(b))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field', type=Path, required=True)
    ap.add_argument('--run-report', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    ap.add_argument('--damping', type=float, default=1e-3)
    args = ap.parse_args()
    stem = args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh immutable check stem')
    start = time.monotonic()
    sources = ['fd2d_gc_local_normal_system.py', 'fd2d_gc_positive_trace_stream_normal.py',
        'fd2d-metric-local-normal-check.py', 'fd2d_gc_positive_trace_bounded_schur.py',
        'fd2d_gc_raw_bump_positive_trace.py', 'fd2d_gc_positive_trace_merit.py',
        'fd2d_gc_gauss_cell_positive_trace.py', 'fd2d_gc_gauss_cell_codazzi_chunked.py']
    source_ids = {name: identity(Path(__file__).parent/name) for name in sources}
    report = dict(schema='fd2d-R159-actual-local-normal-equivalence-check-v1',
        field=identity(args.field), source_run=identity(args.run_report), sources=source_ids,
        status='running', passed=False, no_BVP_run=True, no_body_run=True,
        no_continuous_certificate=True, fixture_scope='Selected existing nodes and cells of the immutable actual v16 field; not the complete objective')
    try:
        saved = load_npz(args.field)
        source_report = json.loads(args.run_report.read_text())
        settings = source_report['settings']
        candidate = Path(settings['candidate'])
        radius = Path(settings['radius_packet'])
        proof = json.loads(radius.read_text())
        if not proof['passed'] or proof['candidate_sha256'] != identity(candidate)['sha256']:
            raise ValueError('Wrong actual radius proof identity')
        witness = dict(**identity(radius), candidate_sha256=proof['candidate_sha256'])
        kwargs = dict(modes=int(saved['modes']), max_step=settings['mesh_step'], gap=settings['gap'],
            reference_inlet=Path(settings['reference_inlet']), reference_cache=Path(settings['reference_cache']),
            reference_rim_fraction=settings['reference_rim_fraction'], minimum_active_n=settings['minimum_active_n'],
            mesh_relative_tolerance=settings['mesh_relative_tolerance'], base_lower_bound='4/5',
            base_lower_provenance=witness, radius_floor=settings['radius_floor'])
        if 'tail_parameter_count' in saved:
            problem = FixedTailDegreePositiveTraceDAE(candidate,
                tail_parameter_count=int(saved['tail_parameter_count']), **kwargs)
        else:
            problem = PositiveTraceRawBumpDAE(candidate, **kwargs)
        if (str(saved['candidate_sha256']) != identity(candidate)['sha256']
            or not np.array_equal(saved['mesh'], problem.x)
            or not np.array_equal(saved['profile_supports'], problem.profile.supports)):
            raise ValueError('Saved object is not the explicitly reconstructed physical field')
        for name in ('seed_weight_definition', 'angular_atlas_definition',
                     'gauss_l_definition', 'positive_trace_definition'):
            if json.loads(str(saved[name])) != getattr(problem, name):
                raise ValueError('Different saved full function definition: '+name)
        vector = np.r_[saved['corrections'].ravel(), saved['parameters']]
        before = vector.copy()
        central_last = int(problem.fixed_central_nodes[-1])
        # These are existing v16 mesh cells, including both nonlinear rims.
        cells = np.unique(np.r_[0, central_last, 63, 64, 67, 70, 71, 118, 119, 120, 121])
        if np.any(cells >= problem.N-1):
            raise ValueError('This immutable local fixture requires the declared 123-node mesh')
        nodes = np.unique(np.r_[cells, cells+1])
        blocks = []
        observed = []
        total = problem.N*problem.q
        def observe(label, node_ids, residual, local_J):
            coo = sparse.coo_matrix(local_J)
            columns = np.r_[np.concatenate([j*problem.q+np.arange(problem.q) for j in node_ids])
                if node_ids else np.empty(0, int), total+np.arange(problem.parameter_count)]
            J = sparse.coo_matrix((coo.data, (coo.row, columns[coo.col])),
                shape=(len(residual), problem.size)).tocsc()
            blocks.append((np.asarray(residual).copy(), J))
            observed.append(dict(label=label, nodes=list(node_ids), rows=len(residual), nnz=int(J.nnz)))
        print(json.dumps(dict(event='actual_small_fixture_start', nodes=nodes.tolist(), cells=cells.tolist())), flush=True)
        normal, stream_info = stream_positive_trace_normal(problem, vector,
            curvature_cap=settings['curvature_cap'], curvature_weight=settings['curvature_weight'],
            high_gauss_weight=settings['high_gauss_weight'], high_codazzi_weight=settings['high_codazzi_weight'],
            block_cells=2, node_indices=nodes, cell_indices=cells, observer=observe)
        residual = np.concatenate([r for r, J in blocks])
        J = sparse.vstack([J for r, J in blocks], format='csc')
        del blocks
        mapping = normal.mapping
        # Independently repeat the frozen tall elimination; do not reuse
        # LocalNormalSystem.transform to define the reference matrix.
        Jf = J[:, mapping.free].tocsc()
        where = {int(old): i for i, old in enumerate(mapping.free)}
        if len(mapping.pairs):
            old = J[:, mapping.pairs[:, 1]].tocoo()
            target = np.array([where[int(ni)] for ni, li in mapping.pairs], int)
            Jf -= sparse.coo_matrix((old.data, (old.row, target[old.col])), shape=Jf.shape).tocsc()
        central_columns = np.concatenate([j*problem.q+np.arange(problem.e) for j in mapping.central_nodes])
        central_map = sparse.vstack([sparse.csc_matrix(problem.core_coefficients)
            for _ in mapping.central_nodes], format='csc')
        Jp = (J[:, total:]+sparse.hstack((J[:, central_columns]@central_map,
            sparse.csc_matrix((len(residual), problem.parameter_count-problem.K))), format='csc')).tocsc()
        Hff, Hfp, Hpp = (Jf.T@Jf).tocsc(), (Jf.T@Jp).toarray(), (Jp.T@Jp).toarray()
        gf, gp = np.asarray(Jf.T@residual).ravel(), np.asarray(Jp.T@residual).ravel()
        nf, np_ = np.asarray(Jf.multiply(Jf).sum(axis=0)).ravel(), np.asarray(Jp.multiply(Jp).sum(axis=0)).ravel()
        comparisons = dict(Hff=relative_difference(normal.hff(), Hff), Hfp=relative_difference(normal.Hfp, Hfp),
            Hpp=relative_difference(normal.Hpp, Hpp), gf=relative_difference(normal.gf, gf),
            gp=relative_difference(normal.gp, gp), field_column_squared_norm=relative_difference(normal.field_norm_squared, nf),
            parameter_column_squared_norm=relative_difference(normal.parameter_norm_squared, np_),
            residual_squared=abs(normal.residual_squared-float(residual@residual))/max(1., float(residual@residual)))
        coo = Hff.tocoo()
        node_of_free = mapping.free//problem.q
        band = int(np.max(abs(node_of_free[coo.row]-node_of_free[coo.col]), initial=0))
        options = dict(damping=args.damping, central_floor=settings['central_floor'],
            central_cap=settings['central_cap'], profile_box=settings['profile_box'], preserve_gap=True)
        old_direction, old_info = bounded_bump_direction(problem, vector, residual, J, **options)
        new_direction, new_info, reduced = bounded_normal_direction(problem, vector, normal,
            **options, return_reduced=True)
        nd = np.linalg.norm(old_direction)
        direction_error = float(np.linalg.norm(new_direction-old_direction)/max(1., nd))
        action_error = float(np.linalg.norm(J@(new_direction-old_direction))/max(1., np.linalg.norm(J@old_direction)))
        explicit_norm = float(np.linalg.norm(residual+J@new_direction))
        constraints = dict(cut_direction_maximum=maximum(new_direction[total-problem.q:total]),
            deleted_coast_l_direction_maximum=maximum(new_direction[np.concatenate([
                j*problem.q+np.arange(problem.d, problem.q) for j in problem.inactive_l_raw_nodes])]),
            trace_pair_sum_maximum=maximum(new_direction[mapping.pairs[:, 0]]+new_direction[mapping.pairs[:, 1]]),
            central_mapping_maximum=max(maximum(new_direction[j*problem.q:j*problem.q+problem.e]
                -problem.core_coefficients@new_direction[total:total+problem.K]) for j in mapping.central_nodes))
        report.update(status='completed', stream=stream_info, observed_row_blocks=observed,
            original_vector_changed_maximum=maximum(vector-before), normal_comparisons_relative_maximum=comparisons,
            actual_field_normal_block_bandwidth=band, old_direction=old_info, streamed_direction=new_info,
            direction_relative_l2=direction_error, direction_action_relative_l2=action_error,
            explicit_new_linear_residual_norm=explicit_norm,
            normal_residual_norm_difference=abs(explicit_norm-new_info['linear_residual_norm']),
            exact_elimination_constraint_errors=constraints,
            tall_fixture_matrix=dict(rows=J.shape[0], columns=J.shape[1], nnz=int(J.nnz),
                storage_bytes=int(J.data.nbytes+J.indices.nbytes+J.indptr.nbytes)),
            normal_storage_bytes=normal.storage_bytes(),
            full_field_or_BVP_success_claimed=False,
            comparison_scope='One actual small row subset, same weights and constrained direction; equality is proved algebraically for the full local objective, not inferred from this fixture')
        report['passed'] = bool(max(comparisons.values()) < 2e-12 and band <= 1
            and direction_error < 2e-4 and action_error < 2e-4
            and max(constraints.values()) < 1e-12 and report['original_vector_changed_maximum'] == 0.
            and old_info['optimizer_success'] and new_info['optimizer_success'])
        witness = stem.with_name(stem.name+'-witnesses.npz')
        np.savez_compressed(witness, selected_nodes=nodes, selected_cells=cells,
            old_direction=old_direction, new_direction=new_direction, residual=residual,
            field_norm_squared=normal.field_norm_squared, parameter_norm_squared=normal.parameter_norm_squared,
            reduced_schur=reduced['schur'], reduced_gradient=reduced['gradient'])
        report['witnesses'] = identity(witness)
    except BaseException as exc:
        report.update(status='failed', exception_type=type(exc).__name__, exception=str(exc), traceback=traceback.format_exc())
        print(report['traceback'], flush=True)
    report['seconds'] = time.monotonic()-start
    report['peak_rss_kib'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report['sources_unchanged'] = all(identity(Path(__file__).parent/name)['sha256'] == item['sha256']
        for name, item in source_ids.items())
    if not report['sources_unchanged']:
        report['passed'] = False
    destination = stem.with_name(stem.name+'-report.json')
    destination.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(event='check_complete', status=report['status'], passed=report['passed'],
        seconds=report['seconds'], report=str(destination))), flush=True)
    return 0 if report['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
