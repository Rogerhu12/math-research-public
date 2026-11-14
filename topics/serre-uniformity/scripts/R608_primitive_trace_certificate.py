"""Actual primitive ring-class trace with an explicit analytic tail.

Only integer arithmetic is used for coefficients.  The new numerical stage uses
directed mpmath interval arithmetic for a finite E1 series, with an explicit
first-omitted-term bound and a rational Euler--Maclaurin enclosure of gamma.
No individual complex L-value or guessed algebraic recognition is used.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
from math import gcd, isqrt
import argparse
import json
import time
import mpmath as mp
import sympy as sy


def mul(x, y, modulus=None):
    a, b = x
    c, d = y
    z = (a*c-b*d, a*d+b*c-b*d)
    return z if modulus is None else (z[0] % modulus, z[1] % modulus)


def power(x, n, modulus):
    result = (1, 0)
    while n:
        if n & 1:
            result = mul(result, x, modulus)
        x = mul(x, x, modulus)
        n >>= 1
    return result


def mu3_exponent(x, q):
    roots = [(1, 0), (0, 1), (q-1, q-1)]
    return roots.index((x[0] % q, x[1] % q))


def rational_cubic_symbol_exponent(alpha, q):
    """Exponent of (alpha/(q))_3 in Z[zeta]/(q), for q != 3.

    At split q this is the product over its two prime ideals, expressed as
    (alpha/conjugate(alpha))^((q-1)/3).  At inert q it is the finite-field
    cubic symbol.  Alpha has norm coprime to q.
    """
    a, b = alpha
    if q % 3 == 2:
        value = power((a % q, b % q), (q*q-1)//3, q)
    else:
        norm = (a*a-a*b+b*b) % q
        invnorm = pow(norm, -1, q)
        square = mul((a, b), (a, b), q)
        ratio = (square[0]*invnorm % q, square[1]*invnorm % q)
        value = power(ratio, (q-1)//3, q)
    return mu3_exponent(value, q)


def quotient_order(alpha, p, M, factors):
    value = power((alpha[0] % p, alpha[1] % p), 3*(p-1), p)
    order = M
    assert power(value, order, p) == (1, 0)
    for ell in factors:
        while order % ell == 0 and power(value, order//ell, p) == (1, 0):
            order //= ell
    return order


def iv_fraction(x):
    x = Fraction(x)
    return mp.iv.mpf(x.numerator) / x.denominator


def gamma_enclosure():
    # H_n-log(n)-1/(2n)+sum B_2k/(2k*n^(2k)).
    # The Stieltjes remainder lies between 0 and the first omitted term.
    n, K = 64, 12
    harmonic = sum((Fraction(1, k) for k in range(1, n+1)), Fraction())
    rational = harmonic - Fraction(1, 2*n)
    for k in range(1, K+1):
        bernoulli = sy.bernoulli(2*k)
        rational += Fraction(int(sy.numer(bernoulli)), int(sy.denom(bernoulli))) / (2*k*n**(2*k))
    next_b = sy.bernoulli(2*K+2)
    omitted = Fraction(int(sy.numer(next_b)), int(sy.denom(next_b))) / ((2*K+2)*n**(2*K+2))
    assert omitted > 0
    return iv_fraction(rational) - mp.iv.log(n) + mp.iv.mpf([0, 1])*iv_fraction(omitted)


def e1_enclosure(x, gamma):
    # E1(x)=-gamma-log(x)-sum_{k>=1}(-x)^k/(k*k!).
    # After N>x all absolute terms decrease; first omitted term bounds tail.
    N = 64 + 4*int(mp.ceil(mp.mpf(x.b)))
    term = -x
    total = term
    for k in range(1, N):
        term = term * (-x) * k / ((k+1)*(k+1))
        total += term
    omitted = term * (-x) * N / ((N+1)*(N+1))
    return -gamma - mp.iv.log(x) - total + mp.iv.mpf([-1, 1])*abs(omitted)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--p', type=int, required=True)
    parser.add_argument('--d0', type=int, required=True)
    parser.add_argument('--cutoff-factor', type=int, default=40)
    parser.add_argument('--dps', type=int, default=60)
    args = parser.parse_args()
    p, d0 = args.p, args.d0
    assert sy.isprime(p) and p > 37 and p % 9 in (2, 5)
    m = 2 if p % 9 == 2 else 1
    assert d0 > 0 and gcd(d0, 6*p) == 1
    facd = {int(q): int(e) for q, e in sy.factorint(d0).items()}
    assert all(e in (1, 2) for e in facd.values())
    d = p**m*d0
    assert d % 9 in (1, 8), 'actual even-branch three-adic cube condition'
    D = 1
    for q in facd:
        D *= q
    sD = sum(q % 3 == 2 for q in facd)
    assert sD % 2 == 0, 'this certificate uses the negative-root E1 kernel'
    M = (p+1)//3
    assert gcd(M, 3) == 1 and M % 2 == 0
    factors = list(map(int, sy.factorint(M)))
    phiM = int(sy.totient(M))
    X = args.cutoff_factor*p*D
    bad = 6*p*D
    R = isqrt(4*X//3)+2
    starts_a = -R + ((1+R) % 3)
    starts_b = -R + (R % 3)
    coefficients = {}
    ideal_count = 0
    weighted_count = 0
    started = time.time()
    roots = [(1, 0), (0, 1), (-1, -1)]
    for a in range(starts_a, R+1, 3):
        for b in range(starts_b, R+1, 3):
            n = a*a-a*b+b*b
            if n == 0 or n > X or gcd(n, bad) != 1:
                continue
            ideal_count += 1
            order = quotient_order((a, b), p, M, factors)
            mu = int(sy.mobius(order))
            if not mu:
                continue
            phi_order = int(sy.totient(order))
            assert phiM % phi_order == 0
            scale = mu*(phiM//phi_order)
            exponent = 2*rational_cubic_symbol_exponent((a, b), 2)
            for q, e in facd.items():
                exponent -= e*rational_cubic_symbol_exponent((a, b), q)
            val = mul((a, b), roots[exponent % 3])
            previous = coefficients.setdefault(n, [0, 0])
            previous[0] += scale*val[0]
            previous[1] += scale*val[1]
            weighted_count += 1
    assert all(pair[1] == 0 for pair in coefficients.values()), 'conjugate-ideal trace must be rational'
    rows = [[n, pair[0]] for n, pair in sorted(coefficients.items()) if pair[0]]
    assert dict(rows)[1] == phiM
    coefficient_data = {
        'p': p, 'd0': d0, 'm': m, 'd': d, 'D': D, 'sD': sD,
        'M': M, 'phiM': phiM, 'X': X, 'scale': 'each row is phi(M) times the primitive averaged a_n',
        'primary_generator': 'a+b*zeta with a=1 mod3 and b=0 mod3',
        'kernel': 'mu(order((alpha^(p-1))^3))/phi(order)',
        'base_character': 'alpha*kappa4(alpha)*kappa_d0(alpha)^(-1)',
        'ideal_count': ideal_count, 'nonzero_kernel_ideal_count': weighted_count,
        'all_zeta_components_cancelled_exactly': True, 'rows': rows,
    }
    stem = Path(__file__).parent / f'R608-p{p}-d0_{d0}'
    coeff_path = Path(str(stem)+'-coefficients.json')
    coeff_path.write_text(json.dumps(coefficient_data, separators=(',', ':'))+'\n')
    mp.mp.dps = args.dps
    mp.iv.dps = args.dps
    t = mp.iv.pi/(3*mp.iv.sqrt(3)*p*D)
    gamma = gamma_enclosure()
    value = mp.iv.mpf(0)
    for index, (n, scaled) in enumerate(rows):
        value += (mp.iv.mpf(2*scaled)/(phiM*n))*e1_enclosure(t*n, gamma)
        if index and index % 1000 == 0:
            print(json.dumps({'stage': 'interval-sum', 'terms': index, 'total_terms': len(rows)}), flush=True)
    # Uniform ideal-count tail; no use of a heuristic estimate for remaining a_n.
    tail = 4*mp.iv.exp(-t*X)/(t*mp.iv.sqrt(X))
    enclosure = value + mp.iv.mpf([-1, 1])*tail
    lower = mp.mpf(enclosure.a)
    result = {
        'status': 'certified-positive' if lower > 0 else 'not-certified',
        'p': p, 'd0': d0, 'd': d, 'D': D, 'M': M, 'primitive_dimension': phiM,
        'cutoff': X, 'nonzero_norm_terms': len(rows),
        'finite_sum_interval': str(value), 'tail_bound_interval': str(tail),
        'full_derivative_mean_interval': str(enclosure),
        'gamma_interval': str(gamma), 'precision_decimal_digits': args.dps,
        'coefficient_path': str(coeff_path), 'coefficient_sha256': sha256(coeff_path.read_bytes()).hexdigest(),
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'mpmath_version': mp.__version__,
        'elapsed_seconds': round(time.time()-started, 3),
        'scope': 'actual primitive family only; not original candidate existence or global Serre completion',
    }
    result_path = Path(str(stem)+'-interval-certificate.json')
    result_path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
