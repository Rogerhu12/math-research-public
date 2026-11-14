#!/usr/bin/env python3
"""R125: exact isogenies and Coleman--Gross heights modulo 5^5.

Standard library only.  The splitting is <U*omega-2*omega>, not an
uncomputed unit-root splitting.  This program does not classify C(Q).
"""
import sys
sys.dont_write_bytecode = True
import argparse
import hashlib
import json
from fractions import Fraction as F
from math import isqrt, lcm
from pathlib import Path

from verify_r120_nine_cartan_twist import (
    K, assertzero, deriv, ecadd, ecmul, padd, peval, pmul, ppow, pscale, psub,
)

w = K(0, 1)
A = -(21 + 27*w)/2
B = 28*w-10
PH = ((7-w)/2, 4*w-4)
P2 = ((1+w)/2, 2*w+4)
hh = 3*(1+w)/2
v2 = 8-8*w
uu = (3-w)/2
tt = 3*hh*hh+A
MOD = 5**5


def negate(P):
    return None if P is None else (P[0], -P[1])


def multiple(P, n):
    return ecmul(P, n, A, None) if n >= 0 else negate(ecmul(P, -n, A, None))


def conjugate(P):
    return None if P is None else tuple(a.conjugate() for a in P)


def mu(P):
    if P is None or P[0] == hh:
        return None
    x, y = P
    z = x-hh
    return ((x+2*tt/z+4*v2/z**2)/uu**2,
            y*(1-2*tt/z**2-8*v2/z**3)/uu**3)


def rm_point(P):
    return conjugate(mu(P))


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def inverse2(a):
    d = a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return [[a[1][1]/d, -a[0][1]/d], [-a[1][0]/d, a[0][0]/d]]


def norm(a):
    return a.a*a.a+3*a.b*a.b


def exact_isogeny_data():
    assert hh**3+A*hh+B == v2
    assert 3*hh**4+6*A*hh**2+12*B*hh-A**2 == K(0)
    z = [-hh, K(1)]
    nx = padd(padd(pmul([K(0), K(1)], ppow(z, 2)), pscale(z, 2*tt)), [4*v2])
    ny = psub(psub(ppow(z, 3), pscale(z, 2*tt)), [8*v2])
    lhs = pmul([B, A, K(0), K(1)], ppow(ny, 2))
    rhs = padd(padd(ppow(nx, 3), pscale(pmul(nx, ppow(z, 4)), A.conjugate()*uu**4)),
               pscale(ppow(z, 6), B.conjugate()*uu**6))
    assertzero(psub(lhs, rhs))
    # The derivative identity proves mu^*(dU/(2V)) = uu*dU/(2V).
    assertzero(psub(psub(pmul(deriv(nx), z), pscale(nx, 2)), ny))
    assert uu*uu.conjugate() == K(3)

    r = (1-w)/2
    f = [(17+9*w)/14, -(45+9*w)/14, (6-3*w)/7, K(1)]
    assert -peval(deriv(f), r)/peval(f, r) == -w
    omega = [[(3+w)/2, w], [-w, (3-w)/2]]
    omega_bar = [[a.conjugate() for a in row] for row in omega]
    assert [[omega[i][j]+omega_bar[i][j] for j in range(2)] for i in range(2)] == [[K(3), K(0)], [K(0), K(3)]]
    pull = [[-3*r/2, -3*r.conjugate()/2], [K(F(3, 2)), K(F(3, 2))]]
    product_rm = [[K(0), uu], [uu.conjugate(), K(0)]]
    curve_rm = mm(mm(pull, product_rm), inverse2(pull))
    assert curve_rm == [[K(-2), K(-1)], [K(1), K(2)]]
    assert -2*w-2*uu == -2*uu.conjugate()
    de_rham = [[uu, -2*w], [K(0), uu.conjugate()]]

    images = []
    for P, coeff in [(PH, (-1, -1)), (P2, (-2, 1))]:
        Q = rm_point(P)
        assert Q == ecadd(multiple(PH, coeff[0]), multiple(P2, coeff[1]), A)
        assert rm_point(Q) == multiple(P, 3)
        images.append(dict(coefficients=list(coeff), coordinates=[x.pair() for x in Q]))
    return dict(kernel_x=hh.pair(), kernel_y_squared=v2.pair(),
                differential_scale=uu.pair(),
                de_rham_pullback=[[x.pair() for x in row] for row in de_rham],
                rm_differentials=[[-2, -1], [1, 2]], rm_points=images,
                rm_point_matrix=[[-1, -2], [-1, 1]],
                rm_D_matrix=[['-3', '3/2'], ['-4', '3']],
                phi_polarization_multiplier=3, phi_degree=9)


# Z[alpha], alpha=(1+w)/2, alpha^2-alpha+1=0.
def zmul(z, t):
    a, b = z
    c, d = t
    return a*c-b*d, a*d+b*c+b*d


def znorm(z):
    a, b = z
    return a*a+a*b+b*b


def zdivround(z, t):
    a, b = z
    c, d = t
    n = znorm(t)
    x, y = a*(c+d)+b*d, b*c-a*d
    return (2*x+n)//(2*n), (2*y+n)//(2*n)


def zgcd(z, t):
    while znorm(t):
        q = zdivround(z, t)
        v = zmul(q, t)
        r = z[0]-v[0], z[1]-v[1]
        assert 4*znorm(r) <= 3*znorm(t)
        z, t = t, r
    return z


