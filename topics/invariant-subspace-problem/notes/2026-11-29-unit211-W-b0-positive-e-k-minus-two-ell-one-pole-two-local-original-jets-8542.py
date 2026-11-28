#!/usr/bin/env python3
"""NEW original W/b0 local finite-jet obstruction, ell -> 1, mu pole.
Exactly two already derived positive valuation centers:
 A: e=x^2 R, (k+2)/e=x Y, R->3,Y->8/3;
 B: e=x R,   (k+2)/e=x Y, R->8,Y->-8; x=1/mu.
The normalized ORIGINAL q2/R6 have unit Jacobians at these two centers.
Their unique p-integral implicit jets are constructed over QQ, degree 12.
Only a first EXACT nonzero, p-unit coefficient of the COMPLETE original
x^5*N5 closes a center.  A zero jet or nonunit coefficient retains it.
No old resultant, gcd, initial ideal, sampled root, or numerical lifting.
Self-contained, 120 seconds /1 GiB; two fixed charts in this one input.
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
def originals(Rs,Ys,mode,need_nv=False):
 power=2 if mode=='A' else 1
 e=X**power*Rs
 k=-2+e*X*Ys
 mu=X**(-1);lam=(mu+3)/2
 u=e+1;Q=e*k;delta=1-Q;Vbar=u*k+2
 ell=u*((k+2)**2-2*e*k)/(k*Vbar)
 m=u-ell;M=ell*ell*delta-m*m;bc=M/(4*delta)
 V2=2*u-ell*Q;T0=V2-2*u*u
 J=2*u*(1-u)+ell*Q;Ast=4*u*Q-J
 kap=u*Q*ell/Ast;T=kap*mu
 A2=(mu*mu+4*mu+5)/2
 B3=(mu**3+6*mu*mu+12*mu+7)/2
 D=ell*A2-T*T;K=ell*ell*B3-3*ell*A2*T+2*T**3
 # q2/(2*u*Q*ell) = 4*delta*(D-M*Sphysical).
 qhat=(4*delta*D-M*(A2/kap+(2*mu+3)/u)).shift(2)
 rhat=(M*K*K-4*m*m*D**3).shift(6)
 fq=qhat.shift(-1)
 fr=rhat.shift(-3 if mode=='A' else -2)
 # All divisions by x here are previously proved entire identities
 # in the local regular coefficient ring at the named center.
 assert fq.val() is None or fq.val()>=0
 assert fr.val() is None or fr.val()>=0
 if not need_nv:return fq,fr
 Phi=T0+4*u-4+Q
 P02=(2-3*u)*V2-Q*u+2*u**3
 G=lam*P02-(1-u)*T0
 Pc=Q*P02*(ell+T)-G*T0
 ts=-Pc/(bc*Q*Phi)
 Vs=-G/Q-Pc/(Q*Phi);Ws=T0/2
 ys=(ell*Ws-u*Vs)/M
 w=lam-1-T;cval=-mu
 z1=-2*(ell*cval+2*T)*ys-2*ell*w+m*T*ts/delta
 z2=-2*G/Q-4*m*ys
 Z0=2*(ell*cval+T)*(ell*u*w+Vs*T)+2*bc*ts*T*T
 n5=2*m*D*(Z0+D*z2)+M*K*z1
 nhat=n5.shift(5)
 assert nhat.val() is None or nhat.val()>=0
 return fq,fr,nhat
# No center selection is made from a value-ideal test.
CHARTS=[('A',q(3),q(8)/3,[[q(0),-q(3)/4],[q(1)/6,q(0)]]),
        ('B',q(8),-q(8),[[-q(1),-q(3)/4],[q(1)/2,q(1)/2]])]
for mode,R0,Y0,JAC in CHARTS:
 Rser=S(R0);Yser=S(Y0)
 fq,fr=originals(Rser,Yser,mode)
 fq.checked_zero_below(1);fr.checked_zero_below(1)
 det=JAC[0][0]*JAC[1][1]-JAC[0][1]*JAC[1][0]
 assert det and pmod(det)
 # Exact coefficient checks of the two derivative columns at order x.
 for j in range(2):
  qa,ra=originals(Rser+(X if j==0 else 0),
                   Yser+(X if j==1 else 0),mode)
  assert qa.coeff(1)-fq.coeff(1)==JAC[0][j]
  assert ra.coeff(1)-fr.coeff(1)==JAC[1][j]
  STAT['seriesExactCoordinateChecks']+=2
 say('new_local_original_q2_R6_unit_Jacobian',
     chart=mode,centerR=str(R0),centerY=str(Y0),
     originalNormalizations=['x^2*q2/(2*u*Q*ell)/x',
                            'x^6*R6/x^'+('3' if mode=='A' else '2')],
     jacobian=[[str(c) for c in row] for row in JAC],
     jacobianDeterminant=str(det),jacobianMod1009=pmod(det),
     prescribedExactQQJetOrder=ORDER,
     noOldResultantGcdOrInitialIdeal=True)
 for n in range(1,ORDER+1):
  fq,fr=originals(Rser,Yser,mode)
  fq.checked_zero_below(n);fr.checked_zero_below(n)
  a,b=fq.coeff(n),fr.coeff(n)
  dR=(-JAC[1][1]*a+JAC[0][1]*b)/det
  dY=(JAC[1][0]*a-JAC[0][0]*b)/det
  pmod(dR);pmod(dY)
  Rser=Rser+S({n:dR});Yser=Yser+S({n:dY})
  STAT['implicitJetCoefficients']+=2
 fq,fr,nhat=originals(Rser,Yser,mode,True)
 fq.checked_zero_below(ORDER+1);fr.checked_zero_below(ORDER+1)
 ipcheck(Rser,ORDER);ipcheck(Yser,ORDER);ipcheck(nhat,ORDER)
 STAT['finalOriginalN5Jets']+=1
 nz=next((n for n in range(ORDER+1) if nhat.coeff(n)),None)
 if nz is None:
  say('new_local_complete_N5_jet_has_no_obstruction',
      chart=mode,throughOrder=ORDER,
      exactQ2R6Jets=[profile(fq,ORDER),profile(fr,ORDER)],
      completeN5Jet=profile(nhat,ORDER),wholeCenterRetained=True,
      noHigherOrderRunAuthorized=True,statistics=STAT)
  continue
 coefficient=nhat.coeff(nz);residue=pmod(coefficient)
 cbytes=str(coefficient).encode()
 say('new_local_complete_original_N5_first_coefficient',
     chart=mode,firstExactNonzeroOrder=nz,
     everyEarlierCoefficientExactlyQQZero=True,
     firstCoefficientMod1009=residue,
     firstCoefficientBytes=len(cbytes),
     firstCoefficientSHA256=hashlib.sha256(cbytes).hexdigest(),
     exactImplicitRJet=profile(Rser,ORDER),
     exactImplicitYJet=profile(Yser,ORDER),
     completeOriginalN5Jet=profile(nhat,ORDER),
     originalQ2AndR6BothZeroThroughOrder=ORDER,
     unitJacobianAndEntirePIntegralLocalModel=True,
     excludesThisValuationCenter=bool(residue),
     nonunitFirstCoefficientRetainsCenter=not bool(residue),
     notBareModDNilpotenceOrQQEmptyLifting=True,statistics=STAT)
say('new_two_prescribed_original_local_jet_input_complete',
 fixedOrder=ORDER,onlyNamedTwoCenters=True,
 actualOriginalN5Jets=STAT['finalOriginalN5Jets'],statistics=STAT)
