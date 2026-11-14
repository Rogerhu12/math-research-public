#!/usr/bin/env python3
"""Fixed repaired-M32 body cross bands and weighted cached finite193 L2 Green.

Only exact candidate nonmean cubics and already certified scalar/Gram rows
are consumed. No target, old residual, mean flow, cap array, projector,
Riccati propagation, old Lyapunov exponential or scalar exponential is run.
"""
from __future__ import annotations
import argparse,json,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_candidate_shards import load_candidate
import fourfold_codazzi_complete_response_repair_source as original
import fourfold_codazzi_finite193_L2_Green_kernel as kernel

sha,read,save,canonical=kernel.sha,kernel.read,kernel.save,kernel.canonical
exact,interval,record=kernel.exact,kernel.interval,kernel.record
upper,positive,signed=kernel.upper,kernel.positive,kernel.signed
KIND='actual_fixed_M32_body_cross_bands_and_cached_weighted_L2_Green_v1'
KERNEL='ac4441cb98afabbbc646697434caebf464a22f702e2d0fa7d8e5910efd7ef448'
KERNEL_SOURCE='5b8f83906d36363266977441427add053a6ed05625525cfd000e05e03360b3db'
KERNEL_WORKER='368b9b0eb613fa7c508adcae6fb3fbd92193413ac879b1a7ab21d7721492f314'
KERNEL_MANIFEST='fb2336796edcd9ccc57a082015cdb6c51ee7c47a921ce03a3cbf3bbab6181ff6'
HIGH='5ad8aaada967f4626a33e978b1c81adf640ee1abaf0876f54ffd22d6dbd107fd'
HIGH_SOURCE='f9104cce14a3f04ebe3271ed19085d9bf4bdc7f9f7c215ed79dd99244e7034bf'
HIGH_WORKER='b11f7e85a555b3942d531ce120700c605d081a989abf320ff5758f70e8ee41cd'
HIGH_MANIFEST='de4bd52b27daceb5b3ea85a79c2ba37dd01196143384ffc72d0946dc6826a759'
HIGH_MATH_PROCESS='085a31c2f760df9076b0aa87672b05becaa1e699838bc14a71438c7592d38496'
HIGH_RECEIPT='cd7aa5f5c21509c629f8508bef21af4254e05716e2868e1804bce60e1ee583fa'
RECEIPT_WORKER='74a00ec426b897222424ca6a9241d7aa1f2d3b9763529fa2fd6be31671caecee'
CUBIC_SOURCE='6e4e8f1a3f69fdc06c15a0471cedb62abce0740b4825ddf5a0d04de4b984d7ad'
CANDIDATE=kernel.CANDIDATE
CENTRE=kernel.CENTRE
OBJECT='91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848'
ALPHA=Fraction(6890507429876859,9007199254740992)
NU=Fraction(-2572625729470897,72057594037927936)
FULL_RIGHT=Fraction(25,8)
RIGHT=kernel.RIGHT
PHASE_RIGHT=kernel.PHASE_RIGHT
INPUTS=('green','green-process','kernel','kernel-process','high','high-receipt',
        'high-receipt-process','high-math-process','candidate')
WINDOWS=('whole_inner_body','fixed_complete_negative_phase_window')


def gate(doc,name,ok):
    doc['gates'].append(dict(name=name,passed=bool(ok)))
    if not ok:raise ValueError('fixed-M32 body feedback: '+name)


def actual(p,run,worker,manifest,native):
    return (p.get('repository')=='Rogerhu12/math-research-public'
        and str(p.get('run_id'))==str(run) and p.get('complete') and not p.get('failure')
        and p.get('worker_source_sha256')==worker and p.get('input_manifest_sha256')==manifest
        and p.get('complete_native_sha256')==native and p.get('children')
        and all(c.get('actual_returncode')==0 for c in p['children']))


