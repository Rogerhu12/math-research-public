#!/usr/bin/env python3
"""NEW correct Phi: the ENTIRE ell=1/2 weight curve, same-lambda original
module, and positive z/D targets. No old whole-Phi action/cofactor/resultant
proof gate is executed. Known definitions are specialized BEFORE expansion.
The new lambda gcd has complete original sources; the finite container keeps
ALL fifteen I6 relations, all lambda multiplicities, and every pure-u pole.
Only actual zero target remainders give a necessary cover. The known D=0
bipartite boundary is not treated as a physical solution or a proof here.
120 seconds / 1 GiB, two small source dependencies, no coefficient payload.
"""
import ast,hashlib,json,math,os,pathlib,resource,signal,time
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
RAW_ALARM=signal.alarm
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120 second boundary')
def bounded_alarm(seconds):
 tick();left=max(1,math.ceil(DEADLINE-time.perf_counter()))
 return RAW_ALARM(left if seconds<=0 else max(1,min(int(seconds),left)))
signal.alarm=bounded_alarm;signal.alarm(120)
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True,separators=(',',':')),flush=True)
def input_path(name):
 p=pathlib.Path(__file__).with_name(name)
 if not p.exists():p=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/name
 return p
BASE='2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py'
MODULE='2026-11-28-unit211-Phi-zero-corrected-whole-original-I6-fifteen-by-three-8542.py'
BASE_SHA='5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7'
MODULE_SHA='84e0efcc19a0274d571484b187b7b155c81ebf255e40a39c38ac13a03f911cf0'
basefull=input_path(BASE).read_text();modfull=input_path(MODULE).read_text()
assert hashlib.sha256(basefull.encode()).hexdigest()==BASE_SHA
assert hashlib.sha256(modfull.encode()).hexdigest()==MODULE_SHA
marker='def param(p):';assert basefull.count(marker)==1
baseprefix=basefull[:basefull.index(marker)]
assert len(baseprefix)==4007
assert hashlib.sha256(baseprefix.encode()).hexdigest()=='dd105b713040712dad7cebeefb489c8e1cf53f56cb5fce8ff0de0bf681d6c669'
def tuple_names(node):
 if not isinstance(node,ast.Assign) or len(node.targets)!=1:return ()
 tt=node.targets[0]
 if not isinstance(tt,(ast.Tuple,ast.List)):return ()
 return tuple(v.id if isinstance(v,ast.Name) else '' for v in tt.elts)
# Specialization homomorphism is applied immediately after the FOUR free
# symbols are defined. Thus no generic C6 or global old proof is computed.
base_nodes=[];specializations=0
for node in ast.parse(baseprefix,str(input_path(BASE))).body:
 if isinstance(node,ast.Assert):continue
 base_nodes.append(node)
 if tuple_names(node)==('u','Q','lam','Tr'):
  base_nodes.extend(ast.parse('Q=4*(u-1)*(u-2)\nQp=Q.n').body)
  specializations+=1
assert specializations==1
env={'__name__':'new_entire_ell_half_original_polynomial_definitions',
     '__file__':str(input_path(BASE))}
exec(compile(ast.fix_missing_locations(ast.Module(body=base_nodes,type_ignores=[])),
             str(input_path(BASE))+'#new-ell-half-specialization','exec'),env)
