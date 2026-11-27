#!/usr/bin/env python3
"""NEW general Phi=0 value graph: a TWO dimensional rho algebra.
The previously closed zn=0 branch pays x*y, x=h-1,y=k-1.
The rho-quadratic leading A=ell-1-2(b-c)^2 is explicitly nonzero
on this open chart; its complete zero branches have separate sources.
No algebraic norm is inverted.  Pf and NT are cleared in one original
Gram scale.  Three original mean rows, then N1, keep the SAME rho.
Only new two-row unit identities are formed; no previous cofactor replay.
120 seconds / 1 GiB.  Every new core is recoverably saved.
"""
import os,sys,json,time,hashlib,signal,resource,zlib,base64
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
ctx=fmpq_mpoly_ctx.get(("lam","x","y"),"lex")
Lp,xp,yp=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
def poly(x):return x if hasattr(x,"to_dict") else ctx.constant(x)
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

lam,x,y=map(R,(Lp,xp,yp))
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1
b=(B3-A2*y)/(x*x*(x-y));c=(A2*x-B3)/(y*y*(x-y))
ell=b+c;diff=b-c;a=1-ell;bc=b*c
T=b*x+c*y;S=x+y+3-2*lam;ww=lam-1-T
Ahead=ell-1-2*diff*diff
Bhead=2*diff*(3-2*ell)
Chead=-(ell-1)*(2*ell-3)
assert b*x*x+c*y*y==A2
assert b*x*x*x+c*y*y*y==B3
assert ell*A2-T*T==bc*(x-y)**2
unit_atoms=[("x",x.n),("y",y.n),("x-y",(x-y).n),
 ("explicit_open_rho_head",Ahead.n),("b",b.n),("c",c.n),
 ("ell",ell.n),("b-c",diff.n),("S",S.n),("lambda",lam.n)]
paid_cache=set()
def strip_unit_product(pp):
 assert pp
 key=str(pp)
 if key in paid_cache:return
 rr=pp
 for name,atom in unit_atoms:
  while rr:
   gg=rr.gcd(atom)
   if gg.total_degree()==0:break
   nn=rr/gg;assert nn*gg==rr;rr=nn
 assert rr.total_degree()==0,("unpaid base denominator",str(rr))
 paid_cache.add(key)
def coefficient_audit(rr):
 rr=R(rr);strip_unit_product(rr.d)
alpha=Bhead/Ahead;beta=Chead/Ahead
coefficient_audit(alpha);coefficient_audit(beta)
stats=dict(multiplications=0,original_difference_coefficients=0)
cooperate_parameter_ring(R)
class K2:
 _isp_quotient_level=1
 __slots__=("coefficients",)
 def __init__(self,value=0):
  if isinstance(value,K2):self.coefficients=value.coefficients;return
  if isinstance(value,(list,tuple)):
   assert len(value)<=2
   cc=[R(z) for z in value]+[R(0)]*(2-len(value))
  else:cc=[R(value),R(0)]
  for z in cc:coefficient_audit(z)
  self.coefficients=tuple(cc)
 @classmethod
 def internal(cls,c0,c1):
  obj=object.__new__(cls);obj.coefficients=(c0,c1);return obj
 def __bool__(self):return any(z!=0 for z in self.coefficients)
 def __add__(self,o):
  if getattr(o,"_isp_quotient_level",0)>1:return NotImplemented
  o=K2(o);return K2.internal(*(a+b for a,b in zip(self.coefficients,o.coefficients)))
 __radd__=__add__
 def __neg__(self):return K2.internal(*(-a for a in self.coefficients))
 def __sub__(self,o):return self+-K2(o)
 def __rsub__(self,o):return K2(o)+-self
 def __mul__(self,o):
  if getattr(o,"_isp_quotient_level",0)>1:return NotImplemented
  o=K2(o);a,b=self.coefficients;c,d=o.coefficients
  raw0,raw1,raw2=a*c,a*d+b*c,b*d
  out0,out1=raw0-raw2*beta,raw1-raw2*alpha
  assert raw0-out0-raw2*beta==0
  assert raw1-out1-raw2*alpha==0
  assert raw2-raw2==0
  stats["multiplications"]+=1;stats["original_difference_coefficients"]+=3
  return K2.internal(out0,out1)
 __rmul__=__mul__
 def __truediv__(self,o):
  if isinstance(o,int) and o!=0:
   return K2.internal(*(z/o for z in self.coefficients))
  raise TypeError("Only explicit base original-unit inverses are allowed")
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  ans,cur=K2(1),self
  while n:
   if n&1:ans=ans*cur
   n>>=1
   if n:cur=cur*cur
  return ans
 def __eq__(self,o):
  if getattr(o,"_isp_quotient_level",0)>1:return NotImplemented
  o=K2(o);return all(a==b for a,b in zip(self.coefficients,o.coefficients))
