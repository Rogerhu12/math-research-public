#!/usr/bin/env python3
"""Bound the known high source from only the exact Z tail on the repaired M32 centre.

This consumes the forty completed scalar parts, saved exact physical cubics,
the complete centre repair and continuous-Z identities, and the successful
mixed source cover. It executes no target provider, original residual or mean
flow. The low193 equations and actual independent mean remain unchanged.
"""
from __future__ import annotations
import argparse,hashlib,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_candidate_shards import load_candidate
import fourfold_codazzi_complete_response_repair_source as original

sha,read,save,q,interval,record=original.sha,original.read,original.save,original.q,original.interval,original.record
KIND='actual_complete_repaired_M32_known_high_source_from_Z_tail_v1'
OLD_MANIFEST='c214f800a5094c905c554e9053c52567d5ae5d76be41ac2e3fe9d673b396d784'
ORIGINAL='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
TRIAL='ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6'
CENTRE_DEFINITION='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
REPAIR='05e0493dbe55490adec8fb6603e0ec431d1bc03f051aec86be8a78741f60f0a4'
REPAIR_PROCESS='16de872ce106e05b6add99d8406598de3cc87b94f4533a9fc3bb46294c66366a'
REPAIR_SOURCE='6e4e8f1a3f69fdc06c15a0471cedb62abce0740b4825ddf5a0d04de4b984d7ad'
Z_NATIVE='87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88'
Z_DEFINITION='6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04'
MIXED='365f0763d8f4c87182507c4372a3be055624607a77d818a084471b368b33d32e'
MIXED_PROCESS='56c84147351d56b262a17ae0cbf96e18c6525083d72bd51e2f590620dc6e5168'
MIXED_SOURCE='90c90fb1b21806e803e61d5f850b1d8057fcadc577452d3454b05348500a697f'
RIGHT=Fraction(25,8)
PHASE_RIGHT=Fraction(2383968743003,10000000000000)
COMMON=('original-manifest','candidate','response','repair-source','repair-process',
        'direction','mixed','mixed-process')


