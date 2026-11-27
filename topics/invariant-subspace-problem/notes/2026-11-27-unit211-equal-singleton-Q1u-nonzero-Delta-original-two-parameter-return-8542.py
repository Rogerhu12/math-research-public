#!/usr/bin/env python3
"""New original h=k,Q=1-u,Delta!=0 complete two-parameter return.
Use original P1/NV and every unscaled original Gram row. Previously
closed T0/JQ/Phi/equal-weight COLLISION faces supply only true units.
No old D!=0 weight theorem. The entire Delta=0 complementary face
is retained separately. Fixed QQ projections. 180s/4GiB.
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
ctx=fmpq_mpoly_ctx.get(("lam","u"),"lex")
Lp,up=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
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
lam,u=map(R,(Lp,up))
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
Q=1-u;disc=1-Q
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
F=S*xi*Pc-Phi*NC;Tnum=Pf*NC-Pc*NF
assert Pf*F+Phi*Tnum+Pc*Delta==0
assert NF*F+S*xi*Tnum+NC*Delta==0
assert disc==u
assert T0==(1-u)*(2*u-ell)
assert J-Q==(1-u)*(2*u+ell-1)
assert Phi==(1-u)*(2*u-ell-3)
assert P02==(1-u)*(-2*u*u+3*(ell+1)*u-2*ell)
Dshort=(2*u-ell-3)*(3-4*lam+(2*u+ell)*xi*eta)-S*xi*(2*u-ell)*(2*u+ell-1)
assert Delta==(1-u)**2*Dshort
assert all(int(ex[1])<=2 for ex in Dshort.n.to_dict())
assert all(int(ex[1])==0 for ex in Dshort.d.to_dict())
Dhead=ctx.from_dict({(int(ex[0]),0):cc for ex,cc in Dshort.n.to_dict().items() if int(ex[1])==2})
assert R(Dhead,Dshort.d)==-4*xi*xi
f=F/Delta;tnum=Tnum/(bc*Q*Delta)
assert f*Delta==F
assert Pc+Pf*f+bc*Q*Phi*tnum==0
assert NC+NF*f+bc*Q*S*xi*tnum==0

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

say("new_Q1u_nonzero_Delta_collision_original_system",
    actualOriginalDomain="h=k!=1,Q=1-u,Delta!=0",parameters=["lambda","u"],
    originalScale="unscaled H=1",bothOriginalAffineRowsActuallyReturned=True,
    E0N0P1NVAndAllOriginalMomentsActuallyReturned=True,
    allEightOriginalRowsAndBothSingletonTargetsRetained=True,
    originalQ1uIdentitiesActuallyReturned=True,
    entireDeltaZeroComplementRetained=True,
    noOldDNonzeroWeightTheorem=True,claimExcluded=False)
base_atoms=[("A2",A.n),("B3",B.n),("Q",Q.n),("rho_squared",disc.n),
            ("original_bc",bc.n),("explicit_Delta_nonzero_chart",Delta.n)]
paid_atoms=base_atoms+[("lambda",Lp),("original_P02",P02.n),
                      ("previous_whole_S_zero_excluded",S.n),
                      ("previous_whole_equal_weight_collision_excluded",(u-ell).n),
                      ("previous_whole_T0_collision_excluded",T0.n),
                      ("previous_whole_JQ_collision_excluded",(J-Q).n),
                      ("previous_whole_Phi_zero_collision_excluded",Phi.n)]

def profile(pp):
 ss=str(pp).encode()
 return dict(degrees_lambda_u=list(map(int,pp.degrees())),
             totalDegree=int(pp.total_degree()),terms=len(pp.to_dict()),
             bytes=len(ss),sha256=hashlib.sha256(ss).hexdigest())
def audit_den(pp):
 rr=pp
 for name,atom in base_atoms:
  while rr:
   gg=rr.gcd(atom)
   if gg.total_degree()==0:break
   nn=rr/gg;assert nn*gg==rr;rr=nn
 assert rr.total_degree()==0,("unpaid original coefficient denominator",str(rr))
def primitive(rr):
 rr=R(rr);audit_den(rr.d);pp=rr.n
 if not pp:return pp,[]
 original=pp;product=oneP;removed=[]
 for name,atom in paid_atoms:
  count=0
  while pp:
   gg=pp.gcd(atom)
   if gg.total_degree()==0:break
   nn=pp/gg;assert nn*gg==pp;pp=nn;product*=gg;count+=1
  if count:removed.append(dict(originalUnit=name,gcdLoops=count))
 scalar=pp.coefficient(0);pp=pp/scalar
 assert pp*scalar*product==original
 return pp,removed
def factored(pp):
 if not pp:return dict(zero=True)
 ct,fs=pp.factor();back=ctx.constant(ct);factors=[]
 for ff,power in fs:
  back*=ff**int(power);item=dict(power=int(power),profile=profile(ff))
  if len(str(ff).encode())<=8192:item["polynomial"]=str(ff)
  factors.append(item)
 assert back==pp
 return dict(content=str(ct),factors=factors,fullQQProductVerified=True)
actual=[("E1",E1.a),("EBe",EB.a),("EBo",EB.b),("N1",n1.a),
        ("NBe",NB.a),("NBo",NB.b),("PBe",PB.a),("PBo",PB.b)]
cores={}
for name,rr in actual:
 pp,removed=primitive(rr);cores[name]=pp
 say("new_Q1u_nonzero_Delta_complete_original_core",
     name=name,raw=profile(rr.n),primitive=profile(pp),factorization=factored(pp),
     onlyPaidOriginalRemoval=removed,claimExcluded=False)
from flint import fmpq_poly
qzero=fmpq_poly([]);qone=fmpq_poly([1])
def univariate(pp):
 assert all(int(m[1])==0 for m in pp.to_dict())
 cc=[fmpq(0)]*(int(pp.degrees()[0])+1) if pp else []
 for m,aa in pp.to_dict().items():cc[int(m[0])]=fmpq(aa)
 return fmpq_poly(cc)
def qprofile(pp):
 co=[str(cc) for cc in pp.coeffs()];bb=json.dumps(co,separators=(",",":")).encode()
 out=dict(degree=int(pp.degree()),bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest())
 if len(bb)<=8192:out["coefficientsAscending"]=co
 return out
def coeffu(pp,j):
 return ctx.from_dict({(int(m[0]),0):vv for m,vv in pp.to_dict().items() if int(m[1])==j})
def fixed_sylvester(aa,bb):
 m,n=int(aa.degrees()[1]),int(bb.degrees()[1]);assert m>0 and n>0
 rows=[]
 for pp,degree,shifts in [(aa,m,n),(bb,n,m)]:
  coeffs=[coeffu(pp,j) for j in range(degree+1)]
  assert sum((v*up**j for j,v in enumerate(coeffs)),zeroP)==pp
  for s in range(shifts):
   row=[zeroP]*(m+n)
   for j,v in enumerate(coeffs):row[j+s]=v
   assert sum((v*up**j for j,v in enumerate(row)),zeroP)==pp*up**s
   rows.append(row)
 assert len(rows)==m+n
 return m+n
cover=qzero;tags=[];inputs=[];names=[]
def add_input(label,rr):
 global cover,tags
 pp,removed=primitive(rr);cc=univariate(pp)
 gg,ss,tt=cover.xgcd(cc)
 assert ss*cover+tt*cc==gg
 tags=[ss*tag for tag in tags]+[tt];inputs.append(cc);names.append(label)
 assert sum((tag*ip for tag,ip in zip(tags,inputs)),qzero)==gg
 cover=gg
 say("new_Q1u_nonzero_Delta_actual_QQ_lambda_cover",
     inputName=label,input=qprofile(cc),currentCover=qprofile(cover),
     onlyPaidOriginalRemoval=removed,fullBezoutProductsReturned=True,
     allLeadingZeroFibersRetained=True,claimExcluded=False)
for name,pp in cores.items():
 if pp and int(pp.degrees()[1])==0:
  add_input("original_"+name,pp)
  if cover.degree()==0:break
if cover.degree()!=0:
 for na,nb in [("E1","EBo"),("E1","N1"),("EBo","N1"),("E1","PBo")]:
  aa,bb=cores[na],cores[nb]
  if not aa or not bb or min(int(aa.degrees()[1]),int(bb.degrees()[1]))<=0:continue
  gg=aa.gcd(bb)
  if gg.total_degree()>0:
   say("new_Q1u_nonzero_Delta_original_common_curve_retained",
       pair=[na,nb],common=profile(gg),claimExcluded=False);continue
  order=fixed_sylvester(aa,bb)
  say("new_Q1u_nonzero_Delta_original_fixed_projection_begin",
      pair=[na,nb],fixedOrder=order,allOriginalRowsReconstructed=True,
      allHeadZeroFibersRetained=True,claimExcluded=False)
  res=aa.resultant(bb,"u");assert res
  say("new_Q1u_nonzero_Delta_original_fixed_projection_complete",
      pair=[na,nb],fixedOrder=order,rawProjection=qprofile(univariate(res)),
      claimExcluded=False)
  add_input("Res_u_"+na+"_"+nb,res)
  if cover.degree()==0:break
factor_data=[]
if cover:
 cover=cover/cover[cover.degree()]
 ct,fs=cover.factor();back=fmpq_poly([ct])
 for ff,power in fs:
  back*=ff**int(power);factor_data.append(dict(power=int(power),profile=qprofile(ff)))
 assert back==cover
signal.alarm(0)
say("new_Q1u_nonzero_Delta_original_input_and_QQ_cover_complete",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    originalDomain="h=k!=1,Q=1-u,Delta!=0",
    lambdaCover=qprofile(cover),completeQQFactorization=factor_data,
    originalProjectionInputs=names,allOriginalHeadZeroFibersRetained=True,
    entireOriginalFaceExcluded=bool(cover) and cover.degree()==0,
    nonconstantCoverRequiresFullOriginalFiniteReturn=True,
    entireDeltaZeroComplementStillOpen=True,
    noClaimAboutOtherOriginalEqualValueFaces=True,ordinaryISPClaim=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
