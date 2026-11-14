#!/usr/bin/env python3
"""Recover two incomplete endpoint quarter ranges without repeating successful cells.

The first Hermite polynomial retains its authorized inlet extension. The
remaining graft quarters use a positive-width intrinsic enclosure that contains
fixed eta0. All original successful rows and six other ranges remain exact.
"""
from __future__ import annotations
import argparse,json,os,shutil,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
import fourfold_codazzi_fixed_eta_physical_cap_pilot as prior
from fourfold_phase_natural_exterior_graft import NaturalGraft

read,save,sha,positive,rec,exact,rowsha=prior.read,prior.save,prior.sha,prior.positive,prior.rec,prior.exact,prior.rowsha
common=prior.common
TERM_NAMES,ERROR_NAMES,BOUNDARY_ERRORS=prior.TERM_NAMES,prior.ERROR_NAMES,prior.BOUNDARY_ERRORS
LEFT,RIGHT=prior.LEFT,prior.RIGHT
PUBLIC=prior.PUBLIC
RANGES=((0,256),(256,512),(512,768),(768,1024),(1024,1280),(1280,1536),(1536,1792),(1792,1977))
KINDS={'plan':'actual_complete_fixed_eta_quarter_cap_plan_v1',
    'range':'actual_complete_fixed_eta_quarter_cap_range_inlet_recovery_v2',
    'finish':'actual_complete_fixed_eta_quarter_cap_finish_inlet_recovery_v2'}
ORIGINAL_RUN=43623547711
ORIGINAL_SOURCE='54e5ec52033bb109618fde1c840730b4b589280382b2da196d3ea748af4490de'
ORIGINAL_PLAN='406e3e5331720a3f87f2b5f53c2e7d2988bea25b7537d650157ed97278e3073a'
ORIGINAL_PREFIXES={
    (0,256):('dff609fe852fb538f126865296e76e991c553f2b586471eb58627461dd320f63',1,
        'a new quarter domain escaped its original Hermite definition'),
    (1792,1977):('1d940cb67a807560c016c2fdb07503ca4c0be1ffd0866bf83a988c27477c3028',640,
        'parameter half width must be positive')}
RECOVERY_RANGES=tuple(ORIGINAL_PREFIXES)
ORIGINAL_WORKER='04d4380d840504f3aedf2da2d95f2112677819885f4a1e367480f97298b332db'
ORIGINAL_MANIFEST='6dc5bf2d8030d506c74dc29ef2cb3c1991cd5f7fb8c2a051b03b0ad89cb2fb69'
FIXED='b5a157d4005eb4aad1c536512c4ea5dcb431e90d09c4b05f324db5cf09203138'
FIXED_SOURCE='3cbadc70a5fc2f1fb9567d9e982995c6e194952913914d234e728a3aee18b75a'
FIXED_WORKER='953940428d8c2ac6a1bf9a1874d9e806d8920f2787f00ba9042ce449db208267'
FIXED_MANIFEST='0e0c95425c53d9fa0d3287f656b9ac478483ff03b159a5412048b39e04f5ffad'
PLAN_INPUTS=prior.INPUTS+('fixed-pilot','fixed-process')
RANGE_INPUTS=('candidate','proposal','object','repair-report','plan')


def gate(doc,name,ok):
    doc['gates'].append(dict(name=name,passed=bool(ok)))
    if not ok:raise ValueError(name)


def proved(d):
    return d.get('complete') and not d.get('failure') and d.get('gates') and all(g['passed'] for g in d['gates'])


def request_interval(parent,j):
    lo,hi=map(Fraction,parent['interval']);h=(hi-lo)/4
    return lo+j*h,lo+(j+1)*h


