#!/usr/bin/env python3
"""Certify an anisotropic low46 box from the actual variable-strip Green.

Floating iteration only proposes dyadic box sizes and metric weights.  Every
mathematical gate is recomputed with outward Arb bounds from the real source.
The boundary problem is still the auxiliary projected pointwise problem with
the exact LINEAR R18 far subspaces, not the full nonlinear far graph.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import resource
import time

from flint import arb,ctx
from closure_real_head_source_enclosure import exact_q,power2,ball_record
from closure_real_head_green_enclosure import load_json,ball,maximum


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--green',type=Path,required=True)
    p.add_argument('--reference',type=Path,required=True)
    p.add_argument('--ready',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--precision',type=int,default=192)
    args=p.parse_args();ctx.prec=args.precision;started=time.monotonic()
    G,graw=load_json(args.green);R,rraw=load_json(args.reference);ready,readyraw=load_json(args.ready)
    if G['modes']!=list(range(2,93,2)):raise ValueError('All 46 low modes are required')
    if G['input_hashes'].get(str(args.reference))!=hashlib.sha256(rraw).hexdigest():
        raise ValueError('Reference does not match Green envelope')
    if G['input_hashes'].get(str(args.ready))!=hashlib.sha256(readyraw).hexdigest():
        raise ValueError('Source ready does not match Green envelope')
    params=ready['rationalDeepModel']['physicalParameters']
    rc=exact_q(params['rCuff']);eps=exact_q(params['epsilonScale'])/rc**7
    d0=exact_q(params['delta0']);ln2=arb(2).log();cells=list(range(12,225));N=len(cells)
    if [r['cell'] for r in R['cell_rows']]!=cells:raise ValueError('Incomplete whole-cell reference')
    X=[ball(r['reference_X']).upper() for r in R['cell_rows']]
    B=[];radii=[]
    for n in cells:
        delta=d0*power2(-n)
        B.append((power2(12)*rc**3/eps*(-arb(19)*delta.log()/4).exp()).upper())
        radii.append((power2(-23)*eps/rc**3*(arb(19)*delta.log()/4).exp()).lower())
    A=[[(power2(e)*B[n]*X[n]*X[n]/X[k]).upper()
         for n,e in enumerate(row)] for k,row in enumerate(G['gamma_log2_upper'])]
    # Proposals are allowed to use ordinary floating arithmetic; no success
    # claim follows from this phase.  They are then fixed as exact dyadics.
    Af=[[float(x) for x in row] for row in A];u=[1.0]*N
    for _ in range(80):
        v=[1+sum(a*x*x for a,x in zip(row,u)) for row in Af]
        if not all(math.isfinite(x) and x>=1 for x in v):raise ArithmeticError('Box proposal diverged')
        u=v
    target_lip=.75
    L=[[4*a*u[n]/target_lip for n,a in enumerate(row)] for row in Af]
    w=[1.0]*N
    for _ in range(100):
        w=[1+sum(a*x for a,x in zip(row,w)) for row in L]
        if not all(math.isfinite(x) and x>=1 for x in w):raise ArithmeticError('Norm-weight proposal diverged')
    U=[exact_q(Q.from_float(x+2**-30*y)) for x,y in zip(u,w)]
    W=[exact_q(Q.from_float(y)) for y in w]
    rows=[];map_gate=True;small_gate=True;lip=arb(0);min_slack=None
    for k,n in enumerate(cells):
        mapping=sum((A[k][j]*U[j]*U[j] for j in range(N)),arb(0)).upper()
        slack=U[k]-1-mapping
        local_lip=(sum((4*A[k][j]*U[j]*W[j] for j in range(N)),arb(0))/W[k]).upper()
        local_small=U[k]*X[k]/radii[k]
        map_gate=map_gate and bool(slack>0);small_gate=small_gate and bool(local_small<1)
        lip=maximum(lip,local_lip)
        normalized_slack=slack/W[k]
        min_slack=normalized_slack if min_slack is None else min(min_slack.lower(),normalized_slack.lower())
        rows.append(dict(cell=n,total_radius_multiple=ball_record(U[k]),
            correction_radius_multiple=ball_record(U[k]-1),metric_weight_multiple=ball_record(W[k]),
            normalized_map_bound=ball_record(mapping),map_slack=ball_record(slack),
            Lipschitz_row_bound=ball_record(local_lip),relative_to_R23_ball=ball_record(local_small)))
    delta=d0*power2(-224);physical_scale=eps/rc**3*(arb(11)*delta.log()/2).exp()
    reference_z=ball(R['reference_far_z_bound']).upper()
    far_loss=ball(R['far_conversion_factor']).upper()
    Z=(reference_z+(U[-1]-1)*X[-1]*far_loss/physical_scale).upper()
    far_gate=bool(Z<power2(-2200));lip_gate=bool(lip<exact_q(Q(4,5)))
    gates=dict(box_invariant=map_gate,all_R23_balls=small_gate,
        contraction_less_than_four_fifths=lip_gate,all46_far_ball_below_2minus2200=far_gate)
    result=dict(status='Verified auxiliary low46 pointwise fixed point in a variable-strip anisotropic box' if all(gates.values()) else 'Anisotropic sufficient gates not all paid',
        gates=gates,modes=G['modes'],strip_formula=G['strip_formula'],
        domain='For every cell n, X_tau_n(correction) <= (U_n-1)*X_reference_n; all 46 modes are retained.',
        distance='max_n X_tau_n(difference)/(W_n*X_reference_n); metric weights and box radii are independent.',
        map_formula='A_kn = 2**gamma_kn * B_n * X_reference_n**2 / X_reference_k; map <= A U**2.',
        contraction_formula='sup_k sum_n 4 A_kn U_n W_n / W_k.',
        proposal='80 ordinary iterations of u=1+A u², 100 of w=1+(4 A diag(u)/(3/4))w; exact dyadic U=u+2^-30 w and W=w are then certified from scratch.',
        maximum_contraction=ball_record(lip),minimum_map_slack_divided_by_metric_weight=ball_record(min_slack),
        complete_far_z_bound=ball_record(Z),complete_far_log2_z=ball_record(Z.log()/ln2),
        far_margin_bits=ball_record(-2200-Z.log()/ln2),rows=rows,
        input_hashes={str(args.green):hashlib.sha256(graw).hexdigest(),str(args.reference):hashlib.sha256(rraw).hexdigest(),str(args.ready):hashlib.sha256(readyraw).hexdigest()},
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        limits=['This certifies only the pointwise vector field projected at output into low46, with the complete mean root.',
            'The far boundary is the actual linear R18 subspace; coupling to the nonlinear R18 graph is still required.',
            'Full high-frequency head-generated forcing, exterior cells0..11, the actual strong H vector and prefix matching are not certified.',
            'The ordinary floating proposal is not evidence; only the listed outward interval gates are used.'])
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(gates=gates,lip=str(lip),far_log2=str(Z.log()/ln2),
        map_slack=str(min_slack),largest_U=str(max(U)),far_U=str(U[-1]),
        seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)
    if not all(gates.values()):raise SystemExit(1)


if __name__=='__main__':main()
