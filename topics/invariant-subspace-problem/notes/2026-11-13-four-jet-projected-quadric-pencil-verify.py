"""Exact finite certificate for the original quartic-support quadric pencil.

Standard library only. Two homogeneous degree-ten maximal minors specialize
along one explicit integer affine line to coprime degree-ten polynomials mod
103. This proves that they have no common complex homogeneous factor.
"""
from fractions import Fraction as Q
from math import lcm
import json

K=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],
   [0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]]
P=103

def inv_exact(A):
    n=len(A);R=[[Q(x) for x in row]+[Q(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next(i for i in range(j,n) if R[i][j]);R[j],R[k]=R[k],R[j]
        u=R[j][j];R[j]=[x/u for x in R[j]]
        for i in range(n):
            if i!=j:
                u=R[i][j];R[i]=[x-u*y for x,y in zip(R[i],R[j])]
    return [row[n:] for row in R]

Ki=inv_exact(K);scale=lcm(*(x.denominator for row in Ki for x in row));assert scale==3200
C=[[int(scale*x) for x in row] for row in Ki]
basis=[]
for i in range(5):
    for j in range(i+1,5):
        A=[[0]*6 for _ in range(6)]
        A[i][j+1]+=1;A[j+1][i]+=1
        A[i+1][j]-=1;A[j][i+1]-=1
        basis.append(A)

def matrix(g):
    L=[list(g)+[0],[0]+list(g)]
    B=[[sum(C[i][j]*L[a][j] for j in range(6))%P for a in range(2)] for i in range(6)]
    return [[sum(A[i][j]*B[j][a] for j in range(6))%P for A in basis] for a in range(2) for i in range(6)]

def det(A):
    A=[list(row) for row in A];n=len(A);d=1
    for j in range(n):
        k=next((i for i in range(j,n) if A[i][j]%P),None)
        if k is None:return 0
        if k!=j:A[j],A[k]=A[k],A[j];d=-d
        x=A[j][j]%P;d=d*x%P;u=pow(x,-1,P)
        for i in range(j+1,n):
            c=A[i][j]*u%P
            for t in range(j+1,n):A[i][t]=(A[i][t]-c*A[j][t])%P
            A[i][j]=0
    return d%P

def solve(A,b):
    R=[[x%P for x in row]+[y%P] for row,y in zip(A,b)];n=len(R)
    for j in range(n):
        k=next(i for i in range(j,n) if R[i][j]);R[j],R[k]=R[k],R[j]
        u=pow(R[j][j],-1,P);R[j]=[x*u%P for x in R[j]]
        for i in range(n):
            if i!=j:
                u=R[i][j];R[i]=[(x-u*y)%P for x,y in zip(R[i],R[j])]
    return [row[-1] for row in R]

def trim(a):
    a=[x%P for x in a]
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%P
    return trim(c)

def minus(a,b):return add(a,[-x for x in b])

def divide(a,b):
    a=trim(a);b=trim(b);assert b!=[0]
    q=[0]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        j=len(a)-len(b);c=a[-1]*pow(b[-1],-1,P)%P;q[j]=c
        a=minus(a,[0]*j+[c*x for x in b])
    return trim(q),a

def bezout(a,b):
    r0,r1=a,b;s0,s1=[1],[0];t0,t1=[0],[1]
    while r1!=[0]:
        q,r=divide(r0,r1);r0,r1=r1,r
        s0,s1=s1,minus(s0,mul(q,s1));t0,t1=t1,minus(t0,mul(q,t1))
    u=pow(r0[-1],-1,P)
    return trim([u*x for x in r0]),trim([u*x for x in s0]),trim([u*x for x in t0])

def verify():
    a=[1,2,3,5,7];b=[11,13,17,19,23]
    omits=[(10,11),(8,9)]
    values=[[],[]]
    for t in range(11):
        M=matrix([x*t+y for x,y in zip(a,b)])
        for k,om in enumerate(omits):values[k].append(det([row for i,row in enumerate(M) if i not in om]))
    Vand=[[pow(t,j,P) for j in range(11)] for t in range(11)]
    polys=[solve(Vand,v) for v in values]
    expected=[[19,7,14,49,29,1,73,82,13,3,6],
              [42,7,4,95,4,67,42,96,65,28,52]]
    assert polys==expected and all(p[-1] for p in polys)
    gcd,u,v=bezout(*polys);assert gcd==[1] and add(mul(u,polys[0]),mul(v,polys[1]))==[1]
    M=matrix([0,-6,11,-6,1]);explicit=[det([row for i,row in enumerate(M) if i not in om]) for om in omits]
    assert explicit==[68,56]
    return dict(all_pass=True,prime=P,inverse_integer_scale=scale,
                line_direction=a,line_offset=b,omitted_zero_based_rows=omits,
                degree_bound=10,specialized_minor_coefficients_ascending=polys,
                bezout_u=u,bezout_v=v,bezout_sum=[1],
                explicit_quartic_coefficients_ascending=[0,-6,11,-6,1],
                explicit_minor_values=explicit,
                scope="Two original homogeneous maximal minors are coprime over C, so the quartic-support quadric locus in P4 has dimension at most two. The explicit support {0,1,2,3} has no projected quadratic relation. No classification of the entire exceptional locus or global Jacobian membership is claimed.")

if __name__=='__main__':print(json.dumps(verify(),ensure_ascii=False,indent=2))
