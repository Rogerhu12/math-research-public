#!/usr/bin/env python3
"""NEW corrected whole Phi B: exact QQ(x)[lambda]^2 module and positive
powers of the actual original unit lambda*t*Dval.  No D inverse.
Only the already defined I6 input prefix is constructed; no former scalar
cofactor, selected-head computation, or frozen gate is executed.
120 seconds / 1 GiB, one absolute deadline, small summaries only.
"""
import hashlib,json,math,os,pathlib,resource,signal,time
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
_RAW_ALARM=signal.alarm
def bounded_alarm(seconds):
 if seconds<=0:return _RAW_ALARM(0)
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120 second boundary')
 return _RAW_ALARM(max(1,min(int(seconds),math.ceil(DEADLINE-time.perf_counter()))))
signal.alarm=bounded_alarm;signal.alarm(120)
BASENAME='2026-11-28-unit211-Phi-zero-true-Bzero-whole-I6-twelve-by-two-8542.py'
BASE_SHA='b802d6c9b7a46b544f1fd5f814b05337a552f938a660b8d047fe4e62ff4eae56'
path=pathlib.Path(__file__).with_name(BASENAME)
if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/BASENAME
full=path.read_text();assert hashlib.sha256(full.encode()).hexdigest()==BASE_SHA
MARKER='def deg(v):'
assert full.count(MARKER)==1
prefix=full[:full.index(MARKER)]
ns={'__name__':'isp_true_B_I6_necessary_input','__file__':str(path),'print':lambda *a,**k:None}
exec(compile(prefix,str(path),'exec'),ns)
signal.alarm=bounded_alarm;signal.alarm(120)
R=ns['R'];ctx=ns['ctx'];up,Qp,Lp,Tp,zp=ctx.gens()
zeroP=ctx.constant(0);oneP=ctx.constant(1)
univar=ns['univar'];lam=ns['lam']
inputs=ns['twelve'];qw=ns['qw'];that=ns['that'];paid=ns['paid']
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
def check_time():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('new original module 120 second boundary')
def pure_x(p):return all(not any(e[1:]) for e in p.to_dict())
def allowed(p):return all(e[1]==e[3]==e[4]==0 for e in p.to_dict())
stats={'fullPolynomialDivisions':0,'seedCoordinateReturns':0,
       'edgeCoordinateReturns':0,'zeroRowCoordinateReturns':0,
       'targetCoordinateReturns':0,'originalOmegaShortDivisions':0}
def exact(a,b):
 q,r=divmod(a,b)
 assert not r and q*b==a
 stats['fullPolynomialDivisions']+=1
 return q
def degree(p):return max((int(e[2]) for e in p.to_dict()),default=-1)
def coeff(p,n):
 return ctx.from_dict({(e[0],0,0,0,0):a for e,a in p.to_dict().items() if int(e[2])==n})
def leading(v):
 return max((degree(p),i) for i,p in enumerate(v))
def profile(p):
 return {'degrees':list(map(int,p.degrees())) if p else [-1]*5,
         'terms':len(p.to_dict()),
         'sha256':hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest()}
def p_lcm(a,b):
 assert pure_x(a) and pure_x(b) and a and b
 return exact(a,a.gcd(b))*b
def primitive(v):
 assert len(v)==2 and all(allowed(p) for p in v)
 if not any(v):return None,None
 g=zeroP
 for p in v:
  for j in range(degree(p)+1):
   a=coeff(p,j)
   if a:g=g.gcd(a)
   if g and int(g.total_degree())==0:break
  if g and int(g.total_degree())==0:break
 assert g and pure_x(g)
 d,j=leading(v);lc=univar(coeff(v[j],d))
 scalar=lc[int(lc.degree())]
 divisor=g*ctx.constant(scalar)
 out=[exact(p,divisor) for p in v]
 assert all(divisor*out[i]==v[i] for i in range(2))
 return out,divisor
