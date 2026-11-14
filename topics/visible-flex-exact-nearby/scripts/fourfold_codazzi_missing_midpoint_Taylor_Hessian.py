#!/usr/bin/env python3
"""Diagnose actual fallback budgets, then translate only missing same-germ points.

No target evaluator is called. Every original7844 residual and every
unaffected complete local Hessian row is reused from the actual successful
native. The full old data remain immutable.
"""
from __future__ import annotations
import argparse,copy,json,os,shutil,time
from pathlib import Path
from fractions import Fraction
from flint import arb,ctx
import fourfold_codazzi_cached_quarter_centre_Hessian_v2 as base
from fourfold_codazzi_cached_same_germ_midpoint_translation import fill_missing
from fourfold_codazzi_known_cut_direction_cap_pilot_v3 import (
    read,sha,positive,rec,exact,rowsha,smaller)

KIND='actual_missing_cached_midpoint_Taylor_same_w0_Hessian_v1'
OLD_RUN=43628443697
OLD_NATIVE='8d652d2515359e3ad1bf91c8ad03fbf66a646ddf0b6bdef1f0aa20d2adcbf12c'
OLD_PROCESS='cd7fdccd2e87f0099b9bde6a82774cc2ddc827ea52b8b06f9664b1514721d5e8'
OLD_SOURCE='dfcc4dabe42638ba1ebd2af2b8a51cccd85dfb7f63738bbbae1b6fe38d3f28c7'
OLD_WORKER='b5029d5d69085114cef9219007488f1780e53e9d5ad73f44c3a0d88500ed9d64'
OLD_MANIFEST='47ff50fc768a24269ea7dab3de284581fdf8be1abd04fb867d4a55be78b1368d'
HELPER='356c8c09ff9014e56e7d0e53521552d6f3d66c96801478c66735790791cef850'
INPUTS=base.INPUTS+('previous-hessian','previous-process')
CHANNELS=base.CHANNELS
save=base.save
gate=base.gate


def inputs(a):
    result=base.inputs(a)
    result.update({'previous-hessian':sha(a.previous_hessian),'previous-process':sha(a.previous_process)})
    return result


def norm_group(rows,gains,resolvent):
    norms,bound=base.prior.accumulated(rows,'selected_four_sources',gains)
    return dict(source_norms={key:rec(value) for key,value in norms.items()},
                physical_Green_Hessian_source=rec(bound),additive=rec((resolvent*bound).upper()))


def original_hessian(a,doc):
    old,p=read(a.previous_hessian),read(a.previous_process)
    gate(doc,'exact_actual_complete_cached_Hessian_and_its_artifact_process',
        sha(a.previous_hessian)==OLD_NATIVE and sha(a.previous_process)==OLD_PROCESS
        and p.get('repository')==base.PUBLIC and str(p.get('run_id'))==str(OLD_RUN)
        and p.get('complete') and not p.get('failure')
        and p.get('worker_source_sha256')==OLD_WORKER
        and p.get('input_manifest_sha256')==OLD_MANIFEST
        and p.get('complete_native_sha256')==OLD_NATIVE
        and p.get('children') and all(c.get('actual_returncode')==0 for c in p['children'])
        and old.get('kind')==base.KIND and base.prior.proved(old)
        and old.get('source_sha256')==OLD_SOURCE
        and old.get('complete_local_rows')==1341 and len(old.get('rows',[]))==1341
        and old.get('complete_actual_trial_intersections')==1977
        and old.get('complete_new_residual_domains')==7844
        and len(old.get('new_quarter_residual_rows',[]))==7844
        and old.get('original_local_rows_retained_for_missing_midpoints')==16
        and old.get('original_target_evaluations_executed')==0
        and old.get('input_sha256')==base.inputs(a)
        and sha(Path(base.__file__))==OLD_SOURCE
        and sha(Path(__file__).with_name('fourfold_codazzi_cached_same_germ_midpoint_translation.py'))==HELPER)
    return old


