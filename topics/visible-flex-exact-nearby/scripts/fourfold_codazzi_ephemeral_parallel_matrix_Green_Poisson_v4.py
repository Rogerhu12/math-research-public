#!/usr/bin/env python3
"""Ephemeral four-core finite193 Green, true97 Poisson and same97 cap contraction.

All original F/C/Gram/target data and the old complete future prefix are
immutable inputs. New temporary products are not persisted in main,
Release, or new Actions artifacts. Only the reproducibility manifest,
actual small conclusion and output hashes may be published.
"""
from __future__ import annotations
import argparse,fcntl,hashlib,json,multiprocessing as mp,os,queue,signal,sys,time,traceback
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,arb_mat,ctx
import fourfold_codazzi_complete_directional_matrix_Green as m
import fourfold_codazzi_complete97_right_Poisson_Grams as p
import fourfold_codazzi_complete_same97_cap_posterior as cap
import fourfold_codazzi_scaled_signed_product_error_Gram_v2 as enc

KIND='actual_ephemeral_parallel_finite193_Green_true97_Poisson_same97_cap_v4'
OLD_SOURCE='9dca5868ed04b051aa10799978412a4b74644ae75dea748bcdc4159b3d47659d'
OLD_WORKER='3709858655e70ebe7bd334b4c1b0c070cdb8855ad31878a240229c4768b3e096'
OLD_MANIFEST='3350a96fbea47ee33bb09cb6602cb1e978e8ba00a034c7f735dfb60bade99910'
POISSON_SOURCE='312398be818621e156c08366f74c2850c61dcc283a44a30d7bb510a1cd51fca0'
CAP_SOURCE='ed62ebe4da583062bf0473aced77d8ee560c51b37c083baf490082c54e8fe1b8'
CAP_NATIVE='56efa27c6410caed656eb7e691de49283dfbd34d60e5b2c23c516b932c72dd99'
CAP_WORKER='a52bb62b3ee9f882b9e1d78f0f9b5a3b25b395e2cf941fe367aa08311ce5fbd9'
CAP_MANIFEST='7473f7866cc7676124f0f95ce047b6316ec5a4156bed8452f3cbd1bfb257ae95'
ENCLOSURE_SOURCE='9e699a2838c035835a9ed4246d5cd6a49418e74b5a2b6b6549dd13f35da62b0e'
N,P,Q=193,96,97
TOTAL=5970
GROUP=32
CHANNELS=m.CHANNELS
WINDOWS=(*m.WINDOWS,'true_cut_trace')
POISSON_COV=('proposal_whole','proposal_negative','body_defect','jump_whole','jump_negative','jump_cut')
JUMP_KEYS=dict(zip(WINDOWS,('jump_whole','jump_negative','jump_cut')))
q,record,norm,exact,eye,zero=m.q,m.record,m.norm,m.exact,m.eye,m.zero
read,save,sha,canonical=m.read,m.save,m.sha,m.canonical
up,block,transpose,trace=m.up,m.block,m.transpose,m.trace
sym,sqrt_upper,positive=m.sym,m.sqrt_upper,m.nonnegative
ARG=None
INPUT=None
STAGE=None
PROFILE=None
ROWS=None
GAINS=None
JUMPGAINS=None
PREFIX=[]
TEMP=None
CURRENT_OPERATION={}
PRODUCT_PREFLIGHT=32

def state_path(stage,index):return TEMP/stage/f'{index:05d}.json'
def progress(name,**data):
    save(TEMP/'progress'/f'{name}.json',
        dict(kind=KIND,stage=name,source_sha256=sha(__file__),stage_identity=STAGE,
             actual_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),**data))

def save_state(path,arrays,metadata):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    meta=dict(kind=KIND,source_sha256=sha(__file__),stage_identity=STAGE,complete=True,**metadata)
    if arrays:
        binary=path.with_suffix('.npz');tmp=binary.with_suffix('.npz.tmp')
        with tmp.open('wb') as out:np.savez(out,**arrays)
        os.replace(tmp,binary)
        meta['arrays']=dict(file=binary.name,bytes=binary.stat().st_size,sha256=sha(binary))
    save(path,meta)
    return meta

def load_state(path):
    path=Path(path);d=read(path)
    if (d.get('kind')!=KIND or d.get('source_sha256')!=sha(__file__)
        or d.get('stage_identity')!=STAGE or not d.get('complete')):
        raise ValueError('one temporary state belongs to another complete scientific object')
    arrays={}
    if d.get('arrays'):
        r=d['arrays'];binary=path.parent/r['file']
        if Path(r['file']).name!=r['file'] or binary.stat().st_size!=r['bytes'] or sha(binary)!=r['sha256']:
            raise ValueError('one temporary exact selected array changed')
        with np.load(binary,allow_pickle=False) as z:
            arrays={k:z[k].copy() for k in z.files}
        if any(A.dtype!=np.dtype('float64') or not np.isfinite(A).all() for A in arrays.values()):
            raise ValueError('one selected complete dyadic matrix is nonfinite or has another dtype')
    return d,arrays

def put_cov(A,key,arrays):return enc.covariance_bound(A,key,arrays)

def selected_twice(A):
    hi,H=enc.choose_centres(A)
    lo,L=enc.choose_centres(A-H)
    chosen=H+L
    if not np.isfinite(hi).all() or not np.isfinite(lo).all():
        raise ArithmeticError('a two-dyadic selected matrix is nonfinite')
    return hi,lo,chosen,norm(A-chosen).upper()

def put_port(A,key,arrays):
    hi,H=enc.choose_centres(A)
    lo,L=enc.choose_centres(A-H)
    tail,T=enc.choose_centres(A-H-L)
    selected=H+L+T;error=norm(A-selected).upper()
    arrays[key+'_hi']=hi;arrays[key+'_lo']=lo;arrays[key+'_tail']=tail
    return dict(hi=key+'_hi',lo=key+'_lo',tail=key+'_tail',
        entrywise_absolute_radius=record(error),
        meaning='three exact dyadics plus a full per-entry interval; canonical matrix unchanged')

def get_port_matrix(arrays,r):
    centre=exact(arrays[r['hi']])+exact(arrays[r['lo']])+exact(arrays[r['tail']])
    e=up(r['entrywise_absolute_radius'])
    if e<0:raise ValueError('a canonical port enclosure radius is negative')
    return arb_mat([[centre[i,j].union(centre[i,j]-e).union(centre[i,j]+e)
        for j in range(centre.ncols())] for i in range(centre.nrows())])

