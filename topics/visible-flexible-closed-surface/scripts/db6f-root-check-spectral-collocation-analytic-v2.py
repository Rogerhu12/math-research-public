#!/usr/bin/env python3
"""Analytic, non-geometric BVP checks of the new coordinate-return interface.

No research candidate, DN, moment engine, geometry, or physical metric is read.
The exact answer is independently available in exponentials and a quadratic.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import numpy as np
from scipy.integrate import solve_bvp


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', required=True, type=Path)
    a = ap.parse_args()
    path = Path(__file__).with_name('db6f-root-spectral-collocation-v2.py')
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    assert digest == '47e1128c8cabb7c77797ebea6534cf77d63964add54f78a2cab827d1f0101854'
    spec = importlib.util.spec_from_file_location('root_spectral_conjugacy', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    n = 7
    rates = -np.arange(n, dtype=float)/8
    initial = np.arange(n, dtype=float)/16
    forcing = np.array([0.] + [(-1.)**j/(10*(j+1)) for j in range(1, n)])

    def fun(x, y, p):
        value = rates[:, None]*y + p[0]*forcing[:, None]
        value[0] = p[0]*x
        return value

    def jac(x, y, p):
        fy = np.zeros((n, n, len(x)))
        fy[np.arange(n), np.arange(n), :] = rates[:, None]
        fp = np.broadcast_to(forcing[:, None, None], (n, 1, len(x))).copy()
        fp[0, 0] = x
        return fy, fp

    def bc(ya, yb, p):
        return np.r_[ya-initial, yb[0]-1]

    def bc_jac(ya, yb, p):
        aa = np.zeros((n+1, n)); bb = aa.copy()
        aa[:n] = np.eye(n); bb[n, 0] = 1
        return aa, bb, np.zeros((n+1, 1))

    def exact(x, derivative):
        answer = np.empty((n, len(x)))
        if derivative == 0:
            answer[0] = x*x
            for j in range(1, n):
                answer[j] = initial[j]*np.exp(rates[j]*x) + 2*forcing[j]/rates[j]*np.expm1(rates[j]*x)
        elif derivative == 1:
            answer[0] = 2*x
            for j in range(1, n):
                answer[j] = (rates[j]*initial[j]+2*forcing[j])*np.exp(rates[j]*x)
        else:
            raise ValueError('Only the two independently checked quantities are defined')
        return answer

    x = np.linspace(0, 1, 5)
    y = np.broadcast_to(initial[:, None], (n, len(x))).copy()
    options = dict(p=np.array([1.]), fun_jac=jac, bc_jac=bc_jac,
                   tol=2e-9, bc_tol=1e-10, max_nodes=1000)
    original = solve_bvp(fun, bc, x, y, **options)
    weighted, records = module.make_solver(module.power2_weights(2))
    transformed = weighted(fun, bc, x, y, **options)
    sample = np.linspace(0, 1, 257)
    results = {}
    for label, result in [('original', original), ('weighted_physical_return', transformed)]:
        assert result.success
        value_error = float(np.max(abs(result.sol(sample)-exact(sample, 0))))
        derivative_error = float(np.max(abs(result.sol(sample, 1)-exact(sample, 1))))
        parameter_error = float(abs(result.p[0]-2))
        node_derivative_error = float(np.max(abs(result.yp-fun(result.x, result.y, result.p))))
        assert value_error < 1e-8 and derivative_error < 2e-8
        assert parameter_error < 1e-12 and node_derivative_error < 1e-12
        assert result.sol.axis == 1 and result.sol.c.shape == (4, len(result.x)-1, n)
        assert np.max(result.rms_residuals) <= options['tol']
        assert np.max(abs(bc(result.y[:, 0], result.y[:, -1], result.p))) <= options['bc_tol']
        results[label] = dict(nodes=len(result.x), p_error=parameter_error,
                              value_error=value_error, first_derivative_error=derivative_error,
                              node_derivative_error=node_derivative_error,
                              physical_rms_max=float(np.max(result.rms_residuals)))
    assert len(records) == 1 and records[0]['success']
    assert records[0]['weighted_rms_max'] >= records[0]['original_physical_rms_max']
    before = len(records)
    try:
        weighted(fun, bc, x, y, S=np.eye(n), **options)
    except ValueError as exc:
        singular_rejection = str(exc)
    else:
        raise AssertionError('Unsupported singular input was accepted')
    assert len(records) == before
    # The rejected inputs must never reach any physical callback or SciPy solve.
    callback_count = [0]
    def forbidden_callback(*args):
        callback_count[0] += 1
        raise AssertionError('Rejected input reached a callback')
    rejected = []
    for dtype in ('complex', 'object_complex'):
        bad_weights = module.power2_weights(2).astype(complex)
        bad_weights[0] += 1j
        if dtype == 'object_complex':
            bad_weights = np.array([np.complex128(v) for v in bad_weights], dtype=object)
        try:
            module.make_solver(bad_weights)
        except ValueError:
            rejected.append('weights_' + dtype)
        else:
            raise AssertionError('Nonreal weights were silently cast')
        bad_p = np.array([np.complex128(1+1j)], dtype=object if dtype == 'object_complex' else complex)
        bad_x = np.array([np.complex128(v+1j) for v in x], dtype=object if dtype == 'object_complex' else complex)
        for name, bad_mesh, bad_parameters in [('p_'+dtype, x, bad_p), ('x_'+dtype, bad_x, options['p'])]:
            try:
                weighted(forbidden_callback, forbidden_callback, bad_mesh, y, p=bad_parameters,
                         fun_jac=forbidden_callback, bc_jac=forbidden_callback)
            except ValueError:
                rejected.append(name)
            else:
                raise AssertionError('Nonreal mesh/parameters were silently cast')
    assert callback_count[0] == 0 and len(rejected) == 6 and len(records) == before
    report = dict(status='ANALYTIC_NON_GEOMETRIC_BVP_INTERFACE_PASS',
                  module_sha256=digest,
                  checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  complex_or_object_inputs_rejected_without_callbacks=rejected,
                  rejection_callback_count=callback_count[0],
                  exact_solution='p=2; y0=x^2; yi=ai*exp(li*x)+2*bi/li*expm1(li*x)',
                  physical_problem_solve_count=0, nongeometric_scipy_solves=2,
                  candidate_or_DN_files_read=False, results=results,
                  transformed_records=records, unsupported_S_rejected_before_solve=singular_rejection,
                  scope='Only parameter/Jacobian/physical-PPoly-return and original-residual gate checks; no M14 or G5 claim.')
    with a.out.open('x') as f:
        json.dump(report, f, ensure_ascii=False, indent=2); f.write('\n')
    print(json.dumps(dict(status=report['status'], results=results,
                          report_bytes=a.out.stat().st_size,
                          report_sha256=hashlib.sha256(a.out.read_bytes()).hexdigest())))


if __name__ == '__main__':
    main()
