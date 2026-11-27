#!/usr/bin/env python3
"""New complete lambda^2-lambda+1/3 h=k Delta-zero original compatibility.
NF=(4*lambda-3)*(J-Q) exactly, and Delta=(J-Q)*xi*Dlin.
The Q head T+eta is an actual constant-field unit. Keep every u root,
remove only original unit factors, and return the same original Gram if
the complete residual is linear. A nonlinear residual remains open.
120 seconds / 1 GiB. No old QQ projection is replayed."""
import json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_poly
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
start=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start)
 print(json.dumps(kw),flush=True)
def QQ(v=()):return fmpq_poly([fmpq(x) for x in v])
class ConstantSplit(Exception):pass
inverse_count=0;division_count=0
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
  def __truediv__(self,v):return self*C(v).inv()
  def __rtruediv__(self,v):return C(v)*self.inv()
  def __pow__(self,n):
   assert isinstance(n,int) and n>=0
   out=C(1)
   for i in range(n):out=out*self
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

 def pdata(pp):return [cc.data() for cc in pp]
 def cooperate(fn):
  def call(self,other):
   if getattr(other,"_isp_level",0)>0:return NotImplemented
   return fn(self,other)
  return call
 for nn in ["__add__","__radd__","__sub__","__rsub__","__mul__","__rmul__","__truediv__","__rtruediv__","__eq__"]:
  setattr(C,nn,cooperate(getattr(C,nn)))
 try:
  class U:
   _isp_level=1
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
   def __truediv__(self,v):return self.scale(C(v).inv())
   def scale(self,v):return U(scale(self.c,C(v)))
   def __pow__(self,n):
    out=U(1)
    for i in range(n):out=out*self
    return out
   def __eq__(self,v):return self.c==U(v).c
  lamb=C([0,1]);Av=2*lamb*lamb-2*lamb+1
  Bv=4*lamb**3-6*lamb*lamb+3*lamb-1
  xiv=Bv/Av;lv=Av**3/(Bv*Bv);Tv=Av*Av/Bv
  wval=lamb-1-Tv;Sv=2*xiv+3-2*lamb;etav=xiv+3-2*lamb;hval=1+xiv
  assert xiv*etav==4*lamb-3
  assert etav-Sv==-xiv and lv*xiv==Tv
  head=Tv+etav
  assert head and head*head.inv()==one
  up=U([0,1]);Qpoly=-((up-1)*(up.scale(2*xiv)+4*etav))/head
  dp=1-Qpoly;mp=up-lv
  Vp2=2*up-lv*Qpoly;Tp0=Vp2-2*up*up
  Jp=2*up*(1-up)+lv*Qpoly;Phip=Tp0+4*up-4+Qpoly
  Pp02=(2-3*up)*Vp2-Qpoly*up+2*up**3
  Pfp=Tp0*(Jp-Qpoly);Gp=lamb*Pp02-(1-up)*Tp0
  Pcp=Qpoly*Pp02*(lv+Tv)-Gp*Tp0
  Nfp=(3-4*lamb)*Qpoly+Jp*xiv*etav
  Ncp=etav*(-Gp*xiv+Qpoly*wval*up)
  assert Nfp==(4*lamb-3)*(Jp-Qpoly)
  assert Phip*Nfp-Sv*xiv*Pfp==U()
  Tnp=Pfp*Ncp-Pcp*Nfp
  inner=Tp0*wval*up-xiv*Pp02*(lv+Tv)
  assert Tnp==Qpoly*etav*(Jp-Qpoly)*inner
  units=[("u",up),("u-1",up-1),("Q",Qpoly),("1-Q",dp),
         ("u-ell",mp),("bc numerator",lv*lv*dp-mp*mp),
         ("T0",Tp0),("J-Q",Jp-Qpoly),("Phi",Phip),
         ("P02",Pp02),("u+Q-1",up+Qpoly-1)]
  say("new_C2_entire_original_Q_graph",lambdaFactor=[str(x) for x in phi.coeffs()],
      originalQCoefficients_u_then_lambda=pdata(Qpoly.c),
      originalQHead=head.data(),headFullQQBezoutInverseReturned=True,
      NFOriginalFactorAndBothDeltaTnumProductsActuallyReturned=True,
      noUParameterInverse=True,allURootsRetained=True)
  for name,pp in units:
   if not pp:
    say("new_C2_entire_original_unit_zero",excluded=True,unit=name)
    return
  g=inner.c[:];product=[one];removals=[]
  for name,pp in units:
   while g:
    gg,ss,tt=xgcd(g,pp.c)
    if len(gg)<=1:break
    qq,rr=divrem(g,gg);assert not rr and mul(qq,gg)==g
    product=mul(product,gg);g=qq
    removals.append(dict(unit=name,degree=len(gg)-1))
  assert mul(product,g)==inner.c
  if g:g=scale(g,g[-1].inv())
  say("new_C2_whole_original_u_compatibility_return",
      residualUPolynomial=pdata(g),uDegree=len(g)-1,onlyOriginalUnitRemovals=removals,
      allWholePolynomialDivisionProductsReturned=True,claimExcluded=len(g)==1)
  if len(g)==1:return
  if len(g)!=2:
   say("new_C2_complete_nonlinear_u_fiber_retained",excluded=False,
       residualUPolynomial=pdata(g),originalGramStillRequired=True)
   return
  uv=-g[0]/g[1]
  def ev(pp):
   vv=z
   for cc in reversed(pp.c):vv=vv*uv+cc
   return vv
  Qv=ev(Qpoly);dv0=1-Qv
  assert ev(inner)==0
  for name,pp in units:
   vv=ev(pp)
   if not vv:
    say("new_C2_recovered_original_unit_zero",excluded=True,unit=name,recoveredU=uv.data())
    return
   assert vv*vv.inv()==one
  bcv=(lv*lv-(uv-lv)**2/dv0)/4
  Vv2=2*uv-lv*Qv;Tv0=Vv2-2*uv*uv
  Jv=2*uv*(1-uv)+lv*Qv;Phiv=Tv0+4*uv-4+Qv
  Pv02=(2-3*uv)*Vv2-Qv*uv+2*uv**3
  Pfv=Tv0*(Jv-Qv);Gv=lamb*Pv02-(1-uv)*Tv0
  Pcv=Qv*Pv02*(lv+Tv)-Gv*Tv0
  Nfv=(3-4*lamb)*Qv+Jv*xiv*etav
  Ncv=etav*(-Gv*xiv+Qv*wval*uv)
  assert Phiv*Nfv-Sv*xiv*Pfv==0
  assert Sv*xiv*Pcv-Phiv*Ncv==0
  assert Pfv*Ncv-Pcv*Nfv==0
  for name,cc in [("A",Av),("B",Bv),("lambda",lamb),("u",uv),("u-1",uv-1),("u-ell",uv-lv),("ell",lv),("P02",Pv02),("T0",Tv0),("J-Q",Jv-Qv),("u+Q-1",uv+Qv-1),("Q",Qv),("rho2",dv0),("bc",bcv),("Phi",Phiv),("Pf",Pfv),("S",Sv)]:
   assert cc,name
   assert cc*cc.inv()==one
  say("new_C2_Delta_zero_same_original_u_recovered",
      case=label,lambdaDegree=int(phi.degree()),recoveredU=uv.data(),
      originalQ=Qv.data(),QequalsOneMinusSameU=False,originalDeltaAndBothCompatibilityRowsReturned=True,
      noDeltaOrNFInverse=True,freeOriginalParameter="f",claimExcluded=False)
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
  free_t=-(free_f.scale(Pfv)+U(Pcv)).scale((bcv*Qv*Phiv).inv())
  assert free_f.scale(Pfv)+free_t.scale(bcv*Qv*Phiv)+U(Pcv)==U()
  assert free_f.scale(Nfv)+free_t.scale(bcv*Qv*Sv*xiv)+U(Ncv)==U()
  bp=lv*C(fmpq(1,2));bodd=(uv-lv)/(2*dv0)
  be=Eunit(bp,bodd);ce=be.conj();ae=Eunit(1-lv)
  pe=Eunit(1,1);qe=pe.conj()
  assert be+ce==Eunit(lv) and be*pe+ce*qe==Eunit(uv)
  assert be*ce==Eunit(bcv)
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
  say("new_C2_Delta_zero_finite_same_original_Gram_complete",
      case=label,lambdaDegree=int(phi.degree()),freeOriginalParameter="f",
      allEightOriginalRows=[dict(name=nn,fDegree=len(pp)-1) for nn,pp in original],
      allMomentE0N0P1NVAndBothSingletonTargetsReturned=True,
      coefficientPairsUseBothActualRowsAndRhoNonzero=True,claimExcluded=False)
  gfinal=[];tags=[];done=[]
  for nn,pp in original:
   gnew,ss,tt=xgcd(gfinal,pp)
   tags=[mul(ss,tag) for tag in tags]+[tt];done.append((nn,pp));gfinal=gnew
   check=[]
   for tag,(_,row) in zip(tags,done):check=add(check,mul(tag,row))
   assert check==gfinal
   say("new_C2_Delta_zero_finite_free_f_original_Bezout",
       newOriginalRow=nn,fDegree=len(gfinal)-1,
       allOriginalCoefficientProductsReturned=True)
   if len(gfinal)==1:break
  cert=dict(lambdaFactor=[str(cc) for cc in phi.coeffs()],originalU=uv.data(),originalQ=Qv.data(),
            originalUCompatibility=pdata(g),QGraph=pdata(Qpoly.c),
            originalRows=[dict(name=nn,coefficients=pdata(pp)) for nn,pp in original],
            usedOriginalRows=[nn for nn,pp in done],
            tags=[pdata(tt) for tt in tags],finalFPolynomial=pdata(gfinal))
  blob=json.dumps(cert,separators=(",",":")).encode()
  say("new_C2_whole_original_Gram_return",excluded=len(gfinal)==1,
      allEightOriginalRowsActuallyReturned=True,originalRowsUsed=[nn for nn,pp in done],
      finalFPolynomial=pdata(gfinal),allLambdaEmbeddingsAndFreeFValuesRetained=True,
      certificateBytes=len(blob),certificateSHA256=hashlib.sha256(blob).hexdigest(),
      fullCertificate=cert if len(blob)<=32000 else None,ordinaryISPClaim=False)
 except ConstantSplit:
  raise AssertionError("The exact irreducible C2 constant factor has no nonconstant split")
process_case(QQ(["1/3",-1,1]),"complete_lambda_C2_original_Delta_zero_fiber")
signal.alarm(0)
say("new_C2_entire_original_return_complete",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    actualConstantInverseCount=inverse_count,actualPolynomialDivisionCount=division_count,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