def validate(a,doc):
    green,events,weights=kernel.validate(a,doc)
    k,kp=read(a.kernel),read(a.kernel_process)
    gate(doc,'exact_successful_6391_signed_Gram_native_and_actual_artifact_process',
        sha(a.kernel)==KERNEL and sha(kernel.__file__)==KERNEL_SOURCE
        and k.get('kind')==kernel.KIND and k.get('source_sha256')==KERNEL_SOURCE
        and k.get('complete') and not k.get('failure')
        and actual(kp,43633074696,KERNEL_WORKER,KERNEL_MANIFEST,KERNEL)
        and len(k.get('gates',[]))==9 and all(g['passed'] for g in k['gates'])
        and k.get('input_sha256')=={'green':sha(a.green),'green-process':sha(a.green_process)}
        and k.get('complete_continuous_cells')==6391 and k.get('complete_projector_interfaces')==5970
        and k.get('complete_finite193_ordinary_L2_source_inverse_bound_proved')
        and k.get('derived_continuous_centre_definition_sha256')==CENTRE
        and k.get('original_candidate_sha256')==CANDIDATE
        and not k.get('complete_infinite_BVP_inverse_proved'))
    back=k.get('backward_kernel_rows',[]);forward=k.get('forward_kernel_event_rows',[])
    if len(back)!=len(events) or len(forward)!=len(events):
        raise ValueError('every original cached kernel event is required')
    for i,event in enumerate(events):
        b,f=back[i],forward[len(events)-1-i]
        if (not b.get('complete') or not f.get('complete')
            or b.get('original_event_index')!=i or f.get('original_event_index')!=i
            or b.get('original_event_sha256')!=canonical(event)
            or f.get('original_event_sha256')!=canonical(event)
            or b.get('kind')!=event['kind'] or f.get('kind')!=event['kind']):
            raise ValueError('a cached kernel row lost its exact old event identity')
        if event['kind']=='continuous':
            if (b.get('interval')!=event['interval'] or f.get('interval')!=event['interval']
                or b.get('exact_weight')!=event['exact_weight']
                or f.get('exact_weight')!=event['exact_weight']
                or f['whole_continuous_cell']['exact_length']!=event['port']['length']):
                raise ValueError('an original Gram or scalar whole-cell integral moved')
            G=kernel.matrix_read(b['new_Lyapunov_Gram'])
            if len(G)!=2 or any(len(row)!=2 for row in G):
                raise ValueError('the full two-row signed Gram is required')
            if not all(x.is_finite() for row in G for x in row):
                raise ValueError('an original signed Gram entry is nonfinite')
            for name in ('I_2lambda_z','I_lambda_p','I_2lambda_p'):
                positive(f['whole_continuous_cell'][name])
    gate(doc,'all_cached_12361_event_identities_and_whole_scalar_integrals_retained',True)

    high,hp,receipt,rp=(read(p) for p in
        (a.high,a.high_math_process,a.high_receipt,a.high_receipt_process))
    failure={'type':'ValueError','message':'small source evidence exceeds60000 bytes; preserve full native instead'}
    gate(doc,'original_high_mathematics_succeeded_before_preserved_optional_publication_failure',
        sha(a.high)==HIGH and sha(a.high_math_process)==HIGH_MATH_PROCESS
        and hp.get('repository')=='Rogerhu12/math-research-public'
        and str(hp.get('run_id'))=='43628921664' and hp.get('complete') is False
        and hp.get('failure')==failure and hp.get('worker_source_sha256')==HIGH_WORKER
        and hp.get('input_manifest_sha256')==HIGH_MANIFEST
        and len(hp.get('children',[]))==1 and hp['children'][0].get('actual_returncode')==0
        and high.get('kind')=='actual_complete_repaired_M32_known_high_source_from_Z_tail_v1'
        and high.get('source_sha256')==HIGH_SOURCE and high.get('complete') and not high.get('failure')
        and len(high.get('gates',[]))==8 and all(g['passed'] for g in high['gates'])
        and high.get('candidate_sha256')==CANDIDATE
        and high.get('derived_continuous_centre_definition_sha256')==CENTRE
        and high.get('coefficient_family_delta')=='0'
        and high.get('background_exact_mode_support')==32
        and high.get('exact_affine_parameter_offset')=='0')
    gate(doc,'exact_six_gate_zero_mathematics_receipt_preserves_the_original_complete_bytes',
        sha(a.high_receipt)==HIGH_RECEIPT
        and receipt.get('kind')=='exact_known_high_mathematical_success_then_diagnostic_size_failure_receipt_v1'
        and receipt.get('complete') and len(receipt.get('gates',[]))==6
        and all(g['passed'] for g in receipt['gates'])
        and receipt.get('original_native_sha256')==HIGH
        and receipt.get('original_actual_artifact_process_sha256')==HIGH_MATH_PROCESS
        and receipt.get('original_child_returncode')==0
        and receipt.get('new_mathematical_children')==0
        and receipt.get('new_source_rows')==0
        and rp.get('kind')=='actual_public_known_high_success_receipt_without_new_mathematics_v1'
        and rp.get('repository')=='Rogerhu12/math-research-public'
        and str(rp.get('run_id'))=='43630093667' and rp.get('complete') and not rp.get('failure')
        and rp.get('worker_source_sha256')==RECEIPT_WORKER
        and rp.get('input_manifest_sha256')==HIGH_MANIFEST
        and rp.get('complete_native_sha256')==HIGH and rp.get('children')==[]
        and rp.get('receipt_checks')==6)
    rows=high.get('rows',[]);edge=Fraction(0)
    for i,row in enumerate(rows):
        lo,hi=map(Fraction,row['interval'])
        if (row.get('common_row')!=i or not row.get('actual_tail_source_row_complete')
            or lo!=edge or not lo<hi):
            raise ValueError('the original closed7721 scalar cover changed')
        for name in ('full_repaired_background_A0','full_repaired_background_angular_A0',
                     'complete_beta_abs','complete_Kstar'):
            positive(row[name])
        edge=hi
    gate(doc,'same_complete_7721_coefficient_rows_with_full_mean_and_true_endpoints',
        len(rows)==7721 and edge==FULL_RIGHT and high.get('complete_original_common_rows')==7721
        and high.get('full_low193_and_independent_mean_unchanged')
        and high.get('all_original_low_and_independent_mean_bounds_retained_without_recomputation'))
    data=load_candidate(a.candidate);meta=json.loads(str(data['metadata']))
    nodes=[Fraction.from_float(float(x)) for x in data['radial_nodes']]
    gate(doc,'exact_same_M32_cubic_nonmean_mask_and_physical_alpha',
        sha(a.candidate)==CANDIDATE and sha(original.__file__)==CUBIC_SOURCE
        and data['piece_coefficients'].shape==(4,6144,65)
        and np.isfinite(data['piece_coefficients']).all()
        and len(nodes)==6145 and nodes[0]==0 and nodes[-1]==FULL_RIGHT
        and all(x<y for x,y in zip(nodes,nodes[1:]))
        and int(meta['modes'])==32 and meta['object_sha256']==OBJECT
        and Fraction.from_float(float(meta['amplitude']))==ALPHA
        and Fraction(meta['exact_float_nu'])==NU)
    E0=positive(high['exact_global_repair_fees']['centre_E0'])
    doc.update(original_candidate_sha256=CANDIDATE,
        derived_continuous_centre_definition_sha256=CENTRE,exact_affine_parameter_offset='0',
        coefficient_family_delta='0',physical_parameter='fixed original physical eta0 and original nu',
        exact_alpha=str(ALPHA),exact_nu=str(NU),background_exact_mode_support=32,
        exact_low_cross_band=[33,96],exact_high_cross_band=[97,160],
        low_and_high_cross_bands_real_dimensions=[128,128],
        full_independent_even_mean_retained=True,
        original_complete_L2_kernel_native_sha256=KERNEL,
        original_complete_scalar_coefficient_native_sha256=HIGH,
        complete_centre_repair_A0=record(E0),
        original_known_high_source_bounds_unchanged=high['complete_known_high_bounds'],
        all_true_cap_infinite_cross_blocks_remain_independent=True,
        high_cut_trace_is_an_independent_input_not_bounded_by_body_L2=True,
        unknown_high_BVP_inverse_and_global_Schur_still_required=True,
        actual_full_PDE_response_error_proved=False,complete_infinite_BVP_inverse_proved=False,
        true_parameter_Schur_proved=False,new_target_provider_calls=0,
        original_residual_mean_cap_or_trial_computations_repeated=0,
        original_6391_Gram_or_scalar_exponentials_recomputed=0,
        original_Riccati_projector_or_frame_calculations=0)
    return green,events,weights,k,rows,data,nodes,E0


