#!/usr/bin/env python3
"""Same captured finite native equations: dyadic equilibration and refinement.

No native worker, new Jacobian, nonlinear trial or accepted DN is produced.
All scientific work is restricted to the public repository's Actions.
The original sigma defines the residual norm throughout. Integer exponents
initialize from each original sigma, equilibrate actual matrix entry exponents,
and form each final scaled entry directly from the original stored binary64.
The refinement RHS is rounded once from every exact original dyadic residual.
"""
from __future__ import annotations

import argparse
from collections import deque
from concurrent.futures import ProcessPoolExecutor
import gzip
import hashlib
import importlib.util
import json
import math
import multiprocessing
import os
from pathlib import Path
import resource
import struct
import sys
import time

import numpy as np
import scipy
from scipy.linalg.lapack import dgbtrf, dgbtrs

HERE=Path(__file__).resolve().parent
BAND_NAME='geometry_20261114_native_captured_band_correction.py'
BAND_SHA='b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390'
EXACT_NAME='exact_20261114_native_allrows_dyadic_residual.py'
EXACT_SHA='0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f'
CAPTURE_SHA='ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7'
SCALING='original-sigma-nearest-dyadic-then-row-column-max-entry-v1'
_EXACT=None


def actions_only():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or
            os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'):
        raise RuntimeError('Equilibrated native linear science belongs only to the public repository Actions')


def file_sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for raw in iter(lambda:stream.read(1<<20),b''):h.update(raw)
    return h.hexdigest()


def load_module(name,digest,key):
    path=HERE/name
    if file_sha(path)!=digest:raise ValueError('Frozen helper source changed: '+name)
    spec=importlib.util.spec_from_file_location(key,path)
    if spec is None or spec.loader is None:raise ImportError('Cannot load '+name)
    module=importlib.util.module_from_spec(spec);sys.modules[key]=module;spec.loader.exec_module(module)
    return module


def exact_module():
    global _EXACT
    if _EXACT is None:_EXACT=load_module(EXACT_NAME,EXACT_SHA,'_native_equil_exact_rows')
    return _EXACT


def exact_stage_job(task):
    actions_only()
    return exact_module().stage_job(task)


def float_hex(value):return struct.pack('<d',float(value)).hex()


def round_dyadic(mantissa,exponent):
    """Correct binary64 nearest/ties-even rounding of m*2**e, one rounding.

    q discards enough integer bits for both a 53-bit significand and the
    subnormal lattice 2**-1074. Integer ties are resolved to even. The remaining
    t has at most53 significant bits (a carry can equal2**53 exactly), so the
    final float(t)/ldexp is exact when finite. No huge integer is converted to
    float before this reduction. Exact real zero has canonical positive sign.
    """
    if mantissa==0:return 0.,dict(rounded=False,underflow_to_zero=False,exact_zero=True)
    negative=mantissa<0;n=abs(mantissa)
    q=max(0,n.bit_length()-53,-1074-exponent)
    if q:
        t,remainder=divmod(n,1<<q);half=1<<(q-1)
        if remainder>half or (remainder==half and t&1):t+=1
    else:t,remainder=n,0
    if t and t.bit_length()-1+exponent+q>1023:
        raise OverflowError('Exact dyadic RHS overflows binary64; m='+hex(mantissa)+', e='+str(exponent))
    value=math.ldexp(float(t),exponent+q) if t else 0.
    if negative:value=-value
    return value,dict(rounded=bool(remainder),underflow_to_zero=bool(t==0),exact_zero=False)


def nearest_dyadic_exponent(word,E):
    """Nearest positive power of two in absolute value; ties choose lower."""
    m,e=E.decode_bits(word)
    if m<=0:raise ValueError('Original sigma must be finite and strictly positive')
    length=m.bit_length();floor=e+length-1
    return floor+int(2*m>3*(1<<(length-1)))


def save_integer(output,name,array,role):
    a=np.asarray(array,dtype='<i4',order='C');raw=a.tobytes()
    relative='large-arrays/'+name+'.i32le'
    with (output.directory/relative).open('xb') as stream:stream.write(raw)
    record=dict(name=name,file=relative,dtype='<i4',order='C',shape=list(a.shape),bytes=len(raw),
        sha256=hashlib.sha256(raw).hexdigest(),role=role)
    output.entries.append(record);return record


