#!/usr/bin/env python3
"""Whole current W: new monic T4 / original mean F2 eight-column input.
Coefficient variables are (e,k,lambda); geometric symbols F,S=T-2lambda
are reduced at once in the actual monic tower. No B239 or lambda-3/2 inverse.
Original Gram/weighted rows, new R4, D, and true multiplications are returned.
Only the small frozen original-Gram prefix is regenerated, not any old gate.
180 seconds / 4 GiB. No complete-system exclusion is claimed by this build.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
dependency=Path(__file__).with_name('2026-11-27-unit211-generic-LS-W-four-S-free-original-cubics-and-binary-head-8542.py')
raw=dependency.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='00c08b48852bc8c38041a617d616922c94b6ab0e6f66c393a7e679949b44568e'
marker=b'\nM=l*(2*u-l*Q)-u*u\nunits='
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
ns={'__file__':str(dependency),'__name__':'__same_original_Gram_prefix_for_new_monic_tower__'}
log=io.StringIO()
with contextlib.redirect_stdout(log):exec(compile(prefix,str(dependency),'exec'),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
ctx=fmpq_mpoly_ctx.get(('e','k','lambda'),'lex')
ep,kp,lp=ctx.gens();zero=ctx.constant(0);one=ctx.constant(1)
def poly(x):return x if hasattr(x,'to_dict') else ctx.constant(x)
class C:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,C):self.n=n.n;self.d=n.d;return
  n=poly(n);d=one if d is None else poly(d);assert d
  if not n:self.n=zero;self.d=one;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __neg__(self):return C(-self.n,self.d,False)
 def __add__(self,v):
  v=C(v)
  if not self:return v
  if not v:return self
  g=self.d.gcd(v.d);a=self.d/g;b=v.d/g
  return C(self.n*b+v.n*a,a*v.d)
 __radd__=__add__
 def __sub__(self,v):return self+-C(v)
 def __rsub__(self,v):return C(v)+-self
 def __mul__(self,v):
  v=C(v)
  if not self or not v:return C()
  g=self.n.gcd(v.d);h=v.n.gcd(self.d)
  return C((self.n/g)*(v.n/h),(self.d/h)*(v.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,v):v=C(v);assert v;return self*C(v.d,v.n,False)
 def __rtruediv__(self,v):return C(v)/self
 def __pow__(self,n):
  return C(self.d**(-n),self.n**(-n),False) if n<0 else C(self.n**n,self.d**n,False)
 def __eq__(self,v):v=C(v);return self.n*v.d==v.n*self.d
 def data(self):
  return dict(n=[[list(map(int,m)),str(c)] for m,c in sorted(self.n.to_dict().items())],
              d=[[list(map(int,m)),str(c)] for m,c in sorted(self.d.to_dict().items())])
class P:
 def __init__(self,v=0):
  if isinstance(v,P):self.t=v.t.copy();return
  cf=C(v);self.t={(0,0):cf} if cf else {}
 @staticmethod
 def monomial(mm,c=1):
  pp=P();c=C(c)
  if c:pp.t[tuple(mm)]=c
  return pp
 def __bool__(self):return bool(self.t)
 def __neg__(self):
  pp=P();pp.t={m:-c for m,c in self.t.items()};return pp
 def __add__(self,v):
  v=P(v);pp=P(self)
  for m,c in v.t.items():
   z=pp.t.get(m,C())+c
   if z:pp.t[m]=z
   elif m in pp.t:del pp.t[m]
  return pp
 __radd__=__add__
 def __sub__(self,v):return self+-P(v)
 def __rsub__(self,v):return P(v)+-self
 def __mul__(self,v):
  v=P(v);pp=P()
  for ma,ca in self.t.items():
   for mb,cb in v.t.items():
    m=(ma[0]+mb[0],ma[1]+mb[1]);z=pp.t.get(m,C())+ca*cb
    if z:pp.t[m]=z
    elif m in pp.t:del pp.t[m]
  return pp
 __rmul__=__mul__
 def scale(self,c):
  c=C(c);pp=P();pp.t={m:v*c for m,v in self.t.items() if v*c};return pp
 def __pow__(self,n):
  pp=P(1)
  for _ in range(n):pp=pp*self
  return pp
 def __eq__(self,v):return not(self-P(v))
 def data(self):return [[list(m),c.data()] for m,c in sorted(self.t.items())]
 def degree(self):return max((sum(m) for m in self.t),default=-1)
def oldscalar(po):
 out=zero
 for mm,cf in po.to_dict().items():
  assert all(mm[j]==0 for j in [2,4,5,6,7])
  out+=cf*ep**int(mm[0])*kp**int(mm[1])*lp**int(mm[3])
 return out
def scalar(v):
 v=ns['R'](v);return C(oldscalar(v.n),oldscalar(v.d))
def convert(v):
 v=ns['R'](v);den=oldscalar(v.d);groups={}
 for mm,cf in v.n.to_dict().items():
  assert all(mm[j]==0 for j in [5,6,7])
  mon=(int(mm[2]),int(mm[4]))
  groups[mon]=groups.get(mon,zero)+cf*ep**int(mm[0])*kp**int(mm[1])*lp**int(mm[3])
 out=P()
 for mon,num in groups.items():out+=P.monomial(mon,C(num,den))
 return out
oldctx=ns['ctx'];oldgens=oldctx.gens()
def embedcoef(v):
 def pp(po):
  out=oldctx.constant(0)
  for mm,cf in po.to_dict().items():
   out+=cf*oldgens[0]**int(mm[0])*oldgens[1]**int(mm[1])*oldgens[3]**int(mm[2])
  return out
 return ns['R'](pp(v.n),pp(v.d))
def embed(pp):
 return sum((embedcoef(cf)*ns['R'](oldgens[2])**mm[0]*ns['R'](oldgens[4])**mm[1]
             for mm,cf in pp.t.items()),ns['R']())
e,k,u,Q,ell,M,Phi,P02,bc,J,T0,Pf=[scalar(ns[name]) for name in ['e','k','u','Q','l','M','Phi','P02','bc','J','T0','Pf']]
d=1-Q;m=u-ell;lam=C(lp);F=P.monomial((1,0));S=P.monomial((0,1));T=S+P(2*lam)
assert M==ell*ell*d-m*m and 2*e*(J-u*Q)==u*Q*Phi
assert Phi*(J-2*u*Q)==Pf
paid_atoms=[ep,kp,(e+1).n,Q.n,(1-Q).n,scalar(ns['Vbar']).n,
            ell.n,m.n,M.n,Phi.n,P02.n,bc.n]
den_seen=set()
def paid(v):
 v=C(v);key=str(v.d)
 if key in den_seen:return True
 assert all(mm[2]==0 for mm in v.d.to_dict()),'geometric lambda denominator'
 rest=v.d
 for atom in paid_atoms:
  while rest:
   g=rest.gcd(atom)
   if g.total_degree()==0:break
   q=rest/g;assert q*g==rest;rest=q
 assert rest.total_degree()==0,'unpaid scalar denominator'
 den_seen.add(key);return True
def ppaid(pp):
 for cf in pp.t.values():assert paid(cf)
def profile(pp):
 pp=P(pp);data=pp.data();bb=json.dumps(data,separators=(',',':')).encode()
 nums=[c.n for c in pp.t.values()];dens=[c.d for c in pp.t.values()]
 return dict(FSDegree=pp.degree(),monomials=len(pp.t),numeratorMaxDegrees=[max((int(z.degrees()[j]) for z in nums),default=-1) for j in range(3)],denominatorMaxDegrees=[max((int(z.degrees()[j]) for z in dens),default=-1) for j in range(3)],numeratorTerms=sum(len(z.to_dict()) for z in nums),bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest())
original={name:convert(ns['symbolic'][name]) for name in ['E1','EBe','EBo','N1','NS','PS']}
for name,po in original.items():
 assert embed(po)==ns['symbolic'][name];ppaid(po)
assert embed(T)==ns['T'] and embed(P(lam))==ns['lam']
L=original['EBe'].scale(m)+original['EBo'].scale(ell*d)
hF=u*u*m*d*Phi/(e*M)
assert L.t.get((2,0),C())==hF and hF
assert paid(hF) and paid(1/hF)
qF=L.scale(1/hF);assert qF.t.get((2,0),C())==1
assert all(mm[0]<=1 for mm in qF.t if mm!=(2,0))
assert qF.degree()==2;ppaid(qF)
Al=2*lam*lam-2*lam+1;Bl=4*lam**3-6*lam*lam+3*lam-1
c=3-2*lam;astar=4*u*Q-J;cstar=astar*m*m+J*d*ell*ell
D=P(ell*Al)-T*T;K=P(ell*ell*Bl)-T.scale(3*ell*Al)+2*T**3
ad=P(M*ell*ell*Q*(3-4*lam))+(T*T).scale(M*astar)+T.scale(2*M*u*Q*c*ell)+D.scale(cstar)
bd=(T.scale(astar)+P(u*Q*c*ell)).scale(2*M*m)
R4=(ad*ad).scale(M)-D*bd*bd
C4=(D*ad).scale(2*m)+K*bd
alpha2=-2*ell*Al-M*(3-4*lam)/(4*u*d)
alpha1=M*(astar*Bl-u*Q*c*Al)/(4*u*Q*d)
alpha0=cstar*Al*Al/(4*u*Q*d)+M*ell*((3-4*lam)*Al+u*c*Bl)/(4*u*d)
qT=T**4+(T*T).scale(alpha2)+T.scale(alpha1)+P(alpha0)
assert qT==C4.scale(1/(8*m*u*Q*ell*ell*d))
assert qT.t.get((0,4),C())==1 and all(mm[0]==0 for mm in qT.t)
assert qT.degree()==4
ppaid(qT);ppaid(R4)
say(stage='new_W_actual_monic_T4_F2_same_original_input',
 originalFrozenPrefixSHA256=hashlib.sha256(prefix).hexdigest(),
 originalPrefixLogSHA256=hashlib.sha256(log.getvalue().encode()).hexdigest(),
 allSixOriginalGramCoefficientEmbeddingsActuallyVerified=True,
 fullOriginalMonicF2IdentityActuallyReturned=True,
 monicF2Leading='u^2*(u-ell)*d*Phi/(e*M)',
 explicitMonicT4OriginalC4IdentityActuallyReturned=True,
 basisCoordinate='S=T-2lambda; qT remains monic S^4',
 qF=profile(qF),qT=profile(qT),R4=profile(R4),
 noB239OrD27HeadInverseUsed=True,noLambdaThreeHalvesInverseUsed=True,
 noPhysicalDOrNormInverse=True,claimExcluded=False)
basis=[(0,j) for j in range(4)]+[(1,j) for j in range(4)]
bp=[P.monomial(mm) for mm in basis]
def reduce_original(pp):
 original=P(pp);rem=P(pp);tf=P();tt=P()
 while any(mm[0]>=2 for mm in rem.t):
  mm=max((v for v in rem.t if v[0]>=2),key=lambda x:(x[0],x[1]))
  cf=rem.t[mm];term=P.monomial((mm[0]-2,mm[1]),cf)
  rem=rem-term*qF;tf=tf+term
 while any(mm[1]>=4 for mm in rem.t):
  mm=max((v for v in rem.t if v[1]>=4),key=lambda x:(x[1],x[0]))
  cf=rem.t[mm];term=P.monomial((mm[0],mm[1]-4),cf)
  rem=rem-term*qT;tt=tt+term
 assert rem+tf*qF+tt*qT==original
 assert all(mm in basis for mm in rem.t)
 for rr in [rem,tf,tt]:ppaid(rr)
 row=[rem.t.get(mm,C()) for mm in basis]
 return row,tf,tt
def rowpoly(row):return sum((bp[j].scale(row[j]) for j in range(8)),P())
def digest_parts(parts):
 h=hashlib.sha256();n=0
 for po in parts:
  bb=json.dumps(po.data(),separators=(',',':')).encode();h.update(bb);h.update(b'\n');n+=len(bb)+1
 return dict(bytes=n,sha256=h.hexdigest(),encoding='successive compact polynomial JSON followed by newline')
pointrows=[];rowlabels=[]
for name,pp in [(n,original[n]) for n in ['E1','EBe','N1','NS','PS']]+[('original_Delta_second_moment_R4',R4)]:
 begin=time.perf_counter();row,tf,tt=reduce_original(pp)
 assert rowpoly(row)+tf*qF+tt*qT==pp
 pointrows.append(row);rowlabels.append(name)
 say(stage='new_W_original_eight_column_row_return',name=name,remainder=profile(rowpoly(row)),
     allOriginalCoefficientProductsActuallyVerified=True,
     monicRulesHavePublishedCompleteOriginalMomentDeltaAndMeanTraces=True,
     noSaturationOrNormInverse=True,certificate=digest_parts([rowpoly(row),tf,tt]),
     rowSeconds=time.perf_counter()-begin,claimExcluded=False)
assert original['EBo']==(qF.scale(hF)-original['EBe'].scale(m)).scale(1/(ell*d))
maps=[]
for variable,name in [(F,'F'),(S,'S')]:
 mat=[]
 for i,bp0 in enumerate(bp):
  row,tf,tt=reduce_original(bp0*variable)
  assert rowpoly(row)+tf*qF+tt*qT==bp0*variable
  mat.append(row)
 maps.append(mat)
 say(stage='new_W_eight_generator_actual_original_multiplication',variable=name,
     allEightProductsActuallyReturned=True,
     matrixCertificate=digest_parts([rowpoly(row) for row in mat]),
     ambientMonicTowerFreeButFinalOriginalQuotientNotClaimedFree=True,claimExcluded=False)
# True ambient multiplication columns already establish the commuting algebra.
# Do not add a duplicate expanded 64-entry commutator audit as a result gate.
unit_profiles=[]
for name,pp in [('physical_D',D),('lambda',P(lam)),('centered_S',S)]:
 row,tf,tt=reduce_original(pp)
 assert rowpoly(row)+tf*qF+tt*qT==pp
 unit_profiles.append(dict(name=name,returned=profile(rowpoly(row)),inverseNotTaken=True))
certificate=digest_parts([rowpoly(r) for r in pointrows]+[rowpoly(r) for ma in maps for r in ma])
signal.alarm(0)
say(stage='new_W_global_monic_T4_F2_eight_column_original_input_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 scalarVariables=['e','k','lambda'],actualBasis=['1','S','S^2','S^3','F','F*S','F*S^2','F*S^3'],
 originalRowLabels=rowlabels,allSixRowsHaveCompleteOriginalQuotientTraceProducts=True,
 allSixteenTrueMultiplicationColumnsActuallyVerified=True,
 allFinalScalarDenominatorsActuallyPaid=True,checkedDistinctDenominators=len(den_seen),
 lambdaThreeHalvesEntireFiberRetained=True,physicalUnitRepresentations=unit_profiles,
 newInputUsesOriginalValueQuarticNotOnlyOldGram=True,coefficientCertificate=certificate,
 bigMatrixCacheWritten=False,noParameterCofactorYetComputed=True,
 completeIndividualValueNPRowsStillRequired=True,fullOriginalSystemExcluded=False,
 claimExcluded=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
