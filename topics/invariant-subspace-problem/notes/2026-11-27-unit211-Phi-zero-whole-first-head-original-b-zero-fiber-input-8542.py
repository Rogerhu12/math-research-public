#!/usr/bin/env python3
"""NEW saved original linear-head b(lambda)=0 fiber on the WHOLE H1 curve.
Read the exact L=a*T+b*z+c already returned before the frozen timeout.
No original L reconstruction, old D cancellation, or lambda Euclid.
The NEW b-zero fiber recovers lambda in the entire Q-quartic algebra;
retain every u pole. Return the same T equation, actual D and F6 first,
then only if needed the same original z-quadratics and full NV.
A generic unit is never called a global original unit: its entire
exceptional u cover remains, with all four Q roots retained.
2026-11-28 Asia/Taipei. 120 seconds /1GiB. One pinned exact JSON.
"""
import time,json,hashlib,zlib,base64,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_poly
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
started=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-started)
 print(json.dumps(kw,separators=(",",":")),flush=True)
def pol(v=()):
 if isinstance(v,fmpq_poly):return v
 if isinstance(v,(int,fmpq)):v=[v]
 return fmpq_poly([fmpq(c) for c in v])
zero=pol();one=pol(1);up=pol([0,1])
def exact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 return q
def monic(p):
 assert p
 return p/p[p.degree()]
