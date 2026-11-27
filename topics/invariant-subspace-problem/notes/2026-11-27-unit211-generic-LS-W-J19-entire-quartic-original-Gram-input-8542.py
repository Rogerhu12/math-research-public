#!/usr/bin/env python3
"""New W/J19 entire monic quartic e-curve: original Gram and 48x35 input.
Every rational-k norm-zero fiber is retained; no existing C9 input is rerun.
This first construction does not assert a rank or a unit certificate.
180 seconds / 4 GiB, self-contained source, no large cache output.
"""
import json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq_poly,fmpq
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.perf_counter()
P=lambda v=():fmpq_poly([fmpq(x) for x in v])
zero=P();one=P([1]);w=P([0,1])
def exact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 return q
class R:
 def __init__(self,n=0,d=None):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  if not isinstance(n,fmpq_poly):n=P([n])
  if d is None:d=one
  elif not isinstance(d,fmpq_poly):d=P([d])
  assert d
  if not n:self.n=zero;self.d=one;return
  g=n.gcd(d);n=exact(n,g);d=exact(d,g);lc=d[d.degree()];self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,v):
  v=R(v);g=self.d.gcd(v.d);a=exact(self.d,g);b=exact(v.d,g)
  return R(self.n*b+v.n*a,a*v.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d)
 def __sub__(self,v):return self+-R(v)
 def __rsub__(self,v):return R(v)+-self
 def __mul__(self,v):
  v=R(v)
  if not self or not v:return R()
  g=self.n.gcd(v.d);h=v.n.gcd(self.d)
  return R(exact(self.n,g)*exact(v.n,h),exact(self.d,h)*exact(v.d,g))
 __rmul__=__mul__
 def __truediv__(self,v):v=R(v);assert v;return self*R(v.d,v.n)
 def __rtruediv__(self,v):return R(v)/self
 def __pow__(self,n):return R(self.d**(-n),self.n**(-n)) if n<0 else R(self.n**n,self.d**n)
 def __eq__(self,v):v=R(v);return self.n*v.d==v.n*self.d
 def json(self):return dict(n=[str(c) for c in self.n.coeffs()],d=[str(c) for c in self.d.coeffs()])

# J19 is monic in e after the original paid 16*k^3 scale.
F=[-w**5-10*w**4-40*w**3-104*w*w-160*w-128,
   -2*w**5-14*w**4-12*w**3-128,
   -w**5-8*w**4+24*w**3+64*w*w+192*w,
   -8*w**4-16*w**3-96*w*w,16*w**3]
assert F[4]==16*w**3
def detP(mat):
 n=len(mat)
 if n==0:return one
 if n==1:return mat[0][0]
 out=zero
 for j in range(n):out+=((-1)**j)*mat[0][j]*detP([[c for h,c in enumerate(row) if h!=j] for row in mat[1:]])
 return out
def coeffmod1009(cc):
 parts=str(cc).split('/');num=int(parts[0]);den=int(parts[1]) if len(parts)>1 else 1
 return num%1009*pow(den%1009,-1,1009)%1009 if den%1009 else None
def pprofile(pp):
 bb=json.dumps([str(c) for c in pp.coeffs()],separators=(',',':')).encode()
 out=dict(degree=int(pp.degree()),bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest(),reduction1009=[coeffmod1009(c) for c in pp.coeffs()])
 if len(bb)<=8192:out['coefficients']=[str(c) for c in pp.coeffs()]
 return out
def say(**r):r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
inverted_norms=[];inverse_cache={};exception_cover=one
def add_exception(pp):
 global exception_cover
 if not pp or pp.degree()<=0:return
 sf=exact(pp,pp.gcd(pp.derivative()));sf=sf/sf[sf.degree()]
 exception_cover*=exact(sf,exception_cover.gcd(sf))
