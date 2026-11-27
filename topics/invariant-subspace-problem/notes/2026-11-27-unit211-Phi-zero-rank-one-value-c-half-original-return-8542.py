#!/usr/bin/env python3
"""New original Phi=0, h=1, c=1/2 whole boundary.
The old original moments force (2lambda-1)^2(3lambda^2-2lambda+1)=0.
Phi then gives ell=1 or3/2; ell=1 is the already-paid equal-weight face.
Return the remaining ell=3/2 original rows over both exact constant fields,
retaining every rho fiber. No modular or resultant inference.120s/1GiB.
"""
import os,json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
start=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start)
 print(json.dumps(kw),flush=True)
def load_helper(env,name,sha):
 pp=Path(os.environ.get(env,str(Path(__file__).with_name(name))))
 ss=pp.read_text();assert hashlib.sha256(ss.encode()).hexdigest()==sha
 exec(compile(ss,str(pp),"exec"),globals())
load_helper("ISP_MONIC_SIX_HELPER",
 "2026-11-27-unit211-monic-six-explicit-geometric-localization-helper-8542.py",
 "5e162fa3adc0737bb152de5635e6956ca03267d055a6b33cea93c957628c96d6")
load_helper("ISP_RANK_ONE_GRAM_HELPER",
 "2026-11-27-unit211-rank-one-centered-value-original-gram-helper-8542.py",
 "41459fea3ff0419d8c9230a2f6093cc0b1bc5f528b6f2d2e714a4469f11e5c3e")

ctx=fmpq_mpoly_ctx.get(("rho",),"lex")
rhop,=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
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


rho=R(rhop);p,q=1+rho,1-rho
paid_atoms=[("rho",rho.n),("p",p.n),("q",q.n)]
def audit_base_unit(pp):
 assert pp
 rr=pp
 for _,atom in paid_atoms:
  while rr:
   gg=rr.gcd(atom)
   if gg.total_degree()==0:break
   new=rr/gg;assert new*gg==rr;rr=new
 assert rr.total_degree()==0,("unpaid rho inverse",str(rr))
def audit_coefficient(rr):
 rr=R(rr);audit_base_unit(rr.d)
alpha=R(fmpq(-2,3));beta=R(fmpq(1,3))
cooperate_parameter_ring(R)
statistics=dict(multiplications=0,reductionIdentities=0,inverseProducts=0,
                polynomialDivisions=0,polynomialBezoutProducts=0)
class K:
 """QQ(rho)[lambda]/(lambda^2-2lambda/3+1/3).
 The lambda=1/2 case uses only its scalar subfield.
 No rho-dependent norm is inverted without the original rho,p,q audit.
 """
 _isp_quotient_level=1
 __slots__=("c",)
 def __init__(self,x=0):
  if isinstance(x,K):self.c=x.c;return
  cc=list(x) if isinstance(x,(list,tuple)) else [x]
  assert len(cc)<=2
  cc=[R(a) for a in cc]+[R(0)]*(2-len(cc))
  for a in cc:audit_coefficient(a)
  self.c=tuple(cc)
 @classmethod
 def internal(cls,a,b):
  ob=object.__new__(cls);ob.c=(a,b);return ob
 def __bool__(self):return any(self.c)
 def __add__(self,o):
  o=K(o);return K.internal(self.c[0]+o.c[0],self.c[1]+o.c[1])
 __radd__=__add__
 def __neg__(self):return K.internal(-self.c[0],-self.c[1])
 def __sub__(self,o):return self+-K(o)
 def __rsub__(self,o):return K(o)+-self
 def __mul__(self,o):
  o=K(o);a,b=self.c;c,d=o.c
  raw0,raw1,raw2=a*c,a*d+b*c,b*d
  out0,out1=raw0-beta*raw2,raw1-alpha*raw2
  assert raw0-out0-beta*raw2==0 and raw1-out1-alpha*raw2==0
  statistics["multiplications"]+=1;statistics["reductionIdentities"]+=2
  return K.internal(out0,out1)
 __rmul__=__mul__
 def inverse(self):
  a,b=self.c
  nn=a*a-alpha*a*b+beta*b*b
  assert nn
  audit_base_unit(nn.n);audit_base_unit(nn.d)
  out=K([(a-alpha*b)/nn,-b/nn])
  assert self*out==1
  statistics["inverseProducts"]+=1
  return out
 def __truediv__(self,o):return self*K(o).inverse()
 def __rtruediv__(self,o):return K(o)*self.inverse()
 def __pow__(self,n):
  assert isinstance(n,int)
  if n<0:return self.inverse()**(-n)
  ans,cur=K(1),self
  while n:
   if n&1:ans=ans*cur
   n>>=1
   if n:cur=cur*cur
  return ans
 def __eq__(self,o):
  o=K(o);return self.c[0]==o.c[0] and self.c[1]==o.c[1]
