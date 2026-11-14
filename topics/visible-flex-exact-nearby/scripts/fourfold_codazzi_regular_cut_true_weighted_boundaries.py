#!/usr/bin/env python3
"""Verify both complete boundaries in the exact cut-to-waist radial weight.

The independent mean and all 96 odd boundary rows remain present.  The
cap error is transformed on its actual even input columns, and the saved
cut/waist frames are checked as exact dyadic matrices with their full Gram.
The last polynomial-to-waist-anchor jump remains a separate required
interface.  This boundary certificate alone grants no continuous inverse.
"""
from __future__ import annotations
import argparse,hashlib,json,time
from fractions import Fraction
from pathlib import Path
from flint import arb,arb_mat,ctx
from fourfold_codazzi_regular_cut_projector_validator import (
    Frames,read,save,sha,gram,exact_matrix,symmetric_largest_upper,
    identity,transpose,CANDIDATE,REPAIR,DIM,MODES)
from fourfold_codazzi_regular_cut_interval_model import q,record,matrix_norm,block

PROPOSAL='6dbc3acfcfbdd051c83344561f13102d30f20699db1e0046357d0ede1ec79639'
CUT='528e2f47d4572d7b90878abc542c3389d76d5fb326d7ef7c3390ef086d6266ba'
CAP_CUT='36f498e3b0addbb46290c12fae6b63af7673db20ba230e22dd83809d18427104'
MESH='f94fd64f8faff800dfe67ea6689905b87acde06964d10eb667629d5c8cd25a75'


def interval(value):
    return arb(value['lower']).lower().union(arb(value['upper']).upper())


def upper(document,key):return interval(document['bounds'][key]).upper()


def exact_hex(value):return q(Fraction.from_float(float.fromhex(value)))


def left_boundary(frame):
    Q=exact_matrix(frame);G,Gi,g,gg,fee=gram(Q)
    UQ=block(Q,0,MODES,0,MODES)
    # A verified inverse of all 96 actual odd restrictions, not a sampled SVD.
    UQi=UQ.inv();lifting=Q*UQi
    Lsquare,spectral=symmetric_largest_upper(transpose(lifting)*lifting)
    if not Lsquare>=1:raise ValueError('the complete left restriction lost its contraction identity')
    L0=Lsquare.sqrt().upper();D0=(Lsquare-1).sqrt().upper()
    return dict(
        complete_waist_anchor_Gram_error=record(fee),
        complete_waist_anchor_Gram_lower=record(g),
        complete_waist_inverse_lifting_L0=record(L0),
        complete_waist_feedback_D0=record(D0),
        complete_waist_restriction_singular_lower=record((1/L0).lower()),
        full_waist_lifting_spectral_verification=spectral,
        full_waist_inverse_source_lifting_columns=MODES,
        all_97_even_states_including_independent_mean_preserved=True,
        feedback_identity='D0_exact^2=L0_exact^2-1 because U Ustar=I96 and the complete orthogonal projector has rank96',
        boundary_location='original saved full dyadic Qwaist at the virtual 0-minus side',
        final_zero_length_projector_jump_to_the_interior_is_still_required=True)


