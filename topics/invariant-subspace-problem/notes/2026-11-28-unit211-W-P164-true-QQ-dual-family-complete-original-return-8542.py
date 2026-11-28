#!/usr/bin/env python3
"""NEW QQ(k) four-dimensional original dual-number family.
E=QQ(k)[e]/(4*k*e^2-(k^2+4*k+8)*e-(k^2+6*k+8)),
S=E[eps]/eps^2.  Do not assume E is a field.
ell=1/2, lambda=1/2+eps, T=-1/2, x=1/2+2*(1-e)*eps,
y=1/2,t=0,f=(e+1)/2-(e-1)*eps.
Return the complete original I6, all required weight denominators, the
same N1/qZ coordinates, and all five complete D-cleared I11 values.
P and chi already lie in the original I6/I4, with the native paid
denominators checked here; their old determinants are NOT replayed.
Together with the separately proved generic dimension <=4, the
surjection onto this rank-four family is an isomorphism, so D is
TRULY zero over QQ(k), not inferred from its modular image.
180s /4GiB; no large or encoded coefficient output.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq,fmpq_poly
START=time.perf_counter();DEADLINE=START+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**kw):
 kw['seconds']=time.perf_counter()-START
 print(json.dumps(kw,separators=(',',':')),flush=True)
def digest(obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
# Only necessary original Gram, three means and N1-square definitions.
# No old cofactor, P determinant, characteristic tail or modular gate.
name='2026-11-28-unit211-W-H198-full-original-values-first-mean-reduction-twenty-two-model-8542.py'
path=Path(__file__).with_name(name);raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='f6f07b2f3fdb50f59565ef6501cbc2121d5882ce7cb32f7d17a4a1d2d139b6a1'
marker=b'\n# The exact I4 construction:'
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert len(prefix)==5551
assert hashlib.sha256(prefix).hexdigest()=='9a6f12dad89cc77c651f902bf881b53eca708cd8f0dcfab2961dabb089ed3523'
val={'__file__':str(path),'__name__':'new_QQ_dual_family_original_definitions'}
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
  exec(compile(prefix,str(path)+'#only_original_definitions','exec'),val)
finally:
 signal.alarm=oa;signal.setitimer=ot
 ot(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
old=val['old'];phys=val['phys'];tri=val['tri']
R=val['R'];ctx=val['ctx'];ep,kp=ctx.gens()[:2]
division_count=0;weight_inverse_count=0
def pp(value):
 return value if isinstance(value,fmpq_poly) else fmpq_poly([value])
def qdiv(a,b):
 global division_count
 q,r=divmod(a,b);assert not r and q*b==a
 division_count+=1;return q
class F:
 __slots__=('n','d')
 def __init__(self,n=0,d=None):
  if isinstance(n,F):
   assert d is None;self.n=n.n;self.d=n.d;return
  n=pp(n);d=pp(1) if d is None else pp(d);assert d
  if not n:self.n=pp(0);self.d=pp(1);return
  g=n.gcd(d);n=qdiv(n,g);d=qdiv(d,g);c=d[d.degree()]
  self.n=n/c;self.d=d/c
 def __bool__(self):return bool(self.n)
 def __neg__(self):return F(-self.n,self.d)
 def __add__(self,other):
  other=F(other)
  if not self:return other
  if not other:return self
  return F(self.n*other.d+other.n*self.d,self.d*other.d)
 __radd__=__add__
 def __sub__(self,other):return self+-F(other)
 def __rsub__(self,other):return F(other)+-self
 def __mul__(self,other):
  other=F(other)
  if not self or not other:return F()
  return F(self.n*other.n,self.d*other.d)
 __rmul__=__mul__
 def __truediv__(self,other):
  other=F(other);assert other
  return F(self.n*other.d,self.d*other.n)
 def __rtruediv__(self,other):return F(other)/self
 def __pow__(self,n):
  if n<0:return F(self.d**(-n),self.n**(-n))
  return F(self.n**n,self.d**n)
 def __eq__(self,other):
  other=F(other);return self.n*other.d==other.n*self.d
 def data(self):return [[str(v) for v in self.n.coeffs()],[str(v) for v in self.d.coeffs()]]
kF=F(fmpq_poly([0,1]))
r1=(kF*kF+4*kF+8)/(4*kF)
r0=(kF*kF+6*kF+8)/(4*kF)
class W:
 __slots__=('a','b')
 def __init__(self,a=0,b=0):
  if isinstance(a,W):
   assert b==0;self.a=a.a;self.b=a.b;return
  self.a=F(a);self.b=F(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __neg__(self):return W(-self.a,-self.b)
 def __add__(self,other):
  other=W(other);return W(self.a+other.a,self.b+other.b)
 __radd__=__add__
 def __sub__(self,other):return self+-W(other)
 def __rsub__(self,other):return W(other)+-self
 def __mul__(self,other):
  other=W(other)
  return W(self.a*other.a+r0*self.b*other.b,
           self.a*other.b+self.b*other.a+r1*self.b*other.b)
 __rmul__=__mul__
 def inv(self):
  global weight_inverse_count
  # Multiplication norm in the WHOLE monic quadratic algebra.
  norm=self.a*self.a+r1*self.a*self.b-r0*self.b*self.b
  if not norm:
   say(stage='new_QQ_dual_family_required_weight_nonunit',
       elementDefinition=digest(self.data()),noFieldAssumption=True,
       originalFamilySurjectionNotEstablished=True,wholeWExcluded=False)
   raise ArithmeticError('required weight not a unit in complete quadratic algebra')
  out=W((self.a+r1*self.b)/norm,-self.b/norm)
  assert self*out==W(1) and out*self==W(1)
  weight_inverse_count+=1;return out
 def __truediv__(self,other):return self*W(other).inv()
 def __rtruediv__(self,other):return W(other)*self.inv()
 def __pow__(self,n):
  if n<0:return self.inv()**(-n)
  out=W(1);base=self
  while n:
   if n&1:out=out*base
   n//=2
   if n:base=base*base
  return out
 def __eq__(self,other):
  other=W(other);return self.a==other.a and self.b==other.b
 def data(self):return [self.a.data(),self.b.data()]
class Dual:
 __slots__=('a','b')
 def __init__(self,a=0,b=0):
  if isinstance(a,Dual):
   assert b==0;self.a=a.a;self.b=a.b;return
  self.a=W(a);self.b=W(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __neg__(self):return Dual(-self.a,-self.b)
 def __add__(self,other):
  other=Dual(other);return Dual(self.a+other.a,self.b+other.b)
 __radd__=__add__
 def __sub__(self,other):return self+-Dual(other)
 def __rsub__(self,other):return Dual(other)+-self
 def __mul__(self,other):
  other=Dual(other)
  return Dual(self.a*other.a,self.a*other.b+self.b*other.a)
 __rmul__=__mul__
 def __truediv__(self,other):
  other=Dual(other)
  # No geometric inverse is used in this construction.
  assert not other.b,'only original pure-weight divisors'
  wi=other.a.inv();return Dual(self.a*wi,self.b*wi)
 def __rtruediv__(self,other):return Dual(other)/self
 def __pow__(self,n):
  assert n>=0;out=Dual(1);base=self
  while n:
   if n&1:out=out*base
   n//=2
   if n:base=base*base
  return out
 def __eq__(self,other):
  other=Dual(other);return self.a==other.a and self.b==other.b
 def data(self):return [self.a.data(),self.b.data()]
half=fmpq(1,2)
e=Dual(W(0,1));k=Dual(W(kF));eps=Dual(0,1);one=Dual(1)
assert eps and eps*eps==0
assert 4*k*e*e-(k*k+4*k+8)*e-(k*k+6*k+8)==0
free_basis=[one,e,eps,e*eps]
# Explicit canonical coordinates: the family is FREE rank four over QQ(k).
assert [(v.a.a,v.a.b,v.b.a,v.b.b) for v in free_basis]==[
 (F(1),F(0),F(0),F(0)),(F(0),F(1),F(0),F(0)),
 (F(0),F(0),F(1),F(0)),(F(0),F(0),F(0),F(1))]
eW=W(0,1);ewpowers=[W(1)]
def weightpoly(poly):
 dd=poly.to_dict();by_e={}
 for mon,cc in dd.items():
  assert not any(mon[j] for j in range(2,len(mon)))
  ie,ik=int(mon[0]),int(mon[1])
  row=by_e.setdefault(ie,{})
  row[ik]=row.get(ik,fmpq(0))+cc
 maxe=max(by_e,default=0)
 while len(ewpowers)<=maxe:ewpowers.append(ewpowers[-1]*eW)
 out=W()
 for ie,coeffs in by_e.items():
  arr=[fmpq(0)]*(max(coeffs,default=-1)+1)
  for ik,c in coeffs.items():arr[ik]=c
  out=out+ewpowers[ie]*W(F(fmpq_poly(arr)))
 return out
den_cache={}
def weightinverse(poly):
 key=str(poly)
 if key not in den_cache:
  value=weightpoly(poly);inverse=value.inv()
  assert value*inverse==W(1)
  den_cache[key]=inverse
 return den_cache[key]
def evalR(rr,images):
 rr=R(rr)
 assert len(images)==8
 assert all(not any(mon[j] for j in range(2,8)) for mon in rr.d.to_dict())
 inv=weightinverse(rr.d)
 groups={}
 for mon,co in rr.n.to_dict().items():
  geo=tuple(int(mon[j]) for j in range(2,8))
  d=groups.setdefault(geo,{})
  pair=(int(mon[0]),int(mon[1]))
  d[pair]=d.get(pair,fmpq(0))+co
 maxd=[max((m[j] for m in groups),default=0) for j in range(6)]
 powers=[]
 for j in range(6):
  seq=[Dual(1)]
  for z in range(maxd[j]):seq.append(seq[-1]*images[j+2])
  powers.append(seq)
 out=Dual()
 for mon,coeffs in groups.items():
  by_e={}
  for (ie,ik),co in coeffs.items():
   d=by_e.setdefault(ie,{})
   d[ik]=d.get(ik,fmpq(0))+co
  while len(ewpowers)<=max(by_e,default=0):ewpowers.append(ewpowers[-1]*eW)
  coefficient=W()
  for ie,d in by_e.items():
   arr=[fmpq(0)]*(max(d,default=-1)+1)
   for ik,co in d.items():arr[ik]=co
   coefficient=coefficient+ewpowers[ie]*W(F(fmpq_poly(arr)))
  term=Dual(coefficient*inv)
  for j in range(6):term=term*powers[j][mon[j]]
  out=out+term
 return out
blank=[e,k]+[Dual() for _ in range(6)]
def weight(rr):return evalR(rr,blank)
u,Q,ell,M,P02,T0,J,Phi,Pf=[weight(old[n]) for n in
 ['u','Q','l','M','P02','T0','J','Phi','Pf']]
bc=weight(old['bc']);m=u-ell;delta=1-Q
assert ell==half and u==e+1 and Q==e*k
assert 4*bc*delta==M
assert P02==(2-u)*T0 and T0-J+Q==0
# Required native weight units for P in I6 and chi in I4. This is
# exactly the established native source atom list, not all physical
# chart exclusions and not an assumption that every nonzero is invertible.
native_atoms=old['units']+[
 ('k_plus_one',kp+1),('whole_equal_k_plus_two',kp+2),
 ('old_H',4*ep*kp-kp**2-4*kp-8),
 ('whole_C9',phys['C9']),('whole_J19',phys['J19'])]
native_unit_records=[]
for label,poly in native_atoms:
 value=weightpoly(poly);inv=value.inv();assert value*inv==1
 native_unit_records.append(dict(label=label,
  wholeQuadraticNormInverseActuallyReturned=True,
  imageDefinition=digest(value.data())))
for name,value in [('u',u),('Q',Q),('ell',ell),('m',m),
 ('delta',delta),('M',M),('P02',P02),('Phi',Phi),('bc',bc)]:
 assert value*(one/value)==1
# Explicit family, including the infinitesimal lambda direction.
L=Dual(half)+eps;T=Dual(-half)
X=Dual(half)+2*(1-e)*eps;Y=Dual(half);tv=Dual()
fv=(e+1)/2-(e-1)*eps
oldimages=[e,k,X,Y,tv,Dual(),Dual(),Dual()]
assert evalR(old['f'],oldimages)==fv
assert evalR(old['lam'],oldimages)==L
assert evalR(old['T'],oldimages)==T
assert evalR(old['A'].a,oldimages)==0 and evalR(old['A'].b,oldimages)==0
rimage=[evalR(old['r'].a,oldimages),evalR(old['r'].b,oldimages)]
simage=[evalR(old['s'].a,oldimages),evalR(old['s'].b,oldimages)]
assert rimage==simage==[2*(2-u)*eps,Dual()]
labels=['E1','EBe','EBo','N1','NS','PS']
original_values=[]
for label in labels:
 value=evalR(old['symbolic'][label],oldimages)
 assert value==0,('complete original I6 failed',label)
 original_values.append(dict(label=label,allFourQQkCoordinatesActuallyZero=True))
say(stage='new_QQ_entire_quadratic_weight_dual_family_complete_I6',
 weightAlgebra='QQ(k)[e]/(4*k*e^2-(k^2+4*k+8)*e-(k^2+6*k+8))',
 noIrreducibilityOrFieldAssumption=True,
 dualRelation='eps^2=0',QQkFreeRank=4,
 originalCoordinates=['ell=1/2','lambda=1/2+eps','T=-1/2',
 'x=1/2+2*(1-e)*eps','y=1/2','t=0','f=(e+1)/2-(e-1)*eps'],
 allOriginalE0N0P1CoordinatesActuallyReturned=True,
 originalGramAZeroAndEqualNilpotentRSActuallyReturned=True,
 nativeOriginalCertificateWeightUnits=native_unit_records,
 completeI6=original_values,
 oldPDeterminantAndQQCharacteristicNotReplayed=True,
 wholeWExcluded=False)
# Same N1 slope coordinate and exact qZ relation of the finite model.
pimages=[e,k,X,Y,L,Dual(),Dual(),Dual()]
aa,cc,dn=[weight(val[n]) for n in ['aa','cc','Delta']]
assert dn*(one/dn)==1
Z=aa*X+cc*Y;pimages[5]=Z
p0,p1,p2=[evalR(co,pimages) for co in val['ns']['nrow']]
assert p0+p1*X+p2*Y==0
assert dn*X==p2*Z+cc*p0
assert dn*Y==-p1*Z-aa*p0
assert evalR(val['xhat'],pimages)==X
assert evalR(val['yhat'],pimages)==Y
assert evalR(phys['tnew'],pimages)==tv
assert evalR(val['qZ'],pimages)==0
assert Z*Z+evalR(val['beta1'],pimages)*Z+evalR(val['beta0'],pimages)==0
# Every actual original coefficient used here has a true norm inverse
# in E; no original D, eps or lambda leading coefficient is inverted.
for co in val['ntag']+val['ns']['ztag']:
 assert all(not any(mon[j] for j in range(2,8)) for mon in co.d.to_dict())
 weightinverse(co.d)
# Full original five additional I11 values. These are evaluated with
# the SAME D and K. All N/P odd parts and N4(V) coefficients exist at
# the family, because their original weight denominators are units.
Al=2*L*L-2*L+1;Bl=4*L**3-6*L*L+3*L-1
Dphys=ell*Al-T*T;Kmom=ell*ell*Bl-3*ell*T*Al+2*T**3
assert Dphys==0 and Kmom==0
Ast=4*u*Q-J;Cst=Ast*m*m+J*delta*ell*ell;cval=3-2*L
ad=M*ell*ell*Q*(3-4*L)+M*Ast*T*T+2*M*u*Q*cval*ell*T+Cst*Dphys
bd=2*M*m*(Ast*T+u*Q*cval*ell)
qt=(2*m*Dphys*ad+Kmom*bd)/(8*m*u*Q*ell*ell*delta)
R6=M*Kmom*Kmom-4*m*m*Dphys**3
nb=evalR(old['N4'](old['rows'][2]).b,oldimages)
pb=evalR(old['P2'](old['rows'][2]).b,oldimages)
A0=1+T/ell
Nlow=Dphys*nb+(2*L*P02/m)*Kmom*A0+(4*L*P02*m/(ell*M))*Dphys*Dphys
Plow=Dphys*pb+(3*P02/(2*m))*Kmom*A0*A0
Plow=Plow+P02*(3*m*m/(ell*ell)+delta)*Kmom*Dphys/(2*m*M)+(6*P02*m/(ell*M))*A0*Dphys*Dphys
Eold=old['E'];Nold=old['N4']
l0=old['l'];m0=old['u']-l0;t0=old['T'];lam0=old['lam']
V0=[Eold(1),Eold(lam0-1-t0),Eold(1+t0/l0),Eold(1+t0/l0)]
V1=[Eold(),Eold(),Eold(m0/l0,-1),Eold(m0/l0,1)]
v0=Nold(V0);v2=Nold(V1)
v1=Nold([V0[j]+V1[j] for j in range(4)])-v0-v2
assert not v0.b and not v1.b and not v2.b
zz0,zz1,zz2=[evalR(v.a,oldimages) for v in [v0,v1,v2]]
Vlow=Dphys*zz0+Kmom*zz1/(2*m)+Dphys*Dphys*zz2/M
extra=[qt,R6,Nlow,Plow,Vlow]
assert all(v==0 for v in extra)
# Images of e and lambda generate this complete rank-four family.
assert e==free_basis[1] and L-half==free_basis[2]
assert e*(L-half)==free_basis[3]
say(stage='new_QQ_dual_family_all_same_model_coordinates_and_I11_return',
 sameN1SlopeCoordinateAndAllForwardReverseProductsReturned=True,
 originalN1AndMonicQZActuallyZero=True,
 actualOriginalDZeroOverQQk=True,actualOriginalKZeroOverQQk=True,
 completeExtraValues=['qT4','R6','Nlow','Plow','entire_Vlow'],
 allFiveCompleteOriginalValuesActuallyZero=True,
 requiredWeightDenominatorDefinitions=len(den_cache),
 fullQuadraticNormInversesReturned=weight_inverse_count,
 exactQQkPolynomialDivisionsReturned=division_count,
 noOriginalDOrGeometricNormInverse=True,
 PAndChiSource='previously proved P in I6 and chi in I4, whose exact native weight units were returned above',
 allFourFamilyBasisVectorsGeneratedByEAndLambda=True,
 modelToFamilySurjective=True,
 independentPreviousGenericDimensionUpperBound=4,
 familyFreeDimensionOverQQk=4,
 genericModelIsomorphicToThisDualFamily=True,
 QQGenericDUnitLocalizationIsZero=True,
 finiteKExceptionsAndEntireH198ZeroRetained=True,
 wholeWExcluded=False,
 familyCoordinateDefinition=digest({n:v.data() for n,v in
  [('e',e),('lambda',L),('Z',Z),('x',X),('y',Y),('t',tv),('f',fv),('T',T)]}),
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 noCoefficientCacheOrEncodedSplitPayloadSaved=True,ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