def coefficients(p):return [str(c) for c in p.coeffs()]
def pdigest(p):
 raw=json.dumps(coefficients(p),separators=(",",":")).encode()
 return dict(degree=int(p.degree()),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
# g=-12*H1, the actual first quadratic-head residual. Its Q head is 1.
g=[pol([64,-272,512,-544,336,-112,16]),
   pol([-112,348,-496,440,-248,80,-12]),
   pol([60,-123,104,-52,13]),
   pol([-13,fmpq(53,4),-3]),one]
cover=one
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
 while len(cc)<4:cc.append(zero)
 for j in range(len(cc)-1,3,-1):
  lead=cc[j]
  if lead:
   for i in range(4):cc[j-4+i]=cc[j-4+i]-lead*g[i]
   cc[j]=zero
 assert not any(cc[4:])
 return tuple(cc[:4]),one
def cgcd(dd,nn):
 gg=dd
 for p in nn:
  if p:gg=gg.gcd(p)
  if gg.degree()==0:break
 return gg
inverses=[];inverse_cache={}
class Nonunit(Exception):pass
class A:
 """The ENTIRE rank-four algebra, without assuming a field or reduced."""
 def __init__(self,v=0,d=None):
  if isinstance(v,A) and d is None:self.n=v.n;self.d=v.d;return
  if isinstance(v,Rat) and d is None:v,d=v.n,v.d
  if not isinstance(v,(tuple,list)):v=[pol(v)]
  else:v=[pol(c) for c in v]
  nn,rd=reduce_numerators(v);dd=rd*(one if d is None else pol(d));assert dd
  if not any(nn):self.n=(zero,)*4;self.d=one;return
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
  cc=[pol() for _ in range(7)]
  for i,x in enumerate(aa):
   for j,y in enumerate(bb):
    if x and y:cc[i+j]+=x*y
  return A(cc,exact(self.d,hh)*exact(v.d,gg))
 __rmul__=__mul__
 def __eq__(self,v):
  if not self.accepts(v):return False
  v=A(v);return all(x*v.d==y*self.d for x,y in zip(self.n,v.n))
 def inverse(self,label="actual whole Q-quartic-algebra inverse"):
  if not self:raise Nonunit(label+": zero")
  if self==1:return A(1)
  key=tuple(str(n) for n in self.n)+(str(self.d),)
  if key in inverse_cache:return inverse_cache[key]
  if not any(self.n[1:]):out=A(self.d,self.n[0])
  else:
   cols=[self*A([0]*j+[1]) for j in range(4)]
   mm=[[cols[j].n[i] for j in range(4)]+[one if i==0 else zero] for i in range(4)]
   previous=one
   for j in range(3):
    if not mm[j][j]:
     sw=next((i for i in range(j+1,4) if mm[i][j]),None)
     if sw is None:raise Nonunit(label+": actual multiplication norm zero")
     mm[j],mm[sw]=mm[sw],mm[j]
    pivot=mm[j][j]
    for i in range(j+1,4):
     for h in range(j+1,5):
      mm[i][h]=exact(mm[i][h]*pivot-mm[i][j]*mm[j][h],previous)
     mm[i][j]=zero
    previous=pivot
   if not mm[3][3]:raise Nonunit(label+": actual multiplication norm zero")
   sol=[Rat() for _ in range(4)]
   for i in range(3,-1,-1):
    sol[i]=(Rat(mm[i][4])-sum((Rat(mm[i][j])*sol[j] for j in range(i+1,4)),Rat()))/Rat(mm[i][i])
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
 iv=b.c[-1].inverse(label+" z-leading")
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
  say("new_original_whole_quartic_z_division_returned",pair=label,step=step,
      divisorDegree=a.degree(),remainderDegree=b.degree(),
      coefficientUDegree=max(a.complexity(),b.complexity()),
      allFourWeightComponentsOfDivisionIdentityReturned=True,
      retainedUCoverDegree=int(cover.degree()))
 return a.normalize(label+" final actual z head")


def exact_checkpoint(label,obj):
 raw=json.dumps(obj,separators=(",",":")).encode()
 encoded=base64.b64encode(zlib.compress(raw,9)).decode()
 assert zlib.decompress(base64.b64decode(encoded))==raw
 pieces=[encoded[i:i+75000] for i in range(0,len(encoded),75000)]
 say("new_H1_b_zero_exact_checkpoint",label=label,rawBytes=len(raw),
     rawSHA256=hashlib.sha256(raw).hexdigest(),chunks=len(pieces),
     maximumChunkCharacters=75000)
 for i,data in enumerate(pieces):
  say("new_H1_b_zero_exact_checkpoint_chunk",label=label,index=i,total=len(pieces),data=data)
def decodeA(rec):
 out=A([pol(c) for c in rec["n"]],pol(rec["d"]))
 for d in [pol(rec["d"]),out.d]:record_denominator(d)
 assert all(out.n[i]*pol(rec["d"])==pol(rec["n"][i])*out.d for i in range(4))
 return out
def horner(row,value):
 out=A()
 for v in reversed(row):out=out*value+v
 return out
def original_b_zero_input():
 inp=Path(__file__).with_name("2026-11-27-unit211-Phi-zero-whole-first-head-original-linear-relation-exact-input-8542.json").read_bytes()
 assert hashlib.sha256(inp).hexdigest()=="c6c0b8973ea18a3fd320921238a7e331e460ca26ed1d96ec5f4e6276fd45ff44"
 saved=json.loads(inp)
 assert saved["producer"]["sourceSHA256"]=="7dfa17a6a871f6a2c1be4773d58f096f3a3252bcffbc61c8f6f766302bc8ea2e"
 assert saved["coefficientOrder"]==["a","b","c"]
 assert [pol(c) for c in saved["monicQRelationCoefficientsAscendingU"]]==g
 la,lb,lc=[[decodeA(v) for v in row] for row in saved["coefficientData"]]
 assert [len(la),len(lb),len(lc)]==[2,2,3]
 u=A(up);Q=A([0,1])
 assert sum((A(c)*(Q**i) for i,c in enumerate(g)),A())==0
 # This is the NEW geometric head b(lambda)=0. Its base-parameter
 # exceptional fibers are kept by the final u cover, not declared paid.
 lam=-(lb[0]*lb[1].inverse("NEW b(lambda)=0 actual whole-algebra leading"))
 assert horner(lb,lam)==0
 aa=horner(la,lam);cc=horner(lc,lam)
 say("new_H1_actual_b_zero_lambda_recovery",wholeQAlgebraRank=4,
     allFourComponentsOfOriginalBEquationReturned=True,
     oldLinearRelationNotRecomputed=True,
     lambdaNumeratorDegrees=[int(p.degree()) for p in lam.n],
     lambdaDenominatorDegree=int(lam.d.degree()),
     TLeadingIdenticallyZero=(not aa),constantIdenticallyZero=(not cc),
     everyNewBaseParameterPoleRetained=True)
 exact_checkpoint("new_lambda_and_remaining_original_linear_relation",
                  dict(lambdaValue=lam.data(),TLeading=aa.data(),constant=cc.data()))
 if not lam:
  say("new_H1_b_zero_generic_branch_excluded_by_original_lambda_unit",
      originalLambdaExactlyZero=True,weightZeroFibersRemain=True)
  return True
 if not aa:
  if not cc:
   say("accurate_new_H1_b_zero_original_linear_relation_degenerates",
       noTRecovery=True,noGenericExclusionClaim=True,
       wholeOriginalWeightAlgebraRetained=True)
   return False
  inv=cc.inverse("NEW b0 a0 remaining actual original constant")
  assert cc*inv==1
  say("new_H1_b_zero_generic_branch_excluded_by_original_linear_constant",
      completeWholeWeightUnitProductReturned=True,weightZeroFibersRemain=True)
  return True
 Tr=-(cc*aa.inverse("NEW b0 original T linear leading"))
 assert horner(la,lam)*Tr+horner(lc,lam)==0
 ell=1-2*(u-1)*(u-2)/Q
 delta=1-Q;m=u-ell;V2=2*u-ell*Q;T0=V2-2*u*u
 J=2*u*(1-u)+ell*Q
 P02=(2-3*u)*V2-Q*u+2*u**3;Pf=T0*(J-Q)
 M=ell*V2-u*u;bc=M/(4*delta)
 A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1
 G=lam*P02+(u-1)*T0;Pc=Q*P02*(ell+Tr)-G*T0
 ff=-Pc/Pf
 assert Pf*ff+Pc==0
 assert T0+4*u-4+Q==0 and J-Q==-4*(u-1)**2
 DD=ell*A2-Tr*Tr
 KK=ell*ell*B3-3*ell*Tr*A2+2*Tr**3
 F6=M*KK*KK-4*m*m*DD**3
 exact_checkpoint("new_original_b_zero_T_D_and_F6",
  dict(TValue=Tr.data(),physicalD=DD.data(),originalF6=F6.data()))
 say("new_H1_b_zero_original_moment_return",
     completeOriginalTLinearEquationReturned=True,
     originalPhysicalDExactlyZero=(not DD),originalF6ExactlyZero=(not F6),
     actualOriginalWeightsAndP1Retained=True,
     noPhysicalDNormInverseUsed=True,
     onlyOnSavedOriginalBZeroBranch=True)
 if not DD:
  say("new_H1_b_zero_generic_branch_excluded_by_original_physical_D",
      actualOriginalDExactlyZero=True,weightZeroFibersRemain=True)
  return True
 if F6:
  try:
   inverse=F6.inverse("NEW actual original F6 scalar contradiction")
   assert F6*inverse==1
   say("new_H1_b_zero_generic_branch_excluded_by_complete_original_F6",
       completeFourComponentOriginalF6UnitProductReturned=True,
       noF6ZeroWeightFiberDiscarded=True,
       allInversePoleRootsRetainedInFiniteBaseCover=True)
   return True
  except Nonunit:
   say("new_H1_b_zero_F6_nonunit_components_retained",
       noAlgebraComponentDiscarded=True,noConclusionFromThisScalar=True)
 # Only if the preceding ORIGINAL scalar equations leave a component:
 # construct the real four original z-quadratics, with the same lambda/T.
 z=U([0,1])
 aweight=1-ell
 vn=J*ff-G+bc*z
 wstar=T0+4*u*ff
 nn=Q*wstar-2*vn
 ww=lam-1-Tr
 ii=((vn+aweight*u*Q)**2-2*u*Q*vn+2*aweight*u*u*Q*Q
     -4*aweight*u*Q*Q*ff+bc*z*z+z*(4*bc*u*Q-ell*vn))
 Rbar=ii+(m/(2*delta))*z*nn
 W4=(8*bc*delta*Q*Q*ell*T0-4*ell*delta*vn*vn-ell*nn*nn
     +4*m*vn*nn+32*bc*delta*Q*ff*vn+16*bc*bc*delta*z*z
     +32*bc*bc*delta*Q*(u-1)*z-8*bc*ell*delta*z*vn+4*bc*m*z*nn)
 s0=2*ell*vn-(m/delta)*nn
 d0=-2*m*vn+ell*nn
 Obar=(32*bc*bc*aweight*Q*Q*delta*(u-1)+4*bc*Q*delta*s0
       +32*bc*bc*Q*delta*vn-64*bc*bc*Q*Q*delta*ff
       +4*bc*Q*(1-u+2*ff)*d0-s0*d0-8*bc*bc*m*z*z
       -16*bc*bc*Q*z*(m*(u-1)+ell*delta)+8*bc*bc*z*nn)
 al=ell*(1-u)-m
 ber=ell*delta-m*(1-u)
 av=(2*u-1)*ell+3*m
 bur=(2*u-1)*m+3*ell*delta
 Nstar=(al*(4*delta*vn*vn+nn*nn)+4*ber*vn*nn
        +8*bc*delta*Q*vn*wstar-24*bc*delta*Q*Q*ff*wstar
        +16*aweight*bc*delta*Q*Q*(u-1)*wstar+64*bc*delta*Q*Q*u*ff*ff
        -32*bc*delta*Q*u*ff*vn+16*bc*delta*Q*Q*(1+aweight)*T0*ff
        +16*bc*delta*Q*(aweight*Q-T0)*vn+4*bc*delta*av*z*vn
        -2*bc*bur*z*nn+16*bc*bc*delta*Q*z*(2*ff+T0-aweight*Q)
        -8*u*bc*bc*delta*z*z)
 N1=Nstar-16*bc*delta*Q*Q*lam*P02*ww
 rows=[U(p) for p in [Rbar,W4,Obar,N1]]
 assert all(p.degree()<=2 for p in rows)
 for p in rows:
  for c in p.c:record_denominator(c.d)
 say("new_H1_b_zero_same_source_original_z_quadratics",
     zDegrees=[p.degree() for p in rows],
     noOriginalMeanReconstructionUsedAsOldAuditGate=True,
     originalNoTOrLambdaVariableRemains=True)
 current=U()
 for label,p in zip(["R","W","O","N1"],rows):
  current=euclid(current,p,"NEW b-zero original "+label)
  if current.degree()==0:break
 if current.degree()>0:
  sn=ell*B3-A2*Tr;zn=Tr*B3-A2*A2
  Znum=u*sn-2*Tr*DD;Snum=sn+(3-2*lam)*DD
  NF4=4*m*((3-4*lam)*Q*DD*DD-J*zn*DD)+2*Snum*(-2*u*Q*KK+J*Znum)
  NC4=(4*m*G*zn*DD-2*G*Snum*Znum-Q*T0*Snum*KK
       +4*m*Q*ww*u*(3-2*lam)*DD*DD
       +2*m*Q*ww*u*sn*DD-2*Q*ww*(u-ell*Q)*KK*DD)
  NV=U(NF4*ff+NC4)+2*bc*Snum*Znum*z
  assert NV.degree()<=1
  current=euclid(current,NV,"NEW b-zero complete original NV")
 say("new_H1_b_zero_original_value_ideal_return",
     remainingZDegree=current.degree(),
     wholeFourComponentOriginalUnitReturned=(current.degree()==0),
     entireBZeroBranchOnlyOutsideBaseCover=(current.degree()==0),
     wholeH1CurveExcluded=False,ordinaryISPClaim=False)
 return current.degree()==0

generic_closed=False
try:
 generic_closed=bool(original_b_zero_input())
except Nonunit as exc:
 say("accurate_new_H1_b_zero_actual_nonunit_retained",
     reason=str(exc),noWeightComponentDiscarded=True,
     noGenericOrWholeCurveExclusionClaim=True)
sf=monic(exact(cover,cover.gcd(cover.derivative())))
removed=[]
for label,p in [("u",up),("u-1",up-one)]:
 gg=sf.gcd(p)
 if gg.degree()>0:
  old=sf;sf=monic(exact(sf,gg));assert monic(sf*gg)==monic(old)
  removed.append([label,int(gg.degree())])
say("complete_new_H1_b_zero_original_weight_cover",
    genericBZeroBranchActuallyExcluded=generic_closed,
    exactSquarefreeBaseUCover=pdigest(sf),
    onlyPaidScalarFactorsRemoved=removed,
    coversEveryOriginalBZeroWeightPair=generic_closed,
    differentWeightPairUpperBound=(4*int(sf.degree()) if generic_closed else None),
    countsWeightsNotAllPossibleValues=True,
    allUnpaidCoverZeroFibersRemainForOriginalReturn=True,
    entireH1CurveExcluded=False,wholePhiFaceExcluded=False,ordinaryISPClaim=False)
exact_checkpoint("new_b_zero_weight_cover",
 dict(variable="u",coefficientsAscending=coefficients(sf),
      scope="only original whole H1 curve and saved cleared b(lambda)=0 branch",
      genericOriginalExclusionReturned=generic_closed))
say("new_H1_b_zero_original_attempt_finished",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    actualWholeAlgebraInverseProducts=len(inverses),
    actualNewZDivisionProducts=divisions,
    actualNewDivisionTraceSHA256=trace.hexdigest(),
    peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    oldLambdaEuclidNotRepeated=True,
    entireH1CurveExcluded=False,ordinaryISPClaim=False)
signal.alarm(0)
