#!/usr/bin/env python3
"""Choose exact dyadic time corrections, then verify the actual new residual.

The stored Fourier/Bernstein reference at one fixed complex label is kept
as its original exact mathematical function. Each added time polynomial has
exact rational complex coefficients and vanishes exactly at u=-1. Floating
or interval midpoints choose the correction; only a fresh true-field residual
verification grants a bound. No full initial-label or full-branch claim.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time
from flint import arb,acb,acb_series,ctx
from fourfold_phase_field_time_refined_root import RefinedGermTimeModel
from fourfold_phase_reference_time_sample import load_segment,reference_time_coefficients
from fourfold_phase_field_time_taylor import polynomial,record_complex
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def midpoint_fraction(value):
    a,b=value.mid().man_exp()
    return Fraction(int(a))*Fraction(2)**int(b)


def choose_correction(model,result,L):
    m=model.precision;old=ctx.cap;ctx.cap=m
    try:
        logq=polynomial(L,m);q=logq.exp()
        density=result['e0']*(-logq).exp()
        integrated=[acb(0)]+[-model.h*density[i-1]/i for i in range(1,m)]
        integrated[0]=-sum((integrated[i]*(-1)**i for i in range(1,m)),acb(0))
        candidate=q*acb_series(integrated,prec=m)
        chosen=[(Fraction(0),Fraction(0))]+[(midpoint_fraction(candidate[i].real),
                                            midpoint_fraction(candidate[i].imag)) for i in range(1,m)]
        chosen[0]=tuple(-sum((chosen[i][c]*(-1)**i for i in range(1,m)),Fraction(0)) for c in range(2))
        if any(sum((chosen[i][c]*(-1)**i for i in range(m)),Fraction(0)) for c in range(2)):
            raise ValueError('exact left-endpoint correction is not zero')
        return chosen
    finally:ctx.cap=old


def summarize(result):
    return dict(residuals={k:ball_record(result[k]) for k in ['e0_bound','e1_bound','e0_tail','e1_tail']},
        local_R60={k:ball_record(result[k]) for k in ['qmin','qmax','A','B','C','denominator','R','actual_error_upper']},
        analytic_outer_domain={k:ball_record(v) for k,v in result['domain'].items()},
        hypothetical_matching_left_flow_proved=result['local_matching_initial_flow_proved'],
        e0_coefficients=[record_complex(result['e0'][i]) for i in range(result['e0'].prec)],
        e1_coefficients=[record_complex(result['e1'][i]) for i in range(result['e1'].prec)])


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--order',type=int,default=32)
    p.add_argument('--iterations',type=int,default=2);p.add_argument('--bits',type=int,default=192)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args();ctx.prec=args.bits
    if args.order<8 or args.iterations<1:raise ValueError('positive correction count and adequate time order required')
    manifest_path=Path('data/phase_ring_continuation/r61_step3_shared_forward/manifest.json')
    object_path=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json')
    root_path=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_root_tight.json')
    files=[Path(__file__),manifest_path,object_path,root_path]+[Path(__file__).with_name(name) for name in
        ['fourfold_phase_field_time_refined_root.py','fourfold_phase_field_time_taylor.py','fourfold_phase_reference_time_sample.py']]
    provenance={str(path):sha(path) for path in files};start=time.monotonic()
    manifest,shard,shard_path,real,imag,a,b=load_segment(manifest_path,419)
    left,right=Fraction(31,64),Fraction(33,64);ta,tb=a+(b-a)*left,a+(b-a)*right
    model=RefinedGermTimeModel(object_path,root_path,(ta+tb)/2,(tb-ta)/2,
        nodes=512,order=args.order,outer_radius=8,branch_sign=manifest['trace_identity']['sign'])
    theta,L=reference_time_coefficients(real,imag,acb(exact_arb(Fraction(1,2)),exact_arb(Fraction(1,512))),left,right)
    theta+= [acb(0)]*(model.precision-len(theta))
    steps=[];corrections=[]
    for iteration in range(args.iterations+1):
        result=model.residual_bound(theta,L,Fraction(1,65536))
        if not result['local_matching_initial_flow_proved']:raise ValueError('new actual R60 tube failed')
        row=summarize(result);row['iteration']=iteration;steps.append(row)
        print(json.dumps(dict(iteration=iteration,e0=str(result['e0_bound']),e1=str(result['e1_bound']),
                              elapsed_seconds=time.monotonic()-start)),flush=True)
        if iteration==args.iterations:break
        chosen=choose_correction(model,result,L)
        corrections.append([[str(a),str(b)] for a,b in chosen])
        for i,(a,b) in enumerate(chosen):theta[i]+=acb(exact_arb(a),exact_arb(b))
    report=dict(kind='actual_time_reference_dyadic_defect_correction_and_reverification',complete=True,
        provenance=provenance,reference_shard_sha256=sha(shard_path),root_refinement=model.root_package.provenance,
        exact_delta_fraction=str(model.target.affine_delta),segment=419,subspan=['31/64','33/64'],
        exact_time_endpoints=list(map(str,[ta,tb])),label={'real':'1/2','imag':'1/512'},
        time_coordinate='tau=tau_center+h*u, exact u in [-1,1]',bits=args.bits,time_order=args.order,
        original_reference_definition='Frozen R61 Fourier/Bernstein reference evaluated at the stated exact complex label',
        corrections_exact_complex_fraction_coefficients=corrections,all_corrections_exactly_zero_at_left=True,
        steps=steps,elapsed_seconds=time.monotonic()-start,
        limitations=['One fixed initial label and one time subspan, no full-circle or full-branch bound.',
                    'Every local flow comparison has matching left initial state, not globally accumulated error.',
                    'The L reference is unchanged; corrections only improve the true position residual.'])
    args.out.write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':main()
