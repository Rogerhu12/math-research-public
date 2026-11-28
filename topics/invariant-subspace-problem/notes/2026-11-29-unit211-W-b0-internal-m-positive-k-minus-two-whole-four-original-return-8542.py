#!/usr/bin/env python3
"""NEW W/b0 internal m-positive, k=-2 unique residual centre.
Characteristic 1009, all e,k,u,delta,Vbar are already integral units.
Original q2/R6 force U=29/49, mu=-7/2. True E1 has f2 head
-8*delta, so f is integral. Keep the complete monic f2 AND sigma2
algebra (dimension four), including both spectrum roots and all
multiplicities. Construct the complete raw dual Gram and all values.
Only target 1; complete unquotiented ten-source polynomial return.
No m inverse, selected f/sigma root, QQ emptiness inference, old
projection/ray replay, coefficient payload, cache or execution dependency.
30 seconds /256 MiB; standard-library exact F_1009 arithmetic.
"""
import hashlib,json,resource,signal,time
START=time.perf_counter();DEADLINE=START+30;PRIME=1009
resource.setrlimit(resource.RLIMIT_AS,(256*1024**2,256*1024**2))
signal.setitimer(signal.ITIMER_REAL,30)
STAT={'baseInverseReturns':0,'rawDefinitionReturns':0,
      'monicOriginalReturns':0,'quotientDivisionReturns':0,
      'originalColumnReturns':0,'GaussianVectorReturns':0,
      'finalOriginalReturns':0}
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute30')
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True,separators=(',',':')),flush=True)
def inv(a):
 a=int(a)%PRIME;assert a
 z=pow(a,PRIME-2,PRIME);assert a*z%PRIME==1
 STAT['baseInverseReturns']+=1;return z
def rat(a,b=1):return int(a)*inv(b)%PRIME
class P:
 # Ordinary F_p[f,sigma], never a quotient or a rational-function ring.
 def __init__(self,v=0):
  if isinstance(v,P):self.c=v.c.copy();return
  if isinstance(v,dict):
   self.c={tuple(map(int,k)):int(c)%PRIME for k,c in v.items()
           if int(c)%PRIME}
  else:self.c={} if not int(v)%PRIME else {(0,0):int(v)%PRIME}
  assert all(len(k)==2 and min(k)>=0 for k in self.c)
 def __bool__(self):return bool(self.c)
 def __neg__(self):return P({k:-v for k,v in self.c.items()})
 def __add__(self,v):
  v=P(v);z=self.c.copy()
  for k,c in v.c.items():z[k]=(z.get(k,0)+c)%PRIME
  return P(z)
 __radd__=__add__
 def __sub__(self,v):return self+-P(v)
 def __rsub__(self,v):return P(v)+-self
 def __mul__(self,v):
  v=P(v);tick();z={}
  for (a,b),c in self.c.items():
   for (d,e),h in v.c.items():
    k=(a+d,b+e);z[k]=(z.get(k,0)+c*h)%PRIME
  return P(z)
 __rmul__=__mul__
 def __truediv__(self,v):
  v=P(v);assert len(v.c)==1 and (0,0) in v.c
  return self*inv(v.c[(0,0)])
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  a=self;z=P(1)
  while n:
   if n&1:z=z*a
   n//=2
   if n:a=a*a
  return z
 def __eq__(self,v):return self.c==P(v).c
 def coeff(self,i,j=0):return self.c.get((i,j),0)
 def deg(self,axis):return max((k[axis] for k in self.c),default=-1)
