#!/usr/bin/env python3
"""Actions-only necessary checks for the new early-release QP source.

This reuses only the already declared seed-2026112007, 32-variable,
28-inequality QP and its independent SLSQP comparison.  No additional fixture
is introduced.  This v2 checker has not been executed locally.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import minimize, LinearConstraint
from scipy.sparse.linalg import aslinearoperator


def load(path):
    spec = importlib.util.spec_from_file_location('checked_early_release_qp', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def compact_qp(report):
    result = {key: report[key] for key in (
        'status', 'advances', 'final_face_projected_gradient_norm',
        'minimum_multiplier', 'maximum_complementarity_residual',
        'maximum_active_face_rank', 'active_face')}
    result['release_event_count'] = sum(
        value['kind'].startswith('release_negative_multiplier') for value in report['transitions'])
    result['early_releases'] = [value for value in report['transitions']
                               if value['kind'] == 'release_negative_multiplier_early']
    return result


def random_case(module):
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
    gap = abs(objective(z)-objective(reference.x))/max(1., abs(objective(reference.x)))
    violation = float(np.max(C@z-bounds))
    return dict(name='original_random_QP_for_changed_algorithm', seed=2026112007,
        reference_success=bool(reference.success), relative_objective_difference=gap,
        maximum_literal_violation=violation, qp=compact_qp(report),
        passed=bool(reference.success and gap<1e-10 and violation<2e-10))



def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Do not overwrite a completed check')
    module = load(args.source)
    result = dict(schema='early-release-QP-necessary-checks-v2',
        source_sha256=hashlib.sha256(args.source.read_bytes()).hexdigest(),
        checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        cases=[random_case(module)],
        new_field_solve_performed=False,
        new_fixture_added=False,
        original_problem='The unchanged 32 x 28 case with seed 2026112007')
    result['passed'] = all(case['passed'] for case in result['cases'])
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result), flush=True)
    if not result['passed']:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
