#!/usr/bin/env python3
"""NEW entire main H7 constant weight algebra and original linear relation.
Uses saved whole-H1 L and paid b=0 weight cover, not P6/P9 on H7=0.
The original R/W/N1 are homogenized by the SAME L; fixed T2/T2
resultants and the actual D target are new finite-number-algebra inputs.
All algebra inverses are checked on the whole quotient, no field claim.
Nonunits or unreturned fibers are retained. 120 seconds /1 GiB.
2026-11-28 Asia/Taipei.
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
zero=pol();one=pol(1);vp=pol([0,1])
def exact(p,q):
 a,b=divmod(p,q);assert not b and a*q==p
 return a
def monic(p):
 assert p
 return p/p[p.degree()]
def coeff(p):return [str(c) for c in p.coeffs()]
def digest(p):
 raw=json.dumps(coeff(p),separators=(",",":")).encode()
 return dict(degree=int(p.degree()),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def read(name,sha):
 raw=Path(__file__).with_name(name).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==sha,name
 return json.loads(raw)
def checkpoint(label,obj):
 raw=json.dumps(obj,separators=(",",":")).encode()
 enc=base64.b64encode(zlib.compress(raw,9)).decode()
 assert zlib.decompress(base64.b64decode(enc))==raw
 pcs=[enc[i:i+75000] for i in range(0,len(enc),75000)]
 say("new_H7_exact_checkpoint",label=label,rawBytes=len(raw),
  rawSHA256=hashlib.sha256(raw).hexdigest(),chunks=len(pcs),encodedCharacters=len(enc))
 for i,p in enumerate(pcs):
  say("new_H7_exact_checkpoint_chunk",label=label,index=i,total=len(pcs),data=p)
saved=read(
 "2026-11-27-unit211-Phi-zero-whole-first-head-original-linear-relation-exact-input-8542.json",
 "c6c0b8973ea18a3fd320921238a7e331e460ca26ed1d96ec5f4e6276fd45ff44")
cvpart=read(
 "2026-11-27-unit211-Phi-zero-H1-b-zero-u-cover-exact-part-01-8542.json",
 "73e1dacb455ecabb933dbdbfe3c967ff03191554dce2ee82c54d7c0ac8172b75")
raw=zlib.decompress(base64.b64decode(cvpart["dataChunk"]))
assert len(raw)==89101 and hashlib.sha256(raw).hexdigest()=="bfb03f2fe2a96360d2930f0ca81733b9e08f503f6889cd5d3c09fbf80a6882dc"
cvobj=json.loads(raw);assert cvobj["variable"]=="u" and cvobj["genericOriginalExclusionReturned"]
cv=pol(cvobj["coefficientsAscending"]);assert cv.degree()==316 and cv[316]==1
h7=monic(pol([1,2,-4,42,15,-12,36,48]))
assert h7.gcd(h7.derivative()).degree()==0
cvh=zero
for c0 in reversed(cv.coeffs()):
 prev=cvh*(1+vp)+c0;q0,cvh=divmod(prev,h7);assert q0*h7+cvh==prev
retained=monic(h7.gcd(cvh))
phi=monic(exact(h7,retained))
assert retained*phi==h7
assert retained.gcd(phi).degree()==0
say("new_H7_complete_paid_b_zero_cover_intersection",
 entireH7Ascending=coeff(h7),
 savedOriginalBZeroCoverDegree=316,
 completeOriginalUEqualsOnePlusVSubstitutionReturned=True,
 retainedBZeroWeightFactorAscending=coeff(retained),
 workingComplementFactorAscending=coeff(phi),
 everyRetainedCommonFactorStillUnpaid=True,
 originalBCoefficientNonzeroOnWorkingActualPoints=True,
 noP6P9EquationUsedOnH7=True)
if phi.degree()==0:
 say("accurate_H7_all_weights_remain_in_paid_cover_zero",
  wholeH7Excluded=False,noOriginalFiniteAlgebraInverseAttempted=True)
 signal.alarm(0);raise SystemExit(0)
inverse_count=0;reduction_count=0;inverse_cache={}
class Nonunit(Exception):pass
def red(p):
 global reduction_count
 q,r=divmod(p,phi);assert q*phi+r==p
 reduction_count+=1
 return r
class A:
 """Whole QQ[v]/phi, with every inverse verified; no irreducibility assumed."""
 def __init__(self,v=0):
  self.p=v.p if isinstance(v,A) else red(pol(v))
 @staticmethod
 def accepts(v):return isinstance(v,(A,fmpq_poly,fmpq,int,tuple,list))
 def __bool__(self):return bool(self.p)
 def __neg__(self):return A(-self.p)
 def __add__(self,v):
  if not self.accepts(v):return NotImplemented
  return A(self.p+A(v).p)
 __radd__=__add__
 def __sub__(self,v):
  if not self.accepts(v):return NotImplemented
  return A(self.p-A(v).p)
 def __rsub__(self,v):
  if not self.accepts(v):return NotImplemented
  return A(v)-self
 def __mul__(self,v):
  if not self.accepts(v):return NotImplemented
  return A(self.p*A(v).p)
 __rmul__=__mul__
 def __eq__(self,v):return self.accepts(v) and self.p==A(v).p
 def inverse(self,label="whole H7 algebra inverse"):
  global inverse_count
  if not self:raise Nonunit(label+": zero")
  key=tuple(coeff(self.p))
  if key in inverse_cache:return inverse_cache[key]
  gg,a,b=self.p.xgcd(phi)
  assert a*self.p+b*phi==gg
  if gg.degree()!=0:
   say("accurate_H7_nonunit_retained",label=label,
       exactCommonWeightFactorAscending=coeff(monic(gg)),
       entireWorkingFactorStillRetained=True)
   raise Nonunit(label)
  ans=A(a/gg[0]);assert self*ans==1
  inverse_cache[key]=ans;inverse_count+=1
  return ans
 def __truediv__(self,v):
  if not self.accepts(v):return NotImplemented
  return self*A(v).inverse()
 def __rtruediv__(self,v):
  if not self.accepts(v):return NotImplemented
  return A(v)*self.inverse()
 def __pow__(self,n):
  if n<0:return self.inverse()**(-n)
  ans=A(1);a=self
  while n:
   if n&1:ans=ans*a
   n//=2
   if n:a=a*a
  return ans
 def data(self):return coeff(self.p)
 def complexity(self):
  return max((len(str(c)) for c in self.p.coeffs()),default=0)
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
 iv=b.c[-1].inverse(label+" actual whole-algebra lambda head")
 qc=[A() for _ in range(max(0,len(a.c)-len(b.c)+1))]
 while a and a.degree()>=b.degree():
  j=a.degree()-b.degree();c0=a.c[-1]*iv;qc[j]=qc[j]+c0
  ac=a.c[:]
  for i,c1 in enumerate(b.c):ac[j+i]=ac[j+i]-c0*c1
  a=U(ac)
 q=U(qc);assert q*b+a==original and a.degree()<b.degree()
 divisions+=1
 for p0 in (original,b,q,a):
  trace.update(json.dumps(p0.data(),separators=(",",":")).encode());trace.update(b"\n")
 return q,a
def euclid(a,b,label):
 a=U(a);b=U(b);j=0
 while b:
  q,r=divide(a,b,label);a,b=b,r;j+=1
  say("new_H7_original_lambda_division_returned",label=label,step=j,
      divisorDegree=a.degree(),remainderDegree=b.degree(),
      coefficientDigitBound=max(a.complexity(),b.complexity()),
      allFiniteWeightComponentsReturned=True)
 return a.normalize(label+" final whole-algebra head")
class P:
 """Finite polynomial in (lambda,T,z) with whole finite H7 weight coefficients."""
 def __init__(self,v=0):
  if isinstance(v,P):self.v=dict(v.v);return
  c=A(v);self.v={(0,0,0):c} if c else {}
 @classmethod
 def from_terms(cls,terms):
  ans=cls();ans.v={tuple(k):A(c) for k,c in terms.items() if A(c)}
  return ans
 def __bool__(self):return bool(self.v)
 def __add__(self,v):
  v=P(v);out=dict(self.v)
  for k,c in v.v.items():
   out[k]=out.get(k,A())+c
   if not out[k]:del out[k]
  return P.from_terms(out)
 __radd__=__add__
 def __neg__(self):return P.from_terms({k:-c for k,c in self.v.items()})
 def __sub__(self,v):return self+-P(v)
 def __rsub__(self,v):return P(v)+-self
 def __mul__(self,v):
  v=P(v);out={}
  for e,c in self.v.items():
   for f,d in v.v.items():
    k=tuple(i+j for i,j in zip(e,f));out[k]=out.get(k,A())+c*d
  return P.from_terms(out)
 __rmul__=__mul__
 def __truediv__(self,v):return self*A(v).inverse("original scalar weight divisor")
 def __pow__(self,n):
  assert n>=0
  ans=P(1);v=self
  while n:
   if n&1:ans=ans*v
   n//=2
   if n:v=v*v
  return ans
 def __eq__(self,v):return self.v==P(v).v
def from_lambda(v):
 v=U(v)
 return P.from_terms({(i,0,0):c for i,c in enumerate(v.c) if c})
def quadelements(p):
 slots={(0,0):0,(1,0):1,(0,1):2,(2,0):3,(1,1):4,(0,2):5}
 rows=[{} for _ in range(6)]
 for (l,t,z),c in p.v.items():
  assert (t,z) in slots
  idx=slots[(t,z)];rows[idx][l]=c
 out=[]
 for row in rows:
  out.append(U([row.get(i,A()) for i in range(max(row,default=-1)+1)]))
 return out
def det3(a):
 return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def adj3(a):
 out=[]
 for i in range(3):
  row=[]
  for j in range(3):
   rr=[k for k in range(3) if k!=j];cc=[k for k in range(3) if k!=i]
   v=a[rr[0]][cc[0]]*a[rr[1]][cc[1]]-a[rr[0]][cc[1]]*a[rr[1]][cc[0]]
   row.append(v if (i+j)%2==0 else -v)
  out.append(row)
 return out
def rowmul(row,M):
 return [sum((row[i]*M[i][j] for i in range(3)),U()) for j in range(3)]
def exactU(a,b,label):
 q,r=divide(a,b,label)
 assert not r and q*U(b)==U(a)
 return q
def gcdU(a,b,label):return euclid(a,b,label)


def run_new_input():
 v=A(vp);u=1+v;Q=1-v
 lam=P.from_terms({(1,0,0):1})
 Tr=P.from_terms({(0,1,0):1});z=P.from_terms({(0,0,1):1})
 ell=1+2*v
 assert ell==1-2*(u-1)*(u-2)/Q
 delta=1-Q;m=u-ell;V2=2*u-ell*Q;T0=V2-2*u*u
 J=2*u*(1-u)+ell*Q
 P02=(2-3*u)*V2-Q*u+2*u**3;Pf=T0*(J-Q)
 M=ell*V2-u*u;bc=M/(4*delta)
 A2=2*lam*lam-2*lam+1
 G=lam*P02+(u-1)*T0
 Pc=Q*P02*(ell+Tr)-G*T0
 ff=-Pc/Pf
 assert T0+4*u-4+Q==0
 assert T0==-Q-4*(u-1) and J-Q==-4*(u-1)**2
 assert P02==2*(u-1)*ell*Q
 assert Pf*ff+Pc==0
 aa=1-ell
 vn=J*ff-G+bc*z
 wstar=T0+4*u*ff
 nn=Q*wstar-2*vn
 ww=lam-1-Tr
 ii=((vn+aa*u*Q)**2-2*u*Q*vn+2*aa*u*u*Q*Q
     -4*aa*u*Q*Q*ff+bc*z*z+z*(4*bc*u*Q-ell*vn))
 Rbar=ii+(m/(2*delta))*z*nn
 W4=(8*bc*delta*Q*Q*ell*T0-4*ell*delta*vn*vn-ell*nn*nn
     +4*m*vn*nn+32*bc*delta*Q*ff*vn+16*bc*bc*delta*z*z
     +32*bc*bc*delta*Q*(u-1)*z-8*bc*ell*delta*z*vn+4*bc*m*z*nn)
 s0=2*ell*vn-(m/delta)*nn
 d0=-2*m*vn+ell*nn
 Obar=(32*bc*bc*aa*Q*Q*delta*(u-1)+4*bc*Q*delta*s0
       +32*bc*bc*Q*delta*vn-64*bc*bc*Q*Q*delta*ff
       +4*bc*Q*(1-u+2*ff)*d0-s0*d0-8*bc*bc*m*z*z
       -16*bc*bc*Q*z*(m*(u-1)+ell*delta)+8*bc*bc*z*nn)
 al=ell*(1-u)-m
 ber=ell*delta-m*(1-u)
 av=(2*u-1)*ell+3*m
 bur=(2*u-1)*m+3*ell*delta
 Nstar=(al*(4*delta*vn*vn+nn*nn)+4*ber*vn*nn
        +8*bc*delta*Q*vn*wstar-24*bc*delta*Q*Q*ff*wstar
        +16*aa*bc*delta*Q*Q*(u-1)*wstar+64*bc*delta*Q*Q*u*ff*ff
        -32*bc*delta*Q*u*ff*vn+16*bc*delta*Q*Q*(1+aa)*T0*ff
        +16*bc*delta*Q*(aa*Q-T0)*vn+4*bc*delta*av*z*vn
        -2*bc*bur*z*nn+16*bc*bc*delta*Q*z*(2*ff+T0-aa*Q)
        -8*u*bc*bc*delta*z*z)
 N1=Nstar-16*bc*delta*Q*Q*lam*P02*ww


 quads=[quadelements(p) for p in [Rbar,W4,Obar,N1]]
 basis=[P(1),Tr,z,Tr*Tr,Tr*z,z*z]
 for p0,row in zip([Rbar,W4,Obar,N1],quads):
  assert sum((from_lambda(c0)*v0 for c0,v0 in zip(row,basis)),P())==p0
 assert all(c0.degree()<=0 for row in quads for c0 in row[3:])
 head=[[c0.c[0] if c0.c else A() for c0 in row[3:]] for row in quads[:3]]
 assert det3(head)==0
 def e_pol(seq,arg):
  out=A()
  for c0 in reversed(seq):out=out*arg+A(fmpq(c0))
  return out
 def saved_A(data):
  num=sum((e_pol(seq,u)*(Q**i) for i,seq in enumerate(data["n"])),A())
  den=e_pol(data["d"],u)
  return num*den.inverse("saved original L coefficient denominator on working weight algebra")
 a,b,c=[U([saved_A(co) for co in series]) for series in saved["coefficientData"]]
 L=from_lambda(a)*Tr+from_lambda(b)*z+from_lambda(c)
 assert L and b
 adj=adj3(head)
 matches=[]
 for i,alpha in enumerate(adj):
  candidate=sum((alpha[j]*p0 for j,p0 in enumerate([Rbar,W4,Obar])),P())
  if candidate==L:matches.append(i)
 assert matches
 assert a.degree()<=1 and b.degree()<=1 and c.degree()<=2
 say("new_H7_same_saved_original_linear_relation_returned",
  workingWeightDegree=int(phi.degree()),lambdaDegrees=[a.degree(),b.degree(),c.degree()],
  originalAdjugateRowsMatchingSavedL=matches,
  completeOriginalRWOIdentityReturned=True,
  bZeroExcludedOnlyByPaidCoverOnWorkingComplement=True,
  retainedWeightFactorDegree=int(retained.degree()))
 def hom(row,p0,label):
  q0,qt,qz,qtt,qtz,qzz=row
  out=[b*b*q0-b*c*qz+c*c*qzz,
       b*b*qt-b*(a*qz+c*qtz)+2*a*c*qzz,
       b*b*qtt-a*b*qtz+a*a*qzz]
  poly=sum((from_lambda(cc)*(Tr**i) for i,cc in enumerate(out)),P())
  mul=from_lambda(b)*(from_lambda(qtz)*Tr+from_lambda(qz)+2*from_lambda(qzz)*z)-from_lambda(qzz)*L
  assert from_lambda(b*b)*p0-poly==L*mul
  say("new_H7_original_homogenized_quadratic",original=label,
   lambdaDegrees=[cc.degree() for cc in out],allOriginalPolynomialCoefficientsReturned=True,
   noFormalLambdaPolynomialInverseUsed=True)
  return out
 mat=[hom(quads[i],p0,label) for i,p0,label in
      [(0,Rbar,"R"),(1,W4,"W"),(3,N1,"N1")]]
 lamunit=U([0,1])
 bmonic=b.normalize("saved b coefficient actual whole-algebra lambda head")
 def paid_strip(p0,label):
  p0=U(p0);removed_lambda=0;removed_b=0
  while p0 and p0.degree()>0 and not p0.c[0]:
   q0=U(p0.c[1:]);assert q0*lamunit==p0
   p0=q0;removed_lambda+=1
  if bmonic.degree()>0:
   while p0 and p0.degree()>=bmonic.degree():
    q0,r0=divide(p0,bmonic,label+" paid original b")
    if r0:break
    assert q0*bmonic==p0;p0=q0;removed_b+=1
  say("new_H7_only_actual_original_value_units_removed",label=label,
   lambdaPower=removed_lambda,originalBPower=removed_b,remainingDegree=p0.degree(),
   wholeBZeroWeightsRemainInExplicitRetainedFactor=True)
  return p0
 current=None
 def take(p0,label):
  nonlocal current
  p0=paid_strip(p0,label)
  if not p0:
   say("new_H7_constraint_identically_zero",label=label,noExtraExclusionClaim=True)
   return
  if current is None:current=p0.normalize(label+" initial head")
  else:current=euclid(current,p0,label)
  current=paid_strip(current,label+" common constraint").normalize(label+" common head")
  say("new_H7_complete_original_common_lambda_constraint",label=label,
   lambdaDegree=current.degree(),weightDegree=int(phi.degree()),
   workingWeightComplementExcluded=(current.degree()==0))
 def fixed_res2(p0,p1,label):
  cc,bb,aa=p0;ff,ee,dd=p1
  ans=(aa*ff-cc*dd)**2-(aa*ee-bb*dd)*(bb*ff-cc*ee)
  # The fixed 4-by-4 Sylvester identity is checked on all finite-algebra coefficients.
  matrix=[[aa,bb,cc,U()],[U(),aa,bb,cc],
          [dd,ee,ff,U()],[U(),dd,ee,ff]]
  import itertools
  determinant=U()
  for perm in itertools.permutations(range(4)):
   sign=(-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
   product=U(sign)
   for i,j in enumerate(perm):product=product*matrix[i][j]
   determinant=determinant+product
  assert determinant==ans
  say("new_H7_fixed_original_T_quadratic_resultant",label=label,
   fixedOriginalTDegrees=[2,2],fixedSylvesterOrder=4,lambdaDegree=ans.degree(),
   completeUniversalPolynomialDeterminantReturned=True,
   allTLeadingZeroLambdaFibersRetained=True)
  return ans
 for i,j in [(0,1),(0,2),(1,2)]:
  if current is not None and current.degree()==0:break
  take(fixed_res2(mat[i],mat[j],str(i)+"_"+str(j)),
       "original pair "+str(i)+"_"+str(j))
 if current is None or current.degree()>0:
  oldc=read("2026-11-27-unit211-Phi-zero-main-head-zero-C71-29-exact-input-8542.json",
   "9aba3e9a6bb845d4067b530d724d3f407a4687538dbe569066b7adfdb7e993d7")
  rec=oldc["polynomial"];rawc=zlib.decompress(base64.b64decode(rec["data"]))
  assert len(rawc)==rec["uncompressedBytes"] and hashlib.sha256(rawc).hexdigest()==rec["payloadSha256"]
  cob=json.loads(rawc);assert cob["variables"]==["v","lam"]
  vpowers=[A(1)]
  for i in range(71):vpowers.append(vpowers[-1]*v)
  cc=[A() for _ in range(30)]
  for i,j,coef0 in cob["terms"]:cc[int(j)]=cc[int(j)]+A(fmpq(coef0))*vpowers[int(i)]
  take(U(cc),"saved global original C71 restricted to full H7 weights")
 if current is None or current.degree()>0:
  # This is a NEW constant-weight original D target, not the frozen QQ(u) gate.
  Drow=[U([1,-2,2])*ell,U(),U(-1)]
  dt=det3(mat)
  if dt:
   ad=adj3(mat);nums=rowmul(Drow,ad)
   assert rowmul(nums,mat)==[dt*w0 for w0 in Drow]
   gam=dt
   for i,p0 in enumerate(nums):
    gam=euclid(gam,p0,"new finite-weight original D common factor "+str(i))
   den=exactU(dt,gam,"new finite-weight D cancelled denominator")
   mults=[exactU(p0,gam,"new finite-weight D cancelled numerator "+str(i)) for i,p0 in enumerate(nums)]
   assert rowmul(mults,mat)==[den*w0 for w0 in Drow]
   say("new_H7_complete_same_original_D_target",necessaryLambdaDegree=den.degree(),
    cancelledCommonDegree=gam.degree(),completeThreeFullCoefficientProductsReturned=True,
    identity="den(lambda)*D is a polynomial combination of the three homogenized ORIGINAL quadratics",
    physicalDNotInverted=True,noGenericWeightDenominator=True)
   take(den,"same original finite-weight D necessary polynomial")
  else:
   say("accurate_H7_three_original_rows_det_zero",
       noDTargetReturned=True,allOriginalWeightFibersRetained=True)
 closed=current is not None and current.degree()==0
 say("complete_new_H7_original_finite_weight_attempt",
  workingWeightDegree=int(phi.degree()),retainedBZeroWeightDegree=int(retained.degree()),
  originalWorkingWeightComplementExcluded=closed,
  remainingOriginalLambdaDegree=(current.degree() if current is not None else None),
  wholeH7Excluded=closed and retained.degree()==0,
  strictH7DifferentWeightBound=(int(retained.degree()) if closed else int(h7.degree())),
  noP6P9UsedOnH7=True,noOldParameterEuclidOrResultantReplayed=True,
  allConstantWeightAlgebraEmbeddingsRetained=True,ordinaryISPClaim=False)
 checkpoint("new_H7_original_finite_weight_and_lambda_constraint",
  dict(variableOrder=["v","lambda"],workingWeightModulusAscending=coeff(phi),
  retainedWeightFactorAscending=coeff(retained),
  originalLinearRelation=[a.data(),b.data(),c.data()],
  currentNecessaryLambdaPolynomial=(current.data() if current is not None else None),
  originalWorkingWeightComplementExcluded=closed))
 return closed

try:
 closed=run_new_input()
except Nonunit as exc:
 say("accurate_new_H7_finite_algebra_nonunit_stop",reason=str(exc),
  wholeWorkingWeightFactorStillRetained=True,wholeH7Excluded=False,ordinaryISPClaim=False)
say("new_H7_original_finite_weight_source_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 wholeFiniteAlgebraInverseProducts=inverse_count,
 wholeWeightReductionProducts=reduction_count,
 originalLambdaDivisionProducts=divisions,
 originalDivisionTraceSHA256=trace.hexdigest(),
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,ordinaryISPClaim=False)
signal.alarm(0)
