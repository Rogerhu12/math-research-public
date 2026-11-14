#!/usr/bin/env python3
"""Exact standard-library certificate for R182 at one fixed (p,ell).

No floating point, prime window, class-number tables, or PARI dependency.
The field is F_1409[x]/(x^2+724*x+1), with x of order 141.
"""
import argparse
import hashlib
import json
from pathlib import Path

P = 47
ELL = 1409
C = 724

def prime(n):
    return n >= 2 and all(n % d for d in range(2, __import__('math').isqrt(n)+1))

def add(x, y):
    a,b = x % ELL, x // ELL
    c,d = y % ELL, y // ELL
    return (a+c) % ELL + ELL*((b+d) % ELL)

def neg(x):
    return (-x % ELL) + ELL*(-(x//ELL) % ELL)

def sub(x,y):
    return add(x,neg(y))

def mul(x,y):
    a,b = x % ELL, x // ELL
    c,d = y % ELL, y // ELL
    bd = b*d
    return (a*c-bd) % ELL + ELL*((a*d+b*c-C*bd) % ELL)

def power(x,n):
    if n < 0:
        return power(power(x,ELL*ELL-2),-n)
    ans = 1
    while n:
        if n&1:
            ans = mul(ans,x)
        x = mul(x,x)
        n >>= 1
    return ans

def inv(x):
    assert x
    return power(x,ELL*ELL-2)

def scalar(n):
    return n % ELL

def mat_zero(n=P,m=P):
    return [[0]*m for _ in range(n)]

def identity(n=P):
    a = mat_zero(n,n)
    for j in range(n): a[j][j] = 1
    return a

def mat_mul(a,b):
    n,k,m = len(a),len(b),len(b[0])
    assert len(a[0]) == k
    out = mat_zero(n,m)
    for i in range(n):
        for j in range(k):
            c = a[i][j]
            if not c: continue
            for t in range(m):
                if b[j][t]: out[i][t] = add(out[i][t],mul(c,b[j][t]))
    return out

def mat_add(a,b,sign=1):
    op = add if sign==1 else sub
    return [[op(x,y) for x,y in zip(ar,br)] for ar,br in zip(a,b)]

def scale(a,s):
    return [[mul(s,x) for x in row] for row in a]

def transpose(a): return [list(row) for row in zip(*a)]

def rref(a):
    a=[row[:] for row in a]
    n,m=len(a),len(a[0]); piv=[]; row=0
    for col in range(m):
        pivot=next((j for j in range(row,n) if a[j][col]),None)
        if pivot is None: continue
        a[row],a[pivot]=a[pivot],a[row]
        u=inv(a[row][col]); a[row]=[mul(u,x) for x in a[row]]
        for j in range(n):
            if j!=row and a[j][col]:
                u=a[j][col]
                a[j]=[sub(x,mul(u,y)) for x,y in zip(a[j],a[row])]
        piv.append(col);row+=1
        if row==n:break
    return a,piv

def rank(a): return len(rref(a)[1])

def basis_image(a):
    _,cols=rref(a)
    return [[row[c] for c in cols] for row in a]

def null_vector(a):
    rr,piv=rref(a);m=len(a[0])
    free=next(c for c in range(m) if c not in piv)
    v=[0]*m;v[free]=1
    for j,c in enumerate(piv):v[c]=neg(rr[j][free])
    assert all(x==0 for row in mat_mul(a,[[x] for x in v]) for x in row)
    return v

def fp2mul(u,v):
    x,y=u;s,t=v
    return ((x*s-y*t)%P,(x*t+y*s)%P)

def fp2pow(u,n):
    v=(1,0)
    while n:
        if n&1:v=fp2mul(v,u)
        u=fp2mul(u,u);n>>=1
    return v

def cartan_parameter(v):
    if v==(1,0):return None
    x,y=v
    # t=i(1+v)/(1-v), with norm(v)=1.
    num=fp2mul((0,1),((1+x)%P,y))
    den=((1-x)%P,(-y)%P)
    ni=pow((den[0]*den[0]+den[1]*den[1])%P,-1,P)
    ti=fp2mul(num,(den[0]*ni%P,-den[1]*ni%P))
    assert ti[1]==0
    return ti[0]

XI=ELL
PSI=power(XI,3)
BETA=power(XI,47)
PSIP=[power(PSI,j) for j in range(P)]

def D(v):
    x,y=v
    out=mat_zero()
    for j in range(P):
        out[(j+x)%P][j]=PSIP[(2*x*y+4*y*j)%P]
    return out

def K(v):
    t=cartan_parameter(v)
    if t is None:return identity()
    out=mat_zero();ip=scalar(-pow(P,-1,ELL))
    for x in range(P):
        for y in range(P):
            norm=(x*x+y*y)%P
            for j in range(P):
                exponent=(t*norm+2*x*y+4*y*j)%P
                out[(j+x)%P][j]=add(out[(j+x)%P][j],mul(ip,PSIP[exponent]))
    return out

def projector(v,order,ch):
    # Direct Weyl coefficients, independent of any eigenvector choice.
    coeff=[0]*P
    identity_coefficient=0
    ip=scalar(-pow(P,-1,ELL))
    for j in range(order):
        vv=fp2pow(v,j); t=cartan_parameter(vv)
        w=power(ch,-j)
        if t is None:
            identity_coefficient=add(identity_coefficient,w)
        else:
            for n in range(P):coeff[n]=add(coeff[n],mul(mul(ip,w),PSIP[t*n%P]))
    io=scalar(pow(order,-1,ELL))
    coeff=[mul(io,x) for x in coeff]
    out=scale(identity(),mul(io,identity_coefficient))
    for x in range(P):
        for y in range(P):
            c=coeff[(x*x+y*y)%P]
            if not c:continue
            for j in range(P):
                out[(j+x)%P][j]=add(out[(j+x)%P][j],mul(c,PSIP[(2*x*y+4*y*j)%P]))
    return out

def matrix_digest(a):
    return hashlib.sha256(json.dumps(a,separators=(',',':')).encode()).hexdigest()

def main():
    assert prime(P) and prime(ELL)
    assert ELL%P==P-1 and P*(P*P-1)%ELL
    assert pow((C*C-4)%ELL,(ELL-1)//2,ELL)==ELL-1
    assert add(add(mul(XI,XI),mul(scalar(C),XI)),1)==0
    assert power(XI,141)==1 and power(XI,47)!=1 and power(XI,3)!=1
    nu=(6,24)
    assert fp2pow(nu,12)==(1,0) and fp2pow(nu,6)==(46,0)
    q0=mat_zero();q1=mat_zero()
    for j in range(12):
        if j%2:q1=mat_add(q1,D(fp2pow(nu,j)))
        else:q0=mat_add(q0,D(fp2pow(nu,j)))
    rr=mat_add(q0,q1,-1)
    assert rr==transpose(rr)
    kh=K(nu)
    assert mat_add(mat_mul(kh,rr),mat_mul(rr,kh))==mat_zero()
    result={"p":P,"ell":ELL,"field_polynomial":[1,C,1],"xi_order":141,"nu":list(nu)}
    data={}
    for label,chi in [("beta",BETA),("minus_beta",neg(BETA)),("beta2",power(BETA,2)),("minus_beta2",neg(power(BETA,2)))]:
        pr=projector(nu,12,chi)
        assert mat_mul(pr,pr)==pr
        assert mat_mul(kh,pr)==scale(pr,chi)
        ui=basis_image(pr)
        ru=mat_mul(rr,ui)
        entry={"projector_rank":len(ui[0]),"image_rank_under_R":rank(ru),"projector_sha256":matrix_digest(pr)}
        if entry['image_rank_under_R']<entry['projector_rank']:
            kv=null_vector(ru)
            w=mat_mul(ui,[[x] for x in kv])
            assert mat_mul(rr,w)==mat_zero(P,1)
            entry['kernel_vector']=[row[0] for row in w]
        data[label]=entry
    # An explicit generator in this same C, aligned so h=g^(m/2)=g^4.
    gen=(37,29)
    assert (gen[0]*gen[0]+gen[1]*gen[1])%P==1
    assert fp2pow(gen,24)!=(1,0) and fp2pow(gen,16)!=(1,0)
    assert fp2pow(gen,4)==nu
    hh=fp2pow(gen,3)
    ph=projector(hh,16,1)
    assert mat_mul(ph,ph)==ph and rank(ph)==2
    assert ph==transpose(ph)
    phr=mat_mul(ph,rr)
    result['C_generator']=list(gen)
    result['P_H_rank']=rank(ph)
    result['P_H_R_rank']=rank(phr)
    result['P_H_R_sha256']=matrix_digest(phr)
    for label,entry in data.items():
        if 'kernel_vector' not in entry:continue
        w=[[x] for x in entry['kernel_vector']]
        phw=mat_mul(ph,w)
        entry['P_H_of_kernel_is_zero']=phw==mat_zero(P,1)
        entry['kernel_is_H_fixed']=phw==w
    result['blocks']=data
    ap=argparse.ArgumentParser()
    ap.add_argument('--check',action='store_true')
    ap.add_argument('--certificate',type=Path,
                    default=Path(__file__).resolve().parent/'data'/'r182_mobius_order12_block_certificate.json')
    args=ap.parse_args()
    out=args.certificate
    if args.check:
        assert json.loads(out.read_text())==result
        print('PASS: exact R182 order-12 blocks and actual H row distinction')
    else:
        out.write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({k:v for k,v in result.items() if k!='blocks'},indent=2))
        print({k:{a:b for a,b in v.items() if a!='kernel_vector'} for k,v in data.items()})

if __name__=='__main__':main()