def plan(a,doc):
    pilot,full,rows,w=prior.validate(a,doc)
    fixed,process=read(a.fixed_pilot),read(a.fixed_process)
    gate(doc,'actual_complete336_fixed_eta_domains_and_original_sixteen_parents',
        sha(a.fixed_pilot)==FIXED and proved(fixed) and fixed.get('kind')==prior.KIND
        and fixed.get('source_sha256')==FIXED_SOURCE and len(fixed.get('new_domain_results',[]))==336
        and fixed.get('complete_original_parent_cells')==1977
        and fixed.get('complete_new_fixed_eta_domains')==336
        and fixed.get('exact_affine_parameter_offset')=='0'
        and prior.actual(process,43619535345)
        and process.get('worker_source_sha256')==FIXED_WORKER
        and process.get('input_manifest_sha256')==FIXED_MANIFEST
        and process.get('complete_native_sha256')==FIXED
        and fixed.get('direction_sha256')==rowsha(pilot['direction'])
        and fixed.get('original_array_sha256')==pilot['original_full_matrix_array_sha256'])
    for k in prior.INPUTS:
        if fixed['input_sha256'].get(k)!=sha(getattr(a,k.replace('-','_'))):
            raise ValueError('the fixed pilot scientific input differs from the exact original input')
    for i,(p,old) in enumerate(zip(a.range_natives,a.range_processes)):
        if (fixed['input_sha256'].get('range-native-'+str(i))!=sha(p)
            or fixed['input_sha256'].get('range-process-'+str(i))!=sha(old)):
            raise ValueError('the actual original four-range receipt order changed')
    selected=fixed['selected_original_cells']
    if len(selected)!=16 or len(set(selected))!=16:raise ValueError('all16 original pilot parents are required')
    quarters=[]
    expected=[(i,4,j) for i in selected for j in range(4)]
    for row in fixed['new_domain_results']:
        request=tuple(row['request'])
        if request[1]!=4:continue
        i,parts,j=request;left,right=request_interval(rows[i],j)
        if (request not in expected or not row.get('complete_new_fixed_eta_coefficient_domain')
            or row.get('new_parameter_half_width')!='0'
            or row.get('original_parent_row_sha256')!=rowsha(rows[i])
            or row['interval']!=list(map(str,(left,right)))
            or row.get('full_resolved_support')!=255 or row.get('independent_input_columns')!=1):
            raise ValueError('a completed original quarter domain changed')
        quarters.append(row)
    quarters.sort(key=lambda r:tuple(r['request']))
    gate(doc,'all64_original_quarter_domains_reused_exactly_with_all_scalar_and_Fourier_data',
        [tuple(r['request']) for r in quarters]==expected)
    decisions=fixed['complete_parent_representation_decisions']
    if len(decisions)!=1977:raise ValueError('the complete old coupled parent decisions are required')
    for i,d in enumerate(decisions):
        if d.get('index')!=i or d.get('original_direct_row_sha256')!=rowsha(rows[i]):
            raise ValueError('an original complete parent representation changed')
    assignments=[]
    for first,end in RANGES:
        parents=[i for i in range(first,end) if i not in selected]
        requests=[[i,4,j] for i in parents for j in range(4)]
        assignments.append(dict(first=first,end=end,actual_new_parent_indices=parents,
            actual_new_requests=requests,reused_original_parent_indices=[i for i in selected if first<=i<end]))
    gate(doc,'eight_disjoint_ranges_cover_all7844_new_domains_without_any_completed_domain',
        sum(len(x['actual_new_requests']) for x in assignments)==7844
        and sorted(i for x in assignments for i in x['actual_new_parent_indices'])==[i for i in range(1977) if i not in selected])
    doc.update(complete=True,original_candidate_sha256=common.CURRENT,
        derived_continuous_centre_definition_sha256=common.REPAIR,
        exact_continuous_direction_definition_sha256=fixed['exact_continuous_direction_definition_sha256'],
        direction=pilot['direction'],direction_sha256=rowsha(pilot['direction']),
        original_array_sha256=fixed['original_array_sha256'],original_parent_rows=rows,
        original_fixed_pilot_native_sha256=FIXED,original_fixed_pilot_process_sha256=sha(a.fixed_process),
        original_fixed_pilot_input_sha256=fixed['input_sha256'],
        reused_quarter_rows=quarters,reused_quarter_row_sha256=[rowsha(r) for r in quarters],
        original_pilot_parent_decisions=decisions,
        original_pilot_complete_physical_cap_error=fixed['selected_complete_physical_cap_error'],
        original_pilot_complete_physical_error_data=fixed['selected_complete_physical_error_data'],
        original_pilot_complete_fourteen_fees=fixed['selected_complete_fourteen_physical_fees'],
        original_direct_coupled_baseline_physical_cap_error=fixed['original_direct_coupled_baseline_physical_cap_error'],
        original_direct_coupled_baseline_error_data=fixed['original_direct_coupled_baseline_error_data'],
        original_direct_coupled_baseline_fourteen_fees=fixed['original_direct_coupled_baseline_fourteen_fees'],
        original_six_boundary_errors={k:full['complete_mixed_error_data'][k] for k in BOUNDARY_ERRORS},
        original_complete_physical_Green_gains=pilot['original_complete_Green_gains'],
        original_range_receipts=fixed['original_complete_range_receipts'],
        reused_original_parent_indices=selected,complete_original_parent_cells=1977,
        reused_original_quarter_domains=64,requested_new_quarter_domains=7844,
        total_complete_quarter_domains=7908,assignments=assignments,
        exact_interval=[str(LEFT),str(RIGHT)],exact_affine_parameter_offset='0',
        physical_parameter='fixed physical eta0 and original nu',
        whole_original_parameter_interval_claimed=False,
        original_target_or_trial_domains_recomputed=0,new_quarter_domains_executed_in_this_child=0)


