#!/usr/bin/env python3
"""NEW unlowered original 22-column Phi weight determinant.
Lift the already fixed 18 ORIGINAL columns before lambda reduction,
and append C6,lambda*C6,T*C6,z*C6. Only old weight denominators are
cleared; H42 is never inverted. Exact QQ entry u-degrees and a full
Hungarian dual give a determinant degree upper bound. Its true Q=2,
p=1009 highest matrix and fixed polynomial determinant are new inputs.
A deficient highest matrix is recorded as an unclosed degree gap.
No old 18-column selection, QQ determinant, projection or rank gate.
120 seconds /1 GiB inclusive of all necessary definition prefixes.
2026-11-28 Asia/Taipei.
"""
import os,time,json,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import nmod_poly
START=time.perf_counter();DEADLINE=START+120
signal.setitimer(signal.ITIMER_REAL,120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
name="2026-11-28-unit211-Phi-zero-monic-six-eighteen-original-columns-and-nonzero-weight-determinant-8542.py"
path=Path(os.environ.get("ISP_PHI_EIGHTEEN_SOURCE",str(Path(__file__).with_name(name))))
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="f62613154879f17f529c7f441b34eede870606f89e714cd1b7e6dc4c6357a401"
mark=b"\np=1009\n";assert raw.count(mark)==1
prefix=raw.split(mark)[0]
assert len(prefix)==5956
assert hashlib.sha256(prefix).hexdigest()=="94105fe17b4e239867c7969ad7e620eca5be074b00c15cb898b2cbdcc02481fb"
sc={"__file__":str(path),"__name__":"new_original_unlowered_22_definition_only"}
oa=signal.alarm;ot=signal.setitimer
def bounded_timer(which,seconds,interval=0):
 if which!=signal.ITIMER_REAL:return ot(which,seconds,interval)
 left=max(.001,DEADLINE-time.perf_counter())
 return ot(which,min(left,float(seconds) if seconds>0 else left),0)
def bounded_alarm(seconds):return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+":only-nine-original-definitions","exec"),sc)
finally:
 signal.alarm=oa;signal.setitimer=ot
 ot(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
R,ctx,one,zero,geo=[sc[x] for x in ["R","ctx","one","zero","geo"]]
seeds,MT,Mz,C6,profile=[sc[x] for x in ["seeds","MT","Mz","C6","profile"]]
lam=R(ctx.from_dict({(0,0,1,0,0):1}))
def action(row,kind):
 if kind=="lambda":return [x*lam for x in row]
 A=MT if kind=="T" else Mz
 out=[R(),R(),R()]
 for j in range(3):
  for k in range(3):out[j]=out[j]+row[k]*A[k][j]
 return out
columns=[list(r) for r in seeds]
descriptors=[dict(seed=i,action=None) for i in range(9)]
for i,kind in [(0,"lambda"),(0,"T"),(0,"z"),
               (1,"lambda"),(1,"T"),(1,"z"),
               (3,"lambda"),(3,"T"),(5,"lambda")]:
 columns.append(action(seeds[i],kind))
 descriptors.append(dict(seed=i,action=kind))
columns.extend([[R(C6),R(),R()],[R(C6)*lam,R(),R()],
                [R(),R(C6),R()],[R(),R(),R(C6)]])
descriptors.extend([dict(originalC6Multiplier=x) for x in ["1","lambda","T","z"]])
assert len(columns)==22
# The first18 rows retain the already fixed low basis. Last4 rows are
# lambda6,lambda7,lambda6*T,lambda6*z. Last4 column block has
# diag(h,h,h,h), one off-diagonal c5, and no head inverse.
def coordinate(component,degree):
 if degree<6:return component*6+degree
 if component==0 and degree==6:return 18
 if component==0 and degree==7:return 19
 if component==1 and degree==6:return 20
 if component==2 and degree==6:return 21
 raise AssertionError(("outside original22 basis",component,degree))
def exact(a,b):
 q=a/b;assert q*b==a
 return q
def vp_integer(a,p):
 if a==0:return 10**9
 a=abs(a);v=0
 while a%p==0:a//=p;v+=1
 return v
def fraction_pair(q):
 ab=str(q).split("/")
 return int(ab[0]),int(ab[1]) if len(ab)>1 else 1
p=1009;Q0=2
assert all(p%d for d in range(2,math.isqrt(p)+1))
def qmod(q):
 a,b=fraction_pair(q);assert b%p
 return (a%p)*pow(b%p,-1,p)%p
N=22
weights=[[-1]*N for _ in range(N)]
coefficient_lists=[[[] for _ in range(N)] for _ in range(N)]
column_returns=[]
for j,row in enumerate(columns):
 den=one
 for value in row:
  assert geo["weight_only"](value.d)
  geo["legal"](value,False)
  den=exact(den,den.gcd(value.d))*value.d
 polys=[value.n*exact(den,value.d) for value in row]
 for k in range(3):assert R(polys[k])==row[k]*R(den)
 vals=[vp_integer(fraction_pair(c)[0],p)-vp_integer(fraction_pair(c)[1],p)
       for poly in polys for c in poly.to_dict().values() if c]
 assert vals
 pv=min(vals)
 scalar=R(p**(-pv)) if pv<=0 else R(1)/R(p**pv)
 # This is a nonzero rational constant, not a new parameter inverse.
 assert scalar.n.total_degree()==0 and scalar.d.total_degree()==0
 scaled=[exact(poly*scalar.n,scalar.d) for poly in polys]
 for k in range(3):assert R(scaled[k])==row[k]*R(den)*scalar
 for component,poly in enumerate(scaled):
  for ex,c in poly.to_dict().items():
   assert not ex[3] and not ex[4]
   degree=int(ex[2]);i=coordinate(component,degree)
   du,dq=int(ex[0]),int(ex[1])
   weights[i][j]=max(weights[i][j],du)
   while len(coefficient_lists[i][j])<=du:coefficient_lists[i][j].append(0)
   coefficient_lists[i][j][du]=(coefficient_lists[i][j][du]+qmod(c)*pow(Q0,dq,p))%p
 column_returns.append(dict(index=j,source=descriptors[j],
   originalDenominatorLCM=profile(den),
   pGaussConstantExponent=-pv,
   clearedThreeRows=[profile(x) for x in scaled],
   allThreeOldWeightClearingReturns=True))
 say("new_original_22_column_exact_clear",**column_returns[-1])
A=[[nmod_poly(coefficient_lists[i][j],p) for j in range(N)] for i in range(N)]
# Fixed exact Hungarian minimization of minus the genuine QQ u-degree.
# Its dual is checked on EVERY nonzero QQ entry, not only selected edges.
BIG=10**8
cost=[[(-weights[i][j] if weights[i][j]>=0 else BIG) for j in range(N)] for i in range(N)]
uu=[0]*(N+1);vv=[0]*(N+1);match=[0]*(N+1);way=[0]*(N+1)
for i in range(1,N+1):
 match[0]=i;j0=0;minv=[BIG*10]*(N+1);used=[False]*(N+1)
 while True:
  used[j0]=True;i0=match[j0];delta=BIG*10;j1=0
  for j in range(1,N+1):
   if not used[j]:
    cur=cost[i0-1][j-1]-uu[i0]-vv[j]
    if cur<minv[j]:minv[j]=cur;way[j]=j0
    if minv[j]<delta:delta=minv[j];j1=j
  assert j1
  for j in range(N+1):
   if used[j]:uu[match[j]]+=delta;vv[j]-=delta
   else:minv[j]-=delta
  j0=j1
  if match[j0]==0:break
 while True:
  j1=way[j0];match[j0]=match[j1];j0=j1
  if j0==0:break
perm=[None]*N
for j in range(1,N+1):perm[match[j]-1]=j-1
assert all(weights[i][perm[i]]>=0 for i in range(N))
dualrow=[-uu[i+1] for i in range(N)]
dualcol=[-vv[j+1] for j in range(N)]
upper=sum(dualrow)+sum(dualcol)
assert upper==sum(weights[i][perm[i]] for i in range(N))
for i in range(N):
 for j in range(N):
  if weights[i][j]>=0:assert weights[i][j]<=dualrow[i]+dualcol[j]
H=[]
for i in range(N):
 row=[]
 for j in range(N):
  d=dualrow[i]+dualcol[j]
  row.append(int(A[i][j][d]) if d>=0 else 0)
 H.append(row)
def scalar_det(matrix):
 C=[r[:] for r in matrix];det=1;rank=0
 for j in range(len(C)):
  pivot=next((i for i in range(j,len(C)) if C[i][j]),None)
  if pivot is None:return 0,rank
  if pivot!=j:C[j],C[pivot]=C[pivot],C[j];det=-det
  c=C[j][j];det=det*c%p;iv=pow(c,-1,p);rank+=1
  for i in range(j+1,len(C)):
   f=C[i][j]*iv%p
   if f:
    for k in range(j,len(C)):C[i][k]=(C[i][k]-f*C[j][k])%p
 return det%p,rank
lead,leading_pivots=scalar_det(H)
say("new_original_22_QQ_u_degree_complete_assignment",
 prime=p,Q=Q0,QQ_u_degree_upper_bound=upper,
 assignment=perm,dualRows=dualrow,dualColumns=dualcol,
 everyNonzeroQQEntryDualVerified=True,
 actualQ2HighestDeterminant=lead,
 leadingEliminationPivots=leading_pivots,
 globalAndSliceDegreeAlreadyProved=bool(lead),
 noUnknownH42Inverse=True,noOld18PointSelectionExecuted=True)
# New actual fixed22 determinant in Fp[u]. Every Bareiss division is
# multiplied back. The output is the specialization of the fixed
# QQ matrix, even where a temporary polynomial pivot vanishes.
Z=nmod_poly([],p);O=nmod_poly([1],p)
C=[r[:] for r in A];previous=O;sign=1;returns=0;swaps=0
for k in range(N-1):
 pivotrow=next((i for i in range(k,N) if C[i][k]),None)
 if pivotrow is None:
  determinant=Z
  say("new_original_22_fixed_polynomial_determinant_zero",
      firstNoPivotColumn=k,QQDegreeOnlyUpperBound=upper,
      noGlobalEmptinessClaim=True)
  break
 if pivotrow!=k:
  C[k],C[pivotrow]=C[pivotrow],C[k];sign=-sign;swaps+=1
 pivot=C[k][k]
 for i in range(k+1,N):
  ik=C[i][k]
  for j in range(k+1,N):
   num=pivot*C[i][j]-ik*C[k][j]
   quotient,remainder=divmod(num,previous)
   assert not remainder and quotient*previous==num
   returns+=1;C[i][j]=quotient
  C[i][k]=Z
 previous=pivot
 say("new_original_22_fixed_polynomial_Bareiss_step",
     step=k,pivotDegree=int(pivot.degree()),
     completeExactDivisionReturns=returns)
else:determinant=C[-1][-1]*sign
degree=int(determinant.degree())
assert degree<=upper
if lead:
 assert degree==upper and int(determinant[degree])==lead
coeffs=[int(x) for x in determinant.coeffs()]
digest=hashlib.sha256(json.dumps(coeffs,separators=(",",":")).encode()).hexdigest()
point_matrix=[[int(A[i][j](3)) for j in range(N)] for i in range(N)]
pointdet,_=scalar_det(point_matrix)
assert int(determinant(3))==pointdet
say("new_original_22_fixed_weight_determinant_degree_return",
 prime=p,Q=Q0,actualModularDegree=degree,
 actualModularLeadingCoefficient=int(determinant[degree]) if degree>=0 else 0,
 actualPolynomialSHA256=digest,
 QQ_u_degree_upper_bound=upper,
 gapFromInitialAssignment=upper-degree,
 QQExactDegreeAndWholeSlicePreserved=bool(lead),
 actualDeterminantAtU3=pointdet,
 allBareissExactDivisionReturns=returns,rowSwaps=swaps,
 fixedOriginalColumnSources=descriptors,
 basis="old18 low coordinates then lambda6,lambda7,lambda6T,lambda6z",
 SchurIdentityBeforeOldWeightScalings="det22=h^4 det18",
 allInputDenominatorsOnlyOldPaidWeights=True,
 H42NotInverted=True,wholeH42ZeroRetained=True,
 wholePhiExcluded=False,ordinaryISPClaim=False,
 noRecomputablePolynomialOrMatrixPayloadSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)
