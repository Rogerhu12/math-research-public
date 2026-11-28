#!/usr/bin/env python3
"""NEW h=k, ell=1/2: Cramer cubic parameters and WHOLE six-dimensional
constant fields, followed by a NEW same-Q original eight-row saturation.
Only the old raw-Gram DEFINITION prefix is loaded. No old normalization,
five Sylvester targets, accumulated u-gcd, or degree-24 norm is rerun.
All embeddings, original Q leading-zero fibres, and unexcluded components
are retained. 180 seconds / 4 GiB. No coefficient payload or cache.
"""
import ast,hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq,fmpq_poly
START=time.perf_counter();DEADLINE=START+180
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
signal.setitimer(signal.ITIMER_REAL,180)
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 180 second boundary')
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(',',':')),flush=True)
NEW=dict(newCramerPolynomialIdentities=0,parameterIdentityChecks=0,
         polynomialDivisionReturns=0,polynomialBezoutReturns=0,
         sixCoordinateInverseReturns=0,fullPaidPrimaryProducts=0,
         originalEightSourceReturns=0)
DEP='2026-11-28-unit211-hk-entire-ell-half-constant-field-scaled-original-Q-cofactors-8542.py'
DEPSHA='44b7c44c5e4ba5408a8662e6f2579be23c6bf9effd0d9d2a59993eb827ca79cb'
PREFIXSHA='45b9c4dfe94dddfbf2c7118dcf9ca65df0ce8ab163cd80147bc0b8e4cb2fdd86'
G12SHA='3714806312a65901fa4cee34d459124cc7ef1cf4d5c10d72faee853fd7f375e7'
F6SHA='0f8be1fab30e5fc1be7583839d9ce4161bbcd071fb7e4a4b750936713626ba7d'
oldpath=Path(__file__).with_name(DEP)
oldbytes=oldpath.read_bytes()
assert hashlib.sha256(oldbytes).hexdigest()==DEPSHA
oldtext=oldbytes.decode()
prefix=oldtext.split("\npaid=[('u',u),",1)[0]
assert len(prefix.encode())==10525
assert hashlib.sha256(prefix.encode()).hexdigest()==PREFIXSHA
tree=ast.parse(prefix)
kept=[];removed=[]
for node in tree.body:
 # Only remove old TOP-LEVEL proof/log/resource statements, not arithmetic
 # checks inside the retained CP/DD/EE definitions.
 if isinstance(node,ast.Assert):
  removed.append('old top-level assertion');continue
 if isinstance(node,ast.FunctionDef) and node.name in ('tick','say'):
  removed.append('old clock/log definition');continue
 if isinstance(node,ast.Assign):
  targets=[t.id for t in node.targets if isinstance(t,ast.Name)]
  if any(t in ('START','DEADLINE','REAL_TIMER') for t in targets):
   removed.append('old clock assignment');continue
 if isinstance(node,ast.AugAssign) and isinstance(node.target,ast.Subscript):
  if isinstance(node.target.value,ast.Name) and node.target.value.id=='stats':
   removed.append('old top-level statistic');continue
 if isinstance(node,ast.Expr) and isinstance(node.value,ast.Call):
  fun=node.value.func
  if ((isinstance(fun,ast.Name) and fun.id in ('say','REAL_TIMER')) or
      (isinstance(fun,ast.Attribute) and isinstance(fun.value,ast.Name)
       and fun.value.id=='resource' and fun.attr=='setrlimit')):
   removed.append('old log/resource call');continue
 kept.append(node)
newtree=ast.Module(body=kept,type_ignores=[])
ns={'__name__':'necessary_raw_Gram_definition','__file__':str(oldpath),
    'tick':tick,'say':lambda *args,**kw:None}
exec(compile(ast.fix_missing_locations(newtree),str(oldpath)+':raw-definition','exec'),ns)
CP=ns['CP'];DD=ns['DD'];profile=ns['profile'];lead=ns['lead']
lam=ns['lam'];u=ns['u'];Q=ns['Q'];delta=ns['delta']
M=ns['M'];Delta=ns['Delta'];Tnum=ns['Tnum']
raw=ns['raw'];names=ns['names'];homogeneity=ns['homogeneity']
assert len(raw)==8 and len(names)==8
assert not any(n=='fixed_q_cofactor' for n in ns)
say('new_original_eight_rows_definition_only',
 dependencySHA256=DEPSHA,prefixBytes=10525,prefixSHA256=PREFIXSHA,
 originalNames=names,homogeneityPowers=homogeneity,
 oldTopLevelStatementsRemoved=len(removed),
 noOldNormalizationOrFiveCofactorsOrUBezoutOrNorm24=True,
 noOldMathematicalTargetReexecuted=True)