def entry_exponent(values):
    if not np.isfinite(values).all():raise FloatingPointError('The original finite matrix has a nonfinite entry')
    # frexp's exponent is exact for every finite normal/subnormal binary64.
    return np.frexp(np.abs(values))[1].astype(np.int64)-1


def maximum_entry_exponents(capture,row_exp,column_exp):
    """Exact floor-log2 maximum of the real dyadically scaled original A.

    No scaled floating matrix is formed during equilibration. Zero coefficients
    stay absent; every nonzero coefficient, including subnormals, is retained.
    """
    M,K,D=capture.M,capture.K,capture.depth;N=(D+1)*K
    sentinel=np.int64(-1000000)
    row_max=np.full(N,sentinel,dtype=np.int64);col_max=row_max.copy()
    local=np.arange(K);small=np.arange(M)
    values=row_exp[:M]+column_exp[:M]
    row_max[:M]=values;col_max[:M]=values
    for n,J in capture.stages():
        r=M+n*K+local;c=(n+1)*K+local
        exponents=entry_exponent(J)+row_exp[r,None]+column_exp[c][None,:]
        exponents=np.where(J!=0,exponents,sentinel)
        row_max[r]=np.maximum(row_max[r],np.max(exponents,axis=1))
        col_max[c]=np.maximum(col_max[c],np.max(exponents,axis=0))
        c0=n*K+local;minus_identity=row_exp[r]+column_exp[c0]
        row_max[r]=np.maximum(row_max[r],minus_identity)
        col_max[c0]=np.maximum(col_max[c0],minus_identity)
    far=capture.all('original-far-graph').reshape(-1)
    r=M+D*K+small;cq=D*K+small;cp=cq+M
    ones=row_exp[r]+column_exp[cp]
    row_max[r]=np.maximum(row_max[r],ones);col_max[cp]=np.maximum(col_max[cp],ones)
    values=entry_exponent(far)+row_exp[r]+column_exp[cq]
    values=np.where(far!=0,values,sentinel)
    row_max[r]=np.maximum(row_max[r],values);col_max[cq]=np.maximum(col_max[cq],values)
    if np.any(row_max==sentinel) or np.any(col_max==sentinel):
        raise ValueError('Unexpected zero row/column in the original full cut/stage/far layout')
    return row_max,col_max


def exponent_summary(values):
    return dict(minimum=int(values.min()),maximum=int(values.max()),
        zero_entries=int((values==0).sum()),entries=int(values.size))


def choose_exponents(capture,E,output,B,out,passes):
    M,K,D=capture.M,capture.K,capture.depth
    words=struct.unpack('<'+'Q'*(D+1),E.read_raw_array(capture,'original-scales'))
    node=np.array([nearest_dyadic_exponent(word,E) for word in words],dtype=np.int64)
    columns=np.repeat(node,K)
    rows=-np.concatenate((np.repeat(node[0],M),np.repeat(node[:-1],K),np.repeat(node[-1],M)))
    initial=dict(node_exponents=save_integer(output,'initial-node-dyadic-exponents',node,
        'Nearest power of two to each exact original sigma; absolute-distance ties choose lower'),
        row_exponents=save_integer(output,'initial-row-dyadic-exponents',rows,'Initial inverse original-node dyadic scale'),
        column_exponents=save_integer(output,'initial-column-dyadic-exponents',columns,'Initial original-node dyadic scale'))
    history=[]
    for iteration in range(passes):
        rmax,cmax=maximum_entry_exponents(capture,rows,columns)
        row_step=-rmax;rows+=row_step
        r_after,c_after=maximum_entry_exponents(capture,rows,columns)
        column_step=-c_after;columns+=column_step
        record=dict(iteration=iteration,source='exact binary64 entry exponents, no intermediate scaled matrix',
            before_row_floorlog2_max=exponent_summary(rmax),before_column_floorlog2_max=exponent_summary(cmax),
            after_row_step_row_floorlog2_max=exponent_summary(r_after),
            after_row_step_column_floorlog2_max=exponent_summary(c_after),
            row_step=save_integer(output,f'equilibration-{iteration:02d}-row-step',row_step,'Exact integer exponent increment'),
            column_step=save_integer(output,f'equilibration-{iteration:02d}-column-step',column_step,'Exact integer exponent increment'),
            cumulative_row_exponents=exponent_summary(rows),cumulative_column_exponents=exponent_summary(columns))
        history.append(record);B.write(out/f'equilibration-{iteration:02d}.json',record)
        print(json.dumps(dict(event='native_dyadic_equilibration',iteration=iteration,
            row_step_range=[int(row_step.min()),int(row_step.max())],
            column_step_range=[int(column_step.min()),int(column_step.max())])),flush=True)
        if not np.any(row_step) and not np.any(column_step):break
    rfinal,cfinal=maximum_entry_exponents(capture,rows,columns)
    result=dict(schema='native-original-matrix-dyadic-equilibration-v1',initial=initial,iterations=history,
        final_row_exponents=save_integer(output,'final-row-dyadic-exponents',rows,'Atilde_ij=2**row_exp[i] A_ij 2**column_exp[j]'),
        final_column_exponents=save_integer(output,'final-column-dyadic-exponents',columns,'delta_j=2**column_exp[j] z_j'),
        final_exact_row_floorlog2_max=exponent_summary(rfinal),
        final_exact_column_floorlog2_max=exponent_summary(cfinal),
        original_sigma_norm_unchanged=True,original_matrix_not_replaced=True,
        no_intermediate_ratio_or_scaled_matrix_rounding=True)
    B.write(out/'equilibration.json',result)
    return rows,columns,result


