#!/usr/bin/env python3
"""NEW W/b0: full original I6+q2 initial ideal on the remaining (-1,0) ray.
The preceding original q2/R6/N5 theorem already forces lambda nonzero and
v(lambda)=0 on this ray.  This input instead uses the complete original
Gram equations in the independent same-point lambda,t coordinates.
All rational t valuations and t exactly zero are covered. Fixed p=1009.
Actual Laurent source vectors accompany every new initial polynomial;
only a returned original Laurent unit excludes a cell. Retained cells
do not assert existence. No old three-input initial or projection gate.
180 seconds / 4 GiB; zero dependencies; no coefficient payload or cache.
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
original=[E1,EBe,EBo,N1,NS,PS,q2]
names=['E1','EBe','EBo','N1','NS','PS','b0_original_q2']
stats={'paidPolynomialReturns':0,'primitiveIntegerReturns':0,
       'unitInitialFaces':0,'nonunitInitialFacesRetained':0,
       'laurentPolynomialProducts':0,'newSourceReturns':0,
       'newSPairs':0,'newBasisElements':0,'unitCells':0}
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
data=[];profiles=[]
for name,ori in zip(names,original):
 tick();paid_den(ori.d)
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
 assert max(ex[2]+ex[3] for ex in dd)<= (3 if name in ('NS','PS') else 2)
 data.append(dd);profiles.append(profile(poly))
say('new_full_I6_q2_original_boundary_definitions',
 originalNames=names,originalProfiles=profiles,prime=P,ray=[-1,0],
 knownLambdaNonzeroValuationZero=True,
 precedingTheoremRun=46157115224,
 originalCoordinateSourceBlob='2f7fd85b7345f8c41747669526ffcf88d9b83acc',
 necessaryWeightDefinitionsSourceBlob='47281af16fdd0ad7500ecda377c3cb9f9d65e725',
 allOriginalPolynomialUnitScalesReturned=True,
 noOldThreeInputInitialsOrQlambdaOrCofactorsReexecuted=True)

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
def solve_initial(forms,cell_label):
 basis=[];pairs=[]
 def append_row(poly,tags):
  poly,tags=normalized(poly,tags)
  poly,tags=reduce_row(poly,tags,basis)
  tag_return(poly,tags,forms)
  if not poly:return False,None
  assert all(all(e>=0 for e in ex) for ex in poly)
  if poly==ONE:
   stats['unitCells']+=1
   return True,{'excluded':True,'completeSevenOriginalLaurentReturn':True,
       'unitMultiplierProfiles':[lp_profile(t) for t in tags],
       'originalInitialProfiles':[lp_profile(f) for f in forms],
       'basisCountBeforeUnit':len(basis)}
  index=len(basis)
  for i,(other,tag) in enumerate(basis):
   lm=tuple(max(a,b) for a,b in zip(lead(poly),lead(other)))
   pairs.append((sum(lm),i,index))
  basis.append((poly,tags));stats['newBasisElements']+=1
  return False,None
 for i,form in enumerate(forms):
  tags=[dict(ONE) if j==i else {} for j in range(len(forms))]
  done,result=append_row(form,tags)
  if done:return result
 while pairs:
  tick();pairs.sort();_,i,j=pairs.pop(0)
  ap,at=basis[i];bp,bt=basis[j]
  am,bm=lead(ap),lead(bp)
  lm=tuple(max(a,b) for a,b in zip(am,bm))
  da=tuple(a-b for a,b in zip(lm,am));db=tuple(a-b for a,b in zip(lm,bm))
  ca=pow(ap[am],-1,P);cb=pow(bp[bm],-1,P)
  sp=sub(shift(ap,da,ca),shift(bp,db,cb))
  tags=[sub(shift(a,da,ca),shift(b,db,cb)) for a,b in zip(at,bt)]
  stats['newSPairs']+=1
  done,result=append_row(sp,tags)
  if done:return result
 return {'excluded':False,'completeSevenOriginalLaurentReturn':False,
         'fixedLaurentRowAlgorithmFinished':True,
         'originalInitialProfiles':[lp_profile(f) for f in forms],
         'retainedBasisProfiles':[lp_profile(b) for b,t in basis],
         'noResidueOrOriginalPointExistenceClaim':True}
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
 if not dd:return {},{'zeroInputOnExactTZero':True}
 minimum=min(-ex[0]+ratio*ex[3] for ex in dd)
 face={ex:c for ex,c in dd.items() if -ex[0]+ratio*ex[3]==minimum}
 out={}
 for ex,c in face.items():
  key=(ex[1],ex[2],ex[3]);out[key]=(out.get(key,0)+c)%P
 out=clean(out)
 if not out:
  stats['nonunitInitialFacesRetained']+=1
  return None,{'minimumGeometricWeight':str(minimum),'unitCoefficient':False}
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
             'originalInitialNormalizationReturned':True,'profile':lp_profile(out)}
say('new_full_I6_q2_t_valuation_partition',ray=[-1,0],
 lambdaValuationExactlyZero=True,lambdaNonzero=True,
 cells=[description(c) for c in cells],allRationalRatiosCovered=True,tExactlyZeroSeparate=True)
results=[]
for index,cell in enumerate(cells):
 tick();forms=[];meta=[]
 for dd in data:
  form,item=initial(dd,cell['sample']);forms.append(form);meta.append(item)
 if any(form is None for form in forms):
  result={'excluded':False,'reason':'entire minimum face is p-nonunit'}
 else:result=solve_initial(forms,index)
 row={'cell':index,'partition':description(cell),'originalFaceMetadata':meta,**result}
 say('new_full_I6_q2_boundary_cell_return',**row);results.append(row)
forms=[];meta=[]
for dd in data:
 form,item=initial(dd,Fraction(0),True);forms.append(form);meta.append(item)
if any(form is None for form in forms):
 zero_result={'excluded':False,'reason':'unpaid t-zero minimum face'}
else:zero_result=solve_initial(forms,'t exactly zero')
say('new_full_I6_q2_t_exactly_zero_return',originalFaceMetadata=meta,**zero_result)
closed=all(r['excluded'] for r in results) and zero_result['excluded']
say('new_full_I6_q2_negative_e_unit_k_boundary_finished',
 ray=[-1,0],nonzeroTCells=len(results),excludedNonzeroTCells=sum(r['excluded'] for r in results),
 tExactlyZeroExcluded=zero_result['excluded'],wholePreviouslyRetainedRayExcluded=closed,
 originalLambdaZeroAndNonzeroValuationAlreadyExcludedByPriorTheorem=True,
 otherFiveRaysUnchanged=True,noFiniteDVRModelClaim=True,noWholeWExclusionClaim=True,
 noOldInitialOrCofactorGateReplayed=True,noCoefficientPayloadSaved=True,
 originalISPClaim=False,statistics=stats,peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
signal.setitimer(signal.ITIMER_REAL,0)
