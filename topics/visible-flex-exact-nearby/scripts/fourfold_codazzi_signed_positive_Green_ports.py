#!/usr/bin/env python3
"""Directed positive comparison ports with signed rates and complete sources.

Every returned quantity is an upper coefficient for an inequality.  The
independently rounded ports are not labelled one exact global Riccati
solution.  A full-suffix no-pole gate and the local positive Green theorem
justify each port before it is used.  No actual candidate calculation is
performed by importing this module.
"""
from __future__ import annotations
from fractions import Fraction
from flint import arb,arb_mat


class NeedsRefinement(ValueError):
    """The sufficient whole-suffix no-pole gate needs a smaller true cell."""


def exact(value):
    value=Fraction(value);return arb(value.numerator)/value.denominator


def nonnegative_upper(value):
    # Positivity must already have been proved analytically for this
    # expression; clamping its enclosure is not a proof of positivity.
    value=arb(value)
    if not value.is_finite():raise ValueError('a positive comparison coefficient is not finite')
    return max(arb(0),value.upper()).upper()


def interval(record):return arb(record['lower']).lower().union(arb(record['upper']).upper())


def record(value):
    value=arb(value)
    if not value.is_finite():raise ValueError('a signed Green coefficient is nonfinite')
    return dict(ball=value.str(80),lower=value.lower().str(80),upper=value.upper().str(80))


def scalar_evolution(rate,length):
    """Positive exp(h rate) and integral exp(t rate), without a zero divide."""
    h=exact(length);rate=arb(rate)
    if not h>=0:raise ValueError('a forward scalar length must be nonnegative')
    matrix=arb_mat([[rate,1],[0,0]])*h
    result=matrix.exp()
    return result[0,0].upper(),nonnegative_upper(result[0,1])


def continuous_port(mu,nu,c,e,length,rho_right):
    """A rigorous two-ended port for one constant comparison system.

    p'<=mu p+c q+f, -q'<=nu q+e p+g, qR<=rhoR pR+zR.
    f,g are nonnegative constant upper bounds on this true interval.
    The output gives qL<=rhoL pL+Z(zR,f,g) and pR<=P(pL,zR,f,g).
    """
    h=exact(length);mu,nu,c,e,r=(arb(x) for x in (mu,nu,c,e,rho_right))
    if not h>0 or not all(x>=0 for x in (c,e,r)):
        raise ValueError('a positive cell and nonnegative coupling/terminal slope are required')
    # For every suffix 0<=tau<=h, ||exp(tau A)-I||_infinity<=exp(h M)-1.
    # Hence T22(tau)-rhoR*T12(tau)>0 on the entire suffix domain.
    M=max((abs(mu).upper()+c).upper(),(e+abs(nu).upper()).upper()).upper()
    margin=(1-(h*M).expm1()*(1+r)).lower()
    if not margin>0:raise NeedsRefinement('the full-suffix no-pole sufficient margin is not positive')
    augmented=arb_mat([[mu,c,1,0],[-e,-nu,0,1],[0,0,0,0],[0,0,0,0]])
    transfer=(augmented*h).exp()
    T=[[transfer[i,j] for j in range(2)] for i in range(2)]
    K=[[transfer[i,j+2] for j in range(2)] for i in range(2)]
    d=T[1][1]-r*T[0][1]
    if not d>0:raise ArithmeticError('the directed endpoint denominator contradicts the whole-suffix gate')
    # Backward Riccati positivity follows from e>=0 and its invariant
    # nonnegative half-line, now that the full denominator cannot vanish.
    # The local positive Green theorem then proves all six source and
    # propagation coefficients below nonnegative.
    rho_left=nonnegative_upper((r*T[0][0]-T[1][0])/d)
    out=dict(
        length=str(Fraction(length)),mu=mu.upper(),nu=nu.upper(),c=c.upper(),e=e.upper(),
        rho_right=r.upper(),rho_left=rho_left,
        rho_whole_upper=max(r.upper(),rho_left).upper(),
        no_pole_entire_suffix_margin=margin,
        exact_comparison_endpoint_denominator_lower=d.lower(),
        z_from_z=nonnegative_upper(1/d),
        z_from_f=nonnegative_upper((r*K[0][0]-K[1][0])/d),
        z_from_g=nonnegative_upper((K[1][1]-r*K[0][1])/d),
        p_from_p=nonnegative_upper(((mu-nu)*h).exp()/d),
        p_from_z=nonnegative_upper(T[0][1]/d),
        p_from_f=nonnegative_upper((T[1][1]*K[0][0]-T[0][1]*K[1][0])/d),
        p_from_g=nonnegative_upper((T[0][1]*K[1][1]-T[1][1]*K[0][1])/d),
        transfer_matrix=T,integrated_transfer_matrix=K,
        full_suffix_no_pole_proved=True,exact_local_positive_Green_proved=True,
        signed_rates_not_replaced_by_absolute_values=True)
    return out


