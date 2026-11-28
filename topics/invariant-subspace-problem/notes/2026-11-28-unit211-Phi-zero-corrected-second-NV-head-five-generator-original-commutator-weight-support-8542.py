#!/usr/bin/env python3
"""NEW corrected Phi, whole remaining second NV head after ell=3/2 closure.
Five genuine generators from the DISPLAYED four-original-cubic head unit.
Only new ordinary original-tagged lambda/sigma actions, their commutators,
and a fixed-point selection of five TRUE original DAG columns.
If selection succeeds, define an integer polynomial 5x5 matrix B.
Universal adjugate gives det(B) in the original localized ideal; a single
fixed F_1009 point (u,Q)=(2,2) and complete matrix inverse certify nonzero.
No expanded QQ determinant, old sigma scalars/cofactors/gcd, point change,
physical D inverse, free-five/commuting-matrix assumption, or emptiness.
Self-contained. 120 seconds /1 GiB; failed new goal is retained, not retried.
"""
import hashlib,json,math,resource,signal,time
from itertools import permutations
from flint import fmpq_mpoly_ctx
START=time.perf_counter();DEADLINE=START+120;P=1009;POINT=(2,2)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
STAT={'exactPolynomialProducts':0,'rawNVIdentityReturns':0,
      'headInverseCoordinates':0,'ordinaryNormalFormReturns':0,
      'fiveActionColumns':0,'commutatorOriginalReturns':0,
      'DAGOriginalReturns':0,'oldPaidDenominatorChecks':0,
      'integerColumnReturns':0,'modularInverseCoordinates':0}
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute120')
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True,separators=(',',':')),flush=True)
ctx=fmpq_mpoly_ctx.get(('u','Q','lambda','sigma'),'lex')
up,Qp,lp,zp=ctx.gens();ONE=ctx.constant(1);ZERO=ctx.constant(0)
def poly(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
def pp(v):
 v=poly(v);d=v.to_dict()
 return {'degrees':list(map(int,v.degrees())) if v else [-1]*4,
         'totalDegree':int(v.total_degree()) if v else -1,'terms':len(d),
         'sha256':hashlib.sha256(str(sorted(d.items())).encode()).hexdigest()}
def exact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 STAT['exactPolynomialProducts']+=1;return q
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=ONE if d is None else poly(d);assert d
  if not n:self.n=ZERO;self.d=ONE;return
  if reduce:
   g=n.gcd(d);n=exact(n,g);d=exact(d,g)
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __neg__(self):return R(-self.n,self.d,False)
 def __add__(self,v):
  v=R(v)
  if not self:return v
  if not v:return self
  g=self.d.gcd(v.d);a=exact(self.d,g);b=exact(v.d,g)
  return R(self.n*b+v.n*a,a*v.d)
 __radd__=__add__
 def __sub__(self,v):return self+-R(v)
 def __rsub__(self,v):return R(v)+-self
 def __mul__(self,v):
  v=R(v)
  if not self or not v:return R()
  g=self.n.gcd(v.d);h=v.n.gcd(self.d)
  return R(exact(self.n,g)*exact(v.n,h),
           exact(self.d,h)*exact(v.d,g),False)
 __rmul__=__mul__
 def __truediv__(self,v):
  v=R(v);assert v;return self*R(v.d,v.n,False)
 def __rtruediv__(self,v):return R(v)/self
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  return R(self.n**n,self.d**n,False)
 def __eq__(self,v):
  v=R(v);return self.n*v.d==v.n*self.d
def rp(v):
 v=R(v);return {'numerator':pp(v.n),'denominator':pp(v.d)}

def matrix_profile(A):
 prof=[[rp(x) for x in row] for row in A]
 raw=json.dumps(prof,sort_keys=True,separators=(',',':')).encode()
 return {'rows':len(A),'columns':len(A[0]) if A else 0,
         'nonzeroEntries':sum(bool(x) for row in A for x in row),
         'numeratorTerms':sum(len(R(x).n.to_dict()) for row in A for x in row),
         'entryProfilesSHA256':hashlib.sha256(raw).hexdigest()}

def pureweight(p):return all(not int(e[2]) and not int(e[3]) for e in p.to_dict())
paid_seen=set()
def oldpaid(v):
 v=R(v);assert pureweight(v.d)
 key=str(v.d)
 if key not in paid_seen:
  d=v.d
  while int(d.total_degree())>0:
   g=d.gcd(PAID)
   if int(g.total_degree())==0:break
   d=exact(d,g)
  assert d and int(d.total_degree())==0,('unpaid denominator',pp(d))
  paid_seen.add(key);STAT['oldPaidDenominatorChecks']+=1
 return v
def gd(v):
 v=oldpaid(v)
 return max((int(e[2])+int(e[3]) for e in v.n.to_dict()),default=-1)
def geo(v):
 v=oldpaid(v);groups={}
 for ex,c in v.n.to_dict().items():
  key=(int(ex[2]),int(ex[3]));ee=(int(ex[0]),int(ex[1]),0,0)
  groups.setdefault(key,{})[ee]=c
 return {k:R(ctx.from_dict(d),v.d) for k,d in groups.items()}
def sumR(a):return sum(a,R())
def rawsum(tag):return sumR(tag[i]*RAW[i] for i in range(3))
def addtag(a,b):return [a[i]+b[i] for i in range(3)]
def scaletag(c,a):return [c*x for x in a]
def mvec(A,v):return [sumR(a*b for a,b in zip(row,v)) for row in A]
def mmul(A,B):
 return [[sumR(A[i][k]*B[k][j] for k in range(len(B)))
          for j in range(len(B[0]))] for i in range(len(A))]
def ddet(A):
 n=len(A);out=R()
 for p in permutations(range(n)):
  sign=-1 if sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))%2 else 1
  term=R(sign)
  for i,j in enumerate(p):term*=A[i][j]
  out+=term
 return out

