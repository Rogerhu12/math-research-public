#!/usr/bin/env python3
"""Original L0 with b+c!=0, after the complete zero-weight-sum theorem.
Use p+q=2 and the entire kappa^2=1-pq algebra in three rational parameters.
All original nine conditions and all P1 leading-zero fibers are retained.
NEW full original L0 necessary system after whole W/G/K/V boundaries are paid.
The whole P1 double-zero chart has been closed, so its t coefficient is paid.
"""
import hashlib,json,resource,signal,time,os,sys,subprocess,shutil,tempfile
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx,fmpq_poly
started=time.perf_counter()
def say(stage,**kw):
 print(json.dumps(dict(stage=stage,elapsedSeconds=round(time.perf_counter()-started,6),**kw),sort_keys=True),flush=True)
def alarm(signum,frame):
 say("timeout_unknown",claimExcluded=False);raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm);signal.alarm(300)
resource.setrlimit(resource.RLIMIT_AS,(8*1024**3,8*1024**3))
ctx=fmpq_mpoly_ctx.get(("rho","lam","w"),"lex")
rp,lp,wp=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
def poly(v):return v if hasattr(v,"to_dict") else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=oo if d is None else poly(d)
  assert d
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
 def __truediv__(self,o):
  o=R(o);assert o
  return self*R(o.d,o.n,False)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):
  if n<0:assert self;return R(self.d**(-n),self.n**(-n),False)
  return R(self.n**n,self.d**n,False)
 def __eq__(self,o):
  o=R(o);return self.n*o.d==o.n*self.d

rho=R(rp);lam=R(lp);w=R(wp)
A=2*lam*lam-2*lam+1;BB=4*lam**3-6*lam*lam+3*lam-1
RR=lam-1-w;Cmom=RR*BB-A*A
u=RR/rho;V2=A/(rho*rho)
Q=(2*A*rho-BB)/(rho*rho*RR);Delta=1-Q
l=(2*u-V2)/Q;T=RR
bc=(l*l*Delta-(u-l)**2)/(4*Delta)
P02=(2-3*u)*V2-Q*u+2*u**3;P0=P02/2
T0=V2-2*u*u
fsol=-(u*(w/2-w*w)+rho*T0/4+lam*rho*rho*P0)/(w*(w-1))
assert Cmom==4*rho**4*bc*Q*Delta
assert P02==(BB-3*RR*A+2*RR**3)/(rho**3)
# l!=0 is paid by the complete L0,b+c=0 theorem, not by a generic assumption.
# A may be zero on this complement and is never inverted.
units=[rp,lp,wp,wp-1,RR.n,Cmom.n,Delta.n,Q.n,P0.n,(u-1).n,l.n]
def strip_units(po):
 po=poly(po)
 for atom in units:
  assert atom
  while po:
   gg=po.gcd(atom)
   if int(gg.total_degree())==0:break
   old=po;po=po/gg;assert po*gg==old
 return po
denominators=set()
def paid(rr):
 dd=R(rr).d;key=str(dd)
 if key not in denominators:
  assert int(strip_units(dd).total_degree())==0
  denominators.add(key)
def profile(po):
 return dict(degrees=list(map(int,po.degrees())) if po else [-1,-1],terms=len(po.to_dict()),sha256=hashlib.sha256(str(po).encode()).hexdigest())