zeroK,oneK=K(0),K(1)
def constant_inverse(a):
 a=K(a)
 assert all(x.n.total_degree()<=0 and x.d.total_degree()==0 for x in a.c)
 return a.inverse()
def kstr(a):
 a=K(a)
 assert all(x.n.total_degree()<=0 and x.d.total_degree()==0 for x in a.c)
 return [str(x.n.coefficient(0)/x.d.coefficient(0)) if x.n else "0" for x in a.c]
def tr(pp):
 pp=list(pp)
 while pp and not pp[-1]:pp.pop()
 return pp
def pa(pp,qq):
 out=[zeroK]*max(len(pp),len(qq))
 for i,a in enumerate(pp):out[i]=out[i]+a
 for i,a in enumerate(qq):out[i]=out[i]+a
 return tr(out)
def pm(pp,qq):
 if not pp or not qq:return []
 out=[zeroK]*(len(pp)+len(qq)-1)
 for i,a in enumerate(pp):
  for j,b in enumerate(qq):out[i+j]=out[i+j]+a*b
 return tr(out)
def pd(pp,qq):
 original=tr(pp);pp=list(original);qq=tr(qq);assert qq
 inv=constant_inverse(qq[-1])
 out=[zeroK]*max(0,len(pp)-len(qq)+1)
 while pp and len(pp)>=len(qq):
  shift=len(pp)-len(qq);a=pp[-1]*inv;out[shift]=out[shift]+a
  for j,b in enumerate(qq):pp[shift+j]=pp[shift+j]-a*b
  pp=tr(pp)
 out=tr(out)
 assert pa(pm(out,qq),pp)==original
 statistics["polynomialDivisions"]+=1
 return out,pp
def pxgcd(pp,qq):
 pp0,qq0=tr(pp),tr(qq)
 pp,qq=list(pp0),list(qq0)
 s0,s1=[oneK],[]
 t0,t1=[],[oneK]
 while qq:
  quot,rem=pd(pp,qq);pp,qq=qq,rem
  s0,s1=s1,pa(s0,[-a for a in pm(quot,s1)])
  t0,t1=t1,pa(t0,[-a for a in pm(quot,t1)])
 if pp:
  inv=constant_inverse(pp[-1])
  pp=[inv*a for a in pp];s0=[inv*a for a in s0];t0=[inv*a for a in t0]
 assert pa(pm(s0,pp0),pm(t0,qq0))==pp
 statistics["polynomialBezoutProducts"]+=1
 return pp,s0,t0
def poly_profile(pp):
 coeff=[kstr(a) for a in pp]
 return dict(degree=len(pp)-1,sha256=hashlib.sha256(json.dumps(coeff,separators=(",",":")).encode()).hexdigest(),
             coefficientsAscending=coeff if len(pp)<=21 else None)
def clear_actual_row(raw):
 raw=K(raw);den=oneP
 for rr in raw.c:
  audit_coefficient(rr);gg=den.gcd(rr.d);den=(den/gg)*rr.d
 audit_base_unit(den)
 nums=[]
 for rr in raw.c:
  quot=den/rr.d;assert quot*rr.d==den
  nums.append(rr.n*quot)
 dd=max((int(pp.degrees()[0]) for pp in nums if pp),default=-1)
 row=[]
 dicts=[pp.to_dict() for pp in nums]
 for j in range(dd+1):
  row.append(K([fmpq(dd0.get((j,),0)) for dd0 in dicts]))
 row=tr(row)
 # Keep the entire lambda element at each rho degree. NEVER infer that
 # its two QQ coefficient functions vanish separately at an original root.
 rebuilt=zeroK
 for j,cc in enumerate(row):rebuilt=rebuilt+cc*(rho**j)
 assert rebuilt==raw*K(R(den))
 removed=[]
 for name,atom in [("rho",[zeroK,oneK]),("p",[oneK,oneK]),("q",[oneK,-oneK])]:
  power=0
  while row:
   quot,rem=pd(row,atom)
   if rem:break
   assert pm(quot,atom)==row
   row=quot;power+=1
  if power:removed.append([name,power])
 return row,removed
