#!/usr/bin/env python3
"""NEW W/b0 (-1,0): eleven complete original initial equations.
This input adds the full R6, Nlow, Plow and Vlow to the seven raw
same-point Gram/q2 definitions.  It recomputes the lower-envelope
partition from ALL ELEVEN equations, including exact t=0.
Fixed p=1009.  On each cell it seeks an original Laurent unit and,
without assuming success, the fixed target powers (k+2)^1..4 and
(2*lambda-3)^1..4.  Every successful target is returned in all eleven
original initial coordinates.  D is never inverted.  No old seven-row
algorithm, cofactor, projection, or old valuation partition is replayed.
180 seconds / 4 GiB; zero dependencies; no coefficient payload/cache.
"""
import hashlib,json,math,resource,signal,time
from fractions import Fraction
from functools import reduce
from pathlib import Path
from flint import fmpq_mpoly_ctx
START=time.perf_counter();DEADLINE=START+180
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
signal.setitimer(signal.ITIMER_REAL,180)
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute first 180-second budget')
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True,separators=(',',':')),flush=True)
P=1009
ctx=fmpq_mpoly_ctx.get(('e','k','lambda','t'),'lex')
ep,kp,lp,tp=ctx.gens();O=ctx.constant(1);Z=ctx.constant(0)
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

e,k,lam,t=map(R,(ep,kp,lp,tp))
u=e+1;Q=e*k;Vbar=u*k+2;delta=1-Q
ell=u*((k+2)**2-2*e*k)/(k*Vbar)
m=u-ell;theta=u-ell*Q;V2=2*u-ell*Q
M=ell*V2-u*u;bc=M/(4*delta)
T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
Phi=T0+4*u-4+Q;Pf=T0*(J-Q)
P02=(2-3*u)*V2-Q*u+2*u**3
Ast=4*u*Q-J;kap=u*Q*ell/Ast
T=kap*(2*lam-3);wv=lam-1-T
f=(P02*(T0-2*kap*Q)*lam+e*T0*T0-Q*P02*(ell-3*kap)
   -bc*Q*Phi*t)/Pf
V=(J*f-lam*P02-e*T0+bc*Q*t)/Q
W1=T0/2+2*u*f
x=(theta*V-m*W1)/M;y=(ell*W1-u*V)/M
A1=2*f-2*V+2*bc*t
A2=2*lam*lam-2*lam+1
B3=4*lam**3-6*lam*lam+3*lam-1
Dval=ell*A2-T*T
# Same original E0/N0/P1 and b0 coordinate definitions, not a chosen root.
assert Pf*f+Q*P02*(ell+T)-(lam*P02+e*T0)*T0+bc*Q*Phi*t==R()
assert Q*V==J*f-lam*P02-e*T0+bc*Q*t
assert 2*m*(Ast*T+u*Q*(3-2*lam)*ell)==R()
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
assert dv==[E(u),E(2*f-V-(1-ell)*u),X,Y] and F2==E(2*f)
def mean(j):
 sq=2*tr(vm(rows[0],rows[1])) if j==1 else tr(vm(rows[j],rows[j]))
 return sq-2*Kd[j]-2*vm(dv,dv)[j]+2*F2*dv[j]
E0=mean(0);E1E=mean(1);EB=mean(2);EC=mean(3)
assert not E0 and not E1E.b and EC==EB.conj()
E1,EBe,EBo=E1E.a,EB.a,EB.b
def N4(v):
 vv=vm(v,v);tv=tr(v)
 return 2*tr(vm(dv,vv))-F2*tr(vv)-4*tv*tr(vm(dv,v))+2*F2*tv*tv+tr(vm(v,DK(v)))
def centered(v):return va(v,vs(-tr(v),one))
def P2(v):
 vc=centered(v);return tr(vm(vm(vc,vc),vc))
