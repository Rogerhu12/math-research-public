#!/usr/bin/env python3
"""R781: the original rational flag via an actual unit-minor prefix gate.
Run mathematics only in public Actions. Pure Python finite-field arithmetic.
A mod-p nullspace is used ONLY after all rational prefix rows have a unit minor.
No output files are persisted.
"""
from __future__ import annotations
import argparse, hashlib, json, math, sys

def prime(p):
    return p >= 2 and all(p % d for d in range(2, math.isqrt(p)+1))

def add(a,b,p,cap):
    c=[0]*min(cap,max(len(a),len(b)))
    for i,x in enumerate(a[:cap]): c[i]=(c[i]+x)%p
    for i,x in enumerate(b[:cap]): c[i]=(c[i]+x)%p
    return c

def scale(a,c,p):
    return [(x*c)%p for x in a]

def mul(a,b,p,cap):
    if not a or not b: return []
    c=[0]*min(cap,len(a)+len(b)-1)
    for i,x in enumerate(a[:cap]):
        if x:
            for j,y in enumerate(b[:cap-i]):
                if y: c[i+j]=(c[i+j]+x*y)%p
    return c

def shift(a,d,cap):
    return ([0]*d+a)[:cap]

def power(a,n,p,cap):
    r=[1]
    while n:
        if n&1: r=mul(r,a,p,cap)
        a=mul(a,a,p,cap)
        n//=2
    return r

def exponential(loga,n,p,cap):
    # exp(n loga) is needed only through t^(s-1), below both p denominators.
    c=[1]+[0]*(cap-1)
    for k in range(1,cap):
        c[k]=sum(j*n*loga[j]*c[k-j] for j in range(1,k+1))%p*pow(k,-1,p)%p
    return c

def original_prefix(D,p):
    s=(p+1)//6
    cap=s+1
    q=[0]*s
    q[1]=-2*pow(5,-1,p)%p
    for j in range(2,s):
        assert (6*j-1)%p
        q[j]=q[j-1]*(6*j-4)*pow(6*j-1,-1,p)%p
    logtheta=[0]+[-q[j]*pow(3*j,-1,p)%p for j in range(1,s)]
    p4=mul(mul([1,-1],[1,8],p,cap),
           [1,4*pow(7,-1,p)%p,16*pow(7,-1,p)%p],p,cap)
    v0=mul(mul([1,-4],[1,-20,-8],p,cap),[1,96,48,-64],p,cap)
    t_dp4=[0]+[j*p4[j]%p for j in range(1,len(p4))]
    B=add(add(scale(mul(q,p4,p,cap),34,p),scale(p4,-6,p),p,cap),
          scale(t_dp4,-6,p),p,cap)
    # There is no q_s or logtheta_s here. S,T have t factor and U t^5,
    # so every prefix coefficient r_0,...,r_s is independent of them.
    S=scale(shift(mul(exponential(logtheta,17,p,s),p4,p,cap),1,cap),-1,p)
    T=scale(shift(mul(mul(exponential(logtheta,36,p,s),p4,p,cap),v0,p,cap),1,cap),-1,p)
    U=scale(shift(mul(mul([1,-3,3,-1],exponential(logtheta,102,p,s),p,cap),
                      power(B,6,p,cap),p,cap),5,cap),-1,p)
    for f in (S,T,U): f.extend([0]*(cap-len(f)))
    assert S[1]==T[1]==p-1 and U[5]==-(6**6)%p
    powers=[]
    for f in (S,T,U):
        pp=[[1]]
        for _ in range(D): pp.append(mul(pp[-1],f,p,cap))
        powers.append(pp)
    labels,cols=[],[]
    for total in range(D+1):
        for nu in range(total+1):
            for b in range(total-nu+1):
                a=total-b-nu
                col=mul(mul(powers[0][a],powers[1][b],p,cap),powers[2][nu],p,cap)
                col.extend([0]*(cap-len(col)))
                labels.append([a,b,nu]);cols.append(col)
    rows=[[cols[j][k] for j in range(len(cols))] for k in range(cap)]
    cp=2*((-1)**s)*math.comb(3*s-1,s-1)%p
    qprev=1
    # Independent product verifies the first actual rational Q residue.
    if s==1:
        qres=-2%p
    else:
        qres=q[s-1]*(6*s-4)%p
    assert qres==cp and cp
    pole=[2*cp*(17 if lab==[1,0,0] else 36 if lab==[0,1,0] else 0)%p for lab in labels]
    return s,labels,rows,pole,cp

