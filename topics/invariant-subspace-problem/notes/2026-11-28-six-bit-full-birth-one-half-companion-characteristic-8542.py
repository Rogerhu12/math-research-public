#!/usr/bin/env python3
"""NEW full six-site birth-one half input, not the old six-support matrix.

The actual full precisions C2 and C3 are formed first in six-root
companion coordinates. J=e2^2 e3 (C2^2-2 C3) has its complete vacuum
column zero. Only then is the invariant zero line factored out.
Faddeev-LeVerrier computes all five characteristic coefficients.
Every completed coefficient is checkpointed with exact integer data.
No positivity is inferred from an incomplete output or mixed signs.
"""
from __future__ import annotations
import resource, signal
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
import argparse, hashlib, json, math, time
from pathlib import Path
from flint import fmpz_mpoly_ctx

def build(checkpoint_path):
    start=time.monotonic(); stages=[]
    ctx=fmpz_mpoly_ctx.get(("S","Z","W","U","V","X"))
    elementary=list(ctx.gens());S,Z,W,U,V,X=elementary
    zero=ctx.constant(0);one=ctx.constant(1);n=6
    def ident(m):return [[one if i==j else zero for j in range(m)] for i in range(m)]
    def ma(A,B):return [[a+b for a,b in zip(ar,br)] for ar,br in zip(A,B)]
    def ms(A,p):return [[p*a for a in ar] for ar in A]
    def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),zero) for j in range(len(B[0]))] for i in range(len(A))]
    def exact_div(a,b):
        q,r=divmod(a,b);assert not r,"nonexact polynomial division";return q
    def mark(stage,**kw):
        record=dict(stage=stage,seconds=time.monotonic()-start,**kw)
        stages.append(record);print(json.dumps(record),flush=True)
    I=ident(n)
    T=[[zero for _ in range(n)] for _ in range(n)]
    for j in range(n-1):T[j+1][j]=one
    for i in range(n):T[i][n-1]=((-1)**(n-i+1))*elementary[n-i-1]
    moments=[ctx.constant(n)]
    for k in range(1,n+1):
        p=sum((((-1)**(i-1))*elementary[i-1]*moments[k-i] for i in range(1,k)),zero)
        moments.append(p+((-1)**(k-1))*k*elementary[k-1])
    Q=[[zero for _ in range(n)] for _ in range(n)];Q[0]=moments[1:]
    T2=mm(T,T)
    F1=ma(ma(ms(I,S),ms(T,-2)),Q)
    F2=ma(ma(ma(ma(ma(ms(I,Z),ms(T,-2*S)),ms(T2,3)),ms(Q,S)),ms(mm(T,Q),-1)),ms(mm(Q,T),-1))
    Uop=ma(ms(I,S),ms(T,-1))
    Gop=ma(ma(ms(I,Z),ms(T,-S)),T2)
    # A=e2*C2.  J=e2^2*e3*(C2^2-2*C3), all on the full six-dimensional layer.
    A=ma(ms(F1,Z),ms(mm(mm(Uop,Q),Uop),-1))
    J=ma(ma(ms(mm(A,A),W),ms(F2,-2*Z*Z*W)),ms(mm(mm(Gop,Q),Gop),2*Z*Z))
    assert all(not J[i][0] for i in range(n)),"complete vacuum column must vanish"
    # First factor the genuine invariant zero line; the remaining quotient
    # has the same five physical eigenvalues as the restriction to K1.
    B=[row[1:] for row in J[1:]]
    mark("full_precision_and_actual_zero_line",
         full_dimension=6,primitive_dimension=5,
         full_matrix_max_terms=max(len(p.to_dict()) for row in J for p in row),
         quotient_max_terms=max(len(p.to_dict()) for row in B for p in row))
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out=dict(schema="isp-six-site-full-birth-one-half-characteristic-v1",
      status="EXACT_COEFFICIENTS_PARTIAL",source_sha256=source_sha256,
      variables=["e1(z)","e2(z)","e3(z)","e4(z)","e5(z)","e6(z)"],
      weighted_degrees=[1,2,3,4,5,6],
      actual_matrix="J=e2^2 e3 (C2^2-2 C3), full precisisons before zero-line quotient",
      denominator_positive="e2^2 e3",
      characteristic="det(t I_6+J)=t*(t^5+c1*t^4+c2*t^3+c3*t^2+c4*t+c5)",
      required_coefficients=5,complete_coefficients=[],
      scope="Complete characteristic coefficients alone are not positivity if their actual positive-root signs remain unproved.",
      stages=stages)
    def save():
        out["elapsed_seconds"]=time.monotonic()-start
        tmp=checkpoint_path.with_suffix(".checkpoint.tmp")
        tmp.write_text(json.dumps(out,separators=(",",":"))+"\n")
        tmp.replace(checkpoint_path)
    save()
    F=ident(5)
    for k in range(1,6):
        BF=mm(B,F)
        ck=exact_div(-sum((BF[i][i] for i in range(5)),zero),ctx.constant(k))
        F=ma(BF,ms(ident(5),ck))
        ek=((-1)**k)*ck
        terms={tuple(int(e) for e in p):int(c) for p,c in ek.to_dict().items()}
        assert terms and all(sum((i+1)*e for i,e in enumerate(p))==9*k for p in terms)
        equal=sum(c*math.prod(math.comb(6,i+1)**e for i,e in enumerate(p)) for p,c in terms.items())
        assert equal==math.comb(5,k)*18000**k,"physical equal-weight eigenvalue check"
        monomial=[min(p[i] for p in terms) for i in range(6)]
        content=math.gcd(*(abs(c) for c in terms.values()))
        reduced=[[[p[i]-monomial[i] for i in range(6)],c//content] for p,c in sorted(terms.items())]
        assert all(c%content==0 for c in terms.values())
        canonical=json.dumps([[[int(e) for e in p],int(c)] for p,c in sorted(terms.items())],separators=(",",":"))
        reduced_canonical=json.dumps(reduced,separators=(",",":"))
        record=dict(index=k,original_weighted_degree=9*k,
          positive_integer_content=content,elementary_monomial_factor=monomial,
          reduced_weighted_degree=9*k-sum((i+1)*e for i,e in enumerate(monomial)),
          original_terms=len(terms),negative_terms=sum(c<0 for c in terms.values()),
          original_sha256=hashlib.sha256(canonical.encode()).hexdigest(),
          reduced_sha256=hashlib.sha256(reduced_canonical.encode()).hexdigest(),
          equal_weight_value=equal,
          complete_reduced_elementary_coefficients=reduced)
        out["complete_coefficients"].append(record)
        save()
        mark("complete_characteristic_coefficient",
             **{a:b for a,b in record.items() if a!="complete_reduced_elementary_coefficients"},
             checkpoint_bytes=checkpoint_path.stat().st_size)
    assert all(not p for row in F for p in row),"complete five-dimensional Cayley-Hamilton return"
    out["cayley_hamilton_return"]=True
    elementary_positive=all(c>0 for record in out["complete_coefficients"] for _,c in record["complete_reduced_elementary_coefficients"])
    out["status"]="CERTIFIED_ELEMENTARY" if elementary_positive else "EXACT_CHARACTERISTIC_READY"
    out["all_elementary_coefficients_positive"]=elementary_positive
    save()
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path,default=Path(__file__).with_suffix(".json"))
    ap.add_argument("--full-orbits",action="store_true",help="Compatibility only; all elementary coefficients are always saved.")
    args=ap.parse_args();out=build(args.output)
    report={k:v for k,v in out.items() if k!="complete_coefficients"}
    report["complete_coefficients"]=[{k:v for k,v in c.items() if k!="complete_reduced_elementary_coefficients"} for c in out["complete_coefficients"]]
    print(json.dumps(report,indent=2),flush=True)
if __name__=="__main__":
    main()
    signal.alarm(0)
