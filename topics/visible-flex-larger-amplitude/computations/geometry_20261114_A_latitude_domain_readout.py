#!/usr/bin/env python3
"""Read latitude shape/domain diagnostics from A's original physical quintic.

No ODE, Newton, new interpolation, or changed metric is computed here. All
reported extrema are samples, used to plan the large-core connection.
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
import numpy as np


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--runtime-topic', type=Path, required=True)
    p.add_argument('--source-topic', type=Path, required=True)
    p.add_argument('--saved', type=Path, required=True)
    p.add_argument('--port', type=Path, required=True)
    p.add_argument('--angular', type=int, default=768)
    p.add_argument('--stations', type=int, default=321)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    spec = importlib.util.spec_from_file_location('geometry_A_readout_loader', a.runtime_topic/'computations/geometric-checkpoint-core-pullback.py')
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    saved, loader = m.load_saved(a.saved, a.source_topic, a.port, a.angular)
    if saved.sol.sol.c.shape[0] != 6:
        raise ValueError('Expected the original physical quintic, not a new cubic interpolation')
    ss = np.unique(np.r_[np.linspace(0, saved.flow.end, a.stations), saved.flow.breaks])
    eta = 2*np.pi*np.arange(a.angular)/a.angular
    rows = []
    for first in range(0, len(ss), 8):
        batch = ss[first:first+8]
        angles = np.tile(eta, (len(batch), 1))
        base = saved.base(batch, angles)
        coeff = saved.sol.sol(batch)
        pos = base['pos']+saved.q*saved.synth(coeff, angles)
        d = base['p1']+saved.q*saved.synth(coeff, angles, 1)
        dd = base['p2']+saved.q*saved.synth(coeff, angles, 2)
        lam = np.linalg.norm(d, axis=-1)
        tangent = d/lam[..., None]
        normal_raw = dd-np.sum(dd*tangent, axis=-1)[..., None]*tangent
        kappa = np.linalg.norm(normal_raw, axis=-1)/lam**2
        aa, vv, acc = saved.flow.profile(batch)
        for i, s in enumerate(batch):
            radius = np.linalg.norm(pos[i, :, :2], axis=-1)
            margin = 1-(vv[i]/(aa[i]*kappa[i]))**2
            j = int(np.argmin(margin))
            rows.append(dict(s=float(s), a=float(aa[i]), ap=float(vv[i]), app=float(acc[i]),
                             latitude_kappa_min=float(kappa[i].min()),
                             latitude_kappa_max=float(kappa[i].max()),
                             a_kappa_min=float(aa[i]*kappa[i].min()),
                             normal_velocity_domain_min=float(margin.min()),
                             domain_min_angle=float(eta[j]),
                             radius_min=float(radius.min()), radius_max=float(radius.max()),
                             radius_span=float(radius.max()-radius.min()),
                             vertical_span=float(np.ptp(pos[i, :, 2]))))
    q = saved.flow._alternative_neck
    phases = []
    for seg in q.segments:
        sub = [r for r in rows if seg['s0']-1e-12 <= r['s'] <= seg['s1']+1e-12]
        phases.append(dict(kind=seg['kind'], s0=seg['s0'], s1=seg['s1'],
                           smallest_a_kappa=min(r['a_kappa_min'] for r in sub),
                           smallest_domain=min(r['normal_velocity_domain_min'] for r in sub),
                           start=min(sub, key=lambda r:abs(r['s']-seg['s0'])),
                           end=min(sub, key=lambda r:abs(r['s']-seg['s1']))))
    result = dict(scope=__doc__, saved_file=str(a.saved),
                  saved_sha256=hashlib.sha256(a.saved.read_bytes()).hexdigest(),
                  source_sha256=source_hash,
                  physical_polynomial_degree=5, physical_nodes=len(saved.sol.x),
                  angular=a.angular, stations=len(ss), profile=saved.rec['frozen_profile'],
                  prefix_length=saved.flow.prefix_end, complete_prefix_bridge_length=saved.flow.end,
                  phases=phases, rows=rows,
                  smallest_domain=min(r['normal_velocity_domain_min'] for r in rows))
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('physical_polynomial_degree','physical_nodes','stations','smallest_domain')}))
    for phase in phases:
        print(json.dumps({k:phase[k] for k in ('kind','s0','s1','smallest_a_kappa','smallest_domain')}))


if __name__ == '__main__':
    main()