def rref_with_gate(rows,p):
    m,n=len(rows),len(rows[0])
    A=[r[:] for r in rows]
    pivots=[];det=1;r=0;swaps=0
    for col in range(n):
        pivot=next((i for i in range(r,m) if A[i][col]),None)
        if pivot is None: continue
        if pivot!=r: A[r],A[pivot]=A[pivot],A[r];swaps+=1
        u=A[r][col];det=det*u%p;inv=pow(u,-1,p)
        A[r]=[x*inv%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][col]:
                c=A[i][col]
                A[i]=[(x-c*y)%p for x,y in zip(A[i],A[r])]
        pivots.append(col);r+=1
        if r==m: break
    return A,pivots,det*((-1)**swaps)%p

def check(D,p):
    if D<1 or not prime(p) or p%6!=5 or p<=119*D or p<11:
        raise ValueError("Require explicit D>=1, inert prime p>119D and p>=11")
    s,labels,rows,pole,cp=original_prefix(D,p)
    N=len(labels)
    assert N==math.comb(D+3,3)
    print("R781 actual prefix D=%s p=%s rows=%s cols=%s"%(D,p,s+1,N),
          file=sys.stderr,flush=True)
    A,pivots,minor=rref_with_gate(rows,p)
    rank=len(pivots)
    residual=pole[:]
    for i,j in enumerate(pivots):
        c=residual[j]
        residual=[(x-c*y)%p for x,y in zip(residual,A[i])]
    augrank=rank+int(any(residual))
    report={"degree":D,"prime":p,"s":s,"tested_order":s+1,"source_rank":N,
            "prefix_rows":len(rows),"prefix_rank_mod_p":rank,
            "prefix_full_row_rank":rank==len(rows),
            "augmented_rank_mod_p":augrank,"cp":cp,
            "prefix_sha256":hashlib.sha256(json.dumps(rows,separators=(",",":")).encode()).hexdigest(),
            "source_labels":labels,"pivot_columns":pivots,
            "full_prefix_unit_minor_determinant":minor if rank==len(rows) else None,
            "pole_row_nonzero":[[j,labels[j],v] for j,v in enumerate(pole) if v],
            "pole_row_residual_nonzero":[[j,v] for j,v in enumerate(residual) if v],
            "actual_rational_kernel_gate_paid":rank==len(rows)}
    if rank==len(rows) and any(residual):
        free=next(j for j,x in enumerate(residual) if x)
        z=[0]*N;z[free]=1
        for i,j in enumerate(pivots): z[j]=-A[i][free]%p
        assert all(sum(x*y for x,y in zip(rr,z))%p==0 for rr in rows)
        val=sum(x*y for x,y in zip(pole,z))%p
        assert val==residual[free] and val
        report.update({"actual_ordered_image_p_valuation":-1,
                       "actual_ordered_operator_norm":"p",
                       "kernel_reduction_witness":[[j,v] for j,v in enumerate(z) if v],
                       "pole_on_witness":val,
                       "scope":"Unit minor pays rational saturated kernel reduction; integral prefix and simple pole give exact -1."})
    elif rank==len(rows):
        report["scope"]="Gate paid; pole residue vanishes on actual kernel, so this one ordered row is p-integral."
        report["actual_ordered_image_p_valuation_lower_bound"]=0
    else:
        report["scope"]="Gate NOT paid. No rational saturated-kernel conclusion is drawn from this mod-p kernel."
    return report

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--pairs",default="8:953")
    args=ap.parse_args()
    pairs=[tuple(map(int,x.split(":"))) for x in args.pairs.split(",")]
    if len(pairs)>8 or any(D>30 or p>20000 for D,p in pairs):
        raise ValueError("Explicit bounded public calculation required")
    reports=[check(D,p) for D,p in pairs]
    print(json.dumps({"format":"R781 original first inert pole and paid rational-prefix gate",
                      "reports":reports,"outputs_persisted":False},separators=(",",":")))
if __name__=="__main__":
    main()