for val in [A,BB,RR,rho,u,V2,Q,Delta,bc,P02,fsol]:paid(val)
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
 def __mul__(self,o):
  o=E(o);return E(self.a*o.a+Delta*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __pow__(self,n):
  assert n>=0
  out=E(1);v=self
  while n:
   if n&1:out=out*v
   v=v*v;n//=2
  return out
 def __eq__(self,o):o=E(o);return self.a==o.a and self.b==o.b
 def conj(self):return E(self.a,-self.b)

b=E(l/2,(u-l)/(2*Delta));c=b.conj();a=E(1-l)
p=E(1,1);q=p.conj()
h=E(1+rho,rho);k=h.conj()
assert b+c==E(l) and b*c==E(bc) and p*q==E(Q)
assert b*p+c*q==E(u) and b*p*p+c*q*q==E(V2)
assert b*p**3+c*q**3==E(2*V2-Q*u)
assert a+E(w)+b*h+c*k==E(lam)
assert a+E(2*w)+b*h*h+c*k*k==E(2*lam*lam)
assert a+E(3*w)+b*h**3+c*k**3==E(4*lam**3)
assert q*(h-1)-p*(k-1)==0
ivdiff=E(0,-1/(2*Delta))
ivbp=c*q*ivdiff*E(1/(bc*Q));ivcq=b*p*ivdiff*E(1/(bc*Q))
assert ivbp*b*p*(q-p)==1 and ivcq*c*q*(q-p)==1
for val in [b,c,p,q,h,k,ivdiff,ivbp,ivcq]:paid(val.a);paid(val.b)
sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
say("complete_original_L0_symmetric_nonzero_l_two_parameter_graph",sourceSha256=sha,retainedQuadraticRoots=2,paid_l_reason="complete original L0 zero-weight-sum theorem; A is retained including zero",claimExcluded=False)
class P:
 def __init__(self,co=None):self.co={ij:E(v) for ij,v in (co or {}).items() if E(v)}
 def __bool__(self):return bool(self.co)
 def __add__(self,o):
  if not isinstance(o,P):o=cp(o)
  dd=dict(self.co)
  for ij,v in o.co.items():dd[ij]=dd.get(ij,E())+v
  return P(dd)
 __radd__=__add__
 def __neg__(self):return P({ij:-v for ij,v in self.co.items()})
 def __sub__(self,o):return self+-o
 def __rsub__(self,o):return cp(o)+-self
 def __mul__(self,o):
  if not isinstance(o,P):return scale(E(o),self)
  dd={}
  for ij,v in self.co.items():
   for kl,vv in o.co.items():
    key=(ij[0]+kl[0],ij[1]+kl[1]);dd[key]=dd.get(key,E())+v*vv
  return P(dd)
 __rmul__=__mul__
 def __pow__(self,n):
  out=cp(1)
  for _ in range(n):out=out*self
  return out
 def conj(self):return P({ij:v.conj() for ij,v in self.co.items()})
def cp(v):return P({(0,0):E(v)})
def scale(v,pp):return P({ij:E(v)*vv for ij,vv in pp.co.items()})
fp=cp(fsol);tp=P({(0,1):E(1)});zero=P()
one=[cp(1),zero,cp(1),cp(1)]
def va(v,z0):return [x+y for x,y in zip(v,z0)]
def vs(v0,v):return [v0*x for x in v]
def vm(v,z0):return [v[0]*z0[0],v[0]*z0[1]+v[1]*z0[0],v[2]*z0[2],v[3]*z0[3]]
def tau(v):return scale(a,v[0])+v[1]+scale(b,v[2])+scale(c,v[3])
T0=V2-2*u*u
W1=cp(T0/2)+scale(E(2*u),fp)
W2=cp(u*T0+lam*P02)+scale(E(V2+2*u*u),fp)-scale(E(bc*Q),tp)
XX=scale(ivbp,scale(q,W1)-W2);YY=scale(ivcq,W2-scale(p,W1))
r=XX-cp(a*p)-scale(c,tp);ss=YY-cp(a*q)-scale(b,tp)
Arow=scale(E(2),fp)-scale(2*b,XX)-scale(2*c,YY)+scale(E(2*bc),tp)
assert not (r.conj()-ss) and not (Arow.conj()-Arow)
rows=[[zero,zero,cp(p),cp(q)],[zero,Arow,r,ss],[cp(p),r,zero,tp],[cp(q),ss,tp,zero]]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d);DKd=DK(d);dd=vm(d,d)
assert not (F2-scale(E(2),fp))
def P2(v):
 cen=va(v,vs(-tau(v),one))
 return tau(vm(vm(cen,cen),cen))
