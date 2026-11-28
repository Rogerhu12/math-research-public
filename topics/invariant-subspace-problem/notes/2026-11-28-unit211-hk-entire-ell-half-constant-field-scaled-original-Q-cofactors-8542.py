#!/usr/bin/env python3
"""NEW correct h=k: the ENTIRE ell=1/2 constant field, Delta already paid.
K=QQ[lambda]/(3 lambda^2-2 lambda+1), before any weight expansion.
Scale the true original Gram by H=M Q Delta; no Delta/norm inverse.
Fixed original Q Sylvester cofactors and complete K[u] Bezout returns.
Only original paid weights are removed. All other heads/zero fibres stay.
180 seconds / 4 GiB; self-contained, no old spectral or projection gate.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx
START=time.perf_counter();DEADLINE=START+180
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
REAL_TIMER=signal.setitimer
REAL_TIMER(signal.ITIMER_REAL,180)
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 180 second boundary')
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(',',':')),flush=True)
stats=dict(constantFieldInverseReturns=0,coefficientExactDivisionReturns=0,
           paidNormalizationProducts=0,originalGramReturns=0,
           originalMomentReturns=0,fixedBareissProducts=0,
           fullFixedCofactorReturns=0,wholeFieldBezoutReturns=0,
           finalEightSourceReturns=0)
ctx=fmpq_mpoly_ctx.get(('u','Q'),'lex')
up,Qp=ctx.gens();Zp=ctx.constant(0);Op=ctx.constant(1)
def pp(x):
 return x if hasattr(x,'to_dict') else ctx.constant(fmpq(x))
class CP:
 """K[u,Q]; the TWO lambda embeddings are never selected separately."""
 _level=0
 def __init__(self,a=0,b=0):
  if isinstance(a,CP):
   assert not b
   self.a=a.a;self.b=a.b
  else:self.a=pp(a);self.b=pp(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,o):
  if getattr(o,'_level',0)>0:return NotImplemented
  o=CP(o);return CP(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return CP(-self.a,-self.b)
 def __sub__(self,o):
  if getattr(o,'_level',0)>0:return NotImplemented
  return self+-CP(o)
 def __rsub__(self,o):
  if getattr(o,'_level',0)>0:return NotImplemented
  return CP(o)+-self
 def __mul__(self,o):
  if getattr(o,'_level',0)>0:return NotImplemented
  o=CP(o)
  return CP(self.a*o.a-self.b*o.b/3,
            self.a*o.b+self.b*o.a+2*self.b*o.b/3)
 __rmul__=__mul__
 def conj(self):return CP(self.a+2*self.b/3,-self.b)
 def norm(self):
  out=self*self.conj();assert not out.b
  return out.a
 def constant(self):
  return all(not p or int(p.total_degree())==0 for p in (self.a,self.b))
 def cinv(self):
  assert self and self.constant()
  nn=self.norm();assert nn and int(nn.total_degree())==0
  c=nn.to_dict().get((0,0),fmpq(0));assert c
  cc=self.conj();out=CP(cc.a/c,cc.b/c)
  assert self*out==CP(1)
  stats['constantFieldInverseReturns']+=1
  return out
 def __truediv__(self,o):
  if getattr(o,'_level',0)>0:return NotImplemented
  o=CP(o);assert o.constant(),'nonconstant field inverse forbidden'
  return self*o.cinv()
 def __rtruediv__(self,o):
  if getattr(o,'_level',0)>0:return NotImplemented
  return CP(o)*self.cinv()
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  a=CP(self);out=CP(1)
  while n:
   if n&1:out=out*a
   n//=2
   if n:a=a*a
  return out
 def __eq__(self,o):
  if getattr(o,'_level',0)>0:return NotImplemented
  o=CP(o);return self.a==o.a and self.b==o.b
 def degree(self,axis):
  return max((int(p.degrees()[axis]) for p in (self.a,self.b) if p),default=-1)
 def total(self):
  return max((int(p.total_degree()) for p in (self.a,self.b) if p),default=-1)
def exact_try(a,b):
 """POLYNOMIAL division, including a norm intermediate, never localization."""
 a=CP(a);b=CP(b);assert b
 if not a:return CP()
 if b.constant():return a/b
 if not b.b:
  qa,ra=divmod(a.a,b.a);qb,rb=divmod(a.b,b.a)
  if ra or rb:return None
  out=CP(qa,qb)
 else:
  numer=a*b.conj();den=b.norm();assert den
  qa,ra=divmod(numer.a,den);qb,rb=divmod(numer.b,den)
  if ra or rb:return None
  out=CP(qa,qb)
 assert out*b==a
 stats['coefficientExactDivisionReturns']+=1
 return out
def exact(a,b):
 out=exact_try(a,b)
 assert out is not None,'required exact polynomial quotient did not exist'
 return out
def lead(a):
 a=CP(a);assert a
 keys=set(a.a.to_dict())|set(a.b.to_dict())
 mm=max(keys)
 return CP(a.a.to_dict().get(mm,0),a.b.to_dict().get(mm,0))
def profile(a):
 a=CP(a);data=[]
 for i,p in enumerate((a.a,a.b)):
  data.extend([[i,int(mm[0]),int(mm[1]),str(cc)] for mm,cc in sorted(p.to_dict().items())])
 raw=json.dumps(data,separators=(',',':')).encode()
 return dict(degrees_u_Q=[a.degree(0),a.degree(1)],weightTotalDegree=a.total(),
             terms=len(data),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
lam=CP(0,1);u=CP(up);Q=CP(Qp);delta=1-Q
ell=CP(fmpq(1,2));xi=1-lam;T=(1-lam)/2
hh=2-lam;w=3*(lam-1)/2;S=5-4*lam;eta=4-3*lam
aa=1-ell;m=u-ell
A=2*lam*lam-2*lam+1;B=4*lam**3-6*lam*lam+3*lam-1
assert 3*lam*lam-2*lam+1==0
assert A==(1-2*lam)/3 and B==(1-5*lam)/9
assert 2*A**3==B**2 and xi*A==B and T*B==A*A
assert hh==1+xi and w==lam-1-T and S==2*xi+3-2*lam
M=u-u*u-Q/4
V2=2*u-ell*Q;T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
Phi=T0+4*u-4+Q
P02=(2-3*u)*V2-Q*u+2*u**3
Pf=T0*(J-Q);G=lam*P02-(1-u)*T0
Pc=Q*P02*(ell+T)-G*T0
NF=(3-4*lam)*Q+J*xi*eta
NC=eta*(-G*xi+Q*w*u)
Delta=Phi*NF-S*xi*Pf
Tnum=Pf*NC-Pc*NF
Fnum=S*xi*Pc-Phi*NC
assert T0==2*M and J-Q==2*M and Pf==4*M*M
assert P02==-2*M*(u-2)
assert 4*M==delta-4*m*m
assert Pf*Fnum+Phi*Tnum+Pc*Delta==0
assert NF*Fnum+S*xi*Tnum+NC*Delta==0
assert Delta
say('new_whole_half_weight_constant_field_and_original_Cramer',
 lambdaPolynomialAscending=[1,-2,3],allTwoEmbeddingsRetained=True,
 originalEllHalfIdentity='2 A^3-B^2=(2 lambda-1)^2(3 lambda^2-2 lambda+1)',
 halfLambdaAlreadyPhysicallyExcluded=True,
 specialisedIdentities=['ell=1/2','xi=1-lambda','T=(1-lambda)/2',
                       'T0=J-Q=2M','Pf=4M^2','P02=-2M(u-2)'],
 newBranchUnitUminusTwoFromOriginalP02=True,
 DeltaPaidOnlyByWholeCorrectCollisionDeltaZeroExclusion=True,
 Delta=profile(Delta),Fnum=profile(Fnum),Tnum=profile(Tnum),
 noPhysicalDOrPhiOrEqualWeightDifferenceInverse=True,
 noOldTwoSpectralFieldTargetOrProjectionReplayed=True)

# The ONLY rational weight denominator in the scaled Gram is a power of delta.
class DD:
 _level=1
 def __init__(self,n=0,e=0):
  if isinstance(n,DD):
   assert not e
   self.n=n.n;self.e=n.e;return
  n=CP(n);assert isinstance(e,int) and e>=0
  if not n:self.n=CP();self.e=0;return
  while e:
   q=exact_try(n,delta)
   if q is None:break
   n=q;e-=1
  self.n=n;self.e=e
 def __bool__(self):return bool(self.n)
 def __add__(self,o):
  if getattr(o,'_level',0)>1:return NotImplemented
  o=DD(o);d=max(self.e,o.e)
  return DD(self.n*delta**(d-self.e)+o.n*delta**(d-o.e),d)
 __radd__=__add__
 def __neg__(self):return DD(-self.n,self.e)
 def __sub__(self,o):
  if getattr(o,'_level',0)>1:return NotImplemented
  return self+-DD(o)
 def __rsub__(self,o):
  if getattr(o,'_level',0)>1:return NotImplemented
  return DD(o)+-self
 def __mul__(self,o):
  if getattr(o,'_level',0)>1:return NotImplemented
  o=DD(o);return DD(self.n*o.n,self.e+o.e)
 __rmul__=__mul__
 def __truediv__(self,o):
  if getattr(o,'_level',0)>1:return NotImplemented
  if isinstance(o,DD):
   assert o.e==0 and o.n.constant();o=o.n
  o=CP(o);assert o.constant()
  return DD(self.n/o,self.e)
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  return DD(self.n**n,self.e*n)
 def __eq__(self,o):
  if getattr(o,'_level',0)>1:return NotImplemented
  o=DD(o)
  return self.n*delta**o.e==o.n*delta**self.e
class EE:
 _level=2
 def __init__(self,e=0,o=0):
  if isinstance(e,EE):
   assert not o
   self.e=e.e;self.o=e.o
  else:self.e=DD(e);self.o=DD(o)
 def __bool__(self):return bool(self.e) or bool(self.o)
 def __add__(self,v):
  v=EE(v);return EE(self.e+v.e,self.o+v.o)
 __radd__=__add__
 def __neg__(self):return EE(-self.e,-self.o)
 def __sub__(self,v):return self+-EE(v)
 def __rsub__(self,v):return EE(v)+-self
 def __mul__(self,v):
  v=EE(v);return EE(self.e*v.e+delta*self.o*v.o,self.e*v.o+self.o*v.e)
 __rmul__=__mul__
 def __truediv__(self,v):
  return EE(self.e/v,self.o/v)
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  out=EE(1)
  for _ in range(n):out=out*self
  return out
 def conj(self):return EE(self.e,-self.o)
 def __eq__(self,v):
  v=EE(v);return self.e==v.e and self.o==v.o
bc=DD(M/4,1)
assert 4*delta*bc==M
rho=EE(0,1);b=EE(ell/2,DD(m/2,1));c=b.conj()
p=1+rho;qq=1-rho
assert b*c==EE(bc) and b+c==ell and b*p+c*qq==u and p*qq==Q
H=M*Q*Delta
ft=M*Q*Fnum
VVnum=J*Fnum-G*Delta+Tnum
WWnum=M*Delta+2*u*Fnum
Vt=M*VVnum
xt=(u-ell*Q)*VVnum-m*Q*WWnum
yt=ell*Q*WWnum-u*VVnum
tt=4*delta*Tnum
A1t=2*M*((Q-J)*Fnum+G*Delta)
assert DD(A1t)==2*DD(ft)-2*DD(Vt)+2*bc*tt
X=EE(xt,yt);Y=X.conj()
assert b*X+c*Y==Vt
assert b*p*X+c*qq*Y==M*Q*WWnum
assert Pf*ft+bc*Phi*Q*tt+Pc*H==0
assert NF*ft+bc*S*xi*Q*tt+NC*H==0
rr=X-aa*H*p-c*tt;ss=Y-aa*H*qq-b*tt
rows=[[EE(),EE(),H*p,H*qq],[EE(),EE(A1t),rr,ss],
      [H*p,rr,EE(),EE(tt)],[H*qq,ss,EE(tt),EE()]]
one=[EE(1),EE(),EE(1),EE(1)]
def vm(vv,ww):
 return [vv[0]*ww[0],vv[0]*ww[1]+vv[1]*ww[0],
         vv[2]*ww[2],vv[3]*ww[3]]
def tau(vv):return aa*vv[0]+vv[1]+b*vv[2]+c*vv[3]
def DK(vv):return [tau(vm(row,vv)) for row in rows]
d=DK(one);F2=tau(d);Kd=DK(d)
assert d[0]==H*u and d[2]==X and d[3]==Y and F2==2*ft
stats['originalGramReturns']+=13
def N4(vv):
 vv2=vm(vv,vv);tv=tau(vv)
 return (2*tau(vm(d,vv2))-F2*tau(vv2)
         -4*tv*tau(vm(d,vv))+2*F2*tv*tv+tau(vm(vv,DK(vv))))
def center(vv):
 tv=tau(vv);return [v-tv*e for v,e in zip(vv,one)]
def P2(vv):
 vc=center(vv);return tau(vm(vm(vc,vc),vc))
g0,g1,gB,gC=rows
P0s=H**3*P02
N0=N4(g0);Nrow1=N4(g1)
NJ=N4([x+y for x,y in zip(g0,g1)])-N0-Nrow1
C0=center(g0);C1=center(g1);PJ=3*tau(vm(vm(C0,C0),C1))
assert P2(g0)==P0s and N0==2*lam*P0s and PJ==3*w*P0s
assert aa+w+ell*hh==lam and aa+2*w+ell*hh*hh==2*lam*lam
assert aa+3*w+ell*hh**3==4*lam**3
VV=[EE(1),EE(w),EE(hh),EE(hh)]
assert N4(VV)==0
e0=tau(vm(g0,g0))-2*Kd[0]-2*vm(d,d)[0]+2*F2*d[0]
assert not e0
stats['originalMomentReturns']+=8
# True dual square at index 1 is 2*d0*d1, NEVER d1*d1.
e1=2*tau(vm(g0,g1))-2*Kd[1]-2*vm(d,d)[1]+2*F2*d[1]
eb=tau(vm(gB,gB))-2*Kd[2]-2*vm(d,d)[2]+2*F2*d[2]
ec=tau(vm(gC,gC))-2*Kd[3]-2*vm(d,d)[3]+2*F2*d[3]
n1=NJ-4*lam*w*P0s
nb=N4(gB)-2*lam*hh*hh*P0s
pb=P2(gB)-hh**3*P0s
assert not e1.o and not n1.o and ec==eb.conj()
assert N4(gC)-2*lam*hh*hh*P0s==nb.conj()
assert P2(gC)-hh**3*P0s==pb.conj()
stats['originalGramReturns']+=5
names=['E1even','EBe','EBo','N1jet','NB_even','NB_odd','PB_even','PB_odd']
raw=[e1.e,eb.e,eb.o,n1.e,nb.e,nb.o,pb.e,pb.o]
homogeneity=[2,2,2,3,3,3,3,3]
paid=[('u',u),('u-1',u-1),('u-2 from P02',u-2),('Q',Q),
      ('delta',delta),('M',M),('Delta correct whole exclusion',Delta)]
def strip_paid(a,atoms):
 a=CP(a);removed=CP(1);history=[]
 if not a:return a,removed,history
 for name,atom in atoms:
  atom=CP(atom);assert atom and not atom.constant()
  count=0
  while a:
   tick()
   q=exact_try(a,atom)
   if q is None:break
   a=q;removed=removed*atom;count+=1
  if count:history.append(dict(unit=name,wholeFactorDivisions=count))
 lc=lead(a);a=a/lc;removed=removed*lc
 return a,removed,history
originals=[];normalised=[];removed_rows=[];row_delta_powers=[];row_histories=[]
def common_paid(histories,atoms):
 out=CP(1)
 for label,atom in atoms:
  count=max((next((x['wholeFactorDivisions'] for x in h if x['unit']==label),0) for h in histories),default=0)
  out=out*atom**count
 return out
for name,value,power in zip(names,raw,homogeneity):
 v,removed,history=strip_paid(value.n,paid)
 assert DD(v*removed,value.e)==value
 stats['paidNormalizationProducts']+=1
 originals.append(value);normalised.append(v);removed_rows.append(removed)
 row_delta_powers.append(value.e);row_histories.append(history)
 say('new_half_weight_scaled_true_original_row',name=name,
     originalHomogeneityPowerOfH=power,clearedDeltaDenominatorPower=value.e,
     rawNumerator=profile(value.n),necessaryPolynomial=profile(v),
     removedOnlyOriginalPaidWholeFactors=history,
     exactOriginalScaledRowReturned=True,
     bothLambdaAndRhoEmbeddingsRetained=True)
say('new_half_weight_all_eight_correct_original_rows',
 originalNames=names,completeTrueDualGram=True,originalE0N0PjetNVReturned=True,
 commonScaleH=profile(H),noDeltaNormOrUnpaidHeadInverse=True,
 allZeroLeadingCoefficientsRetained=True,
 originalChartUnits=['u','u-1','Q','1-Q','M','P02','Delta'],
 extraUminusTwoDerivedFromP02=True,physicalDNeverInverted=True)

def qcoeff(a):
 a=CP(a);n=a.degree(1)+1
 out=[]
 for j in range(n):
  parts=[]
  for p0 in (a.a,a.b):
   parts.append(ctx.from_dict({(int(mm[0]),0):cc for mm,cc in p0.to_dict().items() if int(mm[1])==j}))
  out.append(CP(*parts))
 return out
def fixed_q_cofactor(pa,pb,labels):
 """New fixed Sylvester, exact row-return including ALL leading zero fibres."""
 ca=qcoeff(pa);cb=qcoeff(pb);mdeg=len(ca)-1;ndeg=len(cb)-1
 if mdeg<0 or ndeg<0:
  return dict(zero=True,reason='an original input is identically zero')
 if mdeg==0:
  assert ca[0]==pa
  assert CP(1)*pa+CP()*pb==pa
  stats['fullFixedCofactorReturns']+=1
  return dict(zero=False,scalar=pa,ta=CP(1),tb=CP(),capacity=[0,ndeg],size=1)
 if ndeg==0:
  assert cb[0]==pb
  assert CP()*pa+CP(1)*pb==pb
  stats['fullFixedCofactorReturns']+=1
  return dict(zero=False,scalar=pb,ta=CP(),tb=CP(1),capacity=[mdeg,0],size=1)
 size=mdeg+ndeg
 S0=[]
 for j in range(ndeg):S0.append([CP()]*j+ca+[CP()]*(size-j-len(ca)))
 for j in range(mdeg):S0.append([CP()]*j+cb+[CP()]*(size-j-len(cb)))
 assert len(S0)==size and all(len(row)==size for row in S0)
 mat=[[S0[j][i] for j in range(size)]+[CP(int(i==0))] for i in range(size)]
 prev=CP(1)
 for k in range(size-1):
  tick()
  pivot=next((i for i in range(k,size) if mat[i][k]),None)
  if pivot is None:
   return dict(zero=True,reason='fixed Sylvester identically singular',
               capacity=[mdeg,ndeg],size=size)
  if pivot!=k:mat[k],mat[pivot]=mat[pivot],mat[k]
  pk=mat[k][k]
  for i in range(k+1,size):
   aik=mat[i][k]
   for j in range(k+1,size+1):
    numerator=pk*mat[i][j]-aik*mat[k][j]
    mat[i][j]=exact(numerator,prev)
    assert mat[i][j]*prev==numerator
    stats['fixedBareissProducts']+=1
   mat[i][k]=CP()
  prev=pk
  if k==0 or k+2==size:
   say('new_fixed_original_Q_cofactor_step',sourceRows=labels,
       size=size,completedStep=k,pivot=profile(pk))
 det=mat[-1][-2]
 if not det:
  return dict(zero=True,reason='fixed Sylvester final determinant zero',
              capacity=[mdeg,ndeg],size=size)
 tags=[CP() for _ in range(size)]
 for i in range(size-1,-1,-1):
  numerator=det*mat[i][-1]-sum((mat[i][j]*tags[j] for j in range(i+1,size)),CP())
  tags[i]=exact(numerator,mat[i][i])
 for j in range(size):
  assert sum((tags[i]*S0[i][j] for i in range(size)),CP())==(det if j==0 else CP())
 ta=sum((tags[j]*Q**j for j in range(ndeg)),CP())
 tb=sum((tags[ndeg+j]*Q**j for j in range(mdeg)),CP())
 assert ta*pa+tb*pb==det and det.degree(1)<=0
 stats['fullFixedCofactorReturns']+=1
 return dict(zero=False,scalar=det,ta=ta,tb=tb,capacity=[mdeg,ndeg],size=size)

# Small ordinary polynomial arithmetic over the WHOLE constant field K.
def trim(a):
 while a and not a[-1]:a.pop()
 return a
class PU:
 def __init__(self,a=0):
  if isinstance(a,PU):self.c=a.c[:]
  elif isinstance(a,(list,tuple)):
   self.c=trim([CP(x) for x in a]);assert all(c.constant() for c in self.c)
  else:
   aa=CP(a);assert aa.constant()
   self.c=[aa] if aa else []
 def __bool__(self):return bool(self.c)
 def __add__(self,o):
  o=PU(o);n=max(len(self.c),len(o.c))
  return PU([(self.c[i] if i<len(self.c) else CP())+
             (o.c[i] if i<len(o.c) else CP()) for i in range(n)])
 __radd__=__add__
 def __neg__(self):return PU([-c for c in self.c])
 def __sub__(self,o):return self+-PU(o)
 def __rsub__(self,o):return PU(o)+-self
 def __mul__(self,o):
  o=PU(o)
  if not self or not o:return PU()
  out=[CP() for _ in range(len(self.c)+len(o.c)-1)]
  for i,a in enumerate(self.c):
   for j,b in enumerate(o.c):out[i+j]=out[i+j]+a*b
  return PU(out)
 __rmul__=__mul__
 def __truediv__(self,c):
  c=CP(c);assert c and c.constant();iv=c.cinv()
  return PU([a*iv for a in self.c])
 def __eq__(self,o):return self.c==PU(o).c
 def degree(self):return len(self.c)-1
 def cp(self):return sum((c*u**i for i,c in enumerate(self.c)),CP())
def u_polynomial(p0):
 p0=CP(p0);assert p0.degree(1)<=0
 n=p0.degree(0)+1;out=[]
 aa=p0.a.to_dict();bb=p0.b.to_dict()
 for i in range(n):out.append(CP(aa.get((i,0),0),bb.get((i,0),0)))
 out=PU(out);assert out.cp()==p0
 return out
def udivrem(a,b):
 a=PU(a);b=PU(b);assert b
 r=PU(a);q=[CP() for _ in range(max(0,a.degree()-b.degree()+1))]
 iv=b.c[-1].cinv()
 while r and r.degree()>=b.degree():
  tick();j=r.degree()-b.degree();c=r.c[-1]*iv
  q[j]=q[j]+c;r=r-PU([CP()]*j+[c])*b
 q=PU(q);assert q*b+r==a
 stats['wholeFieldBezoutReturns']+=1
 return q,r
def uxgcd(a,b):
 a=PU(a);b=PU(b);r0,r1=a,b;s0,s1=PU(1),PU();t0,t1=PU(),PU(1)
 while r1:
  q,r=udivrem(r0,r1)
  r0,r1=r1,r;s0,s1=s1,s0-q*s1;t0,t1=t1,t0-q*t1
 if not r0:return r0,s0,t0
 lc=r0.c[-1];r0=r0/lc;s0=s0/lc;t0=t0/lc
 assert s0*a+t0*b==r0
 stats['wholeFieldBezoutReturns']+=1
 return r0,s0,t0

# Predetermined original pairs; no point/prime selection and no old target.
pair_indices=[(0,1),(0,2),(0,3),(1,5),(2,7)]
all_scalars=[];scalar_sources=[];accum=PU();bez=[]
for i,j in pair_indices:
 tick()
 rr0=fixed_q_cofactor(normalised[i],normalised[j],[names[i],names[j]])
 if rr0['zero']:
  say('new_fixed_original_Q_cofactor_zero',sourceRows=[names[i],names[j]],
      **{k:v for k,v in rr0.items() if k!='zero'},
      allFibresRetained=True,claimExcluded=False)
  continue
 det=rr0['scalar']
 core,unit,history=strip_paid(det,[('u',u),('u-1',u-1),('u-2 from P02',u-2)])
 assert core*unit==det and core.degree(1)<=0
 rr0.update(i=i,j=j,core=core,unit=unit,history=history)
 corep=u_polynomial(core)
 if not all_scalars:
  accum=corep;bez=[PU(1)]
 else:
  accum,s,t=uxgcd(accum,corep)
  bez=[s*v for v in bez]+[t]
 all_scalars.append(corep);scalar_sources.append(rr0)
 assert sum((v*c for v,c in zip(bez,all_scalars)),PU())==accum
 say('new_half_weight_fixed_original_Q_scalar_and_whole_Ku_cover',
     sourceRows=[names[i],names[j]],fixedCapacity=rr0['capacity'],
     matrixSize=rr0['size'],rawOriginalScalar=profile(det),
     onlyPureUOriginalUnitRemoval=history,
     retainedNecessaryScalar=profile(core),wholeConstantFieldGCD=profile(accum.cp()),
     completeFixedOriginalCofactorReturned=True,completeAccumulatedBezoutReturned=True,
     allTwoLambdaEmbeddingsAndQHeadZeroFibresRetained=True,
     entireHalfWeightChartExcluded=accum==1)
 if accum==1:break
if all_scalars:
 # Clear the ACTUAL old pure-u supports in the scalar traces.
 E=common_paid([r0['history'] for r0 in scalar_sources],
               [('u',u),('u-1',u-1),('u-2 from P02',u-2)])
 rowtags=[CP() for _ in names]
 for bb,r0 in zip(bez,scalar_sources):
  mult=bb.cp()*exact(E,r0['unit'])
  rowtags[r0['i']]=rowtags[r0['i']]+mult*r0['ta']
  rowtags[r0['j']]=rowtags[r0['j']]+mult*r0['tb']
 assert sum((s*r for s,r in zip(rowtags,normalised)),CP())==E*accum.cp()
 # Then return the COMPLETE eight scaled original Gram rows, not just scalars.
 Rden=common_paid(row_histories,paid)
 omegas=[s*exact(Rden,a0)*delta**ee
         for s,a0,ee in zip(rowtags,removed_rows,row_delta_powers)]
 lhs=sum((DD(om)*val for om,val in zip(omegas,originals)),DD())
 rhs=Rden*E*accum.cp()
 assert lhs==DD(rhs)
 stats['finalEightSourceReturns']+=1
 certificate=dict(targetProfile=profile(rhs),multiplierProfiles=[profile(x) for x in omegas],
                  sourceNames=names,sourceHomogeneityPowers=homogeneity)
 encoded=json.dumps(certificate,separators=(',',':')).encode()
 say('new_half_weight_complete_eight_original_source_return',
     wholeKuGCD=profile(accum.cp()),
     clearingFactorsOnlyOriginalPaidWeights=True,
     exactIdentity='sum Omega_i (H^d_i Original_i)=Rden E gcd_u',
     originalEightSourceReturn=True,
     returnedCoefficientProfilesBytes=len(encoded),
     returnedCoefficientProfilesSHA256=hashlib.sha256(encoded).hexdigest(),
     entireHalfWeightChartExcluded=accum==1,
     allUnexcludedUAndQFibresRetained=accum!=1)
 if accum!=1:
  # A genuine QQ[u] necessary cover; do NOT strip its unproved factors or powers.
  norm=accum.cp().norm()
  assert norm and all(int(mm[1])==0 for mm in norm.to_dict())
  coeffs=[norm.to_dict().get((i,0),fmpq(0)) for i in range(int(norm.degrees()[0])+1)]
  normp=fmpq_poly(coeffs);facscalar,factors=normp.factor()
  back=fmpq_poly([facscalar]);factor_records=[]
  for ff,power in factors:
   back*=ff**int(power)
   rawf=json.dumps([str(c) for c in ff],separators=(',',':')).encode()
   factor_records.append(dict(degree=int(ff.degree()),multiplicity=int(power),
                              bytes=len(rawf),sha256=hashlib.sha256(rawf).hexdigest()))
  assert back==normp
  rawn=json.dumps([str(c) for c in normp],separators=(',',':')).encode()
  say('new_half_weight_complete_QQ_u_norm_cover',
      degree=int(normp.degree()),bytes=len(rawn),sha256=hashlib.sha256(rawn).hexdigest(),
      factors=factor_records,wholeFactorProductReturned=True,
      normUsedOnlyAsPositiveNecessaryMultiple=True,
      noNormInverseAndNoUnprovedFactorRemoval=True,
      noQFibreFinitenessOrWholeExclusionClaim=True)
else:
 say('new_half_weight_no_nonzero_fixed_Q_scalar',
     allOriginalEightRowsStillNecessary=True,claimExcluded=False)
say('new_whole_half_weight_original_first_input_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 wholeConstantField=[1,-2,3],
 entireHalfWeightChartExcluded=bool(all_scalars) and accum==1,
 originalDeltaNonzeroChartOnly=True,DeltaZeroAlreadyIndependentlyClosed=True,
 allOtherWeightFibresStillOpen=True,noWholeCollisionOrOrdinaryISPClaim=True,
 noOldSpectrumOrProjectionTargetReplayed=True,noCoefficientPayloadCacheSaved=True,
 statistics=stats,peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
REAL_TIMER(signal.ITIMER_REAL,0)
