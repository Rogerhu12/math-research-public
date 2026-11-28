#!/usr/bin/env python3
"""NEW first infinity Schur kernel of the fixed original Phi 22 matrix.
Keep the actual previously paid rank14 pivot COLUMNS. Select a
nonzero14 ROW minor only to define complete kernel bases, and return
its exact QQ[Q] adjugate in both directions. Form both actual kernels
and the new 8x8 first-jet matrix U*N1*V, then return its QQ(Q) rank.
No old22 augmented rank, Hungarian or modular determinant is rerun.
Rank3 closes the remaining five orders using the already-paid mod789.
120 seconds /1 GiB inclusive of original definition prefixes.
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
sc={"__file__":str(path),"__name__":"new_original22_first_jet_definition"}
oa=signal.alarm;ot=signal.setitimer
def bounded_timer(which,seconds,interval=0):
 if which!=signal.ITIMER_REAL:return ot(which,seconds,interval)
 left=max(.001,DEADLINE-time.perf_counter())
 return ot(which,min(left,float(seconds) if seconds>0 else left),0)
def bounded_alarm(seconds):return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+":only-original22-column-definition","exec"),sc)
finally:
 signal.alarm=oa;signal.setitimer=ot
 ot(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
R,one,columns,coordinate,exact=[sc[x] for x in ["R","one","columns","coordinate","exact"]]
n=22
ar=[19,18,17,16,14,12,17,16,15,14,12,10,19,18,17,16,14,12,11,10,9,11]
bc=[0,6,7,12,11,44,36,40,36,1,10,11,7,16,17,13,22,45,37,38,39,37]
assert sum(ar)+sum(bc)==802
data=[[[{} for _ in range(n)] for _ in range(n)] for _ in range(2)]
for j,row in enumerate(columns):
 den=one
 for x in row:den=exact(den,den.gcd(x.d))*x.d
 polys=[x.n*exact(den,x.d) for x in row]
 for c,poly in enumerate(polys):
  assert R(poly)==row[c]*R(den)
  for ex,value in poly.to_dict().items():
   assert not ex[3] and not ex[4]
   i=coordinate(c,int(ex[2]));power=ar[i]+bc[j]-int(ex[0])
   assert power>=0
   if power<2:
    d=data[power][i][j];qdegree=int(ex[1])
    d[qdegree]=d.get(qdegree,fmpq(0))+value
def makepoly(d):
 return fmpq_poly([d.get(i,fmpq(0)) for i in range(max(d)+1)]) if d else fmpq_poly([])
H0=[[makepoly(d) for d in row] for row in data[0]]
H1=[[makepoly(d) for d in row] for row in data[1]]
def digest(M):
 return hashlib.sha256(json.dumps([[[str(c) for c in p.coeffs()] for p in row] for row in M],separators=(",",":")).encode()).hexdigest()
assert digest(H0)=="bcbe7bcc2e9a4962af80c1504041aa330edb4903278343f868a46e5d43711b8a"
def maxdeg(M):return max((int(p.degree()) for row in M for p in row),default=-1)
Z=fmpq_poly([]);O=fmpq_poly([1])
p=1009
def qmod(q):
 ab=str(q).split("/");a=int(ab[0]);b=int(ab[1]) if len(ab)>1 else 1
 assert b%p
 return (a%p)*pow(b%p,-1,p)%p
def evalmod(poly,x):
 value=0
 for c in reversed(poly.coeffs()):value=(value*x+qmod(c))%p
 return value
# Actual previous QQ rank14 columns. Only a new small ROW minor is
# chosen here, because the previous receipt did not store row swaps.
J=[0,1,3,4,5,6,7,8,12,13,17,18,19,20]
K=[j for j in range(n) if j not in J]
assert len(J)==14 and len(K)==8
selected=None;minor_samples=[]
for q0 in [2,3,5,7]:
 basis={};I=[]
 for i in range(n):
  v=[evalmod(H0[i][j],q0) for j in J]
  for pivot,row in sorted(basis.items()):
   if v[pivot]:
    f=v[pivot];v=[(x-f*y)%p for x,y in zip(v,row)]
  pivot=next((j for j,x in enumerate(v) if x),None)
  if pivot is not None:
   inv=pow(v[pivot],-1,p);basis[pivot]=[(x*inv)%p for x in v];I.append(i)
  if len(I)==14:break
 minor_samples.append(dict(Q=q0,minorRowsFound=len(I)))
 if len(I)==14:selected=(q0,I);break
if selected is None:
 say("new_first_jet_no_eligible_kernel_minor",
     samples=minor_samples,previousQQRank14Unchanged=True,
     QQDegreeUpperBoundStill794=True,wholePhiExcluded=False)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)
q0,I=selected;L=[i for i in range(n) if i not in I]
A0=[[H0[i][j] for j in J] for i in I]
B0=[[H0[i][j] for j in K] for i in I]
C0=[[H0[i][j] for j in J] for i in L]
say("new_actual_original22_first_jet_and_kernel_minor",
 highestMatrixSHA256=digest(H0),firstJetMatrixSHA256=digest(H1),
 firstJetMaxQDegree=maxdeg(H1),fixedPreviousPivotColumns=J,
 actualMinorRows=I,minorWitnessPrime=p,minorWitnessQ=q0,
 minorSamples=minor_samples,
 onlyKernelBasisSelectionNotOriginalIdealTest=True,
 noOld22AugmentedRankOrModularDeterminantExecuted=True)
returns=0
def exdiv(a,b):
 global returns
 q,r=divmod(a,b)
 assert not r and q*b==a
 returns+=1
 return q
def mm(A,B):
 out=[[Z for _ in range(len(B[0]))] for _ in range(len(A))]
 for i,row in enumerate(A):
  for k,x in enumerate(row):
   if x:
    for j,y in enumerate(B[k]):
     if y:out[i][j]=out[i][j]+x*y
 return out
# Complete exact14 adjugate by fraction-free Gauss-Jordan.
d=14
aug=[A0[i][:]+[O if i==j else Z for j in range(d)] for i in range(d)]
prev=O;adj_pivots=[];swaps=0
for k in range(d):
 pivotrow=next((i for i in range(k,d) if aug[i][k]),None)
 assert pivotrow is not None
 if pivotrow!=k:aug[k],aug[pivotrow]=aug[pivotrow],aug[k];swaps+=1
 pivot=aug[k][k];assert pivot and prev
 for i in range(d):
  if i==k:continue
  entry=aug[i][k]
  for j in range(2*d):
   if j!=k:aug[i][j]=exdiv(pivot*aug[i][j]-entry*aug[k][j],prev)
  aug[i][k]=Z
 prev=pivot;adj_pivots.append(int(pivot.degree()))
Delta=aug[0][0];assert Delta
for i in range(d):
 for j in range(d):assert aug[i][j]==(Delta if i==j else Z)
Adj=[row[d:] for row in aug]
for product in [mm(A0,Adj),mm(Adj,A0)]:
 for i in range(d):
  for j in range(d):assert product[i][j]==(Delta if i==j else Z)
CB=mm(C0,Adj);AB=mm(Adj,B0)
U=[[Z for _ in range(n)] for _ in range(8)]
V=[[Z for _ in range(8)] for _ in range(n)]
for i in range(8):
 for j in range(14):U[i][I[j]]=-CB[i][j]
 U[i][L[i]]=Delta
for j in range(8):
 for i in range(14):V[J[i]][j]=-AB[i][j]
 V[K[j]][j]=Delta
for prod in [mm(U,H0),mm(H0,V)]:
 assert all(not x for row in prod for x in row)
kernel_returns=8*n+n*8
S=mm(mm(U,H1),V)
say("new_complete_QQ_original_left_right_kernels_and_first_Schur",
 minorRows=I,minorColumns=J,
 actualMinorScalarQDegree=int(Delta.degree()),
 actualMinorScalarSHA256=hashlib.sha256(str(Delta).encode()).hexdigest(),
 both14AdjugateProductReturns=2*d*d,
 completeLeftAndRightKernelReturns=kernel_returns,
 leftAndRightKernelDimension=8,
 kernelFullRankWitness="nonpivot8 blocks both equal Delta*I8",
 kernelScalarNotAssumedPhysicalUnit=True,
 exactAdjugateDivisionReturns=returns,
 leftKernelSHA256=digest(U),rightKernelSHA256=digest(V),
 firstSchurMatrixSHA256=digest(S),
 firstSchurMatrixMaxQDegree=maxdeg(S))
# Only a QQ(Q) rank is needed. Remove exact common polynomial row
# and column contents to keep this NEW8 matrix small; all divisions
# are returned, and these factors are NOT physical weight units.
T=[row[:] for row in S];contents=[]
for i in range(8):
 g=Z
 for x in T[i]:
  if x:g=x if not g else g.gcd(x)
 if g and int(g.degree())>0:
  T[i]=[exdiv(x,g) for x in T[i]]
  contents.append(dict(axis="row",index=i,degree=int(g.degree())))
for j in range(8):
 g=Z
 for i in range(8):
  x=T[i][j]
  if x:g=x if not g else g.gcd(x)
 if g and int(g.degree())>0:
  for i in range(8):T[i][j]=exdiv(T[i][j],g)
  contents.append(dict(axis="column",index=j,degree=int(g.degree())))
W=[T[i][:]+[O if i==j else Z for j in range(8)] for i in range(8)]
rank=0;prev=O;pivots=[]
for col in range(8):
 prow=next((i for i in range(rank,8) if W[i][col]),None)
 if prow is None:continue
 if prow!=rank:W[rank],W[prow]=W[prow],W[rank]
 pivot=W[rank][col];assert pivot and prev
 for i in range(rank+1,8):
  entry=W[i][col]
  for j in range(col+1,16):W[i][j]=exdiv(pivot*W[i][j]-entry*W[rank][j],prev)
  W[i][col]=Z
 pivots.append(dict(row=rank,column=col,pivotQDegree=int(pivot.degree())))
 prev=pivot;rank+=1
 if rank==8:break
Transform=[r[8:] for r in W];Echelon=[r[:8] for r in W]
assert mm(Transform,T)==Echelon
for i in range(rank,8):assert all(not x for x in Echelon[i])
for x in pivots:assert Echelon[x["row"]][x["column"]]
order=8+(8-rank);upper=802-order
assert upper>=789 and upper<=794
say("new_actual_first_kernel_Schur_rank_and_original_degree",
 firstSchurRankOverQQQ=rank,
 exactContentDivisionProfile=contents,
 kernelRankMatrixAfterContentMaxQDegree=maxdeg(T),
 whole8RowTransformationReturns=64,
 firstSchurPivots=pivots,
 totalExactPolynomialDivisionReturns=returns,
 previouslyPaidHighestRank=14,firstInfinityOrder=8,
 additionalFirstSchurOrder=8-rank,
 determinantInfinityOrderLowerBound=order,
 improvedGlobalQQ_uDegreeUpperBound=upper,
 alreadyPaidOriginalModularDegree=789,
 alreadyPaidOriginalModularLeadingCoefficient=790,
 exactQQDegree789AndQ2p1009PreservationProved=(upper==789),
 originalFixed22SourceSHA256="043ffc06d0a48f804111ff35cbfee0922fe9a69c87c414f75099b8413cf4b53e",
 alreadyPaidOriginalModularPolynomialSHA256="2b40bf98b99fb097b4d24d3d1f21291b782a2dc0678f756838fe2789343e192b",
 noHigherJetOrOldFullRankOrModularDeterminantRepeated=True,
 noPhysicalWeightZeroFiberRemovedByQQQKernels=True,
 wholeH42ZeroRetained=True,wholePhiExcluded=False,ordinaryISPClaim=False,
 noRecomputablePolynomialOrMatrixPayloadSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)
