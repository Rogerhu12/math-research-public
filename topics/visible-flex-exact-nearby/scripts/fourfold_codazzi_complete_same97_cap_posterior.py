#!/usr/bin/env python3
"""Consume complete same97 cap adjoint Grams and true right-Poisson Grams.

All old targets, trials,7908 cells,5970 propagators and Grams are immutable.
New mathematics is only directed97-dimensional posterior matrix algebra.
"""
from __future__ import annotations
import argparse,json,math,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,arb_mat,ctx
import fourfold_codazzi_cap_adjoint_residual_Gram_core as core
import fourfold_codazzi_cap_adjoint_residual_Gram_pilot as pilot
import fourfold_codazzi_complete_directional_matrix_Green as matrix
from fourfold_codazzi_cap128_CI_worker import read,digest
from fourfold_phase_metric_defect import record

PUBLIC='Rogerhu12/math-research-public'
KIND='actual_complete_same97_cap_posterior_and_right_Poisson_contraction_v1'
CORE='689bf2c54350d832cffa7ca8f46dc424509fb221e3d73cb228a1f9a18130c0dc'
MATRIX='9dca5868ed04b051aa10799978412a4b74644ae75dea748bcdc4159b3d47659d'
CENTRE='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
PROPOSAL='acb2151b60f24ad88b30e6f7d1d966851abc53c15e45df19df2bfca27c2393c7'
PILOT_NATIVE='eb58b97ae182cedf621c4ff122b421ffb844e3839266a6a7d6df86b9134d8cfb'
TRUE_BOUNDARY='56db8a3498494bf48de14b50418010053bb6058c722c41993c894c463786dc25'
NOMINAL_CUT='528e2f47d4572d7b90878abc542c3389d76d5fb326d7ef7c3390ef086d6266ba'
WINDOWS=('whole_inner_body','fixed_complete_negative_phase_window','true_cut_trace')
GRAM_KEYS=('W_L','W_R','W_RB','W_R0','W_T','body_true','body_formal','body_Hessian')
PRODUCERS=dict(
    body=dict(kind='actual_complete7908_same_proposal_physical_adjoint_residual_Grams_v1',
        source='6b3a47a54386171b2c659c776bbfeff52ae0ebe4456ced5b67350f7eabf48a8d',
        worker='86c2a02bd23eb146fbe4ee4c61cb2fd98d35110c36fde8eed1d6f426e73efed7',
        manifest='baf3a42869c52ac0158ec6aac709aebced64a06efda8a8ea6d52939da71f1df5',
        logical='native/complete7908-cap-adjoint-Grams-finish.json.gz',phase='finish',
        label='complete7908_same_object_signed97_ordinary_adjoint_Gram_union'),
    boundary=dict(kind='actual_same97_adjoint_true_endpoints_and_complete_high_output_Grams_v1',
        source='4105236306bcb5c1d43821a44aca06fbea1f214fd983d8c48562a94dfde832dd',
        worker='ab34ab0edfeb69901b46b468255d9d74780a63742ade1bceec459ac226fb5cfe',
        manifest='b753b78658c11326aadb0b70fab2be440c690b1f3ac78fabcac42ca799612465',
        logical='native/complete97-true-cap-adjoint-boundary-and-high-Grams.json.gz',
        phase='true-boundary-and-high-Grams',
        label='true_endpoints_complete97_Grams_and_all_infinite_high_trial_outputs'),
    poisson=dict(kind='actual_complete97_right_boundary_Poisson_Grams_from_same_F_v1',
        source='312398be818621e156c08366f74c2850c61dcc283a44a30d7bb510a1cd51fca0',
        worker='971176325944e30135f91768e4c934f6076843a5f203430a15fbb05a6339083e',
        manifest='94e46b2262ce542eccf04e948eae29eee49d4e4bb62b80231afac48821a79181',
        logical='native/complete97-true-right-boundary-Poisson-Grams.json.gz',phase='right-Poisson',
        label='all5970_complete97_true_right_Poisson_input_Grams_and_all_posterior_defects'))
save,canonical,gate=pilot.save,pilot.canonical,pilot.gate
q,eye,zero=matrix.q,matrix.eye,matrix.zero
up=matrix.up
LENGTH=q(Fraction(25,8)-Fraction(9,10))


