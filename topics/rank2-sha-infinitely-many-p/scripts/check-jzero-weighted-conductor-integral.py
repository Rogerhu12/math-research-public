#!/usr/bin/env python3
"""R326: exact integer certificate for the original weighted conductor.

Requires python-flint. No floating point or prime sampling is used.
The three compressed parts contain every rational coefficient of the
1154 original homogeneous identities used by the degree-12 induction.
"""
from pathlib import Path
from fractions import Fraction
from functools import reduce
from math import gcd, lcm
import gzip
import json
from flint import fmpz_poly, fmpq_poly, fmpz_mat, fmpq_mat, fmpq

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'check-jzero-weighted-conductor-integral.json').read_text())
t = fmpz_poly([0, 1])
q7 = 16*t**2 + 4*t + 7
g2 = 8*t**2 + 20*t - 1
f3 = 64*t**3 - 48*t**2 + 228*t - 1
f4d = 1792*t**4 - 3136*t**3 + 2112*t**2 - 40*t + 1
f4 = 512*t**4 - 2048*t**3 + 1344*t**2 - 536*t - 1
f6 = 4096*t**6 - 33792*t**5 + 204288*t**4 - 47936*t**3 + 11040*t**2 + 84*t + 1
nf = 27*(4*t-1)**2*f3*f4d
df = t**2*(t-1)**2*(8*t+1)*q7**2
nh = -64*g2**2*f4*f6
dh = t**3*(t-1)*(8*t+1)**2*q7**3


def powers(n):
    return [(n-3*j-4*k, j, k)
            for k in range(n//4+1) for j in range((n-4*k)//3+1)]


def den(n):
    a, c, b = 3*n//4, 2*n//3, n//2
    return t**a*(t-1)**c*(8*t+1)**b*q7**a


def col(n, j, k):
    a, c, b = 3*n//4, 2*n//3, n//2
    assert min(a-2*j-3*k, c-2*j-k, b-j-2*k) >= 0
    return (nf**j*nh**k*t**(a-2*j-3*k)*(t-1)**(c-2*j-k)
            *(8*t+1)**(b-j-2*k)*q7**(a-2*j-3*k))


def matrix(n):
    mons = powers(n)
    cols = [col(n, j, k) for i, j, k in mons]
    length = den(n).degree() + n//2 + 1
    return mons, cols, fmpz_mat([[p[r] for p in cols] for r in range(length)])


def only_two_three(value):
    for prime in (2, 3):
        while value % prime == 0:
            value //= prime
    return value == 1


assert nf.gcd(df).degree() == nh.gcd(dh).degree() == 0
assert (nf.degree(), df.degree(), nh.degree(), dh.degree()) == (9, 9, 14, 12)
mons47, cols47, m47 = matrix(47)
assert [list(v) for v in mons47] == DATA['relation_monomials']
fc = [int(v) for v in DATA['relation_coefficients']]
assert reduce(gcd, fc) == 1
assert sum((v*p for v, p in zip(fc, cols47)), fmpz_poly()) == 0
assert len([v for v in fc if v]) == 96

# Residue formula P_h(f,h)/f'(t), evaluated without symbolic resultants.
ph = sum((v*k*col(43, j, k-1)
          for (i, j, k), v in zip(mons47, fc) if k and v), fmpz_poly())
fp = nf.derivative()*df - nf*df.derivative()
kn, kd = ph*df**2, den(43)*fp
common = kn.gcd(kd)
kn, kd = kn//common, kd//common
assert [str(v) for v in kn] == DATA['kappa_numerator']
assert [str(v) for v in kd] == DATA['kappa_denominator']
raw = fmpq_poly([fmpq(v) for v in DATA['conductor_numerator']])
Q = t*(t-1)*(8*t+1)*q7
assert raw*fmpq_poly(kd*Q) == fmpq_poly(den(40)*kn)
scaled = raw*fmpq(DATA['scale'])
assert all(v.denominator == 1 for v in scaled)
N = fmpz_poly([int(v) for v in scaled])
assert N.degree() == 147
assert reduce(gcd, (int(v) for v in N)) == 1
assert next(i for i, v in enumerate(N) if v) == 3
assert N[3] == 3**4*7**3*3159421

# An integral base-point-free degree-12 pencil.
P = den(12)
Q12 = col(12, 4, 0) + col(12, 0, 3)
assert P.resultant(Q12) == -2**2538*3**2275
assert Q12.degree() == 47 and Q12[47] == -2**99

total = 0
all_den = 1
seen = []
for name in DATA['parts']:
    with gzip.open(ROOT/name, 'rt') as stream:
        part = json.load(stream)
    for row in part['rows']:
        m = row['m']
        seen.append(m)
        n = 40+m
        mons, cols, mm = matrix(n)
        assert [list(v) for v in mons] == row['monomials']
        ratio, remainder = divmod(den(n), den(40)*den(m))
        assert not remainder
        count = den(m).degree() + m//2 + 5
        assert count == row['targets'] == len(row['solutions'])
        targets = [N*ratio*t**j for j in range(count)]
        sol = fmpq_mat([[fmpq(row['solutions'][j][r]) for j in range(count)]
                        for r in range(len(mons))])
        target_matrix = fmpq_mat([[v[r] for v in targets] for r in range(mm.nrows())])
        assert fmpq_mat(mm)*sol == target_matrix
        common_den = 1
        for r in range(sol.nrows()):
            for j in range(sol.ncols()):
                common_den = lcm(common_den, int(sol[r, j].denominator))
        assert common_den == int(row['denominator'])
        assert only_two_three(common_den)
        all_den = lcm(all_den, common_den)
        total += count
        print(f'PASS m={m:2d}: {count:2d} complete original identities', flush=True)

assert seen == list(range(24))
assert total == DATA['total_identities'] == 1154
assert all_den == int(DATA['common_denominator']) == 2**215*3**170
print('PASS: primitive 47-relation, five 40-conductors, integral pencil, '
      '1154 exact identities; all denominators supported on {2,3}.')
