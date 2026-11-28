#!/usr/bin/env python3
"""NEW correct Phi f=u: fixed original 12-coordinate / 24-column container.
The monic Q-cubic Psi is already an original necessary relation.
Only its same-point original rows are new here: E,O,N and y multiples,
NS,PS, each times 1,Q,Q^2.  No old cofactor, GB, y-head or norm inverse.
The y<=3 container is NOT asserted to be a quotient algebra.
120 seconds / 1 GiB; small output; every new identity is multiplied back.
"""
import hashlib,json,math,os,pathlib,resource,signal,time
from flint import fmpq_poly
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
_RAW_ALARM=signal.alarm
def bounded_alarm(seconds):
 if seconds<=0:return _RAW_ALARM(0)
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120 second boundary')
 return _RAW_ALARM(max(1,min(int(seconds),math.ceil(DEADLINE-time.perf_counter()))))
signal.alarm=bounded_alarm;signal.alarm(120)
BASENAME='2026-11-28-unit211-Phi-zero-true-fu-single-y-original-scalar-cofactors-8542.py'
BASE_SHA='9d591ab41ed41cc7dbee8ac3e9ce326ef68348455751ae9ad1cea954a7d463cb'
path=pathlib.Path(__file__).with_name(BASENAME)
if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/BASENAME
full=path.read_text();assert hashlib.sha256(full.encode()).hexdigest()==BASE_SHA
MARKER='def det(a):';assert full.count(MARKER)==1
prefix=full[:full.index(MARKER)]
env={'__name__':'isp_fu_original_rows_only','__file__':str(path),
     'print':lambda *a,**kw:None}
exec(compile(prefix,str(path)+'#necessary_original_definitions','exec'),env)
signal.alarm=bounded_alarm;signal.alarm(120)
ctx=env['ctx'];up,Qp,yp,Tp,zp=ctx.gens()
zeroP=ctx.constant(0);oneP=ctx.constant(1)
R=env['R'];prepared=env['prepared'];original=env['original']
input_scales=env['input_scales'];paid=env['paid']
assert len(prepared)==len(original)==len(input_scales)==5
Psi=(Qp**3+(-10*up**2+24*up-15)*Qp**2
 +(32*up**4-152*up**3+276*up**2-228*up+72)*Qp
 -32*up**6+224*up**5-672*up**4+1104*up**3-1040*up**2+528*up-112)
old_target=Psi/4
assert hashlib.sha256(str(sorted(old_target.to_dict().items())).encode()).hexdigest()=='73bbd9835fce4caa3b26b90c7dd4e413a888e4967f5ea675bb8a16594f682223'
# Psi's original ideal source was established in the preceding successful
# fixed-cofactor result.  This input does not rerun those three cofactors.
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute boundary')
P0=fmpq_poly([]);P1=fmpq_poly([1]);stats={'exactPolynomialDivisions':0,
 'QMonicShortDivisions':0,'QShortDivisionSteps':0,'containerCoordinateReturns':0,
 'seedCoordinateReturns':0,'edgeCoordinateReturns':0,
 'zeroEdgeCoordinateReturns':0,'targetCoordinateReturns':0}
