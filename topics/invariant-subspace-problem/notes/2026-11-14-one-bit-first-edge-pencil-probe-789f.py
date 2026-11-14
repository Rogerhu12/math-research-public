"""Short floating exploration of the stronger one-bit first-edge pencil; not a proof."""
import importlib.util
import json
from pathlib import Path
import numpy as np
from scipy import linalg

p=Path(__file__).with_name('2026-11-14-full-boolean-adjacent-search-789f.py')
spec=importlib.util.spec_from_file_location('boolean_probe',p)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def grams(w,s,last):
    n=len(w)
    u=np.eye(1) if s==0 else linalg.null_space(m.incidence(w,s-1,1))
    g=[np.eye(u.shape[1])]
    for j in range(1,last+1):
        a=m.incidence(w,s,j)
        left,sig,_=linalg.svd(a,full_matrices=False)
        z=(left.T@u)/sig[:,None]
        g.append(z.T@z)
    return u,g

rng=np.random.default_rng(7892785)
worst=(0,None)
for n,s in [(3,1),(4,1),(5,2),(6,2),(7,2),(7,3)]:
    for _ in range(70):
        w=np.exp(rng.uniform(-3,0,n));w/=w.max()
        u,g=grams(w,s,min(2,n-2*s));v,l=grams(w,s-1,3)
        c1=linalg.inv(g[1]);c2=linalg.inv(g[2]) if len(g)>2 else np.zeros_like(c1)
        b=v.T@m.incidence(w**3,s-1,1)@u
        q=b.T@l[2];delta=(c1@b.T@l[3]-q)/2
        rr=np.concatenate((c1@q,delta),axis=1)
        for t in np.exp(np.linspace(-8,8,9))*sum(w*w):
            top=c1@c1-c2+t*c1
            low=np.block([[np.eye(l[1].shape[0])+t*l[1],l[1]+t*l[2]],
                          [l[1]+t*l[2],l[2]+t*l[3]]])
            try:
                ct=linalg.cholesky((top+top.T)/2,lower=True)
                cb=linalg.cholesky((low+low.T)/2,lower=True)
            except linalg.LinAlgError:
                print(json.dumps({'status':'nonpositive_diagonal_or_roundoff','n':n,'s':s,'weights':w.tolist(),'t':float(t)}),flush=True)
                continue
            x=linalg.solve_triangular(ct,rr,lower=True)
            x=linalg.solve_triangular(cb,x.T,lower=True).T
            rho=float(t*linalg.svdvals(x)[0]**2)
            if rho>worst[0]:worst=(rho,(n,s,w.tolist(),float(t)))
            if rho>1.000001:
                print(json.dumps({'status':'STRONG_QUADRATIC_PENCIL_CANDIDATE_FAILURE','worst':worst}),flush=True)
                raise SystemExit()
    print(json.dumps({'status':'case_done','n':n,'s':s,'worst':worst}),flush=True)
print(json.dumps({'status':'NO_FAILURE','worst':worst}),flush=True)