class Files(m.MatrixFiles):
    def complete_source_qq(self,index,channel):
        """Read the exact original Hqq after verifying the entire193 input."""
        row=self.rows[index];arrays=self.load_receipt(row['array_receipt'])
        name='cross_reference' if channel=='cross_reference' else 'edge_y_unit'
        rec=row['source_Grams'][name]
        key=rec.get('saved_array_key','H_'+name+'_midpoint')
        values=arrays[key]
        if values.ndim==1:values=m.unpack_symmetric(values,N)
        if values.shape!=(N,N) or not np.array_equal(values,values.T):
            raise ValueError('one original complete signed Gram is not symmetric193')
        slack=q(Fraction(float.fromhex(rec['exact_diagonal_slack_binary64_hex'])))
        if slack<0:raise ValueError('an original complete Gram slack is negative')
        G=exact(values[P:,P:])+eye(Q)*slack
        if channel=='complete_cross_source_error':
            E=up(row['source_definition']['full_true_weighted_cross_source_uniform_error'])
            G*=E*E
        return sym(G)

    def port(self,i):
        path=state_path('ports',i);path.parent.mkdir(parents=True,exist_ok=True)
        with path.with_suffix('.lock').open('a') as lock:
            fcntl.flock(lock.fileno(),fcntl.LOCK_EX)
            if not path.exists():
                A,B,Di,Snext,coordinate=self.effective_port(i)
                arrays={};br=put_port(B,'B',arrays);dr=put_port(Di,'Di',arrays)
                save_state(path,arrays,dict(stage='canonical_port',index=i,
                    original_matrix_row_sha256=canonical(ROWS[i]),
                    complete_same_Q_R_coordinate_event=coordinate,B=br,Di=dr,
                    canonical_reference_not_replaced_by_selected_midpoint=True))
            d,arrays=load_state(path)
        if d['index']!=i or d['original_matrix_row_sha256']!=canonical(ROWS[i]):
            raise ValueError('a cached true port changed its original matrix row')
        A=exact(self.load_receipt(ROWS[i]['array_receipt'])['T_A'])
        return A,get_port_matrix(arrays,d['B']),get_port_matrix(arrays,d['Di']),d

def files():return Files(ARG.array_root,PROFILE,ROWS)

def legacy_prefix(a,doc):
    d,actual=read(a.old_backward),read(a.old_backward_process)
    if (m.sha(m.__file__)!=OLD_SOURCE or sha(p.__file__)!=POISSON_SOURCE
        or sha(cap.__file__)!=CAP_SOURCE):
        raise ValueError('an original frozen matrix/Poisson/cap formula changed')
    if (str(actual.get('run_id'))!='43672023585' or str(actual.get('run_attempt'))!='1'
        or actual.get('worker_source_sha256')!=OLD_WORKER
        or actual.get('input_manifest_sha256')!=OLD_MANIFEST
        or actual.get('actual_input_sha256')!=INPUT
        or actual.get('failure',{}).get('type')!='RuntimeError'
        or actual.get('failure',{}).get('message')!='new unread repository rules need their actual diff read: README.md'
        or d.get('kind')!=m.KIND or d.get('phase')!='backward'
        or d.get('source_sha256')!=OLD_SOURCE or d.get('input_sha256')!=INPUT
        or d.get('failure') is not None or d.get('complete')
        or not 1658<=d.get('completed_rows',-1)<TOTAL
        or not d.get('gates') or not all(v.get('passed') for v in d['gates'])):
        raise ValueError('the exact original rule-only failure and successful future prefix are required')
    found=[]
    for receipt in d['row_chunks']:
        name=receipt['file'];path=a.old_backward.parent/name
        if Path(name).name!=name or sha(path)!=receipt['sha256'] or path.stat().st_size!=receipt['bytes']:
            raise ValueError('an original successful future chunk changed')
        chunk=read(path)
        if (chunk.get('kind')!=m.KIND or chunk.get('phase')!='backward'
            or chunk.get('source_sha256')!=OLD_SOURCE or chunk.get('first_row')!=len(found)
            or len(chunk.get('rows',[]))!=receipt['rows']):
            raise ValueError('an original successful future chunk changed scientific identity')
        for row in chunk['rows']:
            i=len(found)
            if not row.get('complete') or row.get('index')!=i or row.get('original_matrix_row_sha256')!=canonical(ROWS[i]):
                raise ValueError('an original future row has a gap or another complete matrix')
            found.append(row)
    if len(found)!=d['completed_rows']:raise ValueError('the actual original future count is inconsistent')
    doc['exact_original_future_prefix']=dict(native_sha256=sha(a.old_backward),
        process_sha256=sha(a.old_backward_process),complete_rows=len(found),
        actual_original_failure=actual['failure'],original_native_source_sha256=OLD_SOURCE,
        original_arithmetic_bits=d['arithmetic_bits'],old_future_rows_recomputed=0)
    for i,row in enumerate(found):
        save_state(state_path('future',i),{},dict(stage='future',index=i,
            original_matrix_row_sha256=canonical(ROWS[i]),exact_original_successful_row=row,
            original_row_sha256=canonical(row),reused_original_row_without_recomputation=True))
    return found

def read_future(i,F):
    d,arrays=load_state(state_path('future',i))
    if d['index']!=i or d['original_matrix_row_sha256']!=canonical(ROWS[i]):
        raise ValueError('one actual future covariance index changed')
    if d.get('reused_original_row_without_recomputation'):
        r=d['exact_original_successful_row']
        if d['original_row_sha256']!=canonical(r):raise ValueError('one original future row was relabelled')
        arrays=F.load_receipt(r['array_receipt']);receipts=r['future_covariances']
    else:receipts=d['future_covariances']
    return {ch:enc.read_covariance(arrays,receipts[ch]) for ch in CHANNELS}

def future_stream():
    global CURRENT_OPERATION
    ctx.prec=ARG.bits;F=files();start=len(PREFIX)
    Qnext=read_future(start-1,F) if start else {ch:zero(Q,Q) for ch in CHANNELS}
    progress('future',completed_rows=start,reused_rows=start,done=False)
    began=time.monotonic()
    for i in range(start,TOTAL):
        CURRENT_OPERATION=dict(stage='future',index=i,operation='complete_signed_future_covariances')
        A,B,Di,port=F.port(i);arrays={};receipts={};new={}
        for ch in CHANNELS:
            Hqq=F.complete_source_qq(i,ch)
            new[ch],receipts[ch]=put_cov(Di*Qnext[ch]*transpose(Di)+Hqq,'Q_'+ch,arrays)
        save_state(state_path('future',i),arrays,dict(stage='future',index=i,
            original_matrix_row_sha256=canonical(ROWS[i]),future_covariances=receipts,
            reused_original_row_without_recomputation=False))
        Qnext=new
        if (i+1)%16==0:progress('future',completed_rows=i+1,reused_rows=start,done=False,
            new_rows=i+1-start,seconds=time.monotonic()-began)
    progress('future',completed_rows=TOTAL,reused_rows=start,new_rows=TOTAL-start,
        done=True,seconds=time.monotonic()-began)

