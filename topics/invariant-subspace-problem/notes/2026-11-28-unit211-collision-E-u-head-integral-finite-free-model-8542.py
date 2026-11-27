#!/usr/bin/env python3
"""NEW finite-free integral models of the two unpaid original u-head fibres.
The first successful prime is chosen only by integral coefficients and the
OTHER original u-head being a unit, before any common-root computation.
Every lambda residue factor and its multiplicity is retained. Complete
original u-Bezout identities in all residue fields lift through the entire
finite-free Z_(p) model. No physical u localization is used in the lift.
No QQ u-Euclid, projection gate, or original Q gate is replayed.
Historical original E inputs are read only from Actions temporary files.
Only small definitions, profiles, and hashes are printed. 120s /1GiB.
"""
import json,time,hashlib,zlib,base64,signal,resource,math
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx,nmod_poly
started=time.perf_counter();signal.alarm(120)
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
def qprofile(p):
 return dict(degree=int(p.degree()),**digest(coeffs(p)))
def ncoeff(p):return [int(c) for c in p.coeffs()]
def nprofile(p):return dict(degree=int(p.degree()),**digest(ncoeff(p)))
def monic(p):return p/p[p.degree()]
x=fmpq_poly([0,1]);B=4*x**3-6*x*x+3*x-1
grids=[];heads=[];head_factors=[]
for i,pol in enumerate(polys):
 du=int(pol.degrees()[1])
 cols=[fmpq_poly() for _ in range(du+1)]
 for (a,b),c in pol.to_dict().items():cols[int(b)]+=c*x**int(a)
 head=cols[-1];quot,rem=divmod(head,B**5)
 assert not rem and quot*B**5==head
 F=monic(quot)
 assert int(F.degree())==[162,167][i]
 assert F*quot[quot.degree()]*B**5==head
 grids.append(cols);heads.append(head);head_factors.append(F)
 say('new_E_integral_model_original_head_definition',
     curve=i,originalUDegree=du,
     definition='monic([u^degree]E / B^5), B=4*lambda^3-6*lambda^2+3*lambda-1',
     factor=qprofile(F),originalHeadProductReturned=True,
     originalUnpaidWholeHeadRetained=True)
PRIMES=(1009,1013,1019,1021,1031)
def reduceq(poly,p):
 vals=[]
 for c in poly.coeffs():
  den=int(c.denominator)%p
  if not den:return None
  vals.append((int(c.numerator)%p)*pow(den,-1,p)%p)
 return nmod_poly(vals,p)

def residue_return(modulus,first,second,p,label):
 inverse_count=0;division_count=0
 class K:
  def __init__(self,v=0):
   if isinstance(v,K):self.p=v.p;return
   if not isinstance(v,nmod_poly):v=nmod_poly([int(v)%p],p)
   q,r=divmod(v,modulus)
   assert q*modulus+r==v
   self.p=r
  def __bool__(self):return bool(self.p)
  def __eq__(self,v):return self.p==K(v).p
  def __neg__(self):return K(-self.p)
  def __add__(self,v):return K(self.p+K(v).p)
  __radd__=__add__
  def __sub__(self,v):return K(self.p-K(v).p)
  def __rsub__(self,v):return K(v)-self
  def __mul__(self,v):return K(self.p*K(v).p)
  __rmul__=__mul__
  def inv(self):
   nonlocal inverse_count
   assert self
   g,s,t=self.p.xgcd(modulus)
   assert s*self.p+t*modulus==g and g.degree()==0
   gi=pow(int(g[0]),-1,p)
   answer=K(s*gi)
   assert self*answer==1
   inverse_count+=1
   return answer
  def data(self):return ncoeff(self.p)
 class U:
  def __init__(self,v=()):
   if isinstance(v,U):self.c=v.c[:];return
   if isinstance(v,(K,int)):v=[v]
   self.c=[K(z) for z in v]
   while self.c and not self.c[-1]:self.c.pop()
  def __bool__(self):return bool(self.c)
  def __eq__(self,v):return self.c==U(v).c
  def degree(self):return len(self.c)-1
  def __neg__(self):return U([-z for z in self.c])
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
  def scale(self,v):return U([z*K(v) for z in self.c])
  def data(self):return [z.data() for z in self.c]
 def dr(a,b):
  nonlocal division_count
  a,b=U(a),U(b);assert b
  q=U();r=U(a);iv=b.c[-1].inv()
  while r and r.degree()>=b.degree():
   shift=r.degree()-b.degree();cf=r.c[-1]*iv
   term=U([K()]*shift+[cf]);q=q+term;r=r-term*b
  assert q*b+r==a and (not r or r.degree()<b.degree())
  division_count+=1
  return q,r
 aa=U([K(c) for c in first]);bb=U([K(c) for c in second])
 r0,r1=aa,bb;s0,s1=U(1),U();t0,t1=U(),U(1)
 degree_trace=[]
 while r1:
  q,r=dr(r0,r1);r0,r1=r1,r;s0,s1=s1,s0-q*s1;t0,t1=t1,t0-q*t1
  degree_trace.append(r1.degree())
 assert r0
 iv=r0.c[-1].inv();r0=r0.scale(iv);s0=s0.scale(iv);t0=t0.scale(iv)
 assert s0*aa+t0*bb==r0
 certificate=dict(lambdaModulus=ncoeff(modulus),uGcd=r0.data(),
                  firstBezout=s0.data(),secondBezout=t0.data())
 record=dict(path=label,lambdaResidueDegree=int(modulus.degree()),
     originalUDegreesAfterReduction=[aa.degree(),bb.degree()],
     completeOriginalUGcdDegree=r0.degree(),uRemainderDegrees=degree_trace,
     completeOriginalBezoutActuallyMultipliedBack=True,
     actualInverseProducts=inverse_count,actualDivisionProducts=division_count,
     certificate=digest(certificate),unitReturned=(r0==U(1)),
     noUOrUMinusOneLocalization=True)
 say('new_E_integral_model_complete_residue_u_return',**record)
 return record

