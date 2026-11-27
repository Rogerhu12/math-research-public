#!/usr/bin/env python3
"""NEW entire quartic S-moment-image fiber, NOT the already closed S=0 branch.
Original constant weights b=1,c=1/2, ell=3/2, Phi=0, D nonzero.
Read only the three saved original same-rho curves. In the full quartic
field M_J/420 construct the NEW exact G/H multiplication image in
K[rho]/F; rank plus complete short division returns the full same-rho gcd.
Use the original F6 T6 and Sn T2 to remove only already excluded S factors,
retaining every remaining T value and every original rho embedding.
Original N1 has its paid z^2 head. The full compact original means and NV
enter the same monic finite algebra. An integral original-ideal square
matrix times its inverse is the complete constant-fiber certificate.
The new full original R quotient uses only actual QQ divisibility from
explicit same-source fixed Sylvester kernel vectors, never modular
support lifting. No former S=0 Gram, cofactor, high Euclid, or whole
resultant gate is rerun. 120 seconds /1 GiB. Three saved JSON inputs.
"""
import time,json,hashlib,base64,zlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx,nmod_poly,fmpq_mat
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
began=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-began)
 print(json.dumps(kw),flush=True)
ctx=fmpq_mpoly_ctx.get(("rho","lam"),"lex")
def load_poly(data,payload_sha,poly_sha,degrees,terms):
 raw=zlib.decompress(base64.b64decode(data))
 assert hashlib.sha256(raw).hexdigest()==payload_sha
 obj=json.loads(raw);assert obj["variables"]==["rho","lam"]
 pp=ctx.from_dict({(int(i),int(j)):fmpq(c) for i,j,c in obj["terms"]})
 assert list(map(int,pp.degrees()))==degrees and len(pp.to_dict())==terms
 assert hashlib.sha256(str(sorted(pp.to_dict().items())).encode()).hexdigest()==poly_sha
 return pp
def dependency(name,sha256):
 path=Path(__file__).with_name(name)
 raw=path.read_bytes()
 assert hashlib.sha256(raw).hexdigest()==sha256,("wrong exact dependency",name)
 return json.loads(raw)
inputF=dependency(
 "2026-11-27-unit211-Phi-zero-exceptional-F26-exact-input-8542.json",
 "67c73f8f5fef33d509ffebd8165487e5b6abcc59fe391acc4075da1f22287d61")
inputG=dependency(
 "2026-11-27-unit211-Phi-zero-exceptional-PB-core-and-mod-resultant-exact-input-8542.json",
 "74891d2b2f8bd21f74ff063cef7aeed85532a2378e71dac07ad5cfc4d240c8c9")
inputH=dependency(
 "2026-11-27-unit211-Phi-zero-exceptional-mixed-core-and-mod-return-exact-input-8542.json",
 "a9ab01ff03d894ed1fe6033b68268ecbf7b9d36dc2cd4ff3d7bf69b771387073")
rf,rg,rh=(obj["polynomial"] for obj in (inputF,inputG,inputH))
F=load_poly(rf["data"],rf["payloadSha256"],
 "9057238c5d37c8cd9f62f3f512dcff1f6d2e385cd6c0e39250a571713f0aaac7",[26,26],729)
G=load_poly(rg["data"],rg["payloadSha256"],
 "3d850765f6c9338aa8f79af2b5889582cf8d4f45fd81ad90f4743fb5bebd5f6c",[31,50],1632)
H=load_poly(rh["data"],rh["payloadSha256"],
 "496ce5b01ff327ac7b1fa6a125f04808d368aca7a88b0078f0e0622ced90f8e4",[34,48],1715)


phi=fmpq_poly([fmpq(916,420),fmpq(-3084,420),fmpq(3663,420),
                 fmpq(-1884,420),1])
e=4
phi_content,phi_factors=phi.factor()
phi_product=fmpq_poly([phi_content])
for fact,mult in phi_factors:phi_product*=fact**mult
assert phi_product==phi and len(phi_factors)==1 and phi_factors[0][1]==1
say("new_whole_original_S_moment_image_constant_field",
    phiAscending=[str(phi[i]) for i in range(e+1)],
    completeQQIrreducibleFactorProductReturned=True,
    oldSZeroSubbranchExcludedButEntirePhiFiberNotPreviouslyExcluded=True)
kzero=fmpq_poly([]);kone=fmpq_poly([1])
checks={"QQPhiDivisionProducts":0,"QQFieldInverseProducts":0,
        "QQRhoDivisionProducts":0,"QQNamedBaseInverseProducts":0,
        "exactFormalOriginalReductionProducts":0}