class ScalingLedger:
    def __init__(self):
        self.entries=0;self.nonfinite=0;self.zero_from_nonzero=0;self.nonreversible=0;self.examples=[]

    def apply(self,values,exponents,location):
        values=np.asarray(values,dtype=np.float64)
        exponents=np.broadcast_to(np.asarray(exponents,dtype=np.int64),values.shape)
        with np.errstate(over='ignore',under='ignore',invalid='ignore'):
            scaled=np.ldexp(values,exponents)
            recovered=np.ldexp(scaled,-exponents)
        different=(recovered.view(np.uint64)!=values.view(np.uint64))
        bad=~np.isfinite(scaled);lost=(values!=0)&(scaled==0)
        self.entries+=values.size;self.nonfinite+=int(bad.sum())
        self.zero_from_nonzero+=int(lost.sum());self.nonreversible+=int(different.sum())
        for index in np.flatnonzero(different.reshape(-1))[:max(0,12-len(self.examples))]:
            self.examples.append(dict(location=location,index=list(np.unravel_index(index,values.shape)),
                original_float64le_hex=float_hex(values.flat[index]),binary_exponent=int(exponents.flat[index]),
                formed_float64le_hex=float_hex(scaled.flat[index]),
                inverse_scaled_float64le_hex=float_hex(recovered.flat[index])))
        if bad.any():raise FloatingPointError('Final direct dyadic matrix formation is nonfinite at '+str(location))
        return scaled

    def report(self):
        return dict(entries=self.entries,nonfinite=self.nonfinite,
            nonzero_rounded_to_zero=self.zero_from_nonzero,
            nonreversible_binary64_scalings=self.nonreversible,examples=self.examples,
            exact_real_dyadic_entry_scaling_verified=self.nonreversible==0,
            original_raw_entries_and_integer_exponents_reconstruct_every_formation_error=True,
            original_equations_rechecked_even_if_formation_loses_bits=True)


