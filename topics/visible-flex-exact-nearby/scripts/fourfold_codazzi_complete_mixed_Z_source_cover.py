#!/usr/bin/env python3
"""Complete raw-mean/Z source cover with new exact-bump cells only in its support.

All original scalar jets and all already completed exact-bump pilot cells
are reused. Four disjoint jobs compute only remaining compact-support rows.
The final consumer takes minima of complete valid bounds, keeping mean,
known high output, every original row and all mathematical identities.
"""
from __future__ import annotations
import argparse,hashlib,json,shutil,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
import fourfold_codazzi_exact_bump_continuous_Z_source_pilot as pilot
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_phase_beta_bulk_box import DirectedFFT

sha,read,save,exact,interval,record=pilot.sha,pilot.read,pilot.save,pilot.exact,pilot.interval,pilot.record
rowsha=pilot.sha_row
PILOT='c37a5796a3829dfab1846928041f6a91472dc47f20e02f8a2a4080198b574b1c'
PILOT_SOURCE='2d45c2f100484f5a25fe50ec2d8ea2dcd601b79f1f151d4be116225d3284fcc8'
PILOT_WORKER='1abd553afff8444552ce20e8948f9141da53a0ae3fb2a2632bd86c9008e6840f'
PILOT_MANIFEST='563fc148bf219581259eea090271c37f4760115cc6d09e40c0437a14ee93b7bd'
RANGES=((597,886),(886,1175),(1175,1464),(1464,1753))
NAMES=('full_through160','low193','high97_through160')
NORMS=('L2_sup','L2_L2_radial')
COMMON=('original-manifest','candidate','response','body','body-process',
        'repair-source','repair-process','object','direction','pilot','pilot-process')
PLAN_KIND='complete_valid_raw_mean_continuous_Z_baseline_and_exact_bump_assignments_v1'
RANGE_KIND='actual_disjoint_exact_bump_continuous_Z_source_rows_v1'
FINISH_KIND='complete7721_mixed_exact_bump_and_raw_mean_continuous_Z_source_cover_v1'


def up(value):
    out=interval(value).upper()
    if not out.is_finite() or not out>=0:raise ValueError('a complete source norm is invalid')
    return out


def gate(doc,name,ok):
    doc['gates'].append(dict(name=name,passed=bool(ok)))
    if not ok:raise ValueError('complete mixed Z source failed: '+name)