def input_identity(a):
    names=('body','body-process','boundary','boundary-process') if a.phase=='cap' else (
        'cap','cap-process','poisson','poisson-process')
    return {name:digest(getattr(a,name.replace('-','_'))) for name in names}


def actual_native(name,path,process,run,attempt,doc):
    spec=PRODUCERS[name];d,p=read(path),read(process);native=digest(path)
    receipt=[r for r in p.get('native_files',[]) if r.get('logical_file')==spec['logical']
        and r.get('sha256')==native]
    child=any(c.get('label')==spec['label'] and c.get('actual_returncode')==0
        for c in p.get('children',[]))
    reused=bool(p.get('original_complete_success_reused_without_child')
        and p.get('original_success_process_sha256'))
    gate(doc,'actual_complete_'+name+'_mathematics_and_artifact_receipt',
        p.get('repository')==PUBLIC and str(p.get('run_id'))==str(run)
        and str(p.get('run_attempt'))==str(attempt)
        and p.get('worker_source_sha256')==spec['worker']
        and p.get('input_manifest_sha256')==spec['manifest'] and p.get('phase')==spec['phase']
        and len(receipt)==1 and (child or reused)
        and (p.get('complete_native_sha256') is None or p.get('complete_native_sha256')==native)
        and d.get('kind')==spec['kind'] and d.get('source_sha256')==spec['source']
        and d.get('complete') and not d.get('failure')
        and d.get('gates') and all(g.get('passed') for g in d['gates']))
    return d,p


def arrays_from_receipt(root,receipt):
    relative=pilot.valid_relative(receipt['file']);path=root/relative
    if path.stat().st_size!=receipt['bytes'] or digest(path)!=receipt['sha256']:
        raise ValueError('one complete signed97 matrix archive changed its original bytes')
    with np.load(path,allow_pickle=False) as z:
        values={k:z[k].copy() for k in z.files}
    for name,value in values.items():
        if value.dtype!=np.dtype('float64') or not np.isfinite(value).all():
            raise ValueError('one complete signed matrix archive contains a nonfinite or nonfloat array')
    if receipt.get('arrays'):
        if set(values)!=set(receipt['arrays']):
            raise ValueError('one original complete matrix archive added or lost a scientific field')
        for name,value in values.items():
            r=receipt['arrays'][name]
            if (list(value.shape)!=r['shape'] or str(value.dtype)!=r['dtype']
                or matrix.base.raw_sha(value)!=r['raw_little_endian_array_sha256']):
                raise ValueError('one exact original raw matrix receipt changed')
    return values


def gram_single(arrays,receipt):
    if receipt.get('dimension')!=97 or not receipt.get('full_signed_cross_column_covariance_kept'):
        raise ValueError('a complete signed97 Gram including mean is required')
    values=np.asarray(arrays[receipt['array_key']],dtype=float)
    if values.shape!=(4753,):raise ValueError('one signed97 triangle has another dimension')
    A=matrix.unpack_symmetric(values,97)
    slack=q(Fraction.from_float(float.fromhex(receipt['exact_diagonal_slack_binary64_hex'])))
    if not slack>=0:raise ValueError('one exact Loewner rounding slack is negative')
    return matrix.exact(A)+eye(97)*slack


def norm_upper(G):
    # Positivity is proved by the original Gram construction and positive
    # complete-group algebra. This is not an eigenvalue sampling claim.
    return min(matrix.nonnegative(matrix.trace(G)),matrix.norm(G).upper()).upper()


def positive_weight(value,fallback_trace):
    objective=matrix.nonnegative(value)
    fallback=matrix.nonnegative(fallback_trace)*q(Fraction(1,2**160))
    chosen_value=max(objective,fallback).sqrt().upper()
    selected=float(chosen_value)
    if not math.isfinite(selected):raise ArithmeticError('a fixed positive Cauchy weight overflowed')
    if selected<=0:selected=math.ldexp(1.,-512)
    return q(Fraction.from_float(selected)),selected.hex()