def assemble(capture,rows,columns,output,B,report):
    M,K,D=capture.M,capture.K,capture.depth;N=(D+1)*K
    kl=M;ku=3*M-1;ldab=2*kl+ku+1;diagonal=kl+ku
    ab=np.zeros((ldab,N),dtype=np.float64,order='F')
    rmax=np.zeros(N);cmax=np.zeros(N);local=np.arange(K);small=np.arange(M)
    ledger=ScalingLedger()
    values=ledger.apply(np.ones(M),rows[:M]+columns[:M],dict(kind='cut'))
    ab[diagonal,small]=values;rmax[:M]=abs(values);cmax[:M]=abs(values)
    for n,J in capture.stages():
        r=M+n*K+local;c=(n+1)*K+local
        block=ledger.apply(J,rows[r,None]+columns[c][None,:],dict(kind='stage-J',stage=n))
        br=diagonal+r[:,None]-c[None,:]
        if int(br.min())<kl or int(br.max())>=ldab:raise ValueError('Complete stage exceeds exact derived bandwidth')
        ab[br,c[None,:]]=block
        rmax[r]=np.maximum(rmax[r],np.max(np.abs(block),axis=1))
        cmax[c]=np.maximum(cmax[c],np.max(np.abs(block),axis=0))
        c0=n*K+local
        minus=ledger.apply(-np.ones(K),rows[r]+columns[c0],dict(kind='stage-minus-I',stage=n))
        ab[diagonal+M,c0]=minus
        rmax[r]=np.maximum(rmax[r],abs(minus));cmax[c0]=np.maximum(cmax[c0],abs(minus))
    far=capture.all('original-far-graph').reshape(-1);r=M+D*K+small;cq=D*K+small;cp=cq+M
    minus=ledger.apply(-far,rows[r]+columns[cq],dict(kind='far-Q'))
    plus=ledger.apply(np.ones(M),rows[r]+columns[cp],dict(kind='far-Pi'))
    ab[diagonal+M,cq]=minus;ab[diagonal,cp]=plus
    rmax[r]=np.maximum(abs(minus),abs(plus));cmax[cq]=np.maximum(cmax[cq],abs(minus));cmax[cp]=np.maximum(cmax[cp],abs(plus))
    report.update(M=M,K=K,depth=D,dimension=N,lower_bandwidth=kl,upper_bandwidth=ku,LAPACK_band_rows=ldab,
        band_bytes=int(ab.nbytes),band_shape=list(ab.shape),far_is_original_diagonal=True,
        equation_order='cut M; D complete K-row stages; far M',variable_order='node-major complete (Q,Pi)',
        unfactored_band_Fortran_byte_sha256=hashlib.sha256(memoryview(ab.ravel(order='F')).cast('B')).hexdigest(),
        matrix_formation=ledger.report(),formed_matrix_entry_scales=dict(
            row_maximum_range=[B.scalar(rmax.min()),B.scalar(rmax.max())],
            column_maximum_range=[B.scalar(cmax.min()),B.scalar(cmax.max())],
            zero_rows=int((rmax==0).sum()),zero_columns=int((cmax==0).sum()),
            extra_equilibration_applied=True))
    output.save('formed-row-max-absolute-entry',rmax,'Actual formed floating matrix row maximum; not a condition number')
    output.save('formed-column-max-absolute-entry',cmax,'Actual formed floating matrix column maximum; not a condition number')
    return ab,kl,ku


