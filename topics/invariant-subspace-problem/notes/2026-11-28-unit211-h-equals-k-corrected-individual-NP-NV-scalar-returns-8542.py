#!/usr/bin/env python3
"""NEW h=k individual original N/P cubic rows and exact NV scalar return.
Only the successful coordinate-definition prefix of corrected f33 is rebuilt.
No previous five-row/cofactor/factorization or wrong compact source is run.
The full same-point Gram uses true dual multiplication. Four individual
B/C conditions give complete even/odd cubics; NV remains an affine row.
For each cubic P, a^3*P-R=NV*H is returned without dividing a.
All a=0, Delta=0 and original leading-zero fibers remain. Only the named
coordinate/physical units are cleared. 180 seconds / 4 GiB.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq
START=time.perf_counter();DEADLINE=START+180
signal.setitimer(signal.ITIMER_REAL,180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
path=Path(__file__).with_name('2026-11-28-unit211-h-equals-k-corrected-dual-germ-five-original-rows-three-cofactors-8542.py')
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='2ea618c508489fedffdec7418cc153f6fc213ef46b329f8c55743be312d9faa2'
marker=b'\n# Exact scalar forms'
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert len(prefix)==4540
assert hashlib.sha256(prefix).hexdigest()=='a56e54b840cc323675394f96484c99658cad9a8420933cd2f344fe2df0d76efc'
env={'__file__':str(path),'__name__':'new_individual_original_value_rows_only'}
old_alarm=signal.alarm;old_timer=signal.setitimer
def timer(which,seconds,interval=0.0):
 if which!=signal.ITIMER_REAL:return old_timer(which,seconds,interval)
 assert not interval
 left=max(.001,DEADLINE-time.perf_counter())
 return old_timer(which,min(left,float(seconds) if seconds>0 else left),0)
def alarm(seconds):return math.ceil(timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=alarm;signal.setitimer=timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+'#necessary_coordinate_prefix','exec'),env)
finally:
 signal.alarm=old_alarm;signal.setitimer=old_timer
 old_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
R,U,ctx=env['R'],env['U'],env['ctx']
lam,u,Q,disc=[env[k] for k in ['lam','u','Q','disc']]
A,B,xi,ell,T,w,hh=[env[k] for k in ['A','B','xi','ell','T','w','hh']]
m,a,bc,V2,T0,J,Phi,P02,Pf=[env[k] for k in ['m','a','bc','V2','T0','J','Phi','P02','Pf']]
z,f,nv,vn,Wstar=[env[k] for k in ['z','f','nv','vn','Wstar']]
zeroP=ctx.constant(0);oneP=ctx.constant(1)
M=ell*V2-u*u
assert M==4*bc*disc
def higher(fn):
 def call(self,other):
  if getattr(other,'_isp_quotient_level',0)>1:return NotImplemented
  return fn(self,other)
 return call
for name in ['__add__','__radd__','__sub__','__rsub__','__mul__','__rmul__','__truediv__','__eq__']:
 setattr(U,name,higher(getattr(U,name)))
class E:
 _isp_quotient_level=2
 def __init__(self,x=0,y=0):
  if isinstance(x,E):
   assert not y;self.x=x.x;self.y=x.y
  else:self.x=U(x);self.y=U(y)
 def __bool__(self):return bool(self.x) or bool(self.y)
 def __add__(self,o):o=E(o);return E(self.x+o.x,self.y+o.y)
 __radd__=__add__
 def __neg__(self):return E(-self.x,-self.y)
 def __sub__(self,o):return self+-E(o)
 def __rsub__(self,o):return E(o)+-self
 def __mul__(self,o):
  o=E(o);return E(self.x*o.x+disc*self.y*o.y,self.x*o.y+self.y*o.x)
 __rmul__=__mul__
 def __truediv__(self,o):
  assert not isinstance(o,(U,E))
  return E(self.x/o,self.y/o)
 def __pow__(self,n):
  assert n>=0
  out=E(1)
  for _ in range(n):out=out*self
  return out
 def __eq__(self,o):
  o=E(o);return self.x==o.x and self.y==o.y
 def conj(self):return E(self.x,-self.y)
p=E(1,1);q=p.conj()
bb=E(ell/2,m/(2*disc));cc=bb.conj()
assert bb+cc==E(ell) and bb*cc==E(bc) and bb*p+cc*q==E(u)
VV=vn/Q;WW=Wstar/2;t=z/Q
xx=((u-ell*Q)*VV-m*WW)/M
yy=(ell*WW-u*VV)/M
X=E(xx,yy);Y=X.conj()
assert bb*X+cc*Y==E(VV) and bb*p*X+cc*q*Y==E(WW)
r=X-E(a)*p-cc*E(t);s=Y-E(a)*q-bb*E(t)
AA=E(2*f-2*VV+2*bc*t)
rows=[[E(),E(),p,q],[E(),AA,r,s],
      [p,r,E(),E(t)],[q,s,E(t),E()]]
unit=[E(1),E(),E(1),E(1)]
def va(v,z):return [x+y for x,y in zip(v,z)]
def vs(x,v):x=E(x);return [x*y for y in v]
def vm(v,z):
 return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return E(a)*v[0]+v[1]+bb*v[2]+cc*v[3]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(unit);F2=tau(d);Kd=DK(d)
assert F2==E(2*f) and d[0]==E(u)
def mean(j):
 e=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
 return e-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
assert not mean(0)
def N4(v):
 tv=tau(v);vv=vm(v,v)
 return 2*tau(vm(d,vv))-F2*tau(vv)-4*tv*tau(vm(d,v))+2*F2*tv**2+tau(vm(v,DK(v)))
def centered(v):return va(v,vs(-tau(v),unit))
def P2(v):
 cv=centered(v);return tau(vm(vm(cv,cv),cv))
Pj=3*tau(vm(vm(centered(rows[0]),centered(rows[0])),centered(rows[1])))
assert P2(rows[0])==E(P02)
assert N4(rows[0])==E(2*lam*P02)
assert Pj==E(3*w*P02)
value=[E(1),E(w),E(hh),E(hh)]
assert tau(value)==E(lam) and tau(vm(value,value))==E(2*lam*lam)
assert tau(vm(vm(value,value),value))==E(4*lam**3)
assert E(Q)*N4(value)==E(2*nv)
NerrB=N4(rows[2])-E(2*lam*P02*hh*hh)
NerrC=N4(rows[3])-E(2*lam*P02*hh*hh)
PerrB=P2(rows[2])-E(P02*hh**3)
PerrC=P2(rows[3])-E(P02*hh**3)
assert NerrB.conj()==NerrC and PerrB.conj()==PerrC
new_original=[('NBe',NerrB.x),('NBo',NerrB.y),
              ('PBe',PerrB.x),('PBo',PerrB.y)]
assert all(len(v.c)<=4 for _,v in new_original)
say('new_h_equals_k_complete_individual_original_value_rows',
 correctOriginalJetProduct=True,sameGramE0N0P0P1AndFullNVReturned=True,
 originalValueMoments=[1,2,3],bothOriginalSingletonsRetained=True,
 fullRhoQuadraticRetained=True,
 originalZDegrees={name:len(v.c)-1 for name,v in new_original},
 noDeltaOrNVSlopeInverse=True,oldFiveRowCofactorsNotReplayed=True)

# lambda is the nonzero original isolated mean divided by its nonzero
# normalization. lambda=1/2 is excluded by the independently read 347c
# full original five-column physical proof, NOT a naked ideal identity.
physical_atoms=[('A',A.n),('B',B.n),('Q',Q.n),('1-Q',disc.n),
 ('Pf_coordinate',Pf.n),('M_equals_4bc_delta',M.n),
 ('P02_original_nonzero',P02.n),
 ('lambda_original_isolated_mean',lam.n),
 ('lambda_half_original_physical_rank', (2*lam-1).n)]
exact_returns=0
def dex(p,q):
 global exact_returns
 a,b=divmod(p,q);assert not b and a*q==p
 exact_returns+=1;return a
def strip(p):
 original=p;removed=oneP;history=[]
 if not p:return p,removed,history
 for name,atom in physical_atoms:
  count=0
  while True:
   fac=p.gcd(atom)
   if int(fac.total_degree())==0:break
   p=dex(p,fac);removed*=fac;count+=1
  if count:history.append([name,count])
 assert p*removed==original
 return p,removed,history
def paid_den(d):
 rem,_,hist=strip(d)
 assert rem and int(rem.total_degree())==0
 return hist
def info(p):
 if not p:return dict(zero=True,degrees_lambda_u_Q=[-1,-1,-1],terms=0)
 data=[[list(map(int,mm)),str(c)] for mm,c in sorted(p.to_dict().items())]
 raw=json.dumps(data,separators=(',',':')).encode()
 return dict(zero=False,degrees_lambda_u_Q=list(map(int,p.degrees())),
  totalDegree=int(p.total_degree()),terms=len(data),bytes=len(raw),
  sha256=hashlib.sha256(raw).hexdigest())
def clear(name,value):
 den=oneP
 for v in value.c:
  paid_den(v.d);den=dex(den,den.gcd(v.d))*v.d
 paid_den(den)
 rr=[v.n*dex(den,v.d) for v in value.c]
 content=zeroP
 for p0 in rr:
  if p0:content=p0 if not content else content.gcd(p0)
 _,removed,hist=strip(content) if content else (zeroP,oneP,[])
 rr=[dex(p0,removed) for p0 in rr]
 if rr:
  lc=next(p0 for p0 in rr if p0).coefficient(0)
  rr=[p0/lc for p0 in rr];removed*=lc
 assert U([R(p0*removed,den) for p0 in rr])==value
 say('new_individual_original_row_clearing',name=name,
  originalZDegree=len(value.c)-1,coefficients=[info(p0) for p0 in rr],
  namedPhysicalRemoval=hist,entireSameOriginalRowReturned=True,
  noUnknownWeightOrHeadInverse=True)
 return rr
NVrow=clear('NV_original_affine',nv)
NVrow+= [zeroP]*(2-len(NVrow))
b0,a0=NVrow
cleared=[(name,clear(name,value)) for name,value in new_original]
def padd(x,y):
 n=max(len(x),len(y));return [(x[i] if i<len(x) else zeroP)+(y[i] if i<len(y) else zeroP) for i in range(n)]
def pneg(x):return [-v for v in x]
def psub(x,y):return padd(x,pneg(y))
def pmul(x,y):
 if not x or not y:return []
 out=[zeroP for _ in range(len(x)+len(y)-1)]
 for i,v in enumerate(x):
  for j,w0 in enumerate(y):out[i+j]=out[i+j]+v*w0
 return out
def peq(x,y):return all(not p0 for p0 in psub(x,y))
cofactor_records=[]
for name,row in cleared:
 row=row+[zeroP]*(4-len(row))
 result=sum((row[j]*(-b0)**j*a0**(3-j) for j in range(4)),zeroP)
 quotient=[zeroP]*3
 for j in range(1,4):
  for k0 in range(j):
   power=j-1-k0
   quotient[power]=quotient[power]+row[j]*a0**(2-k0)*(-b0)**k0
 assert peq(psub([a0**3*c0 for c0 in row],[result]),pmul(NVrow,quotient))
 core,removed,hist=strip(result)
 if core:
  lc=core.coefficient(0);core=core/lc;removed*=lc
 assert core*removed==result
 record=dict(name=name,originalScalar=info(result),physicalNecessaryCore=info(core),
  physicalRemoval=hist,completeFourZColumnsReturned=True,
  exactOriginalIdentity='a^3*P(z)-R=(b+a*z)*H(z)',
  noSlopeInverse=True,entireDeltaZeroAndAllHeadZerosRetained=True,
  noCommonZeroExclusionClaim=True)
 say('new_individual_original_NV_cubic_scalar_return',**record)
 if core:
  scalar,factors=core.factor();back=ctx.constant(scalar);fs=[]
  for factor,mul0 in factors:
   back*=factor**int(mul0)
   fs.append(dict(multiplicity=int(mul0),**info(factor)))
  assert back==core
  record['factorization']=dict(scalar=str(scalar),factors=fs,wholeProductReturned=True)
  say('new_individual_original_scalar_exact_factors',name=name,**record['factorization'])
 cofactor_records.append(record)
say('new_h_equals_k_individual_NP_NV_scalar_returns_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 completeNewOriginalRowCount=4,completeNewScalarReturnCount=len(cofactor_records),
 namedCoordinateChart=['A','B','Q','1-Q','Pf'],
 physicalAssumptions=['bc!=0','P02!=0','nonzero isolated mean','old physical lambda half exclusion'],
 allDeltaZeroAndNewScalarZeroSetsRetained=True,
 oldCorrectFiveRowCofactorAndFactorizationNotReexecuted=True,
 noOldWrongCompactSourceUsed=True,
 exactPolynomialDivisionReturns=exact_returns,
 noCoefficientCacheSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 originalChartExcluded=False,ordinaryISPClaim=False)
