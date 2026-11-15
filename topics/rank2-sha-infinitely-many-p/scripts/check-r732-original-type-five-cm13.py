#!/usr/bin/env python3
"""R732: actual full degree34/type5 CM13 trace over Q(omega).

Original basis -sigma^34*x*y*X^j, j=0..4, b=1.
Rebuild R297 division functions and the exact R307 y-ratio in every fiber.
All arithmetic is rational or quadratic rational. No saved outputs are inputs;
no output files are written. Intended public Actions: --workers=4,
python-flint==0.9.0. Finite auxiliary checks of the q715 source are separate.
"""
from __future__ import annotations
import argparse, concurrent.futures, hashlib, json, math, sys, time
from flint import fmpq
START=time.time()
ARG=argparse.ArgumentParser()
ARG.add_argument("--workers",type=int,default=4)
ARGS=ARG.parse_args()
Q=fmpq
Z=(Q(0),Q(0)); O=(Q(1),Q(0)); W=(Q(0),Q(1))
def K(a=0,b=0,d=1):return (Q(a)/d,Q(b)/d)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    t=a[1]*b[1]
    return (a[0]*b[0]-t,a[0]*b[1]+a[1]*b[0]-t)
def scale(a,s):return (a[0]*s,a[1]*s)
def inv(a):
    n=a[0]*a[0]-a[0]*a[1]+a[1]*a[1]
    assert n
    return ((a[0]-a[1])/n,-a[1]/n)
def div(a,b):return mul(a,inv(b))
def conj(a):return (a[0]-a[1],-a[1])
def power(a,n):
    r=O
    while n:
        if n&1:r=mul(r,a)
        a=mul(a,a);n//=2
    return r
def sumk(xs):
    r=Z
    for a in xs:r=add(r,a)
    return r
def enc(a):return [str(a[0]),str(a[1])]
def trim(A):
    A=list(A)
    while A and A[-1]==Z:A.pop()
    return A
def pa(A,B):return trim([add(A[i] if i<len(A) else Z,B[i] if i<len(B) else Z) for i in range(max(len(A),len(B)))])
def pn(A):return trim([neg(a) for a in A])
def ps(A,s):return trim([mul(a,s) for a in A])
def pm(A,B):
    C=[Z]*(len(A)+len(B)-1 if A and B else 0)
    for i,a in enumerate(A):
        if a==Z:continue
        for j,b in enumerate(B):
            if b!=Z:C[i+j]=add(C[i+j],mul(a,b))
    return trim(C)
def pd(A):return trim([scale(a,i+1) for i,a in enumerate(A[1:])])
def pq(A,B):
    R=trim(A);B=trim(B);assert B
    C=[Z]*max(0,len(R)-len(B)+1)
    ib=inv(B[-1])
    while len(R)>=len(B):
        j=len(R)-len(B);a=mul(R[-1],ib);C[j]=a
        for k,b in enumerate(B):R[j+k]=sub(R[j+k],mul(a,b))
        R=trim(R)
    return trim(C),R
def rem(A,F):return pq(A,F)[1]
def pi(A,F):
    R0,R1=F[:],rem(A,F);T0,T1=[],[O]
    while R1:
        q,R2=pq(R0,R1)
        T2=rem(pa(T0,pn(pm(q,T1))),F)
        R0,R1,T0,T1=R1,R2,T1,T2
    assert len(R0)==1 and R0[0]!=Z
    return rem(ps(T0,inv(R0[0])),F)
def ppow(A,n,F):
    r=[O];A=rem(A,F)
    while n:
        if n&1:r=rem(pm(r,A),F)
        A=rem(pm(A,A),F);n//=2
    return r
def peval(P,a):return sumk(mul(c,power(a,j)) for j,c in enumerate(P))

G=K(4,1);GB=conj(G)
q=ps([K(64,48,13),Z,Z,K(8,12),Z,Z,O],G)
qb=[conj(v) for v in q]
def isogeny(QP,g):
    q2=pm(QP,QP);qp=pd(QP);qpp=pd(qp)
    num=pa(pa(ps(pm([Z,O],q2),K(13)),
       ps(pm([O,Z,Z,O],pa(pm(qpp,QP),pn(pm(qp,qp)))),K(-4))),
       ps(pm([Z,Z,O],pm(qp,QP)),K(-6)))
    den=ps(q2,mul(g,g))
    return num,den
N,D=isogeny(q,G);NB,DB=isogeny(qb,GB)
def ratio_derivative(num,den,F):
    return rem(pm(pa(pm(pd(num),den),pn(pm(num,pd(den)))),
                  pi(pm(den,den),F)),F)