def rowsha(row):
    return hashlib.sha256((json.dumps(row,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()


def up(value):
    value=interval(value).upper()
    if not value.is_finite() or not value>=0:raise ValueError('a saved nonnegative bound is invalid')
    return value


def gate(doc,name,ok):
    doc['gates'].append(dict(name=name,passed=bool(ok)))
    if not ok:raise ValueError('known high tail source: '+name)


def actual(process,run):
    return (process.get('repository')=='Rogerhu12/math-research-public'
        and str(process.get('run_id'))==str(run) and process.get('complete')
        and not process.get('failure') and process.get('children')
        and all(x.get('actual_returncode')==0 for x in process['children']))


def inputs(a,doc):
    manifest=read(a.original_manifest);repair=read(a.repair_source);rp=read(a.repair_process)
    Z=read(a.direction);mixed=read(a.mixed);mp=read(a.mixed_process)
    identity={name:sha(getattr(a,name.replace('-','_'))) for name in COMMON}
    gate(doc,'exact_original_manifest_cubics_and_two_successful_artifact_receipts',
        identity['original-manifest']==OLD_MANIFEST
        and identity['candidate']==ORIGINAL and identity['response']==TRIAL
        and identity['repair-source']==REPAIR and identity['repair-process']==REPAIR_PROCESS
        and identity['mixed']==MIXED and identity['mixed-process']==MIXED_PROCESS
        and actual(rp,43597921732) and actual(mp,43613560173)
        and rp.get('complete_native_sha256')==REPAIR and mp.get('complete_native_sha256')==MIXED)
    gate(doc,'complete_repaired_M32_centre_and_all_original_source_rows',
        sha(original.__file__)==REPAIR_SOURCE and repair.get('source_sha256')==REPAIR_SOURCE
        and repair.get('complete') and not repair.get('failure')
        and repair.get('complete_common_rows')==7721 and len(repair.get('rows',[]))==7721
        and repair.get('original_candidate_sha256')==ORIGINAL
        and repair.get('derived_continuous_centre_definition_sha256')==CENTRE_DEFINITION
        and repair.get('original_full_physical_response_trial_sha256')==TRIAL
        and repair.get('true_complete_mean_correction_retained')
        and repair.get('gates') and all(x['passed'] for x in repair['gates']))
    gate(doc,'same_complete_continuous_Z_and_global_all193_offset_bounds',
        identity['direction']==Z_NATIVE and Z.get('complete')
        and Z.get('derived_direction_definition_sha256')==Z_DEFINITION
        and Z.get('original_trial_sha256')==TRIAL
        and Z['derived_direction_definition']['exact_interval']==['0','25/8']
        and Z['derived_direction_definition'].get('all193_states_and_mean_retained')
        and len(Z.get('gates',[]))==7 and all(x['passed'] for x in Z['gates']))
    gate(doc,'original_complete_mixed_cover_preserves_all_low_and_mean_equations',
        mixed.get('kind')=='complete7721_mixed_exact_bump_and_raw_mean_continuous_Z_source_cover_v1'
        and mixed.get('source_sha256')==MIXED_SOURCE and mixed.get('complete')
        and not mixed.get('failure') and mixed.get('complete_valid_source_cover')
        and mixed.get('complete_original_common_cells')==7721 and len(mixed.get('rows',[]))==7721
        and mixed.get('derived_continuous_centre_definition_sha256')==CENTRE_DEFINITION
        and mixed.get('exact_continuous_direction_definition_sha256')==Z_DEFINITION
        and mixed.get('true_independent_even_mean_retained')
        and mixed.get('gates') and all(x['passed'] for x in mixed['gates'])
        and all(mixed['common_input_sha256'][k]==identity[k] for k in
            ('original-manifest','candidate','response','repair-source','repair-process','direction')))
    rows=[];parts=[]
    for path in a.parts:
        part=read(path);first,end=part['selected_indices']
        if (part.get('kind')!=manifest['residual_kind'] or part.get('identity')!=manifest['row_identity']
            or not part.get('selected_cells_complete') or part.get('failure')
            or [r['common_row'] for r in part['rows']]!=list(range(first,end))):
            raise ValueError('an exact original scalar part is incomplete or changed')
        rows.extend(part['rows']);parts.append(dict(indices=[first,end],sha256=sha(path)))
    rows.sort(key=lambda r:r['common_row']);parts.sort(key=lambda r:r['indices'])
    gate(doc,'all_forty_original_parts_and7721_rows_match_both_completed_native_receipts',
        len(parts)==40 and len(rows)==7721 and [r['common_row'] for r in rows]==list(range(7721))
        and parts==sorted(repair['original_parts'],key=lambda x:x['indices'])
        and parts==sorted(mixed['original_parts'],key=lambda x:x['indices']))
    edge=Fraction(0)
    for i,row in enumerate(rows):
        lo,hi=map(Fraction,row['interval']);rr=repair['rows'][i];mr=mixed['rows'][i]
        if (lo!=edge or not lo<hi or rr['common_row']!=i or mr['common_row']!=i
            or rr['interval']!=row['interval'] or mr['interval']!=row['interval']
            or rr['original_body_row_sha256']!=rowsha(row) or mr['original_row_sha256']!=rowsha(row)
            or row['full_output_support']!=160 or row['complete_angular_grid']!=512
            or not rr.get('independent_even_mean_included') or not mr.get('true_raw_mean_included')):
            raise ValueError('an original row identity, mean or exact radial edge changed')
        edge=hi
    gate(doc,'complete_closed_scalar_cover_is_exactly_zero_to25over8',edge==RIGHT)
    trial=load_candidate(a.response);centre=load_candidate(a.candidate)
    nodes=[Fraction(float(x)) for x in trial['radial_nodes']]
    meta=json.loads(str(trial['metadata']))
    gate(doc,'exact_physical193_cubics_and_M32_background_with_shared6144_pieces',
        trial['piece_coefficients'].shape==(4,6144,193)
        and centre['piece_coefficients'].shape==(4,6144,65)
        and np.array_equal(trial['radial_nodes'].view(np.uint64),centre['radial_nodes'].view(np.uint64))
        and len(nodes)==6145 and nodes[0]==0 and nodes[-1]==RIGHT
        and meta.get('background_candidate_sha256')==ORIGINAL
        and meta.get('finite_head_mean_was_not_removed_from_the_solve') is True)
    doc.update(common_input_sha256=identity,original_parts=parts,
        candidate_sha256=ORIGINAL,derived_continuous_centre_definition_sha256=CENTRE_DEFINITION,
        original_full_physical_response_trial_sha256=TRIAL,exact_continuous_direction_definition_sha256=Z_DEFINITION,
        exact_affine_parameter_offset='0',physical_parameter='fixed original physical eta0 and original nu',
        coefficient_family_delta='0',background_exact_mode_support=32,
        known_Z_exact_mode_support=96,known_output_mode_support=[97,160],
        complete_source_interval=['0','25/8'],full_low193_and_independent_mean_unchanged=True,
        new_target_provider_calls=0,new_original_residual_evaluations=0,new_mean_flow_evaluations=0,
        new_original_trial_reconstructions=0,
        actual_full_PDE_response_error_proved=False,complete_infinite_inverse_proved=False,
        unknown_high_input_feedback_still_required=True,delta_nonzero_background_transfer_still_required=True)
    context=dict(
        centre_E0=up(repair['exact_centre_repair_bounds']['A0']),
        centre_E1=up(repair['exact_centre_repair_bounds']['angular_A0']),
        Z_E0=up(Z['direction_repair_full_interval_joint_derivative_norms']['1/64'][0]),
        Z_E1=up(Z['direction_repair_full_interval_joint_derivative_norms']['1/64'][1]))
    return rows,repair,mixed,trial,nodes,context


def aggregates(rows,right):
    edge=Fraction(0);sum_new=arb(0);sum_old=arb(0);sum_chosen=arb(0)
    maximum=arb(0);new_maximum=arb(0);improved=0
    for row in rows:
        lo,hi=map(Fraction,row['interval'])
        if lo!=edge or not lo<hi:raise ValueError('the known source aggregate has a radial gap')
        edge=hi
        if lo>=right:continue
        length=q(min(hi,right)-lo)
        new=up(row['tail_high_L2_sup'])
        chosen=up(row['selected_known_high']['L2_sup'])
        old=up(row['original_known_high']['L2_sup'])
        old_rad=up(row['original_known_high']['L2_L2_radial']) if hi<=right else length.sqrt()*old
        selected_rad=(up(row['selected_known_high']['L2_L2_radial'])
                      if hi<=right else length.sqrt()*chosen)
        sum_new=(sum_new+length*new*new).upper()
        sum_old=(sum_old+old_rad*old_rad).upper()
        sum_chosen=(sum_chosen+selected_rad*selected_rad).upper()
        maximum=max(maximum,chosen).upper();new_maximum=max(new_maximum,new).upper()
        improved+=int(new<old)
    if edge!=RIGHT:raise ValueError('an aggregate cannot silently truncate the full7721 cover')
    factor=(q(1+640**2).log()/6).exp().upper()
    return dict(exact_interval=['0',str(right)],new_tail_only_L2_radial=record(sum_new.sqrt().upper()),
        original_known_high_L2_radial=record(sum_old.sqrt().upper()),
        selected_known_high_L2_radial=record(sum_chosen.sqrt().upper()),
        selected_known_high_L2_sup=record(maximum),new_tail_only_L2_sup=record(new_maximum),
        selected_known_high_H_one_third_L2_radial=record((factor*sum_chosen.sqrt()).upper()),
        H_one_third_known_finite_support_factor=record(factor),
        rows_with_strictly_smaller_new_sup=improved,
        fixed_same_background_window_only=True)


def run(a,doc):
    rows,repair,mixed,trial,nodes,c=inputs(a,doc)
    results=[];start_index=0
    if a.resume:
        previous=read(a.resume);saved=previous.get('rows',[])
        gate(doc,'exact_previously_completed_tail_source_rows_are_reused',
            previous.get('kind')==KIND and previous.get('source_sha256')==sha(__file__)
            and previous.get('common_input_sha256')==doc['common_input_sha256']
            and previous.get('original_parts')==doc['original_parts']
            and [r['common_row'] for r in saved]==list(range(len(saved))) and len(saved)<=7721)
        for i,r in enumerate(saved):
            if (r['interval']!=rows[i]['interval'] or r['original_row_sha256']!=rowsha(rows[i])
                or not r.get('actual_tail_source_row_complete')):
                raise ValueError('a completed source prefix row changed')
        results=list(saved);start_index=len(saved)
    doc.update(rows=results,actual_reused_tail_source_rows=start_index,actual_new_tail_source_rows=0,
        exact_global_repair_fees={k:record(v) for k,v in c.items()})
    for i in range(start_index,7721):
        row=rows[i];rr=repair['rows'][i];mr=mixed['rows'][i]
        left,right=map(Fraction,row['interval']);piece=row['pieces']['response']
        if not nodes[piece]<=left<right<=nodes[piece+1]:
            raise ValueError('a tail Bernstein restriction crosses the original exact cubic piece')
        cube=trial['piece_coefficients'][:,piece,:].copy()
        # Odd slots0..95 are j1..96. Slot96 is true even mean.
        # Even slots97..192 are j1..96. Retain exactly both tails j33..96.
        cube[:,:32]=0;cube[:,96:129]=0
        if not np.all(cube[:,96]==0):raise ValueError('the exact projected tail acquired a false mean')
        raw0,raw1,_=original.cubic_pair_norms(cube,nodes[piece],left,right,96)
        H0=(raw0+c['Z_E0']).upper();H1=(raw1+c['Z_E1']).upper()
        Q0=(up(rr['original_background_pair_A0'])+c['centre_E0']).upper()
        Q1=(up(rr['original_background_angular_derivative_pair_A0'])+c['centre_E1']).upper()
        B=abs(interval(row['intrinsic_whole_third_jets']['beta'])).upper()
        Kstar=max(arb(1),abs(interval(row['intrinsic_whole_third_jets']['K'])).upper()).upper()
        drift=(B*Kstar*Q0*Q0*H1/4).upper()
        reaction=(3*B*Kstar*Q0*Q0*H0).upper()
        primitive=(B*Kstar*Q0*Q1*H0/2).upper()
        total=(drift+reaction+primitive).upper()
        old=mr['complete_Z_source']['high97_through160'];length=q(right-left)
        newrad=(length.sqrt()*total).upper()
        chosen=dict(L2_sup=record(min(total,up(old['L2_sup'])).upper()),
            L2_L2_radial=record(min(newrad,up(old['L2_L2_radial'])).upper()))
        results.append(dict(common_row=i,interval=row['interval'],original_row_sha256=rowsha(row),
            original_response_piece=piece,actual_tail_source_row_complete=True,
            full_repaired_background_A0=record(Q0),full_repaired_background_angular_A0=record(Q1),
            raw_tail33_through96_A0=record(raw0),raw_tail33_through96_angular_A0=record(raw1),
            continuous_Z_tail33_through96_A0=record(H0),continuous_Z_tail33_through96_angular_A0=record(H1),
            complete_beta_abs=record(B),complete_Kstar=record(Kstar),
            drift_high_source=record(drift),reaction_high_source=record(reaction),
            primitive_high_source=record(primitive),tail_high_L2_sup=record(total),
            original_known_high=old,selected_known_high=chosen,
            low_and_independent_mean_source_sha256=rowsha({
                'full_through160':mr['complete_Z_source']['full_through160'],
                'low193':mr['complete_Z_source']['low193']})))
        doc['actual_new_tail_source_rows']=len(results)-start_index
        if (i+1)%128==0:
            doc['rows']=results;save(a.out,doc)
            print(json.dumps(dict(actual_known_tail_rows=i+1,new_rows=doc['actual_new_tail_source_rows'])),flush=True)
    gate(doc,'all7721_exact_tail_source_rows_completed_once',
        len(results)==7721 and [r['common_row'] for r in results]==list(range(7721)))
    doc.update(complete=True,rows=results,complete_original_common_rows=7721,
        complete_known_high_bounds=dict(full_body=aggregates(results,RIGHT),
            inner_body=aggregates(results,Fraction(9,10)),
            fixed_negative_phase_window=aggregates(results,PHASE_RIGHT)),
        original_mixed_source_native_sha256=MIXED,
        all_original_low_and_independent_mean_bounds_retained_without_recomputation=True,
        fixed_negative_phase_right_is_not_transferred_to_other_backgrounds=True,
        complete_known_high_source_bound_proved=True)
    save(a.out,doc)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in (*COMMON,'out'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--parts',nargs='+',type=Path,required=True)
    p.add_argument('--resume',type=Path)
    a=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual known-high source outcome')
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],rows=[],source_sha256=sha(__file__))
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=True,rows=7721,new_rows=doc['actual_new_tail_source_rows'],
        bounds=doc['complete_known_high_bounds'],seconds=doc['seconds'])),flush=True)


if __name__=='__main__':main()
