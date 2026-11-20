#!/usr/bin/env python3
"""One small-model check of the new arbitrary-stage map and repeated scatter.

This checks new implementation risks only; no production warm, nonlinear
solve, old dense large probe, or continuous geometry audit is evaluated.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def relative(a, b):
    return float(np.linalg.norm(a-b)/max(1., np.linalg.norm(a), np.linalg.norm(b)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--module', type=Path, required=True)
    parser.add_argument('--batch', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    topic = args.repo/'topics/visible-flex-larger-amplitude'
    dense = topic/'notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py'
    module = load('check_observation_module', args.module)
    batch = load('check_observation_batch', args.batch)
    mesh = np.array([0., .17, .43, .8, 1., 1.2])
    plan = module.make_plan(mesh, .3, order=6)
    a = 1-.2*plan.times
    original = batch.create(dense, mesh, a[:plan.legacy_count], float(a[plan.legacy_count-1]),
                            np.array([-.002]), M=3, N=32, width=.3, quarter=True, stage_block=7)
    observed = module.create(dense, mesh, a[:plan.legacy_count], float(a[plan.legacy_count-1]),
        np.array([-.002]), M=3, N=32, width=.3, quarter=True, stage_block=7,
        batch_source=batch, observation_plan=plan, a_observations=a)
    rng = np.random.default_rng(20261120)
    x = rng.normal(size=observed.free_size)*.002
    x[-1] = .6
    direction = rng.normal(size=x.size)*.01
    weights = rng.normal(size=(observed.P, observed.N, 3))
    r = observed.residual(x)
    jv = observed.jvp(x, direction)
    cs = observed.residual(x+1e-30j*direction).imag/1e-30
    adjoint = observed.vjp(x, weights)
    lhs, rhs = float(np.sum(weights*jv)), float(direction@adjoint)
    errors = dict(legacy_rows_relative=relative(r[:observed.legacy_P], original.residual(x)),
        complex_step_relative=relative(jv, cs),
        adjoint_relative=abs(lhs-rhs)/max(1., abs(lhs), abs(rhs)))
    prepared = observed.prepare(x)
    new = observed.physical_jet_batch(prepared, 0, observed.P)
    for key in new:
        old = np.array([observed.six_jets(prepared, stage)[key] for stage in range(observed.P)])
        errors['batched_'+key+'_relative'] = relative(new[key], old)
    coefficients = np.array([.3, -.1, .25, .7, -.2, .05])
    jets = np.zeros_like(prepared.jets)
    expected = np.empty((observed.P, 3))
    for order in range(3):
        c = np.polynomial.polynomial.polyder(coefficients, m=order)
        jets[:, order, 0] = np.polynomial.polynomial.polyval(mesh, c)
        expected[:, order] = np.polynomial.polynomial.polyval(plan.times, c)
    errors['complete_quintic_three_jet_relative'] = relative(observed._stage_all(jets, 0, observed.P)[:, :, 0], expected)
    result = dict(schema='new-Gauss-stage-map-small-check-20261120-v1',
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        module_sha256=hashlib.sha256(args.module.read_bytes()).hexdigest(),
        J=len(mesh), M=3, N=32, old_stages=original.P, new_stages=observed.P,
        pieces=len(plan.piece_cells), includes_actual_break_inside_cell=True,
        all_affine_variables_and_core_height_in_direction=True,
        repeated_cell_scatter_exercised=True, seed=20261120, errors=errors,
        passed=all(value < 2e-11 for value in errors.values()),
        production_warm_calls=0, nonlinear_solves=0, geometry_audits=0)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    if not result['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