def fiber(a):
    F=pa(N,ps(D,K(-a)));F=ps(F,inv(F[-1]))
    assert len(F)==14
    pi(pd(F),F) # separability of the entire degree13 fiber
    ratio=rem(pm(qb,pi(q,F)),F)
    xb=rem(pm(NB,pi(DB,F)),F)
    yr=ps(rem(pm(ratio_derivative(NB,DB,F),
                   pi(ratio_derivative(N,D,F),F)),F),div(G,GB))
    r34=ppow(ratio,34,F)
    value=rem(pm(pm(r34,yr),xb),F)
    step=ppow(xb,3,F);fp=pd(F)
    row=[]
    for j in range(5):
        r=rem(pm(value,fp),F);row.append(r[12] if len(r)>12 else Z)
        value=rem(pm(value,step),F)
    # This is the unchanged even S anchor, fixing the same absolute trace phase.
    sp=[K(-128,0,7),K(-80,0,7),K(-12,0,7),K(-53,0,7),O]
    sv=[]
    for j,c in enumerate(sp):sv=pa(sv,ps(ppow(xb,2+3*j,F),c))
    rt=rem(pm(rem(pm(r34,sv),F),fp),F)
    sa=mul(power(K(a),2),peval(sp,power(K(a),3)))
    assert (rt[12] if len(rt)>12 else Z)==neg(mul(G,sa))
    print("R732 complete fiber",a,"elapsed",round(time.time()-START,3),file=sys.stderr,flush=True)
    return a,row

def rref(M,rhs=None):
    A=[list(r)+([rhs[i]] if rhs is not None else []) for i,r in enumerate(M)]
    width=len(M[0]);rank=0;piv=[]
    for j in range(width):
        pos=next((i for i in range(rank,len(A)) if A[i][j]!=Z),None)
        if pos is None:continue
        A[rank],A[pos]=A[pos],A[rank]
        d=inv(A[rank][j]);A[rank]=[mul(v,d) for v in A[rank]]
        for i in range(len(A)):
            if i==rank or A[i][j]==Z:continue
            c=A[i][j];A[i]=[sub(v,mul(c,w)) for v,w in zip(A[i],A[rank])]
        piv.append(j);rank+=1
        if rank==len(A):break
    sol=None
    if rhs is not None:
        assert all(all(v==Z for v in r[:width]) and r[-1]==Z for r in A[rank:])
        sol=[Z]*width
        for i,j in enumerate(piv):sol[j]=A[i][-1]
    return A,piv,sol
def mm(A,B):
    return [[sumk(mul(a,b) for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def ma(A,B):return [[add(a,b) for a,b in zip(r,s)] for r,s in zip(A,B)]
def ms(A,c):return [[mul(a,c) for a in r] for r in A]
def eye(n):return [[O if i==j else Z for j in range(n)] for i in range(n)]
def mpow(A,n):
    R=eye(len(A))
    while n:
        if n&1:R=mm(R,A)
        A=mm(A,A);n//=2
    return R
def null(M):
    R,piv,_=rref(M);pset=set(piv);out=[]
    for j in range(len(M[0])):
        if j in pset:continue
        v=[Z]*len(M[0]);v[j]=O
        for i,k in enumerate(piv):v[k]=neg(R[i][j])
        out.append(v)
    return out

def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=ARGS.workers) as ex:
        rows=dict(ex.map(fiber,range(2,9)))
    V=[[K(a**(1+3*j)) for j in range(5)] for a in range(2,7)]
    M=[[Z]*5 for _ in range(5)]
    for j in range(5):
        _,piv,col=rref(V,[rows[a][j] for a in range(2,7)])
        assert len(piv)==5
        for i,v in enumerate(col):M[i][j]=v
    for a in (7,8):
        assert mm([[K(a**(1+3*j)) for j in range(5)]],M)[0]==rows[a]
    A=ms(M,inv(G));I=eye(5);B=I;ch=[O]
    for k in range(1,6):
        B=mm(A,B)
        c=scale(sumk(B[i][i] for i in range(5)),Q(-1,k));ch.append(c)
        B=ma(B,ms(I,c))
    assert all(v==Z for r in B for v in r)
    roots=[O,neg(O),W,neg(W),mul(W,W),neg(mul(W,W))]
    lines=[]
    remaining=list(reversed(ch))
    for ev in roots:
        for v in null(ma(A,ms(I,neg(ev)))):
            # In this negative-y basis, the last coordinate is the z^5 coefficient.
            lead=next((j for j in range(4,-1,-1) if v[j]!=Z))
            v=[div(c,v[lead]) for c in v]
            quotient,remainder=pq(remaining,[neg(ev),O]);assert not remainder
            remaining=quotient
            assert mm(A,[[x] for x in v])==[[mul(ev,x)] for x in v]
            lines.append({"normalized_CM13_eigenvalue":enc(ev),
                          "polynomial_ascending":[enc(x) for x in v],
                          "first_order":29-6*lead,
                          "first_coefficient":enc(O)})
    power18=mpow(A,18)==I
    ans={
      "format":"R732 exact original S34 type5 norm13 full trace",
      "status":"PASS",
      "field":"Q(omega), omega^2+omega+1=0",
      "basis":"-sigma^34*x*y*X^j, j=0,...,4; b=1",
      "fitting_full_fibers":list(range(2,7)),
      "additional_full_fibers":[7,8],
      "even_S_absolute_anchor":"M13 S=-gamma13 S in every same fiber",
      "normalized_CM13_matrix":[[enc(x) for x in row] for row in A],
      "normalized_characteristic_descending":[enc(x) for x in ch],
      "mu6_eigenlines":lines,
      "remaining_characteristic_ascending":[enc(x) for x in remaining],
      "normalized_eighteenth_power_identity":power18,
      "elapsed_seconds":time.time()-START,
      "scope":"Full characteristic-zero operator, not an identification of all its finite Schwartz characters or any negative unit moment.",
      "outputs_persisted":False}
    print(json.dumps(ans,separators=(",",":")))
if __name__=="__main__":main()
