#!/usr/bin/env python3
"""NEW complete F66 constant lambda fibres of P25,3, retaining the same
original u and Q. Exact QQ factorization only of the saved 66-degree
input, not F1474 or any old generic Euclidean/projection gate.
Whole u algebra; all zero/nonunit heads split exactly. Original four
Q equations return one or a power of their already-paid physical product.
180 seconds /4 GiB. No sampling and no modular emptiness inference.
"""
import json,time,hashlib,signal,resource,zlib,base64
from pathlib import Path
from flint import fmpq,fmpq_poly
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
one=P([1]);lp=P([0,1])
f66=P(read('2026-11-28-unit211-collision-P3-exact-66-cover-8542.json',
 'd54fabefc3b1b646dca9350ed5a0bf9d884282bb67ec381337f45f4c20273ea8'))
assert f66.degree()==66 and f66[66]==1
assert digest(coeffs(f66))['sha256']=='77134be0755d744c136fd627db8b5cbc1e7ee38f419658dbb99736d518d1ee06'
content,factors=f66.factor();back=P([content])
for f,ex in factors:back*=f**int(ex)
assert back==f66
factor_records=[dict(degree=int(f.degree()),multiplicity=int(ex),
 coefficients=coeffs(f),**digest(coeffs(f))) for f,ex in factors]
say(stage='new_P3_complete_saved_F66_QQ_factorization',
     originalDegree=66,allQQFactors=factor_records,
     completeFactorProductActuallyReturned=True,
     noF1474OrOldEuclideanGateExecuted=True,wholeP3Excluded=False)
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
manifest=read('2026-11-28-unit211-collision-two-QQ-projections-exact-factor-manifest-8542.json',
 '4a2206f910408ec2ef7bc0a7cc49b24cefe556a226d5bfe66f4c0059d45abb54')
pr=next(r for r in manifest['factors'] if r['name']=='P25-3')
praw=zlib.decompress(base64.b64decode(pr['data']))
assert hashlib.sha256(praw).hexdigest()=='1414ec5c6010ddb33a6e0e471d9bb68dd7070535bfae59472d2948de453ab0ab'
pdata=json.loads(praw)
pgrid=[P() for _ in range(4)]
for (aa,bb,qq),cf in pdata['terms']:
 assert qq==0 and bb<=3
 pgrid[bb]+=fmpq(cf)*lp**aa
grids={}
for name,terms in original['polynomials'].items():
 mq=max(ex[2] for ex,c in terms);mu=max(ex[1] for ex,c in terms)
 grid=[[P() for _ in range(mu+1)] for _ in range(mq+1)]
 for (aa,bb,qq),cf in terms:grid[qq][bb]+=fmpq(cf)*lp**aa
 grids[name]=grid
class BaseNonunit(Exception):
 def __init__(self,g):self.g=g
class ENonunit(Exception):
 def __init__(self,g,q,why,paid=None):self.g=g;self.q=q;self.why=why;self.paid=paid
class PhysicalZero(Exception):
 def __init__(self,name):self.name=name