# NEW short Cramer base-point identities: no inverse of Z or of any Q head.
e=u-1
C=(2*u-13)+(56-19*u)*lam
Z=(25*u-41)+(52-35*u)*lam
Aq=4-5*lam
Bq=(29*u-27)+(39-46*u)*lam
Cq=-u-9+(2*u+15)*lam
r=4*u*e*C
LQ=Q*Z-r
H3=2*u*Aq*C*C-Bq*C*Z+Cq*Z*Z
assert 3*Delta==Aq*Q*Q-2*e*Bq*Q+8*u*e*e*Cq
assert 3*Tnum==M*Q*LQ
assert Z*Z*(3*Delta)-(Aq*Z*Q+Aq*r-2*e*Bq*Z)*LQ==8*u*e*e*H3
NEW['newCramerPolynomialIdentities']+=3
assert H3.degree(1)==0 and H3.degree(0)==3
h3=H3/lead(H3)
assert lead(h3)==1
hbar=h3.conj()
norm=h3.norm()
assert norm and all(int(mm[1])==0 for mm in norm.to_dict())
np=fmpq_poly([norm.to_dict().get((j,0),fmpq(0))
              for j in range(int(norm.degrees()[0])+1)])
scalar,factors=np.factor()
back=fmpq_poly([scalar]);factorinfo=[]
for ff,exponent in factors:
 back*=ff**int(exponent)
 encoded=json.dumps([str(c) for c in ff],separators=(',',':')).encode()
 factorinfo.append(dict(degree=int(ff.degree()),multiplicity=int(exponent),
                        bytes=len(encoded),sha256=hashlib.sha256(encoded).hexdigest()))
assert back==np
norm_is_the_known_irreducible=(len(factorinfo)==1 and factorinfo[0]['degree']==6
 and factorinfo[0]['multiplicity']==1 and factorinfo[0]['sha256']==F6SHA)
matches=[]
for j in range(5):
 candidate=h3**j*hbar**(4-j)
 if profile(candidate)['sha256']==G12SHA:matches.append(j)
say('new_Cramer_cubic_and_existing_parameter_identity',
 threeNewPolynomialIdentitiesReturned=True,noNewHeadInverse=True,
 CramerCubic=profile(h3),conjugateCubic=profile(hbar),
 newNormDegree=int(np.degree()),newNormFactors=factorinfo,
 wholeNewNormFactorProductReturned=True,
 matchesExistingG12AtExponents=matches,
 expectedInterpretation='g12=h3^j conjugate(h3)^(4-j)',
 existingG12SHA256=G12SHA,existingIrreducibleF6SHA256=F6SHA,
 allCramerHeadZZeroFibresRetained=True,
 noClaimH3AlreadyInOriginalIdeal=True,
 newNormUsedOnlyToProveWholeConstantField=True)
if not norm_is_the_known_irreducible or len(matches)!=1:
 say('new_constant_parameter_recognition_incomplete',
     completeNewNormFactorsRetained=factorinfo,
     noConstantRootOrComponentSelected=True,
     noOldCofactorOrGCDReplayed=True,entireHalfWeightExcluded=False)
 signal.setitimer(signal.ITIMER_REAL,0)
 raise SystemExit(0)
j=matches[0]
NEW['parameterIdentityChecks']+=2
# The irreducible degree-six norm proves BOTH cubic algebras are fields
# over the whole K2. We never select one lambda or u embedding.
assert h3!=hbar
components=[]
if j:components.append(('Cramer_cubic',h3,j))
if 4-j:components.append(('conjugate_Cramer_cubic',hbar,4-j))

