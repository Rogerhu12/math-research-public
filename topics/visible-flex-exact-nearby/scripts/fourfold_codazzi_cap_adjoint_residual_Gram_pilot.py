#!/usr/bin/env python3
"""Four exact quarter domains of complete97 ordinary cap-adjoint residual Grams."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from flint import ctx
import fourfold_codazzi_cap_adjoint_residual_Gram_core as core
import fourfold_codazzi_cached_cap_adjoint_proposal_v2 as original
from fourfold_phase_metric_defect import record
from fourfold_codazzi_cap128_CI_worker import read,digest

KIND='actual_complete97_ordinary_physical_adjoint_residual_Gram_four_quarter_pilot_v1'
PUBLIC='Rogerhu12/math-research-public'
SOURCE_PROPOSAL='0bc067d92254b78e00b022beb455a30595b9713fba686639be78480c69685721'
WORKER_PROPOSAL='de387aaf02696fb1794cb0843028d898b0f3cde21bb3816e4e67199c0ca32368'
MANIFEST_PROPOSAL='af838e4127505e8744e140833f30037f8c4103dad08f2a11dc229932666045f3'
NATIVE_PROPOSAL='acb2151b60f24ad88b30e6f7d1d966851abc53c15e45df19df2bfca27c2393c7'
LABEL_PROPOSAL='new_complete257_state97_input_physical_adjoint_QR_from_original7908_cached_scalar_jets'
PILOT=(0,64,4096,7907)
ARRAY_KEYS=('finite_ordinary','full_coefficient_remainder','complete_Hessian_adjoint',
    'complete_formal_ordinary','complete_true_adjoint_ordinary',
    'trial_B','trial_C','trial_Btheta','trial_Ctheta')


def save(path,doc):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(doc,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
    temporary=path.with_suffix(path.suffix+'.partial')
    with temporary.open('wb') as stream:
        stream.write(gzip.compress(raw,mtime=0));stream.flush();os.fsync(stream.fileno())
    temporary.replace(path)


def canonical(value):
    return hashlib.sha256((json.dumps(value,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()


def gate(doc,name,passed):
    doc['gates'].append(dict(name=name,passed=bool(passed)))
    if not passed:raise ArithmeticError(name)


def valid_relative(value):
    path=Path(value)
    if path.is_absolute() or '..' in path.parts:raise ValueError('unsafe exact public array path')
    return path


def exact_proposal(a,original_inputs,doc):
    d,p=read(a.proposal),read(a.proposal_process)
    if (digest(a.proposal)!=NATIVE_PROPOSAL or not d.get('complete') or d.get('failure')
        or d.get('source_sha256')!=SOURCE_PROPOSAL
        or d.get('kind')!='actual_cached_scalar_complete97_physical_adjoint_Hermite_proposal_v2'
        or d.get('input_sha256')!=original_inputs
        or p.get('repository')!=PUBLIC or str(p.get('run_id'))!='43662865692'
        or str(p.get('run_attempt'))!='1'
        or p.get('worker_source_sha256')!=WORKER_PROPOSAL
        or p.get('input_manifest_sha256')!=MANIFEST_PROPOSAL
        or not any(x.get('sha256')==NATIVE_PROPOSAL for x in p.get('native_files',[]))
        or not any(x.get('label')==LABEL_PROPOSAL and x.get('actual_returncode')==0
            for x in p.get('children',[]))
        or len(d.get('gates',[]))!=5 or not all(x.get('passed') for x in d['gates'])
        or not d.get('actual_finite_backward_check',{}).get('passed')
        or d.get('mathematical_certificate') or d.get('complete_continuous_adjoint_bound_proved')
        or d.get('all_original7908_scalar_domains_recomputed')!=0
        or d.get('all_original64_native_points_recomputed')!=0):
        raise ValueError('the original actually completed full97 proposal is required')
    case=d['case'];folder=valid_relative(case)
    receipts=d.get('proposal_array_receipts',[])
    expected={'selected-intrinsic-proposal.npz',str(folder/'nodes.npy'),
        str(folder/'boundary-data.npz'),str(folder/'physical-adjoint-endpoints.npz'),
        str(folder/'matrix-RHS/state.npy'),str(folder/'matrix-RHS/derivative-left.npy'),
        str(folder/'matrix-RHS/derivative-right.npy')}
    if len(receipts)!=7 or {r['file'] for r in receipts}!=expected:
        raise ValueError('all seven exact original Hermite and boundary array receipts are required')
    for receipt in receipts:
        path=a.proposal_arrays/valid_relative(receipt['file'])
        if path.stat().st_size!=receipt['bytes'] or digest(path)!=receipt['sha256']:
            raise ValueError('one exact original scientific proposal array changed')
    directory=a.proposal_arrays/folder
    nodes0=np.load(directory/'nodes.npy',allow_pickle=False)
    state=np.load(directory/'matrix-RHS/state.npy',mmap_mode='r',allow_pickle=False)
    dl=np.load(directory/'matrix-RHS/derivative-left.npy',mmap_mode='r',allow_pickle=False)
    dr=np.load(directory/'matrix-RHS/derivative-right.npy',mmap_mode='r',allow_pickle=False)
    nodes=[Fraction.from_float(float(x)) for x in nodes0]
    gate(doc,'all_exact_shared_Hermite_arrays_and97_input_columns_match_the_completed_proposal',
        len(nodes)==1977 and state.shape==(1977,257,97)
        and dl.shape==dr.shape==(1976,257,97)
        and all(x<y for x,y in zip(nodes,nodes[1:]))
        and core.LEFT<=nodes[0]<=Fraction.from_float(float(core.LEFT))
        and nodes[-1]==core.RIGHT)
    return d,nodes,state,dl,dr


def save_npz(path,arrays):
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists():raise FileExistsError('preserve every exact original Gram/model array')
    temporary=path.with_suffix(path.suffix+'.partial')
    with temporary.open('wb') as f:
        np.savez_compressed(f,**arrays);f.flush();os.fsync(f.fileno())
    temporary.replace(path)
    return dict(file=path.name,sha256=digest(path),bytes=path.stat().st_size,
        exact_binary64_signed_triangles_and_complete_diagonal_slacks=True)


def actual_row(index,row,cached,nodes,state,dl,dr,hessian,arrays_root):
    started=time.monotonic();coefficient=cached.from_saved(row)
    left,right=coefficient['left'],coefficient['right']
    edges={left,right}
    edges.update(x for x in nodes if left<x<right)
    edges.update(x for item in hessian for x in item['interval'] if left<x<right)
    edges=sorted(edges);hleft=[x['interval'][0] for x in hessian]
    totals={key:core.zero() for key in ('finite','coefficient_remainder','hessian','B','C','Btheta','Ctheta')}
    pieces=[]
    for first,last in zip(edges,edges[1:]):
        exact,derivative,piece=core.hermite_subinterval(nodes,state,dl,dr,first,last)
        current=core.restrict_coefficient(coefficient,first,last)
        result=core.adjoint_cell_Grams(cached,current,exact,derivative)
        hi=bisect_right(hleft,first)-1;hr=hessian[hi]
        if not hr['interval'][0]<=first<last<=hr['interval'][1]:
            raise ValueError('a true local Hessian intersection is incomplete')
        hg,hw=core.Hessian_Gram(hr,result['fields'])
        totals['finite']=totals['finite']+result['finite']
        totals['coefficient_remainder']=totals['coefficient_remainder']+result['coefficient_remainder']
        totals['hessian']=totals['hessian']+hg
        for key in ('B','C','Btheta','Ctheta'):totals[key]=totals[key]+result['fields'][key]
        pieces.append(dict(interval=[str(first),str(last)],exact_Hermite_piece=piece,
            original_local_Hessian_row=hi,exact_coefficient_restriction=current['exact_affine_restriction'],
            complete_error_coefficients=result['complete_error_coefficients'],
            remainder_cauchy_weights=result['remainder_cauchy_weights'],Hessian_cauchy_weights=hw,
            finite_radial_degree=result['finite_radial_degree'],complete_physical_finite_support=256,
            finite_ordinary_trace=record(core.matrix_trace(result['finite'])),
            coefficient_remainder_trace=record(core.matrix_trace(result['coefficient_remainder'])),
            Hessian_adjoint_trace=record(core.matrix_trace(hg))))
    formal,fw=core.cauchy_Gram([('complete_finite',1,totals['finite']),
        ('complete_infinite_coefficient_remainder',1,totals['coefficient_remainder'])])
    true,tw=core.cauchy_Gram([('complete_finite',1,totals['finite']),
        ('complete_infinite_coefficient_remainder',1,totals['coefficient_remainder']),
        ('complete_actual_Hessian_adjoint',1,totals['hessian'])])
    gr={'finite_ordinary':totals['finite'],
        'full_coefficient_remainder':totals['coefficient_remainder'],
        'complete_Hessian_adjoint':totals['hessian'],'complete_formal_ordinary':formal,
        'complete_true_adjoint_ordinary':true}
    gr.update({'trial_'+k:totals[k] for k in ('B','C','Btheta','Ctheta')})
    arrays={};receipts={};trace={}
    for key,G in gr.items():
        bounded,receipt=core.covariance_enclosure(G,key,arrays)
        receipts[key]=receipt;trace[key]=record(core.matrix_trace(bounded))
    core.saved_model_arrays(coefficient,arrays)
    array=save_npz(arrays_root/f'adjoint-quarter-{index:04d}.npz',arrays)
    return dict(original_quarter_index=index,request=row['request'],interval=row['interval'],
        exact_original_quarter_row_sha256=canonical(row),
        actual_scalar_germ=row['actual_scalar_germ'],
        original_whole_jet_sha256=canonical(row['all_original_target_coefficients']),
        original_midpoint_jet_sha256=canonical(row['intrinsic_midpoint_jets']),
        physical_coefficient_model=cached.provider.row(coefficient),
        complete_Gram_receipts=receipts,complete_Gram_trace_uppers=trace,
        complete_radial_intersections=pieces,formal_cauchy_weights=fw,true_cauchy_weights=tw,
        new_array_receipt=array,source_physical_finite_support=256,all_infinite_coefficient_tails_retained=True,
        independent_even_mean_retained=True,original_intrinsic_target_calls=0,
        exact_first9over10_Hermite_extension_retained=True,
        seconds=time.monotonic()-started)


def validate_saved_row(row,index,original_row,root):
    if (row.get('original_quarter_index')!=index or row.get('request')!=original_row['request']
        or row.get('interval')!=original_row['interval']
        or row.get('exact_original_quarter_row_sha256')!=canonical(original_row)
        or set(row.get('complete_Gram_receipts',{}))!=set(ARRAY_KEYS)):
        raise ValueError('one saved successful quarter Gram has another exact scientific identity')
    receipt=row['new_array_receipt'];path=root/valid_relative(receipt['file'])
    if path.stat().st_size!=receipt['bytes'] or digest(path)!=receipt['sha256']:
        raise ValueError('one saved exact signed Gram/model array changed')
    with np.load(path,allow_pickle=False) as z:
        for key,value in row['complete_Gram_receipts'].items():
            if value['dimension']!=97 or z[value['array_key']].shape!=(4753,):
                raise ValueError('a saved complete97 signed Gram lost an input coordinate')
    return row


def run(a,doc):
    paths,rows,_=original.load_inputs(SimpleNamespace(input_index=a.input_index),doc)
    original_inputs=dict(doc['input_sha256'])
    pd,nodes,state,dl,dr=exact_proposal(a,original_inputs,doc)
    if digest(a.background)!=core.BACKGROUND or digest(a.local)!=core.LOCAL:
        raise ValueError('the exact original complete physical Hessian coefficient identities changed')
    point=read(paths['native-points']);background=read(a.background);local=read(a.local)
    hessian=core.actual_Hessian_coefficients(point,background,local)
    gates=core.algebra_gates()
    for name,passed in gates.items():gate(doc,name,passed)
    identity=dict(original_inputs=original_inputs,actual_proposal_native_sha256=digest(a.proposal),
        actual_proposal_process_sha256=digest(a.proposal_process),
        actual_proposal_array_receipts=pd['proposal_array_receipts'],
        original_complete_Hessian_local_native_sha256=digest(a.local),
        original_complete_physical_background_native_sha256=digest(a.background),
        core_source_sha256=digest(core.__file__),pilot_indices=list(PILOT))
    doc.update(exact_identity=identity,exact_identity_sha256=canonical(identity),rows=[],
        original_proposal_case=pd['case'],old_target_calls=0,completed_quarters=0,
        original_successful_adjoint_trial_recomputed=False,new_true_scalar_target_calls=0,
        complete7908_adjoint_cover_proved=False,complete_full_cap_high_to_low_bound_proved=False,
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False,
        physical_parameter='same fixed physical eta0, original nu, repaired M32 delta0')
    a.arrays.mkdir(parents=True,exist_ok=True)
    if a.resume:
        old=read(a.resume)
        if (old.get('kind')!=KIND or old.get('source_sha256')!=digest(__file__)
            or old.get('exact_identity')!=identity or old.get('failure')):
            raise ValueError('resume requires an unchanged successful mathematical quarter prefix')
        for i,row in enumerate(old.get('rows',[])):
            if i>=len(PILOT):raise ValueError('saved selected pilot exceeds its fixed request')
            doc['rows'].append(validate_saved_row(row,PILOT[i],rows[PILOT[i]],a.arrays))
        doc['reused_completed_quarters']=len(doc['rows'])
    else:doc['reused_completed_quarters']=0
    doc['completed_quarters']=len(doc['rows']);save(a.out,doc)
    cached=None
    for index in PILOT[len(doc['rows']):]:
        if cached is None:cached=core.CachedCoefficientProvider(paths['candidate'],paths['repair'])
        result=actual_row(index,rows[index],cached,nodes,state,dl,dr,hessian,a.arrays)
        doc['rows'].append(result);doc['completed_quarters']=len(doc['rows'])
        doc['new_completed_quarters_this_child']=len(doc['rows'])-doc['reused_completed_quarters']
        save(a.out,doc)
        print(json.dumps(dict(actual_complete_quarter=index,request=result['request'],
            finite=result['complete_Gram_trace_uppers']['finite_ordinary'],
            full_adjoint=result['complete_Gram_trace_uppers']['complete_true_adjoint_ordinary'],
            new_target_calls=0)),flush=True)
    gate(doc,'all_four_requested_actual_closed_quarters_have_complete_signed97_Grams',
        [r['original_quarter_index'] for r in doc['rows']]==list(PILOT)
        and all(r['independent_even_mean_retained'] and r['all_infinite_coefficient_tails_retained']
            for r in doc['rows']))
    gate(doc,'all_original7908_scalar_domains_and_all_old_trial_arrays_were_reused',
        cached is None or cached.old_target_calls==0)
    doc.update(complete=True,mathematical_certificate_for_listed_four_quarters_only=True,
        complete7908_adjoint_cover_proved=False,all_pilot_array_origins_in_public_Actions=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('input-index','proposal','proposal-process','proposal-arrays','background','local','arrays','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--resume',type=Path)
    a=p.parse_args();ctx.prec=256;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual mathematical pilot outcome')
    doc=dict(kind=KIND,source_sha256=digest(__file__),core_source_sha256=digest(core.__file__),
        repository=PUBLIC,complete=False,failure=None,gates=[],rows=[])
    try:run(a,doc)
    except Exception as error:doc['failure']=dict(type=type(error).__name__,message=str(error))
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps({k:doc.get(k) for k in ('kind','complete','failure','gates','seconds','completed_quarters')}),flush=True)
    if doc['failure']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