def N4(v):
 return scale(E(2),tau(vm(d,vm(v,v))))-F2*tau(vm(v,v))-scale(E(4),tau(v)*tau(vm(d,v)))+scale(E(2),F2*tau(v)**2)+tau(vm(v,DK(v)))
def Pjet2(v,z0):
 v0=va(v,vs(-tau(v),one));z1=va(z0,vs(-tau(z0),one))
 return scale(E(3),tau(vm(vm(v0,v0),z1)))
def Njet4(v,z0):return N4(va(v,z0))-N4(v)-N4(z0)
def mean(jj):
 ev=scale(E(2),tau(vm(rows[0],rows[1]))) if jj==1 else tau(vm(rows[jj],rows[jj]))
 return ev-scale(E(2),DKd[jj])-scale(E(2),dd[jj])+scale(E(2),F2*d[jj])
assert not mean(0) and not (P2(rows[0])-cp(P02)) and not (N4(rows[0])-cp(2*lam*P02))

VV=[cp(1),cp(w),cp(h),cp(k)]
assert not P2(VV) and not N4(VV)
raw=[mean(1),mean(2),Pjet2(rows[0],rows[1])-cp(3*w*P02),P2(rows[2])-cp(h**3*E(P02)),Njet4(rows[0],rows[1])-cp(4*lam*w*P02),N4(rows[2])-cp(h*h*E(2*lam*P02))]
assert not (mean(3)-raw[1].conj())
Lf=T0*(l-1+2*u*(1-u)/Q);Lt=bc*(T0+4*u-4+Q)
Lc=(1-u)*T0*T0/Q+P02*(l+T-lam*T0/Q)
assert not (raw[2]-scale(E(3),scale(E(Lf),fp)+scale(E(Lt),tp)+cp(Lc)))
def parts(pp,part):
 dd={}
 for ij,v in pp.co.items():
  assert ij[0]==0
  rr=v.a if part==0 else v.b
  if rr:dd[ij[1]]=rr
 return dd
for jj in [0,2,4]:assert not parts(raw[jj],1)
names=["E1","EBe","EBo","P1","PBe","PBo","N1","NBe","NBo"]
base=[parts(raw[0],0),parts(raw[1],0),parts(raw[1],1),parts(raw[2],0),parts(raw[3],0),parts(raw[3],1),parts(raw[4],0),parts(raw[5],0),parts(raw[5],1)]
cleared=[]
for name,pp in zip(names,base):
 den=oo
 for vv in pp.values():
  paid(vv);den=den*(vv.d/den.gcd(vv.d))
 nums=[pp[j].n*(den/pp[j].d) if j in pp else zz for j in range(max(pp,default=-1)+1)]
 raw_nums=list(nums);removed_coefficient=oo
 for atom in units:
  while any(nums):
   gg=atom
   for nn in nums:gg=gg.gcd(nn)
   if int(gg.total_degree())==0:break
   previous=list(nums);nums=[nn/gg for nn in nums]
   assert all(a0==b0*gg for a0,b0 in zip(previous,nums));removed_coefficient*=gg
 if any(nums):
  first=next(nn for nn in nums if nn)
  scale0=next(iter(first.to_dict().values()))
  nums=[nn/scale0 for nn in nums];removed_coefficient*=scale0
 assert all(a0==b0*removed_coefficient for a0,b0 in zip(raw_nums,nums))
 while nums and not nums[-1]:nums.pop()
 cleared.append(nums)
 say("original_L0_symmetric_nonzero_l_condition",name=name,tDegree=len(nums)-1,coefficientProfiles=[profile(nn) for nn in nums],claimExcluded=False)
assert len(cleared[3])<=2
def norm(po):
 po=strip_units(po)
 return po/next(iter(po.to_dict().values())) if po else po
def det(mm):
 if not mm:return oo
 if len(mm)==1:return mm[0][0]
 return sum(((-1)**j*mm[0][j]*det([row[:j]+row[j+1:] for row in mm[1:]]) for j in range(len(mm)) if mm[0][j]),zz)