N1E=N4(va(rows[0],rows[1]))-N4(rows[0])-N4(rows[1])-E(4*lam*wv*P02)
NB,NC=N4(rows[2]),N4(rows[3])
PB,PC=P2(rows[2]),P2(rows[3])
NSE=b*NB+c*NC-E(2*lam*P02*(ell+2*T+A2))
PSE=b*PB+c*PC-E(P02*(ell+3*T+3*A2+B3))
assert not N1E.b and not NSE.b and not PSE.b
N1,NS,PS=N1E.a,NSE.a,PSE.a
Cst=Ast*m*m+J*delta*ell*ell
ad=M*ell*ell*Q*(3-4*lam)+M*Ast*T*T+2*M*u*Q*(3-2*lam)*ell*T+Dval*Cst
q2=2*ad/ell

# Four NEW complete original value inputs.  The old physical W chart
# has D != 0; construction here uses D only as a positive polynomial.
# Exact general source: f4e6d79b9956e5a8b39e4a4f88bfbe17eee945f0,
# R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md.
# All three Z's are the FULL same-Gram N4 form and its polarization.
Kval=ell*ell*B3-3*ell*T*A2+2*T**3
A0=(ell+T)/ell
R6=M*Kval*Kval-4*m*m*Dval**3
Nlow=Dval*NB.b+2*lam*P02*(Kval*A0/m+2*m*Dval*Dval/(ell*M))
Plow=Dval*PB.b+P02*(Kval/(2*m)*(3*A0*A0+
       (3*m*m/(ell*ell)+delta)*Dval/M)+6*A0*m*Dval*Dval/(ell*M))
value0=[E(1),E(wv),E(A0),E(A0)]
value1=[E(),E(),E(m/ell,-1),E(m/ell,1)]
assert tr(value0)==E(lam) and not tr(value1)
Z0E=N4(value0);Z2E=N4(value1)
Z1E=N4(va(value0,value1))-Z0E-Z2E
assert not Z0E.b and not Z1E.b and not Z2E.b
Z0,Z1,Z2=Z0E.a,Z1E.a,Z2E.a
Vlow=Dval*Z0+Kval*Z1/(2*m)+Dval*Dval*Z2/M
original=[E1,EBe,EBo,N1,NS,PS,q2,R6,Nlow,Plow,Vlow]
names=['E1','EBe','EBo','N1','NS','PS','b0_original_q2',
       'R6','Nlow','Plow','complete_Vlow']
degree_caps=[2,2,2,2,3,3,2,6,5,5,5]
assert len(original)==len(names)==len(degree_caps)==11
stats={'identicallyZeroOriginalInputs':0,'paidPolynomialReturns':0,'primitiveIntegerReturns':0,
       'unitInitialFaces':0,'nonunitInitialFacesRetained':0,
       'laurentPolynomialProducts':0,'newSourceReturns':0,
       'newSPairs':0,'newBasisElements':0,'unitCells':0,'targetAttempts':0,'targetReturns':0,
       'composedElevenSourceReturns':0}
def weight(poly):return all(not int(ex[2]) and not int(ex[3]) for ex in poly.to_dict())
paid_atoms=[('e',ep),('k',kp),('u',ep+1),('delta',ep*kp-1),
 ('Vbar',(ep+1)*kp+2),('Phi_k_plus_four',kp+4),('P02',P02.n),
 ('M',M.n),('whole_equal_weights_k_plus_two',kp+2),
 ('whole_ell_zero',ell.n),('whole_equal_weights_m',m.n),
 ('whole_original_Lhalf',(2*ell-1).n),
 ('Astar_paid_ONLY_on_entire_b0_zero',Ast.n),
 ('original_W_Pf_chart',Pf.n),('original_W_Phi_chart',Phi.n)]
def exact(a,b):
 tick();quot,rem=divmod(a,b);assert not rem and quot*b==a
 stats['paidPolynomialReturns']+=1
 return quot
def strip(poly):
 oldp=poly;unit=O
 if not poly:return poly,unit
 for name,atom in paid_atoms:
  assert atom and weight(atom)
  while int(poly.total_degree())>0:
   g=poly.gcd(atom)
   if int(g.total_degree())==0:break
   poly=exact(poly,g);unit=unit*g
 assert unit*poly==oldp
 return poly,unit
def paid_den(poly):
 assert poly and weight(poly)
 rem,_=strip(poly);assert rem and int(rem.total_degree())==0
