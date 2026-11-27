#!/usr/bin/env python3
"""New full original Gram return on the Delta=0 equal-weight lambda20 fiber.
Recover Q from the original compatibility gcd in the COMPLETE QQ constant
algebra. Then solve the original N(V) row for t by its already paid coefficient
bc*Q*S*xi, retain free f, and return every original mean and N/P condition.
No Delta inverse, no imported D!=0 theorem. 180s/4GiB.
"""
import json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start)
 print(json.dumps(kw),flush=True)
ctx=fmpq_mpoly_ctx.get(("lam","Q"),"lex")
Lp,Qp=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
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

def cooperate(fn):
 def wrapped(self,other):
  if getattr(other,"_isp_quotient_level",0)>0:return NotImplemented
  return fn(self,other)
 return wrapped
for name in ("__add__","__radd__","__sub__","__rsub__","__mul__","__rmul__",
             "__truediv__","__rtruediv__","__eq__"):
 setattr(R,name,cooperate(getattr(R,name)))
lam,Q=map(R,(Lp,Qp));disc=1-Q
class E:
 _isp_quotient_level=1
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,o):o=E(o);return E(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,o):return self+-E(o)
 def __rsub__(self,o):return E(o)+-self
 def __mul__(self,o):
  o=E(o);return E(self.a*o.a+disc*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __truediv__(self,o):
  assert not isinstance(o,E)
  o=R(o);assert o
  return E(self.a/o,self.b/o)
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  ans,cur=E(1),self
  while n:
   if n&1:ans=ans*cur
   n>>=1
   if n:cur=cur*cur
  return ans
 def __eq__(self,o):o=E(o);return self.a==o.a and self.b==o.b
 def conj(self):return E(self.a,-self.b)
A=2*lam*lam-2*lam+1;B=4*lam**3-6*lam*lam+3*lam-1
xi=B/A;ell=A**3/(B*B);u=ell;T=A*A/B;w=lam-1-T
hh=1+xi;S=2*xi+3-2*lam;eta=xi+3-2*lam
p=E(1,1);q=p.conj()
b=E(ell/2,(u-ell)/(2*disc));c=b.conj();a=E(1-ell)
assert not b.b and b==c and u==ell
bc=(ell*ell-(u-ell)**2/disc)/4
assert b+c==E(ell) and b*p+c*q==E(u) and b*c==E(bc)
assert p*q==E(Q) and (p-q)**2==E(4*disc)
V2=2*u-ell*Q;T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
Phi=T0+4*u-4+Q
P02=(2-3*u)*V2-Q*u+2*u**3
Pf=T0*(J-Q);G=lam*P02-(1-u)*T0
Pc=Q*P02*(ell+T)-G*T0
NF=(3-4*lam)*Q+J*xi*eta
NC=eta*(-G*xi+Q*w*u)
Delta=Phi*NF-S*xi*Pf
F=S*xi*Pc-Phi*NC;Tnum=Pf*NC-Pc*NF
assert Pf*F+Phi*Tnum+Pc*Delta==0
assert NF*F+S*xi*Tnum+NC*Delta==0

# Exact ORIGINAL affine rows in the unknowns (1,f,t).
rowP=[Pc,Pf,bc*Q*Phi]
rowN=[NC,NF,bc*Q*S*xi]
assert [S*xi*rowP[j]-Phi*rowN[j] for j in range(3)]==[F,-Delta,R()]
assert [Pf*rowN[j]-NF*rowP[j] for j in range(3)]==[Tnum,R(),-bc*Q*Delta]
say("new_equal_value_equal_weight_Delta_zero_original_affine_compatibility",
    originalRowP=["Pc","Pf","bc*Q*Phi"],
    originalRowN=["NC","NF","bc*Q*S*xi"],
    fullBothCoefficientIdentitiesActuallyReturned=True,
    necessaryOriginalRows=["Delta","F","Tnum"],
    noDeltaT0PfOrNormInverse=True,oldDNonzeroTheoremNotImported=True)
def profile(pp):
 ss=str(pp).encode()
 return dict(degrees_lambda_Q=list(map(int,pp.degrees())),
             totalDegree=int(pp.total_degree()),terms=len(pp.to_dict()),
             bytes=len(ss),sha256=hashlib.sha256(ss).hexdigest())
base_atoms=[("A2",A.n),("B3",B.n),("Q",Qp),("rho_squared",disc.n)]
paid_atoms=base_atoms+[("lambda",Lp),("original_bc",bc.n),
                      ("original_P02",P02.n),("previous_whole_S_zero_excluded",S.n)]
def audit_den(pp):
 rr=pp
 for name,atom in base_atoms:
  while rr:
   gg=rr.gcd(atom)
   if gg.total_degree()==0:break
   out=rr/gg;assert out*gg==rr;rr=out
 assert rr.total_degree()==0
def primitive(pp):
 rr=pp;product=oneP;removed=[]
 for name,atom in paid_atoms:
  count=0
  while rr:
   gg=rr.gcd(atom)
   if gg.total_degree()==0:break
   out=rr/gg;assert out*gg==rr;rr=out;product*=gg;count+=1
  if count:removed.append(dict(originalUnit=name,gcdLoops=count))
 assert rr*product==pp
 if rr:
  scalar=rr.coefficient(0);rr=rr/scalar
  assert rr*scalar*product==pp
 return rr,removed
def factored(pp):
 if not pp:return dict(zero=True)
 content,factors=pp.factor();back=ctx.constant(content);data=[]
 for ff,power in factors:
  back*=ff**int(power);item=dict(power=int(power),profile=profile(ff))
  ss=str(ff)
  if len(ss.encode())<=8192:item["polynomial"]=ss
  data.append(item)
 assert back==pp
 return dict(content=str(content),factors=data,fullQQProductVerified=True)
cores={}
for name,rr in [("Delta",Delta),("F",F),("Tnum",Tnum)]:
 audit_den(rr.d);cc,removed=primitive(rr.n);cores[name]=cc
 say("new_Delta_zero_equal_weight_original_compatibility_core",
     name=name,rawNumerator=profile(rr.n),primitive=profile(cc),
     factorization=factored(cc),onlyPaidOriginalRemoval=removed,
     originalDeltaWasNotRemoved=True,claimExcluded=False)
from flint import fmpq_poly
def QQ(v=()):return fmpq_poly([fmpq(x) for x in v])
QZ=QQ();QO=QQ([1])
class ConstantSplit(Exception):
 def __init__(self,g,h):self.g=g;self.h=h
case_results=[];split_records=[];inverse_count=0;division_count=0
def process_case(phi,label):
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
  def data(self):return [str(v) for v in self.p.coeffs()]
 z=C();one=C(1)
 def trim(pp):
  while pp and not pp[-1]:pp.pop()
  return pp
 def add(aa,bb):
  cc=[z]*max(len(aa),len(bb))
  for j,v in enumerate(aa):cc[j]=cc[j]+v
  for j,v in enumerate(bb):cc[j]=cc[j]+v
  return trim(cc)
 def neg(aa):return [-v for v in aa]
 def sub(aa,bb):return add(aa,neg(bb))
 def mul(aa,bb):
  if not aa or not bb:return []
  cc=[z]*(len(aa)+len(bb)-1)
  for i,v in enumerate(aa):
   for j,w in enumerate(bb):cc[i+j]=cc[i+j]+v*w
  return trim(cc)
 def scale(aa,v):return trim([cc*v for cc in aa])
 def divrem(aa,bb):
  global division_count
  assert bb
  rr=aa[:];qq=[z]*max(0,len(aa)-len(bb)+1);iv=bb[-1].inv()
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
 def from_mpoly(pp):
  if not pp:return []
  out=[z]*(int(pp.degrees()[1])+1)
  byq={}
  for ex,cc in pp.to_dict().items():
   il,iq=map(int,ex)
   if iq not in byq:byq[iq]=[fmpq(0)]*(int(pp.degrees()[0])+1)
   byq[iq][il]=fmpq(cc)
  for iq,cc in byq.items():out[iq]=C(QQ(cc))
  return trim(out)
 def pdata(pp):return [cc.data() for cc in pp]
 def small_profile(pp):
  blob=json.dumps(pdata(pp),separators=(",",":")).encode()
  r=dict(Qdegree=len(pp)-1,bytes=len(blob),sha256=hashlib.sha256(blob).hexdigest())
  if len(blob)<=8192:r["coefficients_Q_then_lambda"]=pdata(pp)
  return r

 try:
  compat_names=["Delta","F","Tnum"]
  comp={name:from_mpoly(cores[name]) for name in compat_names}
  gg=[];ctags=[];used=[]
  for name in compat_names:
   new,aa,bb=xgcd(gg,comp[name])
   ctags=[mul(aa,tt) for tt in ctags]+[bb];used.append(name);gg=new
   actual=[]
   for tt,nn in zip(ctags,used):actual=add(actual,mul(tt,comp[nn]))
   assert actual==gg
  say("new_Delta_zero_equal_weight_complete_constant_Q_compatibility",
      case=label,lambdaDegree=int(phi.degree()),gcd=small_profile(gg),
      allThreeOriginalCompatibilityBezoutProductsVerified=True,
      allLambdaAndQHeadFibersRetained=True,claimExcluded=False)
  if len(gg)==1:
   out=dict(case=label,excluded=True,reason="original compatibility returns constant one")
   case_results.append(out);say("new_Delta_zero_equal_weight_original_full_return",**out);return
  if len(gg)!=2:
   out=dict(case=label,excluded=False,reason="Q compatibility is not yet a single linear fiber",
            retainedQGcd=small_profile(gg))
   case_results.append(out);say("new_Delta_zero_equal_weight_original_full_return",**out);return
  assert gg[1]==one
  Qvalue=-gg[0]
  def evalq(pp):
   out=z
   for cc in reversed(pp):out=out*Qvalue+cc
   return out
  for name in compat_names:assert not evalq(comp[name])
  for name,atom in paid_atoms:
   value=evalq(from_mpoly(atom))
   if not value:
    out=dict(case=label,excluded=True,reason="an original physical unit vanishes on this whole recovered Q fiber",
             originalUnit=name)
    case_results.append(out);say("new_Delta_zero_equal_weight_original_full_return",**out);return
   assert value*value.inv()==one
  def evr(rr):
   rr=R(rr);numer=evalq(from_mpoly(rr.n));denom=evalq(from_mpoly(rr.d))
   assert denom
   return numer*denom.inv()
  lv,uv,Qv,dv0,bcv,Tv0,Vv2,Pv02,lamb,wval,hval,Sv,xiv,Nfv,Ncv=[
   evr(rr) for rr in [ell,u,Q,disc,bc,T0,V2,P02,lam,w,hh,S,xi,NF,NC]]
  assert Qv==Qvalue and uv==lv
  assert not evr(Delta) and not evr(F) and not evr(Tnum)
  den_t=bcv*Qv*Sv*xiv
  assert den_t
  t_inverse=den_t.inv();assert den_t*t_inverse==one
  class U:
   def __init__(self,v=0):
    if isinstance(v,U):self.c=v.c[:];return
    if isinstance(v,(list,tuple)):self.c=trim([C(cc) for cc in v])
    else:
     cc=C(v);self.c=[cc] if cc else []
   def __bool__(self):return bool(self.c)
   def __neg__(self):return U(neg(self.c))
   def __add__(self,v):return U(add(self.c,U(v).c))
   __radd__=__add__
   def __sub__(self,v):return U(sub(self.c,U(v).c))
   def __rsub__(self,v):return U(sub(U(v).c,self.c))
   def __mul__(self,v):return U(mul(self.c,U(v).c))
   __rmul__=__mul__
   def scale(self,v):return U(scale(self.c,C(v)))
   def __pow__(self,n):
    out=U(1)
    for i in range(n):out=out*self
    return out
   def __eq__(self,v):return self.c==U(v).c
  class Eunit:
   def __init__(self,a=0,b=0):
    if isinstance(a,Eunit):self.a=a.a;self.b=a.b;return
    self.a=U(a);self.b=U(b)
   def __bool__(self):return bool(self.a) or bool(self.b)
   def __neg__(self):return Eunit(-self.a,-self.b)
   def __add__(self,v):v=Eunit(v);return Eunit(self.a+v.a,self.b+v.b)
   __radd__=__add__
   def __sub__(self,v):return self+-Eunit(v)
   def __rsub__(self,v):return Eunit(v)+-self
   def __mul__(self,v):
    v=Eunit(v)
    return Eunit(self.a*v.a+(self.b*v.b).scale(dv0),self.a*v.b+self.b*v.a)
   __rmul__=__mul__
   def __pow__(self,n):
    out=Eunit(1)
    for i in range(n):out=out*self
    return out
   def scale(self,v):return Eunit(self.a.scale(v),self.b.scale(v))
   def conj(self):return Eunit(self.a,-self.b)
   def __eq__(self,v):v=Eunit(v);return self.a==v.a and self.b==v.b
  free_f=U([0,1])
  free_t=-(free_f.scale(Nfv)+U(Ncv)).scale(t_inverse)
  assert free_f.scale(Nfv)+free_t.scale(den_t)+U(Ncv)==U()
  assert free_f.scale(evr(Pf))+free_t.scale(bcv*Qv*evr(Phi))+U(evr(Pc))==U()
  bp=lv*C(fmpq(1,2));cp=bp;av=C(1)-lv
  be,ce,ae=Eunit(bp),Eunit(cp),Eunit(av)
  pe=Eunit(1,1);qe=pe.conj()
  ivdiff=Eunit(0,C(fmpq(-1,2))*dv0.inv())
  assert ivdiff*(qe-pe)==Eunit(1)
  W1=U(Tv0*C(fmpq(1,2)))+free_f.scale(2*uv)
  W2=U(uv*Tv0+lamb*Pv02)+free_f.scale(Vv2+2*uv*uv)-free_t.scale(bcv*Qv)
  invbcQ=(bcv*Qv).inv()
  X=(ce*qe*ivdiff*(qe*Eunit(W1)-Eunit(W2))).scale(invbcQ)
  Y=(be*pe*ivdiff*(Eunit(W2)-pe*Eunit(W1))).scale(invbcQ)
  rg=X-ae*pe-ce*Eunit(free_t)
  sg=Y-ae*qe-be*Eunit(free_t)
  AA=2*Eunit(free_f)-2*be*X-2*ce*Y+Eunit(free_t.scale(2*bcv))
  ez=Eunit();eo=Eunit(1)
  rows=[[ez,ez,pe,qe],[ez,AA,rg,sg],[pe,rg,ez,Eunit(free_t)],[qe,sg,Eunit(free_t),ez]]
  unitvec=[eo,ez,eo,eo]
  def va(x0,y0):return [a0+b0 for a0,b0 in zip(x0,y0)]
  def vs(a0,x0):return [a0*b0 for b0 in x0]
  def vm(x0,y0):return [x0[0]*y0[0],x0[0]*y0[1]+x0[1]*y0[0],x0[2]*y0[2],x0[3]*y0[3]]
  def tau(x0):return ae*x0[0]+x0[1]+be*x0[2]+ce*x0[3]
  def DK(x0):return [tau(vm(row,x0)) for row in rows]
  geomdv=DK(unitvec);F2=tau(geomdv);Kd=DK(geomdv)
  assert F2==Eunit(free_f.scale(2))
  def mean(j):
   ee=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
   return ee-2*Kd[j]-2*vm(geomdv,geomdv)[j]+2*F2*geomdv[j]
  def N4(v0):
   tv=tau(v0)
   return (2*tau(vm(geomdv,vm(v0,v0)))-F2*tau(vm(v0,v0))
           -4*tv*tau(vm(geomdv,v0))+2*F2*tv**2+tau(vm(v0,DK(v0))))
  def P2(v0):
   cc=va(v0,vs(-tau(v0),unitvec))
   return tau(vm(vm(cc,cc),cc))
  V=[eo,Eunit(wval),Eunit(hval),Eunit(hval)]
  assert tau(V)==Eunit(lamb)
  assert tau(vm(V,V))==Eunit(2*lamb*lamb)
  assert tau(vm(vm(V,V),V))==Eunit(4*lamb*lamb*lamb)
  assert N4(V)==ez and mean(0)==ez
  assert P2(rows[0])==Eunit(Pv02)
  assert N4(rows[0])==Eunit(2*lamb*Pv02)
  xc=va(rows[0],vs(-tau(rows[0]),unitvec))
  yc=va(rows[1],vs(-tau(rows[1]),unitvec))
  Pj=3*tau(vm(vm(xc,xc),yc))
  assert Pj==Eunit(3*wval*Pv02)
  n1=N4(va(rows[0],rows[1]))-N4(rows[0])-N4(rows[1])-Eunit(lamb*C(fmpq(4,3)))*Pj
  e1,eb,ec=mean(1),mean(2),mean(3)
  nb=N4(rows[2])-Eunit(2*lamb*Pv02*hval*hval)
  nc=N4(rows[3])-Eunit(2*lamb*Pv02*hval*hval)
  pb=P2(rows[2])-Eunit(Pv02*hval*hval*hval)
  pc=P2(rows[3])-Eunit(Pv02*hval*hval*hval)
  assert not e1.b and not n1.b
  assert eb.conj()==ec and nb.conj()==nc and pb.conj()==pc
  original=[("E1",e1.a.c),("EBe",eb.a.c),("EBo",eb.b.c),("N1",n1.a.c),
            ("NBe",nb.a.c),("NBo",nb.b.c),("PBe",pb.a.c),("PBo",pb.b.c)]
  say("new_Delta_zero_equal_weight_same_original_Gram_complete",
      case=label,lambdaDegree=int(phi.degree()),recoveredQ=Qvalue.data(),
      freeOriginalParameter="f",originalTRecoveredOnlyThroughPaid_bcQ_Sxi=True,
      E0N0P1OriginalNVAndAllMomentIdentitiesActuallyReturned=True,
      allEightOriginalRows=[dict(name=nn,fDegree=len(pp)-1) for nn,pp in original],
      noDeltaOrNormInverse=True,claimExcluded=False)
  gfinal=[];tr=[];done=[]
  for nn,pp in original:
   gnew,ss,tt=xgcd(gfinal,pp)
   tr=[mul(ss,tag) for tag in tr]+[tt];done.append((nn,pp));gfinal=gnew
   returned=[]
   for tag,(_,row) in zip(tr,done):returned=add(returned,mul(tag,row))
   assert returned==gfinal
   say("new_Delta_zero_equal_weight_original_free_f_Bezout",
       case=label,newOriginalRow=nn,currentFDegree=len(gfinal)-1,
       allOriginalCoefficientProductsReturned=True,claimExcluded=False)
   if len(gfinal)==1:break
  cert=dict(lambdaFactor=[str(cc) for cc in phi.coeffs()],Qvalue=Qvalue.data(),
            compatibilityGcd=pdata(gg),compatibilityTags=[pdata(tt) for tt in ctags],
            originalRows=[dict(name=nn,coefficients=pdata(pp)) for nn,pp in done],
            originalTags=[pdata(tt) for tt in tr],finalFPolynomial=pdata(gfinal))
  blob=json.dumps(cert,separators=(",",":")).encode()
  out=dict(case=label,lambdaDegree=int(phi.degree()),excluded=len(gfinal)==1,
           allLambdaRootsAndRecoveredQFibersRetained=True,
           originalRowsUsed=[nn for nn,_ in done],finalFPolynomial=small_profile(gfinal),
           certificateBytes=len(blob),certificateSHA256=hashlib.sha256(blob).hexdigest(),
           noDeltaOrUnpaidNormInverse=True)
  case_results.append(out);say("new_Delta_zero_equal_weight_original_full_return",**out)
 except ConstantSplit as ex:
  assert ex.g*ex.h==phi
  rec=dict(case=label,left=[str(c0) for c0 in ex.g.coeffs()],right=[str(c0) for c0 in ex.h.coeffs()],
           fullProductVerified=True,bothBranchesRetained=True)
  split_records.append(rec);say("new_Delta_zero_equal_weight_constant_nonunit_split",**rec)
  process_case(ex.g,label+"/left");process_case(ex.h,label+"/right")

process_case(QQ(["-3","52","-392","1470","-414","-29126","199932","-829326","2534173","-6080694","11783324","-18678024","24316352","-25940944","22500320","-15651136","8547840","-3547392","1058304","-202752","18432"]),'complete_lambda20')

signal.alarm(0)
say("new_Delta_zero_equal_weight_entire_original_QQ_return_complete",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    allFiniteOriginalReturns=case_results,completeConstantSplits=split_records,
    actualConstantInverseCount=inverse_count,actualPolynomialDivisionCount=division_count,
    originalDomain="h=k!=1,b=c,Delta=0",
    entireOriginalDeltaZeroEqualWeightExcluded=bool(case_results) and all(r["excluded"] for r in case_results),
    noDeltaInverseOrOldDNonzeroWeightTheorem=True,
    genericUnequalWeightEqualValueChartStillOpen=True,ordinaryISPClaim=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
