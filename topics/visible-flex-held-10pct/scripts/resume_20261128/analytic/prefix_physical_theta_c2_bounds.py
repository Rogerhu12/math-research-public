#!/usr/bin/env python3
"""Exact scalar bounds for a complete Cartesian prefix in physical theta.

This module has no source-acceptance gate and performs no numerical solve.
Its inputs are exact rational bounds supplied by the genuine fixed-pair
entry. All arithmetic below is rational; the displayed floats are not used
as bounds. See the accompanying same-material-theta proof.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
import math


PI_LOWER = Q(1231847548, 392109375)
PI_UPPER = Q(22, 7)
SIX = ((0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2))
NEEDED = tuple(sorted(set(SIX) | {(a, b + 1) for a, b in SIX}))
HERMITE = (
    (Q(1), Q(0), Q(0), Q(-10), Q(15), Q(-6)),
    (Q(0), Q(1), Q(0), Q(-6), Q(8), Q(-3)),
    (Q(0), Q(0), Q(1, 2), Q(-3, 2), Q(3, 2), Q(-1, 2)),
)


def affine(poly, start, scale):
    """Coefficients of p(start+scale*t), including negative scale."""
    return [scale**k * sum((poly[j] * math.comb(j, k) * start**(j-k)
                           for j in range(k, len(poly))), Q(0))
            for k in range(len(poly))]


def difference(left, right):
    return [(right[j] if j < len(right) else Q(0))
            - (left[j] if j < len(left) else Q(0))
            for j in range(max(len(left), len(right)))]


@dataclass(frozen=True)
class Pair:
    """Bounds max(|left|,|right|) <= size and |right-left| <= delta.

    The same algebra applies to a vector multiplied by a scalar. No vector
    product is used. Signs are intentionally discarded only after the
    defining analytic expression has been specified.
    """
    size: Q
    delta: Q

    def __post_init__(self):
        if self.size < 0 or self.delta < 0:
            raise ValueError('Bounds must be nonnegative')

    @staticmethod
    def cast(value):
        return value if isinstance(value, Pair) else Pair(abs(Q(value)), Q(0))

    def __add__(self, other):
        other = self.cast(other)
        return Pair(self.size + other.size, self.delta + other.delta)

    __radd__ = __add__
    __sub__ = __add__

    def __mul__(self, other):
        other = self.cast(other)
        return Pair(self.size * other.size,
                    self.size * other.delta + other.size * self.delta)

    __rmul__ = __mul__


def true_core_pair(left, right, *, homotopy, halfwidth, transition, curvature):
    """Global same-material-u difference bounds for the true R53 core.

    Both cores have the same lambda,S,b,k, curvature_blend=1, cosine support,
    threefold center and material origin. The positive l1 inverse bound is
    already required by the currently bound true-core angular oracle.
    """
    lam, S, b, k = map(Q, (homotopy, halfwidth, transition, curvature))
    if not (0 <= lam <= 1 and S > 0 and b > 0 and k > 0
            and S+b < PI_LOWER/3):
        raise ValueError('Use one common valid literal R53 window and target')
    count = max(len(left), len(right))
    a = [list(map(Q, values)) + [Q(0)]*(count-len(values)) for values in (left, right)]
    modes = [3*(j+1) for j in range(count)]
    coefficients = [[(1-m*m)*v for m,v in zip(modes, values)] for values in a]
    radii = [sum(map(abs, values), Q(0)) for values in coefficients]
    rho = 1-max(radii)
    if rho <= 0:
        raise ValueError('The bound true-core oracle requires positive support l1 rho')
    rho_upper = 1+max(radii)
    dc = [r-l for l,r in zip(*coefficients)]
    B = [max(sum((m**j*abs(v) for m,v in zip(modes, values)), Q(0))
             for values in coefficients) for j in range(4)]
    D = [sum((m**j*abs(v) for m,v in zip(modes, dc)), Q(0)) for j in range(3)]
    phase0 = sum((abs(v)/m for m,v in zip(modes, dc)), Q(0))/rho
    dr, dr1, dr2 = (D[j]+B[j+1]*phase0 for j in range(3))
    dk0 = dr/rho**2
    dk0u = dr1/rho**3 + 3*B[1]*dr/rho**4
    dk0uu = (dr2/rho**4 + 4*B[2]*dr/rho**5
               + 6*B[1]*dr1/rho**5 + 15*B[1]**2*dr/rho**6)
    c = S+b/2
    denominator = PI_LOWER/3-c
    dbeta = phase0/denominator
    beta = c*max(abs(1/rho-k), abs(1/rho_upper-k))/denominator
    W1, W2 = Q(630,256)/b, Q(2520,64)/b**2
    K0u = B[1]/rho**3
    K0uu = B[2]/rho**4 + 3*B[1]**2/rho**5
    K = max(k,1/rho)+lam*beta
    Ku = K0u+lam*W1*(1/rho+k+beta)
    Kuu = K0uu+2*lam*W1*K0u+lam*W2*(1/rho+k+beta)
    dk = dk0+lam*dbeta
    dku = dk0u+lam*W1*(dk0+dbeta)
    dkuu = dk0uu+2*lam*W1*dk0u+lam*W2*(dk0+dbeta)
    # Combine the beta and partial-window integral before taking absolute
    # values; their common kernel has L1 norm at most 1+lambda.
    phase = (1+lam)*phase0
    G = [Q(44,35)*phase,
         phase,
         dk+K*phase,
         dku+2*K*dk+(Ku+K*K)*phase]
    return dict(support_l1_left=radii[0], support_l1_right=radii[1],
        support_rho_lower=rho, normal_phase_difference=phase0,
        true_material_phase_difference=phase, true_beta_difference=dbeta,
        true_beta_absolute=beta, kappa_absolute=K, kappa_u_absolute=Ku,
        kappa_uu_absolute=Kuu, kappa_difference=dk, kappa_u_difference=dku,
        kappa_uu_difference=dkuu, core_derivative_differences=G,
        normalization_denominator_lower=denominator,
        same_homotopy=lam, same_halfwidth=S, same_transition=b, same_target_curvature=k,
        numerical_Gauss_position_error_included=False,
        true_integral_core_and_fixed_threefold_center=True)


def inverse_chart(E, delta):
    """Bounds for psi_s,psi_theta and their second derivatives at same theta."""
    E, delta = list(map(Q,E)), list(map(Q,delta))
    if len(E) != 3 or len(delta) != 3 or min(E+delta) < 0 or E[0] >= 1:
        raise ValueError('A complete invertible chart two-jet is required')
    rho = 1-E[0]
    phase = delta[0]/(3*rho)
    trig = min(Q(2),3*phase)
    drho = delta[0]+E[0]*trig
    reciprocal = Pair(1/rho,drho/rho**2)
    e, ep, epp = (Pair(a,d) for a,d in zip(E,delta))
    sine = cosine = Pair(Q(1),trig)
    u = ep*sine*reciprocal*Q(1,3)
    v = reciprocal
    a = (epp*sine*Q(1,3)+2*ep*cosine*u+3*e*sine*u*u)*reciprocal
    b = (ep*cosine+3*e*sine*u)*reciprocal*reciprocal
    c = 3*e*sine*reciprocal*reciprocal*reciprocal
    return dict(phase=phase, rho_lower=rho, rho_difference=drho,
                psi_s=u, psi_theta=v, psi_ss=a, psi_s_theta=b, psi_theta_theta=c)


def physical_theta_pair(same_psi, absolute, E, delta):
    """Transport all six Cartesian jet differences to identical (s,theta)."""
    chart = inverse_chart(E,delta)
    x = {key:Pair(absolute[key], same_psi[key]+absolute[(key[0],key[1]+1)]*chart['phase'])
         for key in SIX}
    u,v,a,b,c = (chart[key] for key in
        ('psi_s','psi_theta','psi_ss','psi_s_theta','psi_theta_theta'))
    values = {
        (0,0):x[0,0],
        (1,0):x[1,0]+x[0,1]*u,
        (0,1):x[0,1]*v,
        (2,0):x[2,0]+2*x[1,1]*u+x[0,2]*u*u+x[0,1]*a,
        (1,1):x[1,1]*v+x[0,2]*u*v+x[0,1]*b,
        (0,2):x[0,2]*v*v+x[0,1]*c,
    }
    return {key:values[key].delta for key in SIX},chart


def radial_weights(left, right, *, center_width, end, cut_width, algebra):
    """Exact Bernstein bounds for identical center/cut weights on one span."""
    width = right-left
    if width <= 0:
        raise ValueError('Require a nonempty common physical-s interval')
    result = []
    for role in ('center','cut'):
        active = (right <= center_width if role == 'center' else left >= end-cut_width)
        inactive = (left >= center_width if role == 'center' else right <= end-cut_width)
        if not (active or inactive):
            raise ValueError('The common partition must split both exact repair joins')
        rows = [[Q(0)]*3 for _ in range(3)]
        if active:
            scale = center_width if role == 'center' else cut_width
            start = left/scale if role == 'center' else (end-left)/scale
            step = width/scale if role == 'center' else -width/scale
            for j,poly in enumerate(HERMITE):
                c = [v*((scale if role == 'center' else -scale)**j)
                     for v in affine(poly,start,step)]
                for order in range(3):
                    rows[order][j] = algebra.bernstein_abs(c)
                    c = algebra.derivative(c,width)
        result.append(rows)
    return result
