#!/usr/bin/env python3
"""Exercise snapshot storage using a 64-node fixture of an existing warm curve.

The fixture is not an inner solve: a cubic Hermite interpolant is constructed
on a subset of the saved warm mesh. No BVP, tail call or integration is run.
The test checks byte preservation, ordinary geometry-reader consumption and
that the live fixture object's caches and counters are unchanged by saving.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import time
from types import SimpleNamespace

import numpy as np
from scipy.interpolate import CubicHermiteSpline

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def identity(path):
    path = Path(path).resolve()
    return {'path': str(path), 'bytes': path.stat().st_size,
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint', type=Path, required=True)
    parser.add_argument('--fixture-directory', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists() or args.fixture_directory.exists():
        raise FileExistsError('Use a new fixture directory and report')
    args.fixture_directory.mkdir()
    begin = time.monotonic()
    loader = module('snapshot_fixture_source', HERE/'db6f-prefix-flat-geometry-source.py')
    snapshots = module('snapshot_fixture_writer', HERE/'78718-prefix-inner-snapshot.py')
    port = TOPIC/'notes/2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json'
    source_root = TOPIC/'repro/source-root'
    rec, obj, flow, saved = loader.source(args.checkpoint, port, source_root)
    # The production runner installs this field; the read-only geometry
    # loader intentionally does not. Match the production object's metadata.
    obj.port['_sha256'] = identity(port)['sha256']
    from curve_stable_prefix_bvp import load_checkpoint
    indices = np.unique(np.linspace(0, len(saved.x)-1, 64).astype(int))
    s = saved.x[indices]
    p = saved.p.copy()
    t = obj.inverse_chart(s, p[0])
    # This explicit test object is not represented as a returned solve.
    y = saved.sol(s)
    dy_t = obj.fun(t, y, p)
    cubic = CubicHermiteSpline(t, y, dy_t, axis=1)
    fixture = SimpleNamespace(x=t, y=y, p=p, sol=cubic, success=False, status=1,
        message='SYNTHETIC STORAGE FIXTURE; no solver executed',
        rms_residuals=np.array([1.]))
    solver_record = {'scope': 'Synthetic storage fixture; residual 1 is a marker, not a computed residual.',
                     'original_tol': 2e-9, 'original_bc_tol': 1e-8}
    physical = SimpleNamespace(x=obj.chart(t, p[0])[0], y=y, p=p)
    expected = flow.c2_interpolant(physical)
    before = {'calls': flow.calls, 'core_key': obj._core_key,
              'support_amplitude': obj.support_amplitude,
              'flow_id': id(obj.fixed_flow), 'core_id': id(obj._core),
              'initial_id': id(obj._initial), 'initial_jac_id': id(obj._initial_jac),
              'pscale': obj.pscale.tobytes(), 'initial': obj._initial.tobytes()}
    snapshot = snapshots.save_inner_candidate(obj, fixture,
        prefix=args.fixture_directory/'synthetic', number=1, chart=rec['chart'],
        tail_config={'scope': 'Synthetic storage fixture; no tail engine'},
        tail_modes=obj.M, input_restart=identity(args.checkpoint), preceding_tail=None,
        solver_record=solver_record)
    after = {'calls': flow.calls, 'core_key': obj._core_key,
             'support_amplitude': obj.support_amplitude,
             'flow_id': id(obj.fixed_flow), 'core_id': id(obj._core),
             'initial_id': id(obj._initial), 'initial_jac_id': id(obj._initial_jac),
             'pscale': obj.pscale.tobytes(), 'initial': obj._initial.tobytes()}
    cp = Path(snapshot['physical_candidate']['path'])
    actual = load_checkpoint(cp)
    returned = load_checkpoint(snapshot['returned_collocation']['path'])
    nodes = []
    for row in actual['nodal_state_chunks']:
        with gzip.open(cp.parent/row['file'], 'rb') as stream:
            nodes.append(np.load(stream, allow_pickle=False))
    nodes = np.concatenate(nodes, axis=0)
    _, _, _, ordinary = loader.source(cp, port, source_root)
    checks = {
        'live_fixture_object_unchanged': before == after,
        'returned_cubic_bytes_identical': returned['pp_coefficients'].tobytes() == cubic.c.tobytes(),
        'returned_nodal_bytes_identical': nodes.tobytes() == y.tobytes(),
        'physical_quintic_bytes_identical_to_original_formula': actual['pp_coefficients'].tobytes() == expected.c.tobytes(),
        'returned_parameters_equal': returned['parameters'] == p.tolist(),
        'returned_numerical_mesh_equal': returned['mesh'] == t.tolist(),
        'physical_mesh_equal': actual['mesh'] == physical.x.tolist(),
        'ordinary_geometry_reader_retains_pp_bytes': ordinary.sol.c.tobytes() == expected.c.tobytes(),
        'success_never_asserted': all(actual[name] is False for name in
            ('solver_success', 'finite_coupled_success', 'closed_surface_success', 'outer_true_boundary_checked')),
        'no_tail_seam_claim': 'tail_seam' not in actual,
        'file_size_limit': max(row['bytes'] for row in snapshot['closed_files']) < 5_000_000}
    if not all(checks.values()):
        raise AssertionError(checks)
    report = {'scope': __doc__, 'checks': checks, 'fixture_nodes': len(t),
        'fixture_is_actual_inner_run': False, 'source_checkpoint': identity(args.checkpoint),
        'script': identity(__file__), 'snapshot_writer': identity(HERE/'78718-prefix-inner-snapshot.py'),
        'snapshot': snapshot, 'BVP_calls': 0, 'DN_calls': 0,
        'seconds': time.monotonic()-begin}
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'report': identity(args.out), 'checks_passed': len(checks),
        'fixture_nodes': len(t), 'BVP_calls': 0, 'DN_calls': 0,
        'fixture_is_actual_inner_run': False, 'seconds': report['seconds']}), flush=True)


if __name__ == '__main__':
    main()