def kk(p):
 if not isinstance(p,fmpq_poly):p=fmpq_poly([p])
 q,r=divmod(p,phi);assert q*phi+r==p
 checks["QQPhiDivisionProducts"]+=1
 return r
inverse_cache={}
def ki(p):
 p=kk(p);assert p
 key=str(p)
 if key in inverse_cache:return inverse_cache[key]
 g,s,t=p.xgcd(phi);assert s*p+t*phi==g and g.degree()==0
 ans=kk(s*(1/g[0]));assert kk(ans*p)==kone
 checks["QQFieldInverseProducts"]+=1;inverse_cache[key]=ans
 return ans
def kt(a):
 out=[kk(p) for p in a]
 while out and not out[-1]:out.pop()
 return out
def ka(a,b):
 out=[kzero]*max(len(a),len(b))
 for i,v in enumerate(a):out[i]=out[i]+v
 for i,v in enumerate(b):out[i]=out[i]+v
 return kt(out)
def kn(a):return kt([-v for v in a])
def ks(a,b):return ka(a,kn(b))
def km(a,b):
 if not a or not b:return []
 out=[kzero]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
 return kt(out)
def kd(a,b):
 a=kt(a);b=kt(b);assert b;original=list(a)
 q=[kzero]*max(0,len(a)-len(b)+1);iv=ki(b[-1])
 while a and len(a)>=len(b):
  shift=len(a)-len(b);c=kk(a[-1]*iv);q[shift]=kk(q[shift]+c)
  for j,v in enumerate(b):a[shift+j]=kk(a[shift+j]-c*v)
  a=kt(a)
 q=kt(q)
 assert ka(km(q,b),a)==original
 checks["QQRhoDivisionProducts"]+=1
 return q,a
def monic(a):
 a=kt(a)
 return [kk(x*ki(a[-1])) for x in a] if a else []
def kgcd(a,b,label):
 a=kt(a);b=kt(b);steps=0
 while b:
  q,r=kd(a,b);a,b=b,r;steps+=1
  say("new_exact_QQ_single_variable_gcd_step",pair=label,step=steps,
      divisorDegree=len(a)-1,nextRemainderDegree=len(b)-1)
 return monic(a)
def kxgcd(a,b):
 a=kt(a);b=kt(b);oa=list(a);ob=list(b)
 s0,s1=[kone],[];t0,t1=[],[kone]
 while b:
  q,r=kd(a,b);a,b=b,r
  s0,s1=s1,ks(s0,km(q,s1));t0,t1=t1,ks(t0,km(q,t1))
 assert ka(km(s0,oa),km(t0,ob))==a
 if a:
  iv=ki(a[-1]);a=[kk(x*iv) for x in a]
  s0=[kk(x*iv) for x in s0];t0=[kk(x*iv) for x in t0]
 assert ka(km(s0,oa),km(t0,ob))==a
 return a,s0,t0
def in_rho(p):
 out=[kzero]*(int(p.degrees()[0])+1)
 for (i,j),c in p.to_dict().items():
  row=[fmpq(0)]*(int(j)+1);row[int(j)]=c
  out[int(i)]=out[int(i)]+fmpq_poly(row)
 return kt(out)
# First use only the NEW small original T6 and S numerator T2
# in the entire irreducible quartic constant field.
klam=fmpq_poly([0,1]);kell=fmpq(3,2)
kA=kk(2*klam*klam-2*klam+1)
kB=kk(4*klam**3-6*klam**2+3*klam-1)
kD=[kk(kell*kA),kzero,fmpq_poly([-1])]
kK=[kk(kell*kell*kB),kk(-3*kell*kA),kzero,fmpq_poly([2])]
kS=kt([kk(kell*kB+(3-2*klam)*kell*kA),-kA,kk(2*klam-3)])
unscaled6=ks([kk(2*c) for c in km(kK,kK)],km(km(kD,kD),kD))
assert len(unscaled6)==7 and unscaled6[-1]==fmpq_poly([9])
q6=monic(unscaled6);qT=list(q6);removedT=[]
while True:
 common=kgcd(qT,kS,"NEW_original_T6_vs_actual_S_numerator_T2")
 if len(common)==1:break
 oldq=list(qT);quotient,remainder=kd(qT,common)
 assert not remainder and km(quotient,common)==oldq
 qT=monic(quotient);removedT.append(common)
