#!/usr/bin/env python3
"""Exact rational n3 local-circle, control, marker and 10% conditional window.

This is a planar-core and conditional full-surface geometry certificate.
It does not produce a nonlinear circular prefix/tail solution.  All input
decimal constants in this file are exact rationals, all trig and integral
bounds use rational Taylor remainders, and pi uses a Machin enclosure.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,math,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'resume_n4'))
from audit_large_radius_core import (point,add,sub,neg,mul,scale,div,
    pi_bounds,sin_bounds,sqrt_bounds,show)

A=F(21,100);B=F(2,25);ORDER=60
CHI={0:1,5:-126,6:420,7:-540,8:315,9:-70}


def moment(m):
    out=A**(m+1)/(m+1)
    for j in range(m+1):
        inner=sum((F(c,j+k+1)for k,c in CHI.items()),F(0))
        out+=B*math.comb(m,j)*A**(m-j)*B**j*inner
    return out


def trig_moment(k,sine=False):
    parity=1 if sine else 0
    polynomial=sum((F((-1)**((m-parity)//2)*k**m,math.factorial(m))*moment(m)
        for m in range(parity,ORDER+1,2)),F(0))
    remainder=(A+B/2)*(k*(A+B))**(ORDER+1)/math.factorial(ORDER+1)
    return polynomial-remainder,polynomial+remainder


def powi(x,k):
    value=point(1)
    for _ in range(k):value=mul(value,x)
    return value


def asin_bounds(x,n=40):
    term=lambda k:F(math.comb(2*k,k),4**k*(2*k+1))*x**(2*k+1)
    lower=sum((term(k)for k in range(n)),F(0))
    # Consecutive positive Taylor terms have ratio < x^2.
    return lower,lower+term(n)/(1-x*x)


def scalar_bounds(x):
    # Compress exact endpoints outward to 40 decimal places; the large
    # intermediate rational denominators are regenerable, not artifacts.
    unit=10**40
    lo=F(x[0].numerator*unit//x[0].denominator,unit)
    hi=F(-((-x[1].numerator*unit)//x[1].denominator),unit)
    assert lo<=x[0]<=x[1]<=hi
    return dict(lower=str(lo),upper=str(hi),display=show((lo,hi)))


def calculate():
    pi=pi_bounds(100);root3=sqrt_bounds(F(3))
    mass=A+B/2;L=scale(pi,F(1,3));T=scale(L,2)
    cm={k:trig_moment(k)for k in [1,2,3,4]}
    sm={k:trig_moment(k,True)for k in [1,2,4]}
    integral=scale(sub(point(mass),cm[3]),8)
    beta=neg(div(integral,sub(L,point(mass))))
    # G0=K0/sin(pi/3), G1=K1/sin(pi/3); no numerical Green integral.
    G0=add(div(cm[1],root3),sm[1])
    G1=sub(scale(G0,8),scale(add(div(add(cm[2],cm[4]),root3),sub(sm[4],sm[2])),4))
    center_per_q=add(sub(sub(point(9),beta),G1),mul(beta,G0))
    assert beta[1]<0 and center_per_q[0]>9
    q=F(17,200);ql=F(849,10000);qh=F(851,10000)
    R=1+8*q;Rlo=1+8*ql;Rhi=1+8*qh
    alpha=F(3523,5000);Ilo=F(3521,10000);Ihi=F(141,400)
    assert Ilo-alpha>-Rlo*A and Ihi<Rlo*A
    rho_nominal=add(point(1-8*q),scale(beta,q))
    rho_range=add(point(1-8*qh),scale(beta,qh))
    nominal_shift=mul(mul(root3,scale(center_per_q,q)),sin_bounds(alpha/(2*R)))
    # c grows with q while alpha/(2R) decreases; this separated endpoint
    # bound is valid for every q in the fixed interval.
    robust_shift=mul(mul(root3,scale(center_per_q,ql)),sin_bounds(alpha/(2*Rhi)))
    assert robust_shift[0]>F(53,200) # .1 * 2.65
    control_rho=F(2,25)
    control_support_constant=sub(div(point(2),root3),point(1))
    # Delta rho_round=q[beta+chi(8-8cos(3x)-beta)].  The second term
    # is nonnegative and its integral is -beta*T.  The positive periodic
    # Green kernel ranges from 1/(2sqrt3) to 1/sqrt3.
    green_min_product=div(L,root3)
    assert green_min_product[0]>F(1,2) and green_min_product[1]<F(2,3)
    round_support=mul(scale(neg(beta),qh),sub(point(1),green_min_product))
    total_support=add(round_support,scale(control_support_constant,control_rho))
    inner=1-qh;outer=1+qh
    support_lower=sub(point(inner),total_support)
    support_upper=add(point(outer),total_support)
    radial_difference=scale(total_support,outer/inner)
    # The pure cosine support curve has exact planar complex third moment
    # -pi*q*(1-12q^2+8q^4).  Use a monotone endpoint lower bound;
    # derivative 1-36q^2+40q^4 is positive on the entire declared interval.
    assert 1-36*qh*qh>0
    pure_moment=scale(pi,ql*(1-12*ql**2+8*ql**4))
    moment_error=scale(mul(mul(pi,powi(support_upper,4)),radial_difference),2)
    core_moment_lower=sub(pure_moment,moment_error)
    assert core_moment_lower[0]>F(1,50) # .02 uniformly, including controls
    controlled_rho=sub(rho_range,point(control_rho))
    assert controlled_rho[0]>F(2,25)
    ell0=F(27,50);ell1=F(5401,10000)
    cylinder_gap=ell1-ell0
    active_moment_lower=scale(core_moment_lower,cylinder_gap/2)
    assert active_moment_lower[0]>F(1,10**6)
    rc=F(1,40);epsilon=F(1)
    marker_value=div(point(8*epsilon*rc**3),scale(root3,81))
    marker_gradient=F(8,9)*epsilon*rc*rc
    marker_curvature=48*epsilon*rc
    marker_moment=scale(pi,epsilon*rc**8/F(140))
    final_diameter=add(point(F(13249,5000)+cylinder_gap),scale(marker_value,2))
    assert final_diameter[1]<F(53,20)
    final_support=F(801,10000)-cylinder_gap/2
    assert final_support>F(2,25) and marker_curvature<F(25,2)
    marker_support=div(point(1-6*epsilon*rc**3),sqrt_bounds(1+marker_gradient**2))
    assert marker_support[0]>1-F(1,1000)
    # The same fixed phase and I work for all q in [ql,qh].
    core_cylinder_diameter=scale(sqrt_bounds(support_upper[1]**2+(ell1/2)**2),2)
    assert core_cylinder_diameter[1]<F(23,10)
    # Initial negative-K window, uniformly for future delta >= .056.
    vu=F(9,20);eps=F(2,5);etar=F(1,20);delta_min=F(7,125);delta_max=F(7,100)
    length=eps*delta_min/(vu*(1-eps))
    accelmax=vu/(length*(1-etar));amax=1+delta_min*eps/(2*(1-eps))
    window=div(asin_bounds(Rlo*vu),scale(sqrt_bounds(amax*accelmax),Rlo))
    assert window[0]>A and Rhi*vu<1
    return dict(scope=__doc__,physical_circle=dict(n=3,eta=0,halfwidth=str(A),transition=str(B),
        q_nominal=str(q),q_interval=[str(ql),str(qh)],radius_nominal=str(R),radius_interval=[str(Rlo),str(Rhi)],
        exact_mean_beta=scalar_bounds(beta),actual_circle_center_norm_per_q=scalar_bounds(center_per_q),
        nominal_center_norm=scalar_bounds(scale(center_per_q,q)),
        nominal_rho_lower=scalar_bounds(rho_nominal),uniform_zero_control_rho_lower=scalar_bounds(rho_range)),
        complete_control_conditions=dict(support_zero_in_protected_neighborhood=True,period='2*pi/3',zero_mean=True,
            rho_control_norm_upper=str(control_rho),support_control_operator_constant=scalar_bounds(control_support_constant),
            total_support_difference_from_cosine_upper=scalar_bounds(total_support),
            controlled_rho_lower=scalar_bounds(controlled_rho),core_support_lower=scalar_bounds(support_lower),
            core_radius_upper=scalar_bounds(support_upper),core_cylinder_diameter_upper=scalar_bounds(core_cylinder_diameter),
            pure_cosine_planar_third_moment_abs_lower=scalar_bounds(pure_moment),
            third_moment_perturbation_upper=scalar_bounds(moment_error),core_third_moment_abs_lower=scalar_bounds(core_moment_lower)),
        regripped_family=dict(fixed_phase_end=str(alpha),fixed_H_material_interval=[str(Ilo),str(Ihi)],
            fixed_H_interval_width=str(Ihi-Ilo),full_q_interval_phase_margin=str(Rlo*A-max(Ihi,alpha-Ilo)),
            cylinder_total_lengths=[str(ell0),str(ell1)],nominal_Hausdorff_lower=scalar_bounds(nominal_shift),
            uniform_Hausdorff_lower=scalar_bounds(robust_shift),uniform_held_ratio=scalar_bounds(scale(robust_shift,F(20,53))),
            H_diameter_ratio_lower=str(F(54,265)),phase_tests_for_noncongruence=[str(alpha/2),str(alpha)]),
        marker_and_active_moment=dict(epsilon=str(epsilon),radius=str(rc),
            maximum_graph_height=scalar_bounds(marker_value),gradient_upper=str(marker_gradient),curvature_upper=str(marker_curvature),
            support_lower_if_cap_height_ge_one=scalar_bounds(marker_support),exact_fixed_cubic_moment=scalar_bounds(marker_moment),
            at_least_one_selected_cylinder_active_moment_abs_lower=scalar_bounds(active_moment_lower)),
        conditional_full_surface=dict(unmarked_diameter_for_ell0_upper=str(F(13249,5000)),
            unmarked_support_for_ell0_lower=str(F(801,10000)),full_actual_curvature_upper=str(F(25,2)),
            plane_cap_height_lower='1',plane_cap_radius_strictly_greater_than=str(rc),
            final_diameter_upper=scalar_bounds(final_diameter),translated_body_support_lower=str(final_support),
            final_support_lower=str(F(2,25)),reach_lower=str(F(2,25)),reach_ratio_lower=str(F(8,265))),
        initial_characteristic_window=dict(vu=str(vu),ramp=str(eps),ramp_eta=str(etar),delta_interval=[str(delta_min),str(delta_max)],
            uniform_R_times_vu_upper=str(Rhi*vu),uniform_loss_div_R_lower=scalar_bounds(window),required_normal_halfwidth=str(A),
            monotonicity_reason='asin(R*vu)/R increases in R; amax*accelmax decreases in delta. This only exhausts the R5 protected window before positive K.'),
        arithmetic=dict(trig_taylor_order=ORDER,machin_terms=100,asin_positive_terms=40,sqrt_decimal_digits=65),
        unproved=['Existence of the corresponding full circular-core prefix and actual nonlinear tail.',
            'One global C2 closed map, complete same-g metric and refinement, and the stated full-surface bounds.',
            'Actual complementary control norm and exact support vanishing must be checked on the accepted lambda=1 state.',
            'Which one of the two cylinder lengths has the certified active moment must be selected from the actual full graph.'])


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();out=calculate()
    sources=[Path(__file__),Path(__file__).resolve().parents[1]/'resume_n4/audit_large_radius_core.py']
    out.update(command=sys.argv,sources_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in sources})
    a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k]for k in ['physical_circle','complete_control_conditions','regripped_family','initial_characteristic_window']},indent=2))


if __name__=='__main__':main()