class GenericNonunit(Exception):pass
class A:
 def __init__(self,v=0,den=None):
  if isinstance(v,A):self.n=v.n[:];self.d=v.d;return
  if isinstance(v,R):nums=[v.n];den=v.d
  elif isinstance(v,(list,tuple)):nums=[p if isinstance(p,fmpq_poly) else P([p]) for p in v]
  else:nums=[v if isinstance(v,fmpq_poly) else P([v])]
  den=one if den is None else den
  assert den and len(nums)<=4
  nums=nums+[zero]*(4-len(nums))
  if not any(nums):self.n=[zero]*4;self.d=one;return
  gg=den
  for p0 in nums:gg=gg.gcd(p0)
  nums=[exact(p0,gg) for p0 in nums];den=exact(den,gg);lc=den[den.degree()]
  self.n=[p0/lc for p0 in nums];self.d=den/lc
 def __bool__(self):return any(self.n)
 def __neg__(self):return A([-p0 for p0 in self.n],self.d)
 def __add__(self,v):
  v=A(v);gg=self.d.gcd(v.d);aa=exact(self.d,gg);bb=exact(v.d,gg)
  return A([self.n[j]*bb+v.n[j]*aa for j in range(4)],aa*v.d)
 __radd__=__add__
 def __sub__(self,v):return self+-A(v)
 def __rsub__(self,v):return A(v)+-self
 def __mul__(self,v):
  v=A(v)
  if not self or not v:return A()
  cc=[zero]*7
  for i in range(4):
   for j in range(4):cc[i+j]+=self.n[i]*v.n[j]
  den=self.d*v.d
  for j in range(6,3,-1):
   lead=cc[j]
   if not lead:continue
   cc=[p0*F[4] for p0 in cc];den*=F[4]
   for h in range(5):cc[h+j-4]-=lead*F[h]
   assert not cc[j]
  assert not any(cc[4:])
  return A(cc[:4],den)
 __rmul__=__mul__
 def __eq__(self,v):
  v=A(v);return all(self.n[j]*v.d==v.n[j]*self.d for j in range(4))
 def __pow__(self,n):
  if n<0:return self.inv()**(-n)
  out=A(1);aa=self
  while n:
   if n&1:out=out*aa
   aa=aa*aa;n//=2
  return out
 def json(self):return dict(n=[[str(c) for c in p0.coeffs()] for p0 in self.n],d=[str(c) for c in self.d.coeffs()])
 def inv(self):
  if not self:raise GenericNonunit('zero element in the whole J19 algebra')
  key=json.dumps(self.json(),separators=(',',':'))
  if key in inverse_cache:return A(inverse_cache[key])
  basis=[A([0]*j+[1]) for j in range(4)]
  cols=[self*v for v in basis];den=one
  for col in cols:den*=exact(col.d,den.gcd(col.d))
  mat=[[cols[j].n[i]*exact(den,cols[j].d) for j in range(4)] for i in range(4)]
  determinant=detP(mat)
  if not determinant:
   say(stage='new_J19_actual_generic_nonunit_detected',elementSHA256=hashlib.sha256(key.encode()).hexdigest(),wholeFourSheetAlgebraRetained=True,requiresExactGenericFactorSplit=True,claimExcluded=False)
   raise GenericNonunit('regular multiplication determinant is zero')
  cof=[]
  for j in range(4):
   co=((-1)**j)*detP([[mat[ii][jj] for jj in range(4) if jj!=j] for ii in range(1,4)])
   cof.append(den*co)
  out=A(cof,determinant)
  assert self*out==1
  for i in range(4):
   assert sum((mat[i][j]*out.n[j] for j in range(4)),zero)==(den*out.d if i==0 else zero)
  norm=R(determinant,den**4)
  add_exception(out.d);add_exception(self.d);add_exception(norm.n);add_exception(norm.d)
  inverted_norms.append(dict(index=len(inverted_norms),inputSHA256=hashlib.sha256(key.encode()).hexdigest(),normNumerator=pprofile(norm.n),normDenominator=pprofile(norm.d),outputDenominator=pprofile(out.d),allFourInverseProductsActuallyOne=True,allScalarNormZeroFibersRetained=True))
  inverse_cache[key]=out
  return A(out)
 def __truediv__(self,v):return self*A(v).inv()
 def __rtruediv__(self,v):return A(v)*self.inv()
