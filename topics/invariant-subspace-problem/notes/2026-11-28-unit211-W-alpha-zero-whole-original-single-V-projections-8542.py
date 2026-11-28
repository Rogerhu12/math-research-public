#!/usr/bin/env python3
"""NEW current W alpha=4*(1-Q)*(f-u)-(u-ell*Q)*t zero.
Whole f=u and whole t=0 are already excluded. Correct R resolves f,t
using only paid weight factors. One free V=bX+cY remains.
Full original means/N/P are rebuilt at that same point. The new general
weighted/jet identities give a quadratic weighted-difference row.
No new mean or affine head is inverted. All head-zero fibers are kept.
Only genuinely new fixed V/e projections are attempted; no old gate.
180 seconds / 4 GiB, self-contained, hash-only mathematical output.
"""
import json,time,hashlib,signal,resource,itertools
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
ctx=fmpq_mpoly_ctx.get(('e','k','v'),'lex');ep,kp,vp=ctx.gens()
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


e,k,V=R(ep),R(kp),R(vp);u=e+1;Q=e*k;Vbar=u*k+2
Aw=(k+2)**2-2*Q
l=u*Aw/(k*Vbar);Delta=1-Q;m=u-l
V2=2*u-l*Q;T0=V2-2*u*u;M=l*V2-u*u
Uhat=V2-u;ghalf=2*l-1
Hold=4*e*k-k*k-4*k-8
L=4*k*e*e-(k*k+4*k+8)*e-(k*k+6*k+8)
assert ghalf==-L/(k*Vbar)
Rw=2*u*(1-u)-u*Q+(2*u-1)*l*Q
Balpha=2*u*m-Uhat
Aalpha=M*Delta+Balpha*Uhat
assert Rw==-e*e*u*Hold/Vbar
assert Aalpha==e*e*u*u*(k+2)*Hold*(Q-2)/(k*Vbar*Vbar)
t=-2*Delta*Aw/((k+2)*(Q-2))
f=u+Uhat*t/(4*Delta)
assert Aalpha*t==2*l*Delta*Rw
assert 4*Delta*(f-u)-Uhat*t==0
W1=(T0+4*u*f)/2
x0=(Uhat*V-m*W1)/M;x1=(l*W1-u*V)/M
# delta*R_true = alpha*V + this weight constant.
Rconstant=M*t*t/4+M*u*t+(m/2)*t*(T0+4*u*f)-4*Delta*f*(f-u)
assert not Rconstant
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
Lmean=2*u*Uhat*EW.a+M*V2*EB.b
assert not Lmean or int(Lmean.n.degrees()[2])<=1
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

assert b*X+c*Y==E(V) and b*p*X+c*q*Y==E(W1)
assert not A.b
eta=f-u;Sx=2*x0;Px=2*x0+2*Delta*x1;XY=x0*x0-Delta*x1*x1
Kw=2*(t*t+(5*u-2*Sx-2)*t+2*XY+2*Px-2*u*Sx+2*u*u-6*u+Q)
Kl=2*(t*t+2*(3*u-Sx-2)*t+2*XY+3*Px+(2-2*u)*Sx-2*W1+4*u*u-16*u+4+l*Q)
Loww=2*P02*(2*lam-1)*(lam-1-T)-bc*t*(Kw+4*eta*(t-2))
Lowl=2*P02*lam*ghalf-4*u*eta*A.a-bc*t*(Kl+4*eta*(t-4))
EW2=b*(2*p-E(u)-X)*EB+c*(2*q-E(u)-Y)*EC
Ep=b*p*EB+c*q*EC
assert not EW2.b and not Ep.b
assert E(Loww)==NS-PS+EW2
assert E(Lowl)==NS-PS+N1+EW2+2*Ep-E(2*u)*E1
assert all(not h or int(h.n.degrees()[2])<=2 for h in [N1.a,Loww,Lowl])
say(stage='new_entire_alpha_zero_same_original_rows',
 correctJetMean=True,originalE0N0P0P1Returned=True,
 alphaZeroWeightConstantReturned=True,AalphaEntirePaidFactorizationReturned=True,
 allFAndTRecoveredWithoutUnpaidHead=True,originalE1EqualsWeightedMeanReturned=True,
 meanQuadraticCancellationAffine=True,
 fullWeightedLowwIdentity='Loww=NS-PS+E_W2',
 fullWeightedLowlIdentity='Lowl=NS-PS+N1+E_W2+2Ep-2uE1',
 completeOriginalWeightedRowsRetained=True,
 noMeanVLeadingOrAffineHeadInverse=True,
 originalVMaxDegrees=dict(EW=int(EW.a.n.degrees()[2]),
  EBo=int(EB.b.n.degrees()[2]),Lmean=int(Lmean.n.degrees()[2]) if Lmean else -1,
  N1=int(N1.a.n.degrees()[2]),Loww=int(Loww.n.degrees()[2]),
  NS=int(NS.a.n.degrees()[2])))
