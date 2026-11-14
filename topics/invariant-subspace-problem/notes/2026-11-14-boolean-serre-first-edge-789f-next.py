"""Exact calibration of the birth-preserving Serre recurrence and its sum."""

import importlib.util
from pathlib import Path
import sympy as sp

source = Path(__file__).with_name('2026-11-14-one-bit-schur-789f-next.py')
spec = importlib.util.spec_from_file_location('one_bit_schur_789f', source)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def source_grams(weights, birth):
    m = len(weights)
    X = base.kernel_basis(base.incidence(weights, birth - 1, 1)) if birth else sp.ones(1, 1)
    grams = []
    for j in range(m - 2 * birth + 1):
        A = base.incidence(weights, birth, j)
        grams.append(X.T * (A * A.T).inv() * X)
    return X, grams


def exact_case(weights, birth):
    weights = tuple(map(sp.Rational, weights))
    length = len(weights) - 2 * birth
    assert birth >= 1 and length >= 2
    X, G = source_grams(weights, birth)
    Y, L = source_grams(weights, birth - 1)
    Z, higher = source_grams(weights, birth + 1)
    cubic_lower = base.incidence(tuple(w**3 for w in weights), birth - 1, 1)
    cubic_higher = base.incidence(tuple(w**3 for w in weights), birth, 1)
    B = L[0].inv() * Y.T * cubic_lower * X
    B_higher = G[0].inv() * X.T * cubic_higher * Z
    assert cubic_lower * X == Y * B
    assert cubic_higher * Z == X * B_higher
    zero = sp.zeros(X.cols, X.cols)
    A = [G[j + 1].inv() * G[j] for j in range(length)] + [zero]
    U = [G[j].inv() * B.T * L[j + 2] * B for j in range(length + 1)]
    V = [zero, zero] + [B_higher * higher[j - 2].inv() * B_higher.T * G[j]
                            for j in range(2, length + 1)]
    for k in range(2, length + 1):
        diagonal = (k + 1)**2 * A[k] - 3 * k*k * A[k - 1] + 3 * (k - 1)**2 * A[k - 2]
        if k >= 3:
            diagonal -= (k - 2)**2 * A[k - 3]
        upward = U[k] - sp.Rational(2 * (k - 1), k) * U[k - 1] + sp.Rational(k - 2, k) * U[k - 2]
        downward = -sp.Rational(k + 1, k - 1) * V[k] + sp.Rational(2 * k, k - 1) * V[k - 1] - V[k - 2]
        assert diagonal + upward + downward == zero, (weights, birth, k)
    integrated = sp.Rational(length - 1, 2 * length) * A[0]
    integrated -= sp.Rational(length - 1, 6 * length) * U[1]
    integrated += sp.Rational(length + 2, 2 * length) * sum(
        (U[j] / ((j + 1) * (j + 2)) for j in range(2, length + 1)), zero)
    integrated -= sum((V[j] / (2 * j * (j - 1)) for j in range(2, length + 1)), zero)
    assert A[1] == integrated, (weights, birth, 'integrated')
    return length - 1


def exact_weighted_trace(weights):
    weights = tuple(map(sp.Rational, weights))
    n = len(weights)
    data = [source_grams(weights, birth) for birth in range(n // 2 + 1)]
    left = right = sp.S(0)
    for birth, (X, G) in enumerate(data):
        length = n - 2 * birth
        if length >= 1:
            A0 = G[1].inv() * G[0]
            A1 = G[2].inv() * G[1] if length >= 2 else sp.zeros(X.cols)
            left += length * sp.trace(A1)
            right += sp.Rational(length - 1, 2) * sp.trace(A0)
        if birth:
            Y, L = data[birth - 1]
            cubic = base.incidence(tuple(w**3 for w in weights), birth - 1, 1)
            B = L[0].inv() * Y.T * cubic * X
            U0 = G[0].inv() * B.T * L[2] * B
            right -= sp.Rational(length + 2, 4) * sp.trace(U0)
            if length >= 1:
                U1 = G[1].inv() * B.T * L[3] * B
                right -= sp.Rational(length, 4) * sp.trace(U1)
    assert left == right


if __name__ == '__main__':
    cases = [((1, 2, 3, 5), 1), ((1, 2, 1, 3, 2), 1),
             ((1, 2, 3, 2, 1, 2), 2)]
    count = sum(exact_case(w, s) for w, s in cases)
    for weights in [(1, 2, 3, 5), (1, 2, 1, 3, 2)]:
        exact_weighted_trace(weights)
    print(f'PASS complete-Boolean birth-preserving Serre recurrences: {count}')
    print(f'PASS finite-top integrated first-edge identities: {len(cases)}')
    print('PASS weighted traces with even and odd top-birth boundaries: 2')
    print('No fixed-metric sign or universal adjacent bound is inferred.')