def plan_input(a,doc):
    p=read(a.plan)
    gate(doc,'exact_original_successful_plan_preserves_all_original_scientific_identities',
        sha(a.plan)==ORIGINAL_PLAN and p.get('kind')==KINDS['plan'] and proved(p)
        and p.get('source_sha256')==ORIGINAL_SOURCE
        and p.get('original_fixed_pilot_native_sha256')==FIXED
        and p.get('complete_original_parent_cells')==1977
        and p.get('reused_original_quarter_domains')==64 and p.get('requested_new_quarter_domains')==7844
        and p.get('total_complete_quarter_domains')==7908
        and p.get('exact_affine_parameter_offset')=='0'
        and p.get('original_candidate_sha256')==common.CURRENT
        and p.get('derived_continuous_centre_definition_sha256')==common.REPAIR)
    doc.update(plan_native_sha256=sha(a.plan),plan_input_sha256=p['input_sha256'],
        original_candidate_sha256=p['original_candidate_sha256'],
        derived_continuous_centre_definition_sha256=p['derived_continuous_centre_definition_sha256'],
        exact_continuous_direction_definition_sha256=p['exact_continuous_direction_definition_sha256'],
        direction_sha256=p['direction_sha256'],exact_affine_parameter_offset='0',
        physical_parameter=p['physical_parameter'],whole_original_parameter_interval_claimed=False,
        reused_original_quarter_domains=64,total_complete_quarter_domains=7908)
    return p


