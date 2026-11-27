#!/usr/bin/env python3
"""NEW full original value input on the exact ten-weight head locus.
Read the saved true QQ F10 and Q=-a9(u). Work in QQ[u]/F10;
every constant inverse has an actual QQ Bezout product. Construct
the four original compact mean/N1 quadratics, retain their complete
rank-two head-zero combinations, and use the resulting SAME two
linear equations. Separate the determinant-zero branch exactly.
On the determinant-nonzero branch impose the original four quads,
original F6, and original NV. Strip only actual lambda and determinant
factors by full K[lambda] gcd/division products; a fixed integral
monic finite original-ideal matrix may then prove whole-branch
exclusion. Any surviving branch and exact coefficients are retained.
120 seconds /1 GiB. One exact ten-weight JSON dependency; no helpers.
"""
import json,time,hashlib,base64,zlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_poly,nmod_poly
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
began=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-began)
 print(json.dumps(kw),flush=True)
name="2026-11-27-unit211-Phi-zero-four-head-common-zero-ten-exact-weights-8542.json"
raw=Path(__file__).with_name(name).read_bytes()
assert hashlib.sha256(raw).hexdigest()=="0181016263cc74ceee904cc5d9c29baf77e5541f2a6535e1c34dfd89a83a619f"
data=json.loads(raw)
phi=fmpq_poly([fmpq(c) for c in data["minimal_polynomial_coefficients_ascending"]])
phi=phi*(1/phi[phi.degree()]);assert phi.degree()==10
stat={"constantQQInverseProducts":0,"KlambdaDivisionProducts":0,
      "KlambdaGcdBezoutProducts":0,"originalLinearCoefficientProducts":0,
      "modMonicDivisionProducts":0,"completeSelectedSquareInverseProducts":0}
inverse_cache={}
class C:
 __slots__=("p",)
 def __init__(self,v=0):
  if isinstance(v,C):self.p=v.p;return
  self.p=(v if isinstance(v,fmpq_poly) else fmpq_poly([v]))%phi
 def __bool__(self):return bool(self.p)
 def __add__(self,o):
  if getattr(o,"_XYZ",False):return NotImplemented
  return C(self.p+C(o).p)
 __radd__=__add__
 def __neg__(self):return C(-self.p)
 def __sub__(self,o):
  if getattr(o,"_XYZ",False):return NotImplemented
  return self+-C(o)
 def __rsub__(self,o):
  if getattr(o,"_XYZ",False):return NotImplemented
  return C(o)+-self
 def __mul__(self,o):
  if getattr(o,"_XYZ",False):return NotImplemented
  return C(self.p*C(o).p)
 __rmul__=__mul__
 def inv(self):
  assert self
  key=str(self.p)
  if key in inverse_cache:return C(inverse_cache[key])
  gg,ss,tt=self.p.xgcd(phi)
  assert ss*self.p+tt*phi==gg and gg.degree()==0
  ans=(ss*(1/gg[0]))%phi
  assert (self.p*ans)%phi==fmpq_poly([1])
  stat["constantQQInverseProducts"]+=1
  inverse_cache[key]=ans;return C(ans)
 def __truediv__(self,o):
  if getattr(o,"_XYZ",False):return NotImplemented
  return self*C(o).inv()
 def __rtruediv__(self,o):
  if getattr(o,"_XYZ",False):return NotImplemented
  return C(o)*self.inv()
 def __pow__(self,n):
  assert isinstance(n,int)
  if n<0:return self.inv()**(-n)
  r=C(1);a=self
  while n:
   if n&1:r=r*a
   n>>=1
   if n:a=a*a
  return r
 def __eq__(self,o):
  if getattr(o,"_XYZ",False):return NotImplemented
  return self.p==C(o).p
 def __repr__(self):return str(self.p)