def PolynomialRing(Coeff):
 class Poly:
  _level=3
  def __init__(self,v=0):
   if isinstance(v,Poly):self.c=v.c[:];return
   if isinstance(v,(list,tuple)):self.c=[Coeff(x) for x in v]
   else:self.c=[Coeff(v)]
   while self.c and not self.c[-1]:self.c.pop()
  def __bool__(self):return bool(self.c)
  def deg(self):return len(self.c)-1
  def lc(self):assert self;return self.c[-1]
  def __add__(self,o):
   o=Poly(o);n=max(len(self.c),len(o.c))
   return Poly([(self.c[i] if i<len(self.c) else Coeff())+
                (o.c[i] if i<len(o.c) else Coeff()) for i in range(n)])
  __radd__=__add__
  def __neg__(self):return Poly([-c for c in self.c])
  def __sub__(self,o):return self+-Poly(o)
  def __rsub__(self,o):return Poly(o)+-self
  def __mul__(self,o):
   o=Poly(o)
   if not self or not o:return Poly()
   out=[Coeff() for _ in range(self.deg()+o.deg()+1)]
   for i,a in enumerate(self.c):
    if a:
     for j,b in enumerate(o.c):
      if b:out[i+j]=out[i+j]+a*b
   return Poly(out)
  __rmul__=__mul__
  def __pow__(self,n):
   assert isinstance(n,int) and n>=0
   out=Poly(1);base=Poly(self)
   while n:
    if n&1:out=out*base
    n//=2
    if n:base=base*base
   return out
  def __eq__(self,o):
   o=Poly(o);return self.c==o.c
  def shift(self,n):
   assert isinstance(n,int) and n>=0
   return Poly([Coeff()]*n+self.c) if self else Poly()
  def scale(self,c):return Poly([a*Coeff(c) for a in self.c])
  def divrem(self,o):
   o=Poly(o);assert o
   initial=Poly(self);rem=Poly(self)
   quot=Poly()
   inv=o.lc().cinv()
   while rem and rem.deg()>=o.deg():
    tick()
    shift=rem.deg()-o.deg();cc=rem.lc()*inv
    piece=Poly(cc).shift(shift)
    quot=quot+piece;rem=rem-piece*o
   assert quot*o+rem==initial
   assert not rem or rem.deg()<o.deg()
   NEW['polynomialDivisionReturns']+=1
   return quot,rem
  def exact(self,o):
   q,r=self.divrem(o);assert not r
   return q
  def monic(self):
   assert self
   return self.scale(self.lc().cinv())
 return Poly

KU=PolynomialRing(CP)
def cp_to_Ku(v):
 v=CP(v);assert v.degree(1)<=0
 data=[]
 for k in range(v.degree(0)+1):
  data.append(CP(v.a.to_dict().get((k,0),0),v.b.to_dict().get((k,0),0)))
 return KU(data)
def ku_profile(v):
 v=KU(v);out=CP()
 for k,a in enumerate(v.c):out=out+a*u**k
 return profile(out)
def xgcd(a,b,Ring):
 aa=Ring(a);bb=Ring(b)
 r0,r1=Ring(a),Ring(b);s0,s1=Ring(1),Ring();t0,t1=Ring(),Ring(1)
 while r1:
  tick();q,r2=r0.divrem(r1)
  r0,r1=r1,r2;s0,s1=s1,s0-q*s1;t0,t1=t1,t0-q*t1
 if not r0:return Ring(),Ring(),Ring()
 cc=r0.lc().cinv()
 g=r0.scale(cc);s=s0.scale(cc);t=t0.scale(cc)
 assert s*aa+t*bb==g
 NEW['polynomialBezoutReturns']+=1
 return g,s,t

class WholeNonunit(Exception):
 def __init__(self,where,factor):
  self.where=where;self.factor=factor
  super().__init__(where)

