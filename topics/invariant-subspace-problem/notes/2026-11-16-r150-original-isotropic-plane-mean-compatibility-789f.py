#!/usr/bin/env python3
"""Exact mean-elimination compatibility on the two original isotropic planes.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.

Keep every physical Hankel condition on Sym^2 W and Sym^3 W. Compute the
full ten ordinary coefficients of T3=Q*l, eliminate only the constant V/l
columns by an exact full left kernel, and retain all mean parameters.
This is a complete parameter calculation on the stipulated supported planes,
not an assertion that all critical points have those supports.
"""
import argparse
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import resource
import signal
import sys
import time

import sympy as sp

FORMAT="r150-original-isotropic-plane-mean-compatibility-v1"
KRAW=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],
      [0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]]
DATA={
 "plus":{"p":[sp.Rational(-8,5),sp.Rational(32,5),-5,1],
         "c":[[279,121,608],[121,-521,-608],[608,-608,-1024]]},
 "minus":{"p":[sp.Rational(864,5),sp.Rational(864,5),27,1],
          "c":[[-1769,1369,5024],[1369,-969,-5024],[5024,-5024,-1024]]},
}
a=sp.symbols("a0 a1 a2")
u=sp.symbols("u0 u1 u2")
t=sp.symbols("t")
MON2=list(itertools.combinations_with_replacement(range(3),2))
MON3=list(itertools.combinations_with_replacement(range(3),3))

def need(ok,msg):
    if not ok: raise ValueError(msg)

def canon(x):
    return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()

def sha(x): return hashlib.sha256(x).hexdigest()

def mv(A): return [[str(A[i,j]) for j in range(A.cols)] for i in range(A.rows)]

def full_kernel(A):
    R,pp=A.rref()
    pp=list(pp)
    ff=[j for j in range(A.cols) if j not in pp]
    X=sp.zeros(A.cols,len(ff))
    for k,j in enumerate(ff):
        X[j,k]=1
        for i,p in enumerate(pp): X[p,k]=-R[i,j]
    need(A*X==sp.zeros(A.rows,len(ff)),"complete exact original nullspace product")
    need(X.extract(ff,range(len(ff)))==sp.eye(len(ff)),"full original free identity")
    return X,pp,ff

def multiplicity(key):
    v=math.factorial(len(key))
    for k in set(key): v//=math.factorial(key.count(k))
    return v

def tensor_polynomial(coords,keys):
    return sp.expand(sum(multiplicity(k)*coords[i]*
                         sp.prod(u[j] for j in k) for i,k in enumerate(keys)))

def coeff3(p):
    P=sp.Poly(sp.expand(p),*u)
    need(P.total_degree()<=3,"all ordinary cubic coefficients")
    return sp.Matrix([P.coeff_monomial(sp.prod(u[j] for j in k)) for k in MON3])

def physical_map(E,degree,keys):
    original=list(itertools.combinations_with_replacement(range(6),degree))
    P=sp.zeros(len(original),len(keys))
    for i,key in enumerate(original):
        for j,small in enumerate(keys):
            P[i,j]=sum(sp.prod(E[key[k],perm[k]] for k in range(degree))
                       for perm in set(itertools.permutations(small)))
    first={}
    constraints=[]
    for i,key in enumerate(original):
        s=sum(key)
        if s in first: constraints.append(P[i,:]-P[first[s],:])
        else: first[s]=i
    C=sp.Matrix.vstack(*constraints) if constraints else sp.zeros(0,len(keys))
    Z,piv,free=full_kernel(C)
    original_columns=P*Z
    for i,key in enumerate(original):
        need(original_columns[i,:]==original_columns[first[sum(key)],:],
             "all original physical Hankel positions equal")
    return P,C,Z,original,first,piv,free

def factored_poly(p):
    pp=sp.Poly(sp.expand(p),*a,domain=sp.QQ)
    unit,fs=sp.factor_list(pp)
    product=sp.Poly(unit,*a,domain=sp.QQ)
    for f,e in fs: product*=f**e
    need(product==pp,"all rational factor coefficients multiplied back")
    return {"expanded":str(pp.as_expr()),"degree":pp.total_degree(),
            "unit":str(unit),"factors":[{"polynomial":str(f.as_expr()),"exponent":e,
                                        "degree":f.total_degree()} for f,e in fs]}

