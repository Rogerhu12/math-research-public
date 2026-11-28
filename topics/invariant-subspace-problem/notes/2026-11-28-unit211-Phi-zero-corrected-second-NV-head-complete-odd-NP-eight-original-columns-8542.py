#!/usr/bin/env python3
"""NEW corrected Phi, second full-NV t-head: COMPLETE odd N/P values.
The previously proved four-generator ambient algebra is only a definition
dependency. No old twenty-column loop, three-cofactor proof or scalar gcd
is entered. Three old base rows R/EBe/N1 are regenerated as parameters.
Eight NEW columns are the four basis multiples of each complete odd value.
Two fixed four-column groups both contain the NEW odd N and odd P:
[R,EBe,EN,EP] and [R,N1,EN,EP]. Every cofactor is transported into NINE
original polynomial numerators before any common multiplier cancellation.
All unproved weight or lambda heads remain. Absolute 120 seconds / 1 GiB.
"""
import ast,hashlib,json,resource,signal,time
from pathlib import Path
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
BASE='2026-11-28-unit211-Phi-zero-corrected-second-NV-t-head-original-four-generator-columns-8542.py'
BASE_SHA='c7141ce12424d916ee415c0ac0121ea938ff206d20b5a8c12193bb3a1cdcdaa1'
PREFIX_BYTES=10519
PREFIX_SHA='67c407b2bd4a611a90a1094403546860459dfbb3bad6676a990dca6773343255'
MARKER='# EXACT source order and all twenty columns are fixed before execution.'
base_path=Path(__file__).with_name(BASE)
base_bytes=base_path.read_bytes()
assert hashlib.sha256(base_bytes).hexdigest()==BASE_SHA
base_text=base_bytes.decode()
assert base_text.index(MARKER)==PREFIX_BYTES
prefix=base_text[:PREFIX_BYTES]
assert hashlib.sha256(prefix.encode()).hexdigest()==PREFIX_SHA
# Only the necessary definitions and parameter assignments are retained.
# The old top-level assertions, progress output, counters, paid-check loop,
# START/DEADLINE reset and all top-level resource/clock calls are omitted.
# Internal checks of exact arithmetic and the monic definitions remain.
# In particular there is no inherited alarm or setitimer invocation.
module=ast.parse(prefix,filename=BASE);kept=[];omitted={}
def omit(kind):omitted[kind]=omitted.get(kind,0)+1
for node in module.body:
 if isinstance(node,ast.Assign):
  names=[v.id for v in node.targets if isinstance(v,ast.Name)]
  if any(v in ('START','DEADLINE') for v in names):
   omit('old_clock_assignment');continue
  kept.append(node)
 elif isinstance(node,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef)):
  kept.append(node)
 elif isinstance(node,ast.Assert):omit('old_top_level_assert')
 elif isinstance(node,ast.AugAssign):omit('old_top_level_counter')
 elif isinstance(node,ast.Expr):omit('old_top_level_expression')
 elif isinstance(node,ast.For):
  assert isinstance(node.target,ast.Name) and node.target.id=='value'
  omit('old_coordinate_paid_check_loop')
 else:raise AssertionError(('unexpected parameter-prefix node',type(node).__name__))
module.body=kept
exec(compile(ast.fix_missing_locations(module),BASE,'exec'),globals())
# This is parameter-generation cost, never a repeated proof receipt.
definition_statistics=dict(stats)
stats={'exactProducts':0,'newMonicDivisionReturns':0,
 'necessaryOldColumnDefinitions':0,'newOddOriginalReturns':0,
 'newColumnRawReturns':0,'newColumnCoordinates':0,
 'newCofactorCoordinates':0,'newNineSourceReturns':0,
 'newFinalDenominatorReturns':0}
tick()

def P2(v):
 cv=center(v)
 return tr(vm(vm(cv,cv),cv))