def weighted_Gram(terms,H):
    """All terms are squared norms of operators on the same unknown input."""
    active=[];weight_sum=arb(0)
    for name,c,G in terms:
        c=matrix.nonnegative(c)
        if c==0:continue
        T=matrix.sym(G*(c*c));tr=matrix.nonnegative(matrix.trace(T))
        if tr==0:continue
        objective=matrix.dot_trace(H,T)
        alpha,encoded=positive_weight(objective,tr)
        active.append((name,T,alpha,encoded,objective,tr));weight_sum+=alpha
    if not active:return zero(97,97),[]
    result=zero(97,97);receipt=[]
    for name,T,alpha,encoded,objective,tr in active:
        result+=T*(weight_sum/alpha)
        receipt.append(dict(name=name,strictly_positive_exact_weight_binary64_hex=encoded,
            objective_trace_upper=record(objective),complete_PSD_trace_upper=record(tr),
            zero_directional_objective_does_not_delete_a_nonzero_matrix=True))
    return matrix.sym(result),receipt


def complete_groups(G,constants):
    LD=up(constants['outer_DN_LD']);L0=up(constants['outer_mean_L0'])
    common=[('true_left',arb(1),G['W_L']),('true_outer',arb(1),G['W_R']),
        ('true_outer_DN',LD,G['W_RB']),('independent_outer_mean',L0,G['W_R0'])]
    length=LENGTH.sqrt().upper()
    return dict(true_body=common+[('complete_true_ordinary_body',length,G['body_true'])],
        split_body=common+[('complete_formal_ordinary_body',length,G['body_formal']),
            ('complete_residual_Hessian_adjoint',length,G['body_Hessian'])])


def whole_candidates(G,constants,H,output,key):
    """Each complete candidate is a valid Loewner bound for all97 inputs."""
    kappa=up(constants['full_repaired_cap_kappa'])
    cstar=up(constants['actual_true_left_complete_even_map_norm_squared']).sqrt().upper()
    result={};diagnostics={}
    for group,terms in complete_groups(G,constants).items():
        E,weights=weighted_Gram(terms,H)
        E=matrix.sym(E*(kappa*kappa))
        E,er=matrix.covariance_bound(E,key+'_'+group+'_error',output)
        nested,nested_weights=weighted_Gram([
            ('complete_infinite_trial_high',arb(1),G['W_T']),
            ('complete_same_input_adjoint_error',cstar,E)],H)
        nested,nr=matrix.covariance_bound(nested,key+'_'+group+'_nested',output)
        direct,direct_weights=weighted_Gram(
            [('complete_infinite_trial_high',arb(1),G['W_T'])]
            +[(name,(cstar*kappa*c).upper(),T) for name,c,T in terms],H)
        direct,dr=matrix.covariance_bound(direct,key+'_'+group+'_direct',output)
        for form,W,receipt,ww in (('nested',nested,nr,nested_weights),
                ('one_complete_Cauchy',direct,dr,direct_weights)):
            name=group+'_'+form
            result[name]=W
            diagnostics[name]=dict(complete_Wcap=receipt,complete_Werr=er,
                full_cap_operator_upper=record(norm_upper(W).sqrt().upper()),
                signed_objective_trace_upper=record(matrix.dot_trace(H,W)),
                actual_error_weights=weights,actual_complete_cap_weights=ww,
                complete_body_choice=group,complete_Young_choice=form,
                all97_directions_and_mean_retained=True)
    selected=min(result,key=lambda name:float(matrix.dot_trace(H,result[name])))
    return result,diagnostics,selected


