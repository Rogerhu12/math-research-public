"""Exact recovery of the four-channel / one-nuisance Gram identity.

This checks equality against the complete physical-layer inverse.  It does
not test or assert the adjacent Gram inequality.  All arithmetic is rational.
Run from any directory: python this_file.py [--quick].
"""

from functools import lru_cache
from math import comb, factorial
import argparse
import sympy as sp


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def basis(q, pool, level):
    return [(r, b, c, level-r-b-c)
            for r in range(q+1) for b in (0, 1) for c in (0, 1)
            if 0 <= level-r-b-c <= pool]


def incidence(q, pool, level, power, a, u, v):
    out = basis(q, pool, level)
    src = basis(q, pool, level+power)
    amplitudes = (a, u, v, sp.S.One)
    sizes = (q, 1, 1, pool)

    def entry(o, x):
        gaps = [x[i]-o[i] for i in range(4)]
        if min(gaps) < 0 or sum(gaps) != power:
            return sp.S.Zero
        return sp.prod(amplitudes[i]**gaps[i]
                       * choose(sizes[i]-o[i], gaps[i]) for i in range(4))

    return sp.Matrix([[entry(o, x) for x in src] for o in out]), src


def source(q, pool, birth, a, u, v):
    d = q+2-birth
    rows = []
    for r, b, c, ell in basis(q, pool, birth):
        rr, yy, zz = q-r, 1-b, 1-c
        scale = ((-1)**ell * a**rr * u**yy * v**zz
                 / sp.Integer(choose(pool, ell)))
        values = [factorial(d)*choose(rr, d),
                  factorial(d-1)*yy*choose(rr, d-1),
                  factorial(d-1)*zz*choose(rr, d-1),
                  factorial(d-2)*yy*zz*choose(rr, d-2)]
        if birth == 1:
            values = values[1:]
        rows.append([scale*x for x in values])
    return sp.Matrix(rows)


def full_gram(q, pool, birth, n, a, u, v):
    E = source(q, pool, birth, a, u, v)
    D, _ = incidence(q, pool, birth-1, 1, a, u, v)
    assert D*E == sp.zeros(D.rows, E.cols)
    assert E.rank() == (3 if birth == 1 else 4)
    A, src = incidence(q, pool, birth, n, a, u, v)
    wi = sp.diag(*[sp.Rational(1, choose(q, r)*choose(pool, ell))
                   for r, _, _, ell in src])
    whole = A*wi*A.T
    return E.T*whole.inv()*E


@lru_cache(maxsize=None)
def monic(q, pool, d, j, degree, z):
    """Norm and top two coefficients with ALL illegal grid roots imposed.

    None means a monic polynomial of this degree is infeasible, not an
    infinite matrix coefficient.  The fixed root polynomial is built first.
    """
    x = sp.Symbol('x')
    legal = [r for r in range(q+1) if 0 <= j+r-d <= pool]
    illegal = [r for r in range(q+1) if r not in legal]
    if degree < len(illegal) or not legal:
        return None
    root = sp.Poly(sp.prod(x-r for r in illegal), x)
    k = degree-len(illegal)
    if k >= len(legal):
        raise ValueError('degree exceeds the unique grid interpolation range')
    ww = [sp.Rational(choose(q, r), choose(pool, j+r-d))
          * z**r * root.eval(r)**2 for r in legal]
    moments = [sum(w*r**ell for w, r in zip(ww, legal))
               for ell in range(2*k+1)]
    if k:
        G = sp.Matrix(k, k, lambda i, j: moments[i+j])
        rhs = sp.Matrix([moments[k+i] for i in range(k)])
        low = -G.inv()*rhs
        pol = root*sp.Poly(x**k+sum(low[i]*x**i for i in range(k)), x)
        norm = moments[2*k]+(rhs.T*low)[0]
    else:
        pol, norm = root, moments[0]
    assert norm > 0
    sub = pol.nth(degree-1) if degree >= 1 else sp.S.Zero
    second = pol.nth(degree-2) if degree >= 2 else sp.S.Zero
    return norm, sub, second


