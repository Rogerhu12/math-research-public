#!/usr/bin/env python3
"""New complete five-dimensional matrix half budget for the original six-site S2.
The known 15-dimensional upper characteristic supplies its complete inverse.
The same two source terms and both cross terms form K. The new target is
I_L-2K, not the already disproved uniform trace-square quarter inequality.
Primitive-only continuing Faddeev reductions preserve exact integer divisions.
Every original new starting matrix, coefficient and continuation is retained
in compressed exact JSON; the same source can be resumed without a new inverse.
"""
from __future__ import annotations
import resource, signal
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
import argparse, base64, hashlib, itertools, json, math, time, zlib
from pathlib import Path
from flint import fmpz_mpoly_ctx

UPPER_CHAR=json.loads("[[[[\"1\",\"0\",\"0\",\"0\",\"0\",\"0\"],\"-10\"]],[[[\"2\",\"0\",\"0\",\"0\",\"0\",\"0\"],\"45\"]],[[[\"0\",\"0\",\"1\",\"0\",\"0\",\"0\"],\"-12\"],[[\"3\",\"0\",\"0\",\"0\",\"0\",\"0\"],\"-120\"]],[[[\"0\",\"0\",\"0\",\"1\",\"0\",\"0\"],\"-48\"],[[\"1\",\"0\",\"1\",\"0\",\"0\",\"0\"],\"96\"],[[\"4\",\"0\",\"0\",\"0\",\"0\",\"0\"],\"210\"]],[[[\"0\",\"0\",\"0\",\"0\",\"1\",\"0\"],\"-528\"],[[\"1\",\"0\",\"0\",\"1\",\"0\",\"0\"],\"336\"],[[\"2\",\"0\",\"1\",\"0\",\"0\",\"0\"],\"-336\"],[[\"5\",\"0\",\"0\",\"0\",\"0\",\"0\"],\"-252\"]],[[[\"0\",\"0\",\"0\",\"0\",\"0\",\"1\"],\"-6912\"],[[\"0\",\"0\",\"2\",\"0\",\"0\",\"0\"],\"48\"],[[\"1\",\"0\",\"0\",\"0\",\"1\",\"0\"],\"3072\"],[[\"2\",\"0\",\"0\",\"1\",\"0\",\"0\"],\"-1008\"],[[\"3\",\"0\",\"1\",\"0\",\"0\",\"0\"],\"672\"],[[\"6\",\"0\",\"0\",\"0\",\"0\",\"0\"],\"210\"]],[[[\"0\",\"0\",\"1\",\"1\",\"0\",\"0\"],\"384\"],[[\"0\",\"1\",\"0\",\"0\",\"1\",\"0\"],\"-768\"],[[\"1\",\"0\",\"0\",\"0\",\"0\",\"1\"],\"31104\"],[[\"1\",\"0\",\"2\",\"0\",\"0\",\"0\"],\"-288\"],[[\"2\",\"0\",\"0\",\"0\",\"1\",\"0\"],\"-7344\"],[[\"3\",\"0\",\"0\",\"1\",\"0\",\"0\"],\"1680\"],[[\"4\",\"0\",\"1\",\"0\",\"0\",\"0\"],\"-840\"],[[\"7\",\"0\",\"0\",\"0\",\"0\",\"0\"],\"-120\"]],[[[\"0\",\"0\",\"0\",\"2\",\"0\",\"0\"],\"768\"],[[\"0\",\"0\",\"1\",\"0\",\"1\",\"0\"],\"1920\"],[[\"0\",\"1\",\"0\",\"0\",\"0\",\"1\"],\"-23040\"],[[\"1\",\"0\",\"1\",\"1\",\"0\",\"0\"],\"-1920\"],[[\"1\",\"1\",\"0\",\"0\",\"1\",\"0\"],\"3840\"],[[\"2\",\"0\",\"0\",\"0\",\"0\",\"1\"],\"-51840\"],[[\"2\",\"0\",\"2\",\"0\",\"0\",\"0\"],\"720\"],[[\"3\",\"0\",\"0\",\"0\",\"1\",\"0\"],\"9120\"],[[\"4\",\"0\",\"0\",\"1\",\"0\",\"0\"],\"-1680\"],[[\"5\",\"0\",\"1\",\"0\",\"0\",\"0\"],\"672\"],[[\"8\",\"0\",\"0\",\"0\",\"0\",\"0\"],\"45\"]],[[[\"0\",\"0\",\"0\",\"1\",\"1\",\"0\"],\"7680\"],[[\"0\",\"0\",\"1\",\"0\",\"0\",\"1\"],\"-27648\"],[[\"0\",\"0\",\"3\",\"0\",\"0\",\"0\"],\"-64\"],[[\"0\",\"2\",\"0\",\"0\",\"1\",\"0\"],\"-256\"],[[\"1\",\"0\",\"0\",\"2\",\"0\",\"0\"],\"-3072\"],[[\"1\",\"0\",\"1\",\"0\",\"1\",\"0\"],\"-6912\"],[[\"1\",\"1\",\"0\",\"0\",\"0\",\"1\"],\"89856\"],[[\"2\",\"0\",\"1\",\"1\",\"0\",\"0\"],\"3840\"],[[\"2\",\"1\",\"0\",\"0\",\"1\",\"0\"],\"-7680\"],[[\"3\",\"0\",\"0\",\"0\",\"0\",\"1\"],\"34560\"],[[\"3\",\"0\",\"2\",\"0\",\"0\",\"0\"],\"-960\"],[[\"4\",\"0\",\"0\",\"0\",\"1\",\"0\"],\"-6000\"],[[\"5\",\"0\",\"0\",\"1\",\"0\",\"0\"],\"1008\"],[[\"6\",\"0\",\"1\",\"0\",\"0\",\"0\"],\"-336\"],[[\"9\",\"0\",\"0\",\"0\",\"0\",\"0\"],\"-10\"]],[[[\"0\",\"0\",\"0\",\"0\",\"2\",\"0\"],\"25344\"],[[\"0\",\"0\",\"0\",\"1\",\"0\",\"1\"],\"-110592\"],[[\"0\",\"0\",\"2\",\"1\",\"0\",\"0\"],\"-768\"],[[\"0\",\"1\",\"1\",\"0\",\"1\",\"0\"],\"3072\"],[[\"0\",\"2\",\"0\",\"0\",\"0\",\"1\"],\"-18432\"],[[\"1\",\"0\",\"0\",\"1\",\"1\",\"0\"],\"-19968\"],[[\"1\",\"0\",\"1\",\"0\",\"0\",\"1\"],\"96768\"],[[\"1\",\"0\",\"3\",\"0\",\"0\",\"0\"],\"256\"],[[\"1\",\"2\",\"0\",\"0\",\"1\",\"0\"],\"1024\"],[[\"2\",\"0\",\"0\",\"2\",\"0\",\"0\"],\"4608\"],[[\"2\",\"0\",\"1\",\"0\",\"1\",\"0\"],\"8448\"],[[\"2\",\"1\",\"0\",\"0\",\"0\",\"1\"],\"-129024\"],[[\"3\",\"0\",\"1\",\"1\",\"0\",\"0\"],\"-3840\"],[[\"3\",\"1\",\"0\",\"0\",\"1\",\"0\"],\"7680\"],[[\"4\",\"0\",\"2\",\"0\",\"0\",\"0\"],\"720\"],[[\"5\",\"0\",\"0\",\"0\",\"1\",\"0\"],\"1728\"],[[\"6\",\"0\",\"0\",\"1\",\"0\",\"0\"],\"-336\"],[[\"7\",\"0\",\"1\",\"0\",\"0\",\"0\"],\"96\"],[[\"10\",\"0\",\"0\",\"0\",\"0\",\"0\"],\"1\"]],[[[\"0\",\"0\",\"0\",\"0\",\"1\",\"1\"],\"-110592\"],[[\"0\",\"0\",\"1\",\"2\",\"0\",\"0\"],\"-3072\"],[[\"0\",\"0\",\"2\",\"0\",\"1\",\"0\"],\"768\"],[[\"0\",\"1\",\"0\",\"1\",\"1\",\"0\"],\"12288\"],[[\"0\",\"1\",\"1\",\"0\",\"0\",\"1\"],\"-18432\"],[[\"1\",\"0\",\"0\",\"0\",\"2\",\"0\"],\"-50688\"],[[\"1\",\"0\",\"0\",\"1\",\"0\",\"1\"],\"276480\"],[[\"1\",\"0\",\"2\",\"1\",\"0\",\"0\"],\"2304\"],[[\"1\",\"1\",\"1\",\"0\",\"1\",\"0\"],\"-9216\"],[[\"1\",\"2\",\"0\",\"0\",\"0\",\"1\"],\"55296\"],[[\"2\",\"0\",\"0\",\"1\",\"1\",\"0\"],\"13824\"],[[\"2\",\"0\",\"1\",\"0\",\"0\",\"1\"],\"-124416\"],[[\"2\",\"0\",\"3\",\"0\",\"0\",\"0\"],\"-384\"],[[\"2\",\"2\",\"0\",\"0\",\"1\",\"0\"],\"-1536\"],[[\"3\",\"0\",\"0\",\"2\",\"0\",\"0\"],\"-3072\"],[[\"3\",\"0\",\"1\",\"0\",\"1\",\"0\"],\"-3072\"],[[\"3\",\"1\",\"0\",\"0\",\"0\",\"1\"],\"78336\"],[[\"4\",\"0\",\"1\",\"1\",\"0\",\"0\"],\"1920\"],[[\"4\",\"1\",\"0\",\"0\",\"1\",\"0\"],\"-3840\"],[[\"5\",\"0\",\"0\",\"0\",\"0\",\"1\"],\"-10368\"],[[\"5\",\"0\",\"2\",\"0\",\"0\",\"0\"],\"-288\"],[[\"6\",\"0\",\"0\",\"0\",\"1\",\"0\"],\"48\"],[[\"7\",\"0\",\"0\",\"1\",\"0\",\"0\"],\"48\"],[[\"8\",\"0\",\"1\",\"0\",\"0\",\"0\"],\"-12\"]],[[[\"0\",\"0\",\"0\",\"0\",\"0\",\"2\"],\"884736\"],[[\"0\",\"0\",\"0\",\"3\",\"0\",\"0\"],\"-4096\"],[[\"0\",\"0\",\"1\",\"1\",\"1\",\"0\"],\"6144\"],[[\"0\",\"1\",\"0\",\"0\",\"2\",\"0\"],\"36864\"],[[\"0\",\"1\",\"0\",\"1\",\"0\",\"1\"],\"-73728\"],[[\"0\",\"2\",\"1\",\"0\",\"1\",\"0\"],\"1024\"],[[\"0\",\"3\",\"0\",\"0\",\"0\",\"1\"],\"-4096\"],[[\"1\",\"0\",\"0\",\"0\",\"1\",\"1\"],\"55296\"],[[\"1\",\"0\",\"1\",\"2\",\"0\",\"0\"],\"6144\"],[[\"1\",\"0\",\"2\",\"0\",\"1\",\"0\"],\"-3072\"],[[\"1\",\"1\",\"0\",\"1\",\"1\",\"0\"],\"-24576\"],[[\"1\",\"1\",\"1\",\"0\",\"0\",\"1\"],\"46080\"],[[\"2\",\"0\",\"0\",\"0\",\"2\",\"0\"],\"27648\"],[[\"2\",\"0\",\"0\",\"1\",\"0\",\"1\"],\"-221184\"],[[\"2\",\"0\",\"2\",\"1\",\"0\",\"0\"],\"-2304\"],[[\"2\",\"1\",\"1\",\"0\",\"1\",\"0\"],\"9216\"],[[\"2\",\"2\",\"0\",\"0\",\"0\",\"1\"],\"-55296\"],[[\"3\",\"0\",\"0\",\"1\",\"1\",\"0\"],\"1536\"],[[\"3\",\"0\",\"1\",\"0\",\"0\",\"1\"],\"69120\"],[[\"3\",\"0\",\"3\",\"0\",\"0\",\"0\"],\"256\"],[[\"3\",\"2\",\"0\",\"0\",\"1\",\"0\"],\"1024\"],[[\"4\",\"0\",\"0\",\"2\",\"0\",\"0\"],\"768\"],[[\"4\",\"0\",\"1\",\"0\",\"1\",\"0\"],\"-1152\"],[[\"4\",\"1\",\"0\",\"0\",\"0\",\"1\"],\"-13824\"],[[\"5\",\"0\",\"1\",\"1\",\"0\",\"0\"],\"-384\"],[[\"5\",\"1\",\"0\",\"0\",\"1\",\"0\"],\"768\"],[[\"6\",\"0\",\"0\",\"0\",\"0\",\"1\"],\"3456\"],[[\"6\",\"0\",\"2\",\"0\",\"0\",\"0\"],\"48\"],[[\"7\",\"0\",\"0\",\"0\",\"1\",\"0\"],\"-96\"]],[[[\"0\",\"0\",\"0\",\"2\",\"1\",\"0\"],\"12288\"],[[\"0\",\"0\",\"1\",\"0\",\"2\",\"0\"],\"9216\"],[[\"0\",\"1\",\"0\",\"0\",\"1\",\"1\"],\"-73728\"],[[\"0\",\"2\",\"0\",\"1\",\"1\",\"0\"],\"4096\"],[[\"1\",\"0\",\"0\",\"0\",\"0\",\"2\"],\"-1327104\"],[[\"1\",\"0\",\"0\",\"3\",\"0\",\"0\"],\"4096\"],[[\"1\",\"0\",\"1\",\"1\",\"1\",\"0\"],\"-18432\"],[[\"1\",\"1\",\"0\",\"0\",\"2\",\"0\"],\"-36864\"],[[\"1\",\"1\",\"0\",\"1\",\"0\",\"1\"],\"110592\"],[[\"1\",\"2\",\"1\",\"0\",\"1\",\"0\"],\"-2048\"],[[\"1\",\"3\",\"0\",\"0\",\"0\",\"1\"],\"8192\"],[[\"2\",\"0\",\"0\",\"0\",\"1\",\"1\"],\"110592\"],[[\"2\",\"0\",\"1\",\"2\",\"0\",\"0\"],\"-3072\"],[[\"2\",\"0\",\"2\",\"0\",\"1\",\"0\"],\"3840\"],[[\"2\",\"1\",\"0\",\"1\",\"1\",\"0\"],\"12288\"],[[\"2\",\"1\",\"1\",\"0\",\"0\",\"1\"],\"-36864\"],[[\"3\",\"0\",\"0\",\"0\",\"2\",\"0\"],\"-4608\"],[[\"3\",\"0\",\"0\",\"1\",\"0\",\"1\"],\"55296\"],[[\"3\",\"0\",\"2\",\"1\",\"0\",\"0\"],\"768\"],[[\"3\",\"1\",\"1\",\"0\",\"1\",\"0\"],\"-3072\"],[[\"3\",\"2\",\"0\",\"0\",\"0\",\"1\"],\"18432\"],[[\"4\",\"0\",\"0\",\"1\",\"1\",\"0\"],\"-3072\"],[[\"4\",\"0\",\"1\",\"0\",\"0\",\"1\"],\"-13824\"],[[\"4\",\"0\",\"3\",\"0\",\"0\",\"0\"],\"-64\"],[[\"4\",\"2\",\"0\",\"0\",\"1\",\"0\"],\"-256\"],[[\"5\",\"0\",\"1\",\"0\",\"1\",\"0\"],\"768\"],[[\"5\",\"1\",\"0\",\"0\",\"0\",\"1\"],\"-2304\"]],[[[\"0\",\"0\",\"0\",\"1\",\"2\",\"0\"],\"36864\"],[[\"0\",\"2\",\"0\",\"0\",\"2\",\"0\"],\"12288\"],[[\"1\",\"0\",\"0\",\"2\",\"1\",\"0\"],\"-24576\"],[[\"1\",\"1\",\"0\",\"0\",\"1\",\"1\"],\"-36864\"],[[\"1\",\"2\",\"0\",\"1\",\"1\",\"0\"],\"-4096\"],[[\"2\",\"0\",\"0\",\"0\",\"0\",\"2\"],\"663552\"],[[\"2\",\"0\",\"1\",\"1\",\"1\",\"0\"],\"12288\"],[[\"2\",\"1\",\"0\",\"1\",\"0\",\"1\"],\"-36864\"],[[\"2\",\"2\",\"1\",\"0\",\"1\",\"0\"],\"1024\"],[[\"2\",\"3\",\"0\",\"0\",\"0\",\"1\"],\"-4096\"],[[\"3\",\"0\",\"0\",\"0\",\"1\",\"1\"],\"-55296\"],[[\"3\",\"0\",\"2\",\"0\",\"1\",\"0\"],\"-1536\"],[[\"3\",\"1\",\"1\",\"0\",\"0\",\"1\"],\"9216\"],[[\"4\",\"0\",\"0\",\"0\",\"2\",\"0\"],\"2304\"]],[[[\"0\",\"0\",\"0\",\"0\",\"3\",\"0\"],\"-110592\"],[[\"1\",\"0\",\"0\",\"1\",\"2\",\"0\"],\"36864\"],[[\"2\",\"0\",\"1\",\"0\",\"2\",\"0\"],\"-9216\"],[[\"2\",\"1\",\"0\",\"0\",\"1\",\"1\"],\"36864\"],[[\"3\",\"0\",\"0\",\"0\",\"0\",\"2\"],\"-110592\"]]]")

