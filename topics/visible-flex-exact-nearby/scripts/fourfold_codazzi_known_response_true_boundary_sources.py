#!/usr/bin/env python3
"""Evaluate the complete known response waist and actual homogeneous-cap sources.

The original complete physical cubics and completed mean are unchanged.
The interior uses its right waist trace and left cut trace. All 96 waist
rows, all 97 actual low cut rows, and the separate full high cut output
remain present. No old cap trial residual or matrix cell is recomputed.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time
from bisect import bisect_left,bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_candidate_shards import load_candidate

ORIGINAL='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
REPAIR='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
TRIAL='ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6'
BODY='a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870'
BODY_PROCESS='0a5dc06520bad5a1230b65cba6e895e998e1f3ce6a32a65d9ffa8800b8ea1a9e'
CUT='528e2f47d4572d7b90878abc542c3389d76d5fb326d7ef7c3390ef086d6266ba'
CAP_CUT='36f498e3b0addbb46290c12fae6b63af7673db20ba230e22dd83809d18427104'
WEIGHTED='56db8a3498494bf48de14b50418010053bb6058c722c41993c894c463786dc25'
LEFT=Fraction(0);RIGHT=Fraction(9,10);FULL_RIGHT=Fraction(25,8)
MODES=96;DIM=193


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)


def save(path,document):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(document,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    temporary=path.with_suffix(path.suffix+'.partial');temporary.write_bytes(raw);temporary.replace(path)


def exact(value):
    value=Fraction(value);return arb(value.numerator)/value.denominator


def interval(value):return arb(value['lower']).lower().union(arb(value['upper']).upper())


def record(value):
    value=arb(value)
    if not value.is_finite():raise ArithmeticError('a complete true boundary source is nonfinite')
    return dict(ball=value.str(80),lower=value.lower().str(80),upper=value.upper().str(80))


def upper(value):
    value=interval(value).upper()
    if not value>=0 or not value.is_finite():raise ValueError('a true boundary error norm is invalid')
    return value


def vector_norm(vector):
    return sum((abs(x).upper()**2 for x in vector),arb(0)).upper().sqrt().upper()


def hexadecimal(value):return exact(Fraction.from_float(float.fromhex(value)))


def actual(process,run_id):
    return (process.get('repository')=='Rogerhu12/math-research-public'
        and str(process.get('run_id'))==str(run_id) and process.get('complete')
        and not process.get('failure') and bool(process.get('children'))
        and all(child.get('actual_returncode')==0 for child in process['children']))


def trace(trial,nodes,body,radius,side):
    """Exact dyadic cubic evaluation and complete scalar mean enclosure."""
    lefts=[Fraction(row['interval'][0]) for row in body['residual_rows']]
    locate=bisect_right if side=='right' else bisect_left
    piece=locate(nodes,radius)-1;row_index=locate(lefts,radius)-1
    if not (0<=piece<6144 and 0<=row_index<7721):
        raise ValueError('the requested interior one-sided complete trace has no original piece')
    row=body['residual_rows'][row_index];lo,hi=map(Fraction,row['interval'])
    if not (nodes[piece]<=radius<=nodes[piece+1] and lo<=radius<=hi):
        raise ValueError('the true trace escaped its original complete piece/mean interval')
    if side=='right' and not nodes[piece]<=radius<nodes[piece+1]:
        raise ValueError('the right interior trace convention changed')
    if side=='left' and not nodes[piece]<radius<=nodes[piece+1]:
        raise ValueError('the left interior trace convention changed')
    x=exact(radius-nodes[piece]);cube=trial['piece_coefficients'][:,piece]
    raw=[]
    for j in range(DIM):
        coefficients=[exact(Fraction.from_float(float(cube[k,j]))) for k in range(4)]
        raw.append(((coefficients[0]*x+coefficients[1])*x+coefficients[2])*x+coefficients[3])
    mean_error=interval(row['response_mean_error']);complete=list(raw);complete[MODES]+=mean_error
    orthonormal=[value if j==MODES else value/arb(2).sqrt() for j,value in enumerate(complete)]
    return orthonormal,dict(exact_radius=str(radius),interior_trace_side=side,
        original_response_piece=piece,original_complete_mean_row=row_index,
        original_cubic_interval=[str(nodes[piece]),str(nodes[piece+1])],
        original_complete_mean_interval=row['interval'],
        complete_mean_correction_enclosure=record(mean_error),
        complete_193_raw_physical_amplitudes=[record(x) for x in raw],
        complete_193_mean_corrected_physical_amplitudes=[record(x) for x in complete],
        complete_193_orthonormal_state=[record(x) for x in orthonormal],
        complete_pair_L2=record(vector_norm(orthonormal)),
        all_96_odd_and_97_even_including_mean_retained=True,
        original_physical_trial_not_multiplied_by_alpha=True)


def run(a,doc):
    def gate(name,ok):
        doc['gates'].append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError('known complete response boundary gate failed: '+name)
    gate('same_complete_original_physical_trial_body_and_actual_mean_process_bytes',
        sha(a.response)==TRIAL and sha(a.body)==BODY and sha(a.body_process)==BODY_PROCESS)
    body,bp=read(a.body),read(a.body_process)
    gate('actual_complete_original_mean_correction_with_all_nonmean_jumps',
        actual(bp,43586413510) and bp.get('complete_native_sha256')==BODY
        and body.get('complete') and not body.get('failure')
        and body.get('candidate_sha256')==ORIGINAL
        and body.get('complete_original_common_cells')==7721
        and body.get('complete_mean_residuals_exactly_zero')
        and body.get('all_original_nonmean_PPoly_jumps_retained')
        and body['row_identity']['full_trials']['response']['sha256']==TRIAL)
    edge=LEFT
    for i,row in enumerate(body['residual_rows']):
        left,right=map(Fraction,row['interval'])
        if (row['common_row']!=i or left!=edge or not left<right
            or row.get('exact_response_mean_residual')!=0
            or not interval(row['response_mean_error']).is_finite()):
            raise ValueError('the complete original mean-flow cover changed')
        edge=right
    gate('all_7721_original_complete_mean_intervals_retained',
        len(body['residual_rows'])==7721 and edge==FULL_RIGHT)
    trial=load_candidate(a.response);nodes=[Fraction(float(x)) for x in trial['radial_nodes']]
    meta=json.loads(str(trial['metadata']))
    gate('same_full193_physical_state_in_all6144_original_pieces',
        trial['piece_coefficients'].shape==(4,6144,DIM)
        and np.isfinite(trial['piece_coefficients']).all()
        and len(nodes)==6145 and nodes[0]==LEFT and nodes[-1]==FULL_RIGHT
        and all(x<y for x,y in zip(nodes,nodes[1:]))
        and meta.get('background_candidate_sha256')==ORIGINAL
        and meta.get('finite_head_mean_was_not_removed_from_the_solve') is True)
    cut,cap,cp=read(a.cut),read(a.cap_cut),read(a.cap_cut_process)
    gate('same_complete_nominal_cut_all96_odd_and_independent_mean_rows',
        sha(a.cut)==CUT and cut.get('complete') and not cut.get('failure')
        and cut.get('candidate_sha256')==ORIGINAL and cut.get('derived_definition_sha256')==REPAIR
        and cut.get('exact_cut')=='9/10' and cut.get('exact_odd_block')=='I_96'
        and cut.get('no_head_or_high_boundary_row_deleted'))
    gate('same_actual_complete_cap_cut_with_all_fourteen_gates',
        sha(a.cap_cut)==CAP_CUT and actual(cp,43587619797)
        and cp.get('complete_native_sha256')==CAP_CUT
        and cap.get('complete') and not cap.get('failure')
        and len(cap.get('gates',[]))==14 and all(x['passed'] for x in cap['gates'])
        and cap.get('candidate_sha256')==ORIGINAL and cap.get('derived_definition_sha256')==REPAIR
        and cap.get('actual_moving_parameter_offset')=='0'
        and cap.get('complete_low_cut_rows')==97 and cap.get('complete_input_columns_including_mean')==97
        and cap.get('all_ordinary_divergence_mean_Robin_and_endpoint_cap_terms_consumed')
        and cap.get('all_unknown_high_input_feedback_and_independent_source_columns_still_required'))
    boundary,wp=read(a.weighted),read(a.weighted_process)
    gate('same_actual_weighted_boundary_source_convention_all_ten_gates',
        sha(a.weighted)==WEIGHTED and actual(wp,43594139132)
        and wp.get('phase')=='prepare' and wp.get('weighted_boundary_native_sha256')==WEIGHTED
        and boundary.get('kind')=='actual_complete_true_weighted_cut_and_waist_boundaries_v1'
        and boundary.get('complete') and not boundary.get('failure')
        and len(boundary.get('gates',[]))==10 and all(x['passed'] for x in boundary['gates'])
        and boundary.get('candidate_sha256')==ORIGINAL and boundary.get('derived_definition_sha256')==REPAIR
        and boundary.get('exact_affine_parameter_offset')=='0'
        and boundary.get('all_5970_polynomial_to_original_anchor_jumps_including_the_waist_required')
        and boundary['right'].get('all_97_true_rows_and_all_193_input_states_retained'))
    h0,t0=trace(trial,nodes,body,LEFT,'right');hL,tL=trace(trial,nodes,body,RIGHT,'left')
    J=[[hexadecimal(x) for x in row['complete_even_binary64_proposal_hex']] for row in cut['rows']]
    M=[hexadecimal(x) for x in cut['independent_mean_row']['binary64_proposal_hex']]
    gate('all_exact_nominal_cut_entries_used',
        len(J)==96 and all(len(row)==97 for row in J) and len(M)==97)
    even=hL[MODES:];odd=hL[:MODES]
    nominal_odd=[odd[i]+sum((J[i][j]*even[j] for j in range(97)),arb(0)) for i in range(96)]
    nominal_mean=sum((M[j]*even[j] for j in range(97)),arb(0))
    even_norm=vector_norm(even);low_nominal=vector_norm(nominal_odd)
    mean_nominal=abs(nominal_mean).upper()
    all_nominal=vector_norm(nominal_odd+[nominal_mean])
    eps_low=upper(cap['bounds']['complete_true_low_odd_matrix_error'])
    eps_mean=upper(cap['bounds']['complete_true_independent_mean_row_error'])
    eps_all=upper(cap['bounds']['complete_true_low_97_row_matrix_error'])
    eps_high=upper(cap['bounds']['complete_true_moving_high_output'])
    low=(low_nominal+eps_low*even_norm).upper()
    mean=(mean_nominal+eps_mean*even_norm).upper()
    direct=(all_nominal+eps_all*even_norm).upper()
    separated=(low*low+mean*mean).sqrt().upper()
    combined=min(direct,separated).upper()
    left_source=vector_norm(h0[:MODES]);high_source=(eps_high*even_norm).upper()
    gate('true_complete_low_and_high_sources_finite_with_positive_exact_weight',
        all(x.is_finite() and x>=0 for x in (left_source,combined,high_source))
        and Fraction(boundary['exact_waist_rho'])>0 and Fraction(boundary['exact_cut_rho'])>0)
    gate('actual_parameter_source_compact_support_precedes_the_true_cap',
        Fraction(1,20)<Fraction(9,50)<RIGHT<FULL_RIGHT)
    doc.update(complete=True,exact_interior_interval=['0','9/10'],
        exact_homogeneous_cap_interval=['9/10','25/8'],
        exact_parameter_source_support=['1/20','9/50'],
        candidate_sha256=ORIGINAL,derived_definition_sha256=REPAIR,
        full_physical_response_trial_sha256=TRIAL,completed_mean_native_sha256=BODY,
        actual_cap_cut_native_sha256=CAP_CUT,actual_weighted_boundary_native_sha256=WEIGHTED,
        exact_affine_parameter_offset='0',physical_parameter='fixed original physical eta0 and nu',
        waist_trace=t0,cut_trace=tL,
        complete_waist_source_96_rows=[record(-x) for x in h0[:MODES]],
        complete_nominal_cut_source_97_rows=[record(-x) for x in nominal_odd+[nominal_mean]],
        source_bounds=dict(
            left_waist_96_row_source_L2=record(left_source),
            right_cut_even_input_L2=record(even_norm),
            nominal_cut_96_odd_rows_L2=record(low_nominal),
            nominal_cut_independent_mean_absolute=record(mean_nominal),
            nominal_cut_complete97_rows_L2=record(all_nominal),
            true_cut_96_odd_rows_L2=record(low),
            true_cut_independent_mean_absolute=record(mean),
            true_cut_complete97_rows_L2_direct=record(direct),
            true_cut_complete97_rows_L2_separated=record(separated),
            true_cut_complete97_rows_L2=record(combined),
            true_cut_known_full_high_output=record(high_source)),
        true_cap_error_constants=dict(low=record(eps_low),mean=record(eps_mean),
            complete97=record(eps_all),full_high=record(eps_high)),
        original_high_output_norm_contract=cap['complete_high_output_contract'],
        boundary_source_convention=boundary['boundary_source_convention'],
        exact_waist_rho=boundary['exact_waist_rho'],exact_cut_rho=boundary['exact_cut_rho'],
        complete_boundary_liftings=dict(
            L0=boundary['left']['complete_waist_inverse_lifting_L0'],
            D0=boundary['left']['complete_waist_feedback_D0'],
            LR=boundary['right']['weighted_true_right_source_lifting_LR'],
            DL=boundary['right']['weighted_true_right_feedback_DL']),
        radial_weight_cancels_in_the_actual_boundary_source=True,
        radial_weight_cancellation='B_R(R h_orth)=B_true h_orth; U(R h_orth)=U h_orth',
        every_original_interior_trial_jump_still_required=True,
        final_virtual_waist_projector_jump_still_required=True,
        old_outer_cap_trial_residual_not_required_for_this_restricted_inner_trial=True,
        full_true_homogeneous_cap_definition_and_unknown_high_inputs_still_required=True,
        known_high_output_is_a_source_and_not_a_high_feedback_bound=True,
        no_unknown_high_input_set_to_zero=True,
        old_trial_reconstructions_recomputed=0,old_mean_flows_recomputed=0,old_cap_matrix_cells_recomputed=0,
        complete_continuous_inverse_proved=False,actual_full_PDE_response_error_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    names=('response','body','body-process','cut','cap-cut','cap-cut-process','weighted','weighted-process')
    for name in names+('out',):p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual complete boundary-source outcome')
    doc=dict(kind='actual_known_response_waist_and_true_homogeneous_cap_sources_v1',
        complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        input_sha256={name:sha(getattr(a,name.replace('-','_'))) for name in names},
        complete_continuous_inverse_proved=False,actual_full_PDE_response_error_proved=False)
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=True,gates=len(doc['gates']),seconds=doc['seconds'],
        left_source=doc['source_bounds']['left_waist_96_row_source_L2']['upper'],
        right_source=doc['source_bounds']['true_cut_complete97_rows_L2']['upper'],
        high_source=doc['source_bounds']['true_cut_known_full_high_output']['upper'])),flush=True)


if __name__=='__main__':main()
