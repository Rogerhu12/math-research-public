"""R919: exact original RR algebra without a gcd in the degree48 field.

This module runs mathematics only in the authorized public Actions.
No coefficient data or certificates are written to files.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical helper only in the public repository Actions.")

import hashlib
import itertools
import json
from sage.all import GF, PolynomialRing


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(obj):
    return hashlib.sha256(canonical(obj).encode()).hexdigest()


def poly_terms(poly):
    return [[list(map(int, exponent)), int(coefficient)]
            for exponent, coefficient in sorted(poly.dict().items())]


def certify_separable_specialization(poly, progress, label):
    """A full-degree squarefree specialization proves the generic resultant nonzero."""
    K = poly.base_ring()
    k = K.constant_base_field()
    p = int(k.characteristic())
    assert k.cardinality() == p
    degree = int(poly.degree())
    derivative_degree = int(poly.derivative().degree())
    assert degree > 0 and derivative_degree >= 0
    coefficients = [(list(c.numerator()), list(c.denominator()))
                    for c in poly.list()]
    progress("r919: separability specialization start", label=label, degree=degree)
    tested = 0
    for extension_degree in (1, 2, 3):
        field = k if extension_degree == 1 else GF(p**extension_degree, "r919_alpha")
        ring = PolynomialRing(field, "r919_z")
        evaluation_polynomials = [(ring(a), ring(b)) for a, b in coefficients]
        for point in itertools.islice(iter(field), 256):
            values = []
            regular = True
            for numerator, denominator in evaluation_polynomials:
                denominator_value = denominator(point)
                if not denominator_value:
                    regular = False
                    break
                values.append(numerator(point)/denominator_value)
            if not regular:
                continue
            specialized = ring(values)
            if (specialized.degree() != degree or
                    specialized.derivative().degree() != derivative_degree):
                continue
            tested += 1
            if specialized.gcd(specialized.derivative()).degree() != 0:
                continue
            def coords(value):
                return [int(value)] if extension_degree == 1 else [
                    int(a) for a in value.polynomial().list()]
            record = {
                "label":label, "generic_degree":degree,
                "derivative_degree":derivative_degree,
                "extension_degree":extension_degree,
                "point_coordinates":coords(point),
                "regular_full_degree_trials":tested, "gcd_degree":0,
                "specialized_coefficients_sha256":digest([
                    coords(value) for value in specialized.list()])}
            progress("r919: generic separability certified by specialization", **record)
            return record
    raise ArithmeticError("No squarefree specialization found in the bounded search; no claim of inseparability.")


_UNIVERSAL = {}


def exact_polynomial_scalar_quotient(poly, scalar):
    """Divide every coefficient in k[x,v], requiring zero remainders."""
    ring = poly.parent()
    C = ring.base_ring()
    scalar = C(scalar)
    assert scalar
    out = []
    for coefficient in poly.list():
        q, remainder = C(coefficient).quo_rem(scalar)
        assert remainder == 0
        assert scalar*q == coefficient
        out.append(q)
    answer = ring(out)
    assert scalar*answer == poly
    return answer


def universal_linear_remainder(prime, terms, progress):
    """Stop the exact fraction-free remainder construction at middle degree 1.

    No division enters Frac(k[x,v]), and the degree-zero resultant is not made.
    The resulting expression is only a candidate until BOTH original Phi17
    identities are checked after evaluation in the same original eta48 field.
    """
    key = (int(prime), digest([[int(i), int(j), str(c)]
                              for (i, j), c in sorted(terms.items())]))
    if key in _UNIVERSAL:
        return _UNIVERSAL[key]
    k = GF(prime)
    C = PolynomialRing(k, names=("r919_left", "r919_right"), order="degrevlex")
    left, right = C.gens()
    R = PolynomialRing(C, "r919_middle")
    fc = [C.zero() for _ in range(19)]
    gc = [C.zero() for _ in range(19)]
    for (i, j), coefficient in terms.items():
        fc[j] += k(coefficient)*left**i
        gc[i] += k(coefficient)*right**j
    first, second = R(fc), R(gc)
    assert first.degree() == second.degree() == 18
    assert first.leading_coefficient() == second.leading_coefficient() == 1
    A = second
    quotient, B = first.pseudo_quo_rem(-second)
    assert (-second.leading_coefficient())*first == quotient*(-second)+B
    assert B.parent() is R and B.degree() < A.degree()
    scale = C.one()
    stages = []
    progress("r919: exact polynomial-ring remainder chain start",
             prime=int(prime), middle_degree=18,
             coefficient_ring=str(C), fraction_field_divisions=False,
             degree_zero_resultant_requested=False)
    while B:
        d, e = int(A.degree()), int(B.degree())
        assert 0 <= e < d
        delta = d-e
        progress("r919: exact polynomial remainder available",
                 step=len(stages)+1, previous_middle_degree=d,
                 current_middle_degree=e,
                 coefficient_terms=sum(len(c.dict()) for c in B.list()))
        if e == 0:
            raise ArithmeticError("No linear remainder; no original U certificate.")
        if delta > 1:
            numerator = R([B.leading_coefficient()**(delta-1)*c for c in B.list()])
            normalized = exact_polynomial_scalar_quotient(numerator, scale**(delta-1))
        else:
            normalized = B
        stages.append({"previous_middle_degree":d, "middle_degree":e,
                       "degree_drop":delta})
        if e == 1:
            original = normalized
            break
        quotient, raw = A.pseudo_quo_rem(-B)
        assert (-B.leading_coefficient())**(d-e+1)*A == quotient*(-B)+raw
        denominator = scale**delta*A.leading_coefficient()
        next_B = exact_polynomial_scalar_quotient(raw, denominator)
        assert not next_B or next_B.degree() < e
        A, B = normalized, next_B
        scale = C(A.leading_coefficient())
    else:
        raise ArithmeticError("Remainder chain vanished before degree 1; no U certificate.")

    assert original.degree() == 1 and original.parent() is R
    leading, constant = original[1], original[0]
    assert leading
    diagonal, diagonal_power = left-right, 0
    while constant:
        qa, ra = leading.quo_rem(diagonal)
        qb, rb = constant.quo_rem(diagonal)
        if ra or rb:
            break
        leading, constant = qa, qb
        diagonal_power += 1
    assert leading and constant
    assert original[1] == diagonal**diagonal_power*leading
    assert original[0] == diagonal**diagonal_power*constant
    record = {
        "method":"exact fraction-free linear remainder; original full identities required",
        "actual_degree_steps":stages,
        "fraction_field_divisions":False,
        "degree_zero_resultant_computed":False,
        "every_coefficient_division_exactly_verified":True,
        "candidate_is_not_accepted_without_both_original_relations":True,
        "cancelled_diagonal_power":diagonal_power,
        "uncancelled_linear_remainder_sha256":digest({
            "leading":poly_terms(original[1]), "constant":poly_terms(original[0])}),
        "linear_relation_sha256":digest({
            "leading":poly_terms(leading), "constant":poly_terms(constant)}),
        "leading_terms":len(leading.dict()), "constant_terms":len(constant.dict())}
    progress("r919: polynomial-ring linear candidate complete", **record)
    answer = leading, constant, record
    _UNIVERSAL[key] = answer
    return answer


def eta_scaled_evaluation(poly, B, T, progress, label):
    """Evaluate P(T,T/t^12) after one exact base denominator clearing.

    Return (scaled_value, right_degree), with
    P(T,V)=t^(-12*right_degree)*scaled_value.
    All reduction is by the SAME original defining polynomial.
    """
    K = B.base_field()
    k = K.constant_base_field()
    kt = PolynomialRing(k, "r919_eta")
    tpoly = kt.gen()
    items = list(poly.dict().items())
    assert items and poly.parent().ngens() == 2
    right_degree = max(int(exponent[1]) for exponent, coefficient in items)
    total_degree = max(int(exponent[0]+exponent[1])
                       for exponent, coefficient in items)
    coefficients = [kt.zero() for _ in range(total_degree+1)]
    for exponent, coefficient in items:
        i, j = int(exponent[0]), int(exponent[1])
        coefficients[i+j] += k(coefficient)*tpoly**(12*(right_degree-j))
    modulus = B.polynomial()
    polynomial_ring = modulus.parent()
    rational_polynomial_ring = K.gen().numerator().parent()
    lift = polynomial_ring([K(rational_polynomial_ring(c.list()))
                            for c in coefficients])
    progress("r919: original eta48 polynomial reduction start",
             label=label, input_degree=total_degree, base_shift=12*right_degree)
    remainder = lift % modulus
    assert remainder.degree() < modulus.degree()
    value = B.zero()
    for coefficient in reversed(remainder.list()):
        value = value*T+B(coefficient)
    progress("r919: original eta48 polynomial reduction complete",
             label=label, reduced_degree=int(remainder.degree()))
    return value, right_degree


def recover_original_middle(prime, terms, B, T, V, evaluate_phi, progress):
    leading, constant, universal_record = universal_linear_remainder(
        prime, terms, progress)
    t = B(B.base_field().gen())
    assert T != V and V == T/t**12
    A, shift_A = eta_scaled_evaluation(leading, B, T, progress, "linear leading")
    B0, shift_B = eta_scaled_evaluation(constant, B, T, progress, "linear constant")
    assert A != 0
    progress("r919: single original field inversion start")
    U = -(B0/A)*t**(12*(shift_A-shift_B))
    progress("r919: complete first original Phi17 identity start")
    assert evaluate_phi(terms, T, U, B.zero()) == 0
    progress("r919: complete second original Phi17 identity start")
    assert evaluate_phi(terms, U, V, B.zero()) == 0
    assert U != T and U != V
    record = dict(universal_record)
    record.update({
        "specialized_linear_leading_nonzero":True,
        "both_complete_original_Phi17_identities":True,
        "middle_coordinate_distinct_from_endpoints":True,
        "eta_scaling_exponent":12*(shift_A-shift_B)})
    progress("r919: exact unique original middle coordinate certified", **record)
    return U, record