def build(path):
    start=time.monotonic();stages=[]
    ctx=fmpz_mpoly_ctx.get(("S","Z","W","U","V","X"))
    es=list(ctx.gens());S,Z,W,U,V,X=es;zero=ctx.constant(0);one=ctx.constant(1)
    n=6;pairs=list(itertools.combinations(range(n),2));m=len(pairs)
    def ident(k):return [[one if i==j else zero for j in range(k)] for i in range(k)]
    def ma(A,B):return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
    def ms(A,c):return [[c*a for a in row] for row in A]
    def mm(A,B):
        assert len(A[0])==len(B)
        return [[sum((A[i][k]*B[k][j] for k in range(len(B))),zero) for j in range(len(B[0]))] for i in range(len(A))]
    def xd(a,b):
        q,r=divmod(a,b);assert not r,"nonexact polynomial division";return q
    def record(p):return [[[int(e) for e in ex],int(c)] for ex,c in sorted(p.to_dict().items())]
    def matrix_record(A):return [[record(p) for p in row] for row in A]
    def stats(A):return dict(rows=len(A),cols=len(A[0]),max_terms=max(len(p.to_dict()) for row in A for p in row),max_ordinary_degree=max((int(p.total_degree()) for row in A for p in row if p),default=-1))
    def mark(stage,**kw):
        r=dict(stage=stage,seconds=time.monotonic()-start,**kw);stages.append(r);print(json.dumps(r),flush=True)
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out=dict(schema="isp-six-site-full-s2-matrix-half-characteristic-v1",status="BUILDING_FULL_SOURCE",
      source_sha256=source_sha256,variables=["e1(z)","e2(z)","e3(z)","e4(z)","e5(z)","e6(z)"],
      weighted_degrees=[1,2,3,4,5,6],stages=stages,
      scope="New target: I_L-2 A*Gu A on the same actual five-dimensional L. Positivity requires all five real characteristic coefficients; no conclusion follows from partial data.")
    def save():
        out["elapsed_seconds"]=time.monotonic()-start
        tmp=path.with_suffix(".checkpoint.tmp");tmp.write_text(json.dumps(out,separators=(",",":"))+"\n");tmp.replace(path)
    def polynomial(rows):
        p=zero
        for powers,c in rows:
            term=ctx.constant(int(c))
            for x,e in zip(es,powers):
                if int(e):term*=x**int(e)
            p+=term
        return p
    def adjdet(A,tag):
        d=len(A);F=ident(d);adj=None;det=None
        for k in range(1,d+1):
            if k==d:adj=ms(F,(-1)**(d-1))
            AF=mm(A,F);ck=xd(-sum((AF[i][i] for i in range(d)),zero),ctx.constant(k))
            F=ma(AF,ms(ident(d),ck))
            if k==d:det=((-1)**d)*ck
        assert det and all(not p for row in F for p in row),"complete low inverse"
        return adj,det
    def upper_from_saved(A):
        # Original complete 15th-order characteristic already returned in run
        # 46052984288. This is its adjugate Horner formula, not a repeated gate.
        assert len(A)==15 and len(UPPER_CHAR)==15
        F=ident(15)
        for rows in UPPER_CHAR[:14]:
            F=ma(mm(A,F),ms(ident(15),polynomial(rows)))
        det=-polynomial(UPPER_CHAR[14])
        out["saved_upper_parameter_blob"]="2237cf832bbc9d14d73553bd43f657df5f3dc66d"
        out["saved_upper_run_id"]=46052984288
        return F,det

    I=ident(n);T=[[zero for _ in range(n)] for _ in range(n)]
    for j in range(n-1):T[j+1][j]=one
    for i in range(n):T[i][n-1]=((-1)**(n-i+1))*es[n-i-1]
    moments=[ctx.constant(n)]
    for k in range(1,n+1):
        moments.append(sum((((-1)**(i-1))*es[i-1]*moments[k-i] for i in range(1,k)),zero)+((-1)**(k-1))*k*es[k-1])
    Q=[[zero for _ in range(n)] for _ in range(n)];Q[0]=moments[1:]
    vp=[[one if i==0 else zero for i in range(n)]]
    for k in range(1,2*n+1):vp.append([sum((T[i][j]*vp[k-1][j] for j in range(n)),zero) for i in range(n)])
    basis=[[one if i==j else zero for i in range(n)] for j in range(n)]
    def wedge(a,b):return [a[i]*b[j]-a[j]*b[i] for i,j in pairs]
    Usum=[[zero for _ in range(m)] for _ in range(m)]
    for k,(a,b) in enumerate(pairs):
        Ta=[T[i][a] for i in range(n)];Tb=[T[i][b] for i in range(n)]
        q=wedge(Ta,basis[b]);r=wedge(basis[a],Tb)
        for i in range(m):Usum[i][k]=q[i]+r[i]
    R=[[zero for _ in range(m)] for _ in range(n)]
    for k,(a,b) in enumerate(pairs):
        for r in range(b-a):
            for i in range(n):R[i][k]+=moments[b-r]*vp[a+r][i]
        for i in range(n):R[i][k]-=(b-a)*vp[a+b][i]
    Rs=[[zero for _ in range(n)] for _ in range(m)]
    for k in range(n):
        a=wedge(basis[0],vp[k+1]);b=wedge(basis[1],vp[k])
        for i in range(m):Rs[i][k]=a[i]-b[i]
    C=ma(mm(R,Usum),ms(mm(T,R),-1))
    Cs=ma(mm(Usum,Rs),ms(mm(Rs,T),-1))
    T2=mm(T,T);T3=mm(T2,T)
    F1=ma(ma(ms(I,S),ms(T,-2)),Q)
    F2=ma(ma(ma(ma(ma(ms(I,Z),ms(T,-2*S)),ms(T2,3)),ms(Q,S)),ms(mm(T,Q),-1)),ms(mm(Q,T),-1))
    F3=ma(ma(ma(ma(ms(I,W),ms(T,-2*Z)),ms(T2,3*S)),ms(T3,-4)),ms(Q,Z))
    F3=ma(F3,ms(ma(mm(T,Q),mm(Q,T)),-S))
    F3=ma(ma(ma(F3,mm(T2,Q)),mm(mm(T,Q),T)),mm(Q,T2))
    P3=ma(ma(ma(ms(I,W),ms(T,-Z)),ms(T2,S)),ms(T3,-1))
    FU=ma(ma(ms(ident(m),S),ms(Usum,-2)),mm(Rs,R))
    assert mm(R,Rs)==F1,"same complete low first Gram"
    assert mm(mm(R,FU),Rs)==ms(F2,4),"same complete low second Gram"
    out["pair_basis"]=[list(p) for p in pairs]
    mark("same_pair_source_and_physical_adjoints",R=stats(R),Rs=stats(Rs),FU=stats(FU))
    adj1,det1=adjdet(F1,"F1");adj2,det2=adjdet(F2,"F2")
    mark("complete_low_inverses",F1_det_terms=len(det1.to_dict()),F2_det_terms=len(det2.to_dict()))
    adjU,detU=upper_from_saved(FU)
    out.pop("upper_inverse_continuation",None)
    out["complete_upper_inverse_determinant"]=record(detU);save()
    mark("same_upper_inverse_from_saved_characteristic",dimension=m,determinant_terms=len(detU.to_dict()),adjugate=stats(adjU))

    delta=xd(det1,ctx.constant(4));epsilon=xd(det2,ctx.constant(9));theta=xd(detU,ctx.constant(9216))
    factors=[ctx.constant(2),ctx.constant(3),S,U,delta,epsilon,theta]
    names=["2","3","S","e4","delta6","epsilon6","theta6"];count=len(factors)
    def exp(**kw):
        a=[0]*count
        for k,v in kw.items():a[names.index(k)]=v
        return a
    def factor_product(powers):
        p=one
        for f,e in zip(factors,powers):
            if e:p*=f**e
        return p
    class FM:
        def __init__(self,A,powers=None):
            self.A=[row[:] for row in A];self.p=[0]*count if powers is None else list(powers);self.cancel()
        def cancel(self):
            if not any(x for row in self.A for x in row):self.p=[0]*count;return
            for j,f in enumerate(factors):
                while self.p[j]:
                    qs=[];ok=True
                    for row in self.A:
                        qr=[]
                        for x in row:
                            q,r=divmod(x,f)
                            if r:ok=False;break
                            qr.append(q)
                        if not ok:break
                        qs.append(qr)
                    if not ok:break
                    self.A=qs;self.p[j]-=1
        def __matmul__(self,o):return FM(mm(self.A,o.A),[a+b for a,b in zip(self.p,o.p)])
        def __add__(self,o):
            p=[max(a,b) for a,b in zip(self.p,o.p)]
            a=factor_product([x-y for x,y in zip(p,self.p)]);b=factor_product([x-y for x,y in zip(p,o.p)])
            return FM(ma(ms(self.A,a),ms(o.A,b)),p)
        def __neg__(self):return FM(ms(self.A,-1),self.p)
        def __sub__(self,o):return self+(-o)
        def summary(self):return dict(denominator_factors={n:e for n,e in zip(names,self.p) if e},**stats(self.A))
        def denominator(self):return factor_product(self.p)
    def divide_power(A,name,k):
        p=A.p[:];p[names.index(name)]+=k;return FM(A.A,p)
    Pi=FM(I)-FM(Q,exp(S=1))
    F1i=FM(adj1,exp(**{"2":2,"delta6":1}))
    F2i=FM(adj2,exp(**{"3":2,"epsilon6":1}))
    FUi=FM(adjU,exp(**{"2":10,"3":2,"theta6":1}))
    L2=Pi@F2i@Pi
    E=FM(F3)-FM(mm(mm(P3,Q),P3),exp(e4=1))
    Xlow=L2@E@L2
    H=mm(C,Rs);Hs=mm(R,Cs)
    Kbb=Pi@(FM(mm(C,Cs))-FM(H)@F1i@FM(Hs))@Pi
    Xc=mm(mm(C,FU),Rs);Xcs=mm(mm(R,FU),Cs)
    Kbc=Pi@(FM(mm(mm(C,FU),Cs))-divide_power(FM(Xc)@F2i@FM(Xcs),"2",2))@Pi
    Usource=FM(Cs)-FM(Rs)@F1i@FM(Hs)
    Ustarsource=FM(C)-FM(H)@F1i@FM(R)
    Kbg=Pi@Ustarsource@FUi@Usource@Pi
    mark("same_full_source_three_cost_blocks",Kbb=Kbb.summary(),Kbc=Kbc.summary(),Kbg=Kbg.summary())
    # Exact expansion of (1/2)(Cu B*L2+B*Xlow), with both mixed terms.
    cost=divide_power(L2@Kbc@L2+L2@Kbb@Xlow+Xlow@Kbb@L2+Xlow@Kbg@Xlow,"2",2)
    mark("same_complete_six_site_s2_cost",cost=cost.summary())
    assert all(not cost.A[i][0] for i in range(n)),"actual low vacuum zero column"
    den=cost.denominator()
    # The full cost preserves the actual L and annihilates its orthogonal
    # vacuum. Its quotient by that line is similar to its physical restriction.
    J=ma(ms(ident(5),den),ms([row[1:] for row in cost.A[1:]],-2))
    pnames=["S","Z","W","U","V","X","delta6","epsilon6","theta6"]
    pfactors=es+[delta,epsilon,theta]
    pweights=[1,2,3,4,5,6,6,12,15]
    equal_es=[6,15,20,15,6,1]
    def evaluate_equal(p):
        return sum(int(c)*math.prod(a**int(e) for a,e in zip(equal_es,powers)) for powers,c in p.to_dict().items())
    pvalues=[evaluate_equal(p) for p in pfactors]
    assert pvalues==[6,15,20,15,6,1,2560,25920,5184]
    assert all(math.gcd(*(abs(int(c)) for c in p.to_dict().values()))==1 for p in pfactors),"primitive continuing factors"
    def factor_value(powers):return math.prod(a**e for a,e in zip(pvalues,powers))
    def pull(A,extract_integer=True):
        if not any(p for row in A for p in row):return A,1,[0]*len(pfactors)
        B=[row[:] for row in A];powers=[0]*len(pfactors)
        for j,f in enumerate(pfactors):
            while True:
                result=[];ok=True
                for row in B:
                    qr=[]
                    for p in row:
                        q,r=divmod(p,f)
                        if r:ok=False;break
                        qr.append(q)
                    if not ok:break
                    result.append(qr)
                if not ok:break
                B=result;powers[j]+=1
        content=1
        if extract_integer:
            content=0
            for row in B:
                for p in row:
                    for c in p.to_dict().values():content=math.gcd(content,abs(int(c)))
            assert content>0
            if content>1:B=[[xd(p,ctx.constant(content)) for p in row] for row in B]
        return B,content,powers
    def pack(value):
        raw=json.dumps(value,separators=(",",":")).encode()
        return dict(encoding="base64+zlib+json",uncompressed_bytes=len(raw),
                    sha256=hashlib.sha256(raw).hexdigest(),
                    data=base64.b64encode(zlib.compress(raw,6)).decode())
    def degree(p):
        degrees={sum((i+1)*int(e) for i,e in enumerate(ex)) for ex in p.to_dict()}
        assert len(degrees)==1,"nonhomogeneous scalar";return degrees.pop()
    A,initial_content,initial_powers=pull(J)
    Adegree=degree(den)-sum(w*e for w,e in zip(pweights,initial_powers))
    qvalue=initial_content*factor_value(initial_powers)
    denvalue=evaluate_equal(den);assert denvalue%qvalue==0
    avalue=denvalue//qvalue
    # At colliding roots the companion evaluation basis degenerates.
    # Only characteristic coefficients, not this matrix itself, specialize
    # to those of avalue*I; their values are checked below.
    out.update(status="EXACT_NEW_MATRIX_READY",
        target="I_L-2K>0, K=A_source*Gu A_source on the SAME actual five-dimensional L",
        positive_denominator_factors={name:record(f) for name,f in zip(names,factors)},
        cost_denominator_factors={name:e for name,e in zip(names,cost.p) if e},
        positive_characteristic_factors={name:record(f) for name,f in zip(pnames,pfactors)},
        starting_matrix_relation="den(cost)*(I5-2K_quotient)=initial_positive_scalar*starting_matrix",
        initial_positive_integer_content=initial_content,
        initial_positive_factor_powers={name:e for name,e in zip(pnames,initial_powers) if e},
        starting_matrix_weighted_degree=Adegree,
        starting_matrix=pack(matrix_record(A)),
        characteristic="det(t I5+starting_matrix)=t^5+c1 t^4+c2 t^3+c3 t^2+c4 t+c5",
        complete_coefficients=[],
        same_source_complete_upper_inverse_and_both_cross_terms=True)
    F=ident(5);scale_powers=[0]*len(pfactors)
    out["continuation"]=dict(order=0,positive_factor_powers=scale_powers[:],matrix=pack(matrix_record(F)))
    save();mark("new_actual_matrix_half_source_ready",matrix=stats(A),weighted_degree=Adegree,
                initial_positive_integer_content=initial_content,
                initial_positive_factor_powers=out["initial_positive_factor_powers"],
                starting_matrix_bytes=out["starting_matrix"]["uncompressed_bytes"],checkpoint_bytes=path.stat().st_size)
    del J,cost,Kbb,Kbc,Kbg,L2,E,Xlow,FUi,F1i,F2i,Usource,Ustarsource,adjU,FU,adj1,adj2,R,Rs,C,Cs
    for k in range(1,6):
        AF=mm(A,F)
        chat=xd(-sum((AF[i][i] for i in range(5)),zero),ctx.constant(k))
        ebase=((-1)**k)*chat
        expected_degree=k*Adegree-sum(w*e for w,e in zip(pweights,scale_powers))
        assert degree(ebase)==expected_degree
        assert factor_value(scale_powers)*evaluate_equal(ebase)==math.comb(5,k)*avalue**k
        reduced,content,powers=pull([[ebase]])
        rp=reduced[0][0];totalpowers=[a+b for a,b in zip(scale_powers,powers)]
        terms=record(rp);canon=json.dumps(terms,separators=(",",":")).encode()
        coefficient=dict(index=k,original_weighted_degree=k*Adegree,
            positive_integer_content=content,
            positive_factor_powers={name:e for name,e in zip(pnames,totalpowers) if e},
            reduced_weighted_degree=degree(rp),reduced_terms=len(terms),
            negative_terms=sum(int(c)<0 for _,c in terms),
            reduced_sha256=hashlib.sha256(canon).hexdigest(),
            complete_reduced_elementary_coefficients=pack(terms))
        out["complete_coefficients"].append(coefficient)
        Ftemp=ma(AF,ms(ident(5),chat))
        out["status"]="EXACT_CHARACTERISTIC_PARTIAL"
        out["continuation"]=dict(order=k,positive_factor_powers=scale_powers[:],matrix=pack(matrix_record(Ftemp)))
        save();mark("new_matrix_half_characteristic_coefficient",
            **{a:b for a,b in coefficient.items() if a!="complete_reduced_elementary_coefficients"},
            checkpoint_bytes=path.stat().st_size)
        if k<5:
            # Only primitive polynomial factors can leave a continuing
            # Faddeev matrix. Never divide out arbitrary integer content here.
            F,mcontent,mpowers=pull(Ftemp,extract_integer=False)
            assert mcontent==1
            scale_powers=[a+b for a,b in zip(scale_powers,mpowers)]
            if any(mpowers):
                out["continuation"]=dict(order=k,positive_factor_powers=scale_powers[:],matrix=pack(matrix_record(F)))
                save()
            mark("same_characteristic_primitive_reduction",index=k,
                 positive_factor_powers={name:e for name,e in zip(pnames,scale_powers) if e},matrix=stats(F))
        else:
            assert all(not p for row in Ftemp for p in row),"complete new Cayley-Hamilton return"
    out["cayley_hamilton_return"]=True
    passed=all(r["negative_terms"]==0 for r in out["complete_coefficients"])
    out["status"]="CERTIFIED_ELEMENTARY" if passed else "EXACT_CHARACTERISTIC_READY"
    out["all_five_reduced_coefficients_elementary_nonnegative"]=passed
    out.pop("continuation",None);save();return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path,default=Path(__file__).with_suffix(".json"))
    ap.add_argument("--full-orbits",action="store_true",help="Compatibility; complete new coefficients are always retained.")
    args=ap.parse_args();out=build(args.output)
    omitted={"starting_matrix","positive_denominator_factors","positive_characteristic_factors",
             "complete_upper_inverse_determinant","complete_coefficients","continuation"}
    report={k:v for k,v in out.items() if k not in omitted}
    report["complete_coefficients"]=[{k:v for k,v in r.items() if k!="complete_reduced_elementary_coefficients"} for r in out["complete_coefficients"]]
    print(json.dumps(report,indent=2),flush=True)
if __name__=="__main__":
    main()
    signal.alarm(0)
