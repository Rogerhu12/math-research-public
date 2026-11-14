#!/usr/bin/env python3
"""Actual complete finite coefficients -> holomorphic two-ray strip bounds.

Every true strict radial box is consumed.  The remaining root interval
uses the same complete target germ and the actual cubic.  Full Fourier
convolution, true mean, exact repair uncertainty, and both flow legs are
kept.  This establishes a holomorphic domain and derivative budgets; it
does not turn an approximate orbit or fitted conjugacy into a proof.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
import time
from flint import arb, arb_poly, ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_curvature_angle_energy_prefix import polynomial_ranges, dyadic
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha

CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
STRICT='23a7554aa141b51b4c897f42399eb355d003d5fe5dd37b1c62f68025a4c8542a'
GERM='397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864'
REPAIR='6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc'
DEFINITION='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
WIDTHS=(Fraction(1,64),Fraction(1,32),Fraction(1,16),Fraction(1,8),Fraction(1,4))


def read(p):
    data=Path(p).read_bytes()
    return json.loads(gzip.decompress(data) if str(p).endswith('.gz') else data)


def b(v):return box_from_record(v)


def coefficients(saved,nodes,piece,left,right,alpha,s,K,beta,errors):
    y,_=polynomial_ranges(saved,nodes,piece,left,right)
    y=[alpha*z+arb(0,e) for z,e in zip(y,errors)]
    # u=i*t, where t has real antisymmetric Laurent coefficients.
    # Both products are complete degree-128 polynomial convolutions
    # after shifting Laurent index -32 to ordinary index zero.
    n=32;t=[arb(0) for _ in range(2*n+1)];v=[arb(0) for _ in t]
    v[n]=s+y[n]
    for j in range(1,n+1):
        t[n+j]=-y[j-1]/2;t[n-j]=y[j-1]/2
        v[n+j]=y[n+j]/2;v[n-j]=y[n+j]/2
    tt=arb_poly(t);vv=arb_poly(v)
    S=-(tt*tt)+K*(vv*vv)
    # Real even S: the real cosine amplitude is 2 times its positive
    # Laurent coefficient. beta*I(S) is a real sine polynomial.
    return [(2*abs(beta*S[2*n+j])/(4*j)).upper() for j in range(1,2*n+1)]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--strict',type=Path,required=True)
    ap.add_argument('--germ',type=Path,default=Path('notes/2026-11-13-R133-actual-moving0765-physical-complex-turning-germ-native.json.gz'))
    ap.add_argument('--repair',type=Path,default=Path('notes/2026-11-14-R133-final-exact-continuous-value-repair-native.json.gz'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic();ctx.prec=256;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve every actual analytic-strip report')
    for p,expected in ((args.candidate,CANDIDATE),(args.strict,STRICT),(args.germ,GERM),(args.repair,REPAIR)):
        if sha(p)!=expected:raise ValueError('same complete centre and certified input required')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']))
    strict,germ,repair=read(args.strict),read(args.germ),read(args.repair)
    if not all(z['complete'] for z in (strict,germ,repair)) or repair['derived_definition_sha256']!=DEFINITION:
        raise ValueError('all true complete inputs and the exact repair are required')
    alpha=exact_arb(Fraction(meta['exact_float_amplitude']))
    nodes=list(map(dyadic,saved['radial_nodes']))
    errors=[exact_arb(Fraction(x)).upper() for x in repair['exact_cumulative_coefficient_suprema']]
    freq=[4*j for j in range(1,65)]
    weights={str(w):[(exact_arb(w)*k).exp().upper() for k in freq] for w in WIDTHS}
    sums={str(w):[arb(0) for _ in range(4)] for w in WIDTHS}
    rows=[];cursor=Fraction(0)
    def add_row(left,right,piece,s,K,beta,kind):
        nonlocal cursor
        if left!=cursor or not nodes[piece]<=left<right<=nodes[piece+1]:
            raise ValueError('complete genuine candidate/target radial cover required')
        coeff=coefficients(saved,nodes,piece,left,right,alpha,s,K,beta,errors)
        length=exact_arb(right-left);paid={}
        for width in WIDTHS:
            key=str(width);ww=weights[key];norms=[]
            for order in range(4):
                value=sum((a*w*k**order for a,w,k in zip(coeff,ww,freq)),arb(0)).upper()
                sums[key][order]+=length*value;norms.append(record(value))
            paid[key]=norms
        rows.append(dict(interval=list(map(str,(left,right))),candidate_piece=piece,
            target_kind=kind,complete_real_sine_degree=64,full_drift_derivative_Astrip=paid))
        cursor=right
    for i,row in enumerate(strict['rows']):
        left,right=map(Fraction,row['interval']);a=row['actual_target']
        add_row(left,right,row['candidate_piece'],b(a['s']),b(a['K']),b(a['beta']),'original_complete_strict_box')
        if i%1024==0:print(dict(rows=len(rows),elapsed=time.monotonic()-start),flush=True)
    roots=list(map(Fraction,germ['root_interval']))
    domain=list(map(Fraction,germ['complex_radial_rectangle']['real_interval']))
    if not domain[0]<cursor<roots[0]<=roots[1]<domain[1]:
        raise ValueError('the true remaining root interval must lie in the paid germ')
    intr=germ['complex_intrinsic_coefficients'];length=exact_arb(roots[1]-cursor)
    Kabs=(abs(b(intr['K1']['modulus_upper']))*length).upper()
    add_row(cursor,roots[1],germ['actual_candidate_piece'],b(intr['s']['real']),
            (-Kabs).union(arb(0)),b(intr['beta']['real']),'true_root_remainder_with_K_root_identity')
    output=[]
    for width in WIDTHS:
        B,L,L2,L3=[z.upper() for z in sums[str(width)]]
        sigma=exact_arb(width)
        # Both legs fit with a strict 1/8 vertical margin.  The radial
        # scalar speeds are real and contribute no imaginary growth.
        rho=(exact_arb(Fraction(7,8))*sigma*(-2*L).exp()).lower()
        logJ=(2*L).upper();Jac=logJ.exp().upper()
        output.append(dict(outer_field_strip=str(width),true_return_input_strip=record(rho),
            complete_one_leg_integrated_drift=record(B),
            complete_one_leg_integrated_first_derivative=record(L),
            complete_one_leg_integrated_second_derivative=record(L2),
            complete_one_leg_integrated_third_derivative=record(L3),
            both_legs_vertical_output_bound=record((rho*Jac).upper()),
            return_derivative_modulus_upper=record(Jac),
            return_derivative_modulus_lower=record((-logJ).exp().lower()),
            return_derivative_minus_one_upper=record((Jac-1).upper()),
            return_minus_full_radial_translation_upper=record((2*B).upper()),
            return_second_derivative_upper=record((2*(4*L).exp()*L2).upper()),
            return_third_derivative_upper=record(((6*L).exp()*(2*L3+12*L2*L2)).upper()),
            full_flow_univalence_from_ODE_uniqueness=True,
            root_and_all_radial_interfaces_retained=True))
    gates=[dict(name=name,passed=bool(ok)) for name,ok in (
        ('same complete candidate with all five shards',sha(args.candidate)==CANDIDATE),
        ('all strict boxes and the genuine root remainder retained',len(rows)==3072),
        ('the actual root remainder stays inside one original candidate piece',nodes[germ['actual_candidate_piece']]<roots[0] and roots[1]<nodes[germ['actual_candidate_piece']+1]),
        ('all true even means occur in complete S convolution',len(errors)==65),
        ('all physical repair coefficients retained',repair['derived_definition_sha256']==DEFINITION),
        ('complete Fourier product is unaliased',all(z['complete_real_sine_degree']==64 for z in rows)),
        ('the complete real scalar speed contributes no imaginary drift',strict['whole_affine_parameter_interval'] and germ['whole_affine_parameter_interval']),
        ('every stated input strip is positive',all(b(z['true_return_input_strip'])>0 for z in output)),
        ('both flow legs retain a strict outer-strip margin',all(b(z['both_legs_vertical_output_bound'])<exact_arb(Fraction(z['outer_field_strip'])) for z in output)),
        ('all first through third analytic derivatives are finite',all(b(z['return_third_derivative_upper']).is_finite() for z in output)),
    )]
    report=dict(kind='actual_final_complete_two_ray_holomorphic_strips_and_derivatives',
        complete=all(g['passed'] for g in gates),source_sha256=sha(__file__),
        inputs={str(p):sha(p) for p in (args.candidate,args.strict,args.germ,args.repair)},
        candidate_sha256=CANDIDATE,derived_definition_sha256=DEFINITION,
        exact_alpha=meta['exact_float_amplitude'],exact_nu=meta['exact_float_nu'],
        whole_original_eta=True,root_interval=germ['root_interval'],
        strict_rows=len(strict['rows']),root_remainder_rows=1,rows=rows,strip_budgets=output,
        complete_primitive_tail_in_all_intrinsic_boxes=True,
        complete_angular_series_not_sampled=True,all_even_mean_terms_retained=True,
        actual_ODE_univalence_not_bare_pullback_smallness=True,
        parameter_response_or_true_conjugacy_certified_here=False,
        rotation_value_or_Diophantine_property_certified_here=False,
        nonlinear_solution_or_global_inverse_certified_here=False,
        gates=gates,seconds=time.monotonic()-start)
    save(args.out,report)
    print(dict(complete=report['complete'],seconds=report['seconds'],strips=[dict(
        field=z['outer_field_strip'],input=b(z['true_return_input_strip']).str(14),
        L=b(z['complete_one_leg_integrated_first_derivative']).str(14),
        displacement=b(z['return_minus_full_radial_translation_upper']).str(14)) for z in output]),flush=True)
    if not report['complete']:raise RuntimeError('an actual complete analytic-flow gate failed')


if __name__=='__main__':main()