def cap_run(a,doc):
    body,bp=actual_native('body',a.body,a.body_process,a.body_run,a.body_attempt,doc)
    boundary,ep=actual_native('boundary',a.boundary,a.boundary_process,a.boundary_run,a.boundary_attempt,doc)
    identity=body.get('exact_object_identity',{});other=boundary.get('exact_identity',{})
    gate(doc,'same_complete_trial_repair_physical_background_and97_input_identity',
        identity and all(other.get(k)==v for k,v in identity.items())
        and identity.get('actual_proposal_native_sha256')==PROPOSAL
        and identity.get('core_source_sha256')==CORE
        and identity.get('original_inputs',{}).get('candidate')==CANDIDATE
        and boundary.get('complete_constants',{}).get('same_repaired_centre_definition_sha256')==CENTRE)
    gate(doc,'all7908_true_closed_body_quarters_and_complete_mean_are_present',
        body.get('phase')=='finish' and body.get('complete_quarter_count')==7908
        and body.get('original_successful_pilot_quarters_reused')==4
        and body.get('new_quarters_from_actual_ranges')==7904
        and body.get('original_successful_pilot_quarters_recomputed')==0
        and body.get('complete7908_adjoint_cover_proved')
        and body.get('mathematical_certificate_for_complete_ordinary_adjoint_body_Grams')
        and body.get('full_independent_even_mean_retained')
        and body.get('exact_true_interval')==['9/10','25/8']
        and len(body.get('complete_origin_receipts',[]))==7908)
    gate(doc,'all_true_endpoints_and_complete_infinite_high_output_Grams_are_present',
        [s.get('stage') for s in boundary.get('stages',[])]==['left','outer','high']
        and all(s.get('complete') for s in boundary['stages'])
        and boundary.get('completed_stages')==3
        and boundary.get('mathematical_certificate_for_true_endpoints_and_trial_high_output')
        and boundary.get('exact_true_endpoints')==['9/10','25/8'])
    gate(doc,'same_continuous_physical_Hermite_trial_has_no_internal_value_jumps',
        boundary.get('all_internal_exact_physical_value_jumps_zero')
        and boundary.get('original_one_sided_derivatives_remain_independent')
        and boundary.get('original_trial_node_count')==1977
        and len(identity.get('actual_proposal_array_receipts',[]))==7)
    G={};original_arrays=[]
    values=arrays_from_receipt(a.body_arrays,body['complete_new_array_receipt'])
    original_arrays.append(body['complete_new_array_receipt'])
    for name,key in (('body_true','complete_true_adjoint_ordinary'),
        ('body_formal','complete_formal_ordinary'),('body_Hessian','complete_Hessian_adjoint')):
        G[name]=gram_single(values,body['complete_signed97_Gram_receipts'][key])
    for stage in boundary['stages']:
        values=arrays_from_receipt(a.boundary_arrays,stage['array_receipt'])
        original_arrays.append(stage['array_receipt'])
        for name in GRAM_KEYS:
            if name in stage['complete_signed97_Gram_receipts']:
                if name in G:raise ValueError('one same-input component Gram was counted twice')
                G[name]=gram_single(values,stage['complete_signed97_Gram_receipts'][name])
    gate(doc,'all_eight_full_signed97_component_matrices_are_read_exactly_once',set(G)==set(GRAM_KEYS))
    outer=boundary['stages'][1]['metadata'];high=boundary['stages'][2]['metadata']
    constants=dict(boundary['complete_constants'],outer_DN_LD=outer['outer_DN_LD'],
        outer_mean_L0=outer['outer_mean_L0'],exact_body_length='89/40')
    gate(doc,'complete_high_output_mean_outer_DN_and_full_Green_constants_are_positive',
        high.get('true_complete_high_output_is_not_truncated')
        and high.get('lowest_moving_high_index')==97
        and high.get('independent_mean_input_retained_in_all_zC_nonmean_amplitudes')
        and up(constants['full_repaired_cap_kappa'])>0
        and up(constants['actual_true_left_complete_even_map_norm_squared'])>0
        and up(constants['outer_DN_LD'])>0 and up(constants['outer_mean_L0'])>0)
    arrays={};base_receipts={}
    for name in GRAM_KEYS:
        G[name],base_receipts[name]=matrix.covariance_bound(G[name],'base_'+name,arrays)
    candidates,receipts,selected=whole_candidates(G,constants,eye(97),arrays,'cap_only')
    gate(doc,'each_complete_cap_bound_is_finite_without_entrywise_minima',
        len(candidates)==4 and all(norm_upper(W).is_finite() for W in candidates.values()))
    a.arrays.mkdir(parents=True,exist_ok=True)
    ar=pilot.save_npz(a.arrays/'complete-same97-full-cap-posterior-Grams.npz',arrays)
    doc.update(complete=True,exact_object_identity=identity,
        complete_same_repaired_centre_definition_sha256=CENTRE,
        complete_original_Gram_array_receipts=original_arrays,
        complete_constants=constants,base_complete97_Gram_receipts=base_receipts,
        complete_cap_candidates=receipts,selected_complete_cap_candidate=selected,
        complete_full_cap_high_to97_operator_upper=receipts[selected]['full_cap_operator_upper'],
        complete_posterior_array_receipt=ar,all_internal_value_jumps_exactly_zero=True,
        all_full_body_and_boundary_error_channels_retained=True,
        complete_full_cap_high_to_low_bound_proved=True,
        original_targets_trials7908cells_and_old_Grams_recomputed=0,
        unknown_moving_high_input='all even Fourier |j|>=97, no finite input cutoff',
        exact_boundary_input_units='original97 regular row Euclidean coordinates; no second rho input weight',
        complete_true_right_Poisson_contraction_proved=False,
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)


