#!/usr/bin/env python3
"""New cyclic-moment companion input for the SAME complete five-site S2.

All matrix operations now use the five elementary symmetric variables.
Multiplication by a root is the quintic companion matrix T; Q=e0*moments.
This is an exact similarity on distinct positive roots, extended only at
the FINAL rational scalar by continuity.  Every physical adjoint is
constructed separately; no Euclidean transpose of companion matrices.

The four short blocks share ONE complete F2 inverse and retain both
cross terms.  The actual cost coefficients are atomically checkpointed
before Tr(cost^2), so a later resource stop retains the exact same input.
Target: Tr(cost^2)<=1/4 plus the proved SAME four-dimensional low-source
half-budget.  EXACT_COST_READY / EXACT_SCALAR_READY are not certificates.
"""
from __future__ import annotations
import resource, signal
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
import argparse, hashlib, itertools, json, time
from pathlib import Path
from flint import fmpz_mpoly_ctx

def build(full_orbits=False,checkpoint_path=None):
    start=time.monotonic(); stages=[]
    ctx=fmpz_mpoly_ctx.get(("S","Z","W","U","V"))
    S,Z,W,U,V=ctx.gens(); zero=ctx.constant(0); one=ctx.constant(1)
    def mark(name,**kw):
        row=dict(stage=name,seconds=time.monotonic()-start,**kw);stages.append(row)
        print(json.dumps(row),flush=True)
    def prod(xs):
        p=one
        for x in xs:p*=x
        return p
    def es(xs,k):return sum((prod(v) for v in itertools.combinations(xs,k)),zero)
    def xd(a,b):
        q,r=divmod(a,b);assert not r,"nonexact polynomial division";return q
    def mm(A,B):
        assert len(A[0])==len(B)
        return [[sum((A[i][k]*B[k][j] for k in range(len(B))),zero)
                 for j in range(len(B[0]))] for i in range(len(A))]
    def ident(n):return [[one if i==j else zero for j in range(n)] for i in range(n)]
    def adjdet(A):
        n=len(A);F=[row[:] for row in A];B=ident(n);previous=one
        for k in range(n):
            pivot=F[k][k];assert pivot
            oldF=[row[:] for row in F];oldB=[row[:] for row in B]
            for i in range(n):
                if i==k:continue
                for j in range(n):
                    if j!=k:F[i][j]=xd(pivot*oldF[i][j]-oldF[i][k]*oldF[k][j],previous)
                    B[i][j]=xd(pivot*oldB[i][j]-oldF[i][k]*oldB[k][j],previous)
                F[i][k]=zero
            previous=pivot
        det=F[0][0];AB=mm(A,B)
        assert all(F[i][j]==(det if i==j else zero) and AB[i][j]==(det if i==j else zero)
                   for i in range(n) for j in range(n))
        return B,det

    delta=S*S*W-4*S*U+12*V
    epsilon=U*U*Z-4*S*U*V+12*V*V
    factors=[ctx.constant(2),ctx.constant(3),S,U,V,delta,epsilon]
    names=["2","3","S","e4","pi","delta","epsilon"];count=len(factors)
    def exp(**kw):
        a=[0]*count
        for n,v in kw.items():a[names.index(n)]=v
        return a
    def multiply_factors(ds):return prod(f**n for f,n in zip(factors,ds) if n)
    class FM:
        def __init__(self,A,powers=None,reduce=True):
            self.A=[row[:] for row in A];self.p=[0]*count if powers is None else list(powers)
            if reduce:self.cancel()
        def cancel(self):
            # Only exact whole-factor division. No assumptions about missing
            # irreducible factors are needed for correctness.
            if not any(x for row in self.A for x in row):
                self.p=[0]*count;return
            for k,f in enumerate(factors):
                while self.p[k]:
                    quot=[];ok=True
                    for row in self.A:
                        qrow=[]
                        for x in row:
                            q,r=divmod(x,f)
                            if r:ok=False;break
                            qrow.append(q)
                        if not ok:break
                        quot.append(qrow)
                    if not ok:break
                    self.A=quot;self.p[k]-=1
        def __add__(self,o):
            pp=[max(a,b) for a,b in zip(self.p,o.p)]
            a=multiply_factors([v-w for v,w in zip(pp,self.p)])
            b=multiply_factors([v-w for v,w in zip(pp,o.p)])
            return FM([[a*self.A[i][j]+b*o.A[i][j] for j in range(len(self.A[0]))]
                       for i in range(len(self.A))],pp)
        def __neg__(self):return FM([[-x for x in row] for row in self.A],self.p,False)
        def __sub__(self,o):return self+(-o)
        def __matmul__(self,o):return FM(mm(self.A,o.A),[a+b for a,b in zip(self.p,o.p)])
        def denominator(self):return multiply_factors(self.p)
        def summary(self):
            return dict(den_factors={n:p for n,p in zip(names,self.p) if p},
              max_num_degree=max((int(x.total_degree()) for row in self.A for x in row if x),default=-1),
              max_num_terms=max(len(x.to_dict()) for row in self.A for x in row))
        def equals(self,o):
            pp=[max(a,b) for a,b in zip(self.p,o.p)]
            a=multiply_factors([v-w for v,w in zip(pp,self.p)])
            b=multiply_factors([v-w for v,w in zip(pp,o.p)])
            return all(a*self.A[i][j]==b*o.A[i][j] for i in range(len(self.A)) for j in range(len(self.A[0])))

    def scalar(p):return FM([[p if i==j else zero for j in range(5)] for i in range(5)])
    def times(A,p):return FM([[p*x for x in row] for row in A.A],A.p)
    I=scalar(one)
    t=ident(5)
    t=[[zero]*5 for _ in range(5)]
    for j in range(4):t[j+1][j]=one
    for i,v in enumerate([V,-U,W,-Z,S]):t[i][4]=v
    T=FM(t);T2=T@T;T3=T2@T;T4=T3@T
    m2=S*S-2*Z;m3=S**3-3*S*Z+3*W
    m4=S**4-4*S*S*Z+2*Z*Z+4*S*W-4*U
    m5=S**5-5*S**3*Z+5*S*Z*Z+5*S*S*W-5*Z*W-5*S*U+5*V
    q=[[zero]*5 for _ in range(5)];q[0]=[S,m2,m3,m4,m5];Q=FM(q)
    P=I-FM(Q.A,exp(S=1))
    F1=scalar(S)-times(T,ctx.constant(2))+Q
    F2=scalar(Z)-times(T,2*S)+times(T2,ctx.constant(3))+times(Q,S)-T@Q-Q@T
    adj1,det1=adjdet(F1.A);assert det1==4*delta
    p1=exp(delta=1);p1[0]=2;F1i=FM(adj1,p1)
    adj2,det2=adjdet(F2.A);assert det2==9*epsilon
    p2=exp(epsilon=1);p2[1]=2;F2i=FM(adj2,p2)
    L1=P@F1i@P;L2=P@F2i@P
    F3=scalar(W)-times(T,2*Z)+times(T2,3*S)-times(T3,ctx.constant(4))+times(Q,Z)-times(T@Q+Q@T,S)+T2@Q+T@Q@T+Q@T2
    ep=exp(e4=1);ep[0]=4
    E=F3-FM(mm(mm(F3.A,Q.A),F3.A),ep)
    Tinv=FM((T4-times(T3,S)+times(T2,Z)-times(T,W)+scalar(U)).A,exp(pi=1))
    assert (T@Tinv).equals(I)
    mark("companion_complete_primitive_grams",L1=L1.summary(),L2=L2.summary(),E=E.summary())
    H=scalar(m2)-times(T2,ctx.constant(2))+Q@T
    Hs=scalar(m2)-times(T2,ctx.constant(2))+T@Q
    Ce=scalar(S)-times(T,ctx.constant(2))+Tinv@Q@T
    Ces=scalar(S)-times(T,ctx.constant(2))+T@Q@Tinv
    DX=scalar(S*m2-m3)-times(T,2*m2)-times(T2,2*S)+times(T3,ctx.constant(6))
    X=DX+times(Q,m2)+times(Q@T,S)-T@Q@T-T2@Q-times(Q@T2,ctx.constant(2))
    Xs=DX+times(Q,m2)+times(T@Q,S)-T@Q@T-Q@T2-times(T2@Q,ctx.constant(2))
    DCD=scalar(S*m3+m2*m2-2*m4)-times(T,2*m3)-times(T2,4*m2)-times(T3,2*S)+times(T4,ctx.constant(12))
    FCD=DCD+times(Q,m3)+times(T@Q+Q@T,m2)+times(T@Q@T,S)-times(T3@Q+Q@T3+T2@Q@T+T@Q@T2,ctx.constant(2))
    Y=times(F1,ctx.constant(2))+Tinv@Q@(scalar(S)-T)
    Ys=times(F1,ctx.constant(2))+(scalar(S)-T)@Q@Tinv
    E1=FM(scalar(U).A,exp(pi=1))-times(Tinv,ctx.constant(2))+Tinv@Q@Tinv
    Ke0=E1@F1+scalar(ctx.constant(3))+Q@Tinv
    Kcc=P@(FCD-X@F2i@Xs)@P
    Kce=P@(Ce@F1+H-X@F2i@Y)@P
    Kec=P@(F1@Ces+Hs-Ys@F2i@Xs)@P
    Kee=P@(Ke0-Ys@F2i@Y)@P
    mark("same_short_four_blocks",Kcc=Kcc.summary(),Kce=Kce.summary(),Kee=Kee.summary())
    R=L1@E;Rs=E@L1
    inner=Kcc+Kce@R+Rs@Kec+Rs@Kee@R
    mark("common_source_inner_square",inner=inner.summary())
    cost=L2@inner@L2
    mark("same_actual_cost_in_companion_coordinates",cost=cost.summary())
    if checkpoint_path is not None:
        checkpoint=dict(status="EXACT_COST_READY",
          source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          variables=["e1(z)","e2(z)","e3(z)","e4(z)","e5(z)"],
          weighted_degrees=[1,2,3,4,5],
          identity="same complete-source cost=A*Gu A",
          denominator_factors=cost.summary()["den_factors"],
          numerator_matrix=[[[[[int(e) for e in p],int(c)] for p,c in sorted(x.to_dict().items())]
                            for x in row] for row in cost.A],
          scope="Complete original cost computed; no cost-square or positivity conclusion yet.",
          stages=stages,elapsed_seconds=time.monotonic()-start)
        temporary=checkpoint_path.with_suffix(".cost-checkpoint.tmp")
        temporary.write_text(json.dumps(checkpoint,separators=(",",":"))+"\n")
        temporary.replace(checkpoint_path)
        mark("exact_cost_checkpoint_written",bytes=checkpoint_path.stat().st_size)
    trN=sum((cost.A[i][j]*cost.A[j][i] for i in range(5) for j in range(5)),zero)
    scalar_trace=FM([[trN]],[2*n for n in cost.p])
    N=scalar_trace.A[0][0];D=scalar_trace.denominator()
    gap=D-4*N;sharp=3*D-16*N
    def stats(poly):
        d=poly.to_dict();canon=[[[int(e) for e in p],int(c)] for p,c in sorted(d.items())]
        degrees=sorted({sum(w*int(a) for w,a in zip([1,2,3,4,5],p)) for p in d})
        return dict(terms=len(d),ordinary_degree=int(poly.total_degree()),weighted_degrees=degrees,negative=sum(c<0 for c in d.values()),
          sha256=hashlib.sha256(json.dumps(canon,separators=(",",":")).encode()).hexdigest())
    mark("exact_scalar_in_elementary_variables",N=stats(N),D=stats(D),gap=stats(gap))
    ds=[p.to_dict() for p in [N,D,gap,sharp]]
    powers=sorted(set().union(*(set(d) for d in ds)),reverse=True)
    records=[dict(powers=[int(e) for e in p],coefficients=[int(d.get(p,0)) for d in ds]) for p in powers]
    passed=bool(gap) and all(c>=0 for c in ds[2].values())
    sharper=bool(sharp) and all(c>=0 for c in ds[3].values())
    return dict(status="CERTIFIED" if passed else "EXACT_SCALAR_READY",
      statement="same complete five-site S2 Ward cost-square",
      identity="Tr((A*Gu A)^2)=N/D",
      variables=["e1(z)","e2(z)","e3(z)","e4(z)","e5(z)"],
      weighted_degrees=[1,2,3,4,5],
      same_source_and_complete_projection=True,
      companion_similarity="evaluation is invertible on five distinct z_i; exact rational identity extends to all positive z by continuity",
      physical_adjoint="separately constructed formulas, never ordinary transpose of companion matrices",
      denominator_positive_on_actual_positive_weights=True,
      denominator_factors=scalar_trace.summary()["den_factors"],
      elementary_one_quarter_coefficient_certificate=passed,
      elementary_three_sixteenths_coefficient_certificate=sharper,
      N=stats(N),D=stats(D),gap=stats(gap),three_sixteenths_gap=stats(sharp),
      complete_elementary_coefficients=records,
      scope="If EXACT_SCALAR_READY, no positive-weight S2 conclusion until a further exact scalar positivity proof.",
      elapsed_seconds=time.monotonic()-start,stages=stages)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path,default=Path(__file__).with_suffix(".json"))
    p.add_argument("--full-orbits",action="store_true",help="compatibility flag; full elementary coefficients are always retained")
    a=p.parse_args();out=build(a.full_orbits,a.output)
    out["source_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    temporary=a.output.with_suffix(".final.tmp")
    temporary.write_text(json.dumps(out,indent=2)+"\n")
    temporary.replace(a.output)
    print(json.dumps({k:v for k,v in out.items() if k!="complete_elementary_coefficients"},indent=2),flush=True)
if __name__=="__main__":
    main()
    signal.alarm(0)