def resultant(p0,q0):
 if not p0 or not q0:return zz
 n=len(p0)-1;m=len(q0)-1
 if n==0:return p0[0]**m if m else p0[0]
 if m==0:return q0[0]**n
 matrix=[[zz]*i+p0[::-1]+[zz]*(m-1-i) for i in range(m)]
 matrix.extend([[zz]*i+q0[::-1]+[zz]*(n-1-i) for i in range(n)])
 return det(matrix)
alpha=cleared[3][1] if len(cleared[3])==2 else zz
beta=cleared[3][0] if cleared[3] else zz
eqs=[]
if not alpha and beta:eqs.append(("P1_constant",norm(beta)))
for name,co in zip(names,cleared):
 if not co or name=="P1":continue
 degree=len(co)-1
 raw_value=sum((v*(-beta)**j*alpha**(degree-j) for j,v in enumerate(co)),zz)
 value=norm(raw_value)
 if value:
  divisor=raw_value/value;assert divisor*value==raw_value and int(strip_units(divisor).total_degree())==0
 if value:eqs.append(("P1_"+name,value))
for name,po in eqs:say("original_L0_symmetric_nonzero_l_two_parameter_projection",name=name,profile=profile(po),allP1ZeroLeadingFibersRetained=True,claimExcluded=False)
assert eqs
eqs.sort(key=lambda item:(int(item[1].degrees()[1]),int(item[1].total_degree()),len(item[1].to_dict())))



lookup=dict(eqs)
alpha0=norm(alpha);beta0=norm(beta)
assert int(alpha0.degrees()[0])==2 and int(beta0.degrees()[0])==1
curveG=384*lp**7*wp**3 + 576*lp**7*wp**2 + 192*lp**7*wp - 128*lp**6*wp**4 - 1472*lp**6*wp**3 - 1904*lp**6*wp**2 - 464*lp**6*wp + 32*lp**6 + 352*lp**5*wp**4 + 2304*lp**5*wp**3 + 2592*lp**5*wp**2 + 368*lp**5*wp - 96*lp**5 - 400*lp**4*wp**4 - 1936*lp**4*wp**3 - 1916*lp**4*wp**2 - 20*lp**4*wp + 120*lp**4 + 248*lp**3*wp**4 + 952*lp**3*wp**3 + 828*lp**3*wp**2 - 156*lp**3*wp - 84*lp**3 - 88*lp**2*wp**4 - 264*lp**2*wp**3 - 194*lp**2*wp**2 + 120*lp**2*wp + 36*lp**2 + 16*lp*wp**4 + 28*lp*wp**3 + 10*lp*wp**2 - 42*lp*wp - 9*lp + 4*wp**3 + 4*wp**2 + 6*wp + 1

def degree0(p,i):return int(p.degrees()[i]) if p else -1
def leading0(p,i):
 d=degree0(p,i)
 return ctx.from_dict({tuple(0 if j==i else int(m[j]) for j in range(3)):a for m,a in p.to_dict().items() if int(m[i])==d})
physical=list(units)
curveW=4*lp*wp+2*lp-2*wp*wp-4*wp-1
Kcurve=norm(alpha0.resultant(beta0,'rho'))
units=physical+[curveW,curveG,Kcurve,alpha0]
Vcurve=norm(leading0(lookup['P1_E1'],0))
assert profile(Vcurve)['sha256']=='2cb9819af2ad4da973bc3abbf2f06d07f00cd1432f820fb534734ee0b24ca10e'
assert list(map(int,Vcurve.degrees()))==[0,4,6]
units.append(Vcurve)
# Every factor of this rho-leading coefficient is now independently paid.
FE=lookup['P1_E1'];lcFE=leading0(FE,0)
assert degree0(FE,0)==5 and int(strip_units(lcFE).total_degree())==0
assert int(strip_units(alpha).total_degree())==0
chart=[curveW,curveG,Kcurve,Vcurve,alpha0]
input_rows=[]
for name in names:
 if name=='P1':continue
 raw=lookup['P1_'+name];rr=norm(raw)
 assert rr
 div=raw/rr;assert div*rr==raw and int(strip_units(div).total_degree())==0
 input_rows.append(('original_P1_'+name,rr))