assert 1<=len(qT)-1<=6
tdegree=len(qT)-1
back=list(qT)
for fac in removedT:back=km(back,fac)
assert back==q6
say("complete_new_whole_S_moment_image_original_small_T_relation",
    originalF6AfterRhoUnitRemoval="2*K(T)^2-D(T)^3",
    originalF6Leading="9",
    originalSCondition="Sn=sn+(3-2*lambda)*D is a unit because original S and D are units",
    removedOnlyFactorsOfActualSn=True,
    removedFactorDegrees=[len(v)-1 for v in removedT],
    quotientTDegree=tdegree,
    quotientAscending=[[str(c[i]) for i in range(e)] for c in qT],
    removedFactorsAscending=[[[str(c[i]) for i in range(e)] for c in fac] for fac in removedT],
    completeQQDivisionsAndOriginalT6ReconstructionReturned=True,
    notReplayingOldSZeroGram=True)
values=[in_rho(p) for p in (F,G,H)]
fdegree=len(values[0])-1
assert 0<=fdegree<=26
say("new_original_curve_specializations_in_whole_quartic_field",
    actualRhoDegrees=[len(v)-1 for v in values],
    allLeadingCoefficientZeroFibersRetained=True,
    constantFieldDegree=e)
if fdegree==0:
 assert values[0][0]
 inverse=ki(values[0][0]);assert kk(inverse*values[0][0])==kone
 say("complete_original_psiS_fiber_exclusion",
     reason="the complete original F is a nonzero constant in the entire quartic field",
     entireMomentImageFiberExcluded=True,ordinaryISPClaim=False)
 raise SystemExit(0)
mf=monic(values[0])
assert mf[-1]==kone
assert [kk(c*values[0][-1]) for c in mf]==values[0]
columns=fdegree*e
lpowers=[fmpq_poly([0]*i+[1]) for i in range(e)]
qqrows=[]
for label,v in zip(["G","H"],values[1:]):
 _,cur=kd(v,mf)
 for rpower in range(fdegree):
  for lpower in range(e):
   cc=[kk(c*lpowers[lpower]) for c in cur]
   row=[]
   for rpower0 in range(fdegree-1,-1,-1):
    c=cc[rpower0] if rpower0<len(cc) else kzero
    row.extend(c[i] for i in range(e))
   assert len(row)==columns;qqrows.append(row)
  if rpower+1<fdegree:_,cur=kd([kzero]+cur,mf)
say("new_original_QQ_G_and_H_multiplication_row_space_built",
    rows=len(qqrows),columns=columns,
    originalSources="rho^j*lambda^i*G and rho^j*lambda^i*H modulo the actual monic original F",
    allQQMonicDivisionProductsReturned=True,
    noHighDegreeKPolynomialEuclidOrFormerLocalKernelRecomputed=True)
linear=fmpq_mat(qqrows)
reduced_matrix,linear_rank=linear.rref();linear_rank=int(linear_rank)
assert linear_rank%e==0
common_degree=fdegree-linear_rank//e
assert 0<=common_degree<=fdegree
pivots=[]
for i in range(linear_rank):
 p=next(j for j in range(columns) if reduced_matrix[i,j])
 assert reduced_matrix[i,p]==1;pivots.append(p)
assert pivots==list(range(linear_rank))
if common_degree==fdegree:
 candidate=list(mf)
else:
 target_column=(fdegree-1-common_degree)*e
 target_row=pivots.index(target_column)
 candidate=[kzero]*fdegree
 for column in range(columns):
  rpower0=fdegree-1-column//e;lpower=column%e
  c=reduced_matrix[target_row,column]
  if c:
   term=[fmpq(0)]*(lpower+1);term[lpower]=c
   candidate[rpower0]=candidate[rpower0]+fmpq_poly(term)
 candidate=kt(candidate)
assert len(candidate)==common_degree+1 and candidate[-1]==kone
short_divisions=[];quotients=[]
for label,v in zip(["F","G","H"],values):
 quotient,remainder=kd(v,candidate)
 assert not remainder and km(quotient,candidate)==v
 quotients.append(quotient)
 short_divisions.append(dict(original=label,actualOriginalDegree=len(v)-1,
     exactMonicDivisorDegree=common_degree,completeQQProductReturned=True))
# Rank of the K-linear image ideal (G,H) in K[rho]/F is
# fdegree-common_degree. Hence candidate of this exact degree is
# the full monic gcd, not merely a proper common divisor.
g=candidate
say("complete_new_true_QQ_same_rho_common_gcd_from_original_linear_input",
    originalQQRows=len(qqrows),originalQQColumns=columns,
    originalQQRank=linear_rank,
    originalFieldDegree=e,degree=common_degree,
    coefficientsAscending=[[str(c[i]) for i in range(e)] for c in g],
    exactFullOriginalShortDivisions=short_divisions,
    fullOriginalFGRhoHRootCoveragePaidByQQImageRankAndExactDivisibility=True,
    allFourLambdaEmbeddingsRetained=True,
    coefficientPayloadSha256=hashlib.sha256(str(g).encode()).hexdigest())
