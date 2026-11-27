#!/usr/bin/env python3
"""NEW whole H1 constant-size Dixon unit/D target over QQ(u)[Q]/g4.
Use saved L and saved lambda0,A0,C0, then a polynomial (x,mu) chart:
T=-(mu*x+C0)/A0, z=(x-a1*T-c1-2*c2*lambda0-c2*mu)/b1.
No mu inverse. All A0/b1/base denominator zero fibers remain explicit.
Three complete original means/N1 become biquadratic. New Dixon8 columns
are constructed by 84 exact integer Cauchy-Binet minors; try 1/lambda.
If necessary add the three original polynomials in 11 coordinates and
try the same physical D. Clear only final coefficient denominators,
while retaining every original chart/source pole. No old lambda Euclid,
resultant/cofactor or b=0 F6 computation is replayed. 120s /1GiB.
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
collect_source_denominators=True
def record_denominator(p):
 global cover
 if not collect_source_denominators:return
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
class P:
 """Finite polynomial in (x,mu,unused) with the whole Q-quartic coefficients."""
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

def read(name,sha):
 raw=Path(__file__).with_name(name).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==sha,name
 return json.loads(raw)
def checkpoint(label,obj):
 # Root README rules 8/15: no encoded/split polynomial payload through
 # tools or into the repository. Keep only its deterministic definition
 # and small byte/SHA receipt. The exact parameter is source-defined.
 raw=json.dumps(obj,separators=(",",":")).encode()
 say("new_H1_Dixon_parameter_definition_receipt",label=label,
  rawBytes=len(raw),rawSHA256=hashlib.sha256(raw).hexdigest(),
  reconstructionDefinition="the exact final sf in this self-contained original source",
  polynomialPayloadTransmitted=False,encodedOrSplitPayloadCreated=False)

saved=read("2026-11-27-unit211-Phi-zero-whole-first-head-original-linear-relation-exact-input-8542.json",
 "c6c0b8973ea18a3fd320921238a7e331e460ca26ed1d96ec5f4e6276fd45ff44")
part=read("2026-11-27-unit211-Phi-zero-H1-b-zero-lambda-linear-exact-part-01-8542.json",
 "1bc01ff121193bf3e50edd7545e0d95ef5a6f6ed1ded3e2b5973d4e6d4276393")
raw=zlib.decompress(base64.b64decode(part["dataChunk"]))
assert len(raw)==18841 and hashlib.sha256(raw).hexdigest()=="302d25083c5066b73c338c4c1d5565d3b7d5292ebc0881019afe49558c89070f"
values=json.loads(raw)
def loadA(ob):
 assert len(ob["n"])==4
 ans=A([pol(v) for v in ob["n"]],pol(ob["d"]))
 record_denominator(ans.d)
 return ans
a,b,c=[[loadA(co) for co in row] for row in saved["coefficientData"]]
assert len(a)==len(b)==2 and len(c)==3
lambda0=loadA(values["lambdaValue"])
A0=loadA(values["TLeading"]);C0=loadA(values["constant"])
assert b[0]+b[1]*lambda0==0
assert a[0]+a[1]*lambda0==A0
assert c[0]+c[1]*lambda0+c[2]*lambda0**2==C0
u=A(up);Q=A([0,1])
x=P.from_terms({(1,0,0):1});mu=P.from_terms({(0,1,0):1})
lam=lambda0+mu
Tr=-(mu*x+C0)/A0
z=(x-a[1]*Tr-c[1]-2*c[2]*lambda0-c[2]*mu)/b[1]
assert (a[0]+a[1]*lam)*Tr+(b[0]+b[1]*lam)*z+c[0]+c[1]*lam+c[2]*lam**2==0
assert x==a[1]*Tr+b[1]*z+c[1]+2*c[2]*lambda0+c[2]*mu
say("new_H1_same_original_L_polynomial_two_coordinate_chart",
 wholeWeightAlgebraRank=4,
 originalLambda0A0C0RelationsReturned=True,
 entirePolynomialLIdentityReturned=True,
 forwardMapAllLPointsReturned=True,noMuInverseUsed=True,
 originalA0B1ZeroFibersRetainedInBaseCover=True,
 currentBasePoleCoverDegree=int(cover.degree()))
ell=1-2*(u-1)*(u-2)/Q
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


polys=[Rbar,W4,N1]
physicalD=ell*A2-Tr*Tr
monomial9=[(i,j,0) for i in range(3) for j in range(3)]
for i,p0 in enumerate(polys):
 assert all(e[2]==0 and 0<=e[0]<=2 and 0<=e[1]<=2 for e in p0.v)
 say("new_H1_original_biquadratic",original=["R","W","N1"][i],
  degrees=[max((e[j] for e in p0.v),default=-1) for j in [0,1]],
  terms=len(p0.v),maxCoefficientUDegree=max((co.complexity() for co in p0.v.values()),default=0),
  sameOriginalLPolynomialChart=True)
for p0 in polys+[physicalD,lam]:
 for co in p0.v.values():record_denominator(co.d)
B=[[p0.v.get(e,A()) for e in monomial9] for p0 in polys]
# Exact integer divided-monomial determinant; no parameter inversion here.
def giadd(a0,b0,sign=1):
 out=dict(a0)
 for e,c0 in b0.items():
  out[e]=out.get(e,0)+sign*c0
  if not out[e]:del out[e]
 return out
def gimul(a0,b0):
 out={}
 for e,c0 in a0.items():
  for f,c1 in b0.items():
   k=tuple(x0+y0 for x0,y0 in zip(e,f));out[k]=out.get(k,0)+c0*c1
 return {k:c0 for k,c0 in out.items() if c0}
geom=[]
for i,j,_ in monomial9:
 r1={(i-1-k,j,k,0):1 for k in range(i)}
 r2={(0,j-1-k,i,k):1 for k in range(j)}
 r3={(0,0,i,j):1}
 geom.append((r1,r2,r3))
def determinant3(mm):
 return mm[0][0]*(mm[1][1]*mm[2][2]-mm[1][2]*mm[2][1])-mm[0][1]*(mm[1][0]*mm[2][2]-mm[1][2]*mm[2][0])+mm[0][2]*(mm[1][0]*mm[2][1]-mm[1][1]*mm[2][0])
perms=[(0,1,2,1),(0,2,1,-1),(1,0,2,-1),
       (1,2,0,1),(2,0,1,1),(2,1,0,-1)]
row8=[(i,j,0) for i in range(2) for j in range(4)]
col8=[(i,j) for i in range(4) for j in range(2)]
rindex={e:i for i,e in enumerate(row8)};cindex={e:i for i,e in enumerate(col8)}
Dmatrix=[[A() for _ in range(8)] for _ in range(8)]
geometric_count=0;geometric_terms=0
for i in range(9):
 for j in range(i+1,9):
  for k in range(j+1,9):
   js=[i,j,k];gd={}
   for a0,b0,c0,sgn in perms:
    term=gimul(gimul(geom[js[a0]][0],geom[js[b0]][1]),geom[js[c0]][2])
    gd=giadd(gd,term,sgn)
   if not gd:continue
   geometric_count+=1;geometric_terms+=len(gd)
   minor=determinant3([[B[r][s] for s in js] for r in range(3)])
   for (xx,yy,ss,tt),integer in gd.items():
    assert (xx,yy,0) in rindex and (ss,tt) in cindex
    r0,c0=rindex[(xx,yy,0)],cindex[(ss,tt)]
    Dmatrix[r0][c0]=Dmatrix[r0][c0]+integer*minor
assert geometric_count==78 and geometric_terms==144
for row in Dmatrix:
 for co in row:record_denominator(co.d)
source_cover=cover
say("new_H1_complete_original_Dixon_eight_columns",
 originalPolynomials=["R","W","N1"],integerCauchyBinetTriples=84,
 nonzeroIntegerTriples=78,integerGeometricTerms=144,
 rowMonomials=[list(e[:2]) for e in row8],
 independentColumnMonomials=[list(e) for e in col8],
 actualCoefficientUDegree=max(co.complexity() for row in Dmatrix for co in row),
 entireDividedDifferenceDeterminantCoefficientIdentity=True,
 originalPointNecessity="v(x,mu)*Dixon=0 from the full original three equations",
 noClaimThatBareNecessaryColumnsAreAlreadyExpandedOriginalIdealRows=True,
 originalSourcePoleCoverDegree=int(source_cover.degree()))
# All Gaussian rational parameter poles may cancel. Only final coefficient
# poles will be added to source_cover; the original chart poles always stay.
collect_source_denominators=False
columns=[[Dmatrix[i][j] for i in range(8)] for j in range(8)]
basis=[]
def tag_scale(tag,s):
 return {i:c0*s for i,c0 in tag.items() if c0*s}
def tag_sub(tag,other,s):
 out=dict(tag)
 for i,c0 in other.items():
  out[i]=out.get(i,A())-s*c0
  if not out[i]:del out[i]
 return out
def add_column(j):
 vec=list(columns[j]);tag={j:A(1)}
 for rr in basis:
  co=vec[rr["pivot"]]
  if not co:continue
  vec=[x0-co*y0 for x0,y0 in zip(vec,rr["vector"])]
  tag=tag_sub(tag,rr["tag"],co)
 pivot=next((i for i,c0 in enumerate(vec) if c0),None)
 if pivot is None:return
 iv=vec[pivot].inverse("new original Dixon column actual pivot")
 vec=[co*iv for co in vec];tag=tag_scale(tag,iv)
 assert vec[pivot]==1
 basis.append(dict(pivot=pivot,vector=vec,tag=tag))
 say("new_H1_Dixon_column_pivot",column=j,actualRank=len(basis),
  ambientDimension=len(vec),maxUDegree=max(co.complexity() for co in vec),
  noGenericParameterPivotDeclaredGlobalUnit=True)
def try_target(target,label,monomials):
 assert all(e in monomials for e in target.v)
 target_vec=[target.v.get(e,A()) for e in monomials]
 vec=target_vec[:];tag={}
 for rr in basis:
  co=vec[rr["pivot"]]
  if not co:continue
  vec=[x0-co*y0 for x0,y0 in zip(vec,rr["vector"])]
  tag=tag_sub(tag,rr["tag"],-co)
 if any(vec):
  say("accurate_new_H1_Dixon_target_not_yet_returned",target=label,
   ambientDimension=len(vec),actualRank=len(basis),
   nonzeroRemainderCoordinates=[i for i,c0 in enumerate(vec) if c0])
  return None
 coeffs=[tag.get(j,A()) for j in range(len(columns))]
 assert all(sum((coeffs[j]*columns[j][i] for j in range(len(columns))),A())==target_vec[i]
 say("new_H1_Dixon_full_original_target_returned",target=label,
  ambientDimension=len(vec),originalNecessaryColumns=len(columns),
  actualRank=len(basis),allFullWeightCoordinatesMultipliedBack=True)
 return dict(label=label,coefficients=coeffs,target=target_vec)
success=None
try:
 for j in range(8):add_column(j)
 for target,label in [(P(1),"constant_one"),(lam,"original_lambda")]:
  success=try_target(target,label,row8)
  if success is not None:break
 if success is None:
  # A new 11-coordinate source combines the same eight Dixon columns
  # and the three complete ORIGINAL biquadratics. Physical D fits here.
  row11=row8+[(2,j,0) for j in range(3)]
  for col in columns:col.extend([A(),A(),A()])
  for rr in basis:rr["vector"].extend([A(),A(),A()])
  for p0 in polys:columns.append([p0.v.get(e,A()) for e in row11])
  for j in range(8,11):add_column(j)
  for target,label in [(P(1),"constant_one"),(lam,"original_lambda"),(physicalD,"same_physical_D")]:
   success=try_target(target,label,row11)
   if success is not None:break
except Nonunit as exc:
 say("accurate_new_H1_Dixon_whole_algebra_nonunit_stop",reason=str(exc),
  allOriginalH1ComponentsRetained=True,noFiniteWholeH1ExclusionClaim=True)
if success is None:
 say("accurate_new_H1_Dixon_original_target_unreturned",
  allOriginalH1ComponentsRemain=True,oldBZeroCover316Unchanged=True,
  wholeH1Excluded=False,ordinaryISPClaim=False)
 signal.alarm(0);raise SystemExit(0)
collect_source_denominators=True
cover=source_cover
for co in success["coefficients"]:record_denominator(co.d)
# The monic Q4 relation has polynomial u coefficients; the returned
# full A4 identity therefore clears to a global polynomial identity.
sf=monic(exact(cover,cover.gcd(cover.derivative())))
removed=[]
for label,pp in [("original u",up),("original u-1",up-1)]:
 gg=sf.gcd(pp)
 if gg.degree()>0:
  old=sf;sf=monic(exact(sf,gg));assert monic(sf*gg)==monic(old)
  removed.append([label,int(gg.degree())])
say("complete_new_whole_H1_original_Dixon_unit_target_weight_cover",
 returnedOriginalUnit=success["label"],exactSquarefreeUCover=pdigest(sf),
 originalChartA0B1AndSourcePolesAllRetained=True,
 allFinalTargetCoefficientPolesRetained=True,
 onlyCancelledIntermediateGaussianPolesNotSeparatelyAdded=True,
 onlyRemovedAlreadyPaidScalarWeightFactors=removed,
 allWholeQQuarticRootComponentsRetained=True,
 strictDifferentH1WeightPairBound=4*int(sf.degree()),
 wholeH1Excluded=(sf.degree()==0),wholePhiFaceExcluded=False,ordinaryISPClaim=False)
checkpoint("new_whole_H1_Dixon_original_unit_target_weight_cover",
 dict(variable="u",coefficientsAscending=coefficients(sf),
 originalUnitTarget=success["label"],weightRelation="the whole monic g4(u,Q)=-12H1",
 originalCoordinateChartA0B1ZeroFibersRetained=True,
 exactSourcePoleCover=pdigest(source_cover),
 finalFullWeightCoordinateIdentityReturned=True,
 allFinalCoefficientDenominatorsCleared=True))
say("new_whole_H1_Dixon_original_attempt_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 actualWholeAlgebraInverseProducts=len(inverses),
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 noOldLambdaEuclidOrResultantReplayed=True,ordinaryISPClaim=False)
signal.alarm(0)
