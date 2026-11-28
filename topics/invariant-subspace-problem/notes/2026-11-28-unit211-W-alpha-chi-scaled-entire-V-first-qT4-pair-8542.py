#!/usr/bin/env python3
"""NEW whole W: scaled complete N4(V), then the NEW qT4/Vlow pair.
The failed 17703 source's native reducer and its old paid-denominator
whitelist are kept byte-identical. The new raw vectors ell*V0,ell*V1
remove the later ell inverse BEFORE native reduction; only the final
pure-weight row is divided by the independently paid ell**2.
Only qT4 is regenerated as a necessary input to this new pair.
No old R6/Nlow/Plow target, ten rows, three scalars or norm is rerun.
180 seconds / 4 GiB; all source DAGs retained, profiles only.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
START=time.perf_counter();DEADLINE=START+180
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
raw_timer=signal.setitimer;raw_alarm=signal.alarm
raw_timer(signal.ITIMER_REAL,180)
def say(**kw):
 kw['seconds']=time.perf_counter()-START
 print(json.dumps(kw,separators=(',',':')),flush=True)
def bounded_timer(which,seconds,interval=0.0):
 if which!=signal.ITIMER_REAL:return raw_timer(which,seconds,interval)
 assert not interval
 left=max(.001,DEADLINE-time.perf_counter())
 return raw_timer(which,min(left,float(seconds) if seconds>0 else left),0.0)
def bounded_alarm(seconds):return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
path=Path(__file__).with_name('2026-11-28-unit211-W-alpha-chi-full-original-ten-by-two-8542.py')
full=path.read_bytes()
assert hashlib.sha256(full).hexdigest()=='18101a4af587253e1dad49cee60d188c60db401ed34b13cf73edeb4e09b6d42b'
marker=b'\nnewfive=rawthree[:]';assert full.count(marker)==1
prefix=full.split(marker)[0]
assert len(prefix)==9855 and hashlib.sha256(prefix).hexdigest()=='c1436ea6bb67d4c720016091fb65f439be5bfcc7af131c00a0749321fcf45e43'
env={'__name__':'new_scaled_entire_V_necessary_alpha_square_only','__file__':str(path)}
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+'#monic_square_definition_only','exec'),env)
finally:
 signal.alarm=raw_alarm;signal.setitimer=raw_timer
 raw_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
R,NR,ctx,ns=[env[key] for key in ['R','NR','ctx','ns']]
ep,kp,cp,ap=ctx.gens()
zz,oo=ctx.constant(0),ctx.constant(1)
paid,strip,profile,embed=[env[key] for key in ['paid','strip','profile','embed']]
qc,qalpha,alpha=env['qc'],env['qalpha'],env['alpha']
ac,adeg=env['ac'],env['adeg']
basis=ns['basis'];oldoriginal=ns['original']
newbasis=[R(1),env['xx'],env['yy'],env['tt'],env['yy']**2,env['yy']*env['tt']]
assert len(basis)==len(newbasis)==6
assert not any(ns['tags'][j][i] for j in range(6) for i in [4,5])
native_den_paid=set()
def native_coefficient(c):
 c=NR(c)
 for p in [c.n,c.d]:
  assert all(not any(int(v) for v in mon[2:]) for mon in p.to_dict())
 key=str(c.d)
 if key not in native_den_paid:
  paid(embed(c.d));native_den_paid.add(key)
 return c
def row_profile(row):
 return [{'n':profile(embed(native_coefficient(c).n)),
          'd':profile(embed(c.d))} for c in row]
def row_digest(row):
 encoded=json.dumps([[[list(map(int,mon[:2])),str(c)]
             for mon,c in sorted(p.to_dict().items())]
             for v in row for p in [v.n,v.d]],separators=(',',':')).encode()
 return dict(bytes=len(encoded),sha256=hashlib.sha256(encoded).hexdigest())
nu,nQ,nell,nM,nP02,nJ=[ns[key] for key in ['u','Q','l','M','P02','J']]
nm=nu-nell;ndelta=1-nQ
for unit in [nu,nQ,nell,nM,nm,ndelta,nP02]:
 paid(embed(unit.n));paid(embed(unit.d))
nlam,nT=ns['lam'],ns['T']
# Full original polynomial source identities for twelve actual actions.
# reduce_six returns row.b - axis*b_j = tag.original, not a free equality.
matrices={};errors={};original_products=0
for name,axis in [('lambda',nlam),('T',nT)]:
 matrix=[];err=[]
 for j,bj in enumerate(basis):
  row,tag=ns['reduce_six'](axis*bj)
  assert not tag[4] and not tag[5]
  for c in row:native_coefficient(c)
  matrix.append(row);err.append(tag);original_products+=1
 matrices[name]=matrix;errors[name]=err
 say(stage='new_scaled_V_necessary_native_axis',
     axis=name,actualOriginalSourceIdentities=6,
     allSixNativeColumnRelationsReturned=True,
     coefficientDefinition=row_digest([c for row in matrix for c in row]),
     noMatrixCommutationOrOriginalFreenessAssumed=True)
# Tiny polynomial ring in two independent placeholders (lambda,T).
# Its coefficients are only the paid native weight ring.
class P:
 def __init__(self,value=0):
  if isinstance(value,P):self.c=value.c.copy();return
  c=native_coefficient(value);self.c={(0,0):c} if c else {}
 @classmethod
 def terms(cls,terms):
  out=object.__new__(cls)
  out.c={key:native_coefficient(c) for key,c in terms.items() if c}
  return out
 def __neg__(self):return P.terms({key:-c for key,c in self.c.items()})
 def __add__(self,other):
  other=P(other);out=self.c.copy()
  for key,c in other.c.items():out[key]=out.get(key,NR())+c
  return P.terms(out)
 __radd__=__add__
 def __sub__(self,other):return self+-P(other)
 def __rsub__(self,other):return P(other)+-self
 def __mul__(self,other):
  other=P(other);out={}
  for (a,b),c in self.c.items():
   for (d,e),v in other.c.items():
    key=(a+d,b+e);out[key]=out.get(key,NR())+c*v
  return P.terms(out)
 __rmul__=__mul__
 def __truediv__(self,other):
  other=P(other);assert set(other.c)=={(0,0)}
  c=other.c[(0,0)];assert c
  paid(embed(c.n));paid(embed(c.d))
  return P.terms({key:v/c for key,v in self.c.items()})
 def __pow__(self,power):
  assert power>=0
  out=P(1);base=self
  while power:
   if power&1:out=out*base
   power//=2
   if power:base=base*base
  return out
L=P.terms({(1,0):NR(1)});Tr=P.terms({(0,1):NR(1)})
u,Q,ell,M,P02,J,m,delta=map(P,[nu,nQ,nell,nM,nP02,nJ,nm,ndelta])
A=2*L*L-2*L+1;B=4*L**3-6*L*L+3*L-1
D=ell*A-Tr*Tr
K=ell*ell*B-3*ell*A*Tr+2*Tr**3
Ast=4*u*Q-J;Cst=Ast*m*m+J*delta*ell*ell;cval=3-2*L
ad=M*ell*ell*Q*(3-4*L)+M*Ast*Tr*Tr+2*M*u*Q*cval*ell*Tr+D*Cst
bd=2*M*m*(Ast*Tr+u*Q*cval*ell)
qT4=(2*m*D*ad+K*bd)/(8*m*u*Q*ell*ell*delta)
assert max((a+b for a,b in qT4.c),default=-1)<=4
# Base rows carry full source traces. Each later lambda/T action
# adds row_i*errors[axis][i] and multiplies its previous original DAG.
bases={};base_tags={};source_nodes=[];cache={};native_rows={}
def new_node(kind,data,row):
 for c in row:native_coefficient(c)
 node=len(source_nodes);source_nodes.append((kind,data))
 native_rows[node]=row
 return node
def add_base(label,poly):
 row,tag=ns['reduce_six'](poly)
 assert not tag[4] and not tag[5]
 for c in row:native_coefficient(c)
 node=new_node('actual_original_base',label,row)
 bases[label]=node;base_tags[label]=tag
 return node
one_node=new_node('one',[1,0,0,0,0,0],[NR(1)]+[NR() for _ in range(5)])
bases['one']=one_node
def act(name,node):
 row=native_rows[node];matrix=matrices[name]
 out=[sum((row[i]*matrix[i][j] for i in range(6)),NR()) for j in range(6)]
 return new_node('actual_axis_action',[name,node],out)
def monomial_node(label,a,b):
 key=(label,a,b)
 if key not in cache:
  if a:node=act('lambda',monomial_node(label,a-1,b))
  elif b:node=act('T',monomial_node(label,0,b-1))
  else:node=bases[label]
  cache[key]=node
 return cache[key]
def polynomial_node(poly,label='one'):
 poly=P(poly);row=[NR() for _ in range(6)];terms=[]
 for (a,b),co in sorted(poly.c.items()):
  node=monomial_node(label,a,b)
  row=[v+co*w for v,w in zip(row,native_rows[node])]
  terms.append((node,co))
 return new_node('original_polynomial_linear_combination',terms,row)
def sum_nodes(*nodes):
 row=[sum((native_rows[node][j] for node in nodes),NR()) for j in range(6)]
 return new_node('sum_original_sources',list(nodes),row)
value_nodes={}
def remember(label,node):
 value_nodes[label]=node
 say(stage='new_scaled_V_pure_weight_six_generator_source',
  name=label,originalDAGNode=node,sourceDAGOperations=len(source_nodes),
  coefficientDefinition=row_digest(native_rows[node]),
  actualSource='full original mean base traces plus twelve actual lambda/T actions',
  noGeometryDenominator=True,noExpandedLargeTraceClaim=True)
# qT4's six row was already returned by 17703. Here it is only a
# necessary coefficient definition for the NEW qT4/Vlow alpha,chi pair;
# its old standalone checkpoint is not counted as a new result.
remember('qT4_input_to_new_pair',polynomial_node(qT4))
N4,E=[ns[key] for key in ['N4','E']]
# Homogeneous quadratic N4: N4(ell*V)=ell**2*N4(V).
# New raw inputs have NO ell inverse. The old reducer's denominator
# assertion is not edited, extended, intercepted or disabled.
V0=[E(1),E(nlam-1-nT),E(1+nT/nell),E(1+nT/nell)]
V1=[E(),E(),E(nm/nell,-1),E(nm/nell,1)]
scaledV0=[E(nell),E(nell*(nlam-1-nT)),E(nell+nT),E(nell+nT)]
scaledV1=[E(),E(),E(nm,-nell),E(nm,nell)]
for original,scaled in [(V0,scaledV0),(V1,scaledV1)]:
 assert all(E(nell)*v==sv for v,sv in zip(original,scaled))
z0=N4(scaledV0);z2=N4(scaledV1)
z1=N4([a+b for a,b in zip(scaledV0,scaledV1)])-z0-z2
assert not z0.b and not z1.b and not z2.b
for name,value in [
 ('scaled_Z0_full_N4V0',z0.a),
 ('scaled_Z1_full_N4polar',z1.a),
 ('scaled_Z2_full_N4V1',z2.a)]:
 say(stage='new_scaled_complete_V_base_begin',name=name,
     oldNativeDenominatorWhitelistUnchanged=True)
 node=add_base(name,value)
 say(stage='new_scaled_complete_V_actual_original_base',
     name=name,originalSourceNode=node,
     fullOriginalMeanSourceIdentityReturned=True,
     oldNativeDenominatorWhitelistPassedUnchanged=True,
     coefficientDefinition=row_digest(native_rows[node]))
scaled_node=sum_nodes(
 polynomial_node(D,'scaled_Z0_full_N4V0'),
 polynomial_node(K/(2*m),'scaled_Z1_full_N4polar'),
 polynomial_node(D*D/M,'scaled_Z2_full_N4V1'))
# This NEW pure-weight operation uses the separately paid ell unit;
# it never feeds an ell denominator into the old native reducer.
scale=native_coefficient(1/(nell*nell))
paid(embed(scale.n));paid(embed(scale.d))
vrow=[scale*c for c in native_rows[scaled_node]]
assert all(nell*nell*c==old for c,old in zip(vrow,native_rows[scaled_node]))
vnode=new_node('paid_weight_scale',[scaled_node,scale],vrow)
remember('entire_Vlow',vnode)
say(stage='new_scaled_entire_V_original_six_return',
    threeScaledFullN4OriginalTracesReturned=True,
    allSixEllSquaredRecoveryProductsReturned=True,
    fullOriginalN4VNotAComponentOrPhiMultiple=True,
    oldReducerWhitelistUnchanged=True,
    noDInverseOrGeometryHeadInverse=True)
# Only NOW transport each six-row once to the new alpha,chi graph.
# There is no old ten-row or old scalar construction in this source.
divisions=0;last_products=0
def dex(a,b):
 global divisions
 q,r=divmod(a,b);assert not r and q*b==a
 divisions+=1;return q
def clear_pair(pair):
 den=oo
 for cf in pair:
  paid(cf.d);den=dex(den,den.gcd(cf.d))*cf.d
 paid(den);cols=[cf.n*dex(den,cf.d) for cf in pair]
 common=cols[0].gcd(cols[1])
 if common:
  rest,removed,hist=strip(common)
  cols=[dex(p,removed) for p in cols]
 else:removed=oo;hist=[]
 if any(cols):
  c=next(p for p in cols if p).coefficient(0)
  cols=[p/c for p in cols];removed*=c
 factor=R(removed,den);paid(factor.n);paid(factor.d)
 assert all(R(cols[j])*factor==pair[j] for j in range(2))
 return cols,factor,hist
lines={};polylines={};scales={}
for label,node in value_nodes.items():
 row=native_rows[node]
 value=sum((R(embed(c.n),embed(c.d))*newbasis[j] for j,c in enumerate(row)),R())
 paid(value.d);assert adeg(value)<=2
 head=ac(value,2);linear=value-head*qalpha
 assert adeg(linear)<=1
 pair=[ac(linear,0),ac(linear,1)]
 assert value==pair[0]+pair[1]*alpha+head*qalpha
 cols,scale,hist=clear_pair(pair)
 lines[label]=pair;polylines[label]=cols;scales[label]=scale
 last_products+=3
 say(stage='new_scaled_V_alpha_chi_linear_return',
  name=label,nativeOriginalSourceNode=node,
  nativeFirstThenSingleCoordinateSubstitution=True,
  fullMonicSquareShortDivisionAndBothScalingProductsReturned=True,
  columns=[profile(p) for p in cols],onlyPaidWeightContentRemoved=hist,
  alphaMultipleDefinedByExistingExactMonicMultiplication=True,
  alphaMultipleCoefficientsNotExpandedHere=True)
say(stage='new_scaled_entire_V_and_qT4_actual_two_column_interface',
 existingExactI6TenRowsRetainedByReference=True,
 actualNewValueLinears=list(lines),
 allThreeScaledOriginalN4InputsAndEllSquaredRecoveryReturned=True,
 monicAlphaClosureFollowsWithoutExpandedAlphaMultiples=True,
 newlyExpandedRows=2,newlyExpandedColumns=2,
 noClaimPreviouslyUnreturnedR6NlowPlowAlphaRowsComputed=True,
 noNewGeometryUnitOrNormInverse=True,
 entireCurrentPaidWeightChartCovered=True,
 wholeWExcluded=False)
# Only genuinely new full-value pair targets. Unknown common zeros stay.
targets=[]
for left_name,right_name in [('qT4_input_to_new_pair','entire_Vlow')]:
 left,right=polylines[left_name],polylines[right_name]
 mu=[right[1],-left[1]];g=mu[0].gcd(mu[1])
 if not g:
  say(stage='new_scaled_V_pair_constant_rows',
      labels=[left_name,right_name],constants=[profile(left[0]),profile(right[0])],
      noNewUnitClaim=True)
  continue
 mu=[dex(v,g) for v in mu]
 scalar=mu[0]*left[0]+mu[1]*right[0]
 assert not mu[0]*left[1]+mu[1]*right[1]
 assert mu[0]*(left[0]+left[1]*ap)+mu[1]*(right[0]+right[1]*ap)==scalar
 out,removed,hist=strip(scalar)
 if out:
  c=out.coefficient(0);out/=c;removed*=c
 assert out*removed==scalar
 last_products+=2
 rec=dict(labels=[left_name,right_name],actualMultiplierCommon=profile(g),
  originalScalar=profile(scalar),retainedNecessaryPolynomial=profile(out),
  onlyPaidWeightRemoval=hist,bothActualMultiplierAndColumnProductsReturned=True,
  entireCommonMultiplierZeroFiberPreserved=True,
  noUnpaidLeadingOrGeometryFactorRemoved=True)
 targets.append(rec);say(stage='new_qT4_scaled_complete_V_alpha_chi_pair',**rec)
say(stage='new_scaled_complete_V_qT4_first_return_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 newActualNativeAxisIdentities=original_products,
 newOriginalScaledBaseTraces=3,originalSourceDAGOperations=len(source_nodes),
 verifiedNativeWeightDenominators=len(native_den_paid),
 newFinalPolynomialDivisionProducts=divisions,
 newFinalShortDivisionAndScalarIdentities=last_products,
 twoOriginalValueLinearsActuallyReturned=True,
 oldR6NlowPlowTargetsNotExecuted=True,
 oldTenRowsThreeScalarsGammaAndNormsNotExecuted=True,
 formalAlphaClosureNotClaimedSeparatelyExpanded=True,
 noCoefficientPayloadOrMatrixCacheSaved=True,
 wholeWExcluded=any(not r['retainedNecessaryPolynomial']['zero'] and
                   r['retainedNecessaryPolynomial']['totalDegree']==0 for r in targets),
 ordinaryISPClaim=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
raw_timer(signal.ITIMER_REAL,0)