if common_degree==0:
 say("complete_original_psiS_fiber_exclusion",
     reason="the full original F,G,H gcd is one in the entire quartic field",
     entireMomentImageFiberExcluded=True,ordinaryISPClaim=False)
 raise SystemExit(0)
# Produce common_degree independent actual original 57-column
# Sylvester kernel vectors over K. Fixed original degrees stay
# 26/31 in the matrix, even if specialization lowered a leading term.
qF,qG=quotients[:2]
kernel=[]
for j in range(common_degree):
 a=[kzero]*j+qG;b=[kzero]*j+kn(qF)
 assert len(a)<=31 and len(b)<=26
 assert not ka(km(a,values[0]),km(b,values[1]))
 kernel.append(a+[kzero]*(31-len(a))+b+[kzero]*(26-len(b)))
assert len(qF)>0
say("complete_new_original_fixed_Sylvester_QQ_local_divisibility_lower_bound",
    originalFixedSylvesterDegrees=[26,31],originalFixedOrder=57,
    independentKKernelColumns=common_degree,
    independence="the shifted nonzero F/g blocks have distinct highest rho degrees",
    completeOriginalKernelProductsReturned=True,
    trueQQPhiDivisibilityLowerBound=common_degree,
    kernelSha256=hashlib.sha256(str(kernel).encode()).hexdigest(),
    noClaimOfExactMultiplicityBeforeActualModularUpperBound=True)

removed=[]
for label,r in [("1-Q",fmpq(0)),("Q_plus",fmpq(1)),("Q_minus",fmpq(-1)),
                ("u",fmpq(-3)),("T0",fmpq(3)),("u+Q-1",fmpq(3,2))]:
 linear=[fmpq_poly([-r]),kone]
 while len(g)>1:
  common=kgcd(g,linear,"paid_rho_unit_"+label)
  if len(common)==1:break
  oldg=list(g);q,rem=kd(g,common);assert not rem and km(q,common)==oldg
  g=monic(q);removed.append(label)
if len(g)==1:
 say("complete_original_psiS_fiber_exclusion",
     reason="all exact QQ rho components lie on already excluded original units",
     removedOnlyOriginalUnits=removed,entireMomentImageFiberExcluded=True,ordinaryISPClaim=False)
 raise SystemExit(0)
n=len(g)-1
def cr(a):
 a=kt(a)
 if len(a)<=n:return a
 q,r=kd(a,g);return r
named_inverses=[]
class C:
 def __init__(self,v=0):
  if isinstance(v,C):self.v=list(v.v);return
  if isinstance(v,list):self.v=cr(v);return
  self.v=cr([v if isinstance(v,fmpq_poly) else fmpq_poly([v])])
 def __bool__(self):return bool(self.v)
 def __add__(self,o):
  if hasattr(o,"is_formal"):return NotImplemented
  return C(ka(self.v,C(o).v))
 __radd__=__add__
 def __neg__(self):return C(kn(self.v))
 def __sub__(self,o):return self+-o if hasattr(o,"is_formal") else self+-C(o)
 def __rsub__(self,o):return C(o)+-self
 def __mul__(self,o):
  if hasattr(o,"is_formal"):return NotImplemented
  return C(km(self.v,C(o).v))
 __rmul__=__mul__
 def __truediv__(self,o):
  assert isinstance(o,(int,fmpq))
  return self*C(fmpq(1)/o)
 def __pow__(self,p):
  assert isinstance(p,int) and p>=0
  out=C(1);b=self
  while p:
   if p&1:out=out*b
   p//=2
   if p:b=b*b
  return out
 def __eq__(self,o):
  if hasattr(o,"is_formal"):return NotImplemented
  return self.v==C(o).v
 def inverse_named(self,label,reason):
  gg,s,t=kxgcd(self.v,g)
  assert gg==[kone],("named constant-algebra unit failed",label)
  result=C(s);assert self*result==C(1)
  checks["QQNamedBaseInverseProducts"]+=1
  named_inverses.append(dict(label=label,reason=reason,
      exactQQInverseProductReturned=True))
  return result
