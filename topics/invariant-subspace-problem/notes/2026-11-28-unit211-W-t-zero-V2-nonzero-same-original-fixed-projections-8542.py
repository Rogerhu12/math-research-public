#!/usr/bin/env python3
"""NEW current W, t=0, V2!=0: unique-geometry original scalar equations.
The whole V=f branch and V2=0 fiber are already closed by their original
mean/QQ certificates. On the complementary f=u chart, keep the complete
mean curve g*(V2-u*Q)^2-M*V2^2=0 and return all original N1/NS/PS at
the SAME recovered x,y,t,lambda,T. No original row is discarded.
Construct at most three new FIXED e-Sylvester resultants over QQ[k].
Every leading-zero specialization is included by the fixed polynomial
matrix; intermediate Bareiss divisions are multiplied back exactly.
Only previously paid pure k factors are stripped from the final common
projection. Zero resultants/unpaid factors stay open.
No old native determinant, lambda-module, seven-row Popov, norm or
Lhalf/F101 return is replayed. 180s/4GiB; zero file dependencies.
Only source/parameter definitions/degrees/SHA/small receipts are saved.
"""
import json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx
START=time.perf_counter();signal.setitimer(signal.ITIMER_REAL,180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**kw):
 kw['seconds']=time.perf_counter()-START
 print(json.dumps(kw,separators=(',',':')),flush=True)
def digest(x):
 raw=json.dumps(x,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
ctx=fmpq_mpoly_ctx.get(('e','k'),'lex');ep,kp=ctx.gens()
zz=ctx.constant(0);oo=ctx.constant(1)
def poly(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=oo if d is None else poly(d);assert d
  if not n:self.n=zz;self.d=oo;return
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
 def __pow__(self,n):return R(self.d**(-n),self.n**(-n),False) if n<0 else R(self.n**n,self.d**n,False)
 def __eq__(self,o):o=R(o);return self.n*o.d==o.n*self.d

e,k=R(ep),R(kp);u=e+1;Q=e*k;Vbar=u*k+2
l=u*((k+2)**2-2*e*k)/(k*Vbar);Delta=1-Q
V2=2*u-l*Q;T0=V2-2*u*u;M=l*V2-u*u
ghalf=2*l-1;J0=V2-u*Q
L=4*k*e*e-(k*k+4*k+8)*e-(k*k+6*k+8)
assert ghalf==-L/(k*Vbar)
assert T0==-u*e*(k+2)*(k+4)/Vbar
assert V2==u*(e*k-2)*(2*e-k-2)/Vbar
Fweight=ghalf*J0*J0-M*V2*V2
assert Fweight
w=-ghalf*J0/V2
x0=u+R(1)/2+(V2-u)*w/(2*M);x1=R(1)/2-u*w/(2*M)
t=R();f=u
qmean=w*w-ghalf*M
assert qmean==ghalf*Fweight/(V2*V2)
assert ghalf*J0+V2*w==0
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,o):o=E(o);return E(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,o):return self+-E(o)
 def __rsub__(self,o):return E(o)+-self
 def __mul__(self,o):o=E(o);return E(self.a*o.a+Delta*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __pow__(self,n):
  out=E(1)
  for _ in range(n):out=out*self
  return out
 def __eq__(self,o):o=E(o);return self.a==o.a and self.b==o.b
 def conj(self):return E(self.a,-self.b)

b=E(l/2,(u-l)/(2*Delta));c=b.conj();a=E(1-l)
p=E(1,1);q=p.conj();bc=M/(4*Delta)
assert b*c==E(bc) and b+c==E(l) and b*p+c*q==E(u)
X=E(x0,x1);Y=X.conj()
P02=(2-3*u)*V2-Q*u+2*u**3
assert f==(u*x0+(u-l*Q)*x1-T0/2)/(2*u)
W2=V2*x0+(2*u-u*Q-l*Q)*x1
lam=(W2-u*T0-(V2+2*u*u)*f+bc*Q*t)/P02
J=2*u*(1-u)+l*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q)
G0=lam*P02-(1-u)*T0
T=(G0*T0-Pf*f-Phi*bc*Q*t)/(Q*P02)-l
assert Phi*(J-2*u*Q)-Pf==0
r=X-a*p-c*E(t);s=Y-a*q-b*E(t)
A=E(2*f)-2*b*X-2*c*Y+E(2*bc*t)
rows=[[E(),E(),p,q],[E(),A,r,s],[p,r,E(),E(t)],[q,s,E(t),E()]]
one=[E(1),E(),E(1),E(1)]
def va(v,z):return [a+b for a,b in zip(v,z)]
def vs(a,v):return [a*b for b in v]
def vm(v,z):return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return a*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d);Kd=DK(d)
assert F2==E(2*f)
def mean(j):
 ee=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
 return ee-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
