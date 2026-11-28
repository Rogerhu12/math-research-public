#!/usr/bin/env python3
"""NEW complete F101 constant algebras on the original Lhalf weight curve.
First factor the already-defined F101 over QQ, returning the full product.
For every complete QQ[k]/phi, retain both e roots and all e nilpotents of
Lhalf; remove only entire components on which a previously paid original
weight vanishes, by repeated exact polynomial gcd. No e root is selected.
The seven same-source, simultaneously Lhalf-column-cancelled original
rows are tested as a map A^7 -> A^6 in a finite free Z_(p) model. The prime
is fixed solely from coefficient integrality BEFORE any ideal rank test.
Only a full original regular-representation right inverse is promoted by
finite-module Nakayama. Deficient blocks remain whole QQ exceptions.
All phi multiplicities lift by the nilpotent-ideal Nakayama argument.
No modular D-nilpotence is promoted to QQ, and no physical D inverse is
used by the calculation. 180 seconds / 4 GiB. Small source/definitions/
SHA/receipts only: no recomputable coefficient or matrix payload cache.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq,fmpq_poly,nmod_poly,nmod_mat
START=time.perf_counter();DEADLINE=START+180
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
signal.setitimer(signal.ITIMER_REAL,180)
def say(**kw):
 kw['seconds']=time.perf_counter()-START
 print(json.dumps(kw,separators=(',',':')),flush=True)
def digest(obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def qprofile(poly):
 return dict(degree=int(poly.degree()),**digest([str(c) for c in poly.coeffs()]))
# Necessary reconstruction of the unique previously defined parameter G:
# stop immediately after the FINAL coefficient-denominator LCM. No old
# explicit polynomial-lift tail, paid-factor result gate, native determinant,
# seven-row function-field Popov, or old modular fibre gate is run.
path=Path(__file__).with_name('2026-11-28-unit211-W-entire-Lhalf-quadratic-original-D-final-denominator-return-8542.py')
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='53c744cfb54beccaae092fb51ab9869331a0b801361eefc5e2e0032d674bdf0f'
mark=b'\nassert G\nG=G/G[G.degree()]'
assert raw.count(mark)==1
prefix=raw.split(mark)[0]
assert len(prefix)==14141
assert hashlib.sha256(prefix).hexdigest()=='fcea5eeab2f66bc7a0f3ae7d757e5be09955c3e6398ae74bdbdd14d6b7ebaada'
env={'__file__':str(path),'__name__':'new_F101_parameter_definition_only'}
oa=signal.alarm;ot=signal.setitimer
def timer(which,seconds,interval=0.0):
 if which!=signal.ITIMER_REAL:return ot(which,seconds,interval)
 assert not interval
 left=max(.001,DEADLINE-time.perf_counter())
 return ot(which,min(left,float(seconds) if seconds>0 else left),0.0)
def alarm(seconds):return math.ceil(timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=alarm;signal.setitimer=timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+'#new_parameter_definition','exec'),env)
finally:
 signal.alarm=oa;signal.setitimer=ot
 ot(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
G=env['G'];G=G/G[G.degree()]
assert qprofile(G)==dict(degree=140,bytes=9539,sha256='c9a9515ce15e56a90e32dac62ffde3380fc6daf7ce9846a6a15f691f79df0a6f')
kpQ=fmpq_poly([0,1]);oneQ=fmpq_poly([1]);zeroQ=fmpq_poly([])
paid=kpQ**7*(kpQ+2)**15*(kpQ+4)**17
F101,rem=divmod(G,paid)
assert not rem and F101*paid==G
assert qprofile(F101)==dict(degree=101,bytes=5793,sha256='185c9cb25e54e6b0b85e2d0e509a500de0fb4effae48d7a8ec51366c3ea0764f')
say(stage='new_F101_complete_constant_fibre_parameter',
 finalPreviouslyDefinedCover=qprofile(F101),
 parameterConstructorPrefixBytes=len(prefix),
 parameterConstructorPrefixSHA256=hashlib.sha256(prefix).hexdigest(),
 originalPaidPureKFactorsOnly=[['k',7],['k+2',15],['k+4',17]],
 oldExplicitLhalfLiftAndSevenRowPopovNotExecuted=True,
 noSavedCoefficientArrayOrPayloadUsed=True,wholeLhalfExcluded=False,wholeWExcluded=False)
unit,fact=F101.factor()
returned=fmpq_poly([unit])
for phi,mult in fact:returned*=phi**int(mult)
assert returned==F101
factors=[(phi/phi[phi.degree()],int(mult)) for phi,mult in fact]
factors.sort(key=lambda fm:(fm[0].degree(),tuple(str(c) for c in fm[0].coeffs())))
returned=oneQ
for phi,mult in factors:
 assert phi.degree()>0 and phi[phi.degree()]==1 and mult>0
 returned*=phi**mult
assert returned==F101 and sum(int(phi.degree())*mult for phi,mult in factors)==101
say(stage='new_F101_complete_QQ_factorization_return',
 allIrreducibleQQFactorsFromExactFactorization=True,
 completeProductAndEveryMultiplicityActuallyReturned=True,
 factors=[dict(index=i,multiplicity=m,**qprofile(f)) for i,(f,m) in enumerate(factors)],
 noFactorDiscardedOrTreatedAsNumericalSample=True,
 entireCoverStillRequiresOriginalReturns=True,wholeLhalfExcluded=False,wholeWExcluded=False)
native=env['native'];ns=env['ns'];R=env['R'];ctx=env['ctx']
zero,one=env['zero'],env['one'];ep,kp=env['ep'],env['kp']
basis=env['basis'];variables=env['variables'];mats=env['mats'];errors=env['errors']
verify=env['verify'];deflate=env['deflate'];rowprofile=env['rowprofile']
baseN=env['baseN'];dprime=env['dprime'];L=env['L']
# This is the independently sourced, already fixed seventh original row.
# Its original trace and BOTH Lhalf column divisions are returned again as
# necessary input construction, without any old pivot or modular selection.
MA,MB=mats[0],mats[1];ix=4
rr=[sum((MA[ix][h]*MB[h][j]-MB[ix][h]*MA[h][j] for h in range(6)),R()) for j in range(6)]
tag=[]
for g in range(6):
 co=variables[0]*errors[1][ix][g]-variables[1]*errors[0][ix][g]
 co+=sum((MB[ix][h]*errors[0][h][g]-MA[ix][h]*errors[1][h][g] for h in range(6)),R())
 tag.append(co)
verify(sum((rr[i]*basis[i] for i in range(6)),R()),tag)
with contextlib.redirect_stdout(io.StringIO()):
 comm_pol,comm_tag=native['clear_original_row'](rr,tag,'fixed_original_xy_commutator_row4')
verify(sum((R(comm_pol[i])*basis[i] for i in range(6)),R()),comm_tag)
commN=deflate(comm_pol)
assert rowprofile(commN)==dict(degrees=[30,41],terms=4775,bytes=186207,
 sha256='3c51635281b8312c2c352bdc4463fd4dd9f6de09d0a603bd12898a4985493f17')
rows=baseN+[commN]
labels=['NS','PS','yNS','tNS','yPS','tPS','comm_xy_row4']
assert len(rows)==7
# Encode only in transient process memory. The same exact polynomial
# definitions are then evaluated in EACH complete QQ constant algebra.
def e_coefficients(poly):
 by_e={}
 for mon,c in poly.to_dict().items():
  assert not any(mon[j] for j in range(2,len(mon)))
  ie,ik=int(mon[0]),int(mon[1])
  by_e.setdefault(ie,{})[ik]=c
 out=[]
 for ie in range(max(by_e,default=-1)+1):
  dd=by_e.get(ie,{})
  out.append(fmpq_poly([dd.get(ik,fmpq(0)) for ik in range(max(dd,default=-1)+1)]))
 while out and not out[-1]:out.pop()
 return tuple(out)
rowdefinitions=[[e_coefficients(x) for x in row] for row in rows]
targetdefinitions=[e_coefficients(x) for x in dprime]
atoms=[(label,e_coefficients(poly)) for label,poly in native['paid_atoms']]
assert all(poly for _,poly in atoms)
say(stage='new_F101_seven_same_original_rows_complete',
 labels=labels,allSevenOriginalSixCoordinateTracesReturned=True,
 simultaneousOriginalDAndTwoCancelledColumnsReturned=True,
 noLhalfInverse=True,noDInverse=True,
 wholeQuadraticAndParameterPrimaryPowersRetained=True,
 newTest='finite integral regular representation of A^7 to A^6',
 noFunctionFieldPopovOrOldNativeDeterminant=True,
 wholeLhalfExcluded=False,wholeWExcluded=False)
def prime_integer(p):
 if p<2:return False
 d=2
 while d*d<=p:
  if p%d==0:return False
  d+=1
 return True

def process_factor(index,phi,multiplicity):
 stats=dict(KInverses=0,KPolynomialDivisionProducts=0,unitProducts=0)
 dK=int(phi.degree())
 class K:
  __slots__=('p',)
  def __init__(self,x=0):
   if isinstance(x,K):self.p=x.p;return
   if not isinstance(x,fmpq_poly):x=fmpq_poly([x])
   self.p=x%phi
  def __bool__(self):return bool(self.p)
  def __neg__(self):return K(-self.p)
  def __add__(self,other):return K(self.p+K(other).p)
  __radd__=__add__
  def __sub__(self,other):return K(self.p-K(other).p)
  def __rsub__(self,other):return K(other)-self
  def __mul__(self,other):return K(self.p*K(other).p)
  __rmul__=__mul__
  def inv(self):
   assert self
   g,s,t=self.p.xgcd(phi)
   assert s*self.p+t*phi==g and g.degree()==0 and g[0]
   out=K(s/g[0])
   assert self*out==K(1) and out*self==K(1)
   stats['KInverses']+=1
   return out
  def __truediv__(self,other):return self*K(other).inv()
  def __rtruediv__(self,other):return K(other)*self.inv()
  def __pow__(self,n):
   if n<0:return self.inv()**(-n)
   a=K(1);b=self
   while n:
    if n&1:a=a*b
    n//=2
    if n:b=b*b
   return a
  def __eq__(self,other):return self.p==K(other).p
  def data(self):return [str(c) for c in self.p.coeffs()]
 zK,oK=K(),K(1);kv=K(kpQ)
 def trim(a):
  a=list(a)
  while a and not a[-1]:a.pop()
  return tuple(a)
 def add(a,b,sgn=1):
  return trim([(a[j] if j<len(a) else zK)+sgn*(b[j] if j<len(b) else zK)
               for j in range(max(len(a),len(b)))])
 def scale(a,c):return trim([q*c for q in a])
 def mul(a,b):
  if not a or not b:return ()
  out=[zK]*(len(a)+len(b)-1)
  for i,x in enumerate(a):
   if x:
    for j,y in enumerate(b):
     if y:out[i+j]=out[i+j]+x*y
  return trim(out)
 def divrem(a,b):
  a=trim(a);b=trim(b);assert b
  original=a
  if len(a)<len(b):return (),a
  iv=b[-1].inv();q=[zK]*(len(a)-len(b)+1);r=list(a)
  while r and len(r)>=len(b):
   j=len(r)-len(b);c=r[-1]*iv;q[j]=q[j]+c
   for i,x in enumerate(b):r[j+i]=r[j+i]-c*x
   r=list(trim(r))
  q=trim(q);r=trim(r)
  assert add(mul(q,b),r)==original
  assert len(r)<len(b)
  stats['KPolynomialDivisionProducts']+=1
  return q,r
 def egcd(a,b):
  original_a,original_b=trim(a),trim(b)
  r0,r1=original_a,original_b;s0,s1=(oK,),();t0,t1=(),(oK,)
  while r1:
   q,r=divrem(r0,r1)
   r0,r1=r1,r;s0,s1=s1,add(s0,mul(q,s1),-1);t0,t1=t1,add(t0,mul(q,t1),-1)
  if not r0:return (),(),()
  iv=r0[-1].inv()
  g,s,t=scale(r0,iv),scale(s0,iv),scale(t0,iv)
  assert g[-1]==oK and add(mul(s,original_a),mul(t,original_b))==g
  return g,s,t
 def data(a):return [x.data() for x in a]
 def red(a,h):return divrem(a,h)[1]
 def ev(definition):return trim([K(x) for x in definition])
 h0=(-(kv*kv+6*kv+8)/(4*kv),-(kv*kv+4*kv+8)/(4*kv),oK)
 h=h0;saturation=[]
 evaluated_atoms=[(label,ev(a)) for label,a in atoms]
 for label,atom in evaluated_atoms:
  while len(h)>1:
   g,s,t=egcd(atom,h)
   assert g
   if len(g)==1:break
   before=h;h,remainder=divrem(h,g)
   assert not remainder and mul(h,g)==before
   saturation.append(dict(atom=label,removedEDegree=len(g)-1,
                          remainingEDegree=len(h)-1,
                          actualGCDAndDivisionReturned=True))
  if len(h)==1:break
 if len(h)==1:
  assert h==(oK,)
  return dict(index=index,QQFactor=qprofile(phi),multiplicity=multiplicity,
      entireOriginalWeightComponentExcludedByPaidUnits=True,
      repeatedWholeComponentSaturation=saturation,remainingEDegree=0,
      exactConstantFieldChecks=stats,wholeFactorReturned=True,
      noModularRankTestNeeded=True)
 assert len(h) in (2,3) and h[-1]==oK
 quot,remainder=divrem(h0,h)
 assert not remainder and mul(quot,h)==h0
 original_units=[]
 for label,atom in evaluated_atoms:
  g,s,t=egcd(atom,h)
  assert g==(oK,)
  iv=red(s,h);ar=red(atom,h)
  assert red(mul(ar,iv),h)==(oK,)
  original_units.append((label,ar,iv))
  stats['unitProducts']+=1
 # All row and target reductions retain the entire surviving e algebra.
 QQrows=[[red(ev(definition),h) for definition in row] for row in rowdefinitions]
 QQtarget=[red(ev(definition),h) for definition in targetdefinitions]
 de=len(h)-1;dimension=dK*de
 # Choose a prime ONLY for the final finite free model and actual original
 # unit inverse coefficients. There is NO rank/ideal test inside selection.
 rational_coefficients=list(phi.coeffs())
 for poly in [h,quot]+[x for row in QQrows for x in row]+QQtarget:
  for x in poly:rational_coefficients.extend(x.p.coeffs())
 for label,ar,iv in original_units:
  for poly in [ar,iv]:
   for x in poly:rational_coefficients.extend(x.p.coeffs())
 denoms={int(c.denominator) for c in rational_coefficients}
 assert all(d>0 for d in denoms)
 p=1009
 while not prime_integer(p) or any(d%p==0 for d in denoms):p+=1
 assert prime_integer(p) and all(d%p for d in denoms)
 def modq(c):return int(c.numerator)%p*pow(int(c.denominator)%p,-1,p)%p
 phip=nmod_poly([modq(c) for c in phi.coeffs()],p)
 assert phip.degree()==dK and int(phip[dK])==1
 zp=nmod_poly([],p);op=nmod_poly([1],p)
 def coeff(x):return nmod_poly([modq(c) for c in x.p.coeffs()],p)%phip
 hp=[coeff(x) for x in h];assert hp[-1]==op
 def reduceA(a):
  out=[q%phip for q in a]
  while out and not out[-1]:out.pop()
  for j in range(len(out)-1,de-1,-1):
   c=out[j]
   if c:
    for i in range(de):
     out[j-de+i]=(out[j-de+i]-c*hp[i])%phip
   out[j]=zp
  return tuple((out[i] if i<len(out) else zp) for i in range(de))
 A0=tuple(zp for _ in range(de));A1=reduceA([op])
 def am(a,b):
  out=[zp]*(2*de-1)
  for i,x in enumerate(a):
   if x:
    for j,y in enumerate(b):
     if y:out[i+j]=(out[i+j]+x*y)%phip
  return reduceA(out)
 def ae(poly):return reduceA([coeff(x) for x in poly])
 def flatten(a):
  return [int(a[j][i]) for j in range(de) for i in range(dK)]
 assert reduceA(hp)==A0
 assert ae(h0)==A0
 for label,ar,iv in original_units:
  assert am(ae(ar),ae(iv))==A1
 RR=[[ae(x) for x in row] for row in QQrows]
 dd=[ae(x) for x in QQtarget]
 unit_defs=[dict(label=label,definition=digest([data(ar),data(iv)]))
            for label,ar,iv in original_units]
 say(stage='new_F101_whole_QQ_factor_integral_model',
  index=index,QQFactor=qprofile(phi),multiplicity=multiplicity,
  completeOriginalQuadraticDegree=2,survivingEDegree=de,
  repeatedWholeComponentSaturation=saturation,
  allRemainingOriginalPaidWeightInversesActuallyReturned=True,
  trueQQUnitDefinitions=unit_defs,exactConstantFieldChecks=stats,
  chosenPrime=p,primeFixedBeforeAnyOriginalIdealRankTest=True,
  checkedIntegralRationalCoefficients=len(rational_coefficients),
  integralDenominatorDefinition=digest(sorted(str(d) for d in denoms)),
  finiteFreeModelRank=dimension,
  fullModKPolynomialIncludingAllPrimaryPowers=True,
  modKFactorizationOrSelectedRootNotUsed=True,
  originalSevenRowDefinition=digest([[data(x) for x in row] for row in QQrows]),
  originalDTargetDefinition=digest([data(x) for x in QQtarget]),
  wholeLhalfExcluded=False,wholeWExcluded=False)
 weightbasis=[]
 for je in range(de):
  for ik in range(dK):
   ww=[zp]*(je+1);ww[je]=nmod_poly([0]*ik+[1],p)
   weightbasis.append(reduceA(ww))
 assert len(weightbasis)==dimension
 for j,bb in enumerate(weightbasis):
  assert flatten(bb)==[int(i==j) for i in range(dimension)]
 # Column (r,b) is EXACTLY weight basis element b times original row r.
 # No free-algebra assumption is used for the original geometry generators.
 sourcecols=[];defs=[]
 for rowindex,row in enumerate(RR):
  for j,bb in enumerate(weightbasis):
   sourcecols.append([v for co in row for v in flatten(am(co,bb))])
   defs.append([rowindex,j])
 n=6*dimension;m=7*dimension
 assert len(sourcecols)==m and all(len(col)==n for col in sourcecols)
 matrix=nmod_mat([[sourcecols[j][i] for j in range(m)] for i in range(n)],p)
 echelon,rank=matrix.rref()
 rank=int(rank);pivots=[]
 for i in range(rank):
  pos=next(j for j in range(m) if int(echelon[i,j]))
  assert int(echelon[i,pos])==1
  assert all(int(echelon[h,pos])==int(h==i) for h in range(rank))
  pivots.append(pos)
 assert len(set(pivots))==rank and pivots==sorted(pivots)
 full=rank==n
 certificate=None;target_return=False
 if full:
  selected=nmod_mat([[sourcecols[j][i] for j in pivots] for i in range(n)],p)
  inverse=selected.inv()
  identity=nmod_mat([[int(i==j) for j in range(n)] for i in range(n)],p)
  assert selected*inverse==identity and inverse*selected==identity
  dvector=[v for co in dd for v in flatten(co)]
  target=nmod_mat(n,1,dvector,p)
  solution=inverse*target
  assert selected*solution==target
  # Actual original selected columns, not only a reduced echelon matrix.
  target_return=True
  certificate=digest(dict(selectedOriginalColumns=[defs[j] for j in pivots],
     inverse=[[int(inverse[i,j]) for j in range(n)] for i in range(n)],
     originalTargetCoefficients=[int(solution[i,0]) for i in range(n)]))
 record=dict(index=index,QQFactor=qprofile(phi),multiplicity=multiplicity,
  remainingEDegree=de,finiteFreeModelRank=dimension,prime=p,
  originalRegularRepresentationShape=[n,m],actualFullFpRank=rank,
  fullOriginalUnitMapReturned=full,actualBothSquareInverseProductsReturned=full,
  actualOriginalDTargetProductReturned=target_return,
  originalSourceMatrixDefinition=digest(sourcecols),
  certificate=certificate,exactConstantFieldChecks=stats,
  wholeFactorReturned=full,allRankDeficientQQSupportRetained=not full)
 say(stage='new_F101_complete_factor_original_regular_return',
  **record,finiteCokernelNakayamaAppliedOnlyIfFullRank=full,
  originalPhiMultiplicityRecoveredByNilpotentIdealNakayama=full,
  simultaneousDColumnIdentityUsesNoLhalfInverse=True,
  noModularDNilpotencePromotion=True,noAlternativePrimeOrRowOrderRetry=True,
  wholeLhalfExcluded=False,wholeWExcluded=False)
 return record

records=[]
for index,(phi,multiplicity) in enumerate(factors):
 record=process_factor(index,phi,multiplicity)
 records.append(record)
 if record.get('entireOriginalWeightComponentExcludedByPaidUnits'):
  say(stage='new_F101_complete_factor_original_paid_exclusion',**record,
      allPhiMultiplicityRetained=True,wholeLhalfExcluded=False,wholeWExcluded=False)
all_closed=all(record['wholeFactorReturned'] for record in records)
say(stage='new_complete_F101_constant_original_return_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 completeQQFactorizationDegree=101,
 completeFactorRecords=records,
 allQQFactorsAndOriginalMultiplicityAccountedFor=True,
 remainingQQFactorIndices=[r['index'] for r in records if not r['wholeFactorReturned']],
 wholeLhalfOriginalPhysicalBranchExcluded=all_closed,
 proofIfComplete='G*D in I6+(L); all unpaid F101 fibres have original D return after paid weights; D is a physical unit',
 noOtherFiniteKOrH198SupportDeclaredClosed=True,
 noModularDNilpotencePromotion=True,noMatrixOrCoefficientPayloadSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 wholeWExcluded=False,ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
