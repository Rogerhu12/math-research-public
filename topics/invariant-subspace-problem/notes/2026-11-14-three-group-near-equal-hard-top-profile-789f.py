#!/usr/bin/env python3
"""One bounded, prescribed large-birth diagnostic on the full group-symmetric block.

Each group spin block reduces both d and d*, so complete block MP inverses
are the actual full physical MP inverses on this reducing component.
No sampled value is a proof or a counterexample certificate.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import resource
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
resource.setrlimit(resource.RLIMIT_CPU,(58,58))
resource.setrlimit(resource.RLIMIT_CORE,(0,0))
import gc, hashlib, json, pathlib, time
import numpy as np
from scipy import linalg
START=time.monotonic()
HERE=pathlib.Path(__file__).resolve().parent

def states(L,k):
    return [(x,y,k-x-y) for x in range(L[0]+1) for y in range(L[1]+1)
            if 0<=k-x-y<=L[2]]

def deletion(L,b,k):
    lo,hi=states(L,k-1),states(L,k)
    ind={x:i for i,x in enumerate(lo)}
    D=np.zeros((len(lo),len(hi)))
    for j,n in enumerate(hi):
        for a in range(3):
            if n[a]:
                q=list(n);q[a]-=1
                D[ind[tuple(q)],j]=b[a]*np.sqrt(n[a]*(L[a]-n[a]+1))
    return D

def actual(r,lam):
    M=2*r+1;L=[M//3]*3
    for j in range(M%3):L[2-j]+=1
    logs=np.array(lam,dtype=float)/r
    logs-=np.dot(L,logs)/M
    b=np.exp(logs)
    R=deletion(L,b,r)
    Uleft,s,Vh=linalg.svd(R,full_matrices=True)
    U=Vh[R.shape[0]:].T
    Rlo=deletion(L,b,r-1)
    vlo,slo,wh=linalg.svd(Rlo,full_matrices=True)
    V=wh[Rlo.shape[0]:].T
    J1=Vh[:len(s)].T@((Uleft.T@V)/s[:,None])
    au=V.T@deletion(L,1/b,r)@U
    LA=J1.T@(J1@au)
    nl=np.array(states(L,r-1),dtype=float)
    topdiag=np.exp(2*nl@logs-np.dot(L,logs))
    J3=topdiag[:,None]*V
    Q,T=linalg.qr(J3,mode='economic')
    X=linalg.solve_triangular(T.T,LA,lower=True)
    sv=linalg.svdvals(X)
    residuals=dict(upper_primitive=float(linalg.norm(R@U,2)/linalg.norm(R,2)),
                   lower_primitive=float(linalg.norm(Rlo@V,2)/linalg.norm(Rlo,2)),
                   first_mp=float(linalg.norm(R@J1-V,2)),
                   top_qr=float(linalg.norm(J3-Q@T,2)/linalg.norm(J3,2)),
                   whitening=float(linalg.norm(T.T@X-LA,2)/max(linalg.norm(LA,2),1e-300)))
    logdiag=np.array(states(L,r),dtype=float)@logs
    conds=dict(full_first_deletion=float(s[0]/s[-1]),
               full_lower_deletion=float(slo[0]/slo[-1]),
               top_factor=float(np.linalg.cond(T)),
               primitive_deweight_bound=float(np.exp(logdiag.max()-logdiag.min())))
    accepted=max(residuals.values())<2e-8 and max(conds.values())<1e7
    return dict(r=r,M=M,group_sizes=L,lambda_groups=lam,weights=b.tolist(),
                physical_block_dimensions=dict(middle=R.shape[1],lower=R.shape[0],upper_source=U.shape[1],lower_source=V.shape[1]),
                all_hard_fees=(sv*sv).tolist(),max_hard_fee=float(sv[0]**2),
                accepted_diagnostic=accepted,conditions=conds,residuals=residuals)

out=dict(purpose='single controlled near-equal large-birth diagnostic; no theorem or counterexample claim',
         group_block='tensor product of all three completely symmetric spin blocks; entire primitive source inside it',
         memory_mib=512,cpu_limit_seconds=58,cases=[])
for r in (3,6,12,24,48):
    for lam in ([-1,0,1],[-2,0,2],[-4,0,4]):
        if time.monotonic()-START>50:break
        t=time.monotonic()
        try:item=actual(r,lam)
        except Exception as exc:item=dict(r=r,lambda_groups=lam,error=type(exc).__name__+': '+str(exc))
        item['case_seconds']=time.monotonic()-t
        out['cases'].append(item)
        print(json.dumps({k:item[k] for k in ('r','lambda_groups','max_hard_fee','accepted_diagnostic','case_seconds') if k in item}),flush=True)
        gc.collect()
    if time.monotonic()-START>50:break
out['elapsed_seconds']=time.monotonic()-START
out['source_sha256']=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
(HERE/'2026-11-14-three-group-near-equal-hard-top-profile-789f.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'event':'completed','elapsed_seconds':out['elapsed_seconds'],'case_count':len(out['cases'])}),flush=True)
