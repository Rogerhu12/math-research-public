"""Exact independent full-incidence normalization checks for phase curvature.

The all-size proof is in the companion Markdown.  These two computations are
not a sampling proof: they verify the claimed coefficient using full first and
second inverse Grams and the original physical source metric.
"""

import argparse
import json
import resource
from itertools import combinations
from pathlib import Path

import sympy as q


def check(n, xs):
    assert n % 2 == 0 and len(xs) == n and sum(xs) == 0
    s, j = n//2, n//2-1

    def subsets(k):
        return list(combinations(range(n), k))

    def incidence(k, power=1, weights=None):
        weights = weights or [1]*n
        return q.Matrix([[q.prod(weights[i] for i in set(I)-set(J))
                          if set(J) <= set(I) else 0
                          for I in subsets(k)] for J in subsets(k-power)])

    def diagonal_series(k, inverse=False):
        sums = [sum(xs[i] for i in I) for I in subsets(k)]
        squares = [sum(xs[i]**2 for i in I) for I in subsets(k)]
        return [q.eye(len(sums)), q.diag(*[(-x if inverse else x) for x in sums]),
                q.diag(*[q.Rational(1, 2)*(x*x+(y if inverse else -y))
                         for x, y in zip(sums, squares)])]

    def add(a, b):
        return [a[i]+b[i] for i in range(3)]

    def scale(a, scalar):
        return [x*scalar for x in a]

    def multiply(*args):
        a = args[0]
        for b in args[1:]:
            a = [sum((a[k]*b[r-k] for k in range(r+1)),
                     q.zeros(a[0].rows, b[0].cols)) for r in range(3)]
        return a

    def inverse(a):
        b = a[0].inv()
        return [b, -b*a[1]*b, b*a[1]*b*a[1]*b-b*a[2]*b]

    def transpose(a):
        return [x.T for x in a]

    E = q.Matrix.hstack(*incidence(j).nullspace())
    H = [E.T*x*E for x in diagonal_series(j, True)]
    Hi = inverse(H)
    grams = []
    for power in (1, 2):
        A = incidence(j+power, power)
        F = [A*x*A.T for x in diagonal_series(j+power)]
        grams.append([E.T*x*E for x in inverse(F)])
    G, L = [multiply(Hi, x) for x in grams]
    C = inverse(G)
    ds = incidence(s)
    Qf = [E.T*ds*x*ds.T*E for x in diagonal_series(s, True)]
    Q = multiply(Hi, Qf)
    H0 = add(add(multiply(C, L), scale(G, 2)), scale(Q, -1))
    H0star = multiply(Hi, transpose(H0), H)
    phase = multiply(H0star, inverse(L), H0)
    assert phase[0] == q.eye(E.cols)
    assert phase[1] == q.zeros(E.cols)
    B = incidence(j, weights=xs)*E
    PU = q.eye(ds.cols)-ds.T*(ds*ds.T).inv()*ds
    Sx = PU*incidence(s, weights=xs).T*E
    target = H[0].inv()*(q.Rational(1, 4)*B.T*B+q.Rational(1, 2)*Sx.T*Sx)
    assert -phase[2] == target
    answer = {'N': n, 'source_dimension': E.cols, 'direction': xs,
              'exact_second_variation': True, 'quadratic_rank': target.rank()}
    print(json.dumps(answer, sort_keys=True), flush=True)
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU, (55, 60))
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
    results = [check(4, [-6, -2, 1, 7]), check(6, [-11, -7, -3, 1, 8, 12])]
    if args.output:
        args.output.write_text(json.dumps(results, indent=2)+'\n')


if __name__ == '__main__':
    main()