u,Q,lam,sigma=map(R,(up,Qp,lp,zp))
s=u-1;delta=1-Q;Kw=Q+4*s;L=Q-2*s*(u-2);ell=L/Q;m=u-ell
T0=-Kw;J=Q-4*s*s;P02=2*s*L;theta=u-ell*Q
Mn=2*up*(Qp-2*(up-1)*(up-2))-(Qp-2*(up-1)*(up-2))**2-up**2*Qp
Lp=Qp-2*(up-1)*(up-2)
PAID=Qp*(Qp-1)*(up-1)*(Qp+4*(up-1))*Lp*Mn*(up*Qp-Lp)*(3*Qp-2*Lp)
a=lam-R(3)/2;j=ell*(lam-R(1)/2)-m*sigma
E=P02*j/T0
f=(P02*lam-Q*E+s*T0)/(J-Q)
w=lam-1-(j-ell)
rr=lam*lam+lam-R(3)/4-delta*sigma*sigma
RR=a*a-delta*sigma*sigma
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1
E2=ell*a*a-2*m*a*sigma+ell*delta*sigma*sigma-A2
E3=ell*a**3-3*m*a*a*sigma+3*ell*delta*a*sigma*sigma-m*delta*sigma**3-B3
Nsharp=2*(-rr*f+RR*E-w*(u*a+theta*sigma))
NV=Nsharp-2*f*E2
# Independent previously proved idempotent compact formula, definitions only.
beta=R(3)/2-lam-sigma;a0=1-ell
Cf=-1+2*a0*beta*beta-4*s*beta*sigma+4*s*s*sigma*sigma
Cu=(1-2*a0*beta+2*s*sigma)*(beta-2*s*sigma)
NVcompact=(f*Cf+u*Cu+2*E*beta*(beta+2*sigma)
           -T0*sigma*(1-2*a0*beta)+2*lam*P02*sigma*sigma)
assert NV==NVcompact and gd(E2)<=2 and gd(E3)<=3 and gd(NV)<=3
STAT['rawNVIdentityReturns']+=1
RAW=[E2,E3,NV]
for v in RAW:oldpaid(v)
MON3=[(3,0),(2,1),(1,2),(0,3)]
polys=[lam*E2,sigma*E2,E3,NV]
ptags=[[lam,R(),R()],[sigma,R(),R()],[R(),R(1),R()],[R(),R(),R(1)]]
H=[[geo(polys[c]).get(MON3[r],R()) for c in range(4)] for r in range(4)]
head=2*P02*m*delta*(3-2*ell)
assert ddet(H)==head
assert m*m-delta*(ell-1)**2==s*s*(3-2*ell)
HI=[]
for i in range(4):
 row=[]
 for jcol in range(4):
  minor=[[H[r][c] for c in range(4) if c!=i]
         for r in range(4) if r!=jcol]
  row.append(oldpaid(R((-1)**(i+jcol))*ddet(minor)/head))
 HI.append(row)