NBerr=N4(rows[2])-E(2*lam*P02)*h**2
NCerr=N4(rows[3])-E(2*lam*P02)*k**2
PBerr=P2(rows[2])-E(P02)*h**3
PCerr=P2(rows[3])-E(P02)*k**3
EN=oldpaid(NBerr.b);EP=oldpaid(PBerr.b)
assert NCerr==NBerr.conj() and PCerr==PBerr.conj()
assert NBerr-NCerr==E(0,2*EN)
assert PBerr-PCerr==E(0,2*EP)
assert geo(EN)<=3 and geo(EP)<=3
stats['newOddOriginalReturns']+=4
# All nine entries are the same-point original equations.  E3 and NV
# retain their old definitions; their multipliers are allowed to be zero.
original=original+[EN,EP]
labels=labels+['complete_odd_N_value','complete_odd_P_value']
raw=[v.n for v in original]
assert len(original)==9 and len(raw)==9
say('new_second_NV_head_two_complete_odd_original_values',
 originalLabels=labels,
 oddN=rp(EN),oddP=rp(EP),geometricDegreeUpperBounds=[3,3],
 completeSingletonErrorsAndConjugatesReturned=True,
 physicalTNotSpecializedToZero=True,
 oldDefinitionSourceSHA256=BASE_SHA,
 oldDefinitionPrefixBytes=PREFIX_BYTES,oldDefinitionPrefixSHA256=PREFIX_SHA,
 parameterASTOmissions=omitted,
 parameterExactProducts=definition_statistics['exactProducts'],
 oldTwentyColumnAndThreeCofactorProofNotEntered=True,
 fixedGroups=[[0,4,20,24],[0,8,20,24]],
 fixedLambdaUpperBounds=[6,6])
tick()

columns={};traces={};meta={}
def old_column_definition(value):
 # Reconstruct only the required canonical remainder and its coefficients.
 # Do not repeat an old full original-row check or old column loop.
 qt_mult,rr0=monic_div(value,qt_tilde,4)
 qs_mult,rem=monic_div(rr0,qs,3)
 tag=[(qs_mult-qt_mult*ws)/(ell*delta),
      qt_mult*gammaR,qt_mult*gammaO]
 stats['necessaryOldColumnDefinitions']+=1
 return four_coordinates(rem),tag
for ci,oi in [(0,1),(4,2),(8,4)]:
 cc,tag=old_column_definition(original[oi])
 columns[ci]=cc;traces[ci]=tag;meta[ci]=(oi,0)
# Only these eight columns are new.  The prior exact 4-by-20 presentation
# plus these eight defines the exact J9 presentation; the old twenty
# columns are not regenerated or re-certified.
for oi,first in [(7,20),(8,24)]:
 block=[]
 for bi,monomial in enumerate(basis):
  cc,tag=reduce_to_original(monomial*original[oi])
  for row in range(4):
   assert only_lambda(cc[row])<=3+basis_degrees[bi]-basis_degrees[row]
  ci=first+bi;columns[ci]=cc;traces[ci]=tag;meta[ci]=(oi,bi)
  block.append([rp(v) for v in cc])
 say('new_second_NV_head_four_complete_odd_columns',
     seed=labels[oi],newColumnIndices=list(range(first,first+4)),
     columns=block,completeOrdinaryOriginalReturns=4,
     fullNewCoordinateReturns=16,
     everyOriginalWeightPoleOldPaid=True)
 tick()
assert stats['necessaryOldColumnDefinitions']==3
assert stats['newColumnRawReturns']==8 and stats['newColumnCoordinates']==32

def det3(A):
 return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
        -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
        +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
FIXED=[('R_EBe_complete_odd_N_and_P',[0,4,20,24],6),
       ('R_N1_complete_odd_N_and_P',[0,8,20,24],6)]