class P:
 is_formal=True
 def __init__(self,v=0):
  if isinstance(v,P):self.v=dict(v.v);return
  c=C(v);self.v={(0,0):c} if c else {}
 @classmethod
 def from_terms(cls,d):
  out=cls();out.v={tuple(k):C(v) for k,v in d.items() if C(v)}
  return out
 def __bool__(self):return bool(self.v)
 def __add__(self,o):
  o=P(o);out=dict(self.v)
  for a,c in o.v.items():
   out[a]=out.get(a,C(0))+c
   if not out[a]:del out[a]
  return P.from_terms(out)
 __radd__=__add__
 def __neg__(self):return P.from_terms({a:-c for a,c in self.v.items()})
 def __sub__(self,o):return self+-P(o)
 def __rsub__(self,o):return P(o)+-self
 def __mul__(self,o):
  o=P(o);out={}
  for (i,j),c in self.v.items():
   for (k,l),d in o.v.items():
    a=(i+k,j+l);out[a]=out.get(a,C(0))+c*d
  return P.from_terms(out)
 __rmul__=__mul__
 def __truediv__(self,o):
  assert isinstance(o,(int,fmpq))
  return self*C(fmpq(1)/o)
 def __pow__(self,p):
  assert isinstance(p,int) and p>=0
  ans=P(1);b=self
  while p:
   if p&1:ans=ans*b
   p//=2
   if p:b=b*b
  return ans
 def __eq__(self,o):return self.v==P(o).v
rho=C([kzero,kone]);lam=C(fmpq_poly([0,1]))
u=(3+rho)/2;Q=1-rho**2;ell=C(fmpq(3,2));m=u-ell
delta=1-Q
delta_inv=delta.inverse_named("1-Q","original physical weight unit")
V2=2*u-ell*Q;T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
P02=(2-3*u)*V2-Q*u+2*u**3;Pf=T0*(J-Q)
Pf_inv=Pf.inverse_named("Pf=T0*(J-Q)","both original entire weight faces already excluded")
M=ell*V2-u*u;bc=M*delta_inv/4
assert m==rho/2 and M==2*rho**2 and bc==C(fmpq(1,2))
assert T0==-Q-4*(u-1) and J-Q==-4*(u-1)**2
assert P02==2*(u-1)*ell*Q
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam**2+3*lam-1
x=P.from_terms({(1,0):1});z=P.from_terms({(0,1):1})
Tr=x
qTformal=P.from_terms({(i,0):C(c) for i,c in enumerate(qT) if c})
fullD=ell*A2-Tr**2
fullK=ell**2*B3-3*ell*Tr*A2+2*Tr**3
fullF6=M*fullK**2-4*m**2*fullD**3
fullSn=ell*B3-A2*Tr+(3-2*lam)*fullD
assert fullF6==rho**2*(2*fullK**2-fullD**3)
assert fullSn==P.from_terms({(i,0):C(c) for i,c in enumerate(kS) if c})
reconstruct=qTformal
for fac in removedT:
 reconstruct=reconstruct*P.from_terms({(i,0):C(c) for i,c in enumerate(fac) if c})
assert fullF6==9*rho**2*reconstruct
assert qTformal.v[(tdegree,0)]==C(1)
prospective_dimension=e*n*tdegree*2
say("new_original_S_unit_reduction_in_whole_rho_constant_algebra",
    actualRhoDegree=n,remainingTDegree=tdegree,
    prospectiveQQDimension=prospective_dimension,
    fullOriginalF6AndSnIdentitiesReturned=True,
    allOriginalQQRhoEmbeddingsRetained=True)
if prospective_dimension>480:
 say("accurate_new_finite_algebra_checkpoint",
     exactOriginalConstantAlgebraAndPhysicalTQuotientPaid=True,
     completeValueMatrixNotRun=True,
     reason="the genuinely new algebra exceeds the fixed 480 dimension small-input limit",
     ordinaryISPClaim=False)
 raise SystemExit(0)

G=lam*P02+(u-1)*T0
Pc=Q*P02*(ell+Tr)-G*T0
ff=-Pc*Pf_inv
assert Pf*ff+Pc==0
aa=1-ell
vn=J*ff-G+bc*z
wstar=T0+4*u*ff
nn=Q*wstar-2*vn
ww=lam-1-Tr
ii=((vn+aa*u*Q)**2-2*u*Q*vn+2*aa*u*u*Q*Q
    -4*aa*u*Q*Q*ff+bc*z*z+z*(4*bc*u*Q-ell*vn))
Rbar=ii+(m*delta_inv/2)*z*nn
W4=(8*bc*delta*Q*Q*ell*T0-4*ell*delta*vn*vn-ell*nn*nn
    +4*m*vn*nn+32*bc*delta*Q*ff*vn+16*bc*bc*delta*z*z
    +32*bc*bc*delta*Q*(u-1)*z-8*bc*ell*delta*z*vn+4*bc*m*z*nn)
