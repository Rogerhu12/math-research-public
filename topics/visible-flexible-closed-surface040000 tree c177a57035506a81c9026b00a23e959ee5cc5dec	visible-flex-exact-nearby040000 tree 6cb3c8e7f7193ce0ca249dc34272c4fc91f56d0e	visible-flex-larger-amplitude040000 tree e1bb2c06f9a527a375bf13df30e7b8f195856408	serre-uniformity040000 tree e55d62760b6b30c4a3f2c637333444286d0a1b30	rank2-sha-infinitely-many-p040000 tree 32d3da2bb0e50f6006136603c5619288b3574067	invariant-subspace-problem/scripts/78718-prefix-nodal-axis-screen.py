#!/usr/bin/env python3
"""Exact necessary-condition screen of an actual finite mirror prefix.

At psi=0 or pi/3 the frozen target ds^2+a(s)^2 dTheta^2 has g_ss=1.
The actual shared nodal one-jet supplies R_s and Z_s as binary rationals.
This does not construct or transfer to the later exact-bridge/common map.
No prior continuous metric certificate, solver or ODE is needed.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
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
BUDGET = Fraction(1, 500_000_000)


def identity(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {'file': str(path), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def require(condition, message):
    if not condition:
        raise ValueError(message)


def decimal_floor(value, digits=24):
    """An exact decimal rational floor, not a float's roundtrip string."""
    scale = 10**digits
    integer = value.numerator*scale // value.denominator
    lower = Fraction(integer, scale)
    require(lower <= value < lower+Fraction(1, scale), 'Invalid decimal floor')
    sign = '-' if integer < 0 else ''
    whole, remainder = divmod(abs(integer), scale)
    return {'digits_after_point': digits,
            'exact': str(lower),
            'decimal': f'{sign}{whole}.{remainder:0{digits}d}'}