def prefix(a,doc):
    if not a.resume:return None
    old=read(a.resume)
    if (old.get('kind')!=KIND or old.get('source_sha256')!=sha(__file__)
        or old.get('input_sha256')!=doc['input_sha256']):
        raise ValueError('a reused body-cross prefix has a different exact scientific identity')
    for name in ('body_cross_rows','weighted_backward_rows','weighted_forward_rows'):
        if any(r.get('complete') is not True for r in old.get(name,[])):
            raise ValueError('a reused prefix contains an incomplete row')
    doc['resumed_native_sha256']=sha(a.resume)
    doc['original_resume_failure_preserved']=old.get('failure')
    return old


def coefficient_rows(a,doc,old,rows,data,nodes,E0):
    saved=old.get('body_cross_rows',[]) if old else []
    if len(saved)>7721:raise ValueError('the reused body-cross prefix is too long')
    result=[];doc['body_cross_rows']=result
    for i,row in enumerate(rows):
        if i<len(saved):
            out=saved[i]
            if (out.get('common_row')!=i or out.get('interval')!=row['interval']
                or out.get('original_coefficient_row_sha256')!=canonical(row)):
                raise ValueError('a saved body-cross scalar row has changed its original input')
            result.append(out);continue
        left,right=map(Fraction,row['interval']);piece=row['original_response_piece']
        if not nodes[piece]<=left<right<=nodes[piece+1]:
            raise ValueError('the background Bernstein restriction crossed an original exact cubic')
        cube=data['piece_coefficients'][:,piece,:].copy()
        cube[:,32]=0
        if not np.all(cube[:,32]==0):raise ValueError('the exact nonmean mask failed')
        raw,_,_=original.cubic_pair_norms(cube,nodes[piece],left,right,32)
        nonmean=upper(abs(exact(ALPHA))*raw+E0)
        Q0=positive(row['full_repaired_background_A0'])
        Q1=positive(row['full_repaired_background_angular_A0'])
        B=positive(row['complete_beta_abs']);KS=positive(row['complete_Kstar'])
        whole=upper(Q0*Q0);modulated=upper(2*Q0*nonmean+nonmean*nonmean)
        D=min(whole,modulated).upper()
        primitive=upper(B*KS*Q0*Q1/130)
        LH=upper(163*B*KS*D+primitive)
        HL=upper(99*B*KS*D+primitive)
        if not all(x.is_finite() and x>=0 for x in (raw,nonmean,D,LH,HL)):
            raise ValueError('a complete cross-frequency scalar fee is invalid')
        result.append(dict(complete=True,common_row=i,interval=row['interval'],
            original_coefficient_row_sha256=canonical(row),original_candidate_piece=piece,
            raw_nonmean_candidate_A0=record(raw),full_repaired_nonmean_pair_A0=record(nonmean),
            full_repaired_background_A0=row['full_repaired_background_A0'],
            full_repaired_background_angular_A0=row['full_repaired_background_angular_A0'],
            complete_beta_abs=row['complete_beta_abs'],complete_Kstar=row['complete_Kstar'],
            whole_quadratic_fee=record(whole),constant_mean_removed_fee=record(modulated),
            selected_cross_quadratic_fee=record(D),complete_cross_primitive_fee=record(primitive),
            high_to_low_body_L2_multiplier=record(LH),low_to_high_body_L2_multiplier=record(HL),
            direct_whole_Q_high_to_low=record(upper(163*B*KS*whole+primitive)),
            direct_whole_Q_low_to_high=record(upper(99*B*KS*whole+primitive)),
            primitive_intermediate_cutoff=65,primitive_inverse_bound='1/260',
            constant_mean_removed_only_from_cross_block=True,
            full_low_mean_and_diagonal_terms_unchanged=True))
        if (i+1)%256==0:
            doc['actual_progress']=dict(phase='new_nonmean_cross_fees',rows=i+1,total=7721)
            save(a.out,doc);print(json.dumps(doc['actual_progress']),flush=True)
    gate(doc,'all7721_actual_cross_band_fees_completed_once',len(result)==7721)
    doc['reused_body_cross_scalar_rows']=len(saved)
    doc['new_body_cross_scalar_rows']=7721-len(saved)
    return result