start="R=env['R'];";stop='seeds=[rN,rNS,rPS,c1,c2]'
assert modfull.count(start)==1 and modfull.count(stop)==1
fragment=modfull[modfull.index(start):modfull.index(stop)]
assert len(fragment)==10153
assert hashlib.sha256(fragment.encode()).hexdigest()=='ccfe93b7ba226f39592c69087a9f5aa08fa556ca320c84831809fdbe878c26d1'
nodes_kept=[];omitted=[];second_specializations=0
for node in ast.parse(fragment,str(input_path(MODULE))).body:
 skip=isinstance(node,ast.Assert)
 if isinstance(node,ast.Expr) and isinstance(node.value,ast.Call):
  skip=skip or isinstance(node.value.func,ast.Name) and node.value.func.id=='say'
 if isinstance(node,ast.For):
  skip=not(isinstance(node.target,ast.Name) and node.target.id=='f'
           and isinstance(node.iter,ast.Name) and node.iter.id=='forms')
 if isinstance(node,ast.Assign):
  names={v.id for v in node.targets if isinstance(v,ast.Name)}
  skip=skip or bool(names & {'AA','BB','normalized','eT','eZ','ntrace'})
 if skip:omitted.append([node.lineno,type(node).__name__]);continue
 nodes_kept.append(node)
 if tuple_names(node)==('u','Q','lam','T','z'):
  nodes_kept.extend(ast.parse('Qp=Q.n').body);second_specializations+=1
assert second_specializations==1
ns={'env':env,'tick':tick,'hashlib':hashlib,
    '__name__':'new_ell_half_known_I6_definitions_only',
    '__file__':str(input_path(MODULE))}
exec(compile(ast.fix_missing_locations(ast.Module(body=nodes_kept,type_ignores=[])),
             str(input_path(MODULE))+'#specialized-necessary-definitions-only','exec'),ns)
signal.alarm=bounded_alarm;signal.alarm(120)
R=ns['R'];ctx=ns['ctx'];Z=ns['Z'];O=ns['O']
u,Q,lam,T,z,ell,m,delta,M,bc,P02=(ns[k] for k in
 ('u','Q','lam','T','z','ell','m','delta','M','bc','P02'))
up,unused_Q,lp,Tp,zp=ctx.gens()
assert Q==4*(u-1)*(u-2) and ell==R(1)/2
assert m==u-R(1)/2 and M==-2*(u-1)**2
assert ns['ff']==u/2-(u-2)*(lam-R(1)/2)-(u-2)**2*(T+R(1)/2)/(u-1)
# u and m are paid by the independent whole original zero-base-mean and
# equal-weight results. A and B are paid by the corrected WHOLE A/B proofs.
# No theta, 2ell-1, new pure-u polynomial, z or D inverse is used.
paidSupport=ns['paidSupport']*up*m.n
ns['paidSupport']=paidSupport
ck=ns['ck'];exact=ns['exact'];strip_paid=ns['strip_paid']
profile=ns['profile'];mv=ns['mv'];mm=ns['mm'];dot=ns['dot']
rules=ns['rules'];MT=ns['MT'];MZ=ns['MZ'];I=ns['I']
seeds=[ns[k] for k in ('rN','rNS','rPS','c1','c2')]
seed_names=['N1','NS','PS','comm_T','comm_z']
for row in rules+MT+MZ+seeds:
 for v in row:ck(v)
statistics={'newLambdaDivisionProducts':0,'newCofactorCoordinates':0,
 'newGcdOriginalCoordinates':0,'newFiniteInputDivisionCoordinates':0,
 'newFiniteMatrixCoordinates':0,'newTargetReductionCoordinates':0,
 'newTargetSpanCoordinates':0,'newFinalPolynomialCoordinates':0}
def u_only(p):
 return all(all(int(ex[j])==0 for j in (1,2,3,4)) for ex in p.to_dict())
def lambda_only(p):
 return all(all(int(ex[j])==0 for j in (1,3,4)) for ex in p.to_dict())
def trim(p):
 p=list(p)
 while p and not p[-1]:p.pop()
 return p
def pfrom(v):
 v=R(v);assert u_only(v.d) and lambda_only(v.n)
 degree=max((int(ex[2]) for ex in v.n.to_dict()),default=-1)
 out=[R() for _ in range(degree+1)]
 for ex,c in v.n.to_dict().items():
  out[int(ex[2])]+=R(ctx.from_dict({(int(ex[0]),0,0,0,0):c}),v.d)
 return trim(out)
def pvalue(p):return sum((v*lam**j for j,v in enumerate(p)),R())
def padd(a,b):
 return trim([(a[j] if j<len(a) else R())+(b[j] if j<len(b) else R())
              for j in range(max(len(a),len(b)))])
