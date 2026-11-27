#!/usr/bin/env python3
"""New general LS h=1 original full value input, after the old value atlas.
Reuse the published collision parameterization; do not re-register it.
Clear the SAME original two-line determinant in the full Gram matrix.
No quotient algebra, no norm inverse, no rational five-coordinate replay.
First actual input: 180 seconds, 4 GiB, three parameters ell/lambda/rho.
"""
import os,json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start)
 print(json.dumps(kw),flush=True)
helper=Path(os.environ.get("ISP_CENTERED_VALUE_HELPER",
 str(Path(__file__).with_name("2026-11-27-unit211-rank-one-centered-value-original-gram-helper-8542.py"))))
helper_text=helper.read_text()
assert hashlib.sha256(helper_text.encode()).hexdigest()=="41459fea3ff0419d8c9230a2f6093cc0b1bc5f528b6f2d2e714a4469f11e5c3e"
exec(compile(helper_text,str(helper),"exec"),globals())
ctx=fmpq_mpoly_ctx.get(('ell','lam','rho'),'lex')
ep,Lp,rp=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
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

ell,lam,rho=map(R,(ep,Lp,rp))
v=original_rank_one_values(ell,lam,rho)
A,B,xi,b,c,p,q,Q,u=(v[k] for k in
 ("A2","B3","xi","b","c","p","q","Q","u"))
T,S,zeta,Pf,Pc,Phi,NF,NC=(v[k] for k in
 ("T","S","zeta","Pf","Pc","Phi","NF","NC"))
M=ell*v["V2"]-u*u;D=ell*A-T*T
assert c*xi*xi==A and c*xi**3==B
assert c*xi==T and D==b*A
assert b*p+c*q==u and p*q==Q
assert M==4*b*c*rho*rho
H0=v["determinant"]
f0=S*zeta*Pc-Phi*NC
t0=(Pf*NC-Pc*NF)/(c*Q)
assert Pf*f0+c*Q*Phi*t0+Pc*H0==0
assert NF*f0+c*Q*S*zeta*t0+NC*H0==0
def profile(pp):
 out=dict(degrees=list(map(int,pp.degrees())),terms=len(pp.to_dict()))
 txt=str(pp).encode();out.update(bytes=len(txt),sha256=hashlib.sha256(txt).hexdigest())
 return out
def rational_profile(rr):
 rr=R(rr);return dict(numerator=profile(rr.n),denominator=profile(rr.d))
def ell_leading(rr):
 rr=R(rr)
 assert all(mm[0]==0 for mm in rr.d.to_dict())
 deg=int(rr.n.degrees()[0]);lc=zeroP
 for mm,cf in rr.n.to_dict().items():
  if mm[0]==deg:lc+=cf*Lp**int(mm[1])*rp**int(mm[2])
 return deg,R(lc,rr.d)
deg,lc=ell_leading(H0)
expected_lc=-2*S*xi*p**5/rho
say("new_general_h_one_original_two_line_compact_input",
 oldCoordinateSource="R150 original U value atlas section 2.2",
 variables=["ell","lambda","rho"],PhiNeverInverted=True,
 originalDIdentity="D=b*A2",originalMomentAndTwoLineProductsVerified=True,
 determinant=rational_profile(H0),ellDegree=deg,
 determinantLeading=rational_profile(lc),
 determinantLeadingEqualsMinus2SXiP5OverRho=(lc==expected_lc),
 noGeneralFiveCoordinateExpansionRerun=True,claimExcluded=False)
# Common numerator factors divide the actual determinant and are point units.
originalH0=H0;originalf0=f0;originalt0=t0
common=H0.n.gcd(f0.n).gcd(t0.n)
H0=R(H0.n/common,H0.d);f0=R(f0.n/common,f0.d);t0=R(t0.n/common,t0.d)
assert R(common)*H0==originalH0
assert R(common)*f0==originalf0 and R(common)*t0==originalt0
assert Pf*f0+c*Q*Phi*t0+Pc*H0==0
assert NF*f0+c*Q*S*zeta*t0+NC*H0==0
say("new_general_h_one_same_determinant_common_cancellation",
 common=profile(common),remainingH0=rational_profile(H0),
 remainingF0=rational_profile(f0),remainingT0=rational_profile(t0),
 fullThreeNumeratorProductsVerified=True,
 removedFactorDividesOriginalDeterminant=True,claimExcluded=False)