def denominator_norm(x):
    a, b = x.a-x.b, 2*x.b
    d = lcm(a.denominator, b.denominator)
    c = int(a*d), int(b*d)
    g = zgcd(c, (d, 0))
    assert d*d % znorm(g) == 0
    n = d*d//znorm(g)
    root = isqrt(n)
    assert root*root == n
    return root


def vp_integer(n, p=5):
    assert n
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v, n


def vp_fraction(q, p=5):
    q = F(q)
    return vp_integer(q.numerator, p)[0]-vp_integer(q.denominator, p)[0] if q else 10**9


def residue(q, modulus=MOD):
    q = F(q)
    return q.numerator*pow(q.denominator, -1, modulus) % modulus


def log5(q, precision=5):
    q = F(q)
    modulus = 5**precision
    extra = 5**(precision+3)
    a, b = vp_integer(q.numerator)[1], vp_integer(q.denominator)[1]
    unit = a*pow(b, -1, extra) % extra
    x = (pow(unit, 4, extra)-1) % extra
    assert x % 5 == 0
    ans = 0
    for k in range(1, 2*precision+2):
        v, d = vp_integer(k)
        term = (pow(x, k, modulus*5**v)//5**v)*pow(d, -1, modulus) % modulus
        ans = (ans+(-1)**(k+1)*term) % modulus
    return ans*pow(4, -1, modulus) % modulus


def alpha_reduction(a, p):
    return residue(a.a-a.b, p), residue(2*a.b, p)


def local_model_data():
    assert -16*(4*A**3+27*B**2) == 55296*(w-1)
    assert ecadd(PH, PH, A) == (w+2, (w-1)/2)
    twice_P2 = ecadd(P2, P2, A)
    assert twice_P2 == ((149+41*w)/49, (347-65*w)/343)
    red2 = [[list(alpha_reduction(a, 2)) for a in P]
            for P in [ecadd(PH, PH, A), twice_P2]]
    assert red2 == [[[1, 0], [1, 1]], [[0, 0], [0, 0]]]
    red3 = [[residue(a.a, 3) for a in P] for P in [PH, P2]]
    assert red3 == [[2, 2], [2, 1]]
    return dict(discriminant=(55296*(w-1)).pair(),
                twice_points_reduction_mod_2=red2,
                points_reduction_mod_w=red3,
                common_multiplier=66)


def height_data(P, multiplier=66):
    Q = multiple(P, multiplier)
    x, y = Q
    assert min(vp_fraction(x.a), vp_fraction(x.b)) == -2
    assert min(vp_fraction(y.a), vp_fraction(y.b)) == -3
    t = -x/y
    assert min(vp_fraction(t.a), vp_fraction(t.b)) == 1
    nd = denominator_norm(x)
    logpart = log5(F(nd)/norm(t))
    t2part = residue(2*(t*t).a)
    h = (logpart-t2part)*2*pow(multiplier*multiplier, -1, MOD) % MOD
    return dict(multiplier=multiplier,
                norm_denominator_mod_3125=nd % MOD,
                log_norm_denominator_over_norm_t=logpart,
                trace_t_squared=t2part, height_mod_3125=h)


def all_heights():
    data = {'PH': height_data(PH), 'P2': height_data(P2),
            'PH_plus_P2': height_data(ecadd(PH, P2, A)),
            'PH_multiplier_132': height_data(PH, 132)}
    a, c, s = [data[k]['height_mod_3125'] for k in ['PH', 'P2', 'PH_plus_P2']]
    b = (s-a-c)*pow(2, -1, MOD) % MOD
    he = [[a, b], [b, c]]
    assert he == [[275, 270], [270, 10]]
    assert data['PH_multiplier_132']['height_mod_3125'] == a
    assert (2*a-2*b-c) % MOD == 0
    assert s == 3*a % MOD
    change = [[4, -2], [0, 1]]
    hj = [[x*pow(3, -1, MOD) % MOD for x in row]
          for row in mm(mm(transpose(change), he), change)]
    determinant = (a*c-b*b) % MOD
    assert vp_integer(determinant)[0] == 2
    return dict(points=data, matrix_E=he, matrix_J=hj,
                determinant_E_mod_3125=determinant,
                determinant_J_mod_3125=(hj[0][0]*hj[1][1]-hj[0][1]**2) % MOD,
                splitting='span(U*omega - 2*omega)',
                idele_log_at_5='Tr_K5_Q5 log_5; log_5(5)=0',
                normalization='Coleman-Gross; local formal value -2 Tr log sigma',
                precision=5, prime=5)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    payload = dict(isogeny=exact_isogeny_data(), local_models=local_model_data(),
                   heights=all_heights(),
                   scope=['explicit rational RM and (3,3) isogeny',
                          'actual global heights for a specified isotropic splitting',
                          'no complete rational-point or quadratic-Chabauty classification'])
    encoded = json.dumps(payload, indent=2, sort_keys=True)+'\n'
    target = Path(__file__).with_name('r125_explicit_rm_heights_certificate.json')
    if args.check:
        assert target.read_text() == encoded
        print('R125 PASS: exact isogenies, local models, four height computations')
    else:
        target.write_text(encoded)
        print(target.name)
    print('certificate sha256', hashlib.sha256(encoded.encode()).hexdigest())


if __name__ == '__main__':
    main()
