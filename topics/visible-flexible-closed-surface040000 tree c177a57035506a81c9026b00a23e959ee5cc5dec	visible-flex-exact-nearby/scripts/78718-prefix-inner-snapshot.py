#!/usr/bin/env python3
"""Preserve a returned inner BVP without asserting outer or surface success.

The numerical-t cubic is copied exactly from the returned unweighted result.
A separate physical-s quintic uses the same C2 construction as the original
final exporter, evaluated by a new Flow instance. Neither object is a true
nonlinear-tail solution merely because its inner BVP succeeded.
"""
import copy
import gzip
import hashlib
import math
from pathlib import Path
import time
from types import SimpleNamespace

import numpy as np


def identity(path):
    path = Path(path).resolve()
    return {'path': str(path), 'bytes': path.stat().st_size,
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def _closed_files(path, record):
    paths = [Path(path)]
    paths.extend(Path(path).parent/part['file']
                 for part in record.get('pp_coefficient_chunks', []))
    result = [identity(p) for p in paths]
    if any(row['bytes'] >= 5_000_000 for row in result):
        raise ValueError('Inner snapshot file reached the 5 MB limit')
    return result


def _save_nodes(prefix, y):
    """Retain the returned nodal values without an endpoint evaluation roundoff."""
    block = max(1, 4_400_000//(y.shape[1]*y.dtype.itemsize))
    rows = []
    for index, first in enumerate(range(0, y.shape[0], block)):
        last = min(first+block, y.shape[0])
        path = Path(str(prefix)+f'-nodes-{index:02d}.npy.gz')
        with path.open('xb') as raw:
            with gzip.GzipFile(fileobj=raw, mode='wb', compresslevel=6, mtime=0) as stream:
                np.save(stream, y[first:last], allow_pickle=False)
        row = identity(path)
        if row['bytes'] >= 5_000_000:
            raise ValueError('Nodal snapshot file reached the 5 MB limit')
        rows.append({'file': path.name, 'state_first': first,
                     'state_last_exclusive': last, **row})
    return rows


def save_inner_candidate(obj, result, *, prefix, number, chart, tail_config,
                         tail_modes, input_restart, preceding_tail, solver_record):
    """Observation only: no BC, initial-core evaluation, integration or DN call.

    The caller catches storage/domain errors and continues its original outer
    algorithm. Successfully closed files remain available even if a later
    snapshot component fails. Only the fixed-g path is supported here.
    """
    from curve_stable_prefix_bvp import save_checkpoint

    begin = time.monotonic()
    if obj.fixed is not True:
        raise ValueError('This snapshot helper records the fixed-g path only')
    prefix = Path(str(prefix)+f'_inner_{number:04d}').resolve()
    if list(prefix.parent.glob(prefix.name+'*')):
        raise FileExistsError('Inner snapshot prefix already exists')
    x, y, p = (np.asarray(result.x), np.asarray(result.y), np.asarray(result.p))
    if (result.sol.axis != 1 or result.sol.c.shape != (4, len(x)-1, obj.n)
            or y.shape != (obj.n, len(x)) or not np.array_equal(result.sol.x, x)):
        raise ValueError('Unexpected returned physical-state collocation layout')
    if not all(np.all(np.isfinite(v)) for v in (x, y, p, result.sol.c)):
        raise ValueError('Returned inner candidate has nonfinite values')

    nodal = _save_nodes(prefix, y)
    origin = {'run_prefix': str(prefix).rsplit('_inner_', 1)[0],
              'inner_call': int(number), 'input_restart': input_restart,
              'preceding_true_tail_packet': preceding_tail,
              'preceding_tail_is_not_a_candidate_seam': True,
              'snapshot_source': identity(__file__)}
    flags = {'status': 'UNSOLVED_OUTER_INNER_CANDIDATE',
             'solver_success': False, 'finite_coupled_success': False,
             'closed_surface_success': False,
             'inner_success': bool(result.success),
             'inner_message': str(result.message),
             'inner_solver_status': int(result.status),
             'outer_true_boundary_checked': False,
             'inner_physical_rms_max': float(np.max(result.rms_residuals)),
             'inner_spectral_coordinate_audit': copy.deepcopy(solver_record),
             'snapshot_origin': origin}
    cubic_path = Path(str(prefix)+'-collocation.json.gz')
    cubic = {**flags,
        'scope': 'Exact returned physical-state cubic in numerical t. This is not a physical-s geometry checkpoint.',
        'mesh_coordinate': 'numerical_t', 'state_coordinates': 'unweighted_physical_coefficients',
        'mesh': x.tolist(), 'parameters': p.tolist(), 'nodes': len(x),
        'pp_coefficients': result.sol.c, 'nodal_state_chunks': nodal}
    saved_cubic = save_checkpoint(cubic_path, cubic)
    cubic_files = _closed_files(cubic_path, saved_cubic)

    # Fixed obj.chart reads its existing fixed_flow; it does not change its
    # cache. All RHS/C2 evaluations below instead use an independent Flow,
    # including an independent bridge. The live initial-core cache is unused.
    physical_x = obj.chart(x, p[0])[0]
    flow = obj.Flow(copy.deepcopy(obj.cfg), copy.deepcopy(obj.port),
                    obj.M, obj.q, obj.nt, obj.base_mode)
    physical = SimpleNamespace(x=physical_x, y=y, p=p)
    physical.sol = flow.c2_interpolant(physical)
    record = {**flags,
        'scope': 'Physical-s C2 Hermite candidate from a returned inner BVP. The true nonlinear outer BC and seam are unsolved; no metric certificate is asserted.',
        'angular_chart': 'frozen-spline-adaptive-v1', 'chart': copy.deepcopy(chart),
        'warp_reference_q': obj.warp_q,
        'config': {'modes': obj.M, 'tail_modes': int(tail_modes), 'base_mode': obj.base_mode,
                   'core_kind': 'adaptive_warped_support', 'angular': obj.nt,
                   'tol': float(solver_record['original_tol']),
                   'bc_tol': float(solver_record['original_bc_tol']),
                   'physical_bc_tol': 2e-11, 'fixed_metric': True,
                   'actual_nonlinear_tail': False},
        'frozen_profile': copy.deepcopy(obj.cfg), 'gauge_amplitude': obj.q,
        'actual_primary_amplitude': obj.seed_support_amplitude*math.exp(float(p[0])),
        'meridian_length': flow.end, 'physical_port_sha256': obj.port['_sha256'],
        'physical_tail_parameters': copy.deepcopy(obj.port['parameters']),
        'physical_tail_cut': copy.deepcopy(obj.port['cut']),
        'tail_config': copy.deepcopy(tail_config),
        'parameters': p.tolist(), 'central_correction_scales': obj.pscale.tolist(),
        'nodes': len(x), 'message': 'UNSOLVED OUTER; '+str(result.message),
        'max_rms_collocation_residual': float(np.max(result.rms_residuals)),
        'mesh': physical_x.tolist(), 'pp_coefficients': physical.sol.c,
        'nodal_state_chunks': nodal, 'returned_collocation': identity(cubic_path),
        'interpolant_scope': 'Same physical-s quintic formula as the original final output, not a claim that the numerical-t cubic is unchanged under reparametrization.',
        'snapshot_rhs_calls_on_separate_flow': int(flow.calls)}
    physical_path = Path(str(prefix)+'.json.gz')
    saved_physical = save_checkpoint(physical_path, record)
    physical_files = _closed_files(physical_path, saved_physical)
    return {'status': flags['status'], 'inner_call': number,
            'inner_success': bool(result.success),
            'physical_candidate': identity(physical_path),
            'returned_collocation': identity(cubic_path),
            'closed_files': physical_files+cubic_files+
                [{key: row[key] for key in ('path', 'bytes', 'sha256')} for row in nodal],
            'seconds': time.monotonic()-begin,
            'snapshot_rhs_calls_on_separate_flow': int(flow.calls),
            'new_BVP_calls': 0, 'new_DN_calls': 0,
            'finite_coupled_success': False, 'closed_surface_success': False}