# One paid-leading rho reduction is a true original ideal combination.
FN=lookup['P1_N1'];lcFN=leading0(FN,0)
rawR=lcFE*FN-lcFN*FE;reducedR=norm(rawR)
assert reducedR and degree0(reducedR,0)<5
factorR=rawR/reducedR
assert factorR*reducedR==lcFE*FN-lcFN*FE
assert int(strip_units(factorR).total_degree())==0
input_rows.append(('original_mean_normal_rho4_return',reducedR))
assert len(input_rows)==9
for name,rr in input_rows:say('full_original_L0_paid_leading_generator',name=name,profile=profile(rr),originalIdentityVerified=True,claimExcluded=False)
say('full_original_L0_paid_leading_input',originalConditions=names,originalP1Reconstruction='t=-beta/alpha',allOriginalNPEvenOddRetained=True,rho5LeadingPaid=True,originalPhysicalUnits=[profile(x) for x in physical],independentlyPaidChartUnits=[dict(name=nm,profile=profile(x)) for nm,x in zip(['W','G','K','V','alpha'],chart)],noGlobalBetaLeadingAssumption=True,claimExcluded=False)

# NEW original bounded-rho Macaulay matrix: no large X/Y projection is run.
row_specs=[('P1_E1',0),('P1_E1',1),('P1_E1',2),('P1_N1',0),('P1_N1',1),('P1_N1',2),('P1_EBo',0),('P1_EBe',0)]
row_polys=[lookup[name]*rp**shift for name,shift in row_specs]
columns=list(range(7,-1,-1));matrix=[]
for po in row_polys:
 assert degree0(po,0)<=7
 cs=[ctx.from_dict({(0,int(m[1]),int(m[2])):a for m,a in po.to_dict().items() if int(m[0])==d}) for d in columns]
 assert sum((cc*rp**d for cc,d in zip(cs,columns)),zz)==po
 matrix.append(cs)
say('original_eight_by_eight_rho_matrix',rows=row_specs,columns=columns,sha256=hashlib.sha256('|'.join(str(c) for row in matrix for c in row).encode()).hexdigest(),sourceSha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),claimExcluded=False)
B=[row[:] for row in matrix];previous=oo;operations=[];sign=1
for z0 in range(7):
 if not B[z0][z0]:
  pivotrow=next((i for i in range(z0+1,8) if B[i][z0]),None)
  assert pivotrow is not None,'selected matrix rank deficient before final column'
  B[z0],B[pivotrow]=B[pivotrow],B[z0];operations.append(('swap',z0,pivotrow));sign=-sign
 pivot=B[z0][z0]
 multipliers=[B[i][z0] for i in range(z0+1,8)]
 operations.append(('eliminate',z0,pivot,previous,multipliers))
 for i in range(z0+1,8):
  for j0 in range(z0+1,8):
   numerator=pivot*B[i][j0]-B[i][z0]*B[z0][j0]
   quotient=numerator/previous;assert quotient*previous==numerator;B[i][j0]=quotient
  B[i][z0]=zz
 previous=pivot
 say('original_eight_by_eight_bareiss_step',step=z0+1,diagonalProfile=profile(B[z0+1][z0+1]),allExactDivisionsMultipliedBack=True,claimExcluded=False)
D=B[7][7];assert D
# Recover the polynomial constant-coordinate cofactor row.  The final
# Bareiss pivot supplies the last cofactor; only the pivot-coordinate
# coefficient changes at each reverse step, preserving exact division.
cofactor=[zz]*8;cofactor[-1]=operations[-1][2]
for op in reversed(operations):
 if op[0]=='swap':
  _,i,j0=op;cofactor[i],cofactor[j0]=cofactor[j0],cofactor[i];continue
 _,z0,pivot,prev,multipliers=op
 numerator=-sum((cofactor[i]*multipliers[i-z0-1] for i in range(z0+1,8)),zz)
 quotient=numerator/pivot;assert quotient*pivot==numerator;cofactor[z0]=quotient
