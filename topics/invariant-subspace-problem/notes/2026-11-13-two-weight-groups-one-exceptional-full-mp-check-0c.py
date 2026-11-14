import sympy as s
from math import comb,factorial

def basis(q,L,p):
 return [(r,k,p-r-k) for r in range(q+1) for k in [0,1] if 0<=p-r-k<=L]

def full(q,L,t,n,a,c):
 de=q-t;src=basis(q,L,t+n);out=basis(q,L,t)
 def coeff(o,v):
  ds=[v[i]-o[i] for i in range(3)]
  if min(ds)<0 or sum(ds)!=n:return s.S.Zero
  return a**ds[0]*c**ds[1]*comb(q-o[0],ds[0])*comb(1-o[1],ds[1])*comb(L-o[2],ds[2])
 A=s.Matrix([[coeff(o,v) for v in src] for o in out])
 Wi=s.diag(*[s.Rational(1,comb(q,r)*comb(L,l)) for r,k,l in src])
 G=s.Matrix([[(-1)**l*a**(q-r)*c**(1-k)*s.Rational(factorial(de+1)*comb(q-r,de+1),comb(L,l)),(-1)**l*a**(q-r)*c**(1-k)*s.Rational(factorial(de)*(1-k)*comb(q-r,de),comb(L,l))] for r,k,l in out])
 return G.T*(A*Wi*A.T).inv()*G

def monic(q,L,d,j,z):
 h=L-q+2*d;u=max(d-j,0);v=max(d-h+j,0);k=d-u-v
 rr=list(range(u,q-v+1))
 ff=[s.prod(r-i for i in range(u))*s.prod(r-q+i for i in range(v)) for r in rr]
 ww=[s.Rational(comb(q,r),comb(L,j+r-d))*z**r*f*f for r,f in zip(rr,ff)]
 xx=[r-u for r in rr]
 mm=[sum(w*x**l for w,x in zip(ww,xx)) for l in range(2*k+1)]
 if k:
  J=s.Matrix(k,k,lambda i,j:mm[i+j]);b=s.Matrix([mm[k+i]for i in range(k)])
  coeff=-J.inv()*b
  norm=mm[2*k]+(b.T*coeff)[0]
  sub=coeff[k-1]
 else:norm=mm[0];sub=0
 sub=sub-u*k-s.Rational(u*(u-1),2)-s.Rational(v*(2*q-v+1),2)
 return norm,sub

count=0
for q in range(1,5):
 for L in range(q,q+4):
  for t in range(1,q+1):
   h=q+L+1-2*t
   if h<2:continue
   de=q-t
   for a,c in [(s.Rational(2),s.Rational(3)),(s.Rational(1,2),s.Rational(2))]:
    z=a*a;w=c*c
    av=[monic(q,L,de+1,j,z) for j in range(h+2)]
    bv=[monic(q,L,de,j,z)[0] for j in range(h)]
    for n in range(h+1):
     aa=av[n][0]+w*av[n+1][0];dd=av[n+1][1]-av[n][1]
     bb=w*bv[0] if n==0 else bv[h-1] if n==h else w*bv[n-1]*bv[n]/(bv[n-1]+w*bv[n])
     H=s.Matrix([[aa+bb*dd*dd,-bb*dd],[-bb*dd,bb]])
     actual=full(q,L,t,n,a,c)
     assert H==actual,(q,L,t,n,a,c,H,actual)
     count+=1
print('PASS full three-chain MP equals all-height 2x2 shear:',count)