def run(args):
    begin = time.monotonic()
    require(not args.out.exists(), 'Refuse to replace a prior screen')
    require(math.isfinite(args.correction_width) and args.correction_width > 0,
            'Correction width must be finite and positive')
    source_paths = [HERE/'78718-prefix-nodal-axis-lower-v1.py',
                    HERE/'78718-prefix-storage-v1.py',
                    HERE/'78718-prefix-byte-shards-v1.py',
                    HERE/'78718-prefix-common-cut-storage-v1.py']
    sources = [identity(p) for p in source_paths]
    axis = module('actual_axis_exact_algebra', source_paths[0])
    storage = module('actual_axis_storage_reader', source_paths[1])
    geometry, payload, bindings = storage.read_payload(args.geometry, verify_arrays=True)
    geometry_id = identity(args.geometry)
    require(geometry.get('mirror_inlet_C2_exact') is True and geometry.get('ell') == 0,
            'This screen expects the actual ell=0 shared-jet mirror prefix')
    require(geometry.get('frozen_profile', {}).get('ramp_law') == 'flat'
            and isinstance(geometry.get('chart'), dict)
            and math.isfinite(geometry.get('warp_reference_q', math.nan)),
            'Missing fixed flat-profile/chart target identity')
    with np.load(io.BytesIO(gzip.decompress(payload)), allow_pickle=False) as saved:
        mesh = saved['mesh']
        jets = saved['jets']
        increments = saved['mean_increments']
    modes, nodes = geometry['modes'], geometry['nodes']
    require(type(modes) is int and modes > 0 and type(nodes) is int and nodes >= 3,
            'Invalid finite representation dimensions')
    require(mesh.shape == (nodes,) and jets.shape == (3, nodes, 3*modes+2)
            and increments.shape == (nodes-1,), 'Unexpected shared-jet layout')
    require(all(a.dtype.kind == 'f' and a.dtype.itemsize == 8
                and np.isfinite(a).all() for a in (mesh, jets, increments)),
            'Defining values must be finite binary64 arrays')
    require(np.all(np.diff(mesh) > 0), 'Non-increasing physical mesh')
    # Same binary operation as the prescribed common-cut producer. The
    # assertion about its support is conditional until that map is produced.
    start = int(np.searchsorted(mesh, mesh[-1]-args.correction_width))
    require(1 < start < nodes-1, 'No nontrivial unaffected interior region')
    worst = None
    checked = 0
    for node in range(1, start):
        for alternating in (False, True):
            value = axis.nodal_axis(jets, node, modes, alternating)
            if worst is None or value['absolute'] > worst['absolute']:
                worst = value
            checked += 1
    require(worst is not None, 'No exact point was evaluated')
    witness = {
        'native_node_index': worst['node'], 'psi_exact': worst['axis'],
        's': axis.rational_bounds(Fraction.from_float(float(mesh[worst['node']]))),
        'radial_s_derivative': axis.rational_bounds(worst['rs']),
        'height_s_derivative': axis.rational_bounds(worst['zs']),
        'tangential_s_derivative_exact': '0',
        'frozen_target_metric_ss_exact': '1',
        'metric_ss': axis.rational_bounds(worst['E']),
        'signed_metric_ss_difference': axis.rational_bounds(worst['signed']),
        'relative_metric_operator_lower': axis.rational_bounds(worst['absolute']),
        'safe_decimal_lower': decimal_floor(worst['absolute'])}
    report = {
        'schema': '78718-actual-prefix-nodal-axis-screen-v1',
        'status': 'EXACT_FROZEN_PREFIX_POINT_LOWER_COMPUTED',
        'script': identity(__file__), 'source_bindings': sources,
        'input_bindings': [geometry_id, *bindings],
        'checkpoint_identity_in_geometry': {
            'file': geometry['checkpoint'], 'sha256': geometry['checkpoint_sha256']},
        'modes': modes, 'nodes': nodes, 'exact_point_evaluations': checked,
        'witness': witness, 'original_budget_exact': str(BUDGET),
        'exceeds_original_budget_relative_to_frozen_prefix_target':
            worst['absolute'] > BUDGET,
        'target_definition': 'The frozen prefix metric ds^2+a(s)^2 dTheta^2, '
            'Theta=psi-e(s)*sin(3 psi)/3, from this geometry metadata. '
            'At either selected axis Theta_s=0 and g_ss=1 exactly.',
        'conditional_common_cut_support': {
            'width_binary64_hex': args.correction_width.hex(),
            'start_index': start,
            'witness_strictly_before_support': worst['node'] < start,
            'statement': 'If the prescribed common-cut construction uses this '
                'base and this width, its added jet correction is zero at the '
                'witness. Its target radial scaling still needs separate treatment.'},
        'scope': {
            'actual_saved_finite_prefix': True,
            'frozen_prefix_target_only': True,
            'continuous_metric_certificate_required': False,
            'new_exact_bridge_target_transfer': False,
            'actual_common_cut_constructed': False,
            'complete_closed_graph_rejection': False,
            'solver_success_asserted': False},
        'solver_calls': 0, 'new_ode_calls': 0, 'geometry_producer_calls': 0,
        'seconds': time.monotonic()-begin}
    # Concurrent replacement of a closed input would invalidate its identity.
    for record in [report['script'], *sources, *report['input_bindings']]:
        require(identity(record['file']) == record, 'Closed input/source changed')
    with args.out.open('x') as handle:
        json.dump(report, handle, indent=2, sort_keys=True)
        handle.write('\n')
    print(json.dumps({'status': report['status'], 'output': identity(args.out),
        'checked_points': checked, 'witness_node': worst['node'],
        'witness_axis': worst['axis'],
        'safe_exact_decimal_lower': witness['safe_decimal_lower']['decimal'],
        'exceeds_frozen_target_budget': report[
            'exceeds_original_budget_relative_to_frozen_prefix_target'],
        'new_exact_bridge_transfer': False, 'solver_calls': 0}, sort_keys=True))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--geometry', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--correction-width', type=float, default=.15)
    run(parser.parse_args())


if __name__ == '__main__':
    main()
