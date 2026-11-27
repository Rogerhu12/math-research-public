#!/usr/bin/env python3
"""New exact input: the complete five-site, birth-two S2.

Every inverse belongs to a full physical row or to the explicitly named
primitive metric.  Coordinates on a p-subset I are v_I=b_I*u_I and have
metric diag(z_I).  The source remains the whole four-dimensional K_1.
No numerical fit, weight identification, or compression-before-inverse.

This is an attempted certificate, not a theorem until status says
CERTIFIED.  A failed coefficient test is retained as INCONCLUSIVE.
"""
from __future__ import annotations
import resource, signal
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS, (4*1024**3, 4*1024**3))
import argparse, hashlib, itertools, json, time
from pathlib import Path
from flint import fmpz_mpoly_ctx

def build(full_orbits=False):
    start=time.monotonic()
    ctx=fmpz_mpoly_ctx.get(tuple("z"+str(i+1) for i in range(5)))
    z=ctx.gens(); zero=ctx.constant(0); one=ctx.constant(1)
    stages=[]
    def mark(name,**kw):
        row=dict(stage=name,seconds=time.monotonic()-start,**kw)
        stages.append(row); print(json.dumps(row),flush=True)
    def prod(xs):
        out=one
        for x in xs: out*=x
        return out
    def es(xs,k):
        return sum((prod(v) for v in itertools.combinations(xs,k)),zero)
    def xd(a,b):
        q,r=divmod(a,b)
        assert not r,"nonexact polynomial division"
        return q
    def mm(A,B):
        assert len(A[0])==len(B)
        return [[sum((A[i][k]*B[k][j] for k in range(len(B))),zero)
                 for j in range(len(B[0]))] for i in range(len(A))]
    def ident(n):
        return [[one if i==j else zero for j in range(n)] for i in range(n)]
    def ad(A,B,sgn=1):
        return [[A[i][j]+sgn*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    def same(A,B):
        return all(A[i][j]==B[i][j] for i in range(len(A)) for j in range(len(A[0])))
    def adjdet(A):
        n=len(A); F=[row[:] for row in A]; B=ident(n); previous=one
        for k in range(n):
            pivot=F[k][k]
            assert pivot,"zero symbolic principal pivot"
            rowsF=[row[:] for row in F]; rowsB=[row[:] for row in B]
            for i in range(n):
                if i==k: continue
                for j in range(n):
                    if j!=k:
                        F[i][j]=xd(pivot*rowsF[i][j]-rowsF[i][k]*rowsF[k][j],previous)
                    B[i][j]=xd(pivot*rowsB[i][j]-rowsF[i][k]*rowsB[k][j],previous)
                F[i][k]=zero
            previous=pivot
        det=F[0][0]
        assert all(F[i][j]==(det if i==j else zero) for i in range(n) for j in range(n))
        # Exact final multiplication verifies the full inverse identity.
        AB=mm(A,B)
        assert all(AB[i][j]==(det if i==j else zero) for i in range(n) for j in range(n))
        return B,det
    class RM:
        def __init__(self,A,d=None,reduce=True):
            self.A=[row[:] for row in A]; self.d=one if d is None else d
            assert self.d
            if reduce:
                g=self.d
                for row in self.A:
                    for x in row:
                        g=g.gcd(x)
                        if g==one: break
                    if g==one: break
                if g!=one:
                    self.A=[[xd(x,g) for x in row] for row in self.A]
                    self.d=xd(self.d,g)
        def __add__(self,o):
            g=self.d.gcd(o.d); a=xd(o.d,g); b=xd(self.d,g)
            return RM([[a*self.A[i][j]+b*o.A[i][j] for j in range(len(self.A[0]))]
                       for i in range(len(self.A))],self.d*a)
        def __neg__(self): return RM([[-x for x in row] for row in self.A],self.d,False)
        def __sub__(self,o): return self+(-o)
        def __matmul__(self,o): return RM(mm(self.A,o.A),self.d*o.d)
        def scaled(self,p,q=None):
            return RM([[p*x for x in row] for row in self.A],
                      self.d*(one if q is None else q))
        def inverse(self):
            a,d=adjdet(self.A)
            return RM([[self.d*x for x in row] for row in a],d)
        def trace(self): return RM([[sum((self.A[i][i] for i in range(len(self.A))),zero)]],self.d)
        def equals(self,o): return same([[x*o.d for x in row] for row in self.A],
                                        [[x*self.d for x in row] for row in o.A])
        def summary(self):
            return dict(den_degree=int(self.d.total_degree()),den_terms=len(self.d.to_dict()),
                        max_num_degree=max(int(x.total_degree()) for row in self.A for x in row if x),
                        max_num_terms=max(len(x.to_dict()) for row in self.A for x in row))
    I=RM(ident(5)); S=sum(z,zero); e2=es(z,2); e3=es(z,3); e4=es(z,4); pi=prod(z)
    P=RM([[(S if i==j else zero)-z[j] for j in range(5)] for i in range(5)],S)
    P0=I-P
    pairs=list(itertools.combinations(range(5),2))
    triples=list(itertools.combinations(range(5),3))
    def other_product(I,i,power=1):
        return prod(z[j]**power for j in I if j!=i)
    R=RM([[other_product(J,i) if i in J else zero for J in pairs] for i in range(5)])
    Rs=RM([[one if i in J else zero for i in range(5)] for J in pairs])
    C=RM([[other_product(J,i,2) if i in J else zero for J in pairs] for i in range(5)])
    Cs=RM([[sum((z[j] for j in J if j!=i),zero) if i in J else zero
            for i in range(5)] for J in pairs])
    F1=R@Rs
    F1i=F1.inverse()
    delta=S*S*e3-4*S*e4+12*pi
    _,detF1=adjdet(F1.A)
    assert detF1==4*delta
    R2=RM([[other_product(J,i) if i in J else zero for J in triples] for i in range(5)])
    R2s=RM([[one if i in J else zero for i in range(5)] for J in triples])
    F2=R2@R2s
    F2i=F2.inverse()
    epsilon=e4*e4*e2-4*S*e4*pi+12*pi*pi
    _,detF2=adjdet(F2.A)
    assert detF2==9*epsilon
    L1=P@F1i@P; L2=P@F2i@P
    # Complete inverse, THEN compression, checked against the true precisions.
    u=[S-x for x in z]
    v=[e2-S*x+x*x for x in z]
    C2=F1-RM([[u[i]*z[j]*u[j] for j in range(5)] for i in range(5)],e2)
    C3=F2-RM([[v[i]*z[j]*v[j] for j in range(5)] for i in range(5)],e3)
    assert (C2@L1).equals(P) and (L1@C2).equals(P)
    assert (C3@L2).equals(P) and (L2@C3).equals(P)
    # Actual top Gram and its actual compressed inverse, extended by zero.
    Z2=RM([[z[i]**2 if i==j else zero for j in range(5)] for i in range(5)],pi)
    L3=P@Z2@P
    Epoly=[[
        xd(pi,z[i])*es(tuple(z[k] for k in range(5) if k!=i),3) if i==j
        else -xd(pi*pi,z[i]**2*z[j]) for j in range(5)] for i in range(5)]
    E=RM(Epoly,e4)
    assert (E@L3).equals(P) and (L3@E).equals(P)
    mark("all_complete_low_inverses_and_top_compressed_inverse",L1=L1.summary(),L2=L2.summary())

    # P_K C* and C P_K without choosing or deleting a primitive direction.
    PU_Cs=Cs-Rs@F1i@R@Cs
    C_PU=C-C@Rs@F1i@R
    assert (R@PU_Cs).equals(RM([[zero]*5 for _ in range(5)]))
    Kbb=P@(C@PU_Cs)@P
    # The hard-top identity J_(1,2)=pi^(-1/2)*complement*diag(z_I)
    # on the WHOLE five-dimensional K_2 gives the following true Gram.
    Zupper=RM([[prod(z[i]**2 for i in J) if a==b else zero
                for b in range(10)] for a,J in enumerate(pairs)],pi)
    Kg1=P@(C_PU@Zupper@PU_Cs)@P

    # Short of d_3 d_3*: C_1^ext=Fmid-Fmid R* (R Fmid R*)^-1 R Fmid.
    # R Fmid R*=4F2; the two cross terms each have factor two.
    Cd=RM([[other_product(J,i)*sum((z[j] for j in J if j!=i),zero)
            if i in J else zero for J in triples] for i in range(5)])
    Cds=RM([[sum((z[j] for j in J if j!=i),zero) if i in J else zero
             for i in range(5)] for J in triples])
    X=Cd@R2s; Xs=R2@Cds
    Kc1=P@(Cd@Cds-X@F2i@Xs)@P
    mark("upper_source_eliminated_exactly",Kbb=Kbb.summary(),Kg1=Kg1.summary(),Kc1=Kc1.summary())

    # A=(C_upper B* L2+B* L2 E L2)/2.
    # This expansion retains its two mixed terms in their original order.
    LE=L2@E@L2
    cost=((L2@Kc1@L2)+(L2@Kbb@LE)+(LE@Kbb@L2)+(LE@Kg1@LE)).scaled(one,ctx.constant(4))
    assert (P@cost@P).equals(cost)
    budget=P-L1@C3@L1
    mark("actual_S2_cost_and_budget",cost=cost.summary(),budget=budget.summary())

    # New universal birth-one theorem gives C3 <= (2/3) C2^2,
    # hence W=C2^2-C3 is positive on K_1.  Add S^2 on its true kernel.
    W=C2@C2-C3
    Waug=W+P0.scaled(S*S)
    mark("budget_precision_before_inverse",W=Waug.summary())
    Wi=Waug.inverse()
    budgeti=C2@Wi@C2
    assert (budgeti@budget).equals(P) and (budget@budgeti).equals(P)
    mark("actual_budget_inverse",inverse=budgeti.summary())
    result=(budgeti@cost).trace()
    N=result.A[0][0]; D=result.d
    # Reduction has no zero on the positive orthant: its unreduced
    # denominator consists of full positive Grams and Waug>0.
    if sum(D.to_dict().values())<0: N=-N; D=-D
    assert sum(D.to_dict().values())>0
    assert not N or int(N.total_degree())==int(D.total_degree())
    mark("exact_normalized_trace",numerator_terms=len(N.to_dict()),
         denominator_terms=len(D.to_dict()),degree=int(D.total_degree()))
    nd=N.to_dict(); dd=D.to_dict()
    def poly_stats(poly):
        data=poly.to_dict()
        canon=[[[int(e) for e in p],int(c)] for p,c in sorted(data.items())]
        return dict(terms=len(data),degree=int(poly.total_degree()),
                    negative=sum(c<0 for c in data.values()),
                    sha256=hashlib.sha256(json.dumps(canon,separators=(",",":")).encode()).hexdigest())
    def orbit_table(polys):
        dictionaries=[p.to_dict() for p in polys]
        union=set().union(*(set(d) for d in dictionaries))
        orbits={}
        for powers in union:
            part=tuple(sorted(powers,reverse=True))
            coeff=tuple(int(d.get(powers,0)) for d in dictionaries)
            if part in orbits: assert orbits[part]==coeff,"nonsymmetric exact coefficient"
            else: orbits[part]=coeff
        for part,coeff in orbits.items():
            for powers in set(itertools.permutations(part)):
                assert tuple(int(d.get(powers,0)) for d in dictionaries)==coeff
        return [dict(partition=list(p),coefficients=list(c),
                     multiplicity=len(set(itertools.permutations(p))))
                for p,c in sorted(orbits.items(),reverse=True)]
    gap=D-N; sharp_gap=3*D-4*N
    table=orbit_table([N,D,gap,sharp_gap])
    passed=bool(gap) and all(c>=0 for c in gap.to_dict().values())
    sharp_passed=bool(sharp_gap) and all(c>=0 for c in sharp_gap.to_dict().values())
    bad=[row for row in table if row["coefficients"][2]<0]
    report=dict(status="CERTIFIED" if passed else "INCONCLUSIVE",
      statement="M=5,s=2,complete-source S2",normalization="z_i=b_i^2, all five independent and positive",
      identity="Tr[(I-L1 L2^-1 L1)^-1 A*G1 A]=N/D",
      inverse_and_primitive_identities=True,actual_cross_terms_retained=True,
      known_budget_lower_bound="I-L1 L2^-1 L1 >= (1/3) I",
      coefficient_gap_passed=passed,three_quarters_gap_passed=sharp_passed,
      N=poly_stats(N),D=poly_stats(D),gap=poly_stats(gap),three_quarters_gap=poly_stats(sharp_gap),
      symmetry_orbits=len(table),negative_gap_orbits=bad[:50],
      elapsed_seconds=time.monotonic()-start,stages=stages)
    if full_orbits: report["complete_symmetric_orbits"]=table
    return report

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path,default=Path(__file__).with_suffix(".json"))
    p.add_argument("--full-orbits",action="store_true")
    a=p.parse_args()
    report=build(a.full_orbits)
    report["source_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    a.output.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:v for k,v in report.items() if k!="complete_symmetric_orbits"},indent=2),flush=True)

if __name__=="__main__":
    main()
    signal.alarm(0)
