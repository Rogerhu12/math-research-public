#!/usr/bin/env python3
"""Solve the unchanged finite multiple-shooting Newton linear equations.

All node variables remain present. Diagonal node scales use the original
shooting residual's first-mode normalization. There is no Riccati graph
inverse and no change to the root equation, radial integration or guards.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import json,sys,time
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import splu
x=json.load(sys.stdin);M=int(x['M']);K=2*M;L=int(x['depth']);n=(L+1)*K
Js=np.asarray(x['Js'],float).reshape(L,K,K);sc=np.asarray(x['scales'],float);g=np.asarray(x['deepGraph'],float)
if len(sc)!=L+1 or len(g)!=M or np.any(sc<=0)or not np.isfinite(Js).all():raise ValueError('Invalid finite shooting dimensions or scales')
ratio=sc[1:]/sc[:-1];row=[];col=[];data=[]
for j in range(L):
 row.extend((j*K+np.arange(K)).tolist());col.extend((j*K+np.arange(K)).tolist());data.extend(np.ones(K).tolist())
 row.extend(np.repeat(j*K+np.arange(K),K).tolist());col.extend(np.tile((j+1)*K+np.arange(K),K).tolist());data.extend((-ratio[j]*Js[j]).ravel().tolist())
for k in range(M):
 row.extend([L*K+k,L*K+M+k,L*K+M+k]);col.extend([k,L*K+M+k,L*K+k]);data.extend([1.,1.,-g[k]])
A=coo_matrix((data,(row,col)),shape=(n,n)).tocsc();A.eliminate_zeros()
mode=x['mode']
if mode=='correction':
 b=np.zeros((n,1));r=np.asarray(x['residuals'],float).reshape(L,K);b[:L*K,0]=(r/sc[:-1,None]).ravel();b[L*K:L*K+M,0]=np.asarray(x['targetDelta'])/sc[0];b[L*K+M:,0]=-np.asarray(x['deepEnd'])/sc[-1]
elif mode=='tangent':
 b=np.zeros((n,M));b[L*K:L*K+M,:]=np.eye(M)/sc[0]
else:raise ValueError('Unknown linear solve mode')
start=time.monotonic();lu=splu(A,permc_spec='COLAMD',diag_pivot_thresh=1.,options={'Equil':True});z=lu.solve(b)
# Long-double residual evaluation verifies exactly these original linear equations.
JL=Js.astype(np.longdouble);rl=ratio.astype(np.longdouble);gl=g.astype(np.longdouble);bl=b.astype(np.longdouble)
def residual(zz):
 zz=np.asarray(zz,np.longdouble).reshape(L+1,K,-1);v=np.zeros_like(bl)
 for j in range(L):v[j*K:(j+1)*K]=zz[j]-rl[j]*(JL[j]@zz[j+1])
 v[L*K:L*K+M]=zz[0,:M];v[L*K+M:]=zz[-1,M:]-gl[:,None]*zz[-1,:M]
 return bl-v
before=float(np.max(np.abs(residual(z))))
for _ in range(2):
 dz=lu.solve(np.asarray(residual(z),float));trial=z+dz
 if np.max(np.abs(residual(trial)))>=np.max(np.abs(residual(z))):break
 z=trial
rr=residual(z);den=np.abs(bl)+np.asarray(abs(A)@np.abs(z),np.longdouble);err=float(np.max(np.abs(rr)/np.maximum(den,np.longdouble(1e-300))))
out=dict(linear_solver='all-node-scaled-SuperLU',dimension=n,nnz=int(A.nnz),rhs_columns=b.shape[1],residual_linf=float(np.max(np.abs(rr))),initial_residual_linf=before,componentwise_backward_error=err,seconds=time.monotonic()-start)
if mode=='correction':out['delta']=(z.reshape(L+1,K)*sc[:,None]).tolist()
else:out['graph']=(z[M:K]*sc[0]).ravel().tolist()
trace=os.environ.get('VISIBLE_FLEX_SPARSE_TRACE')
if trace:
 with open(trace,'a')as f:f.write(json.dumps({k:v for k,v in out.items()if k not in ['delta','graph']})+'\n')
json.dump(out,sys.stdout,separators=(',',':'));sys.stdout.write('\n')