class P:
 _XYZ=True
 __slots__=("terms",)
 def __init__(self,v=0):
  if isinstance(v,P):self.terms=v.terms;return
  if isinstance(v,dict):self.terms={tuple(e):C(c) for e,c in v.items() if C(c)}
  else:
   c=C(v);self.terms={(0,0,0):c} if c else {}
 def __bool__(self):return bool(self.terms)
 def __add__(self,o):
  o=P(o);r=dict(self.terms)
  for e,c in o.terms.items():
   cc=r.get(e,C())+c
   if cc:r[e]=cc
   elif e in r:del r[e]
  return P(r)
 __radd__=__add__
 def __neg__(self):return P({e:-c for e,c in self.terms.items()})
 def __sub__(self,o):return self+-P(o)
 def __rsub__(self,o):return P(o)+-self
 def __mul__(self,o):
  o=P(o);r={}
  for e,c in self.terms.items():
   for f,d in o.terms.items():
    h=tuple(a+b for a,b in zip(e,f));r[h]=r.get(h,C())+c*d
  return P(r)
 __rmul__=__mul__
 def __truediv__(self,o):
  if isinstance(o,P):
   assert all(e==(0,0,0) for e in o.terms)
   o=o.terms.get((0,0,0),C())
  iv=C(o).inv();return P({e:c*iv for e,c in self.terms.items()})
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  r=P(1);a=self
  while n:
   if n&1:r=r*a
   n>>=1
   if n:a=a*a
  return r
 def __eq__(self,o):return not (self-P(o))
 def uc(self):
  assert all(e[1]==0 and e[2]==0 for e in self.terms)
  n=max((e[0] for e in self.terms),default=-1)
  return [self.terms.get((j,0,0),C()) for j in range(n+1)]
 def const(self):
  assert all(e==(0,0,0) for e in self.terms)
  return self.terms.get((0,0,0),C())
 def profile(self):
  seq=[(e,str(c.p)) for e,c in sorted(self.terms.items())]
  return dict(degrees=[max((e[j] for e in self.terms),default=-1) for j in range(3)],
              terms=len(seq),sha256=hashlib.sha256(str(seq).encode()).hexdigest())
u=C(fmpq_poly([0,1]))
Q=-C(fmpq_poly([fmpq(c) for c in data["a9_numerator_coefficients_ascending"]]))/C(fmpq(data["a9_denominator"]))
ell=1-2*(u-1)*(u-2)/Q
delta=1-Q;m=u-ell;V2=2*u-ell*Q;T0=V2-2*u*u
J=2*u*(1-u)+ell*Q;P02=(2-3*u)*V2-Q*u+2*u**3
Pf=T0*(J-Q);M=ell*V2-u*u;bc=M/(4*delta)
for nm,a in [("u",u),("u-1",u-1),("Q",Q),("1-Q",delta),("ell",ell),
             ("u-ell",m),("M",M),("P02",P02),("T0",T0),
             ("J-Q",J-Q),("u+Q-1",u+Q-1)]:
 assert a,nm
 assert a*a.inv()==1
lam=P({(1,0,0):1});Tr=P({(0,1,0):1});z=P({(0,0,1):1})
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1
G=lam*P02+(u-1)*T0
Pc=Q*P02*(ell+Tr)-G*T0
ff=-Pc/Pf
assert T0+4*u-4+Q==0 and Pf*ff+Pc==0
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


quads=[Rbar,W4,Obar,N1]
slots={(0,0):0,(1,0):1,(0,1):2,(2,0):3,(1,1):4,(0,2):5}
def extract_quad(p):
 rows=[P() for _ in range(6)]
 for (l,t,z0),c in p.terms.items():
  assert (t,z0) in slots
  j=slots[(t,z0)];rows[j]=rows[j]+P({(l,0,0):c})
 assert rows[0]+rows[1]*Tr+rows[2]*z+rows[3]*Tr**2+rows[4]*Tr*z+rows[5]*z**2==p
 return rows
qr=[extract_quad(p) for p in quads]
A=[[p.const() for p in row[3:]] for row in qr]
original_head=[list(row) for row in A]
U=[[C(int(i==j)) for j in range(4)] for i in range(4)]
rank=0;pivots=[]
for col in range(3):
 pivot=next((i for i in range(rank,4) if A[i][col]),None)
 if pivot is None:continue
 A[rank],A[pivot]=A[pivot],A[rank];U[rank],U[pivot]=U[pivot],U[rank]
 iv=A[rank][col].inv();A[rank]=[x*iv for x in A[rank]];U[rank]=[x*iv for x in U[rank]]
 for i in range(4):
  if i==rank:continue
  c=A[i][col]
  if c:
   A[i]=[x-c*y for x,y in zip(A[i],A[rank])]
   U[i]=[x-c*y for x,y in zip(U[i],U[rank])]
 pivots.append(col);rank+=1
assert all(sum((U[i][k]*original_head[k][j] for k in range(4)),C())==A[i][j]
           for i in range(4) for j in range(3))
transformed=[sum((U[i][j]*quads[j] for j in range(4)),P()) for i in range(4)]
for i,p in enumerate(transformed):
 assert [x.const() for x in extract_quad(p)[3:]]==A[i]
