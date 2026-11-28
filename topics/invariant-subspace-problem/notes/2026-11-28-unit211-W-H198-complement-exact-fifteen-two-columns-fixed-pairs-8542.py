#!/usr/bin/env python3
"""NEW exact original 15 x 2 presentation on the explicit H198 complement.
Use the paid three mean rules and N1's actual weight-slope coordinate.
Transform ALL fifteen exact stable relations, including NS, PS and their
x/y products, by the same invertible (1,x,y)->(1,z,Nrow) matrix. Remove
only the actual Nrow coordinate. No relation of the original I6 is lost.
Two new fixed 2 x 2 constant-target cofactors use N1*x,N1*y and NS,PS.
A common factor may be cancelled only from BOTH cofactor multipliers;
both resulting column products are actually returned. Every unpaid
scalar content/head remains, as does the entire H198=0 branch.
No chi norm, old 12-resultant, 18-row module or native weight determinant.
180 seconds / 4 GiB. Source-defined original DAGs, no coefficient cache.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
started=time.perf_counter();deadline=started+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**kw):
 kw['seconds']=time.perf_counter()-started
 print(json.dumps(kw,separators=(',',':')),flush=True)
slope_path=Path(__file__).with_name(
 '2026-11-28-unit211-W-original-N1-slope-weight-coordinate-monic-square-8542.py')
raw=slope_path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='9b7731d221175a88edbf7f98bb1c811402ab1d8e332b94fb005dd073b7894d00'
marka=b'\nscalar,factors=remaining.factor()'
markb=b'\ndef pay_chart(p):'
markend=b"\nsay(stage='new_W_N1_slope_coordinate_monic_square_complete_original_return',"
assert raw.count(marka)==raw.count(markb)==raw.count(markend)==1
parta=raw.split(marka)[0]
partb=markb+raw.split(markb)[1].split(markend)[0]
assert len(parta)==4799 and hashlib.sha256(parta).hexdigest()=='be7547a34352074e9fd8ded0bfb8ede4ef0179614c5b72527483ffaaf2165871'
assert len(partb)==1851 and hashlib.sha256(partb).hexdigest()=='060d92ecc52c08cabb909b7c3d8b8b86f5dae62a7bda9e385fa8d453596287ab'
ns={'__file__':str(slope_path),'__name__':'new_two_column_necessary_N1_coordinate_only'}
saved_alarm=signal.alarm
def bounded_alarm(seconds):
 remaining=max(.001,deadline-time.perf_counter())
 previous=signal.setitimer(signal.ITIMER_REAL,min(remaining,float(seconds) if seconds>0 else remaining))
 return math.ceil(previous[0])
signal.alarm=bounded_alarm
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(parta+partb,str(slope_path)+'#coordinate_definitions_without_old_QQ_factorization','exec'),ns)
finally:signal.alarm=saved_alarm
signal.setitimer(signal.ITIMER_REAL,max(.001,deadline-time.perf_counter()))
tri=ns['tri'];R=ns['R'];ctx=ns['ctx'];one=ns['one'];zero=ns['zero']
ep,kp,xp,yp,Lp,Zp=ctx.gens()[:6]
profile=ns['profile'];rp=ns['rp'];strip=ns['strip'];pay_chart=ns['pay_chart'];legal=ns['legal']
Delta=ns['Delta'];aa=ns['a'];cc=ns['c'];p0,p1,p2=ns['nrow']
ntag=ns['ntag'];z=ns['z'];original=ns['original']
assert Delta and not ns['whole']
assert aa*p2-cc*p1==Delta
say(stage='new_two_column_coordinate_prefix_original_products',
 exactChart='existing paid W with H198 != 0',
 sameOriginalN1AndMonicSquareSourceReturned=True,
 oldCompleteQQH198FactorizationNotReexecuted=True,
 pureWeightDeterminant=rp(Delta),
 monicSquareLambdaDegrees=[3,2],
 noLambdaOrPhysicalDInverse=True,wholeH198ZeroBranchRetained=True,
 wholeWExcluded=False)
three_path=Path(__file__).with_name(
 '2026-11-28-unit211-W-K7-open-physical-lambda-original-three-column-projection-binding-corrected-8542.py')
three_raw=three_path.read_bytes()
assert hashlib.sha256(three_raw).hexdigest()=='7cf3ff802cdf8166e3fb96f3ea806b81b83570f9200d10fad11caa13862f2c3f'
tail=three_raw[5833:7854]
assert len(tail)==2021 and hashlib.sha256(tail).hexdigest()=='7bfee4bbfdaafd3bff7044685536439adef2b96467781261e493e3b4b2408e25'
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(tail,str(three_path)+'#only_eleven_original_rows_after_already_built_rules','exec'),tri)
rows=tri['rows'];rowtags=tri['rowtags'];labels=tri['labels']
matrices=tri['matrices'];errors=tri['errors'];xx=tri['xx'];yy=tri['yy']
assert len(rows)==11
# The four previously proved missing products complete the exact stable
# presentation. Their original traces use the SAME point and six inputs.
for label in ['NS','PS']:
 idx=labels.index(label)
 for axis,var in enumerate([xx,yy]):
  row=[sum((R(rows[idx][i])*matrices[axis][i][j] for i in range(3)),R()) for j in range(3)]
  tag=[var*rowtags[idx][g]-sum((R(rows[idx][i])*errors[axis][i][g] for i in range(3)),R()) for g in range(6)]
  with contextlib.redirect_stdout(io.StringIO()):
   tri['addrow'](row,tag,label+'*'+'xy'[axis])
wanted=['N1','same_point_commutator_1','same_point_commutator_2',
 'N1*x','N1*y','same_point_commutator_1*x','same_point_commutator_1*y',
 'same_point_commutator_2*x','same_point_commutator_2*y',
 'NS','PS','NS*x','NS*y','PS*x','PS*y']
assert len(wanted)==15 and len(set(labels))==len(labels)
assert all(label in wanted for label in labels)
say(stage='new_full_fifteen_original_same_point_relations_built',
 nonzeroOriginalRows=len(rows),formalRelationCount=15,
 allStoredOriginalSixPolynomialSourceProductsReturned=True,
 allFourMissingNSPSProductsReturned=True,
 noOriginalEquationContentDividedByUnpaidFactor=True,
 exactPresentationTheoremUsed='global-three-generators-exact-fifteen-original-relations',
 wholeWExcluded=False)
def strip_chart(poly):
 assert poly
 rest,removed,hist=strip(poly)
 assert rest*removed==poly
 chart_count=0
 while rest.total_degree()>0:
  gg=rest.gcd(Delta.n)
  if gg.total_degree()==0:break
  nxt=rest/gg
  assert nxt*gg==rest
  rest=nxt;removed*=gg;chart_count+=1
 assert removed*rest==poly
 pay_chart(removed)
 return rest,removed,hist,chart_count
def clear_two_row(rr):
 for co in rr:legal(co)
 if not any(rr):return [zero,zero],R(1)
 den=one
 for co in rr:den*=co.d/den.gcd(co.d)
 pay_chart(den)
 pp=[co.n*(den/co.d) for co in rr]
 common=pp[0].gcd(pp[1])
 unused,removed,hist,n=strip_chart(common)
 qq=[v/removed for v in pp]
 assert all(qq[j]*removed==pp[j] for j in range(2))
 scalar=next(v for v in qq if v).coefficient(0)
 qq=[v/scalar for v in qq]
 factor=R(den,removed)/scalar
 assert all(R(qq[j])==factor*rr[j] for j in range(2))
 legal(factor)
 return qq,factor
newrows={};dag={}
for label in wanted:
 if label in labels:
  index=labels.index(label);oldrow=[R(v) for v in rows[index]]
  oldtag=rowtags[index]
 else:
  index=None;oldrow=[R(),R(),R()];oldtag=[R() for _ in range(6)]
 r0,r1,r2=oldrow
 kappa=(-cc*r1+aa*r2)/Delta
 s0=r0+(cc*r1-aa*r2)*p0/Delta
 s1=(p2*r1-p1*r2)/Delta
 # Exact coefficientwise basis-change product, including the Nrow column.
 assert s0+kappa*p0==r0
 assert aa*s1+kappa*p1==r1
 assert cc*s1+kappa*p2==r2
 for co in [kappa,s0,s1]:legal(co)
 out,scale=clear_two_row([s0,s1])
 newrows[label]=out
 # Source DAG: out.(1,z) = scale*(oldtag-kappa*ntag).F6.
 # The old six-variable trace and each new three-coefficient product
 # have already been actually returned; no expanded large trace cache.
 dag[label]=dict(oldIndex=index,scale=scale,kappa=kappa)
 if label=='N1':assert not any(out)
 say(stage='new_exact_original_two_column_row',label=label,
     entries=[profile(v) for v in out],
     allThreeBasisChangeProductsReturned=True,
     polynomialRowScalingProductsReturned=True,
     originalSourceDefinition='scale*(oldtag-kappa*ntag)',
     originalSourceComposedFromActualProducts=True,
     scalarContentRemovedOnlyIfPaidOnH198Complement=True,
     noOriginalMeanConsistencyOrNSPSRelationDropped=True,
     wholeWExcluded=False)
say(stage='new_complete_fifteen_by_two_exact_presentation',
 relationLabels=wanted,rows=15,columns=2,
 basis=['1','z'],samePointCoordinate='z=a*x+c*y',
 determinantOfChangeMatrix='DeltaN=a*p2-c*p1',
 actualN1MapsToItsOwnUnitCoordinate=True,
 originalI6QuotientExactlyPresentedOnH198Complement=True,
 freenessOfOriginalQuotientNotAssumed=True,
 monicQuadraticEnvironmentOnlyIsFree=True,
 wholeH198ZeroBranchRetained=True,
 noLambdaPhysicalDNormInverse=True,wholeWExcluded=False)
def lcontent(poly):
 parts=ns['coefficients_lambda'](R(poly));out=zero
 for co in parts.values():
  assert co.d==one
  out=out.gcd(co.n)
 assert out
 quo=poly/out
 assert quo*out==poly
 return out,quo
pairs=[('two_N1_products',['N1*x','N1*y']),
       ('both_original_NS_PS',['NS','PS'])]
cofactor_records=[]
for name,pair in pairs:
 ra,rb=[newrows[label] for label in pair]
 omega=[rb[1],-ra[1]]
 if not any(omega):
  say(stage='new_two_column_fixed_pair_already_constant',name=name,labels=pair,
      bothZCoefficientsZero=True,
      twoOriginalConstantRows=[profile(ra[0]),profile(rb[0])],
      noDivisionByZeroOrRankAssumption=True,wholeWExcluded=False)
  cofactor_records.append(dict(name=name,constantRows=True))
  continue
 common=omega[0].gcd(omega[1])
 assert common
 primitive=[om/common for om in omega]
 assert all(primitive[j]*common==omega[j] for j in range(2))
 scalar=sum((primitive[j]*[ra,rb][j][0] for j in range(2)),zero)
 assert sum((primitive[j]*[ra,rb][j][1] for j in range(2)),zero)==0
 assert common*scalar==ra[0]*rb[1]-ra[1]*rb[0]
 # Dividing the two actual multipliers is a polynomial operation; the
 # returned two columns give (scalar,0), including the entire common=0.
 say(stage='new_two_column_constant_target_cofactor_returned',name=name,labels=pair,
     cancelledOnlyCommonFactorOfBothMultipliers=profile(common),
     twoExactMultiplierDivisionProductsReturned=True,
     bothOriginalColumnProductsReturned=True,
     scalarOriginalCombination=profile(scalar),
     commonFactorZeroFibrePreservedByNewColumnIdentity=True,
     finalExpandedSixVariableTraceNotClaimed=True,
     exactComposedSource='sum_j primitive_j*scale_j*(oldtag_j-kappa_j*ntag)',
     wholeWExcluded=False)
 if not scalar:
  cofactor_records.append(dict(name=name,zero=True))
  continue
 rest,paid,hist,hcount=strip_chart(scalar)
 qq=rest.coefficient(0);out=rest/qq;unit=paid*qq
 assert unit*out==scalar
 pay_chart(unit)
 multipliers=[R(om,unit) for om in primitive]
 for om in multipliers:legal(om)
 assert sum((multipliers[j]*R([ra,rb][j][0]) for j in range(2)),R())==R(out)
 assert sum((multipliers[j]*R([ra,rb][j][1]) for j in range(2)),R())==0
 cofactor_records.append(dict(name=name,labels=pair,definition=profile(out)))
 say(stage='new_two_column_paid_normalized_original_scalar',name=name,labels=pair,
     definition=profile(out),oldPaidFactorLabelsAndCounts=hist,
     explicitH198ComplementGcdRemovals=hcount,
     allFinalTwoColumnProductsReturned=True,
     allUnpaidWeightAndLambdaLeadingZeroFibresRetained=True,
     noModularSamplingOrMultivariateGcdEmptinessClaim=True,wholeWExcluded=False)
 content,primitive_scalar=lcontent(out)
 say(stage='new_two_column_scalar_full_lambda_content_preserved',name=name,
     unpaidWeightContent=profile(content),
     primitiveLambdaPart=profile(primitive_scalar),
     exactContentProductReturned=True,
     onlyWholeProductIsClaimedInOriginalIdeal=True,
     unpaidContentZeroBranchRetained=True,wholeWExcluded=False)
say(stage='new_W_N1_slope_exact_fifteen_two_columns_and_fixed_pairs_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 exactChart='existing paid W with H198 != 0',
 formalRelationCount=15,allFifteenCoordinateProductsReturned=True,
 fixedPairResults=cofactor_records,
 allOriginalNSPSAndTheirFourProductsRetained=True,
 originalI6ScopeOnly=True,fullIndividualValueSufficiencyNotClaimed=True,
 allUnpaidContentsAndHeadsAndEntireH198ZeroBranchRetained=True,
 noOldNormTwelveResultantModuleOrNativeDeterminantExecuted=True,
 noCoefficientPayloadCacheOrEncodedOutputWritten=True,
 wholeWExcluded=False,ordinaryISPClaim=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