k=A(w);e=A([0,1]);u=e+1;Q=e*k;V=(e+1)*k+2
assert sum((A(F[j])*e**j for j in range(5)),A())==0
ell=u*((k+2)**2-2*e*k)/(k*V);d=1-Q;bc=(ell*ell-(u-ell)**2/d)/4
V2=2*u-ell*Q;T0=V2-2*u*u;P02=(2-3*u)*V2-Q*u+2*u**3;J=2*u*(1-u)+ell*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q);M=ell*V2-u*u
assert M==4*bc*d and Phi*(J-2*u*Q)-Pf==0
J19=16*e**4*k**3+e**3*(-8*k**4-16*k**3-96*k*k)+e*e*(-k**5-8*k**4+24*k**3+64*k*k+192*k)+e*(-2*k**5-14*k**4-12*k**3-128)-k**5-10*k**4-40*k**3-104*k*k-160*k-128
assert not J19
say(stage='new_J19_entire_quartic_weight_algebra',relationLeading='16*k^3, original paid unit',basis=['1','e','e^2','e^3'],allOriginalWeightAndWProductsActuallyVerified=True,noIrreducibilityAssumption=True,allNormZeroKFibersRetained=True,inverseCount=len(inverted_norms),claimExcluded=False)
class Mpoly:
 def __init__(self,v=0):
  if isinstance(v,Mpoly):self.terms=v.terms.copy();return
  c=A(v);self.terms={(0,0,0):c} if c else {}
 @staticmethod
 def variable(j):
  p=Mpoly();m=[0,0,0];m[j]=1;p.terms[tuple(m)]=A(1);return p
 @staticmethod
 def from_terms(ts):
  p=Mpoly();p.terms={m:c for m,c in ts if c};return p
 def __bool__(self):return bool(self.terms)
 def __add__(self,v):
  v=Mpoly(v);p=Mpoly(self)
  for m,c in v.terms.items():
   z=p.terms.get(m,A())+c
   if z:p.terms[m]=z
   elif m in p.terms:del p.terms[m]
  return p
 __radd__=__add__
 def __neg__(self):return Mpoly.from_terms((m,-c) for m,c in self.terms.items())
 def __sub__(self,v):return self+-Mpoly(v)
 def __rsub__(self,v):return Mpoly(v)+-self
 def __mul__(self,v):
  v=Mpoly(v);p=Mpoly()
  for ma,ca in self.terms.items():
   for mb,cb in v.terms.items():
    m=tuple(ma[j]+mb[j] for j in range(3));z=p.terms.get(m,A())+ca*cb
    if z:p.terms[m]=z
    elif m in p.terms:del p.terms[m]
  return p
 __rmul__=__mul__
 def scale(self,c):
  c=A(c);return Mpoly.from_terms((m,v*c) for m,v in self.terms.items())
 def __pow__(self,n):
  p=Mpoly(1)
  for i in range(n):p=p*self
  return p
 def __eq__(self,v):return not(self-Mpoly(v))
 def degree(self):return max((sum(m) for m in self.terms),default=-1)
 def json(self):return [[list(m),c.json()] for m,c in sorted(self.terms.items())]
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=Mpoly(a);self.b=Mpoly(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,v):v=E(v);return E(self.a+v.a,self.b+v.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,v):return self+-E(v)
 def __rsub__(self,v):return E(v)+-self
 def __mul__(self,v):v=E(v);return E(self.a*v.a+(self.b*v.b).scale(d),self.a*v.b+self.b*v.a)
 __rmul__=__mul__
 def __pow__(self,n):
  out=E(1)
  for i in range(n):out=out*self
  return out
 def conj(self):return E(self.a,-self.b)
 def __eq__(self,v):v=E(v);return self.a==v.a and self.b==v.b