division_returns=0
def exact(p,q):
 global division_returns
 a,b=divmod(p,q);assert not b and a*q==p
 division_returns+=1;return a
def profile(p):
 if not p:return dict(zero=True,degrees_e_k_v=[-1,-1,-1],terms=0)
 data=[[[int(v) for v in m],str(c)] for m,c in sorted(p.to_dict().items())]
 return dict(zero=False,degrees_e_k_v=list(map(int,p.degrees())),
 totalDegree=int(p.total_degree()),terms=len(data),**digest(data))
def qprofile(p):
 return dict(degree=int(p.degree()),**digest([str(c) for c in p.coeffs()]))
H=4*ep*kp-kp*kp-4*kp-8
units=[('e',ep),('k',kp),('u',ep+1),('Q_minus_one',ep*kp-1),
 ('Vbar',(ep+1)*kp+2),('Phi_k_plus_four',kp+4),
 ('P02',P02.n),('M',M.n),('k_plus_one',kp+1),
 ('whole_H_old',H),('whole_equal_weights_k_plus_two',kp+2),
 ('whole_ell_zero',l.n),('whole_Lhalf_zero',L.n),('whole_equal_weights_Q_minus_two',(Q-2).n),
 ('Uhat_paid_on_alpha_zero_from_t_and_f_minus_u',Uhat.n)]
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


for value in [l,M,Aalpha,Rw,f,t,x0,x1,lam,T,Dphysical]:
 assert all(int(mm[2])==0 for mm in value.d.to_dict())
 paid_den(value.d)
EWp=primitive('original_EW',EW.a);EOp=primitive('original_EBo',EB.b)
Lmp=primitive('original_affine_mean_combination',Lmean)
N1p=primitive('original_N1',N1.a)
Lowp=primitive('original_weighted_N_minus_P_low_quadratic',Loww)
NSp=primitive('original_NS',NS.a)
def vcoeff(p):
 if not p:return []
 n=int(p.degrees()[2]);out=[zz for _ in range(n+1)]
 for mm,c0 in p.to_dict().items():
  ie,ik,iw=map(int,mm);out[iw]+=c0*ep**ie*kp**ik
 return out
def det_poly(A,label):
 global division_returns
 N=len(A)
 if not N:return oo
 if N==1:return A[0][0]
 previous=oo;sgn=1
 for j in range(N-1):
  pivot=next((r for r in range(j,N) if A[r][j]),None)
  if pivot is None:return zz
  if pivot!=j:A[pivot],A[j]=A[j],A[pivot];sgn=-sgn
  p0=A[j][j]
  for r in range(j+1,N):
   for c in range(j+1,N):
    num=p0*A[r][c]-A[r][j]*A[j][c]
    q0,r0=divmod(num,previous);assert not r0 and q0*previous==num
    A[r][c]=q0;division_returns+=1
  for r in range(j+1,N):A[r][j]=zz
  previous=p0
 return sgn*A[-1][-1]
