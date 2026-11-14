#!/usr/bin/env python3
"""Evaluate only64 genuinely missing native points on frozen target germs.

All original7908 whole-target domains,7844 ordinary saved-point residuals,
Taylor64 rows and original1341 trial norms stay immutable. New residuals
are separately identified by their new native-point enclosure.
"""
from __future__ import annotations
import argparse,copy,json,os,time
from pathlib import Path
from fractions import Fraction
from flint import ctx
import fourfold_codazzi_missing_midpoint_Taylor_Hessian as previous
from fourfold_codazzi_full_body_graft_target_jets import ReciprocalFullTargetJets
from fourfold_phase_natural_exterior_graft import NaturalGraft
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_codazzi_known_cut_direction_cap_pilot_v3 import (
    read,sha,positive,rec,exact,rowsha,smaller)

base=previous.base
KIND='actual_missing_native_point_same_w0_Hessian_v1'
TAYLOR_RUN=43633412397
TAYLOR_NATIVE='f85bddc8c1ac7e30a6790818fb52596c88e193fff9312cd4f2bfe20b07549759'
TAYLOR_SOURCE='ebaa3caaca274b36e816dc4c1797cf7367a3ce06d5eb1d8778879e24c0349c3e'
TAYLOR_WORKER='5ea4af7652c92b89b7570fde1a9a187ff24be1a37a6fdd357ddc45efccac9963'
TAYLOR_MANIFEST='890c5f9d9c5251ddf7d545b4c373fd96d35dfca5782b9137651374be367a14fd'
OBJECT='91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848'
TARGET_SOURCE='0a7b76a9820a9670ad40bbeb50e49d2e9a3f3a65e0e2d8f81ee361babba85d95'
INPUTS=previous.INPUTS+('actual-taylor','actual-taylor-process','object')
NAMES=('gamma','beta','K','s')
save=base.save
gate=base.gate


def inputs(a):
    out=previous.inputs(a)
    out.update({key:sha(getattr(a,key.replace('-','_')))
                for key in ('actual-taylor','actual-taylor-process','object')})
    return out


def taylor_input(a,doc):
    d,p=read(a.actual_taylor),read(a.actual_taylor_process)
    gate(doc,'actual_complete_Taylor64_native_and_original_successful_artifact_receipt',
        sha(a.actual_taylor)==TAYLOR_NATIVE
        and d.get('kind')==previous.KIND and base.prior.proved(d)
        and d.get('source_sha256')==TAYLOR_SOURCE
        and d.get('input_sha256')==previous.inputs(a)
        and len(d.get('rows',[]))==1341 and len(d.get('derived_midpoint_cells',[]))==64
        and len(d.get('new_missing_residual_rows',[]))==64
        and d.get('original_completed_residual_domains_reused')==7844
        and d.get('new_target_evaluations')==0
        and d.get('original7844_completed_residuals_recomputed')==0
        and len(d.get('changed_local_indices',[]))==16
        and d.get('complete_actual_trial_intersections')==1977
        and p.get('repository')==base.PUBLIC and str(p.get('run_id'))==str(TAYLOR_RUN)
        and p.get('complete') and not p.get('failure')
        and p.get('worker_source_sha256')==TAYLOR_WORKER
        and p.get('input_manifest_sha256')==TAYLOR_MANIFEST
        and p.get('complete_native_sha256')==TAYLOR_NATIVE
        and p.get('children') and all(c.get('actual_returncode')==0 for c in p['children'])
        and sha(Path(previous.__file__))==TAYLOR_SOURCE)
    return d


