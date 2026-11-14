#!/usr/bin/env python3
"""Exact continuous finite direction and complete negative-interval norms.

The full all-regular finite response is an explicit dyadic function.  It
is not declared to be the true PDE response.  Repair its value jumps by
the exact same algebra as the background, including all193 states and
the mean, then enclose its entire finite Fourier polynomial on the real
negative interval.  Scalar values come only from the proved Taylor cache.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

from flint import arb, ctx
import numpy as np
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_final_continuous_value_repair import iter_repair, fraction
from fourfold_codazzi_phase_scalar_cache_jets import read, restrict_model
from fourfold_phase_beta_bulk_interval import exact_arb, real_interval
from fourfold_phase_metric_defect import record, save, sha

CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
TRIAL='ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6'
REPAIR='6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc'
COVER='94492bbafda1e5efb30b129e534171c9fc305524a2d972064e34e8894948bad3'
DEFINITION='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'


def up(x):return abs(x).upper()


def evaluate(coeff, piece, component, x, scale=Fraction(1), offset=Fraction(0)):
    ans=arb(0)
    for j in range(4):
        ans=ans*x+exact_arb(scale*fraction(coeff[j,piece,component]))
    return ans+exact_arb(offset)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--trial',type=Path,required=True)
    ap.add_argument('--repair',type=Path,default=Path('notes/2026-11-14-R133-final-exact-continuous-value-repair-native.json.gz'))
    ap.add_argument('--cover',type=Path,default=Path('notes/2026-11-14-R133-complete-169-germ-phase-scalar-cover-native.json.gz'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=256
    if args.out.exists():raise FileExistsError('preserve every actual direction consumption')
    for p,h in ((args.candidate,CANDIDATE),(args.trial,TRIAL),(args.repair,REPAIR),(args.cover,COVER)):
        if sha(p)!=h:raise ValueError(f'the exact explicit family input changed: {p}')
    base,trial=load_candidate(args.candidate),load_candidate(args.trial)
    bm,tm=(json.loads(str(x['metadata'])) for x in (base,trial))
    if not (tm['role']=='response_full' and tm['original_fourth_Robin_row_retained'] and
            tm['finite_head_mean_was_not_removed_from_the_solve'] and
            tm['background_candidate_sha256']==CANDIDATE and tm['modes']==96 and
            tm['coordinates']=='physical unnormalized moving variation; h1 sine(4j phi), h2 cosine(4j phi) including its true mean'):
        raise ValueError('the complete physical all-regular finite direction is required')
    if base['piece_coefficients'].shape!=(4,6144,65) or trial['piece_coefficients'].shape!=(4,6144,193):
        raise ValueError('the complete original and response cubic shapes are required')
    if not np.array_equal(base['radial_nodes'].view(np.uint64),trial['radial_nodes'].view(np.uint64)):
        raise ValueError('the exact physical direction must use the same actual radial interfaces')
    if not np.array_equal(trial['initial_state'].view(np.uint64),trial['piece_coefficients'][3,0,:].view(np.uint64)):
        raise ValueError('the complete original trial initial state must be the actual first right trace')
    repair,cover=read(args.repair),read(args.cover)
    if not (repair['complete'] and repair['derived_definition_sha256']==DEFINITION and cover['complete']):
        raise ValueError('complete same-centre repair and scalar cover are required')
    left,right=map(Fraction,cover['exact_complete_interval'])
    nodes=list(map(fraction,base['radial_nodes']));alpha=Fraction(bm['exact_float_amplitude'])
    base_fee=list(map(Fraction,repair['exact_cumulative_coefficient_suprema']))
    bmax=[arb(0) for _ in range(65)];qmax=[arb(0) for _ in range(193)]
    qrepairmax=[Fraction(0) for _ in range(193)];qjump=[Fraction(0) for _ in range(193)]
    qmean={};bmean={};prefix_rows=[];last_offset=None;count=0;exact_components=0
    digest=hashlib.sha256();prefix_last=-1;zero_left=False
    for piece,offset,jump in iter_repair(trial,Fraction(1)):
        if piece==0:zero_left=all(x==0 for x in offset)
        digest.update((json.dumps(dict(piece=piece,physical_offset=list(map(str,offset))),
            sort_keys=True,separators=(',',':'))+'\n').encode())
        qrepairmax=[max(a,abs(z)) for a,z in zip(qrepairmax,offset)]
        if jump is not None:
            count+=1;exact_components+=len(jump)
            qjump=[a+abs(z) for a,z in zip(qjump,jump)]
        last_offset=offset
        if nodes[piece]<right:
            end=min(nodes[piece+1],right);x=real_interval(Fraction(0),end-nodes[piece])
            qvalues=[evaluate(trial['piece_coefficients'],piece,k,x,offset=offset[k]) for k in range(193)]
            bvalues=[evaluate(base['piece_coefficients'],piece,k,x,scale=alpha)+arb(0,exact_arb(base_fee[k])) for k in range(65)]
            qmax=[max(a,up(z)).upper() for a,z in zip(qmax,qvalues)]
            bmax=[max(a,up(z)).upper() for a,z in zip(bmax,bvalues)]
            qmean[piece]=qvalues[96];bmean[piece]=bvalues[32]
            prefix_rows.append(dict(piece=piece,interval=[str(nodes[piece]),str(end)],
                complete_direction_mean=record(qvalues[96]),
                complete_base_finite_mean_without_s=record(bvalues[32]),
                exact_direction_mean_offset=str(offset[96])))
            prefix_last=piece
        if piece%512==0:
            print(dict(exact_repaired_pieces=piece+1,prefix_pieces=len(prefix_rows),seconds=time.monotonic()-started),flush=True)
    if count!=6143 or exact_components!=6143*193:
        raise ValueError('the complete physical direction has an omitted exact interface')
    mmax=arb(0);zmax=arb(0);mgap=arb(1000000);all_negative=True
    mean_rows=[];piece=0
    for germ in cover['germs']:
        path=Path(germ['path'])
        if sha(path)!=germ['sha256']:raise ValueError('a complete scalar germ changed')
        for row in read(path)['rows']:
            a,b=map(Fraction,row['interval']);cursor=a
            while nodes[piece+1]<=cursor:piece+=1
            while cursor<b:
                end=min(b,nodes[piece+1]);s=restrict_model(row,'s',cursor,end,0)[2]
                m=s+bmean[piece];z=qmean[piece]
                mmax=max(mmax,up(m)).upper();zmax=max(zmax,up(z)).upper()
                if not m<0:all_negative=False
                else:mgap=min(mgap,(-m).lower()).lower()
                mean_rows.append(dict(interval=[str(cursor),str(end)],piece=piece,
                    complete_base_mean=record(m),complete_direction_mean=record(z)))
                cursor=end
                if cursor==nodes[piece+1] and cursor<right:piece+=1
    widths=[Fraction(1,64),Fraction(1,32),Fraction(1,16),Fraction(1,8)]
    bf=[4*j for j in range(1,33)]+[0]+[4*j for j in range(1,33)]
    qf=[4*j for j in range(1,97)]+[0]+[4*j for j in range(1,97)]
    # Replace only the base finite mean by the complete s+finite mean.
    # Every nonmean coefficient and the genuine direction mean is retained.
    bmax[32]=mmax;qmax[96]=zmax
    norms={};repairnorms={}
    for width in widths:
        w=exact_arb(width);br=[(k*w).exp().upper() for k in bf];qr=[(k*w).exp().upper() for k in qf]
        component={}
        for j in range(4):
            component[str(j)]=dict(
                base_u=record(sum((bmax[k]*br[k]*bf[k]**j for k in range(32)),arb(0)).upper()),
                base_v=record(sum((bmax[k]*br[k]*bf[k]**j for k in range(32,65)),arb(0)).upper()),
                direction_xi=record(sum((qmax[k]*qr[k]*qf[k]**j for k in range(96)),arb(0)).upper()),
                direction_zeta=record(sum((qmax[k]*qr[k]*qf[k]**j for k in range(96,193)),arb(0)).upper()))
        norms[str(width)]=component
        repairnorms[str(width)]=[record(sum((exact_arb(z)*weight*k**j for z,weight,k in zip(qrepairmax,qr,qf)),arb(0)).upper()) for j in range(4)]
    definition=dict(kind='exact_continuous_repair_of_full_physical_response_direction',
        original_trial_sha256=TRIAL,background_definition_sha256=DEFINITION,
        offset_rule='z_0=0; z_j=z_(j-1)-(q_j(r_j)-q_(j-1)(r_j))',
        complete_offset_sequence_sha256=digest.hexdigest(),physical_frequency_factor=4,
        modes=96,all193_states_and_mean_retained=True,exact_interval=['0','25/8'],
        original_trial_was_not_changed=True,direction_not_asserted_to_solve_PDE=True)
    definition_sha=hashlib.sha256((json.dumps(definition,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
    tests=[
        ('all6143 times193 original interface identities were checked with exact rational arithmetic',exact_components==6143*193),
        ('the direction has the original exact zero left repair',zero_left),
        ('all genuine mean and all96 angular pairs remain in the physical direction',len(qmax)==193),
        ('the full complete scalar cover reaches the exact phase endpoint',mean_rows[0]['interval'][0]=='0' and mean_rows[-1]['interval'][1]==str(right)),
        ('the explicit base mean is negative over the whole actual negative interval',all_negative and mgap>0),
        ('the complete explicit parameter disc keeps the scalar mean negative',mgap-exact_arb(Fraction(1,1000000))*zmax>0),
        ('all complete analytic direction norms are finite',all(z.is_finite() for z in qmax)),
    ]
    report=dict(kind='actual_exact_continuous_explicit_phase_direction_and_complete_norms',
        complete=all(bool(ok) for _,ok in tests),source_sha256=sha(__file__),
        candidate_sha256=CANDIDATE,original_trial_sha256=TRIAL,repair_input_sha256=REPAIR,
        scalar_cover_sha256=COVER,background_definition_sha256=DEFINITION,
        derived_direction_definition=definition,derived_direction_definition_sha256=definition_sha,
        exact_alpha=str(alpha),exact_nu=bm['exact_float_nu'],
        actual_affine_parameter='eta_0',exact_affine_offset='0',whole_original_eta=False,
        exact_phase_interval=[str(left),str(right)],prefix_piece_count=len(prefix_rows),prefix_last_piece=prefix_last,
        exact_interface_count=count,exact_component_interface_count=exact_components,
        exact_complete_repair_coefficient_suprema=list(map(str,qrepairmax)),
        exact_sum_original_direction_jump_moduli=list(map(str,qjump)),
        exact_right_physical_direction_offset=list(map(str,last_offset)),
        exact_right_mean_offset=str(last_offset[96]),
        direction_repair_full_interval_joint_derivative_norms=repairnorms,
        complete_negative_interval_direction_coefficient_suprema=[record(x) for x in qmax],
        complete_negative_interval_base_coefficient_suprema=[record(x) for x in bmax],
        complete_joint_Wiener_homogeneous_angular_derivative_norms=norms,
        complete_base_mean_abs_upper=record(mmax),complete_direction_mean_abs_upper=record(zmax),
        complete_base_mean_abs_lower=record(mgap),
        complete_mean_margin_on_parameter_disc=record((mgap-exact_arb(Fraction(1,1000000))*zmax).lower()),
        complete_mean_restrictions=mean_rows,
        no_original_target_or_primitive_recomputed=True,
        finite_response_used_only_as_explicit_direction=True,actual_response_error_not_paid_here=True,
        full_PDE_parameter_Schur_not_proved=True,original_finite_response_success_or_failure_not_relabelled=True,
        dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            'fourfold_codazzi_candidate_shards.py','fourfold_codazzi_final_continuous_value_repair.py',
            'fourfold_codazzi_phase_scalar_cache_jets.py','fourfold_phase_metric_defect.py')},
        gates=[dict(name=name,passed=bool(ok)) for name,ok in tests],seconds=time.monotonic()-started)
    save(args.out,report)
    print(dict(complete=report['complete'],direction_definition=definition_sha,
        mean_base=mmax.str(16),mean_direction=zmax.str(16),mean_gap=mgap.str(16),
        prefix_pieces=len(prefix_rows),seconds=report['seconds']),flush=True)
    if not report['complete']:raise RuntimeError('an explicit direction norm gate failed; actual report retained')


if __name__=='__main__':main()
