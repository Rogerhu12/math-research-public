#!/usr/bin/env python3
"""Exact certificate for R71; no modular-forms database or numerical eigenvalues.

Usage: python necklace_chen_spectrum.py [41] [--show-radial]
Dependencies: SymPy; python-flint is optional and only speeds up charpoly.

The generic part constructs nonsplit involutions, their antipodal-pair Gram
matrix, and its normalizer-invariant radial quotient.  The p=41 certificate
also checks character-type factors, holomorphic multiplicities, and the
polarization determinant.  The proof identifying this matrix with a genuine
Jacobian correspondence is in R71, not an assumption supplied by this script.
"""

import argparse
from sympy import Matrix, Poly, Rational, Symbol, cyclotomic_poly, factor_list, factorint
from sympy import isprime, resultant


def certificate(p, show_radial=False):
    if p < 5 or not isprime(p):
        raise ValueError("p must be an odd prime at least 5")

    def legendre(a):
        a %= p
        return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)

    nonsquares = [a for a in range(1, p) if legendre(a) == -1]
    delta = nonsquares[0]
    necklaces = [(a, d) for a in range(p) for d in nonsquares]
    necklace_index = {r: i for i, r in enumerate(necklaces)}

    def antipodal_pairs(r):
        a, d = r
        out = {(a, p)}  # p denotes infinity.
        for x in range(p):
            if x != a:
                y = (a + d * pow((x - a) % p, -1, p)) % p
                if x < y:
                    out.add((x, y))
        assert len(out) == (p + 1) // 2
        return out

    pair_sets = [antipodal_pairs(r) for r in necklaces]

    def multiply(g, h):
        a, b, c, d = g
        A, B, C, D = h
        return ((a*A+b*C) % p, (a*B+b*D) % p,
                (c*A+d*C) % p, (c*B+d*D) % p)

    def conjugate(g, r):
        a, d = r
        involution = (a, (d-a*a) % p, 1, -a % p)
        A, B, C, D = g
        adjugate = (D, -B, -C, A)
        h = multiply(multiply(g, involution), adjugate)
        scale = pow(h[2], -1, p)
        aa = h[0] * scale % p
        dd = (aa*aa + h[1]*scale) % p
        assert (h[0]+h[3]) % p == 0 and legendre(dd) == -1
        return aa, dd

    torus = [(1, 0, 0, 1)] + [(t, delta, 1, t) for t in range(p)]
    reflection = (1, 0, 0, -1)
    normalizer = torus + [multiply(reflection, t) for t in torus]
    assert len(normalizer) == 2 * (p + 1)
    unused = set(necklaces)
    orbits = []
    while unused:
        representative = min(unused)
        orbit = sorted({conjugate(g, representative) for g in normalizer})
        assert set(orbit) <= unused
        orbits.append(orbit)
        unused.difference_update(orbit)
    assert sum(map(len, orbits)) == p * (p - 1) // 2

    def gram(r, s):
        return len(pair_sets[necklace_index[r]] & pair_sets[necklace_index[s]])

    radial = [[sum(gram(oi[0], r) for r in oj) for oj in orbits]
              for oi in orbits]
    assert all(sum(row) == (p*p-1) // 4 for row in radial)
    assert all(len(orbits[i])*radial[i][j] == len(orbits[j])*radial[j][i]
               for i in range(len(orbits)) for j in range(len(orbits)))
    x = Symbol("x")
    try:
        from flint import fmpz_mat
        coefficients = list(fmpz_mat(radial).charpoly())
        characteristic = Poly(sum(int(c)*x**i for i, c in enumerate(coefficients)), x)
    except ImportError:
        characteristic = Poly(Matrix(radial).charpoly(x).as_expr(), x)
    print("p, delta, necklace count, radial dimension:",
          p, delta, len(necklaces), len(orbits))
    print("Normalizer orbit sizes:", list(map(len, orbits)))
    print("Radial characteristic polynomial:", factor_list(characteristic.as_expr()))
    if show_radial:
        print("Radial matrix:")
        for row in radial:
            print(row)

    generator = next(g for g in range(2, p)
                     if len({pow(g, i, p) for i in range(p-1)}) == p-1)
    base = (0, delta)
    a_vector = [sum(gram(base, (a, delta*pow(generator, 2*m, p) % p))
                    for a in range(p)) for m in range((p-1)//2)]
    print("Primitive root, principal-series A vector:", generator, a_vector)
    t = Symbol("t")
    principal_resultants = {}
    for d in range(1, (p-1)//2 + 1):
        if ((p-1)//2) % d == 0:
            value = sum(a*t**(m % d) for m, a in enumerate(a_vector))
            polynomial = Poly(resultant(cyclotomic_poly(d, t), x-value, t), x)
            principal_resultants[d] = polynomial
            print("Principal character order", d, ":", factor_list(polynomial.as_expr()))

    if p != 41:
        return
    f2 = Poly(x**2-40*x+80, x)
    f3 = Poly(x**3-83*x**2+2035*x-12769, x)
    f4 = Poly(x**4-48*x**3+544*x**2-1792*x+256, x)
    f6 = Poly(x**6-94*x**5+3159*x**4-45828*x**3
              +275615*x**2-613310*x+212521, x)
    expected = Poly((x-420)*(x-16)*(x-25)*(x-32)*(x-36)**2, x)*f2*f3*f4*f6
    assert characteristic == expected
    expected_principal = {
        1: Poly(x-420, x), 2: Poly(x-16, x), 4: Poly((x-32)**2, x),
        5: f2**2, 10: Poly((x-36)**4, x), 20: f4**2,
    }
    assert principal_resultants == expected_principal
    principal_real_values = {4: 32, 5: 12-16*x, 10: 36,
                             20: -4*x**3-8*x**2+16*x+32}
    for d, expression in principal_real_values.items():
        cyc = Poly(cyclotomic_poly(d, t), t)
        value = Poly(sum(a*t**((-m) % d) for m, a in enumerate(a_vector)), t).rem(cyc)
        target = Poly(Poly(expression, x).as_expr().subs(x, t+t**(d-1)), t).rem(cyc)
        assert (value-target).is_zero
    print("Principal eigenvalues in c=zeta+zeta^-1:", principal_real_values)

    # The cuspidal spherical character calculation labels the factors directly.
    # F_(p^2) = F_p[sqrt(delta)]; its projective multiplicative group has order p+1.
    def field_multiply(u, v):
        a, b = u
        A, B = v
        return ((a*A+delta*b*B) % p, (a*B+b*A) % p)

    def projective_field(u):
        a, b = u
        return (1, 0) if b == 0 else (a*pow(b, -1, p) % p, 1)

    def field_power(u, exponent):
        out = (1, 0)
        while exponent:
            if exponent & 1:
                out = field_multiply(out, u)
            u = field_multiply(u, u)
            exponent //= 2
        return out

    rho = next((a, 1) for a in range(p)
               if len({projective_field(field_power((a, 1), j))
                       for j in range(p+1)}) == p+1)
    logarithms = {projective_field(field_power(rho, j)): j for j in range(p+1)}
    square_roots = {a*a % p: a for a in range(p)}
    histogram = [0]*(p+1)
    constant = 0
    inv_two = pow(2, -1, p)
    for m in range((p-1)//2):
        s = pow(generator, m, p)
        for a in range(p):
            r = (a, delta*s*s % p)
            weight = gram(base, r)
            if weight == 0:
                continue
            g_r = (s, a, 0, 1)
            for n in normalizer:
                aa, bb, cc, dd = multiply(g_r, n)
                if bb == cc == 0 and aa == dd:
                    constant += weight*(p-1)  # character at scalar matrices
                    continue
                discriminant = ((aa+dd)**2-4*(aa*dd-bb*cc)) % p
                if discriminant == 0:
                    constant -= weight  # character at a nontrivial unipotent
                    continue
                if legendre(discriminant) == 1:
                    continue  # cuspidal character at a split regular element
                b = square_roots[discriminant*pow(delta, -1, p) % p]
                eigenvalue = ((aa+dd)*inv_two % p, b*inv_two % p)
                j = logarithms[projective_field(eigenvalue)]
                histogram[j] += weight
    assert rho == (4, 1) and constant == 0
    print("Nonsplit generator, constant, class histogram:", rho, constant, histogram)
    cuspidal_real_values = {6: 25, 14: 12*x**2-4*x+9,
                           42: -4*x**4+4*x**3+20*x**2-20*x-3}
    cuspidal_resultants = {6: Poly((x-25)**2, x), 14: f3**2, 42: f6**2}
    for d, expression in cuspidal_real_values.items():
        cyc = Poly(cyclotomic_poly(d, t), t)
        value = Poly(Rational(constant, len(normalizer))
                     -sum(Rational(h, len(normalizer))
                          *(t**(j % d)+t**((-j) % d))
                          for j, h in enumerate(histogram)), t).rem(cyc)
        target = Poly(Poly(expression, x).as_expr().subs(x, t+t**(d-1)), t).rem(cyc)
        assert (value-target).is_zero
        assert Poly(resultant(cyc.as_expr(), x-value.as_expr(), t), x) == cuspidal_resultants[d]
    print("Cuspidal eigenvalues in c=zeta+zeta^-1:", cuspidal_real_values)
    # Each indicated reduction has the original degree and is irreducible.
    for f, prime in [(f2, 3), (f3, 3), (f4, 3), (f6, 11)]:
        assert Poly(f.as_expr(), x, modulus=prime).is_irreducible
    print("Irreducibility certificates (degree, reduction prime):",
          [(2, 3), (3, 3), (4, 3), (6, 11)])

    # Actual H^0 multiplicities from the equivariant Euler-characteristic proof.
    # Each entry is (dimension, I_2-fixed dimension, I_3-fixed dimension,
    # I_41-fixed dimension).  None of these nontrivial types has PSL invariants.
    fixed_dimensions = {
        "St quadratic": (41, 21, 13, 1),
        "PS each": (42, 22, 14, 2),
        "SC order 6": (40, 20, 14, 0),
        "SC order 14": (40, 20, 12, 0),
        "SC order 42": (40, 20, 14, 0),
    }
    multiplicities = {}
    for kind, (dimension, *fixed) in fixed_dimensions.items():
        numerator = dimension-sum(fixed)
        assert numerator % 2 == 0
        multiplicities[kind] = numerator // 2
    assert multiplicities == {"St quadratic": 3, "PS each": 2,
                              "SC order 6": 3, "SC order 14": 4,
                              "SC order 42": 3}
    print("Actual H^0 multiplicities:", multiplicities)

    finite_degree = 1+41+42+84+40+2*42+4*42+3*40+6*40
    holomorphic = (Poly((x-16)**3*(x-32)**2*(x-36)**4*(x-25)**3, x)
                   *f2**2*f4**2*f3**4*f6**3)
    assert finite_degree == 820 and holomorphic.degree() == 54
    determinant_c = int(holomorphic.eval(0))  # even degree
    determinant_kappa = 2**54 * determinant_c
    expected_det = 2**108 * 3**8 * 5**8 * 113**8 * 461**6
    assert determinant_kappa == expected_det
    print("Full finite characteristic-polynomial degree:", finite_degree)
    print("Actual H^0 Gram characteristic polynomial:", factor_list(holomorphic.as_expr()))
    print("det(kappa | H^0) factorization:", factorint(determinant_kappa))
    print("All p=41 exact assertions passed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("p", type=int, nargs="?", default=41)
    parser.add_argument("--show-radial", action="store_true")
    args = parser.parse_args()
    certificate(args.p, args.show_radial)