def check_inputs(a,doc):
    manifest=read(a.original_manifest);body=read(a.body);repair=read(a.repair_source)
    bp=read(a.body_process);rp=read(a.repair_process)
    Z=read(a.direction);oldpilot=read(a.pilot);pp=read(a.pilot_process)
    identity={name:sha(getattr(a,name.replace('-','_'))) for name in COMMON}
    gate(doc,'all_original_inputs_and_successful_complete_mean_and_repair_outcomes',
        sha(pilot.__file__)==PILOT_SOURCE
        and identity['original-manifest']==pilot.OLD_MANIFEST
        and identity['candidate']==pilot.ORIGINAL and identity['response']==pilot.TRIAL
        and identity['body']==pilot.BODY and identity['body-process']==pilot.BODY_PROCESS
        and identity['repair-source']==pilot.REPAIR_SOURCE and identity['repair-process']==pilot.REPAIR_PROCESS
        and identity['object']==manifest['row_identity']['object_sha256']
        and pilot.actual(bp,43586413510) and pilot.actual(rp,43597921732)
        and body.get('complete') and repair.get('complete')
        and body.get('complete_original_common_cells')==7721
        and repair.get('complete_common_rows')==7721
        and body.get('row_identity')==manifest['row_identity'])
    gate(doc,'actual_completed_exact_bump_pilot_is_consumed_without_rerunning_a_cell',
        identity['pilot']==PILOT and pilot.actual(pp,43610523058)
        and pp.get('worker_source_sha256')==PILOT_WORKER
        and pp.get('input_manifest_sha256')==PILOT_MANIFEST
        and pp.get('complete_native_sha256')==PILOT
        and oldpilot.get('source_sha256')==PILOT_SOURCE
        and oldpilot.get('complete') and not oldpilot.get('failure')
        and len(oldpilot.get('gates',[]))==10 and all(x['passed'] for x in oldpilot['gates'])
        and oldpilot.get('new_fixed_eta_target_evaluations_in_this_child')==0
        and oldpilot.get('continuous_Z_full_mean_retained')
        and oldpilot.get('complete_continuous_direction_definition_sha256')==pilot.Z_DEFINITION)
    gate(doc,'same_full_continuous_Z_definition_and_global_angular_offset_fees',
        identity['direction']==pilot.Z_NATIVE and Z.get('complete')
        and Z.get('derived_direction_definition_sha256')==pilot.Z_DEFINITION
        and Z.get('original_trial_sha256')==pilot.TRIAL
        and Z['derived_direction_definition']['exact_interval']==['0','25/8']
        and Z['derived_direction_definition'].get('all193_states_and_mean_retained')
        and len(Z.get('gates',[]))==7 and all(x['passed'] for x in Z['gates']))
    rows=[];parts=[]
    for path in a.parts:
        p=read(path);first,end=p['selected_indices']
        if (p.get('identity')!=manifest['row_identity'] or p.get('kind')!=manifest['residual_kind']
            or not p.get('selected_cells_complete') or p.get('failure')
            or [r['common_row'] for r in p['rows']]!=list(range(first,end))):
            raise ValueError('an original complete cached scalar row part changed')
        rows.extend(p['rows']);parts.append(dict(indices=[first,end],sha256=sha(path)))
    rows.sort(key=lambda r:r['common_row']);parts.sort(key=lambda p:p['indices'])
    gate(doc,'all_original_forty_parts_and7721_rows_match_three_successful_native_receipts',
        len(parts)==40 and len(rows)==7721 and [r['common_row'] for r in rows]==list(range(7721))
        and sorted(p['sha256'] for p in parts)==sorted(body['inputs'].values())
        and parts==sorted(repair['original_parts'],key=lambda p:p['indices'])
        and parts==sorted(oldpilot['all_original_parts'],key=lambda p:p['indices']))
    edge=Fraction(0)
    for i,r in enumerate(rows):
        lo,hi=map(Fraction,r['interval'])
        rr=repair['rows'][i];br=body['residual_rows'][i]
        if (r['common_row']!=i or lo!=edge or not lo<hi
            or rr['interval']!=r['interval'] or br['interval']!=r['interval']
            or rr['common_row']!=i or br['common_row']!=i
            or r['full_output_support']!=160 or r['complete_angular_grid']!=512
            or not rr.get('independent_even_mean_included')
            or rr.get('new_repaired_response_mean_residual_set_to_zero') is not False
            or not interval(r['response_mean_residual']).is_finite()):
            raise ValueError('a true raw mean, complete source row or original interval was lost')
        edge=hi
    gate(doc,'all7721_closed_rows_preserve_true_raw_mean_and_cover_the_exact_full_body',edge==Fraction(25,8))
    context=dict(grid=512,fft=DirectedFFT(),
        Z_offset_A0=up(Z['direction_repair_full_interval_joint_derivative_norms']['1/64'][0]),
        Z_offset_angle_A0=up(Z['direction_repair_full_interval_joint_derivative_norms']['1/64'][1]))
    completed={x['common_row']:x for x in oldpilot['rows']}
    if sorted(completed)!=oldpilot['selected_original_rows']:
        raise ValueError('the exact completed pilot row set changed')
    for i,p in completed.items():
        if (not p.get('actual_projection_complete') or p['cached_scalar_row_sha256']!=rowsha(rows[i])
            or p['interval']!=rows[i]['interval']):
            raise ValueError('an already completed exact-bump cell differs')
    required=[i for i,r in enumerate(rows) if Fraction(r['interval'][0])<pilot.CONTROL_RIGHT
        and Fraction(r['interval'][1])>pilot.CONTROL_LEFT]
    gate(doc,'exact_compact_support_coverage_and_four_fixed_disjoint_assignments',
        required==list(range(597,1753))
        and [i for lo,hi in RANGES for i in range(lo,hi)]==required)
    doc.update(common_input_sha256=identity,original_parts=parts,
        candidate_sha256=pilot.ORIGINAL,derived_continuous_centre_definition_sha256=
            '440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47',
        original_full_physical_response_trial_sha256=pilot.TRIAL,
        exact_continuous_direction_definition_sha256=pilot.Z_DEFINITION,
        exact_affine_parameter_offset='0',physical_parameter='fixed original physical eta0 and nu',
        new_target_provider_calls=0,old_original_target_mean_or_trial_reconstructions_executed=0,
        original_exact_bump_pilot_rows_reused=sorted(completed),
        whole_complete_source_interval=['0','25/8'],new_compact_source_interval=['1/20','9/50'],
        true_independent_even_mean_retained=True,unknown_high_input_feedback_still_required=True,
        actual_full_PDE_response_error_proved=False,complete_infinite_inverse_proved=False)
    return manifest,body,repair,rows,context,completed,required


