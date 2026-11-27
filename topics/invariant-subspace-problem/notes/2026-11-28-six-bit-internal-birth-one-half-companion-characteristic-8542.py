#!/usr/bin/env python3
"""NEW six-site birth-one INTERNAL j=2 half target.

H=C3*Gamma1*C3-2*C4 = C3*F1^{-1}*C3-2*C4 on the actual K1.
The full six-dimensional matrix is formed before removing its true
vacuum zero line. Primitive positive polynomial factors are removed from Faddeev
matrices with exact divisions, preserving the full original polynomial.
Each coefficient and the full continuation matrix are checkpointed.
No positivity or completion is inferred from a partial return.
"""
from __future__ import annotations
import resource, signal
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
import argparse, hashlib, json, math, time
from pathlib import Path
from flint import fmpz_mpoly_ctx

def build(path):
    start=time.monotonic();stages=[]
    ctx=fmpz_mpoly_ctx.get(("S","Z","W","U","V","X"))
    es=list(ctx.gens());S,Z,W,U,V,X=es;zero=ctx.constant(0);one=ctx.constant(1)
    def ident(n):return [[one if i==j else zero for j in range(n)] for i in range(n)]
    def ma(A,B):return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
    def ms(A,c):return [[c*a for a in row] for row in A]
    def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),zero) for j in range(len(B[0]))] for i in range(len(A))]
    def xd(a,b):
        q,r=divmod(a,b);assert not r,"nonexact division";return q
    def rec(p):return [[[int(e) for e in ex],int(c)] for ex,c in sorted(p.to_dict().items())]
    def matrix_rec(A):return [[rec(p) for p in row] for row in A]
    def stats(A):return dict(max_terms=max(len(p.to_dict()) for row in A for p in row),max_ordinary_degree=max((int(p.total_degree()) for row in A for p in row if p),default=-1))
    def mark(stage,**kw):
        r=dict(stage=stage,seconds=time.monotonic()-start,**kw);stages.append(r);print(json.dumps(r),flush=True)
    delta=S**3*W-4*S*S*U+12*S*V-32*X
    names=["S","Z","W","U","V","X","delta6"]
    factors=es+[delta];weights=[1,2,3,4,5,6,6]
    unit_values=[6,15,20,15,6,1,2560]
    def factor_values(powers):
        return math.prod(a**n for a,n in zip(unit_values,powers))
    def pull(A,extract_integer=True):
        if not any(p for row in A for p in row):return A,1,[0]*7
        powers=[0]*7;B=[row[:] for row in A]
        for j,f in enumerate(factors):
            while True:
                qs=[];ok=True
                for row in B:
                    qr=[]
                    for p in row:
                        q,r=divmod(p,f)
                        if r:ok=False;break
                        qr.append(q)
                    if not ok:break
                    qs.append(qr)
                if not ok:break
                B=qs;powers[j]+=1
        content=0
        for row in B:
            for p in row:
                for c in p.to_dict().values():content=math.gcd(content,abs(int(c)))
        assert content>0
        if not extract_integer:content=1
        if content>1:B=[[xd(p,ctx.constant(content)) for p in row] for row in B]
        return B,content,powers

    I=ident(6);T=[[zero for _ in range(6)] for _ in range(6)]
    for j in range(5):T[j+1][j]=one
    for i in range(6):T[i][5]=((-1)**(7-i))*es[5-i]
    moments=[ctx.constant(6)]
    for k in range(1,7):
        moments.append(sum((((-1)**(i-1))*es[i-1]*moments[k-i] for i in range(1,k)),zero)+((-1)**(k-1))*k*es[k-1])
    Q=[[zero for _ in range(6)] for _ in range(6)];Q[0]=moments[1:]
    T2=mm(T,T);T3=mm(T2,T)
    F1=ma(ma(ms(I,S),ms(T,-2)),Q)
    F2=ma(ma(ma(ma(ma(ms(I,Z),ms(T,-2*S)),ms(T2,3)),ms(Q,S)),ms(mm(T,Q),-1)),ms(mm(Q,T),-1))
    F3=ma(ma(ma(ma(ms(I,W),ms(T,-2*Z)),ms(T2,3*S)),ms(T3,-4)),ms(Q,Z))
    F3=ma(F3,ms(ma(mm(T,Q),mm(Q,T)),-S))
    F3=ma(ma(ma(F3,mm(T2,Q)),mm(mm(T,Q),T)),mm(Q,T2))
    # Complete inverse: no primitive compression precedes this adjugate.
    FF=I;adj=None;det=None
    for k in range(1,7):
        if k==6:adj=ms(FF,-1)
        BF=mm(F1,FF);ck=xd(-sum((BF[i][i] for i in range(6)),zero),ctx.constant(k))
        FF=ma(BF,ms(I,ck))
        if k==6:det=ck
    assert det==4*delta and all(not p for row in FF for p in row)
    check=mm(F1,adj);assert all(check[i][j]==(det if i==j else zero) for i in range(6) for j in range(6))
    G=ma(ma(ms(I,Z),ms(T,-S)),T2)
    P3=ma(ma(ma(ms(I,W),ms(T,-Z)),ms(T2,S)),ms(T3,-1))
    B=ma(ms(F2,W),ms(mm(mm(G,Q),G),-1))
    # J = e3^2 det(F1) e4 * (C3 F1^{-1} C3 - 2 C4).
    J=ma(ma(ms(mm(mm(B,adj),B),U),ms(F3,-2*W*W*det*U)),ms(mm(mm(P3,Q),P3),2*W*W*det))
    assert all(not J[i][0] for i in range(6)),"actual vacuum line"
    A=[row[1:] for row in J[1:]]
    mark("full_internal_precision_and_complete_inverse",det_F1="4 delta6",full_matrix=stats(J),quotient=stats(A))
    out=dict(schema="isp-six-site-full-birth-one-internal-half-characteristic-v1",
      status="EXACT_COEFFICIENTS_PARTIAL",source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      variables=["e1(z)","e2(z)","e3(z)","e4(z)","e5(z)","e6(z)"],weighted_degrees=[1,2,3,4,5,6],
      target="Gamma2 Gamma3^{-1} Gamma2 < (1/2) Gamma1 on the SAME six-site K1",
      actual_matrix="J=e3^2 det(F1) e4 (C3 F1^{-1} C3-2 C4)",
      positive_polynomial_factors={n:rec(f) for n,f in zip(names,factors)},
      determinant_factor="det(F1)=4 delta6>0 on actual positive weights",
      characteristic="det(t I6+J)=t*(t^5+c1*t^4+c2*t^3+c3*t^2+c4*t+c5)",
      complete_quotient_matrix=matrix_rec(A),complete_coefficients=[],stages=stages,
      scope="Exact coefficient data is not positive-weight certification unless all five original coefficient signs are paid.")
    def save():
        out["elapsed_seconds"]=time.monotonic()-start
        tmp=path.with_suffix(".checkpoint.tmp");tmp.write_text(json.dumps(out,separators=(",",":"))+"\n");tmp.replace(path)
    F=ident(5);scale_content=1;scale_powers=[0]*7
    out["continuation"]=dict(order=0,positive_integer_scale=1,positive_factor_powers=scale_powers[:],matrix=matrix_rec(F));save()
    for k in range(1,6):
        AF=mm(A,F)
        chat=xd(-sum((AF[i][i] for i in range(5)),zero),ctx.constant(k))
        ebase=((-1)**k)*chat
        terms=ebase.to_dict()
        expected_degree=19*k-sum(a*b for a,b in zip(weights,scale_powers))
        assert terms and all(sum((i+1)*int(e) for i,e in enumerate(p))==expected_degree for p in terms)
        eq_base=sum(int(c)*math.prod(math.comb(6,i+1)**int(e) for i,e in enumerate(p)) for p,c in terms.items())
        assert scale_content*factor_values(scale_powers)*eq_base==math.comb(5,k)*61440000**k
        small,content,powers=pull([[ebase]]);rp=small[0][0]
        totalpowers=[a+b for a,b in zip(scale_powers,powers)]
        data=rec(rp);canon=json.dumps(data,separators=(",",":"))
        record=dict(index=k,original_weighted_degree=19*k,
          positive_integer_content=scale_content*content,
          positive_factor_powers={n:p for n,p in zip(names,totalpowers) if p},
          reduced_weighted_degree=19*k-sum(a*b for a,b in zip(weights,totalpowers)),
          reduced_terms=len(data),negative_terms=sum(c<0 for _,c in data),
          reduced_sha256=hashlib.sha256(canon.encode()).hexdigest(),
          complete_reduced_elementary_coefficients=data,
          equal_weight_original_value=math.comb(5,k)*61440000**k)
        out["complete_coefficients"].append(record)
        Ftemp=ma(AF,ms(ident(5),chat))
        out["continuation"]=dict(order=k,positive_integer_scale=scale_content,positive_factor_powers=scale_powers[:],matrix=matrix_rec(Ftemp))
        save()
        mark("complete_internal_characteristic_coefficient",
             **{a:b for a,b in record.items() if a!="complete_reduced_elementary_coefficients"},
             checkpoint_bytes=path.stat().st_size)
        if k<5:
            F,mcontent,mpowers=pull(Ftemp,extract_integer=False)
            scale_content*=mcontent;scale_powers=[a+b for a,b in zip(scale_powers,mpowers)]
            out["continuation"]=dict(order=k,positive_integer_scale=scale_content,positive_factor_powers=scale_powers[:],matrix=matrix_rec(F))
            save()
            mark("same_faddeev_matrix_positive_factor_reduction",index=k,positive_integer_scale=scale_content,
                 positive_factor_powers={n:p for n,p in zip(names,scale_powers) if p},matrix=stats(F))
        else:
            assert all(not p for row in Ftemp for p in row),"complete actual Cayley-Hamilton return"
    out["cayley_hamilton_return"]=True
    passed=all(c>0 for r in out["complete_coefficients"] for _,c in r["complete_reduced_elementary_coefficients"])
    out["status"]="CERTIFIED_ELEMENTARY" if passed else "EXACT_CHARACTERISTIC_READY"
    out["all_reduced_elementary_coefficients_positive"]=passed
    out.pop("continuation",None);save()
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path,default=Path(__file__).with_suffix(".json"))
    ap.add_argument("--full-orbits",action="store_true",help="Compatibility; all exact coefficients are always retained.")
    args=ap.parse_args();out=build(args.output)
    report={k:v for k,v in out.items() if k not in ("complete_quotient_matrix","positive_polynomial_factors","complete_coefficients")}
    report["complete_coefficients"]=[{k:v for k,v in r.items() if k!="complete_reduced_elementary_coefficients"} for r in out["complete_coefficients"]]
    print(json.dumps(report,indent=2),flush=True)
if __name__=="__main__":
    main()
    signal.alarm(0)
