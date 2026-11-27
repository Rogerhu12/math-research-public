#!/usr/bin/env python3
"""NEW original u-leading fibres and finite-u lambda-infinity coefficients
of the two saved collision E curves. No full u-resultant or previous Q
projection is repeated. Factor complete original heads over QQ, preserve
every zero fibre, and return full original u gcd combinations there.
Only published physical u and u-1 units may be removed. 120s / 1GiB.
The lambda-infinity calculation is only the stated biprojective boundary;
it says nothing about the simultaneous u-infinity corner."""
import json,time,hashlib,zlib,base64,signal,resource,math
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx
started=time.perf_counter()
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**v):
 v.update(stage=stage,seconds=time.perf_counter()-started)
 print(json.dumps(v,separators=(',',':')),flush=True)
def read(name,sha):
 raw=Path(__file__).with_name(name).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==sha
 return json.loads(raw)
def coeffs(p):return [str(c) for c in p.coeffs()]
def pprofile(p):
 raw=json.dumps(coeffs(p),separators=(',',':')).encode()
 return dict(degree=int(p.degree()),bytes=len(raw),
             sha256=hashlib.sha256(raw).hexdigest())
def checkpoint(label,obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 enc=base64.b64encode(zlib.compress(raw,9)).decode()
 assert zlib.decompress(base64.b64decode(enc))==raw
 chunks=[enc[j:j+75000] for j in range(0,len(enc),75000)]
 say('new_collision_E_u_head_exact_input',label=label,
     bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),
     base64Characters=len(enc),chunks=len(chunks),
     encoding='base64+zlib+json',maximumChunkCharacters=75000)
 for j,ch in enumerate(chunks):
  say('new_collision_E_u_head_exact_input_chunk',
      label=label,index=j,total=len(chunks),data=ch)
ctx=fmpq_mpoly_ctx.get(('lambda','u'),'lex')
manifest=read('2026-11-28-unit211-collision-two-QQ-projections-exact-factor-manifest-8542.json',
 '4a2206f910408ec2ef7bc0a7cc49b24cefe556a226d5bfe66f4c0059d45abb54')
