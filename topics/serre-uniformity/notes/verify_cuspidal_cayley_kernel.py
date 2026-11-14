"""Exact normalization check only; no exceptional-prime search.
Compares the trace definition and the norm-conic formula at p=41,
using one splitting coefficient field and two fixed additive frequencies.
"""
from math import isqrt
p=41
z=next(z for z in range(2,p) if pow(z,(p-1)//2,p)==p-1)
d=(p+1)//3
ell=1723
assert all(ell%r for r in range(2,isqrt(ell)+1))
assert (ell-1)%(p*(p+1))==0

def factors(n):
    a=[]
    for r in range(2,isqrt(n)+1):
        if n%r==0:
            a.append(r)
            while n%r==0:n//=r
    if n>1:a.append(n)
    return a

def mul(v,w):return ((v[0]*w[0]+z*v[1]*w[1])%p,(v[0]*w[1]+v[1]*w[0])%p)
def power(v,n):
    r=(1,0)
    while n:
        if n&1:r=mul(r,v)
        v=mul(v,v);n//=2
    return r

g=next((x,y) for x in range(p) for y in range(1,p)
       if all(power((x,y),(p*p-1)//q)!=(1,0) for q in factors(p*p-1)))
logs={};v=(1,0)
for j in range(p*p-1):logs[v]=j;v=mul(v,g)
assert len(logs)==p*p-1
cgen=next(a for a in range(2,ell) if all(pow(a,(ell-1)//q,ell)!=1 for q in factors(ell-1)))
psi=pow(cgen,(ell-1)//p,ell)
eta=pow(cgen,(ell-1)//3,ell)
zetad=pow(cgen,(ell-1)//d,ell)
ps=[pow(psi,j,ell) for j in range(p)]
H=[t for t in range(p) if logs[(t,1)]%3==0]
assert len(H)==d-1
AH=[sum(ps[t*y%p] for t in H)%ell for y in range(p)]
SC=[sum(pow(eta,logs[(t,1)]%3,ell)*ps[t*y%p] for t in range(p))%ell for y in range(p)]
SCm=[sum(pow(eta,-logs[(t,1)]%3,ell)*ps[t*y%p] for t in range(p))%ell for y in range(p)]
assert all(3*AH[y]%ell==((p if y==0 else 0)+SC[y]+SCm[y])%ell for y in range(p))

def mm(A,B):return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2))%p for i in range(2) for j in range(2))
trace_tests=0
individual_tests=0
for u in (1,3,5):
    theta={v:pow(zetad,(u*j)%d,ell) for v,j in logs.items()}
    char_ns={}
    for (x,y),vtheta in theta.items():
        if y:
            char_ns[(2*x%p,(x*x-z*y*y)%p)]=(-vtheta-theta[(x,-y%p)])%ell
    def char(M):
        if M[1]==M[2]==0 and M[0]==M[3]:return p-1
        tr=(M[0]+M[3])%p;det=(M[0]*M[3]-M[1]*M[2])%p
        dis=(tr*tr-4*det)%p
        if dis==0:return ell-1
        if pow(dis,(p-1)//2,p)==1:return 0
        return char_ns[(tr,det)]
    for a in (1,7):
        for b in range(1,p):
            D=(a*pow(b,-1,p)%p,0,0,1)
            lhs=0
            for x in range(p):
                U=(1,x,0,1)
                lhs+=ps[-a*x%p]*char(mm(U,D))
                for t in H:
                    C=(t,z,1,t)
                    lhs+=ps[-a*x%p]*pow(theta[(t,1)],-1,ell)*char(mm(mm(U,C),D))
            lhs%=ell # This is pd*C_theta(a,b).
            rhs=p*(a==b)
            for w,tw in theta.items():
                x,y=w
                if (x*x-z*y*y)%p!=a*b%p:continue
                q=(a+b-2*x)%p
                assert q==(((x-a)**2-z*y*y)*pow(a,-1,p))%p
                rhs-=tw*ps[-2*z*y%p]*AH[q]
            assert lhs==rhs%ell,(u,a,b,lhs,rhs%ell)
            trace_tests+=1
            for eps in (1,-1):
                old=SCm if eps==1 else SC
                full=0
                for xx in range(p):
                    U=(1,xx,0,1)
                    full+=ps[-a*xx%p]*char(mm(U,D))
                    for tt in range(p):
                        C=(tt,z,1,tt)
                        phi=theta[(tt,1)]*pow(eta,eps*logs[(tt,1)]%3,ell)%ell
                        full+=ps[-a*xx%p]*pow(phi,-1,ell)*char(mm(mm(U,C),D))
                expected=p*(a==b)
                for ww,tw in theta.items():
                    xx,yy=ww
                    if (xx*xx-z*yy*yy)%p==a*b%p:
                        expected-=tw*ps[-2*z*yy%p]*old[(a+b-2*xx)%p]
                assert full%ell==expected%ell,(u,a,b,eps,full%ell,expected%ell)
                individual_tests+=1
result={'p':p,'z':z,'coefficient_prime':ell,'theta_exponents':[1,3,5],
       'actual_frequencies_checked':[1,7],'merged_row_entries_verified':trace_tests,'individual_row_entries_verified':individual_tests,
       'claim':'trace formula equals norm-conic kernel; no unit/nonzero assertion'}
if __name__=='__main__':
    import json
    Path=__import__('pathlib').Path
    Path('/tmp/cuspidal_cayley_kernel_certificate.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True))
