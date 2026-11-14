#!/usr/bin/env python3
"""R86 spatial budgets -> complete finite endpoint and uniform real-p box.

Inputs are proved full-time integral bounds, not node statistics.  A partial
cover may use this API for a partial-flow calculation, but cannot be labelled
an actual return.  No CLI silently promotes finite data into a KAM proof.
"""
from __future__ import annotations

from flint import arb, acb
from fourfold_forward_endpoint_bound_v3 import norm, add, derivative, product, midpoint
from fourfold_parameter_endpoint_kam import nonnegative, hardy
from fourfold_parameter_ordered_defect import endpoint_parameter_budget
from fourfold_spatial_derivative_defect_budget import certify


def spatial_rows(values):
    if len(values)!=3 or any(len(row)!=3 for row in values):
        raise ValueError('three spatial derivative bounds for each parameter order required')
    return [[nonnegative(v,'integrated spatial bound').upper() for v in row]
            for row in values]


def true_parameter_variations(A,B,C):
    """Ordinary first/second p derivatives on a paid common trajectory tube."""
    A,B,C=spatial_rows([A,B,C])
    growth=A[1].exp().upper()
    Z=(growth*B[0]).upper()
    W=(growth*(C[0]+A[2]*Z*Z+2*B[1]*Z)).upper()
    return dict(true_first_parameter_modulus=Z,true_second_parameter_modulus=W,
                exponential_growth=growth)


def endpoint_three_orders_spatial(U,coordinate_rows,spatial_majorants,spatial_errors,
                                  integration_fees,derivative_strip,sigma):
    """Retain every finite endpoint mode and use the R86 true sup errors.

    coordinate_rows[i]=C_i+D_i are full positive-frequency ball rows.
    spatial_majorants[i][j] bound integral sup of true AND finite sources
    on derivative_strip, j=0,1,2. spatial_errors[i][j], j=0,1, are complete
    integral sup errors on that strip. integration_fees are measured on sigma.
    """
    outer,sigma=map(arb,(derivative_strip,sigma))
    if not 0<sigma<outer or len(coordinate_rows)!=3:
        raise ValueError('three orders and a strict trajectory strip margin required')
    A,B,C=spatial_rows(spatial_majorants)
    budget=certify(A,B,C,spatial_errors,trajectory_strip_gap=outer-sigma,
                   finite_output_fees=integration_fees)
    chosen=[midpoint(row) for row in coordinate_rows]
    choices=[norm([a-b for a,b in zip(row,pick)],sigma)
             for row,pick in zip(coordinate_rows,chosen)]
    errors=[(v+c).upper() for v,c in zip(budget['total_errors'],choices)]
    D=[norm(row,sigma) for row in chosen]
    r=(sigma+max(A[0],D[0])).upper()
    Q0=(arb(1)/4+norm(U,r,1)).upper()
    Q1,Q2=norm(U,r,2),norm(U,r,3)
    variation=true_parameter_variations(A,B,C)
    Z=min(variation['true_first_parameter_modulus'],(D[1]+errors[1]).upper())
    W=min(variation['true_second_parameter_modulus'],(D[2]+errors[2]).upper())
    endpoint_fees=endpoint_parameter_budget(errors,Q0,Q1,Q2,Z,W,D[1])
    w0,w1,w2=chosen
    linear=add((1,[acb(1)]),(4,derivative(U)))
    U2=derivative(U,2)
    P0=add((4,U),(1,product(linear,w0)),(2,product(U2,product(w0,w0))))
    multiplier=add((1,linear),(4,product(U2,w0)))
    P1=product(multiplier,w1)
    P2=add((1,product(multiplier,w2)),(4,product(U2,product(w1,w1))))
    M3=norm(U,(sigma+D[0]).upper(),3)
    taylor=[(arb(2)/3*M3*D[0]**3).upper(),(2*M3*D[0]**2*D[1]).upper(),
            (2*M3*D[0]**2*D[2]+4*M3*D[0]*D[1]**2).upper()]
    return dict(periodic_rows=[P0,P1,P2],
        sup_errors=[(a+b).upper() for a,b in zip(endpoint_fees,taylor)],
        coordinate_budget=budget,coefficient_selection_fees=choices,
        chosen_coordinate_norms=D,true_Z=Z,true_W=W,
        endpoint_derivative_radius=r,endpoint_Q=[Q0,Q1,Q2],
        exact_full_product_frequencies=True,complete_Taylor_fees=taylor,
        coordinate_error_method='R86_actual_integrated_spatial_derivatives',
        supplied_full_time_and_parameter_identity_must_be_verified=True)


def uniform_box_majorants(center_A,uniform_B,uniform_C,parameter_radius,
                           center_errors=None):
    """Pay g0(p)-g0(p0) on a real p interval using its true uniform g1.

    The reference is independent of p.  Uniform B/C must concern the same
    geometric family and tube.  If center g0 is retained as a finite proxy,
    its j=0,1 errors receive eta*B_j too.  Center A is never promoted to a
    uniform bound without this fee.
    """
    A,B,C=spatial_rows([center_A,uniform_B,uniform_C])
    eta=nonnegative(parameter_radius,'parameter radius')
    boxA=[(a+eta*b).upper() for a,b in zip(A,B)]
    result=dict(majorants=[boxA,B,C],base_source_parameter_fees=[(eta*b).upper() for b in B],
                parameter_radius=eta,parameter_independent_reference_required=True)
    if center_errors is not None:
        if len(center_errors)!=2:
            raise ValueError('the base source needs both zeroth and first spatial error bounds')
        result['uniform_base_source_errors']=[
            (nonnegative(e,'center source error')+eta*b).upper()
            for e,b in zip(center_errors,B)]
    return result


