#!/usr/bin/env python3
"""Exact original U-value atlas and five-coordinate necessary chart for R150.
This generates necessary equations; it does not claim that their solutions
are physical critical points or that the nonzero-lambda layer is empty.
"""
import hashlib,json,resource,time
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
started=time.perf_counter()
ctx=fmpq_mpoly_ctx.get(('f','t','q','lam','h','k','b_free'),'lex')
fp,tp,qp,lp,hp,kp,bfp=ctx.gens()
zero=ctx.constant(0);unit=ctx.constant(1)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=n if hasattr(n,'to_dict') else ctx.constant(n)
  d=unit if d is None else d
  assert d
  if not n:self.n=zero;self.d=unit;return
  if reduce:
   gg=n.gcd(d);n=n/gg;d=d/gg
  self.n=n;self.d=d
 def __add__(self,o):o=R(o);return R(self.n*o.d+o.n*self.d,self.d*o.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):o=R(o);return R(self.n*o.n,self.d*o.d)
 __rmul__=__mul__
 def __truediv__(self,o):o=R(o);return R(self.n*o.d,self.d*o.n)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):return R(self.n**n,self.d**n,False) if n>=0 else R(self.d**(-n),self.n**(-n),False)
 def iszero(self):return not self.n
def equal(x,y):return (R(x)-R(y)).iszero()
def degree(po):return tuple(int(max((mm[j] for mm in po.to_dict()),default=-1)) for j in range(7))
def normal(po):return po/po.leading_coefficient()
def strip(po,known):
 while po:
  gg=po.gcd(known)
  if gg.total_degree()==0:return normal(po)
  po=po/gg
 return po
def evaluate_poly(po,arg,index):
 groups={}
 for mm,cf in po.to_dict().items():
  key=tuple(0 if j==index else mm[j] for j in range(7))
  groups.setdefault(mm[index],{})[key]=cf
 out=R(0)
 for i in range(max(groups,default=0),-1,-1):out=out*arg+R(ctx.from_dict(groups.get(i,{})))
 return out
def evaluate(ex,arg,index):return evaluate_poly(ex.n,arg,index)/evaluate_poly(ex.d,arg,index)
f=R(fp);t=R(tp);q=R(qp);lam=R(lp);h=R(hp);k=R(kp)
Al=2*lam**2-2*lam+1
Bl=4*lam**3-6*lam**2+3*lam-1
assert equal(Bl,(2*lam-1)*Al-lam)
assert Al.n.gcd(Bl.n).total_degree()==0
b=(Bl-(k-1)*Al)/((h-1)**2*(h-k))
c=((h-1)*Al-Bl)/((k-1)**2*(h-k))
a=1-b-c
w=lam-a-b*h-c*k
one=[R(1),R(0),R(1),R(1)]
VV=[R(1),w,h,k]
def add(x,y):return [xx+yy for xx,yy in zip(x,y)]
def scale(cc,x):return [cc*xx for xx in x]
def mul(x,y):return [x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[2]*y[2],x[3]*y[3]]
def tau(x):return a*x[0]+x[1]+b*x[2]+c*x[3]
assert equal(tau(VV),lam)
assert equal(tau(mul(VV,VV)),2*lam**2)
assert equal(tau(mul(mul(VV,VV),VV)),4*lam**3)
# Complete value-collision charts, checked independently of the generic chart.
vc=lam*(2*lam-1)**2/Al
wc=lam**2*(1-2*lam)/Bl
totalc=Al**3/Bl**2
free=R(bfp)
def check_collision(bb,cc,hh,kk):
 aa=1-bb-cc
 assert equal(aa+wc+bb*hh+cc*kk,lam)
 assert equal(aa+2*wc+bb*hh**2+cc*kk**2,2*lam**2)
 assert equal(aa+3*wc+bb*hh**3+cc*kk**3,4*lam**3)
check_collision(free,totalc,R(1),vc)
check_collision(totalc,free,vc,R(1))
check_collision(free,totalc-free,vc,vc)
# At lambda=3/4, the raw N(V) coefficient of A vanishes. The two r,s
# coefficients cannot both vanish: C(z)=(z-1)(z+1/2) would give
# Bl=-3*Al/2, whereas its actual difference is 1/2.
def CC(z):return 1+z+z*z-2*lam*(1+z)
assert equal(evaluate(CC(h),R(fmpq(3,4)),3),(h-1)*(h+R(fmpq(1,2))))
assert equal(evaluate(Bl+R(fmpq(3,2))*Al,R(fmpq(3,4)),3),R(fmpq(1,2)))
# p=1 is a common homogeneous Gram scaling, with U0 kept implicit.
# Thus P0=-U0^3 and N0=lambda*P0, rather than P0=-1.
k0=[R(0),R(0),R(1),q]
def P(xx):
 z=add(xx,scale(-tau(xx),one))
 return tau(mul(mul(z,z),z))/2
P0=P(k0);u=b+c*q;V2=b+c*q*q
W1=V2/2-u*u+2*f*u
W2=u*V2-2*u**3+f*(V2+2*u*u)-b*c*q*t+2*lam*P0
x=(q*W1-W2)/(b*(q-1))
y=(W2-W1)/(c*q*(q-1))
r=x-a-c*t;s=y-a*q-b*t;A1=2*f-2*b*x-2*c*y+2*b*c*t
K=[k0,[R(0),A1,r,s],[R(1),r,R(0),t],[q,s,t,R(0)]]
def DK(xx):return [tau(mul(row,xx)) for row in K]
d=DK(one);F=tau(d)/2
assert equal(F,f)
def N(xx):
 return tau(mul(add(d,scale(-F,one)),mul(xx,xx)))/2-tau(xx)*tau(mul(d,xx))+F*tau(xx)**2+tau(mul(xx,DK(xx)))/4