def native_point(cell,derived,target,nu):
    left,right=map(Fraction,cell['interval']);point=(left+right)/2
    original_germ=tuple(map(Fraction,cell['actual_scalar_germ']))
    if not original_germ[0]<=left<point<right<=original_germ[1]:
        raise ValueError('the point must lie inside the same original closed scalar germ')
    if point>3 and target._graft is None:
        # This positive-width enclosure includes fixed eta0; it is not
        # relabelled as an original zero-width graft evaluation.
        target._graft=NaturalGraft(target.object_path,Fraction(1,10**9),Fraction(1,8))
    values,germ=target.coefficients(point,point,nu)
    if tuple(germ)!=original_germ:
        raise ValueError('the native point selected a different actual scalar germ')
    prior_jets=derived['intrinsic_midpoint_jets'];whole=cell['all_original_target_coefficients']
    refined={}
    for name in NAMES:
        for order in range(3):
            key=name+('' if order==0 else str(order))
            value=values[key].intersection(box_from_record(whole[key]))
            value=value.intersection(box_from_record(prior_jets[key]))
            if not value.is_finite():
                raise ValueError('native point, original whole and certified Taylor enclosures disagree')
            refined[key]=rec(value)
        # The actual residual uses the original whole third derivative.
        refined[name+'3']=whole[name+'3']
    receipt=dict(request=cell['request'],exact_midpoint=str(point),
        exact_native_point_domain=[str(point),str(point)],
        actual_scalar_germ=list(map(str,germ)),
        original_quarter_row_sha256=rowsha(cell),
        original_whole_coefficients_sha256=rowsha(whole),
        successful_Taylor_derived_cell_sha256=rowsha(derived),
        successful_Taylor_midpoint_jets_sha256=rowsha(prior_jets),
        exact_target_object_sha256=OBJECT,target_source_sha256=TARGET_SOURCE,
        actual_nu=str(nu),exact_affine_offset='0',
        actual_native_point_parameter_half_width='1/1000000000' if point>3 else '0',
        native_parameter_enclosure_contains_same_fixed_eta0=True,
        actual_full_native_point_coefficients={k:rec(v) for k,v in values.items()},
        refined_midpoint_jets_sha256=rowsha(refined),
        original_whole_target_not_recomputed=True,original_Taylor_point_not_recomputed=True,
        full_original_mean_and_primitive_tail_retained=True)
    out=copy.deepcopy(cell)
    out['intrinsic_midpoint_jets']=refined
    out['native_point_receipt']=receipt
    return out,receipt


