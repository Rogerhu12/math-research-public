"""R910: exact original RR algebra without a gcd in the degree48 field.

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
    progress("r910: separability specialization start", label=label, degree=degree)
    tested = 0
    for extension_degree in (1, 2, 3):
        field = k if extension_degree == 1 else GF(p**extension_degree, "r910_alpha")
        ring = PolynomialRing(field, "r910_z")
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
            progress("r910: generic separability certified by specialization", **record)
            return record
    raise ArithmeticError("No squarefree specialization found in the bounded search; no claim of inseparability.")


_UNIVERSAL = {}


def universal_linear_subresultant(prime, terms, progress):
    """The exact first nonzero linear subresultant of the two original relations."""
    key = (int(prime), digest([[int(i), int(j), str(c)]
                              for (i, j), c in sorted(terms.items())]))
    if key in _UNIVERSAL:
        return _UNIVERSAL[key]
    k = GF(prime)
    coefficient_ring = PolynomialRing(
        k, names=("r910_left", "r910_right"), order="degrevlex")
    left, right = coefficient_ring.gens()
    polynomial_ring = PolynomialRing(coefficient_ring, "r910_middle")
    first_coefficients = [coefficient_ring.zero() for _ in range(19)]
    second_coefficients = [coefficient_ring.zero() for _ in range(19)]
    for (i, j), coefficient in terms.items():
        first_coefficients[j] += k(coefficient)*left**i
        second_coefficients[i] += k(coefficient)*right**j
    first = polynomial_ring(first_coefficients)
    second = polynomial_ring(second_coefficients)
    assert first.degree() == second.degree() == 18
    assert first.leading_coefficient() == second.leading_coefficient() == 1
    progress("r910: universal polynomial subresultants start", prime=int(prime),
             middle_degree=18, coefficient_ring=str(coefficient_ring),
             conversion="direct univariate coefficient vectors")
    chain = first.subresultants(second)
    degree_list = [int(f.degree()) for f in chain]
    linear = [f for f in chain if f.degree() == 1]
    if not linear:
        raise ArithmeticError("No linear universal subresultant; no original U certificate.")
    original = linear[0]
    leading, constant = original[1], original[0]
    diagonal_power = 0
    diagonal = left-right
    while True:
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
        "method":"universal original Phi17 linear subresultant",
        "subresultant_middle_degrees":degree_list,
        "linear_subresultants":len(linear),
        "cancelled_diagonal_power":diagonal_power,
        "uncancelled_subresultant_sha256":digest({
            "leading":poly_terms(original[1]), "constant":poly_terms(original[0])}),
        "linear_relation_sha256":digest({
            "leading":poly_terms(leading), "constant":poly_terms(constant)}),
        "leading_terms":len(leading.dict()), "constant_terms":len(constant.dict())}
    progress("r910: universal original linear relation complete", **record)
    answer = (leading, constant, record)
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
    kt = PolynomialRing(k, "r910_eta")
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
    progress("r910: original eta48 polynomial reduction start",
             label=label, input_degree=total_degree, base_shift=12*right_degree)
    remainder = lift % modulus
    assert remainder.degree() < modulus.degree()
    value = B.zero()
    for coefficient in reversed(remainder.list()):
        value = value*T+B(coefficient)
    progress("r910: original eta48 polynomial reduction complete",
             label=label, reduced_degree=int(remainder.degree()))
    return value, right_degree


def recover_original_middle(prime, terms, B, T, V, evaluate_phi, progress):
    leading, constant, universal_record = universal_linear_subresultant(
        prime, terms, progress)
    t = B(B.base_field().gen())
    assert T != V and V == T/t**12
    A, shift_A = eta_scaled_evaluation(leading, B, T, progress, "linear leading")
    B0, shift_B = eta_scaled_evaluation(constant, B, T, progress, "linear constant")
    assert A != 0
    progress("r910: single original field inversion start")
    U = -(B0/A)*t**(12*(shift_A-shift_B))
    progress("r910: complete first original Phi17 identity start")
    assert evaluate_phi(terms, T, U, B.zero()) == 0
    progress("r910: complete second original Phi17 identity start")
    assert evaluate_phi(terms, U, V, B.zero()) == 0
    assert U != T and U != V
    record = dict(universal_record)
    record.update({
        "specialized_linear_leading_nonzero":True,
        "both_complete_original_Phi17_identities":True,
        "middle_coordinate_distinct_from_endpoints":True,
        "eta_scaling_exponent":12*(shift_A-shift_B)})
    progress("r910: exact unique original middle coordinate certified", **record)
    return U, record
