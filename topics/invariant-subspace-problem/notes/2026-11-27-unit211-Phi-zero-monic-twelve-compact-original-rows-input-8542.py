#!/usr/bin/env python3
"""NEW Phi=0 original input: keep z=Q*t and use monic original N1 first.
The true original z^2 coefficient is -4*(bc)^2*ell*Q*(u-1).
The actual algebra has monic T^6 then monic z^2, rank 12 over paid
weight coefficients.  No D, Sn*Z, Pf norm, or original two-line
determinant is inverted.  Original NV remains an additional row.
Use the already-paid compact original scalar identities, not a replay
of the failed general rho-two substitution or full Gram expansion.
First return the four original rows and their exact quadratic heads.
120 seconds / 1 GiB, one monic-six helper only.
"""
import os,sys,json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
start=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start)
 print(json.dumps(kw),flush=True)
helper_path=Path(os.environ.get("ISP_MONIC_SIX_HELPER",
 str(Path(__file__).with_name("2026-11-27-unit211-monic-six-explicit-geometric-localization-helper-8542.py"))))
helper_text=helper_path.read_text()
assert hashlib.sha256(helper_text.encode()).hexdigest()=="5e162fa3adc0737bb152de5635e6956ca03267d055a6b33cea93c957628c96d6"
exec(compile(helper_text,str(helper_path),"exec"),globals())
ctx=fmpq_mpoly_ctx.get(('u','Q','lam','T'),'lex')
up,Qp,Lp,Tp=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
def poly(x):return x if hasattr(x,'to_dict') else ctx.constant(x)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=oneP if d is None else poly(d);assert d
  if not n:self.n=zeroP;self.d=oneP;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,o):
  o=R(o)
  if not self:return o
  if not o:return self
  g=self.d.gcd(o.d);a=self.d/g;b=o.d/g
  return R(self.n*b+o.n*a,a*o.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):
  o=R(o)
  if not self or not o:return R()
  g=self.n.gcd(o.d);h=o.n.gcd(self.d)
  return R((self.n/g)*(o.n/h),(self.d/h)*(o.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,o):o=R(o);assert o;return self*R(o.d,o.n,False)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):
  return R(self.d**(-n),self.n**(-n),False) if n<0 else R(self.n**n,self.d**n,False)
 def __eq__(self,o):
  o=R(o)
  if self.n==o.n and self.d==o.d:return True
  return self.n*o.d==o.n*self.d
u,Q,lam,Tr=map(R,(up,Qp,Lp,Tp))
ell=1-2*(u-1)*(u-2)/Q
delta=1-Q;m=u-ell;V2=2*u-ell*Q;T0=V2-2*u*u
J=2*u*(1-u)+ell*Q;Phi=T0+4*u-4+Q
P02=(2-3*u)*V2-Q*u+2*u**3;Pf=T0*(J-Q)
M=ell*V2-u*u;bc=M/(4*delta)
assert Phi==0
assert T0==-Q-4*(u-1) and J-Q==-4*(u-1)**2
assert P02==2*(u-1)*ell*Q
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1
Dr=ell*A2-Tr*Tr
snr=ell*B3-A2*Tr;znr=Tr*B3-A2*A2
Kr=ell*ell*B3-3*ell*Tr*A2+2*Tr**3
Zr=u*snr-2*Tr*Dr;Snr=snr+(3-2*lam)*Dr
F6r=M*Kr*Kr-4*m*m*Dr**3
G=lam*P02-(1-u)*T0;wr=lam-1-Tr
Pcr=Q*P02*(ell+Tr)-G*T0
NF4r=4*m*((3-4*lam)*Q*Dr*Dr-J*znr*Dr)+2*Snr*(-2*u*Q*Kr+J*Zr)
NC4r=(4*m*G*znr*Dr-2*G*Snr*Zr-Q*T0*Snr*Kr
      +4*m*Q*wr*u*(3-2*lam)*Dr*Dr
      +2*m*Q*wr*u*snr*Dr-2*Q*wr*(u-ell*Q)*Kr*Dr)
# These are exact polynomial identities before taking the moment quotient.
assert Kr+2*Tr*Dr==ell*snr
assert ell*Zr==2*m*Tr*Dr+u*Kr
assert m*snr-Zr+Kr==0
raw_values=dict(D=Dr,sn=snr,zn=znr,K=Kr,Z=Zr,Sn=Snr,Pc=Pcr,
                NF4=NF4r,NC4=NC4r)
