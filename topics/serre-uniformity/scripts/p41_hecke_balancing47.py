#!/usr/bin/env python3
"""Integral Hecke balancing operators for actual T3 at level41.

Constructs the separability projector e and the inverse s of X-Y off the
Hecke diagonal.  No unevaluated Poincare transport scalar is supplied by
these linear-algebra data; the actual mixed quadratic defect is still an
input to R140.
"""
import argparse,gzip,hashlib,json
from pathlib import Path
import sympy as sp

P=47

def reduce_poly(a,f,q):
    n=len(f)-1;a=[int(v)%q for v in a]
    while len(a)>n:
        v=a.pop();shift=len(a)-n
        for j in range(n):a[shift+j]=(a[shift+j]-v*f[j])%q
    return a+[0]*(n-len(a))

def mul(a,b,f,q):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%q
    return reduce_poly(z,f,q)

def add(a,b,q):return [(x+y)%q for x,y in zip(a,b)]
def scale(a,c,q):return [(x*c)%q for x in a]

def shift_y(A,f,q):return [reduce_poly([0]+row,f,q) for row in A]

def shift_x(A,f,q):
    n=len(f)-1;last=A[-1]
    return [[((A[i-1][j] if i else 0)-f[i]*last[j])%q for j in range(n)] for i in range(n)]

def matrix_sub(A,B,q):return [[(x-y)%q for x,y in zip(a,b)] for a,b in zip(A,B)]
def diagonal(A,f,q):
    n=len(f)-1;ans=[0]*n;power=[1]+[0]*(n-1)
    for row in A:
        ans=add(ans,mul(row,power,f,q),q);power=reduce_poly([0]+power,f,q)
    return ans

def exact_t3_polynomial(full):
    x,z=sp.symbols('x z');factors=[]
    for field in full['fields']:
        f=sp.Poly.from_list(field['factor_descending'],x)
        den,co=field['directions'][1][0]
        t=sp.Poly.from_list(co,x).as_expr()/den
        g=sp.Poly(sp.resultant(f.as_expr(),z-t,x),z)
        assert g.LC()==1 and all(c.q==1 for c in g.all_coeffs())
        factors.append([int(c) for c in g.all_coeffs()])
    total=sp.Poly(sp.prod(sp.Poly.from_list(c,z).as_expr() for c in factors),z)
    assert total.degree()==54
    disc=int(sp.discriminant(sp.Poly(total,z,modulus=P)))%P
    assert disc==23
    return factors,[int(c) for c in total.all_coeffs()],disc

def build_projectors(desc,q):
    n=len(desc)-1;f=[c%q for c in desc[::-1]];one=[1]+[0]*(n-1)
    fp=reduce_poly([(i+1)*f[i+1] for i in range(n)],f,q)
    fpp=reduce_poly([(i+1)*fp[i+1] for i in range(n-1)],f,q)
    x=sp.symbols('x');poly=sp.Poly.from_list(desc,x,modulus=P)
    iv=sp.invert(poly.diff(),poly)
    a=[int(iv.nth(i))%P for i in range(n)];prec=P
    while prec<q:
        prec=min(prec*prec,q)
        a=mul(a,add(scale(mul(a,fp,f,prec),-1,prec),scale(one,2,prec),prec),f,prec)
    assert mul(a,fp,f,q)==one
    divided=[[f[i+j+1] if i+j<n else 0 for j in range(n)] for i in range(n)]
    e=[mul(row,a,f,q) for row in divided]
    zero=[[0]*n for _ in range(n)];identity=[row[:] for row in zero];identity[0][0]=1
    assert matrix_sub(shift_x(e,f,q),shift_y(e,f,q),q)==zero
    assert diagonal(e,f,q)==one
    assert e==[list(row) for row in zip(*e)]
    numerator=matrix_sub(identity,e,q);work=[row[:] for row in numerator];s0=[row[:] for row in zero]
    for k in range(n-1,0,-1):
        s0[k-1]=work[k]
        work[k-1]=add(work[k-1],reduce_poly([0]+work[k],f,q),q)
    assert work[0]==[0]*n
    correction=scale(mul(fpp,a,f,q),pow(2,-1,q),q)
    s=[add(row,mul(erow,correction,f,q),q) for row,erow in zip(s0,e)]
    assert matrix_sub(shift_x(s,f,q),shift_y(s,f,q),q)==numerator
    assert diagonal(s,f,q)==[0]*n
    assert s==[[(-v)%q for v in row] for row in zip(*s)]
    # delta*e=0 and diagonal(e)=1 imply e^2=e; diagonal(s)=0 implies e*s=0.
    return a,e,s

