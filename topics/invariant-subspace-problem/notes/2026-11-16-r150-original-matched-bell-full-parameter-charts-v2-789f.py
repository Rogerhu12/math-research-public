#!/usr/bin/env python3
"""Complete original matched Bell coefficient charts and weighted-six source gate.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.

Use the literal K, all physical Hankel coordinates, and the original J3
inverse.  No mean is fixed.  Independently check all seventeen Schur
derivatives against the original N/Gamma formulas.  Work over the exact
matched cubic field for Bell coefficients.  The optional finite-field
weighted-six gate retains EVERY original weighted source and output.
A positive finite-field membership is never called a rational certificate.
"""
import argparse, gzip, hashlib, itertools, json, math, os
from pathlib import Path
import resource, signal, sys, time
from flint import fmpq, fmpq_mat, fmpq_poly, fmpq_mpoly_ctx, nmod_mat

FORMAT="r150-original-matched-bell-full-parameter-charts-v2"
KRAW=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],
      [0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]]
J3DET=23366320238786911411830138211362846399922176000
MATCHED=[52565262336,6080833024,-43931504,3725]
PRIME=127
VARNAMES=tuple("y%d"%i for i in range(6))+tuple("H%d"%i for i in range(11))
CTX=fmpq_mpoly_ctx.get(VARNAMES)
GEN=CTX.gens()
ZERO=CTX.from_dict({})
WEIGHTS=(1,)*6+(2,)*11

def need(ok,msg):
    if not ok: raise ValueError(msg)
def canon(x): return json.dumps(x,sort_keys=True,separators=(",",":")).encode("ascii")
def sha(x): return hashlib.sha256(x).hexdigest()
def save_json(p,x):
    b=json.dumps(x,sort_keys=True,indent=2).encode("ascii")
    q=p.with_name(p.name+".tmp");q.write_bytes(b);os.replace(q,p)
    return {"path":p.name,"bytes":len(b),"sha256":sha(b)}
def save_gz(p,x):
    b=canon(x);z=gzip.compress(b,compresslevel=1,mtime=0)
    q=p.with_name(p.name+".tmp");q.write_bytes(z);os.replace(q,p)
    return {"path":p.name,"bytes":len(z),"sha256":sha(z),
            "logicalBytes":len(b),"logicalSha256":sha(b)}
def vals(x): return [str(x[i]) for i in range(3)]
def pv(p): return [[[int(z) for z in e],str(q)] for e,q in sorted(p.to_dict().items())]
def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),ZERO)
             for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,b):return [sum((a*x for a,x in zip(row,b)),ZERO) for row in A]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),ZERO)
def conv(a,b):
    o=[ZERO for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):o[i+j]+=x*y
    return o
def tr(A):return sum((A[i][i] for i in range(len(A))),ZERO)
def weighted(p,w):
    need(all(sum(a*b for a,b in zip(e,WEIGHTS))==w for e in p.to_dict()),
         "all complete polynomial terms have their original weight")
def j3():
    p={(0,0):1};b={(i,j):KRAW[i][j] for i in range(6) for j in range(6) if KRAW[i][j]}
    for _ in range(3):
        n={}
        for (i,j),a in p.items():
            for (k,l),c in b.items():n[i+k,j+l]=n.get((i+k,j+l),0)+a*c
        p={k:v for k,v in n.items() if v}
    J=fmpq_mat([[p.get((i,j),0) for j in range(16)] for i in range(16)])
    need(J.det()==J3DET,"literal original J3 determinant")
    Ji=J.inv();I=fmpq_mat([[int(i==j) for j in range(16)] for i in range(16)])
    need(J*Ji==I and Ji*J==I,"all512 original inverse products")
    return J,Ji

class Field:
    def __init__(self):
        self.f=fmpq_poly([fmpq(x,MATCHED[-1]) for x in MATCHED])
        self.zero=fmpq_poly();self.one=fmpq_poly([1]);self.ninv=0
    def v(self,x):return fmpq_poly([fmpq(x)])
    def red(self,x):return x%self.f
    def mul(self,a,b):return (a*b)%self.f
    def inv(self,a):
        g,x,y=a.xgcd(self.f);need(g==self.one,"genuine matched-field inverse")
        z=x%self.f;need(self.mul(a,z)==self.one,"every matched-field inverse product")
        self.ninv+=1;return z
    def mul_polys(self,a,b):
        o=[ZERO for _ in range(5)]
        for i in range(3):
            for j in range(3):o[i+j]+=a[i]*b[j]
        for d in (4,3):
            for j in range(3):o[d-3+j]-=o[d]*self.f[j]
            o[d]=ZERO
        return o[:3]
    def scale_polys(self,a,c):
        return self.mul_polys(a,[CTX.from_dict({(0,)*17:c[i]}) if c[i] else ZERO for i in range(3)])

