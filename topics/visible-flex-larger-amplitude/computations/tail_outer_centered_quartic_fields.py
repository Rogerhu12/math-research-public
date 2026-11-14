"""Two certified interval evaluations of exactly the same R48 quartic.

The old weighted_panel_fields remains authoritative for the height primitive.
For k and its actual derivative, intersect its five-basis interval value with
the exact quartic expanded and recentered at the panel midpoint.  Only the
enclosure changes; the unique exact bubble, true moments, endpoints and g do
not.  No source, root, residual, acceptance, or angle mode is replaced.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from fractions import Fraction as F
from math import comb

from flint import acb, arb
from tail_outer_weighted_compatible import (
    intersection, weighted_panel_fields as original_weighted_panel_fields)


def quartic_coefficients(candidate, mode):
    a, b, lam = (candidate["left"], candidate["right"],
                 candidate["bubble_coefficient"][mode])
    A, B, C, D = a["K"][mode], a["Ku"][mode], b["K"][mode], b["Ku"][mode]
    # q00=1-3u²+2u³, q10=u-2u²+u³, q01=3u²-2u³,
    # the right-derivative basis is -q11=-u²+u³, and b=u²-2u³+u⁴.
    return (A, B, -3*A-2*B+3*C-D+lam,
            2*A+B-2*C+D-2*lam, lam)


def centered_range(coefficients, u):
    midpoint = u.mid()
    delta = u-midpoint
    shifted = [
        sum((comb(i, j)*coefficients[i]*midpoint**(i-j)
             for i in range(j, len(coefficients))), arb(0))
        for j in range(len(coefficients))]
    # Arb integer powers retain nonnegativity for the even centered powers.
    return sum((coefficient*delta**j for j, coefficient in enumerate(shifted)),
               arb(0))


def weighted_panel_fields(candidate, *, u, u_x, prefix_moments, suffix_moments):
    H, K, Kx = original_weighted_panel_fields(candidate, u=u, u_x=u_x,
        prefix_moments=prefix_moments, suffix_moments=suffix_moments)
    u = intersection(u, arb(0).union(arb(1)))
    for m in sorted(candidate["left"]["K"]):
        coefficients = quartic_coefficients(candidate, m)
        derivative = [i*coefficients[i] for i in range(1, len(coefficients))]
        k = centered_range(coefficients, u)/2
        kx = u_x*centered_range(derivative, u)/2
        K[m] = K[-m] = acb(intersection(K[m].real, k))
        Kx[m] = Kx[-m] = acb(intersection(Kx[m].real, kx))
    return H, K, Kx


def rational_identity_checks():
    """Exact five-basis polynomial/derivative identities, without Arb or g."""
    cases = 0
    for basis in range(5):
        inputs = [F(int(i == basis)) for i in range(5)]
        A, B, C, D, lam = inputs
        coeffs = [A, B, -3*A-2*B+3*C-D+lam,
                  2*A+B-2*C+D-2*lam, lam]
        for u in map(F, (0, F(1, 7), F(1, 3), F(1, 2), F(6, 7), 1)):
            original = (A*(1-u)**2*(1+2*u)+B*u*(1-u)**2+
                        C*u*u*(3-2*u)-D*u*u*(1-u)+lam*u*u*(1-u)**2)
            original_derivative = (A*(-6*u+6*u*u)+B*(1-4*u+3*u*u)+
                                   C*(6*u-6*u*u)-D*(2*u-3*u*u)+
                                   lam*(2*u-6*u*u+4*u**3))
            if original != sum(c*u**i for i, c in enumerate(coeffs)):
                raise AssertionError("The exact R48 quartic identity is false")
            if original_derivative != sum(i*coeffs[i]*u**(i-1) for i in range(1, 5)):
                raise AssertionError("The exact same-polynomial derivative identity is false")
            cases += 1
    return dict(exact_rational_basis_and_derivative_cases=cases,
                same_unique_R48_polynomial_and_chain_derivative=True,
                true_source_or_radial_evaluations=0)