s0=2*ell*vn-(m*delta_inv)*nn
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

head=N1.v.get((0,2),C(0))
assert head==-4*bc**2*ell*Q*(u-1)
assert all(j<=2 and (j!=2 or i==0) for i,j in N1.v)
head_inv=head.inverse_named("original N1 z^2 head",
    "proved full original coefficient -4*bc^2*ell*Q*(u-1), all factors physical weight units")
n1monic=N1*head_inv
assert n1monic.v[(0,2)]==C(1)
Dr=fullD;sn=ell*B3-A2*Tr;zn=Tr*B3-A2*A2
Kr=fullK;Z=u*sn-2*Tr*Dr;Sn=sn+(3-2*lam)*Dr
NF4=4*m*((3-4*lam)*Q*Dr*Dr-J*zn*Dr)+2*Sn*(-2*u*Q*Kr+J*Z)
NC4=(4*m*G*zn*Dr-2*G*Sn*Z-Q*T0*Sn*Kr
     +4*m*Q*ww*u*(3-2*lam)*Dr*Dr
     +2*m*Q*ww*u*sn*Dr-2*Q*ww*(u-ell*Q)*Kr*Dr)
NV=NF4*ff+NC4+2*bc*Sn*Z*z
assert Kr+2*Tr*Dr==ell*sn
assert ell*Z==2*m*Tr*Dr+u*Kr
original_rows=[("mean_R",Rbar),("mean_W",W4),("mean_O",Obar),("original_NV",NV)]
def reduce_formal(p):
 p=P(p);original=P(p);qz=P(0);qx=P(0)
 while any(j>=2 for i,j in p.v):
  j,i=max((j,i) for i,j in p.v if j>=2)
  c=p.v[(i,j)];term=P.from_terms({(i,j-2):c})
  p=p-term*n1monic;qz=qz+term
 while any(i>=tdegree for i,j in p.v):
  i,j=max((i,j) for i,j in p.v if i>=tdegree)
  c=p.v[(i,j)];term=P.from_terms({(i-tdegree,j):c})
  p=p-term*qTformal;qx=qx+term
 assert p+qz*n1monic+qx*qTformal==original
 assert all(i<tdegree and j<2 for i,j in p.v)
 checks["exactFormalOriginalReductionProducts"]+=1
 return p
reduced_rows=[(label,reduce_formal(p)) for label,p in original_rows]
def saveC(c):
 return [[str(p[i]) for i in range(e)] for p in c.v]
def saveP(p):
 return [[int(i),int(j),saveC(c)] for (i,j),c in sorted(p.v.items())]
exact_obj={
 "constantFieldPhiAscending":[str(phi[i]) for i in range(e+1)],
 "trueQQRhoGcdAscending":[[str(c[i]) for i in range(e)] for c in g],
 "rhoDegree":n,"originalRhoUnitComponentsRemoved":removed,
 "originalTQuotientAscending":[[str(c[i]) for i in range(e)] for c in qT],
 "removedOnlyOriginalSUnitFactors":[[[str(c[i]) for i in range(e)] for c in fac] for fac in removedT],
 "originalMonicN1InXAndZ":saveP(n1monic),
 "originalRows":[{"label":label,"coefficients":saveP(p)} for label,p in reduced_rows]}
bb=json.dumps(exact_obj,separators=(",",":")).encode()
packed=zlib.compress(bb,9);assert zlib.decompress(packed)==bb
say("complete_new_original_same_constant_algebra_rows",
    actualQQDimension=e*n*tdegree*2,originalLabels=[label for label,p in reduced_rows],
    originalRowsHaveFullQQDivisionProducts=True,
    allNamedInverses=named_inverses,
    encoding="base64+zlib+json",uncompressedBytes=len(bb),
    payloadSha256=hashlib.sha256(bb).hexdigest(),
    data=base64.b64encode(packed).decode())
# The following matrix is a fixed QQ original-ideal matrix reduced
# at an actual integral prime. Multiplication by all basis monomials
# is in the same monic, free finite algebra. No norm is inverted.
allqq=[phi]+g
for p in [qTformal,n1monic]+[p for label,p in reduced_rows]:
 for c in p.v.values():allqq.extend(c.v)
prime=None
for cand in [1009,1013,1019,1021,1031,1033,1039,1049]:
 assert all(cand%d for d in range(2,int(cand**0.5)+1))
 if all(int(p[i].denominator)%cand for p in allqq for i in range(p.degree()+1)):
  prime=cand;break