results=[];splits=[]
def run_fiber(F,label,hdata=None):
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
  a,b=U(a),U(b);assert b
  q=U();r=U(a);li=b.c[-1].inv()
  while r and r.degree()>=b.degree():
   shift=r.degree()-b.degree();cf=r.c[-1]*li
   term=U([K()]*shift+[cf]);q=q+term;r=r-term*b
  assert q*b+r==a and (not r or r.degree()<b.degree())
  return q,r
 def xg(a,b):
  a,b=U(a),U(b);r0,r1=a,b;s0,s1=U(1),U();t0,t1=U(),U(1)
  while r1:
   q,r=dr(r0,r1);r0,r1=r1,r;s0,s1=s1,s0-q*s1;t0,t1=t1,t0-q*t1
  if r0:
   iv=r0.c[-1].inv();r0=r0.scale(iv);s0=s0.scale(iv);t0=t0.scale(iv)
  assert s0*a+t0*b==r0
  return r0,s0,t0

 lk=K(lp)
 A2k=2*lk*lk-2*lk+1;B3k=4*lk**3-6*lk**2+3*lk-1
 scalar_units=[('lambda',lk),('A',A2k),('B',B3k),
   ('S_numerator',(2*lk-1)*(2*lk*lk-1)),('entire_J2',3*lk*lk-2*lk+1)]
 for name,v in scalar_units:
  if not v:raise PhysicalZero('published whole collision scalar '+name)
  assert v*v.inv()==1
 pu=U([K(c) for c in pgrid])
 assert pu,'P25,3 has no vertical lambda fibre'
 if pu.degree()==0:
  iv=pu.c[0].inv();assert pu.c[0]*iv==1
  return dict(path=label,lambdaModulus=coeffs(F),
    originalPCoefficientConstantUnitActuallyReturned=True,excluded=True)
 original_pu=U(pu)
 pu=pu.scale(pu.c[-1].inv())
 assert pu.scale(original_pu.c[-1])==original_pu
 H=pu if hdata is None else U([K(P(c)) for c in hdata])
 H=H.scale(H.c[-1].inv())
 qq,rr=dr(pu,H);assert not rr and qq*H==pu
 assert H.degree()>0 and H.c[-1]==1
 n=H.degree()
 class A:
  def __init__(self,v=0):
   if isinstance(v,A):self.c=v.c[:];return
   v=U(v);cc=v.c[:]
   for j in range(len(cc)-1,n-1,-1):
    lead=cc[j]
    if lead:
     for h in range(n):cc[j-n+h]=cc[j-n+h]-lead*H.c[h]
    cc[j]=K()
   assert not any(cc[n:]);self.c=cc[:n]+[K()]*(n-min(n,len(cc)))
  def __bool__(self):return any(self.c)
  def __neg__(self):return A([-c for c in self.c])
  def __add__(self,v):v=A(v);return A([a+b for a,b in zip(self.c,v.c)])
  __radd__=__add__
  def __sub__(self,v):return self+-A(v)
  def __rsub__(self,v):return A(v)+-self
  def __mul__(self,v):
   v=A(v);out=[K() for _ in range(2*n-1)]
   for i,a in enumerate(self.c):
    if not a:continue
    for j,b in enumerate(v.c):
     if b:out[i+j]=out[i+j]+a*b
   return A(out)
  __rmul__=__mul__
  def __eq__(self,v):return self.c==A(v).c
  def inv(self,why='actual original inverse',paid=None):
   nonlocal inverse_count
   if not self:
    if paid is not None:raise PhysicalZero(paid)
    raise ZeroDivisionError(why)
   g,s,t=xg(U(self.c),H)
   assert s*U(self.c)+t*H==g
   if g.degree()>0:
    q,r=dr(H,g);assert not r and q*g==H and 0<g.degree()<H.degree()
    raise ENonunit(g.data(),q.data(),why,paid)
   ans=A(s);assert self*ans==1;inverse_count+=1;return ans
  def __truediv__(self,v):return self*A(v).inv()
  def __rtruediv__(self,v):return A(v)*self.inv()
  def __pow__(self,n0):
   if n0<0:return self.inv()**(-n0)
   out=A(1);v=self
   while n0:
    if n0&1:out=out*v
    v=v*v;n0//=2
   return out
  def json(self):return [c.data() for c in self.c]

 def unit(name,v):
  v=A(v)
  if not v:raise PhysicalZero(name)
  vi=v.inv('published collision original unit '+name,paid=name)
  assert v*vi==1
 lam=A(lk);u=A([0,1]);A2=2*lam*lam-2*lam+1
 B3=4*lam**3-6*lam**2+3*lam-1
 xi=B3/A2;ell=A2**3/(B3**2)
 for name,v in [('u',u),('u-1',u-1),('u-ell',u-ell)]:unit(name,v)
 assert sum((A(K(c))*u**j for j,c in enumerate(pgrid)),A())==0
 say(stage='new_P3_entire_original_finite_lambda_u_algebra',
     path=label,lambdaDegree=int(F.degree()),uDegree=n,
     QQDimension=int(F.degree())*n,
     actualOriginalPRelationAndAllUsedWeightInversesReturned=True,
     allUHeadDropsRetained=True,noFieldAssumptionForUAlgebra=True)
 class Qpoly:
  def __init__(self,v=0):
   if isinstance(v,Qpoly):self.c=v.c[:];return
   self.c=[A(c) for c in v] if isinstance(v,(tuple,list)) else [A(v)]
   while self.c and not self.c[-1]:self.c.pop()
  def __bool__(self):return bool(self.c)
  def degree(self):return len(self.c)-1
  def __neg__(self):return Qpoly([-c for c in self.c])
  def __add__(self,v):
   v=Qpoly(v);n0=max(len(self.c),len(v.c))
   return Qpoly([(self.c[j] if j<len(self.c) else A())+(v.c[j] if j<len(v.c) else A()) for j in range(n0)])
  __radd__=__add__
  def __sub__(self,v):return self+-Qpoly(v)
  def __rsub__(self,v):return Qpoly(v)+-self
  def __mul__(self,v):
   v=Qpoly(v)
   if not self or not v:return Qpoly()
   out=[A() for _ in range(len(self.c)+len(v.c)-1)]
   for i,a in enumerate(self.c):
    for j,b in enumerate(v.c):out[i+j]=out[i+j]+a*b
   return Qpoly(out)
  __rmul__=__mul__
  def scale(self,v):return Qpoly([c*A(v) for c in self.c])
  def __pow__(self,j):
   assert j>=0
   out=Qpoly(1);v=self
   while j:
    if j&1:out=out*v
    v=v*v;j//=2
   return out
  def __eq__(self,v):return self.c==Qpoly(v).c
  def data(self):return [c.json() for c in self.c]
 def divQ(a,b,why):
  nonlocal division_count
  a,b=Qpoly(a),Qpoly(b);assert b
  original_a=Qpoly(a);iv=b.c[-1].inv(why+' actual Q head')
  quotient=[A() for _ in range(max(0,len(a.c)-len(b.c)+1))]
  while a and len(a.c)>=len(b.c):
   shift=len(a.c)-len(b.c);cf=a.c[-1]*iv
   quotient[shift]=quotient[shift]+cf
   row=a.c[:]
   for j,c in enumerate(b.c):row[shift+j]=row[shift+j]-cf*c
   a=Qpoly(row)
  q=Qpoly(quotient)
  assert q*b+a==original_a and a.degree()<b.degree()
  division_count+=1;return q,a
 values={name:Qpoly([A(U([K(c) for c in col])) for col in grid]) for name,grid in grids.items()}
 Q=Qpoly([0,1]);T0=Qpoly(2*u-2*u*u)-Q.scale(ell)
 J=Qpoly(2*u*(1-u))+Q.scale(ell)
 Phi=T0+4*u-4+Q
 S=2*xi+3-2*lam;eta=xi+3-2*lam
 NF=Q.scale(3-4*lam)+J.scale(xi*eta)
 Pf=T0*(J-Q)
 Delta=Phi*NF-Pf.scale(S*xi)
 M=Qpoly(2*ell*u-u*u)-Q.scale(ell*ell)
 V2=Qpoly(2*u)-Q.scale(ell)
 P02=V2.scale(2-3*u)-Q.scale(u)+2*u**3
 physical=Delta*Q*(1-Q)*M*P02*Phi*Pf
 # Every factor is already nonzero on the exact current collision chart:
 # Delta whole-zero exclusion; Q,1-Q,bc and P02 physical; M=4bc(1-Q);
 # Pf/Phi are paid explicitly in the published four-original-polynomial input.
 if not physical:
  return dict(path=label,lambdaModulus=coeffs(F),uModulus=H.data(),
     completePaidOriginalQProductIdenticallyZero=True,
     originalProduct='Delta*Q*(1-Q)*M*P02*Phi*Pf',excluded=True)
 current=Qpoly();tags={};used=[]
 for name in ['R','W','O','N1']:
  if not values[name]:continue
  if not current:
   iv=values[name].c[-1].inv('initial nonzero original Q row head')
   current=values[name].scale(iv);tags={name:Qpoly(iv)};used.append(name)
  else:
   a,b=current,values[name];ta=dict(tags);tb={name:Qpoly(1)}
   while b:
    q,r=divQ(a,b,'same original Q gcd')
    tr={key:ta.get(key,Qpoly())-q*tb.get(key,Qpoly()) for key in set(ta)|set(tb)}
    a,b=b,r;ta,tb=tb,tr
   iv=a.c[-1].inv('actual final original Q gcd head')
   current=a.scale(iv);tags={key:v.scale(iv) for key,v in ta.items() if v}
   used.append(name)
  assert sum((tags.get(key,Qpoly())*pp for key,pp in values.items()),Qpoly())==current
  say(stage='new_P3_same_lambda_u_complete_original_Q_gcd_return',
      path=label,originalRowsUsed=used,currentQDegree=current.degree(),
      completeOriginalRowCombinationActuallyMultipliedBack=True,
      actualQDivisionProducts=division_count)
  if current.degree()==0:
   assert current==Qpoly(1)
   cert=dict(lambdaModulus=coeffs(F),uModulus=H.data(),
        actualOriginalConstantOneCombination={key:vv.data() for key,vv in tags.items()})
   return dict(path=label,lambdaModulus=coeffs(F),uModulus=H.data(),
       lambdaDegree=int(F.degree()),uDegree=n,QQDimension=int(F.degree())*n,
       originalRowsUsed=used,commonQDegree=0,
       actualOriginalConstantOneReturned=True,
       actualOriginalCombinationReturned=True,
       actualQDivisionProducts=division_count,actualInverseProducts=inverse_count,
       certificate=digest(cert),excluded=True)
  if len(used)<2:continue
  targets=[('Delta',Delta),('paid_physical_product',physical)]
  for target_name,target in targets:
   q0,r0=divQ(target,current,'original '+target_name+' target')
   rem=Qpoly(1);chain=[]
   for exponent in range(1,7):
    rawrem=rem*r0;qstep,newrem=divQ(rawrem,current,'small original target power reduction')
    assert qstep*current+newrem==rawrem
    chain.append(digest([rem.data(),r0.data(),qstep.data(),newrem.data()]))
    rem=newrem
    if rem:continue
    cert=dict(lambdaModulus=coeffs(F),uModulus=H.data(),
       originalRowsUsed=used,currentQPolynomial=current.data(),
       actualOriginalGcdCombination={key:vv.data() for key,vv in tags.items()},
       originalTarget=target_name,targetPolynomial=target.data(),
       initialTargetDivision=[q0.data(),r0.data()],
       targetPower=exponent,actualPowerReductionChain=chain)
    return dict(path=label,lambdaModulus=coeffs(F),uModulus=H.data(),
       lambdaDegree=int(F.degree()),uDegree=n,QQDimension=int(F.degree())*n,
       originalRowsUsed=used,commonQDegree=current.degree(),
       actualOriginalCombinationReturned=True,target=target_name,targetPower=exponent,
       allPowerReductionProductsActuallyReturned=True,
       proofByCompositionOfOriginalGcdAndTargetDivisionIdentities=True,
       actualQDivisionProducts=division_count,actualInverseProducts=inverse_count,
       certificate=digest(cert),excluded=True)
 if not current:
  payload=dict(lambdaModulus=coeffs(F),uModulus=H.data(),
       allFourOriginalQPolynomialsIdenticallyZero=True,
       fullOriginalQFiberRetained=True)
 else:
  payload=dict(lambdaModulus=coeffs(F),uModulus=H.data(),
       remainingMonicOriginalQGcd=current.data(),
       originalGcdCombination={key:v.data() for key,v in tags.items()},
       originalTargetProduct=physical.data(),
       originalSameLambdaUQRequired=True)
 packed=json.dumps(payload,separators=(',',':')).encode()
 encoded=base64.b64encode(zlib.compress(packed,9)).decode()
 assert zlib.decompress(base64.b64decode(encoded))==packed
 chunks=[encoded[j:j+75000] for j in range(0,len(encoded),75000)]
 say(stage='new_P3_exact_unreturned_original_finite_fiber_payload',
     path=label,rawBytes=len(packed),rawSHA256=hashlib.sha256(packed).hexdigest(),
     base64Characters=len(encoded),chunks=len(chunks),wholeFiberRetained=True)
 for j,chunk in enumerate(chunks):say(stage='new_P3_exact_unreturned_original_finite_fiber_chunk',path=label,index=j,total=len(chunks),data=chunk)
 return dict(path=label,lambdaModulus=coeffs(F),uModulus=H.data(),
    originalRowsUsed=used,remainingQDegree=current.degree(),
    allOriginalConditionsRetained=True,noEmptinessOrNonmembershipInferred=True,
    actualQDivisionProducts=division_count,actualInverseProducts=inverse_count,
    exactRemainingPayload=digest(payload),excluded=False)
