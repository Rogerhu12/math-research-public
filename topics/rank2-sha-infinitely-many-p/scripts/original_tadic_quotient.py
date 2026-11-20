"""Exact rational quotient recovery in the original finite function algebra.

Local series only propose a quotient.  Acceptance requires a complete exact
polynomial remainder over k[t], followed by the caller's original identities.
No reconstructed coefficients are written to disk.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical helper only in the public Actions.")

import itertools
from sage.all import GF, PolynomialRing


def polynomial_api_preflight():
    k = GF(29)
    R = PolynomialRing(k, "z_preflight")
    z = R.gen()
    denominator = 1 + z + z**2
    series = ((1 + 2*z)*denominator.inverse_series_trunc(16)).truncate(16)
    a, b = series.rational_reconstruction(z**16, 7, 7)
    assert a*denominator == b*(1 + 2*z)
    assert (z**5 + z + 1).compose_mod(z + 3, z**16) == (z + 3)**5 + z + 4


def exact_linear_relation(modulus, left, candidate, right, progress):
    """Prove left*candidate=right modulo the ORIGINAL modulus, without inversion."""
    K = modulus.base_ring()
    kt = K.gen().numerator().parent()
    R = PolynomialRing(kt, "X_exact")

    def clear(values):
        denominator = kt.one()
        for value in values:
            denominator = denominator.lcm(K(value).denominator())
        out = []
        for value in values:
            value = K(value)
            quotient, remainder = denominator.quo_rem(value.denominator())
            assert remainder == 0
            out.append(value.numerator()*quotient)
        return R(out), denominator

    hp, hd = clear(modulus.list())
    ap, ad = clear(left)
    up, ud = clear(candidate)
    bp, bd = clear(right)
    residual = ap*up*bd - bp*ad*ud
    if not residual:
        remainder = R.zero()
    elif residual.degree() < hp.degree():
        remainder = residual
    else:
        exponent = residual.degree() - hp.degree() + 1
        quotient, remainder = residual.pseudo_quo_rem(hp)
        assert hp.leading_coefficient()**exponent*residual == quotient*hp + remainder
    progress("t-adic: exact original fraction-free linear check",
             passed=not bool(remainder),
             modulus_degree=int(hp.degree()),
             modulus_denominator_degree=int(hd.degree()),
             candidate_denominator_degree=int(ud.degree()),
             candidate_numerator_degree=max((int(c.degree()) for c in up.list()), default=-1))
    return not bool(remainder)


def recover_exact_quotient(modulus, left, right, progress, max_precision=4096):
    """Find u with left*u=right in K[X]/(modulus), and verify it exactly.

    The precision cap is only a resource limit.  Exhaustion never means that
    the original quotient or its required arithmetic interpretation is absent.
    """
    K = modulus.base_ring()
    k = K.constant_base_field()
    p = int(k.characteristic())
    d = int(modulus.degree())
    assert modulus.leading_coefficient() == 1
    assert k.cardinality() == p
    left = [K(c) for c in left] + [K.zero()]*(d-len(left))
    right = [K(c) for c in right] + [K.zero()]*(d-len(right))
    assert len(left) == len(right) == d and any(left)
    source = [K(c) for c in modulus.list()] + left + right
    assert max_precision >= 32 and max_precision & (max_precision-1) == 0

    chosen = None
    for extension_degree in (1, 2, 3):
        residue = k if extension_degree == 1 else GF(p**extension_degree, "tadic_residue")
        R = PolynomialRing(residue, "z_local")
        converted = [(R(c.numerator().list()), R(c.denominator().list())) for c in source]
        RX = PolynomialRing(residue, "X_specialized")
        for center in itertools.islice(iter(residue), 256):
            values = []
            for numerator, denominator in converted:
                dv = denominator(center)
                if not dv:
                    break
                values.append(numerator(center)/dv)
            if len(values) != len(source):
                continue
            h0 = RX(values[:d+1])
            a0 = RX(values[d+1:2*d+1])
            if h0.degree() != d:
                continue
            gcd, bezout, unused = a0.xgcd(h0)
            if gcd.degree() != 0:
                continue
            inverse0 = (bezout/gcd[0]) % h0
            assert (a0*inverse0) % h0 == 1
            chosen = (extension_degree, residue, R, center, converted, inverse0)
            break
        if chosen is not None:
            break
    if chosen is None:
        raise ArithmeticError("No regular unit specialization in the bounded search; no nonexistence claim.")
    extension_degree, residue, R, center, converted, inverse0 = chosen
    z = R.gen()
    center_coordinates = ([int(center)] if extension_degree == 1 else
                          [int(c) for c in center.polynomial().list()])
    progress("t-adic: regular original unit specialization",
             extension_degree=extension_degree, center_coordinates=center_coordinates,
             original_degree=d, coefficient_count=len(source))

    def expand_all(precision):
        power = z**precision
        out = []
        for numerator, denominator in converted:
            numerator = numerator.compose_mod(z+center, power)
            denominator = denominator.compose_mod(z+center, power)
            assert denominator[0]
            out.append((numerator*denominator.inverse_series_trunc(precision)).truncate(precision))
        return out[:d+1], out[d+1:2*d+1], out[2*d+1:]

    def multiply(x, y, h, precision):
        out = [R.zero() for _ in range(2*d-1)]
        for i, a in enumerate(x):
            if a:
                for j, b in enumerate(y):
                    if b:
                        out[i+j] += (a*b).truncate(precision)
        for j in range(2*d-2, d-1, -1):
            leading = out[j]
            if leading:
                for i in range(d):
                    if h[i]:
                        out[j-d+i] -= (leading*h[i]).truncate(precision)
        return [c.truncate(precision) for c in out[:d]]

    def descend(value):
        assert value**p == value
        if extension_degree == 1:
            return k(value)
        polynomial = value.polynomial()
        assert polynomial.degree() <= 0
        return k(polynomial[0])

    def reconstruct(series, precision):
        candidate = []
        kt = K.gen().numerator().parent()
        cap = (precision-1)//2
        for coefficient in series:
            if not coefficient:
                candidate.append(K.zero())
                continue
            try:
                numerator, denominator = coefficient.rational_reconstruction(z**precision, cap, cap)
            except (ArithmeticError, ValueError, ZeroDivisionError):
                return None
            if not denominator or not denominator[0]:
                return None
            assert (coefficient*denominator-numerator).truncate(precision) == 0
            numerator = numerator(z-center)
            denominator = denominator(z-center)
            scale = denominator.leading_coefficient()
            numerator, denominator = numerator/scale, denominator/scale
            if any(c**p != c for c in numerator.list()+denominator.list()):
                return None
            num = kt([descend(c) for c in numerator.list()])
            den = kt([descend(c) for c in denominator.list()])
            candidate.append(K(num)/K(den))
        return candidate

    inverse = [R(inverse0[i]) for i in range(d)]
    precision = 1
    one = [R.one()] + [R.zero() for _ in range(d-1)]
    while precision < max_precision:
        precision *= 2
        progress("t-adic: exact Newton precision start", precision=precision)
        h, a, b = expand_all(precision)
        assert h[d] == 1
        error = multiply(a, inverse, h, precision)
        correction = [-c for c in error]
        correction[0] += 2
        inverse = multiply(inverse, correction, h, precision)
        assert multiply(a, inverse, h, precision) == one
        progress("t-adic: complete original inverse residual passed", precision=precision)
        if precision < 32:
            continue
        proposal = reconstruct(multiply(b, inverse, h, precision), precision)
        if proposal is None:
            progress("t-adic: no rational candidate at current precision", precision=precision)
            continue
        if exact_linear_relation(modulus, left, proposal, right, progress):
            return proposal, {
                "method":"local-series quotient, rational reconstruction, exact original polynomial remainder",
                "extension_degree":extension_degree,
                "center_coordinates":center_coordinates,
                "precision":precision,
                "complete_original_linear_relation":True,
                "all_Newton_residuals_checked":True,
                "base_field_descent_checked":True,
                "bounded_precision_is_not_a_nonexistence_test":True}
    raise ArithmeticError("Precision cap reached without an exactly certified quotient; no nonexistence claim.")