def scalar_aggregate(rows,right):
    edge=Fraction(0);values={'LH':arb(0),'HL':arb(0)};where={}
    for row in rows:
        lo,hi=map(Fraction,row['interval'])
        if lo!=edge or not lo<hi:raise ValueError('a scalar aggregate lost the full original cover')
        edge=hi
        if lo>=right:continue
        for name,key in (('LH','high_to_low_body_L2_multiplier'),('HL','low_to_high_body_L2_multiplier')):
            value=positive(row[key])
            if value>values[name]:values[name]=value;where[name]=row['common_row']
    if edge!=FULL_RIGHT:raise ValueError('a scalar aggregate silently truncated the original body')
    return dict(exact_interval=['0',str(right)],
        high_to_low_ordinary_L2_multiplier=record(values['LH']),
        low_to_high_ordinary_L2_multiplier=record(values['HL']),
        maximum_rows=where,all_full_mean_rows_still_part_of_the_operator=True)


def cell_cross_fee(event,rows,lefts):
    lo,hi=map(Fraction,event['interval']);start=max(0,bisect_right(lefts,lo)-1)
    cursor=lo;values=[];identities=[]
    while start<len(rows) and Fraction(rows[start]['interval'][0])<hi:
        row=rows[start];a,b=map(Fraction,row['interval']);l,z=max(lo,a),min(hi,b)
        if l<z:
            if l!=cursor:raise ValueError('new coefficient rows fail an old continuous Green cell')
            values.append(positive(row['high_to_low_body_L2_multiplier']))
            identities.append(dict(common_row=row['common_row'],interval=list(map(str,(l,z))),
                new_cross_row_sha256=canonical(row)))
            cursor=z
        start+=1
    if cursor!=hi or not values:raise ValueError('the original whole continuous cell was not covered')
    return max(values).upper(),identities