def choose(candidates):
    """Take componentwise minima only between independently valid scalar bounds."""
    out={};origins={}
    for name in NAMES:
        out[name]={};origins[name]={}
        for norm in NORMS:
            index=min(range(len(candidates)),key=lambda i:up(candidates[i][1][name][norm]))
            label,data=candidates[index]
            out[name][norm]=record(up(data[name][norm]));origins[name][norm]=label
    return out,origins


def completed_pilot_candidates(row):
    ans=[('original_completed_exact_bump_whole_eta',row['exact_bump_cached_complete_eta']['continuous_Z_complete_residual'])]
    for child in row['reused_fixed_eta_refinements']:
        ans.append(('original_completed_exact_bump_fixed_eta_subdivision_'+str(child['subdivisions']),
            child['continuous_Z_complete_residual']))
    return ans


def baseline(row,rr,context):
    length=exact(Fraction(row['interval'][1])-Fraction(row['interval'][0]))
    source=row['uncorrected_response_nonmean'];mean=abs(interval(row['response_mean_residual'])).upper()
    non=up(source['L2_sup']);rad=up(source['L2_L2_radial'])
    whole={k:interval(v) for k,v in row['intrinsic_whole_third_jets'].items()}
    fee,fee_evidence=pilot.complete_Z_repair_fee(rr,whole,context)
    full_sup=((non*non+mean*mean).sqrt()+fee).upper()
    full_rad=((rad*rad+length*mean*mean).sqrt()+length.sqrt()*fee).upper()
    high_sup=(non+fee).upper();high_rad=(rad+length.sqrt()*fee).upper()
    data=dict(full_through160=dict(L2_sup=record(full_sup),L2_L2_radial=record(full_rad)),
        low193=dict(L2_sup=record(full_sup),L2_L2_radial=record(full_rad)),
        high97_through160=dict(L2_sup=record(high_sup),L2_L2_radial=record(high_rad)))
    return data,dict(original_raw_nonmean_L2_sup=source['L2_sup'],
        original_raw_nonmean_L2_L2_radial=source['L2_L2_radial'],
        original_signed_raw_mean_residual=row['response_mean_residual'],
        exact_mean_L2_normalization='normalized circle; actual mean is the orthonormal constant coefficient',
        raw_mean_restored_by_exact_L2_orthogonality=True,complete_Z_transfer=fee_evidence)


def aggregate(rows,right):
    totals={name:arb(0) for name in NAMES};maxima={name:arb(0) for name in NAMES};edge=Fraction(0)
    for row in rows:
        lo,hi=map(Fraction,row['interval'])
        if lo!=edge or not lo<hi:raise ValueError('the complete mixed source partition has a gap')
        edge=hi
        if lo>=right:continue
        length=min(hi,right)-lo
        for name in NAMES:
            b=row['complete_Z_source'][name]
            radial=up(b['L2_L2_radial']) if hi<=right else exact(length).sqrt()*up(b['L2_sup'])
            totals[name]=(totals[name]+radial*radial).upper()
            maxima[name]=max(maxima[name],up(b['L2_sup'])).upper()
    if edge!=Fraction(25,8):raise ValueError('the complete source cover was truncated')
    return {name:dict(L2_L2_radial=record(totals[name].sqrt().upper()),
        L2_sup=record(maxima[name])) for name in NAMES}