def run(a,doc):
    local,background,particular,ordinary,split,table,groups,wanted,data,knots,alpha=base.validate(a,doc)
    old=previous.original_hessian(a,doc);taylor=taylor_input(a,doc)
    missing=previous.target_domain_checks(table,doc)
    original_results={tuple(r['request']):r for r in old['new_quarter_residual_rows']}
    derived={tuple(c['request']):c for c in taylor['derived_midpoint_cells']}
    taylor_results={tuple(r['request']):r for r in taylor['new_missing_residual_rows']}
    metadata=json.loads(str(data['metadata']));nu=Fraction(metadata['exact_float_nu'])
    plan=read(a.quarter_plan)
    gate(doc,'same_exact_intrinsic_object_nu_and_only64_genuinely_missing_native_points',
        sorted(original_results)==wanted and len(original_results)==7844
        and sorted(derived)==missing and sorted(taylor_results)==missing
        and sha(a.object)==OBJECT==plan['input_sha256']['object']
        and sha(Path(__file__).with_name('fourfold_codazzi_full_body_graft_target_jets.py'))==TARGET_SOURCE
        and all(rowsha(table[key])==derived[key]['midpoint_derivation_receipt']['original_quarter_row_sha256']
            and rowsha(table[key])==taylor_results[key]['quarter_row_sha256'] for key in missing)
        and all(not table[key].get('intrinsic_midpoint_jets') for key in missing))
    # Preserve the complete successful Taylor certificate as an independent
    # fallback and preserve each unchanged original local row byte-for-byte.
    gains={k:positive(v) for k,v in local['original_closed_physical_Green_gains'].items()}
    resolvent=positive(local['original_complete_bridge_resolvent'])
    doc.update(original_complete_cached_Hessian_native_sha256=previous.OLD_NATIVE,
        original_complete_Taylor_native_sha256=TAYLOR_NATIVE,
        actual_original_fallback_budget_diagnostic=taylor['actual_fallback_budget_diagnostic'],
        original_completed_residual_domains_reused=7844,
        original_Taylor_residual_domains_preserved=64,
        new_native_point_cells=[],native_point_receipts=[],new_point_residual_rows=[],updated_local_rows=[],
        new_native_point_evaluations_in_this_child=0,new_residual_domains_executed_in_this_child=0,
        new_local_rows_executed_in_this_child=0,new_whole_target_domains_evaluated=0,
        original7908_whole_target_domains_recomputed=0,original7844_residuals_recomputed=0,
        original_Taylor64_enclosures_recomputed=0)
    resumed=None
    if a.resume:
        resumed=read(a.resume)
        if (resumed.get('kind')!=KIND or resumed.get('source_sha256')!=sha(__file__)
            or resumed.get('input_sha256')!=doc['input_sha256']):
            raise ValueError('only the exact native-point source and complete inputs may resume')
        doc['original_resume_native_sha256']=sha(a.resume)
        doc['original_resume_failure_retained']=resumed.get('failure')
    save(a.out,doc)
    new_table=dict(table)
    if resumed:
        saved=resumed.get('new_native_point_cells',[])
        if len(saved)>64:raise ValueError('a native point prefix exceeds64')
        for key,cell in zip(missing,saved):
            receipt=cell.get('native_point_receipt',{})
            if (tuple(cell.get('request',[]))!=key
                or receipt.get('original_quarter_row_sha256')!=rowsha(table[key])
                or receipt.get('successful_Taylor_derived_cell_sha256')!=rowsha(derived[key])
                or receipt.get('refined_midpoint_jets_sha256')!=rowsha(cell.get('intrinsic_midpoint_jets'))
                or receipt.get('original_whole_coefficients_sha256')!=rowsha(cell.get('all_original_target_coefficients'))
                or rowsha(cell.get('all_original_target_coefficients'))!=rowsha(table[key]['all_original_target_coefficients'])
                or receipt.get('actual_nu')!=str(nu) or receipt.get('exact_target_object_sha256')!=OBJECT
                or receipt.get('target_source_sha256')!=TARGET_SOURCE):
                raise ValueError('a previously completed native point identity changed')
            new_table[key]=cell
        doc['new_native_point_cells']=saved
        doc['native_point_receipts']=[c['native_point_receipt'] for c in saved]
        doc['completed_native_points_reused_without_target_calls']=len(saved)
    target=None
    for key in missing[len(doc['new_native_point_cells']):]:
        if target is None:target=ReciprocalFullTargetJets(a.object,Fraction(0),512)
        tick=time.monotonic();cell,receipt=native_point(table[key],derived[key],target,nu)
        receipt['actual_point_seconds']=time.monotonic()-tick
        new_table[key]=cell;doc['new_native_point_cells'].append(cell)
        doc['native_point_receipts'].append(receipt);doc['new_native_point_evaluations_in_this_child']+=1
        save(a.out,doc)
        print(json.dumps(dict(actual_native_points=len(doc['new_native_point_cells']),
            request=list(key),new_whole_target_domains=0,old_target_domains_recomputed=0)),flush=True)
    gate(doc,'all64_new_native_points_preserve_original_whole_germs_and_Taylor_intersections',
        len(doc['new_native_point_cells'])==64
        and all(rowsha(c['all_original_target_coefficients'])==rowsha(table[tuple(c['request'])]['all_original_target_coefficients'])
            and c['native_point_receipt']['native_parameter_enclosure_contains_same_fixed_eta0']
            for c in doc['new_native_point_cells']))
    if resumed:
        saved=resumed.get('new_point_residual_rows',[])
        if len(saved)>64:raise ValueError('a point residual prefix exceeds64')
        for key,row in zip(missing,saved):
            if (tuple(row.get('request',[]))!=key or row.get('quarter_row_sha256')!=rowsha(table[key])
                or row.get('native_point_quarter_row_sha256')!=rowsha(new_table[key])
                or row.get('native_point_receipt_sha256')!=rowsha(new_table[key]['native_point_receipt'])
                or row.get('original_Taylor_residual_row_sha256')!=rowsha(taylor_results[key])
                or not row.get('original_whole_jets_and_new_native_point_used')):
                raise ValueError('a completed new native-point residual changed')
        doc['new_point_residual_rows']=saved
        doc['completed_new_residual_prefix_reused_without_execution']=len(saved)
    fft=base.DirectedFFT()
    for key in missing[len(doc['new_point_residual_rows']):]:
        tick=time.monotonic();cell=new_table[key]
        row=base.residual_from_saved_cell(cell,data,knots,alpha,fft)
        row.update(quarter_row_sha256=rowsha(table[key]),native_point_quarter_row_sha256=rowsha(cell),
            native_point_receipt_sha256=rowsha(cell['native_point_receipt']),
            original_Taylor_residual_row_sha256=rowsha(taylor_results[key]),
            exact_scalar_midpoint_and_whole_jets_reused=False,
            original_whole_jets_and_new_native_point_used=True,
            actual_seconds=time.monotonic()-tick)
        doc['new_point_residual_rows'].append(row);doc['new_residual_domains_executed_in_this_child']+=1
        save(a.out,doc)
    results=dict(original_results)
    results.update({tuple(r['request']):r for r in doc['new_point_residual_rows']})
    changed=list(taylor['changed_local_indices']);rows=list(taylor['rows']);newgroups=copy.deepcopy(groups)
    if len(changed)!=16 or sorted(changed)!=changed:raise ValueError('the original16-row set changed')
    for i in changed:
        if groups[i]['all_target_midpoints_saved']:raise ValueError('an unaffected original row was requested')
        if not all(new_table[tuple(q['request'])].get('intrinsic_midpoint_jets') for q in groups[i]['intersections']):
            raise ValueError('a complete original local row lacks a new native point')
        newgroups[i]['all_target_midpoints_saved']=True
    if resumed:
        saved=resumed.get('updated_local_rows',[])
        if len(saved)>16:raise ValueError('a new local prefix exceeds16')
        for i,row in zip(changed,saved):
            if (row.get('local_source_row')!=i
                or row.get('original_complete_Taylor_local_row_sha256')!=rowsha(taylor['rows'][i])
                or not row.get('complete_target_point_enclosures_from_original_or_new_native')):
                raise ValueError('a completed point-only local Hessian row changed')
            rows[i]=row
        doc['updated_local_rows']=saved
        doc['completed_local_updates_reused_without_execution']=len(saved)
    for i in changed[len(doc['updated_local_rows']):]:
        one_local=dict(local,rows=[local['rows'][i]])
        one_particular=dict(particular,rows=[particular['rows'][i]])
        one_ordinary=dict(ordinary,rows=[ordinary['rows'][i]])
        one_split=dict(split,rows=[split['rows'][i]])
        updated,_=base.hessian_rows(one_local,background,one_particular,one_ordinary,
                                    one_split,[newgroups[i]],results,alpha)
        row=updated[0];row['local_source_row']=i
        row.update(all_target_midpoints_saved=False,
            complete_target_point_enclosures_from_original_or_new_native=True,
            missing_midpoint_uses_original_full_row=False,
            original_complete_Taylor_local_row_sha256=rowsha(taylor['rows'][i]),
            original_whole_target_jets_reused=True)
        rows[i]=row;doc['updated_local_rows'].append(row);doc['new_local_rows_executed_in_this_child']+=1
        save(a.out,doc)
    reused=[i for i in range(1341) if i not in changed]
    gate(doc,'all1325_unaffected_local_rows_reused_exactly_and_all7908_residuals_covered',
        len(reused)==1325 and all(rowsha(rows[i])==rowsha(taylor['rows'][i])==rowsha(old['rows'][i]) for i in reused)
        and sorted(results)==sorted(table) and len(results)==7908)
    gate(doc,'all64_new_point_residuals_keep_full_mean_support_and_uniform_errors',
        len(doc['new_point_residual_rows'])==64
        and all(r.get('complete_angular_support')==96 and r.get('full_even_residual_mean_retained')
                and r.get('new_target_evaluations')==0 for r in doc['new_point_residual_rows']))
    bounds={}
    for name,key in (('original_ordinary','original_ordinary_sources'),('original_split','original_split_sources'),
                    ('tight_ordinary','new_ordinary_sources'),('tight_split','new_split_sources'),
                    ('selected_local','selected_four_sources')):
        norms,bound=base.prior.accumulated(rows,key,gains)
        bounds[name]=dict(source_norms={k:rec(v) for k,v in norms.items()},
            physical_Green_Hessian_source=rec(bound),additive=rec((resolvent*bound).upper()))
    previous_add=positive(taylor['additive_same_w0_actual_moving_cap_error']);chosen=previous_add
    for result in bounds.values():chosen=smaller(chosen,positive(result['additive']))
    gate(doc,'complete_global_four_source_comparison_preserves_Taylor_fallback_and_same_resolvent',
        all(positive(r['additive']).is_finite() for r in bounds.values()) and chosen<=previous_add
        and sum(r['original_trial_subcells'] for r in rows)==1977)
    doc.update(complete=True,rows=rows,changed_local_indices=changed,
        reused_complete_local_row_count=1325,
        original_reused_local_row_receipts=[dict(index=i,sha256=rowsha(taylor['rows'][i])) for i in reused],
        complete_local_rows=1341,complete_actual_trial_intersections=1977,
        complete_cached_target_domains=7908,complete_original_residual_domains=7844,
        complete_new_native_point_domains=64,complete_new_native_point_residual_domains=64,
        complete_residual_domains_available=7908,
        original_candidate_sha256=taylor['original_candidate_sha256'],
        derived_continuous_centre_definition_sha256=taylor['derived_continuous_centre_definition_sha256'],
        direction_sha256=taylor['direction_sha256'],exact_interval=taylor['exact_interval'],
        exact_affine_offset='0',physical_parameter='same fixed physical eta0 and original nu',
        complete_source_decomposition_bounds=bounds,
        original_complete_Hessian_feedback_resolvent=taylor['original_complete_Hessian_feedback_resolvent'],
        multiplier_of_same_w0_complete_physical_cap_error=taylor['multiplier_of_same_w0_complete_physical_cap_error'],
        previous_complete_Taylor_Hessian_additive=taylor['additive_same_w0_actual_moving_cap_error'],
        additive_same_w0_actual_moving_cap_error=rec(chosen),full_independent_even_mean_retained=True,
        original7844_completed_residuals_recomputed=0,original1341_trial_norms_recomputed=0,
        original_Taylor64_residual_rows_preserved_without_recomputation=True,
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
        raise RuntimeError('new mathematics runs only in this public repository Actions')
    if a.out.exists():raise FileExistsError('preserve every actual point-only attempt')
    ctx.prec=320;ctx.cap=6;started=time.monotonic()
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],source_sha256=sha(__file__),
             input_sha256=inputs(a),actual_original_quarter_run=a.quarter_run)
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:
        doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=True,new_native_points=doc['new_native_point_evaluations_in_this_child'],
        new_residuals=doc['new_residual_domains_executed_in_this_child'],
        original7908_whole_targets_recomputed=0,additive=doc['additive_same_w0_actual_moving_cap_error']['upper'])),flush=True)


if __name__=='__main__':main()
