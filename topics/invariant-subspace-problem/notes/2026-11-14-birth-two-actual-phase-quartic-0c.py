"""Actual same-source birth-two canonical quartic from the original Z phase.
No claim of general interior coefficient positivity. Pure rational identities;
SymPy is used to calibrate against the entire five-dimensional physical inverse.
"""
import sympy as s
from math import comb,factorial

def base_phase(M,N,u,eta,tau):
 alpha=N-1-u*eta;beta=M-1-eta
 J=u*(M+1+eta)-N+1;K=N+1-u*beta
 R=N/(M*u)-(N-1)*J*tau/(M*u*alpha)
 T=M*u/N-(M-1)*K/(N*beta*tau)
 return dict(M=M,N=N,u=u,eta=eta,tau=tau,alpha=alpha,beta=beta,J=J,K=K,R=R,T=T)
def curv_pair(M,N,u,eta,tau):
 q=base_phase(M,N,u,eta,tau);H=M+N
 f0=(q['J']*(N+(N-1)*tau)-2*u*(H-1))/(eta*u)
 f1=(q['K']*(M-1+M*tau)-2*(H-1)*tau)/(eta*tau)
 return f0,f1

def canonical_birth_two(M,N,u,eta,tau,simplify=False):
 # Physical comparison n=N-2, m=M-2, ordinary coefficient k=n+1.
 can=s.cancel if simplify else lambda v:v
 q=base_phase(M,N,u,eta,tau);alpha,beta,R,T=[q[k]for k in ('alpha','beta','R','T')]
 minus=(M+1,N-1,u*(N-1)*R/alpha,u*eta*M/(N-1),(N-1)*tau/(alpha*R))
 plus=(M-1,N+1,u*beta/((M-1)*T),eta*N*T/(u*beta),beta*T*tau/(M-1))
 fm=can(M*u/(N-1)*curv_pair(*minus)[0])
 f0,f1=map(can,curv_pair(M,N,u,eta,tau))
 fp=can(N*T/(u*beta)*curv_pair(*plus)[1])
 aa=tuple(map(can,(1/(u*R),s.Integer(1),u,u*u/T)))
 bb=tuple(map(can,(f0/(u*R*fm),s.Integer(1),u*f0/f1,u*u*f0/(T*fp))))
 chi=can(eta*f0/(u*tau));n=N-2
 dx=can((1/bb[0]-u)/n);dy=can((aa[3]/bb[2]-u)/(n+1))
 xx=can(chi*dx*dx);yy=can(chi*dy*dy);xy=can(chi*dx*dy)
 return dict(base=q,minus=minus,plus=plus,phi=(fm,f0,f1,fp),high=aa,low=bb,chi=chi,dx=dx,dy=dy,x2=xx,y2=yy,xy=xy,
             R2=can(R*fm*f1/f0**2),T2=can(T*f0*fp/f1**2))

def quartic_coefficients(data,simplify=False):
 a,b,c,d=data['high'];p,Q,r,ss=data['low'];xx,yy,xy=[data[k]for k in ('x2','y2','xy')]
 la=[a*c-b*b,a*d-b*c,b*d-c*c]
 ff=[p*Q*(Q*ss-r*r),Q*r*(p*ss-Q*r),r*ss*(p*r-Q*Q)]
 co=[sum(Q*la[i]*ff[k-i]for i in range(3)if 0<=k-i<3)for k in range(5)]
 for fac,U,V in ((p*Q**3*r*xx,(c,d),(r,ss)),(Q*Q*r*r*ss*yy,(a,b),(p,Q)),(2*p*Q*Q*r*ss*xy,(b,c),(Q,r))):
  for i in range(2):
   for j in range(2):co[i+j+1]-=fac*U[i]*V[j]
 co[2]-=p*Q**3*r*r*ss*xx*yy
 return [s.cancel(v)for v in co]if simplify else co

def actual_data(q,L,k,z):
 nodes=range(max(0,k-L),min(q,k)+1)
 nu=[(i,s.Integer(comb(q,i)*comb(L,k-i))*z**i)for i in nodes]
 mm=[sum(w*s.Integer(i)**a for i,w in nu)for a in range(5)]
 Z=mm[0];mu=mm[1]/Z;var=mm[2]/Z-mu*mu
 G2=s.Matrix(2,2,lambda a,b:mm[a+b]);G3=s.Matrix(3,3,lambda a,b:mm[a+b]);D2=G2.det();D3=G3.det()
 curv=Z*D3/D2**2
 fprime=s.trace(G2.inv()*s.Matrix(2,2,lambda a,b:mm[a+b+1]))
 return dict(Z=Z,mu=mu,var=var,curv=curv,fprime=fprime)

def actual_phase(q,L,k,z):
 M=s.Integer(q+L-k);N=s.Integer(k+1)
 d0=actual_data(q,L,k,z);d1=actual_data(q,L,k+1,z)
 p=(q-d0['mu'])/M;r=d1['mu']/N;A=p*(1-p);B=r*(1-r)
 th=d1['var']/(N*B);u=A*(1-th)/(B*th);eta=(r-p)**2*th/A;tau=th/(1-th)
 return (M,N,u,eta,tau),dict(p=p,r=r,theta=th,g=B*th,c=(1-r)/(1-p),d=r-p)