def v_resultant(label,p,q):
 aa,bb=vcoeff(p),vcoeff(q)
 if not aa or not bb:return zz
 m,n=len(aa)-1,len(bb)-1
 if m==0 and n==0:
  say(stage='new_constant_original_projection',name=label,source='first constant original row',profile=profile(aa[0]))
  return aa[0]
 if m==0:return aa[0]**n
 if n==0:return bb[0]**m
 N=m+n;matrix=[[zz for _ in range(N)] for _ in range(N)]
 for i in range(n):
  for j,c0 in enumerate(reversed(aa)):matrix[i][i+j]=c0
 for i in range(m):
  for j,c0 in enumerate(reversed(bb)):matrix[n+i][i+j]=c0
 out=det_poly(matrix,label)
 assert not out or int(out.degrees()[2])==0
 say(stage='new_fixed_original_v_resultant',
     name=label,fixedDegrees=[m,n],matrixOrder=N,
     originalDeterminant=profile(out),allVHeadZerosRetained=True)
 if not out:return out
 core,removed,hist=strip(out)
 sc=core.coefficient(0);core/=sc;removed*=sc
 assert core*removed==out
 say(stage='new_original_v_resultant_paid_primitive',
     name=label,polynomial=profile(core),onlyPaidWeightContentRemoved=hist)
 return core

if Lmp and int(Lmp.degrees()[2])==0:
 Hweight=Lmp
 say(stage='new_alpha_zero_weight_necessity',source='constant original affine mean row',polynomial=profile(Hweight))
else:
 Hweight=v_resultant('whole_original_EW__EBo',EWp,EOp)
 say(stage='new_alpha_zero_weight_necessity',source='fixed original mean resultant',polynomial=profile(Hweight))
necessary=[]
if Hweight and int(Hweight.total_degree())>0:
 if Lmp:
  for name,p0 in [('N1',N1p),('Loww',Lowp),('NS',NSp)]:
   necessary.append(v_resultant('affine_mean__'+name,Lmp,p0))
 common=Hweight
 for p0 in necessary:common=common.gcd(p0)
 if int(common.total_degree())>0:
  for first,p0 in [('EW',EWp),('EBo',EOp)]:
   for name,q0 in [('N1',N1p),('Loww',Lowp),('NS',NSp)]:
    necessary.append(v_resultant(first+'__'+name,p0,q0))
  common=Hweight
  for p0 in necessary:common=common.gcd(p0)
else:common=Hweight
say(stage='new_alpha_zero_original_common_curve_test',
 wholeNecessaryWeight=profile(Hweight),commonCurve=profile(common),
 noMultivariateGcdEmptinessClaim=True)
def ecoeff(p):
 if not p:return []
 assert int(p.degrees()[2])==0
 n=int(p.degrees()[0]);vals=[{} for _ in range(n+1)]
 for mm,c0 in p.to_dict().items():
  ie,ik,iw=map(int,mm);assert iw==0
  vals[ie][ik]=c0
 return [fmpq_poly([v.get(i,0) for i in range(max(v,default=-1)+1)]) for v in vals]

combinations=[]
if Hweight and int(Hweight.total_degree())>0 and int(common.total_degree())==0:
 # Count all irreducible curve components, INCLUDING vertical k components.
 # A coefficient polynomial in c has degree at most len(necessary)-1.
 bound=max(1,len(necessary)-1)*int(Hweight.total_degree())+2
 for c0 in range(bound):
  p0=sum((ctx.constant(c0**j)*r for j,r in enumerate(necessary)),zz)
  if not p0:continue
  if int(Hweight.gcd(p0).total_degree())==0:
   combinations.append((c0,p0))
   say(stage='new_alpha_zero_original_unmixed_parameter_combination',
    coefficientParameter=c0,definition='sum c^j R_j in the printed necessary-row order',
    polynomial=profile(p0),wholeCurveGcdConstant=True)
  if len(combinations)==2:break
 assert len(combinations)==2