for A,B in ((H,HI),(HI,H)):
 C=mmul(A,B)
 for i in range(4):
  for k in range(4):
   assert C[i][k]==int(i==k)
   STAT['headInverseCoordinates']+=1
rules=[];rule_tags=[]
for jcol,(aa,bb) in enumerate(MON3):
 tag=[sumR(HI[i][jcol]*ptags[i][r] for i in range(4)) for r in range(3)]
 low=lam**aa*sigma**bb-rawsum(tag)
 assert gd(low)<=2
 assert lam**aa*sigma**bb==low+rawsum(tag)
 for v in tag:oldpaid(v)
 rules.append(low);rule_tags.append(tag)
qtag=[1/(ell*delta),R(),R()]
qlow=sigma*sigma-rawsum(qtag)
assert gd(qlow)<=2 and not geo(qlow).get((0,2),R())
BAS=[(0,0),(1,0),(0,1),(2,0),(1,1)]
BVAL=[lam**i*sigma**j for i,j in BAS]
def basis_poly(v):return sumR(v[i]*BVAL[i] for i in range(5))
def normal(value):
 value=oldpaid(value);rem=value;tag=[R(),R(),R()]
 while gd(rem)>=3:
  tick();terms=geo(rem)
  aa,bb=max((k for k in terms if sum(k)>=3),key=lambda k:(sum(k),k[0],k[1]))
  c=terms[(aa,bb)]
  r=0 if aa>=3 else 1 if aa>=2 else 2 if aa>=1 else 3
  ra,rb=MON3[r];mult=c*lam**(aa-ra)*sigma**(bb-rb)
  rem-=mult*(lam**ra*sigma**rb-rules[r])
  tag=addtag(tag,scaletag(mult,rule_tags[r]))
 c=geo(rem).get((0,2),R())
 if c:
  rem-=c*(sigma*sigma-qlow)
  tag=addtag(tag,scaletag(c,qtag))
 terms=geo(rem);assert all(k in BAS for k in terms)
 vec=[terms.get(k,R()) for k in BAS]
 assert value==basis_poly(vec)+rawsum(tag)
 for v in vec+tag:oldpaid(v)
 STAT['ordinaryNormalFormReturns']+=1
 return vec,tag
actions=[];action_tags=[]
for variable in (lam,sigma):
 cols=[];tags=[]
 for b in BVAL:
  v,tg=normal(variable*b);cols.append(v);tags.append(tg)
  STAT['fiveActionColumns']+=1
 actions.append([[cols[j][i] for j in range(5)] for i in range(5)])
 action_tags.append(tags)
ML,MS=actions;TL,TS=action_tags
def tag_columns(tags,v):
 return [sumR(v[i]*tags[i][r] for i in range(5)) for r in range(3)]
seeds=[]
for jcol in range(5):
 lc=[ML[i][jcol] for i in range(5)];sc=[MS[i][jcol] for i in range(5)]
 v=[x-y for x,y in zip(mvec(ML,sc),mvec(MS,lc))]
 tlsc=tag_columns(TL,sc);tslc=tag_columns(TS,lc)
 tg=[-lam*TS[jcol][r]-tlsc[r]+sigma*TL[jcol][r]+tslc[r] for r in range(3)]
 assert basis_poly(v)==rawsum(tg)
 for t in tg:oldpaid(t)
 STAT['commutatorOriginalReturns']+=1
 seeds.append({'v':v,'tag':tg,'depth':0,'parent':None,'kind':'commutator','basisIndex':jcol})
say('new_global_B2_five_generator_original_actions_and_defects',
    scope='corrected physical Phi, B2, ell!=3/2 already paid',
    rawProfiles=[rp(v) for v in RAW],head=rp(head),
    actionProfiles=[matrix_profile(A) for A in actions],
    commutatorNonzeroColumns=[i for i,a in enumerate(seeds) if any(a['v'])],
    allFiveDefectsReturnedToThreeOriginals=True,noFreeOrCommutingMatrixAssumption=True)

class FixedPointIneligible(Exception):pass
def rational_parts(c):
 ss=str(c);a,sep,b=ss.partition('/')
 return int(a),int(b) if sep else 1
def common_integer_den(polys):
 d=1
 for a in polys:
  for c in a.to_dict().values():
   _,b=rational_parts(c);d=math.lcm(d,b)
 return d