def one(sign):
    info=DATA[sign]
    P=info["p"]
    E=sp.zeros(6,3)
    for i in range(3): E[i,i]=1
    for i in range(3,6):
        for j in range(3): E[i,j]=-sum(P[k]*E[i-3+k,j] for k in range(3))
    K=sp.Matrix(KRAW);Cq=sp.Matrix(info["c"])
    need(E[:3,:]==sp.eye(3) and E.T*K*E==sp.zeros(3),"same original rational isotropic plane")
    need(Cq.det()!=0,"original projection quadratic is nondegenerate")
    vp=sp.Matrix([t**j for j in range(6)])
    polarity=E.T*K*vp
    pp=sp.Poly(sum(P[i]*t**i for i in range(4)),t)
    psi=[]
    for f in polarity:
        q,r=sp.div(sp.Poly(f,t),pp)
        need(r.is_zero,"entire original P factor in the physical projection")
        psi.append(q.as_expr())
    need(sp.expand((sp.Matrix(psi).T*Cq*sp.Matrix(psi))[0])==0,
         "full original physical projection quadratic identity")
    Hmap,HC,ZH,Hkeys,Hfirst,Hp,Hf=physical_map(E,2,MON2)
    Vmap,VC,ZV,Vkeys,Vfirst,Vpiv,Vfree=physical_map(E,3,MON3)
    Hpoly=[tensor_polynomial(ZH[:,i],MON2) for i in range(ZH.cols)]
    Vpoly=[tensor_polynomial(ZV[:,i],MON3) for i in range(ZV.cols)]
    Q=sp.expand((sp.Matrix(u).T*Cq*sp.Matrix(u))[0])
    constant=sp.Matrix.hstack(*[4*coeff3(x) for x in Vpoly],
                             *[-coeff3(Q*u[i]) for i in range(3)])
    LK,cp,cf=full_kernel(constant.T)
    quotient=LK.T
    mean=sum(a[i]*u[i] for i in range(3))
    hcols=sp.Matrix.hstack(*[-6*coeff3(mean*x) for x in Hpoly])
    rhs=coeff3(mean**3)
    low=quotient*hcols
    reduced_rhs=quotient*rhs
    whole=sp.Matrix.hstack(hcols,constant)
    need(quotient*constant==sp.zeros(quotient.rows,constant.cols),
         "all constant V and Q-linear source directions eliminated exactly")
    need(quotient.cols==10,"all ten original ordinary cubic positions retained")
    mean6=E*sp.Matrix(a)
    cat=sp.Matrix([[mean6[i+j] for j in range(3)] for i in range(4)])
    catmins=[sp.expand(cat.extract(rows,range(3)).det())
             for rows in itertools.combinations(range(4),3)]
    nonzero=[sp.Poly(x,*a,domain=sp.QQ) for x in catmins if x!=0]
    need(nonzero,"original catalecticant is not identically deficient on the plane")
    catgcd=nonzero[0]
    for p in nonzero[1:]: catgcd=sp.gcd(catgcd,p)
    catgcd=catgcd.monic()
    need(all(sp.rem(p,catgcd).is_zero for p in nonzero),
         "all four original catalecticant minors divided by their exact gcd")
    result={
     "plane":sign,"E":mv(E),"originalCq":mv(Cq),
     "mean":[str(x) for x in mean6],
     "physicalHConstraintShape":[HC.rows,HC.cols],"physicalHConstraintRank":len(Hp),
     "physicalHCompleteKernel":mv(ZH),"physicalHFreeColumns":Hf,
     "physicalVConstraintShape":[VC.rows,VC.cols],"physicalVConstraintRank":len(Vpiv),
     "physicalVCompleteKernel":mv(ZV),"physicalVFreeColumns":Vfree,
     "Hpolynomials":[str(x) for x in Hpoly],"Vpolynomials":[str(x) for x in Vpoly],
     "fullTenCoefficientMatrix":mv(whole),
     "constantSixColumnMatrix":mv(constant),"constantSourceRank":len(cp),
     "fullConstantLeftKernel":mv(LK),
     "reducedHShape":[low.rows,low.cols],"reducedHMatrix":mv(low),
     "reducedCubicRightHandSide":mv(reduced_rhs),
     "allOriginalCatalecticantMinors":[str(x) for x in catmins],
     "catalecticantGcd":factored_poly(catgcd.as_expr()),
     "allPhysicalHankelEqualitiesVerified":True,
     "allOriginalProjectionPolynomialCoefficientsVerified":True,
     "allTenCubicCoefficientPositionsRetained":True,
     "parameterScope":"all means and allowed moments supported on this original W",
    }
    if low.rows==low.cols+1:
        aug=sp.Matrix.hstack(low,reduced_rhs)
        det=sp.expand(aug.det(method="domain-ge"))
        result["augmentedCompatibilityDeterminant"]=factored_poly(det)
        if det!=0:
            quotient_det,remainder=sp.div(sp.Poly(det,*a,domain=sp.QQ),catgcd**2)
            result["compatibilityDividedByCatalecticantSquare"]={
              "quotient":str(quotient_det.as_expr()),"remainder":str(remainder.as_expr()),
              "exact":remainder.is_zero,
            }
            hminors=[sp.expand(low.extract(rows,range(low.cols)).det())
                     for rows in itertools.combinations(range(low.rows),low.cols)]
            result["allReducedHMaximalMinors"]=[factored_poly(x) for x in hminors]
            result["nonzeroDeterminantIsOnlyNecessaryWithoutSourceLift"]=True
    return result

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--out",required=True)
    parser.add_argument("--seconds",type=float,default=60)
    parser.add_argument("--memory-mib",type=int,default=1024)
    ar=parser.parse_args()
    need(5<=ar.seconds<=180 and 512<=ar.memory_mib<=2048,"bounded exact small parameter task")
    out=Path(ar.out);out.mkdir(parents=True,exist_ok=True)
    resource.setrlimit(resource.RLIMIT_AS,(ar.memory_mib*1024**2,ar.memory_mib*1024**2))
    start=time.monotonic()
    source_sha=sha(Path(__file__).read_bytes())
    rec={"format":FORMAT,"sourceSha256":source_sha,"status":"started",
         "binding":sha(canon({"format":FORMAT,"sourceSha256":source_sha,"K":KRAW,
                             "signs":["plus","minus"]})),
         "parameters":{"seconds":ar.seconds,"memoryMiB":ar.memory_mib}}
    def timeout(*args): raise TimeoutError("exact two-plane parameter budget")
    signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,ar.seconds)
    code=1
    try:
        allr=[one(sign) for sign in ("plus","minus")]
        raw=canon({"format":FORMAT+"-complete-parameters","binding":rec["binding"],"planes":allr})
        path=out/"complete-original-two-plane-parameters.json"
        tmp=path.with_suffix(".tmp");tmp.write_bytes(raw);os.replace(tmp,path)
        rec["parameters"]["completeParameterModel"]={"path":path.name,"bytes":len(raw),"sha256":sha(raw)}
        rec["parameters"]["planes"]=[{k:r[k] for k in [
            "plane","physicalHConstraintShape","physicalHConstraintRank",
            "physicalVConstraintShape","physicalVConstraintRank","constantSourceRank",
            "reducedHShape","catalecticantGcd","augmentedCompatibilityDeterminant",
            "compatibilityDividedByCatalecticantSquare"] if k in r} for r in allr]
        rec["status"]="completed";code=0
    except BaseException as exc:
        code=75 if isinstance(exc,TimeoutError) else 1
        rec["status"]="budget-prefix" if code==75 else "failed"
        rec["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)}
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        rec["elapsedSeconds"]=time.monotonic()-start
        raw=json.dumps(rec,ensure_ascii=False,sort_keys=True,indent=2).encode()
        path=out/"original-two-plane-mean-compatibility-receipt.json";path.write_bytes(raw)
        print(json.dumps({"receipt":{"path":path.name,"bytes":len(raw),"sha256":sha(raw)},
                          "exitCode":code,"result":rec},ensure_ascii=False,sort_keys=True),flush=True)
    return code

if __name__=="__main__":sys.exit(main())
