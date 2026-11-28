#!/usr/bin/env python3
"""NEW B2 AND ell=3/2, corrected Phi original finite values.
The two complete moments give an exact fixed degree-four QQ algebra.
A new full scaled Gram returns (u-3)*NV=2G(u), deg G<=2.
Only then use all QQ constant factors, all good u primary multiplicities,
the original monic t2 and E1/EB/EC/N1/complete NB/NC/PB/PC.
Fixed targets 1, [lambda*D*t*(f-u)]^1,...,^dimension, full raw returns.
No old six-column/cofactor/gcd, first-head gate, selected complex root,
new physical head inverse, modular lifting or execution dependency.
120 seconds /1GiB, outer135; no retry, resumed stage or enlarged budget.
"""
import hashlib,json,resource,signal,time
from flint import fmpq as QQ, fmpq_poly, fmpq_mpoly_ctx
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
STAT={'polynomialDivisionReturns':0,'fieldInverseReturns':0,
      'finiteAlgebraInverseReturns':0,'scaledGramNVReturns':0,
      'monicTOriginalReturns':0,'rawColumnReturns':0,
      'rationalVectorReturns':0,'finalEightOriginalReturns':0}
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute120')
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True,separators=(',',':')),flush=True)
def tr(a):
 a=list(a)
 while a and not a[-1]:a.pop()
 return a
def pa(a,b):
 z=[0]*max(len(a),len(b))
 for i,x in enumerate(a):z[i]=z[i]+x
 for i,x in enumerate(b):z[i]=z[i]+x
 return tr(z)
def ps(a,c):return tr([x*c for x in a])
def pn(a,b):return pa(a,ps(b,-1))
def pm(a,b):
 if not a or not b:return []
 z=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]=z[i+j]+x*y
 return tr(z)
def pd(a,b):
 a=tr(a);b=tr(b);assert b
 original=a[:];out=[0]*max(0,len(a)-len(b)+1)
 ib=1/b[-1];assert ib*b[-1]==1
 while a and len(a)>=len(b):
  tick();j=len(a)-len(b);c=a[-1]*ib;out[j]=out[j]+c
  a=pn(a,[0]*j+ps(b,c))
 out=tr(out)
 assert pa(pm(out,b),a)==original and (not a or len(a)<len(b))
 STAT['polynomialDivisionReturns']+=1
 return out,a
def px(a,b):
 a=tr(a);b=tr(b);r0,r1=a[:],b[:]
 one=(a[0] if a else b[0])*0+1
 s0,s1=[one],[];t0,t1=[],[one]
 while r1:
  q,r2=pd(r0,r1)
  r0,r1=r1,r2;s0,s1=s1,pn(s0,pm(q,s1));t0,t1=t1,pn(t0,pm(q,t1))
  assert pa(pm(s0,a),pm(t0,b))==r0
 assert r0
 c=1/r0[-1];g,s,t=ps(r0,c),ps(s0,c),ps(t0,c)
 assert pa(pm(s,a),pm(t,b))==g
 return g,s,t
def pe(a,n):
 z=[a[0]*0+1] if a else [QQ(1)]
 while n:
  if n&1:z=pm(z,a)
  a=pm(a,a);n//=2
 return z
def qprofile(a):
 a=tr(a);raw=json.dumps([str(x) for x in a],separators=(',',':')).encode()
 return {'degree':len(a)-1,'coefficients':len(a),'bytes':len(raw),
         'sha256':hashlib.sha256(raw).hexdigest()}
