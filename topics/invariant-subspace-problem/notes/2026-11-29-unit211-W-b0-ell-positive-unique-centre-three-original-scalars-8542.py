#!/usr/bin/env python3
"""FIRST NEW ell-positive unique Astar centre, complete finite-mu T-unit input.
The original valuation proof pays e,k,u,delta,Vbar units, ell integral,
then excludes Astar-unit, mu/T poles and the complete T-zero residue.
At U=-5/4, k=-1/2, Q=9/8, keep all finite mu and all nonzero T.
Return N5=2*ell^2*H from its complete original definition before residue.
Two fixed Sylvester capacities (3,4),(3,5), no selected root or head inverse.
All three original residual tags, then FIRST joint F_1009[mu] Bezout.
Only mu*(mu^2+4mu+5) paid on this T-unit chart by the displayed paper proof.
120 seconds /1 GiB, outer135; no old gate, retry, coefficient payload or cache.
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
ctx=fmpq_mpoly_ctx.get(('mu','T','ell'),'lex')
mp,tp,ep=ctx.gens();Z=ctx.constant(0);O=ctx.constant(1)
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

mu,T,ell=map(R,(mp,tp,ep))
def exact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 STAT['exactPolynomialDivisionProducts']+=1
 return q
def weight(a):return all(int(ex[1])==0 and int(ex[2])==0 for ex in a.to_dict())
def deg_T(a):
 a=R(a);assert weight(a.d)
 return max((int(ex[1]) for ex in a.n.to_dict()),default=-1)
def coeff(a,j):
 a=R(a);assert weight(a.d)
 assert all(int(ex[2])==0 for ex in a.n.to_dict())
 return R(ctx.from_dict({(int(ex[0]),0,0):cc for ex,cc in a.n.to_dict().items()
                         if int(ex[1])==j}),a.d)
def profile(p):
 data=[[list(map(int,ex)),str(c)] for ex,c in sorted(p.to_dict().items())]
 raw=json.dumps(data,separators=(',',':')).encode()
 return {'degrees':list(map(int,p.degrees())) if p else [-1,-1,-1],
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
def lift(a):return ctx.from_dict({(i,0,0):cc for i,cc in enumerate(a) if cc})
def fprofile(a):
 bb=json.dumps(a,separators=(',',':')).encode()
 return {'degree':len(a)-1,'terms':sum(bool(v) for v in a),
         'bytes':len(bb),'sha256':hashlib.sha256(bb).hexdigest()}

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
     remainingNecessaryMuPolynomial=fprofile(remaining),
     paidSupport=profile(paidPoly),paidSupportPower=layers,
     returnedTarget=fprofile(target),
     actualAllOriginalMultiplierProfiles=[rp(v) for v in final],
     allOriginalCoefficientsReturnedModulo1009=True,
     excludesWholeNamedChart=(len(remaining)==1),statistics=STAT)



# Necessary complete original definitions, with T still free. The specialization
# fixes only the weight residue centre; it is NOT a physical f=0 substitution.
u=-R(5)/4;Q=R(9)/8;delta=1-Q;m=u-ell
M=delta*ell*ell-m*m;bc=M/(4*delta)
J=2*u*(1-u)+ell*Q;Ast=4*u*Q-J
Cst=Ast*m*m+J*delta*ell*ell
T0=2*u-ell*Q-2*u*u;Phi=T0+4*u-4+Q
P02=(2-3*u)*(2*u-ell*Q)-Q*u+2*u**3
lam=(mu+3)/2;A2=(mu*mu+4*mu+5)/2
B3=(mu**3+6*mu*mu+12*mu+7)/2
D=ell*A2-T*T;K=ell*ell*B3-3*ell*A2*T+2*T**3
blinear=Ast*T-u*Q*ell*mu
q2=2*Cst*A2+2*M*ell*Q*(3-4*lam)-8*u*Q*delta*ell*T*T
qtilde=4*u*delta*D*T-M*(u*mu*A2+(3+2*mu)*T)
assert Q*ell*qtilde-T*q2/2-M*A2*blinear==0
R6=M*K*K-4*m*m*D**3
C3=4*B3*T**3-3*A2*A2*T*T-6*ell*A2*B3*T+ell*ell*B3*B3+4*ell*A2**3
assert K*K+4*D**3==ell*ell*C3
Rdiv=R(exact(R6.n,ep*ep),R6.d)
assert Rdiv==delta*K*K-m*m*C3
G=lam*P02+(u-1)*T0;Pc=Q*P02*(ell+T)-G*T0
B=Pc/(Q*Phi);V=-G/Q-B
y=(ell*T0/2-u*V)/M;w=lam-1-T
ts=-B/bc
z1=2*(ell*mu-2*T)*y-2*ell*w+m*T*ts/delta
z2=-2*G/Q-4*m*y
Z0=2*(T-ell*mu)*(ell*u*w+V*T)+2*bc*ts*T*T
N5=2*m*D*(Z0+D*z2)+M*K*z1
theta=u-ell*Q
Hformula=(2*m/M)*(A2-mu*T)*((m*T0/2-theta*V)*T*T+M*A2*V)
Hformula+=y*(delta*K*(ell*mu-2*T)-m*m*(4*A2*A2-2*B3*T-3*mu*A2*T+ell*mu*B3))
Hformula+=w*(m*(-2*T**3+(2*u-3*m)*A2*T+2*u*mu*T*T)
               +ell*(-2*m*u*A2*mu+m*m*B3-delta*K))
Hformula+=2*m*B*(A2*A2-B3*T)
Hdiv=R(exact(N5.n,2*ep*ep),N5.d)
assert Hdiv==Hformula and N5==2*ell*ell*Hformula
STAT['completeN5EllSquaredFactorReturns']=1
def ell_zero_poly(p):
 return ctx.from_dict({(int(ex[0]),int(ex[1]),0):cc
                       for ex,cc in p.to_dict().items() if int(ex[2])==0})
def ell_zero(v):
 v=R(v);den=ell_zero_poly(v.d);assert den
 return R(ell_zero_poly(v.n),den)
q0=ell_zero(qtilde);r0=ell_zero(Rdiv);h0=ell_zero(Hdiv)
Qhat=-8*T**3-25*mu*A2+20*(3+2*mu)*T
Rhat=-8*T**4-100*B3*T+75*A2*A2
assert q0==R(5)/64*Qhat
assert r0==T*T*Rhat/16
V0=ell_zero(V);B0=ell_zero(B);T00=ell_zero(T0)
H0formula=-2*(A2-mu*T)*((T00/2-V0)*T*T-u*A2*V0)
H0formula+=(V0/u)*(-4*delta*T**4-u*u*(4*A2*A2-2*B3*T-3*mu*A2*T))
H0formula+=u*w*(-2*T**3-u*A2*T+2*u*mu*T*T)
H0formula+=2*u*B0*(A2*A2-B3*T)
assert h0==H0formula
RAW=[q0,r0/(T*T),h0]
ATOMS=[mp,mp*mp+4*mp+5]
basis=[];scales=[]
for val in RAW:
 integral(val,ATOMS)
 pp,removed=strip(val.n,ATOMS)
 scale=R(val.d,removed)
 assert R(pp)==scale*val
 integral(scale,ATOMS)
 basis.append(R(pp));scales.append(scale)
assert [deg_T(v) for v in basis]==[3,4,5]
say('new_ell_positive_unique_centre_complete_original_residues',
    originalN5=rp(N5),originalN5AfterExactTwoEllSquaredDivision=rp(Hdiv),
    qtildeReturnedFromOriginalQAndBlinear=True,
    originalR6EllSquaredFactorReturned=True,
    completeOriginalN5EllSquaredFactorReturned=True,
    residueProfiles=[rp(v) for v in RAW],
    normalizedProfiles=[rp(v) for v in basis],
    exactOriginalScales=[rp(v) for v in scales],
    allTUnitAndAllFiniteMuRetained=True,
    noAstarOrEllOrUnpaidHeadInverseInResidue=True,
    oldBoundaryGatesNotExecuted=True,statistics=STAT)
def cofactor_pair(ia,ib,ma,mb):
 # Columns T^j*p_a, j<mb and T^j*p_b, j<ma.
 n=ma+mb
 columns=[basis[ia]*T**j for j in range(mb)]+[basis[ib]*T**j for j in range(ma)]
 assert all(deg_T(v)<n for v in columns)
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
 omega[ia]=sum((R(co[j])*T**j for j in range(mb)),R())*scales[ia]
 omega[ib]=sum((R(co[mb+j])*T**j for j in range(ma)),R())*scales[ib]
 assert R(determinant)==sum((omega[i]*RAW[i] for i in range(3)),R())
 STAT['fullOriginalReturns']+=1
 scalar,removed=strip(determinant,ATOMS)
 omega=[v/R(removed) for v in omega]
 assert R(scalar)==sum((omega[i]*RAW[i] for i in range(3)),R())
 for v in omega:integral(v,ATOMS)
 STAT['fullOriginalReturns']+=1
 return (scalar,omega),{'determinant':profile(determinant),
                        'removedOnlyProvedMuSupport':profile(removed)}

results=[]
for ia,ib,ma,mb in [(0,1,3,4),(0,2,3,5)]:
 value,metadata=cofactor_pair(ia,ib,ma,mb)
 if value is None:
  results.append((Z,[R(),R(),R()]))
  say('new_ell_positive_fixed_pair_scalar_zero',
      originalPair=[ia,ib],capacities=[ma,mb],
      noDifferentMinorTried=True,**metadata)
 else:
  scalar,omega=value;results.append(value)
  say('new_ell_positive_fixed_pair_full_original_return',
      originalPair=[ia,ib],capacities=[ma,mb],
      scalar=profile(scalar),actualThreeOriginalMultipliers=[rp(v) for v in omega],
      entireCofactorAndAllOriginalCoordinatesReturned=True,**metadata)
original_modular_joint('new_ell_positive_two_original_scalars',
    RAW,[v[0] for v in results],[v[1] for v in results],ATOMS)
say('new_ell_positive_complete_finite_centre_target_finished',
    fixedPairCapacities=[[3,4],[3,5]],
    noOldGateReplayed=True,noOtherInternalBoundaryClaim=True,
    ordinaryISPClaim=False,noCoefficientCacheWritten=True,
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    statistics=STAT)