def irreducible():
    primes=[101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199]
    for p in primes:
        if MATCHED[-1]%p==0:continue
        values=[]
        for x in range(p):
            v=0
            for c in reversed(MATCHED):v=(v*x+c)%p
            values.append(v)
        if all(values):
            return {"prime":p,"allRootValuesNonzero":True,
                    "rootValuesSha256":sha(canon(values)),
                    "criterion":"a degree-three polynomial with no field root is irreducible"}
    raise ValueError("fixed prime list did not prove cubic irreducible")

def rank_and_rows(F,A):
    R=[list(row) for row in A];idx=list(range(len(A)));row=0;piv=[]
    for j in range(len(A[0])):
        k=next((i for i in range(row,len(A)) if R[i][j]),None)
        if k is None:continue
        R[row],R[k]=R[k],R[row];idx[row],idx[k]=idx[k],idx[row]
        inv=F.inv(R[row][j]);R[row]=[F.mul(x,inv) for x in R[row]]
        for i in range(len(A)):
            if i!=row and R[i][j]:
                c=R[i][j];R[i]=[(x-F.mul(c,y))%F.f for x,y in zip(R[i],R[row])]
        piv.append(j);row+=1
    return row,idx[:row],piv

def square_inverse(F,A):
    n=len(A);R=[list(row)+[F.v(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        p=next((i for i in range(j,n) if R[i][j]),None)
        need(p is not None,"actual selected Bell coefficient minor")
        R[j],R[p]=R[p],R[j];v=F.inv(R[j][j]);R[j]=[F.mul(x,v) for x in R[j]]
        for i in range(n):
            if i!=j and R[i][j]:
                c=R[i][j];R[i]=[(x-F.mul(c,y))%F.f for x,y in zip(R[i],R[j])]
    V=[row[n:] for row in R]
    for i in range(n):
        for j in range(n):
            need(sum((F.mul(A[i][k],V[k][j]) for k in range(n)),F.zero)%F.f==F.v(i==j),
                 "all original coefficient right-inverse coordinates")
            need(sum((F.mul(V[i][k],A[k][j]) for k in range(n)),F.zero)%F.f==F.v(i==j),
                 "all original coefficient left-inverse coordinates")
    return V

def weighted_monomials(w):
    out=[]
    for hdegree in range(w//2+1):
        yd=w-2*hdegree
        for ys in itertools.combinations_with_replacement(range(6),yd):
            for hs in itertools.combinations_with_replacement(range(11),hdegree):
                e=[0]*17
                for i in ys:e[i]+=1
                for i in hs:e[6+i]+=1
                out.append(tuple(e))
    return out

def field127(q):
    q=fmpq(q);d=int(q.denom())%PRIME
    need(d!=0,"every original rational coefficient is127 integral")
    return int(q.numer())%PRIME*pow(d,-1,PRIME)%PRIME

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",required=True)
    ap.add_argument("--seconds",type=float,default=180)
    ap.add_argument("--memory-mib",type=int,default=2048)
    ap.add_argument("--weight-six",action="store_true")
    a=ap.parse_args();need(0<a.seconds<=300 and 512<=a.memory_mib<=4096,"bounded exact original budget")
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    started=time.monotonic();ss=sha(Path(__file__).read_bytes())
    binding=sha(canon({"format":FORMAT,"sourceSha256":ss,"K":KRAW,
                      "matchedCubic":MATCHED,"weights":WEIGHTS,"prime":PRIME,
                      "weightSixRequested":a.weight_six}))
    rec={"format":FORMAT,"binding":binding,"sourceSha256":ss,"status":"started",
         "parameters":{"originalFreeMeanVariables":6,"originalHankelVariables":11,
             "meanNotSpecialized":True,"seconds":a.seconds,"memoryMiB":a.memory_mib}}
    def timeout(signum,frame):raise TimeoutError("bounded exact matched Bell model")
    signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,a.seconds)
    code=1
    try:
        ir=irreducible();FF=Field();d=fmpq_poly([0,1])
        A=FF.mul(-(521*d*d-46784*d+271360),FF.inv(160*(5*d-704)))
        r=[A,(A+d)%FF.f,FF.zero,FF.zero,FF.zero,FF.one]
        need((160*(5*d-704)*A+521*d*d-46784*d+271360)%FF.f==0,
             "complete unchanged matched direction relation")
        J,Ji=j3();y=list(GEN[:6]);h=list(GEN[6:])
        H=[[h[i+j] for j in range(6)] for i in range(6)]
        p=mv(KRAW,y);F=dot(y,p)/2
        KH=mm(KRAW,H);KH2=mm(KH,KH);HKH=mm(H,KH);KHK=mm(KRAW,mm(H,KRAW))
        b=dot(p,mv(H,p));c=dot(p,mv(HKH,p));tau2=tr(KH2);tau3=tr(mm(KH2,KH))
        G=F**3-6*F*b+6*F*tau2+12*c-8*tau3
        qpolar=[sum((KHK[i][j] for i in range(6) for j in range(6) if i+j==k),ZERO) for k in range(11)]
        dp=conv(conv(p,p),p);ep=conv(qpolar,p);ell=[dp[i]-6*ep[i] for i in range(16)]
        ellinv=[sum((ell[j]*Ji[i,j] for j in range(16)),ZERO) for i in range(16)]
        R=G-dot(ell,ellinv)/2;weighted(R,6)
        eq=[R.derivative(6+i) for i in range(11)]+[R.derivative(i) for i in range(6)]
        for i,z in enumerate(eq):weighted(z,4 if i<11 else 5)
        V=[-z/4 for z in ellinv];Hp=mv(H,p)
        N=[[F*y[i]*y[j]-2*F*H[i][j]-2*(y[i]*Hp[j]+Hp[i]*y[j])
            +4*sum((V[i+j+k]*p[k] for k in range(6)),ZERO)+4*HKH[i][j]
            for j in range(6)] for i in range(6)]
        KNK=mm(KRAW,mm(N,KRAW))
        origH=[-6*sum((KNK[i][j] for i in range(6) for j in range(6) if i+j==m),ZERO) for m in range(11)]
        HKHp=mv(HKH,p)
        Gam=[(F**2-2*b+2*tau2)*y[i]-4*F*Hp[i]+8*HKHp[i]
             +4*sum((V[i+j+k]*p[j]*p[k] for j in range(6) for k in range(6)),ZERO)
             -8*sum((V[i+j+k]*KHK[j][k] for j in range(6) for k in range(6)),ZERO) for i in range(6)]
        origY=[3*z for z in mv(KRAW,Gam)]
        need(eq==origH+origY,"all seventeen original full-parameter Schur and N/Gamma polynomials")
        need(6*R==sum((y[i]*eq[11+i] for i in range(6)),ZERO)+
             2*sum((h[i]*eq[i] for i in range(11)),ZERO),"complete weighted Euler source identity")
        ar=[sum((y[i]*r[i][j] for i in range(6)),ZERO) for j in range(3)]
        rr=[FF.zero for _ in range(11)]
        for i in range(6):
            for j in range(6):rr[i+j]=(rr[i+j]+FF.mul(r[i],r[j]))%FF.f
        cr=[FF.zero for _ in range(16)]
        for i in range(6):
            for j in range(11):cr[i+j]=(cr[i+j]+FF.mul(r[i],rr[j]))%FF.f
        wr=[sum((cr[j]*Ji[i,j] for j in range(16)),FF.zero)%FF.f for i in range(16)]
        hr=[sum((h[i]*rr[i][j] for i in range(11)),ZERO) for j in range(3)]
        ar3=FF.mul_polys(FF.mul_polys(ar,ar),ar);ahr=FF.mul_polys(ar,hr)
        Bell=[ar3[k]-6*ahr[k]-sum((ell[i]*wr[i][k] for i in range(16)),ZERO) for k in range(3)]
        for z in Bell:weighted(z,3)
        L=[[FF.zero for _ in range(6)] for _ in range(11)]
        for m in range(11):
            for j in range(6):
                coefficients=[]
                for k in range(3):
                    pol=Bell[k].derivative(6+m)
                    need(all(sum(e[:6])==1 and not any(e[6:]) for e in pol.to_dict()),
                         "complete Bell Hankel coefficient is exactly linear in original mean")
                    ee=[0]*17;ee[j]=1;coefficients.append(pol.to_dict().get(tuple(ee),fmpq(0)))
                L[m][j]=fmpq_poly(coefficients)
        cubic=[Bell[k]-sum((h[m]*sum((y[j]*L[m][j][k] for j in range(6)),ZERO) for m in range(11)),ZERO) for k in range(3)]
        need(all(all(not any(e[6:]) for e in z.to_dict()) for z in cubic),
             "all complete Bell constant-in-H terms retained")
        independent=[[FF.zero for _ in range(6)] for _ in range(11)]
        for m in range(11):
            polar_m=[sum(KRAW[i][a0]*KRAW[b0][j] for i in range(6) for j in range(6)
                         for a0 in range(6) for b0 in range(6) if i+j==k and a0+b0==m) for k in range(11)]
            for j in range(6):
                s=FF.zero
                for k in range(11):
                    for i in range(6):s=(s+wr[k+i]*polar_m[k]*KRAW[i][j])%FF.f
                independent[m][j]=(6*(s-FF.mul(rr[m],r[j])))%FF.f
        need(independent==L,"all66 independent original Bell Hankel coefficient formulas")
        lr,rows,piv=rank_and_rows(FF,L)
        inverse=None
        if lr==6:inverse=square_inverse(FF,[L[i] for i in rows])
        model={"K":KRAW,"J3Determinant":str(J.det()),"matchedCubic":MATCHED,
               "matchedDirection":[vals(x) for x in r],
               "R3":pv(R),"originalSeventeenGradients":[pv(z) for z in eq],
               "BellFieldComponents":[pv(z) for z in Bell],
               "BellCubicMeanComponents":[pv(z) for z in cubic],
               "BellHankelMeanCoefficientMatrix":[[vals(x) for x in row] for row in L],
               "coefficientRank":lr,"originalIndependentHankelRows":rows,
               "coefficientColumnPivots":piv,
               "selectedCoefficientInverse":([[vals(x) for x in row] for row in inverse] if inverse else None),
               "irreducibilityCertificate":ir,"all512J3InverseProducts":True,
               "all17OriginalGradientPolynomialsVerified":True,"all66BellCoefficientFormulaProducts":True}
        desc=save_gz(out/"complete-original-matched-bell-parameter-model.json.gz",
                     {"format":FORMAT+"-model","binding":binding,"data":model})
        rec["parameters"].update({"model":desc,"irreducibility":ir,
            "all512OriginalJ3InverseCoordinatesVerified":True,
            "allSeventeenOriginalFullParameterGradientPolynomialsVerified":True,
            "allOriginalWeightedEulerCoefficientsVerified":True,
            "R3TermCount":len(R.to_dict()),
            "gradientTermCounts":[len(z.to_dict()) for z in eq],
            "BellFieldComponentTermCounts":[len(z.to_dict()) for z in Bell],
            "BellHankelCoefficientRank":lr,"BellHankelIndependentOriginalRows":rows,
            "all66IndependentBellCoefficientIdentitiesVerified":True,
            "all72OriginalCoefficientMinorInverseProductsVerified":inverse is not None,
            "matchedFieldInversesVerified":FF.ninv,
            "allNonzeroBellPointsCoveredByHankelCoefficientCharts":lr==6})
        if a.weight_six:
            mons=weighted_monomials(6);need(len(mons)==3520,"all3520 original weighted-six outputs")
            pos={e:i for i,e in enumerate(mons)};sources=[]
            for j,z in enumerate(eq):
                for mon in weighted_monomials(2 if j<11 else 1):sources.append((j,mon))
            need(len(sources)==388,"all388 original weighted-six source multiples")
            cols=[]
            for j,mon in sources:
                pol=eq[j]*CTX.from_dict({mon:1})
                need(all(e in pos for e in pol.to_dict()),"no weighted-six source term omitted")
                col=[0]*len(mons)
                for e,q in pol.to_dict().items():col[pos[e]]=field127(q)
                cols.append(col)
            B2=FF.mul_polys(Bell,Bell)
            tcols=[]
            for pol in B2:
                col=[0]*len(mons)
                for e,q in pol.to_dict().items():col[pos[e]]=field127(q)
                tcols.append(col)
            M=nmod_mat([[cols[j][i] for j in range(len(cols))] for i in range(len(mons))],PRIME)
            Mp=nmod_mat([[cols[j][i] for j in range(len(cols))]+[c[i] for c in tcols] for i in range(len(mons))],PRIME)
            ranks=[int(M.rank()),int(Mp.rank())]
            rec["parameters"]["weightedSix"]={"prime":PRIME,"sourceShape":[3520,388],
                "augmentedShape":[3520,391],"sourceRank":ranks[0],"augmentedRank":ranks[1],
                "allRationalCoefficients127Integral":True,
                "originalSourceDictionarySha256":sha(canon([[j,list(e)] for j,e in sources])),
                "originalOutputDictionarySha256":sha(canon([list(e) for e in mons])),
                "originalSourceFieldMatrixSha256":sha(bytes(x for c in cols for x in c)),
                "threeOriginalTargetFieldColumnsSha256":sha(bytes(x for c in tcols for x in c)),
                "rationalNonmembershipProvedByRankAboveAllSourceColumns":ranks[1]>388,
                "noFiniteFieldPositivePromotedToRationalMembership":True}
        rec["status"]="completed";code=0
    except BaseException as e:
        rec["status"]="budget-checkpoint" if isinstance(e,TimeoutError) else "failed"
        rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        code=75 if isinstance(e,TimeoutError) else 1
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        rec["elapsedSeconds"]=time.monotonic()-started
        desc=save_json(out/"original-matched-bell-full-parameter-receipt.json",rec)
        print(json.dumps({"status":rec["status"],"binding":binding,"exitCode":code,
                          "receipt":desc,"elapsedSeconds":rec["elapsedSeconds"],
                          "parameters":rec["parameters"]},sort_keys=True),flush=True)
    return code
if __name__=="__main__":sys.exit(main())
