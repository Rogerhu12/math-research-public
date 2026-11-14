#!/usr/bin/env python3
"""Actual nonzero-frontload first-piece polynomial and Gauss64 comparison.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The input is explicitly a completed UNSOLVED warm screen, not an accepted
solution. Its frozen degree22 stored Bernstein velocity is treated as an
exact polynomial. Complete complex ellipse boxes certify a square-root
branch, then exact Chebyshev tails and the previously certified actual binary
Gauss64 table pay the ideal partial height primitive through derivative two.
Internal floating evaluation, affine physical alignment, the remaining
segments, complete surface mean and actual PDE geometry remain separate.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb, isqrt
from pathlib import Path
import resource
import struct
import time
from flint import arb, acb, ctx

HERE = Path(__file__).resolve().parent
PINS = {
    'strong_monotone_initial_speed.py':
        '12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7',
    'strong_monotone_initial_speed_anchor.py':
        '583af82cdd6bb672325844587d8aac67e47365ccb5152ac2eae543837adc0ffc',
    'alternative-neck-provider.py':
        '84ed048425c8b0f4deeec8af37828e318150cde5d59995da77f64d923591b9c2',
    'strong_newg_gauss64_table_bridge.py':
        'd83ef3e22b238244ef28f653d8b66b35d5cc5bb1794498a3a184177ef3dfaec0',
}
TABLE_SHA = '0a6bb86d0b492ba47ff5d34a4ef63419686aef316cacdec62ed1781f48da621d'


def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p): return json.loads(Path(p).read_text())
def binary(x): return F.from_float(float(x))
def rat(x): return dict(numerator=str(x.numerator), denominator=str(x.denominator))
def dy(x): return F(int(x[0]))*F(2)**int(x[1])
def aq(x):
    x = F(x)
    return arb(x.numerator)/x.denominator
def upper(x):
    m, e = arb(x).upper().man_exp()
    return [str(m), int(e)]
def differences(values): return [b-a for a, b in zip(values, values[1:])]
def bits(x): return struct.pack('<d', float(x))


def tail_moment(order, first, r):
    moments = [1/(1-r), r/(1-r)**2, r*(1+r)/(1-r)**3,
        r*(1+4*r+r*r)/(1-r)**4,
        r*(1+11*r+11*r*r+r**3)/(1-r)**5]
    return r**first*sum((comb(order,j)*F(first)**(order-j)*moments[j]
                        for j in range(order+1)), F(0))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('warm-screen','warm-resource','table','out'):
        ap.add_argument('--'+name, type=Path, required=True)
    ap.add_argument('--ellipse-rho', default='3/2')
    ap.add_argument('--panels', type=int, default=1024)
    a = ap.parse_args()
    start = time.monotonic(); ctx.prec = 256; ctx.threads = 1
    if a.out.exists(): raise FileExistsError('A fresh certificate is required')
    rho = F(a.ellipse_rho)
    if not 1 < rho <= 2 or a.panels < 128:
        raise ValueError('Explicit ellipse and complete boundary cover required')
    checks = {}
    def check(name, condition):
        if not condition: raise ArithmeticError(name)
        checks[name] = checks.get(name,0)+1
    for name, wanted in PINS.items():
        check('frozen_source_'+name, sha(HERE/name) == wanted)
    screen, owned, table = read(a.warm_screen), read(a.warm_resource), read(a.table)
    check('actual_completed_unsolved_warm', screen['finished'] and screen['finite_domain_passed']
        and not screen['nonlinear_solution'] and not screen['true_new_H_tail_evaluated']
        and screen['worker_start_attempts'] == 0 and owned['exitcode'] == 0
        and owned['wait4_observed'] and owned['termination_signal'] is None)
    check('owned_same_warm_output', owned['command'][owned['command'].index('--inspect-warm-output')+1] == str(a.warm_screen))
    profile = screen['warm_profile']
    weight = binary(profile.get('initial_speed_frontload',0))
    degree = int(profile.get('initial_speed_frontload_degree',22))
    check('actual_nonzero_frontload_only', 0 < weight <= 1 and degree == 22
        and float(profile.get('initial_speed_pulse',0)) == 0
        and profile['ramp_law'] == 'hermite_boost_neck' and profile['boost_law'] == 'angle')
    from strong_monotone_initial_speed_anchor import physical_piece
    data = physical_piece(1., profile['delta'], profile['vu'], profile['start_acceleration'],
                          float(weight), degree)
    proof_path = Path(screen['geometry_fields']['actual_exact_chart_order_bridge']['path'])
    proof = read(proof_path)
    check('actual_first_piece_length_bits', bits(data['length']) == bits(proof['actual_physical_breaks'][1])
        and proof['physical_profile'] == profile and proof['actual_physical_breaks'][0] == 0)
    S, V, k0, delta = map(binary, (data['length'],profile['vu'],profile['start_acceleration'],profile['delta']))
    C = list(map(binary,data['strong_initial_speed_frontload_velocity_controls']))
    R = list(map(binary,data['strong_initial_speed_frontload_radius_controls']))
    Astore = list(map(binary,data['strong_initial_speed_frontload_acceleration_controls']))
    check('complete_actual_degree22_controls', len(C)==degree+1 and len(R)==degree+2 and len(Astore)==degree)
    check('stored_real_speed_hull', C[0]==0 and C[-1]==C[-2]==V and 0<V<1
        and S>0 and min(C)>=0 and max(C)<=V and min(differences(C))>=0)
    # Exact coherent radius integrates the actual stored velocity. Its
    # comparison with independently rounded stored r and acceleration is paid.
    Rcoh = [F(1)+S*sum(C[:j],F(0))/(degree+1) for j in range(degree+2)]
    deltaR = [r-c for r,c in zip(R,Rcoh)]
    radius_costs=[]; dr=deltaR; multiplier=F(1)
    for order in range(3):
        radius_costs.append(multiplier*max(map(abs,dr)))
        if order<2: multiplier*=F(degree+1-order)/S; dr=differences(dr)
    exact_accel = [degree*x/S for x in differences(C)]
    accel_cost = max(abs(x-y) for x,y in zip(Astore,exact_accel))
    # The ideal velocity coefficients at this exact binary length are affine
    # in length. The exact ideal-root displacement is paid independently.
    b=k0*S; cubic=(F(0),b/3,V,V)
    elevated=[sum((cubic[k]*comb(3,k)*comb(degree-3,j-k)/comb(degree,j)
        for k in range(max(0,j-(degree-3)),min(3,j)+1)),F(0)) for j in range(degree+1)]
    endpoint=[F(0),b/degree]+[V]*(degree-1)
    ideal_at_S=[(1-weight)*x+weight*y for x,y in zip(elevated,endpoint)]
    coeff_errors=[x-y for x,y in zip(C,ideal_at_S)]
    emax=max(map(abs,coeff_errors))
    aa=(1-weight)/2+weight*F(degree-1,degree+1)
    bb=(1-weight)/12+weight*F(1,degree*(degree+1))
    check('unique_ideal_positive_length_root', aa>0 and bb>=0 and delta>0 and k0>0)
    residual=aa*V*S+bb*k0*S*S-delta
    length_cost=abs(residual)/(aa*V)
    check('ideal_length_positive_bracket', S-length_cost>0)
    # The maximum coefficient sensitivity of the degree-elevated cubic and
    # endpoint control list is at most k0/3 for degree>=3.
    ideal_coeff_cost=emax+k0*length_cost/3
    check('exact_ideal_length_residual_identity', residual==aa*V*S+bb*k0*S*S-delta)
    # Exact real derivative caps and a positive rational sqrt denominator.
    derivative_caps=[]; ds=C; factor=F(1)
    for order in range(4):
        derivative_caps.append(factor*max(map(abs,ds)))
        if order<3: factor*=degree-order; ds=differences(ds)
    radicand=1-V*V; scale=1<<128
    root_lower=F(isqrt((radicand.numerator*scale*scale)//radicand.denominator),scale)
    check('strict_real_square_root_domain', root_lower>0 and root_lower*root_lower<=radicand)
    d1,d2,d3=derivative_caps[1:]
    fcap=[F(1),V*d1/root_lower,
        d1*d1/root_lower**3+V*d2/root_lower,
        3*V*d1**3/root_lower**5+3*d1*d2/root_lower**3+V*d3/root_lower]
    semi_a=(rho+1/rho)/4; semi_b=(rho-1/rho)/4
    coefficient_complex_cost=emax*(2*semi_a)**degree
    rows=[]; largest=F(0)
    for j in range(a.panels):
        theta=arb.pi()*(aq(F(2*j+1,a.panels))+arb(0,aq(F(1,a.panels))))
        u=acb(aq(F(1,2))+aq(semi_a)*theta.cos(), aq(semi_b)*theta.sin())
        v3=aq(V)*u*u*(3-2*u)+aq(b)*u*(1-u)**2
        vD=aq(V)-(1-u)**(degree-1)*(aq(V)+aq((degree-1)*V-b)*u)
        structured=(1-aq(weight))*v3+aq(weight)*vD
        cap=upper(abs(structured)+aq(coefficient_complex_cost)); capq=dy(cap)
        largest=max(largest,capq)
        rows.append(dict(panel=j,theta_over_pi=[str(F(2*j,a.panels)),str(F(2*j+2,a.panels))],
                         complete_velocity_modulus_upper=cap,strictly_below_one=capq<1))
    ellipse_pass=all(row['strictly_below_one'] for row in rows)
    check('actual_binary_Gauss64_certificate', sha(a.table)==TABLE_SHA
        and table['all_gates'] and len(table['gates'])==399 and all(table['gates'].values())
        and len(table['root_weight_rows'])==64
        and table['source_sha256']==PINS['strong_newg_gauss64_table_bridge.py'])
    result=dict(schema='actual-frontload-first-piece-stored-polynomial-ellipse-Gauss64-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',scope=__doc__,source_sha256=sha(__file__),
        input_sha256={str(p):sha(p) for p in (a.warm_screen,a.warm_resource,a.table,proof_path)},
        frozen_sources=PINS,input_kind='completed-unsolved-warm',actual_profile=profile,
        exact_provider_first_piece_data=data,degree=degree,
        exact_binary_length=rat(S),ideal_length_equation_residual=rat(residual),
        ideal_length_root_displacement_upper=rat(length_cost),
        ideal_velocity_coefficient_error_at_same_normalized_u_upper=rat(ideal_coeff_cost),
        coherent_radius_control_exact=list(map(rat,Rcoh)),
        stored_radius_to_coherent_radius_C0_C1_C2=list(map(rat,radius_costs)),
        stored_acceleration_to_exact_velocity_derivative_upper=rat(accel_cost),
        coherent_radius_right_endpoint_increment_error=rat(abs(Rcoh[-1]-1-delta)),
        normalized_velocity_derivative_caps_0_1_2_3=list(map(rat,derivative_caps)),
        normalized_height_integrand_real_derivative_caps_0_1_2_3=list(map(rat,fcap)),
        real_sqrt_denominator_lower=rat(root_lower),ellipse_rho=rat(rho),
        ellipse_semiaxes=list(map(rat,(semi_a,semi_b))),ellipse_boundary_rows=rows,
        boundary_modulus_upper=rat(largest),coefficient_complex_error_upper=rat(coefficient_complex_cost),
        all_ellipse_domain_boxes_passed=ellipse_pass,
        complete_continuous_boundary_not_samples=True,
        complete_candidate_or_accepted_solution_certified=False,
        internal_numpy_math_evaluation_or_affine_alignment_paid=False,
        complete_surface_mean_or_Cartesian_PDE_reach_certified=False,
        new_ODE_Node_Newton_or_geometry_samples=0)
    if ellipse_pass:
        check('whole_ellipse_nonzero_principal_sqrt', largest<1)
        M=F(2); r=1/rho; K=128
        s0,s2,s4=[tail_moment(j,K,r) for j in (0,2,4)]
        tails=[2*M*s0,4*M*s2,F(8,3)*M*(s4-s2)]
        ideal=[2*tails[0],2*tails[0]+tails[1],3*tails[1]+tails[2]]
        eps=table['certified_error_bounds'];Ew=dy(eps['normalized_total_weight_error']);Eu=dy(eps['maximum_normalized_node_error'])
        m0,m1,m2,m3=fcap
        table_cost=[Ew*m0+Eu*m1,Ew*(m0+m1)+Eu*(2*m1+m2),Ew*(2*m1+m2)+Eu*(2*m1+4*m2+m3)]
        total=[x+y for x,y in zip(ideal,table_cost)]
        physical=[S*total[0],total[1],total[2]/S]
        check('all_exact_primitive_error_costs_nonnegative', min(tails+ideal+table_cost+physical)>=0)
        result.update(square_root_holomorphic_on_complete_ellipse=True,
            principal_branch_agrees_with_positive_real_sqrt=True,analytic_modulus_upper=rat(M),
            global_Chebyshev_polynomial_degree=127,first_omitted_degree=K,
            shifted_Chebyshev_tail_C0_C1_C2=list(map(rat,tails)),
            ideal_Gauss_partial_primitive_C0_C1_C2=list(map(rat,ideal)),
            binary_Gauss_table_partial_primitive_C0_C1_C2=list(map(rat,table_cost)),
            physical_first_piece_partial_height_C0_C1_C2=list(map(rat,physical)),
            comparison_anchor='Both partial height primitives equal zero at the same actual first-piece left endpoint.',
            partial_primitive_derivatives_are_continuous_interval_bounds=True,
            ideal_root_to_actual_physical_coordinate_alignment_still_separate=True)
    result.update(all_gates=ellipse_pass,gate_count=sum(checks.values())+len(rows),
        gates={key:True for key in checks},gate_multiplicities=checks,
        elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(out=str(a.out),sha256=sha(a.out),all_gates=ellipse_pass,
        panels=len(rows),maximum_velocity_modulus=float(largest),
        physical_height_errors=([float(x) for x in physical] if ellipse_pass else None),
        peak_rss_kib=result['peak_rss_kib'])),flush=True)
    if not ellipse_pass:raise SystemExit(1)


if __name__=='__main__': main()