def interface_port(projector_distance,rho_right):
    """True sec/tan mixed port, retaining independent a and b sources."""
    delta,r=(arb(x) for x in (projector_distance,rho_right))
    if not 0<=delta<1 or not r>=0:raise ValueError('a true subunit projector gap and nonnegative slope are required')
    denominator=(1-delta*delta).sqrt()
    sec=nonnegative_upper(1/denominator);tan=nonnegative_upper(delta/denominator)
    d=1-tan*r
    if not d>0:raise ValueError('the actual projector jump has no positive mixed-port denominator')
    # sec and tan have been rounded independently upwards, so retain the
    # general A/D/B/C formula instead of assuming sec^2=1+tan^2 exactly.
    return dict(projector_distance_upper=delta.upper(),rho_right=r.upper(),
        rho_left=nonnegative_upper(tan+sec*sec*r/d),
        secant_upper=sec,tangent_upper=tan,positive_jump_denominator_lower=d.lower(),
        z_from_z=nonnegative_upper(sec/d),z_from_a=nonnegative_upper(sec*r/d),z_from_b=arb(1),
        p_from_p=nonnegative_upper(sec/d),p_from_z=nonnegative_upper(tan/d),
        p_from_a=nonnegative_upper(1/d),
        full_source_jump_a_and_b_retained=True)


def apply_backward(port,z_right,f,g):
    return nonnegative_upper(port['z_from_z']*z_right+port['z_from_f']*f+port['z_from_g']*g)


def apply_forward(port,p_left,z_right,f,g):
    return nonnegative_upper(port['p_from_p']*p_left+port['p_from_z']*z_right
        +port['p_from_f']*f+port['p_from_g']*g)


def apply_jump_backward(port,z_right,a,b):
    return nonnegative_upper(port['z_from_z']*z_right+port['z_from_a']*a+port['z_from_b']*b)


def apply_jump_forward(port,p_left,z_right,a):
    return nonnegative_upper(port['p_from_p']*p_left+port['p_from_z']*z_right+port['p_from_a']*a)


def whole_segment(port,p_left,z_right,f,g):
    """Complete pointwise p/q upper bounds on the same true constant cell."""
    h=Fraction(port['length']);rho=port['rho_whole_upper'];c=port['c']
    # An autonomous scalar Riccati trajectory with no pole is monotone
    # between its endpoints (or constant), so rho_whole_upper is valid.
    ez,iz=scalar_evolution((port['nu']+c*rho).upper(),h)
    z=max(arb(z_right).upper(),(ez*z_right+iz*(g+rho*f)).upper()).upper()
    ep,ip=scalar_evolution((port['mu']+c*rho).upper(),h)
    p=max(arb(p_left).upper(),(ep*p_left+ip*(c*z+f)).upper()).upper()
    q=(rho*p+z).upper()
    return dict(p=p,q=q,z=z,rho=rho,
        full_orthogonal_pair_square=(p*p+q*q).upper())


def serialize_port(port):
    out={}
    for key,value in port.items():
        if isinstance(value,arb):out[key]=record(value)
        elif key in ('transfer_matrix','integrated_transfer_matrix'):
            out[key]=[[record(x) for x in row] for row in value]
        else:out[key]=value
    return out