def ex(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 stats['exactPolynomialDivisions']+=1;return q
def lc(p):assert p;return p[int(p.degree())]
def monic(p):return p/lc(p) if p else p
def plcm(a,b):
 if not a or not b:return P0
 return monic(ex(a,a.gcd(b))*b)
def pinfo(p):
 out={'degree':int(p.degree()),'sha256':hashlib.sha256(str(p).encode()).hexdigest()}
 if p and int(p.degree())<=14:out['polynomial']=str(p)
 return out
def pure_u(p):return all(not any(e[1:]) for e in p.to_dict())
def univar(p):
 assert pure_u(p)
 d=max((int(e[0]) for e in p.to_dict()),default=-1)
 return fmpq_poly([p.to_dict().get((j,0,0,0,0),0) for j in range(d+1)])
def multivar(p):
 return ctx.from_dict({(j,0,0,0,0):p[j] for j in range(int(p.degree())+1) if p[j]})
def qdegree(p):return max((int(e[1]) for e in p.to_dict()),default=-1)
def qcoeff(p,d):
 return ctx.from_dict({(e[0],0,e[2],e[3],e[4]):v
                       for e,v in p.to_dict().items() if int(e[1])==d})
assert qdegree(Psi)==3 and qcoeff(Psi,3)==oneP
def qreduce(p):
 rem=p;quot=zeroP
 while rem and qdegree(rem)>=3:
  tick();d=qdegree(rem);term=qcoeff(rem,d)*Qp**(d-3)
  rem=rem-term*Psi;quot+=term
  stats['QShortDivisionSteps']+=1
 assert p==quot*Psi+rem and qdegree(rem)<3
 stats['QMonicShortDivisions']+=1
 return rem,quot
DIM=12
def flatten(p):
 assert all(e[1]<3 and e[2]<4 and not e[3] and not e[4] for e in p.to_dict())
 entries=[]
 for j in range(4):
  for k in range(3):
   pp=ctx.from_dict({(e[0],0,0,0,0):a for e,a in p.to_dict().items()
                     if int(e[1])==k and int(e[2])==j})
   entries.append(univar(pp))
 back=sum((multivar(entries[3*j+k])*Qp**k*yp**j
           for j in range(4) for k in range(3)),zeroP)
 assert back==p
 stats['containerCoordinateReturns']+=DIM
 return entries
# No y^4 action or closure is assumed.  Each item is an actual polynomial
# multiple of one of the same five original values.
spec=[(0,0),(0,1),(1,0),(1,1),(2,0),(2,1),(3,0),(4,0)]
inputs=[];input_descriptions=[]
for row,shift in spec:
 for k in range(3):
  pp=Qp**k*yp**shift*prepared[row]
  rem,quot=qreduce(pp)
  v=flatten(rem)
  assert R(prepared[row])*input_scales[row]==original[row]
  inputs.append(v);input_descriptions.append((row,shift,k))
assert len(inputs)==24
say('new_fu_same_point_original_container',
 originalFullSourceSHA256=BASE_SHA,
 originalNecessaryPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest(),
 originalMonicPsiDegree=[6,3],
 originalInputColumns=24,coefficientCoordinates=DIM,
 basis='Q^i*y^j, 0<=i<3, 0<=j<4',
 exactOriginalColumnDefinitions=input_descriptions,
 onlyQQ_uModuleContainer=True,yQuotientAlgebraClaim=False,
 allQQPsiComponentsAndRepeatedFibersKept=True,
 noYHeadOrWeightNormInverse=True,oldCofactorAndGBExecuted=False,
 maximumInputUDegree=max(int(a.degree()) for v in inputs for a in v))
class Fr:
 def __init__(self,n=0,d=None):
  if isinstance(n,Fr):self.n=n.n;self.d=n.d;return
  n=n if isinstance(n,fmpq_poly) else fmpq_poly([n])
  d=P1 if d is None else d if isinstance(d,fmpq_poly) else fmpq_poly([d])
  assert d
  if not n:self.n=P0;self.d=P1;return
  g=n.gcd(d);n=ex(n,g);d=ex(d,g);c=lc(d)
  self.n=n/c;self.d=d/c
 def __bool__(self):return bool(self.n)
 def __neg__(self):return Fr(-self.n,self.d)
 def __add__(self,o):
  o=Fr(o);g=self.d.gcd(o.d);a=ex(self.d,g);b=ex(o.d,g)
  return Fr(self.n*b+o.n*a,a*o.d)
 __radd__=__add__
 def __sub__(self,o):return self+-Fr(o)
 def __rsub__(self,o):return Fr(o)+-self
 def __mul__(self,o):
  o=Fr(o)
  if not self or not o:return Fr()
  g=self.n.gcd(o.d);h=o.n.gcd(self.d)
  return Fr(ex(self.n,g)*ex(o.n,h),ex(self.d,h)*ex(o.d,g))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=Fr(o);assert o;return self*Fr(o.d,o.n)
 def __eq__(self,o):
  o=Fr(o);return self.n*o.d==o.n*self.d
def leading(v):return next((j for j,a in enumerate(v) if a),None)
def primitive(v):
 g=P0
 for a in v:
  g=g.gcd(a)
  if g and int(g.degree())==0:break
 assert g
 out=[ex(a,g) for a in v]
 assert all(g*out[j]==v[j] for j in range(DIM))
 return out,g
nodes=[];basis={}
def seed(index):
 raw=inputs[index]
 if not any(raw):return None
 v,g=primitive(raw)
 for j in range(DIM):assert g*v[j]==raw[j]
 stats['seedCoordinateReturns']+=DIM
 nodes.append({'v':v,'seed':index,'seed_scale':Fr(1,g),
               'parents':[],'depth':1})
 return len(nodes)-1
def cancel(current,pivot):
 old=nodes[current]['v'];pv=nodes[pivot]['v'];j=leading(old)
 assert j==leading(pv)
 a=old[j];b=pv[j]
 raw=[b*old[k]-a*pv[k] for k in range(DIM)]
 if not any(raw):
  assert all(b*old[k]==a*pv[k] for k in range(DIM))
  stats['zeroEdgeCoordinateReturns']+=DIM;return None
 v,g=primitive(raw)
 assert all(g*v[k]==b*old[k]-a*pv[k] for k in range(DIM))
 assert leading(v)>j
 stats['edgeCoordinateReturns']+=DIM
 nodes.append({'v':v,'seed':None,
  'parents':[(current,Fr(b,g)),(pivot,Fr(-a,g))],
  'depth':1+max(nodes[current]['depth'],nodes[pivot]['depth'])})
 return len(nodes)-1
for i in range(len(inputs)):
 tick();cur=seed(i)
 while cur is not None:
  j=leading(nodes[cur]['v'])
  if j not in basis:basis[j]=cur;break
  cur=cancel(cur,basis[j])
 say('new_fu_original_column_processed',originalColumn=i,
     actualQQ_uRank=len(basis),exactOriginalDAGNodes=len(nodes))
 # Once all 12 coordinate directions are in the original span, further
 # columns cannot improve the requested target.  This is the new module,
 # not a replay of any earlier Gaussian.
 if len(basis)==DIM:break
def reduce_target(v):
 rem=list(map(Fr,v));comb={}
 for j in sorted(basis):
  tick()
  if not rem[j]:continue
  n=basis[j];pv=nodes[n]['v'];c=rem[j]/Fr(pv[j])
  rem=[rem[k]-c*Fr(pv[k]) for k in range(DIM)]
  comb[n]=c
 for k in range(DIM):
  assert Fr(v[k])==rem[k]+sum((c*Fr(nodes[n]['v'][k]) for n,c in comb.items()),Fr())
 stats['targetCoordinateReturns']+=DIM
 return rem,comb
targets=[('one',flatten(oneP))]
Dphys=env['ell']*(2*env['lam']**2-2*env['lam']+1)-env['T']**2
assert env['supported'](Dphys.d)
Drem,Dquot=qreduce(Dphys.n)
targets.append(('physical_D_numerator',flatten(Drem)))
found=None;comb=None
for name,v in targets:
 rem,cc=reduce_target(v)
 success=not any(rem)
 say('new_fu_actual_original_target_return',
     target=name,allTwelveCoordinatesReturned=True,exactZeroRemainder=success,
     remainderNonzeroCoordinates=[j for j,a in enumerate(rem) if a],
     actualQQ_uRank=len(basis),
     physicalDInverted=False,yAlgebraClosureAssumed=False)
 if success:found=name;comb=cc;break
if found is None:
 say('new_fu_fixed_original_container_inconclusive',
     originalInputsUsed=i+1,actualQQ_uRank=len(basis),
     statistics=stats,wholeFuExcluded=False,
     wholePhiExcluded=False,ordinaryISPClaim=False)
else:
 reachable=set();stack=[n for n,c in comb.items() if c]
 while stack:
  n=stack.pop()
  if n in reachable:continue
  reachable.add(n);stack.extend(p for p,_ in nodes[n]['parents'])
 delta_u=P1
 for n,c in comb.items():
  if c:delta_u=plcm(delta_u,c.d)
 for n in reachable:
  node=nodes[n]
  if node['seed'] is not None:delta_u=plcm(delta_u,node['seed_scale'].d)
  for _,c in node['parents']:delta_u=plcm(delta_u,c.d)
 depth=max((nodes[n]['depth'] for n,c in comb.items() if c),default=0)+1
 assert delta_u
 for n,c in comb.items():
  if c:ex(delta_u,c.d)
 for n in reachable:
  node=nodes[n]
  if node['seed'] is not None:ex(delta_u,node['seed_scale'].d)
  for _,c in node['parents']:ex(delta_u,c.d)
 # Every DAG edge has at most one listed rational u denominator.
 # Induction on its actual depth gives delta_u^depth*target in the
 # original column module modulo the already-original Psi.
 retained,removed=env['strip_paid'](multivar(delta_u))
 C=univar(retained);assert C and multivar(C)*removed==multivar(delta_u)
 say('new_fu_original_same_point_weight_cover',
     target=found,actualQQ_uRank=len(basis),
     originalInputsUsed=i+1,reachableOriginalDAGNodes=len(reachable),
     denominatorLCM=pinfo(delta_u),retainedPureUCover=pinfo(C),
     coveringExponent=depth,
     identity='C(u)^N*target belongs to the original five-value ideal',
     sourceOfPsi='already-returned original fixed scalar cofactor',
     everyRawOriginalScaleOnlyPaid=True,
     allTerminalAndIntermediatePureUDenominatorsCovered=True,
     physicalTargetIdentity='Dval=ell*A2-T^2=bc*(h-k)^2 at original points',
     physicalDInverted=False,noYHeadInverted=True,noWeightNormInverted=True,
     allPureUCoverZeroFibersKept=True,
     differentUPointUpperBound=int(C.degree()),
     differentWeightPairUpperBound=3*int(C.degree()),
     completeOriginalPointFinitenessClaim=False,
     wholeFuExcluded=int(C.degree())==0,
     statistics=stats,wholePhiExcluded=False,ordinaryISPClaim=False)
 # Optional classification of this genuinely new cover, after its
 # complete original identity has already been reported.
 if 0<int(C.degree())<=120:
  const,factors=C.factor();prod=fmpq_poly([const]);rad=P1;power=0
  profiles=[]
  for p,e in factors:
   e=int(e);prod*=p**e;rad*=p;power=max(power,e)
   profiles.append({'factor':pinfo(p),'multiplicity':e})
  assert prod==C
  ex(rad**power,C)
  say('new_fu_exact_cover_support',
      factors=profiles,radical=pinfo(rad),maximumMultiplicity=power,
      factorProductAndRadicalPowerDivisionReturned=True,
      differentUPointUpperBound=int(rad.degree()),
      differentWeightPairUpperBound=3*int(rad.degree()),
      allCoverFibersKept=True,completeOriginalPointFinitenessClaim=False)