finished=[]
for label,indices,bound in FIXED:
 tick()
 matrix=[[columns[j][i] for j in indices] for i in range(4)]
 omega=[]
 for j in range(4):
  sub=[[matrix[i][k0] for k0 in range(4) if k0!=j] for i in range(1,4)]
  omega.append((-1)**j*det3(sub))
 target=sum((matrix[0][j]*omega[j] for j in range(4)),R())
 for i in range(4):
  assert sum((matrix[i][j]*omega[j] for j in range(4)),R())==(target if i==0 else R())
  stats['newCofactorCoordinates']+=1
 assert only_lambda(target)<=bound
 coefficients=[R() for _ in range(9)]
 for j,ci in enumerate(indices):
  oi,bi=meta[ci];tag=traces[ci];c0=omega[j]
  coefficients[oi]+=c0*basis[bi]
  coefficients[0]-=c0*tag[0]
  coefficients[1]-=c0*tag[1]
  coefficients[3]-=c0*tag[2]
 # First transport to all nine rational original equations.
 assert target==sum((coefficients[i]*original[i] for i in range(9)),R())
 stats['newNineSourceReturns']+=1
 if not target:
  say('new_second_NV_head_complete_odd_cofactor_zero',
      label=label,indices=indices,lambdaUpperBound=bound,
      completeFourCoordinateAndNineOriginalReturn=True,
      allOriginalFibersRetained=True,wholeSecondHeadExcluded=False)
  finished.append({'label':label,'zero':True})
  continue
 # Fi=raw_i/di, so the multiplier on raw_i is coefficients_i/di.
 raw_coeff=[oldpaid(coefficients[i]/original[i].d) for i in range(9)]
 assert target==sum((raw_coeff[i]*R(raw[i]) for i in range(9)),R())
 stats['newNineSourceReturns']+=1
 denominator=ONE
 for value in raw_coeff+[target]:
  oldpaid(value)
  denominator=exact(denominator,denominator.gcd(value.d))*value.d
 Om=[value.n*exact(denominator,value.d) for value in raw_coeff]
 rhs=target.n*exact(denominator,target.d)
 assert sum((Om[i]*raw[i] for i in range(9)),ZERO)==rhs
 stats['newNineSourceReturns']+=1
 # Cancel only a common factor of ALL actual original multipliers.
 common=ZERO
 for value in Om:common=common.gcd(value)
 assert common
 Om=[exact(value,common) for value in Om];rhs=exact(rhs,common)
 assert sum((Om[i]*raw[i] for i in range(9)),ZERO)==rhs
 stats['newNineSourceReturns']+=1
 # Only old physical weight units are removed from the necessary scalar.
 removed=ONE
 while rhs and int(rhs.total_degree())>0:
  gg=rhs.gcd(PAID)
  if int(gg.total_degree())==0:break
  rhs=exact(rhs,gg);removed*=gg
 lc=rhs.coefficient(0);rhs/=lc;removed*=lc
 final=[oldpaid(R(value,removed)) for value in Om]
 assert sum((final[i]*R(raw[i]) for i in range(9)),R())==R(rhs)
 stats['newNineSourceReturns']+=1
 stats['newFinalDenominatorReturns']+=9
 degree=only_lambda(R(rhs));assert degree<=bound
 lead=at(R(rhs),2,degree) if degree>=0 else R()
 say('new_second_NV_head_complete_odd_nine_original_scalar',
     label=label,indices=indices,lambdaUpperBound=bound,
     actualLambdaDegree=degree,scalar=pp(rhs),
     lambdaLeadingCoefficient=rp(lead),
     commonOfAllNineActualOriginalMultipliers=pp(common),
     initialFinalDenominator=pp(denominator),
     removedOnlyOldPaidUnits=pp(removed),
     nineFinalOriginalMultipliers=[rp(value) for value in final],
     fourAdjugateCoordinatesReturned=True,
     completeNineOriginalPolynomialIdentityReturned=True,
     everyCommonAndNewHeadZeroFiberRetained=True,
     noGenericScalarGcdFactorizationPrimeOrDeterminantInverse=True,
     wholeSecondHeadExcluded=(int(rhs.total_degree())==0))
 finished.append({'label':label,'zero':False,'lambdaDegree':degree,
                  'oldPaidScalarUnit':int(rhs.total_degree())==0,
                  'sha256':pp(rhs)['sha256']})
 tick()
say('new_second_NV_head_complete_odd_input_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 originalSourceCount=9,freeAmbientBasis=['1','sigma','t','sigma*t'],
 newOriginalColumnCount=8,previouslyProvedColumnCount=20,
 exactCombinedPresentationColumnCount=28,
 onlyNecessaryOldBaseRowDefinitionsRegenerated=3,
 oldTwentyColumnOrThreeCofactorGateReplayed=False,
 fixedCofactors=finished,statistics=stats,
 allOtherOriginalConditionsRetained=True,
 allUnpaidWeightAndLambdaHeadsRetained=True,
 wholeSecondHeadExcludedByReturnedUnit=any(v.get('oldPaidScalarUnit',False) for v in finished),
 wholePhiExcluded=False,noExclusionFromDegreeOrProfileAlone=True)
