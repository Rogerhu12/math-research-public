#!/usr/bin/env python3
"""NEW QQ(Q) highest-matrix rank for the fixed original Phi 22 determinant.
Use its already-paid exact u-degree dual, form the actual QQ[Q]
highest22 matrix, and perform complete fraction-free polynomial row
operations with an augmented identity. Every division and the final
22x22 row-transformation identity are returned. No old Hungarian,
modular determinant, matrix selection, or higher-order lift is run.
If rank9 is returned, the infinity determinant order is at least13;
combine only with the already-published true mod degree789 to conclude
QQ degree789 and Q=2/p1009 preservation. Other ranks stay explicit.
120 seconds /1 GiB inclusive of necessary source prefixes.
2026-11-28 Asia/Taipei.
"""
import os,time,json,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq_poly,fmpq
START=time.perf_counter();DEADLINE=START+120
signal.setitimer(signal.ITIMER_REAL,120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
name="2026-11-28-unit211-Phi-zero-unlowered-twenty-two-original-columns-and-fixed-u-degree-8542.py"
path=Path(os.environ.get("ISP_PHI_RAW_TWENTYTWO_SOURCE",str(Path(__file__).with_name(name))))
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="043ffc06d0a48f804111ff35cbfee0922fe9a69c87c414f75099b8413cf4b53e"
mark=b"\nN=22\n";assert raw.count(mark)==1
prefix=raw.split(mark)[0]
assert len(prefix)==4080
assert hashlib.sha256(prefix).hexdigest()=="d6e4f9f2eaabf58efe7a06c7b4b4da8b3effb77cadc3f881c4a5ba12a3804e89"
sc={"__file__":str(path),"__name__":"new_fixed22_original_definition_only"}
oa=signal.alarm;ot=signal.setitimer
def bounded_timer(which,seconds,interval=0):
 if which!=signal.ITIMER_REAL:return ot(which,seconds,interval)
 left=max(.001,DEADLINE-time.perf_counter())
 return ot(which,min(left,float(seconds) if seconds>0 else left),0)
def bounded_alarm(seconds):return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+":only-fixed22-original-column-definition","exec"),sc)
finally:
 signal.alarm=oa;signal.setitimer=ot
 ot(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
R,one,geo,columns,coordinate,exact=[
 sc[x] for x in ["R","one","geo","columns","coordinate","exact"]]
N=22
a=[19,18,17,16,14,12,17,16,15,14,12,10,19,18,17,16,14,12,11,10,9,11]
b=[0,6,7,12,11,44,36,40,36,1,10,11,7,16,17,13,22,45,37,38,39,37]
assert len(a)==len(b)==N and sum(a)+sum(b)==802
hd=[[{} for _ in range(N)] for _ in range(N)]
entryChecks=0;columnChecks=0
for j,row in enumerate(columns):
 den=one
 for value in row:
  assert geo["weight_only"](value.d)
  den=exact(den,den.gcd(value.d))*value.d
 polys=[value.n*exact(den,value.d) for value in row]
 # These are precisely the former B22 columns: the actual former
 # receipt returned p-Gauss exponent0 for ALL22 columns. No new
 # constant or parameter normalization is made here.
 for c in range(3):
  assert R(polys[c])==row[c]*R(den);columnChecks+=1
  for ex,value in polys[c].to_dict().items():
   assert not ex[3] and not ex[4]
   i=coordinate(c,int(ex[2]));bound=a[i]+b[j]
   assert int(ex[0])<=bound;entryChecks+=1
   if int(ex[0])==bound:
    qdegree=int(ex[1])
    hd[i][j][qdegree]=hd[i][j].get(qdegree,fmpq(0))+value
def pol(d):
 if not d:return fmpq_poly([])
 return fmpq_poly([d.get(i,fmpq(0)) for i in range(max(d)+1)])
H=[[pol(hd[i][j]) for j in range(N)] for i in range(N)]
def matrix_digest(M):
 value=[[[str(c) for c in z.coeffs()] for z in row] for row in M]
 return hashlib.sha256(json.dumps(value,separators=(",",":")).encode()).hexdigest()
def matrix_max_degree(M):
 return max((int(z.degree()) for row in M for z in row),default=-1)
say("new_actual_QQ_Q_highest22_definition",
 originalMatrixSourceSHA256="043ffc06d0a48f804111ff35cbfee0922fe9a69c87c414f75099b8413cf4b53e",
 originalPrime1009GaussExponentsAllZeroFromPriorActualReceipt=True,
 fixedDegreeDualRows=a,fixedDegreeDualColumns=b,
 initialQQ_uDegreeUpperBound=802,
 actualQQCoefficientDegreeChecks=entryChecks,
 completeThreeColumnReturns=columnChecks,
 actualHighestMatrixSHA256=matrix_digest(H),
 highestMatrixMaxQDegree=matrix_max_degree(H),
 highestMatrixNonzeroEntries=sum(bool(z) for row in H for z in row),
 noQSpecializationForRank=True,noPhysicalQParameterInverse=True)
O=fmpq_poly([1]);Z=fmpq_poly([])
A=[H[i][:]+[O if i==j else Z for j in range(N)] for i in range(N)]
rank=0;prev=O;returns=0;swaps=0;pivots=[]
def pexact(x,y):
 global returns
 q,r=divmod(x,y)
 assert not r and q*y==x
 returns+=1
 return q
# This is elimination of the NEW highest matrix alone. The right
# identity block records a genuine polynomial row transformation.
# Every step is invertible over QQ(Q), because its recorded pivots
# and previous pivot are nonzero polynomials; their Q zeros are
# never removed from the original Phi graph.
for col in range(N):
 pivotrow=next((i for i in range(rank,N) if A[i][col]),None)
 if pivotrow is None:continue
 if pivotrow!=rank:
  A[rank],A[pivotrow]=A[pivotrow],A[rank];swaps+=1
 pivot=A[rank][col]
 assert pivot and prev
 for i in range(rank+1,N):
  entry=A[i][col]
  for j in range(col+1,2*N):
   A[i][j]=pexact(pivot*A[i][j]-entry*A[rank][j],prev)
  A[i][col]=Z
 pivots.append(dict(row=rank,column=col,pivotQDegree=int(pivot.degree()),
                    previousQDegree=int(prev.degree())))
 prev=pivot;rank+=1
 say("new_QQ_Q_highest22_fraction_free_pivot",
     rank=rank,pivot=pivots[-1],
     completePolynomialDivisionReturns=returns)
 if rank==N:break
E=[row[N:] for row in A];F=[row[:N] for row in A]
identityReturns=0
for i in range(N):
 for j in range(N):
  q=Z
  for k in range(N):q=q+E[i][k]*H[k][j]
  assert q==F[i][j];identityReturns+=1
for i in range(rank,N):assert all(not z for z in F[i])
for x in pivots:assert F[x["row"]][x["column"]]
upper=802-(N-rank)
# The former fixed22 determinant has true reduction degree789 and
# leading coefficient790 at Q=2,p=1009. It is NOT recomputed here.
assert upper>=789
say("new_actual_QQ_Q_highest_rank_and_global_u_bound",
 rankOverQQQ=rank,numberOfZeroTransformedRows=N-rank,
 wholeRowTransformationIdentityReturns=identityReturns,
 rowTransformationInvertibleOverQQQ=True,
 exactPolynomialDivisionReturns=returns,rowSwaps=swaps,
 actualHighestMatrixSHA256=matrix_digest(H),
 actualRowTransformationSHA256=matrix_digest(E),
 actualEchelonMatrixSHA256=matrix_digest(F),
 allPivots=pivots,
 initialDegreeUpperBound=802,
 determinantInfinityValuationLowerBound=N-rank,
 improvedGlobalQQ_uDegreeUpperBound=upper,
 alreadyPaidActualModularDegree=789,
 alreadyPaidActualModularLeadingCoefficient=790,
 alreadyPaidActualModularPolynomialSHA256="2b40bf98b99fb097b4d24d3d1f21291b782a2dc0678f756838fe2789343e192b",
 exactQQDegreeAndQ2p1009PreservationProved=(upper==789),
 noOldHungarianOrModularDeterminantRepeated=True,
 noHigherOrderSeriesOrKernelLiftExecuted=True,
 allPhysicalWeightAndH42ZeroBranchesRetained=True,
 wholePhiExcluded=False,ordinaryISPClaim=False,
 noRecomputableMatrixOrPolynomialPayloadSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)
