#!/usr/bin/env python3
"""Test stronger preconditioners against the complete saved actual shooting J.

Mode bands are used ONLY inside the preconditioner. Every matrix product and
final residual uses every entry of the true complete stored J, every shooting
unknown, and every original boundary row. This produces no nonlinear accepted
field and does not implement or benchmark a native matrix-free JVP.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import json
from pathlib import Path
import struct
import time

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import LinearOperator, gmres, splu

from tail_full_state_tangent_predictor import load, ref, module, read_packet


def verified(item):
    if ref(item['path'])!=item:
        raise ValueError('Actual recorded identity changed: '+item['path'])
    return Path(item['path'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--predictor-summary',type=Path,required=True)
    p.add_argument('--outdir',type=Path,required=True)
    a=p.parse_args();out=a.outdir.resolve();out.mkdir(parents=True,exist_ok=False)
    source=load(a.predictor_summary)
    packet=read_packet(verified(source['accepted_source_packet']))
    record=load(verified(source['actual_fresh_native_record']))
    bg=load(verified(source['original_scaling']))
    M,K,L=bg['M'],bg['K'],bg['depth'];n=(L+1)*K
    states=np.asarray(packet['response']['checkpoint']['states'])
    wire=verified(record['input']).read_bytes()
    helper=module('_modal_preconditioner_wire',a.repo/'topics/visible-flex-held-10pct/scripts/resume_n4_tail/native_extended/parallel_native_batch.py')
    shape=helper.split_wire(wire);data=verified(record['output']).read_bytes()
    blocks,failed=helper.output_records(data,shape,L,shape['token'],0)
    J=np.empty((L,K,K));flows=np.empty((L,K))
    for s,(start,end,status) in enumerate(blocks):
        values=np.frombuffer(data,dtype='<f8',count=(K+2)*(K+1),offset=start+8)
        flows[s]=values[:K]
        J[s]=values[K+2:].reshape(K+2,K)[:K]
        flows[s,M:]/=bg['portRatios'][s];J[s,M:]/=bg['portRatios'][s]
    sc=np.asarray(bg['scales']);ratio=sc[1:]/sc[:-1];deep=np.asarray(bg['deepGraph'])
    b=np.empty((L+1,K));b[:L]=(flows-states[:-1])/sc[:-1,None]
    b[L,:M]=(np.asarray(bg['desiredTarget'])-states[0,:M])/sc[0]
    b[L,M:]=-(states[-1,M:]-deep*states[-1,:M])/sc[-1]
    b=b.ravel()
    jl=J.astype(np.longdouble);rl=ratio.astype(np.longdouble);gl=deep.astype(np.longdouble)
    def matvec(v):
        v=np.asarray(v).reshape(L+1,K);result=np.empty_like(v)
        result[:L]=v[:-1]-ratio[:,None]*np.einsum('nij,nj->ni',J,v[1:])
        result[L,:M]=v[0,:M];result[L,M:]=v[-1,M:]-deep*v[-1,:M]
        return result.ravel()
    def residual(z):
        v=np.asarray(z,np.longdouble).reshape(L+1,K);r=np.empty_like(v)
        r[:L]=v[:-1]-rl[:,None]*np.einsum('nij,nj->ni',jl,v[1:])
        r[L,:M]=v[0,:M];r[L,M:]=v[-1,M:]-gl*v[-1,:M]
        return b.astype(np.longdouble)-r.ravel()
    Ainf=max(1.,float(np.max(1+ratio[:,None]*np.sum(abs(J),axis=2))),float(np.max(1+abs(deep))))
    answer=dict(scope=__doc__,source=ref(__file__),predictor_summary=ref(a.predictor_summary),
        actual_native_record=source['actual_fresh_native_record'],M=M,stages=L,unknowns=n,
        complete_actual_matrix_used_for_every_operator=True,all_boundary_rows_retained=True,
        native_JVP_implemented=False,predictor_accepted=False,rows=[])
    def save():
        (out/'summary.json').write_text(json.dumps(answer,indent=2,allow_nan=False)+'\n')
    save()
    for bandwidth in (M-1,0,2,4):
        rindex,cindex=np.indices((K,K));keep=np.abs(rindex%M-cindex%M)<=bandwidth
        ii,jj=rindex[keep],cindex[keep]
        rows=[];cols=[];values=[]
        for s in range(L):
            rows.extend((s*K+np.arange(K)).tolist());cols.extend((s*K+np.arange(K)).tolist());values.extend([1.]*K)
            rows.extend((s*K+ii).tolist());cols.extend(((s+1)*K+jj).tolist());values.extend((-ratio[s]*J[s,ii,jj]).tolist())
        for j in range(M):
            rows.extend([L*K+j,L*K+M+j,L*K+M+j]);cols.extend([j,L*K+M+j,L*K+j]);values.extend([1.,1.,-deep[j]])
        P=coo_matrix((values,(rows,cols)),shape=(n,n)).tocsc();P.eliminate_zeros()
        before=time.monotonic();lu=splu(P,permc_spec='COLAMD',diag_pivot_thresh=1.,options={'Equil':True})
        factor_seconds=time.monotonic()-before
        del rows,cols,values
        calls=0;history=[]
        def operator(v):
            nonlocal calls
            calls+=1
            return matvec(lu.solve(v))
        A=LinearOperator((n,n),matvec=operator,dtype=float)
        before=time.monotonic()
        y,info=gmres(A,b,rtol=1e-8,atol=0.,restart=40,maxiter=3,
                     callback=lambda r:history.append(float(r)),callback_type='pr_norm')
        z=lu.solve(y);seconds=time.monotonic()-before
        rr=residual(z);maximum=float(np.max(abs(rr)))
        normwise=maximum/(Ainf*float(np.max(abs(z)))+float(np.max(abs(b))))
        own=lu.solve(b)
        own_residual=np.asarray(b-P@own,np.longdouble)
        row=dict(mode_bandwidth=bandwidth,all_modes_in_preconditioner=True,
            preconditioner_only_cross_mode_entries_dropped=(bandwidth<M-1),
            P_nnz=int(P.nnz),LU_nnz=int(lu.L.nnz+lu.U.nnz),factor_seconds=factor_seconds,
            gmres_seconds=seconds,gmres_info=int(info),inner_iterations=len(history),
            all_actual_matrix_products=calls,rtol=1e-8,restart=40,max_restart_cycles=3,
            residual_history_first=history[:5],residual_history_last=history[-5:],
            final_original_longdouble_residual_linf=maximum,
            relative_rhs_residual_linf=maximum/float(np.max(abs(b))),
            original_normwise_backward_error=normwise,original_backward_error_gate_passed=normwise<1e-11,
            preconditioner_solve_relative_rhs_residual_linf=float(np.max(abs(own_residual)))/float(np.max(abs(b))))
        answer['rows'].append(row);save();print(json.dumps(row),flush=True)
    answer['status']='all_complete_matrix_preconditioner_probes_returned';save()


if __name__=='__main__':
    main()