base_units=[("lambda",lam),("rho",rho),("p",p),("q",q),
            ("A2",A),("B3",B),("S",S)]
all_units=base_units+[
 ("b",b),("c",c),("u",u),("u-1",u-1),("Q",Q),
 ("ell",ell),("u-ell",u-ell),("M",M),("P02",v["P02"]),
 ("T0",v["T0"]),("J-Q",v["J"]-Q),("u+Q-1",u+Q-1),
 ("original_Delta",originalH0)]
base_atoms=[(n,R(a).n) for n,a in base_units]
atoms=[(n,R(a).n) for n,a in all_units]
den_cache=set()
def audit_base_den(rr):
 rr=R(rr);pp=rr.d
 assert all(mm[0]==0 for mm in pp.to_dict())
 key=str(pp)
 if key in den_cache:return
 for name,atom in base_atoms:
  while pp:
   gg=pp.gcd(atom)
   if gg.total_degree()==0:break
   qq=pp/gg;assert qq*gg==pp
   aa=atom/gg;assert aa*gg==atom
   pp=qq
 assert pp.total_degree()==0,("unpaid base denominator",str(pp))
 den_cache.add(key)
for rr in list(v.values())+[f0,t0,H0]:
 audit_base_den(rr)
gram=original_rank_one_cleared_gram(v,f0,t0,H0)
assert gram["P1Residual"]==0
for row in gram["rows"]:
 for rr in row:audit_base_den(rr)
say("new_general_h_one_full_original_cleared_Gram",
 scale="H=b*H0",originalF="f0/H0",originalT="t0/(b*H0)",
 originalH0DividesActualTwoLineDeterminant=True,
 allClearedGramEntriesUseOnlyPaidBaseDenominators=True,
 currentOriginalP1ExactlyZero=True,
 originalNVRetrievedByPaidAtlasAndActualMomentsAndTwoLines=True,
 fullOriginalNVExpansionNotRepeated=True,claimExcluded=False)
def normalized_row(name,rr):
 rr=R(rr);audit_base_den(rr);pp=rr.n;removed=[];prod=oneP
 for uname,atom in atoms:
  count=0
  while pp:
   gg=pp.gcd(atom)
   if gg.total_degree()==0:break
   qq=pp/gg;assert qq*gg==pp
   aa=atom/gg;assert aa*gg==atom
   pp=qq;prod*=gg;count+=1
  if count:removed.append([uname,count])
 assert pp*prod==rr.n
 if pp:
  leading=pp.coefficient(0);pp=pp/leading
 else:leading=fmpq(1)
 assert pp*leading*prod==rr.n
 de,lc=ell_leading(R(pp))
 report=dict(name=name,scale="H^2" if name in ["E1","EB","EC"] else "H^3",
 before=profile(rr.n),after=profile(pp),denominator=profile(rr.d),
 paidRemoved=removed,completePaidProductVerified=True,
 ellDegree=de,ellLeading=profile(lc.n),unpaidLeadingNeverInverted=True)
 txt=str(pp)
 if len(txt)<=8192:report["exactPolynomial"]=txt
 say("new_general_h_one_full_individual_original_row",**report,claimExcluded=False)
 return pp,report
polys={};reports=[]
for name,rr in gram["equations"]():
 pp,rec=normalized_row(name,rr);polys[name]=pp;reports.append(rec)
assert list(polys)==["E1","EB","EC","N1","NB","PB","NC","PC"]
signal.alarm(0)
say("complete_general_h_one_original_cleared_eight_values",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 helperSHA256=hashlib.sha256(helper_text.encode()).hexdigest(),
 allOriginalMeansN1AndBothSingletonNP=True,
 oldCollisionParameterizationReused=True,secondCollisionByLabelInterchange=True,
 originalNonzeroConditionsRetained=[n for n,a in all_units]+["S","zeta","D","h-k"],
 noPhiInverse=True,noFiniteAlgebraNormInverse=True,
 chart="general LS; (h-1)(k-1)=0; original two-line determinant nonzero",
 allEightRowsReturned=True,newParameterProjectionComputed=False,
 allDenominatorsOnlyLambdaRhoBase=True,baseDenominatorCount=len(den_cache),
 claimExcluded=False,ordinaryISPClaim=False,
 maximumChildRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