def profile(a):
 a=P(a);data=[[int(k[0]),int(k[1]),int(v)] for k,v in sorted(a.c.items())]
 raw=json.dumps(data,separators=(',',':')).encode()
 return {'fDegree':a.deg(0),'sigmaDegree':a.deg(1),'terms':len(data),
         'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def check(a,b):
 assert P(a)==P(b);STAT['rawDefinitionReturns']+=1
f=P({(1,0):1});sig=P({(0,1):1})
u=rat(29,49);e=(u-1)%PRIME;kk=-2%PRIME
Q=rat(40,49);delta=rat(9,49);ell=u;m=0
rho=rat(3,7);b=c=ell*inv(2)%PRIME;bc=b*c%PRIME
a=(1-ell)%PRIME;p=(1+rho)%PRIME;q=(1-rho)%PRIME
lam=rat(-1,4);mu=rat(-7,2);Tm=rat(-29,28);w=rat(-3,14)
M=ell*ell*delta%PRIME
Vbar=(u*kk+2)%PRIME
J=(2*u*(1-u)+ell*Q)%PRIME
T0=(2*u-ell*Q-2*u*u)%PRIME
Phi=(T0+4*u-4+Q)%PRIME
P02=((2-3*u)*(2*u-ell*Q)-Q*u+2*u**3)%PRIME
Ast=(4*u*Q-J)%PRIME
A2=(2*lam*lam-2*lam+1)%PRIME
B3=(4*lam**3-6*lam*lam+3*lam-1)%PRIME
D=(ell*A2-Tm*Tm)%PRIME
K=(ell*ell*B3-3*ell*A2*Tm+2*Tm**3)%PRIME
Cst=(Ast*m*m+J*delta*ell*ell)%PRIME
q2=(2*Cst*A2+2*M*ell*Q*(3-4*lam)-8*u*Q*delta*ell*Tm*Tm)%PRIME
R6=(M*K*K-4*m*m*D**3)%PRIME
for z in [e,kk,u,Q,delta,Vbar,rho,b,c,bc,Phi,M,Ast]:
 assert z*inv(z)%PRIME==1
assert m==0 and T0==0 and K==0 and q2==0 and R6==0
assert rho*rho%PRIME==delta and (p+q)%PRIME==2
assert Ast*Tm%PRIME==u*Q*ell*mu%PRIME
assert D==rat(-87,784)
G=(lam*P02-(1-u)*T0)%PRIME
Pf=T0*(J-Q)%PRIME
Pc=(Q*P02*(ell+Tm)-G*T0)%PRIME
tt=-(P(Pf)*f+Pc)/(bc*Q*Phi%PRIME)
V=(J*f+bc*Q*tt-G)/Q
W1=2*u*f+rat(T0,2)
X=(W1-q*V)/(b*(p-q)%PRIME)
Y=(p*V-W1)/(c*(p-q)%PRIME)
A1=2*f-2*V+2*bc*tt
rs=X-a*p-c*tt;ss=Y-a*q-b*tt
check(tt,rat(-27,49));check(V.coeff(1),2*u)
check(X.coeff(1),2);check(Y.coeff(1),2)
rows=[[P(),P(),P(p),P(q)],
      [P(),A1,rs,ss],
      [P(p),rs,P(),tt],
      [P(q),ss,tt,P()]]
one=[P(1),P(),P(1),P(1)]
def va(v,z):return [v[i]+z[i] for i in range(4)]
def vs(c0,v):return [c0*x for x in v]
def vm(v,z):
 return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def trc(v):return a*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [trc(vm(row,v)) for row in rows]
dv=DK(one);F2=trc(dv);Kd=DK(dv)
def N4(v):
 vv=vm(v,v);tv=trc(v)
 return (2*trc(vm(dv,vv))-F2*trc(vv)-4*tv*trc(vm(dv,v))
         +2*F2*tv*tv+trc(vm(v,DK(v))))
def P2(v):
 vv=va(v,vs(-trc(v),one));return trc(vm(vm(vv,vv),vv))
def mean(j):
 squared=(2*trc(vm(rows[0],rows[1])) if j==1
          else trc(vm(rows[j],rows[j])))
 return squared-2*Kd[j]-2*vm(dv,dv)[j]+2*F2*dv[j]
check(F2,2*f);check(dv[0],u);check(dv[2],X);check(dv[3],Y)
check(mean(0),0);check(P2(rows[0]),P02)
check(N4(rows[0]),2*lam*P02)
v0=va(rows[0],vs(-u,one));v1=va(rows[1],vs(-trc(rows[1]),one))
check(3*trc(vm(vm(v0,v0),v1)),3*w*P02)
h=P(1)+rat(Tm,ell)+rho*sig
k=P(1)+rat(Tm,ell)-rho*sig
vphys=[P(1),P(w),h,k]
E2=b*(h-1)**2+c*(k-1)**2-A2
E3=b*(h-1)**3+c*(k-1)**3-B3
qs=sig*sig-rat(D,M)
check(E2,rat(M,ell)*qs)
check(E3,3*Tm*delta*qs)
check(trc(vphys),lam)
E1,EB,EC=[mean(i) for i in (1,2,3)]
assert E1.deg(0)==2 and E1.deg(1)==0
head=E1.coeff(2);assert head==(-8*delta)%PRIME and head
assert EB.coeff(2)==0 and EC.coeff(2)==0
qf=E1/head
assert qf.coeff(2)==1 and qf.deg(1)==0
N1=N4(va(rows[0],rows[1]))-N4(rows[0])-N4(rows[1])-4*lam*w*P02
NB=N4(rows[2])-2*lam*P02*h*h
NC=N4(rows[3])-2*lam*P02*k*k
PB=P2(rows[2])-P02*h**3
PC=P2(rows[3])-P02*k**3
NV=N4(vphys)
originals=[E2,E1,EB,EC,N1,NB,NC,PB,PC,NV]
labels=['complete_second_spectral_moment','true_dual_E1','complete_EB',
        'complete_EC','complete_N1','complete_NB','complete_NC',
        'complete_PB','complete_PC','complete_NV']
tf=[P() for _ in originals];ts=[P() for _ in originals]
tf[1]=P(inv(head));ts[0]=P(rat(ell,M))
assert qf==sum((tf[i]*originals[i] for i in range(10)),P())
assert qs==sum((ts[i]*originals[i] for i in range(10)),P())
STAT['monicOriginalReturns']+=2
say('new_m_positive_k_minus_two_unique_centre_complete_raw_Gram',
    prime=PRIME,centre={'u':u,'k':kk,'Q':Q,'ell':ell,'m':m,
                       'lambda':lam,'mu':mu,'T':Tm,'D':D,'rho':rho},
    unitFQuadraticHead=head,monicF=profile(qf),monicSigma=profile(qs),
    allRawLabels=labels,allRawProfiles=[profile(x) for x in originals],
    originalF2AndMeanZeroN0P1Returned=True,completeDualSquareVm=True,
    oppositeRhoOnlySwapsBothOriginalSingletonLabels=True,
    noMInverse=True,noSelectedFOrSigmaRoot=True,statistics=STAT)
def reduce(v):
 # Exact ordinary polynomial division; qf and qs are independent monic quadrics.
 original=P(v);r=P(v);af=P();asig=P()
 while True:
  keys=[k for k in r.c if k[0]>=2]
  if not keys:break
  i,j=max(keys);z=P({(i-2,j):r.c[(i,j)]})
  r-=z*qf;af+=z
 while True:
  keys=[k for k in r.c if k[1]>=2]
  if not keys:break
  i,j=max(keys);z=P({(i,j-2):r.c[(i,j)]})
  r-=z*qs;asig+=z
 assert original==af*qf+asig*qs+r
 assert all(i<2 and j<2 for i,j in r.c)
 STAT['quotientDivisionReturns']+=1
 return r,af,asig
basis=[P(1),f,sig,f*sig]
positions=[(0,0),(1,0),(0,1),(1,1)]
def flat(v):
 v=P(v);assert all(k in positions for k in v.c)
 return [v.c.get(k,0) for k in positions]
columns=[];coltags=[]
for oi,F in enumerate(originals):
 for bmon in basis:
  rem,af,asig=reduce(bmon*F)
  tags=[-af*tf[i]-asig*ts[i] for i in range(10)]
  tags[oi]+=bmon
  assert rem==sum((tags[i]*originals[i] for i in range(10)),P())
  columns.append(flat(rem));coltags.append(tags)
  STAT['originalColumnReturns']+=1
assert len(columns)==40
piv={}
for ci,column in enumerate(columns):
 v=column[:];rep={ci:1}
 for pivot in sorted(piv):
  pv,pr=piv[pivot];c0=v[pivot]
  if not c0:continue
  v=[(x-c0*y)%PRIME for x,y in zip(v,pv)]
  for j,z in pr.items():
   rep[j]=(rep.get(j,0)-c0*z)%PRIME
   if not rep[j]:del rep[j]
 nz=next((i for i,x in enumerate(v) if x),None)
 if nz is None:continue
 z=inv(v[nz]);v=[x*z%PRIME for x in v]
 rep={j:x*z%PRIME for j,x in rep.items()}
 assert [sum(c0*columns[j][i] for j,c0 in rep.items())%PRIME
         for i in range(4)]==v
 STAT['GaussianVectorReturns']+=1;piv[nz]=(v,rep)
target=[1,0,0,0];v=target[:];sol={}
for pivot in sorted(piv):
 pv,pr=piv[pivot];c0=v[pivot]
 if not c0:continue
 v=[(x-c0*y)%PRIME for x,y in zip(v,pv)]
 for j,z in pr.items():
  sol[j]=(sol.get(j,0)+c0*z)%PRIME
  if not sol[j]:del sol[j]
success=not any(v)
if success:
 assert [sum(c0*columns[j][i] for j,c0 in sol.items())%PRIME
         for i in range(4)]==target
 Omega=[P() for _ in originals]
 for j,z in sol.items():
  for i in range(10):Omega[i]+=z*coltags[j][i]
 assert sum((Omega[i]*originals[i] for i in range(10)),P())==1
 STAT['finalOriginalReturns']+=1
 say('new_m_positive_k_minus_two_original_unit_returned',
     dimension=4,rank=len(piv),target='1',
     originalMultipliers=[profile(x) for x in Omega],
     fullUnquotientedFpFAndSigmaPolynomialReturned=True,
     allFAndSigmaMultiplicitiesKept=True,
     excludesThisValuationResidueCentreOnly=True,
     QEqualsTwoOtherMChartNotClaimed=True,statistics=STAT)
else:
 say('new_m_positive_k_minus_two_complete_original_residue_retained',
     dimension=4,rank=len(piv),target='1',remainingCoordinates=v,
     allFAndSigmaRootsAndMultiplicitiesRetained=True,
     noPositiveTargetOrQQEmptinessInference=True,statistics=STAT)
say('new_m_positive_k_minus_two_original_input_complete',
    originalColumns=len(columns),unitReturned=success,dimension=4,
    scope='ONLY v(m)>0 with kbar=-2 in current W/b0 and p=1009',
    noOldGateReplayed=True,statistics=STAT)
