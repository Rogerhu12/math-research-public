#!/usr/bin/env python3
"""NEW third-order scalar of the same original Phi22 matrix.
Use only the already fixed rank14 and rank5 kernel definitions,
then complete the actual rank2 second kernel by a new2 minor.
Both original14 and subsequent5 Schur inverse corrections are kept.
No old3/8/22 rank, original modular determinant or Hungarian replay.
If the scalar is nonzero, the original degree is790, not789.
The exact coefficient of u790 is recovered from block determinants.
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
sc={"__file__":str(path),"__name__":"new_original22_third_jet_definition"}
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
data=[[[{} for _ in range(n)] for _ in range(n)] for _ in range(4)]
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
   if power<4:
    d=data[power][i][j];qdegree=int(ex[1])
    d[qdegree]=d.get(qdegree,fmpq(0))+value
def makepoly(d):
 return fmpq_poly([d.get(i,fmpq(0)) for i in range(max(d)+1)]) if d else fmpq_poly([])
H0=[[makepoly(d) for d in row] for row in data[0]]
H1=[[makepoly(d) for d in row] for row in data[1]]
H2=[[makepoly(d) for d in row] for row in data[2]]
H3=[[makepoly(d) for d in row] for row in data[3]]
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
say("new_actual_original22_third_jet_definition",
 highestMatrixSHA256=digest(H0),firstJetMatrixSHA256=digest(H1),
 secondJetMatrixSHA256=digest(H2),secondJetMaxQDegree=maxdeg(H2),
 thirdJetMatrixSHA256=digest(H3),thirdJetMaxQDegree=maxdeg(H3),
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
# Both index sets were actually returned by the preceding source.
# Reuse their definition; do not repeat the previous minor search.
I2=[1,2,3,4,7];L2=[i for i in range(8) if i not in I2]
samples=[]
A2=[[T[i][j] for j in J2] for i in I2]
B2=[[T[i][j] for j in K2] for i in I2]
C2=[[T[i][j] for j in J2] for i in L2]
d2=5
aug2=[A2[i][:]+[O if i==j else Z for j in range(d2)] for i in range(d2)]
prev=O;swaps2=0
for k in range(d2):
 prow=next((i for i in range(k,d2) if aug2[i][k]),None);assert prow is not None
 if prow!=k:aug2[k],aug2[prow]=aug2[prow],aug2[k];swaps2+=1
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
say("new_third_input_fixed_lower_kernel_definitions",
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

assert digest(Second)=="4aacdbb9a20536e2ce661f87f1b713267fed2de3a4bd982eb7195788fe08ea75"
# Normalize only to define the final one-dimensional kernels.
T3=[row[:] for row in Second];rs3=[O for _ in range(3)];cs3=[O for _ in range(3)]
for i in range(3):
 g=Z
 for x in T3[i]:
  if x:g=x if not g else g.gcd(x)
 if g:
  rs3[i]=g;T3[i]=[exdiv(x,g) for x in T3[i]]
for j in range(3):
 g=Z
 for i in range(3):
  x=T3[i][j]
  if x:g=x if not g else g.gcd(x)
 if g:
  cs3[j]=g
  for i in range(3):T3[i][j]=exdiv(T3[i][j],g)
for i in range(3):
 for j in range(3):assert T3[i][j]*rs3[i]*cs3[j]==Second[i][j]
J3=[0,1];K3=[2]
chosen=None;last_samples=[]
for q0 in [2,3,5,7]:
 for i0 in range(3):
  for i1 in range(i0+1,3):
   dd=evalq(T3[i0][0],q0)*evalq(T3[i1][1],q0)-evalq(T3[i0][1],q0)*evalq(T3[i1][0],q0)
   if dd:chosen=(q0,[i0,i1]);break
  if chosen is not None:break
 last_samples.append(dict(Q=q0,nonzeroMinorFound=chosen is not None))
 if chosen is not None:break
if chosen is None:
 say("new_third_scalar_no_eligible_kernel_minor",
     samples=last_samples,previousDegreeUpper790Unchanged=True,
     noDegree789Or790EqualityClaim=True,wholePhiExcluded=False)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)
q0,I3=chosen;L3=[i for i in range(3) if i not in I3]
A3=[[T3[i][j] for j in J3] for i in I3]
B3=[[T3[i][j] for j in K3] for i in I3]
C3=[[T3[i][j] for j in J3] for i in L3]
Delta3=A3[0][0]*A3[1][1]-A3[0][1]*A3[1][0];assert Delta3
Adj3=[[A3[1][1],-A3[0][1]],[-A3[1][0],A3[0][0]]]
for prod in [mm(A3,Adj3),mm(Adj3,A3)]:
 for i in range(2):
  for j in range(2):assert prod[i][j]==(Delta3 if i==j else Z)
CA3=mm(C3,Adj3);AB3=mm(Adj3,B3)
ut=[[Z for _ in range(3)]];vt=[[Z] for _ in range(3)]
for j in range(2):ut[0][I3[j]]=-CA3[0][j]
ut[0][L3[0]]=Delta3
for i in range(2):vt[J3[i]][0]=-AB3[i][0]
vt[K3[0]][0]=Delta3
assert all(not x for row in mm(ut,T3) for x in row)
assert all(not x for row in mm(T3,vt) for x in row)
lr3,lc3=lcmpolys(rs3),lcmpolys(cs3)
ur=[[ut[0][j]*exdiv(lr3,rs3[j]) for j in range(3)]]
vr=[[exdiv(lc3,cs3[i])*vt[i][0]] for i in range(3)]
def primitive_vector(v):
 g=Z
 for x in v:
  if x:g=x if not g else g.gcd(x)
 assert g
 return [exdiv(x,g) for x in v],g
ur[0],discardU=primitive_vector(ur[0])
vp,discardV=primitive_vector([x[0] for x in vr]);vr=[[x] for x in vp]
assert all(not x for row in mm(ur,Second) for x in row)
assert all(not x for row in mm(Second,vr) for x in row)
alpha,beta=ur[0][L3[0]],vr[K3[0]][0];assert alpha and beta
l8=mm(ur,Uh);r8=mm(Vh,vr)
l8[0],gLeft=primitive_vector(l8[0])
vp,gRight=primitive_vector([x[0] for x in r8]);r8=[[x] for x in vp]
assert all(not x for row in mm(l8,S) for x in row)
assert all(not x for row in mm(S,r8) for x in row)
LL=mm(l8,U);RR=mm(V,r8)
JH1=[[H1[i][j] for j in J] for i in range(n)]
IH1=[[H1[i][j] for j in range(n)] for i in I]
JH2=[[H2[i][j] for j in J] for i in range(n)]
IH2=[[H2[i][j] for j in range(n)] for i in I]
X1=mm(LL,JH1);Y1=mm(IH1,RR)
X2=mm(LL,JH2);Y2=mm(IH2,RR)
Aone=[[H1[i][j] for j in J] for i in I]
def scalar(M):assert len(M)==len(M[0])==1;return M[0][0]
zero2=Delta*scalar(mm(mm(LL,H2),RR))-scalar(mm(mm(X1,Adj),Y1))
assert not zero2
# Complete third term from the first14 block, including the A1
# contribution from the first derivative of A(t)^-1.
third14=(Delta**2)*scalar(mm(mm(LL,H3),RR))
third14-=Delta*(scalar(mm(mm(X2,Adj),Y1))+scalar(mm(mm(X1,Adj),Y2)))
third14+=scalar(mm(mm(mm(mm(X1,Adj),Aone),Adj),Y1))
# The second5 pivot is an ACTUAL submatrix of S1, not of its
# content-normalized copy. Return its inverse with all scales.
dC5=lcmpolys([cscale[j] for j in J2])
dR5=lcmpolys([rscale[i] for i in I2])
Adj5=[[exdiv(dC5,cscale[J2[i]])*Adj2[i][j]*exdiv(dR5,rscale[I2[j]])
       for j in range(5)] for i in range(5)]
Delta5=Delta2*dC5*dR5
A5=[[S[i][j] for j in J2] for i in I2]
for prod in [mm(A5,Adj5),mm(Adj5,A5)]:
 for i in range(5):
  for j in range(5):assert prod[i][j]==(Delta5 if i==j else Z)
VJ=[[V[i][j] for j in J2] for i in range(n)]
UI=[U[i][:] for i in I2]
row2a=mm(mm(LL,H2),VJ)
row2b=mm(mm(X1,Adj),mm(IH1,VJ))
Row2=[[Delta*x-y for x,y in zip(row2a[0],row2b[0])]]
col2a=mm(mm(UI,H2),RR)
col2b=mm(mm(mm(UI,JH1),Adj),Y1)
Col2=[[Delta*col2a[i][0]-col2b[i][0]] for i in range(5)]
third5=scalar(mm(mm(Row2,Adj5),Col2))
Third=Delta5*third14-third5
def polyprofile(poly):
 return dict(degree=int(poly.degree()),terms=sum(bool(x) for x in poly.coeffs()),
             sha256=hashlib.sha256(str(poly).encode()).hexdigest())
# The mathematical degree result is complete here. Record it
# before the additional exact leading-coefficient cancellation.
say("new_complete_third_scalar_before_leading_coefficient",
 fixedEarlierRanks=[14,5,2],lastKernelMinorRows=I3,lastKernelMinorColumns=J3,
 finalMinorSelectionSamples=last_samples,
 new2AdjugateReturns=8,newFinalKernelReturns=6,
 transferredFinalKernelReturns=6,completeSecond5InverseReturns=50,
 lowerSecondTermOnFinalKernelActuallyZero=True,
 thirdJetMatrixSHA256=digest(H3),
 fullThird14Term=polyprofile(third14),
 completeSecond5Correction=polyprofile(third5),
 actualCompleteThirdScalar=polyprofile(Third),
 actualCompleteThirdScalarZero=not Third,
 exactGlobalQQ_uDegree=(790 if Third else 789),
 previousModularDegree789UsedOnlyAsLowerBound=True,
 totalExactPolynomialDivisionReturns=returns,
 allPhysicalQZeroFibersRetained=True,wholeH42ZeroRetained=True,
 oldThreeEightTwentyTwoRanksNotReplayed=True,
 wholePhiExcluded=False,ordinaryISPClaim=False)
# Recover the actual u790 coefficient of the original fixed B22.
# This also distinguishes a true QQ degree790 with a Q2/p1009
# degree drop from the vanishing third scalar / exact degree789.
def permutation_sign(seq):
 return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1
sgn=permutation_sign(I+L)*permutation_sign(J+K)
sgn*=permutation_sign(I2+L2)*permutation_sign(J2+K2)
sgn*=permutation_sign(I3+L3)*permutation_sign(J3+K3)
det14=(-1 if swaps%2 else 1)*Delta
det5=(-1 if swaps2%2 else 1)*Delta2
for i in I2:det5=det5*rscale[i]
for j in J2:det5=det5*cscale[j]
det2=Second[I3[0]][J3[0]]*Second[I3[1]][J3[1]]-Second[I3[0]][J3[1]]*Second[I3[1]][J3[0]]
assert det14 and det5 and det2
detU=fmpq_poly([1]);detV=fmpq_poly([1])
for i in range(3):
 for j in range(3):
  assert Uh[i][L2[j]]==(Uh[i][L2[i]] if i==j else Z)
  assert Vh[K2[i]][j]==(Vh[K2[i]][i] if i==j else Z)
 detU=detU*Uh[i][L2[i]];detV=detV*Vh[K2[i]][i]
leading=Z;leadingDenDegreeBeforeCancel=-1
if Third:
 num=sgn*det14*det5*det2*Third*gLeft*gRight
 den=(Delta**20)*Delta5*detU*detV*alpha*beta
 assert den
 leadingDenDegreeBeforeCancel=int(den.degree())
 gg=num.gcd(den);num=exdiv(num,gg);den=exdiv(den,gg)
 # This is an actual original QQ[Q] coefficient, not a new
 # function-field weight inverse. All denominator factors cancel.
 assert int(den.degree())==0
 leading=exdiv(num,den);assert leading
p=1009
def qmod(q):
 ab=str(q).split("/");a=int(ab[0]);b=int(ab[1]) if len(ab)>1 else 1
 assert b%p
 return (a%p)*pow(b%p,-1,p)%p
for c in leading.coeffs():qmod(c)
leading_values=[]
for q in [2,3,5,7]:
 val=evalq(leading,q);leading_values.append(dict(Q=q,QQZero=not val,mod1009=qmod(val)))
assert leading_values[0]["mod1009"]==0
exact_degree=790 if Third else 789
slice_Q2_degree=789 if not evalq(leading,2) else 790
say("new_actual_third_scalar_and_exact_original_degree",
 fixedEarlierRanks=[14,5,2],lastKernelMinorRows=I3,lastKernelMinorColumns=J3,
 finalMinorSelectionSamples=last_samples,
 new2AdjugateReturns=8,newFinalKernelReturns=6,
 transferredFinalKernelReturns=6,
 completeSecond5InverseReturns=50,
 lowerSecondTermOnFinalKernelActuallyZero=True,
 thirdJetMatrixSHA256=digest(H3),
 fullThird14Term=polyprofile(third14),
 completeSecond5Correction=polyprofile(third5),
 actualCompleteThirdScalar=polyprofile(Third),
 actualCompleteThirdScalarZero=not Third,
 actualOriginal_u790Coefficient=polyprofile(leading),
 actualOriginalLeadingCoefficientDenominatorFullyCanceled=True,
 originalLeadingCoefficientDenDegreeBeforeCancel=leadingDenDegreeBeforeCancel,
 actualOriginal_u790CoefficientValues=leading_values,
 exactGlobalQQ_uDegree=exact_degree,
 exactQQ_Q2SliceDegree=slice_Q2_degree,
 alreadyPaidOriginalQ2p1009Degree=789,
 Q2p1009PreservesGlobalDegree=(exact_degree==789),
 Q2p1009PreservesQQ_Q2SliceDegree=(slice_Q2_degree==789),
 totalExactPolynomialDivisionReturns=returns,
 allPhysicalQZeroFibersRetained=True,wholeH42ZeroRetained=True,
 originalModularDeterminantNotReplayed=True,
 oldThreeEightTwentyTwoRanksNotReplayed=True,
 wholePhiExcluded=False,ordinaryISPClaim=False,
 noRecomputableMatrixOrPolynomialPayloadSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)