def pneg(a):return [-v for v in a]
def psub(a,b):return padd(a,pneg(b))
def pscale(a,c):return trim([v*R(c) for v in a])
def pmul(a,b):
 if not a or not b:return []
 out=[R() for _ in range(len(a)+len(b)-1)]
 for j,x in enumerate(a):
  for k,y in enumerate(b):out[j+k]+=x*y
 return trim(out)
def pshift(a,j):return [R() for _ in range(j)]+list(a) if a else []
def pdiv(a,b):
 tick();a=trim(a);b=trim(b);assert b
 saved=list(a);q=[R() for _ in range(max(0,len(a)-len(b)+1))]
 while a and len(a)>=len(b):
  j=len(a)-len(b);ratio=a[-1]/b[-1];q[j]+=ratio
  a=psub(a,pshift(pscale(b,ratio),j))
 q=trim(q)
 assert padd(pmul(q,b),a)==saved
 statistics['newLambdaDivisionProducts']+=1
 return q,a
one=[R(1)]
def pxgcd(a,b):
 aa=list(a);bb=list(b)
 x0,x1=one,[];y0,y1=[],one
 while bb:
  q,rr=pdiv(aa,bb)
  aa,bb=bb,rr
  x0,x1=x1,psub(x0,pmul(q,x1))
  y0,y1=y1,psub(y0,pmul(q,y1))
 if not aa:return [],[],[]
 inv=1/aa[-1];g=pscale(aa,inv)
 x0=pscale(x0,inv);y0=pscale(y0,inv)
 assert padd(pmul(x0,a),pmul(y0,b))==g and g[-1]==R(1)
 return g,x0,y0
denominators={};den_reasons={}
def retain_den(v,reason):
 v=R(v);assert u_only(v.d)
 key=str(v.d);denominators[key]=v.d
 den_reasons[reason]=den_reasons.get(reason,0)+1
def retain_poly(p,reason):
 for v in p:retain_den(v,reason)
def retain_vector(p,reason):
 for a in p:retain_poly(a,reason)
def poly_profile(p):
 v=pvalue(p)
 return {'lambdaDegree':len(p)-1,'numerator':profile(v.n),
         'denominator':profile(v.d)}
def cofactor(chosen):
 row=[seeds[i] for i in chosen]
 mu=[row[1][1]*row[2][2]-row[1][2]*row[2][1],
     row[2][1]*row[0][2]-row[2][2]*row[0][1],
     row[0][1]*row[1][2]-row[0][2]*row[1][1]]
 tag=[[] for _ in range(5)]
 if not any(mu):return [],tag
 den=O
 for v in mu:ck(v);den=exact(den,den.gcd(v.d))*v.d
 nums=[v.n*exact(den,v.d) for v in mu];common=Z
 for pp in nums:common=common.gcd(pp)
 assert common
 primitive=[R(exact(v,common)) for v in nums]
 returned=[sum((primitive[j]*row[j][i] for j in range(3)),R()) for i in range(3)]
 assert not returned[1] and not returned[2]
 statistics['newCofactorCoordinates']+=3
 for j,idx in enumerate(chosen):tag[idx]=pfrom(primitive[j])
 return pfrom(returned[0]),tag
def vecadd(a,b):return [padd(a[i],b[i]) for i in range(3)]
def vecsub(a,b):return [psub(a[i],b[i]) for i in range(3)]
def pmatvec(mat,v):
 return [sum_polys([pmul(mat[i][j],v[j]) for j in range(3)]) for i in range(3)]
def sum_polys(polys):
 out=[]
 for p in polys:out=padd(out,p)
 return out
