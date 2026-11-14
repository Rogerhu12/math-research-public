"""Verify cubic-weight innovation against full physical inverses, exactly."""

import importlib.util
from pathlib import Path
import sympy as sp

source = Path(__file__).with_name('2026-11-14-one-bit-schur-789f-next.py')
spec = importlib.util.spec_from_file_location('one_bit_schur_789f', source)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def exact_case(weights, s):
    weights = tuple(map(sp.Rational, weights))
    m = len(weights)
    h = m + 1 - 2 * s
    d = base.incidence(weights, s - 1, 1)
    X = base.kernel_basis(d)
    Y = base.kernel_basis(base.incidence(weights, s - 2, 1)) if s >= 2 else sp.ones(1, 1)
    R = d.T * (d * d.T).inv() * Y
    G, L, T = [], [], []
    for j in range(h):
        A = base.incidence(weights, s, j)
        F_inv = (A * A.T).inv()
        g = X.T * F_inv * X
        G.append(g)
        T.append(g.inv() * X.T * F_inv * R)
    for j in range(h + 2):
        A = base.incidence(weights, s - 1, j)
        L.append(Y.T * (A * A.T).inv() * Y)
    A = base.incidence(weights, s, h)
    U_R = R - A * (d * A).inv() * Y
    T.append((X.T * X).inv() * X.T * U_R)
    Q = [T[0]] + [(j + 1) * T[j] - j * T[j - 1] for j in range(1, h + 1)]

    cubic = base.incidence(tuple(w**3 for w in weights), s - 1, 1)
    B = (Y.T * Y).inv() * Y.T * cubic * X
    assert cubic * X == Y * B
    for j in range(1, h + 1):
        formula = G[j - 1].inv() * B.T * L[j + 1]
        if j >= 2:
            formula -= G[j - 2].inv() * B.T * L[j]
        formula /= j
        assert Q[j] - Q[j - 1] == formula, (weights, s, j)
    return h


if __name__ == '__main__':
    count = sum(exact_case(w, s) for w, s in [
        ((2, 3, 5), 1),
        ((1, 2, 3, 4), 1),
        ((1, 2, 1, 3, 2), 2),
        ((1, 2, 3, 2, 1, 2), 2),
    ])
    print(f'PASS cubic innovation from complete physical inverse: {count}')
    print('Includes all highest-layer hard constraints and two source births.')
    print('No adjacent-positivity conclusion is inferred.')