def cached_whole(p,old,weight,gain,Zright2,Pleft2):
    """Use old integral upper bounds with the sign-correct max-exponential bound."""
    lz=signed(old['signed_lambda_z']);lp=signed(old['signed_lambda_p'])
    Iz=signed(old['I_2lambda_z']);Ip=signed(old['I_lambda_p']);Ip2=signed(old['I_2lambda_p'])
    if not all(x>=0 for x in (Iz,Ip,Ip2)):
        raise ValueError('a cached exact positive scalar integral is not nonnegative')
    iz,ip,ip2=upper(Iz),upper(Ip),upper(Ip2)
    # The old scalar records are upper bounds, not two-sided exact
    # integrals. For a negative rate the required max(1,exp) is1.
    # For a nonnegative rate, 1+lambda*I_upper is a valid growth bound.
    ez2=upper(1+2*max(arb(0),lz.upper())*iz)
    ep=upper(1+max(arb(0),lp.upper())*ip)
    rho=p['rho_whole_upper'];c=upper(p['c'])
    Zwhole2=upper(max(arb(1),ez2)*Zright2+weight*weight*(1+rho*rho)*iz)
    z=upper(Zwhole2.sqrt())
    ps=upper(max(arb(1),ep)*Pleft2.sqrt()+c*ip*z+weight*ip2.sqrt())
    qs=upper(rho*ps+z);squared=upper(gain*gain*(ps*ps+qs*qs))
    return squared,dict(
        original_whole_scalar_integral_record_sha256=canonical(old),
        signed_lambda_z=old['signed_lambda_z'],signed_lambda_p=old['signed_lambda_p'],
        I_2lambda_z=old['I_2lambda_z'],I_lambda_p=old['I_lambda_p'],
        I_2lambda_p=old['I_2lambda_p'],
        safe_max_exponential_bound='max(1,exp(lambda*h))<=1+max(0,lambda_upper)*I_upper',
        whole_z_kernel_square=record(Zwhole2),
        whole_weighted_p_kernel_norm=record(ps),whole_weighted_q_kernel_norm=record(qs),
        ordinary_pair_whole_kernel_square=record(squared),
        disjoint_future_and_local_input_squared=True,
        left_p_may_depend_on_local_input_no_false_independence=True,
        new_scalar_or_matrix_exponentials=0)