rho=K2([0,1]);p=1+rho;q=1-rho;Q=1-rho*rho
u=K2(ell)+K2(diff)*rho
V2=2*u-ell*Q;T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
Phi=T0+4*u-4+Q
assert Phi==0
assert Ahead*rho*rho+Bhead*rho+Chead==0
assert T0==-Q-4*(u-1) and J-Q==-4*(u-1)**2
P02=(2-3*u)*V2-Q*u+2*u**3
assert P02==2*(u-1)*ell*Q
G=lam*P02+(u-1)*T0
Pf=T0*(J-Q)
Pc=Q*P02*(ell+T)-G*T0
Pf1=-4*(u-1)*T0
Pc1=2*ell*Q*Q*(ell+T)-(2*lam*ell*Q+T0)*T0
assert Pf==(u-1)*Pf1 and Pc==(u-1)*Pc1
Lnum=p*y-q*x
NF2r=2*rho*(3-4*lam)*Q+S*(2*u*Q*(x-y)+Lnum*J)
NT2r=bc*Q*S*Lnum
NC2r=(-G*S*Lnum+S*Q*T0*(x-y)/2+
 Q*ww*(2*rho*u*(3-2*lam+(x+y)/2)+(u-ell*Q)*(x-y)))
f0=-Pc1*NT2r
t0=NF2r*Pc1-NC2r*Pf1
H0=Pf1*NT2r
assert Pf1*f0+Pc1*H0==0
assert NF2r*f0+NT2r*t0+NC2r*H0==0
def profile(pp):
 return dict(degrees=list(map(int,pp.degrees())),terms=len(pp.to_dict()),
             totalDegree=int(pp.total_degree()),
             sha256=hashlib.sha256(str(sorted(pp.to_dict().items())).encode()).hexdigest())
say("new_general_Phi0_rho_two_original_line_input",
 variables=["lambda","x","y"],rhoAlgebraDimension=2,
 headCondition="A=ell-1-2*(b-c)^2 != 0",
 headZeroBranchesRetainedSeparately=True,
 originalMomentsAndBothClearedLines=True,
 clearedSecondLineFactor="2*rho",initialGramDenominator="Pf1*NT2r",
 parameterizedWeightsPreviouslyKnown=True,
 newInputIsPhiMonicRhoQuadratic=True,
 noA2OrB3Inversion=True,noNormInverse=True,statistics=dict(stats))
# Remove only a common scalar content of the SAME actual nonzero H0.
# If this scalar vanished at an original point, H0 would vanish there.
content=None
for kk in (H0,f0,t0):
 for rr in kk.coefficients:
  coefficient_audit(rr)
  if rr.n:content=rr.n if content is None else content.gcd(rr.n)
assert content
if content.total_degree()>0:
 unit_atoms.append(("actual_H0_common_content",content))
 original=[H0,f0,t0];reduced=[]
 for kk in original:
  cc=[rr/R(content) for rr in kk.coefficients]
  for rr in cc:coefficient_audit(rr)
  nn=K2(cc);assert K2(R(content))*nn==kk;reduced.append(nn)
 H0,f0,t0=reduced
say("new_same_H0_actual_content_return",content=profile(content),
 contentUnitPaidByOriginalH0=True,statistics=dict(stats))
# H=2bcQrho H0 clears ALL p,q,rho denominators in W1/W2 restoration.
W1=H0*T0/2+2*u*f0
W2=H0*(u*T0+lam*P02)+(V2+2*u*u)*f0-bc*Q*t0
scale=2*bc*Q*rho
H=scale*H0;Fnum=scale*f0;Tnum=scale*t0
Xnum=c*q*(W2-q*W1)
Ynum=b*p*(p*W1-W2)
Rnum=Xnum-H*a*p-c*Tnum
Snum=Ynum-H*a*q-b*Tnum
Anum=2*Fnum-2*b*Xnum-2*c*Ynum+2*bc*Tnum
gram=[[K2(),K2(),H*p,H*q],
      [K2(),Anum,Rnum,Snum],
      [H*p,Rnum,K2(),Tnum],
      [H*q,Snum,Tnum,K2()]]
one=[K2(1),K2(),K2(1),K2(1)]
def va(v,z):return [aa+bb for aa,bb in zip(v,z)]
def vs(aa,v):return [aa*bb for bb in v]
def vm(v,z):return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return a*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tau(vm(row,v)) for row in gram]
dvec=DK(one);F2=tau(dvec)
assert F2==2*Fnum
Kd=DK(dvec)
def mean(j):
 ee=2*tau(vm(gram[0],gram[1])) if j==1 else tau(vm(gram[j],gram[j]))
 return ee-2*Kd[j]-2*vm(dvec,dvec)[j]+2*F2*dvec[j]
