#!/usr/bin/env python3
"""Complete finite Cp derivative norms and real-box stability for R31.

This is an arithmetic/finite-Fourier API, not an actual-flow certificate.
It uses center finite cancellation to avoid replacing every spatial
derivative by a Cauchy bound on the entire parameter norm.
"""
from __future__ import annotations

from flint import arb, acb
from fourfold_forward_endpoint_bound_v2 import norm, product, derivative
from fourfold_parameter_endpoint_kam import nonnegative


def sharp_half_spatial_bounds(P1,q,d,cp_error,*,center_u,uniform_u,
                              uniform_T,parameter_radius,outer_width,inner_width):
    """R82 supplies ||Cp(center)-P1*q(x+d)||_outer <= cp_error.

    uniform_T bounds Cpp on the full real parameter interval and outer
    width. Cauchy is applied only to the error and parameter variation.
    All modes of the finite product and its derivative are retained.
    """
    eps,U,T,eta,fee=[nonnegative(v,'uniform or center bound') for v in
                     (center_u,uniform_u,uniform_T,parameter_radius,cp_error)]
    a,b=map(arb,(outer_width,inner_width))
    if not 0<=b<a or not U>=eps:
        raise ValueError('nested widths and a true uniform displacement bound required')
    gap=(a-b).lower()
    shifted=[z*(acb(0,k)*d).exp() for k,z in enumerate(q)]
    L=product(P1,shifted)
    finite_P=norm(L,b)
    finite_Q=norm(derivative(L),b)
    e=arb(1).exp()
    P0=(finite_P+fee).upper()
    Q0=(finite_Q+fee/(e*gap)).upper()
    P=(P0+eta*T).upper()
    Q=(Q0+eta*T/(e*gap)).upper()
    return dict(P=P,Q=Q,T=T,B=(2*U/gap**2).upper(),
        J=(1+U/(e*gap)).upper(),center_J_minus_one=(eps/(e*gap)).upper(),
        center_P=P0,center_Q=Q0,center_u=eps,uniform_u=U,
        complete_finite_P=finite_P,complete_finite_Q=finite_Q,
        center_Cp_approximation_fee=fee,parameter_variation_P_fee=(eta*T).upper(),
        parameter_variation_Q_fee=(eta*T/(e*gap)).upper(),
        finite_Cp_row=L,all_finite_product_and_derivative_modes_retained=True,
        proved_half_derivative_width=b,outer_width=a)


def square_sharp_half_bounds(half,*,full_width,half_twist_lower):
    """Full-return chain rules using the actual sharp half P,Q,T,B."""
    s=arb(full_width)
    sig=nonnegative(half_twist_lower,'center half twist lower bound')
    if not 0<=s or not s+half['uniform_u']<half['proved_half_derivative_width']:
        raise ValueError('full return leaves the proved half derivative domain')
    P,Q,T,B,J=(half[k] for k in ('P','Q','T','B','J'))
    eps=half['center_u']
    twist_fee=(half['center_Q']*eps
               +half['center_J_minus_one']*half['center_P']).upper()
    return dict(P=((1+J)*P).upper(),Q=(2*J*Q+B*J*P).upper(),
        T=((1+J)*T+2*Q*P+B*P*P).upper(),B=(B*(J*J+J)).upper(),
        epsilon=(2*eps).upper(),twist_lower=(2*sig-twist_fee).lower(),
        complete_square_twist_fee=twist_fee,
        actual_full_domain_width=s,
        complete_chain_rule_terms_retained=True)
