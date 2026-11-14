#!/usr/bin/env python3
"""Finalize already saved local samples after a JSON-only producer failure.

This does not evaluate the field again. The original nonzero process exit
is explicitly retained, with hashes of both completed producer outputs.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import importlib.util
import json
from pathlib import Path
import resource
import time
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz


def scalar(q):
    if isinstance(q, np.generic):
        return float(q)
    raise TypeError(type(q).__name__)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--producer-prefix', type=Path, required=True)
    ap.add_argument('--source-report', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    if args.output.exists():
        raise FileExistsError('Use a new closed finalization path')
    started = time.monotonic()
    prefix = str(args.producer_prefix)
    receipt_path = Path(prefix+'-exit-receipt.json')
    receipt = json.loads(receipt_path.read_text())
    if receipt['exit_code'] != 1 or receipt['exception_type'] != 'TypeError':
        raise ValueError('This finalizer binds the observed JSON-only producer failure')
    for row in [receipt['source']]+receipt['retained_outputs']:
        if identity(row['path'])['sha256'] != row['sha256']:
            raise ValueError('Original closed producer bytes have changed')
    source_path = Path(receipt['source']['path'])
    spec = importlib.util.spec_from_file_location('closed_atlas_local_sample_algebra', source_path)
    algebra = importlib.util.module_from_spec(spec); spec.loader.exec_module(algebra)
    maximum, projection, spectrum = algebra.maximum, algebra.projection, algebra.spectral_summary
    samples_path, definition_path = Path(prefix+'-samples.npz'), Path(prefix+'-definition.json')
    samples = load_npz(samples_path)
    definition = json.loads(definition_path.read_text())
    origin = json.loads(args.source_report.read_text())
    if definition['arrays']['sha256'] != origin['latest_checkpoint']['sha256']:
        raise ValueError('Saved sample definition and original report have different fields')
    for name, value in samples.items():
        if not np.all(np.isfinite(value)):
            raise ValueError('Nonfinite saved sample '+name)
    xi, G, K = samples['xi'], samples['node_G'], samples['node_target_K']
    V, R, c = samples['node_actual'], samples['node_reference'], samples['node_correction']
    retained = int(definition['maximum_mode']) if 'maximum_mode' in definition else 30
    # The actual correction dimension determines retained frequency; it is
    # not inferred from a diagnostic filename or an angular sample count.
    raw = load_npz(definition['arrays']['path'])
    retained = 2*((raw['corrections'].shape[1]-2)//3)
    W = len(xi); stride = W//256
    rank = R[:, 0]*R[:, 2]-R[:, 1]*R[:, 1]
    cross = R[:, 0]*c[:, 2]+R[:, 2]*c[:, 0]-2*R[:, 1]*c[:, 1]
    quadratic = c[:, 0]*c[:, 2]-c[:, 1]*c[:, 1]
    def at(j):
        return dict(angular_index=int(j), xi=xi[j], actual_n_m_l=V[j].tolist(),
            frozen_reference_n_m_l=R[j].tolist(), correction_n_m_l=c[j].tolist(),
            target_K=K[j], G=G[j], reference_rank1_defect=rank[j],
            linear_correction_contribution=cross[j], quadratic_correction_contribution=quadratic[j],
            target_contribution=-K[j])
    node = dict(node=origin['final_locations']['full_gauss']['node'],
        s=origin['final_locations']['full_gauss']['s'], sampled_peak=at(int(np.argmax(abs(G)))),
        original_256_grid_peak=at(stride*int(np.argmax(abs(G[::stride])))),
        actual_minus_reference_minus_correction=maximum(V-R-c),
        decomposition_roundoff=maximum(G-(rank+cross+quadratic-K)),
        sampled_minimum_n=float(np.min(V[:, 0])), sampled_minimum_l=float(np.min(V[:, 2])),
        actual_G_in_low_modes_maximum=maximum(projection(G, retained)),
        actual_G_in_high_modes_maximum=maximum(G-projection(G, retained)))
    rows = []
    for name in ('whole_Gauss2', 'split_Gauss3', 'split_Gauss8'):
        full, corr, lift = [samples[name+'_'+key] for key in
            ('average_codazzi', 'correction_codazzi', 'lifting_codazzi')]
        rows.append(dict(name=name, full=spectrum(full, retained),
            correction=spectrum(corr, retained), lifting=spectrum(lift, retained),
            decomposition_roundoff=maximum(full-corr-lift)))
    g2, g3, g8 = [samples[name+'_average_codazzi'] for name in
        ('whole_Gauss2', 'split_Gauss3', 'split_Gauss8')]
    coarse = spectrum(g2[::stride], retained)
    left, right = samples['cell_endpoints']
    ref = definition['coast_reference_definition']
    e, f = ref['support']; rim = ref['rim_fraction']*(f-e)
    cell = dict(cell=origin['final_locations']['full_angular_codazzi']['n']['cell'],
        endpoints=[left, right], width=right-left, split_point=f-rim,
        original_256_grid=coarse,
        original_report_maxima=[origin['final_locations']['full_angular_codazzi'][key]['maximum'] for key in ('n', 'm')],
        original_report_omitted_maxima=[origin['final_locations']['omitted_angular_codazzi'][key]['maximum'] for key in ('n', 'm')],
        angular_refinement_maximum_change=[rows[0]['full'][j]['sampled_maximum']-coarse[j]['sampled_maximum'] for j in range(2)],
        whole2_vs_split8_maximum=np.max(abs(g2-g8),axis=0).tolist(),
        split3_vs_split8_maximum=np.max(abs(g3-g8),axis=0).tolist(),
        quadrature=rows,
        endpoint_full=spectrum(samples['endpoint_full'],retained),
        endpoint_correction=spectrum(samples['endpoint_correction'],retained),
        endpoint_lifting=spectrum(samples['endpoint_lifting'],retained))
    report = dict(schema='fd2d-actual-atlas-local-GC-decomposition-finalized-v1',
        actual_execution=True, source=identity(__file__), producer_source=receipt['source'],
        producer_exit_receipt=identity(receipt_path), producer_exit_code=1,
        producer_failure='JSON serialization of numpy.longdouble after complete sample/definition saves',
        producer_exit_reinterpreted_as_success=False, field=definition['arrays'],
        source_report=identity(args.source_report), definition=identity(definition_path),
        samples=identity(samples_path), angular_points=W, original_angular_points=256,
        maximum_retained_frequency=retained, gauss_node=node, codazzi_cell=cell,
        finite_scope='One reported worst node and one reported worst cell. Saved samples only; no whole-domain inference.',
        quadrature_scope='Same finite field; full endpoint difference minus fixed-xi Gauss PDE averages. No remainder bound.',
        hypothetical_spectral_projection_is_new_solution=False,
        field_evaluation_repeated=False, source_or_field_modified=False,
        BVP_or_Jacobian_matrix_assembled=False, body_integration_run=False,
        nonlinear_solve_performed=False, continuous_certificate=False,
        finalizer_seconds=time.monotonic()-started,
        finalizer_maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.output.write_text(json.dumps(report,indent=2,allow_nan=False,default=scalar)+'\n')
    print(json.dumps(dict(report=identity(args.output),node=node,
        cell_full=[x['sampled_maximum'] for x in rows[0]['full']],
        split8_full=[x['sampled_maximum'] for x in rows[2]['full']],
        whole2_vs_split8=cell['whole2_vs_split8_maximum'],
        split3_vs_split8=cell['split3_vs_split8_maximum']),default=scalar),flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
