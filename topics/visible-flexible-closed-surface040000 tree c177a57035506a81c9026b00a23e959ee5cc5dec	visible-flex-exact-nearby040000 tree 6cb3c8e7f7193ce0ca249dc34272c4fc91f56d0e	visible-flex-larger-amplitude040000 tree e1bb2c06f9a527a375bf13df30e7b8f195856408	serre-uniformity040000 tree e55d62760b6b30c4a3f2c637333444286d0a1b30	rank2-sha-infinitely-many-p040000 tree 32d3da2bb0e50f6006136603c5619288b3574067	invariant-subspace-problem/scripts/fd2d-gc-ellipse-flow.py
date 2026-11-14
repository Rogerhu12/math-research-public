#!/usr/bin/env python3
"""Finite first-angular-derivative Gauss--Codazzi IVP on the frozen v2 g.

Independent Fourier coefficients evolve for n,m, position and an auxiliary
orthonormal frame. The actual position velocity, angular derivatives and
projected acceleration determine E,F,G and principal curvatures; auxiliary
frame orthogonality is never substituted for these checks. This is a finite
diagnostic, not a closed surface, a BVP solution or a continuous certificate.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import time
import numpy as np
from scipy import fft
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('fd2d_gc_frozen_metric', HERE/'fd2d_frozen_ellipse_candidate.py')
frozen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(frozen)


def identity(path):
    path = Path(path)
    return dict(file=str(path.resolve()), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


class Flow:
    # n,m; X; e1; e2; normal. Parity is the exact D2 symmetry of the inlet.
    harmonic_parity = np.array([0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0])
    imaginary = np.array([0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0], dtype=bool)

    def __init__(self, candidate, modes, oversample, max_calls):
        self.candidate, self.M, self.work = candidate, modes, 2*oversample*(modes+1)
        self.max_calls, self.calls = max_calls, 0
        self.A, self.B, self.a0 = candidate.ellipse.A, candidate.ellipse.B, candidate.ellipse.a0
        self.theta = np.arange(self.work, dtype=np.longdouble)*(2*np.arccos(np.longdouble(-1))/self.work)
        self.ell0 = np.sqrt((self.A*np.sin(self.theta))**2+(self.B*np.cos(self.theta))**2)
        self.wave = np.fft.fftfreq(self.work, 1/self.work).astype(np.longdouble)
        kk = np.arange(modes+1)[:, None]
        allowed = kk % 2 == self.harmonic_parity[None, :]
        allowed[0, self.imaginary] = False
        self.indices = np.nonzero(allowed)
        self.active_wave = self.indices[0]
        self.cache_s, self.cache_y, self.cache_frame = None, None, None

    def decode(self, state):
        raw = np.zeros((self.work//2+1, 14), dtype=np.clongdouble)
        factors = np.where(self.imaginary[self.indices[1]], 1j, 1)
        raw[self.indices] = np.asarray(state, dtype=np.longdouble)*factors
        return fft.irfft(raw, n=self.work, axis=0, norm='forward')

    def encode(self, values):
        raw = fft.rfft(np.asarray(values, dtype=np.longdouble), axis=0, norm='forward')
        selected = raw[self.indices]
        return np.asarray(np.where(self.imaginary[self.indices[1]], selected.imag, selected.real), dtype=float)

    def derivative(self, values, order=1):
        return fft.ifft(fft.fft(values, axis=0)*(1j*self.wave[:, None])**order, axis=0).real

    def initial(self):
        """Positive binomial products avoid FFT cancellation in tiny inlet modes.

        ell=C |1-q exp(2i theta)|. For beta=1/2 or 3/2,
        (1-q z)^(-beta)(1-q/z)^(-beta) has coefficient
        sum_j ((beta)_(j+k)/(j+k)! q^(j+k))*((beta)_j/j! q^j).
        The finite evaluation is numerical, not an interval input certificate.
        """
        q = (np.longdouble(self.A)-np.longdouble(self.B))/(np.longdouble(self.A)+np.longdouble(self.B))
        C = (np.longdouble(self.A)+np.longdouble(self.B))/2
        limit = self.M+320
        def coefficients(beta):
            a = np.ones(limit+1, dtype=np.longdouble)
            for j in range(1, limit+1):
                a[j] = a[j-1]*q*(np.longdouble(beta)+j-1)/j
            return np.array([np.sum(a[k:]*a[:limit+1-k]) for k in range(self.M//2+3)])
        speed_inverse = coefficients(.5)/C
        curvature = self.A*self.B*coefficients(1.5)/C**3
        raw = np.zeros((self.M+1, 14), dtype=np.clongdouble)
        raw[0, 7] = 1
        raw[1, 2] = self.A/2
        raw[1, 3] = -1j*self.B/2
        for k in range(self.M+1):
            if k % 2 == 0:
                raw[k, 0] = curvature[k//2]
            else:
                left, right = speed_inverse[(k-1)//2], speed_inverse[(k+1)//2]
                raw[k, 8] = 1j*self.A*(left-right)/2
                raw[k, 9] = self.B*(left+right)/2
                raw[k, 11] = -raw[k, 9]
                raw[k, 12] = raw[k, 8]
        selected = raw[self.indices]
        return np.asarray(np.where(self.imaginary[self.indices[1]], selected.imag, selected.real), dtype=float)

    def frame(self, s, state):
        if s == self.cache_s and self.cache_y is not None and np.array_equal(state, self.cache_y):
            return self.cache_frame
        values = self.decode(state)
        n, m = values[:, 0], values[:, 1]
        if np.min(n) <= 0:
            raise ArithmeticError('The chosen nonzero normal-curvature chart failed')
        X, e1, e2, normal = (values[:, a:a+3] for a in (2, 5, 8, 11))
        a, ap, app = [np.longdouble(x[0]) for x in self.candidate.profile([s])]
        c, K, b = ap/a, -app/a, (a/self.a0)*self.ell0
        l = (m*m+K)/n
        lm_derivative = self.derivative(np.column_stack((l, m)))
        velocity = np.empty_like(values)
        velocity[:, 0] = lm_derivative[:, 1]/b+c*(l-n)
        velocity[:, 1] = lm_derivative[:, 0]/b-2*c*m
        velocity[:, 2:5] = e1
        velocity[:, 5:8] = l[:, None]*normal
        velocity[:, 8:11] = m[:, None]*normal
        velocity[:, 11:14] = -l[:, None]*e1-m[:, None]*e2
        projected_coefficients = self.encode(velocity)
        projected = self.decode(projected_coefficients)
        Xs, Xss = projected[:, 2:5], projected[:, 5:8]
        Xu, Xuu, Xsu = self.derivative(X), self.derivative(X, 2), self.derivative(Xs)
        E, F, G = (np.sum(Xs*Xs, axis=1), np.sum(Xs*Xu, axis=1), np.sum(Xu*Xu, axis=1))
        de, df, dg = E-1, F/b, G/b**2-1
        metric = abs(de+dg)/2+np.sqrt(((de-dg)/2)**2+df**2)
        own_normal = np.cross(Xs, Xu)
        own_normal /= np.linalg.norm(own_normal, axis=1)[:, None]
        L, M, N = (np.sum(own_normal*v, axis=1) for v in (Xss, Xsu, Xuu))
        determinant = E*G-F*F
        trace = (G*L-2*F*M+E*N)/determinant
        gauss = (L*N-M*M)/determinant
        curvature = abs(trace)/2+np.sqrt(np.maximum(0, trace**2/4-gauss))
        basis = np.stack((e1, e2, normal), axis=2)
        orthogonality = np.max(abs(np.einsum('nki,nkj->nij', basis, basis)-np.eye(3)))
        result = dict(values=values, coefficients=projected_coefficients, a=a, ap=ap, app=app, K=K,
                      metric=float(np.max(metric)), E_error=float(np.max(abs(de))),
                      F_error=float(np.max(abs(df))), G_error=float(np.max(abs(dg))),
                      actual_curvature=float(np.max(curvature)), minimum_n=float(np.min(n)),
                      orthogonality=float(orthogonality),
                      curve_frame_defect=float(np.max(np.linalg.norm(Xu-b[:, None]*e2, axis=1)/b)),
                      projection_defect=float(np.max(np.linalg.norm(velocity-projected, axis=1))),
                      maximum_abs_y=float(np.max(abs(X[:, 1]))), maximum_abs_z=float(np.max(abs(X[:, 2]))),
                      maximum_radius=float(np.max(np.linalg.norm(X, axis=1))),
                      held_distance=float(np.min(np.linalg.norm(X-np.array([0., self.A, 0.]), axis=1))))
        self.cache_s, self.cache_y, self.cache_frame = s, np.array(state, copy=True), result
        return result

    def rhs(self, s, state):
        self.calls += 1
        if self.calls > self.max_calls:
            raise RuntimeError('Finite diagnostic RHS budget reached; no endpoint conclusion')
        return self.frame(s, state)['coefficients']

    def diagnostics(self, s, state):
        data = self.frame(s, state)
        return dict(s=float(s), **{k:float(v) for k, v in data.items() if k not in ('values', 'coefficients')})


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--state', type=Path, required=True)
    p.add_argument('--modes', type=int, default=95)
    p.add_argument('--oversample', type=int, default=2)
    p.add_argument('--stop-at', type=float, default=.53)
    p.add_argument('--max-step', type=float, default=.001)
    p.add_argument('--max-calls', type=int, default=80000)
    args = p.parse_args()
    if args.out.exists() or args.state.exists():
        raise FileExistsError('Use new diagnostic outputs')
    candidate = frozen.Candidate(json.loads(args.candidate.read_text()))
    flow = Flow(candidate, args.modes, args.oversample, args.max_calls)
    state = flow.initial()
    stop, last, started = min(candidate.end, args.stop_at), 0., time.monotonic()
    report = dict(schema='fd2d-fixed-g-first-order-codazzi-flow-v1', scope=__doc__,
                  source=identity(__file__), provider=identity(HERE/'fd2d_frozen_ellipse_candidate.py'),
                  candidate=identity(args.candidate), modes=args.modes, geometry_grid=flow.work,
                  dtypes=dict(ode_state=str(state.dtype), point_geometry=str(flow.decode(state).dtype),
                              longdouble_mantissa_bits=int(np.finfo(np.longdouble).nmant)),
                  metric_frozen=True, actual_metric_from_position_derivatives=True,
                  angular_derivative_order_in_dynamic_shape_equations=1,
                  closed_surface=False, continuous_certificate=False, BVP_solved=False,
                  initial=flow.diagnostics(0., state), rows=[])
    def metric(s,y): return 2e-5-flow.frame(s,y)['metric']
    def curvature(s,y): return 1/.136-flow.frame(s,y)['actual_curvature']
    def normal(s,y): return flow.frame(s,y)['minimum_n']-1e-4
    def slab(s,y): return .75-flow.frame(s,y)['maximum_abs_y']
    def height(s,y): return 1.2886410585615193-flow.frame(s,y)['maximum_abs_z']
    events = [metric, curvature, normal, slab, height]
    names = ['metric', 'curvature', 'normal_chart', 'slab', 'height']
    for event in events:
        event.terminal, event.direction = True, -1
    atol = 2e-14/(1+flow.active_wave)**2
    try:
        for j, seg in enumerate(candidate.segments):
            if seg['s0'] >= stop-1e-14:
                break
            right = min(seg['s1'], stop)
            sol = solve_ivp(flow.rhs, (seg['s0'], right), state, method='DOP853',
                            rtol=2e-12, atol=atol, max_step=args.max_step,
                            t_eval=np.linspace(seg['s0'], right, 5), events=events)
            samples = [flow.diagnostics(s,y) for s,y in zip(sol.t,sol.y.T)]
            last, state = float(sol.t[-1]), sol.y[:, -1]
            if sol.status == 1:
                for ts, ys in zip(sol.t_events, sol.y_events):
                    if len(ts):
                        last, state = float(ts[-1]), ys[-1]
                        samples.append(flow.diagnostics(last,state))
            row = dict(segment=j, kind=seg['kind'], status=sol.status, last=samples[-1],
                       events={name:ts.tolist() for name,ts in zip(names,sol.t_events)},
                       maximum_metric=max(x['metric'] for x in samples),
                       maximum_curvature=max(x['actual_curvature'] for x in samples))
            report['rows'].append(row)
            report.update(last_s=last, rhs_calls=flow.calls, seconds=time.monotonic()-started)
            args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
            np.savez_compressed(args.state, state=state, s=last, modes=args.modes,
                                candidate_sha256=report['candidate']['sha256'])
            if j % 10 == 0 or sol.status != 0:
                print(json.dumps(dict(segment=j, s=last, metric=row['last']['metric'],
                                      curvature=row['last']['actual_curvature'], status=sol.status)), flush=True)
            if sol.status != 0:
                break
    except Exception as exc:
        report['failure'] = dict(type=type(exc).__name__, message=str(exc))
    report.update(last_s=last, rhs_calls=flow.calls, seconds=time.monotonic()-started,
                  reaches_requested_endpoint=abs(last-stop)<1e-12)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps({k:report.get(k) for k in ('last_s','reaches_requested_endpoint','rhs_calls','seconds','failure')}), flush=True)


if __name__ == '__main__':
    main()