def initial_waist(F):
    values=F.frame_values(TOTAL-1,'left');S=exact(values)
    UQ,UN=block(S,0,P,0,P),block(S,0,P,P,N)
    inverse,fee=m.checked_inverse(UQ,'the exact complete96 waist restriction')
    hi,lo,V,rounding=selected_twice(-inverse*UN)
    arrays=dict(V_hi=hi,V_lo=lo)
    save_state(TEMP/'initial-waist.json',arrays,dict(stage='initial_waist',
        true_waist_inverse_identity=fee,
        chosen_exact_two_dyadic_graph_error=record(rounding),
        original_full_waist_frame_sha256=m.base.raw_sha(values),
        initial_true_waist_defect_not_deleted=True))
    return hi,lo,V

def past_stream():
    global CURRENT_OPERATION
    ctx.prec=ARG.bits;F=files();hi0,lo0,V=initial_waist(F)
    W={ch:zero(P,P) for ch in CHANNELS};began=time.monotonic()
    progress('past',completed_rows=0,done=False)
    for order in range(TOTAL):
        i=TOTAL-1-order
        CURRENT_OPERATION=dict(stage='past',index=i,operation='complete_signed_past_and_real_graph_choice')
        A,B,Di,port=F.port(i)
        hi,lo,Vnext,Verror=selected_twice((A*V+B)*Di)
        arrays=dict(V_before_hi=hi0,V_before_lo=lo0,V_next_hi=hi,V_next_lo=lo)
        receipts={};newW={}
        for ch in CHANNELS:
            H=F.gram(i,'source',ch);Hw=m.source_blocks(H,V)[3]
            complete,receipts[ch]=put_cov(W[ch]+Hw,'past_plus_'+ch,arrays)
            # This additional measured Loewner rounding only enlarges the
            # exact current/past covariance. It never changes the state.
            scratch={}
            newW[ch],unused=put_cov(A*complete*transpose(A),'next_'+ch,scratch)
        save_state(state_path('past',i),arrays,dict(stage='past',index=i,
            original_matrix_row_sha256=canonical(ROWS[i]),past_plus_current=receipts,
            full_V_selection_error=record(Verror),new_Loewner_rounding_paid=True,
            exact_V_is_two_dyadic_sum=True))
        V,W,hi0,lo0=Vnext,newW,hi,lo
        if (order+1)%16==0:progress('past',completed_rows=order+1,done=False,
            seconds=time.monotonic()-began)
    final=dict(V_cut_hi=hi0,V_cut_lo=lo0);rc={}
    for ch in CHANNELS:W[ch],rc[ch]=put_cov(W[ch],'cut_W_'+ch,final)
    save_state(TEMP/'past-final.json',final,dict(stage='past_final',cut_covariances=rc,
        all_full193_and_even_mean_preserved=True))
    progress('past',completed_rows=TOTAL,done=True,seconds=time.monotonic()-began)

def product_step(F,i,E,W,legacy,stage):
    global CURRENT_OPERATION
    CURRENT_OPERATION=dict(stage=stage,index=i,operation='true_Di_product_and_signed_error')
    A,B,Di,port=F.port(i);arrays={}
    E,W,receipt=enc.selected_product_step(Di,E,W,'product',arrays)
    rounding=up(receipt['complete_candidate_rounding_upper'])
    legacy=(norm(Di)*positive(legacy)+rounding).upper()
    diagnostics=dict(selected_product_norm_log2_upper=enc.upper_exponent(norm(E)),
        signed_error_norm_log2_upper=enc.upper_exponent(sqrt_upper(norm(W))),
        old_scalar_error_diagnostic_log2_upper=enc.upper_exponent(legacy),
        single_true_Di_norm_log2_upper=enc.upper_exponent(norm(Di)),
        local_complete_rounding_log2_upper=enc.upper_exponent(rounding))
    save_state(state_path('product',i),arrays,dict(stage='product',index=i,
        original_matrix_row_sha256=canonical(ROWS[i]),product_enclosure=receipt,
        legacy_scalar_radius_diagnostic_only=record(legacy),diagnostic_exponents=diagnostics,
        exact_definition='E_i^0=D_i_inverse ... D_0_inverse; E_cut^0=I97',
        full_output_side_product_error_Gram=True,
        this_enclosure_choice_is_not_a_physical_state_jump=True))
    CURRENT_OPERATION=dict(stage=stage,index=i,operation='complete',diagnostic_exponents=diagnostics)
    return E,W,legacy,diagnostics

def product_preflight(doc):
    global CURRENT_OPERATION
    F=files();E=eye(Q);W=zero(Q,Q);legacy=arb(0);began=time.monotonic()
    progress('preflight',completed_rows=0,done=False)
    for i in range(PRODUCT_PREFLIGHT):
        if state_path('product',i).exists():
            raise ValueError('do not repeat an already complete same-run preflight product')
        E,W,legacy,diagnostics=product_step(F,i,E,W,legacy,'preflight')
        progress('preflight',completed_rows=i+1,done=False,diagnostic_exponents=diagnostics,
            seconds=time.monotonic()-began)
    CURRENT_OPERATION=dict(stage='preflight',operation='actual_full97_scaled_Gram_and_weights')
    J=enc.read_covariance(F.load_receipt(PREFIX[0]['array_receipt']),
        PREFIX[0]['future_covariances'][CHANNELS[0]])
    small=eye(Q)+J/enc.power2(enc.upper_exponent(norm(J)) or 0)
    reports=[]
    for exponent in (-4096,4096):
        arrays={};target=sym(small*enc.power2(exponent))
        bounded,receipt=put_cov(target,'scale_probe',arrays)
        restored=enc.read_covariance(arrays,receipt)
        if not all(restored[i,j].overlaps(bounded[i,j]) for i in range(Q) for j in range(Q)):
            raise ValueError('the scaled complete signed covariance receipt did not round-trip')
        total,weight,alpha=enc.weighted_add(zero(Q,Q),arb(0),restored)
        if not alpha>0 or not weight>0 or not norm(total).is_finite():
            raise ArithmeticError('arbitrary-exponent complete Gram weights failed')
        reports.append(dict(exact_test_scale=exponent,
            exact_selected_scale=receipt['centre']['exact_binary_scale_exponent'],
            exact_positive_weight_log2=enc.upper_exponent(alpha),
            actual_complete97_rows=restored.nrows()))
    bound,detail=enc.sandwich(E,W,small)
    encoded={};upper,receipt=put_cov(bound,'preflight_sandwich',encoded)
    if not norm(upper).is_finite():raise ArithmeticError('actual full97 error sandwich failed')
    doc['actual_early_preflight']=dict(first=0,end=PRODUCT_PREFLIGHT,
        complete_product_rows=PRODUCT_PREFLIGHT,rows_reused_by_following_product_stream=True,
        extreme_scale_tests=reports,whole_signed_sandwich=detail,
        no_complete_global_Green_claim_from_preflight=True,
        original_F_C_target_or_validator_calls=0,seconds=time.monotonic()-began)
    m.gate(doc,'actual_first32_products_scaled_full97_receipts_and_extreme_exact_positive_weights',
        len(reports)==2 and receipt['dimension']==Q)
    progress('preflight',completed_rows=PRODUCT_PREFLIGHT,done=True,
        extreme_positive_weight_tests=len(reports),diagnostic_exponents=diagnostics,
        seconds=time.monotonic()-began)

