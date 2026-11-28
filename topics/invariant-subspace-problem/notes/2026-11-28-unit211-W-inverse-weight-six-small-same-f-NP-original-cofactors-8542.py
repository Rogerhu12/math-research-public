#!/usr/bin/env python3
"""NEW whole W: inverse-slope WEIGHTS, FREE T, six small N/P cofactors.
The coordinates nu=beta/u are globally inverse on CURRENT paid W.
No b0 assumption; nu+2/Astar is NEVER inverted.
Only TRUE Gram, monic qf and three f-linear remainder DEFINITIONS.
No old b1 six scalar gate, full c0 eleven-row gate, f-head/factor,
adjugate-five-cubic, entire-b0 projections or frozen PRS is replayed.
Each raw NS/PS gives A_F+B_F*f modulo monic qf; the NEW six
H_Fi=A_F*B_i-A_i*B_F are fully returned to all SIX original sources.
Only the common factor of ALL actual source multipliers is cancelled,
with another full original return: its zero set is retained.
The published pure-weight unit sum(v_i B_i)=1 gives exact I6 after
adding these six to the existing exact six-scalar I4 presentation.
180 seconds /4 GiB, self-contained. No coefficient cache, encoded
payload, resultant, factor, geometry-head inverse or sampling gate.
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
ctx=fmpq_mpoly_ctx.get(('u','nu','lam','T','f'),'lex')
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

# New whole current-W birational weight coordinates nu=beta/u.
u,nu,lam,T,f=map(R,(ep,kp,lp,tp,fp))
e=u-1;slope_unit=2*u-1
dweight=u*nu-slope_unit;rweight=slope_unit-nu
k=2*rweight/dweight
Vbar=u*k+2;Q=e*k;delta=1-Q
Hweight=nu*nu-(u+1)*nu+slope_unit
ell=u*Hweight/rweight
m=u-ell;theta=u-ell*Q;V2=2*u-ell*Q
M=ell*V2-u*u;bc=M/(4*delta)
T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
Phi=T0+4*u-4+Q;Pf=T0*(J-Q)
Pbar=(3*u-2)*nu*nu-(2*u*u+3*u-3)*nu+slope_unit*slope_unit
P02=2*u*e*Pbar/dweight
assert P02==(2-3*u)*V2-Q*u+2*u**3
beta=2*u-J/Q
# These complete forward/inverse identities pay dweight/rweight through
# OLD physical units, not by deleting a new weight chart.
assert ell==u*((k+2)**2-2*e*k)/(k*Vbar)
assert nu==slope_unit*(k+2)/Vbar
assert dweight==2*slope_unit*e/Vbar
assert rweight==slope_unit*e*k/Vbar
assert Q==2*e*rweight/dweight
assert m==u*nu*(u-nu)/rweight
assert beta==u*nu
assert Phi==-2*e*(nu-1)
assert J-Q==-2*e*rweight
assert T0==-2*u*e*nu*(nu-1)/dweight
assert delta==(nu*(3*u-2)-slope_unit*slope_unit)/dweight
assert M==ell*ell*delta-m*m
assert J*Phi-Pf==2*u*Q*Phi
assert u-beta==u*(1-nu)
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
  'degrees_u_nu_lambda_T_f':list(map(int,p.degrees())) if p else [-1]*5,
  'totalDegree':int(p.total_degree()) if p else -1,'terms':len(data),
  'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
# Fixed OLD 36-term original G36 definition. Only its new rational
# pullback is used; no old whole-G36 exclusion gate or factor is replayed.
# Source c489948be8e967575417a1e21de51cd5a915dc80 and published whole
# R150-appendix-unit211-W-G36-entire-original-exclusion-and-global-F-recovery.md.
GDATA=[[0,0,"4096"],[0,1,"9216"],[0,2,"7680"],[0,3,"3072"],[0,4,"592"],[0,5,"24"],[0,6,"-10"],[0,7,"-1"],[1,1,"-6144"],[1,2,"-16128"],[1,3,"-14336"],[1,4,"-6048"],[1,5,"-1416"],[1,6,"-186"],[1,7,"-9"],[2,2,"512"],[2,3,"6016"],[2,4,"6560"],[2,5,"2528"],[2,6,"468"],[2,7,"50"],[2,8,"2"],[3,3,"1792"],[3,4,"832"],[3,5,"-832"],[3,6,"-392"],[3,7,"-50"],[3,8,"-2"],[4,4,"-256"],[4,5,"-544"],[4,6,"-24"],[4,7,"24"],[4,8,"4"],[5,5,"-192"],[5,7,"-8"],[6,6,"32"]]
G36_original_definition=ctx.from_dict({(i,j,0,0,0):int(cc) for i,j,cc in GDATA})
assert len(GDATA)==36
assert profile(G36_original_definition)['sha256']=='994fe0821fb8c70e7f82edf8aea19a17ee1ffa99fd5fd4b5b3c065daea84ad78'
G36_pullback=sum((R(int(cc))*e**i*k**j for i,j,cc in GDATA),R())
G36_clear=sum((int(cc)*(ep-1)**i*(2*rweight.n)**j*dweight.n**(8-j)
              for i,j,cc in GDATA),Z)
assert G36_pullback*R(dweight.n**8)==R(G36_clear)
assert weight(G36_pullback.n) and weight(G36_pullback.d)

# Only the currently proved pure-weight W supports. Neither E1=EW,
# nor any new lambda,T,f head nor D is assumed.
paid_atoms=[
 ('original_u',ep),('original_e',ep-1),
 ('original_JQ_two_u_minus_one',2*ep-1),
 ('inverse_coordinate_d',dweight.n),('inverse_coordinate_r',rweight.n),
 ('original_equal_weights_k_plus_two_nu',kp),
 ('original_Phi_nu_minus_one',kp-1),
 ('original_delta',delta.n),('original_M',M.n),
 ('original_ell',ell.n),('original_m',m.n),('original_P02',P02.n),
 ('whole_original_Lhalf',(2*ell-1).n),
 ('whole_original_G36_pullback',G36_pullback.n)]
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
for v in [u,nu,e,slope_unit,dweight,rweight,k,Q,Vbar,delta,ell,m,M,bc,Phi,P02,G36_pullback,t,V,W1,x,y,A1]:
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

statistics.update(newNPMonicDivisionProducts=0,newOriginalSixSourceReturns=0,
 newOriginalFCoefficientReturns=0,newSixMultiplierCommonCancellations=0)
def shortdivide_original(value):
 rem=R(value);quot=R()
 while fdeg(rem)>=2:
  degree=fdeg(rem)
  term=fc(rem,degree)*f**(degree-2)
  old=rem;rem=rem-term*qf;quot=quot+term
  assert old==term*qf+rem and fdeg(rem)<degree
  statistics['newNPMonicDivisionProducts']+=1
 av=fc(rem,0);bv=fc(rem,1)
 assert value==quot*qf+av+bv*f
 assert geomdegree(av)<=3 and geomdegree(bv)<=2
 for vv in [quot,av,bv]:ck(vv)
 return quot,av,bv
def return_full(value,tag):
 assert len(tag)==6
 back=sum((tag[j]*original6[j] for j in range(6)),R())
 assert back==value
 for jj in range(max(fdeg(value),fdeg(back),0)+1):
  assert fc(back,jj)==fc(value,jj)
  statistics['newOriginalFCoefficientReturns']+=1
 for vv in [value]+tag:ck(vv)
 statistics['newOriginalSixSourceReturns']+=1
def primitive_cofactor(label,value,tag):
 return_full(value,tag)
 assert fdeg(value)<=0 and geomdegree(value)<=4
 denominator=O
 for vv in tag:
  denominator=exact(denominator,denominator.gcd(vv.d))*vv.d
 paid(denominator)
 numerators=[vv.n*exact(denominator,vv.d) for vv in tag]
 common=Z
 for pp in numerators:common=common.gcd(pp)
 if not common:
  assert not value
  say('new_same_f_small_NP_cofactor_zero',label=label,
      exactOriginalI6StillRetainsAllOtherRows=True)
  return dict(label=label,value=R(),tag=[R() for _ in range(6)])
 primitive=[R(exact(pp,common)) for pp in numerators]
 returned=sum((primitive[j]*original6[j] for j in range(6)),R())
 assert R(common)*returned==R(denominator)*value
 return_full(returned,primitive)
 assert fdeg(returned)<=0 and geomdegree(returned)<=4
 core,removed,hist=strip(returned.n)
 if core:
  scale=core.coefficient(0);core/=scale;removed*=scale
 assert core*removed==returned.n
 if not core:
  assert not returned
  return dict(label=label,value=R(),tag=primitive)
 paid(removed)
 finaltag=[R(returned.d,removed)*vv for vv in primitive]
 final=R(core)
 return_full(final,finaltag)
 statistics['newSixMultiplierCommonCancellations']+=1
 say('new_same_f_small_NP_original_cofactor_complete',
     label=label,retainedNecessaryPolynomial=profile(core),
     geometryDegree=geomdegree(final),
     actualSixMultiplierCommon=profile(common),
     onlyOldPaidWeightSupportRemoved=hist,
     finalSixOriginalMultiplierNumerators=[profile(vv.n) for vv in finaltag],
     finalSixOriginalMultiplierDenominators=[profile(vv.d) for vv in finaltag],
     allSixOriginalCoefficientsAndEveryFCoefficientReturned=True,
     noUnpaidEquationOrHeadDivided=True,
     completeCommonContentZeroLocusRetained=True,
     rawValueTimesOriginalPaidDenominatorEqualsPolynomialTimesNewCore=True)
 return dict(label=label,value=final,tag=finaltag)
say('new_same_f_small_NP_input_definitions_ready',
    trueIndependentE1=True,
    weightCoordinates=['u','nu=beta/u'],
    allForwardInverseWeightIdentitiesReturned=True,
    originalPureWeightP02CompactIdentityReturned=True,
    oldG36DefinitionSHAAndFullNewWeightPullbackReturned=True,
    TIsFreeAndBzeroNotImposed=True,
    nuPlusTwoOrAstarNeverInverted=True,
    rawOriginalNSPSProfiles=[profile(v.n) for v in [NS,PS]],
    oldSixNormPairsAndGHeadMatrixAndFullI11NotRun=True,
    noGOrInverseRawHeadConstructed=True)
new_conditions=[]
for originalindex,(label,value) in enumerate([('NS',NS),('PS',PS)],4):
 quotient,av,bv=shortdivide_original(value)
 say('new_raw_NP_monic_F_remainder_definitions',
     label=label,constantRemainder=profile(av.n),
     linearRemainder=profile(bv.n),
     originalDivisionWholeProductReturned=True)
 for ii,rr in enumerate(rowdata):
  hi=av*rr['B']-rr['A']*bv
  tag=[]
  for jj in range(6):
   entry=rr['B']*int(jj==originalindex)
   if jj<4:
    entry=entry-rr['B']*quotient*qtag[jj]-bv*rr['tag'][jj]
   tag.append(entry)
  assert hi==rr['B']*(value-quotient*qf)-bv*rr['value']
  item=primitive_cofactor(label+'_row_'+str(ii+1),hi,tag)
  new_conditions.append(item)
assert len(new_conditions)==6
say('new_six_same_f_small_NP_original_conditions_complete',
    names=[item['label'] for item in new_conditions],
    profiles=[profile(item['value'].n) for item in new_conditions],
    geometryDegrees=[geomdegree(item['value']) for item in new_conditions],
    exactPublishedI4SixScalarsRetained=True,
    exactI6UsesPublishedPureWeightUnitCombinationOfThreeB=True,
    originalIdentity='sum(v_i H_Fi)=A_F-g B_F; H_Fi=B_i P_F-B_F P_i',
    noNewB_iOrRawWeightHeadOrGeometryInverse=True,
    entireOriginalI11ConditionsStillRetained=True,
    noNewWeightProjectionOrEmptyConclusion=True,
    noOldProofGateReplayed=True,
    distinctPaidWeightDenominators=len(den_seen),
    statistics=statistics,
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    maxRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    noLargeCoefficientCacheWritten=True,ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0)