b=E(Mpoly(ell/2),Mpoly((u-ell)/(2*d)));c=b.conj();p=E(1,1);q=p.conj();a=1-ell
assert b*c==E(Mpoly(bc)) and b*p+c*q==E(Mpoly(u))
x,y,t=[Mpoly.variable(j) for j in range(3)];X=E(x,y);Y=X.conj()
f=(x.scale(u)+y.scale(u-ell*Q)-Mpoly(T0/2)).scale(1/(2*u))
W2=x.scale(V2)+y.scale(2*u-u*Q-ell*Q)
lam=(W2-Mpoly(u*T0)-f.scale(V2+2*u*u)+t.scale(bc*Q)).scale(1/P02)
T=((lam.scale(P02)-Mpoly((1-u)*T0)).scale(T0)-f.scale(Pf)-t.scale(Phi*bc*Q)).scale(1/(Q*P02))-Mpoly(ell)
rg=X-p*E(Mpoly(a))-c*E(t);sg=Y-q*E(Mpoly(a))-b*E(t)
ag=E(f.scale(2))-2*b*X-2*c*Y+E(t.scale(2*bc))
zz=E();oo=E(1);gram=[[zz,zz,p,q],[zz,ag,rg,sg],[p,rg,zz,E(t)],[q,sg,E(t),zz]];unitvec=[oo,zz,oo,oo]
def va(v,z):return [a+b for a,b in zip(v,z)]
def vs(v,z):return [v*a for a in z]
def vm(v,z):return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return E(Mpoly(a))*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tau(vm(row,v)) for row in gram]
dv=DK(unitvec);F2=tau(dv);Kd=DK(dv)
assert F2==E(f.scale(2))
def mean(j):
 first=2*tau(vm(gram[0],gram[1])) if j==1 else tau(vm(gram[j],gram[j]))
 return first-2*Kd[j]-2*vm(dv,dv)[j]+2*F2*dv[j]
assert not mean(0)
def N4(v):return 2*tau(vm(dv,vm(v,v)))-F2*tau(vm(v,v))-4*tau(v)*tau(vm(dv,v))+2*F2*tau(v)**2+tau(vm(v,DK(v)))
def P2(v):
 cv=va(v,vs(-tau(v),unitvec));return tau(vm(vm(cv,cv),cv))
vc=va(gram[0],vs(-tau(gram[0]),unitvec));zc=va(gram[1],vs(-tau(gram[1]),unitvec));Pj=3*tau(vm(vm(vc,vc),zc))
assert N4(gram[0])==E(lam.scale(2*P02)) and Pj==E((lam-1-T).scale(3*P02)) and P2(gram[0])==E(Mpoly(P02))
N1=N4(va(gram[0],gram[1]))-N4(gram[0])-N4(gram[1])-E(lam.scale(A(fmpq(4,3))))*Pj
A2=2*lam**2-2*lam+1;B3=4*lam**3-6*lam**2+3*lam-1
NS=b*N4(gram[2])+c*N4(gram[3])-E((lam*(Mpoly(ell)+2*T+A2)).scale(2*P02))
PS=b*P2(gram[2])+c*P2(gram[3])-E((Mpoly(ell)+3*T+3*A2+B3).scale(P02))
E1,EB,EC=mean(1),mean(2),mean(3)
assert not E1.b and EB.conj()==EC and not N1.b and not NS.b and not PS.b
original=[E1.a,EB.a,EB.b,N1.a,NS.a,PS.a];names=['E1','EBe','EBo','N1','NS','PS']

def aprofile(v):return dict(numeratorKDegrees=[int(p0.degree()) for p0 in v.n],denominatorKDegree=int(v.d.degree()))
say(stage='new_J19_original_six_Gram_rows',originalE0N0P1AndRawN4P2DefinitionsActuallyRebuilt=True,bothWeightedNSPSDefinitionsFromSameOriginalGram=True,originalRows=[dict(name=name,totalDegree=pp.degree(),monomials=len(pp.terms),maxNumeratorKDegree=max(max(p0.degree() for p0 in cf.n) for cf in pp.terms.values()),maxDenominatorKDegree=max(cf.d.degree() for cf in pp.terms.values())) for name,pp in zip(names,original)],allScalarNormZeroFibersRetained=True,claimExcluded=False)
# Independent original binary (x,t) head identities, not inferred from a sample.
def binaryhead(pp):
 return Mpoly.from_terms((mm,cf) for mm,cf in pp.terms.items() if sum(mm)==2 and mm[1]==0)
