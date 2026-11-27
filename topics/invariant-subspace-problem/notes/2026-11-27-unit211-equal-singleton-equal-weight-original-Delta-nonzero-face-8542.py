#!/usr/bin/env python3
"""New original equal-weight face b=c on h=k!=1, Delta!=0.
This D=0 value collision was not closed by the old D!=0 equal-weight theorem.
Set u=ell before constructing the same full original Gram. Preserve Delta=0.
Return exact factors and fixed QQ Q-resultant covers, with all heads retained.
180s/4GiB. No physical D, T0, Pf or norm inverse.
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
H=bc*Delta;fnum=bc*F;tnum=Tnum/Q
W1P=T0*Delta/2+2*u*F
W2P=(u*T0+lam*P02)*Delta+(V2+2*u*u)*F-Tnum
ivdiff=E(0,-1/(2*disc))
assert ivdiff*(q-p)==1
Xnum=c*q*ivdiff*(q*W1P-E(W2P))/Q
Ynum=b*p*ivdiff*(E(W2P)-p*W1P)/Q
assert b*p*(q-p)*Xnum==E(bc)*(q*W1P-E(W2P))
assert c*q*(q-p)*Ynum==E(bc)*(E(W2P)-p*W1P)
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
say("new_equal_singleton_invariant_weight_original_system",
    parameters=["lambda","Q"],newOriginalFace="b=c, u=ell inside h=k and Delta!=0",quadraticSymbol="rho^2=1-Q",
    originalScale="H=bc*Delta",oldMomentParameterizationOnlyReused=True,
    E0N0P1AndOriginalNVActuallyVerified=True,
    sameOriginalBothSingletonHighestAndGradientTargets=True,
    bothOriginalRowsUsedForEachCoefficientPair=True,
    coefficientZeroEquivalenceUsesTwoActualRowsAndRhoNonzero=True,
    noDOrT0PfSNormInverse=True,claimExcluded=False)
atoms=[("A2",A.n),("B3",B.n),("Q",Qp),("rho_squared",disc.n)]
def audit_den(pp):
 assert pp;rr=pp
 for name,atom in atoms:
  while True:
   gg=rr.gcd(atom)
   if gg.total_degree()==0:break
   qq=rr/gg;assert qq*gg==rr;rr=qq
 assert rr.total_degree()==0,("unpaid coefficient denominator",str(rr))
def profile(pp):
 ss=str(pp).encode()
 return dict(degrees_lambda_Q=list(map(int,pp.degrees())),
             totalDegree=int(pp.total_degree()),terms=len(pp.to_dict()),
             bytes=len(ss),sha256=hashlib.sha256(ss).hexdigest())
physical_atoms=atoms+[("lambda",Lp),("original_bc",bc.n),
                      ("original_P02",P02.n),("chart_Delta_nonzero",Delta.n),("previous_whole_S_zero_excluded",S.n)]
def primitive(rr):
 rr=R(rr);audit_den(rr.d);pp=rr.n
 if not pp:return pp,[]
 original=pp;prod=oneP;hist=[]
 for name,atom in physical_atoms:
  count=0
  while True:
   gg=pp.gcd(atom)
   if gg.total_degree()==0:break
   old=pp;pp=pp/gg;assert pp*gg==old;prod=prod*gg;count+=1
  if count:hist.append(dict(name=name,count=count))
 scalar=pp.coefficient(0);pp=pp/scalar
 assert pp*scalar*prod==original
 return pp,hist
actual=[("E1",E1.a),("EBe",EB.a),("EBo",EB.b),("N1",n1.a),
        ("NBe",NB.a),("NBo",NB.b),("PBe",PB.a),("PBo",PB.b)]
allcores={}
for name,rr in actual:
 core,removed=primitive(rr);allcores[name]=core
 say("new_invariant_weight_complete_original_scalar_row",
     name=name,rawNumerator=profile(rr.n),primitive=profile(core),
     paidOnlyRemoval=removed,fullScaleProductVerified=True,
     allOriginalValuePairsRetained=True,claimExcluded=False)
Lmean=(u-ell)*EB.a+ell*disc*EB.b
Lcore,Lremoved=primitive(Lmean)
say("new_invariant_weight_actual_linear_mean_combination",
    originalCombination="(u-ell)*EBe+ell*(1-Q)*EBo",
    primitive=profile(Lcore),paidOnlyRemoval=Lremoved,
    noNonlinearTraceReplaced=True,claimExcluded=False)

# These are new original b=c fibers in the D=0 value collision.
# The old equal-weight exclusion in the D!=0 chart is not imported.
from flint import fmpq_poly
def factor_record(pp):
 if not pp:return dict(zero=True,fullQQProductActuallyReturned=True)
 content,factors=pp.factor()
 product=ctx.constant(content);records=[]
 for ff,mult in factors:
  product*=ff**int(mult)
  rec=dict(power=int(mult),profile=profile(ff))
  ss=str(ff)
  if len(ss.encode())<=8192:rec["polynomial"]=ss
  records.append(rec)
 assert product==pp
 return dict(content=str(content),factors=records,fullQQProductActuallyReturned=True)
for name,pp in allcores.items():
 say("new_equal_value_equal_weight_original_factorization",
     name=name,primitive=profile(pp),factorization=factor_record(pp),
     onlyOriginalPhysicalUnitsRemoved=True,
     wholeDeltaZeroFaceRetained=True,claimExcluded=False)
gall=next(iter(allcores.values()))
for pp in list(allcores.values())[1:]:gall=gall.gcd(pp)
say("new_equal_value_equal_weight_full_original_core_gcd",
    profile=profile(gall),factorization=factor_record(gall),
    noEmptinessOrFinitenessFromMultivariateGcd=True,claimExcluded=False)
def as_univariate(pp):
 assert all(int(m[1])==0 for m in pp.to_dict())
 dd=int(pp.degrees()[0]) if pp else -1
 cc=[fmpq(0)]*(dd+1)
 for m,a0 in pp.to_dict().items():cc[int(m[0])]=a0
 return fmpq_poly(cc)
def qprofile(pp):
 ss=json.dumps([str(c0) for c0 in pp.coeffs()],separators=(",",":")).encode()
 out=dict(degree=int(pp.degree()),bytes=len(ss),sha256=hashlib.sha256(ss).hexdigest())
 if len(ss)<=8192:out["coefficients"]=[str(c0) for c0 in pp.coeffs()]
 return out
def coefficient_Q(pp,exponent):
 return ctx.from_dict({(int(m[0]),0):a0 for m,a0 in pp.to_dict().items() if int(m[1])==exponent})
def fixed_sylvester_input(aa,bb):
 da,db=int(aa.degrees()[1]),int(bb.degrees()[1])
 assert da>0 and db>0
 ac=[coefficient_Q(aa,j) for j in range(da+1)]
 bc0=[coefficient_Q(bb,j) for j in range(db+1)]
 assert sum((cc*Qp**j for j,cc in enumerate(ac)),zeroP)==aa
 assert sum((cc*Qp**j for j,cc in enumerate(bc0)),zeroP)==bb
 matrix=[]
 for coeff,shifts,original in [(ac,db,aa),(bc0,da,bb)]:
  for shift in range(shifts):
   row=[zeroP]*(da+db)
   for j,cc in enumerate(coeff):row[j+shift]=cc
   assert sum((cc*Qp**j for j,cc in enumerate(row)),zeroP)==original*Qp**shift
   matrix.append(row)
 assert len(matrix)==da+db
 return da+db
def paid_scalar_projection(pp):
 # A scalar lambda divisor can only be removed if it divides an actually
 # nonzero original physical numerator in this same Delta!=0 chart.
 out=pp;product=oneP;removed=[]
 for name,atom in physical_atoms:
  count=0
  while out:
   gg=out.gcd(atom)
   if gg.total_degree()==0:break
   qq=out/gg;assert qq*gg==out
   out=qq;product*=gg;count+=1
  if count:removed.append(dict(name=name,gcdLoops=count))
 assert out*product==pp
 return as_univariate(out),removed
names_sorted=sorted(allcores,key=lambda name:(int(allcores[name].degrees()[1]),len(allcores[name].to_dict()),name))
zeroQ=fmpq_poly([]);oneQ=fmpq_poly([1])
gcd_projection=zeroQ;projection_inputs=[];projection_tags=[];projection_names=[]
def add_projection(label,rr,removal):
 global gcd_projection,projection_tags
 gg,aa,bb=gcd_projection.xgcd(rr)
 assert aa*gcd_projection+bb*rr==gg
 projection_tags=[aa*tt for tt in projection_tags]+[bb]
 projection_inputs.append(rr);projection_names.append(label);gcd_projection=gg
 assert sum((tt*ff for tt,ff in zip(projection_tags,projection_inputs)),zeroQ)==gg
 say("new_equal_value_equal_weight_actual_QQ_projection_gcd",
     input=label,inputProfile=qprofile(rr),paidOnlyRemoval=removal,
     currentCover=qprofile(gg),
     allUnivariateBezoutProductsActuallyReturned=True,
     noOriginalLeadingZeroFiberDeleted=True,claimExcluded=False)
for name in names_sorted:
 pp=allcores[name]
 if int(pp.degrees()[1])==0:
  rr,removed=paid_scalar_projection(pp)
  add_projection("original_scalar_"+name,rr,removed)
  if gcd_projection.degree()==0:break
projected=0
if gcd_projection.degree()!=0:
 for ii,na in enumerate(names_sorted):
  if projected>=4 or gcd_projection.degree()==0:break
  for nb in names_sorted[ii+1:]:
   if projected>=4 or gcd_projection.degree()==0:break
   aa,bb=allcores[na],allcores[nb]
   if int(aa.degrees()[1])<=0 or int(bb.degrees()[1])<=0:continue
   if aa.gcd(bb).total_degree()!=0:continue
   order=fixed_sylvester_input(aa,bb)
   say("new_equal_value_equal_weight_fixed_QQ_projection_begin",
       rows=[na,nb],fixedOrder=order,inputs=[profile(aa),profile(bb)],
       allFixedRowsReturnedToOriginalInputs=True,
       allLeadingZeroFibersRetained=True,claimExcluded=False)
   raw=aa.resultant(bb,"Q")
   assert raw and all(int(m[1])==0 for m in raw.to_dict())
   rr,removed=paid_scalar_projection(raw)
   say("new_equal_value_equal_weight_complete_fixed_QQ_projection",
       rows=[na,nb],fixedOrder=order,rawProjection=qprofile(as_univariate(raw)),
       retainedProjection=qprofile(rr),paidOnlyRemoval=removed,
       noUncomputedCoefficientCertificateClaim=True,claimExcluded=False)
   add_projection("Res_Q_"+na+"_"+nb,rr,removed);projected+=1
if gcd_projection:
 gcd_projection=gcd_projection/gcd_projection[gcd_projection.degree()]
 content,factors=gcd_projection.factor();back=fmpq_poly([content])
 ffrec=[]
 for ff,mult in factors:
  back*=ff**int(mult);ffrec.append(dict(power=int(mult),profile=qprofile(ff)))
 assert back==gcd_projection
else:ffrec=[]
signal.alarm(0)
say("new_equal_value_equal_weight_original_QQ_cover_complete",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    newOriginalDomain="h=k!=1, b=c, Delta!=0",
    exactLambdaCover=qprofile(gcd_projection),exactQQFactors=ffrec,
    actualProjectionNames=projection_names,
    originalDeltaNonzeroEqualWeightFaceExcluded=bool(gcd_projection) and gcd_projection.degree()==0,
    allEightOriginalConditionsRetained=True,
    allParameterLeadingZeroFibersRetained=True,
    DeltaZeroStillRequiresSeparateOriginalReturn=True,
    genericUnequalWeightFaceStillOpen=True,ordinaryISPClaim=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