def uniform_endpoint_variations(U,center_A,uniform_B,uniform_C,parameter_radius,
                                derivative_strip,sigma,width):
    """A direct full-box derivative bound, without a chosen p-polynomial.

    This branch only needs true derivative moduli.  It is often sufficient
    for uniform T; center signed polynomials still determine the twist and Q.
    """
    outer,sigma,s=map(arb,(derivative_strip,sigma,width))
    if not 0<=s<sigma<outer:
        raise ValueError('strict endpoint Hardy and trajectory margins required')
    box=uniform_box_majorants(center_A,uniform_B,uniform_C,parameter_radius)
    A,B,C=box['majorants']
    if not A[0]<outer-sigma:
        raise ValueError('the full real-p box trajectory leaves its proved tube')
    variations=true_parameter_variations(A,B,C)
    Z,W=variations['true_first_parameter_modulus'],variations['true_second_parameter_modulus']
    r=(sigma+A[0]).upper()
    Q0=(arb(1)/4+norm(U,r,1)).upper();Q1=norm(U,r,2)
    h=hardy(sigma-s)
    Pg=(h*4*Q0*Z).upper()
    Tg=(h*4*(Q1*Z*Z+Q0*W)).upper()
    return dict(**box,**variations,endpoint_radius=r,endpoint_Q=[Q0,Q1],
                uniform_endpoint_P=Pg,uniform_endpoint_T=Tg,
                uniform_trajectory_tube_included=True,Hardy_factor=h)


def uniform_half_return_box(center_endpoint_error,center_half_error,
                            endpoint_P,endpoint_T,parameter_radius,constants,
                            center_half_P_bound=None):
    """Check R63 on the whole real box before using the inverse in P and T."""
    E0,u0,Pg,Tg,eta=[nonnegative(v,'uniform half-return input') for v in
                    (center_endpoint_error,center_half_error,endpoint_P,endpoint_T,parameter_radius)]
    Ebox=(E0+eta*Pg).upper()
    if not constants['inverse_Hprime']*Ebox<=constants['radius']/2:
        raise ValueError('R63 local inverse is not proved on the full parameter box')
    P=(constants['perturbed_inverse']*Pg).upper()
    T=(constants['perturbed_inverse']*(Tg+constants['Hsecond']*P*P)).upper()
    tightening=[]
    if center_half_P_bound is not None:
        P0=nonnegative(center_half_P_bound,'actual center half-return derivative bound')
        # Every step starts from an already valid uniform bound.  There is
        # no circular assumption of a favorable root of a quadratic.
        for iteration in range(8):
            P=min(P,(P0+eta*T).upper())
            T=min(T,(constants['perturbed_inverse']*(Tg+constants['Hsecond']*P*P)).upper())
            tightening.append(dict(iteration=iteration+1,P=P,T=T))
    U=min((constants['inverse_displacement_factor']*Ebox).upper(),(u0+eta*P).upper())
    return dict(uniform_endpoint_error=Ebox,uniform_half_U=U,uniform_half_P=P,
                uniform_half_T=T,full_real_parameter_box_inverse_proved=True,
                true_uniform_parameter_tightening=tightening)


def hybrid_parameter_source_bounds(center_A,center_B,center_E0,center_E1,
                                   uniform_C,uniform_E2,parameter_radius):
    """Use precise center g0/g1 polynomials and a true whole-box g2 polynomial.

    The three finite approximants need not be derivatives of one finite
    family: R86 pays them separately.  The TRUE sources must be g, g_p,
    g_pp of one family.  Real-parameter mean value controls g1 from g2,
    then g0 from g1, without any third p derivative.
    All rows here include spatial derivatives j=0,1,2 as integrated sup.
    """
    rows=[center_A,center_B,center_E0,center_E1,uniform_C,uniform_E2]
    if any(len(row)!=3 for row in rows):
        raise ValueError('each source and error needs three spatial entries')
    a,b,e0,e1,c,e2=[[nonnegative(v,'hybrid source bound').upper() for v in row]
                  for row in rows]
    eta=nonnegative(parameter_radius,'parameter radius')
    fee1=[(eta*v).upper() for v in c]
    B=[(v+fee).upper() for v,fee in zip(b,fee1)]
    fee0=[(eta*v).upper() for v in B]
    A=[(v+fee).upper() for v,fee in zip(a,fee0)]
    E0=[(v+fee).upper() for v,fee in zip(e0,fee0)]
    E1=[(v+fee).upper() for v,fee in zip(e1,fee1)]
    return dict(spatial_majorants=[A,B,c],spatial_errors=[E0,E1,e2],
                uniform_first_source_parameter_fees=fee1,
                uniform_base_source_parameter_fees=fee0,
                parameter_radius=eta,
                finite_source_choice=['center_g0','center_g1','uniform_g2'],
                third_parameter_derivative_not_used=True,
                all_true_sources_must_be_derivatives_of_same_family=True)
