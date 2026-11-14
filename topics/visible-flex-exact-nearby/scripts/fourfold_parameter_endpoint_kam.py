#!/usr/bin/env python3
"""Actual finite H data and the R82 -> R63 -> R31 arithmetic interface.

The CLI without true parameter-flow inputs proves ONLY finite H/reciprocal
facts. The imported endpoint and KAM functions require independently proved
whole-flow and whole-parameter-box bounds. No finite-only run accepts KAM.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path
from flint import arb, acb, ctx

from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_saved_circle_field_multidomain_budget import read, upper
from fourfold_forward_endpoint_bound_v2 import norm, add, derivative, product, midpoint
from fourfold_forward_density_pipeline_Q1024_v3 import save, encode_ball
from fourfold_parameter_ordered_defect import (
    parameter_coordinate_budget, endpoint_parameter_budget,
)


def nonnegative(value, name):
    value=arb(value)
    if not value.is_finite() or not value>=0:
        raise ValueError(name+' must be a finite nonnegative bound')
    return value


def hardy(gap):
    if not gap>0:
        raise ValueError('strict Hardy width loss required')
    return (1+4/((2*gap).exp()-1)).sqrt().upper()


def load_H(path):
    doc=read(path)
    if (doc['kind']!='exact_dyadic_trigonometric_polynomials_H_and_q'
        or doc.get('source_metadata',{}).get('target')!='D5'):
        raise ValueError('the exact D5 H and reciprocal polynomial are required')
    den=2**int(doc['denominator_power_of_two'])
    def coefficients(name):
        values=[acb(arb(int(a))/den,arb(int(b))/den) for a,b in doc[name]]
        if not values or values[0].imag!=0:
            raise ValueError('finite real Fourier data required')
        return values
    return doc,coefficients('h_nonnegative_integer_coefficients'),coefficients('q_nonnegative_integer_coefficients')


def finite_H_constants(h,q,width,radius):
    """Same exact polynomial q, with a complete Neumann reciprocal error."""
    s,r=map(arb,(width,radius))
    if not s>=0 or not r>0:
        raise ValueError('invalid finite inverse widths')
    hp=add((1,[acb(1)]),(1,derivative(h)))
    residual=add((1,product(hp,q)),(-1,[acb(1)]))
    eta=norm(residual,s)
    if not eta<1:
        raise ValueError('finite H reciprocal Neumann gate failed')
    real_orientation=(hp[0].real+2*sum((z.real for z in hp[1:]),arb(0))).lower()
    if not real_orientation>0:
        raise ValueError('the real H orientation is unresolved')
    qnorm=norm(q,s)
    inverse=(qnorm/(1-eta)).upper()
    B=norm(h,(s+r).upper(),2)
    kappa=(inverse*B*r).upper()
    if not kappa<=arb(1)/2:
        raise ValueError('finite H local inverse contraction gate failed')
    return dict(reciprocal_residual=eta,finite_q_norm=qnorm,
        inverse_Hprime=inverse,reciprocal_error=(qnorm*eta/(1-eta)).upper(),
        Hsecond=B,kappa=kappa,radius=r,
        perturbed_inverse=(inverse/(1-kappa)).upper(),
        inverse_displacement_factor=(inverse/(1-kappa/2)).upper())


def endpoint_three_orders(U,coordinate_rows,majorants,errors,integration_fees,S,sigma):
    """Keep all finite endpoint product modes, with R82's three real fees.

    coordinate_rows are C_i+D_i, i=0,1,2, enclosed positive Fourier balls.
    majorants=(A,B1,B2), errors=(E0,E1,E2), with their true source premises
    already proved on S. All integration fees are measured on sigma.
    """
    S,sigma=map(arb,(S,sigma))
    if not 0<sigma<S or len(coordinate_rows)!=3:
        raise ValueError('three orders and strict flow widths required')
    budget=parameter_coordinate_budget(*majorants,*errors,S-sigma,integration_fees)
    chosen=[midpoint(row) for row in coordinate_rows]
    choices=[norm([a-b for a,b in zip(row,pick)],sigma)
             for row,pick in zip(coordinate_rows,chosen)]
    b=[(v+c).upper() for v,c in zip(budget['total_coordinate_errors'],choices)]
    D=[norm(row,sigma) for row in chosen]
    A=nonnegative(majorants[0],'A')
    r=(sigma+max(A,D[0])).upper()
    Q0=(arb(1)/4+norm(U,r,1)).upper()
    Q1,Q2=norm(U,r,2),norm(U,r,3)
    Z=min(budget['true_first_parameter_modulus'],(D[1]+b[1]).upper())
    W=min(budget['true_second_parameter_modulus'],(D[2]+b[2]).upper())
    endpoint_fees=endpoint_parameter_budget(b,Q0,Q1,Q2,Z,W,D[1])
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
    return dict(periodic_rows=[P0,P1,P2],sup_errors=[(a+b).upper() for a,b in zip(endpoint_fees,taylor)],
        coordinate_budget=budget,coefficient_selection_fees=choices,
        chosen_coordinate_norms=D,true_Z=Z,true_W=W,
        endpoint_derivative_radius=r,endpoint_Q=[Q0,Q1,Q2],
        exact_full_product_frequencies=True,complete_Taylor_fees=taylor)


def half_return_data(endpoint,h,q,constants,d,width,sigma,uniform_endpoint_norms=None):
    """Center finite signed mean, actual error and optional uniform derivatives.

    uniform_endpoint_norms=(P_Gamma,T_Gamma) must already be Wiener bounds
    on width for the entire same true parameter box. Center norms never
    silently replace them.
    """
    s,outer=map(arb,(width,sigma));H=hardy(outer-s)
    P0,P1,P2=endpoint['periodic_rows']
    shifted_h=[z*(acb(0,k)*d).exp() for k,z in enumerate(h)]
    shifted_q=[z*(acb(0,k)*d).exp() for k,z in enumerate(q)]
    residual=add((1,P0),(-1,shifted_h),(-1,[acb(d)]))
    errors=[(H*v).upper() for v in endpoint['sup_errors']]
    center_E=(norm(residual,s)+errors[0]).upper()
    R=constants['inverse_Hprime'];B=constants['Hsecond'];kappa=constants['kappa']
    if not R*center_E<=constants['radius']/2:
        raise ValueError('center R63 local inverse gate failed')
    u=(constants['inverse_displacement_factor']*center_E).upper()
    parameter_norms=[(norm(row,s)+fee).upper() for row,fee in zip((P1,P2),errors[1:])]
    tau=product(P1,shifted_q)[0].real
    finite_first=norm(P1,s)
    fee=(R*errors[1]+finite_first*constants['reciprocal_error']
         +R*R*B/(1-kappa)*parameter_norms[0]*u).upper()
    sigma0=(tau.abs_lower()-fee).lower()
    result=dict(center_endpoint_error=center_E,center_half_error=u,
        center_endpoint_parameter_norms=parameter_norms,
        center_endpoint_Wiener_error_fees=errors,finite_signed_half_twist=tau,
        complete_half_twist_error=fee,half_twist_lower=sigma0,
        half_twist_separated=bool(sigma0>0),
        signed_mean_roundoff_included_in_ball=True)
    if uniform_endpoint_norms is not None:
        Pg,Tg=[nonnegative(v,'uniform endpoint norm') for v in uniform_endpoint_norms]
        P=(constants['perturbed_inverse']*Pg).upper()
        T=(constants['perturbed_inverse']*(Tg+B*P*P)).upper()
        result['uniform_half_P']=P;result['uniform_half_T']=T
    return result


def half_to_full_bounds(U,P,T,width_loss,center_U,half_twist_lower):
    """C o C at a strictly narrower width; C=x+d+u on the outer strip.

    Returns genuine full-return derivative bounds and a center signed-mean
    loss. The box supremum U pays composition domains; center_U alone pays
    the twist translation error. No equality <(C o C)_p>=2<C_p> is assumed.
    """
    U,P,T,eps,sig=[nonnegative(v,'half-return bound') for v in
                   (U,P,T,center_U,half_twist_lower)]
    gap=arb(width_loss)
    if not gap>U:
        raise ValueError('full-return composition needs a paid width margin')
    d=(gap-U).lower()
    ux=(U/(arb(1).exp()*d)).upper()
    J=(1+ux).upper()
    Q=(P/(arb(1).exp()*d)).upper()
    B=(2*U/d**2).upper()
    Pfull=((1+J)*P).upper()
    Qfull=(2*J*Q+B*J*P).upper()
    Tfull=((1+J)*T+2*Q*P+B*P*P).upper()
    Bfull=(B*(J*J+J)).upper()
    # For the real average use center u_x, not the whole-box U_x.
    center_ux=(eps/(arb(1).exp()*d)).upper()
    twist_fee=(Q*eps+center_ux*P).upper()
    return dict(P=Pfull,Q=Qfull,T=Tfull,B=Bfull,
        epsilon=(2*eps).upper(),twist_lower=(2*sig-twist_fee).lower(),
        true_half_derivative_envelope=J,half_Q=Q,half_B=B,
        complete_square_twist_fee=twist_fee,
        remaining_composition_derivative_width=d)


def r31_gates(*,epsilon,P,Q,T,B,twist_lower,K,s0,delta0,S,parameter_radius,M0=1,R0=1,h0_norm=0):
    """Directed arithmetic for the already-proved actual R31 hypotheses."""
    eps,P,Q,T,B=[nonnegative(v,'R31 nonnegative input') for v in (epsilon,P,Q,T,B)]
    sig,K,s0,delta,S,ra,M0,R0,h0=map(arb,(twist_lower,K,s0,delta0,S,parameter_radius,M0,R0,h0_norm))
    if (not sig>0 or not K>0 or not 0<delta<s0/4 or not delta<=1
        or not S>s0 or not ra>0 or not M0>=1 or not R0>=1 or not h0>=0):
        raise ValueError('invalid R31 domain, twist or initial-conjugacy input')
    M,R=M0+1,2*R0
    La=(2*R/sig).upper();Astar=(R*(1+P*La)).upper();LH=(M*K*Astar).upper()
    C=(K*Astar+B*LH*LH/2+Q*LH*La+T*La*La/2).upper()
    Z=(R0*Q*LH+R0*T*La+P*R0*R0*LH).upper()
    threshold=(delta**2*min(1/(32*C),1/(4*R0*LH),sig/(8*Z))).lower()
    move_p=(2*La*eps).upper();move_H=(2*LH*eps/delta).upper()
    gates=dict(error_smallness=bool(eps<=threshold),parameter_margin=bool(move_p<ra),
               analytic_domain_margin=bool(s0+h0+move_H<S))
    return dict(arithmetic_gates_passed=all(gates.values()),gates=gates,
        epsilon_threshold=threshold,parameter_movement=move_p,
        conjugacy_movement=move_H,conjugacy_derivative_movement=(move_H/delta).upper(),
        final_analytic_width=(s0-4*delta).lower(),
        La=La,Astar=Astar,LH=LH,C=C,Z=Z,
        actual_input_hypotheses_must_be_proved_separately=True)


def records(values):
    return {name:ball_record(value) for name,value in values.items()}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    base=Path('data/phase_ring_continuation')
    p.add_argument('--H',type=Path,default=base/'type_fixed_step02_d5_exact_affine_step5_dyadic_H.json')
    p.add_argument('--widths',default='1/512,5/2048,1/256')
    p.add_argument('--inverse-radius',default='1/1000')
    p.add_argument('--bits',type=int,default=256)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits
    doc,h,q=load_H(args.H)
    rows=[]
    for s in map(Fraction,args.widths.split(',')):
        constants=finite_H_constants(h,q,exact_arb(s),exact_arb(Fraction(args.inverse_radius)))
        rows.append(dict(width=str(s),**records(constants)))
    result=dict(kind='actual_finite_H_and_parameter_endpoint_interface',
        complete_finite_H=True,complete_true_parameter_flow=False,actual_R31_accepted=False,
        source_sha256=sha(__file__),H_path=str(args.H),H_sha256=sha(args.H),bits=args.bits,
        H_degree=doc['H_degree'],q_degree=doc['q_degree'],finite_H_budgets=rows,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_forward_endpoint_bound_v2.py','fourfold_parameter_ordered_defect.py',
            'fourfold_forward_density_pipeline_Q1024_v3.py')},
        scope='All finite H/q modes, exact Neumann reciprocal error, and arithmetic API; true parameter-flow premises are still required.')
    save(args.out,result)
    print({'complete_finite_H':True,'actual_R31_accepted':False,
           'widths':[{'width':r['width'],'reciprocal_error':r['reciprocal_error']['ball']} for r in rows]},flush=True)


if __name__=='__main__':main()