def pairdet(A,p):
    A=[[tuple(int(t)%p for t in v) for v in row] for row in A];n=len(A);det=(1,0)
    def pm(a,b):return ((a[0]*b[0]-a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
    def inv(a):
        v=pow((a[0]*a[0]+a[1]*a[1])%p,-1,p);return (a[0]*v%p,-a[1]*v%p)
    for j in range(n):
        k=next(i for i in range(j,n) if A[i][j]!=(0,0))
        if k!=j:A[k],A[j]=A[j],A[k];det=((-det[0])%p,(-det[1])%p)
        v=A[j][j];det=pm(det,v);iv=inv(v);A[j]=[pm(a,iv) for a in A[j]]
        for i in range(j+1,n):
            c=A[i][j]
            for k in range(j+1,n):
                z=pm(c,A[j][k]);A[i][k]=((A[i][k][0]-z[0])%p,(A[i][k][1]-z[1])%p)
            A[i][j]=(0,0)
    return list(det)

def actual_operator_check(hecke,log,desc,q):
    import numpy as np
    values=np.array(hecke['operators']['3']['canonical_operator'],dtype=np.int64)
    # T* on differentials has columns in the published basis; tangent/log action is transpose.
    T=(values[:,:,0].T%q,values[:,:,1].T%q);n=54
    def mm(A,B,mod):return ((A[0]@B[0]-A[1]@B[1])%mod,(A[0]@B[1]+A[1]@B[0])%mod)
    I=np.eye(n,dtype=np.int64);Z=np.zeros((n,n),dtype=np.int64);v=(Z.copy(),Z.copy())
    for c in desc:
        v=mm(v,T,q);v=((v[0]+(c%q)*I)%q,v[1])
    assert not np.any(v[0]) and not np.any(v[1])
    logs=np.array(log['log_of_B_divided47_mod47'],dtype=np.int64);u=(logs[:,0:1],logs[:,1:2])
    K=np.zeros((n,n,2),dtype=np.int64)
    for j in range(n):
        K[:,j,0]=u[0][:,0];K[:,j,1]=u[1][:,0];u=mm(T,u,P)
    det=pairdet(K.tolist(),P);norm=(det[0]**2+det[1]**2)%P;assert norm
    # Each complex matrix product has <=54 terms, all reduced moduloq before multiplication.
    assert 2*54*(q-1)**2<2**63
    return {'T3_tangent_transpose_of_differential_operator':True,'annihilating_polynomial_mod47_power':True,
            'normalized_logB_Krylov_determinant_mod47':det,'determinant_norm_mod47':norm,'dimension':n}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,default=Path(__file__).resolve().parent)
    ap.add_argument('--output',type=Path);ap.add_argument('--precision',type=int,default=4);args=ap.parse_args()
    assert 1<=args.precision<=4,'actual finite operator certificate is supplied to47^4'
    q=P**args.precision;root=args.script_dir/'data'
    names=['p41_full_chow_heegner_certificate.json.gz','p41_hecke47_compact.json.gz','p41_formal47_log_compact.json.gz']
    raw=[(root/name).read_bytes() for name in names];full,hecke,log=[json.loads(gzip.decompress(b)) for b in raw]
    assert full['row_metadata'][1]['n']==3
    factors,desc,disc=exact_t3_polynomial(full);a,e,s=build_projectors(desc,q)
    checked=actual_operator_check(hecke,log,desc,q)
    out={'level':41,'auxiliary_prime':P,'precision':args.precision,'modulus':q,
         'source_sha256':{name:hashlib.sha256(b).hexdigest() for name,b in zip(names,raw)},
         'T3_factors_descending':factors,'T3_polynomial_descending':desc,'T3_discriminant_mod47':disc,
         'inverse_derivative_ascending':a,'separability_projector_coefficients_XY':e,
         'off_diagonal_inverse_coefficients_XY':s,'actual_operator_checks':checked,
         'identities':['(X-Y)e=0','mu(e)=1','e^2=e','(X-Y)s=1-e','mu(s)=0','es=0','e(Y,X)=e(X,Y)','s(Y,X)=-s(X,Y)'],
         'status':'Exact universal balancing operators only. The actual Poincare mixed quadratic transport scalar remains an input; no auxiliary height or QC root is claimed.'}
    packed=gzip.compress((json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0)
    target=args.output or root/'p41_hecke_balancing47_certificate.json.gz';target.write_bytes(packed)
    print('Actual T3 polynomial, etaleness and cyclic log PASS:',checked,flush=True)
    print('Integral separability projector and off-diagonal inverse identities PASS.',flush=True)
    print(target,len(packed),'SHA256',hashlib.sha256(packed).hexdigest(),flush=True)
if __name__=='__main__':main()
