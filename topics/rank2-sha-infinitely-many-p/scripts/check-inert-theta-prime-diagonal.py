#!/usr/bin/env python3
"""Finite computations of the actual degree-17 theta prime diagonal.

No inference about infinitely many primes is made here.  The default run
compares two independent coefficient algorithms for all inert primes < 500.
The fast algorithm needs python-flint.  Run --bound 25000 to reproduce the
larger finite sample recorded in the accompanying note.
"""
import argparse

from flint import nmod_poly


def primes_below(bound):
    sieve = bytearray(b"\1") * bound
    if bound:
        sieve[0] = 0
    if bound > 1:
        sieve[1] = 0
    for n in range(2, int(bound**0.5) + 1):
        if sieve[n]:
            start = n*n
            sieve[start::n] = b"\0" * ((bound-1-start)//n + 1)
    return [n for n in range(7, bound) if sieve[n] and n % 4 == 3]


def series_log(a, n, p):
    assert a[0] == 1
    out = [0] * (n+1)
    for k in range(1, n+1):
        out[k] = (a[k] - sum(
            j*out[j]*a[k-j] for j in range(1, k)
        ) * pow(k, -1, p)) % p
    return out


def series_exp(a, n, p):
    assert a[0] == 0
    out = [1] + [0]*n
    for k in range(1, n+1):
        out[k] = sum(
            j*a[j]*out[k-j] for j in range(1, k+1)
        ) * pow(k, -1, p) % p
    return out


def prime_diagonal_direct(p):
    """x''=6x^2-2; log(sigma/z)''=-(x-z^-2)."""
    assert p >= 7 and p % 4 == 3
    r = (p+1)//4
    n = r-1
    X = [1] + [0]*n
    for j in range(1, n+1):
        X[j] = (
            6*sum(X[k]*X[j-k] for k in range(1, j)) - 2*(j == 1)
        ) * pow((4*j-2)*(4*j-3)-12, -1, p) % p
    log_X = series_log(X, n, p)
    log_sigma = [0] + [
        -X[j]*pow(4*j*(4*j-1), -1, p) % p for j in range(1, n+1)
    ]
    inv5 = pow(5, -1, p)
    parameters = [1, 3*inv5, -inv5, inv5]
    answer = 0
    for j in range(1, min(r, 4)+1):
        exponent = [
            (17*log_sigma[k] + (17-4*j)*pow(2, -1, p)*log_X[k]) % p
            for k in range(n+1)
        ]
        answer += parameters[j-1] * series_exp(exponent, r-j, p)[r-j]
    return answer % p


def polynomial_exp(L, length, p):
    """Newton iteration G <- G*(1 + L - log G), with length < p."""
    G = nmod_poly([1], p)
    precision = 1
    while precision < length:
        precision = min(2*precision, length)
        log_G = (
            G.derivative()*G.inverse_series_trunc(precision)
        ).truncate(precision-1).integral()
        G = (G*(1+L.truncate(precision)-log_G)).truncate(precision)
    return G


def prime_diagonal_fast(p):
    """Lagrange formula 4*[v^((p-3)/4)]((Theta^17*q)'/F)."""
    assert p >= 7 and p % 4 == 3
    n = (p-3)//4
    coefficients = [1]
    for j in range(1, n+1):
        coefficients.append(
            coefficients[-1]*(2*j-1)*pow(2*j, -1, p) % p
        )
    F = nmod_poly([
        coefficients[j]*pow(4*j+1, -1, p) % p for j in range(n+1)
    ], p)
    H = nmod_poly([
        coefficients[j]*pow(4*j+3, -1, p) % p for j in range(n)
    ], p)
    inverse_square_root = nmod_poly(coefficients, p)
    L = ((H*inverse_square_root).truncate(n)*pow(4, -1, p)).integral()*17
    theta_power = polynomial_exp(L, n+1, p)
    inv5 = pow(5, -1, p)
    q = nmod_poly([0, 1, 3*inv5, -inv5, inv5], p)
    numerator = (theta_power*q).truncate(n+2).derivative()
    result = (numerator*F.inverse_series_trunc(n+1)).truncate(n+1)
    return 4*int(result[n]) % p


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bound", type=int, default=500)
    parser.add_argument("--compare-bound", type=int, default=500)
    parser.add_argument("--values", action="store_true")
    args = parser.parse_args()
    assert args.bound >= 8 and args.compare_bound >= 8
    for p in primes_below(args.compare_bound):
        direct = prime_diagonal_direct(p)
        fast = prime_diagonal_fast(p)
        assert direct == fast, (p, direct, fast)
    print("Independent algorithms agree for inert primes below", args.compare_bound)
    primes = primes_below(args.bound)
    zeros = []
    for p in primes:
        value = prime_diagonal_fast(p)
        if not value:
            zeros.append(p)
        if args.values:
            print(p, value)
    print("Finite prime count:", len(primes))
    print("Zero residues in this finite range:", zeros)
    print("This finite computation does not prove nonvanishing at infinitely many primes.")


if __name__ == "__main__":
    main()