assert mean(0)==0
rows={}
def clear_original_row(name,kk):
 rr=list(K2(kk).coefficients);den=oneP
 for cc in rr:
  coefficient_audit(cc)
  gg=den.gcd(cc.d);den=(den/gg)*cc.d
 strip_unit_product(den)
 nums=[]
 for cc in rr:
  qq=den/cc.d;assert qq*cc.d==den;nums.append(cc.n*qq)
 removed=[]
 for label,atom in unit_atoms:
  count=0
  while any(nums):
   gg=nums[0].gcd(nums[1]).gcd(atom)
   if gg.total_degree()==0:break
   new=[pp/gg for pp in nums]
   assert all(nn*gg==pp for nn,pp in zip(new,nums))
   nums=new;count+=1
  if count:removed.append([label,count])
 if any(nums):
  scalar=next(pp for pp in nums if pp).coefficient(0)
  before=nums;nums=[pp/scalar for pp in nums]
  assert all(qq*scalar==pp for qq,pp in zip(nums,before))
 out=K2([R(pp) for pp in nums])
 say("new_general_Phi0_same_rho_original_row",name=name,
     coefficients=[profile(pp) for pp in nums],
     paidScalarDenominator=profile(den),paidGcdSources=removed,
     notSeparateCoefficientZeroEquations=True,
     originalGramScale="H=2bcQrho*H0",statistics=dict(stats))
 return out
for name,j in [("E1",1),("EB",2),("EC",3)]:
 rows[name]=clear_original_row(name,mean(j))
H2=H*H
def saved_polynomial(pp,label):
 payload=json.dumps({"variables":["lambda","x","y"],
  "terms":[[list(map(int,ex)),str(cc)] for ex,cc in sorted(pp.to_dict().items())]},
  separators=(",",":")).encode()
 compressed=zlib.compress(payload,9)
 back=json.loads(zlib.decompress(compressed))
 rebuilt=ctx.from_dict({tuple(ex):fmpq(cc) for ex,cc in back["terms"]})
 assert rebuilt==pp
 say("new_exact_recoverable_polynomial",label=label,profile=profile(pp),
  encoding="base64+zlib+json",uncompressedBytes=len(payload),compressedBytes=len(compressed),
  payloadSha256=hashlib.sha256(payload).hexdigest(),
  data=base64.b64encode(compressed).decode(),
  completeReconstructionMultipliedBack=True)
def actual_unit_pair(left,right,label):
 aa,bb=rows[left].coefficients,rows[right].coefficients
 tt=H2.coefficients
 det=aa[0]*bb[1]-aa[1]*bb[0]
 if not det:
  say("new_original_pair_identically_degenerate",left=left,right=right,
      entireZeroFiberRetained=True);return
 ca=(tt[0]*bb[1]-tt[1]*bb[0])/det
 cb=(aa[0]*tt[1]-aa[1]*tt[0])/det
 gd=ca.d.gcd(cb.d);den=(ca.d/gd)*cb.d
 qa,qb=den/ca.d,den/cb.d
 assert qa*ca.d==den and qb*cb.d==den
 tagA,tagB=ca.n*qa,cb.n*qb
 assert K2(R(den))*H2==K2(R(tagA))*rows[left]+K2(R(tagB))*rows[right]
 core=den;removed=[]
 for uname,atom in unit_atoms:
  count=0
  while core:
   gg=core.gcd(atom)
   if gg.total_degree()==0:break
   qq=core/gg;assert qq*gg==core;core=qq;count+=1
  if count:removed.append([uname,count])
 if core:
  cc=core.coefficient(0);before=core;core=core/cc;assert core*cc==before
 say("new_general_Phi0_two_row_original_unit_return",
     label=label,left=left,right=right,target="same H^2",
     necessaryCore=profile(core),completeTwoCoefficientIdentity=True,
     allTemporaryParameterPivotZeroFibersRetained=True,
     paidGcdSources=removed,statistics=dict(stats),
     entireOpenChartExcluded=(core.total_degree()==0))
 saved_polynomial(core,label)
actual_unit_pair("E1","EB","mean_E1_EB")
actual_unit_pair("E1","EC","mean_E1_EC")
# One genuinely new original value row follows the complete mean returns.
v,z=gram[0],gram[1]
vc=va(v,vs(-tau(v),one));zc=va(z,vs(-tau(z),one))
Pj=3*tau(vm(vm(vc,vc),zc))
Nv=(4*tau(vm(dvec,vm(v,z)))-2*F2*tau(vm(v,z))
 -4*(tau(v)*tau(vm(dvec,z))+tau(z)*tau(vm(dvec,v)))
 +4*F2*tau(v)*tau(z)+tau(vm(v,DK(z)))+tau(vm(z,DK(v))))
N1=Nv-(4*lam/3)*Pj
rows["N1"]=clear_original_row("N1",N1)
actual_unit_pair("E1","N1","mean_E1_original_N1")
say("complete_new_general_Phi0_rho_two_mean_N1_input",
    originalRows=list(rows),sameOriginalRhoAndSameGram=True,
    noAlgebraicNormInversions=True,
    headZeroBranchesNotDiscarded=True,
    entirePhiFaceClaim=False,ordinaryISPClaim=False)