def profile(p):
 return dict(degrees=list(map(int,p.degrees())),terms=len(p.to_dict()),
             sha256=hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest())
say("original_Phi0_exact_weight_and_compact_numerator_input",
    variables=["u","Q","lambda","T"],PhiExactlyZero=True,
    originalMomentRelation=profile(F6r.n),
    originalNumerators={k:profile(v.n) for k,v in raw_values.items()},
    originalUnits=["u","u-1","Q","1-Q","ell","ell-u","M","P02",
                   "T0","J-Q","u+Q-1","lambda","D","S","zeta"],
    ordinaryISPClaim=False)
unit_atoms=[("u",u.n),("u-1",(u-1).n),("Q",Q.n),("1-Q",delta.n),
            ("ell",ell.n),("ell-u",m.n),("M",M.n),("P02",P02.n),
            ("T0",T0.n),("J-Q",(J-Q).n),("u+Q-1",(u+Q-1).n),
            ("lambda",lam.n)]
paid_cache=set();coefficient_cache=set()
def strip_paid(pp):
 if not pp:raise AssertionError("zero cannot be a paid weight unit")
 key=str(pp)
 if key in paid_cache:return
 p=pp
 for name,atom in unit_atoms:
  while p:
   g=p.gcd(atom)
   if g.total_degree()==0:break
   q=p/g;assert q*g==p;p=q
 assert p.total_degree()==0,("unpaid weight factor",str(p),str(pp))
 paid_cache.add(key)
def noT(pp):return all(int(e[3])==0 for e in pp.to_dict())
def coefficient_audit(rr):
 rr=R(rr);assert noT(rr.n) and noT(rr.d)
 key=str(rr.d)
 if key not in coefficient_cache:
  strip_paid(rr.d);coefficient_cache.add(key)
def parameter_unit_audit(name,rr):
 assert name.startswith("paid_weight:") or name=="F6_leading"
 rr=R(rr);assert noT(rr.n) and noT(rr.d)
 strip_paid(rr.n);strip_paid(rr.d)
cooperate_parameter_ring(R)
alg=make_six_from_mpoly(R,ctx,F6r.n,3,coefficient_audit,
                       parameter_unit_audit,"F6_leading")
K6=alg.K6;T=alg.T
# The true monic leading coefficient is the old F6 leading times its
# already-paid scalar denominator; verify it in the original coefficient ring.
assert alg.original_leading_coefficient==4*ell*ell*delta*R(F6r.d)
def kin(rr):
 rr=R(rr);assert noT(rr.d)
 inv=alg.inverse_parameter("paid_weight:input_denominator",R(rr.d))
 return alg.from_mpoly(rr.n)*inv
kv={k:kin(v) for k,v in raw_values.items()}
D,sn,zn,K,Z,Sn,Pc,NF4,NC4=(kv[k] for k in
                            ("D","sn","zn","K","Z","Sn","Pc","NF4","NC4"))
assert D==K6(ell*A2)-T*T
assert alg.from_mpoly(F6r.n)==0

# Ordinary polynomials in the NEW variable z over the paid monic T algebra.
class ZPoly:
 _isp_quotient_level=2
 __slots__=("coefficients",)
 def __init__(self,value=0):
  if isinstance(value,ZPoly):self.coefficients=value.coefficients;return
  vals=[K6(x) for x in value] if isinstance(value,(tuple,list)) else [K6(value)]
  while len(vals)>1 and vals[-1]==0:vals.pop()
  self.coefficients=tuple(vals)
 def __bool__(self):return any(v!=0 for v in self.coefficients)
 def __add__(self,o):
  o=ZPoly(o);n=max(len(self.coefficients),len(o.coefficients))
  return ZPoly([(self.coefficients[i] if i<len(self.coefficients) else K6(0))+
                (o.coefficients[i] if i<len(o.coefficients) else K6(0))
               for i in range(n)])
 __radd__=__add__
 def __neg__(self):return ZPoly([-x for x in self.coefficients])
 def __sub__(self,o):return self+-ZPoly(o)
 def __rsub__(self,o):return ZPoly(o)+-self
 def __mul__(self,o):
  o=ZPoly(o);v=[K6(0)]*(len(self.coefficients)+len(o.coefficients)-1)
  for i,a0 in enumerate(self.coefficients):
   for j,b0 in enumerate(o.coefficients):v[i+j]=v[i+j]+a0*b0
  return ZPoly(v)
 __rmul__=__mul__
 def __truediv__(self,o):
  assert isinstance(o,int) and o
  return ZPoly([x/o for x in self.coefficients])
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  ans=ZPoly(1);cur=self
  while n:
   if n&1:ans=ans*cur
   n>>=1
   if n:cur=cur*cur
  return ans
 def __eq__(self,o):
  o=ZPoly(o)
  return (self-o).coefficients==(K6(0),)
 def coef(self,j):
  return self.coefficients[j] if j<len(self.coefficients) else K6(0)
