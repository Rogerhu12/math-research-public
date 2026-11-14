"""Actual all-birth dual-Hankel norm identities, including forced-root endpoints.
Standalone SymPy rational checks; general proof is in the companion manuscript.
Also calibrates the birth-two fixed block against the entire 5x5 physical inverse.
"""
import sympy as s
from math import comb,factorial

def bc(n,k):return comb(n,k)if 0<=k<=n else 0

def dual(q,L,k,z,d):
 weights=[s.Integer(bc(q,i)*bc(L,k-i))*z**i for i in range(q+1)]
 mm=[sum(weights[i]*s.Integer(i)**j for i in range(q+1))for j in range(2*d+1)]
 DD=[s.Integer(1)]
 for r in range(1,d+2):DD.append(s.det(s.Matrix(r,r,lambda a,b:mm[a+b])))
 return DD,mm

def monic(q,L,D,j,z):
 h=L-q+2*D;lo=max(D-j,0);hi=max(D-h+j,0);d=D-lo-hi
 rr=list(range(lo,q-hi+1));roots=list(range(lo))+list(range(q-hi+1,q+1))
 ww=[s.Rational(comb(q,r),comb(L,j+r-D))*z**r*s.prod(r-i for i in roots)**2 for r in rr]
 xx=[r-lo for r in rr]
 mm=[sum(w*s.Integer(x)**k for w,x in zip(ww,xx))for k in range(2*d+1)]
 if d:
  G=s.Matrix(d,d,lambda a,b:mm[a+b]);b=s.Matrix([mm[d+a]for a in range(d)])
  cc=-G.inv()*b;norm=mm[2*d]+(b.T*cc)[0];sub=cc[d-1]-lo*d-sum(roots)
 else:norm=mm[0];sub=-sum(roots)
 return norm,s.sympify(sub)

count=0
for q,L in ((2,2),(4,4),(4,6),(5,7),(5,4)):
 for t in range(1,min(q,L)+1):
  D=q-t+1;h=q+L+1-2*t
  for z in (s.Rational(1,4),s.Integer(1),s.Integer(4)):
   C=factorial(q)**2*z**q
   for j in range(h+2):
    k=j+t-1;DD,mm=dual(q,L,k,z,t)
    an,cn=monic(q,L,D,j,z)
    assert DD[t]>0 and an==C*DD[t-1]/DD[t]
    # derivative of log Delta_t, using the finite moment derivative m'_r=m_(r+1).
    Mt=s.Matrix(t,t,lambda a,b:mm[a+b]);Mtprime=s.Matrix(t,t,lambda a,b:mm[a+b+1])
    mean=s.trace(Mt.inv()*Mtprime)
    assert cn==-s.Rational(q*(q+1),2)+t*q-mean
    if 1<=j<=h:
     bn,_=monic(q,L,D-1,j-1,z)
     assert DD[t+1]>0 and bn==C*DD[t]/DD[t+1]
    else:assert DD[t+1]==0
    count+=1
print('ALL_FORCED_ROOT_NORM_AND_SUBLEADING_IDENTITIES_PASS',count,flush=True)

# Physical fixed layer: source is 5-dimensional when relative t=2.
def basis(q,L,p):
 return [(r,b,p-r-b)for r in range(q+1)for b in (0,1)if 0<=p-r-b<=L]
def full(q,L,t,n,a,c):
 D=q-t+1;src=basis(q,L,t+n);out=basis(q,L,t)
 def coef(o,v):
  ds=[v[i]-o[i]for i in range(3)]
  if min(ds)<0 or sum(ds)!=n:return s.Integer(0)
  return a**ds[0]*c**ds[1]*bc(q-o[0],ds[0])*bc(1-o[1],ds[1])*bc(L-o[2],ds[2])
 A=s.Matrix([[coef(o,v)for v in src]for o in out])
 Wi=s.diag(*[s.Rational(1,comb(q,r)*comb(L,l))for r,b,l in src])
 E=s.Matrix([[(-1)**l*a**(q-r)*c**(1-b)*s.Rational(factorial(D)*bc(q-r,D),comb(L,l)),(-1)**l*a**(q-r)*c**(1-b)*s.Rational(factorial(D-1)*(1-b)*bc(q-r,D-1),comb(L,l))]for r,b,l in out])
 assert len(out)==2*t+1
 return E.T*(A*Wi*A.T).inv()*E

checks=0
for q,L in ((4,4),(4,5),(5,4)):
 t=2;h=q+L-3
 for a,c in ((s.Integer(2),s.Integer(3)),(s.Rational(1,2),s.Integer(2))):
  z=a*a;w=c*c;C=factorial(q)**2*z**q;avs=[];bvs=[];subs=[]
  for j in range(h+2):
   DD,mm=dual(q,L,j+1,z,2)
   avs.append(C*DD[1]/DD[2])
   Mt=s.Matrix(2,2,lambda aa,bb:mm[aa+bb]);Mtprime=s.Matrix(2,2,lambda aa,bb:mm[aa+bb+1])
   subs.append(-s.Rational(q*(q+1),2)+2*q-s.trace(Mt.inv()*Mtprime))
   if 1<=j<=h:bvs.append(C*DD[2]/DD[3])
  for n in range(h+1):
   AA=avs[n]+w*avs[n+1];kk=subs[n+1]-subs[n]
   BB=w*bvs[0]if n==0 else bvs[-1]if n==h else w*bvs[n-1]*bvs[n]/(bvs[n-1]+w*bvs[n])
   H=s.Matrix([[AA+BB*kk*kk,-BB*kk],[-BB*kk,BB]])
   assert H==full(q,L,2,n,a,c)
   checks+=1
print('BIRTH_TWO_FULL_FIVE_DIMENSIONAL_INVERSE_PASS',checks,flush=True)
z=s.symbols('z');DD,_=dual(4,4,2,z,2)
assert s.expand(DD[2]-48*z*(2+3*z+2*z*z))==0
assert s.discriminant(2+3*z+2*z*z,z)==-7
print('ACTUAL_NONREAL_ROOT_OBSTRUCTION_PASS',flush=True)
print('ALL_PASS',flush=True)