assert not mean(0)
E1,EB,EC=mean(1),mean(2),mean(3)
assert not E1.b and EB.conj()==EC
EW=b*EB+c*EC
assert not EW.b and E1==EW
assert E(2*M)*EW==E(-V2*qmean)
assert M*M*EB.b-u*(V2-u)*qmean==M*l*(ghalf*J0+V2*w)
# The complete individual mean identity retains the rho coordinate.
assert E(2*M*M)*EB+(E(V2)-E(u)*p)**2*E(qmean)==E(2*M)*(E(l)*p-E(u))*E(ghalf*J0+V2*w)
def N4(v):
 return 2*tau(vm(d,vm(v,v)))-F2*tau(vm(v,v))-4*tau(v)*tau(vm(d,v))+2*F2*tau(v)**2+tau(vm(v,DK(v)))
vc=va(rows[0],vs(-tau(rows[0]),one))
zc=va(rows[1],vs(-tau(rows[1]),one))
Pj=3*tau(vm(vm(vc,vc),zc))
Nv=N4(va(rows[0],rows[1]))-N4(rows[0])-N4(rows[1])
N1=Nv-E(lam*fmpq(4,3))*Pj
assert not N1.b
assert N4(rows[0])==E(2*lam*P02)
assert Pj==E(3*(lam-1-T)*P02)
def P2(v):
 cc=va(v,vs(-tau(v),one))
 return tau(vm(vm(cc,cc),cc))
assert P2(rows[0])==E(P02)
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1
NS=b*N4(rows[2])+c*N4(rows[3])-E(2*lam*P02*(l+2*T+A2))
PS=b*P2(rows[2])+c*P2(rows[3])-E(P02*(l+3*T+3*A2+B3))
assert not NS.b and not PS.b
Dphysical=l*A2-T*T
say(stage='new_t_zero_V2_nonzero_same_original_Gram_and_mean_curve',
 originalJetSquareCorrect=True,originalE0N0P0P1Returned=True,
 completeIndividualAndWeightedMeansReturned=True,
 exactMeanCurve='(2ell-1)*(V2-uQ)^2-M*V2^2',
 uniqueGeometry='w=-(2ell-1)*(V2-uQ)/V2',
 N1NSPSSameLambdaTAndRhoReturned=True,
 V2ZeroAlreadySeparatelyClosed=True,allNewWeightZerosKept=True)

division_returns=0
def exact(p,q):
 global division_returns
 a,b=divmod(p,q);assert not b and a*q==p
 division_returns+=1;return a
def profile(p):
 if not p:return dict(zero=True,degrees_e_k=[-1,-1],terms=0)
 data=[[[int(v) for v in m],str(c)] for m,c in sorted(p.to_dict().items())]
 return dict(zero=False,degrees_e_k=list(map(int,p.degrees())),
 totalDegree=int(p.total_degree()),terms=len(data),**digest(data))
def qprofile(p):
 return dict(degree=int(p.degree()),**digest([str(c) for c in p.coeffs()]))
H=4*ep*kp-kp*kp-4*kp-8
units=[('e',ep),('k',kp),('u',ep+1),('Q_minus_one',ep*kp-1),
 ('Vbar',(ep+1)*kp+2),('Phi_k_plus_four',kp+4),
 ('P02',P02.n),('M',M.n),('k_plus_one',kp+1),
 ('whole_H_old',H),('whole_equal_weights_k_plus_two',kp+2),
 ('whole_ell_zero',l.n),('whole_Lhalf_zero',L.n),
 ('current_V2_nonzero_chart',V2.n)]
def strip(p):
 before=p;scale=oo;hist=[]
 if not p:return p,scale,hist
 for name,atom in units:
  count=0
  while True:
   fac=p.gcd(atom)
   if int(fac.total_degree())==0:break
   p=exact(p,fac);scale*=fac;count+=1
  if count:hist.append([name,count])
 assert p*scale==before
 return p,scale,hist
def paid_den(d):
 rest,scale,hist=strip(d)
 assert rest and int(rest.total_degree())==0
 return hist
def primitive(name,value):
 paid_den(value.d)
 core,removed,hist=strip(value.n)
 if core:
  sc=core.coefficient(0);core=core/sc;removed*=sc
 assert R(core)*R(removed,value.d)==value
 say(stage='new_original_pure_weight_row',name=name,
 polynomial=profile(core),removedOnlyPaidFactors=hist,
 wholeOriginalRationalReturn=True,allOtherFactorsRetained=True)
 return core
for value in [l,V2,M,w,x0,x1,lam,T,Dphysical]:paid_den(value.d)
Pmean=primitive('complete_mean_curve',Fweight)
PN=primitive('same_original_N1',N1.a)
PSN=primitive('same_original_weighted_N',NS.a)
PSP=primitive('same_original_weighted_P',PS.a)
assert list(map(int,Pmean.degrees()))==[7,8] and len(Pmean.to_dict())==51
def factor_profile(p):
 if not p:return dict(zero=True)
 scalar,fac=p.factor();back=ctx.constant(scalar);ans=[]
 for v,mul in fac:
  back*=v**int(mul);ans.append(dict(multiplicity=int(mul),**profile(v)))
 assert back==p
 return dict(factors=ans,content=str(scalar),wholeProductReturned=True)
