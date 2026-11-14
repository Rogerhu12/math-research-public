#!/usr/bin/env python3
"""One bounded diagnostic, never a proof or a double-precision counterexample."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import resource, time, json, itertools, pathlib
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
resource.setrlimit(resource.RLIMIT_CPU,(55,55))
resource.setrlimit(resource.RLIMIT_CORE,(0,0))
import numpy as np
from scipy import linalg
START=time.monotonic()
HERE=pathlib.Path(__file__).resolve().parent

def bases(m,p):
    return list(itertools.combinations(range(m),p))

def deletion(b,p):
    lo,hi=bases(len(b),p-1),bases(len(b),p)
    ind={I:j for j,I in enumerate(lo)}
    out=np.zeros((len(lo),len(hi)))
    for c,I in enumerate(hi):
        for i in I: out[ind[tuple(t for t in I if t!=i)],c]=b[i]
    return out

def evaluate(b):
    b=np.array(b,dtype=float); b=b/np.exp(np.log(b).mean())
    m=len(b); r=(m-1)//2
    dr=deletion(b,r)
    uv,sv,vhv=linalg.svd(dr,full_matrices=True)
    U=vhv[dr.shape[0]:].T
    dl=deletion(b,r-1)
    ul,sl,vhl=linalg.svd(dl,full_matrices=True)
    V=vhl[dl.shape[0]:].T
    # Full first MP on H_(r-1), then restrict to the primitive source.
    J1=vhv[:len(sv)].T @ ((uv.T@V)/sv[:,None])
    LA=J1.T @ (J1 @ (V.T @ deletion(1/b,r) @ U))
    topdiag=np.array([np.prod(b[list(I)]**2)/np.prod(b) for I in bases(m,r-1)])
    J3=topdiag[:,None]*V
    Q,R=linalg.qr(J3,mode='economic')
    X=linalg.solve_triangular(R.T,LA,lower=True)
    sx=linalg.svdvals(X)
    cost=float(sx[0]**2)
    residuals={
      'upper_primitive':float(linalg.norm(dr@U,2)/linalg.norm(dr,2)),
      'lower_primitive':float(linalg.norm(dl@V,2)/linalg.norm(dl,2)),
      'first_mp':float(linalg.norm(dr@J1-V,2)),
      'top_qr':float(linalg.norm(J3-Q@R,2)/linalg.norm(J3,2)),
      'whitened_equation':float(linalg.norm(R.T@X-LA,2)/max(linalg.norm(LA,2),1e-300))}
    cond_d=float(sv[0]/sv[-1]); cond_top=float(np.linalg.cond(R))
    accepted=(max(residuals.values())<2e-8 and cond_d<1e7 and cond_top<1e7)
    return {'weights':b.tolist(),'cost':cost,'accepted_diagnostic':accepted,
            'condition_first_deletion':cond_d,'condition_top_factor':cond_top,'residuals':residuals}

rng=np.random.default_rng(789)
output={'purpose':'bounded targeted diagnostic; no proof claim','memory_limit_mib':512,'cpu_limit_seconds':55,'cases':[]}
for m in (7,9):
    patterns=[np.linspace(-1,1,m),np.array([1]*(m//2)+[0]+[-1]*(m//2)),
              np.array([1,1]+[0]*(m-4)+[-1,-1]),np.array([0]*(m-1)+[-1]),
              np.array([1]+[0]*(m-2)+[-1])]
    patterns += [rng.uniform(-1,1,m) for _ in range(6)]
    for j,exp in enumerate(patterns):
        for scale in (3.,30.,300.):
            if time.monotonic()-START>48: break
            item={'M':m,'birth':(m-1)//2,'pattern':j,'scale':scale,'exponents':exp.tolist()}
            try: item.update(evaluate(scale**exp))
            except Exception as exc: item['error']=type(exc).__name__+': '+str(exc)
            output['cases'].append(item)
        if time.monotonic()-START>48: break
    if time.monotonic()-START>48: break
output['wall_seconds']=time.monotonic()-START
accepted=[x for x in output['cases'] if x.get('accepted_diagnostic')]
output['accepted_count']=len(accepted)
output['rejected_count']=len(output['cases'])-len(accepted)
output['best_accepted']=sorted(accepted,key=lambda x:x['cost'],reverse=True)[:4]
path=HERE/'2026-11-14-odd-hard-top-targeted-profile-789f.json'
path.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:output[k] for k in ('wall_seconds','accepted_count','rejected_count','best_accepted')},indent=2))
