#!/usr/bin/env python3
"""NEW second infinity Schur on the remaining3 dimensional kernel.
Reuse only the fixed actual fourteen-block kernel definitions.
Return H2 and the full inverse correction, then obtain the full
three-dimensional kernels of the already-paid rank5 first Schur
from a new5 minor. The corrected3 matrix is contracted directly.
No old8 rank, old22 rank, Hungarian or modular determinant replay.
120 seconds /1 GiB inclusive of necessary original definitions.
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
sc={"__file__":str(path),"__name__":"new_original22_second_jet_definition"}
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
data=[[[{} for _ in range(n)] for _ in range(n)] for _ in range(3)]
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
   if power<3:
    d=data[power][i][j];qdegree=int(ex[1])
    d[qdegree]=d.get(qdegree,fmpq(0))+value
def makepoly(d):
 return fmpq_poly([d.get(i,fmpq(0)) for i in range(max(d)+1)]) if d else fmpq_poly([])
H0=[[makepoly(d) for d in row] for row in data[0]]
H1=[[makepoly(d) for d in row] for row in data[1]]
H2=[[makepoly(d) for d in row] for row in data[2]]
def digest(M):
 return hashlib.sha256(json.dumps([[[str(c) for c in p.coeffs()] for p in row] for row in M],separators=(",",":")).encode()).hexdigest()
assert digest(H0)=="bcbe7bcc2e9a4962af80c1504041aa330edb4903278343f868a46e5d43711b8a"
def maxdeg(M):return max((int(p.degree()) for row in M for p in row),default=-1)
Z=fmpq_poly([]);O=fmpq_poly([1])
# These are the already-returned original minor indices. No old
# highest-matrix rank or modular minor selection is executed.
J=[0,1,3,4,5,6,7,8,12,13,17,18,19,20]
I=[0,1,2,3,4,5,9,10,11,16,17,18,19,20]
K=[j for j in range(n) if j not in J]
L=[i for i in range(n) if i not in I]
assert len(I)==len(J)==14 and len(K)==len(L)==8
A0=[[H0[i][j] for j in J] for i in I]
B0=[[H0[i][j] for j in K] for i in I]
C0=[[H0[i][j] for j in J] for i in L]
say("new_actual_original22_second_jet_definition",
 highestMatrixSHA256=digest(H0),firstJetMatrixSHA256=digest(H1),
 secondJetMatrixSHA256=digest(H2),secondJetMaxQDegree=maxdeg(H2),
 fixedAlreadyPaidMinorRows=I,fixedAlreadyPaidMinorColumns=J,
 noOldRankOrPointSelectionRepeated=True)
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
assert digest(S)=="5568e61824cb876cc7b91db7d970595f40816dad1c1c44eee7f4f7407c0ab31b"
# These contents define only constant QQ(Q) coordinate scales.
# Keep their exact values for transporting the NEW second term.
T=[row[:] for row in S];rscale=[O for _ in range(8)];cscale=[O for _ in range(8)]
for i in range(8):
 g=Z
 for x in T[i]:
  if x:g=x if not g else g.gcd(x)
 if g and int(g.degree())>0:
  rscale[i]=g;T[i]=[exdiv(x,g) for x in T[i]]
for j in range(8):
 g=Z
 for i in range(8):
  x=T[i][j]
  if x:g=x if not g else g.gcd(x)
 if g and int(g.degree())>0:
  cscale[j]=g
  for i in range(8):T[i][j]=exdiv(T[i][j],g)
for i in range(8):
 for j in range(8):assert T[i][j]*rscale[i]*cscale[j]==S[i][j]
# The actual first-Schur rank5 columns are fixed. Choose only a
# nonzero5-row minor to define its kernel; no old8 rank is rerun.
J2=[1,2,5,6,7];K2=[j for j in range(8) if j not in J2]
def evalq(poly,x):
 y=fmpq(0)
 for c in reversed(poly.coeffs()):y=y*x+c
 return y
selected=None;samples=[]
for q0 in [2,3,5,7]:
 basis={};I2=[]
 for i in range(8):
  v=[evalq(T[i][j],q0) for j in J2]
  for pivot,row in sorted(basis.items()):
   if v[pivot]:
    f=v[pivot];v=[x-f*y for x,y in zip(v,row)]
  pivot=next((j for j,x in enumerate(v) if x),None)
  if pivot is not None:
   f=v[pivot];basis[pivot]=[x/f for x in v];I2.append(i)
  if len(I2)==5:break
 samples.append(dict(Q=q0,minorRowsFound=len(I2)))
 if len(I2)==5:selected=(q0,I2);break
if selected is None:
 say("new_second_kernel_no_eligible_minor",
     samples=samples,previousRank5AndDegreeUpper791Unchanged=True,
     exact789Claim=False,wholePhiExcluded=False)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)
q0,I2=selected;L2=[i for i in range(8) if i not in I2]
A2=[[T[i][j] for j in J2] for i in I2]
B2=[[T[i][j] for j in K2] for i in I2]
C2=[[T[i][j] for j in J2] for i in L2]
d2=5
aug2=[A2[i][:]+[O if i==j else Z for j in range(d2)] for i in range(d2)]
prev=O
for k in range(d2):
 prow=next((i for i in range(k,d2) if aug2[i][k]),None);assert prow is not None
 if prow!=k:aug2[k],aug2[prow]=aug2[prow],aug2[k]
 pivot=aug2[k][k];assert pivot and prev
 for i in range(d2):
  if i==k:continue
  entry=aug2[i][k]
  for j in range(2*d2):
   if j!=k:aug2[i][j]=exdiv(pivot*aug2[i][j]-entry*aug2[k][j],prev)
  aug2[i][k]=Z
 prev=pivot
Delta2=aug2[0][0];assert Delta2
for i in range(d2):
 for j in range(d2):assert aug2[i][j]==(Delta2 if i==j else Z)
Adj2=[row[d2:] for row in aug2]
for prod in [mm(A2,Adj2),mm(Adj2,A2)]:
 for i in range(d2):
  for j in range(d2):assert prod[i][j]==(Delta2 if i==j else Z)
CA2=mm(C2,Adj2);AB2=mm(Adj2,B2)
U2=[[Z for _ in range(8)] for _ in range(3)]
V2=[[Z for _ in range(3)] for _ in range(8)]
for i in range(3):
 for j in range(5):U2[i][I2[j]]=-CA2[i][j]
 U2[i][L2[i]]=Delta2
for j in range(3):
 for i in range(5):V2[J2[i]][j]=-AB2[i][j]
 V2[K2[j]][j]=Delta2
assert all(not x for row in mm(U2,T) for x in row)
assert all(not x for row in mm(T,V2) for x in row)
def lcmpolys(seq):
 out=O
 for p0 in seq:out=exdiv(out,out.gcd(p0))*p0
 return out
lr,lc=lcmpolys(rscale),lcmpolys(cscale)
Uh=[[U2[i][j]*exdiv(lr,rscale[j]) for j in range(8)] for i in range(3)]
Vh=[[exdiv(lc,cscale[i])*V2[i][j] for j in range(3)] for i in range(8)]
assert all(not x for row in mm(Uh,S) for x in row)
assert all(not x for row in mm(S,Vh) for x in row)
# Contract before constructing any8x8 high-degree second matrix.
# Complete original block Schur is
# t*Delta^-2 S + t^2*Delta^-3 W2 + O(t^3), where
# W2=Delta*U H2 V - (U H1[:,J])Adj(H1[I,:] V).
Left=mm(Uh,U);Right=mm(V,Vh)
assert all(not x for row in mm(mm(Left,H1),Right) for x in row)
direct=mm(mm(Left,H2),Right)
crossL=mm(Left,[[H1[i][j] for j in J] for i in range(n)])
crossR=mm([[H1[i][j] for j in range(n)] for i in I],Right)
correction=mm(mm(crossL,Adj),crossR)
Second=[[Delta*direct[i][j]-correction[i][j] for j in range(3)] for i in range(3)]
say("new_complete_second_kernel_and_inverse_corrected_three_matrix",
 original14MinorScalarDegree=int(Delta.degree()),
 firstSchurKernelMinorRows=I2,firstSchurKernelMinorColumns=J2,
 new5MinorSelectionSamples=samples,new5MinorScalarDegree=int(Delta2.degree()),
 new5AdjugateProductReturns=50,
 new3KernelCoordinateReturns=48,
 transportedOriginal8KernelCoordinateReturns=48,
 firstJetOnRemaining3KernelZeroReturns=9,
 fullRankWitness="both new complement3 blocks are Delta2*I3; all scales nonzero",
 secondJetMatrixSHA256=digest(H2),
 new3LeftKernelSHA256=digest(Uh),new3RightKernelSHA256=digest(Vh),
 fullInverseCorrectionMatrixSHA256=digest(correction),
 correctedSecond3MatrixSHA256=digest(Second),
 correctedSecond3MaxQDegree=maxdeg(Second),
 allKernelScalesOnlyQQQNotPhysicalUnits=True,
 noOld8RankOrOriginal22RankRepeated=True)
R3=[row[:] for row in Second];contents=[]
for i in range(3):
 g=Z
 for x in R3[i]:
  if x:g=x if not g else g.gcd(x)
 if g and int(g.degree())>0:
  R3[i]=[exdiv(x,g) for x in R3[i]]
  contents.append(dict(axis="row",index=i,degree=int(g.degree())))
for j in range(3):
 g=Z
 for i in range(3):
  x=R3[i][j]
  if x:g=x if not g else g.gcd(x)
 if g and int(g.degree())>0:
  for i in range(3):R3[i][j]=exdiv(R3[i][j],g)
  contents.append(dict(axis="column",index=j,degree=int(g.degree())))
W=[R3[i][:]+[O if i==j else Z for j in range(3)] for i in range(3)]
rank=0;prev=O;pivots=[]
for col in range(3):
 prow=next((i for i in range(rank,3) if W[i][col]),None)
 if prow is None:continue
 if prow!=rank:W[rank],W[prow]=W[prow],W[rank]
 pivot=W[rank][col];assert pivot and prev
 for i in range(rank+1,3):
  entry=W[i][col]
  for j in range(col+1,6):W[i][j]=exdiv(pivot*W[i][j]-entry*W[rank][j],prev)
  W[i][col]=Z
 pivots.append(dict(row=rank,column=col,pivotQDegree=int(pivot.degree())))
 prev=pivot;rank+=1
 if rank==3:break
Transform=[r[3:] for r in W];Echelon=[r[:3] for r in W]
assert mm(Transform,R3)==Echelon
for i in range(rank,3):assert all(not x for x in Echelon[i])
for pp in pivots:assert Echelon[pp["row"]][pp["column"]]
order=8+3+(3-rank);upper=802-order
assert 789<=upper<=791
say("new_actual_second_kernel_Schur_rank_and_original_degree",
 correctedSecondKernelRankOverQQQ=rank,
 secondKernelContentDivisions=contents,
 rankMatrixMaxQDegree=maxdeg(R3),
 whole3RankTransformationReturns=9,new3RankPivots=pivots,
 totalExactPolynomialDivisionReturns=returns,
 previouslyPaidHighestRank=14,previouslyPaidFirstSchurRank=5,
 determinantInfinityOrderLowerBound=order,
 improvedGlobalQQ_uDegreeUpperBound=upper,
 alreadyPaidOriginalModularDegree=789,
 alreadyPaidOriginalModularLeadingCoefficient=790,
 exactQQDegree789AndQ2p1009PreservationProved=(upper==789),
 originalFixed22SourceSHA256="043ffc06d0a48f804111ff35cbfee0922fe9a69c87c414f75099b8413cf4b53e",
 alreadyPaidOriginalModularPolynomialSHA256="2b40bf98b99fb097b4d24d3d1f21291b782a2dc0678f756838fe2789343e192b",
 noOriginalModularDeterminantOrOldRankGateRepeated=True,
 noPhysicalQZeroFiberRemoved=True,wholeH42ZeroRetained=True,
 wholePhiExcluded=False,ordinaryISPClaim=False,
 noRecomputableMatrixOrPolynomialPayloadSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)