for j0 in range(8):assert sum((cofactor[i]*matrix[i][j0] for i in range(8)),zz)==(D if j0==7 else zz)
assert sum((cofactor[i]*row_polys[i] for i in range(8)),zz)==D
necessary=norm(D);scaleD=D/necessary
assert scaleD*necessary==D and int(strip_units(scaleD).total_degree())==0
say('complete_original_eight_by_eight_parameter_curve',determinant=profile(D),necessaryCurve=profile(necessary),cofactorIdentityAllEightColumnsVerified=True,constantColumnExactlyOne=True,allRemovedFactorsPaid=True,pivotZeroFibresRetained=True,claimExcluded=False)

# NEW only two geometric parameters, retaining three full original curves.
X=norm(FE.resultant(FN,'rho'));Y=norm(FE.resultant(lookup['P1_EBe'],'rho'))
assert list(map(int,X.degrees()))==[0,34,52] and len(X.to_dict())==1580
assert list(map(int,Y.degrees()))==[0,78,95] and len(Y.to_dict())==6379
parameter_units=[]
for name,atom in [('physical_'+str(i),a) for i,a in enumerate(physical)]+list(zip(['W','G','K','V','alpha'],chart)):
 if int(atom.degrees()[0])==0:
  assert int(strip_units(atom).total_degree())==0
  parameter_units.append((name,atom))
assert len(parameter_units)==10
curves=[('C39_53',necessary),('X34_52',X),('Y78_95',Y)]
for name,curve in curves:
 assert int(curve.degrees()[0])==0;say('original_two_parameter_necessary_curve',name=name,profile=profile(curve),claimExcluded=False)
say('original_two_parameter_paid_units',units=[dict(name=name,profile=profile(a)) for name,a in parameter_units],noUnpaidLeadingCoefficientInverted=True,claimExcluded=False)
Spaid='*'.join('('+str(a)+')' for name,a in parameter_units)
smoke_script='ring smokeRing=0,(s),dp;\nideal smoke=s,s-1;matrix smc;ideal smg=liftstd(smoke,smc,"std");matrix smp=matrix(smoke)*smc;\nif(size(smg)==1 && smg[1]==1 && nrows(smp)==1 && ncols(smp)==1 && smp[1,1]==1){print("ISP_L0_PARAMETER_CURVES_STD_SMOKE_VERIFIED");}else{print("ISP_L0_PARAMETER_CURVES_STD_SMOKE_FAILED");}quit;\n'
script='ring isp=0,(invPaid,w,lam),dp;\noption(redSB);\n'
script+='poly Spaid='+Spaid+';\n'
script+='ideal I='+',\n'.join(str(curve) for name,curve in curves)+',invPaid*Spaid-1;\n'
script+='print("ISP_L0_BEGIN_PARAMETER_CURVES_QQ_LIFT");matrix cert;ideal GB=liftstd(I,cert,"slimgb");print("ISP_L0_PARAMETER_CURVES_LIFT_RETURNED");matrix product=matrix(I)*cert;\n'
script+='if(size(GB)==1 && GB[1]==1 && nrows(product)==1 && ncols(product)==1 && product[1,1]==1){print("ISP_L0_PARAMETER_CURVES_QQ_UNIT_VERIFIED");int q;for(q=1;q<=nrows(cert);q++){print(q);print(deg(cert[q,1]));print(size(cert[q,1]));}}else{print("ISP_L0_PARAMETER_CURVES_NO_UNIT_IDENTITY");print(size(GB));print(dim(GB));}quit;\n'
say('original_parameter_curves_QQ_input_built',geometricVariables=['lam','w'],auxiliaryVariables=['invPaid'],variables=3,nonSaturationGenerators=3,paidUnitCount=len(parameter_units),scriptBytes=len(script.encode()),scriptSha256=hashlib.sha256(script.encode()).hexdigest(),smokeScriptSha256=hashlib.sha256(smoke_script.encode()).hexdigest(),sourceSha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),claimExcluded=False)
signal.alarm(0)
if '--build-only' in sys.argv:
 say('build_only_complete',allOriginalIdentitiesAndTracesVerified=True,claimExcluded=False);raise SystemExit(0)
