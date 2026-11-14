#!/usr/bin/env python3
"""Actual two-ray response-error norm and a bounded-quotient quadratic target.

Consumes the same complete strict cover and the true current root germ.
No numerical orbit is used to prove a rotation number.  The quadratic is
an exact possible counterterm target, not the rotation of the actual map.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from functools import reduce
import gzip
import json
from math import gcd
from pathlib import Path
import time
from flint import arb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha

STRICT='23a7554aa141b51b4c897f42399eb355d003d5fe5dd37b1c62f68025a4c8542a'
GERM='397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864'
REPAIR='6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc'
DEFINITION='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
PREFIX=[0,3,1,1,1,3,7,1,3]


def load(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def b(value):return box_from_record(value)
def up(value):return abs(value).upper()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--strict',type=Path,required=True)
    ap.add_argument('--germ',type=Path,default=Path('notes/2026-11-13-R133-actual-moving0765-physical-complex-turning-germ-native.json.gz'))
    ap.add_argument('--repair',type=Path,default=Path('notes/2026-11-14-R133-final-exact-continuous-value-repair-native.json.gz'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic();ctx.prec=320;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve every actual phase budget')
    for path,expected in ((args.strict,STRICT),(args.germ,GERM),(args.repair,REPAIR)):
        if sha(path)!=expected:raise ValueError('a complete actual phase input changed')
    strict,germ,repair=load(args.strict),load(args.germ),load(args.repair)
    if not strict['complete'] or not germ['complete'] or not repair['complete']:
        raise ValueError('all actual covers and the exact repair must be complete')
    if repair['derived_definition_sha256']!=DEFINITION:
        raise ValueError('the new exact continuous centre identity changed')
    left,right=map(Fraction,strict['exact_requested_interval'])
    roots=list(map(Fraction,germ['root_interval']))
    domain=list(map(Fraction,germ['complex_radial_rectangle']['real_interval']))
    if left!=0 or not domain[0]<right<roots[0]<=roots[1]<domain[1]:
        raise ValueError('the complete strict and actual root domains do not overlap correctly')
    eps=exact_arb(Fraction(repair['exact_maximum_piece_pair_Ak']['0'])).upper()
    cI=(arb.pi()/(4*arb(3).sqrt())).upper()
    L=arb(0);square=arb(0);ordinary_square=arb(0);maximum=arb(0);cursor=left
    certificate_rows=[]
    for row in strict['rows']:
        a,c=map(Fraction,row['interval'])
        if a!=cursor or not a<c:raise ValueError('the complete true negative cover has a gap')
        cursor=c;h=exact_arb(c-a)
        target,base=row['actual_target'],row['base']
        beta=up(b(target['beta']));gamma=up(b(target['gamma']));K=up(b(target['K']))
        q=up(b(base['q']));R=up(b(base['actual_R_upper']));V=up(b(base['v_abs_upper']))
        delta_S=(2*(R+K*V)*eps+max(arb(1),K)*eps*eps).upper()
        drift=(up(b(base['actual_d_phi']))+2*beta*delta_S).upper()
        corrected_R=(R+max(arb(1),q)*eps).upper()
        response=(2*beta*cI*corrected_R+gamma).upper()
        L+=h*drift;square+=h*response**2
        ordinary_square+=h*(response*max(arb(1),q))**2
        maximum=max(maximum,response).upper()
        certificate_rows.append(dict(interval=row['interval'],common_row=row['common_row'],
            actual_drift_derivative=record(drift),weighted_response_coefficient=record(response)))
    if cursor!=right:raise ValueError('the strict certificate ends at a different fixed cut')
    intrinsic=germ['complex_intrinsic_coefficients'];h=exact_arb(roots[1]-right)
    beta=up(b(intrinsic['beta']['modulus_upper']));gamma=up(b(intrinsic['gamma']['modulus_upper']))
    K1=up(b(intrinsic['K1']['modulus_upper']));K=(K1*h).upper();q=K.sqrt().upper()
    U=(up(b(germ['moving_U_derivative_Astrip'][0]))+eps).upper()
    V=(up(b(germ['moving_v_derivative_Astrip'][0]))+eps).upper()
    R=(U*U+K*V*V).sqrt().upper()
    drift=(2*beta*(U*U+K*V*V)).upper()
    response=(2*beta*cI*R+gamma).upper()
    L+=h*drift;square+=h*response**2;ordinary_square+=h*(response*max(arb(1),q))**2
    maximum=max(maximum,response).upper();L=L.upper();square=square.upper();ordinary_square=ordinary_square.upper()
    Jplus=L.exp().upper();Jminus=(-L).exp().lower()
    response_L2=(2*(2*L).exp()*square.sqrt()).upper()
    ordinary_L2=(2*(2*L).exp()*ordinary_square.sqrt()).upper()
    response_L1=(2*(2*L).exp()*maximum).upper()
    root_q=q

    # Exact continued fraction [PREFIX; overline(1)].  Its complete
    # quotients are <=7, independently of how close it lies to a proposal.
    pm2,pm1,qm2,qm1=0,1,1,0
    for a in PREFIX:
        p,q=a*pm1+pm2,a*qm1+qm2
        pm2,pm1,qm2,qm1=pm1,p,qm1,q
    p,pp,q,qp=pm1,pm2,qm1,qm2
    phi=(1+arb(5).sqrt())/2;rho=(p*phi+pp)/(q*phi+qp)
    A=qp*qp+qp*q-q*q
    B=-2*pp*qp-pp*q-qp*p+2*q*p
    C=pp*pp+pp*p-p*p
    common=reduce(gcd,(abs(A),abs(B),abs(C)))
    A,B,C=A//common,B//common,C//common
    if A<0:A,B,C=-A,-B,-C
    discriminant=B*B-4*A*C
    diagnostic=exact_arb(Fraction('0.2749224469841854'))
    difference=rho-diagnostic
    gates=[dict(name=n,passed=bool(ok)) for n,ok in (
        ('the actual full strict cover starts at the true waist',left==0),
        ('every complete strict row is retained',len(certificate_rows)==3071),
        ('the remaining true root interval lies in the paid same-centre germ',domain[0]<right and roots[1]<domain[1]),
        ('the exact continuous repair is retained',eps>0 and eps<arb(10)**-16),
        ('the complete ray flow Jacobian remains positive',Jminus>0),
        ('the weighted response functional is finite without q inverse',response_L2.is_finite()),
        ('the ordinary response functional is finite',ordinary_L2.is_finite()),
        ('the continued-fraction matrix is unimodular',abs(p*qp-pp*q)==1),
        ('all finite partial quotients and the periodic tail are bounded by seven',max(PREFIX)==7),
        ('the chosen target is a real irrational quadratic',discriminant==5),
        ('the exact quadratic lies in the unit circle interval',rho>0 and rho<1),
        ('the exact polynomial contains the selected quadratic root',(A*rho*rho+B*rho+C).contains(0)),
    )]
    report=dict(kind='actual_final_full_ray_response_error_and_exact_quadratic_counterterm',
        complete=all(g['passed'] for g in gates),source_sha256=sha(__file__),
        derived_definition_sha256=DEFINITION,original_candidate_sha256=germ['candidate_sha256'],
        object_sha256=germ['object_sha256'],whole_original_eta=True,
        strict_native_sha256=sha(args.strict),germ_native_sha256=sha(args.germ),repair_native_sha256=sha(args.repair),
        complete_strict_rows=len(certificate_rows),fixed_strict_end=str(right),actual_root_interval=germ['root_interval'],
        bounds={k:record(v) for k,v in dict(
            primitive_L2_to_Linfty=cI,complete_drift_derivative_integral=L,
            full_flow_Jacobian_lower=Jminus,full_flow_Jacobian_upper=Jplus,
            complete_weighted_response_coefficient_L2=square.sqrt().upper(),
            full_return_weighted_response_L2_to_Linfty=response_L2,
            full_return_ordinary_response_L2_to_Linfty=ordinary_L2,
            full_return_weighted_response_L1_to_Linfty=response_L1,
            remaining_root_length=h,root_K_abs=K,root_q_upper=root_q,
            root_drift_derivative=drift,root_weighted_response_coefficient=response).items()},
        quadratic_target=dict(continued_fraction_prefix=PREFIX,periodic_tail=[1],
            exact_mobius_coefficients=dict(p=p,p_previous=pp,q=q,q_previous=qp),
            minimal_polynomial=[A,B,C],discriminant=discriminant,
            normalized_target=record(rho),angle_target=record(arb.pi()*rho/2),
            comparison_to_floating_proposal_only=record(difference),
            complete_bad_approximation_constant='1/9',
            full_homogeneous_Fourier_gap_constant='4/9',
            full_fourth_root_of_unity_gap_constant='1/36',
            first_order_phase_beta_not_included=True,
            actual_return_already_has_this_rotation=False),
        same_background_response_error_only=True,complete_true_response_mean_retained=True,
        no_actual_conjugacy_or_rotation_differentiability_assumed=True,
        no_actual_parameter_value_selected=True,no_nonlinear_solution_branch_proved=True,
        no_full_return_inverse_proved=True,no_metric_change_inside_flex_family=True,
        certificate_rows=certificate_rows,gates=gates,seconds=time.monotonic()-start)
    save(args.out,report)
    print(dict(complete=report['complete'],drift_integral=L.str(16),
        weighted_response_error=response_L2.str(16),ordinary_response_error=ordinary_L2.str(16),
        quadratic_polynomial=[A,B,C],quadratic=rho.str(24),
        proposal_difference=difference.str(16),seconds=report['seconds']),flush=True)
    if not report['complete']:raise RuntimeError('an actual phase-response or exact arithmetic gate failed')


if __name__=='__main__':main()
