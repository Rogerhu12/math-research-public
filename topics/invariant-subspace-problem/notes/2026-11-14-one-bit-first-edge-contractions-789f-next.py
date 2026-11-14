"""Small directed probes of two stronger one-bit first-edge conditions.

Uses full ordinary Boolean layers and orthonormal primitive sources.
Finite floating-point evidence only; no claim of general positivity.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
from functools import lru_cache
from itertools import combinations
import numpy as np
from scipy.linalg import eigvalsh, null_space, solve


@lru_cache(None)
def subsets(m, s):
    return tuple(map(frozenset, combinations(range(m), s)))


def incidence(weights, s, j):
    rows, cols = subsets(len(weights), s), subsets(len(weights), s+j)
    out = np.zeros((len(rows), len(cols)))
    for k, target in enumerate(cols):
        for i, source in enumerate(rows):
            if source <= target:
                out[i, k] = np.prod([weights[v] for v in target-source])
    return out


def inverse(matrix):
    return solve(matrix, np.eye(len(matrix)), assume_a="pos")


def gram(weights, birth, height, source):
    matrix = incidence(weights, birth, height)
    return source.T @ solve(matrix @ matrix.T, source, assume_a="pos")


def probe(weights, birth):
    weights = np.asarray(weights, dtype=float)
    old_height = len(weights)-2*birth
    assert old_height >= 1
    upper = null_space(incidence(weights, birth-1, 1))
    lower = (null_space(incidence(weights, birth-2, 1)) if birth >= 2
             else np.ones((1, 1)))
    g1 = gram(weights, birth, 1, upper)
    c1 = inverse(g1)
    c2 = (inverse(gram(weights, birth, 2, upper)) if old_height >= 2
          else np.zeros_like(c1))
    l1, l2, l3 = [gram(weights, birth-1, j, lower) for j in (1, 2, 3)]
    bridge = lower.T @ incidence(weights**3, birth-1, 1) @ upper
    q = bridge.T @ l2
    delta = (c1 @ bridge.T @ l3-q)/2
    a = c1 @ q-delta @ solve(l3, l2, assume_a="pos")
    defect = c1 @ c1-c2
    rho1 = eigvalsh(delta @ solve(l3, delta.T, assume_a="pos"), defect)[-1]
    rho2 = eigvalsh(a.T @ g1 @ a+l1 @ solve(l2, l1, assume_a="pos"))[-1]
    return tuple(float(x) for x in (rho1, rho2, np.linalg.cond(g1)))


if __name__ == "__main__":
    for ratio in (3., 10., 30.):
        cases = (
            ("five", [1., ratio, ratio, ratio, ratio**2], 2),
            ("six", [1., ratio, ratio, ratio, ratio, ratio**2], 2),
            ("seven-a", [1., ratio, ratio, ratio, ratio, ratio, ratio**2], 3),
            ("seven-b", [1., 1., ratio, ratio, ratio, ratio, ratio], 3),
        )
        for name, weights, birth in cases:
            print(name, ratio, probe(weights, birth), flush=True)
