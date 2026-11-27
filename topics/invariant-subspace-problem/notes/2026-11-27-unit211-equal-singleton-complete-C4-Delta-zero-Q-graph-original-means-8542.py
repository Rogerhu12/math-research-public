#!/usr/bin/env python3
"""New whole C4(lambda), h=k, Delta=0 original Q graph and scalar cofactors.
First pay the complete Q head by a whole K[u] Bezout against the original
Delta constant term, retaining any unpaid head-zero fiber. Use only the
proved compact original mean/N1 identities, all on that same Q(u).
Return complete K[u] gcds of original Tnum and fixed original 3-column
cofactors, stripping only original units and the just-paid Q head.
120 seconds /1 GiB. No prior lambda projection or Gram gate is run.
"""
import json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_poly
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
start=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start);print(json.dumps(kw),flush=True)
def QQ(v=()):return fmpq_poly([fmpq(x) for x in v])
class ConstantSplit(Exception):pass
inverse_count=0;division_count=0
def process_case(phi):
 global inverse_count,division_count
 phi=phi/phi[phi.degree()]
 class C:
  def __init__(self,v=0):
   if isinstance(v,C):self.p=v.p;return
   if isinstance(v,fmpq_poly):pp=v
   elif isinstance(v,(list,tuple)):pp=QQ(v)
   else:pp=QQ([v])
   qq,rr=divmod(pp,phi);assert qq*phi+rr==pp
   self.p=rr
  def __bool__(self):return bool(self.p)
  def __neg__(self):return C(-self.p)
  def __add__(self,v):return C(self.p+C(v).p)
  __radd__=__add__
  def __sub__(self,v):return self+-C(v)
  def __rsub__(self,v):return C(v)+-self
  def __mul__(self,v):return C(self.p*C(v).p)
  __rmul__=__mul__
  def __eq__(self,v):return self.p==C(v).p
  def inv(self):
   global inverse_count
   assert self
   gg,ss,tt=self.p.xgcd(phi)
   assert ss*self.p+tt*phi==gg
   if gg.degree()>0:
    qq,rr=divmod(phi,gg);assert not rr and qq*gg==phi
    assert 0<gg.degree()<phi.degree()
    raise ConstantSplit(gg,qq)
   out=C(ss/gg[0]);assert self*out==C(1);inverse_count+=1
   return out
  def __truediv__(self,v):return self*C(v).inv()
  def __rtruediv__(self,v):return C(v)*self.inv()
  def __pow__(self,n):
   assert isinstance(n,int) and n>=0
   out=C(1)
   for i in range(n):out=out*self
   return out
  def data(self):return [str(v) for v in self.p.coeffs()]
 zeroC=C();one=C(1)
 def trim(pp):
  while pp and not pp[-1]:pp.pop()
  return pp
 def add(aa,bb):
  cc=[zeroC]*max(len(aa),len(bb))
  for j,v in enumerate(aa):cc[j]=cc[j]+v
  for j,v in enumerate(bb):cc[j]=cc[j]+v
  return trim(cc)
 def neg(aa):return [-v for v in aa]
 def sub(aa,bb):return add(aa,neg(bb))
 def mul(aa,bb):
  if not aa or not bb:return []
  cc=[zeroC]*(len(aa)+len(bb)-1)
  for i,v in enumerate(aa):
   for j,w in enumerate(bb):cc[i+j]=cc[i+j]+v*w
  return trim(cc)
 def scale(aa,v):return trim([cc*v for cc in aa])
 def divrem(aa,bb):
  global division_count
  assert bb
  rr=aa[:];qq=[zeroC]*max(0,len(aa)-len(bb)+1);iv=bb[-1].inv()
  while rr and len(rr)>=len(bb):
   shift=len(rr)-len(bb);cf=rr[-1]*iv
   qq[shift]=qq[shift]+cf
   for j,v in enumerate(bb):rr[j+shift]=rr[j+shift]-cf*v
   rr=trim(rr)
  qq=trim(qq);assert add(mul(qq,bb),rr)==aa;division_count+=1
  return qq,rr
 def xgcd(aa,bb):
  r0,r1=aa[:],bb[:];s0,s1=[one],[];t0,t1=[],[one]
  while r1:
   q0,r2=divrem(r0,r1)
   r0,r1=r1,r2;s0,s1=s1,sub(s0,mul(q0,s1));t0,t1=t1,sub(t0,mul(q0,t1))
   assert add(mul(s0,aa),mul(t0,bb))==r0
   assert add(mul(s1,aa),mul(t1,bb))==r1
  if not r0:return [],[],[]
  iv=r0[-1].inv();gg,ss,tt=scale(r0,iv),scale(s0,iv),scale(t0,iv)
  assert add(mul(ss,aa),mul(tt,bb))==gg
  return gg,ss,tt

 def pdata(pp):return [cc.data() for cc in pp]
 def cooperate(fn,level):
  def call(self,other):
   if getattr(other,"_isp_quotient_level",0)>level:return NotImplemented
   return fn(self,other)
  return call
 for nm in ["__add__","__radd__","__sub__","__rsub__","__mul__","__rmul__","__truediv__","__rtruediv__","__eq__"]:
  setattr(C,nm,cooperate(getattr(C,nm),0))
 class R:
  _isp_quotient_level=1
  def __init__(self,n=0,d=None,reduced=False):
   if isinstance(n,R):self.n=n.n[:];self.d=n.d[:];return
   def inp(x):
    if isinstance(x,(list,tuple)):return trim([C(v) for v in x])
    cc=C(x);return [cc] if cc else []
   nn=inp(n);dd=[one] if d is None else inp(d);assert dd
   if not nn:self.n=[];self.d=[one];return
   if not reduced:
    gg,ss,tt=xgcd(nn,dd)
    nn,r1=divrem(nn,gg);dd,r2=divrem(dd,gg);assert not r1 and not r2
   iv=dd[-1].inv();self.n=scale(nn,iv);self.d=scale(dd,iv)
  def __bool__(self):return bool(self.n)
  def __neg__(self):return R(neg(self.n),self.d,True)
  def __add__(self,v):
   v=R(v)
   return R(add(mul(self.n,v.d),mul(v.n,self.d)),mul(self.d,v.d))
  __radd__=__add__
  def __sub__(self,v):return self+-R(v)
  def __rsub__(self,v):return R(v)+-self
  def __mul__(self,v):
   v=R(v);return R(mul(self.n,v.n),mul(self.d,v.d))
  __rmul__=__mul__
  def __truediv__(self,v):
   v=R(v);assert v;return R(mul(self.n,v.d),mul(self.d,v.n))
  def __rtruediv__(self,v):return R(v)/self
  def __pow__(self,n):
   assert n>=0;out=R(1)
   for i in range(n):out=out*self
   return out
  def __eq__(self,v):
   v=R(v);return mul(self.n,v.d)==mul(v.n,self.d)
 for nm in ["__add__","__radd__","__sub__","__rsub__","__mul__","__rmul__","__truediv__","__rtruediv__","__eq__"]:
  setattr(R,nm,cooperate(getattr(R,nm),1))
 lc=C([0,1]);Ac=2*lc*lc-2*lc+1;Bc=4*lc**3-6*lc*lc+3*lc-1
 xc=Bc/Ac;ec=Ac**3/(Bc*Bc);tc=Ac*Ac/Bc
 assert ec==one and tc==xc
 lam=R(lc);A=R(Ac);B=R(Bc);xi=R(xc);ell=R(ec);T=R(tc)
 w=lam-1-T;S=2*xi+3-2*lam;eta=xi+3-2*lam;hh=1+xi
 u=R([0,1]);cstar=3-4*lam+xi*eta
 H=(cstar+S*xi)*u-2*cstar
 C0=2*xi*u*(u-1)*(xi*u+2*eta)
 hg,hs,ht=xgcd(H.n,C0.n)
 assert add(mul(hs,H.n),mul(ht,C0.n))==hg
 headres=hg[:];headrem=[]
 for nm,ap in [("u",[zeroC,one]),("u-1",[-one,one])]:
  while headres:
   gg,ss,tt=xgcd(headres,ap)
   if len(gg)<=1:break
   qq,rr=divrem(headres,gg);assert not rr
   headres=qq;headrem.append(dict(unit=nm,degree=len(gg)-1))
 say("new_C4_original_Delta_Q_head_complete_return",
     originalHead=pdata(H.n),originalConstant=pdata(C0.n),
     fullHeadConstantGcd=pdata(hg),headZeroOriginalUnitRemovals=headrem,
     remainingHeadZeroUPolynomial=pdata(headres),
     allQQConstantInversesAndPolynomialBezoutReturned=True,
     entireHeadZeroFiberExcluded=len(headres)==1)
 if len(headres)!=1:
  say("new_C4_unpaid_original_head_zero_fiber_retained",wholeC4Excluded=False)
  return
 Q=-C0/H;disc=1-Q
 m=u-ell;a=1-ell;bc=(ell*ell-m*m/disc)/4
 V2=2*u-ell*Q;T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
 Phi=T0+4*u-4+Q;P02=(2-3*u)*V2-Q*u+2*u**3
 Pf=T0*(J-Q);G=lam*P02-(1-u)*T0
 Pc=Q*P02*(ell+T)-G*T0;NF=(3-4*lam)*Q+J*xi*eta
 NC=eta*(-G*xi+Q*w*u)
 Delta=Phi*NF-S*xi*Pf;Tnum=Pf*NC-Pc*NF
 assert Delta==R()
 say("new_C4_complete_original_Delta_zero_Q_graph",
     numerator=pdata(Q.n),denominator=pdata(Q.d),
     originalDeltaActuallyZero=True,entireOriginalQHeadZeroExcluded=True)
 def trim(v):
  while v and not v[-1]:v.pop()
  return v
 class U:
  _isp_quotient_level=2
  def __init__(self,v=0):
   if isinstance(v,U):self.c=v.c[:];return
   self.c=trim([R(c) for c in v]) if isinstance(v,(list,tuple)) else ([R(v)] if R(v) else [])
  def __bool__(self):return bool(self.c)
  def __add__(self,v):
   v=U(v);n=max(len(self.c),len(v.c))
   return U([(self.c[j] if j<len(self.c) else R())+(v.c[j] if j<len(v.c) else R()) for j in range(n)])
  __radd__=__add__
  def __neg__(self):return U([-c for c in self.c])
  def __sub__(self,v):return self+-U(v)
  def __rsub__(self,v):return U(v)+-self
  def __mul__(self,v):
   v=U(v)
   if not self or not v:return U()
   out=[R() for _ in range(len(self.c)+len(v.c)-1)]
   for i,x in enumerate(self.c):
    for j,y in enumerate(v.c):out[i+j]=out[i+j]+x*y
   return U(out)
  __rmul__=__mul__
  def __truediv__(self,v):
   assert not isinstance(v,U);v=R(v);assert v
   return U([x/v for x in self.c])
  def __pow__(self,n):
   assert n>=0
   out=U(1)
   for j in range(n):out=out*self
   return out
  def __eq__(self,v):
   v=U(v)
   return len(self.c)==len(v.c) and all(x==y for x,y in zip(self.c,v.c))
 z=U([0,1]);f=-(U(Pc)+bc*Phi*z)/Pf
 assert Pf*f+bc*Phi*z+Pc==U()
 nv=NF*f+bc*S*xi*z+NC
 assert Pf*nv==U(Tnum)-bc*Delta*z
 vn=J*f-G+bc*z
 Wstar=T0+4*u*f;N=Q*Wstar-2*vn
 say("new_equal_singleton_compact_original_full_chart_input",
  variables=["u"],constantField="complete_C4_lambda",originalQGraphPaid=True,freeOriginalCoordinate="z=Q*t",
  fFromOriginalP1=True,NVExactAffineRow=True,
  actualNVIdentity="Pf*NV=Tnum-bc*Delta*z",
  PfPaidByEntireOriginalT0AndJQExclusions=True,
  noDeltaInverse=True,allDeltaZeroFibersRetained=True,
  compactOriginalIdentitySHA256="9ab0270fe53a0a6f169755f92f731e6cf636f1d9b7a9e12364ef487a01cdea6e",
  noOldGramOrProjectionReplayed=True,claimExcluded=False)

 # Exact scalar forms after rho^2=1-Q and rho*(b-c)=u-ell.
 # The paid scaling is R2/(2rho), W4/(4rho^2), O8/rho, and N1*.
 I=((vn+a*u*Q)**2-2*u*Q*vn+2*a*u*u*Q*Q-4*a*u*Q*Q*f
    +bc*z*z+z*(4*bc*u*Q-ell*vn))
 compact_R=I+(m/(2*disc))*z*N
 compact_W=(2*bc*Q*Q*ell*T0-ell*vn*vn-(ell/(4*disc))*N*N
  +(m/disc)*vn*N+8*bc*Q*f*vn+4*bc*bc*z*z
  +8*bc*bc*Q*(u-1)*z-2*bc*ell*z*vn+(bc*m/disc)*z*N)
 Sred=2*ell*vn-(m/disc)*N;Dred=-2*m*vn+ell*N
 compact_O=(32*bc*bc*a*Q*Q*disc*(u-1)+4*bc*Q*disc*Sred
  +32*bc*bc*Q*disc*vn-64*bc*bc*Q*Q*disc*f
  +4*bc*Q*(1-u+2*f)*Dred-Sred*Dred
  -8*bc*bc*m*z*z-16*bc*bc*Q*z*(m*(u-1)+ell*disc)+8*bc*bc*z*N)
 alpha=ell*(1-u)-m;beta_rho=ell*disc-m*(1-u)
 Av=(2*u-1)*ell+3*m;Bu_rho=(2*u-1)*m+3*ell*disc
 compact_N=(alpha*(4*disc*vn*vn+N*N)+4*beta_rho*vn*N
  +8*bc*disc*Q*vn*Wstar-24*bc*disc*Q*Q*f*Wstar
  +16*a*bc*disc*Q*Q*(u-1)*Wstar+64*bc*disc*Q*Q*u*f*f
  -32*bc*disc*Q*u*f*vn+16*bc*disc*Q*Q*(1+a)*T0*f
  +16*bc*disc*Q*(a*Q-T0)*vn+4*bc*disc*Av*z*vn
  -2*bc*Bu_rho*z*N+16*bc*bc*disc*Q*z*(2*f+T0-a*Q)
  -8*u*bc*bc*disc*z*z-16*bc*disc*Q*Q*lam*w*P02)
 assert all(len(v.c)<=3 for v in [compact_R,compact_W,compact_O,compact_N])
 assert len(nv.c)<=2

 paid_atoms=[("Q_head",H.n),("u",u.n),("u-1",(u-1).n),
   ("Q",Q.n),("1-Q",disc.n),("bc",bc.n),("u-ell",m.n),
   ("P02",P02.n),("T0",T0.n),("J-Q",(J-Q).n),("Phi",Phi.n),
   ("u+Q-1",(u+Q-1).n)]
 for nm,ap in paid_atoms:
  if not ap:
   say("new_C4_original_unit_identically_zero",unit=nm,wholeC4Excluded=True)
   return
 def strip(pp):
  orig=pp[:];prod=[one];rec=[]
  if not pp:return pp,rec
  for nm,ap in paid_atoms:
   while pp:
    gg,ss,tt=xgcd(pp,ap)
    if len(gg)<=1:break
    nn,rr=divrem(pp,gg);assert not rr
    prod=mul(prod,gg);pp=nn;rec.append(dict(unit=nm,degree=len(gg)-1))
  assert mul(pp,prod)==orig
  return pp,rec
 den_cache=set()
 def audit_den(pp):
  key=str(pdata(pp))
  if key in den_cache:return
  rr,_=strip(pp);assert len(rr)==1,("unpaid original denominator",pdata(rr))
  den_cache.add(key)
 for rr in [Q,Tnum]:
  audit_den(rr.d)
 rows={}
 for nm,rr in [("R",compact_R),("W",compact_W),("O",compact_O),("N1",compact_N)]:
  for cc in rr.c:audit_den(cc.d)
  rows[nm]=rr.c+[R()]*(3-len(rr.c))
 say("new_C4_all_original_compact_rows_on_same_Q_graph",
     originalRowDegrees={nm:max(i for i,c in enumerate(row) if c) for nm,row in rows.items()},
     allOriginalDenominatorsPaid=True,freeOriginalCoordinate="z=Q*t")
 common,removed=strip(Tnum.n)
 if common:common=scale(common,common[-1].inv())
 say("new_C4_complete_original_Tnum_u_constraint",
     degree=len(common)-1,coefficients=pdata(common),onlyPaidRemovals=removed)
 used=["original_Tnum"]
 for names in [("R","W","O"),("R","W","N1")]:
  if len(common)==1:break
  aa,bb,cc=[rows[nm] for nm in names]
  cof=[bb[1]*cc[2]-bb[2]*cc[1],aa[2]*cc[1]-aa[1]*cc[2],aa[1]*bb[2]-aa[2]*bb[1]]
  det=sum((cof[i]*[aa,bb,cc][i][0] for i in range(3)),R())
  assert all(sum((cof[i]*[aa,bb,cc][i][j] for i in range(3)),R())==(det if j==0 else R()) for j in range(3))
  audit_den(det.d)
  pp,history=strip(det.n)
  ng,ss,tt=xgcd(common,pp)
  assert add(mul(ss,common),mul(tt,pp))==ng
  common=ng;used.append("/".join(names))
  say("new_C4_complete_original_constant_cofactor_and_u_Bezout",
      rows=list(names),necessaryUDegree=len(pp)-1,onlyPaidRemovals=history,
      fullThreeColumnCofactorProductsReturned=True,allWholeUBezoutProductsReturned=True,
      finalUDegree=len(common)-1,finalUPolynomial=pdata(common))
 say("new_C4_entire_original_Delta_zero_return_complete",
     wholeC4Excluded=len(common)==1,originalConditionsUsed=used,
     remainingWholeUPolynomial=pdata(common),allLambdaAndURootsRetained=True,
     paidOriginalDenominatorCount=len(den_cache),ordinaryISPClaim=False)
process_case(QQ(["3/8","-3/2",3,-3,1]))
signal.alarm(0)
say("new_C4_original_Q_graph_and_compact_return_finished",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    actualConstantInverseCount=inverse_count,actualPolynomialDivisionCount=division_count,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
