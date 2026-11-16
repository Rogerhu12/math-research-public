#!/usr/bin/env python3
"""Exact original critical points on the two full mean-compatibility cubics.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.

Read only the complete original supported-plane parameter model.  At a=(1,0,t)
choose a proved irreducible factor of the non-Cat compatibility cubic, solve
ALL ten original coefficient equations, and verify ALL 33 original gradients
and physical Hankel positions over the resulting characteristic-zero field.
No scalar numerical approximation and no pointwise mod-p criticality is used.
"""
import argparse,hashlib,itertools,json,math,os
from pathlib import Path
import resource,signal,sys,time
import sympy as sp
from flint import fmpq,fmpq_poly

FORMAT="r150-original-isotropic-plane-cat3-critical-points-v1"
MODEL_SHA="17ecc103fd28b5e617353eda80c417494d2de03ca49836d6c64eb3c2e64f9f66"
MODEL_BYTES=26409
MODEL_BINDING="ed7174cd2a10d5eee4ddfa45f4d764385c6899f87c209b8d96696e82a9124956"
KRAW=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],
      [0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]]
PAID_J3_DET=23366320238786911411830138211362846399922176000
a=sp.symbols("a0 a1 a2");u=sp.symbols("u0 u1 u2");t=sp.symbols("t")
MON2=list(itertools.combinations_with_replacement(range(3),2))
MON3=list(itertools.combinations_with_replacement(range(3),3))

def need(ok,s):
    if not ok: raise ValueError(s)
def canon(o):return json.dumps(o,sort_keys=True,separators=(",",":")).encode()
def sha(x):return hashlib.sha256(x).hexdigest()
def scalar(x):return fmpq_poly([fmpq(str(x))])
def pars(s):return sp.sympify(s,locals={**{str(x):x for x in a},"t":t})

class Field:
    def __init__(self,fp):
        self.degree=fp.degree()
        self.f=fmpq_poly([fmpq(str(fp.nth(i))) for i in range(self.degree+1)])
        need(self.f[self.degree]==1,"monic exact number-field modulus")
        self.zero=fmpq_poly();self.one=scalar(1);self.inverse_count=0
    def red(self,x):return x%self.f
    def add(self,x,y):return (x+y)%self.f
    def neg(self,x):return (-x)%self.f
    def sub(self,x,y):return (x-y)%self.f
    def mul(self,x,y):return (x*y)%self.f
    def inv(self,x):
        g,s,v=x.xgcd(self.f)
        need(g==self.one,"true number-field inverse")
        q=s%self.f
        need(self.mul(x,q)==self.one,"number-field inverse multiplied back")
        self.inverse_count+=1;return q
    def div(self,x,y):return self.mul(x,self.inv(y))
    def sum(self,xs):
        r=self.zero
        for x in xs:r=self.add(r,x)
        return r
    def from_expr(self,x):
        q=sp.Poly(sp.expand(pars(x).subs({a[0]:1,a[1]:0,a[2]:t})),t,domain=sp.QQ)
        return self.red(fmpq_poly([fmpq(str(q.nth(i))) for i in range(q.degree()+1)])) if not q.is_zero else self.zero
    def values(self,x):return [str(x[i]) for i in range(self.degree)]
    def matrix_values(self,A):return [[self.values(x) for x in row] for row in A]