def range_run(a,doc):
    plan_doc=plan_input(a,doc);pair=(a.first,a.end)
    if pair not in RECOVERY_RANGES:raise ValueError('only the two incomplete original endpoint ranges may execute')
    prefix_sha,prefix_count,prefix_failure=ORIGINAL_PREFIXES[pair]
    assignment=next(x for x in plan_doc['assignments'] if (x['first'],x['end'])==pair)
    requests=[tuple(x) for x in assignment['actual_new_requests']]
    for key in ('candidate','proposal','object','repair-report'):
        if sha(getattr(a,key.replace('-','_')))!=plan_doc['input_sha256'][key]:
            raise ValueError('the range scientific object differs from the complete plan')
    proposal=read(a.proposal);paths={Path(p).name:Path(p) for p in proposal['full_matrix_inputs']}
    if set(paths)!={'state.npy','derivative-left.npy','derivative-right.npy'}:
        raise ValueError('all three exact original matrices are required')
    endpoint=Path(proposal['physical_endpoint_graph']['path'])
    identities={str(p):sha(p) for p in paths.values()};identities[str(endpoint)]=sha(endpoint)
    if identities!=plan_doc['original_array_sha256']:raise ValueError('an original complete array changed')
    state,dl,dr=[np.load(paths[n],mmap_mode='r',allow_pickle=False)
        for n in ('state.npy','derivative-left.npy','derivative-right.npy')]
    with np.load(endpoint,allow_pickle=False) as e:
        nodes=[Fraction.from_float(float(x)) for x in e['nodes']]
        left_state=e['left_state'];right_state=e['right_state']
    gate(doc,'all_original257_by97_arrays_and_true9over10_inlet_extension_retained',
        state.shape==(len(nodes),257,97) and dl.shape==(len(nodes)-1,257,97) and dr.shape==dl.shape
        and np.array_equal(state[0],left_state) and np.array_equal(state[-1],right_state)
        and nodes[0]==Fraction.from_float(float(LEFT)) and LEFT<=nodes[0]<nodes[1]
        and nodes[-1]==RIGHT and proposal['identity']['model']['exact_requested_left']==str(LEFT))
    w=np.asarray([float.fromhex(x) for x in plan_doc['direction']['exact_binary64_w0_hex']],dtype=float)
    if w.shape!=(97,) or not np.isfinite(w).all():raise ValueError('the complete original even direction is required')
    provider=prior.PhysicalCapCoefficientJets(a.candidate,a.object,a.repair_report,
        half_width=Fraction(0),width=Fraction(1,16),angles=512,cutoff=127)
    parents=plan_doc['original_parent_rows']
    cuts=sorted({LEFT,RIGHT}|{x for x in nodes+provider.knots+provider.target.cuts if LEFT<x<RIGHT})
    gate(doc,'same1977_parent_partition_with_only_new_fixed_parameter_quarter_domains',
        len(cuts)==1978 and all(r['interval']==list(map(str,cuts[i:i+2])) for i,r in enumerate(parents)))
    doc.update(range=list(pair),rows=[],requested_new_domains=len(requests),
        requested_new_parent_count=len(assignment['actual_new_parent_indices']),
        original_array_sha256=identities,new_quarter_domains_executed_in_this_child=0)
    if a.resume:
        prior_doc=read(a.resume)
        if (prior_doc.get('kind')!=KINDS['range'] or prior_doc.get('source_sha256')!=sha(__file__)
            or prior_doc.get('input_sha256')!=doc['input_sha256'] or prior_doc.get('range')!=list(pair)
            or prior_doc.get('plan_native_sha256')!=sha(a.plan)
            or prior_doc.get('original_array_sha256')!=identities
            or prior_doc.get('direction_sha256')!=plan_doc['direction_sha256']):
            raise ValueError('only an exact same-input completed-domain prefix may resume')
        saved=prior_doc.get('rows',[])
        if len(saved)>len(requests):raise ValueError('an original prefix exceeds the request')
        for r,request in zip(saved,requests):
            if (tuple(r.get('request',[]))!=request or not r.get('complete_new_fixed_eta_coefficient_domain')
                or r.get('original_parent_row_sha256')!=rowsha(parents[request[0]])
                or r['interval']!=list(map(str,request_interval(parents[request[0]],request[2])))):
                raise ValueError('a completed quarter domain or its input identity changed')
        doc['rows']=saved;doc['original_prefix_provenance']=dict(native_sha256=sha(a.resume),
            complete_domains_reused=len(saved),original_failure=prior_doc.get('failure'))
    prefix,process=read(a.original_prefix),read(a.original_prefix_process)
    logical=f'native/new-fixed-eta-quarter-domains-{pair[0]:04d}-{pair[1]:04d}.json.gz'
    records=[r for r in process.get('native_files',[]) if r.get('logical_file')==logical]
    gate(doc,'exact_failed_original_process_and_successful_quarter_prefix_preserved_without_reexecution',
        sha(a.original_prefix)==prefix_sha
        and prefix.get('kind')=='actual_complete_fixed_eta_quarter_cap_range_v1'
        and prefix.get('source_sha256')==ORIGINAL_SOURCE
        and prefix.get('input_sha256')==doc['input_sha256']
        and prefix.get('range')==list(pair) and prefix.get('plan_native_sha256')==ORIGINAL_PLAN
        and prefix.get('original_array_sha256')==identities
        and prefix.get('direction_sha256')==plan_doc['direction_sha256']
        and len(prefix.get('rows',[]))==prefix_count
        and [tuple(r.get('request',[])) for r in prefix['rows']]==requests[:prefix_count]
        and all(r.get('complete_new_fixed_eta_coefficient_domain') and r.get('intrinsic_midpoint_jets')
            for r in prefix['rows'])
        and prefix.get('gates') and all(g['passed'] for g in prefix['gates'])
        and prefix.get('failure',{}).get('message')==prefix_failure
        and process.get('repository')==PUBLIC and str(process.get('run_id'))==str(ORIGINAL_RUN)
        and process.get('phase')=='range' and process.get('source_range')==list(pair)
        and process.get('worker_source_sha256')==ORIGINAL_WORKER
        and process.get('input_manifest_sha256')==ORIGINAL_MANIFEST
        and len(records)==1 and records[0].get('sha256')==prefix_sha
        and any(c.get('label')=='actual_complete_quarter_cap_range'
            and c.get('actual_returncode')==1 for c in process.get('children',[])))
    for row,request in zip(prefix['rows'],requests[:prefix_count]):
        if (row['original_parent_row_sha256']!=rowsha(parents[request[0]])
            or row['interval']!=list(map(str,request_interval(parents[request[0]],request[2])))):
            raise ValueError('an exact successful original quarter has a different parent')
    if not a.resume:doc['rows']=prefix['rows']
    if ([rowsha(r) for r in doc['rows'][:prefix_count]]!=[rowsha(r) for r in prefix['rows']]):
        raise ValueError('all original successful quarters must remain byte-for-byte canonical')
    doc['inlet_recovery_provenance']=dict(original_workflow_run=ORIGINAL_RUN,
        original_source_sha256=ORIGINAL_SOURCE,original_plan_native_sha256=ORIGINAL_PLAN,
        original_prefix_native_sha256=prefix_sha,original_prefix_process_sha256=sha(a.original_prefix_process),
        original_prefix_row_sha256=[rowsha(r) for r in prefix['rows']],
        original_successful_quarters_reused=prefix_count,original_successful_quarters_recomputed=0,
        original_failure=prefix.get('failure'),
        sole_Hermite_guard_change='piece==0 and left==LEFT becomes piece==0 and LEFT<=left',
        only_authorized_left_extension=[str(LEFT),str(nodes[0])],
        physical_parameter_is_still_fixed_eta0=True)
    if pair==(1792,1977):
        # The original positive-width graft family contains the fixed eta0.
        # Only this target enclosure is wider; the candidate and physical
        # problem remain at affine offset zero. No old target cell is rerun.
        if any(request_interval(parents[i],j)[0]<3 for i,parts,j in requests[prefix_count:]):
            raise ValueError('the graft recovery may only enclose the original r>=3 tail')
        provider.target._graft=NaturalGraft(a.object,Fraction(1,10**9),Fraction(1,8))
        doc['inlet_recovery_provenance']['new_graft_target_enclosure_half_width']='1/1000000000'
        doc['inlet_recovery_provenance']['original_parameter_germ_source_unchanged']=True
    for request in requests[len(doc['rows']):]:
        started=time.monotonic();index,parts,j=request
        left,right=request_interval(parents[index],j);piece=max(0,bisect_right(nodes,left)-1)
        if not ((nodes[piece]<=left or piece==0 and LEFT<=left) and left<right<=nodes[piece+1]):
            raise ValueError('a new quarter domain escaped its original Hermite definition')
        values,derivatives=common.hermite_series(state[piece],state[piece+1],dl[piece],dr[piece],
            nodes[piece],nodes[piece+1],left,right)
        values=[common.contract_matrix(v,w) for v in values]
        derivatives=[common.contract_matrix(v,w) for v in derivatives]
        coefficient=provider.coefficients(left,right)
        residual=common.cell_residual(provider,coefficient,values,derivatives,m=128)
        finite=residual['finite_ordinary'];length=exact(right-left)
        pieces=[x['nonmean_inverse_sqrt_M_L2_average'] for x in finite]
        pieces+=[x['complete_mean_L2_average'] for x in finite]
        terms=[length*x*x for x in pieces+list(residual['ordinary_remainder_HS'])]
        terms.extend(x*x for x in residual['divergence_module_HS'])
        if residual['independent_columns']!=1 or residual['full_support']!=255:
            raise ValueError('the complete product support or independent mean was truncated')
        row=provider.row(coefficient)
        # Preserve the already computed exact midpoint jets for later consumers.
        # This records existing arithmetic; it makes no new target call.
        row['intrinsic_midpoint_jets']={k:rec(v) for k,v in coefficient['centre'].items()}
        row['intrinsic_target_enclosure_half_width']='1/1000000000' if left>=3 else '0'
        row['intrinsic_target_enclosure_contains_fixed_eta0']=True
        row.update(request=list(request),original_parent_row_sha256=rowsha(parents[index]),
            complete_new_fixed_eta_coefficient_domain=True,exact_affine_parameter_offset='0',
            new_parameter_half_width='0',original_parameter_half_width='1/1000000000',
            source_representation_kept_as_one_eight_component_unit=True,
            full_physical_state_dimension=257,full_resolved_support=255,independent_input_columns=1,
            accumulator_terms={k:rec(v.upper()) for k,v in zip(TERM_NAMES,terms)},
            scalar_remainder=residual['scalar_remainder'],
            full_Hermite_module={k:rec(v) for k,v in zip(('B','C'),residual['complete_Hermite_module_HS'])},
            actual_seconds=time.monotonic()-started)
        doc['rows'].append(row);doc['new_quarter_domains_executed_in_this_child']+=1
        if len(doc['rows'])%8==0:save(a.out,doc)
        print(json.dumps(dict(range=list(pair),request=list(request),completed=len(doc['rows']),
            total=len(requests),seconds=row['actual_seconds'])),flush=True)
    gate(doc,'every_assigned_new_quarter_domain_complete_without_repeating_pilot_domains',
        [tuple(r['request']) for r in doc['rows']]==requests
        and all(r['request'][0] not in plan_doc['reused_original_parent_indices'] for r in doc['rows']))
    doc.update(complete=True,selected_domains_complete=True,completed_new_domains=len(doc['rows']),
        original_target_or_trial_domains_recomputed=0,changing_models_never_mixed_component_by_component=True)


