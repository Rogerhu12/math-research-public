#!/usr/bin/env python3
"""New factored, one-projection input for the complete five-site S2.

Uses the hard-end Ward identity to form ONE common physical source V:
  A=Cu(B*+E_d* L1 L3^-1)L2,
  V=d3*(C*+e L1 L3^-1)L2,
  A*Gu A=V*(I-R2* F2^-1 R2)V.
All cross terms remain inside V.  Known denominator factors are cancelled
by exact division, never a large general multivariate gcd.
The new target is Tr((A*Gu A)^2)<1/4, using the proved SAME low-source
half-bound I-L1 L2^-1 L1>I/2.  No numeric evidence enters the certificate.
"""
from __future__ import annotations
import resource, signal
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
import argparse, hashlib, itertools, json, time
from pathlib import Path
from flint import fmpz_mpoly_ctx

def build(full_orbits=False):
    start=time.monotonic(); stages=[]
    ctx=fmpz_mpoly_ctx.get(tuple("z"+str(i+1) for i in range(5)))
    z=ctx.gens(); zero=ctx.constant(0); one=ctx.constant(1)
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
    S=sum(z,zero);e2=es(z,2);e3=es(z,3);e4=es(z,4);pi=prod(z)
    delta=S*S*e3-4*S*e4+12*pi
    epsilon=e4*e4*e2-4*S*e4*pi+12*pi*pi
    # Strictly positive, explicit denominator factors on z_i>0.
    factors=[ctx.constant(2),ctx.constant(3),*z,S,e4,delta,epsilon]
    names=["2","3",*[str(x) for x in z],"S","e4","delta","epsilon"]
    count=len(factors)
    def exp(**kw):
        out=[0]*count
        for name,value in kw.items():out[names.index(name)]=value
        return out
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
    P=FM([[(S if i==j else zero)-z[j] for j in range(5)] for i in range(5)],exp(S=1))
    pairs=list(itertools.combinations(range(5),2))
    triples=list(itertools.combinations(range(5),3))
    def op(I,i,p=1):return prod(z[j]**p for j in I if j!=i)
    R=FM([[op(J,i) if i in J else zero for J in pairs] for i in range(5)])
    Rs=FM([[one if i in J else zero for i in range(5)] for J in pairs])
    C=FM([[op(J,i,2) if i in J else zero for J in pairs] for i in range(5)])
    Cs=FM([[sum((z[j] for j in J if j!=i),zero) if i in J else zero for i in range(5)] for J in pairs])
    F1=R@Rs;adj1,det1=adjdet(F1.A);assert det1==4*delta
    p1=exp(delta=1);p1[0]=2
    F1i=FM(adj1,p1)
    R2=FM([[op(J,i) if i in J else zero for J in triples] for i in range(5)])
    R2s=FM([[one if i in J else zero for i in range(5)] for J in triples])
    F2=R2@R2s;adj2,det2=adjdet(F2.A);assert det2==9*epsilon
    p2=exp(epsilon=1);p2[1]=2
    F2i=FM(adj2,p2)
    L1=P@F1i@P;L2=P@F2i@P
    Epoly=[[
        xd(pi,z[i])*es(tuple(z[k] for k in range(5) if k!=i),3) if i==j
        else -xd(pi*pi,z[i]**2*z[j]) for j in range(5)] for i in range(5)]
    E=FM(Epoly,exp(e4=1))
    # E is the already proved actual compressed inverse of Gamma_3.
    mark("factored_complete_low_operators",L1=L1.summary(),L2=L2.summary(),E=E.summary())

    # e = sum a_i^-1 E_i*; ed=e*.  In u_I=v_I/a_I coordinates,
    # e(I,i)=1/z_(I\i), while ed(i,I)=1.
    pp=[0]*count
    for k in range(2,7):pp[k]=1
    ec=FM([[xd(pi,op(J,i)) if i in J else zero for i in range(5)] for J in pairs],pp)
    ed=FM([[one if i in J else zero for J in pairs] for i in range(5)])
    d3=FM([[prod(z[i] for i in J if i not in I) if set(I).issubset(J) else zero
            for J in triples] for I in pairs])
    d3s=FM([[one if set(I).issubset(J) else zero for I in pairs] for J in triples])
    # Both formulas are the PHYSICAL adjoints in their inherited metrics.
    F=Cs+ec@L1@E
    Fs=C+E@L1@ed
    mark("single_joint_source_before_outer_gram",F=F.summary(),Fs=Fs.summary())
    V=d3s@F@L2
    Vs=L2@Fs@d3
    mark("same_physical_V_and_adjoint",V=V.summary(),Vs=Vs.summary())
    H=R2@V;Hs=Vs@R2s
    first=Vs@V
    mark("unprojected_same_source_square",first=first.summary(),H=H.summary())
    second=Hs@F2i@H
    mark("complete_Moore_Penrose_removed_square",second=second.summary())
    cost=first-second
    mark("actual_S2_cost",cost=cost.summary())
    # Its right and left source is the same L, and the single complete
    # H3 projection proves positivity; this is not an arbitrary 5x5 trace.
    assert (P@cost@P).equals(cost)
    trN=sum((cost.A[i][j]*cost.A[j][i] for i in range(5) for j in range(5)),zero)
    scalar=FM([[trN]],[2*n for n in cost.p])
    N=scalar.A[0][0];D=scalar.denominator()
    assert not N or int(N.total_degree())==int(D.total_degree())
    gap=D-4*N;sharp=3*D-16*N
    mark("exact_cost_square_trace",degree=int(D.total_degree()),N_terms=len(N.to_dict()),D_terms=len(D.to_dict()))
    def stats(poly):
        d=poly.to_dict();canon=[[[int(e) for e in p],int(c)] for p,c in sorted(d.items())]
        return dict(terms=len(d),degree=int(poly.total_degree()),negative=sum(c<0 for c in d.values()),
          sha256=hashlib.sha256(json.dumps(canon,separators=(",",":")).encode()).hexdigest())
    dictionaries=[p.to_dict() for p in [N,D,gap,sharp]]
    orbits={}
    for powers in set().union(*(set(d) for d in dictionaries)):
        part=tuple(sorted(powers,reverse=True));cs=tuple(int(d.get(powers,0)) for d in dictionaries)
        if part in orbits:assert orbits[part]==cs,"nonsymmetric trace"
        else:orbits[part]=cs
    for part,cs in orbits.items():
        for powers in set(itertools.permutations(part)):
            assert tuple(int(d.get(powers,0)) for d in dictionaries)==cs
    records=[dict(partition=list(p),multiplicity=len(set(itertools.permutations(p))),coefficients=list(c))
             for p,c in sorted(orbits.items(),reverse=True)]
    passed=bool(gap) and all(c>=0 for c in gap.to_dict().values())
    sharper=bool(sharp) and all(c>=0 for c in sharp.to_dict().values())
    out=dict(status="CERTIFIED" if passed else "INCONCLUSIVE",
      statement="complete five-site birth-two S2 via same-source cost-square",
      identity="Tr((A*Gu A)^2)=N/D",target="N/D<1/4",
      theorem_dependency="same actual five-site low primitive budget>I/2",
      source="V=d3*(C*+e L1 L3^-1)L2",projector="I-R2* F2^-1 R2, R2=d^2/2",
      all_cross_terms_retained=True,known_denominator_factors=scalar.summary()["den_factors"],
      one_quarter_gap_passed=passed,three_sixteenths_gap_passed=sharper,
      N=stats(N),D=stats(D),gap=stats(gap),three_sixteenths_gap=stats(sharp),
      symmetric_orbit_count=len(records),
      negative_gap_orbits=[x for x in records if x["coefficients"][2]<0][:50],
      elapsed_seconds=time.monotonic()-start,stages=stages)
    if full_orbits:out["complete_symmetric_orbits"]=records
    return out

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path,default=Path(__file__).with_suffix(".json"))
    p.add_argument("--full-orbits",action="store_true")
    a=p.parse_args();out=build(a.full_orbits)
    out["source_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    a.output.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k!="complete_symmetric_orbits"},indent=2),flush=True)
if __name__=="__main__":
    main()
    signal.alarm(0)
