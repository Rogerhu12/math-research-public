#!/usr/bin/env python3
"""Exact bounded int64 linear algebra over (Z/47^4)[i]/(i^2+1).

Every matrix product has inner dimension at most820.  Inputs are reduced
before multiplication: 2*820*(47**4-1)**2 < 4*10**16 < 2**63.
Thus all NumPy int64 accumulations are exact integers; no floating arithmetic.
"""
import numpy as np

P = 47
Q = P**4
assert 2*820*(Q-1)**2 < 4*10**16 < 2**63


def from_json(data, q=Q):
    array = np.asarray(data, dtype=np.int64)
    assert array.ndim == 3 and array.shape[-1] == 2
    return array[:, :, 0].copy() % q, array[:, :, 1].copy() % q


def column(data, q=Q):
    return from_json([[c] for c in data], q)


def to_json(A):
    return np.stack(A, axis=-1).tolist()


def zeros(n, m):
    return np.zeros((n, m), dtype=np.int64), np.zeros((n, m), dtype=np.int64)


def eye(n):
    return np.eye(n, dtype=np.int64), np.zeros((n, n), dtype=np.int64)


def equal(A, B):
    return np.array_equal(A[0], B[0]) and np.array_equal(A[1], B[1])


def iszero(A):
    return not np.any(A[0]) and not np.any(A[1])


def add(A, B, q=Q):
    return (A[0]+B[0]) % q, (A[1]+B[1]) % q


def sub(A, B, q=Q):
    return (A[0]-B[0]) % q, (A[1]-B[1]) % q


def neg(A, q=Q):
    return -A[0] % q, -A[1] % q


def conjugate(A, q=Q):
    return A[0].copy(), -A[1] % q


def mul(A, B, q=Q):
    return (A[0]*B[0]-A[1]*B[1]) % q, (A[0]*B[1]+A[1]*B[0]) % q


def mm(A, B, q=Q):
    assert A[0].shape[1] == B[0].shape[0] <= 820 and 1 <= q <= Q
    assert all(np.all((x >= 0) & (x < q)) for x in A+B)
    return (A[0]@B[0]-A[1]@B[1]) % q, (A[0]@B[1]+A[1]@B[0]) % q


def units(A):
    return ((A[0] % P)**2+(A[1] % P)**2) % P != 0


def inverse_values(A, q=Q):
    norm = (A[0]*A[0]+A[1]*A[1]) % q
    inverses = np.asarray([pow(int(x), -1, q) for x in norm.flat], dtype=np.int64).reshape(norm.shape)
    return A[0]*inverses % q, -A[1]*inverses % q


def rows(A, indices):
    return A[0][indices].copy(), A[1][indices].copy()


def cols(A, indices):
    return A[0][:, indices].copy(), A[1][:, indices].copy()


def hcat(*matrices):
    return np.concatenate([A[0] for A in matrices], axis=1), np.concatenate([A[1] for A in matrices], axis=1)


def rank_pivots(A):
    """Return original row and column indices of a unit minor modulo47."""
    ar, ai = (x.copy() % P for x in A)
    m, n = ar.shape
    order = np.arange(m)
    selected_rows, selected_cols = [], []
    r = 0
    for c in range(n):
        candidates = np.flatnonzero((ar[r:, c]**2+ai[r:, c]**2) % P)
        if not len(candidates):
            continue
        pivot = r+int(candidates[0])
        if pivot != r:
            ar[[r, pivot]], ai[[r, pivot]] = ar[[pivot, r]], ai[[pivot, r]]
            order[[r, pivot]] = order[[pivot, r]]
        selected_rows.append(int(order[r]))
        selected_cols.append(c)
        a, b = int(ar[r, c]), int(ai[r, c])
        inverse = pow((a*a+b*b) % P, -1, P)
        ir, ii = a*inverse % P, -b*inverse % P
        pr = (ar[r, c:]*ir-ai[r, c:]*ii) % P
        pi = (ar[r, c:]*ii+ai[r, c:]*ir) % P
        vr, vi = ar[r+1:, c].copy()[:, None], ai[r+1:, c].copy()[:, None]
        ar[r+1:, c:] = (ar[r+1:, c:]-vr*pr+vi*pi) % P
        ai[r+1:, c:] = (ai[r+1:, c:]-vr*pi-vi*pr) % P
        r += 1
        if r == m:
            break
    return selected_rows, selected_cols


def inverse_matrix(A, q=Q):
    n = A[0].shape[0]
    assert A[0].shape == (n, n)
    ar = np.concatenate([A[0] % P, np.eye(n, dtype=np.int64)], axis=1)
    ai = np.concatenate([A[1] % P, np.zeros((n, n), dtype=np.int64)], axis=1)
    for k in range(n):
        candidates = np.flatnonzero((ar[k:, k]**2+ai[k:, k]**2) % P)
        assert len(candidates), ('matrix not a unit', k)
        pivot = k+int(candidates[0])
        if pivot != k:
            ar[[k, pivot]], ai[[k, pivot]] = ar[[pivot, k]], ai[[pivot, k]]
        a, b = int(ar[k, k]), int(ai[k, k])
        inverse = pow((a*a+b*b) % P, -1, P)
        ir, ii = a*inverse % P, -b*inverse % P
        pr = (ar[k]*ir-ai[k]*ii) % P
        pi = (ar[k]*ii+ai[k]*ir) % P
        ar[k], ai[k] = pr, pi
        vr, vi = ar[:, k].copy()[:, None], ai[:, k].copy()[:, None]
        vr[k], vi[k] = 0, 0
        ar = (ar-vr*pr+vi*pi) % P
        ai = (ai-vr*pi-vi*pr) % P
    assert np.array_equal(ar[:, :n], np.eye(n, dtype=np.int64)) and not np.any(ai[:, :n])
    C = ar[:, n:], ai[:, n:]
    if q != P:
        for _ in range(2):
            C = mm(C, sub(add(eye(n), eye(n), q), mm(A, C, q), q), q)
    assert equal(mm(A, C, q), eye(n))
    return C


def kernel_from_rows(R, pivot_rows, pivot_cols, q=Q):
    """R has only the selected rows; its original row indices are recorded."""
    n = R[0].shape[1]
    assert len(pivot_rows) == len(pivot_cols) == R[0].shape[0]
    free = [k for k in range(n) if k not in set(pivot_cols)]
    inverse = inverse_matrix(cols(R, pivot_cols), q)
    block = neg(mm(inverse, cols(R, free), q), q)
    K = zeros(n, len(free))
    for r in range(2):
        K[r][pivot_cols] = block[r]
        K[r][free] = eye(len(free))[r]
    assert iszero(mm(R, K, q))
    return K, free, block


def normalize(A, expected_rank, q=Q):
    rr, cc = rank_pivots(A)
    assert len(rr) == expected_rank, (len(rr), expected_rank)
    V = cols(A, cc)
    C = inverse_matrix(rows(V, rr), q)
    W = mm(V, C, q)
    assert equal(rows(W, rr), eye(expected_rank))
    return W, rr, cc, C


def rational_trace(A, rng, q=Q):
    n = A[0].shape[0]
    seed = column([[rng.randrange(P), rng.randrange(P)] for _ in range(n)], q)
    return seed, add(seed, mm(A, conjugate(seed, q), q), q)