def reduced_gram(q, pool, birth, n, a, u, v):
    """Build 5x5 (or 4x4) Gram, then one exact Schur complement.

    At n=0,h the nuisance is fixed by the actual empty lower channel.
    """
    d, h = q+2-birth, q+pool+2-2*birth
    dim = 3 if birth == 1 else 4
    alpha = None if birth == 1 else 0
    beta, gamma, delta = (0, 1, 2) if birth == 1 else (1, 2, 3)
    nuisance = dim
    M = sp.zeros(dim+1)
    p, s, tau, aa, bb, cc = {}, {}, {}, {}, {}, {}
    for j in range(n, n+3):
        hi = None if birth == 1 else monic(q, pool, d, j, d, a*a)
        mid = monic(q, pool, d, j, d-1, a*a)
        lo = monic(q, pool, d, j, d-2, a*a)
        aa[j], p[j], s[j] = hi if hi is not None else (0, 0, 0)
        bb[j], tau[j] = (mid[0], mid[1]) if mid is not None else (None, 0)
        cc[j] = lo[0] if lo is not None else None
    denom = sp.S.Zero
    slots = [(0, 0, sp.S.One), (1, 0, u*u),
             (0, 1, v*v), (1, 1, u*u*v*v)]
    for yy, zz, weight in slots:
        j = n+yy+zz
        if alpha is not None:
            M[alpha, alpha] += weight*aa[j]
        if bb[j] is not None:
            row = sp.zeros(1, dim+1)
            row[0, nuisance] = 1
            row[0, beta], row[0, gamma] = yy, zz
            if alpha is not None:
                row[0, alpha] = -p[j]
            M += weight*bb[j]*(row.T*row)
        if cc[j] is not None:
            denom += 1/(weight*cc[j])
    assert denom > 0
    second_difference = lambda f: f[n]-2*f[n+1]+f[n+2]
    row = sp.zeros(1, dim+1)
    row[0, delta] = 1
    row[0, nuisance] = -second_difference(tau)
    row[0, beta] = row[0, gamma] = -(tau[n+2]-tau[n+1])
    if alpha is not None:
        aterm = {j: s[j]-tau[j]*p[j] for j in range(n, n+3)}
        row[0, alpha] = -second_difference(aterm)
    M += (row.T*row)/denom
    if n in (0, h):
        # At n=0: x=alpha*p_0.  At n=h: x=alpha*p_(h+2)-beta-gamma.
        P = sp.eye(dim).col_join(sp.zeros(1, dim))
        if alpha is not None:
            P[dim, alpha] = p[0] if n == 0 else p[h+2]
        if n == h:
            P[dim, beta] = P[dim, gamma] = -1
        return P.T*M*P
    assert M[nuisance, nuisance] > 0
    b = M[:dim, nuisance]
    return M[:dim, :dim]-(b*b.T)/M[nuisance, nuisance]


def check_case(case):
    q, pool, birth, n, a, u, v = case
    a, u, v = map(sp.Rational, (a, u, v))
    actual = full_gram(q, pool, birth, n, a, u, v)
    recovered = reduced_gram(q, pool, birth, n, a, u, v)
    assert actual == recovered, case


def cases(quick=False):
    weights = [(2, 3, 5), (sp.Rational(1, 2), 2, sp.Rational(3, 2))]
    if quick:
        first_pairs, general = [(1, 1), (2, 1)], [(2, 2, 2), (3, 2, 2)]
    else:
        first_pairs = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1),
                       (1, 3), (2, 3), (3, 2), (3, 3), (4, 1)]
        general = [(2, 2, 2), (3, 2, 2), (2, 3, 2),
                   (3, 3, 2), (3, 3, 3), (4, 3, 3)]
    for q, pool in first_pairs:
        for amplitudes in weights:
            for n in range(q+pool+1):
                yield (q, pool, 1, n, *amplitudes)
    for q, pool, birth in general:
        for amplitudes in weights:
            for n in range(q+pool+3-2*birth):
                yield (q, pool, birth, n, *amplitudes)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--quick', action='store_true')
    args = parser.parse_args()
    first = general = 0
    for case in cases(args.quick):
        check_case(case)
        if case[2] == 1:
            first += 1
        else:
            general += 1
    print(f'PASS exact complete-layer Gram identities: birth-one={first}, general={general}')
    print('Includes all endpoint heights, unequal exceptional weights, and q > pool.')
    print('No adjacent-positivity claim is tested or made.')
