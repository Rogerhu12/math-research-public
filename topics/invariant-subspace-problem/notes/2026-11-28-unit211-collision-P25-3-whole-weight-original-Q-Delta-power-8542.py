#!/usr/bin/env python3
"""NEW whole P25,3 collision curve: same original Q-polynomials in the
rank-three weight algebra over QQ(lambda), then original Euclidean
identities and a true Delta power target. Only the three frozen exact-input
JSONs are read. No previous resultant, Gram or cofactor is rerun.
Every scalar lambda denominator is retained; all original head-zero
fibers remain in the final parameter cover. No field/reduced assumption.
180 seconds /4 GiB. A generic return does not exclude its exceptional roots.
"""
import json,time,hashlib,signal,resource,zlib,base64
from pathlib import Path
from flint import fmpq,fmpq_poly
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
started=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-started)
 print(json.dumps(kw,separators=(',',':')),flush=True)
def read(name,sha):
 raw=Path(__file__).with_name(name).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==sha
 return json.loads(raw)
parts=[]
for name,sha in [
 ("2026-11-27-unit211-collision-Delta-nonzero-four-original-exact-input-part1-8542.json","c4723da150647c453cd53151b4e9f84e5d6ed1c45dffcf4c39299b9ef968c3e6"),
 ("2026-11-27-unit211-collision-Delta-nonzero-four-original-exact-input-part2-8542.json","8f8a547ba11ffc2baafd0229f9ffce5a16576206d06460d627927b80d4671682")]:
 data=read(name,sha);parts.append(data["dataChunk"])
raw=zlib.decompress(base64.b64decode("".join(parts)))
assert hashlib.sha256(raw).hexdigest()=="11046373e5362f4b5606e2940483929954a74382e152e40f211fbe79ec42b292"
original=json.loads(raw);assert original["variables"]==["lambda","u","Q"]
manifest=read("2026-11-28-unit211-collision-two-QQ-projections-exact-factor-manifest-8542.json",
 "4a2206f910408ec2ef7bc0a7cc49b24cefe556a226d5bfe66f4c0059d45abb54")
record=next(r for r in manifest["factors"] if r["name"]=="P25-3")
raw=zlib.decompress(base64.b64decode(record["data"]))
assert hashlib.sha256(raw).hexdigest()=="1414ec5c6010ddb33a6e0e471d9bb68dd7070535bfae59472d2948de453ab0ab"
pinput=json.loads(raw)
def pol(v=()):
 if isinstance(v,fmpq_poly):return v
 if isinstance(v,(int,fmpq)):v=[v]
 return fmpq_poly([fmpq(c) for c in v])
zero=pol();one=pol(1);lp=pol([0,1])
def exact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 return q
def monic(p):
 assert p
 return p/p[p.degree()]