if __name__=='__main__':
 def bc(n,k):return comb(n,k)if 0<=k<=n else 0
 def full(q,L,n,a,c):
  t=2;D=q-1
  def bs(p):return [(r,b,p-r-b)for r in range(q+1)for b in (0,1)if 0<=p-r-b<=L]
  src=bs(t+n);out=bs(t)
  def coef(o,v):
   ds=[v[i]-o[i]for i in range(3)]
   if min(ds)<0 or sum(ds)!=n:return s.Integer(0)
   return a**ds[0]*c**ds[1]*bc(q-o[0],ds[0])*bc(1-o[1],ds[1])*bc(L-o[2],ds[2])
  A=s.Matrix([[coef(o,v)for v in src]for o in out]);Wi=s.diag(*[s.Rational(1,comb(q,r)*comb(L,l))for r,b,l in src])
  E=s.Matrix([[(-1)**l*a**(q-r)*c**(1-b)*s.Rational(factorial(D)*bc(q-r,D),comb(L,l)),(-1)**l*a**(q-r)*c**(1-b)*s.Rational(factorial(D-1)*(1-b)*bc(q-r,D-1),comb(L,l))]for r,b,l in out])
  assert len(out)==5
  return E.T*(A*Wi*A.T).inv()*E
 for q,L,n,a,c0 in ((4,4,2,s.Integer(2),s.Integer(3)),(4,6,3,s.Integer(2),s.Integer(2)),(5,7,4,s.Integer(2),s.Integer(3)),(6,4,3,s.Integer(2),s.Integer(3))):
  z=a*a;w=c0*c0;k=n+1
  params,info=actual_phase(q,L,k,z);data=canonical_birth_two(*params,simplify=True)
  M,N,u,eta,tau=params;g=info['g'];cg=info['c'];actual=[actual_data(q,L,k+i,z)for i in (-1,0,1,2)]
  assert all(s.cancel(phi-dd['curv']/g)==0 for phi,dd in zip(data['phi'],actual))
  minus,_=actual_phase(q,L,k-1,z);plus,_=actual_phase(q,L,k+1,z)
  assert all(s.cancel(x-y)==0 for x,y in zip(minus,data['minus']))
  assert all(s.cancel(x-y)==0 for x,y in zip(plus,data['plus']))
  Cq=s.Integer(factorial(q)**2)*z**q;Ck=actual[1]['Z']*actual[1]['var'];gam2=actual[1]['curv'];gamma=s.sqrt(gam2)
  assert s.cancel((z-1)**2*cg**2*gam2-data['chi'])==0
  for jj,aa,bb,dd in zip(range(n-1,n+3),data['high'],data['low'],actual):
   fac=Ck/Cq*cg**(k-jj-1)
   assert s.cancel(aa-fac*Cq/(dd['Z']*dd['var']))==0
   assert s.cancel(bb-fac*gam2*Cq/(dd['Z']*dd['var']*dd['curv']))==0
  assert 0<data['R2']<1 and 0<data['T2']<1
  omega=cg*w;a1,b1,c1,d1=data['high'];p1,Q1,r1,s1=data['low']
  xc=(z-1)*cg*gamma*data['dx'];yc=(z-1)*cg*gamma*data['dy']
  Bm=omega*p1/(p1+omega);B0=omega*r1/(1+omega*r1);Bp=omega*r1*s1/(r1+omega*s1)
  canon=[s.Matrix([[a1+omega*b1+Bm*xc**2,-Bm*xc],[-Bm*xc,Bm]]),s.diag(b1+omega*c1,B0),s.Matrix([[c1+omega*d1+Bp*yc**2,-Bp*yc],[-Bp*yc,Bp]])]
  center=actual[1]['fprime']-actual[2]['fprime']
  common=s.Matrix([[1,0],[center,gamma]])
  for jj,Hcan in zip((n-1,n,n+1),canon):
   fac=Ck/Cq*cg**(k-jj-1);HH=fac*common.T*full(q,L,jj,a,c0)*common
   assert all(s.simplify(v)==0 for v in HH-Hcan)
  Kmat=canon[0]-canon[1]*canon[2].inv()*canon[1]
  coef=quartic_coefficients(data,simplify=True)
  denom=(p1+omega)*(1+omega*r1)**2*(c1+omega*d1)*s1/omega
  assert s.simplify(sum(coef[i]*omega**i for i in range(5))-Kmat.det()*denom)==0
  print('ACTUAL_ALL_FOUR_NORMS_PHASE_STEPS_AND_FULL_FIVE_DIMENSIONAL_TRIPLE_PASS',q,L,n,z,w,flush=True)
 print('ALL_PASS: identities only; no general positivity asserted',flush=True)
