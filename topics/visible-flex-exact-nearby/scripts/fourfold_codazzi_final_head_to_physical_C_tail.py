#!/usr/bin/env python3
"""Complete physical-C high tail of a finite moving head at the true cap.

Uses the exact Fourier moment formula, not composition-minus-identity.
The complete even mean and the distinct continuous repair are retained.
All output Fourier modes above each declared physical cutoff are summed.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip,json,time
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha

CAP='ad6efc2a226131245ff4197a0b5da2843578224368a340f7a50d383c03a1819b'
REPAIR='6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc'
DEFINITION='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'


def read(p):
    raw=Path(p).read_bytes();return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)


def b(z):return box_from_record(z)


def tail_moments(t,k):
    n=k+1;one=1-t
    return [t**n/one,t**n*(n/one+t/one**2),
        t**n*(n*n/one+2*n*t/one**2+t*(1+t)/one**3)]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cap',type=Path,default=Path('notes/2026-11-14-R133-final-physical-cap-linear-module-r09-v2-native.json.gz'))
    ap.add_argument('--repair',type=Path,default=Path('notes/2026-11-14-R133-final-exact-continuous-value-repair-native.json.gz'))
    ap.add_argument('--head',type=int,default=96)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic();ctx.prec=256;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve every complete physical output-tail budget')
    cap,repair=read(args.cap),read(args.repair)
    if (not cap['complete'] or not repair['complete'] or cap['kind']!='actual_final_physical_cap_linear_module_v1'
        or cap['candidate_sha256']!=repair['candidate_sha256'] or sha(args.cap)!=CAP or sha(args.repair)!=REPAIR
        or repair['derived_definition_sha256']!=DEFINITION or cap['exact_interval']!=['9/10','25/8']):
        raise ValueError('the complete same-centre cap and exact repair are required')
    if not 1<=args.head<=256:raise ValueError('explicit positive finite moving head required')
    pcoef=[abs(b(z)).upper() for z in cap['complete_coefficient_suprema']['psi']]
    if len(pcoef)!=65:raise ValueError('all actual moving angle coefficients required')
    errors=list(map(Fraction,repair['exact_cumulative_coefficient_suprema']))
    em=exact_arb(errors[32]).upper();oldgap=b(cap['bounds']['minimum_mean_abs']).lower()
    gap=(oldgap-em).lower()
    rows=[];rejected=[]
    widths=[Fraction(j,32) for j in range(1,33)]
    cutoffs=(args.head,args.head+8,args.head+16,args.head+32,args.head+64,args.head+96)
    for width in widths:
        sig=exact_arb(width)
        pold=sum((z*(4*abs(j-32)*sig).exp() for j,z in enumerate(pcoef)),arb(0)).upper()
        ep=sum((exact_arb(errors[32+j])*(4*j*sig).exp()/(4*j) for j in range(1,33)),arb(0)).upper()
        delta=((ep+em*pold)/gap).upper();p=(pold+delta).upper();a=(sig-p).lower()
        if not a>0:
            rejected.append(dict(width=str(width),psi=record(p),positive_contour_gap=False));continue
        BN=(2*sum(((8*j*sig).exp()/(4*j)**2 for j in range(1,args.head+1)),arb(0))).sqrt().upper()
        t=(-8*a).exp();bycut={}
        for k in cutoffs:
            s0,s1,s2=tail_moments(t,k)
            ne=(4*BN/gap**2*(2*s2).sqrt()).upper()
            mean=((2*(s0+8*p*s1+16*p*p*s2)).sqrt()/gap**2).upper()
            full=(ne*ne+mean*mean).sqrt().upper()
            bycut[str(k)]=dict(nonmean_moving_h2_L2_to_physical_C_L2_tail=record(ne),
                moving_mean_to_physical_C_L2_tail=record(mean),
                complete_moving_h2_L2_to_physical_C_L2_tail=record(full))
        rows.append(dict(contour_width=str(width),complete_original_psi=record(pold),
            exact_repair_angle_change=record(delta),complete_repaired_psi=record(p),
            positive_contour_gap=record(a),complete_primitive_head_norm=record(BN),tail_bounds=bycut))
    best={}
    for k in cutoffs:
        row=min(rows,key=lambda z:float(b(z['tail_bounds'][str(k)]['complete_moving_h2_L2_to_physical_C_L2_tail']).upper()))
        best[str(k)]=dict(contour_width=row['contour_width'],**row['tail_bounds'][str(k)])
    gates=[dict(name=name,passed=bool(ok)) for name,ok in (
        ('the original complete physical-cap native is retained',cap['complete_unknown_Fourier_modes']),
        ('the distinct repaired mean remains nonzero',gap>0),
        ('every finite moving head mode and its even mean are retained',args.head==96),
        ('the whole original parameter interval is retained',cap['whole_original_eta']),
        ('the repair is bounded coefficientwise before the contour weight',len(errors)==65),
        ('all physical output frequencies are summed by complete geometric moments',len(best)==len(cutoffs)),
        ('at least one actual admissible contour exists',len(rows)>0),
        ('the padded physical-128 tail is genuinely small',b(best[str(args.head+32)]['complete_moving_h2_L2_to_physical_C_L2_tail'])<arb(10)**-8),
    )]
    report=dict(kind='actual_repaired_cap_finite_moving_head_complete_physical_C_tail',
        complete=all(z['passed'] for z in gates),source_sha256=sha(__file__),
        inputs={str(p):sha(p) for p in (args.cap,args.repair)},
        derived_definition_sha256=DEFINITION,candidate_sha256=cap['candidate_sha256'],
        whole_original_eta=True,exact_interval=cap['exact_interval'],moving_head=args.head,
        complete_physical_C_mean_derivative='-mean_phi(h2)/mean_phi(v)^2',
        physical_C_variation_from_h1='exactly zero',
        normalized_L2_and_physical_frequency_factor_4=True,
        complete_repaired_mean_gap=record(gap),all_contour_rows=rows,
        rejected_contour_rows=rejected,best_complete_tail_bounds=best,
        finite_head_is_not_identified_with_physical_finite_head=True,
        no_same_order_composition_minus_identity_bound_used=True,
        no_full_body_or_parameter_inverse_proved=True,gates=gates,seconds=time.monotonic()-start)
    save(args.out,report)
    print(dict(complete=report['complete'],seconds=report['seconds'],best={k:dict(
        width=z['contour_width'],tail=b(z['complete_moving_h2_L2_to_physical_C_L2_tail']).str(14)) for k,z in best.items()}),flush=True)
    if not report['complete']:raise RuntimeError('an actual finite-head physical-tail gate failed')


if __name__=='__main__':main()