z=ZPoly([0,1])
fnum=-Pc*alg.inverse_parameter("paid_weight:Pf",Pf)
assert Pf*fnum+Pc==0
assert all(fnum.coefficients[j]==0 for j in range(2,6))
ff=ZPoly(fnum);aa=1-ell
vn=J*ff-G+bc*z
wstar=ZPoly(T0)+4*u*ff
nn=Q*wstar-2*vn
ww=ZPoly(K6(lam-1)-T)
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
head=-4*bc*bc*ell*Q*(u-1)
assert len(N1.coefficients)<=3 and N1.coef(2)==K6(head)
head_inv=alg.inverse_parameter("paid_weight:original_N1_z2",head)
za=N1.coef(1)*head_inv;zb=N1.coef(0)*head_inv
assert all(za.coefficients[j]==0 for j in range(2,6))
assert all(zb.coefficients[j]==0 for j in range(3,6))
monic=ZPoly([zb,za,1]);assert N1==head*monic
say("new_actual_original_N1_monic_z_quadratic",
 quadraticHead="-4*(bc)^2*ell*Q*(u-1)",
 degreeTOfLinearZCoefficientAtMost=1,degreeTOfConstantCoefficientAtMost=2,
 originalCoefficientIdentityReturned=True,
 onlyPaidWeightInverses=True,noDOrSnZInverse=True,
 sourceCompactIdentitySha256="9ab0270fe53a0a6f169755f92f731e6cf636f1d9b7a9e12364ef487a01cdea6e",
 statistics=dict(alg.statistics))
class K12:
 _isp_quotient_level=2
 __slots__=("coefficients",)
 def __init__(self,value=0):
  if isinstance(value,K12):self.coefficients=value.coefficients;return
  if isinstance(value,(tuple,list)):
   assert len(value)<=2
   vals=[K6(x) for x in value]+[K6(0)]*(2-len(value))
  else:vals=[K6(value),K6(0)]
  self.coefficients=tuple(vals)
 def __add__(self,o):
  o=K12(o);return K12([a+b for a,b in zip(self.coefficients,o.coefficients)])
 __radd__=__add__
 def __neg__(self):return K12([-x for x in self.coefficients])
 def __sub__(self,o):return self+-K12(o)
 def __rsub__(self,o):return K12(o)+-self
 def __mul__(self,o):
  o=K12(o);a0,a1=self.coefficients;b0,b1=o.coefficients
  c0,c1,c2=a0*b0,a0*b1+a1*b0,a1*b1
  out0,out1=c0-c2*zb,c1-c2*za
  assert c0-out0-c2*zb==0 and c1-out1-c2*za==0
  stat12["multiplications"]+=1;stat12["coefficient_identity_checks"]+=3
  return K12([out0,out1])
 __rmul__=__mul__
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  ans=K12(1);cur=self
  while n:
   if n&1:ans=ans*cur
   n>>=1
   if n:cur=cur*cur
  return ans
 def __eq__(self,o):
  o=K12(o);return all(a==b for a,b in zip(self.coefficients,o.coefficients))
stat12=dict(multiplications=0,coefficient_identity_checks=0)
Z12=K12([0,1])
def from_zpoly(v):
 v=ZPoly(v);ans=K12(0)
 for cc in reversed(v.coefficients):ans=ans*Z12+K12(cc)
 return ans
assert from_zpoly(N1)==0
assert Z12*Z12+K12(za)*Z12+K12(zb)==0
relations={"R2_over_2rho":from_zpoly(Rbar),
           "W4":from_zpoly(W4),"O8_over_rho":from_zpoly(Obar),
           "actual_NV_line":K12(NF4*fnum+NC4)+K12(2*bc*Sn*Z)*Z12}
def clear_twelve(elt):
 cc=[rr for part in K12(elt).coefficients for rr in part.coefficients]
 den=oneP
 for rr in cc:
  coefficient_audit(rr);gg=den.gcd(rr.d);den=(den/gg)*rr.d
 strip_paid(den)
 nums=[]
 for rr in cc:
  q0=den/rr.d;assert q0*rr.d==den;nums.append(rr.n*q0)
 assert all(noT(pp) for pp in nums)
 # The complete coefficient identity, not a sampled equality.
 assert all(R(pp)==rr*R(den) for pp,rr in zip(nums,cc))
 return nums,den