def weighted_sweeps(a,doc,old,green,events,weights,k,rows):
    saved=old.get('weighted_backward_rows',[]) if old else []
    savedforward=old.get('weighted_forward_rows',[]) if old else []
    if len(saved)>len(events) or len(savedforward)>len(events):
        raise ValueError('an original weighted prefix is too long')
    if savedforward and len(saved)!=len(events):
        raise ValueError('forward weighted source rows require complete backward source rows')
    lefts=[Fraction(r['interval'][0]) for r in rows]
    back=[];doc['weighted_backward_rows']=back;Z2=arb(0);newback=0
    for index,(event,krow) in enumerate(zip(events,k['backward_kernel_rows'])):
        p=kernel.port(event);a0=p['z_from_z'];esh=canonical(event)
        if index<len(saved):
            r=saved[index]
            if (r.get('original_event_index')!=index or r.get('original_event_sha256')!=esh
                or r.get('original_kernel_row_sha256')!=canonical(krow)):
                raise ValueError('a saved weighted backward row has a changed original identity')
            Z2=positive(r['z_left_kernel_square']);back.append(r);continue
        Zright2=Z2;newback+=1
        r=dict(complete=True,original_event_index=index,original_event_sha256=esh,
            original_kernel_row_sha256=canonical(krow),kind=event['kind'],
            z_right_kernel_square=record(Zright2))
        if event['kind']=='continuous':
            factor,cover=cell_cross_fee(event,rows,lefts)
            w=upper(positive(krow['ordinary_input_weight'])*factor)
            G=kernel.matrix_read(krow['new_Lyapunov_Gram'])
            q2=upper(w*w*a0*a0*kernel.quadratic(G,p['rho_right'],arb(-1)))
            Z2=upper(a0*a0*Zright2+q2)
            r.update(interval=event['interval'],exact_weight=event['exact_weight'],
                high_to_low_complete_closed_cell_fee=record(factor),coefficient_cover=cover,
                weighted_ordinary_input_factor=record(w),local_Q_kernel_square=record(q2),
                original_Gram_reused_without_new_exponential=True)
        else:
            Z2=upper(a0*a0*Zright2)
            r.update(radius=event['radius'],local_Q_kernel_square=record(arb(0)),
                original_secant_tangent_retained=True,new_interface_source_is_zero=True)
        r['z_left_kernel_square']=record(Z2);back.append(r)
        if (index+1)%256==0:
            doc['actual_progress']=dict(phase='weighted_cached_backward',events=index+1,total=len(events))
            save(a.out,doc);print(json.dumps(doc['actual_progress']),flush=True)
    gate(doc,'complete_cached_Gram_weighted_backward_cover',len(back)==12361)
    graph=green['complete_backward_graph']
    v=upper(positive(graph['D0'])/signed(graph['final_waist_closure_margin']).lower())
    W2=arb(0);sums={x:arb(0) for x in WINDOWS};maxs={x:arb(0) for x in WINDOWS}
    forward=[];doc['weighted_forward_rows']=forward;cells=0;newforward=0
    for order,(event,brow,krow,kf) in enumerate(zip(reversed(events),reversed(back),
            reversed(k['backward_kernel_rows']),k['forward_kernel_event_rows'])):
        index=len(events)-1-order;p=kernel.port(event)
        if order<len(savedforward):
            r=savedforward[order]
            if (r.get('forward_event_index')!=order or r.get('original_event_index')!=index
                or r.get('original_event_sha256')!=canonical(event)
                or r.get('original_kernel_forward_row_sha256')!=canonical(kf)
                or r.get('new_weighted_backward_row_sha256')!=canonical(brow)):
                raise ValueError('a weighted forward prefix lost its exact source/old-kernel identity')
            v=positive(r['v_right']);W2=positive(r['past_right_kernel_square'])
            sums={x:positive(y) for x,y in r['cumulative_ordinary_L2_kernel_squares'].items()}
            maxs={x:positive(y) for x,y in r['cumulative_ordinary_C0_kernel_squares'].items()}
            cells=r['continuous_cells_consumed'];forward.append(r);continue
        a0,b,kk=p['z_from_z'],p['p_from_p'],p['p_from_z']
        Zleft2=positive(brow['z_left_kernel_square']);Zright2=positive(brow['z_right_kernel_square'])
        vold,Wold=v,W2;vnew=upper(b*v*a0+kk);newforward+=1
        r=dict(complete=True,forward_event_index=order,original_event_index=index,
            original_event_sha256=canonical(event),kind=event['kind'],
            original_kernel_forward_row_sha256=canonical(kf),
            new_weighted_backward_row_sha256=canonical(brow),v_left=record(vold),
            past_left_kernel_square=record(Wold),z_left_kernel_square=record(Zleft2),
            z_right_kernel_square=record(Zright2))
        if event['kind']=='continuous':
            lo,hi=map(Fraction,event['interval']);wl,wr=map(Fraction,event['exact_weight'])
            w=positive(brow['weighted_ordinary_input_factor'])
            gain=positive(krow['ordinary_output_weight'])
            G=kernel.matrix_read(krow['new_Lyapunov_Gram']);rr=p['rho_right']
            combined=upper(w*w*kernel.quadratic(G,1+rr*vnew,-vnew))
            W2=upper(b*b*Wold+combined);Pleft2=upper(Wold+vold*vold*Zleft2)
            squared,whole=cached_whole(p,kf['whole_continuous_cell'],w,gain,Zright2,Pleft2)
            cells+=1;windows=['whole_inner_body']
            if hi<=PHASE_RIGHT:windows.append('fixed_complete_negative_phase_window')
            elif lo<PHASE_RIGHT:raise ValueError('the fixed original negative endpoint must remain an exact cut')
            for window in windows:
                sums[window]=upper(sums[window]+exact(hi-lo)*squared)
                maxs[window]=max(maxs[window],squared).upper()
            ln,lg=kernel.node_square(vold,Wold,Zleft2,p['rho_left'],exact(max(Fraction(1),1/wl)))
            rn,rg=kernel.node_square(vnew,W2,Zright2,upper(rr),exact(max(Fraction(1),1/wr)))
            r.update(interval=event['interval'],exact_weight=event['exact_weight'],
                combined_same_cell_Q_P_kernel_square=record(combined),
                whole_continuous_cell=whole,left_node_two_row_Gram=lg,right_node_two_row_Gram=rg)
            endpoints=((lo,ln),(hi,rn))
        else:
            W2=upper(b*b*Wold);radius=Fraction(event['radius'])
            gain=exact(max(Fraction(1),1/weights[radius]))
            ln,lg=kernel.node_square(vold,Wold,Zleft2,p['rho_left'],gain)
            rn,rg=kernel.node_square(vnew,W2,Zright2,upper(p['rho_right']),gain)
            r.update(radius=event['radius'],original_secant_tangent_retained=True,
                left_node_two_row_Gram=lg,right_node_two_row_Gram=rg,new_interface_source_is_zero=True)
            endpoints=((radius,ln),(radius,rn))
        for radius,square in endpoints:
            maxs['whole_inner_body']=max(maxs['whole_inner_body'],square).upper()
            if radius<=PHASE_RIGHT:
                maxs['fixed_complete_negative_phase_window']=max(maxs['fixed_complete_negative_phase_window'],square).upper()
        v=vnew
        r.update(v_right=record(v),past_right_kernel_square=record(W2),
            cumulative_ordinary_L2_kernel_squares={x:record(y) for x,y in sums.items()},
            cumulative_ordinary_C0_kernel_squares={x:record(y) for x,y in maxs.items()},
            continuous_cells_consumed=cells)
        forward.append(r)
        if (order+1)%256==0:
            doc['actual_progress']=dict(phase='weighted_cached_forward',events=order+1,
                total=len(events),continuous_cells=cells)
            save(a.out,doc);print(json.dumps(doc['actual_progress']),flush=True)
    gate(doc,'all6391_weighted_cells_all5970_true_jumps_and_virtual_waist_retained',
        len(forward)==12361 and cells==6391
        and sum(r['kind']=='interface' for r in forward)==5970)
    gate(doc,'complete_ordinary_L2_body_feedback_bounds_are_finite',
        all(x.is_finite() and x>=0 for x in list(sums.values())+list(maxs.values())))
    doc.update(
        complete_body_only_Green_high_to_low_L2_bounds={x:record(upper(y.sqrt())) for x,y in sums.items()},
        complete_body_only_Green_high_to_low_C0_bounds={x:record(upper(y.sqrt())) for x,y in maxs.items()},
        complete_continuous_cells=6391,complete_projector_interfaces=5970,
        reused_weighted_backward_events=len(saved),new_weighted_backward_events=newback,
        reused_weighted_forward_events=len(savedforward),new_weighted_forward_events=newforward)