def integer_pair(v):
 v=R(v);a=common_integer_den([v.n,v.d])
 n=v.n*a;d=v.d*a;content=0
 for p0 in (n,d):
  for c in p0.to_dict().values():
   aa,bb=rational_parts(c);assert bb==1;content=math.gcd(content,abs(aa))
 assert content>0;n=n/content;d=d/content
 assert R(n,d)==v
 return n,d
def evpoly(p):
 assert pureweight(p)
 z=0
 for ex,c in p.to_dict().items():
  a,b=rational_parts(c)
  if b%P==0:raise FixedPointIneligible('rational coefficient not p-integral')
  z=(z+(a%P)*pow(b%P,P-2,P)*pow(POINT[0],int(ex[0]),P)
     *pow(POINT[1],int(ex[1]),P))%P
 return z
def ev(v):
 v=R(v);assert pureweight(v.n) and pureweight(v.d)
 n,d=integer_pair(v);dn=evpoly(d)
 if dn==0:raise FixedPointIneligible('fixed point denominator zero')
 return evpoly(n)*pow(dn,P-2,P)%P
try:
 paid_value=evpoly(PAID)
 if not paid_value:raise FixedPointIneligible('old-paid weight zero')
 MLp=[[ev(x) for x in row] for row in ML]
 MSp=[[ev(x) for x in row] for row in MS]
 seedp=[[ev(x) for x in a['v']] for a in seeds]
except FixedPointIneligible as err:
 say('new_fixed_point_input_ineligible_no_selection',
     p=P,point=list(POINT),reason=str(err),noPointChange=True,
     noNewPureWeightSupport=True,statistics=STAT)
 raise SystemExit(0)
say('new_single_fixed_point_input_eligibility_complete',
    p=P,point=list(POINT),paidValue=paid_value,
    allActualActionAndSeedDenominatorsChecked=True,
    noRankOrIdealOutcomeUsedToSelectPoint=True)
def modvec(A,v):return [sum(a*b for a,b in zip(row,v))%P for row in A]
def child(parent,which,selected_index):
 A=actions[which];tags=action_tags[which];var=(lam,sigma)[which]
 v=mvec(A,parent['v'])
 correction=tag_columns(tags,parent['v'])
 tg=[var*parent['tag'][r]-correction[r] for r in range(3)]
 assert basis_poly(v)==rawsum(tg)
 for t in tg:oldpaid(t)
 STAT['DAGOriginalReturns']+=1
 return {'v':v,'tag':tg,'depth':parent['depth']+1,
         'parent':selected_index,'kind':('lambda','sigma')[which],
         'basisIndex':None}
queue=list(seeds);echelon={};selected=[];processed=0;dag_metadata=[]
while queue and len(selected)<5:
 tick();cand=queue.pop(0);processed+=1
 pointv=[ev(x) for x in cand['v']];r=pointv[:]
 for pivot,row in sorted(echelon.items()):
  c=r[pivot]
  if c:r=[(a-c*b)%P for a,b in zip(r,row)]
 if not any(r):continue
 pivot=next(i for i,a in enumerate(r) if a)
 inv=pow(r[pivot],P-2,P)
 assert r[pivot]*inv%P==1
 echelon[pivot]=[a*inv%P for a in r]
 selected_index=len(selected)
 selected.append(cand)
 dag_metadata.append({'selected':selected_index,'kind':cand['kind'],
                      'basisIndex':cand['basisIndex'],'parent':cand['parent'],
                      'depth':cand['depth'],'modPivot':pivot})
 if len(selected)<5:
  queue.append(child(cand,0,selected_index))
  queue.append(child(cand,1,selected_index))
say('new_fixed_point_original_commutator_DAG_selection',
    p=P,point=list(POINT),rank=len(selected),processed=processed,
    selectedOriginalDAG=dag_metadata,
    gaussianResidualsNeverUsedAsOriginalColumns=True,
    statistics=STAT)
if len(selected)<5:
 say('new_global_B2_commutator_support_inconclusive',
     fixedPointRank=len(selected),noPointChange=True,
     noNonzeroDeterminantClaim=True,noWholeSecondHeadExclusion=True,
     allOriginalFibersRetained=True,statistics=STAT)
 raise SystemExit(0)

