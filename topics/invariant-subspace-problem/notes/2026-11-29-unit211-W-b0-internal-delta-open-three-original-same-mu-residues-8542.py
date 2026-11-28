#!/usr/bin/env python3
"""NEW W/b0 INTERNAL delta-positive, complete finite-mu residual input.
Residue characteristic 1009; Q=1 is taken BEFORE any new expansion.
Only the open residue chart u*(u-1)*(3u-2)*(2u^2-1)*(2u-1)*
(4u^2+2u-3)*(4u-3) != 0 is used. All other residue charts retained.
q2 is monic in the SAME mu; full R6/full N5 reduce to two linear rows.
One cross and two same-mu norms return to the three complete originals.
Their fixed Fp[u] Bezout gives an unpaid u support or a full positive
declared-chart-unit target. No QQ emptiness lift, selected residue point, prime
change, old ray/initial/gcd replay, coefficient payload or cache.
120 seconds / 1 GiB; self-contained standard-library arithmetic.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
START=time.perf_counter(); DEADLINE=START+120; P=1009
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
STAT={'FpPolynomialDivisionProducts':0,'FpBezoutCoordinateReturns':0,
      'rationalCoefficientInverseProducts':0,'muDivisionProducts':0,
      'threeOriginalMuCoordinateReturns':0,'paidDenominatorChecks':0,
      'sameMuCofactorReturns':0,'supportDivisionProducts':0}
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute120')
def say(stage,**data):
 data.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(data,sort_keys=True,separators=(',',':')),flush=True)
def tr(a):
 a=[int(x)%P for x in a]
 while a and not a[-1]:a.pop()
 return a
def add(a,b):
 z=[0]*max(len(a),len(b))
 for i,x in enumerate(a):z[i]=(z[i]+x)%P
 for i,x in enumerate(b):z[i]=(z[i]+x)%P
 return tr(z)
def scale(a,c):return tr([x*int(c) for x in a])
def neg(a):return scale(a,-1)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 if not a or not b:return []
 tick();z=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  if not x:continue
  for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%P
 return tr(z)
def divmodp(a,b):
 a=tr(a);b=tr(b);assert b
 orig=a[:];q=[0]*max(0,len(a)-len(b)+1);ib=pow(b[-1],P-2,P)
 assert b[-1]*ib%P==1
 while a and len(a)>=len(b):
  tick();j=len(a)-len(b);c=a[-1]*ib%P;q[j]=c
  for i,x in enumerate(b):a[i+j]=(a[i+j]-c*x)%P
  a=tr(a)
 q=tr(q);assert add(mul(q,b),a)==orig
 STAT['FpPolynomialDivisionProducts']+=1
 return q,a
def exact(a,b):
 q,r=divmodp(a,b);assert not r and mul(q,b)==tr(a);return q
def xgcd(a,b):
 aa,bb=tr(a),tr(b);a,b=aa[:],bb[:]
 s0,s1=[1],[];t0,t1=[],[1]
 while b:
  q,r=divmodp(a,b)
  a,b=b,r;s0,s1=s1,sub(s0,mul(q,s1));t0,t1=t1,sub(t0,mul(q,t1))
  assert add(mul(s0,aa),mul(t0,bb))==a
  STAT['FpBezoutCoordinateReturns']+=1
 if not a:return [],[],[]
 c=pow(a[-1],P-2,P)
 g,s,t=scale(a,c),scale(s0,c),scale(t0,c)
 assert add(mul(s,aa),mul(t,bb))==g
 STAT['FpBezoutCoordinateReturns']+=1
 return g,s,t
def gcd(a,b):return xgcd(a,b)[0]
def power(a,n):
 assert isinstance(n,int) and n>=0
 z=[1]
 while n:
  if n&1:z=mul(z,a)
  n//=2
  if n:a=mul(a,a)
 return z
class F:
 def __init__(self,n=0,d=None):
  if isinstance(n,F):
   assert d is None;self.n=n.n[:];self.d=n.d[:];return
  n=tr(n if isinstance(n,(list,tuple)) else [n])
  d=[1] if d is None else tr(d)
  assert d
  if not n:self.n=[];self.d=[1];return
  g=gcd(n,d);n=exact(n,g);d=exact(d,g)
  c=pow(d[-1],P-2,P);self.n=scale(n,c);self.d=scale(d,c)
 def __bool__(self):return bool(self.n)
 def __neg__(self):return F(neg(self.n),self.d)
 def __add__(self,v):
  v=F(v)
  if not self:return v
  if not v:return self
  g=gcd(self.d,v.d);a=exact(self.d,g);b=exact(v.d,g)
  return F(add(mul(self.n,b),mul(v.n,a)),mul(a,v.d))
 __radd__=__add__
 def __sub__(self,v):return self+-F(v)
 def __rsub__(self,v):return F(v)+-self
 def __mul__(self,v):
  v=F(v)
  if not self or not v:return F()
  g=gcd(self.n,v.d);h=gcd(v.n,self.d)
  return F(mul(exact(self.n,g),exact(v.n,h)),
           mul(exact(self.d,h),exact(v.d,g)))
 __rmul__=__mul__
 def inv(self):
  assert self;z=F(self.d,self.n);assert self*z==1
  STAT['rationalCoefficientInverseProducts']+=1;return z
 def __truediv__(self,v):return self*F(v).inv()
 def __rtruediv__(self,v):return F(v)*self.inv()
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  return F(power(self.n,n),power(self.d,n))
 def __eq__(self,v):
  v=F(v);return self.n==v.n and self.d==v.d
class MP:
 def __init__(self,c=0):
  if isinstance(c,MP):self.c=c.c[:];return
  self.c=[F(x) for x in c] if isinstance(c,(list,tuple)) else [F(c)]
  while self.c and not self.c[-1]:self.c.pop()
 def __bool__(self):return bool(self.c)
 def __neg__(self):return MP([-x for x in self.c])
 def __add__(self,v):
  v=MP(v);z=[F() for _ in range(max(len(self.c),len(v.c)))]
  for i,x in enumerate(self.c):z[i]+=x
  for i,x in enumerate(v.c):z[i]+=x
  return MP(z)
 __radd__=__add__
 def __sub__(self,v):return self+-MP(v)
 def __rsub__(self,v):return MP(v)+-self
 def __mul__(self,v):
  v=MP(v)
  if not self or not v:return MP()
  z=[F() for _ in range(len(self.c)+len(v.c)-1)]
  for i,x in enumerate(self.c):
   for j,y in enumerate(v.c):z[i+j]+=x*y
  return MP(z)
 __rmul__=__mul__
 def __truediv__(self,v):
  v=MP(v);assert len(v.c)==1;iv=v.c[0].inv()
  return MP([x*iv for x in self.c])
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  z=MP(1);a=self
  while n:
   if n&1:z=z*a
   n//=2
   if n:a=a*a
  return z
 def __eq__(self,v):return self.c==MP(v).c
 def coeff(self,j):return self.c[j] if j<len(self.c) else F()
def mdiv(a,b):
 a=MP(a);b=MP(b);assert b
 original=a;q=MP()
 while a and len(a.c)>=len(b.c):
  tick();j=len(a.c)-len(b.c);lc=a.c[-1]/b.c[-1]
  mon=MP([F()]*j+[lc]);q+=mon;a-=mon*b
 assert q*b+a==original and (not a or len(a.c)<len(b.c))
 STAT['muDivisionProducts']+=1
 return q,a
def pprofile(a):
 a=tr(a);raw=json.dumps(a,separators=(',',':')).encode()
 return {'degree':len(a)-1,'nonzeroTerms':sum(bool(x) for x in a),
         'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def mprofile(a):
 a=MP(a);data=[[x.n,x.d] for x in a.c]
 raw=json.dumps(data,separators=(',',':')).encode()
 return {'muDegree':len(a.c)-1,
         'maxNumeratorUDegree':max((len(x.n)-1 for x in a.c),default=-1),
         'maxDenominatorUDegree':max((len(x.d)-1 for x in a.c),default=-1),
         'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
u=F([0,1]);e=u-1;Q=F(1)
ell=u*(2*u*u-1)/(3*u-2)
m=u-ell;M=-m*m
J=2*u*(1-u)+ell;Ast=4*u-J;Cst=Ast*m*m
T0=2*u-ell-2*u*u;Phi=T0+4*u-3
P02=(2-3*u)*(2*u-ell)-u+2*u**3
assert Ast==u*(4*u*u+2*u-3)/(3*u-2)
assert m==-u*(u-1)*(2*u-1)/(3*u-2)
assert Phi==-2*(u-1)**2*(4*u-3)/(3*u-2)
assert P02==2*u*(u-1)*(2*u-1)
paid_atoms=[('u',u.n),('e',(u-1).n),('Vbar',(3*u-2).n),
            ('ell',(2*u*u-1).n),('m',(2*u-1).n),
            ('Astar',(4*u*u+2*u-3).n),('Phi',(4*u-3).n)]
S=[1]
for _,a in paid_atoms:S=mul(S,a)
seen=set()
def paid_den(d):
 d=tr(d);assert d
 key=tuple(d)
 if key in seen:return
 before=d[:]
 for _,a in paid_atoms:
  while len(d)>1:
   g=gcd(d,a)
   if len(g)==1:break
   d=exact(d,g)
 assert len(d)==1,'unpaid residue denominator retained; no closure'
 seen.add(key);STAT['paidDenominatorChecks']+=1
def paid_mp(a):
 for x in MP(a).c:paid_den(x.d)
mu=MP([0,1]);lam=(mu+3)/2
ellp,mp,Mp,up=map(MP,(ell,m,M,u))
T=mu*MP(u*ell/Ast)
A2=(mu*mu+4*mu+5)/2;B3=(mu**3+6*mu*mu+12*mu+7)/2
D=ellp*A2-T*T;K=ellp**2*B3-3*ellp*A2*T+2*T**3
qraw=2*MP(Cst)*A2+2*Mp*ellp*(-3-2*mu)
Rraw=Mp*K*K-4*mp*mp*D**3
# Exact regular delta-zero specialization of the COMPLETE full N5.
# bc*t_s=-Pc/Phi and m*T*t_s/delta=-4*m*T*Pc/(M*Phi)
# are cancelled as original rational identities before delta=0.
G=lam*MP(P02)+MP(e*T0)
Pc=MP(P02)*(ellp+T)-G*MP(T0)
Vs=-G-Pc/MP(Phi)
ys=(MP(ell*T0/2)-up*Vs)/Mp
w=lam-1-T
z1=-2*(-ellp*mu+2*T)*ys-2*ellp*w-4*mp*T*Pc/MP(M*Phi)
z2=-2*G-4*mp*ys
Z0=2*(T-ellp*mu)*(MP(ell*u)*w+Vs*T)-2*Pc*T*T/MP(Phi)
Nraw=2*mp*D*(Z0+D*z2)+Mp*K*z1
raw=[qraw,Rraw,Nraw]
for F0 in raw:paid_mp(F0)
assert len(qraw.c)==3 and qraw.coeff(2)==m*m*Ast
say('new_internal_delta_open_same_mu_three_original_residues',
    p=P,openResidueSupport=pprofile(S),
    paidSupportLabels=[x[0] for x in paid_atoms],
    originalProfiles=[mprofile(v) for v in raw],
    deltaZeroTakenAfterExactN5Cancellation=True,
    noPhysicalFZero=True,noResidualLambdaOrDUnitAssumed=True,
    allComplementaryResidueChartsRetained=True)
qscale=1/(m*m*Ast);q=qraw*MP(qscale)
assert q.coeff(2)==1
qtag=[MP(qscale),MP(),MP()]
def combine(tags):return sum((tags[i]*raw[i] for i in range(3)),MP())
def original_return(value,tags):
 back=combine(tags);assert back==MP(value)
 for j in range(max(len(back.c),len(MP(value).c))):
  assert back.coeff(j)==MP(value).coeff(j)
  STAT['threeOriginalMuCoordinateReturns']+=1
 for a in tags:paid_mp(a)
original_return(q,qtag)
qr,r=mdiv(Rraw,q);qn,n=mdiv(Nraw,q)
rtag=[-qr*MP(qscale),MP(1),MP()]
ntag=[-qn*MP(qscale),MP(),MP(1)]
original_return(r,rtag);original_return(n,ntag)
assert len(r.c)<=2 and len(n.c)<=2
say('new_same_mu_monic_quadratic_and_two_complete_linear_rows',
    monicQ=mprofile(q),Rremainder=mprofile(r),Nremainder=mprofile(n),
    completeMuCoordinatesReturned=True,noSlopeInverse=True)
ar,br=r.coeff(0),r.coeff(1);an,bn=n.coeff(0),n.coeff(1)
q0,q1=q.coeff(0),q.coeff(1)
specs=[]
cross=MP(bn)*r-MP(br)*n
ct=[MP(bn)*rtag[i]-MP(br)*ntag[i] for i in range(3)]
specs.append(('same_mu_R_N_cross',cross,ct))
for label,row,tag,aa,bb in [('same_mu_R_norm',r,rtag,ar,br),
                          ('same_mu_N_norm',n,ntag,an,bn)]:
 L=MP(aa-q1*bb)-MP(bb)*mu
 val=L*row+MP(bb*bb)*q
 target=MP(aa*aa-q1*aa*bb+q0*bb*bb)
 assert val==target
 tags=[L*tag[i]+MP(bb*bb)*qtag[i] for i in range(3)]
 specs.append((label,val,tags))
polys=[];ptags=[]
for label,val,tags in specs:
 assert len(val.c)<=1
 original_return(val,tags)
 cf=val.coeff(0);p=cf.n[:]
 poly_tags=[MP(F(cf.d))*a for a in tags]
 original_return(MP(F(p)),poly_tags)
 polys.append(p);ptags.append(poly_tags)
 STAT['sameMuCofactorReturns']+=1
 say('new_same_mu_original_scalar_complete',
     label=label,necessaryPolynomial=pprofile(p),
     originalThreeMultipliers=[mprofile(a) for a in poly_tags],
     completeThreeOriginalMuCoordinatesReturned=True,
     allRemainderSlopeAndMuHeadsRetained=True)
g=[];gt=[MP(),MP(),MP()]
for i,p in enumerate(polys):
 if not p:continue
 if not g:
  c=pow(p[-1],P-2,P);g=scale(p,c)
  gt=[MP(c)*a for a in ptags[i]]
 else:
  ng,a,b=xgcd(g,p)
  gt=[MP(F(a))*gt[j]+MP(F(b))*ptags[i][j] for j in range(3)]
  g=ng
 original_return(MP(F(g)),gt)
 say('new_three_original_residue_u_Bezout',
     throughScalar=i,common=pprofile(g),
     entireThreeOriginalMuReturn=True)
remaining=g[:];removed=[1];history=[]
if g:
 for label,a in paid_atoms:
  count=0
  while len(remaining)>1:
   h=gcd(remaining,a)
   if len(h)==1:break
   remaining=exact(remaining,h);removed=mul(removed,h);count+=1
   STAT['supportDivisionProducts']+=1
  if count:history.append({'label':label,'gcdLayers':count})
 assert mul(remaining,removed)==g
closed=False
if g and len(remaining)==1:
 exponent=max(0,len(g)-1)
 target=power(S,exponent);quot,rem=divmodp(target,g)
 assert not rem
 finaltags=[MP(F(quot))*a for a in gt]
 original_return(MP(F(target)),finaltags)
 # Clear ALL ACTUAL terminal u denominators, only from the declared chart.
 den=[1]
 for a in finaltags:
  for x in a.c:
   paid_den(x.d);den=mul(exact(den,gcd(den,x.d)),x.d)
 paid_den(den)
 cleared=[MP(F(den))*a for a in finaltags]
 for a in cleared:
  assert all(x.d==[1] for x in a.c)
 fulltarget=mul(den,target)
 original_return(MP(F(fulltarget)),cleared)
 closed=True
 say('new_internal_delta_open_original_positive_unit_returned',
     declaredResidueSupportPower=exponent,terminalDenominator=pprofile(den),
     target=pprofile(fulltarget),
     exactThreeOriginalPolynomialMultipliers=[mprofile(a) for a in cleared],
     entireOriginalMuPolynomialReturned=True,
     noQQFiberEmptinessLift=True,onlyDeclaredResidueOpenChart=True)
say('new_internal_delta_finite_mu_original_input_complete',
    p=P,completeCommon=pprofile(g),unpaidRemainder=pprofile(remaining),
    paidSupportRemoval=history,excludesWholeDeclaredResidueChart=closed,
    allUnpaidUZeroFibersRetained=not closed,
    allComplementaryResidueChartsRetained=True,
    statistics=STAT,
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    noOldGateReplayed=True,noCoefficientPayloadOrCache=True)
