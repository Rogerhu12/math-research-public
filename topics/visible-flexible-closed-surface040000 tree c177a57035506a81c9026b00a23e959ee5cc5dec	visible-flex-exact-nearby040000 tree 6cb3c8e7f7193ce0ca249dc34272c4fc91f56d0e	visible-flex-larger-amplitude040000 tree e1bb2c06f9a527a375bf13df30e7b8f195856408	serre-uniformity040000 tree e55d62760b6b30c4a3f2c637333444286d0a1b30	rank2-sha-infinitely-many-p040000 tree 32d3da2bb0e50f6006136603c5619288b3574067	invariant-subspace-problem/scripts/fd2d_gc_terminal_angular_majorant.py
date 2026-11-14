"""R174 exact finite-coefficient majorants at the completed physical cut.

No body/ODE evaluation is performed. Fractions contain the actual input
coefficients; square-root endpoints are explicit outward dyadic bounds.
The hypotheses and formulas are proved in R174. Standard tail geometry is
accurate rational 4/5,17/50,23/50, not its numerical display labels.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb, isqrt
import numpy as np
from fd2d_dyadic_bernstein_tail import DyadicBernsteinControlBox


def rational(value):
    if isinstance(value, (float, np.floating)):
        return F.from_float(float(value))
    if isinstance(value, (int, np.integer)):
        return F(int(value))
    return F(value)


def sqrt_bounds(value, bits=96):
    value = rational(value)
    if value < 0:
        raise ValueError('A nonnegative square-root argument is required')
    scale = 1 << int(bits)
    n = isqrt((value.numerator*scale*scale)//value.denominator)
    lo = F(n,scale)
    hi = lo if lo*lo == value else F(n+1,scale)
    if not lo*lo <= value <= hi*hi:
        raise ArithmeticError('Invalid outward square-root bounds')
    return lo,hi


def atan_bounds(x, terms):
    x = rational(x)
    if not 0 < x < 1:
        raise ValueError('Use the alternating arctangent expansion inside (0,1)')
    total = sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(int(terms))),F(0))
    next_term = x**(2*terms+1)/F(2*terms+1)
    return (total,total+next_term) if terms % 2 == 0 else (total-next_term,total)


def pi_bounds():
    lo5,hi5 = atan_bounds(F(1,5),8)
    lo239,hi239 = atan_bounds(F(1,239),4)
    return 16*lo5-4*hi239,16*hi5-4*lo239


def bernstein_product(left, right):
    n,m = len(left)-1,len(right)-1
    out = []
    for k in range(n+m+1):
        out.append(sum((F(comb(n,i)*comb(m,k-i),comb(n+m,k))*left[i]*right[k-i]
            for i in range(max(0,k-m),min(n,k)+1)),F(0)))
    return tuple(out)


def tail_curvature_bounds(controls, radius_upper):
    """Global |kappa|,|kappa_y|,|kappa_yy| from exact local degree-23 controls."""
    controls = tuple(rational(v) for v in controls)
    box = DyadicBernsteinControlBox()
    certificate = box.certificate(controls)
    if not certificate['passed']:
        raise ValueError('The actual R170 domain must hold')
    local = box.coefficients_exact(controls)
    width = F(23,50)
    rows = []
    curvature_controls = []
    for j in range(8):
        a,b = F(j,8),F(j+1,8)
        q4 = tuple(a**(4-i)*b**i for i in range(5))
        one_minus_q4 = tuple((1-a)**(4-i)*(1-b)**i for i in range(5))
        envelope = bernstein_product(q4,one_minus_q4)
        e = tuple(F(630,1)/width*v for v in
                  bernstein_product(envelope,local[j*16:(j+1)*16]))
        if len(e) != 24 or min(e) < 0:
            raise ArithmeticError('The exact nonnegative curvature controls were lost')
        first = tuple(F(8*23,1)/width*(e[i+1]-e[i]) for i in range(23))
        second = tuple(F(64*23*22,1)/width**2*(e[i+2]-2*e[i+1]+e[i]) for i in range(22))
        rows.append(dict(interval=j,curvature=max(e),first=max(map(abs,first)),
                         second=max(map(abs,second))))
        curvature_controls.append(e)
    c0 = min(F(4725,736),max(r['curvature'] for r in rows))
    c1 = max(r['first'] for r in rows)
    c2 = max(r['second'] for r in rows)
    radius_upper = rational(radius_upper)
    if radius_upper <= 0:
        raise ValueError('Use a positive radius upper bound')
    M2 = radius_upper**2*c2+radius_upper*c1
    return dict(certificate=certificate,curvature=c0,curvature_y=c1,curvature_yy=c2,
        radius_upper=radius_upper,M0=c0,M2=M2,glaeser_constant=2*M2,
        local_rows=rows,local_curvature_controls=curvature_controls,
        envelope_and_product_degree=[8,15,23],
        constants_are_exact_rational_upper_bounds=True)


def cubic_terminal_K_bounds(length, phase0, tau_upper, *, cut_radius=F(4,5)):
    """K_- tau^3 <= K <= K_+ tau^3 for the R172 cubic terminal phase."""
    L,p0,tau0,ac = map(rational,(length,phase0,tau_upper,cut_radius))
    if not (0 < tau0 <= L/2 and ac > 0):
        raise ValueError('Use a positive terminal window no larger than half the phase bridge')
    pi_lo,pi_hi = pi_bounds()
    dlo,dhi = p0+pi_lo/2,p0+pi_hi/2
    if not 0 < dlo <= dhi:
        raise ValueError('The initial phase must be above the exact -pi/2 cut phase')
    x0 = tau0/L
    theta_upper = 3*dhi*x0*x0
    if theta_upper > 1:
        raise ValueError('This explicit sine lower bound is selected for theta<=1')
    sine_factor = 1-theta_upper*theta_upper/6
    lower = 6*dlo*dlo*(1-x0)*(3-2*x0)*sine_factor/(L**4*(ac+tau0))
    upper = 18*dhi*dhi/(L**4*ac)
    if not 0 < lower <= upper:
        raise ArithmeticError('Invalid cubic curvature bounds')
    return dict(lower=lower,upper=upper,phase_difference_lower=dlo,
        phase_difference_upper=dhi,theta_upper=theta_upper,sine_lower_factor=sine_factor,
        phase_length=L,phase0=p0,tau_upper=tau0,cut_radius=ac,
        radius_lower=ac,radius_upper=ac+tau0,
        pi_lower=pi_lo,pi_upper=pi_hi,
        exact_phase='-pi/2 + Delta*(tau/L)^2*(3-2*tau/L)',
        hypotheses='cubic shared phase with zero endpoint slopes, accurate flat cut, no bump on this window')


def raw_vector_slope_bounds(raw_last_left, modes, length_lower):
    """B_j for r=(raw_n-raw_l,2raw_m), j=0,1,2, with r=(tau/ell)r0."""
    K = int(modes)
    values = tuple(rational(v) for v in raw_last_left)
    ell = rational(length_lower)
    if K < 1 or len(values) != 3*K+2 or ell <= 0:
        raise ValueError('Require the actual last-left Fourier row and a positive exact width lower bound')
    e,d = K+1,2*K+1
    difference = tuple(values[i]-values[d+i] for i in range(e))
    twice_m = tuple(2*values[e+i] for i in range(K))
    result = []
    for order in range(3):
        bound = sum((abs(v)*(2*i)**order for i,v in enumerate(difference)),F(0))
        bound += sum((abs(v)*(2*(i+1))**order for i,v in enumerate(twice_m)),F(0))
        result.append(bound/ell)
    return dict(B0=result[0],B1=result[1],B2=result[2],length_lower=ell,
        raw_difference_coefficients=difference,twice_raw_m_coefficients=twice_m,
        cancellation_before_absolute_value=True,
        norm='Euclidean vector norm bounded by the exact Fourier coefficient l1 sum')


def terminal_angular_majorant(controls, raw_last_left, modes, *,
        cell_length_lower, cell_length_upper, phase_length, phase0):
    """R174 constants for the entire explicitly completed last cell."""
    tau0 = rational(cell_length_upper)
    raw = raw_vector_slope_bounds(raw_last_left,modes,cell_length_lower)
    K = cubic_terminal_K_bounds(phase_length,phase0,tau0)
    tail = tail_curvature_bounds(controls,K['radius_upper'])
    B0,B1,B2 = (raw[key] for key in ('B0','B1','B2'))
    M0,M2 = tail['M0'],tail['M2']
    root_tau = sqrt_bounds(tau0)[1]
    H = 2*sqrt_bounds(K['lower'])[0]
    if H <= 0:
        raise ArithmeticError('Increase square-root precision for this positive curvature lower bound')
    D2 = M2+4*sqrt_bounds(2*M0*M2)[1]+4*M0+B2*tau0
    A = 4*M2+8*M0
    C0 = D2+2*A+2*B1*B1*root_tau/H
    C1 = 2*A*B0/H
    D = B0+2*sqrt_bounds(K['upper'])[1]*root_tau
    V = sqrt_bounds(2*M2+4*M0)[1]
    first_trace = max(2*D*V,V+sqrt_bounds(2*M2)[1])
    V1 = V*sqrt_bounds(M0)[1]+B1*tau0
    alpha0 = F(3,2)*M0+(D+2*B0)*tau0/2
    alpha1 = F(3,2)*V1
    alpha20,alpha21 = C0/2+D2,C1/2
    return dict(schema='fd2d-R174-terminal-angular-integrable-majorant-v1',
        tail=tail,raw=raw,K=K,tau_upper=tau0,
        constants=dict(M0=M0,M2=M2,B0=B0,B1=B1,B2=B2,H_lower=H,
            V2=D2,A=A,h_uu_constant=C0,h_uu_singular=C1,
            h_minus_k_coefficient=D,h_u_minus_k_u_sqrt_coefficient=first_trace,
            alpha_absolute=alpha0,alpha_u_absolute=alpha1,
            alpha_uu_constant=alpha20,alpha_uu_singular=alpha21),
        exact_meaning=dict(h_uu='abs(h_uu)<=C0+C1/sqrt(tau)',
            value_trace='abs(h-k)<=D*tau',
            first_trace='abs(h_u-k_u)<=J*sqrt(tau)+B1*tau',
            alpha_uu='norm(alpha_uu)<=alpha20+alpha21/sqrt(tau)'),
        required_weight='0<=eta<=1, eta independent of u, eta->1',
        actual_Codazzi_metric_body_seam_or_reach_certified=False,
        II_uu_uniform_cut_limit_claimed=False,cut_radial_II_derivative_assigned=False)


def terminal_integrals(majorant, epsilon):
    eps = rational(epsilon)
    if not 0 <= eps <= majorant['tau_upper']:
        raise ValueError('Use an epsilon inside the proved terminal interval')
    c = majorant['constants']
    root = sqrt_bounds(eps)[1]
    return dict(epsilon=eps,
        h_uu_integral=c['h_uu_constant']*eps+2*c['h_uu_singular']*root,
        alpha_uu_integral=c['alpha_uu_constant']*eps+2*c['alpha_uu_singular']*root,
        h_value_trace_error=c['h_minus_k_coefficient']*eps,
        h_first_trace_error=c['h_u_minus_k_u_sqrt_coefficient']*root+c['B1']*eps)


def body_variation_bounds(majorant, initial_bounds, *, epsilon=None):
    """Conditional R124 norms/remainders from genuine input r,b,v,c bounds.

    This is algebra only. No initial value is supplied or inferred here.
    R126 still needs the actual resulting cut jets and alignment errors.
    """
    initial = {key:rational(initial_bounds[key]) for key in ('r','b','v','c')}
    if any(v < 0 for v in initial.values()):
        raise ValueError('Initial quantities must be genuine nonnegative norm upper bounds')
    c = majorant['constants'];t = majorant['tau_upper']
    A0,A1 = c['alpha_absolute'],c['alpha_u_absolute']
    integral = terminal_integrals(majorant,t)['alpha_uu_integral']
    R = initial['r']+A1*t
    B = initial['b']+R*t
    V = initial['v']+R*A1*t+integral
    C = initial['c']+(A1*B+V)*t
    eps = t if epsilon is None else rational(epsilon)
    I = terminal_integrals(majorant,eps)['alpha_uu_integral']
    dr,db = (A0*R+A1)*eps,(A0*B+R)*eps
    dv,dc = (A0*V+R*A1)*eps+I,(A0*C+A1*B+V)*eps
    return dict(conditional_on_actual_initial_bounds=initial,
        uniform_norm_bounds=dict(r=R,b=B,v=V,c=C),epsilon=eps,
        cut_remainders=dict(r=dr,b=db,v=dv,c=dc,
            F=A0*eps,F_u=A0*R*eps+dr,
            F_uu=A0*(V+R*R)*eps+dv+2*R*dr,
            X=eps,X_u=R*eps,X_uu=(V+R*R)*eps),
        skew_energy_used=True,body_integrated=False,
        cut_twojet_agreement_or_R126_budget_claimed=False)


def encode(value):
    if isinstance(value,F):
        return dict(exact_rational=str(value),display=float(value))
    if isinstance(value,dict):
        return {key:encode(v) for key,v in value.items()}
    if isinstance(value,(list,tuple)):
        return [encode(v) for v in value]
    return value