def plan(a,doc):
    manifest,body,repair,rows,context,completed,required=check_inputs(a,doc)
    output=[];start=time.monotonic()
    for i,row in enumerate(rows):
        base,evidence=baseline(row,repair['rows'][i],context)
        candidates=[('complete_original_raw_nonmean_plus_true_mean_and_Z_fee',base)]
        if i in completed:candidates.extend(completed_pilot_candidates(completed[i]))
        best,origins=choose(candidates)
        output.append(dict(common_row=i,interval=row['interval'],original_row_sha256=rowsha(row),
            original_pieces=row['pieces'],complete_Z_source=best,selected_valid_bound=origins,
            original_raw_mean_baseline=evidence,
            already_completed_pilot_used=i in completed))
    remaining=[i for i in required if i not in completed]
    assignments=[dict(first=lo,end=hi,actual_new_rows=[i for i in remaining if lo<=i<hi]) for lo,hi in RANGES]
    gate(doc,'every_requested_new_compact_row_is_assigned_once_and_no_completed_pilot_cell_is_repeated',
        [i for a0 in assignments for i in a0['actual_new_rows']]==remaining
        and not set(remaining)&set(completed))
    doc.update(complete=True,selected_cells_complete=True,complete_valid_source_cover=True,
        complete_original_common_cells=7721,rows=output,assignments=assignments,
        new_compact_rows_requested=len(remaining),new_compact_rows_computed=0,
        new_source_rows_executed_in_this_child=0,
        original_completed_exact_bump_pilot_native_sha256=PILOT,
        all_original_completed_pilot_subcells_reused=True,all_original_scalar_mean_residuals_retained=True,
        complete_source_bounds=dict(full_body=aggregate(output,Fraction(25,8)),
            inner_body=aggregate(output,Fraction(9,10)),
            fixed_negative_phase_window=aggregate(output,pilot.PHASE_RIGHT)),
        new_source_rows_seconds=time.monotonic()-start)
    save(a.out,doc)


def range_run(a,doc):
    manifest,body,repair,rows,context,completed,required=check_inputs(a,doc)
    plan_doc=read(a.plan)
    gate(doc,'exact_completed_baseline_plan_and_requested_disjoint_range',
        plan_doc.get('kind')==PLAN_KIND and plan_doc.get('complete') and not plan_doc.get('failure')
        and plan_doc.get('source_sha256')==sha(__file__)
        and plan_doc.get('common_input_sha256')==doc['common_input_sha256']
        and plan_doc.get('original_parts')==doc['original_parts']
        and (a.first,a.end) in RANGES and all(x['passed'] for x in plan_doc.get('gates',[])))
    assignment=next(x for x in plan_doc['assignments'] if (x['first'],x['end'])==(a.first,a.end))
    selected=assignment['actual_new_rows']
    if selected!=[i for i in required if a.first<=i<a.end and i not in completed]:
        raise ValueError('the requested new source list changed')
    bg=load_candidate(a.candidate);trial=load_candidate(a.response)
    nodes=[Fraction(float(x)) for x in bg['radial_nodes']]
    gate(doc,'unchanged_complete_physical_cubics_with_all193_states_and_real_mean',
        bg['piece_coefficients'].shape==(4,6144,65)
        and trial['piece_coefficients'].shape==(4,6144,193)
        and np.array_equal(bg['radial_nodes'].view(np.uint64),trial['radial_nodes'].view(np.uint64))
        and nodes[0]==0 and nodes[-1]==Fraction(25,8))
    alpha=exact(Fraction(manifest['row_identity']['exact_alpha']))
    doc.update(plan_native_sha256=sha(a.plan),range=[a.first,a.end],selected_original_rows=selected,rows=[],
        new_source_rows_executed_in_this_child=0)
    if a.resume:
        previous=read(a.resume)
        if (previous.get('kind')!=RANGE_KIND or previous.get('source_sha256')!=sha(__file__)
            or previous.get('common_input_sha256')!=doc['common_input_sha256']
            or previous.get('plan_native_sha256')!=sha(a.plan)
            or previous.get('selected_original_rows')!=selected
            or [x['common_row'] for x in previous.get('rows',[])]!=selected[:len(previous.get('rows',[]))]):
            raise ValueError('a true new source prefix changed identity')
        for r in previous.get('rows',[]):
            if (not r.get('actual_new_source_cell_complete')
                or r['original_row_sha256']!=rowsha(rows[r['common_row']])):
                raise ValueError('an already completed source cell changed')
        doc['rows']=previous['rows']
        doc['original_prefix_provenance']=dict(native_sha256=sha(a.resume),
            original_failure=previous.get('failure'),completed_cells_not_recomputed=True)
    for i in selected[len(doc['rows']):]:
        tick=time.monotonic();r=rows[i];lo,hi=map(Fraction,r['interval'])
        whole={k:interval(v) for k,v in r['intrinsic_whole_third_jets'].items()}
        midpoint={k:interval(v) for k,v in r['intrinsic_midpoint_jets'].items()}
        cell=pilot.projection_at(r,body['residual_rows'][i],repair['rows'][i],
            bg,trial,nodes,alpha,context,lo,hi,whole,midpoint)
        compact=dict(common_row=i,interval=r['interval'],original_row_sha256=rowsha(r),
            actual_new_source_cell_complete=True,complete_Z_source=cell['continuous_Z_complete_residual'],
            full_raw_residual_including_mean=cell['raw_full_residual_before_any_mean_completion'],
            complete_Z_transfer=cell['complete_Z_source_transfer_evidence'],
            exact_bump_coefficients=cell['exact_compact_source_coefficient_evidence'],
            scalar_model_budgets=cell['scalar_model_budgets'],
            D_component_budgets=cell['D_component_budgets'],Fnu_component_budgets=cell['Fnu_component_budgets'],
            full_independent_mean_retained=True,known_high97_through160_retained=True,
            original_whole_eta_scalar_jets_reused=True,new_target_provider_calls=0,
            complete_projection_record_sha256=rowsha(cell),
            complete_projection_defined_by_pinned_source_and_original_exact_inputs=True,
            seconds=time.monotonic()-tick)
        doc['rows'].append(compact);doc['new_source_rows_executed_in_this_child']+=1;save(a.out,doc)
        print(json.dumps(dict(actual_new_source_row=i,completed=len(doc['rows']),requested=len(selected),
            low193_Z_sup=compact['complete_Z_source']['low193']['L2_sup']['upper'],
            seconds=compact['seconds'])),flush=True)
    gate(doc,'every_requested_new_compact_source_row_completed_exactly_once',
        [x['common_row'] for x in doc['rows']]==selected)
    doc.update(complete=True,selected_cells_complete=True,new_compact_rows_computed=len(selected),
        complete_valid_source_cover=False)
    save(a.out,doc)