nodes=[]
def seed(index,row):
 den=oneP
 for a in row:
  assert pure_x(a.d);den=p_lcm(den,a.d)
 raw=[a.n*exact(den,a.d) for a in row]
 if not any(raw):
  assert all(not a for a in row);return None
 v,g=primitive(raw);scale=R(den,g)
 for j in range(2):assert R(v[j])==scale*row[j]
 stats['seedCoordinateReturns']+=2
 node={'v':v,'seed':index,'seed_scale':scale,'parents':[],'depth':1}
 nodes.append(node);return len(nodes)-1
def cancel(current,pivot):
 old=nodes[current]['v'];pv=nodes[pivot]['v']
 d,j=leading(old);dp,jp=leading(pv)
 assert j==jp and d>=dp
 aa=coeff(old[j],d);bb=coeff(pv[j],dp);shift=Lp**(d-dp)
 raw=[bb*old[i]-aa*shift*pv[i] for i in range(2)]
 if not any(raw):
  for i in range(2):assert bb*old[i]==aa*shift*pv[i]
  stats['zeroRowCoordinateReturns']+=2
  return None
 v,g=primitive(raw)
 for i in range(2):assert g*v[i]==bb*old[i]-aa*shift*pv[i]
 stats['edgeCoordinateReturns']+=2
 assert leading(v)<(d,j)
 edges=[(current,R(bb,g)),(pivot,R(-aa*shift,g))]
 assert all(pure_x(a.d) for _,a in edges)
 node={'v':v,'seed':None,'parents':edges,
       'depth':1+max(nodes[k]['depth'] for k,_ in edges)}
 nodes.append(node);return len(nodes)-1
basis={}
say('new_B_original_module_input_ready',originalInputRows=len(inputs),
 monicOmegaDegrees=[degree(a.n) for a in qw],
 noOldScalarCofactorExecuted=True,originalFullSourceSHA256=BASE_SHA,
 originalDefinitionPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest(),
 originalUnitTarget='lambda*t*(ell*(2lambda^2-2lambda+1)-T^2)',
 noPhysicalDInverted=True)
reductions=0
for i,row in enumerate(inputs):
 check_time();current=seed(i,row)
 while current is not None:
  check_time()
  d,j=leading(nodes[current]['v'])
  if j not in basis:basis[j]=current;break
  old=basis[j]
  if d<leading(nodes[old]['v'])[0]:
   basis[j]=current;current=old
  current=cancel(current,basis[j]);reductions+=1
 say('new_B_module_row_processed',originalRow=i,
     distinctLeadingPositions=sorted(basis),
     basisDegrees={str(j):leading(nodes[n]['v'])[0] for j,n in basis.items()},
     exactDAGNodes=len(nodes),leadingCancellations=reductions)
assert len(basis)==2
basis_degrees={j:leading(nodes[n]['v'])[0] for j,n in basis.items()}
dimension=sum(basis_degrees.values())
say('new_B_actual_weak_Popov_basis',genericQuotientDimension=dimension,
 basisDegrees=[basis_degrees[0],basis_degrees[1]],exactDAGNodes=len(nodes),
 allLeadingPositionsDistinct=True,allOriginalInputsIncluded=True,
 originalModuleFreenessAssumed=False,wholeBExcluded=False)
def r_degree(a):
 assert pure_x(a.d) and allowed(a.n)
 return degree(a.n)
def r_coeff(a,d):return R(coeff(a.n,d),a.d)
def reduce_target(target):
 rem=target[:];comb={j:R() for j in basis};steps=0
 while True:
  check_time()
  candidates=[(r_degree(rem[j]),j) for j in basis
              if r_degree(rem[j])>=basis_degrees[j]]
  if not candidates:break
  d,j=max(candidates);node=nodes[basis[j]];p=node['v']
  dp=basis_degrees[j]
  c=r_coeff(rem[j],d)/R(coeff(p[j],dp))
  assert pure_x(c.n) and pure_x(c.d)
  mult=c*lam**(d-dp)
  rem=[rem[k]-mult*R(p[k]) for k in range(2)]
  comb[j]+=mult;steps+=1
 for k in range(2):
  assert target[k]==rem[k]+sum((a*R(nodes[basis[j]]['v'][k]) for j,a in comb.items()),R())
  stats['targetCoordinateReturns']+=1
 return rem,comb,steps