class K:
 mod=None
 def __init__(self,v=0):
  if isinstance(v,K):self.c=v.c[:];return
  a=[QQ(x) for x in v] if isinstance(v,(list,tuple)) else [QQ(v)]
  a=tr(a)
  if self.mod is not None and len(a)>=len(self.mod):a=pd(a,self.mod)[1]
  self.c=a
 def __bool__(self):return bool(self.c)
 def __neg__(self):return K(ps(self.c,-1))
 def __add__(self,v):return K(pa(self.c,K(v).c))
 __radd__=__add__
 def __sub__(self,v):return self+-K(v)
 def __rsub__(self,v):return K(v)+-self
 def __mul__(self,v):return K(pm(self.c,K(v).c))
 __rmul__=__mul__
 def inv(self):
  assert self
  if len(self.c)==1:z=K(1/self.c[0])
  else:
   g,s,_=px(self.c,self.mod);assert len(g)==1
   z=K(ps(s,1/g[0]))
  assert self*z==1
  STAT['fieldInverseReturns']+=1
  return z
 def __truediv__(self,v):return self*K(v).inv()
 def __rtruediv__(self,v):return K(v)*self.inv()
 def __pow__(self,n):
  assert isinstance(n,int)
  if n<0:return self.inv()**(-n)
  return K(pe(self.c,n))
 def __eq__(self,v):return self.c==K(v).c
 def coeff(self,j):return self.c[j] if j<len(self.c) else QQ(0)
class A:
 # mod=None means the ORDINARY ring K[u], used for the scaled raw NV.
 # Later mod is the complete monic good u polynomial, with all multiplicities.
 mod=None
 def __init__(self,v=0):
  if isinstance(v,A):self.c=v.c[:];return
  a=[K(x) for x in v] if isinstance(v,(list,tuple)) else [K(v)]
  a=tr(a)
  if self.mod is not None and len(a)>=len(self.mod):a=pd(a,self.mod)[1]
  self.c=a
 def __bool__(self):return bool(self.c)
 def __neg__(self):return A(ps(self.c,-1))
 def __add__(self,v):return A(pa(self.c,A(v).c))
 __radd__=__add__
 def __sub__(self,v):return self+-A(v)
 def __rsub__(self,v):return A(v)+-self
 def __mul__(self,v):return A(pm(self.c,A(v).c))
 __rmul__=__mul__
 def inv(self):
  assert self
  if len(self.c)==1:z=A(self.c[0].inv())
  else:
   assert self.mod is not None,'no rational-function inverse of u'
   g,s,_=px(self.c,self.mod);assert len(g)==1,'unpaid finite-algebra denominator'
   z=A(ps(s,1/g[0]))
  assert self*z==1
  STAT['finiteAlgebraInverseReturns']+=1
  return z
 def __truediv__(self,v):return self*A(v).inv()
 def __rtruediv__(self,v):return A(v)*self.inv()
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  return A(pe(self.c,n))
 def __eq__(self,v):return self.c==A(v).c
 def exact(self,v):
  assert self.mod is None
  q,r=pd(self.c,A(v).c);assert not r
  z=A(q);assert z*A(v)==self
  return z
 def coeff(self,j):return self.c[j] if j<len(self.c) else K()
class T:
 def __init__(self,v=0):
  if isinstance(v,T):self.c=v.c[:];return
  self.c=tr([A(x) for x in v] if isinstance(v,(list,tuple)) else [A(v)])
 def __bool__(self):return bool(self.c)
 def __neg__(self):return T(ps(self.c,-1))
 def __add__(self,v):return T(pa(self.c,T(v).c))
 __radd__=__add__
 def __sub__(self,v):return self+-T(v)
 def __rsub__(self,v):return T(v)+-self
 def __mul__(self,v):return T(pm(self.c,T(v).c))
 __rmul__=__mul__
 def __truediv__(self,v):
  v=T(v);assert len(v.c)==1
  return T(ps(self.c,v.c[0].inv()))
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  return T(pe(self.c,n))
 def __eq__(self,v):return self.c==T(v).c
 def coeff(self,j):return self.c[j] if j<len(self.c) else A()
 def exact(self,v):return T([a.exact(v) for a in self.c])
def kp(a):
 a=tr(a)
 rows=[[str(z) for z in x.c] for x in a]
 raw=json.dumps(rows,separators=(',',':')).encode()
 return {'uDegree':len(a)-1,'Kdegree':len(K.mod)-1,'bytes':len(raw),
         'sha256':hashlib.sha256(raw).hexdigest()}
def tp(v):
 v=T(v);rows=[[[str(z) for z in x.c] for x in a.c] for a in v.c]
 raw=json.dumps(rows,separators=(',',':')).encode()
 return {'tDegree':len(v.c)-1,'uDegree':max((len(a.c)-1 for a in v.c),default=-1),
         'Kdegree':len(K.mod)-1,'bytes':len(raw),
         'sha256':hashlib.sha256(raw).hexdigest()}