all_returns=[]
for i,F in enumerate(head_factors):
 chosen=None;eligibility=[]
 for p in PRIMES:
  fp=reduceq(F,p)
  if fp is None:
   eligibility.append(dict(prime=p,integralMonicFactor=False))
   continue
  assert int(fp.degree())==int(F.degree()) and int(fp[fp.degree()])==1
  other=reduceq(heads[1-i],p)
  assert other is not None
  gd,s,t=other.xgcd(fp)
  assert s*other+t*fp==gd
  ok=gd.degree()==0
  record=dict(prime=p,integralMonicFactor=True,
              otherOriginalUHeadUnitInWholeReduction=ok,
              otherHeadGcdDegree=int(gd.degree()))
  eligibility.append(record)
  if not ok:continue
  inv=s*pow(int(gd[0]),-1,p)
  q,r=divmod(inv*other,fp)
  assert q*fp+r==inv*other and r==nmod_poly([1],p)
  chosen=(p,fp,dict(record,actualWholeHeadInverseReturned=True,
       unitCertificate=digest([ncoeff(fp),ncoeff(other),ncoeff(inv),ncoeff(q)])))
  break
 if chosen is None:
  record=dict(curve=i,factorDegree=int(F.degree()),
       eligibility=eligibility,integralModelReturned=False,
       originalWholeHeadExcluded=False,entireUnreturnedFibreRetained=True)
  all_returns.append(record)
  say('new_E_integral_model_unavailable',**record)
  continue
 p,fp,headunit=chosen
 other_degree=len(grids[1-i])-1
 say('new_E_integral_model_whole_finite_free_environment',
     curve=i,prime=p,eligibility=eligibility,
     originalOtherUDegree=other_degree,
     finiteFreeRank=int(F.degree())*other_degree,
     chosenBeforeAnyCommonRootOrUGcdCalculation=True,
     monicLambdaIntegral=True,wholeOriginalOtherUHeadUnit=headunit,
     noPhysicalGeometricLocalizationUsed=True)
 nc,ff=fp.factor();product=nmod_poly([int(nc)],p)
 factors=[]
 for fac,mul in ff:
  product*=fac**int(mul);factors.append((fac,int(mul)))
 assert product==fp
 say('new_E_integral_model_complete_lambda_residue_factorization',
     curve=i,prime=p,
     factors=[dict(degree=int(f.degree()),multiplicity=m,profile=nprofile(f))
              for f,m in factors],
     completeFactorProductReturned=True,allPrimaryMultiplicitiesRetained=True)
 reduced=[[reduceq(c,p) for c in row] for row in grids]
 assert all(c is not None for row in reduced for c in row)
 blocks=[]
 for j,(fac,mul) in enumerate(factors):
  rec=residue_return(fac,reduced[0],reduced[1],p,'F'+str(int(F.degree()))+'/residue'+str(j))
  rec['primaryMultiplicity']=mul;blocks.append(rec)
 passed=all(r['unitReturned'] for r in blocks)
 record=dict(curve=i,factorDegree=int(F.degree()),prime=p,
     integralFiniteFreeRank=int(F.degree())*other_degree,
     completeResidueBlockReturns=blocks,
     everyOriginalResidueUnitReturned=passed,
     fullNilpotentPrimaryLiftApplicable=passed,
     finiteFreeDeterminantOrNakayamaLiftApplicable=passed,
     entireCharacteristicZeroOriginalHeadExcluded=passed,
     noPhysicalUOrOtherAdditionalLocalization=True,
     anyUnreturnedResidueRetained=not passed)
 all_returns.append(record)
 say('new_E_integral_model_whole_original_head_result',**record)
say('new_E_integral_model_finished',
     sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     allOriginalHeadResults=all_returns,
     bothWholeOriginalUHeadsExcluded=all(r.get('entireCharacteristicZeroOriginalHeadExcluded',False) for r in all_returns),
     noQQHeadFibreGateOrFixedSylvesterProjectionReplayed=True,
     noCoefficientPayloadPrintedOrStored=True,
     remainingAffineIntersectionStillRequiresAllOriginalQConditions=True,
     wholeCollisionExcluded=False,ordinaryISPClaim=False,
     peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