def result_e(label,p,q):
 global division_returns
 aa,bb=ecoeff(p),ecoeff(q)
 if not aa or not bb:return fmpq_poly()
 m,n=len(aa)-1,len(bb)-1;N=m+n
 if m==0 and n==0:return aa[0]
 if m==0:return aa[0]**n
 if n==0:return bb[0]**m
 matrix=[[fmpq_poly() for _ in range(N)] for _ in range(N)]
 for i in range(n):
  for j,c0 in enumerate(reversed(aa)):matrix[i][i+j]=c0
 for i in range(m):
  for j,c0 in enumerate(reversed(bb)):matrix[n+i][i+j]=c0
 previous=fmpq_poly([1]);sgn=1;count=0
 say(stage='new_fixed_original_e_projection_begin',
     name=label,fixedDegrees=[m,n],matrixOrder=N,
     allLeadingZeroFibersRetained=True)
 for j in range(N-1):
  pivot=next((r for r in range(j,N) if matrix[r][j]),None)
  if pivot is None:return fmpq_poly()
  if pivot!=j:matrix[pivot],matrix[j]=matrix[j],matrix[pivot];sgn=-sgn
  p0=matrix[j][j]
  for r in range(j+1,N):
   for c in range(j+1,N):
    num=p0*matrix[r][c]-matrix[r][j]*matrix[j][c]
    q0,r0=divmod(num,previous);assert not r0 and q0*previous==num
    matrix[r][c]=q0;division_returns+=1;count+=1
  for r in range(j+1,N):matrix[r][j]=fmpq_poly()
  previous=p0
  say(stage='new_e_projection_exact_step',name=label,step=j,
      completeQuotientProducts=count,pivotDegree=int(p0.degree()))
 out=sgn*matrix[-1][-1]
 say(stage='new_fixed_original_e_projection_returned',
     name=label,polynomial=qprofile(out),completeQuotientProducts=count)
 return out
kk=fmpq_poly([0,1])
k_units=[('k',kk),('k_plus_one',kk+1),('k_plus_two',kk+2),('k_plus_four',kk+4)]
def strip_k(p):
 original=p;scale=fmpq_poly([1]);hist=[]
 assert p
 for name,atom in k_units:
  count=0
  while True:
   gg=p.gcd(atom)
   if gg.degree()==0:break
   qq,rr=divmod(p,gg);assert not rr and qq*gg==p
   p=qq;scale*=gg;count+=1
  if count:hist.append([name,count])
 sc=p[p.degree()];p/=sc;scale*=sc
 assert p*scale==original
 return p,hist

cover=fmpq_poly([1]) if Hweight and int(Hweight.total_degree())==0 else fmpq_poly()
for c0,p0 in combinations:
 res=result_e('alpha_zero_weight__combination_'+str(c0),Hweight,p0)
 assert res
 retained,hist=strip_k(res)
 say(stage='new_alpha_zero_original_e_projection_only_paid_k_removed',
     coefficientParameter=c0,polynomial=qprofile(retained),paidRemoval=hist)
 if not cover:cover=retained
 else:
  gg,s0,t0=cover.xgcd(retained)
  assert s0*cover+t0*retained==gg
  cover=gg/gg[gg.degree()]
  say(stage='new_alpha_zero_same_weight_QQ_Bezout',
      cover=qprofile(cover),bothOriginalProductsReturned=True)
 if cover.degree()==0:break
fac=[]
if cover and cover.degree()>0:
 cc,fs=cover.factor();back=fmpq_poly([cc])
 for h0,mul in fs:
  back*=h0**int(mul);fac.append(dict(multiplicity=int(mul),**qprofile(h0)))
 assert back==cover
say(stage='new_entire_alpha_zero_original_projection_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 pureWeight=profile(Hweight),retainedCommonCurve=profile(common),
 allMeanVAffineAndQuadraticHeadZerosRetained=True,
 remainingKCover=qprofile(cover),remainingFactors=fac,
 wholeAlphaZeroExcluded=bool(cover) and cover.degree()==0,
 noOldGateExecuted=True,noPayloadSaved=True,
 exactDivisionProducts=division_returns,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 ordinaryISPClaim=False)
