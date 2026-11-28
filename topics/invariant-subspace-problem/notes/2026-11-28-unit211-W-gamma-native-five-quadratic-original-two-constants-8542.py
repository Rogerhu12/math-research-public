#!/usr/bin/env python3
"""NEW entire W/gamma: direct native NS/PS quadratic pullback, exact five rows.
Only two necessary definition prefixes: same-point gamma Gram (10176B)
and native six monic mean rules (14656B). No old 18 multiplication columns,
commutators, weight determinant, f-cube/q_f, nine lift or ten-by-two tail.
The native NS/PS remainders have total x,y,t degree <=2. Gamma x,y,t
are affine in the SAME f, so all FIVE rows are truly quadratic in f.
Complete original traces and two NEW fixed three-row scalar targets.
180s/4GiB, absolute nested deadline, profiles only, no data cache.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
START=time.perf_counter();DEADLINE=START+180
signal.setitimer(signal.ITIMER_REAL,180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**kw):
 kw['seconds']=time.perf_counter()-START
 print(json.dumps(kw,separators=(',',':')),flush=True)
def digest(obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def run_prefix(name,full_sha,marker,nbytes,prefix_sha,nsname):
 path=Path(__file__).with_name(name);raw=path.read_bytes()
 assert hashlib.sha256(raw).hexdigest()==full_sha
 assert raw.count(marker)==1
 pref=raw.split(marker)[0]
 assert len(pref)==nbytes and hashlib.sha256(pref).hexdigest()==prefix_sha
 ns={'__file__':str(path),'__name__':nsname}
 old_alarm=signal.alarm;old_timer=signal.setitimer
 def timer(which,seconds,interval=0.0):
  if which!=signal.ITIMER_REAL:return old_timer(which,seconds,interval)
  assert not interval
  left=max(.001,DEADLINE-time.perf_counter())
  return old_timer(which,min(left,float(seconds) if seconds>0 else left),0.0)
 def alarm(seconds):return math.ceil(timer(signal.ITIMER_REAL,seconds)[0])
 signal.alarm=alarm;signal.setitimer=timer
 try:
  with contextlib.redirect_stdout(io.StringIO()):
   exec(compile(pref,str(path)+'#new_definition_prefix_only','exec'),ns)
 finally:
  signal.alarm=old_alarm;signal.setitimer=old_timer
  old_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
 return ns
env=run_prefix(
 '2026-11-28-unit211-W-gamma-open-direct-native-f-cube-monic-two-8542.py',
 'bd68e5e5e66f31e9c3e2ad0b66468c021fc7d852d44462d3a937966200ab961c',
 b'\n# Necessary old definitions only:',10176,
 '8545759f4c40266068fc932bd2ef10710fe67cd767cf743900fe3d215bfb6bcf',
 'new_gamma_original_Gram_only')
ns=run_prefix(
 '2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py',
 '10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1',
 b'\nmatrices=[];errors=[]',14656,
 '88b8e2f49f925e51c0b940f929efb502ced9ed358228a605fea3755d9cdefff8',
 'new_native_mean_rule_definitions_only')
R,ctx,ep,kp,sp,fp,zz,oo=[env[k] for k in ['R','ctx','ep','kp','sp','fp','zz','oo']]
f,xx,yy,tt,l,m=[env[k] for k in ['f','x0','x1','t','l','m']]
EW,EB,N1,NS,PS=[env[k] for k in ['EW','EB','N1','NS','PS']]
original=[EW.a,EB.b,N1.a,NS.a,PS.a]
atoms=env['base_atoms'];paid=env['paid_den']
NR=ns['R'];native_original=ns['original']
assert ns['freemons']==[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(0,2,0),(0,1,1)]
assert len(ns['q'])==6 and len(native_original)==6
assert all(not tag[j] for tag in ns['tags'] for j in [4,5])
exact_products=0;new_original_products=0
def dex(a,b):
 global exact_products
 q,r=divmod(a,b)
 assert not r and q*b==a
 exact_products+=1;return q
def profile(p):
 if not p:return dict(zero=True,degrees_e_k_s_f=[-1]*4,terms=0)
 data=[[list(map(int,mm)),str(c)] for mm,c in sorted(p.to_dict().items())]
 return dict(zero=False,degrees_e_k_s_f=list(map(int,p.degrees())),
  totalDegree=int(p.total_degree()),terms=len(data),**digest(data))
def embed_weight(p):
 out=zz
 for mm,co in p.to_dict().items():
  assert all(int(mm[j])==0 for j in range(2,8))
  out+=co*ep**int(mm[0])*kp**int(mm[1])
 return out
def pull(v,maxdegree=3):
 """Explicit context embedding, not a cast between unlike mpoly contexts."""
 v=NR(v);den=embed_weight(v.d);paid(den,atoms)
 grouped={}
 for mm,co in v.n.to_dict().items():
  assert all(int(mm[j])==0 for j in range(5,8))
  geo=tuple(map(int,mm[2:5]));assert sum(geo)<=maxdegree
  grouped[geo]=grouped.get(geo,zz)+co*ep**int(mm[0])*kp**int(mm[1])
 out=R()
 for geo,po in grouped.items():
  term=R(po,den)
  for var,power in zip([xx,yy,tt],geo):term=term*var**power
  out=out+term
 paid(out.d,atoms)
 return out
# Actual native determinants and all original rule-trace denominators.
for po in [ns['delta2'],ns['delta3'].n,ns['delta3'].d]:
 paid(embed_weight(po),atoms)
for rule,tag in zip(ns['q'],ns['tags']):
 for cf in ns['coeffmap'](rule).values():paid(embed_weight(cf.d),atoms)
 for cf in tag:paid(embed_weight(cf.d),atoms)
# Same normalization and same Gram before using the two original remainders.
for key in ['u','Q','l','Delta','P02','f','lam','T']:
 assert pull(ns[key],1)==env[key]
for nr,gr in zip(ns['rows'],env['rows']):
 for nv,gv in zip(nr,gr):
  assert pull(nv.a,1)==gv.a and pull(nv.b,1)==gv.b
new_original_products+=40
assert EW.a==env['E1'].a and EW.a==l*EB.a+m*EB.b
say(stage='new_gamma_native_original_Gram_context_identification',
 explicitEightToFourVariableContextEmbedding=True,
 allSameOriginalWeightsFMeanLambdaTAndGramReturned=True,
 actualNativeQuadraticAndCubicRuleHeadsPaid=True,
 noOldEighteenMultiplicationsOrCofactorTailExecuted=True,
 noMonicF2OrNineLiftScalarReplayed=True)
gamma_basis=[R(1),xx,yy,tt,yy*yy,yy*tt]
newrows=original[:3]
pullback_tags=[]
for gen in [4,5]:
 initial=[NR(int(j==gen)) for j in range(6)]
 row,tag=ns['reduce_six'](native_original[gen],initial)
 assert len(row)==6 and len(tag)==6
 assert tag[4]==NR(int(gen==4)) and tag[5]==NR(int(gen==5))
 native_rem=sum((row[j]*ns['basis'][j] for j in range(6)),NR())
 assert native_rem==sum((tag[j]*native_original[j] for j in range(6)),NR())
 assert all(sum(mon)<=2 for mon in ns['coeffmap'](native_rem))
 coeffs=[pull(co,0) for co in row]
 rem=sum((coeffs[j]*gamma_basis[j] for j in range(6)),R())
 pulled_tag=[pull(tag[j],1) for j in range(4)]
 # Native E1=EW and EBe=(EW-m*EBo)/ell on the exact gamma graph.
 mean_tag=[pulled_tag[0]+pulled_tag[1]/l,
           pulled_tag[2]-m*pulled_tag[1]/l,pulled_tag[3]]
 target=original[gen-1]
 returned=target+sum((mean_tag[j]*original[j] for j in range(3)),R())
 assert rem==returned
 assert all(int(mm[3])==0 for mm in rem.d.to_dict())
 assert not rem or int(rem.n.degrees()[3])<=2
 for co in mean_tag:paid(co.d,atoms)
 newrows.append(rem);pullback_tags.append(mean_tag)
 new_original_products+=2
 say(stage='new_gamma_true_native_quadratic_original_pullback',
  name=['NS','PS'][gen-4],originalCubicIndex=gen,
  nativeTotalGeometricDegreeAtMostTwo=True,
  exactOriginalIdentity='Qnative=original_cubic+sum(mean_tag_j*Qj)',
  originalCubicCoefficientIsOne=True,
  allThreeMeanSourceProductsReturned=True,
  sameOriginalFQuadraticProfile=profile(rem.n),
  denominator=profile(rem.d),
  meanMultipliers=[dict(numerator=profile(c.n),denominator=profile(c.d)) for c in mean_tag],
  noIndividualFHeadInverted=True,noNewParameterOpen=True)
assert len(newrows)==5
primitive=[];units=[]
for index,val in enumerate(newrows):
 assert all(int(mm[3])==0 for mm in val.d.to_dict())
 if not val:
  primitive.append(zz);units.append(R(1))
  say(stage='new_gamma_exact_five_quadratic_original_zero_row',index=index)
  continue
 core,removed,hist=env['strip_atoms'](val.n,atoms)
 assert core
 rational_scale=core.coefficient(0);core/=rational_scale;removed*=rational_scale
 unit=R(removed,val.d)
 assert R(core)*unit==val
 paid(unit.n,atoms);paid(unit.d,atoms)
 primitive.append(core);units.append(unit)
 new_original_products+=1
 say(stage='new_gamma_exact_five_quadratic_original_primitive_row',
  index=index,name=['EW','EBo','N1','nativeNS','nativePS'][index],
  originalProfile=profile(core),onlyPaidParameterContentRemoved=hist,
  completeOriginalUnitScalingReturned=True)
def fcols(po):
 if not po:return [zz,zz,zz]
 assert int(po.degrees()[3])<=2
 out=[zz,zz,zz]
 for mm,co in po.to_dict().items():
  ee,kk,ss,ff=map(int,mm)
  out[ff]+=co*ep**ee*kp**kk*sp**ss
 assert sum((out[j]*fp**j for j in range(3)),zz)==po
 return out
matrix=[fcols(po) for po in primitive]
say(stage='new_entire_gamma_exact_original_five_quadratic_system',
 rows=5,columns=['1','f','f^2'],
 exactOriginalI6Equality=True,
 allUnpaidParameterAndHeadZeroFibersKept=True,
 noF2HeadInverse=True,noFrozenTenByTwoComputed=True,
 actualFAndSRowDegrees=[[int(p.degrees()[3]),int(p.degrees()[2])] if p else [-1,-1] for p in primitive])
targets=[]
# New targets only: do not regenerate the completed EW/EBo/N1 scalar.
for indices in [(0,1,3),(0,1,4)]:
 selected=[matrix[i] for i in indices]
 b0,b1,b2=[v[1] for v in selected];a0,a1,a2=[v[2] for v in selected]
 mu=[b1*a2-b2*a1,b2*a0-b0*a2,b0*a1-b1*a0]
 common=zz
 for po in mu:common=common.gcd(po)
 if not common:
  say(stage='new_gamma_native_fixed_scalar_zero',rows=list(indices),
   reason='all_three_actual_multipliers_are_zero',wholeGammaExcluded=False)
  targets.append(dict(rows=list(indices),zero=True));continue
 reduced=[dex(po,common) for po in mu]
 result=[sum((reduced[i]*selected[i][j] for i in range(3)),zz) for j in range(3)]
 assert not result[1] and not result[2]
 scalar=result[0]
 assert sum((reduced[i]*primitive[indices[i]] for i in range(3)),zz)==scalar
 new_original_products+=2
 core,removed,hist=env['strip_atoms'](scalar,atoms)
 if core:
  normal=core.coefficient(0);core/=normal;removed*=normal
 assert core*removed==scalar
 # At no point was an original equation divided by common.
 rec=dict(rows=list(indices),commonMultiplier=profile(common),
  originalScalar=profile(scalar),necessaryPrimitive=profile(core),
  onlyPaidParameterRemoval=hist,
  completeThreeColumnAndOriginalPolynomialProductsReturned=True,
  allActualMultiplierCommonFactorZeroFibersPreserved=True)
 targets.append(rec)
 say(stage='new_gamma_native_quadratic_fixed_original_constant',**rec)
say(stage='new_gamma_native_five_quadratic_two_scalars_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 exactOriginalI6FiveQuadraticEquality=True,
 actualPolynomialDivisionProducts=exact_products,
 actualOriginalIdentityProducts=new_original_products,
 nativeDefinitionProductsAlreadyReturned=True,
 newNecessaryNonzeroScalars=sum('necessaryPrimitive' in r and not r['necessaryPrimitive']['zero'] for r in targets),
 wholeGammaExcluded=any('necessaryPrimitive' in r and not r['necessaryPrimitive']['zero'] and r['necessaryPrimitive']['totalDegree']==0 for r in targets),
 noOldCompletedScalarOrFrozenDeterminantReplayed=True,
 noCoefficientOrMatrixCacheSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 ordinaryISPClaim=False)
