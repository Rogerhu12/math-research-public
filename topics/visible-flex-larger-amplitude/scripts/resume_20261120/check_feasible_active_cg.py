#!/usr/bin/env python3
"""Reproduce the one independent small convex-QP check; no field solve."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import minimize, LinearConstraint
from scipy.sparse.linalg import aslinearoperator


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Do not overwrite an actual check')
    spec = importlib.util.spec_from_file_location('checked_full_inequality_qp', args.source)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    rng = np.random.default_rng(2026112007)
    n, m = 32, 28
    A = rng.standard_normal((85, n))/np.sqrt(85)
    residual = rng.standard_normal(85)
    C = rng.standard_normal((m, n))
    C /= np.linalg.norm(C, axis=1)[:, None]
    bounds = .005+.08*rng.random(m)
    mu = .03
    z, report = module.solve(aslinearoperator(A), residual, C, bounds,
        damping=mu, parameters=module.Parameters(maxiter=400, rtol=1e-9,
                                               atol=1e-12, progress_every=100))
    H, g = A.T@A+mu**2*np.eye(n), A.T@residual
    objective = lambda v: .5*np.linalg.norm(A@v+residual)**2+.5*mu**2*(v@v)
    reference = minimize(objective, np.zeros(n), jac=lambda v: H@v+g,
        method='SLSQP', constraints=[LinearConstraint(C, -np.inf, bounds)],
        options=dict(ftol=1e-13, maxiter=1000))
    result = dict(source_sha256=hashlib.sha256(args.source.read_bytes()).hexdigest(),
        seed=2026112007, dimension=n, inequalities=m, damping=mu,
        independent_solver='scipy SLSQP dense original QP',
        reference_success=bool(reference.success), reference_message=str(reference.message),
        objective_relative_difference=abs(objective(z)-objective(reference.x))/max(1., abs(objective(reference.x))),
        solution_relative_difference=float(np.linalg.norm(z-reference.x)/max(1., np.linalg.norm(reference.x))),
        maximum_actual_violation=float(np.max(C@z-bounds)),
        qp={k: report[k] for k in ['status', 'advances', 'final_face_projected_gradient_norm',
            'minimum_multiplier', 'maximum_complementarity_residual', 'maximum_active_face_rank', 'active_face']},
        released_rows=sum(v['kind']=='release_negative_multiplier' for v in report['transitions']),
        new_field_solve_performed=False)
    result['passed'] = bool(reference.success and result['objective_relative_difference']<1e-10
        and result['maximum_actual_violation']<2e-10
        and report['final_face_projected_gradient_norm']<1e-7
        and report['minimum_multiplier']>-1e-9)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