def process(F,label,hdata=None):
 t0=time.perf_counter()
 try:
  rec=run_fiber(F,label,hdata);rec['elapsedSeconds']=time.perf_counter()-t0
  results.append(rec);say(stage='new_P3_original_F66_whole_finite_fiber_return',**rec)
 except BaseNonunit as ex:
  q,r=divmod(F,ex.g);assert not r and q*ex.g==F and 0<ex.g.degree()<F.degree()
  rec=dict(path=label,lambdaFactor=coeffs(ex.g),lambdaComplement=coeffs(q),
       actualFactorProductVerified=True,bothOriginalFibersRetained=True)
  splits.append(rec);say(stage='new_P3_actual_lambda_nonunit_split',**rec)
  process(ex.g,label+'/la',hdata);process(q,label+'/lb',hdata)
 except ENonunit as ex:
  rec=dict(path=label,uFactor=ex.g,uComplement=ex.q,reason=ex.why,
       originalPaidUnitOnFirstFactor=ex.paid,
       completeOriginalPFactorProductVerified=True,bothOriginalFibersRetained=True)
  splits.append(rec);say(stage='new_P3_actual_u_nonunit_complete_split',**rec)
  if ex.paid is not None:
   done=dict(path=label+'/ua',lambdaModulus=coeffs(F),uModulus=ex.g,
        originalPaidUnitIdenticallyZero=ex.paid,
        actualOriginalGcdProductVerified=True,excluded=True)
   results.append(done);say(stage='new_P3_named_original_unit_zero_entire_component',**done)
  else:process(F,label+'/ua',ex.g)
  process(F,label+'/ub',ex.q)
 except PhysicalZero as ex:
  rec=dict(path=label,lambdaModulus=coeffs(F),uModulus=hdata,
       originalPaidUnitIdenticallyZero=ex.name,excluded=True)
  results.append(rec);say(stage='new_P3_named_original_unit_zero_entire_component',**rec)
for j,(factor,mul) in enumerate(factors):
 process(factor,'lambda_'+str(j))
closed=bool(results) and all(r['excluded'] for r in results)
signal.alarm(0)
say(stage='new_complete_original_P3_F66_finite_return_finished',
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    completeOriginalF66QQFactors=factor_records,
    allActualLambdaAndUFactorSplits=splits,allOriginalFiniteReturns=results,
    wholeP3OriginalCurveExcluded=closed,
    allOriginalQLeadingZeroFibersRetained=True,
    actualUHeadDropsPreserved=True,noPhysicalDInverse=True,
    noF1474OrGenericEuclideanGateReplayed=True,
    residualTwoBaseCurvesStillRequireTheirOriginalReturn=True,
    wholeCollisionExcluded=False,ordinaryISPClaim=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
