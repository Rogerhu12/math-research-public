#!/usr/bin/env python3
"""NEW whole W: all original I6/I11 in the SAME pure (lambda,T) coordinates.
Only necessary TRUE Gram, qf and the already-paid f-head definitions are
reconstructed. No old six f-multiple/pair/norm, head factorization, resultant,
native action, or frozen NV matrix gate is run.
NEW targets: full NS/PS and both individual odd N/P components are divided
by the original monic qf, then use the SAME f=-g. Every new pure row returns
its complete six/eleven original coefficients. Pure C4/R6/N5 replace the
whole Vlow by the published exact original ideal identity, with no D inverse.
No lambda/T head, resultant, norm, D or b0 inverse. 180 seconds / 4 GiB.
Only definitions/profiles/SHA and small receipts; no coefficient cache.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq_mpoly_ctx
START=time.perf_counter()
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
signal.setitimer(signal.ITIMER_REAL,180)
def say(stage,**data):
 data.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(data,separators=(',',':')),flush=True)
ctx=fmpq_mpoly_ctx.get(('e','k','lam','T','f'),'lex')
ep,kp,lp,tp,fp=ctx.gens();Z=ctx.constant(0);O=ctx.constant(1)
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

e,k,lam,T,f=map(R,(ep,kp,lp,tp,fp))
u=e+1;Q=e*k;Vbar=u*k+2;delta=1-Q
ell=u*((k+2)**2-2*e*k)/(k*Vbar)
m=u-ell;theta=u-ell*Q;V2=2*u-ell*Q
M=ell*V2-u*u;bc=M/(4*delta)
T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
Phi=T0+4*u-4+Q;Pf=T0*(J-Q)
P02=(2-3*u)*V2-Q*u+2*u**3
assert M==ell*ell*delta-m*m
assert J*Phi-Pf==2*u*Q*Phi
beta=2*u-J/Q
assert u-beta==-u*e*(k+4)/Vbar
assert u-beta==u*Phi/(2*e)
G=lam*P02-(1-u)*T0
Pc=Q*P02*(ell+T)-G*T0
t=-(Pf*f+Pc)/(bc*Q*Phi)
V=(J*f-G+bc*Q*t)/Q
W1=T0/2+2*u*f
x=(theta*V-m*W1)/M
y=(ell*W1-u*V)/M
A1=2*f-2*V+2*bc*t

statistics={'exactPolynomialDivisionProducts':0,
 'originalFCoefficientReturns':0,'paidSupportProducts':0,
 'fourSourceContentCancellations':0,'sameFNormIdentities':0}
def exact(p,g):
 out,rem=divmod(p,g);assert not rem and out*g==p
 statistics['exactPolynomialDivisionProducts']+=1
 return out
def weight(p):
 return all(all(int(ex[j])==0 for j in (2,3,4)) for ex in p.to_dict())
def f_free(p):return all(int(ex[4])==0 for ex in p.to_dict())
def fdeg(v):
 v=R(v);assert weight(v.d)
 return max((int(ex[4]) for ex in v.n.to_dict()),default=-1)
def fc(v,j):
 v=R(v);assert weight(v.d)
 return R(ctx.from_dict({(int(ex[0]),int(ex[1]),int(ex[2]),int(ex[3]),0):c
       for ex,c in v.n.to_dict().items() if int(ex[4])==j}),v.d)
def geomdegree(v):
 v=R(v);assert weight(v.d)
 return max((sum(int(ex[j]) for j in (2,3,4))
      for ex in v.n.to_dict()),default=-1)
def profile(p):
 data=[[list(map(int,ex)),str(c)] for ex,c in sorted(p.to_dict().items())]
 raw=json.dumps(data,separators=(',',':')).encode()
 return {'zero':not bool(p),
  'degrees_e_k_lambda_T_f':list(map(int,p.degrees())) if p else [-1]*5,
  'totalDegree':int(p.total_degree()) if p else -1,'terms':len(data),
  'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
# Only the currently proved pure-weight W supports. Neither E1=EW,
# nor any new lambda,T,f head nor D is assumed.
paid_atoms=[('e',ep),('k',kp),('u',ep+1),('delta',ep*kp-1),
 ('Vbar',(ep+1)*kp+2),('Phi_k_plus_four',kp+4),('P02',P02.n),
 ('M',M.n),('whole_equal_weights_k_plus_two',kp+2),
 ('whole_ell_zero',ell.n),('whole_equal_weights_m',m.n),
 ('whole_original_Lhalf',(2*ell-1).n)]
def strip(p):
 if not p:return p,O,[]
 before=p;removed=O;history=[]
 for label,atom in paid_atoms:
  assert atom and weight(atom)
  layers=0
  while p:
   gg=p.gcd(atom)
   if int(gg.total_degree())==0:break
   p=exact(p,gg);removed*=gg;layers+=1
   statistics['paidSupportProducts']+=1
  if layers:history.append({'paidSupport':label,'gcdLayers':layers})
 assert p*removed==before
 return p,removed,history
den_seen=set()
def paid(p):
 assert p and weight(p)
 key=str(p)
 if key in den_seen:return
 rr,_,_=strip(p);assert rr and int(rr.total_degree())==0
 den_seen.add(key)
def ck(v):
 v=R(v);paid(v.d);return v
for v in [u,Q,Vbar,delta,ell,m,M,bc,Phi,P02,t,V,W1,x,y,A1]:
 ck(v)
assert fc(t,1)==beta/bc and fc(V,1)==2*u and fc(W1,1)==2*u
assert fc(x,1)==2*u*ell*delta/M and fc(y,1)==-2*u*m/M

# Actual quadratic extension and TRUE dual-number Gram. No compact
# derivative-square replacement is used anywhere in this source.
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,v):
  v=E(v);return E(self.a+v.a,self.b+v.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,v):return self+-E(v)
 def __rsub__(self,v):return E(v)+-self
 def __mul__(self,v):
  v=E(v);return E(self.a*v.a+delta*self.b*v.b,self.a*v.b+self.b*v.a)
 __rmul__=__mul__
 def __truediv__(self,v):
  v=R(v);return E(self.a/v,self.b/v)
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  out=E(1)
  for _ in range(n):out=out*self
  return out
 def __eq__(self,v):
  v=E(v);return self.a==v.a and self.b==v.b
 def conj(self):return E(self.a,-self.b)
b=E(ell/2,m/(2*delta));c=b.conj();a=E(1-ell)
p=E(1,1);q=p.conj();X=E(x,y);Y=X.conj()
assert b*c==E(bc)
assert b*X+c*Y==E(V)
assert b*p*X+c*q*Y==E(W1)
r=X-a*p-c*E(t);s=Y-a*q-b*E(t)
rows=[[E(),E(),p,q],[E(),E(A1),r,s],
      [p,r,E(),E(t)],[q,s,E(t),E()]]
one=[E(1),E(),E(1),E(1)]
def va(v,z):return [a+b for a,b in zip(v,z)]
def vs(h,v):return [h*a for a in v]
def vm(v,z):
 return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return a*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d);Kd=DK(d)
assert d==[E(u),E(2*f-V-(1-ell)*u),X,Y]
assert F2==E(2*f)
def mean(j):
 sq=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
 return sq-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
E0=mean(0);E1=mean(1);EB=mean(2);EC=mean(3)
assert not E0 and not E1.b and EC==EB.conj()
# Full singleton expression checks 2*p*r, never r*r.
EB_direct=(a*p*p+2*p*r+c*E(t*t)
 -2*(a*p*E(u)+p*d[1]+r*E(u)+c*E(t)*Y)-2*X*X+4*E(f)*X)
assert EB==EB_direct

def N4(v):
 return (2*tau(vm(d,vm(v,v)))-F2*tau(vm(v,v))
   -4*tau(v)*tau(vm(d,v))+2*F2*tau(v)**2+tau(vm(v,DK(v))))
v0=rows[0];v1=rows[1]
Npolar=N4(va(v0,v1))-N4(v0)-N4(v1)
v0c=va(v0,vs(-tau(v0),one));v1c=va(v1,vs(-tau(v1),one))
Pjet=3*tau(vm(vm(v0c,v0c),v1c))
w=lam-1-T
assert N4(v0)==E(2*lam*P02)
assert Pjet==E(3*w*P02)
N1=Npolar-E(4*lam*w*P02)
assert not N1.b
original=[E1.a,EB.a,EB.b,N1.a]
assert all(geomdegree(v)<=2 for v in original)
for v in original:ck(v)

statistics.update(newMonicFDivisionProducts=0,newSixSourceCoefficientReturns=0,
                  newElevenSourceCoefficientReturns=0)
# This is the fixed OLD mathematical G36 definition, not a new output cache.
# Original source blob c489948be8e967575417a1e21de51cd5a915dc80,
# SHA256 3ec9b206da1dbde4103ebf7633e725e4cf5b8518055ac8f0945d7ba6a1e24a22.
# Entire original paid theorem:
# R150-appendix-unit211-W-G36-entire-original-exclusion-and-global-F-recovery.md
G36p=4096+9216*kp+7680*kp**2+3072*kp**3+592*kp**4+24*kp**5-10*kp**6-1*kp**7-6144*ep*kp-16128*ep*kp**2-14336*ep*kp**3-6048*ep*kp**4-1416*ep*kp**5-186*ep*kp**6-9*ep*kp**7+512*ep**2*kp**2+6016*ep**2*kp**3+6560*ep**2*kp**4+2528*ep**2*kp**5+468*ep**2*kp**6+50*ep**2*kp**7+2*ep**2*kp**8+1792*ep**3*kp**3+832*ep**3*kp**4-832*ep**3*kp**5-392*ep**3*kp**6-50*ep**3*kp**7-2*ep**3*kp**8-256*ep**4*kp**4-544*ep**4*kp**5-24*ep**4*kp**6+24*ep**4*kp**7+4*ep**4*kp**8-192*ep**5*kp**5-8*ep**5*kp**7+32*ep**6*kp**6
assert profile(G36p)['sha256']=='994fe0821fb8c70e7f82edf8aea19a17ee1ffa99fd5fd4b5b3c065daea84ad78'
paid_atoms += [('whole_J_equals_Q_two_e_plus_one',2*ep+1),
               ('whole_original_G36',G36p)]
# (J-Q)*Vbar=-2e^2*k*(2e+1), same old W domain.
assert (J-Q)*Vbar==-2*e*e*k*(2*e+1)

# Necessary old qf/three remainders/head DEFINITIONS only. No old f-multiple
# generation, old six scalar gate, or old head factorization is repeated.
cf=bc/(2*u*(u-beta))
qtag=[R(),cf,cf*ell*delta/m,R()]
qf=sum((qtag[i]*original[i] for i in range(4)),R())
q0=fc(qf,0);q1=fc(qf,1)
assert qf==f*f+q1*f+q0
rowdata=[]
for j in (0,2,3):
 hh=fc(original[j],2)
 rr=original[j]-hh*qf
 aa=fc(rr,0);bb=fc(rr,1)
 assert rr==aa+bb*f and geomdegree(aa)<=2 and geomdegree(bb)<=1
 tt=[(R(1) if i==j else R())-hh*qtag[i] for i in range(4)]
 rowdata.append(dict(A=aa,B=bb,value=rr,tag=tt,originalIndex=j))
Bmatrix=[]
for rr in rowdata:
 bb=rr['B'];co=[]
 for dl,dT in [(0,0),(1,0),(0,1)]:
  pp=ctx.from_dict({(int(ex[0]),int(ex[1]),0,0,0):cc
       for ex,cc in bb.n.to_dict().items()
       if int(ex[2])==dl and int(ex[3])==dT and int(ex[4])==0})
  co.append(R(pp,bb.d))
 assert bb==co[0]+co[1]*lam+co[2]*T
 Bmatrix.append(co)
mu=[Bmatrix[1][1]*Bmatrix[2][2]-Bmatrix[1][2]*Bmatrix[2][1],
    Bmatrix[2][1]*Bmatrix[0][2]-Bmatrix[2][2]*Bmatrix[0][1],
    Bmatrix[0][1]*Bmatrix[1][2]-Bmatrix[0][2]*Bmatrix[1][1]]
hh=sum((mu[i]*Bmatrix[i][0] for i in range(3)),R())
aa=sum((mu[i]*rowdata[i]['A'] for i in range(3)),R())
assert hh and weight(hh.n)
ck(hh);ck(aa)
# hh may contain a common factor removed from ALL old source multipliers.
# Work as rational functions, cancel exactly, then check the FINAL g/rtag
# denominators as old paid weights and return the whole identity. No
# physical hh!=0 condition is imposed.
g=ck(aa/hh)
rline=f+g
rtag=[ck(sum((mu[i]*rowdata[i]['tag'][j] for i in range(3)),R())/hh)
      for j in range(4)]
assert geomdegree(g)<=2
assert sum((rtag[i]*original[i] for i in range(4)),R())==rline
say('new_whole_W_same_f_input_ready',
    gNumerator=profile(g.n),gDenominator=profile(g.d),
    originalMeanNames=['E1','EBe','EBo','N1'],
    allFinalGAndOriginalMultiplierDenominatorsOldPaid=True,
    possibleRawCommonHeadZeroRetainedByFullOriginalReturn=True,
    noOldHeadFactorizationOrSixScalarGateReplayed=True,
    trueGramE1StillIndependent=True)

def P2(vv):
 vc=va(vv,vs(-tau(vv),one))
 return tau(vm(vm(vc,vc),vc))
A_lambda=2*lam*lam-2*lam+1
B_lambda=4*lam**3-6*lam*lam+3*lam-1
NB=N4(rows[2]);NC=N4(rows[3])
PB=P2(rows[2]);PC=P2(rows[3])
assert NC==NB.conj() and PC==PB.conj()
NSext=b*NB+c*NC-E(2*lam*P02*(ell+2*T+A_lambda))
PSext=b*PB+c*PC-E(P02*(ell+3*T+3*A_lambda+B_lambda))
assert not NSext.b and not PSext.b
NS=ck(NSext.a);PS=ck(PSext.a)
assert geomdegree(NS)<=3 and geomdegree(PS)<=3
assert geomdegree(NB.b)<=3 and geomdegree(PB.b)<=3
original6=original+[NS,PS]
say('new_true_full_weighted_and_individual_NP_constructed',
    names=['NS','PS','N4B_rho_odd','P2B_rho_odd'],
    profiles=[profile(v.n) for v in [NS,PS,NB.b,PB.b]],
    allConjugateAndWeightedOddPartsReturned=True,
    fullRawCubicDegreeAtMostThree=True)

def monic_f_divide(value,label):
 value=R(value);rem=value;quot=R()
 while fdeg(rem)>=2:
  jj=fdeg(rem)
  term=fc(rem,jj)*f**(jj-2)
  oldrem=rem
  rem=rem-term*qf;quot=quot+term
  assert oldrem==term*qf+rem and fdeg(rem)<jj
  statistics['newMonicFDivisionProducts']+=1
 assert value==quot*qf+rem and fdeg(rem)<=1
 av=fc(rem,0);bv=fc(rem,1)
 assert rem==av+bv*f
 for vv in [value,quot,av,bv]:ck(vv)
 pure=ck(av-bv*g)
 assert fdeg(pure)<=0
 # Complete exact forward identity; reverse follows by rearranging.
 assert value==quot*qf+bv*rline+pure
 return dict(label=label,value=value,quot=quot,A=av,B=bv,pure=pure)

def return_original(value,tag,gens,label):
 assert len(tag)==len(gens)
 back=sum((tag[j]*gens[j] for j in range(len(gens))),R())
 assert back==value
 for jj in range(max(fdeg(back),fdeg(value),0)+1):
  assert fc(back,jj)==fc(value,jj)
  key='newSixSourceCoefficientReturns' if len(gens)==6 else 'newElevenSourceCoefficientReturns'
  statistics[key]+=1
 for vv in [value]+tag:ck(vv)
 return dict(label=label,numerator=profile(value.n),
             denominator=profile(value.d),geometryDegree=geomdegree(value),
             fullOriginalSources=len(gens),allFCoefficientsReturned=True)

qtag6=qtag+[R(),R()];rtag6=rtag+[R(),R()]
pure6=[];trace6=[];pureprofiles=[]
P0=ck(g*g-q1*g+q0)
tag0=[qtag6[j]-(f+q1-g)*rtag6[j] for j in range(6)]
assert geomdegree(P0)<=4
pureprofiles.append(return_original(P0,tag0,original6,'qf_at_same_f'))
pure6.append(P0);trace6.append(tag0)
for ii,rr in enumerate(rowdata):
 value=ck(rr['A']-rr['B']*g)
 tag=[(rr['tag']+[R(),R()])[j]-rr['B']*rtag6[j] for j in range(6)]
 assert geomdegree(value)<=3
 pureprofiles.append(return_original(value,tag,original6,'mean_'+str(ii)))
 pure6.append(value);trace6.append(tag)
divNP=[]
for jj,(label,value) in enumerate([('NS',NS),('PS',PS)]):
 ddv=monic_f_divide(value,label)
 assert geomdegree(ddv['A'])<=3 and geomdegree(ddv['B'])<=2
 assert geomdegree(ddv['pure'])<=4
 tag=[R(int(j==4+jj))-ddv['quot']*qtag6[j]-ddv['B']*rtag6[j]
      for j in range(6)]
 pureprofiles.append(return_original(ddv['pure'],tag,original6,label+'_pure'))
 pure6.append(ddv['pure']);trace6.append(tag);divNP.append(ddv)
 reverse=(ddv['quot']*(f+q1-g)+ddv['B'])*rline+ddv['quot']*P0+ddv['pure']
 assert reverse==value
 say('new_same_f_full_weighted_NP_pure_return',label=label,
     pure=pureprofiles[-1],
     monicDivisionQuotient=profile(ddv['quot'].n),
     originalRemainderA=profile(ddv['A'].n),
     originalRemainderB=profile(ddv['B'].n),
     completeSixSourceForwardAndReverseReturned=True)
assert len(pure6)==6
say('new_exact_whole_W_I6_six_pure_lambda_T_conditions',
    pureProfiles=pureprofiles,
    exactIdeal='I6=(f+g,P0,P1,P2,P3,PN,PP)',
    oneSameFForAllOriginalConditions=True,
    noPolynomialQuotientFreenessAssumed=True,
    noNewLambdaTHeadOrDInverse=True)

# Entire pure C4/R6/N5 are published original value generators.
# R150-appendix-unit211-W-pure-lambda-T-six-four-five-entire-value-equivalence.md
# R150-appendix-unit211-W-pure-weight-f-head-exact-lambda-T-original-ideal.md
D=ell*A_lambda-T*T
K=ell*ell*B_lambda-3*ell*A_lambda*T+2*T**3
c_lambda=3-2*lam
Astar=4*u*Q-J
Cstar=Astar*m*m+J*delta*ell*ell
ad=(M*ell*ell*Q*(3-4*lam)+M*Astar*T*T
    +2*M*u*Q*c_lambda*ell*T+D*Cstar)
bzero=2*m*(Astar*T+u*Q*c_lambda*ell)
bd=M*bzero
C4=ck(2*m*D*ad+K*bd)
R6=ck(M*K*K-4*m*m*D**3)
tstar=-Pc/(bc*Q*Phi)
Vstar=-G/Q-Pc/(Q*Phi)
Wstar=T0/2
xstar=(theta*Vstar-m*Wstar)/M
ystar=(ell*Wstar-u*Vstar)/M
A1star=2*G/Q
z1star=-2*(ell*c_lambda+2*T)*ystar-2*ell*w+m*T*tstar/delta
z2star=2*(ell*xstar-m*ystar-bc*tstar)
Z0star=(ell*ell*A1star+2*ell*u*w*(ell*c_lambda+T)
       +2*Vstar*(ell*ell+ell*c_lambda*T+T*T)
       +2*bc*tstar*(T*T-ell*ell))
Nfive=ck(2*m*D*(Z0star+D*z2star)+M*K*z1star)
assert fdeg(C4)<=0 and geomdegree(C4)<=4
assert fdeg(R6)<=0 and geomdegree(R6)<=6
assert fdeg(Nfive)<=0 and geomdegree(Nfive)<=5
A0=1+T/ell
Nadd=2*lam*P02*(K*A0/m+2*m*D*D/(ell*M))
Padd=P02*(K/(2*m)*(3*A0*A0+(3*m*m/(ell*ell)+delta)*D/M)
           +6*A0*m*D*D/(ell*M))
Nlow=ck(D*NB.b+Nadd)
Plow=ck(D*PB.b+Padd)
original11=original6+[C4,R6,Nlow,Plow,Nfive]
# In this exact auxiliary ideal, qT4 differs from C4 only by a paid
# weight scale, and 2m ell^2 Vlow=Nfive+(2f/(MQ))*C4.
# This identity does NOT invert D; equivalence to physical original values
# retains the previously stated D!=0 domain.
rtag11=rtag+[R() for _ in range(7)]
qtag11=qtag+[R() for _ in range(7)]
pure11=pure6+[C4,R6]
for jj,(label,rawodd,addition,originalindex) in enumerate([
      ('Nlow',NB.b,Nadd,8),('Plow',PB.b,Padd,9)]):
 ddv=monic_f_divide(rawodd,label+'_raw_odd')
 assert geomdegree(ddv['A'])<=3 and geomdegree(ddv['B'])<=2
 value=ck(D*ddv['pure']+addition)
 tag=[R(int(i==originalindex))-D*ddv['quot']*qtag11[i]
      -D*ddv['B']*rtag11[i] for i in range(11)]
 assert fdeg(value)<=0 and geomdegree(value)<=6
 pp=return_original(value,tag,original11,label+'_pure')
 assert original11[originalindex]==D*ddv['quot']*qf+D*ddv['B']*rline+value
 pure11.append(value)
 say('new_same_f_full_individual_odd_NP_pure_return',
     label=label,pure=pp,rawOddRemainderA=profile(ddv['A'].n),
     rawOddRemainderB=profile(ddv['B'].n),
     allElevenOriginalSourceCoefficientsReturned=True,
     completeForwardAndReverseReturned=True,
     physicalDOnlyMultipliedNeverInverted=True)
pure11.append(Nfive)
assert len(pure11)==11
assert all(fdeg(v)<=0 for v in pure11)
say('new_complete_whole_W_same_f_pure_I11',
    names=['P0','P1','P2','P3','PN','PP','C4','R6','Nlow','Plow','N5'],
    numerators=[profile(v.n) for v in pure11],
    denominators=[profile(v.d) for v in pure11],
    exactOriginalIdeal='I11=(f+g,eleven displayed pure lambda,T conditions)',
    entireVlowReplacedByPublishedExactN5AndC4Identity=True,
    weightedAndIndividualNPBothRetained=True,
    noD_bzero_Lambda_T_HeadOrNormInverse=True,
    geometryEnvironmentNotAssumedFree=True,
    noNecessaryPairListCalledSufficient=True,
    statistics=statistics,distinctPaidWeightDenominators=len(den_seen),
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    noLargeCoefficientCacheWritten=True,
    noOldScalarOrNormOrNativeActionGateReplayed=True,
    noNewFiniteWeightOrPointBound=True,
    wholeWExcluded=False,ordinaryISPClaim=False,
    maxRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)