assert prime is not None
dimension=e*n*tdegree*2
def modq(c):
 d=int(c.denominator)%prime;assert d
 iv=pow(d,-1,prime);assert d*iv%prime==1
 return int(c.numerator)%prime*iv%prime
def vector(p):
 p=P(p);ans=[0]*dimension
 for (i,j),c in p.v.items():
  assert 0<=i<tdegree and 0<=j<2
  for r,cc in enumerate(c.v):
   assert r<n
   for l in range(e):
    ans[((j*tdegree+i)*n+r)*e+l]=modq(cc[l])
 return ans
basis=[]
for j in range(2):
 for i in range(tdegree):
  for r in range(n):
   for l in range(e):
    coefficient=C([kzero]*r+[fmpq_poly([0]*l+[1])])
    basis.append(P.from_terms({(i,j):coefficient}))
assert len(basis)==dimension
operators=[];operator_hashes=[]
for label,op in [("lambda",P(lam)),("rho",P(rho)),("T",x),("z",z)]:
 table=[vector(reduce_formal(b*op)) for b in basis]
 sparse=[[(j,c) for j,c in enumerate(row) if c] for row in table]
 operators.append(sparse)
 operator_hashes.append(dict(label=label,sha256=hashlib.sha256(str(table).encode()).hexdigest()))
 say("new_actual_original_constant_algebra_multiplication",
     operator=label,dimension=dimension,prime=prime,
     allQQDivisionProductsBeforeReductionReturned=True)
def act(row,op):
 ans=[0]*dimension
 for i,c in enumerate(row):
  if c:
   for j,d in op[i]:ans[j]=(ans[j]+c*d)%prime
 return ans
Ml,Mr,Mx,Mz=operators
rows=[];tags=[]
for label,p in reduced_rows:
 initial=vector(p);rz=initial
 for j in range(2):
  rx=rz
  for i in range(tdegree):
   rr=rx
   for r in range(n):
    cur=rr
    for l in range(e):
     rows.append(cur);tags.append([label,l,r,i,j])
     if l+1<e:cur=act(cur,Ml)
    if r+1<n:rr=act(rr,Mr)
   if i+1<tdegree:rx=act(rx,Mx)
  if j+1<2:rz=act(rz,Mz)
assert len(rows)==4*dimension
basis_rows={};chosen=[]
for index,row in enumerate(rows):
 a=list(row)
 for pivot,b in sorted(basis_rows.items()):
  c=a[pivot]
  if c:
   for j in range(pivot,dimension):a[j]=(a[j]-c*b[j])%prime
 pivot=next((j for j,c in enumerate(a) if c),None)
 if pivot is None:continue
 iv=pow(a[pivot],-1,prime);assert a[pivot]*iv%prime==1
 a=[c*iv%prime for c in a]
 basis_rows[pivot]=a;chosen.append(index)
 if len(basis_rows)==dimension:break
full=len(basis_rows)==dimension;certificate=None
if full:
 B=[list(rows[i]) for i in chosen]
 aug=[row+[int(i==j) for j in range(dimension)] for i,row in enumerate(B)]
 for c in range(dimension):
  pivot=next(r for r in range(c,dimension) if aug[r][c])
  aug[c],aug[pivot]=aug[pivot],aug[c]
  iv=pow(aug[c][c],-1,prime);assert aug[c][c]*iv%prime==1
  aug[c]=[v*iv%prime for v in aug[c]]
  for r in range(dimension):
   if r==c:continue
   z0=aug[r][c]
   if z0:aug[r]=[(v-z0*w)%prime for v,w in zip(aug[r],aug[c])]
 assert all(aug[i][j]==int(i==j) for i in range(dimension) for j in range(dimension))
 inverse=[r[dimension:] for r in aug];cols=list(zip(*inverse))
 for i,row in enumerate(B):
  for j,col in enumerate(cols):
   assert sum(a*b for a,b in zip(row,col))%prime==int(i==j)
 certificate=dict(selectedActualOriginalRows=[tags[i] for i in chosen],
     matrixSha256=hashlib.sha256(str(B).encode()).hexdigest(),
     inverseSha256=hashlib.sha256(str(inverse).encode()).hexdigest(),
     completeSelectedSquareTimesInverseReturned=True)
