#!/usr/bin/env python3
"""Actual finite GC flow of the balanced seed on one fixed candidate metric.

The computational angle is the FIXED seed normal angle phi. Its material
map is u=arc_seed(phi)/a0, so b=a(s)*rho_seed(phi)/a0. Independent n,m Fourier
coefficients drive pointwise position and orthogonal-frame equations. Every
reported metric and curvature is computed from actual position derivatives.
This finite IVP diagnostic does not solve the two-boundary problem, supply a
continuous enclosure, close the surface, or prove any global reach bound.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np
from fd2d_balanced_oval_core import BalancedOvalCore

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('fd2d_balanced_hybrid', HERE/'fd2d-gc-ellipse-hybrid-flow.py')
hybrid = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = hybrid
spec.loader.exec_module(hybrid)
base = hybrid.base


class Balanced(hybrid.Hybrid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.core = BalancedOvalCore()
        self.seed = self.core.normal_geometry(self.theta)
        self.ell0 = np.asarray(self.seed['rho'], dtype=np.longdouble)
        self.A, self.B = self.core.A, self.core.B
        if abs(self.a0-self.core.a0) > 1e-15:
            raise ValueError('Core and frozen physical profile have different a0')

    def initial(self):
        values = np.zeros((self.work, 14), dtype=np.longdouble)
        values[:, 0] = 1/self.ell0
        values[:, 2:5] = self.seed['F']
        values[:, 7] = 1
        values[:, 8:11] = self.seed['t']
        values[:, 11:14] = -self.seed['n']
        return self.encode(values)


if __name__ == '__main__':
    provider_before = base.identity(HERE/'fd2d_balanced_oval_core.py')
    base.Flow, base.__doc__ = Balanced, __doc__
    base.main()
    out = Path(sys.argv[sys.argv.index('--out')+1])
    report = json.loads(out.read_text())
    provider_after = base.identity(HERE/'fd2d_balanced_oval_core.py')
    if provider_before != provider_after:
        raise RuntimeError('Balanced input provider changed during this actual run')
    report.update(balanced_adapter=base.identity(__file__), balanced_provider=provider_before,
        pointwise_adapter=base.identity(HERE/'fd2d-gc-ellipse-hybrid-flow.py'),
        coordinate='fixed seed normal phi; physical material u=arc_seed(phi)/original_a0',
        target_b='a(s)*rho_seed(phi)/original_a0',
        state_representation='Fourier n,m and untruncated pointwise position plus frame',
        skew_frame_products_angularly_truncated=False,
        exact_ODE_definition_covers_finite_integrator_error=False,
        core=BalancedOvalCore().summary())
    out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