def mm(F,A,B):
    need(len(A[0])==len(B),"original matrix product shape")
    return [[F.sum(F.mul(A[i][k],B[k][j]) for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def mv(F,A,x):return [F.sum(F.mul(v,w) for v,w in zip(row,x)) for row in A]
def dot(F,x,y):return F.sum(F.mul(v,w) for v,w in zip(x,y))
def trans(A):return [list(x) for x in zip(*A)]
def conv(F,x,y):
    out=[F.zero for _ in range(len(x)+len(y)-1)]
    for i,v in enumerate(x):
        for j,w in enumerate(y):out[i+j]=F.add(out[i+j],F.mul(v,w))
    return out

def solve(F,A,b):
    n,m=len(A),len(A[0]);R=[list(row)+[b[i]] for i,row in enumerate(A)]
    piv=[];r=0
    for j in range(m):
        p=next((i for i in range(r,n) if R[i][j]),None)
        if p is None:continue
        R[r],R[p]=R[p],R[r]
        inv=F.inv(R[r][j]);R[r]=[F.mul(x,inv) for x in R[r]]
        for i in range(n):
            if i!=r and R[i][j]:
                q=R[i][j];R[i]=[F.sub(x,F.mul(q,y)) for x,y in zip(R[i],R[r])]
        piv.append(j);r+=1
    need(all(not any(R[i][j] for j in range(m)) and not R[i][m] for i in range(r,n)),
         "all original overdetermined rows are consistent")
    x=[F.zero for _ in range(m)]
    for i,j in enumerate(piv):x[j]=R[i][m]
    need(mv(F,A,x)==b,"all original source equations multiplied back")
    return x,piv
def rank(F,A):
    zero=[F.zero for _ in A]
    _,p=solve(F,A,zero);return len(p)

def irreducibility_prime(f):
    den=sp.ilcm(*[x.q for x in f.all_coeffs()])
    v=[int(f.nth(i)*den) for i in range(f.degree()+1)]
    cont=0
    for x in v:cont=math.gcd(cont,abs(x))
    v=[x//cont for x in v]
    for p in list(sp.primerange(101,1000)):
        if v[-1]%p==0:continue
        vals=[]
        for x in range(p):
            z=0
            for c in reversed(v):z=(z*x+c)%p
            vals.append(z)
        if all(vals):
            need(1<=f.degree()<=3,"root-free irreducibility criterion degree at most three")
            return {"prime":int(p),"degree":f.degree(),"allFieldValuesNonzero":True,
                    "fieldValuesCount":int(p),"primitiveIntegerCoefficients":v,
                    "fieldValuesSha256":sha(canon(vals))}
    raise ValueError("no bounded independent irreducibility prime found")

def j3():
    base={(i,j):KRAW[i][j] for i in range(6) for j in range(6) if KRAW[i][j]}
    p={(0,0):1}
    for _ in range(3):
        q={}
        for (i,j),c in p.items():
            for (k,l),d in base.items():q[i+k,j+l]=q.get((i+k,j+l),0)+c*d
        p={k:v for k,v in q.items() if v}
    J=sp.Matrix([[p.get((i,j),0) for j in range(16)] for i in range(16)])
    need(J.det()==PAID_J3_DET,"same complete original J3 determinant")
    return [[int(J[i,j]) for j in range(16)] for i in range(16)]

def one(model,J):
    cat=sp.Poly(pars(model["catalecticantGcd"]["expanded"]),*a,domain=sp.QQ)
    fs=model["augmentedCompatibilityDeterminant"]["factors"]
    rest=[pars(x["polynomial"]) for x in fs
          if not sp.rem(sp.Poly(pars(x["polynomial"]),*a,domain=sp.QQ),cat).is_zero]
    need(len(rest)==1,"one exact non-Cat compatibility cubic")
    specialized=sp.Poly(rest[0].subs({a[0]:1,a[1]:0,a[2]:t}),t,domain=sp.QQ)
    unit,factors=sp.factor_list(specialized)
    prod=sp.Poly(unit,t,domain=sp.QQ)
    for f,e in factors:prod*=f**e
    need(prod==specialized,"complete rational specialized factorization")
    catspec=sp.Poly(cat.as_expr().subs({a[0]:1,a[1]:0,a[2]:t}),t,domain=sp.QQ)
    chosen=None
    for fp,e in factors:
        if sp.gcd(fp,catspec).degree()==0:
            chosen=fp.monic();break
    need(chosen is not None and 1<=chosen.degree()<=3,"actual non-Cat characteristic-zero factor")
    irreducible=irreducibility_prime(chosen)
    F=Field(chosen)
    A=[[F.from_expr(x) for x in row] for row in model["fullTenCoefficientMatrix"]]
    mean=u[0]+t*u[2]
    rhsP=sp.Poly(sp.expand(-mean**3),*u)
    rhs=[F.from_expr(str(rhsP.coeff_monomial(sp.prod(u[j] for j in key)))) for key in MON3]
    x,piv=solve(F,A,rhs)
    need(len(piv)==9,"full nine original supported-moment and Q-linear columns")
    E=[[F.from_expr(s) for s in row] for row in model["E"]]
    ZH=[[F.from_expr(s) for s in row] for row in model["physicalHCompleteKernel"]]
    ZV=[[F.from_expr(s) for s in row] for row in model["physicalVCompleteKernel"]]
    hs=mv(F,ZH,x[:3]);vs=mv(F,ZV,x[3:6]);ell=x[6:9]
    need(any(ell),"nonzero complete Q-linear third moment")
    Hsmall=[[F.zero for _ in range(3)] for _ in range(3)]
    for v,(i,j) in zip(hs,MON2):Hsmall[i][j]=Hsmall[j][i]=v
    H=mm(F,mm(F,E,Hsmall),trans(E))
    y=mv(F,E,[F.one,F.zero,F.from_expr("t")])
    Vsmall={p:v for key,v in zip(MON3,vs) for p in set(itertools.permutations(key))}
    V={}
    for i in range(6):
        for j in range(6):
            for k in range(6):
                V[i,j,k]=F.sum(F.mul(F.mul(F.mul(E[i][r],E[j][s]),E[k][q]),Vsmall[r,s,q])
                              for r in range(3) for s in range(3) for q in range(3))
    hm=[None]*11;vm=[None]*16
    for i in range(6):
        for j in range(6):
            idx=i+j
            if hm[idx] is None:hm[idx]=H[i][j]
            need(H[i][j]==hm[idx],"all 36 original H Hankel positions")
            for k in range(6):
                idx3=i+j+k
                if vm[idx3] is None:vm[idx3]=V[i,j,k]
                need(V[i,j,k]==vm[idx3],"all 216 original V Hankel positions")
    K=[[scalar(c) for c in row] for row in KRAW]
    p=mv(F,K,y);FC=F.div(dot(F,y,p),scalar(2))
    Hp=mv(F,H,p);HKH=mm(F,mm(F,H,K),H);KHK=mm(F,mm(F,K,H),K)
    KH=mm(F,K,H);KH2=mm(F,KH,KH)
    b=dot(F,p,Hp);tau2=F.sum(KH2[i][i] for i in range(6))
    Vp=[[F.sum(F.mul(V[i,j,k],p[k]) for k in range(6)) for j in range(6)] for i in range(6)]
    N=[[F.add(F.sub(F.mul(FC,F.mul(y[i],y[j])),F.mul(scalar(2),F.mul(FC,H[i][j]))),
              F.add(F.mul(scalar(-2),F.add(F.mul(y[i],Hp[j]),F.mul(Hp[i],y[j]))),
                    F.add(F.mul(scalar(4),Vp[i][j]),F.mul(scalar(4),HKH[i][j]))))
        for j in range(6)] for i in range(6)]
    KNK=mm(F,mm(F,K,N),K)
    gradH=[F.mul(scalar(-6),F.sum(KNK[i][j] for i in range(6) for j in range(6) if i+j==s))
           for s in range(11)]
    HKHp=mv(F,HKH,p)
    Vpp=[F.sum(F.mul(V[i,j,k],F.mul(p[j],p[k])) for j in range(6) for k in range(6)) for i in range(6)]
    VKHK=[F.sum(F.mul(V[i,j,k],KHK[j][k]) for j in range(6) for k in range(6)) for i in range(6)]
    leading=F.add(F.sub(F.mul(FC,FC),F.mul(scalar(2),b)),F.mul(scalar(2),tau2))
    Gamma=[F.sum([F.mul(leading,y[i]),F.mul(scalar(-4),F.mul(FC,Hp[i])),
                  F.mul(scalar(8),HKHp[i]),F.mul(scalar(4),Vpp[i]),
                  F.mul(scalar(-8),VKHK[i])]) for i in range(6)]
    grady=[F.mul(scalar(3),v) for v in mv(F,K,Gamma)]
    polar=[F.sum(KHK[i][j] for i in range(6) for j in range(6) if i+j==s) for s in range(11)]
    d=conv(F,conv(F,p,p),p);ep=conv(F,polar,p)
    ellOriginal=[F.sub(d[i],F.mul(scalar(6),ep[i])) for i in range(16)]
    JV=mv(F,[[scalar(z) for z in row] for row in J],vm)
    gradV=[F.add(F.mul(scalar(4),ellOriginal[i]),F.mul(scalar(16),JV[i])) for i in range(16)]
    need(all(not q for q in gradH+grady+gradV),"all 33 original exact physical gradients")
    need(rank(F,[[y[i+j] for j in range(3)] for i in range(4)])==3,
         "complete original mean catalecticant rank three")
    # Ordinary T3 cubic in the three original plane coordinates.
    Tcoef=[]
    for row in range(10):
        Tcoef.append(F.add(F.neg(rhs[row]),F.sum(F.mul(A[row][j],x[j]) for j in range(6))))
    derivatives=[[F.zero for _ in MON2] for _ in range(3)]
    ix={key:i for i,key in enumerate(MON2)}
    for key,v in zip(MON3,Tcoef):
        for j in set(key):
            tail=list(key);tail.remove(j)
            derivatives[j][ix[tuple(tail)]]=F.mul(scalar(key.count(j)),v)
    erank=rank(F,derivatives)
    need(erank==3,"actual complete third moment essential rank three")
    return {
     "plane":model["plane"],"fieldPolynomial":str(chosen.as_expr()),
     "fieldDegree":F.degree,"irreducibilityCertificate":irreducible,
     "meanParameterCoordinates":[["1"],["0"],["0","1"]],
     "mean":F.matrix_values([y])[0],"HankelH":F.matrix_values([hm])[0],
     "HankelV":F.matrix_values([vm])[0],"Qlinear":F.matrix_values([ell])[0],
     "allNineSupportedSourceCoordinates":F.matrix_values([x])[0],
     "allTenOriginalCubicCoefficientEquationsVerified":True,
     "fullOriginalSupportedLinearRank":9,
     "all36HankelHPositionsVerified":True,"all216HankelVPositionsVerified":True,
     "all33OriginalGradientsVerified":True,
     "allOriginalGradientFieldCoordinates":33*F.degree,
     "meanCatalecticantRank":3,"thirdMomentEssentialRank":erank,
     "allOriginalThirdMomentCoefficientPositions":10,
     "allActualFieldInversesMultipliedBack":F.inverse_count,
     "noFiniteFieldCriticalPointLiftUsed":True,
     "notANonzeroMatchedBellExample":True,
    }

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--parameters",required=True);ap.add_argument("--out",required=True)
    ap.add_argument("--seconds",type=float,default=60);ap.add_argument("--memory-mib",type=int,default=1024)
    ar=ap.parse_args();need(5<=ar.seconds<=180 and 512<=ar.memory_mib<=2048,"bounded exact algebraic-point task")
    out=Path(ar.out);out.mkdir(parents=True,exist_ok=True)
    resource.setrlimit(resource.RLIMIT_AS,(ar.memory_mib*1024**2,ar.memory_mib*1024**2))
    start=time.monotonic();source_sha=sha(Path(__file__).read_bytes())
    rec={"format":FORMAT,"status":"started","sourceSha256":source_sha,
         "binding":sha(canon({"format":FORMAT,"sourceSha256":source_sha,"inputSha256":MODEL_SHA})),
         "parameters":{"seconds":ar.seconds,"memoryMiB":ar.memory_mib}}
    def stop(*args):raise TimeoutError("bounded exact original critical-point budget")
    signal.signal(signal.SIGALRM,stop);signal.setitimer(signal.ITIMER_REAL,ar.seconds);code=1
    try:
        raw=Path(ar.parameters).read_bytes()
        need(len(raw)==MODEL_BYTES and sha(raw)==MODEL_SHA,"entire paid original parameter model")
        model=json.loads(raw);need(model["binding"]==MODEL_BINDING,"original supported parameter binding")
        J=j3();points=[one(p,J) for p in model["planes"]]
        raw=canon({"format":FORMAT+"-points","binding":rec["binding"],"points":points})
        path=out/"complete-original-cat3-critical-points.json";path.write_bytes(raw)
        rec["parameters"]["completeOriginalPoints"]={"path":path.name,"bytes":len(raw),"sha256":sha(raw)}
        rec["parameters"]["points"]=[{k:p[k] for k in [
            "plane","fieldPolynomial","fieldDegree","irreducibilityCertificate",
            "allTenOriginalCubicCoefficientEquationsVerified","fullOriginalSupportedLinearRank",
            "all36HankelHPositionsVerified","all216HankelVPositionsVerified","all33OriginalGradientsVerified",
            "allOriginalGradientFieldCoordinates","meanCatalecticantRank","thirdMomentEssentialRank",
            "allActualFieldInversesMultipliedBack","noFiniteFieldCriticalPointLiftUsed",
            "notANonzeroMatchedBellExample"]} for p in points]
        rec["status"]="completed";code=0
    except BaseException as exc:
        code=75 if isinstance(exc,TimeoutError) else 1;rec["status"]="budget-prefix" if code==75 else "failed"
        rec["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)}
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);rec["elapsedSeconds"]=time.monotonic()-start
        raw=json.dumps(rec,sort_keys=True,indent=2).encode();path=out/"original-cat3-critical-points-receipt.json"
        path.write_bytes(raw)
        print(json.dumps({"exitCode":code,"receipt":{"path":path.name,"bytes":len(raw),"sha256":sha(raw)},"result":rec},
                         sort_keys=True),flush=True)
    return code
if __name__=="__main__":sys.exit(main())
