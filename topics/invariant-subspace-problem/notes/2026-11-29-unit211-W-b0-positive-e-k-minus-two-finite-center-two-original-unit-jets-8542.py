#!/usr/bin/env python3
"""NEW W/b0 unique finite-mu residual center, full original local jet.
q2/(4e) and R6 have an invertible Jacobian in (mu,e) at Z=-4/3,
mu=-2,e=0.  They uniquely determine (mu,e) as p-integral series in
x=Z+4/3. The first exact QQ nonzero coefficient of COMPLETE N5
must be p-unit to exclude this center; otherwise retain it.
Fixed degree 12, 120 seconds /1 GiB, self-contained. No old resultants,
no weak tangent gate, no pole jets and no numerical root selection.
"""
import hashlib,json,resource,signal,time
from flint import fmpq
START=time.perf_counter()
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
PRIME=1009;ORDER=12;CAP=44
STAT={'seriesExactCoordinateChecks':0,'implicitJetCoefficients':0,
      'pIntegralCoefficientChecks':0,'finalOriginalN5Jets':0}
def say(stage,**d):
 d.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(d,separators=(',',':')),flush=True)
def q(x):return x if isinstance(x,fmpq) else fmpq(x)
def lower(a,b):
 if a is None:return b
 if b is None:return a
 return min(a,b)
class S:
 # a dict of Laurent coefficients; known modulo x^prec.
 # prec=None is an EXACT finite Laurent polynomial.
 def __init__(self,terms=None,prec=None):
  if isinstance(terms,S):self.c=dict(terms.c);self.prec=terms.prec;return
  if terms is None:terms={}
  elif not isinstance(terms,dict):terms={} if not q(terms) else {0:q(terms)}
  self.prec=prec
  self.c={int(i):q(a) for i,a in terms.items()
          if q(a) and (prec is None or int(i)<prec)}
 def val(self):
  if self.c:return min(self.c)
  return self.prec
 def coeff(self,i):
  assert self.prec is None or i<self.prec
  return self.c.get(i,q(0))
 def __add__(self,b):
  b=S(b);p=lower(self.prec,b.prec);c=dict(self.c)
  for i,a in b.c.items():c[i]=c.get(i,q(0))+a
  return S(c,p)
 __radd__=__add__
 def __neg__(self):return S({i:-a for i,a in self.c.items()},self.prec)
 def __sub__(self,b):return self+-S(b)
 def __rsub__(self,b):return S(b)+-self
 def __mul__(self,b):
  b=S(b);va=self.val();vb=b.val()
  if va is None or vb is None:return S()
  pa=None if self.prec is None else self.prec+vb
  pb=None if b.prec is None else b.prec+va
  p=lower(pa,pb);c={}
  for i,a in self.c.items():
   for j,bb in b.c.items():
    if p is None or i+j<p:c[i+j]=c.get(i+j,q(0))+a*bb
  return S(c,p)
 __rmul__=__mul__
 def inverse(self):
  assert self.c
  v=min(self.c);lead=self.c[v]
  if len(self.c)==1 and self.prec is None:return S({-v:1/lead})
  # Exact polynomial denominators still have infinite inverses, truncated
  # at CAP. An inexact input propagates its exact known precision.
  p=CAP if self.prec is None else self.prec-2*v
  assert p>-v
  nmax=p+v
  den={i-v:a/lead for i,a in self.c.items() if i>v}
  inv=[q(1)]
  for n in range(1,nmax):
   inv.append(-sum((den[i]*inv[n-i] for i in den if i<=n),q(0)))
  return S({i-v:a/lead for i,a in enumerate(inv)},p)
 def __truediv__(self,b):return self*S(b).inverse()
 def __rtruediv__(self,b):return S(b)*self.inverse()
 def __pow__(self,n):
  assert isinstance(n,int)
  if n<0:return self.inverse()**(-n)
  ret=S(1);base=self
  while n:
   if n&1:ret=ret*base
   n//=2
   if n:base=base*base
  return ret
 def shift(self,n):
  return S({i+n:a for i,a in self.c.items()},
           None if self.prec is None else self.prec+n)
 def checked_zero_below(self,n):
  assert self.prec is None or self.prec>=n
  assert all(not a for i,a in self.c.items() if i<n)
  STAT['seriesExactCoordinateChecks']+=1
def pmod(a):
 s=str(q(a))
 if '/' in s:
  nu,de=map(int,s.split('/'))
 else:nu,de=int(s),1
 assert de%PRIME
 STAT['pIntegralCoefficientChecks']+=1
 return (nu%PRIME)*pow(de%PRIME,-1,PRIME)%PRIME
def ipcheck(v,n):
 assert v.prec is None or v.prec>n
 for i in range(min(0,min(v.c,default=0)),n+1):pmod(v.coeff(i))