lamh=x.scale(T0/(2*P02))+t.scale(bc*Q/P02)
diffh=x.scale(ell*T0/P02)+t.scale(2*bc*(Q+2*(u-1))/P02)
H1=(x*x).scale(2*(1-2*ell))+(x*t).scale(4*bc)
HB=(t*t-2*x*t).scale(ell/2)
HN=H1.scale(u)-HB.scale(4*u*bc/ell)-(lamh*diffh).scale(4*P02)
assert binaryhead(original[0])==H1
assert binaryhead(original[1])==HB
assert binaryhead(original[3])==HN
def detA(mat):
 n=len(mat)
 if n==0:return A(1)
 if n==1:return mat[0][0]
 return sum((((-1)**j)*mat[0][j]*detA([[cf for h,cf in enumerate(row) if h!=j] for row in mat[1:]]) for j in range(n)),A())
binarymons=[(2,0,0),(1,0,1),(0,0,2)]
binarymat=[[pp.terms.get(mm,A()) for mm in binarymons] for pp in [H1,HB,HN]]
assert not detA(binarymat)
say(stage='new_J19_original_binary_heads_exactly_returned',headE1='2(1-2ell)x^2+4bc*x*t',headEBe='ell*(t^2-2*x*t)/2',headN1='u*H1-4u*bc*HB/ell-4P02*lambda_h*(lambda-T)_h',fullOriginalCoefficientIdentitiesVerified=True,binaryHeadDeterminantExactlyZeroOnWholeQuartic=True,physicalHighestDirectionNotClaimedFiniteSolution=True,claimExcluded=False)
# Original 48 x 35 Macaulay rows: identities and only a small certificate digest.
mons=sorted(((aa,bb,cc) for aa in range(5) for bb in range(5-aa) for cc in range(5-aa-bb)),key=lambda mm:(sum(mm),mm))
assert len(mons)==35 and mons[0]==(0,0,0)
def shifted(pp,mm):return Mpoly.from_terms((tuple(m[j]+mm[j] for j in range(3)),cf) for m,cf in pp.terms.items())
mac=[];maclabels=[]
for j,pp in enumerate(original):
 bound=2 if j<4 else 3;assert pp.degree()<=bound
 md=4-bound
 multipliers=[mm for mm in mons if sum(mm)<=md]
 for mm in multipliers:
  rr=shifted(pp,mm)
  row=[rr.terms.get(nn,A()) for nn in mons]
  assert Mpoly.from_terms((nn,cf) for nn,cf in zip(mons,row))==rr
  mac.append(row);maclabels.append(dict(original=j,multiplier=list(mm)))
assert len(mac)==48
enc=json.dumps(dict(columns=mons,labels=maclabels,rows=[[cf.json() for cf in row] for row in mac]),separators=(',',':')).encode()
# No rank/emptiness gate is run here: this is the new exact one-parameter input.
unit_k=exception_cover
while unit_k and not unit_k[0]:unit_k=exact(unit_k,w)
assert unit_k
sf=exact(unit_k,unit_k.gcd(unit_k.derivative()));sf=sf/sf[sf.degree()]
# Actual inverse certificates are valid off this complete scalar exceptional cover.
signal.alarm(0)
say(stage='new_J19_complete_original_quartic_Gram_input',sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),baseParameter='k',wholeQuarticEConstraint=True,allOriginalGramRowsReturned=True,all48MacaulayRowsActuallyMultipliedBack=True,monomialColumns=35,matrixCertificateBytes=len(enc),matrixCertificateSHA256=hashlib.sha256(enc).hexdigest(),genericScalarInverseCount=len(inverted_norms),scalarNormZeroCover=pprofile(sf),onlyOriginalKZeroRemoved=True,completeScalarNormZeroFibersStillRequireOriginalReturn=True,inverseReceipts=inverted_norms,rankNotComputed=True,noParameterCofactorYet=True,noWholeJ19ExclusionClaim=True,claimExcluded=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