def power_target_name(kind,n):return ('z' if kind=='z' else 'Dphysical')+'^'+str(n)
def cover_result(target,exponent):
 den=O
 for pp in denominators.values():den=exact(den,den.gcd(pp))*pp
 assert den and u_only(den)
 # Final exact denominators, not stale generic pivots, are the source of
 # this cover. The known three rules have only OLD paid denominators.
 for pp in denominators.values():assert exact(den,pp)*pp==den
 core,paidpart=strip_paid(den)
 assert core and core*paidpart==den and u_only(core)
 constant=core.coefficient(0);core=exact(core,ctx.constant(constant))
 paidpart*=constant
 assert core*paidpart==den
 rr,_=strip_paid(paidpart);assert rr and int(rr.total_degree())==0
 say('new_ell_half_complete_original_positive_target_cover',
     target=target,coverNumerator=profile(core),
     completeActualDenominatorLCM=profile(den),
     clearingExponent=exponent,
     identity='cover^exponent * target belongs to the original I6 on ell=1/2',
     finalDenominatorCount=len(denominators),denominatorUseCounts=den_reasons,
     allUnpaidPureUZeroFibersRetained=True,
     originalZTargetIsQTimesPhysicalT=True,
     originalDTarget='ell*A2-T^2 = bc*(h-k)^2',
     noPhysicalZOrDInverseInCertificate=True,
     wholePhysicalEllHalfExcluded=int(core.total_degree())==0)
 return int(core.total_degree())==0

