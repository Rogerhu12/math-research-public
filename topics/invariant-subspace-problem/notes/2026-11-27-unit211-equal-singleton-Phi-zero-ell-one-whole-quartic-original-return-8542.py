#!/usr/bin/env python3
"""New whole h=k,Phi=0,ell=1,u=2 quartic constant-fiber return.
The ell=1 collision relation leaves all roots of
8 lambda^4-24 lambda^3+24 lambda^2-12 lambda+3.
Keep free original Q and rebuild the same unscaled eight Gram rows.
All Q denominators are returned to true original units; full K[Q]
Bezout includes every lambda embedding and all Q leading-zero fibers.
No original Delta=0 assumptions. 180 seconds / 4 GiB.
"""
import json,time,hashlib,signal,resource
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
  r=dict(Qdegree=len(pp)-1,bytes=len(blob),sha256=hashlib.sha256(blob).hexdigest())
  if len(blob)<=8192:r["coefficients_Q_then_lambda"]=pdata(pp)
  return r

 try:
  lamb=C([0,1])
  class R:
   def __init__(self,n=0,d=None,reduce=True):
    if isinstance(n,R):self.n=n.n[:];self.d=n.d[:];return
    def cv(x):
     if isinstance(x,(list,tuple)):return trim([C(v) for v in x])
     v=C(x);return [v] if v else []
    nn=cv(n);dd=[one] if d is None else cv(d);assert dd
    if not nn:self.n=[];self.d=[one];return
    if reduce:
     gg,ss,tt=xgcd(nn,dd)
     qq,rr=divrem(nn,gg);assert not rr;nn=qq
     qq,rr=divrem(dd,gg);assert not rr;dd=qq
    iv=dd[-1].inv();self.n=scale(nn,iv);self.d=scale(dd,iv)
   def __bool__(self):return bool(self.n)
   def __neg__(self):return R(neg(self.n),self.d,False)
   def __add__(self,v):
    if getattr(v,"_isp_quotient_level",0)>0:return NotImplemented
    v=R(v)
    if not self:return v
    if not v:return self
    return R(add(mul(self.n,v.d),mul(v.n,self.d)),mul(self.d,v.d))
   __radd__=__add__
   def __sub__(self,v):
    if getattr(v,"_isp_quotient_level",0)>0:return NotImplemented
    return self+-R(v)
   def __rsub__(self,v):
    if getattr(v,"_isp_quotient_level",0)>0:return NotImplemented
    return R(v)+-self
   def __mul__(self,v):
    if getattr(v,"_isp_quotient_level",0)>0:return NotImplemented
    v=R(v)
    if not self or not v:return R()
    return R(mul(self.n,v.n),mul(self.d,v.d))
   __rmul__=__mul__
   def __truediv__(self,v):
    if getattr(v,"_isp_quotient_level",0)>0:return NotImplemented
    v=R(v);assert v
    return self*R(v.d,v.n,False)
   def __rtruediv__(self,v):
    if getattr(v,"_isp_quotient_level",0)>0:return NotImplemented
    return R(v)/self
   def __pow__(self,n):
    assert isinstance(n,int)
    if n<0:return R(self.d,self.n,False)**(-n)
    out=R(1);cur=self
    while n:
     if n&1:out=out*cur
     n>>=1
     if n:cur=cur*cur
    return out
   def __eq__(self,v):
    if getattr(v,"_isp_quotient_level",0)>0:return NotImplemented
    v=R(v);return mul(self.n,v.d)==mul(v.n,self.d)
   def data(self):return dict(numerator=pdata(self.n),denominator=pdata(self.d))
  lam=R(lamb);u=R(2);Q=R([z,one])

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
  xi=B/A;ell=A**3/(B*B);T=A*A/B;w=lam-1-T
  assert ell==1 and B*B-A**3==0
  disc=1-Q
  hh=1+xi;S=2*xi+3-2*lam;eta=xi+3-2*lam
  p=E(1,1);q=p.conj()
  b=E(ell/2,(u-ell)/(2*disc));c=b.conj();a=E(1-ell)
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
  assert Phi==0 and T0==-Q-4 and J-Q==-4
  assert P02==2*Q and Pf==4*(Q+4) and bc==-Q/(4*disc)
  assert Delta==-S*xi*Pf
  f=-Pc/Pf;tnum=-(NC+NF*f)/(bc*Q*S*xi)
  assert Pc+Pf*f+bc*Q*Phi*tnum==0
  assert NC+NF*f+bc*Q*S*xi*tnum==0
  say("new_Phi_zero_ell_one_entire_quartic_original_base",
      lambdaPolynomial=[3,-12,24,-24,8],allLambdaEmbeddingsRetained=True,
      originalU=2,freeOriginalParameter="Q",originalQUnits=["Q","1-Q","Q+4"],
      PhiZeroAndWholeEllOneOriginalRelationsActuallyReturned=True,
      noOldDNonzeroTheorem=True,claimExcluded=False)

  H=R(1);fnum=f
  W1=T0/2+2*u*fnum
  W2=u*T0+lam*P02+(V2+2*u*u)*fnum-bc*Q*tnum
  ivdiff=E(0,-1/(2*disc))
  assert ivdiff*(q-p)==1
  Xnum=c*q*ivdiff*(q*W1-E(W2))/(bc*Q)
  Ynum=b*p*ivdiff*(E(W2)-p*W1)/(bc*Q)
  rg=Xnum-a*p*H-c*tnum
  sg=Ynum-a*q*H-b*tnum
  AA=2*E(fnum)-2*b*Xnum-2*c*Ynum+E(2*bc*tnum)
  rows=[[E(),E(),p*H,q*H],[E(),AA,rg,sg],
        [p*H,rg,E(),E(tnum)],[q*H,sg,E(tnum),E()]]
  one=[E(1),E(),E(1),E(1)]
  def va(x,y):return [a+b for a,b in zip(x,y)]
  def vs(a,x):return [a*b for b in x]
  def vm(x,y):return [x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[2]*y[2],x[3]*y[3]]
  def tau(x):return a*x[0]+x[1]+b*x[2]+c*x[3]
  def DK(x):return [tau(vm(row,x)) for row in rows]
  dv=DK(one);F2=tau(dv);Kd=DK(dv)
  assert F2==E(2*fnum)
  def mean(j):
   ee=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
   return ee-2*Kd[j]-2*vm(dv,dv)[j]+2*F2*dv[j]
  def N4(x):
   tv=tau(x)
   return (2*tau(vm(dv,vm(x,x)))-F2*tau(vm(x,x))
           -4*tv*tau(vm(dv,x))+2*F2*tv**2+tau(vm(x,DK(x))))
  def P2(x):
   cc=va(x,vs(-tau(x),one));return tau(vm(vm(cc,cc),cc))
  V=[E(1),E(w),E(hh),E(hh)]
  assert tau(V)==E(lam)
  assert tau(vm(V,V))==E(2*lam*lam)
  assert tau(vm(vm(V,V),V))==E(4*lam**3)
  assert N4(V)==0
  assert mean(0)==0
  H3=H**3
  assert P2(rows[0])==E(P02*H3)
  assert N4(rows[0])==E(2*lam*P02*H3)
  x,y=rows[0],rows[1]
  xc=va(x,vs(-tau(x),one));yc=va(y,vs(-tau(y),one))
  Pj=3*tau(vm(vm(xc,xc),yc))
  assert Pj==E(3*w*P02*H3)
  Nv=N4(va(x,y))-N4(x)-N4(y)
  n1=Nv-E(4*lam/3)*Pj
  E1=mean(1);EB=mean(2);EC=mean(3)
  NB=N4(rows[2])-E(2*lam*P02*hh*hh*H3)
  NCrow=N4(rows[3])-E(2*lam*P02*hh*hh*H3)
  PB=P2(rows[2])-E(P02*hh**3*H3)
  PC=P2(rows[3])-E(P02*hh**3*H3)
  assert not E1.b and not n1.b
  assert EB.conj()==EC and NB.conj()==NCrow and PB.conj()==PC

  q_units=[("Q",Q.n),("rho_squared",disc.n),("previous_whole_T0_collision_excluded",T0.n)]
  def strip(pp):
   original=pp[:];product=[one];removed=[]
   for name,atom in q_units:
    count=0
    while pp:
     gg,ss,tt=xgcd(pp,atom)
     assert add(mul(ss,pp),mul(tt,atom))==gg
     if len(gg)<=1:break
     nn,rr=divrem(pp,gg);assert not rr
     pp=nn;product=mul(product,gg);count+=1
    if count:removed.append(dict(originalUnit=name,gcdLoops=count))
   assert mul(pp,product)==original
   return pp,removed
  actual=[("E1",E1.a),("EBe",EB.a),("EBo",EB.b),("N1",n1.a),
          ("NBe",NB.a),("NBo",NB.b),("PBe",PB.a),("PBo",PB.b)]
  cores=[];rowrecords=[]
  for name,rr in actual:
   den,removed_den=strip(rr.d)
   assert len(den)==1,("unpaid_original_Q_denominator",name,pdata(den))
   pp,removed_num=strip(rr.n)
   cores.append((name,pp))
   rowrecords.append(dict(name=name,rawQDegree=len(rr.n)-1,
                          primitiveQDegree=len(pp)-1,
                          onlyPaidNumeratorRemovals=removed_num,
                          wholeOriginalDenominatorReturned=True,
                          primitive=small_profile(pp)))
  say("new_Phi_zero_ell_one_all_original_rows",
      case=label,lambdaDegree=int(phi.degree()),allEightOriginalRows=rowrecords,
      allE0N0P1NVMomentsAndBothSingletonTargetsActuallyReturned=True,
      bothActualRowsAndRhoNonzeroPayEvenOddExtraction=True,
      allQAndLambdaHeadZeroFibersRetained=True,claimExcluded=False)
  gg=[];tags=[];done=[]
  for name,pp in cores:
   newg,ss,tt=xgcd(gg,pp)
   tags=[mul(ss,tag) for tag in tags]+[tt]
   done.append((name,pp));gg=newg
   check=[]
   for tag,(_,ip) in zip(tags,done):check=add(check,mul(tag,ip))
   assert check==gg
   say("new_Phi_zero_ell_one_original_Q_Bezout",
       newOriginalRow=name,QDegree=len(gg)-1,wholeCombinationActuallyReturned=True)
   if len(gg)==1:break
  cert=dict(lambdaFactor=[str(cc) for cc in phi.coeffs()],originalU=2,
            originalRows=[dict(name=nn,coefficients=pdata(pp)) for nn,pp in done],
            tags=[pdata(tt) for tt in tags],finalQPolynomial=pdata(gg))
  bb=json.dumps(cert,separators=(",",":")).encode()
  out=dict(case=label,lambdaDegree=int(phi.degree()),excluded=len(gg)==1,
           originalRowsUsed=[nn for nn,pp in done],finalQPolynomial=pdata(gg),
           allLambdaEmbeddingsRetained=True,allOriginalQUnitFibersAccounted=True,
           certificateBytes=len(bb),certificateSHA256=hashlib.sha256(bb).hexdigest(),
           fullCertificate=cert if len(bb)<=16000 else None)
  case_results.append(out);say("new_Phi_zero_ell_one_full_original_return",**out)
 except ConstantSplit as ex:
  assert ex.g*ex.h==phi
  rec=dict(case=label,left=[str(cc) for cc in ex.g.coeffs()],
           right=[str(cc) for cc in ex.h.coeffs()],bothBranchesRetained=True)
  split_records.append(rec);say("new_Phi_zero_ell_one_constant_nonunit_split",**rec)
  process_case(ex.g,label+"/left");process_case(ex.h,label+"/right")

phi=QQ([3,-12,24,-24,8])
assert phi.gcd(phi.derivative()).degree()==0
process_case(phi,"complete_lambda_quartic")
signal.alarm(0)
say("new_Phi_zero_ell_one_entire_original_return_complete",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    originalDomain="h=k!=1,Phi=0,ell=1,u=2",
    allOriginalReturns=case_results,constantSplits=split_records,
    entireOriginalFaceExcluded=bool(case_results) and all(x["excluded"] for x in case_results),
    actualConstantInverseCount=inverse_count,actualPolynomialDivisionCount=division_count,
    complementaryEllNononeFaceRequiresIndependentReturn=True,ordinaryISPClaim=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