case_returns=[]
for label,lam in [("lambda_half",K(fmpq(1,2))),("lambda_quadratic",K([0,1]))]:
 ell=K(fmpq(3,2))
 if label=="lambda_half":assert 2*lam-1==0
 else:assert 3*lam*lam-2*lam+1==0
 vv=original_rank_one_values(ell,lam,rho)
 assert 2*vv["A2"]**3==vv["B3"]**2
 assert vv["c"]==fmpq(1,2) and vv["b"]==1 and vv["Phi"]==0
 assert vv["S"] and vv["zeta"] and vv["Pf"]
 # Constants A2,B3,S in each of the two exact lambda fields are explicitly
 # inverted with full products; only rho,p,q parameter factors are inverted.
 for atom in (vv["A2"],vv["B3"],vv["S"]):
  assert atom*atom.inverse()==1
 f0=-vv["Pc"];Pf=vv["Pf"]
 t0=-(vv["NF"]*f0+vv["NC"]*Pf)/(vv["c"]*vv["Q"]*vv["S"]*vv["zeta"])
 assert vv["NF"]*f0+vv["c"]*vv["Q"]*vv["S"]*vv["zeta"]*t0+vv["NC"]*Pf==0
 gram=original_rank_one_cleared_gram(vv,f0,t0,Pf)
 assert gram["P1Residual"]==0
 say("whole_c_half_original_constant_field_input",
     case=label,lambdaEquation="2*lambda-1" if label=="lambda_half" else "3*lambda^2-2*lambda+1",
     ell="3/2",weights_b_c=["1","1/2"],originalPhiZero=True,
     originalPfLine=True,originalNVLine=True,originalP1=True,
     discardedEllOneOnlyByPublishedWholeEqualWeights=True,
     noRhoFiberDiscarded=True,claimExcluded=False)
 generators=[];tags=[];gg=[];names=[]
 for name,raw in gram["equations"]():
  pp,removed=clear_actual_row(raw)
  say("new_c_half_same_source_original_row",case=label,name=name,
      originalScalePower=2 if name in ("E1","EB","EC") else 3,
      polynomial=poly_profile(pp),paidRhoFactorsRemoved=removed,
      actualBothLambdaEmbeddingsRetained=(label=="lambda_quadratic"),
      noSeparateCoefficientVanishingInference=True,claimExcluded=False)
  if not pp:continue
  newg,ss,tt=pxgcd(gg,pp)
  tags=[pm(ss,tag) for tag in tags]+[tt]
  generators.append(pp);names.append(name)
  check=[]
  for tag,gen in zip(tags,generators):check=pa(check,pm(tag,gen))
  assert check==newg
  gg=newg
  say("whole_c_half_actual_constant_field_Bezout",case=label,
      usedOriginalRows=names,gcd=poly_profile(gg),
      tagDegrees=[len(tag)-1 for tag in tags],
      allOriginalProductsMultipliedBack=True,
      tagSha256=hashlib.sha256(json.dumps([[kstr(a) for a in tag] for tag in tags],separators=(",",":")).encode()).hexdigest(),
      claimExcluded=(gg==[oneK]))
  if gg==[oneK]:break
 done=gg==[oneK]
 case_returns.append(dict(case=label,completeOriginalExclusion=done,
                          usedOriginalRows=names,remainingGcd=poly_profile(gg)))
 say("complete_c_half_actual_field_return",**case_returns[-1],statistics=dict(statistics),
     modularResultUsed=False,actualRowFields="QQ or QQ[lambda]/(3lambda^2-2lambda+1)")
say("complete_Phi0_rank_one_c_half_original_return",
    scope="only Phi=0 and zn=0, ordered h=1, c=1/2; k=1 follows by B/C exchange",
    exactMomentFactor="2*A2^3-B3^2=(2lambda-1)^2*(3lambda^2-2lambda+1)",
    exactPhiFactor="Phi=-(1+rho)^2*(ell-1)*(2ell-3)",
    ellOneExcludedByPublishedWholeEqualWeights=True,
    originalFieldReturns=case_returns,claimExcluded=all(x["completeOriginalExclusion"] for x in case_returns),
    wholePhiFaceClaim=False,ordinaryISPClaim=False)