def finish(a,doc):
    base=read(a.plan)
    gate(doc,'unchanged_complete_baseline_and_full_raw_mean_cover',
        base.get('kind')==PLAN_KIND and base.get('complete') and not base.get('failure')
        and base.get('source_sha256')==sha(__file__) and base.get('complete_valid_source_cover')
        and len(base.get('rows',[]))==7721 and all(x['passed'] for x in base.get('gates',[])))
    if len(a.range_natives)!=4 or len(a.range_processes)!=4:
        raise ValueError('all four actual disjoint range artifacts are required')
    received={};new={};receipts=[]
    for path,process_path in zip(a.range_natives,a.range_processes):
        r=read(path);process=read(process_path);pair=tuple(r.get('range',[]))
        gate(doc,'actual_complete_new_source_range_'+str(pair),
            pair in RANGES and pair not in received and r.get('kind')==RANGE_KIND
            and r.get('complete') and not r.get('failure') and r.get('selected_cells_complete')
            and r.get('source_sha256')==sha(__file__) and r.get('plan_native_sha256')==sha(a.plan)
            and r.get('common_input_sha256')==base['common_input_sha256']
            and r.get('original_parts')==base['original_parts']
            and all(x['passed'] for x in r.get('gates',[]))
            and pilot.actual(process,a.workflow_run)
            and process.get('phase')=='range'
            and process.get('complete_native_sha256')==sha(path))
        expected=next(x['actual_new_rows'] for x in base['assignments'] if (x['first'],x['end'])==pair)
        if [x['common_row'] for x in r['rows']]!=expected:
            raise ValueError('a new exact-bump range is incomplete or overlaps a previous source cell')
        for row in r['rows']:
            i=row['common_row']
            if (i in new or row['interval']!=base['rows'][i]['interval']
                or row['original_row_sha256']!=base['rows'][i]['original_row_sha256']
                or not row.get('actual_new_source_cell_complete')
                or not row.get('full_independent_mean_retained')
                or not row.get('known_high97_through160_retained')):
                raise ValueError('a completed exact-bump cell identity or full mean was lost')
            new[i]=row
        received[pair]=True;receipts.append(dict(range=list(pair),native_sha256=sha(path),
            original_actual_process_sha256=sha(process_path),actual_new_rows=len(expected)))
    expected=[i for assignment in base['assignments'] for i in assignment['actual_new_rows']]
    gate(doc,'exact_union_of_all_new_requested_rows_with_no_repeated_pilot_cell',
        sorted(new)==expected and not set(new)&set(base['original_exact_bump_pilot_rows_reused']))
    output=[]
    for old in base['rows']:
        i=old['common_row'];candidates=[('complete_original_plan_bound',old['complete_Z_source'])]
        if i in new:candidates.append(('new_exact_rational_bump_cached_whole_eta',new[i]['complete_Z_source']))
        best,origins=choose(candidates)
        output.append(dict(common_row=i,interval=old['interval'],original_row_sha256=old['original_row_sha256'],
            complete_Z_source=best,selected_valid_bound=origins,
            already_completed_pilot_used=old['already_completed_pilot_used'],
            actual_new_exact_bump_cell_used=i in new,
            true_raw_mean_included=True))
    doc.update(complete=True,selected_cells_complete=True,complete_valid_source_cover=True,
        complete_original_common_cells=7721,rows=output,range_receipts=receipts,
        candidate_sha256=base['candidate_sha256'],
        derived_continuous_centre_definition_sha256=base['derived_continuous_centre_definition_sha256'],
        original_full_physical_response_trial_sha256=base['original_full_physical_response_trial_sha256'],
        exact_continuous_direction_definition_sha256=pilot.Z_DEFINITION,
        common_input_sha256=base['common_input_sha256'],original_parts=base['original_parts'],
        original_plan_native_sha256=sha(a.plan),original_exact_bump_pilot_native_sha256=PILOT,
        original_exact_bump_pilot_rows_reused=base['original_exact_bump_pilot_rows_reused'],
        new_compact_rows_computed=len(new),new_source_rows_executed_in_this_child=0,new_target_provider_calls=0,
        old_original_target_mean_or_trial_reconstructions_executed=0,
        exact_affine_parameter_offset='0',physical_parameter='fixed original physical eta0 and nu',
        whole_complete_source_interval=['0','25/8'],
        complete_source_bounds=dict(full_body=aggregate(output,Fraction(25,8)),
            inner_body=aggregate(output,Fraction(9,10)),
            fixed_negative_phase_window=aggregate(output,pilot.PHASE_RIGHT)),
        true_independent_even_mean_retained=True,known_high_output_retained=True,
        unknown_high_input_feedback_still_required=True,
        exact_same_Z_waist_and_true_cut_sources_still_required=True,
        actual_full_PDE_response_error_proved=False,complete_infinite_inverse_proved=False)
    save(a.out,doc)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--phase',choices=('plan','range','finish'),required=True)
    for name in COMMON+('plan','out','resume'):p.add_argument('--'+name,type=Path)
    p.add_argument('--parts',type=Path,nargs='*',default=[])
    p.add_argument('--range-natives',type=Path,nargs='*',default=[])
    p.add_argument('--range-processes',type=Path,nargs='*',default=[])
    p.add_argument('--first',type=int,default=0);p.add_argument('--end',type=int,default=0)
    p.add_argument('--workflow-run',type=int)
    a=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out is None or a.out.exists():raise ValueError('a fresh actual output is required')
    if a.phase!='finish' and any(getattr(a,n.replace('-','_')) is None for n in COMMON):
        raise ValueError('every original complete scientific input is required')
    kinds={'plan':PLAN_KIND,'range':RANGE_KIND,'finish':FINISH_KIND}
    doc=dict(kind=kinds[a.phase],complete=False,failure=None,gates=[],rows=[],
        source_sha256=sha(__file__),exact_bump_source_sha256=sha(pilot.__file__),
        phase=a.phase,actual_full_PDE_response_error_proved=False,complete_infinite_inverse_proved=False)
    if a.phase=='plan' and a.resume:
        try:
            check_inputs(a,doc)
            previous=read(a.resume)
            gate(doc,'exact_complete_original_plan_reused_without_recomputing_any_baseline_row',
                previous.get('kind')==PLAN_KIND and previous.get('complete') and not previous.get('failure')
                and previous.get('source_sha256')==sha(__file__)
                and previous.get('common_input_sha256')==doc['common_input_sha256']
                and previous.get('original_parts')==doc['original_parts']
                and previous.get('complete_valid_source_cover')
                and [r['common_row'] for r in previous.get('rows',[])]==list(range(7721))
                and previous.get('gates') and all(x['passed'] for x in previous['gates']))
            a.out.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(a.resume,a.out)
            print(json.dumps(dict(phase='plan',complete=True,original_native_sha256=sha(a.resume),
                original_plan_bytes_reused=True,new_source_rows_executed_in_this_child=0,
                new_target_provider_calls=0,seconds=time.monotonic()-started)),flush=True)
        except BaseException as error:
            doc['failure']=dict(type=type(error).__name__,message=str(error))
            doc['seconds']=time.monotonic()-started;save(a.out,doc);raise
        return
    try:{'plan':plan,'range':range_run,'finish':finish}[a.phase](a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(phase=a.phase,complete=doc['complete'],gates=len(doc['gates']),
        rows=len(doc['rows']),new_target_provider_calls=0,seconds=doc['seconds'])),flush=True)


if __name__=='__main__':main()