def right_boundary(frame,cut,complete,rho):
    Q=exact_matrix(frame);G,Gi,g,gg,fee=gram(Q)
    J=arb_mat([[exact_hex(x) for x in row['complete_even_binary64_proposal_hex']]
               for row in cut['rows']])
    M=[exact_hex(x) for x in cut['independent_mean_row']['binary64_proposal_hex']]
    if J.nrows()!=96 or J.ncols()!=97 or len(M)!=97:
        raise ValueError('one of the complete original mean or odd rows was lost')
    B=arb_mat([[arb(int(i==j)) for j in range(MODES)]
        +[J[i,j]/q(rho) for j in range(97)] for i in range(MODES)]
        +[[arb(0) for _ in range(MODES)]+[x/q(rho) for x in M]])
    low=upper(complete,'complete_true_low_odd_matrix_error')
    mean=upper(complete,'complete_true_independent_mean_row_error')
    total=upper(complete,'complete_true_low_97_row_matrix_error')
    high=upper(complete,'complete_true_moving_high_output')
    # The odd block is the exact identity; every unknown cap error acts
    # only on the complete even input, including its independent mean.
    Qeven=block(Q,MODES,DIM,0,MODES)
    qeven=matrix_norm(Qeven)
    proposed=matrix_norm(B*Q)
    true_kernel=((proposed+total*qeven/q(rho))/g.sqrt()).upper()
    mean_margin=interval(complete['bounds']['true_mean_coefficient_absolute_lower_bound']).lower()
    if not mean_margin>0:raise ValueError('the independent actual mean has no positive margin')
    J0=arb_mat([[J[i,0]] for i in range(MODES)])
    actual_J0=(matrix_norm(J0)+low).upper()
    aa=(actual_J0/mean_margin).upper();bb=(q(rho)/mean_margin).upper()
    trace=(1+aa*aa+bb*bb).upper()
    ell=((trace+(trace*trace-4*bb*bb).sqrt())/2).sqrt().upper()
    sigma=(1/ell).lower()
    complement_square=(sigma*sigma-true_kernel*true_kernel).lower()
    if not complement_square>0:
        raise ValueError('the actual weighted complete 97-row complement failed rank')
    complement=complement_square.sqrt().lower()
    LR=(1/complement).upper();DL=(LR*true_kernel).upper()
    gap=(ell*true_kernel).upper()
    if not gap<1:raise ValueError('the true weighted kernel is not close enough to the saved cut frame')
    return dict(
        exact_cut_rho=str(rho),
        complete_cut_anchor_Gram_error=record(fee),
        complete_cut_anchor_Gram_lower=record(g),
        complete_cut_anchor_even_block_operator_upper=record(qeven),
        full_weighted_nominal_boundary_on_exact_cut_frame=record(proposed),
        full_weighted_true_boundary_on_exact_cut_projector=record(true_kernel),
        weighted_true_low_odd_matrix_error=record((low/q(rho)).upper()),
        weighted_true_independent_mean_row_error=record((mean/q(rho)).upper()),
        weighted_true_low_97_row_matrix_error=record((total/q(rho)).upper()),
        weighted_complete_moving_high_output=record((high/q(rho)).upper()),
        weighted_true_independent_mean_coefficient_lower=record((mean_margin/q(rho)).lower()),
        weighted_true_full_boundary_explicit_right_inverse=record(ell),
        weighted_true_full_boundary_row_singular_lower=record(sigma),
        weighted_true_complement_singular_lower=record(complement),
        weighted_true_right_source_lifting_LR=record(LR),
        weighted_true_right_feedback_DL=record(DL),
        weighted_true_kernel_to_saved_cut_projector_gap=record(gap),
        boundary_formula='B_R=B_true diag(I96,rho^-1 I97), with exact nominal [I96,J/rho;0,M/rho]',
        all_97_true_rows_and_all_193_input_states_retained=True,
        unknown_high_inputs_still_require_their_own_operator_and_source_contract=True,
        full_high_output_bound_does_not_mean_the_low_kernel_annihilates_high_rows=True,
        no_additional_cut_projector_jump_needed=True)


