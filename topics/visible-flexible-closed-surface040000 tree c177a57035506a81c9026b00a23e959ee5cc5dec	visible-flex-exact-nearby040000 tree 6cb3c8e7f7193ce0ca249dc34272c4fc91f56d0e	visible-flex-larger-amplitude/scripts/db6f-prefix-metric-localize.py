#!/usr/bin/env python3
"""Locate prefix metric errors and split source projection from interpolation.

All output is a floating, finite-angle diagnostic on one saved state.
The source field uses the original solver quadrature and the same frozen g.
No checkpoint or nonlinear equation is modified.
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


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root', type=Path, required=True)
    p.add_argument('--checkpoint', type=Path, required=True)
    p.add_argument('--linear-port', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--angular', type=int, default=1024)
    a = p.parse_args()
    spec = importlib.util.spec_from_file_location('localize_source', HERE/'db6f-prefix-flat-geometry-source.py')
    loader = importlib.util.module_from_spec(spec); spec.loader.exec_module(loader)
    rec, obj, unused, sol = loader.source(a.checkpoint, a.linear_port, a.source_root)
    flow = obj.Flow(obj.cfg, obj.port, obj.M, obj.q,
                    rec['config']['angular'], obj.base_mode, obj.bridge)
    N = a.angular
    B, B1, B2 = flow.basis(N)
    ss = np.unique(np.r_[np.linspace(0, flow.end, 151), sol.x,
                        (sol.x[:-1]+sol.x[1:])/2])
    rows = []
    maxima = {}
    def record(name, values, s):
        i = int(np.argmax(values)); v = float(values[i])
        if name not in maxima or maxima[name]['value'] < v:
            maxima[name] = dict(value=v, s=float(s[i]), normalized_s=float(s[i]/flow.end))
    for start in range(0, len(ss), 16):
        s = ss[start:start+16]
        Y, Yp = sol.sol(s), sol.sol(s, 1)
        srcp = flow.fun(s, Y, sol.p)
        fr = flow.frame(s, obj.q*Y, B1, B2)
        geo = fr['geo']; rho, v = geo['rho'], geo['v']
        aa = flow.profile(s)[0][:, None]
        Ft = fr['d']/rho[:, :, None]
        G = np.sum(Ft*Ft, axis=2)
        common = geo['s1']-v[:, :, None]*fr['d']
        common[:, :, 2] += np.mean(fr['V'][:, :, 2], axis=1)[:, None]
        local = {}
        for name, derivative in [('interpolant', Yp), ('source', srcp)]:
            Fs = common+obj.q*flow.values(derivative, B)
            err = np.stack((np.sum(Fs*Fs, axis=2)-1,
                            np.sum(Fs*Ft, axis=2)/aa, G/aa**2-1), axis=2)
            comp = np.sum(abs(np.fft.fft(err, axis=1)/N), axis=1)
            total = np.max(comp, axis=1)
            local[name] = total
            record(name+'_metric', total, s)
            for j, component in enumerate(('ss', 's_theta', 'theta_theta')):
                record(name+'_'+component, comp[:, j], s)
            record(name+'_velocity_defect', np.linalg.norm(Fs-fr['Vnormal'], axis=2).max(axis=1), s)
        interpolation = obj.q*flow.values(Yp-srcp, B)
        record('interpolation_velocity', np.linalg.norm(interpolation, axis=2).max(axis=1), s)
        for i, x in enumerate(s):
            rows.append(dict(s=float(x), source_metric=float(local['source'][i]),
                             interpolant_metric=float(local['interpolant'][i])))
    rows.sort(key=lambda r:r['interpolant_metric'], reverse=True)
    out = dict(scope=__doc__, checkpoint=str(a.checkpoint),
               checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),
               script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               modes=obj.M, source_angular=rec['config']['angular'], audit_angular=N,
               radial_points=len(ss), maxima=maxima, worst_samples=rows[:32],
               saved_inlet=rec['summary']['inlet'],
               support_coefficients=rec['summary']['core']['coefficients'])
    a.out.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(dict(modes=obj.M, maxima=maxima)), flush=True)


if __name__ == '__main__':
    main()