import base64,zlib
def save_exact_row(name,nums,den):
 payload=json.dumps({"variables":["u","Q","lambda"],
  "basis":[["T",i,"z",j] for j in range(2) for i in range(6)],
  "coefficientNumerators":[[[list(map(int,e[:3])),str(c)]
      for e,c in sorted(pp.to_dict().items())] for pp in nums],
  "commonPaidDenominator":[[list(map(int,e[:3])),str(c)]
      for e,c in sorted(den.to_dict().items())]},
  separators=(",",":")).encode()
 packed=zlib.compress(payload,9);back=json.loads(zlib.decompress(packed))
 assert len(back["coefficientNumerators"])==12
 for seq,pp in zip(back["coefficientNumerators"],nums):
  assert ctx.from_dict({tuple(e)+(0,):fmpq(c) for e,c in seq})==pp
 assert ctx.from_dict({tuple(e)+(0,):fmpq(c) for e,c in back["commonPaidDenominator"]})==den
 say("new_exact_recoverable_original_twelve_row",name=name,
  numeratorProfiles=[profile(pp) for pp in nums],denominator=profile(den),
  encoding="base64+zlib+json",payloadSha256=hashlib.sha256(payload).hexdigest(),
  uncompressedBytes=len(payload),compressedBytes=len(packed),
  data=base64.b64encode(packed).decode(),
  fullOriginalTwelveCoefficientsReturned=True,noGeometricInversions=True)
for name,elt in relations.items():
 nums,den=clear_twelve(elt)
 save_exact_row(name,nums,den)
say("complete_new_Phi0_original_four_rows_in_monic_twelve_environment",
 originalRows=list(relations),freeEnvironmentRank=12,
 sameOriginalTAndZ=True,
 N1UsedAsMonicRelationNotDropped=True,
 NVKeptAsExtraRowNotSolvedBySnZ=True,
 noDOrSnZInverse=True,noNormInverse=True,
 statisticsT6=dict(alg.statistics),statisticsZ2=dict(stat12),
 originalOtherIndividualNPNotClaimed=True,
 noFullTwelveRowIdealClosureClaim=True,
 wholePhiFaceExcluded=False,ordinaryISPClaim=False)
# NEW small weight-only quadratic head input.  It may permit fewer than
# twelve generators, but no head or its norm is inverted in this source.
quad={"R2_over_2rho":Rbar,"W4":W4,"O8_over_rho":Obar,"N1":N1}
heads={}
for name,qq in quad.items():
 assert len(qq.coefficients)<=3
 for j,cc in enumerate(qq.coefficients):
  assert all(cc.coefficients[i]==0 for i in range(6) if i+j>2)
 hh=[qq.coef(0).coefficients[2],qq.coef(1).coefficients[1],qq.coef(2).coefficients[0]]
 assert all(all(int(e[2])==0 and int(e[3])==0 for e in x.n.to_dict())
            and all(int(e[2])==0 and int(e[3])==0 for e in x.d.to_dict()) for x in hh)
 heads[name]=hh
def d3(a):
 return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
        -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
        +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
import itertools
for labels in itertools.combinations(list(heads),3):
 val=d3([heads[x] for x in labels])
 coefficient_audit(val)
 if not val:
  say("new_original_quadratic_head_minor_zero",rows=list(labels));continue
 core=val.n;removed=[]
 for name,atom in unit_atoms:
  count=0
  while core:
   gg=core.gcd(atom)
   if gg.total_degree()==0:break
   q0=core/gg;assert q0*gg==core;core=q0;count+=1
  if count:removed.append([name,count])
 scale=core.coefficient(0);before=core;core=core/scale;assert core*scale==before
 say("new_actual_original_quadratic_head_minor",
  rows=list(labels),numerator=profile(val.n),paidDenominator=profile(val.d),
  residualAfterPaidUnitFactors=profile(core),
  residualPolynomial=str(core),paidGcdSources=removed,
  thisHeadIsPaidUnit=(core.total_degree()==0),
  noTemporaryHeadInverseUsed=True)
say("complete_new_actual_Phi0_quadratic_head_input",
 originalHeadMonomials=["T^2","T*z","z^2"],
 weightVariablesOnly=["u","Q"],unknownHeadZeroFibersRetained=True,
 wholePhiFaceExcluded=False,ordinaryISPClaim=False)
