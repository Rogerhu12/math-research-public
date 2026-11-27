#!/usr/bin/env python3
"""NEW whole original collision fibre u=2, including every lambda/Q head.
Use the four ORIGINAL same-point Q rows, not the two E projections.
Only factors dividing the explicitly paid original physical product may
be saturated. Fixed actual Q resultants give a necessary lambda cover;
all remaining QQ factors are returned to every original Q condition.
No old E37 determinant or old u-head gate is replayed.
Only small definitions/profiles/hashes; historical inputs are temporary.
180 seconds /4GiB.
"""
import json,time,hashlib,signal,resource,zlib,base64,itertools
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx
start=time.perf_counter();signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start
 print(json.dumps(r,separators=(',',':')),flush=True)
def read(name,sha):
 raw=Path(__file__).with_name(name).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==sha
 return json.loads(raw)
def digest(obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def P(v=()):
 if isinstance(v,fmpq_poly):return v
 if isinstance(v,(int,fmpq)):v=[v]
 return fmpq_poly([fmpq(c) for c in v])
def coeffs(v):return [str(c) for c in v.coeffs()]
def pp(v):return dict(degree=int(v.degree()),**digest(coeffs(v)))
one=P(1);lp=P([0,1])
class BaseNonunit(Exception):
 def __init__(self,g):self.g=g
encoded=[]
for name,sha in [
 ('2026-11-27-unit211-collision-Delta-nonzero-four-original-exact-input-part1-8542.json',
  'c4723da150647c453cd53151b4e9f84e5d6ed1c45dffcf4c39299b9ef968c3e6'),
 ('2026-11-27-unit211-collision-Delta-nonzero-four-original-exact-input-part2-8542.json',
  '8f8a547ba11ffc2baafd0229f9ffce5a16576206d06460d627927b80d4671682')]:
 encoded.append(read(name,sha)['dataChunk'])
raw=zlib.decompress(base64.b64decode(''.join(encoded)))
assert hashlib.sha256(raw).hexdigest()=='11046373e5362f4b5606e2940483929954a74382e152e40f211fbe79ec42b292'
original=json.loads(raw);assert original['variables']==['lambda','u','Q']

ctx=fmpq_mpoly_ctx.get(('lambda','Q'),'lex');lam,q=ctx.gens()
def profile(v):
 data=[[list(map(int,e)),str(c)] for e,c in sorted(v.to_dict().items())]
 return dict(degrees=list(map(int,v.degrees())),terms=len(data),**digest(data))
def qcoeff(v):
 out=[P() for _ in range(max(0,int(v.degrees()[1]))+1)]
 for (a,b),c in v.to_dict().items():out[int(b)]+=c*lp**int(a)
 while out and not out[-1]:out.pop()
 return out
A=2*lam*lam-2*lam+1;B=4*lam**3-6*lam*lam+3*lam-1
X=A**3;Y=B**2;eta=B+(3-2*lam)*A;sn=2*B+(3-2*lam)*A
Tnum=-4*Y-X*q;JminusQnum=-4*Y+(X-Y)*q
Phinum=q*(Y-X);Pfnum=Tnum*JminusQnum
NFnum=(3-4*lam)*q*Y*A*A+(-4*Y+X*q)*B*eta
Deltanum=Phinum*NFnum-B*sn*Pfnum
Mnum=4*X*Y-X*X*q-4*Y*Y
P02num=2*q*(2*X-Y)
J2=3*lam*lam-2*lam+1;G2=lam*lam+lam-1
C4=8*lam**4-24*lam**3+24*lam*lam-12*lam+3
physical=Deltanum*q*(1-q)*Mnum*P02num*Phinum*Pfnum
physical*=lam*A*B*sn*J2*G2*C4*(2*Y-X)
assert physical
physical_grid=qcoeff(physical)
scalar_units=P()
for c in physical_grid:scalar_units=scalar_units.gcd(c)
assert scalar_units
scalar_units=scalar_units/scalar_units[scalar_units.degree()]
values={};original_values={};saturation_records=[]
for name in ['R','W','O','N1']:
 terms=original['polynomials'][name];dd={}
 for (aa,bb,qq),cf in terms:
  key=(aa,qq);dd[key]=dd.get(key,fmpq(0))+fmpq(cf)*2**bb
 v=ctx.from_dict({e:c for e,c in dd.items() if c})
 original_values[name]=v
 if not v:
  values[name]=v
  say(stage='new_collision_u2_original_row_identically_zero',name=name)
  continue
 counts=0;removed=ctx.constant(1);r=v
 while True:
  gg=r.gcd(physical)
  if gg.total_degree()<=0:break
  rr=r/gg
  assert rr*gg==r and not physical%gg
  r=rr;removed*=gg;counts+=1
 scalar=r.coefficient(0)
 r=r/scalar;removed*=scalar
 assert r*removed==v
 values[name]=r
 record=dict(name=name,original=profile(v),remaining=profile(r),
             paidFactorRemovalSteps=counts,
             wholePhysicalProduct='Delta*Q*(1-Q)*M*P02*Phi*Pf times explicitly paid scalar units',
             noUnpaidFactorRemoved=True,completeOriginalSaturationProductReturned=True)
 saturation_records.append(record)
 say(stage='new_collision_u2_complete_original_saturation',**record)
grids={name:qcoeff(v) for name,v in values.items()}
say(stage='new_collision_u2_original_input_ready',
    allOriginalRows=['R','W','O','N1'],
    originalPhysicalProductProfile=profile(physical),
    physicalScalarContent=pp(scalar_units),
    lambdaAndQAllRemainVariables=True,noEProjectionReconstruction=True)
def strip_scalar_units(p):
 before=P(p);removed=one
 while p:
  gg=p.gcd(scalar_units)
  if gg.degree()<=0:break
  qq,rr=divmod(p,gg)
  assert not rr and qq*gg==p
  p=qq;removed*=gg
 if p:
  sc=p[p.degree()];p=p/sc;removed*=sc
 assert p*removed==before
 return p
cover=P();projection_records=[]
for name,v in values.items():
 if v and int(v.degrees()[1])<=0:
  pp0=qcoeff(v)[0]
  cover=pp0 if not cover else cover.gcd(pp0)
  cover=strip_scalar_units(cover)
  projection_records.append(dict(type='entire original scalar row',name=name,profile=pp(pp0)))
  if cover.degree()==0:break
if cover.degree()!=0:
 for a,b in itertools.combinations(['R','W','O','N1'],2):
  va,vb=values[a],values[b]
  if not va or not vb or int(va.degrees()[1])<=0 or int(vb.degrees()[1])<=0:continue
  say(stage='new_collision_u2_fixed_original_Q_projection_started',
      originals=[a,b],fixedQDegrees=[int(va.degrees()[1]),int(vb.degrees()[1])])
  resultant=va.resultant(vb,'Q')
  assert not resultant or int(resultant.degrees()[1])<=0
  rp=qcoeff(resultant)[0] if resultant else P()
  record=dict(originals=[a,b],fixedQDegrees=[int(va.degrees()[1]),int(vb.degrees()[1])],
              projection=pp(rp),allLambdaHeadDropsRetainedByPolynomialResultant=True)
  projection_records.append(record)
  if rp:
   cover=rp if not cover else cover.gcd(rp)
   cover=strip_scalar_units(cover)
  say(stage='new_collision_u2_fixed_original_Q_projection_returned',
      **record,necessaryRemainingLambdaCover=pp(cover))
  if cover.degree()==0:break

def run_lambda_fibre(F,label):
 F=F/F[F.degree()];inverse_count=0;division_count=0
 class K:
  def __init__(self,v=0):
   if isinstance(v,K):self.p=v.p;return
   if not isinstance(v,fmpq_poly):v=P([v])
   qq,rr=divmod(v,F);assert qq*F+rr==v;self.p=rr
  def __bool__(self):return bool(self.p)
  def __neg__(self):return K(-self.p)
  def __add__(self,v):return K(self.p+K(v).p)
  __radd__=__add__
  def __sub__(self,v):return K(self.p-K(v).p)
  def __rsub__(self,v):return K(v)-self
  def __mul__(self,v):return K(self.p*K(v).p)
  __rmul__=__mul__
  def __eq__(self,v):return self.p==K(v).p
  def inv(self):
   nonlocal inverse_count
   assert self
   if self==1:return K(1)
   g,s,t=self.p.xgcd(F);assert s*self.p+t*F==g
   if g.degree()>0:raise BaseNonunit(g/g[g.degree()])
   ans=K(s/g[0]);assert self*ans==1;inverse_count+=1;return ans
  def __truediv__(self,v):return self*K(v).inv()
  def __rtruediv__(self,v):return K(v)*self.inv()
  def __pow__(self,n):
   if n<0:return self.inv()**(-n)
   out=K(1);v=self
   while n:
    if n&1:out=out*v
    v=v*v;n//=2
   return out
  def data(self):return coeffs(self.p)
 class U:
  def __init__(self,v=()):
   if isinstance(v,U):self.c=v.c[:];return
   if isinstance(v,(K,int,fmpq)):v=[v]
   self.c=[K(z) for z in v]
   while self.c and not self.c[-1]:self.c.pop()
  def __bool__(self):return bool(self.c)
  def degree(self):return len(self.c)-1
  def __neg__(self):return U([-z for z in self.c])
  def __add__(self,v):
   v=U(v);n=max(len(self.c),len(v.c))
   return U([(self.c[j] if j<len(self.c) else K())+(v.c[j] if j<len(v.c) else K()) for j in range(n)])
  __radd__=__add__
  def __sub__(self,v):return self+-U(v)
  def __rsub__(self,v):return U(v)+-self
  def __mul__(self,v):
   v=U(v)
   if not self or not v:return U()
   w=[K() for _ in range(len(self.c)+len(v.c)-1)]
   for i,a in enumerate(self.c):
    for j,b in enumerate(v.c):w[i+j]=w[i+j]+a*b
   return U(w)
  __rmul__=__mul__
  def scale(self,v):return U([z*K(v) for z in self.c])
  def __eq__(self,v):return self.c==U(v).c
  def data(self):return [z.data() for z in self.c]
 def dr(a,b):
  nonlocal division_count
  a,b=U(a),U(b);assert b
  q=U();r=U(a);li=b.c[-1].inv()
  while r and r.degree()>=b.degree():
   shift=r.degree()-b.degree();cf=r.c[-1]*li
   term=U([K()]*shift+[cf]);q=q+term;r=r-term*b
  assert q*b+r==a and (not r or r.degree()<b.degree())
  division_count+=1
  return q,r
 def xg(a,b):
  a,b=U(a),U(b);r0,r1=a,b;s0,s1=U(1),U();t0,t1=U(),U(1)
  while r1:
   q,r=dr(r0,r1);r0,r1=r1,r;s0,s1=s1,s0-q*s1;t0,t1=t1,t0-q*t1
  if r0:
   iv=r0.c[-1].inv();r0=r0.scale(iv);s0=s0.scale(iv);t0=t0.scale(iv)
  assert s0*a+t0*b==r0
  return r0,s0,t0

 vals={name:U([K(c) for c in col]) for name,col in grids.items()}
 target=U([K(c) for c in physical_grid])
 common=dict(path=label,lambdaFactor=pp(F),allActualQDegrees={name:v.degree() for name,v in vals.items()})
 if not target:
  return dict(common,excluded=True,reason='complete original paid physical product identically zero')
 current=U();tags={}
 for name,v in vals.items():
  if not v:continue
  gg,aa,bb=xg(current,v)
  tags={key:aa*value for key,value in tags.items()}
  tags[name]=tags.get(name,U())+bb
  current=gg
  assert sum((tags.get(key,U())*value for key,value in vals.items()),U())==current
  say(stage='new_collision_u2_complete_original_Q_gcd',
      path=label,originalsUsed=list(tags),degree=current.degree(),
      completeOriginalCombinationActuallyMultipliedBack=True)
  if current.degree()==0:
   assert current==U(1)
   return dict(common,excluded=True,reason='full original Q constant one',
      inverseProducts=inverse_count,divisionProducts=division_count,
      certificate=digest({key:v.data() for key,v in tags.items()}))
 if not current:
  return dict(common,excluded=False,reason='all original Q rows zero',entireQFibreRetained=True)
 quotient,remainder=dr(target,current)
 power=U(1)
 for exponent in range(1,current.degree()+1):
  rawpower=power*remainder;qq,power=dr(rawpower,current)
  assert qq*current+power==rawpower
  if not power:
   return dict(common,excluded=True,reason='full paid physical product nilpotent modulo original Q gcd',
       originalQGcdDegree=current.degree(),targetPower=exponent,
       inverseProducts=inverse_count,divisionProducts=division_count,
       certificate=digest(dict(originalGcd=current.data(),combination={key:v.data() for key,v in tags.items()},
                               targetRemainder=remainder.data(),targetPower=exponent)))
 return dict(common,excluded=False,remainingQDegree=current.degree(),
     completeOriginalConditionsRetained=True,
     inverseProducts=inverse_count,divisionProducts=division_count,
     remainingPolynomialIdentity=digest(current.data()))

returns=[];factor_records=[]
if not cover:
 say(stage='accurate_new_collision_u2_no_nonzero_projection',
     allOriginalRowsRetained=True,noNewFiniteLambdaCoverClaim=True)
elif cover.degree()==0:
 assert cover==one
 returns.append(dict(excluded=True,reason='whole original projection cover is one after only physical units'))
else:
 gg=cover.gcd(cover.derivative());sq,rr=divmod(cover,gg)
 assert not rr and sq*gg==cover
 cover=sq/sq[sq.degree()]
 unit,factors=cover.factor();back=P([unit])
 for f,m in factors:back*=f**int(m)
 assert back==cover
 for j,(f,m) in enumerate(factors):
  F=f/f[f.degree()]
  factor_records.append(dict(index=j,multiplicity=int(m),factor=pp(F)))
  say(stage='new_collision_u2_complete_QQ_lambda_factor',**factor_records[-1],
      entireOriginalLambdaFibreRetained=True)
  try:result=run_lambda_fibre(F,'lambda_'+str(j))
  except BaseNonunit as ex:
   result=dict(path='lambda_'+str(j),excluded=False,
               reason='actual QQ factor nonunit retained',nonunitFactor=pp(ex.g))
  returns.append(result)
  say(stage='new_collision_u2_entire_original_lambda_fibre_return',**result)
say(stage='new_collision_u2_original_fibre_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 necessaryLambdaCover=pp(cover),completeQQFactors=factor_records,
 originalFibreReturns=returns,
 entireOriginalCollisionUEqualsTwoExcluded=bool(returns) and all(r['excluded'] for r in returns),
 noUnpaidOriginalHeadOrGeometricFactorDeleted=True,
 noOldE37ProjectionOrQQHeadGateReplayed=True,
 coefficientPayloadPrintedOrStored=False,
 wholeCollisionExcluded=False,ordinaryISPClaim=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
