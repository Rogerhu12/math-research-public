#!/usr/bin/env python3
"""New whole h=k,Q=1-u,Delta=0 finite ORIGINAL Gram return.
Use both complete QQ lambda factors C6 and C24 of the actual original
compatibility cover. Reconstruct only the frozen affine-input prefix;
no old projections are rerun. Whole K[u] gcd retains every u root.
If it is linear, recover that same u and retain free original f in all
eight original Gram rows. Any genuinely quadratic remaining u fiber is
explicitly retained, not discarded. 180 seconds / 4 GiB.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq,fmpq_poly
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start)
 print(json.dumps(kw),flush=True)
def QQ(v=()):return fmpq_poly([fmpq(x) for x in v])
QZ=QQ();QO=QQ([1])
class ConstantSplit(Exception):
 def __init__(self,g,h):self.g=g;self.h=h
case_results=[];split_records=[];inverse_count=0;division_count=0
deadline=start+180
dep=Path(__file__).with_name("2026-11-27-unit211-equal-singleton-Q1u-Delta-zero-original-compatibility-cover-8542.py")
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="2298408cf56888d710f4a22d74026a81b2d900aca84541148459ea4eacfe6ab2"
marker=b"\nactual=["
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
ns={"__file__":str(dep),"__name__":"__new_finite_original_Q1u_input__"}
prefixlog=io.StringIO()
with contextlib.redirect_stdout(prefixlog):
 exec(compile(prefix,str(dep),"exec"),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
actual=[("Delta",ns["Delta"]),("F",ns["F"]),("Tnum",ns["Tnum"])]
for name,rr in actual:ns["audit_den"](rr.d)
original_units=ns["paid_atoms"]
say("new_Q1u_Delta_zero_complete_affine_finite_input",
    originalInputSourceSHA256=hashlib.sha256(raw).hexdigest(),
    onlyRawConstructionPrefixSHA256=hashlib.sha256(prefix).hexdigest(),
    noOldOriginalFactorizationOrProjectionGateReplayed=True,
    allThreeOriginalCompatibilityPolynomialsReconstructed=True,
    allOriginalTwoRowEliminationIdentitiesReturned=True,
    completeLambdaFactorDegrees=[6,24],claimExcluded=False)

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
  r=dict(uDegree=len(pp)-1,bytes=len(blob),sha256=hashlib.sha256(blob).hexdigest())
  if len(blob)<=8192:r["coefficients_u_then_lambda"]=pdata(pp)
  return r

 try:
  units=[]
  for name,ap in original_units:
   pp=from_mpoly(ap)
   if not pp:
    out=dict(case=label,lambdaDegree=int(phi.degree()),excluded=True,
             excludedByEntireOriginalUnitZero=name,
             allLambdaEmbeddingsRetained=True)
    case_results.append(out);say("new_Q1u_Delta_zero_whole_original_unit_zero",**out)
    return
   units.append((name,pp))
  def strip(pp):
   original=pp[:];product=[one];records=[]
   for name,ap in units:
    count=0
    while pp:
     gg,ss,tt=xgcd(pp,ap)
     assert add(mul(ss,pp),mul(tt,ap))==gg
     if len(gg)<=1:break
     nn,rr=divrem(pp,gg);assert not rr
     pp=nn;product=mul(product,gg);count+=1
    if count:records.append(dict(originalUnit=name,gcdLoops=count))
   assert mul(pp,product)==original
   return pp,records
  gg=[];ctags=[];cinputs=[];crecords=[]
  for name,rr in actual:
   den=from_mpoly(rr.d);assert den
   rem,_=strip(den);assert len(rem)==1,("unpaid original affine denominator",name)
   pp,removed=strip(from_mpoly(rr.n))
   newg,ss,tt=xgcd(gg,pp)
   ctags=[mul(ss,tag) for tag in ctags]+[tt]
   cinputs.append((name,pp));gg=newg
   check=[]
   for tag,(_,ip) in zip(ctags,cinputs):check=add(check,mul(tag,ip))
   assert check==gg
   crecords.append(dict(name=name,onlyPaidRemovals=removed,primitive=small_profile(pp)))
  say("new_Q1u_Delta_zero_complete_original_compatibility_return",
      case=label,lambdaDegree=int(phi.degree()),originalRows=crecords,
      fullCompatibilityGcd=small_profile(gg),allBezoutProductsReturned=True,
      allOriginalUnitRemovalsReturned=True,claimExcluded=False)
  if len(gg)==1:
   out=dict(case=label,lambdaDegree=int(phi.degree()),excluded=True,
            originalCompatibilityUnit=True,allLambdaAndURootsRetained=True)
   case_results.append(out);say("new_Q1u_Delta_zero_compatibility_unit_exclusion",**out)
   return
  if len(gg)!=2:
   out=dict(case=label,lambdaDegree=int(phi.degree()),excluded=False,
            remainingWholeUPolynomial=pdata(gg),
            originalGramStillRequiresReturn=True,
            allLambdaAndURootsRetained=True)
   case_results.append(out);say("new_Q1u_Delta_zero_higher_u_fiber_retained",**out)
   return
  uv=-gg[0]/gg[1]
  assert gg[0]+gg[1]*uv==0
  def evpoly(pp):
   out=z
   for cc in reversed(from_mpoly(pp)):out=out*uv+cc
   return out
  def evr(rr):
   nn=evpoly(rr.n);dd=evpoly(rr.d);assert dd
   return nn/dd
  for name,ap in original_units:
   val=evpoly(ap)
   if not val:
    out=dict(case=label,lambdaDegree=int(phi.degree()),excluded=True,
             recoveredOriginalU=uv.data(),
             excludedByRecoveredOriginalUnitZero=name,
             allLambdaAndURootsRetained=True)
    case_results.append(out);say("new_Q1u_Delta_zero_recovered_original_unit_zero",**out)
    return
   assert val*val.inv()==one
  for name,rr in actual:assert evr(rr)==z
  lamb=C([0,1])
  lv=evr(ns["ell"]);Tv=evr(ns["T"]);xiv=evr(ns["xi"])
  wval=evr(ns["w"]);Sv=evr(ns["S"]);etav=evr(ns["eta"]);hval=1+xiv
  Qv=1-uv;dv0=uv
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
  for name,cc in [("Q",Qv),("rho2",dv0),("bc",bcv),("Phi",Phiv),("Pf",Pfv),("S",Sv)]:
   assert cc,name
   assert cc*cc.inv()==one
  say("new_Q1u_Delta_zero_same_original_u_recovered",
      case=label,lambdaDegree=int(phi.degree()),recoveredU=uv.data(),
      QequalsOneMinusSameU=True,originalDeltaAndBothCompatibilityRowsReturned=True,
      noDeltaOrNFInverse=True,freeOriginalParameter="f",claimExcluded=False)
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
  say("new_Q1u_Delta_zero_finite_same_original_Gram_complete",
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
   say("new_Q1u_Delta_zero_finite_free_f_original_Bezout",
       newOriginalRow=nn,fDegree=len(gfinal)-1,
       allOriginalCoefficientProductsReturned=True)
   if len(gfinal)==1:break
  cert=dict(lambdaFactor=[str(cc) for cc in phi.coeffs()],originalU=uv.data(),compatibilityGcd=pdata(gg),
            compatibilityOriginalRows=[dict(name=nn,coefficients=pdata(pp)) for nn,pp in cinputs],
            compatibilityTags=[pdata(tt) for tt in ctags],
            originalRows=[dict(name=nn,coefficients=pdata(pp)) for nn,pp in done],
            tags=[pdata(tt) for tt in tags],finalFPolynomial=pdata(gfinal))
  blob=json.dumps(cert,separators=(",",":")).encode()
  out=dict(case=label,lambdaDegree=int(phi.degree()),excluded=len(gfinal)==1,
           originalRowsUsed=[nn for nn,pp in done],
           finalFPolynomial=pdata(gfinal),allLambdaEmbeddingsRetained=True,
           certificateBytes=len(blob),certificateSHA256=hashlib.sha256(blob).hexdigest(),
           fullCertificate=cert if len(blob)<=16000 else None)
  case_results.append(out);say("new_Q1u_Delta_zero_finite_full_original_return",**out)
 except ConstantSplit as ex:
  assert ex.g*ex.h==phi
  rec=dict(case=label,left=[str(cc) for cc in ex.g.coeffs()],
           right=[str(cc) for cc in ex.h.coeffs()],bothBranchesRetained=True)
  split_records.append(rec);say("new_Q1u_Delta_zero_finite_constant_nonunit_split",**rec)
  process_case(ex.g,label+"/left");process_case(ex.h,label+"/right")

factors=[
 [2,-12,39,-76,96,-72,24],
 [-18,399,-4412,32152,-171905,710808,-2332482,6112826,-12570078,18848763,
 -14402138,-21172682,111728893,-266613390,460231700,-629475832,702614944,
 -645322096,486216224,-296971456,143911680,-53435136,14348800,-2500608,215040]
]
for coefficients in factors:
 pp=QQ(coefficients);assert pp.gcd(pp.derivative()).degree()==0
 process_case(pp,"complete_lambda_degree_"+str(pp.degree()))
signal.alarm(0)
say("new_Q1u_Delta_zero_complete_original_finite_return",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    originalDomain="h=k!=1,Q=1-u,Delta=0",
    allOriginalReturns=case_results,constantSplits=split_records,
    allTwoCompleteLambdaFactorsProcessed=True,
    entireOriginalFaceExcluded=bool(case_results) and all(x["excluded"] for x in case_results),
    actualConstantInverseCount=inverse_count,actualPolynomialDivisionCount=division_count,
    noDeltaInverse=True,ordinaryISPClaim=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
