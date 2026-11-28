#!/usr/bin/env python3
"""NEW corrected Phi B2, complete true E1/N1 t resultant and five raw columns.
Full E1 has paid t2 head; N1-2(u-1)E1 is genuinely t-linear.
Construct their SAME-t norm with both original multipliers returned, without
a linear-head inverse. Reduce its five basis multiples only by the already
proved four cubic/head and sigma2 DEFINITIONS. Every new ordinary column
returns to E2/E3/completeNV/trueE1/completeN1.
Fixed p1009 point (2,2), no new point search or selected old commutator.
If the new integer 5x5 matrix is invertible there, universal adjugate defines
a second nonzero pure-weight necessary support. No QQ det expansion/gcd.
No old actions, commutators, DAG selection, 20/8/6-column or sigma-scalar
proof gate; no physical D inverse. Entire new weight zero set retained.
Self-contained, 120 seconds /1 GiB, outer135; no retries or budget extension.
"""
import hashlib,json,math,resource,signal,time
from itertools import permutations
from flint import fmpq_mpoly_ctx
START=time.perf_counter();DEADLINE=START+120;P=1009;POINT=(2,2)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
STAT={'exactPolynomialProducts':0,'oldPaidDenominatorChecks':0,
      'ordinaryNormalFormReturns':0,'newOriginalQuadraticAndLinearReturns':0,
      'newTwoOriginalNormReturns':0,'newFiveOriginalColumns':0,
      'integerColumnReturns':0,'modularInverseCoordinates':0}
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute120')
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True,separators=(',',':')),flush=True)
ctx=fmpq_mpoly_ctx.get(('u','Q','lambda','sigma','t'),'lex')
up,Qp,lp,zp,tp=ctx.gens();ONE=ctx.constant(1);ZERO=ctx.constant(0)
def poly(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
def pp(v):
 v=poly(v);d=v.to_dict()
 return {'degrees':list(map(int,v.degrees())) if v else [-1]*5,
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

def pureweight(p):return all(not any(map(int,e[2:])) for e in p.to_dict())
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
 return max((sum(map(int,e[2:])) for e in v.n.to_dict()),default=-1)
def geo(v):
 v=oldpaid(v);groups={}
 for ex,c in v.n.to_dict().items():
  assert not int(ex[4])
  key=(int(ex[2]),int(ex[3]));ee=(int(ex[0]),int(ex[1]),0,0,0)
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


u,Q,lam,sigma,t=map(R,(up,Qp,lp,zp,tp))
s=u-1;delta=1-Q;Kw=Q+4*s;L=Q-2*s*(u-2);ell=L/Q;m=u-ell
T0=-Kw;J=Q-4*s*s;P02=2*s*L;theta=u-ell*Q
Lp=Qp-2*(up-1)*(up-2)
Mnp=2*up*Lp-Lp*Lp-up*up*Qp
M=R(Mnp)/Q;bc=M/(4*delta)
PAID=Qp*(Qp-1)*(up-1)*(Qp+4*(up-1))*Lp*Mnp*(up*Qp-Lp)*(3*Qp-2*Lp)
a=lam-R(3)/2;j=ell*(lam-R(1)/2)-m*sigma
Tm=j-ell;w=lam-1-Tm;E=P02*j/T0
f=(P02*lam-Q*E+s*T0)/(J-Q)
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1
E2=ell*a*a-2*m*a*sigma+ell*delta*sigma*sigma-A2
E3=ell*a**3-3*m*a*a*sigma+3*ell*delta*a*sigma*sigma-m*delta*sigma**3-B3
rr=lam*lam+lam-R(3)/4-delta*sigma*sigma
Nsharp=2*(-rr*f+(a*a-delta*sigma*sigma)*E-w*(u*a+theta*sigma))
NV=Nsharp-2*f*E2
RAW=[E2,E3,NV]
for v in RAW:oldpaid(v)
# Only necessary definitions of the paid five-generator reduction.
# No old 4x4 determinant/32 inverse coordinates, 10 actions, defects,
# point selection, old integer matrix, old support or old degree test.
MON3=[(3,0),(2,1),(1,2),(0,3)]
polys=[lam*E2,sigma*E2,E3,NV]
ptags=[[lam,R(),R()],[sigma,R(),R()],[R(),R(1),R()],[R(),R(),R(1)]]
H=[[geo(polys[c]).get(MON3[r],R()) for c in range(4)] for r in range(4)]
head=2*P02*m*delta*(3-2*ell)
HI=[]
for i in range(4):
 row=[]
 for jcol in range(4):
  minor=[[H[r][c] for c in range(4) if c!=i] for r in range(4) if r!=jcol]
  row.append(oldpaid(R((-1)**(i+jcol))*ddet(minor)/head))
 HI.append(row)
rules=[];rule_tags=[]
for jcol,(aa,bb) in enumerate(MON3):
 tg=[sumR(HI[i][jcol]*ptags[i][r] for i in range(4)) for r in range(3)]
 low=lam**aa*sigma**bb-rawsum(tg)
 assert gd(low)<=2
 rules.append(low);rule_tags.append(tg)
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

# New ordinary true Gram E1 and N1, with full t dependence kept.
# Equations are the complete dual-germ identities, not highest parts.
a0=1-ell;V0=f-E;W1=T0/2+2*u*f;V2=2*u-ell*Q
x0=(theta*V0-m*W1)/M;y0=(ell*W1-u*V0)/M
x=x0+theta*t/(4*delta);y=y0-u*t/(4*delta)
A1=2*E;d10=f+E-a0*u;d1=d10-bc*t
Wr=W1-a0*V2-2*bc*t
S1=ell*(x*x+delta*y*y)+2*m*x*y-a0*W1-2*bc*t*x
SD=m*(x*x+delta*y*y)+2*ell*delta*x*y-a0*(theta*x+u*delta*y)-2*bc*delta*t*y
S2=S1+SD
PCROSS=2*x-2*delta*y-2*a0*Q-u*t
E1=2*Wr-2*u*A1-2*S1+4*(f-u)*d1
N1=(4*S2-4*f*Wr-4*u*(u*A1+S1)-4*d1*W1+8*f*u*d1
    +2*A1*V2+2*bc*t*PCROSS-4*lam*w*P02)
S10=ell*(x0*x0+delta*y0*y0)+2*m*x0*y0-a0*W1
SD0=m*(x0*x0+delta*y0*y0)+2*ell*delta*x0*y0-a0*(theta*x0+u*delta*y0)
S20=S10+SD0
aE=-bc*ell*Q/(2*delta)
bE=4*bc*(y0-f+s)
cE=2*(W1-a0*V2)-4*u*E-2*S10+4*(f-u)*d10
aN=(4*(S20-S10)-4*(f+s)*(W1-a0*V2)
    +(-4*W1+8*f+8*s*u)*d10-4*ell*Q*E-4*lam*w*P02)
bN=4*bc*(W1-x0-delta*y0-2*s*s)
assert E1==aE*t*t+bE*t+cE
assert N1-2*s*E1==aN+bN*t
assert gd(E1)<=2 and gd(N1)<=2
assert gd(aN)<=2 and gd(bN)<=1
for v in [1/aE,E1,N1,aN,bN,bE,cE]:oldpaid(v)
STAT['newOriginalQuadraticAndLinearReturns']+=2
q1=bE/aE;q0=cE/aE
qE=t*t+q1*t+q0
assert qE==E1/aE
STAT['newOriginalQuadraticAndLinearReturns']+=1
norm=aN*aN-q1*aN*bN+q0*bN*bN
ON=aN-q1*bN-bN*t
OE=bN*bN/aE-2*s*ON
assert norm==OE*E1+ON*N1
assert all(not int(ex[4]) for ex in norm.n.to_dict())
assert gd(norm)<=4
for v in [norm,OE,ON]:oldpaid(v)
STAT['newTwoOriginalNormReturns']+=1
say('new_true_E1_N1_same_t_complete_norm_returned',
    scope='corrected Phi; specialize B2 without inverting its linear t coefficient',
    E1=rp(E1),N1=rp(N1),paidTQuadraticHead=rp(aE),
    linearN1Constant=rp(aN),linearN1Coefficient=rp(bN),
    sameTNorm=rp(norm),completeTwoOriginalMultipliers=[rp(OE),rp(ON)],
    noLinearHeadInverse=True,noNormSufficiencyClaim=True,
    statistics=STAT)
if not norm:
 say('new_true_E1_N1_norm_zero_original_fibers_retained',
     noNonzeroWeightSupportClaim=True,statistics=STAT)
 raise SystemExit(0)

# FIVE NEW VALUE COLUMNS, fixed and not selected from old commutators.
ORIGINAL=RAW+[E1,N1]
vectors=[];tags=[]
for bmon in BVAL:
 v,tg=normal(bmon*norm)
 full=[-tg[0],-tg[1],-tg[2],bmon*OE,bmon*ON]
 assert basis_poly(v)==sumR(full[i]*ORIGINAL[i] for i in range(5))
 for z in full:oldpaid(z)
 vectors.append(v);tags.append(full);STAT['newFiveOriginalColumns']+=1
say('new_same_t_value_norm_five_full_original_columns_returned',
    fixedMultipliers=['1','lambda','sigma','lambda^2','lambda*sigma'],
    vectorMatrix=matrix_profile([[vectors[j][i] for j in range(5)] for i in range(5)]),
    allFiveOriginalLabels=['E2','E3','complete_NV','true_E1','complete_N1'],
    noOldCommutatorOrPointSelectionReplayed=True,statistics=STAT)

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

# Each new column is integralized from its actual coefficients only.
Bcols=[];scales=[];scaledtags=[]
for v,tag in zip(vectors,tags):
 den=ONE
 for z in v:
  z=oldpaid(z);den=exact(den,den.gcd(z.d))*z.d
 oldpaid(R(1,den))
 col=[]
 for z in v:
  z=R(den)*z;assert z.d==ONE;col.append(z.n)
 k=common_integer_den(col);col=[z*k for z in col];content=0
 for z in col:
  for c in z.to_dict().values():
   aa,bb=rational_parts(c);assert bb==1;content=math.gcd(content,abs(aa))
 if not content:
  say('new_value_column_zero_no_determinant_certificate',
      column=len(Bcols),allOriginalFibersRetained=True,statistics=STAT)
  raise SystemExit(0)
 col=[z/content for z in col]
 gamma=R(den)*R(k)/content
 full=scaletag(gamma,tag)
 for i in range(5):
  assert R(col[i])==gamma*v[i] and pureweight(col[i])
  assert all(rational_parts(c)[1]==1 for c in col[i].to_dict().values())
 for z in full:oldpaid(z)
 assert sumR(R(col[i])*BVAL[i] for i in range(5))==sumR(full[i]*ORIGINAL[i] for i in range(5))
 Bcols.append(col);scales.append(gamma);scaledtags.append(full)
 STAT['integerColumnReturns']+=1
BM=[[Bcols[j][i] for j in range(5)] for i in range(5)]
try:
 paid_value=evpoly(PAID)
 if not paid_value:raise FixedPointIneligible('fixed old-paid point zero')
 BMp=[[evpoly(z) for z in row] for row in BM]
 scale_values=[ev(z) for z in scales]
 if not all(scale_values):raise FixedPointIneligible('new integer column scale not p-unit')
except FixedPointIneligible as err:
 say('new_same_t_norm_fixed_point_ineligible',
     p=P,point=list(POINT),reason=str(err),noPointChange=True,
     noNonzeroDeterminantClaim=True,statistics=STAT)
 raise SystemExit(0)
Aaug=[BMp[i][:]+[int(i==j) for j in range(5)] for i in range(5)]
detp=1;rank=0
for jcol in range(5):
 pvt=next((i for i in range(rank,5) if Aaug[i][jcol]),None)
 if pvt is None:continue
 if pvt!=rank:Aaug[rank],Aaug[pvt]=Aaug[pvt],Aaug[rank];detp=-detp%P
 pivot=Aaug[rank][jcol];detp=detp*pivot%P;ip=pow(pivot,P-2,P)
 assert pivot*ip%P==1
 Aaug[rank]=[z*ip%P for z in Aaug[rank]]
 for i in range(5):
  if i==rank:continue
  c=Aaug[i][jcol]
  if c:Aaug[i]=[(a-c*b)%P for a,b in zip(Aaug[i],Aaug[rank])]
 rank+=1
if rank<5:
 say('new_same_t_norm_fixed_five_matrix_rank_inconclusive',
     p=P,point=list(POINT),rank=rank,paidValue=paid_value,
     integerMatrixProfile=matrix_profile([[R(z) for z in row] for row in BM]),
     noPointChange=True,noNonzeroDeterminantClaim=True,
     allOriginalWeightFibersRetained=True,statistics=STAT)
 raise SystemExit(0)
Inv=[row[5:] for row in Aaug]
for A0,B0 in ((BMp,Inv),(Inv,BMp)):
 for i in range(5):
  for jcol in range(5):
   assert sum(A0[i][k]*B0[k][jcol] for k in range(5))%P==int(i==jcol)
   STAT['modularInverseCoordinates']+=1
assert detp%P
def determinant_degree_bound(coordinate):
 best=None;witness=None
 for perm in permutations(range(5)):
  if any(not BM[i][j] for i,j in enumerate(perm)):continue
  weight=sum(int(BM[i][j].total_degree()) if coordinate is None
             else int(BM[i][j].degrees()[coordinate]) for i,j in enumerate(perm))
  if best is None or weight>best:best=weight;witness=list(perm)
 assert best is not None
 return {'upperBound':best,'maxWeightPerfectMatching':witness}
say('new_same_t_E1_N1_five_original_nonzero_weight_support',
    p=P,point=list(POINT),rank=rank,paidValue=paid_value,determinantModuloP=detp%P,
    integerMatrixProfile=matrix_profile([[R(z) for z in row] for row in BM]),
    actualIntegerColumnScales=[rp(z) for z in scales],
    allFiveOriginalMultiplierProfiles=[matrix_profile([tag]) for tag in scaledtags],
    degreeBounds={'u':determinant_degree_bound(0),'Q':determinant_degree_bound(1),
                  'total':determinant_degree_bound(None)},
    determinantDefinition='Gwt=det(Bnew); fixed columns normal(basis_j*Norm_t(E1,N1)) with exact five-original tags',
    universalOriginalIdentity='basis Bnew_j=sum_r Omega[r,j] ORIGINAL_r; Bnew adj(Bnew)e0=Gwt e0',
    newWeightZeroSetEntirelyRetained=True,noExpandedQQDeterminant=True,
    noOldWeightSupportOrGcdRecomputed=True,noWholeB2Exclusion=True,
    noNormCommonRootSufficiencyClaim=True,statistics=STAT)