say("new_exact_ten_weight_original_quadratic_head_rank",
    trueQQConstantDegree=10,actualHeadRank=rank,pivotColumns=pivots,
    allOriginalRowTransformationProductsReturned=True,
    transformedOriginalProfiles=[p.profile() for p in transformed])
assert rank<=2
if rank!=2:
 say("new_ten_weight_input_unresolved",reason="head rank is not two",
     actualHeadRank=rank,wholeTenWeightBranchExcluded=False,ordinaryISPClaim=False)
 raise SystemExit(0)
lines=[extract_quad(p)[:3] for p in transformed[2:]]
a0,at,az=lines[0];b0,bt,bz=lines[1]
hd=at*bz-az*bt
Nt=az*b0-bz*a0;Nz=bt*a0-at*b0
assert at*Nt+az*Nz==-hd*a0 and bt*Nt+bz*Nz==-hd*b0
stat["originalLinearCoefficientProducts"]+=2
say("new_same_two_original_linear_equations",
    determinant=hd.profile(),Tnumerator=Nt.profile(),znumerator=Nz.profile(),
    originalLineProfiles=[[p.profile() for p in row] for row in lines],
    completeTwoCramerCoefficientIdentitiesReturned=True)
if not hd:
 say("new_ten_weight_input_unresolved",reason="same two linear determinant identically zero",
     wholeTenWeightBranchExcluded=False,ordinaryISPClaim=False)
 raise SystemExit(0)
def tr(a):
 a=[C(x) for x in a]
 while a and not a[-1]:a.pop()
 return a
def add(a,b):
 c=[C()]*max(len(a),len(b))
 for i in range(len(a)):c[i]=c[i]+a[i]
 for i in range(len(b)):c[i]=c[i]+b[i]
 return tr(c)
def sub(a,b):return add(a,[-x for x in b])
def mul(a,b):
 if not a or not b:return []
 c=[C()]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=c[i+j]+x*y
 return tr(c)
def scl(a,c):return tr([x*c for x in a])
def dv(a,b):
 a=tr(a);b=tr(b);assert b
 original=list(a);q=[C()]*max(0,len(a)-len(b)+1);iv=b[-1].inv()
 while a and len(a)>=len(b):
  shift=len(a)-len(b);c=a[-1]*iv;q[shift]=c
  for j in range(len(b)):a[shift+j]=a[shift+j]-c*b[j]
  a=tr(a)
 q=tr(q);assert add(mul(q,b),a)==original
 stat["KlambdaDivisionProducts"]+=1
 return q,a
def xgcd(a,b):
 a=tr(a);b=tr(b);aa,bb=list(a),list(b)
 r0,r1=a,b;s0,s1=[C(1)],[];t0,t1=[],[C(1)]
 while r1:
  q,r=dv(r0,r1);r0,r1=r1,r
  s0,s1=s1,sub(s0,mul(q,s1));t0,t1=t1,sub(t0,mul(q,t1))
 if r0:
  iv=r0[-1].inv();r0=scl(r0,iv);s0=scl(s0,iv);t0=scl(t0,iv)
 assert add(mul(s0,aa),mul(t0,bb))==r0
 stat["KlambdaGcdBezoutProducts"]+=1
 return r0,s0,t0
def encode_coeffs(a):
 return [[str(c.p[j]) for j in range(c.p.degree()+1)] for c in a]
def save_polys(stage,polys,**kw):
 obj={label:encode_coeffs(a) for label,a in polys}
 raw=json.dumps(obj,separators=(",",":")).encode();packed=zlib.compress(raw,9)
 back=json.loads(zlib.decompress(packed))
 for label,a in polys:
  assert [C(fmpq_poly([fmpq(c) for c in seq])) for seq in back[label]]==a
 say(stage,encoding="base64+zlib+json",
     payloadSha256=hashlib.sha256(raw).hexdigest(),
     data=base64.b64encode(packed).decode(),uncompressedBytes=len(raw),
     allDecodedOriginalCoefficientProductsReturned=True,**kw)
hp=hd.uc()
g0,_,_=xgcd(hp,Nt.uc());g0,_,_=xgcd(g0,Nz.uc())
while len(g0)>1 and not g0[0]:
 oldg=list(g0);g0=g0[1:]
 assert mul([C(),C(1)],g0)==oldg
