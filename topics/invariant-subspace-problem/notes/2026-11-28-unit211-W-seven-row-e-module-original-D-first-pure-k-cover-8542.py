#!/usr/bin/env python3
"""NEW QQ(k)[e]^6 original D target, seven rows, fraction-free Popov.
Use the already proved simultaneous column identities MC=N*Lambda,
dC=dprime*Lambda. Reconstruct only those necessary native definitions,
then add the one fixed original commutator row (MxMy-MyMx)[4].
The complete old Pprime/Qstar result proves that the seven-row cokernel
is killed by S^98, where S is a product of native paid e-dependent atoms.
A new univariate module algorithm returns S^j*dprime using actual
six-coordinate DAG operations; all new k contents and pivot factors
remain in the final pure-k cover. No original D inverse is used in
the algorithm. No old determinant, norm, characteristic, modular
primary, or 18-row physical-lambda module is replayed.
180 seconds /4GiB. Only small source/parameters/hashes/receipts.
"""
import json,time,hashlib,signal,resource,contextlib,io,math,itertools
from pathlib import Path
from flint import fmpq,fmpq_poly
START=time.perf_counter();DEADLINE=START+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**kw):
 kw['seconds']=time.perf_counter()-START
 print(json.dumps(kw,separators=(',',':')),flush=True)