say("complete_new_original_psiS_moment_fiber_reduced_T_by_two_return",
    actualQQConstantFieldDegree=e,actualQQRhoDegree=n,
    dimension=dimension,originalRows=len(rows),prime=prime,
    actualRank=len(basis_rows),certificate=certificate,
    operatorHashes=operator_hashes,checks=checks,
    exactQQRhoGcdAndAllNamedConstantInverseProductsReturned=True,
    monicTRelationFromOriginalF6AndPhysicalSUnit=True,
    actualOriginalTDegree=tdegree,
    monicZSquareIsCompleteOriginalN1=True,
    fullOriginalMeansAndNVInSameAlgebra=True,
    fixedQQIdealMatrixIntegralAtActualPrime=True,
    wholeQQMomentImageFiberExcluded=full,
    allFourLambdaEmbeddingsAndAllRhoRootsCovered=True,
    noBareModularEmptinessInference=True,
    noOriginalResultantOrFormerLocalKernelRecomputed=True,
    noGeometricDOrUnclassifiedNormInverse=True,
    ordinaryISPClaim=False)

# Only a NEW complete entire quartic-fiber value exclusion licenses
# deletion of the corresponding true QQ resultant factor. The
# original same-source kernel above proves the exact QQ lower bound.
if full:
 def fixed_mod1009(p):
  aa=[]
  for i in range(p.degree()+1):
   c=p[i];dd=int(c.denominator)%1009;assert dd
   iv=pow(dd,-1,1009);assert dd*iv%1009==1
   aa.append(int(c.numerator)%1009*iv%1009)
  return nmod_poly(aa,1009)
 def read_complete_mod(rec,expected_sha,expected_degree):
  raw=zlib.decompress(base64.b64decode(rec["fullCoefficientsData"]))
  assert hashlib.sha256(raw).hexdigest()==rec["fullCoefficientsPayloadSha256"]
  pp=nmod_poly(json.loads(raw),1009)
  assert pp.degree()==expected_degree
  assert hashlib.sha256(str(pp).encode()).hexdigest()==expected_sha
  return pp
 oldR=read_complete_mod(inputG["full_fixed_mod1009_resultant"],
  "f4505a726a6c2691ac52b92ec424160f7cc748d6a9b17751ce8b2f9f3f0eaa85",2033)
 oldS=read_complete_mod(inputH["fixed_mod_resultant"],
  "060c2f63b871fec6e649ce3bdfbf29612df9402b07c3c4d381245f639edb8e12",2050)
 ph1=fmpq_poly([fmpq(-1,2),1])
 ph6=fmpq_poly([fmpq(5,64),fmpq(39,80),fmpq(63,80),
                 fmpq(-7,10),fmpq(-9,4),fmpq(3,5),1])
 phD=fmpq_poly([fmpq(1,32),fmpq(-3,16),fmpq(27,32),fmpq(-17,8),
                  fmpq(27,8),-3,1])
 total=ph1**10*ph6**2*phD**3*phi**common_degree
 newR,remainder=divmod(oldR,fixed_mod1009(total))
 assert not remainder and newR*fixed_mod1009(total)==oldR
 assert newR.degree()==1993-e*common_degree
 gcdR,aa,bb=newR.xgcd(oldS)
 assert aa*newR+bb*oldS==gcdR
 temp=oldR;mod_multiplicity=0
 while True:
  q,remainder=divmod(temp,fixed_mod1009(phi))
  if remainder:break
  assert q*fixed_mod1009(phi)==temp
  mod_multiplicity+=1;temp=q
 assert common_degree<=mod_multiplicity
 say("complete_new_actual_full_quotient_original_Gauss_return",
     exactQQEntireSMomentImageFiberExclusionPaidByThisRun=True,
     trueQQMultiplicityLowerBound=common_degree,
     actualFullOriginalRModPhiMultiplicity=mod_multiplicity,
     exactQQMultiplicityPaid=(common_degree==mod_multiplicity),
     originalRQQDegreeAnd1009LeadingUnitPreviouslyProved=True,
     totalTrueQQFactorDegree=int(total.degree()),
     actualFullRQuotientDegree=int(newR.degree()),
     actualFullSDegree=int(oldS.degree()),
     actualNewFullGcdDegree=int(gcdR.degree()),
     actualNewFullGcdCoefficients=[int(gcdR[i]) for i in range(gcdR.degree()+1)],
     bezoutDegrees=[int(aa.degree()),int(bb.degree())],
     completeNewQuotientAndBezoutProductsReturned=True,
     strictDifferentOrderedBasePointBound=int(gcdR.degree()),
     noVerticalFibersByPreviouslyProvedF26Irreducibility=True,
     BCSwappedChartNotMergedIntoSameBound=True,
     wholeExceptionalBranchExcluded=gcdR.degree()==0,
     ordinaryISPClaim=False)
