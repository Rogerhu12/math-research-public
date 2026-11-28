#!/usr/bin/env python3
"""FIRST NEW full finite-mu Vbar-positive original target.
Use only necessary original residual definitions from 7fe1, not either
completed M-zero or mu-pole proof gate. All four special L centers and
both M-zero centers already excluded; mu is integral.
Three fixed original scalar sources: Sylvester capacities (2,6) for
q2/R6, capacities (2,5) for q2/N5, and the complete pseudoremainder
linear wedge of R6 and N5 by q2, with all three original tags.
One FIRST joint F_1009[L] Bezout, only old paid L support removed.
No mu-head inverse, no selected L or mu root, no adaptive minor/prime.
120 seconds /1 GiB, outer135; no retries, no coefficient cache.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq_mpoly_ctx
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
P=1009
STAT={'exactPolynomialDivisionProducts':0,'cofactorCoordinates':0,
      'fullOriginalReturns':0,'paidSupportProducts':0,'pIntegralChecks':0,
      'finiteFieldDivisions':0,'finiteFieldBezoutChecks':0}
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute120')
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True,separators=(',',':')),flush=True)
ctx=fmpq_mpoly_ctx.get(('L','mu'),'lex')
lp,mp=ctx.gens();Z=ctx.constant(0);O=ctx.constant(1)
def polynomial(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=polynomial(n);d=O if d is None else polynomial(d);assert d
  if not n:self.n=Z;self.d=O;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  s=d.coefficient(0);self.n=n/s;self.d=d/s
 def __bool__(self):return bool(self.n)
 def __add__(self,v):
  v=R(v)
  if not self:return v
  if not v:return self
  g=self.d.gcd(v.d);a=self.d/g;b=v.d/g
  return R(self.n*b+v.n*a,a*v.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,v):return self+-R(v)
 def __rsub__(self,v):return R(v)+-self
 def __mul__(self,v):
  v=R(v)
  if not self or not v:return R()
  g=self.n.gcd(v.d);h=v.n.gcd(self.d)
  return R((self.n/g)*(v.n/h),(self.d/h)*(v.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,v):
  v=R(v);assert v
  return self*R(v.d,v.n,False)
 def __rtruediv__(self,v):return R(v)/self
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  return R(self.n**n,self.d**n,False)
 def __eq__(self,v):
  v=R(v);return self.n*v.d==v.n*self.d

L,mu=map(R,(lp,mp))
def exact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 STAT['exactPolynomialDivisionProducts']+=1
 return q
def weight(a):return all(int(ex[1])==0 for ex in a.to_dict())
def deg_mu(a):
 a=R(a);assert weight(a.d)
 return max((int(ex[1]) for ex in a.n.to_dict()),default=-1)
def coeff(a,j):
 a=R(a);assert weight(a.d)
 return R(ctx.from_dict({(int(ex[0]),0):cc for ex,cc in a.n.to_dict().items()
                         if int(ex[1])==j}),a.d)
def profile(p):
 data=[[list(map(int,ex)),str(c)] for ex,c in sorted(p.to_dict().items())]
 raw=json.dumps(data,separators=(',',':')).encode()
 return {'degrees':list(map(int,p.degrees())) if p else [-1,-1],
         'totalDegree':int(p.total_degree()) if p else -1,
         'terms':len(data),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def rp(v):
 v=R(v);return {'numerator':profile(v.n),'denominator':profile(v.d)}
def strip(p,atoms):
 if not p:return p,O
 before=p;removed=O
 for atom in atoms:
  while p:
   tick();g=p.gcd(atom)
   if int(g.total_degree())==0:break
   p=exact(p,g);removed*=g;STAT['paidSupportProducts']+=1
 assert p*removed==before
 return p,removed
def paid(p,atoms):
 assert p and weight(p)
 rr,_=strip(p,atoms);assert int(rr.total_degree())==0
def cmod(c):
 s=str(c)
 nu,de=map(int,s.split('/')) if '/' in s else (int(s),1)
 assert de%P
 return (nu%P)*pow(de%P,P-2,P)%P
def integral(v,atoms):
 v=R(v);paid(v.d,atoms)
 for pp0 in [v.n,v.d]:
  for cc in pp0.to_dict().values():cmod(cc)
 STAT['pIntegralChecks']+=1
 return v
def ft(a):
 a=[int(c)%P for c in a]
 while a and not a[-1]:a.pop()
 return a
def fa(a,b):
 return ft([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
            for i in range(max(len(a),len(b)))])
def fs(a,b):return fa(a,[-c for c in b])
def fm(a,b):
 if not a or not b:return []
 cc=[0]*(len(a)+len(b)-1)
 for i,x0 in enumerate(a):
  for j,y0 in enumerate(b):cc[i+j]=(cc[i+j]+x0*y0)%P
 return ft(cc)
def fscale(a,c):return ft([c*v for v in a])
def fd(a,b):
 tick();a0=ft(a);bb=ft(b);assert bb
 rr=list(a0);qq=[0]*max(0,len(rr)-len(bb)+1);inv=pow(bb[-1],P-2,P)
 while rr and len(rr)>=len(bb):
  j=len(rr)-len(bb);vv=rr[-1]*inv%P;qq[j]=vv
  for i,cc in enumerate(bb):rr[j+i]=(rr[j+i]-vv*cc)%P
  rr=ft(rr)
 qq=ft(qq);assert fa(fm(qq,bb),rr)==a0
 STAT['finiteFieldDivisions']+=1
 return qq,rr
def fx(a,b):
 r0,r1=ft(a),ft(b);s0,s1=[1],[];t0,t1=[],[1]
 while r1:
  qq,r2=fd(r0,r1)
  r0,r1=r1,r2;s0,s1=s1,fs(s0,fm(qq,s1));t0,t1=t1,fs(t0,fm(qq,t1))
 if not r0:return [],[],[]
 cc=pow(r0[-1],P-2,P)
 gg,ss,tt=fscale(r0,cc),fscale(s0,cc),fscale(t0,cc)
 assert fa(fm(ss,a),fm(tt,b))==gg
 STAT['finiteFieldBezoutChecks']+=1
 return gg,ss,tt
def fexact(a,b):
 qq,rr=fd(a,b);assert not rr;return qq
def fpower(a,n):
 out=[1]
 for _ in range(n):out=fm(out,a)
 return out
def from_poly(p):
 assert weight(p)
 out=[0]*(int(p.degrees()[0])+1) if p else []
 for ex,cc in p.to_dict().items():out[int(ex[0])]=cmod(cc)
 return ft(out)
def lift(a):return ctx.from_dict({(i,0):cc for i,cc in enumerate(a) if cc})
def fprofile(a):
 bb=json.dumps(a,separators=(',',':')).encode()
 return {'degree':len(a)-1,'terms':sum(bool(v) for v in a),
         'bytes':len(bb),'sha256':hashlib.sha256(bb).hexdigest()}

BASE=[lp,2*lp-1,4*lp-1,7-4*lp]
F=8*lp*lp-4*lp+1
def original_modular_joint(label,original,scalars,tags,atoms):
 assert len(scalars)==len(tags)
 for row,scalar in zip(tags,scalars):
  assert len(row)==len(original)
  assert R(scalar)==sum((row[i]*original[i] for i in range(len(original))),R())
  STAT['fullOriginalReturns']+=1
  for v in row:integral(v,atoms)
  for c in scalar.to_dict().values():cmod(c)
 sf=[from_poly(s) for s in scalars]
 gg=[];weights=[[] for _ in sf]
 for j,ss in enumerate(sf):
  if not ss:continue
  new,a,b=fx(gg,ss)
  weights=[fm(a,w) for w in weights];weights[j]=fa(weights[j],b);gg=new
 recomposed=[]
 for w,s in zip(weights,sf):recomposed=fa(recomposed,fm(w,s))
 assert recomposed==gg;STAT['finiteFieldBezoutChecks']+=1
 if not gg:
  say(label+'_all_zero_mod1009',retained=True,statistics=STAT);return
 paidPoly=O
 for atom in atoms:paidPoly*=atom
 Uf=from_poly(paidPoly);remaining=gg[:];removed=[1];layers=0
 while len(remaining)>1:
  common=fx(remaining,Uf)[0]
  if len(common)==1:break
  remaining=fexact(remaining,common);removed=fm(removed,common);layers+=1
 assert fm(remaining,removed)==gg
 support=fpower(Uf,layers);quotient=fexact(support,removed)
 weights=[fm(w,quotient) for w in weights]
 target=fm(support,remaining);combined=[]
 for w,s in zip(weights,sf):combined=fa(combined,fm(w,s))
 assert target==combined
 final=[sum((R(lift(weights[j]))*tags[j][i] for j in range(len(tags))),R())
        for i in range(len(original))]
 for v in final:integral(v,atoms)
 difference=sum((final[i]*original[i] for i in range(len(original))),R())-R(lift(target))
 integral(difference,atoms)
 assert all(cmod(cc)==0 for cc in difference.n.to_dict().values())
 STAT['fullOriginalReturns']+=1
 say(label+'_complete_original_Bezout_return',
     originalProfiles=[rp(v) for v in original],
     scalarProfiles=[fprofile(v) for v in sf],
     exactJointGcd=fprofile(gg),removedPaidSupport=fprofile(removed),
     remainingNecessaryLPolynomial=fprofile(remaining),
     paidSupport=profile(paidPoly),paidSupportPower=layers,
     returnedTarget=fprofile(target),
     actualAllOriginalMultiplierProfiles=[rp(v) for v in final],
     allOriginalCoefficientsReturnedModulo1009=True,
     excludesWholeNamedChart=(len(remaining)==1),statistics=STAT)


# Complete original residual definitions; not a physical f=0 specialization.
u=R(1)/2;Q=R(2);delta=R(-1);ell=L;m=u-L
M=delta*L*L-m*m;bc=M/(4*delta)
J=2*u*(1-u)+L*Q;Ast=4*u*Q-J
Cst=Ast*m*m+J*delta*L*L
T0=2*u-L*Q-2*u*u;Phi=T0+4*u-4+Q
P02=(2-3*u)*(2*u-L*Q)-Q*u+2*u**3
lam=(mu+3)/2;T=u*Q*L*mu/Ast
A2=(mu*mu+4*mu+5)/2;B3=(mu**3+6*mu*mu+12*mu+7)/2
D=L*A2-T*T;K=L*L*B3-3*L*A2*T+2*T**3
q2=2*Cst*A2+2*M*L*Q*(3-4*lam)-8*u*Q*delta*L*T*T
R6=M*K*K-4*m*m*D**3
G=lam*P02-(1-u)*T0;Pc=Q*P02*(L+T)-G*T0
ts=-Pc/(bc*Q*Phi);Vs=-G/Q-Pc/(Q*Phi);Ws=T0/2
ys=(L*Ws-u*Vs)/M;w=lam-1-T
z1=-2*(-L*mu+2*T)*ys-2*L*w+m*T*ts/delta
z2=-2*G/Q-4*m*ys
Z0=2*(T-L*mu)*(L*u*w+Vs*T)+2*bc*ts*T*T
N5=2*m*D*(Z0+D*z2)+M*K*z1

STAT['pseudoDivisionSteps']=0
ATOMS=BASE+[F]
RAW=[q2,R6,N5]
LABELS=['complete_q2_finite_mu','complete_R6_finite_mu','complete_N5_finite_mu']
basis=[];scales=[]
for val in RAW:
 integral(val,ATOMS)
 p,removed=strip(val.n,ATOMS)
 scale=R(val.d,removed)
 assert R(p)==scale*val
 integral(scale,ATOMS)
 basis.append(R(p));scales.append(scale)
assert [deg_mu(v) for v in basis]==[2,6,5]
say('new_Vbar_finite_mu_three_complete_original_inputs',
    labels=LABELS,originalProfiles=[rp(v) for v in RAW],
    normalizedProfiles=[rp(v) for v in basis],
    exactOriginalScales=[rp(v) for v in scales],
    allMuIncludingZeroAndLambdaZeroRetained=True,
    alreadyProvedMUnitAndMuIntegral=True,
    oldMZeroAndPoleGatesNotExecuted=True)
def cofactor_pair(ia,ib,ma,mb):
 # Columns mu^j*p_a, j<mb and mu^j*p_b, j<ma.
 n=ma+mb
 columns=[basis[ia]*mu**j for j in range(mb)]+[basis[ib]*mu**j for j in range(ma)]
 assert all(deg_mu(v)<n for v in columns)
 mat=[[coeff(v,i).n for v in columns] for i in range(n)]
 assert all(coeff(v,i).d==O for v in columns for i in range(n))
 work=[list(mat[i])+[O if i==0 else Z] for i in range(n)]
 previous=O;sign=1
 for i in range(n-1):
  tick();pivot=next((r for r in range(i,n) if work[r][i]),None)
  if pivot is None:return None,{'zeroPivotStep':i}
  if pivot!=i:work[i],work[pivot]=work[pivot],work[i];sign=-sign
  v=work[i][i]
  for r in range(i+1,n):
   a=work[r][i]
   for c in range(i+1,n+1):work[r][c]=exact(v*work[r][c]-a*work[i][c],previous)
   work[r][i]=Z
  previous=v
 if not work[-1][-2]:return None,{'zeroPivotStep':n-1}
 determinant=sign*work[-1][-2];co=[Z]*n
 for i in range(n-1,-1,-1):
  numerator=determinant*work[i][n]-sum((work[i][j]*co[j] for j in range(i+1,n)),Z)
  co[i]=exact(numerator,work[i][i])
 for i in range(n):
  assert sum((mat[i][j]*co[j] for j in range(n)),Z)==(determinant if i==0 else Z)
  STAT['cofactorCoordinates']+=1
 omega=[R(),R(),R()]
 omega[ia]=sum((R(co[j])*mu**j for j in range(mb)),R())*scales[ia]
 omega[ib]=sum((R(co[mb+j])*mu**j for j in range(ma)),R())*scales[ib]
 assert R(determinant)==sum((omega[i]*RAW[i] for i in range(3)),R())
 STAT['fullOriginalReturns']+=1
 scalar,removed=strip(determinant,ATOMS)
 omega=[v/R(removed) for v in omega]
 assert R(scalar)==sum((omega[i]*RAW[i] for i in range(3)),R())
 for v in omega:integral(v,ATOMS)
 STAT['fullOriginalReturns']+=1
 return (scalar,omega),{'determinant':profile(determinant),
                        'removedOnlyOldPaidSupport':profile(removed)}
results=[]
for ia,ib,ma,mb in [(0,1,2,6),(0,2,2,5)]:
 value,metadata=cofactor_pair(ia,ib,ma,mb)
 if value is None:
  results.append((Z,[R(),R(),R()]))
  say('new_Vbar_finite_mu_fixed_pair_scalar_zero',
      originalPair=[ia,ib],capacities=[ma,mb],
      noDifferentMinorTried=True,**metadata)
 else:
  scalar,omega=value;results.append(value)
  say('new_Vbar_finite_mu_fixed_pair_full_original_return',
      originalPair=[ia,ib],capacities=[ma,mb],
      scalar=profile(scalar),actualThreeOriginalMultipliers=[rp(v) for v in omega],
      entireCofactorAndAllOriginalCoordinatesReturned=True,**metadata)
def pseudo_linear(index):
 r=basis[index];omega=[R(),R(),R()];omega[index]=scales[index]
 h=coeff(basis[0],2);assert h
 while deg_mu(r)>=2:
  tick();d=deg_mu(r);head=coeff(r,d);mon=mu**(d-2)
  r=h*r-head*mon*basis[0]
  omega=[h*v for v in omega];omega[0]-=head*mon*scales[0]
  assert r==sum((omega[i]*RAW[i] for i in range(3)),R())
  STAT['pseudoDivisionSteps']+=1;STAT['fullOriginalReturns']+=1
 assert deg_mu(r)<=1
 for v in omega:integral(v,ATOMS)
 return r,omega
r,rt=pseudo_linear(1);n,nt=pseudo_linear(2)
r1,n1=coeff(r,1),coeff(n,1)
wedge=r1*n-n1*r
omega=[r1*nt[i]-n1*rt[i] for i in range(3)]
assert deg_mu(wedge)<=0
assert wedge==sum((omega[i]*RAW[i] for i in range(3)),R())
STAT['fullOriginalReturns']+=1
scalar,removed=strip(wedge.n,ATOMS)
omega=[v*R(wedge.d,removed) for v in omega]
assert R(scalar)==sum((omega[i]*RAW[i] for i in range(3)),R())
STAT['fullOriginalReturns']+=1
for v in omega:integral(v,ATOMS)
results.append((scalar,omega))
say('new_Vbar_finite_mu_pseudolinear_wedge_full_original_return',
    completeRemainderProfiles=[rp(r),rp(n)],
    scalar=profile(scalar),removedOnlyOldPaidSupport=profile(removed),
    actualThreeOriginalMultipliers=[rp(v) for v in omega],
    noQuadraticHeadInverse=True,statistics=STAT)
original_modular_joint('new_Vbar_finite_mu_three_original_scalars',
    RAW,[v[0] for v in results],[v[1] for v in results],ATOMS)
say('new_Vbar_complete_finite_mu_target_finished',
    fixedPairCapacities=[[2,6],[2,5]],fixedThirdScalar='complete_R_N_pseudolinear_wedge',
    noOldMZeroOrPoleGateReplayed=True,noOtherInternalBoundaryClaim=True,
    ordinaryISPClaim=False,noCoefficientCacheWritten=True,
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),statistics=STAT)
