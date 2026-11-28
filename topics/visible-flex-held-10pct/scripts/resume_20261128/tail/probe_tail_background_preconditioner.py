#!/usr/bin/env python3
"""Measure full-node GMRES convergence using actual stored J and background blocks.

This is a feasibility probe for an eventual native literal-JVP predictor. The
actual stored complete stage Jacobians are still used in every matrix product;
no native JVP implementation, nonlinear solve or new tail acceptance is claimed.
The preconditioner integrates all independent background 2x2 mode blocks on
the original frozen RK/cusp grid and retains every node and boundary row.
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


def checked(item):
    if ref(item['path'])!=item:
        raise ValueError('Referenced bytes changed: '+item['path'])
    return Path(item['path'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--predictor-summary',type=Path,required=True)
    p.add_argument('--outdir',type=Path,required=True)
    a=p.parse_args()
    out=a.outdir.resolve();out.mkdir(parents=True,exist_ok=False)
    source=load(a.predictor_summary)
    packet=read_packet(checked(source['accepted_source_packet']))
    record=load(checked(source['actual_fresh_native_record']))
    bg=load(checked(source['original_scaling']))
    cp=packet['response']['checkpoint'];states=np.asarray(cp['states'])
    M,K,L=bg['M'],bg['K'],bg['depth'];size=(L+1)*K
    if states.shape!=(L+1,K):
        raise ValueError('Complete actual state required')
    helper=module('_background_probe_wire',a.repo/'topics/visible-flex-held-10pct/scripts/resume_n4_tail/native_extended/parallel_native_batch.py')
    wire=checked(record['input']).read_bytes();shape=helper.split_wire(wire)
    if shape['modes']!=M or shape['count']!=L or shape['jac']!=1:
        raise ValueError('Expected this complete actual full-J input')
    data=checked(record['output']).read_bytes()
    blocks,failed=helper.output_records(data,shape,L,shape['token'],0)
    if failed is not None:
        raise ValueError('A successful complete actual J is required')
    J=np.empty((L,K,K));flows=np.empty((L,K))
    for n,(start,end,status) in enumerate(blocks):
        offset=start+8
        state=np.frombuffer(data,dtype='<f8',count=K+2,offset=offset)
        tangent=np.frombuffer(data,dtype='<f8',count=(K+2)*K,
                              offset=offset+8*(K+2)).reshape(K+2,K)
        flows[n]=state[:K];J[n]=tangent[:K]
        flows[n,M:]/=bg['portRatios'][n];J[n,M:,:]/=bg['portRatios'][n]
    before=time.monotonic()
    transfers=np.empty((L,M,2,2))
    modes=np.arange(1,M+1,dtype=np.longdouble)*packet['config']['spacing']
    for n,(start,end) in enumerate(shape['spans']):
        steps,points=struct.unpack_from('<2i',wire,start)
        offset=start+8+8*(K+2)
        g=np.frombuffer(wire,dtype='<f8',count=points*(M+12),offset=offset).reshape(points,M+12).astype(np.longdouble)
        A=np.empty((points,M,2,2),dtype=np.longdouble)
        A[:,:,0,0]=g[:,8,None]*(modes*modes-4)
        A[:,:,0,1]=g[:,8,None]*g[:,10,None]*g[:,7,None]/g[:,0,None]
        A[:,:,1,0]=g[:,9,None]*modes*(modes*modes-1)*(g[:,12:]/g[:,6,None])
        A[:,:,1,1]=4*g[:,8,None]-g[:,9,None]*modes*modes*g[:,7,None]
        cursor=offset+8*points*(M+12)
        T=np.broadcast_to(np.eye(2,dtype=np.longdouble),(M,2,2)).copy()
        for step in range(steps):
            profile,index,ia,im,ie,x,h0=struct.unpack_from('<5i2d',wire,cursor);cursor+=36
            h=np.longdouble(h0)
            aa=A[ia]@T
            bb=A[im]@(T+h*aa/2)
            cc=A[im]@(T+h*bb/2)
            dd=A[ie]@(T+h*cc)
            T+=h*(aa+2*bb+2*cc+dd)/6
        if cursor!=end or not np.all(np.isfinite(T)):
            raise ValueError('Background flow extent or finiteness failed')
        transfers[n]=T
        transfers[n,:,1,:]/=bg['portRatios'][n]
    background_seconds=time.monotonic()-before
    sc=np.asarray(bg['scales']);ratio=sc[1:]/sc[:-1];deep=np.asarray(bg['deepGraph'])
    rows=[];cols=[];values=[]
    for n in range(L):
        rows.extend((n*K+np.arange(K)).tolist());cols.extend((n*K+np.arange(K)).tolist());values.extend([1.]*K)
        for j in range(M):
            indices=[j,M+j]
            for i in range(2):
                for k in range(2):
                    rows.append(n*K+indices[i]);cols.append((n+1)*K+indices[k])
                    values.append(-ratio[n]*transfers[n,j,i,k])
    for j in range(M):
        rows.extend([L*K+j,L*K+M+j,L*K+M+j]);cols.extend([j,L*K+M+j,L*K+j]);values.extend([1.,1.,-deep[j]])
    P=coo_matrix((values,(rows,cols)),shape=(size,size)).tocsc();P.eliminate_zeros()
    before=time.monotonic();lu=splu(P,permc_spec='COLAMD',diag_pivot_thresh=1.,options={'Equil':True})
    factor_seconds=time.monotonic()-before
    def matvec(vector):
        v=np.asarray(vector).reshape(L+1,K);result=np.empty((L+1,K))
        result[:L]=v[:-1]-ratio[:,None]*np.einsum('nij,nj->ni',J,v[1:])
        result[L,:M]=v[0,:M];result[L,M:]=v[-1,M:]-deep*v[-1,:M]
        return result.ravel()
    b=np.empty((L+1,K));b[:L]=(flows-states[:-1])/sc[:-1,None]
    b[L,:M]=(np.asarray(bg['desiredTarget'])-states[0,:M])/sc[0]
    b[L,M:]=-(states[-1,M:]-deep*states[-1,:M])/sc[-1]
    b=b.ravel()
    history=[];calls=0
    def operator(vector):
        nonlocal calls
        calls+=1
        return matvec(lu.solve(vector))
    A=LinearOperator((size,size),matvec=operator,dtype=float)
    before=time.monotonic()
    y,info=gmres(A,b,rtol=1e-12,atol=0.,restart=40,maxiter=5,
                 callback=lambda value:history.append(float(value)),callback_type='pr_norm')
    z=lu.solve(y)
    solve_seconds=time.monotonic()-before
    zl=z.reshape(L+1,K).astype(np.longdouble)
    rl=ratio.astype(np.longdouble);jl=J.astype(np.longdouble)
    exact=np.empty((L+1,K),dtype=np.longdouble)
    exact[:L]=zl[:-1]-rl[:,None]*np.einsum('nij,nj->ni',jl,zl[1:])
    exact[L,:M]=zl[0,:M]
    exact[L,M:]=zl[-1,M:]-deep.astype(np.longdouble)*zl[-1,:M]
    residual=b.astype(np.longdouble)-exact.ravel()
    row_norm=max(1.,float(np.max(1+ratio[:,None]*np.sum(np.abs(J),axis=2))),float(np.max(1+abs(deep))))
    normwise=float(np.max(abs(residual)))/(row_norm*float(np.max(abs(z)))+float(np.max(abs(b))))
    with_gmres=states+z.reshape(L+1,K)*sc[:,None]
    np.savez_compressed(out/'unaccepted-gmres-predictor.npz',states=with_gmres,
                        normalized_step=z.reshape(L+1,K),background_transfers=transfers)
    report=dict(scope=__doc__,source=ref(__file__),predictor_summary=ref(a.predictor_summary),
        actual_native_record=source['actual_fresh_native_record'],M=M,stages=L,unknowns=size,
        nonlinear_unknowns_or_boundary_rows_dropped=False,
        background_zero_state_blocks='All modes; literal frozen coefficients, original RK4/cusp steps, original output portRatio',
        preconditioner_nnz=int(P.nnz),preconditioner_factor_nnz=int(lu.L.nnz+lu.U.nnz),
        background_seconds=background_seconds,preconditioner_factor_seconds=factor_seconds,
        gmres_seconds=solve_seconds,gmres_info=int(info),gmres_inner_iterations=len(history),
        all_stage_matrix_products=calls,gmres_relative_residual_history=history,
        gmres_relative_tolerance=1e-12,gmres_restart=40,gmres_max_restart_cycles=5,
        final_original_linear_residual_linf=float(np.max(abs(residual))),
        final_relative_rhs_residual_linf=float(np.max(abs(residual)))/float(np.max(abs(b))),
        original_full_J_normwise_backward_error=normwise,
        original_backward_error_gate_passed=normwise<1e-11,
        native_JVP_implemented=False,stored_complete_actual_J_used=True,
        nonlinear_solve_invoked=False,predictor_accepted=False,complete_surface=False)
    (out/'summary.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(report,indent=2,allow_nan=False))


if __name__=='__main__':
    main()