class ExactOriginalResidual:
    def __init__(self,capture,E,B,output,rows,workers):
        self.capture=capture;self.E=E;self.B=B;self.output=output;self.rows=rows;self.workers=workers
        M,K,D=capture.M,capture.K,capture.depth
        names=('stage-residuals','cut-residual','end-residual','original-scales','original-far-graph')
        self.inputs={name:E.read_raw_array(capture,name) for name in names}
        self.residuals=E.decoded_array(self.inputs['stage-residuals'],D*K,'all original stage residuals')
        self.cut=E.decoded_array(self.inputs['cut-residual'],M,'all original cut residuals')
        self.far=E.decoded_array(self.inputs['end-residual'],M,'all original far residuals')
        self.graph=E.decoded_array(self.inputs['original-far-graph'],M,'complete original diagonal far graph')
        self.sigma_words=struct.unpack('<'+'Q'*(D+1),self.inputs['original-scales'])
        for word in self.sigma_words:E.sigma_denominator(word)

    def initial_rhs(self):
        pairs=(*self.cut,*self.residuals,*self.far)
        rhs=np.empty(len(pairs),dtype=np.float64);rounded=0;underflow=0;examples=[]
        for i,(m,e) in enumerate(pairs):
            value,info=round_dyadic(-m,e+int(self.rows[i]));rhs[i]=value
            rounded+=int(info['rounded']);underflow+=int(info['underflow_to_zero'])
            if info['rounded'] and len(examples)<8:
                examples.append(dict(row=i,original_mantissa=str(m),original_exponent=e,
                    row_scale_exponent=int(self.rows[i]),rounded_rhs_float64le_hex=float_hex(value)))
        return rhs,dict(rounding='one exact dyadic nearest/ties-even to binary64',rounded_rows=rounded,
            underflow_to_zero_rows=underflow,examples=examples,exact_real_zero_convention='positive zero')

    def evaluate(self,delta,iteration):
        E,B,capture=self.E,self.B,self.capture;M,K,D=capture.M,capture.K,capture.depth
        raw=B.float_bytes(delta);digest=hashlib.sha256(raw).hexdigest()
        decoded=E.decoded_array(raw,(D+1)*K,'every original-coordinate trial direction coefficient')
        rhs=np.empty((D+1)*K,dtype=np.float64);worst=None;base_worst=None;completed=0;rows_seen=0;products=0
        rounding=dict(rounded_rows=0,underflow_to_zero_rows=0,exact_zero_rows=0,examples=[])
        label=f'iteration-{iteration:02d}';name='large-arrays/'+label+'-exact-residuals.jsonl.gz'
        path=self.output.directory/name;started=time.monotonic();pool=None
        handle=path.open('xb');ledger=gzip.GzipFile(fileobj=handle,mode='wb',mtime=0)

        def consume(kind,node,data,jhash=None):
            nonlocal worst,base_worst,rows_seen,products
            result=data['directions']['candidate'];count=K if kind=='stage' else M
            if len(result['rows'])!=count:raise ValueError('An exact original row block is incomplete')
            mr=E.max_record(kind,node,result['maximum_row'],result['maximum_integer'],self.sigma_words[node])
            if E.better(mr,worst):worst=mr
            value,row=data['base_maximum'];br=E.max_record(kind,node,row,value,self.sigma_words[node])
            if E.better(br,base_worst):base_worst=br
            start=E.row_order(kind,node,0)
            for j,(coefficient,power) in enumerate(result['rows']):
                m=int(coefficient,16);r=start+j
                value,info=round_dyadic(-m,power+int(self.rows[r]));rhs[r]=value
                for key,target in [('rounded','rounded_rows'),('underflow_to_zero','underflow_to_zero_rows'),('exact_zero','exact_zero_rows')]:
                    rounding[target]+=int(info[key])
                if info['rounded'] and len(rounding['examples'])<8:
                    rounding['examples'].append(dict(row=r,exact_residual=[coefficient,power],
                        row_scale_exponent=int(self.rows[r]),rounded_rhs_float64le_hex=float_hex(value)))
            ledger.write(E.json_bytes(dict(kind=kind,node=node,first_global_equation_row=start,
                all_exact_unscaled_rows=result['rows'],original_J_stage_sha256=jhash,
                exact_original_sigma_maximum=E.public_record(mr),direction_float64le_sha256=digest)))
            rows_seen+=count;products+=result['original_product_positions']

        try:
            consume('cut',0,E.boundary_job('cut',self.cut,{'candidate':decoded[:K]},self.graph))

            def tasks():
                for n,J in E.stage_bytes(capture):
                    yield dict(stage=n,J=J,residuals=self.residuals[n*K:(n+1)*K],
                        directions={'candidate':(decoded[n*K:(n+1)*K],decoded[(n+1)*K:(n+2)*K])})

            def consume_stage(result):
                nonlocal completed
                if result['stage']!=completed:raise ValueError('Exact original stage order changed')
                consume('stage',completed,result,result['J_stage_raw_sha256']);completed+=1
                if completed%32==0 or completed==D:
                    print(json.dumps(dict(event='native_refinement_exact_residual',iteration=iteration,
                        completed_stages=completed,expected_stages=D,elapsed_seconds=time.monotonic()-started)),flush=True)

            if self.workers==1:
                for task in tasks():consume_stage(E.stage_job(task))
            else:
                pool=ProcessPoolExecutor(max_workers=self.workers,mp_context=multiprocessing.get_context('spawn'))
                pending=deque();source=iter(tasks())
                for _ in range(2*self.workers):
                    task=next(source,None)
                    if task is None:break
                    pending.append(pool.submit(exact_stage_job,task))
                while pending:
                    consume_stage(pending.popleft().result());task=next(source,None)
                    if task is not None:pending.append(pool.submit(exact_stage_job,task))
                pool.shutdown(wait=True);pool=None
            consume('far',D,E.boundary_job('far',self.far,{'candidate':decoded[D*K:(D+1)*K]},self.graph))
            if completed!=D or rows_seen!=(D+1)*K or products!=D*K*K+M:
                raise ValueError('Incomplete exact original residual assembly')
        finally:
            if pool is not None:pool.shutdown(wait=True,cancel_futures=True)
            ledger.close();handle.close()
        record=dict(name=label+'-exact-residuals',file=name,dtype='exact-dyadic-jsonl-gzip',shape=[rows_seen],
            bytes=path.stat().st_size,sha256=file_sha(path),
            role='All original real binary-array e rows; each [hex coefficient,binary exponent] is exact')
        self.output.entries.append(record)
        witness=dict(schema='native-equilibrated-exact-global-row-witness-v1',iteration=iteration,
            direction_float64le_sha256=digest,exact_global_original_sigma_norm=E.public_record(worst),
            operands=E.worst_witness(capture,worst,raw,self.inputs),all_original_rows_visited=True,
            exact_stored_finite_arrays_only=True,not_exact_derivative_of_nonlinear_flow=True)
        witness_file=B.write(self.output.directory/(label+'-exact-global-witness.json'),witness)
        rounded_rhs=self.output.save(label+'-refinement-rhs',rhs,
            'Correctly rounded once: negative exact e times final dyadic row scale; original full row order')
        report=dict(iteration=iteration,direction_float64le_sha256=digest,
            exact_rows=rows_seen,completed_stages=completed,original_product_positions=products,
            exact_global_original_sigma_norm=E.public_record(worst),
            exact_original_stored_base_sigma_norm=E.public_record(base_worst),exact_witness=witness_file,
            all_exact_residual_rows=record,rounded_refinement_rhs=rounded_rhs,rhs_rounding=rounding,
            all_nonzero_finite_operands_retained=True,native_accepted=False,
            elapsed_seconds=time.monotonic()-started)
        B.write(self.output.directory/(label+'-exact-residual-summary.json'),report)
        return rhs,worst,report