polys=[];scales=[]
for name,expected in [('E177-18',[177,18]),('E182-19',[182,19])]:
 item=next(x for x in manifest['factors'] if x['name']==name)
 chunks=[read(p['filename'],p['sha256'])['dataChunk'] for p in item['parts']]
 enc=''.join(chunks)
 assert hashlib.sha256(enc.encode()).hexdigest()==item['encodedDataSHA256']
 raw=zlib.decompress(base64.b64decode(enc))
 assert len(raw)==item['payloadBytes']
 assert hashlib.sha256(raw).hexdigest()==item['payloadSHA256']
 obj=json.loads(raw);assert obj['variables']==['lambda','u','Q']
 dd={}
 for (a,b,q),c in obj['terms']:
  assert q==0 and (a,b) not in dd
  dd[(a,b)]=fmpq(c)
 original=ctx.from_dict(dd)
 assert list(map(int,original.degrees()))==expected
 den=1
 for c in dd.values():den=math.lcm(den,int(c.denominator))
 ints={e:int(c*den) for e,c in dd.items()}
 content=0
 for c in ints.values():content=math.gcd(content,abs(c))
 assert content
 integer=ctx.from_dict({e:c//content for e,c in ints.items()})
 assert integer*fmpq(content,den)==original
 polys.append(integer);scales.append(dict(name=name,denominator=den,content=content))
 say('new_collision_E_head_original_saved_curve_loaded',
     name=name,degrees=expected,terms=len(dd),
     originalPayloadSHA256=item['payloadSHA256'],
     completePrimitiveIntegerInputProductReturned=True,
     noPriorProjectionReconstruction=True)
def digest(obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def monic(p):
 assert p
 return p/p[p.degree()]
def uni_from_dict(dd,index,other_power):
 vals={int(e[index]):c for e,c in dd.items() if int(e[1-index])==other_power}
 out=fmpq_poly([0]*(max(vals,default=0)+1))
 for j,c in vals.items():out[j]=c
 return out
x=fmpq_poly([0,1])
units=[
 ('original lambda',x),
 ('original A',2*x*x-2*x+1),
 ('original B',4*x**3-6*x*x+3*x-1),
 ('original S first factor',2*x-1),
 ('original S second factor',2*x*x-1),
 ('complete original J2 fibre excluded',3*x*x-2*x+1),
 ('complete original G2 fibre excluded',x*x+x-1),
 ('complete original C4 fibre excluded',8*x**4-24*x**3+24*x*x-12*x+3)]
heads=[];all_factors=[];head_records=[]
for i,p in enumerate(polys):
 du=int(p.degrees()[1]);head=uni_from_dict(p.to_dict(),0,du)
 assert head
 c,fs=head.factor()
 product=fmpq_poly([c]);records=[]
 for fac,mul in fs:
  product*=fac**mul;f=monic(fac)
  paid=[name for name,unit in units if not (unit%f)]
  rec=dict(lambdaPolynomialAscending=coeffs(f),degree=int(f.degree()),
           multiplicity=int(mul),alreadyPaidOriginalUnits=paid)
  records.append(rec)
  if not paid and not any(f==g for g in all_factors):all_factors.append(f)
 assert product==head
 heads.append(head)
 rec=dict(curveIndex=i,originalUDegree=du,completeUHead=pprofile(head),
          headCoefficientsAscending=coeffs(head),allQQFactors=records,
          completeFactorProductActuallyReturned=True,
          everyUnpaidWholeLambdaFibreRetained=True)
 head_records.append(rec)
 say('new_collision_E_complete_original_u_head_factorization',**rec)
checkpoint('complete_original_u_head_polynomials_and_unpaid_factors',
 dict(variable='lambda',heads=[coeffs(h) for h in heads],
      unpaidDistinctFactors=[coeffs(f) for f in all_factors],
      factorRecords=head_records,
      allUnpaidOriginalHeadZeroFibresRetained=True))
# Highest lambda coefficients at finite u. This is not total-degree homogenization.
inf=[]
for i,p in enumerate(polys):
 dl=int(p.degrees()[0]);h=uni_from_dict(p.to_dict(),1,dl)
 assert h
 c,fs=h.factor();prod=fmpq_poly([c])
 for f,m in fs:prod*=f**m
 assert prod==h
 inf.append(h)
 say('new_collision_E_lambda_infinity_finite_u_coefficient',
     curveIndex=i,originalLambdaDegree=dl,uCoefficientAscending=coeffs(h),
     completeQQFactorization=[
      dict(coefficientsAscending=coeffs(monic(f)),multiplicity=int(m)) for f,m in fs],
     completeFactorProductActuallyReturned=True,
     noClaimAboutSimultaneousLambdaAndUInfinity=True)
ig,ia,ib=inf[0].xgcd(inf[1])
assert ia*inf[0]+ib*inf[1]==ig
say('new_collision_E_finite_u_lambda_infinity_original_combination',
    gcdCoefficientsAscending=coeffs(ig),
    firstMultiplierAscending=coeffs(ia),secondMultiplierAscending=coeffs(ib),
    completeOriginalCombinationActuallyReturned=True,
    affineLambdaCollisionNotExcludedByThisBoundaryCalculation=True,
    simultaneousUInfinityNotHandled=True)
checkpoint('finite_u_lambda_infinity_original_coefficient_combination',
 dict(variable='u',first=coeffs(inf[0]),second=coeffs(inf[1]),
      gcd=coeffs(ig),firstMultiplier=coeffs(ia),secondMultiplier=coeffs(ib),
      scope='only lambda infinity with finite u; not the simultaneous infinity corner'))
# Only new unpaid original u-head zero fibres are visited below.
egrids=[]
for p in polys:
 grid=[fmpq_poly() for _ in range(int(p.degrees()[1])+1)]
 for (a,b),c in p.to_dict().items():grid[int(b)][int(a)]=c
 egrids.append(grid)
class BaseNonunit(Exception):
 def __init__(self,g):self.g=g
results=[]
def run_fibre(F,label):
 assert F==monic(F) and F.gcd(F.derivative()).degree()==0
 inverse_count=0;division_count=0
 class K:
  def __init__(self,v=0):
   if isinstance(v,K):self.p=v.p;return
   self.p=(v if isinstance(v,fmpq_poly) else fmpq_poly([v]))%F
  def __bool__(self):return bool(self.p)
  def __eq__(self,v):return self.p==K(v).p
  def __neg__(self):return K(-self.p)
  def __add__(self,v):return K(self.p+K(v).p)
  __radd__=__add__
  def __sub__(self,v):return self+-K(v)
  def __rsub__(self,v):return K(v)+-self
  def __mul__(self,v):return K(self.p*K(v).p)
  __rmul__=__mul__
  def inv(self):
   nonlocal inverse_count
   assert self
   g,s,t=self.p.xgcd(F);assert s*self.p+t*F==g
   if g.degree()>0:raise BaseNonunit(monic(g))
   ans=K(s/g[0]);assert self*ans==1
   inverse_count+=1;return ans
  def data(self):return coeffs(self.p)
 class U:
  def __init__(self,v=()):
   if isinstance(v,U):self.c=v.c[:];return
   if isinstance(v,(K,int,fmpq)):v=[v]
   self.c=[K(z) for z in v]
   while self.c and not self.c[-1]:self.c.pop()
  def __bool__(self):return bool(self.c)
  def degree(self):return len(self.c)-1
  def __eq__(self,v):return self.c==U(v).c
  def __neg__(self):return U([-a for a in self.c])
  def __add__(self,v):
   v=U(v);n=max(len(self.c),len(v.c))
   return U([(self.c[j] if j<len(self.c) else K())+
             (v.c[j] if j<len(v.c) else K()) for j in range(n)])
  __radd__=__add__
  def __sub__(self,v):return self+-U(v)
  def __rsub__(self,v):return U(v)+-self
  def __mul__(self,v):
   v=U(v)
   if not self or not v:return U()
   out=[K() for _ in range(len(self.c)+len(v.c)-1)]
   for i,a in enumerate(self.c):
    for j,b in enumerate(v.c):out[i+j]=out[i+j]+a*b
   return U(out)
  __rmul__=__mul__
  def scale(self,v):return U([a*K(v) for a in self.c])
  def data(self):return [a.data() for a in self.c]
 def dr(a,b):
  nonlocal division_count
  a,b=U(a),U(b);assert b
  q=U();r=U(a);li=b.c[-1].inv()
  while r and r.degree()>=b.degree():
   j=r.degree()-b.degree();v=r.c[-1]*li
   t=U([K()]*j+[v]);q=q+t;r=r-t*b
  assert q*b+r==a and (not r or r.degree()<b.degree())
  division_count+=1;return q,r
 def xg(a,b):
  a,b=U(a),U(b)
  r0,r1=a,b;s0,s1=U(1),U();t0,t1=U(),U(1)
  while r1:
   q,r=dr(r0,r1)
   r0,r1=r1,r;s0,s1=s1,s0-q*s1;t0,t1=t1,t0-q*t1
  if r0:
   iv=r0.c[-1].inv();r0=r0.scale(iv);s0=s0.scale(iv);t0=t0.scale(iv)
  assert s0*a+t0*b==r0
  return r0,s0,t0
 ea,eb=[U([K(c) for c in grid]) for grid in egrids]
 assert ea or eb
 g,sa,sb=xg(ea,eb)
 assert g and sa*ea+sb*eb==g and g.c[-1]==1
 cert=dict(lambdaModulus=coeffs(F),firstOriginalCurve=ea.data(),
           secondOriginalCurve=eb.data(),gcd=g.data(),
           firstMultiplier=sa.data(),secondMultiplier=sb.data())
 say('new_collision_E_original_u_head_whole_fibre_gcd',
     path=label,lambdaDegree=int(F.degree()),
     actualOriginalUDegrees=[ea.degree(),eb.degree()],
     monicUGcdDegree=g.degree(),
     completeOriginalCombinationActuallyReturned=True,
     entireUHeadDropsPreserved=True,certificate=digest(cert))
 remaining=U(g);product=U(1);removed=[]
 for name,unit in [('original u',U([0,1])),('original u-1',U([-1,1]))]:
  m=0
  while remaining.degree()>0:
   q,r=dr(remaining,unit)
   if r:break
   assert q*unit==remaining
   remaining=q;product=product*unit;m+=1
  if m:removed.append(dict(originalPaidUnit=name,multiplicity=m))
 assert product*remaining==g
 excluded=remaining==U(1)
 rec=dict(path=label,lambdaModulus=coeffs(F),
          originalUDegrees=[ea.degree(),eb.degree()],
          originalMonicUGcdDegree=g.degree(),
          removedOnlyOriginalPhysicalUUnits=removed,
          exactFactorProductActuallyReturned=True,
          remainingOriginalMonicUDegree=remaining.degree(),
          excluded=excluded,actualInverseProducts=inverse_count,
          actualDivisionProducts=division_count,certificate=digest(cert),
          allOriginalQAndValueConditionsStillRequiredIfNotExcluded=True)
 if not excluded:
  payload=dict(lambdaModulus=coeffs(F),remainingMonicU=remaining.data(),
               originalUGcd=g.data(),physicalRemoved=removed,
               sameOriginalLambdaAndU=True,allQAndValueFibresRetained=True)
  checkpoint('unreturned_original_u_head_fibre_'+label,payload)
  rec['remainingExactParameter']=digest(payload)
 say('new_collision_E_original_u_head_fibre_return',**rec)
 return rec
for j,F in enumerate(all_factors):
 try:results.append(run_fibre(F,'head_factor_'+str(j)))
 except BaseNonunit as ex:
  quotient,remainder=divmod(F,ex.g)
  assert not remainder and quotient*ex.g==F
  rec=dict(path='head_factor_'+str(j),lambdaModulus=coeffs(F),
           nonunitFactor=coeffs(ex.g),complement=coeffs(quotient),
           completeOriginalFactorProductReturned=True,
           entireUnreturnedLambdaFibreRetained=True,excluded=False)
  results.append(rec)
  say('new_collision_E_u_head_actual_nonunit_retained',**rec)
closed=all(r['excluded'] for r in results)
say('new_collision_E_original_u_heads_and_infinity_attempt_finished',
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    distinctUnpaidOriginalHeadFactors=len(all_factors),
    allOriginalHeadFactorRecords=head_records,wholeFibreReturns=results,
    allCurrentOriginalUHeadZeroFibresExcluded=closed,
    noPriorFullUResultantOrQProjectionOrCompletedHeadGateReplayed=True,
    originalFiniteFiveCoordinateBound=235170,
    noUnpaidHeadOrGeometryOrPhysicalDInverse=True,
    remainingEIntersectionStillNeedsAllOriginalConditions=True,
    wholeCollisionExcluded=False,ordinaryISPClaim=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