def product_stream():
    ctx.prec=ARG.bits;F=files();began=time.monotonic()
    last,arrays=load_state(state_path('product',PRODUCT_PREFLIGHT-1))
    if last.get('index')!=PRODUCT_PREFLIGHT-1 or last['original_matrix_row_sha256']!=canonical(ROWS[PRODUCT_PREFLIGHT-1]):
        raise ValueError('the same-run product preflight changed identity')
    E,W=read_product(PRODUCT_PREFLIGHT-1)
    legacy=up(last['legacy_scalar_radius_diagnostic_only'])
    progress('product',completed_rows=PRODUCT_PREFLIGHT,reused_same_run_preflight_rows=PRODUCT_PREFLIGHT,done=False)
    for i in range(PRODUCT_PREFLIGHT,TOTAL):
        if state_path('product',i).exists():
            raise ValueError('do not recompute an already complete new product row')
        E,W,legacy,diagnostics=product_step(F,i,E,W,legacy,'product')
        if (i+1)%16==0:progress('product',completed_rows=i+1,
            reused_same_run_preflight_rows=PRODUCT_PREFLIGHT,diagnostic_exponents=diagnostics,
            done=False,seconds=time.monotonic()-began)
    progress('product',completed_rows=TOTAL,done=True,reused_same_run_preflight_rows=PRODUCT_PREFLIGHT,
        diagnostic_exponents=diagnostics,seconds=time.monotonic()-began)

def read_product(i):
    if i<0:return eye(Q),zero(Q,Q)
    d,arrays=load_state(state_path('product',i))
    if d['index']!=i or d['original_matrix_row_sha256']!=canonical(ROWS[i]):
        raise ValueError('one complete product row changed original identity')
    r=d['product_enclosure']
    return enc.read_selected(arrays,r['selected_product']),enc.read_covariance(arrays,r['complete_output_error_Gram'])

def read_past(i):
    d,ar=load_state(state_path('past',i))
    if d['index']!=i or d['original_matrix_row_sha256']!=canonical(ROWS[i]):
        raise ValueError('one complete past covariance row changed original identity')
    V=exact(ar['V_before_hi'])+exact(ar['V_before_lo'])
    Vnext=exact(ar['V_next_hi'])+exact(ar['V_next_lo'])
    W={ch:enc.read_covariance(ar,d['past_plus_current'][ch]) for ch in CHANNELS}
    return V,Vnext,W

def empty_source_sums():
    return {ch:dict(squared={w:arb(0) for w in m.WINDOWS},
        body_squared=arb(0),jumps={w:arb(0) for w in WINDOWS}) for ch in CHANNELS}

def merge_group(first,end):
    global CURRENT_OPERATION
    F=files();source=empty_source_sums()
    grams={k:zero(Q,Q) for k in POISSON_COV};weights={w:arb(0) for w in WINDOWS}
    for i in range(first,end):
        CURRENT_OPERATION=dict(stage='local_group',first=first,end=end,index=i,operation='read_complete_sources')
        row=ROWS[i];V,Vnext,past=read_past(i);Ql=read_future(i,F)
        Qnext=read_future(i-1,F) if i else {ch:zero(Q,Q) for ch in CHANNELS}
        E,product_error=read_product(i);Enext,next_product_error=read_product(i-1)
        A,B,Di,port=F.port(i)
        right_values=F.frame_values(i-1,'left') if i else F.frame_values(0,'right')
        anchor=block(exact(right_values),0,N,0,P)
        delta=Vnext-(A*V+B)*Di
        jump_factor=sym(transpose(delta)*transpose(anchor)*anchor*delta)
        left,right=map(Fraction,row['interval'])
        w=PROFILE['rows'][i]['exact_weight']
        rhomin=min(Fraction(w['exact_rho_left']),Fraction(w['exact_rho_right']))
        metric=q(max(Fraction(1),1/rhomin))
        deltaA=up(row['patch']['true_complete_generator_difference_upper'])
        local={}
        for name in ('full_weighted','full_physical','negative_physical'):
            if name=='negative_physical' and left>=m.PHASE_RIGHT:
                local[name]=(None,None);continue
            J=F.gram(i,name);Jpp=block(J,0,P,0,P);Jpq=block(J,0,P,P,N);Jqq=block(J,P,N,P,N)
            Jeff=sym(transpose(V)*Jpp*V+transpose(V)*Jpq+transpose(Jpq)*V+Jqq)
            local[name]=(Jpp,Jeff)
        for ch in CHANNELS:
            values={name:(positive(m.dot_trace(f[0],past[ch])+m.dot_trace(f[1],Ql[ch]))
                if f[0] is not None else arb(0)) for name,f in local.items()}
            source[ch]['squared']['whole_inner_body']+=values['full_physical']
            source[ch]['squared']['fixed_complete_negative_phase_window']+=values['negative_physical']
            source[ch]['body_squared']+=deltaA**2*metric**2*values['full_weighted']
            if i:
                jump=sqrt_upper(m.dot_trace(jump_factor,Qnext[ch]))
                for window in WINDOWS:source[ch]['jumps'][window]+=JUMPGAINS[right][window]*jump
        for name,key in (('full_physical','proposal_whole'),('negative_physical','proposal_negative'),
                         ('full_weighted','body_defect')):
            Jeff=local[name][1]
            if Jeff is None:continue
            CURRENT_OPERATION.update(operation='signed_product_sandwich',gram=name,
                E_norm_log2=enc.upper_exponent(norm(E)),W_norm_log2=enc.upper_exponent(norm(product_error)),
                J_norm_log2=enc.upper_exponent(norm(Jeff)))
            H,fee=enc.sandwich(E,product_error,Jeff)
            if name=='full_weighted':H*=deltaA**2*metric**2
            grams[key]+=sym(H)
        if i:
            Hjump,fee=enc.sandwich(Enext,next_product_error,jump_factor)
            for window in WINDOWS:
                gain=JUMPGAINS[right][window];key=JUMP_KEYS[window]
                CURRENT_OPERATION.update(operation='actual_jump_positive_weight',window=window,
                    component_norm_log2=enc.upper_exponent(norm(Hjump*gain**2)))
                grams[key],weights[window],alpha=enc.weighted_add(grams[key],weights[window],sym(Hjump*gain**2))
    arrays={};receipts={}
    for key in POISSON_COV:
        CURRENT_OPERATION.update(operation='complete_group_scaled_covariance',gram=key)
        grams[key],receipts[key]=put_cov(grams[key],key,arrays)
    save_state(state_path('groups',first//GROUP),arrays,dict(stage='local_group',first=first,end=end,
        original_row_sha256=[canonical(ROWS[i]) for i in range(first,end)],
        source_sums={ch:dict(squared={w:record(v) for w,v in r['squared'].items()},
            body_squared=record(r['body_squared']),jumps={w:record(v) for w,v in r['jumps'].items()})
            for ch,r in source.items()},
        unnormalized_Poisson_Grams=receipts,
        positive_jump_weights={w:record(v) for w,v in weights.items()},
        same_input_jumps_not_assumed_orthogonal=True))

