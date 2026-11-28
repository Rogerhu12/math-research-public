#!/usr/bin/env python3
"""Raise M in a genuine complete unaccepted checkpoint, without promotion.

Reuse the original full three-block Fourier embedding and exact inlet-lift
identity at the source lambda. No accepted-source validator is weakened; this
separate operation consumes an explicitly unaccepted before-J checkpoint.
Only a Newton initial guess is emitted. Any subsequent change of lambda is a
new original BVP and must pass every original numerical and physical gate.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '2'

import argparse
import gc
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'source-run', 'checkpoint-metadata', 'port', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--modes', type=int, required=True)
    parser.add_argument('--angular', type=int, required=True)
    parser.add_argument('--check-angular', type=int, default=2048)
    parser.add_argument('--radial-block', type=int, default=8)
    args = parser.parse_args()
    repo, out = args.repo.resolve(), args.outdir.resolve()
    if out == repo or repo in out.parents or args.radial_block < 1:
        raise ValueError('Scratch output and positive radial blocks are required')
    source_bytes = args.source_run.read_bytes()
    meta_bytes = args.checkpoint_metadata.read_bytes()
    record, metadata = json.loads(source_bytes), json.loads(meta_bytes)
    old_m, new_m = int(record['modes']), args.modes
    raw = args.checkpoint_metadata.resolve().parent/metadata['file']
    if (metadata.get('kind') != 'unaccepted_complete_nodal_restart'
            or metadata.get('accepted_bvp') is not False
            or metadata.get('before_full_J_assembly') is not True
            or sha(raw) != metadata['sha256'] or new_m <= old_m
            or args.angular < max(record['angular'], 32*new_m)):
        raise ValueError('Require a genuine full unaccepted checkpoint and an actual mode raise')
    for group in (record['source_hashes'], record['inputs'], metadata['original_source_hashes']):
        for filename, expected in group.items():
            if sha(filename) != expected:
                raise ValueError('Original source/input changed: '+filename)
    builder_path = HERE.parent/'analytic/check_unaccepted_design_delta_nodes_v2.py'
    transfer_path = SCRIPTS/'resume_m3/prepare_lifted_mode_restart.py'
    builder = module('_unaccepted_lift_original_model', builder_path)
    transfer = module('_unaccepted_complete_original_transfer', transfer_path)
    out.mkdir(parents=True, exist_ok=False)
    (out/'source-run-snapshot.json').write_bytes(source_bytes)
    (out/'checkpoint-metadata-snapshot.json').write_bytes(meta_bytes)
    started = time.monotonic()
    old, table_stats, branch = builder.build_original_model(record, repo)
    port = json.loads(args.port.read_text())
    port['cut']['_prefix_bridge'] = old.cfg['prefix_bridge']
    port['_sha256'] = sha(args.port)
    if (port['parameters'] != record['physical_tail_parameters']
            or port['cut'] != record['physical_tail_cut']
            or len(port['linearSlope']) < new_m
            or port['linearSlope'][:old_m] != old.port['linearSlope'][:old_m]):
        raise ValueError('The enlarged original port changed a physical input or old slope')
    new = type(old)(old.cfg, port, old.q, new_m, args.angular, False, record['warp_reference'])
    new.bcweights = np.full(new_m, record['gates']['physical_bc_tol']/record['gates']['bc_tol'])
    with np.load(raw, allow_pickle=False) as saved:
        x, y0, p0, scale0 = (saved[k].copy() for k in ('x', 'y', 'p', 'pscale'))
    if (x.shape != (metadata['nodes'],) or y0.shape != (old.n, len(x))
            or p0.shape != (old_m,) or not np.array_equal(scale0, old.pscale)
            or not all(np.isfinite(v).all() for v in (x, y0, p0, scale0))
            or not (np.diff(x) > 0).all() or x[0] != 0 or x[-1] != 1):
        raise ValueError('The complete old nodal state or coordinates differ')
    p1 = np.zeros(new_m)
    p1[0] = p0[0]
    p1[1:old_m] = p0[1:]*old.pscale/new.pscale[:old_m-1]
    i0, i1 = old.initial(p0).copy(), new.initial(p1).copy()
    f0, f1 = old.flow(p0[0]), new.flow(p1[0])
    s, ds = old.chart(x, p0[0])
    sn, dsn = new.chart(x, p1[0])
    if not np.array_equal(s, sn) or not np.array_equal(ds, dsn):
        raise ValueError('The meridian chart changed during the reference transfer')
    difference = i1-transfer.embed(i0, old_m, new_m)
    weight, _, _ = transfer.lift_weights(f1, s)
    y1 = transfer.embed(y0, old_m, new_m)+weight[None, :]*difference[:, None]
    N = max(args.check_angular, 32*(3*new_m+1))
    B0, D0, DD0 = f0.basis(N)
    B1, D1, DD1 = f1.basis(N)
    checks = dict(position=0., psi=0., psi_psi=0., rho=0.)
    for first in range(0, len(s), args.radial_block):
        sl = slice(first, first+args.radial_block)
        g0, g1 = f0.geo(s[sl], N), f1.geo(s[sl], N)
        checks['rho'] = max(checks['rho'], float(np.max(np.abs(g0['rho']-g1['rho']))))
        for name, key, left, right in (('position', 'pos', B0, B1),
                ('psi', 'p1', D0, D1), ('psi_psi', 'p2', DD0, DD1)):
            delta = g1[key]+old.q*f1.values(y1[:, sl], right)-g0[key]-old.q*f0.values(y0[:, sl], left)
            checks[name] = max(checks[name], float(np.max(np.linalg.norm(delta, axis=2))))
        del g0, g1, delta
        gc.collect()
    if max(checks.values()) > 1e-7 or not np.isfinite(y1).all():
        raise FloatingPointError('The original nodal reference identity failed: '+str(checks))
    target = out/'initial.npz'
    np.savez_compressed(target, x=x, y=y1, p=p1, pscale=new.pscale)
    report = dict(kind='unaccepted_complete_nodal_mode_lift',
        status='unaccepted_complete_nodal_mode_lift_ready', scope=__doc__,
        actual_command=list(sys.argv), source_run=str(args.source_run.resolve()),
        source_run_sha256=hashlib.sha256(source_bytes).hexdigest(),
        checkpoint_metadata=str(args.checkpoint_metadata.resolve()),
        checkpoint_metadata_sha256=hashlib.sha256(meta_bytes).hexdigest(),
        raw_source=str(raw), raw_source_sha256=sha(raw), source_checkpoint=metadata,
        source_is_accepted_original=False, source_lambda=record['core_settings']['homotopy'],
        core_settings_changed=False, exact_lift_coefficient=1,
        modes=[old_m, new_m], angular=args.angular, nodes=len(x),
        source_physical_controls=(p0[1:]*old.pscale).tolist(),
        output_physical_controls=(p1[1:]*new.pscale).tolist(),
        physical_control_roundtrip_max=float(np.max(np.abs(p0[1:]*old.pscale-p1[1:old_m]*new.pscale[:old_m-1]))),
        all_source_nodes_preserved=True, meridian_chart_bitwise_unchanged=True,
        all_three_state_blocks_retained=True, additive_delta_unchanged=bool(p1[0] == p0[0]),
        original_nodal_reference_checks=checks, check_radial_nodes=len(s), check_angular=N,
        meridian_two_jets_checked=False, no_physical_cubic_was_supplied=True,
        no_new_interpolant_identity_claimed=True, original_model_branch=branch,
        source_hashes={str(p.resolve()):sha(p) for p in (Path(__file__), builder_path, transfer_path)},
        target_port=str(args.port.resolve()), target_port_sha256=sha(args.port),
        result=dict(initial_raw=str(target), initial_raw_sha256=sha(target)),
        seconds=time.monotonic()-started, maximum_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        full_J_assembled=False, nonlinear_solver_invoked=False,
        accepted_BVP_claimed=False, all_terminal_gates_still_unpaid=True, complete_surface=False)
    dest = out/'transfer.json'
    dest.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(status=report['status'], report=str(dest), report_sha256=sha(dest),
        result=report['result'], checks=checks, nodes=len(x), modes=[old_m, new_m],
        seconds=report['seconds'], maximum_RSS_KiB=report['maximum_RSS_KiB'])), flush=True)


if __name__ == '__main__':
    main()