def finish(a,doc):
    p=plan_input(a,doc)
    if len(a.range_natives)!=8 or len(a.range_processes)!=8:raise ValueError('all eight completed ranges are required')
    table={tuple(r['request']):r for r in p['reused_quarter_rows']}
    if len(table)!=64:raise ValueError('the64 original complete quarter rows are required')
    receipts=[];seen=set()
    for native,process in zip(a.range_natives,a.range_processes):
        r,proc=read(native),read(process);pair=tuple(r.get('range',[]))
        gate(doc,'actual_complete_quarter_range_'+str(pair),
            pair in RANGES and pair not in seen
            and r.get('kind')==(KINDS['range'] if pair in RECOVERY_RANGES
                else 'actual_complete_fixed_eta_quarter_cap_range_v1')
            and proved(r) and r.get('source_sha256')==(sha(__file__) if pair in RECOVERY_RANGES else ORIGINAL_SOURCE)
            and r.get('selected_domains_complete') and r.get('plan_native_sha256')==sha(a.plan)
            and r.get('direction_sha256')==p['direction_sha256']
            and r.get('original_array_sha256')==p['original_array_sha256']
            and proc.get('repository')==PUBLIC
            and str(proc.get('run_id'))==str(a.workflow_run if pair in RECOVERY_RANGES else ORIGINAL_RUN)
            and proc.get('phase')=='range'
            and any(c.get('label')=='actual_complete_quarter_cap_range'
                and c.get('actual_returncode')==0 for c in proc.get('children',[]))
            and any(e.get('logical_file')=='native/new-fixed-eta-quarter-domains-'+str(pair[0]).zfill(4)+'-'+str(pair[1]).zfill(4)+'.json.gz'
                and e.get('sha256')==sha(native) for e in proc.get('native_files',[]))
            and proc.get('actual_plan_native_sha256')==sha(a.plan))
        if pair in RECOVERY_RANGES:
            recovery=r.get('inlet_recovery_provenance',{});prefix_sha,prefix_count,_=ORIGINAL_PREFIXES[pair]
            if (recovery.get('original_prefix_native_sha256')!=prefix_sha
                or recovery.get('original_successful_quarters_reused')!=prefix_count
                or [rowsha(x) for x in r['rows'][:prefix_count]]!=recovery.get('original_prefix_row_sha256')):
                raise ValueError('every successful original prefix row must survive the endpoint recovery')
        elif (proc.get('worker_source_sha256')!=ORIGINAL_WORKER
            or proc.get('input_manifest_sha256')!=ORIGINAL_MANIFEST):
            raise ValueError('a middle range no longer has its exact original frozen process')
        assignment=next(x for x in p['assignments'] if (x['first'],x['end'])==pair)
        expected=[tuple(x) for x in assignment['actual_new_requests']]
        if [tuple(x['request']) for x in r['rows']]!=expected:raise ValueError('an actual range request is incomplete')
        for row in r['rows']:
            request=tuple(row['request']);i,parts,j=request
            if (request in table or parts!=4 or not row.get('complete_new_fixed_eta_coefficient_domain')
                or row.get('original_parent_row_sha256')!=rowsha(p['original_parent_rows'][i])
                or row['interval']!=list(map(str,request_interval(p['original_parent_rows'][i],j)))
                or row.get('full_resolved_support')!=255 or row.get('independent_input_columns')!=1):
                raise ValueError('a complete quarter cell changed or was counted twice')
            table[request]=row
        receipts.append(dict(range=list(pair),native_sha256=sha(native),actual_original_process_sha256=sha(process),
            source_sha256=r['source_sha256'],actual_workflow_run=int(proc['run_id']),
            actual_workflow_attempt=proc.get('run_attempt','1'),
            actual_worker_sha256=proc.get('worker_source_sha256'),
            actual_manifest_sha256=proc.get('input_manifest_sha256'),
            original_completed_prefix_domains_reused=ORIGINAL_PREFIXES[pair][1] if pair in RECOVERY_RANGES else 0,
            completed_new_domains=len(expected)));seen.add(pair)
    gate(doc,'all7908_quarter_domains_cover1977_parents_exactly_once_with64_original_rows_unchanged',
        seen==set(RANGES) and sorted(table)==[(i,4,j) for i in range(1977) for j in range(4)]
        and [rowsha(table[tuple(r['request'])]) for r in p['reused_quarter_rows']]==p['reused_quarter_row_sha256'])
    gains={k:positive(v) for k,v in p['original_complete_physical_Green_gains'].items()}
    chosen=[];all_quarters=[];decisions=[]
    for i,old in enumerate(p['original_parent_rows']):
        quarter_terms={key:rec(sum((positive(table[(i,4,j)]['accumulator_terms'][key])
            for j in range(4)),arb(0)).upper()) for key in TERM_NAMES}
        options=[('original_direct',old['accumulator_terms']),('complete_fixed_eta_quarters',quarter_terms)]
        for option in p['original_pilot_parent_decisions'][i]['refined_options']:
            options.append(('original_pilot_fixed_eta_'+str(option['subdivision']),option['all_eight_terms']))
        best_name,best=options[0];value=prior.score(best,gains)
        for name,terms in options[1:]:
            score=prior.score(terms,gains)
            if score<value:best_name,best,value=name,terms,score
        all_quarters.append(quarter_terms);chosen.append(best)
        decisions.append(dict(index=i,interval=old['interval'],original_direct_row_sha256=rowsha(old),
            complete_quarter_row_sha256=[rowsha(table[(i,4,j)]) for j in range(4)],
            selected_representation=best_name,selected_all_eight_terms=best,
            complete_quarter_all_eight_terms=quarter_terms,
            reused_original_pilot_quarters=i in p['reused_original_parent_indices']))
    mixed,errors,fees=prior.cap_bound(chosen,gains,p['original_six_boundary_errors'])
    quarter,quarter_errors,quarter_fees=prior.cap_bound(all_quarters,gains,p['original_six_boundary_errors'])
    candidates=[
        ('new_complete_coupled_selection',mixed,errors,fees),
        ('all_complete_fixed_eta_quarters',quarter,quarter_errors,quarter_fees),
        ('original_pilot_complete_coupled_bound',positive(p['original_pilot_complete_physical_cap_error']),
            {k:positive(v) for k,v in p['original_pilot_complete_physical_error_data'].items()},
            {k:positive(v) for k,v in p['original_pilot_complete_fourteen_fees'].items()}),
        ('original_direct_complete_coupled_bound',positive(p['original_direct_coupled_baseline_physical_cap_error']),
            {k:positive(v) for k,v in p['original_direct_coupled_baseline_error_data'].items()},
            {k:positive(v) for k,v in p['original_direct_coupled_baseline_fourteen_fees'].items()})]
    best=candidates[0]
    for candidate in candidates[1:]:
        if candidate[1]<best[1]:best=candidate
    name,bound,used_errors,used_fees=best
    gate(doc,'complete_eight_channel_representations_and_all14_Green_fees_preserved',
        len(decisions)==1977 and set(used_errors)==set(gains)==set(BOUNDARY_ERRORS+ERROR_NAMES)
        and bound.is_finite() and all(x.is_finite() and x>=0 for x in used_fees.values()))
    gate(doc,'only_whole_valid_physical_error_bounds_compared',
        all(bound<=candidate[1] for candidate in candidates))
    doc.update(complete=True,complete_original_parent_cells=1977,
        completed_new_quarter_domains=7844,complete_quarter_domains=7908,
        new_quarter_domains_executed_in_this_child=0,range_receipts=receipts,
        original_fixed_pilot_native_sha256=FIXED,reused_original_quarter_row_sha256=p['reused_quarter_row_sha256'],
        complete_parent_representation_decisions=decisions,
        new_coupled_complete_physical_cap_error=rec(mixed),
        all_complete_quarters_physical_cap_error=rec(quarter),
        original_pilot_complete_physical_cap_error=p['original_pilot_complete_physical_cap_error'],
        original_direct_coupled_baseline_physical_cap_error=p['original_direct_coupled_baseline_physical_cap_error'],
        selected_complete_physical_cap_error=rec(bound),selected_whole_representation=name,
        selected_complete_physical_error_data={k:rec(v) for k,v in used_errors.items()},
        selected_complete_fourteen_physical_fees={k:rec(v) for k,v in used_fees.items()},
        all_complete_quarters_fourteen_physical_fees={k:rec(v) for k,v in quarter_fees.items()},
        original_complete_physical_Green_gains=p['original_complete_physical_Green_gains'],
        original_six_boundary_errors_reused_without_recomputation=True,
        changing_coefficient_models_never_minimized_component_by_component=True,
        full_finite_mean_and_infinite_coefficient_remainders_retained=True,
        complete_true_cut_source_claimed=False,complete_finite193_response_error_proved=False,
        full_unknown_cap_error_operator_improved=False,complete_infinite_BVP_inverse_proved=False,
        original_target_or_trial_domains_recomputed=0)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--phase',choices=('range','finish'),required=True)
    for name in PLAN_INPUTS+('plan','resume','out','original-prefix','original-prefix-process'):p.add_argument('--'+name,type=Path)
    p.add_argument('--range-natives',type=Path,nargs='*',default=[])
    p.add_argument('--range-processes',type=Path,nargs='*',default=[])
    p.add_argument('--first',type=int,default=0);p.add_argument('--end',type=int,default=0)
    p.add_argument('--workflow-run',type=int,required=True);a=p.parse_args()
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!=PUBLIC:
        raise RuntimeError('new mathematics executes only in this public repository Actions')
    if a.out is None or a.out.exists():raise ValueError('a fresh output path is required')
    ctx.prec=320;ctx.cap=6;started=time.monotonic()
    names=RANGE_INPUTS if a.phase=='range' else ('plan',)
    if a.phase=='range' and (a.original_prefix is None or a.original_prefix_process is None):
        raise ValueError('the exact original one-quarter prefix and its actual process are mandatory')
    if any(getattr(a,k.replace('-','_')) is None for k in names):raise ValueError('a complete exact input is missing')
    inputs={k:sha(getattr(a,k.replace('-','_'))) for k in names}
    if a.phase!='range':
        for label,paths in (('range-native',a.range_natives),('range-process',a.range_processes)):
            inputs.update({label+'-'+str(i):sha(path) for i,path in enumerate(paths)})
    doc=dict(kind=KINDS[a.phase],phase=a.phase,source_sha256=sha(__file__),
        complete=False,failure=None,gates=[],input_sha256=inputs,
        complete_finite193_response_error_proved=False,complete_infinite_BVP_inverse_proved=False)
    if a.resume:
        old=read(a.resume)
        if (old.get('kind')==KINDS[a.phase] and old.get('source_sha256')==sha(__file__)
            and old.get('input_sha256')==inputs and proved(old)
            and (a.phase!='range' or old.get('range')==[a.first,a.end])):
            a.out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.resume,a.out)
            print(json.dumps(dict(original_complete_native_reused=True,new_domains_executed=0,
                native_sha256=sha(a.out))),flush=True);return
        if a.phase!='range':raise ValueError('only an exact complete original plan/finish may be reused')
    try:{'range':range_run,'finish':finish}[a.phase](a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(phase=a.phase,complete=doc['complete'],gates=len(doc['gates']),
        new_domains=doc.get('new_quarter_domains_executed_in_this_child',0),seconds=doc['seconds'])),flush=True)

if __name__=='__main__':main()
