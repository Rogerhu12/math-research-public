#!/usr/bin/env python3
"""Consume complete exact mean-error flows and compare q_star to phase Z.

This does not solve the body equation.  The original full finite trial,
its exact scalar-mean completion, and the phase direction remain distinct.
All mathematical arithmetic is intended for the public repository Actions.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

BODY='a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870'
DIRECTION='87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88'
TRIAL='ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6'
CENTRE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
Z='6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04'

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)
def exact(value):
    value=Fraction(value)
    return arb(value.numerator)/value.denominator
def interval(value):return arb(value['lower']).lower().union(arb(value['upper']).upper())
def record(value):
    value=arb(value)
    return dict(ball=value.str(80),lower=value.lower().str(80),upper=value.upper().str(80))
def save(path,document):
    raw=(json.dumps(document,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes(gzip.compress(raw,mtime=0) if path.suffix=='.gz' else raw)


def run(body,direction,process,document):
    def gate(name,test):
        document['gates'].append(dict(name=name,passed=bool(test)))
        if not test:raise ValueError('actual complete-mean gate failed: '+name)
    gate('original_complete_body_actual_process',
         str(process.get('run_id'))=='43586413510' and process.get('complete')
         and not process.get('failure') and process.get('repository')=='Rogerhu12/math-research-public'
         and process.get('complete_native_sha256')==BODY
         and bool(process.get('children'))
         and all(row.get('actual_returncode')==0 for row in process['children']))
    gate('complete_original_body_and_both_exact_means',
         body.get('kind')=='actual_complete_correlated_mean_errors_and_full_body_residuals_v1'
         and body.get('complete') and not body.get('failure')
         and body.get('exact_interval')==['0','25/8']
         and body.get('complete_original_common_cells')==7721
         and body.get('exact_continuous_completed_means')
         and body.get('complete_mean_residuals_exactly_zero')
         and body.get('all_original_nonmean_PPoly_jumps_retained'))
    gate('same_entire_original_193_state_response_trial',
         body['row_identity']['full_trials']['response']['sha256']==TRIAL
         and direction.get('original_trial_sha256')==TRIAL
         and body.get('candidate_sha256')==CENTRE
         and direction.get('candidate_sha256')==CENTRE)
    gate('exact_original_phase_direction_definition',
         direction.get('kind')=='actual_exact_continuous_explicit_phase_direction_and_complete_norms'
         and direction.get('complete') and not direction.get('failure')
         and direction.get('derived_direction_definition_sha256')==Z
         and direction.get('actual_response_error_not_paid_here'))
    rows=body['residual_rows'];response=list(reversed(body['response_error_reverse']))
    adjoint=body['adjoint_error_flow']
    gate('all_7721_original_flow_and_residual_rows_retained',len(rows)==len(response)==len(adjoint)==7721)
    sums={role:arb(0) for role in ('response','adjoint')}
    sup={role:arb(0) for role in sums};next_radius=Fraction(0)
    zones=[(Fraction(0),Fraction(9,10)),(Fraction(9,10),Fraction(25,8))]
    localized={f'{left}:{right}':{role:arb(0) for role in sums} for left,right in zones}
    residual_sums={role:{name:arb(0) for name in ('L2','H_one_third','H1')} for role in sums}
    signed=arb(0)
    for i,(row,rr,aa) in enumerate(zip(rows,response,adjoint)):
        left,right=map(Fraction,row['interval'])
        if (row['common_row']!=i or rr['common_row']!=i or aa['common_row']!=i
            or row['interval']!=rr['interval'] or row['interval']!=aa['interval']
            or left!=next_radius or right<=left):
            raise ValueError('a true original body or scalar-flow row was dropped, repeated or moved')
        next_radius=right
        if row['exact_response_mean_residual']!=0 or row['exact_adjoint_mean_residual']!=0:
            raise ValueError('the exact completed mean equations were not retained')
        for role,flow in (('response',rr),('adjoint',aa)):
            e=abs(interval(flow['entire'])).upper()
            if not interval(flow['entire']).contains(interval(row[role+'_mean_error'])):
                raise ValueError('the actual mean correction and residual correction differ')
            sums[role]+=exact(right-left)*e*e;sup[role]=max(sup[role],e).upper()
            for a,b in zones:
                length=max(Fraction(0),min(right,b)-max(left,a))
                if length:localized[f'{a}:{b}'][role]+=exact(length)*e*e
            for name in residual_sums[role]:
                bound=interval(row[role+'_complete_nonmean_residual'][name+'_L2_radial']).upper()
                if bound<0:raise ValueError('a residual norm is negative')
                residual_sums[role][name]+=bound*bound
        signed+=interval(row['signed_complete_dual_response_residual_integral'])
    gate('whole_exact_interval_without_any_gap_or_overlap',next_radius==Fraction(25,8))
    mean_norms={role:sums[role].sqrt().upper() for role in sums}
    repair=interval(direction['direction_repair_full_interval_joint_derivative_norms']['1/64'][0]).upper()
    repair_l2=(exact(Fraction(25,8)).sqrt()*repair).upper()
    gate('complete_mean_and_nonmean_phase_repair_fee',repair_l2<exact(Fraction(42,10**17)))
    qstar_to_Z=(mean_norms['response']+repair_l2).upper()
    remaining=(exact(Fraction(1,200))-qstar_to_Z).lower()
    gate('strict_positive_remaining_true_response_error_budget',remaining>0)
    gate('finite_native_signed_integral_recomputed_with_all_original_rows',signed.is_finite())
    gate('no_inverse_or_true_Schur_was_imported',not body['complete_BVP_inverse_proved']
         and not body['true_nu_Schur_nonzero_proved']
         and direction['full_PDE_parameter_Schur_not_proved'])
    document.update(complete=True,complete_original_common_cells=7721,exact_interval=['0','25/8'],
        original_response_trial_sha256=TRIAL,explicit_phase_direction_definition_sha256=Z,
        ordinary_L2_circle_normalization='mean weight 1, every sine/cosine weight 1/2',
        exact_mean_completion_minus_raw_trial={role:dict(L2_radial=record(mean_norms[role]),
            uniform_absolute=record(sup[role])) for role in sums},
        exact_mean_correction_on_subintervals={zone:{role:record(value.sqrt().upper())
            for role,value in roles.items()} for zone,roles in localized.items()},
        raw_trial_minus_Z_complete_L2_upper=record(repair_l2),
        mean_completed_response_minus_Z_complete_L2_upper=record(qstar_to_Z),
        remaining_sufficient_L2_true_response_minus_mean_completed_trial=record(remaining),
        complete_body_residual_norms={role:{name:record(value.sqrt().upper())
            for name,value in norms.items()} for role,norms in residual_sums.items()},
        signed_body_dual_response_residual_integral=record(signed),
        phase_direction_exact_right_physical_offset_retained=direction['exact_right_physical_direction_offset'],
        phase_direction_exact_right_mean_offset_retained=direction['exact_right_mean_offset'],
        application='At eta=0, a proved full ordinary L2 bound ||q_nu-q_star|| no larger than the recorded remaining budget implies ||q_nu-Z||<=1/200.',
        original_body_whole_parameter_half_width=body['row_identity']['original_parameter_half_width'],
        phase_application_parameter_offset='0',
        original_ac1_operator_not_relabelled_as_continuous_repair=True,
        actual_continuous_inverse_still_required=True,
        background_operator_change_fee_still_required=True,
        all_regular_boundary_and_high_frequency_fees_still_required=True,
        nonlinear_background_phase_change_still_required=True,
        continuous_BVP_inverse_proved=False,true_parameter_Schur_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('body','direction','actual-process','out'):p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args();ctx.prec=320;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every real complete or failed outcome')
    doc=dict(kind='actual_complete_body_mean_error_norms_and_explicit_direction_bridge_v1',
        complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        input_sha256={name:sha(getattr(a,name.replace('-','_'))) for name in ('body','direction','actual-process')},
        continuous_BVP_inverse_proved=False,true_parameter_Schur_proved=False)
    try:
        if sha(a.body)!=BODY or sha(a.direction)!=DIRECTION:
            raise ValueError('one of the exact complete original native inputs changed')
        run(read(a.body),read(a.direction),read(a.actual_process),doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:
        doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=doc['complete'],gates=len(doc['gates']),seconds=doc['seconds'])),flush=True)


if __name__=='__main__':main()
