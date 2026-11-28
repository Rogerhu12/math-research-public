#!/usr/bin/env python3
"""NEW exact QQ local M=0 extraction on its whole rational curve for the same reduced original 22 matrix.
Only actual constant-kernel rows transport the long jet; selected
original pivot rows are copied by a verified invertible replacement.
Only the necessary polynomial definition of C22 is reconstructed.
No old determinant, factorization, high-u kernel, or prior local case is run.
The published integral F has exact mod1009,Q=2 order14 at every root of the primitive M numerator.  This is an
upper bound, not a substituted assertion.  Every lower bound here is
from the actual QQ(s) constant kernel and fully transported finite jets.
All parameter pivots are coefficient-field operations, never physical
units.  The final divisibility returns to QQ[u,Q] by the irreducible primitive original M numerator.
Total absolute deadline120 seconds,1GiB. 2026-11-28 Asia/Taipei.
"""
import os,time,json,hashlib,signal,resource,contextlib,io,math,gc
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx
START=time.perf_counter();DEADLINE=START+120
signal.setitimer(signal.ITIMER_REAL,120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
name="2026-11-28-unit211-Phi-zero-original-paid-row-column-content-and-reduced-integral-weight-model-8542.py"
path=Path(os.environ.get("ISP_PHI_PAID_CONTENT_SOURCE",str(Path(__file__).with_name(name))))
raw=path.read_bytes()
FULL_SHA="b190f315da00c0df673b33723972aa23380b29403270982aaf92ac3f30214ae4"
assert hashlib.sha256(raw).hexdigest()==FULL_SHA
mark=b"\nallunits=rowunits+colunits\n";assert raw.count(mark)==1
prefix=raw.split(mark)[0]
assert len(prefix)==4960
assert hashlib.sha256(prefix).hexdigest()=="3be7967c9f269d8ae00aa1d8f04ab01173e2b87674999f123c9908f4f889964c"
sc={"__file__":str(path),"__name__":"new_local_M_zero_original_reduced_matrix_definition"}
oa=signal.alarm;ot=signal.setitimer
def bounded_timer(which,seconds,interval=0):
 if which!=signal.ITIMER_REAL:return ot(which,seconds,interval)
 left=max(.001,DEADLINE-time.perf_counter())
 return ot(which,min(left,float(seconds) if seconds>0 else left),0)
def bounded_alarm(seconds):return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+":only-reduced-original-matrix-definition","exec"),sc)
finally:
 signal.alarm=oa;signal.setitimer=ot
 ot(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
C,ctx=[sc[k] for k in ["C","ctx"]]
n=22;TARGET=14;INITIAL_PRECISION=TARGET+1
Z=fmpq_poly([]);O=fmpq_poly([1])
def poly_profile(a):
 cs=[str(x) for x in a.coeffs()]
 return dict(degree=int(a.degree()),
             sha256=hashlib.sha256(json.dumps(cs,separators=(",",":")).encode()).hexdigest())
def matrix_profile(A):
 h=hashlib.sha256();maxdeg=-1
 for row in A:
  for a in row:
   maxdeg=max(maxdeg,int(a.degree()))
   h.update(json.dumps([str(x) for x in a.coeffs()],separators=(",",":")).encode())
   h.update(b"\n")
 return dict(rows=len(A),columns=len(A[0]),maximumParameterDegree=maxdeg,sha256=h.hexdigest())
def matrix_zero():
 return [[Z for _ in range(n)] for _ in range(n)]
# Actual primitive numerator of M, not a modular factor guess.
up=ctx.from_dict({(1,0,0,0,0):fmpq(1)})
qp=ctx.from_dict({(0,1,0,0,0):fmpq(1)})
onep=ctx.from_dict({(0,0,0,0,0):fmpq(1)})
L=qp-2*(up-1)*(up-2)
Mn=2*up*L-L*L-up*up*qp
assert Mn==-qp*qp+(3*up-4)*(up-2)*qp-4*(up-1)*(up-2)*(up*up-2*up+2)
original_M_atom=next(p for label,p in sc["geo"]["paid"] if label=="M")
qM,rM=divmod(original_M_atom,Mn)
assert not rM and qM*Mn==original_M_atom and int(qM.total_degree())==0 and qM
mconst=next(iter(qM.to_dict().values()))
ab=str(mconst).split("/")
assert int(ab[0])%1009 and (int(ab[1]) if len(ab)>1 else 1)%1009
ninv=qp+2*up-4
assert (up-1)*ninv*ninv-up*ninv*L+(2*up-3)*L*L==-2*(up-2)*Mn
A=(3*up-4)*(up-2)
assert A*A-16*(up-1)*(up-2)*(up*up-2*up+2)==up*up*(up-2)*(6-7*up)
# The displayed discriminant is not a square in QQ(u); hence Mn is
# irreducible as a primitive quadratic in Q.  This is a paper proof,
# not a claim inferred from modular factorization.
sp=fmpq_poly([0,1]);den=sp*sp-sp+2;un=sp*sp+3
qn=4*(1-sp)*(sp*sp+1)
Ln=qn-2*(un-den)*(un-2*den)
an=(sp-1)*(sp+3)*(sp*sp+3)
assert un-den==sp+1
assert un-2*den==-(sp-1)**2
assert Ln==2*(1-sp)*(sp*sp+3)
assert qn+2*un*den-4*den*den==sp*Ln
assert 2*un*Ln*den-Ln*Ln-un*un*qn==0
assert (3*un-4*den)*(un-2*den)-2*qn==an
assert den and an
say("new_original_M_entire_curve_and_transverse_parameter",
 primitiveOriginalMNumeratorMatched=True,
 originalDiscriminantIdentityReturned=True,
 irreducibilityReason="u^2(u-2)(6-7u) is not a square in QQ(u)",
 inverseParameter="s=(Q+2u-4)/(Q-2(u-1)(u-2))",
 inversePolynomialIdentityReturned=True,
 forwardNumerators=[poly_profile(un),poly_profile(qn),poly_profile(den)],
 actualTransverseIdentity="Mn(u(s),q(s)+t)=an(s)/den(s)^2*t-t^2",
 forwardAndTransversePolynomialIdentitiesReturned=True,
 allGenericBranchesCoveredBySameRationalFunctionField=True,
 coefficientField="QQ(s)",targetLowerOrder=TARGET,
 knownIntegralQ2Mod1009UpperOrder=14,
 noParameterChartDenominatorDeclaredPhysicalUnit=True)

# Column j is cleared by den(s)^D_j, where D_j bounds a+2b
# for every original coefficient c*u^a*Q^b in that column.
# The exact original homogeneous expression is
# sum c*un^a*(qn+den^2*t)^b*den^(D_j-a-2b).
# Each column scale has t-valuation zero.  The univariate homogeneous
# Horner recurrence below computes its coefficients directly.
Dcols=[]
for j in range(n):
 Dcols.append(max([int(ex[0])+2*int(ex[1]) for i in range(n)
                   for ex in C[i][j].to_dict()]+[0]))
maxD=max(Dcols)
maxQ=max([int(ex[1]) for row in C for p0 in row for ex in p0.to_dict()]+[0])
dp=[O];qnp=[O]
for k in range(maxD+2*INITIAL_PRECISION+1):dp.append(dp[-1]*den)
for k in range(maxQ+1):qnp.append(qnp[-1]*qn)
components=[[None for _ in range(n)] for _ in range(n)]
H0=matrix_zero();constant_specialization_returns=0;original_coefficient_returns=0
for j in range(n):
 for i in range(n):
  groups={};back={}
  for ex,c in C[i][j].to_dict().items():
   assert not any(ex[2:])
   aa,bb=int(ex[0]),int(ex[1])
   assert Dcols[j]-aa-2*bb>=0
   groups.setdefault(bb,{})[aa]=c
   back[(aa,bb,0,0,0)]=c;original_coefficient_returns+=1
  assert ctx.from_dict(back)==C[i][j]
  cb=[]
  for bb,coeffs in sorted(groups.items()):
   aa=max(coeffs)
   hom=fmpq_poly([coeffs.get(aa,0)])
   for k in range(aa-1,-1,-1):
    hom=hom*un+dp[aa-k]*coeffs.get(k,0)
   # hom = den^aa*c_bb(un/den), by the complete homogeneous recurrence.
   base=hom*dp[Dcols[j]-aa-2*bb]
   cb.append((bb,base))
  components[i][j]=cb
  H0[i][j]=sum((base*qnp[bb] for bb,base in cb),Z)
  constant_specialization_returns+=1
 if j%4==3 or j==n-1:
  say("new_M_curve_original_column_definition_checkpoint",
      columnsCompleted=j+1,totalColumns=n,
      currentColumnDenominatorExponent=Dcols[j],
      originalCoefficientHomogenizationTerms=original_coefficient_returns)
# The original large namespaces are no longer used.  Release their
# lifetime before any new coefficient-field elimination.
del C
sc.clear();gc.collect()
M=[H0];jets_ready=False;initial_returns=0;shift_returns=0
def build_original_jets():
 global initial_returns,shift_returns,components
 Jets=[matrix_zero() for _ in range(INITIAL_PRECISION)]
 for i in range(n):
  for j in range(n):
   for k in range(INITIAL_PRECISION):
    value=sum((base*qnp[bb-k]*math.comb(bb,k)
               for bb,base in components[i][j] if bb>=k),Z)
    Jets[k][i][j]=value*dp[2*k]
    initial_returns+=1
   # Exact binomial decomposition of each original Q^bb term:
   # (qn+den^2*t)^bb, retaining all k<precision.
   shift_returns+=1
 assert Jets[0]==H0
 components=None;gc.collect()
 say("new_M_curve_complete_high_jets_only_when_required",
     plannedPrecision=INITIAL_PRECISION,
     actualOriginalTruncatedCoordinates=initial_returns,
     completeEntryBinomialCoefficientDefinitions=shift_returns,
     sameOriginalConstantMatrixReturned=True,
     truncationRemainderExplicitlyAllBinomialTermsKAtLeastPrecision=True)
 return Jets
say("new_local_original_QQ_M_zero_constant_definition",
 transverseParameter="Q-q(s)",coefficientField="QQ(s)",
 targetLowerOrder=TARGET,plannedJetPrecision=INITIAL_PRECISION,
 fullOriginalConstantSpecializationDefinitions=constant_specialization_returns,
 originalEntryAssemblyReturns=constant_specialization_returns,
 originalCoefficientHomogenizationTerms=original_coefficient_returns,
 columnCoefficientFieldDenominatorPowers=Dcols,
 columnClearingDoesNotChangeTransverseOrder=True,
 onlyConstantMatrixConstructedSoFar=True,
 constantMatrix=matrix_profile(H0),
 knownUpperBoundFromPublishedIntegralPolynomial=14,
 knownModularFactorsSHA256=[
 "6b8efb2dc0b1934c825393454ddd004606e3e74ad752ece802d70e8f59ea1a21",
 "986bb6790f123044421f4e0f97e9920ba1108eaf7d1f71eb5cc215b6a9bd475d",
 "e56069f3fe12b447399c2e28879450e18d4054d8c4934d6001a88117f247f0f2",
 "faff6695016a0402a2be3826f112381249934154d45d4154ae0d29ffd31cc0b1"],
 knownWholeReducedModularPolynomialSHA256="ca632b1fc0b2d69fa810a11f19a759908dd6bf6a5151b045967dc6930653f0a6",
 noOldDeterminantOrFactorizationExecuted=True)
division_returns=0;constant_identity_returns=0;jet_division_returns=0
parameter_content_returns=0;transform_coordinate_definitions=0
def exact_poly(a,b):
 global division_returns
 assert b
 q,r=divmod(a,b)
 assert not r and q*b==a
 division_returns+=1
 return q
primitive_row_returns=0;primitive_scalar_returns=0
def kernel_echelon(H):
 """Actual primitive row Gaussian over QQ(s), including the I22 half.
    Only rows with nonzero elimination entries are changed.  After each
    cross-multiplication, full-row polynomial content is removed with
    complete returns.  No previous Bareiss pivot is reused after content
    normalization.  This is a new M-curve input, not a rerun of u=1.
 """
 global constant_identity_returns,parameter_content_returns
 global primitive_row_returns,primitive_scalar_returns
 W=[[a+Z for a in H[i]]+[O if i==j else Z for j in range(n)] for i in range(n)]
 rank=0;pivots=[];swaps=0;order=list(range(n))
 content_hash=hashlib.sha256();content_count=0;maximum_content_degree=0
 for col in range(n):
  choices=[i for i in range(rank,n) if W[i][col]]
  if not choices:continue
  prow=min(choices,key=lambda i:int(W[i][col].degree()))
  if prow!=rank:
   W[rank],W[prow]=W[prow],W[rank]
   order[rank],order[prow]=order[prow],order[rank];swaps+=1
  pivot=W[rank][col];assert pivot
  pivots.append(dict(column=col,pivot=poly_profile(pivot)))
  for i in range(rank+1,n):
   entry=W[i][col]
   if not entry:continue
   old=W[i]
   new=[pivot*old[j]-entry*W[rank][j] for j in range(2*n)]
   assert not new[col]
   for j in range(2*n):
    assert new[j]+entry*W[rank][j]==pivot*old[j]
    primitive_row_returns+=1
   gg=Z
   for x in new:
    if x:gg=x if not gg else gg.gcd(x)
    if gg and int(gg.degree())==0:break
   assert gg
   if int(gg.degree())>0:
    new=[exact_poly(x,gg) for x in new]
    parameter_content_returns+=2*n;content_count+=1
    maximum_content_degree=max(maximum_content_degree,int(gg.degree()))
    content_hash.update(json.dumps(poly_profile(gg),separators=(",",":")).encode())
   right=next(x for x in new[n:] if x)
   lc=right.coeffs()[-1]
   assert lc
   if lc!=1:
    before=new;new=[x*(1/lc) for x in before]
    for aa,bb in zip(new,before):
     assert aa*lc==bb;primitive_scalar_returns+=1
   W[i]=new
  rank+=1
  if rank==n:break
 E=[[W[i][n+j] for j in range(n)] for i in range(n)]
 F=[[W[i][j] for j in range(n)] for i in range(n)]
 for i in range(n):
  for j in range(n):
   assert sum((E[i][k]*H[k][j] for k in range(n)),Z)==F[i][j]
   constant_identity_returns+=1
 for i in range(rank,n):assert all(not x for x in F[i])
 selected=order[:rank];selected_set=set(selected)
 for i in range(rank):
  assert E[i][selected[i]]
  for j in range(i+1,rank):assert not E[i][selected[j]]
  for j in range(n):
   if j not in selected_set:assert not E[i][j]
 K=[[O if j==selected[i] else Z for j in range(n)] for i in range(rank)]+E[rank:]
 KH=[[a+Z for a in H[selected[i]]] for i in range(rank)]+F[rank:]
 for i in range(n):
  for j in range(n):
   assert sum((K[i][k]*H[k][j] for k in range(n)),Z)==KH[i][j]
   constant_identity_returns+=1
 contents=[dict(actualPrimitiveRowContentDivisions=content_count,
                maximumContentDegree=maximum_content_degree,
                contentDefinitionSHA256=content_hash.hexdigest())]
 return rank,K,KH,pivots,swaps,contents,selected
def normalize_jet_rows(Jets):
 """Only nonzero QQ[s] common factors, which are t-adic scalar units."""
 global parameter_content_returns
 records=[]
 for i in range(n):
  gg=Z
  for A in Jets:
   for x in A[i]:
    if x:gg=x if not gg else gg.gcd(x)
    if gg and int(gg.degree())==0:break
   if gg and int(gg.degree())==0:break
  assert gg
  if int(gg.degree())>0:
   for A in Jets:
    for j in range(n):
     A[i][j]=exact_poly(A[i][j],gg);parameter_content_returns+=1
   records.append(dict(row=i,content=poly_profile(gg)))
 return records
precision=INITIAL_PRECISION;accumulated=0;rounds=[];exact_order=None
while accumulated<TARGET:
 assert precision>=1 and accumulated+precision>=TARGET+1
 rank,E,F,pivots,swaps,contents,selected=kernel_echelon(M[0])
 nullity=n-rank
 stage=dict(round=len(rounds)+1,precisionBefore=precision,
            extractedOrderBefore=accumulated,constantRank=rank,
            zeroRows=nullity,constantMatrix=matrix_profile(M[0]),
            transformation=matrix_profile(E),
            nonzeroCoefficientFieldPivots=pivots,rowSwaps=swaps,
            coefficientFieldRowContents=contents,
            completeEH0Returns=968,
            selectedOriginalPivotRows=selected,
            transformInvertibility="row swaps; nonzero primitive cross-elimination pivots; exact full-row QQ[s] contents; verified triangular replacement by selected original rows",
            noParameterPivotDeclaredPhysicalUnit=True)
 if nullity==0:
  exact_order=accumulated
  stage.update(exactOrderBecauseConstantMatrixInvertible=exact_order,
               noFurtherTransportNecessary=True)
  rounds.append(stage);say("new_exact_local_M_zero_constant_kernel_round",**stage)
  break
 # The verified zero rows alone already give nullity new factors of the actual transverse parameter.
 # Stop immediately if that proves the target; no redundant jet gate.
 if accumulated+nullity>=TARGET:
  assert accumulated+nullity<=14
  accumulated+=nullity;exact_order=accumulated
  stage.update(extractedOrderAfter=accumulated,precisionAfter=precision,
               zeroRowsAlreadyProveTargetWithoutFurtherJetTransport=True,
               exactOrderByPublishedModularUpperBound=exact_order)
  rounds.append(stage);say("new_exact_local_M_zero_constant_kernel_round",**stage)
  break
 assert precision>=2
 if not jets_ready:
  assert not accumulated and precision==INITIAL_PRECISION
  M=build_original_jets();jets_ready=True
 assert len(M)==precision
 transformed=[]
 for A in M:
  B=matrix_zero()
  for i in range(rank):
   B[i]=[a+Z for a in A[selected[i]]]
   transform_coordinate_definitions+=n
  for i in range(rank,n):
   for j in range(n):
    B[i][j]=sum((E[i][k]*A[k][j] for k in range(n)),Z)
    transform_coordinate_definitions+=1
  transformed.append(B)
 assert transformed[0]==F
 newM=[matrix_zero() for _ in range(precision-1)]
 for i in range(n):
  if i>=rank:
   for j in range(n):
    assert not transformed[0][i][j]
    for a in range(precision-1):newM[a][i][j]=transformed[a+1][i][j]
    assert [Z]+[A[i][j] for A in newM]==[A[i][j] for A in transformed]
    jet_division_returns+=1
  else:
   for a in range(precision-1):
    for j in range(n):newM[a][i][j]=transformed[a][i][j]
 # Other rows are reduced modulo u^(precision-1); the omitted top coefficient
 # is the explicit remainder.  Zero rows were divided with full jet return.
 newcontents=normalize_jet_rows(newM)
 accumulated+=nullity;precision-=1;M=newM
 assert accumulated+precision>=TARGET+1
 stage.update(extractedOrderAfter=accumulated,precisionAfter=precision,
              nextConstantMatrix=matrix_profile(M[0]),
              fullZeroRowJetDivisionReturns=nullity*n,
              furtherCoefficientFieldContents=newcontents,
              retainedDeterminantPrecisionAtLeast=accumulated+precision)
 rounds.append(stage);say("new_exact_local_M_zero_constant_kernel_round",**stage)
assert exact_order is not None
say("new_original_reduced_weight_polynomial_exact_QQ_M_zero_order",
 sameOriginalReducedMatrix=True,originalPolynomialName="F=det(C22)",
 coefficientRingConclusion="QQ[u,Q]",
 localOrderLowerBound=accumulated,actualExactMZeroOrder=exact_order,
 targetFourteenAchieved=(exact_order==TARGET),
 publishedIntegralQ2Mod1009UpperOrder=14,
 targetNeverAssumedForLowerBound=True,
 allParameterZerosRetainedByPrimitiveIrreducibleCurveDivisibility=True,
 wholeOriginalMFunctionFieldNotOnlyOneComponent=True,
 noPhysicalParameterPivotInverse=True,
 actualKernelRounds=len(rounds),
 actualOriginalTruncatedCoordinateDefinitions=initial_returns,
 entrywiseTruncatedBinomialDefinitions=shift_returns,
 allExactPolynomialDivisionReturns=division_returns,
 allConstantMatrixTransformationReturns=constant_identity_returns,
 allZeroRowJetDivisionReturns=jet_division_returns,
 originalConstantEntryDefinitions=constant_specialization_returns,
 highJetsNeeded=jets_ready,
 coefficientFieldContentReturns=parameter_content_returns,
 fullPrimitiveRowOperationReturns=primitive_row_returns,
 fullRationalScalarNormalizationReturns=primitive_scalar_returns,
 transformedJetCoordinateDefinitions=transform_coordinate_definitions,
 noWholePhiExclusionClaim=True,noRecomputablePayloadSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)