# Integer polynomial columns; ONLY actual coefficient denominators are cleared.
# Rational integer content is a QQ unit and removes no weight-zero component.
scales=[];Bcols=[];fulltags=[]
for cand in selected:
 den=ONE
 for v in cand['v']:
  v=oldpaid(v);den=exact(den,den.gcd(v.d))*v.d
 oldpaid(R(1,den))
 col=[]
 for v in cand['v']:
  r=R(den)*v;assert r.d==ONE;col.append(r.n)
 k=common_integer_den(col);col=[p0*k for p0 in col];content=0
 for p0 in col:
  for c in p0.to_dict().values():
   aa,bb=rational_parts(c);assert bb==1;content=math.gcd(content,abs(aa))
 assert content>0
 col=[p0/content for p0 in col]
 scale=R(den)*R(k)/content
 tg=scaletag(scale,cand['tag'])
 for r in tg:oldpaid(r)
 for i in range(5):
  assert R(col[i])==scale*cand['v'][i] and pureweight(col[i])
  assert all(rational_parts(c)[1]==1 for c in col[i].to_dict().values())
 assert sumR(R(col[i])*BVAL[i] for i in range(5))==rawsum(tg)
 STAT['integerColumnReturns']+=1
 scales.append(scale);Bcols.append(col);fulltags.append(tg)
BM=[[Bcols[j][i] for j in range(5)] for i in range(5)]
try:
 BMp=[[evpoly(x) for x in row] for row in BM]
 scale_values=[ev(x) for x in scales]
 if not all(scale_values):raise FixedPointIneligible('integer column scale not a p-unit at fixed point')
except FixedPointIneligible as err:
 say('new_integer_original_matrix_defined_but_fixed_point_ineligible',
     reason=str(err),p=P,point=list(POINT),noPointChange=True,
     nonzeroNotCertified=True,statistics=STAT)
 raise SystemExit(0)
Aaug=[BMp[i][:]+[int(i==j) for j in range(5)] for i in range(5)]
detp=1
for jcol in range(5):
 pvt=next((i for i in range(jcol,5) if Aaug[i][jcol]),None)
 assert pvt is not None
 if pvt!=jcol:Aaug[jcol],Aaug[pvt]=Aaug[pvt],Aaug[jcol];detp=-detp%P
 z=Aaug[jcol][jcol];detp=detp*z%P;iz=pow(z,P-2,P)
 assert z*iz%P==1
 Aaug[jcol]=[x*iz%P for x in Aaug[jcol]]
 for i in range(5):
  if i==jcol:continue
  c=Aaug[i][jcol]
  if c:Aaug[i]=[(a-c*b)%P for a,b in zip(Aaug[i],Aaug[jcol])]
Inv=[row[5:] for row in Aaug]
for A0,B0 in ((BMp,Inv),(Inv,BMp)):
 for i in range(5):
  for jcol in range(5):
   assert sum(A0[i][k]*B0[k][jcol] for k in range(5))%P==int(i==jcol)
   STAT['modularInverseCoordinates']+=1
assert detp%P
def determinant_degree_bound(coordinate):
 best=None;bestperm=None
 for perm in permutations(range(5)):
  vals=[];valid=True
  for i,jcol in enumerate(perm):
   a=BM[i][jcol]
   if not a:valid=False;break
   vals.append(int(a.total_degree()) if coordinate is None else int(a.degrees()[coordinate]))
  if valid and (best is None or sum(vals)>best):
   best=sum(vals);bestperm=list(perm)
 assert best is not None
 return {'upperBound':best,'maxWeightPerfectMatching':bestperm}
say('new_global_B2_nonzero_five_by_five_original_weight_support',
    p=P,point=list(POINT),determinantModuloP=detp%P,
    integerMatrixProfile=matrix_profile([[R(x) for x in row] for row in BM]),
    selectedColumnScales=[rp(x) for x in scales],
    originalThreeMultiplierProfiles=[matrix_profile([tag]) for tag in fulltags],
    degreeBounds={'u':determinant_degree_bound(0),
                  'Q':determinant_degree_bound(1),
                  'total':determinant_degree_bound(None)},
    determinantDefinition='F(u,Q)=det(B(u,Q)); B is the exact five integer polynomial original columns',
    universalOriginalIdentity='basis^T B_j=sum_r Omega[r,j]*RAW[r]; B adj(B)e0=F e0',
    entirePureWeightZeroSetRetained=True,
    originalSecondHeadAllPaidWeightChartsIncluded=True,
    noExpandedQQDeterminant=True,noFreeFiveAlgebraAssumed=True,
    noWholeSecondHeadExclusion=True,
    statistics=STAT)