singular=shutil.which('Singular');assert singular is not None
version=subprocess.run([singular,'--version'],capture_output=True,text=True,timeout=15)
say('singular_version',returncode=version.returncode,version=(version.stdout+version.stderr).splitlines()[0])
limit=int(os.environ.get('ISP_ALG_SECONDS','1200'))
def limits():resource.setrlimit(resource.RLIMIT_AS,(8*1024**3,8*1024**3))
def process_output(stdout,stderr):return ''.join(part.decode(errors='replace') if isinstance(part,bytes) else (part or '') for part in [stdout,stderr])
def diagnostics(output):return [ln for ln in output.splitlines() if ln.lstrip().startswith('?')]
with tempfile.TemporaryDirectory(prefix='isp-L0-parameter-curves-') as td:
 smoke_path=Path(td)/'smoke.sing';smoke_path.write_text(smoke_script)
 try:
  sm=subprocess.run([singular,'-q',str(smoke_path)],capture_output=True,text=True,timeout=45,preexec_fn=limits)
 except subprocess.TimeoutExpired as ex:
  output=process_output(ex.stdout,ex.stderr)
  say('independent_std_smoke_timeout',timeoutSeconds=45,stdoutSha256=hashlib.sha256(output.encode()).hexdigest(),stdoutBytes=len(output.encode()),text=output[:30000],fullInputWritten=False,fullAlgorithmStarted=False,claimExcluded=False);raise
 smoke_output=sm.stdout+sm.stderr;smoke_lines=set(sm.stdout.splitlines());smoke_diagnostics=diagnostics(smoke_output)
 smoke_passed=sm.returncode==0 and 'ISP_L0_PARAMETER_CURVES_STD_SMOKE_VERIFIED' in smoke_lines and not smoke_diagnostics
 say('independent_std_smoke_return',returncode=sm.returncode,smokeVerified=smoke_passed,singularDiagnosticLines=len(smoke_diagnostics),stdoutSha256=hashlib.sha256(smoke_output.encode()).hexdigest(),stdoutBytes=len(smoke_output.encode()),text=smoke_output[:30000],fullInputWritten=False,fullAlgorithmStarted=False,claimExcluded=False)
 assert smoke_passed,'separate std smoke failed: full input is not written or started'
 path=Path(td)/'input.sing';path.write_text(script)
 say('full_slimgb_start_after_verified_independent_smoke',fullScriptSha256=hashlib.sha256(path.read_bytes()).hexdigest(),smokeVerified=True,timeoutSeconds=limit,addressSpaceBytes=8*1024**3,claimExcluded=False)
 try:
  rr=subprocess.run([singular,'-q',str(path)],capture_output=True,text=True,timeout=limit,preexec_fn=limits)
  output=rr.stdout+rr.stderr;lines=set(rr.stdout.splitlines());error_lines=diagnostics(output)
  passed=rr.returncode==0 and 'ISP_L0_PARAMETER_CURVES_QQ_UNIT_VERIFIED' in lines and not error_lines
  say('actual_original_parameter_curves_L0_QQ_return',returncode=rr.returncode,actualUnitVerified=passed,singularDiagnosticLines=len(error_lines),stdoutSha256=hashlib.sha256(output.encode()).hexdigest(),stdoutBytes=len(output.encode()),text=output[:30000],claimExcluded=passed)
  assert passed,'original three-curve parameter L0 system has not produced a unit certificate'
 except subprocess.TimeoutExpired as ex:
  output=process_output(ex.stdout,ex.stderr)
  say('actual_original_parameter_curves_L0_QQ_timeout',timeoutSeconds=limit,stdoutSha256=hashlib.sha256(output.encode()).hexdigest(),stdoutBytes=len(output.encode()),text=output[:30000],claimExcluded=False);raise
say('complete',identity='matrix(original three-curve parameter L0 necessary localized generators)*certificate=[1]',scope='remaining original L0 with all W/G/K/V boundaries paid',ordinaryISPClaim=False,claimExcluded=True)
