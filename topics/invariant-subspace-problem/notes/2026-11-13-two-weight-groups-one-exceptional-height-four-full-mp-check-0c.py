import sympy as sp,json
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


xz=sp.Symbol('z');th=lambda f:sp.expand(xz*sp.diff(f,xz));var=lambda f:sp.expand(f*th(th(f))-th(f)**2)
h3=lambda f:sp.det(sp.Matrix([[sum(int(f.expand().coeff(xz,r))*(r**(i+j))*xz**r for r in range(sp.degree(f,xz)+1)) for j in range(3)] for i in range(3)]))
BTERMS=[{'i': 0, 'den': 'q', 'terms': [[[3, 0, 1, 1, 0, 1, 0, 0, 0], 1], [[2, 2, 0, 1, 0, 1, 0, 0, 0], -1], [[1, 1, 1, 0, 2, 0, 0, 0, 0], -1], [[0, 3, 0, 0, 2, 0, 0, 0, 0], 1]]}, {'i': 1, 'den': 'q*r', 'terms': [[[3, 1, 1, 1, 0, 0, 1, 0, 0], 1], [[2, 3, 0, 1, 0, 0, 1, 0, 0], -1], [[2, 1, 2, 1, 0, 1, 0, 0, 0], 1], [[2, 0, 2, 0, 1, 1, 0, 0, 0], -1], [[1, 2, 1, 0, 1, 1, 0, 0, 0], 1], [[1, 0, 1, 0, 0, 1, 0, 2, 0], -1], [[0, 2, 2, 0, 2, 0, 0, 0, 0], -1], [[0, 1, 0, 1, 0, 0, 0, 0, 2], -1], [[0, 0, 1, 0, 1, 0, 0, 1, 1], -2]]}, {'i': 2, 'den': 'p*q**2*r', 'terms': [[[4, 0, 2, 0, 0, 2, 0, 0, 0], -1], [[3, 3, 1, 1, 0, 0, 1, 0, 0], 1], [[3, 2, 1, 0, 1, 0, 1, 0, 0], 1], [[3, 2, 1, 0, 0, 2, 0, 0, 0], 1], [[2, 4, 0, 0, 1, 0, 1, 0, 0], -1], [[2, 3, 2, 1, 0, 1, 0, 0, 0], 1], [[2, 2, 2, 0, 1, 1, 0, 0, 0], -1], [[2, 2, 0, 0, 0, 0, 1, 2, 0], -1], [[2, 0, 2, 0, 0, 1, 0, 2, 0], -1], [[2, 0, 1, 0, 0, 1, 0, 1, 1], -2], [[0, 4, 2, 0, 2, 0, 0, 0, 0], -1], [[0, 2, 1, 0, 1, 0, 0, 1, 1], -2], [[0, 2, 0, 0, 1, 0, 0, 0, 2], -1], [[0, 0, 0, 0, 0, 0, 0, 2, 2], -1]]}, {'i': 3, 'den': 'q', 'terms': [[[2, 0, 1, 0, 0, 2, 0, 0, 0], -1], [[1, 3, 0, 1, 0, 0, 1, 0, 0], 1], [[1, 2, 0, 0, 1, 0, 1, 0, 0], 1], [[1, 0, 0, 0, 0, 0, 1, 2, 0], -1], [[0, 2, 1, 0, 1, 1, 0, 0, 0], -1], [[0, 0, 0, 0, 0, 1, 0, 1, 1], -2]]}, {'i': 4, 'den': '1', 'terms': [[[1, 0, 1, 0, 0, 2, 0, 0, 0], -1], [[0, 2, 0, 0, 1, 0, 1, 0, 0], 1]]}]
CTERMS=[{'i': 0, 'den': 'r', 'terms': [[[1, 1, 1, 1, 0, 2, 0, 0, 0, 0], -1], [[1, 0, 3, 0, 0, 2, 0, 0, 0, 0], 1], [[0, 3, 0, 1, 1, 0, 1, 0, 0, 0], 1], [[0, 2, 2, 0, 1, 0, 1, 0, 0, 0], -1]]}, {'i': 1, 'den': 'p*r*t', 'terms': [[[2, 2, 0, 2, 0, 1, 1, 0, 0, 0], -1], [[2, 1, 2, 1, 0, 1, 1, 0, 0, 0], 1], [[2, 0, 2, 2, 0, 2, 0, 0, 0, 0], -1], [[1, 3, 1, 1, 1, 0, 0, 1, 0, 0], 1], [[1, 2, 3, 0, 1, 0, 0, 1, 0, 0], -1], [[1, 2, 1, 2, 1, 0, 1, 0, 0, 0], 1], [[1, 1, 3, 1, 0, 2, 0, 0, 0, 0], 1], [[1, 0, 1, 0, 1, 0, 0, 0, 0, 2], -1], [[1, 0, 0, 1, 0, 1, 0, 0, 1, 1], -2], [[0, 3, 2, 1, 1, 0, 1, 0, 0, 0], -1], [[0, 1, 0, 1, 0, 0, 1, 0, 2, 0], -1]]}, {'i': 2, 'den': 'p*q*r**2*t', 'terms': [[[2, 4, 0, 2, 0, 0, 2, 0, 0, 0], -1], [[2, 3, 2, 1, 0, 1, 0, 1, 0, 0], 1], [[2, 3, 2, 1, 0, 0, 2, 0, 0, 0], 1], [[2, 2, 4, 0, 0, 1, 0, 1, 0, 0], -1], [[2, 2, 2, 2, 0, 1, 1, 0, 0, 0], -1], [[2, 0, 4, 2, 0, 2, 0, 0, 0, 0], -1], [[2, 0, 2, 0, 0, 1, 0, 0, 0, 2], -1], [[1, 3, 3, 1, 1, 0, 0, 1, 0, 0], 1], [[1, 3, 3, 1, 0, 1, 1, 0, 0, 0], 1], [[1, 2, 3, 2, 1, 0, 1, 0, 0, 0], 1], [[1, 2, 3, 2, 0, 2, 0, 0, 0, 0], 1], [[1, 2, 0, 1, 0, 0, 1, 0, 1, 1], -2], [[1, 0, 2, 1, 0, 1, 0, 0, 1, 1], -2], [[0, 4, 4, 0, 1, 0, 0, 1, 0, 0], -1], [[0, 4, 2, 2, 1, 0, 1, 0, 0, 0], -1], [[0, 2, 2, 0, 1, 0, 0, 0, 0, 2], -1], [[0, 2, 2, 0, 0, 0, 0, 1, 2, 0], -1], [[0, 2, 0, 2, 0, 0, 1, 0, 2, 0], -1], [[0, 0, 0, 0, 0, 0, 0, 0, 2, 2], -1]]}, {'i': 3, 'den': 'p*r*t', 'terms': [[[2, 2, 0, 2, 0, 0, 2, 0, 0, 0], -1], [[2, 1, 2, 1, 0, 1, 0, 1, 0, 0], 1], [[2, 0, 2, 2, 0, 1, 1, 0, 0, 0], -1], [[1, 3, 1, 1, 0, 0, 2, 0, 0, 0], 1], [[1, 2, 3, 0, 0, 1, 0, 1, 0, 0], -1], [[1, 2, 1, 2, 0, 1, 1, 0, 0, 0], 1], [[1, 1, 3, 1, 1, 0, 0, 1, 0, 0], 1], [[1, 0, 1, 0, 0, 1, 0, 0, 0, 2], -1], [[1, 0, 0, 1, 0, 0, 1, 0, 1, 1], -2], [[0, 3, 2, 1, 1, 0, 0, 1, 0, 0], -1], [[0, 1, 0, 1, 0, 0, 0, 1, 2, 0], -1]]}, {'i': 4, 'den': 'r', 'terms': [[[1, 1, 1, 1, 0, 0, 2, 0, 0, 0], -1], [[1, 0, 3, 0, 0, 1, 0, 1, 0, 0], 1], [[0, 3, 0, 1, 0, 0, 2, 0, 0, 0], 1], [[0, 2, 2, 0, 0, 1, 0, 1, 0, 0], -1]]}]
def evterms(row,values):return sum(sp.Integer(c)*sp.prod(v**e for v,e in zip(values,exps)) for exps,c in row['terms'])
count=0
for delta in [0,1]:
 for m in ([1,2,3] if delta==0 else [2,3,4]):
  Q=m+1;L=m+3-2*delta;t=m-delta;W=sum(xz**r for r in range(m+1));weight=sp.Integer(Q*(Q+1)*(Q+2) if delta==0 else Q)
  if delta==0:
   ph=[sum(sp.prod(list(range(r+1,r+j+1))+list(range(Q-r,Q+3-j-r)))*xz**r for r in range(m+1)) for j in range(4)]
   av=[sum(r*sp.prod(Q+k-r for k in range(4))*xz**r for r in range(m+1))]+[var(f)/f for f in ph]
   bv=ph;sub=[0]+[-th(f)/f for f in ph]
  else:
   F0=sum((Q-r)*xz**r for r in range(m+1));F1=sum((r+1)*xz**r for r in range(m+1));T0=var(F0);T1=var(F1)
   V=sum(r*(Q-r)*(Q+1-r)*xz**r for r in range(m+1));R=sum((m-r)*(r+1)*(r+2)*xz**r for r in range(m+1))
   A0=sum(r*(r-1)*(Q-r)*(Q+1-r)*(Q+2-r)*xz**r for r in range(m+1))
   av=[A0,var(V)/V,h3(F0)/T0,h3(F1)/T1,var(R)/R];bv=[V,T0/F0,T1/F1,R]
   sub=[-1,-th(V)/V,-th(T0)/T0,-th(T1)/T1,-m-th(R)/R]
  av=[sp.sympify(v).subs(xz,4) for v in av];bv=[sp.sympify(v).subs(xz,4) for v in bv];sub=[sp.sympify(v).subs(xz,4) for v in sub]
  for n in [1,2]:
   a,b,c,d=av[n-1:n+3];kx=sub[n]-sub[n-1]-(sub[n+1]-sub[n]);ky=sub[n+2]-sub[n+1]-(sub[n+1]-sub[n]);w=sp.Integer(9)
   if n==1:
    p,q,r=bv[:3];A=a;T_0=b*p;T_1=c*q;T_2=d*r;X=kx*p*q;Y=ky*p*q*r
    vals=[p,q,r,A,T_0,T_1,T_2,X,Y];dens=[q,q*r,p*q*q*r,q,1]
    P=sum(evterms(row,vals)/dens[i]*w**i for i,row in enumerate(BTERMS));pred=w*P/((p+w*q)**2*(c+w*d)*r)
   else:
    p,q,r,tt=bv;vals=[p,q,r,tt,a*p,b*q,c*r,d*tt,kx*p*q*r,ky*q*r*tt];dens=[r,p*r*tt,p*q*r*r*tt,p*r*tt,r]
    P=sum(evterms(row,vals)/dens[i]*w**i for i,row in enumerate(CTERMS));pred=w*P/((p+w*q)*(q+w*r)**2*(c+w*d)*tt)
   actual=[weight*full(m,L,t,j,sp.Integer(2),sp.Integer(3)) for j in [n-1,n,n+1]]
   K=actual[0]-actual[1]*actual[2].inv()*actual[1]
   assert sp.cancel(K.det()-pred)==0,(delta,m,n,K.det(),pred)
   count+=1
print('PASS independent full physical MP determinant and both generic quartics:',count)