def profile(v,n):
 data=[[int(i),str(v.coeff(i))] for i in range(min(0,min(v.c,default=0)),n+1)]
 raw=json.dumps(data,separators=(',',':')).encode()
 return {'knownThrough':n,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
X=S({1:q(1)})
Z=X-q(4)/3
def originals(mu,r,need_nv=False):
 u=1+r;k=-2+r*Z;Q=r*k;delta=1-Q
 # Entire regular cancellation of the common e in the weight formula.
 ell=(1+r)*(4+r*(Z*Z-2*Z))/((-2+r*Z)*(Z-2+r*Z))
 m=u-ell;M=ell*ell*delta-m*m;bc=M/(4*delta)
 # Exact original scales T0=r*t0, J=r*j, Ast=r*aa, Phi=r*ph,
 # P02=r*p02, G=r*gg, Pc=r^2*pc. Never divide an unknown zero jet r.
 t0=-2*u-ell*k;j=-2*u+ell*k;aa=4*u*k-j;ph=t0+4+k
 p02=-2+2*r*r+k*((1+3*r)*ell-u)
 cs=aa*m*m+j*delta*ell*ell
 kap=u*k*ell/aa;T=kap*mu;lam=(mu+3)/2
 A2=(mu*mu+4*mu+5)/2
 B3=(mu**3+6*mu*mu+12*mu+7)/2
 D=ell*A2-T*T;K=ell*ell*B3-3*ell*A2*T+2*T**3
 fq=(2*cs*A2+2*M*ell*k*(3-4*lam)-8*u*k*delta*ell*T*T)/4
 fr=M*K*K-4*m*m*D**3
 assert fq.val() is None or fq.val()>=0
 assert fr.val() is None or fr.val()>=0
 if not need_nv:return fq,fr
 gg=lam*p02+r*t0;pc=k*p02*(ell+T)-gg*t0
 ts=-pc/(bc*k*ph);Vs=-gg/k-pc/(k*ph);Ws=r*t0/2
 ys=(ell*Ws-u*Vs)/M
 w=lam-1-T;cval=-mu
 z1=-2*(ell*cval+2*T)*ys-2*ell*w+m*T*ts/delta
 z2=-2*gg/k-4*m*ys
 Z0=2*(ell*cval+T)*(ell*u*w+Vs*T)+2*bc*ts*T*T
 n5=2*m*D*(Z0+D*z2)+M*K*z1
 assert n5.val() is None or n5.val()>=0
 return fq,fr,n5

mu=S(-2);r=S()
# Columns ordered (mu,e); the second row has zero mu derivative.
JAC=[[-q(9)/25,q(217)/375],[q(0),-q(27)/62500]]
det=JAC[0][0]*JAC[1][1]-JAC[0][1]*JAC[1][0]
assert det==q(243)/1562500 and pmod(det)
fq,fr=originals(mu,r)
fq.checked_zero_below(1);fr.checked_zero_below(1)
for j in range(2):
 qa,ra=originals(mu+(X if j==0 else 0),r+(X if j==1 else 0))
 assert qa.coeff(1)-fq.coeff(1)==JAC[0][j]
 assert ra.coeff(1)-fr.coeff(1)==JAC[1][j]
 STAT['seriesExactCoordinateChecks']+=2
say('new_finite_center_two_original_unit_Jacobian',
 center={'Z':'-4/3','ell':'3/5','mu':'-2','lambda':'1/2','T':'-1/2'},
 parameter='x=Z+4/3',unknownOrder=['mu','e'],
 originalEquations=['q2/(4e)','complete_R6'],
 jacobian=[[str(c) for c in row] for row in JAC],
 jacobianDeterminant=str(det),jacobianMod1009=pmod(det),
 prescribedExactQQJetOrder=ORDER,
 everyOriginalEFactorCancelledBeforeSeries=True,
 noOldResultantGcdInitialIdealOrPoleJet=True)
for n in range(1,ORDER+1):
 fq,fr=originals(mu,r)
 fq.checked_zero_below(n);fr.checked_zero_below(n)
 a,b=fq.coeff(n),fr.coeff(n)
 dmu=(-JAC[1][1]*a+JAC[0][1]*b)/det
 dr=(JAC[1][0]*a-JAC[0][0]*b)/det
 pmod(dmu);pmod(dr)
 mu=mu+S({n:dmu});r=r+S({n:dr})
 STAT['implicitJetCoefficients']+=2
fq,fr,n5=originals(mu,r,True)
fq.checked_zero_below(ORDER+1);fr.checked_zero_below(ORDER+1)
ipcheck(mu,ORDER);ipcheck(r,ORDER);ipcheck(n5,ORDER)
STAT['finalOriginalN5Jets']+=1
nz=next((n for n in range(ORDER+1) if n5.coeff(n)),None)
rfirst=next((n for n in range(ORDER+1) if r.coeff(n)),None)
if nz is None:
 say('new_finite_center_complete_N5_jet_has_no_obstruction',
     throughOrder=ORDER,exactOriginalQ2R6Returned=True,
     implicitMuJet=profile(mu,ORDER),implicitEJet=profile(r,ORDER),
     completeN5Jet=profile(n5,ORDER),firstEOrder=rfirst,
     wholeCenterRetained=True,noHigherOrderRunAuthorized=True,
     statistics=STAT)
else:
 coefficient=n5.coeff(nz);residue=pmod(coefficient)
 cbytes=str(coefficient).encode()
 say('new_finite_center_complete_original_N5_first_coefficient',
     firstExactNonzeroOrder=nz,everyEarlierCoefficientExactlyQQZero=True,
     firstCoefficientMod1009=residue,firstCoefficientBytes=len(cbytes),
     firstCoefficientSHA256=hashlib.sha256(cbytes).hexdigest(),
     exactImplicitMuJet=profile(mu,ORDER),exactImplicitEJet=profile(r,ORDER),
     firstEOrder=rfirst,completeOriginalN5Jet=profile(n5,ORDER),
     originalQ2AndR6BothZeroThroughOrder=ORDER,
     unitJacobianAndEntirePIntegralLocalModel=True,
     parameterZeroWouldForcePhysicalEZero=True,
     excludesEntireNamedValuationCenter=bool(residue),
     nonunitFirstCoefficientRetainsCenter=not bool(residue),
     notBareModDNilpotenceOrQQEmptyLifting=True,statistics=STAT)
say('new_finite_center_original_local_jet_input_complete',
 fixedOrder=ORDER,onlyNamedFiniteCenter=True,
 oldUnexecutedTangentSourceNotEntered=True,
 actualOriginalN5Jets=STAT['finalOriginalN5Jets'],statistics=STAT)
