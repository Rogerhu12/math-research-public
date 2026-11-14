#!/usr/bin/env python3
"""Evaluate R122 on the actual p148 rotational background, piece by piece.

The comparison is to its explicit surface of revolution, with height from
separate Gauss quadrature. It checks geometry/sign conventions on the entire
candidate prefix; it is neither a nonlinear core nor a continuous certificate.
"""
from __future__ import annotations
import os
for _thread_key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_thread_key] = '1'
import argparse, hashlib, json, time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from fd2d_frozen_ellipse_candidate import Candidate, phase
from fd2d_gc_body_geometry import body_rhs, initial_body, initial_direction, numerical_readout

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def identity(path):
    path = Path(path)
    return dict(path=path.name, bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate', type=Path, default=ROOT/'notes/2026-11-12-fd2d-moderate-deep-p148-frozen-01.json')
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Keep each observed report immutable')
    started = time.monotonic()
    candidate = Candidate(json.loads(args.candidate.read_text()))
    angles = np.arange(8)*np.pi/4
    er = np.column_stack((np.cos(angles), np.sin(angles), np.zeros_like(angles)))
    et = np.column_stack((-np.sin(angles), np.cos(angles), np.zeros_like(angles)))
    ez = np.broadcast_to(np.array([0., 0., 1.]), er.shape)
    F0 = np.stack((ez, et, -er), axis=-1)
    X0 = candidate.a0*er
    witness = np.array([0., 1.405, 0.])
    values = np.stack((initial_body(F0, X0), initial_body(F0, X0, witness),
                       initial_direction(F0, np.array([0., 1., 0.])),
                       initial_direction(F0, np.array([0., 0., 1.]))))
    gx, gw = np.polynomial.legendre.leggauss(48)
    gx, gw = (gx+1)/2, gw/2
    z0 = 0.
    errors = {name:0. for name in ('radius', 'auxiliary_outward_support', 'witness_distance', 'y', 'z')}
    rows, calls = [], 0
    shape = values.shape
    for index, piece in enumerate(candidate.segments):
        def coefficients(u):
            if piece['kind'] == 'hermite':
                _, v, acc = candidate._jet(piece, np.atleast_1d(u))
                b = np.sqrt((1-v)*(1+v))
                return b, -acc/b
            phi, ps = phase(piece, np.atleast_1d(u))
            return np.cos(phi), -ps

        def rhs(u, state):
            _, ell = coefficients(u)
            q = state.reshape(shape)
            deriv = body_rhs(ell[0], 0., q, fixed_point=False)
            deriv[:2, :, 0] += 1
            return piece['L']*deriv.ravel()

        sol = solve_ivp(rhs, (0., 1.), values.ravel(), method='DOP853',
                        rtol=3e-13, atol=3e-15, max_step=.05, dense_output=True)
        if not sol.success:
            raise ArithmeticError(sol.message)
        calls += sol.nfev
        sample = np.linspace(0, 1, 17)
        z = []
        for u in sample:
            cuts = [0.]+[t for t in (.08, .92) if piece['kind']=='turn' and t<u]+[u]
            height = z0
            for lo, hi in zip(cuts[:-1], cuts[1:]):
                b, _ = coefficients(lo+(hi-lo)*gx)
                height += piece['L']*(hi-lo)*float(b@gw)
            z.append(height)
        z = np.asarray(z)
        a, v, acc = candidate._jet(piece, sample)
        b, _ = coefficients(sample)
        states = sol.sol(sample).T.reshape((len(sample),)+shape)
        measured = numerical_readout(states[:, 0], q_witness=states[:, 1],
                                     h_y=states[:, 2], h_z=states[:, 3])
        X = a[:, None, None]*er[None]+z[:, None, None]*ez[None]
        expected = dict(radius=np.broadcast_to(np.sqrt(a*a+z*z)[:, None], (len(sample), len(angles))),
                        auxiliary_outward_support=np.broadcast_to((a*b-z*v)[:, None], (len(sample), len(angles))),
                        witness_distance=np.linalg.norm(X-witness, axis=-1),
                        y=X[..., 1], z=X[..., 2])
        row = dict(piece=index, label=piece.get('label'), samples=len(sample))
        for name in errors:
            error = float(np.max(abs(measured[name]-expected[name])))
            errors[name] = max(errors[name], error)
            row[name+'_maximum_difference'] = error
        rows.append(row)
        z0 = float(z[-1])
        values = sol.y[:, -1].reshape(shape)
    report = dict(schema='fd2d-R122-body-background-check-v1', scope=__doc__,
                  source=identity(__file__), body_provider=identity(HERE/'fd2d_gc_body_geometry.py'),
                  candidate=identity(args.candidate), candidate_provider=identity(HERE/'fd2d_frozen_ellipse_candidate.py'),
                  initial_core='exact circular background evaluated numerically, not the noncircular accepted6 core',
                  angles=len(angles), pieces=len(rows), rhs_calls=calls,
                  full_prefix_length=candidate.end, background_height=z0,
                  maximum_numerical_comparison_errors=errors, piece_results=rows,
                  witness=witness.tolist(), witness_is_a_finite_diagnostic_only=True,
                  nonlinear_core_solved=False, continuous_certificate=False,
                  elapsed_seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(report=identity(args.out), errors=errors, seconds=report['elapsed_seconds']), indent=2), flush=True)


if __name__ == '__main__':
    main()
