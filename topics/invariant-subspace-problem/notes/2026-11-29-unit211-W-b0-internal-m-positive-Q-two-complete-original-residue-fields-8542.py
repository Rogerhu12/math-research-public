#!/usr/bin/env python3
"""NEW W/b0 internal m-positive Q=2 residue chart, p=1009.
Whole Astar-deep U=-2 and mu poles are excluded by the accompanying
original valuation proof. Keep all finite mu, P02=0, lambda=0 and D=0.
New fixed 5x5 q2/K determinant with all five adjugate coordinates;
all Fp U factors, actual same-mu gcd, monic true E1 f2 and complete
second-moment sigma2. Complete twelve raw sources times every finite
basis vector, only target 1, final ordinary K[mu,f,sigma] return.
K is EACH full irreducible residue field, not a selected root or
unidentified QQ lift. U projection multiplicities are recorded; this
is residue-point exclusion, not a scheme-length assertion.
120 seconds /1GiB, zero source dependencies. No old projection or
initial gate, no m/D/lambda/P02 inverse, no coefficient payload/cache.
"""
import hashlib,itertools,json,resource,signal,time
from flint import nmod_poly
START=time.perf_counter();DEADLINE=START+120;PRIME=1009
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
STAT={'baseInverseReturns':0,'FpPolynomialDivisionReturns':0,
      'FpBezoutReturns':0,'projectionCoordinates':0,
      'factorProductReturns':0,'fieldInverseReturns':0,
      'muDivisionReturns':0,'muBezoutReturns':0,
      'rawDefinitionReturns':0,'monicOriginalReturns':0,
      'quotientDivisionReturns':0,'originalColumnReturns':0,
      'GaussianVectorReturns':0,'finalOriginalReturns':0}
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute120')
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True,separators=(',',':')),flush=True)
def inv0(a):
 a=int(a)%PRIME;assert a
 z=pow(a,PRIME-2,PRIME);assert a*z%PRIME==1
 STAT['baseInverseReturns']+=1;return z
def tr0(a):
 a=[int(x)%PRIME for x in a]
 while a and not a[-1]:a.pop()
 return a
def add0(a,b):
 z=[0]*max(len(a),len(b))
 for i,x in enumerate(a):z[i]=(z[i]+x)%PRIME
 for i,x in enumerate(b):z[i]=(z[i]+x)%PRIME
 return tr0(z)
def sc0(a,b):return tr0([int(b)*x for x in a])
def sub0(a,b):return add0(a,sc0(b,-1))
def mul0(a,b):
 if not a or not b:return []
 tick();z=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%PRIME
 return tr0(z)
def div0(a,b):
 a=tr0(a);b=tr0(b);assert b;orig=a[:]
 q=[0]*max(0,len(a)-len(b)+1);iv=inv0(b[-1])
 while a and len(a)>=len(b):
  j=len(a)-len(b);c=a[-1]*iv%PRIME;q[j]=c
  a=sub0(a,[0]*j+sc0(b,c))
 q=tr0(q);assert add0(mul0(q,b),a)==orig
 STAT['FpPolynomialDivisionReturns']+=1;return q,a
def xg0(a,b):
 aa,bb=tr0(a),tr0(b);r0,r1=aa[:],bb[:]
 s0,s1=[1],[];t0,t1=[],[1]
 while r1:
  q,r=div0(r0,r1);r0,r1=r1,r
  s0,s1=s1,sub0(s0,mul0(q,s1));t0,t1=t1,sub0(t0,mul0(q,t1))
  assert add0(mul0(s0,aa),mul0(t0,bb))==r0
  STAT['FpBezoutReturns']+=1
 if not r0:return [],[],[]
 iv=inv0(r0[-1]);g,s,t=sc0(r0,iv),sc0(s0,iv),sc0(t0,iv)
 assert add0(mul0(s,aa),mul0(t,bb))==g
 STAT['FpBezoutReturns']+=1;return g,s,t
