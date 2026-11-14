"""Exact calibration of the complete one-bit primitive MP recursion.

The direct branch uses the full physical subset incidence matrix.  The
recursive branch uses two old births, a genuine Schur complement, and the
separate highest-layer range constraint.  No adjacent-positivity claim.
"""

from functools import lru_cache
from itertools import combinations
import sympy as sp


@lru_cache(None)
def layer(m, s):
    return tuple(combinations(range(m), s))


def incidence(weights, s, j):
    m = len(weights)
    rows, cols = layer(m, s), layer(m, s + j)
    mat = sp.zeros(len(rows), len(cols))
    for row, source in enumerate(rows):
        source = set(source)
        for col, target in enumerate(cols):
            target = set(target)
            if source <= target:
                mat[row, col] = sp.prod(weights[i] for i in target - source)
    return mat


def kernel_basis(mat):
    return sp.Matrix.hstack(*mat.nullspace())


def exact_case(weights, s, new_weight):
    weights = tuple(map(sp.Rational, weights))
    a = sp.Rational(new_weight)
    m = len(weights)
    h = m + 1 - 2 * s
    assert h >= 2
    d = incidence(weights, s - 1, 1)
    X = kernel_basis(d)
    Y = kernel_basis(incidence(weights, s - 2, 1)) if s >= 2 else sp.ones(1, 1)
    R = d.T * (d * d.T).inv() * Y
    assert d * X == sp.zeros(d.rows, X.cols)
    assert d * R == Y
    assert X.T * R == sp.zeros(X.cols, R.cols)

    G, T, L = [], [], []
    for j in range(h):
        A = incidence(weights, s, j)
        F_inv = (A * A.T).inv()
        g = X.T * F_inv * X
        G.append(g)
        T.append(g.inv() * X.T * F_inv * R)
    for j in range(h + 2):
        A = incidence(weights, s - 1, j)
        L.append(Y.T * (A * A.T).inv() * Y)

    A_top = incidence(weights, s, h)
    U_R = R - A_top * (d * A_top).inv() * Y
    assert d * U_R == sp.zeros(d.rows, U_R.cols)
    T_top = (X.T * X).inv() * X.T * U_R
    assert X * T_top == U_R
    T.append(T_top)
    Q = [T[0]] + [(j + 1) * T[j] - j * T[j - 1] for j in range(1, h + 1)]

    P = [G[0]]
    P += [(G[j].inv() + a * a * G[j - 1].inv()).inv() for j in range(1, h)]
    P += [G[h - 1] / (a * a)]
    V = [L[j] + a * a * L[j + 1] for j in range(h + 1)]
    recursive = []
    for p, q, v in zip(P, Q, V):
        upper_right = -a * p * q
        recursive.append(p.row_join(upper_right).col_join(
            upper_right.T.row_join(v + a * a * q.T * p * q)))

    all_weights = weights + (a,)
    E = sp.zeros(len(layer(m + 1, s)), X.cols + Y.cols)
    lookup_s = {v: i for i, v in enumerate(layer(m, s))}
    lookup_lower = {v: i for i, v in enumerate(layer(m, s - 1))}
    for row, subset in enumerate(layer(m + 1, s)):
        if m in subset:
            old_row = lookup_lower[tuple(i for i in subset if i != m)]
            E[row, X.cols:] = Y[old_row, :]
        else:
            old_row = lookup_s[subset]
            E[row, :X.cols] = X[old_row, :]
            E[row, X.cols:] = -a * R[old_row, :]
    D_new = incidence(all_weights, s - 1, 1)
    assert D_new * E == sp.zeros(D_new.rows, E.cols)
    assert E.rank() == E.cols
    for j in range(h + 1):
        A = incidence(all_weights, s, j)
        direct = E.T * (A * A.T).inv() * E
        assert direct == recursive[j], (weights, s, a, j)

    # Independently compare the common-shear defect with the actual new defect.
    for n in range(1, h):
        p_minus, p_zero, p_plus = P[n - 1:n + 2]
        v_minus, v_zero, v_plus = V[n - 1:n + 2]
        delta_minus = Q[n] - Q[n - 1]
        delta_plus = Q[n + 1] - Q[n]
        A0 = p_minus - p_zero * p_plus.inv() * p_zero
        B0 = v_minus - v_zero * v_plus.inv() * v_zero
        upper = A0 - a * a * p_zero * delta_plus * v_plus.inv() * delta_plus.T * p_zero
        cross = a * (p_minus * delta_minus - p_zero * delta_plus * v_plus.inv() * v_zero)
        lower = B0 + a * a * delta_minus.T * p_minus * delta_minus
        innovation = upper.row_join(cross).col_join(cross.T.row_join(lower))
        common = sp.eye(E.cols)
        common[:X.cols, X.cols:] = a * Q[n]
        actual = recursive[n - 1] - recursive[n] * recursive[n + 1].inv() * recursive[n]
        assert common.T * actual * common == innovation
    return h + 1, h - 1


def exact_shear_obstruction():
    r = sp.symbols('r', positive=True)
    z = r * r
    F1 = sp.Matrix([[2, r, r], [r, z + 1, 1], [r, 1, z + 1]])
    Q2 = (1 - z * z) / ((z + 2) * (2 * z + 1)) * sp.Matrix([-2 / r, 1, 1])
    v2 = 1 / (2 * z + 1) + 1 / z
    ratio = (Q2.T * F1.inv() * Q2)[0] / v2
    closed = 2 * (z * z - 1)**2 / ((z + 2)**2 * (3 * z + 1))
    assert sp.factor(ratio - closed) == 0
    assert sp.limit(closed / z, r, sp.oo) == sp.Rational(2, 3)


def main():
    cases = [
        ((2, 3, 5), 1, 7),
        ((1, 2, 3, 4), 1, sp.Rational(1, 2)),
        ((1, 2, 1, 3, 2), 2, 2),
        ((1, 2, 3, 2, 1, 2), 2, sp.Rational(3, 2)),
    ]
    gram_count = defect_count = 0
    for weights, s, a in cases:
        g, d = exact_case(weights, s, a)
        gram_count += g
        defect_count += d
    exact_shear_obstruction()
    print(f'PASS complete-layer one-bit identities: {gram_count}')
    print(f'PASS exact common-source innovation defects: {defect_count}')
    print('PASS symbolic actual Boolean unbounded single-height shear ratio')
    print('No universal adjacent-positivity claim is tested or made.')


if __name__ == '__main__':
    main()
