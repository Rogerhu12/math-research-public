#!/usr/bin/env python3
"""Exact finite certificate for the sixteen fields in R150; standard library only.

Reduced positive binary quadratic forms compute h(D).  Their ambiguous shapes
prove exponent two.  The selected ramified ideal classes are certified by
reducing their forms and checking that all 2^r products are distinct.
No table of class numbers or floating-point arithmetic is used.
"""
from itertools import combinations
from math import gcd, isqrt, prod

DISCRIMINANTS = (-7, -11, -19, -67, -20, -24, -35, -52,
                 -187, -232, -267, -372, -483, -555, -795, -1435)
EXPECTED_H = (1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4)


def factor(n):
    ans = {}
    q = 2
    while q*q <= n:
        while n % q == 0:
            ans[q] = ans.get(q, 0) + 1
            n //= q
        q += 1
    if n > 1:
        ans[n] = 1
    return ans


def is_prime(n):
    return n >= 2 and all(n % q for q in range(2, isqrt(n)+1))


def fundamental(D):
    if D % 4 == 1:
        return all(e == 1 for e in factor(-D).values())
    if D % 4:
        return False
    d = D // 4
    return d % 4 in (2, 3) and all(e == 1 for e in factor(-d).values())


def reduced_forms(D):
    out = []
    for a in range(1, isqrt((-D)//3)+1):
        for b in range(-a, a+1):
            if (b*b-D) % (4*a):
                continue
            c = (b*b-D)//(4*a)
            if a > c or gcd(gcd(a, abs(b)), c) != 1:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            out.append((a, b, c))
    return out


def reduce_form(a, b, c):
    D = b*b-4*a*c
    while True:
        k = (a-b)//(2*a)
        b, c = b+2*a*k, a*k*k+b*k+c
        if a > c:
            a, b, c = c, -b, a
            continue
        if a == c and b < 0:
            b = -b
        if b == -a:
            b = a
        assert -a < b <= a <= c and b*b-4*a*c == D
        return (a, b, c)


def ramified_product_form(D, a):
    # The product of ramified ideals above primes dividing a has norm a.
    b = 0 if D % (4*a) == 0 else a
    assert (b*b-D) % (4*a) == 0
    c = (b*b-D)//(4*a)
    assert gcd(gcd(a, b), c) == 1
    return reduce_form(a, b, c)


def trace_E389(q):
    total = 0
    for x in range(q):
        d = (1+4*(x*x*x+x*x-2*x)) % q
        e = pow(d, (q-1)//2, q)
        total += -1 if e == q-1 else e
    return -total


def ordinary_principal_q(D, D0):
    candidates = []
    for b in range(1, 11):
        for a in range(0, 151):
            if D % 4 == 1:
                if (a-b) % 2:
                    continue
                n = a*a-D*b*b
                if n % 4:
                    continue
                q = n//4
                den = 2
            else:
                q = a*a-(D//4)*b*b
                den = 1
            if q < 7 or not is_prime(q) or (389*(-D)*D0) % q == 0:
                continue
            candidates.append((q, a, b, den))
    assert candidates
    for q, a, b, den in sorted(candidates):
        ap = trace_E389(q)
        if ap % q not in (0, 1, q-1):
            return q, a, b, den, ap
    raise AssertionError(("no ordinary principal witness", D))


def main():
    rows = []
    prime_set = sorted(set(q for D in DISCRIMINANTS for q in factor(-D)))
    echelon = {}
    for D, expected_h in zip(DISCRIMINANTS, EXPECTED_H):
        assert fundamental(D)
        assert pow(D % 389, 194, 389) == 1
        forms = reduced_forms(D)
        assert len(forms) == expected_h
        assert all(b == 0 or abs(b) == a or a == c for a, b, c in forms)
        # Omit the largest odd ramified prime.  Distinct reduced products
        # below certify this choice, without assuming a genus-theory basis.
        ramified = sorted(factor(-D))
        omit = max(q for q in ramified if q != 2)
        gens = [q for q in ramified if q != omit]
        products = [prod(s) for j in range(len(gens)+1)
                    for s in combinations(gens, j)]
        classes = [ramified_product_form(D, a) for a in products]
        assert len(set(classes)) == len(forms) == len(products)
        assert set(classes) == set(forms)
        D0 = prod(gens)
        qdata = ordinary_principal_q(D, D0)
        squareclass = 1  # negative sign
        exponents = factor(-D)
        for j, q in enumerate(prime_set, 1):
            if exponents.get(q, 0) % 2:
                squareclass ^= 1 << j
        v = squareclass
        while v:
            j = v.bit_length()-1
            if j in echelon:
                v ^= echelon[j]
            else:
                echelon[j] = v
                break
        assert v, ("dependent quadratic character", D)
        rows.append((D, expected_h, D0, tuple(gens), qdata, forms))
    assert len(echelon) == 16
    for D, h, D0, gens, (q, a, b, den, ap), forms in rows:
        d = D if D % 4 == 1 else D//4
        print(f"D={D:5d} h={h} D0={D0:2d} generators={gens} "
              f"q={q:4d} Norm(({a}+{b}sqrt({d}))/{den})={q} "
              f"a_q={ap:3d} forms={forms}")
    print("PASS: 16 independent fields; 389 split; exact class groups "
          "of exponent 2; ramified bases; principal ordinary q certificates.")


if __name__ == "__main__":
    main()