degenerate_excluded=len(g0)==1
save_polys("new_exact_linear_determinant_zero_compatibility",
           [("determinant",hp),("Tnumerator",Nt.uc()),("znumerator",Nz.uc()),("residual",g0)],
           residualLambdaDegree=len(g0)-1,
           determinantZeroBranchExcluded=degenerate_excluded,
           removedOnlyOriginalLambdaUnit=True)
# Complete additional original moment and NV conditions, with no
# geometric inverse.  All remain the same T,z before Cramer substitution.
D=ell*A2-Tr*Tr;sn=ell*B3-A2*Tr;zn=Tr*B3-A2*A2
Kr=ell*ell*B3-3*ell*Tr*A2+2*Tr**3
Z=u*sn-2*Tr*D;Sn=sn+(3-2*lam)*D
F6=M*Kr*Kr-4*m*m*D**3
ww=lam-1-Tr
NF4=4*m*((3-4*lam)*Q*D*D-J*zn*D)+2*Sn*(-2*u*Q*Kr+J*Z)
NC4=(4*m*G*zn*D-2*G*Sn*Z-Q*T0*Sn*Kr
     +4*m*Q*ww*u*(3-2*lam)*D*D+2*m*Q*ww*u*sn*D
     -2*Q*ww*(u-ell*Q)*Kr*D)
NV=NF4*ff+NC4+2*bc*Sn*Z*z
def substitute_clear(p):
 d=max((e[1]+e[2] for e in p.terms),default=0)
 ht=[P(1)];tt=[P(1)];zz=[P(1)]
 for j in range(d):
  ht.append(ht[-1]*hd);tt.append(tt[-1]*Nt);zz.append(zz[-1]*Nz)
 out=P()
 for (l,t,z0),c in p.terms.items():
  out=out+c*(lam**l)*tt[t]*zz[z0]*ht[d-t-z0]
 assert all(e[1]==0 and e[2]==0 for e in out.terms)
 return out.uc(),d
labels=["mean_R","mean_W","mean_O","original_N1","original_F6","original_NV"]
raw_poly=[];values=[];removed=[]
for label,p in zip(labels,quads+[F6,NV]):
 a,d=substitute_clear(p);raw_poly.append((label,a))
 if not a:continue
 divs=[]
 for uname,unit in [("same_linear_determinant",hp),("original_lambda",[C(),C(1)])]:
  while len(a)>1:
   gg,_,_=xgcd(a,unit)
   if len(gg)<=1:break
   q,r=dv(a,gg);assert not r and mul(q,gg)==a
   divs.append([uname,len(gg)-1]);a=q
 values.append((label,a));removed.append(dict(original=label,removed=divs,clearingPower=d))
say("new_original_value_polynomials_on_same_linear_open_chart",
    degrees={label:len(a)-1 for label,a in values},
    exactOriginalUnitAndDeterminantFactorDivisions=removed,
    noIndividualNBPBCompletenessClaim=True)
save_polys("new_exact_recoverable_ten_weight_original_lambda_polynomials",
           values+[("same_linear_determinant",hp)],
           originalLabels=[label for label,a in values])
if not values:
 say("new_ten_weight_open_input_unresolved",reason="all imposed original polynomials vanish identically",
     wholeTenWeightBranchExcluded=False,ordinaryISPClaim=False)
 raise SystemExit(0)
j0=min(range(len(values)),key=lambda j:len(values[j][1]))
base=values[j0][1];n=len(base)-1
iv=base[-1].inv();monic=scl(base,iv);assert monic[-1]==1
assert scl(monic,base[-1])==base
if n==0:
 say("complete_new_ten_weight_original_value_return",
     openLinearChartExcluded=True,determinantZeroBranchExcluded=degenerate_excluded,
     wholeTenWeightBranchExcluded=degenerate_excluded,
     reason="one actual original residual is a nonzero K constant",
     checks=stat,ordinaryISPClaim=False)
 raise SystemExit(0)
chosen=None
allq=[phi]+[c.p for c in monic]+[c.p for _,a in values for c in a]
for prime in [1009,1013,1019,1021,1031,1033,1039,1049,1051]:
 assert all(prime%d for d in range(2,int(prime**0.5)+1))
 if all(int(p[j].denominator)%prime for p in allq for j in range(p.degree()+1)):
  chosen=prime;break
assert chosen is not None
prime=chosen
def bar(p):
 cc=[]
 for j in range(p.degree()+1):
  c=p[j];den=int(c.denominator)%prime;assert den
  v=pow(den,-1,prime);assert den*v%prime==1
  cc.append(int(c.numerator)%prime*v%prime)
 return nmod_poly(cc,prime)
