#!/usr/bin/env python3
"""Actual finite Frenet IVP from the complete 32-mode R225 core.

This is an open-prefix numerical design probe, not a closed-surface result.
The geometric metric ds^2+a(s)^2 d(material-angle)^2 and full core are fixed
when M/N/steps change. All reported extrema are sampled; no reach is claimed.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
from fractions import Fraction
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('r225_frenet_base', HERE / 'alternative-outward-probe.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
spec = importlib.util.spec_from_file_location('r225_control_law', HERE / 'alternative-controlled-profile.py')
control = importlib.util.module_from_spec(spec)
spec.loader.exec_module(control)


class FullCoreProbe(base.Probe):
    def __init__(self, coefficients, M, N, velocity, length, k0):
        if M < len(coefficients) or N < 4 * M + 4:
            raise ValueError('All 32 core modes and sufficiently many angular points are required')
        super().__init__(A=0., M=M, N=N, v=.5, S=1., amax=2.)
        self.coefficients = np.asarray(coefficients, dtype=float)
        self.law = control.HermiteOutward(velocity, length, k0)
        self.rho0 = 1 + ((1 - self.freq[1:len(coefficients)+1]**2) * coefficients) @ self.C[1:len(coefficients)+1]
        if float(self.rho0.min()) <= 0:
            raise ValueError('Core rho is nonpositive at a sample')
        self.hmajor = 1 + float(np.sum(coefficients))
        self.hminor = 1 + float(np.sum(coefficients * (-1.)**np.arange(1, len(coefficients)+1)))
        self.gap = self.hmajor - self.hminor
        self.witness = np.array([0., self.hmajor, 0.])

    def profile(self, s):
        return self.law.profile(s)

    def initial(self):
        y = np.zeros(self.n)
        y[0] = 1.
        k = len(self.coefficients)
        y[1:k+1] = self.coefficients
        y[self.M+1:self.M+k+1] = -self.freq[1:k+1] * self.coefficients
        return y

    def stats(self, s, y):
        row = super().stats(s, y)
        F, _, _ = self.jet(y)
        cp, sp = np.cos(self.phi), np.sin(self.phi)
        xyz = np.stack([cp*F[:,0]-sp*F[:,1], sp*F[:,0]+cp*F[:,1], F[:,2]], axis=1)
        dist2 = np.sum((xyz-self.witness)**2, axis=1)
        j = int(np.argmin(dist2))
        norms = np.linalg.norm(xyz, axis=1)
        row.update(ball_radius_max=float(norms.max()),
                   core_witness_sample_distance=float(np.sqrt(dist2[j])),
                   core_witness_sample_ball_margin=float(dist2[j]-self.gap**2),
                   witness_nearest_angle=float(self.phi[j]),
                   minor_axis_point=xyz[self.N//4].tolist(),
                   app=float(self.profile(s)[2]))
        return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--core', type=Path, required=True)
    ap.add_argument('--M', type=int, default=48)
    ap.add_argument('--N', type=int, default=512)
    ap.add_argument('--v', type=float, default=.3)
    ap.add_argument('--length', type=float, default=.9)
    ap.add_argument('--k0', type=float, default=.2)
    ap.add_argument('--end', type=float)
    ap.add_argument('--steps', type=int, default=90)
    ap.add_argument('--maxstep', type=float, default=.002)
    ap.add_argument('--rtol', type=float, default=1e-11)
    ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args()
    raw = a.core.read_bytes()
    core = json.loads(raw)
    if core['check_count'] != 126 or core['all_checks'] is not True:
        raise ValueError('Expected the complete R225 exact core report')
    fractions = [Fraction(int(r['value']['numerator']), int(r['value']['denominator'])) for r in core['coefficients']]
    coeff = np.array([float(c) for c in fractions])
    q = FullCoreProbe(coeff, a.M, a.N, a.v, a.length, a.k0)
    y = q.initial()
    end = a.length if a.end is None else a.end
    start = time.time()
    rows, states, accepted = [q.stats(0., y)], [y.tolist()], [0.]
    reached = 0.
    status = 'success'
    for i, right in enumerate(np.linspace(0, end, a.steps+1)[1:]):
        try:
            sol = solve_ivp(q.fun, (reached, right), y, method='DOP853',
                            rtol=a.rtol, atol=a.rtol*.01,
                            max_step=min(a.maxstep, (right-reached)/2))
            if not sol.success:
                raise RuntimeError(sol.message)
            y = sol.y[:, -1]
            reached = float(right)
            rows.append(q.stats(reached, y))
            states.append(y.tolist())
            accepted.append(reached)
            if (i+1) % 10 == 0:
                print(json.dumps(dict(event='prefix', index=i+1, reached_s=reached,
                                      metric=rows[-1]['metric_sample'],
                                      kappa=rows[-1]['surface_kappa_sample'],
                                      witness=rows[-1]['core_witness_sample_distance'])), flush=True)
        except Exception as e:
            status = repr(e)
            break
    scientific_parameters = dict(core_sha256=hashlib.sha256(raw).hexdigest(),
                                 coefficients_rational=[str(c) for c in fractions],
                                 law=dict(velocity=a.v, length=a.length, k0=a.k0), end=end)
    report = dict(scope=__doc__, status=status, reached_s=reached, target_s=end,
                  metric_identity=scientific_parameters,
                  metric_identity_sha256=hashlib.sha256(json.dumps(scientific_parameters, sort_keys=True).encode()).hexdigest(),
                  numerical_parameters=dict(M=a.M,N=a.N,steps=a.steps,maxstep=a.maxstep,rtol=a.rtol),
                  rows=rows, coefficient_states=states, state_locations=accepted,
                  full_original_32_core_kept=True,
                  core=dict(hmajor=q.hmajor,hminor=q.hminor,gap=q.gap,
                            rho_sample_min=float(q.rho0.min()),rho_sample_max=float(q.rho0.max())),
                  summary=dict(metric_sample=max(r['metric_sample'] for r in rows),
                               kappa_sample=max(r['surface_kappa_sample'] for r in rows),
                               reflected_prefix_D_sample=2*max(r['ball_radius_max'] for r in rows),
                               core_witness_sample_distance=min(r['core_witness_sample_distance'] for r in rows),
                               smallest_domain_margin=min(r['margin'] for r in rows)),
                  calls=q.calls,seconds=time.time()-start,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  base_source_sha256=hashlib.sha256((HERE/'alternative-outward-probe.py').read_bytes()).hexdigest())
    a.out.parent.mkdir(parents=True,exist_ok=True)
    encoded=(json.dumps(report,indent=2)+'\n').encode()
    if a.out.suffix=='.gz': a.out.write_bytes(gzip.compress(encoded,mtime=0))
    else: a.out.write_bytes(encoded)
    print(json.dumps(dict(event='complete', status=status, reached_s=reached, target_s=end,
                          seconds=report['seconds'], calls=q.calls, summary=report['summary'],
                          output=str(a.out))), flush=True)
    return 0


if __name__=='__main__':
    raise SystemExit(main())