def completed_cap(a,doc):
    d,p=read(a.cap),read(a.cap_process);actual=digest(a.cap)
    child=any(c.get('label')=='complete_same97_full_cap_posterior_matrices'
        and c.get('actual_returncode')==0 for c in p.get('children',[]))
    reused=p.get('original_complete_success_reused_without_child') and p.get('original_success_process_sha256')
    gate(doc,'same_source_actual_full_cap_posterior_complete_native',
        d.get('kind')==KIND and d.get('phase')=='cap' and d.get('source_sha256')==digest(__file__)
        and d.get('complete') and not d.get('failure')
        and d.get('gates') and all(x.get('passed') for x in d['gates'])
        and d.get('complete_full_cap_high_to_low_bound_proved')
        and d.get('complete_same_repaired_centre_definition_sha256')==CENTRE
        and p.get('repository')==PUBLIC and str(p.get('run_id'))==str(a.cap_run)
        and str(p.get('run_attempt'))==str(a.cap_attempt)
        and p.get('worker_source_sha256')==a.consumer_worker_sha
        and p.get('input_manifest_sha256')==a.consumer_manifest_sha and p.get('phase')=='cap'
        and len([x for x in p.get('native_files',[]) if
            x.get('logical_file')=='native/complete-same97-cap-posterior.json.gz'
            and x.get('sha256')==actual])==1 and (child or reused))
    return d