phibar=bar(phi);mz=nmod_poly([],prime);mo=nmod_poly([1],prime)
def mk(p):return p%phibar
def mt(a):
 a=[mk(x) for x in a]
 while a and not a[-1]:a.pop()
 return a
def ma(a,b):
 c=[mz]*max(len(a),len(b))
 for i in range(len(a)):c[i]=c[i]+a[i]
 for i in range(len(b)):c[i]=c[i]+b[i]
 return mt(c)
def mm(a,b):
 if not a or not b:return []
 c=[mz]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=c[i+j]+x*y
 return mt(c)
mf=mt([bar(c.p) for c in monic]);assert len(mf)==n+1 and mf[-1]==mo
def red(a):
 a=mt(a);old=list(a);q=[mz]*max(0,len(a)-n)
 while a and len(a)>n:
  shift=len(a)-1-n;c=a[-1];q[shift]=c
  for j in range(n+1):a[shift+j]=mk(a[shift+j]-c*mf[j])
  a=mt(a)
 q=mt(q);assert ma(mm(q,mf),a)==old
 stat["modMonicDivisionProducts"]+=1
 return a
rows=[];tags=[]
for j,(label,a) in enumerate(values):
 if j==j0:continue
 cur=red([bar(c.p) for c in a])
 for lpower in range(n):
  for upower in range(10):
   up=nmod_poly([0]*upower+[1],prime);cc=[mk(c*up) for c in cur]
   row=[]
   for l in range(n):
    c=cc[l] if l<len(cc) else mz
    row.extend(int(c[t]) for t in range(10))
   rows.append(row);tags.append([label,lpower,upower])
  cur=red([mz]+cur)
dim=10*n;basis={};picked=[]
for ix,row in enumerate(rows):
 a=list(row)
 for p,b in sorted(basis.items()):
  c=a[p]
  if c:
   for j in range(p,dim):a[j]=(a[j]-c*b[j])%prime
 p=next((j for j,c in enumerate(a) if c),None)
 if p is None:continue
 iv=pow(a[p],-1,prime);assert a[p]*iv%prime==1
 basis[p]=[c*iv%prime for c in a];picked.append(ix)
 if len(basis)==dim:break
full=len(basis)==dim;cert=None
if full:
 B=[list(rows[i]) for i in picked]
 aug=[r+[int(i==j) for j in range(dim)] for i,r in enumerate(B)]
 for j in range(dim):
  p=next(i for i in range(j,dim) if aug[i][j]);aug[j],aug[p]=aug[p],aug[j]
  iv=pow(aug[j][j],-1,prime);assert aug[j][j]*iv%prime==1
  aug[j]=[c*iv%prime for c in aug[j]]
  for i in range(dim):
   if i==j:continue
   c=aug[i][j]
   if c:aug[i]=[(x-c*y)%prime for x,y in zip(aug[i],aug[j])]
 inverse=[r[dim:] for r in aug]
 assert all(aug[i][j]==int(i==j) for i in range(dim) for j in range(dim))
 columns=list(zip(*inverse))
 assert all(sum(x*y for x,y in zip(row,col))%prime==int(i==j)
            for i,row in enumerate(B) for j,col in enumerate(columns))
 stat["completeSelectedSquareInverseProducts"]+=1
 cert=dict(selectedOriginalRowTags=[tags[i] for i in picked],
           matrixSha256=hashlib.sha256(str(B).encode()).hexdigest(),
           inverseSha256=hashlib.sha256(str(inverse).encode()).hexdigest(),
           completeSelectedSquareTimesInverseReturned=True)
say("complete_new_ten_weight_original_value_return",
    trueQQWeightDegree=10,prime=prime,monicOriginalLambdaPolynomial=values[j0][0],
    monicOriginalLambdaDegree=n,finiteAlgebraDimension=dim,
    genuineOriginalIdealRows=len(rows),actualModRank=len(basis),
    integralFixedQQMatrixGaussCertificate=cert,
    openLinearChartExcluded=full,determinantZeroBranchExcluded=degenerate_excluded,
    wholeTenWeightBranchExcluded=full and degenerate_excluded,
    originalLambdaOpenChartCandidateBound=10*n if not full else 0,
    fullQQDegenerateCompatibilitySaved=True,
    noBareModularSaturationInference=True,
    noUnpaidGeometricNormInverse=True,checks=stat,ordinaryISPClaim=False)
