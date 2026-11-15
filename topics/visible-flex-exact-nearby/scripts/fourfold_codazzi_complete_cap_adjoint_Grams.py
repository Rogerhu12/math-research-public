#!/usr/bin/env python3
"""Complete7908 same-proposal cap-adjoint Grams, reusing four actual pilot rows."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from flint import arb,ctx
import fourfold_codazzi_cap_adjoint_residual_Gram_core as core
import fourfold_codazzi_cap_adjoint_residual_Gram_pilot as pilot
import fourfold_codazzi_cached_cap_adjoint_proposal_v2 as original
from fourfold_codazzi_cap128_CI_worker import read,digest
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_bulk_box import Box

KIND='actual_complete7908_same_proposal_physical_adjoint_residual_Grams_v1'
PILOT_SOURCE='ae3b90c15e65343a0d5bdeb80cba4d6eb2a6f519155bff9a175b0f48a2f72310'
PILOT_WORKER='3f7c1f5862530cf13bda0a30466fc16998ef2a1f0f60ab97a8e5bc9506d81222'
PILOT_MANIFEST='467cd31f6d62b834d3a0cf07a1ef92efe1a2ef218e27d862140122c37a9ce71f'
PILOT_NATIVE='eb58b97ae182cedf621c4ff122b421ffb844e3839266a6a7d6df86b9134d8cfb'
CORE='689bf2c54350d832cffa7ca8f46dc424509fb221e3d73cb228a1f9a18130c0dc'
GROUPS=[(248*g,min(7908,248*(g+1))) for g in range(32)]
PILOTS=tuple(pilot.PILOT)
KEYS=tuple(pilot.ARRAY_KEYS)
save=pilot.save
canonical=pilot.canonical
gate=pilot.gate


def exact_pilot(a,rows,identity,doc):
    d,p=read(a.pilot),read(a.pilot_process)
    if (digest(a.pilot)!=PILOT_NATIVE or d.get('kind')!=pilot.KIND
        or not d.get('complete') or d.get('failure') or d.get('source_sha256')!=PILOT_SOURCE
        or d.get('core_source_sha256')!=CORE or d.get('exact_identity')!=identity
        or str(p.get('run_id'))!='43664278200' or str(p.get('run_attempt'))!='1'
        or p.get('repository')!=original.PUBLIC or p.get('worker_source_sha256')!=PILOT_WORKER
        or p.get('input_manifest_sha256')!=PILOT_MANIFEST
        or not any(x.get('sha256')==PILOT_NATIVE for x in p.get('native_files',[]))
        or not any(x.get('label')=='four_actual_closed_quarters_complete97_ordinary_adjoint_and_Hessian_Grams'
            and x.get('actual_returncode')==0 for x in p.get('children',[]))
        or len(d.get('gates',[]))!=9 or not all(g.get('passed') for g in d['gates'])):
        raise ValueError('the same successful four-quarter mathematical pilot is required')
    if [r['original_quarter_index'] for r in d['rows']]!=list(PILOTS):
        raise ValueError('the original four exact successful quarter indices changed')
    for r,i in zip(d['rows'],PILOTS):pilot.validate_saved_row(r,i,rows[i],a.pilot_arrays)
    gate(doc,'all_four_successful_signed97_pilot_quarters_and_exact_arrays_reused',True)
    return d


def small_json(path,d):
    raw=(json.dumps(d,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('one complete-Gram plaintext receipt exceeds60000 UTF8 bytes')
    path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_suffix(path.suffix+'.partial')
    tmp.write_bytes(raw);tmp.replace(path)


def raw_array_sha(value):
    a=np.ascontiguousarray(value,dtype='<f8')
    return hashlib.sha256(memoryview(a).cast('B')).hexdigest()


def npz_exact(path,arrays):
    if path.exists():
        with np.load(path,allow_pickle=False) as old:
            if set(old.files)!=set(arrays) or any(raw_array_sha(old[k])!=raw_array_sha(v)
                or old[k].shape!=v.shape for k,v in arrays.items()):
                raise ValueError('an existing exact original slice archive differs from its original bytes')
        return
    path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_suffix(path.suffix+'.partial')
    with tmp.open('wb') as out:
        np.savez_compressed(out,**arrays);out.flush();os.fsync(out.fileno())
    tmp.replace(path)


def file_entry(path,root):
    return dict(file=str(path.relative_to(root)),sha256=digest(path),bytes=path.stat().st_size)


def serialized_hessian(rows,point,local):
    result=[]
    for row in rows:
        i=row['local_index']
        result.append(dict(global_index=i,interval=list(map(str,row['interval'])),
            original_native_point_row_sha256=canonical(point['rows'][i]),
            original_local_row_sha256=canonical(local['rows'][i]),
            coefficients={k:record(row[k]) for k in ('Einf','E1','ZBB','ZBC','ZCC')}))
    return result


def original_identity(paths,pd,a):
    return dict(original_inputs={k:digest(v) for k,v in paths.items()},
        actual_proposal_native_sha256=digest(a.proposal),actual_proposal_process_sha256=digest(a.proposal_process),
        actual_proposal_array_receipts=pd['proposal_array_receipts'],
        original_complete_Hessian_local_native_sha256=digest(a.local),
        original_complete_physical_background_native_sha256=digest(a.background),
        core_source_sha256=digest(core.__file__),pilot_indices=list(PILOTS))


def prepare_bundle(group,rows,nodes,state,dl,dr,hessian,identity,root):
    first,end=GROUPS[group];requests=[i for i in range(first,end) if i not in PILOTS]
    left,right=Fraction(rows[first]['interval'][0]),Fraction(rows[end-1]['interval'][1])
    first_node=max(0,bisect_right(nodes,left)-1)
    last_piece=bisect_right(nodes,right)-1
    if last_piece==len(nodes)-1 or nodes[last_piece]==right:last_piece-=1
    if last_piece<first_node:raise ValueError('the original requested Hermite slice is empty')
    stop_node=last_piece+2
    if not ((nodes[first_node]<=left or first_node==0 and core.LEFT<=left<nodes[0])
        and right<=nodes[stop_node-1]):
        raise ValueError('one exact original node slice does not cover its whole requested interval')
    folder=root/f'range-{group:02d}';folder.mkdir(parents=True,exist_ok=True)
    selected=[rows[i] for i in requests]
    rowpath=folder/'exact-original-quarters.json.gz';save(rowpath,dict(indices=requests,rows=selected))
    local=[r for r in hessian if Fraction(r['interval'][0])<right and left<Fraction(r['interval'][1])]
    if not local:raise ValueError('the complete old Hessian source window is empty')
    hpath=folder/'exact-original-Hessian-coefficients.json.gz';save(hpath,dict(rows=local))
    arrays=dict(nodes=np.asarray([float(x) for x in nodes[first_node:stop_node]],dtype='<f8'),
        state=np.asarray(state[first_node:stop_node],dtype='<f8'),
        derivative_left=np.asarray(dl[first_node:stop_node-1],dtype='<f8'),
        derivative_right=np.asarray(dr[first_node:stop_node-1],dtype='<f8'))
    arrpath=folder/'exact-original-Hermite-slice.npz';npz_exact(arrpath,arrays)
    scalar_receipts={k:dict(shape=list(v.shape),dtype='<f8',raw_binary64_sha256=raw_array_sha(v))
        for k,v in arrays.items()}
    d=dict(kind='exact_original_adjoint_quarter_and_Hermite_byte_slice_v1',
        repository=original.PUBLIC,source_sha256=digest(__file__),object_identity_sha256=canonical(identity),
        group=group,range=[first,end],indices=requests,interval=[str(left),str(right)],
        original_global_first_node=first_node,original_global_stop_node=stop_node,
        exact_selected_array_receipts=scalar_receipts,
        original_proposal_native_sha256=pilot.NATIVE_PROPOSAL,
        original_full_proposal_array_receipts=identity['actual_proposal_array_receipts'],
        original_quarter_row_sha256=[canonical(r) for r in selected],
        original_Hessian_global_indices=[r['global_index'] for r in local],
        exact_source_files=[file_entry(x,folder) for x in (rowpath,hpath,arrpath)],
        no_numeric_target_or_trial_recomputation=True,
        all_node_values_and_derivatives_are_literal_original_binary64_slices=True)
    index=folder/'bundle-index.json';small_json(index,d)
    return dict(group=group,range=[first,end],requested_new_quarters=len(requests),
        bundle_index=file_entry(index,root),source_files=[file_entry(x,root) for x in (rowpath,hpath,arrpath)],
        original_global_first_node=first_node,original_global_stop_node=stop_node)


def plan_run(a,doc):
    paths,rows,_=original.load_inputs(SimpleNamespace(input_index=a.input_index),doc)
    pd,nodes,state,dl,dr=pilot.exact_proposal(a,{k:digest(v) for k,v in paths.items()},doc)
    if digest(a.local)!=core.LOCAL or digest(a.background)!=core.BACKGROUND:
        raise ValueError('the original same-centre full Hessian fields changed')
    point,local,background=read(paths['native-points']),read(a.local),read(a.background)
    identity=original_identity(paths,pd,a);p=exact_pilot(a,rows,identity,doc)
    hessian=serialized_hessian(core.actual_Hessian_coefficients(point,background,local),point,local)
    complete_input_sha=dict(identity['original_inputs'],proposal=digest(a.proposal),
        **{'proposal-process':digest(a.proposal_process),'local':digest(a.local),'background':digest(a.background),
        'pilot':digest(a.pilot),'pilot-process':digest(a.pilot_process)})
    doc.update(exact_object_identity=identity,object_identity_sha256=canonical(identity),
        actual_input_sha256=complete_input_sha,completed_bundles=0,bundles=[],
        original_complete_pilot_native_sha256=PILOT_NATIVE,original_complete_pilot_rows=p['rows'],
        pilot_array_receipts=[r['new_array_receipt'] for r in p['rows']],
        complete_quarter_origin_records=[dict(index=i,request=r['request'],interval=r['interval'],
            original_row_sha256=canonical(r)) for i,r in enumerate(rows)],
        all_original7908_scalar_targets_recomputed=0,all_original64_points_recomputed=0,
        original_adjoint_QR_or_Hermite_recomputed=False,new_Hessian_scalar_representations=1341)
    if a.resume:
        old=read(a.resume)
        if (old.get('kind')!=KIND or old.get('phase')!='plan' or old.get('source_sha256')!=digest(__file__)
            or old.get('exact_object_identity')!=identity or old.get('failure')):
            raise ValueError('the original unchanged successful bundle prefix is required')
        for item in old.get('bundles',[]):
            for f in [item['bundle_index'],*item['source_files']]:
                path=a.bundles/pilot.valid_relative(f['file'])
                if path.stat().st_size!=f['bytes'] or digest(path)!=f['sha256']:
                    raise ValueError('one completed original proposal byte slice changed')
            doc['bundles'].append(item)
        doc['completed_bundles']=len(doc['bundles'])
    save(a.out,doc)
    for group in range(len(doc['bundles']),32):
        entry=prepare_bundle(group,rows,nodes,state,dl,dr,hessian,identity,a.bundles)
        doc['bundles'].append(entry);doc['completed_bundles']=len(doc['bundles']);save(a.out,doc)
    gate(doc,'all32_exact_original_array_slices_cover_only7904_missing_quarters',
        len(doc['bundles'])==32 and sum(x['requested_new_quarters'] for x in doc['bundles'])==7904
        and len(doc['complete_quarter_origin_records'])==7908)
    doc.update(complete=True,new_intrinsic_target_calls=0,new_adjoint_trial_computations=0,
        complete7908_adjoint_cover_proved=False)


def read_plan(a):
    p=read(a.plan)
    if (p.get('kind')!=KIND or p.get('phase')!='plan' or p.get('source_sha256')!=digest(__file__)
        or not p.get('complete') or p.get('failure') or p.get('completed_bundles')!=32
        or p.get('original_complete_pilot_native_sha256')!=PILOT_NATIVE
        or not p.get('gates') or not all(g.get('passed') for g in p['gates'])
        or len(p.get('complete_quarter_origin_records',[]))!=7908):
        raise ValueError('the actual completed exact32 bundle plan is required')
    return p


def load_bundle(a,plan):
    group=a.group
    if not 0<=group<32:raise ValueError('invalid exact original range')
    desc=plan['bundles'][group]
    if desc['group']!=group or desc['range']!=list(GROUPS[group]):
        raise ValueError('one prepared range identity changed')
    index=a.bundle/'bundle-index.json'
    if digest(index)!=desc['bundle_index']['sha256']:raise ValueError('the exact prepared slice index changed')
    d=read(index)
    if (d.get('group')!=group or d.get('object_identity_sha256')!=plan['object_identity_sha256']
        or not d.get('all_node_values_and_derivatives_are_literal_original_binary64_slices')):
        raise ValueError('one original Hermite slice has another exact mathematical object')
    for item in d['exact_source_files']:
        path=a.bundle/pilot.valid_relative(item['file'])
        if path.stat().st_size!=item['bytes'] or digest(path)!=item['sha256']:
            raise ValueError('one actual original scalar, Hessian or trial slice changed')
    first,end=GROUPS[group];indices=[i for i in range(first,end) if i not in PILOTS]
    rr=read(a.bundle/'exact-original-quarters.json.gz')
    rows=rr['rows']
    if (rr['indices']!=indices or d['indices']!=indices or len(rows)!=len(indices)
        or [canonical(r) for r in rows]!=d['original_quarter_row_sha256']):
        raise ValueError('one original requested complete quarter changed or repeated a successful pilot')
    for index,row in zip(indices,rows):
        old=plan['complete_quarter_origin_records'][index]
        if (old['index']!=index or old['original_row_sha256']!=canonical(row)
            or old['request']!=row['request'] or old['interval']!=row['interval']):
            raise ValueError('a true original quarter is missing from its complete origin table')
    native=read(a.bundle/'exact-original-Hessian-coefficients.json.gz')
    hessian=[]
    for row in native['rows']:
        hessian.append(dict(local_index=row['global_index'],interval=list(map(Fraction,row['interval'])),
            **{k:core.positive(v) for k,v in row['coefficients'].items()}))
    if [r['local_index'] for r in hessian]!=d['original_Hessian_global_indices']:
        raise ValueError('one exact original Hessian interval index changed')
    if any(x['interval'][1]!=y['interval'][0] for x,y in zip(hessian,hessian[1:])):
        raise ValueError('the actual old local Hessian window has a gap')
    with np.load(a.bundle/'exact-original-Hermite-slice.npz',allow_pickle=False) as z:
        arrays={}
        for name,item in d['exact_selected_array_receipts'].items():
            value=np.asarray(z[name],dtype='<f8')
            if list(value.shape)!=item['shape'] or raw_array_sha(value)!=item['raw_binary64_sha256']:
                raise ValueError('one exact original node/value/derivative slice failed its raw-byte SHA')
            arrays[name]=value
    nodes=list(map(Fraction.from_float,map(float,arrays['nodes'])))
    n=len(nodes)
    if (arrays['state'].shape!=(n,257,97) or arrays['derivative_left'].shape!=(n-1,257,97)
        or arrays['derivative_right'].shape!=(n-1,257,97) or not all(x<y for x,y in zip(nodes,nodes[1:]))):
        raise ValueError('the complete257 by97 actual Hermite slice has invalid dimensions')
    left,right=map(Fraction,d['interval'])
    if not ((nodes[0]<=left or d['original_global_first_node']==0 and core.LEFT<=left<nodes[0])
        and right<=nodes[-1] and hessian[0]['interval'][0]<=left<right<=hessian[-1]['interval'][1]):
        raise ValueError('the true closed scalar range is not covered by its old trial and Hessian slices')
    return d,indices,rows,nodes,arrays,hessian


def range_run(a,doc):
    plan=read_plan(a);bundle,indices,rows,nodes,arrays,hessian=load_bundle(a,plan)
    if digest(a.candidate)!=core.CURRENT or digest(a.repair)!=original.REPAIR_NATIVE:
        raise ValueError('the exact complete candidate and continuous repair changed')
    identity=dict(plan_native_sha256=digest(a.plan),object_identity_sha256=plan['object_identity_sha256'],
        group=a.group,range=list(GROUPS[a.group]),bundle_index_sha256=digest(a.bundle/'bundle-index.json'),
        original_candidate_sha256=digest(a.candidate),original_repair_native_sha256=digest(a.repair),
        core_source_sha256=digest(core.__file__),pilot_actual_row_source_sha256=digest(pilot.__file__))
    gate(doc,'the_exact_original_scope_excludes_every_successful_pilot_quarter',
        not set(indices)&set(PILOTS) and len(indices)==plan['bundles'][a.group]['requested_new_quarters'])
    doc.update(exact_range_identity=identity,completed_quarters=0,rows=[],range=list(GROUPS[a.group]),
        group=a.group,requested_indices=indices,reused_completed_quarters=0,
        original_proposal_native_sha256=pilot.NATIVE_PROPOSAL,new_intrinsic_target_calls=0)
    if a.resume:
        old=read(a.resume)
        if (old.get('kind')!=KIND or old.get('phase')!='range'
            or old.get('source_sha256')!=digest(__file__)
            or old.get('exact_range_identity')!=identity or old.get('failure')):
            raise ValueError('an unchanged original successful mathematical range prefix is required')
        for j,row in enumerate(old.get('rows',[])):
            if j>=len(indices):raise ValueError('the saved successful range exceeds its original request')
            doc['rows'].append(pilot.validate_saved_row(row,indices[j],rows[j],a.arrays))
        doc['reused_completed_quarters']=len(doc['rows'])
    doc['completed_quarters']=len(doc['rows']);save(a.out,doc)
    cached=None
    for j in range(len(doc['rows']),len(indices)):
        if cached is None:cached=core.CachedCoefficientProvider(a.candidate,a.repair)
        result=pilot.actual_row(indices[j],rows[j],cached,nodes,arrays['state'],
            arrays['derivative_left'],arrays['derivative_right'],hessian,a.arrays)
        # Only index labels change from the immutable pilot calculation.
        # The literal original values, derivatives and mathematical formulas do not.
        for part in result['complete_radial_intersections']:
            part['exact_Hermite_piece']+=bundle['original_global_first_node']
            part['original_local_Hessian_row']=hessian[part['original_local_Hessian_row']]['local_index']
        result['complete_original_Hermite_slice_first_node']=bundle['original_global_first_node']
        doc['rows'].append(result);doc['completed_quarters']=len(doc['rows'])
        doc['new_completed_quarters_this_child']=len(doc['rows'])-doc['reused_completed_quarters']
        save(a.out,doc)
        print(json.dumps(dict(group=a.group,actual_complete_quarter=indices[j],
            true_Gram_trace=result['complete_Gram_trace_uppers']['complete_true_adjoint_ordinary'],
            original_target_calls=0)),flush=True)
    gate(doc,'every_requested_closed_quarter_has_its_complete_signed97_residual_Gram',
        [r['original_quarter_index'] for r in doc['rows']]==indices
        and all(r.get('independent_even_mean_retained') and r.get('all_infinite_coefficient_tails_retained')
            and r.get('original_intrinsic_target_calls')==0 for r in doc['rows']))
    gate(doc,'no_original_intrinsic_target_or_completed_pilot_quarter_recomputed',
        cached is None or cached.old_target_calls==0)
    doc.update(complete=True,mathematical_certificate_for_listed_range_only=True,
        complete7908_adjoint_cover_proved=False,complete_full_cap_high_to_low_bound_proved=False)


def restored_Gram(row,key,archive):
    item=row['complete_Gram_receipts'][key];data=np.asarray(archive[item['array_key']],dtype=float)
    if item['dimension']!=97 or data.shape!=(4753,):
        raise ValueError('one complete signed97 upper matrix changed dimensions')
    mid=np.zeros((97,97));ix=np.triu_indices(97);mid[ix]=data;mid[(ix[1],ix[0])]=data
    slack=float.fromhex(item['exact_diagonal_slack_binary64_hex'])
    if not np.isfinite(slack) or slack<0:raise ValueError('one true Gram diagonal slack is invalid')
    return Box(mid)+Box(np.eye(97)*slack)


def finish_run(a,doc):
    plan=read_plan(a);index=read(a.range_index)
    if (index.get('repository')!=original.PUBLIC or index.get('plan_native_sha256')!=digest(a.plan)
        or len(index.get('ranges',[]))!=32):
        raise ValueError('the exact32 actual successful range receipts are required')
    selected={}
    if (index.get('original_pilot_actual_process_sha256')
        !=plan['actual_input_sha256']['pilot-process']):
        raise ValueError('the exact original pilot artifact process changed')
    for group,item in enumerate(index['ranges']):
        if item['group']!=group:raise ValueError('the actual completed range list is not in canonical order')
        path=Path(item['native']);pp=Path(item['process']);d=read(path);p=read(pp)
        if (digest(path)!=item['native_sha256'] or digest(pp)!=item['actual_process_sha256']
            or d.get('kind')!=KIND or d.get('phase')!='range' or d.get('source_sha256')!=digest(__file__)
            or d.get('group')!=group or d.get('range')!=list(GROUPS[group])
            or d.get('exact_range_identity',{}).get('plan_native_sha256')!=digest(a.plan)
            or not d.get('complete') or d.get('failure') or not d.get('gates')
            or not all(x.get('passed') for x in d['gates'])
            or p.get('worker_source_sha256')!=index['worker_source_sha256']
            or p.get('input_manifest_sha256')!=index['manifest_sha256']
            or not any(x.get('sha256')==item['native_sha256'] for x in p.get('native_files',[]))
            or not (any(x.get('label')=='new_missing_complete97_adjoint_quarter_Grams'
                and x.get('actual_returncode')==0 for x in p.get('children',[]))
                or p.get('original_complete_success_reused_without_child')
                and p.get('original_success_process_sha256'))):
            raise ValueError('one full actual mathematical range identity or child receipt changed')
        requested=[j for j in range(*GROUPS[group]) if j not in PILOTS]
        if [r['original_quarter_index'] for r in d['rows']]!=requested:
            raise ValueError('one original successful pilot was recomputed or a new quarter is missing')
        for row in d['rows']:
            i=row['original_quarter_index']
            if i in selected:raise ValueError('one complete quarter was counted twice')
            selected[i]=(row,Path(item['arrays']),digest(path),digest(pp))
    for row in plan['original_complete_pilot_rows']:
        i=row['original_quarter_index']
        if i in selected or i not in PILOTS:raise ValueError('one exact original pilot was repeated')
        selected[i]=(row,a.pilot_arrays,PILOT_NATIVE,index['original_pilot_actual_process_sha256'])
    gate(doc,'all7908_original_closed_quarters_covered_once_with_exact_four_pilot_reuse',
        sorted(selected)==list(range(7908)) and len(selected)==7908)
    sums={key:core.zero() for key in KEYS};origins=[];cursor=core.LEFT
    for i in range(7908):
        row,arrays,native_sha,process_sha=selected[i];origin=plan['complete_quarter_origin_records'][i]
        if (row['interval']!=origin['interval'] or row['request']!=origin['request']
            or row['exact_original_quarter_row_sha256']!=origin['original_row_sha256']):
            raise ValueError('one original complete quarter or its full scalar identity changed')
        left,right=map(Fraction,row['interval'])
        if left!=cursor or not left<right:raise ValueError('the genuine full cap source intervals have a gap')
        cursor=right
        receipt=row['new_array_receipt'];path=arrays/pilot.valid_relative(receipt['file'])
        if path.stat().st_size!=receipt['bytes'] or digest(path)!=receipt['sha256']:
            raise ValueError('one actual signed97 Gram/model archive failed its exact receipt')
        with np.load(path,allow_pickle=False) as z:
            for key in KEYS:sums[key]=sums[key]+restored_Gram(row,key,z)
        origins.append(dict(index=i,interval=row['interval'],original_quarter_row_sha256=origin['original_row_sha256'],
            source_native_sha256=native_sha,actual_source_process_sha256=process_sha,
            certified_Gram_row_sha256=canonical(row),exact_array=receipt,
            reused_original_pilot=i in PILOTS))
    gate(doc,'true9over10_to25over8_radial_measure_mean_and_all_infinite_errors_retained',
        cursor==core.RIGHT and len(origins)==7908)
    arrays={};receipts={};trace={}
    for key,G in sums.items():
        H,entry=core.covariance_enclosure(G,key,arrays)
        receipts[key]=entry;trace[key]=record(core.matrix_trace(H))
    output=a.arrays/'complete7908-adjoint-residual-Grams.npz'
    array=pilot.save_npz(output,arrays)
    doc.update(complete=True,plan_native_sha256=digest(a.plan),exact_object_identity=plan['exact_object_identity'],
        complete_quarter_count=7908,original_successful_pilot_quarters_reused=4,new_quarters_from_actual_ranges=7904,
        original_successful_pilot_quarters_recomputed=0,complete_origin_receipts=origins,
        complete_signed97_Gram_receipts=receipts,complete_Gram_trace_uppers=trace,
        complete_Gram_HS_uppers={k:record(core.positive(v).sqrt().upper()) for k,v in trace.items()},
        complete_new_array_receipt=array,full_independent_even_mean_retained=True,
        mathematical_certificate_for_complete_ordinary_adjoint_body_Grams=True,
        complete7908_adjoint_cover_proved=True,new_intrinsic_target_calls=0,
        exact_true_interval=['9/10','25/8'],full_left_right_and_high_output_Grams_still_separate=True,
        complete_full_cap_high_to_low_bound_proved=False,complete_infinite_BVP_inverse_proved=False,
        true_parameter_Schur_proved=False)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--phase',choices=('plan','range','finish'),required=True)
    for name in ('input-index','proposal','proposal-process','proposal-arrays','background','local','pilot',
        'pilot-process','pilot-arrays','bundles','plan','bundle','candidate','repair','arrays','range-index','out','resume'):
        ap.add_argument('--'+name,type=Path,required=name=='out')
    ap.add_argument('--group',type=int)
    a=ap.parse_args();ctx.prec=256;ctx.cap=6;start=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every original full-cap Gram attempt')
    if digest(core.__file__)!=CORE or digest(pilot.__file__)!=PILOT_SOURCE:
        raise ValueError('the actual four-quarter mathematical formulas must remain exact')
    doc=dict(kind=KIND,phase=a.phase,source_sha256=digest(__file__),core_source_sha256=CORE,
        pilot_actual_row_source_sha256=PILOT_SOURCE,repository=original.PUBLIC,complete=False,
        failure=None,gates=[],complete_full_cap_high_to_low_bound_proved=False,
        complete_infinite_BVP_inverse_proved=False)
    try:
        if a.phase=='plan':plan_run(a,doc)
        elif a.phase=='range':range_run(a,doc)
        else:finish_run(a,doc)
    except Exception as error:doc['failure']=dict(type=type(error).__name__,message=str(error))
    finally:doc['seconds']=time.monotonic()-start;save(a.out,doc)
    print(json.dumps({k:doc.get(k) for k in ('kind','phase','complete','failure','gates',
        'seconds','completed_bundles','completed_quarters','complete_quarter_count')}),flush=True)
    if doc['failure']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