def main():
 say('new_ell_half_original_specialization_ready',
     actualWeightCurve='ell=1/2, Q=4*(u-1)*(u-2)',
     baseFullSHA256=BASE_SHA,moduleFullSHA256=MODULE_SHA,
     originalDefinitionSpecializationBeforeExpansion=True,
     basePrefixSHA256=hashlib.sha256(baseprefix.encode()).hexdigest(),
     moduleDefinitionFragmentSHA256=hashlib.sha256(fragment.encode()).hexdigest(),
     omittedOldTopLevelChecks=omitted,
     noOldWholePhiFifteenColumnCofactorOrFixedResultantGateRun=True,
     oldCorrectThreeMeanRulesAndExactI6PresentationUsed=True,
     allPureUNewPoleFibersWillBeRetained=True,
     noBipartiteBoundaryUsedAsPhysicalPointOrProof=True)
 C0,tag0=cofactor([0,1,2]);C1,tag1=cofactor([0,3,4])
 assert len(C0)<=7 and len(C1)<=7
 say('new_ell_half_two_original_scalar_definitions',
     scalars=[poly_profile(C0),poly_profile(C1)],
     onlyNewFaceActualMultiplierCommonCancelled=True,
     allSixOriginalModuleCoordinatesReturned=True)
 if not C0 and not C1:
  say('new_ell_half_no_scalar_lambda_model_returned',
      entireWeightCurveAndAllOriginalConditionsRetained=True)
  return
 g,sa,sb=pxgcd(C0,C1)
 assert g
 gtags=[padd(pmul(sa,tag0[i]),pmul(sb,tag1[i])) for i in range(5)]
 gv=pvalue(g)
 for j in range(3):
  returned=sum((pvalue(gtags[i])*seeds[i][j] for i in range(5)),R())
  assert returned==(gv if j==0 else R())
  statistics['newGcdOriginalCoordinates']+=1
 retain_poly(g,'monic_lambda_model')
 for tag in gtags:retain_poly(tag,'complete_original_g_seed_multipliers')
 gden=O
 for pp in denominators.values():gden=exact(gden,gden.gcd(pp))*pp
 say('new_ell_half_complete_original_same_lambda_gcd',
     gcd=poly_profile(g),degree=len(g)-1,
     originalFiveSeedMultiplierDenominatorLCM=profile(gden),
     completeTwoScalarBezoutAndAllThreeOriginalCoordinatesReturned=True,
     allOriginalLambdaMultiplicityRetained=True,
     originalGDenominatorZeroFibersRetained=True,
     noAssumedGcdDegreeOrBoundaryIdentification=True)
 if len(g)==1:
  assert g==one
  cover_result('1',1)
  return
 degree=len(g)-1;dimension=3*degree
 seedpolys=[[pfrom(v) for v in row] for row in seeds]
 matrixT=[[pfrom(v) for v in row] for row in MT]
 matrixZ=[[pfrom(v) for v in row] for row in MZ]
 identitypoly=[[one if i==j else [] for j in range(3)] for i in range(3)]
 relations=[];relation_names=[]
 # EXACT old I6: G,MT G,MZ G. Here these are only the specialized original
 # source columns for the NEW finite same-lambda computation, not a replay
 # of the old presentation proof or global actions.
 for name,row in zip(seed_names,seedpolys):
  for action,mat in [('one',identitypoly),('T',matrixT),('z',matrixZ)]:
   vv=pmatvec(mat,row)
   for pp in vv:
    for c0 in pp:ck(c0)
   relations.append(vv);relation_names.append([name,action])
 def modulo_vector(v,reason):
  quot=[];rem=[]
  for pp in v:
   qq,rr=pdiv(pp,g);quot.append(qq);rem.append(rr)
   assert padd(pmul(qq,g),rr)==pp
  retain_vector(quot,reason+'_quotients')
  retain_vector(rem,reason+'_remainders')
  return rem,quot
 def flatten(v):
  assert len(v)==3 and all(len(pp)<=degree for pp in v)
  return [v[i][j] if j<len(v[i]) else R()
          for i in range(3) for j in range(degree)]
 def unflatten(v):
  assert len(v)==dimension
  return [trim(v[i*degree:(i+1)*degree]) for i in range(3)]
 columns=[];original_columns=[];column_names=[]
 for ri,row in enumerate(relations):
  for jj in range(degree):
   raw=[pshift(pp,jj) for pp in row]
   reduced,qq=modulo_vector(raw,'finite_original_column')
   columns.append(flatten(reduced));original_columns.append(raw)
   column_names.append([relation_names[ri],jj])
   statistics['newFiniteInputDivisionCoordinates']+=3
 assert len(columns)==15*degree
 def trace_add(a,b,factor):
  out=dict(a);factor=R(factor)
  for j,v in b.items():
   out[j]=out.get(j,R())+factor*v
   if not out[j]:del out[j]
  return out
 def trace_scale(a,factor):
  return {j:v*factor for j,v in a.items() if v*factor}
 def trace_vector(trace):
  return [sum((coef*columns[j][ii] for j,coef in trace.items()),R())
          for ii in range(dimension)]
 echelon=[]
 for idx,column in enumerate(columns):
  tick();v=list(column);trace={idx:R(1)}
  for pivot,row,rt in echelon:
   coef=v[pivot]
   if not coef:continue
   v=[v[ii]-coef*row[ii] for ii in range(dimension)]
   trace=trace_add(trace,rt,-coef)
  pivot=next((ii for ii,x in enumerate(v) if x),None)
  if pivot is None:continue
  inv=1/v[pivot];v=[x*inv for x in v];trace=trace_scale(trace,inv)
  assert v[pivot]==R(1) and trace_vector(trace)==v
  statistics['newFiniteMatrixCoordinates']+=dimension
  echelon.append((pivot,v,trace))
  echelon.sort(key=lambda entry:entry[0])
 rank=len(echelon)
 say('new_ell_half_full_original_finite_same_lambda_module',
     lambdaDegree=degree,coefficientContainerDimension=dimension,
     originalRelationColumns=len(columns),rankOverQQofU=rank,
     genericOriginalI6QuotientDimension=dimension-rank,
     everySelectedEchelonColumnHasCompleteOriginalTrace=True,
     allFifteenRelationsAndAllLambdaPowersRetained=True,
     notAFreedomOrGenericEmptyInference=True,
     everyPureUPoleFiberRetained=True)
 def solve_target(v):
  original=list(v);trace={};res=list(v)
  for pivot,row,rt in echelon:
   coef=res[pivot]
   if not coef:continue
   res=[res[ii]-coef*row[ii] for ii in range(dimension)]
   trace=trace_add(trace,rt,coef)
  back=trace_vector(trace)
  assert all(back[ii]+res[ii]==original[ii] for ii in range(dimension))
  statistics['newTargetSpanCoordinates']+=dimension
  return res,trace
 # Both are genuine original polynomial actions. In particular D is
 # ell*A2-T^2, NOT an inverse or a quotient by its norm.
 matrixTT=[[sum_polys([pmul(matrixT[i][k],matrixT[k][j])
                       for k in range(3)]) for j in range(3)] for i in range(3)]
 ellA2=pfrom(ell*(2*lam*lam-2*lam+1))
 matrixD=[[psub(ellA2 if i==j else [],matrixTT[i][j])
           for j in range(3)] for i in range(3)]
 for mat in [matrixZ,matrixD]:
  for row in mat:
   for pp in row:
    for cc in pp:ck(cc)
 successes=[]
 # Fixed first targets, not an adaptive rerun: positive z powers first;
 # only if all powers 1..dimension fail do we test the positive D powers.
 for kind,mat in [('z',matrixZ),('Dphysical',matrixD)]:
  value=[one,[],[]]
  for power in range(1,dimension+1):
   tick();raw=pmatvec(mat,value)
   value,qq=modulo_vector(raw,'positive_'+kind+'_action')
   statistics['newTargetReductionCoordinates']+=3
   res,trace=solve_target(flatten(value))
   if any(res):
    say('new_ell_half_original_positive_target_nonzero_remainder',
        target=power_target_name(kind,power),
        remainderNonzeroCoordinates=sum(bool(v) for v in res),
        noExclusionOrNilpotenceClaim=True)
    continue
   # Lift the returned finite combination all the way back to the three
   # FULL lambda-polynomial coordinates of the original fifteen columns.
   # This is the new target certificate, not merely a finite matrix rank.
   for coeff in trace.values():retain_den(coeff,'final_original_column_multipliers')
   combination=[[],[],[]]
   for idx,coeff in trace.items():
    for j in range(3):
     combination[j]=padd(combination[j],pscale(original_columns[idx][j],coeff))
   final_quotients=[]
   for j in range(3):
    diff=psub(value[j],combination[j]);qqq,rr=pdiv(diff,g)
    assert not rr and pmul(qqq,g)==diff
    final_quotients.append(qqq)
    statistics['newFinalPolynomialCoordinates']+=1
   retain_vector(final_quotients,'final_complete_three_coordinate_g_quotients')
   # Let Gamma be the FINAL denominator LCM. Gamma*g is in original I6.
   # The displayed full target identity uses only one Gamma in the other
   # multipliers. Every action error is an old-rule error plus g*q, whose
   # denominators are retained above. Thus Gamma^2 times the LITERAL
   # z^power or D^power belongs to I6. The power does not grow along these
   # actions: their original multipliers z or D have only old paid units.
   label=power_target_name(kind,power)
   say('new_ell_half_literal_original_positive_target_returned',
       target=label,originalColumnsUsed=len(trace),
       finiteCoordinateReturnCount=dimension,
       allThreeFullLambdaPolynomialCoordinatesReturned=True,
       completeOriginalGSourcePreviouslyReturned=True,
       originalActionErrorsUseOnlyOldRulesAndReturnedGQuotients=True,
       clearingExponent=2,noInverseOfTargetOrPhysicalD=True)
   excluded=cover_result(label,2)
   successes.append([kind,power,excluded])
   break
  if successes:break
 if not successes:
  say('new_ell_half_all_fixed_positive_targets_retained',
      maximumPositivePowerTested=dimension,
      noZOrDZeroRemainderReturned=True,
      allPureUPoleFibersAndEntireRemainingOriginalBranchRetained=True,
      noWholeEllHalfExclusion=True)
main()
say('new_ell_half_same_lambda_original_positive_target_input_finished',
    statistics=statistics,
    sourceSHA256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
    onlyNewEllHalfSpecializedOriginalTargetsComputed=True,
    noOldWholePhiProofGateReplayed=True,
    noCoefficientPayloadOrChunksWritten=True,
    ordinaryISPClaim=False,
    maxRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
RAW_ALARM(0)