def gram(rows):
 aw,b,c=T(QQ(-1,2)),T(1),T(QQ(1,2))
 one=[T(1),T(),T(1),T(1)]
 def va(v,w):return [v[i]+w[i] for i in range(4)]
 def vs(a,v):return [a*x for x in v]
 def vm(v,w):return [v[0]*w[0],v[0]*w[1]+v[1]*w[0],v[2]*w[2],v[3]*w[3]]
 def trc(v):return aw*v[0]+v[1]+b*v[2]+c*v[3]
 def DK(v):return [trc(vm(row,v)) for row in rows]
 d=DK(one);F2=trc(d);Kd=DK(d)
 def N4(v):
  vv=vm(v,v);tv=trc(v)
  return (2*trc(vm(d,vv))-F2*trc(vv)-4*tv*trc(vm(d,v))
          +2*F2*tv*tv+trc(vm(v,DK(v))))
 def P2(v):
  vv=va(v,vs(-trc(v),one))
  return trc(vm(vm(vv,vv),vv))
 def mean(j):
  sq=2*trc(vm(rows[0],rows[1])) if j==1 else trc(vm(rows[j],rows[j]))
  return sq-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
 return {'one':one,'va':va,'vm':vm,'tr':trc,'d':d,'F2':F2,
         'N4':N4,'P2':P2,'mean':mean}

# New ordinary moment identity BEFORE any quotient or factor choice.
ctx=fmpq_mpoly_ctx.get(('y','v'),'lex');yp,vp=ctx.gens()
NN=yp*yp-8*yp+7
E2p=(NN-2*yp*vp)/2
lam_p=(yp+vp+1)/2
E3p=(yp-2)**3+vp**3/2-(4*lam_p**3-6*lam_p**2+3*lam_p-1)
PP=5*yp**4-48*yp**3+180*yp*yp-276*yp+147
assert PP==6*(NN+2*yp*vp+2*yp*yp)*E2p-8*yp*E3p
assert 7==2*E2p+yp*(8+2*vp-yp)
P4=fmpq_poly([147,-276,180,-48,5])
unit,factors=P4.factor()
back=fmpq_poly([unit])
for phi,multiplicity in factors:back*=phi**int(multiplicity)
assert back==P4
factors=sorted(factors,key=lambda fm:(int(fm[0].degree()),tuple(str(fm[0][i]) for i in range(int(fm[0].degree())+1))))
say('new_B2_ell_three_halves_complete_moment_quartic_defined',
    P4=qprofile([QQ(P4[i]) for i in range(5)]),
    factors=[{'profile':qprofile([QQ(f[i]) for i in range(int(f.degree())+1)]),
              'multiplicity':int(e)} for f,e in factors],
    exactMomentIdentityReturned=True,exactYUnitIdentityReturned=True,
    scope='B2 AND ell=3/2 in corrected physical Phi only',
    oppositeRhoChoiceOnlyInterchangesOriginalSingletonLabels=True)