def reduce_product(a,b):
 raw=ns['mul'](a,b)
 rem,quot=ns['reduce_omega'](raw)
 assert not ns['sub'](raw,ns['add'](ns['mul'](quot,qw),rem))
 stats['originalOmegaShortDivisions']+=1
 return rem
Dphys=ns['ell']*(2*lam*lam-2*lam+1)-ns['T']**2
Dchanged=ns['substitute'](Dphys,2)
Drow,Dquot=ns['reduce_omega'](Dchanged)
assert not ns['sub'](Dchanged,ns['add'](ns['mul'](Dquot,qw),Drow))
stats['originalOmegaShortDivisions']+=1
unitrow=[lam*a for a in reduce_product(that,Drow)]
for a in unitrow:
 ns['ckden'](a)
say('new_B_actual_positive_unit_action',DvalOriginalIdentity='ell*A2-T^2=bc*(h-k)^2 at the same original physical point',
 unitRowLambdaDegrees=[r_degree(a) for a in unitrow],
 onlyOriginalPositiveProducts=True,physicalUnitScope='current original D!=0 Phi and already excluded t=0, nonzero isolated mean',
 DNormInverseUsed=False)
target=[R(1),R()];found=None;rem=None;comb=None
for n in range(dimension+1):
 check_time()
 rem,comb,steps=reduce_target(target)
 say('new_B_original_unit_power_reduced',power=n,
     target='(lambda*t*Dval)^n',remainderLambdaDegrees=[r_degree(a) for a in rem],
     fullTwoCoordinateReturn=True,divisionSteps=steps,
     exactZeroRemainder=not any(rem))
 if not any(rem):
  found=n;break
 if n<dimension:target=reduce_product(target,unitrow)
if found is None:
 say('new_B_original_positive_unit_not_annihilated',
     genericQuotientDimension=dimension,powersTestedThrough=dimension,
     exactDAGNodes=len(nodes),statistics=stats,
     originalUnitNilpotenceProved=False,wholeBExcluded=False,
     wholePhiExcluded=False,ordinaryISPClaim=False)
else:
 used=[basis[j] for j,a in comb.items() if a]
 reachable=set();stack=used[:]
 while stack:
  n=stack.pop()
  if n in reachable:continue
  reachable.add(n);stack.extend(k for k,_ in nodes[n]['parents'])
 cover=oneP
 for n in sorted(reachable):
  node=nodes[n]
  values=[node['seed_scale']] if node['seed'] is not None else [a for _,a in node['parents']]
  for a in values:
   assert pure_x(a.d);cover=p_lcm(cover,a.d)
 for a in list(comb.values())+target+unitrow+qw+that:
  assert pure_x(a.d);cover=p_lcm(cover,a.d)
 depth=1+max((nodes[n]['depth'] for n in reachable),default=0)
 remaining=cover;paidRemoved=oneP
 while int(remaining.total_degree())>0:
  g=remaining.gcd(paid)
  if int(g.total_degree())<=0:break
  remaining=exact(remaining,g);paidRemoved*=g
 assert paidRemoved*remaining==cover
 assert remaining and pure_x(remaining)
 # Each DAG edge denominator divides cover; one extra power per edge depth.
 # Thus cover^depth*target is in the module generated by all original inputs.
 # The source identities for q and the variable change return this to I6.
 say('new_B_actual_original_positive_unit_cover',
     genericQuotientDimension=dimension,annihilatedOriginalUnitPower=found,
     clearedDAGExponent=depth,exactDAGNodes=len(nodes),
     reachableDAGNodes=len(reachable),
     pureXDenominatorLCM=profile(cover),retainedUnpaidCover=profile(remaining),
     paidPartTimesRetainedCoverReturned=True,allEdgeTwoCoordinateReturns=True,
     finalTwoCoordinateReturn=True,
     strictOriginalConclusion='retained_cover^N*(lambda*t*Dval)^n belongs to the correct original I6 in the stated paid ring',
     everyRetainedWeightZeroFiberKept=True,
     noPhysicalDInverted=True,wholeBExcluded=int(remaining.total_degree())==0,
     wholePhiExcluded=False,ordinaryISPClaim=False,statistics=stats)