def digest(obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
path=Path(__file__).with_name('2026-11-28-unit211-W-entire-native-NSPS-y-t-fixed-six-original-determinant-8542.py')
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='eca419501bf348518fe4f36582d417784235cc7c35872f1a1eb180c88b1e537d'
mark=b'\n# A NEW fixed native-coordinate determinant'
assert raw.count(mark)==1
prefix=raw.split(mark)[0]
assert len(prefix)==8074
assert hashlib.sha256(prefix).hexdigest()=='1dbb8a70ac77f5d531339ca26b5a60b8b3c3cc9a37e41eb54808063c11490878'
native={'__file__':str(path),'__name__':'new_D_target_original_rows_only'}
oa=signal.alarm;ot=signal.setitimer
def timer(which,seconds,interval=0.0):
 if which!=signal.ITIMER_REAL:return ot(which,seconds,interval)
 assert not interval
 left=max(.001,DEADLINE-time.perf_counter())
 return ot(which,min(left,float(seconds) if seconds>0 else left),0.0)
def alarm(seconds):return math.ceil(timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=alarm;signal.setitimer=timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+'#new_D_target_prefix','exec'),native)
finally:
 signal.alarm=oa;signal.setitimer=ot
 ot(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
ns=native['ns'];R=native['R'];ctx=native['ctx']
zero,one=native['zero'],native['one'];ep,kp=ns['ep'],ns['kp']
basis=native['basis'];variables=native['variables']
mats=native['matrices'];errors=native['errors']
original=native['original'];verify=native['verify']
paid_poly=native['paid_poly'];paid_scalar=native['paid_scalar']
baseM=[r[:] for r in native['rows']];baseTags=[r[:] for r in native['traces']]
assert native['rows_digest'](baseM)==dict(bytes=1728830,sha256='e5b3bc078fecd6d472d62bcba5ec831e10a2f88a8feaf51beb15ba816a9da9cf')
L=4*kp*ep**2-(kp**2+4*kp+8)*ep-(kp**2+6*kp+8)
assert L
qq_divisions=0;coefficient_checks=0;mod_divisions=0;mod_inverse_count=0
def exact(poly,divisor):
 global qq_divisions
 q=poly/divisor
 assert q*divisor==poly
 qq_divisions+=1;return q
def profile(poly):
 return dict(degrees=list(map(int,poly.degrees()[:2])),
 totalDegree=int(poly.total_degree()),terms=len(poly.to_dict()),
 **digest([[[int(z) for z in m],str(c)] for m,c in sorted(poly.to_dict().items())]))
def rowprofile(row):return dict(
 degrees=[max(int(q.degrees()[i]) for q in row) for i in [0,1]],
 terms=sum(len(q.to_dict()) for q in row),
 **digest([[[[int(z) for z in m],str(c)] for m,c in sorted(q.to_dict().items())] for q in row]))
def transform(row):
 return [row[0]+row[1]/2+row[2]/2+row[4]/4,row[1],row[2],row[3],row[4],row[5]]
def deflate(row):
 transformed=transform(row)
 out=[exact(transformed[0],L),exact(transformed[1],L)]+transformed[2:]
 # Actual forward and reverse constant-coordinate products.
 assert transformed==[out[0]*L,out[1]*L]+out[2:]
 reverse=[out[0]*L-out[1]*L/2-out[2]/2-out[4]/4,
          out[1]*L,out[2],out[3],out[4],out[5]]
 assert reverse==row
 return out
# Original D is a quadratic geometry polynomial; take its true
# four-mean reduction, including the complete original multiplier.
drow,dtag=ns['reduce_six'](ns['symbolic']['Dphysical'])
assert not dtag[4] and not dtag[5]
for c in drow:paid_scalar(c)
for c in dtag:paid_poly(c.d)
den=one
for c in drow:den=exact(den,den.gcd(c.d))*c.d
paid_poly(den)
dpoly=[c.n*exact(den,c.d) for c in drow]
dtrace=[R(den)*c for c in dtag]
assert all(R(dpoly[i])==R(den)*drow[i] for i in range(6))
verify(sum((R(dpoly[i])*basis[i] for i in range(6)),R())-R(den)*ns['symbolic']['Dphysical'],dtrace)
dprime=deflate(dpoly)
baseN=[deflate(row) for row in baseM]
say(stage='necessary_same_original_D_column_input_reconstructed',
 originalKernelColumns=[[1,'1/2','1/2',0,'1/4',0],[0,1,0,0,0,0]],
 constantColumnTransformationDeterminant=1,
 exactLhalf='4*k*e^2-(k^2+4*k+8)*e-(k^2+6*k+8)',
 allBaseRowsAndOriginalDTargetForwardReverseProductsReturned=True,
 QQExactColumnDivisionReturns=qq_divisions,
 originalDTargetMeanTraceReturned=True,
 DTargetPaidDenominator=profile(den),
 deflatedDTarget=rowprofile(dprime),
 deflatedBaseRowProfiles=[rowprofile(r) for r in baseN],
 universalOriginalCofactorIdentity='det(N)*d=dprime*adj(N)*M',
 noLhalfInverse=True,entireLhalfZeroRetained=True,
 noH198OrOtherNewHeadInverse=True,
 originalDTargetValidOnEntireCurrentW=True,
 oldQQNativeDeterminantNotReplayed=True,wholeWExcluded=False)
# The one fixed new row already has a complete original source.
# Reconstruct this row directly, without any old modular selection.
MA,MB=mats[0],mats[1];ix=4
rr=[sum((MA[ix][h]*MB[h][j]-MB[ix][h]*MA[h][j] for h in range(6)),R()) for j in range(6)]
tag=[]
for g in range(6):
 co=variables[0]*errors[1][ix][g]-variables[1]*errors[0][ix][g]
 co+=sum((MB[ix][h]*errors[0][h][g]-MA[ix][h]*errors[1][h][g] for h in range(6)),R())
 tag.append(co)
verify(sum((rr[i]*basis[i] for i in range(6)),R()),tag)
with contextlib.redirect_stdout(io.StringIO()):
 comm_pol,comm_tag=native['clear_original_row'](rr,tag,'fixed_original_xy_commutator_row4')
verify(sum((R(comm_pol[i])*basis[i] for i in range(6)),R()),comm_tag)
commN=deflate(comm_pol)
assert rowprofile(commN)==dict(degrees=[30,41],terms=4775,bytes=186207,
 sha256='3c51635281b8312c2c352bdc4463fd4dd9f6de09d0a603bd12898a4985493f17')
say(stage='new_QQk_e_seven_row_original_D_module_input',
 fixedRows=['NS','PS','yNS','tNS','yPS','tPS','comm_xy_row4'],
 originalSixCoordinatesAndAllSevenTracesReturned=True,
 originalTarget='dprime from the simultaneous original D column identity',
 bothLhalfZeroAndH198ZeroRetained=True,
 mathematicalSupportBound='gcd of all maximal minors divides U; degree_e U=98',
 noOldPQQDeterminantOrModularUnitGateReplayed=True,wholeWExcluded=False)
# Each polynomial is a tuple of QQ[k] coefficients, indexed by e.
# This is the exact univariate coefficient ring QQ(k)[e], implemented
# fraction-free over QQ[k]; no numerical specialization is used.
O=fmpq_poly([1]);Z=fmpq_poly([]);kpoly=fmpq_poly([0,1])
def etrim(a):
 a=list(a)
 while a and not a[-1]:a.pop()
 return tuple(a)
def convert(poly):
 dic={}
 for mm,cc in poly.to_dict().items():
  assert not any(mm[j] for j in range(2,8))
  ee,kk=int(mm[0]),int(mm[1])
  dd=dic.setdefault(ee,{})
  dd[kk]=dd.get(kk,fmpq(0))+cc
 ans=[]
 for ee in range(max(dic,default=-1)+1):
  dd=dic.get(ee,{})
  ans.append(fmpq_poly([dd.get(j,fmpq(0)) for j in range(max(dd,default=-1)+1)]))
 return etrim(ans)
def scale(a,c):return etrim([x*c for x in a])
def eshift(a,j):return (Z,)*j+a if a else ()
def add(a,b,sgn=1):
 return etrim([(a[i] if i<len(a) else Z)+sgn*(b[i] if i<len(b) else Z)
               for i in range(max(len(a),len(b)))])
def emul(a,b):
 if not a or not b:return ()
 out=[Z for _ in range(len(a)+len(b)-1)]
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:out[i+j]=out[i+j]+x*y
 return etrim(out)
def ediag(a):
 return [[[str(c) for c in q.coeffs()] for q in a]]
def rdata(r):return [[[str(c) for c in q.coeffs()] for q in a] for a in r]
def rstat(r):
 return dict(eDegree=max((len(a)-1 for a in r),default=-1),
 kDegree=max((int(q.degree()) for a in r for q in a),default=-1),
 coefficientPolynomials=sum(len(a) for a in r))
def rprofile(r):
 return dict(eDegree=max((len(a)-1 for a in r),default=-1),
 kDegree=max((int(q.degree()) for a in r for q in a),default=-1),
 coefficientPolynomials=sum(len(a) for a in r),
 rationalCoefficients=sum(len(q.coeffs()) for a in r for q in a),
 **digest(rdata(r)))
def leading(r):
 nonzero=[(len(a)-1,j) for j,a in enumerate(r) if a]
 return max(nonzero) if nonzero else None
def rowzero(r):return not any(r)
polynomial_divisions=0;coordinate_returns=0;reduction_count=0
transcript=hashlib.sha256();transcript_bytes=0;node_count=0
cover=O;cover_input_count=0;cover_seen=set();cover_products=0
cover_factors=[];cover_support_degree_bound=0
def qdiv(a,b):
 global polynomial_divisions
 q,r=divmod(a,b)
 assert not r and q*b==a
 polynomial_divisions+=1;return q
def pprofile(a,exact_limit=0):
 obj=dict(degree=int(a.degree()),**digest([str(c) for c in a.coeffs()]))
 if exact_limit:
  ar=[str(c) for c in a.coeffs()]
  if len(json.dumps(ar,separators=(',',':')).encode())<=exact_limit:
   obj['coefficientsAscending']=ar
 return obj
def add_pole(poly,reason):
 global cover_input_count,cover_support_degree_bound
 assert poly
 if int(poly.degree())<=0:return
 mon=poly/poly[poly.degree()]
 key=tuple(str(x) for x in mon.coeffs())
 if key in cover_seen:return
 cover_seen.add(key);cover_input_count+=1;cover_factors.append(mon)
 cover_support_degree_bound+=int(mon.degree())
 # The product of these actual nonzero polynomials is already an
 # exact cover definition. Delay its squarefree LCM until AFTER the
 # new original D identity is complete; this is not a theorem gate.
 # All roots are retained. None is declared to be a physical unit.
def node(op,parents,r,denbound,target_numbound=0,target_power=None,**params):
 global node_count,transcript_bytes
 record=dict(id=node_count,op=op,parents=parents,denBound=denbound,
             targetNumeratorBound=target_numbound,targetPaidSPower=target_power,
             parameters=params,actualRowShape=rstat(r))
 raw=json.dumps(record,separators=(',',':')).encode()
 transcript.update(raw);transcript.update(b'\n');transcript_bytes+=len(raw)+1
 out=dict(id=node_count,row=r,denbound=denbound,numbound=target_numbound,
          targetpower=target_power)
 node_count+=1
 return out
def normalize(a):
 global coordinate_returns
 r=a['row']
 if rowzero(r):return a
 gg=None
 # Pure k content of the WHOLE six-coordinate polynomial row.
 for poly in r:
  for cc in poly:
   if cc:
    gg=cc if gg is None else gg.gcd(cc)
    if int(gg.degree())==0:break
  if gg is not None and int(gg.degree())==0:break
 assert gg
 if int(gg.degree())>0:
  gg=gg/gg[gg.degree()];add_pole(gg,'whole-row pure-k content')
  nr=[etrim([qdiv(cc,gg) for cc in poly]) for poly in r]
  for i in range(6):
   assert scale(nr[i],gg)==r[i];coordinate_returns+=1
  a=node('divide_pure_k_content',[a['id']],nr,
         a['denbound']+int(gg.degree()),a['numbound'],a['targetpower'],
         divisor=[str(c) for c in gg.coeffs()])
  r=nr
 # A rational constant is a QQ unit, not an extra k factor.
 deg,pos=leading(r);cc=r[pos][deg];c=cc[cc.degree()]
 assert c
 if c!=1:
  nr=[etrim([q/c for q in poly]) for poly in r]
  for i in range(6):
   assert scale(nr[i],fmpq_poly([c]))==r[i];coordinate_returns+=1
  a=node('divide_QQ_constant',[a['id']],nr,a['denbound'],
         a['numbound'],a['targetpower'],constant=str(c))
 return a
def cancel(a,b,pos,shift):
 global coordinate_returns,reduction_count
 ar,br=a['row'],b['row']
 db=len(br[pos])-1;da=db+shift
 assert shift>=0 and len(ar[pos])-1==da
 alpha=br[pos][db];beta=ar[pos][da]
 assert alpha and beta
 add_pole(alpha,'nonzero QQ(k) leading coefficient used for module equivalence')
 nr=[add(scale(ar[i],alpha),eshift(scale(br[i],beta),shift),-1) for i in range(6)]
 # Complete six-coordinate original combination, returned additively.
 for i in range(6):
  back=add(nr[i],eshift(scale(br[i],beta),shift))
  assert back==scale(ar[i],alpha);coordinate_returns+=1
 assert len(nr[pos])-1<da
 assert b['targetpower'] is None
 nb=a['numbound']+(int(alpha.degree()) if a['targetpower'] is not None else 0)
 out=node('fraction_free_original_row_reduction',[a['id'],b['id']],nr,
          max(a['denbound'],b['denbound']),nb,a['targetpower'],
          originalColumn=pos,eShift=shift,
          leftMultiplier=[str(c) for c in alpha.coeffs()],
          rightMultiplier=[str(c) for c in beta.coeffs()])
 out=normalize(out);reduction_count+=1
 if reduction_count%20==0:
  say(stage='new_QQk_e_original_module_checkpoint',
      reductions=reduction_count,dagNodes=node_count,
      completeSixCoordinateProducts=coordinate_returns,
      pureKCoverProductDegreeUpperBound=cover_support_degree_bound,
      currentRow=rprofile(out['row']),currentTargetPaidSPower=out['targetpower'],
      noMembershipOrWholeWExclusionClaim=True)
 return out
gens=[]
for i,row in enumerate(baseN+[commN]):
 rr6=[convert(q) for q in row]
 # No mod matrix or approximated coefficient is introduced.
 assert len(rr6)==6
 gens.append(normalize(node('original_D_column_row',[],rr6,0,sourceRow=i)))
# Online weak-Popov row basis in the fixed degree-then-rightmost-position order.
# A swap is only a basis bookkeeping change, never division by an e polynomial.
B={}
for original_node in gens:
 a=original_node
 while not rowzero(a['row']):
  degree,pos=leading(a['row'])
  if pos not in B:
   B[pos]=a;break
  b=B[pos];bd,bp=leading(b['row']);assert bp==pos
  if degree<bd:
   B[pos]=a;a=b;b=B[pos];degree,pos=leading(a['row']);bd,bp=leading(b['row'])
  a=cancel(a,b,pos,degree-bd)
say(stage='new_QQk_e_complete_seven_row_weak_Popov_basis',
 rank=len(B),leadingPositions=sorted(B),
 ePivotDegrees=[leading(B[j]['row'])[0] for j in sorted(B)],
 actualOriginalCoordinateReturnCount=coordinate_returns,
 reductions=reduction_count,dagNodes=node_count,
 poleCoverProductDegreeUpperBound=cover_support_degree_bound,
 actualAllBasisRows=[rprofile(B[j]['row']) for j in sorted(B)],
 originalRowModuleOverQQkPreserved=True,
 noPhysicalKLeadingFactorInvertedWithoutCover=True,wholeWExcluded=False)
assert len(B)==6 and sorted(B)==list(range(6))
assert all(leading(B[j]['row'])[1]==j for j in range(6))
actual_cokernel_length=sum(leading(B[j]['row'])[0] for j in range(6))
assert actual_cokernel_length<=98
say(stage='new_exact_QQk_seven_row_cokernel_length',
    length=actual_cokernel_length,originalBound=98,
    weakPopovLeadingPositionsDistinct=True,
    allPaidESupportRetained=True,wholeWExcluded=False)
def normal_form(a):
 # Reduce the highest REDUCIBLE term, including terms below an
 # irreducible leading term. No lost remainder or hidden scalar inverse.
 while True:
  terms=[]
  for j,pol in enumerate(a['row']):
   if pol:
    degree=len(pol)-1;bd=leading(B[j]['row'])[0]
    if degree>=bd:terms.append((degree,j))
  if not terms:return a
  degree,pos=max(terms);b=B[pos];bd=leading(b['row'])[0]
  a=cancel(a,b,pos,degree-bd)
# Compute the e-squarefree support of the native paid atoms by
# exact QQ[e,k] gcds. Each factor is already paid; no new support is
# inverted. Pure-k contents disappear in this QQ(k)[e] definition.
Smp=one;slabels=[]
for label,atom in native['paid_atoms']:
 if int(atom.degrees()[0])<=0:continue
 derivative=sum((cc*int(mm[0])*ep**(int(mm[0])-1)*kp**int(mm[1])
                 for mm,cc in atom.to_dict().items() if mm[0]),zero)
 assert derivative
 aa=exact(atom,atom.gcd(derivative))
 gg=Smp.gcd(aa);nextS=exact(Smp,gg)*aa
 assert nextS*gg==Smp*aa
 Smp=nextS;slabels.append(label)
paid_poly(Smp)
S=convert(Smp)
assert S and len(S)>1
say(stage='new_same_original_paid_annihilator_product',
 nativePaidAtomLabels=slabels,eDegree=len(S)-1,
 definition=digest(ediag(S)),
 theoreticalExponentBound=98,actualLengthExponentBound=actual_cokernel_length,
 proof='maximal-minor gcd divides U; degree_e U=98; all its e-prime support is in the actual native squarefree S, so U divides S^98',
 actualSquarefreePaidSupportReturned=True,
 noNewWeightUnit=True,wholeWExcluded=False)
target=normalize(node('same_original_D_target',[],[convert(q) for q in dprime],
                      0,0,0,source='dprime from dC=dprime*Lambda'))
success=False
for exponent in range(actual_cokernel_length+1):
 assert target['targetpower']==exponent
 target=normal_form(target)
 say(stage='new_original_D_module_target_remainder',
     paidSPower=exponent,row=rprofile(target['row']),
     actuallyZero=rowzero(target['row']),
     exactSixCoordinateReturns=coordinate_returns,
     currentPureKCoverProductDegreeUpperBound=cover_support_degree_bound,
     currentDAGNodes=node_count,
     actualOriginalDTargetNotJustAnUnrelatedKernelVector=True,
     wholeWExcluded=False)
 if rowzero(target['row']):
  success=True;break
 if exponent==actual_cokernel_length:break
 nr=[emul(pol,S) for pol in target['row']]
 # The multiplication is a direct polynomial convolution in the exact ring.
 # Its six output coordinate definitions are retained in the same source DAG.
 target=node('multiply_by_original_paid_S',[target['id']],nr,
             target['denbound'],target['numbound'],exponent+1,
             originalPaidAtoms=slabels,paidProductDefinition=digest(ediag(S)))
 target=normalize(target)
if not success:
 say(stage='new_original_D_module_unexpected_nonzero_after_proved_bound',
     actualRemainingRow=rprofile(target['row']),
     allOriginalFibresRetained=True,
     noMembershipOrNewCoverClaim=True,
     sourceLogicalAssertToFollow=True,ordinaryISPClaim=False)
 raise AssertionError('new exact module failed the proved paid-support length annihilator bound')
assert rowzero(target['row'])
# The DAG divisions are only QQ constants and k contents. Every factor
# is supported on cover. If depth bounds its coefficient denominators,
# and numb bounds the nonzero target coefficient numerator, cover^(depth+numb)
# times S^exponent*dprime is in the original seven-row module.
power_bound=target['denbound']+target['numbound']
assert power_bound>=0
say(stage='new_complete_QQk_e_original_D_membership_before_cover_simplification',
 targetPaidSPower=exponent,
 actualFinalSixCoordinateTargetZero=True,
 actualNonzeroTargetCoefficientNumeratorSupportedOnCover=True,
 coefficientDenominatorExponentBound=target['denbound'],
 targetCoefficientNumeratorExponentBound=target['numbound'],
 actualPureKCoverPowerBound=power_bound,
 originalColumnIdentities='MC=N*Lambda,dC=dprime*Lambda',
 fullOriginalIdealConsequence='cover^N * D belongs to I6 after only original native weight localization',
 allFiniteKCoverZerosRetained=True,entireLhalfZeroRetained=True,
 entireH198ZeroRetained=True,
 pureKCoverProductDefinition=digest([[str(c) for c in q.coeffs()] for q in cover_factors]),
 pureKCoverProductDegreeUpperBound=cover_support_degree_bound,
 exactSixCoordinateReturns=coordinate_returns,
 exactUnivariatePolynomialDivisionReturns=polynomial_divisions,
 reductions=reduction_count,dagNodes=node_count,
 actualDAGDefinitionBytes=transcript_bytes,
 actualDAGDefinitionSHA256=transcript.hexdigest(),
 noFlatHugeTraceExpansionRequired=True,wholeWExcluded=False,ordinaryISPClaim=False)
# Only now form the squarefree LCM. If this optional representation
# work reaches the resource boundary, the preceding complete original
# D identity and the fixed product-cover definition remain established.
for factor in cover_factors:
 sf=qdiv(factor,factor.gcd(factor.derivative()))
 gg=cover.gcd(sf);piece=qdiv(sf,gg)
 nc=cover*piece
 assert nc*gg==cover*sf
 cover_products+=1;cover=nc/nc[nc.degree()]
assert cover and cover.gcd(cover.derivative()).degree()==0
# Only already-paid pure-k factors are removed. Every other zero stays.
rawcover=cover;paid_removed=O;paid_hist=[]
for label,atom in [('k',kpoly),('k+1',kpoly+1),('k+2',kpoly+2),('k+4',kpoly+4)]:
 g=cover.gcd(atom)
 if int(g.degree())>0:
  cover=qdiv(cover,g);paid_removed=paid_removed*g;paid_hist.append(label)
assert cover*paid_removed==rawcover and cover
cover=cover/cover[cover.degree()]
say(stage='new_exact_pure_k_original_D_module_cover',
 QQCover=pprofile(cover,8192),QQCoverDegree=int(cover.degree()),
 paidPureKFactorsRemoved=paid_hist,
 originalIdealPowerBound=power_bound,originalPaidSPower=exponent,
 mathematicalConclusion='all current physical W points have cover(k)=0',
 wholeCurrentWExcluded=(power_bound==0 or int(cover.degree())==0),
 allUnpaidPureKFactorsRetained=True,
 allLeadingZeroAndLhalfH198FibresCovered=True,
 noNumericalCandidateExhaustionClaim=True,
 coverDefinedByOriginalQQOperationsNotModularEmptiness=True,
 originalDTargetAllSixCoordinatesReturned=True,
 QQCoverSquarefree=int(cover.gcd(cover.derivative()).degree())==0,
 originalDAGDefinitionBytes=transcript_bytes,
 originalDAGDefinitionSHA256=transcript.hexdigest(),
 pureKFactorCount=cover_input_count,
 coverLCMProductReturns=cover_products,
 exactSixCoordinateReturns=coordinate_returns,
 exactUnivariatePolynomialDivisionReturns=polynomial_divisions,
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 noLargeCoefficientCacheEncodedOrSplitPayload=True,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 ordinaryISPClaim=False)
# A small complete univariate residue may supply a later finite model.
# Prime selection uses only this exact monic cover's denominators, before
# any later original-ideal rank test. No bad root is deleted.
def ratpair(c):
 ss=str(c).split('/');return int(ss[0]),int(ss[1]) if len(ss)==2 else 1
good=None
for prime in [1009,1013,1019,1021,1031,1033,1039,1049,1051,1061]:
 if all(ratpair(c)[1]%prime for c in cover.coeffs()):
  good=prime;break
if good is not None:
 coeff=[ratpair(c)[0]%good*pow(ratpair(c)[1]%good,-1,good)%good for c in cover.coeffs()]
 obj=dict(prime=good,degree=len(coeff)-1,**digest(coeff),
          exactMonicQQCoverIntegralAtPrime=True,
          primeSelectedWithoutAnyIdealRankTest=True)
 if len(json.dumps(coeff,separators=(',',':')).encode())<=8192:obj['coefficientsAscending']=coeff
 say(stage='new_exact_cover_good_integral_model_parameter',**obj,
     noRemainingOriginalFibreReturnedByThisRecord=True,wholeWExcluded=(power_bound==0 or int(cover.degree())==0))
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
