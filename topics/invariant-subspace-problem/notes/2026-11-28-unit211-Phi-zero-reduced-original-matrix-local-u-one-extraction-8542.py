#!/usr/bin/env python3
"""NEW exact QQ local u=1 extraction for the same reduced original 22 matrix.
Only actual constant-kernel rows transport the long jet; selected
original pivot rows are copied by a verified invertible replacement.
Only the necessary polynomial definition of C22 is reconstructed.
No old determinant, factorization, high-u kernel, or prior local case is run.
The published integral F has exact mod1009,Q=2 (u-1)-order39.  This is an
upper bound, not a substituted assertion.  Every lower bound here is
from the actual QQ(Q) constant kernel and fully transported finite jets.
All parameter pivots are coefficient-field operations, never physical
units.  The final divisibility returns to QQ[u,Q] by monicity of u-1.
Total absolute deadline120 seconds,1GiB. 2026-11-28 Asia/Taipei.
"""
import os,time,json,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq,fmpq_poly
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
sc={"__file__":str(path),"__name__":"new_local_u_one_original_reduced_matrix_definition"}
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
n=22;TARGET=39;INITIAL_PRECISION=TARGET+1
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
M=[matrix_zero() for _ in range(INITIAL_PRECISION)]
initial_returns=0;shift_returns=0
phi=ctx.from_dict({(1,0,0,0,0):fmpq(1),(0,0,0,0,0):fmpq(-1)})
phi_powers=[ctx.from_dict({(0,0,0,0,0):fmpq(1)})]
for a in range(INITIAL_PRECISION):phi_powers.append(phi_powers[-1]*phi)
for i in range(n):
 for j in range(n):
  quotient,remainder=divmod(C[i][j],phi_powers[INITIAL_PRECISION])
  assert quotient*phi_powers[INITIAL_PRECISION]+remainder==C[i][j]
  assert not remainder or int(remainder.degrees()[0])<INITIAL_PRECISION
  by_power=[{} for _ in range(INITIAL_PRECISION)]
  for ex,c in remainder.to_dict().items():
   assert not any(ex[2:])
   a,b=int(ex[0]),int(ex[1])
   for k in range(a+1):
    by_power[k][b]=by_power[k].get(b,0)+c*math.comb(a,k)
  reconstructed=ctx.from_dict({})
  for a,ds in enumerate(by_power):
   M[a][i][j]=fmpq_poly([ds.get(b,0) for b in range(max(ds)+1)]) if ds else Z
   cQ=ctx.from_dict({(0,b,0,0,0):v for b,v in ds.items() if v})
   reconstructed=reconstructed+cQ*phi_powers[a]
  assert reconstructed==remainder
  shift_returns+=1;initial_returns+=1
