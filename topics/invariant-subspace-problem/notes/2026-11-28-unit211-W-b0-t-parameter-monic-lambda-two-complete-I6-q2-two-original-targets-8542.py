#!/usr/bin/env python3
"""NEW whole W/b0: original t parameter, monic lambda TWO, full I6.
No new geometric or weight head is inverted. The fixed-t (f,V) true
mean head 32*u*Q*(2*ell-1)/M^2 is already paid on the current W chart.
Its actual pure-weight inverse gives the monic lambda quadratic after
the exact b0 affine substitution, including the full W Phi term.
Keep all SIX original equations and the b0 necessary original q2.
Return the full twelve/two I6 presentation, then fourteen/two J7.
Only TWO genuinely new same-lambda original targets are constructed:
q2 with N1, and q2 with NS, of t-degree at most 3 and 4.
Only a common factor of ALL seven actual original multipliers may be
cancelled; every resulting complete polynomial identity is returned.
All new t leading zeros remain. No old qf/head/resultant/PRS, cross
gcd, 4x5 recovery, C2/Loww target or old large action gate is replayed.
Self-contained, zero dependencies. 180 seconds / 4 GiB; one first run.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq_mpoly_ctx
START=time.perf_counter();DEADLINE=START+180
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
signal.setitimer(signal.ITIMER_REAL,180)
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('fixed original 180-second deadline')
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(',',':')),flush=True)
ctx=fmpq_mpoly_ctx.get(('u','nu','lambda','t'),'lex')
up,nup,lp,tp=ctx.gens();O=ctx.constant(1);Z=ctx.constant(0)
def polynomial(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=polynomial(n);d=O if d is None else polynomial(d);assert d
  if not n:self.n=Z;self.d=O;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
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
u,nu,lam,t=map(R,(up,nup,lp,tp))
e=u-1;s=2*u-1;dc=u*nu-s;rc=s-nu
k=2*rc/dc;Q=2*e*rc/dc
ell=u*(nu*nu-(u+1)*nu+s)/rc
m=u-ell;delta=1-Q
M=ell*(2*u-ell*Q)-u*u;bc=M/(4*delta)
T0=2*u-ell*Q-2*u*u;J=2*u*(1-u)+ell*Q
Phi=T0+4*u-4+Q
P02=(2-3*u)*(2*u-ell*Q)-Q*u+2*u**3
Pf=T0*(J-Q);Astar=4*u*Q-J
kap=u*Q*ell/Astar
T=kap*(2*lam-3)
f=(P02*(T0-2*kap*Q)*lam+e*T0*T0
   -Q*P02*(ell-3*kap)-bc*Q*Phi*t)/Pf
V=(J*f-lam*P02-e*T0+bc*Q*t)/Q
W1=T0/2+2*u*f
theta=u-ell*Q
x=(theta*V-m*W1)/M;y=(ell*W1-u*V)/M
A1=2*f-2*V+2*bc*t
A2=2*lam*lam-2*lam+1
B3=4*lam**3-6*lam*lam+3*lam-1
wv=lam-1-T
Dval=ell*A2-T*T
statistics={'exactPolynomialDivisionProducts':0,'paidDenominators':0,
 'newCoordinateReturns':0,'newMeanHeadCoordinates':0,
 'newMonicOriginalCoordinates':0,'newRawMomentReturns':0,
 'newFullReductionReturns':0,'newTwoCoordinateRows':0,
 'newOriginalCofactorReturns':0}
def exact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 statistics['exactPolynomialDivisionProducts']+=1;return q
def weight(p):return all(not int(ex[2]) and not int(ex[3]) for ex in p.to_dict())
paid_values=[
 ('original_u',u),('original_u_minus_one',e),('inverse_coordinate_s',s),
 ('inverse_coordinate_d',dc),('inverse_coordinate_r',rc),
 ('inverse_coordinate_nu',nu),('inverse_coordinate_nu_minus_one',nu-1),
 ('original_Q',Q),('original_delta',delta),('original_bc',bc),
 ('original_M',M),('original_ell',ell),('original_m',m),
 ('original_P02',P02),('original_Pf',Pf),('original_Phi',Phi),
 ('b0_original_Astar',Astar),('whole_W_ell_half_excluded',2*ell-1)]
paid_atoms=[]
for label,value in paid_values:
 assert value and weight(value.n) and weight(value.d)
 paid_atoms.append((label,value.n))
def strip_paid(poly):
 if not poly:return Z,O,[]
 original=poly;removed=O;hist=[]
 for name,atom in paid_atoms:
  layers=0
  while int(poly.total_degree())>0:
   g=poly.gcd(atom)
   if int(g.total_degree())==0:break
   poly=exact(poly,g);removed*=g;layers+=1
  if layers:hist.append({'support':name,'gcdLayers':layers})
 assert removed*poly==original
 return poly,removed,hist
den_cache=set()
def ck(v):
 v=R(v);assert weight(v.d)
 key=str(v.d)
 if key not in den_cache:
  rem,_,_=strip_paid(v.d)
  assert rem and int(rem.total_degree())==0,('unpaid denominator',str(rem))
  den_cache.add(key);statistics['paidDenominators']+=1
 return v
def lc(v,j):
 v=ck(v)
 return R(ctx.from_dict({(ex[0],ex[1],0,ex[3]):cc
   for ex,cc in v.n.to_dict().items() if int(ex[2])==j}),v.d)
def ldegree(v):
 v=ck(v);return max((int(ex[2]) for ex in v.n.to_dict()),default=-1)
def tdegree(v):
 v=ck(v);return max((int(ex[3]) for ex in v.n.to_dict()),default=-1)
def geomdegree(v):
 v=ck(v);return max((int(ex[2])+int(ex[3]) for ex in v.n.to_dict()),default=-1)
def scalar_t(v):
 v=ck(v);assert not any(int(ex[2]) for ex in v.n.to_dict());return v
def pure_weight(v):
 v=ck(v);assert weight(v.n);return v
def profile(p):
 raw=str(sorted(p.to_dict().items())).encode()
 return {'degrees':list(map(int,p.degrees())) if p else [-1]*4,
  'totalDegree':int(p.total_degree()) if p else -1,
  'terms':len(p.to_dict()),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def rp(v):return {'numerator':profile(v.n),'denominator':profile(v.d)}
for value in [k,Q,ell,m,delta,M,bc,T0,J,Phi,P02,Pf,Astar,kap,T,f,V,W1,x,y,A1]:
 ck(value)
assert Astar==u*Q*(nu+2) and kap==ell/(nu+2)
assert (lam*P02==J*f-Q*V+bc*Q*t-e*T0)
assert T==-ell+(T0*(f-V)+bc*(T0-Phi)*t)/P02
assert Pf*f+Q*P02*(ell+T)-(lam*P02+e*T0)*T0+bc*Q*Phi*t==R()
assert 2*m*(Astar*T+u*Q*(3-2*lam)*ell)==R()
assert geomdegree(f)<=1 and geomdegree(V)<=1
# The exact coefficient, with no derivative API or new slope test.
ft=R(ctx.from_dict({(ex[0],ex[1],0,0):cc
  for ex,cc in f.n.to_dict().items() if not ex[2] and int(ex[3])==1}),f.d)
assert ft==-bc*Q*Phi/Pf
statistics['newCoordinateReturns']+=7
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
b=E(ell/2,m/(2*delta));c=b.conj();aw=E(1-ell)
p=E(1,1);q=p.conj();X=E(x,y);Y=X.conj()
rr=X-aw*p-c*E(t);ss=Y-aw*q-b*E(t)
rows=[[E(),E(),p,q],[E(),E(A1),rr,ss],
      [p,rr,E(),E(t)],[q,ss,E(t),E()]]
one=[E(1),E(),E(1),E(1)]
def va(v,w):return [v[i]+w[i] for i in range(4)]
def vs(a,v):return [a*x for x in v]
def vm(v,w):
 return [v[0]*w[0],v[0]*w[1]+v[1]*w[0],v[2]*w[2],v[3]*w[3]]
def tr(v):return aw*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tr(vm(row,v)) for row in rows]
dv=DK(one);F2=tr(dv);Kd=DK(dv)
assert b*c==E(bc) and b*X+c*Y==E(V)
assert b*p*X+c*q*Y==E(W1)
assert dv==[E(u),E(2*f-V-(1-ell)*u),X,Y] and F2==E(2*f)
statistics['newCoordinateReturns']+=5
def mean(j):
 sq=2*tr(vm(rows[0],rows[1])) if j==1 else tr(vm(rows[j],rows[j]))
 return sq-2*Kd[j]-2*vm(dv,dv)[j]+2*F2*dv[j]
E0=mean(0);E1E=mean(1);EB=mean(2);EC=mean(3)
assert not E0 and not E1E.b and EC==EB.conj()
E1=E1E.a;EBe=EB.a;EBo=EB.b
Rcal=4*(f-u)*(V-f)+bc*t*t+t*(4*bc*u-ell*V+m*(T0+4*u*f-2*V)/(2*delta))
assert E(2*Rcal)+E1E-b*EB-c*EC==E()
for v in [E1,EBe,EBo,Rcal]:assert geomdegree(v)<=2
statistics['newRawMomentReturns']+=4
# Derive the actual fixed-t f,V head from their true X/Y linear parts.
Xf=E(-2*m*u/M,2*ell*u/M)
XV=E(theta/M,-u/M)
assert b*Xf+c*Xf.conj()==E()
assert b*XV+c*XV.conj()==E(1)
assert b*p*Xf+c*q*Xf.conj()==E(2*u)
assert b*p*XV+c*q*XV.conj()==E()
HB=[-2*Xf*Xf+4*Xf,-4*Xf*XV+4*XV,-2*XV*XV]
H=[[R(-4),R(4),R()],[v.a for v in HB],[v.b for v in HB]]
def dot(a,b):return sum((v*w for v,w in zip(a,b)),R())
def det3(A):
 return A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])
def adj3(A):
 out=[]
 for i in range(3):
  row=[]
  for j in range(3):
   rr=[a for a in range(3) if a!=j];cc=[a for a in range(3) if a!=i]
   row.append((-1)**(i+j)*(A[rr[0]][cc[0]]*A[rr[1]][cc[1]]-A[rr[0]][cc[1]]*A[rr[1]][cc[0]]))
  out.append(row)
 return out
head=32*u*Q*(2*ell-1)/(M*M)
assert det3(H)==head
Hinv=[[pure_weight(v/head) for v in row] for row in adj3(H)]
for i in range(3):
 for j in range(3):
  assert dot(H[i],[Hinv[k][j] for k in range(3)])==R(int(i==j))
  statistics['newMeanHeadCoordinates']+=1
jf=J/P02;jV=-Q/P02
square_row=[jf*jf,2*jf*jV,jV*jV]
eh=[pure_weight(dot(square_row,[Hinv[i][j] for i in range(3)])) for j in range(3)]
qtag=[-eh[0]/2,eh[0]*ell/2+eh[1],eh[0]*m/2+eh[2]]
qtag=[pure_weight(v) for v in qtag]
mean_original=[E1,EBe,EBo]
ql=ck(dot(qtag,mean_original))
assert ldegree(ql)==2 and lc(ql,2)==R(1)
q0=scalar_t(lc(ql,0));q1=scalar_t(lc(ql,1))
assert ql==lam*lam+q1*lam+q0
assert tdegree(q1)<=1 and tdegree(q0)<=2 and geomdegree(ql)<=2
assert ql==dot(eh,[Rcal,EBe,EBo])
statistics['newMonicOriginalCoordinates']+=3
say('new_whole_b0_t_parameter_monic_lambda_two',
 originalMeanNames=['E1','EBe','EBo'],
 headDefinition='32*u*Q*(2*ell-1)/M^2',headProfile=rp(head),
 exactPureWeightOriginalMultiplierProfiles=[rp(v) for v in qtag],
 qLambdaProfiles=[rp(q0),rp(q1)],qLambdaMonicDegree=2,
 totalLambdaTDegreeUpperBound=2,
 W_PhiCorrectionKept=True,oldLambdaFAndNewLambdaTAffineMapUnit=True,
 noNewWeightOrGeometricHeadInverse=True,noOriginalQuotientFreenessAssumed=True,
 statistics=statistics)
tick()
def N4(v):
 vv=vm(v,v);tv=tr(v)
 return 2*tr(vm(dv,vv))-F2*tr(vv)-4*tv*tr(vm(dv,v))+2*F2*tv*tv+tr(vm(v,DK(v)))
def centered(v):return va(v,vs(-tr(v),one))
def P2(v):
 vc=centered(v);return tr(vm(vm(vc,vc),vc))
N0=N4(rows[0]);Npolar=N4(va(rows[0],rows[1]))-N0-N4(rows[1])
vc0,vc1=centered(rows[0]),centered(rows[1])
Pjet=3*tr(vm(vm(vc0,vc0),vc1))
assert N0==E(2*lam*P02) and Pjet==E(3*wv*P02)
N1E=Npolar-E(4*lam*wv*P02);assert not N1E.b
N1=N1E.a;assert geomdegree(N1)<=2
statistics['newRawMomentReturns']+=3
NB,NC=N4(rows[2]),N4(rows[3])
PB,PC=P2(rows[2]),P2(rows[3])
assert NC==NB.conj() and PC==PB.conj()
NSE=b*NB+c*NC-E(2*lam*P02*(ell+2*T+A2))
PSE=b*PB+c*PC-E(P02*(ell+3*T+3*A2+B3))
assert not NSE.b and not PSE.b
NS,PS=NSE.a,PSE.a
assert geomdegree(NS)<=3 and geomdegree(PS)<=3
statistics['newRawMomentReturns']+=4
# The original b0 necessary q2; its whole leading-zero locus is retained.
Cstar=Astar*m*m+J*delta*ell*ell
ad=M*ell*ell*Q*(3-4*lam)+M*Astar*T*T+2*M*u*Q*(3-2*lam)*ell*T+Dval*Cstar
q2=ck(2*ad/ell)
assert ldegree(q2)<=2 and not any(int(ex[3]) for ex in q2.n.to_dict())
original=mean_original+[N1,NS,PS,q2]
names=['E1','EBe','EBo','N1','NS','PS','b0_original_q2']
full_qtag=qtag+[R(),R(),R(),R()]
assert ql==dot(full_qtag,original)
def divide_monic(value):
 value=ck(value);remainder=value;quotient=R()
 while ldegree(remainder)>=2:
  tick();j=ldegree(remainder)-2;coef=scalar_t(lc(remainder,j+2))
  term=coef*lam**j;old=remainder
  quotient+=term;remainder=ck(remainder-term*ql)
  assert remainder+term*ql==old
 assert value==quotient*ql+remainder
 statistics['newFullReductionReturns']+=1
 return quotient,remainder
base_rows=[];all_rows=[];base_tags=[];all_tags=[]
for idx,value in enumerate(original):
 quotient,remainder=divide_monic(value)
 aa=scalar_t(lc(remainder,0));bb=scalar_t(lc(remainder,1))
 assert remainder==aa+bb*lam
 tag=[R(int(i==idx))-quotient*full_qtag[i] for i in range(7)]
 assert dot(tag,original)==remainder
 bound=3 if idx in (4,5) else 2
 assert tdegree(aa)<=bound and tdegree(bb)<=bound-1
 multiplied=[-q0*bb,aa-q1*bb]
 mtag=[lam*tag[i]-bb*full_qtag[i] for i in range(7)]
 assert dot(mtag,original)==multiplied[0]+multiplied[1]*lam
 assert lam*remainder-(multiplied[0]+multiplied[1]*lam)==bb*ql
 for vv in [aa,bb]+multiplied+tag+mtag:ck(vv)
 base_rows.append([aa,bb]);base_tags.append(tag)
 all_rows.extend([[aa,bb],multiplied]);all_tags.extend([tag,mtag])
 statistics['newFullReductionReturns']+=3
 statistics['newTwoCoordinateRows']+=2
say('new_whole_b0_original_I6_and_q2_t_parameter_two_columns',
 originalNames=names,baseRowProfiles=[[rp(v) for v in row] for row in base_rows],
 originalI4Rows=8,originalI6Rows=12,necessaryJ7Rows=14,columns=2,
 ambient='A_W[t][lambda]/(monic lambda^2+q1(t)*lambda+q0(t))',
 allSevenOriginalDivisionIdentitiesReturned=True,
 allFourteenFullOriginalMultiplierIdentitiesReturned=True,
 I6PresentationExact=True,J7AddsOnlyOriginalNecessaryB0ValueQ2=True,
 originalPhysicalSystemNotDeclaredEquivalentToJ7=True,
 noNewLambdaLeadingInverse=True,noDInverse=True,statistics=statistics)
tick()
def primitive_original_cofactor(idx,jdx,bound):
 ai,bi=base_rows[idx];aj,bj=base_rows[jdx]
 scalar=scalar_t(ai*bj-aj*bi)
 tags=[bj*base_tags[idx][i]-bi*base_tags[jdx][i] for i in range(7)]
 assert dot(tags,original)==scalar
 assert tdegree(scalar)<=bound
 if not scalar:
  say('new_b0_t_scalar_identically_zero',pair=[names[idx],names[jdx]],
      fullSevenOriginalCombinationZeroReturned=True,noNewCover=True)
  return {'pair':[names[idx],names[jdx]],'zero':True}
 scale=O
 for tag in tags:
  ck(tag);scale=exact(scale,scale.gcd(tag.d))*tag.d
 assert weight(scale)
 poly_tags=[tag.n*exact(scale,tag.d) for tag in tags]
 common=Z
 for value in poly_tags:
  if value:common=value if not common else common.gcd(value)
 assert common
 reduced_polys=[exact(value,common) if value else Z for value in poly_tags]
 reduced_tags=[R(v) for v in reduced_polys]
 target=scalar_t(dot(reduced_tags,original))
 assert target*R(common)==scalar*R(scale)
 assert tdegree(target)<=bound
 # Clear only its actual old-paid weight denominator; then only old-paid
 # numerator support may be stripped. No unpaid scalar content is inverted.
 clear=target.d
 final_tags=[R(clear)*v for v in reduced_tags]
 target_poly=target.n
 assert dot(final_tags,original)==R(target_poly)
 retained,removed,hist=strip_paid(target_poly)
 assert retained and not any(int(ex[2]) for ex in retained.to_dict())
 final_tags=[ck(v/R(removed)) for v in final_tags]
 assert dot(final_tags,original)==R(retained)
 statistics['newOriginalCofactorReturns']+=4
 say('new_whole_b0_same_lambda_original_t_cofactor',
     pair=[names[idx],names[jdx]],tDegreeUpperBound=bound,
     rawScalar=rp(scalar),commonOfAllSevenActualMultipliers=profile(common),
     newPureTScalar=profile(retained),oldPaidSupportStripped=hist,
     allSevenOriginalCoordinatesReturned=True,
     allCancelledCommonZeroFibersRetainedByNewOriginalIdentity=True,
     everyNewTHeadZeroFiberRetained=True,
     unpaidContentNotStripped=True,noWeightProjectionOrEmptinessClaim=True,
     statistics=statistics)
 return {'pair':[names[idx],names[jdx]],'zero':False,'scalar':profile(retained)}
new_targets=[
 primitive_original_cofactor(6,3,3),
 primitive_original_cofactor(6,4,4)]
say('new_whole_b0_t_model_two_original_targets_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 targets=new_targets,statistics=statistics,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 noExternalDependencies=True,noOldGateReplayed=True,
 noLargeCoefficientPayloadOrCacheSaved=True,
 wholeBzeroExcluded=False,wholeWExcluded=False,ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0)