def compose_run(a,doc):
    cap=completed_cap(a,doc)
    poisson,pp=actual_native('poisson',a.poisson,a.poisson_process,a.poisson_run,a.poisson_attempt,doc)
    gate(doc,'true_complete97_Poisson_and_cap_share_repaired_centre_boundary_and_input_units',
        poisson.get('complete97_input_Poisson_Gram_bound_proved')
        and poisson.get('true_complete_finite193_BVP_only')
        and poisson.get('completed_rows')==5970
        and poisson.get('exact_inner_interval')==['0','9/10']
        and poisson.get('exact_negative_output_interval')==['0',str(matrix.PHASE_RIGHT)]
        and poisson.get('input_sha256',{}).get('boundary')==TRUE_BOUNDARY
        and poisson.get('input_sha256',{}).get('nominal-cut')==NOMINAL_CUT
        and poisson.get('exact_boundary_input_units')==cap.get('exact_boundary_input_units')
        and set(poisson.get('complete_true_right_Poisson_Gram_certificates',{}))==set(WINDOWS)
        and not poisson.get('complete_infinite_BVP_inverse_proved'))
    cv=arrays_from_receipt(a.cap_arrays,cap['complete_posterior_array_receipt'])
    pv=arrays_from_receipt(a.poisson_arrays,poisson['complete_true97_Gram_array_receipt'])
    G={k:matrix.read_covariance(cv,v) for k,v in cap['base_complete97_Gram_receipts'].items()}
    if set(G)!=set(GRAM_KEYS) or any(A.nrows()!=97 or A.ncols()!=97 for A in G.values()):
        raise ValueError('one same-input complete cap Gram lost the independent mean')
    old_candidates={k:matrix.read_covariance(cv,v['complete_Wcap'])
        for k,v in cap['complete_cap_candidates'].items()}
    arrays={};windows={}
    for window in WINDOWS:
        pr=poisson['complete_true_right_Poisson_Gram_certificates'][window]['actual_true97_input_Gram']
        H=matrix.read_covariance(pv,pr)
        if H.nrows()!=97 or H.ncols()!=97:raise ValueError('one true Poisson input Gram is incomplete')
        H,hr=matrix.covariance_bound(H,window+'_actual_true_Poisson',arrays)
        new,records,selected=whole_candidates(G,cap['complete_constants'],H,arrays,window)
        choices={name:dict(complete_Wcap=entry['complete_Wcap'],
            squared_signed_trace_upper=record(matrix.dot_trace(H,new[name])),
            operator_upper=record(matrix.dot_trace(H,new[name]).sqrt().upper()),
            origin='new_fixed_positive_weights_for_this_output')
            for name,entry in records.items()}
        for name,W in old_candidates.items():
            value=matrix.dot_trace(H,W)
            choices['original_'+name]=dict(
                complete_Wcap=cap['complete_cap_candidates'][name]['complete_Wcap'],
                squared_signed_trace_upper=record(value),operator_upper=record(value.sqrt().upper()),
                origin='exact_original_cap_only_matrix_without_recomputation')
        chosen=min(choices,key=lambda name:float(up(choices[name]['operator_upper'])))
        windows[window]=dict(actual_true97_Poisson_Gram=hr,
            original_actual_Poisson_Gram_receipt=pr,
            complete_new_cap_candidates=records,all_complete_contraction_choices=choices,
            selected_complete_contraction=chosen,complete_operator_upper=choices[chosen]['operator_upper'],
            signed_products_before_final_upper=True,
            original_ordinary_body_or_cut_trace_certificate_not_interchanged=True,
            individual_defect_objectives_not_interpreted_as_lower_bounds=True)
        gate(doc,'complete_'+window+'_signed97_trace_contraction_is_finite',
            up(windows[window]['complete_operator_upper']).is_finite())
    a.arrays.mkdir(parents=True,exist_ok=True)
    ar=pilot.save_npz(a.arrays/'complete-same97-cap-times-true-right-Poisson-Grams.npz',arrays)
    doc.update(complete=True,exact_object_identity=cap['exact_object_identity'],
        complete_same_repaired_centre_definition_sha256=CENTRE,
        original_complete_cap_native_sha256=digest(a.cap),
        original_complete_cap_array_receipt=cap['complete_posterior_array_receipt'],
        original_actual_true97_Poisson_native_sha256=digest(a.poisson),
        original_actual_true97_Poisson_array_receipt=poisson['complete_true97_Gram_array_receipt'],
        complete_same_input_directional_contractions=windows,
        complete_contraction_array_receipt=ar,
        complete_full_cap_high_to_low_bound_proved=True,
        complete_true_right_Poisson_contraction_proved=True,
        original_targets_trials7908cells5970propagators_and_Grams_recomputed=0,
        independent_high_body_and_high_cut_inputs_retained=True,
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--phase',choices=('cap','compose'),required=True)
    for name in ('body','body-process','body-arrays','boundary','boundary-process','boundary-arrays',
        'cap','cap-process','cap-arrays','poisson','poisson-process','poisson-arrays','arrays','out'):
        ap.add_argument('--'+name,type=Path,required=name in ('arrays','out'))
    for name in ('body-run','body-attempt','boundary-run','boundary-attempt',
        'cap-run','cap-attempt','poisson-run','poisson-attempt','consumer-worker-sha','consumer-manifest-sha'):
        ap.add_argument('--'+name)
    a=ap.parse_args();ctx.prec=320;ctx.cap=6;start=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every original cap-posterior result and actual failure')
    if digest(core.__file__)!=CORE or digest(matrix.__file__)!=MATRIX:
        raise ValueError('one exact original signed-Gram arithmetic source changed')
    doc=dict(kind=KIND,phase=a.phase,source_sha256=digest(__file__),repository=PUBLIC,
        arithmetic_bits=320,complete=False,failure=None,gates=[],input_sha256=input_identity(a),
        complete_full_cap_high_to_low_bound_proved=False,
        complete_true_right_Poisson_contraction_proved=False,
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)
    try:
        if a.phase=='cap':cap_run(a,doc)
        else:compose_run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-start;save(a.out,doc)
    print(json.dumps(dict(kind=KIND,phase=a.phase,complete=doc['complete'],
        gates=len(doc['gates']),seconds=doc['seconds'],
        full_cap_high_to97=doc.get('complete_full_cap_high_to97_operator_upper'),
        contractions={k:v['complete_operator_upper'] for k,v in
            doc.get('complete_same_input_directional_contractions',{}).items()},
        complete_infinite_BVP_inverse_proved=False)),flush=True)


if __name__=='__main__':main()
