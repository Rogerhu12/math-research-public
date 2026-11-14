#!/usr/bin/env python3
"""Inspect convexity of the existing amplitude warm-core extrapolation only.

The coefficients follow the actual linear-secondary-law restart exponent:
q1/q2 scale linearly and coefficient j>=3 scales by (q/q0)^ceil(j/2).
No coefficient sequence here is asserted to solve a new BVP. Floating
Chebyshev critical-point calculations are diagnostics, not interval proofs.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.optimize import brentq


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    source_sha256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    restart_source = Path(__file__).with_name('root_dual_core_bvp.py')
    restart_source_sha256 = hashlib.sha256(restart_source.read_bytes()).hexdigest()
    raw = args.input.read_bytes()
    data = json.loads(gzip.decompress(raw) if args.input.suffix == '.gz' else raw)
    if not data['solver_success'] or data['secondary_law'] != 'linear':
        raise ValueError('Successful linear-secondary-law prefix required')
    c = np.asarray(data['core']['coefficients'], dtype=float)
    q0 = float(data['gauge_amplitude'])
    j = np.arange(1, len(c)+1)
    exponents = np.ceil(j/2)
    exponents[:2] = 1

    def minimum(q, keep):
        coeff = c*(q/q0)**exponents
        coeff[keep:] = 0
        # rho(phi)=h+h''=1-sum((4*j*j-1)*c_j*T_j(cos(2*phi))).
        polynomial = np.r_[1., -(4*j*j-1)*coeff]
        roots = np.polynomial.chebyshev.chebroots(np.polynomial.chebyshev.chebder(polynomial))
        x = [-1., 1.]+[float(r.real) for r in roots if abs(r.imag)<1e-9 and -1 <= r.real <= 1]
        values = np.polynomial.chebyshev.chebval(x, polynomial)
        k = int(np.argmin(values))
        return dict(minimum_rho=float(values[k]), cos_two_phi=float(x[k]),
                    evaluated_real_critical_points=len(x)-2)

    rows = []
    for q in (.085, .09, .10, .15, .2, .25, .3, .35, .38, .4):
        rows.append(dict(q=q, full_warm=minimum(q, len(c)),
                         three_harmonic_comparison=minimum(q, 3)))
    crossings = []
    for keep in (len(c), 3):
        grid = np.linspace(q0, .45, 201)
        values = [minimum(q, keep)['minimum_rho'] for q in grid]
        for a, b, fa, fb in zip(grid, grid[1:], values, values[1:]):
            if fa > 0 >= fb:
                zero = brentq(lambda q: minimum(q, keep)['minimum_rho'], a, b)
                crossings.append(dict(retained_harmonics=keep, first_detected_zero=zero,
                                      bracket=[float(a), float(b)]))
                break
    result = dict(scope=__doc__, nonlinear_solve_run=False,
                  input=str(args.input), input_sha256=hashlib.sha256(raw).hexdigest(),
                  source_sha256=source_sha256,
                  restart_formula_source=str(restart_source),
                  restart_formula_source_sha256=restart_source_sha256,
                  q0=q0, source_coefficients=c.tolist(), warm_exponents=exponents.tolist(),
                  rho_formula='1-sum((4*j^2-1)*c_j*T_j(cos(2*phi)))',
                  secondary_comparison_scope='Deleting all modes above physical m=6 is only a second extrapolation diagnostic, not a solved field or a spectral refinement.',
                  rows=rows, zero_crossing_diagnostics=crossings,
                  conclusion='Small q=.09 warm has positive inlet rho in this floating calculation. The same frozen coefficients cannot be extrapolated in one jump to q~.4. A true branch changes all free coefficients and geometry; this is not a nonexistence result.')
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(rows=rows, zero_crossings=crossings), indent=2))


if __name__ == '__main__':
    main()