def diagnose(local,old,doc):
    gains={key:positive(value) for key,value in local['original_closed_physical_Green_gains'].items()}
    resolvent=positive(local['original_complete_bridge_resolvent'])
    missing=[row for row in old['rows'] if row['missing_midpoint_uses_original_full_row']]
    others=[row for row in old['rows'] if not row['missing_midpoint_uses_original_full_row']]
    gate(doc,'exact_original_sixteen_missing_point_rows_and_complement_partition',
        len(missing)==16 and len(others)==1325
        and sorted(row['local_source_row'] for row in missing+others)==list(range(1341)))
    data=dict(missing_local_indices=[row['local_source_row'] for row in missing],
              missing_group=norm_group(missing,gains,resolvent),
              unchanged_group=norm_group(others,gains,resolvent),
              all_selected=norm_group(old['rows'],gains,resolvent),
              old_complete_additive=old['additive_same_w0_actual_moving_cap_error'],
              diagnostic_is_for_certified_numerical_majorants_not_actual_defect_lower_bounds=True)
    # rec uses lower/upper strings; use the same explicit interval reader
    # as the native arithmetic, never float or a midpoint for the decision.
    from fourfold_codazzi_rotational_cap_jacobi import box_from_record
    miss=box_from_record(data['missing_group']['additive'])
    total=box_from_record(data['all_selected']['additive'])
    ratio=miss/total
    requested=miss.lower()>=total.upper()/2
    data.update(missing_fraction_of_selected_budget=rec(ratio),
                threshold='1/2',refinement_requested=bool(requested))
    doc['actual_fallback_budget_diagnostic']=data
    return gains,resolvent,requested


def target_domain_checks(table,doc):
    missing=[]
    for key,cell in sorted(table.items()):
        if cell.get('exact_affine_parameter_offset')!='0' or cell.get('new_parameter_half_width')!='0':
            raise ValueError('an original quarter is not at the same fixed physical eta0')
        half=Fraction(cell.get('intrinsic_target_enclosure_half_width',cell['new_parameter_half_width']))
        if half not in (Fraction(0),Fraction(1,1000000000)):
            raise ValueError('an undeclared original parameter enclosure was substituted')
        if half and not cell.get('intrinsic_target_enclosure_contains_fixed_eta0'):
            raise ValueError('a positive-width original target does not certify fixed eta0')
        if not cell.get('intrinsic_midpoint_jets'):missing.append(key)
    gate(doc,'every_original_parameter_enclosure_contains_same_fixed_eta0',
         len(missing)==64 and len(table)==7908)
    return missing


