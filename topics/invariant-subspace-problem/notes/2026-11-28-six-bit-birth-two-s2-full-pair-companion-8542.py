#!/usr/bin/env python3
"""NEW whole six-site birth-two S2 source.

Pair-Schur coordinates represent the entire 15-dimensional H2.
The complete FU=d3 d3* inverse precedes the 9-dimensional K2 compression.
Physical R*, C* are constructed separately, never ordinary transposes.
Both mixed blocks in A*Gu A are kept. The full cost is checkpointed
before its square trace. A quarter-square certificate plus the proved
same six-site birth-one half first edge is sufficient for S2 only.
"""
from __future__ import annotations
import resource, signal
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
import argparse, hashlib, itertools, json, math, time
from pathlib import Path
from flint import fmpz_mpoly_ctx

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
    out=dict(schema="isp-six-site-full-birth-two-s2-pair-companion-v1",status="BUILDING_FULL_SOURCE",
      source_sha256=source_sha256,variables=["e1(z)","e2(z)","e3(z)","e4(z)","e5(z)","e6(z)"],
      weighted_degrees=[1,2,3,4,5,6],stages=stages,
      scope="Only the exact same full six-site birth-two S2 cost. No upper S1, seven-site first edge, infinite source or ordinary ISP claim.")
    def save():
        out["elapsed_seconds"]=time.monotonic()-start
        tmp=path.with_suffix(".checkpoint.tmp");tmp.write_text(json.dumps(out,separators=(",",":"))+"\n");tmp.replace(path)
    def adjdet(A,tag):
        d=len(A);F=ident(d);adj=None;det=None
        if tag=="FU":out["complete_upper_characteristic_coefficients"]=[]
        for k in range(1,d+1):
            if k==d:adj=ms(F,(-1)**(d-1))
            AF=mm(A,F);ck=xd(-sum((AF[i][i] for i in range(d)),zero),ctx.constant(k))
            F=ma(AF,ms(ident(d),ck))
            if k==d:det=((-1)**d)*ck
            if tag=="FU":
                out["complete_upper_characteristic_coefficients"].append(dict(index=k,coefficient=record(ck)))
                out["status"]="FULL_UPPER_INVERSE_PARTIAL"
                out["upper_inverse_continuation"]=dict(order=k,F=matrix_record(F),last_coefficient=record(ck))
                save();mark("complete_upper_faddeev_order",index=k,coefficient_terms=len(ck.to_dict()),matrix=stats(F),checkpoint_bytes=path.stat().st_size)
        assert det and all(not p for row in F for p in row),"Cayley-Hamilton inverse return"
        chk=mm(A,adj)
        assert all(chk[i][j]==(det if i==j else zero) for i in range(d) for j in range(d)),"actual complete inverse"
        return adj,det

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
    out["complete_upper_Gram"]=matrix_record(FU)
    save();mark("full_pair_source_and_physical_adjoints",R=stats(R),Rs=stats(Rs),FU=stats(FU))
    adj1,det1=adjdet(F1,"F1");adj2,det2=adjdet(F2,"F2")
    mark("complete_low_inverses",F1_det_terms=len(det1.to_dict()),F2_det_terms=len(det2.to_dict()))
    adjU,detU=adjdet(FU,"FU")
    out.pop("upper_inverse_continuation",None)
    out["complete_upper_inverse_determinant"]=record(detU);save()
    mark("complete_full_upper_inverse",dimension=m,determinant_terms=len(detU.to_dict()),adjugate=stats(adjU))

    factors=[ctx.constant(2),ctx.constant(3),S,U,det1,det2,detU]
    names=["2","3","S","e4","detF1","detF2","detFU"];count=len(factors)
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
    F1i=FM(adj1,exp(detF1=1));F2i=FM(adj2,exp(detF2=1));FUi=FM(adjU,exp(detFU=1))
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
    out["status"]="EXACT_COST_READY"
    out["positive_denominator_factors"]={n:record(f) for n,f in zip(names,factors)}
    out["cost_denominator_factors"]={n:e for n,e in zip(names,cost.p) if e}
    out["complete_cost_numerator_matrix"]=matrix_record(cost.A)
    save();mark("actual_full_cost_checkpoint_written",bytes=path.stat().st_size)
    trN=sum((cost.A[i][j]*cost.A[j][i] for i in range(n) for j in range(n)),zero)
    scalar=FM([[trN]],[2*e for e in cost.p])
    numerator=scalar.A[0][0];denominator=scalar.denominator();gap=denominator-4*numerator
    def pstats(p):
        data=record(p);degs=sorted({sum((i+1)*e for i,e in enumerate(ex)) for ex,c in data})
        return dict(terms=len(data),weighted_degrees=degs,negative_terms=sum(c<0 for ex,c in data),sha256=hashlib.sha256(json.dumps(data,separators=(",",":")).encode()).hexdigest())
    ds=[p.to_dict() for p in (numerator,denominator,gap)]
    powers=sorted(set().union(*(set(d) for d in ds)),reverse=True)
    records=[dict(powers=[int(e) for e in p],coefficients=[int(d.get(p,0)) for d in ds]) for p in powers]
    passed=bool(gap) and all(c>=0 for c in ds[2].values())
    out.update(status="CERTIFIED_ELEMENTARY" if passed else "EXACT_SCALAR_READY",
      scalar_identity="Tr_L((A*Gu A)^2)=N/D on the actual five-dimensional L",
      scalar_denominator_factors={n:e for n,e in zip(names,scalar.p) if e},
      N=pstats(numerator),D=pstats(denominator),gap=pstats(gap),
      complete_elementary_coefficients=records,
      same_source_complete_upper_inverse_and_both_cross_terms=True,
      all_elementary_gap_coefficients_nonnegative=passed)
    out.pop("complete_upper_Gram",None);out.pop("complete_cost_numerator_matrix",None)
    save();mark("same_complete_s2_scalar",N=out["N"],D=out["D"],gap=out["gap"],bytes=path.stat().st_size)
    save();return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path,default=Path(__file__).with_suffix(".json"))
    ap.add_argument("--full-orbits",action="store_true",help="Compatibility; complete exact coefficients are always retained.")
    a=ap.parse_args();out=build(a.output)
    omitted={"complete_elementary_coefficients","positive_denominator_factors","complete_upper_inverse_determinant","complete_upper_Gram","complete_cost_numerator_matrix","upper_inverse_continuation","complete_upper_characteristic_coefficients"}
    print(json.dumps({k:v for k,v in out.items() if k not in omitted},indent=2),flush=True)
if __name__=="__main__":
    main()
    signal.alarm(0)