def run(a,doc):
    green,events,weights,k,rows,data,nodes,E0=validate(a,doc);old=prefix(a,doc)
    newrows=coefficient_rows(a,doc,old,rows,data,nodes,E0)
    doc['complete_body_cross_multiplier_bounds']={
        'whole_body':scalar_aggregate(newrows,FULL_RIGHT),
        'whole_inner_body':scalar_aggregate(newrows,RIGHT),
        'fixed_complete_negative_phase_window':scalar_aggregate(newrows,PHASE_RIGHT)}
    weighted_sweeps(a,doc,old,green,events,weights,k,newrows)
    doc.update(complete=True,complete_original_common_rows=7721,
        exact_complete_coefficient_interval=['0',str(FULL_RIGHT)],
        exact_inner_BVP_interval=['0',str(RIGHT)],
        fixed_phase_error_norm_interval=['0',str(PHASE_RIGHT)],
        original_complete_finite193_L2_source_bounds=k['complete_ordinary_L2_source_to_L2_bounds'],
        original_complete_finite193_C0_source_bounds=k['complete_ordinary_L2_source_to_C0_bounds'],
        complete_fixed_M32_body_cross_operator_fees_proved=True,
        complete_body_only_weighted_Green_feedback_bound_proved=True,
        exact_full_PDE_parameter_response_error_proved=False,
        fixed_phase_root_upper_not_transferred_to_new_background=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in (*INPUTS,'out'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--resume',type=Path)
    a=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual body feedback outcome')
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        input_sha256={name:sha(getattr(a,name.replace('-','_'))) for name in INPUTS},
        body_cross_rows=[],weighted_backward_rows=[],weighted_forward_rows=[])
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:
        doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=True,scalar_rows=7721,continuous_cells=6391,
        body_feedback=doc['complete_body_only_Green_high_to_low_L2_bounds'],
        seconds=doc['seconds'],complete_infinite_inverse=False)),flush=True)


if __name__=='__main__':main()