def run(a,doc):
    local,background,particular,ordinary,split,table,groups,wanted,data,knots,alpha=base.validate(a,doc)
    old=original_hessian(a,doc)
    old_results={tuple(row['request']):row for row in old['new_quarter_residual_rows']}
    gate(doc,'all7844_actual_residuals_are_same_original_quarter_rows',
        sorted(old_results)==wanted and len(old_results)==7844
        and all(row['quarter_row_sha256']==rowsha(table[key])
            and row.get('exact_scalar_midpoint_and_whole_jets_reused')
            and row.get('new_target_evaluations')==0 and row.get('full_even_residual_mean_retained')
            for key,row in old_results.items())
        and all(old['rows'][i]['original_local_row_sha256']==rowsha(row)
            for i,row in enumerate(local['rows'])))
    gains,resolvent,requested=diagnose(local,old,doc)
    original_missing=target_domain_checks(table,doc)
    doc.update(original_complete_cached_Hessian_native_sha256=OLD_NATIVE,
        original_completed_residual_domains_reused=7844,original_target_evaluations_executed=0,
        original_physical_cap_residual_domains_recomputed=0,new_target_evaluations=0,
        new_residual_domains_executed_in_this_child=0,new_missing_residual_rows=[],
        derived_midpoint_cells=[],midpoint_derivation_receipts=[],unavailable_midpoints=[],
        updated_local_rows=[],new_local_rows_executed_in_this_child=0)
    previous=None
    if a.resume:
        previous=read(a.resume)
        if (previous.get('kind')!=KIND or previous.get('source_sha256')!=sha(__file__)
            or previous.get('input_sha256')!=doc['input_sha256']
            or previous.get('actual_fallback_budget_diagnostic',{}).get('refinement_requested')!=requested):
            raise ValueError('only the exact same actual fallback/pinned source prefix may resume')
        doc['original_resume_native_sha256']=sha(a.resume)
        doc['original_resume_failure_retained']=previous.get('failure')
    # Commit the actual small diagnostic before deriving a single new point.
    save(a.out,doc)
    print(json.dumps(dict(actual_fallback_budget_diagnostic=doc['actual_fallback_budget_diagnostic'],
                          original_target_evaluations=0)),flush=True)
    rows=list(old['rows']);new_table=table;results=dict(old_results);changed=[]
    if requested:
        if previous and previous.get('midpoint_derivation_complete'):
            new_table=dict(table)
            for cell in previous['derived_midpoint_cells']:
                key=tuple(cell['request']);receipt=cell.get('midpoint_derivation_receipt',{})
                if (key not in original_missing or receipt.get('original_quarter_row_sha256')!=rowsha(table[key])
                    or receipt.get('derived_midpoint_jets_sha256')!=rowsha(cell['intrinsic_midpoint_jets'])):
                    raise ValueError('an exact completed derived point prefix changed')
                new_table[key]=cell
            doc['derived_midpoint_cells']=previous['derived_midpoint_cells']
            doc['midpoint_derivation_receipts']=previous['midpoint_derivation_receipts']
            doc['unavailable_midpoints']=previous['unavailable_midpoints']
            doc['derived_midpoints_reused_without_new_Taylor_arithmetic']=len(doc['derived_midpoint_cells'])
        else:
            new_table,receipts,unavailable=fill_missing(table)
            doc['derived_midpoint_cells']=[new_table[key] for key in original_missing if new_table[key] is not table[key]]
            doc['midpoint_derivation_receipts']=receipts;doc['unavailable_midpoints']=unavailable
            doc['derived_midpoints_reused_without_new_Taylor_arithmetic']=0
        doc['midpoint_derivation_complete']=True
        save(a.out,doc)
        newgroups=copy.deepcopy(groups)
        for i,group in enumerate(groups):
            if group['all_target_midpoints_saved']:continue
            eligible=all(new_table[tuple(q['request'])].get('intrinsic_midpoint_jets') for q in group['intersections'])
            if eligible:
                # This flag is only the old formula's internal dispatch.
                # Actual output below explicitly labels derived point data.
                newgroups[i]['all_target_midpoints_saved']=True;changed.append(i)
        requests=sorted({tuple(q['request']) for i in changed for q in newgroups[i]['intersections']}
                        -set(old_results))
        gate(doc,'only_original_missing_sixtyfour_domains_can_be_new_residual_requests',
             len(requests)<=64 and set(requests)<=set(original_missing)
             and all(key in new_table and new_table[key].get('midpoint_derivation_receipt') for key in requests))
        if previous:
            saved=previous.get('new_missing_residual_rows',[])
            if len(saved)>len(requests):raise ValueError('a new residual prefix exceeds the actual missing request')
            for key,row in zip(requests,saved):
                cell=new_table[key]
                if (tuple(row['request'])!=key or row['quarter_row_sha256']!=rowsha(table[key])
                    or row.get('derived_point_quarter_row_sha256')!=rowsha(cell)
                    or row.get('midpoint_derivation_receipt_sha256')!=rowsha(cell['midpoint_derivation_receipt'])
                    or row.get('exact_scalar_midpoint_and_whole_jets_reused') is not False
                    or not row.get('exact_original_whole_jets_and_validated_derived_midpoint_used')):
                    raise ValueError('a completed missing-point residual prefix changed')
            doc['new_missing_residual_rows']=saved
            doc['new_residual_prefix_reused_without_execution']=len(saved)
        fft=base.DirectedFFT()
        for key in requests[len(doc['new_missing_residual_rows']):]:
            tick=time.monotonic();cell=new_table[key]
            row=base.residual_from_saved_cell(cell,data,knots,alpha,fft)
            row.update(quarter_row_sha256=rowsha(table[key]),
                derived_point_quarter_row_sha256=rowsha(cell),
                midpoint_derivation_receipt_sha256=rowsha(cell['midpoint_derivation_receipt']),
                exact_scalar_midpoint_and_whole_jets_reused=False,
                exact_original_whole_jets_and_validated_derived_midpoint_used=True,
                actual_seconds=time.monotonic()-tick)
            doc['new_missing_residual_rows'].append(row)
            doc['new_residual_domains_executed_in_this_child']+=1
            save(a.out,doc)
            print(json.dumps(dict(request=list(key),actual_new_residuals=len(doc['new_missing_residual_rows']),
                target_calls=0,original7844_residuals_recomputed=0)),flush=True)
        results.update({tuple(row['request']):row for row in doc['new_missing_residual_rows']})
        if previous:
            saved_updates=previous.get('updated_local_rows',[])
            if len(saved_updates)>len(changed):raise ValueError('a saved local update exceeds the actual changed set')
            for i,row in zip(changed,saved_updates):
                if (row.get('local_source_row')!=i
                    or row.get('original_actual_fallback_row_sha256')!=rowsha(old['rows'][i])
                    or row.get('all_target_midpoints_saved') is not False
                    or not row.get('complete_target_point_enclosures_from_original_or_Taylor')):
                    raise ValueError('a completed same-input Taylor local update changed')
                rows[i]=row
            doc['updated_local_rows']=saved_updates
            doc['completed_local_updates_reused_without_execution']=len(saved_updates)
        for i in changed[len(doc['updated_local_rows']):]:
            one_local=dict(local,rows=[local['rows'][i]])
            one_particular=dict(particular,rows=[particular['rows'][i]])
            one_ordinary=dict(ordinary,rows=[ordinary['rows'][i]])
            one_split=dict(split,rows=[split['rows'][i]])
            updated,_=base.hessian_rows(one_local,background,one_particular,one_ordinary,
                                        one_split,[newgroups[i]],results,alpha)
            row=updated[0];row['local_source_row']=i
            row.update(all_target_midpoints_saved=False,
                complete_target_point_enclosures_from_original_or_Taylor=True,
                missing_midpoint_uses_original_full_row=False,
                original_actual_fallback_row_sha256=rowsha(old['rows'][i]),
                exact_same_whole_target_jets_no_new_target=True)
            rows[i]=row
            doc['updated_local_rows'].append(row);doc['new_local_rows_executed_in_this_child']+=1
            save(a.out,doc)
    else:
        doc['midpoint_derivation_complete']=False
        doc['refinement_skipped_because_actual_fallback_budget_not_dominant']=True
    reused=[i for i in range(1341) if i not in changed]
    gate(doc,'every_unaffected_complete_local_row_is_reused_exactly',
         all(rowsha(rows[i])==rowsha(old['rows'][i]) for i in reused)
         and len(rows)==1341 and set(changed)<=set(doc['actual_fallback_budget_diagnostic']['missing_local_indices']))
    gate(doc,'every_new_point_residual_keeps_original_mean_support_and_uniform_errors',
         len(doc['new_missing_residual_rows'])<=64
         and all(row.get('complete_angular_support')==96 and row.get('full_even_residual_mean_retained')
             and row.get('new_target_evaluations')==0 for row in doc['new_missing_residual_rows']))
    all_bounds={}
    if changed:
        for name,key in (('original_ordinary','original_ordinary_sources'),('original_split','original_split_sources'),
                        ('tight_ordinary','new_ordinary_sources'),('tight_split','new_split_sources'),
                        ('selected_local','selected_four_sources')):
            norms,bound=base.prior.accumulated(rows,key,gains)
            all_bounds[name]=dict(source_norms={k:rec(v) for k,v in norms.items()},
                physical_Green_Hessian_source=rec(bound),additive=rec((resolvent*bound).upper()))
    else:all_bounds=old['complete_source_decomposition_bounds']
    oldadd=positive(old['additive_same_w0_actual_moving_cap_error']);chosen=oldadd
    for result in all_bounds.values():chosen=smaller(chosen,positive(result['additive']))
    gate(doc,'complete_four_source_global_comparison_retains_original_resolvent_and_trial_cover',
         all(positive(result['additive']).is_finite() for result in all_bounds.values())
         and chosen<=oldadd and sum(row['original_trial_subcells'] for row in rows)==1977)
    doc.update(complete=True,rows=rows,changed_local_indices=changed,
        reused_complete_local_row_count=len(reused),
        original_reused_local_row_receipts=[dict(index=i,sha256=rowsha(old['rows'][i])) for i in reused],
        complete_local_rows=1341,complete_actual_trial_intersections=1977,
        complete_cached_target_domains=7908,complete_original_residual_domains=7844,
        complete_new_missing_point_residual_domains=len(doc['new_missing_residual_rows']),
        new_Taylor_midpoint_derivations_executed=len(doc['derived_midpoint_cells'])-doc.get('derived_midpoints_reused_without_new_Taylor_arithmetic',0),
        complete_residual_domains_available=7844+len(doc['new_missing_residual_rows']),
        original_local_rows_retained_for_missing_midpoints=16-len(changed),
        original_candidate_sha256=old['original_candidate_sha256'],
        derived_continuous_centre_definition_sha256=old['derived_continuous_centre_definition_sha256'],
        direction_sha256=old['direction_sha256'],exact_interval=old['exact_interval'],
        exact_affine_offset='0',physical_parameter='same fixed physical eta0 and original nu',
        complete_source_decomposition_bounds=all_bounds,
        original_complete_Hessian_feedback_resolvent=old['original_complete_Hessian_feedback_resolvent'],
        multiplier_of_same_w0_complete_physical_cap_error=old['multiplier_of_same_w0_complete_physical_cap_error'],
        previous_complete_cached_Hessian_additive=old['additive_same_w0_actual_moving_cap_error'],
        additive_same_w0_actual_moving_cap_error=rec(chosen),
        full_independent_even_mean_retained=True,
        original7844_completed_residuals_recomputed=0,original1341_trial_norms_recomputed=0,
        original_complete_Hessian_operator_or_unknown_error_norm_improved=False,
        remaining_Z_minus_w0_still_uses_original_complete_moving_error_operator=True,
        all_original_physical_fourteen_fees_and_six_boundary_errors_unchanged=True,
        complete_true_cut_source_claimed=False,complete_finite193_response_error_proved=False,
        complete_infinite_BVP_inverse_proved=False,actual_full_PDE_response_error_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in INPUTS+('out',):p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--range-natives',type=Path,nargs='+',required=True)
    p.add_argument('--range-processes',type=Path,nargs='+',required=True)
    p.add_argument('--quarter-run',type=int,required=True);p.add_argument('--resume',type=Path)
    a=p.parse_args()
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!=base.PUBLIC:
        raise RuntimeError('new numerical mathematics runs only in this public repository Actions')
    if a.out.exists():raise FileExistsError('preserve every complete or partial Taylor/Hessian outcome')
    ctx.prec=320;ctx.cap=6;started=time.monotonic()
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],source_sha256=sha(__file__),
             input_sha256=inputs(a),actual_original_quarter_run=a.quarter_run)
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:
        doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=True,seconds=doc['seconds'],
        actual_new_missing_residuals=doc['new_residual_domains_executed_in_this_child'],
        original_target_calls=0,additive=doc['additive_same_w0_actual_moving_cap_error']['upper'])),flush=True)


if __name__=='__main__':main()