def Pjet(xx,yy):
 z=add(xx,scale(-tau(xx),one));v=add(yy,scale(-tau(yy),one))
 return 3*tau(mul(mul(z,z),v))/2
def Njet(xx,yy):return N(add(xx,yy))-N(xx)-N(yy)
Ps=[P0,Pjet(K[0],K[1]),P(K[2]),P(K[3])]
Ns=[N(K[0]),Njet(K[0],K[1]),N(K[2]),N(K[3])]
ev=[tau(mul(K[0],K[0])),2*tau(mul(K[0],K[1])),tau(mul(K[2],K[2])),tau(mul(K[3],K[3]))]
E=add(add(ev,scale(-2,DK(d))),add(scale(-2,mul(d,d)),scale(4*F,d)))
assert E[0].iszero() and equal(Ns[0],lam*P0)
NV=N(VV)
raw=(3-4*lam)*A1+2*b*CC(h)*r+2*c*CC(k)*s
raw+=2*b*c*(h*h+h*k+k*k-2*lam*(h+k))*t
raw+=2*b*(a*CC(h)+w*(2+h-2*lam))
raw+=2*c*(a*CC(k)+w*(2+k-2*lam))*q
assert equal(4*NV,raw)
assert not NV.d.derivative('f') and not NV.d.derivative('t')
assert not NV.n.derivative('f').derivative('t')
Af=R(NV.n.derivative('f'),NV.d)
At=R(NV.n.derivative('t'),NV.d)
Cst=evaluate(evaluate(NV,R(0),0),R(0),1)
assert equal(NV,Af*f+At*t+Cst)
L=q*(h-1)-(k-1);S=h+k+1-2*lam
assert equal(At,b*c*L*S/(2*(q-1)))
# The L=0 fiber has VV=one+rho*k0+w*epsilon. Under E0 and N0=lambda*P0,
# N(VV)=w(w-1)*f+u*(w/2-w^2)+rho*(V2-2*u^2)/4+lambda*rho^2*P0.
# w=0 is excluded by P(VV)=rho^3*P0 with rho*P0!=0.
# At w=1 the two remaining identities imply 8*lambda^2-6*lambda-1=0.
rr=lam-2
pconst=R(fmpq(3,2))*(2*rr**2-Al)+3*rr+1
assert equal(pconst,R(fmpq(11,2))-6*lam)
cubevalue=6*lam-R(fmpq(11,2))
assert equal(4*lam*cubevalue+4*lam-3,3*(8*lam**2-6*lam-1))
# On L*S!=0 this is a global linear t graph. No sufficient-condition claim.
tgraph=-(Af*f+Cst)/At
assert equal(evaluate(NV,tgraph,1),0)
known=lp*qp*(qp-1)*(qp+1)*(hp-1)*(kp-1)*(hp-kp)*b.n*c.n*P0.n*L.n*S.n
assert strip(tgraph.d,known).total_degree()==0
raw_conditions=E[1:]+[Ps[1]-3*w*P0,Ps[2]-h**3*P0,Ps[3]-k**3*P0,Ns[1]-2*lam*w*P0,Ns[2]-lam*h*h*P0,Ns[3]-lam*k*k*P0]
labels=['E1','EB','EC','P1-3wP0','PB-h3P0','PC-k3P0','N1-2lambda*w*P0','NB-lambda-h2P0','NC-lambda-k2P0']
polys=[];profiles=[]
for name,value in zip(labels,raw_conditions):
 value=evaluate(value,tgraph,1)
 assert strip(value.d,known).total_degree()==0
 po=strip(value.n,known);polys.append(po)
 assert degree(po)[1]<=0 and degree(po)[6]<=0
 assert degree(po)[0]<= (2 if name.startswith('E') else 3)
 profiles.append({'name':name,'degree':degree(po),'terms':len(po.to_dict())})
def fcoeff(po,i):
 return ctx.from_dict({(0,mm[1],mm[2],mm[3],mm[4],mm[5],mm[6]):cf for mm,cf in po.to_dict().items() if mm[0]==i})
rows=[[fcoeff(po,j) for j in [2,1,0]] for po in polys[:3]]
aa,bb,cc=rows
cr=[aa[1]*bb[2]-aa[2]*bb[1],aa[2]*bb[0]-aa[0]*bb[2],aa[0]*bb[1]-aa[1]*bb[0]]
det=strip(sum((cr[j]*cc[j] for j in range(3)),zero),known)
assert degree(det)[0]<=0 and degree(det)[1]<=0 and degree(det)[6]<=0
report={'schema':'r150-unit211-original-U-value-atlas-v1','status':'necessary_atlas_and_original_five_coordinate_chart_verified','claimPhysicalSufficiency':False,'claimLambdaLayerEmpty':False,'ordinaryISPClaim':False,'sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'remainingCoordinates':['f','q','lambda','h','k'],'linearFCoefficient':{'degree':degree(Af.n),'terms':len(Af.n.to_dict())},'linearConstant':{'degree':degree(Cst.n),'terms':len(Cst.n.to_dict())},'genericChartUnits':'lambda*q*(q-1)*(q+1)*(h-1)*(k-1)*(h-k)*b*c*P0*L*S','newLinearDivisorFactors':['L=q*(h-1)-(k-1)','S=h+k+1-2*lambda'],'conditions':profiles,'meanDeterminant':{'degree':degree(det),'terms':len(det.to_dict()),'identicallyZero':not bool(det)},'elapsedSeconds':round(time.perf_counter()-started,6),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
print(json.dumps(report,sort_keys=True))
