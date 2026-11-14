#!/usr/bin/env python3
"""Actual repaired moving96-to-physical128 C-port matrix, with every tail.

The output entries are physical cosine amplitudes, the input is the raw
moving basis (1,cos(4phi),...,cos(384phi)).  The true target/eta interval,
the exact value repair, physical angle variation, and both Fourier signs
are retained.  One-sided formal exponentials have independent complete
Wiener tail bounds.  No quadrature or composition-minus-identity is used.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import gzip,json,math,time
from pathlib import Path
from flint import arb,arb_poly,arb_series,ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_current_positive_complete_coefficients import (
    CURRENT_SHA,OBJECT_SHA,dyadic,exact_polynomial_endpoint,literal_coordinates)
from fourfold_codazzi_final_continuous_value_repair import iter_repair
from fourfold_codazzi_final_head_to_physical_C_tail import REPAIR,DEFINITION
from fourfold_codazzi_rotational_cap_jacobi import RotationalPositiveCap,box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha

TAIL='85fad1a353a11bdacf97fcfad5e87cf85cde3b1fa40ef6ac34e7da29d1c77cc7'


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def exact_endpoint(x):
    a,b=x.man_exp();a,b=int(a),int(b)
    return Fraction(a*2**b) if b>=0 else Fraction(a,2**(-b))


def integer_box(x,scale):
    lo=exact_endpoint(x.lower())*scale;hi=exact_endpoint(x.upper())*scale
    return lo.numerator//lo.denominator,-((-hi.numerator)//hi.denominator)


def exponential(A,goal):
    """A is a real Laurent interval vector on [-32,32], A_0=0.

    For positive/negative one-sided factors, their Fourier tails past n
    are bounded by exp(M_sigma-sigma(n+1)).  Multiplying the two complete
    factors therefore gives the displayed whole A0 remainder.
    """
    modes=(len(A)-1)//2
    if not A[modes].is_zero():raise ValueError('the finite phase must have exact zero mean')
    pos=[arb(0)]+[A[modes+j] for j in range(1,modes+1)]
    neg=[arb(0)]+[A[modes-j] for j in range(1,modes+1)]
    Mp0=sum(map(abs,pos),arb(0)).upper();Mn0=sum(map(abs,neg),arb(0)).upper()
    choices=[]
    for width in (Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1),Fraction(5,4)):
        w=exact_arb(width)
        Mp=sum((abs(z)*(j*w).exp() for j,z in enumerate(pos)),arb(0)).upper()
        Mn=sum((abs(z)*(j*w).exp() for j,z in enumerate(neg)),arb(0)).upper()
        fee=((Mp+Mn0).exp()+(Mn+Mp0).exp()).upper()
        n=max(modes,int(math.ceil(float(((fee.log()-goal.log())/w).upper()))))
        while not fee*(-w*(n+1)).exp()<goal:n+=1
        choices.append((n,width,fee))
    n,width,fee=min(choices,key=lambda z:z[0]);w=exact_arb(width)
    if n>4096:raise ValueError('the explicit entire-exponential degree limit was exceeded')
    previous=ctx.cap;ctx.cap=n+1
    try:
        ep=arb_series(pos,prec=n+1).exp();en=arb_series(neg,prec=n+1).exp()
        polynomial=arb_poly([ep[j] for j in range(n+1)])*arb_poly([en[j] for j in range(n,-1,-1)])
    finally:ctx.cap=previous
    tail=(fee*(-w*(n+1)).exp()).upper()
    return polynomial,-n,tail,dict(one_sided_cutoff=n,weighted_width=str(width),
        complete_exponential_A0_tail=record(tail),positive_A0=record(Mp0),negative_A0=record(Mn0))


def coefficient(poly,lo,k):
    j=k-lo
    return poly[j] if 0<=j<len(poly) else arb(0)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--repair',type=Path,default=Path('notes/2026-11-14-R133-final-exact-continuous-value-repair-native.json.gz'))
    ap.add_argument('--tail',type=Path,default=Path('notes/2026-11-14-R133-repaired-moving-head96-physical-C-tail-v2-native.json.gz'))
    ap.add_argument('--cut',type=Fraction,default=Fraction(9,10))
    ap.add_argument('--half-width',type=Fraction,default=Fraction(1,10**9))
    ap.add_argument('--bits',type=int,default=320)
    ap.add_argument('--interval-bits',type=int,default=256)
    ap.add_argument('--exponential-bits',type=int,default=180)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=args.bits;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve every actual complete matrix report')
    if args.cut!=Fraction(9,10) or args.half_width!=Fraction(1,10**9):
        raise ValueError('this complete matrix is for the declared actual cut and whole eta interval')
    if not 192<=args.interval_bits<=args.bits-32 or args.exponential_bits<160:
        raise ValueError('insufficient explicit output or infinite-tail precision')
    if sha(args.candidate)!=CURRENT_SHA or sha(args.object)!=OBJECT_SHA or sha(args.repair)!=REPAIR or sha(args.tail)!=TAIL:
        raise ValueError('the exact current centre, repair, object and complete tail are required')
    repair,tail=read(args.repair),read(args.tail)
    if not repair['complete'] or not tail['complete'] or repair['derived_definition_sha256']!=DEFINITION:
        raise ValueError('the true repaired background and full output tail must be proved')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']))
    if meta['coordinates']!=literal_coordinates() or meta['object_sha256']!=OBJECT_SHA or int(meta['modes'])!=32:
        raise ValueError('the complete actual moving coordinate identity changed')
    alpha=Fraction(meta['exact_float_amplitude']);nodes=list(map(dyadic,saved['radial_nodes']))
    piece=bisect_right(nodes,args.cut)-1
    vals=exact_polynomial_endpoint(saved,nodes,piece,args.cut)
    offset=None
    for index,e,jump in iter_repair(saved,alpha):
        if index==piece:offset=e;break
    if offset is None:raise ValueError('the exact cumulative repair did not reach the true cut')
    target=RotationalPositiveCap(args.object,args.half_width,512)
    intrinsic,germ,part=target.values(args.cut,args.cut)
    if part!='body':raise ValueError('the intended cut changed scalar branch')
    s=1/intrinsic['Cref'];m=s+exact_arb(alpha*vals[32]+offset[32])
    vcos=[exact_arb(alpha*vals[32+j]+offset[32+j]) for j in range(1,33)]
    if not m<0:raise ValueError('the complete repaired mean must remain negative')
    psi=[z/(4*j*m) for j,z in enumerate(vcos,1)]
    jac_lower=(1-sum((abs(z/m) for z in vcos),arb(0))).lower()
    if not jac_lower>0:raise ValueError('the true physical angular chart must be oriented')
    A=[arb(0) for _ in range(65)]
    for j,z in enumerate(psi,1):A[32+j]=z/2;A[32-j]=-z/2
    Anorm=sum(map(abs,A),arb(0)).upper();goal=arb(2)**(-args.exponential_bits)
    scale=2**args.interval_bits;rows=[];all_float_ok=True
    gram_radius_squared=Fraction(0);gram_float_squared=Fraction(0)
    for ell in range(1,129):
        E,lo,eps,details=exponential([-4*ell*z for z in A],goal)
        Ee=coefficient(E,lo,ell)
        AE=sum((z*coefficient(E,lo,ell-k) for k,z in zip(range(-32,33),A)),arb(0))
        mean=2*(-Ee+4*ell*AE)/(m*m)+arb(0,(2*(1+4*ell*Anorm)*eps/(m*m)).upper())
        values=[mean]
        for j in range(1,97):
            value=-arb(ell)/(j*m*m)*(coefficient(E,lo,ell-j)-coefficient(E,lo,ell+j))
            values.append(value+arb(0,(2*ell*eps/(j*m*m)).upper()))
        intervals=[];midpoints=[];float_hex=[];max_radius=Fraction(0)
        for j,value in enumerate(values):
            lower,upper=integer_box(value,scale);mid=Fraction(lower+upper,2*scale)
            rad=Fraction(upper-lower,2*scale);proposal=float(mid)
            diff=abs(Fraction.from_float(proposal)-mid)
            if not diff<=Fraction(1,2**52):all_float_ok=False
            weight=Fraction(1,2) if j==0 else Fraction(1)
            gram_radius_squared+=weight*rad*rad
            gram_float_squared+=weight*diff*diff
            max_radius=max(max_radius,rad)
            intervals.append([str(lower),str(upper)]);midpoints.append(str(lower+upper));float_hex.append(proposal.hex())
        rows.append(dict(physical_index=ell,physical_frequency=4*ell,
            exact_interval_numerators=intervals,dyadic_midpoint_numerators=midpoints,
            exact_binary64_proposal_hex=float_hex,maximum_entry_radius=record(exact_arb(max_radius)),
            complete_exponential=details))
        if ell%16==0:print(dict(physical_rows=ell,complete_cols=97,seconds=time.monotonic()-started),flush=True)
    meanrow=-1/(m*m);L,U=integer_box(meanrow,scale);mid=Fraction(L+U,2*scale)
    rad=Fraction(U-L,2*scale);float_mean=float(mid);difference=abs(Fraction.from_float(float_mean)-mid)
    gram_radius_squared+=rad*rad;gram_float_squared+=difference*difference
    all_float_ok=all_float_ok and difference<=Fraction(1,2**52)
    directed_error=exact_arb(gram_radius_squared).sqrt().upper()
    float_error=exact_arb(gram_float_squared).sqrt().upper()
    fulltail=box_from_record(tail['best_complete_tail_bounds']['128']['complete_moving_h2_L2_to_physical_C_L2_tail']).upper()
    full_error=((directed_error+float_error)**2+fulltail**2).sqrt().upper()
    gates=[dict(name=name,passed=bool(ok)) for name,ok in (
        ('same complete actual centre and exact continuous repair',True),
        ('all cumulative repair components to the true cut retained',len(offset)==65),
        ('complete original eta interval retained before every branch',args.half_width==Fraction(1,10**9)),
        ('the compact nu control is exactly absent at the true cut',args.cut>=Fraction(9,50)),
        ('actual physical angle is an oriented real circle diffeomorphism',jac_lower>0),
        ('all 128 physical cosine rows and 97 moving mean/cosine columns retained',len(rows)==128 and all(len(r['exact_interval_numerators'])==97 for r in rows)),
        ('every omitted exponential Fourier coefficient is paid',all(box_from_record(r['complete_exponential']['complete_exponential_A0_tail'])<goal for r in rows)),
        ('physical mean is retained as its exact separate derivative',meanrow<0),
        ('every binary64 proposal is rounded from the exact rational midpoint',all_float_ok),
        ('the normalized input/output Gram factors are paid',gram_radius_squared>=0 and gram_float_squared>=0),
        ('the full omitted physical output tail is separately retained',fulltail<arb(10)**-8),
        ('the actual entire matrix has a finite directed operator error',full_error.is_finite()),
    )]
    report=dict(kind='actual_repaired_moving96_physical128_complete_C_port_matrix',complete=all(g['passed'] for g in gates),
        source_sha256=sha(__file__),candidate_sha256=CURRENT_SHA,derived_definition_sha256=DEFINITION,
        input_sha256={str(p):sha(p) for p in (args.candidate,args.object,args.repair,args.tail)},
        exact_cut=str(args.cut),actual_candidate_piece=piece,actual_scalar_germ=list(map(str,germ)),
        whole_original_eta=True,parameter_half_width=str(args.half_width),exact_alpha=str(alpha),exact_nu=meta['exact_float_nu'],
        normalization='physical unnormalized moving variation; raw mean/cos amplitudes in, physical cos amplitudes out',
        input_columns=['mean']+[f'cos({4*j} phi)' for j in range(1,97)],physical_rows=128,
        h1_all_columns_exactly_zero=True,input_Gram='diag(1,1/2,...,1/2)',nonmean_output_Gram='diag(1/2,...,1/2)',
        mean_output_Gram='1',exact_interval_denominator=str(scale),dyadic_midpoint_denominator=str(2*scale),rows=rows,
        physical_mean_row=dict(exact_interval_numerator=[str(L),str(U)],dyadic_midpoint_numerator=str(L+U),
            exact_binary64_proposal_hex=float_mean.hex(),all_nonmean_input_columns_exactly_zero=True),
        complete_actual_mean=record(m),actual_physical_angle_Jacobian_lower=record(jac_lower),
        true_intrinsic_coefficients={k:record(v) for k,v in intrinsic.items()},
        exact_cut_physical_offset=list(map(str,offset)),exact_cut_finite_candidate=list(map(str,vals)),
        complete_phase_sine_coefficients=[record(z) for z in psi],
        complete_directed_matrix_Gram_error=record(directed_error),complete_binary64_rounding_Gram_error=record(float_error),
        complete_physical_tail_L2_gain=record(fulltail),complete_matrix_and_tail_L2_operator_error=record(full_error),
        no_finite_head_identified_with_same_physical_head=True,no_whole_body_inverse_proved=True,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_candidate_shards.py','fourfold_codazzi_current_positive_complete_coefficients.py',
            'fourfold_codazzi_final_continuous_value_repair.py','fourfold_codazzi_final_head_to_physical_C_tail.py',
            'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_phase_metric_defect.py','fourfold_phase_beta_bulk_interval.py')},
        gates=gates,seconds=time.monotonic()-started)
    save(args.out,report)
    print(dict(complete=report['complete'],matrix_error=directed_error.str(14),rounding_error=float_error.str(14),
        full_error=full_error.str(14),mean=m.str(14),seconds=report['seconds']),flush=True)
    if not report['complete']:raise RuntimeError('a complete physical port matrix gate failed')


if __name__=='__main__':main()