def profile(poly):
 data=[[list(map(int,ex)),str(co)] for ex,co in sorted(poly.to_dict().items())]
 encoded=json.dumps(data,separators=(',',':')).encode()
 return {'degrees_e_k_lambda_t':list(map(int,poly.degrees())) if poly else [-1]*4,
         'totalDegree':int(poly.total_degree()) if poly else -1,
         'terms':len(data),'bytes':len(encoded),'sha256':hashlib.sha256(encoded).hexdigest()}
for zz in (Z0,Z1,Z2):paid_den(zz.d)
data=[];profiles=[]
for name,ori,degree_cap in zip(names,original,degree_caps):
 tick();paid_den(ori.d)
 if not ori:
  data.append({});profiles.append(profile(Z));stats['identicallyZeroOriginalInputs']+=1
  continue
 prim,unit=strip(ori.n);assert prim
 fractions={ex:Fraction(str(co)) for ex,co in prim.to_dict().items()}
 den=1
 for co in fractions.values():den=math.lcm(den,co.denominator)
 integers={ex:co.numerator*(den//co.denominator) for ex,co in fractions.items()}
 content=reduce(math.gcd,(abs(co) for co in integers.values()))
 assert content
 poly=ctx.from_dict({ex:co//content for ex,co in integers.items()})
 assert poly*content==prim*den
 # This full original scaling is only by old paid weight and QQ units.
 assert R(poly)*R(unit)*R(content)==ori*R(ori.d)*R(den)
 stats['primitiveIntegerReturns']+=1
 dd={tuple(map(int,ex)):int(Fraction(str(co))) for ex,co in poly.to_dict().items()}
 assert all(Fraction(str(co)).denominator==1 for co in poly.to_dict().values())
 assert max(ex[2]+ex[3] for ex in dd)<=degree_cap
 data.append(dd);profiles.append(profile(poly))
say('new_eleven_complete_original_boundary_definitions',
 originalNames=names,originalProfiles=profiles,prime=P,ray=[-1,0],
 knownLambdaNonzeroValuationZero=True,
 precedingTheoremRun=46157115224,
 originalCoordinateSourceBlob='2f7fd85b7345f8c41747669526ffcf88d9b83acc',
 necessaryWeightDefinitionsSourceBlob='47281af16fdd0ad7500ecda377c3cb9f9d65e725',
 allOriginalPolynomialUnitScalesReturned=True,
 newValueSources=['R6','Nlow','Plow','complete_Vlow'],
 newValueZProfiles=[profile(Z0.n),profile(Z1.n),profile(Z2.n)],
 newValueZDenominatorsAllPaid=True,physicalDNotInverted=True,
 newTargetNames=['k_plus_two','two_lambda_minus_three'],fixedTargetExponents=[1,2,3,4],
 rawSevenDefinitionSourceBlob='b33c1abc4ebeaf2ad7f84ff883a56155352df81e',
 rawSevenDefinitionSourceSHA256='54e04e96a39f0caca9e59d55ba3636f27cf8678c7cfeffbecb6212ce8756af0d',
 noOldSevenRowInitialAlgorithmOrProjectionReexecuted=True)

# Sparse exact Fp Laurent polynomials in (k_lead,lambda_lead,t_lead).
# Rows are ordinary polynomials; original multiplier tags may be Laurent.
NVAR=3;ZERO={};ONE={(0,0,0):1}
def clean(p):return {e:c%P for e,c in p.items() if c%P}
def add(p,q):
 out=dict(p)
 for ex,c in q.items():out[ex]=(out.get(ex,0)+c)%P
 return clean(out)
def neg(p):return {ex:(-c)%P for ex,c in p.items()}
def sub(p,q):return add(p,neg(q))
def shift(p,ex,scalar=1):
 return {tuple(a+b for a,b in zip(m,ex)):c*scalar%P
         for m,c in p.items() if c*scalar%P}
def mul(p,q):
 tick();out={}
 for a,c in p.items():
  for b,d in q.items():
   ex=tuple(x+y for x,y in zip(a,b))
   out[ex]=(out.get(ex,0)+c*d)%P
 stats['laurentPolynomialProducts']+=1
 return clean(out)
def order(ex):return (sum(ex),-ex[2],-ex[1],-ex[0])
def lead(p):return max(p,key=order)
def lp_profile(p):
 encoded=json.dumps([[list(ex),co] for ex,co in sorted(p.items())],separators=(',',':')).encode()
 return {'terms':len(p),'minExponents':[min((ex[i] for ex in p),default=0) for i in range(3)],
         'maxExponents':[max((ex[i] for ex in p),default=0) for i in range(3)],
         'bytes':len(encoded),'sha256':hashlib.sha256(encoded).hexdigest()}
def tag_return(poly,tags,forms):
 assert len(tags)==len(forms)==11
 value={}
 for a,b in zip(tags,forms):value=add(value,mul(a,b))
 assert value==poly
 stats['newSourceReturns']+=1
def normalized(poly,tags):
 if not poly:return {},tags
 low=tuple(min(ex[i] for ex in poly) for i in range(3))
 amount=tuple(-v for v in low)
 inv=pow(poly[lead(poly)],-1,P)
 return shift(poly,amount,inv),[shift(x,amount,inv) for x in tags]
def reduce_row(poly,tags,basis):
 # Keep the exact source of remainder+work while removing leading terms.
 while poly:
  tick();work=dict(poly);rem={}
  while work:
   mon=lead(work);coef=work[mon];used=False
   for bp,bt in basis:
    bm=lead(bp)
    if all(a>=b for a,b in zip(mon,bm)):
     difference=tuple(a-b for a,b in zip(mon,bm))
     scale=coef*pow(bp[bm],-1,P)%P
     work=sub(work,shift(bp,difference,scale))
     tags=[sub(a,shift(b,difference,scale)) for a,b in zip(tags,bt)]
     used=True;break
   if not used:
    rem[mon]=coef;del work[mon]
  if not rem:return {},tags
  low=tuple(min(ex[i] for ex in rem) for i in range(3))
  poly,tags=normalized(rem,tags)
  if not any(low):return poly,tags
  # Monomial stripping can expose a new reducible leading term.
 return {},tags

TARGETS=[('k_plus_two',{(1,0,0):1,(0,0,0):2}),
         ('two_lambda_minus_three',{(0,1,0):2,(0,0,0):P-3})]
TARGET_POWERS=(1,2,3,4)
# New value rows are seeded FIRST; there is no old seven-row solve.
SEED_ORDER=(7,8,9,10,0,1,2,3,4,5,6)
def power(poly,n):
 out=dict(ONE)
 for _ in range(n):out=mul(out,poly)
 return out
def target_remainder(target,basis):
 work=dict(target);rem={};coeff=[{} for _ in range(11)]
 while work:
  tick();mon=lead(work);co=work[mon];used=False
  for row,tags in basis:
   lm=lead(row)
   if all(a>=b for a,b in zip(mon,lm)):
    diff=tuple(a-b for a,b in zip(mon,lm))
    sc=co*pow(row[lm],-1,P)%P
    work=sub(work,shift(row,diff,sc))
    coeff=[add(x,shift(y,diff,sc)) for x,y in zip(coeff,tags)]
    used=True;break
  if not used:rem[mon]=co;del work[mon]
 # NO monomial or scalar division of the target: its fixed power is kept.
 return rem,coeff
def compose_original_return(target,tags,forms,raw_forms,normalizers):
 tag_return(target,tags,forms)
 combined=[mul(tag,norm) for tag,norm in zip(tags,normalizers)]
 tag_return(target,combined,raw_forms)
 stats['composedElevenSourceReturns']+=1
 return [lp_profile(tag) for tag in combined]
def solve_initial(forms,raw_forms,normalizers):
 assert len(forms)==len(raw_forms)==len(normalizers)==11
 basis=[];pairs=[];unit_tags=None
 def append_row(poly,tags):
  nonlocal unit_tags
  poly,tags=normalized(poly,tags)
  poly,tags=reduce_row(poly,tags,basis)
  tag_return(poly,tags,forms)
  if not poly:return
  assert all(all(e>=0 for e in ex) for ex in poly)
  if poly==ONE:
   unit_tags=tags;stats['unitCells']+=1;return
  index=len(basis);lm_new=lead(poly)
  for i,(other,tag) in enumerate(basis):
   lm_old=lead(other)
   # The ordinary polynomial product criterion is valid for these
   # polynomial rows; Laurent source vectors do not change that identity.
   if all(min(a,b)==0 for a,b in zip(lm_new,lm_old)):continue
   lm=tuple(max(a,b) for a,b in zip(lm_new,lm_old))
   pairs.append((sum(lm),i,index))
  basis.append((poly,tags));stats['newBasisElements']+=1
 for i in SEED_ORDER:
  tags=[dict(ONE) if j==i else {} for j in range(11)]
  append_row(forms[i],tags)
  if unit_tags is not None:break
 while pairs and unit_tags is None:
  tick();pairs.sort();_,i,j=pairs.pop(0)
  ap,at=basis[i];bp,bt=basis[j]
  am,bm=lead(ap),lead(bp)
  lm=tuple(max(a,b) for a,b in zip(am,bm))
  da=tuple(a-b for a,b in zip(lm,am));db=tuple(a-b for a,b in zip(lm,bm))
  ca=pow(ap[am],-1,P);cb=pow(bp[bm],-1,P)
  sp=sub(shift(ap,da,ca),shift(bp,db,cb))
  tags=[sub(shift(a,da,ca),shift(b,db,cb)) for a,b in zip(at,bt)]
  stats['newSPairs']+=1
  append_row(sp,tags)
 outcome={'excluded':unit_tags is not None,
          'completeElevenOriginalUnitReturn':unit_tags is not None,
          'fixedNewElevenRowAlgorithmFinished':True,
          'originalInitialProfiles':[lp_profile(f) for f in raw_forms],
          'retainedBasisProfiles':[lp_profile(b) for b,tags in basis],
          'noResidueOrOriginalPointExistenceClaim':True}
 if unit_tags is not None:
  outcome['unitMultiplierProfiles']=compose_original_return(
    ONE,unit_tags,forms,raw_forms,normalizers)
 tested=[]
 for target_name,target in TARGETS:
  item={'target':target_name,'fixedAvailablePowers':list(TARGET_POWERS),
        'returnedPower':None,'powersTested':[]}
  for exponent in TARGET_POWERS:
   tick();tpower=power(target,exponent);stats['targetAttempts']+=1
   if unit_tags is not None:
    rem={};coeff=[mul(tpower,x) for x in unit_tags]
   else:rem,coeff=target_remainder(tpower,basis)
   tag_return(sub(tpower,rem),coeff,forms)
   item['powersTested'].append({'power':exponent,'remainder':lp_profile(rem)})
   if not rem:
    item['returnedPower']=exponent
    item['completeElevenOriginalLaurentMultiplierProfiles']=compose_original_return(
       tpower,coeff,forms,raw_forms,normalizers)
    item['allOriginalInitialNormalizationsComposed']=True
    stats['targetReturns']+=1
    break
  tested.append(item)
 outcome['newFixedPositiveTargetResults']=tested
 return outcome
def breakpoints(dd):
 heights={}
 for (i,j,l,m) in dd:
  h=-i;heights[m]=min(heights.get(m,h),h)
 out=set();keys=sorted(heights)
 for i in keys:
  for j in keys:
   if i>=j:continue
   z=Fraction(heights[i]-heights[j],j-i)
   values=[Fraction(h)+m*z for m,h in heights.items()]
   if values.count(min(values))>=2:out.add(z)
 return out
cuts=sorted(set().union(*(breakpoints(dd) for dd in data)))
cells=[];edges=[None]+cuts+[None]
for lo,hi in zip(edges,edges[1:]):
 z=Fraction(0) if lo is None and hi is None else hi-1 if lo is None else lo+1 if hi is None else (lo+hi)/2
 cells.append({'kind':'open interval','lo':str(lo) if lo is not None else None,
               'hi':str(hi) if hi is not None else None,'sample':z})
for z in cuts:cells.append({'kind':'point','value':str(z),'sample':z})
def description(cell):return {k:str(v) if k=='sample' else v for k,v in cell.items()}

def initial(dd,ratio,exact_zero=False):
 if exact_zero:dd={ex:c for ex,c in dd.items() if not ex[3]}
 if not dd:
  return {},{'zeroInputOnExactTZeroOrIdenticallyZero':True},{},dict(ONE)
 minimum=min(-ex[0]+ratio*ex[3] for ex in dd)
 face={ex:c for ex,c in dd.items() if -ex[0]+ratio*ex[3]==minimum}
 out={}
 for ex,c in face.items():
  key=(ex[1],ex[2],ex[3]);out[key]=(out.get(key,0)+c)%P
 out=clean(out)
 if not out:
  stats['nonunitInitialFacesRetained']+=1
  return None,{'minimumGeometricWeight':str(minimum),'unitCoefficient':False},None,None
 stats['unitInitialFaces']+=1
 if exact_zero:assert all(ex[2]==0 for ex in out)
 raw_initial=dict(out)
 removed=tuple(min(ex[i] for ex in out) for i in range(3))
 leading_scalar=out[lead(out)]
 out,_=normalized(out,[])
 normalizer=shift(ONE,tuple(-v for v in removed),pow(leading_scalar,-1,P))
 assert mul(normalizer,raw_initial)==out
 if exact_zero:assert removed[2]==0
 return out,{'minimumGeometricWeight':str(minimum),'unitCoefficient':True,
             'eLeadingResidueNormalizedToOne':True,
             'removedTorusMonomial':list(removed),'removedNonzeroScalar':leading_scalar,
             'originalInitialNormalizationReturned':True,'profile':lp_profile(out)},raw_initial,normalizer
say('new_eleven_original_t_valuation_partition',ray=[-1,0],
 lambdaValuationExactlyZero=True,lambdaNonzero=True,
 cells=[description(c) for c in cells],allRationalRatiosCovered=True,
 recomputedFromAllElevenOriginalInputs=True,tExactlyZeroSeparate=True,
 fixedTargetExponents=list(TARGET_POWERS),newValueSeedOrder=list(SEED_ORDER))
def run_cell(ratio,exact_zero=False):
 forms=[];meta=[];raw_forms=[];normalizers=[]
 for dd in data:
  form,item,raw,norm=initial(dd,ratio,exact_zero)
  forms.append(form);meta.append(item);raw_forms.append(raw);normalizers.append(norm)
 if any(form is None for form in forms):
  return {'originalFaceMetadata':meta,'excluded':False,
          'newFixedPositiveTargetResults':[],
          'reason':'an entire minimum face is p-nonunit; whole cell retained'}
 result=solve_initial(forms,raw_forms,normalizers)
 return {'originalFaceMetadata':meta,**result}
results=[]
for index,cell in enumerate(cells):
 tick();result=run_cell(cell['sample'])
 row={'cell':index,'partition':description(cell),**result}
 say('new_eleven_original_boundary_cell_return',**row);results.append(row)
zero_result=run_cell(Fraction(0),True)
say('new_eleven_original_t_exactly_zero_return',**zero_result)
closed=all(r['excluded'] for r in results) and zero_result['excluded']
say('new_eleven_original_negative_e_unit_k_boundary_finished',
 ray=[-1,0],nonzeroTCells=len(results),
 excludedNonzeroTCells=sum(r['excluded'] for r in results),
 tExactlyZeroExcluded=zero_result['excluded'],
 wholePreviouslyRetainedRayExcluded=closed,
 originalLambdaZeroAndNonzeroValuationAlreadyExcludedByPriorTheorem=True,
 allNewTargetClaimsRequireCompleteElevenSourceReturn=True,
 allUnknownTargetAndMinimumFaceCellsRetained=True,
 otherFiveRaysUnchanged=True,noFiniteDVRModelClaim=True,noWholeWExclusionClaim=True,
 noCharacteristicZeroLiftOfResidueTargetPowers=True,physicalDNotInverted=True,
 noOldSevenRowInitialAlgorithmOrCofactorGateReplayed=True,
 noCoefficientPayloadSaved=True,originalISPClaim=False,statistics=stats,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
signal.setitimer(signal.ITIMER_REAL,0)