def coefficients(p):return [str(c) for c in p.coeffs()]
def pdigest(p):
 raw=json.dumps(coefficients(p),separators=(',',':')).encode()
 return dict(degree=int(p.degree()),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
g=[pol() for _ in range(4)]
for ex,c in pinput["terms"]:
 a,b,q=ex;assert q==0 and b<=3
 g[b]+=fmpq(c)*lp**a
assert g[3] and max(int(p.degree()) for p in g)==25
phead=g[3]
cover=monic(phead)
def record_denominator(p):
 global cover
 if p.degree()<=0:return
 p=monic(p);cover=monic(cover*exact(p,cover.gcd(p)))
class Rat:
 def __init__(self,n=0,d=None):
  if isinstance(n,Rat):self.n=n.n;self.d=n.d;return
  n=pol(n);d=one if d is None else pol(d);assert d
  if not n:self.n=zero;self.d=one;return
  gg=n.gcd(d);n=exact(n,gg);d=exact(d,gg);c=d[d.degree()]
  self.n=n/c;self.d=d/c
 def __bool__(self):return bool(self.n)
 def __neg__(self):return Rat(-self.n,self.d)
 def __add__(self,v):
  v=Rat(v);gg=self.d.gcd(v.d);a=exact(self.d,gg);b=exact(v.d,gg)
  return Rat(self.n*b+v.n*a,a*v.d)
 __radd__=__add__
 def __sub__(self,v):return self+-Rat(v)
 def __rsub__(self,v):return Rat(v)+-self
 def __mul__(self,v):
  v=Rat(v);gg=self.n.gcd(v.d);hh=v.n.gcd(self.d)
  return Rat(exact(self.n,gg)*exact(v.n,hh),exact(self.d,hh)*exact(v.d,gg))
 __rmul__=__mul__
 def __truediv__(self,v):
  v=Rat(v);assert v
  return self*Rat(v.d,v.n)
def reduce_numerators(cc):
 cc=list(cc)
 while len(cc)<3:cc.append(zero)
 denominator=one
 for j in range(len(cc)-1,2,-1):
  lead=cc[j]
  if lead:
   for i in range(j):cc[i]=cc[i]*phead
   for i in range(3):cc[j-3+i]=cc[j-3+i]-lead*g[i]
   cc[j]=zero;denominator*=phead
 assert not any(cc[3:])
 return tuple(cc[:3]),denominator
def cgcd(dd,nn):
 gg=dd
 for p in nn:
  if p:gg=gg.gcd(p)
  if gg.degree()==0:break
 return gg
inverses=[];inverse_cache={}
class Nonunit(Exception):pass
class A:
 """The ENTIRE rank-three algebra, without assuming a field or reduced."""
 def __init__(self,v=0,d=None):
  if isinstance(v,A) and d is None:self.n=v.n;self.d=v.d;return
  if isinstance(v,Rat) and d is None:v,d=v.n,v.d
  if not isinstance(v,(tuple,list)):v=[pol(v)]
  else:v=[pol(c) for c in v]
  nn,rd=reduce_numerators(v);dd=rd*(one if d is None else pol(d));assert dd
  if not any(nn):self.n=(zero,)*3;self.d=one;return
  gg=cgcd(dd,nn)
  if gg.degree()>0:nn=tuple(exact(n,gg) for n in nn);dd=exact(dd,gg)
  c=dd[dd.degree()];self.n=tuple(n/c for n in nn);self.d=dd/c
 @staticmethod
 def accepts(v):return isinstance(v,(A,Rat,fmpq_poly,fmpq,int,tuple,list))
 def __bool__(self):return any(self.n)
 def __neg__(self):return A(tuple(-n for n in self.n),self.d)
 def __add__(self,v):
  if not self.accepts(v):return NotImplemented
  v=A(v)
  if not self:return v
  if not v:return self
  gg=self.d.gcd(v.d);a=exact(self.d,gg);b=exact(v.d,gg)
  return A(tuple(x*b+y*a for x,y in zip(self.n,v.n)),a*v.d)
 __radd__=__add__
 def __sub__(self,v):
  if not self.accepts(v):return NotImplemented
  return self+-A(v)
 def __rsub__(self,v):
  if not self.accepts(v):return NotImplemented
  return A(v)+-self
 def __mul__(self,v):
  if not self.accepts(v):return NotImplemented
  v=A(v)
  if not self or not v:return A()
  gg=cgcd(v.d,self.n);hh=cgcd(self.d,v.n)
  aa=[exact(n,gg) for n in self.n];bb=[exact(n,hh) for n in v.n]
  cc=[pol() for _ in range(5)]
  for i,x in enumerate(aa):
   for j,y in enumerate(bb):
    if x and y:cc[i+j]+=x*y
  return A(cc,exact(self.d,hh)*exact(v.d,gg))
 __rmul__=__mul__
 def __eq__(self,v):
  if not self.accepts(v):return False
  v=A(v);return all(x*v.d==y*self.d for x,y in zip(self.n,v.n))
 def inverse(self,label="actual whole cubic-algebra inverse"):
  if not self:raise Nonunit(label+": zero")
  if self==1:return A(1)
  key=tuple(str(n) for n in self.n)+(str(self.d),)
  if key in inverse_cache:return inverse_cache[key]
  if not any(self.n[1:]):out=A(self.d,self.n[0])
  else:
   cols=[self*A([0]*j+[1]) for j in range(3)]
   mm=[[cols[j].n[i] for j in range(3)]+[one if i==0 else zero] for i in range(3)]
   previous=one
   for j in range(2):
    if not mm[j][j]:
     sw=next((i for i in range(j+1,3) if mm[i][j]),None)
     if sw is None:raise Nonunit(label+": actual multiplication norm zero")
     mm[j],mm[sw]=mm[sw],mm[j]
    pivot=mm[j][j]
    for i in range(j+1,3):
     for h in range(j+1,4):
      mm[i][h]=exact(mm[i][h]*pivot-mm[i][j]*mm[j][h],previous)
     mm[i][j]=zero
    previous=pivot
   if not mm[2][2]:raise Nonunit(label+": actual multiplication norm zero")
   sol=[Rat() for _ in range(3)]
   for i in range(2,-1,-1):
    sol[i]=(Rat(mm[i][3])-sum((Rat(mm[i][j])*sol[j] for j in range(i+1,3)),Rat()))/Rat(mm[i][i])
   sol=[s*Rat(c.d) for s,c in zip(sol,cols)]
   den=one
   for c in sol:den=monic(den*exact(c.d,den.gcd(c.d)))
   out=A([c.n*exact(den,c.d) for c in sol],den)
  assert self*out==1
  record_denominator(self.d);record_denominator(out.d)
  inverse_cache[key]=out
  inverses.append(dict(label=label,inputDenominator=pdigest(self.d),inverseDenominator=pdigest(out.d)))
  return out
 def __truediv__(self,v):
  if not self.accepts(v):return NotImplemented
  return self*A(v).inverse()
 def __rtruediv__(self,v):
  if not self.accepts(v):return NotImplemented
  return A(v)*self.inverse()
 def __pow__(self,n):
  if n<0:return self.inverse()**(-n)
  ans=A(1);v=self
  while n:
   if n&1:ans=ans*v
   n//=2
   if n:v=v*v
  return ans
 def data(self):return dict(n=[coefficients(p) for p in self.n],d=coefficients(self.d))
 def complexity(self):return max([int(p.degree()) for p in self.n]+[int(self.d.degree())])
lam=A(lp);u=A([0,1])
assert sum((A(c)*u**i for i,c in enumerate(g)),A())==0
say("new_entire_P25_3_whole_cubic_weight_algebra",
 originalUDegree=3,originalULeading=pdigest(phead),allLeadingZeroFibersRetained=True,
 originalRelationActuallyReturned=True,noFieldOrReducedAssumption=True)
class U:
 def __init__(self,v=0):
  if isinstance(v,U):self.c=list(v.c);return
  self.c=[A(c) for c in v] if isinstance(v,(tuple,list)) else [A(v)]
  while self.c and not self.c[-1]:self.c.pop()
 def __bool__(self):return bool(self.c)
 def __neg__(self):return U([-c for c in self.c])
 def __add__(self,v):
  v=U(v);n=max(len(self.c),len(v.c))
  return U([(self.c[i] if i<len(self.c) else A())+(v.c[i] if i<len(v.c) else A()) for i in range(n)])
 __radd__=__add__
 def __sub__(self,v):return self+-U(v)
 def __rsub__(self,v):return U(v)+-self
 def __mul__(self,v):
  v=U(v)
  if not self or not v:return U()
  cc=[A() for _ in range(len(self.c)+len(v.c)-1)]
  for i,x in enumerate(self.c):
   for j,y in enumerate(v.c):
    if x and y:cc[i+j]=cc[i+j]+x*y
  return U(cc)
 __rmul__=__mul__
 def __eq__(self,v):
  v=U(v);return len(self.c)==len(v.c) and all(x==y for x,y in zip(self.c,v.c))
 def __pow__(self,n):
  ans=U(1);v=self
  while n:
   if n&1:ans=ans*v
   n//=2
   if n:v=v*v
  return ans
 def degree(self):return len(self.c)-1
 def complexity(self):return max((c.complexity() for c in self.c),default=-1)
 def data(self):return [c.data() for c in self.c]
 def normalize(self,label):
  if not self:return self
  iv=self.c[-1].inverse(label)
  out=U([c*iv for c in self.c])
  assert out*self.c[-1]==self and out.c[-1]==1
  return out
divisions=0;trace=hashlib.sha256()
def divide(a,b,label):
 global divisions
 a=U(a);b=U(b);assert b;original=U(a)
 iv=b.c[-1].inverse(label+" Q-leading")
 quotient=[A() for _ in range(max(0,len(a.c)-len(b.c)+1))]
 while a and len(a.c)>=len(b.c):
  shift=len(a.c)-len(b.c);c=a.c[-1]*iv
  quotient[shift]=quotient[shift]+c
  cc=a.c[:]
  for i,v in enumerate(b.c):cc[shift+i]=cc[shift+i]-c*v
  a=U(cc)
 q=U(quotient)
 assert q*b+a==original and a.degree()<b.degree()
 divisions+=1
 # All coefficient products above were actually returned. Retain a compact
 # digest of the composed division identities, not a giant coefficient cache.
 for p in (original,b,q,a):
  trace.update(json.dumps(p.data(),separators=(',',':')).encode());trace.update(b"\n")
 return q,a
def euclid(a,b,label):
 a=U(a);b=U(b);step=0
 while b:
  q,r=divide(a,b,label)
  a,b=b,r;step+=1
  say("new_original_whole_cubic_Q_division_returned",pair=label,step=step,
      divisorDegree=a.degree(),remainderDegree=b.degree(),
      coefficientLambdaDegree=max(a.complexity(),b.complexity()),
      allThreeWeightComponentsOfDivisionIdentityReturned=True,
      retainedLambdaCoverDegree=int(cover.degree()))
 return a.normalize(label+" final actual Q head")
values={}
for name,terms in original["polynomials"].items():
 maxq=max(ex[2] for ex,c in terms);maxu=max(ex[1] for ex,c in terms)
 grid=[[pol() for _ in range(maxu+1)] for _ in range(maxq+1)]
 for (a,b,q),c in terms:grid[q][b]+=fmpq(c)*lp**a
 coeff=[]
 for col in grid:
  v=A()
  for c in reversed(col):v=v*u+A(c)
  coeff.append(v)
 values[name]=U(coeff)
 for c in coeff:record_denominator(c.d)
 say("new_saved_same_original_Q_polynomial_on_entire_cubic_weight",
     original=name,QDegree=values[name].degree(),lambdaDegree=values[name].complexity(),
     noPreviousMeanCofactorOrProjectionRerun=True,
     allCoefficientDenominatorsRetained=True)
# Delta is the ACTUAL unscaled determinant in the same original chart.
Q=U([0,1]);A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam**2+3*lam-1
xi=B3/A2;ell=A2**3/(B3**2)
T0=2*u-ell*Q-2*u*u
J=2*u*(1-u)+ell*Q
Phi=T0+4*u-4+Q
S=2*xi+3-2*lam;eta=xi+3-2*lam
NF=(3-4*lam)*Q+J*xi*eta
Delta=Phi*NF-S*xi*T0*(J-Q)
assert Delta and Delta.degree()<=2
for c in Delta.c:record_denominator(c.d)
say("new_actual_collision_Delta_target_on_entire_cubic_weight",
    QDegree=Delta.degree(),lambdaDegree=Delta.complexity(),
    originalFormula="Phi*NF-S*xi*T0*(J-Q)",
    originalDeltaNonzeroAlreadyPaidByEntireOriginalDeltaZeroExclusion=True)
returned=False;power=None;current=values["R"];used=["R"];nonunit=None
try:
 for name in ["W","O","N1"]:
  current=euclid(current,values[name],"same original "+",".join(used+[name]))
  used.append(name)
  for exponent in range(1,5):
   target=Delta**exponent
   quotient,remainder=divide(target,current,"actual Delta power "+str(exponent))
   if not remainder:
    assert quotient*current==target
    returned=True;power=exponent
    for c in quotient.c:record_denominator(c.d)
    say("new_actual_Delta_power_return_in_original_Q_ideal",
        usedOriginalRows=used,DeltaPower=power,commonQDegree=current.degree(),
        completeActualTargetProductReturned=True,
        everyEuclideanDivisionAndNormalizationAlreadyReturned=True,
        originalIdealCertificateByCompositionOfActualIdentities=True,
        genericExclusionOnly=True,allLambdaDenominatorZeroFibersRetained=True)
    break
  if returned:break
except Nonunit as ex:
 nonunit=str(ex)
 say("new_entire_cubic_original_nonunit_head_retained",
     reason=nonunit,noComponentDiscarded=True,genericExclusionNotClaimed=True)
if not returned:
 say("new_entire_cubic_original_Delta_power_not_yet_returned",
     usedOriginalRows=used,currentQDegree=current.degree(),
     testedPowers=[1,2,3,4],nonunit=nonunit,
     noNonmembershipOrEmptinessClaim=True)
for c in current.c:record_denominator(c.d)
assert cover
sf=monic(exact(cover,cover.gcd(cover.derivative())))
# Strip only globally paid scalar lambda units of the entire h=k chart.
# G2/C4 and every other new Q-leading or u-leading zero remain.
paid=[("lambda",lp),("A",2*lp**2-2*lp+1),
      ("B",4*lp**3-6*lp**2+3*lp-1),
      ("S",(2*lp-1)*(2*lp**2-1)),("entire_J2",3*lp**2-2*lp+1)]
removed=[]
for label,atom in paid:
 gg=sf.gcd(atom)
 if gg.degree()>0:
  old=sf;sf=monic(exact(sf,gg))
  assert monic(sf*gg)==monic(old)
  removed.append(dict(originalUnit=label,removedDegree=int(gg.degree())))
payload=json.dumps(coefficients(sf),separators=(',',':')).encode()
encoded=base64.b64encode(zlib.compress(payload,9)).decode()
assert zlib.decompress(base64.b64decode(encoded))==payload
chunks=[encoded[i:i+75000] for i in range(0,len(encoded),75000)]
say("new_entire_P25_3_original_generic_return_complete_parameter_cover",
    genericOriginalDeltaPowerReturned=returned,DeltaPower=power,
    exactCover=pdigest(sf),onlyPreviouslyPaidScalarUnitsRemoved=removed,
    completeULeadingAndAllOriginalQLeadingZeroFibersRetained=True,
    coverZeroFibersEntirelyStillOpen=True,
    onlySomePowerOfCoverInOriginalLocalizedIdealNotFirstPower=True,
    allIndividualNPStillRequired=True,ordinaryISPClaim=False)
say("new_cubic_weight_exact_lambda_cover_encoding",
    rawBytes=len(payload),rawSHA256=hashlib.sha256(payload).hexdigest(),
    chunks=len(chunks),base64Characters=len(encoded),maximumChunkCharacters=75000)
for i,chunk in enumerate(chunks):
 say("new_cubic_weight_exact_lambda_cover_chunk",index=i,total=len(chunks),data=chunk)
say("new_entire_cubic_weight_Delta_power_attempt_finished",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    originalRowsUsed=used,actualInverseProducts=len(inverses),
    actualOriginalQDivisionProducts=divisions,
    actualComposedDivisionCertificateSHA256=trace.hexdigest(),
    genericOriginalDeltaPowerReturned=returned,DeltaPower=power,
    wholeCubicWeightCurveExcluded=False,wholeCollisionChartExcluded=False,
    ordinaryISPClaim=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