closed=[];unresolved=[]
for fi,(phi,exponent) in enumerate(factors):
 tick()
 pc=[QQ(phi[i]) for i in range(int(phi.degree())+1)]
 K.mod=ps(pc,1/pc[-1]);A.mod=None
 kd=len(K.mod)-1;y=K([0,1]);yi=y.inv()
 NN=y*y-8*y+7
 h=y-1;k=1+NN/(2*y)
 lam=(h+k+1)/2;Tmean=h+k/2-K(QQ(3,2));w=(3-y)/2
 A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1
 assert (h-1)**2+(k-1)**2/2==A2
 assert (h-1)**3+(k-1)**3/2==B3
 assert lam-1-Tmean==w
 Dphys=K(QQ(3,2))*A2-Tmean*Tmean
 assert Dphys==(h-k)**2/2
 if not lam or not Dphys:
  closed.append(fi)
  say('new_constant_factor_physically_absent',
      factor=fi,multiplicity=int(exponent),lambdaZero=not bool(lam),
      originalDZero=not bool(Dphys),wholeFactorRetainedUntilOriginalUnitApplied=True)
  continue
 # Only genuine constant-field units have been inverted so far.
 # D and lambda are only tested for a physically absent constant factor;
 # neither is inverted in the original value construction or the target.
 r0=h+k+h*k;R0=(1-h)*(1-k);j0=h+k/2
 uu=[K(),K(1)]
 def um(j):return [K(-j),K(1)]
 Ftilde=pn(pa(ps(pm(um(2),um(3)),3*lam),ps(pm(um(2),um(2)),3*j0)),
           pm(um(3),um(3)))
 Etilde=ps(pm(um(1),um(2)),-3*j0)
 lin=pa(ps(uu,1+h-2*k),[2*(k-h)])
 G=pa(pa(ps(Ftilde,-r0),ps(Etilde,R0)),ps(pm(um(3),lin),w))
 assert len(G)<=3
 # Entire ordinary K[u,t] scaled raw Gram. No u denominator is inverted.
 u=A(uu);rho=2*u-3;p=1+rho;q=1-rho;s=u-1
 H=rho*(u-3);Ft=A(Ftilde);Et=A(Etilde);tt=T([A(),A(1)])
 Vs=T(rho*(Ft-Et))+tt*T(H/2)
 Ws=T(2*H*s*(u-3)+2*rho*u*Ft)
 Xs=(Ws-T(q)*Vs).exact(2*rho)
 Ys=(T(p)*Vs-Ws).exact(rho)
 rs=Xs+T(H*p/2)-tt*T(H/2)
 ss=Ys+T(H*q/2)-tt*T(H)
 rows=[[T(),T(),T(H*p),T(H*q)],
       [T(),T(2*rho*Et),rs,ss],
       [T(H*p),rs,T(),tt*T(H)],
       [T(H*q),ss,tt*T(H),T()]]
 raw=gram(rows)
 vphys=[T(1),T(A(w)),T(A(h)),T(A(k))]
 assert raw['F2']==T(2*rho*Ft)
 Nscaled=raw['N4'](vphys)
 assert Nscaled==T(2*rho*A(G))
 STAT['scaledGramNVReturns']+=1
 say('new_complete_scaled_Gram_NV_weight_polynomial_returned',
     factor=fi,multiplicity=int(exponent),Kdegree=kd,
     exactScale='H=(2u-3)(u-3); H*complete_NV=2(2u-3)*G(u)',
     weightPolynomial=kp(G),rawScaledNV=tp(Nscaled),
     noTZeroSpecialization=True,allOrdinaryUCoefficientsReturned=True)
 if not G:
  unresolved.append({'factor':fi,'reason':'whole original NV u-polynomial is zero'})
  continue
 if len(G)==1:
  assert G[0]*G[0].inv()==1
  closed.append(fi)
  say('new_constant_factor_closed_by_original_NV_constant',factor=fi)
  continue
 # Full u polynomial, not a selected root. Remove only actual old-weight primary parts.
 g=ps(G,1/G[-1]);gOriginal=g[:]
 paid=[K(1)]
 for aa in [uu,um(1),um(2),um(3),[K(-3),K(2)]]:paid=pm(paid,aa)
 removals=[]
 while len(g)>1:
  bad,_,_=px(g,paid)
  if len(bad)==1:break
  quot,rem=pd(g,bad);assert not rem
  assert pm(quot,bad)==g
  removals.append(kp(bad));g=quot
 if len(g)==1:
  closed.append(fi)
  say('new_whole_u_factor_closed_by_old_paid_primary_removal',
      factor=fi,originalU=kp(gOriginal),removals=removals)
  continue
 good,pa0,pb0=px(g,paid);assert good==[K(1)]
 assert pa(pm(pa0,g),pm(pb0,paid))==[K(1)]
 ud=len(g)-1;assert 1<=ud<=2
 A.mod=g
 u=A(uu);rho=2*u-3;s=u-1;Qw=-4*s*(u-2);delta=rho*rho
 ell=A(QQ(3,2));bc=A(QQ(1,2));m=u-ell
 lamA=A(lam);Tm=A(Tmean);wA=A(w);hA=A(h);kA=A(k)
 D=A(Dphys);P02=3*s*Qw;T0=4*s*(u-3)
 # Every original denominator in this finite algebra is checked by actual multiplication.
 for z in [u,s,u-2,u-3,rho,Qw,delta,P02]:
  assert z*z.inv()==1
 f=A(Ftilde)/(u-3);E=A(Etilde)/(u-3)
 tt=T([A(),A(1)]);V=T(f-E)+tt*T(bc)
 W1=T(T0/2+2*u*f);p=1+rho;q=1-rho
 X=(W1-T(q)*V)/T(2*rho);Y=(T(p)*V-W1)/T(rho)
 rs=X+T(p/2)-tt*T(bc);ss=Y+T(q/2)-tt
 rows=[[T(),T(),T(p),T(q)],
       [T(),T(2*E),rs,ss],
       [T(p),rs,T(),tt],
       [T(q),ss,tt,T()]]
 raw=gram(rows);N4=raw['N4'];P2=raw['P2'];mean=raw['mean']
 assert raw['F2']==T(2*f)
 assert mean(0)==T()
 assert P2(rows[0])==T(P02)
 assert N4(rows[0])==T(2*lamA*P02)
 vphys=[T(1),T(wA),T(hA),T(kA)]
 assert raw['tr'](vphys)==T(lamA)
 assert N4(vphys)==T()
 v0=[x-T(u)*one for x,one in zip(rows[0],raw['one'])]
 d1=raw['tr'](rows[1]);v1=[x-d1*one for x,one in zip(rows[1],raw['one'])]
 assert 3*raw['tr'](raw['vm'](raw['vm'](v0,v0),v1))==T(3*wA*P02)
 E1,EB,EC=[mean(i) for i in (1,2,3)]
 N1=N4(raw['va'](rows[0],rows[1]))-N4(rows[0])-N4(rows[1])-T(4*lamA*wA*P02)
 NB=N4(rows[2])-T(2*lamA*P02*hA*hA)
 NC=N4(rows[3])-T(2*lamA*P02*kA*kA)
 PB=P2(rows[2])-T(P02*hA**3)
 PC=P2(rows[3])-T(P02*kA**3)
 seeds=[E1,EB,EC,N1,NB,NC,PB,PC]
 labels=['true_dual_E1','complete_EB','complete_EC','complete_N1',
         'complete_NB','complete_NC','complete_PB','complete_PC']
 Rcal=(EB+EC/2-E1)/2
 Bq=Qw*Qw+(2*u*u-3)*Qw+2*s*(2*u-1)*(u-2)
 gammaR=-Bq/(ell*bc*s*Qw);gammaO=-8*delta/ell
 EBo=(EB-EC)/T(2*rho)
 qt=T(gammaR)*Rcal+T(gammaO)*EBo
 qtags=[T(-gammaR/2),T(gammaR/2+gammaO/(2*rho)),
        T(gammaR/4-gammaO/(2*rho))]+[T() for _ in range(5)]
 assert len(qt.c)==3 and qt.c[-1]==1
 assert qt==sum((qtags[i]*seeds[i] for i in range(8)),T())
 STAT['monicTOriginalReturns']+=1
 N=2*kd*ud
 assert N<=16
 def flat(v):
  v=T(v);assert len(v.c)<=2
  return [v.coeff(ti).coeff(ui).coeff(yi)
          for ti in range(2) for ui in range(ud) for yi in range(kd)]
 def tdiv(v):
  quo,rem=pd(T(v).c,qt.c)
  quo,rem=T(quo),T(rem)
  assert T(v)==quo*qt+rem
  return quo,rem
 basis=[]
 for ti in range(2):
  for ui in range(ud):
   for yi in range(kd):
    a=A((K([0,1])**yi))*u**ui
    basis.append(T(a)*(tt**ti))
 assert len(basis)==N
 columns=[];ctags=[]
 for oi,F in enumerate(seeds):
  for mon in basis:
   quot,rem=tdiv(mon*F)
   tags=[-quot*qtags[i] for i in range(8)]
   tags[oi]+=mon
   assert rem==sum((tags[i]*seeds[i] for i in range(8)),T())
   columns.append(flat(rem));ctags.append(tags)
   STAT['rawColumnReturns']+=1
 say('new_whole_quartic_u_and_original_t_finite_algebra',
     factor=fi,multiplicity=int(exponent),Kdegree=kd,uDegree=ud,
     originalU=kp(gOriginal),goodU=kp(g),paidPrimaryRemovals=removals,
     dimension=N,rawLabels=labels,rawProfiles=[tp(z) for z in seeds],
     monicT=tp(qt),actualRawColumns=len(columns),
     retainsAllUAndTMultiplicities=True,noDInverse=True)
 # Rational Gaussian arithmetic only selects combinations of the actual raw columns.
 piv={}
 for j,col in enumerate(columns):
  v=col[:];rep={j:QQ(1)}
  for pi in sorted(piv):
   pv,pr=piv[pi]
   if not v[pi]:continue
   c=v[pi];v=[x-c*y for x,y in zip(v,pv)]
   for key,value in pr.items():
    rep[key]=rep.get(key,QQ(0))-c*value
    if not rep[key]:del rep[key]
  nz=next((i for i,x in enumerate(v) if x),None)
  if nz is None:continue
  iv=1/v[nz];assert iv*v[nz]==1
  v=[x*iv for x in v];rep={i:x*iv for i,x in rep.items()}
  back=[sum((coeff*columns[index][row] for index,coeff in rep.items()),QQ(0))
        for row in range(N)]
  assert back==v
  STAT['rationalVectorReturns']+=1
  piv[nz]=(v,rep)
 def solve(target):
  v=target[:];sol={}
  for pi in sorted(piv):
   pv,pr=piv[pi]
   if not v[pi]:continue
   c=v[pi];v=[x-c*y for x,y in zip(v,pv)]
   for key,value in pr.items():
    sol[key]=sol.get(key,QQ(0))+c*value
    if not sol[key]:del sol[key]
  if any(v):return None
  assert [sum((coeff*columns[index][row] for index,coeff in sol.items()),QQ(0))
          for row in range(N)]==target
  STAT['rationalVectorReturns']+=1
  return sol
 U=T(lamA*D*(f-u))*tt
 success=False
 for exponent_target in range(N+1):
  tick();target=U**exponent_target
  tq,rem=tdiv(target);sol=solve(flat(rem))
  if sol is None:continue
  Omega=[tq*qtags[i] for i in range(8)]
  for j,coeff in sol.items():
   for i in range(8):Omega[i]+=T(coeff)*ctags[j][i]
  assert target==sum((Omega[i]*seeds[i] for i in range(8)),T())
  STAT['finalEightOriginalReturns']+=1
  closed.append(fi);success=True
  say('new_whole_constant_factor_original_positive_target_returned',
      factor=fi,constantMultiplicity=int(exponent),
      originalU=kp(gOriginal),goodU=kp(g),dimension=N,rank=len(piv),
      targetPower=exponent_target,target='[lambda*D*t*(f-u)]^n',
      targetProfile=tp(target),actualEightOriginalMultipliers=[tp(o) for o in Omega],
      entireOriginalTPolynomialReturned=True,
      noInverseOfPhysicalTOrFminusUOrD=True,statistics=STAT)
  break
 if not success:
  unresolved.append({'factor':fi,'reason':'no prescribed original target returned',
                     'dimension':N,'rank':len(piv),'maxPositivePower':N})
  say('new_whole_constant_factor_retained',
      factor=fi,dimension=N,rank=len(piv),maxPositivePower=N,
      allOriginalFibersRetained=True,statistics=STAT)
say('new_B2_ell_three_halves_original_finite_input_complete',
    constantFactors=len(factors),closedFactors=closed,unresolved=unresolved,
    excludesWholeNamedIntersection=(not unresolved and len(closed)==len(factors)),
    onlySecondHeadAndEllThreeHalves=True,noWholePhiClaim=True,
    allConstantAndUPrimaryMultiplicitiesAccountedFor=True,
    noOldGateReplayed=True,statistics=STAT)
