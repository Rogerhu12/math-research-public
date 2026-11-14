#!/usr/bin/env python3
"""Enclose a variable-strip real linear reference and the full low46 far ball.

No ODE is solved here.  Actual stored real columns and their verified dyadic
endpoints are consumed.  All 46 possible correction heights enter the far
ball estimate, although the chosen reference has only eight nonzero heights.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import time
import resource

from flint import arb,ctx
from closure_real_head_source_enclosure import exact_q,power2,ball_record
from closure_real_head_green_enclosure import load_json,ball,endpoint,maximum


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--columns',type=Path,required=True)
    p.add_argument('--ready',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--relative-radius',default='1/500')
    p.add_argument('--far-strip',type=int,default=38)
    p.add_argument('--far-log2-ball',type=int,default=-2200)
    p.add_argument('--precision',type=int,default=192)
    args=p.parse_args();ctx.prec=args.precision;started=time.monotonic()
    data,raw=load_json(args.columns);ready,ready_raw=load_json(args.ready)
    if data['modes']!=list(range(2,93,2)):
        raise ValueError('All 46 deep parameters must be retained')
    if hashlib.sha256(ready_raw).hexdigest() not in data['input_hashes'].values():
        raise ValueError('The source ready does not match the real columns')
    params=ready['rationalDeepModel']['physicalParameters']
    rc=exact_q(params['rCuff']);eps=exact_q(params['epsilonScale'])/rc**7
    d0=exact_q(params['delta0']);ln2=arb(2).log()
    cells=list(range(12,225));tau=[1+arb(n-12)*ln2/4 for n in cells]
    X=[arb(0) for _ in cells]
    amplitudes={row['mode']:max(abs(endpoint(row['required_far_Q']['lower'])),
        abs(endpoint(row['required_far_Q']['upper']))).upper() for row in data['endpoint_rows']}
    group_hashes={}
    for group_ref in data['column_groups']:
        group_path=Path(group_ref['path']);group,graw=load_json(group_path)
        digest=hashlib.sha256(graw).hexdigest()
        if digest!=group_ref['sha256']:raise ValueError('Column group hash differs')
        group_hashes[str(group_path)]=digest
        if [row['cell'] for row in group['cell_rows']]!=cells:
            raise ValueError('Noncontiguous or incorrect cell order')
        for k,row in enumerate(group['cell_rows']):
            for col in row['linear_rows']:
                m=col['mode'];amp=amplitudes[m]
                if amp:
                    X[k]+=(tau[k]*m).exp()*amp*((1+m)**3*ball(col['column_Q_sup']).upper()
                        +(1+m)*ball(col['column_Xi_sup']).upper())
    delta_far=d0*power2(-224)
    physical_scale=eps/rc**3*(arb(11)*delta_far.log()/2).exp()
    reference_z=sum(((arb(args.far_strip*m)).exp()*amp for m,amp in amplitudes.items()),arb(0))/physical_scale
    gap=arb(args.far_strip)-tau[-1]
    losses=[dict(mode=m,value=(gap*m).exp()/((1+m)**3)) for m in data['modes']]
    loss=arb(0);worst_mode=None
    for row in losses:
        if row['value']>loss:worst_mode=row['mode']
        loss=maximum(loss,row['value'])
    radius=exact_q(Q(args.relative_radius))
    correction_z=radius*X[-1]*loss/physical_scale
    complete_z=(reference_z+correction_z).upper()
    target=power2(args.far_log2_ball)
    rows=[];max_ratio=arb(0)
    for n,t,x in zip(cells,tau,X):
        delta=d0*power2(-n)
        r23=power2(-23)*eps/rc**3*(arb(19)*delta.log()/4).exp()
        B=power2(12)*rc**3/eps*(-arb(19)*delta.log()/4).exp()
        H=power2(8)*rc**7/eps*(-arb(23)*delta.log()/4).exp()
        ratio=x/r23;max_ratio=maximum(max_ratio,ratio)
        rows.append(dict(cell=n,tau=ball_record(t),reference_X=ball_record(x),
            reference_log2_X=ball_record(x.log()/ln2),
            relative_to_R23_radius=ball_record(ratio),
            complete_R23_source_L1=ball_record(B*x*x),
            complete_R23_mean_increment=ball_record(H*x*x)))
    result=dict(status='Validated real linear reference and conditional full low46 far-domain containment; no nonlinear head solution is asserted',
        strip_formula='tau_n = 1 + (n-12)*log(2)/4, each whole cell uses its stated constant strip',
        target_far_strip=args.far_strip,target_far_log2_ball=args.far_log2_ball,
        correction_norm='max_n (X_tau_n of correction on whole cell n)/(reference_X_n)',
        relative_correction_radius=str(Q(args.relative_radius)),
        reference_far_z_bound=ball_record(reference_z),reference_far_log2_z=ball_record(reference_z.log()/ln2),
        additional_strip_at_far=ball_record(gap),worst_far_conversion_mode=worst_mode,
        far_conversion_factor=ball_record(loss),
        full_46_correction_far_z_bound=ball_record(correction_z),
        full_46_correction_far_log2_z=ball_record(correction_z.log()/ln2),
        complete_far_z_bound=ball_record(complete_z),complete_far_log2_z=ball_record(complete_z.log()/ln2),
        reference_margin_bits=ball_record(arb(args.far_log2_ball)-reference_z.log()/ln2),
        complete_margin_bits=ball_record(arb(args.far_log2_ball)-complete_z.log()/ln2),
        target_far_ball_paid=bool(complete_z<target),
        all_corrected_R23_balls_paid=bool((1+radius)*max_ratio<1),
        maximum_reference_R23_ratio=ball_record(max_ratio),cell_rows=rows,
        input_hashes={str(args.columns):hashlib.sha256(raw).hexdigest(),str(args.ready):hashlib.sha256(ready_raw).hexdigest(),**group_hashes},
        source_hashes={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in
            ['closure_far_ball_and_variable_reference.py','closure_real_head_green_enclosure.py','closure_real_head_source_enclosure.py']},
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        limits=['The 1/500 correction ball is a domain specification, not an already constructed 46-mode or full-frequency correction.',
            'All 46 low deep correction heights enter the worst-mode conversion; no low parameter is omitted.',
            'The reference retains the saved eight nonzero node12 heights, not the stronger actual-prefix H vector.',
            'The source and mean are R23 complete pointwise quantities; their Green feedback still needs payment.'])
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['target_far_ball_paid','all_corrected_R23_balls_paid','reference_far_log2_z','complete_far_log2_z','reference_margin_bits','complete_margin_bits','worst_far_conversion_mode','elapsed_seconds','peak_RSS_KiB']}),flush=True)


if __name__=='__main__':main()
