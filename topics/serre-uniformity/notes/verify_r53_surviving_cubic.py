#!/usr/bin/env python3
"""Exact, dependency-free verification of the R53 surviving cubic example.

The primality proof uses the full Lucas N+1 criterion proved in R53.
No probable-prime test, external database, or elliptic-curve package is used.
"""

from math import gcd, isqrt, prod


def small_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def lucas_u(index, p, q, modulus):
    """U_0=0, U_1=1, U_(m+2)=p U_(m+1)-q U_m, modulo modulus."""
    u, v, q_power = 0, 2, 1
    inv2 = (modulus + 1) // 2
    discriminant = p * p - 4 * q
    for bit in bin(index)[2:]:
        u, v, q_power = (
            u * v % modulus,
            (v * v - 2 * q_power) % modulus,
            q_power * q_power % modulus,
        )
        if bit == "1":
            u, v = (
                inv2 * (p * u + v) % modulus,
                inv2 * (discriminant * u + p * v) % modulus,
            )
            q_power = q_power * q % modulus
    return u


def main():
    p = 43
    small_primes = [r for r in range(2, 462) if small_prime(r)]
    assert len(small_primes) == 89 and small_primes[-1] == 461
    m = prod(small_primes)
    n = 116 * m
    q = 432 * n * n - 1
    z = -q

    # Complete prime factorisation of q+1:
    # 432=2^4*3^3, 116=2^2*29, and M contains each r once.
    factorisation = {r: 2 for r in small_primes}
    factorisation[2] += 8
    factorisation[3] += 3
    factorisation[29] += 2
    assert prod(r**a for r, a in factorisation.items()) == q + 1
    assert gcd(q, 2 * (-127) * 509) == 1
    assert lucas_u(q + 1, 1, -127, q) == 0
    for r in small_primes:
        assert gcd(lucas_u((q + 1) // r, 1, -127, q), q) == 1
    # By R53 §2, q is now proved prime.

    assert small_prime(467)
    assert (-8 * n) % 467 == 213
    assert all((t**3 - t + 213) % 467 != 0 for t in range(467))
    # Hence g=T^3-T-8n is irreducible over Q.

    for r in small_primes[1:]:
        assert n % r == 0
        assert q % r == r - 1
        assert (8 * n) % r == 0
        # g mod r = T(T-1)(T+1), three distinct roots for odd r.
        assert len({0, 1, r - 1}) == 3

    assert q % (4 * p) == 4 * p - 1
    assert z % 432 == 1
    assert gcd(z, 6 * p) == 1
    assert q > p**4
    assert 1 - 27 * (4 * n) ** 2 == z
    assert (108 * n) ** 2 == 3**3 + 27 * q

    # q-adic simple root: g(24n)=0 mod q and g'(24n)=3 mod q.
    assert ((24 * n) ** 3 - 24 * n - 8 * n) % q == 0
    assert (3 * (24 * n) ** 2 - 1) % q == 3
    # At 2, n has valuation 3; strong Hensel at +/-1 and simple Hensel at 0.
    assert n % 8 == 0 and n % 16 != 0
    assert (8 * n) % 64 == 0 and (8 * n) % 128 != 0

    print("R53 exact verification passed")
    print("p=43; M=product of primes <=461; n=116M; q=432n^2-1")
    print(f"q has {len(str(q))} digits")
    print("Lucas N+1 certificate: (P,Q,D)=(1,-127,509)")
    print("U_(q+1)=0 modulo q; all 89 required gcd values are 1")
    print("T^3-T+213 has no root in F_467")
    print("g splits at every odd prime <=461; q=-1 modulo 4p")
    print("P=(3,108n) lies on D: V^2=U^3+27q")


if __name__ == "__main__":
    main()
