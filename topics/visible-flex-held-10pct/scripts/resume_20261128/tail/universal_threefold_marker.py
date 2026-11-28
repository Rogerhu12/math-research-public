"""The exact rational all-harmonic marker of R67, with Cartesian two-jets.

The mathematical function is epsilon*(1-|z/r|^2)_+^3 times the real
part of (z/r)^3/(1-(z/r)^3/2). No Fourier series is truncated. This module
evaluates that fixed C2 cap; it does not assert that an input closed surface
has already paid its support, curvature, moment or held-set obligations.
"""
from fractions import Fraction
import math

import numpy as np


def downward_float(value):
    """A binary64 number no larger than the positive exact rational value."""
    value = Fraction(value)
    result = float(value)
    if not math.isfinite(result) or result <= 0:
        raise ValueError('The exact marker amplitude has no positive finite binary64 value')
    if Fraction(result) > value:
        result = math.nextafter(result, 0.)
    if not 0 < Fraction(result) <= value:
        raise ValueError('The downward-rounded marker amplitude is not positive')
    return result


class UniversalThreefoldMarker:
    def __init__(self, radius, amplitude=None):
        self.radius = float(radius)
        if not math.isfinite(self.radius) or self.radius <= 0:
            raise ValueError('A positive finite cap radius is required')
        r = Fraction(self.radius)
        self.limit = min(Fraction(1, 100000), r*r/10000)
        self.amplitude = downward_float(self.limit) if amplitude is None else float(amplitude)
        if (not math.isfinite(self.amplitude) or
                not 0 < Fraction(self.amplitude) <= self.limit):
            raise ValueError('The positive marker amplitude must satisfy the exact R67 bound')

    def jets(self, x, y):
        """Return f, grad f and Hessian f in the same physical x,y chart."""
        x, y = float(x), float(y)
        if not math.isfinite(x) or not math.isfinite(y):
            raise ValueError('Finite Cartesian query coordinates are required')
        r, eps = self.radius, self.amplitude
        # Normalized coordinates avoid overflow in x*x+y*y for outside points.
        xx, yy = x/r, y/r
        if not math.isfinite(xx) or not math.isfinite(yy) or math.hypot(xx, yy) >= 1.:
            return 0., np.zeros(2), np.zeros((2, 2))
        z = complex(xx, yy)
        d = 1-z**3/2
        analytic = z**3/d
        first = 3*z*z/(d*d)
        second = 6*z/(d*d)+9*z**4/(d*d*d)
        h = analytic.real
        gh = np.asarray([first.real, -first.imag])/r
        Hh = np.asarray([[second.real, -second.imag],
                         [-second.imag, -second.real]])/(r*r)
        v = np.asarray([xx, yy])
        u = 1-xx*xx-yy*yy
        b = u**3
        gb = -6*u*u*v/r
        Hb = (24*u*np.outer(v, v)-6*u*u*np.eye(2))/(r*r)
        value = eps*b*h
        gradient = eps*(b*gh+h*gb)
        hessian = eps*(b*Hh+h*Hb+np.outer(gb, gh)+np.outer(gh, gb))
        if not (math.isfinite(value) and np.all(np.isfinite(gradient)) and
                np.all(np.isfinite(hessian))):
            raise FloatingPointError('Nonfinite marker two-jet; no cap was accepted')
        return float(value), gradient, hessian

    def moment_coefficient(self, j):
        """B_(3j)/pi as an exact positive rational for the chosen literal inputs.

        This is the cap contribution in R67. It does not evaluate the unknown
        activity moment or by itself prove that a complete family changes shape.
        """
        if not isinstance(j, int) or isinstance(j, bool) or j < 1:
            raise ValueError('A positive integer harmonic index is required')
        n = 3*j
        return (6*Fraction(self.amplitude)*Fraction(1, 2**(j-1))*
                Fraction(self.radius)**(n+2)/((n+1)*(n+2)*(n+3)*(n+4)))

    def metadata(self):
        r, eps = Fraction(self.radius), Fraction(self.amplitude)
        return dict(
            definition='epsilon*(1-|z/r|^2)_+^3*Re((z/r)^3/(1-(z/r)^3/2))',
            radius=self.radius, radius_exact_binary=str(r),
            amplitude=self.amplitude, amplitude_exact_binary=str(eps),
            exact_amplitude_upper=str(self.limit),
            amplitude_bound_checked_exactly=True,
            all_harmonics_retained_by_rational_function=True,
            symmetry_order=3, boundary_cartesian_two_jet_exactly_zero=True,
            height_absolute_upper_exact=str(2*eps),
            gradient_norm_upper_exact=str(24*eps/r),
            hessian_operator_upper_exact=str(252*eps/(r*r)),
            diameter_increase_upper_exact=str(4*eps),
            cap_principal_curvature_upper_exact=str(252*eps/(r*r)),
            first_cap_moment_divided_by_pi_exact=str(self.moment_coefficient(1)),
            analytical_source='results/R67-universal-threefold-marker-and-euclidean-noncongruence.md',
            numerical_evaluation_is_outward_rounded=False,
            complete_surface_geometry_paid=False,
            activity_moment_or_noncircular_core_verified=False,
            euclidean_noncongruence_paid=False)
