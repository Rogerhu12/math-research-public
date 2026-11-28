#!/usr/bin/env python3
"""Exact majorants for R98 time refinement of the true R53 Cartesian field.

This module contains no source-acceptance gate and calls no numerical oracle.
Its rational inputs must be supplied by a genuine complete-field reader.
The angular-four bound is new; an existing angular 0..3 table is never
relabelled.  Vector bounds use the Euclidean norm and every sum/product is
performed in Fraction.  Floats are deliberately rejected by this layer.
"""
from fractions import Fraction as Q
from math import factorial, isqrt

PI_LOWER = Q(1231847548, 392109375)
PI_UPPER = Q(22, 7)
SIX = ((0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2))
NEEDED = tuple((r, j) for r in range(3) for j in range(5-r))


def exact(value):
    if isinstance(value, float):
        raise TypeError('Convert literal binary inputs explicitly before exact arithmetic')
    return Q(value)


def positive(value, name, *, zero=False):
    value = exact(value)
    if value < 0 or (value == 0 and not zero):
        raise ValueError(name+' must be '+('nonnegative' if zero else 'positive'))
    return value


def sqrt_upper(value, bits=80):
    """A proved dyadic upper bound, including equality for exact squares."""
    value = positive(value, 'squared norm', zero=True)
    if type(bits) is not int or bits < 1:
        raise ValueError('Use a positive exact dyadic precision')
    numerator = value.numerator << (2*bits)
    root = isqrt(numerator//value.denominator)
    if root*root*value.denominator < numerator:
        root += 1
    result = Q(root, 1 << bits)
    if result*result < value:
        raise ArithmeticError('The exact square-root upper inequality failed')
    return result


def true_core_bounds(coefficients, *, homotopy, halfwidth, transition, curvature):
    """Complete true-material derivatives Gamma^(j), j=0,...,5.

    The support is 1+sum a_j cos(3(j+1) phi), curvature_blend=1.
    The original true integral and its fixed threefold center are required.
    The bound Gamma<=44/35 follows from unit speed and exact C3 covariance:
    sqrt(3)|Gamma(u)| <= 2*pi/3, pi<22/7, sqrt(3)>5/3.
    It is not a choice of a new origin or a rounded Gauss position.
    """
    lam, S, b, k = map(exact, (homotopy, halfwidth, transition, curvature))
    a = list(map(exact, coefficients))
    if (not a or not 0 <= lam <= 1 or min(S, b, k) <= 0
            or not S+b < PI_LOWER/3):
        raise ValueError('Require the entire cosine support and the true R53 window')
    modes = [3*(j+1) for j in range(len(a))]
    c = [(1-m*m)*v for m, v in zip(modes, a)]
    B = [sum((abs(v)*m**j for m, v in zip(modes, c)), Q(0)) for j in range(4)]
    r = 1-B[0]
    if r <= 0:
        raise ValueError('The complete support l1 inverse bound must be positive')
    d = S+b/2
    denominator = PI_LOWER/3-d
    beta = d*max(abs(k-1/r), abs(k-1/(1+B[0])))/denominator
    q = [1/r, B[1]/r**3,
         B[2]/r**4+3*B[1]**2/r**5,
         B[3]/r**5+10*B[1]*B[2]/r**6+15*B[1]**3/r**7]
    W1, W2, W3 = Q(630, 256)/b, Q(2520, 64)/b**2, Q(2205, 4)/b**3
    gap = q[0]+k+beta
    K = [max(q[0], k)+lam*beta,
         q[1]+lam*W1*gap,
         q[2]+2*lam*W1*q[1]+lam*W2*gap,
         q[3]+3*lam*W1*q[2]+3*lam*W2*q[1]+lam*W3*gap]
    G = [Q(44, 35), Q(1), K[0], K[1]+K[0]**2,
         K[2]+K[0]**3+3*K[0]*K[1],
         6*K[0]**2*K[1]+K[3]+K[0]**4+4*K[0]*K[2]+3*K[1]**2]
    return dict(support_coefficients=a, support_frequencies=modes,
        support_radius_derivative_l1=B, support_rho_lower=r,
        original_kappa_derivatives=q, normalization_denominator_lower=denominator,
        beta_absolute=beta, window_derivative_bounds=[W1, W2, W3],
        kappa_material_derivatives=K, gamma_material_derivatives=G,
        held_circle_center_norm_upper=G[0]+1/k,
        homotopy=lam, halfwidth=S, transition=b, curvature=k,
        true_integral_and_fixed_threefold_center_required=True,
        numerical_position_or_beta_substituted=False)


def composed_fourth(gamma, inlet_e):
    """Fourth psi derivative of Gamma(psi-E0*sin(3psi)/3)."""
    G = list(map(exact, gamma))
    if len(G) < 5 or any(x < 0 for x in G):
        raise ValueError('Require complete nonnegative Gamma derivatives through four')
    e = abs(exact(inlet_e))
    if e >= 1:
        raise ValueError('The literal inlet chart must be strictly monotone')
    rho, rp, rpp, rppp = 1+e, 3*e, 9*e, 27*e
    return (rho**4*G[4]+6*rho*rho*rp*G[3]
            +(3*rp*rp+4*rho*rpp)*G[2]+rppp*G[1])


def center_second_fourth(gamma, inlet_e, inlet_epp):
    """Fourth angular derivative of b(psi) Gamma'(theta0(psi))."""
    G = list(map(exact, gamma))
    if len(G) != 6 or any(x < 0 for x in G):
        raise ValueError('The center second radial jet needs Gamma through five')
    e, epp = abs(exact(inlet_e)), abs(exact(inlet_epp))
    if e >= 1:
        raise ValueError('The literal inlet chart must be strictly monotone')
    rho, rp, rpp, rppp = 1+e, 3*e, 9*e, 27*e
    b0, b1, b2, b3, b4 = epp/3, epp, 3*epp, 9*epp, 27*epp
    return (b4*G[1]+(4*b3*rho+6*b2*rp+4*b1*rpp+b0*rppp)*G[2]
        +(6*b2*rho*rho+12*b1*rho*rp+b0*(3*rp*rp+4*rho*rpp))*G[3]
        +(4*b1*rho**3+6*b0*rho*rho*rp)*G[4]+b0*rho**4*G[5])


def angular_fourth(core, inlet_e, inlet_epp, projection_fourth,
                   raw_center_fourth, center_lift_radial):
    """New complete lift/center order-four bounds; lower tables stay intact."""
    G = core['gamma_material_derivatives']
    projection_fourth = positive(projection_fourth, 'full projection fourth bound', zero=True)
    raw = [positive(x, 'full endpoint fourth bound', zero=True) for x in raw_center_fourth]
    radial = list(map(exact, center_lift_radial))
    if len(raw) != 3 or len(radial) != 3:
        raise ValueError('All three actual radial endpoint jets are required')
    target0 = composed_fourth(G, inlet_e)
    lift = target0+composed_fourth([Q(1)]*6, inlet_e)+projection_fourth
    targets = [target0, Q(0), center_second_fourth(G, inlet_e, inlet_epp)]
    centers = [targets[j]+raw[j]+abs(radial[j])*lift for j in range(3)]
    return dict(lift_fourth=lift, center_fourth=centers,
        center_target_fourth=targets, complete_initial_projection_fourth=projection_fourth,
        full_finite_endpoint_fourth=raw, old_orders_zero_through_three_relabelled=False)


def _add(*series):
    n = min(map(len, series))
    return [sum((row[j] for row in series), Q(0)) for j in range(n)]


def _scale(series, value):
    return [exact(value)*x for x in series]


def _product(left, right):
    n = min(len(left), len(right))
    return [sum((left[j]*right[k-j] for j in range(k+1)), Q(0)) for k in range(n)]


def _derivative(series):
    return [(j+1)*series[j+1] for j in range(len(series)-1)]


def inverse_chart_series(chart, degree=4):
    """Nonnegative Taylor majorants in psi, coefficients bound f^(j)/j!.

    V=1/rho, U=e' sin(3psi)/(3rho), and the exact inverse second radial jet is
    A=(e'' sin/3+2e' cos U-3e sin U^2)/rho. Its final minus sign is discarded
    only for an absolute majorant. No radial derivative above e'' is used.
    """
    E = [positive(x, 'chart derivative bound', zero=True) for x in chart]
    if len(E) != 3 or E[0] >= 1 or type(degree) is not int or degree < 2:
        raise ValueError('Require a complete invertible chart two-jet and degree >=2')
    n, lower = degree+1, 1-E[0]
    trig = [Q(3**j, factorial(j)) for j in range(n)]
    radius = [Q(0)]+[E[0]*trig[j] for j in range(1, n)]
    V = [1/lower]
    for k in range(1, n):
        V.append(sum((radius[j]*V[k-j] for j in range(1, k+1)), Q(0))/lower)
    U = _scale(_product(trig, V), E[1]/3)
    A = _product(_add(_scale(trig, E[2]/3),
        _scale(_product(trig, U), 2*E[1]),
        _scale(_product(trig, _product(U, U)), 3*E[0])), V)
    return dict(rho_lower=lower, V=V, U=U, A=A,
        coefficients_are_absolute_derivative_over_factorial=True,
        unused_radial_third_derivative_required=False)


def physical_theta_jets(same_psi, chart):
    """Bounds F_(s^r theta^j), r=0..2, r+j<=4, at fixed physical theta.

    The input contains every rectangular X_(s^r psi^j), r<=2, j<=4-r.
    Apply V*d/dpsi to F, F_s=X_s+U X_psi and
    F_ss=X_ss+2U X_spsi+U^2 X_psipsi+A X_psi.
    All coefficient series are absolute majorants, not rounded sampled jets.
    """
    if set(same_psi) != set(NEEDED):
        raise ValueError('Every required original Cartesian mixed derivative is mandatory')
    values = {key:positive(v, 'Cartesian mixed derivative bound', zero=True)
              for key, v in same_psi.items()}
    inverse = inverse_chart_series(chart)
    U, V, A = (inverse[key] for key in ('U', 'V', 'A'))
    X = [[values[r, j]/factorial(j) for j in range(5-r)] for r in range(3)]
    first = _add(X[1], _product(U, _derivative(X[0])))
    second = _add(X[2], _scale(_product(U, _derivative(X[1])), 2),
        _product(_product(U, U), _derivative(_derivative(X[0]))),
        _product(A, _derivative(X[0])))
    result = {}
    for r, row in enumerate((X[0], first, second)):
        for j in range(5-r):
            if not row:
                raise ArithmeticError('A physical-angle derivative lost its complete remainder')
            result[r, j] = row[0]
            if j < 4-r:
                row = _product(V, _derivative(row))
    return result, inverse


def time_bounds(physical, *, phase_end, curvature, center_norm, radius_lower):
    """R98 M2, M_g,2 and V_g,1 for a complete physical-s chart component.

    g=ds^2+a(s)^2 dtheta^2 and alpha(t)=phase_end*t. The physical derivative
    rectangle is complete. The coordinate C2 norm uses the full Jacobian
    Frobenius and full symmetric Hessian Frobenius bounds, so it also bounds
    the corresponding operator and bilinear norms.
    """
    if set(physical) != set(NEEDED):
        raise ValueError('Require complete physical mixed derivatives through R98 order four')
    P = {key:positive(v, 'physical mixed derivative bound', zero=True)
         for key, v in physical.items()}
    omega = positive(phase_end, 'affine phase endpoint')
    k = positive(curvature, 'actual circular curvature')
    center = positive(center_norm, 'true held-circle center bound', zero=True)
    a = positive(radius_lower, 'true target radius lower bound')
    T = {}
    for r, j in SIX:
        T[r, j] = omega**2*(k*k*P[r, j]+2*k*P[r, j+1]+P[r, j+2]
            +(k*k*center if (r, j) == (0, 0) else 0))
    C1 = sqrt_upper(T[1, 0]**2+T[0, 1]**2)
    C2 = sqrt_upper(T[2, 0]**2+2*T[1, 1]**2+T[0, 2]**2)
    M2 = max(T[0, 0], C1, C2)
    Mg2 = sqrt_upper(T[1, 0]**2+(T[0, 1]/a)**2)
    first = [omega*(k*P[1, 0]+P[1, 1]), omega*(k*P[0, 1]+P[0, 2])/a]
    Vg1 = sqrt_upper(first[0]**2+first[1]**2)
    return dict(time_second_six_jets=T, coordinate_C2_time_second=M2,
        normalized_jacobian_time_second=Mg2, normalized_jacobian_time_first=Vg1,
        true_target_radius_lower=a, affine_phase_end=omega, circular_curvature=k,
        exact_held_circle_center_bound=center,
        coordinate_norm='max(position Euclidean, Jacobian Frobenius, symmetric Hessian Frobenius)',
        normalized_norm='3 by 2 operator bounded by Frobenius')


def minimum_metric_intervals(endpoint_error, target, velocity):
    """Smallest positive integer n verified by eta+V^2/(4n^2)<=target."""
    eta = positive(endpoint_error, 'endpoint metric error', zero=True)
    tau = positive(target, 'target metric error')
    V = positive(velocity, 'normalized time velocity', zero=True)
    if eta >= tau:
        raise ValueError('Time refinement needs a strictly positive endpoint metric margin')
    q = V*V/(4*(tau-eta))
    n = max(1, isqrt(q.numerator//q.denominator))
    if Q(n*n) < q:
        n += 1
    if eta+V*V/Q(4*n*n) > tau:
        raise ArithmeticError('The exact endpoint-Gram time-step inequality failed')
    return n
