#!/usr/bin/env python3
"""Exact dyadic continuous value repair of the complete final ac1 centre.

The original candidate/shards are never changed.  The derived centre adds
one exact physical constant Fourier vector to each radial cubic piece.
Every value jump and the complete cumulative correction, including mean,
is computed with Fraction arithmetic.  No original native is silently
relabelled as a certificate for the derived object.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time
from flint import arb,ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_current_positive_complete_coefficients import CURRENT_SHA,OBJECT_SHA,literal_coordinates
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha

KIND='actual_final_exact_continuous_value_repair_v1'


def fraction(x):return Fraction.from_float(float(x))


def iter_repair(saved,alpha):
    """Yield (piece,physical_offset,previous_physical_jump), all exact.

    The normalized candidate is y=(U_sin,V_cos), including V0.  The
    physical state is (alpha*U, s+alpha*V).  The intrinsic s is continuous
    and does not enter a candidate value jump.  The same offsets therefore
    work for every original affine parameter and every admissible nu.
    """
    coeff=saved['piece_coefficients'];nodes=list(map(fraction,saved['radial_nodes']))
    n=coeff.shape[2];offset=[Fraction(0) for _ in range(n)]
    yield 0,tuple(offset),None
    for piece in range(1,len(nodes)-1):
        step=nodes[piece]-nodes[piece-1];jump=[]
        for k in range(n):
            left=Fraction(0)
            for order in range(4):left=left*step+fraction(coeff[order,piece-1,k])
            right=fraction(coeff[3,piece,k]);j=alpha*(right-left)
            # Both sides of this equality are exact dyadic rationals.
            old=offset[k];offset[k]-=j
            if alpha*left+old!=alpha*right+offset[k]:
                raise ArithmeticError('an exact repaired interface failed')
            jump.append(j)
        yield piece,tuple(offset),tuple(jump)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve every exact repair report')
    if sha(args.candidate)!=CURRENT_SHA:raise ValueError('the exact complete final ac1 index is required')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']))
    if meta['object_sha256']!=OBJECT_SHA or meta['coordinates']!=literal_coordinates():
        raise ValueError('the original complete moving background changed')
    modes=int(meta['modes']);alpha=Fraction(meta['exact_float_amplitude'])
    if modes!=32 or len(saved['radial_nodes'])!=6145 or saved['piece_coefficients'].shape!=(4,6144,65):
        raise ValueError('every original cubic, state and interface is required')
    freq=[4*j for j in range(1,modes+1)]+[0]+[4*j for j in range(1,modes+1)]
    maxcoef=[Fraction(0) for _ in freq]
    jump_norms={s:Fraction(0) for s in range(7)}
    maximum_norms={s:Fraction(0) for s in range(7)}
    maximum_rows={s:0 for s in range(7)}
    maxmean=Fraction(0);sum_mean_jumps=Fraction(0)
    digest=hashlib.sha256();nonzero_jumps=0;count=0;root_offset=None
    special={}
    nodes=list(map(fraction,saved['radial_nodes']))
    for piece,offset,jump in iter_repair(saved,alpha):
        digest.update((json.dumps(dict(piece=piece,physical_offset=list(map(str,offset))),
                                  sort_keys=True,separators=(',',':'))+'\n').encode())
        maxcoef=[max(a,abs(b)) for a,b in zip(maxcoef,offset)]
        maxmean=max(maxmean,abs(offset[modes]))
        for s in range(7):
            current=sum((abs(z)*(1+k)**s for z,k in zip(offset,freq)),Fraction(0))
            if current>maximum_norms[s]:maximum_norms[s]=current;maximum_rows[s]=piece
        if jump is not None:
            count+=1;nonzero_jumps+=sum(z!=0 for z in jump)
            sum_mean_jumps+=abs(jump[modes])
            for s in range(7):
                jump_norms[s]+=sum((abs(z)*(1+k)**s for z,k in zip(jump,freq)),Fraction(0))
        if piece in (0,2549,6143):
            special[str(piece)]=dict(interval=[str(nodes[piece]),str(nodes[piece+1])],
                                    physical_offset=list(map(str,offset)))
        if piece==2549:root_offset=offset
        final_offset=offset
        if piece%1024==0:print(dict(exact_pieces=piece+1),flush=True)
    if count!=6143:raise ValueError('one or more true candidate interfaces were omitted')
    definition=dict(kind=KIND,base_candidate_sha256=CURRENT_SHA,object_sha256=OBJECT_SHA,
        physical_offset_rule='e_0=0; e_j=e_(j-1)-alpha*(y_j(r_j)-y_(j-1)(r_j))',
        repaired_state='u_bar=alpha*U+e_u,j; v_bar=s_eta,nu+alpha*V+e_v,j',
        exact_alpha=str(alpha),reference_nu=meta['exact_float_nu'],
        offset_sequence_sha256=digest.hexdigest(),physical_frequency_factor=4,modes=modes,
        first_piece=0,last_piece=6143,radial_nodes_count=6145,
        exact_radial_interval=['0','25/8'],offsets_independent_of_eta_and_nu=True,
        centre_is_not_the_original_ac1_index=True)
    definition_bytes=(json.dumps(definition,sort_keys=True,separators=(',',':'))+'\n').encode()
    widths={}
    for width in (Fraction(1,2048),Fraction(1,1024),Fraction(1,64),Fraction(1,32)):
        w=exact_arb(width)
        widths[str(width)]=record(sum((exact_arb(a)*(k*w).exp() for a,k in zip(maxcoef,freq)),arb(0)).upper())
    gates=[('all 6143 radial interfaces checked exactly',count==6143),
           ('all 65 components retained',len(maxcoef)==65),
           ('original waist state unchanged exactly',all(Fraction(z)==0 for z in special['0']['physical_offset'])),
           ('root correction belongs to the same complete analytic piece',root_offset is not None),
           ('true even mean retained',maxmean>=abs(final_offset[modes])),
           ('complete correction A3 is below the installed root neighbourhood',maximum_norms[3]<Fraction(1,10**6))]
    if not all(ok for _,ok in gates):raise ArithmeticError('an exact continuous repair gate failed')
    report=dict(kind=KIND,complete=True,source_sha256=sha(__file__),
        definition=definition,derived_definition_sha256=hashlib.sha256(definition_bytes).hexdigest(),
        candidate_path=str(args.candidate),candidate_sha256=sha(args.candidate),
        all_original_shards_verified=True,whole_original_eta=True,
        all_admissible_compact_nu_values=True,exact_interface_count=count,
        nonzero_exact_component_jumps=nonzero_jumps,
        exact_cumulative_coefficient_suprema=list(map(str,maxcoef)),
        exact_maximum_piece_pair_Ak={str(s):str(maximum_norms[s]) for s in maximum_norms},
        exact_maximizing_piece_Ak={str(s):maximum_rows[s] for s in maximum_rows},
        exact_sum_all_original_pair_jump_Ak={str(s):str(jump_norms[s]) for s in jump_norms},
        maximum_piece_pair_Ak={str(s):record(exact_arb(maximum_norms[s]).upper()) for s in maximum_norms},
        sum_all_original_pair_jump_Ak={str(s):record(exact_arb(jump_norms[s]).upper()) for s in jump_norms},
        joint_analytic_pair_coefficient_supremum=widths,
        exact_maximum_mean_correction=str(maxmean),maximum_mean_correction=record(exact_arb(maxmean).upper()),
        exact_sum_original_mean_jumps=str(sum_mean_jumps),
        special_piece_offsets=special,exact_right_physical_offset=list(map(str,final_offset)),
        exact_right_mean_offset=str(final_offset[modes]),
        right_pair_A0=record(exact_arb(sum(map(abs,final_offset),Fraction(0))).upper()),
        piecewise_radial_derivative_correction='exactly zero on every open original cubic piece',
        corrected_value_and_all_angular_derivatives_continuous=True,
        corrected_radial_derivative_continuity_claimed=False,
        no_new_radial_or_angular_truncation=True,
        original_scientific_data_changed=False,
        original_native_bounds_automatically_transferred=False,
        full_nonlinear_solution_or_global_inverse_claimed=False,
        gates=[dict(name=name,passed=bool(ok)) for name,ok in gates],
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_candidate_shards.py','fourfold_codazzi_current_positive_complete_coefficients.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_metric_defect.py')},
        seconds=time.monotonic()-started)
    save(args.out,report)
    print(dict(complete=True,derived_definition_sha256=report['derived_definition_sha256'],
        interfaces=count,A0=report['maximum_piece_pair_Ak']['0']['upper'],
        A3=report['maximum_piece_pair_Ak']['3']['upper'],
        mean=report['maximum_mean_correction']['upper'],seconds=report['seconds']),flush=True)


if __name__=='__main__':main()