def exact_smaller(left,right):
    return abs(left['_integer'])*right['_denominator']<abs(right['_integer'])*left['_denominator']


def save_checkpoint(B,output,capture,delta,source_sha,name):
    rows=[dict(node=n,state=row.tolist(),negative_zero_columns=np.flatnonzero((row==0)&np.signbit(row)).tolist())
        for n,row in enumerate(delta)]
    return B.write(output.directory/name,dict(schema='complete-original-native-band-direction-v1',
        source_sha256=source_sha,input_binding=capture.binding,scaling=SCALING,
        M=capture.M,K=capture.K,depth=capture.depth,
        delta_float64le_sha256=hashlib.sha256(B.float_bytes(delta)).hexdigest(),rows=rows,
        no_nonlinear_trial=True,native_accepted=False,task_completed=False),compressed=True)


def main():
    actions_only();parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--capture-directory',type=Path,required=True)
    parser.add_argument('--capture-result-sha256',default=CAPTURE_SHA)
    parser.add_argument('--equilibration-passes',type=int,default=3)
    parser.add_argument('--refinement-steps',type=int,default=3)
    parser.add_argument('--exact-workers',type=int,default=2)
    parser.add_argument('--out',type=Path,required=True)
    a=parser.parse_args()
    if not 0<=a.equilibration_passes<=8 or not 0<=a.refinement_steps<=8 or not 1<=a.exact_workers<=4:
        raise ValueError('Explicit bounded equilibration/refinement/worker budgets required')
    a.out=a.out.resolve()
    if a.out.exists() or a.out.is_relative_to(a.capture_directory.resolve()):
        raise ValueError('Use a new independent output directory')
    a.out.mkdir(parents=True);started=time.monotonic();output=None
    report=dict(schema='original-captured-native-full-band-correction-v1',source_sha256=file_sha(__file__),
        algorithm='dyadic-row-column-equilibration-and-exact-original-residual-refinement-v1',
        binding_helper_sha256=BAND_SHA,exact_row_helper_sha256=EXACT_SHA,capture_result_sha256=a.capture_result_sha256,
        scaling=SCALING,diagnostic_completed=False,linear_direction_computed=False,native_accepted=False,task_completed=False,
        original_native_calls=0,new_J_calls=0,nonlinear_trials=0,original_sigma_norm_unchanged=True,
        NumPy=np.__version__,SciPy=scipy.__version__,
        BLAS_threads={key:os.environ.get(key) for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
        requested_equilibration_passes=a.equilibration_passes,requested_refinement_steps=a.refinement_steps,
        exact_workers=a.exact_workers,refinement_history=[])
    B=load_module(BAND_NAME,BAND_SHA,'_native_equil_capture_binding');E=exact_module()
    try:
        capture=B.CapturedArrays(a.capture_directory,a.capture_result_sha256)
        B.write(a.out/'input-binding.json',capture.binding);output=B.OutputArrays(a.out)
        M,K,D=capture.M,capture.K,capture.depth
        original_delta=capture.all('original-delta');residuals=capture.all('stage-residuals')
        cut=capture.all('cut-residual').reshape(-1);far=capture.all('end-residual').reshape(-1)
        scales=capture.all('original-scales').reshape(-1);far_graph=capture.all('original-far-graph').reshape(-1)
        old=capture.summary['linear_defect_summary']['all_original_rows']['worst']
        report['exact_original_captured_worst_row']=B.exact_row(capture,original_delta,residuals,cut,far,scales,far_graph,
            old,B.stored_scalar(old['value']),output,'exact-original-captured-worst-row')
        rows,columns,equilibration=choose_exponents(capture,E,output,B,a.out,a.equilibration_passes)
        report['equilibration']=equilibration
        ab,kl,ku=assemble(capture,rows,columns,output,B,report)
        evaluator=ExactOriginalResidual(capture,E,B,output,rows,a.exact_workers)
        initial_rhs,initial_rounding=evaluator.initial_rhs()
        report['initial_rhs_rounding']=initial_rounding
        output.save('complete-scaled-rhs',initial_rhs,'Negative original captured residual times final dyadic row scale')
        B.write(a.out/'assembled-model.json',report)
        factor_started=time.monotonic();pointer=ab.__array_interface__['data'][0]
        lu,piv,info=dgbtrf(ab,kl,ku,overwrite_ab=1)
        report.update(lapack_factor_info=int(info),factorization_seconds=time.monotonic()-factor_started,
            LU_shares_input_storage=bool(np.shares_memory(lu,ab)),LU_retains_input_pointer=pointer==lu.__array_interface__['data'][0],
            LU_Fortran_byte_sha256=hashlib.sha256(memoryview(lu.ravel(order='F')).cast('B')).hexdigest())
        report['pivot_array']=save_integer(output,'lapack-pivots',piv,'Actual SciPy dgbtrf pivot vector; reused unchanged')
        B.write(a.out/'factorization.json',report)
        if info<0:raise RuntimeError('dgbtrf rejected argument '+str(-info))
        if info>0:raise FloatingPointError('dgbtrf returned zero pivot '+str(info))

        def solve_rhs(rhs,label):
            before=time.monotonic();column=np.array(rhs[:,None],dtype=np.float64,order='F',copy=True)
            result,info=dgbtrs(lu,kl,ku,column,piv,overwrite_b=1)
            detail=dict(label=label,lapack_solve_info=int(info),seconds=time.monotonic()-before)
            if info:raise RuntimeError('dgbtrs failed with info='+str(info))
            if not np.isfinite(result).all():raise FloatingPointError('Nonfinite complete scaled correction '+label)
            z=result[:,0];ledger=ScalingLedger()
            recovered=ledger.apply(z,columns,dict(kind='restore-original-coordinates',label=label)).reshape(D+1,K)
            detail['original_coordinate_recovery']=ledger.report()
            output.save(label+'-scaled-coordinate-delta',z.reshape(D+1,K),'All scaled coordinates before exact powers-of-two recovery')
            return recovered,detail

        delta,detail=solve_rhs(initial_rhs,'initial')
        report['lapack_solve_info']=detail['lapack_solve_info'];report['initial_solve']=detail
        best=None;best_rhs=None;best_exact=None;best_iteration=None
        for iteration in range(a.refinement_steps+1):
            descriptor=output.save(f'iteration-{iteration:02d}-original-coordinate-delta',delta,
                'Every full original coordinate before this exact original-equation residual check')
            checkpoint=save_checkpoint(B,output,capture,delta,report['source_sha256'],f'direction-checkpoint-iteration-{iteration:02d}.json.gz')
            rhs,exact,residual_report=evaluator.evaluate(delta,iteration)
            improved=best is None or exact_smaller(exact,best_exact)
            history=dict(iteration=iteration,delta=descriptor,direction_checkpoint=checkpoint,
                exact_original_residual=residual_report,strictly_improved_original_sigma_norm=improved)
            report['refinement_history'].append(history)
            B.write(a.out/f'iteration-{iteration:02d}-summary.json',history)
            if not improved:
                report['refinement_stop_reason']='Exact original-sigma norm did not strictly improve; previous complete best direction retained'
                break
            best=delta.copy();best_rhs=rhs;best_exact=exact;best_iteration=iteration
            if exact['_integer']==0:
                report['refinement_stop_reason']='Exact residual of all saved finite linear equations is zero; no nonlinear acceptance asserted'
                break
            if iteration==a.refinement_steps:
                report['refinement_stop_reason']='Explicit finite refinement budget exhausted'
                break
            correction,correction_detail=solve_rhs(best_rhs,f'refinement-{iteration+1:02d}')
            history['following_error_correction_solve']=correction_detail
            output.save(f'refinement-{iteration+1:02d}-original-coordinate-increment',correction,
                'Full solution of the correctly rounded scaled negative exact residual')
            with np.errstate(over='ignore',invalid='ignore',under='ignore'):candidate=best+correction
            if not np.isfinite(candidate).all():
                history['following_nonfinite_candidate']=output.save(f'iteration-{iteration+1:02d}-nonfinite-candidate',candidate,
                    'Actual nonfinite binary64 update retained; original finite best direction preserved')
                report['refinement_stop_reason']='Binary64 error-correction update became nonfinite; previous complete best retained'
                break
            if B.float_bytes(candidate)==B.float_bytes(best):
                report['refinement_stop_reason']='Full proposed binary64 update is byte-identical; exact residual cannot improve'
                break
            delta=candidate
        if best is None:raise RuntimeError('No complete finite direction and exact residual were retained')
        report['best_iteration']=best_iteration;report['best_exact_original_sigma_norm']=E.public_record(best_exact)
        report['linear_direction_computed']=True
        report['new_delta']=output.save('complete-original-coordinate-delta',best,
            'Complete restored best direction selected by exact original-sigma residual, before nonlinear trials')
        report['direction_checkpoint']=save_checkpoint(B,output,capture,best,report['source_sha256'],'direction-checkpoint.json.gz')
        report['linear_defects']=B.evaluate_directions(capture,{'original':original_delta,'new':best},
            residuals,cut,far,scales,far_graph,output,'complete')
        new_site,new_entry=B.select_report_worst(report['linear_defects']['new'])
        report['exact_new_floating_worst_row']=B.exact_row(capture,best,residuals,cut,far,scales,far_graph,
            new_site,B.stored_scalar(new_entry),output,'exact-new-floating-worst-row')
        report['diagnostic_completed']=True
    except Exception as error:
        report['actual_error']=repr(error)
    finally:
        if output is not None:
            report['array_manifest']=B.write(a.out/'output-array-manifest.json',dict(
                schema='captured-native-band-direction-arrays-v1',source_sha256=report['source_sha256'],
                capture_result_sha256=a.capture_result_sha256,arrays=output.entries,
                all_arrays_artifact_only=True,native_accepted=False,task_completed=False))
        report['elapsed_seconds']=time.monotonic()-started
        report['maximum_RSS_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        B.write(a.out/'result.json',report)
    print(json.dumps(dict(event='native_equilibrated_band_finished',diagnostic_completed=report['diagnostic_completed'],
        linear_direction_computed=report['linear_direction_computed'],native_accepted=False,task_completed=False)),flush=True)
    return 0 if report['diagnostic_completed'] else 2


if __name__=='__main__':raise SystemExit(main())
