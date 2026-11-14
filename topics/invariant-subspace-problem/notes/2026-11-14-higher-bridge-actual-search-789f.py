"""Bounded exploration of the true strengthened heavy-bit limit matrices.

Finite floating samples are not a proof of either universal inequality.
Every Gram is the inverse of the complete physical layer, followed by one
common primitive compression.  Candidate violations require exact follow-up.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import time
import numpy as np
from scipy import linalg

HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location(
    'actual_boolean', HERE/'2026-11-14-full-boolean-adjacent-search-789f.py')
physical = importlib.util.module_from_spec(spec)
spec.loader.exec_module(physical)


def elementary_four(weights):
    values = np.zeros(5)
    values[0] = 1.0
    for value in weights*weights:
        for degree in range(4, 0, -1):
            values[degree] += value*values[degree-1]
    return values


def evaluate(input_weights):
    weights, source, gram, conditions, residual, _ = physical.actual_grams(
        input_weights, 1, last=3)
    dimension = source.shape[1]
    gram_conditions = [float(np.linalg.cond(g)) for g in gram]
    if max(conditions) > 1e5 or max(gram_conditions) > 1e9:
        return None
    c1, c2, c3 = [linalg.solve(g, np.eye(dimension), assume_a='pos')
                  for g in gram[1:4]]
    bridge = source.T@(weights**3)
    e = elementary_four(weights)
    delta3 = (c2@bridge/e[4]-c1@bridge/e[3])/3
    left = c2@gram[1]@c2
    right = c3+e[4]*np.outer(delta3, delta3)
    left, right = (left+left.T)/2, (right+right.T)/2
    s1_ratio = float(linalg.eigh(right, left, subset_by_index=(dimension-1, dimension-1),
                               eigvals_only=True)[0])
    kappa = gram[1]@c2@gram[1]
    kappa = (kappa+kappa.T)/2
    main_column = (kappa@c1@bridge/e[3]-3*kappa@bridge/e[2]
                   +2*bridge*e[4]/e[3]**2)/6
    low_defect = 1/e[1]-e[3]/e[2]**2
    product = kappa@(np.eye(dimension)-kappa)
    product = (product+product.T)/2
    # Schur of [[I-K,-M],[-M*,D-M*K^-1M]] uses
    # K^-1+(I-K)^-1=[K(I-K)]^-1, with the same physical metric.
    s2_ratio = float(main_column@linalg.solve(product, main_column, assume_a='pos')/low_defect)
    return {'s1_ratio': s1_ratio, 's2_ratio': s2_ratio,
            'weights': np.asarray(input_weights).tolist(),
            'incidence_conditions': conditions, 'gram_conditions': gram_conditions,
            'primitive_residual': float(residual)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--samples', type=int, default=100)
    parser.add_argument('--seed', type=int, default=202611148)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    rng = np.random.default_rng(args.seed)
    started = time.monotonic()
    report = {'status': 'floating_exploration_only', 'seed': args.seed,
              'samples_per_dimension': args.samples, 'random_weights': '2**uniform_integer(0,5)',
              'scope': 'Actual birth-one second-height strengthened S1 and heavy-bit S2 limit; finite samples do not prove universality.',
              'cases': []}
    for n in (5, 6, 7, 8, 10):
        samples = [np.ones(n), np.r_[8., np.ones(n-1)],
                   np.r_[8., 8., np.ones(n-2)], np.arange(1, n+1, dtype=float)]
        samples += [2.**rng.integers(0, 6, size=n) for _ in range(args.samples)]
        maxima = {key: None for key in ('s1_ratio', 's2_ratio')}
        accepted = flagged = 0
        candidates = []
        for weights in samples:
            try:
                row = evaluate(weights)
            except (ValueError, linalg.LinAlgError):
                row = None
            if row is None:
                flagged += 1
                continue
            accepted += 1
            for key in maxima:
                if maxima[key] is None or row[key] > maxima[key][key]:
                    maxima[key] = row
            if row['s1_ratio'] > 1+1e-6 or row['s2_ratio'] > 1+1e-6:
                candidates.append(row)
        case = {'N': n, 'accepted': accepted, 'flagged': flagged,
                'maxima': maxima, 'candidate_violations_not_certified': candidates}
        report['cases'].append(case)
        print(json.dumps(case), flush=True)
        args.output.write_text(json.dumps(report, indent=2)+'\n')
    report['elapsed_seconds'] = time.monotonic()-started
    report['complete'] = True
    args.output.write_text(json.dumps(report, indent=2)+'\n')


if __name__ == '__main__':
    main()
