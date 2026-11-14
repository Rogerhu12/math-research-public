#!/usr/bin/env python3
"""Exact rational point lower for the saved finite prefix at two symmetry axes.

No solver, ODE, source BVP evaluator, or new geometry is run.  This is a lower
bound relative to the *frozen prefix target*.  The future exact-bridge target
and any completed common-cut graph are not claimed to have been constructed.
The reported witness is before the original common-cut correction support.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
import time

import numpy as np


HERE = Path(__file__).resolve().parent
SOURCE_SHA256 = {
    '78718-prefix-storage-v1.py': '83cf59cfe5ab373421e53d0c0d8d2274edfc6a6b266fc2ab6161274b474a4329',
    '78718-prefix-byte-shards-v1.py': 'e23153ae6b364854a24acc464be97921b134f7e25024e82c8c91995ca2f96f39',
    '78718-prefix-continuous-hermite-storage-v1.py': '09e8c748c7cc49347876d849029e835a8cd0e5f097d36eaf6cf2fd7c0f2ddc18',
    '78718-prefix-common-cut-storage-v1.py': '34b0b92c6f4d92bd497f3d84d28cbd73cb29271e36b240d3a19795987f057d43',
    '78718-prefix-metric-polynomial-storage-v1.py': 'd290543f75224509fef8287db838265540a74b7caec38d7b9f34cea563d8359e',
    '78718-prefix-metric-supplier-storage-v1.py': 'f2d8e79504a2a3895ec8705457eabe46321e80b68b8e7c7de11f13015d160ff3',
}
BUDGET = Q(1, 500_000_000)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def identity(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return {'file': str(path), 'bytes': len(raw),
            'sha256': hashlib.sha256(raw).hexdigest()}


def rational_bounds(value):
    """Both binary64 endpoints provably enclose an exact Fraction."""
    mid = float(value)
    require(math.isfinite(mid), 'Unbounded displayed scalar')
    qmid = Q.from_float(mid)
    lo = math.nextafter(mid, -math.inf) if qmid > value else mid
    hi = math.nextafter(mid, math.inf) if qmid < value else mid
    require(Q.from_float(lo) <= value <= Q.from_float(hi), 'Bad display enclosure')
    return {'exact': str(value), 'lower': lo, 'upper': hi}


def nodal_axis(jets, node, modes, alternating):
    # Mode layout of the exact shared-jet map, not a sampled polar derivative.
    # R = r0 + sum r_j cos(3j psi), T = sum t_j sin(3j psi),
    # Z = z0 + sum z_j cos(3j psi).  At psi=0 or pi/3, T_s=0.
    row = jets[1, node]
    rs = Q.from_float(float(row[0]))
    zs = Q.from_float(float(row[-1]))
    for j in range(1, modes+1):
        sign = -1 if alternating and j % 2 else 1
        rs += sign * Q.from_float(float(row[j]))
        zs += sign * Q.from_float(float(row[2*modes+j]))
    E = rs*rs + zs*zs
    signed = E-1
    return {'node': node, 'axis': 'pi/3' if alternating else '0',
            'rs': rs, 'zs': zs, 'E': E, 'signed': signed, 'absolute': abs(signed)}


def run(args):
    started = time.monotonic()
    require(not args.out.exists(), 'Refuse to replace an existing point report')
    sources = []
    for name, expected in SOURCE_SHA256.items():
        rec = identity(HERE/name)
        require(rec['sha256'] == expected, 'Frozen source differs: '+name)
        sources.append(rec)
    spec = importlib.util.spec_from_file_location('nodal_lower_storage', HERE/'78718-prefix-storage-v1.py')
    storage = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(storage)
    geometry, payload, storage_bindings = storage.read_payload(args.geometry, verify_arrays=True)
    geometry_id, target_id, metric_id = [identity(p) for p in
                                         (args.geometry, args.target, args.metric_certificate)]
    target = json.loads(args.target.read_text())
    metric = json.loads(args.metric_certificate.read_text())
    require(geometry.get('mirror_inlet_C2_exact') is True and geometry.get('ell') == 0.,
            'Expected the already generated mirror prefix')
    require(target.get('geometry_sha256') == geometry_id['sha256'], 'Target geometry differs')
    require(target.get('script_sha256') == SOURCE_SHA256['78718-prefix-metric-supplier-storage-v1.py'],
            'Frozen target supplier differs')
    require(metric.get('geometry_sha256') == geometry_id['sha256'] and
            metric.get('target_sha256') == target_id['sha256'], 'Metric input identities differ')
    require(metric.get('script_sha256') == SOURCE_SHA256['78718-prefix-metric-polynomial-storage-v1.py'] and
            metric.get('entire_prefix_covered') is True, 'Expected the full frozen metric report')
    with np.load(io.BytesIO(gzip.decompress(payload)), allow_pickle=False) as raw:
        mesh = raw['mesh']
        jets = raw['jets']
        increments = raw['mean_increments']
    M, N = geometry['modes'], geometry['nodes']
    require(type(M) is int and M > 0 and type(N) is int and N >= 3, 'Bad geometry dimensions')
    require(mesh.shape == (N,) and jets.shape == (3,N,3*M+2) and increments.shape == (N-1,),
            'Unexpected exact-Hermite array layout')
    require(np.isfinite(mesh).all() and np.isfinite(jets).all() and np.isfinite(increments).all(),
            'Nonfinite defining coefficients')
    require(np.all(np.diff(mesh)>0), 'Non-increasing geometry mesh')
    # Exactly the original common-cut make() expression; no replacement
    # continuum subtraction or new correction width is used.
    width = .15
    correction_start = int(np.searchsorted(mesh, mesh[-1]-width))
    require(1 < correction_start < N-1, 'No interior nodes before the correction support')
    worst = None
    checked = 0
    for node in range(1, correction_start):
        for alternating in (False, True):
            value = nodal_axis(jets, node, M, alternating)
            checked += 1
            if worst is None or value['absolute'] > worst['absolute']:
                worst = value
    require(worst is not None and worst['node'] < correction_start, 'No unaffected witness')
    witness = {'native_node_index': worst['node'], 'psi_exact': worst['axis'],
        's': rational_bounds(Q.from_float(float(mesh[worst['node']]))),
        'radial_s_derivative': rational_bounds(worst['rs']),
        'height_s_derivative': rational_bounds(worst['zs']),
        'tangential_s_derivative_exact': '0',
        'metric_ss': rational_bounds(worst['E']),
        'frozen_target_metric_ss_exact': '1',
        'signed_metric_ss_difference': rational_bounds(worst['signed']),
        'relative_metric_operator_lower': rational_bounds(worst['absolute'])}
    inputs = [geometry_id, target_id, metric_id, *storage_bindings]
    report = {'schema': '78718-prefix-nodal-axis-exact-lower-v1',
        'status': 'EXACT_FROZEN_PREFIX_POINT_LOWER_COMPUTED',
        'script': identity(__file__), 'source_bindings': sources,
        'input_bindings': list({rec['file']: rec for rec in inputs}.values()),
        'modes': M, 'nodes': N, 'exact_point_evaluations': checked,
        'witness': witness, 'original_budget_exact': str(BUDGET),
        'exceeds_original_budget_relative_to_frozen_prefix_target': worst['absolute'] > BUDGET,
        'common_cut_support': {'source': str(HERE/'78718-prefix-common-cut-storage-v1.py'),
            'width_float_hex': width.hex(), 'start_index': correction_start,
            'start_s': rational_bounds(Q.from_float(float(mesh[correction_start]))),
            'witness_strictly_before_support': True,
            'statement': 'The prescribed width=.15 common-cut correction is identically zero here if that graph is constructed from this base; its construction is not claimed.'},
        'proof_scope': {'finite_shared_jet_map': True, 'frozen_prefix_target': True,
            'point_rayleigh_lower_only': True, 'new_exact_bridge_target_transfer': False,
            'actual_common_cut_generated_by_this_program': False,
            'complete_closed_graph_rejection': False,
            'exact_infinite_isometry_rejection': False},
        'solver_calls': 0, 'new_ode_calls': 0, 'geometry_producer_calls': 0,
        'seconds': time.monotonic()-started}
    # A source or input change during this read-only computation invalidates it.
    for rec in [report['script'], *sources, *report['input_bindings']]:
        require(identity(rec['file']) == rec, 'Input/source changed during exact point computation')
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'status': report['status'], 'output': identity(args.out),
        'checked_points': checked, 'witness_node': worst['node'], 'witness_axis': worst['axis'],
        'metric_operator_lower': witness['relative_metric_operator_lower']['lower'],
        'exceeds_frozen_target_budget': report['exceeds_original_budget_relative_to_frozen_prefix_target'],
        'new_exact_bridge_transfer': False, 'solver_calls': 0}, sort_keys=True))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--geometry', type=Path, required=True)
    p.add_argument('--target', type=Path, required=True)
    p.add_argument('--metric-certificate', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    run(p.parse_args())


if __name__ == '__main__':
    main()