outcomes=[]
for label,field_cp,multiplicity in components:
 tick()
 field_poly=cp_to_Ku(field_cp)
 assert field_poly.deg()==3 and field_poly.lc()==1
 class K6:
  _level=2
  def __init__(self,v=0):
   if isinstance(v,K6):self.c=v.c[:];return
   if isinstance(v,KU):p0=KU(v)
   elif isinstance(v,(list,tuple)):p0=KU(v)
   else:p0=KU(CP(v))
   assert all(a.constant() for a in p0.c)
   if p0.deg()>=3:_,p0=p0.divrem(field_poly)
   self.c=p0.c+[CP()]*(3-len(p0.c))
  def __bool__(self):return any(self.c)
  def __add__(self,o):
   if getattr(o,'_level',0)>2:return NotImplemented
   o=K6(o);return K6([a+b for a,b in zip(self.c,o.c)])
  __radd__=__add__
  def __neg__(self):return K6([-x for x in self.c])
  def __sub__(self,o):
   if getattr(o,'_level',0)>2:return NotImplemented
   return self+-K6(o)
  def __rsub__(self,o):
   if getattr(o,'_level',0)>2:return NotImplemented
   return K6(o)+-self
  def __mul__(self,o):
   if getattr(o,'_level',0)>2:return NotImplemented
   o=K6(o);return K6(KU(self.c)*KU(o.c))
  __rmul__=__mul__
  def __pow__(self,n):
   assert isinstance(n,int) and n>=0
   out=K6(1);base=K6(self)
   while n:
    if n&1:out=out*base
    n//=2
    if n:base=base*base
   return out
  def __eq__(self,o):
   if getattr(o,'_level',0)>2:return NotImplemented
   o=K6(o);return self.c==o.c
  def cinv(self):
   if not self:raise WholeNonunit('zero constant coefficient',field_poly)
   g,s,t=xgcd(KU(self.c),field_poly,KU)
   if g!=1:raise WholeNonunit('nonunit in complete constant algebra',g)
   out=K6(s)
   assert self*out==K6(1) and out*self==K6(1)
   NEW['sixCoordinateInverseReturns']+=1
   return out
  def coordinates(self):
   out=[]
   for cc in self.c:
    assert cc.constant()
    out.extend([str(cc.a.to_dict().get((0,0),fmpq(0))),
                str(cc.b.to_dict().get((0,0),fmpq(0)))])
   assert len(out)==6
   return out
 QK=PolynomialRing(K6)
 Uroot=K6([0,1]);Lroot=K6(lam)
 def special(v):
  v=CP(v)
  out=[K6() for _ in range(v.degree(1)+1)]
  upowers={0:K6(1)}
  def u_power(i):
   if i not in upowers:upowers[i]=Uroot**i
   return upowers[i]
  for basis,pp0 in enumerate((v.a,v.b)):
   for mm,cc in pp0.to_dict().items():
    i,qj=int(mm[0]),int(mm[1])
    out[qj]=out[qj]+K6(cc)*(Lroot if basis else K6(1))*u_power(i)
  return QK(out)
 def qp_profile(v):
  v=QK(v)
  data=[c.coordinates() for c in v.c]
  encoded=json.dumps(data,separators=(',',':')).encode()
  return dict(Qdegree=v.deg(),constantQQdimension=6,bytes=len(encoded),
              sha256=hashlib.sha256(encoded).hexdigest())
 try:
  assert special(field_cp)==0
  # These are pure constant old physical units; no D, m, Phi, or Z inverse.
  for const in (Uroot,Uroot-1,Uroot-2):
   inv=const.cinv();assert const*inv==1
  Qvar=QK([0,1]);delQ=QK(1)-Qvar
  MQ=special(M);DQ=special(Delta)
  paidQ=Qvar*delQ*MQ*DQ
  if not paidQ:
   # The WHOLE constant component lies in an already excluded weight divisor.
   outcomes.append(dict(component=label,multiplicity=multiplicity,
                        excluded=True,reason='original paid product identically zero',
                        noOriginalTargetClaim=True))
   say('new_whole_constant_component_has_no_physical_Q',
       component=label,constantQQdimension=6,originalMultiplicity=multiplicity,
       originalPaidProductIdenticallyZero=True,
       allEmbeddingsRetained=True,noOriginalEightRowTargetExecuted=True)
   continue
  rawnums=[special(v.n) for v in raw]
  assert all(v.e>=0 for v in raw)
  normalized=[];removed_polys=[];pass_counts=[];histories=[]
  for name,original in zip(names,rawnums):
   now=QK(original);rem=QK(1);hist=[]
   if now:
    while True:
     tick()
     gd,sg,tg=xgcd(now,paidQ,QK)
     if gd.deg()<=0:break
     new=now.exact(gd);unitquot=paidQ.exact(gd)
     assert new*gd==now and unitquot*gd==paidQ
     rem=rem*gd;now=new
     NEW['fullPaidPrimaryProducts']+=2
     hist.append(qp_profile(gd))
   assert rem*now==original
   normalized.append(now);removed_polys.append(rem)
   pass_counts.append(len(hist));histories.append(hist)
   say('new_whole_K6_original_Q_row_paid_primary',
       component=label,name=name,constantQQdimension=6,
       originalMultiplicity=multiplicity,
       rawNumerator=qp_profile(original),retainedOriginalQRow=qp_profile(now),
       removedOnlyWholeFactorsOfOriginalQdeltaMDelta=hist,
       exactNormalizationProductReturned=True,
       originalDeltaDenominatorPower=raw[names.index(name)].e,
       allQHeadsAndBothLambdaEmbeddingsRetained=True)
  common=QK();bez=[QK() for _ in raw];used=[]
  for index,rr in enumerate(normalized):
   if not rr:continue
   common,s,t=xgcd(common,rr,QK)
   bez=[s*x for x in bez]
   bez[index]=bez[index]+t;used.append(index)
   assert sum((a*b for a,b in zip(bez,normalized)),QK())==common
   say('new_whole_K6_same_Q_original_Bezout',
       component=label,lastOriginalName=names[index],
       originalRowsUsed=[names[k] for k in used],
       wholeQGCD=qp_profile(common),fullEightColumnIdentityReturned=True,
       noOriginalQRootSelected=True)
   if common==1:break
  if not common:
   outcomes.append(dict(component=label,multiplicity=multiplicity,
                        excluded=False,reason='all original rows vanish identically'))
   say('new_whole_constant_Q_fibre_still_open',
       component=label,allOriginalQRowsZero=True,
       noQOrConstantComponentRemoved=True,excluded=False)
   continue
  # EXACT common clearing: every removed factor divides paidQ; repeated
  # primary factors are retained until their entire multiplicity is paid.
  N=max(pass_counts,default=0)
  clearing=paidQ**N
  # Raw DD_i=n_i/delta^e_i; return all eight scaled original rows by using
  # one common DELTA-DENOMINATOR POWER, never a quotient-ring inverse.
  delta_power=max((v.e for v in raw),default=0)
  den=delQ**delta_power
  omegas=[]
  for bi,removed_i,val in zip(bez,removed_polys,raw):
   quot=clearing.exact(removed_i)
   assert quot*removed_i==clearing
   omegas.append(bi*quot*delQ**val.e)
  lhs=sum((oi*ni*delQ**(delta_power-val.e)
           for oi,ni,val in zip(omegas,rawnums,raw)),QK())
  rhs=den*clearing*common
  assert lhs==rhs
  NEW['originalEightSourceReturns']+=1
  certificate=dict(component=label,oldMultiplicity=multiplicity,
                   target=qp_profile(clearing*common),
                   originalNames=names,homogeneityPowersOfH=homogeneity,
                   sourceMultiplierProfiles=[qp_profile(x) for x in omegas],
                   sameQCommonFactor=qp_profile(common),paidClearingPower=N,
                   rawCommonDeltaDenominatorPower=delta_power)
  certbytes=json.dumps(certificate,separators=(',',':')).encode()
  excluded=common==1
  outcomes.append(dict(component=label,multiplicity=multiplicity,
                       excluded=excluded,QGCDdegree=common.deg(),
                       QGCDsha256=qp_profile(common)['sha256']))
  say('new_whole_K6_complete_original_eight_row_return',
      component=label,constantQQdimension=6,originalMultiplicity=multiplicity,
      targetIdentity='sum Omega_i H^d_i Original_i=(Q delta M Delta)^N gcd_Q',
      originalEightScaledRowsReturned=True,
      allQQCoordinatesAndQCoefficientsReturned=True,
      paidClearingPower=N,commonDeltaDenominatorPower=delta_power,
      wholeSameQGCD=qp_profile(common),
      returnedProfilesBytes=len(certbytes),
      returnedProfilesSHA256=hashlib.sha256(certbytes).hexdigest(),
      entireConstantFieldPhysicallyExcluded=excluded,
      allUnexcludedQFibresRetained=not excluded,
      noPhysicalDOrUnpaidNormInverse=True)
 except WholeNonunit as problem:
  outcomes.append(dict(component=label,multiplicity=multiplicity,
                       excluded=False,reason=problem.where,
                       wholeConstantFactor=ku_profile(problem.factor)))
  say('new_whole_constant_nonunit_component_retained',
      component=label,where=problem.where,
      completeConstantFactor=ku_profile(problem.factor),
      noEmbeddingSelectedAndNoPartialExclusion=True,excluded=False)
allclosed=len(outcomes)==len(components) and all(x['excluded'] for x in outcomes)
say('new_Cramer_cubic_constant_original_Q_return_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 outcomes=outcomes,entireHalfWeightChartExcluded=allclosed,
 originalG12MultiplicityPreserved=True,
 allComponentExclusionsSupportNilpotentCRT=allclosed,
 nilpotentLiftUsesOnlyOriginalPaidUnits=True,
 DeltaNonzeroChartOnly=True,otherCollisionWeightsNotExcluded=True,
 noOldFiveCofactorsOrAccumulatedUBezoutOrNorm24Replayed=True,
 noNumericPrimeOrIndividualAlgebraicRootUsed=True,
 noCoefficientPayloadCacheSaved=True,
 statistics=NEW,
 definitionArithmeticStatistics=ns['stats'],
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)