say("new_local_original_QQ_u_one_jet_definition",
 transverseParameter="u-1",coefficientField="QQ(Q)",
 targetLowerOrder=TARGET,initialPrecision=INITIAL_PRECISION,
 fullOriginalCoefficientTruncationReturns=initial_returns,
 fullInverseShiftReturns=shift_returns,
 constantMatrix=matrix_profile(M[0]),
 knownUpperBoundFromPublishedIntegralPolynomial=39,
 knownModularFactorSHA256="53d44ff6405c0c5a7ff73dd8cfd432024931a9924f4a3ffad16f6932577c9c80",
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
def kernel_echelon(H):
 """Every row transformation is invertible over QQ(Q).
    Skipped constant-zero columns do not change the row space.
    The right half starts at I22; all exact divisions apply to both halves.
 """
 global constant_identity_returns,parameter_content_returns
 W=[[a+Z for a in H[i]]+[O if i==j else Z for j in range(n)] for i in range(n)]
 rank=0;prev=O;pivots=[];swaps=0;order=list(range(n))
 for col in range(n):
  prow=next((i for i in range(rank,n) if W[i][col]),None)
  if prow is None:continue
  if prow!=rank:
   W[rank],W[prow]=W[prow],W[rank]
   order[rank],order[prow]=order[prow],order[rank];swaps+=1
  pivot=W[rank][col];assert pivot and prev
  pivots.append(dict(column=col,pivot=poly_profile(pivot),previous=poly_profile(prev)))
  for i in range(rank+1,n):
   entry=W[i][col]
   for j in range(col+1,2*n):
    W[i][j]=exact_poly(pivot*W[i][j]-entry*W[rank][j],prev)
   W[i][col]=Z
  prev=pivot;rank+=1
  if rank==n:break
 E=[[W[i][n+j] for j in range(n)] for i in range(n)]
 F=[[W[i][j] for j in range(n)] for i in range(n)]
 contents=[]
 for i in range(n):
  gg=Z
  for x in E[i]:
   if x:gg=x if not gg else gg.gcd(x)
  assert gg
  if int(gg.degree())>0:
   E[i]=[exact_poly(x,gg) for x in E[i]]
   F[i]=[exact_poly(x,gg) for x in F[i]]
   parameter_content_returns+=2*n
   contents.append(dict(row=i,content=poly_profile(gg)))
 for i in range(n):
  for j in range(n):
   value=sum((E[i][k]*H[k][j] for k in range(n)),Z)
   assert value==F[i][j]
   constant_identity_returns+=1
 for i in range(rank,n):assert all(not x for x in F[i])
 assert all(any(x for x in E[i]) for i in range(n))
 # Each old pivot row is a triangular nonzero combination of exactly
 # the chosen original rows.  Replacing these pivot rows by the
 # corresponding coordinate unit rows is therefore invertible.
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
 return rank,K,KH,pivots,swaps,contents,selected
def normalize_jet_rows(Jets):
 """Only nonzero QQ[Q] common factors, which are t-adic scalar units."""
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
            transformInvertibility="row swaps; nonzero pivot/previous scaling; nonzero QQ[Q] contents; verified triangular replacement by selected original rows",
            noParameterPivotDeclaredPhysicalUnit=True)
 if nullity==0:
  exact_order=accumulated
  stage.update(exactOrderBecauseConstantMatrixInvertible=exact_order,
               noFurtherTransportNecessary=True)
  rounds.append(stage);say("new_exact_local_u_one_constant_kernel_round",**stage)
  break
 # The verified zero rows alone already give nullity new factors of u-1.
 # Stop immediately if that proves the target; no redundant jet gate.
 if accumulated+nullity>=TARGET:
  assert accumulated+nullity<=39
  accumulated+=nullity;exact_order=accumulated
  stage.update(extractedOrderAfter=accumulated,precisionAfter=precision,
               zeroRowsAlreadyProveTargetWithoutFurtherJetTransport=True,
               exactOrderByPublishedModularUpperBound=exact_order)
  rounds.append(stage);say("new_exact_local_u_one_constant_kernel_round",**stage)
  break
 assert precision>=2
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
 rounds.append(stage);say("new_exact_local_u_one_constant_kernel_round",**stage)
assert exact_order is not None
say("new_original_reduced_weight_polynomial_exact_QQ_u_one_order",
 sameOriginalReducedMatrix=True,originalPolynomialName="F=det(C22)",
 coefficientRingConclusion="QQ[u,Q]",
 localOrderLowerBound=accumulated,actualExactUOneOrder=exact_order,
 targetThirtyNineAchieved=(exact_order==TARGET),
 publishedIntegralQ2Mod1009UpperOrder=39,
 targetNeverAssumedForLowerBound=True,
 allParameterZerosRetainedByMonicGaussDivisibility=True,
 noPhysicalParameterPivotInverse=True,
 actualKernelRounds=len(rounds),
 originalCoefficientTruncationReturns=initial_returns,
 originalShiftInverseReturns=shift_returns,
 allExactPolynomialDivisionReturns=division_returns,
 allConstantMatrixTransformationReturns=constant_identity_returns,
 allZeroRowJetDivisionReturns=jet_division_returns,
 coefficientFieldContentReturns=parameter_content_returns,
 transformedJetCoordinateDefinitions=transform_coordinate_definitions,
 noWholePhiExclusionClaim=True,noRecomputablePayloadSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)