def run(a,doc):
    def gate(name,ok):
        doc['gates'].append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError('complete weighted boundary gate failed: '+name)
    gate('exact_original_complete_native_inputs',
        sha(a.proposal)==PROPOSAL and sha(a.cut)==CUT and sha(a.cap_cut)==CAP_CUT)
    proposal,cut,complete=read(a.proposal),read(a.cut),read(a.cap_cut)
    process=read(a.cap_cut_process)
    gate('actual_public_complete_cap_cut_child_success',
        str(process.get('run_id'))=='43587619797' and process.get('complete')
        and not process.get('failure') and process.get('repository')=='Rogerhu12/math-research-public'
        and bool(process.get('children'))
        and all(child.get('actual_returncode')==0 for child in process['children']))
    gate('actual_all_fourteen_complete_cap_cut_gates',
        complete.get('complete') and not complete.get('failure')
        and len(complete.get('gates',[]))==14 and all(x['passed'] for x in complete['gates'])
        and complete.get('candidate_sha256')==CANDIDATE
        and complete.get('derived_definition_sha256')==REPAIR
        and complete.get('actual_moving_parameter_offset')=='0'
        and complete.get('complete_low_cut_rows')==97
        and complete.get('true_low_cut_kernel_dimension')==96)
    gate('complete_original_independent_mean_and_odd_identity',
        cut.get('complete') and not cut.get('failure')
        and cut.get('candidate_sha256')==CANDIDATE and cut.get('derived_definition_sha256')==REPAIR
        and cut.get('exact_cut')=='9/10' and cut.get('exact_odd_block')=='I_96'
        and cut.get('no_head_or_high_boundary_row_deleted'))
    gate('actual_complete_original_5970_cell_frame_proposal',
        proposal.get('complete') and not proposal.get('failure')
        and len(proposal.get('rows',[]))==5970
        and proposal.get('exact_covered_interval')==['0','9/10']
        and proposal['identity']['input_SHA256']['cut-native']==CUT
        and proposal['identity']['complete_background']['candidate_sha256']==CANDIDATE
        and proposal['identity']['complete_background']['derived_continuous_centre_definition_sha256']==REPAIR)
    mesh_path=a.frames/'exact-weight-and-base-mesh.json';mesh=read(mesh_path)
    gate('same_complete_exact_continuous_weight_mesh',sha(mesh_path)==MESH
         and proposal['identity']['exact_weight_mesh_sha256']==MESH)
    nodes=list(map(Fraction,mesh['exact_base_partition']))
    rhos=list(map(Fraction,mesh['exact_positive_rho_nodes']))
    gate('entire_weight_positive_and_complete',len(nodes)==len(rhos) and nodes[0]==0
        and nodes[-1]==Fraction(9,10) and all(x>0 for x in rhos)
        and all(x<y for x,y in zip(nodes,nodes[1:])))
    frames=Frames(a.frames,proposal)
    Qcut,_,cut_chunk=frames.pair(0)
    _,Qwaist,waist_chunk=frames.pair(5969)
    gate('complete_original_boundary_frame_dimensions',Qcut.shape==(193,96) and Qwaist.shape==(193,96))
    doc['left']=left_boundary(Qwaist)
    gate('all_96_waist_rows_verified_with_full_Gram',True)
    doc['right']=right_boundary(Qcut,cut,complete,rhos[-1])
    gate('all_97_true_weighted_cut_rows_verified_with_full_Gram',True)
    doc.update(complete=True,exact_interval=['0','9/10'],candidate_sha256=CANDIDATE,
        derived_definition_sha256=REPAIR,exact_affine_parameter_offset='0',
        physical_parameter='fixed original physical eta0; zero affine offset is not physical eta=0',
        exact_waist_rho=str(rhos[0]),exact_cut_rho=str(rhos[-1]),
        original_full_frame_chunks=dict(cut=cut_chunk,waist=waist_chunk),
        exact_cut_anchor_array_sha256=hashlib.sha256(Qcut.tobytes()).hexdigest(),
        exact_waist_anchor_array_sha256=hashlib.sha256(Qwaist.tobytes()).hexdigest(),
        boundary_source_convention='p(0-minus)<=D0 q(0-minus)+L0 ||g0||; q(L)<=DL p(L)+LR ||gL||',
        all_5970_polynomial_to_original_anchor_jumps_including_the_waist_required=True,
        ordinary_physical_state_norm_conversion='||h(r)||_physical<=max(1,rho(r)^-1) ||R(r)h(r)||',
        complete_continuous_Green_inverse_proved=False,
        full_particular_response_error_proved=False,unknown_high_input_feedback_paid=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('proposal','frames','cut','cap-cut','cap-cut-process','out'):
        p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every complete or failed true weighted boundary outcome')
    doc=dict(kind='actual_complete_true_weighted_cut_and_waist_boundaries_v1',
        complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        input_sha256={name:sha(getattr(a,name.replace('-','_')))
                      for name in ('proposal','cut','cap-cut','cap-cut-process')})
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['wall_seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=doc['complete'],gates=len(doc['gates']),
        L0=doc['left']['complete_waist_inverse_lifting_L0']['upper'],
        D0=doc['left']['complete_waist_feedback_D0']['upper'],
        LR=doc['right']['weighted_true_right_source_lifting_LR']['upper'],
        DL=doc['right']['weighted_true_right_feedback_DL']['upper'],
        seconds=doc['wall_seconds'])),flush=True)


if __name__=='__main__':main()