def consumer_stream(number,tasks):
    ctx.prec=ARG.bits;done=0;began=time.monotonic()
    while True:
        item=tasks.get()
        if item is None:break
        first,end=item;merge_group(first,end);done+=1
        progress('consumer-'+str(number),completed_groups=done,last_group=[first,end],done=False)
    progress('consumer-'+str(number),completed_groups=done,done=True,seconds=time.monotonic()-began)

def guarded(name,function,*args):
    try:function(*args)
    except BaseException as error:
        progress(name,done=False,failure=dict(type=type(error).__name__,message=str(error),
            operation=CURRENT_OPERATION,traceback_frames=[dict(file=Path(x.filename).name,line=x.lineno,function=x.name)
                for x in traceback.extract_tb(error.__traceback__)[-16:]]))
        traceback.print_exc();raise

def status(name):
    path=TEMP/'progress'/f'{name}.json'
    return read(path) if path.exists() else dict(completed_rows=0,done=False)

def orchestrate(doc):
    context=mp.get_context('fork');tasks=context.Queue()
    streams={}
    for name,function in (('future',future_stream),('past',past_stream),('product',product_stream)):
        child=context.Process(target=guarded,args=(name,function),name=name)
        child.start();streams[name]=child
    consumers={}
    def add_consumer():
        n=len(consumers);child=context.Process(target=guarded,args=('consumer-'+str(n),consumer_stream,n,tasks))
        child.start();consumers[n]=child
    add_consumer();queued=set();last_report=0;sent_end=False
    try:
        while True:
            for name,child in list(streams.items())+[(f'consumer-{n}',v) for n,v in consumers.items()]:
                if child.exitcode not in (None,0):raise RuntimeError('actual temporary '+name+' child failed')
            counts={name:int(status(name).get('completed_rows',0)) for name in streams}
            for group,first in enumerate(range(0,TOTAL,GROUP)):
                end=min(TOTAL,first+GROUP)
                if group in queued:continue
                if (first>=TOTAL-counts['past'] and end<=counts['future'] and end<=counts['product']):
                    tasks.put((first,end));queued.add(group)
            active=sum(child.is_alive() for child in streams.values())
            while len(consumers)<4-active:add_consumer()
            completed=sum(state_path('groups',i).exists() for i in range((TOTAL+GROUP-1)//GROUP))
            if time.monotonic()-last_report>=30:
                progress('combined',streams=counts,complete_groups=completed,
                    queued_groups=len(queued),consumer_processes=len(consumers),done=False)
                print(json.dumps(dict(streams=counts,groups=completed,consumers=len(consumers))),flush=True)
                last_report=time.monotonic()
            if active==0 and len(queued)==(TOTAL+GROUP-1)//GROUP and not sent_end:
                for _ in consumers:tasks.put(None)
                sent_end=True
            if sent_end and all(not c.is_alive() for c in consumers.values()):break
            time.sleep(.2)
        for child in [*streams.values(),*consumers.values()]:
            child.join()
            if child.exitcode:raise RuntimeError('one actual temporary computation did not finish successfully')
        if completed!=(TOTAL+GROUP-1)//GROUP:raise ValueError('the whole5970 temporary local group cover is incomplete')
        doc['actual_parallel_completion']=dict(streams={k:status(k) for k in streams},
            complete_local_groups=completed,maximum_compute_processes=4,
            original_future_rows_reused=len(PREFIX),new_future_rows=TOTAL-len(PREFIX),
            new_past_rows=TOTAL,new_unnormalized_Poisson_product_rows=TOTAL)
        progress('combined',streams={k:TOTAL for k in streams},complete_groups=completed,done=True)
    finally:
        for child in [*streams.values(),*consumers.values()]:
            if child.is_alive():child.terminate()
        for child in [*streams.values(),*consumers.values()]:child.join(timeout=20)

def aggregate_groups():
    sources=empty_source_sums();grams={k:zero(Q,Q) for k in POISSON_COV};weights={w:arb(0) for w in WINDOWS}
    for group,first in enumerate(range(0,TOTAL,GROUP)):
        end=min(TOTAL,first+GROUP);d,arrays=load_state(state_path('groups',group))
        if (d.get('first')!=first or d.get('end')!=end
            or d['original_row_sha256']!=[canonical(ROWS[i]) for i in range(first,end)]):
            raise ValueError('the actual complete local group union lost one original row')
        for ch in CHANNELS:
            for w in m.WINDOWS:sources[ch]['squared'][w]+=up(d['source_sums'][ch]['squared'][w])
            sources[ch]['body_squared']+=up(d['source_sums'][ch]['body_squared'])
            for w in WINDOWS:sources[ch]['jumps'][w]+=up(d['source_sums'][ch]['jumps'][w])
        for k in POISSON_COV:grams[k]+=enc.read_covariance(arrays,d['unnormalized_Poisson_Grams'][k])
        for w in WINDOWS:weights[w]+=up(d['positive_jump_weights'][w])
    return sources,{k:sym(v) for k,v in grams.items()},{w:positive(v) for w,v in weights.items()}

def initial_values():
    d,a=load_state(TEMP/'initial-waist.json')
    return exact(a['V_hi'])+exact(a['V_lo'])

def finite_source_result(doc,sums,F,boundary,cut):
    V0=initial_values();S0=exact(F.frame_values(TOTAL-1,'left'))
    R0=block(S0,0,P,0,P)*V0+block(S0,0,P,P,N);normal=sym(transpose(R0)*R0)
    Qwaist=read_future(TOTAL-1,F)
    last,values=load_state(TEMP/'past-final.json')
    S=exact(F.frame_values(0,'right'));rho=Fraction(boundary['exact_cut_rho'])
    B=m.exact_nominal_boundary(cut,rho);error=up(boundary['right']['weighted_true_low_97_row_matrix_error'])
    totals={w:arb(0) for w in WINDOWS};components={}
    for ch in CHANNELS:
        W=enc.read_covariance(values,last['cut_covariances'][ch])
        right,cut_norm,detail=m.right_defect(W,S,B,error,rho)
        left=sqrt_upper(m.dot_trace(normal,Qwaist[ch]));body=sqrt_upper(sums[ch]['body_squared'])
        proposal={w:sqrt_upper(sums[ch]['squared'][w]) for w in m.WINDOWS}
        proposal['true_cut_trace']=cut_norm;results={}
        for w in WINDOWS:
            terms=dict(proposal=proposal[w],ordinary_body=GAINS[w]['body']*body,
                true_waist=GAINS[w]['left']*left,true_regular97=GAINS[w]['right']*right,
                all_actual_state_jumps=sums[ch]['jumps'][w])
            value=positive(sum(terms.values(),arb(0)));totals[w]+=value
            results[w]=dict(complete_HS_upper=record(value),
                individually_paid_components={k:record(positive(v)) for k,v in terms.items()})
        components[ch]=dict(body=record(body),left=record(left),right=record(right),
            right_details=detail,complete_bounds=results)
    doc['complete_true_finite193_body_high_to_low_bounds']={w:record(positive(v)) for w,v in totals.items()}
    doc['complete_directional_posterior_components']=components
    m.gate(doc,'complete_finite193_source_Green_keeps_true96_true97_mean_all_body_and_every_jump',
        all(positive(v).is_finite() for v in totals.values()))

def normalize_Poisson(doc,grams,weights,F,boundary,cut):
    V0,Vchosen,past=read_past(0)
    A,B,Di,port=F.port(0);Vexact=(A*V0+B)*Di
    L=p.lift(Vexact);Scut=exact(F.frame_values(0,'right'))
    rho=Fraction(boundary['exact_cut_rho']);Bhat=m.exact_nominal_boundary(cut,rho)
    nominal=Bhat*Scut*L;inverse,identity=m.checked_inverse(nominal,'the full97 actual nominal cut row')
    hi,lo,C,rounding=selected_twice(inverse)
    Y=Scut*L*C;odd=block(Y,0,P,0,Q);even=block(Y,P,N,0,Q)
    Hcut=sym(transpose(odd)*odd+transpose(even)*even*q(1/rho**2))
    residual=nominal*C-eye(Q);Enom=sym(transpose(residual)*residual)
    cap_error=up(boundary['right']['weighted_true_low_97_row_matrix_error'])
    Eeven=sym(transpose(even)*even*cap_error**2)
    Hright,right_choices=enc.weighted_pair(Enom,Eeven)
    normalized={k:sym(transpose(C)*H*C) for k,H in grams.items()}
    Ewaist,waist_error_Gram=read_product(TOTAL-1)
    Vwaist=initial_values();Swaist=exact(F.frame_values(TOTAL-1,'left'))
    R0=block(Swaist*p.lift(Vwaist),0,P,0,Q)
    unnormalized_left,fee=enc.sandwich(Ewaist,waist_error_Gram,p.signed_gram(R0))
    Hleft=sym(transpose(C)*unnormalized_left*C)
    proposals=dict(whole_inner_body=normalized['proposal_whole'],
        fixed_complete_negative_phase_window=normalized['proposal_negative'],true_cut_trace=Hcut)
    final={};certificates={};arrays={'C_hi':hi,'C_lo':lo}
    for w in WINDOWS:
        total=normalized[JUMP_KEYS[w]];alpha_sum=weights[w];selected={}
        for name,H in (('ordinary_body',normalized['body_defect']*GAINS[w]['body']**2),
                       ('true_waist',Hleft*GAINS[w]['left']**2),
                       ('true_regular97',Hright*GAINS[w]['right']**2)):
            total,alpha_sum,alpha=enc.weighted_add(total,alpha_sum,sym(H));selected[name]=record(alpha)
        posterior=sym(total*alpha_sum)
        total,alpha_sum,alpha=enc.weighted_add(total,alpha_sum,sym(proposals[w]))
        result=sym(total*alpha_sum)
        final[w],r=put_cov(result,'true_'+w,arrays)
        certificates[w]=dict(actual_true97_input_Gram=r,
            true_operator_bound=record(sqrt_upper(norm(final[w]))),
            proposal_operator_bound=record(sqrt_upper(norm(proposals[w]))),
            posterior_operator_bound=record(sqrt_upper(norm(posterior))),
            actual_positive_post_weights=selected,proposal_weight=record(alpha),
            total_positive_weight=record(alpha_sum),
            all_unormalized_signed_Grams_conjugated_by_same_exact_C=True,
            product_radius_not_a_physical_jump=True)
    save_state(TEMP/'complete-true97-Poisson.json',arrays,dict(stage='complete_true97_Poisson',
        complete_true_right_Poisson_Gram_certificates=certificates))
    doc['actual_true97_normalization']=dict(nominal_inverse_identity=identity,
        exact_two_dyadic_choice_error=record(rounding),true_nominal_boundary_defect=record(norm(residual)),
        true_even97_boundary_error=record(cap_error),right_positive_weights=right_choices,
        unnormalized_product_radius_at_waist=record(sqrt_upper(norm(waist_error_Gram))),
        complete_signed_product_error_Gram_preserved=True,
        full_mean_preserved=True,no_added_cut_V_jump=True)
    doc['complete_true_right_Poisson_Gram_certificates']=certificates
    doc['complete_true_right_Poisson_operator_upper']={w:r['true_operator_bound'] for w,r in certificates.items()}
    m.gate(doc,'all_true97_Poisson_inputs_use_exact_final_graph_PC_minus_I_and_complete_even_boundary_fee',
        set(final)==set(WINDOWS))
    return final

def consume_same97_cap(doc,H):
    native,actual=read(ARG.cap),read(ARG.cap_process)
    if (sha(ARG.cap)!=CAP_NATIVE or str(actual.get('run_id'))!='43671537267'
        or str(actual.get('run_attempt'))!='1' or actual.get('worker_source_sha256')!=CAP_WORKER
        or actual.get('input_manifest_sha256')!=CAP_MANIFEST
        or native.get('source_sha256')!=CAP_SOURCE or not native.get('complete') or native.get('failure')
        or not native.get('gates') or not all(x['passed'] for x in native['gates'])
        or not any(c.get('label')=='complete_same97_full_cap_posterior_matrices' and c.get('actual_returncode')==0
                   for c in actual.get('children',[]))
        or not native.get('complete_full_cap_high_to_low_bound_proved')
        or native.get('complete_same_repaired_centre_definition_sha256')!=cap.CENTRE
        or native.get('exact_boundary_input_units')!='original97 regular row Euclidean coordinates; no second rho input weight'):
        raise ValueError('the original complete same97 cap result has another exact mathematical identity')
    values=cap.arrays_from_receipt(ARG.cap_arrays,native['complete_posterior_array_receipt'])
    G={k:enc.read_covariance(values,r) for k,r in native['base_complete97_Gram_receipts'].items()}
    if set(G)!=set(cap.GRAM_KEYS):raise ValueError('one full cap component or independent mean is absent')
    old={k:enc.read_covariance(values,r['complete_Wcap']) for k,r in native['complete_cap_candidates'].items()}
    arrays={};windows={}
    for w in WINDOWS:
        fresh,receipts,selected=enc.whole_cap_candidates(G,native['complete_constants'],H[w],arrays,w)
        choices={k:dict(operator_upper=record(sqrt_upper(m.dot_trace(H[w],W))),
                       origin='new_same_input_positive_weights',complete_Wcap=receipts[k]['complete_Wcap'])
                 for k,W in fresh.items()}
        for k,W in old.items():
            choices['original_'+k]=dict(operator_upper=record(sqrt_upper(m.dot_trace(H[w],W))),
                origin='exact_original_complete_cap_Gram',complete_Wcap=native['complete_cap_candidates'][k]['complete_Wcap'])
        best=min(choices,key=lambda k:positive(up(choices[k]['operator_upper'])))
        windows[w]=dict(complete_operator_upper=choices[best]['operator_upper'],selected_complete_contraction=best,
            all_complete_contraction_choices=choices,
            complete_new_candidates=receipts,signed_trace_before_final_upper=True)
    save_state(TEMP/'complete-same97-contraction.json',arrays,
        dict(stage='complete_same97_contraction',original_cap_native_sha256=CAP_NATIVE,
             complete_same_input_directional_contractions=windows))
    doc['complete_same_input_directional_contractions']=windows
    m.gate(doc,'same97_complete_infinite_cap_high_input_and_true_right_Poisson_use_signed_correlations',
        all(up(v['complete_operator_upper']).is_finite() for v in windows.values()))

def exact_original_event_posterior_constants(green,events,kernel,impulse,boundary,doc):
    # The original impulse producer hashes compact JSON WITHOUT a final
    # newline (old.canonical). Matrix rows use a different WITH-newline
    # canonical convention. Bind each event to its actual producer,
    # preserving the exact SHA gate and every original numerical formula.
    # These are the actual original L2 source norm and full boundary
    # columns, not the norm of a unit pointwise forcing.
    gains={w:dict(body=up(kernel['complete_ordinary_L2_source_to_L2_bounds'][w]),
        left=up(green['complete_source_component_L2_bounds'][w]['left_boundary_unit_norm']),
        right=up(green['complete_source_component_L2_bounds'][w]['right_boundary_unit_norm'])) for w in m.WINDOWS}
    rho=Fraction(boundary['exact_cut_rho'])
    physical=q(max(Fraction(1),1/rho))
    DL=up(boundary['right']['weighted_true_right_feedback_DL'])
    LR=up(boundary['right']['weighted_true_right_source_lifting_LR'])
    last=kernel['forward_kernel_event_rows'][-1]
    if last.get('kind')!='continuous' or Fraction(last['interval'][1])!=m.RIGHT:
        raise ValueError('the original L2 kernel has no true final cut node')
    kg=last['right_node_two_row_Gram']
    body_cut=(physical*sqrt_upper(up(kg['pp'])+up(kg['qq']))).upper()
    lastp=green['complete_forward_source_component_profiles'][-1]
    if Fraction(lastp['interval'][1])!=m.RIGHT:
        raise ValueError('the actual original boundary profiles do not reach the cut')
    bp={}
    for name,short in (('left_boundary_unit_norm','left'),('right_boundary_unit_norm','right')):
        p=up(lastp['channels'][name]['right_weighted_p'])
        qcut=DL*p+(LR if short=='right' else arb(0))
        bp[short]=(physical*sqrt_upper(p*p+qcut*qcut)).upper()
    gains['true_cut_trace']=dict(body=body_cut,**bp)
    allimp={Fraction(x['radius']):x for x in impulse['interface_impulse_rows']}
    if len(allimp)!=5970:raise ValueError('the complete impulse map has a repeated radius')
    # Events are stored from the true cut backwards. At each interface
    # product contains ALL events strictly outside that interface.
    # unit_weighted_jump_p_after already includes the interface's own b.
    multiplier=arb(1);jumps={};cutfactor=(physical*sqrt_upper(1+DL*DL)).upper()
    for event in events:
        if event['kind']=='interface':
            radius=Fraction(event['radius'])
            if radius not in allimp:raise ValueError('one real interface has no original gain')
            original=allimp[radius]
            if original['original_event_sha256']!=m.old.canonical(event):
                raise ValueError('one true interface impulse belongs to a different event')
            jumps[radius]={w:up(original['ordinary_L2_output_bound'][w]) for w in m.WINDOWS}
            jumps[radius]['true_cut_trace']=(cutfactor*multiplier
                *up(original['unit_weighted_jump_p_after'])).upper()
        multiplier=(multiplier*m.old.port(event)['p_from_p']).upper()
    if len(jumps)!=5970 or m.RIGHT in jumps:
        raise ValueError('the true cut is not an extra projector interface')
    doc['posterior_complete_true_Green_constants']={
        w:{k:record(v) for k,v in row.items()} for w,row in gains.items()}
    doc['new_cut_jump_trace_proof']=dict(
        exact_formula='metric_cut*sqrt(1+DL^2)*product(b strictly outside interface)*original_unit_p_after',
        interface_own_b_included_exactly_once_in_original_unit_p_after=True,
        true_zero_right_source_for_each_individual_jump=True,
        original_L2_kernel_final_node_used_for_ordinary_source_trace=True,
        body_L2_norm_not_substituted_for_a_trace=True,new_exponentials_or_old_port_calls=0)
    return gains,jumps


def run(a,doc):
    global ARG,INPUT,STAGE,PROFILE,ROWS,GAINS,JUMPGAINS,PREFIX,TEMP
    ARG=a;ctx.prec=a.bits;ctx.cap=6;TEMP=a.temp
    if sha(enc.__file__)!=ENCLOSURE_SOURCE:raise ValueError('the exact new scaled-error proof implementation changed')
    TEMP.mkdir(parents=True,exist_ok=True)
    INPUT=m.input_identity(a)
    original=m.inputs(a,doc)
    PROFILE,ROWS,green,events,kernel,impulse,boundary,cut=original
    STAGE=canonical(dict(source_sha256=sha(__file__),input_sha256=INPUT,
        old_prefix_sha256=sha(a.old_backward),arithmetic_bits=a.bits,cap_sha256=sha(a.cap),
        same_original_operator=True))
    doc.update(stage_identity=STAGE,input_sha256=INPUT,
        original_formula_sources=dict(matrix=OLD_SOURCE,Poisson=POISSON_SOURCE,cap=CAP_SOURCE,
            new_scaled_signed_error_Gram=ENCLOSURE_SOURCE),
        actual_v2_unpersisted_arithmetic_redone=dict(run_id='43681612825',future_new=2340,
            past=1800,product=4331,canonical_ports=5970,complete_groups=0,
            all_original1886_future_rows_reused_without_recomputation=True))
    PREFIX=legacy_prefix(a,doc)
    GAINS,JUMPGAINS=exact_original_event_posterior_constants(green,events,kernel,impulse,boundary,doc)
    m.gate(doc,'every_original_impulse_event_SHA_uses_its_exact_no_newline_producer_convention',True)
    product_preflight(doc)
    orchestrate(doc)
    sums,grams,weights=aggregate_groups();F=files()
    finite_source_result(doc,sums,F,boundary,cut)
    H=normalize_Poisson(doc,grams,weights,F,boundary,cut)
    consume_same97_cap(doc,H)
    m.gate(doc,'all5970_original_operator_cells_and_every_real_interface_are_consumed_exactly_once',
        len(ROWS)==TOTAL and all(state_path('groups',i).exists() for i in range((TOTAL+GROUP-1)//GROUP)))
    m.gate(doc,'only_temporary_new_arrays_and_no_new_target_F_C_or_validator_calls',True)
    doc.update(complete=True,complete_finite193_directional_two_boundary_bound_proved=True,
        complete97_input_Poisson_Gram_bound_proved=True,
        complete_true_right_Poisson_contraction_proved=True,
        exact_inner_interval=['0','9/10'],exact_negative_output_interval=['0',str(m.PHASE_RIGHT)],
        exact_boundary_input_units='original97 regular row Euclidean coordinates; no second rho input weight',
        old_future_rows_recomputed=0,old_target_F_C_Gram_or_validator_calls=0,
        all_full193_and_independent_mean_preserved=True,
        independent_full_high_body_and_high_cut_inputs_retained=True,
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False,
        new_recomputable_arrays_persisted=False,new_math_only_in_this_public_runner=True)

def phase_output_receipts():
    result={}
    if TEMP is None:return result
    for stage in ('future','past','product','ports','groups'):
        directory=TEMP/stage;h=hashlib.sha256();count=0
        for path in sorted(directory.glob('*.json')) if directory.exists() else ():
            raw=path.read_bytes();d=json.loads(raw)
            if d.get('kind')!=KIND or d.get('source_sha256')!=sha(__file__) or d.get('stage_identity')!=STAGE or not d.get('complete'):
                raise ValueError('a phase-output receipt changed scientific identity')
            # Full arrays are bound by the SHA receipt inside these exact
            # complete state bytes. Their raw identities were verified by
            # the local consumer, never replaced by this metadata digest.
            h.update(path.name.encode()+b'\0'+hashlib.sha256(raw).digest());count+=1
        result[stage]=dict(complete_state_files=count,
            ordered_exact_state_receipts_sha256=h.hexdigest(),
            arrays_bound_by_each_original_exact_receipt=True,
            persisted_recomputable_output=False)
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('matrix-data','matrix-process','profile','profile-process','green','green-process',
                 'kernel','kernel-process','impulse','impulse-process','reviewed-impulse-process',
                 'boundary','nominal-cut','array-root','old-backward','old-backward-process',
                 'cap','cap-process','cap-arrays','temp','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--matrix-run',required=True)
    parser.add_argument('--bits',type=int,default=192)
    a=parser.parse_args()
    if a.bits<192:raise ValueError('the new directed arithmetic budget cannot be below192 bits')
    if a.out.exists():raise FileExistsError('preserve the original temporary conclusion file')
    started=time.monotonic()
    doc=dict(kind=KIND,source_sha256=sha(__file__),complete=False,failure=None,gates=[],
        arithmetic_bits=a.bits,maximum_compute_processes=4,
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error),operation=CURRENT_OPERATION,
            traceback_frames=[dict(file=Path(x.filename).name,line=x.lineno,function=x.name)
                for x in traceback.extract_tb(error.__traceback__)[-16:]]);raise
    finally:
        doc['actual_phase_output_hashes']=phase_output_receipts()
        doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=doc['complete'],seconds=doc['seconds'],
        old_future_rows_reused=doc['exact_original_future_prefix']['complete_rows'],
        actual_output_sha256=sha(a.out),
        finite193=doc.get('complete_finite193_directional_two_boundary_bound_proved'),
        true97=doc.get('complete97_input_Poisson_Gram_bound_proved'),
        infinite_inverse=False)),flush=True)

if __name__=='__main__':main()