say(stage='entire_new_mean_curve_QQ_factorization',**factor_profile(Pmean))
def ecoeff(p):
 if not p:return []
 n=int(p.degrees()[0]);vals=[{} for _ in range(n+1)]
 for mm,c0 in p.to_dict().items():
  ee,kk=map(int,mm);vals[ee][kk]=c0
 out=[]
 for d0 in vals:
  out.append(fmpq_poly([d0.get(i,0) for i in range(max(d0,default=-1)+1)]))
 return out
def resultant_fixed(label,p,q):
 global division_returns
 aa,bb=ecoeff(p),ecoeff(q)
 if not aa or not bb:
  say(stage='new_fixed_original_resultant_zero_input',name=label)
  return fmpq_poly()
 m,n=len(aa)-1,len(bb)-1
 if m==0:return aa[0]**n
 if n==0:return bb[0]**m
 ad,bd=list(reversed(aa)),list(reversed(bb))
 N=m+n;A=[[fmpq_poly() for _ in range(N)] for _ in range(N)]
 for i in range(n):
  for j,c0 in enumerate(ad):A[i][i+j]=c0
 for i in range(m):
  for j,c0 in enumerate(bd):A[n+i][i+j]=c0
 previous=fmpq_poly([1]);sgn=1;count=0
 say(stage='new_fixed_original_resultant_begin',name=label,
 eliminatedVariable='e',fixedDegrees=[m,n],matrixOrder=N,
 noELeadingCoefficientInverted=True)
 for j in range(N-1):
  pivot=next((i for i in range(j,N) if A[i][j]),None)
  if pivot is None:
   say(stage='new_fixed_original_resultant_exact_zero',name=label,zeroColumn=j)
   return fmpq_poly()
  if pivot!=j:A[pivot],A[j]=A[j],A[pivot];sgn=-sgn
  x=A[j][j]
  for r0 in range(j+1,N):
   for c0 in range(j+1,N):
    num=x*A[r0][c0]-A[r0][j]*A[j][c0]
    v,rem=divmod(num,previous)
    assert not rem and v*previous==num
    A[r0][c0]=v;count+=1;division_returns+=1
  for r0 in range(j+1,N):A[r0][j]=fmpq_poly()
  previous=x
  say(stage='new_fixed_original_resultant_Bareiss_step',name=label,step=j,
      completeQuotientProducts=count,pivotDegree=int(x.degree()))
 out=sgn*A[-1][-1]
 say(stage='new_fixed_original_resultant_returned',name=label,
     polynomial=qprofile(out),allIntermediateQuotientsReturned=count,
     allFiniteLeadingZeroSpecializationsRetained=True)
 return out
K=fmpq_poly([0,1])
k_units=[('k',K),('k_plus_one',K+1),('k_plus_two',K+2),('k_plus_four',K+4)]
def strip_k(p):
 original=p;scale=fmpq_poly([1]);hist=[]
 if not p:return p,scale,hist
 for name,atom in k_units:
  count=0
  while True:
   g0=p.gcd(atom)
   if int(g0.degree())==0:break
   v,r0=divmod(p,g0);assert not r0 and v*g0==p
   p=v;scale*=g0;count+=1
  if count:hist.append([name,count])
 assert p*scale==original
 if p:
  c0=p[p.degree()];p/=c0;scale*=c0
 assert p*scale==original
 return p,scale,hist
cover=fmpq_poly()
for name,row in [('N1',PN),('NS',PSN),('PS',PSP)]:
 res=resultant_fixed('mean_curve__'+name,Pmean,row)
 if not res:continue
 reduced,scale,hist=strip_k(res)
 say(stage='new_fixed_projection_only_paid_k_removed',name=name,
     original=qprofile(res),retained=qprofile(reduced),paidRemoval=hist)
 if not cover:cover=reduced
 else:
  g0,s0,t0=cover.xgcd(reduced)
  assert s0*cover+t0*reduced==g0
  cover=g0/ g0[g0.degree()]
  say(stage='new_original_parameter_Bezout_return',lastRow=name,
      commonProjection=qprofile(cover),fullTwoProductsReturned=True)
 if int(cover.degree())==0:
  say(stage='new_whole_t_zero_complement_original_excluded',
      originalFixedResultantsAndQQBezoutOne=True,
      allV2AndOtherLeadingZeroFacesPreviouslyRetained=True)
  break
factor_info=[]
if cover and int(cover.degree())>0:
 c0,fs=cover.factor();back=fmpq_poly([c0])
 for h0,mul in fs:
  back*=h0**int(mul)
  factor_info.append(dict(multiplicity=int(mul),**qprofile(h0)))
 assert back==cover
say(stage='new_t_zero_V2_nonzero_original_scalar_projection_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 remainingKCover=qprofile(cover),remainingFactors=factor_info,
 QQFactorProductReturned=bool(cover),wholeComplementExcluded=bool(cover) and cover.degree()==0,
 noNewHeadOrContentZeroDiscarded=True,allFixedResultantHeadZerosIncluded=True,
 noOldGateReplayed=True,noRecomputablePayloadSaved=True,
 exactDivisionMultiplicationReturns=division_returns,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 ordinaryISPClaim=False)