def pow0(a,n):
 z=[1]
 while n:
  if n&1:z=mul0(z,a)
  n//=2
  if n:a=mul0(a,a)
 return z
class UPoly:
 def __init__(self,v=0):
  self.c=v.c[:] if isinstance(v,UPoly) else tr0(v if isinstance(v,(list,tuple)) else [v])
 def __bool__(self):return bool(self.c)
 def __neg__(self):return UPoly(sc0(self.c,-1))
 def __add__(self,v):return UPoly(add0(self.c,UPoly(v).c))
 __radd__=__add__
 def __sub__(self,v):return self+-UPoly(v)
 def __rsub__(self,v):return UPoly(v)+-self
 def __mul__(self,v):return UPoly(mul0(self.c,UPoly(v).c))
 __rmul__=__mul__
 def __pow__(self,n):return UPoly(pow0(self.c,n))
 def __eq__(self,v):return self.c==UPoly(v).c
def up(a):
 a=UPoly(a);raw=json.dumps(a.c,separators=(',',':')).encode()
 return {'degree':len(a.c)-1,'terms':sum(bool(x) for x in a.c),
         'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
U=UPoly([0,1]);hh=U+2
G3=8-4*U-2*U**2-U**3
H3=U**3+3*U**2+4*U-4
qco=[(4-5*U)*hh**2,4*(1-U)*hh**2,G3]
kco=[7*hh**3,3*(4*U+3)*hh**2,6*U*hh**2,H3]
assert G3+H3==U**2+4
assert (U+3)*G3+(U+2)*H3==16
# Fixed rows q,mu*q,mu^2*q,K,mu*K; capacity remains 2+3 at every U.
rows=[]
for co,shifts in [(qco,range(3)),(kco,range(2))]:
 for j in shifts:rows.append([UPoly()]*j+co+[UPoly()]*(5-j-len(co)))
assert len(rows)==5 and all(len(r)==5 for r in rows)
def det(C):
 if not C:return UPoly(1)
 if len(C)==1:return C[0][0]
 z=UPoly()
 for j,v in enumerate(C[0]):
  if v:z+=((-1)**j)*v*det([[row[k] for k in range(len(C)) if k!=j]
                          for row in C[1:]])
 return z
projection=det(rows)
adj=[((-1)**i)*det([[rows[r][c] for c in range(1,5)]
                    for r in range(5) if r!=i]) for i in range(5)]
for j in range(5):
 assert sum((adj[i]*rows[i][j] for i in range(5)),UPoly())==(projection if j==0 else UPoly())
 STAT['projectionCoordinates']+=1
say('new_Q_two_complete_fixed_five_original_projection_returned',
    prime=PRIME,fixedCapacity=[2,3],projection=up(projection),
    fiveOriginalCoordinatesReturned=True,
    allMuHeadZeroFibersRetained=True,noR6NilpotenceLift=True,statistics=STAT)
if not projection:
 say('new_Q_two_projection_zero_all_original_fibers_retained',
     noFiniteUClaim=True,statistics=STAT)
 raise SystemExit(0)
if len(projection.c)==1:
 assert projection.c[0]*inv0(projection.c[0])%PRIME==1
 say('new_Q_two_original_q_and_K_unit_projection_returned',
     entireNamedResidueChartExcluded=True,statistics=STAT)
 raise SystemExit(0)
np=nmod_poly(projection.c,PRIME)
unit,nf=np.factor()
factors=[]
back=UPoly(int(unit))
for phi,exponent in nf:
 pc=[int(phi[i]) for i in range(int(phi.degree())+1)]
 exponent=int(exponent);back*=UPoly(pc)**exponent
 factors.append((pc,exponent))
assert back==projection
STAT['factorProductReturns']+=1
factors.sort(key=lambda x:(len(x[0]),tuple(x[0])))
say('new_Q_two_complete_Fp_projection_factorization',
    factors=[{'factor':up(c),'multiplicity':e} for c,e in factors],
    allFactorProductReturned=True,
    purpose='All residue embeddings, not a QQ factor interpretation',
    UProjectionMultiplicitiesRecordedNoSchemeLengthClaim=True,statistics=STAT)
class K:
 mod=None
 def __init__(self,v=0):
  if isinstance(v,K):self.c=v.c[:];return
  a=tr0(v if isinstance(v,(list,tuple)) else [v])
  if self.mod is not None and len(a)>=len(self.mod):a=div0(a,self.mod)[1]
  self.c=a
 def __bool__(self):return bool(self.c)
 def __neg__(self):return K(sc0(self.c,-1))
 def __add__(self,v):
  if not isinstance(v,(K,int,list,tuple)):return NotImplemented
  return K(add0(self.c,K(v).c))
 __radd__=__add__
 def __sub__(self,v):
  if not isinstance(v,(K,int,list,tuple)):return NotImplemented
  return self+-K(v)
 def __rsub__(self,v):return K(v)+-self
 def __mul__(self,v):
  if not isinstance(v,(K,int,list,tuple)):return NotImplemented
  return K(mul0(self.c,K(v).c))
 __rmul__=__mul__
 def inv(self):
  assert self
  if len(self.c)==1:z=K(inv0(self.c[0]))
  else:
   gg,s,_=xg0(self.c,self.mod);assert len(gg)==1
   z=K(sc0(s,inv0(gg[0])))
  assert self*z==1;STAT['fieldInverseReturns']+=1;return z
 def __truediv__(self,v):
  if not isinstance(v,(K,int,list,tuple)):return NotImplemented
  return self*K(v).inv()
 def __rtruediv__(self,v):return K(v)*self.inv()
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  z=K(1);a=self
  while n:
   if n&1:z=z*a
   n//=2
   if n:a=a*a
  return z
 def __eq__(self,v):
  if not isinstance(v,(K,int,list,tuple)):return False
  return self.c==K(v).c
 def coeff(self,j):return self.c[j] if j<len(self.c) else 0
def trim(a):
 a=[K(x) for x in a]
 while a and not a[-1]:a.pop()
 return a
def pa(a,b):
 z=[K() for _ in range(max(len(a),len(b)))]
 for i,x in enumerate(a):z[i]+=x
 for i,x in enumerate(b):z[i]+=x
 return trim(z)
def ps(a,c):return trim([x*c for x in a])
def pn(a,b):return pa(a,ps(b,-1))
def pm(a,b):
 if not a or not b:return []
 z=[K() for _ in range(len(a)+len(b)-1)]
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 return trim(z)
def pd(a,b):
 a=trim(a);b=trim(b);assert b;orig=a[:]
 out=[K() for _ in range(max(0,len(a)-len(b)+1))]
 iv=b[-1].inv()
 while a and len(a)>=len(b):
  j=len(a)-len(b);c=a[-1]*iv;out[j]+=c
  a=pn(a,[K()]*j+ps(b,c))
 out=trim(out);assert pa(pm(out,b),a)==orig
 STAT['muDivisionReturns']+=1;return out,a
def px(a,b):
 aa,bb=trim(a),trim(b);r0,r1=aa[:],bb[:]
 s0,s1=[K(1)],[];t0,t1=[],[K(1)]
 while r1:
  q,r=pd(r0,r1);r0,r1=r1,r
  s0,s1=s1,pn(s0,pm(q,s1));t0,t1=t1,pn(t0,pm(q,t1))
  assert pa(pm(s0,aa),pm(t0,bb))==r0
  STAT['muBezoutReturns']+=1
 assert r0
 iv=r0[-1].inv();g,s,t=ps(r0,iv),ps(s0,iv),ps(t0,iv)
 assert pa(pm(s,aa),pm(t,bb))==g
 STAT['muBezoutReturns']+=1;return g,s,t
def kp(a):
 data=[K(x).c for x in trim(a)]
 raw=json.dumps(data,separators=(',',':')).encode()
 return {'muDegree':len(data)-1,'UFieldDegree':len(K.mod)-1,
         'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
class P:
 # Ordinary K[mu,f,sigma]; only the constant field U relation is reduced.
 def __init__(self,v=0):
  if isinstance(v,P):self.c=v.c.copy();return
  if isinstance(v,dict):
   self.c={tuple(map(int,k)):K(c) for k,c in v.items() if K(c)}
  else:
   z=K(v);self.c={} if not z else {(0,0,0):z}
  assert all(len(k)==3 and min(k)>=0 for k in self.c)
 def __bool__(self):return bool(self.c)
 def __neg__(self):return P({k:-c for k,c in self.c.items()})
 def __add__(self,v):
  v=P(v);z=self.c.copy()
  for k,c in v.c.items():z[k]=z.get(k,K())+c
  return P(z)
 __radd__=__add__
 def __sub__(self,v):return self+-P(v)
 def __rsub__(self,v):return P(v)+-self
 def __mul__(self,v):
  v=P(v);tick();z={}
  for a,c in self.c.items():
   for b,d in v.c.items():
    k=tuple(a[i]+b[i] for i in range(3));z[k]=z.get(k,K())+c*d
  return P(z)
 __rmul__=__mul__
 def __truediv__(self,v):
  v=P(v);assert len(v.c)==1 and (0,0,0) in v.c
  return self*v.c[(0,0,0)].inv()
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  z=P(1);a=self
  while n:
   if n&1:z=z*a
   n//=2
   if n:a=a*a
  return z
 def __eq__(self,v):return self.c==P(v).c
 def coeff(self,i,j=0,k=0):return self.c.get((i,j,k),K())
 def deg(self,axis):return max((x[axis] for x in self.c),default=-1)
def embed(a):return P({(i,0,0):K(c) for i,c in enumerate(a) if K(c)})
def pp(v):
 v=P(v);data=[[list(k),c.c] for k,c in sorted(v.c.items())]
 raw=json.dumps(data,separators=(',',':')).encode()
 return {'muDegree':v.deg(0),'fDegree':v.deg(1),'sigmaDegree':v.deg(2),
         'terms':len(data),'UFieldDegree':len(K.mod)-1,'bytes':len(raw),
         'sha256':hashlib.sha256(raw).hexdigest()}
def check(a,b):
 assert P(a)==P(b);STAT['rawDefinitionReturns']+=1
closed=[];retained=[];paid=[]
for fi,(phi,exponent) in enumerate(factors):
 tick();K.mod=sc0(phi,inv0(phi[-1]));du=len(K.mod)-1
 u=K([0,1]);eu=u-1;hh=u+2
 supports=[('u_already_valuation_unit',u),
           ('e_already_valuation_unit',eu),
           ('Astar_deep_U_minus_two_paper_exclusion',hh),
           ('Vbar_already_valuation_unit',2*u-1)]
 absent=[name for name,z in supports if not z]
 if absent:
  paid.append(fi)
  say('new_Q_two_whole_residue_field_removed_by_declared_old_scope',
      factor=fi,profile=up(phi),projectionMultiplicity=exponent,
      supports=absent,allEmbeddingsOfThisFactor=True)
  continue
 for _,z in supports:assert z*z.inv()==1
 qa=[K(c.c) for c in qco];ka=[K(c.c) for c in kco]
 assert qa[1]
 g,gb,kg=px(qa,ka)
 assert len(g)<=3 and g[-1]==1
 # All actual lower mu degrees are retained after specialization.
 say('new_Q_two_whole_residue_field_same_mu_Bezout',
     factor=fi,UFieldDegree=du,projectionMultiplicity=exponent,
     actualQDegree=len(trim(qa))-1,actualKDegree=len(trim(ka))-1,
     completeMuGcd=kp(g),qMultiplier=kp(gb),kMultiplier=kp(kg),
     noSelectedMuRoot=True,statistics=STAT)
 mu=P({(1,0,0):1});f=P({(0,1,0):1});sig=P({(0,0,1):1})
 ell=u;delta=K(-1);Qw=K(2);m=K();rho=K(469)
 assert rho*rho==delta
 b=c=u/2;bc=b*c;aw=1-u;p=1+rho;q=1-rho
 lam=(mu+3)/2;Tm=u*mu/hh;w=lam-1-Tm
 A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1
 D=u*A2-Tm*Tm;Kv=u*u*B3-3*u*A2*Tm+2*Tm**3
 M=-u*u;J=2*u*(2-u);Ast=2*u*hh
 Cst=-J*u*u
 q2=2*Cst*A2+2*M*u*Qw*(3-4*lam)-8*u*Qw*delta*u*Tm*Tm
 qhat=embed(qa);khat=embed(ka)
 check(q2,(-2*u**3/(hh*hh))*qhat)
 check(Kv,(u*u/(2*hh**3))*khat)
 T0=-2*u*u;Phi=-2*eu*eu;P02=2*u*eu*(u+1)
 G=lam*P02-(1-u)*T0;Pf=T0*(J-Qw)
 Pc=Qw*P02*(u+Tm)-G*T0
 for z in [u,eu,hh,Qw,delta,M,rho,b,c,bc,Phi,Ast]:
  assert z*z.inv()==1
 tt=-(Pf*f+Pc)/(bc*Qw*Phi)
 V=(J*f+bc*Qw*tt-G)/Qw;W1=2*u*f+T0/2
 X=(W1-q*V)/(b*(p-q));Y=(p*V-W1)/(c*(p-q))
 A1=2*f-2*V+2*bc*tt
 rs=X-aw*p-c*tt;ss=Y-aw*q-b*tt
 check(tt.coeff(0,1,0),4);check(V.coeff(0,1,0),2*u)
 check(X.coeff(0,1,0),2);check(Y.coeff(0,1,0),2)
 rawrows=[[P(),P(),P(p),P(q)],[P(),A1,rs,ss],
          [P(p),rs,P(),tt],[P(q),ss,tt,P()]]
 one=[P(1),P(),P(1),P(1)]
 def va(x,y):return [x[i]+y[i] for i in range(4)]
 def vs(c0,v):return [c0*x for x in v]
 def vm(x,y):return [x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[2]*y[2],x[3]*y[3]]
 def trc(x):return aw*x[0]+x[1]+b*x[2]+c*x[3]
 def DK(v):return [trc(vm(row,v)) for row in rawrows]
 dv=DK(one);F2=trc(dv);Kd=DK(dv)
 def N4(v):
  vv=vm(v,v);tv=trc(v)
  return (2*trc(vm(dv,vv))-F2*trc(vv)-4*tv*trc(vm(dv,v))
          +2*F2*tv*tv+trc(vm(v,DK(v))))
 def P2(v):
  x=va(v,vs(-trc(v),one));return trc(vm(vm(x,x),x))
 def mean(j):
  sq=2*trc(vm(rawrows[0],rawrows[1])) if j==1 else trc(vm(rawrows[j],rawrows[j]))
  return sq-2*Kd[j]-2*vm(dv,dv)[j]+2*F2*dv[j]
 check(F2,2*f);check(mean(0),0);check(P2(rawrows[0]),P02)
 check(N4(rawrows[0]),2*lam*P02)
 v0=va(rawrows[0],vs(-u,one));v1=va(rawrows[1],vs(-trc(rawrows[1]),one))
 check(3*trc(vm(vm(v0,v0),v1)),3*w*P02)
 hv=1+Tm/u+rho*sig;kv=1+Tm/u-rho*sig
 vphys=[P(1),w,hv,kv]
 E2=b*(hv-1)**2+c*(kv-1)**2-A2
 E3=b*(hv-1)**3+c*(kv-1)**3-B3
 check(trc(vphys),lam)
 check(Kv,3*u*Tm*E2-u*u*E3)
 E1,EB,EC=[mean(i) for i in (1,2,3)]
 head=8*eu*eu
 assert E1.deg(1)==2 and E1.deg(2)<=0
 assert E1.coeff(0,2,0)==head
 assert all(not (ex[1]==2 and (ex[0] or ex[2])) for ex in E1.c)
 N1=N4(va(rawrows[0],rawrows[1]))-N4(rawrows[0])-N4(rawrows[1])-4*lam*w*P02
 NB=N4(rawrows[2])-2*lam*P02*hv*hv
 NC=N4(rawrows[3])-2*lam*P02*kv*kv
 PB=P2(rawrows[2])-P02*hv**3
 PC=P2(rawrows[3])-P02*kv**3
 NV=N4(vphys)
 originals=[q2,E2,E3,E1,EB,EC,N1,NB,NC,PB,PC,NV]
 labels=['original_q2','complete_E2','complete_E3','true_dual_E1',
         'complete_EB','complete_EC','complete_N1','complete_NB',
         'complete_NC','complete_PB','complete_PC','complete_NV']
 gg=embed(g);bq=embed(gb);bk=embed(kg)
 tg=[P() for _ in originals]
 tg[0]=bq*(-hh*hh/(2*u**3))
 tg[1]=bk*(2*hh**3/(u*u))*(3*u*Tm)
 tg[2]=bk*(2*hh**3/(u*u))*(-u*u)
 assert gg==sum((tg[i]*originals[i] for i in range(12)),P())
 STAT['monicOriginalReturns']+=1
 if len(g)==1:
  assert gg==1
  STAT['finalOriginalReturns']+=1;closed.append(fi)
  say('new_Q_two_entire_residue_field_original_moment_unit_returned',
      factor=fi,UFieldDegree=du,projectionMultiplicity=exponent,
      finalTwelveOriginalMultipliers=[pp(x) for x in tg],
      completeOrdinaryKMuFSigmaReturn=True,statistics=STAT)
  continue
 dm=len(g)-1
 qf=E1/head;qs=sig*sig-D/M
 tf=[P() for _ in originals];ts=[P() for _ in originals]
 tf[3]=P(head.inv());ts[1]=P(u/M)
 assert qf==sum((tf[i]*originals[i] for i in range(12)),P())
 assert qs==sum((ts[i]*originals[i] for i in range(12)),P())
 assert qf.coeff(0,2,0)==1 and qs.coeff(0,0,2)==1
 STAT['monicOriginalReturns']+=2
 def reduce(v):
  original=P(v);r=P(v);af=P();asig=P();ag=P()
  while True:
   ks=[ex for ex in r.c if ex[1]>=2]
   if not ks:break
   i,j,k=max(ks);z=P({(i,j-2,k):r.c[(i,j,k)]})
   r-=z*qf;af+=z
  while True:
   ks=[ex for ex in r.c if ex[2]>=2]
   if not ks:break
   i,j,k=max(ks);z=P({(i,j,k-2):r.c[(i,j,k)]})
   r-=z*qs;asig+=z
  while True:
   ks=[ex for ex in r.c if ex[0]>=dm]
   if not ks:break
   i,j,k=max(ks);z=P({(i-dm,j,k):r.c[(i,j,k)]})
   r-=z*gg;ag+=z
  assert original==r+af*qf+asig*qs+ag*gg
  assert all(i<dm and j<2 and k<2 for i,j,k in r.c)
  STAT['quotientDivisionReturns']+=1;return r,af,asig,ag
 positions=[(mi,ff,ss) for ff in range(2) for ss in range(2) for mi in range(dm)]
 basis=[P({ex:u**ui}) for ex in positions for ui in range(du)]
 NN=4*dm*du;assert len(basis)==NN and NN<=120
 def flat(v):
  v=P(v);assert all(ex in positions for ex in v.c)
  return [v.c.get(ex,K()).coeff(ui) for ex in positions for ui in range(du)]
 columns=[];coltags=[]
 for oi,F in enumerate(originals):
  for mon in basis:
   rem,af,asig,ag=reduce(mon*F)
   tags=[-af*tf[i]-asig*ts[i]-ag*tg[i] for i in range(12)]
   tags[oi]+=mon
   assert rem==sum((tags[i]*originals[i] for i in range(12)),P())
   columns.append(flat(rem));coltags.append(tags)
   STAT['originalColumnReturns']+=1
 say('new_Q_two_complete_same_point_finite_original_model',
     factor=fi,UFieldDegree=du,projectionMultiplicity=exponent,
     muDegree=dm,dimension=NN,actualColumns=len(columns),
     monicF=pp(qf),monicSigma=pp(qs),muGcd=kp(g),
     allRawLabels=labels,allRawProfiles=[pp(x) for x in originals],
     retainsAllMuFAndSigmaMultiplicities=True,
     noSmallMOrDOrLambdaOrP02Inverse=True,
     P02ZeroAndDZeroAndLambdaZeroRetained=True,statistics=STAT)
 piv={}
 for ci,col in enumerate(columns):
  v=col[:];rep={ci:1}
  for pivot in sorted(piv):
   pv,pr=piv[pivot];c0=v[pivot]
   if not c0:continue
   v=[(x-c0*y)%PRIME for x,y in zip(v,pv)]
   for j,z in pr.items():
    rep[j]=(rep.get(j,0)-c0*z)%PRIME
    if not rep[j]:del rep[j]
  nz=next((i for i,x in enumerate(v) if x),None)
  if nz is None:continue
  iv=inv0(v[nz]);v=[x*iv%PRIME for x in v];rep={j:x*iv%PRIME for j,x in rep.items()}
  assert [sum(c0*columns[j][r] for j,c0 in rep.items())%PRIME for r in range(NN)]==v
  STAT['GaussianVectorReturns']+=1;piv[nz]=(v,rep)
 target=[1]+[0]*(NN-1);v=target[:];sol={}
 for pivot in sorted(piv):
  pv,pr=piv[pivot];c0=v[pivot]
  if not c0:continue
  v=[(x-c0*y)%PRIME for x,y in zip(v,pv)]
  for j,z in pr.items():
   sol[j]=(sol.get(j,0)+c0*z)%PRIME
   if not sol[j]:del sol[j]
 if not any(v):
  assert [sum(c0*columns[j][r] for j,c0 in sol.items())%PRIME for r in range(NN)]==target
  Omega=[P() for _ in originals]
  for j,z in sol.items():
   for i in range(12):Omega[i]+=z*coltags[j][i]
  assert sum((Omega[i]*originals[i] for i in range(12)),P())==1
  STAT['finalOriginalReturns']+=1;closed.append(fi)
  say('new_Q_two_whole_residue_field_twelve_original_unit_returned',
      factor=fi,UFieldDegree=du,projectionMultiplicity=exponent,
      dimension=NN,rank=len(piv),target='1',
      originalMultipliers=[pp(x) for x in Omega],
      entireOrdinaryKMuFSigmaPolynomialReturned=True,
      allResidueEmbeddingsCovered=True,statistics=STAT)
 else:
  retained.append(fi)
  say('new_Q_two_whole_residue_field_retained',
      factor=fi,UFieldDegree=du,projectionMultiplicity=exponent,
      dimension=NN,rank=len(piv),muGcd=kp(g),
      allUnreturnedFibersKept=True,noPositiveTargetOrQQLift=True,statistics=STAT)
say('new_m_positive_Q_two_original_input_complete',
    factorCount=len(factors),paidAbsentFields=paid,closedFields=closed,
    retainedFields=retained,
    excludesEntireNamedResidueChart=(len(paid)+len(closed)==len(factors) and not retained),
    purpose='Original 1009 valuation boundary, not QQ generic emptiness or scheme length',
    noOldGateReplayed=True,statistics=STAT)
