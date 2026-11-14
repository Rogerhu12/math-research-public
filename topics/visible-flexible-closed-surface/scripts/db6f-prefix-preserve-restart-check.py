#!/usr/bin/env python3
"""Check saved-mesh initialization without solving or changing a physical BVP.

Checks exact signed-mode placement, gauge scaling, retained physical nodes,
the explicit inlet adjustment, and rejection of changed physical input.
The numerical checks do not certify any solution of the nonlinear equations.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root', type=Path, required=True)
    p.add_argument('--checkpoint', type=Path, required=True)
    p.add_argument('--linear-port', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    loader = module('restart_check_source', HERE/'db6f-prefix-flat-geometry-source.py')
    helper = module('restart_check_helper', HERE/'db6f-prefix-preserve-restart.py')
    rec, oldobj, oldflow, sol = loader.source(a.checkpoint, a.linear_port, a.source_root)
    rows = []
    oldM = oldobj.M
    for M in (oldM, oldM+2):
        obj = oldobj.__class__(rec['frozen_profile'], oldobj.port,
                               rec['gauge_amplitude'], M, 256, True,
                               rec['warp_reference_q'])
        x, y, par, info = helper.restart(obj, a.checkpoint, rec['chart'])
        s, unused = obj.chart(x, par[0])
        flow = obj.flow(par[0])
        # Only a small set of already existing mesh nodes is needed to test
        # the signed Fourier placement. Retention is checked over every node.
        idx = np.unique(np.r_[0, np.linspace(0, len(x)-1, 43).astype(int), len(x)-1])
        B0 = oldflow.basis(512)[0]
        B1 = flow.basis(512)[0]
        before = oldobj.q*oldflow.values(sol.sol(s[idx]), B0)
        after = obj.q*flow.values(y[:, idx], B1)
        cutoff = (flow.Tu if flow.direction == 'outward' else flow.Td)/2
        whole = float(np.max(np.linalg.norm(after-before, axis=2)))
        outside = s[idx] >= cutoff
        outside_error = float(np.max(np.linalg.norm(after[outside]-before[outside], axis=2)))
        inlet_error = float(np.max(abs(y[:, 0]-obj.initial(par))))
        oldmesh = np.asarray(rec['mesh'])
        pos = np.searchsorted(s, oldmesh)
        nearest = np.minimum(abs(oldmesh-s[np.minimum(pos, len(s)-1)]),
                             abs(oldmesh-s[np.maximum(pos-1, 0)]))
        mesh_error = float(nearest.max())
        saved = obj.cfg
        obj.cfg = dict(saved, delta=saved['delta']+1e-6)
        rejected = False
        try:
            helper.restart(obj, a.checkpoint, rec['chart'])
        except ValueError as e:
            rejected = str(e) == 'Changed fixed-metric restart input: frozen_profile'
        finally:
            obj.cfg = saved
        passed = (outside_error < 3e-15 and inlet_error < 3e-15 and
                  mesh_error < 2e-12 and rejected and
                  whole <= info['inlet_correction_physical_l1']+3e-15)
        rows.append(dict(modes=M, angular=256, passed=bool(passed),
                         physical_mode_padding_error_outside_inlet=outside_error,
                         whole_profile_difference=whole,
                         inlet_coefficient_residual=inlet_error,
                         maximum_physical_saved_node_displacement=mesh_error,
                         changed_metric_rejected=rejected, initializer=info))
    out = dict(scope=__doc__, checkpoint=str(a.checkpoint),
               checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),
               script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               all_passed=all(r['passed'] for r in rows), checks=rows)
    a.out.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(dict(all_passed=out['all_passed'], rows=[{
        k:r[k] for k in ('modes', 'physical_mode_padding_error_outside_inlet',
                        'maximum_physical_saved_node_displacement',
                        'inlet_coefficient_residual', 'changed_metric_rejected')}
        for r in rows])))
    if not out['all_passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
