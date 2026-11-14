#!/usr/bin/env python3
"""Compare actual boost and first-turn curvature on a small saved-map sample.

No solve or Jacobian is constructed. These deliberately sparse samples only
locate a design bottleneck. They are neither a full interval audit nor a
continuous curvature, reach, or closed-surface certificate.
"""
from __future__ import annotations
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import time

import numpy as np

HERE = Path(__file__).resolve().parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('input', 'source-topic', 'port', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--angular', type=int, default=512)
    args = parser.parse_args()
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    input_hash = hashlib.sha256(args.input.read_bytes()).hexdigest()
    started = time.time()
    cv = module('strong_sparse_curvature_module', HERE/'alternative-neck-curvature-map.py')
    saved, _ = cv.pb.load_saved(args.input, args.source_topic, args.port, args.angular)
    if not saved.rec['solver_success']:
        raise ValueError('Successful saved prefix required')
    flow = saved.flow
    B, B1, B2 = flow.basis(args.angular)
    prefix = flow._alternative_neck
    selected = [seg for seg in prefix.segments
                if cv.label(seg, prefix.loop_begin) in ('boost', 'first descending turn')]
    if len(selected) != 2:
        raise ValueError('Expected one boost and one first descending turn')
    rows = []
    for seg in selected:
        fractions = np.unique(np.r_[np.linspace(0, 1, 21), .075, .08, .085, .915, .92, .925])
        samples = []

        def evaluate(fractions):
            for first in range(0, len(fractions), 4):
                u = fractions[first:first+4]
                s = seg['s0']+seg['length']*u
                Y = saved.sol.sol(s)
                Yp = saved.sol.sol(s, 1)
                Ypp = saved.sol.sol(s, 2)
                frame, Fsp, dW = flow.velocity_s(s, Y, Yp, B1, B2)
                geo = frame['geo']
                Fs = geo['s1']+saved.q*flow.values(Yp, B)
                Fs[:, :, 2] += np.mean(frame['V'][:, :, 2], axis=1)[:, None]
                Fss = geo['s2']+saved.q*flow.values(Ypp, B)
                Fss[:, :, 2] += np.mean(dW[:, :, 2], axis=1)[:, None]
                values = cv.principal(Fs, frame['d'], Fss, Fsp, frame['dd'])
                radius, speed, accel = flow.profile(s)
                for k in range(len(s)):
                    j = int(np.argmax(values[0][k]))
                    samples.append(dict(s=float(s[k]), segment_fraction=float(u[k]),
                        psi=float(j*2*np.pi/args.angular), kappa=float(values[0][k, j]),
                        principal_signed=[float(values[i][k, j]) for i in (1, 2)],
                        chart_meridian_normal=float(values[3][k, j]),
                        chart_mixed_normal=float(values[4][k, j]),
                        chart_latitude_normal=float(values[5][k, j]),
                        background_meridian_curvature=float(abs(accel[k])/np.sqrt(1-speed[k]**2)),
                        background_latitude_curvature=float(np.sqrt(1-speed[k]**2)/radius[k])))

        evaluate(fractions)
        best = max(samples, key=lambda r: r['kappa'])
        nearby = np.linspace(max(0, best['segment_fraction']-.025),
                             min(1, best['segment_fraction']+.025), 9)
        nearby = np.asarray([u for u in nearby if not np.any(abs(fractions-u) < 1e-14)])
        evaluate(nearby)
        rows.append(dict(label=cv.label(seg, prefix.loop_begin),
                         segment_bounds=[seg['s0'], seg['s1']], radial_samples=len(samples),
                         best=max(samples, key=lambda r: r['kappa']), samples=samples))
    result = dict(scope=__doc__, nonlinear_solve_run=False, input=str(args.input),
                  input_sha256=input_hash, source_sha256=source_hash,
                  angular=args.angular, batch=4,
                  total_radial_samples=sum(row['radial_samples'] for row in rows),
                  frozen_profile=saved.rec['frozen_profile'], rows=rows,
                  seconds=time.time()-started)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(seconds=result['seconds'], radial_samples=result['total_radial_samples'],
                          peaks=[dict(label=row['label'], **row['best']) for row in rows]), indent=2))


if __name__ == '__main__':
    main()
